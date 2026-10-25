# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG II: SỐ THỰC
PHẦN 2:
- BÀI 7: TẬP HỢP CÁC SỐ THỰC (c2_7_bai3)
- BÀI KIỂM TRA CUỐI CHƯƠNG II: SỐ THỰC (c2_7_bai4)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 7: TẬP HỢP CÁC SỐ THỰC (c2_7_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c2_7_bai3_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 7: Tập hợp các số thực - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tập hợp các số thực bao gồm:", "options": ["Số hữu tỉ và số vô tỉ", "Chỉ các số hữu tỉ", "Chỉ các số vô tỉ", "Số tự nhiên và số nguyên"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Tập hợp các số thực được kí hiệu là:", "options": ["$\\mathbb{R}$", "$\\mathbb{Q}$", "$\\mathbb{I}$", "$\\mathbb{Z}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Số đối của số thực $-\\sqrt{5}$ là:", "options": ["$\\sqrt{5}$", "$-\\sqrt{5}$", "$5$", "$-5$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Giá trị tuyệt đối của số thực $x$ (kí hiệu $|x|$) là:", "options": ["Khoảng cách từ điểm $x$ đến điểm gốc 0 trên trục số", "Chính số $x$", "Số đối của $x$", "Bình phương của $x$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Giá trị của $|-3,5|$ là:", "options": ["$3,5$", "$-3,5$", "$0$", "$7$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Khẳng định nào sau đây là SAI?", "options": ["$\\mathbb{R} \\subset \\mathbb{Q}$", "$\\mathbb{Q} \\subset \\mathbb{R}$", "$\\mathbb{I} \\subset \\mathbb{R}$", "$\\mathbb{Z} \\subset \\mathbb{R}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "So sánh hai số thực $-1,41$ và $-\\sqrt{2}$:", "options": ["$-1,41 > -\\sqrt{2}$", "$-1,41 < -\\sqrt{2}$", "$-1,41 = -\\sqrt{2}$", "Không so sánh được"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tìm $x$ biết $|x| = 2,5$:", "options": ["$x = 2,5$ hoặc $x = -2,5$", "$x = 2,5$", "$x = -2,5$", "$x = 5$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Trong các số sau: $-3;\\ 0;\\ \\sqrt{2};\\ -\\frac{5}{2};\\ \\pi$, có bao nhiêu số thực dương?", "options": ["$2$", "$3$", "$1$", "$4$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Sắp xếp theo thứ tự giảm dần: $-2;\\ 0;\\ \\sqrt{5};\\ -\\frac{7}{3}$:", "options": ["$\\sqrt{5} > 0 > -2 > -\\frac{7}{3}$", "$\\sqrt{5} > 0 > -\\frac{7}{3} > -2$", "$0 > \\sqrt{5} > -2 > -\\frac{7}{3}$", "$-\\frac{7}{3} > -2 > 0 > \\sqrt{5}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Giá trị của biểu thức $|-\\sqrt{9}| + |4|$ là:", "options": ["$7$", "$1$", "$-7$", "$-1$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Điểm biểu diễn các số thực lấp đầy:", "options": ["Toàn bộ trục số", "Chỉ các điểm chia hết", "Chỉ nửa trục số dương", "Chỉ các số nguyên"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho các mệnh đề về tập hợp số thực:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Mỗi số thực được biểu diễn bởi một điểm duy nhất trên trục số.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Ngược lại, mỗi điểm trên trục số đều biểu diễn đúng một số thực.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu x là số vô tỉ thì x không thể là số thực.", "correct": False},
                {"key": "d", "level": "Thông hiểu", "text": "Giao của tập số hữu tỉ Q và tập số vô tỉ I là tập rỗng.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai số thực x = -√3 và y = -1,732:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "x là một số vô tỉ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "y là một số hữu tỉ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "|x| = √3 và |y| = 1,732.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Hai số x và y hoàn toàn bằng nhau.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm giá trị của: A = | -2,8 | + | 3,2 |.", "answer": "6"},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu số nguyên x thỏa mãn: -√10 < x < √10?", "answer": "7"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số thực x biết: |x - 1,5| = 0.", "answer": "1,5"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho x = -√7. Tính giá trị của biểu thức M = |x| - √7.", "answer": "0"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Tìm số đối của mỗi số sau: -3,2 ; √5 ; -1/3 ; π.\nb) Tìm giá trị tuyệt đối của mỗi số sau: -7,5 ; √2 ; -√11 ; 0.",
            "rubric": "a) Số đối lần lượt là: 3,2 ; -√5 ; 1/3 ; -π (0.5đ).\nb) Giá trị tuyệt đối lần lượt là: 7,5 ; √2 ; √11 ; 0 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "So sánh các cặp số thực sau:\na) √11 và 3\nb) -2,65 và -√7\nc) 0,(3) và 1/3.",
            "rubric": "a) Vì 11 > 9 nên √11 > √9 = 3 (0.3đ).\nb) 2,65² = 7,0225 > 7 => 2,65 > √7 => -2,65 < -√7 (0.4đ).\nc) 0,(3) = 3/9 = 1/3. Vậy hai số bằng nhau (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Bác Tư có một mảnh sân hình vuông diện tích 80 m².\na) Tính độ dài cạnh của mảnh sân (viết dưới dạng căn bậc hai số học).\nb) Hãy làm tròn độ dài cạnh mảnh sân đến hàng phần mười để bác Tư mua nẹp nhôm viền sân.",
            "rubric": "a) Cạnh sân: a = √80 m (0.5đ).\nb) Dùng máy tính: √80 ≈ 8,944... Làm tròn đến hàng phần mười: a ≈ 8,9 m (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c2_7_bai3_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 7: Tập hợp các số thực - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $x = -2,5$. Giá trị của biểu thức $P = -|x| + 3,5$ là:", "options": ["$1$", "$6$", "$-1$", "$-6$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $x$ biết $|x - 2| = 3$:", "options": ["$x = 5$ hoặc $x = -1$", "$x = 5$", "$x = -1$", "$x = 1$ hoặc $x = -5$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Trong các số: $-\\sqrt{3};\\ -1,7;\\ 0;\\ \\sqrt{5};\\ 2,236$, số thực nhỏ nhất là:", "options": ["$-\\sqrt{3}$", "$-1,7$", "$0$", "$\\sqrt{5}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm tất cả các giá trị của $x$ thỏa mãn $|x| = -x$:", "options": ["$x \\leq 0$", "$x < 0$", "$x = 0$", "$x \\geq 0$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Giá trị của biểu thức $A = |x - 1| + |2 - x|$ khi $1 \\leq x \\leq 2$ là:", "options": ["$1$", "$2x - 3$", "$3 - 2x$", "Không đổi bằng $3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Số các số nguyên $x$ thỏa mãn $|x| < \\sqrt{17}$ là:", "options": ["$9$", "$8$", "$4$", "$5$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Biểu thức $B = \\sqrt{(2 - \\sqrt{5})^2}$ rút gọn được kết quả là:", "options": ["$\\sqrt{5} - 2$", "$2 - \\sqrt{5}$", "$3$", "$-1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tìm $x$ biết $|2x - 3| - 1 = 4$:", "options": ["$x = 4$ hoặc $x = -1$", "$x = 4$", "$x = -1$", "$x = 3$ hoặc $x = -2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $M = |x - 3,5| + 1,2$:", "options": ["$1,2$", "$3,5$", "$4,7$", "$0$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hai số thực $x, y$ thỏa mãn $|x - 1| + |y + 2| = 0$. Giá trị của $x + y$ là:", "options": ["$-1$", "$1$", "$3$", "$-3$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số nghiệm của phương trình $|x - 1| + |x - 4| = 2$ là:", "options": ["$0$", "$1$", "$2$", "Vô số"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị lớn nhất của biểu thức $Q = 10 - |2x - 6|$ là:", "options": ["$10$", "$6$", "$4$", "Không có giá trị lớn nhất"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai số thực a và b tùy ý:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "|a| ≥ 0 và |a| = |-a| với mọi số thực a.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "|a . b| = |a| . |b| với mọi số thực a, b.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "|a + b| = |a| + |b| với mọi số thực a, b.", "correct": False},
                {"key": "d", "level": "Vận dụng cao", "text": "|a + b| ≤ |a| + |b|, dấu bằng xảy ra khi a và b cùng dấu (a.b ≥ 0).", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm x: |x - 2| = 2x - 1:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Điều kiện để phương trình có nghiệm là 2x - 1 ≥ 0, tức x ≥ 1/2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "TH1: x - 2 = 2x - 1 => x = -1.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "TH2: x - 2 = -(2x - 1) => 3x = 3 => x = 1.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Phương trình có 2 nghiệm phân biệt x = -1 và x = 1.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số nguyên x thỏa mãn: -3 ≤ x < √8. Có bao nhiêu số nguyên x thỏa mãn?", "answer": "6"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm giá trị của x biết: |x - 1/2| = 3/2 và x > 0.", "answer": "2"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính giá trị của biểu thức: A = √( (1 - √2)² ) + √2.", "answer": "1"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: P = |x - 4| + 5.", "answer": "5"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Rút gọn các biểu thức sau:\na) A = √( (3 - √10)² ) + √10\nb) B = |x - 3| - x + 5 với x ≥ 3.",
            "rubric": "a) |3 - √10| + √10. Vì 3 < √10 nên |3 - √10| = √10 - 3. Do đó A = √10 - 3 + √10 = 2√10 - 3 (0.5đ).\nb) Vì x ≥ 3 nên |x - 3| = x - 3. B = x - 3 - x + 5 = 2 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số thực x biết:\na) |2x - 1/3| = 5/6\nb) |x - 1| = 3x - 5.",
            "rubric": "a) 2x - 1/3 = 5/6 => 2x = 7/6 => x = 7/12; hoặc 2x - 1/3 = -5/6 => 2x = -3/6 = -1/2 => x = -1/4 (0.5đ).\nb) Điều kiện 3x - 5 ≥ 0 => x ≥ 5/3. TH1: x - 1 = 3x - 5 => 2x = 4 => x = 2 (nhận). TH2: x - 1 = 5 - 3x => 4x = 6 => x = 3/2 (loại vì < 5/3). Vậy x = 2 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một cột cờ cao 8 m dựng vuông góc với mặt đất. Người ta căng một sợi dây cáp từ đỉnh cột cờ đến một chiếc cọc đóng trên mặt đất cách chân cột cờ 6 m.\na) Tính chiều dài sợi dây cáp đó.\nb) Do gió lớn, cọc bị xê dịch ra xa thêm 2 m nữa (thành 8 m). Hỏi sợi dây cáp cần nối thêm bao nhiêu mét? (Làm tròn đến hàng phần mười).",
            "rubric": "a) Áp dụng định lí Pythagore: chiều dài dây d = √(8² + 6²) = √(64 + 36) = √100 = 10 m (0.5đ).\nb) Chiều dài dây mới: d' = √(8² + 8²) = √128 ≈ 11,31 m. Chiều dài cần nối thêm: 11,31 - 10 = 1,31 ≈ 1,3 m (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c2_7_bai3_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 7: Tập hợp các số thực - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = |x - 1| + |x - 2024|$:", "options": ["$2023$", "$2024$", "$0$", "$1$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Số nghiệm thực của phương trình $|x - 2| + |2x - 4| = 9$ là:", "options": ["$2$", "$1$", "$0$", "Vô số"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Rút gọn biểu thức $M = \\sqrt{7 + 4\\sqrt{3}} - \\sqrt{7 - 4\\sqrt{3}}$ ta được kết quả là:", "options": ["$4$", "$2\\sqrt{3}$", "$2$", "$0$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $x, y$ là các số thực thỏa mãn $(x - 1)^2 + |x + y - 3| = 0$. Giá trị của $x \\cdot y$ là:", "options": ["$2$", "$-2$", "$3$", "$1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Giá trị nhỏ nhất của biểu thức $P = |x - 1| + |x - 2| + |x - 3| + |x - 4|$ là:", "options": ["$4$", "$3$", "$6$", "$5$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Tìm tất cả các số thực $x$ thỏa mãn: $|x + 1| + |x - 2| = 3$:", "options": ["$-1 \\leq x \\leq 2$", "$x = -1$ hoặc $x = 2$", "$x \\geq 2$", "$x \\leq -1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Biết $A = \\sqrt{2 + \\sqrt{2 + \\sqrt{2 + \\dots}}}$ (vô hạn dấu căn). Giá trị của $A$ bằng:", "options": ["$2$", "$\\sqrt{2}$", "$4$", "$1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $a, b, c$ là ba số thực thỏa mãn $a + b + c = 0$ và $a, b, c \\neq 0$. Biểu thức $T = \\frac{|a|}{a} + \\frac{|b|}{b} + \\frac{|c|}{c} + \\frac{|abc|}{abc}$ có thể nhận các giá trị là:", "options": ["$0$", "$4$", "$-4$", "$-2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức $B = \\frac{12}{|x - 2| + 3}$:", "options": ["$4$", "$12$", "$3$", "Không tồn tại"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $x, y$ là các số thực thỏa mãn $|x| + |y| = 1$. Giá trị lớn nhất của $x^2 + y^2$ là:", "options": ["$1$", "$2$", "$\\frac{1}{2}$", "$\\frac{1}{4}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm nghiệm nguyên dương của phương trình: $\\sqrt{x} + \\sqrt{y} = \\sqrt{20}$:", "options": ["$(x; y) = (5; 5)$", "$(x; y) = (4; 16)$", "$(x; y) = (1; 19)$", "Vô nghiệm"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Số các số nguyên $x$ thỏa mãn $\\sqrt{x^2 - 4x + 4} \\leq 3$ là:", "options": ["$7$", "$6$", "$5$", "$8$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức A = |x - 2| + |x - 6| với x là số thực:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "A = |x - 2| + |6 - x| ≥ |x - 2 + 6 - x| = 4.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Giá trị nhỏ nhất của A bằng 4.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Dấu bằng xảy ra khi và chỉ khi 2 ≤ x ≤ 6.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Có đúng 4 giá trị nguyên của x làm cho A đạt giá trị nhỏ nhất.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán giải phương trình |x² - 1| + |x - 1| = 0:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Vì |x² - 1| ≥ 0 và |x - 1| ≥ 0 nên tổng bằng 0 khi cả hai số hạng đồng thời bằng 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "x² - 1 = 0 cho ta x = 1 hoặc x = -1.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "x - 1 = 0 cho ta x = 1.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Phương trình có nghiệm duy nhất là x = 1.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm giá trị nhỏ nhất của biểu thức: P = |x - 2024| + |x - 2026|.", "answer": "2"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số thực x biết: |x - 1| + |2x - 2| = 6 và x > 1.", "answer": "3"},
        {"id": 3, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên x thỏa mãn: |x - 3| + |x + 1| ≤ 6?", "answer": "7"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức: M = 2024 - (x - 1)² - |y + 2|.", "answer": "2024"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Tìm số thực x biết:\na) |3x - 1| = |x + 5|\nb) |2x - 3| + |x - 1| = 4.",
            "rubric": "a) 3x - 1 = x + 5 => 2x = 6 => x = 3; hoặc 3x - 1 = -x - 5 => 4x = -4 => x = -1. Vậy x ∈ {-1; 3} (0.5đ).\nb) Xét các khoảng giá trị chia bởi x = 1 và x = 1,5. Giải ra tìm được x = 8/3 hoặc x = 0 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức:\nA = |x - 1| + |x - 2| + |x - 3|.",
            "rubric": "A = (|x - 1| + |3 - x|) + |x - 2| ≥ |x - 1 + 3 - x| + |x - 2| = 2 + |x - 2| (0.5đ). Vì |x - 2| ≥ 0 nên A ≥ 2. Dấu bằng xảy ra khi (x - 1)(3 - x) ≥ 0 và x - 2 = 0 <=> x = 2. Vậy min A = 2 khi x = 2 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho x, y, z là các số thực thỏa mãn:\n√(x - 1) + √(y - 2) + √(z - 3) = (x + y + z) / 2.\nTìm giá trị của x, y, z.",
            "rubric": "Quy đồng: 2√(x-1) + 2√(y-2) + 2√(z-3) = x + y + z (0.3đ). Chuyển vế tách thành tổng các bình phương: [(x - 1) - 2√(x-1) + 1] + [(y - 2) - 2√(y-2) + 1] + [(z - 3) - 2√(z-3) + 1] = 0 (0.4đ) => (√(x-1) - 1)² + (√(y-2) - 1)² + (√(z-3) - 1)² = 0 => x = 2; y = 3; z = 4 (0.3đ)."
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG II: SỐ THỰC (c2_7_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c2_7_bai4_test1"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương II: Số thực - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Số nào sau đây là số vô tỉ?", "options": ["$\\sqrt{3}$", "$\\sqrt{9}$", "$0,(5)$", "$-\\frac{4}{7}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Căn bậc hai số học của 36 là:", "options": ["$6$", "$-6$", "$\\pm 6$", "$18$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Khẳng định nào sau đây là đúng?", "options": ["$\\sqrt{a}$ có nghĩa khi và chỉ khi $a \\geq 0$", "Số âm cũng có căn bậc hai số học", "$\\sqrt{a^2} = a$ với mọi số thực $a$", "$\\sqrt{0}$ không xác định"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Giá trị tuyệt đối của $-4,7$ là:", "options": ["$4,7$", "$-4,7$", "$0$", "$9,4$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Số đối của $\\sqrt{7}$ là:", "options": ["$-\\sqrt{7}$", "$\\sqrt{7}$", "$7$", "$-7$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Phân số nào sau đây viết được dưới dạng số thập phân hữu hạn?", "options": ["$\\frac{7}{25}$", "$\\frac{5}{6}$", "$\\frac{2}{7}$", "$\\frac{1}{9}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{49} - \\sqrt{16}$ là:", "options": ["$3$", "$7$", "$4$", "$33$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tìm $x$ biết: $\\sqrt{x} = 5$:", "options": ["$x = 25$", "$x = \\pm 25$", "$x = \\sqrt{5}$", "$x = 10$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Làm tròn số $7,846$ đến hàng phần mười được kết quả là:", "options": ["$7,8$", "$7,9$", "$7,85$", "$8$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Số thập phân vô hạn tuần hoàn $0,(5)$ viết dưới dạng phân số tối giản là:", "options": ["$\\frac{5}{9}$", "$\\frac{1}{2}$", "$\\frac{5}{10}$", "$\\frac{5}{99}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "So sánh $\\sqrt{15}$ và $4$:", "options": ["$\\sqrt{15} < 4$", "$\\sqrt{15} > 4$", "$\\sqrt{15} = 4$", "Không so sánh được"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Một hình vuông có diện tích $81\\text{ cm}^2$. Chu vi hình vuông đó là:", "options": ["$36\\text{ cm}$", "$9\\text{ cm}$", "$18\\text{ cm}$", "$81\\text{ cm}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tập hợp các số thực S = {-2; 0; 3/5; √2; -1,2(3); π}:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Các số -2; 0; 3/5; -1,2(3) là các số hữu tỉ.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Các số √2 và π là các số vô tỉ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tất cả các phần tử của S đều là số thực.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Trong tập S có đúng 1 số nguyên.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét các phép tính căn bậc hai số học:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "√(0,09) = 0,3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "√(25/64) = 5/8.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "√(100) + √(36) = 16.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "√(100 - 36) = 10 - 6 = 4.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = √(144) - √(81) + √(9).", "answer": "6"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số thực x biết: |x| = 7 và x < 0.", "answer": "-7"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm x thỏa mãn: √(x + 1) = 3.", "answer": "8"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tính kết quả phép tính: 0,(2) + 0,(7) dưới dạng số tự nhiên.", "answer": "1"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị các biểu thức sau:\na) A = √(0,36) . √(25) + 3/4\nb) B = 2 . √(81) - 3 . √(49) + 4 . √(25).",
            "rubric": "a) A = 0,6 . 5 + 0,75 = 3 + 0,75 = 3,75 (0.5đ).\nb) B = 2 . 9 - 3 . 7 + 4 . 5 = 18 - 21 + 20 = 17 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm x biết:\na) 2√x - 3 = 7\nb) |x - 2,5| = 1,5.",
            "rubric": "a) 2√x = 10 => √x = 5 => x = 25 (0.5đ).\nb) x - 2,5 = 1,5 => x = 4; hoặc x - 2,5 = -1,5 => x = 1. Vậy x ∈ {1; 4} (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một phòng khách hình vuông có diện tích 36 m². Người ta dùng các viên gạch men hình vuông cạnh 60 cm để lát toàn bộ nền phòng khách đó.\na) Tính độ dài cạnh của phòng khách.\nb) Cần bao nhiêu viên gạch men để lát kín nền phòng khách (coi mạch vữa không đáng kể)?",
            "rubric": "a) Cạnh phòng khách: a = √36 = 6 m = 600 cm (0.5đ).\nb) Diện tích 1 viên gạch: 60 x 60 = 3600 cm². Diện tích nền: 36 m² = 360 000 cm². Số viên gạch: 360 000 : 3600 = 100 viên (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c2_7_bai4_test2"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương II: Số thực - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Giá trị của biểu thức $A = \\sqrt{25} - \\sqrt{\\frac{16}{9}} + | -1,5 |$ là:", "options": ["$\\frac{31}{6}$", "$\\frac{23}{6}$", "$5$", "$\\frac{13}{6}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $x$ biết $x^2 = 18$ và $x > 0$:", "options": ["$x = 3\\sqrt{2}$", "$x = 9$", "$x = 6$", "$x = 2\\sqrt{3}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "So sánh hai số thực $a = \\sqrt{29}$ và $b = 5,4$:", "options": ["$a < b$", "$a > b$", "$a = b$", "Không so sánh được"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $\\sqrt{3x - 2} = 4$:", "options": ["$x = 6$", "$x = 2$", "$x = 18$", "$x = 5$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Giá trị của biểu thức $P = \\sqrt{(3 - \\sqrt{7})^2} + \\sqrt{7}$ là:", "options": ["$3$", "$2\\sqrt{7} - 3$", "$6$", "$\\sqrt{7}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Số nghiệm của phương trình $|2x - 1| = x + 2$ là:", "options": ["$2$", "$1$", "$0$", "Vô số"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Làm tròn số $a = 15,3849$ đến chữ số thập phân thứ hai với độ chính xác $d = 0,005$:", "options": ["$15,38$", "$15,39$", "$15,4$", "$15,385$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Một hình chữ nhật có diện tích $45\\text{ cm}^2$, chiều dài gấp 5 lần chiều rộng. Chiều rộng của hình chữ nhật là:", "options": ["$3\\text{ cm}$", "$9\\text{ cm}$", "$\\sqrt{5}\\text{ cm}$", "$5\\text{ cm}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $M = \\sqrt{x - 2} + |y + 1| + 3$:", "options": ["$3$", "$2$", "$0$", "$5$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số các số nguyên $x$ thỏa mãn $\\sqrt{x} < 10$ là:", "options": ["$100$", "$99$", "$10$", "$81$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Giá trị của biểu thức $C = \\frac{\\sqrt{15} + \\sqrt{5}}{\\sqrt{3} + 1}$ là:", "options": ["$\\sqrt{5}$", "$5$", "$\\sqrt{3}$", "$1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $x$ thỏa mãn $|x - 2| + |x - 5| = 3$. Giá trị của $x$ có thể là:", "options": ["Mọi $x$ thỏa mãn $2 \\leq x \\leq 5$", "$x = 2$ hoặc $x = 5$", "$x = 3,5$", "Vô nghiệm"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức A = √(x - 3) + 2:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Biểu thức A xác định khi x ≥ 3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Với x = 7 thì A = 4.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Giá trị nhỏ nhất của A bằng 2 khi x = 3.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "A có thể nhận giá trị bằng 1.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét phương trình |x - 1| = 2x - 3:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Điều kiện để phương trình có nghiệm là 2x - 3 ≥ 0 => x ≥ 1,5.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi x ≥ 1,5 thì x - 1 > 0 nên phương trình trở thành x - 1 = 2x - 3.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nghiệm của phương trình là x = 2.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Phương trình có thêm một nghiệm âm.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: P = √(64) : 2 + √(81) . 1/3.", "answer": "7"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số thực x thỏa mãn: 3√(x) - 4 = 11.", "answer": "25"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm giá trị nhỏ nhất của biểu thức: A = |x - 2,5| + 4.", "answer": "4"},
        {"id": 4, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên dương x thỏa mãn: √x < 6?", "answer": "35"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính hợp lý nếu có thể:\na) A = √(81/16) - √(25/36) : √(25/9)\nb) B = |-4,5| . 2/3 - √(0,16) . 5.",
            "rubric": "a) 9/4 - (5/6) : (5/3) = 9/4 - 1/2 = 9/4 - 2/4 = 7/4 (0.5đ).\nb) 4,5 . 2/3 - 0,4 . 5 = 3 - 2 = 1 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm x biết:\na) √(2x + 5) = 7\nb) |3x - 1| = 2x + 4.",
            "rubric": "a) Điều kiện x ≥ -2,5. 2x + 5 = 49 => 2x = 44 => x = 22 (0.5đ).\nb) Điều kiện 2x + 4 ≥ 0 => x ≥ -2. TH1: 3x - 1 = 2x + 4 => x = 5 (nhận). TH2: 3x - 1 = -2x - 4 => 5x = -3 => x = -3/5 (nhận). Vậy x ∈ {-3/5; 5} (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một kim tự tháp có đáy là hình vuông diện tích 44 100 m².\na) Tính độ dài cạnh đáy của kim tự tháp.\nb) Người ta đi vòng quanh chu vi đáy kim tự tháp với vận tốc 4,2 km/h. Hỏi mất bao nhiêu phút để đi hết 1 vòng quanh đáy kim tự tháp?",
            "rubric": "a) Cạnh đáy kim tự tháp: a = √44100 = 210 m (0.5đ).\nb) Chu vi đáy: 210 x 4 = 840 m = 0,84 km. Thời gian đi: t = 0,84 : 4,2 = 0,2 giờ = 12 phút (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c2_7_bai4_test3"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương II: Số thực - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Rút gọn biểu thức $A = \\sqrt{9 - 4\\sqrt{5}} + \\sqrt{9 + 4\\sqrt{5}}$ ta được:", "options": ["$2\\sqrt{5}$", "$4$", "$\\sqrt{5}$", "$2$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Số nghiệm nguyên của phương trình $\\sqrt{x + 1} + \\sqrt{y - 2} = 0$ là:", "options": ["$1$", "$2$", "$0$", "Vô số"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "So sánh $A = \\sqrt{17} + \\sqrt{8}$ và $B = 7$:", "options": ["$A < B$", "$A > B$", "$A = B$", "Không so sánh được"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ sao cho $\\sqrt{n + 1} + \\sqrt{n} = \\frac{1}{\\sqrt{2025} - \\sqrt{2024}}$:", "options": ["$n = 2024$", "$n = 2025$", "$n = 2023$", "Không tồn tại"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Giá trị nhỏ nhất của biểu thức $P = \\sqrt{x^2 - 2x + 5} + 3$ là:", "options": ["$5$", "$3$", "$\\sqrt{5} + 3$", "$2$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $x$ thỏa mãn $\\sqrt{x} + \\frac{1}{\\sqrt{x}} = 4$. Giá trị của biểu thức $x^2 + \\frac{1}{x^2}$ là:", "options": ["$194$", "$14$", "$196$", "$192$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm tất cả các cặp số thực $(x; y)$ thỏa mãn $\\sqrt{x - 1} + \\sqrt{y - 2} = 2$ và $x + y = 5$:", "options": ["$(x; y) = (2; 3)$", "$(x; y) = (1; 4)$", "$(x; y) = (3; 2)$", "Vô số nghiệm"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên $x$ để phân số $\\frac{\\sqrt{x} + 2}{\\sqrt{x} - 1}$ nhận giá trị nguyên?", "options": ["$3$", "$2$", "$4$", "$1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $S = \\frac{1}{\\sqrt{1} + \\sqrt{2}} + \\frac{1}{\\sqrt{2} + \\sqrt{3}} + \\dots + \\frac{1}{\\sqrt{99} + \\sqrt{100}}$. Giá trị của $S$ là:", "options": ["$9$", "$10$", "$8$", "$\\sqrt{99}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số nghiệm của phương trình $|x - 1| + |x - 2| + |x - 3| = 2$ là:", "options": ["$1$", "$2$", "$0$", "Vô số"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức $Q = \\frac{1}{x - \\sqrt{x} + 1}$ với $x \\geq 0$:", "options": ["$\\frac{4}{3}$", "$1$", "$2$", "$\\frac{3}{4}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Biết $x$ là số vô tỉ và $y$ là số hữu tỉ khác 0. Khi đó tích $x \\cdot y$ luôn là:", "options": ["Số vô tỉ", "Số hữu tỉ", "Số nguyên", "Số tự nhiên"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho x là số thực không âm. Xét tính đúng/sai của các mệnh đề sau:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu x < 1 thì √x > x.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu x > 1 thì √x < x.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Với mọi x ≥ 0 thì x - √x + 1 > 0.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Phương trình x = √x có đúng 1 nghiệm duy nhất.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai số thực a, b thỏa mãn a + b = 2√2 và a . b = 1:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "a² + b² = (a + b)² - 2ab = (2√2)² - 2 = 8 - 2 = 6.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "a⁴ + b⁴ = (a² + b²)² - 2(ab)² = 36 - 2 = 34.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Cả hai số a và b đều là các số thực dương.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Hai số a và b là hai số hữu tỉ.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = √(10 + 2√9).", "answer": "4"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên x biết: √(x + 3) = 2√3. Giá trị của x là:", "answer": "9"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: P = |x - 1| + |x - 2| + |x - 3| + |x - 4|.", "answer": "4"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính tổng: S = 1/(1 + √2) + 1/(√2 + √3) + 1/(√3 + √4). Kết quả bằng:", "answer": "1"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "a) Trục căn thức ở mẫu: 1 / (√3 - √2).\nb) Tính giá trị của biểu thức: M = 1 / (√2 + 1) + 1 / (√3 + √2) + 1 / (√4 + √3).",
            "rubric": "a) 1/(√3 - √2) = (√3 + √2)/[(√3 - √2)(√3 + √2)] = (√3 + √2)/(3 - 2) = √3 + √2 (0.5đ).\nb) M = (√2 - 1) + (√3 - √2) + (√4 - √3) = √4 - 1 = 2 - 1 = 1 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm các số thực x, y thỏa mãn:\n√(x - 2) + √(y - 1) = (x + y) / 2.",
            "rubric": "Quy đồng và chuyển vế: (x - 2√(x-2)) + (y - 2√(y-1)) = 0 (0.3đ). Viết lại: [(x - 2) - 2√(x-2) + 1] + [(y - 1) - 2√(y-1) + 1] = 0 (0.4đ) => (√(x-2) - 1)² + (√(y-1) - 1)² = 0 => √(x-2) = 1 và √(y-1) = 1 => x = 3 và y = 2 (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng với mọi số tự nhiên n ≥ 1 thì biểu thức:\nP = 1 / (2√1) + 1 / (3√2) + 1 / (4√3) + ... + 1 / ((n+1)√n) < 2.",
            "rubric": "Xét số hạng tổng quát: 1 / ((k+1)√k) = √k / (k(k+1)) = √k . (1/k - 1/(k+1))? Hoặc đánh giá: 1 / ((k+1)√k) < 2 / (√k + √(k+1)) = 2(√(k+1) - √k) (0.5đ). Lấy tổng từ 1 đến n: P < 2[(√2 - 1) + (√3 - √2) + ... + (√(n+1) - √n)] = 2(√(n+1) - 1). Để chứng minh < 2, đánh giá chặt hơn: 1/((k+1)√k) < 2(1/√k - 1/√(k+1)) => Tổng < 2(1 - 1/√(n+1)) < 2 (0.5đ)."
        }
    ]
}
