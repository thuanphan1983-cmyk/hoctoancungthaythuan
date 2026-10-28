# -*- coding: utf-8 -*-
"""
GENERATOR UTILS - BỘ CÔNG CỤ SINH VÀ ĐÓNG GÓI ĐỀ THI TOÁN THCS (KNTT)
Tuân thủ tuyệt đối quy định ma trận khảo thí 2025:
- Đề 1 & 2 (Khá): 40% Nhận biết, 30% Thông hiểu, 20% Vận dụng, 10% Vận dụng cao.
- Đề 3 (Khá Giỏi): 20% Nhận biết, 30% Thông hiểu, 30% Vận dụng, 20% Vận dụng cao.
- Ràng buộc cấu trúc:
  + Phần II: Trong mỗi câu lớn (4 ý a,b,c,d), BẮT BUỘC có đúng 1 ý Vận dụng.
  + Phần III: Trong 4 câu hỏi, BẮT BUỘC có đúng 2 câu Vận dụng.
"""

import os
import sys
import json
import re
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
OUTPUT_DIR = os.path.join(PROJECT_DIR, "src", "data", "generated")
MANIFEST_PATHS = [
    os.path.join(PROJECT_DIR, "manifest.json"),
    os.path.join(PROJECT_DIR, "dist", "manifest.json")
]

def is_vd(level_str):
    """Kiểm tra mức độ Vận dụng (không bao gồm Vận dụng cao)"""
    l = str(level_str).lower().strip()
    return "vận dụng" in l and "cao" not in l

def is_vdc(level_str):
    """Kiểm tra mức độ Vận dụng cao"""
    l = str(level_str).lower().strip()
    return "cao" in l or "vdc" in l

def make_mc(q_id, level, question, options, correct, explanation=""):
    assert len(options) == 4, f"Câu {q_id} phải có đúng 4 phương án!"
    assert correct in [0, 1, 2, 3], f"Câu {q_id} có đáp án correct không hợp lệ: {correct}"
    letters = ["A", "B", "C", "D"]
    if not explanation:
        explanation = f"Phương án đúng là **{letters[correct]}**. Căn cứ vào định nghĩa và tính chất của bài học."
    return {
        "id": q_id,
        "level": level,
        "question": question,
        "options": options,
        "correct": correct,
        "explanation": explanation
    }

def make_tf(q_id, stem, statements):
    assert len(statements) == 4, f"Phần II Câu {q_id} phải có đúng 4 ý a,b,c,d!"
    vd_count = sum(1 for s in statements if is_vd(s.get("level", "")) or is_vdc(s.get("level", "")))
    assert vd_count == 1, f"Phần II Câu {q_id} BẮT BUỘC có đúng 1 ý Vận dụng (hiện có {vd_count})!"
    
    formatted = []
    for s in statements:
        k = s.get("key", "a")
        c = bool(s.get("correct"))
        exp = s.get("explanation", "")
        if not exp:
            exp = f"Ý {k.upper()} là **{'Đúng' if c else 'Sai'}** theo quy tắc và tính chất bài học."
        formatted.append({
            "key": k,
            "level": s.get("level", "Thông hiểu"),
            "text": s.get("text", ""),
            "correct": c,
            "explanation": exp
        })
    return {
        "id": q_id,
        "stem": stem,
        "statements": formatted
    }

def make_sa(q_id, level, question, answer, acceptable=None, explanation=""):
    ans_str = str(answer).strip()
    if acceptable is None:
        acceptable = [ans_str]
    elif ans_str not in acceptable:
        acceptable.insert(0, ans_str)
    
    if not explanation:
        explanation = f"Các bước giải chi tiết dẫn đến kết quả: **{ans_str}**."
    return {
        "id": q_id,
        "level": level,
        "question": question,
        "answer": ans_str,
        "acceptableAnswers": acceptable,
        "explanation": explanation
    }

def make_essay(q_id, level, question, rubric):
    return {
        "id": q_id,
        "level": level,
        "question": question,
        "rubric": rubric
    }

