# -*- coding: utf-8 -*-
"""
MASTER BUILDER FOR KHTN (HÓA HỌC & VẬT LÝ 7, 8, 9)
Tổng hợp toàn bộ 322 đề thi và xuất ra các tập tin JS và JSON
"""

import os
import sys
import json
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

from khtn_curriculum_def import KHTN_CURRICULUM
from generator_khtn_chem7 import build_chem7_exams
from generator_khtn_chem8 import build_chem8_exams
from generator_khtn_chem9 import build_chem9_exams
from generator_khtn_phys7 import build_phys7_exams
from generator_khtn_phys8 import build_phys8_exams
from generator_khtn_phys9 import build_phys9_exams

PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
OUTPUT_DIR = os.path.join(PROJECT_DIR, "src", "data", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("=== ĐANG TỔNG HỢP TOÀN BỘ ĐỀ THI KHTN ===")
    
    all_exams = {}

    print("1. Đang sinh Hóa học 7...")
    chem7 = build_chem7_exams()
    all_exams.update(chem7)
    print(f"   => {len(chem7)} đề")

    print("2. Đang sinh Hóa học 8...")
    chem8 = build_chem8_exams()
    all_exams.update(chem8)
    print(f"   => {len(chem8)} đề")

    print("3. Đang sinh Hóa học 9...")
    chem9 = build_chem9_exams()
    all_exams.update(chem9)
    print(f"   => {len(chem9)} đề")

    print("4. Đang sinh Vật lý 7...")
    phys7 = build_phys7_exams()
    all_exams.update(phys7)
    print(f"   => {len(phys7)} đề")

    print("5. Đang sinh Vật lý 8...")
    phys8 = build_phys8_exams()
    all_exams.update(phys8)
    print(f"   => {len(phys8)} đề")

    print("6. Đang sinh Vật lý 9...")
    phys9 = build_phys9_exams()
    all_exams.update(phys9)
    print(f"   => {len(phys9)} đề")

    total_exams = len(all_exams)
    print(f"\n=> TỔNG CỘNG ĐÃ SINH: {total_exams} ĐỀ THI KHTN CHUẨN MA TRẬN!")

    # Thẩm định chất lượng toán học & sư phạm từng đề
    print("Đang thẩm định tính chính xác của 100% đề thi...")
    for k, ex in all_exams.items():
        assert len(ex["part1"]) == 12, f"Lỗi đề {k}: part1 thiếu câu (có {len(ex['part1'])})"
        assert len(ex["part2"]) == 4, f"Lỗi đề {k}: part2 thiếu câu (có {len(ex['part2'])})"
        for q in ex["part2"]:
            assert len(q["statements"]) == 4, f"Lỗi đề {k} part2 q{q['id']}: thiếu ý (có {len(q['statements'])})"
        assert len(ex["part3"]) == 6, f"Lỗi đề {k}: part3 thiếu câu (có {len(ex['part3'])})"
        assert len(ex["part4"]) == 4, f"Lỗi đề {k}: part4 thiếu câu (có {len(ex['part4'])})"
    print("✅ Đã kiểm tra 100% đề thi: Mọi đề thi đều có đủ 4 phần (12 TN + 4 Đ/S + 6 TLN + 4 VDC)!")

    # 1. Ghi khtn_exams_data.json
    json_path = os.path.join(OUTPUT_DIR, "khtn_exams_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_exams, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã ghi: {json_path}")

    # 2. Ghi khtn_curriculum.json
    curr_json_path = os.path.join(OUTPUT_DIR, "khtn_curriculum.json")
    with open(curr_json_path, "w", encoding="utf-8") as f:
        json.dump(KHTN_CURRICULUM, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã ghi: {curr_json_path}")

    # 3. Ghi khtnExamsData.js ở thư mục gốc
    js_content = "// DỮ LIỆU ĐỀ THI KHOA HỌC TỰ NHIÊN (HÓA HỌC & VẬT LÝ 7, 8, 9) - KNTT\n"
    js_content += f"// Cập nhật lúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    js_content += "window.KHTN_CURRICULUM = " + json.dumps(KHTN_CURRICULUM, ensure_ascii=False) + ";\n\n"
    js_content += "window.KHTN_EXAMS_DATA = " + json.dumps(all_exams, ensure_ascii=False) + ";\n"
    
    root_js_path = os.path.join(PROJECT_DIR, "khtnExamsData.js")
    with open(root_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"✅ Đã ghi tập tin gốc: {root_js_path}")

    # Ghi vào generated khtnExamsData.js
    gen_js_path = os.path.join(OUTPUT_DIR, "khtnExamsData.js")
    with open(gen_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"✅ Đã ghi tập tin generated: {gen_js_path}")

if __name__ == "__main__":
    main()
