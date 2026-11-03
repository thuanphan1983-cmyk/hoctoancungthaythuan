# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 11: PHÉP CỘNG, PHÉP TRỪ PHÂN SỐ - PHẦN 1 (BÀI 51 VÀ BÀI 52) - TOÁN 4 KNTT
Gồm 2 bài học, mỗi bài có 3 đề kiểm tra độc lập:
- Bài 51: Phép cộng phân số (th4_b51_test1, th4_b51_test2, th4_b51_test3)
- Bài 52: Phép trừ phân số (th4_b52_test1, th4_b52_test2, th4_b52_test3)
Tổng cộng: 6 đề kiểm tra chất lượng cao, độc lập 100%.
"""

def make_mc(qid, question, options, correct, explanation, level="Thông hiểu"):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "choices": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5,
        "level": level
    }

def make_essay(qid, question, solution, answer, lineCount=4, points=1.0, level="Thông hiểu"):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    sol = solution if "Đáp số" in solution else f"{solution}\nĐáp số: {answer}."
    return {
        "id": qid,
        "question": p_text,
        "solution": sol,
        "answer": answer,
        "lineCount": lineCount,
        "points": points,
        "level": level
    }

def get_ch11_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 51: PHÉP CỘNG PHÂN SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b51_test1"] = {
        "id": "th4_b51_test1",
        "lessonId": "th4_b51",
        "lessonNum": 51,
        "testNum": 1,
        "title": "Bài 51: Phép cộng phân số - Đề số 1",
        "topic": "Phép cộng phân số cùng mẫu số và khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, phép trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn cộng hai phân số có cùng mẫu số, ta làm như sau:", ["Cộng hai tử số với nhau và giữ nguyên mẫu số", "Cộng cả tử số và mẫu số", "Nhân hai tử số với nhau", "Quy đồng mẫu số"], 0, "Quy tắc cộng hai phân số cùng mẫu số: lấy tử số cộng tử số, giữ nguyên mẫu số.", "Nhận biết"),
            make_mc(2, "Kết quả của phép cộng 2/7 + 3/7 là:", ["5/7", "5/14", "6/7", "1/7"], 0, "2/7 + 3/7 = (2 + 3)/7 = 5/7.", "Nhận biết"),
            make_mc(3, "Kết quả của phép cộng 1/3 + 1/6 là:", ["1/2", "2/9", "2/6", "5/6"], 0, "1/3 = 2/6. Ta có: 2/6 + 1/6 = 3/6 = 1/2.", "Thông hiểu"),
            make_mc(4, "Tính: 3/5 + 2/15 =", ["11/15", "5/20", "1/3", "1/4"], 0, "3/5 = 9/15. Ta có: 9/15 + 2/15 = 11/15.", "Thông hiểu"),
            make_mc(5, "Kết quả của phép tính 1 + 2/3 là:", ["5/3", "3/3", "2/3", "4/3"], 0, "1 + 2/3 = 3/3 + 2/3 = 5/3.", "Thông hiểu"),
            make_mc(6, "Một tấm vải được cắt làm hai lần: lần thứ nhất cắt 2/9 tấm vải, lần thứ hai cắt 4/9 tấm vải. Cả hai lần đã cắt số phần tấm vải là:", ["6/9 (hay 2/3)", "6/18", "2/9", "8/9"], 0, "2/9 + 4/9 = 6/9 = 2/3.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính (rút gọn kết quả nếu có thể):\na) 4/11 + 5/11\nb) 7/15 + 8/15", "a) 4/11 + 5/11 = (4 + 5)/11 = 9/11\nb) 7/15 + 8/15 = 15/15 = 1\nĐáp số: a) 9/11; b) 1.", "a) 9/11; b) 1", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 1/4 + 3/8\nb) 2/5 + 3/10", "a) 1/4 = 2/8. Ta có: 2/8 + 3/8 = 5/8\nb) 2/5 = 4/10. Ta có: 4/10 + 3/10 = 7/10\nĐáp số: a) 5/8; b) 7/10.", "a) 5/8; b) 7/10", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính bằng cách quy đồng mẫu số:\na) 2/3 + 3/5\nb) 1/6 + 5/8", "a) MSC là 15: 2/3 = 10/15; 3/5 = 9/15. Ta có: 10/15 + 9/15 = 19/15\nb) MSC là 24: 1/6 = 4/24; 5/8 = 15/24. Ta có: 4/24 + 15/24 = 19/24\nĐáp số: a) 19/15; b) 19/24.", "a) 19/15; b) 19/24", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đội công nhân làm đường trong hai ngày. Ngày thứ nhất sửa được 3/10 quãng đường, ngày thứ hai sửa được 2/5 quãng đường. Hỏi cả hai ngày đội công nhân sửa được bao nhiêu phần của quãng đường?", "Cả hai ngày đội công nhân sửa được số phần quãng đường là:\n3/10 + 2/5 = 3/10 + 4/10 = 7/10 (quãng đường)\nĐáp số: 7/10 quãng đường.", "7/10 quãng đường", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một bể nước có hai vòi cùng chảy vào. Trong một giờ, vòi thứ nhất chảy được 1/3 bể nước, vòi thứ hai chảy được 2/7 bể nước. Hỏi trong một giờ cả hai vòi chảy được bao nhiêu phần của bể nước?", "Trong một giờ cả hai vòi chảy được số phần bể nước là:\n1/3 + 2/7 = 7/21 + 6/21 = 13/21 (bể nước)\nĐáp số: 13/21 bể nước.", "13/21 bể nước", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính giá trị của biểu thức bằng cách thuận tiện nhất:\nA = 2/9 + 3/5 + 7/9 + 2/5", "Nhóm các phân số có cùng mẫu số:\nA = (2/9 + 7/9) + (3/5 + 2/5)\nA = 9/9 + 5/5\nA = 1 + 1 = 2\nĐáp số: 2.", "2", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b51_test2"] = {
        "id": "th4_b51_test2",
        "lessonId": "th4_b51",
        "lessonNum": 51,
        "testNum": 2,
        "title": "Bài 51: Phép cộng phân số - Đề số 2",
        "topic": "Phép cộng phân số cùng mẫu số và khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, phép trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 3/8 + 1/8 là:", ["1/2", "4/16", "2/8", "4/8"], 0, "3/8 + 1/8 = 4/8 = 1/2.", "Nhận biết"),
            make_mc(2, "Muốn cộng hai phân số khác mẫu số, bước đầu tiên ta cần làm là:", ["Quy đồng mẫu số hai phân số", "Cộng hai tử số", "Cộng hai mẫu số", "Rút gọn phân số"], 0, "Bước đầu tiên là quy đồng mẫu số hai phân số đó.", "Nhận biết"),
            make_mc(3, "Tính: 2/5 + 1/4 =", ["13/20", "3/9", "3/20", "8/20"], 0, "MSC là 20: 8/20 + 5/20 = 13/20.", "Thông hiểu"),
            make_mc(4, "Kết quả của phép cộng 5/12 + 1/3 là:", ["3/4", "6/15", "7/12", "9/12"], 0, "1/3 = 4/12. Ta có: 5/12 + 4/12 = 9/12 = 3/4.", "Thông hiểu"),
            make_mc(5, "Tính: 3 + 1/4 =", ["13/4", "4/4", "7/4", "3/4"], 0, "3 = 12/4. Ta có: 12/4 + 1/4 = 13/4.", "Thông hiểu"),
            make_mc(6, "Buổi sáng Mai đọc được 1/5 quyển sách, buổi chiều Mai đọc được 2/5 quyển sách. Cả ngày Mai đọc được:", ["3/5 quyển sách", "3/10 quyển sách", "1/5 quyển sách", "4/5 quyển sách"], 0, "1/5 + 2/5 = 3/5.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính (rút gọn kết quả nếu có thể):\na) 5/14 + 3/14\nb) 9/20 + 11/20", "a) 5/14 + 3/14 = 8/14 = 4/7\nb) 9/20 + 11/20 = 20/20 = 1\nĐáp số: a) 4/7; b) 1.", "a) 4/7; b) 1", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 1/3 + 4/9\nb) 3/7 + 5/14", "a) 1/3 = 3/9. Ta có: 3/9 + 4/9 = 7/9\nb) 3/7 = 6/14. Ta có: 6/14 + 5/14 = 11/14\nĐáp số: a) 7/9; b) 11/14.", "a) 7/9; b) 11/14", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính bằng cách quy đồng mẫu số:\na) 3/4 + 2/5\nb) 4/9 + 1/6", "a) MSC là 20: 3/4 = 15/20; 2/5 = 8/20. Ta có: 15/20 + 8/20 = 23/20\nb) MSC là 18: 4/9 = 8/18; 1/6 = 3/18. Ta có: 8/18 + 3/18 = 11/18\nĐáp số: a) 23/20; b) 11/18.", "a) 23/20; b) 11/18", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một mảnh đất hình chữ nhật, người ta dùng 1/4 diện tích để trồng hoa, 3/8 diện tích để trồng rau. Hỏi diện tích trồng hoa và trồng rau chiếm tất cả bao nhiêu phần diện tích mảnh đất?", "Diện tích trồng hoa và rau chiếm số phần diện tích mảnh đất là:\n1/4 + 3/8 = 2/8 + 3/8 = 5/8 (diện tích)\nĐáp số: 5/8 diện tích mảnh đất.", "5/8 diện tích", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một ô tô chạy trong hai giờ. Giờ thứ nhất chạy được 2/9 quãng đường, giờ thứ hai chạy được 1/3 quãng đường. Hỏi sau hai giờ ô tô chạy được bao nhiêu phần quãng đường?", "Sau hai giờ ô tô chạy được số phần quãng đường là:\n2/9 + 1/3 = 2/9 + 3/9 = 5/9 (quãng đường)\nĐáp số: 5/9 quãng đường.", "5/9 quãng đường", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính bằng cách thuận tiện nhất:\nB = 1/6 + 3/8 + 5/6 + 5/8", "B = (1/6 + 5/6) + (3/8 + 5/8)\nB = 6/6 + 8/8\nB = 1 + 1 = 2\nĐáp số: 2.", "2", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b51_test3"] = {
        "id": "th4_b51_test3",
        "lessonId": "th4_b51",
        "lessonNum": 51,
        "testNum": 3,
        "title": "Bài 51: Phép cộng phân số - Đề số 3",
        "topic": "Phép cộng phân số cùng mẫu số và khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, phép trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 5/13 + 4/13 là:", ["9/13", "9/26", "1/13", "20/13"], 0, "5/13 + 4/13 = 9/13.", "Nhận biết"),
            make_mc(2, "Tính: 3/10 + 2/5 =", ["7/10", "5/15", "5/10", "1/2"], 0, "2/5 = 4/10. Ta có: 3/10 + 4/10 = 7/10.", "Thông hiểu"),
            make_mc(3, "Kết quả phép tính 1/2 + 1/3 sau khi cộng là:", ["5/6", "2/5", "1/6", "2/6"], 0, "3/6 + 2/6 = 5/6.", "Thông hiểu"),
            make_mc(4, "Tính: 4/7 + 5/21 =", ["17/21", "9/28", "9/21", "12/21"], 0, "4/7 = 12/21. Ta có: 12/21 + 5/21 = 17/21.", "Thông hiểu"),
            make_mc(5, "Kết quả của phép tính 2 + 5/7 là:", ["19/7", "7/7", "10/7", "17/7"], 0, "2 = 14/7. Ta có: 14/7 + 5/7 = 19/7.", "Thông hiểu"),
            make_mc(6, "Một bình nước có 3/8 lít nước, người ta đổ thêm vào 1/4 lít nước. Bình có tất cả số lít nước là:", ["5/8 lít", "4/12 lít", "1/2 lít", "7/8 lít"], 0, "3/8 + 1/4 = 3/8 + 2/8 = 5/8 (lít).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 6/17 + 8/17\nb) 7/18 + 5/18", "a) 6/17 + 8/17 = 14/17\nb) 7/18 + 5/18 = 12/18 = 2/3\nĐáp số: a) 14/17; b) 2/3.", "a) 14/17; b) 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 2/9 + 5/18\nb) 3/8 + 7/24", "a) 2/9 = 4/18. Ta có: 4/18 + 5/18 = 9/18 = 1/2\nb) 3/8 = 9/24. Ta có: 9/24 + 7/24 = 16/24 = 2/3\nĐáp số: a) 1/2; b) 2/3.", "a) 1/2; b) 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính bằng cách quy đồng mẫu số:\na) 3/7 + 2/3\nb) 4/5 + 1/6", "a) MSC là 21: 3/7 = 9/21; 2/3 = 14/21. Ta có: 9/21 + 14/21 = 23/21\nb) MSC là 30: 4/5 = 24/30; 1/6 = 5/30. Ta có: 24/30 + 5/30 = 29/30\nĐáp số: a) 23/21; b) 29/30.", "a) 23/21; b) 29/30", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một giá sách có hai ngăn. Ngăn thứ nhất chiếm 3/7 tổng số sách, ngăn thứ hai chiếm 2/5 tổng số sách. Hỏi cả hai ngăn chiếm bao nhiêu phần tổng số sách?", "Cả hai ngăn chiếm số phần tổng số sách là:\n3/7 + 2/5 = 15/35 + 14/35 = 29/35 (tổng số sách)\nĐáp số: 29/35 tổng số sách.", "29/35 tổng số sách", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một ngày bạn Hùng dành 1/4 ngày để học bài và 1/3 ngày để ngủ. Hỏi thời gian học bài và ngủ chiếm bao nhiêu phần của ngày?", "Thời gian học bài và ngủ chiếm số phần ngày là:\n1/4 + 1/3 = 3/12 + 4/12 = 7/12 (ngày)\nĐáp số: 7/12 ngày.", "7/12 ngày", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: C = 3/10 + 4/15 + 7/10 + 11/15", "C = (3/10 + 7/10) + (4/15 + 11/15)\nC = 10/10 + 15/15\nC = 1 + 1 = 2\nĐáp số: 2.", "2", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 52: PHÉP TRỪ PHÂN SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b52_test1"] = {
        "id": "th4_b52_test1",
        "lessonId": "th4_b52",
        "lessonNum": 52,
        "testNum": 1,
        "title": "Bài 52: Phép trừ phân số - Đề số 1",
        "topic": "Phép trừ phân số cùng mẫu số và khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, phép trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn trừ hai phân số cùng mẫu số, ta làm như sau:", ["Trừ tử số của phân số thứ nhất cho tử số của phân số thứ hai và giữ nguyên mẫu số", "Trừ cả tử số và mẫu số", "Lấy mẫu số trừ tử số", "Quy đồng mẫu số"], 0, "Quy tắc trừ hai phân số cùng mẫu số.", "Nhận biết"),
            make_mc(2, "Kết quả của phép trừ 7/9 - 4/9 là:", ["3/9 (hay 1/3)", "3/0", "11/9", "3/18"], 0, "7/9 - 4/9 = 3/9 = 1/3.", "Nhận biết"),
            make_mc(3, "Tính: 5/6 - 1/3 =", ["1/2", "4/3", "4/6", "2/3"], 0, "1/3 = 2/6. Ta có: 5/6 - 2/6 = 3/6 = 1/2.", "Thông hiểu"),
            make_mc(4, "Kết quả của phép tính 1 - 3/5 là:", ["2/5", "4/5", "3/5", "1/5"], 0, "1 = 5/5. Ta có: 5/5 - 3/5 = 2/5.", "Thông hiểu"),
            make_mc(5, "Tính: 3/4 - 2/5 =", ["7/20", "1/20", "1/1", "1/9"], 0, "MSC là 20: 15/20 - 8/20 = 7/20.", "Thông hiểu"),
            make_mc(6, "Một tấm vải dài 8/9 m, người ta cắt đi 5/9 m. Tấm vải còn lại dài là:", ["3/9 m (hay 1/3 m)", "13/9 m", "3/0 m", "2/9 m"], 0, "8/9 - 5/9 = 3/9 = 1/3 (m).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính (rút gọn kết quả nếu có thể):\na) 11/15 - 4/15\nb) 19/24 - 7/24", "a) 11/15 - 4/15 = 7/15\nb) 19/24 - 7/24 = 12/24 = 1/2\nĐáp số: a) 7/15; b) 1/2.", "a) 7/15; b) 1/2", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 7/8 - 1/4\nb) 5/6 - 5/18", "a) 1/4 = 2/8. Ta có: 7/8 - 2/8 = 5/8\nb) 5/6 = 15/18. Ta có: 15/18 - 5/18 = 10/18 = 5/9\nĐáp số: a) 5/8; b) 5/9.", "a) 5/8; b) 5/9", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x + 2/5 = 7/10\nb) x - 1/3 = 5/12", "a) x = 7/10 - 2/5 = 7/10 - 4/10 = 3/10\nb) x = 5/12 + 1/3 = 5/12 + 4/12 = 9/12 = 3/4\nĐáp số: a) x = 3/10; b) x = 3/4.", "a) x = 3/10; b) x = 3/4", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một bể nước đang có 7/8 lượng nước. Người ta đã dùng hết 3/4 lượng nước đó. Hỏi trong bể còn lại bao nhiêu phần lượng nước?", "Lượng nước còn lại trong bể là:\n7/8 - 3/4 = 7/8 - 6/8 = 1/8 (bể nước)\nĐáp số: 1/8 lượng nước.", "1/8 bể nước", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một cuộn dây dài 2 m. Người ta cắt ra một đoạn dài 3/5 m. Hỏi cuộn dây còn lại bao nhiêu mét?", "Cuộn dây còn lại số mét là:\n2 - 3/5 = 10/5 - 3/5 = 7/5 (m)\nĐáp số: 7/5 m.", "7/5 m", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính giá trị biểu thức bằng cách hợp lý:\nA = 17/12 - (5/12 + 1/3)", "A = 17/12 - 5/12 - 1/3\nA = (17/12 - 5/12) - 1/3\nA = 12/12 - 1/3 = 1 - 1/3 = 2/3\nĐáp số: 2/3.", "2/3", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b52_test2"] = {
        "id": "th4_b52_test2",
        "lessonId": "th4_b52",
        "lessonNum": 52,
        "testNum": 2,
        "title": "Bài 52: Phép trừ phân số - Đề số 2",
        "topic": "Phép trừ phân số cùng mẫu số và khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, phép trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép trừ 8/11 - 3/11 là:", ["5/11", "5/22", "5/0", "11/11"], 0, "8/11 - 3/11 = 5/11.", "Nhận biết"),
            make_mc(2, "Tính: 3/4 - 1/2 =", ["1/4", "2/2", "2/4", "1/2"], 0, "3/4 - 2/4 = 1/4.", "Thông hiểu"),
            make_mc(3, "Kết quả của 7/10 - 2/5 là:", ["3/10", "5/5", "5/10", "1/2"], 0, "7/10 - 4/10 = 3/10.", "Thông hiểu"),
            make_mc(4, "Tính: 2 - 4/7 =", ["10/7", "2/7", "8/7", "6/7"], 0, "2 = 14/7. Ta có: 14/7 - 4/7 = 10/7.", "Thông hiểu"),
            make_mc(5, "Kết quả của phép trừ 4/5 - 2/3 là:", ["2/15", "2/2", "2/8", "6/15"], 0, "MSC là 15: 12/15 - 10/15 = 2/15.", "Thông hiểu"),
            make_mc(6, "Một can dầu chứa 9/10 lít dầu, rót ra 3/10 lít. Can còn lại số lít dầu là:", ["6/10 lít (hay 3/5 lít)", "12/10 lít", "3/10 lít", "6/20 lít"], 0, "9/10 - 3/10 = 6/10 = 3/5 (lít).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính (rút gọn kết quả nếu có thể):\na) 13/16 - 5/16\nb) 25/36 - 13/36", "a) 13/16 - 5/16 = 8/16 = 1/2\nb) 25/36 - 13/36 = 12/36 = 1/3\nĐáp số: a) 1/2; b) 1/3.", "a) 1/2; b) 1/3", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 5/6 - 7/18\nb) 8/15 - 1/5", "a) 5/6 = 15/18. Ta có: 15/18 - 7/18 = 8/18 = 4/9\nb) 1/5 = 3/15. Ta có: 8/15 - 3/15 = 5/15 = 1/3\nĐáp số: a) 4/9; b) 1/3.", "a) 4/9; b) 1/3", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x + 3/8 = 5/6\nb) 7/9 - x = 1/3", "a) x = 5/6 - 3/8 = 20/24 - 9/24 = 11/24\nb) x = 7/9 - 1/3 = 7/9 - 3/9 = 4/9\nĐáp số: a) x = 11/24; b) x = 4/9.", "a) x = 11/24; b) x = 4/9", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại có diện tích trồng trọt gồm trồng lúa và trồng ngô. Trong đó diện tích trồng lúa chiếm 5/7 diện tích trang trại. Hỏi diện tích trồng ngô chiếm bao nhiêu phần diện tích trang trại?", "Coi toàn bộ diện tích trang trại là 1 đơn vị.\nDiện tích trồng ngô chiếm số phần diện tích trang trại là:\n1 - 5/7 = 2/7 (diện tích trang trại)\nĐáp số: 2/7 diện tích trang trại.", "2/7 diện tích", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một cửa hàng có 3 tấn gạo. Buổi sáng cửa hàng bán được 4/5 tấn gạo. Hỏi cửa hàng còn lại bao nhiêu tấn gạo?", "Cửa hàng còn lại số tấn gạo là:\n3 - 4/5 = 15/5 - 4/5 = 11/5 (tấn gạo)\nĐáp số: 11/5 tấn gạo.", "11/5 tấn", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nB = 15/14 - 3/7 - 2/14", "B = (15/14 - 2/14) - 3/7\nB = 13/14 - 6/14 = 7/14 = 1/2\nĐáp số: 1/2.", "1/2", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b52_test3"] = {
        "id": "th4_b52_test3",
        "lessonId": "th4_b52",
        "lessonNum": 52,
        "testNum": 3,
        "title": "Bài 52: Phép trừ phân số - Đề số 3",
        "topic": "Phép trừ phân số cùng mẫu số và khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, phép trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 9/14 - 5/14 là:", ["4/14 (hay 2/7)", "4/0", "14/14", "4/28"], 0, "9/14 - 5/14 = 4/14 = 2/7.", "Nhận biết"),
            make_mc(2, "Tính: 4/5 - 1/10 =", ["7/10", "3/5", "3/10", "3/0"], 0, "4/5 = 8/10. Ta có: 8/10 - 1/10 = 7/10.", "Thông hiểu"),
            make_mc(3, "Kết quả của 5/7 - 1/2 là:", ["3/14", "4/5", "4/14", "6/14"], 0, "MSC là 14: 10/14 - 7/14 = 3/14.", "Thông hiểu"),
            make_mc(4, "Tính: 1 - 5/8 =", ["3/8", "5/8", "4/8", "13/8"], 0, "1 = 8/8. Ta có: 8/8 - 5/8 = 3/8.", "Thông hiểu"),
            make_mc(5, "Kết quả phép tính 5/9 - 1/6 là:", ["7/18", "4/3", "4/15", "4/18"], 0, "MSC là 18: 10/18 - 3/18 = 7/18.", "Thông hiểu"),
            make_mc(6, "Một người thợ sơn được 7/12 bức tường trong buổi sáng, buổi chiều sơn thêm để hoàn thành bức tường. Buổi chiều người đó sơn được:", ["5/12 bức tường", "7/12 bức tường", "1/12 bức tường", "6/12 bức tường"], 0, "1 - 7/12 = 5/12.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính (rút gọn kết quả nếu có thể):\na) 17/20 - 7/20\nb) 23/28 - 9/28", "a) 17/20 - 7/20 = 10/20 = 1/2\nb) 23/28 - 9/28 = 14/28 = 1/2\nĐáp số: a) 1/2; b) 1/2.", "a) 1/2; b) 1/2", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 7/9 - 5/18\nb) 9/14 - 2/7", "a) 7/9 = 14/18. Ta có: 14/18 - 5/18 = 9/18 = 1/2\nb) 2/7 = 4/14. Ta có: 9/14 - 4/14 = 5/14\nĐáp số: a) 1/2; b) 5/14.", "a) 1/2; b) 5/14", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x + 1/4 = 5/8\nb) 8/15 - x = 1/5", "a) x = 5/8 - 1/4 = 5/8 - 2/8 = 3/8\nb) x = 8/15 - 1/5 = 8/15 - 3/15 = 5/15 = 1/3\nĐáp số: a) x = 3/8; b) x = 1/3.", "a) x = 3/8; b) x = 1/3", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một bình chứa 3/4 lít dầu hỏa. Mẹ dùng hết 1/2 lít dầu để thắp đèn. Hỏi trong bình còn lại bao nhiêu lít dầu?", "Trong bình còn lại số lít dầu là:\n3/4 - 1/2 = 3/4 - 2/4 = 1/4 (lít dầu)\nĐáp số: 1/4 lít dầu.", "1/4 lít", 4, 1.5, "Vận dụng"),
            make_essay(5, "Đoạn đường từ nhà Nam đến trường dài 4/5 km. Nam đã đi được 1/2 km. Hỏi Nam còn phải đi bao nhiêu ki-lô-mét nữa thì đến trường?", "Nam còn phải đi số ki-lô-mét nữa là:\n4/5 - 1/2 = 8/10 - 5/10 = 3/10 (km)\nĐáp số: 3/10 km.", "3/10 km", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính bằng cách thuận tiện nhất:\nC = 19/15 - (4/15 + 1/5)", "C = 19/15 - 4/15 - 1/5\nC = (19/15 - 4/15) - 1/5\nC = 15/15 - 1/5 = 1 - 1/5 = 4/5\nĐáp số: 4/5.", "4/5", 4, 1.0, "Vận dụng cao")
        ]
    }

    return exams
