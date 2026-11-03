# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 3: SỐ CÓ NHIỀU CHỮ SỐ (PHẦN 1: BÀI 10 ĐẾN BÀI 13) - TOÁN 4 KNTT
Gồm 4 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 10: Số có sáu chữ số. Số 1 000 000 (th4_b10_test1, th4_b10_test2, th4_b10_test3)
- Bài 11: Hàng và lớp (th4_b11_test1, th4_b11_test2, th4_b11_test3)
- Bài 12: Các số trong phạm vi lớp triệu (th4_b12_test1, th4_b12_test2, th4_b12_test3)
- Bài 13: Làm tròn số đến hàng trăm nghìn (th4_b13_test1, th4_b13_test2, th4_b13_test3)
Tổng cộng: 12 đề kiểm tra chất lượng cao, độc lập 100%.
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

def get_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 10: SỐ CÓ SÁU CHỮ SỐ. SỐ 1 000 000
    # =========================================================================
    exams["th4_b10_test1"] = {
        "id": "th4_b10_test1",
        "lessonId": "th4_b10",
        "lessonNum": 10,
        "testNum": 1,
        "title": "Bài 10: Số có sáu chữ số. Số 1 000 000 - Đề số 1",
        "topic": "Số có sáu chữ số. Số 1 000 000",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 5 trăm nghìn, 7 chục nghìn, 3 nghìn, 4 trăm và 8 đơn vị được viết là:", [
                "573 408",
                "573 480",
                "570 348",
                "57 348"
            ], 0, "Viết theo thứ tự các hàng: 5 trăm nghìn, 7 chục nghìn, 3 nghìn, 4 trăm, 0 chục, 8 đơn vị là 573 408."),
            make_mc(2, "Số 1 000 000 đọc là gì và có bao nhiêu chữ số 0?", [
                "Một trăm nghìn, có 5 chữ số 0",
                "Một triệu, có 6 chữ số 0",
                "Mười triệu, có 7 chữ số 0",
                "Một triệu, có 5 chữ số 0"
            ], 1, "Số 1 000 000 đọc là một triệu, gồm chữ số 1 và 6 chữ số 0 theo sau."),
            make_mc(3, "Số liền sau của số 999 999 là số nào?", [
                "999 998",
                "1 000 000",
                "100 000",
                "1 000 001"
            ], 1, "999 999 + 1 = 1 000 000 (Một triệu)."),
            make_mc(4, "Số 428 519 có chữ số thuộc hàng trăm nghìn là:", [
                "4",
                "2",
                "8",
                "5"
            ], 0, "Chữ số hàng trăm nghìn của 428 519 là 4."),
            make_mc(5, "Số bé nhất có sáu chữ số khác nhau là:", [
                "100 000",
                "102 345",
                "123 456",
                "102 354"
            ], 1, "Chữ số đầu tiên là 1, chữ số tiếp theo là 0, sau đó là 2, 3, 4, 5. Vậy số đó là 102 345."),
            make_mc(6, "10 trăm nghìn được gọi là:", [
                "Mười nghìn",
                "Một trăm nghìn",
                "Một triệu",
                "Mười triệu"
            ], 2, "10 trăm nghìn = 1 000 000 (một triệu).")
        ],
        "part2": [
            make_essay(1, "Viết và đọc số gồm 8 trăm nghìn, 2 chục nghìn, 9 trăm và 5 đơn vị.",
                       "Lời giải:\n- Viết số: 820 905.\n- Đọc số: Tám trăm hai mươi nghìn chín trăm linh năm.\nĐáp số: 820 905; Tám trăm hai mươi nghìn chín trăm linh năm.",
                       "820 905; Tám trăm hai mươi nghìn chín trăm linh năm", 4, 1.0),
            make_essay(2, "Viết số 645 280 thành tổng giá trị các hàng (trăm nghìn, chục nghìn, nghìn, trăm, chục, đơn vị).",
                       "Lời giải:\nTa có:\n645 280 = 600 000 + 40 000 + 5 000 + 200 + 80\nĐáp số: 600 000 + 40 000 + 5 000 + 200 + 80.",
                       "600 000 + 40 000 + 5 000 + 200 + 80", 4, 1.0),
            make_essay(3, "Một trang trại gà thu hoạch được 999 990 quả trứng trong một năm. Năm sau trang trại thu hoạch thêm 10 quả trứng nữa. Hỏi tổng số trứng sau khi thu hoạch thêm là bao nhiêu quả? Số đó đọc là gì?",
                       "Lời giải:\nTổng số trứng trang trại thu hoạch được là:\n999 990 + 10 = 1 000 000 (quả trứng)\nSố 1 000 000 đọc là: Một triệu.\nĐáp số: 1 000 000 quả trứng; Một triệu.",
                       "1 000 000 quả trứng; Một triệu", 4, 1.0),
            make_essay(4, "Từ sáu thẻ số: 4, 0, 7, 2, 5, 8. Em hãy lập:\na) Số lớn nhất có sáu chữ số khác nhau từ các thẻ trên.\nb) Số bé nhất có sáu chữ số khác nhau từ các thẻ trên.",
                       "Lời giải:\na) Để lập số lớn nhất có sáu chữ số khác nhau, ta xếp các chữ số từ lớn đến bé: 8, 7, 5, 4, 2, 0. Ta được số: 875 420.\nb) Để lập số bé nhất, chữ số hàng trăm nghìn bé nhất khác 0 là 2, tiếp theo là 0, 4, 5, 7, 8. Ta được số: 204 578.\nĐáp số: a) 875 420; b) 204 578.",
                       "a) 875 420; b) 204 578", 5, 1.5),
            make_essay(5, "Một thư viện thành phố có 520 000 cuốn sách giáo khoa và 380 000 cuốn sách tham khảo. Vừa qua thư viện nhập thêm 100 000 cuốn truyện thiếu nhi. Hỏi hiện nay thư viện có tất cả bao nhiêu cuốn sách? Số đó có phải là số 1 000 000 không?",
                       "Lời giải:\nTổng số sách ban đầu của thư viện là:\n520 000 + 380 000 = 900 000 (cuốn sách)\nHiện nay thư viện có tất cả số cuốn sách là:\n900 000 + 100 000 = 1 000 000 (cuốn sách)\nSố đó chính là số 1 000 000 (Một triệu).\nĐáp số: 1 000 000 cuốn sách; Đúng là số 1 000 000.",
                       "1 000 000 cuốn sách; Đúng là số 1 000 000", 5, 1.5),
            make_essay(6, "Tìm số liền trước và số liền sau của số 700 000.",
                       "Lời giải:\n- Số liền trước của 700 000 là: 700 000 - 1 = 699 999.\n- Số liền sau của 700 000 là: 700 000 + 1 = 700 001.\nĐáp số: Số liền trước: 699 999; Số liền sau: 700 001.",
                       "Liền trước: 699 999; Liền sau: 700 001", 4, 1.0)
        ]
    }

    exams["th4_b10_test2"] = {
        "id": "th4_b10_test2",
        "lessonId": "th4_b10",
        "lessonNum": 10,
        "testNum": 2,
        "title": "Bài 10: Số có sáu chữ số. Số 1 000 000 - Đề số 2",
        "topic": "Số có sáu chữ số. Số 1 000 000",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số 305 060 được đọc là:", [
                "Ba trăm linh năm nghìn sáu mươi",
                "Ba mươi lăm nghìn không trăm sáu mươi",
                "Ba trăm linh năm nghìn không trăm sáu mươi",
                "Ba trăm năm mươi nghìn sáu mươi"
            ], 2, "305 060 đọc là: Ba trăm linh năm nghìn không trăm sáu mươi."),
            make_mc(2, "Số lớn nhất có sáu chữ số là số nào?", [
                "100 000",
                "999 999",
                "1 000 000",
                "987 654"
            ], 1, "Số lớn nhất có sáu chữ số là 999 999."),
            make_mc(3, "Chữ số 7 trong số 714 250 có giá trị là:", [
                "7 000",
                "70 000",
                "700 000",
                "7 000 000"
            ], 2, "Chữ số 7 đứng ở hàng trăm nghìn nên có giá trị là 700 000."),
            make_mc(4, "Một triệu gấp một trăm nghìn bao nhiêu lần?", [
                "5 lần",
                "10 lần",
                "100 lần",
                "1 000 lần"
            ], 1, "1 000 000 : 100 000 = 10 (lần)."),
            make_mc(5, "Số gồm 9 trăm nghìn và 9 đơn vị viết là:", [
                "900 009",
                "909 000",
                "900 090",
                "990 000"
            ], 0, "Hàng trăm nghìn là 9, hàng đơn vị là 9, các hàng khác là 0: 900 009."),
            make_mc(6, "Dãy số: 999 997, 999 998, 999 999, ... Số tiếp theo là:", [
                "999 990",
                "1 000 000",
                "1 000 001",
                "100 000"
            ], 1, "Đếm thêm 1 đơn vị liên tiếp: 999 999 + 1 = 1 000 000.")
        ],
        "part2": [
            make_essay(1, "Viết các số sau:\na) Bốn trăm năm mươi nghìn bảy trăm ba mươi.\nb) Tám trăm linh hai nghìn không trăm linh tư.",
                       "Lời giải:\na) Số 'Bốn trăm năm mươi nghìn bảy trăm ba mươi' viết là: 450 730.\nb) Số 'Tám trăm linh hai nghìn không trăm linh tư' viết là: 802 004.\nĐáp số: a) 450 730; b) 802 004.",
                       "a) 450 730; b) 802 004", 4, 1.0),
            make_essay(2, "Số 836 154 có chữ số 8 thuộc hàng nào? Chữ số 3 thuộc hàng nào? Nêu giá trị của mỗi chữ số đó.",
                       "Lời giải:\n- Chữ số 8 thuộc hàng trăm nghìn, có giá trị là 800 000.\n- Chữ số 3 thuộc hàng chục nghìn, có giá trị là 30 000.\nĐáp số: 8 thuộc hàng trăm nghìn (giá trị 800 000); 3 thuộc hàng chục nghìn (giá trị 30 000).",
                       "8 thuộc hàng trăm nghìn (800 000); 3 thuộc hàng chục nghìn (30 000)", 4, 1.0),
            make_essay(3, "Một công ty xi măng tháng Một sản xuất được 450 000 bao xi măng, tháng Hai sản xuất được 550 000 bao xi măng. Hỏi trong cả hai tháng công ty sản xuất được bao nhiêu bao xi măng? Viết kết quả dưới dạng số có 7 chữ số.",
                       "Lời giải:\nCả hai tháng công ty sản xuất được số bao xi măng là:\n450 000 + 550 000 = 1 000 000 (bao)\nSố 1 000 000 là số có 7 chữ số (gồm 1 chữ số 1 và 6 chữ số 0).\nĐáp số: 1 000 000 bao xi măng.",
                       "1 000 000 bao xi măng", 4, 1.0),
            make_essay(4, "Cho các chữ số 9, 1, 0, 4, 3, 6. Hãy:\na) Viết số chẵn lớn nhất có sáu chữ số khác nhau từ các chữ số trên.\nb) Viết số lẻ bé nhất có sáu chữ số khác nhau từ các chữ số trên.",
                       "Lời giải:\na) Để số là số chẵn lớn nhất, chữ số tận cùng có thể là 0, 4, 6. Ta chọn hàng tận cùng là 0 để các hàng cao nhận các số lớn nhất: 964 310.\nb) Để số là số lẻ bé nhất, hàng tận cùng phải là chữ số lẻ (1, 3, 9). Chọn hàng đơn vị là 9 để các hàng đầu bé nhất: chữ số trăm nghìn là 1, tiếp theo là 0, 3, 4, 6, 9. Ta được số: 103 469.\nĐáp số: a) 964 310; b) 103 469.",
                       "a) 964 310; b) 103 469", 5, 1.5),
            make_essay(5, "Một khu dân cư có 3 tổ dân phố. Tổ một có 235 000 người, tổ hai có 315 000 người, tổ ba có số người bằng tổng số người của tổ một và tổ hai bớt đi 150 000 người. Hỏi cả ba tổ dân phố có tất cả bao nhiêu người?",
                       "Lời giải:\nTổng số người của tổ một và tổ hai là:\n235 000 + 315 000 = 550 000 (người)\nSố người của tổ ba là:\n550 000 - 150 000 = 400 000 (người)\nCả ba tổ dân phố có tất cả số người là:\n550 000 + 400 000 = 950 000 (người)\nĐáp số: 950 000 người.",
                       "950 000 người", 5, 1.5),
            make_essay(6, "Viết số tự nhiên thích hợp vào chỗ chấm: 300 000 + 80 000 + 500 + 7 = ...",
                       "Lời giải:\nTa thực hiện cộng các giá trị:\n300 000 + 80 000 + 500 + 7 = 380 507\nĐáp số: 380 507.",
                       "380 507", 4, 1.0)
        ]
    }

    exams["th4_b10_test3"] = {
        "id": "th4_b10_test3",
        "lessonId": "th4_b10",
        "lessonNum": 10,
        "testNum": 3,
        "title": "Bài 10: Số có sáu chữ số. Số 1 000 000 - Đề số 3",
        "topic": "Số có sáu chữ số. Số 1 000 000",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số bé nhất có sáu chữ số là số nào?", [
                "100 000",
                "111 111",
                "102 345",
                "100 001"
            ], 0, "Số bé nhất có sáu chữ số là 100 000."),
            make_mc(2, "Số 1 000 000 là số liền sau của số nào?", [
                "99 999",
                "999 999",
                "1 000 001",
                "900 000"
            ], 1, "Số liền sau của 999 999 là 1 000 000."),
            make_mc(3, "Trong số 582 341, chữ số 8 có giá trị lớn hơn chữ số 2 bao nhiêu đơn vị?", [
                "6 đơn vị",
                "6 000 đơn vị",
                "78 000 đơn vị",
                "80 000 đơn vị"
            ], 2, "Chữ số 8 có giá trị 80 000; chữ số 2 có giá trị 2 000. Hiệu là: 80 000 - 2 000 = 78 000."),
            make_mc(4, "Số gồm 7 trăm nghìn, 4 nghìn và 6 đơn vị viết là:", [
                "740 006",
                "704 006",
                "704 060",
                "74 006"
            ], 1, "Hàng trăm nghìn là 7, chục nghìn là 0, hàng nghìn là 4, hàng trăm là 0, chục là 0, đơn vị là 6: 704 006."),
            make_mc(5, "Đọc số 600 000:", [
                "Sáu mươi nghìn",
                "Sáu trăm nghìn",
                "Sáu triệu",
                "Sáu trăm"
            ], 1, "600 000 đọc là: Sáu trăm nghìn."),
            make_mc(6, "Bao nhiêu số 100 000 cộng lại thì bằng 1 000 000?", [
                "5 số",
                "10 số",
                "50 số",
                "100 số"
            ], 1, "10 x 100 000 = 1 000 000.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) 200 000, 300 000, 400 000, ..., ..., 700 000.\nb) 999 996, 999 997, 999 998, ..., ...",
                       "Lời giải:\na) Dãy số đếm thêm 100 000: 200 000, 300 000, 400 000, 500 000, 600 000, 700 000.\nb) Dãy số đếm thêm 1 đơn vị: 999 996, 999 997, 999 998, 999 999, 1 000 000.\nĐáp số: a) 500 000, 600 000; b) 999 999, 1 000 000.",
                       "a) 500 000, 600 000; b) 999 999, 1 000 000", 4, 1.0),
            make_essay(2, "Phân tích số 918 305 thành tổng theo cấu tạo thập phân.",
                       "Lời giải:\nTa có:\n918 305 = 900 000 + 10 000 + 8 000 + 300 + 5\nĐáp số: 900 000 + 10 000 + 8 000 + 300 + 5.",
                       "900 000 + 10 000 + 8 000 + 300 + 5", 4, 1.0),
            make_essay(3, "Một nhà máy in dự kiến in 1 000 000 cuốn vở cho năm học mới. Đợt một nhà máy đã in được 340 000 cuốn vở, đợt hai in được 460 000 cuốn vở. Hỏi nhà máy còn phải in bao nhiêu cuốn vở nữa để hoàn thành kế hoạch?",
                       "Lời giải:\nCả hai đợt nhà máy đã in được số cuốn vở là:\n340 000 + 460 000 = 800 000 (cuốn vở)\nNhà máy còn phải in số cuốn vở nữa là:\n1 000 000 - 800 000 = 200 000 (cuốn vở)\nĐáp số: 200 000 cuốn vở.",
                       "200 000 cuốn vở", 4, 1.0),
            make_essay(4, "Tìm một số có sáu chữ số, biết rằng chữ số hàng trăm nghìn là 7, chữ số hàng đơn vị là 3 và các chữ số còn lại đều là 0. Số đó hơn số 700 000 bao nhiêu đơn vị?",
                       "Lời giải:\nSố có sáu chữ số thỏa mãn điều kiện đề bài là: 700 003.\nSố đó hơn số 700 000 số đơn vị là:\n700 003 - 700 000 = 3 (đơn vị)\nĐáp số: Số đó là 700 003; hơn 3 đơn vị.",
                       "Số 700 003; hơn 3 đơn vị", 5, 1.5),
            make_essay(5, "Một quỹ khuyến học có 850 000 đồng. Hội phụ huynh ủng hộ thêm 150 000 đồng. Sau đó quỹ đã trao 10 suất học bổng, mỗi suất trị giá 80 000 đồng cho các em học sinh vượt khó. Hỏi quỹ khuyến học còn lại bao nhiêu tiền?",
                       "Lời giải:\nTổng số tiền quỹ khuyến học có sau khi được ủng hộ là:\n850 000 + 150 000 = 1 000 000 (đồng)\nSố tiền đã trao cho 10 suất học bổng là:\n80 000 x 10 = 800 000 (đồng)\nQuỹ khuyến học còn lại số tiền là:\n1 000 000 - 800 000 = 200 000 (đồng)\nĐáp số: 200 000 đồng.",
                       "200 000 đồng", 5, 1.5),
            make_essay(6, "Viết số lớn nhất có 6 chữ số khác nhau có chữ số hàng trăm nghìn là 9 và chữ số hàng đơn vị là 0.",
                       "Lời giải:\nĐể số là lớn nhất, các chữ số ở các hàng chục nghìn, nghìn, trăm, chục phải lần lượt nhận các giá trị lớn nhất còn lại khác nhau: 8, 7, 6, 5.\nVậy số đó là: 987 650.\nĐáp số: 987 650.",
                       "987 650", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 11: HÀNG VÀ LỚP
    # =========================================================================
    exams["th4_b11_test1"] = {
        "id": "th4_b11_test1",
        "lessonId": "th4_b11",
        "lessonNum": 11,
        "testNum": 1,
        "title": "Bài 11: Hàng và lớp - Đề số 1",
        "topic": "Hàng và lớp",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Lớp đơn vị gồm những hàng nào?", [
                "Hàng đơn vị, hàng chục, hàng trăm",
                "Hàng nghìn, hàng chục nghìn, hàng trăm nghìn",
                "Hàng triệu, hàng chục triệu, hàng trăm triệu",
                "Hàng chục, hàng trăm, hàng nghìn"
            ], 0, "Lớp đơn vị gồm ba hàng: hàng đơn vị, hàng chục, hàng trăm."),
            make_mc(2, "Lớp nghìn gồm những hàng nào?", [
                "Hàng đơn vị, hàng chục, hàng trăm",
                "Hàng nghìn, hàng chục nghìn, hàng trăm nghìn",
                "Hàng triệu, hàng chục triệu",
                "Hàng trăm nghìn, hàng triệu"
            ], 1, "Lớp nghìn gồm ba hàng: hàng nghìn, hàng chục nghìn, hàng trăm nghìn."),
            make_mc(3, "Trong số 654 321, các chữ số thuộc lớp nghìn là:", [
                "3, 2, 1",
                "6, 5, 4",
                "6, 3, 1",
                "5, 4, 3"
            ], 1, "Lớp nghìn gồm các chữ số ở hàng nghìn (4), chục nghìn (5), trăm nghìn (6): đó là 6, 5, 4."),
            make_mc(4, "Chữ số 8 trong số 482 105 thuộc hàng nào, lớp nào?", [
                "Hàng nghìn, lớp đơn vị",
                "Hàng chục nghìn, lớp nghìn",
                "Hàng trăm nghìn, lớp nghìn",
                "Hàng trăm, lớp đơn vị"
            ], 1, "Chữ số 8 đứng ở hàng chục nghìn, thuộc lớp nghìn."),
            make_mc(5, "Số nào dưới đây có chữ số hàng trăm bằng 7 và thuộc lớp đơn vị?", [
                "712 345",
                "458 729",
                "371 450",
                "123 457"
            ], 1, "Trong số 458 729, chữ số hàng trăm là 7 thuộc lớp đơn vị."),
            make_mc(6, "Giá trị của chữ số 5 trong số 350 482 là:", [
                "50",
                "500",
                "5 000",
                "50 000"
            ], 3, "Chữ số 5 ở hàng chục nghìn nên có giá trị là 50 000.")
        ],
        "part2": [
            make_essay(1, "Cho số 729 416. Hãy cho biết:\na) Các chữ số thuộc lớp đơn vị là những chữ số nào?\nb) Các chữ số thuộc lớp nghìn là những chữ số nào?",
                       "Lời giải:\na) Các chữ số thuộc lớp đơn vị (gồm hàng đơn vị, chục, trăm) là: 4, 1, 6.\nb) Các chữ số thuộc lớp nghìn (gồm hàng nghìn, chục nghìn, trăm nghìn) là: 7, 2, 9.\nĐáp số: a) 4, 1, 6; b) 7, 2, 9.",
                       "a) 4, 1, 6; b) 7, 2, 9", 4, 1.0),
            make_essay(2, "Xác định hàng và lớp của chữ số 9 trong mỗi số sau:\na) 193 450.\nb) 409 218.",
                       "Lời giải:\na) Trong số 193 450, chữ số 9 thuộc hàng chục nghìn, lớp nghìn.\nb) Trong số 409 218, chữ số 9 thuộc hàng nghìn, lớp nghìn.\nĐáp số: a) Hàng chục nghìn, lớp nghìn; b) Hàng nghìn, lớp nghìn.",
                       "a) Hàng chục nghìn, lớp nghìn; b) Hàng nghìn, lớp nghìn", 4, 1.0),
            make_essay(3, "Viết số có sáu chữ số biết lớp nghìn gồm các chữ số 3, 8, 5 (theo thứ tự từ hàng cao đến hàng thấp) và lớp đơn vị gồm các chữ số 0, 7, 2 (theo thứ tự từ hàng cao đến hàng thấp).",
                       "Lời giải:\n- Lớp nghìn gồm 3 trăm nghìn, 8 chục nghìn, 5 nghìn: 385 nghìn.\n- Lớp đơn vị gồm 0 trăm, 7 chục, 2 đơn vị: 072.\nSố cần viết là: 385 072.\nĐáp số: 385 072.",
                       "385 072", 4, 1.0),
            make_essay(4, "Một số có sáu chữ số có chữ số hàng trăm nghìn gấp đôi chữ số hàng chục nghìn. Chữ số hàng chục nghìn là 4. Các chữ số ở lớp đơn vị đều là 0, chữ số hàng nghìn là 5. Hãy tìm số đó và viết số đó thành tổng các lớp.",
                       "Lời giải:\nChữ số hàng chục nghìn là 4.\nChữ số hàng trăm nghìn là: 4 x 2 = 8.\nChữ số hàng nghìn là 5.\nLớp đơn vị gồm các chữ số 0 nên có 0 trăm, 0 chục, 0 đơn vị.\nSố đó là: 845 000.\nViết thành tổng các lớp: 845 000 = 845 nghìn + 0 đơn vị (hoặc 800 000 + 40 000 + 5 000).\nĐáp số: 845 000.",
                       "845 000", 5, 1.5),
            make_essay(5, "Cho số 638 214. Nếu xóa đi chữ số thuộc hàng trăm nghìn thì số mới nhận được có giá trị giảm đi bao nhiêu đơn vị so với số ban đầu?",
                       "Lời giải:\nTrong số 638 214, chữ số hàng trăm nghìn là 6, có giá trị là 600 000.\nKhi xóa đi chữ số hàng trăm nghìn (chữ số 6), ta được số mới là: 38 214.\nSố mới giảm đi số đơn vị so với số ban đầu là:\n638 214 - 38 214 = 600 000 (đơn vị)\nĐáp số: 600 000 đơn vị.",
                       "600 000 đơn vị", 5, 1.5),
            make_essay(6, "Tìm giá trị của chữ số 3 trong số 835 120 và giá trị của chữ số 3 trong số 412 305. Hỏi giá trị chữ số 3 ở số thứ nhất gấp mấy lần giá trị chữ số 3 ở số thứ hai?",
                       "Lời giải:\n- Giá trị của chữ số 3 trong số 835 120 là 30 000.\n- Giá trị của chữ số 3 trong số 412 305 là 300.\nSố lần gấp là:\n30 000 : 300 = 100 (lần)\nĐáp số: 100 lần.",
                       "100 lần", 4, 1.0)
        ]
    }

    exams["th4_b11_test2"] = {
        "id": "th4_b11_test2",
        "lessonId": "th4_b11",
        "lessonNum": 11,
        "testNum": 2,
        "title": "Bài 11: Hàng và lớp - Đề số 2",
        "topic": "Hàng và lớp",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Mỗi lớp gồm có mấy hàng?", [
                "2 hàng",
                "3 hàng",
                "4 hàng",
                "5 hàng"
            ], 1, "Mỗi lớp gồm đúng 3 hàng (ví dụ lớp đơn vị gồm: hàng đơn vị, chục, trăm)."),
            make_mc(2, "Số 526 914 có lớp đơn vị gồm các chữ số:", [
                "5, 2, 6",
                "9, 1, 4",
                "5, 9, 4",
                "2, 6, 1"
            ], 1, "Lớp đơn vị gồm 9 trăm, 1 chục, 4 đơn vị: các chữ số 9, 1, 4."),
            make_mc(3, "Chữ số 4 trong số 941 230 có giá trị là bao nhiêu?", [
                "400",
                "4 000",
                "40 000",
                "400 000"
            ], 2, "Chữ số 4 đứng ở hàng chục nghìn nên có giá trị là 40 000."),
            make_mc(4, "Số nào dưới đây có chữ số 6 thuộc hàng trăm nghìn?", [
                "162 450",
                "612 450",
                "346 200",
                "500 600"
            ], 1, "Số 612 450 có chữ số 6 đứng ở hàng trăm nghìn."),
            make_mc(5, "Số có lớp nghìn là 705 và lớp đơn vị là 042 viết là:", [
                "705 420",
                "750 042",
                "705 042",
                "705 402"
            ], 2, "Viết ghép lớp nghìn và lớp đơn vị: 705 042."),
            make_mc(6, "Trong số 888 888, chữ số 8 thuộc hàng trăm nghìn có giá trị gấp bao nhiêu lần chữ số 8 thuộc hàng trăm?", [
                "10 lần",
                "100 lần",
                "1 000 lần",
                "10 000 lần"
            ], 2, "Chữ số hàng trăm nghìn có giá trị 800 000, chữ số hàng trăm có giá trị 800. 800 000 : 800 = 1 000 lần.")
        ],
        "part2": [
            make_essay(1, "Ghi rõ giá trị của từng chữ số trong số 415 672 theo mẫu: Chữ số 4 có giá trị là 400 000.",
                       "Lời giải:\n- Chữ số 4 có giá trị là 400 000.\n- Chữ số 1 có giá trị là 10 000.\n- Chữ số 5 có giá trị là 5 000.\n- Chữ số 6 có giá trị là 600.\n- Chữ số 7 có giá trị là 70.\n- Chữ số 2 có giá trị là 2.\nĐáp số: 400 000; 10 000; 5 000; 600; 70; 2.",
                       "400 000; 10 000; 5 000; 600; 70; 2", 4, 1.0),
            make_essay(2, "Viết số tự nhiên biết:\na) Lớp nghìn gồm các chữ số 6, 0, 8 và lớp đơn vị gồm các chữ số 5, 2, 1.\nb) Lớp nghìn gồm các chữ số 9, 3, 0 và lớp đơn vị gồm các chữ số 0, 0, 7.",
                       "Lời giải:\na) Ghép lớp nghìn và lớp đơn vị ta được số: 608 521.\nb) Ghép lớp nghìn và lớp đơn vị ta được số: 930 007.\nĐáp số: a) 608 521; b) 930 007.",
                       "a) 608 521; b) 930 007", 4, 1.0),
            make_essay(3, "Cho số 518 392. Hãy đổi chỗ hai chữ số nào để chữ số 9 có giá trị bằng 90 000?",
                       "Lời giải:\nĐể chữ số 9 có giá trị bằng 90 000 thì chữ số 9 phải đứng ở hàng chục nghìn.\nHiện tại chữ số 9 đang ở hàng chục, và chữ số ở hàng chục nghìn đang là 1.\nDo đó, ta cần đổi chỗ chữ số 9 và chữ số 1 cho nhau.\nKhi đó ta được số mới là: 598 312.\nĐáp số: Đổi chỗ chữ số 9 và chữ số 1.",
                       "Đổi chỗ chữ số 9 và chữ số 1", 4, 1.0),
            make_essay(4, "Một trường học có mã số định danh là một số có sáu chữ số. Biết lớp nghìn là số lớn nhất có 3 chữ số khác nhau, lớp đơn vị là số bé nhất có 3 chữ số khác nhau. Hỏi mã số định danh của trường đó là số nào? Đọc số đó.",
                       "Lời giải:\nSố lớn nhất có 3 chữ số khác nhau là: 987 (lớp nghìn).\nSố bé nhất có 3 chữ số khác nhau là: 102 (lớp đơn vị).\nVậy mã số định danh của trường là: 987 102.\nĐọc số: Chín trăm tám mươi bảy nghìn một trăm linh hai.\nĐáp số: 987 102; Chín trăm tám mươi bảy nghìn một trăm linh hai.",
                       "987 102; Chín trăm tám mươi bảy nghìn một trăm linh hai", 5, 1.5),
            make_essay(5, "Cho số 463 825. Tìm hiệu giữa giá trị của chữ số thuộc hàng trăm nghìn và giá trị của chữ số thuộc hàng trăm của số đó.",
                       "Lời giải:\n- Chữ số thuộc hàng trăm nghìn là 4, có giá trị là 400 000.\n- Chữ số thuộc hàng trăm là 8, có giá trị là 800.\nHiệu giữa hai giá trị đó là:\n400 000 - 800 = 399 200\nĐáp số: 399 200.",
                       "399 200", 5, 1.5),
            make_essay(6, "Số có sáu chữ số mà tất cả các chữ số thuộc lớp nghìn đều là 5, tất cả các chữ số thuộc lớp đơn vị đều là 2. Viết số đó và đọc số đó.",
                       "Lời giải:\nSố đó viết là: 555 222.\nĐọc số: Năm trăm năm mươi lăm nghìn hai trăm hai mươi hai.\nĐáp số: 555 222; Năm trăm năm mươi lăm nghìn hai trăm hai mươi hai.",
                       "555 222; Năm trăm năm mươi lăm nghìn hai trăm hai mươi hai", 4, 1.0)
        ]
    }

    exams["th4_b11_test3"] = {
        "id": "th4_b11_test3",
        "lessonId": "th4_b11",
        "lessonNum": 11,
        "testNum": 3,
        "title": "Bài 11: Hàng và lớp - Đề số 3",
        "topic": "Hàng và lớp",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hàng nào sau đây KHÔNG thuộc lớp nghìn?", [
                "Hàng trăm nghìn",
                "Hàng chục nghìn",
                "Hàng nghìn",
                "Hàng trăm"
            ], 3, "Hàng trăm thuộc lớp đơn vị, không thuộc lớp nghìn."),
            make_mc(2, "Số 370 605 có chữ số 0 ở những hàng nào?", [
                "Hàng nghìn và hàng chục",
                "Hàng trăm và hàng đơn vị",
                "Hàng chục nghìn và hàng trăm",
                "Hàng trăm nghìn và hàng nghìn"
            ], 0, "Chữ số 0 thứ nhất ở hàng nghìn (370 nghìn) và chữ số 0 thứ hai ở hàng chục (605)."),
            make_mc(3, "Lớp đơn vị của số 824 159 là:", [
                "824",
                "159",
                "241",
                "859"
            ], 1, "Lớp đơn vị gồm 1 trăm, 5 chục, 9 đơn vị là 159."),
            make_mc(4, "Số nào dưới đây có chữ số 5 mang giá trị là 5 000?", [
                "512 340",
                "152 340",
                "125 340",
                "123 540"
            ], 2, "Trong số 125 340, chữ số 5 ở hàng nghìn nên có giá trị là 5 000."),
            make_mc(5, "Tổng 600 000 + 4 000 + 30 biểu diễn số nào?", [
                "640 030",
                "604 030",
                "604 300",
                "643 000"
            ], 1, "600 000 + 4 000 + 30 = 604 030."),
            make_mc(6, "Trong số có sáu chữ số, hàng cao nhất là hàng nào?", [
                "Hàng chục nghìn",
                "Hàng trăm nghìn",
                "Hàng triệu",
                "Hàng nghìn"
            ], 1, "Số có 6 chữ số thì hàng cao nhất là hàng trăm nghìn.")
        ],
        "part2": [
            make_essay(1, "Cho số 481 927. Hãy chỉ ra:\na) Chữ số hàng trăm nghìn và chữ số hàng trăm.\nb) Chữ số hàng chục nghìn và chữ số hàng chục.",
                       "Lời giải:\na) Chữ số hàng trăm nghìn là 4; chữ số hàng trăm là 9.\nb) Chữ số hàng chục nghìn là 8; chữ số hàng chục là 2.\nĐáp số: a) Hàng trăm nghìn: 4, hàng trăm: 9; b) Hàng chục nghìn: 8, hàng chục: 2.",
                       "a) 4 và 9; b) 8 và 2", 4, 1.0),
            make_essay(2, "Số 753 620 có tổng các chữ số thuộc lớp nghìn là bao nhiêu? Tổng các chữ số thuộc lớp đơn vị là bao nhiêu?",
                       "Lời giải:\n- Các chữ số thuộc lớp nghìn là: 7, 5, 3.\nTổng các chữ số thuộc lớp nghìn là: 7 + 5 + 3 = 15.\n- Các chữ số thuộc lớp đơn vị là: 6, 2, 0.\nTổng các chữ số thuộc lớp đơn vị là: 6 + 2 + 0 = 8.\nĐáp số: Lớp nghìn: 15; Lớp đơn vị: 8.",
                       "Lớp nghìn: 15; Lớp đơn vị: 8", 4, 1.0),
            make_essay(3, "Viết số tự nhiên có sáu chữ số, biết rằng số đó có lớp nghìn gồm ba chữ số giống nhau và bằng 6, lớp đơn vị gồm ba chữ số giống nhau và bằng 1. Đọc số đó.",
                       "Lời giải:\n- Lớp nghìn gồm ba chữ số 6: 666.\n- Lớp đơn vị gồm ba chữ số 1: 111.\nSố đó viết là: 666 111.\nĐọc số: Sáu trăm sáu mươi sáu nghìn một trăm mười một.\nĐáp số: 666 111; Sáu trăm sáu mươi sáu nghìn một trăm mười một.",
                       "666 111; Sáu trăm sáu mươi sáu nghìn một trăm mười một", 4, 1.0),
            make_essay(4, "Một cửa hàng sách trong tuần lễ đầu tiên bán được số sách là số có sáu chữ số. Biết chữ số hàng trăm nghìn là 2, chữ số hàng chục nghìn lớn hơn chữ số hàng trăm nghìn là 3 đơn vị, chữ số hàng nghìn là 5, còn lớp đơn vị gồm toàn chữ số 0. Hỏi cửa hàng đã bán được bao nhiêu cuốn sách? Đọc số đó.",
                       "Lời giải:\nChữ số hàng trăm nghìn là 2.\nChữ số hàng chục nghìn là: 2 + 3 = 5.\nChữ số hàng nghìn là 5.\nLớp đơn vị gồm ba chữ số 0: 000.\nVậy số sách cửa hàng đã bán là: 255 000 (cuốn sách).\nĐọc số: Hai trăm năm mươi lăm nghìn.\nĐáp số: 255 000 cuốn sách; Hai trăm năm mươi lăm nghìn.",
                       "255 000 cuốn sách; Hai trăm năm mươi lăm nghìn", 5, 1.5),
            make_essay(5, "Tìm số có sáu chữ số biết lớp nghìn là 420, chữ số hàng trăm là số lớn nhất có một chữ số, chữ số hàng chục kém chữ số hàng trăm 2 đơn vị và chữ số hàng đơn vị là 0.",
                       "Lời giải:\nLớp nghìn là 420.\nSố lớn nhất có một chữ số là 9, nên chữ số hàng trăm là 9.\nChữ số hàng chục là: 9 - 2 = 7.\nChữ số hàng đơn vị là 0.\nVậy số cần tìm là: 420 970.\nĐáp số: 420 970.",
                       "420 970", 5, 1.5),
            make_essay(6, "Viết số: 7 trăm nghìn, 5 chục nghìn, 2 trăm và 9 đơn vị thành số tự nhiên.",
                       "Lời giải:\nHàng trăm nghìn là 7, hàng chục nghìn là 5, hàng nghìn là 0, hàng trăm là 2, hàng chục là 0, hàng đơn vị là 9.\nSố cần viết là: 750 209.\nĐáp số: 750 209.",
                       "750 209", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 12: CÁC SỐ TRONG PHẠM VI LỚP TRIỆU
    # =========================================================================
    exams["th4_b12_test1"] = {
        "id": "th4_b12_test1",
        "lessonId": "th4_b12",
        "lessonNum": 12,
        "testNum": 1,
        "title": "Bài 12: Các số trong phạm vi lớp triệu - Đề số 1",
        "topic": "Các số trong phạm vi lớp triệu",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Lớp triệu gồm những hàng nào?", [
                "Hàng triệu, hàng chục triệu, hàng trăm triệu",
                "Hàng trăm, hàng chục, hàng đơn vị",
                "Hàng nghìn, hàng chục nghìn, hàng trăm nghìn",
                "Hàng triệu, hàng tỉ"
            ], 0, "Lớp triệu gồm ba hàng: hàng triệu, hàng chục triệu, hàng trăm triệu."),
            make_mc(2, "Số mười lăm triệu được viết là:", [
                "15 000",
                "150 000",
                "1 500 000",
                "15 000 000"
            ], 3, "Mười lăm triệu có lớp triệu là 15, các lớp nghìn và đơn vị đều là 0: 15 000 000."),
            make_mc(3, "Số 320 000 000 có bao nhiêu chữ số 0?", [
                "6 chữ số 0",
                "7 chữ số 0",
                "8 chữ số 0",
                "9 chữ số 0"
            ], 1, "Số 320 000 000 gồm chữ số 3, 2 và 7 chữ số 0 theo sau."),
            make_mc(4, "Chữ số 7 trong số 74 125 000 thuộc hàng nào?", [
                "Hàng triệu",
                "Hàng chục triệu",
                "Hàng trăm triệu",
                "Hàng trăm nghìn"
            ], 1, "Chữ số 7 đứng ở hàng chục triệu."),
            make_mc(5, "Số gồm 5 trăm triệu, 2 triệu và 6 nghìn viết là:", [
                "502 006 000",
                "520 060 000",
                "502 060 000",
                "52 006 000"
            ], 0, "Lớp triệu: 502, lớp nghìn: 006, lớp đơn vị: 000 -> 502 006 000."),
            make_mc(6, "Số nào dưới đây là số tròn trăm triệu?", [
                "10 000 000",
                "50 000 000",
                "300 000 000",
                "1 000 000 000"
            ], 2, "300 000 000 là ba trăm triệu (số tròn trăm triệu).")
        ],
        "part2": [
            make_essay(1, "Đọc các số sau:\na) 25 000 000.\nb) 412 000 000.",
                       "Lời giải:\na) Số 25 000 000 đọc là: Hai mươi lăm triệu.\nb) Số 412 000 000 đọc là: Bốn trăm mười hai triệu.\nĐáp số: a) Hai mươi lăm triệu; b) Bốn trăm mười hai triệu.",
                       "a) Hai mươi lăm triệu; b) Bốn trăm mười hai triệu", 4, 1.0),
            make_essay(2, "Viết các số sau:\na) Năm mươi triệu sáu trăm nghìn.\nb) Bảy trăm ba mươi triệu.",
                       "Lời giải:\na) Năm mươi triệu sáu trăm nghìn viết là: 50 600 000.\nb) Bảy trăm ba mươi triệu viết là: 730 000 000.\nĐáp số: a) 50 600 000; b) 730 000 000.",
                       "a) 50 600 000; b) 730 000 000", 4, 1.0),
            make_essay(3, "Cho số 856 214 000. Hãy xác định:\na) Các chữ số thuộc lớp triệu.\nb) Giá trị của chữ số 8 trong số đó.",
                       "Lời giải:\na) Các chữ số thuộc lớp triệu là: 8, 5, 6.\nb) Chữ số 8 đứng ở hàng trăm triệu nên có giá trị là: 800 000 000 (tám trăm triệu).\nĐáp số: a) 8, 5, 6; b) 800 000 000.",
                       "a) 8, 5, 6; b) 800 000 000", 4, 1.0),
            make_essay(4, "Dân số của một quốc gia là 98 000 000 người. Một năm sau dân số tăng thêm 1 000 000 người. Hỏi sau một năm dân số quốc gia đó là bao nhiêu người? Viết và đọc số dân đó.",
                       "Lời giải:\nSau một năm, dân số của quốc gia đó là:\n98 000 000 + 1 000 000 = 99 000 000 (người)\nSố 99 000 000 đọc là: Chín mươi chín triệu.\nĐáp số: 99 000 000 người; Chín mươi chín triệu.",
                       "99 000 000 người; Chín mươi chín triệu", 5, 1.5),
            make_essay(5, "Một dự án xây dựng cầu vượt có kinh phí giai đoạn 1 là 150 000 000 đồng, giai đoạn 2 là 250 000 000 đồng. Dự kiến giai đoạn 3 cần kinh phí gấp đôi giai đoạn 1. Hỏi tổng kinh phí dự kiến cho cả ba giai đoạn là bao nhiêu đồng?",
                       "Lời giải:\nKinh phí dự kiến của giai đoạn 3 là:\n150 000 000 x 2 = 300 000 000 (đồng)\nTổng kinh phí cho cả ba giai đoạn là:\n150 000 000 + 250 000 000 + 300 000 000 = 700 000 000 (đồng)\nĐáp số: 700 000 000 đồng.",
                       "700 000 000 đồng", 5, 1.5),
            make_essay(6, "Viết số tự nhiên biết số đó gồm 6 trăm triệu, 4 chục triệu, 8 trăm nghìn và 5 chục.",
                       "Lời giải:\nLớp triệu: 640 triệu; lớp nghìn: 800 nghìn; lớp đơn vị: 050.\nSố cần viết là: 640 800 050.\nĐáp số: 640 800 050.",
                       "640 800 050", 4, 1.0)
        ]
    }

    exams["th4_b12_test2"] = {
        "id": "th4_b12_test2",
        "lessonId": "th4_b12",
        "lessonNum": 12,
        "testNum": 2,
        "title": "Bài 12: Các số trong phạm vi lớp triệu - Đề số 2",
        "topic": "Các số trong phạm vi lớp triệu",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số nào dưới đây có chữ số 3 ở hàng trăm triệu?", [
                "35 000 000",
                "300 000 000",
                "3 000 000",
                "30 000 000"
            ], 1, "Số 300 000 000 có chữ số 3 ở hàng trăm triệu."),
            make_mc(2, "Số 100 000 000 đọc là:", [
                "Mười triệu",
                "Một trăm triệu",
                "Một tỉ",
                "Một trăm nghìn"
            ], 1, "100 000 000 đọc là: Một trăm triệu."),
            make_mc(3, "Số gồm 8 chục triệu và 5 triệu viết là:", [
                "85 000 000",
                "805 000 000",
                "8 500 000",
                "850 000"
            ], 0, "8 chục triệu và 5 triệu là 85 triệu = 85 000 000."),
            make_mc(4, "Trong số 245 618 300, chữ số thuộc hàng chục triệu là:", [
                "2",
                "4",
                "5",
                "6"
            ], 1, "Chữ số hàng chục triệu là 4."),
            make_mc(5, "Số tròn chục triệu liền trước số 50 000 000 là số nào?", [
                "40 000 000",
                "49 000 000",
                "49 999 999",
                "60 000 000"
            ], 0, "Số tròn chục triệu liền trước 50 000 000 là 40 000 000."),
            make_mc(6, "Một trăm triệu gồm bao nhiêu chục triệu?", [
                "5 chục triệu",
                "10 chục triệu",
                "100 chục triệu",
                "1 000 chục triệu"
            ], 1, "10 chục triệu = 1 trăm triệu = 100 000 000.")
        ],
        "part2": [
            make_essay(1, "Viết và đọc số gồm 3 trăm triệu, 7 chục triệu và 2 triệu.",
                       "Lời giải:\n- Lớp triệu gồm: 3 trăm triệu, 7 chục triệu, 2 triệu là 372 triệu.\n- Viết số: 372 000 000.\n- Đọc số: Ba trăm bảy mươi hai triệu.\nĐáp số: 372 000 000; Ba trăm bảy mươi hai triệu.",
                       "372 000 000; Ba trăm bảy mươi hai triệu", 4, 1.0),
            make_essay(2, "Số 680 450 000 có:\na) Lớp triệu gồm những chữ số nào?\nb) Lớp nghìn gồm những chữ số nào?",
                       "Lời giải:\na) Lớp triệu gồm các chữ số: 6, 8, 0.\nb) Lớp nghìn gồm các chữ số: 4, 5, 0.\nĐáp số: a) 6, 8, 0; b) 4, 5, 0.",
                       "a) 6, 8, 0; b) 4, 5, 0", 4, 1.0),
            make_essay(3, "Một doanh nghiệp công nghệ có doanh thu quý 1 là 120 000 000 đồng, doanh thu quý 2 là 180 000 000 đồng. Hỏi tổng doanh thu của doanh nghiệp trong 2 quý đó là bao nhiêu đồng? Đọc số tiền đó.",
                       "Lời giải:\nTổng doanh thu của doanh nghiệp trong 2 quý là:\n120 000 000 + 180 000 000 = 300 000 000 (đồng)\nSố 300 000 000 đọc là: Ba trăm triệu.\nĐáp số: 300 000 000 đồng; Ba trăm triệu đồng.",
                       "300 000 000 đồng; Ba trăm triệu đồng", 4, 1.0),
            make_essay(4, "Một ngân hàng xuất quỹ 3 lần tiền mặt. Lần thứ nhất xuất 200 000 000 đồng, lần thứ hai xuất ít hơn lần thứ nhất 50 000 000 đồng, lần thứ ba xuất gấp đôi lần thứ hai. Hỏi cả ba lần ngân hàng xuất bao nhiêu tiền mặt?",
                       "Lời giải:\nSố tiền xuất lần thứ hai là:\n200 000 000 - 50 000 000 = 150 000 000 (đồng)\nSố tiền xuất lần thứ ba là:\n150 000 000 x 2 = 300 000 000 (đồng)\nCả ba lần ngân hàng xuất số tiền là:\n200 000 000 + 150 000 000 + 300 000 000 = 650 000 000 (đồng)\nĐáp số: 650 000 000 đồng.",
                       "650 000 000 đồng", 5, 1.5),
            make_essay(5, "Tìm số tròn chục triệu lớn nhất có 8 chữ số và số tròn trăm triệu bé nhất có 9 chữ số. Tính tổng của hai số đó.",
                       "Lời giải:\n- Số tròn chục triệu lớn nhất có 8 chữ số là: 90 000 000 (chín mươi triệu).\n- Số tròn trăm triệu bé nhất có 9 chữ số là: 100 000 000 (một trăm triệu).\nTổng của hai số đó là:\n90 000 000 + 100 000 000 = 190 000 000\nĐáp số: 190 000 000.",
                       "190 000 000", 5, 1.5),
            make_essay(6, "Viết số tự nhiên thích hợp: 500 000 000 + 30 000 000 + 2 000 000 = ...",
                       "Lời giải:\nThực hiện cộng:\n500 000 000 + 30 000 000 + 2 000 000 = 532 000 000\nĐáp số: 532 000 000.",
                       "532 000 000", 4, 1.0)
        ]
    }

    exams["th4_b12_test3"] = {
        "id": "th4_b12_test3",
        "lessonId": "th4_b12",
        "lessonNum": 12,
        "testNum": 3,
        "title": "Bài 12: Các số trong phạm vi lớp triệu - Đề số 3",
        "topic": "Các số trong phạm vi lớp triệu",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số bé nhất có 9 chữ số là số nào?", [
                "100 000 000",
                "111 111 111",
                "999 999 999",
                "10 000 000"
            ], 0, "Số bé nhất có 9 chữ số là 100 000 000 (Một trăm triệu)."),
            make_mc(2, "Số 804 000 000 đọc là:", [
                "Tám mươi tư triệu",
                "Tám trăm linh bốn triệu",
                "Tám trăm bốn mươi triệu",
                "Tám trăm bốn triệu nghìn"
            ], 1, "804 000 000 đọc là: Tám trăm linh bốn triệu."),
            make_mc(3, "Giá trị của chữ số 6 trong số 625 000 000 là:", [
                "6 000 000",
                "60 000 000",
                "600 000 000",
                "600 000"
            ], 2, "Chữ số 6 đứng ở hàng trăm triệu nên có giá trị là 600 000 000."),
            make_mc(4, "Số gồm 2 trăm triệu và 5 chục nghìn viết là:", [
                "200 050 000",
                "250 000 000",
                "200 500 000",
                "20 050 000"
            ], 0, "Lớp triệu: 200, lớp nghìn: 050, lớp đơn vị: 000 -> 200 050 000."),
            make_mc(5, "Số tròn triệu liền sau số 99 000 000 là:", [
                "99 000 001",
                "100 000 000",
                "99 100 000",
                "100 000"
            ], 1, "99 000 000 + 1 000 000 = 100 000 000 (Một trăm triệu)."),
            make_mc(6, "Trong số 519 284 370, chữ số hàng triệu là chữ số nào?", [
                "5",
                "1",
                "9",
                "2"
            ], 2, "Chữ số hàng triệu là 9 (thuộc lớp triệu 519 triệu).")
        ],
        "part2": [
            make_essay(1, "Viết các số sau:\na) Chín trăm triệu.\nb) Tám mươi sáu triệu năm trăm nghìn.",
                       "Lời giải:\na) Chín trăm triệu viết là: 900 000 000.\nb) Tám mươi sáu triệu năm trăm nghìn viết là: 86 500 000.\nĐáp số: a) 900 000 000; b) 86 500 000.",
                       "a) 900 000 000; b) 86 500 000", 4, 1.0),
            make_essay(2, "Số 750 000 000 có bao nhiêu chữ số 0? Chữ số 7 có giá trị gấp mấy lần chữ số 5?",
                       "Lời giải:\n- Số 750 000 000 có 7 chữ số 0.\n- Chữ số 7 có giá trị là 700 000 000. Chữ số 5 có giá trị là 50 000 000.\nTa có: 700 000 000 : 50 000 000 = 14 (lần).\nĐáp số: Có 7 chữ số 0; gấp 14 lần.",
                       "7 chữ số 0; gấp 14 lần", 4, 1.0),
            make_essay(3, "Một tập đoàn nông nghiệp xuất khẩu cà phê trong năm qua đạt giá trị 450 000 000 đô la Mỹ. Năm nay dự kiến xuất khẩu đạt 550 000 000 đô la Mỹ. Hỏi cả hai năm dự kiến xuất khẩu đạt tổng cộng bao nhiêu đô la Mỹ? Viết và đọc kết quả đó.",
                       "Lời giải:\nCả hai năm tập đoàn dự kiến đạt tổng số đô la Mỹ là:\n450 000 000 + 550 000 000 = 1 000 000 000 (đô la Mỹ)\nSố 1 000 000 000 đọc là: Một tỉ.\nĐáp số: 1 000 000 000 đô la Mỹ; Một tỉ đô la Mỹ.",
                       "1 000 000 000 đô la Mỹ; Một tỉ đô la Mỹ", 4, 1.0),
            make_essay(4, "Một thành phố chi ngân sách cho ba công trình: Công trình thứ nhất 180 000 000 đồng, công trình thứ hai 220 000 000 đồng. Tổng kinh phí cả ba công trình là 600 000 000 đồng. Hỏi công trình thứ ba có kinh phí là bao nhiêu đồng?",
                       "Lời giải:\nTổng kinh phí của hai công trình đầu là:\n180 000 000 + 220 000 000 = 400 000 000 (đồng)\nKinh phí của công trình thứ ba là:\n600 000 000 - 400 000 000 = 200 000 000 (đồng)\nĐáp số: 200 000 000 đồng.",
                       "200 000 000 đồng", 5, 1.5),
            make_essay(5, "Viết số tròn triệu lớn nhất có 8 chữ số và số tròn triệu bé nhất có 8 chữ số. Tính hiệu của hai số đó.",
                       "Lời giải:\n- Số tròn triệu lớn nhất có 8 chữ số là: 99 000 000.\n- Số tròn triệu bé nhất có 8 chữ số là: 10 000 000.\nHiệu của hai số đó là:\n99 000 000 - 10 000 000 = 89 000 000\nĐáp số: 89 000 000.",
                       "89 000 000", 5, 1.5),
            make_essay(6, "Điền dấu thích hợp (>, <, =) vào chỗ chấm: 250 000 000 ... 200 000 000 + 50 000 000.",
                       "Lời giải:\nTa có:\n200 000 000 + 50 000 000 = 250 000 000\nVì 250 000 000 = 250 000 000 nên ta điền dấu '='.\nĐáp số: =.",
                       "=", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 13: LÀM TRÒN SỐ ĐẾN HÀNG TRĂM NGHÌN
    # =========================================================================
    exams["th4_b13_test1"] = {
        "id": "th4_b13_test1",
        "lessonId": "th4_b13",
        "lessonNum": 13,
        "testNum": 1,
        "title": "Bài 13: Làm tròn số đến hàng trăm nghìn - Đề số 1",
        "topic": "Làm tròn số đến hàng trăm nghìn",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khi làm tròn số đến hàng trăm nghìn, ta cần quan sát chữ số ở hàng nào?", [
                "Hàng chục nghìn",
                "Hàng nghìn",
                "Hàng trăm",
                "Hàng triệu"
            ], 0, "Khi làm tròn đến hàng trăm nghìn, ta so sánh chữ số ở hàng chục nghìn với 5."),
            make_mc(2, "Làm tròn số 342 500 đến hàng trăm nghìn ta được số nào?", [
                "300 000",
                "340 000",
                "400 000",
                "350 000"
            ], 0, "Chữ số hàng chục nghìn là 4 (< 5), nên làm tròn xuống ta được 300 000."),
            make_mc(3, "Làm tròn số 581 200 đến hàng trăm nghìn ta được số nào?", [
                "500 000",
                "580 000",
                "600 000",
                "590 000"
            ], 2, "Chữ số hàng chục nghìn là 8 (>= 5), nên làm tròn lên ta được 600 000."),
            make_mc(4, "Số nào dưới đây khi làm tròn đến hàng trăm nghìn thì được số 800 000?", [
                "725 000",
                "749 999",
                "763 000",
                "860 000"
            ], 2, "763 000 có chữ số hàng chục nghìn là 6 >= 5 nên làm tròn lên thành 800 000."),
            make_mc(5, "Làm tròn số 150 000 đến hàng trăm nghìn ta được số:", [
                "100 000",
                "150 000",
                "200 000",
                "300 000"
            ], 2, "Chữ số hàng chục nghìn là 5 (>= 5), nên làm tròn lên ta được 200 000."),
            make_mc(6, "Dân số một huyện là 218 450 người. Làm tròn số dân này đến hàng chục nghìn ta được:", [
                "210 000 người",
                "220 000 người",
                "200 000 người",
                "218 000 người"
            ], 1, "Chữ số hàng nghìn là 8 >= 5 nên làm tròn lên thành 220 000 người.")
        ],
        "part2": [
            make_essay(1, "Làm tròn các số sau đến hàng trăm nghìn:\na) 427 100.\nb) 674 800.",
                       "Lời giải:\na) Số 427 100 có chữ số hàng chục nghìn là 2 (2 < 5), nên làm tròn thành: 400 000.\nb) Số 674 800 có chữ số hàng chục nghìn là 7 (7 >= 5), nên làm tròn thành: 700 000.\nĐáp số: a) 400 000; b) 700 000.",
                       "a) 400 000; b) 700 000", 4, 1.0),
            make_essay(2, "Làm tròn số 835 620 đến:\na) Hàng nghìn.\nb) Hàng chục nghìn.\nc) Hàng trăm nghìn.",
                       "Lời giải:\na) Làm tròn đến hàng nghìn (xem hàng trăm là 6 >= 5): 836 000.\nb) Làm tròn đến hàng chục nghìn (xem hàng nghìn là 5 >= 5): 840 000.\nc) Làm tròn đến hàng trăm nghìn (xem hàng chục nghìn là 3 < 5): 800 000.\nĐáp số: a) 836 000; b) 840 000; c) 800 000.",
                       "a) 836 000; b) 840 000; c) 800 000", 4, 1.0),
            make_essay(3, "Một tỉnh có diện tích rừng trồng là 368 450 ha. Báo cáo thống kê yêu cầu làm tròn diện tích rừng này đến hàng trăm nghìn. Em hãy thực hiện làm tròn số liệu trên.",
                       "Lời giải:\nSố 368 450 có chữ số hàng trăm nghìn là 3, chữ số hàng chục nghìn là 6.\nVì 6 >= 5 nên ta làm tròn lên, cộng 1 vào chữ số hàng trăm nghìn và các hàng sau thành 0.\nSố được làm tròn là: 400 000 ha.\nĐáp số: 400 000 ha.",
                       "400 000 ha", 4, 1.0),
            make_essay(4, "Một nhà máy sản xuất bánh kẹo trong năm qua xuất xưởng được 524 800 hộp bánh và 478 200 hộp kẹo. Em hãy:\na) Tính tổng số hộp bánh và kẹo nhà máy đã sản xuất.\nb) Làm tròn tổng số hộp bánh kẹo đó đến hàng trăm nghìn.",
                       "Lời giải:\na) Tổng số hộp bánh và kẹo nhà máy đã sản xuất là:\n524 800 + 478 200 = 1 003 000 (hộp)\nb) Làm tròn số 1 003 000 đến hàng trăm nghìn:\nChữ số hàng trăm nghìn là 0, chữ số hàng chục nghìn là 0 (< 5) nên làm tròn thành: 1 000 000 hộp.\nĐáp số: a) 1 003 000 hộp; b) 1 000 000 hộp.",
                       "a) 1 003 000 hộp; b) 1 000 000 hộp", 5, 1.5),
            make_essay(5, "Tìm số tự nhiên lớn nhất và số tự nhiên bé nhất có sáu chữ số mà khi làm tròn đến hàng trăm nghìn thì được số 500 000.",
                       "Lời giải:\n- Để làm tròn đến hàng trăm nghìn được 500 000, số bé nhất phải có hàng trăm nghìn là 4 và hàng chục nghìn là 5, các hàng sau là 0: đó là 450 000.\n- Số lớn nhất phải có hàng trăm nghìn là 5 và hàng chục nghìn là 4, các hàng sau là 9: đó là 549 999.\nĐáp số: Bé nhất: 450 000; Lớn nhất: 549 999.",
                       "Bé nhất: 450 000; Lớn nhất: 549 999", 5, 1.5),
            make_essay(6, "Một cửa hàng sách bán được 185 200 cuốn tập trong học kì 1. Bác thủ kho báo cáo: 'Cửa hàng đã bán khoảng 200 000 cuốn tập'. Hỏi bác thủ kho đã làm tròn số sách đến hàng nào?",
                       "Lời giải:\nTừ 185 200 làm tròn thành 200 000 tức là chữ số hàng trăm nghìn từ 1 chuyển thành 2 (do hàng chục nghìn là 8 >= 5).\nVậy bác thủ kho đã làm tròn số sách đến hàng trăm nghìn.\nĐáp số: Hàng trăm nghìn.",
                       "Hàng trăm nghìn", 4, 1.0)
        ]
    }

    exams["th4_b13_test2"] = {
        "id": "th4_b13_test2",
        "lessonId": "th4_b13",
        "lessonNum": 13,
        "testNum": 2,
        "title": "Bài 13: Làm tròn số đến hàng trăm nghìn - Đề số 2",
        "topic": "Làm tròn số đến hàng trăm nghìn",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Làm tròn số 750 000 đến hàng trăm nghìn ta được kết quả là:", [
                "700 000",
                "750 000",
                "800 000",
                "900 000"
            ], 2, "Chữ số hàng chục nghìn là 5 >= 5 nên làm tròn lên thành 800 000."),
            make_mc(2, "Số 916 430 khi làm tròn đến hàng trăm nghìn ta được số:", [
                "900 000",
                "920 000",
                "1 000 000",
                "910 000"
            ], 0, "Chữ số hàng chục nghìn là 1 < 5 nên làm tròn xuống thành 900 000."),
            make_mc(3, "Có bao nhiêu chữ số ở hàng chục nghìn (từ 0 đến 9) làm cho một số được làm tròn xuống khi làm tròn đến hàng trăm nghìn?", [
                "4 chữ số",
                "5 chữ số",
                "6 chữ số",
                "10 chữ số"
            ], 1, "Có 5 chữ số: 0, 1, 2, 3, 4 sẽ làm tròn xuống."),
            make_mc(4, "Số nào dưới đây khi làm tròn đến hàng trăm nghìn KHÔNG được 600 000?", [
                "589 000",
                "612 000",
                "648 000",
                "652 000"
            ], 3, "652 000 có chữ số hàng chục nghìn là 5 nên làm tròn lên thành 700 000."),
            make_mc(5, "Quãng đường từ Hà Nội đến một điểm du lịch dài 394 500 m. Làm tròn đến hàng trăm nghìn mét ta được:", [
                "300 000 m",
                "390 000 m",
                "400 000 m",
                "500 000 m"
            ], 2, "Hàng chục nghìn là 9 >= 5 nên làm tròn lên thành 400 000 m."),
            make_mc(6, "Làm tròn số 273 400 đến hàng chục nghìn ta được:", [
                "270 000",
                "280 000",
                "300 000",
                "274 000"
            ], 0, "Chữ số hàng nghìn là 3 < 5 nên làm tròn thành 270 000.")
        ],
        "part2": [
            make_essay(1, "Thực hiện làm tròn các số sau đến hàng trăm nghìn:\na) 184 900.\nb) 936 250.",
                       "Lời giải:\na) Số 184 900 có hàng chục nghìn là 8 >= 5 nên làm tròn thành: 200 000.\nb) Số 936 250 có hàng chục nghìn là 3 < 5 nên làm tròn thành: 900 000.\nĐáp số: a) 200 000; b) 900 000.",
                       "a) 200 000; b) 900 000", 4, 1.0),
            make_essay(2, "Cho số 468 152. Hãy làm tròn số này đến:\na) Hàng chục nghìn.\nb) Hàng trăm nghìn.",
                       "Lời giải:\na) Làm tròn đến hàng chục nghìn: Chữ số hàng nghìn là 8 >= 5, ta được: 470 000.\nb) Làm tròn đến hàng trăm nghìn: Chữ số hàng chục nghìn là 6 >= 5, ta được: 500 000.\nĐáp số: a) 470 000; b) 500 000.",
                       "a) 470 000; b) 500 000", 4, 1.0),
            make_essay(3, "Năm ngoái một thành phố thu hút 647 800 lượt khách du lịch. Hãy làm tròn số lượt khách du lịch này đến hàng trăm nghìn để đưa vào bản tin tổng hợp cuối năm.",
                       "Lời giải:\nSố lượt khách du lịch là 647 800.\nChữ số hàng trăm nghìn là 6, chữ số hàng chục nghìn là 4.\nVì 4 < 5 nên ta làm tròn xuống, giữ nguyên chữ số 6 và thay các chữ số sau bằng 0.\nTa được số: 600 000 lượt khách.\nĐáp số: 600 000 lượt khách.",
                       "600 000 lượt khách", 4, 1.0),
            make_essay(4, "Một trang trại cam thu hoạch đợt 1 được 165 400 kg cam, đợt 2 thu hoạch được 238 600 kg cam. Hỏi:\na) Cả hai đợt trang trại thu hoạch được tất cả bao nhiêu ki-lô-gam cam?\nb) Làm tròn tổng số ki-lô-gam cam đó đến hàng trăm nghìn.",
                       "Lời giải:\na) Cả hai đợt trang trại thu hoạch được số ki-lô-gam cam là:\n165 400 + 238 600 = 404 000 (kg)\nb) Làm tròn số 404 000 đến hàng trăm nghìn:\nChữ số hàng chục nghìn là 0 (< 5) nên làm tròn xuống thành: 400 000 kg.\nĐáp số: a) 404 000 kg; b) 400 000 kg.",
                       "a) 404 000 kg; b) 400 000 kg", 5, 1.5),
            make_essay(5, "Bạn Minh viết một số có sáu chữ số. Khi làm tròn số đó đến hàng trăm nghìn bạn được 700 000. Biết rằng nếu làm tròn số đó đến hàng chục nghìn thì bạn được 740 000. Hỏi chữ số hàng trăm nghìn và chữ số hàng chục nghìn của số bạn Minh viết là những chữ số nào?",
                       "Lời giải:\n- Khi làm tròn đến hàng chục nghìn được 740 000 nên chữ số hàng trăm nghìn của số đó là 7 và chữ số hàng chục nghìn có thể là 3 hoặc 4.\n- Khi làm tròn đến hàng trăm nghìn được 700 000, số hàng chục nghìn phải bé hơn 5. Nếu là 4 thì làm tròn đến hàng trăm nghìn vẫn là 700 000.\nVậy chữ số hàng trăm nghìn là 7, chữ số hàng chục nghìn là 3 hoặc 4 (chính xác hơn, khi làm tròn đến hàng chục nghìn được 740 000 thì chữ số hàng chục nghìn thường là 4 (hoặc 3 nếu chữ số hàng nghìn >= 5)).\nĐáp số: Chữ số hàng trăm nghìn là 7; chữ số hàng chục nghìn là 3 hoặc 4.",
                       "Hàng trăm nghìn là 7; hàng chục nghìn là 3 hoặc 4", 5, 1.5),
            make_essay(6, "Hãy viết ba số có 6 chữ số khác nhau sao cho khi làm tròn đến hàng trăm nghìn đều nhận được số 300 000.",
                       "Lời giải:\nCác số có hàng trăm nghìn là 3 và hàng chục nghìn < 5 hoặc hàng trăm nghìn là 2 và hàng chục nghìn >= 5.\nVí dụ ba số:\n- 312 456\n- 340 589\n- 285 147\nĐáp số: 312 456; 340 589; 285 147 (hoặc các số tương tự).",
                       "312 456; 340 589; 285 147", 4, 1.0)
        ]
    }

    exams["th4_b13_test3"] = {
        "id": "th4_b13_test3",
        "lessonId": "th4_b13",
        "lessonNum": 13,
        "testNum": 3,
        "title": "Bài 13: Làm tròn số đến hàng trăm nghìn - Đề số 3",
        "topic": "Làm tròn số đến hàng trăm nghìn",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Làm tròn số 850 120 đến hàng trăm nghìn ta được số nào?", [
                "800 000",
                "850 000",
                "900 000",
                "1 000 000"
            ], 2, "Hàng chục nghìn là 5 >= 5 nên làm tròn lên thành 900 000."),
            make_mc(2, "Số 409 999 khi làm tròn đến hàng trăm nghìn ta được:", [
                "400 000",
                "410 000",
                "500 000",
                "409 000"
            ], 0, "Chữ số hàng chục nghìn là 0 < 5 nên làm tròn xuống thành 400 000."),
            make_mc(3, "Khoảng cách giữa hai thành phố là 265 800 m. Nếu làm tròn đến hàng trăm nghìn mét thì khoảng cách đó xấp xỉ bao nhiêu?", [
                "200 000 m",
                "260 000 m",
                "270 000 m",
                "300 000 m"
            ], 3, "Chữ số hàng chục nghìn là 6 >= 5 nên làm tròn lên thành 300 000 m."),
            make_mc(4, "Có tất cả bao nhiêu số tròn trăm nghìn có sáu chữ số?", [
                "8 số",
                "9 số",
                "10 số",
                "90 số"
            ], 1, "Các số: 100 000, 200 000, 300 000, 400 000, 500 000, 600 000, 700 000, 800 000, 900 000. Có tất cả 9 số."),
            make_mc(5, "Khi làm tròn số 625 400 đến hàng chục nghìn ta được:", [
                "620 000",
                "630 000",
                "600 000",
                "625 000"
            ], 1, "Hàng nghìn là 5 >= 5 nên làm tròn lên thành 630 000."),
            make_mc(6, "Số nào dưới đây khi làm tròn đến hàng trăm nghìn thì được số 100 000?", [
                "49 999",
                "51 200",
                "155 000",
                "210 000"
            ], 1, "51 200 có thể coi là 051 200 với hàng chục nghìn là 5 >= 5 làm tròn lên thành 100 000.")
        ],
        "part2": [
            make_essay(1, "Điền số thích hợp vào chỗ chấm sau khi làm tròn đến hàng trăm nghìn:\na) 372 000 làm tròn đến hàng trăm nghìn được ...\nb) 529 100 làm tròn đến hàng trăm nghìn được ...",
                       "Lời giải:\na) 372 000 có hàng chục nghìn là 7 >= 5, làm tròn thành 400 000.\nb) 529 100 có hàng chục nghìn là 2 < 5, làm tròn thành 500 000.\nĐáp số: a) 400 000; b) 500 000.",
                       "a) 400 000; b) 500 000", 4, 1.0),
            make_essay(2, "Một siêu thị điện máy trong tháng khuyến mại bán được 258 400 sản phẩm. Hãy làm tròn số sản phẩm này đến:\na) Hàng chục nghìn.\nb) Hàng trăm nghìn.",
                       "Lời giải:\na) Làm tròn đến hàng chục nghìn: Chữ số hàng nghìn là 8 >= 5, ta được: 260 000 sản phẩm.\nb) Làm tròn đến hàng trăm nghìn: Chữ số hàng chục nghìn là 5 >= 5, ta được: 300 000 sản phẩm.\nĐáp số: a) 260 000 sản phẩm; b) 300 000 sản phẩm.",
                       "a) 260 000 sản phẩm; b) 300 000 sản phẩm", 4, 1.0),
            make_essay(3, "Bác Nam có một mảnh đất trang trại trị giá 785 000 000 đồng. Bác tính nhẩm và bảo con: 'Mảnh đất này trị giá khoảng 800 triệu đồng'. Hỏi bác Nam đã làm tròn số tiền đến hàng nào?",
                       "Lời giải:\nSố 785 000 000 có chữ số hàng chục triệu là 8 (>= 5), khi làm tròn lên thành 800 000 000 (800 triệu).\nDo đó bác Nam đã làm tròn số tiền đến hàng trăm triệu.\nĐáp số: Hàng trăm triệu.",
                       "Hàng trăm triệu", 4, 1.0),
            make_essay(4, "Một công ty may mặc sản xuất hai loại áo. Loại áo sơ mi nam sản xuất được 314 200 chiếc, loại áo sơ mi nữ sản xuất được 289 500 chiếc. Em hãy:\na) Tính tổng số áo sơ mi cả hai loại.\nb) Làm tròn tổng số áo đó đến hàng trăm nghìn.",
                       "Lời giải:\na) Tổng số áo sơ mi cả hai loại công ty đã sản xuất là:\n314 200 + 289 500 = 603 700 (chiếc áo)\nb) Làm tròn số 603 700 đến hàng trăm nghìn:\nChữ số hàng chục nghìn là 0 (< 5) nên ta làm tròn thành: 600 000 chiếc áo.\nĐáp số: a) 603 700 chiếc; b) 600 000 chiếc.",
                       "a) 603 700 chiếc; b) 600 000 chiếc", 5, 1.5),
            make_essay(5, "Tìm số tròn nghìn bé nhất có sáu chữ số mà khi làm tròn số đó đến hàng trăm nghìn thì được số 900 000.",
                       "Lời giải:\nĐể làm tròn đến hàng trăm nghìn được 900 000:\n- Nếu làm tròn lên từ hàng trăm nghìn là 8 thì hàng chục nghìn bé nhất phải là 5.\n- Các hàng nghìn, trăm, chục, đơn vị là 0 để số là số tròn nghìn bé nhất.\nVậy số cần tìm là: 850 000.\nĐáp số: 850 000.",
                       "850 000", 5, 1.5),
            make_essay(6, "So sánh kết quả làm tròn đến hàng trăm nghìn của hai số: 449 999 và 450 000.",
                       "Lời giải:\n- Số 449 999 có hàng chục nghìn là 4 (< 5) nên làm tròn xuống thành: 400 000.\n- Số 450 000 có hàng chục nghìn là 5 (>= 5) nên làm tròn lên thành: 500 000.\nHai kết quả chênh lệch nhau: 500 000 - 400 000 = 100 000 đơn vị.\nĐáp số: 449 999 làm tròn thành 400 000; 450 000 làm tròn thành 500 000.",
                       "400 000 và 500 000", 4, 1.0)
        ]
    }

    return exams
