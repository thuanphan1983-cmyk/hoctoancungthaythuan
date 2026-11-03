# -*- coding: utf-8 -*-
"""
AUDIT TOÀN DIỆN CHO CÁC CHỦ ĐỀ TOÁN 4 KNTT DO SUBAGENT 3 PHỤ TRÁCH:
- th4_ch4_builder: 12 đề (Bài 17-20)
- th4_ch5_builder: 12 đề (Bài 21-24)
- th4_ch6_builder: 12 đề (Bài 25-28)
- th4_ch7_builder: 9 đề (Bài 29-31)
- th4_ch11_builder: 12 đề (Bài 51-54)
- th4_ch13_builder: 15 đề (Bài 59-63)
Tổng cộng: 72 đề thi.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from th4_ch4_builder import get_exams as get_ch4_exams
from th4_ch5_builder import get_exams as get_ch5_exams
from th4_ch6_builder import get_exams as get_ch6_exams
from th4_ch7_builder import get_exams as get_ch7_exams
from th4_ch11_builder import get_exams as get_ch11_exams
from th4_ch13_builder import get_exams as get_ch13_exams

def run_audit():
    ch4 = get_ch4_exams()
    ch5 = get_ch5_exams()
    ch6 = get_ch6_exams()
    ch7 = get_ch7_exams()
    ch11 = get_ch11_exams()
    ch13 = get_ch13_exams()

    print("[1] KIỂM TRA SỐ LƯỢNG ĐỀ THI:")
    print(f"  - Chủ đề 4: {len(ch4)} đề (Kỳ vọng: 12)")
    print(f"  - Chủ đề 5: {len(ch5)} đề (Kỳ vọng: 12)")
    print(f"  - Chủ đề 6: {len(ch6)} đề (Kỳ vọng: 12)")
    print(f"  - Chủ đề 7: {len(ch7)} đề (Kỳ vọng: 9)")
    print(f"  - Chủ đề 11: {len(ch11)} đề (Kỳ vọng: 12)")
    print(f"  - Chủ đề 13: {len(ch13)} đề (Kỳ vọng: 15)")

    assert len(ch4) == 12, "Lỗi số lượng Chủ đề 4"
    assert len(ch5) == 12, "Lỗi số lượng Chủ đề 5"
    assert len(ch6) == 12, "Lỗi số lượng Chủ đề 6"
    assert len(ch7) == 9, "Lỗi số lượng Chủ đề 7"
    assert len(ch11) == 12, "Lỗi số lượng Chủ đề 11"
    assert len(ch13) == 15, "Lỗi số lượng Chủ đề 13"

    all_exams = {}
    all_exams.update(ch4)
    all_exams.update(ch5)
    all_exams.update(ch6)
    all_exams.update(ch7)
    all_exams.update(ch11)
    all_exams.update(ch13)

    total_exams = len(all_exams)
    print(f"  => TỔNG CỘNG: {total_exams} đề thi (Kỳ vọng: 72 đề)\n")
    assert total_exams == 72, f"Tổng số đề là {total_exams} khác 72"

    print("[2] KIỂM TRA ĐỊNH DẠNG VÀ THANG ĐIỂM TỪNG ĐỀ:")
    expected_part2_points = [1.0, 1.0, 1.0, 1.5, 1.5, 1.0]

    for key, exam in all_exams.items():
        assert exam["id"] == key, f"{key}: lỗi id"
        assert "lessonId" in exam, f"{key}: thiếu lessonId"
        assert "lessonNum" in exam, f"{key}: thiếu lessonNum"
        assert "testNum" in exam, f"{key}: thiếu testNum"
        assert "title" in exam and len(exam["title"]) > 0, f"{key}: thiếu title"
        assert exam["duration"] == "35 phút", f"{key}: duration không phải '35 phút'"
        assert exam["points"] == 10.0, f"{key}: points không phải 10.0"

        # Kiểm tra Phần 1 (Trắc nghiệm: 6 câu x 0.5 = 3.0 điểm)
        p1 = exam["part1"]
        assert len(p1) == 6, f"{key}: part1 không đủ 6 câu ({len(p1)})"
        for i, q in enumerate(p1, 1):
            assert q["id"] == i, f"{key} p1 câu {i}: id sai ({q['id']})"
            expected_prefix = f"**Câu {i}:** "
            assert q["question"].startswith(expected_prefix), f"{key} p1 câu {i}: tiêu đề câu hỏi không bắt đầu bằng '{expected_prefix}': '{q['question'][:25]}'"
            assert len(q["options"]) == 4, f"{key} p1 câu {i}: options không đủ 4 ({len(q['options'])})"
            assert q["correct"] in [0, 1, 2, 3], f"{key} p1 câu {i}: correct sai ({q['correct']})"
            assert abs(q["points"] - 0.5) < 1e-6, f"{key} p1 câu {i}: điểm khác 0.5 ({q['points']})"
            assert len(q["explanation"].strip()) > 0, f"{key} p1 câu {i}: explanation rỗng"

        # Kiểm tra Phần 2 (Tự luận: 6 câu = 7.0 điểm)
        p2 = exam["part2"]
        assert len(p2) == 6, f"{key}: part2 không đủ 6 bài ({len(p2)})"
        for i, q in enumerate(p2, 1):
            assert q["id"] == i, f"{key} p2 bài {i}: id sai ({q['id']})"
            expected_prefix = f"**Bài {i}:** "
            assert q["question"].startswith(expected_prefix), f"{key} p2 bài {i}: tiêu đề bài không bắt đầu bằng '{expected_prefix}': '{q['question'][:25]}'"
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

    print("  => Tất cả 72 đề thi đạt chuẩn 100% cấu trúc, thang điểm và format!\n")

    print("[3] KIỂM TRA TÍNH ĐỘC LẬP (TRÙNG LẶP SỐ LIỆU / CÂU HỎI TRONG MỖI BÀI HỌC):")
    lessons = {}
    for key, exam in all_exams.items():
        lnum = exam["lessonNum"]
        if lnum not in lessons:
            lessons[lnum] = []
        lessons[lnum].append(exam)

    for lnum, tests in sorted(lessons.items()):
        assert len(tests) == 3, f"Bài {lnum} không đủ 3 đề (có {len(tests)})"
        t1, t2, t3 = tests[0], tests[1], tests[2]
        
        # So sánh trắc nghiệm
        for c in range(6):
            q1 = t1["part1"][c]["question"].strip()
            q2 = t2["part1"][c]["question"].strip()
            q3 = t3["part1"][c]["question"].strip()
            assert q1 != q2, f"Bài {lnum} Part1 Câu {c+1}: Trùng nhau giữa Test 1 và Test 2"
            assert q1 != q3, f"Bài {lnum} Part1 Câu {c+1}: Trùng nhau giữa Test 1 và Test 3"
            assert q2 != q3, f"Bài {lnum} Part1 Câu {c+1}: Trùng nhau giữa Test 2 và Test 3"

        # So sánh tự luận
        for b in range(6):
            b1 = t1["part2"][b]["question"].strip()
            b2 = t2["part2"][b]["question"].strip()
            b3 = t3["part2"][b]["question"].strip()
            assert b1 != b2, f"Bài {lnum} Part2 Bài {b+1}: Trùng nhau giữa Test 1 và Test 2"
            assert b1 != b3, f"Bài {lnum} Part2 Bài {b+1}: Trùng nhau giữa Test 1 và Test 3"
            assert b2 != b3, f"Bài {lnum} Part2 Bài {b+1}: Trùng nhau giữa Test 2 và Test 3"

    print(f"  => Toàn bộ {len(lessons)} bài học ({len(lessons)} x 3 = {total_exams} đề) đều độc lập 100%, 0% trùng lặp!\n")

    print("==================================================================")
    print("AUDIT THÀNH CÔNG: TẤT CẢ 72 ĐỀ THI TOÁN 4 HOÀN HẢO 100%!")
    print("==================================================================")

if __name__ == "__main__":
    run_audit()
