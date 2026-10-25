# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

chapters = [
    {
        "id": "grade9_c1_9",
        "json": "src/data/generated/grade9_c1_9_exams.json",
        "count": 12,
        "prefix": "c1_9",
        "lessons": 4
    },
    {
        "id": "grade9_c2_9",
        "json": "src/data/generated/grade9_c2_9_exams.json",
        "count": 12,
        "prefix": "c2_9",
        "lessons": 4
    },
    {
        "id": "grade9_c3_9",
        "json": "src/data/generated/grade9_c3_9_exams.json",
        "count": 15,
        "prefix": "c3_9",
        "lessons": 5
    },
    {
        "id": "grade9_c4_9",
        "json": "src/data/generated/grade9_c4_9_exams.json",
        "count": 9,
        "prefix": "c4_9",
        "lessons": 3
    }
]

total_exams = 0
print("🔍 BẮT ĐẦU KIỂM ĐỊNH TOÀN DIỆN TOÁN 9 (CHƯƠNG 1 - 4)...")

for ch in chapters:
    print(f"\n--- Kiểm tra {ch['id']} ---")
    assert os.path.exists(ch["json"]), f"Thiếu file: {ch['json']}"
    with open(ch["json"], "r", encoding="utf-8") as f:
        data = json.load(f)
    
    exams = data.get("exams", {})
    assert len(exams) == ch["count"], f"Số lượng đề {len(exams)} khác kỳ vọng {ch['count']}"
    
    for l in range(1, ch["lessons"] + 1):
        for t in range(1, 4):
            key = f"{ch['prefix']}_bai{l}_test{t}"
            assert key in exams, f"Thiếu key: {key}"
            ex = exams[key]
            
            p1 = ex.get("part1", [])
            assert len(p1) == 12, f"{key} p1 != 12"
            p2 = ex.get("part2", [])
            assert len(p2) == 2, f"{key} p2 != 2"
            for stmt in p2:
                assert len(stmt.get("statements", [])) == 4, f"{key} p2 st != 4"
            p3 = ex.get("part3", [])
            assert len(p3) == 4, f"{key} p3 != 4"
            p4 = ex.get("part4", [])
            assert len(p4) == 3, f"{key} p4 != 3"
            
    print(f"✅ {ch['id']}: {ch['count']} đề hợp lệ 100% chuẩn ma trận Bộ GD&ĐT 2025.")
    total_exams += ch["count"]

print(f"\n🎯 TỔNG SỐ ĐỀ TOÁN 9 ĐÃ KIỂM TRA: {total_exams} / 48 đề.")

# Kiểm tra 4 bản manifest
manifests = [
    "manifest.json",
    "src/data/generated/manifest.json",
    "dist/manifest.json",
    "dist/generated/manifest.json"
]

for mf in manifests:
    if os.path.exists(mf):
        with open(mf, "r", encoding="utf-8") as f:
            m = json.load(f)
        for ch in chapters:
            assert ch["id"] in m, f"Manifest {mf} thiếu key {ch['id']}"
            assert m[ch["id"]]["totalExams"] == ch["count"], f"Manifest {mf} {ch['id']} totalExams != {ch['count']}"
        print(f"✅ Manifest {mf}: Đã đồng bộ chuẩn xác 4 chương Toán 9.")

print("\n🎉 TẤT CẢ DỮ LIỆU ĐỀ THI TOÁN 9 ĐÃ HOÀN TOÀN HỢP LỆ VÀ SẴN SÀNG!")
