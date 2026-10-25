# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI - BÀI 24: PHÉP NHÂN VÀ PHÉP CHIA PHÂN THỨC ĐẠI SỐ (TOÁN 8 - KNTT)
Gồm 3 đề phân hóa:
- Đề 1 (Cơ bản): Quy tắc nhân, chia phân thức, phân thức nghịch đảo, rút gọn tích/thương đơn giản.
- Đề 2 (Khá): Nhân chia kết hợp hằng đẳng thức, biểu thức hữu tỉ phối hợp các phép tính, tìm x thỏa mãn điều kiện.
- Đề 3 (Nâng cao): Biểu thức hữu tỉ phức tạp, tích dãy số quy luật, bài toán cực trị và giá trị nguyên.
"""

BAI4_EXAMS = {}

# ==============================================================================
# BÀI 24 - ĐỀ 1: CƠ BẢN (🌱)
# ==============================================================================
BAI4_EXAMS["c6_8_bai4_test1"] = {
    "title": "Toán 8 (KNTT) - Bài 24: Phép nhân và phép chia phân thức đại số - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Kết quả của phép nhân hai phân thức $\\frac{A}{B} \\cdot \\frac{C}{D}$ ($B \\neq 0, D \\neq 0$) là:",
            "options": ["$\\frac{A \\cdot C}{B \\cdot D}$", "$\\frac{A \\cdot D}{B \\cdot C}$", "$\\frac{A + C}{B + D}$", "$\\frac{A \\cdot B}{C \\cdot D}$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Phân thức nghịch đảo của phân thức $\\frac{x - 2}{x + 3}$ ($x \\neq 2, x \\neq -3$) là:",
            "options": ["$\\frac{x + 3}{x - 2}$", "$\\frac{2 - x}{x + 3}$", "$-\\frac{x - 2}{x + 3}$", "$\\frac{x - 3}{x + 2}$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Nhận biết",
            "question": "Muốn chia phân thức $\\frac{A}{B}$ cho phân thức $\\frac{C}{D}$ khác 0, ta làm như sau:",
            "options": [
                "Nhân phân thức $\\frac{A}{B}$ với phân thức nghịch đảo của $\\frac{C}{D}$",
                "Chia tử thức $A$ cho $C$ và chia mẫu thức $B$ cho $D$",
                "Nhân tử thức $A$ với $C$ và mẫu thức $B$ với $D$",
                "Cộng hai phân thức lại với nhau"
            ],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Nhận biết",
            "question": "Thực hiện phép nhân $\\frac{2x}{y} \\cdot \\frac{3y^2}{4x^2}$ ta được kết quả là:",
            "options": ["$\\frac{3y}{2x}$", "$\\frac{3x}{2y}$", "$\\frac{6y}{4x}$", "$\\frac{3y^2}{2x^2}$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Nhận biết",
            "question": "Kết quả của phép chia $\\frac{x}{2} : \\frac{x}{4}$ với $x \\neq 0$ là:",
            "options": ["$2$", "$\\frac{1}{2}$", "$\\frac{x^2}{8}$", "$4$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Nhận biết",
            "question": "Phân thức nào sau đây KHÔNG CÓ phân thức nghịch đảo?",
            "options": ["$0$", "$1$", "$x - 1$", "$\\frac{1}{x}$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{x - 1}{x + 2} \\cdot \\frac{x + 2}{x - 1}$ với $x \\neq 1, x \\neq -2$ ta được:",
            "options": ["$1$", "$0$", "$-1$", "$\\frac{(x - 1)^2}{(x + 2)^2}$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Thông hiểu",
            "question": "Rút gọn tích $\\frac{x^2 - 4}{x} \\cdot \\frac{2x}{x + 2}$ với $x \\neq 0, x \\neq -2$ ta được:",
            "options": ["$2(x - 2)$", "$x - 2$", "$2(x + 2)$", "$\\frac{2(x - 2)}{x}$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{x^2 - 1}{3x} : \\frac{x + 1}{6x^2}$ với $x \\neq 0, x \\neq -1$ ta được:",
            "options": ["$2x(x - 1)$", "$2(x - 1)$", "$\\frac{x - 1}{2x}$", "$\\frac{2x}{x - 1}$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Giá trị của biểu thức $P = \\frac{x + 3}{x - 1} \\cdot \\frac{x - 1}{2x + 6}$ tại $x = 100$ là:",
            "options": ["$\\frac{1}{2}$", "$1$", "$2$", "$\\frac{1}{4}$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Thương của phép chia $\\frac{4x^2}{y^3} : \\frac{2x}{y}$ bằng:",
            "options": ["$\\frac{2x}{y^2}$", "$\\frac{2x^2}{y^2}$", "$\\frac{2}{y^2}$", "$\\frac{x}{2y^2}$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Tính $\\left(\\frac{x}{y}\\right)^2 : \\frac{x^2}{y}$ với $x \\neq 0, y \\neq 0$ ta được:",
            "options": ["$\\frac{1}{y}$", "$y$", "$\\frac{x}{y}$", "$1$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai phân thức $A = \\frac{x^2 - 9}{2x + 4}$ và $B = \\frac{x + 2}{x - 3}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Phân thức nghịch đảo của $B$ là $\\frac{x - 3}{x + 2}$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Tích $A \\cdot B = \\frac{x + 3}{2}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Thương $A : B = \\frac{(x + 3)(x - 3)^2}{2(x + 2)^2}$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 5$, giá trị của tích $A \\cdot B$ bằng $3$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho biểu thức $P = \\left(\\frac{x + 1}{x - 1}\\right) : \\left(\\frac{x^2 + x}{x^2 - 1}\\right)$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của biểu thức là $x \\neq 0, x \\neq 1, x \\neq -1$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Ta có $\\frac{x^2 + x}{x^2 - 1} = \\frac{x(x + 1)}{(x - 1)(x + 1)} = \\frac{x}{x - 1}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Biểu thức rút gọn của $P$ là $P = \\frac{x + 1}{x}$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 2$, giá trị của $P$ bằng $1.2$.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của tích $\\frac{x^2 - 16}{x + 3} \\cdot \\frac{2x + 6}{x - 4}$ tại $x = 6$.",
            "answer": "20"
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{3x^2}{5y} : \\frac{6x}{10y^2}$ rồi tính giá trị khi $x = 2, y = 3$.",
            "answer": "6"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tìm $x$ để biểu thức $\\frac{2x - 4}{x + 1} \\cdot \\frac{x + 1}{x - 2}$ có giá trị bằng 2.",
            "answer": "Vô số"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Rút gọn biểu thức $M = \\left(\\frac{x}{x - 2}\\right) : \\left(\\frac{x^2}{x^2 - 4}\\right)$ rồi tính giá trị tại $x = 4$.",
            "answer": "1.5"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện các phép tính sau:\na) $A = \\frac{x^2 - 25}{x^2 + 2x} \\cdot \\frac{x + 2}{x - 5}$.\nb) $B = \\frac{x^2 - 4x + 4}{2x + 6} : \\frac{x - 2}{x + 3}$.",
            "rubric": "a) Tử 1: (x - 5)(x + 5); Mẫu 1: x(x + 2) (0.2đ).\nA = [(x - 5)(x + 5)(x + 2)] / [x(x + 2)(x - 5)] = (x + 5) / x (0.3đ).\nb) Phép chia bằng nhân nghịch đảo:\nB = [(x - 2)^2 / 2(x + 3)] * [(x + 3) / (x - 2)] (0.25đ).\nRút gọn: B = (x - 2) / 2 (0.25đ)."
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\left(\\frac{1}{x - 1} - \\frac{1}{x + 1}\\right) : \\frac{2}{x^2 - 1}$.\na) Tìm điều kiện xác định của biểu thức $P$.\nb) Rút gọn biểu thức $P$.\nc) Nhận xét về giá trị của $P$ khi $x$ thay đổi.",
            "rubric": "a) ĐKXĐ: x - 1 ≠ 0, x + 1 ≠ 0, x^2 - 1 ≠ 0 <=> x ≠ 1 và x ≠ -1 (0.25đ).\nb) Quy đồng trong ngoặc:\n1/(x - 1) - 1/(x + 1) = [(x + 1) - (x - 1)] / (x^2 - 1) = 2 / (x^2 - 1) (0.35đ).\nThực hiện phép chia: P = [2 / (x^2 - 1)] : [2 / (x^2 - 1)] = 1 (0.25đ).\nc) Với mọi x thỏa mãn ĐKXĐ (x ≠ ±1), biểu thức P luôn nhận giá trị không đổi bằng 1 (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một tấm tôn hình chữ nhật có diện tích là $\\frac{x^2 - 9}{x}\\text{ m}^2$ và chiều rộng là $\\frac{x - 3}{2x}\\text{ m}$ ($x > 3$).\na) Hãy viết phân thức biểu thị chiều dài của tấm tôn.\nb) Tính chiều dài tấm tôn khi $x = 5\\text{ m}$.",
            "rubric": "a) Chiều dài = Diện tích : Chiều rộng (0.2đ).\nChiều dài = [(x^2 - 9) / x] : [(x - 3) / (2x)]\n= [(x - 3)(x + 3) / x] * [2x / (x - 3)] (0.35đ).\nRút gọn: Chiều dài = 2(x + 3) (m) (0.25đ).\nb) Khi x = 5 m:\nChiều dài = 2(5 + 3) = 16 (m) (0.2đ)."
        }
    ]
}

# ==============================================================================
# BÀI 24 - ĐỀ 2: KHÁ (🌿)
# ==============================================================================
BAI4_EXAMS["c6_8_bai4_test2"] = {
    "title": "Toán 8 (KNTT) - Bài 24: Phép nhân và phép chia phân thức đại số - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $A = \\frac{x^3 - 8}{x^2 + x} \\cdot \\frac{x + 1}{x^2 + 2x + 4}$ với $x \\neq 0, x \\neq -1$ ta được:",
            "options": ["$\\frac{x - 2}{x}$", "$\\frac{x + 2}{x}$", "$\\frac{x - 2}{x + 1}$", "$\\frac{1}{x}$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{x^2 - 4y^2}{x^2 - y^2} : \\frac{x - 2y}{x - y}$ ta được kết quả là:",
            "options": ["$\\frac{x + 2y}{x + y}$", "$\\frac{x - 2y}{x + y}$", "$\\frac{x + 2y}{x - y}$", "$1$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\left(\\frac{x}{x + 1} + 1\\right) : \\left(1 - \\frac{3x^2}{1 - x^2}\\right)$. Điều kiện xác định của $P$ là:",
            "options": ["$x \\neq \\pm 1$ và $x \\neq \\pm \\frac{1}{2}$", "$x \\neq \\pm 1$", "$x \\neq 0$ và $x \\neq 1$", "$x \\neq -1$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $\\frac{x^2 - 1}{x^2 + 2x + 1} : \\frac{x - 1}{x + 1}$ với $x \\neq \\pm 1$ ta được:",
            "options": ["$1$", "$\\frac{x - 1}{x + 1}$", "$-1$", "$\\frac{1}{(x + 1)^2}$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Thông hiểu",
            "question": "Tìm biểu thức $Q$ biết rằng $\\frac{x - 1}{x + 2} \\cdot Q = \\frac{x^2 - 1}{x^2 - 4}$:",
            "options": ["$\\frac{x + 1}{x - 2}$", "$\\frac{x - 1}{x - 2}$", "$\\frac{x + 1}{x + 2}$", "$\\frac{x - 1}{x + 2}$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng thấp",
            "question": "Cho $M = \\left(\\frac{x + 2}{x - 2} - \\frac{x - 2}{x + 2}\\right) : \\frac{8}{x^2 - 4}$. Giá trị của $M$ là:",
            "options": ["$x$", "$2x$", "$\\frac{x}{2}$", "$1$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $A = \\left(\\frac{x - 1}{x}\\right)^2 : \\frac{x^2 - 1}{x^2 + x}$. Sau khi rút gọn, giá trị của $A$ tại $x = 5$ là:",
            "options": ["$\\frac{4}{5}$", "$\\frac{5}{4}$", "$1$", "$\\frac{6}{5}$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng thấp",
            "question": "Tìm $x$ để biểu thức $B = \\frac{x^2 - 9}{x + 1} : \\frac{x - 3}{x + 1}$ có giá trị bằng 7:",
            "options": ["$x = 4$", "$x = 3$", "$x = -4$", "$x = 10$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng thấp",
            "question": "Tính tích $P = \\left(1 - \\frac{1}{2}\\right)\\left(1 - \\frac{1}{3}\\right)\\left(1 - \\frac{1}{4}\\right) \\dots \\left(1 - \\frac{1}{n}\\right)$ dưới dạng phân thức:",
            "options": ["$\\frac{1}{n}$", "$\\frac{2}{n}$", "$\\frac{n - 1}{n}$", "$\\frac{1}{n(n - 1)}$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng thấp",
            "question": "Rút gọn biểu thức $C = \\frac{x^2 - 4x + 4}{x^2 - 1} \\cdot \\frac{x + 1}{x - 2}$ ta được:",
            "options": ["$\\frac{x - 2}{x - 1}$", "$\\frac{x - 2}{x + 1}$", "$\\frac{x + 2}{x - 1}$", "$1$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng thấp",
            "question": "Tìm giá trị nguyên của $x$ để biểu thức $D = \\frac{2x + 4}{x - 1} : \\frac{x + 2}{x - 1}$ nhận giá trị nguyên:",
            "options": ["Với mọi số nguyên $x \\neq 1, x \\neq -2$", "$x = 0$", "$x = 2$", "Không có $x$ nào"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng thấp",
            "question": "Một khối rubik hình lập phương có thể tích là $V = \\frac{x^3 + 3x^2 + 3x + 1}{8}\\text{ cm}^3$. Cạnh của khối rubik đó là:",
            "options": ["$\\frac{x + 1}{2}\\text{ cm}$", "$\\frac{x + 1}{4}\\text{ cm}$", "$\\frac{(x + 1)^2}{4}\\text{ cm}$", "$(x + 1)\\text{ cm}$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A = \\left(\\frac{x}{x^2 - 4} + \\frac{1}{x + 2}\\right) : \\frac{2x - 2}{x^2 - 2x}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của biểu thức là $x \\neq 0, x \\neq 2, x \\neq -2, x \\neq 1$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Biểu thức trong ngoặc quy đồng được là $\\frac{2x - 2}{x^2 - 4}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Biểu thức $A$ sau khi rút gọn tối giản là $A = \\frac{x}{x + 2}$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 4$, giá trị của biểu thức $A$ bằng $1$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho biểu thức hữu tỉ $B = \\left(\\frac{x^2}{y^2} - \\frac{y^2}{x^2}\\right) : \\left(\\frac{x}{y} + \\frac{y}{x}\\right)$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Ta có $\\frac{x^2}{y^2} - \\frac{y^2}{x^2} = \\left(\\frac{x}{y} - \\frac{y}{x}\\right)\\left(\\frac{x}{y} + \\frac{y}{x}\\right)$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Kết quả rút gọn của biểu thức $B$ là $\\frac{x}{y} - \\frac{y}{x}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Viết $B$ dưới dạng một phân thức đại số là $B = \\frac{x^2 - y^2}{xy}$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Nếu $x = y$ thì biểu thức $B$ nhận giá trị bằng 1.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $P = \\left(\\frac{x^2 - 9}{x^2 + 9}\\right) : \\left(\\frac{x - 3}{x^2 + 9}\\right)$ tại $x = 17$.",
            "answer": "20"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $A = \\left(\\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1}\\right) \\cdot \\frac{x^2 - 1}{4x}$. Tính giá trị của $A$ với mọi $x \\neq 0, x \\neq \\pm 1$.",
            "answer": "1"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tìm $x$ để biểu thức $M = \\frac{x^2 - 4}{x + 3} : \\frac{x - 2}{x + 3}$ có giá trị bằng 8.",
            "answer": "6"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Tính giá trị của tích $S = \\left(1 - \\frac{1}{4}\\right)\\left(1 - \\frac{1}{9}\\right)\\left(1 - \\frac{1}{16}\\right)$ viết dưới dạng số thập phân.",
            "answer": "0.625"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\left(\\frac{x}{x^2 - 36} - \\frac{x - 6}{x^2 + 6x}\\right) : \\frac{2x - 6}{x^2 + 6x}$.\na) Tìm điều kiện xác định của biểu thức $P$.\nb) Rút gọn biểu thức $P$.\nc) Tính giá trị của $P$ tại $x = 4$.",
            "rubric": "a) ĐKXĐ: x ≠ 0, x ≠ 6, x ≠ -6, x ≠ 3 (0.25đ).\nb) Quy đồng trong ngoặc:\nx / [(x - 6)(x + 6)] - (x - 6) / [x(x + 6)] = [x^2 - (x - 6)^2] / [x(x - 6)(x + 6)]\n= [x^2 - (x^2 - 12x + 36)] / [x(x - 6)(x + 6)] = (12x - 36) / [x(x - 6)(x + 6)] = 12(x - 3) / [x(x - 6)(x + 6)] (0.35đ).\nThực hiện phép chia:\nP = {12(x - 3) / [x(x - 6)(x + 6)]} * [x(x + 6) / 2(x - 3)] = 12 / [2(x - 6)] = 6 / (x - 6) (0.25đ).\nc) Tại x = 4 (thỏa mãn ĐKXĐ): P = 6 / (4 - 6) = 6 / (-2) = -3 (0.15đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $A = \\left(\\frac{x^2 + 1}{x^2 - 1} - 1\\right) : \\left(\\frac{x}{x - 1} - \\frac{1}{x + 1}\\right)$.\na) Rút gọn biểu thức $A$.\nb) Tìm giá trị của $x$ để $A = \\frac{1}{3}$.",
            "rubric": "a) Nhóm 1: (x^2 + 1)/(x^2 - 1) - 1 = (x^2 + 1 - x^2 + 1) / (x^2 - 1) = 2 / (x^2 - 1) (0.25đ).\nNhóm 2: x/(x - 1) - 1/(x + 1) = [x(x + 1) - (x - 1)] / (x^2 - 1) = (x^2 + x - x + 1) / (x^2 - 1) = (x^2 + 1) / (x^2 - 1) (0.25đ).\nThực hiện phép chia: A = [2 / (x^2 - 1)] * [(x^2 - 1) / (x^2 + 1)] = 2 / (x^2 + 1) (0.25đ).\nb) Cho A = 1/3 <=> 2 / (x^2 + 1) = 1/3 <=> x^2 + 1 = 6 <=> x^2 = 5 <=> x = ±sqrt(5) (thỏa mãn ĐKXĐ). Vậy x = ±sqrt(5) (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một người dự định chèo thuyền trên sông một đoạn đường $s\\text{ (km)}$. Vận tốc của thuyền khi nước yên lặng là $v\\text{ (km/h)}$, vận tốc dòng nước là $u\\text{ (km/h)}$ ($v > u > 0$).\na) Viết phân thức biểu thị tỉ số giữa thời gian ngược dòng và thời gian xuôi dòng của thuyền trên đoạn sông đó.\nb) Biết tỉ số thời gian ngược dòng so với xuôi dòng là $1.5$ lần và vận tốc dòng nước $u = 3\\text{ km/h}$. Tính vận tốc của thuyền khi nước yên lặng.",
            "rubric": "a) Thời gian xuôi dòng: t_x = s / (v + u); Thời gian ngược dòng: t_n = s / (v - u) (0.25đ).\nTỉ số: T = t_n / t_x = [s / (v - u)] : [s / (v + u)] = (v + u) / (v - u) (0.35đ).\nb) Cho (v + u) / (v - u) = 1.5 <=> v + 3 = 1.5(v - 3) <=> v + 3 = 1.5v - 4.5 (0.2đ).\n<=> 0.5v = 7.5 <=> v = 15 (km/h) (thỏa mãn v > 3). Vậy vận tốc của thuyền khi nước yên lặng là 15 km/h (0.2đ)."
        }
    ]
}

# ==============================================================================
# BÀI 24 - ĐỀ 3: NÂNG CAO (🚀)
# ==============================================================================
BAI4_EXAMS["c6_8_bai4_test3"] = {
    "title": "Toán 8 (KNTT) - Bài 24: Phép nhân và phép chia phân thức đại số - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính tích vô hạn $P = \\left(1 - \\frac{1}{4}\\right)\\left(1 - \\frac{1}{9}\\right)\\left(1 - \\frac{1}{16}\\right) \\dots \\left(1 - \\frac{1}{n^2}\\right)$ theo $n$:",
            "options": ["$\\frac{n + 1}{2n}$", "$\\frac{n}{2(n + 1)}$", "$\\frac{n - 1}{2n}$", "$\\frac{1}{2n}$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = \\left(\\frac{x^2 - y^2}{x^3 - y^3}\\right) : \\left(\\frac{x + y}{x^2 + xy + y^2}\\right)$. Giá trị của $A$ bằng:",
            "options": ["$1$", "$x - y$", "$x + y$", "$\\frac{1}{x - y}$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Rút gọn biểu thức $M = \\left(\\frac{a + b}{a - b} - \\frac{a - b}{a + b}\\right) : \\left(\\frac{a + b}{a - b} + \\frac{a - b}{a + b}\\right)$ ta được:",
            "options": ["$\\frac{2ab}{a^2 + b^2}$", "$\\frac{4ab}{a^2 + b^2}$", "$\\frac{ab}{a^2 + b^2}$", "$1$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Cho $x, y, z$ khác 0 thỏa mãn $x + y + z = 0$. Rút gọn biểu thức $P = \\left(\\frac{x}{y - z} + \\frac{y}{z - x} + \\frac{z}{x - y}\\right)\\left(\\frac{y - z}{x} + \\frac{z - x}{y} + \\frac{x - y}{z}\\right)$ ta được:",
            "options": ["$9$", "$0$", "$1$", "$3$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Vận dụng thấp",
            "question": "Giá trị của biểu thức $Q = \\frac{x^3 + y^3 + z^3 - 3xyz}{(x - y)^2 + (y - z)^2 + (z - x)^2}$ khi $x + y + z = 12$ bằng:",
            "options": ["$6$", "$12$", "$3$", "$24$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng cao",
            "question": "Cho phân thức $P = \\frac{4x^2 + 1}{2x}$. Với $x > 0$, giá trị nhỏ nhất của $P$ bằng:",
            "options": ["$2$", "$1$", "$4$", "$\\frac{5}{2}$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $A = \\left(\\frac{x^2 - 1}{x^4 - x^2 + 1}\\right) \\cdot \\left(\\frac{x^6 + 1}{x^2 + 1}\\right)$. Rút gọn biểu thức $A$ ta được:",
            "options": ["$x^2 - 1$", "$x^2 + 1$", "$x^4 - 1$", "$1$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng cao",
            "question": "Tìm số cặp số nguyên $(x; y)$ thỏa mãn đẳng thức phân thức $\\frac{x}{y} + \\frac{y}{x} = 2$ với $1 \\leq x, y \\leq 10$:",
            "options": ["$10$", "$5$", "$1$", "$20$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng cao",
            "question": "Cho $a, b, c > 0$ thỏa mãn $abc = 1$. Giá trị của biểu thức $S = \\frac{1}{1 + a + ab} + \\frac{1}{1 + b + bc} + \\frac{1}{1 + c + ca}$ bằng:",
            "options": ["$1$", "$3$", "$\\frac{1}{3}$", "$0$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các giá trị nguyên của $x$ để phân thức $B = \\left(\\frac{x + 2}{x - 1}\\right) : \\left(\\frac{x + 2}{2x + 1}\\right)$ nhận giá trị nguyên:",
            "options": ["$x \\in \\{-2, 0, 2, 4\\}$", "$x \\in \\{0, 2\\}$", "$x \\in \\{2, 4\\}$", "$x \\in \\{-1, 1\\}$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng cao",
            "question": "Cho $x > 1$. Giá trị nhỏ nhất của biểu thức $E = \\frac{x^2}{x - 1}$ bằng:",
            "options": ["$4$", "$2$", "$3$", "$1$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng cao",
            "question": "Rút gọn tích $T = \\left(1 + \\frac{1}{1 \\cdot 3}\\right)\\left(1 + \\frac{1}{2 \\cdot 4}\\right)\\left(1 + \\frac{1}{3 \\cdot 5}\\right) \\dots \\left(1 + \\frac{1}{n(n + 2)}\\right)$ theo $n$:",
            "options": ["$\\frac{2(n + 1)}{n + 2}$", "$\\frac{n + 1}{n + 2}$", "$\\frac{2n}{n + 1}$", "$\\frac{n + 2}{2(n + 1)}$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $P = \\left(\\frac{x^2 - 2x}{2x^2 + 8} - \\frac{2x^2}{8 - 4x + 2x^2 - x^3}\\right) \\cdot \\left(1 - \\frac{1}{x} - \\frac{2}{x^2}\\right)$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của $P$ là $x \\neq 0, x \\neq 2, x \\neq -1$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Biểu thức trong ngoặc thứ nhất thu gọn được là $\\frac{x}{2(x - 2)}$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Biểu thức trong ngoặc thứ hai thu gọn được là $\\frac{(x - 2)(x + 1)}{x^2}$.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Kết quả rút gọn tối giản của $P$ là $P = \\frac{x + 1}{2x}$.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Cho ba số thực dương $a, b, c$ thỏa mãn $abc = 1$. Xét biểu thức $M = \\frac{1}{ab + a + 1} + \\frac{1}{bc + b + 1} + \\frac{1}{ca + c + 1}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Thay $1 = abc$ vào phân thức thứ hai và thứ ba để đưa về cùng mẫu số.", "correct": True },
                { "key": "b", "level": "Vận dụng cao", "text": "Phân thức thứ hai biến đổi thành $\\frac{a}{1 + a + ab}$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Phân thức thứ ba biến đổi thành $\\frac{ab}{1 + a + ab}$.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Giá trị của biểu thức $M$ bằng 3.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Tính giá trị của tích $P = \\left(1 - \\frac{1}{4}\\right)\\left(1 - \\frac{1}{9}\\right)\\left(1 - \\frac{1}{16}\\right) \\dots \\left(1 - \\frac{1}{100}\\right)$. Kết quả là phân số tối giản $\\frac{a}{b}$. Tính $a + b$.",
            "answer": "31"
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $x > 2$. Tìm giá trị nhỏ nhất của biểu thức $A = \\frac{x^2 - 2x + 4}{x - 2}$.",
            "answer": "4"
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị của $x$ để biểu thức $M = \\frac{4x}{x^2 + 4}$ đạt giá trị lớn nhất.",
            "answer": "2"
        },
        {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Cho $a, b, c$ thỏa mãn $a + b + c = 0$ và $a^2 + b^2 + c^2 = 1$. Tính giá trị của biểu thức $a^4 + b^4 + c^4$ nhân với 2.",
            "answer": "1"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $A = \\left(\\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1}\\right) : \\left(\\frac{x^2 + 1}{x^2 - 1} - \\frac{x^2 - 1}{x^2 + 1}\\right)$.\na) Tìm điều kiện xác định của biểu thức $A$.\nb) Rút gọn biểu thức $A$.\nc) Chứng minh rằng $A > 0$ với mọi $x$ thỏa mãn điều kiện xác định.",
            "rubric": "a) ĐKXĐ: x ≠ 1 và x ≠ -1 (vì x^2 + 1 > 0 và x^2 + 1 ≠ x^2 - 1) (0.25đ).\nb) Tử thức:\n(x + 1)/(x - 1) - (x - 1)/(x + 1) = [(x + 1)^2 - (x - 1)^2] / (x^2 - 1) = 4x / (x^2 - 1) (0.25đ).\nMẫu thức:\n(x^2 + 1)/(x^2 - 1) - (x^2 - 1)/(x^2 + 1) = [(x^2 + 1)^2 - (x^2 - 1)^2] / [(x^2 - 1)(x^2 + 1)] = 4x^2 / [(x^2 - 1)(x^2 + 1)] (0.25đ).\nThực hiện phép chia:\nA = [4x / (x^2 - 1)] * {[(x^2 - 1)(x^2 + 1)] / (4x^2)} = (x^2 + 1) / x (0.15đ).\nc) ĐKXĐ cần bổ sung x ≠ 0. Khi x > 0 thì A > 0. Nếu x < 0 thì A < 0. Nhận xét đúng tập giá trị (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực dương $a, b, c$ thỏa mãn $abc = 1$.\nChứng minh rằng:\n$S = \\frac{1}{1 + a + ab} + \\frac{1}{1 + b + bc} + \\frac{1}{1 + c + ca} = 1$.",
            "rubric": "- Phân thức thứ nhất: P_1 = 1 / (1 + a + ab) (0.1đ).\n- Phân thức thứ hai: Nhân cả tử và mẫu với a:\nP_2 = a / [a(1 + b + bc)] = a / (a + ab + abc) = a / (a + ab + 1) (vì abc = 1) (0.35đ).\n- Phân thức thứ ba: Nhân cả tử và mẫu với ab:\nP_3 = ab / [ab(1 + c + ca)] = ab / (ab + abc + a^2bc) = ab / (ab + 1 + a) (vì abc = 1) (0.35đ).\n- Cộng ba phân thức cùng mẫu:\nS = P_1 + P_2 + P_3 = (1 + a + ab) / (1 + a + ab) = 1 (0.2đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức:\n$P = \\frac{x^2 + 2x + 17}{x + 1}$.",
            "rubric": "- Biến đổi biểu thức:\nP = [(x + 1)^2 + 16] / (x + 1) = (x + 1) + 16 / (x + 1) (0.35đ).\n- Vì x > 0 nên x + 1 > 1 > 0 (0.15đ).\n- Áp dụng bất đẳng thức Cô-si cho hai số dương (x + 1) và 16 / (x + 1):\n(x + 1) + 16 / (x + 1) ≥ 2 * sqrt((x + 1) * 16 / (x + 1)) = 2 * sqrt(16) = 8 (0.35đ).\n- Dấu '=' xảy ra khi x + 1 = 16 / (x + 1) <=> (x + 1)^2 = 16 <=> x + 1 = 4 (vì x + 1 > 0) <=> x = 3 (thỏa mãn x > 0) (0.1đ).\n- Vậy giá trị nhỏ nhất của P là 8 khi x = 3 (0.05đ)."
        }
    ]
}
