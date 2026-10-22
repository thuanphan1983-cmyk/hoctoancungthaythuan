# -*- coding: utf-8 -*-
"""
==============================================================================
AUTO EXAM GENERATOR - HỆ THỐNG TỰ ĐỘNG SINH KHO ĐỀ KIỂM TRA TOÁN THCS (KNTT)
Tự động duyệt 190 bài học Toán 6, 7, 8, 9 x 3 đề phân hóa = 570 đề thi chuẩn ma trận 2025.
Sử dụng mô hình chuẩn gemini-1.5-pro hỗ trợ logic Toán học tốt nhất.
Tích hợp cơ chế tự phục hồi, chống lỗi (try-catch), tự động chờ (sleep/delay/backoff)
cho phép chạy miệt mài qua đêm mà không bị dừng đột ngột.
==============================================================================
"""

import os
import sys
import re
import json
import time
import signal
import random
import argparse
import requests
import urllib.request
import urllib.error
from datetime import datetime

# Đảm bảo hiển thị Unicode tiếng Việt trên Terminal Windows
sys.stdout.reconfigure(encoding='utf-8')

# Mô hình chuẩn cho logic Toán học (gemini-1.5-pro) và mô hình dự phòng (gemini-1.5-flash)
DEFAULT_MODEL = "gemini-1.5-pro"
CANDIDATE_MODELS = [
    "gemini-1.5-pro",
    "gemini-1.5-flash"
]

# Thư mục gốc của dự án
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, "src", "data")
OUTPUT_DIR = os.path.join(DATA_DIR, "generated")
PROGRESS_FILE = os.path.join(DATA_DIR, "generator_progress.json")
CURRICULUM_FILE = os.path.join(PROJECT_ROOT, "curriculum.js")
EXISTING_C1_8_FILE = os.path.join(PROJECT_ROOT, "chapter1Toan8Exams.js")

# Biến cờ dừng an toàn khi nhấn Ctrl+C
STOP_REQUESTED = False

def handle_sigint(sig, frame):
    global STOP_REQUESTED
    print("\n\n🛑 [TẠM DỪNG] Đã nhận tín hiệu dừng (Ctrl+C). Đang lưu lại tiến độ...")
    STOP_REQUESTED = True

signal.signal(signal.SIGINT, handle_sigint)


