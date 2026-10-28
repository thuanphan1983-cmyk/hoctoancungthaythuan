# -*- coding: utf-8 -*-
"""
VALIDATOR KIỂM SOÁT MA TRẬN ĐỀ THI ĐỊNH KỲ (GIỮA KỲ 2 & CUỐI KỲ 2)
Tuân thủ tuyệt đối quy định ma trận:
1. Tổng thể: 30% Nhận biết (3.0đ), 30% Thông hiểu (3.0đ), 20% Vận dụng (2.0đ), 20% Vận dụng cao (2.0đ). Tổng: 10.0đ.
2. Cấu trúc vi mô:
   - Phần II (Đúng/Sai - 2 câu): Trong mỗi câu hỏi lớn (4 ý a,b,c,d), BẮT BUỘC có đúng 1 ý Vận dụng.
   - Phần III (Trả lời ngắn - 4 câu): BẮT BUỘC có đúng 1 câu Vận dụng, 1 câu Vận dụng cao, 2 câu cơ bản (Nhận biết / Thông hiểu).
   - Phần IV (Tự luận - 4 câu):
     + 2 câu đầu ở mức cơ bản / vừa phải: Câu 1 (1.0đ NB/TH), Câu 2 (1.0đ TH).
     + 1 ý 'khó vừa' (0.5đ) ở mức Vận dụng (Câu 3).
     + 1 ý 'rất khó' (0.5đ) ở mức Vận dụng cao chốt điểm 10 (Câu 4).
3. Không lặp lại, đa dạng hóa bài toán và ngữ cảnh thực tế.
"""

import sys

def norm_lvl(lvl):
    l = str(lvl or "").strip().lower()
    if "cao" in l or "vdc" in l:
        return "vdc"
    if "vận dụng" in l or "van dung" in l or "vd" in l:
        return "vd"
    if "thông hiểu" in l or "thong hieu" in l or "th" in l:
        return "th"
    if "nhận biết" in l or "nhan biet" in l or "nb" in l:
        return "nb"
    return "unknown"

