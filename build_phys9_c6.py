# -*- coding: utf-8 -*-
"""
BUILDER FOR CHƯƠNG VI: ÁNH SÁNG - VẬT LÝ 9 (KNTT)
Gồm 6 bài học / chuyên đề ôn tập (20 đề thi độc lập 100%):
- phys9_c6_b17: Bài 17: Hiện tượng khúc xạ ánh sáng (3 đề)
- phys9_c6_b18: Bài 18: Hiện tượng phản xạ toàn phần (3 đề)
- phys9_c6_b19: Bài 19: Thấu kính (3 đề)
- phys9_c6_b20: Bài 20: Thực hành xác định tiêu cự của thấu kính hội tụ (3 đề)
- phys9_c6_b21: Bài 21: Kính lúp (3 đề)
- phys9_c6_rev: [Đề tổng hợp] Ôn tập cuối Chương VI (5 đề)
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

def make_exam(ch_id, ch_title, l_id, l_name, t, p1, p2, p3, p4):
    return {
        "title": f"Đề kiểm tra KHTN 9 (Vật lý) - {l_name} - Đề số {t:02d}",
        "grade": "9",
        "subject": "physics",
        "subjectName": "Vật lý",
        "chapterId": ch_id,
        "chapterTitle": ch_title,
        "lessonId": l_id,
        "lessonName": l_name,
        "testNum": t,
        "duration": "45 phút",
        "points": 10.0,
        "part1": p1,
        "part2": p2,
        "part3": p3,
        "part4": p4
    }

def build_c6():
    exams_c6 = {}
    from data_phys9_c6_b17 import exams as e_b17
    from data_phys9_c6_b18 import exams as e_b18
    from data_phys9_c6_b19 import exams as e_b19
    from data_phys9_c6_b20 import exams as e_b20
    from data_phys9_c6_b21 import exams as e_b21
    from data_phys9_c6_rev import exams as e_rev

    exams_c6.update(e_b17)
    exams_c6.update(e_b18)
    exams_c6.update(e_b19)
    exams_c6.update(e_b20)
    exams_c6.update(e_b21)
    exams_c6.update(e_rev)
    return exams_c6

if __name__ == "__main__":
    exs = build_c6()
    print("Chapter VI total exams:", len(exs))
