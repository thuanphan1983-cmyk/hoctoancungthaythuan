# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 2: SỐ THẬP PHÂN (BÀI 10 ĐẾN BÀI 14) - TỔNG HỢP 15 ĐỀ THI
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from th5_ch2_part1 import get_ch2_part1_exams
from th5_ch2_part2 import get_ch2_part2_exams

def get_all_ch2_exams():
    exams = {}
    exams.update(get_ch2_part1_exams())
    exams.update(get_ch2_part2_exams())
    return exams

if __name__ == "__main__":
    ex = get_all_ch2_exams()
    print(f"Tổng số đề Chủ đề 2: {len(ex)} (Kỳ vọng: 15 đề)")
