# -*- coding: utf-8 -*-
import sys
import re
from collections import defaultdict
import generator_khtn_chem9 as c9

sys.stdout.reconfigure(encoding='utf-8')

exams = c9.build_chem9_exams()
print(f"Total exams loaded: {len(exams)}")
assert len(exams) == 73, f"Expected 73 exams, got {len(exams)}"

lesson_exams = defaultdict(list)
total_questions = 0
prefix_errors = 0
dap_so_errors = 0
schema_errors = 0

for eid, exam in exams.items():
    lid = exam.get('lessonId')
    assert lid, f"Exam {eid} missing lessonId"
    lesson_exams[lid].append((eid, exam))
    
    # Check parts
    p1 = exam.get('part1', [])
    p2 = exam.get('part2', [])
    p3 = exam.get('part3', [])
    p4 = exam.get('part4', [])
    
    if len(p1) != 12:
        print(f"Schema error in {eid}: part1 has {len(p1)} questions (expected 12)")
        schema_errors += 1
    if len(p2) != 4:
        print(f"Schema error in {eid}: part2 has {len(p2)} questions (expected 4)")
        schema_errors += 1
    if len(p3) != 6:
        print(f"Schema error in {eid}: part3 has {len(p3)} questions (expected 6)")
        schema_errors += 1
    if len(p4) != 4:
        print(f"Schema error in {eid}: part4 has {len(p4)} questions (expected 4)")
        schema_errors += 1
        
    for p_name, p_list in [('part1', p1), ('part2', p2), ('part3', p3), ('part4', p4)]:
        for q in p_list:
            total_questions += 1
            qtxt = q.get('question', '')
            # check prefix
            if re.match(r'^Đề\s+(\d+|tổng\s+hợp\s+\d+)\s*[-:]', qtxt, re.IGNORECASE):
                print(f"Prefix error in {eid} {p_name} Q{q.get('id')}: {qtxt[:40]}")
                prefix_errors += 1
            if 'Đáp số:' in qtxt or 'Đáp số :' in qtxt or '.........' in qtxt:
                print(f"Dap so error in {eid} {p_name} Q{q.get('id')}: {qtxt[:40]}")
                dap_so_errors += 1
                
    # Check part2 statements
    for q in p2:
        stmts = q.get('statements', [])
        if len(stmts) != 4:
            print(f"Part2 statements error in {eid} Q{q.get('id')}: has {len(stmts)} stmts")
            schema_errors += 1
        for s in stmts:
            if not isinstance(s.get('correct'), bool):
                print(f"Part2 boolean error in {eid} Q{q.get('id')} sub {s.get('subId')}")
                schema_errors += 1

print(f"Total questions validated across 73 exams: {total_questions}")
print(f"Prefix errors: {prefix_errors}")
print(f"Dap so errors: {dap_so_errors}")
print(f"Schema errors: {schema_errors}")

print(f"\nChecking duplicates across all {len(lesson_exams)} lessons...")
total_duplicates = 0
for lid, ex_list in sorted(lesson_exams.items()):
    lesson_dups = 0
    for part in ['part1', 'part2', 'part3', 'part4']:
        seen = {}
        for eid, exam in ex_list:
            for q in exam[part]:
                qtxt = q['question'].strip()
                if qtxt in seen:
                    print(f"  [DUPLICATE] in {lid} ({part}): '{qtxt[:50]}...' between {seen[qtxt]} and {eid}")
                    lesson_dups += 1
                else:
                    seen[qtxt] = eid
    if lesson_dups > 0:
        print(f"Lesson {lid}: FAILED with {lesson_dups} duplicates")
        total_duplicates += lesson_dups
    else:
        print(f"Lesson {lid} ({len(ex_list)} exams): PASSED (0 duplicates)")

print("=" * 60)
print(f"FINAL RESULT: Total duplicates = {total_duplicates}")
if total_duplicates == 0 and prefix_errors == 0 and dap_so_errors == 0 and schema_errors == 0 and len(exams) == 73:
    print("ALL 73 EXAMS IN CHEMISTRY 9 ARE 100% INDEPENDENT AND VALIDATED! PERFECT!")
else:
    print("VALIDATION FAILED! PLEASE REVIEW ERRORS ABOVE.")
print("=" * 60)
