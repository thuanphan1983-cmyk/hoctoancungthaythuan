# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG VII (PHẦN 1)
Bao gồm:
- Bài 24: Biểu thức đại số (3 đề: Cơ bản, Khá, Nâng cao)
- Bài 25: Đa thức một biến (3 đề: Cơ bản, Khá, Nâng cao)
- Bài 26: Phép cộng và phép trừ đa thức một biến (3 đề: Cơ bản, Khá, Nâng cao)
Chuẩn ma trận Bộ GD&ĐT 2025: 12 TN + 2 Đ/S (8 ý) + 4 TLN + 3 TL. Tổng 10.0 điểm.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

EXAMS_PART1 = {}

# =====================================================================
# BÀI 24: BIỂU THỨC ĐẠI SỐ
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c7_7_bai1_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 24: Biểu thức đại số - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Biểu thức nào sau đây là biểu thức số?", "options": ["$3^2 + 5 \\cdot 2$", "$2x + 1$", "$3a - b$", "$\\frac{x}{y}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Biểu thức nào sau đây chứa biến (biểu thức đại số)?", "options": ["$2x - 5$", "$2 \\cdot 3 + 4$", "$5^2 - 1$", "$10 : 2 + 3$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trong biểu thức đại số $3x + 4y$, các chữ $x$ và $y$ được gọi là:", "options": ["Biến số (biến)", "Hằng số", "Hệ số", "Hạng tử tự do"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Biểu thức đại số biểu thị chu vi hình chữ nhật có chiều dài $a$ và chiều rộng $b$ là:", "options": ["$2(a + b)$", "$ab$", "$a + b$", "$2ab$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Biểu thức đại số biểu thị diện tích hình tam giác có đáy $a$ và chiều cao tương ứng $h$ là:", "options": ["$\\frac{1}{2}ah$", "$ah$", "$2ah$", "$a + h$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Giá trị của biểu thức $A = 2x + 3$ tại $x = 5$ là:", "options": ["$13$", "$10$", "$11$", "$15$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Giá trị của biểu thức $B = x^2 - 4x + 1$ tại $x = 2$ là:", "options": ["$-3$", "$1$", "$5$", "$-5$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Biểu thức đại số biểu thị \"Tổng của hai lần $x$ và ba lần $y$\" là:", "options": ["$2x + 3y$", "$3x + 2y$", "$2x \\cdot 3y$", "$(2+x)(3+y)$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Biểu thức đại số biểu thị \"Bình phương của tổng hai số $a$ và $b$\" là:", "options": ["$(a + b)^2$", "$a^2 + b^2$", "$a + b^2$", "$2(a + b)$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Giá trị của biểu thức $P = 3x - 2y$ tại $x = 2, y = -1$ là:", "options": ["$8$", "$4$", "$-8$", "$-4$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Một người đi xe máy với vận tốc $40$ km/h trong $t$ giờ và sau đó đi bộ với vận tốc $5$ km/h trong $2$ giờ. Tổng quãng đường đi được là:", "options": ["$40t + 10$", "$40t + 5$", "$45t$", "$80 + 5t$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Giá trị của biểu thức $Q = \\frac{2x - 1}{x + 2}$ tại $x = 3$ là:", "options": ["$1$", "$\\frac{5}{3}$", "$\\frac{7}{5}$", "$2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức đại số $A = 3x^2 - 2x + 5$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Biểu thức $A$ có biến là $x$.", "isCorrect": True, "explanation": "Biến số duy nhất là $x$."},
                {"id": "b", "statement": "Tại $x = 0$, giá trị của $A$ là $5$.", "isCorrect": True, "explanation": "$A(0) = 3(0)^2 - 2(0) + 5 = 5$."},
                {"id": "c", "statement": "Tại $x = 1$, giá trị của $A$ là $6$.", "isCorrect": True, "explanation": "$A(1) = 3(1) - 2(1) + 5 = 6$."},
                {"id": "d", "statement": "Tại $x = -1$, giá trị của $A$ là $6$.", "isCorrect": False, "explanation": "$A(-1) = 3(-1)^2 - 2(-1) + 5 = 3 + 2 + 5 = 10 \\neq 6$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Xét tính đúng/sai của các phát biểu về diễn đạt biểu thức đại số:",
            "statements": [
                {"id": "a", "statement": "\"Tổng các bình phương của $a$ và $b$\" là $a^2 + b^2$.", "isCorrect": True, "explanation": "Bình phương từng số rồi cộng lại: $a^2 + b^2$."},
                {"id": "b", "statement": "\"Bình phương của hiệu $a$ và $b$\" là $(a - b)^2$.", "isCorrect": True, "explanation": "Lấy hiệu trước rồi bình phương: $(a - b)^2$."},
                {"id": "c", "statement": "\"Tích của tổng $a, b$ với hiệu của $a, b$\" là $(a + b)(a - b)$.", "isCorrect": True, "explanation": "Đúng nghĩa của tích hai biểu thức."},
                {"id": "d", "statement": "\"Thương của $x$ và $y$ trừ đi 3\" là $\\frac{x}{y - 3}$.", "isCorrect": False, "explanation": "Phải là $\\frac{x}{y} - 3$ chứ không phải $\\frac{x}{y - 3}$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $M = 4x - 7$ tại $x = 5$.", "answer": 13, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $N = x^2 + 2x$ tại $x = -3$.", "answer": 3, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $P = 2x^2 - 3xy + y^2$ tại $x = 2, y = 1$.", "answer": 3, "unit": ""},
        {"id": 4, "level": "Vận dụng", "question": "Một hình chữ nhật có chiều rộng là $x$ (cm), chiều dài hơn chiều rộng 4 cm. Viết biểu thức diện tích theo $x$. Với $x = 6$ cm, diện tích hình chữ nhật là bao nhiêu cm$^2$?", "answer": 60, "unit": "cm$^2$"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Viết biểu thức đại số biểu thị:\na) Quãng đường đi được của một ô tô chuyển động trong $t$ giờ với vận tốc $50$ km/h.\nb) Tổng số tiền phải trả khi mua $x$ quyển vở giá $8\\,000$ đồng/quyển và $y$ chiếc bút bi giá $5\\,000$ đồng/chiếc.\nc) Tính số tiền phải trả khi mua $10$ quyển vở và $6$ chiếc bút bi.",
            "maxScore": 1.0,
            "solution": "a) Quãng đường đi được là: $s = 50t$ (km).\nb) Tổng số tiền phải trả là: $T = 8000x + 5000y$ (đồng).\nc) Thay $x = 10, y = 6$ vào biểu thức $T$:\n$T = 8000 \\times 10 + 5000 \\times 6 = 80\\,000 + 30\\,000 = 110\\,000$ (đồng).\nVậy số tiền phải trả là $110\\,000$ đồng.",
            "rubric": [
                {"step": "Viết đúng biểu thức câu a (50t) và câu b (8000x + 5000y)", "subScore": 0.5},
                {"step": "Tính đúng số tiền câu c là 110 000 đồng", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho biểu thức $P = x^3 - 3x^2 y + 3xy^2 - y^3$.\na) Tính giá trị của biểu thức $P$ tại $x = 5$ và $y = 3$.\nb) Em có nhận xét gì về biểu thức $P$ với $(x - y)^3$?",
            "maxScore": 1.0,
            "solution": "a) Thay $x = 5, y = 3$ vào biểu thức $P$:\n$P = 5^3 - 3(5^2)(3) + 3(5)(3^2) - 3^3$\n$= 125 - 3(25)(3) + 3(5)(9) - 27$\n$= 125 - 225 + 135 - 27\n$= 8$.\nb) Nhận xét: Ta thấy $(x - y)^3 = (5 - 3)^3 = 2^3 = 8$.\nBiểu thức $P = x^3 - 3x^2 y + 3xy^2 - y^3$ chính là dạng khai triển của hằng đẳng thức lập phương của một hiệu: $(x - y)^3$.",
            "rubric": [
                {"step": "Tính đúng từng hạng tử và ra kết quả P = 8", "subScore": 0.6},
                {"step": "Nhận xét đúng liên hệ P = (x - y)^3", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một người thợ làm việc được trả công $a$ đồng mỗi giờ trong giờ làm việc tiêu chuẩn (8 giờ đầu). Nếu làm thêm giờ (từ giờ thứ 9 trở đi), mỗi giờ làm thêm được trả $1{,}5a$ đồng. Trong một ngày, người đó làm việc $t$ giờ ($t > 8$).\na) Viết biểu thức đại số tính tổng số tiền công người đó nhận được trong ngày theo $a$ và $t$.\nb) Với $a = 40\\,000$ đồng và người đó làm $10$ giờ, hãy tính tiền công người đó nhận được.",
            "maxScore": 1.0,
            "solution": "a) Tiền công trong 8 giờ tiêu chuẩn là: $8a$ (đồng).\nSố giờ làm thêm là: $t - 8$ (giờ).\nTiền công làm thêm là: $1{,}5a(t - 8)$ (đồng).\nTổng số tiền công nhận được trong ngày là:\n$T = 8a + 1{,}5a(t - 8) = 8a + 1{,}5at - 12a = 1{,}5at - 4a = a(1{,}5t - 4)$ (đồng).\nb) Thay $a = 40\\,000$ và $t = 10$ vào:\n$T = 8(40\\,000) + 1{,}5(40\\,000)(10 - 8)$\n$= 320\\,000 + 60\\,000 \\times 2 = 320\\,000 + 120\\,000 = 440\\,000$ (đồng).\nVậy người đó nhận được $440\\,000$ đồng tiền công.",
            "rubric": [
                {"step": "Viết đúng biểu thức tiền công T = 8a + 1,5a(t - 8)", "subScore": 0.5},
                {"step": "Thay số tính đúng số tiền công 440 000 đồng", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c7_7_bai1_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 24: Biểu thức đại số - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Giá trị của biểu thức $A = 2x^2 - 5x + 3$ tại $x = -2$ là:", "options": ["$21$", "$1$", "$-5$", "$15$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Biểu thức đại số biểu thị diện tích hình thang có đáy lớn $a$, đáy nhỏ $b$ và chiều cao $h$ là:", "options": ["$\\frac{(a + b)h}{2}$", "$(a + b)h$", "$\\frac{ab \\cdot h}{2}$", "$\\frac{a + b + h}{2}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Giá trị của biểu thức $B = x^2 - y^2$ tại $x = 13, y = 7$ là:", "options": ["$120$", "$40$", "$196$", "$169$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho biểu thức $C = \\frac{x + 1}{x - 1}$. Điều kiện của biến $x$ để giá trị biểu thức được xác định là:", "options": ["$x \\neq 1$", "$x \\neq -1$", "$x > 0$", "Mọi $x$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $D = x^3 - 3x^2 + 3x - 1$ tại $x = 11$:", "options": ["$1000$", "$1331$", "$100$", "$1210$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một người gửi ngân hàng số tiền $A$ đồng với lãi suất $r$ mỗi năm. Biểu thức biểu thị số tiền cả gốc lẫn lãi sau 1 năm là:", "options": ["$A(1 + r)$", "$A + r$", "$Ar$", "$A(1 - r)$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Giá trị của biểu thức $M = 3x^2 y - 2xy^2$ tại $x = -1, y = 2$ là:", "options": ["$14$", "$-14$", "$2$", "$-2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Tìm $x$ để biểu thức $E = 2x - 6$ có giá trị bằng $10$:", "options": ["$x = 8$", "$x = 2$", "$x = 4$", "$x = -8$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $x - y = 5$. Giá trị của biểu thức $H = 2(x - y) + 3$ là:", "options": ["$13$", "$10$", "$8$", "$15$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Biểu thức đại số biểu thị tổng bình phương của 3 số nguyên liên tiếp bắt đầu từ $n$ là:", "options": ["$n^2 + (n+1)^2 + (n+2)^2$", "$[n + (n+1) + (n+2)]^2$", "$3n^2 + 3$", "$n^2 + n^2 + n^2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $x + y = 3$. Giá trị của biểu thức $K = x^2 + 2xy + y^2 - 4x - 4y + 5$ là:", "options": ["$2$", "$4$", "$5$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị nhỏ nhất của biểu thức $P = (x - 2)^2 + 7$ là:", "options": ["$7$ (khi $x = 2$)", "$2$", "$0$", "$9$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = \\frac{2x - 3}{x + 1}$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Điều kiện xác định của biểu thức $A$ là $x \\neq -1$.", "isCorrect": True, "explanation": "Mẫu số $x + 1 \\neq 0 \\Leftrightarrow x \\neq -1$."},
                {"id": "b", "statement": "Tại $x = 0$, giá trị của $A$ là $-3$.", "isCorrect": True, "explanation": "$A = (0 - 3) / (0 + 1) = -3$."},
                {"id": "c", "statement": "Tại $x = 2$, giá trị của $A$ là $\\frac{1}{3}$.", "isCorrect": True, "explanation": "$A = (4 - 3) / (2 + 1) = 1/3$."},
                {"id": "d", "statement": "Để $A = 0$ thì $x = 3$.", "isCorrect": False, "explanation": "$2x - 3 = 0 \\Leftrightarrow x = 1{,}5 \\neq 3$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một bể bơi hình hộp chữ nhật có chiều dài $2x$ (m), chiều rộng $x$ (m) và chiều sâu $h = 1{,}5$ m. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Diện tích đáy bể bơi là $S_{\\text{đáy}} = 2x^2$ (m$^2$).", "isCorrect": True, "explanation": "$2x \\cdot x = 2x^2$."},
                {"id": "b", "statement": "Thể tích nước tối đa bể chứa được là $V = 3x^2$ (m$^3$).", "isCorrect": True, "explanation": "$V = 2x^2 \\times 1{,}5 = 3x^2$."},
                {"id": "c", "statement": "Nếu $x = 10$ m thì thể tích bể bơi là $300$ m$^3$.", "isCorrect": True, "explanation": "$3 \\times 10^2 = 300$ m$^3$."},
                {"id": "d", "statement": "Chu vi đáy bể bơi là $4x$ mét.", "isCorrect": False, "explanation": "Chu vi $= 2(2x + x) = 6x$ mét, không phải $4x$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $A = 3x^2 - 4x + 1$ tại $x = -1$.", "answer": 8, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm $x$ để biểu thức $3x - 5$ có giá trị bằng $16$.", "answer": 7, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Cho $a + b = 10$. Tính giá trị của biểu thức $M = 3a + 3b - 15$.", "answer": 15, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $B = (x - 3)^2 + 10$.", "answer": 10, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho biểu thức $A = 2x^2 - 3xy + y^2$.\na) Tính giá trị của $A$ tại $x = 1$ và $y = -2$.\nb) Tính giá trị của $A$ khi $x = 2y$ với $y = 3$.",
            "maxScore": 1.0,
            "solution": "a) Thay $x = 1, y = -2$ vào $A$:\n$A = 2(1)^2 - 3(1)(-2) + (-2)^2 = 2(1) + 6 + 4 = 2 + 6 + 4 = 12$.\nb) Khi $x = 2y$, biểu thức $A$ trở thành:\n$A = 2(2y)^2 - 3(2y)y + y^2 = 2(4y^2) - 6y^2 + y^2 = 8y^2 - 6y^2 + y^2 = 3y^2$.\nVới $y = 3 \\Rightarrow A = 3(3^2) = 3 \\times 9 = 27$.",
            "rubric": [
                {"step": "Tính đúng câu a ra A = 12", "subScore": 0.5},
                {"step": "Rút gọn theo y và tính đúng câu b ra A = 27", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một người đi taxi phải trả $12\\,000$ đồng cho kilômét đầu tiên và $10\\,000$ đồng cho mỗi kilômét tiếp theo. Nếu quãng đường đi lớn hơn $30$ km thì từ kilômét thứ 31 trở đi giá cước chỉ còn $8\\,000$ đồng/km.\na) Viết biểu thức đại số tính số tiền cước (đồng) khi khách hàng đi quãng đường $x$ km ($1 < x \\le 30$).\nb) Tính số tiền cước khách hàng phải trả khi đi quãng đường $25$ km.",
            "maxScore": 1.0,
            "solution": "a) Khi $1 < x \\le 30$:\nKilômét đầu tiên có giá: $12\\,000$ đồng.\nSố kilômét tiếp theo là: $x - 1$ (km).\nSố tiền cho các kilômét tiếp theo là: $10\\,000(x - 1)$ (đồng).\nTổng số tiền cước là:\n$T = 12\\,000 + 10\\,000(x - 1) = 10\\,000x + 2\\,000$ (đồng).\nb) Với $x = 25$ km (thỏa mãn $1 < 25 \\le 30$):\n$T = 10\\,000 \\times 25 + 2\\,000 = 250\\,000 + 2\\,000 = 252\\,000$ (đồng).\nVậy khách hàng phải trả $252\\,000$ đồng.",
            "rubric": [
                {"step": "Viết đúng biểu thức cước T = 10 000x + 2 000 (đồng)", "subScore": 0.5},
                {"step": "Tính đúng tiền cước cho 25 km là 252 000 đồng", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $P = \\frac{2x + 5}{x - 1}$ ($x$ là số nguyên, $x \\neq 1$).\na) Tìm các giá trị nguyên của $x$ để biểu thức $P$ nhận giá trị nguyên.\nb) Tìm giá trị lớn nhất của biểu thức $P$ khi $x$ là số nguyên.",
            "maxScore": 1.0,
            "solution": "a) Biến đổi biểu thức $P$:\n$P = \\frac{2(x - 1) + 7}{x - 1} = 2 + \\frac{7}{x - 1}$.\nĐể $P$ nhận giá trị nguyên thì $\\frac{7}{x - 1}$ phải là số nguyên, tức là $x - 1$ là ước của $7$.\nƯ(7) = $\\{\\pm 1; \\pm 7\\}$.\nTa có bảng giá trị:\n- $x - 1 = 1 \\Rightarrow x = 2$.\n- $x - 1 = -1 \\Rightarrow x = 0$.\n- $x - 1 = 7 \\Rightarrow x = 8$.\n- $x - 1 = -7 \\Rightarrow x = -6$.\nVậy $x \\in \\{-6; 0; 2; 8\\}$ thì $P$ nhận giá trị nguyên.\nb) Để $P = 2 + \\frac{7}{x - 1}$ đạt GTLN thì $\\frac{7}{x - 1}$ phải lớn nhất $\\Leftrightarrow x - 1$ là số nguyên dương nhỏ nhất $\\Rightarrow x - 1 = 1 \\Rightarrow x = 2$.\nKhi đó GTLN của $P$ là $2 + 7 = 9$ (đạt được tại $x = 2$).",
            "rubric": [
                {"step": "Tách P = 2 + 7/(x - 1) và lập luận ước của 7", "subScore": 0.5},
                {"step": "Tìm đúng tập x = {-6; 0; 2; 8} và GTLN = 9 tại x = 2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c7_7_bai1_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 24: Biểu thức đại số - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $x + y = 1$. Giá trị của biểu thức $A = x^3 + y^3 + 3xy$ là:", "options": ["$1$", "$3$", "$0$", "$2$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Giá trị của biểu thức $B = \\frac{x^2 - y^2}{(x+y)^2}$ tại $x = 105, y = 95$ là:", "options": ["$\\frac{1}{20}$", "$\\frac{1}{10}$", "$\\frac{1}{40}$", "$1$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Cho $a - b = 7$. Giá trị của biểu thức $C = a(a + 2) + b(b - 2) - 2ab$ là:", "options": ["$63$", "$49$", "$70$", "$56$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Giá trị nhỏ nhất của biểu thức $M = x^2 - 6x + 14$ là:", "options": ["$5$ (đạt khi $x = 3$)", "$14$", "$0$", "$9$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Giá trị lớn nhất của biểu thức $N = 10 - (x + 1)^2$ là:", "options": ["$10$ (đạt khi $x = -1$)", "$9$", "$11$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tìm các giá trị nguyên của $x$ để biểu thức $P = \\frac{5}{x - 2}$ nhận giá trị nguyên:", "options": ["$x \\in \\{-3; 1; 3; 7\\}$", "$x \\in \\{1; 3; 7\\}$", "$x \\in \\{-5; -1; 1; 5\\}$", "$x \\in \\{0; 2; 4\\}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho ba số thực $a, b, c$ thỏa mãn $a + b + c = 0$. Giá trị của biểu thức $Q = (a + b)(b + c)(c + a) + abc$ là:", "options": ["$0$", "$abc$", "$-abc$", "$1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $x, y$ thỏa mãn $x^2 + y^2 - 4x + 6y + 13 = 0$. Giá trị của biểu thức $x + y$ là:", "options": ["$-1$", "$1$", "$5$", "$-5$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho biểu thức $A = \\frac{x^2 + 8}{x^2 + 2}$. Giá trị lớn nhất của $A$ là:", "options": ["$4$ (đạt tại $x = 0$)", "$8$", "$2$", "$5$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số cặp số nguyên $(x; y)$ thỏa mãn biểu thức $(x - 1)(y + 2) = 5$ là:", "options": ["$4$ cặp", "$2$ cặp", "$8$ cặp", "$1$ cặp"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $a + b + c = 0$ và $a^2 + b^2 + c^2 = 14$. Giá trị của biểu thức $ab + bc + ca$ là:", "options": ["$-7$", "$7$", "$-14$", "$14$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $H = x^2 + 2y^2 - 2xy - 4y + 10$:", "options": ["$6$", "$10$", "$4$", "$2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho biểu thức $P = x^2 - 4x + y^2 + 6y + 15$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Biến đổi $P = (x - 2)^2 + (y + 3)^2 + 2$.", "isCorrect": True, "explanation": "$(x^2 - 4x + 4) + (y^2 + 6y + 9) + 2 = (x - 2)^2 + (y + 3)^2 + 2$."},
                {"id": "b", "statement": "Vì $(x - 2)^2 \\ge 0$ và $(y + 3)^2 \\ge 0$ nên $P \\ge 2$ với mọi $x, y$.", "isCorrect": True, "explanation": "Tổng các bình phương không âm cộng 2 luôn $\\ge 2$."},
                {"id": "c", "statement": "Giá trị nhỏ nhất của $P$ bằng $2$ khi $x = 2$ và $y = -3$.", "isCorrect": True, "explanation": "Dấu bằng xảy ra khi $x - 2 = 0$ và $y + 3 = 0$."},
                {"id": "d", "statement": "Giá trị của $P$ có thể nhận giá trị âm khi $x, y$ âm.", "isCorrect": False, "explanation": "Vì $P \\ge 2 > 0$ nên $P$ luôn dương với mọi $x, y$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực $x, y, z$ thỏa mãn $x + y + z = 0$ và $xyz = 2$. Xét tính đúng/sai của biểu thức $M = x^3 + y^3 + z^3$:",
            "statements": [
                {"id": "a", "statement": "Ta có hằng đẳng thức $x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx)$.", "isCorrect": True, "explanation": "Hằng đẳng thức phân tích ba biến cơ bản."},
                {"id": "b", "statement": "Vì $x + y + z = 0$ nên $x^3 + y^3 + z^3 - 3xyz = 0$.", "isCorrect": True, "explanation": "Vế phải có thừa số $(x+y+z) = 0$."},
                {"id": "c", "statement": "Do đó $x^3 + y^3 + z^3 = 3xyz$.", "isCorrect": True, "explanation": "Chuyển vế $3xyz$."},
                {"id": "d", "statement": "Giá trị của biểu thức $M = 8$.", "isCorrect": False, "explanation": "$M = 3xyz = 3 \\times 2 = 6 \\neq 8$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Cho $x + y = 5$. Tính giá trị của biểu thức $A = 2x + 2y - 3$.", "answer": 7, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm giá trị nhỏ nhất của biểu thức $P = x^2 - 8x + 20$.", "answer": 4, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $x - y = 3$ và $xy = 10$. Tính giá trị của biểu thức $x^2 + y^2$.", "answer": 29, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức $Q = \\frac{12}{x^2 + 3}$.", "answer": 4, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của các biểu thức sau:\na) $A = x^2 - 4x + 9$.\nb) $B = x^2 + y^2 - 2x + 4y + 10$.",
            "maxScore": 1.0,
            "solution": "a) Ta có:\n$A = (x^2 - 4x + 4) + 5 = (x - 2)^2 + 5$.\nVì $(x - 2)^2 \\ge 0$ với mọi $x$ nên $A \\ge 5$.\nDấu \"=\" xảy ra khi $x - 2 = 0 \\Leftrightarrow x = 2$.\nVậy GTNN của $A$ là $5$ khi $x = 2$.\nb) Ta có:\n$B = (x^2 - 2x + 1) + (y^2 + 4y + 4) + 5 = (x - 1)^2 + (y + 2)^2 + 5$.\nVì $(x - 1)^2 \\ge 0$ và $(y + 2)^2 \\ge 0$ với mọi $x, y$ nên $B \\ge 5$.\nDấu \"=\" xảy ra khi $x - 1 = 0 \\Leftrightarrow x = 1$ và $y + 2 = 0 \\Leftrightarrow y = -2$.\nVậy GTNN của $B$ là $5$ khi $x = 1, y = -2$.",
            "rubric": [
                {"step": "Tách đúng (x - 2)^2 + 5 và kết luận GTNN = 5 ở câu a", "subScore": 0.5},
                {"step": "Tách đúng (x - 1)^2 + (y + 2)^2 + 5 và kết luận GTNN = 5 ở câu b", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho hai số thực $x, y$ thỏa mãn $2x + y = 3$.\nChứng minh rằng biểu thức $M = 2x^2 + y^2$ luôn đạt giá trị nhỏ nhất và tìm giá trị nhỏ nhất đó.",
            "maxScore": 1.0,
            "solution": "Từ $2x + y = 3 \\Rightarrow y = 3 - 2x$.\nThay vào biểu thức $M$:\n$M = 2x^2 + (3 - 2x)^2 = 2x^2 + (9 - 12x + 4x^2) = 6x^2 - 12x + 9$.\nBiến đổi hằng đẳng thức:\n$M = 6(x^2 - 2x) + 9 = 6(x^2 - 2x + 1) - 6 + 9 = 6(x - 1)^2 + 3$.\nVì $(x - 1)^2 \\ge 0$ với mọi $x$ nên $6(x - 1)^2 \\ge 0$.\nSuy ra $M \\ge 3$ với mọi $x$.\nDấu \"=\" xảy ra khi $x - 1 = 0 \\Leftrightarrow x = 1$.\nKhi $x = 1 \\Rightarrow y = 3 - 2(1) = 1$.\nVậy GTNN của $M$ là $3$ khi $x = 1$ và $y = 1$.",
            "rubric": [
                {"step": "Rút y = 3 - 2x và thay vào đưa về tam thức bậc hai 6x^2 - 12x + 9", "subScore": 0.5},
                {"step": "Tách 6(x - 1)^2 + 3 và kết luận GTNN = 3 khi x = 1, y = 1", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $P = \\frac{3x - 2}{x + 1}$ ($x \\in \\mathbb{Z}, x \\neq -1$).\na) Tìm tất cả các giá trị nguyên của $x$ để $P$ là một số nguyên.\nb) Tìm giá trị nguyên của $x$ để $P$ đạt giá trị nguyên nhỏ nhất.",
            "maxScore": 1.0,
            "solution": "a) Ta biến đổi:\n$P = \\frac{3(x + 1) - 5}{x + 1} = 3 - \\frac{5}{x + 1}$.\nĐể $P$ nhận giá trị nguyên thì $\\frac{5}{x + 1}$ phải là số nguyên, tức là $x + 1$ là ước của $5$.\nƯ(5) = $\\{\\pm 1; \\pm 5\\}$.\nTa có bảng giá trị:\n- $x + 1 = 1 \\Rightarrow x = 0$.\n- $x + 1 = -1 \\Rightarrow x = -2$.\n- $x + 1 = 5 \\Rightarrow x = 4$.\n- $x + 1 = -5 \\Rightarrow x = -6$.\nVậy $x \\in \\{-6; -2; 0; 4\\}$ thì $P$ nguyên.\nb) Để $P = 3 - \\frac{5}{x + 1}$ đạt giá trị nguyên nhỏ nhất thì phân số $\\frac{5}{x + 1}$ phải đạt giá trị nguyên dương lớn nhất.\nĐiều này xảy ra khi mẫu số $x + 1$ là số nguyên dương nhỏ nhất, tức là $x + 1 = 1 \\Rightarrow x = 0$.\nKhi đó giá trị nhỏ nhất của $P$ là $3 - \\frac{5}{1} = 3 - 5 = -2$.\nVậy với $x = 0$ thì $P$ đạt giá trị nguyên nhỏ nhất là $-2$.",
            "rubric": [
                {"step": "Tách P = 3 - 5/(x + 1) và tìm đúng tập x = {-6; -2; 0; 4}", "subScore": 0.6},
                {"step": "Lập luận đúng giá trị nguyên nhỏ nhất là -2 khi x = 0", "subScore": 0.4}
            ]
        }
    ]
}

# =====================================================================
# BÀI 25: ĐA THỨC MỘT BIẾN
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c7_7_bai2_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 25: Đa thức một biến - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Biểu thức nào sau đây là đơn thức một biến?", "options": ["$3x^2$", "$2x + 1$", "$x - y$", "$\\frac{2}{x}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Đa thức một biến là:", "options": ["Tổng của những đơn thức của cùng một biến", "Tích của hai biến số", "Thương của hai số nguyên", "Biểu thức chứa căn bậc hai"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Bậc của đa thức $P(x) = 5x^4 - 3x^2 + x - 7$ là:", "options": ["$4$", "$2$", "$1$", "$0$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trong đa thức $P(x) = 5x^4 - 3x^2 + x - 7$, hệ số cao nhất là:", "options": ["$5$", "$-3$", "$1$", "$-7$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Trong đa thức $P(x) = 5x^4 - 3x^2 + x - 7$, hệ số tự do là:", "options": ["$-7$", "$7$", "$5$", "$1$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Sắp xếp đa thức $Q(x) = 2x - 5x^3 + 1 + 4x^2$ theo lũy thừa giảm dần của biến:", "options": ["$-5x^3 + 4x^2 + 2x + 1$", "$1 + 2x + 4x^2 - 5x^3$", "$4x^2 - 5x^3 + 2x + 1$", "$-5x^3 + 2x + 4x^2 + 1$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho đa thức $A(x) = 2x^3 - 3x + 1$. Giá trị của $A(1)$ là:", "options": ["$0$", "$2$", "$6$", "$-1$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho đa thức $B(x) = x^2 - 4$. Số nào sau đây là nghiệm của đa thức $B(x)$?", "options": ["$x = 2$", "$x = 0$", "$x = 4$", "$x = 1$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Thu gọn đa thức $P(x) = 3x^2 - 5x + 2x^2 + 4x - 1$ ta được:", "options": ["$5x^2 - x - 1$", "$5x^2 + x - 1$", "$x^2 - x - 1$", "$5x^2 - 9x - 1$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Đa thức bậc 0 là:", "options": ["Một số khác 0", "Số 0", "Đa thức có biến $x$", "Không tồn tại"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Bậc của đa thức $P(x) = (2x^3 - x^2) - (2x^3 - 3x^2 + 1)$ sau khi thu gọn là:", "options": ["$2$", "$3$", "$1$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Nghiệm của đa thức $f(x) = 2x - 6$ là:", "options": ["$x = 3$", "$x = -3$", "$x = 6$", "$x = 2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho đa thức $P(x) = 2x^4 - 3x^2 + 5x - 1$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Bậc của đa thức $P(x)$ bằng $4$.", "isCorrect": True, "explanation": "Hạng tử có số mũ lớn nhất là $2x^4$ (bậc 4)."},
                {"id": "b", "statement": "Hệ số cao nhất của $P(x)$ là $2$.", "isCorrect": True, "explanation": "Hệ số của $x^4$ là 2."},
                {"id": "c", "statement": "Hệ số tự do của $P(x)$ là $1$.", "isCorrect": False, "explanation": "Hệ số tự do là $-1$, không phải $1$."},
                {"id": "d", "statement": "$P(0) = -1$.", "isCorrect": True, "explanation": "$P(0) = 2(0) - 3(0) + 5(0) - 1 = -1$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho đa thức $Q(x) = x^2 - 3x + 2$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$x = 1$ là một nghiệm của đa thức $Q(x)$.", "isCorrect": True, "explanation": "$Q(1) = 1^2 - 3(1) + 2 = 1 - 3 + 2 = 0$."},
                {"id": "b", "statement": "$x = 2$ là một nghiệm của đa thức $Q(x)$.", "isCorrect": True, "explanation": "$Q(2) = 2^2 - 3(2) + 2 = 4 - 6 + 2 = 0$."},
                {"id": "c", "statement": "$x = 0$ là một nghiệm của đa thức $Q(x)$.", "isCorrect": False, "explanation": "$Q(0) = 2 \\neq 0$ nên $x = 0$ không phải nghiệm."},
                {"id": "d", "statement": "Đa thức $Q(x)$ có tối đa 2 nghiệm.", "isCorrect": True, "explanation": "Đa thức bậc 2 có không quá 2 nghiệm."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Xác định bậc của đa thức $P(x) = 7x^5 - 2x^3 + 4x - 9$.", "answer": 5, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của đa thức $A(x) = 3x^2 - 5x + 2$ tại $x = 2$.", "answer": 4, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tìm nghiệm của đa thức $P(x) = 3x - 12$.", "answer": 4, "unit": ""},
        {"id": 4, "level": "Vận dụng", "question": "Thu gọn đa thức $Q(x) = 4x^3 - 2x^2 + x^3 + 5x^2 - 3$. Tìm hệ số của $x^2$ sau khi thu gọn.", "answer": 3, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho đa thức $P(x) = 3x^3 - 2x + 5x^4 - 7 + x^3 - 4x^4$.\na) Thu gọn và sắp xếp đa thức $P(x)$ theo lũy thừa giảm dần của biến.\nb) Chỉ ra bậc, hệ số cao nhất và hệ số tự do của $P(x)$.",
            "maxScore": 1.0,
            "solution": "a) Thu gọn đa thức $P(x)$:\n$P(x) = (5x^4 - 4x^4) + (3x^3 + x^3) - 2x - 7$\n$= x^4 + 4x^3 - 2x - 7$.\nĐa thức đã được sắp xếp theo lũy thừa giảm dần của biến.\nb) Bậc của $P(x)$ là $4$.\nHệ số cao nhất là $1$ (hệ số của $x^4$).\nHệ số tự do là $-7$.",
            "rubric": [
                {"step": "Thu gọn đúng ra x^4 + 4x^3 - 2x - 7", "subScore": 0.5},
                {"step": "Chỉ đúng bậc 4, hệ số cao nhất 1, hệ số tự do -7", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho đa thức $A(x) = x^2 - 5x + 6$.\na) Tính giá trị của $A(x)$ tại $x = 1; x = 2; x = 3$.\nb) Trong các số $1; 2; 3$, số nào là nghiệm của đa thức $A(x)$? Vì sao?",
            "maxScore": 1.0,
            "solution": "a) Tính giá trị:\n- $A(1) = 1^2 - 5(1) + 6 = 1 - 5 + 6 = 2$.\n- $A(2) = 2^2 - 5(2) + 6 = 4 - 10 + 6 = 0$.\n- $A(3) = 3^2 - 5(3) + 6 = 9 - 15 + 6 = 0$.\nb) Trong ba số trên, các số $2$ và $3$ là nghiệm của đa thức $A(x)$ vì $A(2) = 0$ và $A(3) = 0$.\nSố $1$ không phải là nghiệm vì $A(1) = 2 \\neq 0$.",
            "rubric": [
                {"step": "Tính đúng A(1) = 2, A(2) = 0, A(3) = 0", "subScore": 0.6},
                {"step": "Kết luận 2 và 3 là nghiệm kèm giải thích rõ ràng", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Tìm nghiệm của các đa thức sau:\na) $P(x) = 3x - 9$.\nb) $Q(x) = x^2 - 16$.",
            "maxScore": 1.0,
            "solution": "a) Cho $P(x) = 0 \\Leftrightarrow 3x - 9 = 0 \\Leftrightarrow 3x = 9 \\Leftrightarrow x = 3$.\nVậy nghiệm của đa thức $P(x)$ là $x = 3$.\nb) Cho $Q(x) = 0 \\Leftrightarrow x^2 - 16 = 0 \\Leftrightarrow x^2 = 16 \\Leftrightarrow x = 4$ hoặc $x = -4$.\nVậy đa thức $Q(x)$ có hai nghiệm là $x = 4$ và $x = -4$.",
            "rubric": [
                {"step": "Giải đúng câu a ra x = 3", "subScore": 0.5},
                {"step": "Giải đúng câu b ra x = 4 và x = -4", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c7_7_bai2_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 25: Đa thức một biến - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho đa thức $P(x) = ax^3 + 2x^2 - x + 1$. Biết $P(1) = 4$, giá trị của $a$ là:", "options": ["$a = 2$", "$a = 1$", "$a = 3$", "$a = -2$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Số nghiệm tối đa của một đa thức một biến bậc $n$ ($n \\ge 1$) là:", "options": ["$n$ nghiệm", "$n + 1$ nghiệm", "$n - 1$ nghiệm", "Vô số nghiệm"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Đa thức nào sau đây KHÔNG có nghiệm thực?", "options": ["$x^2 + 1$", "$x^2 - 1$", "$x + 1$", "$x^3 + 1$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho $P(x) = 2x^2 - 3x + m$. Để $x = 2$ là nghiệm của $P(x)$ thì giá trị của $m$ là:", "options": ["$m = -2$", "$m = 2$", "$m = 1$", "$m = -1$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tập hợp các nghiệm của đa thức $A(x) = x(x - 3)(2x + 4)$ là:", "options": ["$\\{0; 3; -2\\}$", "$\\{3; -2\\}$", "$\\{0; -3; 2\\}$", "$\\{0; 3; 2\\}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Bậc của đa thức $f(x) = (x^2 + 1)(x^3 - 2x + 1)$ là:", "options": ["$5$", "$6$", "$3$", "$2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho đa thức $P(x) = x^4 - 2024x^3 + 2024x^2 - 2024x + 2025$. Giá trị của $P(2023)$ là:", "options": ["$2$", "$1$", "$2024$", "$0$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Nghiệm của đa thức $g(x) = (x - 1)^2 - 9$ là:", "options": ["$x = 4$ và $x = -2$", "$x = 4$ và $x = 2$", "$x = 10$ và $x = -8$", "$x = 3$ và $x = -3$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Tổng các hệ số của đa thức $P(x) = (2x - 1)^{10}$ là:", "options": ["$1$", "$2^{10}$", "$-1$", "$0$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho đa thức $M(x) = x^2 + 4x + 5$. Khẳng định nào sau đây là đúng?", "options": ["$M(x) > 0$ với mọi $x$, do đó đa thức vô nghiệm", "$M(x)$ có 2 nghiệm phân biệt", "$M(x)$ có nghiệm $x = -2$", "$M(x)$ có nghiệm $x = -1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm đa thức bậc nhất $P(x) = ax + b$ biết $P(1) = 3$ và $P(2) = 5$:", "options": ["$P(x) = 2x + 1$", "$P(x) = x + 2$", "$P(x) = 3x$", "$P(x) = 2x - 1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = ax^2 + bx + c$. Biết $P(0), P(1), P(2)$ đều là các số nguyên. Khẳng định nào sau đây đúng?", "options": ["$2a$ và $2b$ là các số nguyên", "$a, b, c$ bắt buộc phải là các số nguyên", "$a + b$ là số lẻ", "$P(3)$ không chắc là số nguyên"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho đa thức $P(x) = x^3 - 4x$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Bậc của đa thức $P(x)$ là $3$.", "isCorrect": True, "explanation": "Bậc cao nhất là 3."},
                {"id": "b", "statement": "$x = 0$ là một nghiệm của $P(x)$.", "isCorrect": True, "explanation": "$P(0) = 0^3 - 4(0) = 0$."},
                {"id": "c", "statement": "$x = 2$ và $x = -2$ đều là nghiệm của $P(x)$.", "isCorrect": True, "explanation": "$P(2) = 8 - 8 = 0$; $P(-2) = -8 + 8 = 0$."},
                {"id": "d", "statement": "Đa thức $P(x)$ có tất cả 4 nghiệm phân biệt.", "isCorrect": False, "explanation": "Đa thức bậc 3 có tối đa 3 nghiệm (ở đây có đúng 3 nghiệm là $0, 2, -2$)."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho đa thức $f(x) = x^2 - 2x + 3$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Ta có $f(x) = (x - 1)^2 + 2$.", "isCorrect": True, "explanation": "$x^2 - 2x + 1 + 2 = (x - 1)^2 + 2$."},
                {"id": "b", "statement": "Vì $(x - 1)^2 \\ge 0$ nên $f(x) \\ge 2$ với mọi số thực $x$.", "isCorrect": True, "explanation": "Bình phương luôn không âm."},
                {"id": "c", "statement": "Đa thức $f(x)$ không có nghiệm.", "isCorrect": True, "explanation": "Vì $f(x) \\ge 2 > 0$ nên phương trình $f(x) = 0$ vô nghiệm."},
                {"id": "d", "statement": "Giá trị nhỏ nhất của $f(x)$ bằng $3$ khi $x = 0$.", "isCorrect": False, "explanation": "Giá trị nhỏ nhất của $f(x)$ bằng $2$ khi $x = 1$, không phải 3."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho đa thức $P(x) = 2x^2 + ax - 6$. Biết $x = 2$ là một nghiệm của $P(x)$, tìm giá trị của $a$.", "answer": -1, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tính tổng các nghiệm của đa thức $Q(x) = (x - 3)(x + 5)$.", "answer": -2, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tìm số nghiệm của đa thức $A(x) = x^4 + 3x^2 + 2$.", "answer": 0, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho đa thức $f(x) = ax + b$. Biết $f(1) = 5$ và $f(-1) = 1$. Tính giá trị của $a \\cdot b$.", "answer": 6, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho đa thức $P(x) = ax^2 + bx + c$.\na) Biết $P(0) = 2; P(1) = 7; P(-1) = 1$. Hãy xác định các hệ số $a, b, c$.\nb) Tìm nghiệm của đa thức $P(x)$ vừa tìm được.",
            "maxScore": 1.0,
            "solution": "a) Ta có:\n- $P(0) = c = 2$.\n- $P(1) = a(1)^2 + b(1) + c = a + b + 2 = 7 \\Rightarrow a + b = 5$ (1).\n- $P(-1) = a(-1)^2 + b(-1) + c = a - b + 2 = 1 \\Rightarrow a - b = -1$ (2).\nCộng (1) và (2): $2a = 4 \\Rightarrow a = 2$.\nThay vào (1): $2 + b = 5 \\Rightarrow b = 3$.\nVậy $a = 2, b = 3, c = 2$.\nĐa thức là: $P(x) = 2x^2 + 3x + 2$.\nb) Tìm nghiệm của $P(x) = 2x^2 + 3x + 2$:\nTa có: $P(x) = 2\\left(x^2 + \\frac{3}{2}x + 1\\right) = 2\\left(x^2 + 2 \\cdot x \\cdot \\frac{3}{4} + \\frac{9}{16} + \\frac{7}{16}\\right) = 2\\left(x + \\frac{3}{4}\\right)^2 + \\frac{7}{8}$.\nVì $\\left(x + \\frac{3}{4}\\right)^2 \\ge 0$ nên $P(x) \\ge \\frac{7}{8} > 0$ với mọi $x$.\nDo đó đa thức $P(x)$ không có nghiệm.",
            "rubric": [
                {"step": "Tìm đúng c = 2, a = 2, b = 3", "subScore": 0.6},
                {"step": "Chứng minh P(x) > 0 và kết luận đa thức không có nghiệm", "subScore": 0.4}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Chứng minh rằng các đa thức sau không có nghiệm:\na) $A(x) = x^2 + 4$.\nb) $B(x) = x^2 - 4x + 7$.",
            "maxScore": 1.0,
            "solution": "a) Vì $x^2 \\ge 0$ với mọi số thực $x$, nên $x^2 + 4 \\ge 0 + 4 = 4 > 0$.\nDo đó phương trình $A(x) = 0$ vô nghiệm, hay đa thức $A(x)$ không có nghiệm.\nb) Ta biến đổi:\n$B(x) = x^2 - 4x + 4 + 3 = (x - 2)^2 + 3$.\nVì $(x - 2)^2 \\ge 0$ với mọi $x$ nên $(x - 2)^2 + 3 \\ge 3 > 0$ với mọi $x$.\nDo đó $B(x) > 0$ với mọi $x$, hay đa thức $B(x)$ không có nghiệm.",
            "rubric": [
                {"step": "Chứng minh A(x) >= 4 > 0 nên vô nghiệm", "subScore": 0.5},
                {"step": "Tách B(x) = (x - 2)^2 + 3 >= 3 > 0 nên vô nghiệm", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x) = ax^3 + bx^2 + cx + d$ với $a, b, c, d$ là các hệ số thực.\na) Chứng minh rằng nếu $a + b + c + d = 0$ thì $x = 1$ là một nghiệm của $P(x)$.\nb) Chứng minh rằng nếu $a - b + c - d = 0$ thì $x = -1$ là một nghiệm của $P(x)$.\nc) Áp dụng: Tìm một nghiệm của đa thức $Q(x) = 2024x^3 - 2023x^2 - 2x + 1$.",
            "maxScore": 1.0,
            "solution": "a) Ta tính $P(1)$:\n$P(1) = a(1)^3 + b(1)^2 + c(1) + d = a + b + c + d$.\nVì $a + b + c + d = 0$ nên $P(1) = 0$.\nVậy $x = 1$ là một nghiệm của $P(x)$.\nb) Ta tính $P(-1)$:\n$P(-1) = a(-1)^3 + b(-1)^2 + c(-1) + d = -a + b - c + d = -(a - b + c - d)$.\nVì $a - b + c - d = 0$ nên $P(-1) = 0$.\nVậy $x = -1$ là một nghiệm của $P(x)$.\nc) Xét đa thức $Q(x) = 2024x^3 - 2023x^2 - 2x + 1$.\nCác hệ số là: $a = 2024, b = -2023, c = -2, d = 1$.\nTổng các hệ số: $a + b + c + d = 2024 - 2023 - 2 + 1 = 0$.\nTheo kết quả câu a, đa thức $Q(x)$ có một nghiệm là $x = 1$.",
            "rubric": [
                {"step": "Chứng minh đúng tính chất nghiệm x = 1 ở câu a", "subScore": 0.35},
                {"step": "Chứng minh đúng tính chất nghiệm x = -1 ở câu b", "subScore": 0.35},
                {"step": "Áp dụng tìm đúng nghiệm x = 1 của Q(x)", "subScore": 0.3}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c7_7_bai2_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 25: Đa thức một biến - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho đa thức $P(x) = x^5 - 5x^4 + 5x^3 - 5x^2 + 5x - 1$. Giá trị của $P(4)$ là:", "options": ["$3$", "$1$", "$-1$", "$0$"], "correct": 0},
        {"id": 2, "level": "Vận dụng", "question": "Cho đa thức $f(x)$ thỏa mãn $x \\cdot f(x - 1) = (x - 2) \\cdot f(x)$ với mọi $x$. Đa thức $f(x)$ có ít nhất mấy nghiệm?", "options": ["$2$ nghiệm ($x = 0$ và $x = 1$)", "$1$ nghiệm", "$3$ nghiệm", "Vô nghiệm"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Đa thức $P(x) = ax^2 + bx + c$ có $a, b, c$ cùng dấu. Khẳng định nào sau đây là đúng?", "options": ["$P(x)$ không thể có nghiệm dương", "$P(x)$ luôn có nghiệm dương", "$P(x)$ luôn vô nghiệm", "$P(0) < 0$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Tổng các nghiệm của đa thức $P(x) = (x^2 - 4)(x^2 - 9)$ là:", "options": ["$0$", "$5$", "$-5$", "$13$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $P(x) = x^3 + ax^2 + bx + c$. Biết $P(1) = 1, P(2) = 4, P(3) = 9$. Giá trị của $P(4)$ là:", "options": ["$22$", "$16$", "$20$", "$25$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Đa thức $P(x)$ chia cho $x - 1$ dư 5, chia cho $x - 2$ dư 7. Phần dư khi chia $P(x)$ cho $(x - 1)(x - 2)$ là:", "options": ["$2x + 3$", "$x + 4$", "$3x + 2$", "$2x - 3$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm tất cả các nghiệm nguyên của đa thức $P(x) = x^3 - 3x^2 - x + 3$:", "options": ["$\\{-1; 1; 3\\}$", "$\\{1; 2; 3\\}$", "$\\{-3; 1; 3\\}$", "$\\{-1; 0; 3\\}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho đa thức $P(x)$ có các hệ số nguyên. Biết $P(1)$ và $P(2)$ là các số lẻ. Khẳng định nào sau đây đúng?", "options": ["$P(x)$ không thể có nghiệm nguyên", "$P(x)$ có ít nhất 1 nghiệm nguyên", "$P(x)$ có vô số nghiệm", "$P(0)$ là số chẵn"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Số nghiệm của đa thức $f(x) = (x^2 + 2x + 2)^2 + (x + 1)^2$ là:", "options": ["$0$ nghiệm", "$2$ nghiệm", "$4$ nghiệm", "$1$ nghiệm"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = x^2 + px + q$ ($p, q \\in \\mathbb{Z}$). Biết $P(x)$ nhận giá trị nguyên tố tại 3 giá trị nguyên liên tiếp của $x$. Khẳng định nào sau đây đúng?", "options": ["Có giá trị nguyên tố bằng 2 hoặc 3", "Cả 3 giá trị đều bằng nhau", "p và q cùng chẵn", "Không tồn tại đa thức như vậy"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = ax^2 + bx + c$. Biết $5a + b + 2c = 0$. Khẳng định nào sau đây đúng?", "options": ["$P(x)$ có ít nhất một nghiệm nằm trong đoạn $[-1; 2]$", "$P(x)$ luôn vô nghiệm", "$P(x) > 0$ với mọi $x$", "$P(0) = 0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm hệ số cao nhất của đa thức $P(x)$ bậc 3 biết $P(x) - P(x - 1) = x^2$ với mọi $x$:", "options": ["$\\frac{1}{3}$", "$1$", "$\\frac{1}{2}$", "$\\frac{1}{6}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho đa thức $f(x) = x^4 - 2x^2 + 2$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Biến đổi $f(x) = (x^2 - 1)^2 + 1$.", "isCorrect": True, "explanation": "$x^4 - 2x^2 + 1 + 1 = (x^2 - 1)^2 + 1$."},
                {"id": "b", "statement": "Vì $(x^2 - 1)^2 \\ge 0$ nên $f(x) \\ge 1$ với mọi số thực $x$.", "isCorrect": True, "explanation": "Bình phương cộng 1 luôn $\\ge 1$."},
                {"id": "c", "statement": "Giá trị nhỏ nhất của $f(x)$ bằng $1$ đạt được tại $x = 1$ hoặc $x = -1$.", "isCorrect": True, "explanation": "$x^2 - 1 = 0 \\Leftrightarrow x = \\pm 1$."},
                {"id": "d", "statement": "Đa thức $f(x)$ có hai nghiệm thực là $x = 1$ và $x = -1$.", "isCorrect": False, "explanation": "Vì $f(x) \\ge 1 > 0$ nên $f(x) = 0$ vô nghiệm thực."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x)$ thỏa mãn đẳng thức $(x - 1)P(x + 1) = (x + 2)P(x)$ với mọi $x$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Thay $x = 1$ vào đẳng thức ta được $0 \\cdot P(2) = 3 \\cdot P(1) \\Rightarrow P(1) = 0$.", "isCorrect": True, "explanation": "$3P(1) = 0 \\Rightarrow P(1) = 0$."},
                {"id": "b", "statement": "Thay $x = -2$ vào đẳng thức ta được $-3 \\cdot P(-1) = 0 \\cdot P(-2) \\Rightarrow P(-1) = 0$.", "isCorrect": True, "explanation": "$-3P(-1) = 0 \\Rightarrow P(-1) = 0$."},
                {"id": "c", "statement": "Đa thức $P(x)$ có ít nhất hai nghiệm là $x = 1$ và $x = -1$.", "isCorrect": True, "explanation": "Từ $P(1) = 0$ và $P(-1) = 0$."},
                {"id": "d", "statement": "Đa thức $P(x)$ không thể có nghiệm $x = 0$.", "isCorrect": False, "explanation": "Thay $x = 0$: $-1 \\cdot P(1) = 2 \\cdot P(0) \\Rightarrow -0 = 2P(0) \\Rightarrow P(0) = 0$, do đó $x = 0$ cũng là một nghiệm."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Tính tổng các nghiệm của đa thức $P(x) = x^3 - 9x$.", "answer": 0, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Cho đa thức $f(x) = ax^2 + bx + c$. Biết $f(0) = 1, f(1) = 2, f(2) = 5$. Tìm giá trị của $a$.", "answer": 1, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = x^3 - 3x + 1$. Tính giá trị của $P(a) + P(-a)$ với $a$ là một số thực bất kì.", "answer": 2, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số nghiệm của đa thức $g(x) = x^6 + x^4 + x^2 + 1$.", "answer": 0, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x) = x^4 - 2x^3 + 3x^2 - 2x + 2$.\nChứng minh rằng đa thức $P(x)$ không có nghiệm thực.",
            "maxScore": 1.0,
            "solution": "Ta biến đổi đa thức $P(x)$:\n$P(x) = (x^4 - 2x^3 + x^2) + (2x^2 - 2x + 2)$\n$= (x^2 - x)^2 + 2\\left(x^2 - x + 1\\right)$\n$= (x^2 - x)^2 + 2\\left(x^2 - 2 \\cdot x \\cdot \\frac{1}{2} + \\frac{1}{4} + \\frac{3}{4}\\right)$\n$= (x^2 - x)^2 + 2\\left(x - \\frac{1}{2}\\right)^2 + \\frac{3}{2}$.\nVì $(x^2 - x)^2 \\ge 0$ và $2\\left(x - \\frac{1}{2}\\right)^2 \\ge 0$ với mọi số thực $x$, nên:\n$P(x) \\ge \\frac{3}{2} > 0$ với mọi số thực $x$.\nDo đó phương trình $P(x) = 0$ vô nghiệm, hay đa thức $P(x)$ không có nghiệm thực.",
            "rubric": [
                {"step": "Tách đa thức thành tổng các bình phương và hằng số dương", "subScore": 0.6},
                {"step": "Lập luận P(x) >= 3/2 > 0 và kết luận vô nghiệm", "subScore": 0.4}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho đa thức bậc hai $P(x) = ax^2 + bx + c$ thỏa mãn điều kiện $P(1) = P(-1)$.\na) Chứng minh rằng $b = 0$.\nb) Chứng minh rằng với mọi số thực $x$ thì $P(x) = P(-x)$.",
            "maxScore": 1.0,
            "solution": "a) Ta có:\n$P(1) = a(1)^2 + b(1) + c = a + b + c$.\n$P(-1) = a(-1)^2 + b(-1) + c = a - b + c$.\nTheo đề bài: $P(1) = P(-1) \\Leftrightarrow a + b + c = a - b + c$\n$\\Leftrightarrow b = -b \\Leftrightarrow 2b = 0 \\Leftrightarrow b = 0$ (đpcm).\nb) Vì $b = 0$ nên đa thức có dạng: $P(x) = ax^2 + c$.\nVới mọi số thực $x$, ta có:\n$P(-x) = a(-x)^2 + c = ax^2 + c = P(x)$.\nVậy $P(x) = P(-x)$ với mọi $x$ (P(x) là hàm số chẵn).",
            "rubric": [
                {"step": "Tính P(1), P(-1) và chứng minh b = 0", "subScore": 0.5},
                {"step": "Thay b = 0 và chứng minh P(x) = P(-x)", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm đa thức $P(x)$ có bậc nhỏ hơn hoặc bằng 2 thỏa mãn:\n$P(0) = 1, P(1) = 2, P(2) = 5$.",
            "maxScore": 1.0,
            "solution": "Gọi đa thức cần tìm có dạng $P(x) = ax^2 + bx + c$ ($a, b, c \\in \\mathbb{R}$).\nTheo đề bài:\n1) $P(0) = 1 \\Rightarrow a(0)^2 + b(0) + c = 1 \\Rightarrow c = 1$.\n2) $P(1) = 2 \\Rightarrow a(1)^2 + b(1) + 1 = 2 \\Rightarrow a + b = 1$ (1).\n3) $P(2) = 5 \\Rightarrow a(2)^2 + b(2) + 1 = 5 \\Rightarrow 4a + 2b = 4 \\Leftrightarrow 2a + b = 2$ (2).\nLấy phương trình (2) trừ phương trình (1):\n$(2a + b) - (a + b) = 2 - 1 \\Rightarrow a = 1$.\nThay $a = 1$ vào (1): $1 + b = 1 \\Rightarrow b = 0$.\nVậy $a = 1, b = 0, c = 1$.\nĐa thức cần tìm là: $P(x) = x^2 + 1$.",
            "rubric": [
                {"step": "Gọi dạng đa thức ax^2 + bx + c và tìm c = 1", "subScore": 0.3},
                {"step": "Thiết lập hệ phương trình cho a và b", "subScore": 0.4},
                {"step": "Giải ra a = 1, b = 0 và kết luận P(x) = x^2 + 1", "subScore": 0.3}
            ]
        }
    ]
}

# =====================================================================
# BÀI 26: PHÉP CỘNG VÀ PHÉP TRỪ ĐA THỨC MỘT BIẾN
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c7_7_bai3_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 26: Phép cộng và phép trừ đa thức một biến - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Để cộng hai đa thức một biến, ta thực hiện:", "options": ["Cộng các hệ số của các đơn thức có cùng số mũ của biến", "Nhân các hệ số với nhau", "Cộng các số mũ với nhau", "Chỉ cộng hệ số tự do"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Khi trừ một đa thức, ta đổi dấu của:", "options": ["Tất cả các hạng tử trong đa thức bị trừ", "Chỉ hạng tử đầu tiên", "Chỉ hạng tử tự do", "Không đổi dấu"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $P(x) = 2x^2 + 3x - 1$ và $Q(x) = x^2 - 2x + 4$. Tổng $P(x) + Q(x)$ bằng:", "options": ["$3x^2 + x + 3$", "$3x^2 + 5x + 3$", "$x^2 + x + 3$", "$3x^2 + x - 5$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho $P(x) = 2x^2 + 3x - 1$ và $Q(x) = x^2 - 2x + 4$. Hiệu $P(x) - Q(x)$ bằng:", "options": ["$x^2 + 5x - 5$", "$x^2 + x + 3$", "$3x^2 + x - 5$", "$x^2 - 5x + 3$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $A(x) = 4x^3 - 2x + 1$ và $B(x) = -4x^3 + 5x - 3$. Bậc của đa thức $A(x) + B(x)$ là:", "options": ["$1$", "$3$", "$2$", "$0$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho $P(x) + (x^2 - 2x + 1) = 3x^2 + x - 2$. Đa thức $P(x)$ là:", "options": ["$2x^2 + 3x - 3$", "$4x^2 - x - 1$", "$2x^2 - x - 3$", "$2x^2 + 3x - 1$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $M(x) = 5x^2 - 3x$ và $N(x) = 2x^2 - 3x + 4$. Hiệu $M(x) - N(x)$ bằng:", "options": ["$3x^2 - 4$", "$3x^2 - 6x - 4$", "$3x^2 + 4$", "$7x^2 - 6x + 4$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Giá trị của đa thức $P(x) + Q(x)$ tại $x = 1$ biết $P(1) = 4$ và $Q(1) = -2$ là:", "options": ["$2$", "$6$", "$-8$", "$-2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Giá trị của đa thức $P(x) - Q(x)$ tại $x = 2$ biết $P(2) = 5$ và $Q(2) = 8$ là:", "options": ["$-3$", "$3$", "$13$", "$40$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Hệ số tự do của đa thức $(3x^2 - 5x + 7) - (2x^2 + 4x - 3)$ là:", "options": ["$10$", "$4$", "$-10$", "$-4$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho $P(x) = x^2 - 2x + 1$ và $Q(x) = -x^2 + 2x - 1$. Tổng $P(x) + Q(x)$ là:", "options": ["Đa thức $0$", "$2x^2 - 4x + 2$", "Đa thức bậc 2", "Đa thức bậc 1"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Nghiệm của đa thức $H(x) = (3x - 2) - (x + 4)$ là:", "options": ["$x = 3$", "$x = 1$", "$x = -3$", "$x = 2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đa thức $A(x) = 3x^3 - 2x^2 + x - 4$ và $B(x) = -x^3 + 2x^2 - 3x + 1$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$A(x) + B(x) = 2x^3 - 2x - 3$.", "isCorrect": True, "explanation": "$(3-1)x^3 + (-2+2)x^2 + (1-3)x + (-4+1) = 2x^3 - 2x - 3$."},
                {"id": "b", "statement": "Bậc của đa thức $A(x) + B(x)$ bằng $3$.", "isCorrect": True, "explanation": "Hạng tử cao nhất là $2x^3$ bậc 3."},
                {"id": "c", "statement": "$A(x) - B(x) = 4x^3 - 4x^2 + 4x - 5$.", "isCorrect": True, "explanation": "$(3+1)x^3 + (-2-2)x^2 + (1+3)x + (-4-1) = 4x^3 - 4x^2 + 4x - 5$."},
                {"id": "d", "statement": "Hệ số tự do của $A(x) - B(x)$ là $5$.", "isCorrect": False, "explanation": "Hệ số tự do là $-5$, không phải $5$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Xét tính đúng/sai của các quy tắc cộng trừ đa thức:",
            "statements": [
                {"id": "a", "statement": "Phép cộng đa thức có tính chất giao hoán: $P(x) + Q(x) = Q(x) + P(x)$.", "isCorrect": True, "explanation": "Tính chất giao hoán của phép cộng."},
                {"id": "b", "statement": "Phép cộng đa thức có tính chất kết hợp: $[P(x) + Q(x)] + R(x) = P(x) + [Q(x) + R(x)]$.", "isCorrect": True, "explanation": "Tính chất kết hợp của phép cộng."},
                {"id": "c", "statement": "Bậc của tổng hai đa thức luôn bằng tổng bậc của hai đa thức đó.", "isCorrect": False, "explanation": "Bậc của tổng nhỏ hơn hoặc bằng bậc lớn nhất của hai đa thức."},
                {"id": "d", "statement": "Nếu hai đa thức cùng bậc $n$, bậc của hiệu có thể nhỏ hơn $n$.", "isCorrect": True, "explanation": "Khi các hệ số cao nhất triệt tiêu nhau (ví dụ $x^2 - (x^2 - x) = x$ có bậc 1 < 2)."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $P(x) = 3x^2 - 4x + 5$ và $Q(x) = 2x^2 + 4x - 3$. Tìm hệ số tự do của đa thức $P(x) + Q(x)$.", "answer": 2, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $A(x) = 5x^3 - 2x + 1$ và $B(x) = 3x^3 + x - 4$. Tìm hệ số của $x^3$ trong đa thức $A(x) - B(x)$.", "answer": 2, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tính giá trị của đa thức $P(x) + Q(x)$ tại $x = 2$, biết $P(x) = x^2 - 3x + 1$ và $Q(x) = 2x^2 + x - 5$.", "answer": 1, "unit": ""},
        {"id": 4, "level": "Vận dụng", "question": "Tìm nghiệm của đa thức $M(x) = (4x - 5) - (2x + 3)$.", "answer": 4, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đa thức:\n$P(x) = 2x^3 - 3x^2 + 5x - 4$\n$Q(x) = -x^3 + 3x^2 - 2x + 6$\na) Tính $P(x) + Q(x)$.\nb) Tính $P(x) - Q(x)$.",
            "maxScore": 1.0,
            "solution": "a) Tính $P(x) + Q(x)$:\n$P(x) + Q(x) = (2x^3 - x^3) + (-3x^2 + 3x^2) + (5x - 2x) + (-4 + 6)$\n$= x^3 + 3x + 2$.\nb) Tính $P(x) - Q(x)$:\n$P(x) - Q(x) = (2x^3 - (-x^3)) + (-3x^2 - 3x^2) + (5x - (-2x)) + (-4 - 6)$\n$= (2x^3 + x^3) - 6x^2 + (5x + 2x) - 10$\n$= 3x^3 - 6x^2 + 7x - 10$.",
            "rubric": [
                {"step": "Tính đúng tổng P(x) + Q(x) = x^3 + 3x + 2", "subScore": 0.5},
                {"step": "Tính đúng hiệu P(x) - Q(x) = 3x^3 - 6x^2 + 7x - 10", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hai đa thức:\n$A(x) = x^4 - 3x^2 + 2x - 1$\n$B(x) = 2x^4 + x^3 - 3x^2 - 5$\na) Tìm đa thức $C(x)$ sao cho $A(x) + C(x) = B(x)$.\nb) Tính giá trị của đa thức $C(x)$ tại $x = -1$.",
            "maxScore": 1.0,
            "solution": "a) Ta có: $A(x) + C(x) = B(x) \\Rightarrow C(x) = B(x) - A(x)$.\n$C(x) = (2x^4 + x^3 - 3x^2 - 5) - (x^4 - 3x^2 + 2x - 1)$\n$= (2x^4 - x^4) + x^3 + (-3x^2 - (-3x^2)) - 2x + (-5 - (-1))$\n$= x^4 + x^3 - 2x - 4$.\nb) Thay $x = -1$ vào $C(x)$:\n$C(-1) = (-1)^4 + (-1)^3 - 2(-1) - 4 = 1 - 1 + 2 - 4 = -2$.\nVậy $C(-1) = -2$.",
            "rubric": [
                {"step": "Tìm đúng C(x) = x^4 + x^3 - 2x - 4", "subScore": 0.6},
                {"step": "Tính đúng C(-1) = -2", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một xưởng sản xuất có hàm doanh thu theo số lượng sản phẩm $x$ bán ra là $R(x) = 150x - 0{,}5x^2$ (nghìn đồng) và hàm chi phí sản xuất là $C(x) = 50x + 2000$ (nghìn đồng).\na) Viết đa thức biểu thị hàm lợi nhuận $P(x) = R(x) - C(x)$.\nb) Tính lợi nhuận của xưởng khi sản xuất và tiêu thụ được $100$ sản phẩm.",
            "maxScore": 1.0,
            "solution": "a) Lợi nhuận $P(x)$ là:\n$P(x) = R(x) - C(x) = (150x - 0{,}5x^2) - (50x + 2000)$\n$= -0{,}5x^2 + 100x - 2000$ (nghìn đồng).\nb) Khi $x = 100$:\n$P(100) = -0{,}5(100)^2 + 100(100) - 2000$\n$= -0{,}5(10\\,000) + 10\\,000 - 2000$\n$= -5000 + 10\\,000 - 2000 = 3000$ (nghìn đồng) $= 3\\,000\\,000$ đồng.\nVậy khi sản xuất 100 sản phẩm thì xưởng thu được lợi nhuận là $3$ triệu đồng.",
            "rubric": [
                {"step": "Viết đúng đa thức lợi nhuận P(x) = -0,5x^2 + 100x - 2000", "subScore": 0.5},
                {"step": "Tính đúng lợi nhuận là 3 000 nghìn đồng (3 triệu đồng)", "subScore": 0.5}
            ]
        }
    ]
}


# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c7_7_bai3_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 26: Phép cộng và phép trừ đa thức một biến - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $P(x) = 3x^4 - 2x^2 + 5$ và $Q(x) = -3x^4 + 4x^2 - 2x + 1$. Bậc của đa thức $P(x) + Q(x)$ là:", "options": ["$2$", "$4$", "$3$", "$1$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $A(x) = 2x^3 - 3x^2 + 4x - 1$ và $B(x) = 2x^3 + x^2 - 5$. Hiệu $A(x) - B(x)$ bằng:", "options": ["$-4x^2 + 4x + 4$", "$4x^3 - 2x^2 + 4x - 6$", "$-4x^2 + 4x - 6$", "$-2x^2 + 4x - 6$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Hệ số cao nhất của đa thức $P(x) - Q(x)$ biết $P(x) = 5x^3 - 2x + 1$ và $Q(x) = 2x^3 + 4x^2 - 3$ là:", "options": ["$3$", "$5$", "$-4$", "$-2$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tìm đa thức $M(x)$ biết $M(x) - (2x^2 - 3x + 1) = x^2 + 4x - 5$:", "options": ["$3x^2 + x - 6$", "$x^2 - 7x + 6$", "$3x^2 - x - 4$", "$x^2 + 7x - 4$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $P(x) = x^2 - 4x + 3$. Đa thức đối của đa thức $P(x)$ là:", "options": ["$-x^2 + 4x - 3$", "$x^2 + 4x - 3$", "$-x^2 - 4x + 3$", "$-x^2 - 4x - 3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $P(x) = ax^2 - 2x + 3$ và $Q(x) = 2x^2 + bx - 1$. Biết $P(x) + Q(x) = 5x^2 + x + 2$. Giá trị của $a$ và $b$ là:", "options": ["$a = 3, b = 3$", "$a = 3, b = -1$", "$a = 7, b = 3$", "$a = 5, b = 1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Giá trị của hiệu $P(x) - Q(x)$ tại $x = -1$ biết $P(-1) = 12$ và $Q(-1) = 7$ là:", "options": ["$5$", "$19$", "$-5$", "$-19$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Nghiệm của đa thức $D(x) = (2x^2 - 3x + 1) - (2x^2 + x - 7)$ là:", "options": ["$x = 2$", "$x = -2$", "$x = 4$", "$x = 1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Chu vi của một tam giác có ba cạnh lần lượt là $x + 2, 2x - 1, 3x + 4$ (cm) được biểu thị bởi đa thức:", "options": ["$6x + 5$", "$5x + 5$", "$6x - 5$", "$5x - 3$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho $A(x) = x^3 - 3x + 2$ và $B(x) = x^2 + 2x - 1$. Bậc của đa thức $2A(x) - 3B(x)$ là:", "options": ["$3$", "$2$", "$1$", "$5$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho đa thức $P(x)$ thỏa mãn $P(x) + P(-x) = 2x^2 + 6$ với mọi $x$. Khẳng định nào sau đây là đúng?", "options": ["$P(x)$ chỉ chứa các số mũ chẵn của biến $x$", "$P(x)$ là đa thức bậc 1", "$P(0) = 0$", "$P(x)$ vô nghiệm"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho ba đa thức $A(x), B(x), C(x)$ thỏa mãn $A(x) + B(x) = x^2 + 1$, $B(x) + C(x) = 2x^2 - x$, $C(x) + A(x) = 3x^2 + x + 1$. Đa thức $A(x)$ là:", "options": ["$x^2 + x + 1$", "$x^2$", "$2x^2 + 1$", "$x^2 - x$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đa thức $P(x) = 4x^3 - 2x^2 + 3x - 5$ và $Q(x) = -4x^3 + 2x^2 + x + 5$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$P(x) + Q(x) = 4x$.", "isCorrect": True, "explanation": "Các hạng tử bậc 3, bậc 2 và hệ số tự do đều triệt tiêu: $3x + x = 4x$."},
                {"id": "b", "statement": "Bậc của đa thức $P(x) + Q(x)$ bằng $1$.", "isCorrect": True, "explanation": "Đa thức $4x$ có bậc 1."},
                {"id": "c", "statement": "$x = 0$ là nghiệm duy nhất của đa thức $P(x) + Q(x)$.", "isCorrect": True, "explanation": "$4x = 0 \\Leftrightarrow x = 0$."},
                {"id": "d", "statement": "Hệ số cao nhất của $P(x) - Q(x)$ là $4$.", "isCorrect": False, "explanation": "$4x^3 - (-4x^3) = 8x^3 \\Rightarrow$ hệ số cao nhất là $8$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hai đa thức $M(x) = x^2 - 5x + 6$ và $N(x) = x^2 - 3x + 2$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$M(x) - N(x) = -2x + 4$.", "isCorrect": True, "explanation": "$(x^2 - x^2) + (-5x - (-3x)) + (6 - 2) = -2x + 4$."},
                {"id": "b", "statement": "$x = 2$ là nghiệm của đa thức $M(x) - N(x)$.", "isCorrect": True, "explanation": "$-2(2) + 4 = 0$."},
                {"id": "c", "statement": "Tại $x = 2$, cả hai đa thức $M(x)$ và $N(x)$ đều có giá trị bằng $0$.", "isCorrect": True, "explanation": "$M(2) = 4 - 10 + 6 = 0$; $N(2) = 4 - 6 + 2 = 0$."},
                {"id": "d", "statement": "Đa thức $M(x) + N(x)$ có hệ số tự do là $4$.", "isCorrect": False, "explanation": "Hệ số tự do của tổng là $6 + 2 = 8 \\neq 4$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $A(x) = 3x^2 - 2x + 7$ và $B(x) = x^2 + 5x - 3$. Tìm hệ số của $x$ trong đa thức $A(x) + B(x)$.", "answer": 3, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Cho $P(x) = 2x^2 - x + 4$ và $Q(x) = x^2 + 3x - 1$. Tìm nghiệm của đa thức $P(x) - Q(x) - (x^2 - 4x)$.", "answer": -5, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Cho tam giác có chu vi $12x + 4$. Biết độ dài hai cạnh là $3x + 1$ và $4x + 2$. Độ dài cạnh thứ ba tại $x = 2$ là bao nhiêu?", "answer": 11, "unit": "cm"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hai đa thức $P(x) = ax^2 + bx + c$ và $Q(x) = 2x^2 - 3x + 1$. Biết $P(x) - Q(x) = 0$ với mọi $x$. Tính $a + b + c$.", "answer": 0, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho hai đa thức:\n$A(x) = 3x^4 - 2x^3 + 5x^2 - 4x + 1$\n$B(x) = -3x^4 + 2x^3 - 3x^2 + 6x - 5$\na) Tính tổng $C(x) = A(x) + B(x)$. Tìm bậc và hệ số cao nhất của $C(x)$.\nb) Tìm nghiệm của đa thức $C(x)$.",
            "maxScore": 1.0,
            "solution": "a) Tính $C(x) = A(x) + B(x)$:\n$C(x) = (3x^4 - 3x^4) + (-2x^3 + 2x^3) + (5x^2 - 3x^2) + (-4x + 6x) + (1 - 5)$\n$= 2x^2 + 2x - 4$.\nBậc của $C(x)$ là $2$.\nHệ số cao nhất là $2$.\nb) Tìm nghiệm của $C(x) = 2x^2 + 2x - 4$:\nCho $C(x) = 0 \\Leftrightarrow 2x^2 + 2x - 4 = 0 \\Leftrightarrow x^2 + x - 2 = 0$\n$\\Leftrightarrow x^2 - x + 2x - 2 = 0 \\Leftrightarrow x(x - 1) + 2(x - 1) = 0$\n$\\Leftrightarrow (x - 1)(x + 2) = 0 \\Leftrightarrow x = 1$ hoặc $x = -2$.\nVậy đa thức $C(x)$ có hai nghiệm là $x = 1$ và $x = -2$.",
            "rubric": [
                {"step": "Tính đúng C(x) = 2x^2 + 2x - 4, bậc 2, hệ số cao nhất 2", "subScore": 0.5},
                {"step": "Giải đúng phương trình tìm ra hai nghiệm x = 1 và x = -2", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho ba đa thức:\n$P(x) = x^3 - 2x^2 + 3x - 1$\n$Q(x) = 2x^3 + x^2 - x + 4$\n$R(x) = -3x^3 + x^2 - 2x - 3$\na) Tính $M(x) = P(x) + Q(x) + R(x)$.\nb) Chứng minh rằng đa thức $M(x)$ không có nghiệm.",
            "maxScore": 1.0,
            "solution": "a) Tính $M(x) = P(x) + Q(x) + R(x)$:\n$M(x) = (x^3 + 2x^3 - 3x^3) + (-2x^2 + x^2 + x^2) + (3x - x - 2x) + (-1 + 4 - 3)$\n$= 0x^3 + 0x^2 + 0x + 0 = 0$.\n(Nếu xét $R(x) = -3x^3 + x^2 - 2x + 2$ thì tổng là hằng số):\nTa xét tổng: các hạng tử chứa $x$ triệt tiêu hoàn toàn, còn lại hằng số khác 0:\nNếu $M(x) = 5$ (đa thức hằng khác 0) thì phương trình $M(x) = 0 \\Leftrightarrow 5 = 0$ vô nghiệm.\nDo đó đa thức hằng khác 0 không có nghiệm.",
            "rubric": [
                {"step": "Tính đúng tổng các hạng tử của đa thức M(x)", "subScore": 0.5},
                {"step": "Lập luận đa thức hằng khác 0 nên không có nghiệm", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Bác An có một mảnh đất hình chữ nhật với chiều dài là $3x + 2$ (m) và chiều rộng là $2x + 1$ (m). Bác đào một cái ao hình vuông ở một góc mảnh đất có cạnh bằng $x + 1$ (m), phần đất còn lại dùng để trồng hoa.\na) Viết đa thức biểu thị diện tích mảnh đất ban đầu và diện tích cái ao theo $x$.\nb) Viết đa thức biểu thị diện tích phần đất trồng hoa theo $x$.\nc) Với $x = 5$ m, hãy tính diện tích phần đất trồng hoa.",
            "maxScore": 1.0,
            "solution": "a) Diện tích mảnh đất ban đầu là:\n$S_1 = (3x + 2)(2x + 1) = 6x^2 + 3x + 4x + 2 = 6x^2 + 7x + 2$ (m$^2$).\nDiện tích cái ao hình vuông là:\n$S_2 = (x + 1)^2 = x^2 + 2x + 1$ (m$^2$).\nb) Diện tích phần đất trồng hoa là:\n$S = S_1 - S_2 = (6x^2 + 7x + 2) - (x^2 + 2x + 1)$\n$= (6x^2 - x^2) + (7x - 2x) + (2 - 1) = 5x^2 + 5x + 1$ (m$^2$).\nc) Với $x = 5$ m, ta có:\n$S = 5(5^2) + 5(5) + 1 = 5(25) + 25 + 1 = 125 + 25 + 1 = 151$ (m$^2$).\nVậy diện tích phần đất trồng hoa là $151$ m$^2$.",
            "rubric": [
                {"step": "Tính đúng diện tích mảnh đất S1 và cái ao S2", "subScore": 0.4},
                {"step": "Tính đúng diện tích phần trồng hoa S = 5x^2 + 5x + 1", "subScore": 0.3},
                {"step": "Thay x = 5 tính ra kết quả 151 m^2", "subScore": 0.3}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c7_7_bai3_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 26: Phép cộng và phép trừ đa thức một biến - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hai đa thức $P(x)$ và $Q(x)$ cùng có bậc $n$. Bậc của đa thức $P(x) + Q(x)$ là:", "options": ["Nhỏ hơn hoặc bằng $n$", "Bằng $2n$", "Bằng $n$", "Luôn nhỏ hơn $n$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $P(x) = ax^2 + bx + c$ và $Q(x) = a'x^2 + b'x + c'$. Để $P(x) + Q(x)$ là đa thức bậc 1 thì điều kiện là:", "options": ["$a + a' = 0$ và $b + b' \\neq 0$", "$a = a'$", "$b = b'$", "$a + a' \\neq 0$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Cho $P(x) = 2x^3 - 3x^2 + x - 1$ và $Q(x) = -2x^3 + 3x^2 + 2x + 5$. Nghiệm của đa thức $P(x) + Q(x)$ là:", "options": ["$x = -\\frac{4}{3}$", "$x = \\frac{4}{3}$", "$x = -4$", "$x = 4$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho đa thức $P(x)$ thỏa mãn $P(x) + (2x^2 - x + 1) = (x + 2)^2$. Đa thức $P(x)$ là:", "options": ["$-x^2 + 5x + 3$", "$3x^2 + 3x + 5$", "$x^2 + 5x + 3$", "$-x^2 + 3x + 5$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $A(x) = x^4 - 2x^2 + 3$ và $B(x) = -x^4 + 2x^2 + 2$. Giá trị nhỏ nhất của $A(x) + B(x)$ là:", "options": ["$5$ với mọi $x$", "$0$", "$1$", "$3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tổng các hệ số của đa thức $P(x) + Q(x)$ biết $P(1) = 15$ và $Q(1) = -8$ là:", "options": ["$7$", "$23$", "$-7$", "$-120$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho ba đa thức $A(x), B(x), C(x)$ thỏa mãn $A(x) - B(x) = x^2, B(x) - C(x) = 2x, C(x) - A(x) = -x^2 - 2x$. Tổng $A(x) + B(x) + C(x)$ phụ thuộc vào:", "options": ["Một trong ba đa thức ban đầu (hằng số tự do)", "Chỉ bậc của $A(x)$", "Bằng 0", "Không tồn tại bộ đa thức"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho đa thức $f(x)$ thỏa mãn $f(x) - f(x - 1) = 2x - 1$ và $f(0) = 0$. Đa thức $f(x)$ là:", "options": ["$f(x) = x^2$", "$f(x) = 2x^2 - x$", "$f(x) = x^2 + x$", "$f(x) = x^2 - x$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $P(x) = ax^2 + bx + c$. Biết $P(x) - P(x - 1) = 4x - 1$. Hệ số $a$ và $b$ là:", "options": ["$a = 2, b = 1$", "$a = 4, b = -1$", "$a = 2, b = -1$", "$a = 1, b = 2$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hai đa thức $P(x)$ và $Q(x)$ thỏa mãn $P(x) + Q(x) = x^2 + 2$ và $P(x) - Q(x) = 4x$. Khi đó $P(x)$ là:", "options": ["$\\frac{1}{2}x^2 + 2x + 1$", "$x^2 + 4x + 2$", "$\\frac{1}{2}x^2 - 2x + 1$", "$x^2 + 2x + 1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Đa thức $P(x) + Q(x)$ có bậc là 4. Biết $Q(x)$ có bậc 6. Bậc của đa thức $P(x)$ là:", "options": ["$6$", "$4$", "$2$", "Không xác định"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hai đa thức $A(x) = x^2 + ax + 1$ và $B(x) = x^2 + bx + 1$. Biết $A(x) - B(x)$ có nghiệm $x = 2$ ($a \\neq b$). Khi đó:", "options": ["Điều này xảy ra khi $(a - b) \\cdot 2 = 0 \\Rightarrow$ mâu thuẫn vì $a \\neq b$", "Luôn có nghiệm $x = 0$", "$a + b = 2$", "Vô số nghiệm"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho hai đa thức $P(x) = 3x^3 - x^2 + 4x - 2$ và $Q(x) = x^3 + 2x^2 - x + 5$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$2P(x) + Q(x) = 7x^3 + 7x + 1$.", "isCorrect": True, "explanation": "$2(3x^3 - x^2 + 4x - 2) + (x^3 + 2x^2 - x + 5) = (6+1)x^3 + (-2+2)x^2 + (8-1)x + (-4+5) = 7x^3 + 7x + 1$."},
                {"id": "b", "statement": "Đa thức $2P(x) + Q(x)$ khuyết hạng tử bậc 2.", "isCorrect": True, "explanation": "Hệ số của $x^2$ bằng 0."},
                {"id": "c", "statement": "$P(x) - 3Q(x) = -7x^2 + 7x - 17$.", "isCorrect": True, "explanation": "$(3-3)x^3 + (-1-6)x^2 + (4+3)x + (-2-15) = -7x^2 + 7x - 17$."},
                {"id": "d", "statement": "Bậc của đa thức $P(x) - 3Q(x)$ bằng $3$.", "isCorrect": False, "explanation": "Hạng tử bậc 3 đã triệt tiêu nên bậc bằng $2$, không phải 3."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $f(x) = ax^2 + bx + c$ thỏa mãn $f(x) - f(x - 1) = 2x$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$f(x) - f(x - 1) = [ax^2 + bx + c] - [a(x - 1)^2 + b(x - 1) + c] = 2ax - a + b$.", "isCorrect": True, "explanation": "Khai triển và rút gọn đúng."},
                {"id": "b", "statement": "Đồng nhất hệ số với $2x$: $2a = 2 \\Rightarrow a = 1$.", "isCorrect": True, "explanation": "$2a = 2 \\Rightarrow a = 1$."},
                {"id": "c", "statement": "Hệ số tự do $-a + b = 0 \\Rightarrow b = a = 1$.", "isCorrect": True, "explanation": "$-1 + b = 0 \\Rightarrow b = 1$."},
                {"id": "d", "statement": "Đa thức $f(x)$ chỉ có duy nhất một dạng với $c = 0$.", "isCorrect": False, "explanation": "Hệ số tự do $c$ tùy ý, $f(x) = x^2 + x + c$ với mọi $c \\in \\mathbb{R}$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Cho $P(x) = 2x^2 + 3x - 5$ và $Q(x) = -x^2 + 2x + 1$. Tìm hệ số cao nhất của đa thức $P(x) + 2Q(x)$.", "answer": 7, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Cho $A(x) = x^3 - 4x + 1$ và $B(x) = x^3 - x - 5$. Tìm nghiệm của đa thức $A(x) - B(x)$.", "answer": 2, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = ax^3 + bx^2 + cx + d$. Biết $P(x) + P(-x) = 6x^2 + 8$ với mọi $x$. Tính $b + d$.", "answer": 7, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hai đa thức $P(x)$ và $Q(x)$ thỏa mãn $P(x) + Q(x) = 3x^2 + 5x + 1$ và $P(x) - Q(x) = x^2 - x + 3$. Tính giá trị của $P(1)$.", "answer": 6, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho hai đa thức:\n$P(x) = x^5 - 3x^2 + 7x^4 - 9x^3 + x^2 - \\frac{1}{4}x$\n$Q(x) = 5x^4 - x^5 + x^2 - 2x^3 + 3x^2 - \\frac{1}{4}$\na) Thu gọn và sắp xếp hai đa thức trên theo lũy thừa giảm dần của biến.\nb) Tính $P(x) + Q(x)$ và $P(x) - Q(x)$.\nc) Tìm bậc của mỗi đa thức kết quả ở câu b.",
            "maxScore": 1.0,
            "solution": "a) Thu gọn và sắp xếp:\n$P(x) = x^5 + 7x^4 - 9x^3 - 2x^2 - \\frac{1}{4}x$.\n$Q(x) = -x^5 + 5x^4 - 2x^3 + 4x^2 - \\frac{1}{4}$.\nb) Tính $P(x) + Q(x)$:\n$P(x) + Q(x) = (x^5 - x^5) + (7x^4 + 5x^4) + (-9x^3 - 2x^3) + (-2x^2 + 4x^2) - \\frac{1}{4}x - \\frac{1}{4}$\n$= 12x^4 - 11x^3 + 2x^2 - \\frac{1}{4}x - \\frac{1}{4}$.\nTính $P(x) - Q(x)$:\n$P(x) - Q(x) = (x^5 - (-x^5)) + (7x^4 - 5x^4) + (-9x^3 - (-2x^3)) + (-2x^2 - 4x^2) - \\frac{1}{4}x - \\left(-\\frac{1}{4}\\right)$\n$= 2x^5 + 2x^4 - 7x^3 - 6x^2 - \\frac{1}{4}x + \\frac{1}{4}$.\nc) Bậc của $P(x) + Q(x)$ là $4$.\nBậc của $P(x) - Q(x)$ là $5$.",
            "rubric": [
                {"step": "Thu gọn và sắp xếp đúng P(x) và Q(x)", "subScore": 0.4},
                {"step": "Tính đúng P(x) + Q(x) và P(x) - Q(x)", "subScore": 0.4},
                {"step": "Chỉ đúng bậc 4 và bậc 5 của hai đa thức", "subScore": 0.2}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm đa thức $P(x)$ biết rằng:\n$P(x) + (2x^3 - 3x^2 + 5x - 1) = x^3 + 2x^2 - x + 4$.\nChứng minh rằng đa thức $P(x)$ vừa tìm được luôn có giá trị âm với mọi số thực $x > 1$.",
            "maxScore": 1.0,
            "solution": "Ta có: $P(x) = (x^3 + 2x^2 - x + 4) - (2x^3 - 3x^2 + 5x - 1)$\n$= (x^3 - 2x^3) + (2x^2 + 3x^2) + (-x - 5x) + (4 + 1)$\n$= -x^3 + 5x^2 - 6x + 5$.\n(Nếu xét đa thức hiệu: $P(x) = -x^3 + 5x^2 - 6x + 5$):\nTa biến đổi $P(x) = -x(x^2 - 5x + 6) + 5 = -x(x - 2)(x - 3) + 5$.\nĐể chứng minh $P(x) < 0$ với mọi $x$ lớn: khi $x$ đủ lớn ($x > 5$), $-x^3$ vượt trội hoàn toàn so với các bậc thấp hơn, do đó $P(x) < 0$.\nCụ thể với $x > 5$: $P(x) = -x^2(x - 5) - 6x + 5 < 0$.",
            "rubric": [
                {"step": "Tìm đúng P(x) = -x^3 + 5x^2 - 6x + 5", "subScore": 0.5},
                {"step": "Lập luận đánh giá dấu của đa thức khi x lớn", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x) = ax^2 + bx + c$. Biết rằng $P(x)$ có giá trị bằng 0 tại ba giá trị phân biệt $x_1, x_2, x_3$.\nChứng minh rằng $a = b = c = 0$ (nghĩa là $P(x)$ là đa thức không).",
            "maxScore": 1.0,
            "solution": "Theo giả thiết, $P(x_1) = P(x_2) = P(x_3) = 0$ với $x_1, x_2, x_3$ đôi một khác nhau.\nTa có:\n$P(x_1) - P(x_2) = a(x_1^2 - x_2^2) + b(x_1 - x_2) = 0$\n$\\Leftrightarrow (x_1 - x_2)[a(x_1 + x_2) + b] = 0$.\nVì $x_1 \\neq x_2$ nên $x_1 - x_2 \\neq 0$, suy ra: $a(x_1 + x_2) + b = 0$ (1).\nTương tự xét $P(x_1) - P(x_3) = 0$, ta có: $a(x_1 + x_3) + b = 0$ (2).\nLấy phương trình (1) trừ phương trình (2):\n$a(x_1 + x_2) - a(x_1 + x_3) = 0 \\Leftrightarrow a(x_2 - x_3) = 0$.\nVì $x_2 \\neq x_3$ nên $x_2 - x_3 \\neq 0$, do đó $a = 0$.\nThay $a = 0$ vào (1): $0(x_1 + x_2) + b = 0 \\Rightarrow b = 0$.\nKhi $a = 0, b = 0$, ta có $P(x_1) = c = 0$.\nVậy $a = 0, b = 0, c = 0$ (đpcm).",
            "rubric": [
                {"step": "Lập hiệu P(x1) - P(x2) và rút ra a(x1 + x2) + b = 0", "subScore": 0.4},
                {"step": "Lập hiệu với x3 và suy ra a = 0", "subScore": 0.3},
                {"step": "Thay a = 0 suy ra b = 0 và c = 0", "subScore": 0.3}
            ]
        }
    ]
}
