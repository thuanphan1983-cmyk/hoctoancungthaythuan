# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 3: CÁC PHÉP TÍNH VỚI SỐ THẬP PHÂN (PHẦN 2: BÀI 19 ĐẾN BÀI 21) - TOÁN 5 KNTT
Gồm 9 đề kiểm tra (mỗi bài 3 đề):
- Bài 19: Phép chia số thập phân (th5_b19_test1, th5_b19_test2, th5_b19_test3)
- Bài 20: Chia số thập phân cho 10, 100, 1000... hoặc cho 0,1; 0,01; 0,001... (th5_b20_test1, th5_b20_test2, th5_b20_test3)
- Bài 21: Luyện tập chung Chủ đề 3 (th5_b21_test1, th5_b21_test2, th5_b21_test3)
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

def get_ch3_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 19: PHÉP CHIA SỐ THẬP PHÂN
    # =========================================================================
    exams["th5_b19_test1"] = {
        "id": "th5_b19_test1",
        "lessonId": "th5_b19",
        "lessonNum": 19,
        "testNum": 1,
        "title": "Bài 19: Phép chia số thập phân - Đề số 1",
        "topic": "Phép chia số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Thương của phép chia $42,6 : 3$ là:", ["14,2", "14,3", "13,2", "15,2"], 0, "$42,6 : 3 = 14,2$."),
            make_mc(2, "Khi chia $15$ cho $4$ ta được số thập phân là:", ["3,5", "3,75", "3,25", "3,85"], 1, "$15 : 4 = 3,75$."),
            make_mc(3, "Kết quả của phép chia $23,5 : 5$ là:", ["4,5", "4,7", "4,3", "5,7"], 1, "$23,5 : 5 = 4,7$."),
            make_mc(4, "Một mảnh vải dài 18 m, may được 6 bộ quần áo như nhau. Hỏi may mỗi bộ quần áo hết bao nhiêu mét vải?", [
                "2,5 m",
                "3 m",
                "3,5 m",
                "4 m"
            ], 1, "Mỗi bộ quần áo hết: $18 : 6 = 3$ m."),
            make_mc(5, "Tìm $x$ biết $x \\times 4 = 14,6$. Giá trị của $x$ là:", [
                "3,65",
                "3,55",
                "3,45",
                "3,75"
            ], 0, "$x = 14,6 : 4 = 3,65$."),
            make_mc(6, "Trong phép chia $21,8 : 3,5$, số dư khi lấy thương có 1 chữ số ở phần thập phân là:", [
                "0,8",
                "0,08",
                "0,1",
                "0,01"
            ], 0, "Ta có $218 : 35 = 6$ dư 8. Viết dấu phẩy: thương 6,2 và số dư 0,08 hoặc xét: $21,8 - 3,5 \\times 6,2 = 21,8 - 21,7 = 0,1$. Vậy số dư là 0,1.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $75,6 : 6$\nb) $89 : 4$", "Bài giải:\na) $75,6 : 6 = 12,6$\nb) $89 : 4 = 22,25$\nĐáp số: a) 12,6; b) 22,25", "a) 12,6; b) 22,25", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\n$(24,8 + 15,2) : 5$", "Bài giải:\n$(24,8 + 15,2) : 5 = 40 : 5 = 8$\nĐáp số: 8", "8", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 8 = 36,4 + 19,6$", "Bài giải:\n$x \\times 8 = 56$\n$x = 56 : 8 = 7$\nĐáp số: $x = 7$", "x = 7", 4, 1.0),
            make_essay(4, "Một xưởng dệt dệt được 315 m vải trong 7 ngày. Hỏi với mức làm như thế, để dệt được 450 m vải thì xưởng đó cần bao nhiêu ngày?", "Bài giải:\nMỗi ngày xưởng dệt được số mét vải là:\n$315 : 7 = 45$ (m)\nSố ngày để xưởng dệt được 450 m vải là:\n$450 : 45 = 10$ (ngày)\nĐáp số: 10 ngày.", "10 ngày", 6, 1.5),
            make_essay(5, "Một thửa ruộng hình chữ nhật có diện tích là 336 $\\text{m}^2$, chiều rộng là 14 m.\na) Tính chiều dài thửa ruộng đó.\nb) Người ta đóng cọc rào xung quanh thửa ruộng, hai cọc cách nhau 2 m. Hỏi cần bao nhiêu cái cọc?", "Bài giải:\na) Chiều dài thửa ruộng là:\n$336 : 14 = 24$ (m)\nb) Chu vi thửa ruộng là:\n$(24 + 14) \\times 2 = 76$ (m)\nSố cọc cần dùng là:\n$76 : 2 = 38$ (cái cọc)\nĐáp số: a) 24 m; b) 38 cái cọc.", "a) 24 m; b) 38 cọc", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị của biểu thức:\n$A = (12,5 \\times 4 - 50) : 2,75$", "Bài giải:\nTa tính giá trị trong ngoặc trước:\n$12,5 \\times 4 = 50$\n$50 - 50 = 0$\nBiểu thức trở thành: $0 : 2,75 = 0$\nĐáp số: $A = 0$", "A = 0", 4, 1.0)
        ]
    }

    exams["th5_b19_test2"] = {
        "id": "th5_b19_test2",
        "lessonId": "th5_b19",
        "lessonNum": 19,
        "testNum": 2,
        "title": "Bài 19: Phép chia số thập phân - Đề số 2",
        "topic": "Phép chia số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép chia $75 : 2,5$ là:", ["30", "3", "300", "0,3"], 0, "$75 : 2,5 = 750 : 25 = 30$."),
            make_mc(2, "Tính: $19,5 : 1,5 = ?$", ["13", "12", "14", "13,5"], 0, "$19,5 : 1,5 = 195 : 15 = 13$."),
            make_mc(3, "Thương của phép chia $3,6 : 0,4$ là:", ["9", "0,9", "90", "0,09"], 0, "$3,6 : 0,4 = 36 : 4 = 9$."),
            make_mc(4, "Một mảnh đất hình chữ nhật có diện tích $86,4\\text{ m}^2$, chiều dài 12 m. Chiều rộng mảnh đất là:", [
                "7,2 m",
                "7,4 m",
                "6,8 m",
                "8,2 m"
            ], 0, "$86,4 : 12 = 7,2$ m."),
            make_mc(5, "Tìm $x$ biết $x \\times 1,2 = 4,8$. Giá trị của $x$ là:", [
                "4",
                "0,4",
                "40",
                "4,8"
            ], 0, "$x = 4,8 : 1,2 = 4$."),
            make_mc(6, "Kết quả của phép tính $25 : 0,5$ bằng:", [
                "50",
                "12,5",
                "5",
                "10"
            ], 0, "$25 : 0,5 = 25 \\times 2 = 50$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $91,8 : 3,4$\nb) $153 : 4,5$", "Bài giải:\na) $91,8 : 3,4 = 918 : 34 = 27$\nb) $153 : 4,5 = 1530 : 45 = 34$\nĐáp số: a) 27; b) 34", "a) 27; b) 34", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\n$64,8 : 2,4 - 15,5$", "Bài giải:\n$64,8 : 2,4 = 27$\n$27 - 15,5 = 11,5$\nĐáp số: 11,5", "11,5", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 3,5 = 45,5 - 17,5$", "Bài giải:\n$x \\times 3,5 = 28$\n$x = 28 : 3,5 = 8$\nĐáp số: $x = 8$", "x = 8", 4, 1.0),
            make_essay(4, "Một ô tô chạy quãng đường 162 km trong 3,6 giờ. Hỏi với vận tốc như thế, ô tô đó chạy quãng đường 225 km thì hết bao nhiêu giờ?", "Bài giải:\nVận tốc của ô tô là:\n$162 : 3,6 = 45$ (km/h)\nThời gian ô tô chạy hết quãng đường 225 km là:\n$225 : 45 = 5$ (giờ)\nĐáp số: 5 giờ.", "5 giờ", 6, 1.5),
            make_essay(5, "Có 45 lít nước mắm đựng đều vào các can, mỗi can chứa 2,5 lít. Người ta đã bán đi một nửa số can nước mắm đó với giá 75 000 đồng một can. Hỏi người ta đã thu về bao nhiêu tiền?", "Bài giải:\nSố can nước mắm có tất cả là:\n$45 : 2,5 = 18$ (can)\nSố can nước mắm đã bán là:\n$18 : 2 = 9$ (can)\nSố tiền thu về là:\n$9 \\times 75 000 = 675 000$ (đồng)\nĐáp số: 675 000 đồng.", "675 000 đồng", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị của biểu thức:\n$B = \\frac{4,8 \\times 0,5 \\times 16}{1,2 \\times 8}$", "Bài giải:\nBiến đổi:\n$B = \\frac{(4,8 : 1,2) \\times (0,5 \\times 16)}{8} = \\frac{4 \\times 8}{8} = 4$\nĐáp số: $B = 4$", "B = 4", 4, 1.0)
        ]
    }

    exams["th5_b19_test3"] = {
        "id": "th5_b19_test3",
        "lessonId": "th5_b19",
        "lessonNum": 19,
        "testNum": 3,
        "title": "Bài 19: Phép chia số thập phân - Đề số 3",
        "topic": "Phép chia số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $14,4 : 1,2 = ?$", ["12", "1,2", "120", "14"], 0, "$14,4 : 1,2 = 144 : 12 = 12$."),
            make_mc(2, "Kết quả của phép chia $8,75 : 2,5$ là:", ["3,5", "35", "0,35", "3,25"], 0, "$8,75 : 2,5 = 87,5 : 25 = 3,5$."),
            make_mc(3, "Tìm số dư của phép chia $25 : 3$ khi thương lấy đến hai chữ số ở phần thập phân:", [
                "0,01",
                "0,1",
                "1",
                "0,001"
            ], 0, "$25 : 3 = 8,33$ (dư 0,01) vì $25 - 3 \\times 8,33 = 25 - 24,99 = 0,01$."),
            make_mc(4, "Một tổ công nhân làm 8 giờ được 54,4 sản phẩm. Trung bình mỗi giờ tổ đó làm được số sản phẩm là:", [
                "6,8 sản phẩm",
                "6,6 sản phẩm",
                "7,2 sản phẩm",
                "6,4 sản phẩm"
            ], 0, "$54,4 : 8 = 6,8$ sản phẩm."),
            make_mc(5, "Tìm $x$ biết $x \\times 2,4 = 18$. Giá trị của $x$ là:", [
                "7,5",
                "7,2",
                "8,5",
                "6,5"
            ], 0, "$x = 18 : 2,4 = 7,5$."),
            make_mc(6, "Thương của hai số là 4,5. Nếu số bị chia gấp lên 2 lần và giữ nguyên số chia thì thương mới là:", [
                "9",
                "4,5",
                "2,25",
                "18"
            ], 0, "Số bị chia gấp 2 lần thì thương gấp 2 lần: $4,5 \\times 2 = 9$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $86,4 : 2,7$\nb) $112,5 : 4,5$", "Bài giải:\na) $86,4 : 2,7 = 864 : 27 = 32$\nb) $112,5 : 4,5 = 1125 : 45 = 25$\nĐáp số: a) 32; b) 25", "a) 32; b) 25", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\n$(58,5 - 16,5) : 3,5$", "Bài giải:\n$(58,5 - 16,5) : 3,5 = 42 : 3,5 = 420 : 35 = 12$\nĐáp số: 12", "12", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 1,6 = 15,5 - 10,5$", "Bài giải:\n$x : 1,6 = 5$\n$x = 5 \\times 1,6 = 8$\nĐáp số: $x = 8$", "x = 8", 4, 1.0),
            make_essay(4, "Người ta đổ 67,5 lít dầu mè vào các chai, mỗi chai chứa được 0,75 lít. Sau đó người ta đóng tất cả số chai dầu đó vào các thùng, mỗi thùng chứa 15 chai. Hỏi đóng được tất cả bao nhiêu thùng?", "Bài giải:\nSố chai dầu mè rót được là:\n$67,5 : 0,75 = 90$ (chai)\nSố thùng dầu mè đóng được là:\n$90 : 15 = 6$ (thùng)\nĐáp số: 6 thùng.", "6 thùng", 6, 1.5),
            make_essay(5, "Một người đi xe máy khởi hành từ A lúc 7 giờ 30 phút và đến B lúc 10 giờ cùng ngày. Quãng đường AB dài 112,5 km. Dọc đường người đó nghỉ 30 phút. Tính vận tốc của người đi xe máy.", "Bài giải:\nThời gian người đó đi từ A đến B (kể cả nghỉ) là:\n10 giờ - 7 giờ 30 phút = 2 giờ 30 phút\nThời gian thực tế người đó đi trên đường là:\n2 giờ 30 phút - 30 phút = 2 giờ\nVận tốc của người đi xe máy là:\n$112,5 : 2 = 56,25$ (km/h)\nĐáp số: 56,25 km/h.", "56,25 km/h", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$C = 13,5 : 0,5 + 13,5 : 0,25 + 13,5 : 0,125$", "Bài giải:\nChia cho 0,5 bằng nhân với 2; chia cho 0,25 bằng nhân 4; chia cho 0,125 bằng nhân 8.\n$C = 13,5 \\times 2 + 13,5 \\times 4 + 13,5 \\times 8$\n$C = 13,5 \\times (2 + 4 + 8) = 13,5 \\times 14 = 189$\nĐáp số: $C = 189$", "C = 189", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 20: CHIA SỐ THẬP PHÂN CHO 10, 100, 1000... HOẶC CHO 0,1; 0,01...
    # =========================================================================
    exams["th5_b20_test1"] = {
        "id": "th5_b20_test1",
        "lessonId": "th5_b20",
        "lessonNum": 20,
        "testNum": 1,
        "title": "Bài 20: Chia số thập phân cho 10, 100... hoặc cho 0,1; 0,01... - Đề số 1",
        "topic": "Chia cho 10, 100... hoặc cho 0,1; 0,01...",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn chia một số thập phân cho 10, 100, 1000... ta chỉ việc:", [
                "Chuyển dấu phẩy sang bên trái 1, 2, 3... chữ số",
                "Chuyển dấu phẩy sang bên phải 1, 2, 3... chữ số",
                "Thêm số 0 vào bên phải",
                "Bỏ dấu phẩy"
            ], 0, "Chia cho 10, 100, 1000... là dịch dấu phẩy sang bên trái 1, 2, 3... chữ số."),
            make_mc(2, "Tính nhẩm: $45,8 : 10 = ?$", ["458", "4,58", "0,458", "45,80"], 1, "$45,8 : 10 = 4,58$."),
            make_mc(3, "Muốn chia một số thập phân cho 0,1; 0,01; 0,001... ta làm thế nào?", [
                "Chuyển dấu phẩy sang bên phải 1, 2, 3... chữ số",
                "Chuyển dấu phẩy sang bên trái 1, 2, 3... chữ số",
                "Nhân với 0,1",
                "Chia cho 10"
            ], 0, "Chia cho 0,1; 0,01... chính là nhân với 10, 100... nên chuyển dấu phẩy sang bên phải."),
            make_mc(4, "Tính nhẩm: $3,6 : 0,1 = ?$", ["0,36", "36", "360", "3,60"], 1, "$3,6 : 0,1 = 3,6 \\times 10 = 36$."),
            make_mc(5, "Số nào chia cho 100 thì được 0,025?", [
                "2,5",
                "25",
                "0,25",
                "250"
            ], 0, "$2,5 : 100 = 0,025$."),
            make_mc(6, "Một bao gạo nặng 50 kg được chia đều vào 10 túi. Mỗi túi có số ki-lô-gam gạo là:", [
                "5 kg",
                "0,5 kg",
                "500 kg",
                "50 kg"
            ], 0, "$50 : 10 = 5$ kg.")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) $34,5 : 10$\nb) $256,7 : 100$\nc) $4,8 : 0,1$\nd) $15,2 : 0,01$", "Bài giải:\na) $34,5 : 10 = 3,45$\nb) $256,7 : 100 = 2,567$\nc) $4,8 : 0,1 = 48$\nd) $15,2 : 0,01 = 1520$\nĐáp số: a) 3,45; b) 2,567; c) 48; d) 1520", "a) 3,45; b) 2,567; c) 48; d) 1520", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$24,5 : 0,25 + 24,5 : 0,5$", "Bài giải:\n$24,5 \\times 4 + 24,5 \\times 2 = 24,5 \\times (4 + 2) = 24,5 \\times 6 = 147$\nĐáp số: 147", "147", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 0,1 = 4,25 + 3,75$", "Bài giải:\n$x \\times 0,1 = 8$\n$x = 8 : 0,1 = 80$\nĐáp số: $x = 80$", "x = 80", 4, 1.0),
            make_essay(4, "Một kho gạo có 12,5 tấn gạo. Người ta xuất ra $\\frac{1}{10}$ số gạo đó cho các trường bán trú. Hỏi trong kho còn lại bao nhiêu tấn gạo?", "Bài giải:\nSố gạo đã xuất là:\n$12,5 : 10 = 1,25$ (tấn)\nSố gạo còn lại trong kho là:\n$12,5 - 1,25 = 11,25$ (tấn)\nĐáp số: 11,25 tấn gạo.", "11,25 tấn", 5, 1.5),
            make_essay(5, "Một xưởng sản xuất đóng 340 lít nước khoáng vào 100 bình loại lớn và 100 chai loại nhỏ. Biết mỗi bình loại lớn chứa 2,5 lít. Hỏi mỗi chai loại nhỏ chứa bao nhiêu lít nước khoáng?", "Bài giải:\n100 bình loại lớn chứa số lít nước khoáng là:\n$2,5 \\times 100 = 250$ (lít)\n100 chai loại nhỏ chứa số lít nước khoáng là:\n$340 - 250 = 90$ (lít)\nMỗi chai loại nhỏ chứa số lít nước khoáng là:\n$90 : 100 = 0,9$ (lít)\nĐáp số: 0,9 lít nước khoáng.", "0,9 lít", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị của biểu thức:\n$M = 4,5 : 0,1 + 4,5 \\times 90$", "Bài giải:\nTa có $4,5 : 0,1 = 4,5 \\times 10$.\nBiểu thức viết lại thành:\n$M = 4,5 \\times 10 + 4,5 \\times 90 = 4,5 \\times (10 + 90) = 4,5 \\times 100 = 450$\nĐáp số: $M = 450$", "M = 450", 4, 1.0)
        ]
    }

    exams["th5_b20_test2"] = {
        "id": "th5_b20_test2",
        "lessonId": "th5_b20",
        "lessonNum": 20,
        "testNum": 2,
        "title": "Bài 20: Chia số thập phân cho 10, 100... hoặc cho 0,1; 0,01... - Đề số 2",
        "topic": "Chia cho 10, 100... hoặc cho 0,1; 0,01...",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $750 : 100 = ?$", ["75", "7,5", "0,75", "7500"], 1, "$750 : 100 = 7,5$."),
            make_mc(2, "Tính: $0,84 : 0,01 = ?$", ["8,4", "84", "840", "0,084"], 1, "$0,84 : 0,01 = 0,84 \\times 100 = 84$."),
            make_mc(3, "Chia một số cho 0,5 tương đương với:", [
                "Nhân số đó với 2",
                "Chia số đó cho 2",
                "Nhân số đó với 5",
                "Chia số đó cho 5"
            ], 0, "Chia cho 0,5 chính là nhân với 2."),
            make_mc(4, "Một cuộn dây thép dài 45 m được cắt thành các đoạn nhỏ dài 0,1 m. Cắt được tất cả bao nhiêu đoạn dây?", [
                "4,5 đoạn",
                "45 đoạn",
                "450 đoạn",
                "4500 đoạn"
            ], 2, "$45 : 0,1 = 450$ đoạn."),
            make_mc(5, "Tìm $x$ biết $x : 0,01 = 350$. Giá trị của $x$ là:", [
                "3,5",
                "35",
                "3500",
                "0,35"
            ], 0, "$x = 350 \\times 0,01 = 3,5$."),
            make_mc(6, "Kết quả của phép tính $12,5 : 1000$ là:", [
                "0,125",
                "0,0125",
                "1,25",
                "0,00125"
            ], 1, "Dời dấu phẩy sang trái 3 chữ số: 0,0125.")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) $86,4 : 10$\nb) $315 : 100$\nc) $7,2 : 0,1$\nd) $0,45 : 0,01$", "Bài giải:\na) $86,4 : 10 = 8,64$\nb) $315 : 100 = 3,15$\nc) $7,2 : 0,1 = 72$\nd) $0,45 : 0,01 = 45$\nĐáp số: a) 8,64; b) 3,15; c) 72; d) 45", "a) 8,64; b) 3,15; c) 72; d) 45", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$36 : 0,2 + 36 : 0,5 + 36 \\times 3$", "Bài giải:\n$36 \\times 5 + 36 \\times 2 + 36 \\times 3 = 36 \\times (5 + 2 + 3) = 36 \\times 10 = 360$\nĐáp số: 360", "360", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 0,1 = 28,6 + 11,4$", "Bài giải:\n$x : 0,1 = 40$\n$x = 40 \\times 0,1 = 4$\nĐáp số: $x = 4$", "x = 4", 4, 1.0),
            make_essay(4, "Một trại chăn nuôi thu được 2450 quả trứng gà trong 100 ngày (mỗi ngày thu được số trứng như nhau). Hỏi:\na) Trung bình mỗi ngày trại thu được bao nhiêu quả trứng?\nb) Trong 10 ngày trại đó thu được bao nhiêu quả trứng?", "Bài giải:\na) Trung bình mỗi ngày trại thu được số quả trứng là:\n$2450 : 100 = 24,5$ (quả)\nb) Trong 10 ngày trại thu được số quả trứng là:\n$24,5 \\times 10 = 245$ (quả)\nĐáp số: a) 24,5 quả trứng; b) 245 quả trứng.", "a) 24,5 quả; b) 245 quả", 6, 1.5),
            make_essay(5, "Một khu vườn hình vuông có chu vi là 180 m.\na) Tính độ dài một cạnh của khu vườn đó.\nb) Tính diện tích khu vườn đó ra đơn vị héc-ta.", "Bài giải:\na) Độ dài cạnh khu vườn là:\n$180 : 4 = 45$ (m)\nb) Diện tích khu vườn là:\n$45 \\times 45 = 2025$ ($\\text{m}^2$)\nĐổi sang héc-ta: $2025 : 10 000 = 0,2025$ (ha)\nĐáp số: a) 45 m; b) 0,2025 ha.", "a) 45 m; b) 0,2025 ha", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức sau:\n$N = 8,6 : 0,1 + 86 \\times 9$", "Bài giải:\nTa có $8,6 : 0,1 = 86$.\n$N = 86 + 86 \\times 9 = 86 \\times (1 + 9) = 86 \\times 10 = 860$\nĐáp số: $N = 860$", "N = 860", 4, 1.0)
        ]
    }

    exams["th5_b20_test3"] = {
        "id": "th5_b20_test3",
        "lessonId": "th5_b20",
        "lessonNum": 20,
        "testNum": 3,
        "title": "Bài 20: Chia số thập phân cho 10, 100... hoặc cho 0,1; 0,01... - Đề số 3",
        "topic": "Chia cho 10, 100... hoặc cho 0,1; 0,01...",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $12,4 : 0,01 = ?$", ["124", "1240", "1,24", "0,124"], 1, "$12,4 : 0,01 = 12,4 \\times 100 = 1240$."),
            make_mc(2, "Kết quả của phép tính $450 : 1000$ là:", ["4,5", "0,45", "0,045", "45"], 1, "$450 : 1000 = 0,45$."),
            make_mc(3, "Chia một số cho 0,25 tương đương với:", [
                "Nhân số đó với 4",
                "Chia số đó cho 4",
                "Nhân số đó với 25",
                "Chia số đó cho 25"
            ], 0, "Chia cho 0,25 chính là nhân với 4."),
            make_mc(4, "Có 35 kg bột mì được chia đều vào 100 gói nhỏ. Mỗi gói nhỏ chứa số gam bột mì là:", [
                "350 g",
                "35 g",
                "3,5 g",
                "3500 g"
            ], 0, "Mỗi gói chứa $35 : 100 = 0,35$ kg = 350 g."),
            make_mc(5, "Tìm $x$ biết $x \\times 0,01 = 0,05$. Giá trị của $x$ là:", [
                "5",
                "0,5",
                "50",
                "0,005"
            ], 0, "$x = 0,05 : 0,01 = 5$."),
            make_mc(6, "Biểu thức $18 : 0,5 + 18 : 0,5$ có giá trị bằng:", [
                "72",
                "36",
                "18",
                "9"
            ], 0, "$18 \\times 2 + 18 \\times 2 = 36 + 36 = 72$.")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) $94,8 : 10$\nb) $62,5 : 100$\nc) $1,8 : 0,1$\nd) $3,45 : 0,01$", "Bài giải:\na) $94,8 : 10 = 9,48$\nb) $62,5 : 100 = 0,625$\nc) $1,8 : 0,1 = 18$\nd) $3,45 : 0,01 = 345$\nĐáp số: a) 9,48; b) 0,625; c) 18; d) 345", "a) 9,48; b) 0,625; c) 18; d) 345", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$4,8 : 0,2 + 4,8 \\times 5$", "Bài giải:\n$4,8 \\times 5 + 4,8 \\times 5 = 4,8 \\times (5 + 5) = 4,8 \\times 10 = 48$\nĐáp số: 48", "48", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 0,01 = 450 + 250$", "Bài giải:\n$x : 0,01 = 700$\n$x = 700 \\times 0,01 = 7$\nĐáp số: $x = 7$", "x = 7", 4, 1.0),
            make_essay(4, "Một cửa hàng nhập về 100 thùng sữa chua, mỗi thùng có 48 hộp. Cửa hàng đã bán được $\\frac{3}{10}$ tổng số hộp sữa chua đó. Hỏi cửa hàng đã bán được bao nhiêu hộp sữa chua?", "Bài giải:\nTổng số hộp sữa chua cửa hàng đã nhập là:\n$48 \\times 100 = 4800$ (hộp)\nSố hộp sữa chua cửa hàng đã bán là:\n$4800 \\times \\frac{3}{10} = 1440$ (hộp)\nĐáp số: 1440 hộp sữa chua.", "1440 hộp", 6, 1.5),
            make_essay(5, "Đoạn đường từ thị trấn về làng dài 15 km. Người ta trồng cây ở cả hai bên đường, cứ cách 10 m trồng một cây (ở cả hai đầu đường đều có cây). Hỏi người ta đã trồng tất cả bao nhiêu cây trên đoạn đường đó?", "Bài giải:\nĐổi: $15\\text{ km} = 15 000\\text{ m}$.\nSố khoảng cách 10 m ở một bên đường là:\n$15 000 : 10 = 1500$ (khoảng cách)\nSố cây trồng ở một bên đường là:\n$1500 + 1 = 1501$ (cây)\nSố cây trồng ở cả hai bên đường là:\n$1501 \\times 2 = 3002$ (cây)\nĐáp số: 3002 cây.", "3002 cây", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức sau:\n$P = 15 : 0,25 + 15 : 0,5 + 15 : 0,25$", "Bài giải:\n$P = 15 \\times 4 + 15 \\times 2 + 15 \\times 4 = 15 \\times (4 + 2 + 4) = 15 \\times 10 = 150$\nĐáp số: $P = 150$", "P = 150", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 21: LUYỆN TẬP CHUNG CHỦ ĐỀ 3
    # =========================================================================
    exams["th5_b21_test1"] = {
        "id": "th5_b21_test1",
        "lessonId": "th5_b21",
        "lessonNum": 21,
        "testNum": 1,
        "title": "Bài 21: Luyện tập chung Chủ đề 3 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 3",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của biểu thức $15,6 + 4,4 \\times 2$ là:", ["40", "24,4", "24", "44"], 1, "$4,4 \\times 2 = 8,8$, $15,6 + 8,8 = 24,4$."),
            make_mc(2, "Kết quả của phép tính $(25,5 - 5,5) : 4$ là:", ["5", "4", "6", "5,5"], 0, "$20 : 4 = 5$."),
            make_mc(3, "Một mảnh đất hình chữ nhật có chiều dài 15,5 m, chiều rộng 8 m. Chu vi mảnh đất là:", [
                "47 m",
                "23,5 m",
                "124 m",
                "46 m"
            ], 0, "$(15,5 + 8) \\times 2 = 23,5 \\times 2 = 47$ m."),
            make_mc(4, "Biểu thức $3,2 \\times 10 - 4,5 : 0,1$ có giá trị là:", [
                "-13",
                "13",
                "32 - 45",
                "-13"
            ], 1, "Sửa biểu thức cho số tự nhiên dương: $4,5 : 0,1 - 3,2 \\times 10 = 45 - 32 = 13$."),
            make_mc(5, "Tìm $x$ biết $x + 2,5 \\times 4 = 15$. Giá trị của $x$ là:", [
                "5",
                "6",
                "7",
                "4"
            ], 0, "$2,5 \\times 4 = 10 \\Rightarrow x = 15 - 10 = 5$."),
            make_mc(6, "Một người mua 2,5 kg đường với giá 24 000 đồng/kg. Người đó trả bằng tờ 100 000 đồng thì được trả lại số tiền là:", [
                "40 000 đồng",
                "50 000 đồng",
                "60 000 đồng",
                "30 000 đồng"
            ], 0, "Tiền đường: $2,5 \\times 24 000 = 60 000$ đ. Tiền thừa: $100 000 - 60 000 = 40 000$ đ.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\na) $45,8 + 12,4 \\times 3$\nb) $(85,6 - 25,6) : 5$", "Bài giải:\na) $45,8 + 37,2 = 83$\nb) $60 : 5 = 12$\nĐáp số: a) 83; b) 12", "a) 83; b) 12", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$4,75 \\times 6,8 + 4,75 \\times 3,2$", "Bài giải:\n$4,75 \\times (6,8 + 3,2) = 4,75 \\times 10 = 47,5$\nĐáp số: 47,5", "47,5", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 2,5 + 3,8 = 10,2$", "Bài giải:\n$x : 2,5 = 10,2 - 3,8 = 6,4$\n$x = 6,4 \\times 2,5 = 16$\nĐáp số: $x = 16$", "x = 16", 4, 1.0),
            make_essay(4, "Một cửa hàng nhập về 3 bao gạo tẻ, mỗi bao nặng 50,5 kg và 4 bao gạo nếp, mỗi bao nặng 25,5 kg.\na) Tính tổng số ki-lô-gam gạo cửa hàng đã nhập về.\nb) Cửa hàng đã bán hết toàn bộ số gạo đó trong 3 ngày. Hỏi trung bình mỗi ngày cửa hàng bán được bao nhiêu ki-lô-gam gạo?", "Bài giải:\na) Khối lượng gạo tẻ là:\n$50,5 \\times 3 = 151,5$ (kg)\nKhối lượng gạo nếp là:\n$25,5 \\times 4 = 102$ (kg)\nTổng số gạo nhập về là:\n$151,5 + 102 = 253,5$ (kg)\nb) Trung bình mỗi ngày bán được:\n$253,5 : 3 = 84,5$ (kg)\nĐáp số: a) 253,5 kg; b) 84,5 kg.", "a) 253,5 kg; b) 84,5 kg", 6, 1.5),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chiều dài 28,5 m, chiều rộng bằng $\\frac{2}{3}$ chiều dài.\na) Tính diện tích mảnh vườn đó.\nb) Người ta dùng 60% diện tích vườn để trồng cây ăn quả, phần còn lại trồng rau. Tính diện tích phần đất trồng rau.", "Bài giải:\na) Chiều rộng mảnh vườn là:\n$28,5 \\times \\frac{2}{3} = 19$ (m)\nDiện tích mảnh vườn là:\n$28,5 \\times 19 = 541,5$ ($\\text{m}^2$)\nb) Diện tích trồng rau chiếm số phần trăm là:\n$100\\% - 60\\% = 40\\%$\nDiện tích trồng rau là:\n$541,5 \\times 40 : 100 = 216,6$ ($\\text{m}^2$)\nĐáp số: a) 541,5 $\\text{m}^2$; b) 216,6 $\\text{m}^2$.", "a) 541,5 m²; b) 216,6 m²", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức sau:\n$Q = 0,2 \\times 17,5 \\times 5 + 0,25 \\times 82,5 \\times 4$", "Bài giải:\n$Q = (0,2 \\times 5) \\times 17,5 + (0,25 \\times 4) \\times 82,5$\n$Q = 1 \\times 17,5 + 1 \\times 82,5 = 17,5 + 82,5 = 100$\nĐáp số: $Q = 100$", "Q = 100", 4, 1.0)
        ]
    }

    exams["th5_b21_test2"] = {
        "id": "th5_b21_test2",
        "lessonId": "th5_b21",
        "lessonNum": 21,
        "testNum": 2,
        "title": "Bài 21: Luyện tập chung Chủ đề 3 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 3",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $36 : 0,4 + 10 = ?$", ["100", "90", "19", "25"], 0, "$36 : 0,4 = 90$, $90 + 10 = 100$."),
            make_mc(2, "Giá trị của biểu thức $5,8 \\times 2 + 3,4$ là:", ["15", "14,8", "15,2", "14,4"], 0, "$11,6 + 3,4 = 15$."),
            make_mc(3, "Một ô tô chạy trong 2,5 giờ được 112,5 km. Vận tốc của ô tô là:", [
                "45 km/h",
                "48 km/h",
                "42 km/h",
                "50 km/h"
            ], 0, "$112,5 : 2,5 = 45$ km/h."),
            make_mc(4, "Biểu thức $8,5 \\times 9,9 + 8,5 \\times 0,1$ có giá trị bằng:", [
                "85",
                "8,5",
                "850",
                "0,85"
            ], 0, "$8,5 \\times (9,9 + 0,1) = 8,5 \\times 10 = 85$."),
            make_mc(5, "Tìm $x$ biết $x - 4,8 : 2 = 10$. Giá trị của $x$ là:", [
                "12,4",
                "7,6",
                "14,8",
                "12,8"
            ], 0, "$x - 2,4 = 10 \\Rightarrow x = 12,4$."),
            make_mc(6, "Diện tích một hình tam giác có đáy 12 cm và chiều cao 6,5 cm là:", [
                "39 $\\text{cm}^2$",
                "78 $\\text{cm}^2$",
                "36 $\\text{cm}^2$",
                "42 $\\text{cm}^2$"
            ], 0, "$(12 \\times 6,5) : 2 = 39$ $\\text{cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $64,8 \\times 2,5$\nb) $102,6 : 4,5$", "Bài giải:\na) $64,8 \\times 2,5 = 162$\nb) $102,6 : 4,5 = 22,8$\nĐáp số: a) 162; b) 22,8", "a) 162; b) 22,8", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$15,6 \\times 8,4 + 15,6 \\times 2,6 - 15,6$", "Bài giải:\n$15,6 \\times (8,4 + 2,6 - 1) = 15,6 \\times (11 - 1) = 15,6 \\times 10 = 156$\nĐáp số: 156", "156", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 4,5 = 65,7 - 25,2$", "Bài giải:\n$x \\times 4,5 = 40,5$\n$x = 40,5 : 4,5 = 9$\nĐáp số: $x = 9$", "x = 9", 4, 1.0),
            make_essay(4, "Hai đội công nhân cùng sửa một đoạn đường. Đội thứ nhất sửa được 145,5 m đường. Đội thứ hai sửa được số mét đường gấp 1,4 lần đội thứ nhất. Hỏi cả hai đội sửa được tất cả bao nhiêu mét đường?", "Bài giải:\nĐội thứ hai sửa được số mét đường là:\n$145,5 \\times 1,4 = 203,7$ (m)\nCả hai đội sửa được tất cả số mét đường là:\n$145,5 + 203,7 = 349,2$ (m)\nĐáp số: 349,2 m đường.", "349,2 m", 6, 1.5),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chu vi là 140 m, chiều rộng bằng $\\frac{2}{3}$ chiều dài.\na) Tính diện tích thửa ruộng đó.\nb) Cứ $100\\text{ m}^2$ thu hoạch được 65 kg thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Bài giải:\na) Nửa chu vi là: $140 : 2 = 70$ (m).\nTổng số phần bằng nhau: $2 + 3 = 5$ (phần).\nChiều rộng: $70 : 5 \\times 2 = 28$ (m).\nChiều dài: $70 - 28 = 42$ (m).\nDiện tích thửa ruộng: $42 \\times 28 = 1176$ ($\\text{m}^2$).\nb) Số thóc thu hoạch được:\n$1176 : 100 \\times 65 = 764,4$ (kg) = 7,644 tạ.\nĐáp số: a) 1176 $\\text{m}^2$; b) 7,644 tạ thóc.", "a) 1176 m²; b) 7,644 tạ", 6, 1.5),
            make_essay(6, "Tính giá trị biểu thức sau một cách hợp lý:\n$S = \\frac{2,4 \\times 15 + 4,8 \\times 2,5}{0,8 \\times 12}$", "Bài giải:\nTử số: $2,4 \\times 15 + 2,4 \\times 2 \\times 2,5 = 2,4 \\times 15 + 2,4 \\times 5 = 2,4 \\times 20 = 48$.\nMẫu số: $0,8 \\times 12 = 9,6$.\nGiá trị biểu thức: $48 : 9,6 = 5$.\nĐáp số: $S = 5$", "S = 5", 5, 1.0)
        ]
    }

    exams["th5_b21_test3"] = {
        "id": "th5_b21_test3",
        "lessonId": "th5_b21",
        "lessonNum": 21,
        "testNum": 3,
        "title": "Bài 21: Luyện tập chung Chủ đề 3 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 3",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $(15,4 + 4,6) : 2 = ?$", ["10", "20", "5", "8"], 0, "$20 : 2 = 10$."),
            make_mc(2, "Kết quả của $45 : 0,5 - 30$ là:", ["60", "90", "15", "50"], 0, "$45 \\times 2 - 30 = 90 - 30 = 60$."),
            make_mc(3, "Một ô tô tiêu thụ 12,5 lít xăng để đi 100 km. Để đi 240 km ô tô đó cần bao nhiêu lít xăng?", [
                "30 lít",
                "25 lít",
                "35 lít",
                "28 lít"
            ], 0, "Đi 1 km cần $12,5 : 100 = 0,125$ lít. Đi 240 km cần $0,125 \\times 240 = 30$ lít."),
            make_mc(4, "Biểu thức $2,5 \\times 7,8 \\times 4$ có kết quả là:", [
                "78",
                "7,8",
                "780",
                "39"
            ], 0, "$(2,5 \\times 4) \\times 7,8 = 10 \\times 7,8 = 78$."),
            make_mc(5, "Tìm $x$ biết $x : 3,5 = 2,4$. Giá trị của $x$ là:", [
                "8,4",
                "8,2",
                "7,4",
                "6,8"
            ], 0, "$x = 2,4 \\times 3,5 = 8,4$."),
            make_mc(6, "Trung bình cộng của ba số 14,5; 18,2 và 21,3 là:", [
                "18",
                "17",
                "19",
                "18,5"
            ], 0, "$(14,5 + 18,2 + 21,3) : 3 = 54 : 3 = 18$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị các biểu thức sau:\na) $72,5 - 18,4 \\times 2,5$\nb) $(48,6 + 23,4) : 1,8$", "Bài giải:\na) $72,5 - 46 = 26,5$\nb) $72 : 1,8 = 40$\nĐáp số: a) 26,5; b) 40", "a) 26,5; b) 40", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$3,48 \\times 145 - 3,48 \\times 45$", "Bài giải:\n$3,48 \\times (145 - 45) = 3,48 \\times 100 = 348$\nĐáp số: 348", "348", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 1,5 + 14,8 = 25,6$", "Bài giải:\n$x : 1,5 = 25,6 - 14,8 = 10,8$\n$x = 10,8 \\times 1,5 = 16,2$\nĐáp số: $x = 16,2$", "x = 16,2", 4, 1.0),
            make_essay(4, "Một người thợ may dùng 45,5 m vải để may 14 bộ quần áo như nhau. Sau đó người thợ may tiếp 20 bộ quần áo cùng loại. Hỏi người đó cần dùng thêm bao nhiêu mét vải nữa?", "Bài giải:\nMay mỗi bộ quần áo hết số mét vải là:\n$45,5 : 14 = 3,25$ (m)\nĐể may thêm 20 bộ quần áo nữa cần số mét vải là:\n$3,25 \\times 20 = 65$ (m)\nĐáp số: 65 m vải.", "65 m", 6, 1.5),
            make_essay(5, "Một khu đất hình chữ nhật có chu vi là 250 m, chiều rộng bằng $\\frac{2}{3}$ chiều dài.\na) Tính diện tích khu đất đó ra mét vuông.\nb) Người ta dành $\\frac{1}{5}$ diện tích để làm nhà, phần đất còn lại làm sân bóng đá mini. Tính diện tích sân bóng đá mini.", "Bài giải:\na) Nửa chu vi khu đất là: $250 : 2 = 125$ (m).\nTổng số phần bằng nhau: $2 + 3 = 5$ (phần).\nChiều rộng khu đất: $125 : 5 \\times 2 = 50$ (m).\nChiều dài khu đất: $125 - 50 = 75$ (m).\nDiện tích khu đất: $75 \\times 50 = 3750$ ($\\text{m}^2$).\nb) Diện tích làm nhà là: $3750 : 5 = 750$ ($\\text{m}^2$).\nDiện tích làm sân bóng đá là:\n$3750 - 750 = 3000$ ($\\text{m}^2$).\nĐáp số: a) 3750 $\\text{m}^2$; b) 3000 $\\text{m}^2$.", "a) 3750 m²; b) 3000 m²", 6, 1.5),
            make_essay(6, "Tính nhanh tổng dãy số sau:\n$K = 1,2 + 2,3 + 3,4 + 4,5 + 5,6 + 6,7 + 7,8 + 8,9$", "Bài giải:\nNhóm các cặp số có tổng bằng nhau:\n$K = (1,2 + 8,9) + (2,3 + 7,8) + (3,4 + 6,7) + (4,5 + 5,6)$\n$K = 10,1 + 10,1 + 10,1 + 10,1$\n$K = 10,1 \\times 4 = 40,4$\nĐáp số: $K = 40,4$", "K = 40,4", 5, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_ch3_part2_exams()
    print(f"Chủ đề 3 Phần 2: {len(ex)} đề (Kỳ vọng: 9 đề)")
