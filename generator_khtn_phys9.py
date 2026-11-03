# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - VẬT LÝ 9 (KNTT)
Gồm 14 bài/chuyên đề ôn tập => 48 đề thi độc lập 100%
Cấu trúc mỗi đề: 12 TN + 4 Đ/S (16 ý) + 6 TLN + 4 VDC (TN nâng cao) = 26 câu, 10.0 điểm.
Tỷ lệ ma trận: 30% NB, 30% TH, 20% VD, 20% VDC.
Tuyệt đối không có tiền tố "Đề X - " hay "Đề tổng hợp X - ".
Tuyệt đối không có dòng chờ điền đáp án "Đáp số: ......".

Chương VI: Ánh sáng (6 bài, 20 đề)
- phys9_c6_b17: Bài 17: Hiện tượng khúc xạ ánh sáng (3 đề)
- phys9_c6_b18: Bài 18: Hiện tượng phản xạ toàn phần (3 đề)
- phys9_c6_b19: Bài 19: Thấu kính (3 đề)
- phys9_c6_b20: Bài 20: Thực hành xác định tiêu cự của thấu kính hội tụ (3 đề)
- phys9_c6_b21: Bài 21: Kính lúp (3 đề)
- phys9_c6_rev: [Đề tổng hợp] Ôn tập cuối Chương VI (5 đề)

Chương VII: Điện từ (5 bài, 17 đề)
- phys9_c7_b22: Bài 22: Từ trường của ống dây có dòng điện. Nam châm điện (3 đề)
- phys9_c7_b23: Bài 23: Tác dụng của từ trường lên đoạn dây dẫn mang dòng điện (3 đề)
- phys9_c7_b24: Bài 24: Hiện tượng cảm ứng điện từ. Dòng điện xoay chiều (3 đề)
- phys9_c7_b25: Bài 25: Máy biến thế (3 đề)
- phys9_c7_rev: [Đề tổng hợp] Ôn tập cuối Chương VII (5 đề)

Chương VIII: Năng lượng và sự biến đổi năng lượng (3 bài, 11 đề)
- phys9_c8_b26: Bài 26: Năng lượng của Trái Đất. Năng lượng hoá thạch (3 đề)
- phys9_c8_b27: Bài 27: Năng lượng tái tạo (3 đề)
- phys9_c8_rev: [Đề tổng hợp] Ôn tập cuối Chương VIII (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import build_c6
from build_phys9_c7 import build_c7
from build_phys9_c8 import build_c8

def build_phys9_exams():
    exams = {}
    exams.update(build_c6())
    exams.update(build_c7())
    exams.update(build_c8())
    return exams

PHYS9_EXAMS = build_phys9_exams()

if __name__ == "__main__":
    exs = build_phys9_exams()
    print(f"Phys 9 generated total: {len(exs)} exams.")
