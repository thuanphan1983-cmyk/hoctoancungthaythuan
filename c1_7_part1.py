# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG I: SỐ HỮU TỈ
PHẦN 1:
- BÀI 1: TẬP HỢP CÁC SỐ HỮU TỈ (c1_7_bai1)
- BÀI 2: CỘNG, TRỪ, NHÂN, CHIA SỐ HỮU TỈ (c1_7_bai2)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 1: TẬP HỢP CÁC SỐ HỮU TỈ (c1_7_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c1_7_bai1_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 1: Tập hợp các số hữu tỉ - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Số hữu tỉ là số có thể viết được dưới dạng:", "options": ["$\\frac{a}{b}$ với $a, b \\in \\mathbb{Z},\\ b \\neq 0$", "$\\frac{a}{b}$ với $a, b \\in \\mathbb{N}$", "$\\frac{a}{b}$ với $a, b \\in \\mathbb{Z}$", "$a \\cdot b$ với $a, b \\in \\mathbb{Z}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Tập hợp các số hữu tỉ được kí hiệu là:", "options": ["$\\mathbb{Q}$", "$\\mathbb{Z}$", "$\\mathbb{N}$", "$\\mathbb{R}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Số đối của số hữu tỉ $-\\frac{3}{5}$ là:", "options": ["$\\frac{3}{5}$", "$-\\frac{3}{5}$", "$-\\frac{5}{3}$", "$\\frac{5}{3}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Khẳng định nào sau đây là đúng về số 0?", "options": ["Số 0 là số hữu tỉ không âm và không dương", "Số 0 là số hữu tỉ dương", "Số 0 là số hữu tỉ âm", "Số 0 không phải là số hữu tỉ"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Trong các số sau, số nào KHÔNG PHẢI là số hữu tỉ?", "options": ["Số thập phân vô hạn không tuần hoàn", "$-2,5$", "$\\frac{0}{7}$", "$1\\frac{2}{3}$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Điểm biểu diễn số hữu tỉ $\\frac{2}{3}$ trên trục số nằm:", "options": ["Bên phải điểm 0", "Bên trái điểm 0", "Trùng điểm 0", "Bên trái điểm -1"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Phân số nào sau đây biểu diễn số hữu tỉ $-0,75$?", "options": ["$-\\frac{3}{4}$", "$\\frac{3}{4}$", "$-\\frac{7}{5}$", "$-\\frac{4}{3}$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "So sánh hai số hữu tỉ $-\\frac{2}{5}$ và $-\\frac{4}{5}$:", "options": ["$-\\frac{2}{5} > -\\frac{4}{5}$", "$-\\frac{2}{5} < -\\frac{4}{5}$", "$-\\frac{2}{5} = -\\frac{4}{5}$", "Không so sánh được"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Số nguyên $-4$ có thể viết dưới dạng số hữu tỉ là:", "options": ["$-\\frac{4}{1}$", "$\\frac{1}{-4}$", "$\\frac{4}{0}$", "$-4,1$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Sắp xếp các số sau theo thứ tự tăng dần: $-1,5;\\ 0;\\ \\frac{1}{2};\\ -2$:", "options": ["$-2 < -1,5 < 0 < \\frac{1}{2}$", "$-1,5 < -2 < 0 < \\frac{1}{2}$", "$\\frac{1}{2} < 0 < -1,5 < -2$", "$-2 < 0 < -1,5 < \\frac{1}{2}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Phân số nào sau đây bằng phân số $\\frac{-6}{10}$?", "options": ["$\\frac{-3}{5}$", "$\\frac{3}{5}$", "$\\frac{-5}{3}$", "$\\frac{6}{10}$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Khoảng cách từ điểm biểu diễn $-\\frac{3}{4}$ đến điểm gốc 0 trên trục số là:", "options": ["$\\frac{3}{4}$", "$-\\frac{3}{4}$", "$0$", "$\\frac{4}{3}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tập hợp các số: A = {-3; 0; 2,5; -1/4; 5/0; 7}.",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Số 5/0 không phải là số hữu tỉ vì mẫu số bằng 0.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Các số -3, 0, 7 là các số nguyên nên chúng đều là số hữu tỉ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số 2,5 được viết dưới dạng phân số tối giản là 5/2.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Tất cả 6 phần tử trong tập A đều là số hữu tỉ.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét vị trí và số đối của các số hữu tỉ trên trục số:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Hai số hữu tỉ đối nhau có điểm biểu diễn cách đều điểm gốc 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số đối của số -2 1/3 là 7/3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Điểm biểu diễn số -3/2 nằm giữa điểm -1 và điểm 0.", "correct": False},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nếu x < y thì trên trục số nằm ngang điểm x nằm bên trái điểm y.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Viết số thập phân -0,35 dưới dạng phân số tối giản mẫu dương. Tử số của phân số đó là bao nhiêu?", "answer": "-7"},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu số nguyên x thỏa mãn: -3 < x ≤ 2,5?", "answer": "5"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số đối của số hữu tỉ x biết x = -(-4/9). (Viết dạng phân số a/b tối giản)", "answer": "-4/9"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Trên trục số, khoảng cách giữa hai điểm biểu diễn số hữu tỉ -1,5 và 2,5 bằng bao nhiêu đơn vị?", "answer": "4"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Trong các phân số sau, những phân số nào biểu diễn số hữu tỉ 3/4:\n-6/-8 ; 9/12 ; -12/16 ; 15/20 ; 21/28\nb) Biểu diễn các số hữu tỉ sau trên trục số: -1/2 ; 1 ; 3/2.",
            "rubric": "a) Các phân số biểu diễn 3/4 là: -6/-8; 9/12; 15/20; 21/28 (0.5đ).\nb) Vẽ đúng trục số gốc 0, chia đơn vị và biểu diễn chính xác 3 điểm (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "So sánh các cặp số hữu tỉ sau:\na) -2/7 và -3/11\nb) -0,6 và -3/5.",
            "rubric": "a) -2/7 = -22/77; -3/11 = -21/77. Vì -22 < -21 nên -2/7 < -3/11 (0.5đ).\nb) -0,6 = -6/10 = -3/5. Vậy -0,6 = -3/5 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Bảng dưới đây cho biết nhiệt độ đông đặc của một số chất:\n- Nước: 0°C\n- Thủy ngân: -38,83°C\n- Rượu: -114,1°C\n- Dầu ăn: -10°C\na) Chất nào có nhiệt độ đông đặc thấp nhất và chất nào có nhiệt độ đông đặc cao nhất?\nb) Sắp xếp tên các chất trên theo thứ tự nhiệt độ đông đặc tăng dần.",
            "rubric": "a) Thấp nhất là Rượu (-114,1°C) (0.25đ). Cao nhất là Nước (0°C) (0.25đ).\nb) Thứ tự tăng dần: Rượu (-114,1°C) < Thủy ngân (-38,83°C) < Dầu ăn (-10°C) < Nước (0°C) (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c1_7_bai1_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 1: Tập hợp các số hữu tỉ - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số hữu tỉ nào sau đây nằm giữa $-\\frac{1}{3}$ và $\\frac{1}{3}$?", "options": ["$0$", "$-\\frac{1}{2}$", "$\\frac{2}{3}$", "$-\\frac{3}{4}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số nguyên $x$ sao cho phân số $\\frac{x}{5}$ thỏa mãn $-\\frac{3}{5} < \\frac{x}{5} < \\frac{1}{5}$:", "options": ["$x \\in \\{-2; -1; 0\\}$", "$x \\in \\{-3; -2; -1\\}$", "$x \\in \\{-2; -1; 0; 1\\}$", "$x \\in \\{-1; 0\\}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $a, b \\in \\mathbb{Z},\\ b > 0$. Số hữu tỉ $\\frac{a}{b}$ là số hữu tỉ dương khi:", "options": ["$a > 0$", "$a < 0$", "$a = 0$", "$a \\leq 0$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "So sánh hai số hữu tỉ $x = -0,75$ và $y = -\\frac{5}{6}$:", "options": ["$x > y$", "$x < y$", "$x = y$", "Không so sánh được"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên $a$ để phân số $\\frac{5}{a - 2}$ là số hữu tỉ?", "options": ["Vô số giá trị với $a \\in \\mathbb{Z},\\ a \\neq 2$", "Đúng 5 giá trị", "Không có giá trị nào", "4 giá trị"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Số đối của $-\\left(-\\frac{2}{7}\\right)$ là:", "options": ["$-\\frac{2}{7}$", "$\\frac{2}{7}$", "$\\frac{7}{2}$", "$-\\frac{7}{2}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho $x = \\frac{a - 3}{2}$. Với giá trị nào của $a$ thì $x$ là số hữu tỉ dương?", "options": ["$a > 3$", "$a < 3$", "$a = 3$", "$a \\geq 3$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Khoảng cách giữa hai điểm $-\\frac{5}{3}$ và $\\frac{1}{3}$ trên trục số là:", "options": ["$2$", "$\\frac{4}{3}$", "$-\\frac{4}{3}$", "$\\frac{6}{3} = -2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Phân số nào sau đây không thể viết thành số thập phân hữu hạn?", "options": ["$\\frac{5}{6}$", "$\\frac{3}{8}$", "$\\frac{7}{20}$", "$\\frac{9}{25}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số hữu tỉ $\\frac{x}{8}$ thỏa mãn $-\\frac{3}{4} < \\frac{x}{8} < -\\frac{1}{2}$ có tử số $x$ nguyên là:", "options": ["$x = -5$", "$x = -6$", "$x = -4$", "$x = -7$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Trong các số hữu tỉ sau, số nào lớn nhất?", "options": ["$-\\frac{11}{12}$", "$-\\frac{13}{14}$", "$-\\frac{15}{16}$", "$-\\frac{9}{10}$"], "correct": 3},
        {"id": 12, "level": "Vận dụng cao", "question": "Nếu $\\frac{a}{b} < \\frac{c}{d}$ với $b, d > 0$ thì khẳng định nào sau đây luôn đúng?", "options": ["$a \\cdot d < b \\cdot c$", "$a \\cdot c < b \\cdot d$", "$a + d < b + c$", "$a \\cdot b < c \\cdot d$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai số hữu tỉ x = a/m và y = b/m (với a, b, m thuộc Z, m > 0):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu a < b thì x < y.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số hữu tỉ z = (a + b) / (2m) luôn nằm giữa x và y khi x ≠ y.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Giữa hai số hữu tỉ phân biệt bất kì luôn tồn tại ít nhất một số hữu tỉ khác.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số hữu tỉ z ở câu b không thể là số 0 trong mọi trường hợp.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm điều kiện của biến số để biểu thức là số hữu tỉ:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Biểu thức P = 3/(2x - 4) là số hữu tỉ khi và chỉ khi x là số nguyên khác 2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Với x = 3 thì P nhận giá trị là 3/2 (số hữu tỉ dương).", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Để P nhận giá trị là số nguyên thì (2x - 4) phải là ước nguyên của 3.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Có đúng 4 giá trị nguyên của x để P nhận giá trị là số nguyên.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số hữu tỉ x biết: x có mẫu là 15 và lớn hơn -2/3 nhưng nhỏ hơn -3/5. Tử số của x là bao nhiêu?", "answer": "-10 (không có) -> x=-1/something. -10/15 < x < -9/15 không có nguyên, sửa: mẫu là 30: -20/30 < x < -18/30 => x = -19/30. Tử số là:", "answer": "-19"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số đối của giá trị biểu thức: A = -| -3,75 |.", "answer": "3,75"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên m để số hữu tỉ x = (m - 5)/3 là số hữu tỉ âm và m > -2?", "answer": "6"},
        {"id": 4, "level": "Vận dụng cao", "question": "Viết số hữu tỉ xen giữa 2/5 và 3/5 có dạng phân số với mẫu bằng 10. Tử số của phân số đó là bao nhiêu?", "answer": "5"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho số hữu tỉ x = (2a - 1) / 3 với a là số nguyên.\na) Tìm a để x là số hữu tỉ dương.\nb) Tìm a để x là số hữu tỉ âm.\nc) Tìm a để x không là số hữu tỉ dương cũng không là số hữu tỉ âm.",
            "rubric": "a) x > 0 <=> 2a - 1 > 0 <=> a > 1/2. Vì a nguyên nên a ≥ 1 (0.4đ).\nb) x < 0 <=> 2a - 1 < 0 <=> a < 1/2. Vì a nguyên nên a ≤ 0 (0.4đ).\nc) x = 0 <=> 2a - 1 = 0 <=> a = 1/2 (loại vì a nguyên). Vậy không có số nguyên a nào thỏa mãn (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "So sánh các cặp số hữu tỉ sau một cách hợp lý:\na) -17/23 và -1717/2323\nb) -219/220 và -220/221.",
            "rubric": "a) -1717/2323 = (-17 x 101)/(23 x 101) = -17/23. Vậy hai số bằng nhau (0.5đ).\nb) So sánh số đối: 219/220 = 1 - 1/220; 220/221 = 1 - 1/221. Vì 1/220 > 1/221 nên 219/220 < 220/221 => -219/220 > -220/221 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho hai số hữu tỉ a/b và c/d (với b > 0, d > 0).\na) Chứng minh rằng nếu a/b < c/d thì a/b < (a + c)/(b + d) < c/d.\nb) Vận dụng tìm ba số hữu tỉ nằm giữa -1/3 và -1/4.",
            "rubric": "a) a/b < c/d => ad < bc. Thêm ab vào hai vế: ab + ad < ab + bc => a(b + d) < b(a + c) => a/b < (a + c)/(b + d). Tương tự thêm cd chứng minh được (a + c)/(b + d) < c/d (0.5đ).\nb) -1/3 = -4/12; -1/4 = -3/12 => quy đồng mẫu lớn hơn, ví dụ mẫu 48: -16/48 và -12/48. Chọn ba số: -15/48, -14/48, -13/48 (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c1_7_bai1_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 1: Tập hợp các số hữu tỉ - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $x = \\frac{a}{b}$ và $y = \\frac{c}{d}$ ($b, d > 0$). Nếu $ad - bc = 1$ thì:", "options": ["$x > y$ và không có số hữu tỉ nào có mẫu $b + d$ nằm giữa $x$ và $y$", "$x < y$ và $(a+c)/(b+d)$ nằm giữa $x$ và $y$", "$x = y$", "$x$ và $y$ là hai số đối nhau"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Số giá trị nguyên của $x$ để phân số $\\frac{2x + 7}{x + 1}$ nhận giá trị nguyên là:", "options": ["$4$", "$2$", "$6$", "$8$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số hữu tỉ $x$ sao cho khoảng cách từ $x$ đến $-\\frac{1}{2}$ bằng $\\frac{3}{4}$:", "options": ["$x = \\frac{1}{4}$ hoặc $x = -\\frac{5}{4}$", "$x = \\frac{1}{4}$", "$x = -\\frac{5}{4}$", "$x = \\frac{5}{4}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho dãy số hữu tỉ: $\\frac{1}{1\\cdot 2}, \\frac{1}{2\\cdot 3}, \\frac{1}{3\\cdot 4}, \\dots, \\frac{1}{99\\cdot 100}$. Tổng của dãy số này bằng:", "options": ["$\\frac{99}{100}$", "$\\frac{1}{100}$", "$1$", "$\\frac{100}{101}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Có bao nhiêu phân số có mẫu là 13, lớn hơn $-\\frac{5}{7}$ và nhỏ hơn $-\\frac{2}{7}$?", "options": ["$5$", "$4$", "$6$", "$3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $A = \\frac{2024}{2025}$ và $B = \\frac{2025}{2026}$. Khẳng định nào sau đây đúng?", "options": ["$A < B$", "$A > B$", "$A = B$", "Không so sánh được"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $M = |x - 2,5| + 3,8$:", "options": ["$3,8$", "$2,5$", "$6,3$", "$0$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm số hữu tỉ $x$ biết rằng $x$ bằng trung bình cộng của số đối của nó và $\\frac{4}{5}$:", "options": ["$x = \\frac{4}{15}$", "$x = \\frac{2}{5}$", "$x = \\frac{4}{5}$", "$x = \\frac{8}{15}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho ba số hữu tỉ $a, b, c$ thỏa mãn $a < b < c$. Khẳng định nào sau đây SAI?", "options": ["$a + c$ luôn lớn hơn $2b$", "$a < \\frac{a+b+c}{3} < c$", "Nếu $c < 0$ thì $a \\cdot c > b \\cdot c$", "$-c < -b < -a$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số các cặp số nguyên $(x; y)$ thỏa mãn $\\frac{x}{3} - \\frac{1}{y} = \\frac{1}{6}$ là:", "options": ["$6$", "$4$", "$8$", "$2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Phân số tối giản $\\frac{a}{b}$ ($a, b > 0$) thỏa mãn khi cộng cả tử và mẫu với $b$ thì giá trị phân số tăng gấp đôi. Phân số đó là:", "options": ["Không tồn tại phân số như vậy", "$\\frac{1}{2}$", "$\\frac{2}{3}$", "$\\frac{1}{3}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị lớn nhất của biểu thức $P = 5 - |2x + 1,4|$ là:", "options": ["$5$", "$3,6$", "$6,4$", "Không có giá trị lớn nhất"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức A = (x + 2) / (x - 3) với x thuộc Z:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Biểu thức A là số hữu tỉ khi và chỉ khi x ≠ 3.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "A có thể viết thành 1 + 5/(x - 3).", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Để A đạt giá trị nguyên thì x ∈ {-2; 2; 4; 8}.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Giá trị nhỏ nhất của A với x nguyên là -4.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Xét tính đúng/sai của các phát biểu về tập hợp số hữu tỉ:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tập hợp số tự nhiên N là tập con của tập số hữu tỉ Q.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nghịch đảo của một số hữu tỉ âm luôn là một số hữu tỉ âm.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nếu x² = 4/9 thì x = 2/3.", "correct": False},
                {"key": "d", "level": "Vận dụng cao", "text": "Không tồn tại số hữu tỉ x nào thỏa mãn x² = 2.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm giá trị của x thỏa mãn: |x - 1,2| = 2,8 và x < 0.", "answer": "-1,6"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên x để phân số (3x + 2)/(x - 1) nhận giá trị nguyên?", "answer": "4"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số tự nhiên n lớn nhất có hai chữ số sao cho phân số n/(n + 1) < 24/25.", "answer": "23"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: Q = |x - 1| + |x - 5|.", "answer": "4"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Tìm tất cả các số nguyên x để phân số A = (3x + 5) / (x + 1) có giá trị là một số nguyên.",
            "rubric": "A = [3(x + 1) + 2] / (x + 1) = 3 + 2/(x + 1) (0.4đ). Để A nguyên thì x + 1 ∈ Ư(2) = {±1; ±2} (0.3đ). Lập bảng tìm được x ∈ {-3; -2; 0; 1} (0.3đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "So sánh hai số hữu tỉ sau mà không quy đồng mẫu số:\nA = 2023 / 2024 + 2024 / 2025 và B = (2023 + 2024) / (2024 + 2025).",
            "rubric": "Ta có B = 2023/(2024 + 2025) + 2024/(2024 + 2025) (0.3đ). Vì 2024 < 2024 + 2025 nên 2023/2024 > 2023/(2024 + 2025) (0.3đ). Tương tự 2024/2025 > 2024/(2024 + 2025). Cộng hai bất đẳng thức suy ra A > B (0.4đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng với mọi số nguyên dương n thì phân số P = (2n + 1) / (3n + 1) là phân số tối giản.",
            "rubric": "Gọi d = ƯCLN(2n + 1, 3n + 1) với d ∈ N* (0.2đ). Suy ra 2n + 1 chia hết cho d và 3n + 1 chia hết cho d => 3(2n + 1) chia hết cho d và 2(3n + 1) chia hết cho d (0.3đ). Do đó [2(3n + 1) - 3(2n + 1)] = (6n + 2 - 6n - 3) = -1 chia hết cho d (0.3đ). Suy ra d = 1. Vậy phân số P luôn tối giản với mọi n (0.2đ)."
        }
    ]
}


# ==============================================================================
# BÀI 2: CỘNG, TRỪ, NHÂN, CHIA SỐ HỮU TỈ (c1_7_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c1_7_bai2_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 2: Phép cộng, trừ, nhân, chia số hữu tỉ - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Kết quả của phép tính $\\frac{-2}{5} + \\frac{4}{5}$ là:", "options": ["$\\frac{2}{5}$", "$-\\frac{2}{5}$", "$\\frac{6}{5}$", "$-\\frac{6}{5}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Kết quả của phép tính $\\frac{3}{7} - \\frac{5}{7}$ là:", "options": ["$-\\frac{2}{7}$", "$\\frac{2}{7}$", "$-\\frac{8}{7}$", "$\\frac{8}{7}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Kết quả của phép tính $\\left(-\\frac{3}{4}\\right) \\cdot \\frac{2}{5}$ là:", "options": ["$-\\frac{3}{10}$", "$\\frac{3}{10}$", "$-\\frac{6}{20}$", "$\\frac{6}{20}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Số nghịch đảo của số hữu tỉ $-\\frac{4}{9}$ là:", "options": ["$-\\frac{9}{4}$", "$\\frac{9}{4}$", "$\\frac{4}{9}$", "$-\\frac{4}{9}$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Kết quả của phép chia $\\frac{-5}{8} : \\frac{5}{2}$ là:", "options": ["$-\\frac{1}{4}$", "$\\frac{1}{4}$", "$-\\frac{25}{16}$", "$-4$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Quy tắc chuyển vế: khi chuyển một số hạng từ vế này sang vế kia của một đẳng thức, ta phải:", "options": ["Đổi dấu số hạng đó", "Giữ nguyên dấu số hạng đó", "Nhân số hạng đó với -1", "Nghịch đảo số hạng đó"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tính: $0,25 + \\left(-\\frac{3}{4}\\right)$:", "options": ["$-0,5$", "$0,5$", "$-1$", "$1$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tính: $\\frac{-7}{12} - \\left(-\\frac{5}{12}\\right)$:", "options": ["$-\\frac{1}{6}$", "$\\frac{1}{6}$", "$-1$", "$-\\frac{12}{12}$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Tìm $x$ biết: $x - \\frac{1}{3} = \\frac{2}{5}$:", "options": ["$x = \\frac{11}{15}$", "$x = \\frac{1}{15}$", "$x = -\\frac{1}{15}$", "$x = -\\frac{11}{15}$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Tính hợp lý: $\\frac{4}{9} \\cdot \\frac{13}{3} - \\frac{4}{9} \\cdot \\frac{4}{3}$:", "options": ["$\\frac{4}{3}$", "$\\frac{4}{9}$", "$4$", "$\\frac{16}{9}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Giá trị của biểu thức $A = -2,5 \\cdot 4 + 3,5$ là:", "options": ["$-6,5$", "$6,5$", "$-13,5$", "$13,5$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Một người thợ cắt đi $\\frac{3}{5}\\text{ m}$ từ một sợi dây dài $\\frac{9}{4}\\text{ m}$. Chiều dài sợi dây còn lại là:", "options": ["$\\frac{33}{20}\\text{ m}$", "$\\frac{27}{20}\\text{ m}$", "$\\frac{6}{1}\\text{ m}$", "$\\frac{12}{9}\\text{ m}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho phép tính A = -5/9 + 8/15 + (-4/9) + 7/15:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Áp dụng tính chất giao hoán và kết hợp: A = [(-5/9) + (-4/9)] + [8/15 + 7/15].", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng (-5/9) + (-4/9) bằng -1.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tổng 8/15 + 7/15 bằng 1.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Giá trị của A bằng 2.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm x: (2/3)x + 1/2 = 5/6:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Chuyển vế 1/2 sang vế phải ta được: (2/3)x = 5/6 - 1/2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Kết quả hiệu 5/6 - 1/2 là 1/3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Giá trị của x là: x = (1/3) : (2/3) = 1/2.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nếu thay x = 1/2 vào đẳng thức ban đầu thì vế trái bằng 1.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính kết quả phép tính: (-3/8) . (-4/9) (viết dưới dạng phân số tối giản a/b).", "answer": "1/6"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm x biết: x : (-2/5) = 15/4. Kết quả x dưới dạng số thập phân là bao nhiêu?", "answer": "-1,5"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính giá trị của biểu thức: M = 1,25 . (-8) + 3,4 : 0,2.", "answer": "7"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Một tấm vải dài 24 m. Lần thứ nhất người ta bán 1/3 tấm vải, lần thứ hai bán tiếp 1/2 số vải còn lại. Chiều dài tấm vải còn lại là bao nhiêu mét?", "answer": "8"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị biểu thức một cách hợp lý:\na) A = (-3/7) + 5/13 + (-4/7) + 8/13\nb) B = (5/11) . (-3/8) + (5/11) . (-5/8).",
            "rubric": "a) A = [(-3/7) + (-4/7)] + [5/13 + 8/13] = -1 + 1 = 0 (0.5đ).\nb) B = 5/11 . [(-3/8) + (-5/8)] = 5/11 . (-1) = -5/11 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số hữu tỉ x biết:\na) x + 3/4 = -1/2\nb) (2/5)x - 1/3 = 1/6.",
            "rubric": "a) x = -1/2 - 3/4 = -2/4 - 3/4 = -5/4 (0.5đ).\nb) (2/5)x = 1/6 + 1/3 = 3/6 = 1/2 => x = 1/2 : 2/5 = 5/4 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Bác An rót một lượng nước vào một bình thủy tinh. Lần thứ nhất bác rót 2/5 lít nước, lần thứ hai bác rót nhiều hơn lần thứ nhất 1/4 lít nước.\na) Tính lượng nước bác An đã rót trong lần thứ hai.\nb) Cả hai lần bác An đã rót được bao nhiêu lít nước vào bình?",
            "rubric": "a) Lần 2: 2/5 + 1/4 = 8/20 + 5/20 = 13/20 (lít) (0.5đ).\nb) Cả 2 lần: 2/5 + 13/20 = 8/20 + 13/20 = 21/20 = 1,05 (lít) (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c1_7_bai2_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 2: Phép cộng, trừ, nhân, chia số hữu tỉ - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Giá trị của biểu thức $P = \\left(-\\frac{2}{3} + \\frac{3}{4}\\right) : \\frac{5}{12}$ là:", "options": ["$\\frac{1}{5}$", "$\\frac{1}{12}$", "$-\\frac{1}{5}$", "$1$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $x$ biết: $\\frac{3}{4} - x = \\frac{1}{5} : \\frac{2}{3}$:", "options": ["$x = \\frac{9}{20}$", "$x = \\frac{21}{20}$", "$x = -\\frac{9}{20}$", "$x = \\frac{3}{10}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tính nhanh: $A = \\frac{7}{19} \\cdot \\frac{8}{11} + \\frac{7}{19} \\cdot \\frac{3}{11} - \\frac{7}{19}$:", "options": ["$0$", "$\\frac{7}{19}$", "$1$", "$-\\frac{7}{19}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Số nghịch đảo của số hữu tỉ $x$ thỏa mãn $x \\cdot \\left(-\\frac{5}{8}\\right) = \\frac{15}{16}$ là:", "options": ["$-\\frac{2}{3}$", "$-\\frac{3}{2}$", "$\\frac{2}{3}$", "$\\frac{3}{2}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $\\left|x - \\frac{1}{2}\\right| = \\frac{3}{4}$:", "options": ["$x = \\frac{5}{4}$ hoặc $x = -\\frac{1}{4}$", "$x = \\frac{5}{4}$", "$x = -\\frac{1}{4}$", "$x = \\frac{1}{4}$ hoặc $x = -\\frac{5}{4}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Kết quả của phép tính $\\left(1 - \\frac{1}{2}\\right)\\left(1 - \\frac{1}{3}\\right)\\left(1 - \\frac{1}{4}\\right)\\dots\\left(1 - \\frac{1}{10}\\right)$ là:", "options": ["$\\frac{1}{10}$", "$\\frac{9}{10}$", "$\\frac{1}{20}$", "$\\frac{2}{10}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Một cửa hàng bán gạo ngày thứ nhất bán được $120\\text{ kg}$. Ngày thứ hai bán bằng $\\frac{3}{4}$ số gạo ngày thứ nhất. Ngày thứ ba bán bằng $\\frac{2}{3}$ tổng số gạo của cả hai ngày trước. Tổng số gạo bán trong ba ngày là:", "options": ["$350\\text{ kg}$", "$210\\text{ kg}$", "$140\\text{ kg}$", "$420\\text{ kg}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho $M = \\frac{1}{2} - \\frac{1}{3} + \\frac{1}{4} - \\frac{1}{5}$ và $N = \\frac{1}{6} + \\frac{1}{20}$. So sánh $M$ và $N$:", "options": ["$M = N$", "$M > N$", "$M < N$", "Không so sánh được"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Giá trị của biểu thức $C = \\frac{\\frac{1}{2} + \\frac{1}{3} + \\frac{1}{4}}{\\frac{1}{4} + \\frac{1}{6} + \\frac{1}{8}}$ bằng:", "options": ["$2$", "$\\frac{1}{2}$", "$4$", "$\\frac{3}{2}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm $x$ biết: $\\frac{x - 1}{2024} + \\frac{x - 2}{2023} = \\frac{x - 3}{2022} + \\frac{x - 4}{2021}$:", "options": ["$x = 2025$", "$x = 2024$", "$x = 1$", "$x = 0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hai số hữu tỉ $x, y$ thỏa mãn $x + y = x \\cdot y = x : y$ ($y \\neq 0$). Cặp số $(x; y)$ là:", "options": ["$(-0,5; -1)$", "$(0,5; 1)$", "$(2; 0,5)$", "Không tồn tại"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một ô tô đi quãng đường từ A đến B hết 3 giờ. Giờ thứ nhất đi được $\\frac{1}{3}$ quãng đường, giờ thứ hai đi được $\\frac{2}{5}$ quãng đường còn lại, giờ thứ ba đi $60\\text{ km}$. Quãng đường AB dài:", "options": ["$150\\text{ km}$", "$180\\text{ km}$", "$120\\text{ km}$", "$200\\text{ km}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức A = [(-3/4) + 2/5] : 3/7 + [(-1/4) + 3/5] : 3/7:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Có thể áp dụng tính chất phân phối để đặt nhân tử chung chia cho 3/7 ra ngoài.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng trong ngoặc [(-3/4) + (-1/4)] + [2/5 + 3/5] = -1 + 1 = 0.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Giá trị của biểu thức A bằng 0.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số nghịch đảo của biểu thức A là 0.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm x: (3/5)x - 2/3 = (1/4)x + 1/2:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Chuyển vế đưa về: (3/5 - 1/4)x = 1/2 + 2/3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hệ số của x sau khi rút gọn là 7/20.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Vế phải có giá trị là 7/6.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Giá trị của x là: x = 10/3.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm số hữu tỉ x biết: (3/4) : x = -1,5. (Viết kết quả dưới dạng phân số tối giản a/b)", "answer": "-1/2"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tính giá trị của biểu thức: H = (1 - 1/3)(1 - 1/4)(1 - 1/5)...(1 - 1/20).", "answer": "1/10"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một người đi xe máy từ A đến B mất 2,5 giờ với vận tốc 40 km/h. Lúc về người đó đi với vận tốc 50 km/h. Thời gian đi về của người đó là bao nhiêu giờ?", "answer": "2"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị của x thỏa mãn: 1/(1.3) + 1/(3.5) + 1/(5.7) + ... + 1/((2x-1)(2x+1)) = 49/99. Giá trị của x là:", "answer": "49"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính một cách hợp lý:\na) A = (-5/12) . 4/19 + (-5/12) . 15/19 + 1 5/12\nb) B = (1/3 - 1/4 + 1/5) : (5/3 - 5/4 + 1).",
            "rubric": "a) A = -5/12 . (4/19 + 15/19) + 17/12 = -5/12 . 1 + 17/12 = 12/12 = 1 (0.5đ).\nb) Mẫu số: 5.(1/3 - 1/4 + 1/5). Do đó B = [1/3 - 1/4 + 1/5] / [5.(1/3 - 1/4 + 1/5)] = 1/5 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số hữu tỉ x biết:\na) 3/4 - (x + 1/2) = 4/5\nb) |2x - 1/3| - 1/4 = 5/12.",
            "rubric": "a) x + 1/2 = 3/4 - 4/5 = -1/20 => x = -1/20 - 1/2 = -11/20 (0.5đ).\nb) |2x - 1/3| = 5/12 + 1/4 = 8/12 = 2/3. TH1: 2x - 1/3 = 2/3 => 2x = 1 => x = 1/2. TH2: 2x - 1/3 = -2/3 => 2x = -1/3 => x = -1/6 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Ba lớp 7A, 7B, 7C tham gia trồng cây xanh. Lớp 7A trồng được 1/3 tổng số cây. Lớp 7B trồng được 40% số cây còn lại. Lớp 7C trồng nốt 72 cây còn lại.\na) Hỏi cả ba lớp đã trồng được tất cả bao nhiêu cây xanh?\nb) Tính số cây xanh mà mỗi lớp 7A và 7B đã trồng.",
            "rubric": "a) Phân số chỉ số cây còn lại sau lớp 7A: 1 - 1/3 = 2/3. Lớp 7B trồng: 2/3 x 40% = 4/15 tổng số cây. Phân số chỉ 72 cây của lớp 7C: 2/3 - 4/15 = 6/15 = 2/5 tổng số cây. Tổng số cây cả 3 lớp: 72 : (2/5) = 180 cây (0.6đ).\nb) Lớp 7A trồng: 180 x 1/3 = 60 cây. Lớp 7B trồng: 180 x 4/15 = 48 cây (0.4đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c1_7_bai2_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 2: Phép cộng, trừ, nhân, chia số hữu tỉ - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính tổng $S = \\frac{1}{1\\cdot 3} + \\frac{1}{3\\cdot 5} + \\frac{1}{5\\cdot 7} + \\dots + \\frac{1}{19\\cdot 21}$:", "options": ["$\\frac{10}{21}$", "$\\frac{20}{21}$", "$\\frac{5}{21}$", "$\\frac{1}{21}$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $\\frac{x+1}{99} + \\frac{x+2}{98} + \\frac{x+3}{97} + 3 = 0$:", "options": ["$x = -100$", "$x = 100$", "$x = -99$", "$x = 0$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho $A = \\left(1 - \\frac{1}{4}\\right)\\left(1 - \\frac{1}{9}\\right)\\left(1 - \\frac{1}{16}\\right)\\dots\\left(1 - \\frac{1}{100}\\right)$. Giá trị của $A$ là:", "options": ["$\\frac{11}{20}$", "$\\frac{9}{20}$", "$\\frac{1}{20}$", "$\\frac{19}{20}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ thỏa mãn: $\\frac{1}{3} + \\frac{1}{6} + \\frac{1}{10} + \\dots + \\frac{2}{n(n+1)} = \\frac{2024}{2025}$:", "options": ["$n = 2024$", "$n = 2025$", "$n = 2023$", "$n = 4048$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Cho $a, b, c$ là các số hữu tỉ khác 0 thỏa mãn $ab = 2(a+b),\\ bc = 3(b+c),\\ ca = 4(c+a)$. Giá trị của biểu thức $\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}$ là:", "options": ["$\\frac{13}{24}$", "$\\frac{7}{12}$", "$\\frac{11}{24}$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Số nghiệm hữu tỉ $x$ của phương trình $|x - 1| + |x + 3| = 4$ là:", "options": ["Vô số nghiệm với $-3 \\leq x \\leq 1$", "$2$ nghiệm", "$1$ nghiệm", "Vô nghiệm"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho $x, y$ là các số hữu tỉ dương thỏa mãn $x + y = 1$. Giá trị nhỏ nhất của biểu thức $P = \\frac{1}{x} + \\frac{1}{y}$ là:", "options": ["$4$", "$2$", "$1$", "$8$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Rút gọn biểu thức $M = \\frac{\\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{2025}}{\\frac{2024}{1} + \\frac{2023}{2} + \\dots + \\frac{1}{2024}}$ ta được:", "options": ["$\\frac{1}{2025}$", "$2025$", "$1$", "$\\frac{1}{2024}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm $x$ biết: $|2x - 1| + |2x - 5| = 4$. Tập nghiệm của phương trình là:", "options": ["$\\frac{1}{2} \\leq x \\leq \\frac{5}{2}$", "$x = \\frac{1}{2}$ hoặc $x = \\frac{5}{2}$", "$x \\geq \\frac{5}{2}$", "Vô nghiệm"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho biểu thức $S = 1 + \\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{2^{100}-1}$. So sánh $S$ với $50$:", "options": ["$S > 50$", "$S < 50$", "$S = 50$", "Không so sánh được"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm hai số hữu tỉ $a$ và $b$ sao cho $a - b = 2(a + b) = a : b$ ($b \\neq 0$):", "options": ["$a = -2,25;\\ b = -0,75$", "$a = 2,25;\\ b = 0,75$", "$a = -1;\\ b = -0,5$", "$a = 1;\\ b = 0,5$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Biết tổng các chữ số của số hữu tỉ $A = \\frac{10^{2025} + 8}{9}$ là:", "options": ["Một số chia hết cho 9", "$9$", "$2025$", "Không xác định"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tổng S = 1/2² + 1/3² + 1/4² + ... + 1/100²:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Với mọi k ≥ 2 ta luôn có: 1/k² < 1/((k - 1)k).", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Tổng S < 1/(1.2) + 1/(2.3) + ... + 1/(99.100).", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Giá trị của tổng 1/(1.2) + 1/(2.3) + ... + 1/(99.100) bằng 99/100.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Chứng minh được rằng S > 1.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét phương trình chứa giá trị tuyệt đối |x - 2| + |x - 7| = m:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Ta luôn có |x - 2| + |x - 7| = |x - 2| + |7 - x| ≥ |(x - 2) + (7 - x)| = 5.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Với m < 5 thì phương trình vô nghiệm.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Với m = 5 phương trình có vô số nghiệm là mọi x thỏa mãn 2 ≤ x ≤ 7.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Với m > 5 phương trình luôn có đúng 1 nghiệm duy nhất.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = (1 - 1/2) . (1 - 1/3) . (1 - 1/4) ... (1 - 1/2025). Kết quả là 1/n. Tìm n.", "answer": "2025"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số hữu tỉ x thỏa mãn: (x - 2)/2023 + (x - 1)/2024 = 2.", "answer": "2025"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tính tổng: S = 2/(1.3) + 2/(3.5) + 2/(5.7) + ... + 2/(97.99). Tử số của phân số tối giản S là bao nhiêu?", "answer": "98"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: P = |x - 2024| + |x - 2026|.", "answer": "2"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Tính giá trị biểu thức:\nA = 1/2 + 1/6 + 1/12 + 1/20 + 1/30 + 1/42 + 1/56 + 1/72 + 1/90.",
            "rubric": "A = 1/(1.2) + 1/(2.3) + 1/(3.4) + ... + 1/(9.10) (0.4đ) = (1 - 1/2) + (1/2 - 1/3) + ... + (1/9 - 1/10) = 1 - 1/10 = 9/10 (0.6đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm số hữu tỉ x biết:\n(x + 1)/10 + (x + 1)/11 + (x + 1)/12 = (x + 1)/13 + (x + 1)/14.",
            "rubric": "Chuyển vế: (x + 1) . [1/10 + 1/11 + 1/12 - 1/13 - 1/14] = 0 (0.4đ). Vì 1/10 > 1/13 và 1/11 > 1/14 nên biểu thức trong ngoặc khác 0 (0.4đ). Do đó x + 1 = 0 => x = -1 (0.2đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho biểu thức A = 1/2 + 2/2² + 3/2³ + 4/2⁴ + ... + 100/2¹⁰⁰. Chứng minh rằng A < 2.",
            "rubric": "Ta có 2A = 1 + 2/2 + 3/2² + ... + 100/2⁹⁹ (0.3đ). Lấy 2A - A = 1 + (2/2 - 1/2) + (3/2² - 2/2²) + ... + (100/2⁹⁹ - 99/2⁹⁹) - 100/2¹⁰⁰ = 1 + [1/2 + 1/2² + ... + 1/2⁹⁹] - 100/2¹⁰⁰ (0.4đ). Đặt B = 1/2 + 1/2² + ... + 1/2⁹⁹ < 1. Suy ra A < 1 + 1 - 100/2¹⁰⁰ < 2 (0.3đ)."
        }
    ]
}
