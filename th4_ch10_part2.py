# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 10: PHÂN SỐ - PHẦN 2 (BÀI 48 ĐẾN BÀI 50) - TOÁN 4 KNTT
Gồm 3 bài học, mỗi bài có 3 đề kiểm tra độc lập:
- Bài 48: Quy đồng mẫu số các phân số (th4_b48_test1, th4_b48_test2, th4_b48_test3)
- Bài 49: So sánh hai phân số (th4_b49_test1, th4_b49_test2, th4_b49_test3)
- Bài 50: Luyện tập chung Chủ đề 10 (th4_b50_test1, th4_b50_test2, th4_b50_test3)
Tổng cộng: 9 đề kiểm tra chất lượng cao, độc lập 100%.
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

def get_ch10_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 48: QUY ĐỒNG MẪU SỐ CÁC PHÂN SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b48_test1"] = {
        "id": "th4_b48_test1",
        "lessonId": "th4_b48",
        "lessonNum": 48,
        "testNum": 1,
        "title": "Bài 48: Quy đồng mẫu số các phân số - Đề số 1",
        "topic": "Quy đồng mẫu số các phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Quy đồng mẫu số hai phân số 1/3 và 2/5 với mẫu số chung 15 ta được:", ["5/15 và 6/15", "3/15 và 6/15", "5/15 và 2/15", "1/15 và 2/15"], 0, "1/3 = 5/15 và 2/5 = 6/15.", "Thông hiểu"),
            make_mc(2, "Mẫu số chung nhỏ nhất của hai phân số 3/4 và 5/8 là:", ["8", "16", "32", "12"], 0, "Vì 8 chia hết cho 4 nên mẫu số chung là 8.", "Nhận biết"),
            make_mc(3, "Quy đồng mẫu số hai phân số 5/6 và 7/18 ta được:", ["15/18 và 7/18", "10/18 và 7/18", "5/18 và 7/18", "30/18 và 7/18"], 0, "5/6 = (5 x 3)/(6 x 3) = 15/18 và giữ nguyên 7/18.", "Thông hiểu"),
            make_mc(4, "Muốn quy đồng mẫu số hai phân số khi mẫu số của phân số này chia hết cho mẫu số của phân số kia, ta lấy:", ["Mẫu số lớn hơn làm mẫu số chung", "Tích hai mẫu số", "Mẫu số bé hơn", "Tổng hai mẫu số"], 0, "Lấy mẫu số lớn làm mẫu số chung.", "Nhận biết"),
            make_mc(5, "Khi quy đồng mẫu số hai phân số 3/5 và 4/7 với mẫu số chung là 35, phân số 3/5 trở thành:", ["21/35", "15/35", "20/35", "12/35"], 0, "3/5 = (3 x 7)/(5 x 7) = 21/35.", "Thông hiểu"),
            make_mc(6, "Quy đồng mẫu số ba phân số 1/2, 1/3, 1/4 với mẫu số chung nhỏ nhất là:", ["12", "24", "8", "6"], 0, "12 chia hết cho cả 2, 3 và 4.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Quy đồng mẫu số hai phân số:\na) 2/3 và 4/5\nb) 3/7 và 5/8", "a) Mẫu số chung là 15:\n2/3 = (2 x 5)/(3 x 5) = 10/15\n4/5 = (4 x 3)/(5 x 3) = 12/15\nb) Mẫu số chung là 56:\n3/7 = (3 x 8)/(7 x 8) = 24/56\n5/8 = (5 x 7)/(8 x 7) = 35/56\nĐáp số: a) 10/15 và 12/15; b) 24/56 và 35/56.", "a) 10/15 và 12/15; b) 24/56 và 35/56", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Quy đồng mẫu số các phân số (chọn mẫu số chung thuận tiện nhất):\na) 5/6 và 7/12\nb) 3/8 và 9/24", "a) Chọn mẫu số chung là 12:\n5/6 = (5 x 2)/(6 x 2) = 10/12; giữ nguyên 7/12.\nb) Chọn mẫu số chung là 24:\n3/8 = (3 x 3)/(8 x 3) = 9/24; giữ nguyên 9/24.\nĐáp số: a) 10/12 và 7/12; b) 9/24 và 9/24.", "a) 10/12 và 7/12; b) 9/24 và 9/24", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Rút gọn rồi quy đồng mẫu số hai phân số:\na) 15/20 và 8/12\nb) 14/21 và 9/15", "a) Rút gọn: 15/20 = 3/4; 8/12 = 2/3.\nQuy đồng với mẫu số chung 12:\n3/4 = 9/12; 2/3 = 8/12.\nb) Rút gọn: 14/21 = 2/3; 9/15 = 3/5.\nQuy đồng với mẫu số chung 15:\n2/3 = 10/15; 3/5 = 9/15.\nĐáp số: a) 9/12 và 8/12; b) 10/15 và 9/15.", "a) 9/12 và 8/12; b) 10/15 và 9/15", 5, 1.0, "Thông hiểu"),
            make_essay(4, "Hai bạn An và Bình có hai thanh sô-cô-la bằng nhau. An đã ăn 3/4 thanh sô-cô-la của mình, Bình đã ăn 5/6 thanh sô-cô-la của mình. Hãy quy đồng mẫu số hai phân số chỉ phần sô-cô-la hai bạn đã ăn.", "Mẫu số chung của 4 và 6 là 12.\nTa có:\n3/4 = (3 x 3)/(4 x 3) = 9/12\n5/6 = (5 x 2)/(6 x 2) = 10/12\nĐáp số: 9/12 và 10/12.", "9/12 và 10/12", 4, 1.5, "Vận dụng"),
            make_essay(5, "Quy đồng mẫu số ba phân số sau: 2/3 ; 3/4 và 5/6.", "Mẫu số chung của 3, 4, 6 là 12.\n2/3 = (2 x 4)/(3 x 4) = 8/12\n3/4 = (3 x 3)/(4 x 3) = 9/12\n5/6 = (5 x 2)/(6 x 2) = 10/12\nĐáp số: 8/12 ; 9/12 ; 10/12.", "8/12, 9/12, 10/12", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm hai phân số có cùng mẫu số là 20 sao cho một phân số bằng 3/4 và phân số kia bằng 4/5.", "Ta có:\n3/4 = (3 x 5)/(4 x 5) = 15/20\n4/5 = (4 x 4)/(5 x 4) = 16/20\nVậy hai phân số cần tìm là 15/20 và 16/20.\nĐáp số: 15/20 và 16/20.", "15/20 và 16/20", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b48_test2"] = {
        "id": "th4_b48_test2",
        "lessonId": "th4_b48",
        "lessonNum": 48,
        "testNum": 2,
        "title": "Bài 48: Quy đồng mẫu số các phân số - Đề số 2",
        "topic": "Quy đồng mẫu số các phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Quy đồng mẫu số hai phân số 2/5 và 3/7 với mẫu số chung 35 ta được:", ["14/35 và 15/35", "10/35 và 15/35", "14/35 và 21/35", "2/35 và 3/35"], 0, "2/5 = 14/35 và 3/7 = 15/35.", "Thông hiểu"),
            make_mc(2, "Mẫu số chung của 5/9 và 4/27 là:", ["27", "9", "54", "18"], 0, "Vì 27 chia hết cho 9 nên mẫu số chung là 27.", "Nhận biết"),
            make_mc(3, "Quy đồng mẫu số hai phân số 3/8 và 7/16 ta được:", ["6/16 và 7/16", "3/16 và 7/16", "9/16 và 7/16", "6/16 và 14/16"], 0, "3/8 = 6/16; giữ nguyên 7/16.", "Thông hiểu"),
            make_mc(4, "Khi quy đồng mẫu số hai phân số 1/4 và 5/6, mẫu số chung nhỏ nhất là:", ["12", "24", "18", "16"], 0, "12 chia hết cho cả 4 và 6.", "Thông hiểu"),
            make_mc(5, "Phân số 2/3 quy đồng với mẫu số 18 trở thành:", ["12/18", "6/18", "9/18", "8/18"], 0, "2/3 = (2 x 6)/(3 x 6) = 12/18.", "Thông hiểu"),
            make_mc(6, "Quy đồng mẫu số hai phân số 7/10 và 4/15 với mẫu số chung nhỏ nhất là:", ["21/30 và 8/30", "14/30 và 8/30", "21/30 và 12/30", "7/30 và 4/30"], 0, "MSC là 30: 7/10 = 21/30 và 4/15 = 8/30.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Quy đồng mẫu số hai phân số:\na) 3/4 và 2/7\nb) 4/9 và 5/6", "a) Mẫu số chung là 28:\n3/4 = 21/28; 2/7 = 8/28.\nb) Mẫu số chung là 18:\n4/9 = 8/18; 5/6 = 15/18.\nĐáp số: a) 21/28 và 8/28; b) 8/18 và 15/18.", "a) 21/28 và 8/28; b) 8/18 và 15/18", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Quy đồng mẫu số các phân số (mẫu số này chia hết cho mẫu số kia):\na) 3/5 và 11/20\nb) 5/8 và 17/32", "a) Chọn mẫu số chung là 20:\n3/5 = 12/20; giữ nguyên 11/20.\nb) Chọn mẫu số chung là 32:\n5/8 = 20/32; giữ nguyên 17/32.\nĐáp số: a) 12/20 và 11/20; b) 20/32 và 17/32.", "a) 12/20 và 11/20; b) 20/32 và 17/32", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Rút gọn rồi quy đồng mẫu số hai phân số:\na) 18/24 và 10/15\nb) 12/16 và 14/21", "a) 18/24 = 3/4; 10/15 = 2/3.\nMSC là 12: 3/4 = 9/12; 2/3 = 8/12.\nb) 12/16 = 3/4; 14/21 = 2/3.\nMSC là 12: 3/4 = 9/12; 2/3 = 8/12.\nĐáp số: a) 9/12 và 8/12; b) 9/12 và 8/12.", "a) 9/12 và 8/12; b) 9/12 và 8/12", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Lớp 4A có 2/5 số học sinh thích học môn Mỹ thuật và 1/2 số học sinh thích học môn Âm nhạc. Hãy quy đồng mẫu số hai phân số chỉ số phần học sinh thích hai môn học trên.", "Mẫu số chung của 5 và 2 là 10.\nTa có:\n2/5 = (2 x 2)/(5 x 2) = 4/10\n1/2 = (1 x 5)/(2 x 5) = 5/10\nĐáp số: 4/10 và 5/10.", "4/10 và 5/10", 4, 1.5, "Vận dụng"),
            make_essay(5, "Quy đồng mẫu số ba phân số sau: 1/2 ; 2/3 và 3/5.", "Mẫu số chung của 2, 3, 5 là 30.\n1/2 = (1 x 15)/(2 x 15) = 15/30\n2/3 = (2 x 10)/(3 x 10) = 20/30\n3/5 = (3 x 6)/(5 x 6) = 18/30\nĐáp số: 15/30 ; 20/30 ; 18/30.", "15/30, 20/30, 18/30", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm phân số có mẫu số là 24 bằng phân số 5/8 và phân số có mẫu số là 24 bằng phân số 7/12.", "Ta có:\n5/8 = (5 x 3)/(8 x 3) = 15/24\n7/12 = (7 x 2)/(12 x 2) = 14/24\nĐáp số: 15/24 và 14/24.", "15/24 và 14/24", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b48_test3"] = {
        "id": "th4_b48_test3",
        "lessonId": "th4_b48",
        "lessonNum": 48,
        "testNum": 3,
        "title": "Bài 48: Quy đồng mẫu số các phân số - Đề số 3",
        "topic": "Quy đồng mẫu số các phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Quy đồng mẫu số hai phân số 3/7 và 4/9 với mẫu số chung 63 ta được:", ["27/63 và 28/63", "21/63 và 28/63", "27/63 và 36/63", "12/63 và 28/63"], 0, "3/7 = 27/63 và 4/9 = 28/63.", "Thông hiểu"),
            make_mc(2, "Mẫu số chung thuận tiện nhất của 7/15 và 3/5 là:", ["15", "75", "30", "45"], 0, "15 chia hết cho 5 nên MSC là 15.", "Nhận biết"),
            make_mc(3, "Quy đồng mẫu số hai phân số 5/12 và 3/4 được hai phân số:", ["5/12 và 9/12", "5/12 và 6/12", "10/12 và 9/12", "5/12 và 3/12"], 0, "Giữ nguyên 5/12; 3/4 = 9/12.", "Thông hiểu"),
            make_mc(4, "Quy đồng mẫu số hai phân số 5/8 và 7/10 với mẫu số chung nhỏ nhất là 40 ta được:", ["25/40 và 28/40", "20/40 và 28/40", "25/40 và 35/40", "5/40 và 7/40"], 0, "5/8 = 25/40 và 7/10 = 28/40.", "Thông hiểu"),
            make_mc(5, "Khi quy đồng mẫu số của 2/9 và 5/18 ta chọn mẫu số chung là:", ["18", "9", "27", "81"], 0, "18 chia hết cho 9.", "Nhận biết"),
            make_mc(6, "Quy đồng mẫu số hai phân số 1/6 và 3/8 với mẫu số chung 24 ta được:", ["4/24 và 9/24", "4/24 và 6/24", "6/24 và 9/24", "1/24 và 3/24"], 0, "1/6 = 4/24 và 3/8 = 9/24.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Quy đồng mẫu số hai phân số:\na) 4/5 và 3/8\nb) 2/9 và 5/7", "a) MSC là 40: 4/5 = 32/40; 3/8 = 15/40.\nb) MSC là 63: 2/9 = 14/63; 5/7 = 45/63.\nĐáp số: a) 32/40 và 15/40; b) 14/63 và 45/63.", "a) 32/40 và 15/40; b) 14/63 và 45/63", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Quy đồng mẫu số các phân số sau:\na) 7/10 và 13/30\nb) 5/12 và 19/36", "a) MSC là 30: 7/10 = 21/30; giữ nguyên 13/30.\nb) MSC là 36: 5/12 = 15/36; giữ nguyên 19/36.\nĐáp số: a) 21/30 và 13/30; b) 15/36 và 19/36.", "a) 21/30 và 13/30; b) 15/36 và 19/36", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Rút gọn rồi quy đồng mẫu số hai phân số:\na) 16/20 và 18/30\nb) 15/35 và 24/42", "a) Rút gọn: 16/20 = 4/5; 18/30 = 3/5. Cùng mẫu số 5 không cần quy đồng nữa: 4/5 và 3/5.\nb) 15/35 = 3/7; 24/42 = 4/7. Cùng mẫu số 7: 3/7 và 4/7.\nĐáp số: a) 4/5 và 3/5; b) 3/7 và 4/7.", "a) 4/5 và 3/5; b) 3/7 và 4/7", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một ngày có 24 giờ. Bạn Mai ngủ 1/3 ngày và học 1/4 ngày. Hãy quy đồng mẫu số hai phân số chỉ thời gian ngủ và học của bạn Mai.", "Mẫu số chung của 3 và 4 là 12.\nTa có:\n1/3 = (1 x 4)/(3 x 4) = 4/12\n1/4 = (1 x 3)/(4 x 3) = 3/12\nĐáp số: 4/12 và 3/12.", "4/12 và 3/12", 4, 1.5, "Vận dụng"),
            make_essay(5, "Quy đồng mẫu số ba phân số: 3/4 ; 5/6 và 7/12.", "Mẫu số chung của 4, 6, 12 là 12.\n3/4 = 9/12\n5/6 = 10/12\nGiữ nguyên 7/12.\nĐáp số: 9/12 ; 10/12 ; 7/12.", "9/12, 10/12, 7/12", 5, 1.5, "Vận dụng"),
            make_essay(6, "Quy đồng mẫu số hai phân số a/5 và 3/7 sao cho cả hai phân số đều có mẫu số là 35 và tổng hai tử số sau khi quy đồng bằng 36. Tìm số tự nhiên a.", "Quy đồng mẫu số:\na/5 = (a x 7)/35\n3/7 = 15/35\nTheo đề bài ta có: a x 7 + 15 = 36\na x 7 = 36 - 15 = 21\na = 21 : 7 = 3\nĐáp số: a = 3.", "a = 3", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 49: SO SÁNH HAI PHÂN SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b49_test1"] = {
        "id": "th4_b49_test1",
        "lessonId": "th4_b49",
        "lessonNum": 49,
        "testNum": 1,
        "title": "Bài 49: So sánh hai phân số - Đề số 1",
        "topic": "So sánh hai phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "So sánh hai phân số cùng mẫu số: Trong hai phân số cùng mẫu số, phân số nào có tử số lớn hơn thì:", ["Lớn hơn", "Bé hơn", "Bằng nhau", "Không so sánh được"], 0, "Quy tắc so sánh hai phân số cùng mẫu số.", "Nhận biết"),
            make_mc(2, "Điền dấu thích hợp: 5/9 ... 7/9:", ["<", ">", "=", "Không so sánh được"], 0, "5 < 7 nên 5/9 < 7/9.", "Nhận biết"),
            make_mc(3, "So sánh hai phân số 2/3 và 3/4:", ["2/3 < 3/4", "2/3 > 3/4", "2/3 = 3/4", "Không so sánh được"], 0, "2/3 = 8/12 và 3/4 = 9/12. Vì 8/12 < 9/12 nên 2/3 < 3/4.", "Thông hiểu"),
            make_mc(4, "Trong hai phân số có cùng tử số (khác 0), phân số nào có mẫu số bé hơn thì:", ["Lớn hơn", "Bé hơn", "Bằng nhau", "Bằng 1"], 0, "Phân số có mẫu số bé hơn thì lớn hơn.", "Nhận biết"),
            make_mc(5, "So sánh hai phân số 4/7 và 4/9:", ["4/7 > 4/9", "4/7 < 4/9", "4/7 = 4/9", "Không so sánh được"], 0, "Cùng tử số 4, mẫu số 7 < 9 nên 4/7 > 4/9.", "Thông hiểu"),
            make_mc(6, "Trong các phân số 1/5, 3/5, 4/5, 2/5, phân số lớn nhất là:", ["4/5", "3/5", "2/5", "1/5"], 0, "4/5 có tử số lớn nhất.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Điền dấu (<, >, =) thích hợp vào chỗ chấm:\na) 4/7 ... 6/7\nb) 9/8 ... 7/8\nc) 5/11 ... 5/13\nd) 8/15 ... 8/15", "a) 4/7 < 6/7\nb) 9/8 > 7/8\nc) 5/11 > 5/13\nd) 8/15 = 8/15\nĐáp số: a) <; b) >; c) >; d) =.", "a) <; b) >; c) >; d) =", 4, 1.0, "Thông hiểu"),
            make_essay(2, "So sánh hai phân số (bằng cách quy đồng mẫu số):\na) 3/5 và 4/7\nb) 5/6 và 7/9", "a) MSC là 35: 3/5 = 21/35; 4/7 = 20/35. Vì 21/35 > 20/35 nên 3/5 > 4/7.\nb) MSC là 18: 5/6 = 15/18; 7/9 = 14/18. Vì 15/18 > 14/18 nên 5/6 > 7/9.\nĐáp số: a) 3/5 > 4/7; b) 5/6 > 7/9.", "a) 3/5 > 4/7; b) 5/6 > 7/9", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Sắp xếp các phân số sau theo thứ tự từ bé đến lớn:\na) 2/9, 5/9, 1/9, 8/9\nb) 1/2, 2/3, 3/4", "a) Các phân số cùng mẫu số: 1/9 ; 2/9 ; 5/9 ; 8/9.\nb) Quy đồng mẫu số 12: 1/2 = 6/12; 2/3 = 8/12; 3/4 = 9/12.\nThứ tự từ bé đến lớn là: 1/2 ; 2/3 ; 3/4.\nĐáp số: a) 1/9, 2/9, 5/9, 8/9; b) 1/2, 2/3, 3/4.", "a) 1/9, 2/9, 5/9, 8/9; b) 1/2, 2/3, 3/4", 5, 1.0, "Thông hiểu"),
            make_essay(4, "Có hai đoạn dây: đoạn dây thứ nhất dài 3/5 m, đoạn dây thứ hai dài 4/7 m. Hỏi đoạn dây nào dài hơn?", "Quy đồng mẫu số hai phân số với mẫu số chung 35:\n3/5 = 21/35 (m)\n4/7 = 20/35 (m)\nVì 21/35 > 20/35 nên 3/5 m > 4/7 m.\nVậy đoạn dây thứ nhất dài hơn đoạn dây thứ hai.\nĐáp số: Đoạn dây thứ nhất dài hơn.", "Đoạn thứ nhất", 5, 1.5, "Vận dụng"),
            make_essay(5, "Trong một bài kiểm tra chạy 100 m, An chạy hết 1/4 phút, Bình chạy hết 1/5 phút. Hỏi bạn nào chạy nhanh hơn?", "Cùng quãng đường 100 m, bạn nào chạy hết ít thời gian hơn thì bạn đó chạy nhanh hơn.\nSo sánh hai phân số 1/4 và 1/5:\nVì hai phân số cùng tử số là 1 và 4 < 5 nên 1/4 > 1/5.\nThời gian Bình chạy ít hơn thời gian An chạy, vậy bạn Bình chạy nhanh hơn.\nĐáp số: Bạn Bình chạy nhanh hơn.", "Bạn Bình", 5, 1.5, "Vận dụng"),
            make_essay(6, "So sánh hai phân số sau bằng cách so sánh phần bù tới 1:\n2023/2024 và 2024/2025", "Ta có:\n1 - 2023/2024 = 1/2024\n1 - 2024/2025 = 1/2025\nVì 1/2024 > 1/2025 (hai phân số cùng tử số 1, mẫu số 2024 < 2025) nên:\n2023/2024 < 2024/2025.\nĐáp số: 2023/2024 < 2024/2025.", "2023/2024 < 2024/2025", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b49_test2"] = {
        "id": "th4_b49_test2",
        "lessonId": "th4_b49",
        "lessonNum": 49,
        "testNum": 2,
        "title": "Bài 49: So sánh hai phân số - Đề số 2",
        "topic": "So sánh hai phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "So sánh 7/11 và 5/11:", ["7/11 > 5/11", "7/11 < 5/11", "7/11 = 5/11", "Không so sánh được"], 0, "7 > 5 nên 7/11 > 5/11.", "Nhận biết"),
            make_mc(2, "So sánh hai phân số 3/8 và 3/5:", ["3/8 < 3/5", "3/8 > 3/5", "3/8 = 3/5", "Không so sánh được"], 0, "Cùng tử số 3, mẫu 8 > 5 nên 3/8 < 3/5.", "Thông hiểu"),
            make_mc(3, "Phân số nào bé hơn phân số 4/7?", ["3/7", "5/7", "6/7", "4/5"], 0, "3/7 có tử số bé hơn 4.", "Nhận biết"),
            make_mc(4, "So sánh 5/8 và 9/16:", ["5/8 > 9/16", "5/8 < 9/16", "5/8 = 9/16", "Không so sánh được"], 0, "5/8 = 10/16 > 9/16.", "Thông hiểu"),
            make_mc(5, "Trong các phân số 2/3, 3/4, 4/5, 5/6, phân số lớn nhất là:", ["5/6", "4/5", "3/4", "2/3"], 0, "Phần bù tới 1 lần lượt là 1/3, 1/4, 1/5, 1/6. Vì 1/6 bé nhất nên 5/6 lớn nhất.", "Thông hiểu"),
            make_mc(6, "Phân số nào lớn hơn 1?", ["8/7", "7/8", "6/6", "5/9"], 0, "8/7 có tử số lớn hơn mẫu số nên 8/7 > 1.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Điền dấu thích hợp (<, >, =) vào chỗ chấm:\na) 7/15 ... 9/15\nb) 11/10 ... 9/10\nc) 6/13 ... 6/11\nd) 12/12 ... 1", "a) 7/15 < 9/15\nb) 11/10 > 9/10\nc) 6/13 < 6/11\nd) 12/12 = 1\nĐáp số: a) <; b) >; c) <; d) =.", "a) <; b) >; c) <; d) =", 4, 1.0, "Thông hiểu"),
            make_essay(2, "So sánh hai phân số:\na) 4/5 và 5/6\nb) 7/10 và 11/15", "a) Quy đồng mẫu số 30: 4/5 = 24/30; 5/6 = 25/30. Vì 24/30 < 25/30 nên 4/5 < 5/6.\nb) Quy đồng mẫu số 30: 7/10 = 21/30; 11/15 = 22/30. Vì 21/30 < 22/30 nên 7/10 < 11/15.\nĐáp số: a) 4/5 < 5/6; b) 7/10 < 11/15.", "a) 4/5 < 5/6; b) 7/10 < 11/15", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Sắp xếp các phân số sau theo thứ tự từ lớn đến bé:\na) 7/12, 11/12, 5/12, 1/12\nb) 2/3, 5/6, 3/4", "a) Cùng mẫu số 12: 11/12 ; 7/12 ; 5/12 ; 1/12.\nb) Quy đồng mẫu số 12: 2/3 = 8/12; 5/6 = 10/12; 3/4 = 9/12.\nThứ tự từ lớn đến bé là: 5/6 ; 3/4 ; 2/3.\nĐáp số: a) 11/12, 7/12, 5/12, 1/12; b) 5/6, 3/4, 2/3.", "a) 11/12, 7/12, 5/12, 1/12; b) 5/6, 3/4, 2/3", 5, 1.0, "Thông hiểu"),
            make_essay(4, "Có hai can đựng nước: Can A đựng 3/4 lít nước, can B đựng 7/10 lít nước. Hỏi can nào đựng nhiều nước hơn?", "Quy đồng mẫu số hai phân số với mẫu số chung 20:\n3/4 = 15/20 (lít)\n7/10 = 14/20 (lít)\nVì 15/20 > 14/20 nên 3/4 lít > 7/10 lít.\nVậy can A đựng nhiều nước hơn can B.\nĐáp số: Can A đựng nhiều hơn.", "Can A", 5, 1.5, "Vận dụng"),
            make_essay(5, "Ba bạn Hoa, Mai, Lan cùng đọc một quyển truyện như nhau. Sau một tuần, Hoa đọc được 2/3 quyển truyện, Mai đọc được 3/4 quyển truyện, Lan đọc được 5/6 quyển truyện. Hỏi bạn nào đọc được nhiều trang truyện nhất?", "Quy đồng mẫu số ba phân số với mẫu số chung 12:\n2/3 = 8/12\n3/4 = 9/12\n5/6 = 10/12\nVì 8/12 < 9/12 < 10/12 nên 2/3 < 3/4 < 5/6.\nVậy bạn Lan đọc được nhiều trang truyện nhất.\nĐáp số: Bạn Lan.", "Bạn Lan", 5, 1.5, "Vận dụng"),
            make_essay(6, "So sánh hai phân số: 15/17 và 13/19 không cần quy đồng mẫu số (sử dụng phân số trung gian 15/19 hoặc 13/17).", "Ta có: 15/17 > 15/19 (hai phân số cùng tử số 15, mẫu số 17 < 19).\nMà 15/19 > 13/19 (hai phân số cùng mẫu số 19, tử số 15 > 13).\nDo đó theo tính chất bắc cầu: 15/17 > 13/19.\nĐáp số: 15/17 > 13/19.", "15/17 > 13/19", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b49_test3"] = {
        "id": "th4_b49_test3",
        "lessonId": "th4_b49",
        "lessonNum": 49,
        "testNum": 3,
        "title": "Bài 49: So sánh hai phân số - Đề số 3",
        "topic": "So sánh hai phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Điền dấu thích hợp: 8/13 ... 11/13:", ["<", ">", "=", "Không so sánh được"], 0, "8 < 11 nên 8/13 < 11/13.", "Nhận biết"),
            make_mc(2, "So sánh hai phân số 7/10 và 7/12:", ["7/10 > 7/12", "7/10 < 7/12", "7/10 = 7/12", "Không so sánh được"], 0, "Cùng tử số 7, mẫu số 10 < 12 nên 7/10 > 7/12.", "Thông hiểu"),
            make_mc(3, "So sánh 2/5 và 3/10:", ["2/5 > 3/10", "2/5 < 3/10", "2/5 = 3/10", "Không so sánh được"], 0, "2/5 = 4/10 > 3/10.", "Thông hiểu"),
            make_mc(4, "Trong các phân số sau, phân số nào bé nhất?", ["1/8", "3/8", "5/8", "7/8"], 0, "1/8 có tử số bé nhất.", "Nhận biết"),
            make_mc(5, "So sánh hai phân số 5/6 và 6/7:", ["5/6 < 6/7", "5/6 > 6/7", "5/6 = 6/7", "Không so sánh được"], 0, "1 - 5/6 = 1/6; 1 - 6/7 = 1/7. Vì 1/6 > 1/7 nên 5/6 < 6/7.", "Thông hiểu"),
            make_mc(6, "Phân số 9/8 lớn hơn phân số nào sau đây?", ["8/9", "10/8", "9/7", "11/8"], 0, "9/8 > 1 trong khi 8/9 < 1 nên 9/8 > 8/9.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Điền dấu (<, >, =) thích hợp vào chỗ chấm:\na) 5/8 ... 3/8\nb) 7/9 ... 7/11\nc) 6/7 ... 12/14\nd) 15/14 ... 1", "a) 5/8 > 3/8\nb) 7/9 > 7/11\nc) 6/7 = 12/14\nd) 15/14 > 1\nĐáp số: a) >; b) >; c) =; d) >.", "a) >; b) >; c) =; d) >", 4, 1.0, "Thông hiểu"),
            make_essay(2, "So sánh hai phân số bằng cách quy đồng mẫu số:\na) 5/7 và 3/4\nb) 7/8 và 8/9", "a) MSC là 28: 5/7 = 20/28; 3/4 = 21/28. Vì 20/28 < 21/28 nên 5/7 < 3/4.\nb) MSC là 72: 7/8 = 63/72; 8/9 = 64/72. Vì 63/72 < 64/72 nên 7/8 < 8/9.\nĐáp số: a) 5/7 < 3/4; b) 7/8 < 8/9.", "a) 5/7 < 3/4; b) 7/8 < 8/9", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Sắp xếp các phân số sau theo thứ tự từ bé đến lớn:\na) 4/15, 8/15, 2/15, 11/15\nb) 1/3, 2/5, 3/10", "a) Các phân số cùng mẫu số: 2/15 ; 4/15 ; 8/15 ; 11/15.\nb) Quy đồng mẫu số 30: 1/3 = 10/30; 2/5 = 12/30; 3/10 = 9/30.\nThứ tự từ bé đến lớn là: 3/10 ; 1/3 ; 2/5.\nĐáp số: a) 2/15, 4/15, 8/15, 11/15; b) 3/10, 1/3, 2/5.", "a) 2/15, 4/15, 8/15, 11/15; b) 3/10, 1/3, 2/5", 5, 1.0, "Thông hiểu"),
            make_essay(4, "Hai máy bơm cùng bơm nước vào hai bể nước như nhau. Sau một giờ, máy bơm thứ nhất bơm được 5/8 bể, máy bơm thứ hai bơm được 7/12 bể. Hỏi máy bơm nào bơm được nhiều nước hơn?", "Quy đồng mẫu số hai phân số với mẫu số chung 24:\n5/8 = 15/24 (bể)\n7/12 = 14/24 (bể)\nVì 15/24 > 14/24 nên 5/8 bể > 7/12 bể.\nVậy máy bơm thứ nhất bơm được nhiều nước hơn máy bơm thứ hai.\nĐáp số: Máy bơm thứ nhất.", "Máy thứ nhất", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một cửa hàng buổi sáng bán được 3/8 bao gạo, buổi chiều bán được 2/5 bao gạo đó. Hỏi buổi nào cửa hàng bán được nhiều gạo hơn?", "Quy đồng mẫu số hai phân số với mẫu số chung 40:\n3/8 = 15/40 (bao gạo)\n2/5 = 16/40 (bao gạo)\nVì 16/40 > 15/40 nên 2/5 > 3/8.\nVậy buổi chiều cửa hàng bán được nhiều gạo hơn buổi sáng.\nĐáp số: Buổi chiều bán được nhiều hơn.", "Buổi chiều", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm một phân số có mẫu số là 9 sao cho phân số đó lớn hơn 1/3 và bé hơn 2/3.", "Quy đồng mẫu số hai phân số 1/3 và 2/3 với mẫu số 9:\n1/3 = 3/9\n2/3 = 6/9\nPhân số có mẫu số là 9 nằm giữa 3/9 và 6/9 là 4/9 hoặc 5/9.\nĐáp số: 4/9 hoặc 5/9.", "4/9 hoặc 5/9", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 50: LUYỆN TẬP CHUNG CHỦ ĐỀ 10 (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b50_test1"] = {
        "id": "th4_b50_test1",
        "lessonId": "th4_b50",
        "lessonNum": 50,
        "testNum": 1,
        "title": "Bài 50: Luyện tập chung Chủ đề 10 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 10",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số nào đã được rút gọn về dạng tối giản?", ["7/9", "6/8", "15/20", "9/12"], 0, "7/9 tối giản.", "Nhận biết"),
            make_mc(2, "Phân số bằng phân số 3/5 là:", ["12/20", "9/20", "6/15", "15/30"], 0, "3/5 = 12/20 (cùng nhân 4).", "Thông hiểu"),
            make_mc(3, "Trong các phân số 4/5, 5/6, 7/7, 8/5, phân số lớn hơn 1 là:", ["8/5", "4/5", "5/6", "7/7"], 0, "8/5 có tử số lớn hơn mẫu số.", "Thông hiểu"),
            make_mc(4, "Quy đồng mẫu số hai phân số 2/3 và 3/4 ta được hai phân số:", ["8/12 và 9/12", "6/12 và 9/12", "8/12 và 6/12", "2/12 và 3/12"], 0, "2/3 = 8/12 và 3/4 = 9/12.", "Thông hiểu"),
            make_mc(5, "Rút gọn phân số 24/36 về tối giản được:", ["2/3", "4/6", "6/9", "12/18"], 0, "24/36 = 2/3.", "Thông hiểu"),
            make_mc(6, "So sánh hai phân số 4/7 và 5/8:", ["4/7 < 5/8", "4/7 > 5/8", "4/7 = 5/8", "Không so sánh được"], 0, "4/7 = 32/56 và 5/8 = 35/56 nên 4/7 < 5/8.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) 18/24\nb) 25/35\nc) 36/48\nd) 40/60", "a) 18/24 = 3/4\nb) 25/35 = 5/7\nc) 36/48 = 3/4\nd) 40/60 = 2/3\nĐáp số: a) 3/4; b) 5/7; c) 3/4; d) 2/3.", "a) 3/4; b) 5/7; c) 3/4; d) 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Quy đồng mẫu số các phân số:\na) 3/5 và 4/7\nb) 5/8 và 7/16", "a) MSC là 35: 3/5 = 21/35; 4/7 = 20/35.\nb) MSC là 16: 5/8 = 10/16; giữ nguyên 7/16.\nĐáp số: a) 21/35 và 20/35; b) 10/16 và 7/16.", "a) 21/35 và 20/35; b) 10/16 và 7/16", 4, 1.0, "Thông hiểu"),
            make_essay(3, "So sánh các phân số sau:\na) 5/9 và 5/11\nb) 4/5 và 7/10\nc) 8/7 và 1\nd) 9/10 và 10/11", "a) 5/9 > 5/11 (cùng tử số 5, 9 < 11)\nb) 4/5 = 8/10 > 7/10\nc) 8/7 > 1\nd) 1 - 9/10 = 1/10; 1 - 10/11 = 1/11. Vì 1/10 > 1/11 nên 9/10 < 10/11.\nĐáp số: a) >; b) >; c) >; d) <.", "a) >; b) >; c) >; d) <", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chiều dài 24 m, chiều rộng bằng 3/4 chiều dài. Tính chu vi và diện tích mảnh vườn đó.", "Chiều rộng mảnh vườn là:\n24 x 3 : 4 = 18 (m)\nChu vi mảnh vườn là:\n(24 + 18) x 2 = 84 (m)\nDiện tích mảnh vườn là:\n24 x 18 = 432 (m²)\nĐáp số: Chu vi: 84 m; Diện tích: 432 m².", "Chu vi: 84 m; Diện tích: 432 m²", 6, 1.5, "Vận dụng"),
            make_essay(5, "Lớp 4A có 32 học sinh, trong đó có 12 bạn tham gia câu lạc bộ cờ vua, 16 bạn tham gia câu lạc bộ bóng rổ, còn lại tham gia câu lạc bộ bơi lội.\na) Viết phân số chỉ số học sinh tham gia câu lạc bộ bơi lội so với cả lớp.\nb) Rút gọn phân số đó về dạng tối giản.", "a) Số học sinh tham gia câu lạc bộ bơi lội là:\n32 - (12 + 16) = 4 (học sinh)\nPhân số chỉ số học sinh bơi lội là: 4/32.\nb) Rút gọn: 4/32 = (4 : 4)/(32 : 4) = 1/8.\nĐáp số: a) 4/32; b) 1/8.", "a) 4/32; b) 1/8", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm phân số có mẫu số là 30 bằng phân số 3/5.", "Ta có:\n3/5 = (3 x 6)/(5 x 6) = 18/30\nVậy phân số cần tìm là 18/30.\nĐáp số: 18/30.", "18/30", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b50_test2"] = {
        "id": "th4_b50_test2",
        "lessonId": "th4_b50",
        "lessonNum": 50,
        "testNum": 2,
        "title": "Bài 50: Luyện tập chung Chủ đề 10 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 10",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số 15/25 rút gọn về tối giản là:", ["3/5", "5/3", "1/5", "3/4"], 0, "15/25 = 3/5.", "Thông hiểu"),
            make_mc(2, "Số thích hợp để 4/9 = 16/... là:", ["36", "32", "27", "40"], 0, "16 : 4 = 4, 9 x 4 = 36.", "Thông hiểu"),
            make_mc(3, "So sánh hai phân số 5/8 và 7/12:", ["5/8 > 7/12", "5/8 < 7/12", "5/8 = 7/12", "Không so sánh được"], 0, "5/8 = 15/24 > 7/12 = 14/24.", "Thông hiểu"),
            make_mc(4, "Phân số nào bé hơn 1?", ["8/9", "9/8", "9/9", "10/9"], 0, "8/9 có tử số bé hơn mẫu số.", "Nhận biết"),
            make_mc(5, "Mẫu số chung nhỏ nhất của 3/10 và 4/15 là:", ["30", "150", "20", "60"], 0, "30 chia hết cho cả 10 và 15.", "Thông hiểu"),
            make_mc(6, "Trong các phân số 2/7, 4/7, 5/7, 6/7, phân số lớn nhất là:", ["6/7", "5/7", "4/7", "2/7"], 0, "Cùng mẫu số 7, tử số 6 lớn nhất.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau về dạng tối giản:\na) 21/28\nb) 35/45\nc) 48/64\nd) 30/75", "a) 21/28 = 3/4\nb) 35/45 = 7/9\nc) 48/64 = 3/4\nd) 30/75 = 2/5\nĐáp số: a) 3/4; b) 7/9; c) 3/4; d) 2/5.", "a) 3/4; b) 7/9; c) 3/4; d) 2/5", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Quy đồng mẫu số các phân số:\na) 2/3 và 5/8\nb) 7/12 và 11/24", "a) MSC là 24: 2/3 = 16/24; 5/8 = 15/24.\nb) MSC là 24: 7/12 = 14/24; giữ nguyên 11/24.\nĐáp số: a) 16/24 và 15/24; b) 14/24 và 11/24.", "a) 16/24 và 15/24; b) 14/24 và 11/24", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Sắp xếp các phân số sau theo thứ tự từ bé đến lớn:\na) 5/13, 2/13, 8/13, 11/13\nb) 1/2, 3/5, 7/10", "a) Các phân số cùng mẫu số: 2/13 ; 5/13 ; 8/13 ; 11/13.\nb) Quy đồng mẫu số 10: 1/2 = 5/10; 3/5 = 6/10; 7/10.\nThứ tự từ bé đến lớn là: 1/2 ; 3/5 ; 7/10.\nĐáp số: a) 2/13, 5/13, 8/13, 11/13; b) 1/2, 3/5, 7/10.", "a) 2/13, 5/13, 8/13, 11/13; b) 1/2, 3/5, 7/10", 5, 1.0, "Thông hiểu"),
            make_essay(4, "Một hộp bi có 40 viên bi gồm 15 viên bi đỏ, 10 viên bi xanh và 15 viên bi vàng.\na) Viết phân số chỉ số bi xanh so với tổng số bi trong hộp.\nb) Rút gọn phân số đó thành phân số tối giản.", "a) Phân số chỉ số bi xanh là: 10/40.\nb) Rút gọn: 10/40 = (10 : 10)/(40 : 10) = 1/4.\nĐáp số: a) 10/40; b) 1/4.", "a) 10/40; b) 1/4", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh đất hình bình hành có độ dài đáy là 28 m, chiều cao tương ứng bằng 3/4 độ dài đáy. Tính diện tích mảnh đất hình bình hành đó.", "Chiều cao mảnh đất hình bình hành là:\n28 x 3 : 4 = 21 (m)\nDiện tích mảnh đất là:\n28 x 21 = 588 (m²)\nĐáp số: 588 m².", "588 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên x sao cho: 3/5 = x/20.", "Ta có:\n3/5 = (3 x 4)/(5 x 4) = 12/20\nVì 12/20 = x/20 nên x = 12.\nĐáp số: x = 12.", "x = 12", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b50_test3"] = {
        "id": "th4_b50_test3",
        "lessonId": "th4_b50",
        "lessonNum": 50,
        "testNum": 3,
        "title": "Bài 50: Luyện tập chung Chủ đề 10 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 10",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số nào bằng phân số 2/7?", ["6/21", "4/21", "6/14", "8/21"], 0, "2/7 = (2 x 3)/(7 x 3) = 6/21.", "Thông hiểu"),
            make_mc(2, "Rút gọn phân số 36/45 về tối giản ta được:", ["4/5", "3/5", "12/15", "9/15"], 0, "36 : 9 = 4, 45 : 9 = 5. Kết quả 4/5.", "Thông hiểu"),
            make_mc(3, "So sánh hai phân số 3/4 và 5/7:", ["3/4 > 5/7", "3/4 < 5/7", "3/4 = 5/7", "Không so sánh được"], 0, "3/4 = 21/28 > 5/7 = 20/28.", "Thông hiểu"),
            make_mc(4, "Phân số nào sau đây lớn hơn 1?", ["9/8", "8/9", "8/8", "7/8"], 0, "9/8 có tử số lớn hơn mẫu số.", "Nhận biết"),
            make_mc(5, "Khi quy đồng mẫu số của 3/8 và 5/12 với mẫu số chung nhỏ nhất là:", ["24", "48", "96", "36"], 0, "24 chia hết cho cả 8 và 12.", "Thông hiểu"),
            make_mc(6, "Trong các phân số 1/2, 1/4, 1/6, 1/8, phân số có giá trị lớn nhất là:", ["1/2", "1/4", "1/6", "1/8"], 0, "Cùng tử số 1, mẫu số bé nhất là 2 nên 1/2 lớn nhất.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) 24/30\nb) 27/36\nc) 35/50\nd) 44/66", "a) 24/30 = 4/5\nb) 27/36 = 3/4\nc) 35/50 = 7/10\nd) 44/66 = 2/3\nĐáp số: a) 4/5; b) 3/4; c) 7/10; d) 2/3.", "a) 4/5; b) 3/4; c) 7/10; d) 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Quy đồng mẫu số các phân số:\na) 4/5 và 5/9\nb) 5/14 và 3/7", "a) MSC là 45: 4/5 = 36/45; 5/9 = 25/45.\nb) MSC là 14: giữ nguyên 5/14; 3/7 = 6/14.\nĐáp số: a) 36/45 và 25/45; b) 5/14 và 6/14.", "a) 36/45 và 25/45; b) 5/14 và 6/14", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Sắp xếp các phân số sau theo thứ tự từ lớn đến bé:\na) 9/11, 4/11, 7/11, 10/11\nb) 5/6, 2/3, 7/12", "a) Cùng mẫu số 11: 10/11 ; 9/11 ; 7/11 ; 4/11.\nb) Quy đồng mẫu số 12: 5/6 = 10/12; 2/3 = 8/12; giữ nguyên 7/12.\nThứ tự từ lớn đến bé: 5/6 ; 2/3 ; 7/12.\nĐáp số: a) 10/11, 9/11, 7/11, 4/11; b) 5/6, 2/3, 7/12.", "a) 10/11, 9/11, 7/11, 4/11; b) 5/6, 2/3, 7/12", 5, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại có 90 con gà và vịt, trong đó có 54 con gà.\na) Viết phân số chỉ số con gà so với tổng số gia cầm.\nb) Rút gọn phân số đó thành phân số tối giản.", "a) Phân số chỉ số con gà là: 54/90.\nb) Rút gọn: 54/90 = (54 : 18)/(90 : 18) = 3/5.\nĐáp số: a) 54/90; b) 3/5.", "a) 54/90; b) 3/5", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một thửa ruộng hình bình hành có độ dài đáy là 35 m, chiều cao bằng 4/5 độ dài đáy. Tính diện tích của thửa ruộng đó.", "Chiều cao thửa ruộng là:\n35 x 4 : 5 = 28 (m)\nDiện tích thửa ruộng hình bình hành là:\n35 x 28 = 980 (m²)\nĐáp số: 980 m².", "980 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên a biết: 14/(a - 2) = 2/3.", "Ta có:\n2/3 = (2 x 7)/(3 x 7) = 14/21\nDo đó: 14/(a - 2) = 14/21\nSuy ra: a - 2 = 21\na = 21 + 2 = 23\nĐáp số: a = 23.", "a = 23", 4, 1.0, "Vận dụng cao")
        ]
    }

    return exams
