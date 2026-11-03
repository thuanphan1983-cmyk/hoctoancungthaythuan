# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - TẠO TOÀN BỘ 43 ĐỀ THI ĐỘC LẬP 100%
Đảm bảo:
- Mỗi bài 3 đề (hoặc 5 đề ôn tập) hoàn toàn khác nhau 100%
- Không trùng lặp câu hỏi, số liệu, chất và đáp án
- Bám sát 100% từng bài học SGK KNTT
- Không có tiền tố thừa 'Đề X - '
"""

import sys
import json
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

print("Helper functions ready for Chem 8.")
