# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 3: CÁC PHÉP TÍNH VỚI SỐ THẬP PHÂN (PHẦN 1: BÀI 15 ĐẾN BÀI 18) - TOÁN 5 KNTT
Gồm 12 đề kiểm tra (mỗi bài 3 đề):
- Bài 15: Phép cộng số thập phân (th5_b15_test1, th5_b15_test2, th5_b15_test3)
- Bài 16: Phép trừ số thập phân (th5_b16_test1, th5_b16_test2, th5_b16_test3)
- Bài 17: Phép nhân số thập phân (th5_b17_test1, th5_b17_test2, th5_b17_test3)
- Bài 18: Nhân số thập phân với 10, 100, 1000... hoặc với 0,1; 0,01; 0,001... (th5_b18_test1, th5_b18_test2, th5_b18_test3)
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

def get_ch3_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 15: PHÉP CỘNG SỐ THẬP PHÂN
    # =========================================================================
    exams["th5_b15_test1"] = {
        "id": "th5_b15_test1",
        "lessonId": "th5_b15",
        "lessonNum": 15,
        "testNum": 1,
        "title": "Bài 15: Phép cộng số thập phân - Đề số 1",
        "topic": "Phép cộng số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khi đặt tính cộng hai số thập phân, ta cần viết các chữ số ở cùng một hàng như thế nào?", [
                "Lệch nhau sang bên phải",
                "Thẳng cột với nhau và dấu phẩy thẳng cột",
                "Lệch nhau sang bên trái",
                "Tùy ý không cần thẳng cột"
            ], 1, "Khi đặt tính cộng các số thập phân, các chữ số ở cùng một hàng phải đặt thẳng cột với nhau và dấu phẩy thẳng cột."),
            make_mc(2, "Tính nhẩm: $12,5 + 7,5 = ?$", ["19,0", "20", "20,5", "19,5"], 1, "$12,5 + 7,5 = 20,0 = 20$."),
            make_mc(3, "Kết quả của phép tính $34,85 + 16,15$ là:", ["50", "51", "51,1", "50,9"], 1, "$34,85 + 16,15 = 51,00 = 51$."),
            make_mc(4, "Biểu thức $a + b = b + a$ thể hiện tính chất nào của phép cộng?", [
                "Tính chất kết hợp",
                "Tính chất giao hoán",
                "Tính chất phân phối",
                "Cộng với số 0"
            ], 1, "Đổi chỗ các số hạng mà tổng không đổi là tính chất giao hoán."),
            make_mc(5, "Một bao gạo nặng 25,5 kg, bao thứ hai nặng hơn bao thứ nhất 3,8 kg. Cả hai bao gạo nặng bao nhiêu ki-lô-gam?", [
                "29,3 kg",
                "54,8 kg",
                "51 kg",
                "53,8 kg"
            ], 1, "Bao thứ hai: $25,5 + 3,8 = 29,3$ kg. Cả hai bao: $25,5 + 29,3 = 54,8$ kg."),
            make_mc(6, "Tìm số thích hợp điền vào chỗ chấm: $4,6 + .......... = 10$", [
                "5,4",
                "6,4",
                "5,6",
                "6,6"
            ], 0, "Số cần tìm là $10 - 4,6 = 5,4$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $38,45 + 26,78$\nb) $125,6 + 48,95$", "Bài giải:\na) $38,45 + 26,78 = 65,23$\nb) $125,60 + 48,95 = 174,55$\nĐáp số: a) 65,23; b) 174,55", "a) 65,23; b) 174,55", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$12,7 + 5,89 + 7,3$", "Bài giải:\n$12,7 + 5,89 + 7,3 = (12,7 + 7,3) + 5,89$\n$= 20 + 5,89$\n$= 25,89$\nĐáp số: 25,89", "25,89", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 14,8 = 25,6 + 9,4$", "Bài giải:\n$x - 14,8 = 35$\n$x = 35 + 14,8$\n$x = 49,8$\nĐáp số: $x = 49,8$", "x = 49,8", 4, 1.0),
            make_essay(4, "Một người đi xe đạp: giờ thứ nhất đi được 12,5 km; giờ thứ hai đi được 13,8 km; giờ thứ ba đi được nhiều hơn giờ thứ hai 1,7 km. Hỏi trong cả ba giờ, người đó đi được bao nhiêu ki-lô-mét?", "Bài giải:\nQuãng đường người đó đi trong giờ thứ ba là:\n$13,8 + 1,7 = 15,5$ (km)\nCả ba giờ người đó đi được là:\n$12,5 + 13,8 + 15,5 = 41,8$ (km)\nĐáp số: 41,8 km.", "41,8 km", 6, 1.5),
            make_essay(5, "Một mảnh vườn hình tam giác có độ dài ba cạnh lần lượt là 15,6 m; 18,4 m và 21,5 m.\na) Tính chu vi mảnh vườn đó.\nb) Người ta rào lưới xung quanh vườn, có để cổng ra vào rộng 2,5 m. Hỏi chiều dài lưới thép cần dùng là bao nhiêu mét?", "Bài giải:\na) Chu vi mảnh vườn hình tam giác là:\n$15,6 + 18,4 + 21,5 = 55,5$ (m)\nb) Chiều dài lưới thép cần dùng là:\n$55,5 - 2,5 = 53$ (m)\nĐáp số: a) 55,5 m; b) 53 m.", "a) 55,5 m; b) 53 m", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$S = 1,1 + 2,2 + 3,3 + 4,4 + 5,5 + 6,6 + 7,7 + 8,8 + 9,9$", "Bài giải:\n$S = (1,1 + 9,9) + (2,2 + 8,8) + (3,3 + 7,7) + (4,4 + 6,6) + 5,5$\n$S = 11 + 11 + 11 + 11 + 5,5$\n$S = 44 + 5,5 = 49,5$\nĐáp số: $S = 49,5$", "S = 49,5", 4, 1.0)
        ]
    }

    exams["th5_b15_test2"] = {
        "id": "th5_b15_test2",
        "lessonId": "th5_b15",
        "lessonNum": 15,
        "testNum": 2,
        "title": "Bài 15: Phép cộng số thập phân - Đề số 2",
        "topic": "Phép cộng số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $0,75 + 0,25 = ?$", ["0,100", "1,0", "0,9", "1,5"], 1, "$0,75 + 0,25 = 1,0 = 1$."),
            make_mc(2, "Kết quả của phép tính $28,4 + 11,6$ là:", ["39", "40", "41", "40,1"], 1, "$28,4 + 11,6 = 40$."),
            make_mc(3, "Phép tính $(a + b) + c = a + (b + c)$ là tính chất gì của phép cộng?", [
                "Giao hoán",
                "Kết hợp",
                "Phân phối",
                "Cộng với 0"
            ], 1, "Đây là tính chất kết hợp của phép cộng."),
            make_mc(4, "Đoạn thẳng $AB$ dài 4,5 cm, đoạn thẳng $BC$ dài 6,8 cm. Độ dài đoạn thẳng $AC$ khi $B$ nằm giữa $A$ và $C$ là:", [
                "10,3 cm",
                "11,3 cm",
                "11,5 cm",
                "12,3 cm"
            ], 1, "$AC = 4,5 + 6,8 = 11,3$ cm."),
            make_mc(5, "Tìm $x$ biết $x - 6,5 = 14,5$. Giá trị của $x$ là:", [
                "20",
                "21",
                "8",
                "21,5"
            ], 1, "$x = 14,5 + 6,5 = 21$."),
            make_mc(6, "Số thập phân nào cộng với 3,75 để được kết quả bằng 10?", [
                "6,25",
                "7,25",
                "6,35",
                "7,35"
            ], 0, "$10 - 3,75 = 6,25$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $54,67 + 38,59$\nb) $216,4 + 85,73$", "Bài giải:\na) $54,67 + 38,59 = 93,26$\nb) $216,40 + 85,73 = 302,13$\nĐáp số: a) 93,26; b) 302,13", "a) 93,26; b) 302,13", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$(14,25 + 5,75) + (8,36 + 1,64)$", "Bài giải:\n$(14,25 + 5,75) + (8,36 + 1,64) = 20 + 10 = 30$\nĐáp số: 30", "30", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 17,65 = 32,35 + 10$", "Bài giải:\n$x - 17,65 = 42,35$\n$x = 42,35 + 17,65$\n$x = 60$\nĐáp số: $x = 60$", "x = 60", 4, 1.0),
            make_essay(4, "Có ba bao đường. Bao thứ nhất nặng 35,5 kg. Bao thứ hai nặng hơn bao thứ nhất 4,8 kg. Bao thứ ba nặng bằng tổng khối lượng của hai bao đầu. Hỏi cả ba bao nặng bao nhiêu ki-lô-gam đường?", "Bài giải:\nBao thứ hai nặng số ki-lô-gam là:\n$35,5 + 4,8 = 40,3$ (kg)\nBao thứ ba nặng số ki-lô-gam là:\n$35,5 + 40,3 = 75,8$ (kg)\nCả ba bao đường nặng số ki-lô-gam là:\n$35,5 + 40,3 + 75,8 = 151,6$ (kg)\nĐáp số: 151,6 kg đường.", "151,6 kg", 6, 1.5),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chiều rộng là 15,8 m, chiều dài hơn chiều rộng 8,7 m.\na) Tính chiều dài mảnh vườn đó.\nb) Tính chu vi mảnh vườn đó.", "Bài giải:\na) Chiều dài mảnh vườn là:\n$15,8 + 8,7 = 24,5$ (m)\nb) Chu vi mảnh vườn là:\n$(24,5 + 15,8) \\times 2 = 40,3 \\times 2 = 80,6$ (m)\nĐáp số: a) 24,5 m; b) 80,6 m.", "a) 24,5 m; b) 80,6 m", 6, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$A = 0,1 + 0,3 + 0,5 + 0,7 + 0,9 + 1,1 + 1,3 + 1,5 + 1,7 + 1,9$", "Bài giải:\n$A = (0,1 + 1,9) + (0,3 + 1,7) + (0,5 + 1,5) + (0,7 + 1,3) + (0,9 + 1,1)$\n$A = 2 + 2 + 2 + 2 + 2 = 10$\nĐáp số: $A = 10$", "A = 10", 4, 1.0)
        ]
    }

    exams["th5_b15_test3"] = {
        "id": "th5_b15_test3",
        "lessonId": "th5_b15",
        "lessonNum": 15,
        "testNum": 3,
        "title": "Bài 15: Phép cộng số thập phân - Đề số 3",
        "topic": "Phép cộng số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính nhanh: $45,8 + 34,2 = ?$", ["79", "80", "80,5", "81"], 1, "$45,8 + 34,2 = 80$."),
            make_mc(2, "Số thập phân nào sau đây khi cộng với 12,34 thì được 20?", [
                "7,66",
                "8,66",
                "7,76",
                "8,76"
            ], 0, "$20 - 12,34 = 7,66$."),
            make_mc(3, "Tổng của ba số $3,5 + 4,2 + 6,5$ là:", [
                "13,2",
                "14,2",
                "14",
                "15,2"
            ], 1, "$(3,5 + 6,5) + 4,2 = 10 + 4,2 = 14,2$."),
            make_mc(4, "Một ô tô chạy giờ đầu được 42,5 km, giờ sau chạy được 48,7 km. Cả hai giờ ô tô chạy được:", [
                "90,2 km",
                "91,2 km",
                "89,2 km",
                "91 km"
            ], 1, "$42,5 + 48,7 = 91,2$ km."),
            make_mc(5, "Biểu thức $15,6 + x = 20,4$. Giá trị của $x$ là:", [
                "4,8",
                "5,8",
                "4,2",
                "36"
            ], 0, "$x = 20,4 - 15,6 = 4,8$."),
            make_mc(6, "Giá trị của biểu thức $0,6 + 0,06 + 0,006$ là:", [
                "0,66",
                "0,666",
                "0,606",
                "6,66"
            ], 1, "$0,600 + 0,060 + 0,006 = 0,666$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $67,82 + 45,69$\nb) $158,35 + 94,8$", "Bài giải:\na) $67,82 + 45,69 = 113,51$\nb) $158,35 + 94,80 = 253,15$\nĐáp số: a) 113,51; b) 253,15", "a) 113,51; b) 253,15", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$26,45 + 18,72 + 13,55 + 11,28$", "Bài giải:\n$= (26,45 + 13,55) + (18,72 + 11,28)$\n$= 40 + 30 = 70$\nĐáp số: 70", "70", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 28,4 = 15,6 + 34,4$", "Bài giải:\n$x - 28,4 = 50$\n$x = 50 + 28,4$\n$x = 78,4$\nĐáp số: $x = 78,4$", "x = 78,4", 4, 1.0),
            make_essay(4, "Một cửa hàng buổi sáng bán được 145,5 kg gạo, buổi chiều bán được nhiều hơn buổi sáng 28,5 kg gạo. Buổi tối bán được số gạo bằng một nửa tổng số gạo bán được của cả sáng và chiều. Hỏi cả ngày cửa hàng đó bán được bao nhiêu ki-lô-gam gạo?", "Bài giải:\nBuổi chiều cửa hàng bán được số gạo là:\n$145,5 + 28,5 = 174$ (kg)\nTổng số gạo bán trong buổi sáng và chiều là:\n$145,5 + 174 = 319,5$ (kg)\nBuổi tối cửa hàng bán được số gạo là:\n$319,5 : 2 = 159,75$ (kg)\nCả ngày cửa hàng bán được số gạo là:\n$319,5 + 159,75 = 479,25$ (kg)\nĐáp số: 479,25 kg gạo.", "479,25 kg", 6, 1.5),
            make_essay(5, "Một tam giác có độ dài đáy là 24,6 cm, chiều cao tương ứng là 15,4 cm. Tính tổng độ dài của đáy và chiều cao của tam giác đó.", "Bài giải:\nTổng độ dài của đáy và chiều cao là:\n$24,6 + 15,4 = 40$ (cm)\nĐáp số: 40 cm.", "40 cm", 4, 1.5),
            make_essay(6, "Tính nhanh tổng dãy số sau:\n$B = 2,4 + 3,5 + 4,6 + 5,7 + 6,8 + 7,9 + 9,0 + 10,1$", "Bài giải:\nNhóm các cặp số có tổng bằng nhau:\n$B = (2,4 + 10,1) + (3,5 + 9,0) + (4,6 + 7,9) + (5,7 + 6,8)$\n$B = 12,5 + 12,5 + 12,5 + 12,5$\n$B = 12,5 \\times 4 = 50$\nĐáp số: $B = 50$", "B = 50", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 16: PHÉP TRỪ SỐ THẬP PHÂN
    # =========================================================================
    exams["th5_b16_test1"] = {
        "id": "th5_b16_test1",
        "lessonId": "th5_b16",
        "lessonNum": 16,
        "testNum": 1,
        "title": "Bài 16: Phép trừ số thập phân - Đề số 1",
        "topic": "Phép trừ số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép trừ $15,8 - 7,3$ là:", ["8,5", "7,5", "8,2", "7,8"], 0, "$15,8 - 7,3 = 8,5$."),
            make_mc(2, "Tính: $45 - 12,6 = ?$", ["33,4", "32,4", "33,6", "32,6"], 1, "$45,0 - 12,6 = 32,4$."),
            make_mc(3, "Muốn trừ một số cho một tổng, ta có thể làm thế nào?", [
                "Lấy số đó trừ đi số hạng thứ nhất rồi cộng số hạng thứ hai",
                "Lấy số đó trừ đi từng số hạng của tổng",
                "Lấy số đó cộng từng số hạng",
                "Không thực hiện được"
            ], 1, "Quy tắc: $a - (b + c) = a - b - c$."),
            make_mc(4, "Một cuộn dây dài 20 m, người ta cắt đi 6,75 m. Cuộn dây còn lại dài bao nhiêu mét?", [
                "13,75 m",
                "14,25 m",
                "13,25 m",
                "14,75 m"
            ], 2, "$20,00 - 6,75 = 13,25$ m."),
            make_mc(5, "Tìm $x$ biết $28,5 - x = 12,3$. Giá trị của $x$ là:", [
                "16,2",
                "40,8",
                "15,2",
                "16,8"
            ], 0, "$x = 28,5 - 12,3 = 16,2$."),
            make_mc(6, "Hiệu của số lớn nhất có một chữ số và 4,85 là:", [
                "5,15",
                "4,15",
                "4,25",
                "5,25"
            ], 1, "Số lớn nhất có 1 chữ số là 9. $9 - 4,85 = 4,15$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $84,5 - 37,28$\nb) $120 - 45,67$", "Bài giải:\na) $84,50 - 37,28 = 47,22$\nb) $120,00 - 45,67 = 74,33$\nĐáp số: a) 47,22; b) 74,33", "a) 47,22; b) 74,33", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$46,85 - 18,3 - 11,7$", "Bài giải:\n$46,85 - (18,3 + 11,7) = 46,85 - 30 = 16,85$\nĐáp số: 16,85", "16,85", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x + 14,8 = 45,2 - 8,4$", "Bài giải:\n$x + 14,8 = 36,8$\n$x = 36,8 - 14,8 = 22$\nĐáp số: $x = 22$", "x = 22", 4, 1.0),
            make_essay(4, "Một thùng đựng 45,5 lít dầu. Lần thứ nhất người ta lấy ra 14,8 lít dầu. Lần thứ hai lấy ra nhiều hơn lần thứ nhất 2,4 lít dầu. Hỏi trong thùng còn lại bao nhiêu lít dầu?", "Bài giải:\nLần thứ hai lấy ra số lít dầu là:\n$14,8 + 2,4 = 17,2$ (lít)\nCả hai lần lấy ra số lít dầu là:\n$14,8 + 17,2 = 32$ (lít)\nTrong thùng còn lại số lít dầu là:\n$45,5 - 32 = 13,5$ (lít)\nĐáp số: 13,5 lít dầu.", "13,5 lít", 6, 1.5),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chu vi là 96,4 m. Biết chiều rộng là 18,2 m. Tính chiều dài của thửa ruộng đó.", "Bài giải:\nNửa chu vi thửa ruộng là:\n$96,4 : 2 = 48,2$ (m)\nChiều dài của thửa ruộng là:\n$48,2 - 18,2 = 30$ (m)\nĐáp số: 30 m.", "30 m", 5, 1.5),
            make_essay(6, "Tìm một số biết rằng lấy số đó trừ đi 15,4 rồi cộng với 8,6 thì được kết quả là 24,5.", "Bài giải:\nGọi số cần tìm là $x$.\nTheo đề bài ta có:\n$x - 15,4 + 8,6 = 24,5$\n$x - 15,4 = 24,5 - 8,6 = 15,9$\n$x = 15,9 + 15,4 = 31,3$\nĐáp số: 31,3", "31,3", 5, 1.0)
        ]
    }

    exams["th5_b16_test2"] = {
        "id": "th5_b16_test2",
        "lessonId": "th5_b16",
        "lessonNum": 16,
        "testNum": 2,
        "title": "Bài 16: Phép trừ số thập phân - Đề số 2",
        "topic": "Phép trừ số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $78,6 - 29,4 = ?$", ["49,2", "48,2", "50,2", "49,4"], 0, "$78,6 - 29,4 = 49,2$."),
            make_mc(2, "Kết quả của phép trừ $100 - 34,75$ là:", ["66,25", "65,25", "65,35", "75,25"], 1, "$100,00 - 34,75 = 65,25$."),
            make_mc(3, "Một sợi dây dài 15,4 m, người ta cắt lấy 8,6 m. Đoạn dây còn lại dài là:", [
                "7,8 m",
                "6,8 m",
                "6,2 m",
                "7,2 m"
            ], 1, "$15,4 - 8,6 = 6,8$ m."),
            make_mc(4, "Biểu thức $a - b - c$ bằng biểu thức nào dưới đây?", [
                "$a - (b - c)$",
                "$a - (b + c)$",
                "$(a - b) + c$",
                "$a + (b - c)$"
            ], 1, "$a - b - c = a - (b + c)$."),
            make_mc(5, "Tìm $y$ biết $y - 32,8 = 18,2$. Giá trị của $y$ là:", [
                "50",
                "51",
                "14,6",
                "50,8"
            ], 1, "$y = 18,2 + 32,8 = 51$."),
            make_mc(6, "Bớt 4,25 ở số 10 thì được kết quả là:", [
                "5,75",
                "6,75",
                "5,85",
                "6,25"
            ], 0, "$10 - 4,25 = 5,75$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $92,3 - 48,75$\nb) $250 - 136,8$", "Bài giải:\na) $92,30 - 48,75 = 43,55$\nb) $250,0 - 136,8 = 113,2$\nĐáp số: a) 43,55; b) 113,2", "a) 43,55; b) 113,2", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$58,42 - (18,42 + 15)$", "Bài giải:\n$58,42 - 18,42 - 15 = 40 - 15 = 25$\nĐáp số: 25", "25", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$64,8 - x = 18,5 + 12,3$", "Bài giải:\n$64,8 - x = 30,8$\n$x = 64,8 - 30,8 = 34$\nĐáp số: $x = 34$", "x = 34", 4, 1.0),
            make_essay(4, "Một ô tô chở tất cả 3,5 tấn hàng gồm ngô và khoai. Khối lượng ngô là 1,85 tấn. Hỏi khối lượng khoai là bao nhiêu tấn? Khối lượng ngô nhiều hơn khối lượng khoai bao nhiêu tấn?", "Bài giải:\nKhối lượng khoai là:\n$3,5 - 1,85 = 1,65$ (tấn)\nKhối lượng ngô nhiều hơn khối lượng khoai là:\n$1,85 - 1,65 = 0,2$ (tấn)\nĐáp số: Khoai: 1,65 tấn; Ngô nhiều hơn khoai: 0,2 tấn.", "Khoai: 1,65 tấn; Hơn: 0,2 tấn", 6, 1.5),
            make_essay(5, "Một hình tam giác có chu vi là 35,4 cm. Tổng độ dài của cạnh thứ nhất và cạnh thứ hai là 24,8 cm. Cạnh thứ hai dài hơn cạnh thứ ba là 2,5 cm. Tính độ dài ba cạnh của hình tam giác đó.", "Bài giải:\nĐộ dài cạnh thứ ba là:\n$35,4 - 24,8 = 10,6$ (cm)\nĐộ dài cạnh thứ hai là:\n$10,6 + 2,5 = 13,1$ (cm)\nĐộ dài cạnh thứ nhất là:\n$24,8 - 13,1 = 11,7$ (cm)\nĐáp số: Cạnh 1: 11,7 cm; Cạnh 2: 13,1 cm; Cạnh 3: 10,6 cm.", "11,7 cm; 13,1 cm; 10,6 cm", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị của biểu thức:\n$C = 100 - 9,9 - 8,8 - 7,7 - 6,6 - 5,5 - 4,4 - 3,3 - 2,2 - 1,1$", "Bài giải:\n$C = 100 - (9,9 + 8,8 + 7,7 + 6,6 + 5,5 + 4,4 + 3,3 + 2,2 + 1,1)$\nTổng trong ngoặc là $49,5$.\n$C = 100 - 49,5 = 50,5$\nĐáp số: $C = 50,5$", "C = 50,5", 4, 1.0)
        ]
    }

    exams["th5_b16_test3"] = {
        "id": "th5_b16_test3",
        "lessonId": "th5_b16",
        "lessonNum": 16,
        "testNum": 3,
        "title": "Bài 16: Phép trừ số thập phân - Đề số 3",
        "topic": "Phép trừ số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $62,5 - 18,3 = ?$", ["44,2", "43,2", "44,8", "43,8"], 0, "$62,5 - 18,3 = 44,2$."),
            make_mc(2, "Kết quả của phép trừ $75 - 28,45$ là:", ["46,55", "46,65", "47,55", "47,65"], 0, "$75,00 - 28,45 = 46,55$."),
            make_mc(3, "Bình có 50 000 đồng, Bình mua bút chì hết 6 500 đồng và quyển vở hết 12 500 đồng. Số tiền Bình còn lại là:", [
                "31 000 đồng",
                "32 000 đồng",
                "30 000 đồng",
                "33 000 đồng"
            ], 0, "$50 000 - (6 500 + 12 500) = 31 000$ đồng."),
            make_mc(4, "Tìm $x$ biết $80 - x = 35,6$. Giá trị của $x$ là:", [
                "44,4",
                "45,4",
                "44,6",
                "54,4"
            ], 0, "$x = 80 - 35,6 = 44,4$."),
            make_mc(5, "Hiệu của số bé nhất có hai chữ số và số 3,75 là:", [
                "6,25",
                "7,25",
                "5,25",
                "6,35"
            ], 0, "Số bé nhất có hai chữ số là 10. $10 - 3,75 = 6,25$."),
            make_mc(6, "Điền dấu thích hợp: $15,8 - 5,2 ..... 10,8$", ["$<$", "$>$", "$=$", "Không so sánh được"], 0, "$15,8 - 5,2 = 10,6 < 10,8$, điền dấu $<$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $76,4 - 38,56$\nb) $310 - 148,25$", "Bài giải:\na) $76,40 - 38,56 = 37,84$\nb) $310,00 - 148,25 = 161,75$\nĐáp số: a) 37,84; b) 161,75", "a) 37,84; b) 161,75", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$75,86 - 24,35 - 15,65$", "Bài giải:\n$75,86 - (24,35 + 15,65) = 75,86 - 40 = 35,86$\nĐáp số: 35,86", "35,86", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x + 23,7 = 85,4 - 21,7$", "Bài giải:\n$x + 23,7 = 63,7$\n$x = 63,7 - 23,7 = 40$\nĐáp số: $x = 40$", "x = 40", 4, 1.0),
            make_essay(4, "Một bể nước chứa 2500 lít nước. Buổi sáng người ta đã dùng hết 850,5 lít nước. Buổi chiều dùng nhiều hơn buổi sáng 120 lít nước. Hỏi trong bể còn lại bao nhiêu lít nước?", "Bài giải:\nSố lít nước dùng trong buổi chiều là:\n$850,5 + 120 = 970,5$ (lít)\nCả hai buổi đã dùng số lít nước là:\n$850,5 + 970,5 = 1821$ (lít)\nTrong bể còn lại số lít nước là:\n$2500 - 1821 = 679$ (lít)\nĐáp số: 679 lít nước.", "679 lít", 6, 1.5),
            make_essay(5, "Đoạn đường từ tỉnh A đến tỉnh B dài 125,5 km. Một xe khách đi từ A đến B, sau khi đi được 2 giờ, mỗi giờ đi được 45,5 km thì xe dừng lại nghỉ. Hỏi xe khách còn cách tỉnh B bao nhiêu ki-lô-mét?", "Bài giải:\nQuãng đường xe khách đã đi được là:\n$45,5 \\times 2 = 91$ (km)\nXe khách còn cách tỉnh B số ki-lô-mét là:\n$125,5 - 91 = 34,5$ (km)\nĐáp số: 34,5 km.", "34,5 km", 6, 1.5),
            make_essay(6, "Cho biểu thức $D = 85,75 - a - b$. Tính giá trị của biểu thức $D$ khi $a = 18,35$ và $b = 31,65$ bằng cách thuận tiện nhất.", "Bài giải:\nThay $a = 18,35$ và $b = 31,65$ vào biểu thức:\n$D = 85,75 - 18,35 - 31,65$\n$D = 85,75 - (18,35 + 31,65)$\n$D = 85,75 - 50 = 35,75$\nĐáp số: $D = 35,75$", "D = 35,75", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 17: PHÉP NHÂN SỐ THẬP PHÂN
    # =========================================================================
    exams["th5_b17_test1"] = {
        "id": "th5_b17_test1",
        "lessonId": "th5_b17",
        "lessonNum": 17,
        "testNum": 1,
        "title": "Bài 17: Phép nhân số thập phân - Đề số 1",
        "topic": "Phép nhân số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $3,5 \\times 4 = ?$", ["14", "12", "14,5", "13,5"], 0, "$3,5 \\times 4 = 14,0 = 14$."),
            make_mc(2, "Tích của $2,5 \\times 1,4$ có bao nhiêu chữ số ở phần thập phân?", [
                "1 chữ số",
                "2 chữ số",
                "3 chữ số",
                "Không có chữ số nào"
            ], 1, "Cả hai thừa số có tất cả $1 + 1 = 2$ chữ số ở phần thập phân."),
            make_mc(3, "Kết quả của phép nhân $4,25 \\times 2$ là:", ["8,5", "8,25", "8,05", "9,5"], 0, "$4,25 \\times 2 = 8,50 = 8,5$."),
            make_mc(4, "Một mét vải giá 85 000 đồng. Mẹ mua 3,5 mét vải hết số tiền là:", [
                "297 500 đồng",
                "285 000 đồng",
                "255 000 đồng",
                "300 000 đồng"
            ], 0, "$85 000 \\times 3,5 = 297 500$ đồng."),
            make_mc(5, "Tính nhẩm: $0,8 \\times 0,5 = ?$", ["4", "0,4", "0,04", "0,45"], 1, "$8 \\times 5 = 40$, tách 2 chữ số thập phân được 0,40 = 0,4."),
            make_mc(6, "Biểu thức $a \\times (b + c) = a \\times b + a \\times c$ là tính chất gì của phép nhân?", [
                "Giao hoán của phép nhân",
                "Kết hợp của phép nhân",
                "Nhân một số với một tổng",
                "Nhân với số 1"
            ], 2, "Đây là tính chất nhân một số với một tổng (tính chất phân phối).")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $28,4 \\times 3,5$\nb) $15,6 \\times 4,2$", "Bài giải:\na) $28,4 \\times 3,5 = 99,40 = 99,4$\nb) $15,6 \\times 4,2 = 65,52$\nĐáp số: a) 99,4; b) 65,52", "a) 99,4; b) 65,52", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$2,5 \\times 4,8 \\times 4$", "Bài giải:\n$(2,5 \\times 4) \\times 4,8 = 10 \\times 4,8 = 48$\nĐáp số: 48", "48", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 3,2 = 4,5 + 1,5$", "Bài giải:\n$x : 3,2 = 6$\n$x = 6 \\times 3,2 = 19,2$\nĐáp số: $x = 19,2$", "x = 19,2", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chiều dài 24,5 m và chiều rộng 16 m.\na) Tính diện tích mảnh vườn hình chữ nhật đó.\nb) Người ta dùng 25% diện tích vườn để trồng hoa. Tính diện tích trồng hoa.", "Bài giải:\na) Diện tích mảnh vườn là:\n$24,5 \\times 16 = 392$ ($\\text{m}^2$)\nb) Diện tích phần đất trồng hoa là:\n$392 \\times 25 : 100 = 98$ ($\\text{m}^2$)\nĐáp số: a) 392 $\\text{m}^2$; b) 98 $\\text{m}^2$.", "a) 392 m²; b) 98 m²", 6, 1.5),
            make_essay(5, "Một ô tô chạy trong 3,5 giờ với vận tốc 48 km/h. Sau đó ô tô chạy tiếp trong 1,5 giờ với vận tốc 42 km/h. Hỏi ô tô đã chạy được tất cả bao nhiêu ki-lô-mét?", "Bài giải:\nQuãng đường ô tô chạy trong đoạn thứ nhất là:\n$48 \\times 3,5 = 168$ (km)\nQuãng đường ô tô chạy trong đoạn thứ hai là:\n$42 \\times 1,5 = 63$ (km)\nTổng quãng đường ô tô đã chạy là:\n$168 + 63 = 231$ (km)\nĐáp số: 231 km.", "231 km", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$M = 4,5 \\times 6,8 + 4,5 \\times 3,2$", "Bài giải:\n$M = 4,5 \\times (6,8 + 3,2) = 4,5 \\times 10 = 45$\nĐáp số: $M = 45$", "M = 45", 4, 1.0)
        ]
    }

    exams["th5_b17_test2"] = {
        "id": "th5_b17_test2",
        "lessonId": "th5_b17",
        "lessonNum": 17,
        "testNum": 2,
        "title": "Bài 17: Phép nhân số thập phân - Đề số 2",
        "topic": "Phép nhân số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $0,25 \\times 8 = ?$", ["2", "20", "0,2", "0,02"], 0, "$0,25 \\times 8 = 2,00 = 2$."),
            make_mc(2, "Kết quả của phép nhân $1,2 \\times 1,2$ là:", ["14,4", "1,44", "0,144", "144"], 1, "$12 \\times 12 = 144$, tách hai chữ số thập phân được 1,44."),
            make_mc(3, "Diện tích một hình vuông có cạnh dài 4,5 cm là:", [
                "18 $\\text{cm}^2$",
                "20,25 $\\text{cm}^2$",
                "20,5 $\\text{cm}^2$",
                "16,25 $\\text{cm}^2$"
            ], 1, "Diện tích: $4,5 \\times 4,5 = 20,25$ $\\text{cm}^2$."),
            make_mc(4, "Một ki-lô-gam táo có giá 45 000 đồng. Hỏi 2,4 kg táo giá bao nhiêu tiền?", [
                "108 000 đồng",
                "90 000 đồng",
                "110 000 đồng",
                "102 000 đồng"
            ], 0, "$45 000 \\times 2,4 = 108 000$ đồng."),
            make_mc(5, "Tìm $x$ biết $x : 2,5 = 4$. Giá trị của $x$ là:", [
                "10",
                "1",
                "100",
                "0,1"
            ], 0, "$x = 4 \\times 2,5 = 10$."),
            make_mc(6, "Tính nhanh: $0,4 \\times 125 \\times 2 = ?$", [
                "100",
                "10",
                "1000",
                "50"
            ], 0, "$0,4 \\times 250 = 100$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $36,8 \\times 2,4$\nb) $14,5 \\times 3,06$", "Bài giải:\na) $36,8 \\times 2,4 = 88,32$\nb) $14,5 \\times 3,06 = 44,37$\nĐáp số: a) 88,32; b) 44,37", "a) 88,32; b) 44,37", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$12,5 \\times 3,7 \\times 8$", "Bài giải:\n$(12,5 \\times 8) \\times 3,7 = 100 \\times 3,7 = 370$\nĐáp số: 370", "370", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 15,6 = 3,4 \\times 5$", "Bài giải:\n$x - 15,6 = 17$\n$x = 17 + 15,6 = 32,6$\nĐáp số: $x = 32,6$", "x = 32,6", 4, 1.0),
            make_essay(4, "Một người thợ dệt một mét vải tốn 1,45 giờ. Hỏi người đó dệt một tấm vải dài 36 m thì hết bao nhiêu giờ?", "Bài giải:\nThời gian người thợ dệt tấm vải là:\n$1,45 \\times 36 = 52,2$ (giờ)\nĐáp số: 52,2 giờ.", "52,2 giờ", 5, 1.5),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chiều dài 48,5 m và chiều rộng 25 m. Người ta cấy lúa trên thửa ruộng, cứ $100\\text{ m}^2$ thu hoạch được 70 kg thóc. Hỏi trên cả thửa ruộng người ta thu hoạch được bao nhiêu ki-lô-gam thóc?", "Bài giải:\nDiện tích thửa ruộng hình chữ nhật là:\n$48,5 \\times 25 = 1212,5$ ($\\text{m}^2$)\nSố thóc thu hoạch được trên thửa ruộng là:\n$1212,5 : 100 \\times 70 = 848,75$ (kg)\nĐáp số: 848,75 kg thóc.", "848,75 kg", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức:\n$N = 7,85 \\times 64 + 7,85 \\times 35 + 7,85$", "Bài giải:\n$N = 7,85 \\times (64 + 35 + 1) = 7,85 \\times 100 = 785$\nĐáp số: $N = 785$", "N = 785", 4, 1.0)
        ]
    }

    exams["th5_b17_test3"] = {
        "id": "th5_b17_test3",
        "lessonId": "th5_b17",
        "lessonNum": 17,
        "testNum": 3,
        "title": "Bài 17: Phép nhân số thập phân - Đề số 3",
        "topic": "Phép nhân số thập phân",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $0,5 \\times 0,2 = ?$", ["0,1", "0,01", "1", "0,001"], 0, "$5 \\times 2 = 10$, tách hai chữ số thập phân được 0,10 = 0,1."),
            make_mc(2, "Kết quả của phép nhân $5,6 \\times 1,5$ là:", ["8,4", "8,2", "7,4", "8,6"], 0, "$5,6 \\times 1,5 = 8,4$."),
            make_mc(3, "Một can đựng 4,5 lít mật ong, mỗi lít mật ong nặng 1,35 kg. Hỏi can mật ong đó nặng bao nhiêu ki-lô-gam (không tính vỏ can)?", [
                "6,075 kg",
                "6,75 kg",
                "5,85 kg",
                "6,05 kg"
            ], 0, "$1,35 \\times 4,5 = 6,075$ kg."),
            make_mc(4, "Biểu thức $3,6 \\times 5 + 3,6 \\times 5$ có giá trị bằng:", [
                "36",
                "18",
                "3,6",
                "72"
            ], 0, "$3,6 \\times (5 + 5) = 3,6 \\times 10 = 36$."),
            make_mc(5, "Tìm $x$ biết $x : 1,2 = 3,5$. Giá trị của $x$ là:", [
                "4,2",
                "4,7",
                "3,6",
                "2,3"
            ], 0, "$x = 3,5 \\times 1,2 = 4,2$."),
            make_mc(6, "Tích của số lẻ nhỏ nhất khác 1 và 7,45 là:", [
                "22,35",
                "14,9",
                "7,45",
                "29,8"
            ], 0, "Số lẻ nhỏ nhất khác 1 là 3. $3 \\times 7,45 = 22,35$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $45,7 \\times 3,8$\nb) $23,65 \\times 4,2$", "Bài giải:\na) $45,7 \\times 3,8 = 173,66$\nb) $23,65 \\times 4,2 = 99,33$\nĐáp số: a) 173,66; b) 99,33", "a) 173,66; b) 99,33", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$8,4 \\times 9,5 + 8,4 \\times 0,5$", "Bài giải:\n$8,4 \\times (9,5 + 0,5) = 8,4 \\times 10 = 84$\nĐáp số: 84", "84", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 2,4 = 12,5 - 8,5$", "Bài giải:\n$x : 2,4 = 4$\n$x = 4 \\times 2,4 = 9,6$\nĐáp số: $x = 9,6$", "x = 9,6", 4, 1.0),
            make_essay(4, "Một máy bay bay với vận tốc 650 km/h trong thời gian 2,4 giờ. Sau đó máy bay hạ bớt vận tốc xuống còn 580 km/h và bay thêm 1,5 giờ nữa thì đến nơi. Tính toàn bộ quãng đường máy bay đã bay.", "Bài giải:\nQuãng đường máy bay bay trong 2,4 giờ đầu là:\n$650 \\times 2,4 = 1560$ (km)\nQuãng đường máy bay bay trong 1,5 giờ sau là:\n$580 \\times 1,5 = 870$ (km)\nToàn bộ quãng đường máy bay đã bay là:\n$1560 + 870 = 2430$ (km)\nĐáp số: 2430 km.", "2430 km", 6, 1.5),
            make_essay(5, "Một căn phòng hình chữ nhật có chiều dài 8,5 m và chiều rộng 6,4 m. Người ta dùng gạch men hình vuông cạnh 40 cm để lát kín nền căn phòng đó (không tính mạch vữa). Hỏi cần bao nhiêu viên gạch men?", "Bài giải:\nDiện tích căn phòng hình chữ nhật là:\n$8,5 \\times 6,4 = 54,4$ ($\\text{m}^2$)\nĐổi cạnh viên gạch: $40\\text{ cm} = 0,4\\text{ m}$.\nDiện tích một viên gạch men là:\n$0,4 \\times 0,4 = 0,16$ ($\\text{m}^2$)\nSố viên gạch men cần dùng là:\n$54,4 : 0,16 = 340$ (viên)\nĐáp số: 340 viên gạch.", "340 viên", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị của biểu thức sau:\n$P = 0,8 \\times 96 + 1,6 \\times 2$", "Bài giải:\nTa có: $1,6 \\times 2 = 0,8 \\times 4$.\n$P = 0,8 \\times 96 + 0,8 \\times 4 = 0,8 \\times (96 + 4) = 0,8 \\times 100 = 80$\nĐáp số: $P = 80$", "P = 80", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 18: NHÂN SỐ THẬP PHÂN VỚI 10, 100, 1000... HOẶC VỚI 0,1; 0,01...
    # =========================================================================
    exams["th5_b18_test1"] = {
        "id": "th5_b18_test1",
        "lessonId": "th5_b18",
        "lessonNum": 18,
        "testNum": 1,
        "title": "Bài 18: Nhân số thập phân với 10, 100, 1000... hoặc 0,1; 0,01... - Đề số 1",
        "topic": "Nhân với 10, 100... hoặc 0,1; 0,01...",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn nhân một số thập phân với 10, 100, 1000... ta chỉ việc:", [
                "Chuyển dấu phẩy sang bên trái 1, 2, 3... chữ số",
                "Chuyển dấu phẩy sang bên phải 1, 2, 3... chữ số",
                "Thêm 1, 2, 3 chữ số 0 vào bên trái số đó",
                "Bỏ dấu phẩy đi"
            ], 1, "Khi nhân một số thập phân với 10, 100, 1000... ta chuyển dấu phẩy sang bên phải 1, 2, 3... chữ số."),
            make_mc(2, "Tính nhẩm: $3,456 \\times 100 = ?$", ["34,56", "345,6", "3456", "0,3456"], 1, "Dời dấu phẩy sang phải 2 chữ số: 345,6."),
            make_mc(3, "Muốn nhân một số thập phân với 0,1; 0,01; 0,001... ta chuyển dấu phẩy sang phía nào?", [
                "Bên phải 1, 2, 3... chữ số",
                "Bên trái 1, 2, 3... chữ số",
                "Giữ nguyên dấu phẩy",
                "Không chuyển được"
            ], 1, "Nhân với 0,1; 0,01... chuyển dấu phẩy sang bên trái 1, 2, 3... chữ số."),
            make_mc(4, "Tính nhẩm: $48,5 \\times 0,1 = ?$", ["485", "4,85", "0,485", "48,50"], 1, "Dời dấu phẩy sang trái 1 chữ số: 4,85."),
            make_mc(5, "Số nào dưới đây nhân với 0,01 thì được 0,75?", [
                "7,5",
                "75",
                "750",
                "0,075"
            ], 1, "$75 \\times 0,01 = 0,75$."),
            make_mc(6, "Một cuộn dây điện dài 100 m, mỗi mét nặng 0,085 kg. Cuộn dây điện đó nặng bao nhiêu ki-lô-gam?", [
                "0,85 kg",
                "8,5 kg",
                "85 kg",
                "850 kg"
            ], 1, "$0,085 \\times 100 = 8,5$ kg.")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) $4,08 \\times 10$\nb) $0,725 \\times 100$\nc) $25,4 \\times 0,1$\nd) $348 \\times 0,01$", "Bài giải:\na) $4,08 \\times 10 = 40,8$\nb) $0,725 \\times 100 = 72,5$\nc) $25,4 \\times 0,1 = 2,54$\nd) $348 \\times 0,01 = 3,48$\nĐáp số: a) 40,8; b) 72,5; c) 2,54; d) 3,48", "a) 40,8; b) 72,5; c) 2,54; d) 3,48", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$2,5 \\times 7,9 \\times 40$", "Bài giải:\n$(2,5 \\times 40) \\times 7,9 = 100 \\times 7,9 = 790$\nĐáp số: 790", "790", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x : 100 = 0,45 + 0,15$", "Bài giải:\n$x : 100 = 0,6$\n$x = 0,6 \\times 100 = 60$\nĐáp số: $x = 60$", "x = 60", 4, 1.0),
            make_essay(4, "Một ô tô chở 100 bao xi măng, mỗi bao nặng 50 kg và 10 thùng sơn, mỗi thùng nặng 18,5 kg. Hỏi ô tô đó chở tất cả bao nhiêu tấn hàng?", "Bài giải:\nKhối lượng của 100 bao xi măng là:\n$50 \\times 100 = 5000$ (kg)\nKhối lượng của 10 thùng sơn là:\n$18,5 \\times 10 = 185$ (kg)\nTổng khối lượng hàng ô tô chở là:\n$5000 + 185 = 5185$ (kg)\nĐổi $5185\\text{ kg} = 5,185\\text{ tấn}$\nĐáp số: 5,185 tấn hàng.", "5,185 tấn", 6, 1.5),
            make_essay(5, "Một khu đất hình chữ nhật có chiều rộng 45,5 m và chiều dài gấp 10 lần chiều rộng.\na) Tính chiều dài khu đất đó.\nb) Tính diện tích khu đất đó ra đơn vị mét vuông và đơn vị héc-ta.", "Bài giải:\na) Chiều dài khu đất là:\n$45,5 \\times 10 = 455$ (m)\nb) Diện tích khu đất là:\n$455 \\times 45,5 = 20702,5$ ($\\text{m}^2$)\nĐổi: $20702,5\\text{ m}^2 = 2,07025\\text{ ha}$\nĐáp số: a) 455 m; b) 20 702,5 $\\text{m}^2$ (hay 2,07025 ha).", "a) 455 m; b) 20702,5 m² = 2,07025 ha", 6, 1.5),
            make_essay(6, "Tính nhanh giá trị biểu thức sau:\n$Q = 3,45 \\times 99 + 3,45$", "Bài giải:\n$Q = 3,45 \\times (99 + 1) = 3,45 \\times 100 = 345$\nĐáp số: $Q = 345$", "Q = 345", 4, 1.0)
        ]
    }

    exams["th5_b18_test2"] = {
        "id": "th5_b18_test2",
        "lessonId": "th5_b18",
        "lessonNum": 18,
        "testNum": 2,
        "title": "Bài 18: Nhân số thập phân với 10, 100, 1000... hoặc 0,1; 0,01... - Đề số 2",
        "topic": "Nhân với 10, 100... hoặc 0,1; 0,01...",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $0,056 \\times 1000 = ?$", ["0,56", "5,6", "56", "560"], 2, "Dời dấu phẩy sang phải 3 chữ số: 56."),
            make_mc(2, "Tính: $35,8 \\times 0,01 = ?$", ["3,58", "0,358", "0,0358", "358"], 1, "Dời dấu phẩy sang trái 2 chữ số: 0,358."),
            make_mc(3, "Nhân một số với 0,1 có kết quả tương đương với phép tính nào?", [
                "Chia số đó cho 10",
                "Nhân số đó với 10",
                "Chia số đó cho 100",
                "Nhân số đó với 100"
            ], 0, "Nhân với 0,1 bằng chia cho 10."),
            make_mc(4, "Một can dầu chứa 10 lít dầu, mỗi lít dầu cân nặng 0,78 kg. Vỏ can nặng 0,5 kg. Hỏi cả can dầu nặng bao nhiêu ki-lô-gam?", [
                "7,8 kg",
                "8,3 kg",
                "7,3 kg",
                "8,5 kg"
            ], 1, "Dầu nặng $0,78 \\times 10 = 7,8$ kg. Cả can nặng $7,8 + 0,5 = 8,3$ kg."),
            make_mc(5, "Tìm $x$ biết $x : 10 = 2,45$. Giá trị của $x$ là:", [
                "0,245",
                "24,5",
                "245",
                "2,45"
            ], 1, "$x = 2,45 \\times 10 = 24,5$."),
            make_mc(6, "Tích của $0,004 \\times 100$ là:", [
                "0,04",
                "0,4",
                "4",
                "40"
            ], 1, "$0,004 \\times 100 = 0,4$.")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) $12,45 \\times 100$\nb) $0,009 \\times 1000$\nc) $456,8 \\times 0,01$\nd) $78 \\times 0,1$", "Bài giải:\na) $12,45 \\times 100 = 1245$\nb) $0,009 \\times 1000 = 9$\nc) $456,8 \\times 0,01 = 4,568$\nd) $78 \\times 0,1 = 7,8$\nĐáp số: a) 1245; b) 9; c) 4,568; d) 7,8", "a) 1245; b) 9; c) 4,568; d) 7,8", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$0,25 \\times 6,75 \\times 400$", "Bài giải:\n$(0,25 \\times 400) \\times 6,75 = 100 \\times 6,75 = 675$\nĐáp số: 675", "675", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 0,1 = 4,5 - 2,75$", "Bài giải:\n$x \\times 0,1 = 1,75$\n$x = 1,75 : 0,1 = 17,5$\nĐáp số: $x = 17,5$", "x = 17,5", 4, 1.0),
            make_essay(4, "Một tấm kính hình chữ nhật có chiều dài 1,8 m và chiều rộng 0,75 m. Người ta cắt từ tấm kính đó ra 10 miếng kính nhỏ có diện tích như nhau. Hỏi diện tích mỗi miếng kính nhỏ là bao nhiêu mét vuông?", "Bài giải:\nDiện tích tấm kính ban đầu là:\n$1,8 \\times 0,75 = 1,35$ ($\\text{m}^2$)\nDiện tích mỗi miếng kính nhỏ là:\n$1,35 : 10 = 0,135$ ($\\text{m}^2$)\nĐáp số: 0,135 $\\text{m}^2$.", "0,135 m²", 6, 1.5),
            make_essay(5, "Một đoàn xe tải gồm 10 chiếc xe loại lớn, mỗi xe chở được 4,5 tấn hàng và 10 chiếc xe loại nhỏ, mỗi xe chở được 2,8 tấn hàng. Hỏi cả đoàn xe đó chở được tất cả bao nhiêu tấn hàng?", "Bài giải:\n10 chiếc xe loại lớn chở được số tấn hàng là:\n$4,5 \\times 10 = 45$ (tấn)\n10 chiếc xe loại nhỏ chở được số tấn hàng là:\n$2,8 \\times 10 = 28$ (tấn)\nCả đoàn xe chở được số tấn hàng là:\n$45 + 28 = 73$ (tấn)\nĐáp số: 73 tấn hàng.", "73 tấn", 6, 1.5),
            make_essay(6, "Tính nhanh:\n$K = 1,25 \\times 4,6 \\times 80$", "Bài giải:\n$K = (1,25 \\times 80) \\times 4,6 = 100 \\times 4,6 = 460$\nĐáp số: $K = 460$", "K = 460", 4, 1.0)
        ]
    }

    exams["th5_b18_test3"] = {
        "id": "th5_b18_test3",
        "lessonId": "th5_b18",
        "lessonNum": 18,
        "testNum": 3,
        "title": "Bài 18: Nhân số thập phân với 10, 100, 1000... hoặc 0,1; 0,01... - Đề số 3",
        "topic": "Nhân với 10, 100... hoặc 0,1; 0,01...",
        "chapter": "Chủ đề 3: Các phép tính với số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $7,8 \\times 100 = ?$", ["78", "780", "7800", "0,78"], 1, "Dời dấu phẩy sang phải 2 chữ số: 780."),
            make_mc(2, "Tính: $125 \\times 0,001 = ?$", ["1,25", "0,125", "0,0125", "12,5"], 1, "Dời dấu phẩy sang trái 3 chữ số: 0,125."),
            make_mc(3, "Nhân một số thập phân với 0,01 bằng:", [
                "Chia số đó cho 10",
                "Chia số đó cho 100",
                "Nhân số đó với 100",
                "Chia số đó cho 1000"
            ], 1, "Nhân với 0,01 bằng chia cho 100."),
            make_mc(4, "Biểu thức $0,45 \\times 10 + 0,45 \\times 90$ có giá trị là:", [
                "45",
                "450",
                "4,5",
                "0,45"
            ], 0, "$0,45 \\times (10 + 90) = 0,45 \\times 100 = 45$."),
            make_mc(5, "Đổi 4,5 tạ ra ki-lô-gam bằng cách nhân với 100 ta được:", [
                "45 kg",
                "450 kg",
                "4500 kg",
                "0,45 kg"
            ], 1, "$4,5 \\times 100 = 450$ kg."),
            make_mc(6, "Tìm $x$ biết $x : 100 = 0,08$. Giá trị của $x$ là:", [
                "0,8",
                "8",
                "80",
                "0,0008"
            ], 1, "$x = 0,08 \\times 100 = 8$.")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) $3,14 \\times 10$\nb) $0,058 \\times 100$\nc) $128,5 \\times 0,1$\nd) $560 \\times 0,01$", "Bài giải:\na) $3,14 \\times 10 = 31,4$\nb) $0,058 \\times 100 = 5,8$\nc) $128,5 \\times 0,1 = 12,85$\nd) $560 \\times 0,01 = 5,6$\nĐáp số: a) 31,4; b) 5,8; c) 12,85; d) 5,6", "a) 31,4; b) 5,8; c) 12,85; d) 5,6", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$0,5 \\times 9,84 \\times 20$", "Bài giải:\n$(0,5 \\times 20) \\times 9,84 = 10 \\times 9,84 = 98,4$\nĐáp số: 98,4", "98,4", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 0,01 = 0,25 + 0,35$", "Bài giải:\n$x \\times 0,01 = 0,6$\n$x = 0,6 : 0,01 = 0,6 \\times 100 = 60$\nĐáp số: $x = 60$", "x = 60", 4, 1.0),
            make_essay(4, "Một người thợ tiện 100 chi tiết máy, mỗi chi tiết bằng kim loại nặng 0,45 kg. Người đó đóng tất cả số chi tiết máy vào các hộp, mỗi hộp chứa 10 chi tiết. Hỏi:\na) Tổng khối lượng kim loại của 100 chi tiết máy là bao nhiêu ki-lô-gam?\nb) Mỗi hộp nặng bao nhiêu ki-lô-gam (không tính vỏ hộp)?", "Bài giải:\na) Tổng khối lượng của 100 chi tiết máy là:\n$0,45 \\times 100 = 45$ (kg)\nb) Mỗi hộp chứa 10 chi tiết máy nặng số ki-lô-gam là:\n$0,45 \\times 10 = 4,5$ (kg)\nĐáp số: a) 45 kg; b) 4,5 kg.", "a) 45 kg; b) 4,5 kg", 6, 1.5),
            make_essay(5, "Một khu rừng hình chữ nhật có chiều dài 1,5 km và chiều rộng 0,8 km. Tính diện tích khu rừng đó ra đơn vị héc-ta (biết $1\\text{ km}^2 = 100\\text{ ha}$).", "Bài giải:\nDiện tích khu rừng theo đơn vị ki-lô-mét vuông là:\n$1,5 \\times 0,8 = 1,2$ ($\\text{km}^2$)\nĐổi sang đơn vị héc-ta bằng cách nhân với 100:\n$1,2 \\times 100 = 120$ (ha)\nĐáp số: 120 ha.", "120 ha", 5, 1.5),
            make_essay(6, "Tính nhanh giá trị của biểu thức:\n$T = 0,48 \\times 990 + 4,8$", "Bài giải:\nTa có: $4,8 = 0,48 \\times 10$.\nBiểu thức trở thành:\n$T = 0,48 \\times 990 + 0,48 \\times 10$\n$T = 0,48 \\times (990 + 10) = 0,48 \\times 1000 = 480$\nĐáp số: $T = 480$", "T = 480", 5, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_ch3_part1_exams()
    print(f"Chủ đề 3 Phần 1: {len(ex)} đề (Kỳ vọng: 12 đề)")
