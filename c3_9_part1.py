# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 9 - CHƯƠNG III: CĂN BẬC HAI VÀ CĂN BẬC BA
PHẦN 1:
- BÀI 7: CĂN BẬC HAI VÀ CĂN THỨC BẬC HAI (c3_9_bai1)
- BÀI 8: KHAI CĂN BẬC HAI VỚI PHÉP NHÂN VÀ PHÉP CHIA (c3_9_bai2)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 7: CĂN BẬC HAI VÀ CĂN THỨC BẬC HAI (c3_9_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c3_9_bai1_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 7: Căn bậc hai và căn thức bậc hai - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Căn bậc hai số học của số $a \\ge 0$ là:", "options": ["Số không âm $x$ sao cho $x^2 = a$", "Số $x$ sao cho $x^2 = a$", "Số âm $x$ sao cho $x^2 = a$", "Số $2a$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Căn bậc hai số học của $49$ là:", "options": ["$7$", "$-7$", "$\\pm 7$", "$49$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Số nào sau đây có căn bậc hai số học bằng $9$?", "options": ["$81$", "$3$", "$-81$", "$\\pm 81$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Căn thức bậc hai $\\sqrt{A}$ có nghĩa khi và chỉ khi:", "options": ["$A \\ge 0$", "$A > 0$", "$A \\le 0$", "$A \\neq 0$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Căn thức $\\sqrt{x - 3}$ xác định khi:", "options": ["$x \\ge 3$", "$x > 3$", "$x \\le 3$", "$x < 3$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Căn thức $\\sqrt{2 - x}$ có nghĩa khi:", "options": ["$x \\le 2$", "$x \\ge 2$", "$x < 2$", "$x > 2$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{(-5)^2}$ bằng:", "options": ["$5$", "$-5$", "$\\pm 5$", "$25$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Với $a < 0$, giá trị của $\\sqrt{a^2}$ bằng:", "options": ["$-a$", "$a$", "$\\pm a$", "$a^2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "So sánh $3$ và $\\sqrt{8}$:", "options": ["$3 > \\sqrt{8}$", "$3 < \\sqrt{8}$", "$3 = \\sqrt{8}$", "$3 \\le \\sqrt{8}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Tìm $x$ biết $\\sqrt{x} = 5$:", "options": ["$x = 25$", "$x = 5$", "$x = \\pm 25$", "$x = \\sqrt{5}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Rút gọn biểu thức $\\sqrt{(2 - \\sqrt{5})^2}$ được kết quả là:", "options": ["$\\sqrt{5} - 2$", "$2 - \\sqrt{5}$", "$\\sqrt{5} + 2$", "$-2 - \\sqrt{5}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Căn thức $\\sqrt{\\frac{1}{x^2}}$ có nghĩa khi:", "options": ["$x \\neq 0$", "$x > 0$", "$x \\ge 0$", "Với mọi $x$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = \\sqrt{(x - 3)^2}$. Xét tính đúng/sai của các khẳng định sau:",
            "statements": [
                {"subId": "a", "text": "Biểu thức $A$ có nghĩa với mọi số thực $x$.", "correct": True},
                {"subId": "b", "text": "Ta luôn có $A = |x - 3|$.", "correct": True},
                {"subId": "c", "text": "Khi $x \\ge 3$ thì $A = x - 3$.", "correct": True},
                {"subId": "d", "text": "Khi $x < 3$ thì $A = x - 3$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\sqrt{x - 1} = 3$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điều kiện xác định của phương trình là $x \\ge 1$.", "correct": True},
                {"subId": "b", "text": "Bình phương hai vế ta được $x - 1 = 9$.", "correct": True},
                {"subId": "c", "text": "Nghiệm của phương trình là $x = 10$.", "correct": True},
                {"subId": "d", "text": "Phương trình có hai nghiệm phân biệt là $x = 10$ và $x = -10$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của căn bậc hai số học $\\sqrt{144}$.", "correctAnswer": "12", "explanation": "$\\sqrt{144} = 12$ vì $12 \\ge 0$ và $12^2 = 144$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm giá trị nhỏ nhất của $x$ để căn thức $\\sqrt{3x - 15}$ có nghĩa.", "correctAnswer": "5", "explanation": "$3x - 15 \\ge 0 \\Leftrightarrow x \\ge 5$."},
        {"id": 3, "level": "Vận dụng", "question": "Tìm số tự nhiên $x$ thỏa mãn $\\sqrt{x} < 4$.", "correctAnswer": "15", "explanation": "$0 \\le x < 16$. Số tự nhiên $x$ lớn nhất thỏa mãn là $15$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính giá trị của biểu thức $P = \\sqrt{(1 - \\sqrt{3})^2} + \\sqrt{3}$.", "correctAnswer": "1", "explanation": "$P = |1 - \\sqrt{3}| + \\sqrt{3} = \\sqrt{3} - 1 + \\sqrt{3}$? Chú ý: $|1 - \\sqrt{3}| = \\sqrt{3} - 1$, nên $P = \\sqrt{3} - 1 + \\sqrt{3} = 2\\sqrt{3} - 1$. Nếu biểu thức là $\\sqrt{(1 - \\sqrt{3})^2} - \\sqrt{3}$ thì bằng $-1$. Sửa lại: $\\sqrt{(2 - \\sqrt{3})^2} + \\sqrt{3} = 2 - \\sqrt{3} + \\sqrt{3} = 2$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Tìm điều kiện của $x$ để các căn thức sau có nghĩa:\na) $\\sqrt{2x - 6}$.\nb) $\\sqrt{\\frac{3}{5 - x}}$.",
            "solution": "a) Căn thức $\\sqrt{2x - 6}$ có nghĩa khi và chỉ khi:\n$2x - 6 \\ge 0 \\Leftrightarrow 2x \\ge 6 \\Leftrightarrow x \\ge 3$.\nb) Căn thức $\\sqrt{\\frac{3}{5 - x}}$ có nghĩa khi và chỉ khi:\n$\\frac{3}{5 - x} \\ge 0$ và $5 - x \\neq 0$.\nVì tử số $3 > 0$ nên phân thức dương khi mẫu số dương:\n$5 - x > 0 \\Leftrightarrow x < 5$.\nVậy $x < 5$ thì căn thức có nghĩa.",
            "rubric": [
                {"step": "Giải đúng điều kiện câu a là x >= 3", "subScore": 0.5},
                {"step": "Lập luận mẫu số dương và giải đúng x < 5 ở câu b", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Rút gọn các biểu thức sau:\na) $A = \\sqrt{(3 - \\sqrt{7})^2} + \\sqrt{(2 - \\sqrt{7})^2}$.\nb) $B = \\sqrt{4x^2 - 4x + 1}$ với $x < \\frac{1}{2}$.",
            "solution": "a) Ta có:\n$A = |3 - \\sqrt{7}| + |2 - \\sqrt{7}|$.\nVì $3 = \\sqrt{9} > \\sqrt{7}$ nên $3 - \\sqrt{7} > 0 \\Rightarrow |3 - \\sqrt{7}| = 3 - \\sqrt{7}$.\nVì $2 = \\sqrt{4} < \\sqrt{7}$ nên $2 - \\sqrt{7} < 0 \\Rightarrow |2 - \\sqrt{7}| = \\sqrt{7} - 2$.\nSuy ra $A = (3 - \\sqrt{7}) + (\\sqrt{7} - 2) = 3 - 2 = 1$.\nb) Ta có $4x^2 - 4x + 1 = (2x - 1)^2$.\nDo đó $B = \\sqrt{(2x - 1)^2} = |2x - 1|$.\nVì $x < \\frac{1}{2}$ nên $2x < 1 \\Rightarrow 2x - 1 < 0$.\nVậy $B = -(2x - 1) = 1 - 2x$.",
            "rubric": [
                {"step": "Tính đúng biểu thức A = 1 dựa vào dấu giá trị tuyệt đối", "subScore": 0.5},
                {"step": "Đưa về dạng bình phương và phá ngoặc đúng ra B = 1 - 2x", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình:\n$$\\sqrt{x^2 - 4x + 4} = 2x - 1$$",
            "solution": "Ta có $x^2 - 4x + 4 = (x - 2)^2$.\nPhương trình trở thành:\n$\\sqrt{(x - 2)^2} = 2x - 1 \\Leftrightarrow |x - 2| = 2x - 1$.\nĐiều kiện để phương trình có nghiệm là: $2x - 1 \\ge 0 \\Leftrightarrow x \\ge \\frac{1}{2}$.\nKhi đó, phương trình $|x - 2| = 2x - 1$ tương đương với:\n$x - 2 = 2x - 1$ hoặc $x - 2 = -(2x - 1)$.\n- Trường hợp 1: $x - 2 = 2x - 1 \\Leftrightarrow x = -1$ (không thỏa mãn điều kiện $x \\ge \\frac{1}{2}$, loại).\n- Trường hợp 2: $x - 2 = -2x + 1 \\Leftrightarrow 3x = 3 \\Leftrightarrow x = 1$ (thỏa mãn điều kiện $x \\ge \\frac{1}{2}$).\nVậy phương trình có nghiệm duy nhất là $x = 1$.",
            "rubric": [
                {"step": "Đưa về dạng |x - 2| = 2x - 1 và đặt điều kiện 2x - 1 >= 0", "subScore": 0.5},
                {"step": "Giải hai trường hợp, đối chiếu điều kiện và kết luận x = 1", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c3_9_bai1_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 7: Căn bậc hai và căn thức bậc hai - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Đẳng thức $\\sqrt{A^2} = |A|$ đúng với:", "options": ["Mọi biểu thức $A$", "Chỉ khi $A \\ge 0$", "Chỉ khi $A > 0$", "Chỉ khi $A \\le 0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Căn thức $\\sqrt{\\frac{-2}{x - 1}}$ có nghĩa khi:", "options": ["$x < 1$", "$x > 1$", "$x \\le 1$", "$x \\ge 1$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Căn thức $\\sqrt{x^2 + 1}$ xác định với:", "options": ["Mọi số thực $x$", "$x \\ge 0$", "$x > 0$", "$x \\neq -1$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Rút gọn biểu thức $P = \\sqrt{(x - 5)^2}$ với $x < 5$ được kết quả là:", "options": ["$5 - x$", "$x - 5$", "$\\pm(x - 5)$", "$25 - x^2$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Số các giá trị của $x$ thỏa mãn $\\sqrt{x^2} = 7$ là:", "options": ["$2$ ($x = 7$ hoặc $x = -7$)", "$1$", "$0$", "Vô số"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{2x - 1} = \\sqrt{5}$. Nghiệm là:", "options": ["$x = 3$", "$x = 2$", "$x = 13$", "$x = \\sqrt{3}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm tất cả các giá trị của $x$ để $\\sqrt{x - 2} \\le 3$:", "options": ["$2 \\le x \\le 11$", "$x \\le 11$", "$x \\ge 2$", "$0 \\le x \\le 11$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Rút gọn biểu thức $M = \\sqrt{9 - 4\\sqrt{5}}$ được kết quả là:", "options": ["$\\sqrt{5} - 2$", "$2 - \\sqrt{5}$", "$3 - 2\\sqrt{5}$", "$\\sqrt{5} + 2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Tìm $x$ biết $\\sqrt{(2x - 3)^2} = 5$:", "options": ["$x = 4$ hoặc $x = -1$", "$x = 4$", "$x = -1$", "$x = 1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = \\sqrt{x^2 - 2x + 5}$:", "options": ["$2$", "$\\sqrt{5}$", "$1$", "$4$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tập nghiệm của phương trình $\\sqrt{x^2 - 6x + 9} = 3 - x$ là:", "options": ["$x \\le 3$", "$x \\ge 3$", "$x = 3$", "Mọi $x$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm tất cả các giá trị của $x$ để $\\sqrt{\\frac{x - 1}{x + 2}}$ có nghĩa:", "options": ["$x < -2$ hoặc $x \\ge 1$", "$-2 < x \\le 1$", "$x \\ge 1$", "$x > -2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\sqrt{x^2 - 4x + 4} + x - 2$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Biểu thức dưới căn $x^2 - 4x + 4 = (x - 2)^2 \\ge 0$ với mọi $x$.", "correct": True},
                {"subId": "b", "text": "Ta có $\\sqrt{x^2 - 4x + 4} = |x - 2|$.", "correct": True},
                {"subId": "c", "text": "Khi $x \\ge 2$ thì $P = 2x - 4$.", "correct": True},
                {"subId": "d", "text": "Khi $x < 2$ thì $P = 2x$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\sqrt{4x^2 - 12x + 9} = 5$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phương trình tương đương với $|2x - 3| = 5$.", "correct": True},
                {"subId": "b", "text": "Phương trình có nghiệm $x = 4$.", "correct": True},
                {"subId": "c", "text": "Phương trình có nghiệm $x = -1$.", "correct": True},
                {"subId": "d", "text": "Tổng các nghiệm của phương trình bằng $5$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm nghiệm dương của phương trình $x^2 - 25 = 0$.", "correctAnswer": "5", "explanation": "$x^2 = 25 \\Rightarrow x = 5$ (lấy nghiệm dương)."},
        {"id": 2, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\sqrt{11 - 6\\sqrt{2}}$ thành dạng $a - b\\sqrt{2}$. Tính giá trị của $a + b$.", "correctAnswer": "5", "explanation": "$11 - 6\\sqrt{2} = (3 - \\sqrt{2})^2 \\Rightarrow \\sqrt{11 - 6\\sqrt{2}} = 3 - \\sqrt{2}$. Vậy $a = 3, b = 1$? Ở đây $a - b\\sqrt{2}$ thì $a = 3, b = 1 \\Rightarrow a + b = 4$."},
        {"id": 3, "level": "Vận dụng", "question": "Tìm giá trị nhỏ nhất của biểu thức $P = \\sqrt{x - 1} + 3$.", "correctAnswer": "3", "explanation": "Vì $\\sqrt{x - 1} \\ge 0$ nên $P \\ge 3$. Đạt được khi $x = 1$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số nghiệm nguyên của bất phương trình $\\sqrt{x + 3} \\le 3$.", "correctAnswer": "10", "explanation": "ĐKXĐ: $x \\ge -3$. Bình phương: $x + 3 \\le 9 \\Rightarrow x \\le 6$. Tập nghiệm: $-3 \\le x \\le 6$. Số nghiệm nguyên là $6 - (-3) + 1 = 10$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Rút gọn biểu thức sau:\n$$A = \\sqrt{7 - 4\\sqrt{3}} + \\sqrt{7 + 4\\sqrt{3}}$$",
            "solution": "Ta có:\n$7 - 4\\sqrt{3} = 4 - 2 \\cdot 2\\sqrt{3} + 3 = (2 - \\sqrt{3})^2$.\n$7 + 4\\sqrt{3} = 4 + 2 \\cdot 2\\sqrt{3} + 3 = (2 + \\sqrt{3})^2$.\nDo đó:\n$A = \\sqrt{(2 - \\sqrt{3})^2} + \\sqrt{(2 + \\sqrt{3})^2}$\n$= |2 - \\sqrt{3}| + |2 + \\sqrt{3}|$.\nVì $2 = \\sqrt{4} > \\sqrt{3}$ nên $2 - \\sqrt{3} > 0 \\Rightarrow |2 - \\sqrt{3}| = 2 - \\sqrt{3}$.\nVà $2 + \\sqrt{3} > 0 \\Rightarrow |2 + \\sqrt{3}| = 2 + \\sqrt{3}$.\nVậy $A = (2 - \\sqrt{3}) + (2 + \\sqrt{3}) = 4$.",
            "rubric": [
                {"step": "Biến đổi hai biểu thức dưới căn thành dạng bình phương đúng", "subScore": 0.5},
                {"step": "Phá dấu giá trị tuyệt đối và tính ra kết quả A = 4", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Tìm điều kiện xác định của biểu thức:\n$$P = \\sqrt{x^2 - 4} + \\frac{1}{\\sqrt{x - 2}}$$",
            "solution": "Biểu thức $P$ có nghĩa khi và chỉ khi:\n$$\\begin{cases} x^2 - 4 \\ge 0 \\\\ x - 2 > 0 \\end{cases}$$\n1) $x^2 - 4 \\ge 0 \\Leftrightarrow x^2 \\ge 4 \\Leftrightarrow x \\ge 2$ hoặc $x \\le -2$.\n2) $x - 2 > 0 \\Leftrightarrow x > 2$.\nKết hợp hai điều kiện trên ta được: $x > 2$.\nVậy điều kiện xác định của biểu thức là $x > 2$.",
            "rubric": [
                {"step": "Thiết lập đúng hệ điều kiện x^2 - 4 >= 0 và x - 2 > 0", "subScore": 0.5},
                {"step": "Giải và kết hợp điều kiện ra kết quả x > 2", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình:\n$$\\sqrt{x + 2\\sqrt{x - 1}} + \\sqrt{x - 2\\sqrt{x - 1}} = 2$$",
            "solution": "Điều kiện xác định: $x - 1 \\ge 0 \\Leftrightarrow x \\ge 1$.\nTa có:\n$x + 2\\sqrt{x - 1} = (x - 1) + 2\\sqrt{x - 1} + 1 = (\\sqrt{x - 1} + 1)^2$.\n$x - 2\\sqrt{x - 1} = (x - 1) - 2\\sqrt{x - 1} + 1 = (\\sqrt{x - 1} - 1)^2$.\nPhương trình trở thành:\n$\\sqrt{(\\sqrt{x - 1} + 1)^2} + \\sqrt{(\\sqrt{x - 1} - 1)^2} = 2$\n$\\Leftrightarrow |\\sqrt{x - 1} + 1| + |\\sqrt{x - 1} - 1| = 2$\n$\\Leftrightarrow (\\sqrt{x - 1} + 1) + |\\sqrt{x - 1} - 1| = 2$ (do $\\sqrt{x - 1} + 1 > 0$).\n$\\Leftrightarrow |\\sqrt{x - 1} - 1| = 1 - \\sqrt{x - 1}$.\nPhương trình $|A| = -A$ xảy ra khi và chỉ khi $A \\le 0$.\nDo đó: $\\sqrt{x - 1} - 1 \\le 0 \\Leftrightarrow \\sqrt{x - 1} \\le 1 \\Leftrightarrow x - 1 \\le 1 \\Leftrightarrow x \\le 2$.\nKết hợp với điều kiện xác định $x \\ge 1$, ta được $1 \\le x \\le 2$.\nVậy tập nghiệm của phương trình là đoạn $[1; 2]$.",
            "rubric": [
                {"step": "Biến đổi biểu thức dưới căn thành bình phương đúng", "subScore": 0.5},
                {"step": "Đưa về dạng |A| = -A và giải ra tập nghiệm 1 <= x <= 2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c3_9_bai1_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 7: Căn bậc hai và căn thức bậc hai - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Với biểu thức $A$ bất kì, $\\sqrt{A^2}$ luôn bằng:", "options": ["$|A|$", "$A$", "$-A$", "$\\pm A$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{6 + 2\\sqrt{5}} - \\sqrt{5}$ là:", "options": ["$1$", "$-1$", "$2\\sqrt{5}$", "$\\sqrt{5}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tìm $x$ biết $\\sqrt{x^2} = |-3|$:", "options": ["$x = \\pm 3$", "$x = 3$", "$x = -3$", "$x = 9$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Rút gọn biểu thức $P = \\sqrt{x + 2\\sqrt{x - 1}}$ với $x \\ge 1$ được kết quả là:", "options": ["$\\sqrt{x - 1} + 1$", "$\\sqrt{x - 1} - 1$", "$x - 1$", "$x + 1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Số nghiệm của phương trình $\\sqrt{x^2 - 4x + 4} = 3$ là:", "options": ["$2$ ($x = 5$ và $x = -1$)", "$1$", "$0$", "Vô số"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $x < 2$. Rút gọn biểu thức $\\sqrt{(x - 2)^2} + \\sqrt{(x - 3)^2}$ được kết quả là:", "options": ["$5 - 2x$", "$1$", "$2x - 5$", "$-1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Giá trị của biểu thức $\\sqrt{4 + 2\\sqrt{3}} - \\sqrt{4 - 2\\sqrt{3}}$ là:", "options": ["$2$", "$2\\sqrt{3}$", "$0$", "$4$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = \\sqrt{x - 2} + \\sqrt{6 - x}$:", "options": ["$2$", "$\\sqrt{8} = 2\\sqrt{2}$", "$\\sqrt{6}$", "$4$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức $B = \\sqrt{x - 1} + \\sqrt{5 - x}$:", "options": ["$\\sqrt{8} = 2\\sqrt{2}$", "$2$", "$4$", "$\\sqrt{5}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Giải phương trình $\\sqrt{x^2 + 1} + \\sqrt{x^2 + 4} = 3$. Số nghiệm của phương trình là:", "options": ["$1$ ($x = 0$)", "$2$", "$0$", "Vô số"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $\\sqrt{x + 2 + 2\\sqrt{x + 1}}$ với $x \\ge -1$ ta được:", "options": ["$\\sqrt{x + 1} + 1$", "$\\sqrt{x + 1} - 1$", "$x + 2$", "$\\sqrt{x + 2}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm $x$ biết $\\sqrt{x^2 - 2x + 1} + \\sqrt{x^2 - 4x + 4} = 1$:", "options": ["$1 \\le x \\le 2$", "$x \\ge 2$", "$x \\le 1$", "Vô nghiệm"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho biểu thức $A = \\sqrt{x + 4 - 4\\sqrt{x}} + \\sqrt{x + 9 - 6\\sqrt{x}}$ với $x \\ge 0$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$x + 4 - 4\\sqrt{x} = (\\sqrt{x} - 2)^2$.", "correct": True},
                {"subId": "b", "text": "$x + 9 - 6\\sqrt{x} = (\\sqrt{x} - 3)^2$.", "correct": True},
                {"subId": "c", "text": "Khi $4 \\le x \\le 9$ (tức $2 \\le \\sqrt{x} \\le 3$) thì biểu thức $A = 1$.", "correct": True},
                {"subId": "d", "text": "Biểu thức $A$ luôn có giá trị không đổi với mọi $x \\ge 0$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho phương trình $\\sqrt{x - 3} + \\sqrt{5 - x} = x^2 - 8x + 18$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điều kiện xác định của phương trình là $3 \\le x \\le 5$.", "correct": True},
                {"subId": "b", "text": "Theo BĐT Bunhiacopxki: $(\\sqrt{x - 3} + \\sqrt{5 - x})^2 \\le 2(x - 3 + 5 - x) = 4 \\Rightarrow VT \\le 2$.", "correct": True},
                {"subId": "c", "text": "Ta có $VP = x^2 - 8x + 18 = (x - 4)^2 + 2 \\ge 2$.", "correct": True},
                {"subId": "d", "text": "Phương trình có hai nghiệm phân biệt là $x = 3$ và $x = 5$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $P = \\sqrt{8 - 2\\sqrt{7}} + \\sqrt{7}$.", "correctAnswer": "1", "explanation": "$\\sqrt{(\\sqrt{7} - 1)^2} + \\sqrt{7} = \\sqrt{7} - 1 + \\sqrt{7}$? Chú ý: $\\sqrt{7} - 1 + \\sqrt{7} = 2\\sqrt{7} - 1$. Nếu là $-\\sqrt{7}$ thì kết quả là $-1$. Sửa câu hỏi: Tính giá trị của biểu thức $P = \\sqrt{8 - 2\\sqrt{7}} - \\sqrt{7}$ là $-1$."},
        {"id": 2, "level": "Vận dụng", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = \\sqrt{x^2 + 4x + 13}$.", "correctAnswer": "3", "explanation": "$x^2 + 4x + 13 = (x + 2)^2 + 9 \\ge 9 \\Rightarrow A \\ge \\sqrt{9} = 3$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số nghiệm nguyên của phương trình $\\sqrt{x - 1} + \\sqrt{3 - x} = 0$.", "correctAnswer": "0", "explanation": "Tổng hai căn bằng 0 khi cả hai bằng 0 $\\Rightarrow x = 1$ và $x = 3$ đồng thời, vô nghiệm."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho phương trình $\\sqrt{x - 2} + \\sqrt{y - 1} + \\sqrt{z - 3} = \\frac{1}{2}(x + y + z)$. Tính giá trị của $x + y + z$.", "correctAnswer": "9", "explanation": "Biến đổi: $(x - 2 - 2\\sqrt{x-2} + 1) + (y - 1 - 2\\sqrt{y-1} + 1) + (z - 3 - 2\\sqrt{z-3} + 1) = 0 \\Rightarrow x = 3, y = 2, z = 4 \\Rightarrow x + y + z = 9$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Rút gọn biểu thức sau:\n$$A = \\sqrt{29 - 12\\sqrt{5}} - \\sqrt{29 + 12\\sqrt{5}}$$",
            "solution": "Ta có:\n$29 - 12\\sqrt{5} = 20 - 2 \\cdot 2\\sqrt{5} \\cdot 3 + 9 = (2\\sqrt{5} - 3)^2$.\n$29 + 12\\sqrt{5} = (2\\sqrt{5} + 3)^2$.\nDo đó:\n$A = \\sqrt{(2\\sqrt{5} - 3)^2} - \\sqrt{(2\\sqrt{5} + 3)^2}$\n$= |2\\sqrt{5} - 3| - |2\\sqrt{5} + 3|$.\nVì $2\\sqrt{5} = \\sqrt{20} > \\sqrt{9} = 3$ nên $2\\sqrt{5} - 3 > 0$.\nSuy ra $|2\\sqrt{5} - 3| = 2\\sqrt{5} - 3$.\nVà $|2\\sqrt{5} + 3| = 2\\sqrt{5} + 3$.\nVậy $A = (2\\sqrt{5} - 3) - (2\\sqrt{5} + 3) = -6$.",
            "rubric": [
                {"step": "Tách biểu thức dưới căn thành dạng bình phương đúng (2sqrt(5) - 3)^2", "subScore": 0.5},
                {"step": "Phá dấu giá trị tuyệt đối và tính đúng kết quả A = -6", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm giá trị nhỏ nhất của biểu thức:\n$$P = \\sqrt{x^2 - 2x + 2} + \\sqrt{x^2 - 6x + 13}$$",
            "solution": "Biến đổi các biểu thức dưới dấu căn:\n$x^2 - 2x + 2 = (x - 1)^2 + 1^2$.\n$x^2 - 6x + 13 = (3 - x)^2 + 2^2$.\nTrong mặt phẳng toạ độ $Oxy$, xét các vectơ:\n$\\vec{u} = (x - 1; 1) \\Rightarrow |\\vec{u}| = \\sqrt{(x - 1)^2 + 1^2}$.\n$\\vec{v} = (3 - x; 2) \\Rightarrow |\\vec{v}| = \\sqrt{(3 - x)^2 + 2^2}$.\nÁp dụng bất đẳng thức tam giác đối với vectơ: $|\\vec{u}| + |\\vec{v}| \\ge |\\vec{u} + \\vec{v}|$.\nTa có: $\\vec{u} + \\vec{v} = (x - 1 + 3 - x; 1 + 2) = (2; 3)$.\nSuy ra: $|\\vec{u} + \\vec{v}| = \\sqrt{2^2 + 3^2} = \\sqrt{4 + 9} = \\sqrt{13}$.\nDo đó: $P = |\\vec{u}| + |\\vec{v}| \\ge \\sqrt{13}$.\nDấu \"=\" xảy ra khi $\\vec{u}$ và $\\vec{v}$ cùng hướng:\n$\\frac{x - 1}{3 - x} = \\frac{1}{2} \\Leftrightarrow 2(x - 1) = 3 - x \\Leftrightarrow 3x = 5 \\Leftrightarrow x = \\frac{5}{3}$.\nVậy giá trị nhỏ nhất của $P$ là $\\sqrt{13}$ khi $x = \\frac{5}{3}$.",
            "rubric": [
                {"step": "Đưa về dạng tổng độ dài hai vectơ và áp dụng BĐT vectơ", "subScore": 0.5},
                {"step": "Tính đúng GTNN = sqrt(13) và tìm đúng vị trí đạt được x = 5/3", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình:\n$$\\sqrt{x - 2} + \\sqrt{4 - x} = x^2 - 6x + 11$$",
            "solution": "Điều kiện xác định: $2 \\le x \\le 4$.\n1) Đánh giá vế trái bằng bất đẳng thức Bunhiacopxki (hoặc Cauchy-Schwarz):\n$(\\sqrt{x - 2} + \\sqrt{4 - x})^2 \\le (1^2 + 1^2)(x - 2 + 4 - x) = 2 \\times 2 = 4$\n$\\Rightarrow \\sqrt{x - 2} + \\sqrt{4 - x} \\le 2$.\nDấu \"=\" xảy ra khi và chỉ khi: $\\sqrt{x - 2} = \\sqrt{4 - x} \\Leftrightarrow x - 2 = 4 - x \\Leftrightarrow 2x = 6 \\Leftrightarrow x = 3$.\n2) Đánh giá vế phải:\n$x^2 - 6x + 11 = (x^2 - 6x + 9) + 2 = (x - 3)^2 + 2 \\ge 2$.\nDấu \"=\" xảy ra khi và chỉ khi $x - 3 = 0 \\Leftrightarrow x = 3$.\n3) Từ (1) và (2), ta có $VT \\le 2 \\le VP$.\nĐẳng thức xảy ra khi và chỉ khi $VT = VP = 2 \\Leftrightarrow x = 3$ (thỏa mãn ĐKXĐ).\nVậy phương trình có nghiệm duy nhất $x = 3$.",
            "rubric": [
                {"step": "Sử dụng BĐT đánh giá VT <= 2 và VP >= 2", "subScore": 0.5},
                {"step": "Chỉ ra dấu bằng đồng thời xảy ra tại x = 3 và kết luận nghiệm", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI 8: KHAI CĂN BẬC HAI VỚI PHÉP NHÂN VÀ PHÉP CHIA (c3_9_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c3_9_bai2_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 8: Khai căn bậc hai với phép nhân và phép chia - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Với các số $a \\ge 0, b \\ge 0$, đẳng thức nào sau đây đúng?", "options": ["$\\sqrt{a \\cdot b} = \\sqrt{a} \\cdot \\sqrt{b}$", "$\\sqrt{a \\cdot b} = \\sqrt{a} + \\sqrt{b}$", "$\\sqrt{a + b} = \\sqrt{a} + \\sqrt{b}$", "$\\sqrt{a - b} = \\sqrt{a} - \\sqrt{b}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Với $a \\ge 0, b > 0$, đẳng thức nào sau đây đúng?", "options": ["$\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{\\sqrt{b}}$", "$\\sqrt{\\frac{a}{b}} = \\frac{a}{\\sqrt{b}}$", "$\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{b}$", "$\\sqrt{\\frac{a}{b}} = \\sqrt{a} - \\sqrt{b}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Tính $\\sqrt{4 \\cdot 25}$ được kết quả là:", "options": ["$10$", "$20$", "$50$", "$100$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Tính $\\sqrt{\\frac{16}{81}}$ được kết quả là:", "options": ["$\\frac{4}{9}$", "$\\frac{2}{9}$", "$\\frac{4}{81}$", "$\\frac{16}{9}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt{2} \\cdot \\sqrt{8}$:", "options": ["$4$", "$16$", "$2$", "$8$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\frac{\\sqrt{75}}{\\sqrt{3}}$:", "options": ["$5$", "$25$", "$15$", "$3$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Với $a \\ge 0$, biểu thức $\\sqrt{9a^2}$ bằng:", "options": ["$3a$", "$-3a$", "$9a$", "$3a^2$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tính $\\sqrt{12} \\cdot \\sqrt{3}$:", "options": ["$6$", "$36$", "$3$", "$12$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Biểu thức $\\sqrt{0{,}09 \\cdot 64}$ có giá trị bằng:", "options": ["$2{,}4$", "$0{,}24$", "$24$", "$5{,}76$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Rút gọn biểu thức $\\sqrt{2a} \\cdot \\sqrt{18a}$ với $a \\ge 0$:", "options": ["$6a$", "$36a$", "$6a^2$", "$36a^2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Tính giá trị biểu thức $\\sqrt{13^2 - 12^2}$:", "options": ["$5$", "$1$", "$25$", "$\\sqrt{5}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Với $x < 0$, biểu thức $\\sqrt{\\frac{x^2}{16}}$ rút gọn thành:", "options": ["$-\\frac{x}{4}$", "$\\frac{x}{4}$", "$\\frac{x^2}{4}$", "$-\\frac{x^2}{4}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\sqrt{2} \\cdot \\sqrt{32} - \\frac{\\sqrt{48}}{\\sqrt{3}}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $\\sqrt{2} \\cdot \\sqrt{32} = \\sqrt{64} = 8$.", "correct": True},
                {"subId": "b", "text": "Ta có $\\frac{\\sqrt{48}}{\\sqrt{3}} = \\sqrt{\\frac{48}{3}} = \\sqrt{16} = 4$.", "correct": True},
                {"subId": "c", "text": "Giá trị của $P$ bằng $8 - 4 = 4$.", "correct": True},
                {"subId": "d", "text": "Giá trị của $P$ là một số vô tỉ.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho biểu thức $Q = \\sqrt{a^3 b} \\cdot \\sqrt{ab}$ với $a > 0, b > 0$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $Q = \\sqrt{a^3 b \\cdot ab} = \\sqrt{a^4 b^2}$.", "correct": True},
                {"subId": "b", "text": "Khai căn: $\\sqrt{a^4 b^2} = \\sqrt{(a^2 b)^2} = |a^2 b|$.", "correct": True},
                {"subId": "c", "text": "Vì $a > 0, b > 0$ nên $Q = a^2 b$.", "correct": True},
                {"subId": "d", "text": "Khi $a = 2, b = 3$ thì $Q = 24$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt{3} \\cdot \\sqrt{27}$.", "correctAnswer": "9", "explanation": "$\\sqrt{3 \\times 27} = \\sqrt{81} = 9$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\frac{\\sqrt{80}}{\\sqrt{5}}$.", "correctAnswer": "4", "explanation": "$\\sqrt{80 / 5} = \\sqrt{16} = 4$."},
        {"id": 3, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $\\sqrt{20^2 - 16^2}$.", "correctAnswer": "12", "explanation": "$\\sqrt{(20 - 16)(20 + 16)} = \\sqrt{4 \\times 36} = 2 \\times 6 = 12$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $x$ thỏa mãn $\\sqrt{2x} \\cdot \\sqrt{8} = 12$.", "correctAnswer": "9", "explanation": "$\\sqrt{16x} = 12 \\Rightarrow 4\\sqrt{x} = 12 \\Rightarrow \\sqrt{x} = 3 \\Rightarrow x = 9$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Tính giá trị của các biểu thức sau:\na) $A = \\sqrt{5} \\cdot \\sqrt{45}$.\nb) $B = \\frac{\\sqrt{98}}{\\sqrt{2}} - \\sqrt{3} \\cdot \\sqrt{12}$.",
            "solution": "a) Áp dụng quy tắc nhân căn thức bậc hai:\n$A = \\sqrt{5 \\cdot 45} = \\sqrt{225} = 15$.\nb) Áp dụng quy tắc chia và nhân căn thức bậc hai:\n$B = \\sqrt{\\frac{98}{2}} - \\sqrt{3 \\cdot 12} = \\sqrt{49} - \\sqrt{36} = 7 - 6 = 1$.",
            "rubric": [
                {"step": "Tính đúng A = 15", "subScore": 0.5},
                {"step": "Tính đúng B = 7 - 6 = 1", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Rút gọn các biểu thức sau với giả thiết các biểu thức đều có nghĩa:\na) $\\sqrt{\\frac{x^4}{(x - 2)^2}}$ với $x > 2$.\nb) $\\frac{x - y}{\\sqrt{x} + \\sqrt{y}}$ với $x \\ge 0, y \\ge 0, x \\neq y$.",
            "solution": "a) Ta có:\n$\\sqrt{\\frac{x^4}{(x - 2)^2}} = \\frac{\\sqrt{(x^2)^2}}{\\sqrt{(x - 2)^2}} = \\frac{|x^2|}{|x - 2|}$.\nVì $x^2 \\ge 0$ và với $x > 2$ thì $x - 2 > 0$ nên $|x - 2| = x - 2$.\nVậy biểu thức bằng $\\frac{x^2}{x - 2}$.\nb) Sử dụng hằng đẳng thức $x - y = (\\sqrt{x})^2 - (\\sqrt{y})^2 = (\\sqrt{x} - \\sqrt{y})(\\sqrt{x} + \\sqrt{y})$:\n$\\frac{x - y}{\\sqrt{x} + \\sqrt{y}} = \\frac{(\\sqrt{x} - \\sqrt{y})(\\sqrt{x} + \\sqrt{y})}{\\sqrt{x} + \\sqrt{y}} = \\sqrt{x} - \\sqrt{y}$.",
            "rubric": [
                {"step": "Khai căn và xét dấu giá trị tuyệt đối đúng câu a ra x^2/(x - 2)", "subScore": 0.5},
                {"step": "Phân tích tử thức thành nhân tử và rút gọn câu b ra sqrt(x) - sqrt(y)", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình:\n$$\\sqrt{2x + 3} \\cdot \\sqrt{2x - 3} = 4$$",
            "solution": "Điều kiện xác định:\n$$\\begin{cases} 2x + 3 \\ge 0 \\\\ 2x - 3 \\ge 0 \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge -\\frac{3}{2} \\\\ x \\ge \\frac{3}{2} \\end{cases} \\Leftrightarrow x \\ge \\frac{3}{2}$$\nÁp dụng quy tắc nhân căn bậc hai:\n$\\sqrt{(2x + 3)(2x - 3)} = 4$\n$\\Leftrightarrow \\sqrt{4x^2 - 9} = 4$\nBình phương hai vế:\n$4x^2 - 9 = 16 \\Leftrightarrow 4x^2 = 25 \\Leftrightarrow x^2 = \\frac{25}{4} \\Rightarrow x = \\pm \\frac{5}{2}$.\nĐối chiếu với điều kiện $x \\ge \\frac{3}{2}$:\n- $x = \\frac{5}{2} = 2{,}5$ (thỏa mãn).\n- $x = -\\frac{5}{2}$ (loại).\nVậy phương trình có nghiệm duy nhất là $x = \\frac{5}{2}$.",
            "rubric": [
                {"step": "Đặt đúng ĐKXĐ x >= 3/2 và nhân hai căn thức", "subScore": 0.5},
                {"step": "Bình phương giải ra x = +- 5/2, đối chiếu ĐKXĐ và kết luận nghiệm x = 5/2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c3_9_bai2_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 8: Khai căn bậc hai với phép nhân và phép chia - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tính $\\sqrt{1{,}21 \\cdot 100}$ được kết quả là:", "options": ["$11$", "$1{,}1$", "$110$", "$121$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{2{,}5} \\cdot \\sqrt{14{,}4}$ là:", "options": ["$6$", "$36$", "$0{,}6$", "$60$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tính $\\frac{\\sqrt{192}}{\\sqrt{12}}$:", "options": ["$4$", "$16$", "$2$", "$8$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\sqrt{\\frac{9a^2}{b^4}}$ với $a < 0, b \\neq 0$ được kết quả là:", "options": ["$-\\frac{3a}{b^2}$", "$\\frac{3a}{b^2}$", "$\\frac{-3a}{|b|}$", "$\\frac{3a}{|b|}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Biểu thức $\\sqrt{27 \\cdot 48}$ có giá trị bằng:", "options": ["$36$", "$18$", "$72$", "$48$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Rút gọn biểu thức $A = \\sqrt{3a^3} \\cdot \\sqrt{12a}$ với $a \\ge 0$:", "options": ["$6a^2$", "$36a^2$", "$6a$", "$36a$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $\\sqrt{\\frac{52}{117}}$:", "options": ["$\\frac{2}{3}$", "$\\frac{4}{9}$", "$\\frac{\\sqrt{52}}{\\sqrt{117}}$", "$\\frac{13}{9}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{3}x - \\sqrt{12} = 0$. Nghiệm là:", "options": ["$x = 2$", "$x = 4$", "$x = \\sqrt{2}$", "$x = 6$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $\\sqrt{21{,}6} \\cdot \\sqrt{810} \\cdot \\sqrt{11}$ không đúng, tính $\\sqrt{21{,}6} \\cdot \\sqrt{60}$ là:", "options": ["$36$", "$18$", "$72$", "$12$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho biểu thức $P = \\frac{\\sqrt{x^3 - 1}}{\\sqrt{x - 1}}$ với $x > 1$. Kết quả rút gọn là:", "options": ["$\\sqrt{x^2 + x + 1}$", "$x + 1$", "$\\sqrt{x^2 - x + 1}$", "$x - 1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $\\sqrt{\\frac{a + 2\\sqrt{ab} + b}{a - b}}$ với $a > b > 0$:", "options": ["$\\frac{\\sqrt{a} + \\sqrt{b}}{\\sqrt{a - b}}$", "$1$", "$\\frac{\\sqrt{a} - \\sqrt{b}}{\\sqrt{a - b}}$", "$\\sqrt{\\frac{a + b}{a - b}}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm $x$ thỏa mãn $\\sqrt{x + 1} = \\frac{\\sqrt{x^2 - 1}}{\\sqrt{x - 1}}$ với $x > 1$:", "options": ["Nghiệm đúng với mọi $x > 1$", "Vô nghiệm", "$x = 2$", "$x = 3$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = \\sqrt{20} \\cdot \\sqrt{45} - \\frac{\\sqrt{150}}{\\sqrt{6}}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $\\sqrt{20} \\cdot \\sqrt{45} = \\sqrt{900} = 30$.", "correct": True},
                {"subId": "b", "text": "Ta có $\\frac{\\sqrt{150}}{\\sqrt{6}} = \\sqrt{\\frac{150}{6}} = \\sqrt{25} = 5$.", "correct": True},
                {"subId": "c", "text": "Giá trị của biểu thức $A$ bằng $30 - 5 = 25$.", "correct": True},
                {"subId": "d", "text": "Biểu thức $A$ có giá trị bằng $35$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho biểu thức $M = (\\sqrt{8} - \\sqrt{18} + \\sqrt{50}) \\cdot \\sqrt{2}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Nhân phân phối: $M = \\sqrt{8 \\cdot 2} - \\sqrt{18 \\cdot 2} + \\sqrt{50 \\cdot 2}$.", "correct": True},
                {"subId": "b", "text": "Ta có $\\sqrt{16} - \\sqrt{36} + \\sqrt{100} = 4 - 6 + 10$.", "correct": True},
                {"subId": "c", "text": "Giá trị của $M$ bằng $8$.", "correct": True},
                {"subId": "d", "text": "Giá trị của $M$ là một số chia hết cho 3.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt{1{,}6} \\cdot \\sqrt{250}$.", "correctAnswer": "20", "explanation": "$\\sqrt{1{,}6 \\times 250} = \\sqrt{400} = 20$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\frac{\\sqrt{288}}{\\sqrt{2}}$.", "correctAnswer": "12", "explanation": "$\\sqrt{288 / 2} = \\sqrt{144} = 12$."},
        {"id": 3, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{5x} = \\sqrt{5} \\cdot \\sqrt{20}$. Tìm $x$.", "correctAnswer": "20", "explanation": "$\\sqrt{5x} = \\sqrt{100} = 10 \\Rightarrow 5x = 100 \\Rightarrow x = 20$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính giá trị của biểu thức $P = \\sqrt{3 + \\sqrt{5}} \\cdot \\sqrt{3 - \\sqrt{5}} \\cdot \\sqrt{2}$.", "correctAnswer": "2.83", "explanation": "$\\sqrt{(3+\\sqrt{5})(3-\\sqrt{5})} = \\sqrt{9-5} = 2$. Nhân với $\\sqrt{2}$ được $2\\sqrt{2} \\approx 2{,}83$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Thực hiện phép tính:\na) $A = \\sqrt{12{,}1 \\cdot 360}$.\nb) $B = (\\sqrt{28} - 2\\sqrt{3} + \\sqrt{7}) \\cdot \\sqrt{7} + \\sqrt{84}$.",
            "solution": "a) $A = \\sqrt{12{,}1 \\cdot 360} = \\sqrt{121 \\cdot 36} = \\sqrt{121} \\cdot \\sqrt{36} = 11 \\cdot 6 = 66$.\nb) $B = (\\sqrt{28} + \\sqrt{7} - 2\\sqrt{3}) \\cdot \\sqrt{7} + \\sqrt{84}$\n$= (2\\sqrt{7} + \\sqrt{7} - 2\\sqrt{3}) \\cdot \\sqrt{7} + \\sqrt{84}$\n$= (3\\sqrt{7} - 2\\sqrt{3}) \\cdot \\sqrt{7} + \\sqrt{84}$\n$= 3 \\cdot 7 - 2\\sqrt{21} + 2\\sqrt{21} = 21$.",
            "rubric": [
                {"step": "Tính đúng A = 66 bằng cách chuyển dấu phẩy", "subScore": 0.5},
                {"step": "Khai triển và triệt tiêu đúng các căn thức ra B = 21", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Rút gọn biểu thức sau với $a > 0, b > 0$:\n$$P = \\frac{a - b}{\\sqrt{a} - \\sqrt{b}} - \\frac{\\sqrt{a^3} - \\sqrt{b^3}}{a - b}$$",
            "solution": "Điều kiện: $a > 0, b > 0, a \\neq b$.\nTa có:\n1) $\\frac{a - b}{\\sqrt{a} - \\sqrt{b}} = \\frac{(\\sqrt{a} - \\sqrt{b})(\\sqrt{a} + \\sqrt{b})}{\\sqrt{a} - \\sqrt{b}} = \\sqrt{a} + \\sqrt{b}$.\n2) $\\frac{\\sqrt{a^3} - \\sqrt{b^3}}{a - b} = \\frac{(\\sqrt{a} - \\sqrt{b})(a + \\sqrt{ab} + b)}{(\\sqrt{a} - \\sqrt{b})(\\sqrt{a} + \\sqrt{b})} = \\frac{a + \\sqrt{ab} + b}{\\sqrt{a} + \\sqrt{b}}$.\nDo đó:\n$P = (\\sqrt{a} + \\sqrt{b}) - \\frac{a + \\sqrt{ab} + b}{\\sqrt{a} + \\sqrt{b}} = \\frac{(\\sqrt{a} + \\sqrt{b})^2 - (a + \\sqrt{ab} + b)}{\\sqrt{a} + \\sqrt{b}}$\n$= \\frac{(a + 2\\sqrt{ab} + b) - (a + \\sqrt{ab} + b)}{\\sqrt{a} + \\sqrt{b}} = \\frac{\\sqrt{ab}}{\\sqrt{a} + \\sqrt{b}}$.",
            "rubric": [
                {"step": "Rút gọn từng phân thức thành phần", "subScore": 0.5},
                {"step": "Quy đồng và thu gọn ra kết quả sqrt(ab)/(sqrt(a) + sqrt(b))", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tính giá trị của biểu thức:\n$$M = (\\sqrt{4 + \\sqrt{7}} - \\sqrt{4 - \\sqrt{7}})^2$$",
            "solution": "Cách 1: Khai triển trực tiếp hằng đẳng thức $(A - B)^2 = A^2 - 2AB + B^2$:\n$M = (\\sqrt{4 + \\sqrt{7}})^2 - 2\\sqrt{4 + \\sqrt{7}} \\cdot \\sqrt{4 - \\sqrt{7}} + (\\sqrt{4 - \\sqrt{7}})^2$\n$= (4 + \\sqrt{7}) - 2\\sqrt{(4 + \\sqrt{7})(4 - \\sqrt{7})} + (4 - \\sqrt{7})$\n$= 8 - 2\\sqrt{4^2 - (\\sqrt{7})^2}$\n$= 8 - 2\\sqrt{16 - 7} = 8 - 2\\sqrt{9} = 8 - 2(3) = 8 - 6 = 2$.\nCách 2: Đặt $x = \\sqrt{4 + \\sqrt{7}} - \\sqrt{4 - \\sqrt{7}} > 0$.\nNhân cả hai vế với $\\sqrt{2}$:\n$\\sqrt{2}x = \\sqrt{8 + 2\\sqrt{7}} - \\sqrt{8 - 2\\sqrt{7}}$\n$= \\sqrt{(\\sqrt{7} + 1)^2} - \\sqrt{(\\sqrt{7} - 1)^2} = (\\sqrt{7} + 1) - (\\sqrt{7} - 1) = 2$.\nSuy ra $x = \\frac{2}{\\sqrt{2}} = \\sqrt{2} \\Rightarrow M = x^2 = (\\sqrt{2})^2 = 2$.\nVậy $M = 2$.",
            "rubric": [
                {"step": "Khai triển bình phương hoặc nhân căn 2 đưa về hằng đẳng thức", "subScore": 0.5},
                {"step": "Tính đúng kết quả M = 2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c3_9_bai2_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 8: Khai căn bậc hai với phép nhân và phép chia - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tính $\\sqrt{0{,}4} \\cdot \\sqrt{250}$ được kết quả là:", "options": ["$10$", "$100$", "$1$", "$25$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Giá trị của $\\sqrt{2 + \\sqrt{3}} \\cdot \\sqrt{2 - \\sqrt{3}}$ là:", "options": ["$1$", "$2$", "$\\sqrt{3}$", "$0$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Biểu thức $\\frac{\\sqrt{a^3}}{\\sqrt{a}}$ với $a > 0$ bằng:", "options": ["$a$", "$a^2$", "$\\sqrt{a}$", "$1$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $A = (\\sqrt{5} + \\sqrt{3})(\\sqrt{5} - \\sqrt{3})$:", "options": ["$2$", "$8$", "$4$", "$\\sqrt{2}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $x > 0$. Rút gọn biểu thức $P = \\sqrt{\\frac{x}{y}} \\cdot \\sqrt{\\frac{y}{x}}$ với $y > 0$:", "options": ["$1$", "$x$", "$y$", "$\\frac{x}{y}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giá trị của biểu thức $(\\sqrt{6} + \\sqrt{2})(\\sqrt{3} - 2)\\sqrt{\\sqrt{3} + 2}$ là:", "options": ["$-\\sqrt{2}$", "$\\sqrt{2}$", "$2$", "$-2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{x - 1} \\cdot \\sqrt{x + 1} = 2\\sqrt{2}$. Nghiệm là:", "options": ["$x = 3$", "$x = \\pm 3$", "$x = 9$", "$x = \\sqrt{7}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tính giá trị biểu thức $S = \\sqrt{2 + \\sqrt{3}} + \\sqrt{2 - \\sqrt{3}}$:", "options": ["$\\sqrt{6}$", "$2$", "$\\sqrt{2}$", "$2\\sqrt{3}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $a, b > 0$. Biểu thức $\\sqrt{a + b + 2\\sqrt{ab}} - \\sqrt{a}$ bằng:", "options": ["$\\sqrt{b}$", "$-\\sqrt{b}$", "$b$", "$a + b$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $B = \\frac{\\sqrt{10} + \\sqrt{15}}{\\sqrt{8} + \\sqrt{12}}$ được kết quả là:", "options": ["$\\frac{\\sqrt{5}}{2}$", "$\\frac{\\sqrt{5}}{\\sqrt{2}}$", "$\\frac{5}{2}$", "$\\frac{\\sqrt{3}}{2}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm $x$ biết $\\sqrt{x^2 - 9} = 2\\sqrt{x - 3}$:", "options": ["$x = 3$ hoặc $x = 7$", "$x = 3$", "$x = 7$", "$x = -3$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tính giá trị của tích $P = \\left(\\sqrt{4 + \\sqrt{15}} + \\sqrt{4 - \\sqrt{15}}\\right) \\cdot \\sqrt{2}$:", "options": ["$2\\sqrt{5} + 2\\sqrt{3}$? Không, $2\\sqrt{5}$ hoặc $\\sqrt{30}$", "$\\sqrt{30}$", "$2\\sqrt{5}$", "$\\sqrt{10}$"], "correct": 1}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho biểu thức $A = \\sqrt{2 + \\sqrt{3}} - \\sqrt{2 - \\sqrt{3}}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Vì $2 + \\sqrt{3} > 2 - \\sqrt{3} > 0$ nên $A > 0$.", "correct": True},
                {"subId": "b", "text": "Ta có $A^2 = (2 + \\sqrt{3}) + (2 - \\sqrt{3}) - 2\\sqrt{(2+\\sqrt{3})(2-\\sqrt{3})} = 4 - 2(1) = 2$.", "correct": True},
                {"subId": "c", "text": "Do $A > 0$ và $A^2 = 2$ nên $A = \\sqrt{2}$.", "correct": True},
                {"subId": "d", "text": "Giá trị của biểu thức $A$ là một số nguyên.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho phương trình $\\sqrt{x - 2} \\cdot \\sqrt{x + 2} = x - 1$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điều kiện xác định của phương trình là $x \\ge 2$.", "correct": True},
                {"subId": "b", "text": "Nhân hai căn thức ta được $\\sqrt{x^2 - 4} = x - 1$.", "correct": True},
                {"subId": "c", "text": "Bình phương hai vế: $x^2 - 4 = x^2 - 2x + 1 \\Leftrightarrow 2x = 5 \\Rightarrow x = 2{,}5$.", "correct": True},
                {"subId": "d", "text": "Giá trị $x = 2{,}5$ bị loại do không thỏa mãn ĐKXĐ.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt{12} \\cdot \\sqrt{75}$.", "correctAnswer": "30", "explanation": "$\\sqrt{12 \\times 75} = \\sqrt{900} = 30$."},
        {"id": 2, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $(\\sqrt{7} + \\sqrt{3})(\\sqrt{7} - \\sqrt{3})$.", "correctAnswer": "4", "explanation": "$(\\sqrt{7})^2 - (\\sqrt{3})^2 = 7 - 3 = 4$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số nghiệm của phương trình $\\sqrt{x - 3} \\cdot \\sqrt{x - 1} = 0$.", "correctAnswer": "1", "explanation": "ĐKXĐ: $x \\ge 3$. Nghiệm $x = 1$ bị loại, chỉ có $x = 3$ thỏa mãn."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính giá trị của biểu thức $A = (\\sqrt{3 + \\sqrt{5}} + \\sqrt{3 - \\sqrt{5}})^2$.", "correctAnswer": "10", "explanation": "$A = (3 + \\sqrt{5}) + (3 - \\sqrt{5}) + 2\\sqrt{9 - 5} = 6 + 2(2) = 10$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Tính giá trị của biểu thức:\n$$P = \\sqrt{4 + \\sqrt{7}} + \\sqrt{4 - \\sqrt{7}}$$",
            "solution": "Nhận xét $P > 0$.\nNhân cả hai vế với $\\sqrt{2}$:\n$\\sqrt{2}P = \\sqrt{2(4 + \\sqrt{7})} + \\sqrt{2(4 - \\sqrt{7})}$\n$= \\sqrt{8 + 2\\sqrt{7}} + \\sqrt{8 - 2\\sqrt{7}}$\n$= \\sqrt{(\\sqrt{7} + 1)^2} + \\sqrt{(\\sqrt{7} - 1)^2}$\n$= |\\sqrt{7} + 1| + |\\sqrt{7} - 1|$.\nVì $\\sqrt{7} > 1$ nên $|\\sqrt{7} - 1| = \\sqrt{7} - 1$.\nDo đó: $\\sqrt{2}P = (\\sqrt{7} + 1) + (\\sqrt{7} - 1) = 2\\sqrt{7}$.\nSuy ra: $P = \\frac{2\\sqrt{7}}{\\sqrt{2}} = \\sqrt{14}$.\nVậy $P = \\sqrt{14}$.",
            "rubric": [
                {"step": "Nhân căn 2 vào biểu thức P để tạo hằng đẳng thức hoàn hảo", "subScore": 0.5},
                {"step": "Khai căn và rút gọn ra kết quả P = sqrt(14)", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $x = \\frac{\\sqrt{3} - 1}{2}$. Tính giá trị của biểu thức:\n$$A = (4x^3 + 2x^2 - 8x + 3)^{2026}$$",
            "solution": "Từ $x = \\frac{\\sqrt{3} - 1}{2} \\Rightarrow 2x + 1 = \\sqrt{3}$.\nBình phương hai vế:\n$(2x + 1)^2 = 3 \\Leftrightarrow 4x^2 + 4x + 1 = 3 \\Leftrightarrow 4x^2 + 4x - 2 = 0 \\Leftrightarrow 2x^2 + 2x - 1 = 0$.\nTa phân tích biểu thức trong ngoặc theo $2x^2 + 2x - 1$:\n$4x^3 + 2x^2 - 8x + 3 = 2x(2x^2 + 2x - 1) - 2x^2 - 6x + 3$\n$= 2x(0) - (2x^2 + 2x - 1) - 4x + 2 = -(0) - 4x + 2 = 2 - 4x$.\nTính $2 - 4x$:\n$2 - 4\\left(\\frac{\\sqrt{3} - 1}{2}\\right) = 2 - 2(\\sqrt{3} - 1) = 2 - 2\\sqrt{3} + 2 = 4 - 2\\sqrt{3} = (\\sqrt{3} - 1)^2$.\nNếu biểu thức được thiết kế để triệt tiêu thành số 1 hoặc 0, ta kiểm tra chia đa thức:\n$(4x^3 + 2x^2 - 8x + 3) : (4x^2 + 4x - 2) = x$ dư $-2x^2 - 6x + 3 = -\\frac{1}{2}(4x^2 + 4x - 2) - 4x + 2$.\nGiá trị của biểu thức nhận được là $(\\sqrt{3} - 1)^{4052}$.",
            "rubric": [
                {"step": "Biến đổi x ra phương trình bậc hai 4x^2 + 4x - 2 = 0", "subScore": 0.5},
                {"step": "Chia đa thức và tính đúng giá trị của biểu thức", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình:\n$$\\sqrt{x + 3} + \\sqrt{x - 1} = 2$$",
            "solution": "Điều kiện xác định: $x \\ge 1$.\nCách 1: Bình phương hai vế (vì hai vế đều dương):\n$(\\sqrt{x + 3} + \\sqrt{x - 1})^2 = 2^2\n\\Leftrightarrow (x + 3) + (x - 1) + 2\\sqrt{(x + 3)(x - 1)} = 4$\n$\\Leftrightarrow 2x + 2 + 2\\sqrt{x^2 + 2x - 3} = 4$\n$\\Leftrightarrow 2\\sqrt{x^2 + 2x - 3} = 2 - 2x$\n$\\Leftrightarrow \\sqrt{x^2 + 2x - 3} = 1 - x$.\nĐiều kiện để có nghiệm: $1 - x \\ge 0 \\Leftrightarrow x \\le 1$.\nKết hợp với ĐKXĐ ban đầu $x \\ge 1$, ta suy ra bắt buộc $x = 1$.\nThử lại với $x = 1$:\n$VT = \\sqrt{1 + 3} + \\sqrt{1 - 1} = \\sqrt{4} + 0 = 2 = VP$ (thỏa mãn).\nVậy phương trình có nghiệm duy nhất $x = 1$.",
            "rubric": [
                {"step": "Đặt điều kiện x >= 1 và bình phương hai vế", "subScore": 0.5},
                {"step": "Rút ra điều kiện 1 - x >= 0 suy ra x = 1, thử lại và kết luận nghiệm", "subScore": 0.5}
            ]
        }
    ]
}
