# -*- coding: utf-8 -*-
# generate_all_c5_part2.py
import sys
import os

# We will write the full build_phys8_c5_part2.py file directly with 14 unique exams
target = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt\build_phys8_c5_part2.py"

with open(target, "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
"""
CHƯƠNG V - PHẦN 2 (14 ĐỀ THI ĐỘC LẬP 100%):
- phys8_c5_b23: Bài 23: Tác dụng của dòng điện (3 đề)
- phys8_c5_b24: Bài 24: Cường độ dòng điện và hiệu điện thế (3 đề)
- phys8_c5_b25: Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế (3 đề)
- phys8_c5_rev: [Đề tổng hợp] Ôn tập cuối Chương V (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid, "level": level, "question": q_text,
        "options": options, "correct": correct_idx, "explanation": explanation
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid, "level": level, "question": prompt,
        "statements": [{"subId": s[0], "text": s[1], "correct": s[2]} for s in statements],
        "explanation": explanation
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid, "level": level, "question": q_text,
        "correctAnswer": str(answer).strip(), "explanation": explanation
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid, "level": "Vận dụng cao", "question": q_text,
        "options": options, "correct": correct_idx, "explanation": explanation
    }

def get_c5_part2_exams():
    exams = {}
    ch_id = "phys8_c5"
    ch_title = "Chương V: Điện"

    def meta(l_id, l_name, t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
''')

print("Header written.")
