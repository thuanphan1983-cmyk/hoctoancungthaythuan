# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 1: ÔN TẬP VÀ BỔ SUNG (BÀI 1 ĐẾN BÀI 9) - TỔNG HỢP 27 ĐỀ THI
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from th5_ch1_part1 import get_ch1_exams
from th5_ch1_part2 import get_ch1_part2_exams
from th5_ch1_part3 import get_ch1_part3_exams

def get_all_ch1_exams():
    exams = {}
    exams.update(get_ch1_exams())
    exams.update(get_ch1_part2_exams())
    exams.update(get_ch1_part3_exams())
    return exams

if __name__ == "__main__":
    ex = get_all_ch1_exams()
    print(f"Tổng số đề Chủ đề 1: {len(ex)} (Kỳ vọng: 27 đề)")

