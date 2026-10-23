# -*- coding: utf-8 -*-
"""
Builder cho Ngân hàng Đề kiểm tra Chương II: Hằng đẳng thức đáng nhớ và ứng dụng - Toán 8 (KNTT)
Bao gồm đầy đủ 5 bài học/chuyên đề x 3 mức độ = 15 đề thi hoàn toàn độc lập, khác biệt, chuẩn ma trận 2025.
Phân hóa: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao).
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams = {}

# ==============================================================================
# BÀI 6: HIỆU HAI BÌNH PHƯƠNG. BÌNH PHƯƠNG CỦA MỘT TỔNG HAY MỘT HIỆU
# ==============================================================================

# --- BÀI 6 - ĐỀ 1: CƠ BẢN (5.0 - 7.0 điểm) ---
exams["c2_8_bai1_test1"] = {
    "title": "Toán 8 (KNTT) - Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        { "id": 1, "level": "Nhận biết", "question": "Khai triển của hằng đẳng thức $(A + B)^2$ là:", "options": ["$A^2 + 2AB + B^2$", "$A^2 + AB + B^2$", "$A^2 - 2AB + B^2$", "$A^2 + B^2$"], "correct": 0 },
        { "id": 2, "level": "Nhận biết", "question": "Khai triển của $(x - 3)^2$ bằng:", "options": ["$x^2 - 6x + 9$", "$x^2 - 3x + 9$", "$x^2 - 9$", "$x^2 + 6x + 9$"], "correct": 0 },
        { "id": 3, "level": "Nhận biết", "question": "Biểu thức $x^2 - 16$ viết dưới dạng tích là:", "options": ["$(x - 4)(x + 4)$", "$(x - 4)^2$", "$(x - 16)(x + 16)$", "$(x - 8)(x + 8)$"], "correct": 0 },
        { "id": 4, "level": "Nhận biết", "question": "Khai triển của $(2x + 1)^2$ là:", "options": ["$4x^2 + 4x + 1$", "$2x^2 + 4x + 1$", "$4x^2 + 1$", "$4x^2 + 2x + 1$"], "correct": 0 },
        { "id": 5, "level": "Nhận biết", "question": "Biểu thức $(x + 5)(x - 5)$ bằng:", "options": ["$x^2 - 25$", "$x^2 - 10$", "$x^2 - 5$", "$x^2 + 25$"], "correct": 0 },
        { "id": 6, "level": "Nhận biết", "question": "Biểu thức $x^2 + 2x + 1$ viết dưới dạng bình phương của một tổng là:", "options": ["$(x + 1)^2$", "$(x - 1)^2$", "$(x + 2)^2$", "$x^2 + 1$"], "correct": 0 },
        { "id": 7, "level": "Thông hiểu", "question": "Tính nhanh giá trị của $101^2$ sử dụng hằng đẳng thức ta được:", "options": ["$10201$", "$10101$", "$10001$", "$10200$"], "correct": 0 },
        { "id": 8, "level": "Thông hiểu", "question": "Rút gọn biểu thức $A = (x + 2)^2 - (x - 2)^2$ ta được:", "options": ["$8x$", "$4x$", "$2x^2 + 8$", "$0$"], "correct": 0 },
        { "id": 9, "level": "Thông hiểu", "question": "Tính nhanh giá trị $99^2$ sử dụng hằng đẳng thức $(100 - 1)^2$ được:", "options": ["$9801$", "$9901$", "$9800$", "$9701$"], "correct": 0 },
        { "id": 10, "level": "Thông hiểu", "question": "Tính nhanh tích $48 \\cdot 52$ bằng công thức hiệu hai bình phương:", "options": ["$2496$", "$2500$", "$2494$", "$2504$"], "correct": 0 },
        { "id": 11, "level": "Thông hiểu", "question": "Đơn thức thích hợp điền vào dấu $?$ trong đẳng thức $x^2 + 6x + ? = (x + 3)^2$ là:", "options": ["$9$", "$6$", "$3$", "$18$"], "correct": 0 },
        { "id": 12, "level": "Thông hiểu", "question": "Tìm $x$ biết $(x + 1)^2 - x^2 = 7$:", "options": ["$x = 3$", "$x = 4$", "$x = 2$", "$x = 6$"], "correct": 0 }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $P = (2x + 3)^2 - 4x(x + 3)$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Khai triển $(2x + 3)^2 = 4x^2 + 12x + 9$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Biểu thức $4x(x + 3) = 4x^2 + 12x$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Rút gọn biểu thức ta được $P = 9$ (giá trị không phụ thuộc vào $x$).", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Khi $x = 100$ thì giá trị của $P$ bằng $900$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai số thực $a, b$ thỏa mãn $a + b = 7$ và $a - b = 3$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Giá trị của biểu thức $a^2 - b^2$ bằng $21$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Giá trị của số $a$ bằng $5$ và số $b$ bằng $2$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Tích $ab$ bằng $12$.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tổng $a^2 + b^2 = (a+b)^2 - 2ab = 49 - 20 = 29$.", "correct": True }
            ]
        }
    ],
    "part3": [
        { "id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $M = x^2 - 4x + 4$ tại $x = 12$.", "answer": "100" },
        { "id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên $x$ thỏa mãn: $x^2 - 25 = 0$.", "answer": "5" },
        { "id": 3, "level": "Vận dụng thấp", "question": "Tính nhanh giá trị biểu thức: $75^2 - 25^2$.", "answer": "5000" },
        { "id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = x^2 - 6x + 14$.", "answer": "5" }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Rút gọn các biểu thức sau:\na) $A = (x + 4)^2 + (x - 4)^2$.\nb) $B = (2x - 3)(2x + 3) - 4x^2 + 10$.",
            "rubric": "a) A = (x^2 + 8x + 16) + (x^2 - 8x + 16) = 2x^2 + 32 (0.5đ).\nb) B = (4x^2 - 9) - 4x^2 + 10 = -9 + 10 = 1 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số thực $x$ biết:\na) $(x - 5)^2 - x(x + 2) = 1$.\nb) $4x^2 - 9 = 0$.",
            "rubric": "a) x^2 - 10x + 25 - x^2 - 2x = 1 <=> -12x + 25 = 1 <=> -12x = -24 <=> x = 2 (0.5đ).\nb) (2x - 3)(2x + 3) = 0 <=> 2x - 3 = 0 hoặc 2x + 3 = 0 <=> x = 1.5 hoặc x = -1.5 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "a) Cho $x + y = 10$ và $xy = 21$. Hãy tính giá trị của biểu thức $x^2 + y^2$.\nb) Một khu vườn hình vuông có cạnh bằng $x$ mét. Bác An mở rộng khu vườn bằng cách tăng một cạnh thêm 4 mét và bớt cạnh kia 4 mét để tạo thành khu vườn hình chữ nhật. Hỏi diện tích khu vườn mới tăng hay giảm bao nhiêu mét vuông so với ban đầu?",
            "rubric": "a) Ta có x^2 + y^2 = (x + y)^2 - 2xy = 10^2 - 2*21 = 100 - 42 = 58 (0.5đ).\nb) Diện tích hình vuông ban đầu là S1 = x^2 (m^2). Diện tích hình chữ nhật sau khi đổi kích thước là S2 = (x + 4)(x - 4) = x^2 - 16 (m^2). Hiệu diện tích S2 - S1 = (x^2 - 16) - x^2 = -16. Vậy diện tích khu vườn mới luôn giảm đi 16 m^2 so với ban đầu (0.5đ)."
        }
    ]
}

# --- BÀI 6 - ĐỀ 2: KHÁ (7.0 - 8.5 điểm - KHÓ HƠN ĐỀ 1) ---
exams["c2_8_bai1_test2"] = {
    "title": "Toán 8 (KNTT) - Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu - Bài kiểm tra số 2 (🚀 Khá)",
    "part1": [
        { "id": 1, "level": "Nhận biết", "question": "Khai triển của $\\left(3x - \\frac{1}{2}\\right)^2$ là:", "options": ["$9x^2 - 3x + \\frac{1}{4}$", "$9x^2 - 6x + \\frac{1}{4}$", "$9x^2 - 3x + \\frac{1}{2}$", "$9x^2 - \\frac{1}{4}$"], "correct": 0 },
        { "id": 2, "level": "Nhận biết", "question": "Đa thức nào dưới đây viết được dưới dạng bình phương của một hiệu?", "options": ["$4x^2 - 12xy + 9y^2$", "$4x^2 - 6xy + 9y^2$", "$4x^2 + 12xy - 9y^2$", "$x^2 - 4x - 4$"], "correct": 0 },
        { "id": 3, "level": "Nhận biết", "question": "Viết biểu thức $(2x - 3y)(2x + 3y)$ dưới dạng hiệu hai bình phương:", "options": ["$4x^2 - 9y^2$", "$2x^2 - 3y^2$", "$4x^2 - 6y^2$", "$4x^2 + 9y^2$"], "correct": 0 },
        { "id": 4, "level": "Nhận biết", "question": "Rút gọn $(x + 2y)^2 - 4xy$ ta thu được:", "options": ["$x^2 + 4y^2$", "$x^2 - 4y^2$", "$x^2 + 2y^2$", "$x^2 + 8xy + 4y^2$"], "correct": 0 },
        { "id": 5, "level": "Thông hiểu", "question": "Cho $x^2 + y^2 = 25$ và $xy = 12$. Giá trị của $(x - y)^2$ bằng:", "options": ["$1$", "$49$", "$13$", "$37$"], "correct": 0 },
        { "id": 6, "level": "Thông hiểu", "question": "Biểu thức $B = (x - 2y)^2 + (x + 2y)^2$ rút gọn được kết quả là:", "options": ["$2x^2 + 8y^2$", "$2x^2 - 8y^2$", "$2x^2 + 4y^2$", "$4xy$"], "correct": 0 },
        { "id": 7, "level": "Thông hiểu", "question": "Rút gọn biểu thức $C = (3x + 1)^2 - 2(3x + 1)(3x - 1) + (3x - 1)^2$:", "options": ["$4$", "$0$", "$36x^2$", "$2$"], "correct": 0 },
        { "id": 8, "level": "Thông hiểu", "question": "Tìm $x$ biết $(2x - 1)^2 - (2x + 3)(2x - 3) = 14$:", "options": ["$x = -1$", "$x = 1$", "$x = -2$", "$x = 2$"], "correct": 0 },
        { "id": 9, "level": "Thông hiểu", "question": "Giá trị nhỏ nhất của biểu thức $F(x) = 4x^2 - 4x + 10$ bằng:", "options": ["$9$", "$10$", "$8$", "$1$"], "correct": 0 },
        { "id": 10, "level": "Thông hiểu", "question": "Giá trị lớn nhất của biểu thức $G(x) = 5 - 4x - x^2$ bằng:", "options": ["$9$", "$5$", "$1$", "$4$"], "correct": 0 },
        { "id": 11, "level": "Thông hiểu", "question": "Đẳng thức nào sau đây là SAI?", "options": ["$(x - y)^2 = -(y - x)^2$", "$(x - y)^2 = (y - x)^2$", "$(-x - y)^2 = (x + y)^2$", "$x^2 - y^2 = -(y^2 - x^2)$"], "correct": 0 },
        { "id": 12, "level": "Thông hiểu", "question": "Rút gọn $(x + 1)(x - 1)(x^2 + 1)(x^4 + 1)$ ta được:", "options": ["$x^8 - 1$", "$x^8 + 1$", "$x^{16} - 1$", "$x^6 - 1$"], "correct": 0 }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A(x) = (x + 3)^2 + (x - 3)^2 - 2(x + 3)(x - 3)$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Biểu thức $A(x)$ có dạng $u^2 - 2uv + v^2$ với $u = x + 3$ và $v = x - 3$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Thu gọn biểu thức ta được $A(x) = [(x + 3) - (x - 3)]^2$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Giá trị của biểu thức $A(x)$ bằng $36$ với mọi giá trị của $x$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Khi $x = 2026$, giá trị của $A(x)$ bằng $2026^2$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai số dương $x, y$ thỏa mãn $x + y = 6$ và $x^2 + y^2 = 20$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Ta có $(x + y)^2 = x^2 + 2xy + y^2 = 36$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Tích $xy = \\frac{36 - 20}{2} = 8$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Giá trị của hiệu $(x - y)^2 = (x + y)^2 - 4xy = 36 - 32 = 4$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Nếu $x > y$ thì giá trị của $x^2 - y^2$ bằng $24$.", "correct": False }
            ]
        }
    ],
    "part3": [
        { "id": 1, "level": "Thông hiểu", "question": "Tính nhanh giá trị của biểu thức $E = 2025^2 - 2024^2$.", "answer": "4049" },
        { "id": 2, "level": "Vận dụng thấp", "question": "Tìm số nguyên dương $x$ thỏa mãn: $(2x + 3)^2 - 4x(x + 2) = 33$.", "answer": "6" },
        { "id": 3, "level": "Vận dụng thấp", "question": "Cho $x + \\frac{1}{x} = 5$. Tính giá trị của biểu thức $x^2 + \\frac{1}{x^2}$.", "answer": "23" },
        { "id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $P = x^2 + y^2 - 4x + 2y + 10$.", "answer": "5" }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Chứng minh rằng giá trị của biểu thức sau không phụ thuộc vào giá trị của biến $x$:\n$$M = (x - 2)(x + 2)(x^2 + 4) - (x^2 - 3)^2 - 6x^2$$",
            "rubric": "M = (x^2 - 4)(x^2 + 4) - (x^4 - 6x^2 + 9) - 6x^2 (0.25đ)\n= (x^4 - 16) - x^4 + 6x^2 - 9 - 6x^2 (0.5đ)\n= -16 - 9 = -25 (hằng số, không phụ thuộc vào x) (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm các số thực $x, y$ thỏa mãn phương trình:\n$$x^2 + 4y^2 - 6x + 4y + 10 = 0$$",
            "rubric": "Biến đổi: (x^2 - 6x + 9) + (4y^2 + 4y + 1) = 0 (0.25đ)\n<=> (x - 3)^2 + (2y + 1)^2 = 0 (0.25đ)\nVì (x - 3)^2 >= 0 và (2y + 1)^2 >= 0 với mọi x, y nên đẳng thức xảy ra <=>\nx - 3 = 0 và 2y + 1 = 0 (0.25đ)\n<=> x = 3 và y = -0.5. Vậy (x; y) = (3; -0.5) (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một người thợ kim hoàn có một tấm bạc hình vuông cạnh $a$ cm. Người đó cắt bỏ ở 4 góc 4 hình vuông nhỏ cạnh $b$ cm ($a > 2b$) rồi gấp các mép xung quanh lên để tạo thành một chiếc hộp đựng trang sức không nắp.\na) Tính diện tích toàn bộ bề mặt bên trong của chiếc hộp theo $a$ và $b$.\nb) Biết tấm bạc ban đầu có diện tích $100\\text{ cm}^2$ và tổng diện tích của 4 góc bị cắt bỏ là $16\\text{ cm}^2$. Tính cạnh $a$ và $b$ của các hình vuông.",
            "rubric": "a) Diện tích toàn phần bên trong hộp bằng diện tích hình vuông lớn trừ 4 góc vuông nhỏ: S = a^2 - 4b^2 = (a - 2b)(a + 2b) cm^2 (0.5đ).\nb) Diện tích ban đầu: a^2 = 100 => a = 10 (vì a > 0) (0.25đ).\nTổng diện tích 4 góc cắt bỏ: 4b^2 = 16 => b^2 = 4 => b = 2 (vì b > 0). Kiểm tra a = 10 > 2b = 4 (thỏa mãn). Vậy a = 10 cm, b = 2 cm (0.25đ)."
        }
    ]
}

# --- BÀI 6 - ĐỀ 3: NÂNG CAO (8.5 - 10.0 điểm - PHÂN HÓA SÂU) ---
exams["c2_8_bai1_test3"] = {
    "title": "Toán 8 (KNTT) - Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu - Bài kiểm tra số 3 (🔥 Nâng cao)",
    "part1": [
        { "id": 1, "level": "Nhận biết", "question": "Khai triển của hằng đẳng thức 3 số hạng $(a + b + c)^2$ bằng:", "options": ["$a^2 + b^2 + c^2 + 2ab + 2bc + 2ca$", "$a^2 + b^2 + c^2 + ab + bc + ca$", "$a^2 + b^2 + c^2 - 2ab - 2bc - 2ca$", "$a^2 + b^2 + c^2$"], "correct": 0 },
        { "id": 2, "level": "Thông hiểu", "question": "Cho $a + b + c = 0$ và $a^2 + b^2 + c^2 = 14$. Giá trị của biểu thức $ab + bc + ca$ là:", "options": ["$-7$", "$7$", "$-14$", "$14$"], "correct": 0 },
        { "id": 3, "level": "Thông hiểu", "question": "Rút gọn biểu thức $P = (a - b + c)^2 - 2(a - b + c)(c - b) + (b - c)^2$:", "options": ["$a^2$", "$b^2$", "$c^2$", "$(a - 2b)^2$"], "correct": 0 },
        { "id": 4, "level": "Thông hiểu", "question": "Biết $x^2 - y^2 = 35$ và $x - y = 5$. Giá trị của $x^2 + y^2$ bằng:", "options": ["$37$", "$25$", "$26$", "$49$"], "correct": 0 },
        { "id": 5, "level": "Thông hiểu", "question": "Số cặp số nguyên dương $(x; y)$ thỏa mãn $x^2 - y^2 = 13$ là:", "options": ["$1$", "$2$", "$0$", "Vô số"], "correct": 0 },
        { "id": 6, "level": "Thông hiểu", "question": "Giá trị nhỏ nhất của đa thức $f(x, y) = x^2 + 2y^2 - 2xy - 2x + 4$ là:", "options": ["$3$", "$4$", "$2$", "$1$"], "correct": 0 },
        { "id": 7, "level": "Vận dụng cao", "question": "Tính tổng $S = 2^2 - 3^2 + 4^2 - 5^2 + \\dots + 20^2 - 21^2$:", "options": ["$-230$", "$-210$", "$-250$", "$230$"], "correct": 0 },
        { "id": 8, "level": "Vận dụng cao", "question": "Tìm số dư khi chia $(2 + 1)(2^2 + 1)(2^4 + 1)(2^8 + 1)(2^{16} + 1)$ cho $2^{32}$:", "options": ["$2^{32} - 1$", "$1$", "$2$", "$0$"], "correct": 0 },
        { "id": 9, "level": "Vận dụng cao", "question": "Cho hai số thực $x, y$ thỏa mãn $x^2 + y^2 = 1$. Giá trị lớn nhất của $x + y$ là:", "options": ["$\\sqrt{2}$", "$2$", "$1$", "$\\frac{\\sqrt{2}}{2}$"], "correct": 0 },
        { "id": 10, "level": "Vận dụng cao", "question": "Cho $a^2 + b^2 + c^2 = ab + bc + ca$. Mối quan hệ giữa ba số $a, b, c$ là:", "options": ["$a = b = c$", "$a + b = c$", "$a + b + c = 0$", "$a = -b = c$"], "correct": 0 },
        { "id": 11, "level": "Vận dụng cao", "question": "Biết $x - \\frac{1}{x} = 3$. Giá trị của $x^4 + \\frac{1}{x^4}$ bằng:", "options": ["$119$", "$121$", "$123$", "$117$"], "correct": 0 },
        { "id": 12, "level": "Vận dụng cao", "question": "Số nghiệm nguyên $(x; y)$ thỏa mãn đẳng thức $x^2 + y^2 - 4x + 6y + 13 = 0$ là:", "options": ["$1$", "$2$", "$4$", "$0$"], "correct": 0 }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho đa thức hai biến $A(x, y) = x^2 - 4xy + 5y^2 + 10x - 22y + 28$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Biểu thức có thể nhóm thành $(x - 2y + 5)^2 + (y - 1)^2 + 2$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Vì bình phương của mọi số thực đều không âm nên $A(x, y) \\ge 2$ với mọi $x, y$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Giá trị nhỏ nhất của $A(x, y)$ bằng $2$ khi $y = 1$ và $x = -3$.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Không tồn tại cặp số thực $(x; y)$ nào để $A(x, y) = 3$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho ba số thực $a, b, c$ thỏa mãn $a^2 + b^2 + c^2 + 3 = 2(a + b + c)$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Chuyển vế ta được $(a - 1)^2 + (b - 1)^2 + (c - 1)^2 = 0$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Đẳng thức chỉ xảy ra khi và chỉ khi $a = b = c = 1$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Biểu thức $T = a^{2026} + b^{2026} + c^{2026}$ có giá trị bằng $3$.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Biểu thức $K = (a - 1)^{2025} + (b - 1)^{2025} + (c - 1)^{2025} = 1$.", "correct": False }
            ]
        }
    ],
    "part3": [
        { "id": 1, "level": "Thông hiểu", "question": "Cho $x + y = 3$ và $x^2 + y^2 = 5$. Tính giá trị của $x^4 + y^4$.", "answer": "17" },
        { "id": 2, "level": "Vận dụng cao", "question": "Tìm số nguyên dương $n$ lớn nhất có hai chữ số sao cho $n^2 + 4n + 2025$ là số chính phương.", "answer": "96" },
        { "id": 3, "level": "Vận dụng cao", "question": "Cho $a, b > 0$ thỏa mãn $a + b = 2$. Tìm giá trị nhỏ nhất của biểu thức $H = \\left(1 + \\frac{1}{a}\\right)\\left(1 + \\frac{1}{b}\\right)$.", "answer": "4" },
        { "id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $M = 2x^2 + y^2 - 2xy - 2x + 3$.", "answer": "2" }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Chứng minh rằng với mọi số thực $a, b, c$ ta luôn có bất đẳng thức:\n$$a^2 + b^2 + c^2 \\ge ab + bc + ca$$\nDấu đẳng thức xảy ra khi nào?",
            "rubric": "Nhân cả 2 vế với 2: 2a^2 + 2b^2 + 2c^2 - 2ab - 2bc - 2ca >= 0 (0.25đ)\n<=> (a^2 - 2ab + b^2) + (b^2 - 2bc + c^2) + (c^2 - 2ca + a^2) >= 0 (0.25đ)\n<=> (a - b)^2 + (b - c)^2 + (c - a)^2 >= 0 (luôn đúng với mọi a, b, c) (0.25đ).\nDấu '=' xảy ra <=> a - b = 0 và b - c = 0 và c - a = 0 <=> a = b = c (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm tất cả các cặp số nguyên $(x; y)$ thỏa mãn phương trình:\n$$x^2 - 2xy + 2y^2 - 2x + 6y + 5 = 0$$",
            "rubric": "Biến đổi: (x^2 - 2xy + y^2) - 2(x - y) + 1 + (y^2 + 4y + 4) = 0 (0.25đ)\n<=> (x - y - 1)^2 + (y + 2)^2 = 0 (0.25đ)\nDo (x - y - 1)^2 >= 0 và (y + 2)^2 >= 0 nên tổng bằng 0 khi:\ny + 2 = 0 <=> y = -2 (0.25đ)\nx - y - 1 = 0 <=> x - (-2) - 1 = 0 <=> x + 1 = 0 <=> x = -1.\nVậy có duy nhất 1 cặp nghiệm nguyên là (x; y) = (-1; -2) (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "(Câu điểm 10)\na) Cho $x, y$ là các số thực thỏa mãn $x^2 + 2y^2 + 2xy + 72 = 12(x + y)$. Tìm giá trị lớn nhất và giá trị nhỏ nhất của biểu thức $S = x + y$.\nb) Chứng minh rằng không tồn tại số nguyên $n$ nào để biểu thức $A = n^4 - 2n^3 + 2n^2 - 2n + 1$ là số chính phương ngoại trừ $n = 0$ và $n = 1$.",
            "rubric": "a) Giả thiết <=> (x + y)^2 + y^2 - 12(x + y) + 72 = 0 (0.25đ)\nĐặt S = x + y, ta có: S^2 - 12S + 72 = -y^2 <= 0 => S^2 - 12S + 36 <= -36 + 36 = 0\n<=> (S - 6)^2 <= 0. Vì (S - 6)^2 >= 0 nên bắt buộc (S - 6)^2 = 0 <=> S = 6 và y = 0. Khi đó x = 6. Vậy GTLN và GTNN của S đều bằng 6 (0.25đ).\nb) Ta có A = (n^2 - n)^2 + n^2 - 2n + 1 = (n^2 - n)^2 + (n - 1)^2 >= (n^2 - n)^2 (0.25đ).\nMặt khác xét [ (n^2 - n) + 1 ]^2 = (n^2 - n)^2 + 2(n^2 - n) + 1 = (n^2 - n)^2 + 2n^2 - 2n + 1. So sánh với A: [ (n^2 - n) + 1 ]^2 - A = n^2 > 0 với mọi n khác 0.\nDo đó với n khác 0 và n khác 1 ta có (n^2 - n)^2 < A < (n^2 - n + 1)^2. A bị kẹp giữa hai số chính phương liên tiếp nên không thể là số chính phương. Khi n = 0 thì A = 1 (1^2), khi n = 1 thì A = 0 (0^2) (ĐPCM) (0.25đ)."
        }
    ]
}

print("Built Bài 6 (3 đề)!")

with open("temp_c2_part1.json", "w", encoding="utf-8") as f:
    json.dump(exams, f, ensure_ascii=False, indent=2)
