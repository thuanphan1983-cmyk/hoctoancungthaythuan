# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI - BÀI KIỂM TRA CUỐI CHƯƠNG VI: PHÂN THỨC ĐẠI SỐ (TOÁN 8 - KNTT)
Gồm 3 đề phân hóa:
- Đề 1 (Cơ bản): Kiểm tra toàn diện kiến thức cơ bản của Chương VI (ĐKXĐ, rút gọn, 4 phép tính, tính giá trị).
- Đề 2 (Khá): Biểu thức hữu tỉ tổng hợp, tìm x để biểu thức nguyên, tìm x để biểu thức dương/âm, bài toán thực tế.
- Đề 3 (Nâng cao): Biểu thức phân thức nhiều biến, cực trị phân thức, bất đẳng thức phân thức, bài toán tối ưu.
"""

BAI5_EXAMS = {}

# ==============================================================================
# ÔN TẬP CHƯƠNG VI - ĐỀ 1: CƠ BẢN (🌱)
# ==============================================================================
BAI5_EXAMS["c6_8_bai5_test1"] = {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương VI: Phân thức đại số - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Điều kiện xác định của phân thức $\\frac{x - 3}{x + 5}$ là:",
            "options": ["$x \\neq -5$", "$x \\neq 3$", "$x \\neq 5$", "$x \\neq 0$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Phân thức $\\frac{x - 1}{x + 1}$ bằng phân thức nào sau đây?",
            "options": ["$\\frac{1 - x}{-x - 1}$", "$\\frac{1 - x}{x + 1}$", "$\\frac{x - 1}{-x - 1}$", "$\\frac{x + 1}{x - 1}$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Nhận biết",
            "question": "Rút gọn phân thức $\\frac{4x^2y}{6xy^2}$ ta được kết quả là:",
            "options": ["$\\frac{2x}{3y}$", "$\\frac{2y}{3x}$", "$\\frac{2x^2}{3y^2}$", "$\\frac{4x}{6y}$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Nhận biết",
            "question": "Phân thức đối của phân thức $\\frac{x}{x - 2}$ là:",
            "options": ["$\\frac{x}{2 - x}$", "$\\frac{-x}{2 - x}$", "$\\frac{x}{x + 2}$", "$\\frac{-x}{-x - 2}$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Nhận biết",
            "question": "Phân thức nghịch đảo của phân thức $\\frac{2x + 1}{x - 3}$ ($x \\neq 3, x \\neq -\\frac{1}{2}$) là:",
            "options": ["$\\frac{x - 3}{2x + 1}$", "$\\frac{3 - x}{2x + 1}$", "$-\\frac{2x + 1}{x - 3}$", "$\\frac{2x - 1}{x + 3}$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Nhận biết",
            "question": "Mẫu thức chung của hai phân thức $\\frac{1}{x - 1}$ và $\\frac{1}{x + 1}$ là:",
            "options": ["$x^2 - 1$", "$x - 1$", "$x + 1$", "$2x$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{x^2}{x + 2} + \\frac{4x + 4}{x + 2}$ với $x \\neq -2$ ta được:",
            "options": ["$x + 2$", "$x - 2$", "$1$", "$\\frac{(x + 2)^2}{x + 2}$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $\\frac{2x - 3}{x - 1} - \\frac{x - 2}{x - 1}$ với $x \\neq 1$ ta được:",
            "options": ["$1$", "$-1$", "$\\frac{x - 5}{x - 1}$", "$\\frac{3x - 5}{x - 1}$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Thực hiện phép nhân $\\frac{x^2 - 9}{x} \\cdot \\frac{3x}{x + 3}$ với $x \\neq 0, x \\neq -3$ ta được:",
            "options": ["$3(x - 3)$", "$x - 3$", "$3(x + 3)$", "$3x(x - 3)$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Thực hiện phép chia $\\frac{x - 2}{x + 1} : \\frac{x - 2}{x^2 - 1}$ với $x \\neq \\pm 1, x \\neq 2$ ta được:",
            "options": ["$x - 1$", "$x + 1$", "$\\frac{1}{x - 1}$", "$1$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Giá trị của phân thức $P = \\frac{x^2 - 16}{x - 4}$ tại $x = 16$ bằng:",
            "options": ["$20$", "$12$", "$16$", "$24$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Tìm $x$ để phân thức $\\frac{2x - 6}{x + 1}$ nhận giá trị bằng $0$:",
            "options": ["$x = 3$", "$x = -3$", "$x = -1$", "$x = 0$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A = \\left(\\frac{1}{x - 2} - \\frac{1}{x + 2}\\right) \\cdot \\frac{x^2 - 4}{4}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của biểu thức $A$ là $x \\neq 2$ và $x \\neq -2$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Quy đồng trong ngoặc ta được $\\frac{(x + 2) - (x - 2)}{x^2 - 4} = \\frac{4}{x^2 - 4}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Biểu thức $A$ sau khi rút gọn nhận giá trị không đổi bằng $1$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tại $x = 2$, giá trị của biểu thức $A$ bằng $1$.", "correct": False }
            ]
        },
        {
            "id": 2,
            "stem": "Cho phân thức $B = \\frac{2x + 6}{x^2 - 9}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của $B$ là $x \\neq 3$ và $x \\neq -3$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Rút gọn phân thức ta được $B = \\frac{2}{x - 3}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Để $B = 1$ thì $x = 5$ (thỏa mãn điều kiện xác định).", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Với mọi $x > 3$, phân thức $B$ luôn nhận giá trị âm.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của phân thức $P = \\frac{x^2 - 4x + 4}{x - 2}$ tại $x = 102$.",
            "answer": "100"
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm giá trị của $x$ để phân thức $\\frac{4x - 12}{x + 5}$ có giá trị bằng 0.",
            "answer": "3"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tính giá trị của biểu thức $M = \\frac{x}{x - 3} + \\frac{3}{3 - x}$ tại $x = 2026$.",
            "answer": "1"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Tìm số các giá trị nguyên của $x$ để phân thức $\\frac{6}{x - 1}$ nhận giá trị là một số nguyên.",
            "answer": "8"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\left(\\frac{x}{x - 2} - \\frac{2}{x + 2}\\right) : \\frac{x^2 + 4}{x^2 - 4}$.\na) Tìm điều kiện xác định của $P$.\nb) Rút gọn biểu thức $P$.\nc) Tính giá trị của $P$ tại $x = 3$.",
            "rubric": "a) ĐKXĐ: x ≠ 2 và x ≠ -2 (0.25đ).\nb) Quy đồng trong ngoặc:\nx/(x - 2) - 2/(x + 2) = [x(x + 2) - 2(x - 2)] / (x^2 - 4) = (x^2 + 2x - 2x + 4) / (x^2 - 4) = (x^2 + 4) / (x^2 - 4) (0.35đ).\nThực hiện phép chia: P = [(x^2 + 4) / (x^2 - 4)] : [(x^2 + 4) / (x^2 - 4)] = 1 (0.25đ).\nc) Tại x = 3 (thỏa mãn ĐKXĐ), P = 1 (0.15đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $A = \\frac{x^2 - 6x + 9}{x^2 - 9} + \\frac{1}{x + 3}$.\na) Rút gọn biểu thức $A$.\nb) Tìm giá trị của $x$ để $A = 2$.",
            "rubric": "a) ĐKXĐ: x ≠ 3 và x ≠ -3 (0.15đ).\nRút gọn phân thức thứ nhất: (x - 3)^2 / [(x - 3)(x + 3)] = (x - 3) / (x + 3) (0.25đ).\nA = (x - 3)/(x + 3) + 1/(x + 3) = (x - 2) / (x + 3) (0.3đ).\nb) Cho A = 2 <=> (x - 2)/(x + 3) = 2 <=> x - 2 = 2(x + 3) <=> x - 2 = 2x + 6 <=> x = -8 (thỏa mãn ĐKXĐ). Vậy x = -8 (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một ô tô đi từ A đến B với vận tốc $45\\text{ km/h}$, rồi từ B quay về A với vận tốc $x\\text{ (km/h)}$. Biết quãng đường AB dài $90\\text{ km}$.\na) Viết phân thức biểu thị tổng thời gian cả đi và về của ô tô theo $x$.\nb) Tính tổng thời gian nếu vận tốc lúc về là $x = 60\\text{ km/h}$.",
            "rubric": "a) Thời gian lúc đi: 90 / 45 = 2 (giờ) (0.25đ).\nThời gian lúc về: 90 / x (giờ) (0.25đ).\nTổng thời gian: T = 2 + 90 / x = (2x + 90) / x (giờ) (0.25đ).\nb) Khi x = 60 km/h:\nT = 2 + 90 / 60 = 2 + 1.5 = 3.5 (giờ) (0.25đ)."
        }
    ]
}

# ==============================================================================
# ÔN TẬP CHƯƠNG VI - ĐỀ 2: KHÁ (🌿)
# ==============================================================================
BAI5_EXAMS["c6_8_bai5_test2"] = {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương VI: Phân thức đại số - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Điều kiện xác định của phân thức $P = \\frac{2x - 1}{x^3 - 4x}$ là:",
            "options": ["$x \\neq 0, x \\neq 2, x \\neq -2$", "$x \\neq 2, x \\neq -2$", "$x \\neq 0, x \\neq 4$", "$x \\neq 0$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Rút gọn phân thức $\\frac{x^3 - 3x^2 + 3x - 1}{x - 1}$ với $x \\neq 1$ ta được:",
            "options": ["$(x - 1)^2$", "$x^2 - 1$", "$x - 1$", "$(x + 1)^2$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Biểu thức $M = \\frac{x + 1}{x - 2} - \\frac{x - 1}{x + 2} - \\frac{8}{x^2 - 4}$ rút gọn được kết quả là:",
            "options": ["$\\frac{6x - 8}{x^2 - 4}$", "$\\frac{6x}{x^2 - 4}$", "$\\frac{2x - 8}{x^2 - 4}$", "$1$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Thông hiểu",
            "question": "Tìm $x$ để phân thức $\\frac{x^2 - 25}{x - 5}$ nhận giá trị bằng $12$:",
            "options": ["$x = 7$", "$x = 5$", "$x = 12$", "Không có $x$ nào"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = \\left(\\frac{x}{x^2 - 1}\\right) : \\left(\\frac{1}{x - 1} - \\frac{1}{x + 1}\\right)$. Rút gọn $A$ ta được:",
            "options": ["$\\frac{x}{2}$", "$2x$", "$x$", "$\\frac{1}{2}$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng thấp",
            "question": "Tìm các giá trị nguyên của $x$ để phân thức $\\frac{2x + 7}{x + 2}$ nhận giá trị nguyên:",
            "options": ["$x \\in \\{-5, -3, -1, 1\\}$", "$x \\in \\{-1, 1\\}$", "$x \\in \\{1, 2, 3\\}$", "$x \\in \\{0, 1\\}$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng thấp",
            "question": "Cho $P = \\frac{x - 2}{x + 3}$. Tìm $x$ để $P < 0$:",
            "options": ["$-3 < x < 2$", "$x > 2$", "$x < -3$", "$x \\leq -3$ hoặc $x \\geq 2$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng thấp",
            "question": "Biết rằng $\\frac{1}{x(x + 1)} = \\frac{a}{x} + \\frac{b}{x + 1}$. Giá trị của $a - b$ bằng:",
            "options": ["$2$", "$0$", "$1$", "$-2$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng thấp",
            "question": "Giá trị nhỏ nhất của phân thức $Q = \\frac{5}{x^2 - 2x + 3}$ là:",
            "options": ["Không có GTNN (GTLN bằng $\\frac{5}{2}$ khi $x = 1$)", "$\\frac{5}{2}$", "$1$", "$5$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng thấp",
            "question": "Biểu thức $K = \\left(1 - \\frac{2}{x + 1}\\right) \\cdot \\left(\\frac{x^2 + 1}{x - 1} + 1\\right)$ với $x \\neq \\pm 1$ rút gọn bằng:",
            "options": ["$x$", "$x - 1$", "$x + 1$", "$1$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng thấp",
            "question": "Hai vòi nước cùng chảy vào bể cạn thì sau 6 giờ đầy bể. Nếu vòi 1 chảy một mình mất $x$ giờ đầy bể ($x > 6$) thì trong 1 giờ vòi 2 chảy được:",
            "options": ["$\\frac{1}{6} - \\frac{1}{x}$ bể", "$\\frac{1}{x} - \\frac{1}{6}$ bể", "$\\frac{x - 6}{6}$ bể", "$\\frac{6}{x}$ bể"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng thấp",
            "question": "Cho phân thức $M = \\frac{x^2 - 4x + 3}{x^2 - 1}$. Giá trị của $M$ tại $x = 99$ bằng:",
            "options": ["$\\frac{48}{50} = 0.96$", "$\\frac{96}{100} = 0.96$", "$\\frac{97}{100}$", "$1$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $P = \\left(\\frac{x + 2}{x^2 - 9} - \\frac{1}{x + 3}\\right) : \\frac{5}{x^2 + 3x}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của biểu thức là $x \\neq 0, x \\neq 3, x \\neq -3$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Biểu thức trong ngoặc quy đồng được kết quả là $\\frac{5}{x^2 - 9}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Kết quả rút gọn của biểu thức $P$ là $P = \\frac{x}{x - 3}$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Để $P = 2$ thì $x = 6$ (thỏa mãn điều kiện xác định).", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Cho phân thức $A = \\frac{3x - 2}{x - 1}$ với $x$ là số nguyên khác 1.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Ta có thể phân tích $A = 3 + \\frac{1}{x - 1}$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Để $A$ nhận giá trị nguyên thì $x - 1 \\in \\{1; -1\\}$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Các giá trị nguyên của $x$ để $A$ nguyên là $x = 0$ và $x = 2$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tổng các giá trị nguyên của $x$ để $A$ nguyên bằng $3$.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $P = \\frac{x^2 - 1}{x^2 - 2x + 1}$ tại $x = 21$.",
            "answer": "1.1"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số các giá trị nguyên của $x$ để phân thức $\\frac{x + 5}{x + 1}$ nhận giá trị nguyên.",
            "answer": "6"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $A = \\left(\\frac{x}{x - 1} - 1\\right) : \\frac{1}{x^2 - 1}$. Tính giá trị của $A$ tại $x = 19$.",
            "answer": "20"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Tìm giá trị lớn nhất của phân thức $M = \\frac{12}{x^2 - 4x + 7}$.",
            "answer": "4"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\left(\\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1}\\right) : \\frac{4x}{x^2 - 1}$.\na) Tìm điều kiện xác định của $P$.\nb) Rút gọn biểu thức $P$.\nc) Tìm giá trị của $P$ khi $x = 2026$.",
            "rubric": "a) ĐKXĐ: x ≠ 0, x ≠ 1, x ≠ -1 (0.25đ).\nb) Tử thức:\n(x + 1)/(x - 1) - (x - 1)/(x + 1) = [(x + 1)^2 - (x - 1)^2] / (x^2 - 1) = 4x / (x^2 - 1) (0.35đ).\nThực hiện phép chia:\nP = [4x / (x^2 - 1)] : [4x / (x^2 - 1)] = 1 (0.25đ).\nc) Tại x = 2026 (thỏa mãn ĐKXĐ), P = 1 (0.15đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho biểu thức $B = \\frac{x}{x + 2} + \\frac{2}{x - 2} - \\frac{4x}{x^2 - 4}$.\na) Rút gọn biểu thức $B$.\nb) Tìm các giá trị của $x$ để $B > 0$.\nc) Tìm các giá trị nguyên của $x$ để $B$ nhận giá trị nguyên.",
            "rubric": "a) ĐKXĐ: x ≠ 2 và x ≠ -2. MTC = x^2 - 4 (0.15đ).\nTử = x(x - 2) + 2(x + 2) - 4x = (x^2 - 2x) + (2x + 4) - 4x = x^2 - 4x + 4 = (x - 2)^2 (0.25đ).\nRút gọn: B = (x - 2)^2 / [(x - 2)(x + 2)] = (x - 2) / (x + 2) (0.2đ).\nb) B > 0 <=> (x - 2)/(x + 2) > 0 <=> x > 2 hoặc x < -2 (0.2đ).\nc) B = (x + 2 - 4)/(x + 2) = 1 - 4/(x + 2). Để B nguyên thì x + 2 ∈ Ư(4) = {±1, ±2, ±4}.\nTìm được x ∈ {-6, -4, -3, -1, 0, 2}. Kết hợp ĐKXĐ (x ≠ ±2) ta được x ∈ {-6; -4; -3; -1; 0} (0.2đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một xưởng theo kế hoạch cần gia công $1500$ sản phẩm trong thời gian quy định. Khi thực hiện, mỗi ngày xưởng làm thêm được $10$ sản phẩm nên đã hoàn thành sớm hơn $5$ ngày so với kế hoạch.\na) Gọi số ngày theo kế hoạch là $x$ (ngày, $x > 5$). Hãy viết phân thức biểu thị năng suất kế hoạch và thực tế.\nb) Lập phương trình biểu thị mối liên hệ và tính số ngày dự định hoàn thành theo kế hoạch.",
            "rubric": "a) Năng suất kế hoạch: N_kh = 1500 / x (sản phẩm/ngày) (0.25đ).\nThời gian thực tế: x - 5 (ngày).\nNăng suất thực tế: N_tt = 1500 / (x - 5) (sản phẩm/ngày) (0.25đ).\nb) Vì mỗi ngày làm thêm 10 sản phẩm nên ta có phương trình:\n1500 / (x - 5) - 1500 / x = 10 (0.2đ).\n<=> 150 / (x - 5) - 150 / x = 1 <=> 150x - 150(x - 5) = x(x - 5)\n<=> 750 = x^2 - 5x <=> x^2 - 5x - 750 = 0 (0.15đ).\n(x - 30)(x + 25) = 0 => x = 30 (thỏa mãn x > 5) hoặc x = -25 (loại).\nVậy thời gian dự định là 30 ngày (0.15đ)."
        }
    ]
}

# ==============================================================================
# ÔN TẬP CHƯƠNG VI - ĐỀ 3: NÂNG CAO (🚀)
# ==============================================================================
BAI5_EXAMS["c6_8_bai5_test3"] = {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương VI: Phân thức đại số - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho ba số thực $a, b, c$ khác 0 thỏa mãn $a + b + c = 0$. Giá trị của biểu thức $P = \\frac{ab}{a^2 + b^2 - c^2} + \\frac{bc}{b^2 + c^2 - a^2} + \\frac{ca}{c^2 + a^2 - b^2}$ bằng:",
            "options": ["$-\\frac{3}{2}$", "$\\frac{3}{2}$", "$0$", "$1$"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $A = \\left(\\frac{x}{x^2 - 4} + \\frac{2}{2 - x} + \\frac{1}{x + 2}\\right) : \\left(x - 2 + \\frac{10 - x^2}{x + 2}\\right)$ với $x$ thỏa mãn ĐKXĐ ta được:",
            "options": ["$-\\frac{1}{x - 2}$", "$\\frac{1}{x - 2}$", "$\\frac{1}{x + 2}$", "$1$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho $x > 0$. Giá trị nhỏ nhất của biểu thức $P = \\frac{x^2 + 2025}{x}$ bằng:",
            "options": ["$2\\sqrt{2025} = 90$", "$45$", "$2025$", "$180$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Cho $x, y$ thỏa mãn $x^2 + y^2 = 1$. Giá trị lớn nhất của phân thức $M = \\frac{2xy}{x^2 + 2xy + y^2 + 1}$ là:",
            "options": ["$\\frac{1}{2}$", "$1$", "$\\frac{1}{4}$", "$\\frac{2}{3}$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Vận dụng thấp",
            "question": "Tính tổng $S = \\frac{1}{1 \\cdot 2 \\cdot 3} + \\frac{1}{2 \\cdot 3 \\cdot 4} + \\dots + \\frac{1}{n(n + 1)(n + 2)}$ theo $n$:",
            "options": [
                "$\\frac{n(n + 3)}{4(n + 1)(n + 2)}$",
                "$\\frac{1}{4(n + 1)(n + 2)}$",
                "$\\frac{n}{2(n + 1)(n + 2)}$",
                "$\\frac{n(n + 1)}{2(n + 2)}$"
            ],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các cặp số nguyên $(x; y)$ thỏa mãn đẳng thức phân thức $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{2}$ với $x \\leq y$:",
            "options": [
                "$(x; y) \\in \\{(3; 6), (4; 4), (1; -2), (-2; 1)\\}$",
                "$(x; y) \\in \\{(3; 6), (4; 4)\\}$",
                "$(x; y) \\in \\{(2; 2), (4; 4)\\}$",
                "$(x; y) \\in \\{(1; 2), (2; 4)\\}$"
            ],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng cao",
            "question": "Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Giá trị nhỏ nhất của biểu thức $P = \\frac{a^2}{b + 1} + \\frac{b^2}{c + 1} + \\frac{c^2}{a + 1}$ bằng:",
            "options": ["$\\frac{3}{2}$", "$3$", "$1$", "$2$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng cao",
            "question": "Cho $x, y, z$ đôi một khác nhau thỏa mãn $\\frac{x}{y - z} + \\frac{y}{z - x} + \\frac{z}{x - y} = 0$. Khẳng định nào sau đây là ĐÚNG?",
            "options": [
                "Trong ba phân thức trên, ít nhất có một phân thức nhận giá trị âm và một phân thức nhận giá trị dương",
                "Cả ba phân thức đều cùng bằng 0",
                "Tích của ba phân thức bằng 1",
                "Tổng bình phương của ba phân thức bằng 0"
            ],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị lớn nhất của biểu thức $A = \\frac{x}{(x + 2026)^2}$ với $x > 0$:",
            "options": ["$\\frac{1}{8104}$", "$\\frac{1}{2026}$", "$\\frac{1}{4052}$", "$\\frac{1}{1013}$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực $a, b, c$ đôi một khác nhau. Giá trị của biểu thức $S = \\frac{(a + b)^2}{(a - b)^2} + \\frac{(b + c)^2}{(b - c)^2} + \\frac{(c + a)^2}{(c - a)^2}$ luôn thỏa mãn:",
            "options": ["$S \\geq 2$", "$S \\geq 0$", "$S \\leq 1$", "$S = 3$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng cao",
            "question": "Tìm số nghiệm nguyên của phương trình $\\frac{x^2 - 3x + 2}{x - 1} = 0$:",
            "options": ["$1$", "$2$", "$0$", "Vô số"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng cao",
            "question": "Cho $x + \\frac{1}{x} = a$. Biểu thức $\\frac{x^6 + 1}{x^3}$ biểu diễn theo $a$ là:",
            "options": ["$a^3 - 3a$", "$a^3 + 3a$", "$a^3 - 1$", "$a(a^2 - 1)$"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $P = \\left(\\frac{x^2 + 3}{x^3 + 3x^2 + x + 3} + \\frac{1}{x^2 + 1}\\right) : \\left(\\frac{x - 2}{x^2 - x - 6}\\right)$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Mẫu thức $x^3 + 3x^2 + x + 3$ phân tích thành $(x + 3)(x^2 + 1)$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Điều kiện xác định của $P$ là $x \\neq 2, x \\neq 3, x \\neq -3, x \\neq -2$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Biểu thức $P$ sau khi rút gọn tối giản có dạng $P = \\frac{2}{x^2 + 1}$.", "correct": False },
                { "key": "d", "level": "Vận dụng cao", "text": "Kết quả rút gọn thực sự là $P = \\frac{2(x - 3)}{x^2 + 1}$.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 1$. Xét biểu thức $E = \\frac{a}{1 + bc} + \\frac{b}{1 + ca} + \\frac{c}{1 + ab}$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Ta có $bc \\leq \\frac{(b + c)^2}{4} = \\frac{(1 - a)^2}{4}$.", "correct": True },
                { "key": "b", "level": "Vận dụng cao", "text": "Mẫu số $1 + bc \\leq 1 + \\frac{1}{4} = \\frac{5}{4}$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Biểu thức $E$ luôn thỏa mãn $E \\geq \\frac{3}{4}$.", "correct": False },
                { "key": "d", "level": "Vận dụng cao", "text": "Khi $a = b = c = \\frac{1}{3}$, giá trị của $E$ bằng $\\frac{9}{10}$.", "correct": True }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $A = x + \\frac{16}{x}$.",
            "answer": "8"
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị lớn nhất của phân thức $P = \\frac{x^2}{x^4 + 1}$.",
            "answer": "0.5"
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $a, b, c$ khác 0 thỏa mãn $a + b + c = 0$. Tính giá trị của biểu thức $M = \\frac{a^3 + b^3 + c^3}{abc}$.",
            "answer": "3"
        },
        {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm số nghiệm nguyên dương của phương trình $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{5}$.",
            "answer": "3"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $A = \\left(\\frac{x + 2}{x^2 - 2x + 1} - \\frac{x - 2}{x^2 - 1}\\right) : \\frac{4x}{x^2 - 1}$.\na) Tìm điều kiện xác định của biểu thức $A$.\nb) Rút gọn biểu thức $A$.\nc) Tìm các giá trị của $x$ để $A < 0$.",
            "rubric": "a) ĐKXĐ: x ≠ 0, x ≠ 1, x ≠ -1 (0.25đ).\nb) Quy đồng trong ngoặc với MTC = (x - 1)^2(x + 1):\nTử = (x + 2)(x + 1) - (x - 2)(x - 1) = (x^2 + 3x + 2) - (x^2 - 3x + 2) = 6x (0.35đ).\nThực hiện phép chia:\nA = [6x / ((x - 1)^2(x + 1))] * [(x - 1)(x + 1) / (4x)] = 6 / [4(x - 1)] = 3 / [2(x - 1)] (0.25đ).\nc) A < 0 <=> 3 / [2(x - 1)] < 0 <=> x - 1 < 0 <=> x < 1.\nKết hợp ĐKXĐ: x < 1, x ≠ 0, x ≠ -1 (0.15đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực $a, b, c$ khác nhau từng đôi một.\nChứng minh rằng:\n$S = \\frac{bc}{(a - b)(a - c)} + \\frac{ca}{(b - c)(b - a)} + \\frac{ab}{(c - a)(c - b)} = 1$.",
            "rubric": "- Mẫu thức chung là (a - b)(b - c)(c - a) (0.25đ).\n- Biến đổi từng phân thức:\nP_1 = -bc(b - c) / MTC\nP_2 = -ca(c - a) / MTC\nP_3 = -ab(a - b) / MTC (0.35đ).\n- Tử thức = -[bc(b - c) + ca(c - a) + ab(a - b)] (0.15đ).\n- Phân tích tử thức thành nhân tử:\nbc(b - c) + ca(c - a) + ab(a - b) = -(a - b)(b - c)(c - a) (0.15đ).\n- Do đó Tử thức = (a - b)(b - c)(c - a) = MTC.\nSuy ra S = MTC / MTC = 1 (đpcm) (0.1đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho hai số thực $x, y$ thỏa mãn $x > 0, y > 0$ và $x + y = 1$.\nTìm giá trị nhỏ nhất của biểu thức:\n$P = \\frac{1}{x^2 + y^2} + \\frac{1}{2xy}$.",
            "rubric": "- Biến đổi biểu thức:\nP = 1/(x^2 + y^2) + 1/(2xy) (0.1đ).\n- Áp dụng bất đẳng thức 1/A + 1/B ≥ 4/(A + B) với A, B > 0:\n1/(x^2 + y^2) + 1/(2xy) ≥ 4 / (x^2 + y^2 + 2xy) = 4 / (x + y)^2 (0.45đ).\n- Vì x + y = 1 nên P ≥ 4 / 1^2 = 4 (0.25đ).\n- Dấu '=' xảy ra khi x^2 + y^2 = 2xy <=> (x - y)^2 = 0 <=> x = y.\nKết hợp x + y = 1 ta được x = y = 1/2 (thỏa mãn x, y > 0) (0.15đ).\n- Vậy giá trị nhỏ nhất của P là 4 khi x = y = 1/2 (0.05đ)."
        }
    ]
}
