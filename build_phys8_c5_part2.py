# -*- coding: utf-8 -*-
"""
CHƯƠNG V - PHẦN 2 (14 ĐỀ THI ĐỘC LẬP 100%):
- phys8_c5_b23: Bài 23: Tác dụng của dòng điện (3 đề)
- phys8_c5_b24: Bài 24: Cường độ dòng điện và hiệu điện thế (3 đề)
- phys8_c5_b25: Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế (3 đề)
- phys8_c5_rev: [Đề tổng hợp] Ôn tập cuối Chương V (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import c5_b23
import c5_b24
import c5_b25
import c5_rev

def get_c5_part2_exams():
    exams = {}
    exams.update(c5_b23.get_b23_exams())
    exams.update(c5_b24.get_b24_exams())
    exams.update(c5_b25.get_b25_exams())
    exams.update(c5_rev.get_c5_rev_exams())
    return exams

if __name__ == "__main__":
    exams = get_c5_part2_exams()
    print(f"Total C5 Part 2 exams: {len(exams)}")
