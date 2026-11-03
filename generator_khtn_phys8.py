# -*- coding: utf-8 -*-
"""
GENERATOR KHTN VẬT LÝ 8 - 71 ĐỀ ĐỘC LẬP 100% (KNTT)
Gồm 4 chương:
- Chương III: Khối lượng riêng và áp suất (20 đề)
- Chương IV: Tác dụng làm quay của lực (11 đề)
- Chương V: Điện (23 đề)
- Chương VI: Nhiệt (17 đề)
Tổng cộng: 71 đề thi độc lập 100%
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys8_c3 import get_c3_exams
from build_phys8_c3_part2 import get_c3_part2_exams
from build_phys8_c3_part3 import get_c3_part3_exams
from build_phys8_c4 import get_c4_exams
from build_phys8_c5_part1 import get_c5_part1_exams
from build_phys8_c5_part2 import get_c5_part2_exams
from build_phys8_c6 import get_c6_exams

def build_phys8_exams():
    exams = {}
    exams.update(get_c3_exams())
    exams.update(get_c3_part2_exams())
    exams.update(get_c3_part3_exams())
    exams.update(get_c4_exams())
    exams.update(get_c5_part1_exams())
    exams.update(get_c5_part2_exams())
    exams.update(get_c6_exams())
    return exams

if __name__ == '__main__':
    exs = build_phys8_exams()
    print("Tổng số đề Vật lý 8 đã sinh thành công:", len(exs))
