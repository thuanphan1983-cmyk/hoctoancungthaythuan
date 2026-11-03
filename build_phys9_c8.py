# -*- coding: utf-8 -*-
"""
BUILDER FOR CHƯƠNG VIII: NĂNG LƯỢNG VÀ SỰ BIẾN ĐỔI NĂNG LƯỢNG - VẬT LÝ 9 (KNTT)
Gồm 3 bài học / chuyên đề ôn tập (11 đề thi độc lập 100%):
- phys9_c8_b26: Bài 26: Năng lượng của Trái Đất. Năng lượng hoá thạch (3 đề)
- phys9_c8_b27: Bài 27: Năng lượng tái tạo (3 đề)
- phys9_c8_rev: [Đề tổng hợp] Ôn tập cuối Chương VIII (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def build_c8():
    exams_c8 = {}
    from data_phys9_c8_b26 import exams as e_b26
    from data_phys9_c8_b27 import exams as e_b27
    from data_phys9_c8_rev import exams as e_rev

    exams_c8.update(e_b26)
    exams_c8.update(e_b27)
    exams_c8.update(e_rev)
    return exams_c8

if __name__ == "__main__":
    exs = build_c8()
    print("Chapter VIII total exams:", len(exs))
