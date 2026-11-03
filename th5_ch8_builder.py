# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 8: HÌNH HỘP CHỮ NHẬT, HÌNH LẬP PHƯƠNG, HÌNH TRỤ (BÀI 38 ĐẾN BÀI 44) - TOÁN 5 KNTT
Gồm 7 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 38: Hình hộp chữ nhật, hình lập phương (th5_b38_test1, th5_b38_test2, th5_b38_test3)
- Bài 39: Diện tích xung quanh và toàn phần hình hộp chữ nhật (th5_b39_test1, th5_b39_test2, th5_b39_test3)
- Bài 40: Diện tích xung quanh và toàn phần hình lập phương (th5_b40_test1, th5_b40_test2, th5_b40_test3)
- Bài 41: Thể tích hình hộp chữ nhật (th5_b41_test1, th5_b41_test2, th5_b41_test3)
- Bài 42: Thể tích hình lập phương (th5_b42_test1, th5_b42_test2, th5_b42_test3)
- Bài 43: Giới thiệu hình trụ (th5_b43_test1, th5_b43_test2, th5_b43_test3)
- Bài 44: Luyện tập chung Chủ đề 8 (th5_b44_test1, th5_b44_test2, th5_b44_test3)
Tổng cộng: 21 đề kiểm tra chất lượng cao, độc lập 100%.
"""

from th5_ch8_part1 import get_ch8_part1_exams
from th5_ch8_part2 import get_ch8_part2_exams

def get_exams():
    exams = {}
    exams.update(get_ch8_part1_exams())
    exams.update(get_ch8_part2_exams())
    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 8: {len(ex)} (Kỳ vọng: 21 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
