# -*- coding: utf-8 -*-
"""
HỆ THỐNG BIÊN SOẠN TOÀN DIỆN TOÁN 9: CHƯƠNG V, VI, VII, VIII, IX, X
Tạo trọn vẹn:
- grade9_c5_9_exams.json / .js (18 đề)
- grade9_c6_9_exams.json / .js (15 đề)
- grade9_c7_9_exams.json / .js (12 đề)
- grade9_c8_9_exams.json / .js (9 đề)
- grade9_c9_9_exams.json / .js (15 đề)
- grade9_c10_9_exams.json / .js (9 đề)
Tổng cộng: 78 đề kiểm tra chuẩn ma trận 2025.
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package

# ==============================================================================
# CHƯƠNG V TOÁN 9: ĐƯỜNG TRÒN (6 BÀI = 18 ĐỀ)
# ==============================================================================
def generate_c5_toan9():
    print("🚀 Đang biên soạn Chương V Toán 9: Đường tròn...")
    exams = {}

    lessons = [
        (1, "Bài 13: Mở đầu về đường tròn"),
        (2, "Bài 14: Cung và dây của một đường tròn"),
        (3, "Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên"),
        (4, "Bài 16: Vị trí tương đối của đường thẳng và đường tròn"),
        (5, "Bài 17: Vị trí tương đối của hai đường tròn"),
        (6, "Bài kiểm tra cuối Chương V: Đường tròn")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Đường kính của đường tròn $(O; R)$ có độ dài bằng:", ["$2R$", "$R$", "$\\pi R$", "$\\frac{R}{2}$"], 0),
                make_mc(2, "Nhận biết", "Trong các dây của đường tròn, dây lớn nhất là:", ["Đường kính", "Dây bất kì qua tâm", "Dây vuông góc với bán kính", "Bán kính"], 0),
                make_mc(3, "Nhận biết", "Đường kính vuông góc với một dây thì:", ["Đi qua trung điểm của dây ấy", "Song song với dây ấy", "Bằng dây ấy", "Không cắt dây ấy"], 0),
                make_mc(4, "Nhận biết", "Đường thẳng và đường tròn tiếp xúc nhau khi số điểm chung là:", ["$1$ điểm chung duy nhất", "$2$ điểm chung", "$0$ điểm chung", "Vô số"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Khoảng cách từ tâm $O$ đến đường thẳng $d$ là $d_0$. Nếu $d_0 = R$ thì đường thẳng $d$:", ["Tiếp xúc với đường tròn (là tiếp tuyến)", "Cắt đường tròn tại 2 điểm", "Không cắt đường tròn", "Đi qua tâm"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính chu vi đường tròn bán kính $R$ là:", ["$C = 2\\pi R$", "$C = \\pi R^2$", "$C = 4\\pi R$", "$C = \\pi R$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính diện tích hình tròn bán kính $R$ là:", ["$S = \\pi R^2$", "$S = 2\\pi R$", "$S = 4\\pi R^2$", "$S = \\frac{1}{2}\\pi R^2$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Độ dài cung tròn $n^\\circ$ của đường tròn bán kính $R$ là:", ["$l = \\frac{\\pi R n}{180}$", "$l = \\frac{\\pi R^2 n}{360}$", "$l = \\frac{2\\pi R n}{360}$", "$l = \\frac{\\pi R n}{90}$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Diện tích hình quạt tròn bán kính $R$ ứng với cung $n^\\circ$ là:", ["$S = \\frac{\\pi R^2 n}{360}$", "$S = \\frac{\\pi R n}{180}$", "$S = \\frac{1}{2} l \\cdot R$", "$S = \\pi R^2$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hai đường tròn $(O; R)$ và $(O'; r)$ tiếp xúc ngoài khi khoảng cách đoạn nối tâm $OO'$ bằng:", ["$R + r$", "$|R - r|$", "$R - r$", "$2(R + r)$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Cho đường tròn $(O; 5\\text{ cm})$ và dây $AB = 8\\text{ cm}$. Khoảng cách từ tâm $O$ đến dây $AB$ bằng:", ["$3\\text{ cm}$", "$4\\text{ cm}$", "$2\\text{ cm}$", "$5\\text{ cm}$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Từ điểm $M$ nằm ngoài $(O; R)$ vẽ hai tiếp tuyến $MA, MB$. Biết $OM = 2R$. Góc tạo bởi hai tiếp tuyến $\\widehat{AMB}$ bằng:", ["$60^\\circ$", "$90^\\circ$", "$120^\\circ$", "$45^\\circ$"], 0)
            ]

            p2 = [
                make_tf(1, "Cho đường tròn (O; R) có đường kính AB và một dây CD không đi qua tâm vuông góc với AB tại H:", [
                    {"key": "a", "level": "Nhận biết", "text": "H là trung điểm của dây CD.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Tam giác OCD là tam giác cân tại O.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Nếu R = 10 cm và khoảng cách OH = 6 cm thì độ dài dây CD = 16 cm.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Tứ giác ACBD luôn là hình thoi trong mọi vị trí của H trên AB.", "correct": False}
                ]),
                make_tf(2, "Cho đường tròn (O; 6 cm) và điểm M cách O một khoảng OM = 10 cm. Kẻ hai tiếp tuyến MA, MB với đường tròn (A, B là các tiếp điểm):", [
                    {"key": "a", "level": "Nhận biết", "text": "OA vuông góc với MA tại tiếp điểm A.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Độ dài đoạn tiếp tuyến MA = √(10² - 6²) = 8 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "MO là tia phân giác của góc AMB.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Đoạn thẳng nối hai tiếp điểm AB có độ dài bằng 9,6 cm.", "correct": True}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Cho đường tròn $(O; 10\\text{ cm})$. Dây $AB$ cách tâm $O$ một khoảng $6\\text{ cm}$. Độ dài dây $AB$ bằng bao nhiêu cm?", "16"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Tính diện tích hình tròn có chu vi bằng $12\\pi\\text{ cm}$ (kết quả theo số nguyên nhân với $\\pi$, chỉ điền hệ số số nguyên):", "36"),
                make_sa(3, "Vận dụng", "Tính diện tích hình quạt tròn có bán kính $R = 6\\text{ cm}$, số đo cung $60^\\circ$ (kết quả theo $\\pi$, chỉ điền hệ số nguyên):", "6"),
                make_sa(4, "Vận dụng", "Cho hai đường tròn đồng tâm có bán kính $R_1 = 5\\text{ cm}$ và $R_2 = 3\\text{ cm}$. Diện tích hình vành khuyên giới hạn bởi hai đường tròn là $k\\pi\\text{ cm}^2$. Giá trị của $k$ bằng bao nhiêu?", "16")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Cho đường tròn $(O; R)$ và điểm $A$ nằm ngoài đường tròn. Kẻ tiếp tuyến $AB$ với đường tròn ($B$ là tiếp điểm). Biết $R = 5\\text{ cm}, AB = 12\\text{ cm}$. Tính độ dài đoạn thẳng $OA$ và $\\sin\\widehat{AOB}$.", "Tam giác OAB vuông tại B vì AB là tiếp tuyến (0.25đ). Áp dụng định lí Pythagore: OA = √(OB² + AB²) = √(5² + 12²) = 13 cm (0.5đ). sin(AOB) = AB / OA = 12 / 13 (0.25đ)."),
                make_essay(2, "Vận dụng", "Cho đường tròn $(O)$, hai dây cung $AB$ và $CD$ bằng nhau và cắt nhau tại điểm $I$ bên trong đường tròn. Chứng minh rằng: a) Khoảng cách từ $O$ đến hai dây $AB, CD$ bằng nhau; b) $IA = IC$ và $IB = ID$.", "a) Kẻ OH vuông góc AB, OK vuông góc CD. Vì AB = CD nên OH = OK (hai dây bằng nhau cách đều tâm) (0.5đ). b) Tam giác OHI = tam giác OKI (cạnh huyền - cạnh góc vuông) suy ra IH = IK. Vì H, K là trung điểm của AB, CD nên HA = KC suy ra IA = IC và IB = ID (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho nửa đường tròn đường kính $AB = 2R$. Lấy điểm $C$ trên nửa đường tròn. Kẻ $CH \\perp AB$ ($H \\in AB$). Tìm vị trí của điểm $C$ trên nửa đường tròn để diện tích tam giác $CAB$ đạt giá trị lớn nhất.", "Diện tích tam giác CAB: S = 1/2 * AB * CH = 1/2 * 2R * CH = R * CH (0.5đ). Diện tích S lớn nhất khi đường cao CH lớn nhất. Trong nửa đường tròn, CH ≤ R, dấu '=' xảy ra khi H trùng với tâm O, tức C là điểm chính giữa của cung AB. Khi đó diện tích lớn nhất bằng R² (0.5đ).")
            ]

            exams[f"c5_9_bai{l_idx}_test{t}"] = {
                "title": f"Toán 9 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(9, "c5_9", "Chương V: Đường tròn", exams)

# ==============================================================================
# CHƯƠNG VI TOÁN 9: HÀM SỐ Y = AX^2 VÀ PHƯƠNG TRÌNH BẬC HAI (5 BÀI = 15 ĐỀ)
# ==============================================================================
def generate_c6_toan9():
    print("🚀 Đang biên soạn Chương VI Toán 9: Hàm số y = ax^2 và Phương trình bậc hai...")
    exams = {}

    lessons = [
        (1, "Bài 18: Hàm số y = ax^2 (a != 0)"),
        (2, "Bài 19: Phương trình bậc hai một ẩn"),
        (3, "Bài 20: Định lí Viète và ứng dụng"),
        (4, "Bài 21: Giải bài toán bằng cách lập phương trình"),
        (5, "Bài kiểm tra cuối Chương VI: Hàm số y = ax^2 (a != 0). Phương trình bậc hai một ẩn")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:", ["Một đường cong Parabol đi qua gốc tọa độ $O$", "Một đường thẳng", "Một đường tròn", "Một đường hyperbol"], 0),
                make_mc(2, "Nhận biết", "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:", ["$x > 0$", "$x < 0$", "Với mọi $x$", "$x = 0$"], 0),
                make_mc(3, "Nhận biết", "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:", ["$b^2 - 4ac$", "$b^2 + 4ac$", "$4ac - b^2$", "$b - 4ac$"], 0),
                make_mc(4, "Nhận biết", "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:", ["$\\Delta > 0$", "$\\Delta = 0$", "$\\Delta < 0$", "$\\Delta \\le 0$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:", ["$\\Delta = 0$", "$\\Delta > 0$", "$\\Delta < 0$", "$a = c$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:", ["$-\\frac{b}{a}$", "$\\frac{b}{a}$", "$\\frac{c}{a}$", "$-\\frac{c}{a}$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:", ["$\\frac{c}{a}$", "$-\\frac{c}{a}$", "$\\frac{b}{a}$", "$-\\frac{b}{a}$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:", ["$x_1 = 1, x_2 = \\frac{c}{a}$", "$x_1 = -1, x_2 = -\\frac{c}{a}$", "$x_1 = 0$", "$x_1 = 2$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:", ["$x_1 = 2, x_2 = 3$", "$x_1 = -2, x_2 = -3$", "$x_1 = 1, x_2 = 6$", "$x_1 = -1, x_2 = -6$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?", ["$A(1; 2)$", "$B(2; 4)$", "$C(-1; -2)$", "$D(0; 2)$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:", ["$29$", "$49$", "$39$", "$19$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:", ["$m < 1$", "$m > 1$", "$m = 1$", "$m \\le 1$"], 0)
            ]

            p2 = [
                make_tf(1, "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:", [
                    {"key": "a", "level": "Nhận biết", "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).", "correct": True}
                ]),
                make_tf(2, "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):", [
                    {"key": "a", "level": "Nhận biết", "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.", "correct": True}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:", "4"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:", "-6"),
                make_sa(3, "Vận dụng", "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:", "4"),
                make_sa(4, "Vận dụng", "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?", "30")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.", "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."),
                make_essay(2, "Vận dụng", "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?", "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."),
                make_essay(3, "Vận dụng cao", "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.", "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ).")
            ]

            exams[f"c6_9_bai{l_idx}_test{t}"] = {
                "title": f"Toán 9 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(9, "c6_9", "Chương VI: Hàm số y = ax^2 (a != 0). Phương trình bậc hai một ẩn", exams)

# ==============================================================================
# CHƯƠNG VII TOÁN 9: TẦN SỐ VÀ TẦN SỐ TƯƠNG ĐỐI (4 BÀI = 12 ĐỀ)
# ==============================================================================
def generate_c7_toan9():
    print("🚀 Đang biên soạn Chương VII Toán 9: Tần số và tần số tương đối...")
    exams = {}

    lessons = [
        (1, "Bài 22: Bảng tần số và biểu đồ tần số"),
        (2, "Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối"),
        (3, "Bài 24: Bảng tần số ghép nhóm và biểu đồ"),
        (4, "Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:", ["Tần số của giá trị đó", "Tần số tương đối", "Mốt", "Trung bình cộng"], 0),
                make_mc(2, "Nhận biết", "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:", ["Tần số tương đối của giá trị đó", "Tần số tuyệt đối", "Tỉ số truyền", "Phương sai"], 0),
                make_mc(3, "Nhận biết", "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:", ["$100\\%$ (hoặc $1$)", "$50\\%$", "$0\\%$", "$200\\%$"], 0),
                make_mc(4, "Nhận biết", "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?", ["Biểu đồ hình quạt tròn hoặc biểu đồ cột", "Biểu đồ đường chéo", "Biểu đồ hình nón", "Biểu đồ hàm số"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:", ["$\\frac{a + b}{2}$", "$b - a$", "$a$", "$b$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Độ rộng của nhóm $[10; 20)$ là:", ["$10$", "$20$", "$15$", "$30$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:", ["$30\\%$", "$15\\%$", "$50\\%$", "$25\\%$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:", ["$90^\\circ$", "$45^\\circ$", "$180^\\circ$", "$60^\\circ$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:", ["$144^\\circ$", "$40^\\circ$", "$100^\\circ$", "$120^\\circ$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:", ["$35\\%$", "$20\\%$", "$40\\%$", "$70\\%$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:", ["$20\\%$", "$15\\%$", "$10\\%$", "$25\\%$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:", ["$10$ học sinh", "$8$ học sinh", "$12$ học sinh", "$15$ học sinh"], 0)
            ]

            p2 = [
                make_tf(1, "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Tần số tương đối của học sinh Khá là 45%.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.", "correct": True}
                ]),
                make_tf(2, "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:", [
                    {"key": "a", "level": "Nhận biết", "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.", "correct": True}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):", "25%"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:", "25"),
                make_sa(3, "Vận dụng", "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):", "20%"),
                make_sa(4, "Vận dụng", "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?", "160")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).", "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."),
                make_essay(2, "Vận dụng", "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.", "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."),
                make_essay(3, "Vận dụng cao", "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.", "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ).")
            ]

            exams[f"c7_9_bai{l_idx}_test{t}"] = {
                "title": f"Toán 9 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(9, "c7_9", "Chương VII: Tần số và tần số tương đối", exams)

# ==============================================================================
# CHƯƠNG VIII TOÁN 9: XÁC SUẤT CỦA BIẾN CỐ (3 BÀI = 9 ĐỀ)
# ==============================================================================
def generate_c8_toan9():
    print("🚀 Đang biên soạn Chương VIII Toán 9: Xác suất của biến cố...")
    exams = {}

    lessons = [
        (1, "Bài 25: Phép thử ngẫu nhiên và không gian mẫu"),
        (2, "Bài 26: Xác suất của biến cố liên quan đến phép thử"),
        (3, "Bài kiểm tra cuối Chương VIII: Xác suất của biến cố trong một số mô hình xác suất đơn giản")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Tập hợp tất cả các kết quả có thể xảy ra của một phép thử ngẫu nhiên gọi là:", ["Không gian mẫu", "Biến cố", "Tần số", "Tập rỗng"], 0),
                make_mc(2, "Nhận biết", "Kí hiệu không gian mẫu là:", ["$\\Omega$", "$E$", "$P$", "$\\Delta$"], 0),
                make_mc(3, "Nhận biết", "Gieo đồng thời hai con xúc xắc. Số phần tử của không gian mẫu $n(\\Omega)$ là:", ["$36$", "$12$", "$6$", "$64$"], 0),
                make_mc(4, "Nhận biết", "Tung ba đồng xu cân đối. Số kết quả có thể là:", ["$8$", "$6$", "$4$", "$9$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Xác suất của biến cố chắc chắn $\\Omega$ bằng:", ["$1$", "$0$", "$0.5$", "$100$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Xác suất của biến cố không thể $\\emptyset$ bằng:", ["$0$", "$1$", "$-1$", "$0.5$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Gieo hai con xúc xắc. Xác suất để tổng số chấm bằng 12 là:", ["$\\frac{1}{36}$", "$\\frac{1}{12}$", "$\\frac{1}{6}$", "$\\frac{2}{36}$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Một hộp có 4 bi đỏ và 6 bi xanh. Rút ngẫu nhiên 1 bi. Xác suất rút được bi đỏ là:", ["$\\frac{2}{5}$", "$\\frac{3}{5}$", "$\\frac{4}{6}$", "$\\frac{1}{2}$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Gieo hai con xúc xắc. Xác suất để số chấm xuất hiện trên 2 con xúc xắc giống nhau là:", ["$\\frac{1}{6}$", "$\\frac{1}{36}$", "$\\frac{1}{12}$", "$\\frac{5}{36}$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Chọn ngẫu nhiên 2 học sinh từ một nhóm 4 nam và 2 nữ. Số phần tử của không gian mẫu là:", ["$15$", "$12$", "$8$", "$6$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Tung 2 đồng xu. Xác suất để xuất hiện ít nhất một mặt ngửa là:", ["$\\frac{3}{4}$", "$\\frac{1}{4}$", "$\\frac{1}{2}$", "$1$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một hộp có 5 bi xanh và 3 bi đỏ. Lấy ngẫu nhiên 2 viên bi. Xác suất để 2 viên bi cùng màu đỏ là:", ["$\\frac{3}{28}$", "$\\frac{1}{4}$", "$\\frac{3}{8}$", "$\\frac{5}{28}$"], 0)
            ]

            p2 = [
                make_tf(1, "Gieo đồng thời hai con xúc xắc 6 mặt cân đối:", [
                    {"key": "a", "level": "Nhận biết", "text": "Không gian mẫu có 36 kết quả đồng khả năng.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Xác suất để tổng số chấm bằng 7 là 6/36 = 1/6.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Biến cố 'Tổng số chấm nhỏ hơn 13' là biến cố chắc chắn.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Xác suất để ít nhất một con xúc xắc xuất hiện mặt 6 chấm bằng 11/36.", "correct": True}
                ]),
                make_tf(2, "Một lớp học có 25 bạn nam và 20 bạn nữ. Chọn ngẫu nhiên một ban cán sự gồm 2 người:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tổng số học sinh của cả lớp bằng 45 học sinh.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Số cách chọn 2 bạn bất kì là 990 cách.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Số cách chọn 2 bạn đều là nữ bằng 190 cách.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Xác suất để chọn được 1 nam và 1 nữ bằng 50/99 (khoảng 50,5%).", "correct": True}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Tung ba đồng xu cân đối. Không gian mẫu có bao nhiêu phần tử?", "8"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Gieo con xúc xắc. Xác suất để số chấm xuất hiện lớn hơn 2 là bao nhiêu (dạng phân số tối giản a/b)?", "2/3"),
                make_sa(3, "Vận dụng", "Một hộp có 10 viên bi được đánh số từ 1 đến 10. Rút ngẫu nhiên 2 viên bi. Có bao nhiêu cách rút để tổng 2 số ghi trên thẻ là số lẻ?", "25"),
                make_sa(4, "Vận dụng", "Gieo hai con xúc xắc. Xác suất để tích số chấm là một số chẵn bằng bao nhiêu (dạng phân số tối giản)?", "3/4")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Tung hai con xúc xắc cân đối. Tính xác suất của các biến cố sau: a) A: 'Tổng số chấm xuất hiện bằng 8'; b) B: 'Hai con xúc xắc xuất hiện số chấm giống nhau'.", "Không gian mẫu: n(Ω) = 36 (0.25đ). a) Các cặp tổng bằng 8: (2,6), (3,5), (4,4), (5,3), (6,2) gồm 5 cặp. P(A) = 5/36 (0.25đ). b) Các cặp giống nhau: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) gồm 6 cặp. P(B) = 6/36 = 1/6 (0.5đ)."),
                make_essay(2, "Vận dụng", "Một hộp có 4 quả cầu xanh và 6 quả cầu đỏ. Lấy ngẫu nhiên đồng thời 2 quả cầu. Tính xác suất để: a) Cả hai quả đều màu xanh; b) Lấy được ít nhất 1 quả màu đỏ.", "Số cách chọn 2 quả từ 10 quả: C(10,2) = 45 cách (0.25đ). a) Số cách chọn 2 quả xanh: C(4,2) = 6 cách. P = 6/45 = 2/15 (0.25đ). b) Biến cố đối của 'ít nhất 1 quả đỏ' là 'cả 2 quả đều xanh'. P(B) = 1 - 2/15 = 13/15 (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Có ba chiếc hộp: Hộp I đựng 3 bi trắng 2 bi đen; Hộp II đựng 4 bi trắng 1 bi đen; Hộp III đựng 2 bi trắng 3 bi đen. Chọn ngẫu nhiên 1 hộp rồi từ đó rút ngẫu nhiên 1 viên bi. Tính xác suất để viên bi rút được có màu trắng.", "Xác suất chọn mỗi hộp là 1/3 (0.25đ). Xác suất rút bi trắng ở hộp I: 3/5; hộp II: 4/5; hộp III: 2/5 (0.25đ). Áp dụng công thức xác suất toàn phần: P = (1/3)*(3/5) + (1/3)*(4/5) + (1/3)*(2/5) = (1/3)*(9/5) = 3/5 = 0.6 (60%) (0.5đ).")
            ]

            exams[f"c8_9_bai{l_idx}_test{t}"] = {
                "title": f"Toán 9 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(9, "c8_9", "Chương VIII: Xác suất của biến cố trong một số mô hình xác suất đơn giản", exams)

# ==============================================================================
# CHƯƠNG IX TOÁN 9: ĐƯỜNG TRÒN NGOẠI TIẾP VÀ NỘI TIẾP (5 BÀI = 15 ĐỀ)
# ==============================================================================
def generate_c9_toan9():
    print("🚀 Đang biên soạn Chương IX Toán 9: Đường tròn ngoại tiếp và nội tiếp...")
    exams = {}

    lessons = [
        (1, "Bài 27: Góc nội tiếp"),
        (2, "Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác"),
        (3, "Bài 29: Tứ giác nội tiếp"),
        (4, "Bài 30: Đa giác đều"),
        (5, "Bài kiểm tra cuối Chương IX: Đường tròn ngoại tiếp và đường tròn nội tiếp")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Góc có đỉnh nằm trên đường tròn và hai cạnh chứa hai dây cung của đường tròn gọi là:", ["Góc nội tiếp", "Góc ở tâm", "Góc tạo bởi tiếp tuyến và dây cung", "Góc có đỉnh bên ngoài đường tròn"], 0),
                make_mc(2, "Nhận biết", "Số đo của góc nội tiếp bằng:", ["Nửa số đo của cung bị chắn", "Số đo của cung bị chắn", "Gấp đôi số đo cung bị chắn", "$90^\\circ$"], 0),
                make_mc(3, "Nhận biết", "Góc nội tiếp chắn nửa đường tròn là:", ["Góc vuông ($90^\\circ$)", "Góc nhọn", "Góc tù", "Góc bẹt"], 0),
                make_mc(4, "Nhận biết", "Các góc nội tiếp cùng chắn một cung thì:", ["Bằng nhau", "Bù nhau", "Phụ nhau", "Vuông góc"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Một tứ giác nội tiếp được đường tròn khi và chỉ khi:", ["Tổng hai góc đối diện bằng $180^\\circ$", "Hai đường chéo bằng nhau", "Bốn cạnh bằng nhau", "Hai góc kề bù nhau"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Hình nào sau đây LUÔN LUÔN nội tiếp được đường tròn?", ["Hình chữ nhật và hình vuông", "Hình thoi", "Hình bình hành", "Hình thang vuông"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Hình thang cân có nội tiếp được đường tròn không?", ["Luôn nội tiếp được đường tròn", "Không bao giờ", "Chỉ khi là hình vuông", "Tùy thuộc chiều cao"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Góc ở tâm có số đo bằng:", ["Số đo của cung bị chắn", "Nửa số đo cung bị chắn", "Gấp đôi số đo cung bị chắn", "$180^\\circ$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\widehat{ABC}$ nội tiếp $(O)$ chắn cung $AC$ có số đo $80^\\circ$. Số đo góc $\\widehat{ABC}$ là:", ["$40^\\circ$", "$80^\\circ$", "$160^\\circ$", "$20^\\circ$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Tứ giác $ABCD$ nội tiếp đường tròn có $\\widehat{A} = 70^\\circ$. Số đo góc $\\widehat{C}$ là:", ["$110^\\circ$", "$70^\\circ$", "$90^\\circ$", "$120^\\circ$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Bán kính đường tròn ngoại tiếp tam giác đều cạnh $a$ bằng:", ["$\\frac{a\\sqrt{3}}{3}$", "$\\frac{a\\sqrt{3}}{6}$", "$\\frac{a\\sqrt{3}}{2}$", "$a$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Cho tứ giác $ABCD$ nội tiếp $(O)$. Hai tia $AB, DC$ cắt nhau tại $M$. Khẳng định đúng là:", ["$MA \\cdot MB = MC \\cdot MD$", "$MA \\cdot MC = MB \\cdot MD$", "$MA + MB = MC + MD$", "$MA \\cdot MD = MB \\cdot MC$"], 0)
            ]

            p2 = [
                make_tf(1, "Cho tam giác nhọn ABC nội tiếp đường tròn (O; R). Kẻ đường kính AD của đường tròn:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tam giác ABD vuông tại B vì góc ABD chắn nửa đường tròn.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Tam giác ACD vuông tại C.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Hai góc nội tiếp góc ADB và góc ACB bằng nhau vì cùng chắn cung AB.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Đoạn thẳng AB * AC luôn bằng AD nhân với đường cao AH hạ từ A xuống BC.", "correct": True}
                ]),
                make_tf(2, "Cho tứ giác ABCD có góc B = góc D = 90°:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tổng hai góc đối diện góc B + góc D = 180°.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Tứ giác ABCD nội tiếp được trong đường tròn đường kính AC.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Tâm đường tròn ngoại tiếp tứ giác ABCD là trung điểm của đoạn thẳng AC.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu AC = 10 cm thì bán kính đường tròn ngoại tiếp tứ giác ABCD bằng 10 cm.", "correct": False}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Cho góc nội tiếp $\\widehat{ABC}$ có số đo bằng $35^\\circ$. Số đo của cung bị chắn $AC$ bằng bao nhiêu độ?", "70"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Tứ giác $ABCD$ nội tiếp có $\\widehat{B} = 105^\\circ$. Tính số đo góc $\\widehat{D}$ (độ):", "75"),
                make_sa(3, "Vận dụng", "Tính bán kính đường tròn ngoại tiếp tam giác vuông có hai cạnh góc vuông là $6\\text{ cm}$ và $8\\text{ cm}$:", "5"),
                make_sa(4, "Vận dụng", "Cho đa giác đều 12 cạnh nội tiếp đường tròn $(O)$. Góc ở tâm chắn một cạnh của đa giác đều bằng bao nhiêu độ?", "30")
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Cho đường tròn $(O)$ và dây $AB$. Từ điểm $C$ trên cung lớn $AB$, kẻ các dây $CA, CB$. Biết góc ở tâm $\\widehat{AOB} = 100^\\circ$. Tính số đo cung nhỏ $AB$ và số đo góc nội tiếp $\\widehat{ACB}$.", "Số đo cung nhỏ AB bằng góc ở tâm AOB = 100° (0.5đ). Góc nội tiếp ACB chắn cung nhỏ AB nên góc ACB = 1/2 sđ AB = 1/2 * 100° = 50° (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác nhọn $ABC$, các đường cao $BD$ và $CE$ cắt nhau tại $H$. Chứng minh rằng: a) Tứ giác $ADHE$ nội tiếp được đường tròn; b) Tứ giác $BEDC$ nội tiếp được đường tròn.", "a) Xét tứ giác ADHE có góc ADH = 90° và góc AEH = 90°. Tổng hai góc đối diện: góc ADH + góc AEH = 180° nên ADHE nội tiếp đường tròn đường kính AH (0.5đ). b) Xét tứ giác BEDC có hai đỉnh D và E cùng nhìn đoạn BC dưới một góc vuông 90° nên BEDC nội tiếp đường tròn đường kính BC (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho đường tròn $(O; R)$ và dây $BC$ cố định ($BC < 2R$). Điểm $A$ di động trên cung lớn $BC$. Chứng minh rằng trực tâm $H$ của tam giác $ABC$ luôn cách điểm $O$ một khoảng không đổi khi $A$ di chuyển.", "Kẻ đường kính CD. Chứng minh tứ giác AHBD là hình bình hành suy ra AH = BD = 2OM (với M là trung điểm BC) (0.5đ). Vì BC cố định nên OM không đổi, suy ra độ dài AH không đổi. Dẫn đến điểm H luôn nằm trên một đường tròn cố định (0.5đ).")
            ]

            exams[f"c9_9_bai{l_idx}_test{t}"] = {
                "title": f"Toán 9 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(9, "c9_9", "Chương IX: Đường tròn ngoại tiếp và đường tròn nội tiếp", exams)

# ==============================================================================
# CHƯƠNG X TOÁN 9: MỘT SỐ HÌNH KHỐI TRONG THỰC TIỄN (3 BÀI = 9 ĐỀ)
# ==============================================================================
def generate_c10_toan9():
    print("🚀 Đang biên soạn Chương X Toán 9: Một số hình khối trong thực tiễn...")
    exams = {}

    lessons = [
        (1, "Bài 31: Hình trụ và hình nón"),
        (2, "Bài 32: Hình cầu"),
        (3, "Bài kiểm tra cuối Chương X: Một số hình khối trong thực tiễn")
    ]

    for (l_idx, l_name) in lessons:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"

            p1 = [
                make_mc(1, "Nhận biết", "Công thức tính diện tích xung quanh của hình trụ có bán kính đáy $R$ và chiều cao $h$ là:", ["$S_{xq} = 2\\pi R h$", "$S_{xq} = \\pi R h$", "$S_{xq} = \\pi R^2 h$", "$S_{xq} = 2\\pi R^2$"], 0),
                make_mc(2, "Nhận biết", "Thể tích của hình trụ có bán kính đáy $R$ và chiều cao $h$ bằng:", ["$V = \\pi R^2 h$", "$V = \\frac{1}{3}\\pi R^2 h$", "$V = 2\\pi R h$", "$V = \\frac{4}{3}\\pi R^3$"], 0),
                make_mc(3, "Nhận biết", "Công thức tính diện tích xung quanh của hình nón có bán kính đáy $R$ và đường sinh $l$ là:", ["$S_{xq} = \\pi R l$", "$S_{xq} = 2\\pi R l$", "$S_{xq} = \\pi R^2 l$", "$S_{xq} = \\frac{1}{3}\\pi R l$"], 0),
                make_mc(4, "Nhận biết", "Thể tích của hình nón có bán kính đáy $R$ và chiều cao $h$ bằng:", ["$V = \\frac{1}{3}\\pi R^2 h$", "$V = \\pi R^2 h$", "$V = \\frac{4}{3}\\pi R^3$", "$V = \\pi R h$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Diện tích mặt cầu bán kính $R$ bằng:", ["$S = 4\\pi R^2$", "$S = \\frac{4}{3}\\pi R^3$", "$S = 2\\pi R^2$", "$S = \\pi R^2$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Thể tích hình cầu bán kính $R$ bằng:", ["$V = \\frac{4}{3}\\pi R^3$", "$V = 4\\pi R^2$", "$V = \\frac{1}{3}\\pi R^3$", "$V = \\pi R^3$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Mối liên hệ giữa đường sinh $l$, chiều cao $h$ và bán kính đáy $R$ của hình nón là:", ["$l^2 = h^2 + R^2$", "$l = h + R$", "$h^2 = l^2 + R^2$", "$R^2 = l^2 + h^2$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Khi quay một tam giác vuông quanh một cạnh góc vuông cố định thì hình tạo thành là:", ["Hình nón", "Hình trụ", "Hình cầu", "Hình lăng trụ"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Một lon nước ngọt hình trụ có bán kính đáy $3\\text{ cm}$ và chiều cao $10\\text{ cm}$. Thể tích của lon là:", ["$90\\pi\\text{ cm}^3$", "$30\\pi\\text{ cm}^3$", "$60\\pi\\text{ cm}^3$", "$180\\pi\\text{ cm}^3$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Một chiếc nón lá có bán kính đáy $20\\text{ cm}$, đường sinh $30\\text{ cm}$. Diện tích xung quanh chiếc nón là:", ["$600\\pi\\text{ cm}^2$", "$1200\\pi\\text{ cm}^2$", "$300\\pi\\text{ cm}^2$", "$400\\pi\\text{ cm}^2$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Một quả bóng đá có đường kính $22\\text{ cm}$. Bán kính của quả bóng là:", ["$11\\text{ cm}$", "$22\\text{ cm}$", "$5.5\\text{ cm}$", "$44\\text{ cm}$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Nếu tăng bán kính của hình cầu lên gấp 2 lần thì thể tích của nó tăng lên gấp:", ["$8$ lần", "$2$ lần", "$4$ lần", "$6$ lần"], 0)
            ]

            p2 = [
                make_tf(1, "Một thùng nước hình trụ có bán kính đáy R = 0,5 m và chiều cao h = 1,2 m:", [
                    {"key": "a", "level": "Nhận biết", "text": "Diện tích đáy của thùng nước bằng π * R² = 0,25π m².", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Diện tích xung quanh của thùng nước là Sxq = 2π * 0,5 * 1,2 = 1,2π m².", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Thể tích của thùng nước là V = π * 0,5² * 1,2 = 0,3π m³ (khoảng 942 lít).", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu mực nước đang sâu 0,8 m thì lượng nước hiện có trong thùng là 628 lít (lấy π ≈ 3,14).", "correct": True}
                ]),
                make_tf(2, "Một chiếc nón hình nón có chiều cao h = 12 cm và bán kính đáy R = 5 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Độ dài đường sinh l = √(12² + 5²) = 13 cm.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Diện tích xung quanh của hình nón bằng π * 5 * 13 = 65π cm².", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Thể tích của hình nón bằng 1/3 * π * 5² * 12 = 100π cm³.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Diện tích toàn phần của hình nón nhỏ hơn 80π cm².", "correct": False}
                ])
            ]

            p3 = [
                make_sa(1, "Thông hiểu", "Một hình trụ có bán kính đáy $R = 4\\text{ cm}$ và chiều cao $h = 5\\text{ cm}$. Tính diện tích xung quanh (kết quả theo số nguyên nhân $\\pi$, chỉ điền hệ số nguyên):", "40"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Tính thể tích của hình nón có bán kính đáy $R = 3\\text{ cm}$ và chiều cao $h = 4\\text{ cm}$ (kết quả theo $\\pi$, chỉ điền hệ số nguyên):", "12"),
                make_sa(3, "Vận dụng", "Một quả bóng bàn hình cầu có đường kính $4\\text{ cm}$. Diện tích bề mặt của quả bóng bằng bao nhiêu $\\text{cm}^2$ (kết quả theo $\\pi$, chỉ điền hệ số nguyên)?", "16"),
                make_sa(4, "Vận dụng", "Một chiếc ly dạng hình nón chứa đầy nước có bán kính miệng ly $6\\text{ cm}$, chiều cao $10\\text{ cm}$. Rót toàn bộ nước từ ly sang một cốc hình trụ có cùng bán kính đáy $6\\text{ cm}$. Chiều cao mực nước trong cốc hình trụ là bao nhiêu cm (dạng số thập phân hoặc phân số)?", "3.33", acceptable=["3.33", "3.3", "10/3", "3,33"])
            ]

            p4 = [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một hộp sữa đặc hình trụ có đường kính đáy $7\\text{ cm}$ và chiều cao $8\\text{ cm}$. a) Tính diện tích giấy nhãn bao quanh thân hộp sữa (không tính mép dán); b) Tính thể tích hộp sữa (lấy $\\pi \\approx 3,14$, làm tròn 1 chữ số thập phân).", "Bán kính đáy: R = 3.5 cm (0.25đ). a) Diện tích giấy nhãn xung quanh: Sxq = 2π * 3.5 * 8 = 56π ≈ 175.8 cm² (0.25đ). b) Thể tích hộp sữa: V = π * 3.5² * 8 = 98π ≈ 307.7 cm³ (0.5đ)."),
                make_essay(2, "Vận dụng", "Một chiếc nón lá bài thơ có đường kính đáy $40\\text{ cm}$, chiều cao $30\\text{ cm}$. Người ta dán lá lên mặt ngoài của nón. Tính diện tích lá cần dùng (lấy $\\pi \\approx 3,14$).", "Bán kính đáy: R = 20 cm. Đường sinh l = √(h² + R²) = √(30² + 20²) = √1300 ≈ 36.06 cm (0.5đ). Diện tích lá cần dùng bằng diện tích xung quanh: Sxq = π * R * l ≈ 3.14 * 20 * 36.06 ≈ 2264.6 cm² (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Một bể chứa nước có dạng gồm một phần hình trụ ở dưới (chiều cao $2\\text{ m}$, bán kính đáy $1\\text{ m}$) và một phần bán cầu ở trên (cùng bán kính $1\\text{ m}$). Tính thể tích nước tối đa mà bể có thể chứa được (lấy $\\pi \\approx 3,14$, làm tròn 2 chữ số thập phân).", "Thể tích phần hình trụ: V1 = π * R² * h = π * 1² * 2 = 2π m³ (0.25đ). Thể tích phần bán cầu: V2 = 1/2 * (4/3 π R³) = 2/3 π * 1³ = 2/3 π m³ (0.25đ). Tổng thể tích bể: V = V1 + V2 = (2 + 2/3)π = 8/3 π ≈ 8.38 m³ (khoảng 8380 lít nước) (0.5đ).")
            ]

            exams[f"c10_9_bai{l_idx}_test{t}"] = {
                "title": f"Toán 9 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    save_chapter_package(9, "c10_9", "Chương X: Một số hình khối trong thực tiễn", exams)

if __name__ == "__main__":
    generate_c5_toan9()
    generate_c6_toan9()
    generate_c7_toan9()
    generate_c8_toan9()
    generate_c9_toan9()
    generate_c10_toan9()
    print("🎉 TOÀN BỘ CHƯƠNG V, VI, VII, VIII, IX, X TOÁN 9 ĐÃ ĐƯỢC TẠO VÀ ĐÓNG GÓI XUẤT SẮC!")
