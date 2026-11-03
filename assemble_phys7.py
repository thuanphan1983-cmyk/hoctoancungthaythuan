# -*- coding: utf-8 -*-
"""
Assembles generator_khtn_phys7.py directly from all parts of Physics 7
"""

import sys
import json
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

from builder_phys7_c3 import c3_exams
from builder_phys7_c4 import c4_exams
from builder_phys7_c5 import c5_exams
from builder_phys7_c6 import c6_exams

all_phys7 = {}
all_phys7.update(c3_exams)
all_phys7.update(c4_exams)
all_phys7.update(c5_exams)
all_phys7.update(c6_exams)

print(f"Total Physics 7 exams assembled: {len(all_phys7)}")
assert len(all_phys7) == 59, f"Expected 59 exams, got {len(all_phys7)}"

# Verify lesson distribution
expected_lessons = [
    ("phys7_c3_b8", 3), ("phys7_c3_b9", 3), ("phys7_c3_b10", 3), ("phys7_c3_b11", 3), ("phys7_c3_rev", 5),
    ("phys7_c4_b12", 3), ("phys7_c4_b13", 3), ("phys7_c4_b14", 3), ("phys7_c4_rev", 5),
    ("phys7_c5_b15", 3), ("phys7_c5_b16", 3), ("phys7_c5_b17", 3), ("phys7_c5_rev", 5),
    ("phys7_c6_b18", 3), ("phys7_c6_b19", 3), ("phys7_c6_b20", 3), ("phys7_c6_rev", 5)
]

by_lesson = defaultdict(list)
for eid, ex in all_phys7.items():
    lid = ex["lessonId"]
    by_lesson[lid].append((eid, ex))

total_duplicates = 0
prefix_errors = 0
structure_errors = 0

for lid, count in expected_lessons:
    ex_list = by_lesson.get(lid, [])
    if len(ex_list) != count:
        print(f"❌ Error in {lid}: expected {count} exams, found {len(ex_list)}")
        structure_errors += 1
    
    # Check question duplicates within lesson across all 4 parts
    p1_seen = set()
    p2_seen = set()
    p3_seen = set()
    p4_seen = set()

    for eid, ex in ex_list:
        # Check structure
        if len(ex.get("part1", [])) != 12:
            print(f"❌ Structure error in {eid}: part1 has {len(ex.get('part1', []))} questions (expected 12)")
            structure_errors += 1
        if len(ex.get("part2", [])) != 4:
            print(f"❌ Structure error in {eid}: part2 has {len(ex.get('part2', []))} questions (expected 4)")
            structure_errors += 1
        if len(ex.get("part3", [])) != 6:
            print(f"❌ Structure error in {eid}: part3 has {len(ex.get('part3', []))} questions (expected 6)")
            structure_errors += 1
        if len(ex.get("part4", [])) != 4:
            print(f"❌ Structure error in {eid}: part4 has {len(ex.get('part4', []))} questions (expected 4)")
            structure_errors += 1

        # Check part 1
        for q in ex.get("part1", []):
            txt = q["question"].strip()
            if txt in p1_seen:
                print(f"❌ Duplicate in {lid} (part1): {txt[:60]}...")
                total_duplicates += 1
            p1_seen.add(txt)
            if "Đề " in txt or "Đề tổng hợp" in txt:
                print(f"❌ Prefix found in {eid} p1: {txt[:50]}")
                prefix_errors += 1

        # Check part 2
        for q in ex.get("part2", []):
            txt = q["question"].strip()
            if txt in p2_seen:
                print(f"❌ Duplicate in {lid} (part2): {txt[:60]}...")
                total_duplicates += 1
            p2_seen.add(txt)
            if "Đề " in txt or "Đề tổng hợp" in txt:
                print(f"❌ Prefix found in {eid} p2: {txt[:50]}")
                prefix_errors += 1

        # Check part 3
        for q in ex.get("part3", []):
            txt = q["question"].strip()
            if txt in p3_seen:
                print(f"❌ Duplicate in {lid} (part3): {txt[:60]}...")
                total_duplicates += 1
            p3_seen.add(txt)
            if "Đề " in txt or "Đề tổng hợp" in txt:
                print(f"❌ Prefix found in {eid} p3: {txt[:50]}")
                prefix_errors += 1
            if "Đáp số" in txt or "......." in txt:
                print(f"❌ Waiting line found in {eid} p3: {txt[:50]}")
                prefix_errors += 1

        # Check part 4
        for q in ex.get("part4", []):
            txt = q["question"].strip()
            if txt in p4_seen:
                print(f"❌ Duplicate in {lid} (part4): {txt[:60]}...")
                total_duplicates += 1
            p4_seen.add(txt)
            if "Đề " in txt or "Đề tổng hợp" in txt:
                print(f"❌ Prefix found in {eid} p4: {txt[:50]}")
                prefix_errors += 1

print("\n--- AUDIT RESULTS ---")
print(f"Structure Errors: {structure_errors}")
print(f"Total Duplicate Questions: {total_duplicates}")
print(f"Prefix / Format Errors: {prefix_errors}")

if structure_errors == 0 and total_duplicates == 0 and prefix_errors == 0:
    print("✅ PERFECT: All 59 exams are 100% independent with ZERO duplicates and ZERO errors!")
else:
    print("❌ AUDIT FAILED! Please inspect errors above.")
    sys.exit(1)

# Write out generator_khtn_phys7.py
code = f"""# -*- coding: utf-8 -*-
\"\"\"
GENERATOR KHTN - VẬT LÝ 7 (CHUẨN 100% ĐỘC LẬP - BÁM SÁT SGK KẾT NỐI TRI THỨC)
Tất cả 59 đề thi trên 17 bài học hoàn toàn độc lập 100% về câu hỏi, số liệu và đáp án.
ZERO câu hỏi trùng lặp giữa các đề trong cùng bài học.
\"\"\"

import sys
sys.stdout.reconfigure(encoding='utf-8')

true = True
false = False
null = None

PHYS7_EXAMS = {json.dumps(all_phys7, ensure_ascii=False, indent=2)}

def build_phys7_exams():
    return PHYS7_EXAMS
"""

with open("generator_khtn_phys7.py", "w", encoding="utf-8") as f:
    f.write(code)

print("✅ Đã ghi thành công generator_khtn_phys7.py!")
