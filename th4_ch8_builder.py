# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 8: PHÉP NHÂN VÀ PHÉP CHIA (BÀI 32 ĐẾN BÀI 39) - TOÁN 4 KNTT
Gồm 8 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 32: Nhân với số có một chữ số (th4_b32_test1, th4_b32_test2, th4_b32_test3)
- Bài 33: Tính chất giao hoán và kết hợp của phép nhân (th4_b33_test1, th4_b33_test2, th4_b33_test3)
- Bài 34: Nhân với 10, 100, 1000,... Chia cho 10, 100, 1000,... (th4_b34_test1, th4_b34_test2, th4_b34_test3)
- Bài 35: Nhân với số có hai chữ số (th4_b35_test1, th4_b35_test2, th4_b35_test3)
- Bài 36: Luyện tập chung (th4_b36_test1, th4_b36_test2, th4_b36_test3)
- Bài 37: Chia cho số có một chữ số (th4_b37_test1, th4_b37_test2, th4_b37_test3)
- Bài 38: Chia cho số có hai chữ số (th4_b38_test1, th4_b38_test2, th4_b38_test3)
- Bài 39: Luyện tập chung Chủ đề 8 (th4_b39_test1, th4_b39_test2, th4_b39_test3)
Tổng cộng: 24 đề kiểm tra chất lượng cao, độc lập 100%.
"""

from th4_ch8_part1 import get_ch8_part1_exams
from th4_ch8_part2 import get_ch8_part2_exams

def get_exams():
    exams = {}
    exams.update(get_ch8_part1_exams())
    exams.update(get_ch8_part2_exams())
    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 8 Toán 4: {len(ex)} (Kỳ vọng: 24 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
