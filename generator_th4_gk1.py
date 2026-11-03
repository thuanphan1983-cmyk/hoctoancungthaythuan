# -*- coding: utf-8 -*-
"""
HỆ THỐNG ĐỀ KIỂM TRA GIỮA HỌC KÌ 1 - TOÁN TIỂU HỌC (LỚP 4)
Bộ sách: KẾT NỐI TRI THỨC VỚI CUỘC SỐNG
Gồm 8 đề kiểm tra chuẩn hóa độc lập 100% (th4_gk1_de01 đến th4_gk1_de08).

Cấu trúc mỗi đề thi:
- Thời gian làm bài: 40 phút
- Thang điểm: 10.0 điểm
- Phần I (3.0 điểm): 6 câu Trắc nghiệm khách quan 4 lựa chọn (mỗi câu 0.5 điểm)
- Phần II (7.0 điểm): 6 bài Tự luận (Điểm số: 1.0, 1.0, 1.0, 1.5, 1.5, 1.0 điểm; lineCount: 4-6 dòng)
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

def get_th4_gk1_exams():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 01 (th4_gk1_de01)
    # Chủ đề: Thu hoạch nông sản và đo lường
    # =========================================================================
    exams["th4_gk1_de01"] = {
        "id": "th4_gk1_de01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 1)",
        "grade": "4",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Trong số 485 273, chữ số 8 thuộc hàng nào và lớp nào?", [
                "Hàng chục nghìn, lớp nghìn",
                "Hàng trăm nghìn, lớp nghìn",
                "Hàng nghìn, lớp nghìn",
                "Hàng chục, lớp đơn vị"
            ], 0, "Chữ số 8 đứng ở vị trí thứ 5 từ phải sang trái nên thuộc hàng chục nghìn, lớp nghìn."),
            make_mc(2, "Đổi 5 tạ 40 kg sang ki-lô-gam ta được kết quả là:", [
                "54 kg",
                "540 kg",
                "504 kg",
                "5400 kg"
            ], 1, "Vì 1 tạ = 100 kg nên 5 tạ 40 kg = 500 kg + 40 kg = 540 kg."),
            make_mc(3, "Góc có số đo lớn hơn góc vuông và nhỏ hơn góc bẹt là:", [
                "Góc nhọn",
                "Góc tù",
                "Góc bẹt",
                "Góc vuông"
            ], 1, "Theo định nghĩa, góc lớn hơn góc vuông và nhỏ hơn góc bẹt là góc tù."),
            make_mc(4, "Làm tròn số 348 625 đến hàng chục nghìn ta được số:", [
                "340 000",
                "350 000",
                "348 000",
                "349 000"
            ], 1, "Chữ số hàng nghìn là 8 ($\\ge 5$) nên làm tròn lên thành 350 000."),
            make_mc(5, "Năm 1945 thuộc thế kỉ nào?", [
                "Thế kỉ XIX",
                "Thế kỉ XX",
                "Thế kỉ XXI",
                "Thế kỉ XVIII"
            ], 1, "Năm 1945 thuộc thế kỉ XX (từ năm 1901 đến năm 2000)."),
            make_mc(6, "Một con trâu nặng 3 tạ, một con bò nặng 25 yến. Con nào nặng hơn và nặng hơn bao nhiêu ki-lô-gam?", [
                "Trâu nặng hơn bò 50 kg",
                "Bò nặng hơn trâu 50 kg",
                "Trâu nặng hơn bò 5 kg",
                "Hai con nặng bằng nhau"
            ], 0, "Trâu nặng: 300 kg; Bò nặng: 250 kg. Trâu nặng hơn bò: 300 - 250 = 50 kg.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) Số \"Bốn trăm ba mươi nghìn bảy trăm linh năm\" viết là: ..........\nb) Trong số 729 456, giá trị của chữ số 2 là: ..........", "Bài giải:\na) Số đã cho viết là: 430 705.\nb) Chữ số 2 thuộc hàng chục nghìn nên có giá trị là 20 000.\nĐáp số: a) 430 705; b) 20 000", "a) 430 705; b) 20 000", 4, 1.0),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) $4\\text{ tấn } 5\\text{ tạ} = ..........\\text{ tạ}$\nb) $3\\text{ yến } 8\\text{ kg} = ..........\\text{ kg}$\nc) $3\\text{ phút } 20\\text{ giây} = ..........\\text{ giây}$\nd) $2\\text{ thế kỉ} = ..........\\text{ năm}$", "Bài giải:\na) $4\\text{ tấn } 5\\text{ tạ} = 40\\text{ tạ} + 5\\text{ tạ} = 45\\text{ tạ}$\nb) $3\\text{ yến } 8\\text{ kg} = 30\\text{ kg} + 8\\text{ kg} = 38\\text{ kg}$\nc) $3\\text{ phút } 20\\text{ giây} = 180\\text{ giây} + 20\\text{ giây} = 200\\text{ giây}$\nd) $2\\text{ thế kỉ} = 2 \\times 100\\text{ năm} = 200\\text{ năm}$\nĐáp số: a) 45; b) 38; c) 200; d) 200", "a) 45; b) 38; c) 200; d) 200", 4, 1.0),
            make_essay(3, "Tính giá trị của biểu thức:\na) $m + 250$ với $m = 1750$\nb) $a - b$ với $a = 8400, b = 2900$", "Bài giải:\na) Với $m = 1750$, giá trị biểu thức là: $1750 + 250 = 2000$\nb) Với $a = 8400, b = 2900$, giá trị biểu thức là: $8400 - 2900 = 5500$\nĐáp số: a) 2000; b) 5500", "a) 2000; b) 5500", 4, 1.0),
            make_essay(4, "Một đoàn xe chở hàng từ kho ra cảng gồm 4 xe tải lớn, mỗi xe chở 35 tạ ngô và 3 xe tải nhỏ, mỗi xe chở 25 tạ ngô. Hỏi cả đoàn xe chở được tất cả bao nhiêu tấn ngô?", "Bài giải:\n4 xe tải lớn chở được số tạ ngô là:\n$35 \\times 4 = 140$ (tạ)\n3 xe tải nhỏ chở được số tạ ngô là:\n$25 \\times 3 = 75$ (tạ)\nCả đoàn xe chở được số tạ ngô là:\n$140 + 75 = 215$ (tạ)\nĐổi $215\\text{ tạ} = 21\\text{ tấn } 5\\text{ tạ}$ (hoặc 21,5 tấn).\nĐáp số: 21 tấn 5 tạ ngô (hay 215 tạ ngô).", "215 tạ ngô (21 tấn 5 tạ)", 6, 1.5),
            make_essay(5, "Cho tứ giác $ABCD$ có góc $A$ và góc $B$ là góc vuông, góc $C$ là góc tù, góc $D$ là góc nhọn.\na) Hãy nêu tên từng góc của tứ giác $ABCD$ theo phân loại (góc vuông, góc nhọn, góc tù).\nb) Đỉnh nào của tứ giác tạo thành góc lớn hơn góc vuông nhưng nhỏ hơn góc bẹt?", "Bài giải:\na) Trong tứ giác $ABCD$:\n- Góc đỉnh $A$ và góc đỉnh $B$ là hai góc vuông.\n- Góc đỉnh $C$ là góc tù.\n- Góc đỉnh $D$ là góc nhọn.\nb) Góc lớn hơn góc vuông và nhỏ hơn góc bẹt là góc tù, đó là góc đỉnh $C$.\nĐáp số: a) A, B: vuông; C: tù; D: nhọn; b) Đỉnh C.", "a) A, B vuông; C tù; D nhọn; b) Đỉnh C", 5, 1.5),
            make_essay(6, "Tìm một số có sáu chữ số biết rằng chữ số hàng trăm nghìn là số lớn nhất có một chữ số, các chữ số còn lại đều bằng nhau và tổng các chữ số của số đó bằng 24.", "Bài giải:\nChữ số hàng trăm nghìn là số lớn nhất có 1 chữ số, nên chữ số đó là 9.\nTổng 5 chữ số còn lại là: $24 - 9 = 15$.\nVì 5 chữ số còn lại đều bằng nhau nên mỗi chữ số là: $15 : 5 = 3$.\nVậy số cần tìm là: 933 333.\nĐáp số: 933 333.", "933 333", 5, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 02 (th4_gk1_de02)
    # =========================================================================
    exams["th4_gk1_de02"] = {
        "id": "th4_gk1_de02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 2)",
        "grade": "4",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Số gồm 5 trăm nghìn, 7 nghìn, 3 chục và 8 đơn vị viết là:", [
                "507 038",
                "570 038",
                "507 380",
                "570 380"
            ], 0, "Lớp nghìn gồm 5 trăm nghìn, 0 chục nghìn, 7 nghìn; lớp đơn vị gồm 0 trăm, 3 chục, 8 đơn vị. Viết là 507 038."),
            make_mc(2, "Đổi 4 tấn 6 yến ra ki-lô-gam được:", [
                "4060 kg",
                "4600 kg",
                "406 kg",
                "460 kg"
            ], 0, "$4\\text{ tấn} = 4000\\text{ kg}$; $6\\text{ yến} = 60\\text{ kg}$. Tổng là 4060 kg."),
            make_mc(3, "Góc tạo bởi hai kim đồng hồ lúc 6 giờ đúng là:", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 3, "Lúc 6 giờ, kim giờ và kim phút tạo thành một đường thẳng, tức là góc bẹt ($180^\\circ$)."),
            make_mc(4, "Làm tròn số 582 714 đến hàng trăm nghìn ta được số:", [
                "500 000",
                "600 000",
                "580 000",
                "590 000"
            ], 1, "Chữ số hàng chục nghìn là 8 ($\\ge 5$) nên làm tròn lên thành 600 000."),
            make_mc(5, "Bác Hồ sinh năm 1890. Năm đó thuộc thế kỉ nào?", [
                "Thế kỉ XVIII",
                "Thế kỉ XIX",
                "Thế kỉ XX",
                "Thế kỉ XVII"
            ], 1, "Năm 1890 thuộc thế kỉ XIX (từ năm 1801 đến năm 1900)."),
            make_mc(6, "Trong các số: 3452, 6789, 4520, 8931, các số chẵn là:", [
                "3452 và 4520",
                "6789 và 8931",
                "3452 và 6789",
                "4520 và 8931"
            ], 0, "Số chẵn có chữ số tận cùng là 0, 2, 4, 6, 8. Đó là 3452 và 4520.")
        ],
        "part2": [
            make_essay(1, "Điền dấu thích hợp ($>, <, =$) vào chỗ chấm:\na) $485 230 ..... 485 320$\nb) $600 000 + 40 000 ..... 640 000$\nc) $99 999 ..... 100 001$\nd) $725 410 ..... 725 401$", "Bài giải:\na) $485 230 < 485 320$\nb) $600 000 + 40 000 = 640 000$\nc) $99 999 < 100 001$\nd) $725 410 > 725 401$\nĐáp số: a) <; b) =; c) <; d) >", "a) <; b) =; c) <; d) >", 4, 1.0),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) $6\\text{ tạ } 5\\text{ yến} = ..........\\text{ yến}$\nb) $3\\text{ tấn } 200\\text{ kg} = ..........\\text{ kg}$\nc) $5\\text{ phút } 15\\text{ giây} = ..........\\text{ giây}$\nd) $300\\text{ năm} = ..........\\text{ thế kỉ}$", "Bài giải:\na) $6\\text{ tạ } 5\\text{ yến} = 60\\text{ yến} + 5\\text{ yến} = 65\\text{ yến}$\nb) $3\\text{ tấn } 200\\text{ kg} = 3000\\text{ kg} + 200\\text{ kg} = 3200\\text{ kg}$\nc) $5\\text{ phút } 15\\text{ giây} = 300\\text{ giây} + 15\\text{ giây} = 315\\text{ giây}$\nd) $300\\text{ năm} = 3\\text{ thế kỉ}$\nĐáp số: a) 65; b) 3200; c) 315; d) 3", "a) 65; b) 3200; c) 315; d) 3", 4, 1.0),
            make_essay(3, "Làm tròn các số sau:\na) Làm tròn số 258 471 đến hàng nghìn: ..........\nb) Làm tròn số 736 820 đến hàng chục nghìn: ..........", "Bài giải:\na) Chữ số hàng trăm là 4 ($< 5$) nên làm tròn thành 258 000.\nb) Chữ số hàng nghìn là 6 ($\\ge 5$) nên làm tròn thành 740 000.\nĐáp số: a) 258 000; b) 740 000", "a) 258 000; b) 740 000", 4, 1.0),
            make_essay(4, "Một cửa hàng lương thực ngày thứ nhất bán được 25 tạ gạo. Ngày thứ hai bán được số gạo gấp 2 lần ngày thứ nhất. Ngày thứ ba bán được ít hơn ngày thứ hai 8 tạ gạo. Hỏi cả ba ngày cửa hàng bán được bao nhiêu tạ gạo?", "Bài giải:\nNgày thứ hai cửa hàng bán được số tạ gạo là:\n$25 \\times 2 = 50$ (tạ)\nNgày thứ ba cửa hàng bán được số tạ gạo là:\n$50 - 8 = 42$ (tạ)\nCả ba ngày cửa hàng bán được số tạ gạo là:\n$25 + 50 + 42 = 117$ (tạ)\nĐáp số: 117 tạ gạo.", "117 tạ gạo", 6, 1.5),
            make_essay(5, "Quan sát hình vẽ tam giác $MNP$ có góc $M = 90^\\circ$ (góc vuông), góc $N = 35^\\circ$ (góc nhọn), góc $P = 55^\\circ$ (góc nhọn).\na) Hãy gọi tên các góc nhọn trong tam giác $MNP$.\nb) So sánh số đo của góc đỉnh $M$ với góc đỉnh $N$.", "Bài giải:\na) Trong tam giác $MNP$, các góc nhọn là: góc đỉnh $N$ và góc đỉnh $P$.\nb) Góc đỉnh $M$ là góc vuông, góc đỉnh $N$ là góc nhọn. Do góc vuông luôn lớn hơn góc nhọn nên góc đỉnh $M$ lớn hơn góc đỉnh $N$.\nĐáp số: a) Góc đỉnh N và góc đỉnh P; b) Góc đỉnh M lớn hơn góc đỉnh N.", "a) Đỉnh N và P; b) Đỉnh M lớn hơn đỉnh N", 5, 1.5),
            make_essay(6, "Viết số tự nhiên nhỏ nhất có 6 chữ số khác nhau sao cho tổng các chữ số của số đó bằng 20.", "Bài giải:\nĐể số có 6 chữ số là nhỏ nhất:\n- Chữ số hàng trăm nghìn phải nhỏ nhất khác 0, chọn chữ số 1.\n- Các chữ số tiếp theo chọn từ nhỏ đến lớn: hàng chục nghìn chọn 0, hàng nghìn chọn 2, hàng trăm chọn 3.\nTổng 4 chữ số đầu tiên là: $1 + 0 + 2 + 3 = 6$.\nTổng hai chữ số còn lại (hàng chục và hàng đơn vị) phải là: $20 - 6 = 14$.\nVì các chữ số phải khác nhau (khác 0, 1, 2, 3) và để số nhỏ nhất thì chữ số hàng chục phải nhỏ hơn, ta chọn hàng chục là 5, khi đó hàng đơn vị là $14 - 5 = 9$.\nVậy số nhỏ nhất thỏa mãn là: 102 359.\nĐáp số: 102 359.", "102 359", 5, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 03 (th4_gk1_de03)
    # =========================================================================
    exams["th4_gk1_de03"] = {
        "id": "th4_gk1_de03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 3)",
        "grade": "4",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Số liền sau của số 999 999 là:", [
                "1 000 000",
                "1 000 001",
                "999 998",
                "10 000 000"
            ], 0, "Số liền sau của 999 999 là $999 999 + 1 = 1 000 000$ (Một triệu)."),
            make_mc(2, "Đổi: 2 phút 45 giây = .......... giây:", [
                "145 giây",
                "165 giây",
                "105 giây",
                "185 giây"
            ], 1, "$2\\text{ phút} = 120\\text{ giây}$, $120 + 45 = 165$ giây."),
            make_mc(3, "Góc tạo bởi hai kim đồng hồ lúc 3 giờ đúng là:", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 1, "Lúc 3 giờ đúng, kim giờ chỉ số 3, kim phút chỉ số 12 tạo thành góc vuông ($90^\\circ$)."),
            make_mc(4, "Một con voi nặng 4 tấn, một con hà mã nặng 35 tạ. Con voi nặng hơn con hà mã bao nhiêu ki-lô-gam?", [
                "500 kg",
                "50 kg",
                "5 kg",
                "5000 kg"
            ], 0, "Voi nặng 4000 kg; Hà mã nặng 3500 kg. Chênh lệch: $4000 - 3500 = 500$ kg."),
            make_mc(5, "Năm 1010, vua Lý Thái Tổ dời đô về Thăng Long. Năm đó thuộc thế kỉ nào?", [
                "Thế kỉ X",
                "Thế kỉ XI",
                "Thế kỉ XII",
                "Thế kỉ IX"
            ], 1, "Năm 1010 thuộc thế kỉ XI (từ năm 1001 đến năm 1100)."),
            make_mc(6, "Cho biểu thức $P = a \\times 5$. Với $a = 140$, giá trị của $P$ là:", [
                "700",
                "500",
                "750",
                "650"
            ], 0, "$P = 140 \\times 5 = 700$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $345 281 + 128 345$\nb) $672 590 - 245 180$", "Bài giải:\na) $345 281 + 128 345 = 473 626$\nb) $672 590 - 245 180 = 427 410$\nĐáp số: a) 473 626; b) 427 410", "a) 473 626; b) 427 410", 4, 1.0),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) $8\\text{ yến} = ..........\\text{ kg}$\nb) $5\\text{ tạ } 30\\text{ kg} = ..........\\text{ kg}$\nc) $7\\text{ tấn } 4\\text{ tạ} = ..........\\text{ tạ}$\nd) $4\\text{ thế kỉ} = ..........\\text{ năm}$", "Bài giải:\na) $8\\text{ yến} = 80\\text{ kg}$\nb) $5\\text{ tạ } 30\\text{ kg} = 530\\text{ kg}$\nc) $7\\text{ tấn } 4\\text{ tạ} = 74\\text{ tạ}$\nd) $4\\text{ thế kỉ} = 400\\text{ năm}$\nĐáp số: a) 80; b) 530; c) 74; d) 400", "a) 80; b) 530; c) 74; d) 400", 4, 1.0),
            make_essay(3, "Sắp xếp các số sau theo thứ tự từ bé đến lớn:\n458 920; 459 012; 458 899; 459 100", "Bài giải:\nSo sánh các số:\n$458 899 < 458 920 < 459 012 < 459 100$\nThứ tự từ bé đến lớn là: 458 899; 458 920; 459 012; 459 100.\nĐáp số: 458 899; 458 920; 459 012; 459 100", "458 899; 458 920; 459 012; 459 100", 4, 1.0),
            make_essay(4, "Một trang trại nuôi 3 chuồng gà. Chuồng thứ nhất có 1250 con gà. Chuồng thứ hai có số gà gấp 2 lần chuồng thứ nhất. Chuồng thứ ba có ít hơn chuồng thứ hai 450 con gà. Hỏi trang trại đó có tất cả bao nhiêu con gà?", "Bài giải:\nSố con gà ở chuồng thứ hai là:\n$1250 \\times 2 = 2500$ (con)\nSố con gà ở chuồng thứ ba là:\n$2500 - 450 = 2050$ (con)\nCả trang trại có tất cả số con gà là:\n$1250 + 2500 + 2050 = 5800$ (con)\nĐáp số: 5800 con gà.", "5800 con", 6, 1.5),
            make_essay(5, "Cho góc đỉnh $O$, cạnh $OM, ON$ là góc bẹt. Kẻ tia $OP$ sao cho góc đỉnh $O$ cạnh $OM, OP$ là góc vuông.\na) Hãy cho biết góc đỉnh $O$ cạnh $OP, ON$ là góc gì?\nb) Kể tên các góc vuông và góc bẹt có trong hình.", "Bài giải:\na) Vì góc $MON$ là góc bẹt ($180^\\circ$) và góc $MOP$ là góc vuông ($90^\\circ$) nên góc $PON = 180^\\circ - 90^\\circ = 90^\\circ$, đây là một góc vuông.\nb) - Các góc vuông là: góc đỉnh $O$ cạnh $OM, OP$ và góc đỉnh $O$ cạnh $OP, ON$.\n- Góc bẹt là: góc đỉnh $O$ cạnh $OM, ON$.\nĐáp số: a) Góc vuông; b) Góc vuông: MOP, PON; Góc bẹt: MON.", "a) Góc vuông; b) Vuông: MOP, PON; Bẹt: MON", 5, 1.5),
            make_essay(6, "Tìm hai số chẵn liên tiếp có tổng bằng 2026.", "Bài giải:\nHai số chẵn liên tiếp hơn kém nhau 2 đơn vị.\nSố bé là: $(2026 - 2) : 2 = 1012$\nSố lớn là: $1012 + 2 = 1014$\nĐáp số: Số bé: 1012; Số lớn: 1014.", "1012 và 1014", 5, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 04 (th4_gk1_de04)
    # =========================================================================
    exams["th4_gk1_de04"] = {
        "id": "th4_gk1_de04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 4)",
        "grade": "4",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Chữ số 7 trong số 714 832 có giá trị là:", [
                "700 000",
                "70 000",
                "7 000",
                "700"
            ], 0, "Chữ số 7 ở hàng trăm nghìn nên có giá trị là 700 000."),
            make_mc(2, "Đổi 8 tạ 6 yến ra yến được:", [
                "86 yến",
                "806 yến",
                "860 yến",
                "68 yến"
            ], 0, "$8\\text{ tạ} = 80\\text{ yến}$, $80 + 6 = 86$ yến."),
            make_mc(3, "Góc tạo bởi hai kim đồng hồ lúc 2 giờ đúng là:", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 0, "Lúc 2 giờ góc tạo bởi kim giờ và kim phút bé hơn góc vuông, nên là góc nhọn."),
            make_mc(4, "Làm tròn số 426 890 đến hàng nghìn ta được số:", [
                "427 000",
                "426 000",
                "430 000",
                "420 000"
            ], 0, "Chữ số hàng trăm là 8 ($\\ge 5$) nên làm tròn lên thành 427 000."),
            make_mc(5, "Năm 2000 là năm cuối cùng của thế kỉ nào?", [
                "Thế kỉ XX",
                "Thế kỉ XIX",
                "Thế kỉ XXI",
                "Thế kỉ XVIII"
            ], 0, "Thế kỉ XX bắt đầu từ năm 1901 và kết thúc vào hết năm 2000."),
            make_mc(6, "Tính giá trị của biểu thức $a + b \\times 2$ với $a = 15, b = 25$:", [
                "65",
                "80",
                "55",
                "75"
            ], 0, "$15 + 25 \\times 2 = 15 + 50 = 65$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $456 128 + 235 741$\nb) $892 450 - 361 280$", "Bài giải:\na) $456 128 + 235 741 = 691 869$\nb) $892 450 - 361 280 = 531 170$\nĐáp số: a) 691 869; b) 531 170", "a) 691 869; b) 531 170", 4, 1.0),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) $5\\text{ tấn } 8\\text{ yến} = ..........\\text{ kg}$\nb) $7\\text{ tạ } 50\\text{ kg} = ..........\\text{ kg}$\nc) $4\\text{ phút } 10\\text{ giây} = ..........\\text{ giây}$\nd) $\\frac{1}{4}\\text{ thế kỉ} = ..........\\text{ năm}$", "Bài giải:\na) $5\\text{ tấn } 8\\text{ yến} = 5000\\text{ kg} + 80\\text{ kg} = 5080\\text{ kg}$\nb) $7\\text{ tạ } 50\\text{ kg} = 700\\text{ kg} + 50\\text{ kg} = 750\\text{ kg}$\nc) $4\\text{ phút } 10\\text{ giây} = 240\\text{ giây} + 10\\text{ giây} = 250\\text{ giây}$\nd) $\\frac{1}{4}\\text{ thế kỉ} = 100 : 4 = 25\\text{ năm}$\nĐáp số: a) 5080; b) 750; c) 250; d) 25", "a) 5080; b) 750; c) 250; d) 25", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 125 400 = 342 600$", "Bài giải:\n$x = 342 600 + 125 400$\n$x = 468 000$\nĐáp số: $x = 468 000$", "x = 468 000", 4, 1.0),
            make_essay(4, "Một đoàn xe vận tải gồm hai đội xe. Đội thứ nhất có 5 xe, mỗi xe chở được 42 tạ hàng. Đội thứ hai có 4 xe, mỗi xe chở được 35 tạ hàng. Hỏi cả hai đội xe chở được tất cả bao nhiêu tấn hàng?", "Bài giải:\nĐội thứ nhất chở được số tạ hàng là:\n$42 \\times 5 = 210$ (tạ)\nĐội thứ hai chở được số tạ hàng là:\n$35 \\times 4 = 140$ (tạ)\nCả hai đội chở được tất cả số tạ hàng là:\n$210 + 140 = 350$ (tạ)\nĐổi $350\\text{ tạ} = 35\\text{ tấn}$\nĐáp số: 35 tấn hàng.", "35 tấn", 6, 1.5),
            make_essay(5, "Vẽ hình và cho biết trong hình chữ nhật $ABCD$ có mấy góc vuông, mấy góc nhọn và mấy góc tù?", "Bài giải:\nHình chữ nhật $ABCD$ có:\n- 4 góc vuông tại các đỉnh $A, B, C, D$.\n- 0 góc nhọn.\n- 0 góc tù.\nĐáp số: 4 góc vuông; 0 góc nhọn; 0 góc tù.", "4 góc vuông, 0 nhọn, 0 tù", 5, 1.5),
            make_essay(6, "Tìm tổng của số lớn nhất có 6 chữ số khác nhau và số bé nhất có 6 chữ số khác nhau.", "Bài giải:\nSố lớn nhất có 6 chữ số khác nhau là: 987 654.\nSố bé nhất có 6 chữ số khác nhau là: 102 345.\nTổng hai số đó là:\n$987 654 + 102 345 = 1 089 999$\nĐáp số: 1 089 999.", "1 089 999", 5, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 05 (th4_gk1_de05)
    # =========================================================================
    exams["th4_gk1_de05"] = {
        "id": "th4_gk1_de05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 5)",
        "grade": "4",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Số nào dưới đây có chữ số 5 thuộc hàng trăm nghìn?", [
                "512 340",
                "152 340",
                "125 340",
                "123 540"
            ], 0, "Số 512 340 có chữ số 5 ở hàng trăm nghìn."),
            make_mc(2, "Đổi 3 tấn 5 tạ = .......... kg:", [
                "3500 kg",
                "3050 kg",
                "350 kg",
                "3005 kg"
            ], 0, "$3\\text{ tấn} = 3000\\text{ kg}$, $5\\text{ tạ} = 500\\text{ kg}$, tổng là 3500 kg."),
            make_mc(3, "Góc tạo bởi hai kim đồng hồ lúc 5 giờ đúng là:", [
                "Góc tù",
                "Góc nhọn",
                "Góc vuông",
                "Góc bẹt"
            ], 0, "Lúc 5 giờ, góc tạo bởi kim giờ và kim phút lớn hơn góc vuông và nhỏ hơn góc bẹt nên là góc tù."),
            make_mc(4, "Làm tròn số 675 320 đến hàng chục nghìn ta được số:", [
                "680 000",
                "670 000",
                "700 000",
                "675 000"
            ], 0, "Chữ số hàng nghìn là 5 nên làm tròn lên thành 680 000."),
            make_mc(5, "Chiến thắng Điện Biên Phủ diễn ra vào năm 1954. Năm đó thuộc thế kỉ nào?", [
                "Thế kỉ XX",
                "Thế kỉ XIX",
                "Thế kỉ XXI",
                "Thế kỉ XVIII"
            ], 0, "Năm 1954 thuộc thế kỉ XX."),
            make_mc(6, "Tìm số lẻ liền sau của số 45 899 là:", [
                "45 901",
                "45 900",
                "45 897",
                "45 903"
            ], 0, "Số liền sau của 45 899 là 45 900 (chẵn), số lẻ liền sau là 45 901.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $518 245 + 236 418$\nb) $742 850 - 319 420$", "Bài giải:\na) $518 245 + 236 418 = 754 663$\nb) $742 850 - 319 420 = 423 430$\nĐáp số: a) 754 663; b) 423 430", "a) 754 663; b) 423 430", 4, 1.0),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) $9\\text{ yến } 5\\text{ kg} = ..........\\text{ kg}$\nb) $6\\text{ tấn } 40\\text{ kg} = ..........\\text{ kg}$\nc) $6\\text{ phút } 20\\text{ giây} = ..........\\text{ giây}$\nd) $\\frac{1}{2}\\text{ thế kỉ} = ..........\\text{ năm}$", "Bài giải:\na) $9\\text{ yến } 5\\text{ kg} = 95\\text{ kg}$\nb) $6\\text{ tấn } 40\\text{ kg} = 6040\\text{ kg}$\nc) $6\\text{ phút } 20\\text{ giây} = 380\\text{ giây}$\nd) $\\frac{1}{2}\\text{ thế kỉ} = 100 : 2 = 50\\text{ năm}$\nĐáp số: a) 95; b) 6040; c) 380; d) 50", "a) 95; b) 6040; c) 380; d) 50", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x + 215 300 = 689 700$", "Bài giải:\n$x = 689 700 - 215 300$\n$x = 474 400$\nĐáp số: $x = 474 400$", "x = 474 400", 4, 1.0),
            make_essay(4, "Một gia đình thu hoạch cà phê trong 3 đợt. Đợt 1 thu được 18 tạ cà phê. Đợt 2 thu được gấp 2 lần đợt 1. Đợt 3 thu được ít hơn đợt 2 là 6 tạ cà phê. Hỏi cả ba đợt gia đình đó thu hoạch được bao nhiêu tạ cà phê?", "Bài giải:\nĐợt 2 thu hoạch được số tạ cà phê là:\n$18 \\times 2 = 36$ (tạ)\nĐợt 3 thu hoạch được số tạ cà phê là:\n$36 - 6 = 30$ (tạ)\nCả 3 đợt thu hoạch được số tạ cà phê là:\n$18 + 36 + 30 = 84$ (tạ)\nĐáp số: 84 tạ cà phê.", "84 tạ", 6, 1.5),
            make_essay(5, "Hình tam giác $ABC$ có một góc tù tại đỉnh $A$. Hai góc còn lại tại đỉnh $B$ và đỉnh $C$ là góc gì? Vì sao?", "Bài giải:\nTrong một hình tam giác, nếu có một góc tù thì hai góc còn lại bắt buộc phải là hai góc nhọn (vì tổng ba góc bằng hai góc vuông, một góc tù đã lớn hơn góc vuông nên hai góc kia phải bé hơn góc vuông).\nDo đó góc tại đỉnh $B$ và góc tại đỉnh $C$ đều là góc nhọn.\nĐáp số: Góc nhọn.", "Hai góc nhọn", 5, 1.5),
            make_essay(6, "Một rạp chiếu phim bán vé trong 3 ngày được tất cả 1860 vé. Biết ngày thứ hai bán gấp đôi ngày thứ nhất, ngày thứ ba bán gấp 3 lần ngày thứ nhất. Hỏi mỗi ngày rạp bán được bao nhiêu vé?", "Bài giải:\nCoi số vé ngày thứ nhất là 1 phần.\nSố vé ngày thứ hai là 2 phần, ngày thứ ba là 3 phần.\nTổng số phần bằng nhau là:\n$1 + 2 + 3 = 6$ (phần)\nSố vé bán ngày thứ nhất là:\n$1860 : 6 = 310$ (vé)\nSố vé bán ngày thứ hai là:\n$310 \\times 2 = 620$ (vé)\nSố vé bán ngày thứ ba là:\n$310 \\times 3 = 930$ (vé)\nĐáp số: Ngày 1: 310 vé; Ngày 2: 620 vé; Ngày 3: 930 vé.", "310; 620; 930 vé", 6, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 06 (th4_gk1_de06)
    # =========================================================================
    exams["th4_gk1_de06"] = {
        "id": "th4_gk1_de06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 6)",
        "grade": "4",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Số gồm 8 trăm nghìn, 5 chục nghìn, 4 trăm và 6 đơn vị viết là:", [
                "850 406",
                "854 006",
                "805 406",
                "850 460"
            ], 0, "Viết là 850 406."),
            make_mc(2, "Đổi 2 tấn 8 tạ = .......... tạ:", [
                "28 tạ",
                "208 tạ",
                "280 tạ",
                "2800 tạ"
            ], 0, "$2\\text{ tấn} = 20\\text{ tạ}$, $20 + 8 = 28$ tạ."),
            make_mc(3, "Góc nhọn là góc:", [
                "Bé hơn góc vuông",
                "Lớn hơn góc vuông",
                "Bằng góc vuông",
                "Bằng hai góc vuông"
            ], 0, "Góc nhọn là góc bé hơn góc vuông."),
            make_mc(4, "Làm tròn số 843 670 đến hàng trăm nghìn ta được số:", [
                "800 000",
                "900 000",
                "840 000",
                "850 000"
            ], 0, "Chữ số hàng chục nghìn là 4 ($< 5$) nên làm tròn thành 800 000."),
            make_mc(5, "Năm 1428, Lê Lợi lên ngôi vua sau khởi nghĩa Lam Sơn. Năm đó thuộc thế kỉ nào?", [
                "Thế kỉ XV",
                "Thế kỉ XIV",
                "Thế kỉ XVI",
                "Thế kỉ XIII"
            ], 0, "Năm 1428 thuộc thế kỉ XV (từ năm 1401 đến năm 1500)."),
            make_mc(6, "Biểu thức $m - n + p$ với $m = 50, n = 20, p = 15$ có giá trị là:", [
                "45",
                "35",
                "15",
                "55"
            ], 0, "$50 - 20 + 15 = 30 + 15 = 45$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $624 350 + 158 270$\nb) $890 540 - 452 380$", "Bài giải:\na) $624 350 + 158 270 = 782 620$\nb) $890 540 - 452 380 = 438 160$\nĐáp số: a) 782 620; b) 438 160", "a) 782 620; b) 438 160", 4, 1.0),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) $4\\text{ tạ } 8\\text{ yến} = ..........\\text{ kg}$\nb) $5\\text{ tấn } 250\\text{ kg} = ..........\\text{ kg}$\nc) $7\\text{ phút } 15\\text{ giây} = ..........\\text{ giây}$\nd) $\\frac{1}{5}\\text{ thế kỉ} = ..........\\text{ năm}$", "Bài giải:\na) $4\\text{ tạ } 8\\text{ yến} = 400\\text{ kg} + 80\\text{ kg} = 480\\text{ kg}$\nb) $5\\text{ tấn } 250\\text{ kg} = 5000\\text{ kg} + 250\\text{ kg} = 5250\\text{ kg}$\nc) $7\\text{ phút } 15\\text{ giây} = 420\\text{ giây} + 15\\text{ giây} = 435\\text{ giây}$\nd) $\\frac{1}{5}\\text{ thế kỉ} = 100 : 5 = 20\\text{ năm}$\nĐáp số: a) 480; b) 5250; c) 435; d) 20", "a) 480; b) 5250; c) 435; d) 20", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$850 000 - x = 240 000 + 160 000$", "Bài giải:\n$850 000 - x = 400 000$\n$x = 850 000 - 400 000 = 450 000$\nĐáp số: $x = 450 000$", "x = 450 000", 4, 1.0),
            make_essay(4, "Một đoàn xe chở 45 tấn xi măng về công trường. Lần thứ nhất có 3 xe, mỗi xe chở được 45 tạ. Lần thứ hai có 4 xe, mỗi xe chở được 55 tạ. Hỏi sau hai lần chở, công trường còn thiếu bao nhiêu tạ xi măng nữa?", "Bài giải:\nĐổi: $45\\text{ tấn} = 450\\text{ tạ}$.\nLần thứ nhất chở được số tạ xi măng là:\n$45 \\times 3 = 135$ (tạ)\nLần thứ hai chở được số tạ xi măng là:\n$55 \\times 4 = 220$ (tạ)\nCả hai lần đã chở được số tạ xi măng là:\n$135 + 220 = 355$ (tạ)\nSố tạ xi măng công trường còn thiếu là:\n$450 - 355 = 95$ (tạ)\nĐáp số: 95 tạ xi măng.", "95 tạ", 6, 1.5),
            make_essay(5, "Vẽ một góc nhọn đỉnh $O$ cạnh $OA, OB$ và một góc tù đỉnh $O$ cạnh $OC, OD$. Nêu rõ cách nhận biết góc nhọn và góc tù dựa vào ê-ke.", "Bài giải:\n- Dùng ê-ke để kiểm tra:\n+ Đặt góc vuông của ê-ke trùng với đỉnh và một cạnh của góc. Nếu cạnh còn lại nằm bên trong góc vuông của ê-ke thì đó là góc nhọn (bé hơn góc vuông).\n+ Nếu cạnh còn lại nằm bên ngoài góc vuông của ê-ke thì đó là góc tù (lớn hơn góc vuông).\nĐáp số: Dùng góc vuông ê-ke để so sánh.", "Nhận biết bằng ê-ke", 5, 1.5),
            make_essay(6, "Tìm một số có 3 chữ số biết rằng khi viết thêm chữ số 2 vào bên trái số đó ta được số mới gấp 9 lần số phải tìm.", "Bài giải:\nGọi số phải tìm là $\\overline{abc}$.\nKhi viết thêm chữ số 2 vào bên trái ta được số mới là $\\overline{2abc} = 2000 + \\overline{abc}$.\nTheo đề bài:\n$2000 + \\overline{abc} = 9 \\times \\overline{abc}$\n$8 \\times \\overline{abc} = 2000$\n$\\overline{abc} = 2000 : 8 = 250$\nVậy số cần tìm là 250.\nĐáp số: 250.", "250", 5, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 07 (th4_gk1_de07)
    # =========================================================================
    exams["th4_gk1_de07"] = {
        "id": "th4_gk1_de07",
        "testNum": 7,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 7)",
        "grade": "4",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Giá trị của chữ số 4 trong số 942 581 là:", [
                "40 000",
                "4 000",
                "400 000",
                "400"
            ], 0, "Chữ số 4 ở hàng chục nghìn nên có giá trị là 40 000."),
            make_mc(2, "Đổi 6 tạ 4 yến ra ki-lô-gam được:", [
                "640 kg",
                "604 kg",
                "64 kg",
                "6400 kg"
            ], 0, "$6\\text{ tạ} = 600\\text{ kg}$, $4\\text{ yến} = 40\\text{ kg}$, tổng là 640 kg."),
            make_mc(3, "Góc bẹt có số đo bằng bao nhiêu góc vuông?", [
                "Bằng 2 góc vuông",
                "Bằng 1 góc vuông",
                "Bằng 3 góc vuông",
                "Bằng 4 góc vuông"
            ], 0, "Góc bẹt bằng 2 góc vuông ($180^\\circ = 2 \\times 90^\\circ$)."),
            make_mc(4, "Làm tròn số 518 490 đến hàng nghìn ta được số:", [
                "518 000",
                "519 000",
                "520 000",
                "510 000"
            ], 0, "Chữ số hàng trăm là 4 ($< 5$) nên làm tròn xuống thành 518 000."),
            make_mc(5, "Năm 938, Ngô Quyền đại phá quân Nam Hán trên sông Bạch Đằng. Năm đó thuộc thế kỉ nào?", [
                "Thế kỉ X",
                "Thế kỉ IX",
                "Thế kỉ XI",
                "Thế kỉ VIII"
            ], 0, "Năm 938 thuộc thế kỉ X (từ năm 901 đến năm 1000)."),
            make_mc(6, "Một bao ngô nặng 5 yến, một bao khoai nặng 45 kg. Cả hai bao nặng tất cả bao nhiêu ki-lô-gam?", [
                "95 kg",
                "50 kg",
                "545 kg",
                "85 kg"
            ], 0, "$5\\text{ yến} = 50\\text{ kg}$, $50 + 45 = 95$ kg.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $482 175 + 341 520$\nb) $956 480 - 412 360$", "Bài giải:\na) $482 175 + 341 520 = 823 695$\nb) $956 480 - 412 360 = 544 120$\nĐáp số: a) 823 695; b) 544 120", "a) 823 695; b) 544 120", 4, 1.0),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) $7\\text{ yến } 8\\text{ kg} = ..........\\text{ kg}$\nb) $4\\text{ tấn } 500\\text{ kg} = ..........\\text{ kg}$\nc) $8\\text{ phút } 30\\text{ giây} = ..........\\text{ giây}$\nd) $\\frac{1}{10}\\text{ thế kỉ} = ..........\\text{ năm}$", "Bài giải:\na) $7\\text{ yến } 8\\text{ kg} = 78\\text{ kg}$\nb) $4\\text{ tấn } 500\\text{ kg} = 4500\\text{ kg}$\nc) $8\\text{ phút } 30\\text{ giây} = 480\\text{ giây} + 30\\text{ giây} = 510\\text{ giây}$\nd) $\\frac{1}{10}\\text{ thế kỉ} = 100 : 10 = 10\\text{ năm}$\nĐáp số: a) 78; b) 4500; c) 510; d) 10", "a) 78; b) 4500; c) 510; d) 10", 4, 1.0),
            make_essay(3, "Tính giá trị của biểu thức:\n$A = x + y - 120$ với $x = 450, y = 270$", "Bài giải:\nVới $x = 450$ và $y = 270$, biểu thức có giá trị là:\n$450 + 270 - 120 = 720 - 120 = 600$\nĐáp số: 600", "600", 4, 1.0),
            make_essay(4, "Một trang trại thu hoạch cam trong 3 ngày. Ngày thứ nhất thu được 15 tạ cam. Ngày thứ hai thu được nhiều hơn ngày thứ nhất 5 tạ. Ngày thứ ba thu được gấp đôi ngày thứ hai. Hỏi cả ba ngày trang trại thu được bao nhiêu tạ cam?", "Bài giải:\nNgày thứ hai trang trại thu được số tạ cam là:\n$15 + 5 = 20$ (tạ)\nNgày thứ ba trang trại thu được số tạ cam là:\n$20 \\times 2 = 40$ (tạ)\nCả ba ngày trang trại thu được số tạ cam là:\n$15 + 20 + 40 = 75$ (tạ)\nĐáp số: 75 tạ cam.", "75 tạ", 6, 1.5),
            make_essay(5, "Một hình vuông có cạnh dài 15 cm. Một hình chữ nhật có chiều rộng bằng cạnh hình vuông và chiều dài hơn chiều rộng 8 cm. Tính chu vi hình chữ nhật đó.", "Bài giải:\nChiều rộng hình chữ nhật là 15 cm.\nChiều dài hình chữ nhật là:\n$15 + 8 = 23$ (cm)\nChu vi hình chữ nhật là:\n$(23 + 15) \\times 2 = 38 \\times 2 = 76$ (cm)\nĐáp số: 76 cm.", "76 cm", 5, 1.5),
            make_essay(6, "Cho dãy số: 2, 4, 6, 8, ..., 200. Dãy số trên có tất cả bao nhiêu số hạng?", "Bài giải:\nKhoảng cách giữa hai số chẵn liên tiếp là 2 đơn vị.\nSố các số hạng của dãy là:\n$(200 - 2) : 2 + 1 = 198 : 2 + 1 = 99 + 1 = 100$ (số hạng)\nĐáp số: 100 số hạng.", "100 số hạng", 5, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08 (th4_gk1_de08)
    # =========================================================================
    exams["th4_gk1_de08"] = {
        "id": "th4_gk1_de08",
        "testNum": 8,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 8)",
        "grade": "4",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Số gồm 9 trăm nghìn, 4 nghìn, 8 chục viết là:", [
                "904 080",
                "940 080",
                "904 800",
                "940 800"
            ], 0, "Viết là 904 080."),
            make_mc(2, "Đổi 5 tấn 7 tạ ra tạ được:", [
                "57 tạ",
                "507 tạ",
                "570 tạ",
                "75 tạ"
            ], 0, "$5\\text{ tấn} = 50\\text{ tạ}$, $50 + 7 = 57$ tạ."),
            make_mc(3, "Góc tạo bởi hai kim đồng hồ lúc 4 giờ đúng là:", [
                "Góc tù",
                "Góc nhọn",
                "Góc vuông",
                "Góc bẹt"
            ], 0, "Lúc 4 giờ, góc tạo bởi hai kim lớn hơn góc vuông và nhỏ hơn góc bẹt nên là góc tù."),
            make_mc(4, "Làm tròn số 785 240 đến hàng trăm nghìn ta được số:", [
                "800 000",
                "700 000",
                "780 000",
                "790 000"
            ], 0, "Chữ số hàng chục nghìn là 8 ($\\ge 5$) nên làm tròn lên thành 800 000."),
            make_mc(5, "Năm 2024 thuộc thế kỉ nào?", [
                "Thế kỉ XXI",
                "Thế kỉ XX",
                "Thế kỉ XIX",
                "Thế kỉ XXII"
            ], 0, "Năm 2024 thuộc thế kỉ XXI (từ năm 2001 đến năm 2100)."),
            make_mc(6, "Tổng của số chẵn lớn nhất có 2 chữ số và số lẻ bé nhất có 3 chữ số là:", [
                "199",
                "198",
                "200",
                "201"
            ], 0, "Số chẵn lớn nhất có 2 chữ số là 98. Số lẻ bé nhất có 3 chữ số là 101. $98 + 101 = 199$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $528 410 + 261 380$\nb) $874 590 - 342 160$", "Bài giải:\na) $528 410 + 261 380 = 789 790$\nb) $874 590 - 342 160 = 532 430$\nĐáp số: a) 789 790; b) 532 430", "a) 789 790; b) 532 430", 4, 1.0),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) $5\\text{ tạ } 6\\text{ yến} = ..........\\text{ yến}$\nb) $8\\text{ tấn } 20\\text{ kg} = ..........\\text{ kg}$\nc) $5\\text{ phút } 45\\text{ giây} = ..........\\text{ giây}$\nd) $500\\text{ năm} = ..........\\text{ thế kỉ}$", "Bài giải:\na) $5\\text{ tạ } 6\\text{ yến} = 56\\text{ yến}$\nb) $8\\text{ tấn } 20\\text{ kg} = 8020\\text{ kg}$\nc) $5\\text{ phút } 45\\text{ giây} = 300\\text{ giây} + 45\\text{ giây} = 345\\text{ giây}$\nd) $500\\text{ năm} = 5\\text{ thế kỉ}$\nĐáp số: a) 56; b) 8020; c) 345; d) 5", "a) 56; b) 8020; c) 345; d) 5", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 315 200 = 241 800$", "Bài giải:\n$x = 241 800 + 315 200 = 557 000$\nĐáp số: $x = 557 000$", "x = 557 000", 4, 1.0),
            make_essay(4, "Một đoàn xe chở lương thực gồm 3 xe tải lớn, mỗi xe chở 40 tạ thóc và 5 xe tải nhỏ, mỗi xe chở 24 tạ thóc. Hỏi cả đoàn xe chở được tất cả bao nhiêu tấn thóc?", "Bài giải:\n3 xe tải lớn chở được số tạ thóc là:\n$40 \\times 3 = 120$ (tạ)\n5 xe tải nhỏ chở được số tạ thóc là:\n$24 \\times 5 = 120$ (tạ)\nCả đoàn xe chở được số tạ thóc là:\n$120 + 120 = 240$ (tạ)\nĐổi $240\\text{ tạ} = 24\\text{ tấn}$\nĐáp số: 24 tấn thóc.", "24 tấn", 6, 1.5),
            make_essay(5, "Một hình chữ nhật có chu vi là 84 cm. Chiều dài bằng 28 cm. Tính chiều rộng của hình chữ nhật đó.", "Bài giải:\nNửa chu vi hình chữ nhật là:\n$84 : 2 = 42$ (cm)\nChiều rộng hình chữ nhật là:\n$42 - 28 = 14$ (cm)\nĐáp số: 14 cm.", "14 cm", 5, 1.5),
            make_essay(6, "Tìm một số biết rằng nếu lấy số đó cộng với 125 rồi trừ đi 45 thì được số tròn trăm lớn nhất có 3 chữ số.", "Bài giải:\nSố tròn trăm lớn nhất có 3 chữ số là 900.\nGọi số cần tìm là $x$.\nTheo đề bài: $x + 125 - 45 = 900$\n$x + 80 = 900$\n$x = 900 - 80 = 820$\nĐáp số: 820.", "820", 5, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_th4_gk1_exams()
    print(f"Tổng số đề GK1 Toán 4: {len(ex)} (Kỳ vọng: 8 đề)")
