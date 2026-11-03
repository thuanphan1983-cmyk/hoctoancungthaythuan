# -*- coding: utf-8 -*-
"""
GENERATOR KHTN HÓA HỌC 9 - 73 ĐỀ ĐỘC LẬP 100% (KNTT)
Gồm 5 chương:
- Chương I: 17 đề
- Chương II: 17 đề
- Chương III: 11 đề
- Chương IV: 20 đề
- Chương V: 8 đề
Tổng cộng: 73 đề
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from builder_chem9_c1 import exams_c1
from builder_chem9_c2 import exams_c2
from builder_chem9_c3 import exams_c3
from builder_chem9_c4 import exams_c4
from builder_chem9_c5 import exams_c5

def build_chem9_exams():
    exams = {}
    exams.update(exams_c1)
    exams.update(exams_c2)
    exams.update(exams_c3)
    exams.update(exams_c4)
    exams.update(exams_c5)
    return exams

if __name__ == '__main__':
    exs = build_chem9_exams()
    print("Tổng số đề Hóa 9 đã sinh thành công:", len(exs))
