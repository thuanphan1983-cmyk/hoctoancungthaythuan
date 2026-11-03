# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 13: ÔN TẬP CUỐI NĂM (BÀI 59 ĐẾN BÀI 63)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Xuất hàm get_exams() trả về dictionary của 15 đề thi (Bài 59 đến Bài 63, mỗi bài 3 đề).
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from th4_ch13_part1 import get_ch13_part1_exams
from th4_ch13_part2 import get_ch13_part2_exams

def get_exams():
    exams = {}
    exams.update(get_ch13_part1_exams())
    exams.update(get_ch13_part2_exams())
    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 13: {len(ex)} (Kỳ vọng: 15 đề)")
    for b in range(59, 64):
        for t in range(1, 4):
            key = f"th4_b{b}_test{t}"
            assert key in ex, f"Thiếu mã đề {key}"
            assert len(ex[key]["part1"]) == 6, f"part1 của {key} không đủ 6 câu"
            assert len(ex[key]["part2"]) == 6, f"part2 của {key} không đủ 6 bài"
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6, f"Điểm part1 của {key} khác 3.0"
            assert abs(p2_pts - 7.0) < 1e-6, f"Điểm part2 của {key} khác 7.0"
            assert abs(p1_pts + p2_pts - 10.0) < 1e-6, f"Tổng điểm của {key} khác 10.0"
    print("Tất cả 15 đề của Chủ đề 13 hoàn hảo 100%!")
