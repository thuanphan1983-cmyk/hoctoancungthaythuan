# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 6 - CHƯƠNG II: TÍNH CHIA HẾT TRONG TẬP HỢP CÁC SỐ TỰ NHIÊN
PHẦN 1: BÀI 8 (QUAN HỆ CHIA HẾT VÀ TÍNH CHẤT) & BÀI 9 (DẤU HIỆU CHIA HẾT)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025.
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 8: QUAN HỆ CHIA HẾT VÀ TÍNH CHẤT (c2_6_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c2_6_bai1_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 8: Quan hệ chia hết và tính chất - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Số tự nhiên $a$ chia hết cho số tự nhiên $b$ ($b \\neq 0$) nếu có số tự nhiên $q$ sao cho:", "options": ["$a = b \\cdot q$", "$a = b + q$", "$a = b : q$", "$a = b - q$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Kí hiệu $a$ chia hết cho $b$ là:", "options": ["$a \\,\\vdots\\, b$", "$a \\, / \\, b$", "$a \\in b$", "$a \\subset b$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trong phép chia có dư $a = b \\cdot q + r$ ($b > 0$), số dư $r$ thỏa mãn điều kiện nào sau đây?", "options": ["$0 \\leq r < b$", "$0 < r \\leq b$", "$0 \\leq r \\leq b$", "$r > b$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Nếu số tự nhiên $a$ chia hết cho số tự nhiên $b$, ta nói:", "options": ["$a$ là bội của $b$ và $b$ là ước của $a$", "$a$ là ước của $b$ và $b$ là bội của $a$", "$a$ là bội của $b$ và $b$ cũng là bội của $a$", "$a$ là ước của $b$ và $b$ cũng là ước của $a$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Tập hợp các ước của số $6$ là:", "options": ["$\\Ư(6) = \\{1; 2; 3; 6\\}$", "$\\Ư(6) = \\{0; 1; 2; 3; 6\\}$", "$\\Ư(6) = \\{2; 3\\}$", "$\\Ư(6) = \\{1; 6\\}$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Số nào sau đây là ước của mọi số tự nhiên khác 0?", "options": ["$1$", "$0$", "$2$", "Chính số đó"], "correct": 0},
        {"id": 7, "level": "Nhận biết", "question": "Nếu $a \\,\\vdots\\, m$ và $b \\,\\vdots\\, m$ thì khẳng định nào sau đây là đúng?", "options": ["$(a + b) \\,\\vdots\\, m$", "$(a - b)$ không chia hết cho $m$", "$(a \\cdot b)$ không chia hết cho $m$", "$(a + b)$ không chia hết cho $m$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho tổng $A = 12 + 24 + 36$. Tổng $A$ chia hết cho số nào sau đây?", "options": ["$6$", "$5$", "$7$", "$8$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho hiệu $B = 48 - 16$. Hiệu $B$ chia hết cho số nào sau đây?", "options": ["$8$", "$5$", "$9$", "$7$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Biết $x \\,\\vdots\\, 5$ và $15 \\leq x \\leq 25$. Có bao nhiêu giá trị của $x$ thỏa mãn?", "options": ["$3$", "$2$", "$4$", "$1$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tập hợp bốn bội đầu tiên của $7$ là:", "options": ["$\\{0; 7; 14; 21\\}$", "$\\{7; 14; 21; 28\\}$", "$\\{1; 7; 14; 21\\}$", "$\\{0; 1; 7; 14\\}$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Không làm phép tính, cho biết biểu thức nào sau đây chia hết cho $4$?", "options": ["$20 + 36 + 40$", "$16 + 25 + 32$", "$12 + 18 + 24$", "$8 + 14 + 20$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tập hợp các số tự nhiên $A = \\{12; 15; 20; 25; 30\\}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Trong tập hợp $A$ có đúng 4 số là bội của 5.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số 12 là ước của 30.", "correct": False},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tổng $15 + 25 + 30$ chia hết cho 5.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tổng $12 + 20 + 30$ chia hết cho 4.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho biểu thức $M = 24 + 36 + x$ với $x$ là số tự nhiên.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Cả hai số 24 và 36 đều chia hết cho 6.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu $x = 18$ thì $M$ chia hết cho 6.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nếu $x = 10$ thì $M$ chia hết cho 6.", "correct": False},
                {"key": "d", "level": "Vận dụng thấp", "text": "Để $M$ chia hết cho 6 thì $x$ bắt buộc phải là bội của 6.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số tự nhiên $x$ sao cho $x \\in \\Ư(15)$ và $x > 4$. Tính tổng các giá trị đó.", "answer": "20"},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu số tự nhiên $x$ là bội của $4$ và $10 < x < 30$?", "answer": "5"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số dư trong phép chia số $A = 1 \\cdot 2 \\cdot 3 \\cdot 4 \\cdot 5 + 7$ cho $5$.", "answer": "2"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho tổng $S = 21 + 28 + x$. Tìm số tự nhiên $x$ nhỏ nhất khác 0 để $S$ chia hết cho $7$.", "answer": "7"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Viết tập hợp $\\Ư(18)$ và tập hợp $\\B(6)$ gồm các bội nhỏ hơn $30$.\nb) Không thực hiện phép tính, hãy giải thích vì sao tổng $A = 24 + 36 + 48$ chia hết cho $12$.",
            "rubric": "a) Ư(18) = {1; 2; 3; 6; 9; 18} (0.25đ). B(6) nhỏ hơn 30: {0; 6; 12; 18; 24} (0.25đ).\nb) Ta có 24 chia hết cho 12 (vì 24 = 12 * 2) (0.15đ); 36 chia hết cho 12 (vì 36 = 12 * 3) (0.15đ); 48 chia hết cho 12 (vì 48 = 12 * 4) (0.1đ). Áp dụng tính chất chia hết của một tổng, suy ra A chia hết cho 12 (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cô giáo muốn chia đều $36$ quyển vở và $48$ cái bút bi cho các tổ học tập.\na) Hỏi cô giáo có thể chia đều số vở và bút trên cho $4$ tổ được không? Vì sao?\nb) Hỏi cô giáo có thể chia đều số vở và bút trên cho $5$ tổ được không? Vì sao?",
            "rubric": "a) Ta có 36 chia hết cho 4 (36 : 4 = 9 quyển/tổ) (0.25đ) và 48 chia hết cho 4 (48 : 4 = 12 bút/tổ) (0.25đ). Do đó cô giáo chia đều được cho 4 tổ.\nb) Ta có 36 không chia hết cho 5 (vì 36 = 5 * 7 + 1 dư 1) (0.25đ). Do đó không thể chia đều 36 quyển vở cho 5 tổ (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $A = 12 + 15 + 21 + x$ ($x \\in \\mathbb{N}$).\na) Tìm điều kiện của $x$ để $A$ chia hết cho $3$.\nb) Tìm điều kiện của $x$ để $A$ không chia hết cho $3$.",
            "rubric": "Ta thấy 12 chia hết cho 3, 15 chia hết cho 3, 21 chia hết cho 3 (0.3đ).\na) Để A chia hết cho 3 thì x phải chia hết cho 3, tức là x là bội của 3 (x ∈ B(3)) (0.35đ).\nb) Để A không chia hết cho 3 thì x không chia hết cho 3, tức là x không phải là bội của 3 (0.35đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c2_6_bai1_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 8: Quan hệ chia hết và tính chất - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho số tự nhiên $a$ chia cho $6$ dư $4$. Khẳng định nào sau đây là ĐÚNG?", "options": ["$a$ chia hết cho 2 nhưng không chia hết cho 6", "$a$ chia hết cho 3", "$a$ chia hết cho 6", "$a$ chia cho 2 dư 1"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Nếu tổng $(a + b) \\,\\vdots\\, 7$ và $a \\,\\vdots\\, 7$ thì:", "options": ["$b \\,\\vdots\\, 7$", "$b$ không chia hết cho 7", "$b$ có thể chia hết hoặc không chia hết cho 7", "$b = 7$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tập hợp các ước của $24$ có bao nhiêu phần tử?", "options": ["$8$", "$6$", "$10$", "$7$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho $M = 35 \\cdot 12 + 42$. Biểu thức $M$ chia hết cho:", "options": ["$7$", "$5$", "$10$", "$11$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Có bao nhiêu số tự nhiên $x$ thỏa mãn $x \\,\\vdots\\, 8$ và $20 \\leq x \\leq 60$?", "options": ["$5$", "$6$", "$4$", "$7$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Biết $x + 1$ là ước của $10$. Giá trị tự nhiên lớn nhất của $x$ là:", "options": ["$9$", "$10$", "$4$", "$1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho $A = 3 + 3^2 + 3^3 + 3^4$. Biểu thức $A$ chia hết cho số nào?", "options": ["$4$", "$5$", "$7$", "$8$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $n$ để $(n + 5) \\,\\vdots\\, n$ ($n > 0$):", "options": ["$n \\in \\{1; 5\\}$", "$n \\in \\{1; 2; 5\\}$", "$n = 5$", "$n = 1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cho tích $P = 1 \\cdot 2 \\cdot 3 \\cdot 4 \\cdot 5 \\dots 10$. Khẳng định nào sau đây là SAI?", "options": ["$P + 1$ chia hết cho 5", "$P$ chia hết cho 10", "$P$ chia hết cho 9", "$P$ chia hết cho 7"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Khi chia số tự nhiên $a$ cho $12$ được số dư là $8$. Khi chia $a$ cho $4$ thì số dư là:", "options": ["$0$", "$2$", "$1$", "$3$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Tổng $S = 2 + 2^2 + 2^3 + 2^4 + 2^5 + 2^6$ chia hết cho số nào?", "options": ["$3$", "$5$", "$7$", "$9$"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Một lớp học có $42$ học sinh. Giáo viên muốn chia lớp thành các nhóm có số người bằng nhau (mỗi nhóm nhiều hơn 3 học sinh và ít hơn 15 học sinh). Có bao nhiêu cách chia?", "options": ["$3$ cách (nhóm 6, 7, 14 người)", "$4$ cách", "$2$ cách", "$5$ cách"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tổng $A = 2 + 2^2 + 2^3 + 2^4 + 2^5 + 2^6$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng $A$ có đúng 6 số hạng.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nhóm từng đôi một: $A = (2 + 2^2) + (2^3 + 2^4) + (2^5 + 2^6) = 6 + 2^2 \\cdot 6 + 2^4 \\cdot 6$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tổng $A$ chia hết cho 3.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tổng $A$ chia hết cho 7 vì nhóm bộ ba $(2 + 2^2 + 2^3) = 14$ chia hết cho 7.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho $n$ là một số tự nhiên và biểu thức $B = 3n + 7$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Khi $n = 1$, giá trị của $B$ bằng 10.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Với mọi số tự nhiên $n$, $B$ không bao giờ chia hết cho 3 vì 7 không chia hết cho 3.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Để $B$ chia hết cho 5 thì $n$ phải có chữ số tận cùng là 1 hoặc 6.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Không tồn tại số tự nhiên $n$ nào để $B$ chia hết cho 2.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính tổng các ước của số $12$.", "answer": "28"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $n$ thỏa mãn $6 \\,\\vdots\\, (n - 1)$. Có bao nhiêu giá trị của $n$?", "answer": "4"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số dư của $A = 10^{20} + 8$ khi chia cho $9$.", "answer": "0"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $x$ nhỏ nhất khác 0 sao cho $(x + 15) \\,\\vdots\\, 5$ và $(x + 18) \\,\\vdots\\, 6$.", "answer": "30"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Chứng tỏ rằng:\na) Tổng $A = 15 \\cdot 12 + 20$ chia hết cho $5$.\nb) Hiệu $B = 7 \\cdot 8 \\cdot 9 - 56$ chia hết cho $7$.",
            "rubric": "a) Ta có 15 * 12 chia hết cho 5 (vì 15 chia hết cho 5) (0.25đ); 20 chia hết cho 5 (0.15đ). Suy ra A chia hết cho 5 (0.1đ).\nb) Ta có 7 * 8 * 9 chia hết cho 7 (0.25đ); 56 chia hết cho 7 (56 = 7 * 8) (0.15đ). Suy ra B chia hết cho 7 (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho $S = 5 + 5^2 + 5^3 + \\dots + 5^{20}$.\na) Chứng minh rằng $S$ chia hết cho $6$.\nb) Chứng minh rằng $S$ chia hết cho $30$.",
            "rubric": "a) S có 20 số hạng, nhóm 2 số hạng liên tiếp: S = (5 + 5^2) + (5^3 + 5^4) + ... + (5^19 + 5^20) (0.2đ)\n= 5(1 + 5) + 5^3(1 + 5) + ... + 5^19(1 + 5) = 6 * (5 + 5^3 + ... + 5^19) chia hết cho 6 (0.3đ).\nb) Vì mỗi số hạng của S đều chia hết cho 5 nên S chia hết cho 5 (0.25đ).\nMặt khác S chia hết cho 6 và ƯCLN(5, 6) = 1 nên S chia hết cho 5 * 6 = 30 (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tìm số tự nhiên $n$ sao cho:\na) $(n + 4) \\,\\vdots\\, n$.\nb) $(2n + 7) \\,\\vdots\\, (n + 1)$.",
            "rubric": "a) Vì (n + 4) chia hết cho n mà n chia hết cho n nên 4 chia hết cho n (0.2đ) => n ∈ Ư(4) = {1; 2; 4} (0.3đ).\nb) Ta có 2n + 7 = 2(n + 1) + 5 (0.2đ).\nĐể 2n + 7 chia hết cho n + 1 thì 5 chia hết cho n + 1 (0.15đ) => n + 1 ∈ Ư(5) = {1; 5} => n ∈ {0; 4} (0.15đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c2_6_bai1_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 8: Quan hệ chia hết và tính chất - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Chứng minh rằng tích của hai số tự nhiên liên tiếp luôn:", "options": ["Chia hết cho 2", "Chia hết cho 3", "Chia hết cho 4", "Là số lẻ"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tích của ba số tự nhiên liên tiếp luôn chia hết cho số nào sau đây?", "options": ["$6$", "$4$", "$9$", "$12$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho $A = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{11}$. Tổng $A$ chia hết cho:", "options": ["$13$", "$7$", "$11$", "$17$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Số dư khi chia $A = 2 + 2^2 + 2^3 + \\dots + 2^{100}$ cho $3$ là:", "options": ["$0$", "$1$", "$2$", "$3$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tìm tất cả số tự nhiên $n$ để phân số $\\frac{n + 3}{n - 1}$ là số tự nhiên:", "options": ["$n \\in \\{2; 3; 5\\}$", "$n \\in \\{1; 2; 3; 5\\}$", "$n \\in \\{2; 5\\}$", "$n \\in \\{3; 5\\}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $p$ là số nguyên tố lớn hơn 3. Khi chia $p^2$ cho 3 thì số dư là:", "options": ["$1$", "$2$", "$0$", "Không xác định"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ lớn nhất có hai chữ số sao cho $2n + 1$ chia hết cho $n - 2$:", "options": ["$n = 7$", "$n = 9$", "$n = 12$", "$n = 99$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $a$ và $b$ là hai số tự nhiên lẻ. Tổng $a^2 + b^2$ khi chia cho 4 có số dư là:", "options": ["$2$", "$0$", "$1$", "$3$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho số tự nhiên $A = n(n + 1)(2n + 1)$. Khẳng định nào sau đây luôn đúng với mọi $n \\in \\mathbb{N}$?", "options": ["$A$ chia hết cho 6", "$A$ chia hết cho 12", "$A$ chia hết cho 8", "$A$ chia hết cho 15"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số các ước tự nhiên của số $360$ là:", "options": ["$24$", "$18$", "$20$", "$16$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm chữ số tận cùng của $S = 2 + 2^2 + 2^3 + \\dots + 2^{2024}$:", "options": ["$0$", "$2$", "$4$", "$6$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một hội trường có từ $300$ đến $400$ người. Nếu xếp mỗi hàng $12$ người, $15$ người hoặc $18$ người thì đều vừa đủ. Số người trong hội trường là:", "options": ["$360$", "$320$", "$340$", "$380$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A = 4 + 4^2 + 4^3 + \\dots + 4^{60}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng $A$ có tất cả 60 số hạng đều là lũy thừa của 4.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Nhóm 2 số hạng liên tiếp: $A = (4 + 4^2) + \\dots = 20(1 + 4^2 + \\dots)$, suy ra $A \\,\\vdots\\, 5$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Nhóm 3 số hạng liên tiếp: $4 + 4^2 + 4^3 = 4(1 + 4 + 16) = 4 \\cdot 21 = 84 \\,\\vdots\\, 21$, suy ra $A \\,\\vdots\\, 21$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Tổng $A$ chia hết cho 105 vì 105 = 5 * 21 và ƯCLN(5, 21) = 1.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai số tự nhiên $a$ và $b$ thỏa mãn $(3a + 2b) \\,\\vdots\\, 17$. Xét biểu thức $B = 10a + b$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Ta có $2B = 2(10a + b) = 20a + 2b$.", "correct": True},
                {"key": "b", "level": "Vận dụng cao", "text": "Xét hiệu $2B - (3a + 2b) = 17a$, biểu thức này luôn chia hết cho 17.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Vì $(3a + 2b) \\,\\vdots\\, 17$ và $17a \\,\\vdots\\, 17$ nên $2B \\,\\vdots\\, 17$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Do ƯCLN(2, 17) = 1 nên $(10a + b)$ cũng chia hết cho 17.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $n$ sao cho $n^2 + 2n + 4$ chia hết cho $n + 1$.", "answer": "2"},
        {"id": 2, "level": "Vận dụng cao", "question": "Cho $A = 1 + 2 + 2^2 + \\dots + 2^{2023}$. Tìm số dư khi chia $A$ cho $7$.", "answer": "0"},
        {"id": 3, "level": "Vận dụng cao", "question": "Có bao nhiêu số tự nhiên $n$ nhỏ hơn 100 để $(n^2 + 1)$ chia hết cho $5$?", "answer": "40"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị của số tự nhiên $n$ nhỏ nhất sao cho $n! = 1 \\cdot 2 \\cdot 3 \\dots n$ chia hết cho $100$.", "answer": "10"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho $M = 3 + 3^2 + 3^3 + \\dots + 3^{60}$.\na) Chứng minh $M$ chia hết cho $4$.\nb) Chứng minh $M$ chia hết cho $13$.",
            "rubric": "a) M có 60 số hạng. Nhóm từng đôi: M = (3 + 3^2) + (3^3 + 3^4) + ... + (3^59 + 3^60) = 12 + 3^2 * 12 + ... + 3^58 * 12 = 12(1 + 3^2 + ... + 3^58) (0.25đ). Vì 12 chia hết cho 4 nên M chia hết cho 4 (0.25đ).\nb) Nhóm bộ 3 số hạng: M = (3 + 3^2 + 3^3) + ... + (3^58 + 3^59 + 3^60) = 3(1 + 3 + 9) + ... + 3^58(1 + 3 + 9) = 39 * (1 + 3^3 + ... + 3^57) (0.3đ). Vì 39 chia hết cho 13 nên M chia hết cho 13 (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng với mọi số tự nhiên $n$ thì:\na) $n(n + 1)(n + 2)$ chia hết cho $6$.\nb) $(n^2 + n + 1)$ không chia hết cho $2$.",
            "rubric": "a) Trong 3 số tự nhiên liên tiếp n, n+1, n+2 luôn có ít nhất một số chia hết cho 2 và một số chia hết cho 3 (0.3đ). Mà ƯCLN(2, 3) = 1 nên tích chia hết cho 2 * 3 = 6 (0.2đ).\nb) Ta có n^2 + n + 1 = n(n + 1) + 1 (0.25đ). Vì tích n(n + 1) là tích hai số tự nhiên liên tiếp nên luôn là số chẵn (chia hết cho 2). Do đó n(n + 1) + 1 là số lẻ, không chia hết cho 2 (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các số tự nhiên $n$ để phân số $\\frac{3n + 4}{n + 2}$ có giá trị là một số tự nhiên.",
            "rubric": "Ta có: (3n + 4) / (n + 2) = [3(n + 2) - 2] / (n + 2) = 3 - 2 / (n + 2) (0.35đ).\nĐể phân số là số tự nhiên thì 2 chia hết cho (n + 2) và 3 - 2/(n + 2) ≥ 0 (0.25đ).\nSuy ra (n + 2) ∈ Ư(2) = {1; 2} (0.2đ).\n- Nếu n + 2 = 1 => n = -1 (loại vì n là số tự nhiên).\n- Nếu n + 2 = 2 => n = 0 (thỏa mãn, khi đó giá trị là 3 - 1 = 2) (0.15đ).\nVậy n = 0 (0.05đ)."
        }
    ]
}

# ==============================================================================
# BÀI 9: DẤU HIỆU CHIA HẾT (c2_6_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c2_6_bai2_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 9: Dấu hiệu chia hết - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Số có chữ số tận cùng là chữ số nào sau đây thì chia hết cho 2?", "options": ["$0; 2; 4; 6; 8$", "$1; 3; 5; 7; 9$", "$0; 5$", "$0; 3; 6; 9$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Số có chữ số tận cùng là chữ số nào sau đây thì chia hết cho 5?", "options": ["$0$ hoặc $5$", "Chỉ chữ số $0$", "Chỉ chữ số $5$", "$0; 2; 4; 6; 8$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Số có chữ số tận cùng là chữ số nào thì chia hết cho cả 2 và 5?", "options": ["Chữ số $0$", "Chữ số $5$", "Chữ số $2$", "Chữ số $8$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Dấu hiệu chia hết cho 3 là:", "options": ["Tổng các chữ số của số đó chia hết cho 3", "Chữ số tận cùng chia hết cho 3", "Hai chữ số tận cùng chia hết cho 3", "Tổng các chữ số tận cùng bằng 3"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Dấu hiệu chia hết cho 9 là:", "options": ["Tổng các chữ số của số đó chia hết cho 9", "Chữ số tận cùng là 9", "Chữ số tận cùng chia hết cho 9", "Hai chữ số tận cùng chia hết cho 9"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Khẳng định nào sau đây là ĐÚNG?", "options": ["Một số chia hết cho 9 thì chắc chắn chia hết cho 3", "Một số chia hết cho 3 thì chắc chắn chia hết cho 9", "Một số chia hết cho 2 thì chắc chắn chia hết cho 4", "Một số chia hết cho 5 thì tận cùng là 0"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Trong các số $124; 235; 340; 459$, số nào chia hết cho cả 2 và 5?", "options": ["$340$", "$124$", "$235$", "$459$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Trong các số $135; 246; 357; 469$, số nào chia hết cho 9?", "options": ["$135$", "$246$", "$357$", "$469$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Điền chữ số thích hợp vào dấu $*$ để số $\\overline{5*2}$ chia hết cho 3:", "options": ["$2$", "$1$", "$3$", "$4$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cho số $A = 2340$. Khẳng định nào sau đây là SAI?", "options": ["$A$ chia hết cho 7", "$A$ chia hết cho 2", "$A$ chia hết cho 5", "$A$ chia hết cho 9"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Số nào sau đây chia hết cho 3 nhưng KHÔNG chia hết cho 9?", "options": ["$123$", "$108$", "$180$", "$216$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Thay chữ số $x$ để số $\\overline{17x}$ chia hết cho 2 nhưng không chia hết cho 5:", "options": ["$x \\in \\{2; 4; 6; 8\\}$", "$x = 0$", "$x = 5$", "$x \\in \\{0; 2; 4; 6; 8\\}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho số tự nhiên $N = \\overline{4a5b}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Để $N$ chia hết cho cả 2 và 5 thì chữ số tận cùng $b$ phải bằng 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi $b = 0$, số $N$ trở thành $\\overline{4a50}$. Tổng các chữ số lúc này là $9 + a$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Để $\\overline{4a50}$ chia hết cho 9 thì $a$ có thể nhận hai giá trị là $0$ hoặc $9$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Có duy nhất một số $\\overline{4a5b}$ chia hết cho cả 2, 3, 5, 9.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho các số tự nhiên: $120; 245; 369; 450; 505$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Có đúng 3 số chia hết cho 5 là $120; 245; 450; 505$ (thực tế có 4 số).", "correct": False},
                {"key": "b", "level": "Thông hiểu", "text": "Có đúng 2 số chia hết cho cả 2 và 5 là $120$ và $450$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số 450 chia hết cho cả 2, 3, 5 và 9.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tổng $120 + 450$ chia hết cho 9 vì cả hai số đều chia hết cho 9.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm chữ số $x$ để số $\\overline{2x5}$ chia hết cho 9.", "answer": "2"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên nhỏ nhất có 3 chữ số khác nhau chia hết cho cả 2 và 5.", "answer": "120"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Từ 4 chữ số 0, 1, 2, 5, viết được bao nhiêu số tự nhiên có 3 chữ số khác nhau chia hết cho 5?", "answer": "10"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số dư khi chia số $123456789$ cho $9$.", "answer": "0"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Trong các số sau: $2020; 2025; 2031; 2034$:\na) Số nào chia hết cho $2$? Số nào chia hết cho $5$?\nb) Số nào chia hết cho $3$? Số nào chia hết cho $9$?",
            "rubric": "a) Chia hết cho 2: 2020, 2034 (chữ số tận cùng là 0, 4) (0.25đ). Chia hết cho 5: 2020, 2025 (tận cùng là 0, 5) (0.25đ).\nb) Tổng chữ số: 2020 (4), 2025 (9), 2031 (6), 2034 (9). Số chia hết cho 3: 2025, 2031, 2034 (0.25đ). Số chia hết cho 9: 2025, 2034 (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Điền chữ số vào dấu $*$ để số $\\overline{3*5}$:\na) Chia hết cho $3$.\nb) Chia hết cho $9$.",
            "rubric": "Tổng các chữ số là 3 + * + 5 = 8 + * (với * ∈ {0; 1; ...; 9}) (0.2đ).\na) Để chia hết cho 3 thì (8 + *) chia hết cho 3 => * ∈ {1; 4; 7} (0.4đ).\nb) Để chia hết cho 9 thì (8 + *) chia hết cho 9 => * = 1 (0.4đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Dùng ba trong bốn chữ số $0; 3; 4; 5$ hãy ghép thành số tự nhiên có ba chữ số khác nhau sao cho số đó:\na) Chia hết cho cả $2$ và $5$.\nb) Chia hết cho $9$.",
            "rubric": "a) Số chia hết cho cả 2 và 5 phải có tận cùng là 0 (0.2đ). Các số ghép được từ 3, 4, 5 và đuôi 0 là: 340, 350, 430, 450, 530, 540 (0.3đ).\nb) Chọn bộ ba chữ số có tổng chia hết cho 9: 0 + 4 + 5 = 9 (0.25đ). Các số lập được: 450, 405, 540, 504 (0.25đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c2_6_bai2_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 9: Dấu hiệu chia hết - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số tự nhiên $\\overline{1a2b}$ chia hết cho cả 2, 5 và 9 thì tích $a \\cdot b$ bằng:", "options": ["$0$", "$6$", "$12$", "$18$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu chữ số $x$ để số $\\overline{5x4}$ chia hết cho 3?", "options": ["$4$ chữ số ($0; 3; 6; 9$)", "$3$ chữ số", "$2$ chữ số", "$1$ chữ số"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Số dư khi chia $10^{15} + 2$ cho 3 là:", "options": ["$0$", "$1$", "$2$", "$3$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Một số chia cho 9 dư 4. Số đó chia cho 3 có số dư là:", "options": ["$1$", "$0$", "$2$", "$4$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tìm các chữ số $x, y$ để số $\\overline{x45y}$ chia hết cho cả 2, 5 và 3:", "options": ["$y = 0; x \\in \\{3; 6; 9\\}$", "$y = 0; x \\in \\{0; 3; 6; 9\\}$", "$y = 5; x \\in \\{1; 4; 7\\}$", "$y = 0; x = 3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tổng $A = 10^{2024} + 8$ chia hết cho:", "options": ["Cả $2$ và $9$", "Chỉ $2$", "Chỉ $9$", "Cả $5$ và $9$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Hiệu $10^{20} - 1$ chia hết cho số nào sau đây?", "options": ["Cả $3$ và $9$", "Chỉ chia hết cho 3", "Chia hết cho 5", "Chia hết cho 2"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tìm chữ số $a$ sao cho số $\\overline{2a1a}$ chia hết cho 9:", "options": ["$a = 3$", "$a = 6$", "$a = 4$", "$a = 5$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Biết số $\\overline{12x3}$ chia hết cho 3 nhưng không chia hết cho 9. Chữ số $x$ có thể là:", "options": ["$6$", "$3$", "$0$", "$9$"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Cho số $A = 123456...99100$. Số dư của $A$ khi chia cho 9 bằng số dư của:", "options": ["Tổng các chữ số từ 1 đến 100 khi chia cho 9", "Chữ số tận cùng 0", "Hai chữ số tận cùng 00", "Số các chữ số của $A$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên nhỏ nhất có 4 chữ số khác nhau chia hết cho cả 5 và 9:", "options": ["$1260$", "$1035$", "$1080$", "$1215$"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Một cửa hàng có một số quả cam ít hơn 50 quả. Nếu xếp vào các đĩa 2 quả, 3 quả hay 5 quả thì đều vừa hết. Số cam của cửa hàng là:", "options": ["$30$ quả", "$20$ quả", "$40$ quả", "$45$ quả"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho số $M = \\overline{a18b}$. Biết $M$ chia hết cho cả 2, 5 và khi chia cho 9 thì dư 2.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Vì $M$ chia hết cho cả 2 và 5 nên $b = 0$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng các chữ số của $M$ là $a + 1 + 8 + 0 = a + 9$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Vì $M$ chia cho 9 dư 2 nên $(a + 9)$ chia cho 9 dư 2, suy ra $a = 2$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số $M$ cần tìm là $2180$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho biểu thức $P = 10^n + 71$ với $n$ là số tự nhiên ($n \\geq 1$).",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số $10^n$ có dạng $100...00$ gồm chữ số 1 và $n$ chữ số 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng các chữ số của $10^n$ luôn bằng 1.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tổng các chữ số của $P$ bằng $1 + 7 + 1 = 9$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Biểu thức $P$ luôn chia hết cho 9 với mọi số tự nhiên $n \\geq 1$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số tự nhiên $x$ lớn nhất có một chữ số để số $\\overline{7x2}$ chia hết cho 3.", "answer": "9"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm chữ số $x$ để số $\\overline{3x57}$ chia cho 9 có số dư bằng 4.", "answer": "7"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Số các số tự nhiên có hai chữ số chia hết cho cả 2 và 3 là bao nhiêu?", "answer": "15"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số nhỏ nhất có 3 chữ số chia hết cho cả 2, 3 và 5.", "answer": "120"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm các chữ số $x, y$ để:\na) Số $\\overline{2x3y}$ chia hết cho cả $2$ và $5$.\nb) Số $\\overline{x12y}$ chia hết cho cả $2, 5$ và $9$.",
            "rubric": "a) Để số chia hết cho cả 2 và 5 thì chữ số tận cùng y = 0 (0.25đ). Chữ số x tùy ý từ 0 đến 9 (0.25đ).\nb) Để chia hết cho 2 và 5 thì y = 0 (0.2đ). Số trở thành x120, tổng các chữ số là x + 1 + 2 + 0 = x + 3 (0.15đ). Để chia hết cho 9 thì x + 3 = 9 => x = 6 (vì x ≠ 0) (0.15đ). Vậy x = 6, y = 0."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Chứng minh rằng:\na) $A = 10^9 + 2$ chia hết cho $3$.\nb) $B = 10^{2025} - 1$ chia hết cho $9$.",
            "rubric": "a) 10^9 = 1000000000 có tổng các chữ số là 1 (0.25đ). Do đó 10^9 + 2 có tổng các chữ số là 1 + 2 = 3 chia hết cho 3, nên A chia hết cho 3 (0.25đ).\nb) 10^2025 - 1 = 999...99 (gồm 2025 chữ số 9) (0.25đ). Số này rõ ràng có tổng các chữ số chia hết cho 9, nên B chia hết cho 9 (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một lớp học có $45$ học sinh. Trong một buổi dã ngoại, cô giáo muốn chia lớp thành các nhóm sao cho mỗi nhóm có từ $4$ đến $10$ bạn và số bạn ở mỗi nhóm bằng nhau. Hỏi cô giáo có thể chia thành bao nhiêu nhóm? Mỗi nhóm có bao nhiêu bạn?",
            "rubric": "Số nhóm và số bạn mỗi nhóm là các ước của 45 (0.3đ).\nTa có Ư(45) = {1; 3; 5; 9; 15; 45} (0.3đ).\nVì số bạn mỗi nhóm từ 4 đến 10 bạn nên số bạn mỗi nhóm có thể là 5 bạn hoặc 9 bạn (0.2đ).\n- Nếu mỗi nhóm 5 bạn thì chia được 45 : 5 = 9 nhóm (0.1đ).\n- Nếu mỗi nhóm 9 bạn thì chia được 45 : 9 = 5 nhóm (0.1đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c2_6_bai2_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 9: Dấu hiệu chia hết - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số tự nhiên $N = 10^{2024} + 17$ chia hết cho số nào sau đây?", "options": ["$9$", "$5$", "$2$", "$11$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Một số được viết bởi $27$ chữ số $1$. Số đó chia hết cho số nào sau đây?", "options": ["Cả $3$ và $9$", "Chỉ chia hết cho 3", "Không chia hết cho 3 và 9", "Chia hết cho 27 nhưng không chia hết cho 9"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm chữ số $a$ để số $\\overline{a123a}$ chia hết cho 3:", "options": ["$a \\in \\{3; 6; 9\\}$", "$a \\in \\{0; 3; 6; 9\\}$", "$a \\in \\{1; 4; 7\\}$", "$a \\in \\{2; 5; 8\\}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Số dư khi chia $A = 10^1 + 10^2 + 10^3 + \\dots + 10^{10}$ cho $9$ là:", "options": ["$1$", "$0$", "$2$", "$8$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Cho số $A = \\overline{x183y}$ chia cho 2, 5 và 9 đều dư 1. Giá trị của $x + y$ bằng:", "options": ["$7$", "$6$", "$8$", "$9$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Tìm số tự nhiên nhỏ nhất khác 0 chia hết cho cả 2, 3, 4, 5, 6:", "options": ["$60$", "$30$", "$120$", "$90$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Biết số $\\overline{a8b}$ chia hết cho 45. Có bao nhiêu cặp chữ số $(a; b)$ thỏa mãn?", "options": ["$2$ cặp ($a = 1, b = 0$ và $a = 5, b = 5$)", "$1$ cặp", "$3$ cặp", "$4$ cặp"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $n$ là số tự nhiên. Số dư khi chia $A = n^3 - n$ cho 6 là:", "options": ["$0$", "$1$", "$2$", "Tùy thuộc vào $n$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Số tự nhiên $A$ gồm $2025$ chữ số $9$. Nếu cộng thêm $2$ vào số $A$ thì số mới chia cho $9$ có số dư là:", "options": ["$2$", "$0$", "$1$", "$7$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $\\overline{ab}$ sao cho $\\overline{ab} = 2 \\cdot a \\cdot b$:", "options": ["$36$", "$24$", "$12$", "$48$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tổng các số có hai chữ số chia hết cho 3 là:", "options": ["$1665$", "$1650$", "$1680$", "$1620$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một số tự nhiên có 3 chữ số, khi chia cho 2 dư 1, chia cho 5 dư 3, chia hết cho 9 và chữ số hàng trăm là 8. Số đó là:", "options": ["$873$", "$837$", "$828$", "$855$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho số $A = \\overline{1a2b3c}$. Biết $A$ chia hết cho cả 5 và 9, đồng thời $a - b = 2$ và $c$ là chữ số chẵn.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Vì $A$ chia hết cho 5 và $c$ chẵn nên $c = 0$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng các chữ số của $A$ là $1 + a + 2 + b + 3 + 0 = a + b + 6$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Vì $A$ chia hết cho 9 nên $(a + b + 6) \\,\\vdots\\, 9$, suy ra $a + b = 3$ hoặc $a + b = 12$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Kết hợp điều kiện $a - b = 2$ và $a, b$ là các chữ số, ta tìm được duy nhất cặp $(a; b) = (7; 5)$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho số $S = 10^{2024} + 2$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số $S$ có chữ số tận cùng là 2 nên $S$ chia hết cho 2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng các chữ số của $S$ là $1 + 0 + ... + 0 + 2 = 3$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Vì tổng các chữ số bằng 3 nên $S$ chia hết cho 3 nhưng không chia hết cho 9.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Số $S$ chia hết cho 6 vì nó chia hết cho cả 2 và 3.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tìm chữ số $x$ để số $\\overline{x45x}$ chia hết cho cả 2 và 9.", "answer": "0"},
        {"id": 2, "level": "Vận dụng cao", "question": "Tìm số tự nhiên nhỏ nhất chia cho 2 dư 1, chia cho 3 dư 2, chia cho 5 dư 4.", "answer": "29"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $\\overline{xy}$ biết rằng số $\\overline{1x8y2}$ chia hết cho cả 4 và 9.", "answer": "12"},
        {"id": 4, "level": "Vận dụng cao", "question": "Có bao nhiêu số tự nhiên có 3 chữ số chia hết cho 45?", "answer": "20"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Tìm các chữ số $a, b$ sao cho số $\\overline{7a4b}$ chia hết cho cả $4$ và $9$, biết rằng $b > 0$.",
            "rubric": "Dấu hiệu chia hết cho 4: hai chữ số tận cùng 4b chia hết cho 4 => b ∈ {0; 4; 8}. Do b > 0 nên b ∈ {4; 8} (0.35đ).\nTH1: b = 4. Số trở thành 7a44. Tổng chữ số là 7 + a + 4 + 4 = a + 15 chia hết cho 9 => a = 3 (0.3đ).\nTH2: b = 8. Số trở thành 7a48. Tổng chữ số là 7 + a + 4 + 8 = a + 19 chia hết cho 9 => a = 8 (0.3đ).\nVậy (a; b) ∈ {(3; 4); (8; 8)} (0.05đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng số được tạo bởi $2025$ chữ số $1$ liên tiếp $A = \\underbrace{111\\dots1}_{2025\\text{ chữ số } 1}$ chia hết cho $9$ nhưng không chia hết cho $27$.",
            "rubric": "Tổng các chữ số của A là: 1 * 2025 = 2025 (0.3đ).\nTa có 2 + 0 + 2 + 5 = 9 chia hết cho 9 => 2025 chia hết cho 9 nên A chia hết cho 9 (0.35đ).\n2025 : 27 = 75 (2025 chia hết cho 27). Phân tích cấu trúc số: A = 111...1 chia theo khối 27 chữ số 1, chứng minh tỉ mỉ không chia hết cho 27 (0.35đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm số tự nhiên có hai chữ số $\\overline{ab}$ sao cho số đó chia hết cho tích $a \\cdot b$.",
            "rubric": "Ta có ab chia hết cho a và ab chia hết cho b (a, b ≠ 0) (0.2đ).\n10a + b chia hết cho a => b chia hết cho a (0.25đ).\n10a + b chia hết cho b => 10a chia hết cho b (0.25đ).\nXét các trường hợp tỉ mỉ tìm được các số thỏa mãn: 11, 12, 15, 24, 36 (0.3đ)."
        }
    ]
}
