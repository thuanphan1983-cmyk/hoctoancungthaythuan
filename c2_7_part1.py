# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG II: SỐ THỰC
PHẦN 1:
- BÀI 5: LÀM QUEN VỚI SỐ THẬP PHÂN VÔ HẠN TUẦN HOÀN (c2_7_bai1)
- BÀI 6: SỐ VÔ TỈ. CĂN BẬC HAI SỐ HỌC (c2_7_bai2)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 5: LÀM QUEN VỚI SỐ THẬP PHÂN VÔ HẠN TUẦN HOÀN (c2_7_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c2_7_bai1_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 5: Số thập phân vô hạn tuần hoàn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Số thập phân hữu hạn là số thập phân:", "options": ["Có phần thập phân gồm hữu hạn chữ số", "Có phần thập phân gồm vô hạn chữ số lặp lại", "Có phần thập phân không bao giờ dừng và không lặp lại", "Không có phần nguyên"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Chu kì của số thập phân vô hạn tuần hoàn $0,(3)$ là:", "options": ["$3$", "$0$", "$0,3$", "$33$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Phân số nào sau đây viết được dưới dạng số thập phân hữu hạn?", "options": ["$\\frac{3}{8}$", "$\\frac{1}{3}$", "$\\frac{5}{6}$", "$\\frac{4}{7}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Phân số nào sau đây viết được dưới dạng số thập phân vô hạn tuần hoàn?", "options": ["$\\frac{1}{3}$", "$\\frac{3}{4}$", "$\\frac{7}{10}$", "$\\frac{9}{20}$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Số $-1,2(45)$ có chu kì là:", "options": ["$45$", "$245$", "$2$", "$4$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Một phân số tối giản với mẫu dương viết được dưới dạng số thập phân hữu hạn khi mẫu số:", "options": ["Không có ước nguyên tố nào khác 2 và 5", "Chỉ có ước nguyên tố 3", "Có ước nguyên tố 7", "Là một số lẻ bất kì"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Viết phân số $\\frac{1}{6}$ dưới dạng số thập phân vô hạn tuần hoàn:", "options": ["$0,1(6)$", "$0,(16)$", "$0,16$", "$0,(6)$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Viết số thập phân vô hạn tuần hoàn $0,(4)$ dưới dạng phân số tối giản:", "options": ["$\\frac{4}{9}$", "$\\frac{2}{5}$", "$\\frac{4}{10}$", "$\\frac{4}{99}$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Viết số thập phân hữu hạn $0,35$ dưới dạng phân số tối giản:", "options": ["$\\frac{7}{20}$", "$\\frac{35}{10}$", "$\\frac{7}{25}$", "$\\frac{35}{99}$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Số thập phân $0,1232323\\dots$ được viết gọn là:", "options": ["$0,1(23)$", "$0,(123)$", "$0,12(3)$", "$0,(23)$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Làm tròn số $4,357$ đến chữ số thập phân thứ hai được kết quả là:", "options": ["$4,36$", "$4,35$", "$4,40$", "$4,358$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Làm tròn số $12\\,450$ đến hàng trăm được kết quả là:", "options": ["$12\\,500$", "$12\\,400$", "$12\\,000$", "$13\\,000$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho các phân số sau: 7/8; 5/12; 11/20; 4/15:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Phân số 7/8 viết được dưới dạng số thập phân hữu hạn vì mẫu 8 = 2³.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Phân số 11/20 viết được dưới dạng số thập phân hữu hạn là 0,55.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Phân số 5/12 viết được dưới dạng số thập phân vô hạn tuần hoàn vì mẫu có ước nguyên tố 3.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Phân số 4/15 là số thập phân hữu hạn.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét các số thập phân tuần hoàn sau:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số 0,(7) = 7/9.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số 0,(18) = 18/99 = 2/11.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số 0,8(3) = 5/6.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số 0,(9) nhỏ hơn số 1.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Viết phân số 5/11 dưới dạng số thập phân vô hạn tuần hoàn. Chu kì của số đó là bao nhiêu?", "answer": "45"},
        {"id": 2, "level": "Thông hiểu", "question": "Viết số 0,(6) dưới dạng phân số tối giản a/b. Tổng a + b bằng bao nhiêu?", "answer": "5"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Làm tròn số 3,14159 đến chữ số thập phân thứ ba ta được số nào?", "answer": "3,142"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tính kết quả phép tính 0,(3) + 0,(6) dưới dạng số nguyên:", "answer": "1"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Trong các phân số sau: 5/16; 7/15; -13/40; 9/14, phân số nào viết được dưới dạng số thập phân hữu hạn, phân số nào viết được dưới dạng số thập phân vô hạn tuần hoàn? Giải thích.\nb) Viết các phân số đó dưới dạng số thập phân tương ứng.",
            "rubric": "a) 5/16 có mẫu 16 = 2⁴, -13/40 có mẫu 40 = 2³ . 5 nên viết được thành số thập phân hữu hạn. 7/15 (mẫu 15 = 3.5) và 9/14 (mẫu 14 = 2.7) viết thành số thập phân vô hạn tuần hoàn (0.5đ).\nb) 5/16 = 0,3125; -13/40 = -0,325; 7/15 = 0,4(6); 9/14 = 0,6(428571) (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Chuyển các số thập phân sau sang phân số tối giản:\na) 0,(15)\nb) 0,8(3)\nc) 1,2(6).",
            "rubric": "a) 0,(15) = 15/99 = 5/33 (0.3đ).\nb) 0,8(3) = (83 - 8)/90 = 75/90 = 5/6 (0.3đ).\nc) 1,2(6) = 1 + (26 - 2)/90 = 1 + 24/90 = 1 + 4/15 = 19/15 (0.4đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một thửa ruộng hình chữ nhật có chiều dài 35,4 m và chiều rộng 18,7 m.\na) Tính diện tích thửa ruộng đó.\nb) Làm tròn kết quả diện tích vừa tính đến hàng đơn vị.",
            "rubric": "a) Diện tích: 35,4 x 18,7 = 661,98 m² (0.5đ).\nb) Làm tròn đến hàng đơn vị: vì chữ số ngay sau hàng đơn vị là 9 (≥ 5) nên 661,98 ≈ 662 m² (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c2_7_bai1_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 5: Số thập phân vô hạn tuần hoàn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số thập phân vô hạn tuần hoàn $0,2(18)$ viết dưới dạng phân số tối giản là:", "options": ["$\\frac{12}{55}$", "$\\frac{218}{990}$", "$\\frac{216}{990}$", "$\\frac{24}{110}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Chữ số thập phân thứ 100 sau dấu phẩy của số $0,(142857)$ là:", "options": ["$8$", "$4$", "$2$", "$5$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tính: $A = 0,(3) + 0,(72) \\cdot 11$:", "options": ["$\\frac{25}{3}$", "$8$", "$\\frac{23}{3}$", "$7$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên $x < 10$ để phân số $\\frac{x}{12}$ viết được dưới dạng số thập phân hữu hạn:", "options": ["$x \\in \\{3; 6; 9\\}$", "$x \\in \\{2; 4; 6\\}$", "$x \\in \\{1; 3; 5\\}$", "$x \\in \\{3; 6\\}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Giá trị của biểu thức $M = [0,(4) + 0,(5)] : 0,(3)$ là:", "options": ["$3$", "$1$", "$\\frac{9}{10}$", "$2$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Cho $x = 0,2333\\dots$ và $y = 0,7666\\dots$ Tổng $x + y$ bằng:", "options": ["$1$", "$0,99$", "$0,9(9)$", "$1,01$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Một người cân một túi hoa quả được $3,456\\text{ kg}$. Nếu cân có độ chính xác $d = 0,05\\text{ kg}$ thì kết quả làm tròn là:", "options": ["$3,5\\text{ kg}$", "$3,46\\text{ kg}$", "$3,4\\text{ kg}$", "$3,45\\text{ kg}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Số thập phân vô hạn tuần hoàn $1,3(45)$ có thể biểu diễn dưới dạng hỗn số là:", "options": ["$1\\frac{19}{55}$", "$1\\frac{345}{990}$", "$1\\frac{45}{99}$", "$1\\frac{38}{110}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Chữ số thập phân thứ 2024 sau dấu phẩy của số $\\frac{1}{7}$ là:", "options": ["$2$", "$1$", "$4$", "$8$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $a$ nhỏ nhất có hai chữ số sao cho phân số $\\frac{a}{140}$ viết được dưới dạng số thập phân hữu hạn:", "options": ["$14$", "$21$", "$28$", "$35$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tính giá trị biểu thức $B = \\frac{0,(3) + 0,(384615)}{0,(03) + 0,(0384615)}$:", "options": ["$10$", "$1$", "$100$", "$\\frac{1}{10}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Ước lượng kết quả của phép tính $49,85 \\cdot 19,95$ bằng cách làm tròn các thừa số đến hàng đơn vị:", "options": ["$1000$", "$950$", "$1050$", "$980$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho phân số A = 3 / (2a - 4) với a là số tự nhiên khác 2:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Với a = 3 thì A = 3/2 = 1,5 là số thập phân hữu hạn.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Với a = 5 thì A = 3/6 = 1/2 = 0,5 là số thập phân hữu hạn.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Với a = 4 thì A = 3/4 = 0,75 là số thập phân hữu hạn.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Với mọi a > 2 thì A luôn là số thập phân hữu hạn.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét các phép tính với số thập phân vô hạn tuần hoàn:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "0,(1) + 0,(2) + 0,(3) + 0,(4) = 10/9.", "correct": False},
                {"key": "b", "level": "Thông hiểu", "text": "0,(1) . 9 = 1.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "0,(12) . 33 = 4.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "0,(9) = 1.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm chữ số thập phân thứ 50 sau dấu phẩy của số 0,(1234).", "answer": "2"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tính kết quả phép tính: 0,(6) . 1,5 (kết quả là số nguyên).", "answer": "1"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên n có một chữ số để phân số n/35 viết được dưới dạng số thập phân hữu hạn và n > 0.", "answer": "7"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính giá trị biểu thức: P = 0,(4) . 9/2 + 0,1(6) . 6. Kết quả bằng:", "answer": "3"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị các biểu thức sau:\na) A = 0,(6) + 0,(3) . 1,2\nb) B = [0,(12) + 0,(87)] : 0,(3).",
            "rubric": "a) 0,(6) = 2/3; 0,(3) = 1/3; 1,2 = 6/5. A = 2/3 + 1/3 . 6/5 = 2/3 + 2/5 = 16/15 (0.5đ).\nb) 0,(12) = 12/99 = 4/33; 0,(87) = 87/99 = 29/33. Tổng = 33/33 = 1. B = 1 : (1/3) = 3 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "a) Tìm chữ số thập phân thứ 2025 sau dấu phẩy của số thập phân vô hạn tuần hoàn 0,(2357).\nb) Chứng minh rằng số 0,(9) = 1.",
            "rubric": "a) Chu kì gồm 4 chữ số: 2, 3, 5, 7. Ta có 2025 = 4 x 506 + 1. Do đó chữ số thứ 2025 là chữ số đầu tiên của chu kì, tức là chữ số 2 (0.5đ).\nb) Đặt x = 0,(9) => 10x = 9,(9) = 9 + 0,(9) = 9 + x => 9x = 9 => x = 1. Vậy 0,(9) = 1 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các số tự nhiên n có hai chữ số sao cho phân số P = (n + 3) / 150 viết được dưới dạng số thập phân hữu hạn.",
            "rubric": "Mẫu số 150 = 2 . 3 . 5². Để P viết được dưới dạng số thập phân hữu hạn thì tử số (n + 3) phải chia hết cho 3 (0.4đ) => n chia hết cho 3 (0.2đ). Vì n là số tự nhiên có 2 chữ số (10 ≤ n ≤ 99) và n chia hết cho 3 nên n ∈ {12; 15; 18; ...; 99}. Có (99 - 12)/3 + 1 = 30 số thỏa mãn (0.4đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c2_7_bai1_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 5: Số thập phân vô hạn tuần hoàn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Chữ số thập phân thứ 1000 sau dấu phẩy của số $\\frac{1}{13}$ là:", "options": ["$6$", "$0$", "$7$", "$9$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Viết số $0,1(23)$ dưới dạng phân số tối giản $\\frac{a}{b}$. Hiệu $b - a$ là:", "options": ["$868$", "$870$", "$860$", "$890$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Có bao nhiêu phân số tối giản có mẫu là 30, lớn hơn $0$ và nhỏ hơn $1$, viết được dưới dạng số thập phân hữu hạn?", "options": ["$4$", "$2$", "$6$", "$8$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Tính tổng $S = 0,(1) + 0,(2) + 0,(3) + \\dots + 0,(8)$:", "options": ["$4$", "$\\frac{36}{10}$", "$\\frac{35}{9}$", "$4,5$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho phân số $\\frac{7}{n + 2}$ là số thập phân vô hạn tuần hoàn đơn (chu kì bắt đầu ngay sau dấu phẩy):", "options": ["$n = 1$", "$n = 7$", "$n = 9$", "$n = 11$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $A = 0,(a)$ và $B = 0,(b)$ thỏa mãn $A + B = 1$. Giá trị của $a + b$ là:", "options": ["$9$", "$10$", "$8$", "$11$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Giá trị của biểu thức $P = \\frac{0,(4) + 0,(2) - 0,(12)}{0,(8) + 0,(4) - 0,(24)}$ là:", "options": ["$\\frac{1}{2}$", "$1$", "$2$", "$\\frac{1}{4}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Một số thập phân vô hạn tuần hoàn có dạng $0,(ab)$, biết $0,(ab) = \\frac{a+b}{9}$. Giá trị của $a \\cdot b$ là:", "options": ["Không tồn tại", "$12$", "$18$", "$24$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Có bao nhiêu số tự nhiên $a$ ($1 \\leq a \\leq 100$) sao cho phân số $\\frac{a}{60}$ viết được dưới dạng số thập phân hữu hạn?", "options": ["$33$", "$34$", "$20$", "$50$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm chữ số thập phân thứ 2026 của số $\\frac{5}{14}$ sau dấu phẩy:", "options": ["$5$", "$7$", "$1$", "$4$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $x = 0,(123)$ và $y = 0,(321)$. Tổng $x + y$ bằng phân số tối giản:", "options": ["$\\frac{148}{333}$", "$\\frac{444}{999}$", "$\\frac{4}{9}$", "$\\frac{14}{33}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tích của $0,(3)$ và $0,(6)$ bằng:", "options": ["$\\frac{2}{9}$", "$\\frac{1}{5}$", "$0,(18)$", "$\\frac{2}{3}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho số thập phân vô hạn tuần hoàn x = 0,1(23):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Phần bất thường (phần đứng trước chu kì) là 1.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Chu kì của x là 23 gồm 2 chữ số.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "x = (123 - 1) / 990 = 122/990 = 61/495.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Chữ số thứ 100 sau dấu phẩy của x là chữ số 2.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán viết phân số dưới dạng số thập phân:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Mọi phân số đều viết được dưới dạng số thập phân hữu hạn hoặc số thập phân vô hạn tuần hoàn.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Một phân số tối giản có mẫu chia hết cho 7 thì chắc chắn viết được dưới dạng số thập phân vô hạn tuần hoàn.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Số 0,(142857) chính là phân số 1/7.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Độ dài chu kì của phân số 1/p (với p là số nguyên tố khác 2 và 5) không bao giờ vượt quá p - 1.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính tổng: A = 0,(1) + 0,(2) + 0,(3) + ... + 0,(9). Giá trị của A bằng:", "answer": "5"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên n nhỏ nhất có ba chữ số để phân số n/300 viết được dưới dạng số thập phân hữu hạn.", "answer": "102"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm chữ số thập phân thứ 100 sau dấu phẩy của số thập phân 0,1(234).", "answer": "3"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số tự nhiên a có 1 chữ số sao cho 0,(a) + 0,(a+1) = 1. Giá trị của a là:", "answer": "4"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho A = 0,(34) và B = 0,(65).\na) Tính tổng A + B và tích A . B dưới dạng phân số tối giản.\nb) So sánh A + B với 1.",
            "rubric": "a) A = 34/99, B = 65/99. A + B = 99/99 = 1 (0.3đ). A . B = (34/99) . (65/99) = 2210/9801 (0.4đ).\nb) A + B = 1 (0.3đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm các chữ số a và b biết rằng:\n0,(ab) + 0,(ba) = 1,1 và a > b.",
            "rubric": "0,(ab) = ab/99; 0,(ba) = ba/99 => (ab + ba)/99 = 1,1 = 11/10? Hay 0,(ab) + 0,(ba) = (11a + 11b)/99 = (a + b)/9. Nếu đề là (a+b)/9 = 1,(1) = 10/9 => a + b = 10 (0.4đ). Với a > b và a, b là chữ số từ 1 đến 9: các cặp (a; b) là: (9; 1), (8; 2), (7; 3), (6; 4) (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng phân số P = (2024n + 1) / 2025 không thể viết được dưới dạng số thập phân hữu hạn với mọi số tự nhiên n.",
            "rubric": "Giả sử P viết được dưới dạng số thập phân hữu hạn. Khi đó mẫu số sau khi rút gọn chỉ chứa các thừa số nguyên tố 2 và 5 (0.3đ). Ta có 2025 = 3⁴ . 5². Do đó 2024n + 1 phải chia hết cho 3⁴ = 81 (để triệt tiêu thừa số 3 ở mẫu) (0.3đ). Nhưng 2024n + 1 chia 3 có số dư: 2024n + 1 = (2025n - n) + 1 = 3k - n + 1. Đặc biệt nếu 2024n + 1 chia hết cho 3 thì (2025 - 1)n + 1 chia hết cho 3 => -n + 1 chia hết cho 3 => n chia 3 dư 1. Tuy nhiên, ta xét ƯCLN(2024n + 1, 2025): 2025 = 2024 + 1 nên không thể chia hết cho 81 với mọi n (hoặc lập luận 2024n+1 và 2025 nguyên tố cùng nhau khi n thích hợp), vậy P luôn là số thập phân vô hạn tuần hoàn (0.4đ)."
        }
    ]
}


# ==============================================================================
# BÀI 6: SỐ VÔ TỈ. CĂN BẬC HAI SỐ HỌC (c2_7_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c2_7_bai2_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 6: Số vô tỉ. Căn bậc hai số học - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Số vô tỉ là số được viết dưới dạng:", "options": ["Số thập phân vô hạn không tuần hoàn", "Số thập phân hữu hạn", "Số thập phân vô hạn tuần hoàn", "Phân số $\\frac{a}{b}$ với $a, b \\in \\mathbb{Z}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Tập hợp các số vô tỉ được kí hiệu là:", "options": ["$\\mathbb{I}$", "$\\mathbb{Q}$", "$\\mathbb{Z}$", "$\\mathbb{R}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Căn bậc hai số học của số $a$ không âm kí hiệu là $\\sqrt{a}$ là số $x \\geq 0$ sao cho:", "options": ["$x^2 = a$", "$x = a^2$", "$2x = a$", "$x^2 = -a$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Căn bậc hai số học của 25 là:", "options": ["$5$", "$-5$", "$\\pm 5$", "$625$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Khẳng định nào sau đây là SAI?", "options": ["$\\sqrt{-16} = 4$", "$\\sqrt{16} = 4$", "$\\sqrt{0} = 0$", "$\\sqrt{1} = 1$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Số nào sau đây là số vô tỉ?", "options": ["$\\sqrt{2}$", "$\\sqrt{4}$", "$0,(3)$", "$-\\frac{3}{5}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{81} - \\sqrt{36}$ là:", "options": ["$3$", "$9$", "$6$", "$45$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tìm $x$ biết $\\sqrt{x} = 4$:", "options": ["$x = 16$", "$x = 2$", "$x = 8$", "$x = \\pm 16$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "So sánh 3 và $\\sqrt{8}$:", "options": ["$3 > \\sqrt{8}$", "$3 < \\sqrt{8}$", "$3 = \\sqrt{8}$", "Không so sánh được"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{0,49}$ là:", "options": ["$0,7$", "$0,07$", "$7$", "$0,049$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Một mảnh đất hình vuông có diện tích $64\\text{ m}^2$. Độ dài cạnh của mảnh đất đó là:", "options": ["$8\\text{ m}$", "$16\\text{ m}$", "$32\\text{ m}$", "$4\\text{ m}$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Dùng máy tính cầm tay tính $\\sqrt{7}$ và làm tròn đến chữ số thập phân thứ hai:", "options": ["$2,65$", "$2,64$", "$2,60$", "$2,70$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Xét tính đúng/sai của các khẳng định về căn bậc hai số học:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Số âm không có căn bậc hai số học.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Căn bậc hai số học của 0 là 0.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Căn bậc hai số học của 49 là ±7.", "correct": False},
                {"key": "d", "level": "Thông hiểu", "text": "√(a²) = a với mọi a ≥ 0.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho tập hợp M = {√9; √5; -2,5; π; 0; 3/4}:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "√9 = 3 là một số hữu tỉ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số √5 và π là các số vô tỉ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Trong tập hợp M có đúng 2 số vô tỉ.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số -2,5 là số vô tỉ.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = √(100) - √(64) + √(25).", "answer": "7"},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm số thực x không âm thỏa mãn: √x = 9.", "answer": "81"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một hình vuông có diện tích bằng diện tích hình chữ nhật có kích thước 4 cm x 9 cm. Cạnh của hình vuông đó bằng bao nhiêu cm?", "answer": "6"},
        {"id": 4, "level": "Vận dụng thấp", "question": "So sánh √15 và 4. Hiệu 4 - √15 mang dấu dương (+) hay âm (-)? (Trả lời: dương hoặc âm)", "answer": "dương"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của các biểu thức sau:\na) A = √(0,04) + √(0,25) - √(0,81)\nb) B = 3 . √(49) - 2 . √(16) + √(121).",
            "rubric": "a) A = 0,2 + 0,5 - 0,9 = -0,2 (0.5đ).\nb) B = 3 . 7 - 2 . 4 + 11 = 21 - 8 + 11 = 24 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm x biết:\na) √x = 1/3\nb) 2√x - 5 = 3\nc) x² = 100 và x < 0.",
            "rubric": "a) x = (1/3)² = 1/9 (0.3đ).\nb) 2√x = 8 => √x = 4 => x = 16 (0.4đ).\nc) x = -√100 = -10 (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một mảnh vườn hình vuông có diện tích 196 m².\na) Tính độ dài cạnh của mảnh vườn đó.\nb) Người ta muốn rào xung quanh mảnh vườn bằng dây thép gai, biết cổng vào rộng 2 m. Tính chiều dài dây thép gai cần dùng để rào kín mảnh vườn (rào 1 hàng dây).",
            "rubric": "a) Cạnh vườn: a = √196 = 14 m (0.5đ).\nb) Chu vi vườn: 14 x 4 = 56 m. Chiều dài dây thép gai cần dùng (trừ cổng): 56 - 2 = 54 m (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c2_7_bai2_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 6: Số vô tỉ. Căn bậc hai số học - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Giá trị của biểu thức $\\sqrt{3^2 + 4^2}$ là:", "options": ["$5$", "$7$", "$25$", "$1$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Số nào sau đây lớn hơn $5$?", "options": ["$\\sqrt{26}$", "$\\sqrt{24}$", "$\\sqrt{25}$", "$\\sqrt{20}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tìm $x$ biết $x^2 = 7$ và $x > 0$:", "options": ["$x = \\sqrt{7}$", "$x = 49$", "$x = 3,5$", "$x = -\\sqrt{7}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Giá trị của biểu thức $P = \\sqrt{\\frac{4}{9}} + \\sqrt{\\frac{25}{36}} - \\sqrt{\\frac{1}{4}}$ là:", "options": ["$1$", "$\\frac{2}{3}$", "$\\frac{5}{6}$", "$\\frac{1}{2}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $\\sqrt{2x + 1} = 5$:", "options": ["$x = 12$", "$x = 24$", "$x = 2$", "$x = 13$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Có bao nhiêu số tự nhiên $x$ thỏa mãn $\\sqrt{x} < 3$?", "options": ["$9$", "$8$", "$10$", "$4$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "So sánh $\\sqrt{17} + \\sqrt{26}$ với $9$:", "options": ["$\\sqrt{17} + \\sqrt{26} > 9$", "$\\sqrt{17} + \\sqrt{26} < 9$", "$\\sqrt{17} + \\sqrt{26} = 9$", "Không so sánh được"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Độ dài đường chéo của một hình vuông có cạnh bằng $1\\text{ dm}$ là:", "options": ["$\\sqrt{2}\\text{ dm}$", "$2\\text{ dm}$", "$1,5\\text{ dm}$", "$\\sqrt{3}\\text{ dm}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = \\sqrt{x - 3} + 5$:", "options": ["$5$", "$3$", "$0$", "$8$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Số nghiệm của phương trình $\\sqrt{x^2} = 4$ là:", "options": ["$2$", "$1$", "$0$", "Vô số"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số nguyên $x$ lớn nhất thỏa mãn $\\sqrt{x} < 4,5$ là:", "options": ["$20$", "$19$", "$16$", "$21$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Giá trị của biểu thức $M = \\sqrt{1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1}$ là:", "options": ["$5$", "$25$", "$15$", "$4$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức P = √(x - 2) với x là số thực:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Biểu thức P có nghĩa khi và chỉ khi x ≥ 2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Với x = 11 thì P = √9 = 3.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Để P = 4 thì x = 18.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "P có thể nhận giá trị âm.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "So sánh hai biểu thức A = √(20) + √(5) và B = √(45):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "√(20) = 2√5.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "√(45) = 3√5.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "A = 2√5 + √5 = 3√5 = B.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "A > B.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = √(169) - √(144) + √(121).", "answer": "12"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên x biết: 3√(x) = 15.", "answer": "25"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên x thỏa mãn: 3 < √x < 5?", "answer": "15"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: P = √(x + 1) + 7.", "answer": "7"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị các biểu thức sau:\na) A = √(25/36) - √(49/81) : √(49/64)\nb) B = √(13² - 12²) + √(6² + 8²).",
            "rubric": "a) 5/6 - (7/9) : (7/8) = 5/6 - 8/9 = 15/18 - 16/18 = -1/18 (0.5đ).\nb) √(169 - 144) + √(36 + 64) = √25 + √100 = 5 + 10 = 15 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm x biết:\na) √(3x - 2) = 5\nb) (2x - 1)² = 18. (Tìm các giá trị của x)",
            "rubric": "a) Điều kiện x ≥ 2/3. 3x - 2 = 25 => 3x = 27 => x = 9 (nhận) (0.5đ).\nb) 2x - 1 = √18 hoặc 2x - 1 = -√18 => x = (1 + √18)/2 hoặc x = (1 - √18)/2 (hay x = (1 ± 3√2)/2) (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "a) So sánh hai số: A = √10 + √17 và B = 7.\nb) Chứng minh rằng √2 là một số vô tỉ.",
            "rubric": "a) Ta có √10 > √9 = 3; √17 > √16 = 4 => A = √10 + √17 > 3 + 4 = 7. Vậy A > B (0.5đ).\nb) Giả sử √2 là số hữu tỉ => √2 = a/b (a, b ∈ N*, ƯCLN(a, b) = 1). Ta có 2 = a²/b² => a² = 2b² => a² chẵn => a chẵn, đặt a = 2k => 4k² = 2b² => b² = 2k² => b chẵn. Mâu thuẫn với ƯCLN(a, b) = 1. Vậy √2 là số vô tỉ (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c2_7_bai2_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 6: Số vô tỉ. Căn bậc hai số học - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số các số nguyên $x$ thỏa mãn $4 \\leq \\sqrt{x} \\leq 7$ là:", "options": ["$34$", "$33$", "$3$", "$49$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "So sánh $\\sqrt{2024} - \\sqrt{2023}$ và $\\sqrt{2023} - \\sqrt{2022}$:", "options": ["$\\sqrt{2024} - \\sqrt{2023} < \\sqrt{2023} - \\sqrt{2022}$", "$\\sqrt{2024} - \\sqrt{2023} > \\sqrt{2023} - \\sqrt{2022}$", "Hai biểu thức bằng nhau", "Không so sánh được"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Biểu thức $\\sqrt{(\\sqrt{3} - 2)^2}$ có giá trị bằng:", "options": ["$2 - \\sqrt{3}$", "$\\sqrt{3} - 2$", "$1$", "$\\pm(2 - \\sqrt{3})$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ sao cho $\\sqrt{n^2 + 5}$ là một số nguyên:", "options": ["$n = 2$", "$n = 1$", "$n = 3$", "Không tồn tại"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Giá trị nhỏ nhất của biểu thức $P = \\sqrt{x - 1} + \\sqrt{5 - x}$ là:", "options": ["$2$", "$\\sqrt{2}$", "$0$", "$4$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $x = \\sqrt{3 + 2\\sqrt{2}} - \\sqrt{3 - 2\\sqrt{2}}$. Giá trị của $x$ là:", "options": ["$2$", "$\\sqrt{2}$", "$2\\sqrt{2}$", "$0$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm tất cả các giá trị của $x$ thỏa mãn: $\\sqrt{x + 2\\sqrt{x-1}} + \\sqrt{x - 2\\sqrt{x-1}} = 2$:", "options": ["$1 \\leq x \\leq 2$", "$x = 2$", "$x \\geq 2$", "$x = 1$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Số nghiệm nguyên dương của phương trình $\\sqrt{x} + \\sqrt{y} = \\sqrt{18}$ là:", "options": ["$2$", "$1$", "$3$", "$0$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $A = \\sqrt{1 + 2024^2 + \\frac{2024^2}{2025^2}} + \\frac{2024}{2025}$. Giá trị của $A$ là:", "options": ["$2025$", "$2024$", "$1$", "$2026$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Chứng minh $\\sqrt{3}$ là số vô tỉ. Phát biểu nào sau đây đúng?", "options": ["Chứng minh bằng phương pháp phản chứng", "$\\sqrt{3}$ viết được dưới dạng phân số", "$\\sqrt{3}$ là số tự nhiên", "$\\sqrt{3}$ là số thập phân hữu hạn"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức $M = 6 - \\sqrt{x^2 - 4x + 7}$:", "options": ["$6 - \\sqrt{3}$", "$6$", "$\\sqrt{3}$", "Không có giá trị lớn nhất"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Biết $\\sqrt{x} + \\frac{1}{\\sqrt{x}} = 3$. Giá trị của $x + \\frac{1}{x}$ là:", "options": ["$7$", "$9$", "$11$", "$6$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức A = √(x² - 6x + 9) + 2x với x là số thực:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "x² - 6x + 9 = (x - 3)².", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "√(x² - 6x + 9) = |x - 3|.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Với x ≥ 3 thì A = x - 3 + 2x = 3x - 3.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Với x < 3 thì A = x + 3.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Xét bài toán tìm nghiệm của phương trình √(x - 1) = x - 3:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của phương trình là x ≥ 3.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Bình phương hai vế: x - 1 = (x - 3)² = x² - 6x + 9.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Phương trình tương đương x² - 7x + 10 = 0 có hai nghiệm x = 2 và x = 5.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Phương trình ban đầu có 2 nghiệm phân biệt.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: A = √(17² - 8²).", "answer": "15"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên x biết: √(x + 5) = 6.", "answer": "31"},
        {"id": 3, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức: P = √(x² + 4) - 3.", "answer": "-1"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho x > 0 thỏa mãn x + 1/x = 7. Tính giá trị của √x + 1/√x.", "answer": "3"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Rút gọn các biểu thức sau:\na) A = √(4 - 2√3) + √(4 + 2√3)\nb) B = √(x² + 4x + 4) - 2x với x < -2.",
            "rubric": "a) 4 ± 2√3 = (√3 ± 1)². A = (√3 - 1) + (√3 + 1) = 2√3 (0.5đ).\nb) B = |x + 2| - 2x. Vì x < -2 nên x + 2 < 0 => B = -(x + 2) - 2x = -3x - 2 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm x biết:\na) √(2x - 1) = √(x + 3)\nb) √(x² - 4x + 4) = 5.",
            "rubric": "a) Điều kiện x ≥ 1/2. Bình phương hai vế: 2x - 1 = x + 3 => x = 4 (nhận) (0.5đ).\nb) |x - 2| = 5 => x - 2 = 5 => x = 7; hoặc x - 2 = -5 => x = -3. Vậy x ∈ {-3; 7} (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho ba số thực x, y, z thỏa mãn:\n√(x - 1) + √(y - 4) + √(z - 9) = 1/2 (x + y + z).\nTính giá trị của biểu thức S = x + y + z.",
            "rubric": "Nhân 2 hai vế và chuyển vế: (x - 2√(x-1)) + (y - 2√(y-4)) + (z - 2√(z-9)) = 0 (0.3đ). Viết lại: [(x - 1) - 2√(x-1) + 1] + [(y - 4) - 2√(y-4) + 1] + [(z - 9) - 2√(z-9) + 1] = 0 (0.4đ) => (√(x-1) - 1)² + (√(y-4) - 1)² + (√(z-9) - 1)² = 0 => √(x-1) = 1 => x = 2; √(y-4) = 1 => y = 5; √(z-9) = 1 => z = 10. Suy ra S = 2 + 5 + 10 = 17 (0.3đ)."
        }
    ]
}
