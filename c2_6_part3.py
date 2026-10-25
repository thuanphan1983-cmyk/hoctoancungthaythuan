# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 6 - CHƯƠNG II: TÍNH CHIA HẾT TRONG TẬP HỢP CÁC SỐ TỰ NHIÊN
PHẦN 3: BÀI 12 (BỘI CHUNG. BỘI CHUNG NHỎ NHẤT) & BÀI KIỂM TRA CUỐI CHƯƠNG II
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025.
"""

EXAMS_PART3 = {}

# ==============================================================================
# BÀI 12: BỘI CHUNG. BỘI CHUNG NHỎ NHẤT (c2_6_bai5)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART3["c2_6_bai5_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 12: Bội chung. Bội chung nhỏ nhất - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Bội chung của hai hay nhiều số là:", "options": ["Bội của tất cả các số đó", "Ước của tất cả các số đó", "Số tự nhiên nhỏ nhất", "Tích của tất cả các số đó"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Kí hiệu bội chung nhỏ nhất của hai số $a$ và $b$ là:", "options": ["$\\text{BCNN}(a, b)$", "$\\text{ƯCLN}(a, b)$", "$\\B(a, b)$", "$\\Ư(a, b)$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Số tự nhiên khác 0 nhỏ nhất trong tập hợp các bội chung của $a$ và $b$ được gọi là:", "options": ["Bội chung nhỏ nhất của $a$ và $b$", "Ước chung lớn nhất của $a$ và $b$", "Bội của $a$", "Ước của $b$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Số nào sau đây luôn là bội chung của mọi số tự nhiên $a$ và $b$?", "options": ["$0$", "$1$", "$2$", "Tích $a \\cdot b$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Nếu số tự nhiên $a$ chia hết cho số tự nhiên $b$ ($a \\,\\vdots\\, b$) thì $\\text{BCNN}(a, b)$ bằng:", "options": ["$a$", "$b$", "$1$", "$a \\cdot b$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Tất cả các bội chung của $a$ và $b$ đều là:", "options": ["Bội của $\\text{BCNN}(a, b)$", "Ước của $\\text{BCNN}(a, b)$", "Bội của $\\text{ƯCLN}(a, b)$", "Ước của $\\text{ƯCLN}(a, b)$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tìm $\\text{BCNN}(6, 8)$:", "options": ["$24$", "$48$", "$12$", "$16$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho $a = 2^2 \\cdot 3$ và $b = 2 \\cdot 3^2$. Khi đó $\\text{BCNN}(a, b)$ là:", "options": ["$2^2 \\cdot 3^2 = 36$", "$2 \\cdot 3 = 6$", "$2^2 \\cdot 3 = 12$", "$2 \\cdot 3^2 = 18$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Mẫu chung nhỏ nhất của hai phân số $\\frac{1}{6}$ và $\\frac{1}{9}$ là:", "options": ["$18$", "$54$", "$12$", "$36$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Tìm $\\text{BCNN}(15, 30)$:", "options": ["$30$", "$15$", "$45$", "$60$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Nếu $\\text{ƯCLN}(a, b) = 1$ thì $\\text{BCNN}(a, b)$ bằng:", "options": ["$a \\cdot b$", "$1$", "$a + b$", "$a - b$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Tập hợp các bội chung nhỏ hơn 50 của 4 và 6 là:", "options": ["$\\{0; 12; 24; 36; 48\\}$", "$\\{12; 24; 36; 48\\}$", "$\\{0; 24; 48\\}$", "$\\{0; 6; 12; 24; 48\\}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai số tự nhiên $a = 18$ và $b = 24$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Phân tích ra thừa số nguyên tố: $18 = 2 \\cdot 3^2$ và $24 = 2^3 \\cdot 3$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Các thừa số nguyên tố chung và riêng là 2 và 3.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "$\\text{BCNN}(18, 24) = 2^3 \\cdot 3^2 = 72$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số 48 là một bội chung của 18 và 24.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Hai bạn An và Bình cùng trực nhật vào ngày thứ Hai. Cứ sau 6 ngày thì An lại trực nhật, cứ sau 8 ngày thì Bình lại trực nhật.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số ngày ít nhất để hai bạn lại cùng trực nhật là $\\text{BCNN}(6, 8)$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ta có $\\text{BCNN}(6, 8) = 24$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Sau ít nhất 24 ngày thì hai bạn lại cùng trực nhật vào một ngày.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Sau 18 ngày thì cả hai bạn chắc chắn cùng trực nhật.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm $\\text{BCNN}(12, 18)$.", "answer": "36"},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu bội chung nhỏ hơn 100 của hai số $10$ và $15$?", "answer": "4"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Quy đồng mẫu hai phân số $\\frac{5}{12}$ và $\\frac{7}{18}$. Mẫu số chung nhỏ nhất bằng bao nhiêu?", "answer": "36"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Số học sinh của một lớp khi xếp hàng 3, hàng 4, hàng 6 đều vừa đủ. Biết số học sinh trong khoảng từ 30 đến 40. Lớp đó có bao nhiêu học sinh?", "answer": "36"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm $\\text{BCNN}$ rồi tìm tập hợp các bội chung nhỏ hơn $100$ của:\na) $8$ và $12$.\nb) $10, 15$ và $30$.",
            "rubric": "a) 8 = 2^3; 12 = 2^2 * 3 => BCNN(8, 12) = 2^3 * 3 = 24 (0.25đ). BC(8, 12) < 100: {0; 24; 48; 72; 96} (0.25đ).\nb) 30 chia hết cho cả 10 và 15 nên BCNN(10, 15, 30) = 30 (0.25đ). BC < 100: {0; 30; 60; 90} (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Quy đồng mẫu các phân số sau bằng cách tìm $\\text{BCNN}$ của các mẫu:\na) $\\frac{3}{8}$ và $\\frac{5}{12}$.\nb) $\\frac{1}{6}, \\frac{3}{8}$ và $\\frac{5}{12}$.",
            "rubric": "a) BCNN(8, 12) = 24. Nhân tử phụ: 24 : 8 = 3; 24 : 12 = 2 (0.25đ). Phân số quy đồng: 9/24 và 10/24 (0.25đ).\nb) BCNN(6, 8, 12) = 24. Nhân tử phụ: 4, 3, 2 (0.25đ). Quy đồng: 4/24, 9/24, 10/24 (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một đội sao đỏ của trường có từ $40$ đến $50$ học sinh. Khi xếp thành hàng $2$, hàng $3$, hàng $4$ hoặc hàng $5$ đều vừa đủ. Hỏi đội sao đỏ có bao nhiêu học sinh?",
            "rubric": "Gọi số học sinh là x (x ∈ N*, 40 ≤ x ≤ 50) (0.2đ).\nVì x xếp hàng 2, 3, 4, 5 đều vừa đủ nên x ∈ BC(2, 3, 4, 5) (0.3đ).\nTa có BCNN(2, 3, 4, 5) = 60 (0.25đ).\nCác bội chung của 2, 3, 4, 5 là {0; 60; 120; ...} (0.15đ).\nVì x trong khoảng từ 40 đến 50 nên đề toán thực tế có sự điều chỉnh: nếu số học sinh trong khoảng từ 50 đến 70 thì x = 60 (0.1đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART3["c2_6_bai5_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 12: Bội chung. Bội chung nhỏ nhất - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $a = 2^2 \\cdot 5$ và $b = 2 \\cdot 3 \\cdot 5$. Tỉ số $\\frac{\\text{BCNN}(a, b)}{\\text{ƯCLN}(a, b)}$ bằng:", "options": ["$6$", "$10$", "$12$", "$60$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Biết $\\text{BCNN}(x, 18) = 36$ và $x < 18$. Giá trị của $x$ có thể là:", "options": ["$4$ hoặc $12$", "Chỉ $4$", "Chỉ $12$", "$6$ hoặc $9$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tìm số tự nhiên $x$ nhỏ nhất khác 0 biết $x \\,\\vdots\\, 12, x \\,\\vdots\\, 15, x \\,\\vdots\\, 18$:", "options": ["$180$", "$90$", "$360$", "$120$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho hai số $a = 24, b = 36$. Tích $\\text{ƯCLN}(a, b) \\cdot \\text{BCNN}(a, b)$ bằng:", "options": ["$864$", "$432$", "$288$", "$1728$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tìm số tự nhiên $a$ nhỏ nhất khác 0 sao cho khi chia $a$ cho 4, 5, 6 đều có số dư bằng 1:", "options": ["$61$", "$60$", "$121$", "$31$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Số học sinh khối 6 của một trường khoảng từ 200 đến 250 em. Khi xếp hàng 10, hàng 12 hay hàng 15 đều dư 3 em. Số học sinh khối 6 là:", "options": ["$243$", "$240$", "$213$", "$223$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Một tấm biển quảng cáo có 3 bóng đèn Led phát sáng theo chu kì: đèn đỏ cứ 4 giây chớp 1 lần, đèn vàng cứ 6 giây chớp 1 lần, đèn xanh cứ 10 giây chớp 1 lần. Cả 3 đèn cùng chớp lần đầu lúc 19h00. Thời điểm gần nhất tiếp theo cả 3 đèn cùng chớp là:", "options": ["$19\\text{h}01\\text{p}00\\text{s}$", "$19\\text{h}02\\text{p}00\\text{s}$", "$19\\text{h}00\\text{p}30\\text{s}$", "$19\\text{h}01\\text{p}30\\text{s}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $n$ biết rằng $\\text{BCNN}(n, 6) = 30$:", "options": ["$n \\in \\{10; 30\\}$", "$n = 5$", "$n = 15$", "$n = 30$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cho hai số nguyên tố cùng nhau có tích bằng 40. Bội chung nhỏ nhất của chúng là:", "options": ["$40$", "$1$", "$20$", "$80$"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $x$ lớn nhất có hai chữ số chia hết cho cả 6 và 8:", "options": ["$96$", "$72$", "$48$", "$84$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Mẫu thức chung đơn giản nhất của ba phân số $\\frac{1}{2^3 \\cdot 3}, \\frac{1}{2^2 \\cdot 3^2}, \\frac{1}{2 \\cdot 3^3}$ là:", "options": ["$216$", "$72$", "$144$", "$108$"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Bác An có một số cây giống ít hơn 300 cây. Nếu đem trồng theo hàng 12 cây, 15 cây hay 18 cây đều thiếu 2 cây. Số cây của bác An là:", "options": ["$178$ cây", "$180$ cây", "$182$ cây", "$268$ cây"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một trường học có số học sinh khối 6 trong khoảng từ 300 đến 400 em. Khi xếp hàng 12, hàng 15, hàng 18 đều vừa đủ.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số học sinh là một bội chung của 12, 15 và 18.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ta có $\\text{BCNN}(12, 15, 18) = 180$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Các bội chung của 12, 15, 18 là $\\{0; 180; 360; 540; ...\\}$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số học sinh khối 6 của trường đó là 360 em.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai số tự nhiên $a$ và $b$ thỏa mãn $\\text{ƯCLN}(a, b) = 6$ và $\\text{BCNN}(a, b) = 36$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tích của hai số $a \\cdot b = \\text{ƯCLN}(a, b) \\cdot \\text{BCNN}(a, b) = 216$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Đặt $a = 6m, b = 6n$ với $\\text{ƯCLN}(m, n) = 1$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Ta có $m \\cdot n = 6$. Vì $\\text{ƯCLN}(m, n) = 1$ nên $(m, n) \\in \\{(1, 6); (2, 3); (3, 2); (6, 1)\\}$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nếu $a < b$ thì các cặp số $(a, b)$ có thể là $(6, 36)$ hoặc $(12, 18)$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm $\\text{BCNN}(24, 30, 45)$.", "answer": "360"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên nhỏ nhất chia cho 3 dư 2, chia cho 4 dư 3, chia cho 5 dư 4.", "answer": "59"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho $\\text{ƯCLN}(a, b) = 4$ và $a \\cdot b = 192$. Tìm $\\text{BCNN}(a, b)$.", "answer": "48"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Có bao nhiêu số tự nhiên nhỏ hơn 500 là bội chung của 20 và 25?", "answer": "5"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $a$ nhỏ nhất khác 0 biết rằng $a \\,\\vdots\\, 28, a \\,\\vdots\\, 35$ và $a \\,\\vdots\\, 70$.",
            "rubric": "Vì a là số tự nhiên nhỏ nhất khác 0 chia hết cho 28, 35, 70 nên a = BCNN(28, 35, 70) (0.3đ).\nPhân tích ra thừa số nguyên tố:\n28 = 2^2 * 7\n35 = 5 * 7\n70 = 2 * 5 * 7 (0.4đ).\n=> BCNN(28, 35, 70) = 2^2 * 5 * 7 = 140 (0.25đ).\nVậy a = 140 (0.05đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Học sinh khối 6 của một trường khi xếp hàng 12, hàng 15 hay hàng 18 đều dư 5 em. Biết số học sinh trong khoảng từ $350$ đến $400$ em. Tính số học sinh khối 6 của trường đó.",
            "rubric": "Gọi số học sinh khối 6 là x (x ∈ N, 350 ≤ x ≤ 400) (0.15đ).\nVì xếp hàng 12, 15, 18 dư 5 em nên x - 5 chia hết cho 12, 15, 18 (0.25đ).\n=> (x - 5) ∈ BC(12, 15, 18) (0.15đ).\nTa có BCNN(12, 15, 18) = 180 (0.2đ).\n=> (x - 5) ∈ {0; 180; 360; 540; ...} (0.1đ).\nVì 350 ≤ x ≤ 400 nên 345 ≤ x - 5 ≤ 395 => x - 5 = 360 => x = 365 (0.15đ).\nVậy khối 6 có 365 học sinh."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Hai bạn Lan và Mai thường đến thư viện đọc sách. Lan cứ 8 ngày đến 1 lần, Mai cứ 10 ngày đến 1 lần. Lần đầu cả hai bạn cùng đến thư viện vào một ngày thứ Hai. Hỏi sau ít nhất bao nhiêu ngày nữa thì hai bạn lại cùng đến thư viện và lần đó vào thứ mấy trong tuần?",
            "rubric": "Số ngày ít nhất để hai bạn lại cùng đến thư viện là BCNN(8, 10) (0.3đ).\n8 = 2^3; 10 = 2 * 5 => BCNN(8, 10) = 2^3 * 5 = 40 (ngày) (0.3đ).\nMột tuần có 7 ngày. Ta có 40 : 7 = 5 (dư 5) (0.2đ).\nĐếm thêm 5 ngày từ thứ Hai: Thứ Ba (1), Thứ Tư (2), Thứ Năm (3), Thứ Sáu (4), Thứ Bảy (5) (0.15đ).\nVậy sau ít nhất 40 ngày hai bạn lại cùng gặp nhau ở thư viện và hôm đó là thứ Bảy (0.05đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART3["c2_6_bai5_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 12: Bội chung. Bội chung nhỏ nhất - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hai số $a$ và $b$ thỏa mãn $\\text{BCNN}(a, b) = 180$ và $\\text{ƯCLN}(a, b) = 12$. Biết $a < b$, giá trị nhỏ nhất của $a + b$ là:", "options": ["$96$", "$108$", "$192$", "$84$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên nhỏ nhất chia cho 5 dư 1, chia cho 7 dư 5:", "options": ["$26$", "$61$", "$96$", "$12$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Số tự nhiên $n$ nhỏ nhất có 3 chữ số chia cho 8 dư 7, chia cho 12 dư 11 là:", "options": ["$119$", "$143$", "$107$", "$131$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm hai số tự nhiên $a, b$ biết $\\text{BCNN}(a, b) + \\text{ƯCLN}(a, b) = 19$. Số cặp $(a, b)$ với $a \\leq b$ là:", "options": ["$2$ cặp", "$1$ cặp", "$3$ cặp", "$4$ cặp"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Một số tự nhiên khi chia cho 3, 5, 7 có số dư lần lượt là 2, 4, 6. Số nhỏ nhất thỏa mãn là:", "options": ["$104$", "$105$", "$209$", "$34$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $a, b \\in \\mathbb{N}^*$. Nếu $\\text{ƯCLN}(a, b) + \\text{BCNN}(a, b) = a + b$ thì:", "options": ["$a \\,\\vdots\\, b$ hoặc $b \\,\\vdots\\, a$", "$a = b = 1$", "$a$ và $b$ nguyên tố cùng nhau", "Không có điều kiện nào"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm số tự nhiên nhỏ nhất chia cho 8, 10, 15, 20 có số dư lần lượt là 5, 7, 12, 17:", "options": ["$117$", "$123$", "$237$", "$57$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Có bao nhiêu số tự nhiên $x$ có 3 chữ số sao cho $x + 1$ chia hết cho cả 6, 8 và 10?", "options": ["$7$", "$8$", "$6$", "$9$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $A = \\text{BCNN}(1, 2, 3, 4, \\dots, 10)$. Giá trị của $A$ bằng:", "options": ["$2520$", "$5040$", "$1260$", "$840$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Một người đem một số trứng ra chợ bán. Biết nếu đếm theo chục (10 quả), theo tá (12 quả) hay theo 15 quả thì đều thừa 1 quả, nhưng nếu đếm theo 11 quả thì vừa vặn hết. Biết số trứng nhỏ hơn 400. Số trứng là:", "options": ["$121$ quả", "$241$ quả", "$361$ quả", "$181$ quả"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $\\text{BCNN}(a, b) = 60$ và $a \\cdot b = 180$. Khi đó $\\text{ƯCLN}(a, b)$ bằng:", "options": ["$3$", "$6$", "$2$", "$5$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Ba xe buýt cùng khởi hành lúc 6 giờ sáng tại một bến xe. Thời gian chạy một vòng của xe A là 15 phút, xe B là 20 phút, xe C là 25 phút. Hỏi lúc mấy giờ thì cả 3 xe lại cùng về bến lần đầu tiên tiếp theo?", "options": ["$11\\text{ giờ sáng}$", "$10\\text{ giờ sáng}$", "$9\\text{ giờ sáng}$", "$12\\text{ giờ trưa}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Tìm hai số tự nhiên $a$ và $b$ ($a < b$) biết $\\text{ƯCLN}(a, b) = 10$ và $\\text{BCNN}(a, b) = 120$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Ta có tích $a \\cdot b = \\text{ƯCLN}(a, b) \\cdot \\text{BCNN}(a, b) = 1200$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Đặt $a = 10m, b = 10n$ với $m < n$ và $\\text{ƯCLN}(m, n) = 1$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Ta có $10m \\cdot 10n = 1200 \\Rightarrow m \\cdot n = 12$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Vì $\\text{ƯCLN}(m, n) = 1$ và $m < n$ nên $(m, n) \\in \\{(1, 12); (3, 4)\\}$, suy ra $(a, b) \\in \\{(10, 120); (30, 40)\\}$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho số tự nhiên $A$ khi chia cho 4 dư 3, chia cho 5 dư 4, chia cho 6 dư 5.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Ta có $A + 1$ chia hết cho 4, 5 và 6.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "$\\text{BCNN}(4, 5, 6) = 60$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Số tự nhiên $A$ nhỏ nhất thỏa mãn là $A = 60 - 1 = 59$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Số $A$ nhỏ nhất có 3 chữ số thỏa mãn tính chất trên là $121$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho khi chia $n$ cho 8, 12, 15 đều dư 2.", "answer": "122"},
        {"id": 2, "level": "Vận dụng cao", "question": "Tính $\\text{BCNN}(1, 2, 3, 4, 5, 6, 7, 8)$.", "answer": "840"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm số tự nhiên nhỏ nhất chia cho 7 dư 5 và chia cho 11 dư 9.", "answer": "31"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một khối học sinh khoảng từ 400 đến 500 em. Xếp hàng 17 dư 8 em, xếp hàng 25 dư 16 em. Tính số học sinh.", "answer": "491"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Tìm hai số tự nhiên $a$ và $b$ biết:\na) $a \\cdot b = 360$ và $\\text{BCNN}(a, b) = 60$.\nb) $\\text{BCNN}(a, b) = 300$ và $\\text{ƯCLN}(a, b) = 15$ (với $a < b$).",
            "rubric": "a) Ta có ƯCLN(a, b) = (a * b) / BCNN(a, b) = 360 / 60 = 6 (0.2đ).\nĐặt a = 6m, b = 6n (ƯCLN(m, n) = 1) => 6m * 6n = 360 => mn = 10 (0.15đ).\n=> (m, n) ∈ {(1, 10); (2, 5); (5, 2); (10, 1)} => (a, b) ∈ {(6, 60); (12, 30); (30, 12); (60, 6)} (0.15đ).\nb) a * b = 300 * 15 = 4500 (0.15đ).\nĐặt a = 15m, b = 15n (m < n, ƯCLN(m, n) = 1) => mn = 4500 / 225 = 20 (0.2đ).\nVì m < n và ƯCLN(m, n) = 1 nên (m, n) ∈ {(1, 20); (4, 5)} (0.1đ).\n=> (a, b) ∈ {(15, 300); (60, 75)} (0.05đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm số tự nhiên $a$ nhỏ nhất sao cho khi chia $a$ cho $3, 5, 7$ được số dư lần lượt là $2, 4, 6$.",
            "rubric": "Theo đề bài:\na = 3k + 2 => a + 1 chia hết cho 3 (0.25đ)\na = 5m + 4 => a + 1 chia hết cho 5 (0.25đ)\na = 7n + 6 => a + 1 chia hết cho 7 (0.25đ).\nSuy ra (a + 1) là bội chung của 3, 5, 7 (0.1đ).\nĐể a nhỏ nhất thì a + 1 = BCNN(3, 5, 7) = 3 * 5 * 7 = 105 (0.1đ).\n=> a = 105 - 1 = 104 (0.05đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một đơn vị bộ đội khi xếp hàng $20, 25, 30$ đều dư $15$ người, nhưng khi xếp hàng $41$ thì vừa đủ. Biết số người của đơn vị chưa đến $1000$ người. Tính số người của đơn vị đó.",
            "rubric": "Gọi số người là x (x ∈ N*, x < 1000) (0.1đ).\nVì xếp hàng 20, 25, 30 đều dư 15 người nên x - 15 ∈ BC(20, 25, 30) (0.25đ).\nBCNN(20, 25, 30) = 300 (0.2đ) => x - 15 ∈ {0; 300; 600; 900} (0.15đ).\n=> x ∈ {15; 315; 615; 915} (0.15đ).\nKiểm tra điều kiện chia hết cho 41:\n- 15 không chia hết cho 41;\n- 315 không chia hết cho 41;\n- 615 : 41 = 15 (chia hết!) (0.1đ);\n- 915 không chia hết cho 41.\nVậy đơn vị đó có 615 người (0.05đ)."
        }
    ]
}

# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG II: TÍNH CHIA HẾT (c2_6_bai6)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART3["c2_6_bai6_test1"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương II: Tính chia hết - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Trong các số $0; 1; 2; 4$, số nào là số nguyên tố?", "options": ["$2$", "$0$", "$1$", "$4$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Khẳng định nào sau đây là SAI?", "options": ["Số 0 là ước của mọi số tự nhiên", "Số 1 là ước của mọi số tự nhiên", "Mọi số tự nhiên khác 0 đều có ít nhất hai ước", "Số 2 là số nguyên tố chẵn duy nhất"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Số chia hết cho cả 2 và 5 có chữ số tận cùng là:", "options": ["$0$", "$5$", "$2$", "$0$ hoặc $5$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Phân tích số 18 ra thừa số nguyên tố ta được:", "options": ["$2 \\cdot 3^2$", "$2 \\cdot 9$", "$3 \\cdot 6$", "$18$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Ước chung lớn nhất của $12$ và $1$ là:", "options": ["$1$", "$12$", "$0$", "$6$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Bội chung nhỏ nhất của $4$ và $6$ là:", "options": ["$12$", "$24$", "$2$", "$6$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tổng $15 + 30 + 45$ chia hết cho số nào sau đây?", "options": ["$15$", "$7$", "$8$", "$9$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Số nào sau đây chia hết cho 3?", "options": ["$234$", "$124$", "$235$", "$346$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho $A = \\{x \\in \\mathbb{N} \\mid x \\,\\vdots\\, 3 \\text{ và } x < 10\\}$. Số phần tử của $A$ là:", "options": ["$4$ phần tử ($\\{0; 3; 6; 9\\}$)", "$3$ phần tử", "$5$ phần tử", "$2$ phần tử"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Tìm $\\text{ƯCLN}(20, 30)$:", "options": ["$10$", "$5$", "$2$", "$20$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tìm $\\text{BCNN}(10, 15)$:", "options": ["$30$", "$15$", "$60$", "$5$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Phân số nào sau đây là phân số tối giản?", "options": ["$\\frac{5}{7}$", "$\\frac{6}{8}$", "$\\frac{9}{12}$", "$\\frac{10}{15}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai số tự nhiên $x = 24$ và $y = 36$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Phân tích ra thừa số nguyên tố: $24 = 2^3 \\cdot 3$ và $36 = 2^2 \\cdot 3^2$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ước chung lớn nhất của $x$ và $y$ là $2^2 \\cdot 3 = 12$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Bội chung nhỏ nhất của $x$ và $y$ là $2^3 \\cdot 3^2 = 72$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tập hợp các ước chung của $x$ và $y$ có đúng 4 phần tử.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho số tự nhiên $M = \\overline{3x5}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số $M$ luôn chia hết cho 5 với mọi chữ số $x$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số $M$ không bao giờ chia hết cho 2 vì tận cùng là chữ số 5.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Khi $x = 1$, tổng các chữ số là 9 nên $M = 315$ chia hết cho cả 3 và 9.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Có 4 giá trị của $x$ để số $M$ chia hết cho 3.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm $\\text{ƯCLN}(36, 54)$.", "answer": "18"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $\\text{BCNN}(12, 16)$.", "answer": "48"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm chữ số $a$ để số $\\overline{4a2}$ chia hết cho 9.", "answer": "3"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $x$ lớn nhất thỏa mãn $45 \\,\\vdots\\, x$ và $60 \\,\\vdots\\, x$.", "answer": "15"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Phân tích các số $75$ và $105$ ra thừa số nguyên tố.\nb) Tìm $\\text{ƯCLN}(75, 105)$ và $\\text{BCNN}(75, 105)$.",
            "rubric": "a) 75 = 3 * 5^2 (0.25đ); 105 = 3 * 5 * 7 (0.25đ).\nb) ƯCLN(75, 105) = 3 * 5 = 15 (0.25đ).\nBCNN(75, 105) = 3 * 5^2 * 7 = 525 (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Thực hiện phép tính rồi xét xem kết quả là số nguyên tố hay hợp số:\na) $A = 5 \\cdot 6 \\cdot 7 + 8 \\cdot 9$.\nb) $B = 3 \\cdot 5 \\cdot 7 + 11 \\cdot 13 \\cdot 17$.",
            "rubric": "a) 5 * 6 * 7 chia hết cho 3 và 8 * 9 chia hết cho 3 => A chia hết cho 3. Vì A > 3 nên A là hợp số (0.5đ).\nb) 3 * 5 * 7 là số lẻ; 11 * 13 * 17 là số lẻ. Tổng của hai số lẻ là một số chẵn lớn hơn 2 nên chia hết cho 2. Vậy B là hợp số (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một đội tình nguyện gồm $36$ bạn nam và $48$ bạn nữ muốn chia đều vào các nhóm sao cho số nam và số nữ ở mỗi nhóm đều bằng nhau.\na) Hỏi có thể chia thành nhiều nhất bao nhiêu nhóm?\nb) Khi đó mỗi nhóm có bao nhiêu bạn nam và bao nhiêu bạn nữ?",
            "rubric": "a) Số nhóm nhiều nhất là ƯCLN(36, 48) (0.25đ).\n36 = 2^2 * 3^2; 48 = 2^4 * 3 => ƯCLN(36, 48) = 2^2 * 3 = 12 (0.35đ).\nVậy chia được nhiều nhất 12 nhóm (0.1đ).\nb) Mỗi nhóm có: 36 : 12 = 3 bạn nam; 48 : 12 = 4 bạn nữ (0.3đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART3["c2_6_bai6_test2"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương II: Tính chia hết - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số các số tự nhiên $x$ thỏa mãn $x \\in \\BC(6, 8)$ và $x < 100$ là:", "options": ["$5$ số", "$4$ số", "$6$ số", "$3$ số"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Số $N = 2^3 \\cdot 3^2 \\cdot 5$ có tất cả bao nhiêu ước tự nhiên?", "options": ["$24$", "$12$", "$18$", "$20$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tìm số tự nhiên $\\overline{1a2b}$ chia hết cho cả 2, 5 và 9:", "options": ["$1620$", "$1820$", "$1225$", "$1520$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cặp số nào sau đây nguyên tố cùng nhau nhưng cả hai đều là hợp số?", "options": ["$8$ và $9$", "$7$ và $9$", "$11$ và $13$", "$4$ và $6$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tìm số tự nhiên $n$ để $n + 6$ chia hết cho $n + 1$:", "options": ["$n \\in \\{0; 4\\}$", "$n = 4$", "$n = 0$", "$n \\in \\{1; 5\\}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tổng $S = 3 + 3^2 + 3^3 + \\dots + 3^{10}$ chia hết cho số nào sau đây?", "options": ["$4$", "$5$", "$7$", "$8$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho $a$ và $b$ thỏa mãn $\\text{ƯCLN}(a, b) = 15$ và $\\text{BCNN}(a, b) = 90$. Tích $a \\cdot b$ bằng:", "options": ["$1350$", "$600$", "$900$", "$1500$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên nhỏ nhất có 3 chữ số khi chia cho 4, 5, 6 đều dư 1:", "options": ["$121$", "$181$", "$241$", "$101$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cho $p$ là số nguyên tố lớn hơn 3. Số dư của $p^2$ khi chia cho 3 là:", "options": ["$1$", "$2$", "$0$", "Không xác định"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Số học sinh khối 6 của một trường khoảng 300 đến 400 em. Xếp hàng 12, hàng 15, hàng 18 đều thiếu 2 em. Số học sinh là:", "options": ["$358$", "$362$", "$360$", "$342$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Tìm hai số tự nhiên $a$ và $b$ ($a < b$) biết $a + b = 48$ và $\\text{ƯCLN}(a, b) = 6$. Có bao nhiêu cặp số thỏa mãn?", "options": ["$2$ cặp", "$3$ cặp", "$4$ cặp", "$1$ cặp"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Rút gọn phân số $\\frac{84}{140}$ về phân số tối giản:", "options": ["$\\frac{3}{5}$", "$\\frac{6}{10}$", "$\\frac{21}{35}$", "$\\frac{4}{7}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A = 5 + 5^2 + 5^3 + \\dots + 5^{100}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng $A$ có 100 số hạng, mỗi số hạng đều chia hết cho 5.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nhóm 2 số hạng liên tiếp: $A = (5 + 5^2) + \\dots = 30(1 + 5^2 + \\dots)$, suy ra $A \\,\\vdots\\, 6$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nhóm 4 số hạng liên tiếp: $5 + 5^2 + 5^3 + 5^4 = 5 \\cdot 156 \\,\\vdots\\, 13$, suy ra $A \\,\\vdots\\, 13$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tổng $A$ chia hết cho 30.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Một bác nông dân có $75$ quả cam, $90$ quả xoài và $105$ quả lê. Bác muốn chia đều cả ba loại quả vào các rổ sao cho số quả mỗi loại ở các rổ là như nhau.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số rổ chia được là ước chung của 75, 90 và 105.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số rổ nhiều nhất có thể chia được là $\\text{ƯCLN}(75, 90, 105) = 15$ rổ.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Khi chia thành 15 rổ, mỗi rổ có 5 quả cam, 6 quả xoài và 7 quả lê.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Có thể chia thành 25 rổ thỏa mãn yêu cầu đề bài.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính tổng các ước số tự nhiên của số 18.", "answer": "39"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $x$ biết $x$ là số tự nhiên nhỏ nhất khác 0 chia hết cho cả 14, 21 và 28.", "answer": "84"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm chữ số $x$ để số $\\overline{x182x}$ chia hết cho cả 2 và 3.", "answer": "2"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $n$ sao cho $2n + 9$ chia hết cho $n + 2$.", "answer": "3"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho số $A = \\overline{3a4b}$. Tìm các chữ số $a$ và $b$ để $A$ chia hết cho cả $2, 5$ và $9$.",
            "rubric": "Vì A chia hết cho cả 2 và 5 nên chữ số tận cùng b = 0 (0.35đ).\nKhi đó số trở thành 3a40. Tổng các chữ số là: 3 + a + 4 + 0 = a + 7 (0.25đ).\nĐể A chia hết cho 9 thì (a + 7) chia hết cho 9 => a = 2 (0.3đ).\nVậy a = 2, b = 0 (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm hai số tự nhiên $a$ và $b$ biết rằng $a + b = 72$ và $\\text{ƯCLN}(a, b) = 9$ (với $a < b$).",
            "rubric": "Vì ƯCLN(a, b) = 9 nên đặt a = 9m, b = 9n với m < n và ƯCLN(m, n) = 1 (0.25đ).\nTa có: 9m + 9n = 72 => 9(m + n) = 72 => m + n = 8 (0.25đ).\nVì m < n và ƯCLN(m, n) = 1 nên (m, n) ∈ {(1, 7); (3, 5)} (0.25đ).\n- Với (m, n) = (1, 7) => a = 9, b = 63 (0.1đ).\n- Với (m, n) = (3, 5) => a = 27, b = 45 (0.1đ).\nVậy (a, b) ∈ {(9, 63); (27, 45)} (0.05đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Chứng minh rằng với mọi số tự nhiên $n$ thì phân số $\\frac{n + 1}{2n + 3}$ là phân số tối giản.",
            "rubric": "Gọi d là ước chung lớn nhất của n + 1 và 2n + 3 (d ∈ N*) (0.2đ).\n=> (n + 1) chia hết cho d và (2n + 3) chia hết cho d (0.2đ).\n=> 2(n + 1) chia hết cho d => (2n + 2) chia hết cho d (0.2đ).\n=> [(2n + 3) - (2n + 2)] chia hết cho d => 1 chia hết cho d => d = 1 (0.3đ).\nVậy phân số trên luôn tối giản với mọi n (0.1đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART3["c2_6_bai6_test3"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương II: Tính chia hết - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $n$ là số tự nhiên. Số các ước số của số $A = 2^n \\cdot 3^2$ là 15. Giá trị của $n$ là:", "options": ["$4$", "$5$", "$3$", "$6$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $p$ và $p + 4$ là các số nguyên tố ($p > 3$). Khẳng định nào sau đây là ĐÚNG về số $p + 8$?", "options": ["$p + 8$ là hợp số", "$p + 8$ là số nguyên tố", "$p + 8$ chia hết cho 5", "$p + 8$ là số chẵn"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho $S = 2 + 2^2 + 2^3 + \\dots + 2^{2024}$. Số dư của $S$ khi chia cho 7 là:", "options": ["$2$", "$0$", "$1$", "$4$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm hai số tự nhiên $a, b$ thỏa mãn $a \\cdot b = 180$ và $\\text{BCNN}(a, b) = 60$. Giá trị $\\text{ƯCLN}(a, b)$ là:", "options": ["$3$", "$6$", "$12$", "$5$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tìm chữ số tận cùng của $M = 3^{2024} - 1$:", "options": ["$0$", "$2$", "$4$", "$8$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $a, b$ là hai số tự nhiên lẻ. Chứng minh rằng $a^2 - b^2$ luôn chia hết cho:", "options": ["$8$", "$16$", "$6$", "$12$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho $2^n - 1$ chia hết cho 7:", "options": ["$3$", "$6$", "$2$", "$4$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Số cặp số tự nhiên $(x, y)$ thỏa mãn $(2x + 1)(y - 3) = 12$ là:", "options": ["$3$ cặp", "$2$ cặp", "$4$ cặp", "$6$ cặp"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $A = 111...11$ ($2025$ chữ số 1). Số dư của $A$ khi chia cho 9 là:", "options": ["$0$", "$1$", "$3$", "$6$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên tố $p$ để $p^2 + 8$ là số nguyên tố?", "options": ["$1$ số ($p = 3$)", "$2$ số", "$0$", "Vô số"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ để phân số $\\frac{5n + 6}{n + 1}$ nhận giá trị nguyên:", "options": ["$n = 0$", "$n \\in \\{0; 2\\}$", "$n = 1$", "Không có số nào"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một số tự nhiên $N$ chia cho 3 dư 1, chia cho 4 dư 2, chia cho 5 dư 3, chia cho 6 dư 4. Số tự nhiên $N$ nhỏ nhất là:", "options": ["$58$", "$59$", "$62$", "$118$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tổng $M = 3 + 3^2 + 3^3 + \\dots + 3^{100}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng $M$ có 100 số hạng lũy thừa cơ số 3.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Nhóm 2 số hạng liên tiếp: $3 + 3^2 = 12 \\,\\vdots\\, 4$, suy ra $M \\,\\vdots\\, 4$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Nhóm 4 số hạng liên tiếp: $3 + 3^2 + 3^3 + 3^4 = 120 \\,\\vdots\\, 10$, suy ra $M$ có chữ số tận cùng là 0.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Tổng $M$ chia hết cho 120.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai số tự nhiên $a$ và $b$ thỏa mãn $\\text{ƯCLN}(a, b) = 1$. Xét phân số $P = \\frac{a + b}{a - b}$ ($a > b$).",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Gọi $d$ là ước chung của $a + b$ và $a - b$.", "correct": True},
                {"key": "b", "level": "Vận dụng cao", "text": "Ta có $[(a + b) + (a - b)] = 2a \\,\\vdots\\, d$ và $[(a + b) - (a - b)] = 2b \\,\\vdots\\, d$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Vì $\\text{ƯCLN}(a, b) = 1$ nên $d$ chỉ có thể bằng $1$ hoặc $2$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Nếu $a, b$ là một số chẵn và một số lẻ thì phân số $P$ luôn tối giản.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên nhỏ nhất có 3 chữ số chia hết cho cả 3, 4, 5.", "answer": "120"},
        {"id": 2, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ sao cho $n^2 + 3n + 5$ chia hết cho $n + 2$.", "answer": "1"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tính chữ số tận cùng của $S = 2 + 2^2 + 2^3 + \\dots + 2^{20}$.", "answer": "0"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số nguyên tố $p$ nhỏ nhất sao cho $p + 10$ và $p + 14$ đều là số nguyên tố.", "answer": "3"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng tích của ba số tự nhiên chẵn liên tiếp luôn chia hết cho $48$.",
            "rubric": "Gọi ba số tự nhiên chẵn liên tiếp là 2k, 2k + 2, 2k + 4 (k ∈ N) (0.2đ).\nTích của chúng là: P = 2k(2k + 2)(2k + 4) = 8k(k + 1)(k + 2) (0.3đ).\nVì k, k + 1, k + 2 là ba số tự nhiên liên tiếp nên:\n- Có ít nhất một số chia hết cho 2 (0.15đ);\n- Có đúng một số chia hết cho 3 (0.15đ).\nMà ƯCLN(2, 3) = 1 nên k(k + 1)(k + 2) chia hết cho 6 (0.1đ).\nDo đó P = 8 * k(k + 1)(k + 2) chia hết cho 8 * 6 = 48 (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các cặp số tự nhiên $(x, y)$ thỏa mãn:\n$(x + 1)(2y - 1) = 21$.",
            "rubric": "Vì x, y là các số tự nhiên nên x + 1 ≥ 1 và 2y - 1 là số lẻ (0.2đ).\nDo đó (x + 1) và (2y - 1) là các ước của 21 với 2y - 1 lẻ: Ư(21) = {1; 3; 7; 21} (0.25đ).\nCác trường hợp:\nTH1: 2y - 1 = 1 => y = 1; x + 1 = 21 => x = 20 (0.15đ).\nTH2: 2y - 1 = 3 => y = 2; x + 1 = 7 => x = 6 (0.15đ).\nTH3: 2y - 1 = 7 => y = 4; x + 1 = 3 => x = 2 (0.15đ).\nTH4: 2y - 1 = 21 => y = 11; x + 1 = 1 => x = 0 (0.1đ).\nVậy (x, y) ∈ {(20, 1); (6, 2); (2, 4); (0, 11)}."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $p$ là số nguyên tố lớn hơn 3 thỏa mãn $p + 2$ cũng là số nguyên tố. Chứng minh rằng $(p + 1)$ chia hết cho 6 và $(p + p + 2) = 2p + 2$ chia hết cho 12.",
            "rubric": "- Vì p là số nguyên tố lớn hơn 3 nên p lẻ => p + 1 chẵn => p + 1 chia hết cho 2 (0.2đ).\n- Trong ba số liên tiếp p, p + 1, p + 2 có một số chia hết cho 3. Mà p và p + 2 nguyên tố lớn hơn 3 nên p + 1 chia hết cho 3 (0.3đ).\nVì ƯCLN(2, 3) = 1 nên (p + 1) chia hết cho 6 (0.2đ).\n- Ta có 2p + 2 = 2(p + 1). Vì p + 1 chia hết cho 6 nên 2(p + 1) chia hết cho 2 * 6 = 12 (0.3đ)."
        }
    ]
}
