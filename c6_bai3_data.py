# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI - BÀI 23: PHÉP CỘNG VÀ PHÉP TRỪ PHÂN THỨC ĐẠI SỐ (TOÁN 8 - KNTT)
Gồm 3 đề phân hóa:
- Đề 1 (Cơ bản): Cộng trừ phân thức cùng mẫu, quy đồng cộng trừ phân thức đơn giản, tính giá trị biểu thức.
- Đề 2 (Khá): Cộng trừ phân thức mẫu bậc hai, đổi dấu mẫu thức, rút gọn biểu thức tổng hợp, bài toán thực tế.
- Đề 3 (Nâng cao): Tổng dãy phân thức dạng sai phân (telescoping), đẳng thức phân thức nhiều biến, bài toán cực trị.
"""

BAI3_EXAMS = {}

# ==============================================================================
# BÀI 23 - ĐỀ 1: CƠ BẢN (🌱)
# ==============================================================================
BAI3_EXAMS["c6_8_bai3_test1"] = {
    "title": "Toán 8 (KNTT) - Bài 23: Phép cộng và phép trừ phân thức đại số - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Kết quả của phép cộng $\\frac{x}{x + 1} + \\frac{1}{x + 1}$ là:",
            "options": ["$1$", "$\\frac{x + 1}{2x + 2}$", "$x$", "$\\frac{x}{x + 1}$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Kết quả của phép trừ $\\frac{3x - 1}{x - 2} - \\frac{x + 3}{x - 2}$ là:",
            "options": ["$\\frac{2x - 4}{x - 2}$", "$\\frac{2x + 2}{x - 2}$", "$\\frac{4x + 2}{x - 2}$", "$2x - 4$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Nhận biết",
            "question": "Phân thức đối của phân thức $\\frac{2x - 1}{x + 3}$ là:",
            "options": ["$\\frac{1 - 2x}{x + 3}$", "$\\frac{2x - 1}{-x + 3}$", "$\\frac{2x + 1}{x + 3}$", "$\\frac{1 - 2x}{-x - 3}$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Nhận biết",
            "question": "Muốn cộng hai phân thức có mẫu thức khác nhau, bước đầu tiên ta cần làm là:",
            "options": [
                "Quy đồng mẫu thức các phân thức",
                "Cộng các tử thức với nhau và cộng các mẫu thức với nhau",
                "Nhân tử thức này với mẫu thức kia",
                "Rút gọn từng phân thức về 1"
            ],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Nhận biết",
            "question": "Kết quả của phép tính $\\frac{a}{m} - \\frac{b}{m} + \\frac{c}{m}$ là:",
            "options": ["$\\frac{a - b + c}{m}$", "$\\frac{a - b - c}{m}$", "$\\frac{a + b + c}{m}$", "$\\frac{a - b + c}{3m}$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Nhận biết",
            "question": "Phép cộng phân thức đại số có tính chất nào sau đây?",
            "options": [
                "Cả tính chất giao hoán, kết hợp và cộng với 0",
                "Chỉ có tính chất giao hoán",
                "Chỉ có tính chất kết hợp",
                "Không có tính chất giao hoán"
            ],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{1}{x} + \\frac{1}{y}$ ta được kết quả là:",
            "options": ["$\\frac{x + y}{xy}$", "$\\frac{2}{x + y}$", "$\\frac{1}{xy}$", "$\\frac{x - y}{xy}$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{x}{x - 2} + \\frac{2}{2 - x}$ với $x \\neq 2$ ta được:",
            "options": ["$1$", "$-1$", "$\\frac{x + 2}{x - 2}$", "$0$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Thực hiện phép trừ $\\frac{x^2}{x - 1} - \\frac{1}{x - 1}$ với $x \\neq 1$ ta được:",
            "options": ["$x + 1$", "$x - 1$", "$1$", "$\\frac{x^2 - 1}{(x - 1)^2}$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Tổng $\\frac{3}{2x} + \\frac{5}{2x}$ bằng:",
            "options": ["$\\frac{4}{x}$", "$\\frac{8}{2x^2}$", "$\\frac{8}{4x}$", "$\\frac{2}{x}$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Kết quả của biểu thức $A = \\frac{2x - 1}{x - 3} - \\frac{x + 2}{x - 3}$ sau khi rút gọn là:",
            "options": ["$1$", "$\\frac{x - 3}{x - 3} = 1$", "$\\frac{x + 1}{x - 3}$", "$-1$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Giá trị của biểu thức $S = \\frac{x}{x + 2} + \\frac{2}{x + 2}$ tại $x = 2026$ bằng:",
            "options": ["$1$", "$2026$", "$2028$", "$0$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $P = \\frac{x^2}{x - 3} + \\frac{9}{3 - x}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của biểu thức $P$ là $x \\neq 3$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Đổi dấu phân thức thứ hai ta được $\\frac{9}{3 - x} = -\\frac{9}{x - 3}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Sau khi thực hiện phép tính và rút gọn, $P = x + 3$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 3$, giá trị của biểu thức $P$ bằng $6$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho biểu thức $Q = \\frac{1}{x - 1} - \\frac{1}{x + 1}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Mẫu thức chung của hai phân thức là $(x - 1)(x + 1) = x^2 - 1$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Tử thức sau khi quy đồng và trừ là $(x + 1) - (x - 1) = 2$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Biểu thức rút gọn là $Q = \\frac{2}{x^2 - 1}$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Khi $x = 3$, giá trị của $Q$ bằng $\\frac{1}{2}$.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $A = \\frac{3x - 4}{x - 2} - \\frac{x}{x - 2}$ với $x = 5$.",
            "answer": "2"
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{2}{x - 1} + \\frac{3}{1 - x}$ rồi tính giá trị tại $x = 2$.",
            "answer": "-1"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $B = \\frac{1}{x} + \\frac{1}{x + 1}$. Khi $x = 1$, giá trị của $B$ bằng bao nhiêu?",
            "answer": "1.5"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Tìm $x$ để biểu thức $\\frac{x}{x - 1} - \\frac{2}{x - 1}$ nhận giá trị bằng 1.",
            "answer": "Không có"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện các phép tính sau:\na) $A = \\frac{2x + 5}{x - 3} + \\frac{x - 14}{x - 3}$.\nb) $B = \\frac{x}{x - 2} - \\frac{x^2 - 4}{x^2 - 4}$.",
            "rubric": "a) Cùng mẫu thức x - 3: A = [(2x + 5) + (x - 14)] / (x - 3) = (3x - 9) / (x - 3) (0.3đ).\nRút gọn: A = 3(x - 3) / (x - 3) = 3 (0.2đ).\nb) Rút gọn phân thức thứ hai: (x^2 - 4)/(x^2 - 4) = 1 (với x ≠ ±2) (0.2đ).\nB = x / (x - 2) - 1 = [x - (x - 2)] / (x - 2) = 2 / (x - 2) (0.3đ)."
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính:\n$M = \\frac{1}{x - 2} + \\frac{1}{x + 2} - \\frac{2x}{x^2 - 4}$.",
            "rubric": "- MTC = (x - 2)(x + 2) = x^2 - 4 (0.25đ).\n- Quy đồng mẫu thức các phân thức:\n+ Phân thức 1: (x + 2) / [(x - 2)(x + 2)] (0.2đ).\n+ Phân thức 2: (x - 2) / [(x - 2)(x + 2)] (0.2đ).\n- Cộng trừ tử thức:\nTử = (x + 2) + (x - 2) - 2x = 2x - 2x = 0 (0.25đ).\n- Vậy M = 0 / (x^2 - 4) = 0 (với x ≠ ±2) (0.1đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một người đi xe đạp từ A đến B dài $30\\text{ km}$ với vận tốc $x\\text{ (km/h)}$. Khi về từ B về A, người đó tăng vận tốc thêm $3\\text{ km/h}$.\na) Viết biểu thức biểu thị tổng thời gian cả đi và về của người đó theo $x$.\nb) Tính tổng thời gian nếu vận tốc lúc đi là $x = 12\\text{ km/h}$.",
            "rubric": "a) Thời gian lúc đi: t_1 = 30 / x (giờ) (0.25đ).\nVận tốc lúc về: x + 3 (km/h). Thời gian lúc về: t_2 = 30 / (x + 3) (giờ) (0.25đ).\nTổng thời gian: T = 30 / x + 30 / (x + 3) = [30(x + 3) + 30x] / [x(x + 3)] = (60x + 90) / [x(x + 3)] (giờ) (0.25đ).\nb) Với x = 12 km/h:\nT = 30 / 12 + 30 / (12 + 3) = 2.5 + 30 / 15 = 2.5 + 2 = 4.5 (giờ) (0.25đ)."
        }
    ]
}

# ==============================================================================
# BÀI 23 - ĐỀ 2: KHÁ (🌿)
# ==============================================================================
BAI3_EXAMS["c6_8_bai3_test2"] = {
    "title": "Toán 8 (KNTT) - Bài 23: Phép cộng và phép trừ phân thức đại số - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{x + 3}{x^2 - 1} - \\frac{1}{x^2 + x}$ ta được kết quả là:",
            "options": ["$\\frac{x + 1}{x(x - 1)}$", "$\\frac{1}{x - 1}$", "$\\frac{x - 1}{x(x + 1)}$", "$\\frac{x + 2}{x^2 - 1}$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $P = \\frac{1}{x - 2} - \\frac{4}{x^2 - 4}$ với $x \\neq \\pm 2$ ta được:",
            "options": ["$\\frac{1}{x + 2}$", "$\\frac{1}{x - 2}$", "$\\frac{x - 2}{x + 2}$", "$\\frac{2}{x^2 - 4}$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Kết quả của phép tính $\\frac{2x}{x^2 - 9} + \\frac{1}{3 - x}$ với $x \\neq \\pm 3$ là:",
            "options": ["$\\frac{1}{x - 3}$", "$\\frac{1}{x + 3}$", "$\\frac{x - 1}{x^2 - 9}$", "$\\frac{3x + 1}{x^2 - 9}$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Thông hiểu",
            "question": "Biểu thức $\\frac{x^2 + 2}{x^3 - 1} + \\frac{2}{x^2 + x + 1} - \\frac{1}{x - 1}$ rút gọn được là:",
            "options": ["$\\frac{2}{x^2 + x + 1}$", "$\\frac{1}{x - 1}$", "$0$", "$\\frac{1}{x^3 - 1}$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Thông hiểu",
            "question": "Tính tổng $\\frac{x - 1}{x} + \\frac{x + 1}{x + 2}$ tại $x = 1$:",
            "options": ["$\\frac{2}{3}$", "$1$", "$0$", "$\\frac{4}{3}$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng thấp",
            "question": "Cho $A = \\frac{2}{x + 1}$ và $B = \\frac{1}{x - 1}$. Để $A + B = 0$ thì $x$ bằng:",
            "options": ["$\\frac{1}{3}$", "$3$", "$-\\frac{1}{3}$", "$-3$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng thấp",
            "question": "Biết $\\frac{3x - 1}{(x - 1)(x + 2)} = \\frac{A}{x - 1} + \\frac{B}{x + 2}$. Giá trị của $A + B$ bằng:",
            "options": ["$3$", "$1$", "$2$", "$0$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng thấp",
            "question": "Rút gọn biểu thức $M = \\frac{x + 1}{x^2 - 2x + 1} - \\frac{1}{x - 1}$ ta được:",
            "options": ["$\\frac{2}{(x - 1)^2}$", "$\\frac{2}{x - 1}$", "$\\frac{x}{(x - 1)^2}$", "$0$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng thấp",
            "question": "Giá trị của biểu thức $P = \\frac{x + 2}{x - 1} - \\frac{x - 3}{x + 1}$ tại $x = 2$ bằng:",
            "options": ["$\\frac{13}{3}$", "$3$", "$\\frac{11}{3}$", "$4$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng thấp",
            "question": "Tìm $x$ nguyên để phân thức $A = \\frac{3}{x - 2} + \\frac{1}{2 - x}$ nhận giá trị nguyên:",
            "options": ["$x \\in \\{0, 1, 3, 4\\}$", "$x \\in \\{1, 3\\}$", "$x \\in \\{2, 4\\}$", "$x \\in \\{-1, 0, 1\\}$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng thấp",
            "question": "Biểu thức $K = \\frac{x - y}{xy} + \\frac{y - z}{yz} + \\frac{z - x}{zx}$ rút gọn được kết quả là:",
            "options": ["$0$", "$1$", "$\\frac{x + y + z}{xyz}$", "$-1$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng thấp",
            "question": "Một ca nô chạy xuôi dòng $45\\text{ km}$ rồi ngược dòng $18\\text{ km}$. Biết vận tốc dòng nước là $3\\text{ km/h}$. Biểu thức biểu thị tổng thời gian ca nô đi theo vận tốc thực $v\\text{ (km/h)}$ ($v > 3$) là:",
            "options": [
                "$\\frac{45}{v + 3} + \\frac{18}{v - 3}$",
                "$\\frac{45}{v - 3} + \\frac{18}{v + 3}$",
                "$\\frac{63}{v}$",
                "$\\frac{45 + 18}{v + 3}$"
            ],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A = \\frac{x}{x - 3} - \\frac{6}{x + 3} - \\frac{18}{x^2 - 9}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của $A$ là $x \\neq 3$ và $x \\neq -3$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Mẫu thức chung của ba phân thức là $x^2 - 9$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Tử thức sau khi quy đồng và thu gọn là $x^2 - 3x = x(x - 3)$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Biểu thức rút gọn là $A = \\frac{x}{x + 3}$.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai biểu thức $P = \\frac{x + 2}{x - 2}$ và $Q = \\frac{x - 2}{x + 2}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Tổng $P + Q = \\frac{2(x^2 + 4)}{x^2 - 4}$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Hiệu $P - Q = \\frac{8x}{x^2 - 4}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Phương trình $P - Q = 0$ có hai nghiệm phân biệt là $x = 0$ và $x = 2$.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 3$, giá trị của $P - Q$ bằng $4.8$.", "correct": True }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $P = \\frac{x^2}{x - 4} - \\frac{16}{x - 4}$ tại $x = 20$.",
            "answer": "24"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Rút gọn biểu thức $A = \\frac{1}{x(x + 1)} + \\frac{1}{(x + 1)(x + 2)}$ rồi tính giá trị tại $x = 2$.",
            "answer": "0.25"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tìm $x$ để biểu thức $\\frac{2}{x - 1} - \\frac{1}{x + 1}$ nhận giá trị bằng 0.",
            "answer": "-3"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $M = \\frac{x + 3}{x - 1} - \\frac{x - 2}{x - 1}$. Biểu thức $M$ nhận giá trị bằng bao nhiêu với mọi $x \\neq 1$?",
            "answer": "Không đổi"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1} - \\frac{4}{x^2 - 1}$.\na) Tìm điều kiện xác định của $P$.\nb) Rút gọn biểu thức $P$.\nc) Tìm giá trị của $x$ để $P = 1$.",
            "rubric": "a) ĐKXĐ: x^2 - 1 ≠ 0 <=> x ≠ 1 và x ≠ -1 (0.25đ).\nb) MTC = (x - 1)(x + 1) = x^2 - 1.\nTử = (x + 1)^2 - (x - 1)^2 - 4 = (x^2 + 2x + 1) - (x^2 - 2x + 1) - 4 = 4x - 4 = 4(x - 1) (0.35đ).\nRút gọn: P = 4(x - 1) / [(x - 1)(x + 1)] = 4 / (x + 1) (0.2đ).\nc) Cho P = 1 <=> 4 / (x + 1) = 1 <=> x + 1 = 4 <=> x = 3 (thỏa mãn ĐKXĐ). Vậy x = 3 (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $B = \\frac{2x - 1}{x + 3} - \\frac{x}{3 - x} - \\frac{3 - 10x}{x^2 - 9}$.\na) Rút gọn biểu thức $B$.\nb) Tìm các giá trị nguyên của $x$ để $B$ nhận giá trị nguyên.",
            "rubric": "a) Đổi dấu: -x / (3 - x) = x / (x - 3). MTC = (x - 3)(x + 3) = x^2 - 9 (0.15đ).\nTử = (2x - 1)(x - 3) + x(x + 3) - (3 - 10x)\n= (2x^2 - 7x + 3) + (x^2 + 3x) - 3 + 10x = 3x^2 + 6x = 3x(x + 2) (0.35đ).\nB = 3x(x + 2) / [(x - 3)(x + 3)] (0.1đ).\nb) Xét biểu thức thu gọn: B = (3x^2 + 6x) / (x^2 - 9) = 3 + (6x + 27) / (x^2 - 9) hoặc xét giá trị x nguyên thỏa mãn chia hết (0.4đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Hai vòi nước cùng chảy vào một bể không có nước. Vòi thứ nhất chảy một mình mất $x$ giờ thì đầy bể, vòi thứ hai chảy một mình mất $y$ giờ thì đầy bể.\na) Viết phân thức biểu thị lượng nước cả hai vòi chảy được trong 1 giờ.\nb) Biết vòi thứ nhất chảy nhanh gấp đôi vòi thứ hai ($y = 2x$) và khi mở cả hai vòi cùng lúc thì mất $4$ giờ đầy bể. Tính thời gian mỗi vòi chảy một mình đầy bể.",
            "rubric": "a) Trong 1 giờ:\nVòi 1 chảy được: 1/x bể (0.15đ).\nVòi 2 chảy được: 1/y bể (0.15đ).\nCả hai vòi chảy được: 1/x + 1/y = (x + y)/(xy) bể (0.2đ).\nb) Vì y = 2x nên trong 1 giờ hai vòi chảy được: 1/x + 1/(2x) = 3/(2x) bể (0.2đ).\nThời gian cả hai vòi chảy đầy bể là 4 giờ, nên trong 1 giờ chảy được 1/4 bể:\n3/(2x) = 1/4 <=> 2x = 12 <=> x = 6 (giờ) (0.15đ).\nSuy ra y = 2x = 12 (giờ). Vậy vòi 1 mất 6 giờ, vòi 2 mất 12 giờ (0.15đ)."
        }
    ]
}

# ==============================================================================
# BÀI 23 - ĐỀ 3: NÂNG CAO (🚀)
# ==============================================================================
BAI3_EXAMS["c6_8_bai3_test3"] = {
    "title": "Toán 8 (KNTT) - Bài 23: Phép cộng và phép trừ phân thức đại số - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính tổng $S = \\frac{1}{x(x + 1)} + \\frac{1}{(x + 1)(x + 2)} + \\frac{1}{(x + 2)(x + 3)}$ ta được kết quả là:",
            "options": ["$\\frac{3}{x(x + 3)}$", "$\\frac{1}{x(x + 3)}$", "$\\frac{3}{(x + 1)(x + 2)}$", "$\\frac{x}{x + 3}$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $P = \\frac{1}{a(a - b)(a - c)} + \\frac{1}{b(b - a)(b - c)} + \\frac{1}{c(c - a)(c - b)}$ với $a, b, c$ đôi một khác nhau và khác 0:",
            "options": ["$\\frac{1}{abc}$", "$0$", "$\\frac{a + b + c}{abc}$", "$1$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho $x + y + z = 0$. Rút gọn biểu thức $M = \\frac{1}{x^2 + y^2 - z^2} + \\frac{1}{y^2 + z^2 - x^2} + \\frac{1}{z^2 + x^2 - y^2}$ ta được:",
            "options": ["$0$", "$1$", "$\\frac{1}{xyz}$", "$-1$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $A = \\frac{1}{x - 1} - \\frac{1}{x + 1} - \\frac{2}{x^2 + 1} - \\frac{4}{x^4 + 1}$. Kết quả rút gọn của $A$ là:",
            "options": ["$\\frac{8}{x^8 - 1}$", "$-\\frac{8}{x^8 - 1}$", "$\\frac{4}{x^8 - 1}$", "$0$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Vận dụng thấp",
            "question": "Tìm các hằng số $A, B$ sao cho $\\frac{5x - 2}{x^2 - 4} = \\frac{A}{x - 2} + \\frac{B}{x + 2}$ với mọi $x \\neq \\pm 2$:",
            "options": ["$A = 2, B = 3$", "$A = 3, B = 2$", "$A = 5, B = -2$", "$A = 1, B = 4$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực $x, y, z$ thỏa mãn $xy + yz + zx = 1$. Giá trị của biểu thức $P = \\frac{x}{1 + x^2} + \\frac{y}{1 + y^2} + \\frac{z}{1 + z^2}$ bằng:",
            "options": [
                "$\\frac{2}{(x + y)(y + z)(z + x)}$",
                "$\\frac{1}{(x + y)(y + z)(z + x)}$",
                "$1$",
                "$0$"
            ],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng cao",
            "question": "Tính tổng $S = \\frac{1}{x^2 + 3x + 2} + \\frac{1}{x^2 + 5x + 6} + \\frac{1}{x^2 + 7x + 12}$ ta được:",
            "options": ["$\\frac{3}{(x + 1)(x + 4)}$", "$\\frac{1}{(x + 1)(x + 4)}$", "$\\frac{3}{x^2 + 4x}$", "$\\frac{x}{(x + 1)(x + 4)}$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng cao",
            "question": "Cho $a, b, c > 0$. Giá trị nhỏ nhất của biểu thức $P = \\frac{a}{b + c} + \\frac{b}{c + a} + \\frac{c}{a + b}$ (Bất đẳng thức Nesbitt) bằng:",
            "options": ["$\\frac{3}{2}$", "$1$", "$2$", "$3$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng cao",
            "question": "Có bao nhiêu số nguyên dương $n$ để phân thức $A = \\frac{n^2 + 3n + 5}{n + 1}$ nhận giá trị nguyên?",
            "options": ["$2$", "$1$", "$3$", "$4$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng cao",
            "question": "Cho $\\frac{a}{x} + \\frac{b}{y} + \\frac{c}{z} = 1$ và $\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 0$. Giá trị của $\\frac{a^2}{x^2} + \\frac{b^2}{y^2} + \\frac{c^2}{z^2}$ bằng:",
            "options": ["$1$", "$0$", "$2$", "$4$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức $Q = \\frac{x^2 - 2x + 2025}{x^2}$ với $x > 0$:",
            "options": ["$\\frac{2024}{2025}$", "$1$", "$2025$", "$\\frac{2025}{2024}$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng cao",
            "question": "Rút gọn biểu thức $S_n = \\frac{1}{1 \\cdot 3} + \\frac{1}{3 \\cdot 5} + \\dots + \\frac{1}{(2n - 1)(2n + 1)}$ thành một phân thức theo $n$:",
            "options": ["$\\frac{n}{2n + 1}$", "$\\frac{1}{2n + 1}$", "$\\frac{2n}{2n + 1}$", "$\\frac{n - 1}{2n + 1}$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho dãy phân thức $A_k = \\frac{1}{k(k + 1)}$ với $k \\in \\mathbb{N}^*$ và xét tổng $S_n = A_1 + A_2 + \\dots + A_n$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Ta có đẳng thức $\\frac{1}{k(k + 1)} = \\frac{1}{k} - \\frac{1}{k + 1}$ với mọi $k \\in \\mathbb{N}^*$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Tổng $S_n = 1 - \\frac{1}{n + 1} = \\frac{n}{n + 1}$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Với mọi số nguyên dương $n$, tổng $S_n$ luôn nhỏ hơn 1.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Khi $n = 99$, giá trị của $S_n$ bằng $0.98$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 1$. Xét biểu thức $P = \\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Ta có $(a + b + c)\\left(\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}\\right) = 3 + \\left(\\frac{a}{b} + \\frac{b}{a}\\right) + \\left(\\frac{b}{c} + \\frac{c}{b}\\right) + \\left(\\frac{c}{a} + \\frac{a}{c}\\right)$.", "correct": True },
                { "key": "b", "level": "Vận dụng cao", "text": "Áp dụng bất đẳng thức $\\frac{x}{y} + \\frac{y}{x} \\geq 2$, ta suy ra $(a + b + c)\\left(\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}\\right) \\geq 9$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Giá trị nhỏ nhất của biểu thức $P$ bằng $9$, đạt được khi $a = b = c = \\frac{1}{3}$.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Biểu thức $P$ có giá trị lớn nhất bằng 27.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Tính tổng $S = \\frac{1}{1 \\cdot 4} + \\frac{1}{4 \\cdot 7} + \\frac{1}{7 \\cdot 10} + \\frac{1}{10 \\cdot 13}$. Kết quả là phân số tối giản $\\frac{a}{b}$. Tính $a + b$.",
            "answer": "17"
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $A = \\frac{x^2 + 4}{x}$.",
            "answer": "4"
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm số nguyên $x$ lớn nhất để phân thức $\\frac{2x + 7}{x + 1}$ nhận giá trị là một số nguyên dương.",
            "answer": "4"
        },
        {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tính giá trị của biểu thức $P = \\frac{1}{x(x + 1)} + \\frac{1}{(x + 1)(x + 2)} + \\dots + \\frac{1}{(x + 9)(x + 10)}$ tại $x = 10$.",
            "answer": "0.05"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực khác 0 thỏa mãn $a + b + c = 0$.\nTính giá trị của biểu thức:\n$A = \\frac{1}{a^2 + b^2 - c^2} + \\frac{1}{b^2 + c^2 - a^2} + \\frac{1}{c^2 + a^2 - b^2}$.",
            "rubric": "- Từ a + b + c = 0 => a + b = -c => (a + b)^2 = c^2 <=> a^2 + 2ab + b^2 = c^2 <=> a^2 + b^2 - c^2 = -2ab (0.25đ).\n- Tương tự:\nb^2 + c^2 - a^2 = -2bc (0.25đ).\nc^2 + a^2 - b^2 = -2ca (0.25đ).\n- Thay vào A:\nA = 1/(-2ab) + 1/(-2bc) + 1/(-2ca) = -1/2 * (1/ab + 1/bc + 1/ca) (0.15đ).\nQuy đồng: 1/ab + 1/bc + 1/ca = (c + a + b) / abc = 0 / abc = 0 (vì a+b+c=0) (0.1đ).\nVậy A = 0 (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Rút gọn biểu thức:\n$S = \\frac{1}{x^2 + x} + \\frac{1}{x^2 + 3x + 2} + \\frac{1}{x^2 + 5x + 6} + \\dots + \\frac{1}{x^2 + 19x + 90}$.",
            "rubric": "- Phân tích các mẫu thức thành nhân tử:\nx^2 + x = x(x + 1)\nx^2 + 3x + 2 = (x + 1)(x + 2)\nx^2 + 5x + 6 = (x + 2)(x + 3)\n...\nx^2 + 19x + 90 = (x + 9)(x + 10) (0.3đ).\n- Áp dụng công thức 1 / [k(k + 1)] = 1/k - 1/(k + 1):\nS = (1/x - 1/(x + 1)) + (1/(x + 1) - 1/(x + 2)) + ... + (1/(x + 9) - 1/(x + 10)) (0.3đ).\n- Triệt tiêu các số hạng đối nhau:\nS = 1/x - 1/(x + 10) (0.2đ).\n- Quy đồng mẫu thức:\nS = (x + 10 - x) / [x(x + 10)] = 10 / [x(x + 10)] (0.2đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho hai số thực $x, y$ thỏa mãn $x > y > 0$ và $xy = 1$.\nChứng minh rằng $\\frac{x^2 + y^2}{x - y} \\geq 2\\sqrt{2}$.",
            "rubric": "- Biến đổi tử thức theo (x - y):\nx^2 + y^2 = (x - y)^2 + 2xy = (x - y)^2 + 2 (vì xy = 1) (0.3đ).\n- Khi đó biểu thức trở thành:\nP = [(x - y)^2 + 2] / (x - y) = (x - y) + 2 / (x - y) (0.3đ).\n- Vì x > y > 0 nên x - y > 0. Áp dụng bất đẳng thức Cô-si cho hai số dương (x - y) và 2/(x - y):\n(x - y) + 2 / (x - y) ≥ 2 * sqrt((x - y) * 2 / (x - y)) = 2 * sqrt(2) (0.3đ).\n- Dấu '=' xảy ra khi x - y = 2/(x - y) <=> (x - y)^2 = 2 <=> x - y = sqrt(2). Kết hợp xy = 1 giải được cặp x, y thỏa mãn. Ta có đpcm (0.1đ)."
        }
    ]
}
