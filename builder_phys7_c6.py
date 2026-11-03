# -*- coding: utf-8 -*-
"""
CHƯƠNG VI: TỪ (14 ĐỀ ĐỘC LẬP 100%)
- phys7_c6_b18: Bài 18 (3 đề)
- phys7_c6_b19: Bài 19 (3 đề)
- phys7_c6_b20: Bài 20 (3 đề)
- phys7_c6_rev: Ôn tập cuối Chương VI (5 đề)
"""

from builder_phys7_c6_b18_b19 import b18_b19_exams, make_mc, make_tf, make_sa, make_vdc
from builder_phys7_c6_b20 import b20_exams
from builder_phys7_c6_rev import c6_rev_exams

c6_exams = {}
c6_exams.update(b18_b19_exams)
c6_exams.update(b20_exams)
c6_exams.update(c6_rev_exams)

if __name__ == "__main__":
    print("Chapter 6 exams assembled:", len(c6_exams))
