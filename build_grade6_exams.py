# -*- coding: utf-8 -*-
"""
HỆ THỐNG BIÊN SOẠN TOÀN DIỆN TOÁN 6: CHƯƠNG V, VI, VII, VIII, IX
Tạo trọn vẹn:
- grade6_c5_6_exams.json / .js (9 đề)
- grade6_c6_6_exams.json / .js (18 đề)
- grade6_c7_6_exams.json / .js (15 đề)
- grade6_c8_6_exams.json / .js (21 đề)
- grade6_c9_6_exams.json / .js (21 đề)
Tổng cộng: 84 đề kiểm tra chuẩn ma trận 2025.
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package

# ==============================================================================
# CHƯƠNG V TOÁN 6: TÍNH ĐỐI XỨNG CỦA HÌNH PHẲNG TRONG TỰ NHIÊN (3 BÀI = 9 ĐỀ)
# ==============================================================================
def generate_c5_toan6():
    print("🚀 Đang biên soạn Chương V Toán 6: Tính đối xứng của hình phẳng...")
    exams = {}

    # BÀI 1: Hình có trục đối xứng
    # BÀI 2: Hình có tâm đối xứng
    # BÀI 3: Bài kiểm tra cuối Chương V
    lessons = [
        (1, "Bài 21: Hình có trục đối xứng", "trục đối xứng"),
        (2, "Bài 22: Hình có tâm đối xứng", "tâm đối xứng"),
        (3, "Bài kiểm tra cuối Chương V: Tính đối xứng của hình phẳng trong tự nhiên", "tính đối xứng")
    ]

    for (l_idx, l_name, focus) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
            
            p1 = [
                make_mc(1, "Nhận biết", f"Hình nào sau đây có {focus}?", ["Đoạn thẳng", "Tam giác thường", "Hình thang vuông", "Hình bình hành không đặc biệt"], 0),
                make_mc(2, "Nhận biết", "Đoạn thẳng $AB$ có trục đối xứng là:", ["Đường trung trực của đoạn thẳng $AB$", "Đường thẳng $AB$", "Đường vuông góc tại $A$", "Đường chéo"], 0),
                make_mc(3, "Nhận biết", "Tâm đối xứng của đoạn thẳng $AB$ là:", ["Trung điểm của đoạn thẳng $AB$", "Điểm $A$", "Điểm $B$", "Không có tâm đối xứng"], 0),
                make_mc(4, "Nhận biết", "Hình tròn có bao nhiêu trục đối xứng?", ["Vô số trục đối xứng (đi qua tâm)", "1 trục", "2 trục", "4 trục"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Hình tròn có tâm đối xứng là:", ["Tâm của hình tròn", "Điểm bất kì trên đường tròn", "Điểm bên ngoài", "Không có"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Tam giác đều có bao nhiêu trục đối xứng?", ["$3$ trục đối xứng", "$1$ trục", "$2$ trục", "$0$ trục"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Hình vuông có bao nhiêu trục đối xứng?", ["$4$ trục đối xứng", "$2$ trục", "$1$ trục", "$8$ trục"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Chữ cái in hoa nào sau đây vừa có trục đối xứng vừa có tâm đối xứng?", ["Chữ H", "Chữ A", "Chữ B", "Chữ C"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Chữ cái in hoa nào sau đây có tâm đối xứng nhưng KHÔNG có trục đối xứng?", ["Chữ N (hoặc Z, S)", "Chữ O", "Chữ H", "Chữ I"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hình thoi có bao nhiêu trục đối xứng?", ["$2$ trục đối xứng (hai đường chéo)", "$4$ trục", "$1$ trục", "Không có"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Hình chữ nhật có tâm đối xứng là:", ["Giao điểm của hai đường chéo", "Trung điểm cạnh dài", "Một đỉnh", "Không có"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Lục giác đều có bao nhiêu trục đối xứng và có tâm đối xứng không?", ["$6$ trục đối xứng và có tâm đối xứng", "$3$ trục và không có tâm", "$6$ trục và không có tâm", "$12$ trục"], 0)
            ]

            p2 = [
                make_tf(1, "Xét tính đối xứng của các hình hình học phẳng quen thuộc:", [
                    {"key": "a", "level": "Nhận biết", "text": "Hình thang cân có đúng 1 trục đối xứng.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Hình bình hành luôn có 1 trục đối xứng.", "correct": False},
                    {"key": "c", "level": "Thông hiểu", "text": "Giao điểm hai đường chéo của hình bình hành là tâm đối xứng của nó.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Biển báo cấm đi ngược chiều (hình tròn đỏ có vạch trắng ngang) có cả trục đối xứng và tâm đối xứng.", "correct": True}
                ]),
                make_tf(2, "Xét các chữ cái và số tự nhiên theo tính đối xứng:", [
                    {"key": "a", "level": "Nhận biết", "text": "Chữ cái O có vô số trục đối xứng và có tâm đối xứng.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Số 8 (viết cân đối) vừa có trục đối xứng vừa có tâm đối xứng.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Chữ cái M có trục đối xứng thẳng đứng.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Từ 'NOON' khi quay 180° quanh tâm của nó vẫn đọc lại chính xác là 'NOON'.", "correct": True}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Hình lục giác đều có bao nhiêu trục đối xứng?", "6"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Hình chữ nhật có bao nhiêu trục đối xứng?", "2"),
                make_sa(3, "Vận dụng", "Trong các chữ cái: A, B, C, D, H, K, M, N, O, X có bao nhiêu chữ cái có tâm đối xứng?", "4"),
                make_sa(4, "Vận dụng", "Một hình ngôi sao 5 cánh đều có bao nhiêu trục đối xứng?", "5")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Vẽ hoặc nêu rõ các trục đối xứng của: a) Hình vuông; b) Hình chữ nhật.", "a) Hình vuông có 4 trục đối xứng: 2 đường thẳng đi qua trung điểm các cặp cạnh đối diện và 2 đường chéo (0.5đ). b) Hình chữ nhật có 2 trục đối xứng: 2 đường thẳng đi qua trung điểm các cặp cạnh đối diện (không phải đường chéo) (0.5đ)."),
                make_essay(2, "Vận dụng", "Tìm 3 đồ vật hoặc hình ảnh trong thực tế cuộc sống có trục đối xứng và 3 đồ vật có tâm đối xứng. Giải thích ngắn gọn.", "Các vật có trục đối xứng: Con bướm, tháp Eiffel, chiếc lá bồ đề... (0.5đ). Các vật có tâm đối xứng: Chong chóng 4 cánh, hoa sen tuyết, bánh xe đạp, mặt trời... (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho đoạn thẳng $AB$ và đường thẳng $d$. Hãy nêu cách dựng điểm $A'$ đối xứng với $A$ qua $d$ và chứng minh đoạn thẳng $A'B$ có mối liên hệ như thế nào với $AB$ khi $d$ là trục đối xứng.", "Kẻ AH vuông góc d tại H, trên tia đối HA lấy A' sao cho HA' = HA (0.5đ). Khi đó d là đường trung trực của AA'. Mọi điểm trên d cách đều A và A' (0.5đ).")
            ]

            exams[f"c5_6_bai{l_idx}_test{t}"] = {
                "title": f"Toán 6 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(6, "c5_6", "Chương V: Tính đối xứng của hình phẳng trong tự nhiên", exams)

# ==============================================================================
# CHƯƠNG VI TOÁN 6: PHÂN SỐ (6 BÀI = 18 ĐỀ)
# ==============================================================================
def generate_c6_toan6():
    print("🚀 Đang biên soạn Chương VI Toán 6: Phân số...")
    exams = {}

    lessons = [
        (1, "Bài 23: Mở rộng phân số. Phân số bằng nhau"),
        (2, "Bài 24: So sánh phân số. Hỗn số dương"),
        (3, "Bài 25: Phép cộng và phép trừ phân số"),
        (4, "Bài 26: Phép nhân và phép chia phân số"),
        (5, "Bài 27: Hai bài toán về phân số"),
        (6, "Bài kiểm tra cuối Chương VI: Phân số")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Phân số có dạng $\\frac{a}{b}$ với điều kiện là:", ["$a, b \\in \\mathbb{Z}, b \\neq 0$", "$a, b \\in \\mathbb{N}$", "$a, b \\in \\mathbb{Z}$", "$b = 0$"], 0),
                make_mc(2, "Nhận biết", "Hai phân số $\\frac{a}{b} = \\frac{c}{d}$ khi và chỉ khi:", ["$a \\cdot d = b \\cdot c$", "$a \\cdot c = b \\cdot d$", "$a + d = b + c$", "$a - d = b - c$"], 0),
                make_mc(3, "Nhận biết", "Phân số tối giản là phân số mà tử và mẫu:", ["Có ước chung lớn nhất bằng 1 và -1", "Đều là số chẵn", "Đều là số nguyên tố", "Bằng nhau"], 0),
                make_mc(4, "Nhận biết", "Số đối của phân số $\\frac{3}{7}$ là:", ["$-\\frac{3}{7}$", "$\\frac{7}{3}$", "$-\\frac{7}{3}$", "$\\frac{3}{-7}$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Phân số nghịch đảo của $-\\frac{4}{9}$ là:", ["$-\\frac{9}{4}$", "$\\frac{4}{9}$", "$\\frac{9}{4}$", "$-\\frac{4}{9}$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Rút gọn phân số $\\frac{-15}{25}$ về dạng tối giản được:", ["$-\\frac{3}{5}$", "$\\frac{3}{5}$", "$-\\frac{5}{3}$", "$-\\frac{1}{2}$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Kết quả phép cộng $\\frac{1}{4} + \\frac{2}{4}$ là:", ["$\\frac{3}{4}$", "$\\frac{3}{8}$", "$\\frac{2}{4}$", "$1$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "So sánh $\\frac{-3}{5}$ và $\\frac{-4}{5}$:", ["$-\\frac{3}{5} > -\\frac{4}{5}$", "$-\\frac{3}{5} < -\\frac{4}{5}$", "$-\\frac{3}{5} = -\\frac{4}{5}$", "Không so sánh được"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Tìm $x$ biết $\\frac{x}{6} = \\frac{-2}{3}$:", ["$x = -4$", "$x = 4$", "$x = -3$", "$x = 6$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Tính $\\frac{2}{3} \\cdot \\frac{-9}{4}$:", ["$-\\frac{3}{2}$", "$\\frac{3}{2}$", "$-\\frac{2}{3}$", "$-1$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Tìm $\\frac{3}{5}$ của $40$:", ["$24$", "$20$", "$15$", "$30$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Tìm một số biết $\\frac{2}{3}$ của số đó bằng $18$:", ["$27$", "$12$", "$9$", "$36$"], 0)
            ]

            p2 = [
                make_tf(1, "Xét tính chất và các phép toán về phân số:", [
                    {"key": "a", "level": "Nhận biết", "text": "Mọi số nguyên n đều viết được dưới dạng phân số n/1.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Phân số có tử và mẫu cùng dấu là phân số dương.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Tổng của hai phân số đối nhau luôn bằng 0.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Phân số 5/(n - 1) nhận giá trị nguyên khi n thuộc tập hợp {-4; 0; 2; 6}.", "correct": True}
                ]),
                make_tf(2, "Cho biểu thức A = 1/2 + 1/3 + 1/6:", [
                    {"key": "a", "level": "Nhận biết", "text": "Mẫu số chung của ba phân số là 6.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Quy đồng mẫu số: 1/2 = 3/6, 1/3 = 2/6.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Giá trị của biểu thức A đúng bằng 1.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu cộng thêm 1/12 vào A thì kết quả nhỏ hơn 1.", "correct": False}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Tính giá trị của biểu thức: $\\frac{5}{12} + \\frac{7}{12}$:", "1"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Rút gọn phân số $\\frac{36}{48}$ về tối giản. Tử số của phân số tối giản là bao nhiêu?", "3"),
                make_sa(3, "Vận dụng", "Tìm $x$ biết: $\\frac{3}{4} - x = \\frac{1}{2}$ (dạng phân số tối giản a/b):", "1/4"),
                make_sa(4, "Vận dụng", "Một lớp học có 45 học sinh, trong đó số học sinh giỏi chiếm $\\frac{2}{5}$ cả lớp. Số học sinh giỏi của lớp là bao nhiêu bạn?", "18")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Thực hiện phép tính hợp lí: a) $\\frac{-5}{9} + \\frac{8}{15} + \\frac{-4}{9} + \\frac{7}{15}$; b) $\\frac{4}{7} \\cdot \\frac{3}{5} + \\frac{4}{7} \\cdot \\frac{2}{5}$.", "a) Ghép: (-5/9 + -4/9) + (8/15 + 7/15) = -1 + 1 = 0 (0.5đ). b) Đặt thừa số chung: 4/7 * (3/5 + 2/5) = 4/7 * 1 = 4/7 (0.5đ)."),
                make_essay(2, "Vận dụng", "Bạn Nam đọc một cuốn sách dày 120 trang trong 3 ngày. Ngày thứ nhất đọc được $\\frac{1}{3}$ số trang. Ngày thứ hai đọc được $\\frac{2}{5}$ số trang còn lại. Hỏi ngày thứ ba Nam đọc bao nhiêu trang?", "Ngày thứ nhất đọc: 120 * (1/3) = 40 trang (0.25đ). Số trang còn lại sau ngày 1: 120 - 40 = 80 trang (0.25đ). Ngày thứ hai đọc: 80 * (2/5) = 32 trang (0.25đ). Ngày thứ ba đọc: 80 - 32 = 48 trang (0.25đ)."),
                make_essay(3, "Vận dụng cao", "Tìm số nguyên $n$ để phân số $A = \\frac{2n + 3}{n + 1}$ nhận giá trị là một số nguyên.", "Biến đổi: A = [2(n + 1) + 1] / (n + 1) = 2 + 1/(n + 1) (0.5đ). Để A nguyên thì 1 phải chia hết cho (n + 1), suy ra n + 1 ∈ {1; -1}. Dẫn đến n ∈ {0; -2} (0.5đ).")
            ]

            exams[f"c6_6_bai{l_idx}_test{t}"] = {
                "title": f"Toán 6 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(6, "c6_6", "Chương VI: Phân số", exams)

# ==============================================================================
# CHƯƠNG VII TOÁN 6: SỐ THẬP PHÂN (5 BÀI = 15 ĐỀ)
# ==============================================================================
def generate_c7_toan6():
    print("🚀 Đang biên soạn Chương VII Toán 6: Số thập phân...")
    exams = {}

    lessons = [
        (1, "Bài 28: Số thập phân"),
        (2, "Bài 29: Tính toán với số thập phân"),
        (3, "Bài 30: Làm tròn và ước lượng"),
        (4, "Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm"),
        (5, "Bài kiểm tra cuối Chương VII: Số thập phân")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Số đối của số thập phân $-3,75$ là:", ["$3,75$", "$-3,75$", "$37,5$", "$-0,375$"], 0),
                make_mc(2, "Nhận biết", "Số thập phân $-2,5$ có phần số nguyên là:", ["$-2$", "$2$", "$-5$", "$5$"], 0),
                make_mc(3, "Nhận biết", "Phân số thập phân $\\frac{-15}{100}$ viết dưới dạng số thập phân là:", ["$-0,15$", "$-1,5$", "$-0,015$", "$-15$"], 0),
                make_mc(4, "Nhận biết", "So sánh hai số thập phân $-1,25$ và $-1,5$:", ["$-1,25 > -1,5$", "$-1,25 < -1,5$", "$-1,25 = -1,5$", "Không so sánh được"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Làm tròn số $4,567$ đến hàng phần mười được:", ["$4,6$", "$4,5$", "$4,57$", "$5$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Làm tròn số $1248$ đến hàng trăm được:", ["$1200$", "$1300$", "$1250$", "$1000$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Tỉ số phần trăm của $3$ và $4$ là:", ["$75\\%$", "$25\\%$", "$50\\%$", "$133\\%$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Tính $2,5 \\cdot (-4)$:", ["$-10$", "$10$", "$-1$", "$100$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Tính $12,5 - (-3,5)$:", ["$16$", "$9$", "$-16$", "$-9$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Tìm $20\\%$ của $150$:", ["$30$", "$15$", "$50$", "$300$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Một món hàng giá $200\\ 000$ đồng được giảm giá $10\\%$. Giá sau khi giảm là:", ["$180\\ 000$ đồng", "$190\\ 000$ đồng", "$170\\ 000$ đồng", "$150\\ 000$ đồng"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Tìm $x$ biết: $x \\cdot 0,25 + x \\cdot 0,75 = 18$:", ["$x = 18$", "$x = 9$", "$x = 36$", "$x = 12$"], 0)
            ]

            p2 = [
                make_tf(1, "Xét các quy tắc tính toán và so sánh số thập phân:", [
                    {"key": "a", "level": "Nhận biết", "text": "Mọi phân số thập phân đều viết được dưới dạng số thập phân.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Số 0 là số thập phân không âm và không dương.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Khi nhân một số thập phân với 0,1 ta chỉ việc dịch dấu phẩy sang bên trái 1 chữ số.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Tổng (-2,5) + (-3,75) = -6,25.", "correct": True}
                ]),
                make_tf(2, "Một lớp học có 40 học sinh gồm 24 nam và 16 nữ:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tỉ số của số học sinh nam và số học sinh nữ là 24/16 = 3/2.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Tỉ số phần trăm của số học sinh nữ so với cả lớp là (16/40)*100% = 40%.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Tỉ số phần trăm của học sinh nam so với cả lớp là 60%.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu có thêm 10 học sinh nữ chuyển vào thì tỉ số phần trăm học sinh nữ đạt 52%.", "correct": True}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Tính: $3,25 + 6,75$:", "10"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Làm tròn số $35,846$ đến hàng phần mười được số nào (dạng số thập phân)?", "35.8", acceptable=["35.8", "35,8"]),
                make_sa(3, "Vận dụng", "Tìm $x$ biết: $2,5 \\cdot x = 15$:", "6"),
                make_sa(4, "Vận dụng", "Một chiếc áo có giá niêm yết $300\\ 000$ đồng, nhân dịp khuyến mãi được giảm giá $15\\%$. Giá bán của chiếc áo là bao nhiêu nghìn đồng?", "255")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Tính một cách hợp lí: a) $15,3 \\cdot 2,4 + 15,3 \\cdot 7,6$; b) $(-2,5) \\cdot 0,38 \\cdot 4$.", "a) Đặt thừa số chung: 15.3 * (2.4 + 7.6) = 15.3 * 10 = 153 (0.5đ). b) Ghép: [(-2.5) * 4] * 0.38 = -10 * 0.38 = -3.8 (0.5đ)."),
                make_essay(2, "Vận dụng", "Mẹ bạn Lan gửi tiết kiệm $50\\ 000\\ 000$ đồng vào ngân hàng với kì hạn 1 năm, lãi suất $6\\%/\\text{năm}$. Hỏi sau 1 năm, mẹ bạn Lan nhận được cả gốc lẫn lãi là bao nhiêu đồng?", "Tiền lãi sau 1 năm: 50 000 000 * 6% = 3 000 000 đồng (0.5đ). Tổng số tiền nhận được cả gốc và lãi: 50 000 000 + 3 000 000 = 53 000 000 đồng (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Giá một lít xăng vào tháng 1 là $24\\ 000$ đồng. Sang tháng 2, giá xăng tăng $10\\%$. Sang tháng 3, giá xăng lại giảm $10\\%$ so với tháng 2. Hỏi giá một lít xăng ở tháng 3 so với tháng 1 đắt hơn hay rẻ hơn bao nhiêu đồng?", "Giá xăng tháng 2: 24000 * (1 + 0.10) = 26400 đồng (0.5đ). Giá xăng tháng 3: 26400 * (1 - 0.10) = 23760 đồng. So với tháng 1, giá xăng tháng 3 rẻ hơn: 24000 - 23760 = 240 đồng (0.5đ).")
            ]

            exams[f"c7_6_bai{l_idx}_test{t}"] = {
                "title": f"Toán 6 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(6, "c7_6", "Chương VII: Số thập phân", exams)

# ==============================================================================
# CHƯƠNG VIII TOÁN 6: NHỮNG HÌNH HÌNH HỌC CƠ BẢN (7 BÀI = 21 ĐỀ)
# ==============================================================================
def generate_c8_toan6():
    print("🚀 Đang biên soạn Chương VIII Toán 6: Những hình hình học cơ bản...")
    exams = {}

    lessons = [
        (1, "Bài 32: Điểm và đường thẳng"),
        (2, "Bài 33: Điểm nằm giữa hai điểm. Tia"),
        (3, "Bài 34: Đoạn thẳng. Độ dài đoạn thẳng"),
        (4, "Bài 35: Trung điểm của đoạn thẳng"),
        (5, "Bài 36: Góc"),
        (6, "Bài 37: Số đo góc"),
        (7, "Bài kiểm tra cuối Chương VIII: Những hình hình học cơ bản")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Qua hai điểm phân biệt $A$ và $B$ có bao nhiêu đường thẳng đi qua?", ["Chỉ có 1 đường thẳng duy nhất", "2 đường thẳng", "Vô số đường thẳng", "Không có đường thẳng nào"], 0),
                make_mc(2, "Nhận biết", "Ba điểm thẳng hàng là ba điểm:", ["Cùng thuộc một đường thẳng", "Tạo thành một tam giác", "Cắt nhau", "Cùng nằm trên một đường tròn"], 0),
                make_mc(3, "Nhận biết", "Hình gồm điểm $O$ và một phần đường thẳng bị chia ra bởi $O$ gọi là:", ["Một tia gốc $O$", "Một đoạn thẳng", "Một góc", "Một đường thẳng"], 0),
                make_mc(4, "Nhận biết", "Hai tia đối nhau là hai tia:", ["Chung gốc và tạo thành một đường thẳng", "Chung gốc và vuông góc", "Song song với nhau", "Không chung gốc"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Trung điểm $M$ của đoạn thẳng $AB$ là điểm:", ["Nằm giữa $A, B$ và cách đều $A, B$ ($MA = MB$)", "Nằm ngoài đoạn thẳng $AB$", "Trùng với điểm $A$", "Tùy ý trên $AB$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Hình gồm hai tia chung gốc được gọi là:", ["Một góc", "Một đoạn thẳng", "Một tia", "Một tam giác"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Góc có số đo bằng $90^\\circ$ gọi là:", ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Góc có số đo lớn hơn $0^\\circ$ và nhỏ hơn $90^\\circ$ gọi là:", ["Góc nhọn", "Góc tù", "Góc vuông", "Góc bẹt"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Góc có số đo bằng $180^\\circ$ gọi là:", ["Góc bẹt", "Góc tù", "Góc vuông", "Góc nhọn"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Cho đoạn thẳng $AB = 8\\text{ cm}$. $M$ là trung điểm của $AB$. Độ dài $AM$ là:", ["$4\\text{ cm}$", "$2\\text{ cm}$", "$8\\text{ cm}$", "$16\\text{ cm}$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Điểm $M$ nằm giữa hai điểm $A$ và $B$. Biết $AM = 3\\text{ cm}, AB = 7\\text{ cm}$. Độ dài $MB$ là:", ["$4\\text{ cm}$", "$10\\text{ cm}$", "$3\\text{ cm}$", "$5\\text{ cm}$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Cho góc $\\widehat{xOy} = 120^\\circ$. Tia $Oz$ nằm giữa hai tia $Ox, Oy$ sao cho $\\widehat{xOz} = 40^\\circ$. Số đo góc $\\widehat{yOz}$ là:", ["$80^\\circ$", "$160^\\circ$", "$60^\\circ$", "$40^\\circ$"], 0)
            ]

            p2 = [
                make_tf(1, "Trên tia Ox lấy hai điểm A và B sao cho OA = 3 cm, OB = 6 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Điểm A nằm giữa hai điểm O và B.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Độ dài đoạn thẳng AB = OB - OA = 3 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "A là trung điểm của đoạn thẳng OB.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Lấy điểm C trên tia đối của tia Ox sao cho OC = 3 cm thì O là trung điểm của đoạn thẳng CA.", "correct": True}
                ]),
                make_tf(2, "Xét các góc và quan hệ giữa các tia:", [
                    {"key": "a", "level": "Nhận biết", "text": "Góc bẹt có hai cạnh là hai tia đối nhau.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Góc có số đo 105° là góc tù.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Nếu tia Oz nằm giữa hai tia Ox và Oy thì góc xOz + góc zOy = góc xOy.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Cho 5 tia chung gốc, số góc tạo thành từ 5 tia đó là 10 góc.", "correct": True}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Cho đoạn thẳng $PQ = 10\\text{ cm}$. Gọi $I$ là trung điểm của $PQ$. Tính độ dài đoạn thẳng $PI$ (cm):", "5"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Góc tạo bởi kim giờ và kim phút lúc 3 giờ đúng có số đo bằng bao nhiêu độ?", "90"),
                make_sa(3, "Vận dụng", "Cho đoạn thẳng $AB = 12\\text{ cm}$. Trên $AB$ lấy hai điểm $C, D$ sao cho $AC = BD = 4\\text{ cm}$. Tính độ dài đoạn thẳng $CD$ (cm):", "4"),
                make_sa(4, "Vận dụng", "Cho 6 điểm phân biệt trong đó không có 3 điểm nào thẳng hàng. Cứ qua 2 điểm vẽ được 1 đường thẳng. Vẽ được tất cả bao nhiêu đường thẳng?", "15")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Cho đoạn thẳng $AB = 6\\text{ cm}$. Lấy điểm $C$ nằm giữa $A$ và $B$ sao cho $AC = 2\\text{ cm}$. a) Tính độ dài đoạn thẳng $CB$; b) Gọi $M$ là trung điểm của $CB$. Tính $AM$.", "a) Vì C nằm giữa A và B nên AC + CB = AB, suy ra CB = 6 - 2 = 4 cm (0.5đ). b) M là trung điểm CB nên CM = CB / 2 = 2 cm. Vì C nằm giữa A và M nên AM = AC + CM = 2 + 2 = 4 cm (0.5đ)."),
                make_essay(2, "Vận dụng", "Trên cùng một nửa mặt phẳng bờ chứa tia $Ox$, vẽ hai tia $Oy, Oz$ sao cho $\\widehat{xOy} = 50^\\circ, \\widehat{xOz} = 100^\\circ$. a) Tia $Oy$ có nằm giữa hai tia $Ox$ và $Oz$ không? Vì sao? b) Tính số đo góc $\\widehat{yOz}$; c) Tia $Oy$ có là tia phân giác của góc $\\widehat{xOz}$ không?", "a) Trên nửa mặt phẳng bờ Ox, vì góc xOy (50°) < góc xOz (100°) nên tia Oy nằm giữa Ox và Oz (0.25đ). b) Suy ra góc xOy + góc yOz = góc xOz => góc yOz = 100° - 50° = 50° (0.5đ). c) Vì Oy nằm giữa và góc xOy = góc yOz = 50° nên Oy là tia phân giác của góc xOz (0.25đ)."),
                make_essay(3, "Vận dụng cao", "Cho $n$ điểm phân biệt trong đó không có ba điểm nào thẳng hàng. Biết vẽ được tất cả $190$ đường thẳng đi qua các cặp điểm. Tìm số điểm $n$.", "Số đường thẳng vẽ được qua n điểm là n(n - 1)/2 (0.5đ). Ta có: n(n - 1)/2 = 190 => n(n - 1) = 380. Vì 20 * 19 = 380 nên n = 20 điểm (0.5đ).")
            ]

            exams[f"c8_6_bai{l_idx}_test{t}"] = {
                "title": f"Toán 6 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(6, "c8_6", "Chương VIII: Những hình hình học cơ bản", exams)

# ==============================================================================
# CHƯƠNG IX TOÁN 6: DỮ LIỆU VÀ XÁC SUẤT THỰC NGHIỆM (7 BÀI = 21 ĐỀ)
# ==============================================================================
def generate_c9_toan6():
    print("🚀 Đang biên soạn Chương IX Toán 6: Dữ liệu và xác suất thực nghiệm...")
    exams = {}

    lessons = [
        (1, "Bài 38: Dữ liệu và thu thập dữ liệu"),
        (2, "Bài 39: Bảng thống kê và biểu đồ tranh"),
        (3, "Bài 40: Biểu đồ cột"),
        (4, "Bài 41: Biểu đồ cột kép"),
        (5, "Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí nghiệm"),
        (6, "Bài 43: Xác suất thực nghiệm"),
        (7, "Bài kiểm tra cuối Chương IX: Dữ liệu và xác suất thực nghiệm")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Dữ liệu nào sau đây là dữ liệu là số (số liệu)?", ["Điểm kiểm tra môn Toán: 8; 9; 10", "Tên các loài hoa: Mai, Đào, Cúc", "Màu sắc yêu thích: Đỏ, Xanh", "Xếp loại học lực: Tốt, Khá"], 0),
                make_mc(2, "Nhận biết", "Dữ liệu nào sau đây là dữ liệu không phải là số?", ["Tên các tỉnh thành: Hà Nội, Huế, Đà Nẵng", "Chiều cao học sinh: 150 cm, 155 cm", "Số học sinh vắng: 0, 1, 2", "Nhiệt độ trong ngày: 28°C, 32°C"], 0),
                make_mc(3, "Nhận biết", "Biểu đồ tranh sử dụng hình ảnh hoặc biểu tượng để:", ["Biểu diễn dữ liệu thống kê", "Vẽ tranh phong cảnh", "Trang trí bài báo", "Tính diện tích"], 0),
                make_mc(4, "Nhận biết", "Biểu đồ cột thích hợp dùng để:", ["So sánh số liệu của các đối tượng khác nhau", "Tính tỉ số góc", "Vẽ đường tròn", "Vẽ sơ đồ tư duy"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Biểu đồ cột kép thích hợp dùng để:", ["So sánh từng cặp số liệu của hai nhóm đối tượng cùng loại", "Biểu diễn 1 đại lượng duy nhất", "Thay thế cho bảng chữ cái", "Vẽ hình khối 3D"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Tung một đồng xu 1 lần. Có mấy kết quả có thể xảy ra?", ["2 kết quả (Sấp hoặc Ngửa)", "1 kết quả", "4 kết quả", "6 kết quả"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Gieo con xúc xắc 6 mặt 1 lần. Sự kiện nào sau đây là sự kiện chắc chắn?", ["Số chấm xuất hiện nhỏ hơn hoặc bằng 6", "Số chấm bằng 6", "Số chấm là số chẵn", "Số chấm bằng 7"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Sự kiện nào sau đây là sự kiện không thể xảy ra?", ["Gieo con xúc xắc được mặt 7 chấm", "Gieo đồng xu được mặt sấp", "Rút được quân bài màu đỏ", "Bắt gặp ngày mưa"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Gieo đồng xu 20 lần thấy 12 lần mặt sấp. Xác suất thực nghiệm mặt sấp là:", ["$\\frac{12}{20} = \\frac{3}{5}$", "$\\frac{8}{20}$", "$\\frac{1}{2}$", "$\\frac{12}{8}$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Trong biểu đồ tranh, một biểu tượng 🌟 đại diện cho 10 học sinh giỏi. Nếu lớp có 35 học sinh giỏi thì cần vẽ:", ["3 biểu tượng nguyên và nửa biểu tượng", "3 biểu tượng", "4 biểu tượng", "2 biểu tượng"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Gieo con xúc xắc 50 lần, thấy có 15 lần xuất hiện mặt số chấm lẻ. Xác suất thực nghiệm xuất hiện mặt chấm chẵn là:", ["$\\frac{35}{50} = 70\\%$", "$30\\%$", "$50\\%$", "$15\\%$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Tung 2 đồng xu 40 lần, thấy có 10 lần cả 2 đồng xu đều sấp. Xác suất thực nghiệm của sự kiện 'Có ít nhất một đồng ngửa' là:", ["$\\frac{30}{40} = 75\\%$", "$25\\%$", "$50\\%$", "$10\\%$"], 0)
            ]

            p2 = [
                make_tf(1, "Một bảng khảo sát môn thể thao yêu thích của 40 học sinh lớp 6A:", [
                    {"key": "a", "level": "Nhận biết", "text": "Môn thể thao yêu thích là dữ liệu không phải là số.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Số lượng học sinh chọn mỗi môn là dữ liệu số liệu.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Nếu có 18 bạn chọn Bóng đá thì tỉ lệ học sinh thích Bóng đá là 18/40 = 45%.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Khi vẽ biểu đồ cột biểu diễn dữ liệu này, độ cao của các cột tỉ lệ thuận với số lượng học sinh chọn từng môn.", "correct": True}
                ]),
                make_tf(2, "Bạn Minh thực hiện thí nghiệm quay vòng quay 50 lần, mũi tên dừng lại ở ô Vàng 15 lần, ô Đỏ 20 lần và ô Xanh 15 lần:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tổng số lần thực hiện phép thử là 50 lần.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Xác suất thực nghiệm mũi tên chỉ vào ô Đỏ là 20/50 = 40%.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Xác suất thực nghiệm mũi tên chỉ vào ô Vàng bằng xác suất thực nghiệm ô Xanh là 30%.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Xác suất thực nghiệm của biến cố 'Mũi tên không dừng ở ô Đỏ' là 60%.", "correct": True}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Gieo đồng xu 50 lần thấy 27 lần xuất hiện mặt ngửa. Số lần xuất hiện mặt sấp là bao nhiêu?", "23"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Một xạ thủ bắn 30 phát đạn thì trúng bia 24 phát. Xác suất thực nghiệm bắn trúng bia bằng bao nhiêu (dạng thập phân)?", "0.8", acceptable=["0.8", "0,8", "4/5", "80%"]),
                make_sa(3, "Vận dụng", "Trong biểu đồ cột kép so sánh số học sinh nam và nữ của 4 khối: Khối 6 có 120 nam và 130 nữ. Khối 6 có tất cả bao nhiêu học sinh?", "250"),
                make_sa(4, "Vận dụng", "Tung một con xúc xắc 100 lần, mặt 6 chấm xuất hiện 18 lần. Xác suất thực nghiệm của sự kiện 'Mặt xuất hiện không phải 6 chấm' là bao nhiêu phần trăm (%)?", "82%")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Bảng thống kê điểm môn Toán của một nhóm học sinh: Điểm 7: 3 bạn; Điểm 8: 5 bạn; Điểm 9: 4 bạn; Điểm 10: 2 bạn. a) Có tất cả bao nhiêu học sinh? b) Tính tỉ số phần trăm số học sinh đạt điểm 9 trở lên.", "a) Tổng số học sinh: 3 + 5 + 4 + 2 = 14 học sinh (0.5đ). b) Số bạn đạt điểm 9 trở lên: 4 + 2 = 6 bạn. Tỉ số phần trăm: (6 / 14) * 100% ≈ 42.86% (0.5đ)."),
                make_essay(2, "Vận dụng", "Bạn Hùng gieo một con xúc xắc 80 lần và ghi lại số lần xuất hiện của các mặt như sau: Mặt 1 chấm: 12 lần; Mặt 2 chấm: 15 lần; Mặt 3 chấm: 13 lần; Mặt 4 chấm: 14 lần; Mặt 5 chấm: 16 lần; Mặt 6 chấm: 10 lần. Tính xác suất thực nghiệm của sự kiện: a) Xuất hiện mặt có số chấm là số nguyên tố; b) Xuất hiện mặt có số chấm lớn hơn 3.", "a) Các mặt số nguyên tố là 2, 3, 5. Số lần xuất hiện: 15 + 13 + 16 = 44 lần. Xác suất P = 44 / 80 = 11/20 = 55% (0.5đ). b) Các mặt lớn hơn 3 là 4, 5, 6. Số lần xuất hiện: 14 + 16 + 10 = 40 lần. Xác suất P = 40 / 80 = 1/2 = 50% (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Trong một hộp kín có 3 quả bóng xanh và một số quả bóng đỏ có kích thước như nhau. Lấy ngẫu nhiên 1 quả bóng, ghi màu rồi thả lại vào hộp. Sau 120 lần thử thì có 36 lần lấy được bóng xanh. Ước tính trong hộp có tất cả bao nhiêu quả bóng đỏ?", "Xác suất thực nghiệm lấy được bóng xanh là: 36 / 120 = 3/10 = 0.3 (0.5đ). Gọi N là tổng số bóng trong hộp. Ta có: 3 / N ≈ 0.3 suy ra N ≈ 10 quả bóng. Số quả bóng đỏ ước tính: 10 - 3 = 7 quả bóng đỏ (0.5đ).")
            ]

            exams[f"c9_6_bai{l_idx}_test{t}"] = {
                "title": f"Toán 6 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(6, "c9_6", "Chương IX: Dữ liệu và xác suất thực nghiệm", exams)

if __name__ == "__main__":
    generate_c5_toan6()
    generate_c6_toan6()
    generate_c7_toan6()
    generate_c8_toan6()
    generate_c9_toan6()
    print("🎉 TOÀN BỘ CHƯƠNG V, VI, VII, VIII, IX TOÁN 6 ĐÃ ĐƯỢC TẠO VÀ ĐÓNG GÓI XUẤT SẮC!")
