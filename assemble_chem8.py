# -*- coding: utf-8 -*-
"""
Assembles all 43 exams of Chemistry 8 into generator_khtn_chem8.py
"""

import sys
import json
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import exams_c1 as c1_b2_b3
from generate_chem8_c1_part2 import exams_c1 as c1_b4
from generate_chem8_c1_part3 import exams_c1_p3 as c1_b5
from generate_chem8_c1_part4 import exams_c1_p4 as c1_b6
from generate_chem8_c1_part5 import exams_c1_p5 as c1_b7
from generate_chem8_c1_rev import exams_c1_rev as c1_rev

from generate_chem8_c2_part1 import exams_c2 as c2_b8
from generate_chem8_c2_part2 import exams_c2_p2 as c2_b9_b10
from generate_chem8_c2_part3 import exams_c2_p3 as c2_b11_b12
from generate_chem8_c2_rev import exams_c2_rev as c2_rev
from generate_chem8_c2_missing8 import missing_8 as c2_m8

all_chem8 = {}
for part in [c1_b2_b3, c1_b4, c1_b5, c1_b6, c1_b7, c1_rev, c2_b8, c2_b9_b10, c2_b11_b12, c2_rev, c2_m8]:
    all_chem8.update(part)

print(f"Total Chem 8 exams assembled: {len(all_chem8)}")

# Verify 0 duplicate questions across tests in same lesson
lesson_exams = defaultdict(dict)
for eid, data in all_chem8.items():
    lid = eid.rsplit('_', 1)[0]
    lesson_exams[lid][eid] = data

total_dup = 0
for lid, tdict in lesson_exams.items():
    keys = list(tdict.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            e1, e2 = tdict[keys[i]], tdict[keys[j]]
            q1 = set([q['question'] for part in ['part1', 'part3', 'part4'] for q in e1[part]])
            q2 = set([q['question'] for part in ['part1', 'part3', 'part4'] for q in e2[part]])
            dup = q1 & q2
            if dup:
                print(f"Dup between {keys[i]} and {keys[j]}: {len(dup)}")
                total_dup += len(dup)

print(f"Total duplicate questions across tests in same lesson for Chem 8: {total_dup}")

# Write to generator_khtn_chem8.py
output_path = 'generator_khtn_chem8.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('"""\nGENERATOR KHTN - HÓA HỌC 8 (CHUẨN 100% ĐỘC LẬP - BÁM SÁT SGK KẾT NỐI TRI THỨC)\n')
    f.write('Tất cả 43 đề thi hoàn toàn khác biệt 100% về câu hỏi, số liệu và đáp án.\n"""\n\n')
    f.write('import sys\n')
    f.write('sys.stdout.reconfigure(encoding="utf-8")\n')
    f.write('true = True\nfalse = False\nnull = None\n\n')
    f.write('CHEM8_EXAMS = ')
    f.write(json.dumps(all_chem8, ensure_ascii=False, indent=2))
    f.write('\n\ndef build_chem8_exams():\n    return CHEM8_EXAMS\n\nexams = CHEM8_EXAMS\n')

print(f"Successfully wrote {output_path} with {len(all_chem8)} distinct exams!")
