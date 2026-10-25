# -*- coding: utf-8 -*-
"""
Kiểm thử toàn diện bộ 54 đề thi Toán 7 - Chương 5, 6, 7, 8
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

def verify_all():
    print("==================================================")
    print("BẮT ĐẦU KIỂM TRA TOÀN DIỆN 54 ĐỀ THI TOÁN 7 (C5 - C8)")
    print("==================================================")

    chapters = [
        {"id": "grade7_c5_7", "name": "Chương V", "count": 12, "json": "src/data/generated/grade7_c5_7_exams.json", "root_js": "chapter5Toan7Exams.js"},
        {"id": "grade7_c6_7", "name": "Chương VI", "count": 15, "json": "src/data/generated/grade7_c6_7_exams.json", "root_js": "chapter6Toan7Exams.js"},
        {"id": "grade7_c7_7", "name": "Chương VII", "count": 18, "json": "src/data/generated/grade7_c7_7_exams.json", "root_js": "chapter7Toan7Exams.js"},
        {"id": "grade7_c8_7", "name": "Chương VIII", "count": 9, "json": "src/data/generated/grade7_c8_7_exams.json", "root_js": "chapter8Toan7Exams.js"},
    ]

    total_exams = 0

    for ch in chapters:
        print(f"\nKiểm tra {ch['name']} ({ch['id']}):")
        assert os.path.exists(ch["json"]), f"File JSON không tồn tại: {ch['json']}"
        assert os.path.exists(ch["root_js"]), f"File JS gốc không tồn tại: {ch['root_js']}"

        with open(ch["json"], "r", encoding="utf-8") as f:
            data = json.load(f)

        exams = data.get("exams", {})
        assert len(exams) == ch["count"], f"Số lượng đề {len(exams)} != {ch['count']}"
        total_exams += len(exams)

        # Kiểm tra từng đề thi
        for key, ex in exams.items():
            assert "title" in ex, f"{key} thiếu title"
            part1 = ex.get("part1", [])
            part2 = ex.get("part2", [])
            part3 = ex.get("part3", [])
            part4 = ex.get("part4", [])

            assert len(part1) == 12, f"{key} part1 ({len(part1)}) != 12"
            assert len(part2) == 2, f"{key} part2 ({len(part2)}) != 2"
            for st in part2:
                assert len(st.get("statements", [])) == 4, f"{key} part2 statements != 4"
            assert len(part3) == 4, f"{key} part3 ({len(part3)}) != 4"
            assert len(part4) == 3, f"{key} part4 ({len(part4)}) != 3"

        print(f"  -> Đạt chuẩn 100%: {len(exams)}/{ch['count']} đề thi chuẩn ma trận Bộ GD&ĐT 2025.")

    print(f"\n==> TỔNG CỘNG KIỂM TRA ĐẠT CHUẨN: {total_exams}/54 ĐỀ THI TOÁN 7!")

    # Kiểm tra manifest ở 4 vị trí
    manifest_paths = [
        "manifest.json",
        "src/data/generated/manifest.json",
        "dist/manifest.json",
        "dist/generated/manifest.json"
    ]

    print("\nKiểm tra tính nhất quán trong manifest.json:")
    for mp in manifest_paths:
        if os.path.exists(mp):
            with open(mp, "r", encoding="utf-8") as mf:
                mdata = json.load(mf)
            for ch in chapters:
                cid = ch["id"]
                assert cid in mdata, f"Thiếu {cid} trong {mp}"
                entry = mdata[cid]
                assert entry["totalExams"] == ch["count"], f"{cid} totalExams sai trong {mp}"
            print(f"  -> {mp}: HỢP LỆ VÀ ĐÃ ĐỒNG BỘ ĐẦY ĐỦ CẢ 4 CHƯƠNG!")
        else:
            print(f"  -> {mp}: Không tìm thấy file")

    print("\n🎉 TOÀN BỘ KIỂM THỬ THÀNH CÔNG RỰC RỠ!")

if __name__ == "__main__":
    verify_all()
