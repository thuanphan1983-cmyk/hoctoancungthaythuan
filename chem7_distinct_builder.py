# -*- coding: utf-8 -*-
"""
GENERATOR HÓA 7 ĐỘC LẬP 100%
Đảm bảo:
1. Tất cả các đề trong cùng 1 bài hoàn toàn khác nhau 100% về câu hỏi, số liệu, chất và đáp án.
2. Nội dung bám sát 100% từng bài học SGK Kết nối tri thức.
3. Không có dấu '**', không có tiền tố 'Đề X - '.
4. Không có dòng chờ điền đáp án ở Phần III.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": prompt.strip(),
        "statements": [
            {"subId": s[0], "text": s[1].strip(), "correct": s[2]} for s in statements
        ],
        "explanation": explanation.strip()
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "correctAnswer": str(answer).strip(),
        "explanation": explanation.strip()
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

print("Base loaded.")
