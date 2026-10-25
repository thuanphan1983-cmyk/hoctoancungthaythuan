# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 6 - CHƯƠNG III: SỐ NGUYÊN
PHẦN 1: BÀI 13 (TẬP HỢP CÁC SỐ NGUYÊN) & BÀI 14 (PHÉP CỘNG VÀ PHÉP TRỪ SỐ NGUYÊN)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025.
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 13: TẬP HỢP CÁC SỐ NGUYÊN (c3_6_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c3_6_bai1_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 13: Tập hợp các số nguyên - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tập hợp các số nguyên gồm:", "options": ["Các số nguyên âm, số 0 và các số nguyên dương", "Các số nguyên âm và số nguyên dương", "Các số nguyên âm và số 0", "Các số nguyên dương và số 0"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Kí hiệu tập hợp các số nguyên là:", "options": ["$\\mathbb{Z}$", "$\\mathbb{N}$", "$\\mathbb{Q}$", "$\\mathbb{R}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Số đối của số nguyên $-5$ là:", "options": ["$5$", "$-5$", "$\\frac{1}{5}$", "$0$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Số 0 là:", "options": ["Số nguyên không âm và không dương", "Số nguyên dương", "Số nguyên âm", "Không phải là số nguyên"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Trên trục số nằm ngang, điểm biểu diễn số $-3$ nằm ở vị trí nào so với điểm gốc 0?", "options": ["Nằm về bên trái điểm 0 và cách điểm 0 ba đơn vị", "Nằm về bên phải điểm 0 và cách điểm 0 ba đơn vị", "Trùng với điểm 0", "Nằm về bên phải điểm 3"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Trong các số sau, số nào là số nguyên âm?", "options": ["$-7$", "$0$", "$7$", "$12$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "So sánh hai số nguyên $-6$ và $-2$:", "options": ["$-6 < -2$", "$-6 > -2$", "$-6 = -2$", "Không so sánh được"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Nhiệt độ $-3^\\circ\\text{C}$ ấm hơn hay lạnh hơn nhiệt độ $-5^\\circ\\text{C}$?", "options": ["Ấm hơn", "Lạnh hơn", "Bằng nhau", "Không xác định được"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Sắp xếp các số nguyên sau theo thứ tự tăng dần: $3; -5; 0; -2; 4$:", "options": ["$-5; -2; 0; 3; 4$", "$-2; -5; 0; 3; 4$", "$4; 3; 0; -2; -5$", "$0; -2; -5; 3; 4$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Tập hợp các số nguyên $x$ thỏa mãn $-3 < x \\leq 2$ là:", "options": ["$\\{-2; -1; 0; 1; 2\\}$", "$\\{-3; -2; -1; 0; 1; 2\\}$", "$\\{-2; -1; 0; 1\\}$", "$\\{-3; -2; -1; 0; 1\\}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Độ cao của mực nước biển được quy ước là $0\\text{ m}$. Một chiếc tàu ngầm đang lặn ở độ sâu $35\\text{ m}$ dưới mực nước biển thì độ cao của tàu ngầm được biểu diễn bằng số nguyên nào?", "options": ["$-35\\text{ m}$", "$35\\text{ m}$", "$0\\text{ m}$", "$-70\\text{ m}$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Số nguyên liền sau của số nguyên $-1$ là:", "options": ["$0$", "$-2$", "$1$", "$-3$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tập hợp $M = \\{-4; -1; 0; 2; 5\\}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Trong tập hợp $M$ có đúng hai số nguyên âm là $-4$ và $-1$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số nhỏ nhất trong tập hợp $M$ là số $-4$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số đối của các phần tử trong $M$ lần lượt là $4; 1; 0; -2; -5$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Số 0 là số nguyên dương nhỏ nhất trong tập hợp $M$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Nhiệt độ đo được lúc 6 giờ sáng tại 4 địa điểm lần lượt là: Sapa ($-2^\\circ\\text{C}$), Mẫu Sơn ($-4^\\circ\\text{C}$), Hà Nội ($15^\\circ\\text{C}$), Đà Lạt ($10^\\circ\\text{C}$).",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Mẫu Sơn là nơi có nhiệt độ thấp nhất trong 4 địa điểm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hà Nội là nơi có nhiệt độ cao nhất trong 4 địa điểm.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nhiệt độ ở Sapa ấm hơn nhiệt độ ở Mẫu Sơn $2^\\circ\\text{C}$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Sắp xếp nhiệt độ từ thấp đến cao: $-2^\\circ\\text{C}; -4^\\circ\\text{C}; 10^\\circ\\text{C}; 15^\\circ\\text{C}$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Số nguyên âm lớn nhất có hai chữ số là bao nhiêu?", "answer": "-10"},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $-4 \\leq x < 3$?", "answer": "7"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính tổng của số nguyên âm nhỏ nhất có một chữ số và số nguyên dương lớn nhất có một chữ số.", "answer": "0"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Trên trục số, khoảng cách giữa điểm biểu diễn số $-7$ và điểm biểu diễn số $3$ bằng bao nhiêu đơn vị?", "answer": "10"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Viết số đối của mỗi số nguyên sau: $-8; 0; 12; -2025$.\nb) Biểu diễn các số nguyên sau trên trục số: $-3; -1; 0; 2; 4$.",
            "rubric": "a) Số đối của -8 là 8; số đối của 0 là 0; số đối của 12 là -12; số đối của -2025 là 2025 (0.5đ).\nb) Vẽ đúng trục số nằm ngang có gốc 0, chiều dương từ trái sang phải, chia đều các vạch đơn vị và biểu diễn chính xác 5 điểm (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "a) Sắp xếp các số nguyên sau theo thứ tự giảm dần: $-15; 0; 8; -3; 12; -9$.\nb) Liệt kê các phần tử của tập hợp $A = \\{x \\in \\mathbb{Z} \\mid -5 \\leq x < 4\\}$.",
            "rubric": "a) Thứ tự giảm dần (từ lớn đến bé): 12; 8; 0; -3; -9; -15 (0.5đ).\nb) Tập hợp A = {-5; -4; -3; -2; -1; 0; 1; 2; 3} (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Bảng dưới đây ghi độ cao so với mực nước biển của một số đỉnh núi và rãnh đại dương:\n- Đỉnh Fansipan: $+3143\\text{ m}$\n- Rãnh Mariana: $-10994\\text{ m}$\n- Đỉnh Everest: $+8848\\text{ m}$\n- Biển Chết: $-430\\text{ m}$\na) Nơi nào cao nhất và nơi nào sâu nhất?\nb) Sắp xếp các độ cao trên theo thứ tự từ thấp đến cao.",
            "rubric": "a) Nơi cao nhất là Đỉnh Everest (+8848 m) (0.25đ). Nơi sâu nhất là Rãnh Mariana (-10994 m) (0.25đ).\nb) Sắp xếp từ thấp đến cao: -10994 m; -430 m; +3143 m; +8848 m (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c3_6_bai1_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 13: Tập hợp các số nguyên - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho số nguyên $a < 0$. Khẳng định nào sau đây là SAI?", "options": ["$-a < 0$", "$-a > 0$", "$a$ nằm bên trái điểm 0 trên trục số", "Số đối của $a$ là số nguyên dương"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $-10 \\leq x \\leq 10$?", "options": ["$21$", "$20$", "$19$", "$22$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $a, b \\in \\mathbb{Z}$ sao cho $a$ nằm bên trái điểm $b$ trên trục số. Khi đó:", "options": ["$a < b$", "$a > b$", "$a = b$", "$a \\geq b$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Khẳng định nào sau đây là ĐÚNG với mọi số nguyên $x$?", "options": ["Nếu $x > 0$ thì số đối của $x$ nhỏ hơn 0", "Nếu $x \\in \\mathbb{Z}$ thì $-x$ luôn là số nguyên âm", "Khoảng cách từ $x$ đến gốc 0 có thể là số âm", "$-(-x) = -x$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Số nguyên liền trước của số nguyên âm lớn nhất là:", "options": ["$-2$", "$0$", "$-1$", "$1$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ biết số đối của $x$ là $-(-7)$:", "options": ["$-7$", "$7$", "$0$", "$14$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho ba số nguyên $a, b, c$ thỏa mãn $a < b < 0 < c$. Sắp xếp các số $a, b, c$ và các số đối của chúng theo thứ tự tăng dần:", "options": ["$-c < a < b < -b < -a < c$", "$a < b < -c < -b < -a < c$", "$-c < -a < -b < a < b < c$", "$a < b < c < -c < -b < -a$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $-5 < x \\leq 5$?", "options": ["$10$", "$11$", "$9$", "$8$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cho tập hợp $A = \\{x \\in \\mathbb{Z} \\mid -2024 \\leq x \\leq 2024\\}$. Tổng của tất cả các phần tử của $A$ bằng:", "options": ["$0$", "$2024$", "$-2024$", "$4048$"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Một tàu ngầm đang ở độ sâu $40\\text{ m}$. Tàu lặn thêm $15\\text{ m}$ nữa rồi nổi lên $20\\text{ m}$. Vị trí mới của tàu ngầm biểu diễn bằng số nguyên nào?", "options": ["$-35\\text{ m}$", "$-75\\text{ m}$", "$-45\\text{ m}$", "$35\\text{ m}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Biết $x$ là số nguyên âm và $-8 < x < -4$. Tích các giá trị của $x$ thỏa mãn bằng:", "options": ["$-210$", "$210$", "$-35$", "$35$"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Điểm $A$ cách gốc 0 năm đơn vị về bên trái. Điểm $B$ cách điểm $A$ tám đơn vị về bên phải. Tọa độ của điểm $B$ là:", "options": ["$3$", "$-13$", "$-3$", "$13$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tập hợp $X = \\{x \\in \\mathbb{Z} \\mid -6 < x \\leq 4\\}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số phần tử nguyên âm trong tập hợp $X$ là 5 phần tử ($\\{-5; -4; -3; -2; -1\\}$).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số phần tử nguyên dương trong tập hợp $X$ là 4 phần tử ($\\{1; 2; 3; 4\\}$).", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tập hợp $X$ có tổng cộng 10 phần tử kể cả số 0.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tổng của tất cả các phần tử thuộc tập hợp $X$ bằng $-5$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Một nhà lạnh có nhiệt độ ban đầu là $6^\\circ\\text{C}$. Người quản lí giảm nhiệt độ $2^\\circ\\text{C}$ mỗi giờ liên tục trong 5 giờ.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Sau 3 giờ đầu tiên, nhiệt độ của nhà lạnh hạ xuống còn $0^\\circ\\text{C}$.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Sau 5 giờ, nhiệt độ trong nhà lạnh giảm tổng cộng $10^\\circ\\text{C}$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nhiệt độ cuối cùng trong nhà lạnh là $-4^\\circ\\text{C}$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nhiệt độ $-4^\\circ\\text{C}$ ấm hơn nhiệt độ $-2^\\circ\\text{C}$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính tổng của tất cả các số nguyên $x$ thỏa mãn $-8 < x < 9$.", "answer": "8"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $-15 \\leq x < 20$?", "answer": "35"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số đối của số nguyên $a$ biết rằng $-a = -(-12)$.", "answer": "-12"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ nhỏ nhất sao cho $x > -25$ và $x$ chia hết cho 5.", "answer": "-20"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho các số nguyên sau: $-12; 7; -3; 0; -18; 15; -1$.\na) Tìm số đối của từng số nguyên trên.\nb) Sắp xếp các số nguyên đã cho theo thứ tự tăng dần.\nc) Viết tập hợp các số nguyên $x$ thỏa mãn: $-12 \\leq x < -3$.",
            "rubric": "a) Số đối lần lượt là: 12; -7; 3; 0; 18; -15; 1 (0.35đ).\nb) Thứ tự tăng dần: -18 < -12 < -3 < -1 < 0 < 7 < 15 (0.35đ).\nc) Tập hợp: {-12; -11; -10; -9; -8; -7; -6; -5; -4} (0.3đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho trục số nằm ngang. Điểm $A$ biểu diễn số $-4$, điểm $B$ biểu diễn số $6$.\na) Tính khoảng cách từ điểm $A$ đến điểm $B$ trên trục số.\nb) Tìm tọa độ trung điểm $M$ của đoạn thẳng $AB$.",
            "rubric": "a) Khoảng cách AB = 6 - (-4) = 6 + 4 = 10 đơn vị (0.5đ).\nb) Trung điểm M nằm cách A và B một khoảng bằng 10 : 2 = 5 đơn vị (0.25đ). Tọa độ của điểm M là: -4 + 5 = 1 (hoặc 6 - 5 = 1) (0.25đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Bác Bình kinh doanh một cửa hàng hoa tươi. Trong 5 ngày liên tiếp, tình hình lợi nhuận (đơn vị: triệu đồng) được ghi lại như sau:\n- Ngày 1: $+2$\n- Ngày 2: $-1$\n- Ngày 3: $+3$\n- Ngày 4: $-2$\n- Ngày 5: $+4$\na) Giải thích ý nghĩa của các số nguyên âm trong bảng số liệu trên.\nb) Tính tổng lợi nhuận của bác Bình sau cả 5 ngày kinh doanh.",
            "rubric": "a) Số nguyên âm biểu thị ngày kinh doanh bị lỗ: Ngày 2 cửa hàng bị lỗ 1 triệu đồng; Ngày 4 cửa hàng bị lỗ 2 triệu đồng (0.5đ).\nb) Tổng lợi nhuận sau 5 ngày là: (+2) + (-1) + (+3) + (-2) + (+4) = (2 + 3 + 4) - (1 + 2) = 9 - 3 = +6 (triệu đồng) (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c3_6_bai1_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 13: Tập hợp các số nguyên - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $a, b \\in \\mathbb{Z}$. Nếu $a > b$ thì khẳng định nào sau đây luôn đúng?", "options": ["$-a < -b$", "$-a > -b$", "$-a = -b$", "$|a| > |b|$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm tất cả các số nguyên $x$ thỏa mãn $-2 \\leq -x < 3$:", "options": ["$-2; -1; 0; 1; 2$", "$-3; -2; -1; 0; 1$", "$-2; -1; 0$", "$1; 2$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho $A = \\{x \\in \\mathbb{Z} \\mid |x| \\leq 5\\}$. Số phần tử của tập hợp $A$ là:", "options": ["$11$", "$10$", "$5$", "$6$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Có bao nhiêu cặp số nguyên $(x; y)$ thỏa mãn $|x| + |y| = 1$?", "options": ["$4$ cặp", "$2$ cặp", "$8$ cặp", "$6$ cặp"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Cho 5 số nguyên $a_1, a_2, a_3, a_4, a_5$ đều khác 0 thỏa mãn tích của 2 số bất kì trong chúng là số dương. Khẳng định nào đúng?", "options": ["Cả 5 số đều cùng dấu", "Có 3 số âm và 2 số dương", "Có 4 số âm và 1 số dương", "Chỉ có 1 số âm"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $x$ là số nguyên. Giá trị nhỏ nhất của biểu thức $P = |x - 3| + 5$ là:", "options": ["$5$", "$3$", "$0$", "$8$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm số nguyên $x$ sao cho khoảng cách từ điểm $x$ đến điểm $-3$ trên trục số bằng 7:", "options": ["$x = 4$ hoặc $x = -10$", "$x = 4$", "$x = -10$", "$x = 10$ hoặc $x = -4$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $a$ là số nguyên âm lớn nhất có 3 chữ số khác nhau, $b$ là số nguyên dương nhỏ nhất có 3 chữ số khác nhau. Hiệu $b - a$ bằng:", "options": ["$204$", "$2024$", "$0$", "$200$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Có bao nhiêu số nguyên $x$ thỏa mãn $|x - 2| < 4$?", "options": ["$7$", "$8$", "$9$", "$6$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $S = \\{x \\in \\mathbb{Z} \\mid -100 \\leq x \\leq 102\\}$. Tổng của các số nguyên trong tập hợp $S$ bằng:", "options": ["$203$", "$101$", "$102$", "$0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Trên trục số, điểm $M$ biểu diễn số $-15$, điểm $N$ biểu diễn số $25$. Điểm $P$ nằm giữa $M$ và $N$ sao cho $MP = 3PN$. Tọa độ của điểm $P$ là:", "options": ["$15$", "$5$", "$10$", "$0$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = |x - 1| + |x - 5|$ với $x \\in \\mathbb{Z}$:", "options": ["$4$", "$0$", "$2$", "$6$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai số nguyên $a$ và $b$ thỏa mãn $a < 0 < b$ và $|a| > |b|$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Trên trục số, điểm $a$ nằm về bên trái điểm 0, điểm $b$ nằm về bên phải điểm 0.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Khoảng cách từ điểm $a$ đến gốc 0 lớn hơn khoảng cách từ điểm $b$ đến gốc 0.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Tổng $a + b$ là một số nguyên âm.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Số đối của $a$ nhỏ hơn số đối của $b$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét biểu thức $E = |x + 2| + |x - 4|$ với $x$ là số nguyên.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Khoảng cách giữa hai điểm biểu diễn số $-2$ và số $4$ trên trục số là 6 đơn vị.", "correct": True},
                {"key": "b", "level": "Vận dụng cao", "text": "Với mọi số nguyên $x$, ta luôn có $|x + 2| + |x - 4| = |x + 2| + |4 - x| \\geq |x + 2 + 4 - x| = 6$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Giá trị nhỏ nhất của biểu thức $E$ bằng 6.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Biểu thức $E$ đạt giá trị nhỏ nhất khi và chỉ khi $x = 0$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tìm số các số nguyên $x$ thỏa mãn $|x| < 20$.", "answer": "39"},
        {"id": 2, "level": "Vận dụng cao", "question": "Tìm giá trị nhỏ nhất của biểu thức $B = |x + 5| - 12$.", "answer": "-12"},
        {"id": 3, "level": "Vận dụng cao", "question": "Có bao nhiêu cặp số nguyên $(x, y)$ thỏa mãn $|x| + |y| \\leq 2$?", "answer": "13"},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm số nguyên $x$ thỏa mãn $|x - 1| + |x - 3| = 2$. Có bao nhiêu giá trị nguyên của $x$?", "answer": "3"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho tập hợp $A = \\{x \\in \\mathbb{Z} \\mid -2024 < x \\leq 2025\\}$.\na) Tập hợp $A$ có bao nhiêu phần tử?\nb) Tính tổng của tất cả các phần tử thuộc tập hợp $A$.",
            "rubric": "a) Các phần tử của A từ -2023 đến 2025 (0.25đ). Số phần tử là: 2025 - (-2023) + 1 = 2025 + 2023 + 1 = 4049 phần tử (0.25đ).\nb) Tổng S = (-2023) + (-2022) + ... + 2023 + 2024 + 2025 (0.2đ). Các cặp số đối nhau từ -2023 đến 2023 có tổng bằng 0 (0.15đ). Vậy S = 2024 + 2025 = 4049 (0.15đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm tất cả các số nguyên $x$ thỏa mãn:\na) $|x - 2| = 5$.\nb) $|x + 1| \\leq 3$.",
            "rubric": "a) x - 2 = 5 => x = 7; hoặc x - 2 = -5 => x = -3. Vậy x ∈ {7; -3} (0.5đ).\nb) |x + 1| ≤ 3 <=> -3 ≤ x + 1 ≤ 3 <=> -4 ≤ x ≤ 2 (0.3đ). Vì x ∈ Z nên x ∈ {-4; -3; -2; -1; 0; 1; 2} (0.2đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho 2025 số nguyên trong đó tích của 3 số bất kì luôn là một số âm. Chứng minh rằng:\na) Cả 2025 số nguyên đó đều là số âm.\nb) Tích của cả 2025 số nguyên đó là một số âm.",
            "rubric": "a) Giả sử trong 2025 số có ít nhất 1 số không âm hoặc bằng 0:\n- Nếu có số 0 thì tích 3 số chứa số 0 sẽ bằng 0 (mâu thuẫn vì tích luôn âm) (0.2đ).\n- Nếu có số dương a > 0, lấy 2 số bất kì b, c thì tích a * b * c < 0 => b * c < 0 (luôn có 1 âm 1 dương). Mâu thuẫn nếu chọn cặp số cùng dương (0.3đ).\nVậy tất cả 2025 số đều phải là số âm (0.25đ).\nb) Tích của 2025 số âm (số lẻ các số âm) luôn là một số âm (0.25đ)."
        }
    ]
}

# ==============================================================================
# BÀI 14: PHÉP CỘNG VÀ PHÉP TRỪ SỐ NGUYÊN (c3_6_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c3_6_bai2_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 14: Phép cộng và phép trừ số nguyên - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tổng của hai số nguyên âm luôn là:", "options": ["Một số nguyên âm", "Một số nguyên dương", "Số 0", "Không xác định được dấu"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Kết quả của phép tính $(-3) + (-5)$ là:", "options": ["$-8$", "$8$", "$-2$", "$2$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Tổng của hai số nguyên đối nhau luôn bằng:", "options": ["$0$", "$1$", "$-1$", "Hai lần số đó"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Muốn trừ số nguyên $a$ cho số nguyên $b$, ta làm như sau:", "options": ["Cộng $a$ với số đối của $b$", "Lấy $b$ trừ đi $a$", "Cộng $a$ với $b$", "Lấy số đối của $a$ trừ đi $b$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Kết quả của phép tính $5 - 9$ là:", "options": ["$-4$", "$4$", "$-14$", "$14$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Tính chất nào sau đây là tính chất của phép cộng các số nguyên?", "options": ["Cả giao hoán, kết hợp và cộng với số 0", "Chỉ có tính chất giao hoán", "Chỉ có tính chất kết hợp", "Không có tính chất kết hợp"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Kết quả của phép tính $(-12) + 7$ là:", "options": ["$-5$", "$5$", "$-19$", "$19$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Kết quả của phép tính $15 + (-8)$ là:", "options": ["$7$", "$-7$", "$23$", "$-23$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Kết quả của phép tính $(-6) - (-4)$ là:", "options": ["$-2$", "$-10$", "$2$", "$10$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Nhiệt độ lúc 12 giờ trưa là $5^\\circ\\text{C}$, đến 20 giờ cùng ngày nhiệt độ giảm $8^\\circ\\text{C}$. Nhiệt độ lúc 20 giờ là:", "options": ["$-3^\\circ\\text{C}$", "$3^\\circ\\text{C}$", "$-13^\\circ\\text{C}$", "$13^\\circ\\text{C}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tìm số nguyên $x$ biết $x - 5 = -8$:", "options": ["$x = -3$", "$x = 3$", "$x = -13$", "$x = 13$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Tính tổng $S = (-20) + 15 + 20$:", "options": ["$15$", "$55$", "$-15$", "$0$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho các phép tính: $A = (-15) + (-25)$, $B = (-40) + 60$, $C = 20 - 35$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Giá trị của biểu thức $A$ là $-40$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Giá trị của biểu thức $B$ là $20$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Giá trị của biểu thức $C$ là $-15$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tổng $A + B + C$ bằng $-5$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Một tàu ngầm đang ở độ sâu $30\\text{ m}$ dưới mực nước biển (biểu diễn là $-30\\text{ m}$). Sau đó tàu nổi lên $12\\text{ m}$, rồi lại lặn sâu thêm $15\\text{ m}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Khi nổi lên 12m, độ cao mới của tàu là $(-30) + 12 = -18\\text{ m}$.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Khi lặn sâu thêm 15m, độ cao cuối cùng của tàu là $(-18) - 15 = -33\\text{ m}$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Sau hai lần di chuyển, vị trí của tàu sâu hơn vị trí ban đầu 3m.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Độ sâu cuối cùng của tàu là $45\\text{ m}$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính: $(-135) + (-65)$.", "answer": "-200"},
        {"id": 2, "level": "Thông hiểu", "question": "Tính: $250 - 320$.", "answer": "-70"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ thỏa mãn: $x + 15 = -5$.", "answer": "-20"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tính tổng các số nguyên $x$ thỏa mãn $-4 \\leq x \\leq 5$.", "answer": "5"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính:\na) $(-28) + (-42)$.\nb) $(-35) + 15$.\nc) $18 - (-12)$.\nd) $(-25) - 15$.",
            "rubric": "a) -(28 + 42) = -70 (0.25đ).\nb) -(35 - 15) = -20 (0.25đ).\nc) 18 + 12 = 30 (0.25đ).\nd) (-25) + (-15) = -40 (0.25đ)."
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tính một cách hợp lí:\na) $A = (-125) + 48 + 125$.\nb) $B = 37 + (-15) + (-37) + 65$.",
            "rubric": "a) A = [(-125) + 125] + 48 = 0 + 48 = 48 (0.5đ).\nb) B = [37 + (-37)] + [(-15) + 65] = 0 + 50 = 50 (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tài khoản ngân hàng của cô Lan có số dư ban đầu là $5\\,000\\,000$ đồng. Trong tuần, cô thực hiện các giao dịch:\n- Ngày thứ Hai: Nộp thêm $2\\,000\\,000$ đồng.\n- Ngày thứ Tư: Rút ra $3\\,500\\,000$ đồng để chi tiêu.\n- Ngày thứ Sáu: Thanh toán hóa đơn tiền điện $800\\,000$ đồng.\nHỏi số dư trong tài khoản của cô Lan vào cuối tuần là bao nhiêu đồng?",
            "rubric": "Số tiền sau ngày thứ Hai: 5 000 000 + 2 000 000 = 7 000 000 đồng (0.3đ).\nSố tiền sau ngày thứ Tư: 7 000 000 - 3 500 000 = 3 500 000 đồng (0.3đ).\nSố dư cuối tuần: 3 500 000 - 800 000 = 2 700 000 đồng (0.4đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c3_6_bai2_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 14: Phép cộng và phép trừ số nguyên - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $P = (-120) + 45 - (-120) + (-55)$:", "options": ["$-10$", "$10$", "$-250$", "$0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm $x$ biết $15 - (x + 2) = -3$:", "options": ["$x = 16$", "$x = 10$", "$x = -16$", "$x = 14$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $a = -15, b = -8$. Giá trị của $a - b$ là:", "options": ["$-7$", "$7$", "$-23$", "$23$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Tổng của số nguyên âm nhỏ nhất có hai chữ số và số nguyên dương lớn nhất có hai chữ số là:", "options": ["$0$", "$-1$", "$1$", "$-198$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $x \\in \\mathbb{Z}$ thỏa mãn $-7 < x < 5$. Tổng tất cả các giá trị của $x$ là:", "options": ["$-11$", "$-6$", "$-18$", "$0$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Tính tổng $S = 1 - 2 + 3 - 4 + 5 - 6 + \\dots + 99 - 100$:", "options": ["$-50$", "$50$", "$-100$", "$0$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Tìm $x$ thỏa mãn $|x| - 5 = -2$:", "options": ["$x = 3$ hoặc $x = -3$", "$x = 3$", "$x = -3$", "$x = 7$ hoặc $x = -7$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Một người bán hàng bị lỗ $300\\,000$ đồng trong đợt 1, đợt 2 lãi $500\\,000$ đồng, đợt 3 bị lỗ $150\\,000$ đồng. Tổng kết cả 3 đợt người đó:", "options": ["Lãi $50\\,000$ đồng", "Lỗ $50\\,000$ đồng", "Lãi $650\\,000$ đồng", "Hòa vốn"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cho $a, b \\in \\mathbb{Z}$. Nếu $a - b = 5$ thì $b - a$ bằng:", "options": ["$-5$", "$5$", "$0$", "Không xác định"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Tính tổng $A = (-1) + 2 + (-3) + 4 + \\dots + (-19) + 20$:", "options": ["$10$", "$-10$", "$20$", "$-20$"], "correct": 0},
        {"id": 11, "level": "Vận dụng thấp", "question": "Tìm $x$ nguyên biết $(x - 3) + (-12) = -8$:", "options": ["$x = 7$", "$x = -17$", "$x = 1$", "$x = -1$"], "correct": 0},
        {"id": 12, "level": "Vận dụng thấp", "question": "Nhiệt độ phòng đông lạnh lúc đầu là $-6^\\circ\\text{C}$. Nếu tăng thêm $4^\\circ\\text{C}$ rồi sau đó lại giảm đi $7^\\circ\\text{C}$ thì nhiệt độ mới là:", "options": ["$-9^\\circ\\text{C}$", "$-5^\\circ\\text{C}$", "$-17^\\circ\\text{C}$", "$5^\\circ\\text{C}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho biểu thức $A = 125 + (-48) - 125 + 48 - (-20)$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Áp dụng tính chất giao hoán và kết hợp: $[125 + (-125)] + [(-48) + 48] = 0 + 0 = 0$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Phép trừ số nguyên âm: $- (-20) = + 20$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Giá trị của biểu thức $A$ là 20.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Biểu thức $A$ nhận giá trị âm.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho dãy số: $S = 2 - 4 + 6 - 8 + 10 - 12 + \\dots + 98 - 100$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Dãy số có tất cả $(100 - 2) : 2 + 1 = 50$ số hạng.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ghép thành 25 cặp, mỗi cặp có giá trị bằng $-2$.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Giá trị của tổng $S$ là $25 \\cdot (-2) = -50$.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Nếu cộng thêm số 102 vào cuối dãy thì giá trị mới là $52$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức: $M = (-250) + 180 + (-50) + 120$.", "answer": "0"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Tìm $x$ biết: $x - (-18) = 10 + (-15)$.", "answer": "-23"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tính tổng: $S = 1 - 3 + 5 - 7 + 9 - 11 + 13 - 15$.", "answer": "-8"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ sao cho $x + (-12) = -(-25)$.", "answer": "37"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính hợp lí giá trị các biểu thức sau:\na) $A = (-312) + 198 + (-188) + 302$.\nb) $B = 45 - (-15) + (-20) - 40$.",
            "rubric": "a) A = [(-312) + (-188)] + (198 + 302) = -500 + 500 = 0 (0.5đ).\nb) B = 45 + 15 + (-20) - 40 = 60 - 60 = 0 (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Tìm số nguyên $x$ biết:\na) $x + 12 = -8$.\nb) $25 - (x - 3) = -10$.\nc) $|x - 1| = 4$.",
            "rubric": "a) x = -8 - 12 = -20 (0.3đ).\nb) x - 3 = 25 - (-10) = 35 => x = 35 + 3 = 38 (0.35đ).\nc) x - 1 = 4 => x = 5 hoặc x - 1 = -4 => x = -3. Vậy x ∈ {5; -3} (0.35đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Tính tổng của tất cả các số nguyên $x$ thỏa mãn:\na) $-10 < x \\leq 10$.\nb) $-15 \\leq x < 12$.",
            "rubric": "a) x ∈ {-9; -8; ...; 8; 9; 10}. Tổng S = [(-9) + 9] + ... + [(-1) + 1] + 0 + 10 = 10 (0.5đ).\nb) x ∈ {-15; -14; ...; 10; 11}. Các số từ -11 đến 11 có tổng bằng 0. Còn lại: (-15) + (-14) + (-13) + (-12) = -54 (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c3_6_bai2_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 14: Phép cộng và phép trừ số nguyên - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $a, b \\in \\mathbb{Z}$. Nếu $a + b < a$ thì:", "options": ["$b < 0$", "$b > 0$", "$b = 0$", "$a < 0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $a, b \\in \\mathbb{Z}$. Nếu $a - b > a$ thì:", "options": ["$b < 0$", "$b > 0$", "$b = 0$", "$a > 0$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm giá trị nhỏ nhất của biểu thức $A = |x + 2| + 10$:", "options": ["$10$", "$2$", "$0$", "$12$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Tính tổng $S = 1 - 4 + 7 - 10 + 13 - 16 + \\dots + 97 - 100$:", "options": ["$-51$", "$-50$", "$51$", "$-48$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Tìm số nguyên $x$ thỏa mãn $|x + 3| + |y - 2| = 0$:", "options": ["$x = -3, y = 2$", "$x = 3, y = -2$", "$x = 0, y = 0$", "Vô số cặp"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $a, b, c \\in \\mathbb{Z}$ thỏa mãn $a + b = 5, b + c = 12, c + a = 7$. Giá trị của $a + b + c$ bằng:", "options": ["$12$", "$24$", "$6$", "$14$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Tìm giá trị lớn nhất của biểu thức $M = 20 - |x - 4|$:", "options": ["$20$", "$16$", "$24$", "$4$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Có bao nhiêu cặp số nguyên $(x, y)$ thỏa mãn $|x| + |y| = 3$?", "options": ["$12$", "$8$", "$16$", "$6$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho dãy số: $x_1, x_2, \\dots, x_{2025}$ sao cho tổng của 3 số bất kì liên tiếp luôn bằng $4$. Biết $x_1 = 5, x_2 = -3$. Giá trị của $x_{2025}$ là:", "options": ["$2$", "$5$", "$-3$", "$4$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $a$ và $b$ là hai số nguyên khác 0 thỏa mãn $a + b = 0$. Giá trị của biểu thức $\\frac{a}{|b|} + \\frac{b}{|a|}$ bằng:", "options": ["$-2$", "$0$", "$2$", "$1$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Tính tổng $S = 100 - 99 + 98 - 97 + \\dots + 2 - 1$:", "options": ["$50$", "$100$", "$-50$", "$25$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $x, y \\in \\mathbb{Z}$ thỏa mãn $|x - y| = 1$. Giá trị của biểu thức $(x - y)^2$ bằng:", "options": ["$1$", "$-1$", "$0$", "$2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho ba số nguyên $a, b, c$ thỏa mãn $a - b = 7$ và $b - c = -11$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Cộng hai vế ta được: $(a - b) + (b - c) = a - c$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Giá trị của $a - c = 7 + (-11) = -4$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Do $a - c = -4$ nên $a < c$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Thứ tự tăng dần của ba số là $a < b < c$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét biểu thức $S = |x - 2| + |x + 5|$ với $x \\in \\mathbb{Z}$.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Khoảng cách giữa hai điểm $-5$ và $2$ trên trục số bằng $2 - (-5) = 7$.", "correct": True},
                {"key": "b", "level": "Vận dụng cao", "text": "Áp dụng bất đẳng thức trị tuyệt đối: $|x - 2| + |x + 5| = |2 - x| + |x + 5| \\geq |2 - x + x + 5| = 7$.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Giá trị nhỏ nhất của $S$ bằng $7$.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Giá trị nhỏ nhất đạt được với mọi số nguyên $x$ thỏa mãn $-5 \\leq x \\leq 2$ (có 8 giá trị nguyên).", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng thấp", "question": "Tính tổng $S = 1 - 2 - 3 + 4 + 5 - 6 - 7 + 8 + \\dots + 97 - 98 - 99 + 100$.", "answer": "0"},
        {"id": 2, "level": "Vận dụng cao", "question": "Tìm số nguyên $x$ sao cho biểu thức $P = 15 - |x + 4|$ đạt giá trị lớn nhất.", "answer": "-4"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $a + b = -2$ và $b + c = 5$ và $c + a = 1$. Tính giá trị của $a + b + c$.", "answer": "2"},
        {"id": 4, "level": "Vận dụng cao", "question": "Có bao nhiêu cặp số nguyên $(x, y)$ thỏa mãn $|x| + |y| = 2$?", "answer": "8"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Tính tổng một cách hợp lí:\n$S = 1 + (-2) + 3 + (-4) + 5 + (-6) + \\dots + 2023 + (-2024) + 2025$.",
            "rubric": "Dãy có 2025 số hạng. Ta nhóm các cặp số từ đầu:\nS = [1 + (-2)] + [3 + (-4)] + ... + [2023 + (-2024)] + 2025 (0.35đ).\nTừ 1 đến 2024 có 2024 : 2 = 1012 cặp, mỗi cặp có giá trị bằng -1 (0.35đ).\nS = 1012 * (-1) + 2025 = -1012 + 2025 = 1013 (0.3đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Tìm các số nguyên $x, y$ thỏa mãn:\na) $|x - 3| + |y + 1| = 0$.\nb) $|x| + |y| = 1$.",
            "rubric": "a) Vì |x - 3| ≥ 0 và |y + 1| ≥ 0 với mọi x, y nên để tổng bằng 0 thì:\n|x - 3| = 0 => x = 3; và |y + 1| = 0 => y = -1. Vậy (x; y) = (3; -1) (0.5đ).\nb) Vì |x|, |y| ≥ 0 và x, y ∈ Z nên:\nTH1: |x| = 0, |y| = 1 => x = 0, y = ±1 (0.25đ).\nTH2: |x| = 1, |y| = 0 => x = ±1, y = 0 (0.25đ).\nVậy có 4 cặp (x; y): (0; 1), (0; -1), (1; 0), (-1; 0)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho $x_1 + x_2 + x_3 + \\dots + x_{50} + x_{51} = 0$.\nBiết rằng $x_1 + x_2 = x_3 + x_4 = \\dots = x_{49} + x_{50} = 1$.\nTính giá trị của số nguyên $x_{51}$.",
            "rubric": "Từ x_1 đến x_50 có 50 số, chia thành 25 cặp liên tiếp dạng (x_{2k-1} + x_{2k}) (0.35đ).\nTổng của 50 số đầu là: (x_1 + x_2) + (x_3 + x_4) + ... + (x_{49} + x_{50}) = 25 * 1 = 25 (0.35đ).\nTheo đề bài: (x_1 + x_2 + ... + x_{50}) + x_{51} = 0 => 25 + x_{51} = 0 => x_{51} = -25 (0.3đ)."
        }
    ]
}
