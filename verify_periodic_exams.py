# -*- coding: utf-8 -*-
"""
VERIFY PERIODIC EXAMS IN ROOT & DIST (ALL 96 EXAMS: GK1, CK1, GK2, CK2)
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
from periodic_validator import validate_periodic_exam

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

FILES_TO_CHECK = [
    "periodicExamsData.js",
    "dist/periodicExamsData.js"
]

def load_bank_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    prefix = "window.PERIODIC_EXAM_BANK = "
    idx = content.find(prefix)
    assert idx != -1, f"Không tìm thấy prefix trong {filepath}"
    json_str = content[idx + len(prefix):].strip()
    if json_str.endswith(";"):
        json_str = json_str[:-1].strip()
    return json.loads(json_str)

def main():
    print("=" * 75)
    print("KIỂM TRA TÍNH TOÀN VẸN CỦA HỆ THỐNG ĐỀ THI ĐỊNH KỲ (HK1 & HK2) - 96 ĐỀ")
    print("=" * 75)

    for fp in FILES_TO_CHECK:
        assert os.path.exists(fp), f"Không tìm thấy {fp}"
        print(f"\nKiểm tra file: {fp}")
        bank = load_bank_from_file(fp)

        total_checked = 0
        for grade in ["6", "7", "8", "9"]:
            assert grade in bank, f"Thiếu grade {grade} trong {fp}"
            
            for term in ["mid1", "final1", "mid2", "final2"]:
                exams = bank[grade].get(term, [])
                assert len(exams) == 6, f"Khối {grade} {term} không đúng 6 đề (hiện có {len(exams)})"
                for i, ex in enumerate(exams, 1):
                    validate_periodic_exam(ex, grade, term, i)
                    total_checked += 1

            print(f"  OK Khối {grade}: Đã kiểm tra 24 đề (6 GK1 + 6 CK1 + 6 GK2 + 6 CK2) -> ĐẠT CHUẨN!")

        print(f"File {fp}: Đã xác thực thành công {total_checked}/96 đề định kỳ!")

    print("\n" + "=" * 75)
    print("TẤT CẢ 96 MÃ ĐỀ ĐỊNH KỲ HK1 VÀ HK2 ĐÃ ĐƯỢC ĐỒNG BỘ VÀ XÁC THỰC 100% HOÀN HẢO!")
    print("=" * 75)

if __name__ == "__main__":
    main()
