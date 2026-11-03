# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 17: HIỆN TƯỢNG KHÚC XẠ ÁNH SÁNG
Bao gồm 3 đề thi độc lập 100%: phys9_c6_b17_test1, phys9_c6_b17_test2, phys9_c6_b17_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c6"
CH_TITLE = "Chương VI: Ánh sáng"

# Import from data_phys9_c6_p1 which has the exact tested implementation
from data_phys9_c6_p1 import exams as p1_exams
for k, v in p1_exams.items():
    if "b17" in k:
        exams[k] = v

print(f"Loaded {len(exams)} exams for Bài 17.")
