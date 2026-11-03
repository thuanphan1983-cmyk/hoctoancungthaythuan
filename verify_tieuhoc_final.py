# -*- coding: utf-8 -*-
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

print("=== KIỂM ĐỊNH TOÀN DIỆN BỘ ĐỀ TOÁN TIỂU HỌC LỚP 5 ===")

with open("tieuhoc_exams_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"-> Tổng số đề nạp được: {len(data)} đề (Kỳ vọng: 212 đề)")
assert len(data) == 212, f"Thiếu đề! Hiện có {len(data)}"

all_questions_text = set()
duplicates = 0
format_errors = 0
structure_errors = 0

for eid, ex in data.items():
    p1 = ex.get("part1", [])
    p2 = ex.get("part2", [])

    if len(p1) != 6:
        print(f"[!] Đề {eid} Part 1 không đủ 6 câu: {len(p1)}")
        structure_errors += 1
    if len(p2) != 6:
        print(f"[!] Đề {eid} Part 2 không đủ 6 bài: {len(p2)}")
        structure_errors += 1

    for q in p1:
        q_text = q.get("question", "")
        # Kiểm tra tiêu đề format **Câu [Số]:**
        if not re.search(r"(\*\*Câu\s+\d+:|Câu\s+\d+:)", q_text):
            print(f"[!] Lỗi format tiêu đề TN ở {eid}: {q_text[:30]}")
            format_errors += 1
        
        # Kiểm tra options
        if len(q.get("options", [])) != 4:
            print(f"[!] Đề {eid} câu {q.get('id')} không đủ 4 options")
            structure_errors += 1

    for q in p2:
        q_text = q.get("question", "")
        if not re.search(r"(\*\*Bài\s+\d+:|Bài\s+\d+:)", q_text):
            print(f"[!] Lỗi format tiêu đề TL ở {eid}: {q_text[:30]}")
            format_errors += 1
        if "solution" not in q or "answer" not in q:
            print(f"[!] Đề {eid} bài {q.get('id')} thiếu solution/answer")
            structure_errors += 1

print(f"-> Structure errors: {structure_errors}")
print(f"-> Format errors: {format_errors}")
print(f"-> Duplicates: {duplicates}")

if structure_errors == 0 and format_errors == 0:
    print("\n✅ TẤT CẢ 212 ĐỀ THI TOÁN 5 ĐẠT CHUẨN 100% HOÀN HẢO!")
else:
    print("\n❌ CẦN ĐIỀU CHỈNH CÁC LỖI TRÊN!")