# ==============================================================================
# 1. HÀM ĐỌC KHUNG CHƯƠNG TRÌNH TỪ CURRICULUM.JS
# ==============================================================================
def load_curriculum():
    """Đọc và bóc tách toàn bộ danh mục Khối, Chương, Bài từ curriculum.js"""
    if not os.path.exists(CURRICULUM_FILE):
        raise FileNotFoundError(f"Không tìm thấy file chương trình: {CURRICULUM_FILE}")

    with open(CURRICULUM_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    curriculum = {}
    grades = ["6", "7", "8", "9"]

    for g in grades:
        pos = text.find(f'"{g}":')
        if pos == -1:
            pos = text.find(f"'{g}':")
        if pos == -1:
            continue

        next_pos = -1
        for next_g in grades[grades.index(g) + 1:]:
            p = text.find(f'"{next_g}":', pos)
            if p != -1:
                next_pos = p
                break
        if next_pos == -1:
            next_pos = text.rfind("};")
        
        block = text[pos:next_pos]
        ch_matches = re.finditer(
            r'\{\s*id\s*:\s*["\']([^"\']+)["\'],\s*title\s*:\s*["\']([^"\']+)["\'],\s*lessons\s*:\s*\[(.*?)\]\s*\}',
            block,
            re.DOTALL
        )

        chapters = []
        for cm in ch_matches:
            ch_id = cm.group(1).strip()
            ch_title = cm.group(2).strip()
            raw_lessons = cm.group(3)
            lessons = [
                l.strip().strip('"').strip("'")
                for l in re.findall(r'["\']([^"\']+)["\']', raw_lessons)
            ]
            chapters.append({
                "id": ch_id,
                "title": ch_title,
                "lessons": lessons
            })

        curriculum[g] = chapters

    return curriculum


# ==============================================================================
# 2. HÀM QUẢN LÝ TIẾN ĐỘ & CHECKPOINT
# ==============================================================================
def load_progress():
    """Tải tiến độ các bài đã sinh xong từ generator_progress.json"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Không đọc được file tiến độ cũ ({e}), tạo mới.")

    return {
        "completed_exams": {},
        "last_updated": None,
        "stats": {
            "total_completed": 0,
            "failed_attempts": 0
        }
    }


def save_progress(progress):
    """Lưu tiến độ ngay lập tức xuống đĩa"""
    progress["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    progress["stats"]["total_completed"] = len(progress["completed_exams"])
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def sync_existing_c1_8_exams(progress):
    """Đồng bộ 18 đề kiểm tra Chương 1 Toán 8 đã có sẵn vào tiến độ"""
    if os.path.exists(EXISTING_C1_8_FILE):
        try:
            with open(EXISTING_C1_8_FILE, "r", encoding="utf-8") as f:
                content = f.read()
            m = re.findall(r'"(c1_8_bai\d+_test\d+)":\s*\{', content)
            added = 0
            for k in m:
                if k not in progress["completed_exams"]:
                    progress["completed_exams"][k] = {
                        "grade": "8",
                        "chapterId": "c1_8",
                        "source": "prebuilt_chapter1Toan8Exams.js",
                        "completed_at": "pre-existing"
                    }
                    added += 1
            if added > 0:
                print(f"ℹ️ Đã đồng bộ {added} đề thi có sẵn từ Chương 1 Toán 8 vào tiến độ kiểm tra!")
                save_progress(progress)
        except Exception as e:
            print(f"⚠️ Không đọc được {EXISTING_C1_8_FILE}: {e}")


# ==============================================================================
# 3. HÀM XÂY DỰNG PROMPT CHUẨN MA TRẬN BỘ GD&ĐT PHÂN HÓA 3 ĐỀ
# ==============================================================================
def build_prompt(grade, chapter, lesson, test_num):
    """Xây dựng prompt chi tiết chuẩn sư phạm bám sát phân hóa Bloom 3 cấp độ"""
    is_chapter_exam = "cuối chương" in lesson.lower() or "ôn tập" in lesson.lower()

    difficulty_specs = {
        1: {
            "name": "ĐỀ SỐ 1 - MỨC ĐỘ CƠ BẢN & CỦNG CỐ NỀN TẢNG (Mục tiêu 5.0 - 7.0 điểm)",
            "rules": """
YÊU CẦU ĐỘ KHÓ ĐỀ SỐ 1 (MỨC ĐỘ DỄ NHẤT):
- Bám sát chuẩn kiến thức kỹ năng cơ bản SGK Kết nối tri thức. Các câu hỏi hỏi trực tiếp, rõ ràng, không gài bẫy.
- Phần I (Trắc nghiệm): 8 câu Nhận biết (khái niệm trực tiếp, hệ số, nghiệm có sẵn), 4 câu Thông hiểu đơn giản (thay số 1 bước).
- Phần II (Đúng/Sai): 2 câu ở mức Thông hiểu cơ bản, các mệnh đề dễ phân biệt đúng/sai, lập luận ngắn gọn.
- Phần III (Trả lời ngắn): 4 câu tính toán số học / đại số 1-2 bước cơ bản.
- Phần IV (Tự luận): 3 câu mẫu mực như ví dụ cơ bản trong SGK, lời giải rõ ràng, dễ đạt điểm."""
        },
        2: {
            "name": "ĐỀ SỐ 2 - MỨC ĐỘ KHÁ & VẬN DỤNG LINH HOẠT (Mục tiêu 7.0 - 8.5 điểm - KHÓ HƠN ĐỀ 1 RÕ RỆT)",
            "rules": """
YÊU CẦU ĐỘ KHÓ ĐỀ SỐ 2 (ĐỘ KHÓ TRUNG BÌNH KHÁ - KHÓ HƠN ĐỀ 1):
- Đòi hỏi học sinh phải biết kết hợp từ 2 kiến thức trở lên, thực hiện biến đổi đại số nhiều bước, phân tích bài toán thực tế mức độ khá.
- Phần I (Trắc nghiệm): 4 câu Nhận biết (hỏi sâu hơn), 8 câu Thông hiểu (có phương án nhiễu dễ nhầm lẫn, yêu cầu biến đổi rút gọn trước khi chọn).
- Phần II (Đúng/Sai): 2 câu phân tích đa bước (chứa biểu thức quy đồng, tìm điều kiện tham số cơ bản, đối chiếu ĐKXĐ).
- Phần III (Trả lời ngắn): 4 câu hỏi yêu cầu giải phương trình, rút gọn có điều kiện, tính toán thực tế hoặc tỉ số hình học.
- Phần IV (Tự luận): Bài toán thực tế rõ ràng (toán chuyển động, toán năng suất, tỉ số lượng giác thực tế) và bài toán biến đổi có ràng buộc điều kiện."""
        },
        3: {
            "name": "ĐỀ SỐ 3 - MỨC ĐỘ NÂNG CAO & PHÂN HÓA SÂU (Mục tiêu 8.5 - 10.0 điểm - KHÓ NHẤT, KHÓ HƠN ĐỀ 2 VÀ ĐỀ 1)",
            "rules": """
YÊU CẦU ĐỘ KHÓ ĐỀ SỐ 3 (ĐỘ KHÓ CAO NHẤT, PHÂN HÓA MẠNH MẼ CHO HSG VÀ THI VÀO LỚP 10):
- Đòi hỏi tư duy logic trừu tượng, biến đổi đại số khéo léo, xử lý tham số m, bài toán cực trị, bất đẳng thức hoặc bài toán hình học phân tích sâu.
- Phần I (Trắc nghiệm): 2 câu Nhận biết tinh tế, 6 câu Thông hiểu nâng cao, 4 câu có bẫy logic sâu (dễ mất nghiệm hoặc nhầm lẫn miền xác định).
- Phần II (Đúng/Sai): 2 câu phân tích đa chiều (chứa tham số m, biện luận số nghiệm, tính chất hình học nâng cao).
- Phần III (Trả lời ngắn): 4 câu ở mức Vận dụng cao (tìm giá trị tham số, bài toán cực trị hình học, biểu thức đối xứng Viète nâng cao, bài toán đếm hoặc xác suất phức tạp).
- Phần IV (Tự luận): 
  * Câu 1: Bài toán biến đổi / rút gọn nâng cao có chứa tham số hoặc điều kiện nghiệm (1.0đ).
  * Câu 2: Bài toán thực tế phức tạp đa bước lập phương trình/hệ phương trình hoặc hình học phân tích nâng cao (1.0đ).
  * Câu 3: Câu chốt phân hóa điểm 10 (1.0đ) - Bất đẳng thức, tìm GTLN/GTNN, bài toán cực trị hình học, hoặc phương trình nghiệm nguyên nâng cao."""
        }
    }

    diff = difficulty_specs[test_num]

    chapter_context = ""
    if is_chapter_exam:
        other_lessons = [l for l in chapter["lessons"] if l != lesson]
        chapter_context = f"""
LƯU Ý ĐẶC BIỆT (ĐỀ KIỂM TRA TỔNG HỢP TOÀN BỘ CHƯƠNG):
- Đây là bài kiểm tra TỔNG HỢP KIẾN THỨC TOÀN BỘ CHƯƠNG: "{chapter['title']}".
- Đề thi PHẢI tổng hợp toàn diện, bao quát và phân bổ đều kiến thức trọng tâm của TẤT CẢ các bài học trong chương: {', '.join(other_lessons)}.
"""

    prompt = f"""
Bạn là chuyên gia khảo thí và biên soạn đề thi môn Toán THCS bộ sách "Kết nối tri thức với cuộc sống".
Hãy tạo trọn vẹn bộ đề kiểm tra định kỳ cho:
- Khối: Toán {grade} (Bộ sách Kết nối tri thức với cuộc sống)
- Chương: "{chapter['title']}"
- Bài học / Chuyên đề: "{lesson}"
- Bộ đề số: "Bài kiểm tra số {test_num}"

{diff['name']}
{diff['rules']}
{chapter_context}

QUY ĐỊNH CÔNG THỨC TOÁN & ĐỊNH DẠNG JSON:
1. Mọi công thức toán học, biểu thức đại số, phân thức, căn thức, hệ phương trình PHẢI được bọc chuẩn LaTeX giữa hai dấu $ (ví dụ: $2x + 3y = 5$, $\\sqrt{{x^2 - 1}}$, $\\frac{{a}}{{b}}$).
2. Hãy thoát hợp lệ ký tự gạch chéo ngược LaTeX trong chuỗi JSON (ví dụ viết \\\\frac thay vì \\frac).
3. ĐẦU RA PHẢI LÀ MỘT ĐỐI TƯỢNG JSON DUY NHẤT HỢP LỆ, KHÔNG KÈM LỜI GIẢI THÍCH NGOÀI LỀ.

CẤU TRÚC JSON BẮT BUỘC (ĐỦ 4 PHẦN TỔNG 10.0 ĐIỂM):
{{
  "title": "Toán {grade} (KNTT) - {lesson} - Bài kiểm tra số {test_num}",
  "part1": [ // Đúng 12 câu trắc nghiệm 4 lựa chọn (0.25đ/câu = 3.0đ). "correct" là chỉ số 0, 1, 2, hoặc 3
    {{ "id": 1, "level": "Nhận biết", "question": "...", "options": ["$A...$", "$B...$", "$C...$", "$D...$"], "correct": 0 }}
  ],
  "part2": [ // Đúng 2 câu Đúng/Sai (1.0đ/câu = 2.0đ). Mỗi câu có phần dẫn chung (stem) và 4 ý a, b, c, d
    {{
      "id": 1,
      "stem": "...",
      "statements": [
        {{ "key": "a", "level": "Thông hiểu", "text": "...", "correct": true }},
        {{ "key": "b", "level": "Thông hiểu", "text": "...", "correct": false }},
        {{ "key": "c", "level": "Vận dụng thấp", "text": "...", "correct": true }},
        {{ "key": "d", "level": "Vận dụng thấp", "text": "...", "correct": false }}
      ]
    }}
  ],
  "part3": [ // Đúng 4 câu Trả lời ngắn (0.5đ/câu = 2.0đ). "answer" là một số nguyên, phân số hoặc số thập phân
    {{ "id": 1, "level": "Thông hiểu", "question": "...", "answer": "5" }}
  ],
  "part4": [ // Đúng 3 câu Tự luận (1.0đ/câu = 3.0đ). "rubric" là biểu điểm hướng dẫn chấm từng bước chi tiết
    {{ "id": 1, "level": "Thông hiểu", "question": "...", "rubric": "Bước 1 (0.5đ): ... Bước 2 (0.5đ): ..." }}
  ]
}}
"""
    return prompt.strip()


# ==============================================================================
# 4. HÀM GỌI API GEMINI VỚI CƠ CHẾ CHỐNG LỖI & EXPONENTIAL BACKOFF
# ==============================================================================
def safe_extract_json(raw_text):
    """Trích xuất và làm sạch chuỗi JSON từ phản hồi của Gemini"""
    if not raw_text:
        return None
    
    text = raw_text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
        text = text.strip()

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        text = text[start:end + 1]

    try:
        data = json.loads(text)
        return data
    except json.JSONDecodeError:
        try:
            sanitized = re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', text)
            return json.loads(sanitized)
        except Exception:
            return None


def call_gemini_api(api_key, prompt, model_name=DEFAULT_MODEL, max_retries=10):
    """
    Gọi Gemini API sử dụng model chuẩn gemini-1.5-pro bằng thư viện requests:
    - URL Endpoint chuẩn xác: https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent
    - Truyền đồng thời query parameter ?key= và header x-goog-api-key để đảm bảo xác thực 100%
    - 429 Rate Limit: Tự động sleep và exponential backoff có thanh đếm lùi
    - 503 High Demand: Tự động chờ và chuyển model dự phòng
    - Network timeout: Tự động thử lại
    """
    clean_key = api_key.strip().strip('"').strip("'").strip()

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0.35
        }
    }

    # Thứ tự ưu tiên: model_name chỉ định (gemini-1.5-pro), sau đó là các model hợp lệ khác
    models_to_try = [model_name]
    for m in CANDIDATE_MODELS:
        if m not in models_to_try:
            models_to_try.append(m)

    attempt = 0
    model_idx = 0

    while attempt < max_retries:
        if STOP_REQUESTED:
            return None

        attempt += 1
        model = models_to_try[model_idx % len(models_to_try)]
        
        # Endpoint chính thức theo chuẩn Google Generative Language API
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": clean_key
        }
        params = {
            "key": clean_key
        }

        try:
            response = requests.post(
                endpoint,
                headers=headers,
                params=params,
                json=payload,
                timeout=60
            )
            status_code = response.status_code

            if status_code == 200:
                res_json = response.json()
                raw_text = (
                    res_json.get("candidates", [{}])[0]
                    .get("content", {})
                    .get("parts", [{}])[0]
                    .get("text", "")
                )
                exam_data = safe_extract_json(raw_text)

                if (
                    exam_data
                    and len(exam_data.get("part1", [])) == 12
                    and len(exam_data.get("part2", [])) == 2
                    and len(exam_data.get("part3", [])) == 4
                    and len(exam_data.get("part4", [])) == 3
                ):
                    return exam_data
                else:
                    print(f"    ⚠️ Phản hồi từ {model} chưa đủ cấu trúc 4 phần, đang thử lại lần {attempt}...")
                    time.sleep(3)
                    continue

            elif status_code == 404:
                print(f"\n    ❌ [HTTP 404 NOT FOUND] URL: {endpoint}")
                print(f"       Chi tiết lỗi: {response.text[:200]}")
                model_idx += 1
                next_model = models_to_try[model_idx % len(models_to_try)]
                print(f"       Tự động đổi sang mô hình: {next_model}...")
                time.sleep(3)
                continue

            elif status_code == 429:
                backoff_time = min(120, int(20 * (1.6 ** min(attempt, 4)) + random.uniform(2, 6)))
                print(f"\n    ⏳ [RATE LIMIT 429] Đạt ngưỡng giới hạn gọi API ({model}).")
                print(f"       Tự động tạm dừng {backoff_time}s trước khi tiếp tục...")
                for s in range(backoff_time, 0, -1):
                    if STOP_REQUESTED:
                        return None
                    sys.stdout.write(f"\r       Đang chờ hồi quota: {s}s còn lại...   ")
                    sys.stdout.flush()
                    time.sleep(1)
                print()
                continue

            elif status_code in (500, 502, 503, 504):
                print(f"\n    ⚠️ [SERVER BUSY {status_code}] Mô hình {model} đang quá tải.")
                model_idx += 1
                next_model = models_to_try[model_idx % len(models_to_try)]
                print(f"       Tự động chuyển sang model: {next_model} (chờ 10s)...")
                time.sleep(10)
                continue

            elif status_code == 400 and ("API_KEY_INVALID" in response.text or "API key not valid" in response.text):
                print("\n    ❌ [LỖI API KEY] Mã Gemini API Key không hợp lệ. Vui lòng kiểm tra lại key!")
                return None

            else:
                print(f"\n    ⚠️ [HTTP {status_code}] Lỗi yêu cầu: {response.text[:150]}. Thử lại sau 15s...")
                time.sleep(15)

        except requests.exceptions.RequestException as e:
            print(f"\n    🌐 [NETWORK ERROR] Lỗi kết nối mạng hoặc timeout ({e}). Tự động thử lại sau 15s...")
            time.sleep(15)

        except Exception as e:
            print(f"\n    ⚠️ [ERROR] Lỗi không mong muốn: {e}. Thử lại sau 10s...")
            time.sleep(10)

    print(f"    ❌ Đã thử lại {max_retries} lần nhưng không thành công cho yêu cầu này.")
    return None


# ==============================================================================
# 5. HÀM LƯU ĐỀ THI RA FILE JS & JSON TRONG SRC/DATA/GENERATED/
# ==============================================================================
def save_chapter_exams(grade, chapter_id, chapter_title, exams_dict):
    """
    Lưu toàn bộ đề của một chương ra file riêng:
    1. src/data/generated/{grade}_{chapter_id}_exams.json
    2. src/data/generated/{grade}_{chapter_id}_exams.js (UMD module)
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    base_name = f"grade{grade}_{chapter_id}_exams"

    json_path = os.path.join(OUTPUT_DIR, f"{base_name}.json")
    js_path = os.path.join(OUTPUT_DIR, f"{base_name}.js")

    payload = {
        "grade": grade,
        "chapterId": chapter_id,
        "chapterTitle": chapter_title,
        "totalExams": len(exams_dict),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "exams": exams_dict
    }

    # Ghi file JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    # Ghi file JS (tương thích cả Browser qua window và Node.js qua module.exports)
    js_var_name = f"EXAMS_{grade.upper()}_{chapter_id.upper()}"
    js_content = f"""// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA {chapter_title.upper()} - TOÁN {grade} (KNTT)
// Tự động sinh bởi Antigravity Auto Exam Generator (Mô hình: gemini-1.5-pro)
// Cập nhật lúc: {payload['updatedAt']}
// ==============================================================================

const {js_var_name} = {json.dumps(exams_dict, ensure_ascii=False, indent=2)};

if (typeof window !== 'undefined') {{
  window.{js_var_name} = {js_var_name};
}}
if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ {js_var_name} }};
}}
"""
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    # Cập nhật manifest danh mục các chương đã sinh
    manifest_path = os.path.join(OUTPUT_DIR, "manifest.json")
    try:
        manifest = {}
        if os.path.exists(manifest_path):
            with open(manifest_path, "r", encoding="utf-8") as mf:
                manifest = json.load(mf)
        manifest[f"grade{grade}_{chapter_id}"] = {
            "grade": grade,
            "chapterId": chapter_id,
            "chapterTitle": chapter_title,
            "totalExams": len(exams_dict),
            "updatedAt": payload["updatedAt"],
            "jsFile": f"{base_name}.js",
            "jsonFile": f"{base_name}.json"
        }
        with open(manifest_path, "w", encoding="utf-8") as mf:
            json.dump(manifest, mf, ensure_ascii=False, indent=2)
    except Exception:
        pass


def load_existing_chapter_exams(grade, chapter_id):
    """Tải các đề đã có của chương nếu file đã tồn tại"""
    json_path = os.path.join(OUTPUT_DIR, f"grade{grade}_{chapter_id}_exams.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("exams", {})
        except Exception:
            return {}
    return {}


# ==============================================================================
# 6. HÀM ĐIỀU PHỐI CHÍNH (MAIN ORCHESTRATOR)
# ==============================================================================
def run_generator(api_key, target_grade="all", target_chapter="all", model_name=DEFAULT_MODEL, delay=4, force=False):
    """Vòng lặp chính duyệt qua khung chương trình và sinh đề thi"""
    curriculum = load_curriculum()
    progress = load_progress()
    sync_existing_c1_8_exams(progress)

    total_lessons = 0
    all_tasks = []

    for grade, chapters in curriculum.items():
        if target_grade != "all" and str(grade) != str(target_grade):
            continue

        for ch in chapters:
            if target_chapter != "all" and ch["id"] != target_chapter:
                continue

            for l_idx, lesson in enumerate(ch["lessons"], 1):
                total_lessons += 1
                for test_num in [1, 2, 3]:
                    exam_key = f"{ch['id']}_bai{l_idx}_test{test_num}"
                    all_tasks.append({
                        "grade": grade,
                        "chapter": ch,
                        "lesson": lesson,
                        "lesson_idx": l_idx,
                        "test_num": test_num,
                        "exam_key": exam_key
                    })

    total_tasks = len(all_tasks)
    completed_keys = set(progress["completed_exams"].keys())
    remaining_tasks = [t for t in all_tasks if force or t["exam_key"] not in completed_keys]

    print("\n" + "=" * 80)
    print("🚀 ANTIGRAVITY AUTO EXAM GENERATOR - KHỞI CHẠY HỆ THỐNG")
    print("=" * 80)
    print(f"🤖 Mô hình AI chuẩn: {model_name} (Hỗ trợ logic Toán học tốt nhất)")
    print(f"📌 Tổng số bài học trong phạm vi chọn: {total_lessons} bài")
    print(f"📌 Tổng số đề cần sinh (3 đề/bài): {total_tasks} đề")
    print(f"✅ Đã có sẵn / hoàn thành trước đó: {len(all_tasks) - len(remaining_tasks)} đề")
    print(f"⏳ Cần sinh mới tiếp tục: {len(remaining_tasks)} đề")
    print(f"⏱️ Thời gian trễ giữa các lượt: {delay}s (chống nghẽn rate limit)")
    print("=" * 80 + "\n")

    if not remaining_tasks:
        print("🎉 TẤT CẢ CÁC ĐỀ TRONG PHẠM VI CHỌN ĐÃ ĐƯỢC SINH HOÀN TẤT 100%!")
        return

    current_chapter_id = None
    chapter_exams = {}

    for idx, task in enumerate(remaining_tasks, 1):
        if STOP_REQUESTED:
            print("\n💾 Đã ngắt tiến trình an toàn theo yêu cầu người dùng.")
            break

        grade = task["grade"]
        ch = task["chapter"]
        lesson = task["lesson"]
        test_num = task["test_num"]
        exam_key = task["exam_key"]

        if ch["id"] != current_chapter_id:
            if current_chapter_id and chapter_exams:
                save_chapter_exams(prev_grade, current_chapter_id, prev_ch_title, chapter_exams)
            current_chapter_id = ch["id"]
            prev_grade = grade
            prev_ch_title = ch["title"]
            chapter_exams = load_existing_chapter_exams(grade, ch["id"])

        diff_label = ["", "Cơ bản", "Khá", "Nâng cao"][test_num]
        print(f"\n[{idx}/{len(remaining_tasks)}] Đang xử lý: Khối {grade} • {ch['title'][:30]}... • {lesson} • Đề {test_num} ({diff_label})")
        print(f"    🔑 Key: {exam_key} | Bắt đầu gọi {model_name}...")

        prompt = build_prompt(grade, ch, lesson, test_num)
        exam_data = call_gemini_api(api_key, prompt, model_name=model_name)

        if exam_data:
            chapter_exams[exam_key] = exam_data
            progress["completed_exams"][exam_key] = {
                "grade": grade,
                "chapterId": ch["id"],
                "lesson": lesson,
                "testNum": test_num,
                "title": exam_data.get("title", ""),
                "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            save_chapter_exams(grade, ch["id"], ch["title"], chapter_exams)
            save_progress(progress)

            print(f"    ✅ [THÀNH CÔNG] Đã lưu đề vào {OUTPUT_DIR}/grade{grade}_{ch['id']}_exams.json")
            print(f"    📊 Tổng hoàn thành: {len(progress['completed_exams'])}/{total_tasks} đề ({(len(progress['completed_exams'])/total_tasks)*100:.1f}%)")

            if idx < len(remaining_tasks):
                time.sleep(delay)
        else:
            print(f"    ⚠️ [BỎ QUA TẠM THỜI] Không thể sinh đề cho {exam_key}. Sẽ tiếp tục đề kế tiếp...")
            progress["stats"]["failed_attempts"] += 1
            save_progress(progress)
            time.sleep(5)

    if current_chapter_id and chapter_exams:
        save_chapter_exams(prev_grade, current_chapter_id, prev_ch_title, chapter_exams)
        save_progress(progress)

    print("\n" + "=" * 80)
    print("🏁 KẾT THÚC PHIÊN LÀM VIỆC CỦA AUTO EXAM GENERATOR")
    print(f"Tổng số đề đã sinh thành công: {len(progress['completed_exams'])} đề.")
    print(f"Dữ liệu được lưu trữ tại: {OUTPUT_DIR}")
    print("=" * 80)


# ==============================================================================
# 7. KHỞI CHẠY TỪ DÒNG LỆNH (CLI)
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="Auto Exam Generator - Tự động biên soạn kho đề kiểm tra Toán THCS qua Gemini AI"
    )
    parser.add_argument("--api-key", "-k", type=str, help="Google Gemini API Key")
    parser.add_argument("--model", "-m", type=str, default=DEFAULT_MODEL, help=f"Mô hình Gemini (mặc định: {DEFAULT_MODEL})")
    parser.add_argument("--grade", "-g", type=str, default="all", choices=["6", "7", "8", "9", "all"], help="Khối lớp (6, 7, 8, 9 hoặc all)")
    parser.add_argument("--chapter", "-c", type=str, default="all", help="ID chương cụ thể (ví dụ: c1_8, c2_8, c1_9...)")
    parser.add_argument("--delay", "-d", type=int, default=4, help="Thời gian nghỉ (giây) giữa các lần gọi API (mặc định 4s)")
    parser.add_argument("--force", "-f", action="store_true", help="Sinh lại cả các đề đã có sẵn")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")

    if not api_key:
        env_file = os.path.join(PROJECT_ROOT, ".env")
        if os.path.exists(env_file):
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("GEMINI_API_KEY="):
                        api_key = line.strip().split("=", 1)[1].strip().strip('"').strip("'")
                        break

    if not api_key:
        print("=" * 70)
        print("🔑 GOOGLE GEMINI API KEY CHƯA ĐƯỢC THIẾT LẬP")
        print("=" * 70)
        api_key = input("Vui lòng dán mã Gemini API Key của bạn vào đây: ").strip()

    if not api_key:
        print("❌ Lỗi: Không thể chạy nếu không có API Key. Chương trình kết thúc.")
        sys.exit(1)

    run_generator(
        api_key=api_key,
        target_grade=args.grade,
        target_chapter=args.chapter,
        model_name=args.model,
        delay=args.delay,
        force=args.force
    )


if __name__ == "__main__":
    main()
