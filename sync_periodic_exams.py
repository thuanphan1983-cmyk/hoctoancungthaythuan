# -*- coding: utf-8 -*-
"""
MASTER SYNC SCRIPT - CẬP NHẬT & ĐỒNG BỘ ĐỀ THI ĐỊNH KỲ GIỮA KỲ 2 & CUỐI KỲ 2
Áp dụng cho cả 4 khối 6, 7, 8, 9 (SGK Kết nối tri thức).
Tích hợp trực tiếp vào periodicExamsData.js và dist/periodicExamsData.js.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

from periodic_validator import validate_periodic_exam
from build_periodic_grade6 import generate_g6_mid2, generate_g6_final2
from build_periodic_grade7 import generate_g7_mid2, generate_g7_final2
from build_periodic_grade8 import generate_g8_mid2, generate_g8_final2
from build_periodic_grade9 import generate_g9_mid2, generate_g9_final2

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

DATA_FILE = "periodicExamsData.js"

def sync_periodic():
    print("=" * 70)
    print("BẮT ĐẦU QUÁ TRÌNH ĐỒNG BỘ 48 MÃ ĐỀ ĐỊNH KỲ (HK2) KHỐI 6, 7, 8, 9")
    print("=" * 70)

    # 1. Sinh toàn bộ 48 đề
    new_exams = {
        "6": {"mid2": generate_g6_mid2(), "final2": generate_g6_final2()},
        "7": {"mid2": generate_g7_mid2(), "final2": generate_g7_final2()},
        "8": {"mid2": generate_g8_mid2(), "final2": generate_g8_final2()},
        "9": {"mid2": generate_g9_mid2(), "final2": generate_g9_final2()},
    }

    # 2. Kiểm tra tính hợp lệ ma trận tuyệt đối
    total_valid = 0
    for grade, terms in new_exams.items():
        for term, exams in terms.items():
            assert len(exams) == 6, f"Khối {grade} kỳ {term} không đủ 6 đề: {len(exams)}"
            for idx, ex in enumerate(exams, 1):
                validate_periodic_exam(ex, grade, term, idx)
                total_valid += 1
    print(f"✅ ĐÃ XÁC THỰC THÀNH CÔNG {total_valid}/48 ĐỀ THEO ĐÚNG MA TRẬN KHẢO THÍ!")

    # 3. Đọc dữ liệu hiện tại từ periodicExamsData.js
    assert os.path.exists(DATA_FILE), f"Không tìm thấy {DATA_FILE}"
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Trích xuất JSON từ window.PERIODIC_EXAM_BANK = { ... };
    prefix = "window.PERIODIC_EXAM_BANK = "
    start_idx = content.find(prefix)
    assert start_idx != -1, "Không tìm thấy prefix 'window.PERIODIC_EXAM_BANK = '"
    
    json_str = content[start_idx + len(prefix):].strip()
    if json_str.endswith(";"):
        json_str = json_str[:-1].strip()

    bank_data = json.loads(json_str)

    # 4. Cập nhật mid2 và final2 cho khối 6, 7, 8, 9
    for g in ["6", "7", "8", "9"]:
        if g not in bank_data:
            bank_data[g] = {}
        bank_data[g]["mid2"] = new_exams[g]["mid2"]
        bank_data[g]["final2"] = new_exams[g]["final2"]
        print(f"📦 Đã tích hợp Khối {g}: 6 đề Giữa kỳ 2 + 6 đề Cuối kỳ 2 mới.")

    # 5. Ghi lại periodicExamsData.js
    header = """/**
 * NGAN HANG DE KIEM TRA DINH KY TOAN THCS & THPT (KNTT) - KHOI 6, 7, 8, 9, 12
 * - Giua ky 1 & Cuoi ky 1: 8 bo de chuan hoa.
 * - Giua ky 2 & Cuoi ky 2: 6 bo de chuan hoa theo ma tran khao thi moi nhat (30% NB, 30% TH, 20% VD, 20% VDC).
 * - Cung cap day du 4 phan: 12 Trac nghiem + 2 Dung/Sai + 4 Tra loi ngan + 4 Tu luan.
 * - Cap nhat tu dong boi Antigravity Agent.
 */
"""
    new_content = header + "window.PERIODIC_EXAM_BANK = " + json.dumps(bank_data, ensure_ascii=False, indent=2) + ";\n"

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("💾 Đã lưu thành công periodicExamsData.js tại thư mục gốc.")
    print("=" * 70)

if __name__ == "__main__":
    sync_periodic()
