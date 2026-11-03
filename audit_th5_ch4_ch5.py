# -*- coding: utf-8 -*-
"""
Script kiểm định chất lượng đề thi Toán 5 Chủ đề 4 và Chủ đề 5:
- Chủ đề 4: 12 đề (Bài 22 - 25, mỗi bài 3 đề: test1, test2, test3)
- Chủ đề 5: 12 đề (Bài 26 - 29, mỗi bài 3 đề: test1, test2, test3)
Tổng cộng: 24 đề kiểm tra.
"""

import sys
import re
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
import th5_ch4_builder
import th5_ch5_builder

def audit_exams():
    print("=" * 70)
    print("BẮT ĐẦU KIỂM ĐỊNH TOÀN DIỆN CHỦ ĐỀ 4 VÀ CHỦ ĐỀ 5 (TOÁN 5 KNTT)")
    print("=" * 70)

    ch4_exams = th5_ch4_builder.get_exams()
    ch5_exams = th5_ch5_builder.get_exams()

    print(f"Chủ đề 4: {len(ch4_exams)} đề (Kỳ vọng: 12)")
    print(f"Chủ đề 5: {len(ch5_exams)} đề (Kỳ vọng: 12)")

    all_exams = {}
    all_exams.update(ch4_exams)
    all_exams.update(ch5_exams)

    total_exams = len(all_exams)
    print(f"Tổng số đề kiểm định: {total_exams} đề (Kỳ vọng: 24)")
    assert total_exams == 24, f"LỖI: Tổng số đề là {total_exams}, kỳ vọng 24!"

    errors = []
    question_stems = defaultdict(list)

    expected_p2_points = [1.0, 1.0, 1.0, 1.5, 1.5, 1.0]

    for exam_id, exam in all_exams.items():
        # 1. Kiểm tra tiêu đề và thời gian
        if not exam.get("title"):
            errors.append(f"[{exam_id}] Thiếu 'title'")
        if exam.get("duration") != "35 phút":
            errors.append(f"[{exam_id}] 'duration' = {exam.get('duration')}, kỳ vọng '35 phút'")
        if exam.get("points") != 10.0:
            errors.append(f"[{exam_id}] 'points' = {exam.get('points')}, kỳ vọng 10.0")

        # 2. Kiểm tra Phần 1 (Trắc nghiệm)
        part1 = exam.get("part1", [])
        if len(part1) != 6:
            errors.append(f"[{exam_id}] Part 1 có {len(part1)} câu, kỳ vọng đúng 6 câu!")

        p1_total = 0.0
        for i, q in enumerate(part1):
            q_num = i + 1
            expected_prefix = f"**Câu {q_num}:** "
            q_text = q.get("question", "")

            # Kiểm tra cú pháp chuẩn tiêu đề
            if not q_text.startswith(expected_prefix):
                errors.append(f"[{exam_id}][Part1][Câu {q_num}] Tiêu đề sai quy chuẩn: '{q_text[:20]}...', kỳ vọng bắt đầu bằng '{expected_prefix}'")
            if f"**Câu {q_num}.**" in q_text:
                errors.append(f"[{exam_id}][Part1][Câu {q_num}] Chứa dấu chấm sai quy chuẩn '**Câu {q_num}.**'")

            # Kiểm tra choices
            choices = q.get("choices", [])
            if len(choices) != 4:
                errors.append(f"[{exam_id}][Part1][Câu {q_num}] Có {len(choices)} lựa chọn, kỳ vọng 4!")

            # Kiểm tra correct
            correct = q.get("correct")
            if correct not in [0, 1, 2, 3]:
                errors.append(f"[{exam_id}][Part1][Câu {q_num}] 'correct' = {correct} không hợp lệ (phải 0..3)!")

            # Kiểm tra explanation
            expl = q.get("explanation", "").strip()
            if not expl:
                errors.append(f"[{exam_id}][Part1][Câu {q_num}] Thiếu giải thích 'explanation'!")

            # Điểm
            pts = q.get("points", 0.0)
            if pts != 0.5:
                errors.append(f"[{exam_id}][Part1][Câu {q_num}] 'points' = {pts}, kỳ vọng 0.5")
            p1_total += pts

            # Lưu câu hỏi để kiểm tra trùng lặp
            clean_q = re.sub(r'^\*\*Câu \d+:\*\*\s*', '', q_text).strip()
            question_stems[clean_q].append((exam_id, f"Part 1 - Câu {q_num}"))

        if abs(p1_total - 3.0) > 1e-6:
            errors.append(f"[{exam_id}] Tổng điểm Part 1 = {p1_total}, kỳ vọng 3.0")

        # 3. Kiểm tra Phần 2 (Tự luận)
        part2 = exam.get("part2", [])
        if len(part2) != 6:
            errors.append(f"[{exam_id}] Part 2 có {len(part2)} câu, kỳ vọng đúng 6 bài!")

        p2_total = 0.0
        for i, b in enumerate(part2):
            b_num = i + 1
            expected_b_prefix = f"**Bài {b_num}:** "
            b_text = b.get("question", "")

            if not b_text.startswith(expected_b_prefix):
                errors.append(f"[{exam_id}][Part2][Bài {b_num}] Tiêu đề sai quy chuẩn: '{b_text[:20]}...', kỳ vọng bắt đầu bằng '{expected_b_prefix}'")
            if f"**Bài {b_num}.**" in b_text:
                errors.append(f"[{exam_id}][Part2][Bài {b_num}] Chứa dấu chấm sai quy chuẩn '**Bài {b_num}.**'")

            # Điểm từng bài
            pts = b.get("points", 0.0)
            if pts != expected_p2_points[i]:
                errors.append(f"[{exam_id}][Part2][Bài {b_num}] 'points' = {pts}, kỳ vọng {expected_p2_points[i]}")
            p2_total += pts

            # lineCount
            lc = b.get("lineCount")
            if lc not in [4, 5, 6]:
                errors.append(f"[{exam_id}][Part2][Bài {b_num}] 'lineCount' = {lc}, kỳ vọng trong khoảng 4..6")

            # solution
            sol = b.get("solution", "").strip()
            if not sol:
                errors.append(f"[{exam_id}][Part2][Bài {b_num}] Thiếu 'solution'!")
            if "Đáp số" not in sol:
                errors.append(f"[{exam_id}][Part2][Bài {b_num}] 'solution' thiếu 'Đáp số:'!")

            # answer
            ans = b.get("answer", "").strip()
            if not ans:
                errors.append(f"[{exam_id}][Part2][Bài {b_num}] Thiếu 'answer'!")

            # Lưu bài để kiểm tra trùng lặp
            clean_b = re.sub(r'^\*\*Bài \d+:\*\*\s*', '', b_text).strip()
            # Bỏ qua các tiêu đề generic như "Đặt tính rồi tính:"
            if not clean_b.startswith("Đặt tính rồi tính:") and not clean_b.startswith("Tính:") and not clean_b.startswith("Tìm x"):
                question_stems[clean_b].append((exam_id, f"Part 2 - Bài {b_num}"))

        if abs(p2_total - 7.0) > 1e-6:
            errors.append(f"[{exam_id}] Tổng điểm Part 2 = {p2_total}, kỳ vọng 7.0")

    # 4. Kiểm tra trùng lặp câu hỏi
    duplicate_count = 0
    for stem, locs in question_stems.items():
        if len(locs) > 1:
            duplicate_count += 1
            loc_str = ", ".join([f"{eid} ({loc})" for eid, loc in locs])
            errors.append(f"[DUPLICATE QUESTION] '{stem[:60]}...' xuất hiện tại: {loc_str}")

    print("\n" + "=" * 70)
    print("KẾT QUẢ KIỂM ĐỊNH:")
    print("=" * 70)
    if errors:
        print(f"PHÁT HIỆN {len(errors)} LỖI:")
        for err in errors:
            print(" -", err)
        return False
    else:
        print("TẤT CẢ 24 ĐỀ THI ĐẠT CHUẨN 100%!")
        print(" - 24/24 đề đầy đủ Part 1 (6 câu MCQ, 0.5đ/câu = 3.0đ)")
        print(" - 24/24 đề đầy đủ Part 2 (6 câu Essay, [1, 1, 1, 1.5, 1.5, 1] = 7.0đ)")
        print(" - Format tiêu đề tuyệt đối chuẩn: '**Câu [Số]:** ' và '**Bài [Số]:** ' (không dấu chấm sai)")
        print(" - Tất cả các câu hỏi hoàn toàn độc lập, 0 trùng lặp nội dung!")
        print(" - Tổng điểm mỗi đề chuẩn 10.0 điểm, thời gian làm bài chuẩn 35 phút.")
        return True

if __name__ == "__main__":
    success = audit_exams()
    if not success:
        sys.exit(1)
