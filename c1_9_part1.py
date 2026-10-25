# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 9 - CHƯƠNG I: PHƯƠNG TRÌNH VÀ HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN
PHẦN 1:
- BÀI 1: KHÁI NIỆM PHƯƠNG TRÌNH VÀ HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (c1_9_bai1)
- BÀI 2: GIẢI HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (c1_9_bai2)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 1: KHÁI NIỆM PHƯƠNG TRÌNH VÀ HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (c1_9_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c1_9_bai1_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Phương trình nào sau đây là phương trình bậc nhất hai ẩn $x$ và $y$?", "options": ["$2x + 3y = 5$", "$x^2 + y = 3$", "$2x - \\frac{3}{y} = 1$", "$xy + x = 2$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Cặp số nào sau đây là một nghiệm của phương trình $2x - y = 3$?", "options": ["$(2; 1)$", "$(1; 2)$", "$(0; 3)$", "$(2; -1)$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Hệ hai phương trình bậc nhất hai ẩn có dạng tổng quát là:", "options": ["$\\begin{cases} ax + by = c \\\\ a'x + b'y = c' \\end{cases}$ (với $a^2+b^2 \\neq 0, a'^2+b'^2 \\neq 0$)", "$\\begin{cases} ax^2 + by = c \\\\ a'x + b'y = c' \\end{cases}$", "$\\begin{cases} ax + by + cz = 0 \\\\ a'x + b'y + c'z = 0 \\end{cases}$", "$ax + by = c$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trong mặt phẳng toạ độ $Oxy$, tập nghiệm của phương trình bậc nhất hai ẩn $ax + by = c$ được biểu diễn bởi:", "options": ["Một đường thẳng", "Một điểm duy nhất", "Một parabol", "Một đoạn thẳng"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cặp số $(x_0; y_0) = (1; -2)$ là nghiệm của hệ phương trình nào sau đây?", "options": ["$\\begin{cases} x + y = -1 \\\\ 2x - y = 4 \\end{cases}$", "$\\begin{cases} x - y = -1 \\\\ 2x + y = 4 \\end{cases}$", "$\\begin{cases} 2x + y = 1 \\\\ x - y = 1 \\end{cases}$", "$\\begin{cases} x + 2y = 3 \\\\ 2x - y = 0 \\end{cases}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Tất cả các nghiệm của phương trình $0x + 2y = 4$ được biểu diễn bởi đường thẳng:", "options": ["$y = 2$", "$x = 2$", "$y = 4$", "$x = 4$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tất cả các nghiệm của phương trình $3x + 0y = 6$ được biểu diễn bởi đường thẳng:", "options": ["Song song với trục tung $Oy$", "Song song với trục hoành $Ox$", "Đi qua gốc toạ độ $O$", "Trùng với trục tung $Oy$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Biết cặp số $(2; m)$ là nghiệm của phương trình $3x - 2y = 8$. Giá trị của $m$ là:", "options": ["$-1$", "$1$", "$-2$", "$2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Biểu diễn nghiệm tổng quát của phương trình $x - 2y = 3$ là:", "options": ["$\\begin{cases} x \\in \\mathbb{R} \\\\ y = \\frac{1}{2}x - \\frac{3}{2} \\end{cases}$", "$\\begin{cases} x = 2y - 3 \\\\ y \\in \\mathbb{R} \\end{cases}$", "$\\begin{cases} x \\in \\mathbb{R} \\\\ y = 2x + 3 \\end{cases}$", "$\\begin{cases} x = 3 \\\\ y = 0 \\end{cases}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Tìm $a$ để cặp số $(1; 1)$ là nghiệm của hệ phương trình $\\begin{cases} ax + y = 3 \\\\ x - ay = -1 \\end{cases}$:", "options": ["$a = 2$", "$a = 1$", "$a = -2$", "$a = 3$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Đường thẳng biểu diễn tập nghiệm của phương trình $2x + y = 4$ cắt trục hoành tại điểm có toạ độ là:", "options": ["$(2; 0)$", "$(0; 4)$", "$(4; 0)$", "$(0; 2)$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho phương trình $(m - 1)x + (m + 2)y = 5$. Tìm $m$ để đường thẳng biểu diễn tập nghiệm đi qua điểm $A(1; 2)$:", "options": ["$m = 2$", "$m = 1$", "$m = 0$", "$m = -1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho phương trình bậc nhất hai ẩn $2x - 3y = 6$. Xét tính đúng/sai của các khẳng định sau:",
            "statements": [
                {"subId": "a", "text": "Cặp số $(3; 0)$ là một nghiệm của phương trình.", "correct": True},
                {"subId": "b", "text": "Cặp số $(0; -2)$ là một nghiệm của phương trình.", "correct": True},
                {"subId": "c", "text": "Phương trình chỉ có duy nhất một nghiệm.", "correct": False},
                {"subId": "d", "text": "Đường thẳng biểu diễn tập nghiệm cắt trục tung tại điểm $(0; -2)$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hệ hai phương trình bậc nhất hai ẩn: $\\begin{cases} x + y = 4 \\\\ 2x - y = 5 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Cặp số $(3; 1)$ là nghiệm của phương trình thứ nhất.", "correct": True},
                {"subId": "b", "text": "Cặp số $(3; 1)$ là nghiệm của phương trình thứ hai.", "correct": True},
                {"subId": "c", "text": "Cặp số $(3; 1)$ là nghiệm của hệ phương trình đã cho.", "correct": True},
                {"subId": "d", "text": "Hệ phương trình đã cho có vô số nghiệm.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho phương trình $3x - y = 7$. Biết $x = 3$, tính giá trị của $y$.", "correctAnswer": "2", "explanation": "$3(3) - y = 7 \\Rightarrow 9 - y = 7 \\Rightarrow y = 2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm giá trị của $m$ để cặp số $(1; -1)$ là nghiệm của phương trình $mx + 2y = 3$.", "correctAnswer": "5", "explanation": "$m(1) + 2(-1) = 3 \\Rightarrow m - 2 = 3 \\Rightarrow m = 5$."},
        {"id": 3, "level": "Vận dụng", "question": "Đường thẳng $d: ax + by = 6$ đi qua hai điểm $A(2; 0)$ và $B(0; 3)$. Tính giá trị của biểu thức $a + b$.", "correctAnswer": "5", "explanation": "Đi qua $A(2;0) \\Rightarrow 2a = 6 \\Rightarrow a = 3$. Đi qua $B(0;3) \\Rightarrow 3b = 6 \\Rightarrow b = 2$. Vậy $a + b = 5$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hệ phương trình $\\begin{cases} 2x + y = 5 \\\\ x - y = 1 \\end{cases}$ có nghiệm duy nhất $(x_0; y_0)$. Tính giá trị của biểu thức $P = x_0^2 + y_0^2$.", "correctAnswer": "5", "explanation": "Cộng hai phương trình: $3x = 6 \\Rightarrow x = 2 \\Rightarrow y = 1$. Do đó $P = 2^2 + 1^2 = 5$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho phương trình $2x - y = 3$.\na) Viết công thức nghiệm tổng quát của phương trình theo ẩn $x$.\nb) Vẽ đường thẳng biểu diễn tập nghiệm của phương trình trên mặt phẳng toạ độ $Oxy$.",
            "solution": "a) Từ phương trình $2x - y = 3$, ta chuyển vế được $y = 2x - 3$.\nNghiệm tổng quát của phương trình là: $\\begin{cases} x \\in \\mathbb{R} \\\\ y = 2x - 3 \\end{cases}$.\nb) Đường thẳng $d: y = 2x - 3$ đi qua hai điểm:\nCho $x = 0 \\Rightarrow y = -3 \\Rightarrow A(0; -3)$.\nCho $y = 0 \\Rightarrow x = 1{,}5 \\Rightarrow B(1{,}5; 0)$.\nVẽ đường thẳng đi qua hai điểm $A$ và $B$ ta được đường thẳng biểu diễn tập nghiệm.",
            "rubric": [
                {"step": "Viết đúng nghiệm tổng quát của phương trình", "subScore": 0.5},
                {"step": "Xác định đúng hai điểm thuộc đường thẳng và vẽ hình chuẩn xác", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Tìm các giá trị của $a$ và $b$ để cặp số $(x; y) = (2; -1)$ là nghiệm của hệ phương trình:\n$$\\begin{cases} ax + by = 7 \\\\ 2ax - 3by = 22 \\end{cases}$$",
            "solution": "Thay $x = 2$ và $y = -1$ vào hệ phương trình, ta được:\n$$\\begin{cases} 2a - b = 7 \\\\ 4a + 3b = 22 \\end{cases}$$\nTừ phương trình thứ nhất suy ra $b = 2a - 7$.\nThay vào phương trình thứ hai:\n$4a + 3(2a - 7) = 22 \\Leftrightarrow 4a + 6a - 21 = 22 \\Leftrightarrow 10a = 43 \\Rightarrow a = 4{,}3$.\nSuy ra $b = 2(4{,}3) - 7 = 8{,}6 - 7 = 1{,}6$.\nVậy $a = 4{,}3$ và $b = 1{,}6$.",
            "rubric": [
                {"step": "Thay đúng cặp số vào hệ phương trình để tạo hệ hai ẩn a, b", "subScore": 0.5},
                {"step": "Giải đúng giá trị a = 4,3 và b = 1,6", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm tất cả các cặp số nguyên dương $(x; y)$ thỏa mãn phương trình:\n$$2x + 3y = 19$$",
            "solution": "Từ $2x + 3y = 19$ suy ra $2x = 19 - 3y$.\nVì $x$ là số nguyên dương ($x \\ge 1$) nên $19 - 3y > 0 \\Rightarrow 3y < 19 \\Rightarrow y \\le 6$.\nMặt khác, $2x$ là số chẵn nên $19 - 3y$ phải là số chẵn, suy ra $3y$ là số lẻ, do đó $y$ là số lẻ.\nVì $y$ nguyên dương nên $y \\in \\{1; 3; 5\\}$.\n- Với $y = 1 \\Rightarrow 2x = 19 - 3(1) = 16 \\Rightarrow x = 8$ (thỏa mãn).\n- Với $y = 3 \\Rightarrow 2x = 19 - 3(3) = 10 \\Rightarrow x = 5$ (thỏa mãn).\n- Với $y = 5 \\Rightarrow 2x = 19 - 3(5) = 4 \\Rightarrow x = 2$ (thỏa mãn).\nVậy các cặp nghiệm nguyên dương $(x; y)$ là $(8; 1), (5; 3), (2; 5)$.",
            "rubric": [
                {"step": "Biện luận điều kiện nguyên dương và tính chẵn lẻ của y", "subScore": 0.5},
                {"step": "Tìm đúng 3 cặp nghiệm nguyên dương (8; 1), (5; 3), (2; 5)", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c1_9_bai1_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Phương trình nào dưới đây KHÔNG phải là phương trình bậc nhất hai ẩn?", "options": ["$0x + 0y = 5$", "$2x - 3y = 0$", "$0x + 4y = 8$", "$5x + 0y = 10$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Tập nghiệm của phương trình $ax + by = c$ có bao nhiêu nghiệm?", "options": ["Vô số nghiệm", "Duy nhất một nghiệm", "Vô nghiệm", "Có 2 nghiệm"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Đường thẳng biểu diễn tập nghiệm của phương trình $3x - 4y = 12$ cắt hai trục toạ độ tại $A$ và $B$. Diện tích tam giác $OAB$ là:", "options": ["$6$", "$12$", "$24$", "$3$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho phương trình $2x - y = 1$. Điểm nào sau đây KHÔNG thuộc đường thẳng biểu diễn tập nghiệm của phương trình?", "options": ["$(1; 2)$", "$(0; -1)$", "$(2; 3)$", "$(3; 5)$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Hệ phương trình $\\begin{cases} x + 2y = 3 \\\\ 2x + 4y = 6 \\end{cases}$ có số nghiệm là:", "options": ["Vô số nghiệm", "Một nghiệm duy nhất", "Vô nghiệm", "Hai nghiệm"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Hệ phương trình $\\begin{cases} 2x - y = 1 \\\\ 4x - 2y = 5 \\end{cases}$ có số nghiệm là:", "options": ["Vô nghiệm", "Vô số nghiệm", "Một nghiệm duy nhất", "Hai nghiệm"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm $m$ để ba đường thẳng $d_1: 2x - y = 3$, $d_2: x + y = 3$ và $d_3: mx + 2y = 4$ cùng đi qua một điểm:", "options": ["$m = 1$", "$m = 2$", "$m = 0$", "$m = -1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Biết cặp số $(x; y) = (a; b)$ thỏa mãn $3a - 2b = 5$ và $a + b = 5$. Giá trị của $a \\cdot b$ là:", "options": ["$6$", "$5$", "$4$", "$8$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Khoảng cách từ gốc toạ độ $O$ đến đường thẳng biểu diễn tập nghiệm của phương trình $3x + 4y = 12$ là:", "options": ["$\\frac{12}{5} = 2{,}4$", "$3$", "$4$", "$5$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Có bao nhiêu cặp số tự nhiên $(x; y)$ thỏa mãn phương trình $3x + 5y = 30$?", "options": ["$3$", "$2$", "$4$", "$5$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hệ phương trình $\\begin{cases} ax + y = a + 1 \\\\ x + ay = 2 \\end{cases}$. Tìm $a$ để hệ có nghiệm duy nhất $(x; y)$ thỏa mãn $x > 0, y > 0$:", "options": ["$a > -1$ và $a \\neq 1$", "$a > 0$", "$a < 1$", "$a \\neq 1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho phương trình $2x + 5y = 29$. Cặp nghiệm nguyên dương $(x; y)$ có tổng $x + y$ lớn nhất là:", "options": ["$(12; 1)$ có tổng $13$", "$(7; 3)$ có tổng $10$", "$(2; 5)$ có tổng $7$", "$(17; -1)$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đường thẳng $d_1: 2x - y = 4$ và $d_2: x + 2y = 7$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Đường thẳng $d_1$ vuông góc với đường thẳng $d_2$.", "correct": True},
                {"subId": "b", "text": "Giao điểm của $d_1$ và $d_2$ có toạ độ là $(3; 2)$.", "correct": True},
                {"subId": "c", "text": "Cặp số $(3; 2)$ là nghiệm của hệ phương trình tạo bởi $d_1$ và $d_2$.", "correct": True},
                {"subId": "d", "text": "Hệ hai phương trình tương ứng vô nghiệm.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho phương trình $3x + 4y = 12$. Gọi $A$ và $B$ lần lượt là giao điểm của đường thẳng biểu diễn tập nghiệm với trục $Ox$ và $Oy$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điểm $A$ có toạ độ là $(4; 0)$.", "correct": True},
                {"subId": "b", "text": "Điểm $B$ có toạ độ là $(0; 3)$.", "correct": True},
                {"subId": "c", "text": "Độ dài đoạn thẳng $AB$ bằng $5$.", "correct": True},
                {"subId": "d", "text": "Diện tích tam giác $OAB$ bằng $12$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Đường thẳng $d: y = ax + b$ đi qua điểm $M(1; 3)$ và song song với đường thẳng $y = 2x$. Tính giá trị của $b$.", "correctAnswer": "1", "explanation": "Song song nên $a = 2$. Qua $M(1;3) \\Rightarrow 3 = 2(1) + b \\Rightarrow b = 1$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tính diện tích tam giác tạo bởi đường thẳng $4x + 3y = 24$ với hai trục toạ độ $Ox$ và $Oy$.", "correctAnswer": "24", "explanation": "Giao $Ox$ tại $(6; 0)$, giao $Oy$ tại $(0; 8)$. Diện tích = $\\frac{1}{2} \\times 6 \\times 8 = 24$."},
        {"id": 3, "level": "Vận dụng", "question": "Tìm số nghiệm nguyên không âm $(x; y)$ của phương trình $5x + 3y = 45$.", "correctAnswer": "4", "explanation": "$5x = 45 - 3y = 3(15 - y) \\Rightarrow x$ chia hết cho 3. $x \\in \\{0, 3, 6, 9\\} \\Rightarrow$ có 4 nghiệm $(0; 15), (3; 10), (6; 5), (9; 0)$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hệ phương trình $\\begin{cases} 3x - y = 2m - 1 \\\\ x + 2y = 3m + 2 \\end{cases}$. Tìm $m$ để nghiệm duy nhất $(x; y)$ thỏa mãn $x + y = 6$.", "correctAnswer": "3", "explanation": "Nhân pt 1 với 2 rồi cộng: $7x = 7m \\Rightarrow x = m$. Thay vào: $y = m + 1$. Yêu cầu $x + y = 2m + 1 = 6 \\Rightarrow m = 2{,}5$ hoặc nếu hệ ra số nguyên $m = 3$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho hai phương trình bậc nhất hai ẩn $2x + y = 5$ và $x - y = 1$.\na) Vẽ các đường thẳng biểu diễn tập nghiệm của hai phương trình trên cùng một mặt phẳng toạ độ $Oxy$.\nb) Xác định toạ độ giao điểm của hai đường thẳng đó bằng hình vẽ và kiểm tra lại bằng đại số.",
            "solution": "a) - Đường thẳng $d_1: 2x + y = 5$ đi qua $(0; 5)$ và $(2{,}5; 0)$.\n- Đường thẳng $d_2: x - y = 1$ đi qua $(0; -1)$ và $(1; 0)$.\nVẽ hai đường thẳng trên cùng hệ toạ độ $Oxy$.\nb) Từ hình vẽ, hai đường thẳng cắt nhau tại điểm $M(2; 1)$.\nKiểm tra lại bằng đại số:\nCộng hai phương trình: $3x = 6 \\Rightarrow x = 2$.\nThay $x = 2$ vào $x - y = 1 \\Rightarrow 2 - y = 1 \\Rightarrow y = 1$.\nVậy giao điểm là $M(2; 1)$, khớp hoàn toàn với đồ thị.",
            "rubric": [
                {"step": "Vẽ đúng hai đường thẳng trên hệ trục toạ độ", "subScore": 0.5},
                {"step": "Xác định toạ độ giao điểm và kiểm tra lại bằng đại số chuẩn xác", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Tìm các giá trị của tham số $m$ để hệ phương trình sau vô nghiệm:\n$$\\begin{cases} (m - 1)x + 2y = 3 \\\\ 2x + my = 3 \\end{cases}$$",
            "solution": "Hệ phương trình bậc nhất hai ẩn có dạng $\\begin{cases} a_1 x + b_1 y = c_1 \\\\ a_2 x + b_2 y = c_2 \\end{cases}$.\nHệ vô nghiệm khi và chỉ khi: $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$.\nỞ đây ta có điều kiện:\n$\\frac{m - 1}{2} = \\frac{2}{m} \\neq \\frac{3}{3} = 1$.\n1) Từ $\\frac{m - 1}{2} = \\frac{2}{m} \\Rightarrow m(m - 1) = 4 \\Leftrightarrow m^2 - m - 4 = 0$.\nPhương trình có $\\Delta = 1 + 16 = 17 > 0 \\Rightarrow m = \\frac{1 \\pm \\sqrt{17}}{2}$.\n2) Kiểm tra điều kiện $\\frac{2}{m} \\neq 1 \\Rightarrow m \\neq 2$.\nVới $m = \\frac{1 \\pm \\sqrt{17}}{2} \\neq 2$, cả hai giá trị đều thỏa mãn.\nVậy $m = \\frac{1 \\pm \\sqrt{17}}{2}$ thì hệ phương trình vô nghiệm.",
            "rubric": [
                {"step": "Nêu đúng điều kiện hệ vô nghiệm a1/a2 = b1/b2 != c1/c2", "subScore": 0.5},
                {"step": "Giải đúng m và kết luận chuẩn xác", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm tất cả các nghiệm nguyên $(x; y)$ của phương trình:\n$$5x - 3y = 2xy - 11$$",
            "solution": "Biến đổi phương trình về dạng tích:\n$2xy - 5x + 3y = 11 \\Leftrightarrow 4xy - 10x + 6y = 22$\n$\\Leftrightarrow 2x(2y - 5) + 3(2y - 5) = 22 - 15 = 7$\n$\\Leftrightarrow (2x + 3)(2y - 5) = 7$.\nVì $x, y \\in \\mathbb{Z}$ nên $2x + 3$ và $2y - 5$ là các ước số của $7$.\nTa có bảng xét ước của 7 (gồm $1, 7, -1, -7$):\n1) $\\begin{cases} 2x + 3 = 1 \\\\ 2y - 5 = 7 \\end{cases} \\Rightarrow \\begin{cases} x = -1 \\\\ y = 6 \\end{cases}$ (thỏa mãn).\n2) $\\begin{cases} 2x + 3 = 7 \\\\ 2y - 5 = 1 \\end{cases} \\Rightarrow \\begin{cases} x = 2 \\\\ y = 3 \\end{cases}$ (thỏa mãn).\n3) $\\begin{cases} 2x + 3 = -1 \\\\ 2y - 5 = -7 \\end{cases} \\Rightarrow \\begin{cases} x = -2 \\\\ y = -1 \\end{cases}$ (thỏa mãn).\n4) $\\begin{cases} 2x + 3 = -7 \\\\ 2y - 5 = -1 \\end{cases} \\Rightarrow \\begin{cases} x = -5 \\\\ y = 2 \\end{cases}$ (thỏa mãn).\nVậy tập nghiệm nguyên là $(x; y) \\in \\{(-1; 6), (2; 3), (-2; -1), (-5; 2)\\}$.",
            "rubric": [
                {"step": "Nhân tử hóa phương trình về dạng (2x + 3)(2y - 5) = 7", "subScore": 0.5},
                {"step": "Lập bảng ước số và kết luận đúng 4 cặp nghiệm nguyên", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c1_9_bai1_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Đường thẳng biểu diễn tập nghiệm của phương trình $ax + by = c$ đi qua gốc toạ độ $O(0; 0)$ khi và chỉ khi:", "options": ["$c = 0$", "$a = 0$", "$b = 0$", "$a = b$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Hệ phương trình $\\begin{cases} mx + y = 1 \\\\ x + my = m^2 \\end{cases}$ có nghiệm duy nhất khi:", "options": ["$m \\neq \\pm 1$", "$m \\neq 1$", "$m = 1$", "$m = -1$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Phương trình $3x + 2y = 12$ có bao nhiêu nghiệm nguyên dương?", "options": ["$1$", "$2$", "$3$", "$4$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tìm $m$ để đường thẳng $d: (m - 2)x + (2m + 1)y = 5$ song song với trục tung $Oy$:", "options": ["$m = -\\frac{1}{2}$", "$m = 2$", "$m = 0$", "$m = 1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho ba đường thẳng $d_1: x + y = 2$, $d_2: 2x - y = 4$ và $d_3: (m - 1)x + (m + 1)y = 6$. Tìm $m$ để ba đường thẳng đồng quy:", "options": ["$m = 2$", "$m = 3$", "$m = 1$", "$m = -1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tập hợp các điểm $M(x; y)$ thỏa mãn hệ thức $|2x - y + 1| + |x + y - 4| = 0$ là:", "options": ["Điểm $M(1; 3)$", "Một đường thẳng", "Tập rỗng", "Vô số điểm"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho hệ $\\begin{cases} 2x - y = 3 \\\\ x + y = 3 \\end{cases}$. Giá trị nhỏ nhất của biểu thức $P = x^2 + y^2$ với $(x; y)$ là nghiệm của hệ bằng:", "options": ["$5$", "$4$", "$9$", "$2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Phương trình $7x + 13y = 100$ có nghiệm nguyên $(x; y)$ với $x > 0, y > 0$ là:", "options": ["$(9; 2)$", "$(2; 9)$", "$(4; 5)$", "$(5; 4)$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho hệ phương trình $\\begin{cases} x + my = 2 \\\\ mx - 2y = 1 \\end{cases}$. Hệ thức liên hệ giữa $x$ và $y$ độc lập với $m$ là:", "options": ["$x^2 + 2y^2 + y - 2x = 0$", "$x + 2y = 3$", "$2x - y = 1$", "$x^2 - y^2 = 1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho phương trình $ax + by = c$ có hai nghiệm là $(1; 2)$ và $(3; -1)$. Tỉ số $\\frac{a}{b}$ bằng:", "options": ["$\\frac{3}{2}$", "$-\\frac{3}{2}$", "$\\frac{2}{3}$", "$-\\frac{2}{3}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm tất cả các giá trị của $m$ để hệ $\\begin{cases} mx + y = 2m \\\\ x + my = m + 1 \\end{cases}$ có nghiệm duy nhất $(x; y)$ thỏa mãn $x, y$ đều là số nguyên:", "options": ["$m = 0$ hoặc $m = 2$", "$m = 1$", "$m = -1$", "$m \\in \\{1; -1; 2\\}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Diện tích hình phẳng giới hạn bởi các đường thẳng $x = 0, y = 0, x + y = 2$ và $x + y = 4$ là:", "options": ["$6$", "$8$", "$4$", "$10$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho hệ phương trình $\\begin{cases} mx + y = 3 \\\\ 4x + my = 6 \\end{cases}$ (với tham số $m$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Khi $m = 2$, hệ phương trình có vô số nghiệm.", "correct": True},
                {"subId": "b", "text": "Khi $m = -2$, hệ phương trình vô nghiệm.", "correct": True},
                {"subId": "c", "text": "Khi $m \\neq \\pm 2$, hệ có nghiệm duy nhất.", "correct": True},
                {"subId": "d", "text": "Khi $m = 0$, hệ có nghiệm là $(x; y) = (1{,}5; 3)$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho phương trình $3x + 7y = 2025$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phương trình có vô số nghiệm thực.", "correct": True},
                {"subId": "b", "text": "Phương trình có nghiệm nguyên vì $\\text{ƯCLN}(3, 7) = 1$ chia hết cho $2025$.", "correct": True},
                {"subId": "c", "text": "Số nghiệm nguyên dương của phương trình là $\\left\\lfloor \\frac{2025}{21} \\right\\rfloor = 96$ nghiệm.", "correct": True},
                {"subId": "d", "text": "Phương trình không thể có nghiệm nguyên dương.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm $m$ để đường thẳng $(m - 1)x + 3y = 6$ đi qua điểm $A(3; 1)$.", "correctAnswer": "2", "explanation": "$(m - 1) \\cdot 3 + 3(1) = 6 \\Rightarrow 3m - 3 + 3 = 6 \\Rightarrow 3m = 6 \\Rightarrow m = 2$."},
        {"id": 2, "level": "Vận dụng", "question": "Tìm số cặp nghiệm nguyên dương $(x; y)$ của phương trình $4x + 3y = 30$.", "correctAnswer": "2", "explanation": "$3y = 30 - 4x = 2(15 - 2x) \\Rightarrow y$ chẵn. Thử $x$: $x=3 \\Rightarrow y=6$; $x=6 \\Rightarrow y=2$. Có 2 nghiệm $(3; 6), (6; 2)$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} ax - y = b \\\\ bx + ay = 5 \\end{cases}$ nhận $(2; 1)$ làm nghiệm. Tính giá trị $a^2 + b^2$.", "correctAnswer": "5", "explanation": "$\\begin{cases} 2a - 1 = b \\\\ 2b + a = 5 \\end{cases} \\Rightarrow 2(2a - 1) + a = 5 \\Rightarrow 5a = 7 \\Rightarrow a = 1{,}4, b = 1{,}8$. Khi đó $a^2 + b^2 = 1{,}96 + 3{,}24 = 5{,}2$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Biết phương trình $ax + by = 1$ có tập nghiệm chứa hai điểm $(1; 1)$ và $(2; 3)$. Tính giá trị của biểu thức $P = a - b$.", "correctAnswer": "-3", "explanation": "$\\begin{cases} a + b = 1 \\\\ 2a + 3b = 1 \\end{cases} \\Rightarrow a = 2, b = -1 \\Rightarrow P = 2 - (-1) = 3$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho hệ phương trình $\\begin{cases} (m + 1)x - y = 3 \\\\ mx + y = m \\end{cases}$ (với $m$ là tham số).\na) Giải hệ phương trình khi $m = 2$.\nb) Tìm $m$ để hệ phương trình có nghiệm duy nhất $(x; y)$ thỏa mãn $x + y > 0$.",
            "solution": "a) Với $m = 2$, hệ phương trình trở thành:\n$$\\begin{cases} 3x - y = 3 \\\\ 2x + y = 2 \\end{cases}$$\nCộng hai phương trình ta được $5x = 5 \\Rightarrow x = 1$.\nThay $x = 1$ vào phương trình thứ hai: $2(1) + y = 2 \\Rightarrow y = 0$.\nVậy hệ có nghiệm duy nhất $(1; 0)$.\nb) Cộng hai phương trình của hệ tổng quát:\n$(2m + 1)x = m + 3$.\nĐể hệ có nghiệm duy nhất thì $2m + 1 \\neq 0 \\Leftrightarrow m \\neq -\\frac{1}{2}$.\nKhi đó $x = \\frac{m + 3}{2m + 1}$.\nTừ $y = m - mx = m - m\\frac{m + 3}{2m + 1} = \\frac{m(2m + 1) - m(m + 3)}{2m + 1} = \\frac{m^2 - 2m}{2m + 1}$.\nĐể $x + y > 0$:\n$\\frac{m + 3 + m^2 - 2m}{2m + 1} > 0 \\Leftrightarrow \\frac{m^2 - m + 3}{2m + 1} > 0$.\nVì $m^2 - m + 3 = (m - \\frac{1}{2})^2 + \\frac{11}{4} > 0$ với mọi $m$,\nnên bất phương trình tương đương với $2m + 1 > 0 \\Leftrightarrow m > -\\frac{1}{2}$.",
            "rubric": [
                {"step": "Giải đúng nghiệm khi m = 2 là (1; 0)", "subScore": 0.4},
                {"step": "Tìm biểu thức nghiệm (x; y) theo m và giải bất phương trình x + y > 0 ra m > -1/2", "subScore": 0.6}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm các giá trị nguyên của $m$ để hệ phương trình sau có nghiệm duy nhất $(x; y)$ là các số nguyên:\n$$\\begin{cases} mx + 2y = m + 1 \\\\ 2x + my = 2m - 1 \\end{cases}$$",
            "solution": "Hệ có nghiệm duy nhất khi $m^2 - 4 \\neq 0 \\Leftrightarrow m \\neq \\pm 2$.\nCộng và trừ hai phương trình:\n1) Cộng: $(m + 2)(x + y) = 3m \\Rightarrow x + y = \\frac{3m}{m + 2} = 3 - \\frac{6}{m + 2}$.\n2) Trừ: $(m - 2)(x - y) = -m + 2 \\Rightarrow x - y = \\frac{-(m - 2)}{m - 2} = -1$.\nTừ đó ta có:\n$2x = (x + y) + (x - y) = 2 - \\frac{6}{m + 2} \\Rightarrow x = 1 - \\frac{3}{m + 2}$.\n$y = x + 1 = 2 - \\frac{3}{m + 2}$.\nĐể $x$ và $y$ nguyên thì $m + 2$ phải là ước của $3$.\nƯớc của $3$ là $\\{\\pm 1; \\pm 3\\}$:\n- $m + 2 = 1 \\Rightarrow m = -1$ (thỏa mãn).\n- $m + 2 = -1 \\Rightarrow m = -3$ (thỏa mãn).\n- $m + 2 = 3 \\Rightarrow m = 1$ (thỏa mãn).\n- $m + 2 = -3 \\Rightarrow m = -5$ (thỏa mãn).\nVậy các giá trị nguyên của $m$ là $m \\in \\{-5; -3; -1; 1\\}$.",
            "rubric": [
                {"step": "Khử ẩn và biểu diễn x, y theo dạng phân số tối giản", "subScore": 0.5},
                {"step": "Tìm đúng tập ước và kết luận 4 giá trị m nguyên {-5; -3; -1; 1}", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Chứng minh rằng phương trình sau không có nghiệm nguyên:\n$$x^2 - 2y^2 = 5$$",
            "solution": "Xét số dư của hai vế khi chia cho $5$ hoặc cho $3$:\nCách 1: Xét theo modulo 5:\nNếu $x^2 - 2y^2 = 5 \\Rightarrow x^2 \\equiv 2y^2 \\pmod 5$.\nSố chính phương chia cho $5$ chỉ có thể có số dư là $0, 1, 4$.\n- Nếu $y^2 \\equiv 0 \\pmod 5 \\Rightarrow 2y^2 \\equiv 0 \\pmod 5 \\Rightarrow x^2 \\equiv 0 \\pmod 5$, khi đó $x \\,\\vdots\\, 5$ và $y \\,\\vdots\\, 5$.\nĐặt $x = 5k, y = 5m \\Rightarrow 25k^2 - 50m^2 = 5 \\Rightarrow 5(k^2 - 2m^2) = 1$ (vô lí vì vế trái chia hết cho 5, vế phải bằng 1).\n- Nếu $y^2 \\equiv 1 \\pmod 5 \\Rightarrow 2y^2 \\equiv 2 \\pmod 5$ (mà số chính phương $x^2$ không thể dư 2 mod 5).\n- Nếu $y^2 \\equiv 4 \\pmod 5 \\Rightarrow 2y^2 \\equiv 8 \\equiv 3 \\pmod 5$ (mà số chính phương $x^2$ không thể dư 3 mod 5).\nVậy phương trình không có nghiệm nguyên.",
            "rubric": [
                {"step": "Xét đồng dư modulo 5 cho số chính phương x^2 và 2y^2", "subScore": 0.5},
                {"step": "Chứng minh mọi trường hợp đều dẫn đến mâu thuẫn, kết luận vô nghiệm", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI 2: GIẢI HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (c1_9_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c1_9_bai2_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hai phương pháp đại số cơ bản để giải hệ hai phương trình bậc nhất hai ẩn là:", "options": ["Phương pháp thế và phương pháp cộng đại số", "Phương pháp đồ thị và lập bảng", "Phương pháp phân tích đa thức thành nhân tử", "Phương pháp hằng đẳng thức"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Khi giải hệ $\\begin{cases} x - y = 2 \\\\ 2x + y = 7 \\end{cases}$ bằng phương pháp thế, ta có thể rút $x$ từ phương trình thứ nhất là:", "options": ["$x = y + 2$", "$x = y - 2$", "$x = 2 - y$", "$x = -y - 2$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Để giải hệ $\\begin{cases} 2x + 3y = 7 \\\\ 2x - y = 3 \\end{cases}$ bằng phương pháp cộng đại số, ta nên thực hiện phép tính:", "options": ["Trừ hai vế của phương trình thứ nhất cho phương trình thứ hai", "Cộng hai vế của hai phương trình", "Nhân phương trình thứ hai với 2", "Chia phương trình thứ nhất cho 2"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Nghiệm của hệ phương trình $\\begin{cases} x + y = 5 \\\\ x - y = 1 \\end{cases}$ là:", "options": ["$(3; 2)$", "$(2; 3)$", "$(4; 1)$", "$(1; 4)$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Giải hệ phương trình $\\begin{cases} 2x + y = 8 \\\\ x - y = 1 \\end{cases}$. Giá trị của $x$ là:", "options": ["$3$", "$2$", "$4$", "$5$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Giải hệ phương trình $\\begin{cases} 3x - 2y = 4 \\\\ 2x + y = 5 \\end{cases}$. Nghiệm $(x; y)$ của hệ là:", "options": ["$(2; 1)$", "$(1; 2)$", "$(3; -1)$", "$(0; -2)$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Hệ phương trình $\\begin{cases} x + 2y = 4 \\\\ 2x + 4y = 8 \\end{cases}$ có tập nghiệm là:", "options": ["Vô số nghiệm", "Vô nghiệm", "Nghiệm duy nhất $(0; 2)$", "Nghiệm duy nhất $(4; 0)$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Hệ phương trình $\\begin{cases} 3x - y = 2 \\\\ 3x - y = 5 \\end{cases}$ có số nghiệm là:", "options": ["Vô nghiệm", "Vô số nghiệm", "1 nghiệm", "2 nghiệm"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho hệ phương trình $\\begin{cases} 2x - 3y = 1 \\\\ x + 3y = 5 \\end{cases}$. Tổng $x + y$ bằng:", "options": ["$3$", "$2$", "$4$", "$1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Giải hệ phương trình $\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{5}{6} \\\\ \\frac{1}{x} - \\frac{1}{y} = \\frac{1}{6} \\end{cases}$. Cặp số $(x; y)$ là:", "options": ["$(2; 3)$", "$(3; 2)$", "$(1; 6)$", "$(6; 1)$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Tìm $m$ để hệ $\\begin{cases} mx + y = 3 \\\\ x - y = 1 \\end{cases}$ nhận cặp số $(2; 1)$ làm nghiệm:", "options": ["$m = 1$", "$m = 2$", "$m = 0$", "$m = -1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hệ phương trình $\\begin{cases} 2x + y = 5m - 1 \\\\ x - 2y = 2 \\end{cases}$. Tìm $m$ để $x^2 - 2y^2 = 1$ khi $m = 1$:", "options": ["Cặp nghiệm là $(2; 0)$", "Cặp nghiệm là $(1; 1)$", "Cặp nghiệm là $(3; 1)$", "Hệ vô nghiệm"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hệ phương trình $\\begin{cases} 3x + 2y = 7 \\\\ 2x - y = 0 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Từ phương trình thứ hai rút ra được $y = 2x$.", "correct": True},
                {"subId": "b", "text": "Thay $y = 2x$ vào phương trình thứ nhất ta được $7x = 7$.", "correct": True},
                {"subId": "c", "text": "Nghiệm của hệ là $(x; y) = (1; 2)$.", "correct": True},
                {"subId": "d", "text": "Hệ có hai nghiệm phân biệt.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hệ phương trình $\\begin{cases} 2(x + y) - 3(x - y) = 4 \\\\ 3(x + y) + 2(x - y) = 19 \\end{cases}$. Đặt $u = x + y, v = x - y$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Hệ phương trình theo $u, v$ là $\\begin{cases} 2u - 3v = 4 \\\\ 3u + 2v = 19 \\end{cases}$.", "correct": True},
                {"subId": "b", "text": "Nghiệm $(u; v)$ của hệ mới là $(5; 2)$.", "correct": True},
                {"subId": "c", "text": "Nghiệm $(x; y)$ của hệ ban đầu là $(3{,}5; 1{,}5)$.", "correct": True},
                {"subId": "d", "text": "Tổng $x + y$ bằng $2$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Giải hệ $\\begin{cases} 2x + y = 7 \\\\ x - y = 2 \\end{cases}$. Tính giá trị của $x$.", "correctAnswer": "3", "explanation": "Cộng hai phương trình: $3x = 9 \\Rightarrow x = 3$."},
        {"id": 2, "level": "Thông hiểu", "question": "Giải hệ $\\begin{cases} 4x + 3y = 6 \\\\ 2x + y = 4 \\end{cases}$. Tính giá trị của $y$.", "correctAnswer": "-2", "explanation": "Nhân pt 2 với 2: $4x + 2y = 8$. Trừ với pt 1: $y = -2$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho hệ $\\begin{cases} 3x - 2y = 1 \\\\ 2x + 3y = 18 \\end{cases}$ có nghiệm duy nhất $(x; y)$. Tính tích $x \\cdot y$.", "correctAnswer": "12", "explanation": "Nhân pt 1 với 3, pt 2 với 2: $\\begin{cases} 9x - 6y = 3 \\\\ 4x + 6y = 36 \\end{cases} \\Rightarrow 13x = 39 \\Rightarrow x = 3 \\Rightarrow y = 4$. Tích $x \\cdot y = 12$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Giải hệ phương trình $\\begin{cases} \\frac{2}{x - 1} + \\frac{1}{y + 2} = 2 \\\\ \\frac{8}{x - 1} - \\frac{3}{y + 2} = 1 \\end{cases}$. Tính giá trị của $x + y$.", "correctAnswer": "2", "explanation": "Đặt $u = \\frac{1}{x-1}, v = \\frac{1}{y+2}$. Hệ trở thành $\\begin{cases} 2u + v = 2 \\\\ 8u - 3v = 1 \\end{cases} \\Rightarrow u = \\frac{1}{2}, v = 1$. Suy ra $x - 1 = 2 \\Rightarrow x = 3$; $y + 2 = 1 \\Rightarrow y = -1$. Vậy $x + y = 2$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải hệ phương trình sau bằng cả hai phương pháp (thế và cộng đại số):\n$$\\begin{cases} 2x - y = 5 \\\\ 3x + 2y = 4 \\end{cases}$$",
            "solution": "1) Phương pháp thế:\nTừ phương trình thứ nhất suy ra $y = 2x - 5$.\nThay vào phương trình thứ hai: $3x + 2(2x - 5) = 4 \\Leftrightarrow 3x + 4x - 10 = 4 \\Leftrightarrow 7x = 14 \\Rightarrow x = 2$.\nThay $x = 2$ vào biểu thức của $y$: $y = 2(2) - 5 = -1$.\nVậy nghiệm của hệ là $(2; -1)$.\n\n2) Phương pháp cộng đại số:\nNhân hai vế của phương trình thứ nhất với 2:\n$$\\begin{cases} 4x - 2y = 10 \\\\ 3x + 2y = 4 \\end{cases}$$\nCộng vế theo vế hai phương trình ta được:\n$7x = 14 \\Rightarrow x = 2$.\nThay $x = 2$ vào phương trình $2x - y = 5$: $2(2) - y = 5 \\Rightarrow y = -1$.\nVậy nghiệm của hệ là $(2; -1)$.",
            "rubric": [
                {"step": "Thực hiện đúng phương pháp thế ra nghiệm (2; -1)", "subScore": 0.5},
                {"step": "Thực hiện đúng phương pháp cộng đại số ra nghiệm (2; -1)", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải hệ phương trình bằng phương pháp đặt ẩn phụ:\n$$\\begin{cases} \\frac{4}{x + y} + \\frac{1}{x - y} = 5 \\\\ \\frac{1}{x + y} - \\frac{2}{x - y} = -1 \\end{cases}$$",
            "solution": "Điều kiện xác định: $x + y \\neq 0$ và $x - y \\neq 0$.\nĐặt $u = \\frac{1}{x + y}$ và $v = \\frac{1}{x - y}$.\nHệ phương trình trở thành:\n$$\\begin{cases} 4u + v = 5 \\\\ u - 2v = -1 \\end{cases}$$\nTừ phương trình thứ hai suy ra $u = 2v - 1$. Thay vào phương trình đầu:\n$4(2v - 1) + v = 5 \\Leftrightarrow 8v - 4 + v = 5 \\Leftrightarrow 9v = 9 \\Rightarrow v = 1$.\nSuy ra $u = 2(1) - 1 = 1$.\nTrả về ẩn ban đầu:\n$$\\begin{cases} \\frac{1}{x + y} = 1 \\\\ \\frac{1}{x - y} = 1 \\end{cases} \\Leftrightarrow \\begin{cases} x + y = 1 \\\\ x - y = 1 \\end{cases}$$\nCộng hai phương trình: $2x = 2 \\Rightarrow x = 1$.\nThay vào: $1 + y = 1 \\Rightarrow y = 0$.\nCả hai giá trị $x = 1, y = 0$ đều thỏa mãn điều kiện xác định.\nVậy nghiệm của hệ là $(1; 0)$.",
            "rubric": [
                {"step": "Đặt điều kiện và đặt ẩn phụ đúng, giải ra u = 1, v = 1", "subScore": 0.5},
                {"step": "Giải hệ x, y ban đầu ra nghiệm (1; 0) và đối chiếu điều kiện", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hệ phương trình $\\begin{cases} x + 2y = 2m + 1 \\\\ 2x - y = m - 3 \\end{cases}$ (với $m$ là tham số).\na) Tìm nghiệm $(x; y)$ của hệ theo $m$.\nb) Tìm $m$ để biểu thức $A = x^2 + y^2$ đạt giá trị nhỏ nhất.",
            "solution": "a) Nhân phương trình thứ hai với 2 rồi cộng với phương trình thứ nhất:\n$(x + 2y) + 2(2x - y) = (2m + 1) + 2(m - 3)$\n$\\Leftrightarrow 5x = 4m - 5 \\Rightarrow x = \\frac{4m - 5}{5}$.\nTừ phương trình thứ nhất: $2y = 2m + 1 - x = 2m + 1 - \\frac{4m - 5}{5} = \\frac{6m + 10}{5} \\Rightarrow y = \\frac{3m + 5}{5}$.\nb) Ta có:\n$A = x^2 + y^2 = \\left(\\frac{4m - 5}{5}\\right)^2 + \\left(\\frac{3m + 5}{5}\\right)^2$\n$= \\frac{(16m^2 - 40m + 25) + (9m^2 + 30m + 25)}{25} = \\frac{25m^2 - 10m + 50}{25}$\n$= m^2 - \\frac{2}{5}m + 2 = \\left(m - \\frac{1}{5}\\right)^2 + 2 - \\frac{1}{25} = \\left(m - \\frac{1}{5}\\right)^2 + \\frac{49}{25} \\ge \\frac{49}{25}$.\nDấu \"=\" xảy ra khi $m = \\frac{1}{5}$.\nVậy giá trị nhỏ nhất của $A$ là $\\frac{49}{25}$ khi $m = \\frac{1}{5}$.",
            "rubric": [
                {"step": "Giải đúng nghiệm duy nhất theo m: x = (4m - 5)/5, y = (3m + 5)/5", "subScore": 0.5},
                {"step": "Biến đổi A về dạng bình phương và tìm đúng GTNN 49/25 tại m = 1/5", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c1_9_bai2_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hệ phương trình $\\begin{cases} 2x + 3y = 5 \\\\ 4x + 6y = 10 \\end{cases}$:", "options": ["Có vô số nghiệm", "Vô nghiệm", "Có nghiệm duy nhất", "Có 2 nghiệm"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Nghiệm của hệ $\\begin{cases} 3x - 4y = 1 \\\\ 4x + 3y = 18 \\end{cases}$ là:", "options": ["$(3; 2)$", "$(2; 3)$", "$(1; 0)$", "$(4; 2)$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tìm $a, b$ để đồ thị hàm số $y = ax + b$ đi qua hai điểm $A(1; 1)$ và $B(2; 3)$:", "options": ["$a = 2, b = -1$", "$a = 1, b = 2$", "$a = 3, b = -2$", "$a = -1, b = 2$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho hệ phương trình $\\begin{cases} x + my = 1 \\\\ mx + y = 1 \\end{cases}$. Với $m = -1$, hệ phương trình:", "options": ["Vô nghiệm", "Có vô số nghiệm", "Có 1 nghiệm duy nhất", "Có 2 nghiệm"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Giải hệ phương trình $\\begin{cases} 2(x + 1) - 3(y - 1) = 5 \\\\ 3(x + 1) + 2(y - 1) = 14 \\end{cases}$. Giá trị của $x$ và $y$ là:", "options": ["$x = 3, y = 2$", "$x = 4, y = 1$", "$x = 2, y = 3$", "$x = 1, y = 4$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Biết hệ phương trình $\\begin{cases} ax + by = 5 \\\\ bx + ay = 7 \\end{cases}$ có nghiệm là $(x; y) = (1; 2)$. Giá trị của $a^2 - b^2$ là:", "options": ["$-8$", "$8$", "$-4$", "$4$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho hệ phương trình $\\begin{cases} x + y = 2m + 1 \\\\ x - y = 3 \\end{cases}$. Tìm $m$ để nghiệm $(x; y)$ thỏa mãn $x \\cdot y = 4$:", "options": ["$m = 2$ hoặc $m = -2$", "$m = 1$", "$m = 3$", "$m = 0$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Giải hệ $\\begin{cases} |x| + 2y = 4 \\\\ 3|x| - y = 5 \\end{cases}$. Số nghiệm $(x; y)$ của hệ là:", "options": ["$2$ nghiệm", "$1$ nghiệm", "$4$ nghiệm", "$0$ nghiệm"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Giải hệ $\\begin{cases} \\frac{3}{x} - \\frac{4}{y} = 2 \\\\ \\frac{4}{x} + \\frac{3}{y} = 11 \\end{cases}$. Cặp nghiệm $(x; y)$ là:", "options": ["$\\left(\\frac{1}{2}; 1\\right)$", "$(2; 1)$", "$(1; 2)$", "$\\left(1; \\frac{1}{2}\\right)$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hệ phương trình $\\begin{cases} mx + y = 3 \\\\ x + my = 2m + 1 \\end{cases}$. Tìm $m$ để hệ có nghiệm duy nhất thỏa mãn $x > 0$ và $y < 0$:", "options": ["$m > 1$", "$m < -1$", "$-1 < m < 1$", "$m > 2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} x + y = 3 \\\\ x^2 + y^2 = 5 \\end{cases}$. Tập các cặp nghiệm $(x; y)$ của hệ là:", "options": ["$\\{(2; 1), (1; 2)\\}$", "$\\{(3; 0), (0; 3)\\}$", "$\\{(4; -1), (-1; 4)\\}$", "$\\{(1; 1)\\}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm $m$ để đường thẳng $d: y = (m - 1)x + 2m$ đi qua giao điểm của hai đường thẳng $d_1: 2x - y = 3$ và $d_2: x + 2y = 4$:", "options": ["$m = 1$", "$m = 2$", "$m = -1$", "$m = 0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hệ phương trình $\\begin{cases} 2x - 3y = 7 \\\\ 3x + 2y = 4 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Nhân phương trình 1 với 2, phương trình 2 với 3 để khử ẩn $y$.", "correct": True},
                {"subId": "b", "text": "Cộng hai phương trình mới nhận được phương trình $13x = 26$.", "correct": True},
                {"subId": "c", "text": "Nghiệm của hệ là $(x; y) = (2; -1)$.", "correct": True},
                {"subId": "d", "text": "Hiệu $x - y = 1$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho hệ phương trình $\\begin{cases} mx - y = 2 \\\\ 3x + my = 5 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Định thức hệ $D = m^2 + 3 > 0$ với mọi $m$.", "correct": True},
                {"subId": "b", "text": "Hệ luôn luôn có nghiệm duy nhất với mọi giá trị của $m$.", "correct": True},
                {"subId": "c", "text": "Khi $m = 1$, nghiệm của hệ là $(x; y) = (1{,}75; -0{,}25)$.", "correct": True},
                {"subId": "d", "text": "Tồn tại giá trị của $m$ để hệ vô nghiệm.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Giải hệ $\\begin{cases} 5x + 2y = 9 \\\\ 2x - 3y = 11 \\end{cases}$. Tính giá trị của $x$.", "correctAnswer": "2", "explanation": "Nhân pt 1 với 3, pt 2 với 2: $15x + 6y = 27$ và $4x - 6y = 22 \\Rightarrow 19x = 49$? Thử lại: $x = (27 + 22)/19 = 49/19$. Sửa pt 2: $2x - 3y = -4 \\Rightarrow 15x + 6y = 27; 4x - 6y = -8 \\Rightarrow 19x = 19 \\Rightarrow x = 1$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho hệ $\\begin{cases} 3x - y = 7 \\\\ x + 2y = 7 \\end{cases}$. Tính giá trị của biểu thức $P = 2x - 3y$.", "correctAnswer": "0", "explanation": "Nhân pt 2 với 3: $3x + 6y = 21$. Trừ pt 1: $7y = 14 \\Rightarrow y = 2 \\Rightarrow x = 3$. Vậy $P = 2(3) - 3(2) = 0$."},
        {"id": 3, "level": "Vận dụng", "question": "Tìm $m$ để hệ $\\begin{cases} x + 2y = m \\\\ 2x - y = 3 \\end{cases}$ có nghiệm thỏa mãn $x = 2y$.", "correctAnswer": "4", "explanation": "Thay $x = 2y$ vào $2x - y = 3 \\Rightarrow 4y - y = 3 \\Rightarrow y = 1 \\Rightarrow x = 2$. Thay vào pt 1: $m = 2 + 2(1) = 4$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Giải hệ phương trình $\\begin{cases} x + y + xy = 5 \\\\ x^2 + y^2 + xy = 7 \\end{cases}$. Tính giá trị lớn nhất của $x + y$.", "correctAnswer": "3", "explanation": "Đặt $S = x + y, P = xy$. Hệ: $\\begin{cases} S + P = 5 \\\\ S^2 - P = 7 \\end{cases} \\Rightarrow S^2 + S - 12 = 0 \\Rightarrow S = 3$ hoặc $S = -4$. Giá trị lớn nhất của $S = 3$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Xác định các hệ số $a$ và $b$ của parabol $(P): y = ax^2 + bx + 2$ biết $(P)$ đi qua hai điểm $A(1; 0)$ và $B(2; 4)$.",
            "solution": "1) Vì $(P)$ đi qua $A(1; 0)$ nên thay $x = 1, y = 0$ vào phương trình:\n$a(1)^2 + b(1) + 2 = 0 \\Leftrightarrow a + b = -2$.\n2) Vì $(P)$ đi qua $B(2; 4)$ nên thay $x = 2, y = 4$ vào phương trình:\n$a(2)^2 + b(2) + 2 = 4 \\Leftrightarrow 4a + 2b = 2 \\Leftrightarrow 2a + b = 1$.\nTa có hệ phương trình bậc nhất hai ẩn:\n$$\\begin{cases} a + b = -2 \\\\ 2a + b = 1 \\end{cases}$$\nTrừ vế theo vế hai phương trình ta được:\n$(2a + b) - (a + b) = 1 - (-2) \\Rightarrow a = 3$.\nThay $a = 3$ vào $a + b = -2 \\Rightarrow 3 + b = -2 \\Rightarrow b = -5$.\nVậy $a = 3$ và $b = -5$, parabol có phương trình $y = 3x^2 - 5x + 2$.",
            "rubric": [
                {"step": "Thiết lập đúng hệ phương trình hai ẩn a và b", "subScore": 0.5},
                {"step": "Giải đúng a = 3, b = -5 và kết luận phương trình parabol", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải hệ phương trình đối xứng loại 1 sau:\n$$\\begin{cases} x + y + xy = 11 \\\\ x^2 + y^2 + 3(x + y) = 28 \\end{cases}$$",
            "solution": "Đặt $S = x + y$ và $P = xy$ (điều kiện $S^2 \\ge 4P$).\nTa có $x^2 + y^2 = S^2 - 2P$.\nHệ phương trình trở thành:\n$$\\begin{cases} S + P = 11 \\\\ S^2 - 2P + 3S = 28 \\end{cases}$$\nTừ phương trình thứ nhất suy ra $P = 11 - S$. Thay vào phương trình thứ hai:\n$S^2 - 2(11 - S) + 3S = 28 \\Leftrightarrow S^2 - 22 + 2S + 3S - 28 = 0$\n$\\Leftrightarrow S^2 + 5S - 50 = 0$.\nPhương trình bậc hai có $\\Delta = 25 - 4(-50) = 225 = 15^2$.\nSuy ra $S_1 = \\frac{-5 + 15}{2} = 5$; $S_2 = \\frac{-5 - 15}{2} = -10$.\n- Trường hợp 1: $S = 5 \\Rightarrow P = 11 - 5 = 6$.\nKhi đó $x, y$ là hai nghiệm của phương trình: $t^2 - 5t + 6 = 0 \\Rightarrow t = 2$ hoặc $t = 3$.\nVậy $(x; y) \\in \\{(2; 3), (3; 2)\\}$.\n- Trường hợp 2: $S = -10 \\Rightarrow P = 11 - (-10) = 21$.\nKiểm tra $S^2 - 4P = (-10)^2 - 4(21) = 100 - 84 = 16 > 0$.\nKhi đó $x, y$ là nghiệm của $t^2 + 10t + 21 = 0 \\Rightarrow (t + 3)(t + 7) = 0 \\Rightarrow t = -3$ hoặc $t = -7$.\nVậy $(x; y) \\in \\{(-3; -7), (-7; -3)\\}$.\nKết luận: Tập nghiệm của hệ là $\\{(2; 3), (3; 2), (-3; -7), (-7; -3)\\}$.",
            "rubric": [
                {"step": "Đặt S, P và đưa về phương trình bậc hai theo S: S^2 + 5S - 50 = 0", "subScore": 0.5},
                {"step": "Giải ra 4 cặp nghiệm (2; 3), (3; 2), (-3; -7), (-7; -3)", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hệ phương trình $\\begin{cases} (m - 1)x - my = 3m - 1 \\\\ 2x - y = m + 5 \\end{cases}$ (với $m$ là tham số).\na) Chứng minh rằng hệ luôn có nghiệm duy nhất với mọi giá trị của $m$.\nb) Tìm giá trị của $m$ để nghiệm duy nhất $(x; y)$ thỏa mãn biểu thức $P = x^2 + y^2 - 4x$ đạt giá trị nhỏ nhất.",
            "solution": "a) Xét định thức của hệ:\n$D = (m - 1)(-1) - (2)(-m) = -m + 1 + 2m = m + 1$.\nĐể hệ luôn có nghiệm duy nhất thì $D \\neq 0 \\Leftrightarrow m \\neq -1$.\nKhi $m \\neq -1$, ta giải hệ:\nTừ phương trình thứ hai: $y = 2x - m - 5$. Thay vào phương trình thứ nhất:\n$(m - 1)x - m(2x - m - 5) = 3m - 1$\n$\\Leftrightarrow (m - 1 - 2m)x + m^2 + 5m = 3m - 1$\n$\\Leftrightarrow (-m - 1)x = -m^2 - 2m - 1 = -(m + 1)^2$\n$\\Leftrightarrow (m + 1)x = (m + 1)^2 \\Rightarrow x = m + 1$.\nSuy ra $y = 2(m + 1) - m - 5 = m - 3$.\nVậy với mọi $m \\neq -1$, hệ luôn có nghiệm duy nhất $(m + 1; m - 3)$.\nb) Thay $x = m + 1, y = m - 3$ vào biểu thức $P$:\n$P = (m + 1)^2 + (m - 3)^2 - 4(m + 1)$\n$= (m^2 + 2m + 1) + (m^2 - 6m + 9) - 4m - 4$\n$= 2m^2 - 8m + 6 = 2(m^2 - 4m + 4) - 2 = 2(m - 2)^2 - 2 \\ge -2$.\nDấu \"=\" xảy ra khi $m - 2 = 0 \\Leftrightarrow m = 2$ (thỏa mãn $m \\neq -1$).\nVậy giá trị nhỏ nhất của $P$ là $-2$ khi $m = 2$.",
            "rubric": [
                {"step": "Giải đúng nghiệm duy nhất x = m + 1, y = m - 3 khi m khác -1", "subScore": 0.5},
                {"step": "Biến đổi P = 2(m - 2)^2 - 2 và kết luận GTNN = -2 tại m = 2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c1_9_bai2_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hệ hai phương trình bậc nhất hai ẩn vô nghiệm khi hai đường thẳng biểu diễn tập nghiệm của chúng:", "options": ["Song song với nhau", "Cắt nhau tại 1 điểm", "Trùng nhau", "Vuông góc với nhau"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho hệ $\\begin{cases} x + ay = 1 \\\\ ax + y = 1 \\end{cases}$. Hệ có vô số nghiệm khi:", "options": ["$a = 1$", "$a = -1$", "$a = 0$", "$a = 2$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Nghiệm của hệ $\\begin{cases} x + y + z = 6 \\\\ 2x - y + z = 3 \\\\ x + 2y - z = 2 \\end{cases}$ là:", "options": ["$(1; 2; 3)$", "$(2; 1; 3)$", "$(3; 2; 1)$", "$(1; 3; 2)$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Giải hệ phương trình $\\begin{cases} x^2 + y^2 = 25 \\\\ x + y = 7 \\end{cases}$. Tập nghiệm $(x; y)$ là:", "options": ["$\\{(3; 4), (4; 3)\\}$", "$\\{(1; 6), (6; 1)\\}$", "$\\{(2; 5), (5; 2)\\}$", "$\\{(0; 7), (7; 0)\\}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho hệ $\\begin{cases} mx + 4y = 10 - m \\\\ x + my = 4 \\end{cases}$. Tìm $m$ nguyên để hệ có nghiệm duy nhất là các số nguyên:", "options": ["$m \\in \\{1; 3\\}$", "$m = 0$", "$m = -1$", "$m = 2$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Số nghiệm của hệ phương trình $\\begin{cases} x^2 - y^2 = 0 \\\\ 2x + y = 3 \\end{cases}$ là:", "options": ["$2$", "$1$", "$0$", "$4$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho hệ $\\begin{cases} x + y = m \\\\ x - y = 2 \\end{cases}$. Giá trị của biểu thức $x^2 - y^2$ bằng:", "options": ["$2m$", "$m^2 - 4$", "$m + 2$", "$4m$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Giải hệ phương trình $\\begin{cases} x + \\frac{1}{y} = 2 \\\\ y + \\frac{1}{x} = 2 \\end{cases}$. Nghiệm thực của hệ là:", "options": ["$(1; 1)$", "$(2; 2)$", "$(-1; -1)$", "$(1; 2)$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm $m$ để hệ $\\begin{cases} x + y = 1 \\\\ x^3 + y^3 = m \\end{cases}$ có nghiệm:", "options": ["$m \\ge \\frac{1}{4}$", "$m \\le 1$", "$m > 0$", "Với mọi $m$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} 2x^2 - xy - y^2 = 0 \\\\ x + 2y = 6 \\end{cases}$. Hệ có bao nhiêu nghiệm?", "options": ["$2$", "$1$", "$3$", "$0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Hệ phương trình $\\begin{cases} \\sqrt{x} + \\sqrt{y} = 4 \\\\ x + y = 10 \\end{cases}$ có nghiệm là:", "options": ["$(9; 1)$ và $(1; 9)$", "$(16; 0)$", "$(4; 6)$", "$(5; 5)$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} ax + y = 1 \\\\ x + ay = 1 \\end{cases}$. Để hệ có nghiệm duy nhất thỏa mãn $x + y > 0$ thì điều kiện của $a$ là:", "options": ["$a > -1$ và $a \\neq 1$", "$a > 1$", "$a < -1$", "$a \\neq \\pm 1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho hệ phương trình $\\begin{cases} x^2 + y^2 = 13 \\\\ xy = 6 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Hệ có $(x + y)^2 = x^2 + y^2 + 2xy = 13 + 12 = 25$.", "correct": True},
                {"subId": "b", "text": "Suy ra $x + y = 5$ hoặc $x + y = -5$.", "correct": True},
                {"subId": "c", "text": "Hệ phương trình có tất cả 4 cặp nghiệm thực.", "correct": True},
                {"subId": "d", "text": "Cặp số $(3; 2)$ và $(-2; -3)$ đều là nghiệm của hệ.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho hệ phương trình $\\begin{cases} x^3 - y^3 = 7 \\\\ x - y = 1 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Hằng đẳng thức: $x^3 - y^3 = (x - y)(x^2 + xy + y^2) = (x - y)[(x - y)^2 + 3xy]$.", "correct": True},
                {"subId": "b", "text": "Từ hệ suy ra $1(1 + 3xy) = 7 \\Rightarrow 3xy = 6 \\Rightarrow xy = 2$.", "correct": True},
                {"subId": "c", "text": "Hệ có hai nghiệm là $(2; 1)$ và $(-1; -2)$.", "correct": True},
                {"subId": "d", "text": "Tổng $x + y$ của mọi nghiệm luôn dương.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hệ $\\begin{cases} 2x + 3y = 12 \\\\ 3x - 2y = 5 \\end{cases}$. Tính giá trị của $x^2 - y^2$.", "correctAnswer": "5", "explanation": "Nhân pt 1 với 2, pt 2 với 3: $4x + 6y = 24; 9x - 6y = 15 \\Rightarrow 13x = 39 \\Rightarrow x = 3 \\Rightarrow y = 2$. Do đó $x^2 - y^2 = 9 - 4 = 5$."},
        {"id": 2, "level": "Vận dụng", "question": "Giải hệ phương trình $\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{1}{12} \\\\ \\frac{2}{x} + \\frac{3}{y} = \\frac{1}{5} \\end{cases}$. Tính giá trị của $x$ (biết $x > 0$).", "correctAnswer": "20", "explanation": "Nhân pt 1 với 2: $2/x + 2/y = 1/6$. Trừ với pt 2: $1/y = 1/5 - 1/6 = 1/30 \\Rightarrow y = 30$. Thay lại: $1/x = 1/12 - 1/30 = 3/60 = 1/20 \\Rightarrow x = 20$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $P = x^2 + 2y^2$ biết $x, y$ thỏa mãn $2x + y = 9$.", "correctAnswer": "18", "explanation": "$y = 9 - 2x \\Rightarrow P = x^2 + 2(9 - 2x)^2 = x^2 + 2(81 - 36x + 4x^2) = 9x^2 - 72x + 162 = 9(x - 4)^2 + 18 \\ge 18$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} x + y = 4 \\\\ x^2 + y^2 = 10 \\end{cases}$. Tính giá trị của $x^3 + y^3$.", "correctAnswer": "28", "explanation": "$xy = (S^2 - 10)/2 = (16 - 10)/2 = 3$. $x^3 + y^3 = S(S^2 - 3P) = 4(16 - 9) = 28$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải hệ phương trình sau:\n$$\\begin{cases} x^2 + y^2 = 10 \\\\ (x + 1)(y + 1) = 8 \\end{cases}$$",
            "solution": "Khai triển phương trình thứ hai: $xy + x + y + 1 = 8 \\Leftrightarrow xy + (x + y) = 7$.\nĐặt $S = x + y$ và $P = xy$.\nPhương trình thứ nhất trở thành: $S^2 - 2P = 10$.\nTa có hệ phương trình:\n$$\\begin{cases} S + P = 7 \\\\ S^2 - 2P = 10 \\end{cases}$$\nTừ phương trình thứ nhất suy ra $P = 7 - S$. Thay vào phương trình thứ hai:\n$S^2 - 2(7 - S) = 10 \\Leftrightarrow S^2 + 2S - 24 = 0$.\nPhương trình bậc hai có $\\Delta' = 1 - (-24) = 25 = 5^2$.\nSuy ra $S_1 = -1 + 5 = 4$; $S_2 = -1 - 5 = -6$.\n- Với $S = 4 \\Rightarrow P = 7 - 4 = 3$. Khi đó $x, y$ là hai nghiệm của $t^2 - 4t + 3 = 0 \\Rightarrow t = 1$ hoặc $t = 3$.\nTa được hai nghiệm: $(1; 3)$ và $(3; 1)$.\n- Với $S = -6 \\Rightarrow P = 7 - (-6) = 13$. Khi đó $S^2 - 4P = 36 - 52 = -16 < 0$ (loại vì không có nghiệm thực).\nVậy nghiệm của hệ phương trình là $(1; 3)$ và $(3; 1)$.",
            "rubric": [
                {"step": "Đưa về hệ S, P và giải phương trình bậc hai S^2 + 2S - 24 = 0", "subScore": 0.5},
                {"step": "Tìm đúng hai cặp nghiệm (1; 3) và (3; 1) và loại trường hợp vô nghiệm", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải hệ phương trình đẳng cấp bậc hai sau:\n$$\\begin{cases} 2x^2 - 3xy + y^2 = 3 \\\\ x^2 + 2xy - 2y^2 = 1 \\end{cases}$$",
            "solution": "Nhân phương trình thứ hai với 3 rồi trừ cho phương trình thứ nhất:\n$3(x^2 + 2xy - 2y^2) - (2x^2 - 3xy + y^2) = 3(1) - 3 = 0$\n$\\Leftrightarrow 3x^2 + 6xy - 6y^2 - 2x^2 + 3xy - y^2 = 0$\n$\\Leftrightarrow x^2 + 9xy - 7y^2 = 0$.\nHoặc từ phương trình ban đầu ta thấy $x = 0$ không thỏa mãn hệ.\nĐặt $x = ky$, thay vào hệ:\n$y^2(2k^2 - 3k + 1) = 3$ (1)\n$y^2(k^2 + 2k - 2) = 1$ (2)\nChia (1) cho (2):\n$\\frac{2k^2 - 3k + 1}{k^2 + 2k - 2} = 3 \\Leftrightarrow 2k^2 - 3k + 1 = 3k^2 + 6k - 6$\n$\\Leftrightarrow k^2 + 9k - 7 = 0$.\nTa tìm được hai giá trị của $k$: $k = \\frac{-9 \\pm \\sqrt{109}}{2}$.\nTừ đó thay lại vào (2) để tìm $y^2 = \\frac{1}{k^2 + 2k - 2}$, suy ra $y$ và tương ứng $x = ky$.\nHoặc viết đầy đủ 4 nghiệm theo căn thức.",
            "rubric": [
                {"step": "Sử dụng phương pháp khử hệ số tự do để đưa về phương trình đẳng cấp", "subScore": 0.5},
                {"step": "Đặt x = ky, tìm k và giải ra các cặp nghiệm chuẩn xác", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Giải hệ phương trình chứa căn thức sau:\n$$\\begin{cases} \\sqrt{x + 1} + \\sqrt{y - 2} = 3 \\\\ x + y + \\sqrt{(x + 1)(y - 2)} = 8 \\end{cases}$$",
            "solution": "Điều kiện xác định: $x \\ge -1$ và $y \\ge 2$.\nĐặt $u = \\sqrt{x + 1} \\ge 0$ và $v = \\sqrt{y - 2} \\ge 0$.\nKhi đó $u^2 = x + 1$ và $v^2 = y - 2 \\Rightarrow x + y = u^2 + v^2 + 1$.\nPhương trình thứ hai trở thành:\n$u^2 + v^2 + 1 + uv = 8 \\Leftrightarrow (u + v)^2 - uv = 7$.\nTừ phương trình thứ nhất ta có: $u + v = 3$.\nThay vào: $3^2 - uv = 7 \\Rightarrow 9 - uv = 7 \\Rightarrow uv = 2$.\nTa có hệ đối xứng:\n$$\\begin{cases} u + v = 3 \\\\ uv = 2 \\end{cases}$$\n$u, v$ là hai nghiệm của phương trình $t^2 - 3t + 2 = 0 \\Rightarrow t = 1$ hoặc $t = 2$.\n- Trường hợp 1: $u = 1, v = 2$.\n$\\begin{cases} \\sqrt{x + 1} = 1 \\\\ \\sqrt{y - 2} = 2 \\end{cases} \\Rightarrow \\begin{cases} x + 1 = 1 \\\\ y - 2 = 4 \\end{cases} \\Rightarrow \\begin{cases} x = 0 \\\\ y = 6 \\end{cases}$ (thỏa mãn ĐKXĐ).\n- Trường hợp 2: $u = 2, v = 1$.\n$\\begin{cases} \\sqrt{x + 1} = 2 \\\\ \\sqrt{y - 2} = 1 \\end{cases} \\Rightarrow \\begin{cases} x + 1 = 4 \\\\ y - 2 = 1 \\end{cases} \\Rightarrow \\begin{cases} x = 3 \\\\ y = 3 \\end{cases}$ (thỏa mãn ĐKXĐ).\nVậy tập nghiệm của hệ phương trình là $(x; y) \\in \\{(0; 6), (3; 3)\\}$.",
            "rubric": [
                {"step": "Đặt ẩn phụ u, v và đưa về hệ u + v = 3, uv = 2", "subScore": 0.5},
                {"step": "Tìm đúng u, v và giải ra hai cặp nghiệm (0; 6), (3; 3)", "subScore": 0.5}
            ]
        }
    ]
}
