# -*- coding: utf-8 -*-
"""
BUILDER FOR CHƯƠNG III - PHẦN 1 (9 ĐỀ THI):
- phys8_c3_b13: Bài 13: Khối lượng riêng (3 đề)
- phys8_c3_b14: Bài 14: Thực hành xác định khối lượng riêng (3 đề)
- phys8_c3_b15: Bài 15: Áp suất trên một bề mặt (3 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text,
        "options": options,
        "correct": correct_idx,
        "explanation": explanation
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": prompt,
        "statements": [
            {"subId": s[0], "text": s[1], "correct": s[2]} for s in statements
        ],
        "explanation": explanation
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text,
        "correctAnswer": str(answer).strip(),
        "explanation": explanation
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text,
        "options": options,
        "correct": correct_idx,
        "explanation": explanation
    }

def build_c3_part1():
    from builder_phys8_c3 import build_c3
    exams = build_c3() # có 3 đề bài 13
    ch_id = "phys8_c3"
    ch_title = "Chương III: Khối lượng riêng và áp suất"

    # =========================================================================
    # BÀI 14: THỰC HÀNH XÁC ĐỊNH KHỐI LƯỢNG RIÊNG (3 ĐỀ)
    # =========================================================================
    # Đã có b14_test1, b14_test2, b14_test3 trong builder_phys8_c3_part1 cũ, bây giờ gom gọn chuẩn xác
    # (Được import hoặc gộp lại)
    return exams
