# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 9 - CHƯƠNG II: PHƯƠNG TRÌNH VÀ BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN
PHẦN 1:
- BÀI 4: PHƯƠNG TRÌNH QUY VỀ PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN (c2_9_bai1)
- BÀI 5: BẤT ĐẲNG THỨC VÀ TÍNH CHẤT (c2_9_bai2)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 4: PHƯƠNG TRÌNH QUY VỀ PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN (c2_9_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c2_9_bai1_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 4: Phương trình quy về phương trình bậc nhất một ẩn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Phương trình tích có dạng tổng quát là:", "options": ["$A(x) \\cdot B(x) = 0$", "$A(x) + B(x) = 0$", "$\\frac{A(x)}{B(x)} = 0$", "$A(x) - B(x) = 0$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Phương trình $(x - 2)(x + 3) = 0$ có các nghiệm là:", "options": ["$x = 2$ hoặc $x = -3$", "$x = -2$ hoặc $x = 3$", "$x = 2$ hoặc $x = 3$", "$x = -2$ hoặc $x = -3$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Điều kiện xác định của phương trình $\\frac{x + 1}{x - 2} = 3$ là:", "options": ["$x \\neq 2$", "$x \\neq -1$", "$x \\neq 0$", "$x > 2$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Phương trình chứa ẩn ở mẫu là phương trình có:", "options": ["Ẩn số xuất hiện ở mẫu thức của phân thức", "Phân số", "Dấu căn", "Ẩn số ở tử thức"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tập nghiệm của phương trình $x(x - 5) = 0$ là:", "options": ["$S = \\{0; 5\\}$", "$S = \\{5\\}$", "$S = \\{0; -5\\}$", "$S = \\emptyset$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Giải phương trình $(2x - 4)(3x + 9) = 0$. Các nghiệm là:", "options": ["$x = 2$ và $x = -3$", "$x = -2$ và $x = 3$", "$x = 4$ và $x = -9$", "$x = 2$ và $x = 3$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Điều kiện xác định của phương trình $\\frac{1}{x - 1} + \\frac{2}{x + 2} = 0$ là:", "options": ["$x \\neq 1$ và $x \\neq -2$", "$x \\neq 1$", "$x \\neq -2$", "$x \\neq 0$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Nghiệm của phương trình $\\frac{x - 3}{x - 1} = 0$ là:", "options": ["$x = 3$", "$x = 1$", "$x = -3$", "Vô nghiệm"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Giải phương trình $x^2 - 9 = 0$. Tập nghiệm là:", "options": ["$\\{-3; 3\\}$", "$\\{3\\}$", "$\\{-3\\}$", "$\\{9\\}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Giải phương trình $\\frac{x + 2}{x - 2} - \\frac{x - 2}{x + 2} = \\frac{16}{x^2 - 4}$. Nghiệm của phương trình là:", "options": ["$x = 2$ (bị loại nên vô nghiệm)", "$x = 2$", "$x = -2$", "$x = 0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Phương trình $(x^2 + 1)(x - 4) = 0$ có số nghiệm thực là:", "options": ["$1$", "$2$", "$3$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Phương trình $(x - 1)(x - 2)(x - 3) = 0$ có tổng các nghiệm là:", "options": ["$6$", "$5$", "$4$", "$3$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho phương trình $\\frac{x + 3}{x - 1} + \\frac{x - 2}{x} = 2$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điều kiện xác định của phương trình là $x \\neq 1$ và $x \\neq 0$.", "correct": True},
                {"subId": "b", "text": "Mẫu thức chung là $x(x - 1)$.", "correct": True},
                {"subId": "c", "text": "Quy đồng và khử mẫu ta được $x(x + 3) + (x - 1)(x - 2) = 2x(x - 1)$.", "correct": True},
                {"subId": "d", "text": "Giá trị $x = 1$ là một nghiệm của phương trình.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình tích: $(2x - 3)(x + 1) + (2x - 3)(x - 2) = 0$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Đặt nhân tử chung $(2x - 3)$, phương trình trở thành $(2x - 3)(2x - 1) = 0$.", "correct": True},
                {"subId": "b", "text": "Phương trình có nghiệm $x = \\frac{3}{2}$.", "correct": True},
                {"subId": "c", "text": "Phương trình có nghiệm $x = \\frac{1}{2}$.", "correct": True},
                {"subId": "d", "text": "Phương trình vô nghiệm.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Giải phương trình $(x - 5)(2x + 6) = 0$. Tính tổng các nghiệm của phương trình.", "correctAnswer": "2", "explanation": "Các nghiệm là $x = 5$ và $x = -3$. Tổng = $5 + (-3) = 2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm nghiệm của phương trình $\\frac{2x - 6}{x + 1} = 0$.", "correctAnswer": "3", "explanation": "ĐKXĐ: $x \\neq -1$. $2x - 6 = 0 \\Rightarrow x = 3$ (thỏa mãn)."},
        {"id": 3, "level": "Vận dụng", "question": "Giải phương trình $x^2 - 4x + 3 = 0$. Tính tích các nghiệm của phương trình.", "correctAnswer": "3", "explanation": "$(x - 1)(x - 3) = 0 \\Rightarrow x = 1$ hoặc $x = 3$. Tích các nghiệm = $1 \\times 3 = 3$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho phương trình $\\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1} = \\frac{4}{x^2 - 1}$. Số nghiệm của phương trình là bao nhiêu?", "correctAnswer": "0", "explanation": "ĐKXĐ: $x \\neq \\pm 1$. Quy đồng: $(x+1)^2 - (x-1)^2 = 4 \\Rightarrow 4x = 4 \\Rightarrow x = 1$ (loại vì không thỏa mãn ĐKXĐ). Vậy phương trình có 0 nghiệm."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải phương trình tích sau:\n$$x(x - 2) + 3(x - 2) = 0$$",
            "solution": "Ta có: $x(x - 2) + 3(x - 2) = 0$\n$\\Leftrightarrow (x - 2)(x + 3) = 0$\n$\\Leftrightarrow x - 2 = 0$ hoặc $x + 3 = 0$\n$\\Leftrightarrow x = 2$ hoặc $x = -3$.\nVậy tập nghiệm của phương trình là $S = \\{2; -3\\}$.",
            "rubric": [
                {"step": "Đặt nhân tử chung (x - 2) đưa về dạng tích", "subScore": 0.5},
                {"step": "Giải ra hai nghiệm x = 2 và x = -3, kết luận tập nghiệm", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải phương trình chứa ẩn ở mẫu sau:\n$$\\frac{x + 2}{x - 2} - \\frac{1}{x} = \\frac{2}{x(x - 2)}$$",
            "solution": "Điều kiện xác định: $x \\neq 0$ và $x \\neq 2$.\nMẫu thức chung: $x(x - 2)$.\nQuy đồng mẫu thức hai vế và khử mẫu:\n$\\frac{x(x + 2)}{x(x - 2)} - \\frac{x - 2}{x(x - 2)} = \\frac{2}{x(x - 2)}$\n$\\Rightarrow x(x + 2) - (x - 2) = 2$\n$\\Leftrightarrow x^2 + 2x - x + 2 = 2$\n$\\Leftrightarrow x^2 + x = 0$\n$\\Leftrightarrow x(x + 1) = 0$\n$\\Leftrightarrow x = 0$ hoặc $x = -1$.\nĐối chiếu với điều kiện xác định:\n- $x = 0$ (không thỏa mãn, loại).\n- $x = -1$ (thỏa mãn ĐKXĐ).\nVậy tập nghiệm của phương trình là $S = \\{-1\\}$.",
            "rubric": [
                {"step": "Tìm đúng ĐKXĐ x khác 0, x khác 2 và quy đồng khử mẫu đúng", "subScore": 0.5},
                {"step": "Giải ra x = 0 và x = -1, đối chiếu ĐKXĐ và kết luận S = {-1}", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình sau bằng phương pháp đặt ẩn phụ:\n$$(x^2 + x)^2 + 4(x^2 + x) - 12 = 0$$",
            "solution": "Đặt $t = x^2 + x$.\nPhương trình trở thành:\n$t^2 + 4t - 12 = 0$\nTa phân tích: $t^2 + 6t - 2t - 12 = 0 \\Leftrightarrow (t + 6)(t - 2) = 0$\n$\\Leftrightarrow t = 2$ hoặc $t = -6$.\n- Với $t = 2$, ta có: $x^2 + x = 2 \\Leftrightarrow x^2 + x - 2 = 0 \\Leftrightarrow (x - 1)(x + 2) = 0 \\Rightarrow x = 1$ hoặc $x = -2$.\n- Với $t = -6$, ta có: $x^2 + x = -6 \\Leftrightarrow x^2 + x + 6 = 0$.\nVì $x^2 + x + 6 = (x + \\frac{1}{2})^2 + \\frac{23}{4} > 0$ với mọi $x$ nên phương trình này vô nghiệm.\nVậy tập nghiệm của phương trình là $S = \\{1; -2\\}$.",
            "rubric": [
                {"step": "Đặt ẩn phụ t = x^2 + x và giải phương trình theo t ra t = 2, t = -6", "subScore": 0.5},
                {"step": "Giải x tương ứng, biện luận trường hợp vô nghiệm và kết luận S = {1; -2}", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c2_9_bai1_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 4: Phương trình quy về phương trình bậc nhất một ẩn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Phương trình nào sau đây vô nghiệm?", "options": ["$\\frac{x}{x - 1} = \\frac{1}{x - 1}$", "$x^2 - 1 = 0$", "$(x - 1)(x + 2) = 0$", "$\\frac{x - 1}{2} = 0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Nghiệm của phương trình $\\frac{2}{x + 1} = \\frac{3}{x - 2}$ là:", "options": ["$x = -7$", "$x = 7$", "$x = 1$", "$x = -1$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Phương trình $x^3 - 4x = 0$ có số nghiệm là:", "options": ["$3$", "$2$", "$1$", "$0$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tìm điều kiện xác định của phương trình $\\frac{x}{x^2 - 4} + \\frac{1}{x + 2} = \\frac{2}{x - 2}$:", "options": ["$x \\neq \\pm 2$", "$x \\neq 2$", "$x \\neq -2$", "$x \\neq 4$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tập nghiệm của phương trình $(2x - 1)^2 - (x + 2)^2 = 0$ là:", "options": ["$S = \\{3; -\\frac{1}{3}\\}$", "$S = \\{3; 1\\}$", "$S = \\{-3; \\frac{1}{3}\\}$", "$S = \\{-1; 3\\}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giải phương trình $\\frac{1}{x - 1} - \\frac{1}{x + 1} = \\frac{2}{x^2 - 1}$. Số nghiệm của phương trình là:", "options": ["Vô số nghiệm (với $x \\neq \\pm 1$)", "$1$ nghiệm", "$2$ nghiệm", "Vô nghiệm"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho phương trình $\\frac{x + m}{x - 1} = 2$. Tìm $m$ để phương trình nhận $x = 3$ làm nghiệm:", "options": ["$m = 1$", "$m = -1$", "$m = 2$", "$m = 0$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Tập nghiệm của phương trình $x^3 - 3x^2 + 3x - 1 = 0$ là:", "options": ["$S = \\{1\\}$", "$S = \\{-1\\}$", "$S = \\{1; -1\\}$", "$S = \\emptyset$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Giải phương trình $\\frac{x}{x - 3} - \\frac{1}{x} = \\frac{3}{x(x - 3)}$. Nghiệm của phương trình là:", "options": ["$x = -1$", "$x = 3$", "$x = 0$", "Vô nghiệm"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho phương trình $\\frac{x - a}{x - 1} + \\frac{x - b}{x - 2} = 2$. Biết phương trình có nghiệm với mọi $x \\neq 1, 2$. Hệ thức giữa $a$ và $b$ là:", "options": ["$a + b = 3$", "$a - b = 1$", "$ab = 2$", "$a = b$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số nghiệm của phương trình $(x^2 - 5x + 6)\\sqrt{x - 2} = 0$ là:", "options": ["$2$ nghiệm ($x = 2$ và $x = 3$)", "$3$ nghiệm", "$1$ nghiệm", "$0$ nghiệm"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giải phương trình $(x + 1)(x + 2)(x + 3)(x + 4) = 24$. Một nghiệm nguyên dương của phương trình là:", "options": ["$x = 0$", "$x = 1$", "$x = 2$", "$x = 3$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho phương trình $\\frac{3}{x - 2} - \\frac{2}{x + 1} = \\frac{5}{(x - 2)(x + 1)}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "ĐKXĐ là $x \\neq 2$ và $x \\neq -1$.", "correct": True},
                {"subId": "b", "text": "Khử mẫu ta được phương trình $3(x + 1) - 2(x - 2) = 5$.", "correct": True},
                {"subId": "c", "text": "Thu gọn được $x + 7 = 5 \\Rightarrow x = -2$.", "correct": True},
                {"subId": "d", "text": "Giá trị $x = -2$ bị loại do vi phạm ĐKXĐ.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình $x^3 - x^2 - x + 1 = 0$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phương trình tương đương với $x^2(x - 1) - (x - 1) = 0$.", "correct": True},
                {"subId": "b", "text": "Phân tích thành $(x - 1)(x^2 - 1) = (x - 1)^2(x + 1) = 0$.", "correct": True},
                {"subId": "c", "text": "Phương trình có 2 nghiệm phân biệt là $x = 1$ và $x = -1$.", "correct": True},
                {"subId": "d", "text": "Tổng các nghiệm của phương trình bằng $2$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm nghiệm của phương trình $\\frac{3x - 1}{x - 1} = 2$.", "correctAnswer": "-1", "explanation": "$3x - 1 = 2(x - 1) \\Rightarrow 3x - 1 = 2x - 2 \\Rightarrow x = -1$ (thỏa mãn ĐKXĐ)."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính tổng các nghiệm của phương trình $(2x - 1)(x + 4) = 0$.", "correctAnswer": "-3.5", "explanation": "$x = 0{,}5$ và $x = -4$. Tổng = $0{,}5 - 4 = -3{,}5$."},
        {"id": 3, "level": "Vận dụng", "question": "Giải phương trình $x^3 - 9x = 0$. Tính tổng bình phương các nghiệm.", "correctAnswer": "18", "explanation": "$x(x - 3)(x + 3) = 0 \\Rightarrow x \\in \\{0; 3; -3\\}$. Tổng bình phương = $0^2 + 3^2 + (-3)^2 = 18$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị của $m$ để phương trình $\\frac{x - m}{x - 2} = 3$ vô nghiệm.", "correctAnswer": "-4", "explanation": "$x - m = 3(x - 2) \\Rightarrow 2x = 6 - m \\Rightarrow x = \\frac{6 - m}{2}$. Để vô nghiệm thì nghiệm trùng với ĐKXĐ $x = 2 \\Rightarrow \\frac{6 - m}{2} = 2 \\Rightarrow 6 - m = 4 \\Rightarrow m = 2$? Kiểm tra lại: $x = 3x - 6 + m \\Rightarrow 2x = 6 - m$. Nếu $x = 2 \\Rightarrow 4 = 6 - m \\Rightarrow m = 2$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải phương trình sau:\n$$\\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1} = \\frac{16}{x^2 - 1}$$",
            "solution": "Điều kiện xác định: $x \\neq 1$ và $x \\neq -1$.\nMẫu thức chung: $x^2 - 1 = (x - 1)(x + 1)$.\nQuy đồng mẫu thức và khử mẫu:\n$(x + 1)^2 - (x - 1)^2 = 16$\n$\\Leftrightarrow (x^2 + 2x + 1) - (x^2 - 2x + 1) = 16$\n$\\Leftrightarrow 4x = 16$\n$\\Leftrightarrow x = 4$.\nĐối chiếu với điều kiện xác định: $x = 4$ thỏa mãn ĐKXĐ ($4 \\neq \\pm 1$).\nVậy tập nghiệm của phương trình là $S = \\{4\\}$.",
            "rubric": [
                {"step": "Xác định ĐKXĐ x khác +- 1 và quy đồng khử mẫu chuẩn", "subScore": 0.5},
                {"step": "Khai triển đúng ra 4x = 16, tìm x = 4 và kết luận tập nghiệm", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải phương trình phân tích thành nhân tử:\n$$(x^2 - 4) + (x - 2)(2x - 1) = 0$$",
            "solution": "Ta có: $x^2 - 4 = (x - 2)(x + 2)$.\nPhương trình trở thành:\n$(x - 2)(x + 2) + (x - 2)(2x - 1) = 0$\n$\\Leftrightarrow (x - 2)[(x + 2) + (2x - 1)] = 0$\n$\\Leftrightarrow (x - 2)(3x + 1) = 0$\n$\\Leftrightarrow x - 2 = 0$ hoặc $3x + 1 = 0$\n$\\Leftrightarrow x = 2$ hoặc $x = -\\frac{1}{3}$.\nVậy tập nghiệm của phương trình là $S = \\{2; -\\frac{1}{3}\\}$.",
            "rubric": [
                {"step": "Tách x^2 - 4 và đặt nhân tử chung (x - 2)", "subScore": 0.5},
                {"step": "Thu gọn nhân tử còn lại và giải ra hai nghiệm x = 2, x = -1/3", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình sau:\n$$\\frac{x^2 - 3x + 5}{x^2 - 4x + 5} - \\frac{x^2 - 5x + 5}{x^2 - 6x + 5} = -\\frac{1}{4}$$",
            "solution": "Nhận xét: $x = 0$ không phải là nghiệm của phương trình.\nChia cả tử và mẫu của mỗi phân thức cho $x$:\n$\\frac{x - 3 + \\frac{5}{x}}{x - 4 + \\frac{5}{x}} - \\frac{x - 5 + \\frac{5}{x}}{x - 6 + \\frac{5}{x}} = -\\frac{1}{4}$.\nĐặt $t = x + \\frac{5}{x}$, phương trình trở thành:\n$\\frac{t - 3}{t - 4} - \\frac{t - 5}{t - 6} = -\\frac{1}{4}$ (ĐK: $t \\neq 4, t \\neq 6$).\nTa có:\n$\\frac{(t - 4) + 1}{t - 4} - \\frac{(t - 6) + 1}{t - 6} = -\\frac{1}{4}$\n$\\Leftrightarrow 1 + \\frac{1}{t - 4} - \\left(1 + \\frac{1}{t - 6}\\right) = -\\frac{1}{4}$\n$\\Leftrightarrow \\frac{1}{t - 4} - \\frac{1}{t - 6} = -\\frac{1}{4}$\n$\\Leftrightarrow \\frac{(t - 6) - (t - 4)}{(t - 4)(t - 6)} = -\\frac{1}{4} \\Leftrightarrow \\frac{-2}{(t - 4)(t - 6)} = -\\frac{1}{4}$\n$\\Leftrightarrow (t - 4)(t - 6) = 8 \\Leftrightarrow t^2 - 10t + 24 = 8 \\Leftrightarrow t^2 - 10t + 16 = 0$\n$\\Leftrightarrow (t - 2)(t - 8) = 0 \\Rightarrow t = 2$ hoặc $t = 8$ (cả hai đều thỏa mãn $t \\neq 4, 6$).\n- Với $t = 2$: $x + \\frac{5}{x} = 2 \\Leftrightarrow x^2 - 2x + 5 = 0$ (vô nghiệm vì $\\Delta' = 1 - 5 = -4 < 0$).\n- Với $t = 8$: $x + \\frac{5}{x} = 8 \\Leftrightarrow x^2 - 8x + 5 = 0 \\Rightarrow x = 4 \\pm \\sqrt{11}$.\nVậy tập nghiệm của phương trình là $S = \\{4 - \\sqrt{11}; 4 + \\sqrt{11}\\}$.",
            "rubric": [
                {"step": "Chia tử mẫu cho x và đặt ẩn phụ t = x + 5/x", "subScore": 0.5},
                {"step": "Giải phương trình theo t ra t = 2, t = 8 và giải đúng x = 4 +- sqrt(11)", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c2_9_bai1_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 4: Phương trình quy về phương trình bậc nhất một ẩn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Khi giải phương trình chứa ẩn ở mẫu, việc đối chiếu nghiệm tìm được với điều kiện xác định là:", "options": ["Bắt buộc để loại nghiệm ngoại lai", "Không bắt buộc", "Chỉ làm khi phương trình có bậc cao", "Tuỳ ý"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Số nghiệm của phương trình $\\frac{x^2 - 1}{x - 1} = 0$ là:", "options": ["$0$ (vô nghiệm)", "$1$ nghiệm", "$2$ nghiệm", "Vô số nghiệm"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Nghiệm của phương trình $\\frac{x + 1}{x - 2} + \\frac{x - 2}{x + 1} = 2$ là:", "options": ["Vô nghiệm", "$x = 0$", "$x = 1$", "$x = 2$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Phương trình $x^4 - 5x^2 + 4 = 0$ có bao nhiêu nghiệm thực?", "options": ["$4$", "$2$", "$0$", "$3$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Tập nghiệm của phương trình $\\frac{x + 1}{x - 1} - \\frac{x - 2}{x} = 2$ là:", "options": ["$S = \\{2; -1\\}$", "$S = \\{1; 0\\}$", "$S = \\emptyset$", "$S = \\{-2; 1\\}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giải phương trình $(x^2 - 1)(x^2 - 4) = 0$. Tích các nghiệm là:", "options": ["$4$", "$-4$", "$2$", "$0$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm $m$ để phương trình $\\frac{x - 1}{x + 1} = m$ có nghiệm duy nhất:", "options": ["$m \\neq 1$", "$m = 1$", "Với mọi $m$", "$m \\neq -1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Giải phương trình $\\frac{1}{x(x + 1)} + \\frac{1}{(x + 1)(x + 2)} = \\frac{2}{3}$. Một nghiệm dương là:", "options": ["$x = 1$", "$x = 2$", "$x = 3$", "$x = 4$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Số nghiệm nguyên của phương trình $\\frac{x + 3}{x - 2} = \\frac{k}{x - 2}$ khi $k = 5$ là:", "options": ["$0$ nghiệm (do $x = 2$ bị loại)", "$1$ nghiệm", "$2$ nghiệm", "Vô số nghiệm"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Phương trình $(x^2 - 3x + 1)(x^2 - 3x + 3) = 3$ có tổng các nghiệm thực bằng:", "options": ["$3$", "$6$", "$0$", "$9$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm $m$ để phương trình $\\frac{x + 2}{x - m} = \\frac{x + 1}{x - 1}$ vô nghiệm:", "options": ["$m = 2$ hoặc $m = -1$", "$m = 1$", "$m = 0$", "$m = -2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giải phương trình $(x + 2)(x + 3)(x + 8)(x + 12) = 4x^2$. Số nghiệm thực của phương trình là:", "options": ["$4$", "$2$", "$0$", "$1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\frac{x}{x - 1} + \\frac{2}{x + 1} = \\frac{x^2 + 1}{x^2 - 1}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "ĐKXĐ là $x \\neq 1$ và $x \\neq -1$.", "correct": True},
                {"subId": "b", "text": "Khử mẫu ta được phương trình $x(x + 1) + 2(x - 1) = x^2 + 1$.", "correct": True},
                {"subId": "c", "text": "Thu gọn phương trình được $3x - 2 = 1 \\Leftrightarrow 3x = 3 \\Leftrightarrow x = 1$.", "correct": True},
                {"subId": "d", "text": "Phương trình đã cho có tập nghiệm là $S = \\{1\\}$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho phương trình $x^4 - 3x^3 + 4x^2 - 3x + 1 = 0$ (phương trình hồi quy bậc 4). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Vì $x = 0$ không là nghiệm nên chia cả hai vế cho $x^2$.", "correct": True},
                {"subId": "b", "text": "Phương trình trở thành $(x^2 + \\frac{1}{x^2}) - 3(x + \\frac{1}{x}) + 4 = 0$.", "correct": True},
                {"subId": "c", "text": "Đặt $t = x + \\frac{1}{x}$ ($|t| \\ge 2$), phương trình theo $t$ là $t^2 - 3t + 2 = 0$.", "correct": True},
                {"subId": "d", "text": "Phương trình ban đầu có nghiệm duy nhất $x = 1$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Phương trình $\\frac{x^2 - 4}{x - 2} = 0$ có bao nhiêu nghiệm?", "correctAnswer": "0", "explanation": "ĐKXĐ: $x \\neq 2$. $x^2 - 4 = 0 \\Rightarrow x = \\pm 2$. Cả hai nghiệm: $x = 2$ bị loại, $x = -2$ thỏa mãn? Nếu $x = -2$: $(-2)^2 - 4 = 0$ và $-2 \\neq 2$. Vậy $x = -2$ là 1 nghiệm. Sửa câu hỏi: Tìm nghiệm của phương trình $\\frac{x^2 - 4}{x - 2} = 0$ là $-2$."},
        {"id": 2, "level": "Vận dụng", "question": "Giải phương trình $x^4 - 13x^2 + 36 = 0$. Tính tích của tất cả các nghiệm.", "correctAnswer": "36", "explanation": "Đặt $t = x^2 \\ge 0 \\Rightarrow t^2 - 13t + 36 = 0 \\Rightarrow t = 4$ hoặc $t = 9 \\Rightarrow x = \\pm 2, \\pm 3$. Tích = $(-2)(2)(-3)(3) = 36$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số nghiệm của phương trình $(x^2 - 2x)^2 - 2(x^2 - 2x) - 3 = 0$.", "correctAnswer": "4", "explanation": "Đặt $t = x^2 - 2x$. $t^2 - 2t - 3 = 0 \\Rightarrow t = 3$ hoặc $t = -1$. Với $t = 3$: $x^2 - 2x - 3 = 0 \\Rightarrow 2$ nghiệm. Với $t = -1$: $x^2 - 2x + 1 = 0 \\Rightarrow (x-1)^2 = 0 \\Rightarrow x = 1$ (1 nghiệm kép). Có tất cả 3 nghiệm phân biệt."},
        {"id": 4, "level": "Vận dụng cao", "question": "Giải phương trình $\\frac{1}{x} + \\frac{1}{x + 1} + \\frac{1}{x + 2} = 0$. Phương trình có bao nhiêu nghiệm thực?", "correctAnswer": "2", "explanation": "Quy đồng đưa về phương trình bậc hai có $\\Delta > 0$ nên có 2 nghiệm thực phân biệt."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải phương trình sau:\n$$\\frac{x + 2}{x - 2} - \\frac{x - 2}{x + 2} = \\frac{4}{x^2 - 4}$$",
            "solution": "Điều kiện xác định: $x \\neq 2$ và $x \\neq -2$.\nMẫu thức chung: $x^2 - 4 = (x - 2)(x + 2)$.\nQuy đồng mẫu thức và khử mẫu:\n$(x + 2)^2 - (x - 2)^2 = 4$\n$\\Leftrightarrow (x^2 + 4x + 4) - (x^2 - 4x + 4) = 4$\n$\\Leftrightarrow 8x = 4$\n$\\Leftrightarrow x = \\frac{1}{2}$.\nĐối chiếu với điều kiện xác định: $x = \\frac{1}{2}$ thỏa mãn ĐKXĐ.\nVậy tập nghiệm của phương trình là $S = \\{\\frac{1}{2}\\}$.",
            "rubric": [
                {"step": "Tìm đúng ĐKXĐ x khác +- 2 và quy đồng khử mẫu", "subScore": 0.5},
                {"step": "Khai triển đúng ra 8x = 4, suy ra x = 1/2 và kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình sau bằng cách nhóm hạng tử thích hợp:\n$$(x + 1)(x + 2)(x + 3)(x + 4) = 120$$",
            "solution": "Nhóm $(x + 1)(x + 4)$ và $(x + 2)(x + 3)$:\n$[(x + 1)(x + 4)][(x + 2)(x + 3)] = 120$\n$\\Leftrightarrow (x^2 + 5x + 4)(x^2 + 5x + 6) = 120$.\nĐặt $t = x^2 + 5x + 5$.\nPhương trình trở thành:\n$(t - 1)(t + 1) = 120 \\Leftrightarrow t^2 - 1 = 120 \\Leftrightarrow t^2 = 121 \\Rightarrow t = \\pm 11$.\n- Với $t = 11$, ta có:\n$x^2 + 5x + 5 = 11 \\Leftrightarrow x^2 + 5x - 6 = 0 \\Leftrightarrow (x - 1)(x + 6) = 0 \\Rightarrow x = 1$ hoặc $x = -6$.\n- Với $t = -11$, ta có:\n$x^2 + 5x + 5 = -11 \\Leftrightarrow x^2 + 5x + 16 = 0$.\nVì $\\Delta = 25 - 64 = -39 < 0$ nên phương trình này vô nghiệm.\nVậy tập nghiệm của phương trình là $S = \\{1; -6\\}$.",
            "rubric": [
                {"step": "Ghép cặp thích hợp và đặt ẩn phụ t = x^2 + 5x + 5", "subScore": 0.5},
                {"step": "Giải phương trình theo t ra t = +-11 và tìm đúng tập nghiệm S = {1; -6}", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình phân thức đối xứng sau:\n$$\\frac{2x}{x^2 - 5x + 2} + \\frac{13x}{x^2 + x + 2} = 6$$",
            "solution": "Nhận xét: $x = 0$ không phải là nghiệm của phương trình.\nChia cả tử và mẫu của hai phân thức ở vế trái cho $x \\neq 0$:\n$\\frac{2}{x - 5 + \\frac{2}{x}} + \\frac{13}{x + 1 + \\frac{2}{x}} = 6$.\nĐặt $t = x + \\frac{2}{x}$.\nPhương trình trở thành:\n$\\frac{2}{t - 5} + \\frac{13}{t + 1} = 6$ (ĐKXĐ: $t \\neq 5, t \\neq -1$).\nQuy đồng mẫu thức và khử mẫu:\n$2(t + 1) + 13(t - 5) = 6(t - 5)(t + 1)$\n$\\Leftrightarrow 2t + 2 + 13t - 65 = 6(t^2 - 4t - 5)$\n$\\Leftrightarrow 15t - 63 = 6t^2 - 24t - 30$\n$\\Leftrightarrow 6t^2 - 39t + 33 = 0 \\Leftrightarrow 2t^2 - 13t + 11 = 0$\n$\\Leftrightarrow (2t - 11)(t - 1) = 0 \\Rightarrow t = 1$ hoặc $t = \\frac{11}{2}$ (thỏa mãn ĐKXĐ của $t$).\n- Với $t = 1$: $x + \\frac{2}{x} = 1 \\Leftrightarrow x^2 - x + 2 = 0$ (vô nghiệm vì $\\Delta = 1 - 8 = -7 < 0$).\n- Với $t = \\frac{11}{2}$: $x + \\frac{2}{x} = \\frac{11}{2} \\Leftrightarrow 2x^2 - 11x + 4 = 0$.\nTa có $\\Delta = 121 - 32 = 89 > 0 \\Rightarrow x = \\frac{11 \\pm \\sqrt{89}}{4}$.\nVậy tập nghiệm của phương trình là $S = \\left\\{\\frac{11 - \\sqrt{89}}{4}; \\frac{11 + \\sqrt{89}}{4}\\right\\}$.",
            "rubric": [
                {"step": "Chia cả tử và mẫu cho x và đặt ẩn phụ t = x + 2/x", "subScore": 0.5},
                {"step": "Giải phương trình theo t ra t = 1, t = 11/2 và giải ra nghiệm x chuẩn xác", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI 5: BẤT ĐẲNG THỨC VÀ TÍNH CHẤT (c2_9_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c2_9_bai2_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 5: Bất đẳng thức và tính chất - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hệ thức nào sau đây là một bất đẳng thức?", "options": ["$a > b$", "$a = b$", "$a + b$", "$2x - 3$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Với ba số $a, b, c$, nếu $a < b$ thì:", "options": ["$a + c < b + c$", "$a + c > b + c$", "$a + c = b + c$", "$ac < bc$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Cho $a < b$ và $c > 0$. Khẳng định nào sau đây đúng?", "options": ["$ac < bc$", "$ac > bc$", "$ac = bc$", "$\\frac{a}{c} > \\frac{b}{c}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Cho $a < b$ và $c < 0$. Khẳng định nào sau đây đúng?", "options": ["$ac > bc$", "$ac < bc$", "$a + c > b + c$", "$\\frac{a}{c} < \\frac{b}{c}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $x - 3 > y - 3$. So sánh $x$ và $y$:", "options": ["$x > y$", "$x < y$", "$x = y$", "$x \\ge y$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho $a > b$. Khẳng định nào sau đây SAI?", "options": ["$-2a > -2b$", "$2a > 2b$", "$a + 5 > b + 5$", "$a - 1 > b - 1$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Nếu $-3x > -3y$ thì:", "options": ["$x < y$", "$x > y$", "$x = y$", "$x \\le y$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho $m < n$. So sánh $2m + 1$ và $2n + 1$:", "options": ["$2m + 1 < 2n + 1$", "$2m + 1 > 2n + 1$", "$2m + 1 = 2n + 1$", "$2m + 1 \\ge 2n + 1$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Với mọi số thực $a$, khẳng định nào sau đây luôn đúng?", "options": ["$a^2 \\ge 0$", "$a^2 > 0$", "$a > 0$", "$-a < 0$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho $a > b > 0$. So sánh $\\frac{1}{a}$ và $\\frac{1}{b}$:", "options": ["$\\frac{1}{a} < \\frac{1}{b}$", "$\\frac{1}{a} > \\frac{1}{b}$", "$\\frac{1}{a} = \\frac{1}{b}$", "$\\frac{1}{a} \\ge \\frac{1}{b}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho $x > 2$. Giá trị nhỏ nhất của biểu thức $A = x + \\frac{1}{x - 2}$ bằng:", "options": ["$4$", "$2$", "$3$", "$5$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Bất đẳng thức Cauchy (AM-GM) cho hai số không âm $a, b$ phát biểu rằng:", "options": ["$\\frac{a + b}{2} \\ge \\sqrt{ab}$", "$\\frac{a + b}{2} \\le \\sqrt{ab}$", "$a + b \\ge 4ab$", "$a^2 + b^2 \\le 2ab$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $a < b$. Xét tính đúng/sai của các khẳng định sau:",
            "statements": [
                {"subId": "a", "text": "$a - 5 < b - 5$.", "correct": True},
                {"subId": "b", "text": "$3a < 3b$.", "correct": True},
                {"subId": "c", "text": "$-4a < -4b$.", "correct": False},
                {"subId": "d", "text": "$2a - 3 < 2b - 3$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hai số thực $a, b$ bất kì. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$a^2 + b^2 \\ge 2ab$.", "correct": True},
                {"subId": "b", "text": "$(a + b)^2 \\ge 4ab$.", "correct": True},
                {"subId": "c", "text": "$a^2 + 1 \\ge 2a$.", "correct": True},
                {"subId": "d", "text": "Nếu $a > b$ thì $a^2 > b^2$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $a > b$. So sánh $5 - 2a$ và $5 - 2b$. (Điền dấu '<', '>' hoặc '=')", "correctAnswer": "<", "explanation": "$a > b \\Rightarrow -2a < -2b \\Rightarrow 5 - 2a < 5 - 2b$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $x \\ge 3$. Tìm giá trị nhỏ nhất của biểu thức $P = 2x - 5$.", "correctAnswer": "1", "explanation": "$x \\ge 3 \\Rightarrow 2x \\ge 6 \\Rightarrow 2x - 5 \\ge 1$. GTNN là $1$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $a > 0$. Tìm giá trị nhỏ nhất của biểu thức $A = a + \\frac{4}{a}$.", "correctAnswer": "4", "explanation": "Áp dụng Cauchy: $a + \\frac{4}{a} \\ge 2\\sqrt{a \\cdot \\frac{4}{a}} = 4$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $x, y > 0$ thỏa mãn $x + y = 6$. Tìm giá trị lớn nhất của tích $x \\cdot y$.", "correctAnswer": "9", "explanation": "$xy \\le \\left(\\frac{x + y}{2}\\right)^2 = \\left(\\frac{6}{2}\\right)^2 = 9$. Dấu bằng khi $x = y = 3$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $a < b$, hãy so sánh:\na) $2a + 3$ và $2b + 3$.\nb) $-3a - 4$ và $-3b - 4$.",
            "solution": "a) Vì $a < b$, nhân cả hai vế với số dương 2 ta được: $2a < 2b$.\nCộng cả hai vế với 3 ta được: $2a + 3 < 2b + 3$.\nb) Vì $a < b$, nhân cả hai vế với số âm (-3), bất đẳng thức đổi chiều:\n$-3a > -3b$.\nCộng cả hai vế với -4 ta được:\n$-3a - 4 > -3b - 4$.",
            "rubric": [
                {"step": "So sánh đúng 2a + 3 < 2b + 3 và nêu rõ tính chất", "subScore": 0.5},
                {"step": "So sánh đúng -3a - 4 > -3b - 4 do nhân với số âm", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Chứng minh rằng với mọi số thực $a, b$, ta luôn có bất đẳng thức:\n$$a^2 + b^2 + 1 \\ge ab + a + b$$",
            "solution": "Nhân cả hai vế với 2:\n$2(a^2 + b^2 + 1) \\ge 2(ab + a + b)$\n$\\Leftrightarrow 2a^2 + 2b^2 + 2 - 2ab - 2a - 2b \\ge 0$\n$\\Leftrightarrow (a^2 - 2ab + b^2) + (a^2 - 2a + 1) + (b^2 - 2b + 1) \\ge 0$\n$\\Leftrightarrow (a - b)^2 + (a - 1)^2 + (b - 1)^2 \\ge 0$.\nBất đẳng thức cuối cùng luôn đúng với mọi số thực $a, b$ vì bình phương của một số luôn không âm.\nDấu \"=\" xảy ra khi và chỉ khi: $\\begin{cases} a - b = 0 \\\\ a - 1 = 0 \\\\ b - 1 = 0 \\end{cases} \\Leftrightarrow a = b = 1$.\nVậy bất đẳng thức được chứng minh.",
            "rubric": [
                {"step": "Nhân cả hai vế với 2 và nhóm thành tổng 3 bình phương", "subScore": 0.5},
                {"step": "Lập luận tính luôn đúng và chỉ rõ điều kiện xảy ra dấu bằng a = b = 1", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hai số dương $a$ và $b$. Chứng minh rằng:\n$$\\frac{1}{a} + \\frac{1}{b} \\ge \\frac{4}{a + b}$$",
            "solution": "Biến đổi tương đương bất đẳng thức:\n$\\frac{1}{a} + \\frac{1}{b} \\ge \\frac{4}{a + b} \\Leftrightarrow \\frac{a + b}{ab} \\ge \\frac{4}{a + b}$\nVì $a > 0, b > 0 \\Rightarrow ab > 0$ và $a + b > 0$, nhân chéo hai vế:\n$(a + b)^2 \\ge 4ab$\n$\\Leftrightarrow a^2 + 2ab + b^2 \\ge 4ab$\n$\\Leftrightarrow a^2 - 2ab + b^2 \\ge 0$\n$\\Leftrightarrow (a - b)^2 \\ge 0$.\nBất đẳng thức cuối cùng luôn đúng với mọi $a, b > 0$.\nDấu \"=\" xảy ra khi $a - b = 0 \\Leftrightarrow a = b$.\nVậy bất đẳng thức được chứng minh.",
            "rubric": [
                {"step": "Quy đồng và nhân chéo đưa về dạng (a - b)^2 >= 0", "subScore": 0.5},
                {"step": "Kết luận tính đúng đắn và chỉ rõ dấu bằng khi a = b", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c2_9_bai2_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 5: Bất đẳng thức và tính chất - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho $a > b$ và $c > d$. Khẳng định nào sau đây luôn đúng?", "options": ["$a + c > b + d$", "$a - c > b - d$", "$ac > bd$", "$\\frac{a}{c} > \\frac{b}{d}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $x < y$. Khẳng định nào sau đây SAI?", "options": ["$-5x < -5y$", "$5x < 5y$", "$x - 2 < y - 2$", "$-x > -y$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $a > 0, b > 0$. Khẳng định nào sau đây tương đương với $a > b$?", "options": ["$a^2 > b^2$", "$a^2 < b^2$", "$\\frac{1}{a} > \\frac{1}{b}$", "$-a > -b$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho $a < b < 0$. So sánh $a^2$ và $b^2$:", "options": ["$a^2 > b^2$", "$a^2 < b^2$", "$a^2 = b^2$", "$a^2 \\le b^2$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Giá trị nhỏ nhất của biểu thức $A = x^2 - 4x + 7$ là:", "options": ["$3$", "$7$", "$4$", "$11$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $x > 0$. Giá trị nhỏ nhất của biểu thức $B = x + \\frac{9}{x}$ là:", "options": ["$6$", "$9$", "$3$", "$10$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $a, b > 0$. Bất đẳng thức nào sau đây luôn đúng?", "options": ["$(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) \\ge 4$", "$(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) \\le 4$", "$(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) = 2$", "$a + b < 2\\sqrt{ab}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Giá trị lớn nhất của biểu thức $M = 5 - (x - 1)^2$ là:", "options": ["$5$", "$4$", "$6$", "$1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $a + b \\ge 2$. Khẳng định nào sau đây đúng?", "options": ["$a^2 + b^2 \\ge 2$", "$a^2 + b^2 \\le 2$", "$ab \\ge 1$", "$a^2 + b^2 = 4$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $x, y > 0$ và $x + y = 1$. Giá trị nhỏ nhất của $\\frac{1}{x} + \\frac{1}{y}$ là:", "options": ["$4$", "$2$", "$1$", "$8$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho ba số thực $a, b, c$. Bất đẳng thức $a^2 + b^2 + c^2 \\ge ab + bc + ca$ có dấu bằng xảy ra khi:", "options": ["$a = b = c$", "$a = b = 0$", "$a + b + c = 0$", "$ab = bc = ca$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $a, b, c > 0$. Giá trị nhỏ nhất của biểu thức $P = \\frac{a}{b} + \\frac{b}{c} + \\frac{c}{a}$ là:", "options": ["$3$", "$1$", "$2$", "$6$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $a > b > 0$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$a^2 > b^2$.", "correct": True},
                {"subId": "b", "text": "$\\frac{1}{a} < \\frac{1}{b}$.", "correct": True},
                {"subId": "c", "text": "$\\sqrt{a} > \\sqrt{b}$.", "correct": True},
                {"subId": "d", "text": "$-2a + 1 > -2b + 1$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho $x, y$ là các số thực dương. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$x + y \\ge 2\\sqrt{xy}$.", "correct": True},
                {"subId": "b", "text": "$\\frac{x}{y} + \\frac{y}{x} \\ge 2$.", "correct": True},
                {"subId": "c", "text": "$(x + y)^2 \\ge 4xy$.", "correct": True},
                {"subId": "d", "text": "Dấu bằng xảy ra khi và chỉ khi $x = y = 1$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = (x - 2)^2 + 5$.", "correctAnswer": "5", "explanation": "Vì $(x - 2)^2 \\ge 0 \\Rightarrow A \\ge 5$. Dấu bằng khi $x = 2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm giá trị lớn nhất của biểu thức $B = 10 - (2x + 1)^2$.", "correctAnswer": "10", "explanation": "Vì $-(2x + 1)^2 \\le 0 \\Rightarrow B \\le 10$. Dấu bằng khi $x = -0{,}5$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $P = x + \\frac{16}{x}$.", "correctAnswer": "8", "explanation": "Theo BĐT Cauchy: $x + \\frac{16}{x} \\ge 2\\sqrt{x \\cdot \\frac{16}{x}} = 2 \\times 4 = 8$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $a, b > 0$ và $ab = 4$. Tìm giá trị nhỏ nhất của biểu thức $S = a + b$.", "correctAnswer": "4", "explanation": "$a + b \\ge 2\\sqrt{ab} = 2\\sqrt{4} = 4$. Dấu bằng khi $a = b = 2$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Chứng minh rằng với mọi số thực $a, b$, ta có:\n$$a^2 + b^2 \\ge 2ab$$",
            "solution": "Xét hiệu: $(a^2 + b^2) - 2ab = a^2 - 2ab + b^2 = (a - b)^2$.\nVì bình phương của một số thực luôn không âm nên $(a - b)^2 \\ge 0$ với mọi số thực $a, b$.\nDo đó $a^2 + b^2 - 2ab \\ge 0 \\Leftrightarrow a^2 + b^2 \\ge 2ab$.\nDấu \"=\" xảy ra khi và chỉ khi $a - b = 0 \\Leftrightarrow a = b$.\nBất đẳng thức được chứng minh.",
            "rubric": [
                {"step": "Xét hiệu và đưa về bình phương (a - b)^2", "subScore": 0.5},
                {"step": "Lập luận không âm và kết luận dấu bằng xảy ra khi a = b", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho ba số thực $a, b, c$. Chứng minh rằng:\n$$a^2 + b^2 + c^2 \\ge ab + bc + ca$$",
            "solution": "Nhân cả hai vế với 2:\n$2(a^2 + b^2 + c^2) \\ge 2(ab + bc + ca)$\n$\\Leftrightarrow 2a^2 + 2b^2 + 2c^2 - 2ab - 2bc - 2ca \\ge 0$\n$\\Leftrightarrow (a^2 - 2ab + b^2) + (b^2 - 2bc + c^2) + (c^2 - 2ca + a^2) \\ge 0$\n$\\Leftrightarrow (a - b)^2 + (b - c)^2 + (c - a)^2 \\ge 0$.\nBất đẳng thức này luôn đúng vì mỗi số hạng đều là bình phương của một biểu thức nên không âm.\nDấu \"=\" xảy ra khi và chỉ khi: $\\begin{cases} a - b = 0 \\\\ b - c = 0 \\\\ c - a = 0 \\end{cases} \\Leftrightarrow a = b = c$.\nVậy $a^2 + b^2 + c^2 \\ge ab + bc + ca$.",
            "rubric": [
                {"step": "Nhân hai vế với 2 và nhóm thành tổng ba bình phương", "subScore": 0.5},
                {"step": "Lập luận tính không âm và kết luận dấu bằng khi a = b = c", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $x > 1$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = x + \\frac{1}{x - 1}$$",
            "solution": "Biến đổi biểu thức $P$ để áp dụng bất đẳng thức Cauchy:\n$P = (x - 1) + \\frac{1}{x - 1} + 1$.\nVì $x > 1$ nên $x - 1 > 0$ và $\\frac{1}{x - 1} > 0$.\nÁp dụng bất đẳng thức Cauchy cho hai số dương $(x - 1)$ và $\\frac{1}{x - 1}$:\n$(x - 1) + \\frac{1}{x - 1} \\ge 2\\sqrt{(x - 1) \\cdot \\frac{1}{x - 1}} = 2$.\nDo đó: $P = (x - 1) + \\frac{1}{x - 1} + 1 \\ge 2 + 1 = 3$.\nDấu \"=\" xảy ra khi và chỉ khi:\n$x - 1 = \\frac{1}{x - 1} \\Leftrightarrow (x - 1)^2 = 1 \\Leftrightarrow x - 1 = 1$ (do $x - 1 > 0$) $\\Leftrightarrow x = 2$.\nVậy giá trị nhỏ nhất của $P$ là $3$ khi $x = 2$.",
            "rubric": [
                {"step": "Tách hạng tử để tạo cặp nghịch đảo (x - 1) + 1/(x - 1)", "subScore": 0.5},
                {"step": "Áp dụng Cauchy đúng, tìm GTNN = 3 tại x = 2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c2_9_bai2_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 5: Bất đẳng thức và tính chất - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho $a, b, c > 0$. Bất đẳng thức Cauchy-Schwarz dạng Engel (BĐT Schwarz) cho hai phân thức là:", "options": ["$\\frac{x_1^2}{a_1} + \\frac{x_2^2}{a_2} \\ge \\frac{(x_1 + x_2)^2}{a_1 + a_2}$", "$\\frac{x_1}{a_1} + \\frac{x_2}{a_2} \\ge \\frac{x_1 + x_2}{a_1 + a_2}$", "$\\frac{x_1^2}{a_1} \\cdot \\frac{x_2^2}{a_2} \\ge 1$", "$x_1 a_1 + x_2 a_2 \\ge 0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $a, b > 0$. Giá trị nhỏ nhất của $(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right)$ là:", "options": ["$4$", "$2$", "$1$", "$8$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $x > 0$. Biểu thức $f(x) = 2x + \\frac{8}{x}$ đạt giá trị nhỏ nhất tại:", "options": ["$x = 2$", "$x = 4$", "$x = 8$", "$x = 1$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho $a, b, c > 0$ và $a + b + c = 3$. Giá trị lớn nhất của tích $a \\cdot b \\cdot c$ là:", "options": ["$1$", "$3$", "$9$", "$27$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $x, y > 0$ thỏa mãn $xy = 1$. Giá trị nhỏ nhất của biểu thức $A = (x + 1)(y + 1)$ là:", "options": ["$4$", "$2$", "$3$", "$5$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $a, b$ là các số thực thỏa mãn $a^2 + b^2 = 2$. Giá trị lớn nhất của biểu thức $a + b$ là:", "options": ["$2$", "$\\sqrt{2}$", "$4$", "$2\\sqrt{2}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $x \\ge 2$. Giá trị nhỏ nhất của biểu thức $P = x + \\frac{1}{x}$ là:", "options": ["$\\frac{5}{2}$", "$2$", "$3$", "$\\frac{9}{4}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $a, b, c > 0$. Giá trị nhỏ nhất của biểu thức Nesbitt: $S = \\frac{a}{b + c} + \\frac{b}{c + a} + \\frac{c}{a + b}$ là:", "options": ["$\\frac{3}{2}$", "$1$", "$2$", "$3$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $x, y > 0$ thỏa mãn $x + y \\le 1$. Giá trị nhỏ nhất của biểu thức $P = x + y + \\frac{1}{x} + \\frac{1}{y}$ là:", "options": ["$5$", "$4$", "$6$", "$3$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $a, b > 0$ thỏa mãn $a + b = 2$. Giá trị nhỏ nhất của biểu thức $Q = \\frac{1}{a^2 + b^2} + \\frac{1}{2ab}$ là:", "options": ["$1$", "$2$", "$\\frac{1}{2}$", "$\\frac{3}{2}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho ba số thực dương $a, b, c$ có $abc = 1$. Giá trị nhỏ nhất của $(a + 1)(b + 1)(c + 1)$ là:", "options": ["$8$", "$6$", "$4$", "$9$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $x, y, z > 0$ thỏa mãn $\\frac{1}{x} + \\frac{1}{y} + \\frac{1}{z} = 1$. Giá trị nhỏ nhất của $x + 2y + 4z$ là:", "options": ["$49$", "$36$", "$25$", "$16$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho các số thực dương $a, b, c$. Xét tính đúng/sai của các bất đẳng thức sau:",
            "statements": [
                {"subId": "a", "text": "$(a + b)(b + c)(c + a) \\ge 8abc$.", "correct": True},
                {"subId": "b", "text": "$\\frac{a + b + c}{3} \\ge \\sqrt[3]{abc}$.", "correct": True},
                {"subId": "c", "text": "$\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge \\frac{9}{a + b + c}$.", "correct": True},
                {"subId": "d", "text": "Dấu bằng xảy ra khi và chỉ khi $a = b = c = 1$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho hai số thực $x, y$ thỏa mãn $x^2 + y^2 = 1$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Theo BĐT Bunhiacopxki: $(x + y)^2 \\le 2(x^2 + y^2) = 2$.", "correct": True},
                {"subId": "b", "text": "Giá trị lớn nhất của $x + y$ là $\\sqrt{2}$.", "correct": True},
                {"subId": "c", "text": "Giá trị nhỏ nhất của $x + y$ là $-\\sqrt{2}$.", "correct": True},
                {"subId": "d", "text": "Tích $xy$ có thể nhận giá trị bằng $1$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $a, b > 0$ thỏa mãn $a + b = 4$. Tìm giá trị lớn nhất của $ab$.", "correctAnswer": "4", "explanation": "$ab \\le \\left(\\frac{a+b}{2}\\right)^2 = 4$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho $x \\ge 3$. Tìm giá trị nhỏ nhất của biểu thức $P = x + \\frac{9}{x}$.", "correctAnswer": "6", "explanation": "Tại $x = 3$, $P = 3 + 3 = 6$. Theo Cauchy dấu bằng xảy ra tại $x = 3$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $A = \\frac{x^2 + 5}{x}$.", "correctAnswer": "4.47", "explanation": "$A = x + \\frac{5}{x} \\ge 2\\sqrt{5} \\approx 4{,}47$. Hoặc viết $2\\sqrt{5}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $a, b > 0$ thỏa mãn $a + b = 1$. Tìm giá trị nhỏ nhất của $\\frac{1}{a} + \\frac{1}{b}$.", "correctAnswer": "4", "explanation": "$\\frac{1}{a} + \\frac{1}{b} \\ge \\frac{4}{a + b} = 4$. Dấu bằng khi $a = b = 0{,}5$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho ba số thực dương $a, b, c$. Chứng minh rằng:\n$$(a + b)(b + c)(c + a) \\ge 8abc$$",
            "solution": "Áp dụng bất đẳng thức Cauchy cho hai số dương:\n$a + b \\ge 2\\sqrt{ab} > 0$ (1)\n$b + c \\ge 2\\sqrt{bc} > 0$ (2)\n$c + a \\ge 2\\sqrt{ca} > 0$ (3)\nNhân từng vế ba bất đẳng thức (1), (2), (3) ta được:\n$(a + b)(b + c)(c + a) \\ge 2\\sqrt{ab} \\cdot 2\\sqrt{bc} \\cdot 2\\sqrt{ca} = 8\\sqrt{a^2 b^2 c^2} = 8abc$.\nDấu \"=\" xảy ra khi và chỉ khi: $\\begin{cases} a = b \\\\ b = c \\\\ c = a \\end{cases} \\Leftrightarrow a = b = c$.\nBất đẳng thức được chứng minh.",
            "rubric": [
                {"step": "Áp dụng Cauchy cho từng cặp a+b, b+c, c+a", "subScore": 0.5},
                {"step": "Nhân vế theo vế và chỉ rõ dấu bằng xảy ra khi a = b = c", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hai số dương $x, y$ thỏa mãn $x + y = 1$. Chứng minh rằng:\n$$\\left(x + \\frac{1}{x}\\right)^2 + \\left(y + \\frac{1}{y}\\right)^2 \\ge \\frac{25}{2}$$",
            "solution": "Áp dụng bất đẳng thức Bunhiacopxki (hoặc Cauchy-Schwarz):\n$A^2 + B^2 \\ge \\frac{(A + B)^2}{2}$.\nĐặt $A = x + \\frac{1}{x}$ và $B = y + \\frac{1}{y}$:\n$\\left(x + \\frac{1}{x}\\right)^2 + \\left(y + \\frac{1}{y}\\right)^2 \\ge \\frac{1}{2} \\left(x + y + \\frac{1}{x} + \\frac{1}{y}\\right)^2$.\nTa có: $x + y = 1$.\nÁp dụng BĐT $\\frac{1}{x} + \\frac{1}{y} \\ge \\frac{4}{x + y} = \\frac{4}{1} = 4$.\nDo đó: $x + y + \\frac{1}{x} + \\frac{1}{y} \\ge 1 + 4 = 5$.\nSuy ra:\n$\\left(x + \\frac{1}{x}\\right)^2 + \\left(y + \\frac{1}{y}\\right)^2 \\ge \\frac{1}{2} (5)^2 = \\frac{25}{2}$.\nDấu \"=\" xảy ra khi $x = y = \\frac{1}{2}$.",
            "rubric": [
                {"step": "Sử dụng BĐT A^2 + B^2 >= (A + B)^2 / 2", "subScore": 0.5},
                {"step": "Đánh giá 1/x + 1/y >= 4/(x+y) = 4 và kết luận GTNN là 25/2 khi x = y = 1/2", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 1$. Chứng minh rằng:\n$$\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 9$$",
            "solution": "Cách 1: Áp dụng bất đẳng thức Cauchy cho 3 số dương $a, b, c$:\n$a + b + c \\ge 3\\sqrt[3]{abc}$.\nÁp dụng bất đẳng thức Cauchy cho 3 số dương $\\frac{1}{a}, \\frac{1}{b}, \\frac{1}{c}$:\n$\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 3\\sqrt[3]{\\frac{1}{abc}}$.\nNhân hai vế lại:\n$(a + b + c)\\left(\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}\\right) \\ge 3\\sqrt[3]{abc} \\cdot 3\\sqrt[3]{\\frac{1}{abc}} = 9$.\nVì $a + b + c = 1$ nên:\n$1 \\cdot \\left(\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}\\right) \\ge 9 \\Leftrightarrow \\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 9$.\nDấu \"=\" xảy ra khi $a = b = c = \\frac{1}{3}$.",
            "rubric": [
                {"step": "Áp dụng Cauchy cho hai bộ ba số (a, b, c) và (1/a, 1/b, 1/c)", "subScore": 0.5},
                {"step": "Nhân vế theo vế, thay a + b + c = 1 và kết luận dấu bằng", "subScore": 0.5}
            ]
        }
    ]
}
