# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 6 - CHƯƠNG III: SỐ NGUYÊN
PHẦN 2: BÀI 15 (QUY TẮC DẤU NGOẶC) & BÀI 16 (PHÉP NHÂN SỐ NGUYÊN)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025.
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 15: QUY TẮC DẤU NGOẶC (c3_6_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c3_6_bai3_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 15: Quy tắc dấu ngoặc - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Khi bỏ dấu ngoặc có dấu \"+\" đằng trước, ta làm như sau:", "options": ["Giữ nguyên dấu của các số hạng trong ngoặc", "Đổi dấu tất cả các số hạng trong ngoặc", "Đổi dấu số hạng đầu tiên", "Đổi dấu số hạng cuối cùng"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Khi bỏ dấu ngoặc có dấu \"-\" đằng trước, ta làm như sau:", "options": ["Đổi dấu tất cả các số hạng trong ngoặc", "Giữ nguyên dấu của các số hạng trong ngoặc", "Chỉ đổi dấu số hạng mang dấu trừ", "Chỉ đổi dấu số hạng đầu tiên"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Bỏ dấu ngoặc biểu thức $-(a - b + c)$ ta được:", "options": ["$-a + b - c$", "$-a - b + c$", "$-a - b - c$", "$a - b + c$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Bỏ dấu ngoặc biểu thức $+(x - y + z)$ ta được:", "options": ["$x - y + z$", "$-x + y - z$", "$x + y + z$", "$-x - y + z$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Biểu thức $a - (b + c)$ bằng biểu thức nào sau đây?", "options": ["$a - b - c$", "$a - b + c$", "$a + b - c$", "$a + b + c$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Đặt dấu ngoặc có dấu \"-\" đằng trước cho biểu thức $-x + y - z$ ta được:", "options": ["$-(x - y + z)$", "$-(x + y - z)$", "$-(-x - y + z)$", "$-(x + y + z)$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tính hợp lí: $A = 215 - (115 + 40)$:", "options": ["$60$", "$140$", "$160$", "$50$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Rút gọn biểu thức $M = (a + b) - (a - b)$:", "options": ["$2b$", "$2a$", "$0$", "$a + 2b$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Kết quả của phép tính $(-35) - (20 - 35)$ là:", "options": ["$-20$", "$20$", "$-50$", "$0$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Tính $B = (123 - 45) - (123 + 55)$:", "options": ["$-100$", "$100$", "$10$", "$-10$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tìm $x$ biết $x - (12 - 5) = -10$:", "options": ["$x = -3$", "$x = 3$", "$x = -17$", "$x = 17$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Giá trị của biểu thức $P = -(15 - 28) - 28$ bằng:", "options": ["$-15$", "$15$", "$41$", "$-41$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A = (27 + 65) + (346 - 27 - 65)$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Bỏ dấu ngoặc ta được $A = 27 + 65 + 346 - 27 - 65$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nhóm các số hạng đối nhau: $(27 - 27) + (65 - 65) = 0$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Giá trị của biểu thức $A$ là $346$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nếu thay $346$ bằng $-100$ thì giá trị của $A$ bằng $100$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho biểu thức $B = (a - b) - (c - d) + (b + c)$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Bỏ dấu ngoặc đúng: $B = a - b - c + d + b + c$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Các số hạng đối nhau triệt tiêu: $(-b + b) = 0$ và $(-c + c) = 0$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Biểu thức rút gọn là $B = a + d$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Khi $a = 15, d = -5$ thì giá trị của $B$ bằng $20$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: $S = (123 - 45) - 123$.", "answer": "-45"},
        {"id": 2, "level": "Thông hiểu", "question": "Rút gọn biểu thức $P = x - (x - y) + (y - z) + z$. Kết quả bằng mấy $y$?", "answer": "2"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính: $A = (15 - 28) - (15 - 28 + 42)$.", "answer": "-42"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ biết $25 - (x + 5) = -10$.", "answer": "30"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Bỏ dấu ngoặc rồi tính giá trị của các biểu thức sau:\na) $A = (135 - 47) - (135 - 47 + 50)$.\nb) $B = -(24 - 115) + (35 - 115)$.",
            "rubric": "a) A = 135 - 47 - 135 + 47 - 50 = (135 - 135) + (-47 + 47) - 50 = -50 (0.5đ).\nb) B = -24 + 115 + 35 - 115 = (115 - 115) + (35 - 24) = 11 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Rút gọn các biểu thức sau:\na) $M = (a + b - c) - (b - c + d)$.\nb) $N = -(x - y + z) + (x + y - z) - (y - z)$.",
            "rubric": "a) M = a + b - c - b + c - d = a + (b - b) + (-c + c) - d = a - d (0.5đ).\nb) N = -x + y - z + x + y - z - y + z = (-x + x) + (y + y - y) + (-z - z + z) = y - z (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tìm số nguyên $x$ biết:\na) $15 - (x - 7) = -8$.\nb) $(x - 3) - (2x + 5) = 10$.",
            "rubric": "a) 15 - x + 7 = -8 => 22 - x = -8 => x = 22 - (-8) = 30 (0.5đ).\nb) x - 3 - 2x - 5 = 10 => -x - 8 = 10 => -x = 18 => x = -18 (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c3_6_bai3_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 15: Quy tắc dấu ngoặc - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của $P = (12 - 34 + 56) - (56 + 12 - 34)$:", "options": ["$0$", "$24$", "$-68$", "$112$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $M = a - (b - c)$ và $N = (a - b) + c$. Khẳng định nào sau đây là đúng?", "options": ["$M = N$", "$M = -N$", "$M = N - 2c$", "$M = N + 2b$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Rút gọn biểu thức $A = -(a - b - c) - (-a + b + c)$:", "options": ["$0$", "$-2a + 2b + 2c$", "$2b + 2c$", "$-2a$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tính $S = (2024 - 15) - (2024 - 35)$:", "options": ["$20$", "$-20$", "$50$", "$-50$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tìm $x$ biết $(x - 4) - (12 - 4) = -20$:", "options": ["$x = -8$", "$x = 8$", "$x = -12$", "$x = 12$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Cho $a - b = 5$. Giá trị của biểu thức $P = (a + c) - (b + c)$ là:", "options": ["$5$", "$5 + 2c$", "$-5$", "$0$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Tính tổng $A = (1 - 2) + (3 - 4) + (5 - 6) + \\dots + (99 - 100)$:", "options": ["$-50$", "$50$", "$-100$", "$0$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Rút gọn $K = (x + y - z) - (x - y + z) - (y + z)$:", "options": ["$y - 3z$", "$y + z$", "$3y - z$", "$-3z$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cho $x - y = -3$. Giá trị của $Q = (x + 2) - (y - 5)$ là:", "options": ["$4$", "$-4$", "$-6$", "$10$"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Tính $M = [12 - (-15 + 4)] - (12 + 15 - 4)$:", "options": ["$0$", "$22$", "$-22$", "$30$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ biết $10 - [x - (5 - 2)] = 15$:", "options": ["$-2$", "$2$", "$8$", "$-8$"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Biểu thức $-(x - y - z) + (x - y - z)$ rút gọn được:", "options": ["$0$", "$-2x + 2y + 2z$", "$2y + 2z$", "$-2x$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $P = (a - b + c) - (a + c - b) + (b - c)$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Bỏ ngoặc hai nhóm đầu: $(a - b + c) - (a + c - b) = a - b + c - a - c + b = 0$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Biểu thức $P$ rút gọn thành $P = b - c$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Khi $b = 12, c = 20$ thì giá trị của $P$ bằng $-8$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Giá trị của biểu thức $P$ phụ thuộc vào giá trị của biến $a$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho ba số nguyên $x, y, z$ thỏa mãn $x - y = 8$ và $y - z = -5$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Xét hiệu $(x - y) + (y - z) = x - z$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Giá trị của $x - z = 8 + (-5) = 3$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Biểu thức $K = (x - z) + (z - y)$ có giá trị bằng $8$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Ta có $x < y < z$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính $S = (45 - 3750) - (29 - 3750)$.", "answer": "16"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $(x + 12) - (15 - 20) = -8$.", "answer": "-25"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho $a - b = 10$. Tính giá trị của biểu thức $(a + 5) - (b - 5)$.", "answer": "20"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Rút gọn $A = -(x - y) - (y - z) - (z - x)$. Kết quả bằng bao nhiêu?", "answer": "0"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính một cách hợp lí:\na) $A = (27 + 65) + (346 - 27 - 65)$.\nb) $B = (42 - 69 + 17) - (42 + 17)$.",
            "rubric": "a) A = 27 + 65 + 346 - 27 - 65 = (27 - 27) + (65 - 65) + 346 = 346 (0.5đ).\nb) B = 42 - 69 + 17 - 42 - 17 = (42 - 42) + (17 - 17) - 69 = -69 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Chứng minh rằng giá trị của biểu thức sau không phụ thuộc vào giá trị của biến:\n$P = (a + b - c) - (b - c + d) + (c + d - a) - c$.",
            "rubric": "Bỏ dấu ngoặc:\nP = a + b - c - b + c - d + c + d - a - c (0.4đ).\nNhóm các số hạng đồng dạng:\nP = (a - a) + (b - b) + (-c + c + c - c) + (-d + d) (0.4đ)\nP = 0 + 0 + 0 + 0 = 0 (0.2đ).\nVậy biểu thức P luôn bằng 0, không phụ thuộc vào các biến a, b, c, d."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tìm số nguyên $x$ biết:\na) $(x - 5) - (2x + 3) = -12$.\nb) $18 - [x - (3 - 7)] = -5$.",
            "rubric": "a) x - 5 - 2x - 3 = -12 => -x - 8 = -12 => -x = -4 => x = 4 (0.5đ).\nb) 18 - [x - (-4)] = -5 => 18 - (x + 4) = -5 => 18 - x - 4 = -5 => 14 - x = -5 => x = 19 (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c3_6_bai3_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 15: Quy tắc dấu ngoặc - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $S_n = (1 - 2) + (3 - 4) + \\dots + [(2n - 1) - 2n]$. Biểu thức rút gọn của $S_n$ theo $n$ là:", "options": ["$-n$", "$n$", "$-2n$", "$0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Rút gọn biểu thức $A = -[-(-a + b) - (c - d)] - (a + d)$:", "options": ["$-b + c$", "$b - c$", "$2a - b + c$", "$-2a + b - c$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho $a + b - c = 20$. Giá trị của biểu thức $M = (a + 5) - (c - 8) + (b - 3)$ là:", "options": ["$30$", "$10$", "$25$", "$14$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm $x$ biết $x - \\{x - [x - (x - 1)]\\} = 0$:", "options": ["$x = 1$", "$x = 0$", "$x = -1$", "Vô số $x$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Cho các số nguyên $a, b, c, d$ thỏa mãn $a + b = c + d$. Khi đó $(a - c) - (d - b)$ bằng:", "options": ["$0$", "$2a$", "$2d$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $A = 1 - 2 + 3 - 4 + \\dots + 2023 - 2024$. Giá trị của $2024 - A$ bằng:", "options": ["$3036$", "$1012$", "$2024$", "$-1012$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Biết $(x - y + z) - (x + y - z) = 10$. Hiệu $z - y$ bằng:", "options": ["$5$", "$10$", "$-5$", "$-10$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của $A = |x - 1| - (x - 1)$ khi $x \\leq 1$:", "options": ["$2(1 - x)$", "$0$", "$1$", "$-2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $S = a_1 - a_2 + a_3 - a_4 + \\dots + a_{99} - a_{100}$. Nếu đổi dấu tất cả các số hạng của $S$ thì tổng mới bằng:", "options": ["$-S$", "$S$", "$0$", "$2S$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho 4 số nguyên $a, b, c, d$. Nếu $(a - b) + (c - d) = (a + c) - (b + d)$ thì đẳng thức này:", "options": ["Luôn đúng với mọi $a, b, c, d$", "Chỉ đúng khi $a = b = c = d$", "Chỉ đúng khi $a = b$", "Chỉ đúng khi $c = d$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm $x$ biết: $(x - 1) - (x - 2) + (x - 3) - (x - 4) + \\dots + (x - 99) - (x - 100) = x$:", "options": ["$x = 50$", "$x = -50$", "$x = 100$", "$x = 0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho biểu thức $P = -(a - b - c) - [(-a + b) - (c - d)] - d$. Giá trị của $P$ là:", "options": ["$0$", "$2a$", "$2b$", "$2c$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho dãy biểu thức $T = (a_1 - a_2) + (a_2 - a_3) + (a_3 - a_4) + \\dots + (a_{2024} - a_{2025})$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Khi bỏ dấu ngoặc, các số hạng trung gian $a_2, a_3, \\dots, a_{2024}$ đều xuất hiện một lần mang dấu trừ và một lần mang dấu cộng.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Tất cả các số hạng trung gian bị triệt tiêu từng đôi một.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Biểu thức thu gọn cuối cùng là $T = a_1 - a_{2025}$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Nếu $a_1 = a_{2025}$ thì giá trị của $T$ luôn bằng $1$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho ba số nguyên $a, b, c$. Xét biểu thức $M = a(b - c) - a(b + d) + ad$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Áp dụng tính chất phân phối: $a(b - c) = ab - ac$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ta có $a(b + d) = ab + ad$, khi có dấu trừ đằng trước đổi thành $-ab - ad$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Khai triển và rút gọn: $M = ab - ac - ab - ad + ad = -ac$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Khi $a = 5, c = -4$ thì giá trị của $M$ bằng $-20$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tính giá trị của biểu thức $A = (1 - 2) + (3 - 4) + \\dots + (2023 - 2024)$.", "answer": "-1012"},
        {"id": 2, "level": "Vận dụng cao", "question": "Cho $a - b = -5$ và $c - d = 12$. Tính giá trị của $(a - d) - (b - c)$.", "answer": "7"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số nguyên $x$ thỏa mãn: $1 - (2 - (3 - (4 - x))) = 10$.", "answer": "12"},
        {"id": 4, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $S = (a + b) - (b - c) + (c - d) - (d - a)$. Kết quả bằng mấy lần của $(a + c - d)$?", "answer": "2"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $A = (a - b + c) - (a + c - b) + (b - c) - (b + c)$.\na) Rút gọn biểu thức $A$.\nb) Tính giá trị của $A$ biết $c = -15$.",
            "rubric": "a) Bỏ dấu ngoặc:\nA = a - b + c - a - c + b + b - c - b - c (0.3đ)\n= (a - a) + (-b + b + b - b) + (c - c - c - c) (0.3đ)\n= 0 + 0 - 2c = -2c (0.2đ).\nb) Với c = -15: A = -2 * (-15) = 30 (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tính tổng sau một cách khoa học:\n$S = (1 - 2 - 3 + 4) + (5 - 6 - 7 + 8) + \\dots + (2021 - 2022 - 2023 + 2024)$.",
            "rubric": "Xét nhóm tổng quát 4 số liên tiếp:\nk - (k + 1) - (k + 2) + (k + 3) = k - k - 1 - k - 2 + k + 3 = (k - k - k + k) + (-1 - 2 + 3) = 0 (0.4đ).\nTổng S gồm các nhóm 4 số hạng có giá trị đều bằng 0 (0.3đ).\nTừ 1 đến 2024 có 2024 số, chia thành 2024 : 4 = 506 nhóm (0.15đ).\nVậy S = 506 * 0 = 0 (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm số nguyên $x$ thỏa mãn:\n$(x - 1) + (x - 2) + (x - 3) + \\dots + (x - 20) = -110$.",
            "rubric": "Phá dấu ngoặc: có 20 số x và tổng các số từ 1 đến 20 (0.3đ).\n(x + x + ... + x) - (1 + 2 + 3 + ... + 20) = -110 (0.25đ).\n20x - (20 * 21 : 2) = -110 => 20x - 210 = -110 (0.25đ).\n20x = 210 - 110 = 100 => x = 100 : 20 = 5 (0.2đ)."
        }
    ]
}

# ==============================================================================
# BÀI 16: PHÉP NHÂN SỐ NGUYÊN (c3_6_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c3_6_bai4_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 16: Phép nhân số nguyên - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tích của hai số nguyên cùng dấu luôn là:", "options": ["Một số nguyên dương", "Một số nguyên âm", "Số 0", "Tùy thuộc vào độ lớn của hai số"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Tích của hai số nguyên khác dấu luôn là:", "options": ["Một số nguyên âm", "Một số nguyên dương", "Số 0", "Không xác định"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Kết quả của phép nhân $(-4) \\cdot (-5)$ là:", "options": ["$20$", "$-20$", "$-9$", "$9$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Kết quả của phép nhân $(-6) \\cdot 7$ là:", "options": ["$-42$", "$42$", "$-13$", "$13$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Tích của bất kì số nguyên $a$ nào với số 0 đều bằng:", "options": ["$0$", "$a$", "$-a$", "$1$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Khi nhân một số nguyên $a$ với $-1$, ta được:", "options": ["Số đối của $a$ (tức là $-a$)", "$a$", "$1$", "$-1$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tính: $(-2) \\cdot (-3) \\cdot (-4)$:", "options": ["$-24$", "$24$", "$-9$", "$9$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tích của ba số nguyên âm và hai số nguyên dương là:", "options": ["Một số nguyên âm", "Một số nguyên dương", "Số 0", "Không xác định"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Kết quả của phép tính $(-5)^2$ là:", "options": ["$25$", "$-25$", "$-10$", "$10$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Kết quả của phép tính $(-2)^3$ là:", "options": ["$-8$", "$8$", "$-6$", "$6$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tính nhanh: $(-25) \\cdot 12 \\cdot (-4)$:", "options": ["$1200$", "$-1200$", "$300$", "$-300$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Tìm số nguyên $x$ biết $3 \\cdot x = -15$:", "options": ["$x = -5$", "$x = 5$", "$x = -18$", "$x = -12$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho các biểu thức: $A = (-4) \\cdot (-25) \\cdot 7$, $B = (-12) \\cdot 5 \\cdot (-2)$, $C = (-8) \\cdot 125$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Biểu thức $A = 100 \\cdot 7 = 700$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Biểu thức $B = (-60) \\cdot (-2) = 120$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Biểu thức $C = -1000$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Trong ba biểu thức trên, chỉ có duy nhất biểu thức $C$ mang giá trị âm.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Một xí nghiệp may mỗi ngày sản xuất được $250$ bộ quần áo. Do gặp sự cố mất điện, trong 4 ngày liên tiếp mỗi ngày sản xuất giảm đi $30$ bộ (biểu diễn là $-30$).",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số lượng quần áo bị giảm trong 4 ngày được tính bằng phép nhân $4 \\cdot (-30)$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Kết quả của phép tính $4 \\cdot (-30) = -120$ bộ quần áo.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Trong 4 ngày gặp sự cố, tổng số bộ quần áo thực tế may được là $880$ bộ.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Năng suất mỗi ngày gặp sự cố là $280$ bộ.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính: $(-15) \\cdot (-4) \\cdot 2$.", "answer": "120"},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của lũy thừa $(-3)^4$.", "answer": "81"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ biết: $(-5) \\cdot x = 45$.", "answer": "-9"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tính nhanh: $47 \\cdot (-25) + 53 \\cdot (-25)$.", "answer": "-2500"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính:\na) $(-12) \\cdot (-5)$.\nb) $18 \\cdot (-4)$.\nc) $(-2)^2 \\cdot (-3)^2$.\nd) $(-1)^{2024} + (-1)^{2025}$.",
            "rubric": "a) 60 (0.25đ).\nb) -72 (0.25đ).\nc) 4 * 9 = 36 (0.25đ).\nd) 1 + (-1) = 0 (0.25đ)."
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tính một cách hợp lí:\na) $A = (-8) \\cdot 25 \\cdot (-125) \\cdot 4$.\nb) $B = 35 \\cdot (-18) + 35 \\cdot (-82)$.",
            "rubric": "a) A = [(-8) * (-125)] * (25 * 4) = 1000 * 100 = 100000 (0.5đ).\nb) B = 35 * [(-18) + (-82)] = 35 * (-100) = -3500 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tìm số nguyên $x$ biết:\na) $4 \\cdot (x - 3) = -20$.\nb) $(-2) \\cdot x + 15 = -5$.",
            "rubric": "a) x - 3 = -20 : 4 = -5 => x = -5 + 3 = -2 (0.5đ).\nb) (-2) * x = -5 - 15 = -20 => x = -20 : (-2) = 10 (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c3_6_bai4_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 16: Phép nhân số nguyên - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Tích của 2025 số nguyên âm là:", "options": ["Một số nguyên âm", "Một số nguyên dương", "Số 0", "Không xác định"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tính $P = 125 \\cdot (-8) \\cdot (-4) \\cdot 25$:", "options": ["$100000$", "$-100000$", "$10000$", "$-10000$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $a \\cdot b > 0$ và $a + b < 0$. Khi đó:", "options": ["Cả $a$ và $b$ đều là số nguyên âm", "Cả $a$ và $b$ đều là số nguyên dương", "$a$ âm và $b$ dương", "$a$ dương và $b$ âm"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Giá trị của biểu thức $A = (-2) \\cdot (-3)^2 \\cdot (-5)$ là:", "options": ["$90$", "$-90$", "$180$", "$-180$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tìm $x$ biết $(x + 2)(x - 3) = 0$:", "options": ["$x = -2$ hoặc $x = 3$", "$x = 2$ hoặc $x = -3$", "$x = -2$", "$x = 3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tính nhanh: $B = 29 \\cdot (-13) + 27 \\cdot (-13) + (-13) \\cdot 44$:", "options": ["$-1300$", "$1300$", "$-130$", "$2600$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho $x$ là số nguyên thỏa mãn $x^2 = 49$. Khi đó $x$ bằng:", "options": ["$7$ hoặc $-7$", "Chỉ $7$", "Chỉ $-7$", "Không có giá trị nào"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ sao cho $(x - 1)^3 = -27$:", "options": ["$x = -2$", "$x = 4$", "$x = -4$", "$x = 2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Một kho lạnh đang ở nhiệt độ $2^\\circ\\text{C}$. Người ta cài đặt để nhiệt độ giảm đều $3^\\circ\\text{C}$ mỗi giờ. Sau 5 giờ, nhiệt độ của kho lạnh là:", "options": ["$-13^\\circ\\text{C}$", "$-15^\\circ\\text{C}$", "$-17^\\circ\\text{C}$", "$-10^\\circ\\text{C}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Biết $a \\cdot b = -24$ và $a < b < 0$. Điều này có thể xảy ra không?", "options": ["Không thể xảy ra vì tích hai số âm luôn dương", "Có thể xảy ra", "Chỉ xảy ra khi $a = -24$", "Chỉ xảy ra khi $b = -1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Cho biểu thức $M = a(b - c) - b(a - c)$. Rút gọn $M$ ta được:", "options": ["$c(b - a)$", "$c(a - b)$", "$ab - c$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Có bao nhiêu cặp số nguyên $(x, y)$ thỏa mãn $x \\cdot y = 5$?", "options": ["$4$ cặp", "$2$ cặp", "$1$ cặp", "Vô số"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A = (-4) \\cdot (x - 3) + 2 \\cdot (x - 3)$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Đặt nhân tử chung $(x - 3)$: $A = (x - 3)[(-4) + 2] = -2(x - 3)$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khai triển ra ta được $A = -2x + 6$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Khi $x = 5$, giá trị của $A$ bằng $-4$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Để $A = 0$ thì $x = -3$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Một nhà đầu tư mua $100$ cổ phiếu với giá $50\\,000$ đồng/cổ phiếu. Trong tuần, giá cổ phiếu biến động như sau:\n- 3 ngày đầu: mỗi ngày tăng $2\\,000$ đồng (+2 000)\n- 2 ngày sau: mỗi ngày giảm $4\\,000$ đồng (-4 000).",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng mức tăng trong 3 ngày đầu là $3 \\cdot 2000 = +6000$ đồng mỗi cổ phiếu.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng mức giảm trong 2 ngày sau là $2 \\cdot (-4000) = -8000$ đồng mỗi cổ phiếu.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Sau 5 ngày, mỗi cổ phiếu bị giảm $2\\,000$ đồng so với giá ban đầu.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tổng số tiền nhà đầu tư bị lỗ sau tuần đó là $200\\,000$ đồng.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính: $P = (-4) \\cdot (-5) \\cdot (-6) \\cdot (-7)$.", "answer": "840"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tính hợp lí: $17 \\cdot (-85) + 17 \\cdot (-15)$.", "answer": "-1700"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ biết: $(x + 5)^2 = 36$ và $x < 0$.", "answer": "-11"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Có bao nhiêu cặp số nguyên $(x, y)$ thỏa mãn $x \\cdot y = -7$?", "answer": "4"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức một cách hợp lí:\na) $A = (-8) \\cdot 25 \\cdot (-2) \\cdot 4 \\cdot (-5) \\cdot 125$.\nb) $B = 48 \\cdot (-24) + (-24) \\cdot 52$.",
            "rubric": "a) A = [(-8) * 125] * (25 * 4) * [(-2) * (-5)] = (-1000) * 100 * 10 = -1000000 (0.5đ).\nb) B = (-24) * (48 + 52) = (-24) * 100 = -2400 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số nguyên $x$ biết:\na) $(x - 2)(x + 4) = 0$.\nb) $(-3) \\cdot (x - 5) + 12 = -6$.\nc) $x^2 - 16 = 0$.",
            "rubric": "a) x - 2 = 0 => x = 2; hoặc x + 4 = 0 => x = -4. Vậy x ∈ {2; -4} (0.35đ).\nb) -3(x - 5) = -18 => x - 5 = 6 => x = 11 (0.35đ).\nc) x^2 = 16 => x = 4 hoặc x = -4 (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một công ty lâm nghiệp trồng rừng có kế hoạch trồng $150\\text{ ha}$ rừng trong 5 tháng. Do thời tiết xấu, mỗi tháng diện tích trồng thực tế bị giảm $4\\text{ ha}$ so với kế hoạch (nghĩa là giảm $-4\\text{ ha/tháng}$).\na) Hỏi sau 5 tháng, diện tích rừng trồng thực tế giảm bao nhiêu héc-ta so với kế hoạch?\nb) Thực tế công ty đã trồng được bao nhiêu héc-ta rừng?",
            "rubric": "a) Diện tích rừng bị giảm sau 5 tháng là: 5 * (-4) = -20 (ha), nghĩa là giảm 20 ha (0.5đ).\nb) Diện tích thực tế công ty trồng được là: 150 - 20 = 130 (ha) (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c3_6_bai4_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 16: Phép nhân số nguyên - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $a < b < 0$. So sánh $a^2$ và $b^2$:", "options": ["$a^2 > b^2$", "$a^2 < b^2$", "$a^2 = b^2$", "Không so sánh được"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $x, y \\in \\mathbb{Z}$ thỏa mãn $x \\cdot y < 0$ và $|x| = y$. Khi đó:", "options": ["$x < 0$ và $y > 0$", "$x > 0$ và $y < 0$", "Cả $x, y$ đều âm", "Cả $x, y$ đều dương"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn $(x - 1)(y + 2) = 5$:", "options": ["$4$ cặp", "$2$ cặp", "$1$ cặp", "$6$ cặp"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho $P = (-1) \\cdot (-1)^2 \\cdot (-1)^3 \\dots (-1)^{2024}$. Giá trị của $P$ là:", "options": ["$1$", "$-1$", "$0$", "$2024$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ sao cho $(x^2 - 1)(x^2 - 4) < 0$:", "options": ["$x \\in \\{-1; 1\\}$", "$x \\in \\{-2; 2\\}$", "Không có số nguyên $x$ nào", "Vô số $x$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Có bao nhiêu cặp số nguyên $(x, y)$ thỏa mãn $x \\cdot y + 2x - 3y = 11$?", "options": ["$4$ cặp", "$2$ cặp", "$6$ cặp", "$8$ cặp"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho $a, b, c \\in \\mathbb{Z}$ thỏa mãn $ab - ac + bc - c^2 = -1$. Khẳng định nào sau đây đúng?", "options": ["$a + c$ và $b - c$ là hai số đối nhau", "$a = b = c$", "$a + b = c$", "$a - b = c$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = (x - 2)^2 - 15$ với $x \\in \\mathbb{Z}$:", "options": ["$-15$", "$0$", "$-11$", "$-19$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm số nguyên $x$ để $(x - 3)(x + 5) < 0$:", "options": ["$-5 < x < 3$", "$x > 3$", "$x < -5$", "$x \\leq -5$ hoặc $x \\geq 3$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho 2025 số nguyên $a_1, a_2, \\dots, a_{2025}$ thỏa mãn tích của 4 số bất kì luôn là một số dương. Khẳng định nào đúng?", "options": ["Cả 2025 số đều là số nguyên dương hoặc cả 2025 số đều là số nguyên âm", "Có đúng 1 số âm", "Có đúng 2 số âm", "Có đúng 3 số âm"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tích của tất cả các ước nguyên của số $10$ bằng:", "options": ["$100$", "$-100$", "$1000$", "$-1000$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức $B = 12 - (x + 1)^2$:", "options": ["$12$", "$11$", "$13$", "$0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho phương trình nghiệm nguyên: $(x - 2)(y + 3) = 7$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Vì $x, y \\in \\mathbb{Z}$ nên $x - 2$ và $y + 3$ là các ước của 7.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tập hợp các ước nguyên của 7 là $\\Ư(7) = \\{1; -1; 7; -7\\}$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Có đúng 4 cặp số nguyên $(x; y)$ thỏa mãn phương trình.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Cặp $(x; y) = (3; 4)$ là một nghiệm của phương trình.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho ba số nguyên $a, b, c$ đôi một khác nhau thỏa mãn $a \\cdot b \\cdot c = 1$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Vì $a, b, c \\in \\mathbb{Z}$ và $abc = 1$ nên mỗi số chỉ có thể nhận giá trị $1$ hoặc $-1$.", "correct": True},
                {"key": "b", "level": "Vận dụng cao", "text": "Vì cả ba số đôi một khác nhau nên không thể tồn tại đồng thời 3 số nguyên khác nhau nhận giá trị trong $\\{1; -1\\}$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Không tồn tại bộ ba số nguyên $a, b, c$ đôi một khác nhau thỏa mãn $abc = 1$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Nếu cho phép hai số bằng nhau thì có thể chọn bộ $(1; -1; -1)$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $(x - 2)(x + 3) < 0$?", "answer": "4"},
        {"id": 2, "level": "Vận dụng cao", "question": "Tìm số cặp số nguyên $(x, y)$ thỏa mãn $xy - 2x + y = 5$.", "answer": "4"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $P = (x + 3)^2 + (y - 1)^2 - 7$.", "answer": "-7"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính tích của tất cả các số nguyên $x$ thỏa mãn $-3 < x < 4$.", "answer": "0"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn:\na) $(x - 3)(y + 1) = 5$.\nb) $xy + 3x - 2y = 11$.",
            "rubric": "a) Ư(5) = {1; -1; 5; -5} (0.15đ).\nCác cặp (x - 3; y + 1):\n- (1; 5) => (x; y) = (4; 4) (0.1đ)\n- (5; 1) => (x; y) = (8; 0) (0.1đ)\n- (-1; -5) => (x; y) = (2; -6) (0.1đ)\n- (-5; -1) => (x; y) = (-2; -2) (0.05đ).\nb) x(y + 3) - 2(y + 3) - 6 = 11 => (x - 2)(y + 3) = 5 (0.25đ).\nTương tự giải ra 4 cặp nghiệm (x; y) (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm số nguyên $x$ sao cho:\na) $(x - 1)(x + 3) < 0$.\nb) $(x + 2)(x - 4) > 0$.",
            "rubric": "a) Tích hai thừa số âm khi hai thừa số trái dấu. Vì x - 1 < x + 3 nên x - 1 < 0 và x + 3 > 0 => -3 < x < 1 (0.25đ). Do x ∈ Z => x ∈ {-2; -1; 0} (0.25đ).\nb) Tích hai thừa số dương khi hai thừa số cùng dấu:\nTH1: x - 4 > 0 => x > 4 (0.25đ).\nTH2: x + 2 < 0 => x < -2 (0.25đ).\nVậy x > 4 hoặc x < -2."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $a$ và $b$ là các số nguyên. Chứng minh rằng:\na) Nếu $a^2 + b^2$ chia hết cho $3$ thì cả $a$ và $b$ đều chia hết cho $3$.\nb) Biểu thức $A = n(n + 1)(n + 2)(n + 3) + 1$ là bình phương của một số nguyên với mọi $n \\in \\mathbb{Z}$.",
            "rubric": "a) Số chính phương chia cho 3 chỉ có số dư là 0 hoặc 1 (0.25đ). Để a^2 + b^2 chia hết cho 3 thì cả a^2 và b^2 phải cùng chia hết cho 3 => a chia hết cho 3 và b chia hết cho 3 (0.25đ).\nb) Nhóm: A = [n(n + 3)] * [(n + 1)(n + 2)] + 1 = (n^2 + 3n)(n^2 + 3n + 2) + 1 (0.2đ).\nĐặt t = n^2 + 3n => A = t(t + 2) + 1 = t^2 + 2t + 1 = (t + 1)^2 (0.2đ).\nThay lại: A = (n^2 + 3n + 1)^2 là bình phương của một số nguyên (0.1đ)."
        }
    ]
}
