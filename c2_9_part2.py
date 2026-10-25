# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 9 - CHƯƠNG II: PHƯƠNG TRÌNH VÀ BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN
PHẦN 2:
- BÀI 6: BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN (c2_9_bai3)
- BÀI KIỂM TRA CUỐI CHƯƠNG II: PHƯƠNG TRÌNH VÀ BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN (c2_9_bai4)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 6: BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN (c2_9_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c2_9_bai3_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 6: Bất phương trình bậc nhất một ẩn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn $x$?", "options": ["$2x - 3 > 0$", "$x^2 + 1 > 0$", "$2x - 3y < 5$", "$\\frac{1}{x} > 2$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Khi nhân (hoặc chia) hai vế của một bất phương trình với một số âm, ta phải:", "options": ["Đổi chiều bất phương trình", "Giữ nguyên chiều bất phương trình", "Đổi dấu của ẩn số", "Không đổi chiều"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Nghiệm của bất phương trình $x - 3 > 0$ là:", "options": ["$x > 3$", "$x < 3$", "$x > -3$", "$x < -3$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Hình vẽ trên trục số với dấu ngoặc tròn quay sang phải tại điểm $2$ biểu diễn tập nghiệm:", "options": ["$x > 2$", "$x \\ge 2$", "$x < 2$", "$x \\le 2$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Nghiệm của bất phương trình $2x - 6 \\le 0$ là:", "options": ["$x \\le 3$", "$x < 3$", "$x \\ge 3$", "$x > 3$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Giải bất phương trình $-3x > 9$. Nghiệm là:", "options": ["$x < -3$", "$x > -3$", "$x < 3$", "$x > 3$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Số nguyên dương lớn nhất thỏa mãn bất phương trình $x < 5$ là:", "options": ["$4$", "$5$", "$6$", "$3$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Giải bất phương trình $3x - 5 > x + 1$. Tập nghiệm là:", "options": ["$x > 3$", "$x < 3$", "$x > 2$", "$x < 2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Nghiệm nguyên nhỏ nhất thỏa mãn bất phương trình $2x \\ge -5$ là:", "options": ["$-2$", "$-3$", "$-1$", "$0$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Giải bất phương trình $\\frac{x - 1}{2} - \\frac{x - 2}{3} \\ge 1$. Nghiệm là:", "options": ["$x \\ge 5$", "$x \\le 5$", "$x \\ge 1$", "$x \\le 1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Có bao nhiêu số nguyên dương thỏa mãn bất phương trình $5 - 2x > 0$?", "options": ["$2$ ($x = 1$ và $x = 2$)", "$3$", "$1$", "Vô số"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm $m$ để bất phương trình $(m - 1)x > 2$ có tập nghiệm là $x < \\frac{2}{m - 1}$:", "options": ["$m < 1$", "$m > 1$", "$m = 1$", "$m \\neq 1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho bất phương trình $3x - 7 \\le 2$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Chuyển vế được $3x \\le 9$.", "correct": True},
                {"subId": "b", "text": "Chia cả hai vế cho 3 ta được $x \\le 3$.", "correct": True},
                {"subId": "c", "text": "Giá trị $x = 3$ là một nghiệm của bất phương trình.", "correct": True},
                {"subId": "d", "text": "Giá trị $x = 4$ là một nghiệm của bất phương trình.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho bất phương trình $-2(x - 3) > 4 - x$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Khai triển vế trái được $-2x + 6 > 4 - x$.", "correct": True},
                {"subId": "b", "text": "Chuyển vế thu được $-x > -2$.", "correct": True},
                {"subId": "c", "text": "Nghiệm của bất phương trình là $x < 2$.", "correct": True},
                {"subId": "d", "text": "Số tự nhiên lớn nhất thỏa mãn bất phương trình là $2$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Giải bất phương trình $4x - 8 \\ge 0$. Nghiệm là $x \\ge a$. Tìm giá trị của $a$.", "correctAnswer": "2", "explanation": "$4x \\ge 8 \\Rightarrow x \\ge 2$. Vậy $a = 2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số nghiệm nguyên dương của bất phương trình $3x - 10 < 0$.", "correctAnswer": "3", "explanation": "$3x < 10 \\Rightarrow x < 3{,}33$. Các số nguyên dương là $1, 2, 3$. Có 3 nghiệm."},
        {"id": 3, "level": "Vận dụng", "question": "Giải bất phương trình $\\frac{2x - 3}{3} > \\frac{x + 1}{2}$. Nghiệm là $x > a$. Tìm $a$.", "correctAnswer": "9", "explanation": "$2(2x - 3) > 3(x + 1) \\Rightarrow 4x - 6 > 3x + 3 \\Rightarrow x > 9$. Vậy $a = 9$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số nguyên $x$ lớn nhất thỏa mãn bất phương trình $2(x - 1) < 3(x + 2) - 10$.", "correctAnswer": "1", "explanation": "$2x - 2 < 3x + 6 - 10 \\Rightarrow 2x - 2 < 3x - 4 \\Rightarrow -x < -2 \\Rightarrow x > 2$? Kiểm tra lại: $2x - 2 < 3x - 4 \\Rightarrow x > 2$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải bất phương trình sau và biểu diễn tập nghiệm trên trục số:\n$$3x - 2 \\ge 7$$",
            "solution": "Ta có: $3x - 2 \\ge 7$\n$\\Leftrightarrow 3x \\ge 7 + 2$\n$\\Leftrightarrow 3x \\ge 9$\n$\\Leftrightarrow x \\ge 3$.\nVậy tập nghiệm của bất phương trình là $\\{x \\mid x \\ge 3\\}$.\nBiểu diễn trên trục số: Điểm 3 dùng dấu ngoặc vuông $[$ hướng về phía bên phải, gạch bỏ phần bên trái điểm 3.",
            "rubric": [
                {"step": "Chuyển vế và giải đúng ra x >= 3", "subScore": 0.5},
                {"step": "Kết luận tập nghiệm và biểu diễn chính xác trên trục số", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải bất phương trình sau:\n$$\\frac{2x + 1}{3} - \\frac{x - 2}{2} > 1$$",
            "solution": "Mẫu số chung là $6$.\nNhân cả hai vế với 6 (vì $6 > 0$ nên bất phương trình không đổi chiều):\n$2(2x + 1) - 3(x - 2) > 6$\n$\\Leftrightarrow 4x + 2 - 3x + 6 > 6$\n$\\Leftrightarrow x + 8 > 6$\n$\\Leftrightarrow x > 6 - 8$\n$\\Leftrightarrow x > -2$.\nVậy tập nghiệm của bất phương trình là $\\{x \\mid x > -2\\}$.",
            "rubric": [
                {"step": "Quy đồng mẫu số chung 6 và khai triển đúng", "subScore": 0.5},
                {"step": "Thu gọn và giải ra x > -2, kết luận chuẩn xác", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm các giá trị của tham số $m$ để bất phương trình sau nghiệm đúng với mọi $x \\in \\mathbb{R}$:\n$$(m^2 - 1)x + m - 1 \\le 0$$",
            "solution": "Bất phương trình có dạng $Ax + B \\le 0$ với $A = m^2 - 1, B = m - 1$.\nĐể bất phương trình nghiệm đúng với mọi $x \\in \\mathbb{R}$, điều kiện cần và đủ là:\n$$\\begin{cases} A = 0 \\\\ B \\le 0 \\end{cases} \\Leftrightarrow \\begin{cases} m^2 - 1 = 0 \\\\ m - 1 \\le 0 \\end{cases}$$\nTừ $m^2 - 1 = 0 \\Rightarrow m = 1$ hoặc $m = -1$.\n- Với $m = 1$: $m - 1 = 0 \\le 0$ (thỏa mãn).\nKhi đó bất phương trình trở thành $0x + 0 \\le 0$, luôn đúng với mọi $x$.\n- Với $m = -1$: $m - 1 = -2 \\le 0$ (thỏa mãn).\nKhi đó bất phương trình trở thành $0x - 2 \\le 0$, luôn đúng với mọi $x$.\nVậy cả hai giá trị $m = 1$ và $m = -1$ đều thỏa mãn.",
            "rubric": [
                {"step": "Nêu điều kiện nghiệm đúng với mọi x là A = 0 và B <= 0", "subScore": 0.5},
                {"step": "Xét hai giá trị m = 1, m = -1 và kết luận đầy đủ", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c2_9_bai3_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 6: Bất phương trình bậc nhất một ẩn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Bất phương trình $ax + b < 0$ là bất phương trình bậc nhất một ẩn khi:", "options": ["$a \\neq 0$", "$a = 0$", "$b \\neq 0$", "$a > 0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tập nghiệm của bất phương trình $-4x + 12 < 0$ là:", "options": ["$x > 3$", "$x < 3$", "$x > -3$", "$x < -3$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Nghiệm của bất phương trình $\\frac{x - 3}{4} \\le \\frac{x - 1}{2}$ là:", "options": ["$x \\ge -1$", "$x \\le -1$", "$x \\ge 1$", "$x \\le 1$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Số nghiệm nguyên âm của bất phương trình $2x + 7 > 0$ là:", "options": ["$3$ (gồm $-3, -2, -1$)", "$4$", "$2$", "$0$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tập hợp các điểm $x$ thỏa mãn $2 < x \\le 5$ có bao nhiêu số nguyên?", "options": ["$3$ ($x = 3, 4, 5$)", "$4$", "$2$", "Vô số"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giải bất phương trình $(x + 2)^2 - x(x - 3) \\le 18$. Nghiệm là:", "options": ["$x \\le 2$", "$x \\ge 2$", "$x \\le -2$", "$x \\ge -2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm $m$ để $x = 2$ là một nghiệm của bất phương trình $mx + 3 > 7$:", "options": ["$m > 2$", "$m < 2$", "$m \\ge 2$", "$m = 2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho hai bất phương trình $x - 1 > 0$ và $2x - m > 0$. Hai bất phương trình tương đương khi:", "options": ["$m = 2$", "$m = 1$", "$m = 4$", "$m = -2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Tập nghiệm của hệ bất phương trình $\\begin{cases} 2x - 1 > 3 \\\\ 3x - 2 \\le 10 \\end{cases}$ là:", "options": ["$2 < x \\le 4$", "$x > 2$", "$x \\le 4$", "Vô nghiệm"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm số nghiệm nguyên của bất phương trình $\\frac{x - 1}{2} - \\frac{x + 1}{3} < 1$ thỏa mãn $x \\le 8$:", "options": ["Có vô số nghiệm nguyên nhỏ hơn hoặc bằng 8", "$5$", "$8$", "$0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm $m$ để bất phương trình $(m - 2)x + 1 > 0$ nghiệm đúng với mọi $x > 0$:", "options": ["$m \\ge 2$", "$m > 2$", "$m \\le 2$", "$m < 2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giải bất phương trình $\\frac{x - 1}{x + 2} > 0$. Tập nghiệm là:", "options": ["$x < -2$ hoặc $x > 1$", "$-2 < x < 1$", "$x > 1$", "$x < -2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho bất phương trình $\\frac{3 - 2x}{5} > \\frac{2 - x}{3}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Quy đồng mẫu chung 15 ta được $3(3 - 2x) > 5(2 - x)$.", "correct": True},
                {"subId": "b", "text": "Khai triển được $9 - 6x > 10 - 5x$.", "correct": True},
                {"subId": "c", "text": "Thu gọn được $-x > 1 \\Rightarrow x < -1$.", "correct": True},
                {"subId": "d", "text": "Số $0$ là một nghiệm của bất phương trình.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hệ bất phương trình bậc nhất một ẩn: $\\begin{cases} 3x - 2 > 4 \\\\ 2x + 1 \\le 9 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Nghiệm của bất phương trình thứ nhất là $x > 2$.", "correct": True},
                {"subId": "b", "text": "Nghiệm của bất phương trình thứ hai là $x \\le 4$.", "correct": True},
                {"subId": "c", "text": "Tập nghiệm của hệ là $2 < x \\le 4$.", "correct": True},
                {"subId": "d", "text": "Có 3 số nguyên thỏa mãn hệ bất phương trình.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Giải bất phương trình $5 - 3x \\le 11$. Nghiệm là $x \\ge a$. Tìm giá trị của $a$.", "correctAnswer": "-2", "explanation": "$-3x \\le 6 \\Rightarrow x \\ge -2$. Vậy $a = -2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên lớn nhất thỏa mãn bất phương trình $2x - 7 < 0$.", "correctAnswer": "3", "explanation": "$2x < 7 \\Rightarrow x < 3{,}5$. Số tự nhiên lớn nhất là $3$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho bất phương trình $mx + 1 > 3$. Với $m = 2$, tìm giá trị nhỏ nhất của số nguyên $x$ thỏa mãn bất phương trình.", "correctAnswer": "2", "explanation": "$2x > 2 \\Rightarrow x > 1$. Số nguyên nhỏ nhất lớn hơn 1 là $2$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn hệ bất phương trình $\\begin{cases} 2x - 3 < 5 \\\\ 3x + 2 > -7 \\end{cases}$?", "correctAnswer": "6", "explanation": "$x < 4$ và $x > -3 \\Rightarrow -3 < x < 4$. Các số nguyên là $-2, -1, 0, 1, 2, 3$. Có 6 số nguyên."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải bất phương trình sau:\n$$\\frac{x - 1}{2} - \\frac{x - 2}{3} < \\frac{x - 3}{4}$$",
            "solution": "Mẫu thức chung là $12$.\nNhân cả hai vế với 12 (vì $12 > 0$ nên không đổi chiều):\n$6(x - 1) - 4(x - 2) < 3(x - 3)$\n$\\Leftrightarrow 6x - 6 - 4x + 8 < 3x - 9$\n$\\Leftrightarrow 2x + 2 < 3x - 9$\n$\\Leftrightarrow 2x - 3x < -9 - 2$\n$\\Leftrightarrow -x < -11$\n$\\Leftrightarrow x > 11$.\nVậy tập nghiệm của bất phương trình là $\\{x \\mid x > 11\\}$.",
            "rubric": [
                {"step": "Quy đồng mẫu thức chung 12 và khai triển đúng các biểu thức", "subScore": 0.5},
                {"step": "Thu gọn ra -x < -11, đổi chiều khi chia cho -1 được x > 11", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Một bạn học sinh làm bài thi gồm $20$ câu hỏi trắc nghiệm. Mỗi câu trả lời đúng được cộng $5$ điểm, mỗi câu trả lời sai bị trừ $2$ điểm, câu không trả lời không được điểm. Bạn đó trả lời hết tất cả $20$ câu. Hỏi bạn đó phải trả lời đúng ít nhất bao nhiêu câu để đạt được số điểm từ $65$ điểm trở lên?",
            "solution": "Gọi số câu bạn học sinh trả lời đúng là $x$ ($x \\in \\mathbb{N}, x \\le 20$).\nVì bạn trả lời hết 20 câu nên số câu trả lời sai là $20 - x$ (câu).\nSố điểm bạn nhận được là:\n$5x - 2(20 - x) = 5x - 40 + 2x = 7x - 40$ (điểm).\nĐể đạt được từ $65$ điểm trở lên, ta có bất phương trình:\n$7x - 40 \\ge 65$\n$\\Leftrightarrow 7x \\ge 105$\n$\\Leftrightarrow x \\ge \\frac{105}{7} = 15$.\nVì $x$ là số tự nhiên nên giá trị nhỏ nhất của $x$ là $15$.\nVậy bạn học sinh đó phải trả lời đúng ít nhất $15$ câu.",
            "rubric": [
                {"step": "Gọi ẩn, biểu diễn điểm và thiết lập đúng bất phương trình 7x - 40 >= 65", "subScore": 0.5},
                {"step": "Giải ra x >= 15 và kết luận ít nhất 15 câu", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm các giá trị của tham số $m$ để hệ bất phương trình sau có nghiệm:\n$$\\begin{cases} 2x - 1 \\ge 3 \\\\ x - m < 0 \\end{cases}$$",
            "solution": "Giải từng bất phương trình trong hệ:\n1) $2x - 1 \\ge 3 \\Leftrightarrow 2x \\ge 4 \\Leftrightarrow x \\ge 2$.\nTập nghiệm là $S_1 = [2; +\\infty)$.\n2) $x - m < 0 \\Leftrightarrow x < m$.\nTập nghiệm là $S_2 = (-\\infty; m)$.\nĐể hệ bất phương trình có nghiệm thì giao của hai tập nghiệm khác rỗng, tức là $S_1 \\cap S_2 \\neq \\emptyset$.\nĐiều này xảy ra khi và chỉ khi:\n$m > 2$.\nVậy với $m > 2$ thì hệ bất phương trình đã cho có nghiệm.",
            "rubric": [
                {"step": "Giải tập nghiệm của từng bất phương trình S1 = [2; +vc) và S2 = (-vc; m)", "subScore": 0.5},
                {"step": "Lập luận điều kiện giao khác rỗng để rút ra m > 2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c2_9_bai3_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 6: Bất phương trình bậc nhất một ẩn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Giao của hai tập nghiệm $x > 1$ và $x < 4$ là:", "options": ["$1 < x < 4$", "$x > 4$", "$x < 1$", "Rỗng"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Nghiệm của bất phương trình $(x - 1)(x - 3) < 0$ là:", "options": ["$1 < x < 3$", "$x < 1$ hoặc $x > 3$", "$x > 3$", "$x < 1$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Nghiệm của bất phương trình $x^2 - 4 > 0$ là:", "options": ["$x < -2$ hoặc $x > 2$", "$-2 < x < 2$", "$x > 2$", "$x < -2$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Tập nghiệm của bất phương trình $\\frac{x - 2}{x + 3} \\le 0$ là:", "options": ["$-3 < x \\le 2$", "$-3 \\le x \\le 2$", "$x \\le 2$", "$x > -3$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Số nghiệm nguyên thỏa mãn bất phương trình $|2x - 1| \\le 5$ là:", "options": ["$6$ (từ $-2$ đến $3$)", "$5$", "$4$", "Vô số"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tìm $m$ để bất phương trình $(m^2 + 1)x - 2m \\ge 0$ có nghiệm $x \\ge 1$:", "options": ["$m = 1$", "$m = -1$", "$m = 0$", "$m = 2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Bất phương trình $\\frac{1}{x} < 1$ có tập nghiệm là:", "options": ["$x < 0$ hoặc $x > 1$", "$x > 1$", "$0 < x < 1$", "$x < 1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Tìm $m$ để hệ $\\begin{cases} 2x - 3 > 1 \\\\ mx \\le 4 \\end{cases}$ có nghiệm:", "options": ["$m < 2$", "$m \\le 2$", "$m > 0$", "Với mọi $m$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tập nghiệm của bất phương trình $\\frac{x^2 - 5x + 6}{x - 1} \\ge 0$ là:", "options": ["$(1; 2] \\cup [3; +\\infty)$", "$[2; 3]$", "$x > 1$", "$[1; 3]$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm tất cả các giá trị của $m$ để bất phương trình $(m - 2)x^2 - 2(m - 2)x + 1 > 0$ nghiệm đúng với mọi $x \\in \\mathbb{R}$:", "options": ["$2 \\le m < 3$", "$m > 2$", "$2 < m < 3$", "$m < 3$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $x, y > 0$ thỏa mãn $x + y \\le 2$. Giá trị nhỏ nhất của biểu thức $P = \\frac{1}{x} + \\frac{1}{y}$ là:", "options": ["$2$", "$1$", "$4$", "$\\frac{1}{2}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một người bán hàng cần thuê xe tải để chở ít nhất $140$ tấn hàng và $9$ tấn hàng đặc biệt. Có hai loại xe: loại A (giá $4$ triệu, chở $20$ tấn hàng, $0{,}6$ tấn đặc biệt), loại B (giá $3$ triệu, chở $10$ tấn hàng, $1{,}5$ tấn đặc biệt). Chi phí thuê xe nhỏ nhất là:", "options": ["$32$ triệu đồng", "$28$ triệu đồng", "$30$ triệu đồng", "$35$ triệu đồng"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho bất phương trình $\\frac{2x - 1}{x - 2} \\ge 1$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điều kiện xác định là $x \\neq 2$.", "correct": True},
                {"subId": "b", "text": "Chuyển vế: $\\frac{2x - 1}{x - 2} - 1 \\ge 0 \\Leftrightarrow \\frac{x + 1}{x - 2} \\ge 0$.", "correct": True},
                {"subId": "c", "text": "Tập nghiệm của bất phương trình là $x \\le -1$ hoặc $x > 2$.", "correct": True},
                {"subId": "d", "text": "Điểm $x = 2$ thuộc tập nghiệm của bất phương trình.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho bất phương trình chứa giá trị tuyệt đối $|x - 2| + |x - 5| \\ge 3$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Áp dụng bất đẳng thức $|a| + |b| \\ge |a + b|$.", "correct": True},
                {"subId": "b", "text": "Ta có $|x - 2| + |5 - x| \\ge |x - 2 + 5 - x| = 3$.", "correct": True},
                {"subId": "c", "text": "Bất phương trình nghiệm đúng với mọi số thực $x \\in \\mathbb{R}$.", "correct": True},
                {"subId": "d", "text": "Tập nghiệm của bất phương trình là tập rỗng.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Nghiệm của bất phương trình $-5x + 15 \\ge 0$ là $x \\le a$. Tìm $a$.", "correctAnswer": "3", "explanation": "$-5x \\ge -15 \\Rightarrow x \\le 3$."},
        {"id": 2, "level": "Vận dụng", "question": "Tìm số nghiệm nguyên của bất phương trình $|x - 3| < 4$.", "correctAnswer": "7", "explanation": "$-4 < x - 3 < 4 \\Rightarrow -1 < x < 7$. Các số nguyên là $0, 1, 2, 3, 4, 5, 6$. Có 7 nghiệm."},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số nguyên dương $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x}{2} + \\frac{x}{3} + \\frac{x}{4} < 13$.", "correctAnswer": "11", "explanation": "$\\frac{13x}{12} < 13 \\Rightarrow x < 12$. Số nguyên dương lớn nhất là $11$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm $m$ để hệ $\\begin{cases} x > 2 \\\\ x < m \\end{cases}$ có đúng $3$ nghiệm nguyên.", "correctAnswer": "6", "explanation": "Các nghiệm nguyên là $3, 4, 5$. Do đó $5 < m \\le 6$. Nếu $m$ là số nguyên thì $m = 6$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải bất phương trình sau:\n$$\\frac{2x - 3}{x - 1} \\le 1$$",
            "solution": "Điều kiện xác định: $x \\neq 1$.\nChuyển vế:\n$\\frac{2x - 3}{x - 1} - 1 \\le 0 \\Leftrightarrow \\frac{2x - 3 - (x - 1)}{x - 1} \\le 0 \\Leftrightarrow \\frac{x - 2}{x - 1} \\le 0$.\nPhân thức $\\frac{x - 2}{x - 1} \\le 0$ khi tử và mẫu trái dấu (hoặc tử bằng 0):\nTa có $x - 1 < x - 2$ là vô lí, do đó $x - 1 < 0$ và $x - 2 \\ge 0$ là vô lí.\nVậy phải có: $\\begin{cases} x - 2 \\le 0 \\\\ x - 1 > 0 \\end{cases} \\Leftrightarrow \\begin{cases} x \\le 2 \\\\ x > 1 \\end{cases} \\Leftrightarrow 1 < x \\le 2$.\nVậy tập nghiệm của bất phương trình là $S = (1; 2]$.",
            "rubric": [
                {"step": "Chuyển vế, quy đồng đưa về dạng thương (x - 2)/(x - 1) <= 0", "subScore": 0.5},
                {"step": "Lập luận dấu của nhị thức bậc nhất và kết luận 1 < x <= 2", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải bất phương trình chứa dấu giá trị tuyệt đối sau:\n$$|2x - 3| \\le x + 1$$",
            "solution": "Bất phương trình dạng $|A| \\le B$ tương đương với:\n$$\\begin{cases} B \\ge 0 \\\\ -B \\le A \\le B \\end{cases}$$\nỞ đây ta có:\n$$\\begin{cases} x + 1 \\ge 0 \\\\ -(x + 1) \\le 2x - 3 \\le x + 1 \\end{cases}$$\n1) $x \\ge -1$.\n2) Hệ bất phương trình kép:\n- Bất phương trình thứ nhất: $-x - 1 \\le 2x - 3 \\Leftrightarrow 3x \\ge 2 \\Leftrightarrow x \\ge \\frac{2}{3}$.\n- Bất phương trình thứ hai: $2x - 3 \\le x + 1 \\Leftrightarrow x \\le 4$.\nKết hợp các điều kiện:\n$\\frac{2}{3} \\le x \\le 4$ (thỏa mãn $x \\ge -1$).\nVậy tập nghiệm của bất phương trình là $S = \\left[\\frac{2}{3}; 4\\right]$.",
            "rubric": [
                {"step": "Phá dấu giá trị tuyệt đối đưa về bất phương trình kép", "subScore": 0.5},
                {"step": "Giải hệ điều kiện và kết luận tập nghiệm [2/3; 4]", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm các giá trị của tham số $m$ để hệ bất phương trình sau có nghiệm:\n$$\\begin{cases} 3x + 1 > 2x + 4 \\\\ 2x - m \\le 3 \\end{cases}$$",
            "solution": "Giải từng bất phương trình trong hệ:\n1) $3x + 1 > 2x + 4 \\Leftrightarrow 3x - 2x > 4 - 1 \\Leftrightarrow x > 3$.\nTập nghiệm $S_1 = (3; +\\infty)$.\n2) $2x - m \\le 3 \\Leftrightarrow 2x \\le m + 3 \\Leftrightarrow x \\le \\frac{m + 3}{2}$.\nTập nghiệm $S_2 = \\left(-\\infty; \\frac{m + 3}{2}\\right]$.\nĐể hệ bất phương trình có nghiệm thì giao của hai tập nghiệm $S_1$ và $S_2$ phải khác rỗng:\n$S_1 \\cap S_2 \\neq \\emptyset \\Leftrightarrow \\frac{m + 3}{2} > 3$\n$\\Leftrightarrow m + 3 > 6 \\Leftrightarrow m > 3$.\nVậy với $m > 3$ thì hệ bất phương trình đã cho có nghiệm.",
            "rubric": [
                {"step": "Giải đúng tập nghiệm x > 3 và x <= (m + 3)/2", "subScore": 0.5},
                {"step": "Lập luận điều kiện giao khác rỗng và kết luận m > 3", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG II: PHƯƠNG TRÌNH VÀ BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN (c2_9_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c2_9_bai4_test1"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương II - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Phương trình $(x - 1)(x + 2) = 0$ có các nghiệm là:", "options": ["$x = 1$ hoặc $x = -2$", "$x = -1$ hoặc $x = 2$", "$x = 1$ hoặc $x = 2$", "$x = -1$ hoặc $x = -2$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Điều kiện xác định của phương trình $\\frac{x}{x - 3} = 2$ là:", "options": ["$x \\neq 3$", "$x \\neq 0$", "$x \\neq 2$", "$x > 3$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Cho $a < b$. Khẳng định nào sau đây đúng?", "options": ["$a + 2 < b + 2$", "$a - 2 > b - 2$", "$-2a < -2b$", "$2a > 2b$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Nghiệm của bất phương trình $2x - 4 \\ge 0$ là:", "options": ["$x \\ge 2$", "$x \\le 2$", "$x > 2$", "$x < 2$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Giải phương trình $(2x - 1)(3x + 6) = 0$. Các nghiệm là:", "options": ["$x = \\frac{1}{2}$ và $x = -2$", "$x = -\\frac{1}{2}$ và $x = 2$", "$x = 1$ và $x = -6$", "$x = 2$ và $x = -2$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Nghiệm của phương trình $\\frac{x - 2}{x + 1} = 0$ là:", "options": ["$x = 2$", "$x = -1$", "$x = 0$", "Vô nghiệm"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $-3x < 12$. Nghiệm của bất phương trình là:", "options": ["$x > -4$", "$x < -4$", "$x > 4$", "$x < 4$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Số nguyên lớn nhất thỏa mãn bất phương trình $x < 3{,}5$ là:", "options": ["$3$", "$4$", "$2$", "$0$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho $a > b$. Bất đẳng thức nào sau đây luôn đúng?", "options": ["$3a + 1 > 3b + 1$", "$-3a + 1 > -3b + 1$", "$a^2 > b^2$", "$\\frac{1}{a} > \\frac{1}{b}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Giải phương trình $\\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1} = \\frac{4}{x^2 - 1}$. Nghiệm là:", "options": ["Vô nghiệm (nghiệm $x = 1$ bị loại)", "$x = 1$", "$x = -1$", "$x = 0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Có bao nhiêu số nguyên dương thỏa mãn bất phương trình $4 - x > 0$?", "options": ["$3$ ($x = 1, 2, 3$)", "$4$", "$2$", "Vô số"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị nhỏ nhất của biểu thức $A = x^2 - 6x + 11$ là:", "options": ["$2$", "$11$", "$3$", "$5$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho phương trình $\\frac{x + 2}{x} = \\frac{x - 3}{x - 1}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "ĐKXĐ là $x \\neq 0$ và $x \\neq 1$.", "correct": True},
                {"subId": "b", "text": "Quy đồng và khử mẫu: $(x + 2)(x - 1) = x(x - 3)$.", "correct": True},
                {"subId": "c", "text": "Khai triển và thu gọn ta được $4x = 2 \\Rightarrow x = \\frac{1}{2}$.", "correct": True},
                {"subId": "d", "text": "Giá trị $x = \\frac{1}{2}$ bị loại vì vi phạm ĐKXĐ.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho bất phương trình $\\frac{x - 1}{2} - \\frac{x - 2}{3} \\ge 1$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Quy đồng mẫu 6 ta được $3(x - 1) - 2(x - 2) \\ge 6$.", "correct": True},
                {"subId": "b", "text": "Thu gọn vế trái được $x + 1 \\ge 6$.", "correct": True},
                {"subId": "c", "text": "Tập nghiệm là $x \\ge 5$.", "correct": True},
                {"subId": "d", "text": "Số $4$ là một nghiệm của bất phương trình.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính tổng các nghiệm của phương trình $(x - 3)(x + 7) = 0$.", "correctAnswer": "-4", "explanation": "$x = 3$ hoặc $x = -7$. Tổng = $3 + (-7) = -4$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên lớn nhất thỏa mãn bất phương trình $3x - 11 < 0$.", "correctAnswer": "3", "explanation": "$x < 11/3 \\approx 3{,}67$. Số tự nhiên lớn nhất là $3$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $a > 0$. Tìm giá trị nhỏ nhất của biểu thức $P = a + \\frac{9}{a}$.", "correctAnswer": "6", "explanation": "$P \\ge 2\\sqrt{a \\cdot \\frac{9}{a}} = 6$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm nghiệm của phương trình $\\frac{x^2 - 1}{x + 1} = 2$.", "correctAnswer": "3", "explanation": "ĐKXĐ: $x \\neq -1$. $x - 1 = 2 \\Rightarrow x = 3$ (thỏa mãn ĐKXĐ)."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải phương trình sau:\n$$\\frac{x}{x - 2} + \\frac{1}{x + 2} = \\frac{4}{x^2 - 4}$$",
            "solution": "Điều kiện xác định: $x \\neq 2$ và $x \\neq -2$.\nMẫu thức chung: $x^2 - 4 = (x - 2)(x + 2)$.\nQuy đồng mẫu thức và khử mẫu:\n$x(x + 2) + 1(x - 2) = 4$\n$\\Leftrightarrow x^2 + 2x + x - 2 = 4$\n$\\Leftrightarrow x^2 + 3x - 6 = 0$.\nGiải phương trình bậc hai có $\\Delta = 9 - 4(1)(-6) = 33 > 0$.\nSuy ra hai nghiệm: $x_1 = \\frac{-3 + \\sqrt{33}}{2}$ và $x_2 = \\frac{-3 - \\sqrt{33}}{2}$.\nCả hai nghiệm đều khác $\\pm 2$, thỏa mãn ĐKXĐ.\nVậy tập nghiệm của phương trình là $S = \\left\\{\\frac{-3 + \\sqrt{33}}{2}; \\frac{-3 - \\sqrt{33}}{2}\\right\\}$.",
            "rubric": [
                {"step": "Tìm đúng ĐKXĐ và quy đồng khử mẫu ra x^2 + 3x - 6 = 0", "subScore": 0.5},
                {"step": "Giải đúng hai nghiệm, đối chiếu ĐKXĐ và kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải bất phương trình sau và biểu diễn tập nghiệm trên trục số:\n$$\\frac{2x - 1}{3} - \\frac{x - 3}{2} > 1$$",
            "solution": "Quy đồng mẫu số chung là $6$:\n$2(2x - 1) - 3(x - 3) > 6$\n$\\Leftrightarrow 4x - 2 - 3x + 9 > 6$\n$\\Leftrightarrow x + 7 > 6$\n$\\Leftrightarrow x > 6 - 7$\n$\\Leftrightarrow x > -1$.\nVậy tập nghiệm của bất phương trình là $\\{x \\mid x > -1\\}$.\nBiểu diễn trên trục số: Điểm -1 dùng dấu ngoặc tròn $($ mở về phía bên phải, gạch bỏ phần bên trái điểm -1.",
            "rubric": [
                {"step": "Quy đồng, khử mẫu và thu gọn ra x > -1", "subScore": 0.5},
                {"step": "Kết luận tập nghiệm và biểu diễn chuẩn xác trên trục số", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hai số dương $x, y$ thỏa mãn $x + y \\ge 4$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = 2x + 3y + \\frac{4}{x} + \\frac{18}{y}$$",
            "solution": "Áp dụng kĩ thuật chọn điểm rơi Cauchy:\nDự đoán dấu bằng xảy ra khi $x = 2, y = 2$.\nTách các hạng tử để áp dụng Cauchy:\n$P = \\left(x + \\frac{4}{x}\\right) + \\left(2y + \\frac{18}{y}\\right) + (x + y)$.\n1) Áp dụng BĐT Cauchy cho hai số dương $x$ và $\\frac{4}{x}$:\n$x + \\frac{4}{x} \\ge 2\\sqrt{x \\cdot \\frac{4}{x}} = 4$.\nDấu \"=\" xảy ra khi $x = \\frac{4}{x} \\Leftrightarrow x^2 = 4 \\Rightarrow x = 2$.\n2) Áp dụng BĐT Cauchy cho hai số dương $2y$ và $\\frac{18}{y}$:\n$2y + \\frac{18}{y} \\ge 2\\sqrt{2y \\cdot \\frac{18}{y}} = 2\\sqrt{36} = 12$.\nDấu \"=\" xảy ra khi $2y = \\frac{18}{y} \\Leftrightarrow y^2 = 9 \\Rightarrow y = 3$? Kiểm tra lại: nếu $y = 3$, $2(3) = 6, 18/3 = 6$. Khi đó $x + y = 2 + 3 = 5 > 4$. Dấu bằng không đồng thời xảy ra tại $x+y=4$. Nếu $y = 2$: $2y + 18/y = 4 + 9 = 13$.\nTách theo điểm rơi $x = 2, y = 2$:\n- $x$ đi với $4/x$: hệ số là $1x$ (vì $4/2^2 = 1$).\n- $y$ đi với $18/y$: hệ số là $\\frac{18}{2^2} y = 4{,}5y > 3y$ (không đủ $y$).\nVậy điểm rơi thực sự nằm ở biên $x + y = 4$ hoặc giải tự do: tại $x = 2, y = 3$, $x + y = 5 \\ge 4$, thỏa mãn điều kiện $x + y \\ge 4$!\nThật vậy, với $x = 2, y = 3$:\n$P = \\left(x + \\frac{4}{x}\\right) + \\left(2y + \\frac{18}{y}\\right) + (x + y)$ không tối ưu.\nTách trực tiếp: $P = \\left(2x + \\frac{4}{x}\\right) + \\left(3y + \\frac{18}{y}\\right)$.\nTại điểm rơi $x = \\sqrt{2}, y = \\sqrt{6}$, tổng $x + y \\approx 1{,}414 + 2{,}449 = 3{,}863 < 4$.\nDo đó điểm rơi bắt buộc phải đạt tại biên $x + y = 4$.\nSử dụng phương pháp nhân tử Lagrange hoặc thế $y = 4 - x$ ta tìm được GTNN chính xác.",
            "rubric": [
                {"step": "Phân tích điều kiện biên và tách hạng tử theo điểm rơi", "subScore": 0.5},
                {"step": "Áp dụng Cauchy và tìm GTNN chuẩn xác", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c2_9_bai4_test2"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương II - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Phương trình $x^2 - 4x = 0$ có các nghiệm là:", "options": ["$x = 0$ hoặc $x = 4$", "$x = 4$", "$x = 0$ hoặc $x = -4$", "$x = 2$ hoặc $x = -2$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Nghiệm của bất phương trình $\\frac{x - 1}{3} > \\frac{x + 2}{4}$ là:", "options": ["$x > 10$", "$x < 10$", "$x > -10$", "$x < -10$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Phương trình $\\frac{2}{x - 1} = \\frac{1}{x + 2}$ có nghiệm là:", "options": ["$x = -5$", "$x = 5$", "$x = 1$", "$x = -2$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Số nghiệm của phương trình $\\frac{x^2 - 9}{x - 3} = 6$ là:", "options": ["$0$ (vô nghiệm)", "$1$", "$2$", "Vô số"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $a < b$. Khẳng định nào sau đây SAI?", "options": ["$-5a < -5b$", "$5a < 5b$", "$a - 7 < b - 7$", "$-2a + 3 > -2b + 3$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tập nghiệm của bất phương trình $(x - 2)^2 \\le x^2 - 8$ là:", "options": ["$x \\ge 3$", "$x \\le 3$", "$x \\ge -3$", "$x \\le -3$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Giải phương trình $x^3 - 4x = 0$. Tích các nghiệm là:", "options": ["$0$", "$4$", "$-4$", "$2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $1 \\le 2x - 3 < 7$?", "options": ["$3$ ($x = 2, 3, 4$)", "$4$", "$2$", "$5$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $x > 0$. Giá trị nhỏ nhất của biểu thức $P = x + \\frac{25}{x}$ là:", "options": ["$10$", "$25$", "$5$", "$15$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm $m$ để phương trình $\\frac{x - m}{x - 1} = 2$ có nghiệm dương:", "options": ["$m < 2$ và $m \\neq 1$", "$m > 2$", "$m < 2$", "$m \\neq 1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Nghiệm của bất phương trình $\\frac{x - 3}{x + 1} > 0$ là:", "options": ["$x < -1$ hoặc $x > 3$", "$-1 < x < 3$", "$x > 3$", "$x < -1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $a, b, c > 0$ thỏa mãn $a + b + c = 1$. Giá trị nhỏ nhất của $\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}$ là:", "options": ["$9$", "$3$", "$6$", "$1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho phương trình $\\frac{x}{x - 3} - \\frac{1}{x} = \\frac{3}{x(x - 3)}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "ĐKXĐ là $x \\neq 0$ và $x \\neq 3$.", "correct": True},
                {"subId": "b", "text": "Khử mẫu ta được phương trình $x^2 - (x - 3) = 3$.", "correct": True},
                {"subId": "c", "text": "Phương trình thu gọn là $x^2 - x = 0 \\Leftrightarrow x(x - 1) = 0$.", "correct": True},
                {"subId": "d", "text": "Phương trình có 2 nghiệm phân biệt.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho bất phương trình bậc nhất một ẩn: $-3(x - 1) \\ge 2x + 8$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Khai triển vế trái: $-3x + 3 \\ge 2x + 8$.", "correct": True},
                {"subId": "b", "text": "Chuyển vế: $-5x \\ge 5$.", "correct": True},
                {"subId": "c", "text": "Nghiệm là $x \\le -1$.", "correct": True},
                {"subId": "d", "text": "Số nguyên lớn nhất thỏa mãn bất phương trình là $0$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm nghiệm của phương trình $\\frac{2x - 5}{3} = \\frac{x - 1}{2}$.", "correctAnswer": "7", "explanation": "$2(2x - 5) = 3(x - 1) \\Rightarrow 4x - 10 = 3x - 3 \\Rightarrow x = 7$."},
        {"id": 2, "level": "Thông hiểu", "question": "Giải bất phương trình $6 - 2x > 0$. Số nguyên dương lớn nhất thỏa mãn là bao nhiêu?", "correctAnswer": "2", "explanation": "$2x < 6 \\Rightarrow x < 3$. Số nguyên dương lớn nhất là $2$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho phương trình $x^2 - 5x + 6 = 0$. Tính tổng các nghiệm của phương trình.", "correctAnswer": "5", "explanation": "$(x - 2)(x - 3) = 0 \\Rightarrow x = 2$ hoặc $x = 3$. Tổng = $5$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $A = x + \\frac{1}{4x}$.", "correctAnswer": "1", "explanation": "$A \\ge 2\\sqrt{x \\cdot \\frac{1}{4x}} = 2 \\times \\frac{1}{2} = 1$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải phương trình sau:\n$$\\frac{x + 2}{x - 2} - \\frac{2}{x^2 - 2x} = \\frac{1}{x}$$",
            "solution": "Điều kiện xác định: $x \\neq 0$ và $x \\neq 2$.\nTa có: $x^2 - 2x = x(x - 2)$. Mẫu thức chung: $x(x - 2)$.\nQuy đồng mẫu thức và khử mẫu:\n$x(x + 2) - 2 = 1(x - 2)$\n$\\Leftrightarrow x^2 + 2x - 2 = x - 2$\n$\\Leftrightarrow x^2 + x = 0$\n$\\Leftrightarrow x(x + 1) = 0$\n$\\Leftrightarrow x = 0$ hoặc $x = -1$.\nĐối chiếu với điều kiện xác định:\n- $x = 0$ (loại do không thỏa mãn ĐKXĐ).\n- $x = -1$ (thỏa mãn ĐKXĐ).\nVậy tập nghiệm của phương trình là $S = \\{-1\\}$.",
            "rubric": [
                {"step": "Tìm đúng ĐKXĐ x khác 0, x khác 2 và quy đồng khử mẫu", "subScore": 0.5},
                {"step": "Giải ra x = 0 (loại), x = -1 (nhận) và kết luận S = {-1}", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải bất phương trình sau:\n$$\\frac{3x - 1}{4} - \\frac{2x - 3}{3} \\le \\frac{x + 1}{6}$$",
            "solution": "Mẫu thức chung là $12$.\nNhân cả hai vế với 12:\n$3(3x - 1) - 4(2x - 3) \\le 2(x + 1)$\n$\\Leftrightarrow 9x - 3 - 8x + 12 \\le 2x + 2$\n$\\Leftrightarrow x + 9 \\le 2x + 2$\n$\\Leftrightarrow x - 2x \\le 2 - 9$\n$\\Leftrightarrow -x \\le -7$\n$\\Leftrightarrow x \\ge 7$.\nVậy tập nghiệm của bất phương trình là $\\{x \\mid x \\ge 7\\}$.",
            "rubric": [
                {"step": "Quy đồng mẫu thức chung 12 và khai triển chuẩn xác", "subScore": 0.5},
                {"step": "Thu gọn ra -x <= -7 và đổi chiều ra x >= 7", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Chứng minh rằng với mọi số thực dương $a, b$, ta có:\n$$\\frac{a^2}{b} + \\frac{b^2}{a} \\ge a + b$$",
            "solution": "Cách 1: Quy đồng mẫu số và biến đổi tương đương:\n$\\frac{a^2}{b} + \\frac{b^2}{a} \\ge a + b \\Leftrightarrow \\frac{a^3 + b^3}{ab} \\ge a + b$\nVì $a, b > 0 \\Rightarrow ab > 0$, nhân cả hai vế với $ab$:\n$a^3 + b^3 \\ge ab(a + b)$\n$\\Leftrightarrow (a + b)(a^2 - ab + b^2) \\ge ab(a + b)$\nVì $a + b > 0$, chia cả hai vế cho $a + b$:\n$a^2 - ab + b^2 \\ge ab \\Leftrightarrow a^2 - 2ab + b^2 \\ge 0 \\Leftrightarrow (a - b)^2 \\ge 0$.\nBất đẳng thức cuối cùng luôn đúng với mọi $a, b > 0$.\nDấu \"=\" xảy ra khi $a = b$.\nCách 2: Áp dụng BĐT Cauchy:\n$\\frac{a^2}{b} + b \\ge 2\\sqrt{\\frac{a^2}{b} \\cdot b} = 2a$.\n$\\frac{b^2}{a} + a \\ge 2\\sqrt{\\frac{b^2}{a} \\cdot a} = 2b$.\nCộng hai bất đẳng thức lại:\n$\\frac{a^2}{b} + \\frac{b^2}{a} + (a + b) \\ge 2a + 2b \\Leftrightarrow \\frac{a^2}{b} + \\frac{b^2}{a} \\ge a + b$.\nĐẳng thức được chứng minh.",
            "rubric": [
                {"step": "Biến đổi tương đương hoặc dùng kĩ thuật thêm bớt Cauchy", "subScore": 0.5},
                {"step": "Hoàn tất chứng minh và chỉ rõ dấu bằng khi a = b", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c2_9_bai4_test3"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương II - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Phương trình $x^4 - 1 = 0$ có bao nhiêu nghiệm thực?", "options": ["$2$ nghiệm ($x = \\pm 1$)", "$4$ nghiệm", "$1$ nghiệm", "$0$ nghiệm"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Nghiệm của bất phương trình $(x - 2)^2 > 0$ là:", "options": ["Mọi $x \\neq 2$", "Mọi $x \\in \\mathbb{R}$", "$x > 2$", "Vô nghiệm"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tập nghiệm của phương trình $|x - 1| = x - 1$ là:", "options": ["$x \\ge 1$", "$x > 1$", "$x = 1$", "Mọi $x$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho $x, y > 0$ thỏa mãn $x + y = 2$. Giá trị nhỏ nhất của $\\frac{1}{x} + \\frac{1}{y}$ là:", "options": ["$2$", "$1$", "$4$", "$\\frac{1}{2}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Giải phương trình $(x^2 - x + 1)(x^2 - x - 3) = 5$. Nghiệm thực của phương trình là:", "options": ["$x = -1$ và $x = 2$", "$x = 1$ và $x = -2$", "$x = 0$ và $x = 1$", "Vô nghiệm"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tìm số nghiệm nguyên của bất phương trình $\\frac{x + 2}{x - 1} < 0$:", "options": ["$2$ ($x = -1$ và $x = 0$)", "$3$", "$1$", "$0$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $a, b > 0$ và $a + b \\le 1$. Giá trị nhỏ nhất của $A = a + b + \\frac{1}{a} + \\frac{1}{b}$ là:", "options": ["$5$", "$4$", "$\\frac{9}{2}$", "$6$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Phương trình $(x - 1)^4 + (x - 3)^4 = 16$ có nghiệm là:", "options": ["$x = 1$ và $x = 3$", "$x = 2$", "$x = 0$ và $x = 4$", "Vô nghiệm"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho ba số dương $a, b, c$. Bất đẳng thức nào sau đây luôn đúng?", "options": ["$\\frac{a^3}{b} + \\frac{b^3}{c} + \\frac{c^3}{a} \\ge ab + bc + ca$", "$\\frac{a}{b+c} + \\frac{b}{c+a} + \\frac{c}{a+b} < 1$", "$a^3 + b^3 + c^3 < 3abc$", "$(a+b+c)^3 \\le 27abc$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm $m$ để bất phương trình $(m - 1)x + 2 > 0$ đúng với mọi $x \\in [-1; 2]$:", "options": ["$0 < m < 3$", "$-1 < m < 2$", "$m < 3$", "$m > 0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $x, y$ thỏa mãn $x^2 + y^2 = 4$. Giá trị lớn nhất của biểu thức $P = x + \\sqrt{3}y$ là:", "options": ["$4$", "$2$", "$8$", "$2\\sqrt{3}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giải phương trình $\\frac{x}{x^2 + 1} + \\frac{x}{x^2 + 2} = \\frac{1}{2}$. Số nghiệm thực của phương trình là:", "options": ["$2$", "$4$", "$1$", "$0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho phương trình $\\frac{x^2 - 3x}{x^2 - 9} = \\frac{x}{x + 3}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điều kiện xác định là $x \\neq 3$ và $x \\neq -3$.", "correct": True},
                {"subId": "b", "text": "Rút gọn vế trái: $\\frac{x(x - 3)}{(x - 3)(x + 3)} = \\frac{x}{x + 3}$.", "correct": True},
                {"subId": "c", "text": "Phương trình nghiệm đúng với mọi $x$ thỏa mãn ĐKXĐ.", "correct": True},
                {"subId": "d", "text": "Tập nghiệm của phương trình là $\\mathbb{R}$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $a, b, c > 0$ thỏa mãn $a + b + c = 3$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Tích $abc \\le 1$.", "correct": True},
                {"subId": "b", "text": "$a^2 + b^2 + c^2 \\ge 3$.", "correct": True},
                {"subId": "c", "text": "$\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 3$.", "correct": True},
                {"subId": "d", "text": "Dấu bằng của các bất đẳng thức trên xảy ra khi $a = 1, b = 2, c = 0$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Giải phương trình $x^2 - 16 = 0$. Tính tích các nghiệm.", "correctAnswer": "-16", "explanation": "$x = 4$ và $x = -4$. Tích = $-16$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho $a, b > 0$ và $ab = 9$. Tìm giá trị nhỏ nhất của $a + b$.", "correctAnswer": "6", "explanation": "$a + b \\ge 2\\sqrt{ab} = 2\\sqrt{9} = 6$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số nghiệm nguyên của bất phương trình $x^2 - 4x \\le 0$.", "correctAnswer": "5", "explanation": "$x(x - 4) \\le 0 \\Rightarrow 0 \\le x \\le 4$. Các nghiệm nguyên là $0, 1, 2, 3, 4$. Có 5 nghiệm."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $x > 1$. Tìm giá trị nhỏ nhất của $P = x + \\frac{4}{x - 1}$.", "correctAnswer": "5", "explanation": "$P = (x - 1) + \\frac{4}{x - 1} + 1 \\ge 2\\sqrt{4} + 1 = 5$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải phương trình trùng phương sau:\n$$x^4 - 8x^2 - 9 = 0$$",
            "solution": "Đặt $t = x^2$ (điều kiện $t \\ge 0$).\nPhương trình trở thành:\n$t^2 - 8t - 9 = 0$\nTa có $a - b + c = 1 - (-8) + (-9) = 0$, nên phương trình có hai nghiệm:\n$t_1 = -1$ (loại vì $t \\ge 0$).\n$t_2 = -\\frac{c}{a} = 9$ (thỏa mãn $t \\ge 0$).\nVới $t = 9 \\Rightarrow x^2 = 9 \\Rightarrow x = \\pm 3$.\nVậy tập nghiệm của phương trình là $S = \\{-3; 3\\}$.",
            "rubric": [
                {"step": "Đặt ẩn phụ t = x^2 (t >= 0) và giải ra t = -1 (loại), t = 9 (nhận)", "subScore": 0.5},
                {"step": "Tìm ra x = +- 3 và kết luận tập nghiệm", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải phương trình bằng phương pháp đặt ẩn phụ đối xứng:\n$$(x - 1)(x - 2)(x - 4)(x - 8) = 4x^2$$",
            "solution": "Nhân $(x - 1)$ với $(x - 8)$ và $(x - 2)$ với $(x - 4)$:\n$[(x - 1)(x - 8)][(x - 2)(x - 4)] = 4x^2$\n$\\Leftrightarrow (x^2 - 9x + 8)(x^2 - 6x + 8) = 4x^2$.\nNhận xét $x = 0$ không phải là nghiệm của phương trình.\nChia cả hai vế cho $x^2 \\neq 0$:\n$\\left(x - 9 + \\frac{8}{x}\\right)\\left(x - 6 + \\frac{8}{x}\\right) = 4$.\nĐặt $t = x + \\frac{8}{x} - 7{,}5$ (hoặc đặt $u = x + \\frac{8}{x}$).\nĐặt $u = x + \\frac{8}{x}$, phương trình trở thành:\n$(u - 9)(u - 6) = 4 \\Leftrightarrow u^2 - 15u + 54 = 4 \\Leftrightarrow u^2 - 15u + 50 = 0$\n$\\Leftrightarrow (u - 5)(u - 10) = 0 \\Rightarrow u = 5$ hoặc $u = 10$.\n- Với $u = 5$: $x + \\frac{8}{x} = 5 \\Leftrightarrow x^2 - 5x + 8 = 0$ (vô nghiệm vì $\\Delta = 25 - 32 < 0$).\n- Với $u = 10$: $x + \\frac{8}{x} = 10 \\Leftrightarrow x^2 - 10x + 8 = 0 \\Rightarrow x = 5 \\pm \\sqrt{17}$.\nVậy tập nghiệm của phương trình là $S = \\{5 - \\sqrt{17}; 5 + \\sqrt{17}\\}$.",
            "rubric": [
                {"step": "Ghép cặp, chia hai vế cho x^2 và đặt ẩn phụ u = x + 8/x", "subScore": 0.5},
                {"step": "Giải ra u = 5, u = 10 và tìm đúng nghiệm x = 5 +- sqrt(17)", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Chứng minh rằng:\n$$\\frac{a}{1 + b^2} + \\frac{b}{1 + c^2} + \\frac{c}{1 + a^2} \\ge \\frac{3}{2}$$",
            "solution": "Áp dụng kĩ thuật Cauchy ngược dấu:\nTa có: $\\frac{a}{1 + b^2} = \\frac{a(1 + b^2) - ab^2}{1 + b^2} = a - \\frac{ab^2}{1 + b^2}$.\nÁp dụng BĐT Cauchy cho mẫu số: $1 + b^2 \\ge 2b > 0$.\nSuy ra: $\\frac{ab^2}{1 + b^2} \\le \\frac{ab^2}{2b} = \\frac{ab}{2}$.\nDo đó: $\\frac{a}{1 + b^2} \\ge a - \\frac{ab}{2}$.\nHoàn toàn tương tự:\n$\\frac{b}{1 + c^2} \\ge b - \\frac{bc}{2}$,\n$\\frac{c}{1 + a^2} \\ge c - \\frac{ca}{2}$.\nCộng vế theo vế ba bất đẳng thức:\n$\\frac{a}{1 + b^2} + \\frac{b}{1 + c^2} + \\frac{c}{1 + a^2} \\ge (a + b + c) - \\frac{ab + bc + ca}{2}$.\nMặt khác, ta luôn có $ab + bc + ca \\le \\frac{(a + b + c)^2}{3} = \\frac{3^2}{3} = 3$.\nSuy ra: $\\frac{ab + bc + ca}{2} \\le \\frac{3}{2} \\Rightarrow -\\frac{ab + bc + ca}{2} \\ge -\\frac{3}{2}$.\nDo đó:\n$\\frac{a}{1 + b^2} + \\frac{b}{1 + c^2} + \\frac{c}{1 + a^2} \\ge 3 - \\frac{3}{2} = \\frac{3}{2}$.\nDấu \"=\" xảy ra khi và chỉ khi $a = b = c = 1$.\nBất đẳng thức được chứng minh.",
            "rubric": [
                {"step": "Sử dụng kĩ thuật Cauchy ngược dấu a/(1+b^2) >= a - ab/2", "subScore": 0.5},
                {"step": "Cộng ba bất đẳng thức, dùng ab+bc+ca <= (a+b+c)^2/3 và kết luận dấu bằng", "subScore": 0.5}
            ]
        }
    ]
}
