# -*- coding: utf-8 -*-
"""
==============================================================================
AUTO EXAM GENERATOR - HỆ THỐNG TỰ ĐỘNG SINH KHO ĐỀ KIỂM TRA TOÁN THCS (KNTT)
Tự động duyệt 190 bài học Toán 6, 7, 8, 9 x 3 đề phân hóa = 570 đề thi chuẩn ma trận 2025.
Sử dụng mô hình gemini-3.8-flash tốc độ cao và hạn mức API lớn, phù hợp sinh số lượng lớn.

TÍNH NĂNG MỚI NÂNG CẤP:
1. LUÂN PHIÊN API KEY (Key Rotation):
   - Cho phép khai báo mảng API_KEYS = ['key1', 'key2', 'key3', ...]
   - Tự động bắt lỗi 429 (Rate Limit) hoặc ResourceExhausted để lập tức đổi sang
     Key tiếp theo trong mảng và thử lại lệnh vừa thất bại mà không bị ngắt chương trình.
2. KIỂM SOÁT NHỊP ĐỘ (Rate Limiter):
   - Nghỉ đủ 75 giây (time.sleep(75)) sau khi sinh xong MỖI đề thi.
   - Đảm bảo an toàn tuyệt đối, không bao giờ chạm ngưỡng 15 requests/phút của bản Gemini Free Tier.
3. TỰ ĐỘNG PHỤC HỒI & CHẠY XUYÊN ĐÊM:
   - Checkpoint tiến độ sau từng đề thi, tự động khôi phục khi chạy lại.
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

# ==============================================================================
# 0. KHAI BÁO MẢNG API KEYS CHO CƠ CHẾ LUÂN PHIÊN (KEY ROTATION)
# ==============================================================================
# Quý thầy cô/người dùng có thể dán trực tiếp danh sách Key vào mảng dưới đây,
# hoặc khai báo trong file .env (GEMINI_API_KEYS=key1,key2,key3),
# hoặc truyền qua tham số dòng lệnh: --api-key "key1,key2,key3"
API_KEYS = [
    # "AIzaSyD-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_1",
    # "AIzaSyD-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_2",
    # "AIzaSyD-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_3",
]

# Mô hình mặc định: gemini-3.8-flash (hạn mức API cao, tốc độ nhanh, phù hợp sinh số lượng lớn)
DEFAULT_MODEL = "gemini-3.8-flash"
CANDIDATE_MODELS = [
    "gemini-3.8-flash",
    "gemini-3.1-pro-preview"
]

# Thư mục gốc của dự án
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, "src", "data")
OUTPUT_DIR = os.path.join(DATA_DIR, "generated")
PROGRESS_FILE = os.path.join(DATA_DIR, "generator_progress.json")
CURRICULUM_FILE = os.path.join(PROJECT_ROOT, "curriculum.js")
EXISTING_C1_8_FILE = os.path.join(PROJECT_ROOT, "chapter1Toan8Exams.js")

# Biến cờ dừng an toàn khi người dùng nhấn Ctrl+C
STOP_REQUESTED = False

def handle_sigint(sig, frame):
    global STOP_REQUESTED
    print("\n\n🛑 [TẠM DỪNG] Đã nhận tín hiệu dừng (Ctrl+C). Đang lưu lại tiến độ...")
    STOP_REQUESTED = True

signal.signal(signal.SIGINT, handle_sigint)


# ==============================================================================
# LỚP QUẢN LÝ VÀ LUÂN PHIÊN API KEYS (KEY ROTATOR)
# ==============================================================================
class KeyRotator:
    """
    Quản lý mảng API Keys và điều phối luân phiên vòng tròn:
    - Lưu danh sách keys hợp lệ
    - Tự động chuyển key tiếp theo khi gặp 429 / ResourceExhausted
    - In thông báo đổi key rõ ràng kèm mã key che bớt bảo mật
    """
    def __init__(self, key_list):
        self.keys = []
        for k in key_list:
            if k:
                # Làm sạch chuỗi key
                clean = str(k).strip().strip('"').strip("'").strip()
                if clean and clean not in self.keys:
                    self.keys.append(clean)
        self.current_idx = 0

    def count(self):
        return len(self.keys)

    def get_current_key(self):
        if not self.keys:
            return ""
        return self.keys[self.current_idx % len(self.keys)]

    def get_masked_key(self, idx=None):
        if not self.keys:
            return "Chưa có Key"
        target_idx = self.current_idx if idx is None else idx
        k = self.keys[target_idx % len(self.keys)]
        if len(k) > 10:
            masked = f"{k[:6]}...{k[-4:]}"
        else:
            masked = "******"
        return f"Key #{target_idx + 1}/{len(self.keys)} [{masked}]"

    def rotate_next(self, reason="Rate Limit 429"):
        if not self.keys:
            return ""
        prev_idx = self.current_idx
        self.current_idx = (self.current_idx + 1) % len(self.keys)
        new_masked = self.get_masked_key()
        prev_masked = self.get_masked_key(prev_idx)

        print("\n" + "!" * 75)
        print(f"🔄 [LUÂN PHIÊN API KEY - {reason.upper()}]")
        print(f"   ⚠️ Key vừa bị lỗi : {prev_masked}")
        print(f"   🚀 Chuyển sang    : {new_masked}")
        print(f"   👉 Tiếp tục thử lại ngay lệnh vừa thất bại mà KHÔNG dừng chương trình!")
        print("!" * 75 + "\n")
        return self.get_current_key()


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
- Phần III (Trả lời ngắn): 4 câu hỏi phức tạp (tìm giá trị cực trị min/max, số nghiệm nguyên, bài toán tổ hợp logic hoặc tỉ số diện tích nâng cao).
- Phần IV (Tự luận):
  + Câu 1 (1.0đ): Vận dụng nâng cao về rút gọn biểu thức có điều kiện, biến đổi đẳng thức phức tạp.
  + Câu 2 (1.0đ): Bài toán hình học chứng minh nhiều bước hoặc bài toán thực tế giải bằng lập phương trình/hệ phương trình nâng cao.
  + Câu 3 (1.0đ): CÂU ĐIỂM 10 PHÂN HÓA HSG (Bất đẳng thức Cauchy/Schwarz, cực trị đại số, phương trình nghiệm nguyên, hoặc tìm m để biểu thức đạt giá trị nguyên/lớn nhất/nhỏ nhất)."""
        }
    }

    spec = difficulty_specs[test_num]

    prompt = f"""Bạn là Chuyên gia Khảo thí và Giáo viên giỏi môn Toán THCS (Chương trình GDPT 2018 - SGK Kết nối tri thức với cuộc sống).
Hãy soạn 01 đề kiểm tra môn TOÁN LỚP {grade} theo đúng chuẩn ma trận đề thi 2025 của Bộ Giáo dục & Đào tạo.

THÔNG TIN BÀI HỌC VÀ CHUYÊN ĐỀ:
- Khối lớp: Toán {grade}
- Chương: {chapter['title']} (Mã: {chapter['id']})
- Bài học / Chuyên đề: {lesson}
- Mức độ biên soạn: {spec['name']}

{spec['rules']}

QUY ĐỊNH CẤU TRÚC ĐỀ THI BẮT BUỘC (TỔNG 10.0 ĐIỂM - ĐẦY ĐỦ 4 PHẦN):
1. PHẦN I: Câu trắc nghiệm nhiều phương án lựa chọn (3.0 điểm)
   - Gồm ĐÚNG 12 câu hỏi (mỗi câu 0.25 điểm).
   - Mỗi câu có 4 phương án A, B, C, D (options là mảng 4 chuỗi, trong đó đúng 1 đáp án chính xác).
   - correct: chỉ số từ 0 đến 3 (0=A, 1=B, 2=C, 3=D).

2. PHẦN II: Câu trắc nghiệm đúng/sai (2.0 điểm)
   - Gồm ĐÚNG 2 câu hỏi (mỗi câu 1.0 điểm).
   - Mỗi câu gồm 1 phần dẫn (stem) và 4 lệnh hỏi con a, b, c, d (statements).
   - Mỗi lệnh con có: key ("a", "b", "c", "d"), level, text, correct (true hoặc false).

3. PHẦN III: Câu trắc nghiệm trả lời ngắn (2.0 điểm)
   - Gồm ĐÚNG 4 câu hỏi (mỗi câu 0.5 điểm).
   - Học sinh chỉ điền kết quả số (số nguyên hoặc số thập phân gọn gàng, hoặc phân số tối giản).
   - answer: chuỗi kết quả số chính xác (ví dụ "15", "-3.5", "2024").

4. PHẦN IV: Tự luận (3.0 điểm)
   - Gồm ĐÚNG 3 bài toán (mỗi bài 1.0 điểm).
   - Mỗi bài có: question và rubric (hướng dẫn chấm chi tiết, barem điểm từng bước giải).

ĐẶC BIỆT LƯU Ý VỀ ĐỊNH DẠNG TOÁN HỌC:
- Mọi công thức toán học PHẢI được bọc trong cặp dấu $...$ (ví dụ: $x^2 - 4x + 4$, $\\frac{{a}}{{b}}$, $\\sqrt{{x}}$).
- Sử dụng dấu gạch chéo ngược hợp lệ trong JSON (ví dụ: \\\\frac, \\\\sqrt, \\\\le, \\\\ge, \\\\in).
- Toàn bộ nội dung trả về là MỘT ĐỐI TƯỢNG JSON DUY NHẤT, KHÔNG kèm lời dẫn, KHÔNG bọc mã ngoài ```json ```.

CẤU TRÚC JSON CHUẨN MẪU:
{{
  "title": "Toán {grade} (KNTT) - {lesson} - Bài kiểm tra số {test_num}",
  "part1": [
    {{ "id": 1, "level": "Nhận biết", "question": "...", "options": ["...", "...", "...", "..."], "correct": 0 }}
  ],
  "part2": [
    {{
      "id": 1,
      "stem": "...",
      "statements": [
        {{ "key": "a", "level": "Thông hiểu", "text": "...", "correct": true }},
        {{ "key": "b", "level": "Thông hiểu", "text": "...", "correct": false }},
        {{ "key": "c", "level": "Vận dụng thấp", "text": "...", "correct": true }},
        {{ "key": "d", "level": "Vận dụng cao", "text": "...", "correct": false }}
      ]
    }}
  ],
  "part3": [
    {{ "id": 1, "level": "Thông hiểu", "question": "...", "answer": "12" }}
  ],
  "part4": [
    {{ "id": 1, "level": "Vận dụng thấp", "question": "...", "rubric": "Bước 1 (0.5đ): ...\\nBước 2 (0.5đ): ..." }}
  ]
}}
"""
    return prompt.strip()


