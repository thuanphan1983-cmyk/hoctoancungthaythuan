# -*- coding: utf-8 -*-
"""
BUILDER SINH TRỌN BỘ 15 ĐỀ THI TOÁN 8 - CHƯƠNG VI: PHÂN THỨC ĐẠI SỐ
Tuân thủ chuẩn ma trận Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, tối đa 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm chi tiết (3.0đ)
Tổng cộng: 10.0 điểm.
"""

import json
import os
import sys
import glob
import shutil

# Đảm bảo stdout ghi tiếng Việt an toàn
sys.stdout.reconfigure(encoding='utf-8')

from c6_bai1_data import BAI1_EXAMS
from c6_bai2_data import BAI2_EXAMS
from c6_bai3_data import BAI3_EXAMS
from c6_bai4_data import BAI4_EXAMS
from c6_bai5_data import BAI5_EXAMS

def build_chapter6():
    print("🚀 Bắt đầu quá trình đóng gói và kiểm định Chương VI: Phân thức đại số...")
    all_exams = {}
    all_exams.update(BAI1_EXAMS)
    all_exams.update(BAI2_EXAMS)
    all_exams.update(BAI3_EXAMS)
    all_exams.update(BAI4_EXAMS)
    all_exams.update(BAI5_EXAMS)

    expected_keys = [
        "c6_8_bai1_test1", "c6_8_bai1_test2", "c6_8_bai1_test3",
        "c6_8_bai2_test1", "c6_8_bai2_test2", "c6_8_bai2_test3",
        "c6_8_bai3_test1", "c6_8_bai3_test2", "c6_8_bai3_test3",
        "c6_8_bai4_test1", "c6_8_bai4_test2", "c6_8_bai4_test3",
        "c6_8_bai5_test1", "c6_8_bai5_test2", "c6_8_bai5_test3"
    ]

    assert len(all_exams) == 15, f"Lỗi: Số lượng đề thi không đủ 15! Hiện có: {len(all_exams)}"
    for key in expected_keys:
        assert key in all_exams, f"Lỗi: Thiếu đề thi {key}!"
        ex = all_exams[key]
        assert len(ex.get("part1", [])) == 12, f"{key}: part1 không đủ 12 câu"
        assert len(ex.get("part2", [])) == 2, f"{key}: part2 không đủ 2 câu"
        for st in ex["part2"]:
            assert len(st.get("statements", [])) == 4, f"{key}: part2 statement không đủ 4 ý"
        assert len(ex.get("part3", [])) == 4, f"{key}: part3 không đủ 4 câu"
        assert len(ex.get("part4", [])) == 3, f"{key}: part4 không đủ 3 câu"

    print("✅ Đã kiểm tra cấu trúc 15 đề thi: 100% đạt chuẩn ma trận Bộ GD&ĐT 2025.")

    chapter_data = {
        "grade": "8",
        "chapterId": "c6_8",
        "chapterTitle": "Chương VI: Phân thức đại số",
        "totalExams": len(all_exams),
        "updatedAt": "2026-10-23 20:50:00",
        "exams": all_exams
    }

    # 1. Ghi JSON và JS vào src/data/generated
    gen_dir = os.path.join("src", "data", "generated")
    os.makedirs(gen_dir, exist_ok=True)

    json_path = os.path.join(gen_dir, "grade8_c6_8_exams.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(chapter_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã tạo tệp dữ liệu JSON: {json_path}")

    js_path = os.path.join(gen_dir, "grade8_c6_8_exams.js")
    js_content = f"""// Auto-generated Chapter 6 Toán 8 Exams (UMD Module)
const CHAPTER6_TOAN8_EXAMS = {json.dumps(all_exams, ensure_ascii=False, indent=2)};
const EXAMS_8_C6_8 = CHAPTER6_TOAN8_EXAMS;

if (typeof window !== 'undefined') {{
  window.CHAPTER6_TOAN8_EXAMS = CHAPTER6_TOAN8_EXAMS;
  window.GRADE8_C6_8_EXAMS = CHAPTER6_TOAN8_EXAMS;
  window.EXAMS_8_C6_8 = CHAPTER6_TOAN8_EXAMS;
  if (!window.DYNAMIC_EXAM_CACHE) window.DYNAMIC_EXAM_CACHE = {{}};
  window.DYNAMIC_EXAM_CACHE["grade8_c6_8"] = {json.dumps(chapter_data, ensure_ascii=False)};
}}

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ CHAPTER6_TOAN8_EXAMS, EXAMS_8_C6_8 }};
}}
"""
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"✅ Đã tạo tệp UMD JS: {js_path}")

    # 2. Ghi ra root chapter6Toan8Exams.js
    with open("chapter6Toan8Exams.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("✅ Đã tạo chapter6Toan8Exams.js tại thư mục gốc")

    # 3. Cập nhật manifest.json tại tất cả các vị trí
    manifest_paths = [
        os.path.join("src", "data", "generated", "manifest.json"),
        "manifest.json",
        os.path.join("dist", "manifest.json"),
        os.path.join("dist", "generated", "manifest.json")
    ]

    manifest = {}
    json_files = glob.glob(os.path.join(gen_dir, "grade*_exams.json"))
    for jf in json_files:
        try:
            fname = os.path.basename(jf)
            with open(jf, "r", encoding="utf-8") as mf:
                data = json.load(mf)
            g = data.get("grade", "")
            cid = data.get("chapterId", "")
            title = data.get("chapterTitle", "")
            ex = data.get("exams", {})
            k = f"grade{g}_{cid}"
            manifest[k] = {
                "grade": str(g),
                "chapterId": cid,
                "chapterTitle": title,
                "totalExams": len(ex),
                "updatedAt": data.get("updatedAt", ""),
                "jsonFile": fname,
                "jsFile": fname.replace(".json", ".js"),
                "examKeys": list(ex.keys())
            }
        except Exception as e:
            print("Lỗi đọc", jf, e)

    for mp in manifest_paths:
        try:
            os.makedirs(os.path.dirname(mp), exist_ok=True)
            with open(mp, "w", encoding="utf-8") as mf:
                json.dump(manifest, mf, ensure_ascii=False, indent=2)
            print(f"✅ Đã cập nhật manifest tại: {mp}")
        except Exception:
            pass

    # 4. Sao chép vào dist nếu tồn tại
    dist_dir = "dist"
    if os.path.exists(dist_dir):
        shutil.copy2("chapter6Toan8Exams.js", os.path.join(dist_dir, "chapter6Toan8Exams.js"))
        os.makedirs(os.path.join(dist_dir, "generated"), exist_ok=True)
        shutil.copy2(json_path, os.path.join(dist_dir, "generated", "grade8_c6_8_exams.json"))
        shutil.copy2(js_path, os.path.join(dist_dir, "generated", "grade8_c6_8_exams.js"))
        os.makedirs(os.path.join(dist_dir, "src", "data", "generated"), exist_ok=True)
        shutil.copy2(json_path, os.path.join(dist_dir, "src", "data", "generated", "grade8_c6_8_exams.json"))
        shutil.copy2(js_path, os.path.join(dist_dir, "src", "data", "generated", "grade8_c6_8_exams.js"))
        print("✅ Đã sao chép toàn bộ tệp Chương VI vào dist/")

    print("🎉 Hoàn tất thành công 100% toàn bộ hệ thống đề thi Chương VI Toán 8!")

if __name__ == "__main__":
    build_chapter6()
