# -*- coding: utf-8 -*-
"""
CHƯƠNG III: TỐC ĐỘ (17 ĐỀ ĐỘC LẬP 100%)
- phys7_c3_b8: Bài 8 (3 đề)
- phys7_c3_b9: Bài 9 (3 đề)
- phys7_c3_b10: Bài 10 (3 đề)
- phys7_c3_b11: Bài 11 (3 đề)
- phys7_c3_rev: Ôn tập cuối Chương III (5 đề)
"""

from builder_phys7_c3_b8_b9 import b8_b9_exams, make_mc, make_tf, make_sa, make_vdc
from builder_phys7_c3_b10_b11 import b10_b11_exams
from builder_phys7_c3_rev import c3_rev_exams

c3_exams = {}
c3_exams.update(b8_b9_exams)
c3_exams.update(b10_b11_exams)
c3_exams.update(c3_rev_exams)

if __name__ == "__main__":
    print("Chapter 3 exams assembled:", len(c3_exams))
