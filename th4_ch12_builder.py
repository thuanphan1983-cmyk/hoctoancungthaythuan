# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 12: PHÉP NHÂN, PHÉP CHIA PHÂN SỐ (BÀI 55 ĐẾN BÀI 58)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 4 bài học x 3 đề độc lập = 12 đề kiểm tra chất lượng cao (th4_b55_test1 -> th4_b58_test3)
Xuất hàm get_exams() trả về dictionary gồm 12 đề.
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

import th4_ch12_part1
import th4_ch12_part2

def get_exams():
    exams = {}
    p1 = th4_ch12_part1.get_part1_exams()
    p2 = th4_ch12_part2.get_part2_exams()
    exams.update(p1)
    exams.update(p2)
    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề thi Chủ đề 12: {len(ex)}")
    for k, v in ex.items():
        print(f" - {k}: {v['title']} ({len(v['part1'])} MCQs, {len(v['part2'])} Essays)")
