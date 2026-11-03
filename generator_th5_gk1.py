# -*- coding: utf-8 -*-
"""
HỆ THỐNG ĐỀ KIỂM TRA GIỮA HỌC KÌ 1 - TOÁN TIỂU HỌC (LỚP 5)
Bộ sách: KẾT NỐI TRI THỨC VỚI CUỘC SỐNG
Gồm 8 đề kiểm tra chuẩn hóa độc lập 100% (th5_gk1_de01 đến th5_gk1_de08).

Cấu trúc mỗi đề thi:
- Thời gian làm bài: 40 phút
- Thang điểm: 10.0 điểm
- Phần I (3.0 điểm): 6 câu Trắc nghiệm khách quan 4 lựa chọn (mỗi câu 0.5 điểm)
- Phần II (7.0 điểm): 6 bài Tự luận (Điểm số: 1.0, 1.0, 1.0, 1.5, 1.5, 1.0 điểm; có lineCount chừa dòng làm bài)
"""

def get_th5_gk1_exams():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 01 (th5_gk1_de01)
    # Chủ đề: Nông trại hoa quả, thu hoạch cam và quýt
    # =========================================================================
    exams["th5_gk1_de01"] = {
        "id": "th5_gk1_de01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 1)",
        "grade": "5",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Trong số thập phân 85,274, chữ số 7 có giá trị là:",
                "options": [
                    "7",
                    "$\\frac{7}{10}$",
                    "$\\frac{7}{100}$",
                    "$\\frac{7}{1000}$"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Chữ số 7 nằm ở hàng phần trăm nên có giá trị là $\\frac{7}{100}$ (hay 0,07)."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Phân số nào dưới đây là phân số thập phân?",
                "options": [
                    "$\\frac{3}{10}$",
                    "$\\frac{4}{25}$",
                    "$\\frac{7}{200}$",
                    "$\\frac{5}{8}$"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Phân số thập phân là phân số có mẫu số là 10, 100, 1000,... Do đó $\\frac{3}{10}$ là phân số thập phân."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Số thập phân 42,085 được đọc là:",
                "options": [
                    "Bốn mươi hai phẩy tám mươi lăm",
                    "Bốn mươi hai phẩy không trăm tám mươi lăm",
                    "Bốn mươi hai phẩy tám năm",
                    "Bốn trăm hai mươi phẩy tám mươi lăm"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Số 42,085 đọc là: 'Bốn mươi hai phẩy không trăm tám mươi lăm'."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Chuyển hỗn số $3\\frac{2}{5}$ thành phân số ta được:",
                "options": [
                    "$\\frac{11}{5}$",
                    "$\\frac{17}{5}$",
                    "$\\frac{6}{5}$",
                    "$\\frac{13}{5}$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Ta có: $3\\frac{2}{5} = \\frac{3 \\times 5 + 2}{5} = \\frac{17}{5}$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Kết quả của phép nhân $\\frac{4}{7} \\times \\frac{21}{8}$ rút gọn về phân số tối giản là:",
                "options": [
                    "$\\frac{3}{2}$",
                    "$\\frac{2}{3}$",
                    "$\\frac{84}{56}$",
                    "$\\frac{7}{4}$"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Ta có: $\\frac{4}{7} \\times \\frac{21}{8} = \\frac{4 \\times 21}{7 \\times 8} = \\frac{1 \\times 3}{1 \\times 2} = \\frac{3}{2}$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Một lớp học có 32 học sinh, trong đó số bạn nữ gấp 3 lần số bạn nam. Hỏi lớp học đó có bao nhiêu bạn nữ?",
                "options": [
                    "8 bạn",
                    "16 bạn",
                    "24 bạn",
                    "20 bạn"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Tổng số phần bằng nhau: $1 + 3 = 4$ phần. Số bạn nữ là: $32 : 4 \\times 3 = 24$ bạn."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Tính giá trị các biểu thức sau:\na) $\\frac{3}{4} + \\frac{2}{5}$\nb) $\\frac{5}{6} - \\frac{3}{8}$",
                "solution": "Bài giải:\na) $\\frac{3}{4} + \\frac{2}{5} = \\frac{15}{20} + \\frac{8}{20} = \\frac{23}{20}$\nb) $\\frac{5}{6} - \\frac{3}{8} = \\frac{20}{24} - \\frac{9}{24} = \\frac{11}{24}$\nĐáp số: a) $\\frac{23}{20}$; b) $\\frac{11}{24}$",
                "answer": "a) 23/20; b) 11/24",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Viết số thập phân thích hợp vào chỗ chấm:\na) $6\\text{ m } 8\\text{ dm} = ..........\\text{ m}$\nb) $4\\text{ kg } 75\\text{ g} = ..........\\text{ kg}$\nc) $3\\text{ m}^2\\text{ } 25\\text{ dm}^2 = ..........\\text{ m}^2$\nd) $15\\text{ dm}^2 = ..........\\text{ m}^2$",
                "solution": "Bài giải:\na) $6\\text{ m } 8\\text{ dm} = 6\\frac{8}{10}\\text{ m} = 6,8\\text{ m}$\nb) $4\\text{ kg } 75\\text{ g} = 4\\frac{75}{1000}\\text{ kg} = 4,075\\text{ kg}$\nc) $3\\text{ m}^2\\text{ } 25\\text{ dm}^2 = 3\\frac{25}{100}\\text{ m}^2 = 3,25\\text{ m}^2$\nd) $15\\text{ dm}^2 = \\frac{15}{100}\\text{ m}^2 = 0,15\\text{ m}^2$\nĐáp số: a) 6,8; b) 4,075; c) 3,25; d) 0,15",
                "answer": "a) 6,8 m; b) 4,075 kg; c) 3,25 m²; d) 0,15 m²",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x : \\frac{3}{5} = \\frac{5}{9}$",
                "solution": "Bài giải:\n$x : \\frac{3}{5} = \\frac{5}{9}$\n$x = \\frac{5}{9} \\times \\frac{3}{5}$\n$x = \\frac{5 \\times 3}{9 \\times 5}$\n$x = \\frac{1}{3}$\nĐáp số: $x = \\frac{1}{3}$",
                "answer": "x = 1/3",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Một nông trại thu hoạch được tất cả 450 kg gồm cam và quýt. Biết rằng số quýt bằng $\\frac{2}{3}$ số cam. Hỏi nông trại đó thu hoạch được bao nhiêu ki-lô-gam cam, bao nhiêu ki-lô-gam quýt?",
                "solution": "Bài giải:\nTheo sơ đồ, tổng số phần bằng nhau là:\n$2 + 3 = 5$ (phần)\nSố ki-lô-gam quýt nông trại thu hoạch được là:\n$450 : 5 \\times 2 = 180$ (kg)\nSố ki-lô-gam cam nông trại thu hoạch được là:\n$450 - 180 = 270$ (kg)\nĐáp số: Quýt: 180 kg; Cam: 270 kg.",
                "answer": "Quýt: 180 kg; Cam: 270 kg",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một mảnh đất hình chữ nhật có chiều dài hơn chiều rộng 18 m. Chiều rộng bằng $\\frac{3}{5}$ chiều dài.\na) Tính chiều dài và chiều rộng của mảnh đất đó.\nb) Tính diện tích của mảnh đất đó.",
                "solution": "Bài giải:\na) Theo sơ đồ, hiệu số phần bằng nhau là:\n$5 - 3 = 2$ (phần)\nChiều rộng của mảnh đất là:\n$18 : 2 \\times 3 = 27$ (m)\nChiều dài của mảnh đất là:\n$27 + 18 = 45$ (m)\nb) Diện tích của mảnh đất là:\n$45 \\times 27 = 1215$ ($\\text{m}^2$)\nĐáp số: a) Chiều dài: 45 m, chiều rộng: 27 m; b) Diện tích: 1215 $\\text{m}^2$.",
                "answer": "a) Dài: 45 m, rộng: 27 m; b) Diện tích: 1215 m²",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tính nhanh giá trị của biểu thức sau:\n$A = \\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\frac{1}{3 \\times 4} + \\frac{1}{4 \\times 5} + \\frac{1}{5 \\times 6}$",
                "solution": "Bài giải:\nTa có:\n$A = (1 - \\frac{1}{2}) + (\\frac{1}{2} - \\frac{1}{3}) + (\\frac{1}{3} - \\frac{1}{4}) + (\\frac{1}{4} - \\frac{1}{5}) + (\\frac{1}{5} - \\frac{1}{6})$\n$A = 1 - \\frac{1}{6}$\n$A = \\frac{5}{6}$\nĐáp số: $A = \\frac{5}{6}$",
                "answer": "A = 5/6",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 02 (th5_gk1_de02)
    # Chủ đề: Thư viện trường học, sách giáo khoa và sách tham khảo
    # =========================================================================
    exams["th5_gk1_de02"] = {
        "id": "th5_gk1_de02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 2)",
        "grade": "5",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Phân số thập phân $\\frac{45}{1000}$ được viết dưới dạng số thập phân là:",
                "options": [
                    "0,45",
                    "0,045",
                    "0,0045",
                    "4,5"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "$\\frac{45}{1000} = 0,045$ vì mẫu số có 3 chữ số 0 nên phần thập phân có 3 chữ số."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Chữ số 8 trong số thập phân 135,82 thuộc hàng nào?",
                "options": [
                    "Hàng chục",
                    "Hàng đơn vị",
                    "Hàng phần mười",
                    "Hàng phần trăm"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Chữ số 8 đứng ngay sau dấu phẩy nên thuộc hàng phần mười."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Trong các số thập phân sau, số thập phân bé nhất là:",
                "options": [
                    "9,42",
                    "9,24",
                    "9,402",
                    "9,204"
                ],
                "correct": 3,
                "points": 0.5,
                "explanation": "Các số đều có phần nguyên là 9. So sánh hàng phần mười: $2 < 4$. So sánh 9,24 và 9,204 ở hàng phần trăm: $0 < 4$ nên 9,204 là số bé nhất."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Chuyển phân số $\\frac{23}{4}$ thành hỗn số ta được:",
                "options": [
                    "$5\\frac{3}{4}$",
                    "$4\\frac{3}{4}$",
                    "$5\\frac{1}{4}$",
                    "$3\\frac{5}{4}$"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Thực hiện phép chia: $23 : 4 = 5$ (dư 3). Do đó $\\frac{23}{4} = 5\\frac{3}{4}$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Kết quả của phép chia $\\frac{5}{7} : \\frac{15}{14}$ là:",
                "options": [
                    "$\\frac{1}{2}$",
                    "$\\frac{2}{3}$",
                    "$\\frac{3}{2}$",
                    "$\\frac{75}{98}$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Ta có: $\\frac{5}{7} : \\frac{15}{14} = \\frac{5}{7} \\times \\frac{14}{15} = \\frac{5 \\times 14}{7 \\times 15} = \\frac{1 \\times 2}{1 \\times 3} = \\frac{2}{3}$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Hiệu của hai số là 48. Tỉ số của số bé và số lớn là $\\frac{1}{4}$. Số lớn là:",
                "options": [
                    "16",
                    "36",
                    "64",
                    "72"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Hiệu số phần bằng nhau: $4 - 1 = 3$ phần. Số lớn là: $48 : 3 \\times 4 = 64$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Tính giá trị các biểu thức sau:\na) $\\frac{5}{8} \\times \\frac{4}{15}$\nb) $\\frac{9}{10} : \\frac{3}{5}$",
                "solution": "Bài giải:\na) $\\frac{5}{8} \\times \\frac{4}{15} = \\frac{5 \\times 4}{8 \\times 15} = \\frac{1 \\times 1}{2 \\times 3} = \\frac{1}{6}$\nb) $\\frac{9}{10} : \\frac{3}{5} = \\frac{9}{10} \\times \\frac{5}{3} = \\frac{9 \\times 5}{10 \\times 3} = \\frac{3 \\times 1}{2 \\times 1} = \\frac{3}{2}$\nĐáp số: a) $\\frac{1}{6}$; b) $\\frac{3}{2}$",
                "answer": "a) 1/6; b) 3/2",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Viết số thập phân thích hợp vào chỗ chấm:\na) $15\\text{ m } 6\\text{ cm} = ..........\\text{ m}$\nb) $2\\text{ tấn } 450\\text{ kg} = ..........\\text{ tấn}$\nc) $7\\text{ m}^2\\text{ } 9\\text{ dm}^2 = ..........\\text{ m}^2$\nd) $360\\text{ g} = ..........\\text{ kg}$",
                "solution": "Bài giải:\na) $15\\text{ m } 6\\text{ cm} = 15\\frac{6}{100}\\text{ m} = 15,06\\text{ m}$\nb) $2\\text{ tấn } 450\\text{ kg} = 2\\frac{450}{1000}\\text{ tấn} = 2,45\\text{ tấn}$\nc) $7\\text{ m}^2\\text{ } 9\\text{ dm}^2 = 7\\frac{9}{100}\\text{ m}^2 = 7,09\\text{ m}^2$\nd) $360\\text{ g} = \\frac{360}{1000}\\text{ kg} = 0,36\\text{ kg}$\nĐáp số: a) 15,06; b) 2,45; c) 7,09; d) 0,36",
                "answer": "a) 15,06 m; b) 2,45 tấn; c) 7,09 m²; d) 0,36 kg",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x - \\frac{2}{3} = \\frac{5}{12}$",
                "solution": "Bài giải:\n$x - \\frac{2}{3} = \\frac{5}{12}$\n$x = \\frac{5}{12} + \\frac{2}{3}$\n$x = \\frac{5}{12} + \\frac{8}{12}$\n$x = \\frac{13}{12}$\nĐáp số: $x = \\frac{13}{12}$",
                "answer": "x = 13/12",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Thư viện một trường tiểu học có tất cả 630 quyển sách gồm sách giáo khoa và sách tham khảo. Biết số sách giáo khoa bằng $\\frac{4}{5}$ số sách tham khảo. Hỏi thư viện có bao nhiêu quyển sách mỗi loại?",
                "solution": "Bài giải:\nTheo sơ đồ, tổng số phần bằng nhau là:\n$4 + 5 = 9$ (phần)\nSố sách giáo khoa của thư viện là:\n$630 : 9 \\times 4 = 280$ (quyển)\nSố sách tham khảo của thư viện là:\n$630 - 280 = 350$ (quyển)\nĐáp số: Sách giáo khoa: 280 quyển; Sách tham khảo: 350 quyển.",
                "answer": "Sách giáo khoa: 280 quyển; Sách tham khảo: 350 quyển",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một sân trường hình chữ nhật có chu vi bằng 140 m. Chiều rộng bằng $\\frac{3}{4}$ chiều dài.\na) Tính chiều dài và chiều rộng của sân trường.\nb) Tính diện tích của sân trường đó.",
                "solution": "Bài giải:\na) Nửa chu vi sân trường là:\n$140 : 2 = 70$ (m)\nTheo sơ đồ, tổng số phần bằng nhau là:\n$3 + 4 = 7$ (phần)\nChiều rộng sân trường là:\n$70 : 7 \\times 3 = 30$ (m)\nChiều dài sân trường là:\n$70 - 30 = 40$ (m)\nb) Diện tích của sân trường là:\n$40 \\times 30 = 1200$ ($\\text{m}^2$)\nĐáp số: a) Chiều dài: 40 m, chiều rộng: 30 m; b) Diện tích: 1200 $\\text{m}^2$.",
                "answer": "a) Dài: 40 m, rộng: 30 m; b) Diện tích: 1200 m²",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tìm số tự nhiên $x$ biết: $3,5 < x < 7,2$ và $x$ là số chẵn chia hết cho 3.",
                "solution": "Bài giải:\nCác số tự nhiên lớn hơn 3,5 và bé hơn 7,2 là: 4; 5; 6; 7.\nTrong các số trên, số chẵn là: 4 và 6.\nTrong hai số chẵn đó, số chia hết cho 3 là: 6.\nVậy số tự nhiên cần tìm là: $x = 6$.\nĐáp số: $x = 6$.",
                "answer": "x = 6",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 03 (th5_gk1_de03)
    # Chủ đề: Đội tình nguyện trồng cây gây rừng
    # =========================================================================
    exams["th5_gk1_de03"] = {
        "id": "th5_gk1_de03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 3)",
        "grade": "5",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Số \"Ba trăm linh năm phẩy không bảy\" được viết là:",
                "options": [
                    "305,7",
                    "305,07",
                    "350,07",
                    "305,007"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Phần nguyên là 305, phần thập phân gồm 0 phần mười và 7 phần trăm nên viết là 305,07."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Trong số thập phân 68,915 chữ số 5 có giá trị là:",
                "options": [
                    "$\\frac{5}{10}$",
                    "$\\frac{5}{100}$",
                    "$\\frac{5}{1000}$",
                    "5"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Chữ số 5 ở hàng phần nghìn nên có giá trị là $\\frac{5}{1000}$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Làm tròn số thập phân 24,76 đến hàng phần mười ta được số:",
                "options": [
                    "24,7",
                    "24,8",
                    "25,0",
                    "24,0"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chữ số ở hàng phần trăm là 6 ($\\ge 5$), nên làm tròn lên thành 24,8."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Viết số đo $5\\text{ km } 38\\text{ m}$ dưới dạng số thập phân với đơn vị ki-lô-mét là:",
                "options": [
                    "5,38 km",
                    "5,038 km",
                    "5,380 km",
                    "50,38 km"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Ta có $38\\text{ m} = \\frac{38}{1000}\\text{ km} = 0,038\\text{ km}$, vậy $5\\text{ km } 38\\text{ m} = 5,038\\text{ km}$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Rút gọn phân số $\\frac{36}{48}$ về dạng tối giản ta được:",
                "options": [
                    "$\\frac{6}{8}$",
                    "$\\frac{9}{12}$",
                    "$\\frac{3}{4}$",
                    "$\\frac{2}{3}$"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Chia cả tử và mẫu cho 12 ta được: $\\frac{36 : 12}{48 : 12} = \\frac{3}{4}$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Một vườn cây có 84 cây ăn quả gồm xoài và nhãn. Số cây nhãn bằng $\\frac{3}{4}$ số cây xoài. Số cây xoài trong vườn là:",
                "options": [
                    "36 cây",
                    "48 cây",
                    "21 cây",
                    "63 cây"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Tổng số phần bằng nhau: $3 + 4 = 7$ phần. Số cây xoài là: $84 : 7 \\times 4 = 48$ cây."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Tính giá trị các biểu thức sau:\na) $\\frac{7}{12} + \\frac{5}{6} - \\frac{3}{4}$\nb) $\\frac{5}{9} : \\frac{2}{3} \\times \\frac{6}{5}$",
                "solution": "Bài giải:\na) $\\frac{7}{12} + \\frac{5}{6} - \\frac{3}{4} = \\frac{7}{12} + \\frac{10}{12} - \\frac{9}{12} = \\frac{7 + 10 - 9}{12} = \\frac{8}{12} = \\frac{2}{3}$\nb) $\\frac{5}{9} : \\frac{2}{3} \\times \\frac{6}{5} = \\frac{5}{9} \\times \\frac{3}{2} \\times \\frac{6}{5} = \\frac{5 \\times 3 \\times 6}{9 \\times 2 \\times 5} = \\frac{90}{90} = 1$\nĐáp số: a) $\\frac{2}{3}$; b) $1$",
                "answer": "a) 2/3; b) 1",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Viết số thập phân thích hợp vào chỗ chấm:\na) $8\\text{ m } 5\\text{ cm} = ..........\\text{ m}$\nb) $5\\text{ kg } 60\\text{ g} = ..........\\text{ kg}$\nc) $12\\text{ ha} = ..........\\text{ km}^2$\nd) $45\\text{ dm}^2 = ..........\\text{ m}^2$",
                "solution": "Bài giải:\na) $8\\text{ m } 5\\text{ cm} = 8\\frac{5}{100}\\text{ m} = 8,05\\text{ m}$\nb) $5\\text{ kg } 60\\text{ g} = 5\\frac{60}{1000}\\text{ kg} = 5,06\\text{ kg}$\nc) $12\\text{ ha} = \\frac{12}{100}\\text{ km}^2 = 0,12\\text{ km}^2$\nd) $45\\text{ dm}^2 = \\frac{45}{100}\\text{ m}^2 = 0,45\\text{ m}^2$\nĐáp số: a) 8,05; b) 5,06; c) 0,12; d) 0,45",
                "answer": "a) 8,05 m; b) 5,06 kg; c) 0,12 km²; d) 0,45 m²",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$\\frac{4}{7} + x = \\frac{11}{14}$",
                "solution": "Bài giải:\n$\\frac{4}{7} + x = \\frac{11}{14}$\n$x = \\frac{11}{14} - \\frac{4}{7}$\n$x = \\frac{11}{14} - \\frac{8}{14}$\n$x = \\frac{3}{14}$\nĐáp số: $x = \\frac{3}{14}$",
                "answer": "x = 3/14",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Hai lớp 5A và 5B tham gia phong trào trồng cây gây rừng. Cả hai lớp trồng được tất cả 160 cây. Biết rằng số cây lớp 5A trồng bằng $\\frac{3}{5}$ số cây lớp 5B trồng. Hỏi mỗi lớp trồng được bao nhiêu cây?",
                "solution": "Bài giải:\nTheo sơ đồ, tổng số phần bằng nhau là:\n$3 + 5 = 8$ (phần)\nSố cây lớp 5A trồng được là:\n$160 : 8 \\times 3 = 60$ (cây)\nSố cây lớp 5B trồng được là:\n$160 - 60 = 100$ (cây)\nĐáp số: Lớp 5A: 60 cây; Lớp 5B: 100 cây.",
                "answer": "5A: 60 cây; 5B: 100 cây",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Đoạn dây thứ nhất dài hơn đoạn dây thứ hai là 36 m. Biết rằng đoạn dây thứ hai dài bằng $\\frac{2}{5}$ đoạn dây thứ nhất. Tính chiều dài của mỗi đoạn dây đó.",
                "solution": "Bài giải:\nTheo sơ đồ, hiệu số phần bằng nhau là:\n$5 - 2 = 3$ (phần)\nChiều dài đoạn dây thứ hai là:\n$36 : 3 \\times 2 = 24$ (m)\nChiều dài đoạn dây thứ nhất là:\n$24 + 36 = 60$ (m)\nĐáp số: Đoạn dây thứ nhất: 60 m; Đoạn dây thứ hai: 24 m.",
                "answer": "Đoạn 1: 60 m; Đoạn 2: 24 m",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tìm hai số tự nhiên liên tiếp $a$ và $b$ sao cho: $a < 12,35 + 8,75 < b$.",
                "solution": "Bài giải:\nTa có phép tính: $12,35 + 8,75 = 21,1$.\nBiểu thức trở thành: $a < 21,1 < b$.\nVì $a$ và $b$ là hai số tự nhiên liên tiếp nên $a$ là số tự nhiên lớn nhất bé hơn 21,1 và $b$ là số tự nhiên bé nhất lớn hơn 21,1.\nDo đó: $a = 21$ và $b = 22$.\nĐáp số: $a = 21; b = 22$.",
                "answer": "a = 21; b = 22",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 04 (th5_gk1_de04)
    # Chủ đề: Cửa hàng lương thực, nhập gạo tẻ và gạo nếp
    # =========================================================================
    exams["th5_gk1_de04"] = {
        "id": "th5_gk1_de04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 4)",
        "grade": "5",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Phân số $\\frac{7}{25}$ được viết thành phân số thập phân có mẫu số là 100 là:",
                "options": [
                    "$\\frac{14}{100}$",
                    "$\\frac{28}{100}$",
                    "$\\frac{35}{100}$",
                    "$\\frac{21}{100}$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Nhân cả tử và mẫu với 4: $\\frac{7 \\times 4}{25 \\times 4} = \\frac{28}{100}$."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Số thập phân gồm có \"5 đơn vị, 8 phần mười và 6 phần nghìn\" viết là:",
                "options": [
                    "5,86",
                    "5,086",
                    "5,806",
                    "58,06"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Hàng đơn vị là 5, hàng phần mười là 8, hàng phần trăm là 0, hàng phần nghìn là 6. Vậy viết là 5,806."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Dãy số nào dưới đây được sắp xếp theo thứ tự từ lớn đến bé?",
                "options": [
                    "6,54; 6,504; 6,45; 6,054",
                    "6,54; 6,45; 6,504; 6,054",
                    "6,054; 6,45; 6,504; 6,54",
                    "6,504; 6,54; 6,45; 6,054"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "So sánh phần thập phân: $6,540 > 6,504 > 6,450 > 6,054$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Hỗn số $4\\frac{3}{8}$ chuyển thành phân số là:",
                "options": [
                    "$\\frac{12}{8}$",
                    "$\\frac{35}{8}$",
                    "$\\frac{32}{8}$",
                    "$\\frac{27}{8}$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Ta có: $4\\frac{3}{8} = \\frac{4 \\times 8 + 3}{8} = \\frac{35}{8}$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Rút gọn phân số $\\frac{42}{56}$ về phân số tối giản ta được:",
                "options": [
                    "$\\frac{7}{8}$",
                    "$\\frac{3}{4}$",
                    "$\\frac{6}{8}$",
                    "$\\frac{21}{28}$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chia cả tử và mẫu cho 14: $\\frac{42 : 14}{56 : 14} = \\frac{3}{4}$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Mẹ hơn con 28 tuổi. Tuổi con bằng $\\frac{2}{9}$ tuổi mẹ. Tuổi của con hiện nay là:",
                "options": [
                    "6 tuổi",
                    "8 tuổi",
                    "10 tuổi",
                    "12 tuổi"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Hiệu số phần bằng nhau: $9 - 2 = 7$ phần. Tuổi con là: $28 : 7 \\times 2 = 8$ tuổi."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Tính giá trị các biểu thức sau:\na) $\\frac{7}{15} \\times \\frac{25}{14}$\nb) $2 - \\frac{5}{7}$",
                "solution": "Bài giải:\na) $\\frac{7}{15} \\times \\frac{25}{14} = \\frac{7 \\times 25}{15 \\times 14} = \\frac{1 \\times 5}{3 \\times 2} = \\frac{5}{6}$\nb) $2 - \\frac{5}{7} = \\frac{14}{7} - \\frac{5}{7} = \\frac{9}{7}$\nĐáp số: a) $\\frac{5}{6}$; b) $\\frac{9}{7}$",
                "answer": "a) 5/6; b) 9/7",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Viết số thích hợp vào chỗ chấm:\na) $9\\text{ dm } 4\\text{ mm} = ..........\\text{ dm}$\nb) $3\\text{ tấn } 80\\text{ kg} = ..........\\text{ tấn}$\nc) $8\\text{ m}^2\\text{ } 6\\text{ dm}^2 = ..........\\text{ m}^2$\nd) $52\\text{ cm} = ..........\\text{ m}$",
                "solution": "Bài giải:\na) $9\\text{ dm } 4\\text{ mm} = 9\\frac{4}{100}\\text{ dm} = 9,04\\text{ dm}$\nb) $3\\text{ tấn } 80\\text{ kg} = 3\\frac{80}{1000}\\text{ tấn} = 3,08\\text{ tấn}$\nc) $8\\text{ m}^2\\text{ } 6\\text{ dm}^2 = 8\\frac{6}{100}\\text{ m}^2 = 8,06\\text{ m}^2$\nd) $52\\text{ cm} = \\frac{52}{100}\\text{ m} = 0,52\\text{ m}$\nĐáp số: a) 9,04; b) 3,08; c) 8,06; d) 0,52",
                "answer": "a) 9,04 dm; b) 3,08 tấn; c) 8,06 m²; d) 0,52 m",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x \\times \\frac{3}{4} = \\frac{9}{16}$",
                "solution": "Bài giải:\n$x \\times \\frac{3}{4} = \\frac{9}{16}$\n$x = \\frac{9}{16} : \\frac{3}{4}$\n$x = \\frac{9}{16} \\times \\frac{4}{3}$\n$x = \\frac{9 \\times 4}{16 \\times 3} = \\frac{3}{4}$\nĐáp số: $x = \\frac{3}{4}$",
                "answer": "x = 3/4",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Cửa hàng lương thực có tất cả 720 kg gạo gồm gạo tẻ và gạo nếp. Số gạo nếp bằng $\\frac{3}{5}$ số gạo tẻ. Hỏi cửa hàng có bao nhiêu ki-lô-gam gạo tẻ, bao nhiêu ki-lô-gam gạo nếp?",
                "solution": "Bài giải:\nTheo sơ đồ, tổng số phần bằng nhau là:\n$3 + 5 = 8$ (phần)\nSố gạo nếp cửa hàng có là:\n$720 : 8 \\times 3 = 270$ (kg)\nSố gạo tẻ cửa hàng có là:\n$720 - 270 = 450$ (kg)\nĐáp số: Gạo nếp: 270 kg; Gạo tẻ: 450 kg.",
                "answer": "Nếp: 270 kg; Tẻ: 450 kg",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một mảnh đất hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Nếu bớt chiều dài đi 24 m thì chiều dài bằng chiều rộng.\na) Tính chu vi của mảnh đất đó.\nb) Tính diện tích của mảnh đất đó.",
                "solution": "Bài giải:\na) Khi bớt chiều dài đi 24 m thì bằng chiều rộng, vậy chiều dài hơn chiều rộng 24 m.\nTheo sơ đồ, hiệu số phần bằng nhau là:\n$3 - 1 = 2$ (phần)\nChiều rộng của mảnh đất là:\n$24 : 2 = 12$ (m)\nChiều dài của mảnh đất là:\n$12 \\times 3 = 36$ (m)\nChu vi của mảnh đất là:\n$(36 + 12) \\times 2 = 96$ (m)\nb) Diện tích của mảnh đất là:\n$36 \\times 12 = 432$ ($\\text{m}^2$)\nĐáp số: a) Chu vi: 96 m; b) Diện tích: 432 $\\text{m}^2$.",
                "answer": "a) Chu vi: 96 m; b) Diện tích: 432 m²",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tính nhanh giá trị của biểu thức sau:\n$B = \\frac{2}{1 \\times 3} + \\frac{2}{3 \\times 5} + \\frac{2}{5 \\times 7} + \\frac{2}{7 \\times 9} + \\frac{2}{9 \\times 11}$",
                "solution": "Bài giải:\nTa có:\n$B = (1 - \\frac{1}{3}) + (\\frac{1}{3} - \\frac{1}{5}) + (\\frac{1}{5} - \\frac{1}{7}) + (\\frac{1}{7} - \\frac{1}{9}) + (\\frac{1}{9} - \\frac{1}{11})$\n$B = 1 - \\frac{1}{11}$\n$B = \\frac{10}{11}$\nĐáp số: $B = \\frac{10}{11}$",
                "answer": "B = 10/11",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 05 (th5_gk1_de05)
    # Chủ đề: Xưởng may may đồng phục học sinh
    # =========================================================================
    exams["th5_gk1_de05"] = {
        "id": "th5_gk1_de05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 5)",
        "grade": "5",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Trong số thập phân 47,382, chữ số 3 có giá trị là:",
                "options": [
                    "3",
                    "$\\frac{3}{10}$",
                    "$\\frac{3}{100}$",
                    "$\\frac{3}{1000}$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chữ số 3 ở ngay sau dấu phẩy thuộc hàng phần mười nên có giá trị là $\\frac{3}{10}$."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Viết phân số $\\frac{3}{8}$ dưới dạng số thập phân ta được:",
                "options": [
                    "0,375",
                    "0,38",
                    "0,25",
                    "0,83"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Thực hiện phép chia: $3 : 8 = 0,375$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Số thập phân nào dưới đây lớn hơn 15,48 và nhỏ hơn 15,5?",
                "options": [
                    "15,479",
                    "15,49",
                    "15,51",
                    "15,502"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Ta có $15,48 < 15,49 < 15,50$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Đổi $4\\text{ m}^2\\text{ } 15\\text{ dm}^2$ sang số thập phân có đơn vị mét vuông ta được:",
                "options": [
                    "4,15 $\\text{m}^2$",
                    "4,015 $\\text{m}^2$",
                    "41,5 $\\text{m}^2$",
                    "415 $\\text{m}^2$"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Ta có $15\\text{ dm}^2 = \\frac{15}{100}\\text{ m}^2 = 0,15\\text{ m}^2$, do đó kết quả là 4,15 $\\text{m}^2$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Một tổ thợ may gồm 20 công nhân may xong 100 bộ đồng phục trong 1 ngày. Muốn may 150 bộ đồng phục cùng loại trong 1 ngày thì cần bao nhiêu công nhân? (Năng suất làm việc mỗi người như nhau).",
                "options": [
                    "25 người",
                    "30 người",
                    "35 người",
                    "40 người"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Một công nhân may được số bộ quần áo là: $100 : 20 = 5$ (bộ). Để may 150 bộ cần: $150 : 5 = 30$ công nhân."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Hỗn số $2\\frac{3}{4}$ tương ứng với số thập phân nào sau đây?",
                "options": [
                    "2,34",
                    "2,43",
                    "2,75",
                    "2,5"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Ta có $\\frac{3}{4} = 0,75$, do đó $2\\frac{3}{4} = 2 + 0,75 = 2,75$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Tính bằng cách hợp lý nhất:\na) $\\frac{4}{9} + \\frac{3}{7} + \\frac{5}{9} + \\frac{4}{7}$\nb) $\\frac{5}{8} \\times \\frac{7}{12} + \\frac{5}{8} \\times \\frac{5}{12}$",
                "solution": "Bài giải:\na) $\\frac{4}{9} + \\frac{3}{7} + \\frac{5}{9} + \\frac{4}{7} = (\\frac{4}{9} + \\frac{5}{9}) + (\\frac{3}{7} + \\frac{4}{7}) = \\frac{9}{9} + \\frac{7}{7} = 1 + 1 = 2$\nb) $\\frac{5}{8} \\times \\frac{7}{12} + \\frac{5}{8} \\times \\frac{5}{12} = \\frac{5}{8} \\times (\\frac{7}{12} + \\frac{5}{12}) = \\frac{5}{8} \\times \\frac{12}{12} = \\frac{5}{8} \\times 1 = \\frac{5}{8}$\nĐáp số: a) 2; b) $\\frac{5}{8}$",
                "answer": "a) 2; b) 5/8",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Viết số thập phân thích hợp vào chỗ chấm:\na) $7\\text{ km } 45\\text{ m} = ..........\\text{ km}$\nb) $8\\text{ tạ } 5\\text{ kg} = ..........\\text{ tạ}$\nc) $14\\text{ m}^2\\text{ } 8\\text{ dm}^2 = ..........\\text{ m}^2$\nd) $750\\text{ m} = ..........\\text{ km}$",
                "solution": "Bài giải:\na) $7\\text{ km } 45\\text{ m} = 7\\frac{45}{1000}\\text{ km} = 7,045\\text{ km}$\nb) $8\\text{ tạ } 5\\text{ kg} = 8\\frac{5}{100}\\text{ tạ} = 8,05\\text{ tạ}$\nc) $14\\text{ m}^2\\text{ } 8\\text{ dm}^2 = 14\\frac{8}{100}\\text{ m}^2 = 14,08\\text{ m}^2$\nd) $750\\text{ m} = \\frac{750}{1000}\\text{ km} = 0,75\\text{ km}$\nĐáp số: a) 7,045; b) 8,05; c) 14,08; d) 0,75",
                "answer": "a) 7,045 km; b) 8,05 tạ; c) 14,08 m²; d) 0,75 km",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x : \\frac{4}{7} = \\frac{21}{16}$",
                "solution": "Bài giải:\n$x : \\frac{4}{7} = \\frac{21}{16}$\n$x = \\frac{21}{16} \\times \\frac{4}{7}$\n$x = \\frac{21 \\times 4}{16 \\times 7} = \\frac{3 \\times 1}{4 \\times 1} = \\frac{3}{4}$\nĐáp số: $x = \\frac{3}{4}$",
                "answer": "x = 3/4",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Một xưởng may nhập về tất cả 540 m vải gồm vải hoa và vải trắng. Biết rằng số mét vải trắng bằng $\\frac{4}{5}$ số mét vải hoa. Hỏi xưởng may đã nhập về bao nhiêu mét vải mỗi loại?",
                "solution": "Bài giải:\nTheo sơ đồ, tổng số phần bằng nhau là:\n$4 + 5 = 9$ (phần)\nSố mét vải trắng xưởng đã nhập là:\n$540 : 9 \\times 4 = 240$ (m)\nSố mét vải hoa xưởng đã nhập là:\n$540 - 240 = 300$ (m)\nĐáp số: Vải trắng: 240 m; Vải hoa: 300 m.",
                "answer": "Trắng: 240 m; Hoa: 300 m",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Trong một vườn ươm, số cây cam ít hơn số cây bưởi là 120 cây. Biết rằng số cây cam bằng $\\frac{3}{7}$ số cây bưởi. Tính số cây mỗi loại có trong vườn ươm đó.",
                "solution": "Bài giải:\nTheo sơ đồ, hiệu số phần bằng nhau là:\n$7 - 3 = 4$ (phần)\nSố cây cam trong vườn ươm là:\n$120 : 4 \\times 3 = 90$ (cây)\nSố cây bưởi trong vườn ươm là:\n$90 + 120 = 210$ (cây)\nĐáp số: Cây cam: 90 cây; Cây bưởi: 210 cây.",
                "answer": "Cam: 90 cây; Bưởi: 210 cây",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tìm chữ số $x$ để số thập phân $45,8x6 < 45,836$ và $x$ là chữ số chẵn lớn hơn 0.",
                "solution": "Bài giải:\nSo sánh hai số thập phân $45,8x6$ và $45,836$:\n- Phần nguyên bằng nhau: $45 = 45$.\n- Hàng phần mười bằng nhau: $8 = 8$.\n- Hàng phần nghìn bằng nhau: $6 = 6$.\nĐể $45,8x6 < 45,836$ thì chữ số ở hàng phần trăm phải thỏa mãn: $x < 3$.\nVì $x$ là chữ số chẵn lớn hơn 0 nên $x$ chỉ có thể là 2.\nVậy $x = 2$.\nĐáp số: $x = 2$.",
                "answer": "x = 2",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 06 (th5_gk1_de06)
    # Chủ đề: Đội xe tải vận chuyển hàng cứu trợ đồng bào lũ lụt
    # =========================================================================
    exams["th5_gk1_de06"] = {
        "id": "th5_gk1_de06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 6)",
        "grade": "5",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Số thập phân 12,059 gồm có:",
                "options": [
                    "12 đơn vị, 5 phần mười, 9 phần trăm",
                    "12 đơn vị, 5 phần trăm, 9 phần nghìn",
                    "12 đơn vị, 5 phần mười, 9 phần nghìn",
                    "12 đơn vị, 59 phần trăm"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Phần nguyên là 12 đơn vị; phần thập phân có: 0 phần mười, 5 phần trăm, 9 phần nghìn."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Phân số nào sau đây bằng phân số $\\frac{3}{5}$?",
                "options": [
                    "$\\frac{9}{15}$",
                    "$\\frac{6}{12}$",
                    "$\\frac{12}{25}$",
                    "$\\frac{15}{20}$"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Nhân cả tử và mẫu với 3: $\\frac{3 \\times 3}{5 \\times 3} = \\frac{9}{15}$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Làm tròn số thập phân 78,45 đến hàng đơn vị ta được:",
                "options": [
                    "78",
                    "79",
                    "78,4",
                    "78,5"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Chữ số hàng phần mười là 4 ($< 5$) nên giữ nguyên hàng đơn vị là 78."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Đổi $3\\text{ kg } 25\\text{ g}$ sang đơn vị ki-lô-gam ta được kết quả là:",
                "options": [
                    "3,25 kg",
                    "3,025 kg",
                    "3,250 kg",
                    "30,25 kg"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "$25\\text{ g} = \\frac{25}{1000}\\text{ kg} = 0,025\\text{ kg}$, do đó $3\\text{ kg } 25\\text{ g} = 3,025\\text{ kg}$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Kết quả của phép trừ $\\frac{7}{10} - \\frac{2}{5}$ là:",
                "options": [
                    "$\\frac{5}{5}$",
                    "$\\frac{3}{10}$",
                    "$\\frac{5}{10}$",
                    "$\\frac{1}{2}$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Quy đồng mẫu số: $\\frac{7}{10} - \\frac{4}{10} = \\frac{3}{10}$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Tổng của hai số là 150. Biết số lớn gấp 4 lần số bé. Số lớn là:",
                "options": [
                    "30",
                    "60",
                    "90",
                    "120"
                ],
                "correct": 3,
                "points": 0.5,
                "explanation": "Tổng số phần bằng nhau: $1 + 4 = 5$ phần. Số lớn là: $150 : 5 \\times 4 = 120$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Thực hiện phép tính:\na) $\\frac{2}{3} + \\frac{5}{6} \\times \\frac{4}{5}$\nb) $(\\frac{7}{8} - \\frac{1}{4}) : \\frac{5}{8}$",
                "solution": "Bài giải:\na) $\\frac{2}{3} + \\frac{5}{6} \\times \\frac{4}{5} = \\frac{2}{3} + \\frac{5 \\times 4}{6 \\times 5} = \\frac{2}{3} + \\frac{2}{3} = \\frac{4}{3}$\nb) $(\\frac{7}{8} - \\frac{1}{4}) : \\frac{5}{8} = (\\frac{7}{8} - \\frac{2}{8}) : \\frac{5}{8} = \\frac{5}{8} : \\frac{5}{8} = 1$\nĐáp số: a) $\\frac{4}{3}$; b) 1",
                "answer": "a) 4/3; b) 1",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Viết số thập phân thích hợp vào chỗ chấm:\na) $25\\text{ m } 8\\text{ dm} = ..........\\text{ m}$\nb) $6\\text{ tấn } 50\\text{ kg} = ..........\\text{ tấn}$\nc) $9\\text{ m}^2\\text{ } 4\\text{ dm}^2 = ..........\\text{ m}^2$\nd) $84\\text{ dm} = ..........\\text{ m}$",
                "solution": "Bài giải:\na) $25\\text{ m } 8\\text{ dm} = 25\\frac{8}{10}\\text{ m} = 25,8\\text{ m}$\nb) $6\\text{ tấn } 50\\text{ kg} = 6\\frac{50}{1000}\\text{ tấn} = 6,05\\text{ tấn}$\nc) $9\\text{ m}^2\\text{ } 4\\text{ dm}^2 = 9\\frac{4}{100}\\text{ m}^2 = 9,04\\text{ m}^2$\nd) $84\\text{ dm} = \\frac{84}{10}\\text{ m} = 8,4\\text{ m}$\nĐáp số: a) 25,8; b) 6,05; c) 9,04; d) 8,4",
                "answer": "a) 25,8 m; b) 6,05 tấn; c) 9,04 m²; d) 8,4 m",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$\\frac{15}{8} - x = \\frac{3}{4}$",
                "solution": "Bài giải:\n$\\frac{15}{8} - x = \\frac{3}{4}$\n$x = \\frac{15}{8} - \\frac{3}{4}$\n$x = \\frac{15}{8} - \\frac{6}{8}$\n$x = \\frac{9}{8}$\nĐáp số: $x = \\frac{9}{8}$",
                "answer": "x = 9/8",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Một đoàn xe tải chở hàng cứu trợ gồm hai tổ xe chở tất cả 350 tấn hàng. Tổ xe thứ nhất chở được số tấn hàng bằng $\\frac{3}{4}$ tổ xe thứ hai. Hỏi mỗi tổ xe chở được bao nhiêu tấn hàng?",
                "solution": "Bài giải:\nTheo sơ đồ, tổng số phần bằng nhau là:\n$3 + 4 = 7$ (phần)\nSố tấn hàng tổ thứ nhất chở được là:\n$350 : 7 \\times 3 = 150$ (tấn)\nSố tấn hàng tổ thứ hai chở được là:\n$350 - 150 = 200$ (tấn)\nĐáp số: Tổ một: 150 tấn; Tổ hai: 200 tấn.",
                "answer": "Tổ 1: 150 tấn; Tổ 2: 200 tấn",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Mẹ mua thịt và cá hết tất cả 240 000 đồng. Số tiền mua cá bằng $\\frac{3}{5}$ số tiền mua thịt.\na) Hỏi mẹ mua mỗi loại hết bao nhiêu tiền?\nb) Số tiền mua thịt nhiều hơn số tiền mua cá bao nhiêu đồng?",
                "solution": "Bài giải:\na) Theo sơ đồ, tổng số phần bằng nhau là:\n$3 + 5 = 8$ (phần)\nSố tiền mẹ mua cá là:\n$240 000 : 8 \\times 3 = 90 000$ (đồng)\nSố tiền mẹ mua thịt là:\n$240 000 - 90 000 = 150 000$ (đồng)\nb) Tiền mua thịt nhiều hơn tiền mua cá là:\n$150 000 - 90 000 = 60 000$ (đồng)\nĐáp số: a) Cá: 90 000 đồng, Thịt: 150 000 đồng; b) 60 000 đồng.",
                "answer": "a) Cá: 90 000 đ, Thịt: 150 000 đ; b) 60 000 đ",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Cho biểu thức $C = \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16} + \\frac{1}{32}$. Tính nhanh giá trị của $C$.",
                "solution": "Bài giải:\nNhân cả hai vế của biểu thức với 2, ta có:\n$2 \\times C = 2 \\times (\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16} + \\frac{1}{32})$\n$2 \\times C = 1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16}$\nLấy biểu thức mới trừ đi biểu thức ban đầu:\n$2 \\times C - C = (1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16}) - (\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16} + \\frac{1}{32})$\n$C = 1 - \\frac{1}{32} = \\frac{31}{32}$\nĐáp số: $C = \\frac{31}{32}$",
                "answer": "C = 31/32",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 07 (th5_gk1_de07)
    # Chủ đề: Khu nuôi trồng thủy sản đầm tôm cá
    # =========================================================================
    exams["th5_gk1_de07"] = {
        "id": "th5_gk1_de07",
        "testNum": 7,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 7)",
        "grade": "5",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Số thập phân gồm \"8 đơn vị, 4 phần trăm\" được viết là:",
                "options": [
                    "8,4",
                    "8,04",
                    "8,40",
                    "8,004"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Hàng đơn vị là 8, hàng phần mười là 0, hàng phần trăm là 4 nên viết là 8,04."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Chữ số 6 trong số thập phân 29,165 có giá trị là:",
                "options": [
                    "$\\frac{6}{10}$",
                    "$\\frac{6}{100}$",
                    "$\\frac{6}{1000}$",
                    "6"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Chữ số 6 ở vị trí thứ hai sau dấu phẩy nên thuộc hàng phần trăm, giá trị là $\\frac{6}{100}$."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Điền dấu thích hợp vào chỗ chấm: $4,509 ..... 4,51$",
                "options": [
                    "$<$",
                    "$>$",
                    "$=$",
                    "Không so sánh được"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "Phần nguyên bằng 4, hàng phần mười bằng 5. So sánh hàng phần trăm: $0 < 1$, nên $4,509 < 4,51$."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Rút gọn phân số thập phân $\\frac{75}{100}$ về phân số tối giản ta được:",
                "options": [
                    "$\\frac{15}{20}$",
                    "$\\frac{3}{5}$",
                    "$\\frac{3}{4}$",
                    "$\\frac{7}{10}$"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "Chia cả tử và mẫu cho 25: $\\frac{75 : 25}{100 : 25} = \\frac{3}{4}$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Tìm $x$ biết $x \\times \\frac{2}{3} = \\frac{8}{9}$. Giá trị của $x$ là:",
                "options": [
                    "$\\frac{4}{3}$",
                    "$\\frac{3}{4}$",
                    "$\\frac{16}{27}$",
                    "$\\frac{10}{12}$"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "$x = \\frac{8}{9} : \\frac{2}{3} = \\frac{8}{9} \\times \\frac{3}{2} = \\frac{4}{3}$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Một hình bình hành có độ dài đáy là 16 cm và chiều cao là 9 cm. Diện tích của hình bình hành đó là:",
                "options": [
                    "72 $\\text{cm}^2$",
                    "144 $\\text{cm}^2$",
                    "50 $\\text{cm}^2$",
                    "25 $\\text{cm}^2$"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Diện tích hình bình hành bằng đáy nhân chiều cao: $16 \\times 9 = 144$ $\\text{cm}^2$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Tính giá trị các biểu thức sau:\na) $\\frac{5}{12} + \\frac{3}{8}$\nb) $\\frac{7}{10} : \\frac{14}{25}$",
                "solution": "Bài giải:\na) $\\frac{5}{12} + \\frac{3}{8} = \\frac{10}{24} + \\frac{9}{24} = \\frac{19}{24}$\nb) $\\frac{7}{10} : \\frac{14}{25} = \\frac{7}{10} \\times \\frac{25}{14} = \\frac{7 \\times 25}{10 \\times 14} = \\frac{1 \\times 5}{2 \\times 2} = \\frac{5}{4}$\nĐáp số: a) $\\frac{19}{24}$; b) $\\frac{5}{4}$",
                "answer": "a) 19/24; b) 5/4",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Viết số thập phân thích hợp vào chỗ chấm:\na) $18\\text{ m } 4\\text{ dm} = ..........\\text{ m}$\nb) $4\\text{ tấn } 8\\text{ tạ} = ..........\\text{ tấn}$\nc) $6\\text{ m}^2\\text{ } 35\\text{ dm}^2 = ..........\\text{ m}^2$\nd) $95\\text{ cm} = ..........\\text{ m}$",
                "solution": "Bài giải:\na) $18\\text{ m } 4\\text{ dm} = 18\\frac{4}{10}\\text{ m} = 18,4\\text{ m}$\nb) $4\\text{ tấn } 8\\text{ tạ} = 4\\frac{8}{10}\\text{ tấn} = 4,8\\text{ tấn}$\nc) $6\\text{ m}^2\\text{ } 35\\text{ dm}^2 = 6\\frac{35}{100}\\text{ m}^2 = 6,35\\text{ m}^2$\nd) $95\\text{ cm} = \\frac{95}{100}\\text{ m} = 0,95\\text{ m}$\nĐáp số: a) 18,4; b) 4,8; c) 6,35; d) 0,95",
                "answer": "a) 18,4 m; b) 4,8 tấn; c) 6,35 m²; d) 0,95 m",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$\\frac{5}{6} - x = \\frac{1}{4}$",
                "solution": "Bài giải:\n$\\frac{5}{6} - x = \\frac{1}{4}$\n$x = \\frac{5}{6} - \\frac{1}{4}$\n$x = \\frac{10}{12} - \\frac{3}{12}$\n$x = \\frac{7}{12}$\nĐáp số: $x = \\frac{7}{12}$",
                "answer": "x = 7/12",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Một đầm nuôi thủy sản thu hoạch được 560 kg tôm và cá. Biết số ki-lô-gam tôm bằng $\\frac{2}{5}$ số ki-lô-gam cá. Hỏi đầm đó thu hoạch được bao nhiêu ki-lô-gam tôm, bao nhiêu ki-lô-gam cá?",
                "solution": "Bài giải:\nTheo sơ đồ, tổng số phần bằng nhau là:\n$2 + 5 = 7$ (phần)\nKhối lượng tôm thu hoạch được là:\n$560 : 7 \\times 2 = 160$ (kg)\nKhối lượng cá thu hoạch được là:\n$560 - 160 = 400$ (kg)\nĐáp số: Tôm: 160 kg; Cá: 400 kg.",
                "answer": "Tôm: 160 kg; Cá: 400 kg",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một thửa ruộng hình chữ nhật có chu vi là 200 m. Chiều rộng bằng $\\frac{2}{3}$ chiều dài.\na) Tính chiều dài và chiều rộng của thửa ruộng đó.\nb) Người ta cấy lúa trên thửa ruộng, cứ $100\\text{ m}^2$ thu hoạch được 60 kg thóc. Hỏi trên cả thửa ruộng người ta thu hoạch được bao nhiêu tạ thóc?",
                "solution": "Bài giải:\na) Nửa chu vi thửa ruộng là:\n$200 : 2 = 100$ (m)\nTheo sơ đồ, tổng số phần bằng nhau là:\n$2 + 3 = 5$ (phần)\nChiều rộng của thửa ruộng là:\n$100 : 5 \\times 2 = 40$ (m)\nChiều dài của thửa ruộng là:\n$100 - 40 = 60$ (m)\nb) Diện tích thửa ruộng là:\n$60 \\times 40 = 2400$ ($\\text{m}^2$)\nSố thóc thu hoạch được trên cả thửa ruộng là:\n$2400 : 100 \\times 60 = 1440$ (kg)\nĐổi $1440\\text{ kg} = 14,4\\text{ tạ}$\nĐáp số: a) Dài: 60 m, Rộng: 40 m; b) 14,4 tạ thóc.",
                "answer": "a) Dài: 60 m, Rộng: 40 m; b) 14,4 tạ thóc",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Tìm phân số $\\frac{a}{b}$ biết rằng nếu cộng thêm 4 vào tử số và giữ nguyên mẫu số thì được phân số mới bằng 1; còn nếu bớt 2 ở tử số và giữ nguyên mẫu số thì được phân số mới bằng $\\frac{1}{2}$.",
                "solution": "Bài giải:\nVì cộng 4 vào tử số và giữ nguyên mẫu số thì bằng 1, nên mẫu số hơn tử số 4 đơn vị:\n$b - a = 4$ hay $b = a + 4$\nKhi bớt 2 ở tử số thì tử số mới là $a - 2$. Phân số mới bằng $\\frac{1}{2}$ nghĩa là mẫu số gấp đôi tử số mới:\n$b = 2 \\times (a - 2)$\nDo đó:\n$a + 4 = 2 \\times a - 4$\n$2 \\times a - a = 4 + 4$\n$a = 8$\nMẫu số là:\n$b = 8 + 4 = 12$\nPhân số cần tìm là: $\\frac{8}{12}$ (rút gọn thành $\\frac{2}{3}$).\nĐáp số: $\\frac{8}{12}$",
                "answer": "8/12 (hoặc 2/3)",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08 (th5_gk1_de08)
    # Chủ đề: Dự án trường học xanh và bóng đèn năng lượng
    # =========================================================================
    exams["th5_gk1_de08"] = {
        "id": "th5_gk1_de08",
        "testNum": 8,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 1 - TOÁN 5 (ĐỀ SỐ 8)",
        "grade": "5",
        "term": "gk1",
        "termName": "Giữa Học kì 1",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "question": "**Câu 1:** Số thập phân gồm \"3 chục, 7 đơn vị, 2 phần mười, 5 phần nghìn\" viết là:",
                "options": [
                    "37,25",
                    "37,205",
                    "37,025",
                    "307,25"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Phần nguyên là 37; phần thập phân có 2 phần mười, 0 phần trăm, 5 phần nghìn nên viết là 37,205."
            },
            {
                "id": 2,
                "question": "**Câu 2:** Hàng lớn nhất trong phần thập phân của số thập phân là:",
                "options": [
                    "Hàng đơn vị",
                    "Hàng phần mười",
                    "Hàng phần trăm",
                    "Hàng phần nghìn"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Trong phần thập phân, hàng phần mười là hàng liền sau dấu phẩy và có giá trị lớn nhất (1 phần mười = 10 phần trăm = 100 phần nghìn)."
            },
            {
                "id": 3,
                "question": "**Câu 3:** Trong các số thập phân 18,25; 18,52; 18,052; 18,502; số lớn nhất là:",
                "options": [
                    "18,25",
                    "18,52",
                    "18,052",
                    "18,502"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Phần nguyên bằng 18. So sánh hàng phần mười: 5 lớn nhất. So sánh 18,52 và 18,502 ở hàng phần trăm: $2 > 0$ nên 18,52 là số lớn nhất."
            },
            {
                "id": 4,
                "question": "**Câu 4:** Chuyển hỗn số $5\\frac{1}{4}$ thành số thập phân ta được:",
                "options": [
                    "5,14",
                    "5,41",
                    "5,25",
                    "5,5"
                ],
                "correct": 2,
                "points": 0.5,
                "explanation": "$\\frac{1}{4} = 0,25$, do đó $5\\frac{1}{4} = 5,25$."
            },
            {
                "id": 5,
                "question": "**Câu 5:** Kết quả của phép chia $\\frac{4}{9} : \\frac{8}{15}$ rút gọn là:",
                "options": [
                    "$\\frac{5}{6}$",
                    "$\\frac{6}{5}$",
                    "$\\frac{32}{135}$",
                    "$\\frac{2}{3}$"
                ],
                "correct": 0,
                "points": 0.5,
                "explanation": "$\\frac{4}{9} : \\frac{8}{15} = \\frac{4}{9} \\times \\frac{15}{8} = \\frac{4 \\times 15}{9 \\times 8} = \\frac{1 \\times 5}{3 \\times 2} = \\frac{5}{6}$."
            },
            {
                "id": 6,
                "question": "**Câu 6:** Hiệu hai số là 65, số lớn gấp 6 lần số bé. Số bé là:",
                "options": [
                    "11",
                    "13",
                    "15",
                    "18"
                ],
                "correct": 1,
                "points": 0.5,
                "explanation": "Hiệu số phần bằng nhau: $6 - 1 = 5$ phần. Số bé là: $65 : 5 = 13$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "question": "**Bài 1:** Tính giá trị các biểu thức sau:\na) $\\frac{3}{5} \\times \\frac{10}{9} + \\frac{1}{3}$\nb) $\\frac{7}{6} - \\frac{3}{4} : \\frac{9}{8}$",
                "solution": "Bài giải:\na) $\\frac{3}{5} \\times \\frac{10}{9} + \\frac{1}{3} = \\frac{3 \\times 10}{5 \\times 9} + \\frac{1}{3} = \\frac{2}{3} + \\frac{1}{3} = \\frac{3}{3} = 1$\nb) $\\frac{7}{6} - \\frac{3}{4} : \\frac{9}{8} = \\frac{7}{6} - (\\frac{3}{4} \\times \\frac{8}{9}) = \\frac{7}{6} - \\frac{2}{3} = \\frac{7}{6} - \\frac{4}{6} = \\frac{3}{6} = \\frac{1}{2}$\nĐáp số: a) 1; b) $\\frac{1}{2}$",
                "answer": "a) 1; b) 1/2",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 2,
                "question": "**Bài 2:** Viết số thập phân thích hợp vào chỗ chấm:\na) $34\\text{ m } 5\\text{ cm} = ..........\\text{ m}$\nb) $5\\text{ tấn } 6\\text{ kg} = ..........\\text{ tấn}$\nc) $12\\text{ m}^2\\text{ } 45\\text{ dm}^2 = ..........\\text{ m}^2$\nd) $680\\text{ m} = ..........\\text{ km}$",
                "solution": "Bài giải:\na) $34\\text{ m } 5\\text{ cm} = 34\\frac{5}{100}\\text{ m} = 34,05\\text{ m}$\nb) $5\\text{ tấn } 6\\text{ kg} = 5\\frac{6}{1000}\\text{ tấn} = 5,006\\text{ tấn}$\nc) $12\\text{ m}^2\\text{ } 45\\text{ dm}^2 = 12\\frac{45}{100}\\text{ m}^2 = 12,45\\text{ m}^2$\nd) $680\\text{ m} = \\frac{680}{1000}\\text{ km} = 0,68\\text{ km}$\nĐáp số: a) 34,05; b) 5,006; c) 12,45; d) 0,68",
                "answer": "a) 34,05 m; b) 5,006 tấn; c) 12,45 m²; d) 0,68 km",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 3,
                "question": "**Bài 3:** Tìm $x$, biết:\n$x \\times \\frac{5}{7} = \\frac{15}{28}$",
                "solution": "Bài giải:\n$x \\times \\frac{5}{7} = \\frac{15}{28}$\n$x = \\frac{15}{28} : \\frac{5}{7}$\n$x = \\frac{15}{28} \\times \\frac{7}{5}$\n$x = \\frac{15 \\times 7}{28 \\times 5} = \\frac{3 \\times 1}{4 \\times 1} = \\frac{3}{4}$\nĐáp số: $x = \\frac{3}{4}$",
                "answer": "x = 3/4",
                "lineCount": 4,
                "points": 1.0
            },
            {
                "id": 4,
                "question": "**Bài 4:** Một trường học lắp đặt 420 bóng đèn tiết kiệm điện gồm đèn LED và đèn huỳnh quang. Số bóng đèn huỳnh quang bằng $\\frac{2}{5}$ số bóng đèn LED. Hỏi trường học đó đã lắp đặt bao nhiêu bóng đèn mỗi loại?",
                "solution": "Bài giải:\nTheo sơ đồ, tổng số phần bằng nhau là:\n$2 + 5 = 7$ (phần)\nSố bóng đèn huỳnh quang là:\n$420 : 7 \\times 2 = 120$ (bóng)\nSố bóng đèn LED là:\n$420 - 120 = 300$ (bóng)\nĐáp số: Đèn huỳnh quang: 120 bóng; Đèn LED: 300 bóng.",
                "answer": "Huỳnh quang: 120 bóng; LED: 300 bóng",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 5,
                "question": "**Bài 5:** Một kho thóc có số thóc nếp ít hơn số thóc tẻ là 84 tạ. Biết số thóc nếp bằng $\\frac{4}{7}$ số thóc tẻ.\na) Tính số thóc mỗi loại có trong kho.\nb) Người ta đã xuất bán đi một nửa số thóc tẻ. Hỏi trong kho còn lại tất cả bao nhiêu tạ thóc cả hai loại?",
                "solution": "Bài giải:\na) Theo sơ đồ, hiệu số phần bằng nhau là:\n$7 - 4 = 3$ (phần)\nSố thóc nếp trong kho là:\n$84 : 3 \\times 4 = 112$ (tạ)\nSố thóc tẻ trong kho là:\n$112 + 84 = 196$ (tạ)\nb) Số thóc tẻ còn lại sau khi bán một nửa là:\n$196 : 2 = 98$ (tạ)\nSố thóc cả hai loại còn lại trong kho là:\n$112 + 98 = 210$ (tạ)\nĐáp số: a) Thóc nếp: 112 tạ; Thóc tẻ: 196 tạ; b) 210 tạ thóc.",
                "answer": "a) Nếp: 112 tạ, Tẻ: 196 tạ; b) Còn lại: 210 tạ",
                "lineCount": 6,
                "points": 1.5
            },
            {
                "id": 6,
                "question": "**Bài 6:** Cho dãy số phân số: $\\frac{1}{2}; \\frac{1}{6}; \\frac{1}{12}; \\frac{1}{20}; \\frac{1}{30}; ...$ Tính tổng của 6 phân số đầu tiên của dãy số đó.",
                "solution": "Bài giải:\nTa nhận thấy quy luật của mẫu số các phân số trong dãy:\n$\\frac{1}{2} = \\frac{1}{1 \\times 2}$\n$\\frac{1}{6} = \\frac{1}{2 \\times 3}$\n$\\frac{1}{12} = \\frac{1}{3 \\times 4}$\n$\\frac{1}{20} = \\frac{1}{4 \\times 5}$\n$\\frac{1}{30} = \\frac{1}{5 \\times 6}$\nPhân số thứ 6 của dãy là: $\\frac{1}{6 \\times 7} = \\frac{1}{42}$.\nTổng 6 phân số đầu tiên là:\n$S = \\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\frac{1}{3 \\times 4} + \\frac{1}{4 \\times 5} + \\frac{1}{5 \\times 6} + \\frac{1}{6 \\times 7}$\n$S = (1 - \\frac{1}{2}) + (\\frac{1}{2} - \\frac{1}{3}) + ... + (\\frac{1}{6} - \\frac{1}{7})$\n$S = 1 - \\frac{1}{7} = \\frac{6}{7}$\nĐáp số: $\\frac{6}{7}$",
                "answer": "S = 6/7",
                "lineCount": 5,
                "points": 1.0
            }
        ]
    }

    return exams


if __name__ == "__main__":
    exams = get_th5_gk1_exams()
    print(f"Tổng số đề GK1: {len(exams)}")
    for eid, ex in exams.items():
        print(f"- {eid}: {ex['title']} | TN: {len(ex['part1'])} câu | TL: {len(ex['part2'])} bài")
