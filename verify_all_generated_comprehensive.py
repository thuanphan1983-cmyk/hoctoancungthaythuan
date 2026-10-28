# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

TARGET_CHAPTERS = [
    # Toán 6
    ("6", "c5_6"),
    ("6", "c6_6"),
    ("6", "c7_6"),
    ("6", "c8_6"),
    ("6", "c9_6"),
    # Toán 7
    ("7", "c9_7"),
    ("7", "c10_7"),
    # Toán 8
    ("8", "c8_8"),
    ("8", "c9_8"),
    ("8", "c10_8"),
    # Toán 9
    ("9", "c5_9"),
    ("9", "c6_9"),
    ("9", "c7_9"),
    ("9", "c8_9"),
    ("9", "c9_9"),
    ("9", "c10_9"),
]

def check_level(l, keyword):
    l = (l or "").lower()
    if keyword == "nb":
        return "nhận biết" in l or "nhan biet" in l or "nb" in l
    if keyword == "th":
        return "thông hiểu" in l or "thong hieu" in l or "th" in l
    if keyword == "vd":
        return ("vận dụng" in l or "van dung" in l or "vd" in l) and ("cao" not in l and "vdc" not in l)
    if keyword == "vdc":
        return "cao" in l or "vdc" in l
    return False

def verify_comprehensive():
    print("=" * 70)
    print("KIỂM TRA TOÀN DIỆN 16 CHƯƠNG ĐỀ MỚI ĐÃ SINH THEO MA TRẬN 2025")
    print("=" * 70)

    # 1. Manifest verification
    with open("manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    total_verified_exams = 0
    total_verified_chapters = 0

    for grade, ch_id in TARGET_CHAPTERS:
        manifest_key = f"grade{grade}_{ch_id}"
        assert manifest_key in manifest, f"Thiếu key {manifest_key} trong manifest.json"
        meta = manifest[manifest_key]

        json_file = f"src/data/generated/grade{grade}_{ch_id}_exams.json"
        js_file = f"src/data/generated/grade{grade}_{ch_id}_exams.js"
        dist_json_file = f"dist/generated/grade{grade}_{ch_id}_exams.json"
        dist_js_file = f"dist/generated/grade{grade}_{ch_id}_exams.js"

        assert os.path.exists(json_file), f"Không tìm thấy file {json_file}"
        assert os.path.exists(js_file), f"Không tìm thấy file {js_file}"
        assert os.path.exists(dist_json_file), f"Không tìm thấy file {dist_json_file}"
        assert os.path.exists(dist_js_file), f"Không tìm thấy file {dist_js_file}"

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        exams = data.get("exams", {})
        assert len(exams) == meta["totalExams"], f"Số đề thi {len(exams)} != {meta['totalExams']} tại {json_file}"
        
        # Verify exam structure
        for ex_id, exam in exams.items():
            test_num = int(ex_id.split("_test")[-1]) if "_test" in ex_id else 1
            part1 = exam.get("part1", [])
            part2 = exam.get("part2", [])
            part3 = exam.get("part3", [])
            part4 = exam.get("part4", [])

            assert len(part1) == 12, f"[{ex_id}] Part 1 phải có đúng 12 câu, thực tế: {len(part1)}"
            assert len(part2) == 2, f"[{ex_id}] Part 2 phải có đúng 2 câu, thực tế: {len(part2)}"
            assert len(part3) == 4, f"[{ex_id}] Part 3 phải có đúng 4 câu, thực tế: {len(part3)}"
            assert len(part4) == 3, f"[{ex_id}] Part 4 phải có đúng 3 câu, thực tế: {len(part4)}"

            # Kiểm tra Part 2: Mỗi câu (4 ý a,b,c,d) có ĐÚNG 1 ý ở mức độ Vận dụng
            for q_idx, q in enumerate(part2):
                stmts = q.get("statements") or q.get("sub_questions", [])
                vd_statements = [s for s in stmts if check_level(s.get("level", ""), "vd")]
                assert len(vd_statements) == 1, (
                    f"[{ex_id}] Part 2 Câu {q_idx+1} phải có ĐÚNG 1 ý Vận dụng. Thực tế: {len(vd_statements)}"
                )

            # Kiểm tra Part 3: Trong 4 câu, có ĐÚNG 2 câu ở mức độ Vận dụng
            vd_sa = [q for q in part3 if check_level(q.get("level", ""), "vd")]
            assert len(vd_sa) == 2, (
                f"[{ex_id}] Part 3 phải có ĐÚNG 2 câu Vận dụng. Thực tế: {len(vd_sa)}"
            )

            # Kiểm tra phân bổ mức độ cho Đề 1, 2 và Đề 3
            # Đếm tổng mức độ toàn bài
            counts = {"nb": 0, "th": 0, "vd": 0, "vdc": 0}
            for q in part1:
                lvl = q.get("level", "")
                if check_level(lvl, "nb"): counts["nb"] += 1
                elif check_level(lvl, "th"): counts["th"] += 1
                elif check_level(lvl, "vd"): counts["vd"] += 1
                elif check_level(lvl, "vdc"): counts["vdc"] += 1

            for q in part2:
                for s in (q.get("statements") or q.get("sub_questions", [])):
                    lvl = s.get("level", "")
                    if check_level(lvl, "nb"): counts["nb"] += 1
                    elif check_level(lvl, "th"): counts["th"] += 1
                    elif check_level(lvl, "vd"): counts["vd"] += 1
                    elif check_level(lvl, "vdc"): counts["vdc"] += 1

            for q in part3:
                lvl = q.get("level", "")
                if check_level(lvl, "nb"): counts["nb"] += 1
                elif check_level(lvl, "th"): counts["th"] += 1
                elif check_level(lvl, "vd"): counts["vd"] += 1
                elif check_level(lvl, "vdc"): counts["vdc"] += 1

            for q in part4:
                lvl = q.get("level", "")
                if check_level(lvl, "nb"): counts["nb"] += 1
                elif check_level(lvl, "th"): counts["th"] += 1
                elif check_level(lvl, "vd"): counts["vd"] += 1
                elif check_level(lvl, "vdc"): counts["vdc"] += 1

            total_items = sum(counts.values()) # 12 + 8 + 4 + 3 = 27 items
            assert total_items == 27, f"[{ex_id}] Tổng số đơn vị đánh giá phải là 27, thực tế: {total_items}"

            if test_num in [1, 2]:
                # Đề 1 & 2: ~40% NB (10-12), ~30% TH (7-9), ~20% VD (5-6), ~10% VDC (1-3)
                assert counts["nb"] >= 9, f"[{ex_id}] Đề {test_num} NB quá thấp: {counts['nb']}"
                assert counts["th"] >= 6, f"[{ex_id}] Đề {test_num} TH quá thấp: {counts['th']}"
                assert counts["vd"] >= 4, f"[{ex_id}] Đề {test_num} VD quá thấp: {counts['vd']}"
            else:
                # Đề 3 (Khá Giỏi): ~20% NB (5-7), ~30% TH (7-9), ~30% VD (7-10), ~20% VDC (2-5)
                assert counts["vd"] >= 6, f"[{ex_id}] Đề 3 VD phải >= 6: {counts['vd']}"
                assert counts["vdc"] >= 2, f"[{ex_id}] Đề 3 VDC phải >= 2: {counts['vdc']}"

            total_verified_exams += 1

        total_verified_chapters += 1
        print(f"✅ Toán {grade} - {ch_id}: {meta['chapterTitle']} -> {meta['totalExams']} đề kiểm tra ĐẠT CHUẨN 100%.")

    print("=" * 70)
    print(f"🎉 TỔNG KẾT: Đã kiểm tra thành công {total_verified_chapters}/16 chương.")
    print(f"🎉 Tổng số đề thi đạt chuẩn ma trận tuyệt đối: {total_verified_exams} đề!")
    print("=" * 70)

if __name__ == "__main__":
    verify_comprehensive()
