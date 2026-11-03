# -*- coding: utf-8 -*-
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

import generator_khtn_phys9 as p9
exams = p9.build_phys9_exams()

print('====================================================')
print('COMPREHENSIVE AUDIT OF PHYS 9 EXAMS (48 EXAMS)')
print('====================================================')

total_exams = len(exams)
print(f'Total exams: {total_exams} (Expected: 48)')
assert total_exams == 48, f'Expected 48, got {total_exams}'

# Group by lesson
by_lesson = {}
for eid, ex in exams.items():
    lid = ex['lessonId']
    if lid not in by_lesson:
        by_lesson[lid] = []
    by_lesson[lid].append((eid, ex))

print(f'Total lessons: {len(by_lesson)} (Expected: 14)')
assert len(by_lesson) == 14, f'Expected 14 lessons, got {len(by_lesson)}'

all_ok = True
prefix_errors = []
dots_errors = []
dup_errors = []
structure_errors = []

for lid, ex_list in by_lesson.items():
    is_rev = 'rev' in lid
    expected_count = 5 if is_rev else 3
    if len(ex_list) != expected_count:
        structure_errors.append(f'Lesson {lid} has {len(ex_list)} exams, expected {expected_count}')

    seen_p1 = {}
    seen_p2 = {}
    seen_p3 = {}
    seen_p4 = {}

    for eid, ex in ex_list:
        # Check structure
        p1 = ex.get('part1', [])
        p2 = ex.get('part2', [])
        p3 = ex.get('part3', [])
        p4 = ex.get('part4', [])

        if len(p1) != 12:
            structure_errors.append(f'{eid} Part 1 has {len(p1)} questions (expected 12)')
        if len(p2) != 4:
            structure_errors.append(f'{eid} Part 2 has {len(p2)} questions (expected 4)')
        for q in p2:
            stmts = q.get('statements', q.get('subQuestions', []))
            if len(stmts) != 4:
                structure_errors.append(f"{eid} Part 2 question {q.get('id')} has {len(stmts)} stmts (expected 4)")
        if len(p3) != 6:
            structure_errors.append(f'{eid} Part 3 has {len(p3)} questions (expected 6)')
        if len(p4) != 4:
            structure_errors.append(f'{eid} Part 4 has {len(p4)} questions (expected 4)')

        # Check prefixes
        for part_name, part_data in [('p1', p1), ('p3', p3), ('p4', p4)]:
            for q in part_data:
                txt = q['question']
                if re.match(r'^(Đề\s*\d+|Đề\s*tổng\s*hợp\s*\d+)', txt, re.IGNORECASE):
                    prefix_errors.append(f"{eid} {part_name} Q{q.get('id')}: {txt[:40]}")
        for q in p2:
            txt = q['question']
            if re.match(r'^(Đề\s*\d+|Đề\s*tổng\s*hợp\s*\d+)', txt, re.IGNORECASE):
                prefix_errors.append(f"{eid} p2 Q{q.get('id')}: {txt[:40]}")
            stmts = q.get('statements', q.get('subQuestions', []))
            for s in stmts:
                stxt = s.get('text', '')
                if re.match(r'^(Đề\s*\d+|Đề\s*tổng\s*hợp\s*\d+)', stxt, re.IGNORECASE):
                    prefix_errors.append(f"{eid} p2 stmt: {stxt[:40]}")

        # Check dots / 'Đáp số:'
        for q in p3:
            txt = q['question']
            if 'Đáp số:' in txt or 'Đáp số :' in txt or '.......' in txt:
                dots_errors.append(f"{eid} p3 Q{q.get('id')}: {txt}")

        # Check duplicates in lesson
        for q in p1:
            q_norm = q['question'].strip()
            if q_norm in seen_p1:
                dup_errors.append(f"Duplicate P1 in {lid}: {eid} vs {seen_p1[q_norm]} -> {q_norm[:50]}")
            else:
                seen_p1[q_norm] = eid

        for q in p2:
            stmts = q.get('statements', q.get('subQuestions', []))
            for s in stmts:
                s_norm = s.get('text', '').strip()
                if s_norm in seen_p2:
                    dup_errors.append(f"Duplicate P2 stmt in {lid}: {eid} vs {seen_p2[s_norm]} -> {s_norm[:50]}")
                else:
                    seen_p2[s_norm] = eid

        for q in p3:
            q_norm = q['question'].strip()
            if q_norm in seen_p3:
                dup_errors.append(f"Duplicate P3 in {lid}: {eid} vs {seen_p3[q_norm]} -> {q_norm[:50]}")
            else:
                seen_p3[q_norm] = eid

        for q in p4:
            q_norm = q['question'].strip()
            if q_norm in seen_p4:
                dup_errors.append(f"Duplicate P4 in {lid}: {eid} vs {seen_p4[q_norm]} -> {q_norm[:50]}")
            else:
                seen_p4[q_norm] = eid

print('\nAUDIT RESULTS:')
print(f'Structure Errors: {len(structure_errors)}')
for e in structure_errors[:5]: print('  ', e)

print(f'Prefix Errors ("Đề X - "): {len(prefix_errors)}')
for e in prefix_errors[:5]: print('  ', e)

print(f'Dots / "Đáp số: ..." Errors: {len(dots_errors)}')
for e in dots_errors[:5]: print('  ', e)

print(f'Duplicate Questions in same lesson: {len(dup_errors)}')
for e in dup_errors: print('  ', e)

if not structure_errors and not prefix_errors and not dots_errors and not dup_errors:
    print('\n>>> ALL 48 EXAMS PASSED 100% OF AUDIT CONSTRAINTS! <<<')
else:
    sys.exit(1)
