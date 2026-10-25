# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 9 - CHƯƠNG III: CĂN BẬC HAI VÀ CĂN BẬC BA
PHẦN 2:
- BÀI 9: BIẾN ĐỔI ĐƠN GIẢN VÀ RÚT GỌN BIỂU THỨC CHỨA CĂN THỨC BẬC HAI (c3_9_bai3)
- BÀI 10: CĂN BẬC BA VÀ CĂN THỨC BẬC BA (c3_9_bai4)
- BÀI KIỂM TRA CUỐI CHƯƠNG III: CĂN BẬC HAI VÀ CĂN BẬC BA (c3_9_bai5)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 9: BIẾN ĐỔI ĐƠN GIẢN VÀ RÚT GỌN BIỂU THỨC CHỨA CĂN THỨC BẬC HAI (c3_9_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c3_9_bai3_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Đưa thừa số ra ngoài dấu căn: với $b \\ge 0$, $\\sqrt{a^2 b}$ bằng:", "options": ["$|a|\\sqrt{b}$", "$a\\sqrt{b}$", "$-a\\sqrt{b}$", "$a^2\\sqrt{b}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Đưa thừa số vào trong dấu căn: với $a \\ge 0, b \\ge 0$, biểu thức $a\\sqrt{b}$ bằng:", "options": ["$\\sqrt{a^2 b}$", "$\\sqrt{ab}$", "$-\\sqrt{a^2 b}$", "$\\sqrt{ab^2}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Khử mẫu của biểu thức lấy căn: với $ab \\ge 0, b \\neq 0$, $\\sqrt{\\frac{a}{b}}$ bằng:", "options": ["$\\frac{\\sqrt{ab}}{|b|}$", "$\\frac{\\sqrt{a}}{b}$", "$\\frac{a}{\\sqrt{b}}$", "$\\sqrt{ab}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trục căn thức ở mẫu của $\\frac{1}{\\sqrt{3}}$ ta được:", "options": ["$\\frac{\\sqrt{3}}{3}$", "$\\frac{3}{\\sqrt{3}}$", "$\\sqrt{3}$", "$\\frac{1}{3}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\sqrt{12} + \\sqrt{27}$ được kết quả là:", "options": ["$5\\sqrt{3}$", "$3\\sqrt{5}$", "$\\sqrt{39}$", "$6\\sqrt{3}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $2\\sqrt{8} - 3\\sqrt{18} + \\sqrt{50}$:", "options": ["$0$", "$\\sqrt{2}$", "$2\\sqrt{2}$", "$-\\sqrt{2}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Trục căn thức ở mẫu của biểu thức $\\frac{2}{\\sqrt{5} - 1}$ được kết quả là:", "options": ["$\\frac{\\sqrt{5} + 1}{2}$", "$\\sqrt{5} + 1$", "$\\frac{\\sqrt{5} - 1}{2}$", "$2(\\sqrt{5} + 1)$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Với $x \\ge 0$, biểu thức $3\\sqrt{x} - \\sqrt{4x} + \\sqrt{9x}$ rút gọn thành:", "options": ["$4\\sqrt{x}$", "$2\\sqrt{x}$", "$3\\sqrt{x}$", "$5\\sqrt{x}$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Trục căn thức ở mẫu của $\\frac{1}{\\sqrt{3} + \\sqrt{2}}$ ta được:", "options": ["$\\sqrt{3} - \\sqrt{2}$", "$\\sqrt{3} + \\sqrt{2}$", "$\\frac{\\sqrt{3} - \\sqrt{2}}{5}$", "$1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Rút gọn biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 1} + \\frac{1}{\\sqrt{x} + 1}\\right) \\cdot \\frac{x - 1}{2}$ với $x \\ge 0, x \\neq 1$:", "options": ["$\\sqrt{x}$", "$x$", "$2\\sqrt{x}$", "$1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Tìm $x$ biết $\\sqrt{4x} - 2\\sqrt{x} + \\sqrt{9x} = 6$:", "options": ["$x = 4$", "$x = 2$", "$x = 16$", "$x = 9$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị của biểu thức $\\frac{1}{2 + \\sqrt{3}} + \\frac{1}{2 - \\sqrt{3}}$ là:", "options": ["$4$", "$2\\sqrt{3}$", "$2$", "$0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = 3\\sqrt{2} - \\sqrt{18} + \\sqrt{32}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $\\sqrt{18} = 3\\sqrt{2}$.", "correct": True},
                {"subId": "b", "text": "Ta có $\\sqrt{32} = 4\\sqrt{2}$.", "correct": True},
                {"subId": "c", "text": "Giá trị rút gọn của $A$ là $4\\sqrt{2}$.", "correct": True},
                {"subId": "d", "text": "Giá trị của $A$ là một số hữu tỉ.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho biểu thức $B = \\frac{x - 4}{\\sqrt{x} + 2}$ với $x \\ge 0$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phân tích $x - 4 = (\\sqrt{x} - 2)(\\sqrt{x} + 2)$.", "correct": True},
                {"subId": "b", "text": "Rút gọn được $B = \\sqrt{x} - 2$.", "correct": True},
                {"subId": "c", "text": "Khi $x = 9$ thì $B = 1$.", "correct": True},
                {"subId": "d", "text": "Giá trị của $B$ luôn luôn dương với mọi $x \\ge 0$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\sqrt{48} - 2\\sqrt{3}$. Kết quả có dạng $a\\sqrt{3}$. Tìm $a$.", "correctAnswer": "2", "explanation": "$\\sqrt{48} = 4\\sqrt{3} \\Rightarrow 4\\sqrt{3} - 2\\sqrt{3} = 2\\sqrt{3}$. Vậy $a = 2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $(\\sqrt{5} + 2)(\\sqrt{5} - 2)$.", "correctAnswer": "1", "explanation": "$(\\sqrt{5})^2 - 2^2 = 5 - 4 = 1$."},
        {"id": 3, "level": "Vận dụng", "question": "Tìm $x$ biết $\\sqrt{9x} - \\sqrt{4x} = 3$.", "correctAnswer": "9", "explanation": "$3\\sqrt{x} - 2\\sqrt{x} = 3 \\Rightarrow \\sqrt{x} = 3 \\Rightarrow x = 9$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính giá trị của biểu thức $P = \\frac{1}{3 + \\sqrt{8}} + \\frac{1}{3 - \\sqrt{8}}$.", "correctAnswer": "6", "explanation": "Trục căn thức: $(3 - \\sqrt{8}) + (3 + \\sqrt{8}) = 6$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Rút gọn các biểu thức sau:\na) $A = 2\\sqrt{12} - 3\\sqrt{27} + \\sqrt{75}$.\nb) $B = \\frac{5}{\\sqrt{5}} + \\frac{2}{\\sqrt{5} - 1}$.",
            "solution": "a) Đưa thừa số ra ngoài dấu căn:\n$A = 2 \\cdot 2\\sqrt{3} - 3 \\cdot 3\\sqrt{3} + 5\\sqrt{3}$\n$= 4\\sqrt{3} - 9\\sqrt{3} + 5\\sqrt{3} = 0$.\nb) Trục căn thức ở mẫu:\n$B = \\frac{5\\sqrt{5}}{5} + \\frac{2(\\sqrt{5} + 1)}{(\\sqrt{5} - 1)(\\sqrt{5} + 1)}$\n$= \\sqrt{5} + \\frac{2(\\sqrt{5} + 1)}{5 - 1} = \\sqrt{5} + \\frac{2(\\sqrt{5} + 1)}{4} = \\sqrt{5} + \\frac{\\sqrt{5} + 1}{2} = \\frac{3\\sqrt{5} + 1}{2}$.",
            "rubric": [
                {"step": "Tính đúng kết quả A = 0", "subScore": 0.5},
                {"step": "Trục căn thức ở mẫu và rút gọn đúng B = (3sqrt(5) + 1)/2", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} + 2} + \\frac{1}{\\sqrt{x} - 2}\\right) : \\frac{\\sqrt{x}}{x - 4}$ với $x > 0, x \\neq 4$.\na) Rút gọn biểu thức $P$.\nb) Tìm giá trị của $x$ để $P = 2$.",
            "solution": "a) Với $x > 0, x \\neq 4$:\nQuy đồng mẫu thức trong ngoặc:\n$\\frac{1}{\\sqrt{x} + 2} + \\frac{1}{\\sqrt{x} - 2} = \\frac{(\\sqrt{x} - 2) + (\\sqrt{x} + 2)}{(\\sqrt{x} + 2)(\\sqrt{x} - 2)} = \\frac{2\\sqrt{x}}{x - 4}$.\nDo đó:\n$P = \\frac{2\\sqrt{x}}{x - 4} : \\frac{\\sqrt{x}}{x - 4} = \\frac{2\\sqrt{x}}{x - 4} \\cdot \\frac{x - 4}{\\sqrt{x}} = 2$.\nb) Nhận xét: Với mọi $x > 0, x \\neq 4$, biểu thức $P$ luôn nhận giá trị bằng $2$.\nVậy phương trình $P = 2$ nghiệm đúng với mọi $x > 0, x \\neq 4$.",
            "rubric": [
                {"step": "Quy đồng và rút gọn đúng P = 2", "subScore": 0.5},
                {"step": "Lập luận đúng giá trị của x thỏa mãn là mọi x > 0, x khác 4", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho biểu thức $A = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2}$ với $x \\ge 0, x \\neq 4$. Tìm các giá trị nguyên của $x$ để biểu thức $A$ nhận giá trị nguyên.",
            "solution": "Ta có: $A = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} = \\frac{(\\sqrt{x} - 2) + 3}{\\sqrt{x} - 2} = 1 + \\frac{3}{\\sqrt{x} - 2}$.\nĐể $A$ nhận giá trị nguyên thì $\\frac{3}{\\sqrt{x} - 2}$ phải là số nguyên, tức là $\\sqrt{x} - 2$ phải là ước của $3$.\nCác ước của $3$ là $\\{\\pm 1; \\pm 3\\}$:\n- $\\sqrt{x} - 2 = 1 \\Rightarrow \\sqrt{x} = 3 \\Rightarrow x = 9$ (thỏa mãn ĐK).\n- $\\sqrt{x} - 2 = -1 \\Rightarrow \\sqrt{x} = 1 \\Rightarrow x = 1$ (thỏa mãn ĐK).\n- $\\sqrt{x} - 2 = 3 \\Rightarrow \\sqrt{x} = 5 \\Rightarrow x = 25$ (thỏa mãn ĐK).\n- $\\sqrt{x} - 2 = -3 \\Rightarrow \\sqrt{x} = -1$ (vô nghiệm vì $\\sqrt{x} \\ge 0$).\nVậy các giá trị nguyên của $x$ để $A$ nhận giá trị nguyên là $x \\in \\{1; 9; 25\\}$.",
            "rubric": [
                {"step": "Tách A = 1 + 3/(sqrt(x) - 2) và lập luận ước số", "subScore": 0.5},
                {"step": "Tìm đúng tập giá trị nguyên x thuộc {1; 9; 25} và đối chiếu ĐKXĐ", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c3_9_bai3_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Với $a < 0$, biểu thức $a\\sqrt{3}$ đưa thừa số vào trong dấu căn thành:", "options": ["$-\\sqrt{3a^2}$", "$\\sqrt{3a^2}$", "$\\sqrt{-3a^2}$", "$-3\\sqrt{a^2}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Trục căn thức ở mẫu của $\\frac{6}{\\sqrt{7} - 1}$ được kết quả là:", "options": ["$\\sqrt{7} + 1$", "$6(\\sqrt{7} + 1)$", "$\\frac{\\sqrt{7} + 1}{6}$", "$\\sqrt{7} - 1$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Rút gọn biểu thức $A = \\sqrt{20} - \\sqrt{45} + 3\\sqrt{80}$:", "options": ["$11\\sqrt{5}$", "$9\\sqrt{5}$", "$7\\sqrt{5}$", "$13\\sqrt{5}$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $(\\sqrt{12} - \\sqrt{75}) \\cdot \\sqrt{3}$:", "options": ["$-9$", "$9$", "$-3$", "$3$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Với $a > 0, b > 0$, rút gọn biểu thức $\\frac{a - b}{\\sqrt{a} - \\sqrt{b}}$ được kết quả là:", "options": ["$\\sqrt{a} + \\sqrt{b}$", "$\\sqrt{a} - \\sqrt{b}$", "$a + b$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{9x - 9} - 1 = 5$. Nghiệm của phương trình là:", "options": ["$x = 5$", "$x = 4$", "$x = 9$", "$x = 2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho biểu thức $P = \\frac{\\sqrt{x}}{\\sqrt{x} - 1} - \\frac{1}{x - \\sqrt{x}}$ với $x > 0, x \\neq 1$. Rút gọn $P$ được kết quả là:", "options": ["$\\frac{\\sqrt{x} + 1}{\\sqrt{x}}$", "$\\frac{\\sqrt{x} - 1}{\\sqrt{x}}$", "$1$", "$\\sqrt{x}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Giá trị của biểu thức $\\frac{1}{3 + 2\\sqrt{2}} + \\frac{1}{3 - 2\\sqrt{2}}$ là:", "options": ["$6$", "$4\\sqrt{2}$", "$1$", "$12$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Tìm $x$ biết $\\sqrt{4x - 20} + \\sqrt{x - 5} - \\frac{1}{3}\\sqrt{9x - 45} = 4$:", "options": ["$x = 9$", "$x = 4$", "$x = 5$", "$x = 7$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = \\frac{x - 3\\sqrt{x} + 4}{\\sqrt{x}}$ với $x > 0$:", "options": ["$1$", "$2$", "$4$", "$-1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $x = 7 - 4\\sqrt{3}$. Giá trị của biểu thức $\\sqrt{x} + \\frac{1}{\\sqrt{x}}$ là:", "options": ["$4$", "$2\\sqrt{3}$", "$2$", "$14$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $S = \\frac{1}{1 + \\sqrt{2}} + \\frac{1}{\\sqrt{2} + \\sqrt{3}} + \\dots + \\frac{1}{\\sqrt{99} + \\sqrt{100}}$ được kết quả là:", "options": ["$9$", "$10$", "$8$", "$\\sqrt{99}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 1} - \\frac{1}{\\sqrt{x}}\\right) : \\frac{\\sqrt{x} + 1}{x - 1}$ với $x > 0, x \\neq 1$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Quy đồng ngoặc thứ nhất: $\\frac{1}{\\sqrt{x}(\\sqrt{x} - 1)}$.", "correct": True},
                {"subId": "b", "text": "Phân tích $\\frac{x - 1}{\\sqrt{x} + 1} = \\sqrt{x} - 1$.", "correct": True},
                {"subId": "c", "text": "Kết quả rút gọn là $P = \\frac{1}{\\sqrt{x}}$.", "correct": True},
                {"subId": "d", "text": "Khi $x = 4$ thì giá trị của $P$ bằng $2$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\sqrt{9x - 18} - \\sqrt{x - 2} = 4$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điều kiện xác định của phương trình là $x \\ge 2$.", "correct": True},
                {"subId": "b", "text": "Đưa thừa số ra ngoài căn: $\\sqrt{9(x - 2)} = 3\\sqrt{x - 2}$.", "correct": True},
                {"subId": "c", "text": "Phương trình thu gọn thành $2\\sqrt{x - 2} = 4 \\Leftrightarrow \\sqrt{x - 2} = 2$.", "correct": True},
                {"subId": "d", "text": "Nghiệm của phương trình là $x = 4$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt{50} - \\sqrt{18}$. Kết quả có dạng $a\\sqrt{2}$. Tìm $a$.", "correctAnswer": "2", "explanation": "$5\\sqrt{2} - 3\\sqrt{2} = 2\\sqrt{2}$. Vậy $a = 2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Trục căn thức ở mẫu của $\\frac{4}{\\sqrt{5} - 1}$. Kết quả có dạng $\\sqrt{a} + b$. Tính $a + b$.", "correctAnswer": "6", "explanation": "$\\frac{4(\\sqrt{5}+1)}{4} = \\sqrt{5} + 1$. $a = 5, b = 1 \\Rightarrow a + b = 6$."},
        {"id": 3, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{4x + 20} = 6$. Tìm nghiệm $x$.", "correctAnswer": "4", "explanation": "$2\\sqrt{x + 5} = 6 \\Rightarrow \\sqrt{x + 5} = 3 \\Rightarrow x + 5 = 9 \\Rightarrow x = 4$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính giá trị của biểu thức $P = \\frac{1}{\\sqrt{2} + 1} + \\frac{1}{\\sqrt{3} + \\sqrt{2}} + \\frac{1}{\\sqrt{4} + \\sqrt{3}}$.", "correctAnswer": "1", "explanation": "$(\\sqrt{2} - 1) + (\\sqrt{3} - \\sqrt{2}) + (2 - \\sqrt{3}) = 2 - 1 = 1$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Rút gọn biểu thức sau:\n$$A = \\left(\\frac{1}{\\sqrt{a} - 3} - \\frac{1}{\\sqrt{a} + 3}\\right) \\cdot \\frac{a - 9}{6}$$ với $a \\ge 0, a \\neq 9$.",
            "solution": "Với $a \\ge 0, a \\neq 9$:\nQuy đồng mẫu thức trong ngoặc:\n$\\frac{1}{\\sqrt{a} - 3} - \\frac{1}{\\sqrt{a} + 3} = \\frac{(\\sqrt{a} + 3) - (\\sqrt{a} - 3)}{(\\sqrt{a} - 3)(\\sqrt{a} + 3)} = \\frac{6}{a - 9}$.\nNhân với phân thức thứ hai:\n$A = \\frac{6}{a - 9} \\cdot \\frac{a - 9}{6} = 1$.\nVậy $A = 1$.",
            "rubric": [
                {"step": "Quy đồng biểu thức trong ngoặc ra 6/(a - 9)", "subScore": 0.5},
                {"step": "Nhân và rút gọn ra kết quả A = 1", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho biểu thức $P = \\left(\\frac{\\sqrt{x}}{\\sqrt{x} + 2} + \\frac{2}{\\sqrt{x} - 2}\\right) : \\frac{x + 4}{x - 4}$ với $x \\ge 0, x \\neq 4$.\na) Rút gọn biểu thức $P$.\nb) Tìm giá trị của $x$ để $P < 1$.",
            "solution": "a) Với $x \\ge 0, x \\neq 4$:\nQuy đồng mẫu thức trong ngoặc:\n$\\frac{\\sqrt{x}}{\\sqrt{x} + 2} + \\frac{2}{\\sqrt{x} - 2} = \\frac{\\sqrt{x}(\\sqrt{x} - 2) + 2(\\sqrt{x} + 2)}{(\\sqrt{x} + 2)(\\sqrt{x} - 2)} = \\frac{x - 2\\sqrt{x} + 2\\sqrt{x} + 4}{x - 4} = \\frac{x + 4}{x - 4}$.\nDo đó:\n$P = \\frac{x + 4}{x - 4} : \\frac{x + 4}{x - 4} = 1$.\nb) Nhận xét: Với mọi $x \\ge 0, x \\neq 4$, ta luôn có $P = 1$.\nDo đó bất phương trình $P < 1 \\Leftrightarrow 1 < 1$ (vô lí).\nVậy không có giá trị nào của $x$ để $P < 1$.",
            "rubric": [
                {"step": "Rút gọn đúng P = 1", "subScore": 0.5},
                {"step": "Lập luận P < 1 vô nghiệm và kết luận chuẩn xác", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho biểu thức $M = \\frac{\\sqrt{x} + 2}{\\sqrt{x} + 1}$ với $x \\ge 0$. Tìm giá trị lớn nhất của biểu thức $M$.",
            "solution": "Ta có: $M = \\frac{\\sqrt{x} + 1 + 1}{\\sqrt{x} + 1} = 1 + \\frac{1}{\\sqrt{x} + 1}$.\nVì $x \\ge 0$ nên $\\sqrt{x} \\ge 0 \\Rightarrow \\sqrt{x} + 1 \\ge 1$.\nDo đó: $\\frac{1}{\\sqrt{x} + 1} \\le \\frac{1}{1} = 1$.\nSuy ra: $M = 1 + \\frac{1}{\\sqrt{x} + 1} \\le 1 + 1 = 2$.\nDấu \"=\" xảy ra khi và chỉ khi $\\sqrt{x} = 0 \\Leftrightarrow x = 0$ (thỏa mãn ĐK $x \\ge 0$).\nVậy giá trị lớn nhất của $M$ là $2$ khi $x = 0$.",
            "rubric": [
                {"step": "Tách M = 1 + 1/(sqrt(x) + 1)", "subScore": 0.5},
                {"step": "Đánh giá mẫu số >= 1 để suy ra GTLN = 2 tại x = 0", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c3_9_bai3_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Biểu thức liên hợp của $\\sqrt{a} - \\sqrt{b}$ là:", "options": ["$\\sqrt{a} + \\sqrt{b}$", "$\\sqrt{a} - \\sqrt{b}$", "$a + b$", "$a - b$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\frac{2}{\\sqrt{3} - 1} - \\frac{2}{\\sqrt{3} + 1}$:", "options": ["$2$", "$\\sqrt{3}$", "$2\\sqrt{3}$", "$4$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $x > 0$. Rút gọn biểu thức $\\frac{x\\sqrt{y} + y\\sqrt{x}}{\\sqrt{xy}}$ với $y > 0$ được kết quả là:", "options": ["$\\sqrt{x} + \\sqrt{y}$", "$x + y$", "$\\sqrt{x} - \\sqrt{y}$", "$\\sqrt{xy}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Giá trị của biểu thức $A = \\sqrt{4 + 2\\sqrt{3}} - \\frac{1}{\\sqrt{3} - 1}$ là:", "options": ["$\\frac{\\sqrt{3} + 1}{2}$", "$1$", "$0$", "$\\sqrt{3}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $P = \\frac{x - 9}{\\sqrt{x} + 3}$. Giá trị của $P$ khi $x = 4$ là:", "options": ["$-1$", "$1$", "$5$", "$-5$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Rút gọn biểu thức $M = \\frac{a\\sqrt{b} + b\\sqrt{a}}{\\sqrt{a} + \\sqrt{b}}$ với $a > 0, b > 0$:", "options": ["$\\sqrt{ab}$", "$ab$", "$\\sqrt{a} + \\sqrt{b}$", "$a + b$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm $x$ biết $\\frac{\\sqrt{x} - 2}{\\sqrt{x} + 1} = \\frac{1}{2}$:", "options": ["$x = 25$", "$x = 5$", "$x = 9$", "$x = 16$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho biểu thức $A = \\frac{\\sqrt{x}}{\\sqrt{x} - 3}$ và $B = \\frac{2\\sqrt{x}}{\\sqrt{x} + 3}$. Có bao nhiêu giá trị nguyên của $x$ để $A \\cdot B < 0$?", "options": ["$8$ ($x \\in \\{1, 2, \\dots, 8\\}$)", "$9$", "$7$", "Vô số"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $P = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 1}$. Tìm $x$ để $P = \\sqrt{x}$:", "options": ["$Vô nghiệm$", "$x = 1$", "$x = 4$", "$x = 9$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $S = \\frac{1}{1 + \\sqrt{2}} + \\frac{1}{\\sqrt{2} + \\sqrt{3}} + \\dots + \\frac{1}{\\sqrt{n} + \\sqrt{n+1}}$ được kết quả là:", "options": ["$\\sqrt{n+1} - 1$", "$\\sqrt{n+1}$", "$\\sqrt{n} - 1$", "$n$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $P = \\frac{\\sqrt{x} + 3}{\\sqrt{x} + 1}$. Giá trị nhỏ nhất của $P$ khi $x \\ge 0$ là:", "options": ["$1$ (khi $x \\to +\\infty$, infimum là 1; tại $x = 0$ đạt max = 3)", "$3$", "$2$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho biểu thức $Q = \\frac{x + 2}{\\sqrt{x}}$ với $x > 0$. Giá trị nhỏ nhất của $Q$ là:", "options": ["$2\\sqrt{2}$", "$2$", "$4$", "$\\sqrt{2}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho biểu thức $P = \\frac{x + \\sqrt{x}}{\\sqrt{x}} - \\frac{x - 4}{\\sqrt{x} + 2}$ với $x > 0$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $\\frac{x + \\sqrt{x}}{\\sqrt{x}} = \\sqrt{x} + 1$.", "correct": True},
                {"subId": "b", "text": "Ta có $\\frac{x - 4}{\\sqrt{x} + 2} = \\sqrt{x} - 2$.", "correct": True},
                {"subId": "c", "text": "Giá trị của biểu thức $P = (\\sqrt{x} + 1) - (\\sqrt{x} - 2) = 3$.", "correct": True},
                {"subId": "d", "text": "Giá trị của biểu thức $P$ phụ thuộc vào biến $x$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $A = \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 2}$ với $x \\ge 0, x \\neq 4$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Biến đổi $A = 1 + \\frac{5}{\\sqrt{x} - 2}$.", "correct": True},
                {"subId": "b", "text": "Để $A$ nguyên thì $\\sqrt{x} - 2$ là ước của $5$.", "correct": True},
                {"subId": "c", "text": "Các giá trị nguyên của $x$ để $A$ nguyên là $x \\in \\{1; 9; 49\\}$.", "correct": True},
                {"subId": "d", "text": "Có 4 giá trị nguyên của $x$ để $A$ nguyên.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $P = (\\sqrt{3} + 1)^2 - 2\\sqrt{3}$.", "correctAnswer": "4", "explanation": "$3 + 2\\sqrt{3} + 1 - 2\\sqrt{3} = 4$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho biểu thức $P = \\frac{x - 1}{\\sqrt{x} - 1}$. Tính giá trị của $P$ khi $x = 16$.", "correctAnswer": "5", "explanation": "$P = \\sqrt{x} + 1 = \\sqrt{16} + 1 = 5$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $A = \\sqrt{x} + \\frac{4}{\\sqrt{x}}$.", "correctAnswer": "4", "explanation": "$A \\ge 2\\sqrt{\\sqrt{x} \\cdot \\frac{4}{\\sqrt{x}}} = 4$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số giá trị nguyên của $x$ để phân thức $\\frac{4}{\\sqrt{x} - 1}$ nhận giá trị nguyên ($x \\ge 0, x \\neq 1$).", "correctAnswer": "4", "explanation": "$\\sqrt{x} - 1 \\in \\{\\pm 1, \\pm 2, \\pm 4\\}$. Vì $\\sqrt{x} \\ge 0$ nên $\\sqrt{x} - 1 \\ge -1$. Các giá trị thỏa mãn: $\\sqrt{x} - 1 \\in \\{-1; 1; 2; 4\\} \\Rightarrow \\sqrt{x} \\in \\{0; 2; 3; 5\\} \\Rightarrow x \\in \\{0; 4; 9; 25\\}$. Có 4 giá trị."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho biểu thức:\n$$P = \\left(\\frac{1}{\\sqrt{x} - 2} - \\frac{1}{\\sqrt{x} + 2}\\right) : \\frac{\\sqrt{x}}{x - 4}$$ với $x > 0, x \\neq 4$.\na) Rút gọn biểu thức $P$.\nb) Tìm giá trị của $x$ để $P = 1$.",
            "solution": "a) Với $x > 0, x \\neq 4$:\n$\\frac{1}{\\sqrt{x} - 2} - \\frac{1}{\\sqrt{x} + 2} = \\frac{(\\sqrt{x} + 2) - (\\sqrt{x} - 2)}{(\\sqrt{x} - 2)(\\sqrt{x} + 2)} = \\frac{4}{x - 4}$.\nDo đó:\n$P = \\frac{4}{x - 4} : \\frac{\\sqrt{x}}{x - 4} = \\frac{4}{x - 4} \\cdot \\frac{x - 4}{\\sqrt{x}} = \\frac{4}{\\sqrt{x}}$.\nb) Để $P = 1$:\n$\\frac{4}{\\sqrt{x}} = 1 \\Leftrightarrow \\sqrt{x} = 4 \\Leftrightarrow x = 16$.\nGiá trị $x = 16$ thỏa mãn điều kiện $x > 0, x \\neq 4$.\nVậy $x = 16$.",
            "rubric": [
                {"step": "Quy đồng và rút gọn đúng P = 4/sqrt(x)", "subScore": 0.5},
                {"step": "Giải đúng x = 16, đối chiếu điều kiện và kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho biểu thức $A = \\frac{x + 2}{\\sqrt{x}}$ với $x > 0$.\na) Tìm giá trị nhỏ nhất của biểu thức $A$.\nb) Tìm $x$ để $A = 2\\sqrt{2}$.",
            "solution": "a) Với $x > 0$, ta tách $A = \\frac{x}{\\sqrt{x}} + \\frac{2}{\\sqrt{x}} = \\sqrt{x} + \\frac{2}{\\sqrt{x}}$.\nÁp dụng bất đẳng thức Cauchy cho hai số dương $\\sqrt{x}$ và $\\frac{2}{\\sqrt{x}}$:\n$A = \\sqrt{x} + \\frac{2}{\\sqrt{x}} \\ge 2\\sqrt{\\sqrt{x} \\cdot \\frac{2}{\\sqrt{x}}} = 2\\sqrt{2}$.\nDấu \"=\" xảy ra khi và chỉ khi:\n$\\sqrt{x} = \\frac{2}{\\sqrt{x}} \\Leftrightarrow (\\sqrt{x})^2 = 2 \\Leftrightarrow x = 2$ (thỏa mãn $x > 0$).\nVậy giá trị nhỏ nhất của $A$ là $2\\sqrt{2}$.\nb) Theo câu a, $A = 2\\sqrt{2}$ khi và chỉ khi dấu \"=\" của bất đẳng thức xảy ra, tức là $x = 2$.",
            "rubric": [
                {"step": "Tách A = sqrt(x) + 2/sqrt(x) và áp dụng BĐT Cauchy tìm GTNN = 2sqrt(2)", "subScore": 0.5},
                {"step": "Chỉ rõ dấu bằng xảy ra khi x = 2", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hai biểu thức $A = \\frac{\\sqrt{x}}{\\sqrt{x} - 2}$ và $B = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} + \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2} - \\frac{x + 4}{x - 4}$ với $x \\ge 0, x \\neq 4$.\na) Rút gọn biểu thức $B$.\nb) Đặt $P = \\frac{B}{A}$. Tìm các giá trị của $x$ để $P < \\frac{1}{2}$.",
            "solution": "a) Với $x \\ge 0, x \\neq 4$, mẫu thức chung là $x - 4 = (\\sqrt{x} - 2)(\\sqrt{x} + 2)$:\n$B = \\frac{(\\sqrt{x} + 1)(\\sqrt{x} + 2) + (\\sqrt{x} - 1)(\\sqrt{x} - 2) - (x + 4)}{x - 4}$\n$= \\frac{(x + 3\\sqrt{x} + 2) + (x - 3\\sqrt{x} + 2) - x - 4}{x - 4}$\n$= \\frac{2x + 4 - x - 4}{x - 4} = \\frac{x}{x - 4}$.\nb) Ta có:\n$P = \\frac{B}{A} = \\frac{x}{x - 4} : \\frac{\\sqrt{x}}{\\sqrt{x} - 2} = \\frac{x}{(\\sqrt{x} - 2)(\\sqrt{x} + 2)} \\cdot \\frac{\\sqrt{x} - 2}{\\sqrt{x}} = \\frac{\\sqrt{x}}{\\sqrt{x} + 2}$.\nXét bất phương trình $P < \\frac{1}{2}$:\n$\\frac{\\sqrt{x}}{\\sqrt{x} + 2} < \\frac{1}{2} \\Leftrightarrow 2\\sqrt{x} < \\sqrt{x} + 2$ (do $\\sqrt{x} + 2 > 0$)\n$\\Leftrightarrow \\sqrt{x} < 2 \\Leftrightarrow 0 \\le x < 4$.\nKết hợp với điều kiện xác định $x \\ge 0, x \\neq 4$ ta được: $0 \\le x < 4$.\nVậy tập nghiệm là $0 \\le x < 4$.",
            "rubric": [
                {"step": "Rút gọn đúng B = x/(x - 4) và P = sqrt(x)/(sqrt(x) + 2)", "subScore": 0.5},
                {"step": "Giải bất phương trình P < 1/2 ra 0 <= x < 4 và kết luận chuẩn xác", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI 10: CĂN BẬC BA VÀ CĂN THỨC BẬC BA (c3_9_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c3_9_bai4_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 10: Căn bậc ba và căn thức bậc ba - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Căn bậc ba của số thực $a$ là số $x$ sao cho:", "options": ["$x^3 = a$", "$x^2 = a$", "$3x = a$", "$x = 3a$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Mỗi số thực $a$ có bao nhiêu căn bậc ba?", "options": ["Duy nhất một căn bậc ba", "Hai căn bậc ba đối nhau", "Ba căn bậc ba", "Không có nếu $a < 0$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Căn bậc ba của $-8$ bằng:", "options": ["$-2$", "$2$", "$\\pm 2$", "Không xác định"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Căn bậc ba của $27$ bằng:", "options": ["$3$", "$-3$", "$\\pm 3$", "$9$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tính $\\sqrt[3]{125}$ được kết quả là:", "options": ["$5$", "$-5$", "$25$", "$15$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Tính $\\sqrt[3]{-64}$:", "options": ["$-4$", "$4$", "$\\pm 4$", "$-8$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt[3]{8} + \\sqrt[3]{-27}$:", "options": ["$-1$", "$5$", "$1$", "$-5$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Căn thức bậc ba $\\sqrt[3]{x - 5}$ xác định với:", "options": ["Mọi số thực $x$", "$x \\ge 5$", "$x > 5$", "$x \\le 5$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Tính $\\sqrt[3]{2} \\cdot \\sqrt[3]{4}$:", "options": ["$2$", "$4$", "$8$", "$\\sqrt[3]{6}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Tìm $x$ biết $\\sqrt[3]{x} = -3$:", "options": ["$x = -27$", "$x = 27$", "$x = -9$", "$x = 9$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $\\frac{\\sqrt[3]{54}}{\\sqrt[3]{2}}$:", "options": ["$3$", "$27$", "$9$", "$\\sqrt[3]{27}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một khối rubik hình lập phương có thể tích là $216\\text{ cm}^3$. Độ dài cạnh của khối rubik đó là:", "options": ["$6\\text{ cm}$", "$14\\text{ cm}$", "$36\\text{ cm}$", "$8\\text{ cm}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = \\sqrt[3]{64} - \\sqrt[3]{-125}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $\\sqrt[3]{64} = 4$.", "correct": True},
                {"subId": "b", "text": "Ta có $\\sqrt[3]{-125} = -5$.", "correct": True},
                {"subId": "c", "text": "Giá trị của biểu thức $A = 4 - (-5) = 9$.", "correct": True},
                {"subId": "d", "text": "Giá trị của biểu thức $A$ bằng $-1$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\sqrt[3]{2x - 1} = 3$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phương trình xác định với mọi số thực $x$.", "correct": True},
                {"subId": "b", "text": "Lập phương hai vế ta được $2x - 1 = 27$.", "correct": True},
                {"subId": "c", "text": "Nghiệm của phương trình là $x = 14$.", "correct": True},
                {"subId": "d", "text": "Phương trình có hai nghiệm phân biệt.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của $\\sqrt[3]{1000}$.", "correctAnswer": "10", "explanation": "$\\sqrt[3]{1000} = 10$ vì $10^3 = 1000$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt[3]{-216}$.", "correctAnswer": "-6", "explanation": "$\\sqrt[3]{-216} = -6$ vì $(-6)^3 = -216$."},
        {"id": 3, "level": "Vận dụng", "question": "Tìm $x$ biết $\\sqrt[3]{x + 2} = 4$.", "correctAnswer": "62", "explanation": "$x + 2 = 4^3 = 64 \\Rightarrow x = 62$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Một bể nước hình lập phương có dung tích chứa đúng $1331$ lít nước ($1\\text{ lít} = 1\\text{ dm}^3$). Tính độ dài cạnh trong của bể nước đó (dm).", "correctAnswer": "11", "explanation": "Cạnh = $\\sqrt[3]{1331} = 11\\text{ dm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Tính giá trị của các biểu thức sau:\na) $A = \\sqrt[3]{27} - \\sqrt[3]{-8} + \\sqrt[3]{125}$.\nb) $B = \\sqrt[3]{3} \\cdot \\sqrt[3]{9} + \\frac{\\sqrt[3]{128}}{\\sqrt[3]{2}}$.",
            "solution": "a) Ta có:\n$A = 3 - (-2) + 5 = 3 + 2 + 5 = 10$.\nb) Áp dụng tính chất nhân và chia căn bậc ba:\n$B = \\sqrt[3]{3 \\cdot 9} + \\sqrt[3]{\\frac{128}{2}} = \\sqrt[3]{27} + \\sqrt[3]{64} = 3 + 4 = 7$.",
            "rubric": [
                {"step": "Tính đúng A = 10", "subScore": 0.5},
                {"step": "Tính đúng B = 7", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải các phương trình sau:\na) $\\sqrt[3]{x - 2} = -2$.\nb) $\\sqrt[3]{3x + 1} = \\sqrt[3]{x - 5}$.",
            "solution": "a) $\\sqrt[3]{x - 2} = -2$\nLập phương hai vế:\n$x - 2 = (-2)^3 = -8 \\Leftrightarrow x = -8 + 2 = -6$.\nVậy nghiệm của phương trình là $x = -6$.\nb) $\\sqrt[3]{3x + 1} = \\sqrt[3]{x - 5}$\nLập phương hai vế:\n$3x + 1 = x - 5 \\Leftrightarrow 2x = -6 \\Leftrightarrow x = -3$.\nVậy nghiệm của phương trình là $x = -3$.",
            "rubric": [
                {"step": "Giải đúng câu a ra x = -6", "subScore": 0.5},
                {"step": "Giải đúng câu b ra x = -3", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tính giá trị của biểu thức:\n$$P = \\sqrt[3]{20 + 14\\sqrt{2}} + \\sqrt[3]{20 - 14\\sqrt{2}}$$",
            "solution": "Đặt $x = \\sqrt[3]{20 + 14\\sqrt{2}} + \\sqrt[3]{20 - 14\\sqrt{2}}$.\nÁp dụng hằng đẳng thức $(a + b)^3 = a^3 + b^3 + 3ab(a + b)$:\n$x^3 = (20 + 14\\sqrt{2}) + (20 - 14\\sqrt{2}) + 3\\sqrt[3]{(20 + 14\\sqrt{2})(20 - 14\\sqrt{2})} \\cdot x$\nTa có:\n$(20 + 14\\sqrt{2})(20 - 14\\sqrt{2}) = 20^2 - (14\\sqrt{2})^2 = 400 - 392 = 8$.\nDo đó $\\sqrt[3]{8} = 2$.\nSuy ra:\n$x^3 = 40 + 3(2)x \\Leftrightarrow x^3 - 6x - 40 = 0$\n$\\Leftrightarrow (x - 4)(x^2 + 4x + 10) = 0$.\nVì $x^2 + 4x + 10 = (x + 2)^2 + 6 > 0$ với mọi $x$, nên phương trình chỉ có nghiệm duy nhất $x = 4$.\nVậy $P = 4$.",
            "rubric": [
                {"step": "Lập phương hai vế và đưa về phương trình x^3 - 6x - 40 = 0", "subScore": 0.5},
                {"step": "Phân tích thành nhân tử và giải ra nghiệm duy nhất P = 4", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c3_9_bai4_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 10: Căn bậc ba và căn thức bậc ba - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tính chất nào sau đây SAI với căn bậc ba?", "options": ["$\\sqrt[3]{a}$ chỉ xác định khi $a \\ge 0$", "$a < b \\Leftrightarrow \\sqrt[3]{a} < \\sqrt[3]{b}$", "$\\sqrt[3]{ab} = \\sqrt[3]{a} \\cdot \\sqrt[3]{b}$", "$\\sqrt[3]{\\frac{a}{b}} = \\frac{\\sqrt[3]{a}}{\\sqrt[3]{b}}$ ($b \\neq 0$)"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tính $\\sqrt[3]{-0{,}027}$:", "options": ["$-0{,}3$", "$0{,}3$", "$-0{,}03$", "$0{,}03$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tính $\\sqrt[3]{5} \\cdot \\sqrt[3]{25}$:", "options": ["$5$", "$25$", "$125$", "$\\sqrt[3]{30}$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\sqrt[3]{8a^3}$:", "options": ["$2a$", "$2|a|$", "$4a$", "$8a$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\sqrt[3]{-27x^3}$:", "options": ["$-3x$", "$3x$", "$3|x|$", "$-9x$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt[3]{x^3 - 7} = 1$. Nghiệm là:", "options": ["$x = 2$", "$x = -2$", "$x = \\pm 2$", "$x = 8$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "So sánh $2\\sqrt[3]{3}$ và $\\sqrt[3]{25}$:", "options": ["$2\\sqrt[3]{3} < \\sqrt[3]{25}$", "$2\\sqrt[3]{3} > \\sqrt[3]{25}$", "$2\\sqrt[3]{3} = \\sqrt[3]{25}$", "Không so sánh được"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Giá trị của biểu thức $(\\sqrt[3]{2} - 1)(\\sqrt[3]{4} + \\sqrt[3]{2} + 1)$ là:", "options": ["$1$", "$3$", "$2$", "$-1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt[3]{x} + \\sqrt[3]{-x} = 0$. Số nghiệm của phương trình là:", "options": ["Vô số nghiệm", "$1$ nghiệm", "$0$ nghiệm", "$2$ nghiệm"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $x = \\sqrt[3]{5\\sqrt{2} + 7} - \\sqrt[3]{5\\sqrt{2} - 7}$. Giá trị của $x$ là:", "options": ["$2$", "$\\sqrt{2}$", "$1$", "$2\\sqrt{2}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm $x$ biết $\\sqrt[3]{x + 1} + \\sqrt[3]{x - 1} = 0$:", "options": ["$x = 0$", "$x = 1$", "$x = -1$", "Vô nghiệm"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một thùng chứa hình lập phương có thể tích gấp $8$ lần thùng chứa hình lập phương có cạnh $3\\text{ m}$. Cạnh của thùng lớn dài:", "options": ["$6\\text{ m}$", "$12\\text{ m}$", "$24\\text{ m}$", "$9\\text{ m}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = \\sqrt[3]{54} - \\sqrt[3]{16}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $\\sqrt[3]{54} = \\sqrt[3]{27 \\cdot 2} = 3\\sqrt[3]{2}$.", "correct": True},
                {"subId": "b", "text": "Ta có $\\sqrt[3]{16} = \\sqrt[3]{8 \\cdot 2} = 2\\sqrt[3]{2}$.", "correct": True},
                {"subId": "c", "text": "Giá trị rút gọn của $A = \\sqrt[3]{2}$.", "correct": True},
                {"subId": "d", "text": "Giá trị của $A$ là một số nguyên.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho biểu thức $P = (\\sqrt[3]{x} + 2)(\\sqrt[3]{x^2} - 2\\sqrt[3]{x} + 4)$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Áp dụng hằng đẳng thức $(a + b)(a^2 - ab + b^2) = a^3 + b^3$.", "correct": True},
                {"subId": "b", "text": "Biểu thức rút gọn được thành $P = x + 8$.", "correct": True},
                {"subId": "c", "text": "Khi $x = -8$ thì $P = 0$.", "correct": True},
                {"subId": "d", "text": "Khi $x = 0$ thì $P = 16$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt[3]{343}$.", "correctAnswer": "7", "explanation": "$7^3 = 343$ nên $\\sqrt[3]{343} = 7$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt[3]{-512}$.", "correctAnswer": "-8", "explanation": "$(-8)^3 = -512$ nên $\\sqrt[3]{-512} = -8$."},
        {"id": 3, "level": "Vận dụng", "question": "Rút gọn biểu thức $\\sqrt[3]{128} : \\sqrt[3]{2}$.", "correctAnswer": "4", "explanation": "$\\sqrt[3]{128 / 2} = \\sqrt[3]{64} = 4$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Giải phương trình $\\sqrt[3]{x^3 + 19} = 3$. Tìm $x$.", "correctAnswer": "2", "explanation": "$x^3 + 19 = 27 \\Rightarrow x^3 = 8 \\Rightarrow x = 2$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Rút gọn biểu thức sau:\n$$A = \\sqrt[3]{250} - \\sqrt[3]{128} + \\sqrt[3]{16}$$",
            "solution": "Phân tích các số dưới dấu căn ra thừa số nguyên tố:\n$\\sqrt[3]{250} = \\sqrt[3]{125 \\cdot 2} = 5\\sqrt[3]{2}$.\n$\\sqrt[3]{128} = \\sqrt[3]{64 \\cdot 2} = 4\\sqrt[3]{2}$.\n$\\sqrt[3]{16} = \\sqrt[3]{8 \\cdot 2} = 2\\sqrt[3]{2}$.\nDo đó:\n$A = 5\\sqrt[3]{2} - 4\\sqrt[3]{2} + 2\\sqrt[3]{2} = 3\\sqrt[3]{2}$.\nVậy $A = 3\\sqrt[3]{2}$.",
            "rubric": [
                {"step": "Đưa thừa số ra ngoài dấu căn đúng cho cả 3 số hạng", "subScore": 0.5},
                {"step": "Thu gọn các căn thức đồng dạng ra 3 căn bậc ba của 2", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải phương trình sau:\n$$\\sqrt[3]{x^3 + 3x^2 + 3x + 2} = 2$$",
            "solution": "Nhận xét: $x^3 + 3x^2 + 3x + 1 = (x + 1)^3$.\nDo đó: $x^3 + 3x^2 + 3x + 2 = (x + 1)^3 + 1$.\nPhương trình tương đương với:\n$\\sqrt[3]{(x + 1)^3 + 1} = 2$.\nLập phương hai vế:\n$(x + 1)^3 + 1 = 2^3 = 8$\n$\\Leftrightarrow (x + 1)^3 = 7$\n$\\Leftrightarrow x + 1 = \\sqrt[3]{7}$\n$\\Leftrightarrow x = \\sqrt[3]{7} - 1$.\nVậy nghiệm của phương trình là $x = \\sqrt[3]{7} - 1$.",
            "rubric": [
                {"step": "Lập phương hai vế đưa về (x + 1)^3 = 7", "subScore": 0.5},
                {"step": "Giải đúng nghiệm x = căn bậc ba của 7 trừ 1", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Chứng minh rằng số sau là một số nguyên:\n$$x = \\sqrt[3]{7 + 5\\sqrt{2}} + \\sqrt[3]{7 - 5\\sqrt{2}}$$",
            "solution": "Áp dụng hằng đẳng thức $(a + b)^3 = a^3 + b^3 + 3ab(a + b)$:\n$x^3 = (7 + 5\\sqrt{2}) + (7 - 5\\sqrt{2}) + 3\\sqrt[3]{(7 + 5\\sqrt{2})(7 - 5\\sqrt{2})} \\cdot x$.\nTa có:\n$(7 + 5\\sqrt{2})(7 - 5\\sqrt{2}) = 7^2 - (5\\sqrt{2})^2 = 49 - 50 = -1$.\nDo đó: $\\sqrt[3]{-1} = -1$.\nSuy ra:\n$x^3 = 14 + 3(-1)x \\Leftrightarrow x^3 + 3x - 14 = 0$\n$\\Leftrightarrow x^3 - 2x^2 + 2x^2 - 4x + 7x - 14 = 0$\n$\\Leftrightarrow (x - 2)(x^2 + 2x + 7) = 0$.\nVì $x^2 + 2x + 7 = (x + 1)^2 + 6 > 0$ với mọi $x$,\nnên phương trình có nghiệm duy nhất $x = 2$.\nVì $2 \\in \\mathbb{Z}$ nên $x$ là một số nguyên.",
            "rubric": [
                {"step": "Lập phương hai vế và đưa về phương trình x^3 + 3x - 14 = 0", "subScore": 0.5},
                {"step": "Phân tích nhân tử tìm ra nghiệm duy nhất x = 2 và kết luận", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c3_9_bai4_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 10: Căn bậc ba và căn thức bậc ba - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Khẳng định nào sau đây SAI?", "options": ["$\\sqrt[3]{-a} = \\sqrt[3]{a}$", "$\\sqrt[3]{-a} = -\\sqrt[3]{a}$", "$(\\sqrt[3]{a})^3 = a$", "$\\sqrt[3]{a^3} = a$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tính $\\sqrt[3]{20 + 14\\sqrt{2}} + \\sqrt[3]{20 - 14\\sqrt{2}}$ được kết quả là:", "options": ["$4$", "$2\\sqrt{2}$", "$2$", "$4\\sqrt{2}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Nghiệm của phương trình $\\sqrt[3]{x} = -4$ là:", "options": ["$x = -64$", "$x = 64$", "$x = -12$", "$x = -16$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Rút gọn biểu thức $P = \\frac{a - b}{\\sqrt[3]{a} - \\sqrt[3]{b}}$ ($a \\neq b$):", "options": ["$\\sqrt[3]{a^2} + \\sqrt[3]{ab} + \\sqrt[3]{b^2}$", "$\\sqrt[3]{a^2} - \\sqrt[3]{ab} + \\sqrt[3]{b^2}$", "$\\sqrt[3]{a} + \\sqrt[3]{b}$", "$a + b$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt[3]{x + 1} + \\sqrt[3]{x + 2} + \\sqrt[3]{x + 3} = 0$. Nghiệm của phương trình là:", "options": ["$x = -2$", "$x = 0$", "$x = 2$", "$x = -1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $x = \\sqrt[3]{2 + \\sqrt{5}} + \\sqrt[3]{2 - \\sqrt{5}}$. Khẳng định nào sau đây đúng?", "options": ["$x^3 + 3x - 4 = 0 \\Rightarrow x = 1$", "$x = 2$", "$x = 0$", "$x = 4$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $\\sqrt[3]{1 + \\sqrt{2}} \\cdot \\sqrt[3]{1 - \\sqrt{2}}$:", "options": ["$-1$", "$1$", "$\\sqrt{2}$", "$-\\sqrt{2}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Giải phương trình $\\sqrt[3]{x - 1} + \\sqrt[3]{x - 2} = \\sqrt[3]{2x - 3}$. Số nghiệm của phương trình là:", "options": ["$3$ nghiệm ($x = 1, x = 2, x = 1{,}5$)", "$1$ nghiệm", "$2$ nghiệm", "$0$ nghiệm"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tính giá trị của biểu thức $P = \\sqrt[3]{9 + 4\\sqrt{5}} + \\sqrt[3]{9 - 4\\sqrt{5}}$:", "options": ["$3$", "$1$", "$2$", "$4$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $M = \\sqrt[3]{a + 3\\sqrt[3]{a^2 b} + 3\\sqrt[3]{ab^2} + b}$:", "options": ["$\\sqrt[3]{a} + \\sqrt[3]{b}$", "$\\sqrt[3]{a} - \\sqrt[3]{b}$", "$a + b$", "$\\sqrt{a} + \\sqrt{b}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số nghiệm nguyên của phương trình $\\sqrt[3]{x + 2} + \\sqrt{x - 1} = 3$ là:", "options": ["$1$ ($x = 2$)", "$2$", "$0$", "$3$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $a, b, c$ thỏa mãn $\\sqrt[3]{a} + \\sqrt[3]{b} + \\sqrt[3]{c} = 0$. Khi đó đẳng thức nào sau đây đúng?", "options": ["$(a + b + c)^3 = 27abc$", "$a + b + c = 3abc$", "$a^3 + b^3 + c^3 = 3abc$", "$a + b + c = 0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\sqrt[3]{x + 1} + \\sqrt[3]{x - 1} = \\sqrt[3]{2x}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phương trình xác định với mọi số thực $x$.", "correct": True},
                {"subId": "b", "text": "Lập phương hai vế ta được $(x + 1) + (x - 1) + 3\\sqrt[3]{(x+1)(x-1)}(\\sqrt[3]{x+1}+\\sqrt[3]{x-1}) = 2x$.", "correct": True},
                {"subId": "c", "text": "Thu gọn được $3\\sqrt[3]{x^2 - 1}\\sqrt[3]{2x} = 0$.", "correct": True},
                {"subId": "d", "text": "Phương trình có đúng 3 nghiệm phân biệt $x = 0, x = 1, x = -1$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $x = \\sqrt[3]{4 + 2\\sqrt{2}} + \\sqrt[3]{4 - 2\\sqrt{2}}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Tích của hai căn là $\\sqrt[3]{16 - 8} = \\sqrt[3]{8} = 2$.", "correct": True},
                {"subId": "b", "text": "Lập phương hai vế ta được phương trình $x^3 = 8 + 6x$.", "correct": True},
                {"subId": "c", "text": "Phương trình $x^3 - 6x - 8 = 0$ có nghiệm nguyên $x = 2$ không đúng, nghiệm là $x = \\sqrt{2} + \\sqrt{2}$?", "correct": False},
                {"subId": "d", "text": "Phương trình $x^3 - 6x - 8 = 0$ vô nghiệm thực.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt[3]{64} + \\sqrt[3]{-125} + \\sqrt[3]{216}$.", "correctAnswer": "5", "explanation": "$4 + (-5) + 6 = 5$."},
        {"id": 2, "level": "Vận dụng", "question": "Tìm nghiệm của phương trình $\\sqrt[3]{2x - 3} = -3$.", "correctAnswer": "-12", "explanation": "$2x - 3 = -27 \\Rightarrow 2x = -24 \\Rightarrow x = -12$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Giải phương trình $\\sqrt[3]{x} + \\sqrt[3]{x - 16} = 0$. Tìm $x$.", "correctAnswer": "8", "explanation": "$\\sqrt[3]{x} = -\\sqrt[3]{x - 16} = \\sqrt[3]{16 - x} \\Rightarrow x = 16 - x \\Rightarrow 2x = 16 \\Rightarrow x = 8$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính giá trị của $x = \\sqrt[3]{10 + 6\\sqrt{3}} - \\sqrt{3}$.", "correctAnswer": "1", "explanation": "$10 + 6\\sqrt{3} = (1 + \\sqrt{3})^3 \\Rightarrow \\sqrt[3]{10 + 6\\sqrt{3}} = 1 + \\sqrt{3}$. Vậy $x = 1 + \\sqrt{3} - \\sqrt{3} = 1$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Tính giá trị của biểu thức:\n$$A = \\sqrt[3]{5\\sqrt{2} + 7} - \\sqrt[3]{5\\sqrt{2} - 7}$$",
            "solution": "Đặt $A = x$.\nÁp dụng hằng đẳng thức $(a - b)^3 = a^3 - b^3 - 3ab(a - b)$:\n$x^3 = (5\\sqrt{2} + 7) - (5\\sqrt{2} - 7) - 3\\sqrt[3]{(5\\sqrt{2} + 7)(5\\sqrt{2} - 7)} \\cdot x$\nTa có:\n$(5\\sqrt{2} + 7)(5\\sqrt{2} - 7) = (5\\sqrt{2})^2 - 7^2 = 50 - 49 = 1$.\nDo đó: $\\sqrt[3]{1} = 1$.\nSuy ra:\n$x^3 = 14 - 3(1)x \\Leftrightarrow x^3 + 3x - 14 = 0$\n$\\Leftrightarrow (x - 2)(x^2 + 2x + 7) = 0$.\nVì $x^2 + 2x + 7 = (x + 1)^2 + 6 > 0$ với mọi $x$,\nnên phương trình có nghiệm duy nhất $x = 2$.\nVậy $A = 2$.",
            "rubric": [
                {"step": "Lập phương biểu thức và áp dụng hằng đẳng thức hiệu hai số", "subScore": 0.5},
                {"step": "Giải phương trình x^3 + 3x - 14 = 0 ra nghiệm duy nhất A = 2", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình:\n$$\\sqrt[3]{x + 1} + \\sqrt[3]{3x + 1} = \\sqrt[3]{x - 1}$$",
            "solution": "Phương trình xác định với mọi $x \\in \\mathbb{R}$.\nÁp dụng hằng đẳng thức: Nếu $a + b + c = 0$ thì $a^3 + b^3 + c^3 = 3abc$.\nViết lại phương trình dưới dạng tổng bằng 0:\n$\\sqrt[3]{x + 1} + \\sqrt[3]{3x + 1} + \\sqrt[3]{1 - x} = 0$.\nĐặt $a = \\sqrt[3]{x + 1}, b = \\sqrt[3]{3x + 1}, c = \\sqrt[3]{1 - x}$.\nVì $a + b + c = 0$ nên $a^3 + b^3 + c^3 = 3abc$.\nTa có: $a^3 + b^3 + c^3 = (x + 1) + (3x + 1) + (1 - x) = 3x + 3 = 3(x + 1)$.\nDo đó:\n$3(x + 1) = 3\\sqrt[3]{(x + 1)(3x + 1)(1 - x)}$\n$\\Leftrightarrow x + 1 = \\sqrt[3]{(x + 1)(3x + 1)(1 - x)}$\nLập phương hai vế:\n$(x + 1)^3 = (x + 1)(3x + 1)(1 - x)$\n$\\Leftrightarrow (x + 1)[(x + 1)^2 - (3x + 1)(1 - x)] = 0$\n$\\Leftrightarrow (x + 1)[(x^2 + 2x + 1) - (3x - 3x^2 + 1 - x)] = 0$\n$\\Leftrightarrow (x + 1)(4x^2) = 0$\n$\\Leftrightarrow x = -1$ hoặc $x = 0$.\nThử lại cả hai giá trị đều thỏa mãn phương trình ban đầu.\nVậy tập nghiệm của phương trình là $S = \\{-1; 0\\}$.",
            "rubric": [
                {"step": "Chuyển vế và áp dụng tính chất a + b + c = 0 => a^3 + b^3 + c^3 = 3abc", "subScore": 0.5},
                {"step": "Lập phương, đặt nhân tử chung giải ra nghiệm x = -1, x = 0", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $x = \\sqrt[3]{a + \\frac{a+1}{3}\\sqrt{\\frac{8a-1}{3}}} + \\sqrt[3]{a - \\frac{a+1}{3}\\sqrt{\\frac{8a-1}{3}}}$. Chứng minh rằng với $a \\ge \\frac{1}{8}$ thì $x$ luôn là một số nguyên dương.",
            "solution": "Đặt $u = \\sqrt[3]{a + \\frac{a+1}{3}\\sqrt{\\frac{8a-1}{3}}}$ và $v = \\sqrt[3]{a - \\frac{a+1}{3}\\sqrt{\\frac{8a-1}{3}}}$.\nTa có: $x = u + v$.\nTính tích $uv$:\n$uv = \\sqrt[3]{a^2 - \\left(\\frac{a+1}{3}\\right)^2 \\cdot \\frac{8a-1}{3}} = \\sqrt[3]{a^2 - \\frac{(a^2+2a+1)(8a-1)}{27}}$\n$= \\sqrt[3]{\\frac{27a^2 - (8a^3 + 15a^2 + 6a - 1)}{27}} = \\sqrt[3]{\\frac{-8a^3 + 12a^2 - 6a + 1}{27}}$\n$= \\sqrt[3]{\\frac{(1 - 2a)^3}{27}} = \\frac{1 - 2a}{3}$.\nLập phương hai vế của $x = u + v$:\n$x^3 = u^3 + v^3 + 3uv(u + v) = 2a + 3 \\cdot \\frac{1 - 2a}{3} \\cdot x$\n$\\Leftrightarrow x^3 = 2a + (1 - 2a)x \\Leftrightarrow x^3 + (2a - 1)x - 2a = 0$\n$\\Leftrightarrow (x - 1)(x^2 + x + 2a) = 0$.\nVì $a \\ge \\frac{1}{8}$ nên $x^2 + x + 2a = (x + \\frac{1}{2})^2 + 2a - \\frac{1}{4} \\ge (x + \\frac{1}{2})^2 + 2(\\frac{1}{8}) - \\frac{1}{4} = (x + \\frac{1}{2})^2 \\ge 0$.\nĐặc biệt $x^2 + x + 2a > 0$ với mọi $x$.\nDo đó phương trình có nghiệm thực duy nhất $x = 1$.\nVì $1$ là số nguyên dương nên $x$ luôn là số nguyên dương với mọi $a \\ge \\frac{1}{8}$.",
            "rubric": [
                {"step": "Tính đúng tích uv = (1 - 2a)/3", "subScore": 0.5},
                {"step": "Lập phương giải ra nghiệm duy nhất x = 1 và kết luận x là số nguyên dương", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG III: CĂN BẬC HAI VÀ CĂN BẬC BA (c3_9_bai5)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c3_9_bai5_test1"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương III - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Căn bậc hai số học của $36$ là:", "options": ["$6$", "$-6$", "$\\pm 6$", "$18$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Căn thức $\\sqrt{x - 4}$ có nghĩa khi:", "options": ["$x \\ge 4$", "$x > 4$", "$x \\le 4$", "$x < 4$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Khẳng định nào sau đây đúng với mọi $a \\ge 0, b \\ge 0$?", "options": ["$\\sqrt{ab} = \\sqrt{a} \\cdot \\sqrt{b}$", "$\\sqrt{a + b} = \\sqrt{a} + \\sqrt{b}$", "$\\sqrt{a - b} = \\sqrt{a} - \\sqrt{b}$", "$\\sqrt{ab} = a\\sqrt{b}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Căn bậc ba của $-125$ là:", "options": ["$-5$", "$5$", "$\\pm 5$", "Không xác định"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{(-7)^2}$ là:", "options": ["$7$", "$-7$", "$\\pm 7$", "$49$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Rút gọn biểu thức $\\sqrt{50} - \\sqrt{18}$ được kết quả là:", "options": ["$2\\sqrt{2}$", "$8\\sqrt{2}$", "$\\sqrt{32}$", "$4\\sqrt{2}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Trục căn thức ở mẫu của $\\frac{2}{\\sqrt{2}}$ ta được:", "options": ["$\\sqrt{2}$", "$2$", "$1$", "$\\frac{1}{\\sqrt{2}}$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Giá trị của $\\sqrt[3]{8} + \\sqrt[3]{27}$ là:", "options": ["$5$", "$35$", "$\\sqrt[3]{35}$", "$6$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Nghiệm của phương trình $\\sqrt{x} = 4$ là:", "options": ["$x = 16$", "$x = 2$", "$x = \\pm 16$", "$x = 8$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Rút gọn biểu thức $\\sqrt{4 - 2\\sqrt{3}}$ được kết quả là:", "options": ["$\\sqrt{3} - 1$", "$1 - \\sqrt{3}$", "$\\sqrt{3} + 1$", "$2 - \\sqrt{3}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho biểu thức $P = \\frac{x - 1}{\\sqrt{x} + 1}$ với $x \\ge 0$. Giá trị của $P$ khi $x = 9$ là:", "options": ["$2$", "$4$", "$3$", "$8$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giải phương trình $\\sqrt[3]{x - 1} = 2$. Nghiệm là:", "options": ["$x = 9$", "$x = 7$", "$x = 8$", "$x = 5$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $A = \\sqrt{20} - 2\\sqrt{45} + 3\\sqrt{5}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $\\sqrt{20} = 2\\sqrt{5}$.", "correct": True},
                {"subId": "b", "text": "Ta có $2\\sqrt{45} = 6\\sqrt{5}$.", "correct": True},
                {"subId": "c", "text": "Biểu thức thu gọn được $A = -\\sqrt{5}$.", "correct": True},
                {"subId": "d", "text": "Biểu thức $A$ có giá trị dương.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\sqrt{x^2 - 2x + 1} = 3$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phương trình tương đương với $|x - 1| = 3$.", "correct": True},
                {"subId": "b", "text": "Phương trình có nghiệm $x = 4$.", "correct": True},
                {"subId": "c", "text": "Phương trình có nghiệm $x = -2$.", "correct": True},
                {"subId": "d", "text": "Tổng các nghiệm của phương trình bằng $0$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của căn bậc hai $\\sqrt{169}$.", "correctAnswer": "13", "explanation": "$\\sqrt{169} = 13$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt[3]{-64} + 10$.", "correctAnswer": "6", "explanation": "$-4 + 10 = 6$."},
        {"id": 3, "level": "Vận dụng", "question": "Rút gọn biểu thức $\\frac{6}{\\sqrt{3}}$. Kết quả có dạng $a\\sqrt{3}$. Tìm $a$.", "correctAnswer": "2", "explanation": "$\\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}$. Vậy $a = 2$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm $x$ biết $\\sqrt{x + 1} = 5$.", "correctAnswer": "24", "explanation": "$x + 1 = 25 \\Rightarrow x = 24$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Thực hiện phép tính:\na) $A = 3\\sqrt{8} - \\sqrt{50} + \\sqrt{18}$.\nb) $B = (\\sqrt{3} + 1)(\\sqrt{3} - 1) + \\frac{\\sqrt{27}}{\\sqrt{3}}$.",
            "solution": "a) Đưa thừa số ra ngoài dấu căn:\n$A = 3 \\cdot 2\\sqrt{2} - 5\\sqrt{2} + 3\\sqrt{2} = 6\\sqrt{2} - 5\\sqrt{2} + 3\\sqrt{2} = 4\\sqrt{2}$.\nb) $B = ((\\sqrt{3})^2 - 1^2) + \\sqrt{\\frac{27}{3}} = (3 - 1) + \\sqrt{9} = 2 + 3 = 5$.",
            "rubric": [
                {"step": "Tính đúng A = 4sqrt(2)", "subScore": 0.5},
                {"step": "Tính đúng B = 5", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 1} + \\frac{\\sqrt{x}}{x - 1}\\right) : \\frac{2\\sqrt{x} + 1}{x - 1}$ với $x \\ge 0, x \\neq 1$.\na) Rút gọn biểu thức $P$.\nb) Tính giá trị của $P$ khi $x = 4$.",
            "solution": "a) Quy đồng mẫu thức trong ngoặc với mẫu chung là $x - 1 = (\\sqrt{x} - 1)(\\sqrt{x} + 1)$:\n$\\frac{1}{\\sqrt{x} - 1} + \\frac{\\sqrt{x}}{x - 1} = \\frac{\\sqrt{x} + 1 + \\sqrt{x}}{x - 1} = \\frac{2\\sqrt{x} + 1}{x - 1}$.\nDo đó:\n$P = \\frac{2\\sqrt{x} + 1}{x - 1} : \\frac{2\\sqrt{x} + 1}{x - 1} = 1$.\nb) Vì $P = 1$ với mọi $x \\ge 0, x \\neq 1$ nên khi $x = 4$ thì giá trị của $P$ vẫn bằng $1$.",
            "rubric": [
                {"step": "Quy đồng và rút gọn đúng P = 1", "subScore": 0.5},
                {"step": "Tính đúng giá trị P = 1 khi x = 4", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm các giá trị của $x$ để biểu thức $M = \\frac{4}{\\sqrt{x} - 3}$ nhận giá trị nguyên ($x \\ge 0, x \\neq 9$).",
            "solution": "Để biểu thức $M$ nhận giá trị nguyên thì $\\sqrt{x} - 3$ phải là ước của $4$.\nƯớc của $4$ gồm các số $\\{\\pm 1; \\pm 2; \\pm 4\\}$.\nVì $x \\ge 0$ nên $\\sqrt{x} \\ge 0 \\Rightarrow \\sqrt{x} - 3 \\ge -3$.\nDo đó ta xét các trường hợp:\n- $\\sqrt{x} - 3 = 1 \\Rightarrow \\sqrt{x} = 4 \\Rightarrow x = 16$ (thỏa mãn ĐK).\n- $\\sqrt{x} - 3 = -1 \\Rightarrow \\sqrt{x} = 2 \\Rightarrow x = 4$ (thỏa mãn ĐK).\n- $\\sqrt{x} - 3 = 2 \\Rightarrow \\sqrt{x} = 5 \\Rightarrow x = 25$ (thỏa mãn ĐK).\n- $\\sqrt{x} - 3 = -2 \\Rightarrow \\sqrt{x} = 1 \\Rightarrow x = 1$ (thỏa mãn ĐK).\n- $\\sqrt{x} - 3 = 4 \\Rightarrow \\sqrt{x} = 7 \\Rightarrow x = 49$ (thỏa mãn ĐK).\nVậy các giá trị nguyên của $x$ là $x \\in \\{1; 4; 16; 25; 49\\}$.",
            "rubric": [
                {"step": "Lập luận sqrt(x) - 3 là ước của 4 và điều kiện sqrt(x) - 3 >= -3", "subScore": 0.5},
                {"step": "Tìm đúng 5 giá trị của x và đối chiếu điều kiện", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c3_9_bai5_test2"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương III - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Biểu thức $\\sqrt{(3 - \\pi)^2}$ có giá trị bằng:", "options": ["$\\pi - 3$", "$3 - \\pi$", "$\\pm(3 - \\pi)$", "Không xác định"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Rút gọn biểu thức $A = \\sqrt{75} - \\sqrt{48} + \\sqrt{300}$:", "options": ["$11\\sqrt{3}$", "$9\\sqrt{3}$", "$13\\sqrt{3}$", "$15\\sqrt{3}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Trục căn thức ở mẫu của $\\frac{4}{3 - \\sqrt{5}}$ được kết quả là:", "options": ["$3 + \\sqrt{5}$", "$3 - \\sqrt{5}$", "$\\frac{3 + \\sqrt{5}}{4}$", "$4(3 + \\sqrt{5})$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt[3]{2} \\cdot \\sqrt[3]{32}$:", "options": ["$4$", "$8$", "$2$", "$\\sqrt[3]{64}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Nghiệm của phương trình $\\sqrt{2x - 1} = 3$ là:", "options": ["$x = 5$", "$x = 4$", "$x = 10$", "$x = 2$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Rút gọn biểu thức $M = \\sqrt{14 - 6\\sqrt{5}}$ được kết quả là:", "options": ["$3 - \\sqrt{5}$", "$\\sqrt{5} - 3$", "$3 + \\sqrt{5}$", "Không rút gọn được"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{4x - 8} - 2 = 0$. Nghiệm là:", "options": ["$x = 3$", "$x = 2$", "$x = 4$", "$x = 6$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Giá trị của biểu thức $\\frac{1}{2 + \\sqrt{3}} - \\frac{1}{2 - \\sqrt{3}}$ là:", "options": ["$-2\\sqrt{3}$", "$2\\sqrt{3}$", "$4$", "$-4$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho biểu thức $P = \\frac{x - \\sqrt{x}}{\\sqrt{x} - 1}$ với $x > 0, x \\neq 1$. Giá trị của $P$ khi $x = 16$ là:", "options": ["$4$", "$16$", "$2$", "$8$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = x - 4\\sqrt{x} + 7$ với $x \\ge 0$:", "options": ["$3$", "$7$", "$4$", "$1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tính giá trị biểu thức $S = \\sqrt[3]{10 + 6\\sqrt{3}} + \\sqrt[3]{10 - 6\\sqrt{3}}$:", "options": ["$2$", "$\\sqrt{3}$", "$2\\sqrt{3}$", "$4$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giải phương trình $\\sqrt{x - 1} + \\sqrt{4x - 4} = 6$. Nghiệm là:", "options": ["$x = 5$", "$x = 4$", "$x = 9$", "$x = 17$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 2} - \\frac{1}{\\sqrt{x} + 2}\\right) \\cdot \\frac{x - 4}{4}$ với $x \\ge 0, x \\neq 4$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Quy đồng mẫu thức trong ngoặc được $\\frac{4}{x - 4}$.", "correct": True},
                {"subId": "b", "text": "Giá trị rút gọn của $P$ là $1$.", "correct": True},
                {"subId": "c", "text": "Biểu thức $P$ phụ thuộc vào giá trị của $x$.", "correct": False},
                {"subId": "d", "text": "Khi $x = 9$ thì $P = 1$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\sqrt{9x - 18} - 2\\sqrt{x - 2} = 3$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điều kiện xác định của phương trình là $x \\ge 2$.", "correct": True},
                {"subId": "b", "text": "Phương trình tương đương với $3\\sqrt{x - 2} - 2\\sqrt{x - 2} = 3$.", "correct": True},
                {"subId": "c", "text": "Thu gọn được $\\sqrt{x - 2} = 3$.", "correct": True},
                {"subId": "d", "text": "Nghiệm của phương trình là $x = 11$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $(\\sqrt{8} - 3\\sqrt{2}) \\cdot \\sqrt{2}$.", "correctAnswer": "-2", "explanation": "$(2\\sqrt{2} - 3\\sqrt{2})\\sqrt{2} = -\\sqrt{2} \\cdot \\sqrt{2} = -2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $\\sqrt[3]{-27} + \\sqrt[3]{64}$.", "correctAnswer": "1", "explanation": "$-3 + 4 = 1$."},
        {"id": 3, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{x - 3} = 4$. Tìm giá trị của $x$.", "correctAnswer": "19", "explanation": "$x - 3 = 16 \\Rightarrow x = 19$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $P = x - 2\\sqrt{x} + 5$ với $x \\ge 0$.", "correctAnswer": "4", "explanation": "$P = (\\sqrt{x} - 1)^2 + 4 \\ge 4$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Rút gọn các biểu thức sau:\na) $A = \\sqrt{48} - 3\\sqrt{75} + 2\\sqrt{108}$.\nb) $B = \\frac{2}{\\sqrt{3} - 1} - \\frac{2}{\\sqrt{3} + 1}$.",
            "solution": "a) Đưa thừa số ra ngoài dấu căn:\n$A = 4\\sqrt{3} - 3 \\cdot 5\\sqrt{3} + 2 \\cdot 6\\sqrt{3} = 4\\sqrt{3} - 15\\sqrt{3} + 12\\sqrt{3} = \\sqrt{3}$.\nb) Trục căn thức ở mẫu:\n$B = \\frac{2(\\sqrt{3} + 1)}{3 - 1} - \\frac{2(\\sqrt{3} - 1)}{3 - 1} = (\\sqrt{3} + 1) - (\\sqrt{3} - 1) = 2$.",
            "rubric": [
                {"step": "Tính đúng A = sqrt(3)", "subScore": 0.5},
                {"step": "Tính đúng B = 2", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho biểu thức $P = \\left(\\frac{\\sqrt{x}}{\\sqrt{x} - 1} - \\frac{1}{x - \\sqrt{x}}\\right) : \\frac{\\sqrt{x} + 1}{x - 1}$ với $x > 0, x \\neq 1$.\na) Rút gọn biểu thức $P$.\nb) Tìm giá trị của $x$ để $P = \\frac{1}{2}$.",
            "solution": "a) Với $x > 0, x \\neq 1$:\nTa có: $x - \\sqrt{x} = \\sqrt{x}(\\sqrt{x} - 1)$.\nQuy đồng mẫu thức trong ngoặc:\n$\\frac{\\sqrt{x}}{\\sqrt{x} - 1} - \\frac{1}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{x - 1}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} + 1)}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{\\sqrt{x} + 1}{\\sqrt{x}}$.\nDo đó:\n$P = \\frac{\\sqrt{x} + 1}{\\sqrt{x}} : \\frac{\\sqrt{x} + 1}{x - 1} = \\frac{\\sqrt{x} + 1}{\\sqrt{x}} \\cdot \\frac{(\\sqrt{x} - 1)(\\sqrt{x} + 1)}{\\sqrt{x} + 1} = \\frac{x - 1}{\\sqrt{x}}$.\nb) Để $P = \\frac{1}{2}$:\n$\\frac{x - 1}{\\sqrt{x}} = \\frac{1}{2} \\Leftrightarrow 2x - 2 = \\sqrt{x} \\Leftrightarrow 2x - \\sqrt{x} - 2 = 0$.\nĐặt $t = \\sqrt{x} > 0$, ta có phương trình bậc hai $2t^2 - t - 2 = 0$.\nTa có $\\Delta = 1 - 4(2)(-2) = 17 > 0$.\nSuy ra nghiệm dương: $t = \\frac{1 + \\sqrt{17}}{4}$.\nDo đó: $x = t^2 = \\left(\\frac{1 + \\sqrt{17}}{4}\\right)^2 = \\frac{18 + 2\\sqrt{17}}{16} = \\frac{9 + \\sqrt{17}}{8}$ (thỏa mãn ĐK).\nVậy $x = \\frac{9 + \\sqrt{17}}{8}$.",
            "rubric": [
                {"step": "Quy đồng và rút gọn đúng P = (x - 1)/sqrt(x)", "subScore": 0.5},
                {"step": "Giải đúng phương trình bậc hai theo t và tìm ra x = (9 + sqrt(17))/8", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình:\n$$\\sqrt{x + 3} + \\sqrt{6 - x} = 3$$",
            "solution": "Điều kiện xác định: $-3 \\le x \\le 6$.\nBình phương hai vế của phương trình:\n$(\\sqrt{x + 3} + \\sqrt{6 - x})^2 = 3^2$\n$\\Leftrightarrow (x + 3) + (6 - x) + 2\\sqrt{(x + 3)(6 - x)} = 9$\n$\\Leftrightarrow 9 + 2\\sqrt{-x^2 + 3x + 18} = 9$\n$\\Leftrightarrow 2\\sqrt{-x^2 + 3x + 18} = 0$\n$\\Leftrightarrow -x^2 + 3x + 18 = 0$\n$\\Leftrightarrow x^2 - 3x - 18 = 0$\n$\\Leftrightarrow (x - 6)(x + 3) = 0$\n$\\Leftrightarrow x = 6$ hoặc $x = -3$.\nCả hai giá trị $x = 6$ và $x = -3$ đều thỏa mãn điều kiện xác định.\nVậy tập nghiệm của phương trình là $S = \\{-3; 6\\}$.",
            "rubric": [
                {"step": "Đặt đúng ĐKXĐ và bình phương hai vế chính xác", "subScore": 0.5},
                {"step": "Giải phương trình tích ra hai nghiệm x = -3, x = 6 và kết luận", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c3_9_bai5_test3"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương III - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho $a \\ge 0$. Biểu thức $\\sqrt{a^2}$ luôn bằng:", "options": ["$a$", "$-a$", "$|a|$", "$\\pm a$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{17 - 12\\sqrt{2}}$ là:", "options": ["$3 - 2\\sqrt{2}$", "$2\\sqrt{2} - 3$", "$3 + 2\\sqrt{2}$", "$\\sqrt{2} - 1$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tính $\\sqrt[3]{-0{,}125}$:", "options": ["$-0{,}5$", "$0{,}5$", "$-0{,}25$", "$0{,}25$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Rút gọn biểu thức $P = \\frac{x - 4}{\\sqrt{x} - 2} - \\frac{x + 2\\sqrt{x}}{\\sqrt{x}}$ với $x > 0, x \\neq 4$:", "options": ["$0$", "$2$", "$-2$", "$\\sqrt{x}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $x = \\sqrt{2} - 1$. Giá trị của biểu thức $(x + 1)^4$ là:", "options": ["$4$", "$2$", "$8$", "$16$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giải phương trình $\\sqrt{x^2 - 6x + 9} = 2x - 1$. Nghiệm là:", "options": ["$x = \\frac{4}{3}$", "$x = 4$", "$x = 2$", "$x = -2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Giá trị của biểu thức $\\frac{1}{\\sqrt{5} + \\sqrt{3}} + \\frac{1}{\\sqrt{5} - \\sqrt{3}}$ là:", "options": ["$\\sqrt{5}$", "$2\\sqrt{5}$", "$\\sqrt{3}$", "$2\\sqrt{3}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = x - 2\\sqrt{x - 1}$ với $x \\ge 1$:", "options": ["$1$", "$0$", "$2$", "$-1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức $B = \\sqrt{x - 2} + \\sqrt{6 - x}$:", "options": ["$2\\sqrt{2}$", "$2$", "$4$", "$\\sqrt{8}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số nghiệm của phương trình $\\sqrt{x - 2} + \\sqrt{y - 3} = \\frac{x + y - 1}{2}$ là:", "options": ["$1$ nghiệm ($x = 3, y = 4$)", "$2$ nghiệm", "$0$ nghiệm", "Vô số"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho biểu thức $P = \\frac{\\sqrt{x} + 2}{\\sqrt{x} + 1}$. Giá trị nguyên lớn nhất của $P$ là:", "options": ["$2$ (tại $x = 0$)", "$1$", "$3$", "Không tồn tại"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tính giá trị của biểu thức $S = \\sqrt[3]{2 + 10\\sqrt{\\frac{1}{27}}} + \\sqrt[3]{2 - 10\\sqrt{\\frac{1}{27}}}$:", "options": ["$2$", "$1$", "$\\sqrt{3}$", "$3$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho biểu thức $P = \\left(\\frac{\\sqrt{x}}{\\sqrt{x} + 3} + \\frac{3}{\\sqrt{x} - 3}\\right) : \\frac{x + 9}{x - 9}$ với $x \\ge 0, x \\neq 9$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Quy đồng mẫu thức trong ngoặc được $\\frac{x + 9}{x - 9}$.", "correct": True},
                {"subId": "b", "text": "Biểu thức rút gọn được thành $P = 1$.", "correct": True},
                {"subId": "c", "text": "Phương trình $P = 2$ vô nghiệm.", "correct": True},
                {"subId": "d", "text": "Khi $x = 16$ thì $P = 16$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức $A = \\sqrt{x + 2\\sqrt{x - 1}} + \\sqrt{x - 2\\sqrt{x - 1}}$ với $x \\ge 1$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Ta có $A = |\\sqrt{x - 1} + 1| + |\\sqrt{x - 1} - 1|$.", "correct": True},
                {"subId": "b", "text": "Khi $1 \\le x \\le 2$ thì $A = 2$.", "correct": True},
                {"subId": "c", "text": "Khi $x > 2$ thì $A = 2\\sqrt{x - 1}$.", "correct": True},
                {"subId": "d", "text": "Giá trị của biểu thức $A$ luôn luôn bằng $2$ với mọi $x \\ge 1$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $(\\sqrt{5} + \\sqrt{2})^2 - 2\\sqrt{10}$.", "correctAnswer": "7", "explanation": "$5 + 2\\sqrt{10} + 2 - 2\\sqrt{10} = 7$."},
        {"id": 2, "level": "Vận dụng", "question": "Tìm $x$ biết $\\sqrt{x - 5} = 3$.", "correctAnswer": "14", "explanation": "$x - 5 = 9 \\Rightarrow x = 14$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = x - 4\\sqrt{x} + 9$ với $x \\ge 0$.", "correctAnswer": "5", "explanation": "$A = (\\sqrt{x} - 2)^2 + 5 \\ge 5$. Dấu bằng khi $x = 4$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính giá trị của $x = \\sqrt[3]{20 + 14\\sqrt{2}} + \\sqrt[3]{20 - 14\\sqrt{2}}$.", "correctAnswer": "4", "explanation": "Lập phương hai vế: $x^3 = 40 + 6x \\Rightarrow x^3 - 6x - 40 = 0 \\Rightarrow x = 4$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho biểu thức $P = \\left(\\frac{x - 2}{x + 2\\sqrt{x}} + \\frac{1}{\\sqrt{x} + 2}\\right) \\cdot \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 1}$ với $x > 0, x \\neq 1$.\na) Rút gọn biểu thức $P$.\nb) Tìm giá trị của $x$ để $P = 2$.",
            "solution": "a) Với $x > 0, x \\neq 1$:\nTa có: $x + 2\\sqrt{x} = \\sqrt{x}(\\sqrt{x} + 2)$.\nQuy đồng mẫu thức trong ngoặc:\n$\\frac{x - 2}{\\sqrt{x}(\\sqrt{x} + 2)} + \\frac{\\sqrt{x}}{\\sqrt{x}(\\sqrt{x} + 2)} = \\frac{x + \\sqrt{x} - 2}{\\sqrt{x}(\\sqrt{x} + 2)}$.\nPhân tích tử thức thành nhân tử:\n$x + \\sqrt{x} - 2 = (\\sqrt{x} - 1)(\\sqrt{x} + 2)$.\nDo đó:\n$\\frac{x + \\sqrt{x} - 2}{\\sqrt{x}(\\sqrt{x} + 2)} = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} + 2)}{\\sqrt{x}(\\sqrt{x} + 2)} = \\frac{\\sqrt{x} - 1}{\\sqrt{x}}$.\nNhân với phân thức thứ hai:\n$P = \\frac{\\sqrt{x} - 1}{\\sqrt{x}} \\cdot \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 1} = \\frac{\\sqrt{x} + 1}{\\sqrt{x}}$.\nb) Để $P = 2$:\n$\\frac{\\sqrt{x} + 1}{\\sqrt{x}} = 2 \\Leftrightarrow \\sqrt{x} + 1 = 2\\sqrt{x} \\Leftrightarrow \\sqrt{x} = 1 \\Leftrightarrow x = 1$.\nĐối chiếu điều kiện: $x = 1$ không thỏa mãn điều kiện $x \\neq 1$.\nVậy không có giá trị nào của $x$ để $P = 2$.",
            "rubric": [
                {"step": "Quy đồng và rút gọn đúng P = (sqrt(x) + 1)/sqrt(x)", "subScore": 0.5},
                {"step": "Giải x = 1, đối chiếu điều kiện và kết luận không có giá trị thỏa mãn", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình:\n$$\\sqrt{x + 1} + \\sqrt{x + 6} = 5$$",
            "solution": "Điều kiện xác định: $x \\ge -1$.\nBình phương hai vế của phương trình:\n$(\\sqrt{x + 1} + \\sqrt{x + 6})^2 = 5^2$\n$\\Leftrightarrow (x + 1) + (x + 6) + 2\\sqrt{(x + 1)(x + 6)} = 25$\n$\\Leftrightarrow 2x + 7 + 2\\sqrt{x^2 + 7x + 6} = 25$\n$\\Leftrightarrow 2\\sqrt{x^2 + 7x + 6} = 18 - 2x$\n$\\Leftrightarrow \\sqrt{x^2 + 7x + 6} = 9 - x$.\nĐiều kiện để phương trình có nghiệm: $9 - x \\ge 0 \\Leftrightarrow x \\le 9$.\nBình phương hai vế:\n$x^2 + 7x + 6 = (9 - x)^2$\n$\\Leftrightarrow x^2 + 7x + 6 = 81 - 18x + x^2$\n$\\Leftrightarrow 7x + 18x = 81 - 6$\n$\\Leftrightarrow 25x = 75$\n$\\Leftrightarrow x = 3$.\nĐối chiếu với điều kiện $-1 \\le x \\le 9$: $x = 3$ thỏa mãn.\nVậy phương trình có nghiệm duy nhất $x = 3$.",
            "rubric": [
                {"step": "Đặt ĐKXĐ x >= -1, bình phương hai vế và rút ra sqrt(x^2 + 7x + 6) = 9 - x", "subScore": 0.5},
                {"step": "Bình phương giải ra x = 3, đối chiếu điều kiện và kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho biểu thức $P = \\frac{2\\sqrt{x}}{\\sqrt{x} + 1}$ với $x \\ge 0$. Tìm tất cả các giá trị của $x$ để biểu thức $P$ nhận giá trị là một số nguyên.",
            "solution": "Với $x \\ge 0$, ta có $\\sqrt{x} \\ge 0$, do đó $P = \\frac{2\\sqrt{x}}{\\sqrt{x} + 1} \\ge 0$.\nMặt khác:\n$P = \\frac{2(\\sqrt{x} + 1) - 2}{\\sqrt{x} + 1} = 2 - \\frac{2}{\\sqrt{x} + 1}$.\nVì $x \\ge 0 \\Rightarrow \\sqrt{x} + 1 \\ge 1 > 0 \\Rightarrow \\frac{2}{\\sqrt{x} + 1} > 0$.\nDo đó $P = 2 - \\frac{2}{\\sqrt{x} + 1} < 2$.\nTừ đó ta có: $0 \\le P < 2$.\nVì $P$ nhận giá trị nguyên nên $P$ chỉ có thể nhận các giá trị $P = 0$ hoặc $P = 1$.\n- Trường hợp 1: $P = 0 \\Leftrightarrow \\frac{2\\sqrt{x}}{\\sqrt{x} + 1} = 0 \\Leftrightarrow \\sqrt{x} = 0 \\Leftrightarrow x = 0$ (thỏa mãn).\n- Trường hợp 2: $P = 1 \\Leftrightarrow \\frac{2\\sqrt{x}}{\\sqrt{x} + 1} = 1 \\Leftrightarrow 2\\sqrt{x} = \\sqrt{x} + 1 \\Leftrightarrow \\sqrt{x} = 1 \\Leftrightarrow x = 1$ (thỏa mãn).\nVậy các giá trị của $x$ để $P$ nhận giá trị nguyên là $x = 0$ và $x = 1$.",
            "rubric": [
                {"step": "Chặn miền giá trị của P: 0 <= P < 2", "subScore": 0.5},
                {"step": "Xét hai trường hợp P = 0, P = 1 và tìm ra đúng hai giá trị x = 0, x = 1", "subScore": 0.5}
            ]
        }
    ]
}