def validate_periodic_exam(exam, expected_grade, expected_term, expected_test_num):
    ex_id = exam.get("id", "unknown_id")
    assert exam.get("grade") == str(expected_grade), f"[{ex_id}] Sai grade: {exam.get('grade')} != {expected_grade}"
    assert exam.get("term") == str(expected_term), f"[{ex_id}] Sai term: {exam.get('term')} != {expected_term}"
    assert str(exam.get("testNum")).zfill(2) == str(expected_test_num).zfill(2) or exam.get("testNum") == expected_test_num, f"[{ex_id}] Sai testNum: {exam.get('testNum')} != {expected_test_num}"
    
    # 1. Phần I: 12 câu trắc nghiệm khách quan
    part1 = exam.get("part1", [])
    assert len(part1) == 12, f"[{ex_id}] Phần I phải có đúng 12 câu, hiện có {len(part1)}"
    for idx, q in enumerate(part1, 1):
        assert len(q.get("options", [])) == 4, f"[{ex_id}] Phần I Câu {idx} không đủ 4 phương án"
        assert q.get("correct") in [0, 1, 2, 3], f"[{ex_id}] Phần I Câu {idx} có đáp án đúng không hợp lệ: {q.get('correct')}"
        assert len(q.get("question", "")) > 10, f"[{ex_id}] Phần I Câu {idx} nội dung quá ngắn"

    # 2. Phần II: 2 câu Đúng/Sai, mỗi câu 4 ý, ĐÚNG 1 ý Vận dụng
    part2 = exam.get("part2", [])
    assert len(part2) == 2, f"[{ex_id}] Phần II phải có đúng 2 câu lớn, hiện có {len(part2)}"
    for idx, q in enumerate(part2, 1):
        stmts = q.get("statements", [])
        assert len(stmts) == 4, f"[{ex_id}] Phần II Câu {idx} phải có 4 ý a,b,c,d, hiện có {len(stmts)}"
        vd_count = sum(1 for s in stmts if norm_lvl(s.get("level")) == "vd")
        assert vd_count == 1, f"[{ex_id}] Phần II Câu {idx} BẮT BUỘC có ĐÚNG 1 ý Vận dụng, hiện có {vd_count}"

    # 3. Phần III: 4 câu Trả lời ngắn, đúng 1 VD, 1 VDC, 2 cơ bản
    part3 = exam.get("part3", [])
    assert len(part3) == 4, f"[{ex_id}] Phần III phải có đúng 4 câu, hiện có {len(part3)}"
    p3_lvls = [norm_lvl(q.get("level")) for q in part3]
    vd_p3 = p3_lvls.count("vd")
    vdc_p3 = p3_lvls.count("vdc")
    basic_p3 = p3_lvls.count("nb") + p3_lvls.count("th")
    assert vd_p3 == 1, f"[{ex_id}] Phần III BẮT BUỘC đúng 1 câu Vận dụng (khó vừa), hiện có {vd_p3}"
    assert vdc_p3 == 1, f"[{ex_id}] Phần III BẮT BUỘC đúng 1 câu Vận dụng cao (khó), hiện có {vdc_p3}"
    assert basic_p3 == 2, f"[{ex_id}] Phần III BẮT BUỘC đúng 2 câu cơ bản (NB/TH), hiện có {basic_p3}"

    # 4. Phần IV: 4 câu Tự luận: 2 câu đầu (1.0đ), 1 ý khó vừa (0.5đ VD), 1 ý rất khó chốt 10 (0.5đ VDC)
    part4 = exam.get("part4", [])
    assert len(part4) == 4, f"[{ex_id}] Phần IV phải có đúng 4 câu, hiện có {len(part4)}"
    q1, q2, q3, q4 = part4[0], part4[1], part4[2], part4[3]
    assert q1.get("points") == 1.0, f"[{ex_id}] Phần IV Câu 1 phải 1.0 điểm, hiện có {q1.get('points')}"
    assert q2.get("points") == 1.0, f"[{ex_id}] Phần IV Câu 2 phải 1.0 điểm, hiện có {q2.get('points')}"
    assert q3.get("points") == 0.5, f"[{ex_id}] Phần IV Câu 3 phải 0.5 điểm, hiện có {q3.get('points')}"
    assert q4.get("points") == 0.5, f"[{ex_id}] Phần IV Câu 4 phải 0.5 điểm, hiện có {q4.get('points')}"
    assert norm_lvl(q3.get("level")) == "vd", f"[{ex_id}] Phần IV Câu 3 BẮT BUỘC là Vận dụng (khó vừa), hiện là {q3.get('level')}"
    assert norm_lvl(q4.get("level")) == "vdc", f"[{ex_id}] Phần IV Câu 4 BẮT BUỘC là Vận dụng cao (chốt 10 điểm), hiện là {q4.get('level')}"

    # 5. Kiểm tra tổng thể ma trận điểm (30% NB, 30% TH, 20% VD, 20% VDC = 10.0đ)
    points = {"nb": 0.0, "th": 0.0, "vd": 0.0, "vdc": 0.0}
    # Part 1 (0.25đ / câu)
    for q in part1:
        points[norm_lvl(q.get("level"))] += 0.25
    # Part 2 (0.25đ / ý)
    for q in part2:
        for s in q.get("statements", []):
            points[norm_lvl(s.get("level"))] += 0.25
    # Part 3 (0.5đ / câu)
    for q in part3:
        points[norm_lvl(q.get("level"))] += 0.50
    # Part 4
    for q in part4:
        pts = float(q.get("points", 0))
        points[norm_lvl(q.get("level"))] += pts

    total = sum(points.values())
    assert abs(total - 10.0) < 1e-5, f"[{ex_id}] Tổng điểm không bằng 10.0 (hiện là {total})"
    assert abs(points["nb"] - 3.0) < 1e-5, f"[{ex_id}] Điểm Nhận biết phải đúng 3.0đ (30%), hiện là {points['nb']}"
    assert abs(points["th"] - 3.0) < 1e-5, f"[{ex_id}] Điểm Thông hiểu phải đúng 3.0đ (30%), hiện là {points['th']}"
    assert abs(points["vd"] - 2.0) < 1e-5, f"[{ex_id}] Điểm Vận dụng phải đúng 2.0đ (20%), hiện là {points['vd']}"
    assert abs(points["vdc"] - 2.0) < 1e-5, f"[{ex_id}] Điểm Vận dụng cao phải đúng 2.0đ (20%), hiện là {points['vdc']}"

    return True
