# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 5: ÔN TẬP HỌC KÌ 1 (BÀI 26 ĐẾN BÀI 29) - TOÁN 5 KNTT
Gồm 4 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 26: Ôn tập về số và các phép tính (th5_b26_test1, th5_b26_test2, th5_b26_test3)
- Bài 27: Ôn tập hình học và đo lường (th5_b27_test1, th5_b27_test2, th5_b27_test3)
- Bài 28: Ôn tập một số yếu tố xác suất và thống kê (th5_b28_test1, th5_b28_test2, th5_b28_test3)
- Bài 29: Luyện tập chung Học kì 1 (th5_b29_test1, th5_b29_test2, th5_b29_test3)
Tổng cộng: 12 đề kiểm tra chất lượng cao, độc lập 100%.
"""

from th5_ch5_part1 import get_ch5_part1_exams
from th5_ch5_part2 import get_ch5_part2_exams

def get_exams():
    exams = {}
    exams.update(get_ch5_part1_exams())
    exams.update(get_ch5_part2_exams())
    
    lesson_topics = {
        26: "Ôn tập về số và các phép tính",
        27: "Ôn tập hình học và đo lường",
        28: "Ôn tập một số yếu tố xác suất và thống kê",
        29: "Luyện tập chung Học kì 1"
    }

    # Chuẩn hóa metadata và các trường id, options, choices cho từng câu hỏi
    for eid, ex in exams.items():
        # Phân tích eid: th5_b[lesson]_test[t]
        parts = eid.split("_")
        lesson_num = int(parts[1].replace("b", ""))
        test_num = int(parts[2].replace("test", ""))
        
        ex["id"] = eid
        ex["lessonId"] = f"th5_b{lesson_num}"
        ex["lessonNum"] = lesson_num
        ex["testNum"] = test_num
        ex["topic"] = lesson_topics.get(lesson_num, "")
        ex["chapter"] = "Chủ đề 5: Ôn tập học kì 1"
        ex["grade"] = "5"
        ex["term"] = "hk1"

        for i, q in enumerate(ex.get("part1", []), start=1):
            if "id" not in q:
                q["id"] = i
            if "options" not in q and "choices" in q:
                q["options"] = q["choices"]
            elif "choices" not in q and "options" in q:
                q["choices"] = q["options"]
        for i, b in enumerate(ex.get("part2", []), start=1):
            if "id" not in b:
                b["id"] = i
    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 5: {len(ex)} (Kỳ vọng: 12 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
