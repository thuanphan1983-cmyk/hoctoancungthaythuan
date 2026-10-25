# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG I: SỐ HỮU TỈ
PHẦN 2:
- BÀI 3: LŨY THỪA VỚI SỐ MŨ TỰ NHIÊN CỦA MỘT SỐ HỮU TỈ (c1_7_bai3)
- BÀI 4: THỨ TỰ THỰC HIỆN CÁC PHÉP TÍNH. QUY TẮC CHUYỂN VẾ (c1_7_bai4)
- BÀI KIỂM TRA CUỐI CHƯƠNG I: SỐ HỮU TỈ (c1_7_bai5)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 3: LŨY THỪA VỚI SỐ MŨ TỰ NHIÊN CỦA MỘT SỐ HỮU TỈ (c1_7_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c1_7_bai3_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 3: Lũy thừa của một số hữu tỉ - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Với số hữu tỉ $x$ và $n \\in \\mathbb{N}^*$, lũy thừa bậc $n$ của $x$ kí hiệu là $x^n$ là:", "options": ["Tích của $n$ thừa số $x$", "Tổng của $n$ số hạng $x$", "Thương của $x$ và $n$", "Hiệu của $x$ và $n$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Quy ước: với số hữu tỉ $x \\neq 0$ thì $x^0$ bằng:", "options": ["$1$", "$0$", "$x$", "Không xác định"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Giá trị của $\\left(-\\frac{1}{2}\\right)^3$ là:", "options": ["$-\\frac{1}{8}$", "$\\frac{1}{8}$", "$-\\frac{1}{6}$", "$\\frac{1}{6}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Công thức nhân hai lũy thừa cùng cơ số $x^m \\cdot x^n$ là:", "options": ["$x^{m+n}$", "$x^{m-n}$", "$x^{m \\cdot n}$", "$(2x)^{m+n}$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Công thức chia hai lũy thừa cùng cơ số $x^m : x^n$ ($x \\neq 0, m \\geq n$) là:", "options": ["$x^{m-n}$", "$x^{m+n}$", "$x^{m/n}$", "$x^{n-m}$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Lũy thừa của một lũy thừa $(x^m)^n$ bằng:", "options": ["$x^{m \\cdot n}$", "$x^{m+n}$", "$x^{m-n}$", "$x^{m^n}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tính: $\\left(-\\frac{2}{3}\\right)^2$:", "options": ["$\\frac{4}{9}$", "$-\\frac{4}{9}$", "$\\frac{4}{6}$", "$-\\frac{4}{6}$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Kết quả của phép tính $\\left(\\frac{3}{5}\\right)^5 : \\left(\\frac{3}{5}\\right)^3$ là:", "options": ["$\\frac{9}{25}$", "$\\frac{3}{5}$", "$\\frac{27}{125}$", "$1$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Viết biểu thức $2^3 \\cdot 5^3$ dưới dạng lũy thừa của một tích:", "options": ["$10^3$", "$10^6$", "$10^9$", "$7^3$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Tìm số tự nhiên $n$ thỏa mãn: $2^n = 16$:", "options": ["$n = 4$", "$n = 3$", "$n = 5$", "$n = 8$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Giá trị của biểu thức $[(-0,1)^2]^3$ là:", "options": ["$0,000001$", "$-0,000001$", "$0,0001$", "$-0,0001$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Khẳng định nào sau đây là SAI?", "options": ["$(-3)^4 = -81$", "$(-3)^4 = 81$", "$(-2)^3 = -8$", "$(-5)^0 = 1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho x là một số hữu tỉ khác 0 và m, n là các số tự nhiên:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Nếu số mũ chẵn thì lũy thừa của một số âm luôn là một số dương.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Nếu số mũ lẻ thì lũy thừa của một số âm là một số âm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "(x . y)^n = x^n . y^n với mọi số hữu tỉ x, y.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Với mọi x thì x² > 0.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét các phép tính lũy thừa sau:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "(-0,5)² = 0,25.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "(2/3)³ = 8/27.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "4⁶ : 2⁶ = 2⁶ = 64.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "(3²)³ = 3⁵.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của: A = (-1/3)⁴ . 3⁴.", "answer": "1"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên n thỏa mãn: (1/2)ⁿ = 1/32.", "answer": "5"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính giá trị của biểu thức: B = (0,25)³ . 4³.", "answer": "1"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm x biết: x² = 49/81 và x > 0. (Viết dưới dạng phân số tối giản a/b)", "answer": "7/9"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị các biểu thức sau:\na) A = (-2/3)³ + 4/9\nb) B = (0,5)⁴ . 2⁴ - (3/4)⁰.",
            "rubric": "a) (-2/3)³ = -8/27. A = -8/27 + 12/27 = 4/27 (0.5đ).\nb) (0,5 . 2)⁴ - 1 = 1⁴ - 1 = 0 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số hữu tỉ x biết:\na) (x - 1/2)³ = 1/27\nb) (2x + 1)² = 25.",
            "rubric": "a) x - 1/2 = 1/3 => x = 1/3 + 1/2 = 5/6 (0.5đ).\nb) 2x + 1 = 5 => 2x = 4 => x = 2; hoặc 2x + 1 = -5 => 2x = -6 => x = -3. Vậy x ∈ {-3; 2} (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Khối lượng của Trái Đất xấp xỉ bằng 6 . 10²⁴ kg, khối lượng của Mặt Trăng xấp xỉ bằng 7,5 . 10²² kg.\na) Khối lượng Trái Đất gấp khoảng bao nhiêu lần khối lượng Mặt Trăng?\nb) Tổng khối lượng của Trái Đất và Mặt Trăng là bao nhiêu kg (viết dưới dạng a . 10²⁴ kg)?",
            "rubric": "a) Tỉ số: (6 . 10²⁴) : (7,5 . 10²²) = (6 : 7,5) . 10² = 0,8 . 100 = 80 lần (0.5đ).\nb) 7,5 . 10²² = 0,075 . 10²⁴. Tổng khối lượng: 6 . 10²⁴ + 0,075 . 10²⁴ = 6,075 . 10²⁴ kg (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c1_7_bai3_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 3: Lũy thừa của một số hữu tỉ - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\frac{4^3 \\cdot 9^4}{6^6}$ ta được kết quả là:", "options": ["$9$", "$6$", "$3$", "$1$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên $n$ biết: $\\frac{16}{2^n} = 2$:", "options": ["$n = 3$", "$n = 4$", "$n = 2$", "$n = 1$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "So sánh $2^{30}$ và $3^{20}$:", "options": ["$2^{30} < 3^{20}$", "$2^{30} > 3^{20}$", "$2^{30} = 3^{20}$", "Không so sánh được"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $\\left(x - \\frac{1}{3}\\right)^2 = \\frac{4}{9}$:", "options": ["$x = 1$ hoặc $x = -\\frac{1}{3}$", "$x = 1$", "$x = -\\frac{1}{3}$", "$x = \\frac{5}{3}$ hoặc $x = -1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Giá trị của biểu thức $P = \\frac{10^8 \\cdot 9^4}{6^8 \\cdot 5^7}$ là:", "options": ["$5$", "$10$", "$2$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $x$ thỏa mãn: $3^{x+1} - 3^x = 54$:", "options": ["$x = 3$", "$x = 2$", "$x = 4$", "$x = 1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Số các chữ số của số $A = 2^{12} \\cdot 5^9$ khi viết trong hệ thập phân là:", "options": ["$12$", "$11$", "$10$", "$13$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho $x$ là số hữu tỉ thỏa mãn: $x^2 = x^5$. Giá trị của $x$ có thể là:", "options": ["$x \\in \\{0; 1\\}$", "$x = 1$", "$x = 0$", "$x \\in \\{-1; 0; 1\\}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ thỏa mãn: $2 \\cdot 2^2 \\cdot 2^3 \\dots 2^n = 1024$:", "options": ["$n = 4$", "$n = 5$", "$n = 6$", "$n = 10$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Chữ số tận cùng của $7^{2024}$ là:", "options": ["$1$", "$7$", "$9$", "$3$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "So sánh $A = 2^{100}$ và $B = 10^{30}$:", "options": ["$A > B$", "$A < B$", "$A = B$", "Không thể so sánh"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị của biểu thức $M = \\frac{2^{12} \\cdot 3^5 - 4^6 \\cdot 9^2}{(2^2 \\cdot 3)^6 + 8^4 \\cdot 3^5}$ là:", "options": ["$-\\frac{1}{3}$", "$\\frac{1}{3}$", "$0$", "$1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "So sánh các lũy thừa sau:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "2³⁰ = (2³)¹⁰ = 8¹⁰ và 3²⁰ = (3²)¹⁰ = 9¹⁰.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Vì 8 < 9 nên 2³⁰ < 3²⁰.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "(-1/2)⁴⁰ > (-1/2)⁵⁰.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "5³⁰⁰ > 3⁵⁰⁰.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm x: (2x - 3)⁴ = (2x - 3)²:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Đưa về phương trình tích: (2x - 3)² . [(2x - 3)² - 1] = 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "TH1: (2x - 3)² = 0 => 2x - 3 = 0 => x = 1,5.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "TH2: (2x - 3)² = 1 => 2x - 3 = 1 hoặc 2x - 3 = -1 => x = 2 hoặc x = 1.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Phương trình có đúng 2 nghiệm phân biệt.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = (4⁵ . 9⁴ - 2 . 6⁹) / (2¹⁰ . 3⁸ + 6⁸ . 20). Kết quả rút gọn là một số âm. Số đó là:", "answer": "-1/3"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên n thỏa mãn: 5ⁿ + 5ⁿ⁺² = 650.", "answer": "2"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm giá trị của x biết: (x - 2/3)³ = -8/27. Giá trị của x là:", "answer": "0"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số chữ số 0 tận cùng của tích: P = 2²⁰ . 5¹⁷.", "answer": "17"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Rút gọn các biểu thức sau:\na) A = (2⁷ . 9³)/(6⁵ . 8²)\nb) B = (4⁶ . 9⁵ + 6⁹ . 120)/(8⁴ . 3¹² - 6¹¹).",
            "rubric": "a) A = (2⁷ . 3⁶)/(2⁵ . 3⁵ . 2⁶) = (2⁷ . 3⁶)/(2¹¹ . 3⁵) = 3/2⁴ = 3/16 (0.5đ).\nb) Đưa về cơ số 2 và 3, rút nhân tử chung tính ra B = 4/5 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm x biết:\na) (2x - 1)³ = -125/216\nb) 3^(x+2) + 3^x = 810.",
            "rubric": "a) 2x - 1 = -5/6 => 2x = 1/6 => x = 1/12 (0.5đ).\nb) 3^x(3² + 1) = 810 => 3^x . 10 = 810 => 3^x = 81 = 3⁴ => x = 4 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "a) So sánh hai số: 3¹⁰⁰ và 2¹⁵⁰.\nb) Tìm tất cả các số nguyên n thỏa mãn: 27 < 3ⁿ ≤ 243.",
            "rubric": "a) 3¹⁰⁰ = (3²)⁵⁰ = 9⁵⁰; 2¹⁵⁰ = (2³)⁵⁰ = 8⁵⁰. Vì 9 > 8 nên 3¹⁰⁰ > 2¹⁵⁰ (0.5đ).\nb) 3³ < 3ⁿ ≤ 3⁵ => 3 < n ≤ 5. Vì n nguyên nên n ∈ {4; 5} (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c1_7_bai3_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 3: Lũy thừa của một số hữu tỉ - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số tự nhiên $n$ biết $3^{-1} \\cdot 3^n + 5 \\cdot 3^{n-1} = 162$:", "options": ["$n = 4$", "$n = 3$", "$n = 5$", "$n = 2$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho $A = 1 + 2 + 2^2 + \\dots + 2^{2024}$. Biểu thức $A + 1$ bằng:", "options": ["$2^{2025}$", "$2^{2024}$", "$2^{2026}$", "$4^{2024}$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm các cặp số tự nhiên $(x; y)$ thỏa mãn $2^{x+1} \\cdot 3^y = 72$:", "options": ["$(x; y) = (2; 2)$", "$(x; y) = (3; 1)$", "$(x; y) = (1; 3)$", "$(x; y) = (2; 3)$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Số dư khi chia $A = 3 + 3^2 + 3^3 + \\dots + 3^{100}$ cho 13 là:", "options": ["$3$", "$0$", "$1$", "$9$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho $2^n > 1000$:", "options": ["$n = 10$", "$n = 9$", "$n = 11$", "$n = 8$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Chữ số tận cùng của $2^{2025}$ là:", "options": ["$2$", "$4$", "$8$", "$6$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "So sánh $A = 100^{100}$ và $B = 2^{100} \\cdot 50^{100}$:", "options": ["$A = B$", "$A > B$", "$A < B$", "Không so sánh được"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho biểu thức $P = \\frac{2^{2024} - 1}{2^{2025} - 1}$ và $Q = \\frac{2^{2025} - 1}{2^{2026} - 1}$. So sánh $P$ và $Q$:", "options": ["$P < Q$", "$P > Q$", "$P = Q$", "Không so sánh được"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $(x - 2)^{x+1} = (x - 2)^{x+3}$?", "options": ["$3$", "$1$", "$2$", "$0$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm chữ số tận cùng của số $S = 1^{2024} + 2^{2024} + 3^{2024} + 4^{2024}$:", "options": ["$4$", "$6$", "$0$", "$2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Biết $x$ thỏa mãn $5^{x} + 5^{x+2} = 650$. Giá trị của biểu thức $x^3 - 2x + 1$ là:", "options": ["$5$", "$1$", "$9$", "$7$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Chứng minh tổng $B = 4 + 4^2 + 4^3 + \\dots + 4^{60}$ chia hết cho 21. Khẳng định nào sau đây đúng?", "options": ["Nhóm 3 số hạng liên tiếp chia hết cho 21", "Nhóm 2 số hạng liên tiếp chia hết cho 21", "B chia hết cho 4 nhưng không chia hết cho 21", "B tận cùng bằng 0"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức S = 1 + 3 + 3² + 3³ + ... + 3²⁰²⁴:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "3S = 3 + 3² + 3³ + ... + 3²⁰²⁵.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "2S = 3S - S = 3²⁰²⁵ - 1.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Giá trị của 2S + 1 là một lũy thừa của 3 có số mũ bằng 2025.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Tổng S chia hết cho 4.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét phương trình (x - 1)⁵ = (x - 1)³:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Chuyển vế đặt nhân tử chung được: (x - 1)³ . [(x - 1)² - 1] = 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "x = 1 là một nghiệm của phương trình.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "(x - 1)² = 1 cho ta hai giá trị x = 2 hoặc x = 0.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Tổng tất cả các nghiệm của phương trình bằng 3.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số tự nhiên n thỏa mãn: 2ⁿ⁺¹ . 3ⁿ = 108.", "answer": "3"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm chữ số tận cùng của số A = 2²⁰²⁴.", "answer": "6"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số tự nhiên x biết: 3^(x-1) + 5 . 3^(x-1) = 162.", "answer": "4"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: M = (x² - 9)² + |y - 2| + 10.", "answer": "10"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "a) Cho A = 2 + 2² + 2³ + ... + 2⁶⁰. Chứng minh rằng A chia hết cho 3 và 7.\nb) Tìm chữ số tận cùng của A.",
            "rubric": "a) Nhóm 2 số: A = 2(1+2) + ... = 3.(...) chia hết cho 3. Nhóm 3 số: A = 2(1+2+4) + ... = 7.(...) chia hết cho 7 (0.6đ).\nb) 2A = 2² + ... + 2⁶¹ => A = 2⁶¹ - 2 = 2 . (2⁴)¹⁵ - 2 = 2 . (...6) - 2 = ...2 - 2 = ...0. Tận cùng là 0 (0.4đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các số nguyên x thỏa mãn:\n(2x - 3)³ = (2x - 3)⁵.",
            "rubric": "Chuyển vế: (2x - 3)³ . [1 - (2x - 3)²] = 0 (0.3đ). TH1: 2x - 3 = 0 => x = 3/2 (loại vì x nguyên) (0.2đ). TH2: 2x - 3 = 1 => 2x = 4 => x = 2 (nhận) (0.2đ). TH3: 2x - 3 = -1 => 2x = 2 => x = 1 (nhận) (0.2đ). Kết luận x ∈ {1; 2} (0.1đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "So sánh hai biểu thức:\nA = (10²⁰²⁴ + 1) / (10²⁰²⁵ + 1) và B = (10²⁰²⁵ + 1) / (10²⁰²⁶ + 1).",
            "rubric": "Xét 10A = (10²⁰²⁵ + 10) / (10²⁰²⁵ + 1) = 1 + 9/(10²⁰²⁵ + 1) (0.4đ). Tương tự 10B = 1 + 9/(10²⁰²⁶ + 1) (0.3đ). Vì 10²⁰²⁵ + 1 < 10²⁰²⁶ + 1 nên 9/(10²⁰²⁵ + 1) > 9/(10²⁰²⁶ + 1) => 10A > 10B => A > B (0.3đ)."
        }
    ]
}


# ==============================================================================
# BÀI 4: THỨ TỰ THỰC HIỆN CÁC PHÉP TÍNH. QUY TẮC CHUYỂN VẾ (c1_7_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c1_7_bai4_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 4: Thứ tự phép tính. Quy tắc chuyển vế - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Thứ tự thực hiện các phép tính trong biểu thức không có dấu ngoặc là:", "options": ["Lũy thừa -> Nhân và chia -> Cộng và trừ", "Cộng và trừ -> Nhân và chia -> Lũy thừa", "Nhân và chia -> Lũy thừa -> Cộng và trừ", "Từ phải sang trái"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Thứ tự thực hiện các phép tính đối với biểu thức có dấu ngoặc là:", "options": ["( ) -> [ ] -> { }", "{ } -> [ ] -> ( )", "[ ] -> ( ) -> { }", "Tùy ý"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Khi chuyển số hạng $-\\frac{2}{3}$ từ vế trái sang vế phải của một đẳng thức, số hạng đó đổi thành:", "options": ["$+\\frac{2}{3}$", "$-\\frac{2}{3}$", "$-\\frac{3}{2}$", "$\\frac{3}{2}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Nếu $x + a = b$ thì giá trị của $x$ bằng:", "options": ["$x = b - a$", "$x = b + a$", "$x = a - b$", "$x = -(a + b)$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: $15 - 3 \\cdot \\left(\\frac{1}{3}\\right)^2$:", "options": ["$\\frac{44}{3}$", "$4$", "$\\frac{4}{3}$", "$12$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Tìm $x$ biết: $x - \\frac{3}{4} = -\\frac{1}{2}$:", "options": ["$x = \\frac{1}{4}$", "$x = -\\frac{5}{4}$", "$x = -\\frac{1}{4}$", "$x = \\frac{5}{4}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Giá trị của biểu thức $20 : [5 - (2 - 1)^2]$ là:", "options": ["$5$", "$4$", "$10$", "$20$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tìm $x$ biết: $\\frac{2}{3} + x = -\\frac{1}{6}$:", "options": ["$x = -\\frac{5}{6}$", "$x = \\frac{5}{6}$", "$x = -\\frac{1}{2}$", "$x = \\frac{1}{2}$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Tính: $A = \\left(-\\frac{1}{2}\\right)^3 : \\frac{1}{4} + \\frac{3}{2}$:", "options": ["$1$", "$-1$", "$2$", "$0$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Bỏ dấu ngoặc của biểu thức $A - (B - C + D)$ ta được:", "options": ["$A - B + C - D$", "$A - B - C + D$", "$A - B - C - D$", "$A + B - C + D$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Kết quả của phép tính $\\frac{3}{4} - \\frac{1}{4} : \\frac{1}{2}$ là:", "options": ["$\\frac{1}{4}$", "$1$", "$\\frac{1}{2}$", "$0$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Tìm $x$ biết: $3x + 1,2 = 4,2$:", "options": ["$x = 1$", "$x = 1,8$", "$x = 2$", "$x = 0,5$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức M = 5/8 - (1/4 + 3/8) . 2:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng trong ngoặc 1/4 + 3/8 = 5/8.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Phép nhân (5/8) . 2 = 5/4.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Giá trị của biểu thức M = 5/8 - 5/4 = -5/8.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Giá trị của M là một số hữu tỉ dương.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm x: 2/3 - 4x = 1/2:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Chuyển vế ta có: -4x = 1/2 - 2/3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hiệu 1/2 - 2/3 = -1/6.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Giá trị x = (-1/6) : (-4) = 1/24.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "x là số hữu tỉ âm.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = 2³ - 3 . (1/2)² + 1/4.", "answer": "7,5"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số hữu tỉ x biết: x/3 + 1/2 = 5/6.", "answer": "1"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm x thỏa mãn: 1,5 - 2x = -0,5.", "answer": "1"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tính giá trị của biểu thức: P = (1/3 + 1/4) . 12 - 5.", "answer": "2"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính:\na) A = 3/4 + 1/4 . (-2/3)\nb) B = [3/8 - (1/2)²] : 5/16.",
            "rubric": "a) 3/4 - 1/6 = 9/12 - 2/12 = 7/12 (0.5đ).\nb) 3/8 - 1/4 = 1/8. B = (1/8) : (5/16) = (1/8) . (16/5) = 2/5 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số hữu tỉ x biết:\na) 2/3 x - 1/4 = 5/12\nb) 3/4 - (x - 1/3) = 1/2.",
            "rubric": "a) 2/3 x = 5/12 + 1/4 = 8/12 = 2/3 => x = 1 (0.5đ).\nb) x - 1/3 = 3/4 - 1/2 = 1/4 => x = 1/4 + 1/3 = 7/12 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một người nông dân thu hoạch cam trong 3 ngày được tổng cộng 450 kg cam. Ngày thứ nhất thu hoạch được 1/3 tổng khối lượng. Ngày thứ hai thu hoạch bằng 4/5 khối lượng ngày thứ nhất. Hỏi ngày thứ ba người đó thu hoạch được bao nhiêu ki-lô-gam cam?",
            "rubric": "Ngày 1: 450 x 1/3 = 150 kg (0.3đ). Ngày 2: 150 x 4/5 = 120 kg (0.3đ). Ngày 3: 450 - (150 + 120) = 180 kg (0.4đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c1_7_bai4_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 4: Thứ tự phép tính. Quy tắc chuyển vế - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Giá trị của biểu thức $A = 12 \\cdot \\left(-\\frac{2}{3}\\right)^2 + \\frac{4}{3}$ là:", "options": ["$\\frac{20}{3}$", "$4$", "$\\frac{16}{3}$", "$8$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $x$ biết: $\\frac{4}{5} - \\left(x + \\frac{1}{3}\\right) = 0,25$:", "options": ["$x = \\frac{13}{60}$", "$x = -\\frac{13}{60}$", "$x = \\frac{7}{20}$", "$x = \\frac{17}{60}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tính: $B = \\frac{2}{3} : \\left(-\\frac{1}{3}\\right)^2 - \\frac{3}{4} \\cdot (-8)$:", "options": ["$12$", "$0$", "$6$", "$-6$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $2(x - 1,5) - 3(x + 0,5) = -4$:", "options": ["$x = -0,5$", "$x = 0,5$", "$x = -1$", "$x = 1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Giá trị của biểu thức $C = \\left[\\left(\\frac{3}{8} - \\frac{5}{12}\\right) \\cdot 6 + \\frac{1}{3}\\right] : 4$ là:", "options": ["$\\frac{1}{48}$", "$-\\frac{1}{48}$", "$\\frac{1}{24}$", "$-\\frac{1}{24}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $\\left|x - \\frac{2}{5}\\right| + \\frac{1}{2} = \\frac{3}{4}$:", "options": ["$x = \\frac{13}{20}$ hoặc $x = \\frac{3}{20}$", "$x = \\frac{13}{20}$", "$x = \\frac{3}{20}$", "$x = \\frac{7}{20}$ hoặc $x = -\\frac{7}{20}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Một bể nước có dung tích $1200\\text{ lít}$. Vòi thứ nhất chảy vào bể mỗi giờ được $\\frac{1}{4}$ bể, vòi thứ hai chảy mỗi giờ được $\\frac{1}{6}$ bể. Nếu mở cả hai vòi cùng chảy thì sau bao lâu bể đầy nước?", "options": ["$2,4\\text{ giờ}$", "$2\\text{ giờ}$", "$3\\text{ giờ}$", "$2,5\\text{ giờ}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $\\frac{2}{3}x - \\frac{1}{2} = \\frac{3}{4}x + \\frac{1}{3}$:", "options": ["$x = -10$", "$x = 10$", "$x = -5$", "$x = 5$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tính giá trị của biểu thức $P = \\left(\\frac{1}{4} - 1\\right)\\left(\\frac{1}{9} - 1\\right)\\dots\\left(\\frac{1}{100} - 1\\right)$:", "options": ["$-\\frac{11}{20}$", "$\\frac{11}{20}$", "$-\\frac{9}{20}$", "$\\frac{9}{20}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm $x$ biết: $(2x - 3)^2 = 36$:", "options": ["$x = 4,5$ hoặc $x = -1,5$", "$x = 4,5$", "$x = -1,5$", "$x = 9$ hoặc $x = -3$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $A = 1 - 2 + 3 - 4 + \\dots + 99 - 100$. Giá trị của $A$ là:", "options": ["$-50$", "$50$", "$-100$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị nhỏ nhất của biểu thức $M = (x - 1)^2 + |y + 2| - 3$ là:", "options": ["$-3$", "$0$", "$3$", "$-2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức A = 4,5 - [(-3/2)² - (5/4 - 1/2) : 1/4]:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "(-3/2)² = 9/4 = 2,25.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "(5/4 - 1/2) : 1/4 = (3/4) . 4 = 3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Giá trị trong ngoặc vuông: 2,25 - 3 = -0,75.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Giá trị của biểu thức A là 3,75.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét phương trình (3/4)x + 1/2 = (2/3)x - 5/6:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Chuyển vế ta được: (3/4 - 2/3)x = -5/6 - 1/2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "3/4 - 2/3 = 1/12.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "-5/6 - 1/2 = -8/6 = -4/3.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nghiệm của phương trình là x = -16.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số hữu tỉ x thỏa mãn: 3/5 - 2x = 1/4.", "answer": "7/40"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tính giá trị biểu thức: P = 2/3 - [(-1/2)² - 3/4] + 1/6.", "answer": "4/3"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên x biết: 2^(x+1) + 2^x = 96.", "answer": "5"},
        {"id": 4, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên x thỏa mãn: |2x - 1| ≤ 5?", "answer": "6"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính một cách hợp lý:\na) A = 15/34 + 7/21 + 19/34 - 1 15/17 + 2/3\nb) B = (-2)³ . (3/4 - 0,25) : (2 1/4 - 1 1/6).",
            "rubric": "a) (15/34 + 19/34) + (1/3 + 2/3) - 32/17 = 1 + 1 - 32/17 = 2 - 32/17 = 2/17 (0.5đ).\nb) (-8) . (1/2) : (9/4 - 7/6) = -4 : (13/12) = -48/13 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số hữu tỉ x biết:\na) 2/3 x + 1/4 = 7/12\nb) (x - 1/3)² - 1/9 = 8/9.",
            "rubric": "a) 2/3 x = 7/12 - 3/12 = 4/12 = 1/3 => x = 1/2 (0.5đ).\nb) (x - 1/3)² = 1 => x - 1/3 = 1 => x = 4/3; hoặc x - 1/3 = -1 => x = -2/3 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một người bán một số quả bưởi trong 3 ngày. Ngày thứ nhất bán được 1/4 tổng số bưởi và 15 quả. Ngày thứ hai bán được 1/3 số quả còn lại và 10 quả. Ngày thứ ba bán nốt 50 quả bưởi còn lại.\na) Hỏi ban đầu người đó có tất cả bao nhiêu quả bưởi mang đi bán?\nb) Tính số quả bưởi bán được trong ngày thứ nhất.",
            "rubric": "a) Số bưởi còn lại trước khi bán ngày 3: (50 + 10) : (1 - 1/3) = 60 : (2/3) = 90 quả. Tổng số bưởi ban đầu: (90 + 15) : (1 - 1/4) = 105 : (3/4) = 140 quả (0.6đ).\nb) Ngày thứ nhất bán: 140 x 1/4 + 15 = 50 quả (0.4đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c1_7_bai4_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 4: Thứ tự phép tính. Quy tắc chuyển vế - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm $x$ biết: $\\frac{x - 1}{2023} + \\frac{x - 2}{2022} + \\frac{x - 3}{2021} = 3$:", "options": ["$x = 2024$", "$x = 2023$", "$x = 2025$", "$x = 2022$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Giá trị của biểu thức $P = \\frac{1}{1\\cdot 4} + \\frac{1}{4\\cdot 7} + \\dots + \\frac{1}{97\\cdot 100}$ là:", "options": ["$\\frac{33}{100}$", "$\\frac{99}{100}$", "$\\frac{1}{100}$", "$\\frac{11}{100}$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $|2x - 3| - |x + 1| = 0$:", "options": ["$x = 4$ hoặc $x = \\frac{2}{3}$", "$x = 4$", "$x = \\frac{2}{3}$", "$x = -4$ hoặc $x = -\\frac{2}{3}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Số các cặp số nguyên $(x; y)$ thỏa mãn $xy - 2x + 3y = 11$ là:", "options": ["$4$", "$2$", "$6$", "$8$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Cho $a + b + c = 0$. Biểu thức $M = \\left(1 + \\frac{a}{b}\\right)\\left(1 + \\frac{b}{c}\\right)\\left(1 + \\frac{c}{a}\\right)$ có giá trị là:", "options": ["$-1$", "$1$", "$0$", "$-8$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = |x - 2| + |x - 5| + |x - 8|$:", "options": ["$6$", "$8$", "$5$", "$10$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho $x, y$ là các số hữu tỉ khác 0 thỏa mãn $x^2 + y^2 = 2xy$. Khi đó tỉ số $\\frac{x}{y}$ bằng:", "options": ["$1$", "$-1$", "$2$", "$\\frac{1}{2}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm $x$ biết: $\\frac{1}{x(x+1)} + \\frac{1}{(x+1)(x+2)} + \\frac{1}{(x+2)(x+3)} = \\frac{3}{10}$ (với $x > 0$):", "options": ["$x = 2$", "$x = 1$", "$x = 3$", "$x = 5$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Biết rằng $\\frac{a}{b} = \\frac{c}{d}$ ($a, b, c, d \\neq 0$). Đẳng thức nào sau đây SAI?", "options": ["$\\frac{a+b}{b} = \\frac{c-d}{d}$", "$\\frac{a+b}{b} = \\frac{c+d}{d}$", "$\\frac{a}{c} = \\frac{b}{d}$", "$\\frac{a-b}{a+b} = \\frac{c-d}{c+d}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Giá trị của biểu thức $S = \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\dots + \\frac{1}{1024}$ là:", "options": ["$\\frac{1023}{1024}$", "$\\frac{1}{1024}$", "$1$", "$\\frac{511}{512}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ sao cho $n^2 + 2n + 7$ chia hết cho $n + 2$:", "options": ["$n = 5$", "$n = 6$", "$n = 4$", "$n = 7$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $x$ thỏa mãn $(x - 1)^{2024} + |y - 2|^{2025} = 0$. Giá trị của $x + y$ là:", "options": ["$3$", "$1$", "$-1$", "$0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho bài toán tìm x: (x + 1)/2024 + (x + 2)/2023 + (x + 3)/2022 = -3:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Cộng 1 vào mỗi phân số ở vế trái ta được: [(x+1)/2024 + 1] + [(x+2)/2023 + 1] + [(x+3)/2022 + 1] = 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Mỗi số hạng đều có tử số chung là (x + 2025).", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Đặt nhân tử chung (x + 2025) . [1/2024 + 1/2023 + 1/2022] = 0.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Nghiệm của phương trình là x = 2025.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét biểu thức P = |x - 1| + |x - 4|:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Ta có |x - 1| + |x - 4| = |x - 1| + |4 - x| ≥ |x - 1 + 4 - x| = 3.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Giá trị nhỏ nhất của P bằng 3.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Dấu bằng xảy ra khi và chỉ khi 1 ≤ x ≤ 4.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Chỉ có duy nhất một giá trị x = 2,5 làm cho P đạt giá trị nhỏ nhất.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số hữu tỉ x biết: (x - 1)/2 = (x + 2)/3.", "answer": "7"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tính giá trị của tổng: S = 1/(1.4) + 1/(4.7) + 1/(7.10) + ... + 1/(28.31). Tử số của phân số tối giản S là:", "answer": "10"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: A = |x - 3| + |x - 7|.", "answer": "4"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số hữu tỉ x thỏa mãn: (x + 1)/99 + (x + 2)/98 = (x + 3)/97 + (x + 4)/96.", "answer": "-100"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Tìm số hữu tỉ x biết:\n(x - 1)/2024 + (x - 2)/2023 = (x - 3)/2022 + (x - 4)/2021.",
            "rubric": "Trừ 1 vào mỗi phân số: [(x-1)/2024 - 1] + [(x-2)/2023 - 1] = [(x-3)/2022 - 1] + [(x-4)/2021 - 1] (0.4đ) => (x - 2025) . [1/2024 + 1/2023 - 1/2022 - 1/2021] = 0 (0.4đ). Vì biểu thức trong ngoặc khác 0 nên x - 2025 = 0 => x = 2025 (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tính tổng: S = 1/3 + 1/3² + 1/3³ + ... + 1/3¹⁰⁰.",
            "rubric": "3S = 1 + 1/3 + 1/3² + ... + 1/3⁹⁹ (0.4đ). 3S - S = 1 - 1/3¹⁰⁰ => 2S = 1 - 1/3¹⁰⁰ => S = (1 - 1/3¹⁰⁰) / 2 = 1/2 - 1/(2 . 3¹⁰⁰) (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức:\nP = |x - 1| + |x - 2| + |x - 3|.",
            "rubric": "Ta có: |x - 1| + |x - 3| = |x - 1| + |3 - x| ≥ |x - 1 + 3 - x| = 2 (0.4đ). Lại có |x - 2| ≥ 0 với mọi x (0.2đ). Do đó P ≥ 2 + 0 = 2. Dấu \"=\" xảy ra khi và chỉ khi (x - 1)(3 - x) ≥ 0 và x - 2 = 0 <=> x = 2. Vậy giá trị nhỏ nhất của P là 2 tại x = 2 (0.4đ)."
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG I: SỐ HỮU TỈ (c1_7_bai5)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c1_7_bai5_test1"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương I: Số hữu tỉ - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Số đối của $-\\frac{5}{7}$ là:", "options": ["$\\frac{5}{7}$", "$-\\frac{5}{7}$", "$-\\frac{7}{5}$", "$\\frac{7}{5}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Tập hợp các số hữu tỉ gồm:", "options": ["Các số viết được dưới dạng phân số $\\frac{a}{b}$ với $a, b \\in \\mathbb{Z}, b \\neq 0$", "Chỉ các số nguyên", "Chỉ các số tự nhiên", "Các số thập phân vô hạn không tuần hoàn"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Giá trị của $\\left(-\\frac{1}{3}\\right)^2$ là:", "options": ["$\\frac{1}{9}$", "$-\\frac{1}{9}$", "$\\frac{1}{6}$", "$-\\frac{1}{6}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Kết quả của phép tính $-\\frac{3}{5} + \\frac{2}{5}$ là:", "options": ["$-\\frac{1}{5}$", "$\\frac{1}{5}$", "$-\\frac{5}{5} = -1$", "$1$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Số nghịch đảo của số hữu tỉ $-2\\frac{1}{3}$ là:", "options": ["$-\\frac{3}{7}$", "$\\frac{3}{7}$", "$-\\frac{7}{3}$", "$\\frac{7}{3}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Tính: $0,75 - \\left(-\\frac{1}{4}\\right)$:", "options": ["$1$", "$0,5$", "$-1$", "$0$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tìm $x$ biết: $x + \\frac{1}{2} = -\\frac{3}{4}$:", "options": ["$x = -\\frac{5}{4}$", "$x = -\\frac{1}{4}$", "$x = \\frac{5}{4}$", "$x = \\frac{1}{4}$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\left(\\frac{2}{3}\\right)^5 : \\left(\\frac{2}{3}\\right)^3$ là:", "options": ["$\\frac{4}{9}$", "$\\frac{2}{3}$", "$\\frac{8}{27}$", "$1$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Khoảng cách từ điểm biểu diễn số $-2,5$ đến gốc 0 trên trục số là:", "options": ["$2,5$", "$-2,5$", "$0$", "$5$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Sắp xếp theo thứ tự tăng dần: $-\\frac{2}{3};\\ 0;\\ 0,5;\\ -1$:", "options": ["$-1 < -\\frac{2}{3} < 0 < 0,5$", "$-\\frac{2}{3} < -1 < 0 < 0,5$", "$0,5 < 0 < -\\frac{2}{3} < -1$", "$-1 < 0 < -\\frac{2}{3} < 0,5$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: $A = \\frac{5}{9} \\cdot \\frac{7}{13} + \\frac{5}{9} \\cdot \\frac{6}{13}$:", "options": ["$\\frac{5}{9}$", "$1$", "$\\frac{13}{9}$", "$\\frac{65}{117}$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Tìm $x$ biết: $x^2 = \\frac{16}{25}$ và $x < 0$:", "options": ["$x = -\\frac{4}{5}$", "$x = \\frac{4}{5}$", "$x = -\\frac{16}{25}$", "$x = -\\frac{8}{25}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Xét tính đúng/sai của các khẳng định sau về số hữu tỉ:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Mọi số nguyên đều là số hữu tỉ.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Số 0 là số hữu tỉ dương.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "(-0,2)³ = -0,008.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Hai số đối nhau có tổng bằng 0.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho biểu thức P = 2/3 - 1/3 . (1/2)²:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Thực hiện phép lũy thừa trước: (1/2)² = 1/4.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Phép nhân: (1/3) . (1/4) = 1/12.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Phép trừ: P = 2/3 - 1/12 = 8/12 - 1/12 = 7/12.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Giá trị của P lớn hơn 1.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính kết quả phép tính: (-3/4) . 8/9. (Viết dưới dạng phân số tối giản a/b)", "answer": "-2/3"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số hữu tỉ x biết: 2x - 1/3 = 1/2.", "answer": "5/12"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính giá trị biểu thức: M = (0,4)⁵ : (0,4)³ + 0,84.", "answer": "1"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Một người đi xe đạp đi được 15 km trong 1,25 giờ. Vận tốc của người đó là bao nhiêu km/h?", "answer": "12"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính hợp lý nếu có thể:\na) A = (-3/7) + 5/11 + (-4/7) + 6/11\nb) B = (2/3)² . 9/4 - (-1/2)³ . 8.",
            "rubric": "a) A = [(-3/7) + (-4/7)] + [5/11 + 6/11] = -1 + 1 = 0 (0.5đ).\nb) B = (4/9) . (9/4) - (-1/8) . 8 = 1 - (-1) = 2 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số hữu tỉ x biết:\na) 3/4 x + 1/2 = -1/4\nb) (2x - 1/3)² = 4/9.",
            "rubric": "a) 3/4 x = -1/4 - 1/2 = -3/4 => x = -1 (0.5đ).\nb) 2x - 1/3 = 2/3 => 2x = 1 => x = 1/2; hoặc 2x - 1/3 = -2/3 => 2x = -1/3 => x = -1/6 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Bác Bình gửi tiết kiệm 50 triệu đồng vào ngân hàng với kì hạn 1 năm, lãi suất 6,5%/năm.\na) Tính số tiền lãi bác Bình nhận được sau 1 năm.\nb) Hết kì hạn 1 năm, bác rút ra 1/2 tổng số tiền (cả gốc và lãi) để mua sắm. Hỏi số tiền còn lại trong tài khoản của bác là bao nhiêu triệu đồng?",
            "rubric": "a) Tiền lãi sau 1 năm: 50 x 6,5% = 3,25 (triệu đồng) (0.5đ).\nb) Tổng số tiền sau 1 năm: 50 + 3,25 = 53,25 (triệu đồng). Số tiền còn lại: 53,25 : 2 = 26,625 (triệu đồng) (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c1_7_bai5_test2"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương I: Số hữu tỉ - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Giá trị của biểu thức $A = \\left(-\\frac{1}{3}\\right)^2 : \\frac{1}{9} - 2 \\cdot \\left(-\\frac{1}{2}\\right)^3$ là:", "options": ["$\\frac{5}{4}$", "$\\frac{3}{4}$", "$1$", "$2$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $x$ biết: $\\frac{2}{3}x - \\frac{1}{4} = \\frac{1}{6}$:", "options": ["$x = \\frac{5}{8}$", "$x = -\\frac{5}{8}$", "$x = \\frac{1}{8}$", "$x = \\frac{3}{8}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\frac{2^5 \\cdot 3^4}{6^4}$ ta được:", "options": ["$2$", "$3$", "$6$", "$1$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $\\left|x - \\frac{3}{4}\\right| = \\frac{1}{2}$:", "options": ["$x = \\frac{5}{4}$ hoặc $x = \\frac{1}{4}$", "$x = \\frac{5}{4}$", "$x = \\frac{1}{4}$", "$x = -\\frac{5}{4}$ hoặc $x = -\\frac{1}{4}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tính nhanh giá trị của biểu thức: $M = \\frac{4}{7} \\cdot \\frac{3}{5} + \\frac{4}{7} \\cdot \\frac{2}{5} - 1\\frac{4}{7}$:", "options": ["$-1$", "$0$", "$1$", "$-\\frac{4}{7}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $n$ biết: $3^{n+1} - 3^n = 162$:", "options": ["$n = 4$", "$n = 3$", "$n = 5$", "$n = 2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Một ô tô đi từ A đến B hết 2 giờ 30 phút với vận tốc $60\\text{ km/h}$. Quãng đường AB dài:", "options": ["$150\\text{ km}$", "$120\\text{ km}$", "$180\\text{ km}$", "$140\\text{ km}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho hai số hữu tỉ $a$ và $b$ thỏa mãn $a + b = -1$ và $a - b = 0,6$. Giá trị của $a \\cdot b$ là:", "options": ["$-0,16$", "$0,16$", "$-0,64$", "$0,64$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Giá trị của biểu thức $B = \\frac{1}{1\\cdot 2} + \\frac{1}{2\\cdot 3} + \\frac{1}{3\\cdot 4} + \\dots + \\frac{1}{49\\cdot 50}$ là:", "options": ["$\\frac{49}{50}$", "$\\frac{1}{50}$", "$\\frac{50}{51}$", "$1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm $x$ biết: $\\frac{x+1}{2024} + \\frac{x+2}{2023} + \\frac{x+3}{2022} = -3$:", "options": ["$x = -2025$", "$x = 2025$", "$x = -2024$", "$x = 2024$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số giá trị nguyên của $x$ để phân số $\\frac{x+3}{x-1}$ nhận giá trị nguyên là:", "options": ["$6$", "$4$", "$8$", "$2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị nhỏ nhất của biểu thức $P = |x - 1,5| + 2,8$ là:", "options": ["$2,8$", "$1,5$", "$4,3$", "$0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai biểu thức A = (1/2)³ . 4 + 3/4 và B = (3/2)² - 1/2 . 3:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "A = (1/8) . 4 + 3/4 = 1/2 + 3/4 = 5/4.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "B = 9/4 - 3/2 = 9/4 - 6/4 = 3/4.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Giá trị của biểu thức A lớn hơn giá trị của biểu thức B.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Hiệu A - B = 1/4.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm x: (2/5)x + 1/3 = (1/2)x - 1/6:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Chuyển vế: (2/5 - 1/2)x = -1/6 - 1/3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "2/5 - 1/2 = -1/10.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "-1/6 - 1/3 = -1/2.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nghiệm của phương trình là x = 5.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = 1/2 - 3/4 + 5/6 - 7/12. (Viết dưới dạng phân số tối giản a/b)", "answer": "0"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên n thỏa mãn: (2ⁿ)² = 64.", "answer": "3"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm x thỏa mãn: |x - 2| + 3 = 5 và x < 0.", "answer": "0 (không có) -> x-2=2=>x=4; x-2=-2=>x=0. Vậy x = ", "answer": "0"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: M = (x - 2)² + 3.", "answer": "3"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị biểu thức một cách hợp lý:\na) A = (-3/4) . 5/17 + (-3/4) . 12/17 + 1 3/4\nb) B = (2/3 - 1/4 + 5/12) : (1/2 - 1/3).",
            "rubric": "a) (-3/4) . (5/17 + 12/17) + 7/4 = (-3/4) . 1 + 7/4 = 4/4 = 1 (0.5đ).\nb) (8/12 - 3/12 + 5/12) : (1/6) = (10/12) . 6 = 5 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm x biết:\na) 3/4 - 2(x + 1/3) = 1/2\nb) (2x - 1)³ = -27/64.",
            "rubric": "a) 2(x + 1/3) = 3/4 - 1/2 = 1/4 => x + 1/3 = 1/8 => x = 1/8 - 1/3 = -5/24 (0.5đ).\nb) 2x - 1 = -3/4 => 2x = 1/4 => x = 1/8 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một người bán một rổ trứng. Lần thứ nhất người đó bán được 1/2 số trứng và thêm 1 quả. Lần thứ hai người đó bán được 1/2 số trứng còn lại và thêm 1 quả. Lần thứ ba bán được 1/2 số trứng còn lại sau hai lần và thêm 1 quả nữa thì vừa hết rổ trứng.\na) Hỏi ban đầu người đó có tất cả bao nhiêu quả trứng trong rổ?\nb) Tính số trứng bán được trong lần thứ nhất.",
            "rubric": "a) Tính ngược từ cuối: Trước lần 3 có: (0 + 1) : (1/2) = 2 quả. Trước lần 2 có: (2 + 1) : (1/2) = 6 quả. Ban đầu có: (6 + 1) : (1/2) = 14 quả trứng (0.6đ).\nb) Lần thứ nhất bán được: 14 x 1/2 + 1 = 8 quả trứng (0.4đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c1_7_bai5_test3"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương I: Số hữu tỉ - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $S = 1 + \\frac{1}{2} + \\frac{1}{2^2} + \\frac{1}{2^3} + \\dots + \\frac{1}{2^{10}}$:", "options": ["$2 - \\frac{1}{2^{10}}$", "$2 - \\frac{1}{2^{11}}$", "$1 - \\frac{1}{2^{10}}$", "$2$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $(x - 1)^{2024} = (x - 1)^{2026}$:", "options": ["$x \\in \\{0; 1; 2\\}$", "$x = 1$", "$x = 2$", "$x \\in \\{1; 2\\}$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Có bao nhiêu cặp số nguyên $(x; y)$ thỏa mãn $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{2}$?", "options": ["$5$", "$3$", "$4$", "$6$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $a, b, c$ là các số hữu tỉ đôi một khác nhau. Giá trị của biểu thức $M = \\frac{a-b}{c} + \\frac{b-c}{a} + \\frac{c-a}{b}$ khi $\\frac{a}{b+c} + \\frac{b}{c+a} + \\frac{c}{a+b} = 1$ là:", "options": ["$0$", "$1$", "$-1$", "$3$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = |x - 2024| + |x - 1|$:", "options": ["$2023$", "$2025$", "$0$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $P = \\left(1 - \\frac{1}{2}\\right)\\left(1 - \\frac{1}{3}\\right)\\left(1 - \\frac{1}{4}\\right)\\dots\\left(1 - \\frac{1}{2025}\\right)$. Giá trị của $P$ là:", "options": ["$\\frac{1}{2025}$", "$\\frac{2024}{2025}$", "$\\frac{1}{2024}$", "$1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ sao cho phân số $\\frac{2n + 3}{4n + 1}$ có giá trị lớn nhất:", "options": ["$n = 0$", "$n = 1$", "$n = 2$", "Không có giá trị lớn nhất"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm chữ số tận cùng của tổng $A = 2 + 2^2 + 2^3 + \\dots + 2^{2024}$:", "options": ["$0$", "$2$", "$4$", "$6$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm $x$ biết: $\\frac{x - 2024}{2} + \\frac{x - 2024}{3} + \\frac{x - 2024}{4} = 0$:", "options": ["$x = 2024$", "$x = 0$", "$x = 1$", "Vô nghiệm"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hai số hữu tỉ dương $x, y$ thỏa mãn $x^3 + y^3 = x - y$. Khẳng định nào sau đây đúng?", "options": ["$x^2 + y^2 < 1$", "$x^2 + y^2 > 1$", "$x^2 + y^2 = 1$", "Không xác định"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số dư khi chia $3^{2025}$ cho 13 là:", "options": ["$1$", "$3$", "$9$", "$0$"], "correct": 1},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị lớn nhất của biểu thức $Q = \\frac{2024}{|x| + 2}$ là:", "options": ["$1012$", "$2024$", "$506$", "Không tồn tại"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho dãy số A = 1/3 + 1/3² + 1/3³ + ... + 1/3²⁰²⁴:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "3A = 1 + 1/3 + 1/3² + ... + 1/3²⁰²³.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "2A = 3A - A = 1 - 1/3²⁰²⁴.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "A < 1/2.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "A > 1.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm x: |x - 3| + |x + 2| = 5:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Áp dụng bất đẳng thức: |x - 3| + |x + 2| = |3 - x| + |x + 2| ≥ |3 - x + x + 2| = 5.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Dấu bằng xảy ra khi (3 - x)(x + 2) ≥ 0.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Tập nghiệm của phương trình là mọi số hữu tỉ x thỏa mãn -2 ≤ x ≤ 3.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Chỉ có 2 nghiệm nguyên thỏa mãn phương trình.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = (1 - 1/4) . (1 - 1/9) . (1 - 1/16) ... (1 - 1/100). (Viết dạng phân số tối giản a/b)", "answer": "11/20"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên n thỏa mãn: 3 . 2ⁿ + 2ⁿ⁺² = 112.", "answer": "4"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: P = |x - 2024| + |x - 2025|.", "answer": "1"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số tự nhiên x biết: 1/(1.2) + 1/(2.3) + ... + 1/(x(x+1)) = 2024/2025.", "answer": "2024"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Tìm số hữu tỉ x biết:\n(x - 2024)/10 + (x - 2024)/11 + (x - 2024)/12 = (x - 2024)/13 + (x - 2024)/14.",
            "rubric": "(x - 2024) . [1/10 + 1/11 + 1/12 - 1/13 - 1/14] = 0 (0.4đ). Vì 1/10 > 1/13 và 1/11 > 1/14 nên ngoặc khác 0 (0.4đ) => x = 2024 (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức A = 1/2² + 1/3² + 1/4² + ... + 1/2024².\nChứng minh rằng 1/2 < A < 1.",
            "rubric": "1/k² < 1/((k-1)k) => A < 1/(1.2) + 1/(2.3) + ... + 1/(2023.2024) = 1 - 1/2024 < 1 (0.5đ). Lại có 1/k² > 1/(k(k+1)) => A > 1/(2.3) + 1/(3.4) + ... + 1/(2024.2025) = 1/2 - 1/2025 > 1/2 - 1/4 = ... Hoặc xét số hạng đầu 1/4 + 1/9 + 1/16 > 1/2. Suy ra 1/2 < A < 1 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các cặp số nguyên (x; y) thỏa mãn:\nxy + 3x - 2y = 11.",
            "rubric": "x(y + 3) - 2(y + 3) + 6 = 11 => (x - 2)(y + 3) = 5 (0.4đ). Xét các ước của 5 = {±1; ±5} (0.2đ). Tìm được 4 cặp nghiệm: (3; 2), (1; -8), (7; -2), (-3; -4) (0.4đ)."
        }
    ]
}
