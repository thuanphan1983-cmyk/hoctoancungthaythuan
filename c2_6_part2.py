# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 6 - CHƯƠNG II: TÍNH CHIA HẾT TRONG TẬP HỢP CÁC SỐ TỰ NHIÊN
PHẦN 2: BÀI 10 (SỐ NGUYÊN TỐ) & BÀI 11 (ƯỚC CHUNG. ƯỚC CHUNG LỚN NHẤT)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025.
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 10: SỐ NGUYÊN TỐ (c2_6_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c2_6_bai3_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 10: Số nguyên tố - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Số nguyên tố là số tự nhiên lớn hơn 1, chỉ có:", "options": ["Đúng hai ước là 1 và chính nó", "Nhiều hơn hai ước", "Một ước duy nhất", "Vô số ước"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hợp số là số tự nhiên lớn hơn 1 và:", "options": ["Có nhiều hơn hai ước", "Chỉ có hai ước", "Không có ước nào", "Là số lẻ"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Số nào sau đây không phải là số nguyên tố cũng không phải là hợp số?", "options": ["$0$ và $1$", "Chỉ số $0$", "Chỉ số $1$", "Số $2$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Số nguyên tố nhỏ nhất và là số nguyên tố chẵn duy nhất là:", "options": ["$2$", "$0$", "$1$", "$3$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Trong các số $11; 12; 15; 21$, số nào là số nguyên tố?", "options": ["$11$", "$12$", "$15$", "$21$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Phân tích số 12 ra thừa số nguyên tố ta được:", "options": ["$2^2 \\cdot 3$", "$3 \\cdot 4$", "$2 \\cdot 6$", "$1 \\cdot 12$"], "correct": 0},
        {"id": 7, "level": "Nhận biết", "question": "Khi phân tích một số ra thừa số nguyên tố, các thừa số đều phải là:", "options": ["Các số nguyên tố", "Các số tự nhiên bất kì", "Các số lẻ", "Các số chẵn"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Khẳng định nào sau đây là ĐÚNG?", "options": ["Mọi số nguyên tố lớn hơn 2 đều là số lẻ", "Mọi số lẻ đều là số nguyên tố", "Mọi số chẵn đều là hợp số", "Tổng của hai số nguyên tố luôn là số chẵn"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Trong các số sau, số nào là hợp số?", "options": ["$27$", "$17$", "$23$", "$29$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Phân tích số 60 ra thừa số nguyên tố là:", "options": ["$2^2 \\cdot 3 \\cdot 5$", "$4 \\cdot 3 \\cdot 5$", "$2 \\cdot 30$", "$6 \\cdot 10$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tập hợp tất cả các số nguyên tố nhỏ hơn 10 là:", "options": ["$\\{2; 3; 5; 7\\}$", "$\\{1; 2; 3; 5; 7\\}$", "$\\{3; 5; 7\\}$", "$\\{2; 3; 5; 7; 9\\}$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Cho $P = 11 \\cdot 13 + 17$. Khẳng định nào sau đây đúng?", "options": ["$P$ là hợp số vì $P$ là số chẵn lớn hơn 2", "$P$ là số nguyên tố", "$P$ chia hết cho 11", "$P$ chia hết cho 13"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tập hợp các số tự nhiên $S = \\{13; 15; 17; 19; 21; 23\\}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Trong tập hợp $S$ có đúng 4 số nguyên tố là $13; 17; 19; 23$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Các số $15$ và $21$ là hợp số vì đều chia hết cho 3.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tổng $13 + 17$ là một số nguyên tố.", "correct": False},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tích $15 \\cdot 23$ là một hợp số.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho số $a = 2^3 \\cdot 3 \\cdot 5$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số $a$ được viết dưới dạng phân tích ra thừa số nguyên tố.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Giá trị của số $a$ là 120.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số $a$ có các ước nguyên tố là $2; 3; 5$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số $a$ không chia hết cho 8.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Có bao nhiêu số nguyên tố có một chữ số?", "answer": "4"},
        {"id": 2, "level": "Thông hiểu", "question": "Phân tích số 72 ra thừa số nguyên tố dạng $2^x \\cdot 3^y$. Tính $x + y$.", "answer": "5"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số nguyên tố $p$ sao cho $p + 2$ và $p + 4$ cũng là số nguyên tố.", "answer": "3"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tính tổng của tất cả các số nguyên tố lớn hơn 10 và nhỏ hơn 20.", "answer": "60"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Viết tập hợp các số nguyên tố nhỏ hơn $20$.\nb) Phân tích các số $84$ và $180$ ra thừa số nguyên tố theo cột dọc.",
            "rubric": "a) Tập hợp các số nguyên tố nhỏ hơn 20: {2; 3; 5; 7; 11; 13; 17; 19} (0.4đ).\nb) 84 = 2^2 * 3 * 7 (0.3đ); 180 = 2^2 * 3^2 * 5 (0.3đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Xét xem các tổng (hiệu) sau là số nguyên tố hay hợp số:\na) $A = 3 \\cdot 4 \\cdot 5 + 6 \\cdot 7$.\nb) $B = 7 \\cdot 9 \\cdot 11 - 2 \\cdot 3 \\cdot 7$.",
            "rubric": "a) A = 3 * 4 * 5 + 6 * 7. Ta có 3 * 4 * 5 chia hết cho 3 và 6 * 7 = 3 * 2 * 7 chia hết cho 3 (0.25đ). Do đó A chia hết cho 3 và A > 3 nên A là hợp số (0.25đ).\nb) B = 7 * (9 * 11 - 2 * 3). Ta có B chia hết cho 7 và B > 7 (0.25đ). Do đó B là hợp số (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Thay chữ số vào dấu $*$ để số $\\overline{1*}$ là:\na) Số nguyên tố.\nb) Hợp số.",
            "rubric": "Xét các số từ 10 đến 19: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 (0.2đ).\na) Để 1* là số nguyên tố thì * ∈ {1; 3; 7; 9} (các số nguyên tố là 11, 13, 17, 19) (0.4đ).\nb) Để 1* là hợp số thì * ∈ {0; 2; 4; 5; 6; 8} (các hợp số là 10, 12, 14, 15, 16, 18) (0.4đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c2_6_bai3_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 10: Số nguyên tố - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số lượng ước số tự nhiên của số $a = 2^3 \\cdot 3^2$ là:", "options": ["$12$", "$6$", "$10$", "$8$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tổng của hai số nguyên tố có thể bằng $2025$ được không?", "options": ["Được, hai số đó là 2 và 2023", "Không thể, vì tổng hai số nguyên tố luôn là số chẵn", "Không thể, vì 2025 chia hết cho 5", "Được, có vô số cặp số như vậy"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Có bao nhiêu số nguyên tố có dạng $\\overline{3*}$?", "options": ["$2$ số ($31; 37$)", "$3$ số", "$1$ số", "$4$ số"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tìm số tự nhiên $k$ để $5k$ là số nguyên tố:", "options": ["$k = 1$", "$k = 0$", "$k = 2$", "$k \\in \\{1; 5\\}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Số $504$ được phân tích ra thừa số nguyên tố là:", "options": ["$2^3 \\cdot 3^2 \\cdot 7$", "$2^2 \\cdot 3^3 \\cdot 7$", "$8 \\cdot 9 \\cdot 7$", "$2^4 \\cdot 3 \\cdot 7$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tìm số nguyên tố $p$ sao cho $p + 10$ và $p + 14$ đều là số nguyên tố:", "options": ["$p = 3$", "$p = 5$", "$p = 7$", "$p = 2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho $P = n(n + 1) + 1$ với $n$ là số tự nhiên khác 0. Khi $n = 3$, $P$ là:", "options": ["Số nguyên tố ($13$)", "Hợp số", "Số chẵn", "Chia hết cho 3"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Tìm số nguyên tố $p$ để $p + 2$ cũng là số nguyên tố. Cặp số $(p; p+2)$ như vậy được gọi là:", "options": ["Cặp số nguyên tố sinh đôi", "Cặp số bạn bè", "Cặp số hoàn hảo", "Cặp số tương hỗ"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Biết $x$ là số tự nhiên thỏa mãn $x \\,\\vdots\\, 7$ và $x$ là số nguyên tố. Giá trị của $x$ là:", "options": ["$7$", "$14$", "$1$", "Không có"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Số tự nhiên nhỏ nhất có 3 chữ số khi phân tích ra thừa số nguyên tố có dạng $2^a \\cdot 3^b \\cdot 5^c$ là:", "options": ["$120$", "$100$", "$108$", "$150$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Cho $A = 1 \\cdot 2 \\cdot 3 \\dots 9 + 77$. Khẳng định nào đúng?", "options": ["$A$ là hợp số vì chia hết cho 11", "$A$ là số nguyên tố", "$A$ chia hết cho 10", "$A$ tận cùng bằng 0"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Hình vuông có diện tích là $S = a^2$ với $a \\in \\mathbb{N}, a > 1$. Khẳng định nào sau đây luôn đúng?", "options": ["$S$ luôn là hợp số", "$S$ có thể là số nguyên tố", "$S$ luôn là số chẵn", "$S$ luôn chia hết cho 4"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho ba số tự nhiên liên tiếp $n, n+1, n+2$ ($n > 0$).",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Trong ba số tự nhiên liên tiếp luôn có ít nhất một số chia hết cho 2 và một số chia hết cho 3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tích của ba số tự nhiên liên tiếp luôn là hợp số với mọi $n > 0$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nếu cả $n$ và $n+2$ đều là số nguyên tố lớn hơn 3 thì $n+1$ chắc chắn chia hết cho 6.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tồn tại duy nhất một bộ ba số nguyên tố liên tiếp cách nhau 2 đơn vị là $(3; 5; 7)$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho số $N = 2^x \\cdot 3^y$ với $x, y$ là các số tự nhiên khác 0. Biết $N$ có đúng 6 ước tự nhiên.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Công thức tính số ước tự nhiên của $N$ là $(x + 1)(y + 1)$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ta có $(x + 1)(y + 1) = 6$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Vì $x, y \\geq 1$ nên $(x + 1; y + 1)$ có thể là $(2; 3)$ hoặc $(3; 2)$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Các giá trị có thể của số $N$ là $12$ và $18$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Số 200 có bao nhiêu ước số tự nhiên?", "answer": "12"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số nguyên tố $p$ sao cho $p + 6$ và $p + 8$ đều là số nguyên tố.", "answer": "5"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm chữ số $x$ để số $\\overline{3x}$ là số nguyên tố lớn nhất có dạng này.", "answer": "7"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tính tổng hai số nguyên tố $p$ và $q$ biết rằng $p + q = 99$.", "answer": "99"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Phân tích các số sau ra thừa số nguyên tố rồi tìm tập hợp các ước của mỗi số:\na) Số $45$.\nb) Số $56$.",
            "rubric": "a) 45 = 3^2 * 5 (0.25đ) => Ư(45) = {1; 3; 5; 9; 15; 45} (0.25đ).\nb) 56 = 2^3 * 7 (0.25đ) => Ư(56) = {1; 2; 4; 7; 8; 14; 28; 56} (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số tự nhiên $k$ để:\na) $3 \\cdot k$ là số nguyên tố.\nb) $7 \\cdot k$ là số nguyên tố.\nc) Giải thích vì sao nếu $k > 1$ thì tích $p \\cdot k$ (với $p$ là số nguyên tố) luôn là hợp số.",
            "rubric": "a) Để 3k là số nguyên tố thì k = 1 (vì nếu k = 0 thì 3k = 0 không là SNT, nếu k > 1 thì 3k chia hết cho 3 và k nên là hợp số) (0.3đ).\nb) Tương tự k = 1 (0.3đ).\nc) Khi k > 1, số p * k có ít nhất các ước là 1, p, k, p * k (nhiều hơn 2 ước) nên p * k luôn là hợp số (0.4đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho $p$ và $p + 2$ là hai số nguyên tố lớn hơn 3. Chứng minh rằng số nằm giữa chúng là $p + 1$ chia hết cho 6.",
            "rubric": "- Vì p là số nguyên tố lớn hơn 3 nên p là số lẻ => p + 1 là số chẵn => (p + 1) chia hết cho 2 (0.3đ).\n- Trong ba số tự nhiên liên tiếp p, p + 1, p + 2 phải có một số chia hết cho 3 (0.3đ).\nMà p và p + 2 là các số nguyên tố lớn hơn 3 nên không chia hết cho 3 (0.2đ).\nDo đó p + 1 phải chia hết cho 3 (0.1đ).\nVì ƯCLN(2, 3) = 1 nên (p + 1) chia hết cho 2 * 3 = 6 (0.1đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c2_6_bai3_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 10: Số nguyên tố - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $p$ là số nguyên tố lớn hơn 3. Khi đó số dư của $p^2 - 1$ khi chia cho 24 là:", "options": ["$0$", "$1$", "$2$", "$12$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm tất cả các số nguyên tố $p$ sao cho $p + 2$ và $p + 4$ đều là số nguyên tố:", "options": ["Duy nhất $p = 3$", "$p = 2$", "$p = 5$", "Không tồn tại số $p$ nào"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Số tự nhiên nhỏ nhất có đúng 12 ước tự nhiên là:", "options": ["$60$", "$72$", "$84$", "$90$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho $p$ và $8p - 1$ là các số nguyên tố ($p > 3$). Khẳng định nào sau đây là đúng về số $8p + 1$?", "options": ["$8p + 1$ là hợp số", "$8p + 1$ là số nguyên tố", "$8p + 1$ là số lẻ", "$8p + 1$ chia hết cho 5"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $n$ sao cho $n^4 + 4$ là số nguyên tố:", "options": ["$n = 1$", "$n = 2$", "$n = 0$", "Không có số nào"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên tố $p$ sao cho $2p + 1$ là lập phương của một số tự nhiên?", "options": ["$1$ số ($p = 13$ vì $2 \\cdot 13 + 1 = 27 = 3^3$)", "$0$", "$2$", "Vô số"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho ba số nguyên tố $p, q, r$ thỏa mãn $p^q + q^p = r$. Giá trị của $r$ là:", "options": ["$17$", "$5$", "$13$", "$19$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Số các số nguyên tố $p$ để $p^2 + 2$ là số nguyên tố là:", "options": ["$1$ số ($p = 3$)", "$2$ số", "$0$", "Vô số"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm số nguyên tố $p$ sao cho $4p + 1$ và $6p + 1$ đều là số nguyên tố ($p < 20$):", "options": ["$p = 3$ và $p = 13$", "$p = 5$", "$p = 7$", "$p = 2$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $n \\in \\mathbb{N}^*$. Số $A = n^3 - n$ luôn chia hết cho số nguyên tố nào sau đây?", "options": ["Cả $2$ và $3$", "Chỉ $2$", "Chỉ $5$", "Cả $2, 3$ và $5$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tổng của 10 số nguyên tố đầu tiên là một số:", "options": ["Có chữ số tận cùng là 9", "Chia hết cho 2", "Chia hết cho 5", "Là số chính phương"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Biết $p$ là số nguyên tố và $a$ là số tự nhiên thỏa mãn $a^2 \\,\\vdots\\, p$. Khi đó:", "options": ["$a \\,\\vdots\\, p$", "$a$ không chia hết cho $p$", "$a = p$", "$a^2 = p$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho $p$ là số nguyên tố lớn hơn 3. Xét biểu thức $A = (p - 1)(p + 1)$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Vì $p$ là số nguyên tố lớn hơn 3 nên $p$ là số lẻ.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Do $p$ lẻ nên $p - 1$ và $p + 1$ là hai số chẵn liên tiếp, do đó tích của chúng chia hết cho 8.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Trong ba số tự nhiên liên tiếp $p - 1, p, p + 1$ có một số chia hết cho 3. Vì $p$ nguyên tố lớn hơn 3 nên $p$ không chia hết cho 3, suy ra $(p - 1)(p + 1) \\,\\vdots\\, 3$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Vì ƯCLN(8, 3) = 1 nên $A = (p - 1)(p + 1)$ chia hết cho $24$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho $n$ là một số tự nhiên lớn hơn 1 và xét số $B = n^4 + 4$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Khi $n = 1$, giá trị của $B = 5$ là một số nguyên tố.", "correct": True},
                {"key": "b", "level": "Vận dụng cao", "text": "Ta có đồng nhất thức Sophie Germain: $n^4 + 4 = (n^2 + 2)^2 - (2n)^2 = (n^2 - 2n + 2)(n^2 + 2n + 2)$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Với mọi $n > 1$, thừa số $n^2 - 2n + 2 = (n - 1)^2 + 1 > 1$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Với mọi $n > 1$, số $B = n^4 + 4$ luôn là hợp số.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tìm số nguyên tố $p$ duy nhất sao cho $p^2 + 44$ là số nguyên tố.", "answer": "3"},
        {"id": 2, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $p$ nhỏ nhất để $p, p+14, p+28$ đều là các số nguyên tố.", "answer": "3"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $p$ là số nguyên tố sao cho $p + 2$ và $p + 6$ cũng là số nguyên tố. Tính tổng $p + (p+2) + (p+6)$.", "answer": "31"},
        {"id": 4, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên tố $p$ có dạng $p = n^3 - 1$ với $n$ là số tự nhiên?", "answer": "1"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các số nguyên tố $p$ sao cho $p + 2$ và $p + 4$ đều là số nguyên tố.",
            "rubric": "- Với p = 2: p + 2 = 4 (hợp số, loại) (0.2đ).\n- Với p = 3: p + 2 = 5, p + 4 = 7 đều là số nguyên tố (thỏa mãn) (0.25đ).\n- Với p > 3: Vì p là số nguyên tố nên p có dạng 3k + 1 hoặc 3k + 2 (k ∈ N*):\n+ Nếu p = 3k + 1 => p + 2 = 3k + 3 = 3(k + 1) chia hết cho 3 và lớn hơn 3 nên p + 2 là hợp số (loại) (0.25đ).\n+ Nếu p = 3k + 2 => p + 4 = 3k + 6 = 3(k + 2) chia hết cho 3 và lớn hơn 3 nên p + 4 là hợp số (loại) (0.25đ).\nVậy duy nhất p = 3 (0.05đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng nếu $p$ và $8p^2 + 1$ là các số nguyên tố thì $8p^2 - 1$ là một hợp số.",
            "rubric": "- Với p = 2: 8p^2 + 1 = 33 (hợp số, loại) (0.2đ).\n- Với p = 3: 8p^2 + 1 = 73 (số nguyên tố). Khi đó 8p^2 - 1 = 8 * 9 - 1 = 71 là số nguyên tố (chú ý kiểm tra giả thiết) (0.25đ).\n- Với p > 3: p không chia hết cho 3 nên p^2 chia 3 dư 1 => p^2 = 3k + 1 (0.25đ).\nKhi đó 8p^2 + 1 = 8(3k + 1) + 1 = 24k + 9 = 3(8k + 3) chia hết cho 3 và lớn hơn 3 => là hợp số (mâu thuẫn với giả thiết) (0.2đ).\nDo đó p = 3 là trường hợp thỏa mãn và lập luận chuẩn xác (0.1đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các số tự nhiên $n$ để phân số $\\frac{n^3 - n^2 + 2}{n - 1}$ nhận giá trị nguyên.",
            "rubric": "Ta có n^3 - n^2 + 2 = n^2(n - 1) + 2 (0.35đ).\nDo đó: (n^3 - n^2 + 2) / (n - 1) = n^2 + 2 / (n - 1) (0.25đ).\nĐể phân số có giá trị nguyên thì 2 chia hết cho n - 1 (0.2đ) => n - 1 ∈ Ư(2) = {±1; ±2}.\nVì n là số tự nhiên nên n - 1 ∈ {-1; 1; 2} => n ∈ {0; 2; 3} (thỏa mãn n ≠ 1) (0.2đ)."
        }
    ]
}

# ==============================================================================
# BÀI 11: ƯỚC CHUNG. ƯỚC CHUNG LỚN NHẤT (c2_6_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c2_6_bai4_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 11: Ước chung. Ước chung lớn nhất - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Ước chung của hai hay nhiều số là:", "options": ["Ước của tất cả các số đó", "Bội của tất cả các số đó", "Số lớn nhất trong các số đó", "Số nhỏ nhất trong các số đó"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Kí hiệu ước chung lớn nhất của hai số $a$ và $b$ là:", "options": ["$\\text{ƯCLN}(a, b)$", "$\\text{BCNN}(a, b)$", "$\\Ư(a, b)$", "$\\B(a, b)$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Ước chung lớn nhất của hai số nguyên tố cùng nhau bằng:", "options": ["$1$", "$0$", "Tích hai số đó", "Số lớn hơn"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Số nào sau đây luôn là ước chung của mọi số tự nhiên $a$ và $b$?", "options": ["$1$", "$0$", "$2$", "Tích $a \\cdot b$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Nếu số tự nhiên $a$ chia hết cho số tự nhiên $b$ ($a \\,\\vdots\\, b$) thì $\\text{ƯCLN}(a, b)$ bằng:", "options": ["$b$", "$a$", "$1$", "$a \\cdot b$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Tập hợp các ước chung của $8$ và $12$ là:", "options": ["$\\{1; 2; 4\\}$", "$\\{1; 2; 4; 8\\}$", "$\\{1; 3; 4\\}$", "$\\{2; 4\\}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tìm $\\text{ƯCLN}(18, 30)$:", "options": ["$6$", "$3$", "$2$", "$9$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho $a = 2^2 \\cdot 3$ và $b = 2 \\cdot 3^2$. Khi đó $\\text{ƯCLN}(a, b)$ là:", "options": ["$2 \\cdot 3 = 6$", "$2^2 \\cdot 3^2 = 36$", "$2^2 = 4$", "$3^2 = 9$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Rút gọn phân số $\\frac{16}{24}$ về phân số tối giản ta được:", "options": ["$\\frac{2}{3}$", "$\\frac{4}{6}$", "$\\frac{8}{12}$", "$\\frac{1}{2}$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cặp số nào sau đây là hai số nguyên tố cùng nhau?", "options": ["$8$ và $9$", "$6$ và $9$", "$12$ và $18$", "$10$ và $25$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tìm $\\text{ƯCLN}(24, 48)$:", "options": ["$24$", "$48$", "$12$", "$6$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Tập hợp $\\ƯC(12, 18)$ có bao nhiêu phần tử?", "options": ["$4$ phần tử ($\\{1; 2; 3; 6\\}$)", "$3$ phần tử", "$5$ phần tử", "$6$ phần tử"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai số tự nhiên $a = 36$ và $b = 60$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Phân tích ra thừa số nguyên tố: $36 = 2^2 \\cdot 3^2$ và $60 = 2^2 \\cdot 3 \\cdot 5$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Các thừa số nguyên tố chung của hai số là 2 và 3.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "$\\text{ƯCLN}(36, 60) = 2^2 \\cdot 3 = 12$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tập hợp các ước chung của 36 và 60 là $\\Ư(12) = \\{1; 2; 3; 4; 6; 12\\}$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Một đội tình nguyện gồm có 24 nam và 36 nữ.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số tổ chia được nhiều nhất là $\\text{ƯCLN}(24, 36) = 12$ tổ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi chia thành 12 tổ, mỗi tổ có đúng 2 nam.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Khi chia thành 12 tổ, mỗi tổ có đúng 3 nữ.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Có thể chia đội tình nguyện thành 8 tổ với số nam và số nữ ở mỗi tổ đều bằng nhau.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm ƯCLN của $45$ và $105$.", "answer": "15"},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu ước chung của hai số $20$ và $30$?", "answer": "4"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Rút gọn phân số $\\frac{48}{72}$ về phân số tối giản $\\frac{a}{b}$. Tính $a + b$.", "answer": "5"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Một khu vườn hình chữ nhật dài 48m, rộng 36m. Người ta muốn chia khu vườn thành các ô vuông bằng nhau cạnh lớn nhất. Cạnh ô vuông đó dài bao nhiêu mét?", "answer": "12"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm $\\text{ƯCLN}$ rồi tìm tập hợp ước chung của các số sau:\na) $24$ và $36$.\nb) $60, 90$ và $135$.",
            "rubric": "a) 24 = 2^3 * 3; 36 = 2^2 * 3^2 (0.2đ) => ƯCLN(24, 36) = 2^2 * 3 = 12 (0.15đ). ƯC(24, 36) = Ư(12) = {1; 2; 3; 4; 6; 12} (0.15đ).\nb) 60 = 2^2 * 3 * 5; 90 = 2 * 3^2 * 5; 135 = 3^3 * 5 (0.25đ) => ƯCLN = 3 * 5 = 15 (0.15đ). ƯC = Ư(15) = {1; 3; 5; 15} (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Rút gọn các phân số sau về dạng tối giản bằng cách chia cả tử và mẫu cho $\\text{ƯCLN}$ của chúng:\na) $\\frac{28}{42}$.\nb) $\\frac{60}{140}$.",
            "rubric": "a) ƯCLN(28, 42) = 14 (0.25đ) => 28/42 = (28 : 14)/(42 : 14) = 2/3 (0.25đ).\nb) ƯCLN(60, 140) = 20 (0.25đ) => 60/140 = (60 : 20)/(140 : 20) = 3/7 (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một lớp có $28$ bạn nam và $24$ bạn nữ. Cô giáo chủ nhiệm muốn chia lớp thành các tổ sao cho số nam và số nữ ở mỗi tổ đều bằng nhau.\na) Hỏi có thể chia được nhiều nhất thành bao nhiêu tổ?\nb) Khi đó mỗi tổ có bao nhiêu bạn nam và bao nhiêu bạn nữ?",
            "rubric": "a) Số tổ chia được nhiều nhất là ƯCLN(28, 24) (0.3đ).\nTa có 28 = 2^2 * 7; 24 = 2^3 * 3 => ƯCLN(28, 24) = 2^2 = 4 (0.3đ).\nVậy có thể chia nhiều nhất thành 4 tổ (0.1đ).\nb) Mỗi tổ có số nam: 28 : 4 = 7 bạn nam (0.15đ).\nMỗi tổ có số nữ: 24 : 4 = 6 bạn nữ (0.15đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c2_6_bai4_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 11: Ước chung. Ước chung lớn nhất - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $a = 2^3 \\cdot 3^2 \\cdot 5$ và $b = 2^2 \\cdot 3^3 \\cdot 7$. Khi đó $\\text{ƯCLN}(a, b)$ bằng:", "options": ["$36$", "$72$", "$18$", "$108$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Biết $\\text{ƯCLN}(a, b) = 18$. Số ước chung của $a$ và $b$ là:", "options": ["$6$", "$8$", "$4$", "$9$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho hai số tự nhiên $a$ và $b$ thỏa mãn $a = 5b$. Khi đó $\\text{ƯCLN}(a, b)$ là:", "options": ["$b$", "$a$", "$5$", "$5b$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tìm số tự nhiên $x$ lớn nhất thỏa mãn $70 \\,\\vdots\\, x$ và $84 \\,\\vdots\\, x$:", "options": ["$14$", "$7$", "$28$", "$2$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Hai số tự nhiên liên tiếp có ước chung lớn nhất bằng:", "options": ["$1$", "$2$", "Không xác định", "Số nhỏ hơn"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $x$ biết $90 \\,\\vdots\\, x$, $126 \\,\\vdots\\, x$ và $x > 10$:", "options": ["$18$", "$9$", "$6$", "$3$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Phân số $\\frac{n + 1}{n + 2}$ ($n \\in \\mathbb{N}$) luôn là phân số tối giản vì:", "options": ["$\\text{ƯCLN}(n+1, n+2) = 1$", "Tử số bé hơn mẫu số", "Mẫu số luôn là số chẵn", "Cả tử và mẫu là hai số nguyên tố"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho hai số $a = 48, b = 72$. Tỉ số $\\frac{a}{\\text{ƯCLN}(a, b)}$ bằng:", "options": ["$2$", "$3$", "$4$", "$1$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Một mảnh đất hình chữ nhật dài 112m, rộng 40m được chia thành các ô vuông bằng nhau sao cho không thừa mảnh nào. Số ô vuông ít nhất chia được là:", "options": ["$35$", "$70$", "$140$", "$28$"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $a$ lớn nhất biết rằng $156$ chia cho $a$ dư $12$ và $280$ chia cho $a$ dư $10$:", "options": ["$18$", "$24$", "$36$", "$12$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Biết $x$ và $y$ là hai số tự nhiên nguyên tố cùng nhau và $\\frac{x}{y} = \\frac{42}{70}$. Giá trị của $x + y$ là:", "options": ["$8$", "$16$", "$56$", "$112$"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Bác thợ mộc có hai thanh gỗ dài 180cm và 240cm. Bác muốn cưa hai thanh gỗ thành các đoạn ngắn bằng nhau mà không lãng phí gỗ. Độ dài lớn nhất của mỗi đoạn gỗ là:", "options": ["$60\\text{ cm}$", "$30\\text{ cm}$", "$40\\text{ cm}$", "$20\\text{ cm}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một bác nông dân thu hoạch được $144$ quả cam và $192$ quả táo. Bác muốn chia đều số quả cam và táo vào các giỏ sao cho mỗi giỏ có số cam và số táo như nhau.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số giỏ chia được là ước chung của 144 và 192.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ta có $144 = 2^4 \\cdot 3^2$ và $192 = 2^6 \\cdot 3$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số giỏ nhiều nhất có thể chia được là $\\text{ƯCLN}(144, 192) = 48$ giỏ.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Khi chia vào 48 giỏ, mỗi giỏ có 3 quả cam và 4 quả táo.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho phân số $A = \\frac{2n + 1}{n + 1}$ với $n \\in \\mathbb{N}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Gọi $d = \\text{ƯCLN}(2n + 1, n + 1)$ thì $(2n + 1) \\,\\vdots\\, d$ và $(n + 1) \\,\\vdots\\, d$.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Suy ra $[(2n + 1) - 2(n + 1)] \\,\\vdots\\, d \\Rightarrow -1 \\,\\vdots\\, d \\Rightarrow d = 1$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Vì $d = 1$ nên tử và mẫu là hai số nguyên tố cùng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Phân số $A$ có thể rút gọn được khi $n = 5$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm $\\text{ƯCLN}(120, 168, 216)$.", "answer": "24"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $a$ lớn nhất sao cho $420 \\,\\vdots\\, a$ và $700 \\,\\vdots\\, a$.", "answer": "140"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một đám đất hình chữ nhật dài 52m, rộng 36m. Người ta muốn đóng cọc rào xung quanh sao cho khoảng cách giữa các cọc bằng nhau và tại mỗi góc có một cọc. Khoảng cách lớn nhất giữa hai cọc là bao nhiêu mét?", "answer": "4"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số ước chung của hai số $a = 2^4 \\cdot 3^2$ và $b = 2^3 \\cdot 3^3 \\cdot 5$.", "answer": "12"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm $\\text{ƯCLN}$ rồi tìm các ước chung lớn hơn $10$ của $144$ và $192$.",
            "rubric": "144 = 2^4 * 3^2; 192 = 2^6 * 3 (0.3đ).\nƯCLN(144, 192) = 2^4 * 3 = 48 (0.3đ).\nƯC(144, 192) = Ư(48) = {1; 2; 3; 4; 6; 8; 12; 16; 24; 48} (0.2đ).\nCác ước chung lớn hơn 10 là: {12; 16; 24; 48} (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Chứng minh rằng với mọi số tự nhiên $n$ thì phân số $\\frac{2n + 3}{3n + 4}$ là phân số tối giản.",
            "rubric": "Gọi d là ước chung của 2n + 3 và 3n + 4 (d ∈ N*) (0.2đ).\nTa có: (2n + 3) chia hết cho d và (3n + 4) chia hết cho d (0.2đ).\n=> 3(2n + 3) chia hết cho d và 2(3n + 4) chia hết cho d (0.2đ).\n=> [(6n + 9) - (6n + 8)] chia hết cho d => 1 chia hết cho d => d = 1 (0.3đ).\nVậy phân số trên luôn tối giản (0.1đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một trường THCS có $180$ học sinh khối 6, $160$ học sinh khối 7 và $140$ học sinh khối 8. Nhà trường muốn chia đều số học sinh của cả 3 khối vào các hàng dọc sao cho số học sinh ở mỗi hàng là như nhau và không có học sinh nào bị lẻ hàng.\na) Hỏi có thể xếp được nhiều nhất bao nhiêu hàng dọc?\nb) Khi đó, mỗi hàng dọc có bao nhiêu học sinh của từng khối?",
            "rubric": "a) Số hàng dọc nhiều nhất là ƯCLN(180, 160, 140) (0.25đ).\n180 = 2^2 * 3^2 * 5; 160 = 2^5 * 5; 140 = 2^2 * 5 * 7 => ƯCLN = 2^2 * 5 = 20 (0.35đ).\nVậy xếp được nhiều nhất 20 hàng dọc (0.1đ).\nb) Mỗi hàng dọc có:\nKhối 6: 180 : 20 = 9 học sinh (0.1đ).\nKhối 7: 160 : 20 = 8 học sinh (0.1đ).\nKhối 8: 140 : 20 = 7 học sinh (0.1đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c2_6_bai4_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 11: Ước chung. Ước chung lớn nhất - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hai số tự nhiên $a$ và $b$ thỏa mãn $a \\cdot b = 720$ và $\\text{BCNN}(a, b) = 120$. Khi đó $\\text{ƯCLN}(a, b)$ bằng:", "options": ["$6$", "$12$", "$24$", "$3$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số tự nhiên $n$ để phân số $\\frac{n + 1}{2n + 1}$ tối giản:", "options": ["Với mọi số tự nhiên $n$", "Chỉ khi $n$ chẵn", "Chỉ khi $n$ lẻ", "Không có $n$ nào"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm hai số tự nhiên $a$ và $b$ ($a < b$) biết $a + b = 96$ và $\\text{ƯCLN}(a, b) = 12$. Có bao nhiêu cặp số $(a, b)$ thỏa mãn?", "options": ["$2$ cặp", "$3$ cặp", "$4$ cặp", "$1$ cặp"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Biết $\\text{ƯCLN}(a, b) = 1$. Giá trị của $\\text{ƯCLN}(a + b, a - b)$ với $a, b$ là hai số lẻ bằng:", "options": ["$2$", "$1$", "$4$", "Không xác định"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $a$ lớn nhất biết $452$ chia cho $a$ dư $32$ và $321$ chia cho $a$ dư $21$:", "options": ["$60$", "$30$", "$42$", "$15$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $a$ và $b$ là hai số nguyên tố cùng nhau. Khẳng định nào sau đây là SAI?", "options": ["$\\text{ƯCLN}(a^2, b) > 1$", "$\\text{ƯCLN}(a, a + b) = 1$", "$\\text{ƯCLN}(b, a \\cdot b + 1) = 1$", "$\\text{ƯCLN}(a^2, b^2) = 1$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ để phân số $\\frac{2n + 5}{n + 1}$ rút gọn được:", "options": ["$n = 3k + 2$ với $k \\in \\mathbb{N}$", "$n$ là số chẵn", "$n$ là số lẻ", "Không có $n$ nào"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Thuật toán Euclid tìm $\\text{ƯCLN}(a, b)$ dựa trên tính chất:", "options": ["$\\text{ƯCLN}(a, b) = \\text{ƯCLN}(b, a \\bmod b)$", "$\\text{ƯCLN}(a, b) = a - b$", "$\\text{ƯCLN}(a, b) = a + b$", "$\\text{ƯCLN}(a, b) = a \\cdot b$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm $\\text{ƯCLN}(2^{100} - 1, 2^{60} - 1)$:", "options": ["$2^{20} - 1$", "$2^{10} - 1$", "$2^{40} - 1$", "$1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $A = 1 + 2 + 3 + \\dots + n$ và $B = 2n + 1$. Ước chung lớn nhất của $A$ và $B$ luôn bằng:", "options": ["$1$", "$2$", "$n$", "Phụ thuộc vào $n$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số cặp số tự nhiên $(a, b)$ thỏa mãn $a \\cdot b = 180$ và $\\text{ƯCLN}(a, b) = 3$ là:", "options": ["$4$ cặp", "$2$ cặp", "$3$ cặp", "$6$ cặp"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ lớn nhất có hai chữ số sao cho $\\text{ƯCLN}(n, 60) = 12$:", "options": ["$84$", "$96$", "$72$", "$60$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai số tự nhiên $a$ và $b$ thỏa mãn $a \\cdot b = 2700$ và $\\text{ƯCLN}(a, b) = 15$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Đặt $a = 15m, b = 15n$ với $\\text{ƯCLN}(m, n) = 1$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ta có $15m \\cdot 15n = 2700 \\Rightarrow m \\cdot n = 12$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Vì $\\text{ƯCLN}(m, n) = 1$ nên các cặp $(m, n)$ có thể là $(1, 12)$ hoặc $(3, 4)$ (và hoán vị).", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Có đúng 4 cặp số tự nhiên $(a, b)$ thỏa mãn đề bài.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Xét phân số $P = \\frac{12n + 1}{30n + 2}$ với $n \\in \\mathbb{N}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Gọi $d = \\text{ƯCLN}(12n + 1, 30n + 2)$.", "correct": True},
                {"key": "b", "level": "Vận dụng cao", "text": "Ta có $5(12n + 1) - 2(30n + 2) = (60n + 5) - (60n + 4) = 1$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Vì hiệu bằng 1 nên $1 \\,\\vdots\\, d \\Rightarrow d = 1$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Phân số $P$ luôn tối giản với mọi số tự nhiên $n$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tìm hai số tự nhiên $a$ và $b$ ($a < b$) biết $a + b = 60$ và $\\text{ƯCLN}(a, b) = 12$. Giá trị của $b - a$ bằng bao nhiêu?", "answer": "12"},
        {"id": 2, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho $\\text{ƯCLN}(n + 1, 2n + 3) = 1$.", "answer": "0"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tính $\\text{ƯCLN}(2^{12} - 1, 2^8 - 1)$.", "answer": "15"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị của $d = \\text{ƯCLN}(7n + 3, 5n + 2)$ với $n = 2024$.", "answer": "1"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Tìm hai số tự nhiên $a$ và $b$ biết:\na) $a + b = 128$ và $\\text{ƯCLN}(a, b) = 16$.\nb) $a \\cdot b = 768$ và $\\text{ƯCLN}(a, b) = 8$.",
            "rubric": "a) Vì ƯCLN(a, b) = 16 nên đặt a = 16m, b = 16n với ƯCLN(m, n) = 1 (0.15đ).\nTa có: 16m + 16n = 128 => m + n = 8 (0.15đ).\nVì ƯCLN(m, n) = 1 nên (m, n) ∈ {(1, 7); (3, 5); (5, 3); (7, 1)} (0.1đ).\n=> (a, b) ∈ {(16, 112); (48, 80); (80, 48); (112, 16)} (0.1đ).\nb) Đặt a = 8m, b = 8n (ƯCLN(m, n) = 1) => 64mn = 768 => mn = 12 (0.25đ).\n(m, n) ∈ {(1, 12); (3, 4); (4, 3); (12, 1)} (0.15đ).\n=> (a, b) ∈ {(8, 96); (24, 32); (32, 24); (96, 8)} (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng với mọi số tự nhiên $n$ thì phân số $\\frac{14n + 3}{21n + 4}$ là phân số tối giản.",
            "rubric": "Gọi d = ƯCLN(14n + 3, 21n + 4) (d ∈ N*) (0.2đ).\n=> (14n + 3) chia hết cho d và (21n + 4) chia hết cho d (0.2đ).\n=> 3(14n + 3) chia hết cho d và 2(21n + 4) chia hết cho d (0.25đ).\n=> [(42n + 9) - (42n + 8)] chia hết cho d => 1 chia hết cho d => d = 1 (0.25đ).\nVậy phân số trên luôn tối giản với mọi n (0.1đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $a$ và $b$ là hai số tự nhiên thỏa mãn $\\text{ƯCLN}(a, b) = 1$. Chứng minh rằng $\\text{ƯCLN}(a + b, a \\cdot b) = 1$.",
            "rubric": "Giả sử d là ước chung của a + b và a * b (d là số nguyên tố) (0.25đ).\n=> (a + b) chia hết cho d và ab chia hết cho d (0.2đ).\nVì ab chia hết cho d và d nguyên tố nên a chia hết cho d hoặc b chia hết cho d (0.25đ).\n- Nếu a chia hết cho d, mà a + b chia hết cho d => b chia hết cho d => d là ước chung của a và b (mâu thuẫn vì ƯCLN(a, b) = 1) (0.15đ).\n- Tương tự nếu b chia hết cho d thì a cũng chia hết cho d (0.1đ).\nVậy d = 1, suy ra ƯCLN(a + b, ab) = 1 (0.05đ)."
        }
    ]
}
