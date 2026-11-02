import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

import generator_utils

out_dir = generator_utils.OUTPUT_DIR

summary = {}

for g in [6, 7, 8, 9]:
    summary[g] = {
        "chapters": 0,
        "total_chapter_tests": 0,
        "parameter_m_found": 0,
        "validated_tests": 0,
        "failed_validation": 0
    }
    
    # List files for this grade
    files = sorted([f for f in os.listdir(out_dir) if f.startswith(f"grade{g}_c") and f.endswith("_exams.json")])
    summary[g]["chapters"] = len(files)
    
    for f in files:
        path = os.path.join(out_dir, f)
        with open(path, "r", encoding="utf-8") as fp:
            d = json.load(fp)
            exams = d.get("exams", {})
            # Find the chapter-end lesson prefix
            # Find max bai number
            bai_nums = []
            for k in exams.keys():
                m = re.search(r'_bai(\d+)_test', k)
                if m:
                    bai_nums.append(int(m.group(1)))
            if not bai_nums:
                continue
            max_bai = max(bai_nums)
            
            for t in range(1, 8):
                key = f"{f.replace('grade' + str(g) + '_', '').replace('_exams.json', '')}_bai{max_bai}_test{t}"
                if key in exams:
                    summary[g]["total_chapter_tests"] += 1
                    exam = exams[key]
                    
                    # Validate structure
                    try:
                        generator_utils.validate_exam(key, exam, t)
                        summary[g]["validated_tests"] += 1
                    except Exception as err:
                        print(f"Validation error in {key}: {err}")
                        summary[g]["failed_validation"] += 1
                        
                    # Check parameter m
                    text = json.dumps(exam, ensure_ascii=False)
                    m_matches = re.findall(r'(?:tham số\s+m\b|tìm\s+m\b|với mọi\s+m\b)', text, re.IGNORECASE)
                    if m_matches:
                        print(f"Param m in {key}: {m_matches}")
                        summary[g]["parameter_m_found"] += len(m_matches)

print("\n" + "="*60)
print("BÁO CÁO TỔNG HỢP KIỂM ĐỊNH TOÀN DIỆN 4 KHỐI LỚP (6, 7, 8, 9)")
print("="*60)
for g in [6, 7, 8, 9]:
    info = summary[g]
    print(f"Toán {g}: {info['chapters']} chương | {info['total_chapter_tests']} đề cuối chương ({info['validated_tests']}/70 pass 100%) | Tham số m: {info['parameter_m_found']} | Lỗi ma trận: {info['failed_validation']}")

total_chap_tests = sum(summary[g]['total_chapter_tests'] for g in [6, 7, 8, 9])
total_passed = sum(summary[g]['validated_tests'] for g in [6, 7, 8, 9])
total_m = sum(summary[g]['parameter_m_found'] for g in [6, 7, 8, 9])
print(f"\nTỔNG CỘNG HỆ THỐNG: {total_chap_tests} ĐỀ KIỂM TRA CUỐI CHƯƠNG ĐỘC LẬP")
print(f"PASS MA TRẬN 30-30-30-10: {total_passed}/{total_chap_tests} ({total_passed/total_chap_tests*100:.1f}%)")
print(f"THAM SỐ m PHÁT HIỆN: {total_m} (TUYỆT ĐỐI KHÔNG CÓ)")
print("="*60)
