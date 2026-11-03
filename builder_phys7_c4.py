# -*- coding: utf-8 -*-
"""
CHƯƠNG IV: ÂM THANH (14 ĐỀ ĐỘC LẬP 100%)
- phys7_c4_b12: Bài 12 (3 đề)
- phys7_c4_b13: Bài 13 (3 đề)
- phys7_c4_b14: Bài 14 (3 đề)
- phys7_c4_rev: Ôn tập cuối Chương IV (5 đề)
"""

from builder_phys7_c4_b12_b13 import b12_b13_exams, make_mc, make_tf, make_sa, make_vdc
from builder_phys7_c4_b14 import b14_exams
from builder_phys7_c4_rev import c4_rev_exams

c4_exams = {}
c4_exams.update(b12_b13_exams)
c4_exams.update(b14_exams)
c4_exams.update(c4_rev_exams)

if __name__ == "__main__":
    print("Chapter 4 exams assembled:", len(c4_exams))
