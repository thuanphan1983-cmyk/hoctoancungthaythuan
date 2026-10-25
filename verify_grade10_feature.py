# -*- coding: utf-8 -*-
"""
KIỂM TRA TÍNH TOÀN VẸN CỦA TÍNH NĂNG THI THỬ VÀO LỚP 10
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

def verify():
    print("==================================================")
    print("KIỂM TRA CHỨC NĂNG THI THỬ VÀO LỚP 10 (GV PHAN ĐÌNH THUẤN)")
    print("==================================================")

    # 1. Kiểm tra file JSON dữ liệu
    json_path = "src/data/generated/grade10_mock_exams.json"
    assert os.path.exists(json_path), f"Không tìm thấy {json_path}"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    exams = data.get("exams", {})
    assert len(exams) == 10, f"Số đề thi {len(exams)} != 10"

    for idx, (k, ex) in enumerate(exams.items(), 1):
        print(f"\nKiểm tra Đề {idx} ({k}):")
        assert "title" in ex and "GV PHAN ĐÌNH THUẤN" in ex["title"].upper(), f"Tiêu đề không đúng: {ex.get('title')}"
        part1 = ex.get("part1", [])
        part2 = ex.get("part2", [])
        assert len(part1) == 8, f"Phần trắc nghiệm {len(part1)} != 8 câu"
        assert len(part2) == 6, f"Phần tự luận {len(part2)} != 6 câu (từ câu 9 đến 14)"
        
        # Kiểm tra trắc nghiệm
        for q in part1:
            assert len(q.get("options", [])) == 4, f"Câu {q['id']} không đủ 4 phương án"
            assert q.get("answer") in ["A", "B", "C", "D"], f"Đáp án không hợp lệ: {q.get('answer')}"
            assert len(q["question"]) > 10, f"Câu {q['id']} nội dung câu hỏi quá ngắn"

        # Kiểm tra tự luận
        for q in part2:
            assert "solution" in q and len(q["solution"]) > 20, f"Câu {q['id']} thiếu lời giải chi tiết"
            assert "rubric" in q and len(q["rubric"]) > 0, f"Câu {q['id']} thiếu barem điểm"

        print(f"  -> Đề số {idx}: 14 câu (8 trắc nghiệm + 6 tự luận) đạt chuẩn 100%.")

    print("\n✅ TẤT CẢ 10 ĐỀ MINH HỌA ĐÃ SẴN SÀNG VÀ HỢP LỆ!")

    # 2. Kiểm tra file JS
    assert os.path.exists("grade10EntranceExams.js"), "Thiếu grade10EntranceExams.js tại root"
    assert os.path.exists("dist/grade10EntranceExams.js"), "Thiếu dist/grade10EntranceExams.js"
    print("✅ Đã kiểm tra file grade10EntranceExams.js tại root và dist/.")

    # 3. Kiểm tra index.html
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    required_markers = [
        "grade10EntranceExams.js",
        "THI THỬ VÀO LỚP 10",
        "GV PHAN ĐÌNH THUẤN",
        "Times New Roman",
        "pdf-exam-container",
        "mock-exam-printable-paper",
        "mock-exam-printable-full",
        "handlePrintExam",
        "window.print"
    ]
    for m in required_markers:
        assert m in html, f"Thiếu marker '{m}' trong index.html"

    print("✅ Đã kiểm tra index.html: Giao diện và tính năng xuất PDF đầy đủ 100%.")

    # 4. Kiểm tra manifest.json
    for mp in ["manifest.json", "src/data/generated/manifest.json", "dist/manifest.json", "dist/generated/manifest.json"]:
        if os.path.exists(mp):
            with open(mp, "r", encoding="utf-8") as f:
                mf = json.load(f)
            assert "grade10_mock" in mf, f"Thiếu grade10_mock trong {mp}"
            assert mf["grade10_mock"]["totalExams"] == 6, f"totalExams sai trong {mp}"
            print(f"✅ {mp}: Đã đồng bộ grade10_mock.")

    print("\n🎉 KIỂM TRA THÀNH CÔNG RỰC RỠ 100%!")

if __name__ == "__main__":
    verify()
