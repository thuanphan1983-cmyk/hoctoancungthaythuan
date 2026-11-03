# -*- coding: utf-8 -*-
"""
CHƯƠNG VI: NHIỆT (17 ĐỀ THI ĐỘC LẬP 100%):
- phys8_c6_b26: Bài 26: Năng lượng nhiệt và nội năng (3 đề)
- phys8_c6_b27: Bài 27: Thực hành đo năng lượng nhiệt bằng nhiệt lượng kế (3 đề)
- phys8_c6_b28: Bài 28: Sự truyền nhiệt (3 đề)
- phys8_c6_b29: Bài 29: Sự nở vì nhiệt (3 đề)
- phys8_c6_rev: Ôn tập cuối Chương VI (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from make_phys8_c6_b26 import get_b26_exams
from make_phys8_c6_b27 import get_b27_exams
from make_phys8_c6_b28 import get_b28_exams
from make_phys8_c6_b29 import get_b29_exams
from make_phys8_c6_rev import get_c6_rev_exams

def get_c6_exams():
    exams = {}
    exams.update(get_b26_exams())
    exams.update(get_b27_exams())
    exams.update(get_b28_exams())
    exams.update(get_b29_exams())
    exams.update(get_c6_rev_exams())
    return exams

if __name__ == '__main__':
    exs = get_c6_exams()
    print("Total C6 exams:", len(exs))
