# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 6 - CHƯƠNG III: SỐ NGUYÊN
PHẦN 3: BÀI 17 (PHÉP CHIA HẾT. ƯỚC VÀ BỘI CỦA MỘT SỐ NGUYÊN) & BÀI KIỂM TRA CUỐI CHƯƠNG III
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART3 = {}

# ==============================================================================
# BÀI 17: PHÉP CHIA HẾT. ƯỚC VÀ BỘI CỦA MỘT SỐ NGUYÊN (c3_6_bai5)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART3["c3_6_bai5_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 17: Phép chia hết. Ước và bội của một số nguyên - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Kết quả của phép chia $(-18) : 3$ là:", "options": ["$-6$", "$6$", "$-15$", "$21$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Kết quả của phép chia $(-24) : (-4)$ là:", "options": ["$6$", "$-6$", "$-28$", "$20$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Với số nguyên $a \\neq 0$, kết quả của phép chia $0 : a$ bằng:", "options": ["$0$", "$1$", "$a$", "$-a$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Tập hợp tất cả các ước nguyên của số $4$ là:", "options": ["$\\{-4; -2; -1; 1; 2; 4\\}$", "$\\{1; 2; 4\\}$", "$\\{-4; -1; 1; 4\\}$", "$\\{-2; -1; 0; 1; 2\\}$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Số nào sau đây là một bội của $(-5)$?", "options": ["$-15$", "$12$", "$-18$", "$22$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Trong các khẳng định sau, khẳng định nào đúng?", "options": ["Số $1$ và $-1$ là ước của mọi số nguyên", "Số $0$ là ước của mọi số nguyên", "Số nguyên dương luôn chia hết cho số nguyên âm", "Số $-1$ không phải là ước của số nào"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tìm số nguyên $x$ thỏa mãn: $(-3) \\cdot x = 21$.", "options": ["$x = -7$", "$x = 7$", "$x = 18$", "$x = -24$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Thương của hai số nguyên khác dấu luôn mang dấu:", "options": ["Dấu âm $(-)$", "Dấu dương $(+)$", "Không mang dấu", "Tùy thuộc độ lớn của hai số"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Có bao nhiêu số nguyên $x$ là ước của số $6$?", "options": ["$8$", "$4$", "$6$", "$2$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Nếu số nguyên $a$ chia hết cho $b$ ($b \\neq 0$) thì:", "options": ["$-a$ cũng chia hết cho $b$", "$a$ không chia hết cho $-b$", "$b$ luôn chia hết cho $a$", "$a + b = 0$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Giá trị của biểu thức $[(-36) : 4] : (-3)$ là:", "options": ["$3$", "$-3$", "$-9$", "$9$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Số nào sau đây KHÔNG PHẢI là ước của $(-12)$?", "options": ["$5$", "$-3$", "$4$", "$-6$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Xét tính đúng/sai của các phát biểu về ước và bội của số nguyên sau:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Số 0 là bội của mọi số nguyên khác 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tập hợp các ước của -7 gồm đúng 4 số: 1; -1; 7; -7.", "correct": True},
                {"key": "c", "level": "Nhận biết", "text": "Số 0 là ước của số 5.", "correct": False},
                {"key": "d", "level": "Thông hiểu", "text": "Nếu a chia hết cho b thì -a chia hết cho -b.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho x là một số nguyên. Xét tính đúng/sai của các mệnh đề sau:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu x chia hết cho 6 thì x chia hết cho 3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu 2x = -10 thì x = 5.", "correct": False},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tập hợp các ước tự nhiên của 6 bằng tập hợp các ước nguyên của 6.", "correct": False},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số nguyên âm nhỏ nhất có 1 chữ số chia hết cho 3 là -9.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số nguyên x thỏa mãn: (-5) . x = -45.", "answer": "9"},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = (-48) : (-6) + (-15) : 3.", "answer": "3"},
        {"id": 3, "level": "Thông hiểu", "question": "Có bao nhiêu ước nguyên dương của số 18?", "answer": "6"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số nguyên x dương nhỏ nhất sao cho x chia hết cho cả -4 và 6.", "answer": "12"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Viết tập hợp tất cả các ước nguyên của số -10.\nb) Tìm tất cả các bội của 4 nằm trong khoảng từ -15 đến 15.",
            "rubric": "a) Ư(-10) = {-10; -5; -2; -1; 1; 2; 5; 10} (0.5đ).\nb) Các bội của 4 trong khoảng (-15; 15) là: -12; -8; -4; 0; 4; 8; 12 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số nguyên x biết:\na) (-4) . x = 32\nb) (x - 2) là ước của 6.",
            "rubric": "a) x = 32 : (-4) = -8 (0.4đ).\nb) (x - 2) ∈ {±1; ±2; ±3; ±6} => x ∈ {-4; -1; 0; 1; 3; 4; 5; 8} (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một công ty kinh doanh có kết quả lợi nhuận trong 4 quý lần lượt là: -40 triệu đồng, 60 triệu đồng, -25 triệu đồng và 85 triệu đồng.\na) Tính tổng lợi nhuận cả năm của công ty.\nb) Tính bình quân lợi nhuận mỗi quý của công ty đó trong năm.",
            "rubric": "a) Tổng lợi nhuận cả năm: (-40) + 60 + (-25) + 85 = 80 (triệu đồng) (0.6đ).\nb) Bình quân mỗi quý: 80 : 4 = 20 (triệu đồng) (0.4đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART3["c3_6_bai5_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 17: Phép chia hết. Ước và bội của một số nguyên - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số nguyên $x$ thỏa mãn $(-72) : x = -8$ là:", "options": ["$9$", "$-9$", "$8$", "$-8$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $15$ chia hết cho $(x + 1)$?", "options": ["$8$", "$4$", "$6$", "$2$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tập hợp các số nguyên $x$ vừa là ước của $20$, vừa là bội của $-4$ là:", "options": ["$\\{\\pm 4; \\pm 20\\}$", "$\\{4; 20\\}$", "$\\{-20; -4; 0; 4; 20\\}$", "$\\{\\pm 1; \\pm 2; \\pm 4\\}$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Giá trị của biểu thức $[(-100) : (-5)] : [(-8) + 6]$ là:", "options": ["$-10$", "$10$", "$-20$", "$20$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Số tự nhiên $a$ lớn nhất thỏa mãn $(-36)$ chia hết cho $a$ và $48$ chia hết cho $a$ là:", "options": ["$12$", "$6$", "$24$", "$4$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Nếu số nguyên $x$ chia hết cho $8$ và $x$ chia hết cho $(-12)$ thì $x$ là bội của:", "options": ["$24$", "$4$", "$48$", "$96$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Tổng của tất cả các ước nguyên của số $25$ bằng:", "options": ["$0$", "$31$", "$25$", "$1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Để $(n + 5)$ chia hết cho $(n + 1)$ với $n$ là số tự nhiên, giá trị lớn nhất của $n$ là:", "options": ["$3$", "$4$", "$2$", "$1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cho hai số nguyên $a, b \\neq 0$. Biết $a$ chia hết cho $b$ và $b$ chia hết cho $a$. Khi đó:", "options": ["$a = b$ hoặc $a = -b$", "$a = b$", "$a = -b$", "$a > b$"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ biết: $3x - (-5) = -16$.", "options": ["$x = -7$", "$x = 7$", "$x = -3$", "$x = 3$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số các cặp số nguyên $(x; y)$ thỏa mãn $(x - 1)(y + 2) = 5$ là:", "options": ["$4$", "$2$", "$8$", "$1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Nhiệt độ phòng lạnh giảm đều đặn mỗi giờ. Sau 6 giờ nhiệt độ giảm tổng cộng 18°C. Trung bình mỗi giờ nhiệt độ thay đổi bao nhiêu độ C?", "options": ["$-3^\\circ\\text{C}$", "$3^\\circ\\text{C}$", "$-2^\\circ\\text{C}$", "$-4^\\circ\\text{C}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho a và b là các số nguyên. Xét tính đúng/sai của các khẳng định sau:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu tổng (a + b) chia hết cho 7 và a chia hết cho 7 thì b chia hết cho 7.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu tích a . b chia hết cho 6 thì chắc chắn a chia hết cho 6 hoặc b chia hết cho 6.", "correct": False},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tổng tất cả các ước nguyên của số 12 bằng 0.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số đối của một bội của 5 cũng là một bội của 5.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm x nguyên để phân số 7/(x - 3) nhận giá trị nguyên:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Để phân số nhận giá trị nguyên thì (x - 3) phải là ước của 7.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Có đúng 4 giá trị nguyên của x thỏa mãn bài toán.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Giá trị nguyên lớn nhất của x để phân số nhận giá trị nguyên dương là x = 10.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Khi x = -4 thì giá trị của phân số bằng 1.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số nguyên âm x lớn nhất thỏa mãn x chia hết cho 7.", "answer": "-7"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số nguyên x biết: (2x + 1) là ước của 10 và x > 0.", "answer": "2"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính giá trị biểu thức: A = [(-45) : (-9)] . (-4) + (-32) : (-8).", "answer": "-16"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số nguyên n để (2n + 7) chia hết cho (n + 1). Tính tổng tất cả các giá trị nguyên của n tìm được.", "answer": "-8"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm số nguyên x biết:\na) 48 : (x + 2) = -6\nb) (2x - 3) . (y + 1) = 7 (với x, y là các số nguyên).",
            "rubric": "a) x + 2 = -8 => x = -10 (0.4đ).\nb) (2x - 3)(y + 1) = 7 => tìm được 4 cặp (x; y): (2; 6), (1; -8), (5; 0), (-2; -2) (0.6đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức A = (3n + 8) / (n + 2) với n là số nguyên.\na) Viết A dưới dạng tổng của một số nguyên và một phân số.\nb) Tìm tất cả các số nguyên n để biểu thức A nhận giá trị nguyên.",
            "rubric": "a) A = 3 + 2/(n + 2) (0.4đ).\nb) n + 2 ∈ Ư(2) = {±1; ±2} => n ∈ {-4; -3; -1; 0} (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một tàu lặn khảo sát đáy biển đang ở độ sâu 180 m dưới mực nước biển (độ cao -180 m). Tàu bắt đầu nổi lên đều đặn với tốc độ 15 mét mỗi phút.\na) Viết biểu thức số biểu thị độ cao của tàu sau t phút nổi lên.\nb) Sau bao nhiêu phút thì tàu nổi lên đến vị trí cách mực nước biển 30 m?",
            "rubric": "a) Biểu thức độ cao: h = -180 + 15t (m) với t ≥ 0 (0.5đ).\nb) Vị trí -30 m: -180 + 15t = -30 => 15t = 150 => t = 10 (phút) (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART3["c3_6_bai5_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 17: Phép chia hết. Ước và bội của một số nguyên - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Có bao nhiêu cặp số nguyên $(x; y)$ thỏa mãn $x \\cdot y = -12$ và $x < y$?", "options": ["$6$", "$4$", "$8$", "$3$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số nguyên $n$ để biểu thức $P = (n^2 + 3n + 5)$ chia hết cho $(n + 3)$:", "options": ["$n \\in \\{-8; -4; -2; 2\\}$", "$n \\in \\{-4; -2; 1; 3\\}$", "$n \\in \\{\\pm 1; \\pm 5\\}$", "$n \\in \\{-2; 2\\}$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho $a, b$ là các số nguyên sao cho $(3a + 2b)$ chia hết cho $17$. Khi đó $(10a + b)$ chia hết cho:", "options": ["$17$", "$34$", "$3$", "$7$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm giá trị nguyên của $x$ để phân số $(2x + 3) / (x - 2)$ đạt giá trị nguyên nhỏ nhất:", "options": ["$x = 1$", "$x = 3$", "$x = -5$", "$x = 9$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Số dư khi chia tổng $S = 2 + 2^2 + 2^3 + \\dots + 2^{60}$ cho $7$ là:", "options": ["$0$", "$1$", "$2$", "$3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Tích của hai số nguyên chẵn liên tiếp luôn chia hết cho:", "options": ["$8$", "$6$", "$12$", "$16$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm số nguyên $x$ để $(x + 1)(x - 3) < 0$:", "options": ["$x \\in \\{0; 1; 2\\}$", "$x \\in \\{-1; 0; 1; 2; 3\\}$", "$x > 3$ hoặc $x < -1$", "$x \\in \\{-2; -1; 0\\}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $A = 1 - 3 + 3^2 - 3^3 + \\dots + 3^{100}$. Khi đó $4A - 1$ chia hết cho:", "options": ["$3^{101}$", "$3^{100}$", "$9$", "$27$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên $n$ để $(n^2 - 2)$ chia hết cho $(n - 1)$?", "options": ["$2$", "$4$", "$6$", "$0$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số nghiệm nguyên $(x; y)$ của phương trình $xy + 2x - 3y = 11$ là:", "options": ["$4$", "$2$", "$8$", "$6$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Biểu thức $n^3 - n$ luôn chia hết cho số nào sau đây với mọi số nguyên $n$?", "options": ["$6$", "$8$", "$9$", "$12$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $B = 5 + 5^2 + 5^3 + \\dots + 5^{96}$. Chữ số tận cùng của biểu thức $B$ là:", "options": ["$0$", "$5$", "$2$", "$8$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho a, b, c là các số nguyên. Xét tính đúng/sai của các mệnh đề số học sau:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu a chia hết cho b thì a^2 chia hết cho b^2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu a^2 chia hết cho b thì chắc chắn a chia hết cho b.", "correct": False},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tích của ba số nguyên liên tiếp luôn chia hết cho 6.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nếu a + b chia hết cho c thì cả a và b đều phải chia hết cho c.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm cặp số nguyên (x; y) thỏa mãn 2xy - x + 4y = 10:",
            "statements": [
                {"key": "a", "level": "Vận dụng thấp", "text": "Đưa phương trình về dạng tích ta được (2y - 1)(x + 2) = 8.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "2y - 1 là số lẻ nên 2y - 1 chỉ có thể nhận các giá trị là ước lẻ của 8.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Có tất cả 4 cặp số nguyên (x; y) thỏa mãn phương trình.", "correct": False},
                {"key": "d", "level": "Vận dụng cao", "text": "Cặp (x; y) = (6; 1) là một nghiệm của phương trình.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số nguyên n lớn nhất sao cho (n + 13) chia hết cho (n - 2).", "answer": "17"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên n thỏa mãn: 3^(n+2) - 3^n = 216.", "answer": "3"},
        {"id": 3, "level": "Vận dụng cao", "question": "Có bao nhiêu cặp số nguyên dương (x; y) thỏa mãn 1/x + 1/y = 1/3?", "answer": "3"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số dư khi chia A = 1 + 4 + 4^2 + ... + 4^2024 cho 5.", "answer": "1"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "a) Tìm tất cả các số nguyên n sao cho A = (2n + 5) / (n - 1) có giá trị là số nguyên.\nb) Tìm n nguyên để A đạt giá trị lớn nhất.",
            "rubric": "a) A = 2 + 7/(n - 1) => n - 1 ∈ Ư(7) => n ∈ {-6; 0; 2; 8} (0.5đ).\nb) A lớn nhất khi n - 1 = 1 => n = 2. Giá trị max = 9 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm các cặp số nguyên (x; y) thỏa mãn:\nxy - 2x + 5y = 17.",
            "rubric": "(x + 5)(y - 2) = 7 (0.4đ). Xét các ước của 7 => 4 cặp nghiệm: (-4; 9), (-6; -5), (2; 3), (-12; 1) (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức S = 3 + 3^2 + 3^3 + ... + 3^100.\na) Chứng minh rằng S chia hết cho 4.\nb) Tìm số dư khi chia S cho 13.",
            "rubric": "a) Ghép từng cặp 2 số: S = 4 . (3 + 3^3 + ... + 3^99) => S chia hết cho 4 (0.5đ).\nb) S = 3 + (3^2 + 3^3 + 3^4) + ... Mỗi nhóm 3 số chia hết cho 13, dư 3 ở đầu => S chia 13 dư 3 (0.5đ)."
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG III: SỐ NGUYÊN (c3_6_bai6)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART3["c3_6_bai6_test1"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương III: Số nguyên - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tập hợp các số nguyên $\\mathbb{Z}$ bao gồm:", "options": ["Các số nguyên âm, số 0 và các số nguyên dương", "Số tự nhiên và phân số", "Chỉ gồm số nguyên âm và số nguyên dương", "Số 0 và các số nguyên âm"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Số đối của số $-15$ là:", "options": ["$15$", "$-15$", "$0$", "$1/15$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Sắp xếp các số sau theo thứ tự tăng dần: $-7; 0; 5; -2$:", "options": ["$-7 < -2 < 0 < 5$", "$-2 < -7 < 0 < 5$", "$5 < 0 < -2 < -7$", "$-7 < 0 < -2 < 5$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Kết quả của phép tính $(-14) + (-6)$ là:", "options": ["$-20$", "$20$", "$-8$", "$8$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Kết quả của phép tính $15 - 23$ là:", "options": ["$-8$", "$8$", "$-38$", "$38$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Tích $(-4) \\cdot (-7)$ bằng:", "options": ["$28$", "$-28$", "$11$", "$-11$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Thương $(-45) : 9$ bằng:", "options": ["$-5$", "$5$", "$-6$", "$6$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Quy tắc phá ngoặc nào sau đây là đúng?", "options": ["$-(a - b + c) = -a + b - c$", "$-(a - b + c) = -a - b + c$", "$+(a - b + c) = a + b + c$", "$-(a - b + c) = -a - b - c$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Tìm $x$ biết: $x + 8 = 3$.", "options": ["$x = -5$", "$x = 5$", "$x = 11$", "$x = -11$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Tập hợp tất cả các ước của số $6$ trong $\\mathbb{Z}$ là:", "options": ["$\\{-6; -3; -2; -1; 1; 2; 3; 6\\}$", "$\\{1; 2; 3; 6\\}$", "$\\{\\pm 1; \\pm 2; \\pm 3\\}$", "$\\{0; 1; 2; 3; 6\\}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Nhiệt độ buổi sáng là $-3^\\circ\\text{C}$, đến trưa tăng thêm $5^\\circ\\text{C}$. Nhiệt độ buổi trưa là:", "options": ["$2^\\circ\\text{C}$", "$-8^\\circ\\text{C}$", "$8^\\circ\\text{C}$", "$-2^\\circ\\text{C}$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Giá trị của biểu thức $(-2)^3$ bằng:", "options": ["$-8$", "$8$", "$-6$", "$6$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Xét tính đúng/sai của các phát biểu tổng quát sau:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Mọi số nguyên âm đều nhỏ hơn 0 và nhỏ hơn mọi số nguyên dương.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Tích của hai số nguyên âm là một số nguyên âm.", "correct": False},
                {"key": "c", "level": "Nhận biết", "text": "Số 0 không phải là số nguyên âm, cũng không phải là số nguyên dương.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Hiệu của hai số nguyên âm luôn luôn là một số nguyên âm.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho phép tính M = 15 - (8 - 12) + (-6). Xét tính đúng/sai của các bước:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Giá trị trong ngoặc (8 - 12) bằng -4.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Bỏ dấu ngoặc đúng: M = 15 - 8 + 12 - 6.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Giá trị của biểu thức M bằng 13.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "M chia hết cho 5.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = (-25) . 4 + (-18) : (-2).", "answer": "-91"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số nguyên x thỏa mãn: 2x - 7 = -19.", "answer": "-6"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính tổng của tất cả các số nguyên x thỏa mãn: -4 < x ≤ 4.", "answer": "4"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Một tàu ngầm lặn từ vị trí -40 m xuống thêm 35 m nữa. Hỏi vị trí mới của tàu ngầm ở độ cao bao nhiêu mét?", "answer": "-75"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính hợp lý nếu có thể:\na) 37 . (-45) + (-45) . 63\nb) 125 - [48 + (125 - 48)].",
            "rubric": "a) (-45) . (37 + 63) = (-45) . 100 = -4500 (0.5đ).\nb) 125 - [48 + 125 - 48] = 125 - 125 = 0 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số nguyên x biết:\na) 15 - 3x = 36\nb) (x + 3) . (x - 2) = 0.",
            "rubric": "a) 3x = -21 => x = -7 (0.5đ).\nb) x + 3 = 0 hoặc x - 2 = 0 => x ∈ {-3; 2} (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Bác An kinh doanh trong 5 tháng đầu năm ghi nhận lợi nhuận như sau: tháng 1 lãi 12 triệu, tháng 2 lỗ 5 triệu, tháng 3 lãi 18 triệu, tháng 4 lỗ 8 triệu, tháng 5 hòa vốn.\na) Tính tổng lợi nhuận của bác An trong 5 tháng.\nb) Bình quân mỗi tháng bác An lãi hay lỗ bao nhiêu tiền?",
            "rubric": "a) Tổng lợi nhuận: 12 + (-5) + 18 + (-8) + 0 = 17 (triệu đồng) (0.6đ).\nb) Trung bình mỗi tháng: 17 : 5 = 3,4 (triệu đồng). Kết luận bác An lãi bình quân 3,4 triệu đồng/tháng (0.4đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART3["c3_6_bai6_test2"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương III: Số nguyên - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Giá trị của biểu thức $(-3)^2 - (-2)^3$ là:", "options": ["$17$", "$1$", "$-17$", "$-1$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Số nguyên $x$ thỏa mãn: $(-15) - x = 8$ là:", "options": ["$-23$", "$23$", "$-7$", "$7$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tổng tất cả các số nguyên $x$ thỏa mãn $-8 \\leq x < 7$ là:", "options": ["$-15$", "$-8$", "$-7$", "$0$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tích của 5 số nguyên âm và 4 số nguyên dương là một số mang dấu:", "options": ["Dấu âm $(-)$", "Dấu dương $(+)$", "Không xác định", "Bằng 0"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $12$ chia hết cho $(2x - 1)$?", "options": ["$4$", "$6$", "$8$", "$12$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Giá trị của biểu thức $180 : [(-12) + 2 \\cdot (-3)]$ là:", "options": ["$-10$", "$10$", "$-15$", "$15$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Để tích $(x - 2)(x + 5) = 0$ thì $x$ nhận các giá trị là:", "options": ["$x = 2$ hoặc $x = -5$", "$x = -2$ hoặc $x = 5$", "$x = 2$ hoặc $x = 5$", "$x = -2$ hoặc $x = -5$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tập hợp các ước chung của $18$ và $-30$ trong $\\mathbb{Z}$ có bao nhiêu phần tử?", "options": ["$8$", "$4$", "$6$", "$12$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm số nguyên $x$ biết: $(x - 4)^2 = 25$.", "options": ["$x = 9$ hoặc $x = -1$", "$x = 9$", "$x = -1$", "$x = 1$ hoặc $x = -9$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Nhiệt độ lúc 6h sáng ở Sa Pa là $-2^\\circ\\text{C}$, trưa tăng $7^\\circ\\text{C}$, đêm giảm $9^\\circ\\text{C}$ so với buổi trưa. Nhiệt độ đêm là:", "options": ["$-4^\\circ\\text{C}$", "$4^\\circ\\text{C}$", "$0^\\circ\\text{C}$", "$-14^\\circ\\text{C}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $a$ là số nguyên âm, $b$ là số nguyên dương. Khẳng định nào sau đây đúng?", "options": ["$a - b < 0$", "$a - b > 0$", "$a - b = 0$", "Không xác định"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $P = -(x - y + z) - (y - x - z)$ ta được:", "options": ["$0$", "$-2z$", "$2x - 2y$", "$-2y$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho x, y là các số nguyên. Xét tính đúng/sai của các phát biểu sau:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu x . y > 0 thì x và y cùng dấu.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu x + y = 0 thì x và y là hai số đối nhau.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Với mọi số nguyên x thì x^2 > 0.", "correct": False},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nếu x chia hết cho 4 và chia hết cho 6 thì x chắc chắn chia hết cho 24.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét biểu thức Q = (-2)^4 - 3 . (-5) + (-48) : (-6):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "(-2)^4 = 16.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "(-3) . (-5) = 15.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "(-48) : (-6) = -8.", "correct": False},
                {"key": "d", "level": "Vận dụng thấp", "text": "Giá trị của biểu thức Q bằng 39.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính nhanh giá trị của: A = 27 . 39 + 27 . 63 - 27 . 2.", "answer": "2700"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số nguyên x thỏa mãn: 3x - (-12) = -18.", "answer": "-10"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số nguyên dương n nhỏ nhất sao cho (n + 4) chia hết cho (n - 1).", "answer": "2"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính tổng các số nguyên x thỏa mãn: -15 ≤ x < 16.", "answer": "0"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính một cách hợp lý:\na) 45 - 5 . (-12) + (-24) : 4\nb) (-125) . 37 . (-8) . (-1)^2024.",
            "rubric": "a) 45 + 60 - 6 = 99 (0.5đ).\nb) [(-125) . (-8)] . 37 . 1 = 1000 . 37 = 37000 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số nguyên x biết:\na) 2(x - 5) - 3(x + 1) = -14\nb) (2x - 1) là ước của 18 và x là số nguyên âm.",
            "rubric": "a) -x - 13 = -14 => x = 1 (0.4đ).\nb) 2x - 1 ∈ {±1; ±3; ±9} và x âm => x ∈ {-4; -1} (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một công ty nhập 100 chiếc máy tính bảng giá 6 triệu đồng/chiếc. Tháng 1 bán được 70 chiếc giá 7,5 triệu/chiếc. Tháng 2 bán 30 chiếc còn lại giá 5 triệu/chiếc. Chi phí vận chuyển bảo quản là 20 triệu. Hỏi công ty lãi hay lỗ bao nhiêu tiền?",
            "rubric": "Tổng chi phí: 100 . 6 + 20 = 620 (triệu). Doanh thu: 70 . 7,5 + 30 . 5 = 675 (triệu). Lợi nhuận: 675 - 620 = 55 (triệu). Kết luận công ty lãi 55 triệu đồng (1.0đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART3["c3_6_bai6_test3"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương III: Số nguyên - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tổng $S = 1 - 2 + 3 - 4 + 5 - 6 + \\dots + 2023 - 2024$. Giá trị của $S$ là:", "options": ["$-1012$", "$1012$", "$-2024$", "$0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Số nghiệm nguyên $(x; y)$ của phương trình $(x + 1)(y - 3) = 6$ là:", "options": ["$8$", "$4$", "$12$", "$6$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên $n$ để phân số $(3n + 2) / (n - 1)$ nhận giá trị nguyên?", "options": ["$4$", "$2$", "$6$", "$8$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = (x - 3)^2 + |y + 2| - 7$ với $x, y \\in \\mathbb{Z}$:", "options": ["$-7$", "$0$", "$7$", "$-5$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Nếu số nguyên $a$ chia $5$ dư $3$ và $b$ chia $5$ dư $2$ thì tích $a \\cdot b$ chia $5$ dư bao nhiêu?", "options": ["$1$", "$0$", "$6$", "$4$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $x$ thỏa mãn: $2^x + 2^{x+3} = 144$.", "options": ["$x = 4$", "$x = 3$", "$x = 5$", "$x = 2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho các số nguyên $a, b, c$ thỏa mãn $a + b + c = 0$. Biểu thức $M = (a + b)(b + c)(c + a)$ bằng:", "options": ["$-abc$", "$abc$", "$0$", "$a^3 + b^3 + c^3$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm các số nguyên $x$ để $(x^2 - 1)(x^2 - 10) < 0$:", "options": ["$x \\in \\{\\pm 2; \\pm 3\\}$", "$x \\in \\{-3; -2; 2; 3\\}$", "$1 < x^2 < 10$", "Cả ba đáp án đều đúng"], "correct": 3},
        {"id": 9, "level": "Vận dụng cao", "question": "Số dư khi chia $2^{100}$ cho $3$ là:", "options": ["$1$", "$2$", "$0$", "Không xác định"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tích của 4 số nguyên liên tiếp cộng thêm 1 luôn là:", "options": ["Một số chính phương lẻ", "Một số chính phương chẵn", "Một số chia hết cho 5", "Một số nguyên tố"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $x \\in \\mathbb{Z}$ sao cho $(x^2 + 1)$ chia hết cho $(x - 1)$. Giá trị nguyên lớn nhất của $x$ là:", "options": ["$3$", "$2$", "$1$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Biết tổng $1 + 2 + 3 + \\dots + n = 120$. Giá trị của số tự nhiên $n$ là:", "options": ["$15$", "$16$", "$14$", "$20$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho n là số nguyên. Xét tính đúng/sai của các mệnh đề số học sau:",
            "statements": [
                {"key": "a", "level": "Vận dụng thấp", "text": "Biểu thức n(n + 1)(2n + 1) luôn chia hết cho 6 với mọi số nguyên n.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Nếu n^2 là số chẵn thì n chắc chắn là số chẵn.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Biểu thức n^2 + n + 1 luôn là số nguyên tố với mọi số tự nhiên n.", "correct": False},
                {"key": "d", "level": "Vận dụng cao", "text": "Tồn tại số nguyên n để n^2 + 1 chia hết cho 3.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm cặp số nguyên (x; y) thỏa mãn xy - 3x + y = 7:",
            "statements": [
                {"key": "a", "level": "Vận dụng thấp", "text": "Biến đổi tương đương đưa về dạng (x + 1)(y - 3) = 4.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Số 4 có đúng 6 ước nguyên.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Có đúng 6 cặp số nguyên (x; y) thỏa mãn phương trình.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Không có cặp nghiệm nào có cả x và y cùng là số nguyên dương.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số nguyên âm x thỏa mãn: |2x - 3| = 7.", "answer": "-2"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tính tổng S = 2 - 4 + 6 - 8 + ... + 98 - 100.", "answer": "-50"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm giá trị lớn nhất của biểu thức: P = 2024 - (x + 1)^2 - |y - 2|.", "answer": "2024"},
        {"id": 4, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên n thỏa mãn (n^2 + 2) chia hết cho (n + 1)?", "answer": "4"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "a) Cho biểu thức A = 1 - 2 + 2^2 - 2^3 + ... + 2^100. Tính giá trị của 3A - 2^101.\nb) Chứng minh rằng với mọi số tự nhiên n thì phân số (12n + 1) / (30n + 2) là phân số tối giản.",
            "rubric": "a) 2A = 2 - 2^2 + ... + 2^101 => 3A = 1 + 2^101 => 3A - 2^101 = 1 (0.5đ).\nb) Gọi d = ƯCLN(12n + 1, 30n + 2) => 5(12n + 1) - 2(30n + 2) = 1 chia hết cho d => d = 1 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các cặp số nguyên (x; y) thỏa mãn phương trình:\n2xy - 3x + y = 4.",
            "rubric": "Nhân 2: (2x + 1)(2y - 3) = 5 (0.4đ). Ước của 5 => 4 cặp: (0; 4), (-1; -1), (2; 2), (-3; 1) (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho 2024 số nguyên, trong đó tích của 3 số bất kì luôn là một số âm.\na) Chứng minh rằng trong 2024 số đó có ít nhất một số âm.\nb) Hỏi tích của cả 2024 số đó mang dấu gì? Giải thích chi tiết.",
            "rubric": "a) Phản chứng: nếu không có số âm nào thì tích 3 số bất kì ≥ 0 (mâu thuẫn), vậy có ít nhất 1 số âm a (0.4đ).\nb) Với a < 0, 2 số bất kì b, c có a.b.c < 0 => b.c > 0. Vậy 2023 số còn lại cùng dấu. Nếu cùng dương thì tích 3 số dương là dương (vô lý). Vậy cả 2024 số đều âm. Tích của 2024 số âm (chẵn số âm) là số DƯƠNG (0.6đ)."
        }
    ]
}
