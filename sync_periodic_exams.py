# -*- coding: utf-8 -*-
"""
MASTER SYNC SCRIPT - ĐỒNG BỘ TOÀN BỘ 96 ĐỀ THI ĐỊNH KỲ (HK1 & HK2) CHO 4 KHỐI 6, 7, 8, 9
- Giữa học kì 1 (mid1): 6 đề chuẩn hóa cho mỗi khối
- Cuối học kì 1 (final1): 6 đề chuẩn hóa cho mỗi khối
- Giữa học kì 2 (mid2): 6 đề chuẩn hóa cho mỗi khối
- Cuối học kì 2 (final2): 6 đề chuẩn hóa cho mỗi khối
Tổng cộng 96 đề THCS được kiểm soát 100% bằng periodic_validator:
30% NB (3.0đ), 30% TH (3.0đ), 20% VD (2.0đ), 20% VDC (2.0đ) = 10.0đ.
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

from periodic_validator import validate_periodic_exam

# Grade 6
from build_periodic_grade6_term1 import generate_g6_mid1, generate_g6_final1
from build_periodic_grade6 import generate_g6_mid2, generate_g6_final2

# Grade 7
from build_periodic_grade7_term1 import generate_g7_mid1, generate_g7_final1
from build_periodic_grade7 import generate_g7_mid2, generate_g7_final2

# Grade 8
from build_periodic_grade8_term1 import generate_g8_mid1, generate_g8_final1
from build_periodic_grade8 import generate_g8_mid2, generate_g8_final2

# Grade 9
from build_periodic_grade9_term1 import generate_g9_mid1, generate_g9_final1
from build_periodic_grade9 import generate_g9_mid2, generate_g9_final2

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

DATA_FILE = "periodicExamsData.js"

def sync_periodic():
    print("=" * 75)
    print("BẮT ĐẦU ĐỒNG BỘ TOÀN BỘ 96 MÃ ĐỀ ĐỊNH KỲ (HK1 & HK2) KHỐI 6, 7, 8, 9")
    print("=" * 75)

    # 1. Sinh toàn bộ 96 đề kiểm tra
    all_exams = {
        "6": {
            "mid1": generate_g6_mid1(),
            "final1": generate_g6_final1(),
            "mid2": generate_g6_mid2(),
            "final2": generate_g6_final2(),
        },
        "7": {
            "mid1": generate_g7_mid1(),
            "final1": generate_g7_final1(),
            "mid2": generate_g7_mid2(),
            "final2": generate_g7_final2(),
        },
        "8": {
            "mid1": generate_g8_mid1(),
            "final1": generate_g8_final1(),
            "mid2": generate_g8_mid2(),
            "final2": generate_g8_final2(),
        },
        "9": {
            "mid1": generate_g9_mid1(),
            "final1": generate_g9_final1(),
            "mid2": generate_g9_mid2(),
            "final2": generate_g9_final2(),
        },
    }

    # 2. Kiểm tra tính hợp lệ ma trận tuyệt đối
    total_valid = 0
    for grade, terms in all_exams.items():
        for term, exams in terms.items():
            assert len(exams) == 6, f"Khối {grade} kì {term} không đủ 6 đề: {len(exams)}"
            for idx, ex in enumerate(exams, 1):
                validate_periodic_exam(ex, grade, term, idx)
                total_valid += 1
    print(f"XÁC THỰC THÀNH CÔNG {total_valid}/96 ĐỀ THEO ĐÚNG MA TRẬN KHẢO THÍ CHUẨN!")

    # 3. Đọc dữ liệu hiện tại từ periodicExamsData.js
    assert os.path.exists(DATA_FILE), f"Không tìm thấy {DATA_FILE}"
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    prefix = "window.PERIODIC_EXAM_BANK = "
    start_idx = content.find(prefix)
    assert start_idx != -1, "Không tìm thấy prefix 'window.PERIODIC_EXAM_BANK = '"
    
    json_str = content[start_idx + len(prefix):].strip()
    if json_str.endswith(";"):
        json_str = json_str[:-1].strip()

    bank_data = json.loads(json_str)

    # 4. Cập nhật dữ liệu cho 4 khối 6, 7, 8, 9
    for g in ["6", "7", "8", "9"]:
        if g not in bank_data:
            bank_data[g] = {}
        for term in ["mid1", "final1", "mid2", "final2"]:
            bank_data[g][term] = all_exams[g][term]
        print(f"Đã cập nhật Khối {g}: 6 đề GK1 + 6 đề CK1 + 6 đề GK2 + 6 đề CK2.")

    # 5. Ghi lại file periodicExamsData.js
    header = """/**
 * NGAN HANG DE KIEM TRA DINH KY TOAN THCS & THPT (KNTT) - KHOI 6, 7, 8, 9, 12
 * - Giua ky 1 & Cuoi ky 1: 6 bo de chuan hoa theo ma tran khao thi (30% NB, 30% TH, 20% VD, 20% VDC).
 * - Giua ky 2 & Cuoi ky 2: 6 bo de chuan hoa theo ma tran khao thi (30% NB, 30% TH, 20% VD, 20% VDC).
 * - Cung cap day du 4 phan: 12 Trac nghiem + 2 Dung/Sai + 4 Tra loi ngan + 4 Tu luan.
 * - Doan dan chung / Ngu canh de bai me duoc hien thi 100% truoc cac y phu a, b, c, d.
 * - Cap nhat tu dong boi Antigravity Agent.
 */
"""
    new_content = header + "window.PERIODIC_EXAM_BANK = " + json.dumps(bank_data, ensure_ascii=False, indent=2) + ";\n"

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Đã lưu thành công periodicExamsData.js tại thư mục gốc.")

    # Ghi cả vào dist/ nếu tồn tại
    dist_file = os.path.join(REPO_DIR, "dist", "periodicExamsData.js")
    if os.path.exists(os.path.join(REPO_DIR, "dist")):
        with open(dist_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Đã đồng bộ sang dist/periodicExamsData.js.")

    print("=" * 75)
    print("HOÀN TẤT ĐỒNG BỘ TOÀN BỘ 96 ĐỀ ĐỊNH KỲ THCS!")

if __name__ == "__main__":
    sync_periodic()
