# -*- coding: utf-8 -*-
"""
BUILDER SINH TRỌN BỘ 12 ĐỀ THI TOÁN 6 - CHƯƠNG IV: MỘT SỐ HÌNH PHẲNG TRONG THỰC TIỄN
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

# Đảm bảo làm việc trong thư mục gốc của repository
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)
sys.path.insert(0, REPO_DIR)

from c4_6_part1 import EXAMS_PART1
from c4_6_part2 import EXAMS_PART2

def build_chapter4_grade6():
    print("🚀 Bắt đầu quá trình kiểm định và đóng gói Chương IV Toán 6: Một số hình phẳng trong thực tiễn...")
    all_exams = {}
    all_exams.update(EXAMS_PART1)
    all_exams.update(EXAMS_PART2)

    expected_keys = [
        "c4_6_bai1_test1", "c4_6_bai1_test2", "c4_6_bai1_test3",
        "c4_6_bai2_test1", "c4_6_bai2_test2", "c4_6_bai2_test3",
        "c4_6_bai3_test1", "c4_6_bai3_test2", "c4_6_bai3_test3",
        "c4_6_bai4_test1", "c4_6_bai4_test2", "c4_6_bai4_test3"
    ]

    assert len(all_exams) == 12, f"Lỗi: Số lượng đề thi không đủ 12! Hiện có: {len(all_exams)}"
    for key in expected_keys:
        assert key in all_exams, f"Lỗi: Thiếu đề thi {key}!"
        ex = all_exams[key]
        assert len(ex.get("part1", [])) == 12, f"{key}: part1 không đủ 12 câu"
        assert len(ex.get("part2", [])) == 2, f"{key}: part2 không đủ 2 câu"
        for st in ex["part2"]:
            assert len(st.get("statements", [])) == 4, f"{key}: part2 statement không đủ 4 ý"
        assert len(ex.get("part3", [])) == 4, f"{key}: part3 không đủ 4 câu"
        assert len(ex.get("part4", [])) == 3, f"{key}: part4 không đủ 3 câu"

    print("✅ Đã kiểm tra 12 đề thi: 100% đạt chuẩn ma trận Bộ GD&ĐT 2025.")

    chapter_data = {
        "grade": "6",
        "chapterId": "c4_6",
        "chapterTitle": "Chương IV: Một số hình phẳng trong thực tiễn",
        "totalExams": len(all_exams),
        "updatedAt": "2026-10-25 14:25:00",
        "exams": all_exams
    }

    # 1. Ghi JSON và JS vào src/data/generated
    gen_dir = os.path.join("src", "data", "generated")
    os.makedirs(gen_dir, exist_ok=True)

    json_path = os.path.join(gen_dir, "grade6_c4_6_exams.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(chapter_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã tạo tệp JSON: {json_path}")

    js_path = os.path.join(gen_dir, "grade6_c4_6_exams.js")
    js_content = f"""// Auto-generated Chapter 4 Toán 6 Exams (UMD Module)
const CHAPTER4_TOAN6_EXAMS = {json.dumps(all_exams, ensure_ascii=False, indent=2)};
const EXAMS_6_C4_6 = CHAPTER4_TOAN6_EXAMS;

if (typeof window !== 'undefined') {{
  window.CHAPTER4_TOAN6_EXAMS = CHAPTER4_TOAN6_EXAMS;
  window.GRADE6_C4_6_EXAMS = CHAPTER4_TOAN6_EXAMS;
  window.EXAMS_6_C4_6 = CHAPTER4_TOAN6_EXAMS;
  if (!window.DYNAMIC_EXAM_CACHE) window.DYNAMIC_EXAM_CACHE = {{}};
  window.DYNAMIC_EXAM_CACHE["grade6_c4_6"] = {json.dumps(chapter_data, ensure_ascii=False)};
}}

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ CHAPTER4_TOAN6_EXAMS, EXAMS_6_C4_6 }};
}}
"""
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"✅ Đã tạo tệp JS: {js_path}")

    # 2. Ghi ra root chapter4Toan6Exams.js
    with open("chapter4Toan6Exams.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("✅ Đã tạo chapter4Toan6Exams.js tại thư mục gốc")

    # 3. Cập nhật manifest.json ở các đường dẫn
    manifest_paths = [
        os.path.join("src", "data", "generated", "manifest.json"),
        "manifest.json",
        os.path.join("dist", "manifest.json"),
        os.path.join("dist", "generated", "manifest.json")
    ]

    manifest_entry = {
        "grade": "6",
        "chapterId": "c4_6",
        "chapterTitle": "Chương IV: Một số hình phẳng trong thực tiễn",
        "totalExams": 12,
        "updatedAt": "2026-10-25 14:25:00",
        "jsonFile": "grade6_c4_6_exams.json",
        "jsFile": "grade6_c4_6_exams.js",
        "jsonPath": "src/data/generated/grade6_c4_6_exams.json",
        "jsPath": "src/data/generated/grade6_c4_6_exams.js",
        "examKeys": expected_keys
    }

    for mp in manifest_paths:
        m_dir = os.path.dirname(mp)
        if m_dir:
            os.makedirs(m_dir, exist_ok=True)
        manifest_data = {}
        if os.path.exists(mp):
            try:
                with open(mp, "r", encoding="utf-8") as mf:
                    manifest_data = json.load(mf)
            except Exception as e:
                print(f"Lỗi đọc {mp}: {e}")
                manifest_data = {}

        manifest_data["grade6_c4_6"] = manifest_entry

        try:
            with open(mp, "w", encoding="utf-8") as mf:
                json.dump(manifest_data, mf, ensure_ascii=False, indent=2)
            print(f"✅ Đã đồng bộ manifest tại: {mp}")
        except Exception as e:
            print(f"Lỗi ghi {mp}: {e}")

    # 4. Sao chép vào dist/ nếu có
    if os.path.exists("dist"):
        dist_gen = os.path.join("dist", "generated")
        os.makedirs(dist_gen, exist_ok=True)
        shutil.copy2(json_path, os.path.join(dist_gen, "grade6_c4_6_exams.json"))
        shutil.copy2(js_path, os.path.join(dist_gen, "grade6_c4_6_exams.js"))
        shutil.copy2(js_path, os.path.join("dist", "chapter4Toan6Exams.js"))
        print("✅ Đã sao chép các tệp vào thư mục dist/")

    print("\n🎉 ĐÃ HOÀN TẤT ĐÓNG GÓI CHƯƠNG IV TOÁN 6!")

if __name__ == "__main__":
    build_chapter4_grade6()
