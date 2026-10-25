# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI - BÀI 21: PHÂN THỨC ĐẠI SỐ (TOÁN 8 - KNTT)
Gồm 3 đề phân hóa:
- Đề 1 (Cơ bản): Định nghĩa phân thức đại số, tử thức, mẫu thức, điều kiện xác định cơ bản, hai phân thức bằng nhau, tính giá trị phân thức.
- Đề 2 (Khá): Điều kiện xác định nâng cao, tìm x để phân thức bằng 0, tìm x nguyên để phân thức nguyên, chứng minh hai phân thức bằng nhau.
- Đề 3 (Nâng cao): Phân thức chứa nhiều biến, giá trị lớn nhất/nhỏ nhất cơ bản, tìm x để phân thức nhận giá trị dương/âm, bài toán thực tế.
"""

BAI1_EXAMS = {}

# ==============================================================================
# BÀI 21 - ĐỀ 1: CƠ BẢN (🌱)
# ==============================================================================
BAI1_EXAMS["c6_8_bai1_test1"] = {
    "title": "Toán 8 (KNTT) - Bài 21: Phân thức đại số - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Biểu thức nào sau đây là một phân thức đại số?",
            "options": ["$\\frac{x - 1}{x + 2}$", "$\\frac{\\sqrt{x}}{x + 1}$", "$\\frac{x + 1}{0}$", "$\\sqrt{x - 3}$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Trong phân thức $\\frac{2x - 3}{x^2 + 1}$, tử thức là:",
            "options": ["$2x - 3$", "$x^2 + 1$", "$2x$", "$1$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Nhận biết",
            "question": "Trong phân thức $\\frac{x + 5}{3x - 6}$, mẫu thức là:",
            "options": ["$3x - 6$", "$x + 5$", "$3x$", "$6$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Nhận biết",
            "question": "Mỗi đa thức được coi là một phân thức đại số với mẫu thức bằng:",
            "options": ["$1$", "$0$", "$x$", "Chính đa thức đó"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Nhận biết",
            "question": "Hai phân thức $\\frac{A}{B}$ và $\\frac{C}{D}$ ($B \\neq 0, D \\neq 0$) được gọi là bằng nhau nếu:",
            "options": ["$A \\cdot D = B \\cdot C$", "$A \\cdot C = B \\cdot D$", "$A + D = B + C$", "$A - D = B - C$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Nhận biết",
            "question": "Điều kiện xác định của phân thức $\\frac{x + 2}{x - 3}$ là:",
            "options": ["$x \\neq 3$", "$x \\neq -2$", "$x \\neq 0$", "$x > 3$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Nhận biết",
            "question": "Điều kiện xác định của phân thức $\\frac{2x + 1}{x + 4}$ là:",
            "options": ["$x \\neq -4$", "$x \\neq 4$", "$x \\neq -\\frac{1}{2}$", "$x \\neq 0$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Thông hiểu",
            "question": "Cặp phân thức nào sau đây bằng nhau?",
            "options": [
                "$\\frac{x - 1}{x + 1}$ và $\\frac{(x - 1)^2}{(x + 1)(x - 1)}$",
                "$\\frac{x}{2}$ và $\\frac{x^2}{2}$",
                "$\\frac{x + 1}{x - 1}$ và $\\frac{-x - 1}{x - 1}$",
                "$\\frac{2x}{3}$ và $\\frac{2}{3x}$"
            ],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Giá trị của phân thức $P = \\frac{x^2 - 1}{x + 1}$ tại $x = 3$ bằng:",
            "options": ["$2$", "$4$", "$8$", "$0$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Phân thức $\\frac{x - 2}{x^2 + 1}$ xác định với:",
            "options": ["Mọi số thực $x$", "$x \\neq 2$", "$x \\neq 1$", "$x \\neq -1$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Giá trị của phân thức $\\frac{3x + 6}{x - 1}$ tại $x = 2$ là:",
            "options": ["$12$", "$6$", "$9$", "$3$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Phân thức nào sau đây luôn có nghĩa với mọi giá trị của $x$?",
            "options": ["$\\frac{x + 3}{x^2 + 4}$", "$\\frac{x - 1}{x^2 - 4}$", "$\\frac{1}{x}$", "$\\frac{x + 2}{x - 5}$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho phân thức đại số $A = \\frac{2x - 4}{x - 3}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Tử thức của phân thức $A$ là đa thức $2x - 4$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Điều kiện xác định của phân thức $A$ là $x \\neq 3$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Tại $x = 5$, giá trị của phân thức $A$ bằng $3$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Phân thức $A$ bằng 0 khi và chỉ khi $x = 3$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai phân thức $M = \\frac{x + 2}{x - 1}$ và $N = \\frac{x^2 - 4}{x^2 - 3x + 2}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Phân thức $M$ xác định khi và chỉ khi $x \\neq 1$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Ta có $(x + 2)(x^2 - 3x + 2) = (x - 1)(x^2 - 4)$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Hai phân thức $M$ và $N$ bằng nhau trên tập xác định chung.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 2$, cả hai phân thức $M$ và $N$ đều nhận giá trị bằng 4.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của phân thức $A = \\frac{x + 5}{x - 2}$ tại $x = 3$.",
            "answer": "8"
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm giá trị của $x$ để phân thức $\\frac{3x - 9}{x + 4}$ có giá trị bằng 0.",
            "answer": "3"
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Cho phân thức $\\frac{x^2 - 16}{x - 4}$. Sau khi rút gọn, tính giá trị của biểu thức tại $x = 6$.",
            "answer": "10"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Tìm số các giá trị nguyên của $x$ để phân thức $\\frac{4}{x - 1}$ nhận giá trị là một số nguyên.",
            "answer": "6"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho phân thức đại số $P = \\frac{3x - 6}{x^2 - 4}$.\na) Tìm điều kiện xác định của phân thức $P$.\nb) Chứng minh rằng phân thức $P$ bằng phân thức $\\frac{3}{x + 2}$ với mọi $x$ thỏa mãn điều kiện xác định.\nc) Tính giá trị của $P$ tại $x = 3$.",
            "rubric": "a) ĐKXĐ: x^2 - 4 ≠ 0 <=> (x - 2)(x + 2) ≠ 0 <=> x ≠ 2 và x ≠ -2 (0.35đ).\nb) Xét tích chéo: (3x - 6)(x + 2) = 3(x - 2)(x + 2) = 3(x^2 - 4) = 3x^2 - 12 (0.2đ).\n(x^2 - 4) * 3 = 3x^2 - 12. Do đó (3x - 6)(x + 2) = (x^2 - 4)*3, suy ra hai phân thức bằng nhau (0.2đ).\nc) Với x = 3 (thỏa mãn ĐKXĐ), P = 3 / (3 + 2) = 3/5 = 0.6 (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $A = \\frac{x^2 - 2x}{2x^2 - 8}$.\na) Tìm điều kiện xác định của $A$.\nb) Rút gọn phân thức $A$.\nc) Tìm giá trị của $x$ để phân thức $A$ nhận giá trị bằng $2$.",
            "rubric": "a) ĐKXĐ: 2x^2 - 8 ≠ 0 <=> 2(x^2 - 4) ≠ 0 <=> x ≠ 2 và x ≠ -2 (0.25đ).\nb) Ta có A = [x(x - 2)] / [2(x - 2)(x + 2)] = x / [2(x + 2)] (0.35đ).\nc) Cho A = 2 <=> x / [2(x + 2)] = 2 <=> x = 4(x + 2) <=> x = 4x + 8 <=> 3x = -8 <=> x = -8/3 (0.25đ).\nKiểm tra x = -8/3 thỏa mãn ĐKXĐ. Vậy x = -8/3 (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một ô tô dự định đi quãng đường $S = 120\\text{ km}$ với vận tốc $x\\text{ (km/h)}$.\na) Hãy viết phân thức biểu thị thời gian dự định đi của ô tô theo $x$.\nb) Thực tế ô tô đi nhanh hơn dự định $10\\text{ km/h}$. Hãy viết phân thức biểu thị thời gian thực tế ô tô đi.\nc) Tính thời gian thực tế ô tô đi nếu vận tốc dự định là $x = 50\\text{ km/h}$.",
            "rubric": "a) Phân thức biểu thị thời gian dự định: t_dự_định = 120 / x (giờ) (0.35đ).\nb) Vận tốc thực tế là x + 10 (km/h). Phân thức biểu thị thời gian thực tế: t_thực_tế = 120 / (x + 10) (giờ) (0.35đ).\nc) Khi x = 50 km/h, t_thực_tế = 120 / (50 + 10) = 120 / 60 = 2 (giờ) (0.3đ)."
        }
    ]
}

# ==============================================================================
# BÀI 21 - ĐỀ 2: KHÁ (🌿)
# ==============================================================================
BAI1_EXAMS["c6_8_bai1_test2"] = {
    "title": "Toán 8 (KNTT) - Bài 21: Phân thức đại số - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Điều kiện xác định của phân thức $\\frac{x - 1}{x^2 - 9}$ là:",
            "options": ["$x \\neq 3$ và $x \\neq -3$", "$x \\neq 3$", "$x \\neq 9$", "$x \\neq -3$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Phân thức $\\frac{x^2 + 1}{x^2 - 2x + 1}$ xác định khi:",
            "options": ["$x \\neq 1$", "$x \\neq -1$", "$x \\neq 0$", "Với mọi $x$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Giá trị của $x$ để phân thức $\\frac{x^2 - 4}{x + 2}$ có giá trị bằng $0$ là:",
            "options": ["$x = 2$", "$x = -2$", "$x = 2$ hoặc $x = -2$", "Không có giá trị nào"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Thông hiểu",
            "question": "Cho hai phân thức $\\frac{A}{x - 1}$ và $\\frac{x + 2}{x^2 - 1}$. Để hai phân thức này bằng nhau thì đa thức $A$ bằng:",
            "options": ["$\\frac{x + 2}{x + 1}$", "$x + 2$", "$x + 1$", "$x - 1$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Thông hiểu",
            "question": "Tìm điều kiện xác định của phân thức $\\frac{2x - 5}{x(x + 3)}$:",
            "options": ["$x \\neq 0$ và $x \\neq -3$", "$x \\neq 0$", "$x \\neq 3$", "$x \\neq \\frac{5}{2}$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Thông hiểu",
            "question": "Biết $\\frac{x^2 - 9}{x + 3} = ax + b$ với mọi $x \\neq -3$. Giá trị của $a + b$ bằng:",
            "options": ["$-2$", "$2$", "$4$", "$-4$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Thông hiểu",
            "question": "Phân thức $\\frac{5}{x^2 + 2x + 2}$ có điều kiện xác định là:",
            "options": ["Xác định với mọi số thực $x$", "$x \\neq -1$", "$x \\neq -2$", "$x > 0$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng thấp",
            "question": "Có bao nhiêu giá trị nguyên của $x$ để phân thức $\\frac{6}{x + 2}$ nhận giá trị nguyên?",
            "options": ["$8$", "$4$", "$6$", "$2$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng thấp",
            "question": "Tìm $x$ để phân thức $\\frac{2x + 1}{x - 3}$ nhận giá trị bằng $3$:",
            "options": ["$x = 10$", "$x = 8$", "$x = -10$", "$x = 5$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $B = \\frac{x - 3}{x + 1}$. Tìm $x$ để $B < 0$:",
            "options": ["$-1 < x < 3$", "$x > 3$", "$x < -1$", "$x \\leq -1$ hoặc $x \\geq 3$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng thấp",
            "question": "Tìm các giá trị nguyên của $x$ để phân thức $\\frac{x + 3}{x - 1}$ nhận giá trị nguyên:",
            "options": [
                "$x \\in \\{-3, -1, 0, 2, 3, 5\\}$",
                "$x \\in \\{1, 2, 3, 4\\}$",
                "$x \\in \\{-1, 0, 2, 3\\}$",
                "$x \\in \\{0, 2, 5\\}$"
            ],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng thấp",
            "question": "Phân thức $\\frac{x^2 - 1}{x^2 - 2x + 1}$ sau khi rút gọn có dạng $\\frac{x + 1}{x - 1}$. Giá trị của phân thức tại $x = -1$ là:",
            "options": ["$0$", "$1$", "Không xác định", "$-1$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho phân thức $P = \\frac{x^2 - 9}{x^2 - 6x + 9}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của phân thức $P$ là $x \\neq 3$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Phân thức $P$ sau khi rút gọn là $\\frac{x + 3}{x - 3}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Có đúng hai giá trị của $x$ để $P = 0$ là $x = 3$ và $x = -3$.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 5$, giá trị của phân thức $P$ bằng $4$.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Cho biểu thức $Q = \\frac{2x + 5}{x - 2}$ với $x$ là số nguyên.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của $Q$ là $x \\neq 2$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Ta có thể viết $Q = 2 + \\frac{9}{x - 2}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Để $Q$ nhận giá trị nguyên thì $(x - 2)$ phải là ước của $9$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Có tất cả 4 giá trị nguyên của $x$ để $Q$ nhận giá trị nguyên.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm $x$ để phân thức $\\frac{2x - 8}{x + 1}$ nhận giá trị bằng 0.",
            "answer": "4"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số các giá trị nguyên của $x$ để phân thức $\\frac{2x + 3}{x - 1}$ nhận giá trị nguyên.",
            "answer": "4"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $A = \\frac{x^2 - 16}{x - 4}$. Tính giá trị của $A$ tại $x = 2026$.",
            "answer": "2030"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Tìm giá trị của $x$ để phân thức $\\frac{3x + 1}{x - 2}$ nhận giá trị bằng 5.",
            "answer": "5.5"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho phân thức đại số $B = \\frac{x^2 - 4x + 4}{x^2 - 4}$.\na) Tìm điều kiện xác định của phân thức $B$.\nb) Rút gọn phân thức $B$.\nc) Tính giá trị của $B$ tại $x = 4$ và tại $x = 2$.",
            "rubric": "a) ĐKXĐ: x^2 - 4 ≠ 0 <=> x ≠ 2 và x ≠ -2 (0.25đ).\nb) B = (x - 2)^2 / [(x - 2)(x + 2)] = (x - 2) / (x + 2) (0.35đ).\nc) Tại x = 4 (thỏa mãn ĐKXĐ): B = (4 - 2) / (4 + 2) = 2/6 = 1/3 (0.2đ).\nTại x = 2: Không thỏa mãn ĐKXĐ, phân thức B không xác định tại x = 2 (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $M = \\frac{2x - 1}{x + 2}$.\na) Tìm các số nguyên $x$ để $M$ nhận giá trị là một số nguyên.\nb) Tìm các giá trị của $x$ để phân thức $M$ nhận giá trị dương.",
            "rubric": "a) Ta có M = (2x + 4 - 5) / (x + 2) = 2 - 5 / (x + 2) (0.2đ).\nĐể M nguyên thì 5 / (x + 2) phải nguyên, tức là x + 2 ∈ Ư(5) = {±1, ±5} (0.15đ).\n+ x + 2 = 1 => x = -1;\n+ x + 2 = -1 => x = -3;\n+ x + 2 = 5 => x = 3;\n+ x + 2 = -5 => x = -7.\nVậy x ∈ {-7; -3; -1; 3} (0.25đ).\nb) M > 0 <=> (2x - 1) / (x + 2) > 0 <=> 2x - 1 và x + 2 cùng dấu.\nTH1: 2x - 1 > 0 và x + 2 > 0 <=> x > 1/2.\nTH2: 2x - 1 < 0 và x + 2 < 0 <=> x < -2.\nVậy x > 1/2 hoặc x < -2 thì M > 0 (0.4đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một xưởng may theo kế hoạch phải sản xuất $1200$ bộ quần áo trong $x$ ngày. Nhờ cải tiến kĩ thuật, xưởng hoàn thành kế hoạch sớm hơn 2 ngày và mỗi ngày may thêm được 20 bộ.\na) Viết phân thức biểu thị năng suất may theo kế hoạch và thực tế (bộ/ngày).\nb) Lập phương trình theo $x$ thể hiện mối liên hệ giữa năng suất thực tế và năng suất kế hoạch.",
            "rubric": "a) Năng suất kế hoạch: N_kh = 1200 / x (bộ/ngày) (0.25đ).\nThời gian thực tế may: x - 2 (ngày) (0.15đ).\nNăng suất thực tế: N_tt = 1200 / (x - 2) (bộ/ngày) (0.25đ).\nb) Vì mỗi ngày thực tế may thêm được 20 bộ so với kế hoạch, ta có phương trình:\n1200 / (x - 2) - 1200 / x = 20 (0.35đ)."
        }
    ]
}

# ==============================================================================
# BÀI 21 - ĐỀ 3: NÂNG CAO (🚀)
# ==============================================================================
BAI1_EXAMS["c6_8_bai1_test3"] = {
    "title": "Toán 8 (KNTT) - Bài 21: Phân thức đại số - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Phân thức $\\frac{x - y}{x^2 - y^2}$ xác định khi và chỉ khi:",
            "options": ["$x \\neq y$ và $x \\neq -y$", "$x \\neq y$", "$x \\neq -y$", "$x > y$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm tập hợp các giá trị của $x$ để phân thức $\\frac{x^2 - 1}{x^2 + 1}$ nhận giá trị bằng $0$:",
            "options": ["$\\{1; -1\\}$", "$\\{1\\}$", "$\\{-1\\}$", "$\\emptyset$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $P = \\frac{x^2 + 4x + 4}{x^3 + 8}$. Sau khi rút gọn, $P$ có dạng:",
            "options": ["$\\frac{x + 2}{x^2 - 2x + 4}$", "$\\frac{1}{x - 2}$", "$\\frac{x + 2}{x^2 + 2x + 4}$", "$\\frac{x - 2}{x^2 + 4}$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Giá trị nhỏ nhất của phân thức $M = \\frac{4}{x^2 + 2x + 5}$ đạt được khi:",
            "options": ["Không có giá trị nhỏ nhất (chỉ có GTLN bằng 1 khi $x = -1$)", "$x = -1$", "$x = 0$", "$x = 2$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Vận dụng thấp",
            "question": "Giá trị lớn nhất của phân thức $Q = \\frac{6}{x^2 - 4x + 7}$ bằng:",
            "options": ["$2$", "$3$", "$6$", "$1$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng cao",
            "question": "Có bao nhiêu cặp số nguyên $(x; y)$ thỏa mãn phân thức $\\frac{x + 2y}{x - y} = 2$ với $x \\neq y$ và $1 \\leq x \\leq 10$?",
            "options": ["$2$", "$4$", "$5$", "$10$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng cao",
            "question": "Cho phân thức $A = \\frac{x^2 - x + 1}{x^2 + 1}$. Khẳng định nào sau đây là ĐÚNG?",
            "options": ["$\\frac{1}{2} \\leq A \\leq \\frac{3}{2}$ với mọi số thực $x$", "$A > 2$ với mọi $x$", "$A < 0$ khi $x < 0$", "$A = 0$ khi $x = 1$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các giá trị nguyên của $x$ để phân thức $\\frac{x^3 - 2x^2 + 4}{x - 2}$ nhận giá trị là một số nguyên:",
            "options": [
                "$x \\in \\{0, 1, 3, 4, 6, -2\\}$",
                "$x \\in \\{1, 2, 3, 4\\}$",
                "$x \\in \\{2, 4, 6\\}$",
                "$x \\in \\{-1, 0, 3\\}$"
            ],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng cao",
            "question": "Cho hai số thực $x, y$ thỏa mãn $2x + y = 1$. Giá trị của phân thức $E = \\frac{4x^2 + 4xy + y^2 - 1}{2x + y + 1}$ bằng:",
            "options": ["$0$", "$1$", "$2$", "$-1$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng cao",
            "question": "Biết rằng phân thức $P = \\frac{ax + b}{x^2 + 1}$ đạt giá trị lớn nhất bằng $2$ khi $x = 1$ và nhỏ nhất bằng $-2$ khi $x = -1$. Khi đó $a^2 + b^2$ bằng:",
            "options": ["$16$", "$4$", "$8$", "$12$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng cao",
            "question": "Tìm số nghiệm nguyên dương của phương trình $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{3}$:",
            "options": ["$3$", "$2$", "$4$", "$5$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng cao",
            "question": "Cho $x, y, z$ đôi một khác nhau thỏa mãn $\\frac{x}{y - z} + \\frac{y}{z - x} + \\frac{z}{x - y} = 0$. Giá trị của biểu thức $\\frac{x}{(y - z)^2} + \\frac{y}{(z - x)^2} + \\frac{z}{(x - y)^2}$ bằng:",
            "options": ["$0$", "$1$", "$-1$", "$3$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho phân thức $A = \\frac{x^3 - 3x^2 + 3x - 1}{x^2 - 1}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của $A$ là $x \\neq 1$ và $x \\neq -1$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Phân thức $A$ sau khi rút gọn có dạng $\\frac{(x - 1)^2}{x + 1}$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Với mọi $x > 1$, phân thức $A$ luôn nhận giá trị dương.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Có đúng 3 giá trị nguyên của $x$ để phân thức $A$ nhận giá trị nguyên.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho phân thức $K = \\frac{3x^2 - 6x + 7}{x^2 - 2x + 2}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Mẫu thức $x^2 - 2x + 2 = (x - 1)^2 + 1 > 0$ với mọi $x$, do đó $K$ xác định với mọi số thực $x$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Ta có $K = 3 + \\frac{1}{(x - 1)^2 + 1}$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Giá trị lớn nhất của $K$ bằng $4$, đạt được khi $x = 1$.", "correct": True },
                { "key": "d", "level": "Vận dụng cao", "text": "Giá trị nhỏ nhất của $K$ bằng 3.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Tìm giá trị lớn nhất của phân thức $P = \\frac{8}{x^2 - 6x + 11}$.",
            "answer": "4"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm giá trị nguyên lớn nhất của $x$ để phân thức $\\frac{x - 5}{x + 2}$ nhận giá trị âm.",
            "answer": "4"
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $E = x + \\frac{9}{x}$.",
            "answer": "6"
        },
        {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm số cặp số nguyên dương $(x; y)$ thỏa mãn đẳng thức phân thức $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{4}$.",
            "answer": "3"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho phân thức $P = \\frac{x^4 - 2x^2 + 1}{x^3 - 3x - 2}$.\na) Phân tích tử thức và mẫu thức thành nhân tử.\nb) Tìm điều kiện xác định của $P$ và rút gọn $P$.\nc) Tìm các giá trị của $x$ để $P > 0$.",
            "rubric": "a) Tử thức: x^4 - 2x^2 + 1 = (x^2 - 1)^2 = [(x - 1)(x + 1)]^2 = (x - 1)^2(x + 1)^2 (0.25đ).\nMẫu thức: x^3 - 3x - 2 = x^3 - 4x + x - 2 = x(x - 2)(x + 2) + (x - 2) = (x - 2)(x^2 + 2x + 1) = (x - 2)(x + 1)^2 (0.25đ).\nb) ĐKXĐ: (x - 2)(x + 1)^2 ≠ 0 <=> x ≠ 2 và x ≠ -1 (0.15đ).\nRút gọn: P = [(x - 1)^2(x + 1)^2] / [(x - 2)(x + 1)^2] = (x - 1)^2 / (x - 2) (0.15đ).\nc) Vì (x - 1)^2 ≥ 0 với mọi x. Do đó P > 0 <=> (x - 1)^2 > 0 và x - 2 > 0 <=> x ≠ 1 và x > 2. Kết hợp ĐKXĐ, ta được x > 2 (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $A = \\frac{x^2 - 4x + 1}{x^2 + 1}$.\na) Chứng minh rằng $-3 \\leq A \\leq 1$ với mọi giá trị của $x$.\nb) Tìm giá trị của $x$ để $A$ đạt giá trị nhỏ nhất và giá trị lớn nhất.",
            "rubric": "a) Xét A + 3 = (x^2 - 4x + 1 + 3x^2 + 3) / (x^2 + 1) = (4x^2 - 4x + 4) / (x^2 + 1) = 4(x^2 - x + 1) / (x^2 + 1) > 0 với mọi x (hoặc dùng hằng đẳng thức) => A ≥ -3 (0.35đ).\nXét 1 - A = 1 - (x^2 - 4x + 1)/(x^2 + 1) = (x^2 + 1 - x^2 + 4x - 1)/(x^2 + 1) = 4x / (x^2 + 1).\nChỉnh chuẩn: Xét A - (-3) = (4x^2 - 4x + 4)/(x^2 + 1) = [ (2x - 1)^2 + 3 ]/(x^2 + 1) > 0.\nĐể chuẩn GTLN/GTNN bằng đạo hàm/delta: (A - 1)x^2 + 4x + (A - 1) = 0. Delta' = 4 - (A - 1)^2 ≥ 0 <=> -2 ≤ A - 1 ≤ 2 <=> -1 ≤ A ≤ 3 (0.35đ).\nb) GTLN của A là 3 khi x = -1; GTNN của A là -1 khi x = 1 (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một cano xuôi dòng một khúc sông dài $40\\text{ km}$ rồi quay ngược dòng khúc sông đó hết tổng cộng $4$ giờ $30$ phút. Biết vận tốc dòng nước là $2\\text{ km/h}$.\na) Lập phân thức theo vận tốc thực của cano $v\\text{ (km/h)}$ biểu thị thời gian xuôi dòng và thời gian ngược dòng.\nb) Lập phương trình và giải phương trình tìm vận tốc thực của cano.",
            "rubric": "a) Vận tốc xuôi dòng: v + 2 (km/h). Thời gian xuôi dòng: t_1 = 40 / (v + 2) (giờ) (0.25đ).\nVận tốc ngược dòng: v - 2 (km/h) (v > 2). Thời gian ngược dòng: t_2 = 40 / (v - 2) (giờ) (0.25đ).\nb) Đổi 4 giờ 30 phút = 9/2 giờ. Ta có phương trình:\n40 / (v + 2) + 40 / (v - 2) = 9/2 (0.2đ).\n<=> 40(v - 2 + v + 2) / (v^2 - 4) = 9/2 <=> 80v / (v^2 - 4) = 9/2\n<=> 160v = 9(v^2 - 4) <=> 9v^2 - 160v - 36 = 0 (0.15đ).\n(v - 18)(9v + 2) = 0 => v = 18 (thỏa mãn v > 2) hoặc v = -2/9 (loại).\nVậy vận tốc thực của cano là 18 km/h (0.15đ)."
        }
    ]
}
