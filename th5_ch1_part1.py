# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 1: ÔN TẬP VÀ BỔ SUNG (BÀI 1 ĐẾN BÀI 9) - TOÁN 5 KNTT
Mỗi bài có đúng 3 đề kiểm tra độc lập (test1, test2, test3):
- 6 câu trắc nghiệm (part1, mỗi câu 0.5 điểm = 3.0 điểm)
- 6 câu tự luận (part2, 4 câu 1.0 đ + 2 câu 1.5 đ = 7.0 điểm, lineCount: 3 đến 6 dòng)
Tổng điểm: 10.0 điểm, thời gian: 35 phút.
"""

def make_mc(qid, question, options, correct, explanation):
    return {
        "id": qid,
        "question": question,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question, solution, answer, lineCount, points=1.0):
    return {
        "id": qid,
        "question": question,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_ch1_exams():
    exams = {}

    # =========================================================================
    # BÀI 1: ÔN TẬP VỀ SỐ TỰ NHIÊN
    # =========================================================================
    # --- Bài 1 - Đề 1 ---
    exams["th5_b1_test1"] = {
        "id": "th5_b1_test1",
        "lessonId": "th5_b1",
        "lessonNum": 1,
        "testNum": 1,
        "title": "Bài 1: Ôn tập về số tự nhiên - Đề số 1",
        "topic": "Ôn tập về số tự nhiên",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Chữ số 7 trong số 875 420 có giá trị là:", ["700", "7 000", "70 000", "700 000"], 2, "Chữ số 7 thuộc hàng chục nghìn nên có giá trị là 70 000."),
            make_mc(2, "Số 'Mười lăm triệu ba trăm hai mươi nghìn không trăm lẻ năm' viết là:", ["15 320 005", "15 320 050", "15 302 005", "15 032 005"], 0, "Viết đúng các lớp: lớp triệu là 15, lớp nghìn là 320, lớp đơn vị là 005."),
            make_mc(3, "Làm tròn số 4 582 710 đến hàng trăm nghìn ta được số:", ["4 500 000", "4 600 000", "4 580 000", "5 000 000"], 1, "Chữ số hàng chục nghìn là 8 (lớn hơn hoặc bằng 5) nên làm tròn lên thành 4 600 000."),
            make_mc(4, "Trong các số sau, số nào là số chẵn chia hết cho 5?", ["1 245", "3 480", "5 672", "8 915"], 1, "Số chẵn chia hết cho 5 phải có chữ số tận cùng là 0."),
            make_mc(5, "Số tự nhiên lớn nhất có sáu chữ số khác nhau là:", ["999 999", "987 654", "987 650", "986 754"], 1, "Chọn các chữ số lớn nhất giảm dần từ trái sang phải: 9, 8, 7, 6, 5, 4."),
            make_mc(6, "Dãy số tự nhiên liên tiếp nào sau đây được xếp theo thứ tự tăng dần?", ["205; 206; 204", "1 098; 1 099; 1 100", "5 401; 5 400; 5 402", "3 200; 3 199; 3 201"], 1, "Dãy 1 098; 1 099; 1 100 gồm ba số tự nhiên liên tiếp tăng dần.")
        ],
        "part2": [
            make_essay(1, "Viết các số sau thành tổng theo các hàng:\na) 45 802\nb) 306 450", "a) 45 802 = 40 000 + 5 000 + 800 + 2\nb) 306 450 = 300 000 + 6 000 + 400 + 50", "a) 40 000 + 5 000 + 800 + 2; b) 300 000 + 6 000 + 400 + 50", 4, 1.0),
            make_essay(2, "Sắp xếp các số sau theo thứ tự từ bé đến lớn:\n524 819; 542 198; 524 189; 542 918", "So sánh các chữ số cùng hàng từ trái sang phải:\n524 189 < 524 819 < 542 198 < 542 918\nVậy thứ tự từ bé đến lớn là: 524 189; 524 819; 542 198; 542 918.", "524 189; 524 819; 542 198; 542 918", 4, 1.0),
            make_essay(3, "Làm tròn số 8 365 490:\na) Đến hàng nghìn;\nb) Đến hàng trăm nghìn.", "a) Chữ số hàng trăm là 4 (< 5), nên làm tròn đến hàng nghìn được: 8 365 000.\nb) Chữ số hàng chục nghìn là 6 (>= 5), nên làm tròn đến hàng trăm nghìn được: 8 400 000.", "a) 8 365 000; b) 8 400 000", 4, 1.0),
            make_essay(4, "Tìm số tự nhiên $x$, biết $x$ là số tròn trăm thỏa mãn: $2 450 < x < 2 750$. Hãy liệt kê tất cả các giá trị của $x$.", "Các số tròn trăm nằm giữa 2 450 và 2 750 là các số có hai chữ số tận cùng là 00.\nĐó là: 2 500; 2 600; 2 700.", "x = 2 500; 2 600; 2 700", 3, 1.0),
            make_essay(5, "Từ 4 chữ số 0; 2; 5; 8, hãy viết tất cả các số có 4 chữ số khác nhau chia hết cho cả 2 và 5.", "Để chia hết cho cả 2 và 5 thì chữ số tận cùng phải là 0.\nChữ số hàng nghìn phải khác 0, nên có 3 cách chọn (2, 5 hoặc 8).\n- Với chữ số hàng nghìn là 2: 2 580; 2 850.\n- Với chữ số hàng nghìn là 5: 5 280; 5 820.\n- Với chữ số hàng nghìn là 8: 8 250; 8 520.\nCó tất cả 6 số thỏa mãn.", "6 số: 2 580; 2 850; 5 280; 5 820; 8 250; 8 520", 5, 1.5),
            make_essay(6, "Để đánh số trang một cuốn sách dày 120 trang bằng các số tự nhiên liên tiếp từ trang 1, người ta cần dùng tất cả bao nhiêu chữ số?", "Từ trang 1 đến trang 9 có 9 trang có 1 chữ số, cần: 9 x 1 = 9 (chữ số).\nTừ trang 10 đến trang 99 có: (99 - 10 + 1) = 90 trang có 2 chữ số, cần: 90 x 2 = 180 (chữ số).\nTừ trang 100 đến trang 120 có: (120 - 100 + 1) = 21 trang có 3 chữ số, cần: 21 x 3 = 63 (chữ số).\nTổng số chữ số cần dùng là: 9 + 180 + 63 = 252 (chữ số).", "252 chữ số", 5, 1.5)
        ]
    }

    # --- Bài 1 - Đề 2 ---
    exams["th5_b1_test2"] = {
        "id": "th5_b1_test2",
        "lessonId": "th5_b1",
        "lessonNum": 1,
        "testNum": 2,
        "title": "Bài 1: Ôn tập về số tự nhiên - Đề số 2",
        "topic": "Ôn tập về số tự nhiên",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của chữ số 6 trong số 96 425 000 là:", ["60 000", "600 000", "6 000 000", "60 000 000"], 2, "Chữ số 6 ở hàng triệu nên giá trị là 6 000 000."),
            make_mc(2, "Số liền trước của số 1 000 000 là:", ["999 999", "1 000 001", "999 990", "990 000"], 0, "Số liền trước của một số tự nhiên bằng số đó trừ đi 1: 1 000 000 - 1 = 999 999."),
            make_mc(3, "Làm tròn số 327 495 đến hàng chục nghìn ta được số:", ["320 000", "330 000", "327 000", "300 000"], 1, "Chữ số hàng nghìn là 7 >= 5, nên làm tròn lên thành 330 000."),
            make_mc(4, "Trong các số: 4 825; 6 930; 7 112; 9 405, số chia hết cho 2 nhưng không chia hết cho 5 là:", ["6 930", "7 112", "4 825", "9 405"], 1, "Số 7 112 có tận cùng là 2 nên chia hết cho 2 và không chia hết cho 5."),
            make_mc(5, "Số bé nhất có bảy chữ số khác nhau là:", ["1 000 000", "1 023 456", "1 234 567", "1 023 465"], 1, "Chữ số đầu tiên là 1, các chữ số tiếp theo là nhỏ nhất khác nhau: 0, 2, 3, 4, 5, 6."),
            make_mc(6, "Số nào dưới đây có lớp triệu gồm các chữ số 4; 0; 8?", ["408 123 456", "480 912 300", "40 800 000", "4 080 000"], 0, "Số 408 123 456 có lớp triệu là 408.")
        ],
        "part2": [
            make_essay(1, "Viết số tự nhiên thích hợp vào chỗ chấm:\na) Số gồm 7 triệu, 5 trăm nghìn, 3 chục và 8 đơn vị: ...\nb) Số gồm 9 chục triệu, 4 triệu, 2 chục nghìn và 6 trăm: ...", "a) 7 500 038\nb) 94 020 600", "a) 7 500 038; b) 94 020 600", 3, 1.0),
            make_essay(2, "Sắp xếp các số sau theo thứ tự từ lớn đến bé:\n1 350 420; 1 305 999; 1 530 000; 1 350 240", "So sánh các số: 1 530 000 > 1 350 420 > 1 350 240 > 1 305 999.\nVậy thứ tự giảm dần là: 1 530 000; 1 350 420; 1 350 240; 1 305 999.", "1 530 000; 1 350 420; 1 350 240; 1 305 999", 4, 1.0),
            make_essay(3, "Làm tròn số dân của một tỉnh là 1 784 650 người:\na) Đến hàng trăm;\nb) Đến hàng triệu.", "a) Hàng chục là 5 (>= 5), làm tròn đến hàng trăm được: 1 784 700 người.\nb) Hàng trăm nghìn là 7 (>= 5), làm tròn đến hàng triệu được: 2 000 000 người.", "a) 1 784 700 người; b) 2 000 000 người", 4, 1.0),
            make_essay(4, "Tìm số tự nhiên $y$ có ba chữ số, biết $y$ chia hết cho cả 3 và 5, đồng thời chữ số hàng trăm là 4 và chữ số hàng chục là 2.", "Số cần tìm có dạng $\\overline{42a}$.\nVì $\\overline{42a}$ chia hết cho 5 nên $a = 0$ hoặc $a = 5$.\n- Nếu $a = 0$: tổng các chữ số là 4 + 2 + 0 = 6 chia hết cho 3 (chọn).\n- Nếu $a = 5$: tổng các chữ số là 4 + 2 + 5 = 11 không chia hết cho 3 (loại).\nVậy $y = 420$.", "y = 420", 4, 1.0),
            make_essay(5, "Cho các chữ số 1; 3; 6; 9. Hãy lập số lớn nhất và số bé nhất có bốn chữ số khác nhau từ 4 chữ số đã cho, rồi tính hiệu của hai số đó.", "Số lớn nhất có 4 chữ số khác nhau lập từ 4 chữ số trên là: 9 631.\nSố bé nhất có 4 chữ số khác nhau lập từ 4 chữ số trên là: 1 369.\nHiệu của hai số đó là: 9 631 - 1 369 = 8 262.", "Số lớn nhất: 9 631; Số bé nhất: 1 369; Hiệu: 8 262", 4, 1.5),
            make_essay(6, "Một bạn học sinh viết dãy các số chẵn liên tiếp: 2; 4; 6; 8; ...; 150. Hỏi bạn đó đã viết tất cả bao nhiêu số và cần dùng bao nhiêu chữ số để viết dãy đó?", "Số lượng các số chẵn trong dãy là: (150 - 2) : 2 + 1 = 75 (số).\n- Từ 2 đến 8 có 4 số có 1 chữ số, cần: 4 x 1 = 4 (chữ số).\n- Từ 10 đến 98 có: (98 - 10) : 2 + 1 = 45 số có 2 chữ số, cần: 45 x 2 = 90 (chữ số).\n- Từ 100 đến 150 có: (150 - 100) : 2 + 1 = 26 số có 3 chữ số, cần: 26 x 3 = 78 (chữ số).\nTổng số chữ số cần dùng là: 4 + 90 + 78 = 172 (chữ số).", "75 số chẵn; 172 chữ số", 5, 1.5)
        ]
    }

    # --- Bài 1 - Đề 3 ---
    exams["th5_b1_test3"] = {
        "id": "th5_b1_test3",
        "lessonId": "th5_b1",
        "lessonNum": 1,
        "testNum": 3,
        "title": "Bài 1: Ôn tập về số tự nhiên - Đề số 3",
        "topic": "Ôn tập về số tự nhiên",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số 50 306 000 đọc là:", [
                "Năm mươi triệu ba trăm linh sáu nghìn",
                "Năm mươi triệu ba mươi sáu nghìn",
                "Năm triệu ba trăm linh sáu nghìn",
                "Năm mươi triệu ba trăm sáu mươi nghìn"
            ], 0, "Đọc số theo từng lớp: lớp triệu là 50, lớp nghìn là 306, lớp đơn vị là 000."),
            make_mc(2, "Số liền sau của số 49 999 999 là:", ["50 000 000", "49 999 998", "50 000 001", "49 999 900"], 0, "Số liền sau bằng số đã cho cộng thêm 1: 49 999 999 + 1 = 50 000 000."),
            make_mc(3, "Làm tròn số 9 450 200 đến hàng triệu ta được:", ["9 000 000", "10 000 000", "9 500 000", "9 400 000"], 0, "Chữ số hàng trăm nghìn là 4 (< 5), nên làm tròn giữ nguyên phần triệu: 9 000 000."),
            make_mc(4, "Trong các số sau, số nào chia hết cho 9?", ["123 456", "345 678", "214 560", "782 109"], 2, "Tổng các chữ số của 214 560 là 2 + 1 + 4 + 5 + 6 + 0 = 18 chia hết cho 9."),
            make_mc(5, "Số các số tự nhiên có 3 chữ số là:", ["900", "899", "999", "1 000"], 0, "Số các số có 3 chữ số là: 999 - 100 + 1 = 900 số."),
            make_mc(6, "Chữ số thích hợp điền vào dấu * để số $\\overline{57*}$ chia hết cho cả 2 và 3 là:", ["0", "2", "6", "8"], 2, "Để chia hết cho 2, * là số chẵn. 5 + 7 + 6 = 18 chia hết cho 3. Do đó chọn 6.")
        ],
        "part2": [
            make_essay(1, "Viết số tự nhiên gồm:\na) 6 trăm nghìn, 8 nghìn, 5 trăm và 4 đơn vị.\nb) 12 triệu, 45 nghìn và 7 chục.", "a) 608 504\nb) 12 045 070", "a) 608 504; b) 12 045 070", 3, 1.0),
            make_essay(2, "Điền dấu thích hợp ($>, <, =$) vào chỗ chấm:\na) 4 521 800 ... 4 519 999\nb) 8 000 000 + 70 000 + 5 ... 8 070 005", "a) So sánh hàng chục nghìn: 2 > 1 => 4 521 800 > 4 519 999.\nb) 8 000 000 + 70 000 + 5 = 8 070 005 => 8 070 005 = 8 070 005.", "a) >; b) =", 4, 1.0),
            make_essay(3, "Khoảng cách từ Trái Đất đến Mặt Trăng xấp xỉ 384 400 km. Hãy làm tròn số này:\na) Đến hàng chục nghìn;\nb) Đến hàng trăm nghìn.", "a) Chữ số hàng nghìn là 4 (< 5), làm tròn đến hàng chục nghìn ta được: 380 000 km.\nb) Chữ số hàng chục nghìn là 8 (>= 5), làm tròn đến hàng trăm nghìn ta được: 400 000 km.", "a) 380 000 km; b) 400 000 km", 4, 1.0),
            make_essay(4, "Tìm số tự nhiên lẻ có hai chữ số, biết tổng hai chữ số của số đó bằng 12 và chữ số hàng chục lớn hơn chữ số hàng đơn vị.", "Gọi số cần tìm là $\\overline{ab}$ ($a, b \\in \\mathbb{N}, 1 \\le a \\le 9, 0 \\le b \\le 9$).\nVì số đó là số lẻ nên $b \\in \\{1; 3; 5; 7; 9\\}$.\nTổng $a + b = 12$ và $a > b$:\n- Nếu $b = 1$ thì $a = 11$ (loại vì $a \\le 9$).\n- Nếu $b = 3$ thì $a = 9$ ($9 > 3$, chọn) => số 93.\n- Nếu $b = 5$ thì $a = 7$ ($7 > 5$, chọn) => số 75.\n- Nếu $b = 7$ thì $a = 5$ ($5 < 7$, loại).\nVậy có hai số thỏa mãn là 93 và 75.", "93 và 75", 5, 1.0),
            make_essay(5, "Một cửa hàng có 3 kho thóc. Kho thứ nhất chứa 125 400 kg thóc, kho thứ hai chứa ít hơn kho thứ nhất 18 200 kg thóc, kho thứ ba chứa nhiều hơn kho thứ hai 24 500 kg thóc. Hỏi cả ba kho chứa tất cả bao nhiêu ki-lô-gam thóc?", "Số thóc ở kho thứ hai là: 125 400 - 18 200 = 107 200 (kg).\nSố thóc ở kho thứ ba là: 107 200 + 24 500 = 131 700 (kg).\nCả ba kho chứa số ki-lô-gam thóc là:\n125 400 + 107 200 + 131 700 = 364 300 (kg).", "364 300 kg thóc", 5, 1.5),
            make_essay(6, "Tìm một số tự nhiên có 3 chữ số, biết rằng nếu viết thêm chữ số 2 vào bên trái số đó thì được số mới gấp 9 lần số ban đầu.", "Gọi số cần tìm là $\\overline{abc}$ ($a > 0$).\nKhi viết thêm chữ số 2 vào bên trái ta được số $\\overline{2abc} = 2000 + \\overline{abc}$.\nTheo đề bài: $2000 + \\overline{abc} = 9 \\times \\overline{abc}$.\nSuy ra: $8 \\times \\overline{abc} = 2000$.\nDo đó: $\\overline{abc} = 2000 : 8 = 250$.\nVậy số cần tìm là 250.", "250", 5, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 2: ÔN TẬP CÁC PHÉP TÍNH VỚI SỐ TỰ NHIÊN
    # =========================================================================
    # --- Bài 2 - Đề 1 ---
    exams["th5_b2_test1"] = {
        "id": "th5_b2_test1",
        "lessonId": "th5_b2",
        "lessonNum": 2,
        "testNum": 1,
        "title": "Bài 2: Ôn tập các phép tính với số tự nhiên - Đề số 1",
        "topic": "Ôn tập các phép tính với số tự nhiên",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $45 820 + 23 415$ là:", ["68 235", "69 235", "69 135", "69 335"], 1, "45 820 + 23 415 = 69 235."),
            make_mc(2, "Kết quả của phép trừ $100 000 - 45 670$ là:", ["54 330", "55 330", "54 430", "64 330"], 0, "100 000 - 45 670 = 54 330."),
            make_mc(3, "Giá trị của biểu thức $250 \\times 40$ là:", ["1 000", "10 000", "100 000", "25 000"], 1, "250 x 40 = 10 000."),
            make_mc(4, "Thương và số dư của phép chia $4 856 : 24$ lần lượt là:", ["Thương 202, dư 8", "Thương 202, dư 12", "Thương 22, dư 8", "Thương 201, dư 32"], 0, "4 856 = 24 x 202 + 8."),
            make_mc(5, "Biểu thức $a \\times (b + c)$ bằng biểu thức nào sau đây?", ["$a \\times b + c$", "$a \\times b + a \\times c$", "$a + b \\times c$", "$a \\times b \\times c$"], 1, "Tính chất phân phối của phép nhân đối với phép cộng."),
            make_mc(6, "Trung bình cộng của ba số 34; 46 và 55 là:", ["40", "45", "50", "42"], 1, "Tổng ba số: 34 + 46 + 55 = 135. Trung bình cộng: 135 : 3 = 45.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $328 \\times 45$\nb) $15 792 : 36$", "a) $328 \\times 45 = 14 760$\nb) $15 792 : 36 = 438$ (chia hết)", "a) 14 760; b) 438", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức bằng cách thuận tiện nhất:\na) $45 \\times 128 - 45 \\times 28$\nb) $25 \\times 48 \\times 4$", "a) $45 \\times (128 - 28) = 45 \\times 100 = 4 500$.\nb) $(25 \\times 4) \\times 48 = 100 \\times 48 = 4 800$.", "a) 4 500; b) 4 800", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\na) $x + 3 540 = 12 800$\nb) $x : 15 = 204$ (dư 8)", "a) $x = 12 800 - 3 540 = 9 260$.\nb) $x = 204 \\times 15 + 8 = 3 060 + 8 = 3 068$.", "a) x = 9 260; b) x = 3 068", 4, 1.0),
            make_essay(4, "Tính giá trị của biểu thức $P = 150 + a \\times b - c$ khi $a = 25, b = 14, c = 80$.", "Thay số vào biểu thức ta có:\n$P = 150 + 25 \\times 14 - 80$\n$P = 150 + 350 - 80$\n$P = 500 - 80 = 420$.", "P = 420", 3, 1.0),
            make_essay(5, "Một đội công nhân làm đường, tuần thứ nhất làm được 1 450 m đường, tuần thứ hai làm được nhiều hơn tuần thứ nhất 260 m đường, tuần thứ ba làm được bằng trung bình cộng của hai tuần đầu. Hỏi cả ba tuần đội đó làm được bao nhiêu mét đường?", "Tuần thứ hai đội làm được: 1 450 + 260 = 1 710 (m).\nTuần thứ ba đội làm được: (1 450 + 1 710) : 2 = 1 580 (m).\nCả ba tuần đội làm được tất cả:\n1 450 + 1 710 + 1 580 = 4 740 (m).", "4 740 m đường", 5, 1.5),
            make_essay(6, "Một mảnh vườn hình chữ nhật có chu vi là 180 m. Nếu tăng chiều rộng thêm 10 m và giảm chiều dài đi 10 m thì mảnh vườn trở thành hình vuông. Tính diện tích mảnh vườn hình chữ nhật ban đầu.", "Nửa chu vi mảnh vườn là: 180 : 2 = 90 (m).\nChiều dài hơn chiều rộng số mét là: 10 + 10 = 20 (m).\nChiều dài ban đầu là: (90 + 20) : 2 = 55 (m).\nChiều rộng ban đầu là: 90 - 55 = 35 (m).\nDiện tích mảnh vườn ban đầu là: 55 x 35 = 1 925 (m$^2$).", "1 925 m$^2$", 5, 1.5)
        ]
    }

    # --- Bài 2 - Đề 2 ---
    exams["th5_b2_test2"] = {
        "id": "th5_b2_test2",
        "lessonId": "th5_b2",
        "lessonNum": 2,
        "testNum": 2,
        "title": "Bài 2: Ôn tập các phép tính với số tự nhiên - Đề số 2",
        "topic": "Ôn tập các phép tính với số tự nhiên",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $324 \\times 101$ là:", ["32 724", "32 400", "32 624", "32 744"], 0, "324 x 101 = 324 x (100 + 1) = 32 400 + 324 = 32 724."),
            make_mc(2, "Phép tính nào sau đây có kết quả lớn nhất?", ["$1 200 + 3 800$", "$150 \\times 30$", "$12 000 : 3$", "$10 000 - 4 500$"], 3, "A = 5 000; B = 4 500; C = 4 000; D = 5 500. Vậy D lớn nhất."),
            make_mc(3, "Một số chia cho 45 được thương là 12 và số dư là số dư lớn nhất có thể. Số đó là:", ["540", "584", "585", "580"], 1, "Số dư lớn nhất có thể khi chia cho 45 là 44. Số cần tìm: 12 x 45 + 44 = 540 + 44 = 584."),
            make_mc(4, "Tìm $x$, biết: $x \\times 25 = 1 500$. Giá trị của $x$ là:", ["60", "50", "40", "70"], 0, "x = 1 500 : 25 = 60."),
            make_mc(5, "Nếu $m = 40, n = 5$ thì giá trị biểu thức $m + n \\times 4$ là:", ["180", "60", "160", "70"], 1, "Thực hiện nhân trước: 40 + 5 x 4 = 40 + 20 = 60."),
            make_mc(6, "Trung bình cộng của bốn số chẵn liên tiếp bắt đầu từ số 10 là:", ["12", "13", "14", "15"], 1, "Bốn số chẵn: 10; 12; 14; 16. Tổng: 52. Trung bình cộng: 52 : 4 = 13.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $416 \\times 208$\nb) $31 620 : 62$", "a) $416 \\times 208 = 86 528$\nb) $31 620 : 62 = 510$", "a) 86 528; b) 510", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức bằng cách tính thuận tiện:\na) $137 \\times 89 + 137 \\times 11$\nb) $125 \\times 32 \\times 7$", "a) $137 \\times (89 + 11) = 137 \\times 100 = 13 700$.\nb) $(125 \\times 8) \\times 4 \\times 7 = 1 000 \\times 28 = 28 000$.", "a) 13 700; b) 28 000", 4, 1.0),
            make_essay(3, "Tìm số tự nhiên $y$, biết:\na) $y - 4 250 = 3 890 + 1 110$\nb) $450 : y = 18$", "a) $y - 4 250 = 5 000 \\Rightarrow y = 5 000 + 4 250 = 9 250$.\nb) $y = 450 : 18 = 25$.", "a) y = 9 250; b) y = 25", 4, 1.0),
            make_essay(4, "Một trang trại nuôi 1 200 con gà và vịt. Trong đó số gà nhiều hơn số vịt là 240 con. Hỏi trang trại đó nuôi bao nhiêu con gà và bao nhiêu con vịt?", "Số con gà trang trại nuôi là: (1 200 + 240) : 2 = 720 (con).\nSố con vịt trang trại nuôi là: 1 200 - 720 = 480 (con).", "Gà: 720 con; Vịt: 480 con", 4, 1.0),
            make_essay(5, "Một chuyến xe tải chở 8 chuyến hàng, mỗi chuyến chở được 45 bao ngô, mỗi bao cân nặng 50 kg. Hỏi xe tải đó đã chở được tất cả bao nhiêu tấn ngô?", "Tổng số bao ngô chở được là: 8 x 45 = 360 (bao).\nKhối lượng ngô chở được là: 360 x 50 = 18 000 (kg).\nĐổi 18 000 kg = 18 tấn.", "18 tấn ngô", 4, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$S = 12 + 15 + 18 + 21 + \\dots + 99$", "Dãy số cách đều có khoảng cách là 3 đơn vị.\nSố số hạng của dãy là: (99 - 12) : 3 + 1 = 30 (số hạng).\nTổng của dãy số là: (12 + 99) x 30 : 2 = 111 x 15 = 1 665.", "1 665", 5, 1.5)
        ]
    }

    # --- Bài 2 - Đề 3 ---
    exams["th5_b2_test3"] = {
        "id": "th5_b2_test3",
        "lessonId": "th5_b2",
        "lessonNum": 2,
        "testNum": 3,
        "title": "Bài 2: Ôn tập các phép tính với số tự nhiên - Đề số 3",
        "topic": "Ôn tập các phép tính với số tự nhiên",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của biểu thức $150 - 50 : 5 + 10$ là:", ["30", "150", "130", "120"], 1, "Thực hiện phép chia trước: 150 - 10 + 10 = 150."),
            make_mc(2, "Tích của hai số là 1 260. Nếu một thừa số gấp lên 3 lần và thừa số kia giữ nguyên thì tích mới là:", ["420", "3 780", "1 263", "2 520"], 1, "Khi gấp 1 thừa số lên 3 lần thì tích mới gấp lên 3 lần: 1 260 x 3 = 3 780."),
            make_mc(3, "Thương của phép chia $27 500 : 250$ là:", ["110", "11", "101", "120"], 0, "27 500 : 250 = 110."),
            make_mc(4, "Biết tổng của hai số là 84 và hiệu của chúng là 16. Số bé là:", ["34", "50", "68", "38"], 0, "Số bé = (Tổng - Hiệu) : 2 = (84 - 16) : 2 = 34."),
            make_mc(5, "Khi nhân một số tự nhiên với 100, ta chỉ việc:", [
                "Viết thêm một chữ số 0 vào bên phải số đó",
                "Viết thêm hai chữ số 0 vào bên phải số đó",
                "Viết thêm ba chữ số 0 vào bên phải số đó",
                "Nhân số đó với 10 rồi cộng thêm 100"
            ], 1, "Nhân với 100 thì viết thêm hai chữ số 0 vào bên phải số đó."),
            make_mc(6, "Một trường tiểu học có 4 khối lớp, mỗi khối có 5 lớp học, mỗi lớp có 32 học sinh. Số học sinh toàn trường là:", ["640", "600", "580", "720"], 0, "Tổng số học sinh: 4 x 5 x 32 = 20 x 32 = 640 học sinh.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $2 458 \\times 36$\nb) $48 576 : 56$", "a) $2 458 \\times 36 = 88 488$\nb) $48 576 : 56 = 867$ (dư 24)", "a) 88 488; b) 867 (dư 24)", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức bằng cách hợp lí:\na) $246 \\times 53 + 246 \\times 46 + 246$\nb) $(100 - 25 \\times 4) \\times (1 + 2 + 3 + \\dots + 100)$", "a) $246 \\times (53 + 46 + 1) = 246 \\times 100 = 24 600$.\nb) Vì $100 - 25 \\times 4 = 100 - 100 = 0$, nên tích bằng 0.", "a) 24 600; b) 0", 4, 1.0),
            make_essay(3, "Tìm $x$, biết: $(x - 125) : 32 = 45$.", "$x - 125 = 45 \\times 32$\n$x - 125 = 1 440$\n$x = 1 440 + 125 = 1 565$.", "x = 1 565", 3, 1.0),
            make_essay(4, "Ba bạn An, Bình, Cường sưu tầm được tất cả 165 con tem. Số tem của An bằng trung bình cộng số tem của Bình và Cường. Hỏi bạn An sưu tầm được bao nhiêu con tem?", "Tổng số tem của ba bạn là 165.\nVì số tem của An bằng trung bình cộng của Bình và Cường, nên tổng số tem của Bình và Cường gấp 2 lần số tem của An.\nCoi số tem của An là 1 phần thì số tem của Bình và Cường là 2 phần.\nTổng số phần bằng nhau: 1 + 2 = 3 (phần).\nSố tem của An là: 165 : 3 = 55 (con tem).", "55 con tem", 4, 1.0),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chu vi 240 m, chiều dài hơn chiều rộng 20 m. Người ta cấy lúa trên thửa ruộng đó, cứ 100 m$^2$ thu hoạch được 65 kg thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Nửa chu vi thửa ruộng: 240 : 2 = 120 (m).\nChiều dài thửa ruộng: (120 + 20) : 2 = 70 (m).\nChiều rộng thửa ruộng: 120 - 70 = 50 (m).\nDiện tích thửa ruộng: 70 x 50 = 3 500 (m$^2$).\nSố ki-lô-gam thóc thu hoạch được: 3 500 : 100 x 65 = 2 275 (kg).\nĐổi 2 275 kg = 22,75 tạ thóc (hoặc 22 tạ 75 kg).", "22,75 tạ thóc (hoặc 2 275 kg)", 5, 1.5),
            make_essay(6, "Khi nhân một số tự nhiên với 24, một bạn học sinh đã vô ý đặt các tích riêng thẳng cột như trong phép cộng nên tìm ra kết quả là 846. Em hãy tìm tích đúng của phép nhân đó.", "Khi đặt các tích riêng thẳng cột, thực chất học sinh đó đã nhân số tự nhiên với tổng các chữ số của 24 là: 2 + 4 = 6.\nSố tự nhiên đem nhân là: 846 : 6 = 141.\nTích đúng của phép nhân là: 141 x 24 = 3 384.", "3 384", 5, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 3: ÔN TẬP PHÂN SỐ
    # =========================================================================
    # --- Bài 3 - Đề 1 ---
    exams["th5_b3_test1"] = {
        "id": "th5_b3_test1",
        "lessonId": "th5_b3",
        "lessonNum": 3,
        "testNum": 1,
        "title": "Bài 3: Ôn tập phân số - Đề số 1",
        "topic": "Ôn tập phân số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Rút gọn phân số $\\frac{24}{36}$ về phân số tối giản ta được:", ["$\\frac{12}{18}$", "$\\frac{6}{9}$", "$\\frac{2}{3}$", "$\\frac{4}{6}$"], 2, "Chia cả tử và mẫu cho 12 ta được 2/3."),
            make_mc(2, "Phân số nào dưới đây bằng phân số $\\frac{3}{5}$?", ["$\\frac{9}{20}$", "$\\frac{12}{20}$", "$\\frac{15}{30}$", "$\\frac{6}{15}$"], 1, "Nhân cả tử và mẫu với 4: (3x4)/(5x4) = 12/20."),
            make_mc(3, "Quy đồng mẫu số hai phân số $\\frac{5}{6}$ và $\\frac{7}{9}$ với mẫu số chung nhỏ nhất là:", ["54", "36", "18", "27"], 2, "Mẫu số chung nhỏ nhất của 6 và 9 là 18."),
            make_mc(4, "Trong các phân số $\\frac{4}{5}; \\frac{7}{6}; \\frac{9}{9}; \\frac{3}{8}$, phân số lớn hơn 1 là:", ["$\\frac{4}{5}$", "$\\frac{7}{6}$", "$\\frac{9}{9}$", "$\\frac{3}{8}$"], 1, "Phân số có tử số lớn hơn mẫu số (7 > 6) thì lớn hơn 1."),
            make_mc(5, "Điền dấu thích hợp: $\\frac{5}{8} \\dots \\frac{5}{12}$:", [">", "<", "=", "Không so sánh được"], 0, "Hai phân số có cùng tử số dương, phân số nào có mẫu số bé hơn thì phân số đó lớn hơn: 8 < 12 nên 5/8 > 5/12."),
            make_mc(6, "Phân số tối giản trong các phân số sau là:", ["$\\frac{14}{21}$", "$\\frac{15}{25}$", "$\\frac{17}{20}$", "$\\frac{9}{33}$"], 2, "17 và 20 không cùng chia hết cho số tự nhiên nào lớn hơn 1.")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) $\\frac{45}{60}$\nb) $\\frac{36}{84}$", "a) $\\frac{45}{60} = \\frac{45 : 15}{60 : 15} = \\frac{3}{4}$\nb) $\\frac{36}{84} = \\frac{36 : 12}{84 : 12} = \\frac{3}{7}$", "a) 3/4; b) 3/7", 3, 1.0),
            make_essay(2, "Quy đồng mẫu số các phân số sau:\na) $\\frac{3}{8}$ và $\\frac{5}{12}$\nb) $\\frac{2}{3}; \\frac{3}{4}$ và $\\frac{5}{6}$", "a) MSC = 24. $\\frac{3}{8} = \\frac{9}{24}; \\frac{5}{12} = \\frac{10}{24}$.\nb) MSC = 12. $\\frac{2}{3} = \\frac{8}{12}; \\frac{3}{4} = \\frac{9}{12}; \\frac{5}{6} = \\frac{10}{12}$.", "a) 9/24 và 10/24; b) 8/12, 9/12 và 10/12", 4, 1.0),
            make_essay(3, "So sánh các phân số sau bằng cách hợp lí nhất:\na) $\\frac{13}{15}$ và $\\frac{14}{15}$\nb) $\\frac{2023}{2024}$ và $\\frac{2024}{2025}$", "a) Cùng mẫu số: 13 < 14 nên $\\frac{13}{15} < \\frac{14}{15}$.\nb) So sánh phần bù với 1: $1 - \\frac{2023}{2024} = \\frac{1}{2024}$; $1 - \\frac{2024}{2025} = \\frac{1}{2025}$.\nVì $\\frac{1}{2024} > \\frac{1}{2025}$ nên $\\frac{2023}{2024} < \\frac{2024}{2025}$.", "a) 13/15 < 14/15; b) 2023/2024 < 2024/2025", 4, 1.0),
            make_essay(4, "Sắp xếp các phân số sau theo thứ tự từ bé đến lớn: $\\frac{1}{2}; \\frac{3}{5}; \\frac{2}{3}; \\frac{4}{15}$.", "Quy đồng mẫu số chung là 30:\n$\\frac{1}{2} = \\frac{15}{30}; \\frac{3}{5} = \\frac{18}{30}; \\frac{2}{3} = \\frac{20}{30}; \\frac{4}{15} = \\frac{8}{30}$.\nVì $\\frac{8}{30} < \\frac{15}{30} < \\frac{18}{30} < \\frac{20}{30}$ nên: $\\frac{4}{15} < \\frac{1}{2} < \\frac{3}{5} < \\frac{2}{3}$.", "4/15; 1/2; 3/5; 2/3", 4, 1.0),
            make_essay(5, "Tìm số tự nhiên $x$, biết: $\\frac{x}{18} = \\frac{20}{24}$.", "Rút gọn phân số $\\frac{20}{24} = \\frac{20 : 4}{24 : 4} = \\frac{5}{6}$.\nTa có $\\frac{x}{18} = \\frac{5}{6} = \\frac{5 \\times 3}{6 \\times 3} = \\frac{15}{18}$.\nVậy $x = 15$.", "x = 15", 3, 1.5),
            make_essay(6, "Cho phân số $\\frac{17}{28}$. Hỏi phải cùng thêm vào cả tử số và mẫu số của phân số đó bao nhiêu đơn vị để được phân số mới bằng phân số $\\frac{2}{3}$?", "Khi cùng thêm vào tử số và mẫu số cùng một số đơn vị thì hiệu giữa mẫu số và tử số không đổi.\nHiệu mẫu số và tử số là: 28 - 17 = 11.\nỞ phân số mới bằng 2/3, coi tử số là 2 phần thì mẫu số là 3 phần.\nHiệu số phần bằng nhau: 3 - 2 = 1 (phần), tương ứng với 11 đơn vị.\nTử số mới là: 11 x 2 = 22.\nSố đơn vị cần thêm vào là: 22 - 17 = 5.", "5 đơn vị", 5, 1.5)
        ]
    }

    # --- Bài 3 - Đề 2 ---
    exams["th5_b3_test2"] = {
        "id": "th5_b3_test2",
        "lessonId": "th5_b3",
        "lessonNum": 3,
        "testNum": 2,
        "title": "Bài 3: Ôn tập phân số - Đề số 2",
        "topic": "Ôn tập phân số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số nào sau đây bằng phân số $\\frac{4}{7}$?", ["$\\frac{8}{21}$", "$\\frac{16}{28}$", "$\\frac{12}{28}$", "$\\frac{20}{42}$"], 1, "Cùng nhân cả tử và mẫu với 4: (4x4)/(7x4) = 16/28."),
            make_mc(2, "Trong các phân số $\\frac{5}{8}; \\frac{7}{9}; \\frac{3}{4}; \\frac{11}{12}$, phân số nào có giá trị lớn nhất?", ["$\\frac{5}{8}$", "$\\frac{7}{9}$", "$\\frac{3}{4}$", "$\\frac{11}{12}$"], 3, "So sánh phần bù tới 1: 1 - 11/12 = 1/12 nhỏ nhất, nên 11/12 lớn nhất."),
            make_mc(3, "Rút gọn phân số $\\frac{48}{72}$ ta được phân số tối giản là:", ["$\\frac{4}{6}$", "$\\frac{2}{3}$", "$\\frac{6}{9}$", "$\\frac{8}{12}$"], 1, "48/72 = (48:24)/(72:24) = 2/3."),
            make_mc(4, "Mẫu số chung nhỏ nhất của hai phân số $\\frac{7}{15}$ và $\\frac{4}{25}$ là:", ["150", "75", "50", "100"], 1, "BCNN(15, 25) = 75."),
            make_mc(5, "Số thích hợp điền vào ô trống để $\\frac{9}{12} = \\frac{\\square}{4}$ là:", ["2", "3", "4", "6"], 1, "12 : 3 = 4, do đó 9 : 3 = 3."),
            make_mc(6, "Có bao nhiêu phân số nhỏ hơn 1 mà tích của tử số và mẫu số bằng 24 (tử số và mẫu số là các số tự nhiên khác 0)?", ["2", "3", "4", "5"], 2, "Các cặp (tử, mẫu) với tử < mẫu và tích bằng 24 là: (1; 24), (2; 12), (3; 8), (4; 6). Có 4 phân số: 1/24; 2/12; 3/8; 4/6.")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) $\\frac{35}{56}$\nb) $\\frac{75}{100}$", "a) $\\frac{35}{56} = \\frac{35 : 7}{56 : 7} = \\frac{5}{8}$\nb) $\\frac{75}{100} = \\frac{75 : 25}{100 : 25} = \\frac{3}{4}$", "a) 5/8; b) 3/4", 3, 1.0),
            make_essay(2, "Quy đồng mẫu số hai phân số $\\frac{7}{18}$ và $\\frac{11}{24}$.", "Mẫu số chung nhỏ nhất của 18 và 24 là 72.\n$72 : 18 = 4; 72 : 24 = 3$.\n$\\frac{7}{18} = \\frac{7 \\times 4}{18 \\times 4} = \\frac{28}{72}$;\n$\\frac{11}{24} = \\frac{11 \\times 3}{24 \\times 3} = \\frac{33}{72}$.", "28/72 và 33/72", 4, 1.0),
            make_essay(3, "So sánh các phân số sau:\na) $\\frac{17}{20}$ và $\\frac{19}{22}$\nb) $\\frac{15}{7}$ và $\\frac{17}{9}$", "a) So sánh phần bù với 1: $1 - \\frac{17}{20} = \\frac{3}{20}$; $1 - \\frac{19}{22} = \\frac{3}{22}$.\nVì $\\frac{3}{20} > \\frac{3}{22}$ nên $\\frac{17}{20} < \\frac{19}{22}$.\nb) So sánh phần hơn với 1: $\\frac{15}{7} = 1 + \\frac{8}{7} = 2 + \\frac{1}{7}$; $\\frac{17}{9} = 1 + \\frac{8}{9}$. Rõ ràng $\\frac{15}{7} > 2 > \\frac{17}{9}$.", "a) 17/20 < 19/22; b) 15/7 > 17/9", 4, 1.0),
            make_essay(4, "Viết các phân số $\\frac{2}{3}; \\frac{5}{6}; \\frac{7}{12}; \\frac{3}{4}$ theo thứ tự từ lớn đến bé.", "Quy đồng mẫu số chung là 12:\n$\\frac{2}{3} = \\frac{8}{12}; \\frac{5}{6} = \\frac{10}{12}; \\frac{7}{12}; \\frac{3}{4} = \\frac{9}{12}$.\nVì $\\frac{10}{12} > \\frac{9}{12} > \\frac{8}{12} > \\frac{7}{12}$ nên thứ tự giảm dần là: $\\frac{5}{6}; \\frac{3}{4}; \\frac{2}{3}; \\frac{7}{12}$.", "5/6; 3/4; 2/3; 7/12", 4, 1.0),
            make_essay(5, "Tìm số tự nhiên $a$ biết: $\\frac{15}{a} = \\frac{45}{75}$.", "Rút gọn phân số $\\frac{45}{75} = \\frac{45 : 15}{75 : 15} = \\frac{3}{5}$.\nTa có: $\\frac{15}{a} = \\frac{3}{5} = \\frac{3 \\times 5}{5 \\times 5} = \\frac{15}{25}$.\nSuy ra $a = 25$.", "a = 25", 3, 1.5),
            make_essay(6, "Cho phân số $\\frac{29}{43}$. Hỏi cùng phải bớt ở cả tử số và mẫu số của phân số đó đi bao nhiêu đơn vị để được phân số mới bằng phân số $\\frac{1}{2}$?", "Khi cùng bớt ở cả tử số và mẫu số đi cùng một số đơn vị thì hiệu giữa mẫu số và tử số không thay đổi.\nHiệu giữa mẫu số và tử số là: 43 - 29 = 14.\nỞ phân số mới bằng 1/2, hiệu số phần bằng nhau: 2 - 1 = 1 (phần), tương ứng với 14.\nTử số mới là: 14 x 1 = 14.\nSố đơn vị cần bớt đi là: 29 - 14 = 15.", "15 đơn vị", 5, 1.5)
        ]
    }

    # --- Bài 3 - Đề 3 ---
    exams["th5_b3_test3"] = {
        "id": "th5_b3_test3",
        "lessonId": "th5_b3",
        "lessonNum": 3,
        "testNum": 3,
        "title": "Bài 3: Ôn tập phân số - Đề số 3",
        "topic": "Ôn tập phân số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số nào sau đây là phân số tối giản?", ["$\\frac{21}{28}$", "$\\frac{18}{27}$", "$\\frac{13}{39}$", "$\\frac{11}{23}$"], 3, "11 và 23 là hai số nguyên tố cùng nhau, không rút gọn được nữa."),
            make_mc(2, "Tìm chữ số $x$ để $\\frac{25}{x} = \\frac{5}{7}$. Giá trị của $x$ là:", ["30", "35", "40", "28"], 1, "x = 25 x 7 : 5 = 35."),
            make_mc(3, "So sánh hai phân số $\\frac{7}{11}$ và $\\frac{7}{9}$:", ["$\\frac{7}{11} > \\frac{7}{9}$", "$\\frac{7}{11} < \\frac{7}{9}$", "$\\frac{7}{11} = \\frac{7}{9}$", "Không so sánh được"], 1, "Cùng tử số 7, mẫu số 11 > 9 nên 7/11 < 7/9."),
            make_mc(4, "Phân số nào dưới đây bằng phân số 1?", ["$\\frac{8}{9}$", "$\\frac{15}{15}$", "$\\frac{12}{10}$", "$\\frac{0}{7}$"], 1, "Phân số có tử số bằng mẫu số (khác 0) thì bằng 1."),
            make_mc(5, "Mẫu số chung của các phân số $\\frac{1}{2}; \\frac{2}{3}; \\frac{3}{4}$ có thể là:", ["12", "8", "10", "6"], 0, "12 chia hết cho cả 2, 3 và 4."),
            make_mc(6, "Có bao nhiêu phân số có tổng của tử số và mẫu số bằng 10 (tử số và mẫu số là các số tự nhiên, mẫu số khác 0)?", ["9", "10", "8", "7"], 0, "Tử số nhận các giá trị từ 0 đến 9 (10 giá trị), tương ứng mẫu số từ 10 xuống 1 (khác 0). Có 10 phân số: 0/10; 1/9; 2/8; 3/7; 4/6; 5/5; 6/4; 7/3; 8/2; 9/1.")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau:\na) $\\frac{54}{90}$\nb) $\\frac{48}{108}$", "a) $\\frac{54}{90} = \\frac{54 : 18}{90 : 18} = \\frac{3}{5}$\nb) $\\frac{48}{108} = \\frac{48 : 12}{108 : 12} = \\frac{4}{9}$", "a) 3/5; b) 4/9", 3, 1.0),
            make_essay(2, "Quy đồng mẫu số các phân số: $\\frac{5}{12}; \\frac{7}{15}$ và $\\frac{3}{20}$.", "Mẫu số chung nhỏ nhất của 12, 15, 20 là 60.\n$60 : 12 = 5; 60 : 15 = 4; 60 : 20 = 3$.\n$\\frac{5}{12} = \\frac{25}{60}$; $\\frac{7}{15} = \\frac{28}{60}$; $\\frac{3}{20} = \\frac{9}{60}$.", "25/60; 28/60 và 9/60", 4, 1.0),
            make_essay(3, "So sánh hai phân số bằng cách thuận tiện nhất:\na) $\\frac{101}{100}$ và $\\frac{201}{200}$\nb) $\\frac{13}{27}$ và $\\frac{27}{53}$", "a) So sánh phần hơn với 1: $\\frac{101}{100} - 1 = \\frac{1}{100}$; $\\frac{201}{200} - 1 = \\frac{1}{200}$. Vì $\\frac{1}{100} > \\frac{1}{200}$ nên $\\frac{101}{100} > \\frac{201}{200}$.\nb) So sánh qua phân số trung gian $\\frac{1}{2}$:\n$\\frac{13}{27} < \\frac{13,5}{27} = \\frac{1}{2}$; $\\frac{27}{53} > \\frac{26,5}{53} = \\frac{1}{2}$. Do đó $\\frac{13}{27} < \\frac{27}{53}$.", "a) 101/100 > 201/200; b) 13/27 < 27/53", 4, 1.0),
            make_essay(4, "Tìm phân số có mẫu số là 9, biết phân số đó lớn hơn $\\frac{4}{7}$ và nhỏ hơn $\\frac{5}{7}$.", "Gọi phân số cần tìm là $\\frac{a}{9}$ ($a$ là số tự nhiên).\nTheo đề bài: $\\frac{4}{7} < \\frac{a}{9} < \\frac{5}{7}$.\nQuy đồng mẫu số chung là 63:\n$\\frac{36}{63} < \\frac{7 \\times a}{63} < \\frac{45}{63}$.\nSuy ra: $36 < 7 \\times a < 45$.\nVì $7 \\times 5 = 35$ và $7 \\times 6 = 42$ nên chỉ có $a = 6$ thỏa mãn (vì $36 < 42 < 45$).\nVậy phân số cần tìm là $\\frac{6}{9} = \\frac{2}{3}$.", "6/9 (hay 2/3)", 5, 1.0),
            make_essay(5, "Tìm một phân số bằng phân số $\\frac{3}{5}$, biết rằng nếu lấy tử số cộng với mẫu số của phân số đó thì được tổng bằng 96.", "Coi tử số là 3 phần thì mẫu số là 5 phần.\nTổng số phần bằng nhau: 3 + 5 = 8 (phần).\nGiá trị một phần là: 96 : 8 = 12.\nTử số là: 12 x 3 = 36.\nMẫu số là: 12 x 5 = 60.\nPhân số cần tìm là $\\frac{36}{60}$.", "36/60", 4, 1.5),
            make_essay(6, "Cho phân số $\\frac{15}{39}$. Tìm số tự nhiên $m$ sao cho khi thêm $m$ vào tử số và bớt $m$ ở mẫu số của phân số đã cho thì ta được phân số mới có giá trị bằng $\\frac{4}{5}$.", "Khi thêm $m$ vào tử số và bớt $m$ ở mẫu số thì tổng của tử số và mẫu số không thay đổi.\nTổng của tử số và mẫu số là: 15 + 39 = 54.\nỞ phân số mới bằng 4/5, coi tử số là 4 phần thì mẫu số là 5 phần.\nTổng số phần bằng nhau: 4 + 5 = 9 (phần).\nTử số mới là: 54 : 9 x 4 = 24.\nSố tự nhiên $m$ cần tìm là: 24 - 15 = 9.", "m = 9", 5, 1.5)
        ]
    }

    return exams
