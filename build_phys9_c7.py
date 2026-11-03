# -*- coding: utf-8 -*-
"""
BUILDER FOR CHƯƠNG VII: ĐIỆN TỪ - VẬT LÝ 9 (KNTT)
Gồm 5 bài học / chuyên đề ôn tập (17 đề thi độc lập 100%):
- phys9_c7_b22: Bài 22: Từ trường của ống dây có dòng điện. Nam châm điện (3 đề)
- phys9_c7_b23: Bài 23: Tác dụng của từ trường lên đoạn dây dẫn mang dòng điện (3 đề)
- phys9_c7_b24: Bài 24: Hiện tượng cảm ứng điện từ. Dòng điện xoay chiều (3 đề)
- phys9_c7_b25: Bài 25: Máy biến thế (3 đề)
- phys9_c7_rev: [Đề tổng hợp] Ôn tập cuối Chương VII (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def build_c7():
    exams_c7 = {}
    from data_phys9_c7_b22 import exams as e_b22
    from data_phys9_c7_b23 import exams as e_b23
    from data_phys9_c7_b24 import exams as e_b24
    from data_phys9_c7_b25 import exams as e_b25
    from data_phys9_c7_rev import exams as e_rev

    exams_c7.update(e_b22)
    exams_c7.update(e_b23)
    exams_c7.update(e_b24)
    exams_c7.update(e_b25)
    exams_c7.update(e_rev)
    return exams_c7

if __name__ == "__main__":
    exs = build_c7()
    print("Chapter VII total exams:", len(exs))
