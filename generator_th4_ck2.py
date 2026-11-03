# -*- coding: utf-8 -*-
"""
HỆ THỐNG 8 ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN LỚP 4
Bộ sách: Kết nối tri thức với cuộc sống
Mã kỳ thi: th4_ck2 (Đề 01 đến Đề 08)
Phạm vi kiến thức:
- Phép cộng, trừ, nhân, chia phân số
- Tìm phân số của một số
- Khái niệm tỉ số, tỉ lệ bản đồ
- Tìm hai số khi biết tổng và tỉ số của hai số đó
- Tìm hai số khi biết hiệu và tỉ số của hai số đó
- Hình học & đo lường: hình thoi, diện tích hình thoi, đơn vị đo diện tích
- Ôn tập cuối năm toàn diện.
Chuẩn mực sư phạm:
- Thời gian làm bài: 40 phút, Thang điểm: 10.0
- Phần 1 (3.0đ): 6 câu trắc nghiệm (0.5đ/câu), tiêu đề strictly '**Câu [Số]:** '
- Phần 2 (7.0đ): 6 câu tự luận (1.0, 1.0, 1.0, 1.5, 1.5, 1.0đ), tiêu đề strictly '**Bài [Số]:** '
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

def get_th4_ck2_exams():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 01 (th4_ck2_de01)
    # =========================================================================
    exams["th4_ck2_de01"] = {
        "id": "th4_ck2_de01",
        "code": "CK2-DE01",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 01)",
        "grade": "4",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 3/7 + 2/7 là:", ["5/14", "5/7", "1/7", "6/7"], 1, "Cộng hai phân số cùng mẫu số: (3 + 2)/7 = 5/7.", "Nhận biết"),
            make_mc(2, "Tìm 3/4 của 24 kg ta được kết quả là:", ["18 kg", "16 kg", "32 kg", "12 kg"], 0, "24 x 3/4 = (24 : 4) x 3 = 18 (kg).", "Thông hiểu"),
            make_mc(3, "Một hình thoi có độ dài hai đường chéo là 12 cm và 8 cm. Diện tích của hình thoi đó là:", ["96 cm²", "48 cm²", "20 cm²", "40 cm²"], 1, "Diện tích hình thoi = (12 x 8) : 2 = 48 (cm²).", "Thông hiểu"),
            make_mc(4, "Tỉ số của số con gà và số con vịt là 3/5. Nếu có 15 con gà thì có bao nhiêu con vịt?", ["25 con", "20 con", "30 con", "9 con"], 0, "Số con vịt là: 15 : 3 x 5 = 25 (con).", "Thông hiểu"),
            make_mc(5, "Kết quả của phép nhân 5/8 x 4/15 sau khi rút gọn tối giản là:", ["20/120", "1/6", "1/3", "2/15"], 1, "5/8 x 4/15 = (5 x 4)/(8 x 15) = 20/120 = 1/6.", "Thông hiểu"),
            make_mc(6, "Trên bản đồ tỉ lệ 1 : 1000, chiều dài một phòng học đo được 1 cm. Chiều dài thật của phòng học đó là:", ["10 m", "100 m", "1 m", "1000 m"], 0, "Chiều dài thật là: 1 x 1000 = 1000 cm = 10 m.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 5/8 + 1/4\nb) 7/9 - 1/3", "a) 5/8 + 1/4 = 5/8 + 2/8 = 7/8\nb) 7/9 - 1/3 = 7/9 - 3/9 = 4/9", "a) 7/8; b) 4/9", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 3/5 x 10/9\nb) 4/7 : 2/3", "a) 3/5 x 10/9 = (3 x 10)/(5 x 9) = 30/45 = 2/3\nb) 4/7 : 2/3 = 4/7 x 3/2 = 12/14 = 6/7", "a) 2/3; b) 6/7", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x - 2/5 = 3/10\nb) x x 3/4 = 9/8", "a) x - 2/5 = 3/10\nx = 3/10 + 2/5\nx = 3/10 + 4/10 = 7/10\nb) x x 3/4 = 9/8\nx = 9/8 : 3/4\nx = 9/8 x 4/3 = 3/2", "a) x = 7/10; b) x = 3/2", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chu vi là 120 m. Chiều rộng bằng 2/3 chiều dài. Tính diện tích của mảnh vườn đó.", "Nửa chu vi mảnh vườn là:\n120 : 2 = 60 (m)\nTổng số phần bằng nhau là:\n2 + 3 = 5 (phần)\nChiều rộng mảnh vườn là:\n60 : 5 x 2 = 24 (m)\nChiều dài mảnh vườn là:\n60 - 24 = 36 (m)\nDiện tích mảnh vườn là:\n36 x 24 = 864 (m²)\nĐáp số: 864 m².", "864 m²", 6, 1.5, "Vận dụng"),
            make_essay(5, "Một hình thoi có đường chéo thứ nhất dài 18 cm, đường chéo thứ hai bằng 5/6 đường chéo thứ nhất. Tính diện tích của hình thoi đó.", "Độ dài đường chéo thứ hai là:\n18 x 5/6 = 15 (cm)\nDiện tích của hình thoi là:\n(18 x 15) : 2 = 135 (cm²)\nĐáp số: 135 cm².", "135 cm²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh giá trị biểu thức sau:\nA = 1/2 + 1/4 + 1/8 + 1/16 + 1/32", "Ta có:\n2 x A = 1 + 1/2 + 1/4 + 1/8 + 1/16\nLấy 2 x A trừ đi A ta được:\nA = 1 - 1/32\nA = 31/32\nĐáp số: 31/32.", "31/32", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 02 (th4_ck2_de02)
    # =========================================================================
    exams["th4_ck2_de02"] = {
        "id": "th4_ck2_de02",
        "code": "CK2-DE02",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 02)",
        "grade": "4",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép trừ 5/6 - 1/2 là:", ["4/4", "1/3", "2/3", "4/6"], 1, "5/6 - 1/2 = 5/6 - 3/6 = 2/6 = 1/3.", "Thông hiểu"),
            make_mc(2, "Tìm 2/5 của 150 m:", ["60 m", "30 m", "75 m", "50 m"], 0, "150 x 2/5 = 60 (m).", "Thông hiểu"),
            make_mc(3, "Diện tích hình thoi có hai đường chéo dài 16 dm và 10 dm là:", ["160 dm²", "80 dm²", "26 dm²", "52 dm²"], 1, "Diện tích hình thoi = (16 x 10) : 2 = 80 (dm²).", "Thông hiểu"),
            make_mc(4, "Một lớp học có 18 bạn nam và 16 bạn nữ. Tỉ số của số bạn nữ so với số bạn nam là:", ["8/9", "9/8", "16/34", "18/34"], 0, "Tỉ số của số bạn nữ so với số bạn nam là 16/18 = 8/9.", "Nhận biết"),
            make_mc(5, "Kết quả của phép chia 7/12 : 14/15 là:", ["5/8", "4/5", "8/5", "7/15"], 0, "7/12 : 14/15 = 7/12 x 15/14 = (7 x 15)/(12 x 14) = 5/8.", "Thông hiểu"),
            make_mc(6, "Khoảng cách giữa hai điểm trên bản đồ tỉ lệ 1 : 100 000 là 5 cm. Khoảng cách thật giữa hai điểm đó là:", ["5 km", "50 km", "500 m", "50 000 cm"], 0, "Khoảng cách thật là: 5 x 100 000 = 500 000 cm = 5 km.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 2/3 + 3/5\nb) 8/7 - 3/4", "a) 2/3 + 3/5 = 10/15 + 9/15 = 19/15\nb) 8/7 - 3/4 = 32/28 - 21/28 = 11/28", "a) 19/15; b) 11/28", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 4/9 x 3/8\nb) 5/6 : 10/9", "a) 4/9 x 3/8 = (4 x 3)/(9 x 8) = 12/72 = 1/6\nb) 5/6 : 10/9 = 5/6 x 9/10 = 45/60 = 3/4", "a) 1/6; b) 3/4", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x + 3/7 = 5/6\nb) x : 4/5 = 15/16", "a) x + 3/7 = 5/6\nx = 5/6 - 3/7\nx = 35/42 - 18/42 = 17/42\nb) x : 4/5 = 15/16\nx = 15/16 x 4/5 = 3/4", "a) x = 17/42; b) x = 3/4", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Mẹ nhiều hơn con 28 tuổi. Tuổi con bằng 2/9 tuổi mẹ. Tính tuổi của mỗi người.", "Hiệu số phần bằng nhau là:\n9 - 2 = 7 (phần)\nTuổi của con là:\n28 : 7 x 2 = 8 (tuổi)\nTuổi của mẹ là:\n8 + 28 = 36 (tuổi)\nĐáp số: Con: 8 tuổi; Mẹ: 36 tuổi.", "Con: 8 tuổi; Mẹ: 36 tuổi", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một tấm bìa hình thoi có tổng độ dài hai đường chéo là 42 cm. Đường chéo thứ nhất bằng 3/4 đường chéo thứ hai. Tính diện tích của tấm bìa hình thoi đó.", "Tổng số phần bằng nhau là:\n3 + 4 = 7 (phần)\nĐộ dài đường chéo thứ nhất là:\n42 : 7 x 3 = 18 (cm)\nĐộ dài đường chéo thứ hai là:\n42 - 18 = 24 (cm)\nDiện tích tấm bìa hình thoi là:\n(18 x 24) : 2 = 216 (cm²)\nĐáp số: 216 cm².", "216 cm²", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính bằng cách thuận tiện nhất:\n3/5 x 7/9 + 3/5 x 2/9", "Áp dụng tính chất phân phối:\n3/5 x 7/9 + 3/5 x 2/9 = 3/5 x (7/9 + 2/9)\n= 3/5 x 9/9\n= 3/5 x 1 = 3/5\nĐáp số: 3/5.", "3/5", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 03 (th4_ck2_de03)
    # =========================================================================
    exams["th4_ck2_de03"] = {
        "id": "th4_ck2_de03",
        "code": "CK2-DE03",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 03)",
        "grade": "4",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 2 + 3/5 là:", ["5/5", "13/5", "7/5", "6/5"], 1, "2 + 3/5 = 10/5 + 3/5 = 13/5.", "Thông hiểu"),
            make_mc(2, "Tìm 4/7 của 35 lít dầu:", ["20 lít", "25 lít", "28 lít", "15 lít"], 0, "35 x 4/7 = 20 (lít).", "Thông hiểu"),
            make_mc(3, "Diện tích hình thoi có độ dài hai đường chéo là 20 cm và 15 cm là:", ["300 cm²", "150 cm²", "35 cm²", "70 cm²"], 1, "Diện tích = (20 x 15) : 2 = 150 (cm²).", "Thông hiểu"),
            make_mc(4, "Tổng của hai số là 80, tỉ số của hai số là 3/5. Số bé là:", ["30", "50", "48", "32"], 0, "Số bé = 80 : (3 + 5) x 3 = 30.", "Thông hiểu"),
            make_mc(5, "Kết quả của phép tính 7/10 x 5/14 sau khi rút gọn là:", ["1/4", "35/140", "1/2", "5/20"], 0, "7/10 x 5/14 = (7 x 5)/(10 x 14) = 1/4.", "Thông hiểu"),
            make_mc(6, "Một sân vận động có chiều dài thật 100 m. Trên bản đồ tỉ lệ 1 : 2000, chiều dài đó vẽ được là:", ["5 cm", "50 cm", "2 cm", "20 cm"], 0, "Đổi 100 m = 10 000 cm. Chiều dài trên bản đồ: 10 000 : 2000 = 5 (cm).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 7/12 + 5/6\nb) 3 - 5/4", "a) 7/12 + 5/6 = 7/12 + 10/12 = 17/12\nb) 3 - 5/4 = 12/4 - 5/4 = 7/4", "a) 17/12; b) 7/4", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 6/7 x 14/15\nb) 8/9 : 4", "a) 6/7 x 14/15 = (6 x 14)/(7 x 15) = 84/105 = 4/5\nb) 8/9 : 4 = 8/9 x 1/4 = 2/9", "a) 4/5; b) 2/9", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính giá trị biểu thức:\n(1/2 + 1/3) x 6/5", "Ta có:\n(1/2 + 1/3) = 3/6 + 2/6 = 5/6\n5/6 x 6/5 = (5 x 6)/(6 x 5) = 1\nĐáp số: 1.", "1", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Hai kho thóc chứa tất cả 240 tấn thóc. Biết rằng số thóc ở kho A bằng 3/5 số thóc ở kho B. Hỏi mỗi kho chứa bao nhiêu tấn thóc?", "Tổng số phần bằng nhau là:\n3 + 5 = 8 (phần)\nSố thóc ở kho A là:\n240 : 8 x 3 = 90 (tấn)\nSố thóc ở kho B là:\n240 - 90 = 150 (tấn)\nĐáp số: Kho A: 90 tấn thóc; Kho B: 150 tấn thóc.", "Kho A: 90 tấn; Kho B: 150 tấn", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh đất hình thoi có đường chéo thứ nhất dài 30 m, đường chéo thứ hai kém đường chéo thứ nhất 8 m. Tính diện tích mảnh đất hình thoi đó.", "Độ dài đường chéo thứ hai là:\n30 - 8 = 22 (m)\nDiện tích mảnh đất hình thoi là:\n(30 x 22) : 2 = 330 (m²)\nĐáp số: 330 m².", "330 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Một cửa hàng buổi sáng bán được 1/3 số gạo, buổi chiều bán được 2/5 số gạo đó. Hỏi cả hai buổi cửa hàng bán được bao nhiêu phần số gạo?", "Cả hai buổi cửa hàng bán được số phần số gạo là:\n1/3 + 2/5 = 5/15 + 6/15 = 11/15 (số gạo)\nĐáp số: 11/15 số gạo.", "11/15 số gạo", 4, 1.0, "Vận dụng")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 04 (th4_ck2_de04)
    # =========================================================================
    exams["th4_ck2_de04"] = {
        "id": "th4_ck2_de04",
        "code": "CK2-DE04",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 04)",
        "grade": "4",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 4 - 3/7 là:", ["1/7", "25/7", "22/7", "5/7"], 1, "4 - 3/7 = 28/7 - 3/7 = 25/7.", "Thông hiểu"),
            make_mc(2, "Tìm 5/8 của số 64:", ["40", "32", "48", "24"], 0, "64 x 5/8 = 40.", "Thông hiểu"),
            make_mc(3, "Diện tích hình thoi có hai đường chéo 24 dm và 18 dm là:", ["432 dm²", "216 dm²", "42 dm²", "84 dm²"], 1, "Diện tích = (24 x 18) : 2 = 216 (dm²).", "Thông hiểu"),
            make_mc(4, "Hiệu của hai số là 45, tỉ số của hai số là 2/5. Số lớn là:", ["75", "30", "60", "90"], 0, "Số lớn = 45 : (5 - 2) x 5 = 75.", "Thông hiểu"),
            make_mc(5, "Kết quả của phép chia 9/16 : 3/8 là:", ["3/2", "2/3", "27/128", "1/2"], 0, "9/16 : 3/8 = 9/16 x 8/3 = 72/48 = 3/2.", "Thông hiểu"),
            make_mc(6, "Trên bản đồ tỉ lệ 1 : 500 000, quãng đường từ A đến B đo được 4 cm. Quãng đường thật từ A đến B là:", ["20 km", "2 km", "200 km", "2000 m"], 0, "Khoảng cách thật: 4 x 500 000 = 2 000 000 cm = 20 km.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 3/10 + 4/15\nb) 9/8 - 5/12", "a) 3/10 + 4/15 = 9/30 + 8/30 = 17/30\nb) 9/8 - 5/12 = 27/24 - 10/24 = 17/24", "a) 17/30; b) 17/24", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 5/12 x 8/15\nb) 6/7 : 9/14", "a) 5/12 x 8/15 = (5 x 8)/(12 x 15) = 40/180 = 2/9\nb) 6/7 : 9/14 = 6/7 x 14/9 = 84/63 = 4/3", "a) 2/9; b) 4/3", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 2/3 = 4/9\nb) x : 5/7 = 14/15", "a) x x 2/3 = 4/9\nx = 4/9 : 2/3\nx = 4/9 x 3/2 = 2/3\nb) x : 5/7 = 14/15\nx = 14/15 x 5/7 = 2/3", "a) x = 2/3; b) x = 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Thùng thứ nhất chứa nhiều hơn thùng thứ hai 36 lít dầu. Biết số dầu thùng thứ hai bằng 3/7 số dầu thùng thứ nhất. Hỏi mỗi thùng chứa bao nhiêu lít dầu?", "Hiệu số phần bằng nhau là:\n7 - 3 = 4 (phần)\nThùng thứ hai chứa số lít dầu là:\n36 : 4 x 3 = 27 (lít)\nThùng thứ nhất chứa số lít dầu là:\n27 + 36 = 63 (lít)\nĐáp số: Thùng 1: 63 lít dầu; Thùng 2: 27 lít dầu.", "Thùng 1: 63 lít; Thùng 2: 27 lít", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh kính hình thoi có độ dài hai đường chéo lần lượt là 40 cm và 25 cm. Tính diện tích mảnh kính đó.", "Diện tích mảnh kính hình thoi là:\n(40 x 25) : 2 = 500 (cm²)\nĐáp số: 500 cm².", "500 cm²", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính bằng cách thuận tiện nhất:\n4/7 x 5/9 + 4/7 x 4/9", "4/7 x 5/9 + 4/7 x 4/9 = 4/7 x (5/9 + 4/9)\n= 4/7 x 9/9\n= 4/7 x 1 = 4/7\nĐáp số: 4/7.", "4/7", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 05 (th4_ck2_de05)
    # =========================================================================
    exams["th4_ck2_de05"] = {
        "id": "th4_ck2_de05",
        "code": "CK2-DE05",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 05)",
        "grade": "4",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 1/4 + 2/3 + 3/4 là:", ["6/11", "5/3", "4/3", "7/4"], 1, "(1/4 + 3/4) + 2/3 = 1 + 2/3 = 5/3.", "Thông hiểu"),
            make_mc(2, "Tìm 3/5 của 100 kg:", ["60 kg", "50 kg", "75 kg", "40 kg"], 0, "100 x 3/5 = 60 (kg).", "Thông hiểu"),
            make_mc(3, "Một hình thoi có diện tích 72 cm², đường chéo thứ nhất dài 12 cm. Độ dài đường chéo thứ hai là:", ["6 cm", "12 cm", "24 cm", "18 cm"], 1, "Độ dài đường chéo thứ hai = 72 x 2 : 12 = 12 (cm).", "Thông hiểu"),
            make_mc(4, "Một tổ có 12 bạn gồm 5 bạn nam và 7 bạn nữ. Tỉ số của số bạn nam so với cả tổ là:", ["5/7", "7/5", "5/12", "7/12"], 2, "Tỉ số là 5/12.", "Nhận biết"),
            make_mc(5, "Kết quả của phép nhân 8/15 x 5/4 sau khi rút gọn tối giản là:", ["2/3", "40/60", "1/3", "4/3"], 0, "8/15 x 5/4 = (8 x 5)/(15 x 4) = 40/60 = 2/3.", "Thông hiểu"),
            make_mc(6, "Khoảng cách giữa hai thành phố là 80 km. Trên bản đồ tỉ lệ 1 : 1 000 000, khoảng cách đó là:", ["8 cm", "80 cm", "0,8 cm", "8 mm"], 0, "80 km = 8 000 000 cm. Chiều dài trên bản đồ: 8 000 000 : 1 000 000 = 8 (cm).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 4/9 + 5/6\nb) 11/15 - 2/5", "a) 4/9 + 5/6 = 8/18 + 15/18 = 23/18\nb) 11/15 - 2/5 = 11/15 - 6/15 = 5/15 = 1/3", "a) 23/18; b) 1/3", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 7/8 x 16/21\nb) 9/10 : 3/5", "a) 7/8 x 16/21 = (7 x 16)/(8 x 21) = 2/3\nb) 9/10 : 3/5 = 9/10 x 5/3 = 45/30 = 3/2", "a) 2/3; b) 3/2", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính giá trị biểu thức:\n(5/6 - 1/3) : 2/3", "Ta có:\n5/6 - 1/3 = 5/6 - 2/6 = 3/6 = 1/2\n1/2 : 2/3 = 1/2 x 3/2 = 3/4\nĐáp số: 3/4.", "3/4", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một thư viện trường học có 630 quyển sách gồm sách giáo khoa và sách tham khảo. Số sách tham khảo bằng 4/5 số sách giáo khoa. Hỏi thư viện có bao nhiêu quyển sách mỗi loại?", "Tổng số phần bằng nhau là:\n4 + 5 = 9 (phần)\nSố quyển sách tham khảo là:\n630 : 9 x 4 = 280 (quyển)\nSố quyển sách giáo khoa là:\n630 - 280 = 350 (quyển)\nĐáp số: Sách tham khảo: 280 quyển; Sách giáo khoa: 350 quyển.", "Sách tham khảo: 280 quyển; Sách GK: 350 quyển", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một bồn hoa hình thoi có đường chéo thứ nhất dài 16 m, đường chéo thứ hai bằng 3/4 đường chéo thứ nhất. Tính diện tích của bồn hoa đó.", "Độ dài đường chéo thứ hai là:\n16 x 3/4 = 12 (m)\nDiện tích của bồn hoa hình thoi là:\n(16 x 12) : 2 = 96 (m²)\nĐáp số: 96 m².", "96 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm phân số tối giản a/b biết: a/b + 1/4 = 5/6.", "a/b = 5/6 - 1/4\na/b = 10/12 - 3/12 = 7/12\nVì 7/12 đã là phân số tối giản nên phân số cần tìm là 7/12.\nĐáp số: 7/12.", "7/12", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 06 (th4_ck2_de06)
    # =========================================================================
    exams["th4_ck2_de06"] = {
        "id": "th4_ck2_de06",
        "code": "CK2-DE06",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 06)",
        "grade": "4",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép chia 3/5 : 2 là:", ["6/5", "3/10", "3/2", "1/5"], 1, "3/5 : 2 = 3/5 x 1/2 = 3/10.", "Thông hiểu"),
            make_mc(2, "Tìm 2/3 của 48 m vải:", ["32 m", "24 m", "16 m", "36 m"], 0, "48 x 2/3 = 32 (m).", "Thông hiểu"),
            make_mc(3, "Diện tích hình thoi có độ dài hai đường chéo 14 cm và 10 cm là:", ["140 cm²", "70 cm²", "24 cm²", "48 cm²"], 1, "Diện tích = (14 x 10) : 2 = 70 (cm²).", "Thông hiểu"),
            make_mc(4, "Một sợi dây dài 28 m được cắt làm hai đoạn, đoạn thứ nhất bằng 3/4 đoạn thứ hai. Chiều dài đoạn thứ nhất là:", ["12 m", "16 m", "14 m", "9 m"], 0, "Đoạn 1 = 28 : (3 + 4) x 3 = 12 (m).", "Thông hiểu"),
            make_mc(5, "Kết quả của phép tính 5/9 + 4/9 x 3/2 là:", ["11/9", "9/9", "15/18", "13/9"], 0, "5/9 + 4/9 x 3/2 = 5/9 + 12/18 = 5/9 + 6/9 = 11/9.", "Thông hiểu"),
            make_mc(6, "Một thửa ruộng hình chữ nhật có chiều dài 60 m. Trên bản đồ tỉ lệ 1 : 500, chiều dài đó được vẽ là:", ["12 cm", "6 cm", "30 cm", "120 cm"], 0, "Đổi 60 m = 6000 cm. Chiều dài trên bản đồ: 6000 : 500 = 12 (cm).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 3/7 + 5/14\nb) 5/8 - 1/6", "a) 3/7 + 5/14 = 6/14 + 5/14 = 11/14\nb) 5/8 - 1/6 = 15/24 - 4/24 = 11/24", "a) 11/14; b) 11/24", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 9/14 x 7/18\nb) 8/15 : 4/5", "a) 9/14 x 7/18 = (9 x 7)/(14 x 18) = 1/4\nb) 8/15 : 4/5 = 8/15 x 5/4 = 40/60 = 2/3", "a) 1/4; b) 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x - 1/3 = 5/12\nb) x : 3/5 = 10/9", "a) x - 1/3 = 5/12\nx = 5/12 + 1/3\nx = 5/12 + 4/12 = 9/12 = 3/4\nb) x : 3/5 = 10/9\nx = 10/9 x 3/5 = 2/3", "a) x = 3/4; b) x = 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại có số gà nhiều hơn số vịt là 120 con. Biết số vịt bằng 3/5 số gà. Hỏi trang trại đó có bao nhiêu con gà và bao nhiêu con vịt?", "Hiệu số phần bằng nhau là:\n5 - 3 = 2 (phần)\nSố con vịt của trang trại là:\n120 : 2 x 3 = 180 (con)\nSố con gà của trang trại là:\n180 + 120 = 300 (con)\nĐáp số: Vịt: 180 con; Gà: 300 con.", "Vịt: 180 con; Gà: 300 con", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một miếng bìa hình thoi có đường chéo lớn dài 24 cm, đường chéo bé bằng 2/3 đường chéo lớn. Tính diện tích miếng bìa đó.", "Độ dài đường chéo bé là:\n24 x 2/3 = 16 (cm)\nDiện tích miếng bìa hình thoi là:\n(24 x 16) : 2 = 192 (cm²)\nĐáp số: 192 cm².", "192 cm²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh giá trị của biểu thức sau:\nA = 1/2 x 2/3 x 3/4 x 4/5 x 5/6", "Rút gọn các thừa số giống nhau ở tử số và mẫu số:\nA = (1 x 2 x 3 x 4 x 5) / (2 x 3 x 4 x 5 x 6)\nA = 1/6\nĐáp số: 1/6.", "1/6", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 07 (th4_ck2_de07)
    # =========================================================================
    exams["th4_ck2_de07"] = {
        "id": "th4_ck2_de07",
        "code": "CK2-DE07",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 07)",
        "grade": "4",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép trừ 7/8 - 5/8 sau khi rút gọn là:", ["2/8", "1/4", "1/2", "3/8"], 1, "7/8 - 5/8 = 2/8 = 1/4.", "Nhận biết"),
            make_mc(2, "Tìm 4/9 của số 81:", ["36", "45", "54", "27"], 0, "81 x 4/9 = 36.", "Thông hiểu"),
            make_mc(3, "Diện tích hình thoi có hai đường chéo dài 30 cm và 20 cm là:", ["600 cm²", "300 cm²", "50 cm²", "100 cm²"], 1, "Diện tích = (30 x 20) : 2 = 300 (cm²).", "Thông hiểu"),
            make_mc(4, "Tổng của hai số là 150, số bé bằng 2/3 số lớn. Số lớn là:", ["90", "60", "100", "50"], 0, "Số lớn = 150 : (2 + 3) x 3 = 90.", "Thông hiểu"),
            make_mc(5, "Kết quả của phép tính 11/12 x 6/11 là:", ["1/2", "66/132", "1/3", "2/3"], 0, "11/12 x 6/11 = (11 x 6)/(12 x 11) = 6/12 = 1/2.", "Thông hiểu"),
            make_mc(6, "Trên bản đồ tỉ lệ 1 : 200, chiều dài một chiếc cầu là 5 cm. Chiều dài thật của cây cầu là:", ["10 m", "100 m", "1000 m", "1 m"], 0, "Chiều dài thật: 5 x 200 = 1000 cm = 10 m.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 5/12 + 3/8\nb) 4/5 - 7/15", "a) 5/12 + 3/8 = 10/24 + 9/24 = 19/24\nb) 4/5 - 7/15 = 12/15 - 7/15 = 5/15 = 1/3", "a) 19/24; b) 1/3", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 4/7 x 14/16\nb) 9/16 : 3/4", "a) 4/7 x 14/16 = (4 x 14)/(7 x 16) = 56/112 = 1/2\nb) 9/16 : 3/4 = 9/16 x 4/3 = 36/48 = 3/4", "a) 1/2; b) 3/4", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính bằng cách thuận tiện nhất:\n5/11 x 7/13 + 5/11 x 6/13", "5/11 x 7/13 + 5/11 x 6/13 = 5/11 x (7/13 + 6/13)\n= 5/11 x 13/13\n= 5/11 x 1 = 5/11\nĐáp số: 5/11.", "5/11", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chu vi là 160 m, chiều dài hơn chiều rộng 20 m. Tính diện tích của mảnh vườn đó.", "Nửa chu vi mảnh vườn là:\n160 : 2 = 80 (m)\nChiều dài mảnh vườn là:\n(80 + 20) : 2 = 50 (m)\nChiều rộng mảnh vườn là:\n50 - 20 = 30 (m)\nDiện tích mảnh vườn là:\n50 x 30 = 1500 (m²)\nĐáp số: 1500 m².", "1500 m²", 6, 1.5, "Vận dụng"),
            make_essay(5, "Một tấm biển quảng cáo hình thoi có độ dài hai đường chéo là 32 dm và 18 dm. Người ta sơn tấm biển đó, chi phí sơn mỗi đề-xi-mét vuông là 500 đồng. Tính tổng chi phí sơn tấm biển đó.", "Diện tích tấm biển hình thoi là:\n(32 x 18) : 2 = 288 (dm²)\nTổng chi phí sơn tấm biển là:\n288 x 500 = 144 000 (đồng)\nĐáp số: 144 000 đồng.", "144 000 đồng", 5, 1.5, "Vận dụng"),
            make_essay(6, "Một người bán được 3/5 số trứng mang đi thì còn lại 24 quả trứng. Hỏi ban đầu người đó mang đi bán bao nhiêu quả trứng?", "Phân số chỉ số trứng còn lại là:\n1 - 3/5 = 2/5 (số trứng)\nSố quả trứng ban đầu người đó mang đi bán là:\n24 : 2/5 = 60 (quả)\nĐáp số: 60 quả trứng.", "60 quả", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08 (th4_ck2_de08)
    # =========================================================================
    exams["th4_ck2_de08"] = {
        "id": "th4_ck2_de08",
        "code": "CK2-DE08",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 08)",
        "grade": "4",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 3/5 + 1/2 là:", ["4/7", "11/10", "4/10", "3/10"], 1, "3/5 + 1/2 = 6/10 + 5/10 = 11/10.", "Thông hiểu"),
            make_mc(2, "Tìm 5/6 của 72 học sinh:", ["60 học sinh", "54 học sinh", "65 học sinh", "48 học sinh"], 0, "72 x 5/6 = 60 (học sinh).", "Thông hiểu"),
            make_mc(3, "Diện tích hình thoi có hai đường chéo là 22 cm và 14 cm là:", ["308 cm²", "154 cm²", "36 cm²", "72 cm²"], 1, "Diện tích = (22 x 14) : 2 = 154 (cm²).", "Thông hiểu"),
            make_mc(4, "Hiệu của hai số là 60, tỉ số của hai số là 1/4. Số bé là:", ["20", "15", "80", "25"], 0, "Số bé = 60 : (4 - 1) x 1 = 20.", "Thông hiểu"),
            make_mc(5, "Kết quả của phép chia 5/8 : 15/16 sau khi rút gọn tối giản là:", ["2/3", "80/120", "3/2", "1/3"], 0, "5/8 : 15/16 = 5/8 x 16/15 = 2/3.", "Thông hiểu"),
            make_mc(6, "Quãng đường từ nhà An đến trường dài thật 2 km. Trên bản đồ tỉ lệ 1 : 50 000, quãng đường đó dài là:", ["4 cm", "40 cm", "2 cm", "10 cm"], 0, "Đổi 2 km = 200 000 cm. Chiều dài trên bản đồ: 200 000 : 50 000 = 4 (cm).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính:\na) 7/10 + 4/15\nb) 9/14 - 2/7", "a) 7/10 + 4/15 = 21/30 + 8/30 = 29/30\nb) 9/14 - 2/7 = 9/14 - 4/14 = 5/14", "a) 29/30; b) 5/14", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính:\na) 8/15 x 5/12\nb) 7/9 : 14/27", "a) 8/15 x 5/12 = (8 x 5)/(15 x 12) = 40/180 = 2/9\nb) 7/9 : 14/27 = 7/9 x 27/14 = 3/2", "a) 2/9; b) 3/2", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x + 2/7 = 5/14\nb) x x 4/9 = 8/15", "a) x + 2/7 = 5/14\nx = 5/14 - 2/7\nx = 5/14 - 4/14 = 1/14\nb) x x 4/9 = 8/15\nx = 8/15 : 4/9\nx = 8/15 x 9/4 = 6/5", "a) x = 1/14; b) x = 6/5", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Cả hai thùng chứa 210 lít nước mắm. Sau khi rót 15 lít từ thùng thứ nhất sang thùng thứ hai thì số nước mắm ở thùng thứ nhất bằng 3/4 số nước mắm ở thùng thứ hai. Hỏi lúc đầu mỗi thùng chứa bao nhiêu lít nước mắm?", "Tổng số lít nước mắm ở cả hai thùng luôn không đổi là 210 lít.\nSố lít nước mắm ở thùng thứ nhất sau khi rót là:\n210 : (3 + 4) x 3 = 90 (lít)\nLúc đầu thùng thứ nhất chứa số lít nước mắm là:\n90 + 15 = 105 (lít)\nLúc đầu thùng thứ hai chứa số lít nước mắm là:\n210 - 105 = 105 (lít)\nĐáp số: Thùng thứ nhất: 105 lít; Thùng thứ hai: 105 lít.", "Thùng 1: 105 lít; Thùng 2: 105 lít", 6, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh đất hình thoi có đường chéo bé dài 20 m, đường chéo lớn bằng 3/2 đường chéo bé. Tính diện tích mảnh đất hình thoi đó.", "Độ dài đường chéo lớn là:\n20 x 3/2 = 30 (m)\nDiện tích mảnh đất hình thoi là:\n(20 x 30) : 2 = 300 (m²)\nĐáp số: 300 m².", "300 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nB = (1 - 1/2) x (1 - 1/3) x (1 - 1/4) x (1 - 1/5)", "Thực hiện trừ trong từng ngoặc:\nB = 1/2 x 2/3 x 3/4 x 4/5\nRút gọn các thừa số giống nhau ở tử và mẫu:\nB = 1/5\nĐáp số: 1/5.", "1/5", 4, 1.0, "Vận dụng cao")
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_th4_ck2_exams()
    print(f"Tổng số đề CK2 Toán 4: {len(ex)} (Kỳ vọng: 8 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
