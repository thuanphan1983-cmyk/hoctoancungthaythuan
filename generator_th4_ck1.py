# -*- coding: utf-8 -*-
"""
HỆ THỐNG ĐỀ KIỂM TRA CUỐI HỌC KÌ 1 - TOÁN TIỂU HỌC (LỚP 4)
Bộ sách: KẾT NỐI TRI THỨC VỚI CUỘC SỐNG
Gồm 8 đề kiểm tra chuẩn hóa độc lập 100% (th4_ck1_de01 đến th4_ck1_de08).

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

def get_th4_ck1_exams():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 01 (th4_ck1_de01)
    # Chủ đề: Nông trường bò sữa và trồng trọt
    # =========================================================================
    exams["th4_ck1_de01"] = {
        "id": "th4_ck1_de01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 1)",
        "grade": "4",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $35 480 + 24 120$ là:", [
                "59 600",
                "59 500",
                "60 600",
                "58 600"
            ], 0, "$35 480 + 24 120 = 59 600$."),
            make_mc(2, "Nhân nhẩm $245 \\times 100$ ta được kết quả là:", [
                "2 450",
                "24 500",
                "245 000",
                "245"
            ], 1, "Thêm 2 chữ số 0 vào bên phải số 245 được 24 500."),
            make_mc(3, "Hai đường thẳng vuông góc với nhau tạo thành mấy góc vuông?", [
                "1 góc vuông",
                "2 góc vuông",
                "4 góc vuông",
                "3 góc vuông"
            ], 2, "Hai đường thẳng vuông góc cắt nhau tạo thành 4 góc vuông."),
            make_mc(4, "Tổng của hai số là 48, hiệu của hai số đó là 12. Số lớn là:", [
                "30",
                "18",
                "36",
                "24"
            ], 0, "Số lớn là: $(48 + 12) : 2 = 30$."),
            make_mc(5, "Tích của $125 \\times 8$ là:", [
                "1000",
                "100",
                "10 000",
                "800"
            ], 0, "$125 \\times 8 = 1000$."),
            make_mc(6, "Hình chữ nhật có chiều dài 25 cm, chiều rộng 12 cm. Diện tích của hình chữ nhật đó là:", [
                "300 $\\text{cm}^2$",
                "74 cm",
                "150 $\\text{cm}^2$",
                "300 cm"
            ], 0, "Diện tích: $25 \\times 12 = 300$ $\\text{cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $345 812 + 238 459$\nb) $682 450 - 345 180$\nc) $124 \\times 23$\nd) $4560 : 5$", "Bài giải:\na) $345 812 + 238 459 = 584 271$\nb) $682 450 - 345 180 = 337 270$\nc) $124 \\times 23 = 2852$\nd) $4560 : 5 = 912$\nĐáp số: a) 584 271; b) 337 270; c) 2852; d) 912", "a) 584 271; b) 337 270; c) 2852; d) 912", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$25 \\times 18 + 25 \\times 82$", "Bài giải:\n$25 \\times (18 + 82) = 25 \\times 100 = 2500$\nĐáp số: 2500", "2500", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 1450 = 250 \\times 4$", "Bài giải:\n$x - 1450 = 1000$\n$x = 1000 + 1450 = 2450$\nĐáp số: $x = 2450$", "x = 2450", 4, 1.0),
            make_essay(4, "Một nông trường có tất cả 450 con bò sữa và bê con. Biết số bò sữa nhiều hơn số bê con là 70 con. Hỏi nông trường đó có bao nhiêu con bò sữa, bao nhiêu con bê con?", "Bài giải:\nSố con bê con là:\n$(450 - 70) : 2 = 190$ (con)\nSố con bò sữa là:\n$190 + 70 = 260$ (con)\nĐáp số: Bò sữa: 260 con; Bê con: 190 con.", "Bò sữa: 260; Bê con: 190", 6, 1.5),
            make_essay(5, "Cho hình chữ nhật $ABCD$ có chiều dài $AB = 30\\text{ cm}$, chiều rộng $BC = 20\\text{ cm}$.\na) Nêu các cặp cạnh song song với nhau trong hình chữ nhật $ABCD$.\nb) Nêu các cặp cạnh vuông góc với nhau tại đỉnh $A$.\nc) Tính diện tích hình chữ nhật $ABCD$.", "Bài giải:\na) Các cặp cạnh song song là: $AB$ song song với $CD$; $AD$ song song với $BC$.\nb) Tại đỉnh $A$, cặp cạnh vuông góc là: $AB$ và $AD$.\nc) Diện tích hình chữ nhật là:\n$30 \\times 20 = 600$ ($\\text{cm}^2$)\nĐáp số: a) AB // CD, AD // BC; b) AB vuông góc AD; c) 600 $\\text{cm}^2$.", "a) AB // CD; b) AB ⊥ AD; c) 600 cm²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị của biểu thức sau:\n$A = 125 \\times 48$", "Bài giải:\nTa tách $48 = 8 \\times 6$.\n$A = 125 \\times 8 \\times 6 = 1000 \\times 6 = 6000$\nĐáp số: $A = 6000$", "A = 6000", 5, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 02 (th4_ck1_de02)
    # =========================================================================
    exams["th4_ck1_de02"] = {
        "id": "th4_ck1_de02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 2)",
        "grade": "4",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Tính: $48 500 - 16 200 = ?$", [
                "32 300",
                "32 200",
                "31 300",
                "32 400"
            ], 0, "$48 500 - 16 200 = 32 300$."),
            make_mc(2, "Kết quả của phép nhân $36 \\times 11$ là:", [
                "396",
                "366",
                "386",
                "406"
            ], 0, "$36 \\times 11 = 396$ (nhân nhẩm với 11: $3 + 6 = 9$, viết xen giữa được 396)."),
            make_mc(3, "Hai đường thẳng song song với nhau là hai đường thẳng:", [
                "Không bao giờ cắt nhau",
                "Cắt nhau tạo thành góc vuông",
                "Cắt nhau tạo thành góc nhọn",
                "Trùng nhau"
            ], 0, "Hai đường thẳng song song không bao giờ cắt nhau."),
            make_mc(4, "Tuổi của hai bố con cộng lại bằng 46 tuổi. Bố hơn con 28 tuổi. Tuổi của con là:", [
                "9 tuổi",
                "8 tuổi",
                "10 tuổi",
                "12 tuổi"
            ], 0, "Tuổi con là: $(46 - 28) : 2 = 9$ tuổi."),
            make_mc(5, "Tích của $240 \\times 30$ là:", [
                "7 200",
                "720",
                "72 000",
                "6 200"
            ], 0, "$24 \\times 3 = 72$, thêm hai chữ số 0 được 7 200."),
            make_mc(6, "Một hình vuông có chu vi 36 cm. Diện tích của hình vuông đó là:", [
                "81 $\\text{cm}^2$",
                "36 $\\text{cm}^2$",
                "72 $\\text{cm}^2$",
                "18 $\\text{cm}^2$"
            ], 0, "Cạnh hình vuông là $36 : 4 = 9$ cm. Diện tích là $9 \\times 9 = 81$ $\\text{cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $456 270 + 382 150$\nb) $748 590 - 425 360$\nc) $215 \\times 24$\nd) $3840 : 6$", "Bài giải:\na) $456 270 + 382 150 = 838 420$\nb) $748 590 - 425 360 = 323 230$\nc) $215 \\times 24 = 5160$\nd) $3840 : 6 = 640$\nĐáp số: a) 838 420; b) 323 230; c) 5160; d) 640", "a) 838 420; b) 323 230; c) 5160; d) 640", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$36 \\times 45 + 36 \\times 55$", "Bài giải:\n$36 \\times (45 + 55) = 36 \\times 100 = 3600$\nĐáp số: 3600", "3600", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 25 = 120 + 80$", "Bài giải:\n$x : 25 = 200$\n$x = 200 \\times 25 = 5000$\nĐáp số: $x = 5000$", "x = 5000", 4, 1.0),
            make_essay(4, "Hai lớp 4A và 4B thu gom được tất cả 360 kg giấy vụn để làm kế hoạch nhỏ. Biết rằng lớp 4A thu gom được nhiều hơn lớp 4B là 40 kg giấy vụn. Hỏi mỗi lớp thu gom được bao nhiêu ki-lô-gam giấy vụn?", "Bài giải:\nLớp 4B thu gom được số ki-lô-gam giấy vụn là:\n$(360 - 40) : 2 = 160$ (kg)\nLớp 4A thu gom được số ki-lô-gam giấy vụn là:\n$160 + 40 = 200$ (kg)\nĐáp số: Lớp 4A: 200 kg; Lớp 4B: 160 kg.", "4A: 200 kg; 4B: 160 kg", 6, 1.5),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chu vi là 120 m, chiều dài hơn chiều rộng 16 m.\na) Tính chiều dài và chiều rộng của mảnh vườn đó.\nb) Tính diện tích của mảnh vườn đó.", "Bài giải:\na) Nửa chu vi mảnh vườn là:\n$120 : 2 = 60$ (m)\nChiều rộng mảnh vườn là:\n$(60 - 16) : 2 = 22$ (m)\nChiều dài mảnh vườn là:\n$22 + 16 = 38$ (m)\nb) Diện tích mảnh vườn là:\n$38 \\times 22 = 836$ ($\\text{m}^2$)\nĐáp số: a) Dài: 38 m, Rộng: 22 m; b) Diện tích: 836 $\\text{m}^2$.", "a) Dài: 38 m, Rộng: 22 m; b) 836 m²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$B = 250 \\times 36 \\times 4$", "Bài giải:\n$B = (250 \\times 4) \\times 36 = 1000 \\times 36 = 36 000$\nĐáp số: $B = 36 000$", "B = 36 000", 4, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 03 (th4_ck1_de03)
    # =========================================================================
    exams["th4_ck1_de03"] = {
        "id": "th4_ck1_de03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 3)",
        "grade": "4",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Tính: $125 000 + 75 000 = ?$", [
                "200 000",
                "190 000",
                "20 000",
                "250 000"
            ], 0, "$125 000 + 75 000 = 200 000$."),
            make_mc(2, "Kết quả của phép nhân $45 \\times 11$ là:", [
                "495",
                "485",
                "455",
                "505"
            ], 0, "$4 + 5 = 9$, viết xen giữa được 495."),
            make_mc(3, "Hình bình hành có mấy cặp cạnh song song với nhau?", [
                "2 cặp cạnh",
                "1 cặp cạnh",
                "3 cặp cạnh",
                "4 cặp cạnh"
            ], 0, "Hình bình hành có 2 cặp cạnh đối diện song song và bằng nhau."),
            make_mc(4, "Hai thùng chứa tất cả 150 lít dầu. Thùng thứ nhất chứa nhiều hơn thùng thứ hai 30 lít dầu. Thùng thứ hai chứa số lít dầu là:", [
                "60 lít",
                "90 lít",
                "75 lít",
                "80 lít"
            ], 0, "Thùng thứ hai chứa: $(150 - 30) : 2 = 60$ lít."),
            make_mc(5, "Tích của $400 \\times 50$ là:", [
                "20 000",
                "2 000",
                "200 000",
                "200"
            ], 0, "$4 \\times 5 = 20$, thêm 3 chữ số 0 được 20 000."),
            make_mc(6, "Biểu thức $a \\times (b + c) = a \\times b + a \\times c$ là tính chất gì?", [
                "Nhân một số với một tổng",
                "Giao hoán của phép nhân",
                "Kết hợp của phép nhân",
                "Cộng hai số"
            ], 0, "Đây là tính chất nhân một số với một tổng.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $367 820 + 251 430$\nb) $894 560 - 471 280$\nc) $136 \\times 35$\nd) $5436 : 9$", "Bài giải:\na) $367 820 + 251 430 = 619 250$\nb) $894 560 - 471 280 = 423 280$\nc) $136 \\times 35 = 4760$\nd) $5436 : 9 = 604$\nĐáp số: a) 619 250; b) 423 280; c) 4760; d) 604", "a) 619 250; b) 423 280; c) 4760; d) 604", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$48 \\times 65 + 48 \\times 35$", "Bài giải:\n$48 \\times (65 + 35) = 48 \\times 100 = 4800$\nĐáp số: 4800", "4800", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 12 = 1440 + 360$", "Bài giải:\n$x \\times 12 = 1800$\n$x = 1800 : 12 = 150$\nĐáp số: $x = 150$", "x = 150", 4, 1.0),
            make_essay(4, "Một trường tiểu học có tất cả 780 học sinh. Số học sinh nữ nhiều hơn số học sinh nam là 60 học sinh. Hỏi trường tiểu học đó có bao nhiêu học sinh nam, bao nhiêu học sinh nữ?", "Bài giải:\nSố học sinh nam của trường là:\n$(780 - 60) : 2 = 360$ (học sinh)\nSố học sinh nữ của trường là:\n$360 + 60 = 420$ (học sinh)\nĐáp số: Nam: 360 học sinh; Nữ: 420 học sinh.", "Nam: 360; Nữ: 420", 6, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có chu vi là 160 m. Chiều dài hơn chiều rộng 20 m.\na) Tính chiều dài và chiều rộng mảnh đất đó.\nb) Người ta dành $\\frac{1}{4}$ diện tích đất để đào ao thả cá, phần còn lại trồng cây ăn quả. Tính diện tích phần đất trồng cây ăn quả.", "Bài giải:\na) Nửa chu vi mảnh đất là:\n$160 : 2 = 80$ (m)\nChiều rộng mảnh đất là:\n$(80 - 20) : 2 = 30$ (m)\nChiều dài mảnh vườn là:\n$30 + 20 = 50$ (m)\nb) Diện tích mảnh đất là:\n$50 \\times 30 = 1500$ ($\\text{m}^2$)\nDiện tích đất đào ao là:\n$1500 : 4 = 375$ ($\\text{m}^2$)\nDiện tích trồng cây ăn quả là:\n$1500 - 375 = 1125$ ($\\text{m}^2$)\nĐáp số: a) Dài: 50 m, Rộng: 30 m; b) 1125 $\\text{m}^2$.", "a) Dài: 50 m, Rộng: 30 m; b) 1125 m²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$C = 4 \\times 125 \\times 25 \\times 8$", "Bài giải:\n$C = (125 \\times 8) \\times (25 \\times 4) = 1000 \\times 100 = 100 000$\nĐáp số: $C = 100 000$", "C = 100 000", 4, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 04 (th4_ck1_de04)
    # =========================================================================
    exams["th4_ck1_de04"] = {
        "id": "th4_ck1_de04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 4)",
        "grade": "4",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Tính nhẩm: $5800 \\times 10 = ?$", [
                "58 000",
                "580",
                "580 000",
                "5 800"
            ], 0, "$5800 \\times 10 = 58 000$."),
            make_mc(2, "Số lớn nhất trong các số: 785 412; 785 421; 785 142; 785 241 là:", [
                "785 421",
                "785 412",
                "785 241",
                "785 142"
            ], 0, "So sánh hàng chục: 2 > 1 > 4. Số lớn nhất là 785 421."),
            make_mc(3, "Góc tạo bởi hai kim đồng hồ lúc 9 giờ đúng là:", [
                "Góc vuông",
                "Góc nhọn",
                "Góc tù",
                "Góc bẹt"
            ], 0, "Lúc 9 giờ đúng, kim phút chỉ số 12, kim giờ chỉ số 9 tạo thành góc vuông."),
            make_mc(4, "Tổng của hai số là 100, hiệu của hai số đó là 20. Số bé là:", [
                "40",
                "60",
                "50",
                "30"
            ], 0, "Số bé là: $(100 - 20) : 2 = 40$."),
            make_mc(5, "Tích của $35 \\times 20$ là:", [
                "700",
                "70",
                "7000",
                "600"
            ], 0, "$35 \\times 20 = 700$."),
            make_mc(6, "Một tấm bìa hình chữ nhật có chu vi 40 cm, chiều dài 12 cm. Chiều rộng của tấm bìa là:", [
                "8 cm",
                "10 cm",
                "6 cm",
                "14 cm"
            ], 0, "Nửa chu vi là $40 : 2 = 20$ cm. Chiều rộng là $20 - 12 = 8$ cm.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $412 580 + 356 290$\nb) $785 400 - 342 180$\nc) $245 \\times 18$\nd) $7280 : 8$", "Bài giải:\na) $412 580 + 356 290 = 768 870$\nb) $785 400 - 342 180 = 443 220$\nc) $245 \\times 18 = 4410$\nd) $7280 : 8 = 910$\nĐáp số: a) 768 870; b) 443 220; c) 4410; d) 910", "a) 768 870; b) 443 220; c) 4410; d) 910", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$54 \\times 78 + 54 \\times 22$", "Bài giải:\n$54 \\times (78 + 22) = 54 \\times 100 = 5400$\nĐáp số: 5400", "5400", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 3450 = 150 \\times 6$", "Bài giải:\n$x - 3450 = 900$\n$x = 900 + 3450 = 4350$\nĐáp số: $x = 4350$", "x = 4350", 4, 1.0),
            make_essay(4, "Một cửa hàng có tất cả 520 kg gạo tẻ và gạo nếp. Biết số gạo tẻ nhiều hơn số gạo nếp là 80 kg. Hỏi cửa hàng có bao nhiêu ki-lô-gam gạo tẻ, bao nhiêu ki-lô-gam gạo nếp?", "Bài giải:\nSố gạo nếp cửa hàng có là:\n$(520 - 80) : 2 = 220$ (kg)\nSố gạo tẻ cửa hàng có là:\n$220 + 80 = 300$ (kg)\nĐáp số: Gạo tẻ: 300 kg; Gạo nếp: 220 kg.", "Tẻ: 300 kg; Nếp: 220 kg", 6, 1.5),
            make_essay(5, "Một khu đất hình chữ nhật có chu vi là 140 m, chiều rộng kém chiều dài 18 m.\na) Tính chiều dài và chiều rộng của khu đất đó.\nb) Tính diện tích của khu đất đó.", "Bài giải:\na) Nửa chu vi khu đất là:\n$140 : 2 = 70$ (m)\nChiều rộng khu đất là:\n$(70 - 18) : 2 = 26$ (m)\nChiều dài khu đất là:\n$26 + 18 = 44$ (m)\nb) Diện tích khu đất là:\n$44 \\times 26 = 1144$ ($\\text{m}^2$)\nĐáp số: a) Dài: 44 m, Rộng: 26 m; b) Diện tích: 1144 $\\text{m}^2$.", "a) Dài: 44 m, Rộng: 26 m; b) 1144 m²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$D = 78 \\times 99 + 78$", "Bài giải:\n$D = 78 \\times (99 + 1) = 78 \\times 100 = 7800$\nĐáp số: $D = 7800$", "D = 7800", 4, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 05 (th4_ck1_de05)
    # =========================================================================
    exams["th4_ck1_de05"] = {
        "id": "th4_ck1_de05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 5)",
        "grade": "4",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Tính: $75 420 + 24 580 = ?$", [
                "100 000",
                "99 000",
                "101 000",
                "90 000"
            ], 0, "$75 420 + 24 580 = 100 000$."),
            make_mc(2, "Nhân nhẩm $58 \\times 11$ ta được:", [
                "638",
                "538",
                "648",
                "588"
            ], 0, "$5 + 8 = 13$, viết 3 ở giữa, nhớ 1 sang 5 thành 6. Kết quả là 638."),
            make_mc(3, "Trong hình vuông, hai đường chéo có tính chất gì?", [
                "Vuông góc với nhau",
                "Song song với nhau",
                "Không cắt nhau",
                "Không vuông góc"
            ], 0, "Hai đường chéo của hình vuông vuông góc với nhau."),
            make_mc(4, "Tổng của hai số là 84, số lớn hơn số bé 16 đơn vị. Số lớn là:", [
                "50",
                "34",
                "48",
                "52"
            ], 0, "Số lớn là: $(84 + 16) : 2 = 50$."),
            make_mc(5, "Tích của $150 \\times 40$ là:", [
                "6 000",
                "600",
                "60 000",
                "5 000"
            ], 0, "$15 \\times 4 = 60$, thêm 2 chữ số 0 được 6 000."),
            make_mc(6, "Một mảnh vườn hình chữ nhật có diện tích 240 $\\text{m}^2$, chiều dài 20 m. Chiều rộng là:", [
                "12 m",
                "14 m",
                "10 m",
                "16 m"
            ], 0, "Chiều rộng là: $240 : 20 = 12$ m.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $528 410 + 261 390$\nb) $894 720 - 451 380$\nc) $142 \\times 25$\nd) $4832 : 8$", "Bài giải:\na) $528 410 + 261 390 = 789 800$\nb) $894 720 - 451 380 = 443 340$\nc) $142 \\times 25 = 3550$\nd) $4832 : 8 = 604$\nĐáp số: a) 789 800; b) 443 340; c) 3550; d) 604", "a) 789 800; b) 443 340; c) 3550; d) 604", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$25 \\times 34 \\times 4$", "Bài giải:\n$(25 \\times 4) \\times 34 = 100 \\times 34 = 3400$\nĐáp số: 3400", "3400", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 15 = 45 + 55$", "Bài giải:\n$x : 15 = 100$\n$x = 100 \\times 15 = 1500$\nĐáp số: $x = 1500$", "x = 1500", 4, 1.0),
            make_essay(4, "Một đoàn tàu chở hàng có tất cả 480 tấn hàng gồm gạo và ngô. Biết khối lượng gạo nhiều hơn khối lượng ngô là 60 tấn. Hỏi đoàn tàu chở bao nhiêu tấn gạo, bao nhiêu tấn ngô?", "Bài giải:\nĐoàn tàu chở số tấn ngô là:\n$(480 - 60) : 2 = 210$ (tấn)\nĐoàn tàu chở số tấn gạo là:\n$210 + 60 = 270$ (tấn)\nĐáp số: Gạo: 270 tấn; Ngô: 210 tấn.", "Gạo: 270 tấn; Ngô: 210 tấn", 6, 1.5),
            make_essay(5, "Một sân bóng đá hình chữ nhật có chu vi là 180 m. Chiều dài hơn chiều rộng 24 m.\na) Tính chiều dài và chiều rộng của sân bóng đá đó.\nb) Tính diện tích của sân bóng đá đó.", "Bài giải:\na) Nửa chu vi sân bóng đá là:\n$180 : 2 = 90$ (m)\nChiều rộng sân bóng đá là:\n$(90 - 24) : 2 = 33$ (m)\nChiều dài sân bóng đá là:\n$33 + 24 = 57$ (m)\nb) Diện tích sân bóng đá là:\n$57 \\times 33 = 1881$ ($\\text{m}^2$)\nĐáp số: a) Dài: 57 m, Rộng: 33 m; b) Diện tích: 1881 $\\text{m}^2$.", "a) Dài: 57 m, Rộng: 33 m; b) 1881 m²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$E = 15 \\times 2 + 15 \\times 3 + 15 \\times 5$", "Bài giải:\n$E = 15 \\times (2 + 3 + 5) = 15 \\times 10 = 150$\nĐáp số: $E = 150$", "E = 150", 4, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 06 (th4_ck1_de06)
    # =========================================================================
    exams["th4_ck1_de06"] = {
        "id": "th4_ck1_de06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 6)",
        "grade": "4",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Tính: $350 000 - 120 000 = ?$", [
                "230 000",
                "220 000",
                "240 000",
                "130 000"
            ], 0, "$350 000 - 120 000 = 230 000$."),
            make_mc(2, "Kết quả của phép nhân $64 \\times 11$ là:", [
                "704",
                "694",
                "714",
                "684"
            ], 0, "$6 + 4 = 10$, viết 0 ở giữa, nhớ 1 sang 6 được 704."),
            make_mc(3, "Trong hình bình hành $ABCD$, cạnh $AB$ song song với cạnh nào?", [
                "$CD$",
                "$BC$",
                "$AD$",
                "$AC$"
            ], 0, "Cạnh $AB$ song song với cạnh đối diện là $CD$."),
            make_mc(4, "Một lớp học có 38 học sinh. Số bạn nam ít hơn số bạn nữ là 4 bạn. Số bạn nam của lớp là:", [
                "17 bạn",
                "21 bạn",
                "16 bạn",
                "18 bạn"
            ], 0, "Số bạn nam là: $(38 - 4) : 2 = 17$ bạn."),
            make_mc(5, "Tích của $120 \\times 50$ là:", [
                "6 000",
                "600",
                "60 000",
                "1 250"
            ], 0, "$12 \\times 5 = 60$, thêm 2 số 0 được 6 000."),
            make_mc(6, "Diện tích hình chữ nhật có chiều dài 18 cm, chiều rộng 15 cm là:", [
                "270 $\\text{cm}^2$",
                "66 cm",
                "135 $\\text{cm}^2$",
                "280 $\\text{cm}^2$"
            ], 0, "$18 \\times 15 = 270$ $\\text{cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $428 150 + 261 480$\nb) $764 500 - 328 170$\nc) $165 \\times 24$\nd) $6545 : 7$", "Bài giải:\na) $428 150 + 261 480 = 689 630$\nb) $764 500 - 328 170 = 436 330$\nc) $165 \\times 24 = 3960$\nd) $6545 : 7 = 935$\nĐáp số: a) 689 630; b) 436 330; c) 3960; d) 935", "a) 689 630; b) 436 330; c) 3960; d) 935", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$75 \\times 38 + 75 \\times 62$", "Bài giải:\n$75 \\times (38 + 62) = 75 \\times 100 = 7500$\nĐáp số: 7500", "7500", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 15 = 3500 + 1000$", "Bài giải:\n$x \\times 15 = 4500$\n$x = 4500 : 15 = 300$\nĐáp số: $x = 300$", "x = 300", 4, 1.0),
            make_essay(4, "Một thư viện trường học có tất cả 960 cuốn sách gồm sách giáo khoa và truyện thiếu nhi. Biết số sách giáo khoa nhiều hơn số truyện thiếu nhi là 120 cuốn. Hỏi thư viện có bao nhiêu cuốn sách mỗi loại?", "Bài giải:\nSố truyện thiếu nhi thư viện có là:\n$(960 - 120) : 2 = 420$ (cuốn)\nSố sách giáo khoa thư viện có là:\n$420 + 120 = 540$ (cuốn)\nĐáp số: Sách giáo khoa: 540 cuốn; Truyện thiếu nhi: 420 cuốn.", "SGK: 540 cuốn; Truyện: 420 cuốn", 6, 1.5),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chu vi là 150 m. Chiều rộng kém chiều dài 15 m.\na) Tính chiều dài và chiều rộng thửa ruộng đó.\nb) Tính diện tích thửa ruộng đó.", "Bài giải:\na) Nửa chu vi thửa ruộng là:\n$150 : 2 = 75$ (m)\nChiều rộng thửa ruộng là:\n$(75 - 15) : 2 = 30$ (m)\nChiều dài thửa ruộng là:\n$30 + 15 = 45$ (m)\nb) Diện tích thửa ruộng là:\n$45 \\times 30 = 1350$ ($\\text{m}^2$)\nĐáp số: a) Dài: 45 m, Rộng: 30 m; b) Diện tích: 1350 $\\text{m}^2$.", "a) Dài: 45 m, Rộng: 30 m; b) 1350 m²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$F = 125 \\times 72$", "Bài giải:\nTa tách $72 = 8 \\times 9$.\n$F = 125 \\times 8 \\times 9 = 1000 \\times 9 = 9000$\nĐáp số: $F = 9000$", "F = 9000", 4, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 07 (th4_ck1_de07)
    # =========================================================================
    exams["th4_ck1_de07"] = {
        "id": "th4_ck1_de07",
        "testNum": 7,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 7)",
        "grade": "4",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Tính: $240 000 + 360 000 = ?$", [
                "600 000",
                "500 000",
                "700 000",
                "60 000"
            ], 0, "$240 000 + 360 000 = 600 000$."),
            make_mc(2, "Nhân nhẩm $73 \\times 11$ ta được:", [
                "803",
                "793",
                "813",
                "783"
            ], 0, "$7 + 3 = 10$, viết 0 ở giữa nhớ 1 sang 7 được 803."),
            make_mc(3, "Góc tù là góc:", [
                "Lớn hơn góc vuông và nhỏ hơn góc bẹt",
                "Nhỏ hơn góc vuông",
                "Lớn hơn góc bẹt",
                "Bằng góc vuông"
            ], 0, "Góc tù lớn hơn góc vuông và nhỏ hơn góc bẹt."),
            make_mc(4, "Tổng của hai số là 64, hiệu của hai số đó là 14. Số bé là:", [
                "25",
                "39",
                "24",
                "30"
            ], 0, "Số bé là: $(64 - 14) : 2 = 25$."),
            make_mc(5, "Tích của $250 \\times 40$ là:", [
                "10 000",
                "1 000",
                "100 000",
                "25 000"
            ], 0, "$25 \\times 4 = 100$, thêm 2 số 0 được 10 000."),
            make_mc(6, "Chu vi hình vuông là 48 cm. Diện tích của hình vuông đó là:", [
                "144 $\\text{cm}^2$",
                "96 $\\text{cm}^2$",
                "120 $\\text{cm}^2$",
                "100 $\\text{cm}^2$"
            ], 0, "Cạnh: $48 : 4 = 12$ cm. Diện tích: $12 \\times 12 = 144$ $\\text{cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $345 670 + 281 450$\nb) $852 340 - 361 280$\nc) $174 \\times 26$\nd) $5840 : 8$", "Bài giải:\na) $345 670 + 281 450 = 627 120$\nb) $852 340 - 361 280 = 491 060$\nc) $174 \\times 26 = 4524$\nd) $5840 : 8 = 730$\nĐáp số: a) 627 120; b) 491 060; c) 4524; d) 730", "a) 627 120; b) 491 060; c) 4524; d) 730", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$64 \\times 75 + 64 \\times 25$", "Bài giải:\n$64 \\times (75 + 25) = 64 \\times 100 = 6400$\nĐáp số: 6400", "6400", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 20 = 450 - 150$", "Bài giải:\n$x : 20 = 300$\n$x = 300 \\times 20 = 6000$\nĐáp số: $x = 6000$", "x = 6000", 4, 1.0),
            make_essay(4, "Một kho hàng có tất cả 650 bao gạo gồm gạo tẻ và gạo nếp. Số bao gạo tẻ nhiều hơn số bao gạo nếp là 90 bao. Hỏi trong kho có bao nhiêu bao gạo tẻ, bao nhiêu bao gạo nếp?", "Bài giải:\nSố bao gạo nếp trong kho là:\n$(650 - 90) : 2 = 280$ (bao)\nSố bao gạo tẻ trong kho là:\n$280 + 90 = 370$ (bao)\nĐáp số: Gạo tẻ: 370 bao; Gạo nếp: 280 bao.", "Tẻ: 370 bao; Nếp: 280 bao", 6, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có chu vi là 132 m. Chiều dài hơn chiều rộng 14 m.\na) Tính chiều dài và chiều rộng của mảnh đất đó.\nb) Tính diện tích mảnh đất đó.", "Bài giải:\na) Nửa chu vi mảnh đất là:\n$132 : 2 = 66$ (m)\nChiều rộng mảnh đất là:\n$(66 - 14) : 2 = 26$ (m)\nChiều dài mảnh đất là:\n$26 + 14 = 40$ (m)\nb) Diện tích mảnh đất là:\n$40 \\times 26 = 1040$ ($\\text{m}^2$)\nĐáp số: a) Dài: 40 m, Rộng: 26 m; b) Diện tích: 1040 $\\text{m}^2$.", "a) Dài: 40 m, Rộng: 26 m; b) 1040 m²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$G = 24 \\times 50$", "Bài giải:\n$G = (24 : 2) \\times (50 \\times 2) = 12 \\times 100 = 1200$\nĐáp số: $G = 1200$", "G = 1200", 4, 1.0)
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08 (th4_ck1_de08)
    # =========================================================================
    exams["th4_ck1_de08"] = {
        "id": "th4_ck1_de08",
        "testNum": 8,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 4 (ĐỀ SỐ 8)",
        "grade": "4",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Tính: $450 000 + 250 000 = ?$", [
                "700 000",
                "600 000",
                "800 000",
                "650 000"
            ], 0, "$450 000 + 250 000 = 700 000$."),
            make_mc(2, "Nhân nhẩm $82 \\times 11$ ta được:", [
                "902",
                "892",
                "912",
                "882"
            ], 0, "$8 + 2 = 10$, viết 0 ở giữa, nhớ 1 sang 8 thành 9. Kết quả là 902."),
            make_mc(3, "Hình chữ nhật có mấy góc vuông?", [
                "4 góc vuông",
                "2 góc vuông",
                "3 góc vuông",
                "1 góc vuông"
            ], 0, "Hình chữ nhật có 4 góc vuông tại 4 đỉnh."),
            make_mc(4, "Tổng của hai số là 72, hiệu của hai số đó là 16. Số lớn là:", [
                "44",
                "28",
                "40",
                "48"
            ], 0, "Số lớn là: $(72 + 16) : 2 = 44$."),
            make_mc(5, "Tích của $160 \\times 50$ là:", [
                "8 000",
                "800",
                "80 000",
                "1 650"
            ], 0, "$16 \\times 5 = 80$, thêm hai số 0 được 8 000."),
            make_mc(6, "Một mảnh vườn hình chữ nhật có chu vi là 50 m, chiều rộng 10 m. Chiều dài là:", [
                "15 m",
                "20 m",
                "25 m",
                "30 m"
            ], 0, "Nửa chu vi là $50 : 2 = 25$ m. Chiều dài là $25 - 10 = 15$ m.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $512 360 + 274 580$\nb) $896 420 - 452 170$\nc) $185 \\times 34$\nd) $6840 : 9$", "Bài giải:\na) $512 360 + 274 580 = 786 940$\nb) $896 420 - 452 170 = 444 250$\nc) $185 \\times 34 = 6290$\nd) $6840 : 9 = 760$\nĐáp số: a) 786 940; b) 444 250; c) 6290; d) 760", "a) 786 940; b) 444 250; c) 6290; d) 760", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$85 \\times 47 + 85 \\times 53$", "Bài giải:\n$85 \\times (47 + 53) = 85 \\times 100 = 8500$\nĐáp số: 8500", "8500", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 2800 = 120 \\times 5$", "Bài giải:\n$x - 2800 = 600$\n$x = 600 + 2800 = 3400$\nĐáp số: $x = 3400$", "x = 3400", 4, 1.0),
            make_essay(4, "Một cửa hàng ngày thứ nhất và ngày thứ hai bán được tất cả 420 kg đường. Biết ngày thứ nhất bán được nhiều hơn ngày thứ hai là 60 kg đường. Hỏi mỗi ngày cửa hàng bán được bao nhiêu ki-lô-gam đường?", "Bài giải:\nNgày thứ hai cửa hàng bán được số ki-lô-gam đường là:\n$(420 - 60) : 2 = 180$ (kg)\nNgày thứ nhất cửa hàng bán được số ki-lô-gam đường là:\n$180 + 60 = 240$ (kg)\nĐáp số: Ngày thứ nhất: 240 kg; Ngày thứ hai: 180 kg.", "Ngày 1: 240 kg; Ngày 2: 180 kg", 6, 1.5),
            make_essay(5, "Một khu vườn hình chữ nhật có chu vi là 110 m. Chiều dài hơn chiều rộng 15 m.\na) Tính chiều dài và chiều rộng của khu vườn đó.\nb) Tính diện tích của khu vườn đó.", "Bài giải:\na) Nửa chu vi khu vườn là:\n$110 : 2 = 55$ (m)\nChiều rộng khu vườn là:\n$(55 - 15) : 2 = 20$ (m)\nChiều dài khu vườn là:\n$20 + 15 = 35$ (m)\nb) Diện tích khu vườn là:\n$35 \\times 20 = 700$ ($\\text{m}^2$)\nĐáp số: a) Dài: 35 m, Rộng: 20 m; b) Diện tích: 700 $\\text{m}^2$.", "a) Dài: 35 m, Rộng: 20 m; b) 700 m²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$H = 25 \\times 44$", "Bài giải:\n$H = 25 \\times 4 \\times 11 = 100 \\times 11 = 1100$\nĐáp số: $H = 1100$", "H = 1100", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_th4_ck1_exams()
    print(f"Tổng số đề CK1 Toán 4: {len(ex)} (Kỳ vọng: 8 đề)")
