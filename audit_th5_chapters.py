# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import th5_ch6_builder
import th5_ch7_builder
import th5_ch8_builder

def audit_chapter_exams(chapter_name, exams, expected_count, lesson_start, lesson_end):
    print(f"\n==================== AUDITING {chapter_name} ====================")
    assert len(exams) == expected_count, f"{chapter_name} expected {expected_count} exams, got {len(exams)}"
    
    all_questions = set()
    
    for l_num in range(lesson_start, lesson_end + 1):
        for t_num in range(1, 4):
            eid = f"th5_b{l_num}_test{t_num}"
            assert eid in exams, f"Missing exam {eid} in {chapter_name}"
            ex = exams[eid]
            
            assert ex["points"] == 10.0, f"{eid} points != 10.0"
            assert ex["grade"] == "5", f"{eid} grade != 5"
            assert ex["term"] == "hk2", f"{eid} term != hk2"
            
            # Check Part 1
            part1 = ex["part1"]
            assert len(part1) == 6, f"{eid} part1 length != 6"
            p1_points = 0.0
            for q_idx, q in enumerate(part1, start=1):
                assert q["id"] == q_idx, f"{eid} Q{q_idx} id mismatch"
                assert q["question"].startswith(f"**Câu {q_idx}:** "), f"{eid} Q{q_idx} format invalid: {q['question'][:15]}"
                assert len(q["options"]) == 4, f"{eid} Q{q_idx} options count != 4"
                assert q["correct"] in [0, 1, 2, 3], f"{eid} Q{q_idx} correct invalid"
                assert len(q["explanation"].strip()) > 0, f"{eid} Q{q_idx} empty explanation"
                p1_points += q.get("points", 0.5)
                
                # Check duplication
                assert q["question"] not in all_questions, f"Duplicate question: {q['question']}"
                all_questions.add(q["question"])
                
            assert abs(p1_points - 3.0) < 1e-6, f"{eid} part1 points != 3.0"
            
            # Check Part 2
            part2 = ex["part2"]
            assert len(part2) == 6, f"{eid} part2 length != 6"
            expected_p2 = [1.0, 1.0, 1.0, 1.5, 1.5, 1.0]
            p2_points = 0.0
            for p_idx, p in enumerate(part2, start=1):
                assert p["id"] == p_idx, f"{eid} P{p_idx} id mismatch"
                assert p["question"].startswith(f"**Bài {p_idx}:** "), f"{eid} P{p_idx} format invalid: {p['question'][:15]}"
                assert len(p["solution"].strip()) > 0, f"{eid} P{p_idx} empty solution"
                assert len(p["answer"].strip()) > 0, f"{eid} P{p_idx} empty answer"
                assert 4 <= p["lineCount"] <= 6, f"{eid} P{p_idx} lineCount {p['lineCount']} not in [4..6]"
                assert p["points"] == expected_p2[p_idx - 1], f"{eid} P{p_idx} points mismatch"
                p2_points += p["points"]
                
                # Check duplication
                assert p["question"] not in all_questions, f"Duplicate essay: {p['question']}"
                all_questions.add(p["question"])
                
            assert abs(p2_points - 7.0) < 1e-6, f"{eid} part2 points != 7.0"
            assert abs(p1_points + p2_points - 10.0) < 1e-6, f"{eid} total != 10.0"
            
    print(f"--> SUCCESS: {chapter_name} ({len(exams)} exams) PASSED 100% VALIDATION WITH 0 ERRORS AND 0 DUPLICATES!")

if __name__ == "__main__":
    ch6 = th5_ch6_builder.get_exams()
    audit_chapter_exams("CHỦ ĐỀ 6: TỈ SỐ PHẦN TRĂM", ch6, 15, 30, 34)
    
    ch7 = th5_ch7_builder.get_exams()
    audit_chapter_exams("CHỦ ĐỀ 7: THỂ TÍCH. ĐƠN VỊ ĐO THỂ TÍCH", ch7, 9, 35, 37)
    
    ch8 = th5_ch8_builder.get_exams()
    audit_chapter_exams("CHỦ ĐỀ 8: HÌNH HỘP CHỮ NHẬT, HÌNH LẬP PHƯƠNG, HÌNH TRỤ", ch8, 21, 38, 44)
    
    print("\n=================================================================")
    print("ALL 45 EXAMS (15 CH6 + 9 CH7 + 21 CH8) VERIFIED 100% PERFECT!")
    print("=================================================================")
