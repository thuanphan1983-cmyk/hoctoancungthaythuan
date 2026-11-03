# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 10: PHÂN SỐ (BÀI 44 ĐẾN BÀI 50) - TOÁN 4 KNTT
Gồm 7 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 44: Khái niệm phân số (th4_b44_test1, th4_b44_test2, th4_b44_test3)
- Bài 45: Phân số và phép chia số tự nhiên (th4_b45_test1, th4_b45_test2, th4_b45_test3)
- Bài 46: Phân số bằng nhau (th4_b46_test1, th4_b46_test2, th4_b46_test3)
- Bài 47: Rút gọn phân số (th4_b47_test1, th4_b47_test2, th4_b47_test3)
- Bài 48: Quy đồng mẫu số các phân số (th4_b48_test1, th4_b48_test2, th4_b48_test3)
- Bài 49: So sánh hai phân số (th4_b49_test1, th4_b49_test2, th4_b49_test3)
- Bài 50: Luyện tập chung Chủ đề 10 (th4_b50_test1, th4_b50_test2, th4_b50_test3)
Tổng cộng: 21 đề kiểm tra chất lượng cao, độc lập 100%.
"""

from th4_ch10_part1 import get_ch10_part1_exams
from th4_ch10_part2 import get_ch10_part2_exams

def get_exams():
    exams = {}
    exams.update(get_ch10_part1_exams())
    exams.update(get_ch10_part2_exams())
    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 10 Toán 4: {len(ex)} (Kỳ vọng: 21 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
