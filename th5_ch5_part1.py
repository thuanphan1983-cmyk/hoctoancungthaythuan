# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 5: ÔN TẬP HỌC KÌ 1 (BÀI 26 ĐẾN BÀI 29) - PHẦN 1: BÀI 26 VÀ BÀI 27
Toán lớp 5 - Kết nối tri thức với cuộc sống.
Gồm 6 đề kiểm tra:
- Bài 26: Ôn tập về số và các phép tính (th5_b26_test1, th5_b26_test2, th5_b26_test3)
- Bài 27: Ôn tập hình học và đo lường (th5_b27_test1, th5_b27_test2, th5_b27_test3)
"""

def get_ch5_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 26: ÔN TẬP VỀ SỐ VÀ CÁC PHÉP TÍNH (TEST 1, 2, 3)
    # =========================================================================

    exams["th5_b26_test1"] = {
        "title": "ĐỀ KIỂM TRA BÀI 26 (ĐỀ 1): ÔN TẬP VỀ SỐ VÀ CÁC PHÉP TÍNH",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Trong số thập phân 45,823, chữ số 8 có giá trị là:",
                "choices": ["8", "8/10", "8/100", "8/1000"],
                "correct": 1,
                "explanation": "Chữ số 8 đứng ở hàng phần mười ngay sau dấu phẩy nên có giá trị là 8/10 (hay 0,8).",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Hỗn số 3 và 2/5 được chuyển thành phân số nào dưới đây?",
                "choices": ["11/5", "17/5", "6/5", "13/5"],
                "correct": 1,
                "explanation": "Ta có: 3 và 2/5 = (3 x 5 + 2) / 5 = 17/5.",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Dãy số thập phân nào dưới đây được sắp xếp theo thứ tự từ bé đến lớn?",
                "choices": [
                    "4,52 ; 4,502 ; 4,5 ; 4,25",
                    "4,25 ; 4,5 ; 4,502 ; 4,52",
                    "4,52 ; 4,502 ; 4,25 ; 4,5",
                    "4,25 ; 4,502 ; 4,5 ; 4,52"
                ],
                "correct": 1,
                "explanation": "So sánh phần thập phân: 4,25 < 4,500 < 4,502 < 4,520 nên dãy xếp từ bé đến lớn là 4,25 ; 4,5 ; 4,502 ; 4,52.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Kết quả của phép tính 42,65 + 18,7 là:",
                "choices": ["60,72", "61,35", "61,42", "60,35"],
                "correct": 1,
                "explanation": "Đặt tính cộng: 42,65 + 18,70 = 61,35.",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Kết quả của phép nhân phân số 5/9 x 3/10 sau khi rút gọn tối giản là:",
                "choices": ["1/6", "15/90", "1/3", "5/30"],
                "correct": 0,
                "explanation": "5/9 x 3/10 = (5 x 3) / (9 x 10) = 15/90 = 1/6.",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Khi nhân một số thập phân với 0,1, ta chỉ việc:",
                "choices": [
                    "Chuyển dấu phẩy của số đó sang bên phải một chữ số",
                    "Chuyển dấu phẩy của số đó sang bên trái một chữ số",
                    "Chuyển dấu phẩy của số đó sang bên trái hai chữ số",
                    "Thêm một chữ số 0 vào bên phải số đó"
                ],
                "correct": 1,
                "explanation": "Nhân một số với 0,1 tương đương chia số đó cho 10, nên ta chuyển dấu phẩy sang bên trái một chữ số.",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Đặt tính rồi tính:\na) 258,47 + 69,85\nb) 715,3 - 48,65",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Đặt tính và cộng thẳng hàng: 258,47 + 69,85 = 328,32\nb) Đặt tính và trừ thẳng hàng (thêm chữ số 0 ở hàng phần trăm): 715,30 - 48,65 = 666,65\nĐáp số: a) 328,32; b) 666,65.",
                "answer": "a) 328,32; b) 666,65"
            },
            {
                "question": "**Bài 2:** Đặt tính rồi tính:\na) 34,5 x 4,6\nb) 88,2 : 36",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 34,5 x 4,6: Thực hiện nhân như số tự nhiên rồi đếm 2 chữ số ở phần thập phân: 34,5 x 4,6 = 158,70 = 158,7\nb) 88,2 : 36: Chia phần nguyên được 2 dư 16; viết dấu phẩy vào thương; hạ 2 được 162, chia 36 được 4 dư 18; thêm 0 được 180, chia 36 được 5: 88,2 : 36 = 2,45\nĐáp số: a) 158,7; b) 2,45.",
                "answer": "a) 158,7; b) 2,45"
            },
            {
                "question": "**Bài 3:** Tính bằng cách thuận tiện nhất:\n12,5 x 4,8 + 12,5 x 5,2",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Áp dụng tính chất phân phối của phép nhân đối với phép cộng:\n12,5 x 4,8 + 12,5 x 5,2 = 12,5 x (4,8 + 5,2)\n= 12,5 x 10\n= 125\nĐáp số: 125.",
                "answer": "125"
            },
            {
                "question": "**Bài 4:** Tìm x, biết:\na) x - 14,5 = 38,2\nb) x x 2,5 = 45",
                "points": 1.5,
                "lineCount": 5,
                "solution": "a) x - 14,5 = 38,2\nx = 38,2 + 14,5\nx = 52,7\nb) x x 2,5 = 45\nx = 45 : 2,5\nx = 18\nĐáp số: a) x = 52,7; b) x = 18.",
                "answer": "a) x = 52,7; b) x = 18"
            },
            {
                "question": "**Bài 5:** Một cửa hàng ngày thứ nhất bán được 125,5 kg gạo. Ngày thứ hai bán được nhiều hơn ngày thứ nhất 28,4 kg gạo. Ngày thứ ba bán được số gạo bằng trung bình cộng của hai ngày đầu. Hỏi cả ba ngày cửa hàng bán được bao nhiêu ki-lô-gam gạo?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "Ngày thứ hai cửa hàng bán được số ki-lô-gam gạo là:\n125,5 + 28,4 = 153,9 (kg)\nNgày thứ ba cửa hàng bán được số ki-lô-gam gạo là:\n(125,5 + 153,9) : 2 = 139,7 (kg)\nCả ba ngày cửa hàng bán được số ki-lô-gam gạo là:\n125,5 + 153,9 + 139,7 = 419,1 (kg)\nĐáp số: 419,1 kg gạo.",
                "answer": "419,1 kg"
            },
            {
                "question": "**Bài 6:** Tìm một số tự nhiên có hai chữ số, biết rằng nếu viết thêm chữ số 3 vào bên trái số đó thì được số mới gấp 7 lần số ban đầu.",
                "points": 1.0,
                "lineCount": 5,
                "solution": "Gọi số tự nhiên có hai chữ số cần tìm là ab (a khác 0; a, b là chữ số).\nKhi viết thêm chữ số 3 vào bên trái số đó ta được số 3ab.\nTheo đề bài ta có:\n3ab = 7 x ab\n300 + ab = 7 x ab\n300 = 7 x ab - ab\n300 = 6 x ab\nab = 300 : 6\nab = 50\nVậy số cần tìm là 50.\nĐáp số: 50.",
                "answer": "50"
            }
        ]
    }

    exams["th5_b26_test2"] = {
        "title": "ĐỀ KIỂM TRA BÀI 26 (ĐỀ 2): ÔN TẬP VỀ SỐ VÀ CÁC PHÉP TÍNH",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Số thập phân gồm 5 đơn vị, 3 phần mười và 8 phần nghìn được viết là:",
                "choices": ["5,38", "5,308", "5,038", "53,8"],
                "correct": 1,
                "explanation": "Số có 5 đơn vị, hàng phần mười là 3, hàng phần trăm là 0, hàng phần nghìn là 8 nên viết là 5,308.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Rút gọn phân số 36/48 về phân số tối giản ta được:",
                "choices": ["6/8", "18/24", "3/4", "9/12"],
                "correct": 2,
                "explanation": "Cả tử số và mẫu số cùng chia hết cho 12: 36 : 12 = 3; 48 : 12 = 4. Vậy tối giản là 3/4.",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Phân số nào dưới đây bằng số thập phân 0,45?",
                "choices": ["45/10", "9/20", "4/5", "45/1000"],
                "correct": 1,
                "explanation": "0,45 = 45/100. Chia cả tử và mẫu cho 5 ta được 9/20.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Kết quả của phép tính 84,6 : 6 là:",
                "choices": ["14,1", "1,41", "141", "14,01"],
                "correct": 0,
                "explanation": "84,6 : 6: 8 chia 6 được 1 dư 2; hạ 4 được 24 chia 6 được 4; viết phẩy; hạ 6 chia 6 được 1. Kết quả là 14,1.",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Tìm x, biết x + 3,75 = 10. Giá trị của x là:",
                "choices": ["6,25", "6,35", "7,25", "13,75"],
                "correct": 0,
                "explanation": "x = 10 - 3,75 = 6,25.",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Một mảnh vải dài 12 m. Người ta cắt đi 2/3 chiều dài mảnh vải. Chiều dài mảnh vải còn lại là:",
                "choices": ["8 m", "4 m", "6 m", "9 m"],
                "correct": 1,
                "explanation": "Phân số chỉ số mét vải còn lại là: 1 - 2/3 = 1/3 (mảnh vải). Chiều dài còn lại là: 12 x 1/3 = 4 (m).",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Đặt tính rồi tính:\na) 456,78 + 235,46\nb) 500 - 138,42",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 456,78 + 235,46 = 692,24\nb) 500,00 - 138,42 = 361,58\nĐáp số: a) 692,24; b) 361,58.",
                "answer": "a) 692,24; b) 361,58"
            },
            {
                "question": "**Bài 2:** Đặt tính rồi tính:\na) 28,4 x 3,5\nb) 75,6 : 18",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 28,4 x 3,5 = 99,4\nb) 75,6 : 18: 75 : 18 = 4 dư 3; phẩy; hạ 6 được 36 : 18 = 2. Kết quả = 4,2\nĐáp số: a) 99,4; b) 4,2.",
                "answer": "a) 99,4; b) 4,2"
            },
            {
                "question": "**Bài 3:** Tính bằng cách thuận tiện nhất:\n7,89 x 6,4 + 7,89 x 3,6",
                "points": 1.0,
                "lineCount": 4,
                "solution": "7,89 x 6,4 + 7,89 x 3,6 = 7,89 x (6,4 + 3,6)\n= 7,89 x 10\n= 78,9\nĐáp số: 78,9.",
                "answer": "78,9"
            },
            {
                "question": "**Bài 4:** Tìm x, biết:\na) x : 1,4 = 15,2\nb) x x 0,8 = 16,4 - 4,4",
                "points": 1.5,
                "lineCount": 5,
                "solution": "a) x : 1,4 = 15,2\nx = 15,2 x 1,4\nx = 21,28\nb) x x 0,8 = 16,4 - 4,4\nx x 0,8 = 12\nx = 12 : 0,8\nx = 15\nĐáp số: a) x = 21,28; b) x = 15.",
                "answer": "a) x = 21,28; b) x = 15"
            },
            {
                "question": "**Bài 5:** Hai kho chứa tất cả 350 tấn thóc. Biết rằng số thóc ở kho thứ nhất bằng 3/4 số thóc ở kho thứ hai. Hỏi mỗi kho chứa bao nhiêu tấn thóc?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "Tổng số phần bằng nhau là:\n3 + 4 = 7 (phần)\nKho thứ nhất chứa số tấn thóc là:\n350 : 7 x 3 = 150 (tấn)\nKho thứ hai chứa số tấn thóc là:\n350 - 150 = 200 (tấn)\nĐáp số: Kho thứ nhất: 150 tấn thóc; Kho thứ hai: 200 tấn thóc.",
                "answer": "Kho thứ nhất: 150 tấn; Kho thứ hai: 200 tấn"
            },
            {
                "question": "**Bài 6:** Tính nhanh giá trị biểu thức:\nA = 1/(2 x 3) + 1/(3 x 4) + 1/(4 x 5) + 1/(5 x 6)",
                "points": 1.0,
                "lineCount": 5,
                "solution": "Ta có nhận xét: 1/(n x (n+1)) = 1/n - 1/(n+1).\nDo đó:\nA = 1/2 - 1/3 + 1/3 - 1/4 + 1/4 - 1/5 + 1/5 - 1/6\nA = 1/2 - 1/6\nA = 3/6 - 1/6 = 2/6 = 1/3\nĐáp số: 1/3.",
                "answer": "1/3"
            }
        ]
    }

    exams["th5_b26_test3"] = {
        "title": "ĐỀ KIỂM TRA BÀI 26 (ĐỀ 3): ÔN TẬP VỀ SỐ VÀ CÁC PHÉP TÍNH",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Trong các số thập phân 7,85; 7,805; 7,851; 7,589, số thập phân lớn nhất là:",
                "choices": ["7,85", "7,805", "7,851", "7,589"],
                "correct": 2,
                "explanation": "Các số đều có phần nguyên là 7. So sánh phần thập phân: 851 phần nghìn lớn nhất, nên 7,851 lớn nhất.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Phân số 7/25 được viết dưới dạng số thập phân là:",
                "choices": ["0,28", "0,7", "0,14", "0,35"],
                "correct": 0,
                "explanation": "7/25 = (7 x 4) / (25 x 4) = 28/100 = 0,28.",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Kết quả của phép trừ phân số 7/8 - 3/4 là:",
                "choices": ["4/4", "1/8", "4/8", "1/4"],
                "correct": 1,
                "explanation": "Quy đồng mẫu số: 3/4 = 6/8. Ta có: 7/8 - 6/8 = 1/8.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Một can chứa 5 lít dầu hỏa cân nặng 4,25 kg. Hỏi 1 lít dầu hỏa đó cân nặng bao nhiêu ki-lô-gam?",
                "choices": ["0,85 kg", "0,75 kg", "0,95 kg", "0,8 kg"],
                "correct": 0,
                "explanation": "1 lít dầu hỏa nặng: 4,25 : 5 = 0,85 (kg).",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Tính nhẩm: 48,5 x 0,01 có kết quả là:",
                "choices": ["4,85", "4850", "0,485", "0,0485"],
                "correct": 2,
                "explanation": "Khi nhân một số thập phân với 0,01, ta dịch dấu phẩy sang bên trái hai chữ số: 48,5 x 0,01 = 0,485.",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Số tự nhiên x thỏa mãn 4,8 < x < 5,9 là:",
                "choices": ["4", "5", "6", "5,5"],
                "correct": 1,
                "explanation": "Số tự nhiên nằm giữa 4,8 và 5,9 chỉ có duy nhất số 5.",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Đặt tính rồi tính:\na) 684,35 + 247,8\nb) 820,4 - 365,78",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 684,35 + 247,80 = 932,15\nb) 820,40 - 365,78 = 454,62\nĐáp số: a) 932,15; b) 454,62.",
                "answer": "a) 932,15; b) 454,62"
            },
            {
                "question": "**Bài 2:** Đặt tính rồi tính:\na) 42,8 x 2,5\nb) 123,5 : 25",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 42,8 x 2,5 = 107\nb) 123,5 : 25 = 4,94 (123 : 25 = 4 dư 23; phẩy; hạ 5 được 235 : 25 = 9 dư 10; thêm 0 được 100 : 25 = 4)\nĐáp số: a) 107; b) 4,94.",
                "answer": "a) 107; b) 4,94"
            },
            {
                "question": "**Bài 3:** Tính bằng cách thuận tiện nhất:\n2,5 x 9,7 x 4",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Áp dụng tính chất giao hoán và kết hợp của phép nhân:\n2,5 x 9,7 x 4 = (2,5 x 4) x 9,7\n= 10 x 9,7\n= 97\nĐáp số: 97.",
                "answer": "97"
            },
            {
                "question": "**Bài 4:** Tìm x, biết:\na) 45,8 - x = 19,65\nb) x : 3,2 = 4,5 + 1,5",
                "points": 1.5,
                "lineCount": 5,
                "solution": "a) 45,8 - x = 19,65\nx = 45,8 - 19,65\nx = 26,15\nb) x : 3,2 = 4,5 + 1,5\nx : 3,2 = 6\nx = 6 x 3,2\nx = 19,2\nĐáp số: a) x = 26,15; b) x = 19,2.",
                "answer": "a) x = 26,15; b) x = 19,2"
            },
            {
                "question": "**Bài 5:** Một mảnh vườn hình chữ nhật có chu vi là 160 m, chiều rộng kém chiều dài 20 m. Người ta dùng 3/5 diện tích mảnh vườn để trồng rau. Tính diện tích phần đất trồng rau.",
                "points": 1.5,
                "lineCount": 6,
                "solution": "Nửa chu vi mảnh vườn là:\n160 : 2 = 80 (m)\nChiều dài mảnh vườn là:\n(80 + 20) : 2 = 50 (m)\nChiều rộng mảnh vườn là:\n50 - 20 = 30 (m)\nDiện tích mảnh vườn là:\n50 x 30 = 1500 (m²)\nDiện tích đất trồng rau là:\n1500 x 3/5 = 900 (m²)\nĐáp số: 900 m².",
                "answer": "900 m²"
            },
            {
                "question": "**Bài 6:** Tìm số tự nhiên a biết: a/12 = 15/20.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Rút gọn phân số 15/20:\n15/20 = (15 : 5) / (20 : 5) = 3/4\nQuy đồng mẫu số để có mẫu số là 12:\n3/4 = (3 x 3) / (4 x 3) = 9/12\nVì a/12 = 9/12 nên a = 9.\nĐáp số: a = 9.",
                "answer": "a = 9"
            }
        ]
    }

    # =========================================================================
    # BÀI 27: ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG (TEST 1, 2, 3)
    # =========================================================================

    exams["th5_b27_test1"] = {
        "title": "ĐỀ KIỂM TRA BÀI 27 (ĐỀ 1): ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Số thập phân thích hợp điền vào chỗ chấm để 3 tấn 45 kg = ... tấn là:",
                "choices": ["3,45", "3,045", "3,450", "30,45"],
                "correct": 1,
                "explanation": "1 tấn = 1000 kg nên 45 kg = 0,045 tấn. Vậy 3 tấn 45 kg = 3,045 tấn.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Viết số đo 4 m² 25 dm² dưới dạng số thập phân với đơn vị mét vuông ta được:",
                "choices": ["4,25 m²", "4,025 m²", "4,250 m²", "42,5 m²"],
                "correct": 0,
                "explanation": "1 m² = 100 dm² nên 25 dm² = 0,25 m². Do đó 4 m² 25 dm² = 4,25 m².",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Một hình tam giác có độ dài đáy là 14 cm và chiều cao tương ứng là 8 cm. Diện tích của hình tam giác đó là:",
                "choices": ["112 cm²", "56 cm²", "28 cm²", "44 cm²"],
                "correct": 1,
                "explanation": "Diện tích tam giác = (14 x 8) : 2 = 56 (cm²).",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Một hình thang có đáy lớn 12 cm, đáy bé 8 cm và chiều cao 5 cm. Diện tích của hình thang đó là:",
                "choices": ["100 cm²", "50 cm²", "60 cm²", "40 cm²"],
                "correct": 1,
                "explanation": "Diện tích hình thang = (12 + 8) x 5 : 2 = 20 x 5 : 2 = 50 (cm²).",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Chu vi hình tròn có bán kính r = 5 cm là:",
                "choices": ["15,7 cm", "31,4 cm", "78,5 cm", "62,8 cm"],
                "correct": 1,
                "explanation": "Chu vi hình tròn = 5 x 2 x 3,14 = 31,4 (cm).",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Một khu rừng hình chữ nhật có chiều dài 2 km và chiều rộng 1,5 km. Diện tích của khu rừng đó là bao nhiêu héc-ta?",
                "choices": ["30 ha", "300 ha", "3000 ha", "3 ha"],
                "correct": 1,
                "explanation": "Diện tích khu rừng = 2 x 1,5 = 3 (km²). Vì 1 km² = 100 ha nên 3 km² = 300 ha.",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Viết số thập phân thích hợp vào chỗ chấm:\na) 7 km 35 m = ... km\nb) 15 tạ 6 kg = ... tạ\nc) 8 m² 5 dm² = ... m²\nd) 45 ha = ... km²",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 35 m = 0,035 km => 7 km 35 m = 7,035 km\nb) 6 kg = 0,06 tạ => 15 tạ 6 kg = 15,06 tạ\nc) 5 dm² = 0,05 m² => 8 m² 5 dm² = 8,05 m²\nd) 1 ha = 0,01 km² => 45 ha = 0,45 km²\nĐáp số: a) 7,035 km; b) 15,06 tạ; c) 8,05 m²; d) 0,45 km².",
                "answer": "a) 7,035 km; b) 15,06 tạ; c) 8,05 m²; d) 0,45 km²"
            },
            {
                "question": "**Bài 2:** Tính chu vi và diện tích của hình tròn có bán kính r = 4 cm.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Chu vi của hình tròn là:\n4 x 2 x 3,14 = 25,12 (cm)\nDiện tích của hình tròn là:\n4 x 4 x 3,14 = 50,24 (cm²)\nĐáp số: Chu vi: 25,12 cm; Diện tích: 50,24 cm².",
                "answer": "Chu vi: 25,12 cm; Diện tích: 50,24 cm²"
            },
            {
                "question": "**Bài 3:** Một thửa ruộng hình thang có đáy lớn 40 m, đáy bé 30 m và chiều cao bằng trung bình cộng của hai đáy. Tính diện tích của thửa ruộng hình thang đó.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Chiều cao của thửa ruộng là:\n(40 + 30) : 2 = 35 (m)\nDiện tích của thửa ruộng hình thang là:\n(40 + 30) x 35 : 2 = 1225 (m²)\nĐáp số: 1225 m².",
                "answer": "1225 m²"
            },
            {
                "question": "**Bài 4:** Một sân vận động hình chữ nhật có chiều dài 120 m, chiều rộng bằng 3/4 chiều dài.\na) Tính diện tích sân vận động đó theo đơn vị mét vuông và héc-ta.\nb) Người ta lát cỏ nhân tạo cho sân vận động, chi phí mỗi mét vuông là 150 000 đồng. Tính tổng chi phí lát cỏ cho sân vận động.",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Chiều rộng sân vận động là:\n120 x 3/4 = 90 (m)\nDiện tích sân vận động là:\n120 x 90 = 10 800 (m²)\nĐổi: 10 800 m² = 1,08 ha\nb) Tổng chi phí lát cỏ nhân tạo là:\n10 800 x 150 000 = 1 620 000 000 (đồng)\nĐáp số: a) 10 800 m² (1,08 ha); b) 1 620 000 000 đồng.",
                "answer": "a) 10 800 m² (1,08 ha); b) 1 620 000 000 đồng"
            },
            {
                "question": "**Bài 5:** Một bồn hoa gồm một hình vuông cạnh 6 m và hai nửa hình tròn có đường kính bằng cạnh của hình vuông được ghép vào hai phía đối diện. Tính diện tích của toàn bộ bồn hoa đó.",
                "points": 1.5,
                "lineCount": 5,
                "solution": "Diện tích phần hình vuông là:\n6 x 6 = 36 (m²)\nBán kính của hai nửa hình tròn là:\n6 : 2 = 3 (m)\nHai nửa hình tròn ghép lại thành một hình tròn có bán kính 3 m. Diện tích hình tròn đó là:\n3 x 3 x 3,14 = 28,26 (m²)\nDiện tích toàn bộ bồn hoa là:\n36 + 28,26 = 64,26 (m²)\nĐáp số: 64,26 m².",
                "answer": "64,26 m²"
            },
            {
                "question": "**Bài 6:** Một hình tam giác có diện tích 75 cm². Nếu kéo dài cạnh đáy thêm 4 cm thì diện tích tam giác tăng thêm 20 cm². Tính độ dài cạnh đáy ban đầu của tam giác.",
                "points": 1.0,
                "lineCount": 5,
                "solution": "Phần diện tích tăng thêm là một hình tam giác có đáy 4 cm và chiều cao chính là chiều cao của tam giác ban đầu.\nChiều cao của hình tam giác là:\n20 x 2 : 4 = 10 (cm)\nĐộ dài cạnh đáy ban đầu của tam giác là:\n75 x 2 : 10 = 15 (cm)\nĐáp số: 15 cm.",
                "answer": "15 cm"
            }
        ]
    }

    exams["th5_b27_test2"] = {
        "title": "ĐỀ KIỂM TRA BÀI 27 (ĐỀ 2): ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Số thích hợp điền vào chỗ chấm để 5 m 8 cm = ... m là:",
                "choices": ["5,8", "5,08", "5,008", "58"],
                "correct": 1,
                "explanation": "1 m = 100 cm nên 8 cm = 0,08 m. Do đó 5 m 8 cm = 5,08 m.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Đổi số đo diện tích 2,5 ha ra mét vuông ta được:",
                "choices": ["250 m²", "2 500 m²", "25 000 m²", "250 000 m²"],
                "correct": 2,
                "explanation": "1 ha = 10 000 m² nên 2,5 ha = 2,5 x 10 000 = 25 000 m².",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Diện tích hình tròn có đường kính d = 8 cm là:",
                "choices": ["200,96 cm²", "50,24 cm²", "25,12 cm²", "100,48 cm²"],
                "correct": 1,
                "explanation": "Bán kính r = 8 : 2 = 4 (cm). Diện tích hình tròn = 4 x 4 x 3,14 = 50,24 (cm²).",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Một hình tam giác vuông có hai cạnh góc vuông lần lượt là 6 cm và 8 cm. Diện tích của tam giác vuông đó là:",
                "choices": ["48 cm²", "24 cm²", "14 cm²", "28 cm²"],
                "correct": 1,
                "explanation": "Diện tích tam giác vuông bằng tích hai cạnh góc vuông chia 2: (6 x 8) : 2 = 24 (cm²).",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Một bánh xe đạp có bán kính 0,35 m. Khi bánh xe lăn được 1 vòng trên mặt đất thì xe đi được quãng đường dài là:",
                "choices": ["1,099 m", "2,198 m", "4,396 m", "0,7 m"],
                "correct": 1,
                "explanation": "Quãng đường khi lăn 1 vòng chính là chu vi bánh xe: 0,35 x 2 x 3,14 = 2,198 (m).",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Một hình thang có diện tích 60 cm² và chiều cao 6 cm. Tổng độ dài hai đáy của hình thang đó là:",
                "choices": ["10 cm", "20 cm", "30 cm", "15 cm"],
                "correct": 1,
                "explanation": "Tổng độ dài hai đáy = Diện tích x 2 : Chiều cao = 60 x 2 : 6 = 20 (cm).",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Đổi các đơn vị đo sau:\na) 12 m 8 dm = ... m\nb) 4 tấn 85 kg = ... tấn\nc) 25 m² 4 dm² = ... m²\nd) 3,2 km² = ... ha",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 8 dm = 0,8 m => 12 m 8 dm = 12,8 m\nb) 85 kg = 0,085 tấn => 4 tấn 85 kg = 4,085 tấn\nc) 4 dm² = 0,04 m² => 25 m² 4 dm² = 25,04 m²\nd) 1 km² = 100 ha => 3,2 km² = 320 ha\nĐáp số: a) 12,8 m; b) 4,085 tấn; c) 25,04 m²; d) 320 ha.",
                "answer": "a) 12,8 m; b) 4,085 tấn; c) 25,04 m²; d) 320 ha"
            },
            {
                "question": "**Bài 2:** Một hình tam giác có độ dài đáy là 15 cm, chiều cao bằng 2/3 độ dài đáy. Tính diện tích của hình tam giác đó.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Chiều cao của hình tam giác là:\n15 x 2/3 = 10 (cm)\nDiện tích của hình tam giác là:\n15 x 10 : 2 = 75 (cm²)\nĐáp số: 75 cm².",
                "answer": "75 cm²"
            },
            {
                "question": "**Bài 3:** Bánh xe của một ô tô có đường kính 0,8 m. Hỏi khi ô tô đi được quãng đường dài 1256 m thì bánh xe đã lăn được bao nhiêu vòng?",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Chu vi bánh xe ô tô là:\n0,8 x 3,14 = 2,512 (m)\nSố vòng bánh xe lăn được trên quãng đường đó là:\n1256 : 2,512 = 500 (vòng)\nĐáp số: 500 vòng.",
                "answer": "500 vòng"
            },
            {
                "question": "**Bài 4:** Một thửa ruộng hình thang có đáy lớn 50 m, đáy bé 30 m và chiều cao 25 m.\na) Tính diện tích thửa ruộng đó.\nb) Cứ 100 m² thu hoạch được 65 kg thóc. Hỏi trên cả thửa ruộng đó người ta thu hoạch được bao nhiêu tạ thóc?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Diện tích thửa ruộng hình thang là:\n(50 + 30) x 25 : 2 = 1000 (m²)\nb) Trên cả thửa ruộng thu hoạch được số ki-lô-gam thóc là:\n1000 : 100 x 65 = 650 (kg)\nĐổi: 650 kg = 6,5 tạ\nĐáp số: a) 1000 m²; b) 6,5 tạ thóc.",
                "answer": "a) 1000 m²; b) 6,5 tạ"
            },
            {
                "question": "**Bài 5:** Một chiếc bàn ăn hình chữ nhật có chiều dài 1,6 m và chiều rộng 0,9 m. Người ta dùng một tấm khăn trải bàn hình chữ nhật phủ lên mặt bàn, mép khăn rủ xuống đều nhau ở mỗi phía là 0,2 m. Tính diện tích của tấm khăn trải bàn đó.",
                "points": 1.5,
                "lineCount": 5,
                "solution": "Chiều dài tấm khăn trải bàn là:\n1,6 + 0,2 x 2 = 2 (m)\nChiều rộng tấm khăn trải bàn là:\n0,9 + 0,2 x 2 = 1,3 (m)\nDiện tích tấm khăn trải bàn là:\n2 x 1,3 = 2,6 (m²)\nĐáp số: 2,6 m².",
                "answer": "2,6 m²"
            },
            {
                "question": "**Bài 6:** Một tấm bìa hình vuông có chu vi 32 cm. Người ta cắt tấm bìa đó thành 4 hình vuông nhỏ bằng nhau. Tính tổng chu vi của 4 hình vuông nhỏ đó.",
                "points": 1.0,
                "lineCount": 5,
                "solution": "Cạnh của hình vuông ban đầu là:\n32 : 4 = 8 (cm)\nKhi chia thành 4 hình vuông nhỏ bằng nhau, cạnh của mỗi hình vuông nhỏ là:\n8 : 2 = 4 (cm)\nChu vi của một hình vuông nhỏ là:\n4 x 4 = 16 (cm)\nTổng chu vi của cả 4 hình vuông nhỏ là:\n16 x 4 = 64 (cm)\nĐáp số: 64 cm.",
                "answer": "64 cm"
            }
        ]
    }

    exams["th5_b27_test3"] = {
        "title": "ĐỀ KIỂM TRA BÀI 27 (ĐỀ 3): ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Số thập phân thích hợp điền vào chỗ chấm để 18 kg 50 g = ... kg là:",
                "choices": ["18,5", "18,05", "18,005", "1,85"],
                "correct": 1,
                "explanation": "1 kg = 1000 g nên 50 g = 0,05 kg. Do đó 18 kg 50 g = 18,05 kg.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Một hình chữ nhật có chiều dài 12,5 m và chiều rộng 8 m. Diện tích hình chữ nhật là:",
                "choices": ["100 m²", "20,5 m²", "41 m²", "96 m²"],
                "correct": 0,
                "explanation": "Diện tích hình chữ nhật = 12,5 x 8 = 100 (m²).",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Một hình tròn có chu vi 18,84 cm. Bán kính của hình tròn đó là:",
                "choices": ["6 cm", "3 cm", "2 cm", "4 cm"],
                "correct": 1,
                "explanation": "Bán kính r = 18,84 : 3,14 : 2 = 3 (cm).",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Một mảnh đất hình thang có tổng độ dài hai đáy là 45 m và chiều cao là 16 m. Diện tích mảnh đất đó là:",
                "choices": ["720 m²", "360 m²", "180 m²", "320 m²"],
                "correct": 1,
                "explanation": "Diện tích hình thang = 45 x 16 : 2 = 360 (m²).",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Đổi 0,75 ha sang mét vuông ta được kết quả là:",
                "choices": ["75 m²", "750 m²", "7 500 m²", "75 000 m²"],
                "correct": 2,
                "explanation": "1 ha = 10 000 m² nên 0,75 ha = 0,75 x 10 000 = 7 500 m².",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Diện tích tam giác vuông có hai cạnh góc vuông lần lượt là 4,5 dm và 6 dm là:",
                "choices": ["27 dm²", "13,5 dm²", "10,5 dm²", "21 dm²"],
                "correct": 1,
                "explanation": "Diện tích = 4,5 x 6 : 2 = 13,5 (dm²).",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Viết số thích hợp vào chỗ chấm:\na) 8 km 450 m = ... km\nb) 6 tấn 5 tạ = ... tấn\nc) 12 m² 35 cm² = ... m²\nd) 5,6 ha = ... m²",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 450 m = 0,45 km => 8 km 450 m = 8,45 km\nb) 5 tạ = 0,5 tấn => 6 tấn 5 tạ = 6,5 tấn\nc) 1 m² = 10 000 cm² nên 35 cm² = 0,0035 m² => 12 m² 35 cm² = 12,0035 m²\nd) 5,6 ha = 5,6 x 10 000 = 56 000 m²\nĐáp số: a) 8,45 km; b) 6,5 tấn; c) 12,0035 m²; d) 56 000 m².",
                "answer": "a) 8,45 km; b) 6,5 tấn; c) 12,0035 m²; d) 56 000 m²"
            },
            {
                "question": "**Bài 2:** Tính diện tích hình thang có đáy lớn 24 cm, đáy bé bằng 2/3 đáy lớn, chiều cao kém đáy bé 6 cm.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Độ dài đáy bé hình thang là:\n24 x 2/3 = 16 (cm)\nChiều cao hình thang là:\n16 - 6 = 10 (cm)\nDiện tích hình thang là:\n(24 + 16) x 10 : 2 = 200 (cm²)\nĐáp số: 200 cm².",
                "answer": "200 cm²"
            },
            {
                "question": "**Bài 3:** Người ta uốn một sợi dây thép thành một hình tròn có bán kính 7 cm. Tính độ dài của sợi dây thép đó.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Độ dài của sợi dây thép chính là chu vi hình tròn bán kính 7 cm:\n7 x 2 x 3,14 = 43,96 (cm)\nĐáp số: 43,96 cm.",
                "answer": "43,96 cm"
            },
            {
                "question": "**Bài 4:** Một mảnh đất hình chữ nhật có chiều dài 24 m và chiều rộng 15 m. Ở giữa mảnh đất, người ta đào một hồ nước hình tròn có bán kính 3 m, phần diện tích còn lại dùng để trồng hoa.\na) Tính diện tích mảnh đất hình chữ nhật.\nb) Tính diện tích phần đất dùng để trồng hoa.",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Diện tích mảnh đất hình chữ nhật là:\n24 x 15 = 360 (m²)\nb) Diện tích hồ nước hình tròn là:\n3 x 3 x 3,14 = 28,26 (m²)\nDiện tích phần đất dùng để trồng hoa là:\n360 - 28,26 = 331,74 (m²)\nĐáp số: a) 360 m²; b) 331,74 m².",
                "answer": "a) 360 m²; b) 331,74 m²"
            },
            {
                "question": "**Bài 5:** Một thửa ruộng hình thang có đáy lớn 60 m, đáy bé 40 m. Khi mở rộng đáy lớn thêm 10 m về một phía thì diện tích thửa ruộng tăng thêm 80 m². Tính diện tích thửa ruộng ban đầu.",
                "points": 1.5,
                "lineCount": 5,
                "solution": "Phần diện tích tăng thêm là hình tam giác có đáy 10 m và diện tích 80 m².\nChiều cao của thửa ruộng là:\n80 x 2 : 10 = 16 (m)\nDiện tích thửa ruộng ban đầu là:\n(60 + 40) x 16 : 2 = 800 (m²)\nĐáp số: 800 m².",
                "answer": "800 m²"
            },
            {
                "question": "**Bài 6:** Tính chu vi đường biên của hình tròn nằm nội tiếp bên trong một hình vuông cạnh 10 cm (hình tròn tiếp xúc với cả 4 cạnh của hình vuông).",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Vì hình tròn nội tiếp tiếp xúc với cả 4 cạnh hình vuông nên đường kính của hình tròn bằng đúng độ dài cạnh hình vuông d = 10 cm.\nChu vi hình tròn đó là:\n10 x 3,14 = 31,4 (cm)\nĐáp số: 31,4 cm.",
                "answer": "31,4 cm"
            }
        ]
    }

    return exams
