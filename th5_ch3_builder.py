# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 3: CÁC PHÉP TÍNH VỚI SỐ THẬP PHÂN (BÀI 15 ĐẾN BÀI 21) - TOÁN 5 KNTT
Gồm 7 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 15: Phép cộng số thập phân (th5_b15_test1, th5_b15_test2, th5_b15_test3)
- Bài 16: Phép trừ số thập phân (th5_b16_test1, th5_b16_test2, th5_b16_test3)
- Bài 17: Phép nhân số thập phân (th5_b17_test1, th5_b17_test2, th5_b17_test3)
- Bài 18: Nhân số thập phân với 10, 100, 1000... hoặc với 0,1; 0,01... (th5_b18_test1, th5_b18_test2, th5_b18_test3)
- Bài 19: Phép chia số thập phân (th5_b19_test1, th5_b19_test2, th5_b19_test3)
- Bài 20: Chia số thập phân cho 10, 100, 1000... hoặc cho 0,1; 0,01... (th5_b20_test1, th5_b20_test2, th5_b20_test3)
- Bài 21: Luyện tập chung Chủ đề 3 (th5_b21_test1, th5_b21_test2, th5_b21_test3)
Tổng cộng: 21 đề kiểm tra chất lượng cao, độc lập 100%.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from th5_ch3_part1 import get_ch3_part1_exams
from th5_ch3_part2 import get_ch3_part2_exams

def get_exams():
    exams = {}
    exams.update(get_ch3_part1_exams())
    exams.update(get_ch3_part2_exams())
    return exams

def get_all_ch3_exams():
    return get_exams()

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề thi Chủ đề 3: {len(ex)} (Kỳ vọng: 21 đề)")
    for eid in sorted(ex.keys()):
        print(f" - {eid}: {ex[eid]['title']}")
