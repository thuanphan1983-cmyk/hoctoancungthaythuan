# -*- coding: utf-8 -*-
"""
KIỂM ĐỊNH TOÀN DIỆN BỘ ĐỀ TOÁN 4 - CHỦ ĐỀ 11 & CHỦ ĐỀ 12
- Chủ đề 11: Phép cộng, phép trừ phân số (12 đề: Bài 51 -> Bài 54)
- Chủ đề 12: Phép nhân, phép chia phân số (12 đề: Bài 55 -> Bài 58)
Tổng cộng: 24 đề kiểm tra độc lập
"""
import sys
import re
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

scratch_dir = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if scratch_dir not in sys.path:
    sys.path.insert(0, scratch_dir)

import th4_ch11_builder
import th4_ch12_builder

def normalize_text(text):
    text = re.sub(r'[*_\r\n\t]+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip().lower()
    return text

def audit_ch11_ch12():
    print("=" * 80)
    print("BẮT ĐẦU KIỂM ĐỊNH TOÁN LỚP 4: CHỦ ĐỀ 11 VÀ CHỦ ĐỀ 12")
    print("=" * 80)

    ch11_exams = th4_ch11_builder.get_exams()
    ch12_exams = th4_ch12_builder.get_exams()

    print(f"1. Số đề Chủ đề 11: {len(ch11_exams)} đề (Kỳ vọng: 12)")
    print(f"2. Số đề Chủ đề 12: {len(ch12_exams)} đề (Kỳ vọng: 12)")

    assert len(ch11_exams) == 12, f"LỖI: Chủ đề 11 có {len(ch11_exams)} đề, kỳ vọng 12!"
    assert len(ch12_exams) == 12, f"LỖI: Chủ đề 12 có {len(ch12_exams)} đề, kỳ vọng 12!"

    all_exams = {}
    all_exams.update(ch11_exams)
    all_exams.update(ch12_exams)

    total_exams = len(all_exams)
    print(f"\n=> TỔNG CỘNG ĐÃ NẠP: {total_exams} ĐỀ KIỂM TRA (Kỳ vọng: 24 đề)")
    assert total_exams == 24, f"LỖI: Tổng số đề {total_exams} != 24!"

    errors = []
    question_stems = defaultdict(list)
    expected_p2_points = [1.0, 1.0, 1.0, 1.5, 1.5, 1.0]

    for eid, exam in all_exams.items():
        # Kiểm tra metadata
        for req_field in ["id", "lessonId", "lessonNum", "testNum", "title", "chapter", "grade", "term", "duration", "points", "part1", "part2"]:
            if req_field not in exam:
                errors.append(f"[{eid}] Thiếu trường bắt buộc '{req_field}'")

        if exam.get("duration") != "35 phút":
            errors.append(f"[{eid}] duration sai: '{exam.get('duration')}', kỳ vọng '35 phút'")
        if exam.get("points") != 10.0:
            errors.append(f"[{eid}] points sai: {exam.get('points')}, kỳ vọng 10.0")

        p1 = exam.get("part1", [])
        p2 = exam.get("part2", [])

        # Kiểm tra Phần 1 (Trắc nghiệm)
        if len(p1) != 6:
            errors.append(f"[{eid}] Phần 1 có {len(p1)} câu (kỳ vọng 6 câu)")

        p1_total = sum(q.get("points", 0) for q in p1)
        if round(p1_total, 2) != 3.0:
            errors.append(f"[{eid}] Tổng điểm Phần 1 là {p1_total} (kỳ vọng 3.0đ)")

        for idx, q in enumerate(p1, 1):
            expected_prefix = f"**Câu {idx}:** "
            q_text = q.get("question", "")
            if not q_text.startswith(expected_prefix):
                errors.append(f"[{eid}][P1-C{idx}] Tiêu đề câu sai quy chuẩn: '{q_text[:30]}...'")

            opts = q.get("options", [])
            if len(opts) != 4:
                errors.append(f"[{eid}][P1-C{idx}] Số phương án options = {len(opts)} != 4")

            if "choices" in q and len(q.get("choices", [])) != 4:
                errors.append(f"[{eid}][P1-C{idx}] Số phương án choices = {len(q.get('choices'))} != 4")

            corr = q.get("correct")
            if corr not in [0, 1, 2, 3]:
                errors.append(f"[{eid}][P1-C{idx}] correct = {corr} không hợp lệ (phải là 0, 1, 2, 3)")

            if not q.get("explanation"):
                errors.append(f"[{eid}][P1-C{idx}] Thiếu lời giải thích explanation")

            # Check duplicate stem
            raw_stem = re.sub(r'^\*\*câu \d+:\*\*\s*', '', normalize_text(q_text))
            question_stems[raw_stem].append(f"{eid}:P1-C{idx}")

        # Kiểm tra Phần 2 (Tự luận)
        if len(p2) != 6:
            errors.append(f"[{eid}] Phần 2 có {len(p2)} bài (kỳ vọng 6 bài)")

        p2_total = sum(q.get("points", 0) for q in p2)
        if round(p2_total, 2) != 7.0:
            errors.append(f"[{eid}] Tổng điểm Phần 2 là {p2_total} (kỳ vọng 7.0đ)")

        for idx, (q, exp_pt) in enumerate(zip(p2, expected_p2_points), 1):
            expected_prefix = f"**Bài {idx}:** "
            q_text = q.get("question", "")
            if not q_text.startswith(expected_prefix):
                errors.append(f"[{eid}][P2-B{idx}] Tiêu đề bài tự luận sai quy chuẩn: '{q_text[:30]}...'")

            pt = q.get("points", 0)
            if pt != exp_pt:
                errors.append(f"[{eid}][P2-B{idx}] Điểm bài tự luận {pt} != {exp_pt}")

            lc = q.get("lineCount", 0)
            if lc < 4 or lc > 6:
                errors.append(f"[{eid}][P2-B{idx}] lineCount = {lc} ngoài khoảng [4, 6]")

            if not q.get("solution"):
                errors.append(f"[{eid}][P2-B{idx}] Thiếu lời giải solution")

            if not q.get("answer"):
                errors.append(f"[{eid}][P2-B{idx}] Thiếu đáp số answer")

            # Check duplicate stem
            raw_stem = re.sub(r'^\*\*bài \d+:\*\*\s*', '', normalize_text(q_text))
            question_stems[raw_stem].append(f"{eid}:P2-B{idx}")

    print("\n--- KIỂM TRA TRÙNG LẶP CÂU HỎI (DUPLICATE STEM AUDIT) ---")
    duplicate_stems = {k: v for k, v in question_stems.items() if len(v) > 1}
    if duplicate_stems:
        print(f"CẢNH BÁO: Phát hiện {len(duplicate_stems)} câu hỏi có nội dung trùng lặp!")
        for stem, locations in list(duplicate_stems.items())[:10]:
            print(f" - [{len(locations)} lần] \"{stem[:60]}...\": {locations}")
            errors.append(f"Trùng lặp câu hỏi giữa {locations}: '{stem[:50]}'")
    else:
        print("TUYỆT VỜI: 0 CÂU HỎI TRÙNG LẶP NỘI DUNG TRÊN TOÀN BỘ 24 ĐỀ!")

    print("\n" + "=" * 80)
    if errors:
        print(f"TỔNG SỐ LỖI PHÁT HIỆN: {len(errors)} LỖI!")
        for err in errors[:20]:
            print(" -", err)
        return False
    else:
        print("TẤT CẢ 24 ĐỀ THI ĐÃ VƯỢT QUA KIỂM ĐỊNH VỚI 0 LỖI VÀ 0 CÂU TRÙNG LẶP!")
        print("=" * 80)
        return True

if __name__ == "__main__":
    success = audit_ch11_ch12()
    sys.exit(0 if success else 1)
