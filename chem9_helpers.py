# -*- coding: utf-8 -*-
"""
Helper functions for Chemistry 9 Exam Generation (KNTT)
"""

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    assert len(options) == 4, f"MC Q{qid} must have 4 options"
    assert 0 <= correct_idx <= 3, f"MC Q{qid} correct index must be 0..3"
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    assert len(statements) == 4, f"TF Q{qid} must have 4 statements"
    return {
        "id": qid,
        "level": level,
        "question": prompt.strip(),
        "statements": [
            {"subId": s[0], "text": s[1].strip(), "correct": bool(s[2])} for s in statements
        ],
        "explanation": explanation.strip()
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    assert not ("Đáp số:" in q_text or "Đáp số : " in q_text), f"SA Q{qid} must not contain 'Đáp số:'"
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "correctAnswer": str(answer).strip(),
        "explanation": explanation.strip()
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    assert len(options) == 4, f"VDC Q{qid} must have 4 options"
    assert 0 <= correct_idx <= 3, f"VDC Q{qid} correct index must be 0..3"
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

def make_exam(chapter_id, chapter_title, lesson_id, lesson_name, test_num, p1, p2, p3, p4):
    assert len(p1) == 12, f"part1 must have 12 questions in {lesson_id}_test{test_num}"
    assert len(p2) == 4, f"part2 must have 4 questions in {lesson_id}_test{test_num}"
    assert len(p3) == 6, f"part3 must have 6 questions in {lesson_id}_test{test_num}"
    assert len(p4) == 4, f"part4 must have 4 questions in {lesson_id}_test{test_num}"
    return {
        "title": f"Đề kiểm tra KHTN 9 (Hóa học) - {lesson_name} - Đề số {test_num:02d}",
        "grade": "9",
        "subject": "chemistry",
        "subjectName": "Hóa học",
        "chapterId": chapter_id,
        "chapterTitle": chapter_title,
        "lessonId": lesson_id,
        "lessonName": lesson_name,
        "testNum": test_num,
        "duration": "45 phút",
        "points": 10.0,
        "part1": p1,
        "part2": p2,
        "part3": p3,
        "part4": p4
    }