# ==============================================================================
# 4. HÀM GỌI API GEMINI VỚI CƠ CHẾ LUÂN PHIÊN KEY & CHỐNG RATE LIMIT
# ==============================================================================
def safe_extract_json(text):
    """Trích xuất và làm sạch chuỗi JSON từ phản hồi của LLM"""
    if not text:
        return None
    text = text.strip()

    # Bóc tách code block ```json ... ```
    m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if m:
        text = m.group(1).strip()

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


def call_gemini_api(key_rotator, prompt, model_name=DEFAULT_MODEL, timeout=150, max_retries=12):
    """
    Gọi Gemini API tích hợp 2 tính năng cốt lõi:
    1. LUÂN PHIÊN KEY (Key Rotation):
       - Tự động bắt lỗi 429 (Rate Limit) hoặc ResourceExhausted.
       - Tự động in thông báo đổi Key và lấy Key tiếp theo trong mảng để thử lại ngay mà không ngắt chương trình.
    2. CHỐNG TREO & SERVER BUSY:
       - Tự động chuyển model dự phòng nếu server bận (503/500).
       - Timeout 150s cho đề thi dài.
    """
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
        current_key = key_rotator.get_current_key()
        masked_key = key_rotator.get_masked_key()

        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": current_key
        }
        params = {
            "key": current_key
        }

        try:
            response = requests.post(
                endpoint,
                headers=headers,
                params=params,
                json=payload,
                timeout=timeout
            )
            status_code = response.status_code
            resp_text = response.text

            # ------------------------------------------------------------------
            # THÀNH CÔNG: HTTP 200
            # ------------------------------------------------------------------
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

            # ------------------------------------------------------------------
            # BẮT LỖI 429 RATE LIMIT HOẶC RESOURCE EXHAUSTED -> TỰ ĐỘNG ĐỔI KEY
            # ------------------------------------------------------------------
            elif status_code == 429 or "RESOURCE_EXHAUSTED" in resp_text or "ResourceExhausted" in resp_text:
                if key_rotator.count() > 1:
                    # Có nhiều key -> Luân phiên ngay sang key tiếp theo và thử lại lập tức!
                    key_rotator.rotate_next(reason="Rate Limit 429 / ResourceExhausted")
                    time.sleep(2)
                    continue
                else:
                    # Chỉ có 1 key duy nhất -> Bắt buộc chờ hồi quota
                    backoff_time = min(120, int(25 * (1.5 ** min(attempt, 4)) + random.uniform(2, 6)))
                    print(f"\n    ⏳ [RATE LIMIT 429] Đạt ngưỡng giới hạn với {masked_key}.")
                    print(f"       Tự động tạm dừng {backoff_time}s trước khi tiếp tục...")
                    for s in range(backoff_time, 0, -1):
                        if STOP_REQUESTED:
                            return None
                        sys.stdout.write(f"\r       Đang chờ hồi quota: {s}s còn lại...   ")
                        sys.stdout.flush()
                        time.sleep(1)
                    print()
                    continue

            # ------------------------------------------------------------------
            # BẮT LỖI KEY KHÔNG HỢP LỆ (HTTP 400) -> TỰ ĐỘNG ĐỔI KEY
            # ------------------------------------------------------------------
            elif status_code == 400 and ("API_KEY_INVALID" in resp_text or "API key not valid" in resp_text):
                print(f"\n    ❌ [LỖI API KEY] {masked_key} không hợp lệ!")
                if key_rotator.count() > 1:
                    key_rotator.rotate_next(reason="API Key Invalid (400)")
                    time.sleep(2)
                    continue
                else:
                    print("    ❌ Không còn Key hợp lệ nào khác. Vui lòng kiểm tra lại API Key!")
                    return None

            # ------------------------------------------------------------------
            # BẮT LỖI MODEL 404 NOT FOUND
            # ------------------------------------------------------------------
            elif status_code == 404:
                print(f"\n    ❌ [HTTP 404 NOT FOUND] URL: {endpoint}")
                model_idx += 1
                next_model = models_to_try[model_idx % len(models_to_try)]
                print(f"       Tự động đổi sang mô hình: {next_model}...")
                time.sleep(3)
                continue

            # ------------------------------------------------------------------
            # BẮT LỖI MÁY CHỦ BẬN (500, 502, 503, 504)
            # ------------------------------------------------------------------
            elif status_code in (500, 502, 503, 504):
                print(f"\n    ⚠️ [SERVER BUSY {status_code}] Mô hình {model} đang quá tải.")
                model_idx += 1
                next_model = models_to_try[model_idx % len(models_to_try)]
                print(f"       Tự động chuyển sang model: {next_model} (chờ 8s)...")
                time.sleep(8)
                continue

            else:
                print(f"\n    ⚠️ [HTTP {status_code}] Lỗi yêu cầu: {resp_text[:150]}. Thử lại sau 10s...")
                time.sleep(10)

        # ----------------------------------------------------------------------
        # CÁC NGOẠI LỆ KHI GỌI MẠNG / THƯ VIỆN SUBPROCESS HOẶC REQUESTS
        # ----------------------------------------------------------------------
        except requests.exceptions.Timeout:
            print(f"\n    ⏳ [READ TIMEOUT > {timeout}s] Gemini đang xử lý đề thi dài. Tự động thử lại sau 8s...")
            time.sleep(8)

        except requests.exceptions.RequestException as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str or "ResourceExhausted" in err_str:
                if key_rotator.count() > 1:
                    key_rotator.rotate_next(reason="Exception RateLimit 429")
                    time.sleep(2)
                    continue
            print(f"\n    🌐 [NETWORK ERROR] Lỗi kết nối mạng ({e}). Tự động thử lại sau 12s...")
            time.sleep(12)

        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "ResourceExhausted" in err_str:
                if key_rotator.count() > 1:
                    key_rotator.rotate_next(reason="General Exception 429")
                    time.sleep(2)
                    continue
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
// Tự động sinh bởi Antigravity Auto Exam Generator (Mô hình: gemini-3.8-flash)
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
def run_generator(key_rotator, target_grade="all", target_chapter="all", model_name=DEFAULT_MODEL, delay=75, timeout=150, force=False):
    """
    Vòng lặp chính duyệt qua khung chương trình và sinh đề thi.
    Tích hợp kiểm soát nhịp độ Rate Limiter: Bắt buộc time.sleep(75) sau mỗi đề thi.
    """
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
    print(f"🤖 Mô hình AI chuẩn     : {model_name} (Hỗ trợ logic Toán học tốt nhất)")
    print(f"🔑 Tổng số API Keys nạp : {key_rotator.count()} Key (Cơ chế Luân phiên Key Rotation)")
    print(f"📌 Tổng số bài học chọn : {total_lessons} bài")
    print(f"📌 Tổng số đề cần sinh  : {total_tasks} đề (3 đề phân hóa / bài)")
    print(f"✅ Đã có sẵn / hoàn thành: {len(all_tasks) - len(remaining_tasks)} đề")
    print(f"⏳ Cần sinh mới tiếp tục: {len(remaining_tasks)} đề")
    print(f"⏱️ KIỂM SOÁT NHỊP ĐỘ     : Nghỉ đủ {delay}s sau MỖI đề thi (Bảo vệ hạn mức 15 RPM Free Tier)")
    print(f"⏳ Thời gian chờ timeout : {timeout}s (cho phép tạo đủ 4 phần chuẩn ma trận)")
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
        print(f"    🔑 Key hiện tại: {key_rotator.get_masked_key()} | Mã đề: {exam_key}")

        prompt = build_prompt(grade, ch, lesson, test_num)
        exam_data = call_gemini_api(key_rotator, prompt, model_name=model_name, timeout=timeout)

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

            # ==================================================================
            # KIỂM SOÁT NHỊP ĐỘ (RATE LIMITER): BẮT BUỘC NGHỈ ĐỦ 75 GIÂY SAU MỖI ĐỀ
            # ==================================================================
            sleep_time = max(delay, 75)
            print(f"    ⏳ [RATE LIMITER] Nghỉ đủ {sleep_time}s sau khi sinh xong đề thi...")
            print(f"       (Đảm bảo không bao giờ vượt ngưỡng 15 requests/phút của bản Gemini Free Tier)")
            for s in range(sleep_time, 0, -1):
                if STOP_REQUESTED:
                    break
                sys.stdout.write(f"\r       Đang đếm lùi nhịp độ an toàn: {s:02d}s còn lại...   ")
                sys.stdout.flush()
                time.sleep(1)
            print()
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
        description="Auto Exam Generator - Tự động biên soạn kho đề kiểm tra Toán THCS qua Gemini AI với Key Rotation & Rate Limiter"
    )
    parser.add_argument("--api-key", "--api-keys", "-k", type=str, help="Một hoặc nhiều Google Gemini API Key (cách nhau bởi dấu phẩy)")
    parser.add_argument("--model", "-m", type=str, default=DEFAULT_MODEL, help=f"Mô hình Gemini (mặc định: {DEFAULT_MODEL})")
    parser.add_argument("--grade", "-g", type=str, default="all", choices=["6", "7", "8", "9", "all"], help="Khối lớp (6, 7, 8, 9 hoặc all)")
    parser.add_argument("--chapter", "-c", type=str, default="all", help="ID chương cụ thể (ví dụ: c1_8, c2_8, c1_9...)")
    parser.add_argument("--delay", "-d", type=int, default=75, help="Thời gian nghỉ (giây) giữa các lần tạo đề (mặc định 75s - Kiểm soát nhịp độ Rate Limiter)")
    parser.add_argument("--timeout", "-t", type=int, default=150, help="Thời gian chờ timeout tối đa cho mỗi yêu cầu API (giây, mặc định: 150s)")
    parser.add_argument("--force", "-f", action="store_true", help="Sinh lại cả các đề đã có sẵn")

    args = parser.parse_args()

    collected_keys = []

    # 1. Lấy từ mảng API_KEYS khai báo sẵn ở đầu file (nếu có)
    for k in API_KEYS:
        if k and isinstance(k, str) and k.strip():
            collected_keys.append(k.strip())

    # 2. Lấy từ tham số CLI
    if args.api_key:
        for k in args.api_key.split(","):
            if k.strip():
                collected_keys.append(k.strip())

    # 3. Lấy từ biến môi trường
    env_keys = os.environ.get("GEMINI_API_KEYS") or os.environ.get("GEMINI_API_KEY")
    if env_keys:
        for k in env_keys.split(","):
            if k.strip():
                collected_keys.append(k.strip())

    # 4. Lấy từ file .env
    env_file = os.path.join(PROJECT_ROOT, ".env")
    if os.path.exists(env_file):
        try:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    line_s = line.strip()
                    if line_s.startswith("GEMINI_API_KEYS=") or line_s.startswith("GEMINI_API_KEY="):
                        val = line_s.split("=", 1)[1].strip().strip('"').strip("'")
                        for k in val.split(","):
                            if k.strip():
                                collected_keys.append(k.strip())
        except Exception:
            pass

    # 5. Nếu chưa có Key nào, cho phép người dùng nhập trực tiếp
    if not collected_keys:
        print("=" * 75)
        print("🔑 THIẾT LẬP GOOGLE GEMINI API KEYS (HỖ TRỢ NHIỀU KEYS)")
        print("=" * 75)
        print("Mẹo: Bạn có thể nhập nhiều Key cách nhau bởi dấu phẩy để bật tính năng luân phiên:")
        print("Ví dụ: AIzaSyD-xxx1, AIzaSyD-xxx2, AIzaSyD-xxx3")
        raw_input = input(">> Dán mã Gemini API Key vào đây: ").strip()
        if raw_input:
            for k in raw_input.split(","):
                if k.strip():
                    collected_keys.append(k.strip())

    if not collected_keys:
        print("❌ Lỗi: Không thể chạy nếu không có ít nhất một API Key hợp lệ. Chương trình kết thúc.")
        sys.exit(1)

    key_rotator = KeyRotator(collected_keys)

    run_generator(
        key_rotator=key_rotator,
        target_grade=args.grade,
        target_chapter=args.chapter,
        model_name=args.model,
        delay=args.delay,
        timeout=args.timeout,
        force=args.force
    )


if __name__ == "__main__":
    main()
