# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI - BÀI 22: TÍNH CHẤT CƠ BẢN CỦA PHÂN THỨC ĐẠI SỐ (TOÁN 8 - KNTT)
Gồm 3 đề phân hóa:
- Đề 1 (Cơ bản): Tính chất cơ bản, quy tắc đổi dấu, rút gọn phân thức đơn giản, tìm mẫu thức chung cơ bản.
- Đề 2 (Khá): Rút gọn dùng hằng đẳng thức, quy đồng mẫu thức đa thức bậc hai, tính giá trị sau khi rút gọn.
- Đề 3 (Nâng cao): Rút gọn phân thức nhiều biến đối xứng, quy đồng hoán vị vòng quanh, ứng dụng đẳng thức a+b+c=0.
"""

BAI2_EXAMS = {}

# ==============================================================================
# BÀI 22 - ĐỀ 1: CƠ BẢN (🌱)
# ==============================================================================
BAI2_EXAMS["c6_8_bai2_test1"] = {
    "title": "Toán 8 (KNTT) - Bài 22: Tính chất cơ bản của phân thức đại số - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Tính chất cơ bản của phân thức đại số khẳng định rằng nếu nhân cả tử và mẫu của một phân thức với cùng một đa thức khác 0 thì:",
            "options": [
                "Được một phân thức bằng phân thức đã cho",
                "Được một phân thức đối của phân thức đã cho",
                "Được một phân thức nghịch đảo của phân thức đã cho",
                "Giá trị của phân thức tăng lên gấp đôi"
            ],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Theo quy tắc đổi dấu, phân thức $\\frac{A}{B}$ bằng phân thức nào sau đây?",
            "options": ["$\\frac{-A}{-B}$", "$\\frac{-A}{B}$", "$\\frac{A}{-B}$", "$-\\frac{-A}{-B}$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Nhận biết",
            "question": "Phân thức $\\frac{x - y}{y - x}$ rút gọn được kết quả là:",
            "options": ["$-1$", "$1$", "$0$", "$x - y$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Nhận biết",
            "question": "Rút gọn phân thức $\\frac{6x^2y}{9xy^2}$ ta được:",
            "options": ["$\\frac{2x}{3y}$", "$\\frac{3x}{2y}$", "$\\frac{2y}{3x}$", "$\\frac{2x^2}{3y^2}$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Nhận biết",
            "question": "Rút gọn phân thức $\\frac{2(x - 1)}{4(x - 1)}$ với $x \\neq 1$ ta được:",
            "options": ["$\\frac{1}{2}$", "$2$", "$\\frac{x - 1}{2}$", "$1$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Nhận biết",
            "question": "Mẫu thức chung đơn giản nhất của hai phân thức $\\frac{1}{2x}$ và $\\frac{1}{3x^2}$ là:",
            "options": ["$6x^2$", "$6x^3$", "$5x^2$", "$6x$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Nhận biết",
            "question": "Nhân tử phụ của mẫu thức $x - 2$ khi quy đồng về mẫu thức chung $(x - 2)(x + 2)$ là:",
            "options": ["$x + 2$", "$x - 2$", "$x^2 - 4$", "$1$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $\\frac{x^2 - 4}{x - 2}$ với $x \\neq 2$ ta được:",
            "options": ["$x + 2$", "$x - 2$", "$1$", "$x$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $\\frac{3x + 3}{x^2 - 1}$ với $x \\neq \\pm 1$ ta được:",
            "options": ["$\\frac{3}{x - 1}$", "$\\frac{3}{x + 1}$", "$\\frac{1}{x - 1}$", "$3(x - 1)$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Đa thức thích hợp điền vào dấu $?$ trong đẳng thức $\\frac{x - 2}{x + 1} = \\frac{?}{x^2 - 1}$ là:",
            "options": ["$(x - 2)(x - 1)$", "$(x - 2)(x + 1)$", "$x - 1$", "$x^2 - 4$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Mẫu thức chung của hai phân thức $\\frac{1}{x^2 - 4}$ và $\\frac{1}{x + 2}$ là:",
            "options": ["$x^2 - 4$", "$(x + 2)^2$", "$x - 2$", "$(x^2 - 4)(x + 2)$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Giá trị của phân thức $\\frac{x^2 - 25}{x - 5}$ tại $x = 15$ bằng:",
            "options": ["$20$", "$10$", "$25$", "$15$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho phân thức $P = \\frac{5x^2 - 10x}{x^2 - 4}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Tử thức có thể phân tích thành nhân tử là $5x(x - 2)$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Mẫu thức có thể phân tích thành nhân tử là $(x - 2)(x + 2)$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Sau khi rút gọn, phân thức $P$ trở thành $\\frac{5x}{x + 2}$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 2$, giá trị của phân thức $P$ bằng $2.5$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai phân thức $A = \\frac{1}{x - 3}$ và $B = \\frac{2}{3 - x}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Áp dụng quy tắc đổi dấu, ta có $\\frac{2}{3 - x} = \\frac{-2}{x - 3}$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Hai phân thức $A$ và $B$ có thể quy về cùng mẫu thức là $x - 3$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Tổng của hai phân thức $A + B$ bằng $\\frac{3}{x - 3}$.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Hiệu của hai phân thức $A - B$ bằng $\\frac{3}{x - 3}$.", "correct": True }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $\\frac{4x^2 - 1}{2x - 1}$ rồi tính giá trị của biểu thức tại $x = 5$.",
            "answer": "11"
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm hệ số bậc cao nhất của mẫu thức chung của hai phân thức $\\frac{1}{4x}$ và $\\frac{1}{6x^2}$.",
            "answer": "12"
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Cho phân thức $\\frac{x^2 - 9}{x + 3}$. Khi $x = 10$, giá trị của phân thức bằng bao nhiêu?",
            "answer": "7"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Rút gọn phân thức $\\frac{x^3 - 8}{x^2 + 2x + 4}$ rồi tính giá trị tại $x = 12$.",
            "answer": "10"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Rút gọn các phân thức sau:\na) $A = \\frac{12x^3y^2}{18x^2y^4}$.\nb) $B = \\frac{x^2 - 6x + 9}{x^2 - 9}$.",
            "rubric": "a) Chia cả tử và mẫu cho 6x^2y^2: A = (12x^3y^2 : 6x^2y^2) / (18x^2y^4 : 6x^2y^2) = 2x / (3y^2) (0.5đ).\nb) Phân tích tử và mẫu: B = (x - 3)^2 / [(x - 3)(x + 3)] (0.25đ).\nRút gọn bằng cách chia cả tử và mẫu cho (x - 3): B = (x - 3) / (x + 3) (0.25đ)."
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Quy đồng mẫu thức các phân thức sau:\na) $\\frac{3}{x^2 - 1}$ và $\\frac{1}{x + 1}$.\nb) $\\frac{x}{2x - 4}$ và $\\frac{1}{x^2 - 4}$.",
            "rubric": "a) Phân tích mẫu: x^2 - 1 = (x - 1)(x + 1). MTC = (x - 1)(x + 1) (0.15đ).\nNhân tử phụ của phân thức thứ hai là (x - 1) (0.15đ).\nQuy đồng: 3 / [(x - 1)(x + 1)] và (x - 1) / [(x - 1)(x + 1)] (0.2đ).\nb) Phân tích: 2x - 4 = 2(x - 2); x^2 - 4 = (x - 2)(x + 2). MTC = 2(x - 2)(x + 2) (0.2đ).\nNhân tử phụ lần lượt là: (x + 2) và 2 (0.15đ).\nQuy đồng: [x(x + 2)] / [2(x - 2)(x + 2)] và 2 / [2(x - 2)(x + 2)] (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $P = \\frac{x^2 + 2x + 1}{x^3 + 1}$.\na) Tìm điều kiện xác định của $P$.\nb) Rút gọn phân thức $P$.\nc) Tính giá trị của $P$ khi $x = 2$.",
            "rubric": "a) ĐKXĐ: x^3 + 1 ≠ 0 <=> (x + 1)(x^2 - x + 1) ≠ 0 <=> x ≠ -1 (vì x^2 - x + 1 = (x - 1/2)^2 + 3/4 > 0 với mọi x) (0.35đ).\nb) Tử thức: x^2 + 2x + 1 = (x + 1)^2 (0.15đ).\nMẫu thức: x^3 + 1 = (x + 1)(x^2 - x + 1) (0.15đ).\nRút gọn: P = (x + 1) / (x^2 - x + 1) (0.2đ).\nc) Tại x = 2 (thỏa mãn ĐKXĐ): P = (2 + 1) / (2^2 - 2 + 1) = 3 / 3 = 1 (0.15đ)."
        }
    ]
}

# ==============================================================================
# BÀI 22 - ĐỀ 2: KHÁ (🌿)
# ==============================================================================
BAI2_EXAMS["c6_8_bai2_test2"] = {
    "title": "Toán 8 (KNTT) - Bài 22: Tính chất cơ bản của phân thức đại số - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Phân thức đối của phân thức $\\frac{x - 3}{x + 2}$ là:",
            "options": ["$\\frac{3 - x}{x + 2}$", "$\\frac{x - 3}{x - 2}$", "$\\frac{x + 3}{x + 2}$", "$\\frac{3 - x}{-x - 2}$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $\\frac{x^3 - 3x^2 + 3x - 1}{x^2 - 2x + 1}$ với $x \\neq 1$ ta được:",
            "options": ["$x - 1$", "$x + 1$", "$(x - 1)^2$", "$1$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Mẫu thức chung đơn giản nhất của ba phân thức $\\frac{1}{x^2 - 2x}$, $\\frac{1}{x^2 - 4}$, $\\frac{1}{x^2 + 2x}$ là:",
            "options": ["$x(x - 2)(x + 2)$", "$x^2(x^2 - 4)$", "$(x^2 - 4)^2$", "$x(x - 2)^2$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $\\frac{x^2 - y^2}{(x - y)^2}$ với $x \\neq y$ ta được:",
            "options": ["$\\frac{x + y}{x - y}$", "$\\frac{x - y}{x + y}$", "$1$", "$\\frac{x + y}{(x - y)^2}$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Thông hiểu",
            "question": "Tìm đa thức $M$ thỏa mãn $\\frac{x^2 - 5x + 6}{x - 2} = M$ với $x \\neq 2$:",
            "options": ["$x - 3$", "$x + 3$", "$x - 2$", "$x + 2$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $P = \\frac{2x^2 + 5x - 3}{x^2 - 9}$ với $x \\neq \\pm 3$ ta được:",
            "options": ["$\\frac{2x - 1}{x - 3}$", "$\\frac{2x + 1}{x + 3}$", "$\\frac{2x - 1}{x + 3}$", "$\\frac{x - 1}{x - 3}$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Thông hiểu",
            "question": "Giá trị của phân thức $\\frac{x^3 + 8}{x^2 - 2x + 4}$ tại $x = 98$ bằng:",
            "options": ["$100$", "$96$", "$102$", "$98$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng thấp",
            "question": "Cho $\\frac{x^2 - 16}{x^2 - 8x + 16} = \\frac{x + 4}{A}$. Đa thức $A$ là:",
            "options": ["$x - 4$", "$x + 4$", "$(x - 4)^2$", "$4 - x$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng thấp",
            "question": "Rút gọn phân thức $\\frac{x^3 - x^2y - xy^2 + y^3}{x^2 - y^2}$ với $x \\neq \\pm y$ ta được:",
            "options": ["$x - y$", "$x + y$", "$(x - y)^2$", "$1$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng thấp",
            "question": "Quy đồng mẫu thức hai phân thức $\\frac{1}{x^2 - 3x + 2}$ và $\\frac{1}{x^2 - 4x + 3}$. Mẫu thức chung là:",
            "options": ["$(x - 1)(x - 2)(x - 3)$", "$(x - 1)^2(x - 2)$", "$(x - 2)(x - 3)$", "$x^2 - 5x + 6$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng thấp",
            "question": "Biết phân thức $\\frac{x^2 + ax + 6}{x - 2}$ rút gọn được thành đa thức bậc nhất. Giá trị của $a$ là:",
            "options": ["$-5$", "$5$", "$-7$", "$7$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng thấp",
            "question": "Cho $x + y = 5$ và $xy = 6$. Giá trị của phân thức $\\frac{x^2 + y^2}{x^3 + y^3}$ bằng:",
            "options": ["$\\frac{13}{35}$", "$\\frac{13}{65}$", "$\\frac{1}{5}$", "$\\frac{19}{35}$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho phân thức $A = \\frac{x^3 - 4x}{x^3 + 2x^2 - 4x - 8}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Tử thức có thể phân tích thành $x(x - 2)(x + 2)$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Mẫu thức có thể phân tích thành $(x - 2)(x + 2)^2$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Sau khi rút gọn, phân thức $A = \\frac{x}{x + 2}$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = -2$, giá trị của phân thức $A$ bằng $0$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai phân thức $P = \\frac{x + 1}{x^2 - 4}$ và $Q = \\frac{x - 1}{2 - x}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Đổi dấu phân thức $Q$ ta được $Q = \\frac{1 - x}{x - 2}$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Mẫu thức chung đơn giản nhất của $P$ và $Q$ là $x^2 - 4$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Nhân tử phụ của phân thức $Q$ khi quy đồng về mẫu $x^2 - 4$ là $x + 2$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tổng $P + Q$ sau khi quy đồng có tử thức là $x^2 + 2x + 3$.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $\\frac{x^2 - 25}{x^2 - 10x + 25}$ rồi tính giá trị tại $x = 15$.",
            "answer": "2"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Rút gọn phân thức $P = \\frac{x^3 - 27}{x - 3}$ rồi tính giá trị của $P$ tại $x = 7$.",
            "answer": "67"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tìm giá trị của $m$ để phân thức $\\frac{x^2 - 4x + m}{x - 3}$ rút gọn được.",
            "answer": "3"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $\\frac{x^4 - 16}{x^2 + 4}$. Tính giá trị của biểu thức tại $x = 6$.",
            "answer": "32"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Rút gọn các phân thức sau:\na) $P = \\frac{2x^2 + 4x}{x^3 + 8}$.\nb) $Q = \\frac{x^2 - 2xy + y^2 - z^2}{x - y + z}$.",
            "rubric": "a) Tử: 2x(x + 2). Mẫu: (x + 2)(x^2 - 2x + 4) (0.25đ).\nRút gọn: P = 2x / (x^2 - 2x + 4) (0.25đ).\nb) Tử: (x - y)^2 - z^2 = (x - y - z)(x - y + z) (0.25đ).\nRút gọn: Q = x - y - z (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Quy đồng mẫu thức ba phân thức sau:\n$\\frac{1}{x^2 + 2x + 1}$, $\\frac{2}{x^2 - 1}$, $\\frac{3}{1 - x}$.",
            "rubric": "- Đổi dấu phân thức thứ ba: 3 / (1 - x) = -3 / (x - 1) (0.2đ).\n- Phân tích các mẫu thức thành nhân tử:\n+ x^2 + 2x + 1 = (x + 1)^2 (0.15đ).\n+ x^2 - 1 = (x - 1)(x + 1) (0.15đ).\n+ x - 1 = x - 1.\n- MTC = (x - 1)(x + 1)^2 (0.2đ).\n- Nhân tử phụ lần lượt là: (x - 1), (x + 1), -(x + 1)^2 (0.15đ).\n- Quy đồng được:\n+ (x - 1) / [(x - 1)(x + 1)^2]\n+ 2(x + 1) / [(x - 1)(x + 1)^2]\n+ -3(x + 1)^2 / [(x - 1)(x + 1)^2] (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $A = \\frac{x^4 - 1}{x^3 + x^2 + x + 1}$.\na) Tìm điều kiện xác định của $A$.\nb) Rút gọn phân thức $A$.\nc) Tìm giá trị của $x$ để $A = 5$.",
            "rubric": "a) Mẫu thức: x^3 + x^2 + x + 1 = x^2(x + 1) + (x + 1) = (x + 1)(x^2 + 1).\nVì x^2 + 1 > 0 nên mẫu khác 0 <=> x + 1 ≠ 0 <=> x ≠ -1 (0.35đ).\nb) Tử: x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1) (0.2đ).\nRút gọn: A = x - 1 (0.2đ).\nc) Cho A = 5 <=> x - 1 = 5 <=> x = 6 (thỏa mãn ĐKXĐ). Vậy x = 6 (0.25đ)."
        }
    ]
}

# ==============================================================================
# BÀI 22 - ĐỀ 3: NÂNG CAO (🚀)
# ==============================================================================
BAI2_EXAMS["c6_8_bai2_test3"] = {
    "title": "Toán 8 (KNTT) - Bài 22: Tính chất cơ bản của phân thức đại số - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $a + b + c = 0$. Rút gọn phân thức $\\frac{a^3 + b^3 + c^3}{3abc}$ với $abc \\neq 0$ ta được kết quả là:",
            "options": ["$1$", "$3$", "$-1$", "$0$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $M = \\frac{(x - y)^3 + (y - z)^3 + (z - x)^3}{(x - y)(y - z)(z - x)}$ ta được:",
            "options": ["$3$", "$1$", "$-3$", "$0$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Rút gọn phân thức $P = \\frac{x^4 + 4}{x^2 + 2x + 2}$ ta được:",
            "options": ["$x^2 - 2x + 2$", "$x^2 + 2$", "$x^2 - 2$", "$x^2 + 2x - 2$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Rút gọn phân thức $\\frac{x^8 + x^4 + 1}{x^4 + x^2 + 1}$ ta được:",
            "options": ["$x^4 - x^2 + 1$", "$x^4 + 1$", "$x^2 - x + 1$", "$x^4 + x^2 - 1$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Vận dụng thấp",
            "question": "Cho $x, y, z$ đôi một khác nhau. Mẫu thức chung gọn nhất của các phân thức $\\frac{1}{(x - y)(y - z)}$, $\\frac{1}{(y - z)(z - x)}$, $\\frac{1}{(z - x)(x - y)}$ là:",
            "options": [
                "$(x - y)(y - z)(z - x)$",
                "$(x - y)^2(y - z)^2(z - x)^2$",
                "$(x - y)(y - z)(x - z)$",
                "$-(x - y)(y - z)(z - x)$"
            ],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng cao",
            "question": "Cho $x + \\frac{1}{x} = 3$. Giá trị của phân thức $\\frac{x^4 + 1}{x^2}$ bằng:",
            "options": ["$7$", "$9$", "$11$", "$6$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng cao",
            "question": "Rút gọn phân thức $A = \\frac{x^2 + y^2 + z^2 - 2xy + 2xz - 2yz}{x - y + z}$ ta được:",
            "options": ["$x - y + z$", "$x + y + z$", "$x - y - z$", "$1$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực $a, b, c$ khác nhau đôi một thỏa mãn $ab + bc + ca = 1$. Giá trị của phân thức $\\frac{(a + b)^2(b + c)^2(c + a)^2}{(a^2 + 1)(b^2 + 1)(c^2 + 1)}$ bằng:",
            "options": ["$1$", "$2$", "$4$", "$\\frac{1}{2}$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng cao",
            "question": "Cho phân thức $P = \\frac{n^3 + 2n^2 - 1}{n^3 + 2n^2 + 2n + 1}$. Phân thức $P$ sau khi rút gọn tối giản có dạng:",
            "options": ["$\\frac{n^2 + n - 1}{n^2 + n + 1}$", "$\\frac{n - 1}{n + 1}$", "$\\frac{n^2 - 1}{n^2 + 1}$", "$\\frac{n + 1}{n^2 + 1}$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng cao",
            "question": "Tìm số tự nhiên $n$ để phân thức $\\frac{2n + 3}{n + 1}$ là một phân số tối giản:",
            "options": ["Với mọi số tự nhiên $n$", "Chỉ khi $n$ là số chẵn", "Chỉ khi $n$ là số lẻ", "Không có số $n$ nào"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng cao",
            "question": "Cho $x, y$ thỏa mãn $x^2 + y^2 = 25$ và $xy = 12$ ($x > y > 0$). Giá trị của phân thức $\\frac{x - y}{x + y}$ bằng:",
            "options": ["$\\frac{1}{7}$", "$\\frac{2}{7}$", "$\\frac{1}{5}$", "$\\frac{3}{7}$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng cao",
            "question": "Rút gọn phân thức $S = \\frac{1}{1 \\cdot 2} + \\frac{1}{2 \\cdot 3} + \\dots + \\frac{1}{n(n + 1)}$ dưới dạng một phân thức đại số theo $n$:",
            "options": ["$\\frac{n}{n + 1}$", "$\\frac{1}{n + 1}$", "$\\frac{n + 1}{n}$", "$\\frac{n - 1}{n}$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho ba số thực $a, b, c$ đôi một khác nhau và phân thức $E = \\frac{a}{(a - b)(a - c)} + \\frac{b}{(b - c)(b - a)} + \\frac{c}{(c - a)(c - b)}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Mẫu thức chung gọn nhất của ba phân thức là $(a - b)(b - c)(c - a)$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Khi quy đồng, phân thức thứ nhất có nhân tử phụ là $-(b - c)$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Tử thức sau khi quy đồng bằng $-[a(b - c) + b(c - a) + c(a - b)] = 0$.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Giá trị của biểu thức $E$ phụ thuộc vào các giá trị cụ thể của $a, b, c$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho phân thức $P = \\frac{x^4 + x^3 + x + 1}{x^4 - x^3 + 2x^2 - x + 1}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Tử thức phân tích thành $(x + 1)(x^3 + 1) = (x + 1)^2(x^2 - x + 1)$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Mẫu thức phân tích thành $(x^2 + 1)(x^2 - x + 1)$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Rút gọn phân thức ta được $P = \\frac{(x + 1)^2}{x^2 + 1}$.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Giá trị nhỏ nhất của $P$ bằng $0$ khi $x = -1$.", "correct": True }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho $x + \\frac{1}{x} = 4$. Tính giá trị của phân thức $\\frac{x^3 + \\frac{1}{x^3}}{x^2 + \\frac{1}{x^2} - 1}$.",
            "answer": "4"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Rút gọn phân thức $\\frac{x^5 + x + 1}{x^2 + x + 1}$ rồi tính giá trị của biểu thức tại $x = 3$.",
            "answer": "19"
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $a, b, c$ thỏa mãn $a + b + c = 0$ và $a^2 + b^2 + c^2 = 14$. Tính giá trị của phân thức $\\frac{a^4 + b^4 + c^4}{49}$.",
            "answer": "2"
        },
        {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tính giá trị của phân thức $P = \\frac{(10^4 + 324)(22^4 + 324)(34^4 + 324)}{(4^4 + 324)(16^4 + 324)(28^4 + 324)}$.",
            "answer": "373"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Rút gọn phân thức đại số sau:\n$A = \\frac{x^4 + 2025x^2 + 2024x + 2025}{x^2 + x + 1}$.",
            "rubric": "- Tách tử thức: x^4 + 2025x^2 + 2024x + 2025 = x^4 + x^2 + 1 + 2024x^2 + 2024x + 2024 (0.3đ).\n- Ta có: x^4 + x^2 + 1 = (x^2 + 1)^2 - x^2 = (x^2 - x + 1)(x^2 + x + 1) (0.25đ).\n- Và 2024(x^2 + x + 1) (0.15đ).\n- Do đó Tử = (x^2 + x + 1)[x^2 - x + 1 + 2024] = (x^2 + x + 1)(x^2 - x + 2025) (0.15đ).\n- Rút gọn: A = x^2 - x + 2025 (0.15đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực $a, b, c$ khác 0 thỏa mãn $a + b + c = 0$.\nChứng minh rằng phân thức sau không phụ thuộc vào giá trị của $a, b, c$:\n$M = \\frac{a^2}{bc} + \\frac{b^2}{ca} + \\frac{c^2}{ab}$.",
            "rubric": "- Quy đồng mẫu thức ba phân thức với MTC = abc:\nM = (a^3 + b^3 + c^3) / abc (0.3đ).\n- Ta có hằng đẳng thức:\na^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca) (0.35đ).\n- Vì a + b + c = 0 nên a^3 + b^3 + c^3 - 3abc = 0 <=> a^3 + b^3 + c^3 = 3abc (0.2đ).\n- Thay vào M: M = 3abc / abc = 3.\nVậy M = 3 luôn là hằng số, không phụ thuộc vào a, b, c (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho phân thức $P = \\frac{x^2 - yz}{(x + y)(x + z)} + \\frac{y^2 - zx}{(y + z)(y + x)} + \\frac{z^2 - xy}{(z + x)(z + y)}$.\na) Tìm mẫu thức chung của ba phân thức.\nb) Rút gọn biểu thức $P$.",
            "rubric": "a) MTC = (x + y)(y + z)(z + x) (0.25đ).\nb) Quy đồng từng phân thức:\n- Phân thức 1: [(x^2 - yz)(y + z)] / MTC = (x^2y + x^2z - y^2z - yz^2) / MTC (0.2đ).\n- Phân thức 2: [(y^2 - zx)(z + x)] / MTC = (y^2z + y^2x - z^2x - zx^2) / MTC (0.2đ).\n- Phân thức 3: [(z^2 - xy)(x + y)] / MTC = (z^2x + z^2y - x^2y - xy^2) / MTC (0.2đ).\n- Cộng các tử thức lại:\nTử = (x^2y - x^2y) + (x^2z - zx^2) + (-y^2z + y^2z) + (-yz^2 + z^2y) + (y^2x - xy^2) + (-z^2x + z^2x) = 0 (0.1đ).\nVậy P = 0 / MTC = 0 (0.05đ)."
        }
    ]
}
