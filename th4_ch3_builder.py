# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 3: SỐ CÓ NHIỀU CHỮ SỐ (BÀI 10 ĐẾN BÀI 16) - TOÁN 4 KNTT
Gồm 7 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 10: Số có sáu chữ số. Số 1 000 000 (th4_b10_test1, th4_b10_test2, th4_b10_test3)
- Bài 11: Hàng và lớp (th4_b11_test1, th4_b11_test2, th4_b11_test3)
- Bài 12: Các số trong phạm vi lớp triệu (th4_b12_test1, th4_b12_test2, th4_b12_test3)
- Bài 13: Làm tròn số đến hàng trăm nghìn (th4_b13_test1, th4_b13_test2, th4_b13_test3)
- Bài 14: So sánh các số có nhiều chữ số (th4_b14_test1, th4_b14_test2, th4_b14_test3)
- Bài 15: Làm quen với dãy số tự nhiên (th4_b15_test1, th4_b15_test2, th4_b15_test3)
- Bài 16: Luyện tập chung Chủ đề 3 (th4_b16_test1, th4_b16_test2, th4_b16_test3)
Tổng cộng: 21 đề kiểm tra chất lượng cao, độc lập 100%.
"""
import sys
import os

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Đảm bảo đường dẫn import
curr_dir = os.path.dirname(os.path.abspath(__file__))
if curr_dir not in sys.path:
    sys.path.insert(0, curr_dir)

import th4_ch3_part1
import th4_ch3_part2

def get_exams():
    exams = {}
    p1 = th4_ch3_part1.get_part1_exams()
    p2 = th4_ch3_part2.get_part2_exams()
    exams.update(p1)
    exams.update(p2)
    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề kiểm tra Chủ đề 3 Toán 4: {len(ex)}")
    for k in sorted(ex.keys()):
        print(f" - {k}: {ex[k]['title']}")
