# -*- coding: utf-8 -*-
"""
HỆ THỐNG ĐỀ KIỂM TRA CUỐI HỌC KÌ 1 - TOÁN TIỂU HỌC (LỚP 5)
Bộ sách: KẾT NỐI TRI THỨC VỚI CUỘC SỐNG
Gồm 8 đề kiểm tra chuẩn hóa độc lập 100% (th5_ck1_de01 đến th5_ck1_de08).

Cấu trúc mỗi đề thi:
- Thời gian làm bài: 40 phút
- Thang điểm: 10.0 điểm
- Phần I (3.0 điểm): 6 câu Trắc nghiệm khách quan 4 lựa chọn (mỗi câu 0.5 điểm)
- Phần II (7.0 điểm): 6 bài Tự luận (Điểm số: 1.0, 1.0, 1.0, 1.5, 1.5, 1.0 điểm; có lineCount chừa dòng làm bài)
"""

def get_th5_ck1_exams():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 01 (th5_ck1_de01)
    # Ngữ cảnh: Thửa ruộng hình thang Đồng bằng sông Hồng, cấy lúa ST25
    # =========================================================================
    exams["th5_ck1_de01"] = {
        "id": "th5_ck1_de01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 1)",
        "grade": "5",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Trong số thập phân 35,462, chữ số 6 có giá trị là:",
                "options": [
                    "6",
                    "$\\frac{6}{10}$",
                    "$\\frac{6}{100}$",
                    "$\\frac{6}{1000}$"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Chữ số 6 ở hàng phần trăm nên có giá trị là $\\frac{6}{100}$ hay 0,06."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Nhân nhẩm phép tính $4,85 \\times 100$ ta được kết quả là:",
                "options": [
                    "48,5",
                    "485",
                    "4850",
                    "0,485"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Khi nhân một số thập phân với 100, ta chuyển dấu phẩy sang bên phải hai chữ số: $4,85 \\times 100 = 485$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Viết số đo $3\\text{ m}^2\\text{ } 45\\text{ dm}^2$ dưới dạng số thập phân có đơn vị mét vuông là:",
                "options": [
                    "3,45 $\\text{m}^2$",
                    "34,5 $\\text{m}^2$",
                    "3,045 $\\text{m}^2$",
                    "345 $\\text{m}^2$"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "$45\\text{ dm}^2 = \\frac{45}{100}\\text{ m}^2 = 0,45\\text{ m}^2$, vậy $3\\text{ m}^2\\text{ } 45\\text{ dm}^2 = 3,45\\text{ m}^2$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Một hình tam giác có độ dài đáy là 14 cm và chiều cao tương ứng là 8 cm. Diện tích của tam giác đó là:",
                "options": [
                    "112 $\\text{cm}^2$",
                    "56 $\\text{cm}^2$",
                    "28 $\\text{cm}^2$",
                    "22 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Diện tích tam giác là: $(14 \\times 8) : 2 = 56$ $\\text{cm}^2$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Tìm $x$ biết $x \\times 4 = 18,4$. Giá trị của $x$ là:",
                "options": [
                    "4,1",
                    "4,6",
                    "4,8",
                    "73,6"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "$x = 18,4 : 4 = 4,6$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Một hình tròn có bán kính $r = 5\\text{ cm}$. Chu vi của hình tròn đó là:",
                "options": [
                    "15,7 cm",
                    "31,4 cm",
                    "78,5 cm",
                    "62,8 cm"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chu vi hình tròn là: $C = 2 \\times r \\times 3,14 = 2 \\times 5 \\times 3,14 = 31,4$ cm."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $46,85 + 28,47$\nb) $82,5 - 36,78$\nc) $14,6 \\times 3,5$\nd) $79,5 : 5$",
                "solution": "Bài giải:\na) Đặt tính cộng:\n   46,85 + 28,47 = 75,32\nb) Đặt tính trừ:\n   82,50 - 36,78 = 45,72\nc) Đặt tính nhân:\n   14,6 × 3,5 = 51,10 = 51,1\nd) Đặt tính chia:\n   79,5 : 5 = 15,9\nĐáp số: a) 75,32; b) 45,72; c) 51,1; d) 15,9",
                "answer": "a) 75,32; b) 45,72; c) 51,1; d) 15,9",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$4,75 \\times 8,3 + 4,75 \\times 1,7$",
                "solution": "Bài giải:\n$4,75 \\times 8,3 + 4,75 \\times 1,7 = 4,75 \\times (8,3 + 1,7)$\n$= 4,75 \\times 10$\n$= 47,5$\nĐáp số: 47,5",
                "answer": "47,5",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x - 12,4 = 18,6 : 3$",
                "solution": "Bài giải:\n$x - 12,4 = 18,6 : 3$\n$x - 12,4 = 6,2$\n$x = 6,2 + 12,4$\n$x = 18,6$\nĐáp số: $x = 18,6$",
                "answer": "x = 18,6",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Một cửa hàng hoa quả nhập về 125 kg táo với giá 32 000 đồng một ki-lô-gam. Cửa hàng đã bán hết toàn bộ số táo đó với giá 40 000 đồng một ki-lô-gam. Hỏi sau khi bán hết số táo, cửa hàng đã thu được bao nhiêu tiền lãi?",
                "solution": "Bài giải:\nSố tiền mua táo (tiền vốn) là:\n$125 \\times 32 000 = 4 000 000$ (đồng)\nSố tiền bán táo thu về là:\n$125 \\times 40 000 = 5 000 000$ (đồng)\nSố tiền lãi cửa hàng thu được là:\n$5 000 000 - 4 000 000 = 1 000 000$ (đồng)\n(Cách khác: Mỗi ki-lô-gam táo lãi: $40 000 - 32 000 = 8 000$ đồng. Tiền lãi là: $125 \\times 8 000 = 1 000 000$ đồng).\nĐáp số: 1 000 000 đồng.",
                "answer": "1 000 000 đồng",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một thửa ruộng hình thang có đáy lớn 45 m, đáy bé bằng $\\frac{2}{3}$ đáy lớn, chiều cao là 24 m.\na) Tính diện tích thửa ruộng hình thang đó.\nb) Biết rằng cứ $100\\text{ m}^2$ thu hoạch được 65 kg thóc. Hỏi trên cả thửa ruộng người ta thu hoạch được bao nhiêu tạ thóc?",
                "solution": "Bài giải:\na) Đáy bé của thửa ruộng hình thang là:\n$45 \\times \\frac{2}{3} = 30$ (m)\nDiện tích của thửa ruộng hình thang là:\n$(45 + 30) \\times 24 : 2 = 900$ ($\\text{m}^2$)\nb) Số ki-lô-gam thóc thu hoạch được trên cả thửa ruộng là:\n$900 : 100 \\times 65 = 585$ (kg)\nĐổi $585\\text{ kg} = 5,85\\text{ tạ}$\nĐáp số: a) 900 $\\text{m}^2$; b) 5,85 tạ thóc.",
                "answer": "a) 900 m²; b) 5,85 tạ thóc",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tính nhanh giá trị của biểu thức sau:\n$M = 0,2 \\times 45,8 \\times 5 + 0,25 \\times 54,2 \\times 4$",
                "solution": "Bài giải:\nÁp dụng tính chất giao hoán và kết hợp của phép nhân:\n$M = (0,2 \\times 5) \\times 45,8 + (0,25 \\times 4) \\times 54,2$\n$M = 1 \\times 45,8 + 1 \\times 54,2$\n$M = 45,8 + 54,2$\n$M = 100$\nĐáp số: $M = 100$",
                "answer": "M = 100",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 02 (th5_ck1_de02)
    # Ngữ cảnh: Công viên bách thảo, bồn hoa hình tròn và đường đi
    # =========================================================================
    exams["th5_ck1_de02"] = {
        "id": "th5_ck1_de02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 2)",
        "grade": "5",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Số thập phân 0,075 được đọc là:",
                "options": [
                    "Không phẩy bảy mươi lăm",
                    "Không phẩy không trăm bảy mươi lăm",
                    "Không phẩy không bảy lăm",
                    "Không phẩy bảy lăm"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Số 0,075 đọc chuẩn là: 'Không phẩy không trăm bảy mươi lăm'."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Chia nhẩm phép tính $36,8 : 100$ ta được kết quả là:",
                "options": [
                    "3,68",
                    "0,368",
                    "0,0368",
                    "368"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Khi chia số thập phân cho 100, ta chuyển dấu phẩy sang bên trái hai chữ số: $36,8 : 100 = 0,368$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Viết số đo $5\\text{ tấn } 80\\text{ kg}$ dưới dạng số thập phân có đơn vị tấn là:",
                "options": [
                    "5,8 tấn",
                    "5,08 tấn",
                    "5,008 tấn",
                    "50,8 tấn"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "$80\\text{ kg} = \\frac{80}{1000}\\text{ tấn} = 0,08\\text{ tấn}$, vậy kết quả là 5,08 tấn."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Diện tích của một hình tròn có bán kính $r = 4\\text{ cm}$ là:",
                "options": [
                    "12,56 $\\text{cm}^2$",
                    "25,12 $\\text{cm}^2$",
                    "50,24 $\\text{cm}^2$",
                    "100,48 $\\text{cm}^2$"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Diện tích hình tròn là: $S = r \\times r \\times 3,14 = 4 \\times 4 \\times 3,14 = 50,24$ $\\text{cm}^2$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Một ô tô chạy trong 3 giờ được quãng đường 136,5 km. Vận tốc trung bình của ô tô đó là:",
                "options": [
                    "45,5 km/h",
                    "45 km/h",
                    "46,5 km/h",
                    "42,5 km/h"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Vận tốc là: $136,5 : 3 = 45,5$ km/h."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Một hình thang có đáy lớn 12 cm, đáy bé 8 cm và chiều cao 5 cm. Diện tích của hình thang đó là:",
                "options": [
                    "100 $\\text{cm}^2$",
                    "50 $\\text{cm}^2$",
                    "40 $\\text{cm}^2$",
                    "60 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Diện tích hình thang là: $(12 + 8) \\times 5 : 2 = 50$ $\\text{cm}^2$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $63,74 + 38,59$\nb) $91,2 - 45,68$\nc) $28,4 \\times 2,6$\nd) $87,5 : 25$",
                "solution": "Bài giải:\na) Đặt tính cộng:\n   63,74 + 38,59 = 102,33\nb) Đặt tính trừ:\n   91,20 - 45,68 = 45,52\nc) Đặt tính nhân:\n   28,4 × 2,6 = 73,84\nd) Đặt tính chia:\n   87,5 : 25 = 3,5\nĐáp số: a) 102,33; b) 45,52; c) 73,84; d) 3,5",
                "answer": "a) 102,33; b) 45,52; c) 73,84; d) 3,5",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$12,5 \\times 6,4 \\times 8$",
                "solution": "Bài giải:\n$12,5 \\times 6,4 \\times 8 = (12,5 \\times 8) \\times 6,4$\n$= 100 \\times 6,4$\n$= 640$\nĐáp số: 640",
                "answer": "640",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x \\times 2,5 = 31,5 - 6,5$",
                "solution": "Bài giải:\n$x \\times 2,5 = 31,5 - 6,5$\n$x \\times 2,5 = 25$\n$x = 25 : 2,5$\n$x = 10$\nĐáp số: $x = 10$",
                "answer": "x = 10",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Một đội công nhân sửa đường trong hai tuần. Tuần thứ nhất đội sửa được 185,5 m đường. Tuần thứ hai đội sửa được nhiều hơn tuần thứ nhất 24,8 m đường. Hỏi trung bình mỗi tuần đội công nhân đó sửa được bao nhiêu mét đường?",
                "solution": "Bài giải:\nSố mét đường đội công nhân sửa được trong tuần thứ hai là:\n$185,5 + 24,8 = 210,3$ (m)\nTổng số mét đường sửa được trong cả hai tuần là:\n$185,5 + 210,3 = 395,8$ (m)\nTrung bình mỗi tuần đội sửa được số mét đường là:\n$395,8 : 2 = 197,9$ (m)\nĐáp số: 197,9 m đường.",
                "answer": "197,9 m",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Ở giữa một công viên, người ta xây một bồn hoa hình tròn có đường kính $d = 8\\text{ m}$.\na) Tính chu vi và diện tích bồn hoa hình tròn đó.\nb) Người ta trồng hoa hồng trên toàn bộ bồn hoa, biết chi phí mua cây giống và công trồng là 80 000 đồng cho mỗi mét vuông. Tính tổng chi phí để trồng hoa trên bồn hoa đó.",
                "solution": "Bài giải:\na) Bán kính của bồn hoa hình tròn là:\n$8 : 2 = 4$ (m)\nChu vi bồn hoa hình tròn là:\n$8 \\times 3,14 = 25,12$ (m)\nDiện tích bồn hoa hình tròn là:\n$4 \\times 4 \\times 3,14 = 50,24$ ($\\text{m}^2$)\nb) Tổng chi phí để trồng hoa là:\n$50,24 \\times 80 000 = 4 019 200$ (đồng)\nĐáp số: a) Chu vi: 25,12 m; Diện tích: 50,24 $\\text{m}^2$; b) 4 019 200 đồng.",
                "answer": "a) Chu vi: 25,12 m, S: 50,24 m²; b) 4 019 200 đồng",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tính nhanh giá trị biểu thức:\n$N = 1,25 \\times 17,4 \\times 8 - 2,5 \\times 7,4 \\times 4$",
                "solution": "Bài giải:\nTa có: $1,25 \\times 8 = 10$ và $2,5 \\times 4 = 10$.\nBiểu thức viết lại thành:\n$N = (1,25 \\times 8) \\times 17,4 - (2,5 \\times 4) \\times 7,4$\n$N = 10 \\times 17,4 - 10 \\times 7,4$\n$N = 174 - 74$\n$N = 100$\nĐáp số: $N = 100$",
                "answer": "N = 100",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 03 (th5_ck1_de03)
    # Ngữ cảnh: Nông trại bò sữa Ba Vì, đồng cỏ voi hình tam giác
    # =========================================================================
    exams["th5_ck1_de03"] = {
        "id": "th5_ck1_de03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 3)",
        "grade": "5",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Trong số thập phân 194,385 chữ số 8 thuộc hàng nào?",
                "options": [
                    "Hàng phần mười",
                    "Hàng phần trăm",
                    "Hàng phần nghìn",
                    "Hàng chục"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chữ số 8 đứng ở vị trí thứ hai sau dấu phẩy nên thuộc hàng phần trăm."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Kết quả của phép nhân nhẩm $0,45 \\times 0,01$ là:",
                "options": [
                    "0,045",
                    "0,0045",
                    "0,45",
                    "0,00045"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Nhân với 0,01 là chuyển dấu phẩy sang bên trái hai chữ số: $0,45 \\times 0,01 = 0,0045$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Viết số đo $7\\text{ km } 250\\text{ m}$ dưới dạng số thập phân có đơn vị ki-lô-mét là:",
                "options": [
                    "7,25 km",
                    "7,025 km",
                    "72,5 km",
                    "7,250 km"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "$250\\text{ m} = \\frac{250}{1000}\\text{ km} = 0,25\\text{ km}$, do đó $7\\text{ km } 250\\text{ m} = 7,25\\text{ km}$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Một hình tam giác có diện tích là 36 $\\text{cm}^2$ và độ dài đáy là 9 cm. Chiều cao của tam giác đó là:",
                "options": [
                    "4 cm",
                    "8 cm",
                    "6 cm",
                    "12 cm"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chiều cao tam giác là: $h = 2 \\times S : a = 2 \\times 36 : 9 = 8$ cm."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Thương của phép chia $21,35 : 7$ là:",
                "options": [
                    "3,5",
                    "3,05",
                    "0,35",
                    "30,5"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Thực hiện phép chia: $21,35 : 7 = 3,05$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Chu vi của một hình tròn có bán kính $r = 2,5\\text{ cm}$ là:",
                "options": [
                    "7,85 cm",
                    "15,7 cm",
                    "19,625 cm",
                    "31,4 cm"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chu vi hình tròn là: $C = 2 \\times 2,5 \\times 3,14 = 5 \\times 3,14 = 15,7$ cm."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $57,84 + 36,79$\nb) $120,5 - 48,65$\nc) $32,5 \\times 4,2$\nd) $93,6 : 18$",
                "solution": "Bài giải:\na) Đặt tính cộng:\n   57,84 + 36,79 = 94,63\nb) Đặt tính trừ:\n   120,50 - 48,65 = 71,85\nc) Đặt tính nhân:\n   32,5 × 4,2 = 136,50 = 136,5\nd) Đặt tính chia:\n   93,6 : 18 = 5,2\nĐáp số: a) 94,63; b) 71,85; c) 136,5; d) 5,2",
                "answer": "a) 94,63; b) 71,85; c) 136,5; d) 5,2",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$8,64 \\times 15,7 - 8,64 \\times 5,7$",
                "solution": "Bài giải:\n$8,64 \\times 15,7 - 8,64 \\times 5,7 = 8,64 \\times (15,7 - 5,7)$\n$= 8,64 \\times 10$\n$= 86,4$\nĐáp số: 86,4",
                "answer": "86,4",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x : 4,2 = 6,5 + 3,5$",
                "solution": "Bài giải:\n$x : 4,2 = 6,5 + 3,5$\n$x : 4,2 = 10$\n$x = 10 \\times 4,2$\n$x = 42$\nĐáp số: $x = 42$",
                "answer": "x = 42",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Nông trại nuôi bò sữa có hai chuồng bò. Chuồng thứ nhất thu được 215,6 lít sữa mỗi ngày. Chuồng thứ hai thu được ít hơn chuồng thứ nhất 18,4 lít sữa mỗi ngày.\na) Hỏi cả hai chuồng thu được bao nhiêu lít sữa mỗi ngày?\nb) Mỗi lít sữa tươi bán được với giá 15 000 đồng. Hỏi mỗi ngày nông trại thu được bao nhiêu tiền từ việc bán sữa của cả hai chuồng?",
                "solution": "Bài giải:\na) Số lít sữa chuồng thứ hai thu được mỗi ngày là:\n$215,6 - 18,4 = 197,2$ (lít)\nSố lít sữa cả hai chuồng thu được mỗi ngày là:\n$215,6 + 197,2 = 412,8$ (lít)\nb) Số tiền nông trại thu được từ bán sữa mỗi ngày là:\n$412,8 \\times 15 000 = 6 192 000$ (đồng)\nĐáp số: a) 412,8 lít sữa; b) 6 192 000 đồng.",
                "answer": "a) 412,8 lít; b) 6 192 000 đồng",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một mảnh đất hình tam giác có độ dài đáy là 36 m và chiều cao bằng $\\frac{3}{4}$ độ dài đáy.\na) Tính diện tích mảnh đất hình tam giác đó.\nb) Người ta dùng $\\frac{2}{3}$ diện tích mảnh đất để trồng cỏ voi nuôi bò, phần còn lại trồng rau sạch. Tính diện tích phần đất trồng rau sạch.",
                "solution": "Bài giải:\na) Chiều cao mảnh đất hình tam giác là:\n$36 \\times \\frac{3}{4} = 27$ (m)\nDiện tích mảnh đất hình tam giác là:\n$36 \\times 27 : 2 = 486$ ($\\text{m}^2$)\nb) Diện tích phần đất trồng cỏ voi là:\n$486 \\times \\frac{2}{3} = 324$ ($\\text{m}^2$)\nDiện tích phần đất trồng rau sạch là:\n$486 - 324 = 162$ ($\\text{m}^2$)\n(Cách khác: Phân số chỉ diện tích trồng rau sạch là $1 - \\frac{2}{3} = \\frac{1}{3}$. Diện tích trồng rau là: $486 \\times \\frac{1}{3} = 162$ $\\text{m}^2$).\nĐáp số: a) 486 $\\text{m}^2$; b) 162 $\\text{m}^2$.",
                "answer": "a) 486 m²; b) 162 m²",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Cho một hình vuông $ABCD$ có cạnh dài 10 cm. Ở bên trong hình vuông có một hình tròn nội tiếp tiếp xúc với bốn cạnh của hình vuông (đường kính hình tròn bằng cạnh hình vuông, tức $d = 10\\text{ cm}$). Tính diện tích phần còn lại của hình vuông nằm ngoài hình tròn.",
                "solution": "Bài giải:\nDiện tích hình vuông $ABCD$ là:\n$10 \\times 10 = 100$ ($\\text{cm}^2$)\nBán kính của hình tròn nội tiếp là:\n$10 : 2 = 5$ (cm)\nDiện tích của hình tròn là:\n$5 \\times 5 \\times 3,14 = 78,5$ ($\\text{cm}^2$)\nDiện tích phần còn lại của hình vuông là:\n$100 - 78,5 = 21,5$ ($\\text{cm}^2$)\nĐáp số: 21,5 $\\text{cm}^2$.",
                "answer": "21,5 cm²",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 04 (th5_ck1_de04)
    # Ngữ cảnh: Xưởng chế biến nông sản hạt điều xuất khẩu Bình Phước
    # =========================================================================
    exams["th5_ck1_de04"] = {
        "id": "th5_ck1_de04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 4)",
        "grade": "5",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Số thập phân thích hợp để điền vào chỗ chấm: $6\\text{ m } 8\\text{ cm} = ..........\\text{ m}$ là:",
                "options": [
                    "6,8 m",
                    "6,08 m",
                    "6,008 m",
                    "68 m"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "$8\\text{ cm} = \\frac{8}{100}\\text{ m} = 0,08\\text{ m}$, do đó $6\\text{ m } 8\\text{ cm} = 6,08\\text{ m}$."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Tích của $3,14 \\times 10$ là:",
                "options": [
                    "0,314",
                    "31,4",
                    "314",
                    "3,140"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Nhân với 10 thì dời dấu phẩy sang phải một chữ số: $3,14 \\times 10 = 31,4$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Diện tích hình thang có hai đáy là 15 cm và 9 cm, chiều cao 6 cm là:",
                "options": [
                    "144 $\\text{cm}^2$",
                    "72 $\\text{cm}^2$",
                    "60 $\\text{cm}^2$",
                    "36 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Diện tích hình thang là: $(15 + 9) \\times 6 : 2 = 24 \\times 6 : 2 = 72$ $\\text{cm}^2$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Kết quả của phép chia nhẩm $4,8 : 0,1$ là:",
                "options": [
                    "0,48",
                    "48",
                    "480",
                    "4,8"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chia cho 0,1 bằng nhân với 10: $4,8 : 0,1 = 4,8 \\times 10 = 48$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Một hình tròn có chu vi $C = 18,84\\text{ cm}$. Bán kính của hình tròn đó là:",
                "options": [
                    "3 cm",
                    "6 cm",
                    "9 cm",
                    "1,5 cm"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Đường kính là $18,84 : 3,14 = 6$ cm. Bán kính là $6 : 2 = 3$ cm."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Giá trị của biểu thức $5,6 + 4,4 \\times 2$ là:",
                "options": [
                    "20",
                    "14,4",
                    "15,6",
                    "13,2"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Thực hiện nhân trước: $4,4 \\times 2 = 8,8$, sau đó cộng: $5,6 + 8,8 = 14,4$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $78,65 + 43,8$\nb) $105,2 - 68,45$\nc) $45,8 \\times 3,4$\nd) $108,5 : 35$",
                "solution": "Bài giải:\na) Đặt tính cộng:\n   78,65 + 43,80 = 122,45\nb) Đặt tính trừ:\n   105,20 - 68,45 = 36,75\nc) Đặt tính nhân:\n   45,8 × 3,4 = 155,72\nd) Đặt tính chia:\n   108,5 : 35 = 3,1\nĐáp số: a) 122,45; b) 36,75; c) 155,72; d) 3,1",
                "answer": "a) 122,45; b) 36,75; c) 155,72; d) 3,1",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$3,6 \\times 4,5 + 3,6 \\times 5,5$",
                "solution": "Bài giải:\n$3,6 \\times 4,5 + 3,6 \\times 5,5 = 3,6 \\times (4,5 + 5,5)$\n$= 3,6 \\times 10$\n$= 36$\nĐáp số: 36",
                "answer": "36",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$7,8 + x = 24,5 : 2$",
                "solution": "Bài giải:\n$7,8 + x = 24,5 : 2$\n$7,8 + x = 12,25$\n$x = 12,25 - 7,8$\n$x = 4,45$\nĐáp số: $x = 4,45$",
                "answer": "x = 4,45",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Xưởng chế biến nông sản đóng gói được 35 bao hạt điều loại lớn, mỗi bao nặng 45,5 kg và 40 bao hạt điều loại nhỏ, mỗi bao nặng 25,5 kg.\na) Hỏi xưởng đã đóng gói được tất cả bao nhiêu ki-lô-gam hạt điều?\nb) Đổi số ki-lô-gam hạt điều đó ra đơn vị tấn.",
                "solution": "Bài giải:\na) Khối lượng hạt điều trong các bao loại lớn là:\n$35 \\times 45,5 = 1592,5$ (kg)\nKhối lượng hạt điều trong các bao loại nhỏ là:\n$40 \\times 25,5 = 1020$ (kg)\nTổng khối lượng hạt điều xưởng đóng gói được là:\n$1592,5 + 1020 = 2612,5$ (kg)\nb) Đổi: $2612,5\\text{ kg} = 2,6125\\text{ tấn}$\nĐáp số: a) 2612,5 kg; b) 2,6125 tấn.",
                "answer": "a) 2612,5 kg; b) 2,6125 tấn",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một thửa đất hình thang có đáy lớn 38 m, đáy bé 22 m và chiều cao bằng trung bình cộng của hai đáy.\na) Tính diện tích thửa đất hình thang đó.\nb) Người ta làm hàng rào bao quanh thửa đất (để chừa cổng ra vào rộng 3 m). Biết tổng độ dài hai cạnh bên của thửa đất hình thang là 34 m. Hỏi chiều dài hàng rào cần làm là bao nhiêu mét?",
                "solution": "Bài giải:\na) Chiều cao của thửa đất hình thang là:\n$(38 + 22) : 2 = 30$ (m)\nDiện tích thửa đất hình thang là:\n$(38 + 22) \\times 30 : 2 = 900$ ($\\text{m}^2$)\nb) Chu vi của thửa đất hình thang là:\n$38 + 22 + 34 = 94$ (m)\nChiều dài hàng rào cần làm là:\n$94 - 3 = 91$ (m)\nĐáp số: a) 900 $\\text{m}^2$; b) 91 m.",
                "answer": "a) 900 m²; b) 91 m",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tính giá trị của biểu thức sau một cách hợp lý:\n$P = \\frac{1,2 \\times 4,5 + 2,4 \\times 2,75}{0,6 \\times 32}$",
                "solution": "Bài giải:\nXét tử số:\n$1,2 \\times 4,5 + 2,4 \\times 2,75 = 1,2 \\times 4,5 + 1,2 \\times 2 \\times 2,75$\n$= 1,2 \\times 4,5 + 1,2 \\times 5,5$\n$= 1,2 \\times (4,5 + 5,5)$\n$= 1,2 \\times 10 = 12$\nXét mẫu số:\n$0,6 \\times 32 = 19,2$\nGiá trị biểu thức là:\n$P = 12 : 19,2 = 120 : 192 = \\frac{5}{8} = 0,625$\nĐáp số: $P = 0,625$ (hoặc $\\frac{5}{8}$).",
                "answer": "P = 0,625 (hoặc 5/8)",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 05 (th5_ck1_de05)
    # Ngữ cảnh: Vườn sinh thái cây ăn trái Đồng Tháp Mười, bưởi da xanh và xoài
    # =========================================================================
    exams["th5_ck1_de05"] = {
        "id": "th5_ck1_de05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 5)",
        "grade": "5",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Trong số thập phân 82,149 chữ số 4 có giá trị là:",
                "options": [
                    "$\\frac{4}{10}$",
                    "$\\frac{4}{100}$",
                    "$\\frac{4}{1000}$",
                    "4"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chữ số 4 nằm ở vị trí thứ hai sau dấu phẩy nên có giá trị là $\\frac{4}{100}$."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Nhân nhẩm $0,86 \\times 0,1$ ta được kết quả là:",
                "options": [
                    "8,6",
                    "0,086",
                    "0,0086",
                    "0,86"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Nhân với 0,1 bằng dịch dấu phẩy sang trái một hàng: $0,86 \\times 0,1 = 0,086$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Đổi $4\\text{ ha } 500\\text{ m}^2 = ..........\\text{ ha}$ ta được số thập phân là:",
                "options": [
                    "4,5 ha",
                    "4,05 ha",
                    "4,005 ha",
                    "45 ha"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Vì $1\\text{ ha} = 10 000\\text{ m}^2$ nên $500\\text{ m}^2 = \\frac{500}{10 000}\\text{ ha} = 0,05\\text{ ha}$. Vậy kết quả là 4,05 ha."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Một hình tam giác có độ dài đáy 16 cm và chiều cao tương ứng 12 cm. Diện tích của hình tam giác đó là:",
                "options": [
                    "192 $\\text{cm}^2$",
                    "96 $\\text{cm}^2$",
                    "48 $\\text{cm}^2$",
                    "14 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Diện tích tam giác là: $(16 \\times 12) : 2 = 96$ $\\text{cm}^2$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Kết quả của phép chia $12,6 : 0,5$ là:",
                "options": [
                    "6,3",
                    "25,2",
                    "2,52",
                    "63"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chia cho 0,5 bằng nhân với 2: $12,6 \\times 2 = 25,2$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Diện tích của một hình tròn có bán kính $r = 3\\text{ cm}$ là:",
                "options": [
                    "9,42 $\\text{cm}^2$",
                    "18,84 $\\text{cm}^2$",
                    "28,26 $\\text{cm}^2$",
                    "56,52 $\\text{cm}^2$"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Diện tích hình tròn: $S = 3 \\times 3 \\times 3,14 = 9 \\times 3,14 = 28,26$ $\\text{cm}^2$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $84,36 + 47,85$\nb) $135,4 - 58,76$\nc) $38,5 \\times 2,4$\nd) $75,6 : 12$",
                "solution": "Bài giải:\na) Đặt tính cộng:\n   84,36 + 47,85 = 132,21\nb) Đặt tính trừ:\n   135,40 - 58,76 = 76,64\nc) Đặt tính nhân:\n   38,5 × 2,4 = 92,40 = 92,4\nd) Đặt tính chia:\n   75,6 : 12 = 6,3\nĐáp số: a) 132,21; b) 76,64; c) 92,4; d) 6,3",
                "answer": "a) 132,21; b) 76,64; c) 92,4; d) 6,3",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$2,5 \\times 7,8 \\times 4$",
                "solution": "Bài giải:\n$2,5 \\times 7,8 \\times 4 = (2,5 \\times 4) \\times 7,8$\n$= 10 \\times 7,8$\n$= 78$\nĐáp số: 78",
                "answer": "78",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x \\times 3,6 = 18,9 + 9,9$",
                "solution": "Bài giải:\n$x \\times 3,6 = 18,9 + 9,9$\n$x \\times 3,6 = 28,8$\n$x = 28,8 : 3,6$\n$x = 8$\nĐáp số: $x = 8$",
                "answer": "x = 8",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Vườn sinh thái thu hoạch được hai đợt cam. Đợt thứ nhất thu hoạch được 345,5 kg cam. Đợt thứ hai thu hoạch được gấp 1,4 lần đợt thứ nhất.\na) Hỏi cả hai đợt vườn thu hoạch được bao nhiêu ki-lô-gam cam?\nb) Người ta đóng toàn bộ số cam trên vào các thùng, mỗi thùng chứa 15 kg. Hỏi đóng được nhiều nhất bao nhiêu thùng và còn thừa bao nhiêu ki-lô-gam cam?",
                "solution": "Bài giải:\na) Số ki-lô-gam cam thu hoạch được ở đợt thứ hai là:\n$345,5 \\times 1,4 = 483,7$ (kg)\nSố ki-lô-gam cam cả hai đợt thu hoạch được là:\n$345,5 + 483,7 = 829,2$ (kg)\nb) Thực hiện phép chia có dư:\n$829,2 : 15 = 55$ (dư 4,2)\nVậy đóng được nhiều nhất 55 thùng và còn thừa 4,2 kg cam.\nĐáp số: a) 829,2 kg cam; b) 55 thùng và thừa 4,2 kg cam.",
                "answer": "a) 829,2 kg; b) 55 thùng, thừa 4,2 kg",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một bồn hoa hình tam giác vuông có hai cạnh góc vuông dài 15 m và 20 m.\na) Tính diện tích bồn hoa hình tam giác vuông đó.\nb) Người ta xây gờ chắn viền xung quanh bồn hoa. Biết cạnh còn lại (cạnh dài nhất) của tam giác vuông dài 25 m. Tính chu vi của bồn hoa đó.",
                "solution": "Bài giải:\na) Diện tích của bồn hoa hình tam giác vuông là:\n$(15 \\times 20) : 2 = 150$ ($\\text{m}^2$)\nb) Chu vi của bồn hoa là:\n$15 + 20 + 25 = 60$ (m)\nĐáp số: a) 150 $\\text{m}^2$; b) 60 m.",
                "answer": "a) 150 m²; b) 60 m",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Cho dãy số thập phân cách đều: $1,1;\\ 2,2;\\ 3,3;\\ 4,4;\\ ...;\\ 9,9$.\na) Dãy số trên có tất cả bao nhiêu số hạng?\nb) Tính tổng của toàn bộ các số hạng trong dãy số trên.",
                "solution": "Bài giải:\na) Khoảng cách giữa hai số liên tiếp là:\n$2,2 - 1,1 = 1,1$\nSố các số hạng của dãy là:\n$(9,9 - 1,1) : 1,1 + 1 = 8,8 : 1,1 + 1 = 8 + 1 = 9$ (số hạng)\nb) Tổng của dãy số là:\n$(1,1 + 9,9) \\times 9 : 2 = 11 \\times 9 : 2 = 99 : 2 = 49,5$\nĐáp số: a) 9 số hạng; b) 49,5.",
                "answer": "a) 9 số hạng; b) 49,5",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 06 (th5_ck1_de06)
    # Ngữ cảnh: Siêu thị tiêu dùng xanh và nông sản hữu cơ
    # =========================================================================
    exams["th5_ck1_de06"] = {
        "id": "th5_ck1_de06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 6)",
        "grade": "5",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Trong số thập phân 47,891, chữ số 9 có giá trị là:",
                "options": [
                    "0,9",
                    "0,09",
                    "0,009",
                    "9"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chữ số 9 ở hàng phần trăm nên có giá trị là 0,09."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Chia nhẩm $54,7 : 10$ ta được kết quả là:",
                "options": [
                    "547",
                    "5,47",
                    "0,547",
                    "54,70"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Khi chia một số cho 10, dời dấu phẩy sang trái 1 chữ số: $54,7 : 10 = 5,47$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Đổi $8\\text{ m}^2\\text{ } 6\\text{ dm}^2$ sang số thập phân có đơn vị mét vuông là:",
                "options": [
                    "8,6 $\\text{m}^2$",
                    "8,06 $\\text{m}^2$",
                    "8,006 $\\text{m}^2$",
                    "86 $\\text{m}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "$6\\text{ dm}^2 = 0,06\\text{ m}^2$, do đó $8\\text{ m}^2\\text{ } 6\\text{ dm}^2 = 8,06\\text{ m}^2$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Chu vi của một hình tròn có đường kính $d = 6\\text{ cm}$ là:",
                "options": [
                    "9,42 cm",
                    "18,84 cm",
                    "28,26 cm",
                    "37,68 cm"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chu vi hình tròn: $C = d \\times 3,14 = 6 \\times 3,14 = 18,84$ cm."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Một lớp học có 40 học sinh, trong đó có 18 bạn nữ. Tỉ số phần trăm của số học sinh nữ và số học sinh cả lớp là:",
                "options": [
                    "45%",
                    "40%",
                    "36%",
                    "55%"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Tỉ số phần trăm là: $18 : 40 = 0,45 = 45\\%$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Một hình tam giác có độ dài đáy là 20 cm, chiều cao bằng một nửa độ dài đáy. Diện tích của tam giác đó là:",
                "options": [
                    "200 $\\text{cm}^2$",
                    "100 $\\text{cm}^2$",
                    "50 $\\text{cm}^2$",
                    "150 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chiều cao là $20 : 2 = 10$ cm. Diện tích tam giác: $(20 \\times 10) : 2 = 100$ $\\text{cm}^2$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $92,45 + 38,76$\nb) $142,3 - 75,84$\nc) $26,5 \\times 4,8$\nd) $94,5 : 15$",
                "solution": "Bài giải:\na) Đặt tính cộng:\n   92,45 + 38,76 = 131,21\nb) Đặt tính trừ:\n   142,30 - 75,84 = 66,46\nc) Đặt tính nhân:\n   26,5 × 4,8 = 127,20 = 127,2\nd) Đặt tính chia:\n   94,5 : 15 = 6,3\nĐáp số: a) 131,21; b) 66,46; c) 127,2; d) 6,3",
                "answer": "a) 131,21; b) 66,46; c) 127,2; d) 6,3",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$6,78 \\times 99 + 6,78$",
                "solution": "Bài giải:\n$6,78 \\times 99 + 6,78 = 6,78 \\times (99 + 1)$\n$= 6,78 \\times 100$\n$= 678$\nĐáp số: 678",
                "answer": "678",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x - 14,5 = 32,4 : 4$",
                "solution": "Bài giải:\n$x - 14,5 = 32,4 : 4$\n$x - 14,5 = 8,1$\n$x = 8,1 + 14,5$\n$x = 22,6$\nĐáp số: $x = 22,6$",
                "answer": "x = 22,6",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Mẹ đi siêu thị mua 3,5 kg khoai tây với giá 24 000 đồng một ki-lô-gam và 2,5 kg cà chua với giá 28 000 đồng một ki-lô-gam. Mẹ đưa cho cô nhân viên thu ngân tờ tiền 200 000 đồng. Hỏi cô nhân viên phải trả lại mẹ bao nhiêu tiền thừa?",
                "solution": "Bài giải:\nSố tiền mẹ mua khoai tây là:\n$3,5 \\times 24 000 = 84 000$ (đồng)\nSố tiền mẹ mua cà chua là:\n$2,5 \\times 28 000 = 70 000$ (đồng)\nTổng số tiền mẹ mua rau củ là:\n$84 000 + 70 000 = 154 000$ (đồng)\nSố tiền cô thu ngân phải trả lại mẹ là:\n$200 000 - 154 000 = 46 000$ (đồng)\nĐáp số: 46 000 đồng.",
                "answer": "46 000 đồng",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một mảnh đất hình thang có đáy bé 26 m, đáy lớn gấp đôi đáy bé, chiều cao là 18 m.\na) Tính diện tích của mảnh đất hình thang đó.\nb) Người ta dùng 40% diện tích mảnh đất để làm nhà ở, phần diện tích còn lại làm sân và trồng hoa cây cảnh. Tính diện tích phần đất làm sân và trồng hoa cây cảnh.",
                "solution": "Bài giải:\na) Độ dài đáy lớn của mảnh đất là:\n$26 \\times 2 = 52$ (m)\nDiện tích mảnh đất hình thang là:\n$(52 + 26) \\times 18 : 2 = 702$ ($\\text{m}^2$)\nb) Diện tích đất dùng để làm nhà ở là:\n$702 \\times 40 : 100 = 280,8$ ($\\text{m}^2$)\nDiện tích đất làm sân và trồng hoa cây cảnh là:\n$702 - 280,8 = 421,2$ ($\\text{m}^2$)\n(Cách khác: Phần trăm đất làm sân và cây cảnh: $100\\% - 40\\% = 60\\%$. Diện tích: $702 \\times 60 : 100 = 421,2$ $\\text{m}^2$).\nĐáp số: a) 702 $\\text{m}^2$; b) 421,2 $\\text{m}^2$.",
                "answer": "a) 702 m²; b) 421,2 m²",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Cho hai hình tròn đồng tâm $O$. Hình tròn lớn có bán kính $R = 6\\text{ cm}$, hình tròn bé có bán kính $r = 4\\text{ cm}$. Tính diện tích của phần hình vành khăn nằm giữa hai hình tròn đó.",
                "solution": "Bài giải:\nDiện tích hình tròn lớn là:\n$6 \\times 6 \\times 3,14 = 113,04$ ($\\text{cm}^2$)\nDiện tích hình tròn bé là:\n$4 \\times 4 \\times 3,14 = 50,24$ ($\\text{cm}^2$)\nDiện tích phần hình vành khăn nằm giữa hai hình tròn là:\n$113,04 - 50,24 = 62,8$ ($\\text{cm}^2$)\nĐáp số: 62,8 $\\text{cm}^2$.",
                "answer": "62,8 cm²",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 07 (th5_ck1_de07)
    # Ngữ cảnh: Dự án trồng rừng phủ xanh đồi trọc Tây Bắc
    # =========================================================================
    exams["th5_ck1_de07"] = {
        "id": "th5_ck1_de07",
        "testNum": 7,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 7)",
        "grade": "5",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Số thập phân 15,038 gồm có:",
                "options": [
                    "15 đơn vị, 3 phần mười, 8 phần trăm",
                    "15 đơn vị, 3 phần trăm, 8 phần nghìn",
                    "15 đơn vị, 38 phần trăm",
                    "15 đơn vị, 3 phần mười, 8 phần nghìn"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Phần nguyên là 15 đơn vị; phần thập phân gồm 0 phần mười, 3 phần trăm, 8 phần nghìn."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Kết quả của phép nhân $45,6 \\times 0,01$ là:",
                "options": [
                    "4,56",
                    "0,456",
                    "0,0456",
                    "456"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Nhân với 0,01 bằng dịch chuyển dấu phẩy sang trái hai hàng: $45,6 \\times 0,01 = 0,456$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Viết số đo $12\\text{ km } 45\\text{ m}$ dưới dạng số thập phân có đơn vị ki-lô-mét là:",
                "options": [
                    "12,45 km",
                    "12,045 km",
                    "12,0045 km",
                    "1,245 km"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "$45\\text{ m} = \\frac{45}{1000}\\text{ km} = 0,045\\text{ km}$, vậy $12\\text{ km } 45\\text{ m} = 12,045\\text{ km}$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Diện tích hình tam giác có độ dài đáy 15 cm và chiều cao tương ứng 8 cm là:",
                "options": [
                    "120 $\\text{cm}^2$",
                    "60 $\\text{cm}^2$",
                    "30 $\\text{cm}^2$",
                    "23 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Diện tích hình tam giác là: $(15 \\times 8) : 2 = 60$ $\\text{cm}^2$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Một mảnh đất hình chữ nhật có diện tích 84 $\\text{m}^2$, chiều dài 12 m. Chiều rộng mảnh đất đó là:",
                "options": [
                    "6 m",
                    "7 m",
                    "8 m",
                    "9 m"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chiều rộng bằng diện tích chia chiều dài: $84 : 12 = 7$ m."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Chu vi của hình tròn có bán kính $r = 10\\text{ cm}$ là:",
                "options": [
                    "31,4 cm",
                    "62,8 cm",
                    "314 cm",
                    "15,7 cm"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chu vi hình tròn: $C = 2 \\times 10 \\times 3,14 = 62,8$ cm."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $68,75 + 46,58$\nb) $150,2 - 84,65$\nc) $34,8 \\times 2,5$\nd) $81,6 : 24$",
                "solution": "Bài giải:\na) Đặt tính cộng:\n   68,75 + 46,58 = 115,33\nb) Đặt tính trừ:\n   150,20 - 84,65 = 65,55\nc) Đặt tính nhân:\n   34,8 × 2,5 = 87,00 = 87\nd) Đặt tính chia:\n   81,6 : 24 = 3,4\nĐáp số: a) 115,33; b) 65,55; c) 87; d) 3,4",
                "answer": "a) 115,33; b) 65,55; c) 87; d) 3,4",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$4,8 \\times 7,3 + 4,8 \\times 3,7 - 4,8$",
                "solution": "Bài giải:\n$4,8 \\times 7,3 + 4,8 \\times 3,7 - 4,8 = 4,8 \\times (7,3 + 3,7 - 1)$\n$= 4,8 \\times (11 - 1)$\n$= 4,8 \\times 10$\n$= 48$\nĐáp số: 48",
                "answer": "48",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x : 2,4 = 15,2 - 7,7$",
                "solution": "Bài giải:\n$x : 2,4 = 15,2 - 7,7$\n$x : 2,4 = 7,5$\n$x = 7,5 \\times 2,4$\n$x = 18$\nĐáp số: $x = 18$",
                "answer": "x = 18",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Đội tình nguyện trồng cây phủ xanh đồi trọc trong 3 ngày. Ngày thứ nhất đội trồng được 420 cây thông. Ngày thứ hai đội trồng được số cây gấp 1,2 lần ngày thứ nhất. Ngày thứ ba đội trồng được nhiều hơn ngày thứ hai 65 cây. Hỏi trong cả 3 ngày, đội tình nguyện đã trồng được bao nhiêu cây?",
                "solution": "Bài giải:\nSố cây ngày thứ hai đội trồng được là:\n$420 \\times 1,2 = 504$ (cây)\nSố cây ngày thứ ba đội trồng được là:\n$504 + 65 = 569$ (cây)\nCả ba ngày đội tình nguyện trồng được số cây là:\n$420 + 504 + 569 = 1493$ (cây)\nĐáp số: 1493 cây.",
                "answer": "1493 cây",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một thửa đất hình thang có đáy lớn 50 m, đáy bé 30 m, chiều cao bằng $\\frac{3}{4}$ đáy bé.\na) Tính diện tích thửa đất hình thang đó.\nb) Người ta trồng cỏ trên toàn bộ thửa đất, chi phí mua cỏ giống và phân bón là 35 000 đồng cho mỗi $10\\text{ m}^2$. Tính tổng số tiền cần chi trả để trồng cỏ trên cả thửa đất.",
                "solution": "Bài giải:\na) Chiều cao của thửa đất hình thang là:\n$30 \\times \\frac{3}{4} = 22,5$ (m)\nDiện tích của thửa đất hình thang là:\n$(50 + 30) \\times 22,5 : 2 = 80 \\times 22,5 : 2 = 900$ ($\\text{m}^2$)\nb) Tổng số tiền cần chi trả để trồng cỏ là:\n$900 : 10 \\times 35 000 = 3 150 000$ (đồng)\nĐáp số: a) 900 $\\text{m}^2$; b) 3 150 000 đồng.",
                "answer": "a) 900 m²; b) 3 150 000 đồng",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Cho một hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Nếu cùng tăng cả chiều dài và chiều rộng thêm 5 m thì diện tích tăng thêm 225 $\\text{m}^2$. Tính diện tích của hình chữ nhật ban đầu.",
                "solution": "Bài giải:\nGọi chiều rộng ban đầu là $a$ (m) thì chiều dài ban đầu là $3 \\times a$ (m).\nDiện tích hình chữ nhật ban đầu là:\n$S_1 = 3 \\times a \\times a$\nKhi tăng cả chiều dài và chiều rộng thêm 5 m:\nChiều dài mới là $3 \\times a + 5$ (m); chiều rộng mới là $a + 5$ (m).\nDiện tích hình chữ nhật mới là:\n$S_2 = (3 \\times a + 5) \\times (a + 5) = 3 \\times a \\times a + 15 \\times a + 5 \\times a + 25 = 3 \\times a \\times a + 20 \\times a + 25$\nPhần diện tích tăng thêm là:\n$S_2 - S_1 = 20 \\times a + 25 = 225$\n$20 \\times a = 225 - 25 = 200$\n$a = 200 : 20 = 10$ (m)\nChiều rộng ban đầu là 10 m, chiều dài ban đầu là:\n$10 \\times 3 = 30$ (m)\nDiện tích hình chữ nhật ban đầu là:\n$30 \\times 10 = 300$ ($\\text{m}^2$)\nĐáp số: 300 $\\text{m}^2$.",
                "answer": "300 m²",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08 (th5_ck1_de08)
    # Ngữ cảnh: Công trình thủy lợi kênh mương nội đồng và hồ chứa nước
    # =========================================================================
    exams["th5_ck1_de08"] = {
        "id": "th5_ck1_de08",
        "testNum": 8,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 8)",
        "grade": "5",
        "term": "ck1",
        "termName": "Cuối Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Trong số thập phân 314,528 chữ số 5 có giá trị là:",
                "options": [
                    "5",
                    "$\\frac{5}{10}$",
                    "$\\frac{5}{100}$",
                    "$\\frac{5}{1000}$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chữ số 5 đứng ngay sau dấu phẩy nên thuộc hàng phần mười, giá trị là $\\frac{5}{10}$."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Tích của phép nhân $0,05 \\times 1000$ là:",
                "options": [
                    "0,5",
                    "5",
                    "50",
                    "500"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Nhân với 1000 thì dịch dấu phẩy sang phải ba chữ số: $0,05 \\times 1000 = 50$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Đổi $15\\text{ m}^2\\text{ } 8\\text{ dm}^2$ sang số thập phân có đơn vị mét vuông là:",
                "options": [
                    "15,8 $\\text{m}^2$",
                    "15,08 $\\text{m}^2$",
                    "15,008 $\\text{m}^2$",
                    "158 $\\text{m}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "$8\\text{ dm}^2 = 0,08\\text{ m}^2$, vậy kết quả là 15,08 $\\text{m}^2$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Diện tích hình tam giác có độ dài đáy 24 cm và chiều cao 15 cm là:",
                "options": [
                    "360 $\\text{cm}^2$",
                    "180 $\\text{cm}^2$",
                    "90 $\\text{cm}^2$",
                    "195 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Diện tích tam giác: $(24 \\times 15) : 2 = 180$ $\\text{cm}^2$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Một hình tròn có bán kính $r = 6\\text{ cm}$. Diện tích của hình tròn đó là:",
                "options": [
                    "37,68 $\\text{cm}^2$",
                    "113,04 $\\text{cm}^2$",
                    "56,52 $\\text{cm}^2$",
                    "18,84 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Diện tích hình tròn: $S = 6 \\times 6 \\times 3,14 = 36 \\times 3,14 = 113,04$ $\\text{cm}^2$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Kết quả của biểu thức $18,9 : 9 + 3,1$ là:",
                "options": [
                    "5,2",
                    "4,2",
                    "5,1",
                    "6,2"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Thực hiện phép chia trước: $18,9 : 9 = 2,1$, sau đó cộng: $2,1 + 3,1 = 5,2$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $85,63 + 57,48$\nb) $164,5 - 89,76$\nc) $42,6 \\times 3,5$\nd) $117,6 : 28$",
                "solution": "Bài giải:\na) Đặt tính cộng:\n   85,63 + 57,48 = 143,11\nb) Đặt tính trừ:\n   164,50 - 89,76 = 74,74\nc) Đặt tính nhân:\n   42,6 × 3,5 = 149,10 = 149,1\nd) Đặt tính chia:\n   117,6 : 28 = 4,2\nĐáp số: a) 143,11; b) 74,74; c) 149,1; d) 4,2",
                "answer": "a) 143,11; b) 74,74; c) 149,1; d) 4,2",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$0,25 \\times 4,68 \\times 40$",
                "solution": "Bài giải:\n$0,25 \\times 4,68 \\times 40 = (0,25 \\times 40) \\times 4,68$\n$= 10 \\times 4,68$\n$= 46,8$\nĐáp số: 46,8",
                "answer": "46,8",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x \\times 4,5 = 38,25 - 6,75$",
                "solution": "Bài giải:\n$x \\times 4,5 = 38,25 - 6,75$\n$x \\times 4,5 = 31,5$\n$x = 31,5 : 4,5$\n$x = 7$\nĐáp số: $x = 7$",
                "answer": "x = 7",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Đội thi công nạo vét kênh thủy lợi dự kiến thực hiện trong 4 ngày. Ba ngày đầu, mỗi ngày đội nạo vét được 165,5 m kênh. Ngày thứ tư đội nạo vét được 182 m kênh.\na) Hỏi trong cả 4 ngày đội đã nạo vét được tất cả bao nhiêu mét kênh?\nb) Trung bình mỗi ngày đội đó nạo vét được bao nhiêu mét kênh?",
                "solution": "Bài giải:\na) Trong ba ngày đầu đội nạo vét được số mét kênh là:\n$165,5 \\times 3 = 496,5$ (m)\nTrong cả bốn ngày đội nạo vét được số mét kênh là:\n$496,5 + 182 = 678,5$ (m)\nb) Trung bình mỗi ngày đội nạo vét được số mét kênh là:\n$678,5 : 4 = 169,625$ (m)\nĐáp số: a) 678,5 m kênh; b) 169,625 m kênh.",
                "answer": "a) 678,5 m; b) 169,625 m",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một hồ chứa nước nhân tạo có bề mặt là hình thang với đáy lớn 75 m, đáy bé bằng $\\frac{3}{5}$ đáy lớn, chiều cao là 40 m.\na) Tính diện tích bề mặt của hồ chứa nước hình thang đó.\nb) Người ta thả cá giống vào hồ, cứ $100\\text{ m}^2$ mặt nước thì thả 25 con cá giống. Hỏi cần thả vào hồ bao nhiêu con cá giống?",
                "solution": "Bài giải:\na) Độ dài đáy bé bề mặt hồ nước là:\n$75 \\times \\frac{3}{5} = 45$ (m)\nDiện tích bề mặt hồ nước là:\n$(75 + 45) \\times 40 : 2 = 120 \\times 40 : 2 = 2400$ ($\\text{m}^2$)\nb) Số con cá giống cần thả vào hồ là:\n$2400 : 100 \\times 25 = 600$ (con)\nĐáp số: a) 2400 $\\text{m}^2$; b) 600 con cá giống.",
                "answer": "a) 2400 m²; b) 600 con cá giống",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Cho dãy số thập phân: $10,1 + 11,2 + 12,3 + ... + 18,9 + 20,0$. Tính giá trị của biểu thức trên bằng cách thuận tiện nhất.",
                "solution": "Bài giải:\nKhoảng cách giữa hai số liên tiếp trong dãy là:\n$11,2 - 10,1 = 1,1$\nSố các số hạng của dãy là:\n$(20,0 - 10,1) : 1,1 + 1 = 9,9 : 1,1 + 1 = 9 + 1 = 10$ (số hạng)\nTổng của dãy số là:\n$(10,1 + 20,0) \\times 10 : 2 = 30,1 \\times 5 = 150,5$\nĐáp số: 150,5.",
                "answer": "150,5",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    return exams


if __name__ == "__main__":
    exams = get_th5_ck1_exams()
    print(f"Tổng số đề CK1: {len(exams)}")
    for eid, ex in exams.items():
        print(f"- {eid}: {ex['title']} | TN: {len(ex['part1'])} câu | TL: {len(ex['part2'])} bài")
