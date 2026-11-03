# -*- coding: utf-8 -*-
"""
AUDIT TOÀN DIỆN CHO CHỦ ĐỀ 9, 10, 11 (TOÁN 5 KNTT)
Kiểm tra cấu trúc, thang điểm, tiêu đề, tính độc lập và số lượng 48 đề thi.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from th5_ch9_builder import get_exams as get_ch9_exams
from th5_ch10_builder import get_exams as get_ch10_exams
from th5_ch11_builder import get_exams as get_ch11_exams

def run_audit():
    ch9 = get_ch9_exams()
    ch10 = get_ch10_exams()
    ch11 = get_ch11_exams()
    
    print(f"[1] Số lượng đề thi:")
    print(f"  - Chủ đề 9: {len(ch9)} đề (kỳ vọng: 24)")
    print(f"  - Chủ đề 10: {len(ch10)} đề (kỳ vọng: 9)")
    print(f"  - Chủ đề 11: {len(ch11)} đề (kỳ vọng: 15)")
    total = len(ch9) + len(ch10) + len(ch11)
    print(f"  => Tổng cộng: {total} đề (kỳ vọng: 48 đề)")
    assert len(ch9) == 24, "Chủ đề 9 không đúng 24 đề"
    assert len(ch10) == 9, "Chủ đề 10 không đúng 9 đề"
    assert len(ch11) == 15, "Chủ đề 11 không đúng 15 đề"
    assert total == 48, "Tổng số đề không đúng 48"

    all_exams = {}
    all_exams.update(ch9)
    all_exams.update(ch10)
    all_exams.update(ch11)

    print("\n[2] Kiểm tra chi tiết từng đề thi:")
    expected_part2_points = [1.0, 1.0, 1.0, 1.5, 1.5, 1.0]

    for key, exam in all_exams.items():
        assert "id" in exam and exam["id"] == key, f"{key}: lỗi id"
        assert "lessonId" in exam, f"{key}: thiếu lessonId"
        assert "lessonNum" in exam, f"{key}: thiếu lessonNum"
        assert "testNum" in exam, f"{key}: thiếu testNum"
        assert "title" in exam and len(exam["title"]) > 0, f"{key}: thiếu title"
        assert exam["duration"] == "35 phút", f"{key}: duration không phải '35 phút'"
        assert exam["points"] == 10.0, f"{key}: points không phải 10.0"

        # Kiểm tra Phần 1 (Trắc nghiệm)
        p1 = exam["part1"]
        assert len(p1) == 6, f"{key}: Part 1 không đủ 6 câu ({len(p1)})"
        for i, q in enumerate(p1, 1):
            assert q["id"] == i, f"{key} p1 câu {i}: id sai ({q['id']})"
            expected_prefix = f"**Câu {i}:** "
            assert q["question"].startswith(expected_prefix), f"{key} p1 câu {i}: tiêu đề câu hỏi không bắt đầu bằng '{expected_prefix}': '{q['question'][:20]}'"
            assert len(q["options"]) == 4, f"{key} p1 câu {i}: options không đủ 4 ({len(q['options'])})"
            assert q["correct"] in [0, 1, 2, 3], f"{key} p1 câu {i}: correct sai ({q['correct']})"
            assert abs(q["points"] - 0.5) < 1e-6, f"{key} p1 câu {i}: points sai ({q['points']})"
            assert len(q["explanation"].strip()) > 0, f"{key} p1 câu {i}: explanation rỗng"

        # Kiểm tra Phần 2 (Tự luận)
        p2 = exam["part2"]
        assert len(p2) == 6, f"{key}: Part 2 không đủ 6 bài ({len(p2)})"
        for i, q in enumerate(p2, 1):
            assert q["id"] == i, f"{key} p2 bài {i}: id sai ({q['id']})"
            expected_prefix = f"**Bài {i}:** "
            assert q["question"].startswith(expected_prefix), f"{key} p2 bài {i}: tiêu đề bài không bắt đầu bằng '{expected_prefix}': '{q['question'][:20]}'"
            assert len(q["question"].strip()) > 0, f"{key} p2 bài {i}: question rỗng"
            assert len(q["solution"].strip()) > 0, f"{key} p2 bài {i}: solution rỗng"
            assert len(q["answer"].strip()) > 0, f"{key} p2 bài {i}: answer rỗng"
            assert 4 <= q["lineCount"] <= 8, f"{key} p2 bài {i}: lineCount không hợp lệ ({q['lineCount']})"
            assert abs(q["points"] - expected_part2_points[i-1]) < 1e-6, f"{key} p2 bài {i}: points sai ({q['points']} != {expected_part2_points[i-1]})"

        # Tổng điểm
        p1_total = sum(q["points"] for q in p1)
        p2_total = sum(q["points"] for q in p2)
        assert abs(p1_total - 3.0) < 1e-6, f"{key}: tổng điểm p1 != 3.0"
        assert abs(p2_total - 7.0) < 1e-6, f"{key}: tổng điểm p2 != 7.0"
        assert abs(p1_total + p2_total - 10.0) < 1e-6, f"{key}: tổng điểm đề != 10.0"

    print("  => Toàn bộ 48 đề thi đạt chuẩn 100% cấu trúc, điểm số và format!")

    print("\n[3] Kiểm tra tính độc lập (trùng lặp nội dung giữa test1, test2, test3 trong cùng bài):")
    lessons = {}
    for key, exam in all_exams.items():
        lnum = exam["lessonNum"]
        if lnum not in lessons:
            lessons[lnum] = []
        lessons[lnum].append(exam)

    for lnum, tests in sorted(lessons.items()):
        assert len(tests) == 3, f"Bài {lnum} không đủ 3 đề (có {len(tests)})"
        t1, t2, t3 = tests[0], tests[1], tests[2]
        
        # So sánh các câu trắc nghiệm
        for c in range(6):
            q1 = t1["part1"][c]["question"].strip()
            q2 = t2["part1"][c]["question"].strip()
            q3 = t3["part1"][c]["question"].strip()
            assert q1 != q2, f"Bài {lnum} Part1 Câu {c+1}: Trùng nhau giữa Test 1 và Test 2:\n{q1}"
            assert q1 != q3, f"Bài {lnum} Part1 Câu {c+1}: Trùng nhau giữa Test 1 và Test 3:\n{q1}"
            assert q2 != q3, f"Bài {lnum} Part1 Câu {c+1}: Trùng nhau giữa Test 2 và Test 3:\n{q2}"

        # So sánh các bài tự luận
        for b in range(6):
            b1 = t1["part2"][b]["question"].strip()
            b2 = t2["part2"][b]["question"].strip()
            b3 = t3["part2"][b]["question"].strip()
            assert b1 != b2, f"Bài {lnum} Part2 Bài {b+1}: Trùng nhau giữa Test 1 và Test 2:\n{b1}"
            assert b1 != b3, f"Bài {lnum} Part2 Bài {b+1}: Trùng nhau giữa Test 1 và Test 3:\n{b1}"
            assert b2 != b3, f"Bài {lnum} Part2 Bài {b+1}: Trùng nhau giữa Test 2 và Test 3:\n{b2}"

    print(f"  => Toàn bộ 16 bài học ({len(lessons)} bài x 3 đề = 48 đề) đều độc lập 100%, 0% trùng lặp!")

    print("\n==========================================")
    print("AUDIT THÀNH CÔNG: TẤT CẢ 48 ĐỀ THI ĐẠT CHUẨN XUẤT SẮC!")
    print("==========================================")

if __name__ == "__main__":
    run_audit()
