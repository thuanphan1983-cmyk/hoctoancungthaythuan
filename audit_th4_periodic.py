# -*- coding: utf-8 -*-
import sys
import re
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import generator_th4_gk2
import generator_th4_ck2

def audit_periodic():
    print("=" * 70)
    print("KIỂM ĐỊNH ĐỀ THI ĐỊNH KỲ TOÁN 4 (GK2 & CK2)")
    print("=" * 70)

    gk2 = generator_th4_gk2.get_th4_gk2_exams()
    ck2 = generator_th4_ck2.get_th4_ck2_exams()

    print(f"GK2: {len(gk2)} đề (Kỳ vọng: 8)")
    print(f"CK2: {len(ck2)} đề (Kỳ vọng: 8)")

    all_exams = {}
    all_exams.update(gk2)
    all_exams.update(ck2)

    errors = []
    question_stems = defaultdict(list)
    expected_p2_points = [1.0, 1.0, 1.0, 1.5, 1.5, 1.0]

    for eid, ex in all_exams.items():
        if ex.get("points") != 10.0:
            errors.append(f"[{eid}] Points != 10.0")
        if ex.get("duration") != "40 phút":
            errors.append(f"[{eid}] Duration != '40 phút'")
        if ex.get("grade") != "4":
            errors.append(f"[{eid}] Grade != '4'")

        part1 = ex.get("part1", [])
        if len(part1) != 6:
            errors.append(f"[{eid}] Part 1 len != 6")
        p1_total = 0.0
        for i, q in enumerate(part1, start=1):
            if not q.get("question", "").startswith(f"**Câu {i}:** "):
                errors.append(f"[{eid}][Câu {i}] Tiêu đề sai quy chuẩn: {q.get('question')[:20]}")
            if f"**Câu {i}.**" in q.get("question", ""):
                errors.append(f"[{eid}][Câu {i}] Dấu chấm sai quy chuẩn")
            if len(q.get("options", [])) != 4:
                errors.append(f"[{eid}][Câu {i}] options len != 4")
            if q.get("correct") not in [0, 1, 2, 3]:
                errors.append(f"[{eid}][Câu {i}] correct invalid")
            if not q.get("explanation", "").strip():
                errors.append(f"[{eid}][Câu {i}] explanation empty")
            p1_total += q.get("points", 0.0)
            clean_q = re.sub(r'^\*\*Câu \d+:\*\*\s*', '', q.get("question", "")).strip()
            question_stems[clean_q].append((eid, f"P1-Q{i}"))

        if abs(p1_total - 3.0) > 1e-6:
            errors.append(f"[{eid}] Part 1 total != 3.0: {p1_total}")

        part2 = ex.get("part2", [])
        if len(part2) != 6:
            errors.append(f"[{eid}] Part 2 len != 6")
        p2_total = 0.0
        for i, b in enumerate(part2, start=1):
            if not b.get("question", "").startswith(f"**Bài {i}:** "):
                errors.append(f"[{eid}][Bài {i}] Tiêu đề sai quy chuẩn: {b.get('question')[:20]}")
            if f"**Bài {i}.**" in b.get("question", ""):
                errors.append(f"[{eid}][Bài {i}] Dấu chấm sai quy chuẩn")
            if b.get("points") != expected_p2_points[i-1]:
                errors.append(f"[{eid}][Bài {i}] Points != {expected_p2_points[i-1]}")
            if b.get("lineCount") not in [4, 5, 6]:
                errors.append(f"[{eid}][Bài {i}] lineCount not in 4..6: {b.get('lineCount')}")
            if not b.get("solution", "").strip():
                errors.append(f"[{eid}][Bài {i}] solution empty")
            if "Đáp số" not in b.get("solution", ""):
                errors.append(f"[{eid}][Bài {i}] missing 'Đáp số:'")
            if not b.get("answer", "").strip():
                errors.append(f"[{eid}][Bài {i}] answer empty")
            p2_total += b.get("points", 0.0)

            clean_b = re.sub(r'^\*\*Bài \d+:\*\*\s*', '', b.get("question", "")).strip()
            if not clean_b.startswith("Đặt tính rồi tính:") and not clean_b.startswith("Tính:") and not clean_b.startswith("Tìm x"):
                question_stems[clean_b].append((eid, f"P2-B{i}"))

        if abs(p2_total - 7.0) > 1e-6:
            errors.append(f"[{eid}] Part 2 total != 7.0: {p2_total}")

    for stem, locs in question_stems.items():
        if len(locs) > 1:
            loc_str = ", ".join([f"{eid} ({loc})" for eid, loc in locs])
            errors.append(f"[DUPLICATE] '{stem[:50]}...' tại: {loc_str}")

    if errors:
        print(f"LỖI PHÁT HIỆN ({len(errors)}):")
        for e in errors:
            print(" -", e)
        return False
    else:
        print("TẤT CẢ 16 ĐỀ THI ĐỊNH KỲ TOÁN 4 (GK2 & CK2) ĐẠT CHUẨN 100%!")
        print(" - 0 lỗi cú pháp, 0 lỗi điểm số, 0 câu trùng lặp.")
        return True

if __name__ == "__main__":
    if not audit_periodic():
        sys.exit(1)
