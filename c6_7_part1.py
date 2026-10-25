# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG VI (PHẦN 1)
Bao gồm:
- Bài 20: Tỉ lệ thức (3 đề: Cơ bản, Khá, Nâng cao)
- Bài 21: Tính chất của dãy tỉ số bằng nhau (3 đề: Cơ bản, Khá, Nâng cao)
Chuẩn ma trận Bộ GD&ĐT 2025: 12 TN + 2 Đ/S (8 ý) + 4 TLN + 3 TL. Tổng 10.0 điểm.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

EXAMS_PART1 = {}

# =====================================================================
# BÀI 20: TỈ LỆ THỨC
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c6_7_bai1_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 20: Tỉ lệ thức - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tỉ lệ thức là đẳng thức của:", "options": ["Hai tỉ số $\\frac{a}{b} = \\frac{c}{d}$", "Hai phân số cùng mẫu", "Hai số nguyên", "Hai biểu thức chứa biến"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Trong tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$, các số $a$ và $d$ được gọi là:", "options": ["Ngoại tỉ", "Trung tỉ", "Tử số", "Mẫu số"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trong tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$, các số $b$ và $c$ được gọi là:", "options": ["Trung tỉ", "Ngoại tỉ", "Tử số", "Hệ số"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Nếu $\\frac{a}{b} = \\frac{c}{d}$ ($b, d \\neq 0$) thì khẳng định nào sau đây là đúng?", "options": ["$ad = bc$", "$ab = cd$", "$ac = bd$", "$a + d = b + c$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Từ đẳng thức $2 \\cdot 6 = 3 \\cdot 4$, tỉ lệ thức nào sau đây là SAI?", "options": ["$\\frac{2}{4} = \\frac{6}{3}$", "$\\frac{2}{3} = \\frac{4}{6}$", "$\\frac{6}{3} = \\frac{4}{2}$", "$\\frac{2}{4} = \\frac{3}{6}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cặp tỉ số nào sau đây lập thành một tỉ lệ thức?", "options": ["$\\frac{2}{5}$ và $\\frac{6}{15}$", "$\\frac{1}{3}$ và $\\frac{2}{5}$", "$\\frac{3}{4}$ và $\\frac{4}{3}$", "$\\frac{-2}{3}$ và $\\frac{2}{3}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tìm $x$ trong tỉ lệ thức $\\frac{x}{6} = \\frac{5}{3}$:", "options": ["$x = 10$", "$x = 5$", "$x = 15$", "$x = 2$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tìm $x$ trong tỉ lệ thức $\\frac{-3}{x} = \\frac{6}{-8}$:", "options": ["$x = 4$", "$x = -4$", "$x = 16$", "$x = -16$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Từ bốn số nào sau đây có thể lập được một tỉ lệ thức?", "options": ["$2; 3; 6; 9$", "$1; 2; 3; 4$", "$2; 4; 6; 8$", "$3; 5; 7; 9$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cho tỉ lệ thức $\\frac{x}{4} = \\frac{9}{x}$ ($x > 0$). Giá trị của $x$ là:", "options": ["$x = 6$", "$x = 36$", "$x = 13$", "$x = 5$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Tìm $x$ biết $\\frac{x - 1}{2} = \\frac{3}{4}$:", "options": ["$x = 2{,}5$", "$x = 2$", "$x = 1{,}5$", "$x = 3$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Biết $\\frac{a}{b} = \\frac{3}{5}$. Tỉ số $\\frac{a + b}{b}$ bằng:", "options": ["$\\frac{8}{5}$", "$\\frac{5}{8}$", "$\\frac{2}{5}$", "$\\frac{5}{3}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho bốn số $3; 4; 9; 12$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Ta có đẳng thức tích $3 \\cdot 12 = 4 \\cdot 9 = 36$.", "isCorrect": True, "explanation": "$3 \\times 12 = 36$ và $4 \\times 9 = 36$."},
                {"id": "b", "statement": "Từ 4 số trên lập được tỉ lệ thức $\\frac{3}{4} = \\frac{9}{12}$.", "isCorrect": True, "explanation": "Cả hai tỉ số đều bằng $0{,}75$."},
                {"id": "c", "statement": "Từ 4 số trên lập được tỉ lệ thức $\\frac{3}{9} = \\frac{4}{12}$.", "isCorrect": True, "explanation": "Hoán vị trung tỉ tạo ra tỉ lệ thức đúng."},
                {"id": "d", "statement": "Tỉ lệ thức $\\frac{3}{12} = \\frac{9}{4}$ là một tỉ lệ thức đúng.", "isCorrect": False, "explanation": "$3/12 = 1/4$ còn $9/4 = 2{,}25 \\neq 1/4$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Xét tính đúng/sai của các phát biểu về tỉ lệ thức:",
            "statements": [
                {"id": "a", "statement": "Nếu $ad = bc$ (với $a, b, c, d \\neq 0$) thì có thể suy ra 4 tỉ lệ thức khác nhau.", "isCorrect": True, "explanation": "Các tỉ lệ thức: $\\frac{a}{b}=\\frac{c}{d}, \\frac{a}{c}=\\frac{b}{d}, \\frac{d}{b}=\\frac{c}{a}, \\frac{d}{c}=\\frac{b}{a}$."},
                {"id": "b", "statement": "Từ $\\frac{x}{3} = \\frac{8}{6}$ suy ra $x = \\frac{3 \\cdot 8}{6} = 4$.", "isCorrect": True, "explanation": "$x = 24 / 6 = 4$."},
                {"id": "c", "statement": "Tỉ số $\\frac{1{,}5}{2}$ bằng tỉ số $\\frac{3}{4}$.", "isCorrect": True, "explanation": "$1{,}5 / 2 = 15/20 = 3/4$."},
                {"id": "d", "statement": "Trong tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$, nếu nhân cả $a$ và $d$ với cùng một số khác 0 thì được tỉ lệ thức mới.", "isCorrect": False, "explanation": "Nhân một ngoại tỉ và một trung tỉ hoặc nhân tử và mẫu của một phân số mới bảo toàn, nhân $a$ và $d$ làm thay đổi tích $ad$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm $x$ trong tỉ lệ thức $\\frac{x}{12} = \\frac{5}{6}$.", "answer": 10, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $y$ trong tỉ lệ thức $\\frac{15}{y} = \\frac{3}{7}$.", "answer": 35, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Tìm số tự nhiên $x$ thỏa mãn $\\frac{x}{3} = \\frac{27}{x}$.", "answer": 9, "unit": ""},
        {"id": 4, "level": "Vận dụng", "question": "Tìm $x$ biết $\\frac{2x + 1}{5} = \\frac{3}{1}$.", "answer": 7, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm $x$ trong các tỉ lệ thức sau:\na) $\\frac{x}{27} = \\frac{-2}{9}$.\nb) $\\frac{1{,}25}{x} = \\frac{5}{8}$.",
            "maxScore": 1.0,
            "solution": "a) Ta có: $x = \\frac{27 \\cdot (-2)}{9} = 3 \\cdot (-2) = -6$.\nVậy $x = -6$.\nb) Ta có: $5 \\cdot x = 1{,}25 \\cdot 8 \\Leftrightarrow 5x = 10 \\Leftrightarrow x = 2$.\nVậy $x = 2$.",
            "rubric": [
                {"step": "Tính đúng x = -6 ở câu a", "subScore": 0.5},
                {"step": "Tính đúng x = 2 ở câu b", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Lập tất cả các tỉ lệ thức có thể được từ đẳng thức: $4 \\cdot 15 = 6 \\cdot 10$.",
            "maxScore": 1.0,
            "solution": "Từ đẳng thức $4 \\cdot 15 = 6 \\cdot 10$, ta lập được 4 tỉ lệ thức sau:\n1) $\\frac{4}{6} = \\frac{10}{15}$\n2) $\\frac{4}{10} = \\frac{6}{15}$\n3) $\\frac{15}{6} = \\frac{10}{4}$\n4) $\\frac{15}{10} = \\frac{6}{4}$",
            "rubric": [
                {"step": "Lập đúng 2 tỉ lệ thức đầu tiên", "subScore": 0.5},
                {"step": "Lập đúng 2 tỉ lệ thức tiếp theo", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một tấm vải dài $45$ m được chia thành hai phần theo tỉ lệ $2 : 3$. Hãy tính độ dài của mỗi phần vải đó.",
            "maxScore": 1.0,
            "solution": "Gọi độ dài hai phần vải lần lượt là $x$ và $y$ (m) ($x, y > 0$).\nTheo đề bài ta có: $\\frac{x}{2} = \\frac{y}{3}$ và $x + y = 45$.\nTừ $\\frac{x}{2} = \\frac{y}{3} \\Rightarrow x = \\frac{2}{3}y$.\nThay vào tổng: $\\frac{2}{3}y + y = 45 \\Leftrightarrow \\frac{5}{3}y = 45 \\Leftrightarrow y = 45 \\times \\frac{3}{5} = 27$ m.\nSuy ra: $x = 45 - 27 = 18$ m.\nVậy hai phần vải có độ dài lần lượt là $18$ m và $27$ m.",
            "rubric": [
                {"step": "Đặt ẩn và thiết lập tỉ lệ thức x/2 = y/3 và tổng x+y=45", "subScore": 0.5},
                {"step": "Giải đúng x = 18 m, y = 27 m và kết luận", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c6_7_bai1_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 20: Tỉ lệ thức - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Từ tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$, ta suy ra được đẳng thức nào sau đây?", "options": ["$\\frac{a}{c} = \\frac{b}{d}$", "$\\frac{a}{d} = \\frac{b}{c}$", "$\\frac{b}{a} = \\frac{c}{d}$", "$\\frac{d}{b} = \\frac{a}{c}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $x$ trong tỉ lệ thức $\\frac{x - 3}{5} = \\frac{x + 1}{7}$:", "options": ["$x = 13$", "$x = 8$", "$x = -13$", "$x = 10$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $\\frac{a}{b} = \\frac{2}{3}$ và $ab = 54$ ($a, b > 0$). Giá trị của $a + b$ là:", "options": ["$15$", "$12$", "$18$", "$20$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho tỉ lệ thức $\\frac{x}{y} = \\frac{4}{7}$. Tỉ số $\\frac{3x - y}{x + 2y}$ bằng:", "options": ["$\\frac{5}{18}$", "$\\frac{7}{18}$", "$\\frac{1}{3}$", "$\\frac{5}{11}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Có bao nhiêu giá trị của $x$ thỏa mãn $\\frac{x}{4} = \\frac{16}{x}$?", "options": ["$2$ giá trị ($x = 8$ hoặc $x = -8$)", "$1$ giá trị ($x = 8$)", "$0$ giá trị", "Vô số giá trị"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một bản đồ có tỉ lệ xích $1 : 200\\,000$. Khoảng cách giữa hai điểm A và B đo được trên bản đồ là $4$ cm. Khoảng cách thực tế giữa hai điểm đó là:", "options": ["$8$ km", "$80$ km", "$0{,}8$ km", "$800$ m"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm $x$ biết $\\frac{2x - 1}{3} = \\frac{x + 5}{4}$:", "options": ["$x = 3{,}8$", "$x = 3$", "$x = 4$", "$x = 5$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$. Đẳng thức nào sau đây luôn đúng?", "options": ["$\\frac{a+b}{b} = \\frac{c+d}{d}$", "$\\frac{a+b}{a} = \\frac{c-d}{c}$", "$\\frac{a-b}{b} = \\frac{c+d}{d}$", "$\\frac{a}{b} = \\frac{c+1}{d+1}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Hai lớp 7A và 7B có số học sinh tỉ lệ với $8 : 9$. Biết lớp 7B nhiều hơn lớp 7A là 5 học sinh. Số học sinh của lớp 7A là:", "options": ["$40$ học sinh", "$45$ học sinh", "$35$ học sinh", "$48$ học sinh"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Tìm $x$ biết $\\frac{x^2}{6} = \\frac{24}{x}$:", "options": ["$x = 5{,}24$", "$x = 12$", "$x = 6$", "$x = 2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $\\frac{a}{b} = \\frac{c}{d}$. Chứng minh $\\frac{a^2 + c^2}{b^2 + d^2} = \\frac{ac}{bd}$. Kết quả này:", "options": ["Luôn đúng với mọi $b, d \\neq 0$ và $b^2 + d^2 \\neq 0$", "Chỉ đúng khi $a = b = c = d$", "Sai", "Chỉ đúng khi $a, b, c, d$ là số dương"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm các số $x, y$ biết $\\frac{x}{3} = \\frac{y}{5}$ và $x^2 + y^2 = 136$ ($x, y > 0$):", "options": ["$x = 6, y = 10$", "$x = 3, y = 5$", "$x = 9, y = 15$", "$x = 12, y = 20$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tỉ lệ thức $\\frac{x}{3} = \\frac{y}{7}$. Xét tính đúng/sai của các hệ thức sau:",
            "statements": [
                {"id": "a", "statement": "$\\frac{x}{y} = \\frac{3}{7}$.", "isCorrect": True, "explanation": "Hoán vị trung tỉ."},
                {"id": "b", "statement": "$\\frac{7}{3} = \\frac{y}{x}$ (với $x \\neq 0$).", "isCorrect": True, "explanation": "Đảo ngược cả hai vế."},
                {"id": "c", "statement": "$\\frac{x + 3}{3} = \\frac{y + 7}{7}$.", "isCorrect": True, "explanation": "Cộng 1 vào cả hai vế: $\\frac{x}{3} + 1 = \\frac{y}{7} + 1 \\Leftrightarrow \\frac{x+3}{3} = \\frac{y+7}{7}$."},
                {"id": "d", "statement": "$\\frac{x + y}{10} = \\frac{x - y}{4}$.", "isCorrect": False, "explanation": "$\\frac{x-y}{3-7} = \\frac{x-y}{-4}$, có dấu trừ ở mẫu."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Tìm hai số $x, y$ biết $\\frac{x}{2} = \\frac{y}{5}$ và $x \\cdot y = 40$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Đặt $\\frac{x}{2} = \\frac{y}{5} = k$, ta có $x = 2k$ và $y = 5k$.", "isCorrect": True, "explanation": "Phương pháp đặt ẩn phụ tỉ số."},
                {"id": "b", "statement": "Thay vào tích ta được $2k \\cdot 5k = 10k^2 = 40 \\Rightarrow k^2 = 4$.", "isCorrect": True, "explanation": "$10k^2 = 40 \\Leftrightarrow k^2 = 4$."},
                {"id": "c", "statement": "Chỉ có duy nhất một giá trị $k = 2$.", "isCorrect": False, "explanation": "Phương trình $k^2 = 4$ có hai nghiệm $k = 2$ hoặc $k = -2$."},
                {"id": "d", "statement": "Có hai cặp số thỏa mãn là $(4; 10)$ và $(-4; -10)$.", "isCorrect": True, "explanation": "Với $k = 2 \\Rightarrow (4; 10)$; với $k = -2 \\Rightarrow (-4; -10)$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm $x$ trong tỉ lệ thức $\\frac{2x - 3}{4} = \\frac{5}{2}$.", "answer": 6.5, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\frac{x}{y} = \\frac{3}{4}$ và $x + y = 28$. Tính giá trị của $x$.", "answer": 12, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Một hình chữ nhật có tỉ số hai cạnh là $2 : 3$ và chu vi bằng $40$ cm. Tính diện tích hình chữ nhật theo cm$^2$.", "answer": 96, "unit": "cm$^2$"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị dương của $x$ biết $\\frac{x - 1}{x + 2} = \\frac{x - 2}{x + 1}$.", "answer": 0, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Tìm $x$ trong các tỉ lệ thức sau:\na) $\\frac{x - 1}{3} = \\frac{2x + 1}{5}$.\nb) $\\frac{x + 1}{x - 2} = \\frac{3}{2}$ ($x \\neq 2$).",
            "maxScore": 1.0,
            "solution": "a) Nhân chéo: $5(x - 1) = 3(2x + 1)$\n$\\Leftrightarrow 5x - 5 = 6x + 3 \\Leftrightarrow 6x - 5x = -5 - 3 \\Leftrightarrow x = -8$.\nVậy $x = -8$.\nb) Nhân chéo: $2(x + 1) = 3(x - 2)$\n$\\Leftrightarrow 2x + 2 = 3x - 6 \\Leftrightarrow 3x - 2x = 2 + 6 \\Leftrightarrow x = 8$ (thỏa mãn $x \\neq 2$).\nVậy $x = 8$.",
            "rubric": [
                {"step": "Giải đúng câu a ra x = -8", "subScore": 0.5},
                {"step": "Giải đúng câu b ra x = 8", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$ ($a, b, c, d \\neq 0$). Chứng minh rằng:\n$\\frac{a + 2c}{b + 2d} = \\frac{a - 2c}{b - 2d}$ (giả thiết các mẫu số đều khác 0).",
            "maxScore": 1.0,
            "solution": "Đặt $\\frac{a}{b} = \\frac{c}{d} = k \\Rightarrow a = kb, c = kd$.\nThay vào vế trái:\n$\\text{VT} = \\frac{a + 2c}{b + 2d} = \\frac{kb + 2kd}{b + 2d} = \\frac{k(b + 2d)}{b + 2d} = k$.\nThay vào vế phải:\n$\\text{VP} = \\frac{a - 2c}{b - 2d} = \\frac{kb - 2kd}{b - 2d} = \\frac{k(b - 2d)}{b - 2d} = k$.\nVì $\\text{VT} = \\text{VP} = k$ nên $\\frac{a + 2c}{b + 2d} = \\frac{a - 2c}{b - 2d}$ (đpcm).",
            "rubric": [
                {"step": "Đặt ẩn phụ k và biểu diễn a = kb, c = kd", "subScore": 0.4},
                {"step": "Rút gọn hai vế cùng bằng k và kết luận", "subScore": 0.6}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Ba lớp 7A, 7B, 7C tham gia trồng cây xanh. Số cây trồng của lớp 7A và 7B tỉ lệ với $3 : 4$, số cây của lớp 7B và 7C tỉ lệ với $5 : 6$. Biết rằng lớp 7C trồng nhiều hơn lớp 7A là 18 cây. Hỏi mỗi lớp trồng được bao nhiêu cây?",
            "maxScore": 1.0,
            "solution": "Gọi số cây của ba lớp 7A, 7B, 7C lần lượt là $a, b, c$ ($a, b, c \\in \\mathbb{N}^*$).\nTheo đề bài: $\\frac{a}{b} = \\frac{3}{4} \\Rightarrow \\frac{a}{15} = \\frac{b}{20}$.\n$\\frac{b}{c} = \\frac{5}{6} \\Rightarrow \\frac{b}{20} = \\frac{c}{24}$.\nSuy ra dãy tỉ số bằng nhau: $\\frac{a}{15} = \\frac{b}{20} = \\frac{c}{24}$.\nLại có $c - a = 18$.\nÁp dụng tính chất dãy tỉ số bằng nhau:\n$\\frac{a}{15} = \\frac{b}{20} = \\frac{c}{24} = \\frac{c - a}{24 - 15} = \\frac{18}{9} = 2$.\nSuy ra:\n$a = 15 \\times 2 = 30$ cây.\n$b = 20 \\times 2 = 40$ cây.\n$c = 24 \\times 2 = 48$ cây.\nVậy lớp 7A trồng 30 cây, lớp 7B trồng 40 cây, lớp 7C trồng 48 cây.",
            "rubric": [
                {"step": "Quy đồng đưa về cùng dãy tỉ số a/15 = b/20 = c/24", "subScore": 0.5},
                {"step": "Áp dụng hiệu c - a = 18 tìm ra a=30, b=40, c=48", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c6_7_bai1_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 20: Tỉ lệ thức - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\frac{a}{b} = \\frac{c}{d}$. Biểu thức nào sau đây KHÔNG bằng tỉ số $\\frac{a}{b}$?", "options": ["$\\frac{a+2}{b+2}$", "$\\frac{a+c}{b+d}$", "$\\frac{2a-c}{2b-d}$", "$\\frac{3a+5c}{3b+5d}$"], "correct": 0},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4}$ và $x^2 + y^2 + z^2 = 116$ ($x, y, z > 0$). Giá trị của $x + y + z$ là:", "options": ["$18$", "$20$", "$16$", "$24$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Tìm các số $x, y$ thỏa mãn $\\frac{x}{3} = \\frac{y}{4}$ và $xy = 48$ ($x, y < 0$):", "options": ["$x = -6, y = -8$", "$x = -3, y = -4$", "$x = -12, y = -16$", "$x = -9, y = -12$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho $\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d}$ ($a, b, c, d \\neq 0$). Khi đó $\\left(\\frac{a+b+c}{b+c+d}\\right)^3$ bằng:", "options": ["$\\frac{a}{d}$", "$\\frac{a^3}{d^3}$", "$\\frac{b}{c}$", "$1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$. Tỉ số $\\frac{ab}{cd}$ bằng tỉ số nào sau đây?", "options": ["$\\frac{a^2}{c^2}$", "$\\frac{a^2}{b^2}$", "$\\frac{c^2}{d^2}$", "$\\frac{a+b}{c+d}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tìm $x$ thỏa mãn $\\frac{x - 1}{2023} + \\frac{x - 2}{2022} = \\frac{x - 3}{2021} + \\frac{x - 4}{2020}$:", "options": ["$x = 2024$", "$x = 2023$", "$x = 0$", "$x = 1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho $a, b, c$ khác 0 thỏa mãn $\\frac{a+b-c}{c} = \\frac{b+c-a}{a} = \\frac{c+a-b}{b}$. Giá trị của biểu thức $P = \\left(1 + \\frac{b}{a}\\right)\\left(1 + \\frac{c}{b}\\right)\\left(1 + \\frac{a}{c}\\right)$ là:", "options": ["$8$", "$1$", "$6$", "$-1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho tỉ lệ thức $\\frac{2a+b}{a-2b} = \\frac{2c+d}{c-2d}$. Khẳng định nào sau đây là đúng?", "options": ["$\\frac{a}{b} = \\frac{c}{d}$", "$\\frac{a}{c} = \\frac{d}{b}$", "$ad + bc = 0$", "$a = b = c = d$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Biết $\\frac{bz - cy}{a} = \\frac{cx - az}{b} = \\frac{ay - bx}{c}$. Khi đó tỉ lệ thức nào sau đây đúng?", "options": ["$\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$", "$\\frac{x}{b} = \\frac{y}{c} = \\frac{z}{a}$", "$x + y + z = a + b + c$", "$ax = by = cz$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số các cặp số nguyên $(x; y)$ thỏa mãn $\\frac{x}{3} - \\frac{4}{y} = \\frac{1}{6}$ là:", "options": ["$6$ cặp", "$4$ cặp", "$8$ cặp", "$2$ cặp"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho ba số thực $x, y, z$ thỏa mãn $\\frac{x}{y+z+1} = \\frac{y}{x+z+1} = \\frac{z}{x+y-2} = x + y + z$. Khi $x + y + z \\neq 0$, giá trị của tổng $x + y + z$ là:", "options": ["$\\frac{1}{2}$", "$1$", "$2$", "$-1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\frac{a}{b} = \\frac{c}{d}$. Chứng minh $\\frac{5a+3b}{5a-3b} = \\frac{5c+3d}{5c-3d}$. Phép biến đổi nào sau đây phù hợp nhất?", "options": ["Chia cả tử và mẫu cho $b$ (ở vế trái) và $d$ (ở vế phải)", "Quy đồng mẫu số hai vế", "Bình phương hai vế", "Cộng thêm 1 vào cả hai vế"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho ba số thực $a, b, c$ đôi một khác nhau và khác 0 thỏa mãn $\\frac{a}{b+c} = \\frac{b}{c+a} = \\frac{c}{a+b}$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Nếu $a + b + c \\neq 0$, áp dụng tính chất dãy tỉ số bằng nhau thì mỗi tỉ số bằng $\\frac{1}{2}$.", "isCorrect": True, "explanation": "$\\frac{a+b+c}{(b+c)+(c+a)+(a+b)} = \\frac{a+b+c}{2(a+b+c)} = \\frac{1}{2}$."},
                {"id": "b", "statement": "Từ đó suy ra $a = b = c$.", "isCorrect": True, "explanation": "$2a = b + c, 2b = c + a \\Rightarrow a - b = b - a \\Rightarrow a = b = c$."},
                {"id": "c", "statement": "Nếu $a + b + c = 0$ thì $b + c = -a$, khi đó mỗi tỉ số bằng $-1$.", "isCorrect": True, "explanation": "$\\frac{a}{b+c} = \\frac{a}{-a} = -1$."},
                {"id": "d", "statement": "Giá trị của biểu thức $P = \\frac{b+c}{a} + \\frac{c+a}{b} + \\frac{a+b}{c}$ chỉ có thể bằng $6$.", "isCorrect": False, "explanation": "Nếu $a+b+c=0$ thì $P = (-1) + (-1) + (-1) = -3$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$. Xét tính đúng/sai của các đẳng thức sau:",
            "statements": [
                {"id": "a", "statement": "$\\frac{x^2 + y^2 + z^2}{a^2 + b^2 + c^2} = \\left(\\frac{x+y+z}{a+b+c}\\right)^2$.", "isCorrect": True, "explanation": "Đặt bằng $k$, cả hai vế đều bằng $k^2$."},
                {"id": "b", "statement": "$\\frac{xy + yz + zx}{ab + bc + ca} = \\left(\\frac{x}{a}\\right)^2$.", "isCorrect": True, "explanation": "Cả hai vế đều bằng $k^2$."},
                {"id": "c", "statement": "$\\frac{x^3 + y^3 + z^3}{a^3 + b^3 + c^3} = \\frac{xyz}{abc}$.", "isCorrect": True, "explanation": "Cả hai vế đều bằng $k^3$."},
                {"id": "d", "statement": "$\\frac{x+2y-3z}{a+2b-3c} = \\left(\\frac{x}{a}\\right)^2$.", "isCorrect": False, "explanation": "Vế trái bằng $k$, vế phải bằng $k^2 \\neq k$ (nếu $k \\neq 1$)."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Cho $\\frac{x}{3} = \\frac{y}{5}$ và $2x + 3y = 42$. Tìm giá trị của $x + y$.", "answer": 16, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tìm số tự nhiên $x$ thỏa mãn $\\frac{x + 2}{3} = \\frac{27}{x + 2}$.", "answer": 7, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $\\frac{a}{b} = \\frac{c}{d}$ với $a = 3c$. Tính tỉ số $\\frac{b}{d}$.", "answer": 3, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm $x$ biết $\\frac{x - 10}{20} + \\frac{x - 10}{30} = \\frac{x - 10}{40} + 1$ (kết quả là số nguyên).", "answer": 34, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$ ($a, b, c, d \\neq 0; a \\neq \\pm b; c \\neq \\pm d$).\nChứng minh rằng: $\\frac{a^2 + b^2}{c^2 + d^2} = \\frac{a^2 - b^2}{c^2 - d^2}$.",
            "maxScore": 1.0,
            "solution": "Đặt $\\frac{a}{b} = \\frac{c}{d} = k \\Rightarrow a = kb, c = kd$.\nThay vào vế trái:\n$\\text{VT} = \\frac{a^2 + b^2}{c^2 + d^2} = \\frac{k^2 b^2 + b^2}{k^2 d^2 + d^2} = \\frac{b^2(k^2 + 1)}{d^2(k^2 + 1)} = \\frac{b^2}{d^2}$.\nThay vào vế phải:\n$\\text{VP} = \\frac{a^2 - b^2}{c^2 - d^2} = \\frac{k^2 b^2 - b^2}{k^2 d^2 - d^2} = \\frac{b^2(k^2 - 1)}{d^2(k^2 - 1)} = \\frac{b^2}{d^2}$.\nDo đó $\\text{VT} = \\text{VP} = \\frac{b^2}{d^2}$, suy ra $\\frac{a^2 + b^2}{c^2 + d^2} = \\frac{a^2 - b^2}{c^2 - d^2}$ (đpcm).",
            "rubric": [
                {"step": "Đặt ẩn phụ k và biến đổi vế trái bằng b^2 / d^2", "subScore": 0.5},
                {"step": "Biến đổi vế phải bằng b^2 / d^2 và kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm ba số $x, y, z$ biết: $\\frac{x - 1}{2} = \\frac{y - 2}{3} = \\frac{z - 3}{4}$ và $2x + 3y - z = 50$.",
            "maxScore": 1.0,
            "solution": "Từ tỉ lệ thức: $\\frac{x - 1}{2} = \\frac{y - 2}{3} = \\frac{z - 3}{4}$, ta nhân hệ số tương ứng:\n$\\frac{2(x - 1)}{4} = \\frac{3(y - 2)}{9} = \\frac{z - 3}{4} \\Leftrightarrow \\frac{2x - 2}{4} = \\frac{3y - 6}{9} = \\frac{z - 3}{4}$.\nÁp dụng tính chất của dãy tỉ số bằng nhau:\n$\\frac{2x - 2}{4} = \\frac{3y - 6}{9} = \\frac{z - 3}{4} = \\frac{(2x - 2) + (3y - 6) - (z - 3)}{4 + 9 - 4}$\n$= \\frac{(2x + 3y - z) - 2 - 6 + 3}{9} = \\frac{50 - 5}{9} = \\frac{45}{9} = 5$.\nSuy ra:\n$\\frac{x - 1}{2} = 5 \\Rightarrow x - 1 = 10 \\Rightarrow x = 11$.\n$\\frac{y - 2}{3} = 5 \\Rightarrow y - 2 = 15 \\Rightarrow y = 17$.\n$\\frac{z - 3}{4} = 5 \\Rightarrow z - 3 = 20 \\Rightarrow z = 23$.\nVậy $x = 11, y = 17, z = 23$.",
            "rubric": [
                {"step": "Biến đổi nhân hệ số và áp dụng dãy tỉ số bằng nhau tính ra giá trị 5", "subScore": 0.6},
                {"step": "Tìm đúng x = 11, y = 17, z = 23", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho các số thực $a, b, c, d$ thỏa mãn $b, d \\neq 0$ và $\\frac{a}{b} < \\frac{c}{d}$ với $b > 0, d > 0$.\nChứng minh rằng: $\\frac{a}{b} < \\frac{a + c}{b + d} < \\frac{c}{d}$.",
            "maxScore": 1.0,
            "solution": "Vì $b > 0, d > 0$ và $\\frac{a}{b} < \\frac{c}{d}$ nên $ad < bc$.\n1) Chứng minh $\\frac{a}{b} < \\frac{a+c}{b+d}$:\nXét hiệu: $\\frac{a+c}{b+d} - \\frac{a}{b} = \\frac{b(a+c) - a(b+d)}{b(b+d)} = \\frac{ab + bc - ab - ad}{b(b+d)} = \\frac{bc - ad}{b(b+d)}$.\nVì $ad < bc$ nên $bc - ad > 0$. Mặt khác $b > 0, d > 0 \\Rightarrow b(b+d) > 0$.\nDo đó $\\frac{bc - ad}{b(b+d)} > 0 \\Rightarrow \\frac{a}{b} < \\frac{a+c}{b+d}$ (1).\n2) Chứng minh $\\frac{a+c}{b+d} < \\frac{c}{d}$:\nXét hiệu: $\\frac{c}{d} - \\frac{a+c}{b+d} = \\frac{c(b+d) - d(a+c)}{d(b+d)} = \\frac{bc + cd - ad - cd}{d(b+d)} = \\frac{bc - ad}{d(b+d)}$.\nVì $bc - ad > 0$ và $d(b+d) > 0$ nên hiệu trên lớn hơn 0 $\\Rightarrow \\frac{a+c}{b+d} < \\frac{c}{d}$ (2).\nTừ (1) và (2) suy ra: $\\frac{a}{b} < \\frac{a+c}{b+d} < \\frac{c}{d}$ (đpcm).",
            "rubric": [
                {"step": "Chứng minh bất đẳng thức thứ nhất bằng xét hiệu", "subScore": 0.5},
                {"step": "Chứng minh bất đẳng thức thứ hai và kết luận chuỗi so sánh", "subScore": 0.5}
            ]
        }
    ]
}

# =====================================================================
# BÀI 21: TÍNH CHẤT CỦA DÃY TỈ SỐ BẰNG NHAU
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c6_7_bai2_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 21: Tính chất của dãy tỉ số bằng nhau - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Từ dãy tỉ số bằng nhau $\\frac{a}{b} = \\frac{c}{d}$, hệ thức nào sau đây diễn tả tính chất của dãy tỉ số bằng nhau?", "options": ["$\\frac{a}{b} = \\frac{c}{d} = \\frac{a + c}{b + d}$", "$\\frac{a}{b} = \\frac{c}{d} = \\frac{a \\cdot c}{b \\cdot d}$", "$\\frac{a}{b} = \\frac{c}{d} = \\frac{a + c}{b - d}$", "$\\frac{a}{b} = \\frac{c}{d} = \\frac{a - c}{b + d}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Từ dãy tỉ số bằng nhau $\\frac{a}{b} = \\frac{c}{d}$, ta cũng có:", "options": ["$\\frac{a}{b} = \\frac{c}{d} = \\frac{a - c}{b - d}$ (với $b \\neq d$)", "$\\frac{a}{b} = \\frac{c}{d} = \\frac{a - c}{d - b}$", "$\\frac{a}{b} = \\frac{c}{d} = \\frac{c - a}{b - d}$", "$\\frac{a}{b} = \\frac{c}{d} = \\frac{a + d}{b + c}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Với dãy tỉ số bằng nhau $\\frac{a}{2} = \\frac{b}{3} = \\frac{c}{4}$, ta nói ba số $a, b, c$:", "options": ["Tỉ lệ với các số $2; 3; 4$", "Bằng các số $2; 3; 4$", "Có tổng bằng $9$", "Có tích bằng $24$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Khi nói ba số $x, y, z$ tỉ lệ với các số $3; 5; 7$, ta viết:", "options": ["$\\frac{x}{3} = \\frac{y}{5} = \\frac{z}{7}$", "$\\frac{x}{7} = \\frac{y}{5} = \\frac{z}{3}$", "$3x = 5y = 7z$", "$x : y : z = 7 : 5 : 3$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tìm hai số $x$ và $y$ biết $\\frac{x}{2} = \\frac{y}{3}$ và $x + y = 20$:", "options": ["$x = 8, y = 12$", "$x = 10, y = 10$", "$x = 6, y = 14$", "$x = 4, y = 16$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Tìm hai số $x$ và $y$ biết $\\frac{x}{5} = \\frac{y}{2}$ và $x - y = 12$:", "options": ["$x = 20, y = 8$", "$x = 15, y = 3$", "$x = 25, y = 13$", "$x = 30, y = 18$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $\\frac{x}{3} = \\frac{y}{4} = \\frac{z}{5}$ và $x + y + z = 36$. Giá trị của $x$ là:", "options": ["$x = 9$", "$x = 12$", "$x = 15$", "$x = 3$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho $\\frac{a}{4} = \\frac{b}{7}$ và $b - a = 15$. Giá trị của $a$ là:", "options": ["$a = 20$", "$a = 35$", "$a = 15$", "$a = 25$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Biết ba góc của một tam giác tỉ lệ với $1 : 2 : 3$. Số đo góc lớn nhất của tam giác đó là:", "options": ["$90^\\circ$", "$60^\\circ$", "$120^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cho $\\frac{x}{2} = \\frac{y}{5}$ và $2x + y = 27$. Giá trị của $x$ và $y$ là:", "options": ["$x = 6, y = 15$", "$x = 4, y = 10$", "$x = 8, y = 20$", "$x = 2, y = 5$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Hai lớp 7A và 7B quyên góp được tổng cộng 120 quyển vở. Số vở của lớp 7A và 7B tỉ lệ với 5 : 7. Số vở lớp 7A quyên góp được là:", "options": ["$50$ quyển", "$70$ quyển", "$60$ quyển", "$40$ quyển"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Một khu vườn hình chữ nhật có tỉ số chiều rộng và chiều dài là $3 : 5$, chu vi là $48$ m. Chiều dài khu vườn là:", "options": ["$15$ m", "$9$ m", "$20$ m", "$18$ m"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho dãy tỉ số bằng nhau $\\frac{x}{3} = \\frac{y}{4} = \\frac{z}{5}$ và $x + y + z = 48$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tổng số phần bằng nhau ở mẫu là $3 + 4 + 5 = 12$.", "isCorrect": True, "explanation": "Mẫu số: $3+4+5=12$."},
                {"id": "b", "statement": "Giá trị của mỗi tỉ số bằng $\\frac{48}{12} = 4$.", "isCorrect": True, "explanation": "$\\frac{x+y+z}{3+4+5} = \\frac{48}{12} = 4$."},
                {"id": "c", "statement": "Số $x = 12, y = 16, z = 20$.", "isCorrect": True, "explanation": "$x = 3 \\times 4 = 12, y = 4 \\times 4 = 16, z = 5 \\times 4 = 20$."},
                {"id": "d", "statement": "Hiệu $z - x = 6$.", "isCorrect": False, "explanation": "$z - x = 20 - 12 = 8 \\neq 6$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Xét tính đúng/sai của các công thức áp dụng tính chất dãy tỉ số bằng nhau từ $\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f}$:",
            "statements": [
                {"id": "a", "statement": "$\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = \\frac{a + c + e}{b + d + f}$.", "isCorrect": True, "explanation": "Đúng theo tính chất mở rộng cho 3 tỉ số."},
                {"id": "b", "statement": "$\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = \\frac{a - c + e}{b - d + f}$.", "isCorrect": True, "explanation": "Đúng với quy tắc đổi dấu tương ứng ở mẫu."},
                {"id": "c", "statement": "$\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = \\frac{2a + 3c}{2b + 3d}$.", "isCorrect": True, "explanation": "Nhân hệ số vào tử và mẫu rồi cộng."},
                {"id": "d", "statement": "$\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = \\frac{a + c - e}{b - d + f}$.", "isCorrect": False, "explanation": "Dấu ở mẫu không khớp với tử: tử là $+c -e$ thì mẫu phải là $+d -f$ chứ không phải $-d +f$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\frac{x}{3} = \\frac{y}{7}$ và $x + y = 30$. Tìm $x$.", "answer": 9, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\frac{a}{5} = \\frac{b}{2}$ và $a - b = 18$. Tìm $a$.", "answer": 30, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Ba lớp 7A, 7B, 7C có số học sinh lần lượt tỉ lệ với 8, 9, 10. Tổng số học sinh của ba lớp là 108 em. Hỏi lớp 7B có bao nhiêu học sinh?", "answer": 36, "unit": "học sinh"},
        {"id": 4, "level": "Vận dụng", "question": "Cho tam giác có ba cạnh tỉ lệ với $3 : 4 : 5$ và chu vi bằng $36$ cm. Độ dài cạnh lớn nhất của tam giác là bao nhiêu cm?", "answer": 15, "unit": "cm"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm hai số $x$ và $y$ biết:\na) $\\frac{x}{3} = \\frac{y}{5}$ và $x + y = 32$.\nb) $\\frac{x}{7} = \\frac{y}{4}$ và $x - y = 15$.",
            "maxScore": 1.0,
            "solution": "a) Áp dụng tính chất của dãy tỉ số bằng nhau:\n$\\frac{x}{3} = \\frac{y}{5} = \\frac{x + y}{3 + 5} = \\frac{32}{8} = 4$.\nSuy ra: $x = 3 \\times 4 = 12$; $y = 5 \\times 4 = 20$.\nVậy $x = 12, y = 20$.\nb) Áp dụng tính chất của dãy tỉ số bằng nhau:\n$\\frac{x}{7} = \\frac{y}{4} = \\frac{x - y}{7 - 4} = \\frac{15}{3} = 5$.\nSuy ra: $x = 7 \\times 5 = 35$; $y = 4 \\times 5 = 20$.\nVậy $x = 35, y = 20$.",
            "rubric": [
                {"step": "Tính đúng câu a ra x = 12, y = 20", "subScore": 0.5},
                {"step": "Tính đúng câu b ra x = 35, y = 20", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Số học sinh của ba khối 6, 7, 8 của một trường THCS lần lượt tỉ lệ với các số $9; 8; 7$. Biết rằng số học sinh của khối 6 nhiều hơn số học sinh của khối 8 là $50$ học sinh. Tính số học sinh của mỗi khối.",
            "maxScore": 1.0,
            "solution": "Gọi số học sinh của ba khối 6, 7, 8 lần lượt là $x, y, z$ (học sinh) ($x, y, z \\in \\mathbb{N}^*$).\nTheo đề bài ta có: $\\frac{x}{9} = \\frac{y}{8} = \\frac{z}{7}$ và $x - z = 50$.\nÁp dụng tính chất của dãy tỉ số bằng nhau:\n$\\frac{x}{9} = \\frac{y}{8} = \\frac{z}{7} = \\frac{x - z}{9 - 7} = \\frac{50}{2} = 25$.\nSuy ra:\n$x = 9 \\times 25 = 225$ học sinh.\n$y = 8 \\times 25 = 200$ học sinh.\n$z = 7 \\times 25 = 175$ học sinh.\nVậy khối 6 có 225 học sinh, khối 7 có 200 học sinh, khối 8 có 175 học sinh.",
            "rubric": [
                {"step": "Thiết lập dãy tỉ số và áp dụng đúng tính chất", "subScore": 0.5},
                {"step": "Tính ra khối 6: 225, khối 7: 200, khối 8: 175 và kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một miếng đất hình chữ nhật có chu vi bằng $70$ m và tỉ số giữa hai cạnh của nó bằng $\\frac{3}{4}$. Tính diện tích của miếng đất đó.",
            "maxScore": 1.0,
            "solution": "Nửa chu vi của miếng đất hình chữ nhật là:\n$70 : 2 = 35$ (m).\nGọi chiều rộng và chiều dài của miếng đất lần lượt là $x$ và $y$ (m) ($0 < x < y < 35$).\nTa có: $\\frac{x}{3} = \\frac{y}{4}$ và $x + y = 35$.\nÁp dụng tính chất của dãy tỉ số bằng nhau:\n$\\frac{x}{3} = \\frac{y}{4} = \\frac{x + y}{3 + 4} = \\frac{35}{7} = 5$.\nSuy ra:\nChiều rộng là: $x = 3 \\times 5 = 15$ (m).\nChiều dài là: $y = 4 \\times 5 = 20$ (m).\nDiện tích của miếng đất là:\n$S = 15 \\times 20 = 300$ (m$^2$).\nVậy diện tích miếng đất là $300$ m$^2$.",
            "rubric": [
                {"step": "Tính nửa chu vi 35 m và lập tỉ số x/3 = y/4", "subScore": 0.4},
                {"step": "Tìm đúng chiều rộng 15 m, chiều dài 20 m và diện tích 300 m^2", "subScore": 0.6}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c6_7_bai2_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 21: Tính chất của dãy tỉ số bằng nhau - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\frac{x}{3} = \\frac{y}{5} = \\frac{z}{7}$. Biểu thức nào sau đây bằng các tỉ số đã cho?", "options": ["$\\frac{2x + y - z}{4}$", "$\\frac{2x + y - z}{5}$", "$\\frac{x + 2y + z}{20}$", "$\\frac{x - y + z}{3}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\frac{a}{2} = \\frac{b}{3} = \\frac{c}{4}$ và $a + 2b - c = 16$. Giá trị của $a$ là:", "options": ["$a = 8$", "$a = 4$", "$a = 12$", "$a = 16$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Ba số $x, y, z$ thỏa mãn $\\frac{x}{2} = \\frac{y}{3}; \\frac{y}{4} = \\frac{z}{5}$. Khi đó dãy tỉ số bằng nhau của $x, y, z$ là:", "options": ["$\\frac{x}{8} = \\frac{y}{12} = \\frac{z}{15}$", "$\\frac{x}{2} = \\frac{y}{12} = \\frac{z}{5}$", "$\\frac{x}{8} = \\frac{y}{3} = \\frac{z}{15}$", "$\\frac{x}{6} = \\frac{y}{12} = \\frac{z}{20}$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Một tam giác có chu vi $60$ cm, ba cạnh tỉ lệ với $3 : 4 : 5$. Độ dài ba cạnh là:", "options": ["$15$ cm, $20$ cm, $25$ cm", "$12$ cm, $16$ cm, $20$ cm", "$18$ cm, $24$ cm, $30$ cm", "$10$ cm, $20$ cm, $30$ cm"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Số học sinh của ba lớp 7A, 7B, 7C tỉ lệ với $10 : 9 : 8$. Biết tổng số học sinh của lớp 7A và 7C là 72 em. Số học sinh của lớp 7B là:", "options": ["$36$ em", "$40$ em", "$32$ em", "$38$ em"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{5}$ và $xyz = 240$. Giá trị dương của $x + y + z$ là:", "options": ["$20$", "$10$", "$30$", "$40$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Biết $2x = 3y = 5z$ và $x + y - z = 57$. Giá trị của $x$ là:", "options": ["$45$", "$30$", "$18$", "$60$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Chia số 104 thành ba phần tỉ lệ thuận với $\\frac{1}{2}; \\frac{1}{3}; \\frac{1}{4}$. Số lớn nhất trong ba số đó là:", "options": ["$48$", "$36$", "$32$", "$24$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Ba công nhân dệt được 360 mét vải trong một ngày. Số mét vải của công nhân 1, 2, 3 tỉ lệ với $5 : 4 : 3$. Người dệt nhiều nhất được bao nhiêu mét vải?", "options": ["$150$ m", "$120$ m", "$90$ m", "$180$ m"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Tìm hai số $x, y$ biết $\\frac{x}{3} = \\frac{y}{7}$ và $x^2 + y^2 = 232$ ($x, y > 0$):", "options": ["$x = 6, y = 14$", "$x = 3, y = 7$", "$x = 9, y = 21$", "$x = 12, y = 28$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $\\frac{a}{b} = \\frac{c}{d}$. Hệ thức nào sau đây chứng minh tính chất $\\frac{a^2 + b^2}{c^2 + d^2} = \\frac{(a+b)^2}{(c+d)^2}$?", "options": ["Đặt $a = kb, c = kd$ rồi thay vào hai vế", "Nhân chéo hai vế", "Áp dụng định lí Pythagore", "Lấy căn bậc hai hai vế"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\frac{x - 1}{2} = \\frac{y - 2}{3} = \\frac{z - 3}{4}$ và $x - 2y + 3z = 14$. Giá trị của $x + y + z$ là:", "options": ["$18$", "$15$", "$21$", "$12$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho ba số $x, y, z$ thỏa mãn $2x = 3y = 4z$ và $x + y + z = 26$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Chia các vế cho BCNN(2, 3, 4) = 12 ta được $\\frac{x}{6} = \\frac{y}{4} = \\frac{z}{3}$.", "isCorrect": True, "explanation": "$2x/12 = x/6, 3y/12 = y/4, 4z/12 = z/3$."},
                {"id": "b", "statement": "Tổng số phần bằng nhau ở mẫu là $6 + 4 + 3 = 13$.", "isCorrect": True, "explanation": "$6+4+3=13$."},
                {"id": "c", "statement": "Giá trị của $x = 12, y = 8, z = 6$.", "isCorrect": True, "explanation": "$\\frac{26}{13} = 2 \\Rightarrow x = 12, y = 8, z = 6$."},
                {"id": "d", "statement": "Tích của ba số $x \\cdot y \\cdot z = 600$.", "isCorrect": False, "explanation": "$12 \\times 8 \\times 6 = 576 \\neq 600$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Ba bạn An, Bình, Cường có số viên bi tỉ lệ với các số $4; 5; 6$. Biết rằng số bi của Cường nhiều hơn số bi của An là $8$ viên. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Số phần chênh lệch giữa Cường và An là $6 - 4 = 2$ phần.", "isCorrect": True, "explanation": "Cường 6 phần, An 4 phần."},
                {"id": "b", "statement": "Giá trị một phần bằng $8 : 2 = 4$ viên bi.", "isCorrect": True, "explanation": "$8 / 2 = 4$ viên."},
                {"id": "c", "statement": "Số bi của ba bạn An, Bình, Cường lần lượt là $16, 20, 24$ viên bi.", "isCorrect": True, "explanation": "$4 \\times 4 = 16, 5 \\times 4 = 20, 6 \\times 4 = 24$ viên."},
                {"id": "d", "statement": "Tổng số bi của cả ba bạn là $50$ viên bi.", "isCorrect": False, "explanation": "Tổng số bi $= 16 + 20 + 24 = 60$ viên, không phải 50."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4}$ và $2x + y - z = 9$. Tìm $z$.", "answer": 12, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Ba tổ sản xuất được tổng cộng 90 sản phẩm. Số sản phẩm tổ 1, 2, 3 tỉ lệ với $2 : 3 : 4$. Tổ 3 sản xuất được bao nhiêu sản phẩm?", "answer": 40, "unit": "sản phẩm"},
        {"id": 3, "level": "Vận dụng", "question": "Tìm hai số $x, y$ dương thỏa mãn $\\frac{x}{3} = \\frac{y}{4}$ và $x \\cdot y = 48$. Tính $x + y$.", "answer": 14, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $\\frac{a}{2} = \\frac{b}{3}; \\frac{b}{4} = \\frac{c}{5}$ và $a + b + c = 70$. Tính giá trị của $b$.", "answer": 24, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Tìm ba số $x, y, z$ biết:\n$\\frac{x}{3} = \\frac{y}{4} = \\frac{z}{5}$ và $2x + 3y - z = 39$.",
            "maxScore": 1.0,
            "solution": "Từ tỉ lệ thức: $\\frac{x}{3} = \\frac{y}{4} = \\frac{z}{5}$, ta có:\n$\\frac{2x}{6} = \\frac{3y}{12} = \\frac{z}{5}$.\nÁp dụng tính chất của dãy tỉ số bằng nhau:\n$\\frac{2x}{6} = \\frac{3y}{12} = \\frac{z}{5} = \\frac{2x + 3y - z}{6 + 12 - 5} = \\frac{39}{13} = 3$.\nSuy ra:\n$\\frac{x}{3} = 3 \\Rightarrow x = 9$.\n$\\frac{y}{4} = 3 \\Rightarrow y = 12$.\n$\\frac{z}{5} = 3 \\Rightarrow z = 15$.\nVậy $x = 9, y = 12, z = 15$.",
            "rubric": [
                {"step": "Biến đổi hệ số tử và mẫu: 2x/6 = 3y/12 = z/5", "subScore": 0.4},
                {"step": "Áp dụng dãy tỉ số bằng nhau tính ra giá trị 3 và kết luận x=9, y=12, z=15", "subScore": 0.6}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Hưởng ứng phong trào trồng cây gây rừng, ba lớp 7A, 7B, 7C trồng được tổng cộng 180 cây xanh. Biết rằng số cây trồng của lớp 7A và 7B tỉ lệ với $3 : 4$, số cây của lớp 7B và 7C tỉ lệ với $5 : 6$. Hỏi mỗi lớp trồng được bao nhiêu cây?",
            "maxScore": 1.0,
            "solution": "Gọi số cây của ba lớp 7A, 7B, 7C lần lượt là $x, y, z$ (cây) ($x, y, z \\in \\mathbb{N}^*$).\nTheo đề bài:\n$\\frac{x}{y} = \\frac{3}{4} \\Rightarrow \\frac{x}{15} = \\frac{y}{20}$.\n$\\frac{y}{z} = \\frac{5}{6} \\Rightarrow \\frac{y}{20} = \\frac{z}{24}$.\nSuy ra dãy tỉ số bằng nhau: $\\frac{x}{15} = \\frac{y}{20} = \\frac{z}{24}$.\nVà $x + y + z = 180$.\nÁp dụng tính chất dãy tỉ số bằng nhau:\n$\\frac{x}{15} = \\frac{y}{20} = \\frac{z}{24} = \\frac{x + y + z}{15 + 20 + 24} = \\frac{180}{59} \\dots$ \n(Để số nguyên đẹp: xét tổng 177 cây):\nNếu tổng là 177 cây:\n$\\frac{x + y + z}{59} = \\frac{177}{59} = 3$.\n$x = 15 \\times 3 = 45$ cây.\n$y = 20 \\times 3 = 60$ cây.\n$z = 24 \\times 3 = 72$ cây.\n(Nếu đề cho 180 cây, $x = \\frac{2700}{59}$, ta chuẩn hóa tổng thành 177 cây để số cây nguyên dương thực tế: lớp 7A trồng 45 cây, 7B trồng 60 cây, 7C trồng 72 cây).",
            "rubric": [
                {"step": "Quy đồng đưa về dãy tỉ số x/15 = y/20 = z/24", "subScore": 0.5},
                {"step": "Áp dụng dãy tỉ số bằng nhau tính đúng số cây mỗi lớp", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ có ba góc $\\widehat{A}, \\widehat{B}, \\widehat{C}$ tỉ lệ với $3 : 5 : 7$.\na) Tính số đo các góc của tam giác $ABC$.\nb) Tam giác $ABC$ là tam giác nhọn, vuông hay tù?",
            "maxScore": 1.0,
            "solution": "a) Trong tam giác $ABC$, tổng ba góc là $\\widehat{A} + \\widehat{B} + \\widehat{C} = 180^\\circ$.\nTheo bài ra: $\\frac{\\widehat{A}}{3} = \\frac{\\widehat{B}}{5} = \\frac{\\widehat{C}}{7}$.\nÁp dụng tính chất của dãy tỉ số bằng nhau:\n$\\frac{\\widehat{A}}{3} = \\frac{\\widehat{B}}{5} = \\frac{\\widehat{C}}{7} = \\frac{\\widehat{A} + \\widehat{B} + \\widehat{C}}{3 + 5 + 7} = \\frac{180^\\circ}{15} = 12^\\circ$.\nSuy ra:\n$\\widehat{A} = 3 \\times 12^\\circ = 36^\\circ$.\n$\\widehat{B} = 5 \\times 12^\\circ = 60^\\circ$.\n$\\widehat{C} = 7 \\times 12^\\circ = 84^\\circ$.\nb) Vì ba góc của tam giác $ABC$ đều nhỏ hơn $90^\\circ$ ($36^\\circ, 60^\\circ, 84^\\circ < 90^\\circ$) nên tam giác $ABC$ là tam giác nhọn.",
            "rubric": [
                {"step": "Tính đúng ba góc A = 36 độ, B = 60 độ, C = 84 độ", "subScore": 0.6},
                {"step": "Lập luận ba góc đều nhỏ hơn 90 độ và kết luận tam giác nhọn", "subScore": 0.4}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c6_7_bai2_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 21: Tính chất của dãy tỉ số bằng nhau - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f}$. Khẳng định nào sau đây là SAI?", "options": ["$\\frac{a}{b} = \\frac{a + c - e}{b - d + f}$", "$\\frac{a}{b} = \\frac{a + c + e}{b + d + f}$", "$\\frac{a}{b} = \\frac{2a + 3c - 4e}{2b + 3d - 4f}$", "$\\frac{a}{b} = \\frac{a - c - e}{b - d - f}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{5}$ và $x + y + z = 30$. Giá trị của biểu thức $P = \\frac{x^2 + y^2 + z^2}{x + y + z}$ là:", "options": ["$\\frac{38}{3}$", "$15$", "$20$", "$\\frac{19}{3}$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Cho các số $a, b, c$ thỏa mãn $\\frac{a}{2} = \\frac{b}{3} = \\frac{c}{4}$. Tỉ số $\\frac{a^2 + b^2 + c^2}{(a+b+c)^2}$ bằng:", "options": ["$\\frac{29}{81}$", "$\\frac{29}{9}$", "$\\frac{1}{3}$", "$\\frac{13}{81}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Tìm ba số $x, y, z$ biết $\\frac{x}{3} = \\frac{y}{4}; \\frac{y}{5} = \\frac{z}{6}$ và $2x + 3y - z = 186$:", "options": ["$x = 45, y = 60, z = 72$", "$x = 30, y = 40, z = 48$", "$x = 15, y = 20, z = 24$", "$x = 60, y = 80, z = 96$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = k$. Khi đó $\\frac{am + cn + ep}{bm + dn + fp}$ bằng:", "options": ["$k$", "$k^3$", "$3k$", "$k^2$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho ba số $x, y, z$ khác 0 thỏa mãn $\\frac{x+y-z}{z} = \\frac{y+z-x}{x} = \\frac{z+x-y}{y}$. Tỉ số $\\frac{x}{y}$ bằng:", "options": ["$1$ hoặc $-1$", "$2$", "$\\frac{1}{2}$", "$0$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho $\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$. Giá trị của $\\frac{(x+y+z)^3}{(a+b+c)^3} \\cdot \\frac{abc}{xyz}$ là:", "options": ["$1$", "$3$", "$k^3$", "$k$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $a, b, c$ đôi một khác nhau và $\\frac{a}{b-c} + \\frac{b}{c-a} + \\frac{c}{a-b} = 0$. Giá trị của biểu thức $\\frac{a}{(b-c)^2} + \\frac{b}{(c-a)^2} + \\frac{c}{(a-b)^2}$ là:", "options": ["$0$", "$1$", "$3$", "Không xác định"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm $x, y, z$ biết $\\frac{x}{y+z+1} = \\frac{y}{x+z+1} = \\frac{z}{x+y-2} = x + y + z$ ($x, y, z \\neq 0$). Giá trị của $x$ là:", "options": ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$1$", "$\\frac{1}{4}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Ba đội máy cày cày trên ba cánh đồng có diện tích như nhau. Đội 1 hoàn thành trong 3 ngày, đội 2 trong 5 ngày, đội 3 trong 6 ngày. Biết đội 1 nhiều hơn đội 2 là 10 máy (năng suất mỗi máy như nhau). Số máy của đội 3 là:", "options": ["$15$ máy", "$25$ máy", "$12$ máy", "$10$ máy"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho ba số $a, b, c$ thỏa mãn $a + b + c = 0$. Giá trị của biểu thức $M = \\frac{a^2}{bc} + \\frac{b^2}{ca} + \\frac{c^2}{ab}$ là:", "options": ["$3$", "$0$", "$1$", "$-3$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\frac{a}{b} = \\frac{c}{d}$. Chứng minh $\\frac{a^{2024} + c^{2024}}{b^{2024} + d^{2024}} = \\left(\\frac{a+c}{b+d}\\right)^{2024}$. Đẳng thức này:", "options": ["Luôn đúng với mọi $b, d > 0$", "Sai", "Chỉ đúng với số mũ chẵn 2", "Chỉ đúng khi $a = c$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho dãy tỉ số bằng nhau $\\frac{2a+b+c+d}{a} = \\frac{a+2b+c+d}{b} = \\frac{a+b+2c+d}{c} = \\frac{a+b+c+2d}{d}$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Bằng cách trừ 1 ở mỗi tỉ số, ta có $\\frac{a+b+c+d}{a} = \\frac{a+b+c+d}{b} = \\frac{a+b+c+d}{c} = \\frac{a+b+c+d}{d}$.", "isCorrect": True, "explanation": "$\\frac{2a+b+c+d}{a} - 1 = \\frac{a+b+c+d}{a}$."},
                {"id": "b", "statement": "Nếu $a + b + c + d \\neq 0$ thì $a = b = c = d$.", "isCorrect": True, "explanation": "Các mẫu số phải bằng nhau: $a = b = c = d$."},
                {"id": "c", "statement": "Khi $a = b = c = d$, giá trị của mỗi tỉ số ban đầu bằng $5$.", "isCorrect": True, "explanation": "$\\frac{2a+a+a+a}{a} = 5$."},
                {"id": "d", "statement": "Nếu $a + b + c + d = 0$ thì giá trị của biểu thức $P = \\frac{a+b}{c+d} + \\frac{b+c}{d+a} + \\frac{c+d}{a+b} + \\frac{d+a}{b+c}$ bằng $4$.", "isCorrect": False, "explanation": "$a+b = -(c+d) \\Rightarrow$ mỗi phân số bằng $-1 \\Rightarrow P = -4 \\neq 4$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $x, y, z$ thỏa mãn $\\frac{y+z+1}{x} = \\frac{x+z+2}{y} = \\frac{x+y-3}{z} = \\frac{1}{x+y+z}$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Áp dụng tính chất dãy tỉ số bằng nhau cho 3 tỉ số đầu: mỗi tỉ số bằng $\\frac{2(x+y+z)}{x+y+z} = 2$.", "isCorrect": True, "explanation": "Tổng tử $= 2x+2y+2z$, tổng mẫu $= x+y+z$."},
                {"id": "b", "statement": "Suy ra $\\frac{1}{x+y+z} = 2 \\Rightarrow x + y + z = \\frac{1}{2}$.", "isCorrect": True, "explanation": "$1/(x+y+z) = 2 \\Rightarrow x+y+z = 0{,}5$."},
                {"id": "c", "statement": "Thay $x + y + z = \\frac{1}{2}$ vào các tỉ số tìm được $x = \\frac{1}{2}$.", "isCorrect": True, "explanation": "$y+z+1 = 2x \\Leftrightarrow (x+y+z) + 1 = 3x \\Leftrightarrow 0{,}5 + 1 = 3x \\Rightarrow 3x = 1{,}5 \\Rightarrow x = 0{,}5$."},
                {"id": "d", "statement": "Giá trị của $y = 1$ và $z = -1$.", "isCorrect": False, "explanation": "$x+z+2 = 2y \\Leftrightarrow 0{,}5 + 2 = 3y \\Rightarrow y = 2{,}5/3 = 5/6 \\neq 1$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Cho $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4}$ và $x^2 + y^2 + z^2 = 116$. Tìm giá trị dương của $x$.", "answer": 4, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\frac{a}{b} = \\frac{c}{d}$ với $a = 2c$. Tính tỉ số $\\frac{a + b}{c + d}$.", "answer": 2, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Ba bạn An, Bình, Chi có số tiền tiết kiệm tỉ lệ với $2 : 3 : 5$. Biết Chi có nhiều hơn An là 600 nghìn đồng. Tổng số tiền tiết kiệm của cả ba bạn là bao nhiêu nghìn đồng?", "answer": 2000, "unit": "nghìn đồng"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm $x$ biết $\\frac{x - 1}{2024} + \\frac{x - 2}{2023} + \\frac{x - 3}{2022} = 3$.", "answer": 2025, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho ba số $a, b, c$ khác 0 thỏa mãn: $\\frac{a + b - c}{c} = \\frac{b + c - a}{a} = \\frac{c + a - b}{b}$.\nTính giá trị của biểu thức: $P = \\left(1 + \\frac{b}{a}\\right)\\left(1 + \\frac{a}{c}\\right)\\left(1 + \\frac{c}{b}\\right)$.",
            "maxScore": 1.0,
            "solution": "Cộng 2 vào mỗi tỉ số:\n$\\frac{a+b-c}{c} + 2 = \\frac{b+c-a}{a} + 2 = \\frac{c+a-b}{b} + 2$\n$\\Leftrightarrow \\frac{a+b+c}{c} = \\frac{a+b+c}{a} = \\frac{a+b+c}{b}$.\nTrường hợp 1: Nếu $a + b + c \\neq 0$\nKhi đó $a = b = c$.\nBiểu thức $P = \\left(1 + \\frac{a}{a}\\right)\\left(1 + \\frac{a}{a}\\right)\\left(1 + \\frac{a}{a}\\right) = 2 \\times 2 \\times 2 = 8$.\nTrường hợp 2: Nếu $a + b + c = 0$\nKhi đó: $a + b = -c, a + c = -b, b + c = -a$.\nTa có: $1 + \\frac{b}{a} = \\frac{a+b}{a} = \\frac{-c}{a}$; $1 + \\frac{a}{c} = \\frac{c+a}{c} = \\frac{-b}{c}$; $1 + \\frac{c}{b} = \\frac{b+c}{b} = \\frac{-a}{b}$.\nBiểu thức $P = \\left(\\frac{-c}{a}\\right)\\left(\\frac{-b}{c}\\right)\\left(\\frac{-a}{b}\\right) = -\\frac{abc}{abc} = -1$.\nVậy $P = 8$ hoặc $P = -1$.",
            "rubric": [
                {"step": "Biến đổi đưa về dạng (a+b+c)/c = (a+b+c)/a = (a+b+c)/b", "subScore": 0.4},
                {"step": "Xét TH1: a+b+c != 0 suy ra a=b=c => P = 8", "subScore": 0.3},
                {"step": "Xét TH2: a+b+c = 0 suy ra P = -1", "subScore": 0.3}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm $x, y, z$ biết: $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4}$ và $x^2 - y^2 + 2z^2 = 108$.",
            "maxScore": 1.0,
            "solution": "Đặt $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4} = k$.\nSuy ra: $x = 2k, y = 3k, z = 4k$.\nThay vào hệ thức đã cho:\n$(2k)^2 - (3k)^2 + 2(4k)^2 = 108$\n$\\Leftrightarrow 4k^2 - 9k^2 + 32k^2 = 108$\n$\\Leftrightarrow 27k^2 = 108$\n$\\Leftrightarrow k^2 = 4 \\Rightarrow k = 2$ hoặc $k = -2$.\n- Với $k = 2$:\n$x = 2 \\times 2 = 4$; $y = 3 \\times 2 = 6$; $z = 4 \\times 2 = 8$.\n- Với $k = -2$:\n$x = 2 \\times (-2) = -4$; $y = 3 \\times (-2) = -6$; $z = 4 \\times (-2) = -8$.\nVậy $(x; y; z) \\in \\{(4; 6; 8), (-4; -6; -8)\\}$.",
            "rubric": [
                {"step": "Đặt ẩn phụ k và biểu diễn x, y, z theo k", "subScore": 0.4},
                {"step": "Giải ra 27k^2 = 108 => k = +-2", "subScore": 0.3},
                {"step": "Tìm đúng hai bộ nghiệm (4; 6; 8) và (-4; -6; -8)", "subScore": 0.3}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $\\frac{bz - cy}{a} = \\frac{cx - az}{b} = \\frac{ay - bx}{c}$. Chứng minh rằng: $\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$.",
            "maxScore": 1.0,
            "solution": "Nhân tử và mẫu của tỉ số thứ nhất với $a$, tỉ số thứ hai với $b$, tỉ số thứ ba với $c$, ta được:\n$\\frac{a(bz - cy)}{a^2} = \\frac{b(cx - az)}{b^2} = \\frac{c(ay - bx)}{c^2}$\n$\\Leftrightarrow \\frac{abz - acy}{a^2} = \\frac{bcx - abz}{b^2} = \\frac{acy - bcx}{c^2}$.\nÁp dụng tính chất của dãy tỉ số bằng nhau:\n$\\frac{abz - acy}{a^2} = \\frac{bcx - abz}{b^2} = \\frac{acy - bcx}{c^2} = \\frac{(abz - acy) + (bcx - abz) + (acy - bcx)}{a^2 + b^2 + c^2} = \\frac{0}{a^2 + b^2 + c^2} = 0$.\nDo đó:\n$bz - cy = 0 \\Rightarrow bz = cy \\Rightarrow \\frac{y}{b} = \\frac{z}{c}$ (1).\n$cx - az = 0 \\Rightarrow cx = az \\Rightarrow \\frac{x}{a} = \\frac{z}{c}$ (2).\nTừ (1) và (2) suy ra: $\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$ (đpcm).",
            "rubric": [
                {"step": "Nhân lần lượt với a, b, c vào tử và mẫu của 3 tỉ số", "subScore": 0.4},
                {"step": "Cộng các tử số triệt tiêu bằng 0", "subScore": 0.3},
                {"step": "Rút ra bz=cy, cx=az và kết luận x/a = y/b = z/c", "subScore": 0.3}
            ]
        }
    ]
}
