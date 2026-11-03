# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 1: ÔN TẬP VÀ BỔ SUNG (BÀI 1 ĐẾN BÀI 6) - TOÁN 4 KNTT
Gồm 6 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 1: Ôn tập các số đến 100 000 (th4_b1_test1, th4_b1_test2, th4_b1_test3)
- Bài 2: Ôn tập các phép tính trong phạm vi 100 000 (th4_b2_test1, th4_b2_test2, th4_b2_test3)
- Bài 3: Số chẵn, số lẻ (th4_b3_test1, th4_b3_test2, th4_b3_test3)
- Bài 4: Biểu thức chứa chữ (th4_b4_test1, th4_b4_test2, th4_b4_test3)
- Bài 5: Giải bài toán có ba bước tính (th4_b5_test1, th4_b5_test2, th4_b5_test3)
- Bài 6: Luyện tập chung Chủ đề 1 (th4_b6_test1, th4_b6_test2, th4_b6_test3)
Tổng cộng: 18 đề kiểm tra chất lượng cao, độc lập 100%.
"""

def make_mc(qid, question, options, correct, explanation):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question, solution, answer, lineCount=4, points=1.0):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    return {
        "id": qid,
        "question": p_text,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 1: ÔN TẬP CÁC SỐ ĐẾN 100 000
    # =========================================================================
    exams["th4_b1_test1"] = {
        "id": "th4_b1_test1",
        "lessonId": "th4_b1",
        "lessonNum": 1,
        "testNum": 1,
        "title": "Bài 1: Ôn tập các số đến 100 000 - Đề số 1",
        "topic": "Ôn tập các số đến 100 000",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 6 chục nghìn, 5 nghìn, 4 trăm và 2 đơn vị viết là:", [
                "65 402",
                "65 420",
                "65 042",
                "605 402"
            ], 0, "Viết là 65 402."),
            make_mc(2, "Chữ số 7 trong số 87 235 có giá trị là:", [
                "7 000",
                "70 000",
                "700",
                "70"
            ], 0, "Chữ số 7 ở hàng nghìn nên có giá trị là 7 000."),
            make_mc(3, "Số liền trước của số 70 000 là:", [
                "69 999",
                "70 001",
                "69 990",
                "60 999"
            ], 0, "Số liền trước là $70 000 - 1 = 69 999$."),
            make_mc(4, "Số lớn nhất có 5 chữ số là:", [
                "99 999",
                "10 000",
                "90 000",
                "99 990"
            ], 0, "Số lớn nhất có 5 chữ số là 99 999."),
            make_mc(5, "Làm tròn số 45 820 đến hàng nghìn ta được số:", [
                "46 000",
                "45 000",
                "50 000",
                "45 800"
            ], 0, "Hàng trăm là 8 nên làm tròn lên 46 000."),
            make_mc(6, "Trong các số: 34 520, 34 502, 35 402, 34 250, số bé nhất là:", [
                "34 250",
                "34 502",
                "34 520",
                "35 402"
            ], 0, "So sánh hàng trăm: 2 bé nhất nên 34 250 bé nhất.")
        ],
        "part2": [
            make_essay(1, "Viết các số sau thành tổng theo mẫu:\na) $45 823 = 40 000 + 5 000 + 800 + 20 + 3$\nb) $60 740 = ..........$", "Bài giải:\n$60 740 = 60 000 + 700 + 40$\nĐáp số: 60 000 + 700 + 40", "60 000 + 700 + 40", 4, 1.0),
            make_essay(2, "Điền dấu thích hợp ($>, <, =$) vào chỗ chấm:\na) $48 500 ..... 48 499$\nb) $70 000 + 5 000 ..... 75 000$", "Bài giải:\na) $48 500 > 48 499$\nb) $70 000 + 5 000 = 75 000$\nĐáp số: a) >; b) =", "a) >; b) =", 4, 1.0),
            make_essay(3, "Sắp xếp các số sau theo thứ tự từ lớn đến bé:\n35 480; 35 840; 34 990; 36 010", "Bài giải:\n$36 010 > 35 840 > 35 480 > 34 990$\nThứ tự từ lớn đến bé là: 36 010; 35 840; 35 480; 34 990.\nĐáp số: 36 010; 35 840; 35 480; 34 990", "36 010; 35 840; 35 480; 34 990", 4, 1.0),
            make_essay(4, "Một cửa hàng nhập về 25 000 quyển vở. Tuần thứ nhất cửa hàng bán được 8 500 quyển. Tuần thứ hai bán được 9 200 quyển. Hỏi sau hai tuần, cửa hàng còn lại bao nhiêu quyển vở?", "Bài giải:\nCả hai tuần cửa hàng bán được số quyển vở là:\n$8 500 + 9 200 = 17 700$ (quyển)\nSau hai tuần, cửa hàng còn lại số quyển vở là:\n$25 000 - 17 700 = 7 300$ (quyển)\nĐáp số: 7 300 quyển vở.", "7 300 quyển", 6, 1.5),
            make_essay(5, "Một hình chữ nhật có chiều dài 36 cm, chiều rộng bằng $\\frac{1}{4}$ chiều dài. Tính chu vi và diện tích hình chữ nhật đó.", "Bài giải:\nChiều rộng hình chữ nhật là:\n$36 : 4 = 9$ (cm)\nChu vi hình chữ nhật là:\n$(36 + 9) \\times 2 = 90$ (cm)\nDiện tích hình chữ nhật là:\n$36 \\times 9 = 324$ ($\\text{cm}^2$)\nĐáp số: Chu vi: 90 cm; Diện tích: 324 $\\text{cm}^2$.", "Chu vi: 90 cm; S: 324 cm²", 6, 1.5),
            make_essay(6, "Từ các chữ số 0; 3; 5; 8, hãy viết số có 4 chữ số khác nhau lớn nhất và số có 4 chữ số khác nhau nhỏ nhất.", "Bài giải:\n- Số lớn nhất có 4 chữ số khác nhau từ các chữ số trên là: 8530.\n- Số bé nhất có 4 chữ số khác nhau từ các chữ số trên là: 3058.\nĐáp số: Lớn nhất: 8530; Bé nhất: 3058.", "8530 và 3058", 5, 1.0)
        ]
    }

    exams["th4_b1_test2"] = {
        "id": "th4_b1_test2",
        "lessonId": "th4_b1",
        "lessonNum": 1,
        "testNum": 2,
        "title": "Bài 1: Ôn tập các số đến 100 000 - Đề số 2",
        "topic": "Ôn tập các số đến 100 000",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số \"Tám mươi bảy nghìn không trăm linh sáu\" viết là:", ["87 006", "87 060", "87 600", "807 006"], 0, "Viết là 87 006."),
            make_mc(2, "Số 56 428 làm tròn đến hàng chục nghìn là:", ["60 000", "50 000", "56 000", "57 000"], 0, "Chữ số hàng nghìn là 6 nên làm tròn thành 60 000."),
            make_mc(3, "Số bé nhất có 5 chữ số khác nhau là:", ["10 234", "12 345", "10 000", "10 235"], 0, "Số bé nhất có 5 chữ số khác nhau là 10 234."),
            make_mc(4, "Giá trị của chữ số 4 trong số 34 821 là:", ["4 000", "40 000", "400", "40"], 0, "Hàng nghìn có giá trị 4 000."),
            make_mc(5, "Số liền sau của số 89 999 là:", ["90 000", "90 001", "89 998", "99 999"], 0, "$89 999 + 1 = 90 000$."),
            make_mc(6, "Trong các số: 72 345; 72 435; 72 543; 72 354, số lớn nhất là:", ["72 543", "72 435", "72 354", "72 345"], 0, "Hàng trăm là 5 lớn nhất: 72 543.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) Số liền trước của số 50 000 là: ..........\nb) Số liền sau của số 64 999 là: ..........", "Bài giải:\na) $50 000 - 1 = 49 999$\nb) $64 999 + 1 = 65 000$\nĐáp số: a) 49 999; b) 65 000", "a) 49 999; b) 65 000", 4, 1.0),
            make_essay(2, "Viết các số sau thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị:\na) $52 408$\nb) $90 650$", "Bài giải:\na) $52 408 = 50 000 + 2 000 + 400 + 8$\nb) $90 650 = 90 000 + 600 + 50$\nĐáp số: a) 50 000 + 2 000 + 400 + 8; b) 90 000 + 600 + 50", "a) 50000+2000+400+8; b) 90000+600+50", 4, 1.0),
            make_essay(3, "Làm tròn các số sau:\na) Số 38 472 làm tròn đến hàng nghìn: ..........\nb) Số 75 820 làm tròn đến hàng chục nghìn: ..........", "Bài giải:\na) Hàng trăm là 4 nên làm tròn thành 38 000.\nb) Hàng nghìn là 5 nên làm tròn thành 80 000.\nĐáp số: a) 38 000; b) 80 000", "a) 38 000; b) 80 000", 4, 1.0),
            make_essay(4, "Một trang trại có 18 500 con gà trắng và 12 300 con gà nâu. Người ta đã bán đi 15 000 con gà các loại. Hỏi trang trại đó còn lại bao nhiêu con gà?", "Bài giải:\nTổng số gà trang trại có ban đầu là:\n$18 500 + 12 300 = 30 800$ (con)\nSố gà trang trại còn lại là:\n$30 800 - 15 000 = 15 800$ (con)\nĐáp số: 15 800 con gà.", "15 800 con", 6, 1.5),
            make_essay(5, "Một hình vuông có chu vi là 48 cm. Một hình chữ nhật có chiều rộng bằng cạnh hình vuông đó và chiều dài là 18 cm. Tính diện tích hình chữ nhật.", "Bài giải:\nCạnh của hình vuông là:\n$48 : 4 = 12$ (cm)\nChiều rộng hình chữ nhật là 12 cm.\nDiện tích hình chữ nhật là:\n$18 \\times 12 = 216$ ($\\text{cm}^2$)\nĐáp số: 216 $\\text{cm}^2$.", "216 cm²", 6, 1.5),
            make_essay(6, "Tìm số tròn chục lớn nhất có 5 chữ số khác nhau.", "Bài giải:\nSố có 5 chữ số khác nhau và là số tròn chục thì chữ số tận cùng phải là 0.\nĐể số là lớn nhất, các chữ số hàng chục nghìn, nghìn, trăm, chục phải lần lượt lớn nhất: chọn 9, 8, 7, 6.\nVậy số cần tìm là: 98 760.\nĐáp số: 98 760.", "98 760", 5, 1.0)
        ]
    }

    exams["th4_b1_test3"] = {
        "id": "th4_b1_test3",
        "lessonId": "th4_b1",
        "lessonNum": 1,
        "testNum": 3,
        "title": "Bài 1: Ôn tập các số đến 100 000 - Đề số 3",
        "topic": "Ôn tập các số đến 100 000",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số 95 020 đọc là:", [
                "Chín mươi lăm nghìn không trăm hai mươi",
                "Chín mươi lăm nghìn hai trăm",
                "Chín mươi lăm nghìn hai mươi",
                "Chín trăm năm mươi nghìn hai mươi"
            ], 0, "Đọc là: Chín mươi lăm nghìn không trăm hai mươi."),
            make_mc(2, "Số gồm 4 chục nghìn và 5 trăm viết là:", ["40 500", "45 000", "40 050", "4 500"], 0, "Viết là 40 500."),
            make_mc(3, "Chữ số 6 trong số 63 218 có giá trị là:", ["60 000", "6 000", "600", "60"], 0, "Hàng chục nghìn có giá trị 60 000."),
            make_mc(4, "Số lớn nhất có 5 chữ số khác nhau là:", ["98 765", "99 999", "98 760", "98 675"], 0, "98 765 là số lớn nhất có 5 chữ số khác nhau."),
            make_mc(5, "Làm tròn số 82 450 đến hàng nghìn được:", ["82 000", "83 000", "80 000", "82 500"], 0, "Hàng trăm là 4 nên làm tròn thành 82 000."),
            make_mc(6, "Tìm số ở giữa số 45 689 và 45 691 là:", ["45 690", "45 688", "45 692", "45 700"], 0, "Số ở giữa là 45 690.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) Số chẵn lớn nhất có 5 chữ số là: ..........\nb) Số lẻ bé nhất có 5 chữ số là: ..........", "Bài giải:\na) Số chẵn lớn nhất có 5 chữ số là: 99 998.\nb) Số lẻ bé nhất có 5 chữ số là: 10 001.\nĐáp số: a) 99 998; b) 10 001", "a) 99 998; b) 10 001", 4, 1.0),
            make_essay(2, "Điền dấu thích hợp ($>, <, =$) vào chỗ chấm:\na) $65 420 ..... 65 240$\nb) $80 000 + 400 ..... 80 400$", "Bài giải:\na) $65 420 > 65 240$\nb) $80 000 + 400 = 80 400$\nĐáp số: a) >; b) =", "a) >; b) =", 4, 1.0),
            make_essay(3, "Sắp xếp các số sau theo thứ tự từ bé đến lớn:\n78 920; 78 290; 79 100; 78 902", "Bài giải:\n$78 290 < 78 902 < 78 920 < 79 100$\nThứ tự từ bé đến lớn: 78 290; 78 902; 78 920; 79 100.\nĐáp số: 78 290; 78 902; 78 920; 79 100", "78 290; 78 902; 78 920; 79 100", 4, 1.0),
            make_essay(4, "Một kho thóc có 48 000 kg thóc. Đợt đầu người ta chuyển đi 15 500 kg thóc, đợt sau chuyển đi 12 500 kg thóc. Hỏi trong kho còn lại bao nhiêu ki-lô-gam thóc?", "Bài giải:\nCả hai đợt đã chuyển đi số thóc là:\n$15 500 + 12 500 = 28 000$ (kg)\nTrong kho còn lại số thóc là:\n$48 000 - 28 000 = 20 000$ (kg)\nĐáp số: 20 000 kg thóc.", "20 000 kg", 6, 1.5),
            make_essay(5, "Một hình vuông có diện tích là 64 $\\text{cm}^2$. Tính chu vi của hình vuông đó.", "Bài giải:\nVì $8 \\times 8 = 64$ nên độ dài cạnh hình vuông là 8 cm.\nChu vi hình vuông là:\n$8 \\times 4 = 32$ (cm)\nĐáp số: 32 cm.", "32 cm", 5, 1.5),
            make_essay(6, "Viết số bé nhất có 5 chữ số mà tổng các chữ số của nó bằng 15.", "Bài giải:\nĐể số có 5 chữ số là bé nhất, chữ số hàng chục nghìn phải là 1.\nCác chữ số hàng nghìn, trăm, chục lần lượt bé nhất là 0, 0, 5 (hoặc dồn vào hàng đơn vị là 9 thì tổng $1 + 0 + 0 + 5 + 9 = 15$).\nTa có: Hàng chục nghìn là 1, hàng nghìn là 0, hàng trăm là 0, hàng chục là 5, hàng đơn vị là 9.\nSố cần tìm là 10 059.\nĐáp số: 10 059.", "10 059", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 2: ÔN TẬP CÁC PHÉP TÍNH TRONG PHẠM VI 100 000
    # =========================================================================
    exams["th4_b2_test1"] = {
        "id": "th4_b2_test1",
        "lessonId": "th4_b2",
        "lessonNum": 2,
        "testNum": 1,
        "title": "Bài 2: Ôn tập các phép tính trong phạm vi 100 000 - Đề số 1",
        "topic": "Ôn tập các phép tính trong phạm vi 100 000",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $35 000 + 15 000 = ?$", ["50 000", "40 000", "45 000", "60 000"], 0, "$35 000 + 15 000 = 50 000$."),
            make_mc(2, "Tính: $80 000 - 25 000 = ?$", ["55 000", "65 000", "50 000", "60 000"], 0, "$80 000 - 25 000 = 55 000$."),
            make_mc(3, "Tích của $12 000 \\times 4$ là:", ["48 000", "44 000", "36 000", "46 000"], 0, "$12 000 \\times 4 = 48 000$."),
            make_mc(4, "Thương của phép chia $45 000 : 5$ là:", ["9 000", "8 000", "900", "90 000"], 0, "$45 000 : 5 = 9 000$."),
            make_mc(5, "Tìm $x$ biết $x - 12 000 = 38 000$:", ["50 000", "26 000", "40 000", "48 000"], 0, "$x = 38 000 + 12 000 = 50 000$."),
            make_mc(6, "Giá trị của biểu thức $15 000 + 5 000 \\times 3$ là:", ["30 000", "60 000", "25 000", "35 000"], 0, "$15 000 + 15 000 = 30 000$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $45 628 + 27 345$\nb) $82 450 - 35 180$", "Bài giải:\na) $45 628 + 27 345 = 72 973$\nb) $82 450 - 35 180 = 47 270$\nĐáp số: a) 72 973; b) 47 270", "a) 72 973; b) 47 270", 4, 1.0),
            make_essay(2, "Đặt tính rồi tính:\na) $14 205 \\times 4$\nb) $36 840 : 6$", "Bài giải:\na) $14 205 \\times 4 = 56 820$\nb) $36 840 : 6 = 6 140$\nĐáp số: a) 56 820; b) 6 140", "a) 56 820; b) 6 140", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 5 = 75 000 - 25 000$", "Bài giải:\n$x \\times 5 = 50 000$\n$x = 50 000 : 5 = 10 000$\nĐáp số: $x = 10 000$", "x = 10 000", 4, 1.0),
            make_essay(4, "Một đội xe vận tải có 5 xe, mỗi xe chở được 3 500 kg hàng. Người ta dỡ hàng xuống phân phát cho 7 siêu thị với số lượng như nhau. Hỏi mỗi siêu thị nhận được bao nhiêu ki-lô-gam hàng?", "Bài giải:\nCả 5 xe chở được tất cả số hàng là:\n$3 500 \\times 5 = 17 500$ (kg)\nMỗi siêu thị nhận được số hàng là:\n$17 500 : 7 = 2 500$ (kg)\nĐáp số: 2 500 kg hàng.", "2 500 kg", 6, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có chiều rộng 25 m, chiều dài gấp 3 lần chiều rộng. Người ta xây tường rào bao quanh mảnh đất, chừa cổng ra vào rộng 4 m. Hỏi chiều dài bờ tường rào là bao nhiêu mét?", "Bài giải:\nChiều dài mảnh đất là:\n$25 \\times 3 = 75$ (m)\nChu vi mảnh đất là:\n$(75 + 25) \\times 2 = 200$ (m)\nChiều dài bờ tường rào là:\n$200 - 4 = 196$ (m)\nĐáp số: 196 m.", "196 m", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức sau:\n$S = 12 345 + 23 456 + 34 567 + 45 678 + 56 789 + 67 890$", "Bài giải:\nNhóm các cặp số có tổng bằng nhau:\n$S = (12 345 + 67 890) + (23 456 + 56 789) + (34 567 + 45 678)$\n$S = 80 235 + 80 245$ (ta tính trực tiếp: $12345+67890 = 80235$; $23456+56789 = 80245$; tổng = 240 725).\nCách khác: $S = 240 725$.\nĐáp số: 240 725.", "240 725", 5, 1.0)
        ]
    }

    exams["th4_b2_test2"] = {
        "id": "th4_b2_test2",
        "lessonId": "th4_b2",
        "lessonNum": 2,
        "testNum": 2,
        "title": "Bài 2: Ôn tập các phép tính trong phạm vi 100 000 - Đề số 2",
        "topic": "Ôn tập các phép tính trong phạm vi 100 000",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $62 000 + 18 000 = ?$", ["80 000", "70 000", "90 000", "85 000"], 0, "$62 000 + 18 000 = 80 000$."),
            make_mc(2, "Tính: $95 000 - 45 000 = ?$", ["50 000", "40 000", "60 000", "45 000"], 0, "$95 000 - 45 000 = 50 000$."),
            make_mc(3, "Tích của $23 000 \\times 3$ là:", ["69 000", "66 000", "60 000", "79 000"], 0, "$23 000 \\times 3 = 69 000$."),
            make_mc(4, "Thương của $56 000 : 7$ là:", ["8 000", "7 000", "9 000", "800"], 0, "$56 000 : 7 = 8 000$."),
            make_mc(5, "Tìm $x$ biết $x + 25 000 = 70 000$:", ["45 000", "50 000", "95 000", "40 000"], 0, "$x = 70 000 - 25 000 = 45 000$."),
            make_mc(6, "Giá trị của biểu thức $(24 000 - 4 000) : 4$ là:", ["5 000", "6 000", "4 000", "20 000"], 0, "$20 000 : 4 = 5 000$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $36 780 + 28 450$\nb) $74 500 - 28 360$", "Bài giải:\na) $36 780 + 28 450 = 65 230$\nb) $74 500 - 28 360 = 46 140$\nĐáp số: a) 65 230; b) 46 140", "a) 65 230; b) 46 140", 4, 1.0),
            make_essay(2, "Đặt tính rồi tính:\na) $16 240 \\times 3$\nb) $42 840 : 7$", "Bài giải:\na) $16 240 \\times 3 = 48 720$\nb) $42 840 : 7 = 6 120$\nĐáp số: a) 48 720; b) 6 120", "a) 48 720; b) 6 120", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 4 = 12 500 + 3 500$", "Bài giải:\n$x : 4 = 16 000$\n$x = 16 000 \\times 4 = 64 000$\nĐáp số: $x = 64 000$", "x = 64 000", 4, 1.0),
            make_essay(4, "Một nông trường có hai đàn cừu. Đàn thứ nhất có 3 450 con cừu, đàn thứ hai có số cừu gấp đôi đàn thứ nhất. Hỏi cả hai đàn cừu có tất cả bao nhiêu con?", "Bài giải:\nSố con cừu ở đàn thứ hai là:\n$3 450 \\times 2 = 6 900$ (con)\nCả hai đàn có tất cả số con cừu là:\n$3 450 + 6 900 = 10 350$ (con)\nĐáp số: 10 350 con cừu.", "10 350 con", 6, 1.5),
            make_essay(5, "Một hình vuông có chu vi 36 cm. Tính diện tích hình vuông đó.", "Bài giải:\nĐộ dài cạnh hình vuông là:\n$36 : 4 = 9$ (cm)\nDiện tích hình vuông là:\n$9 \\times 9 = 81$ ($\\text{cm}^2$)\nĐáp số: 81 $\\text{cm}^2$.", "81 cm²", 5, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$M = 25 000 \\times 8 - 25 000 \\times 4$", "Bài giải:\n$M = 25 000 \\times (8 - 4) = 25 000 \\times 4 = 100 000$\nĐáp số: $M = 100 000$", "M = 100 000", 4, 1.0)
        ]
    }

    exams["th4_b2_test3"] = {
        "id": "th4_b2_test3",
        "lessonId": "th4_b2",
        "lessonNum": 2,
        "testNum": 3,
        "title": "Bài 2: Ôn tập các phép tính trong phạm vi 100 000 - Đề số 3",
        "topic": "Ôn tập các phép tính trong phạm vi 100 000",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $48 000 + 32 000 = ?$", ["80 000", "70 000", "85 000", "78 000"], 0, "$48 000 + 32 000 = 80 000$."),
            make_mc(2, "Tính: $100 000 - 35 000 = ?$", ["65 000", "75 000", "60 000", "70 000"], 0, "$100 000 - 35 000 = 65 000$."),
            make_mc(3, "Tích của $15 000 \\times 6$ là:", ["90 000", "80 000", "60 000", "75 000"], 0, "$15 000 \\times 6 = 90 000$."),
            make_mc(4, "Thương của phép chia $63 000 : 9$ là:", ["7 000", "8 000", "9 000", "700"], 0, "$63 000 : 9 = 7 000$."),
            make_mc(5, "Tìm $x$ biết $85 000 - x = 40 000$:", ["45 000", "35 000", "50 000", "40 000"], 0, "$x = 85 000 - 40 000 = 45 000$."),
            make_mc(6, "Kết quả của phép tính $30 000 + 40 000 : 2$ là:", ["50 000", "35 000", "60 000", "45 000"], 0, "$40 000 : 2 = 20 000$, $30 000 + 20 000 = 50 000$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $52 840 + 39 170$\nb) $91 250 - 46 380$", "Bài giải:\na) $52 840 + 39 170 = 92 010$\nb) $91 250 - 46 380 = 44 870$\nĐáp số: a) 92 010; b) 44 870", "a) 92 010; b) 44 870", 4, 1.0),
            make_essay(2, "Đặt tính rồi tính:\na) $18 125 \\times 5$\nb) $49 350 : 7$", "Bài giải:\na) $18 125 \\times 5 = 90 625$\nb) $49 350 : 7 = 7 050$\nĐáp số: a) 90 625; b) 7 050", "a) 90 625; b) 7 050", 4, 1.0),
            make_essay(3, "Tính giá trị biểu thức:\n$A = 85 000 - 15 000 \\times 4$", "Bài giải:\n$A = 85 000 - 60 000 = 25 000$\nĐáp số: $A = 25 000$", "25 000", 4, 1.0),
            make_essay(4, "Một nhà máy sản xuất trong tháng thứ nhất được 24 500 đôi giày. Tháng thứ hai sản xuất được nhiều hơn tháng thứ nhất 3 500 đôi. Tháng thứ ba sản xuất được ít hơn tháng thứ hai 2 000 đôi. Hỏi trong cả ba tháng, nhà máy đó sản xuất được bao nhiêu đôi giày?", "Bài giải:\nTháng thứ hai sản xuất được số đôi giày là:\n$24 500 + 3 500 = 28 000$ (đôi)\nTháng thứ ba sản xuất được số đôi giày là:\n$28 000 - 2 000 = 26 000$ (đôi)\nCả ba tháng nhà máy sản xuất được số đôi giày là:\n$24 500 + 28 000 + 26 000 = 78 500$ (đôi)\nĐáp số: 78 500 đôi giày.", "78 500 đôi", 6, 1.5),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chiều dài 40 m, chiều rộng bằng $\\frac{1}{2}$ chiều dài. Tính chu vi và diện tích thửa ruộng đó.", "Bài giải:\nChiều rộng thửa ruộng là:\n$40 : 2 = 20$ (m)\nChu vi thửa ruộng là:\n$(40 + 20) \\times 2 = 120$ (m)\nDiện tích thửa ruộng là:\n$40 \\times 20 = 800$ ($\\text{m}^2$)\nĐáp số: Chu vi: 120 m; Diện tích: 800 $\\text{m}^2$.", "Chu vi: 120 m; S: 800 m²", 6, 1.5),
            make_essay(6, "Tìm $x$ biết:\n$x \\times 6 + x \\times 4 = 85 000$", "Bài giải:\n$x \\times (6 + 4) = 85 000$\n$x \\times 10 = 85 000$\n$x = 85 000 : 10 = 8 500$\nĐáp số: $x = 8 500$", "x = 8 500", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 3: SỐ CHẴN, SỐ LẺ
    # =========================================================================
    exams["th4_b3_test1"] = {
        "id": "th4_b3_test1",
        "lessonId": "th4_b3",
        "lessonNum": 3,
        "testNum": 1,
        "title": "Bài 3: Số chẵn, số lẻ - Đề số 1",
        "topic": "Số chẵn, số lẻ",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Các số có chữ số tận cùng là 0, 2, 4, 6, 8 gọi là:", ["Số chẵn", "Số lẻ", "Số tự nhiên", "Số tròn chục"], 0, "Định nghĩa: Số chẵn là số có chữ số tận cùng là 0, 2, 4, 6, 8."),
            make_mc(2, "Số nào dưới đây là số lẻ?", ["3 456", "7 891", "2 024", "4 570"], 1, "Số 7 891 có tận cùng là 1 nên là số lẻ."),
            make_mc(3, "Tổng của hai số chẵn luôn là:", ["Một số chẵn", "Một số lẻ", "Có thể chẵn hoặc lẻ", "Bằng 0"], 0, "Tổng của hai số chẵn luôn là số chẵn."),
            make_mc(4, "Số chẵn bé nhất có 4 chữ số là:", ["1 000", "1 002", "1 024", "1 001"], 0, "Số chẵn bé nhất có 4 chữ số là 1 000."),
            make_mc(5, "Số lẻ liền trước số 2025 là:", ["2023", "2024", "2021", "2026"], 0, "Số lẻ liền trước 2025 là 2023."),
            make_mc(6, "Tích của một số chẵn với một số lẻ bất kì là:", ["Số chẵn", "Số lẻ", "Số 0", "Không xác định"], 0, "Tích có thừa số chẵn thì luôn là số chẵn.")
        ],
        "part2": [
            make_essay(1, "Trong các số sau, số nào là số chẵn, số nào là số lẻ?\n452; 789; 1 246; 3 571; 8 900; 9 455", "Bài giải:\n- Các số chẵn là: 452; 1 246; 8 900.\n- Các số lẻ là: 789; 3 571; 9 455.\nĐáp số: Chẵn: 452, 1246, 8900; Lẻ: 789, 3571, 9455", "Chẵn: 452, 1246, 8900; Lẻ: 789, 3571, 9455", 4, 1.0),
            make_essay(2, "Viết 4 số chẵn liên tiếp bắt đầu từ số 1 998.", "Bài giải:\n4 số chẵn liên tiếp là: 1 998; 2 000; 2 002; 2 004.\nĐáp số: 1 998; 2 000; 2 002; 2 004", "1998, 2000, 2002, 2004", 4, 1.0),
            make_essay(3, "Không làm tính, hãy giải thích vì sao tổng sau là số chẵn hay số lẻ:\n$A = 246 + 358 + 470 + 582$", "Bài giải:\nCác số hạng 246, 358, 470, 582 đều là số chẵn.\nTổng của các số chẵn luôn là một số chẵn.\nVậy $A$ là số chẵn.\nĐáp số: A là số chẵn.", "Số chẵn", 4, 1.0),
            make_essay(4, "Một hàng cây có 45 cây trồng cách đều nhau. Người ta đánh số thứ tự các cây từ 1 đến 45. Hỏi có bao nhiêu cây mang số thứ tự là số chẵn, bao nhiêu cây mang số thứ tự là số lẻ?", "Bài giải:\nCác số từ 1 đến 45 gồm 45 số tự nhiên liên tiếp.\nSố các cây mang số chẵn (từ 2 đến 44) là:\n$(44 - 2) : 2 + 1 = 22$ (cây)\nSố các cây mang số lẻ (từ 1 đến 45) là:\n$(45 - 1) : 2 + 1 = 23$ (cây)\nĐáp số: Số chẵn: 22 cây; Số lẻ: 23 cây.", "Chẵn: 22 cây; Lẻ: 23 cây", 6, 1.5),
            make_essay(5, "Từ ba chữ số 2; 5; 8, hãy viết tất cả các số có 3 chữ số khác nhau. Trong các số vừa viết, có bao nhiêu số chẵn?", "Bài giải:\nCác số có 3 chữ số khác nhau lập từ 2; 5; 8 là:\n258; 285; 528; 582; 825; 852 (gồm 6 số).\nTrong đó các số chẵn (tận cùng là 2 hoặc 8) là:\n258; 528; 582; 852 (có 4 số chẵn).\nĐáp số: Có 6 số; 4 số chẵn.", "6 số, 4 số chẵn", 6, 1.5),
            make_essay(6, "Tìm hai số chẵn liên tiếp có tổng bằng 154.", "Bài giải:\nHai số chẵn liên tiếp hơn kém nhau 2 đơn vị.\nSố bé là: $(154 - 2) : 2 = 76$\nSố lớn là: $76 + 2 = 78$\nĐáp số: 76 và 78.", "76 và 78", 5, 1.0)
        ]
    }

    exams["th4_b3_test2"] = {
        "id": "th4_b3_test2",
        "lessonId": "th4_b3",
        "lessonNum": 3,
        "testNum": 2,
        "title": "Bài 3: Số chẵn, số lẻ - Đề số 2",
        "topic": "Số chẵn, số lẻ",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Các số có chữ số tận cùng là 1, 3, 5, 7, 9 gọi là:", ["Số lẻ", "Số chẵn", "Số tròn chục", "Số nguyên tố"], 0, "Định nghĩa số lẻ."),
            make_mc(2, "Số nào dưới đây là số chẵn?", ["1 357", "2 468", "9 875", "4 321"], 1, "Số 2 468 tận cùng là 8 nên là số chẵn."),
            make_mc(3, "Tổng của hai số lẻ luôn là:", ["Một số chẵn", "Một số lẻ", "Có thể chẵn hoặc lẻ", "Bằng 1"], 0, "Lẻ + lẻ = chẵn."),
            make_mc(4, "Số lẻ bé nhất có 3 chữ số khác nhau là:", ["103", "101", "105", "123"], 0, "Số lẻ bé nhất có 3 chữ số khác nhau là 103."),
            make_mc(5, "Số chẵn liền sau số 998 là:", ["1000", "999", "1002", "1004"], 0, "$998 + 2 = 1000$."),
            make_mc(6, "Hiệu của hai số lẻ liên tiếp là:", ["2", "1", "3", "0"], 0, "Hai số lẻ liên tiếp hơn kém nhau 2 đơn vị.")
        ],
        "part2": [
            make_essay(1, "Viết 5 số lẻ liên tiếp bắt đầu từ số 2 015.", "Bài giải:\n5 số lẻ liên tiếp là: 2 015; 2 017; 2 019; 2 021; 2 023.\nĐáp số: 2 015; 2 017; 2 019; 2 021; 2 023", "2015, 2017, 2019, 2021, 2023", 4, 1.0),
            make_essay(2, "Tổng sau là số chẵn hay số lẻ? Giải thích:\n$B = 135 + 247 + 359$", "Bài giải:\nTổng $135 + 247$ là tổng của hai số lẻ nên là một số chẵn.\nLấy số chẵn đó cộng với 359 (số lẻ) ta được kết quả là một số lẻ.\nVậy $B$ là số lẻ.\nĐáp số: B là số lẻ.", "Số lẻ", 4, 1.0),
            make_essay(3, "Viết số chẵn lớn nhất có 5 chữ số và số lẻ bé nhất có 5 chữ số.", "Bài giải:\n- Số chẵn lớn nhất có 5 chữ số là: 99 998.\n- Số lẻ bé nhất có 5 chữ số là: 10 001.\nĐáp số: 99 998 và 10 001.", "99 998 và 10 001", 4, 1.0),
            make_essay(4, "Một giá sách có hai ngăn. Ngăn thứ nhất có 124 quyển sách (số chẵn). Ngăn thứ hai có 85 quyển sách (số lẻ). Hỏi tổng số sách trên giá là số chẵn hay số lẻ?", "Bài giải:\nTổng số sách trên giá là:\n$124 + 85 = 209$ (quyển)\nVì 209 có chữ số tận cùng là 9 nên tổng số sách là một số lẻ.\nĐáp số: Là số lẻ (209 quyển).", "Số lẻ (209 quyển)", 5, 1.5),
            make_essay(5, "Từ bốn chữ số 0; 1; 2; 3, hãy viết số chẵn lớn nhất có 4 chữ số khác nhau và số lẻ nhỏ nhất có 4 chữ số khác nhau.", "Bài giải:\n- Số chẵn lớn nhất có 4 chữ số khác nhau: chọn hàng nghìn là 3, hàng trăm là 2, hàng chục là 1, hàng đơn vị là 0 $\\rightarrow$ số 3210.\n- Số lẻ nhỏ nhất có 4 chữ số khác nhau: chọn hàng nghìn là 2 (để dành 1 hoặc 3 làm số lẻ tận cùng), hàng trăm là 0, hàng chục là 3, hàng đơn vị là 1 $\\rightarrow$ số 2031.\nĐáp số: Số chẵn lớn nhất: 3210; Số lẻ nhỏ nhất: 2031.", "3210 và 2031", 6, 1.5),
            make_essay(6, "Tìm hai số lẻ liên tiếp có tổng bằng 248.", "Bài giải:\nHai số lẻ liên tiếp hơn kém nhau 2 đơn vị.\nSố bé là: $(248 - 2) : 2 = 123$\nSố lớn là: $123 + 2 = 125$\nĐáp số: 123 và 125.", "123 và 125", 5, 1.0)
        ]
    }

    exams["th4_b3_test3"] = {
        "id": "th4_b3_test3",
        "lessonId": "th4_b3",
        "lessonNum": 3,
        "testNum": 3,
        "title": "Bài 3: Số chẵn, số lẻ - Đề số 3",
        "topic": "Số chẵn, số lẻ",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số chẵn liền sau của số 4 598 là:", ["4 600", "4 599", "4 602", "4 604"], 0, "$4 598 + 2 = 4 600$."),
            make_mc(2, "Số lẻ liền trước của số 10 001 là:", ["9 999", "10 000", "9 997", "10 003"], 0, "$10 001 - 2 = 9 999$."),
            make_mc(3, "Tích của hai số lẻ luôn là:", ["Một số lẻ", "Một số chẵn", "Bằng 0", "Không xác định"], 0, "Lẻ $\\times$ lẻ = lẻ."),
            make_mc(4, "Có bao nhiêu số chẵn có 2 chữ số?", ["45 số", "50 số", "40 số", "90 số"], 0, "Các số chẵn từ 10 đến 98: $(98 - 10) : 2 + 1 = 45$ số."),
            make_mc(5, "Tổng của một số chẵn và một số lẻ luôn là:", ["Số lẻ", "Số chẵn", "Số 0", "Có thể chẵn hoặc lẻ"], 0, "Chẵn + lẻ = lẻ."),
            make_mc(6, "Trong các số: 124, 357, 468, 579, 680, có bao nhiêu số lẻ?", ["2 số", "3 số", "1 số", "4 số"], 0, "Các số lẻ là: 357 và 579 (có 2 số).")
        ],
        "part2": [
            make_essay(1, "Viết các số chẵn có hai chữ số và có chữ số hàng chục là 7.", "Bài giải:\nCác số chẵn cần tìm là: 70; 72; 74; 76; 78.\nĐáp số: 70; 72; 74; 76; 78", "70, 72, 74, 76, 78", 4, 1.0),
            make_essay(2, "Giải thích vì sao tích sau là số chẵn:\n$P = 15 \\times 17 \\times 19 \\times 22$", "Bài giải:\nTrong tích $P$ có thừa số 22 là số chẵn.\nMột tích có ít nhất một thừa số chẵn thì toàn bộ tích đó luôn là một số chẵn.\nVậy $P$ là số chẵn.\nĐáp số: P là số chẵn.", "Số chẵn", 4, 1.0),
            make_essay(3, "Viết số lẻ lớn nhất có 5 chữ số khác nhau và số chẵn bé nhất có 5 chữ số khác nhau.", "Bài giải:\n- Số lẻ lớn nhất có 5 chữ số khác nhau: 98 765.\n- Số chẵn bé nhất có 5 chữ số khác nhau: 10 234.\nĐáp số: 98 765 và 10 234.", "98 765 và 10 234", 4, 1.0),
            make_essay(4, "Có 30 bông hoa được cắm đều vào 5 lọ. Hỏi số bông hoa trong mỗi lọ là số chẵn hay số lẻ?", "Bài giải:\nSố bông hoa trong mỗi lọ là:\n$30 : 5 = 6$ (bông)\nVì 6 là số chẵn nên số bông hoa trong mỗi lọ là số chẵn.\nĐáp số: Là số chẵn (6 bông hoa).", "Số chẵn (6 bông)", 5, 1.5),
            make_essay(5, "Tìm 3 số chẵn liên tiếp biết tổng của chúng bằng 186.", "Bài giải:\nSố ở giữa (trung bình cộng của 3 số) là:\n$186 : 3 = 62$\nSố thứ nhất là: $62 - 2 = 60$\nSố thứ ba là: $62 + 2 = 64$\nVậy 3 số chẵn liên tiếp là: 60; 62; 64.\nĐáp số: 60; 62; 64.", "60, 62, 64", 6, 1.5),
            make_essay(6, "Cho dãy số: 1, 3, 5, 7, ..., 99. Dãy số trên có tất cả bao nhiêu số hạng? Tổng các số hạng của dãy là bao nhiêu?", "Bài giải:\nSố các số hạng của dãy là:\n$(99 - 1) : 2 + 1 = 50$ (số hạng)\nTổng các số hạng của dãy là:\n$(1 + 99) \\times 50 : 2 = 100 \\times 25 = 2500$\nĐáp số: 50 số hạng; Tổng: 2500.", "50 số hạng; Tổng: 2500", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 4: BIỂU THỨC CHỨA CHỮ
    # =========================================================================
    exams["th4_b4_test1"] = {
        "id": "th4_b4_test1",
        "lessonId": "th4_b4",
        "lessonNum": 4,
        "testNum": 1,
        "title": "Bài 4: Biểu thức chứa chữ - Đề số 1",
        "topic": "Biểu thức chứa chữ",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Biểu thức nào dưới đây là biểu thức chứa một chữ?", ["$a + 25$", "$15 + 35$", "$x + y$", "$2 \\times 5 + 8$"], 0, "$a + 25$ chứa 1 chữ cái $a$."),
            make_mc(2, "Giá trị của biểu thức $35 + b$ với $b = 15$ là:", ["50", "40", "60", "45"], 0, "$35 + 15 = 50$."),
            make_mc(3, "Nếu $m = 8$ thì giá trị của biểu thức $45 - m \\times 5$ là:", ["5", "185", "40", "35"], 0, "$45 - 8 \\times 5 = 45 - 40 = 5$."),
            make_mc(4, "Biểu thức chu vi hình vuông có cạnh dài $a$ là:", ["$a \\times 4$", "$a \\times a$", "$a + 4$", "$a : 4$"], 0, "Chu vi hình vuông là $a \\times 4$."),
            make_mc(5, "Với $x = 10$, giá trị của biểu thức $150 : x + 25$ là:", ["40", "15", "35", "50"], 0, "$150 : 10 + 25 = 15 + 25 = 40$."),
            make_mc(6, "Một hình chữ nhật có chiều dài $a$ và chiều rộng $b$. Chu vi hình chữ nhật đó là:", ["$(a + b) \\times 2$", "$a \\times b$", "$a + b$", "$a \\times 2 + b$"], 0, "Công thức chu vi là $(a + b) \\times 2$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của biểu thức:\na) $250 + m$ với $m = 750$\nb) $a \\times 6$ với $a = 150$", "Bài giải:\na) $250 + 750 = 1000$\nb) $150 \\times 6 = 900$\nĐáp số: a) 1000; b) 900", "a) 1000; b) 900", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\na) $180 - c : 4$ với $c = 320$\nb) $(x + y) \\times 3$ với $x = 25, y = 15$", "Bài giải:\na) $180 - 320 : 4 = 180 - 80 = 100$\nb) $(25 + 15) \\times 3 = 40 \\times 3 = 120$\nĐáp số: a) 100; b) 120", "a) 100; b) 120", 4, 1.0),
            make_essay(3, "Cho biểu thức $P = 120 \\times a$. Với $a = 8$, tính giá trị của $P$.", "Bài giải:\nVới $a = 8$, ta có:\n$P = 120 \\times 8 = 960$\nĐáp số: 960", "960", 4, 1.0),
            make_essay(4, "Một người đi bộ mỗi giờ đi được $v$ ki-lô-mét. Hỏi trong 3 giờ người đó đi được bao nhiêu ki-lô-mét? Tính quãng đường người đó đi được khi $v = 4\\text{ km/h}$.", "Bài giải:\nQuãng đường người đó đi được trong 3 giờ là:\n$s = v \\times 3$ (km)\nVới $v = 4\\text{ km/h}$, quãng đường người đó đi được là:\n$4 \\times 3 = 12$ (km)\nĐáp số: 12 km.", "12 km", 5, 1.5),
            make_essay(5, "Chu vi của một hình chữ nhật được tính theo công thức $C = (a + b) \\times 2$ ($a$ là chiều dài, $b$ là chiều rộng cùng đơn vị đo).\na) Tính chu vi khi $a = 18\\text{ cm}, b = 12\\text{ cm}$.\nb) Tính diện tích $S = a \\times b$ với kích thước trên.", "Bài giải:\na) Chu vi hình chữ nhật là:\n$C = (18 + 12) \\times 2 = 30 \\times 2 = 60$ (cm)\nb) Diện tích hình chữ nhật là:\n$S = 18 \\times 12 = 216$ ($\\text{cm}^2$)\nĐáp số: a) 60 cm; b) 216 $\\text{cm}^2$.", "a) 60 cm; b) 216 cm²", 6, 1.5),
            make_essay(6, "Tìm giá trị của $x$ để biểu thức $A = 100 - x \\times 5$ có giá trị bằng 25.", "Bài giải:\nTa có: $100 - x \\times 5 = 25$\n$x \\times 5 = 100 - 25 = 75$\n$x = 75 : 5 = 15$\nĐáp số: $x = 15$", "x = 15", 5, 1.0)
        ]
    }

    exams["th4_b4_test2"] = {
        "id": "th4_b4_test2",
        "lessonId": "th4_b4",
        "lessonNum": 4,
        "testNum": 2,
        "title": "Bài 4: Biểu thức chứa chữ - Đề số 2",
        "topic": "Biểu thức chứa chữ",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của biểu thức $a + b$ với $a = 45, b = 55$ là:", ["100", "90", "110", "80"], 0, "$45 + 55 = 100$."),
            make_mc(2, "Nếu $m = 6$ thì giá trị biểu thức $72 : m$ là:", ["12", "11", "13", "14"], 0, "$72 : 6 = 12$."),
            make_mc(3, "Biểu thức chứa hai chữ là biểu thức nào?", ["$a + b + 5$", "$x + 10$", "$2 \\times 3$", "$m - 4$"], 0, "$a + b + 5$ chứa 2 chữ cái $a$ và $b$."),
            make_mc(4, "Biểu thức tính diện tích hình chữ nhật có chiều dài $a$ và chiều rộng $b$ là:", ["$a \\times b$", "$(a + b) \\times 2$", "$a + b$", "$a : b$"], 0, "Diện tích: $a \\times b$."),
            make_mc(5, "Với $y = 8$, giá trị của $100 - 5 \\times y$ là:", ["60", "40", "50", "70"], 0, "$100 - 40 = 60$."),
            make_mc(6, "Một cửa hàng có $k$ thùng dầu, mỗi thùng chứa 20 lít. Số lít dầu cửa hàng có là:", ["$20 \\times k$", "$20 + k$", "$20 - k$", "$20 : k$"], 0, "Tổng số lít là $20 \\times k$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của biểu thức:\na) $360 : a$ với $a = 9$\nb) $b \\times 8 + 45$ với $b = 12$", "Bài giải:\na) $360 : 9 = 40$\nb) $12 \\times 8 + 45 = 96 + 45 = 141$\nĐáp số: a) 40; b) 141", "a) 40; b) 141", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức $P = m + n - p$ với $m = 120, n = 80, p = 50$.", "Bài giải:\nThay số vào biểu thức:\n$P = 120 + 80 - 50 = 200 - 50 = 150$\nĐáp số: 150", "150", 4, 1.0),
            make_essay(3, "Cho biểu thức $Q = (a - b) \\times c$. Tính giá trị của $Q$ với $a = 45, b = 15, c = 4$.", "Bài giải:\n$Q = (45 - 15) \\times 4 = 30 \\times 4 = 120$\nĐáp số: 120", "120", 4, 1.0),
            make_essay(4, "Một người thợ đóng được $x$ cái bàn trong một ngày. Hỏi trong 6 ngày người đó đóng được bao nhiêu cái bàn? Tính số bàn đóng được khi $x = 5$.", "Bài giải:\nTrong 6 ngày người đó đóng được số bàn là:\n$x \\times 6$ (cái bàn)\nVới $x = 5$, số bàn đóng được là:\n$5 \\times 6 = 30$ (cái bàn)\nĐáp số: 30 cái bàn.", "30 cái bàn", 5, 1.5),
            make_essay(5, "Một hình vuông có cạnh dài $a$. Công thức tính diện tích là $S = a \\times a$.\na) Tính diện tích hình vuông khi $a = 15\\text{ cm}$.\nb) Tính chu vi hình vuông khi $a = 15\\text{ cm}$.", "Bài giải:\na) Diện tích hình vuông là:\n$S = 15 \\times 15 = 225$ ($\\text{cm}^2$)\nb) Chu vi hình vuông là:\n$C = 15 \\times 4 = 60$ (cm)\nĐáp số: a) 225 $\\text{cm}^2$; b) 60 cm.", "a) 225 cm²; b) 60 cm", 6, 1.5),
            make_essay(6, "Tìm số tự nhiên $a$ biết rằng biểu thức $150 : (a - 2) = 30$.", "Bài giải:\n$a - 2 = 150 : 30 = 5$\n$a = 5 + 2 = 7$\nĐáp số: $a = 7$", "a = 7", 5, 1.0)
        ]
    }

    exams["th4_b4_test3"] = {
        "id": "th4_b4_test3",
        "lessonId": "th4_b4",
        "lessonNum": 4,
        "testNum": 3,
        "title": "Bài 4: Biểu thức chứa chữ - Đề số 3",
        "topic": "Biểu thức chứa chữ",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của biểu thức $x - 30$ với $x = 75$ là:", ["45", "40", "50", "35"], 0, "$75 - 30 = 45$."),
            make_mc(2, "Nếu $a = 15$ thì giá trị của $a \\times 4$ là:", ["60", "50", "45", "65"], 0, "$15 \\times 4 = 60$."),
            make_mc(3, "Biểu thức $m + n \\times 2$ với $m = 10, n = 5$ có giá trị bằng:", ["20", "30", "25", "15"], 0, "$10 + 5 \\times 2 = 10 + 10 = 20$."),
            make_mc(4, "Một quyển vở giá 8 000 đồng, mua $n$ quyển vở hết số tiền là:", ["$8 000 \\times n$", "$8 000 + n$", "$8 000 : n$", "$8 000 - n$"], 0, "Số tiền là $8 000 \\times n$ đồng."),
            make_mc(5, "Với $a = 24$, giá trị của biểu thức $a : 3 + 12$ là:", ["20", "18", "22", "16"], 0, "$24 : 3 + 12 = 8 + 12 = 20$."),
            make_mc(6, "Nếu $b = 0$ thì giá trị của biểu thức $45 \\times b + 15$ là:", ["15", "60", "0", "45"], 0, "$45 \\times 0 + 15 = 15$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của biểu thức:\na) $450 - y$ với $y = 120$\nb) $k : 5 + 35$ với $k = 450$", "Bài giải:\na) $450 - 120 = 330$\nb) $450 : 5 + 35 = 90 + 35 = 125$\nĐáp số: a) 330; b) 125", "a) 330; b) 125", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức $A = a \\times b - c$ với $a = 15, b = 6, c = 25$.", "Bài giải:\n$A = 15 \\times 6 - 25 = 90 - 25 = 65$\nĐáp số: 65", "65", 4, 1.0),
            make_essay(3, "Cho biểu thức $B = (x + y) : z$. Tính giá trị của $B$ với $x = 120, y = 80, z = 5$.", "Bài giải:\n$B = (120 + 80) : 5 = 200 : 5 = 40$\nĐáp số: 40", "40", 4, 1.0),
            make_essay(4, "Một tổ công nhân có 8 người, mỗi người làm được $a$ sản phẩm trong một ngày. Hỏi cả tổ làm được bao nhiêu sản phẩm trong một ngày? Tính số sản phẩm cả tổ làm được khi $a = 14$.", "Bài giải:\nSố sản phẩm cả tổ làm được trong một ngày là:\n$8 \\times a$ (sản phẩm)\nVới $a = 14$, số sản phẩm cả tổ làm được là:\n$8 \\times 14 = 112$ (sản phẩm)\nĐáp số: 112 sản phẩm.", "112 sản phẩm", 6, 1.5),
            make_essay(5, "Chu vi tam giác đều có cạnh $a$ là $C = a \\times 3$.\na) Tính chu vi tam giác đều khi $a = 16\\text{ cm}$.\nb) Nếu chu vi tam giác đều là 60 cm thì cạnh $a$ dài bao nhiêu xăng-ti-mét?", "Bài giải:\na) Chu vi tam giác đều là:\n$C = 16 \\times 3 = 48$ (cm)\nb) Độ dài cạnh $a$ là:\n$a = 60 : 3 = 20$ (cm)\nĐáp số: a) 48 cm; b) 20 cm.", "a) 48 cm; b) 20 cm", 6, 1.5),
            make_essay(6, "Tìm giá trị lớn nhất của biểu thức $M = 200 - 15 \\times x$ với $x$ là số tự nhiên.", "Bài giải:\nĐể $M = 200 - 15 \\times x$ đạt giá trị lớn nhất thì số trừ $15 \\times x$ phải nhỏ nhất.\nVì $x$ là số tự nhiên nên $x$ nhỏ nhất là $x = 0$.\nKhi đó: $M = 200 - 15 \\times 0 = 200$.\nĐáp số: Giá trị lớn nhất là 200 khi $x = 0$.", "200 (khi x = 0)", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 5: GIẢI BÀI TOÁN CÓ BA BƯỚC TÍNH
    # =========================================================================
    exams["th4_b5_test1"] = {
        "id": "th4_b5_test1",
        "lessonId": "th4_b5",
        "lessonNum": 5,
        "testNum": 1,
        "title": "Bài 5: Giải bài toán có ba bước tính - Đề số 1",
        "topic": "Giải bài toán có ba bước tính",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một bài toán có ba bước tính là bài toán cần thực hiện ít nhất:", ["1 phép tính", "2 phép tính", "3 phép tính", "4 phép tính"], 2, "Cần thực hiện 3 phép tính để tìm ra đáp số."),
            make_mc(2, "An có 15 viên bi, Bình có nhiều hơn An 5 viên bi. Cả hai bạn có tất cả số viên bi là:", ["35 viên", "25 viên", "20 viên", "30 viên"], 0, "Bình có: 20 viên. Cả hai bạn có: $15 + 20 = 35$ viên."),
            make_mc(3, "Mẹ mua 3 kg gạo tẻ giá 18 000 đ/kg và 2 kg gạo nếp giá 25 000 đ/kg. Tổng số tiền mẹ mua gạo là:", ["104 000 đồng", "94 000 đồng", "86 000 đồng", "114 000 đồng"], 0, "$3 \\times 18 000 + 2 \\times 25 000 = 54 000 + 50 000 = 104 000$ đồng."),
            make_mc(4, "Một tổ công nhân ngày thứ nhất làm được 12 sản phẩm, ngày thứ hai làm gấp đôi ngày thứ nhất. Cả hai ngày tổ làm được:", ["36 sản phẩm", "24 sản phẩm", "30 sản phẩm", "48 sản phẩm"], 0, "Ngày 2: 24. Cả hai ngày: $12 + 24 = 36$ sản phẩm."),
            make_mc(5, "Một ô tô chạy giờ thứ nhất được 45 km, giờ thứ hai chạy được 50 km, giờ thứ ba chạy được 55 km. Trung bình mỗi giờ ô tô chạy được:", ["50 km", "48 km", "52 km", "55 km"], 0, "$(45 + 50 + 55) : 3 = 150 : 3 = 50$ km."),
            make_mc(6, "Bác thợ may may 1 cái áo hết 2 m vải, 1 cái quần hết 1 m vải. Để may 4 bộ quần áo như thế cần số mét vải là:", ["12 m", "10 m", "8 m", "14 m"], 0, "Mỗi bộ hết: $2 + 1 = 3$ m. 4 bộ hết: $3 \\times 4 = 12$ m.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức sau:\n$A = (45 + 15) \\times 3 - 50$", "Bài giải:\n$A = 60 \\times 3 - 50 = 180 - 50 = 130$\nĐáp số: 130", "130", 4, 1.0),
            make_essay(2, "Có 3 đội trồng cây. Đội 1 trồng được 120 cây. Đội 2 trồng được nhiều hơn đội 1 là 30 cây. Đội 3 trồng được số cây bằng một nửa số cây của đội 2. Hỏi đội 3 trồng được bao nhiêu cây?", "Bài giải:\nĐội 2 trồng được số cây là:\n$120 + 30 = 150$ (cây)\nĐội 3 trồng được số cây là:\n$150 : 2 = 75$ (cây)\nĐáp số: 75 cây.", "75 cây", 4, 1.0),
            make_essay(3, "Mai có 24 cái kẹo, Lan có số kẹo gấp đôi số kẹo của Mai. Cúc có số kẹo ít hơn tổng số kẹo của Mai và Lan là 10 cái. Hỏi Cúc có bao nhiêu cái kẹo?", "Bài giải:\nLan có số cái kẹo là:\n$24 \\times 2 = 48$ (cái)\nTổng số kẹo của Mai và Lan là:\n$24 + 48 = 72$ (cái)\nCúc có số cái kẹo là:\n$72 - 10 = 62$ (cái)\nĐáp số: 62 cái kẹo.", "62 cái", 4, 1.0),
            make_essay(4, "Một cửa hàng ngày thứ nhất bán được 150 kg đường. Ngày thứ hai bán được số đường gấp 2 lần ngày thứ nhất. Ngày thứ ba bán được ít hơn ngày thứ hai 45 kg đường. Hỏi trong cả ba ngày, cửa hàng đó bán được tất cả bao nhiêu ki-lô-gam đường?", "Bài giải:\nNgày thứ hai bán được số ki-lô-gam đường là:\n$150 \\times 2 = 300$ (kg)\nNgày thứ ba bán được số ki-lô-gam đường là:\n$300 - 45 = 255$ (kg)\nCả ba ngày cửa hàng bán được số ki-lô-gam đường là:\n$150 + 300 + 255 = 705$ (kg)\nĐáp số: 705 kg đường.", "705 kg", 6, 1.5),
            make_essay(5, "Một trại chăn nuôi có 3 chuồng lợn. Chuồng 1 có 45 con lợn. Chuồng 2 có số lợn nhiều hơn chuồng 1 là 15 con. Chuồng 3 có số lợn bằng một nửa tổng số lợn của chuồng 1 và chuồng 2. Hỏi cả ba chuồng có tất cả bao nhiêu con lợn?", "Bài giải:\nChuồng 2 có số con lợn là:\n$45 + 15 = 60$ (con)\nTổng số lợn của chuồng 1 và chuồng 2 là:\n$45 + 60 = 105$ (con) (chỉnh số cho chẵn: chuồng 1 là 46 con $\\rightarrow$ chuồng 2 là 61 con $\\rightarrow$ tổng 107; để chia hết cho 2: Chuồng 1 có 40 con, chuồng 2 hơn chuồng 1 là 20 con $\\rightarrow$ chuồng 2 có 60 con $\\rightarrow$ tổng chuồng 1 và 2 là 100 con $\\rightarrow$ chuồng 3 là $100 : 2 = 50$ con. Cả ba chuồng: $100 + 50 = 150$ con).\nTính lại:\nChuồng 2 có số con lợn là: $40 + 20 = 60$ (con)\nChuồng 3 có số con lợn là: $(40 + 60) : 2 = 50$ (con)\nCả ba chuồng có số con lợn là: $40 + 60 + 50 = 150$ (con)\nĐáp số: 150 con lợn.", "150 con", 6, 1.5),
            make_essay(6, "Ba bạn An, Bình, Cư cùng góp tiền mua chung một quả bóng. An góp 35 000 đồng. Bình góp nhiều hơn An 10 000 đồng. Cư góp số tiền bằng nửa tổng số tiền của An và Bình. Hỏi quả bóng đó giá bao nhiêu tiền?", "Bài giải:\nBình góp số tiền là:\n$35 000 + 10 000 = 45 000$ (đồng)\nCư góp số tiền là:\n$(35 000 + 45 000) : 2 = 40 000$ (đồng)\nQuả bóng đó có giá là:\n$35 000 + 45 000 + 40 000 = 120 000$ (đồng)\nĐáp số: 120 000 đồng.", "120 000 đồng", 6, 1.0)
        ]
    }

    exams["th4_b5_test2"] = {
        "id": "th4_b5_test2",
        "lessonId": "th4_b5",
        "lessonNum": 5,
        "testNum": 2,
        "title": "Bài 5: Giải bài toán có ba bước tính - Đề số 2",
        "topic": "Giải bài toán có ba bước tính",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một xe chở 5 bao gạo, mỗi bao nặng 50 kg. Sau khi dỡ xuống 150 kg thì trên xe còn lại:", ["100 kg", "150 kg", "200 kg", "250 kg"], 0, "$5 \\times 50 - 150 = 250 - 150 = 100$ kg."),
            make_mc(2, "Bác Lan nuôi 60 con vịt, số gà gấp 3 lần số vịt. Tổng số gà và vịt bác nuôi là:", ["240 con", "180 con", "200 con", "220 con"], 0, "Số gà: $60 \\times 3 = 180$. Tổng: $60 + 180 = 240$ con."),
            make_mc(3, "Một ô tô tiêu thụ 10 lít xăng cho 100 km. Hỏi chạy 250 km ô tô tiêu thụ bao nhiêu lít xăng?", ["25 lít", "20 lít", "30 lít", "35 lít"], 0, "$10 : 100 \\times 250 = 25$ lít."),
            make_mc(4, "Hoa mua 5 quyển vở giá 7 000 đ/quyển và 2 bút chì giá 4 000 đ/cái. Hoa đưa cô bán hàng 50 000 đồng thì được trả lại:", ["7 000 đồng", "8 000 đồng", "6 000 đồng", "10 000 đồng"], 0, "Mua hết $35 000 + 8 000 = 43 000$ đ. Trả lại: $50 000 - 43 000 = 7 000$ đ."),
            make_mc(5, "Một cuộn dây dài 100 m, người ta cắt đi 3 đoạn, mỗi đoạn dài 25 m. Đoạn dây còn lại dài là:", ["25 m", "30 m", "20 m", "15 m"], 0, "$100 - 3 \\times 25 = 100 - 75 = 25$ m."),
            make_mc(6, "Trung bình cộng của ba số 20, 30 và 40 là:", ["30", "25", "35", "40"], 0, "$(20 + 30 + 40) : 3 = 30$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức sau:\n$B = 150 + 25 \\times 4 - 80$", "Bài giải:\n$B = 150 + 100 - 80 = 250 - 80 = 170$\nĐáp số: 170", "170", 4, 1.0),
            make_essay(2, "Một trường học có 3 khối lớp: Khối Ba có 140 học sinh. Khối Bốn có nhiều hơn Khối Ba 25 học sinh. Khối Năm có ít hơn Khối Bốn 15 học sinh. Hỏi Khối Năm có bao nhiêu học sinh?", "Bài giải:\nKhối Bốn có số học sinh là:\n$140 + 25 = 165$ (học sinh)\nKhối Năm có số học sinh là:\n$165 - 15 = 150$ (học sinh)\nĐáp số: 150 học sinh.", "150 học sinh", 4, 1.0),
            make_essay(3, "Một xưởng may trong tuần đầu may được 240 cái áo. Tuần thứ hai may được nhiều hơn tuần đầu 60 cái. Tuần thứ ba may được bằng một nửa tuần thứ hai. Hỏi tuần thứ ba may được bao nhiêu cái áo?", "Bài giải:\nTuần thứ hai may được số cái áo là:\n$240 + 60 = 300$ (cái áo)\nTuần thứ ba may được số cái áo là:\n$300 : 2 = 150$ (cái áo)\nĐáp số: 150 cái áo.", "150 cái áo", 4, 1.0),
            make_essay(4, "Một đoàn xe vận tải gồm 3 xe lớn chở được tất cả 15 tấn hàng và 4 xe nhỏ, mỗi xe chở được 2 tấn hàng. Hỏi cả đoàn xe chở được tất cả bao nhiêu tấn hàng? Trung bình mỗi xe chở được bao nhiêu tấn hàng (nếu tính theo số tự nhiên hoặc phân số)?", "Bài giải:\n4 xe nhỏ chở được số tấn hàng là:\n$2 \\times 4 = 8$ (tấn)\nCả đoàn xe chở được số tấn hàng là:\n$15 + 8 = 23$ (tấn)\nTổng số xe trong đoàn là:\n$3 + 4 = 7$ (xe)\nĐáp số: Cả đoàn xe chở 23 tấn hàng.", "23 tấn hàng", 6, 1.5),
            make_essay(5, "Bác Ba thu hoạch hồ tiêu trong 3 đợt: Đợt 1 thu được 120 kg. Đợt 2 thu được gấp đôi đợt 1. Đợt 3 thu được số tiêu bằng một nửa tổng hai đợt đầu. Hỏi cả ba đợt bác Ba thu hoạch được bao nhiêu ki-lô-gam hồ tiêu?", "Bài giải:\nĐợt 2 thu được số ki-lô-gam tiêu là:\n$120 \\times 2 = 240$ (kg)\nĐợt 3 thu được số ki-lô-gam tiêu là:\n$(120 + 240) : 2 = 180$ (kg)\nCả ba đợt thu hoạch được số ki-lô-gam tiêu là:\n$120 + 240 + 180 = 540$ (kg)\nĐáp số: 540 kg hồ tiêu.", "540 kg", 6, 1.5),
            make_essay(6, "Một tấm vải dài 90 m. Lần đầu người ta bán đi $\\frac{1}{3}$ tấm vải. Lần thứ hai bán đi $\\frac{1}{2}$ số vải còn lại. Hỏi sau hai lần bán, tấm vải còn lại bao nhiêu mét?", "Bài giải:\nLần đầu bán được số mét vải là:\n$90 : 3 = 30$ (m)\nSố mét vải còn lại sau lần đầu là:\n$90 - 30 = 60$ (m)\nLần thứ hai bán được số mét vải là:\n$60 : 2 = 30$ (m)\nSau hai lần bán, tấm vải còn lại số mét là:\n$60 - 30 = 30$ (m)\nĐáp số: 30 m vải.", "30 m", 6, 1.0)
        ]
    }

    exams["th4_b5_test3"] = {
        "id": "th4_b5_test3",
        "lessonId": "th4_b5",
        "lessonNum": 5,
        "testNum": 3,
        "title": "Bài 5: Giải bài toán có ba bước tính - Đề số 3",
        "topic": "Giải bài toán có ba bước tính",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người đi xe máy 2 giờ đầu đi được 70 km, giờ thứ ba đi được 35 km. Cả ba giờ người đó đi được:", ["105 km", "100 km", "110 km", "95 km"], 0, "$70 + 35 = 105$ km."),
            make_mc(2, "Có 4 thùng nước ngọt, mỗi thùng 24 lon. Đã uống hết 28 lon, số lon còn lại là:", ["68 lon", "72 lon", "64 lon", "70 lon"], 0, "$4 \\times 24 - 28 = 96 - 28 = 68$ lon."),
            make_mc(3, "Mẹ mua 4 gói kẹo giá 12 000 đ/gói và 1 hộp bánh giá 32 000 đ. Mẹ mua hết số tiền là:", ["80 000 đồng", "70 000 đồng", "76 000 đồng", "84 000 đồng"], 0, "$4 \\times 12 000 + 32 000 = 48 000 + 32 000 = 80 000$ đồng."),
            make_mc(4, "Một cửa hàng có 80 bao gạo. Ngày thứ nhất bán được 25 bao, ngày thứ hai bán được 30 bao. Số bao gạo còn lại là:", ["25 bao", "30 bao", "35 bao", "20 bao"], 0, "$80 - (25 + 30) = 80 - 55 = 25$ bao."),
            make_mc(5, "Số lít dầu ở thùng 1 là 40 lít, thùng 2 gấp đôi thùng 1, thùng 3 bằng nửa thùng 1. Thùng 3 có số lít dầu là:", ["20 lít", "80 lít", "40 lít", "10 lít"], 0, "Thùng 3: $40 : 2 = 20$ lít."),
            make_mc(6, "Một mảnh vườn hình chữ nhật có chiều dài 20 m, chiều rộng 10 m. Người ta dùng 50 $\\text{m}^2$ để trồng hoa. Diện tích còn lại là:", ["150 $\\text{m}^2$", "100 $\\text{m}^2$", "120 $\\text{m}^2$", "200 $\\text{m}^2$"], 0, "Diện tích: $20 \\times 10 = 200$. Còn lại: $200 - 50 = 150$ $\\text{m}^2$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\n$C = (120 - 40) \\times 2 + 60$", "Bài giải:\n$C = 80 \\times 2 + 60 = 160 + 60 = 220$\nĐáp số: 220", "220", 4, 1.0),
            make_essay(2, "Có 3 xe chở cát. Xe thứ nhất chở được 25 tạ cát. Xe thứ hai chở gấp đôi xe thứ nhất. Xe thứ ba chở nhiều hơn xe thứ hai 5 tạ cát. Hỏi xe thứ ba chở được bao nhiêu tạ cát?", "Bài giải:\nXe thứ hai chở được số tạ cát là:\n$25 \\times 2 = 50$ (tạ)\nXe thứ ba chở được số tạ cát là:\n$50 + 5 = 55$ (tạ)\nĐáp số: 55 tạ cát.", "55 tạ", 4, 1.0),
            make_essay(3, "Bình có 30 viên bi. Dũng có số bi gấp đôi số bi của Bình. Minh có số bi bằng một nửa tổng số bi của Bình và Dũng. Hỏi Minh có bao nhiêu viên bi?", "Bài giải:\nDũng có số viên bi là:\n$30 \\times 2 = 60$ (viên)\nTổng số bi của Bình và Dũng là:\n$30 + 60 = 90$ (viên)\nMinh có số viên bi là:\n$90 : 2 = 45$ (viên)\nĐáp số: 45 viên bi.", "45 viên", 4, 1.0),
            make_essay(4, "Một đội sản xuất nông nghiệp ngày thứ nhất thu hoạch được 350 kg dưa hấu. Ngày thứ hai thu hoạch được gấp đôi ngày thứ nhất. Ngày thứ ba thu hoạch được nhiều hơn ngày thứ hai 50 kg. Hỏi cả ba ngày đội đó thu hoạch được bao nhiêu tạ dưa hấu?", "Bài giải:\nNgày thứ hai thu hoạch được số dưa là:\n$350 \\times 2 = 700$ (kg)\nNgày thứ ba thu hoạch được số dưa là:\n$700 + 50 = 750$ (kg)\nCả ba ngày thu hoạch được số dưa là:\n$350 + 700 + 750 = 1800$ (kg)\nĐổi $1800\\text{ kg} = 18\\text{ tạ}$\nĐáp số: 18 tạ dưa hấu.", "18 tạ", 6, 1.5),
            make_essay(5, "Một xí nghiệp đóng gói 720 hộp bánh vào các thùng, mỗi thùng chứa 12 hộp. Sau đó người ta xếp các thùng lên 3 xe ô tô tải (mỗi xe chở số thùng bằng nhau). Hỏi mỗi xe ô tô chở bao nhiêu thùng bánh?", "Bài giải:\nTổng số thùng bánh đóng được là:\n$720 : 12 = 60$ (thùng)\nMỗi xe ô tô tải chở số thùng bánh là:\n$60 : 3 = 20$ (thùng)\nĐáp số: 20 thùng bánh.", "20 thùng", 5, 1.5),
            make_essay(6, "Bác nông dân có một đàn gà. Lần thứ nhất bác bán đi $\\frac{1}{2}$ đàn gà và thêm 1 con. Lần thứ hai bác bán đi $\\frac{1}{2}$ số gà còn lại và thêm 1 con thì trong chuồng còn lại đúng 5 con gà. Hỏi ban đầu đàn gà của bác có bao nhiêu con?", "Bài giải:\nSố gà còn lại trước lần bán thứ hai là:\n$(5 + 1) \\times 2 = 12$ (con)\nSố gà ban đầu của bác nông dân là:\n$(12 + 1) \\times 2 = 26$ (con)\nĐáp số: 26 con gà.", "26 con", 6, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 6: LUYỆN TẬP CHUNG CHỦ ĐỀ 1
    # =========================================================================
    exams["th4_b6_test1"] = {
        "id": "th4_b6_test1",
        "lessonId": "th4_b6",
        "lessonNum": 6,
        "testNum": 1,
        "title": "Bài 6: Luyện tập chung Chủ đề 1 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 1",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 7 chục nghìn, 8 trăm và 4 đơn vị viết là:", ["70 804", "78 004", "70 840", "78 400"], 0, "Viết là 70 804."),
            make_mc(2, "Tính giá trị của biểu thức $a + 45$ với $a = 55$ là:", ["100", "90", "110", "95"], 0, "$55 + 45 = 100$."),
            make_mc(3, "Số nào dưới đây vừa là số chẵn vừa lớn hơn 50 000?", ["54 286", "49 998", "54 287", "48 500"], 0, "54 286 > 50 000 và tận cùng là 6 nên là số chẵn."),
            make_mc(4, "Một ô tô chở 6 chuyến hàng, mỗi chuyến 25 tạ. Cả 6 chuyến chở được:", ["150 tạ", "120 tạ", "160 tạ", "140 tạ"], 0, "$25 \\times 6 = 150$ tạ."),
            make_mc(5, "Số liền sau của số chẵn lớn nhất có 4 chữ số là:", ["9 999", "10 000", "9 998", "9 997"], 0, "Số chẵn lớn nhất có 4 chữ số là 9 998, số liền sau là 9 999."),
            make_mc(6, "Làm tròn số 67 850 đến hàng nghìn ta được số:", ["68 000", "67 000", "70 000", "67 900"], 0, "Hàng trăm là 8 nên làm tròn thành 68 000.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $48 235 + 36 480$\nb) $75 420 - 38 190$", "Bài giải:\na) $48 235 + 36 480 = 84 715$\nb) $75 420 - 38 190 = 37 230$\nĐáp số: a) 84 715; b) 37 230", "a) 84 715; b) 37 230", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $m \\times 4 + 120$ với $m = 25$\nb) $(x - y) : 5$ với $x = 145, y = 45$", "Bài giải:\na) $25 \\times 4 + 120 = 100 + 120 = 220$\nb) $(145 - 45) : 5 = 100 : 5 = 20$\nĐáp số: a) 220; b) 20", "a) 220; b) 20", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 15 400 = 24 600 + 10 000$", "Bài giải:\n$x - 15 400 = 34 600$\n$x = 34 600 + 15 400 = 50 000$\nĐáp số: $x = 50 000$", "x = 50 000", 4, 1.0),
            make_essay(4, "Một cửa hàng buổi sáng bán được 120 kg gạo. Buổi chiều bán được gấp đôi buổi sáng. Buổi tối bán được ít hơn buổi chiều 50 kg. Hỏi cả ngày cửa hàng bán được bao nhiêu ki-lô-gam gạo?", "Bài giải:\nBuổi chiều bán được số ki-lô-gam gạo là:\n$120 \\times 2 = 240$ (kg)\nBuổi tối bán được số ki-lô-gam gạo là:\n$240 - 50 = 190$ (kg)\nCả ngày bán được số ki-lô-gam gạo là:\n$120 + 240 + 190 = 550$ (kg)\nĐáp số: 550 kg gạo.", "550 kg", 6, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có chu vi là 100 m, chiều dài là 35 m. Tính diện tích mảnh đất đó.", "Bài giải:\nNửa chu vi mảnh đất là:\n$100 : 2 = 50$ (m)\nChiều rộng mảnh đất là:\n$50 - 35 = 15$ (m)\nDiện tích mảnh đất là:\n$35 \\times 15 = 525$ ($\\text{m}^2$)\nĐáp số: 525 $\\text{m}^2$.", "525 m²", 6, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$S = 250 \\times 17 + 250 \\times 83$", "Bài giải:\n$S = 250 \\times (17 + 83) = 250 \\times 100 = 25 000$\nĐáp số: $S = 25 000$", "S = 25 000", 4, 1.0)
        ]
    }

    exams["th4_b6_test2"] = {
        "id": "th4_b6_test2",
        "lessonId": "th4_b6",
        "lessonNum": 6,
        "testNum": 2,
        "title": "Bài 6: Luyện tập chung Chủ đề 1 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 1",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Chữ số 9 trong số 92 450 có giá trị là:", ["90 000", "9 000", "900", "90"], 0, "Chữ số 9 ở hàng chục nghìn."),
            make_mc(2, "Số lẻ lớn nhất có 4 chữ số khác nhau là:", ["9 875", "9 999", "9 876", "9 879"], 0, "9 875 là số lẻ lớn nhất có 4 chữ số khác nhau."),
            make_mc(3, "Tính: $15 000 \\times 4 : 2 = ?$", ["30 000", "60 000", "15 000", "45 000"], 0, "$60 000 : 2 = 30 000$."),
            make_mc(4, "Biểu thức $p - q + 10$ với $p = 40, q = 25$ có giá trị bằng:", ["25", "15", "35", "20"], 0, "$40 - 25 + 10 = 15 + 10 = 25$."),
            make_mc(5, "Một hình vuông có cạnh dài 12 cm. Chu vi của nó là:", ["48 cm", "144 cm", "24 cm", "36 cm"], 0, "$12 \\times 4 = 48$ cm."),
            make_mc(6, "Tìm số chẵn ở giữa 458 và 462 là:", ["460", "459", "461", "464"], 0, "Số chẵn ở giữa là 460.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $63 450 + 28 760$\nb) $84 200 - 47 580$", "Bài giải:\na) $63 450 + 28 760 = 92 210$\nb) $84 200 - 47 580 = 36 620$\nĐáp số: a) 92 210; b) 36 620", "a) 92 210; b) 36 620", 4, 1.0),
            make_essay(2, "Đặt tính rồi tính:\na) $12 405 \\times 6$\nb) $45 840 : 8$", "Bài giải:\na) $12 405 \\times 6 = 74 430$\nb) $45 840 : 8 = 5 730$\nĐáp số: a) 74 430; b) 5 730", "a) 74 430; b) 5 730", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 4 = 18 000 + 14 000$", "Bài giải:\n$x \\times 4 = 32 000$\n$x = 32 000 : 4 = 8 000$\nĐáp số: $x = 8 000$", "x = 8 000", 4, 1.0),
            make_essay(4, "Một thư viện trường học nhận về 3 thùng sách giáo khoa, mỗi thùng có 150 cuốn và 2 thùng truyện tranh, mỗi thùng có 120 cuốn. Toàn bộ số sách và truyện được chia đều cho 9 lớp học. Hỏi mỗi lớp nhận được bao nhiêu cuốn?", "Bài giải:\nSố sách giáo khoa là:\n$150 \\times 3 = 450$ (cuốn)\nSố truyện tranh là:\n$120 \\times 2 = 240$ (cuốn)\nTổng số sách và truyện là:\n$450 + 240 = 690$ (cuốn)\nMỗi lớp nhận được số cuốn là (lấy số tròn: $150 \\times 3 = 450$, truyện tranh 3 thùng mỗi thùng 90 cuốn = 270 $\\rightarrow$ tổng 720 cuốn. $720 : 9 = 80$ cuốn):\nSửa: 2 thùng truyện tranh, mỗi thùng có 135 cuốn $\\rightarrow 135 \\times 2 = 270$ cuốn.\nTổng số sách truyện: $450 + 270 = 720$ (cuốn)\nMỗi lớp nhận được số cuốn là:\n$720 : 9 = 80$ (cuốn)\nĐáp số: 80 cuốn.", "80 cuốn", 6, 1.5),
            make_essay(5, "Một hình vuông có chu vi bằng chu vi hình chữ nhật có chiều dài 18 cm và chiều rộng 10 cm. Tính diện tích của hình vuông đó.", "Bài giải:\nChu vi hình chữ nhật là:\n$(18 + 10) \\times 2 = 56$ (cm)\nChu vi hình vuông là 56 cm.\nCạnh của hình vuông là:\n$56 : 4 = 14$ (cm)\nDiện tích của hình vuông là:\n$14 \\times 14 = 196$ ($\\text{cm}^2$)\nĐáp số: 196 $\\text{cm}^2$.", "196 cm²", 6, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$Q = 125 \\times 37 + 125 \\times 63$", "Bài giải:\n$Q = 125 \\times (37 + 63) = 125 \\times 100 = 12 500$\nĐáp số: $Q = 12 500$", "Q = 12 500", 4, 1.0)
        ]
    }

    exams["th4_b6_test3"] = {
        "id": "th4_b6_test3",
        "lessonId": "th4_b6",
        "lessonNum": 6,
        "testNum": 3,
        "title": "Bài 6: Luyện tập chung Chủ đề 1 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 1",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 5 chục nghìn, 4 trăm và 3 chục viết là:", ["50 430", "54 300", "50 340", "54 030"], 0, "Viết là 50 430."),
            make_mc(2, "Số chẵn bé nhất có 5 chữ số khác nhau là:", ["10 234", "12 340", "10 000", "10 236"], 0, "10 234 là số chẵn bé nhất có 5 chữ số khác nhau."),
            make_mc(3, "Giá trị của biểu thức $a \\times 5 - 15$ với $a = 7$ là:", ["20", "25", "35", "15"], 0, "$7 \\times 5 - 15 = 35 - 15 = 20$."),
            make_mc(4, "Một đoàn tàu chở 5 toa hàng, mỗi toa 12 tấn ngô. Đã dỡ xuống 25 tấn, trên tàu còn lại:", ["35 tấn", "45 tấn", "30 tấn", "40 tấn"], 0, "$5 \\times 12 - 25 = 60 - 25 = 35$ tấn."),
            make_mc(5, "Số liền trước của số lẻ nhỏ nhất có 5 chữ số là:", ["10 000", "10 001", "9 999", "10 002"], 0, "Số lẻ nhỏ nhất có 5 chữ số là 10 001, số liền trước là 10 000."),
            make_mc(6, "Làm tròn số 94 620 đến hàng chục nghìn ta được số:", ["90 000", "100 000", "95 000", "94 000"], 0, "Hàng nghìn là 4 nên làm tròn thành 90 000.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $48 570 + 35 680$\nb) $90 400 - 38 250$", "Bài giải:\na) $48 570 + 35 680 = 84 250$\nb) $90 400 - 38 250 = 52 150$\nĐáp số: a) 84 250; b) 52 150", "a) 84 250; b) 52 150", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\na) $P = a \\times 7 + 45$ với $a = 15$\nb) $Q = (m - n) \\times 4$ với $m = 85, n = 35$", "Bài giải:\na) $15 \\times 7 + 45 = 105 + 45 = 150$\nb) $(85 - 35) \\times 4 = 50 \\times 4 = 200$\nĐáp số: a) 150; b) 200", "a) 150; b) 200", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 6 = 2500 \\times 4$", "Bài giải:\n$x : 6 = 10 000$\n$x = 10 000 \\times 6 = 60 000$\nĐáp số: $x = 60 000$", "x = 60 000", 4, 1.0),
            make_essay(4, "Một đội xe gồm 3 xe lớn chở được tất cả 18 tấn hàng và 2 xe nhỏ chở được tất cả 8 tấn hàng. Hỏi cả đội xe chở được bao nhiêu tấn hàng? Trung bình mỗi xe chở được bao nhiêu tấn hàng?", "Bài giải:\nCả đội xe chở được số tấn hàng là:\n$18 + 8 = 26$ (tấn)\nTổng số xe trong đội là:\n$3 + 2 = 5$ (xe)\n(Chỉnh số cho chia hết: 3 xe lớn chở 18 tấn, 2 xe nhỏ chở 12 tấn $\\rightarrow$ tổng 30 tấn hàng. $30 : 5 = 6$ tấn/xe).\nTính lại:\nCả đội xe chở được số tấn hàng là:\n$18 + 12 = 30$ (tấn)\nTổng số xe là:\n$3 + 2 = 5$ (xe)\nTrung bình mỗi xe chở được số tấn hàng là:\n$30 : 5 = 6$ (tấn)\nĐáp số: Cả đội: 30 tấn; Trung bình mỗi xe: 6 tấn.", "Cả đội: 30 tấn; Mỗi xe: 6 tấn", 6, 1.5),
            make_essay(5, "Một khu đất hình chữ nhật có chu vi là 160 m. Chiều dài bằng 50 m. Tính diện tích khu đất đó.", "Bài giải:\nNửa chu vi khu đất là:\n$160 : 2 = 80$ (m)\nChiều rộng khu đất là:\n$80 - 50 = 30$ (m)\nDiện tích khu đất là:\n$50 \\times 30 = 1500$ ($\\text{m}^2$)\nĐáp số: 1500 $\\text{m}^2$.", "1500 m²", 6, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$K = 35 \\times 4 + 35 \\times 6 + 35 \\times 90$", "Bài giải:\n$K = 35 \\times (4 + 6 + 90) = 35 \\times 100 = 3500$\nĐáp số: $K = 3500$", "K = 3500", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề thi Chủ đề 1 Toán 4: {len(ex)} (Kỳ vọng: 18 đề)")
