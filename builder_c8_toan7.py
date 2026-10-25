# -*- coding: utf-8 -*-
"""
BUILDER SINH TRỌN BỘ 9 ĐỀ THI TOÁN 7 - CHƯƠNG VIII: LÀM QUEN VỚI BIẾN CỐ VÀ XÁC SUẤT CỦA BIẾN CỐ
Chuẩn ma trận Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm chi tiết (3.0đ)
Tổng cộng: 10.0 điểm.
"""

import json
import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)
sys.path.insert(0, REPO_DIR)

from c8_7_part1 import EXAMS_PART1

def build_chapter8_grade7():
    print("🚀 Bắt đầu quá trình kiểm định và đóng gói Chương VIII Toán 7: Làm quen với biến cố và xác suất của biến cố...")
    all_exams = {}
    all_exams.update(EXAMS_PART1)

    expected_keys = [
        "c8_7_bai1_test1", "c8_7_bai1_test2", "c8_7_bai1_test3",
        "c8_7_bai2_test1", "c8_7_bai2_test2", "c8_7_bai2_test3",
        "c8_7_bai3_test1", "c8_7_bai3_test2", "c8_7_bai3_test3"
    ]

    assert len(all_exams) == 9, f"Lỗi: Số lượng đề thi không đủ 9! Hiện có: {len(all_exams)}"
    for key in expected_keys:
        assert key in all_exams, f"Lỗi: Thiếu đề thi {key}!"
        ex = all_exams[key]
        assert len(ex.get("part1", [])) == 12, f"{key}: part1 không đủ 12 câu"
        assert len(ex.get("part2", [])) == 2, f"{key}: part2 không đủ 2 câu"
        for st in ex["part2"]:
            assert len(st.get("statements", [])) == 4, f"{key}: part2 statement không đủ 4 ý"
        assert len(ex.get("part3", [])) == 4, f"{key}: part3 không đủ 4 câu"
        assert len(ex.get("part4", [])) == 3, f"{key}: part4 không đủ 3 câu"

    print("✅ Đã kiểm tra 9 đề thi: 100% đạt chuẩn ma trận Bộ GD&ĐT 2025.")

    chapter_data = {
        "grade": "7",
        "chapterId": "c8_7",
        "chapterTitle": "Chương VIII: Làm quen với biến cố và xác suất của biến cố",
        "totalExams": len(all_exams),
        "updatedAt": "2026-10-25 16:25:00",
        "exams": all_exams
    }

    # 1. Ghi JSON và JS vào src/data/generated
    gen_dir = os.path.join("src", "data", "generated")
    os.makedirs(gen_dir, exist_ok=True)

    json_path = os.path.join(gen_dir, "grade7_c8_7_exams.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(chapter_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã tạo tệp JSON: {json_path}")

    js_path = os.path.join(gen_dir, "grade7_c8_7_exams.js")
    js_content = f"""// Auto-generated Chapter 8 Toán 7 Exams (UMD Module)
const CHAPTER8_TOAN7_EXAMS = {json.dumps(all_exams, ensure_ascii=False, indent=2)};
const EXAMS_7_C8_7 = CHAPTER8_TOAN7_EXAMS;

if (typeof window !== 'undefined') {{
  window.CHAPTER8_TOAN7_EXAMS = CHAPTER8_TOAN7_EXAMS;
  window.GRADE7_C8_7_EXAMS = CHAPTER8_TOAN7_EXAMS;
  window.EXAMS_7_C8_7 = CHAPTER8_TOAN7_EXAMS;
  if (!window.DYNAMIC_EXAM_CACHE) window.DYNAMIC_EXAM_CACHE = {{}};
  window.DYNAMIC_EXAM_CACHE["grade7_c8_7"] = {json.dumps(chapter_data, ensure_ascii=False)};
}}

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ CHAPTER8_TOAN7_EXAMS, EXAMS_7_C8_7 }};
}}
"""
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"✅ Đã tạo tệp JS: {js_path}")

    # 2. Ghi ra root chapter8Toan7Exams.js
    with open("chapter8Toan7Exams.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("✅ Đã tạo chapter8Toan7Exams.js tại thư mục gốc")

    # 3. Cập nhật manifest.json ở các đường dẫn
    manifest_paths = [
        os.path.join("src", "data", "generated", "manifest.json"),
        "manifest.json",
        os.path.join("dist", "manifest.json"),
        os.path.join("dist", "generated", "manifest.json")
    ]

    manifest_entry = {
        "grade": "7",
        "chapterId": "c8_7",
        "chapterTitle": "Chương VIII: Làm quen với biến cố và xác suất của biến cố",
        "totalExams": len(all_exams),
        "updatedAt": "2026-10-25 16:25:00",
        "jsonFile": "grade7_c8_7_exams.json",
        "jsFile": "grade7_c8_7_exams.js",
        "jsonPath": "./src/data/generated/grade7_c8_7_exams.json",
        "jsPath": "./src/data/generated/grade7_c8_7_exams.js",
        "examKeys": expected_keys
    }

    for mp in manifest_paths:
        if os.path.exists(mp):
            try:
                with open(mp, "r", encoding="utf-8") as mf:
                    mdata = json.load(mf)
                mdata["grade7_c8_7"] = manifest_entry
                with open(mp, "w", encoding="utf-8") as mf:
                    json.dump(mdata, mf, ensure_ascii=False, indent=2)
                print(f"✅ Đã cập nhật manifest: {mp}")
            except Exception as e:
                print(f"⚠️ Cảnh báo: Không thể cập nhật {mp}: {e}")

    # 4. Sao chép vào dist/ nếu tồn tại
    dist_gen = os.path.join("dist", "generated")
    if os.path.exists(dist_gen):
        shutil.copy2(json_path, os.path.join(dist_gen, "grade7_c8_7_exams.json"))
        shutil.copy2(js_path, os.path.join(dist_gen, "grade7_c8_7_exams.js"))
        print("✅ Đã đồng bộ vào thư mục dist/generated/")

    dist_root = "dist"
    if os.path.exists(dist_root):
        shutil.copy2("chapter8Toan7Exams.js", os.path.join(dist_root, "chapter8Toan7Exams.js"))
        print("✅ Đã đồng bộ chapter8Toan7Exams.js vào thư mục dist/")

    print("🎉 Hoàn tất đóng gói Chương VIII Toán 7!")

if __name__ == "__main__":
    build_chapter8_grade7()
