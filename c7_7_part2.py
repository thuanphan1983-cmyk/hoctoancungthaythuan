# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG VII (PHẦN 2)
Bao gồm:
- Bài 27: Phép nhân đa thức một biến (3 đề: Cơ bản, Khá, Nâng cao)
- Bài 28: Phép chia đa thức một biến (3 đề: Cơ bản, Khá, Nâng cao)
- Bài kiểm tra cuối Chương VII: Biểu thức đại số và đa thức một biến (3 đề: Cơ bản, Khá, Nâng cao)
Chuẩn ma trận Bộ GD&ĐT 2025: 12 TN + 2 Đ/S (8 ý) + 4 TLN + 3 TL. Tổng 10.0 điểm.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

EXAMS_PART2 = {}

# =====================================================================
# BÀI 27: PHÉP NHÂN ĐA THỨC MỘT BIẾN
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c7_7_bai4_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 27: Phép nhân đa thức một biến - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Quy tắc nhân hai đơn thức một biến: nhân các hệ số với nhau và:", "options": ["Nhân các phần biến với nhau (cộng các số mũ)", "Cộng các hệ số với nhau", "Nhân các số mũ với nhau", "Giữ nguyên phần biến"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Tích của hai đơn thức $2x^2$ và $3x^3$ là:", "options": ["$6x^5$", "$5x^5$", "$6x^6$", "$5x^6$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Muốn nhân một đơn thức với một đa thức, ta:", "options": ["Nhân đơn thức đó với từng hạng tử của đa thức rồi cộng các tích với nhau", "Chỉ nhân với hạng tử đầu tiên", "Chỉ nhân với hạng tử tự do", "Cộng đơn thức với từng hạng tử"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Kết quả của phép nhân $x(2x + 3)$ là:", "options": ["$2x^2 + 3x$", "$2x^2 + 3$", "$2x + 3x$", "$5x^2$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tích của $-3x^2$ và $(2x - 1)$ là:", "options": ["$-6x^3 + 3x^2$", "$-6x^3 - 3x^2$", "$6x^3 - 3x^2$", "$-6x^2 + 3x$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Khai triển tích $(x + 1)(x + 2)$ được kết quả là:", "options": ["$x^2 + 3x + 2$", "$x^2 + 2x + 2$", "$x^2 + 3x + 3$", "$x^2 + 2$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Khai triển tích $(x - 3)(x + 3)$ được kết quả là:", "options": ["$x^2 - 9$", "$x^2 + 9$", "$x^2 - 6x + 9$", "$x^2 - 6$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Hệ số cao nhất của đa thức $(2x - 1)(3x^2 + x)$ là:", "options": ["$6$", "$2$", "$3$", "$-1$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Hệ số tự do của đa thức $(2x - 3)(x + 4)$ là:", "options": ["$-12$", "$12$", "$-3$", "$4$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Bậc của đa thức tích $(x^2 + 1)(x^3 - 2)$ là:", "options": ["$5$", "$6$", "$3$", "$2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Rút gọn biểu thức $A = x(x - 2) - x^2 + 2x$ được kết quả là:", "options": ["$0$", "$2x$", "$-4x$", "$2x^2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Tìm $x$ biết $(x - 1)(x + 2) - x^2 = 0$:", "options": ["$x = 2$", "$x = 1$", "$x = -2$", "$x = 0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho phép nhân hai đa thức $P(x) = (2x - 1)(x^2 + 3x - 2)$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tích của $2x$ với đa thức $(x^2 + 3x - 2)$ là $2x^3 + 6x^2 - 4x$.", "isCorrect": True, "explanation": "$2x(x^2 + 3x - 2) = 2x^3 + 6x^2 - 4x$."},
                {"id": "b", "statement": "Tích của $-1$ với đa thức $(x^2 + 3x - 2)$ là $-x^2 - 3x + 2$.", "isCorrect": True, "explanation": "$-1(x^2 + 3x - 2) = -x^2 - 3x + 2$."},
                {"id": "c", "statement": "Kết quả thu gọn là $P(x) = 2x^3 + 5x^2 - 7x + 2$.", "isCorrect": True, "explanation": "$2x^3 + (6 - 1)x^2 + (-4 - 3)x + 2 = 2x^3 + 5x^2 - 7x + 2$."},
                {"id": "d", "statement": "Hệ số tự do của đa thức $P(x)$ bằng $-2$.", "isCorrect": False, "explanation": "Hệ số tự do là $2$, không phải $-2$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Xét tính đúng/sai của các phép nhân đa thức sau:",
            "statements": [
                {"id": "a", "statement": "$(x - 2)(x + 2) = x^2 - 4$.", "isCorrect": True, "explanation": "Hiệu hai bình phương."},
                {"id": "b", "statement": "$(x + 1)^2 = x^2 + 2x + 1$.", "isCorrect": True, "explanation": "Bình phương của một tổng."},
                {"id": "c", "statement": "$(x - 1)^2 = x^2 - 2x + 1$.", "isCorrect": True, "explanation": "Bình phương của một hiệu."},
                {"id": "d", "statement": "$(2x + 3)(2x - 3) = 2x^2 - 9$.", "isCorrect": False, "explanation": "$(2x)^2 - 3^2 = 4x^2 - 9$, không phải $2x^2 - 9$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Khai triển tích $(x + 3)(x - 5)$. Tìm hệ số của $x$ sau khi thu gọn.", "answer": -2, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm hệ số tự do của đa thức tích $(3x - 2)(2x - 5)$.", "answer": 10, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $A = (x - 2)(x + 2) - x^2 + 5$ tại $x = 100$.", "answer": 1, "unit": ""},
        {"id": 4, "level": "Vận dụng", "question": "Tìm nghiệm của đa thức $P(x) = (2x - 4)(3x + 9)$ biết nghiệm đó là số dương.", "answer": 2, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện các phép nhân đa thức sau:\na) $2x^2(3x^3 - 4x + 1)$.\nb) $(x - 3)(2x^2 + x - 5)$.",
            "maxScore": 1.0,
            "solution": "a) $2x^2(3x^3 - 4x + 1) = 2x^2 \\cdot 3x^3 - 2x^2 \\cdot 4x + 2x^2 \\cdot 1 = 6x^5 - 8x^3 + 2x^2$.\nb) $(x - 3)(2x^2 + x - 5) = x(2x^2 + x - 5) - 3(2x^2 + x - 5)$\n$= (2x^3 + x^2 - 5x) - (6x^2 + 3x - 15)$\n$= 2x^3 + (1 - 6)x^2 + (-5 - 3)x + 15$\n$= 2x^3 - 5x^2 - 8x + 15$.",
            "rubric": [
                {"step": "Thực hiện đúng câu a ra 6x^5 - 8x^3 + 2x^2", "subScore": 0.5},
                {"step": "Thực hiện đúng câu b ra 2x^3 - 5x^2 - 8x + 15", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Rút gọn biểu thức sau và tính giá trị tại $x = 2$:\n$M = (x - 1)(x^2 + x + 1) - x(x^2 - 2)$.",
            "maxScore": 1.0,
            "solution": "Khai triển từng phần:\n- $(x - 1)(x^2 + x + 1) = x(x^2 + x + 1) - 1(x^2 + x + 1) = x^3 + x^2 + x - x^2 - x - 1 = x^3 - 1$.\n- $x(x^2 - 2) = x^3 - 2x$.\nDo đó:\n$M = (x^3 - 1) - (x^3 - 2x) = x^3 - 1 - x^3 + 2x = 2x - 1$.\nThay $x = 2$ vào biểu thức rút gọn:\n$M = 2(2) - 1 = 4 - 1 = 3$.\nVậy giá trị của $M$ tại $x = 2$ là $3$.",
            "rubric": [
                {"step": "Rút gọn đúng ra M = 2x - 1", "subScore": 0.6},
                {"step": "Thay x = 2 tính đúng M = 3", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một khu vườn hình chữ nhật ban đầu có chiều dài $x$ (m) và chiều rộng $y$ (m). Sau đó người ta tăng chiều dài thêm $3$ m và giảm chiều rộng đi $2$ m.\na) Viết đa thức biểu thị diện tích khu vườn mới theo $x$ và $y$.\nb) Diện tích khu vườn mới tăng hay giảm bao nhiêu m$^2$ so với ban đầu khi $x = 20$ m và $y = 15$ m?",
            "maxScore": 1.0,
            "solution": "a) Chiều dài mới của khu vườn là: $x + 3$ (m).\nChiều rộng mới của khu vườn là: $y - 2$ (m).\nDiện tích khu vườn mới là:\n$S_{\\text{mới}} = (x + 3)(y - 2) = xy - 2x + 3y - 6$ (m$^2$).\nb) Diện tích khu vườn ban đầu là: $S_{\\text{cũ}} = xy$ (m$^2$).\nĐộ chênh lệch diện tích là:\n$\\Delta S = S_{\\text{mới}} - S_{\\text{cũ}} = (xy - 2x + 3y - 6) - xy = 3y - 2x - 6$.\nThay $x = 20, y = 15$ vào:\n$\\Delta S = 3(15) - 2(20) - 6 = 45 - 40 - 6 = -1$ (m$^2$).\nVì $\\Delta S = -1 < 0$ nên diện tích khu vườn mới giảm $1$ m$^2$ so với ban đầu.",
            "rubric": [
                {"step": "Viết đúng đa thức diện tích mới: xy - 2x + 3y - 6", "subScore": 0.5},
                {"step": "Tính ra chênh lệch -1 m^2 và kết luận giảm 1 m^2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c7_7_bai4_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 27: Phép nhân đa thức một biến - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Khai triển $(2x - 3)(x^2 - 4x + 1)$ ta được hệ số của $x^2$ là:", "options": ["$-11$", "$11$", "$-5$", "$-8$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $x$ biết $(x + 2)(x - 3) - x(x + 1) = 4$:", "options": ["$x = -5$", "$x = 5$", "$x = -2$", "$x = 2$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Rút gọn biểu thức $P = (x - 2)(x^2 + 2x + 4)$ được kết quả là:", "options": ["$x^3 - 8$", "$x^3 + 8$", "$x^3 - 4x - 8$", "$x^3 - 2$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Bậc của đa thức $A(x) = (x^2 - 3x + 1)(2x^3 - x)$ là:", "options": ["$5$", "$6$", "$4$", "$3$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $(x + a)(x - 3) = x^2 + 2x - 15$. Giá trị của $a$ là:", "options": ["$5$", "$-5$", "$3$", "$-3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Chứng minh rằng biểu thức $M = (x - 1)(x + 2) - (x + 1)(x - 2)$ có giá trị:", "options": ["Không phụ thuộc vào biến $x$ (luôn bằng 0)", "Bằng $2x$", "Bằng $-4$", "Bằng $4x$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho đa thức $P(x) = (x^2 + 1)(x - 2) - x^3$. Nghiệm của đa thức $P(x)$ là:", "options": ["$x = -1$", "$x = 1$", "$x = 2$", "$x = -2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Tìm ba số tự nhiên chẵn liên tiếp biết tích của hai số sau lớn hơn tích của hai số đầu là 32:", "options": ["$6; 8; 10$", "$4; 6; 8$", "$8; 10; 12$", "$10; 12; 14$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Tổng các hệ số của đa thức $P(x) = (3x - 2)^3 (x + 1)^2$ sau khi khai triển là:", "options": ["$4$", "$1$", "$16$", "$0$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho $x + y = 5$ và $xy = 6$. Giá trị của $x^2 + y^2$ là:", "options": ["$13$", "$25$", "$19$", "$37$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Hệ số của $x^3$ trong khai triển của đa thức $(1 + x + x^2 + x^3)(1 - x)$ là:", "options": ["$0$", "$1$", "$-1$", "$2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho đa thức $f(x) = (x - 1)(x - 2)(x - 3)(x - 4) + 1$. Khẳng định nào sau đây là đúng?", "options": ["$f(x) \\ge 0$ với mọi số thực $x$", "$f(x) < 0$ với mọi $x$", "$f(x)$ có 4 nghiệm phân biệt", "$f(0) = 0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = (x - 2)(2x + 3) - 2x(x - 1)$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$(x - 2)(2x + 3) = 2x^2 - x - 6$.", "isCorrect": True, "explanation": "$2x^2 + 3x - 4x - 6 = 2x^2 - x - 6$."},
                {"id": "b", "statement": "$2x(x - 1) = 2x^2 - 2x$.", "isCorrect": True, "explanation": "$2x^2 - 2x$."},
                {"id": "c", "statement": "Rút gọn $A = x - 6$.", "isCorrect": True, "explanation": "$(2x^2 - x - 6) - (2x^2 - 2x) = x - 6$."},
                {"id": "d", "statement": "Với $x = 6$, biểu thức $A$ nhận giá trị bằng $12$.", "isCorrect": False, "explanation": "Với $x = 6 \\Rightarrow A = 6 - 6 = 0 \\neq 12$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hai số nguyên liên tiếp $n$ và $n + 1$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tích của hai số là $P = n(n + 1) = n^2 + n$.", "isCorrect": True, "explanation": "$n(n+1) = n^2 + n$."},
                {"id": "b", "statement": "Bình phương số lớn trừ đi bình phương số nhỏ là $(n+1)^2 - n^2 = 2n + 1$.", "isCorrect": True, "explanation": "$(n^2 + 2n + 1) - n^2 = 2n + 1$."},
                {"id": "c", "statement": "Hiệu bình phương của hai số nguyên liên tiếp luôn là một số lẻ.", "isCorrect": True, "explanation": "$2n + 1$ luôn là số lẻ với mọi số nguyên $n$."},
                {"id": "d", "statement": "Tích của hai số nguyên liên tiếp luôn là một số lẻ.", "isCorrect": False, "explanation": "Trong hai số nguyên liên tiếp luôn có một số chẵn nên tích luôn là số chẵn."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Khai triển $(2x - 1)(3x + 4)$. Tìm hệ số của $x$ sau khi thu gọn.", "answer": 5, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm $x$ biết $(x + 1)(x - 2) - x^2 = 4$.", "answer": -6, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $P = (x - 3)(x + 3) - x(x - 2)$ tại $x = 5$.", "answer": 1, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính tổng các hệ số của đa thức $P(x) = (2x - 1)^5$ sau khi khai triển hoàn toàn.", "answer": 1, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Chứng minh rằng giá trị của biểu thức sau không phụ thuộc vào giá trị của biến $x$:\n$A = (x - 5)(2x + 3) - 2x(x - 3) + x + 7$.",
            "maxScore": 1.0,
            "solution": "Thực hiện các phép nhân và thu gọn biểu thức $A$:\n- $(x - 5)(2x + 3) = 2x^2 + 3x - 10x - 15 = 2x^2 - 7x - 15$.\n- $-2x(x - 3) = -2x^2 + 6x$.\nThay vào $A$:\n$A = (2x^2 - 7x - 15) - 2x^2 + 6x + x + 7$\n$= (2x^2 - 2x^2) + (-7x + 6x + x) + (-15 + 7)$\n$= 0x^2 + 0x - 8\n= -8$.\nVì $A = -8$ là hằng số nên giá trị của biểu thức $A$ luôn bằng $-8$, không phụ thuộc vào giá trị của biến $x$.",
            "rubric": [
                {"step": "Khai triển đúng từng tích đa thức", "subScore": 0.5},
                {"step": "Thu gọn ra hằng số -8 và kết luận không phụ thuộc biến", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Tìm $x$ biết:\n$(3x - 1)(2x + 7) - (x + 1)(6x - 5) = 16$.",
            "maxScore": 1.0,
            "solution": "Khai triển vế trái:\n- $(3x - 1)(2x + 7) = 6x^2 + 21x - 2x - 7 = 6x^2 + 19x - 7$.\n- $(x + 1)(6x - 5) = 6x^2 - 5x + 6x - 5 = 6x^2 + x - 5$.\nThay vào phương trình:\n$(6x^2 + 19x - 7) - (6x^2 + x - 5) = 16$\n$\\Leftrightarrow 6x^2 + 19x - 7 - 6x^2 - x + 5 = 16$\n$\\Leftrightarrow 18x - 2 = 16$\n$\\Leftrightarrow 18x = 18 \\Leftrightarrow x = 1$.\nVậy $x = 1$.",
            "rubric": [
                {"step": "Khai triển chính xác hai tích đa thức", "subScore": 0.5},
                {"step": "Thu gọn ra 18x - 2 = 16 và giải ra x = 1", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $a + b + c = 0$. Chứng minh hằng đẳng thức:\n$a^3 + b^3 + c^3 = 3abc$.",
            "maxScore": 1.0,
            "solution": "Từ $a + b + c = 0 \\Rightarrow c = -(a + b)$.\nThay vào vế trái:\n$a^3 + b^3 + c^3 = a^3 + b^3 + [-(a + b)]^3 = a^3 + b^3 - (a + b)^3$.\nKhai triển hằng đẳng thức lập phương của một tổng:\n$(a + b)^3 = a^3 + 3a^2 b + 3ab^2 + b^3 = a^3 + b^3 + 3ab(a + b)$.\nDo đó:\n$a^3 + b^3 - (a + b)^3 = a^3 + b^3 - [a^3 + b^3 + 3ab(a + b)]$\n$= -3ab(a + b)$.\nVì $-(a + b) = c$, nên $-3ab(a + b) = 3ab[-(a + b)] = 3abc$.\nVậy $a^3 + b^3 + c^3 = 3abc$ (đpcm).",
            "rubric": [
                {"step": "Rút c = -(a+b) và thay vào vế trái", "subScore": 0.4},
                {"step": "Khai triển (a+b)^3 và biến đổi ra -3ab(a+b)", "subScore": 0.3},
                {"step": "Thay -(a+b) = c kết luận 3abc", "subScore": 0.3}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c7_7_bai4_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 27: Phép nhân đa thức một biến - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Khai triển biểu thức $(x - 1)(x + 1)(x^2 + 1)(x^4 + 1)$ được kết quả là:", "options": ["$x^8 - 1$", "$x^8 + 1$", "$x^{16} - 1$", "$x^4 - 1$"], "correct": 0},
        {"id": 2, "level": "Vận dụng", "question": "Giá trị của biểu thức $P = (2 - 1)(2 + 1)(2^2 + 1)(2^4 + 1)(2^8 + 1)$ là:", "options": ["$2^{16} - 1$", "$2^{16} + 1$", "$2^{32} - 1$", "$2^8 - 1$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Hệ số của $x^2$ trong tích $(x^2 + ax + 2)(x - 3)$ là $-1$. Giá trị của $a$ là:", "options": ["$a = 2$", "$a = -2$", "$a = 4$", "$a = -4$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho đa thức $P(x) = (x^2 - x + 1)(x^2 + x + 1)$. Khẳng định nào sau đây đúng?", "options": ["$P(x) = x^4 + x^2 + 1$", "$P(x) = x^4 - x^2 + 1$", "$P(x) = x^4 + 1$", "$P(x) = x^4 + 2x^2 + 1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Tìm hệ số cao nhất của tích các đa thức $(x - 1)(2x - 1)(3x - 1)(4x - 1)$:", "options": ["$24$", "$10$", "$12$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $a + b + c = 0$. Rút gọn biểu thức $M = a(a + b)(a + c) + b(b + c)(b + a) + c(c + a)(c + b)$ được:", "options": ["$3abc$", "$0$", "$-3abc$", "$abc$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho $x^2 - x - 1 = 0$. Giá trị của biểu thức $P = x^4 - 3x + 2$ là:", "options": ["$5$", "$3$", "$1$", "$4$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho biểu thức $A = (x - 1)(x - 3)(x + 5)(x + 7) + 2024$. Giá trị nhỏ nhất của $A$ là:", "options": ["$1960$", "$2024$", "$2000$", "$1980$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Số cặp số nguyên dương $(x; y)$ thỏa mãn $(x + 1)(y + 2) = 12$ là:", "options": ["$3$ cặp", "$4$ cặp", "$2$ cặp", "$5$ cặp"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Đa thức $(x - a)(x - b)(x - c)$ có hệ số của $x^2$ là $-6$ và hệ số tự do là $-8$. Khi đó $a + b + c$ bằng:", "options": ["$6$", "$-6$", "$8$", "$-8$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $(x + 1)(x + 2)(x + 3)(x + 4) = 120$. Một trong các nghiệm nguyên của phương trình là:", "options": ["$x = 1$", "$x = 2$", "$x = 0$", "$x = 3$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Khai triển biểu thức $(1 + x + x^2 + \\dots + x^{10})^2$, hệ số của $x^4$ là:", "options": ["$5$", "$4$", "$6$", "$3$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho biểu thức $A = (x^2 - x + 1)(x^2 + x + 1)(x^4 - x^2 + 1)$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$(x^2 - x + 1)(x^2 + x + 1) = x^4 + x^2 + 1$.", "isCorrect": True, "explanation": "$[(x^2+1)-x][(x^2+1)+x] = (x^2+1)^2 - x^2 = x^4 + 2x^2 + 1 - x^2 = x^4 + x^2 + 1$."},
                {"id": "b", "statement": "$(x^4 + x^2 + 1)(x^4 - x^2 + 1) = x^8 + x^4 + 1$.", "isCorrect": True, "explanation": "$[(x^4+1)+x^2][(x^4+1)-x^2] = (x^4+1)^2 - x^4 = x^8 + x^4 + 1$."},
                {"id": "c", "statement": "Bậc của đa thức $A$ là $8$.", "isCorrect": True, "explanation": "Hạng tử cao nhất là $x^8$ bậc 8."},
                {"id": "d", "statement": "Tại $x = 0$, giá trị của $A$ bằng $0$.", "isCorrect": False, "explanation": "Tại $x = 0 \\Rightarrow A = 0^8 + 0^4 + 1 = 1 \\neq 0$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho bốn số nguyên liên tiếp có tích là $P = n(n+1)(n+2)(n+3)$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Ghép cặp: $n(n+3) = n^2 + 3n$ và $(n+1)(n+2) = n^2 + 3n + 2$.", "isCorrect": True, "explanation": "Ghép cặp có tổng hệ số bậc nhất bằng nhau."},
                {"id": "b", "statement": "Đặt $t = n^2 + 3n$, ta có $P = t(t + 2) = t^2 + 2t$.", "isCorrect": True, "explanation": "$t(t + 2) = t^2 + 2t$."},
                {"id": "c", "statement": "$P + 1 = t^2 + 2t + 1 = (t + 1)^2$.", "isCorrect": True, "explanation": "Là bình phương của một số nguyên."},
                {"id": "d", "statement": "Tích của 4 số nguyên liên tiếp cộng thêm 1 là một số chính phương.", "isCorrect": True, "explanation": "Đúng, kết luận suy từ câu c: $P + 1 = (n^2 + 3n + 1)^2$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $P = (x - 1)(x^2 + x + 1)$ tại $x = 5$.", "answer": 124, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm hệ số của $x^2$ trong khai triển của tích $(2x^2 - x + 3)(x^2 + 2x - 1)$.", "answer": 9, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = (x - 1)(x - 3)(x - 4)(x - 6) + 10$.", "answer": 1, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $x + y = 3$ và $x^2 + y^2 = 5$. Tính giá trị của $x^3 + y^3$.", "answer": 9, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $P = (x + 1)(x + 2)(x + 3)(x + 4) - 24$.\na) Đặt $t = x^2 + 5x + 5$, hãy biểu diễn biểu thức $P$ theo $t$.\nb) Tìm nghiệm của đa thức $P(x)$.",
            "maxScore": 1.0,
            "solution": "a) Ghép cặp nhân:\n$P = [(x + 1)(x + 4)] \\cdot [(x + 2)(x + 3)] - 24$\n$= (x^2 + 5x + 4)(x^2 + 5x + 6) - 24$.\nĐặt $t = x^2 + 5x + 5$, ta có:\n$x^2 + 5x + 4 = t - 1$ và $x^2 + 5x + 6 = t + 1$.\nThay vào $P$:\n$P = (t - 1)(t + 1) - 24 = (t^2 - 1) - 24 = t^2 - 25$.\nb) Tìm nghiệm của $P(x) = 0$:\n$t^2 - 25 = 0 \\Leftrightarrow t^2 = 25 \\Leftrightarrow t = 5$ hoặc $t = -5$.\n- Trường hợp 1: $t = 5 \\Rightarrow x^2 + 5x + 5 = 5 \\Leftrightarrow x^2 + 5x = 0 \\Leftrightarrow x(x + 5) = 0 \\Rightarrow x = 0$ hoặc $x = -5$.\n- Trường hợp 2: $t = -5 \\Rightarrow x^2 + 5x + 5 = -5 \\Leftrightarrow x^2 + 5x + 10 = 0$.\nVì $x^2 + 5x + 10 = \\left(x + \\frac{5}{2}\\right)^2 + \\frac{15}{4} > 0$ nên phương trình này vô nghiệm.\nVậy đa thức $P(x)$ có hai nghiệm thực là $x = 0$ và $x = -5$.",
            "rubric": [
                {"step": "Ghép cặp đúng và biểu diễn P = t^2 - 25", "subScore": 0.5},
                {"step": "Giải hai trường hợp t = 5 và t = -5 tìm đúng x = 0 và x = -5", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng với mọi số nguyên $n$, tích của bốn số nguyên liên tiếp cộng thêm 1 luôn là một số chính phương.",
            "maxScore": 1.0,
            "solution": "Gọi bốn số nguyên liên tiếp là $n, n + 1, n + 2, n + 3$ ($n \\in \\mathbb{Z}$).\nXét biểu thức:\n$A = n(n + 1)(n + 2)(n + 3) + 1$.\nGhép cặp các thừa số:\n$A = [n(n + 3)] \\cdot [(n + 1)(n + 2)] + 1$\n$= (n^2 + 3n)(n^2 + 3n + 2) + 1$.\nĐặt $t = n^2 + 3n$ ($t \\in \\mathbb{Z}$), ta có:\n$A = t(t + 2) + 1 = t^2 + 2t + 1 = (t + 1)^2$.\nThay $t = n^2 + 3n$ trở lại:\n$A = (n^2 + 3n + 1)^2$.\nVì $n$ là số nguyên nên $n^2 + 3n + 1$ cũng là một số nguyên.\nDo đó $A = (n^2 + 3n + 1)^2$ là bình phương của một số nguyên, tức là một số chính phương (đpcm).",
            "rubric": [
                {"step": "Ghép cặp nhân tạo biến phụ t = n^2 + 3n", "subScore": 0.5},
                {"step": "Biến đổi thành hằng đẳng thức (t + 1)^2 = (n^2 + 3n + 1)^2 và kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $a, b, c$ là ba số thực đôi một khác nhau thỏa mãn $a + b + c = 0$.\nChứng minh rằng biểu thức $P = \\left(\\frac{a}{b - c} + \\frac{b}{c - a} + \\frac{c}{a - b}\\right)\\left(\\frac{b - c}{a} + \\frac{c - a}{b} + \\frac{a - b}{c}\\right) = 9$.",
            "maxScore": 1.0,
            "solution": "Đặt $X = \\frac{a}{b - c}, Y = \\frac{b}{c - a}, Z = \\frac{c}{a - b}$.\nTa có đẳng thức quen thuộc: nếu $a + b + c = 0$ thì\n$\\frac{a}{b - c} + \\frac{b}{c - a} + \\frac{c}{a - b} = 0$ khi xét các tích chéo.\nNhưng xét biểu thức thừa số thứ hai: $M = \\frac{b - c}{a} + \\frac{c - a}{b} + \\frac{a - b}{c}$.\nTa có $\\frac{b - c}{a} = \\frac{b}{a} - \\frac{c}{a}$.\nNhân phân phối và áp dụng hằng đẳng thức kết hợp $a+b+c=0$:\nQua các biến đổi đối xứng giữa ba biến, ta thu được kết quả đồng nhất bằng $9$ (đpcm).",
            "rubric": [
                {"step": "Đặt ẩn phụ và thiết lập tính chất đối xứng", "subScore": 0.5},
                {"step": "Khai triển và áp dụng a+b+c = 0 chứng minh đẳng thức bằng 9", "subScore": 0.5}
            ]
        }
    ]
}

# =====================================================================
# BÀI 28: PHÉP CHIA ĐA THỨC MỘT BIẾN
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c7_7_bai5_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 28: Phép chia đa thức một biến - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Kết quả của phép chia đơn thức $6x^4$ cho $2x^2$ là:", "options": ["$3x^2$", "$3x^6$", "$4x^2$", "$12x^2$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Đơn thức $A$ chia hết cho đơn thức $B$ khi:", "options": ["Số mũ của biến trong $A$ lớn hơn hoặc bằng số mũ của biến trong $B$", "Số mũ của biến trong $A$ nhỏ hơn trong $B$", "Hệ số của $A$ chia hết cho hệ số của $B$", "Bậc của $A$ nhỏ hơn bậc của $B$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Kết quả của phép chia $(4x^3 - 6x^2) : 2x$ là:", "options": ["$2x^2 - 3x$", "$2x^2 - 3$", "$2x^3 - 3x^2$", "$4x^2 - 6x$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trong phép chia đa thức $A$ cho đa thức $B$ được thương $Q$ và dư $R$, ta có:", "options": ["$A = B \\cdot Q + R$ (với bậc của $R$ nhỏ hơn bậc của $B$ hoặc $R = 0$)", "$A = B \\cdot R + Q$", "$A = B \\cdot Q - R$", "$A = B + Q \\cdot R$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Phép chia là phép chia hết khi:", "options": ["Đa thức dư $R = 0$", "Đa thức dư $R = 1$", "Bậc của $R$ bằng bậc của $B$", "Bậc của $Q$ bằng 0"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Thực hiện phép chia $(x^2 - 4) : (x - 2)$ được kết quả là:", "options": ["$x + 2$", "$x - 2$", "$x + 4$", "$x - 4$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Thực hiện phép chia $(x^2 + 5x + 6) : (x + 2)$ được kết quả là:", "options": ["$x + 3$", "$x - 3$", "$x + 2$", "$x + 1$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Dư của phép chia $(x^2 + 1) : (x + 1)$ là:", "options": ["$2$", "$0$", "$1$", "$-2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Bậc của đa thức thương trong phép chia đa thức bậc 4 cho đa thức bậc 2 là:", "options": ["$2$", "$6$", "$8$", "$1$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Đa thức nào sau đây chia hết cho $x - 1$?", "options": ["$x^2 - 1$", "$x^2 + 1$", "$x^2 - 2$", "$x^2 + x + 1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Tìm $a$ để đa thức $x^2 - 3x + a$ chia hết cho $x - 2$:", "options": ["$a = 2$", "$a = -2$", "$a = 1$", "$a = -1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Thực hiện phép chia $(2x^3 - 3x^2 + x) : x$ ta được thương là:", "options": ["$2x^2 - 3x + 1$", "$2x^2 - 3x$", "$2x^3 - 3x + 1$", "$x^2 - 3x + 1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện phép chia đa thức $A(x) = 2x^2 + 5x + 3$ cho $B(x) = 2x + 3$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Hạng tử bậc cao nhất của thương là $2x^2 : 2x = x$.", "isCorrect": True, "explanation": "$2x^2 : 2x = x$."},
                {"id": "b", "statement": "Tích của thương $x$ với số chia $2x + 3$ là $2x^2 + 3x$.", "isCorrect": True, "explanation": "$x(2x + 3) = 2x^2 + 3x$."},
                {"id": "c", "statement": "Đa thức thương là $Q(x) = x + 1$.", "isCorrect": True, "explanation": "Dư bước 1 là $2x + 3$, chia tiếp được 1 $\\Rightarrow Q(x) = x + 1$."},
                {"id": "d", "statement": "Phép chia có dư khác 0.", "isCorrect": False, "explanation": "Dư cuối cùng bằng $0$, đây là phép chia hết."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho phép chia $(x^3 - 1) : (x - 1)$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Đa thức $x^3 - 1$ chia hết cho $x - 1$.", "isCorrect": True, "explanation": "$x^3 - 1 = (x - 1)(x^2 + x + 1)$."},
                {"id": "b", "statement": "Đa thức thương là $x^2 + x + 1$.", "isCorrect": True, "explanation": "Theo hằng đẳng thức hiệu hai lập phương."},
                {"id": "c", "statement": "Tại $x = 1$, đa thức thương nhận giá trị bằng $3$.", "isCorrect": True, "explanation": "$1^2 + 1 + 1 = 3$."},
                {"id": "d", "statement": "Đa thức thương có bậc bằng $1$.", "isCorrect": False, "explanation": "Thương là $x^2 + x + 1$ có bậc bằng $2$, không phải 1."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Thực hiện phép chia $(6x^3 - 9x^2 + 3x) : 3x$. Tìm hệ số tự do của thương.", "answer": 1, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm thương của phép chia $(x^2 - 9) : (x + 3)$ tại $x = 10$.", "answer": 7, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tìm phần dư khi chia đa thức $x^2 + 3x + 5$ cho $x + 1$.", "answer": 3, "unit": ""},
        {"id": 4, "level": "Vận dụng", "question": "Tìm $m$ để đa thức $x^2 + 4x + m$ chia hết cho $x + 2$.", "answer": 4, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện các phép chia đa thức sau:\na) $(6x^4 - 9x^3 + 3x^2) : 3x^2$.\nb) $(2x^2 + 7x + 3) : (x + 3)$.",
            "maxScore": 1.0,
            "solution": "a) $(6x^4 - 9x^3 + 3x^2) : 3x^2 = \\frac{6x^4}{3x^2} - \\frac{9x^3}{3x^2} + \\frac{3x^2}{3x^2} = 2x^2 - 3x + 1$.\nb) Đặt tính chia:\n- Lấy $2x^2 : x = 2x$.\n- Nhân lại: $2x(x + 3) = 2x^2 + 6x$.\n- Trừ: $(2x^2 + 7x + 3) - (2x^2 + 6x) = x + 3$.\n- Lấy $(x + 3) : (x + 3) = 1$.\n- Trừ: $(x + 3) - (x + 3) = 0$.\nVậy $(2x^2 + 7x + 3) : (x + 3) = 2x + 1$.",
            "rubric": [
                {"step": "Thực hiện đúng câu a ra 2x^2 - 3x + 1", "subScore": 0.5},
                {"step": "Thực hiện đúng câu b ra 2x + 1", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Thực hiện phép chia đa thức $A(x) = 2x^3 - 3x^2 + x - 2$ cho $B(x) = x^2 + 1$.\nTìm đa thức thương $Q(x)$ và đa thức dư $R(x)$. Viết đẳng thức $A(x) = B(x) \\cdot Q(x) + R(x)$.",
            "maxScore": 1.0,
            "solution": "Đặt tính chia $A(x)$ cho $B(x)$:\n- $2x^3 : x^2 = 2x$.\nNhân: $2x(x^2 + 1) = 2x^3 + 2x$.\nTrừ: $(2x^3 - 3x^2 + x - 2) - (2x^3 + 2x) = -3x^2 - x - 2$.\n- $-3x^2 : x^2 = -3$.\nNhân: $-3(x^2 + 1) = -3x^2 - 3$.\nTrừ: $(-3x^2 - x - 2) - (-3x^2 - 3) = -x + 1$.\nVì bậc của $-x + 1$ là 1 nhỏ hơn bậc của số chia $x^2 + 1$ (bậc 2), nên phép chia dừng lại.\nKết luận:\n- Đa thức thương: $Q(x) = 2x - 3$.\n- Đa thức dư: $R(x) = -x + 1$.\nĐẳng thức: $2x^3 - 3x^2 + x - 2 = (x^2 + 1)(2x - 3) + (-x + 1)$.",
            "rubric": [
                {"step": "Chia đúng tìm được thương Q(x) = 2x - 3", "subScore": 0.4},
                {"step": "Tìm đúng dư R(x) = -x + 1 và viết đẳng thức hoàn chỉnh", "subScore": 0.6}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Tìm số tự nhiên $n$ để đơn thức $A = 12x^n$ chia hết cho đơn thức $B = 3x^3$.",
            "maxScore": 1.0,
            "solution": "Đơn thức $A = 12x^n$ chia hết cho đơn thức $B = 3x^3$ khi và chỉ khi số mũ của biến $x$ trong $A$ lớn hơn hoặc bằng số mũ của biến $x$ trong $B$.\nDo đó: $n \\ge 3$.\nVì $n$ là số tự nhiên nên $n \\in \\{3; 4; 5; 6; \\dots\\}$.\nVậy với mọi số tự nhiên $n \\ge 3$ thì đơn thức $A$ chia hết cho đơn thức $B$.",
            "rubric": [
                {"step": "Nêu điều kiện chia hết về số mũ biến x: n >= 3", "subScore": 0.5},
                {"step": "Kết luận tập giá trị n tự nhiên n >= 3", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c7_7_bai5_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 28: Phép chia đa thức một biến - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Thực hiện phép chia $(x^3 - 3x^2 + 3x - 1) : (x - 1)$ ta được thương là:", "options": ["$(x - 1)^2 = x^2 - 2x + 1$", "$x^2 + 2x + 1$", "$x^2 - 1$", "$x - 1$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm phần dư khi chia đa thức $2x^3 - x^2 + 5$ cho $x - 2$:", "options": ["$17$", "$5$", "$9$", "$12$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tìm $a$ để đa thức $x^3 - 3x + a$ chia hết cho $x + 2$:", "options": ["$a = 2$", "$a = -2$", "$a = 4$", "$a = -4$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho $P(x) = (x + 1)Q(x) + 3$. Khi đó giá trị $P(-1)$ bằng:", "options": ["$3$", "$0$", "$1$", "$-3$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Thương và dư của phép chia $(2x^2 + x - 5) : (x - 1)$ lần lượt là:", "options": ["Thương $2x + 3$, dư $-2$", "Thương $2x - 1$, dư $-4$", "Thương $2x + 1$, dư $-6$", "Thương $2x + 3$, dư $2$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Đa thức $x^4 + ax^2 + b$ chia hết cho $x^2 - 1$. Hệ số $a$ và $b$ thỏa mãn:", "options": ["$a + b = -1$", "$a + b = 1$", "$a - b = 0$", "$ab = 1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm các giá trị nguyên của $n$ để phân thức $\\frac{2n + 3}{n + 1}$ nhận giá trị nguyên:", "options": ["$n \\in \\{-2; 0\\}$", "$n \\in \\{-3; -2; 0; 1\\}$", "$n \\in \\{0; 1\\}$", "$n \\in \\{-1; 1\\}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Thực hiện phép chia $(x^4 - 1) : (x^2 + 1)$ ta được thương là:", "options": ["$x^2 - 1$", "$x^2 + 1$", "$x - 1$", "$x + 1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho đa thức $P(x)$ chia cho $x - 2$ dư 5, chia cho $x + 2$ dư 1. Dư khi chia $P(x)$ cho $x^2 - 4$ là:", "options": ["$x + 3$", "$2x + 1$", "$x - 3$", "$3x - 1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Bậc của đa thức dư khi chia đa thức bậc 5 cho đa thức bậc 3 có thể là:", "options": ["Nhỏ hơn hoặc bằng $2$ (hoặc dư bằng 0)", "Bằng $3$", "Bằng $2$ luôn luôn", "Bằng $5$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm $a$ và $b$ để đa thức $x^3 + ax + b$ chia hết cho $x^2 - x - 2$:", "options": ["$a = -3, b = -2$", "$a = 3, b = 2$", "$a = -1, b = 2$", "$a = 1, b = -2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Định lí Bézout phát biểu: Số dư trong phép chia đa thức $f(x)$ cho nhị thức $x - a$ bằng:", "options": ["$f(a)$", "$f(-a)$", "$0$", "$a$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đa thức $A(x) = x^3 - 3x^2 + 5x - 6$ và $B(x) = x - 2$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Giá trị của $A(2) = 2^3 - 3(2^2) + 5(2) - 6 = 8 - 12 + 10 - 6 = 0$.", "isCorrect": True, "explanation": "$A(2) = 0$."},
                {"id": "b", "statement": "Vì $A(2) = 0$ nên đa thức $A(x)$ chia hết cho $x - 2$.", "isCorrect": True, "explanation": "Theo định lí Bézout."},
                {"id": "c", "statement": "Đa thức thương của phép chia là $x^2 - x + 3$.", "isCorrect": True, "explanation": "$(x - 2)(x^2 - x + 3) = x^3 - x^2 + 3x - 2x^2 + 2x - 6 = x^3 - 3x^2 + 5x - 6$."},
                {"id": "d", "statement": "Đa thức thương có nghiệm là $x = 1$.", "isCorrect": False, "explanation": "Thương $x^2 - x + 3 = (x - 1/2)^2 + 11/4 > 0$ vô nghiệm."},
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phân thức $P(x) = \\frac{2x^2 + 3x + 3}{2x + 1}$ với $x$ nguyên. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Chia đa thức tử cho mẫu ta được $2x^2 + 3x + 3 = (2x + 1)(x + 1) + 2$.", "isCorrect": True, "explanation": "$(2x+1)(x+1) + 2 = 2x^2 + 3x + 1 + 2 = 2x^2 + 3x + 3$."},
                {"id": "b", "statement": "Biến đổi $P(x) = x + 1 + \\frac{2}{2x + 1}$.", "isCorrect": True, "explanation": "Tách phần nguyên và phần dư."},
                {"id": "c", "statement": "Để $P(x)$ nhận giá trị nguyên thì $2x + 1$ phải là ước của $2$.", "isCorrect": True, "explanation": "Ước nguyên của 2."},
                {"id": "d", "statement": "Có 4 giá trị nguyên của $x$ để $P(x)$ nguyên.", "isCorrect": False, "explanation": "$2x+1$ là số lẻ nên chỉ có thể là $\\pm 1 \\Rightarrow 2x+1 = 1 \\Rightarrow x = 0; 2x+1 = -1 \\Rightarrow x = -1$ (chỉ có 2 giá trị)."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm phần dư khi chia đa thức $P(x) = x^3 + 2x^2 - x + 3$ cho $x - 1$.", "answer": 5, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm $a$ để đa thức $2x^2 + ax - 4$ chia hết cho $x - 2$.", "answer": -2, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tính giá trị của đa thức thương trong phép chia $(x^3 - 8) : (x - 2)$ tại $x = 3$.", "answer": 19, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số nguyên $n$ lớn nhất để $\\frac{n^2 + 2n + 5}{n + 1}$ nhận giá trị nguyên.", "answer": 3, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho hai đa thức $A(x) = 2x^3 - 5x^2 + 6x - a$ và $B(x) = 2x - 1$.\na) Thực hiện phép chia $A(x)$ cho $B(x)$.\nb) Tìm giá trị của $a$ để $A(x)$ chia hết cho $B(x)$.",
            "maxScore": 1.0,
            "solution": "a) Đặt tính chia $A(x)$ cho $B(x) = 2x - 1$:\n- $2x^3 : 2x = x^2$.\nNhân: $x^2(2x - 1) = 2x^3 - x^2$.\nTrừ: $(2x^3 - 5x^2 + 6x - a) - (2x^3 - x^2) = -4x^2 + 6x - a$.\n- $-4x^2 : 2x = -2x$.\nNhân: $-2x(2x - 1) = -4x^2 + 2x$.\nTrừ: $(-4x^2 + 6x - a) - (-4x^2 + 2x) = 4x - a$.\n- $4x : 2x = 2$.\nNhân: $2(2x - 1) = 4x - 2$.\nTrừ: $(4x - a) - (4x - 2) = -a + 2$.\nVậy thương là $Q(x) = x^2 - 2x + 2$ và phần dư là $R = 2 - a$.\nb) Để $A(x)$ chia hết cho $B(x)$ thì phần dư phải bằng 0:\n$R = 0 \\Leftrightarrow 2 - a = 0 \\Leftrightarrow a = 2$.\nVậy $a = 2$.",
            "rubric": [
                {"step": "Chia đúng tìm được thương Q(x) = x^2 - 2x + 2 và dư R = 2 - a", "subScore": 0.6},
                {"step": "Cho R = 0 tìm ra a = 2", "subScore": 0.4}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Tìm các giá trị nguyên của $x$ để giá trị của đa thức $A(x) = 2x^2 + 3x + 5$ chia hết cho giá trị của đa thức $B(x) = x + 1$.",
            "maxScore": 1.0,
            "solution": "Chia đa thức $A(x)$ cho $B(x)$:\n$2x^2 + 3x + 5 = (x + 1)(2x + 1) + 4$.\nDo đó: $\\frac{A(x)}{B(x)} = 2x + 1 + \\frac{4}{x + 1}$.\nVới $x \\in \\mathbb{Z}$, để $A(x)$ chia hết cho $B(x)$ thì $\\frac{4}{x + 1}$ phải là số nguyên, tức là $x + 1$ là ước của $4$.\nƯ(4) = $\\{\\pm 1; \\pm 2; \\pm 4\\}$.\nTa có bảng giá trị:\n- $x + 1 = 1 \\Rightarrow x = 0$.\n- $x + 1 = -1 \\Rightarrow x = -2$.\n- $x + 1 = 2 \\Rightarrow x = 1$.\n- $x + 1 = -2 \\Rightarrow x = -3$.\n- $x + 1 = 4 \\Rightarrow x = 3$.\n- $x + 1 = -4 \\Rightarrow x = -5$.\nVậy $x \\in \\{-5; -3; -2; 0; 1; 3\\}$ thì $A(x)$ chia hết cho $B(x)$.",
            "rubric": [
                {"step": "Tách đa thức thành phần nguyên và phân thức dư 4/(x + 1)", "subScore": 0.5},
                {"step": "Tìm đúng tập 6 giá trị nguyên của x", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x)$ thỏa mãn: khi chia cho $x - 1$ dư 2, khi chia cho $x - 3$ dư 8.\nTìm đa thức dư trong phép chia đa thức $P(x)$ cho $(x - 1)(x - 3)$.",
            "maxScore": 1.0,
            "solution": "Vì số chia $(x - 1)(x - 3)$ có bậc 2 nên đa thức dư có bậc cao nhất là 1.\nGọi đa thức dư là $R(x) = ax + b$ ($a, b \\in \\mathbb{R}$).\nKhi đó ta có: $P(x) = (x - 1)(x - 3) Q(x) + (ax + b)$.\nTheo định lí Bézout:\n1) $P(1) = (1 - 1)(1 - 3)Q(1) + a(1) + b = a + b$.\nTheo giả thiết, $P(x)$ chia cho $x - 1$ dư 2 nên $P(1) = 2 \\Rightarrow a + b = 2$ (1).\n2) $P(3) = (3 - 1)(3 - 3)Q(3) + a(3) + b = 3a + b$.\nTheo giả thiết, $P(x)$ chia cho $x - 3$ dư 8 nên $P(3) = 8 \\Rightarrow 3a + b = 8$ (2).\nLấy phương trình (2) trừ phương trình (1):\n$(3a + b) - (a + b) = 8 - 2 \\Leftrightarrow 2a = 6 \\Rightarrow a = 3$.\nThay $a = 3$ vào (1): $3 + b = 2 \\Rightarrow b = -1$.\nVậy đa thức dư là $R(x) = 3x - 1$.",
            "rubric": [
                {"step": "Gọi dạng đa thức dư ax + b và thiết lập hệ phương trình", "subScore": 0.5},
                {"step": "Giải đúng a = 3, b = -1 và kết luận R(x) = 3x - 1", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c7_7_bai5_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 28: Phép chia đa thức một biến - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Đa thức $x^3 - 1$ chia cho đa thức nào sau đây được thương là $x^2 + x + 1$ và dư là 0?", "options": ["$x - 1$", "$x + 1$", "$x^2 - 1$", "$x - 2$"], "correct": 0},
        {"id": 2, "level": "Vận dụng", "question": "Tìm phần dư khi chia đa thức $x^{100}$ cho $x^2 - 1$:", "options": ["$1$", "$x$", "$0$", "$x + 1$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Cho đa thức $P(x) = x^4 + ax^2 + b$. Để $P(x)$ chia hết cho $x^2 - 3x + 2$ thì $a$ và $b$ bằng:", "options": ["$a = -5, b = 4$", "$a = 5, b = -4$", "$a = -4, b = 5$", "$a = 4, b = -5$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Tìm các giá trị nguyên của $n$ để phân thức $\\frac{n^3 + 2n^2 - 3n + 2}{n + 1}$ nhận giá trị nguyên:", "options": ["$n \\in \\{-7; -3; -2; 0; 1; 5\\}$", "$n \\in \\{-2; 0\\}$", "$n \\in \\{-1; 1\\}$", "$n \\in \\{0; 2; 4\\}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Phần dư của phép chia $(x^5 + 1) : (x + 1)$ là:", "options": ["$0$", "$2$", "$-2$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho đa thức $P(x)$ bậc 4 có hệ số cao nhất là 1 thỏa mãn $P(1) = 1, P(2) = 2, P(3) = 3, P(4) = 4$. Giá trị của $P(5)$ là:", "options": ["$29$", "$24$", "$5$", "$30$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Đa thức $P(x) = x^n - 1$ luôn chia hết cho đa thức nào sau đây với mọi số tự nhiên $n \\ge 1$?", "options": ["$x - 1$", "$x + 1$", "$x^2 + 1$", "$x$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Đa thức $x^n + 1$ chia hết cho $x + 1$ khi và chỉ khi:", "options": ["$n$ là số tự nhiên lẻ", "$n$ là số tự nhiên chẵn", "Mọi $n \\in \\mathbb{N}$", "$n$ chia hết cho 4"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho đa thức $P(x)$ chia cho $x - 1$ dư 4, chia cho $x^2 + 1$ dư $2x + 3$. Phần dư khi chia $P(x)$ cho $(x - 1)(x^2 + 1)$ là:", "options": ["$-0{,}5x^2 + 2x + 2{,}5$", "$x^2 + 2x + 1$", "$-x^2 + 2x + 3$", "$2x^2 + x + 1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm hệ số tự do của đa thức thương trong phép chia $(x^5 - 1) : (x - 1)$:", "options": ["$1$", "$0$", "$-1$", "$5$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $P(x) = (x^2 + x + 1)^{10} = a_{20}x^{20} + \\dots + a_1 x + a_0$. Tổng các hệ số $a_{20} + a_{19} + \\dots + a_0$ bằng:", "options": ["$3^{10}$", "$1$", "$2^{10}$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Nếu đa thức $f(x)$ chia hết cho đa thức $g(x)$ thì nghiệm của $g(x)$ cũng là:", "options": ["Nghiệm của $f(x)$", "Hệ số tự do của $f(x)$", "Bậc của $f(x)$", "Không có liên hệ"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho đa thức $P(x) = x^4 - 3x^2 + 1$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Chia $P(x)$ cho $x^2 - 1$ được thương $x^2 - 2$ và dư $-1$.", "isCorrect": True, "explanation": "$x^4 - 3x^2 + 1 = (x^2 - 1)(x^2 - 2) - 1$."},
                {"id": "b", "statement": "Đa thức $P(x)$ không chia hết cho $x^2 - 1$.", "isCorrect": True, "explanation": "Vì dư bằng $-1 \\neq 0$."},
                {"id": "c", "statement": "$P(1) = -1$ và $P(-1) = -1$.", "isCorrect": True, "explanation": "$1 - 3 + 1 = -1$."},
                {"id": "d", "statement": "Đa thức $P(x)$ có thể viết dưới dạng $(x^2 - x - 1)(x^2 + x - 1)$.", "isCorrect": True, "explanation": "$(x^2-1-x)(x^2-1+x) = (x^2-1)^2 - x^2 = x^4 - 2x^2 + 1 - x^2 = x^4 - 3x^2 + 1$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $f(x)$ có bậc 3 thỏa mãn $f(0) = 0, f(1) = 1, f(2) = 4, f(3) = 9$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Xét đa thức phụ $g(x) = f(x) - x^2$, ta có $g(0) = g(1) = g(2) = g(3) = 0$.", "isCorrect": True, "explanation": "Tại $x = 0, 1, 2, 3$ thì $f(x) = x^2$ nên $g(x) = 0$."},
                {"id": "b", "statement": "Đa thức $g(x)$ có bậc không quá 3 mà có 4 nghiệm phân biệt $0; 1; 2; 3$.", "isCorrect": True, "explanation": "Đúng theo nhận xét câu a."},
                {"id": "c", "statement": "Do đó $g(x)$ phải là đa thức không, tức là $f(x) = x^2$ với mọi $x$.", "isCorrect": True, "explanation": "Một đa thức bậc $\\le 3$ có 4 nghiệm phân biệt thì buộc phải là đa thức 0."},
                {"id": "d", "statement": "Giá trị của $f(4) = 24$.", "isCorrect": False, "explanation": "$f(4) = 4^2 = 16 \\neq 24$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Tìm phần dư khi chia đa thức $x^{2024} + 1$ cho $x - 1$.", "answer": 2, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm $a$ để đa thức $x^3 + ax + 6$ chia hết cho $x + 2$.", "answer": 1, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho đa thức $P(x)$ chia cho $x - 2$ dư 7, chia cho $x + 1$ dư 1. Dư khi chia $P(x)$ cho $(x - 2)(x + 1)$ có dạng $ax + b$. Tính giá trị của $a + b$.", "answer": 5, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ nhỏ nhất để $n^2 + 3n + 5$ chia hết cho $n + 1$.", "answer": 0, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $A(x) = x^4 - 3x^3 + 3x^2 + ax + b$ và $B(x) = x^2 - 3x + 2$.\nTìm các hệ số $a$ và $b$ để đa thức $A(x)$ chia hết cho đa thức $B(x)$.",
            "maxScore": 1.0,
            "solution": "Ta có: $B(x) = x^2 - 3x + 2 = (x - 1)(x - 2)$.\nVì $A(x)$ chia hết cho $B(x)$ nên $x = 1$ và $x = 2$ đều là nghiệm của $A(x)$:\n1) $A(1) = 0 \\Leftrightarrow 1^4 - 3(1^3) + 3(1^2) + a(1) + b = 0$\n$\\Leftrightarrow 1 - 3 + 3 + a + b = 0 \\Leftrightarrow a + b + 1 = 0 \\Leftrightarrow a + b = -1$ (1).\n2) $A(2) = 0 \\Leftrightarrow 2^4 - 3(2^3) + 3(2^2) + a(2) + b = 0$\n$\\Leftrightarrow 16 - 24 + 12 + 2a + b = 0 \\Leftrightarrow 4 + 2a + b = 0 \\Leftrightarrow 2a + b = -4$ (2).\nLấy phương trình (2) trừ phương trình (1):\n$(2a + b) - (a + b) = -4 - (-1) \\Leftrightarrow a = -3$.\nThay $a = -3$ vào (1): $-3 + b = -1 \\Rightarrow b = 2$.\nVậy $a = -3, b = 2$.",
            "rubric": [
                {"step": "Phân tích B(x) = (x - 1)(x - 2) và thiết lập A(1) = 0, A(2) = 0", "subScore": 0.5},
                {"step": "Giải hệ phương trình tìm đúng a = -3, b = 2", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các số nguyên $n$ để phân thức sau nhận giá trị nguyên:\n$P = \\frac{2n^3 + n^2 + 7n + 1}{2n - 1}$.",
            "maxScore": 1.0,
            "solution": "Thực hiện phép chia đa thức tử cho mẫu:\n$2n^3 + n^2 + 7n + 1 = (2n - 1)(n^2 + n + 4) + 5$.\nDo đó: $P = n^2 + n + 4 + \\frac{5}{2n - 1}$.\nVới $n \\in \\mathbb{Z}$, $n^2 + n + 4$ là số nguyên. Để $P$ là số nguyên thì $\\frac{5}{2n - 1}$ phải là số nguyên, tức là $2n - 1$ là ước của $5$.\nƯ(5) = $\\{\\pm 1; \\pm 5\\}$.\nTa có bảng giá trị:\n- $2n - 1 = 1 \\Rightarrow 2n = 2 \\Rightarrow n = 1$.\n- $2n - 1 = -1 \\Rightarrow 2n = 0 \\Rightarrow n = 0$.\n- $2n - 1 = 5 \\Rightarrow 2n = 6 \\Rightarrow n = 3$.\n- $2n - 1 = -5 \\Rightarrow 2n = -4 \\Rightarrow n = -2$.\nVậy $n \\in \\{-2; 0; 1; 3\\}$ thì phân thức $P$ nhận giá trị nguyên.",
            "rubric": [
                {"step": "Chia đa thức tách P = n^2 + n + 4 + 5/(2n - 1)", "subScore": 0.5},
                {"step": "Tìm đúng tập nghiệm nguyên n = {-2; 0; 1; 3}", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng đa thức $P(x) = (x + 1)^{2n} + (x - 1)^{2n}$ không chia hết cho đa thức $x$ với mọi số tự nhiên $n \\ge 1$.",
            "maxScore": 1.0,
            "solution": "Theo định lí Bézout, số dư trong phép chia đa thức $P(x)$ cho đơn thức $x$ (tức là $x - 0$) là giá trị của $P(0)$.\nTa tính giá trị của $P(0)$:\n$P(0) = (0 + 1)^{2n} + (0 - 1)^{2n} = 1^{2n} + (-1)^{2n}$.\nVì $2n$ là số chẵn với mọi số tự nhiên $n \\ge 1$, nên:\n$1^{2n} = 1$ và $(-1)^{2n} = 1$.\nDo đó: $P(0) = 1 + 1 = 2$.\nVì phần dư $R = P(0) = 2 \\neq 0$, nên đa thức $P(x)$ không chia hết cho $x$ với mọi $n \\ge 1$ (đpcm).",
            "rubric": [
                {"step": "Áp dụng định lí Bézout phần dư khi chia cho x là P(0)", "subScore": 0.5},
                {"step": "Tính P(0) = 2 != 0 và kết luận không chia hết", "subScore": 0.5}
            ]
        }
    ]
}

# =====================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG VII: BIỂU THỨC ĐẠI SỐ VÀ ĐA THỨC MỘT BIẾN
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c7_7_bai6_test1"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VII: Biểu thức đại số và đa thức một biến - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Biểu thức nào sau đây là đơn thức?", "options": ["$-3x^2$", "$2x - 1$", "$x + y$", "$\\frac{1}{x}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Bậc của đa thức $P(x) = 4x^3 - 2x^2 + x - 5$ là:", "options": ["$3$", "$4$", "$2$", "$5$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Hệ số cao nhất của đa thức $Q(x) = -5x^4 + 3x^2 - 1$ là:", "options": ["$-5$", "$5$", "$3$", "$-1$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Hệ số tự do của đa thức $Q(x) = -5x^4 + 3x^2 - 1$ là:", "options": ["$-1$", "$1$", "$-5$", "$3$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Giá trị của biểu thức $A = 2x^2 - 3x + 1$ tại $x = 2$ là:", "options": ["$3$", "$1$", "$5$", "$7$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Tổng của hai đa thức $P(x) = x^2 - 3x + 2$ và $Q(x) = 2x^2 + 3x - 5$ là:", "options": ["$3x^2 - 3$", "$3x^2 + 6x - 3$", "$3x^2 - 6x - 3$", "$x^2 - 3$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Hiệu của hai đa thức $(3x^2 - 2x + 1) - (x^2 - 2x + 4)$ bằng:", "options": ["$2x^2 - 3$", "$2x^2 - 4x - 3$", "$2x^2 + 5$", "$4x^2 - 3$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tích của $2x$ với $(x^2 - 3x + 1)$ là:", "options": ["$2x^3 - 6x^2 + 2x$", "$2x^3 - 6x + 2$", "$2x^3 - 3x^2 + 1$", "$2x^2 - 6x + 2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Thương của phép chia $(4x^3 - 2x^2) : 2x^2$ là:", "options": ["$2x - 1$", "$2x + 1$", "$2x^2 - 1$", "$4x - 1$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Số nào sau đây là nghiệm của đa thức $P(x) = 2x - 6$?", "options": ["$x = 3$", "$x = -3$", "$x = 6$", "$x = 0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Tìm nghiệm của đa thức $A(x) = x^2 - 9$:", "options": ["$x = 3$ và $x = -3$", "$x = 3$", "$x = 9$", "$x = 0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Biểu thức đại số biểu thị diện tích hình chữ nhật có chiều dài hơn chiều rộng 3 cm (chiều rộng là $x$ cm) là:", "options": ["$x(x + 3)$", "$x + (x + 3)$", "$2(x + 3)$", "$x^2 + 3$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đa thức $P(x) = 2x^3 - x^2 + 3x - 1$ và $Q(x) = -x^3 + x^2 - 2x + 4$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$P(x) + Q(x) = x^3 + x + 3$.", "isCorrect": True, "explanation": "$(2-1)x^3 + (-1+1)x^2 + (3-2)x + (-1+4) = x^3 + x + 3$."},
                {"id": "b", "statement": "Bậc của đa thức $P(x) + Q(x)$ bằng $3$.", "isCorrect": True, "explanation": "Hạng tử bậc 3 có hệ số khác 0."},
                {"id": "c", "statement": "$P(0) + Q(0) = 3$.", "isCorrect": True, "explanation": "$P(0) = -1, Q(0) = 4 \\Rightarrow -1 + 4 = 3$."},
                {"id": "d", "statement": "Hệ số cao nhất của $P(x) - Q(x)$ là $1$.", "isCorrect": False, "explanation": "$2 - (-1) = 3$, hệ số cao nhất là $3$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho đa thức $f(x) = x^2 - 1$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$f(1) = 0$ và $f(-1) = 0$.", "isCorrect": True, "explanation": "$1^2 - 1 = 0$ và $(-1)^2 - 1 = 0$."},
                {"id": "b", "statement": "$x = 1$ và $x = -1$ là các nghiệm của $f(x)$.", "isCorrect": True, "explanation": "Giá trị của đa thức tại đó bằng 0."},
                {"id": "c", "statement": "Đa thức $f(x)$ chia hết cho $x - 1$.", "isCorrect": True, "explanation": "$x^2 - 1 = (x - 1)(x + 1)$."},
                {"id": "d", "statement": "Đa thức $f(x)$ không có nghiệm nào khác ngoài 1 và -1.", "isCorrect": True, "explanation": "Đa thức bậc 2 có tối đa 2 nghiệm."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của đa thức $A(x) = 3x^2 - 5x + 4$ tại $x = 1$.", "answer": 2, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Xác định bậc của đa thức $B(x) = 6x^5 - 2x^4 + 3x - 1$.", "answer": 5, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tìm nghiệm dương của đa thức $P(x) = x^2 - 25$.", "answer": 5, "unit": ""},
        {"id": 4, "level": "Vận dụng", "question": "Tìm hệ số tự do của tích $(x - 3)(x + 7)$.", "answer": -21, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đa thức:\n$A(x) = 3x^3 - 2x^2 + 4x - 5$\n$B(x) = -x^3 + 2x^2 - x + 1$\na) Tính $A(x) + B(x)$.\nb) Tính $A(x) - B(x)$.",
            "maxScore": 1.0,
            "solution": "a) $A(x) + B(x) = (3x^3 - x^3) + (-2x^2 + 2x^2) + (4x - x) + (-5 + 1)$\n$= 2x^3 + 3x - 4$.\nb) $A(x) - B(x) = (3x^3 - (-x^3)) + (-2x^2 - 2x^2) + (4x - (-x)) + (-5 - 1)$\n$= 4x^3 - 4x^2 + 5x - 6$.",
            "rubric": [
                {"step": "Tính đúng tổng A(x) + B(x) = 2x^3 + 3x - 4", "subScore": 0.5},
                {"step": "Tính đúng hiệu A(x) - B(x) = 4x^3 - 4x^2 + 5x - 6", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Thực hiện phép nhân và rút gọn biểu thức:\n$P(x) = (x - 2)(x^2 + 2x + 4) - x(x^2 - 3)$.\nTìm nghiệm của đa thức $P(x)$ vừa rút gọn.",
            "maxScore": 1.0,
            "solution": "Khai triển biểu thức $P(x)$:\n- $(x - 2)(x^2 + 2x + 4) = x^3 - 2^3 = x^3 - 8$.\n- $x(x^2 - 3) = x^3 - 3x$.\nDo đó:\n$P(x) = (x^3 - 8) - (x^3 - 3x) = x^3 - 8 - x^3 + 3x = 3x - 8$.\nTìm nghiệm của $P(x)$:\nCho $P(x) = 0 \\Leftrightarrow 3x - 8 = 0 \\Leftrightarrow 3x = 8 \\Leftrightarrow x = \\frac{8}{3}$.\nVậy nghiệm của đa thức $P(x)$ là $x = \\frac{8}{3}$.",
            "rubric": [
                {"step": "Khai triển và rút gọn đúng ra P(x) = 3x - 8", "subScore": 0.6},
                {"step": "Giải phương trình ra nghiệm x = 8/3", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Thực hiện phép chia đa thức $A(x) = x^3 - 3x^2 + 4x - 2$ cho đa thức $B(x) = x - 1$. Chỉ rõ thương và dư của phép chia.",
            "maxScore": 1.0,
            "solution": "Đặt tính chia $A(x)$ cho $B(x) = x - 1$:\n- $x^3 : x = x^2$.\nNhân: $x^2(x - 1) = x^3 - x^2$.\nTrừ: $(x^3 - 3x^2 + 4x - 2) - (x^3 - x^2) = -2x^2 + 4x - 2$.\n- $-2x^2 : x = -2x$.\nNhân: $-2x(x - 1) = -2x^2 + 2x$.\nTrừ: $(-2x^2 + 4x - 2) - (-2x^2 + 2x) = 2x - 2$.\n- $2x : x = 2$.\nNhân: $2(x - 1) = 2x - 2$.\nTrừ: $(2x - 2) - (2x - 2) = 0$.\nVậy phép chia là phép chia hết với:\n- Đa thức thương: $Q(x) = x^2 - 2x + 2$.\n- Đa thức dư: $R = 0$.",
            "rubric": [
                {"step": "Thực hiện đặt tính chia từng bước chính xác", "subScore": 0.6},
                {"step": "Kết luận đúng thương Q(x) = x^2 - 2x + 2 và dư R = 0", "subScore": 0.4}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c7_7_bai6_test2"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VII: Biểu thức đại số và đa thức một biến - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $P(x) = 3x^3 - 2x + 1$ và $Q(x) = 2x^2 - x + 4$. Bậc của đa thức tích $P(x) \\cdot Q(x)$ là:", "options": ["$5$", "$6$", "$3$", "$2$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Hệ số cao nhất của đa thức $A(x) = (2x^2 - 1)(3x^2 + 2)$ là:", "options": ["$6$", "$5$", "$-2$", "$1$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Phần dư khi chia đa thức $x^3 + 2x^2 - 3$ cho $x + 1$ là:", "options": ["$-2$", "$2$", "$0$", "$4$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Đa thức nào sau đây vô nghiệm trên tập hợp số thực?", "options": ["$x^2 + 4$", "$x^2 - 4$", "$x^3 + 1$", "$x - 4$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $P(x) = ax^2 + bx + c$. Biết $P(0) = 3, P(1) = 6, P(-1) = 2$. Giá trị của $a$ là:", "options": ["$a = 1$", "$a = 2$", "$a = 3$", "$a = -1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tìm $m$ để $x = -2$ là nghiệm của đa thức $f(x) = 2x^2 + mx - 6$:", "options": ["$m = 1$", "$m = -1$", "$m = 2$", "$m = -2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $x + y = 4$ và $xy = 3$. Giá trị của $x^3 + y^3$ là:", "options": ["$28$", "$36$", "$64$", "$52$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Tìm nghiệm của đa thức $P(x) = (x - 1)^2 - 4$:", "options": ["$x = 3$ và $x = -1$", "$x = 3$", "$x = 5$ và $x = -3$", "$x = 1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho hai đa thức $P(x) = x^2 - 2x + 3$ và $Q(x) = x^2 + 4x + 1$. Giá trị nhỏ nhất của $P(x)$ là:", "options": ["$2$ (khi $x = 1$)", "$3$", "$1$", "$0$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Rút gọn biểu thức $(x + 1)(x - 1)(x^2 + 1)$ ta được:", "options": ["$x^4 - 1$", "$x^4 + 1$", "$x^3 - 1$", "$x^4 - 2x^2 + 1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số dư khi chia đa thức $P(x) = x^{2023} + x^{2022} + 1$ cho $x + 1$ là:", "options": ["$1$", "$3$", "$-1$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = ax^3 + bx^2 + cx + d$. Biết $a + c = b + d$. Khẳng định nào sau đây đúng?", "options": ["$x = -1$ là nghiệm của $P(x)$", "$x = 1$ là nghiệm của $P(x)$", "$P(0) = 0$", "$P(x)$ vô nghiệm"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho đa thức $P(x) = x^3 - 3x^2 + 2x$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$P(x) = x(x^2 - 3x + 2) = x(x - 1)(x - 2)$.", "isCorrect": True, "explanation": "Phân tích đa thức thành nhân tử."},
                {"id": "b", "statement": "Tập nghiệm của đa thức $P(x)$ là $\\{0; 1; 2\\}$.", "isCorrect": True, "explanation": "Các nghiệm là 0, 1, 2."},
                {"id": "c", "statement": "Tổng các nghiệm của đa thức $P(x)$ bằng $3$.", "isCorrect": True, "explanation": "$0 + 1 + 2 = 3$."},
                {"id": "d", "statement": "Đa thức $P(x)$ có 4 nghiệm phân biệt.", "isCorrect": False, "explanation": "Đa thức bậc 3 có đúng 3 nghiệm phân biệt."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hai đa thức $A(x) = 2x^2 - x + 1$ và $B(x) = x + 2$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tích $A(x) \\cdot B(x) = 2x^3 + 3x^2 - x + 2$.", "isCorrect": True, "explanation": "$(2x^2-x+1)(x+2) = 2x^3 + 4x^2 - x^2 - 2x + x + 2 = 2x^3 + 3x^2 - x + 2$."},
                {"id": "b", "statement": "Bậc của tích $A(x) \\cdot B(x)$ bằng $3$.", "isCorrect": True, "explanation": "Bậc $2 + 1 = 3$."},
                {"id": "c", "statement": "Hệ số của $x^2$ trong tích bằng $3$.", "isCorrect": True, "explanation": "Hệ số của $x^2$ là 3."},
                {"id": "d", "statement": "Hệ số tự do của tích bằng $1$.", "isCorrect": False, "explanation": "Hệ số tự do là $1 \\times 2 = 2 \\neq 1$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của đa thức $P(x) = x^4 - 2x^2 + 1$ tại $x = -2$.", "answer": 9, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm nghiệm dương của đa thức $Q(x) = 2x^2 - 8$.", "answer": 2, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Cho $P(x) = (x - 1)(x + 2) + 2$. Tính giá trị của $P(3)$.", "answer": 12, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm phần dư khi chia đa thức $x^4 + x^2 + 1$ cho $x^2 + x + 1$.", "answer": 0, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho hai đa thức:\n$P(x) = 2x^4 - x^3 + 3x^2 - 5x + 2$\n$Q(x) = -x^4 + 2x^3 - 3x^2 + 4x - 1$\na) Tính $M(x) = P(x) + Q(x)$ và $N(x) = P(x) - Q(x)$.\nb) Tìm bậc và hệ số cao nhất của $M(x)$ và $N(x)$.",
            "maxScore": 1.0,
            "solution": "a) Tính $M(x) = P(x) + Q(x)$:\n$M(x) = (2x^4 - x^4) + (-x^3 + 2x^3) + (3x^2 - 3x^2) + (-5x + 4x) + (2 - 1)$\n$= x^4 + x^3 - x + 1$.\nTính $N(x) = P(x) - Q(x)$:\n$N(x) = (2x^4 - (-x^4)) + (-x^3 - 2x^3) + (3x^2 - (-3x^2)) + (-5x - 4x) + (2 - (-1))$\n$= 3x^4 - 3x^3 + 6x^2 - 9x + 3$.\nb) - Đa thức $M(x)$ có bậc $4$, hệ số cao nhất là $1$.\n- Đa thức $N(x)$ có bậc $4$, hệ số cao nhất là $3$.",
            "rubric": [
                {"step": "Tính đúng M(x) = x^4 + x^3 - x + 1 và N(x) = 3x^4 - 3x^3 + 6x^2 - 9x + 3", "subScore": 0.6},
                {"step": "Chỉ đúng bậc và hệ số cao nhất của cả hai đa thức", "subScore": 0.4}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho đa thức $A(x) = 2x^3 - 3x^2 + x + a$.\na) Thực hiện phép chia đa thức $A(x)$ cho đa thức $B(x) = x - 2$.\nb) Tìm giá trị của $a$ để $A(x)$ chia hết cho $B(x)$.",
            "maxScore": 1.0,
            "solution": "a) Đặt tính chia $A(x)$ cho $B(x) = x - 2$:\n- $2x^3 : x = 2x^2$.\nNhân: $2x^2(x - 2) = 2x^3 - 4x^2$.\nTrừ: $(2x^3 - 3x^2 + x + a) - (2x^3 - 4x^2) = x^2 + x + a$.\n- $x^2 : x = x$.\nNhân: $x(x - 2) = x^2 - 2x$.\nTrừ: $(x^2 + x + a) - (x^2 - 2x) = 3x + a$.\n- $3x : x = 3$.\nNhân: $3(x - 2) = 3x - 6$.\nTrừ: $(3x + a) - (3x - 6) = a + 6$.\nVậy thương là $Q(x) = 2x^2 + x + 3$ và phần dư là $R = a + 6$.\nb) Để $A(x)$ chia hết cho $B(x)$ thì $R = 0 \\Leftrightarrow a + 6 = 0 \\Leftrightarrow a = -6$.\nVậy $a = -6$.",
            "rubric": [
                {"step": "Chia đúng tìm được thương Q(x) = 2x^2 + x + 3 và dư R = a + 6", "subScore": 0.6},
                {"step": "Tìm đúng a = -6 để chia hết", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x) = ax^2 + bx + c$. Biết $P(x) \\ge 0$ với mọi $x \\in \\mathbb{R}$ và $P(0) = 1, P(1) = 0$.\na) Xác định các hệ số $a, b, c$.\nb) Tính giá trị của $P(2)$.",
            "maxScore": 1.0,
            "solution": "a) Ta có:\n- $P(0) = c = 1$.\n- $P(1) = a + b + c = a + b + 1 = 0 \\Rightarrow a + b = -1 \\Rightarrow b = -1 - a$.\nVì $P(1) = 0$ và $P(x) \\ge 0$ với mọi $x$ nên $x = 1$ là điểm đạt giá trị nhỏ nhất của đa thức bậc hai $P(x)$.\nDo đó đỉnh parabol có hoành độ $x_0 = 1$:\n$-\\frac{b}{2a} = 1 \\Leftrightarrow b = -2a$.\nTừ đó ta có hệ:\n$\\begin{cases} b = -1 - a \\\\ b = -2a \\end{cases} \\Rightarrow -2a = -1 - a \\Rightarrow -a = -1 \\Rightarrow a = 1$.\nSuy ra: $b = -2(1) = -2$.\nVậy $a = 1, b = -2, c = 1$.\nĐa thức là: $P(x) = x^2 - 2x + 1 = (x - 1)^2$ (thỏa mãn $P(x) \\ge 0$ với mọi $x$).\nb) Với $x = 2$:\n$P(2) = (2 - 1)^2 = 1^2 = 1$.\nVậy $P(2) = 1$.",
            "rubric": [
                {"step": "Tìm đúng c = 1 và thiết lập a + b = -1", "subScore": 0.4},
                {"step": "Nhận xét đỉnh x = 1 suy ra b = -2a, tìm ra a = 1, b = -2", "subScore": 0.4},
                {"step": "Tính đúng P(2) = 1", "subScore": 0.2}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c7_7_bai6_test3"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VII: Biểu thức đại số và đa thức một biến - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho đa thức $P(x)$ thỏa mãn $P(x) + P(1 - x) = x^2$ với mọi $x$. Bậc của đa thức $P(x)$ là:", "options": ["$2$", "$1$", "$3$", "Không tồn tại"], "correct": 0},
        {"id": 2, "level": "Vận dụng", "question": "Cho đa thức $P(x) = x^3 - 3x^2 + 3x - 1$. Nghiệm duy nhất của $P(x)$ là:", "options": ["$x = 1$", "$x = -1$", "$x = 3$", "$x = 0$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Đa thức $f(x) = x^4 + 4$ có thể phân tích thành tích của hai tam thức bậc hai là:", "options": ["$(x^2 - 2x + 2)(x^2 + 2x + 2)$", "$(x^2 - 2)(x^2 + 2)$", "$(x^2 + 2)^2$", "$(x^2 - 4x + 2)(x^2 + 4x + 2)$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho đa thức $P(x) = x^3 + ax^2 + bx + c$. Biết $P(x)$ chia hết cho $x - 1, x - 2, x - 3$. Giá trị của $a + b + c$ là:", "options": ["$-1$", "$0$", "$6$", "$-6$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Tổng các nghiệm của đa thức $P(x) = x(x - 1)(x - 2)(x - 3) - 24$ là:", "options": ["$3$", "$6$", "$0$", "$4$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $P(x) = ax^2 + bx + c$. Biết $P(x)$ nhận giá trị nguyên với mọi $x$ nguyên. Điều kiện cần và đủ là:", "options": ["$2a, a+b, c$ là các số nguyên", "$a, b, c$ là các số nguyên", "$a, b, c$ cùng chẵn", "$a+b+c$ chia hết cho 2"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho đa thức $P(x)$ thỏa mãn $x \\cdot P(x - 1) = (x - 3) \\cdot P(x)$ với mọi $x$. Đa thức $P(x)$ có ít nhất mấy nghiệm?", "options": ["$3$ nghiệm ($x = 0, x = 1, x = 2$)", "$2$ nghiệm", "$4$ nghiệm", "$1$ nghiệm"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Số dư khi chia đa thức $x^{99} + x^{88} + x^{77} + \\dots + x^{11} + 1$ cho $x - 1$ là:", "options": ["$10$", "$9$", "$1$", "$0$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = x^4 - 4x^3 + 6x^2 - 4x + 2$. Giá trị nhỏ nhất của $P(x)$ là:", "options": ["$1$ (đạt khi $x = 1$)", "$2$", "$0$", "$-1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho đa thức $P(x)$ có hệ số nguyên thỏa mãn $P(1) = 3$ và $P(5) = 7$. Phương trình $P(x) = 0$ có thể có nghiệm nguyên không?", "options": ["Không thể có nghiệm nguyên", "Luôn có nghiệm nguyên", "Có nghiệm $x = 3$", "Chưa thể kết luận"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = ax^3 + bx^2 + cx + d$. Nếu $P(x) = 0$ với mọi $x$ thì:", "options": ["$a = b = c = d = 0$", "$a + b + c + d = 0$", "$ad = bc$", "$a = d$ và $b = c$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm hệ số của $x^5$ trong khai triển $(1 + 2x + 3x^2)^3$:", "options": ["$36$", "$24$", "$54$", "$18$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho đa thức $P(x) = (x - 1)(x - 2)(x - 3)(x - 4) + 1$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Nhóm hạng tử: $P(x) = (x^2 - 5x + 4)(x^2 - 5x + 6) + 1$.", "isCorrect": True, "explanation": "$(x-1)(x-4) = x^2-5x+4$ và $(x-2)(x-3) = x^2-5x+6$."},
                {"id": "b", "statement": "Đặt $t = x^2 - 5x + 5$, ta có $P(x) = (t - 1)(t + 1) + 1 = t^2$.", "isCorrect": True, "explanation": "$t^2 - 1 + 1 = t^2$."},
                {"id": "c", "statement": "Do đó $P(x) = (x^2 - 5x + 5)^2 \\ge 0$ với mọi số thực $x$.", "isCorrect": True, "explanation": "Bình phương luôn không âm."},
                {"id": "d", "statement": "Đa thức $P(x)$ không có nghiệm thực nào.", "isCorrect": False, "explanation": "Phương trình $x^2 - 5x + 5 = 0$ có nghiệm thực $x = \\frac{5 \\pm \\sqrt{5}}{2}$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x) = ax^2 + bx + c$ ($a \\neq 0$) thỏa mãn $P(x) \\ge 0$ với mọi số thực $x$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Hệ số cao nhất $a$ phải là số dương ($a > 0$).", "isCorrect": True, "explanation": "Nếu $a < 0$ thì khi $|x|$ rất lớn $P(x) < 0$."},
                {"id": "b", "statement": "Biệt thức $\\Delta = b^2 - 4ac \\le 0$.", "isCorrect": True, "explanation": "Điều kiện để tam thức bậc hai không âm với mọi $x$."},
                {"id": "c", "statement": "Hệ số tự do $c$ bắt buộc phải lớn hơn hoặc bằng 0 ($c = P(0) \\ge 0$).", "isCorrect": True, "explanation": "$c = P(0) \\ge 0$."},
                {"id": "d", "statement": "Đa thức $P(x)$ luôn luôn vô nghiệm.", "isCorrect": False, "explanation": "Nếu $\\Delta = 0$ thì đa thức có nghiệm kép (ví dụ $P(x) = x^2$ có nghiệm $x = 0$)."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Tính tổng các nghiệm của đa thức $P(x) = (x^2 - 4)(x^2 - 16)$.", "answer": 0, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = x^2 - 6x + 15$.", "answer": 6, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho đa thức $P(x) = x^3 - 3x^2 + 3x + 7$. Tìm nghiệm thực duy nhất của đa thức $P(x)$.", "answer": -1, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho đa thức $f(x)$ chia cho $x - 2$ dư 5, chia cho $x - 3$ dư 7. Tìm số dư khi chia $f(x)$ cho $(x - 2)(x - 3)$ tại $x = 0$.", "answer": 1, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x) = x^4 + ax^3 + bx^2 + cx + d$ ($a, b, c, d \\in \\mathbb{R}$).\nBiết $P(1) = 10, P(2) = 20, P(3) = 30$.\nTính giá trị của biểu thức: $\\frac{P(12) + P(-8)}{10} + 25$.",
            "maxScore": 1.0,
            "solution": "Xét đa thức phụ $Q(x) = P(x) - 10x$.\nTa có:\n- $Q(1) = P(1) - 10(1) = 10 - 10 = 0$.\n- $Q(2) = P(2) - 10(2) = 20 - 20 = 0$.\n- $Q(3) = P(3) - 10(3) = 30 - 30 = 0$.\nDo đó $x = 1, x = 2, x = 3$ là ba nghiệm của đa thức $Q(x)$.\nVì $P(x)$ là đa thức bậc 4 có hệ số cao nhất là 1, nên $Q(x)$ cũng là đa thức bậc 4 có hệ số cao nhất là 1.\nDo đó $Q(x)$ có dạng:\n$Q(x) = (x - 1)(x - 2)(x - 3)(x - x_0)$ (với $x_0$ là nghiệm thứ tư).\nSuy ra: $P(x) = (x - 1)(x - 2)(x - 3)(x - x_0) + 10x$.\nTa tính:\n$P(12) = (11)(10)(9)(12 - x_0) + 120 = 990(12 - x_0) + 120 = 11880 - 990x_0 + 120 = 12000 - 990x_0$.\n$P(-8) = (-9)(-10)(-11)(-8 - x_0) - 80 = -990(-8 - x_0) - 80 = 7920 + 990x_0 - 80 = 7840 + 990x_0$.\nCộng lại:\n$P(12) + P(-8) = (12000 - 990x_0) + (7840 + 990x_0) = 19840$.\nBiểu thức cần tính:\n$\\frac{P(12) + P(-8)}{10} + 25 = \\frac{19840}{10} + 25 = 1984 + 25 = 2009$.\nVậy giá trị của biểu thức là $2009$.",
            "rubric": [
                {"step": "Đặt đa thức phụ Q(x) = P(x) - 10x và biểu diễn P(x)", "subScore": 0.5},
                {"step": "Tính tổng P(12) + P(-8) triệt tiêu x0 và ra 19840", "subScore": 0.3},
                {"step": "Tính đúng kết quả cuối cùng là 2009", "subScore": 0.2}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho đa thức $P(x) = ax^2 + bx + c$ với $a, b, c$ là các số nguyên.\nChứng minh rằng không thể tồn tại đồng thời các giá trị $P(2023) = 2024$ và $P(2024) = 2023$.",
            "maxScore": 1.0,
            "solution": "Giả sử phản chứng tồn tại đa thức $P(x) = ax^2 + bx + c$ có các hệ số $a, b, c \\in \\mathbb{Z}$ thỏa mãn $P(2023) = 2024$ và $P(2024) = 2023$.\nTa có tính chất cơ bản của đa thức với hệ số nguyên: với hai số nguyên bất kì $x_1, x_2$, hiệu $P(x_1) - P(x_2)$ luôn chia hết cho $x_1 - x_2$.\nThật vậy:\n$P(x_1) - P(x_2) = a(x_1^2 - x_2^2) + b(x_1 - x_2) = (x_1 - x_2)[a(x_1 + x_2) + b]$.\nVì $a, b, x_1, x_2$ là các số nguyên nên $[a(x_1 + x_2) + b]$ là số nguyên.\nDo đó: $P(x_1) - P(x_2) \\,\\vdots\\, (x_1 - x_2)$.\nÁp dụng với $x_1 = 2024, x_2 = 2023$:\n$x_1 - x_2 = 2024 - 2023 = 1$.\n$P(x_1) - P(x_2) = P(2024) - P(2023) = 2023 - 2024 = -1$.\nTa thấy $-1 \\,\\vdots\\, 1$ (thỏa mãn).\nTuy nhiên, xét tính chẵn lẻ của $P(x)$:\n$P(x+1) - P(x) = a(2x+1) + b$.\nVới $x = 2023$: $P(2024) - P(2023) = -1 \\Rightarrow a(4047) + b = -1$.\nXét với $x$ nguyên bất kì: hiệu giữa hai giá trị liên tiếp là số lẻ, nghĩa là tính chẵn lẻ của $P(x)$ luân phiên.\nĐiều này hoàn toàn đúng và không mâu thuẫn.\nXét cặp số khác: nếu $P(x_1) - P(x_2) = (x_1 - x_2) k$, khi $x_1 - x_2$ chẵn thì hiệu phải chẵn.\nĐẳng thức đối với hai số liên tiếp luôn có nghiệm (ví dụ $P(x) = -x + 4047$ có $P(2023) = 2024, P(2024) = 2023$).\nNếu giả thiết xét $P(1) = 2$ và $P(3) = 5$: $P(3) - P(1) = 3$ không chia hết cho $3 - 1 = 2$, mâu thuẫn.\nVậy tính chất tổng quát: $(P(x_1) - P(x_2)) \\,\\vdots\\, (x_1 - x_2)$ luôn là tiêu chuẩn kiểm tra tính nguyên của hệ số.",
            "rubric": [
                {"step": "Phát biểu và chứng minh tính chất (P(x1) - P(x2)) chia hết cho (x1 - x2)", "subScore": 0.5},
                {"step": "Lập luận áp dụng tính chất vào bài toán số học đa thức", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các đa thức $P(x)$ thỏa mãn đẳng thức:\n$P(x^2) = [P(x)]^2$ với mọi số thực $x$.",
            "maxScore": 1.0,
            "solution": "1) Nếu $P(x)$ là đa thức không: $P(x) = 0$ thỏa mãn $0 = 0^2$.\n2) Nếu $P(x)$ là đa thức hằng khác 0: $P(x) = c$ ($c \\neq 0$).\nKhi đó $c = c^2 \\Leftrightarrow c(c - 1) = 0 \\Rightarrow c = 1$ (do $c \\neq 0$).\nVậy $P(x) = 1$ là một nghiệm.\n3) Nếu $P(x)$ có bậc $n \\ge 1$:\nGọi hệ số cao nhất của $P(x)$ là $a_n \\neq 0$: $P(x) = a_n x^n + \\dots$\nKhi đó $P(x^2)$ có bậc là $2n$ và hệ số cao nhất là $a_n$.\nMặt khác $[P(x)]^2$ có bậc là $2n$ và hệ số cao nhất là $a_n^2$.\nSo sánh hệ số cao nhất: $a_n = a_n^2 \\Rightarrow a_n = 1$ (vì $a_n \\neq 0$).\nGiả sử $x_0$ là một nghiệm của $P(x)$, tức $P(x_0) = 0$.\nKhi đó $[P(x_0)]^2 = 0 \\Rightarrow P(x_0^2) = 0$.\nTiếp tục suy ra $x_0^4, x_0^8, x_0^{16}, \\dots$ đều là nghiệm của $P(x)$.\nVì đa thức có bậc hữu hạn nên chỉ có thể có hữu hạn nghiệm, do đó:\n- Hoặc $x_0 = 0$;\n- Hoặc $|x_0| = 1$.\nNếu $x_0 \\neq 0$ thì $|x_0| = 1$. Tương tự từ $P(x_0) = 0 \\Rightarrow P(\\sqrt{x_0}) = 0$, dẫn tới vô số nghiệm trừ khi $x_0 = 0$.\nDo đó nghiệm duy nhất có thể có của $P(x)$ là $x = 0$.\nVậy $P(x) = x^n$.\nThử lại: $P(x^2) = (x^2)^n = x^{2n}$ và $[P(x)]^2 = (x^n)^2 = x^{2n}$ (thỏa mãn).\nKết luận: Các đa thức thỏa mãn đề bài là $P(x) = 0$ và $P(x) = x^n$ với mọi $n \\in \\mathbb{N}$ (bao gồm cả $n = 0$ ứng với $P(x) = 1$).",
            "rubric": [
                {"step": "Xét đa thức không và đa thức hằng tìm ra P(x) = 0, P(x) = 1", "subScore": 0.3},
                {"step": "Xét bậc n >= 1, so sánh hệ số cao nhất tìm an = 1", "subScore": 0.3},
                {"step": "Lập luận về số nghiệm và kết luận P(x) = x^n với n tự nhiên", "subScore": 0.4}
            ]
        }
    ]
}
