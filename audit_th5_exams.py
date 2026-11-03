# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from generator_th5_gk2 import get_th5_gk2_exams
from generator_th5_ck2 import get_th5_ck2_exams

def audit_exams(module_name, exams, expected_prefix):
    print(f"\n==================== AUDITING {module_name} ====================")
    assert len(exams) == 8, f"Expected 8 exams, got {len(exams)}"
    
    expected_ids = [f"{expected_prefix}_de0{i}" for i in range(1, 9)]
    all_questions = set()
    
    for i, eid in enumerate(expected_ids, start=1):
        assert eid in exams, f"Missing exam id {eid}"
        ex = exams[eid]
        print(f"Checking {eid}: {ex['title']}...")
        
        assert ex["duration"] == "40 phút", f"Invalid duration {ex['duration']} in {eid}"
        assert ex["points"] == 10.0, f"Invalid points {ex['points']} in {eid}"
        assert ex["grade"] == "5", f"Invalid grade in {eid}"
        
        # Check part 1
        part1 = ex["part1"]
        assert len(part1) == 6, f"{eid} part1 has {len(part1)} items, expected 6"
        p1_points_sum = 0.0
        for q_idx, q in enumerate(part1, start=1):
            assert q["id"] == q_idx, f"{eid} part1 item {q_idx} has id {q['id']}"
            assert q["question"].startswith(f"**Câu {q_idx}:** "), f"{eid} Q{q_idx} invalid prefix: {q['question'][:15]}"
            assert len(q["options"]) == 4, f"{eid} Q{q_idx} options count {len(q['options'])}"
            assert q["correct"] in [0, 1, 2, 3], f"{eid} Q{q_idx} correct index {q['correct']}"
            assert len(q["explanation"].strip()) > 0, f"{eid} Q{q_idx} empty explanation"
            p1_points_sum += q.get("points", 0.5)
            
            # Duplication check
            q_stem = q["question"]
            assert q_stem not in all_questions, f"Duplicate question across exams: {q_stem}"
            all_questions.add(q_stem)
            
        assert abs(p1_points_sum - 3.0) < 1e-6, f"{eid} part1 sum points {p1_points_sum} != 3.0"
        
        # Check part 2
        part2 = ex["part2"]
        assert len(part2) == 6, f"{eid} part2 has {len(part2)} items, expected 6"
        expected_p2_points = [1.0, 1.0, 1.0, 1.5, 1.5, 1.0]
        p2_points_sum = 0.0
        for p_idx, p in enumerate(part2, start=1):
            assert p["id"] == p_idx, f"{eid} part2 item {p_idx} has id {p['id']}"
            assert p["question"].startswith(f"**Bài {p_idx}:** "), f"{eid} P{p_idx} invalid prefix: {p['question'][:15]}"
            assert len(p["solution"].strip()) > 0, f"{eid} P{p_idx} empty solution"
            assert len(p["answer"].strip()) > 0, f"{eid} P{p_idx} empty answer"
            assert 3 <= p["lineCount"] <= 8, f"{eid} P{p_idx} lineCount {p['lineCount']} out of range [3..8]"
            assert p["points"] == expected_p2_points[p_idx - 1], f"{eid} P{p_idx} points {p['points']} != {expected_p2_points[p_idx-1]}"
            p2_points_sum += p["points"]
            
            # Duplication check
            p_stem = p["question"]
            assert p_stem not in all_questions, f"Duplicate essay question across exams: {p_stem}"
            all_questions.add(p_stem)
            
        assert abs(p2_points_sum - 7.0) < 1e-6, f"{eid} part2 sum points {p2_points_sum} != 7.0"
        assert abs(p1_points_sum + p2_points_sum - 10.0) < 1e-6, f"{eid} total points != 10.0"
        
    print(f"--> ALL 8 EXAMS OF {module_name} PASSED 100% VALIDATION WITH 0 ERRORS AND 0 DUPLICATES!")

if __name__ == "__main__":
    gk2_exams = get_th5_gk2_exams()
    audit_exams("GK2 (th5_gk2)", gk2_exams, "th5_gk2")
    
    ck2_exams = get_th5_ck2_exams()
    audit_exams("CK2 (th5_ck2)", ck2_exams, "th5_ck2")
    
    print("\n=======================================================")
    print("SUCCESS: 16 EXAMS (8 GK2 + 8 CK2) AUDITED 100% PERFECT!")
    print("=======================================================")
