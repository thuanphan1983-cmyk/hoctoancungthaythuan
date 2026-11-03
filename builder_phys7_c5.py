# -*- coding: utf-8 -*-
"""
CHƯƠNG V: ÁNH SÁNG (14 ĐỀ ĐỘC LẬP 100%)
- phys7_c5_b15: Bài 15 (3 đề)
- phys7_c5_b16: Bài 16 (3 đề)
- phys7_c5_b17: Bài 17 (3 đề)
- phys7_c5_rev: Ôn tập cuối Chương V (5 đề)
"""

from builder_phys7_c5_b15_b16 import b15_b16_exams, make_mc, make_tf, make_sa, make_vdc
from builder_phys7_c5_b17 import b17_exams
from builder_phys7_c5_rev import c5_rev_exams

c5_exams = {}
c5_exams.update(b15_b16_exams)
c5_exams.update(b17_exams)
c5_exams.update(c5_rev_exams)

if __name__ == "__main__":
    print("Chapter 5 exams assembled:", len(c5_exams))