def validate_exam(exam_id, exam_data, test_num):
    part1 = exam_data.get("part1", [])
    part2 = exam_data.get("part2", [])
    part3 = exam_data.get("part3", [])
    part4 = exam_data.get("part4", [])

    assert len(part1) == 12, f"[{exam_id}] Phần I phải có đúng 12 câu, hiện có {len(part1)}"
    assert len(part2) == 2, f"[{exam_id}] Phần II phải có đúng 2 câu lớn, hiện có {len(part2)}"
    assert len(part3) == 4, f"[{exam_id}] Phần III phải có đúng 4 câu, hiện có {len(part3)}"
    assert len(part4) == 3, f"[{exam_id}] Phần IV phải có đúng 3 bài tự luận, hiện có {len(part4)}"

    # Ràng buộc cấu trúc Phần II: mỗi câu lớn đúng 1 ý Vận dụng
    for q_idx, q in enumerate(part2, 1):
        stmts = q.get("statements", [])
        assert len(stmts) == 4, f"[{exam_id}] Phần II Câu {q_idx} phải có 4 ý con"
        vd_stmts = [s for s in stmts if is_vd(s.get("level", "")) or is_vdc(s.get("level", ""))]
        assert len(vd_stmts) == 1, f"[{exam_id}] Phần II Câu {q_idx} BẮT BUỘC đúng 1 ý Vận dụng (hiện có {len(vd_stmts)})"

    # Ràng buộc cấu trúc Phần III: đúng 2 câu Vận dụng (hơi khó)
    vd_sa = [q for q in part3 if is_vd(q.get("level", ""))]
    assert len(vd_sa) == 2, f"[{exam_id}] Phần III BẮT BUỘC đúng 2 câu Vận dụng (hiện có {len(vd_sa)})"

    return True

def save_chapter_package(grade, chapter_id, chapter_title, exams_dict):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    base_name = f"grade{grade}_{chapter_id}_exams"
    json_path = os.path.join(OUTPUT_DIR, f"{base_name}.json")
    js_path = os.path.join(OUTPUT_DIR, f"{base_name}.js")

    for key, exam in exams_dict.items():
        m = re.search(r'_test(\d+)$', key)
        t_num = int(m.group(1)) if m else 1
        validate_exam(key, exam, t_num)

    payload = {
        "grade": str(grade),
        "chapterId": chapter_id,
        "chapterTitle": chapter_title,
        "totalExams": len(exams_dict),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "exams": exams_dict
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    js_var_name = f"EXAMS_{str(grade).upper()}_{chapter_id.upper()}"
    js_content = f"""// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA {chapter_title.upper()} - TOÁN {grade} (KNTT)
// Chuẩn ma trận khảo thí 2025: Đề 1 & 2 (Khá 40/30/20/10), Đề 3 (Khá Giỏi 20/30/30/20)
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

    sync_manifest_for_chapter(grade, chapter_id, chapter_title, len(exams_dict), list(exams_dict.keys()))
    print(f"✅ [HOÀN TẤT ĐÓNG GÓI] Toán {grade} - {chapter_title} ({len(exams_dict)} đề kiểm tra chuẩn ma trận)")

def sync_manifest_for_chapter(grade, chapter_id, chapter_title, total_exams, exam_keys):
    ch_key = f"grade{grade}_{chapter_id}"
    base_name = f"grade{grade}_{chapter_id}_exams"
    
    for mp in MANIFEST_PATHS:
        try:
            if os.path.exists(mp):
                with open(mp, "r", encoding="utf-8") as f:
                    manifest = json.load(f)
            else:
                manifest = {}
            
            manifest[ch_key] = {
                "grade": str(grade),
                "chapterId": chapter_id,
                "chapterTitle": chapter_title,
                "totalExams": total_exams,
                "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "jsonFile": f"{base_name}.json",
                "jsFile": f"{base_name}.js",
                "jsonPath": f"src/data/generated/{base_name}.json",
                "jsPath": f"src/data/generated/{base_name}.js",
                "examKeys": exam_keys
            }
            os.makedirs(os.path.dirname(mp), exist_ok=True)
            with open(mp, "w", encoding="utf-8") as f:
                json.dump(manifest, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Cảnh báo khi cập nhật {mp}: {e}")
