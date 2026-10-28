# -*- coding: utf-8 -*-
"""
VERIFY PERIODIC EXAMS IN ROOT & DIST
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
    print("=" * 70)
    print("KIỂM TRA TÍNH TOÀN VẸN CỦA HỆ THỐNG ĐỀ THI ĐỊNH KỲ (HK2)")
    print("=" * 70)

    for fp in FILES_TO_CHECK:
        assert os.path.exists(fp), f"Không tìm thấy {fp}"
        print(f"\nKiểm tra file: {fp}")
        bank = load_bank_from_file(fp)

        total_checked = 0
        for grade in ["6", "7", "8", "9"]:
            assert grade in bank, f"Thiếu grade {grade} trong {fp}"
            
            # Kiểm tra Giữa kỳ 2
            mid2 = bank[grade].get("mid2", [])
            assert len(mid2) == 6, f"Khối {grade} mid2 không đúng 6 đề (hiện có {len(mid2)})"
            for i, ex in enumerate(mid2, 1):
                validate_periodic_exam(ex, grade, "mid2", i)
                total_checked += 1

            # Kiểm tra Cuối kỳ 2
            final2 = bank[grade].get("final2", [])
            assert len(final2) == 6, f"Khối {grade} final2 không đúng 6 đề (hiện có {len(final2)})"
            for i, ex in enumerate(final2, 1):
                validate_periodic_exam(ex, grade, "final2", i)
                total_checked += 1

            print(f"  ✅ Khối {grade}: Đã kiểm tra 6 đề Giữa kỳ 2 + 6 đề Cuối kỳ 2 -> HOÀN TOÀN ĐẠT CHUẨN!")

        print(f"🎉 File {fp}: Đã xác thực thành công {total_checked}/48 đề định kỳ!")

    print("\n" + "=" * 70)
    print("TẤT CẢ 48 MÃ ĐỀ ĐỊNH KỲ HK2 ĐÃ ĐƯỢC ĐỒNG BỘ VÀ XÁC THỰC 100% HOÀN HẢO!")
    print("=" * 70)

if __name__ == "__main__":
    main()
