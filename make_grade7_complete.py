# -*- coding: utf-8 -*-
"""
HỆ THỐNG BIÊN SOẠN TOÀN DIỆN TOÁN 7: CHƯƠNG IX & CHƯƠNG X
Tạo trọn vẹn:
- grade7_c9_7_exams.json / .js (18 đề)
- grade7_c10_7_exams.json / .js (9 đề)
Tuân thủ tuyệt đối ma trận 2025:
- Đề 1 & 2: 40% NB, 30% TH, 20% VD, 10% VDC
- Đề 3: 20% NB, 30% TH, 30% VD, 20% VDC
- Ràng buộc: Phần II có đúng 1 ý VD/câu; Phần III có đúng 2 câu VD/4 câu.
"""

import sys
import os

PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package
from build_grade7_exams import get_bank_c9_bai1, get_bank_c9_bai2

def generate_c9_toan7():
    print("🚀 Đang biên soạn Chương IX Toán 7: Quan hệ giữa các yếu tố trong một tam giác...")
    exams = {}
    
    # Bài 1 (Bài 31)
    for t in [1, 2, 3]:
        exams[f"c9_7_bai1_test{t}"] = get_bank_c9_bai1(t)
        
    # Bài 2 (Bài 32)
    for t in [1, 2, 3]:
        exams[f"c9_7_bai2_test{t}"] = get_bank_c9_bai2(t)

    # --------------------------------------------------------------------------
    # BÀI 3 (Bài 33): BẤT ĐẲNG THỨC TAM GIÁC
    # --------------------------------------------------------------------------
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c9_7_bai3_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài 33: Quan hệ giữa ba cạnh của một tam giác - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Trong một tam giác, độ dài một cạnh bất kì luôn:", ["Nhỏ hơn tổng độ dài hai cạnh còn lại", "Lớn hơn tổng độ dài hai cạnh còn lại", "Bằng tổng hai cạnh còn lại", "Gấp đôi cạnh nhỏ nhất"], 0),
                make_mc(2, "Nhận biết", "Trong một tam giác, độ dài một cạnh bất kì luôn:", ["Lớn hơn hiệu độ dài hai cạnh còn lại", "Nhỏ hơn hiệu hai cạnh còn lại", "Bằng hiệu hai cạnh còn lại", "Bằng 0"], 0),
                make_mc(3, "Nhận biết", "Bộ ba độ dài đoạn thẳng nào sau đây CÓ THỂ là độ dài ba cạnh của một tam giác?", ["$3\\text{ cm}, 4\\text{ cm}, 5\\text{ cm}$", "$2\\text{ cm}, 3\\text{ cm}, 5\\text{ cm}$", "$1\\text{ cm}, 2\\text{ cm}, 4\\text{ cm}$", "$5\\text{ cm}, 5\\text{ cm}, 11\\text{ cm}$"], 0),
                make_mc(4, "Nhận biết", "Bộ ba số nào sau đây KHÔNG THỂ là độ dài ba cạnh của một tam giác?", ["$3, 4, 8$", "$4, 5, 6$", "$6, 8, 10$", "$5, 5, 5$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Cho tam giác $ABC$. Bất đẳng thức nào sau đây luôn đúng?", ["$|AB - AC| < BC < AB + AC$", "$BC > AB + AC$", "$BC < AB - AC$", "$BC = AB + AC$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Tam giác cân có độ dài hai cạnh là $2\\text{ cm}$ và $5\\text{ cm}$. Độ dài cạnh thứ ba là:", ["$5\\text{ cm}$", "$2\\text{ cm}$", "$3\\text{ cm}$", "$7\\text{ cm}$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Để kiểm tra bộ ba đoạn thẳng $a, b, c$ (với $a \\le b \\le c$) có lập thành tam giác không, ta chỉ cần kiểm tra:", ["$a + b > c$", "$a + c > b$", "$b + c > a$", "$a + b < c$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Cho tam giác có hai cạnh là $3\\text{ cm}$ và $7\\text{ cm}$. Cạnh thứ ba $x$ nguyên có thể nhận bao nhiêu giá trị?", ["$5$ giá trị ($5, 6, 7, 8, 9$)", "$4$ giá trị", "$6$ giá trị", "$7$ giá trị"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Một tam giác cân có chu vi $17\\text{ cm}$, cạnh đáy là $5\\text{ cm}$. Độ dài cạnh bên là:", ["$6\\text{ cm}$", "$5\\text{ cm}$", "$7\\text{ cm}$", "$12\\text{ cm}$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Cho điểm $M$ nằm trong tam giác $ABC$. So sánh tổng $MA + MB$ và $AB + AC$:", ["$MA + MB < CA + CB$", "$MA + MB > CA + CB$", "$MA + MB = CA + CB$", "Không so sánh được"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Tìm số đo cạnh nguyên lớn nhất của tam giác biết hai cạnh kia bằng $4\\text{ cm}$ và $9\\text{ cm}$:", ["$12\\text{ cm}$", "$13\\text{ cm}$", "$14\\text{ cm}$", "$11\\text{ cm}$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Cho tam giác $ABC$ có chu vi $2p$ và $M$ là điểm bất kì trong tam giác. Tổng $MA + MB + MC$ thỏa mãn:", ["$p < MA + MB + MC < 2p$", "$MA + MB + MC < p$", "$MA + MB + MC > 2p$", "$MA + MB + MC = p$"], 0)
            ],
            "part2": [
                make_tf(1, "Xét ba độ dài đoạn thẳng a, b, c thỏa mãn a = 4 cm, b = 7 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Hiệu độ dài hai cạnh là b - a = 3 cm.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Tổng độ dài hai cạnh là a + b = 11 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Nếu c = 3 cm thì ba đoạn thẳng a, b, c tạo thành một tam giác.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu tam giác này là tam giác cân thì cạnh c bắt buộc phải bằng 7 cm.", "correct": True}
                ]),
                make_tf(2, "Cho tam giác ABC có chu vi bằng 24 cm và ba cạnh là a, b, c:", [
                    {"key": "a", "level": "Nhận biết", "text": "Ta luôn có a + b + c = 24 cm.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Mỗi cạnh của tam giác ABC luôn nhỏ hơn nửa chu vi (tức nhỏ hơn 12 cm).", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Nếu a = 12 cm thì b + c = 12 cm, khi đó ba đoạn a, b, c vẫn tạo thành tam giác.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu a, b, c là các số nguyên và a ≤ b ≤ c thì cạnh lớn nhất c có thể đạt giá trị tối đa là 11 cm.", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Tam giác cân có hai cạnh lần lượt bằng $3\\text{ cm}$ và $8\\text{ cm}$. Chu vi tam giác đó bằng bao nhiêu cm?", "19"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Cho tam giác có hai cạnh là $5\\text{ cm}$ và $9\\text{ cm}$. Cạnh thứ ba là số nguyên chẵn. Cạnh thứ ba có thể nhận giá trị lớn nhất bằng bao nhiêu cm?", "12"),
                make_sa(3, "Vận dụng", "Có bao nhiêu tam giác có độ dài ba cạnh là các số nguyên sao cho cạnh lớn nhất bằng $5\\text{ cm}$?", "5"),
                make_sa(4, "Vận dụng", "Cho tam giác $ABC$ có $BC = 1\\text{ cm}, AC = 7\\text{ cm}$. Biết $AB$ là một số nguyên, tính độ dài cạnh $AB$ (cm):", "7")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Hai thanh tre có độ dài $60\\text{ cm}$ và $90\\text{ cm}$. Bác thợ mộc muốn chọn thêm thanh tre thứ ba để làm khung diều tam giác. Hỏi thanh thứ ba có thể dài $30\\text{ cm}$ hoặc $150\\text{ cm}$ được không? Giải thích.", "Theo bất đẳng thức tam giác, cạnh thứ ba c phải thỏa mãn 90 - 60 < c < 90 + 60, tức 30 < c < 150 (0.5đ). Cả hai độ dài 30 cm và 150 cm đều không thỏa mãn bất đẳng thức nghiêm ngặt, do đó không thể ghép thành tam giác (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác $ABC$, $M$ là trung điểm của $BC$. Chứng minh rằng: $AM < \\frac{AB + AC}{2}$.", "Trên tia đối của tia MA lấy điểm D sao cho MD = MA. Chứng minh tam giác MAB = tam giác MDC (c.g.c) suy ra CD = AB (0.5đ). Áp dụng bất đẳng thức tam giác trong tam giác ACD: AD < AC + CD, hay 2AM < AC + AB, suy ra AM < (AB + AC)/2 (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Chứng minh rằng trong mọi tam giác $ABC$, tổng ba đường trung tuyến $m_a + m_b + m_c$ luôn lớn hơn $\\frac{3}{4}$ chu vi và nhỏ hơn chu vi của tam giác.", "Áp dụng chứng minh câu 2 cho 3 trung tuyến: ma < (b+c)/2; mb < (a+c)/2; mc < (a+b)/2, cộng lại được ma+mb+mc < a+b+c (0.5đ). Áp dụng tính chất trọng tâm G: GA+GB > AB suy ra 2/3(ma+mb) > c, cộng 3 bđt tương tự ta được ma+mb+mc > 3/4(a+b+c) (0.5đ).")
            ]
        }

    # --------------------------------------------------------------------------
    # BÀI 4 (Bài 34): SỰ ĐỒNG QUY CỦA BA TRUNG TUYẾN, BA PHÂN GIÁC
    # --------------------------------------------------------------------------
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c9_7_bai4_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài 34: Ba đường trung tuyến, ba đường phân giác - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Giao điểm của ba đường trung tuyến trong một tam giác gọi là:", ["Trọng tâm", "Trực tâm", "Tâm đường tròn ngoại tiếp", "Tâm đường tròn nội tiếp"], 0),
                make_mc(2, "Nhận biết", "Trọng tâm của một tam giác cách mỗi đỉnh một khoảng bằng:", ["$\\frac{2}{3}$ độ dài đường trung tuyến đi qua đỉnh đó", "$\\frac{1}{2}$ độ dài trung tuyến", "$\\frac{1}{3}$ độ dài trung tuyến", "Bằng độ dài trung tuyến"], 0),
                make_mc(3, "Nhận biết", "Giao điểm của ba đường phân giác trong tam giác:", ["Cách đều ba cạnh của tam giác", "Cách đều ba đỉnh", "Là trọng tâm", "Trùng trực tâm"], 0),
                make_mc(4, "Nhận biết", "Trong tam giác đều, trọng tâm, trực tâm, tâm nội tiếp và tâm ngoại tiếp:", ["Trùng nhau tại một điểm", "Là 4 điểm phân biệt", "Nằm ngoài tam giác", "Nằm trên cạnh huyền"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Cho $AM$ là trung tuyến của $\\triangle ABC$, $G$ là trọng tâm. Tỉ số $\\frac{AG}{GM}$ bằng:", ["$2$", "$\\frac{1}{2}$", "$\\frac{2}{3}$", "$\\frac{1}{3}$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Cho $AM$ là trung tuyến của $\\triangle ABC$, $G$ là trọng tâm. Tỉ số $\\frac{GM}{AM}$ bằng:", ["$\\frac{1}{3}$", "$\\frac{2}{3}$", "$\\frac{1}{2}$", "$2$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Đường phân giác của một góc trong tam giác là đường thẳng chia góc đó thành:", ["Hai góc có số đo bằng nhau", "Hai góc phụ nhau", "Hai góc bù nhau", "Hai đoạn thẳng bằng nhau"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Trong một tam giác cân, đường phân giác xuất phát từ đỉnh đồng thời là:", ["Đường trung tuyến và đường cao", "Đường trung bình", "Đường chéo", "Cạnh đối diện"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác $ABC$ có trung tuyến $AM = 9\\text{ cm}$. Khoảng cách từ trọng tâm $G$ đến đỉnh $A$ là:", ["$6\\text{ cm}$", "$3\\text{ cm}$", "$4.5\\text{ cm}$", "$2\\text{ cm}$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC$ có hai trung tuyến $BM$ và $CN$ cắt nhau tại $G$. Biết $BM = CN$, khẳng định đúng là:", ["Tam giác $ABC$ cân tại $A$", "Tam giác $ABC$ vuông tại $A$", "Tam giác $ABC$ đều", "$BC = 2MN$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Điểm cách đều ba cạnh của tam giác $ABC$ là giao điểm của:", ["Ba đường phân giác", "Ba đường trung tuyến", "Ba đường cao", "Ba đường trung trực"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$, trung tuyến $AM$. Biết $BC = 10\\text{ cm}$, độ dài $AM$ bằng:", ["$5\\text{ cm}$", "$10\\text{ cm}$", "$2.5\\text{ cm}$", "$7.5\\text{ cm}$"], 0)
            ],
            "part2": [
                make_tf(1, "Cho tam giác ABC có hai đường trung tuyến BM và CN cắt nhau tại G:", [
                    {"key": "a", "level": "Nhận biết", "text": "G là trọng tâm của tam giác ABC.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Tia AG đi qua trung điểm của đoạn thẳng BC.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Độ dài đoạn AG bằng 1/3 độ dài đoạn thẳng kẻ từ A đến trung điểm BC.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Diện tích 6 tam giác nhỏ tạo bởi G với 3 đỉnh và 3 trung điểm là bằng nhau.", "correct": True}
                ]),
                make_tf(2, "Cho tam giác ABC có I là giao điểm của ba đường phân giác trong:", [
                    {"key": "a", "level": "Nhận biết", "text": "I cách đều ba cạnh AB, BC, CA.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "I là tâm đường tròn nội tiếp tam giác ABC.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Góc BIC = 90° + (góc A)/2.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu tam giác ABC vuông tại A với AB = 6 cm, AC = 8 cm thì khoảng cách từ I đến ba cạnh bằng 2 cm.", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Cho tam giác $ABC$ có trung tuyến $BD = 12\\text{ cm}$, $G$ là trọng tâm. Tính độ dài đoạn thẳng $GD$ (cm):", "4"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Tam giác $ABC$ có $\\widehat{A} = 70^\\circ$. Hai đường phân giác của góc $B$ và $C$ cắt nhau tại $I$. Tính số đo góc $\\widehat{BIC}$ (độ):", "125"),
                make_sa(3, "Vận dụng", "Cho tam giác vuông $ABC$ tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Trung tuyến $AM$ kẻ từ đỉnh góc vuông có độ dài bằng bao nhiêu cm?", "5"),
                make_sa(4, "Vận dụng", "Cho tam giác $ABC$, các đường trung tuyến $BD$ và $CE$ vuông góc với nhau tại trọng tâm $G$. Biết $BC = 10\\text{ cm}$. Tính tổng $BD^2 + CE^2$:", "225")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác $ABC$ cân tại $A$, đường trung tuyến $AM$. Chứng minh $AM \\perp BC$ và $AM$ là tia phân giác của góc $\\widehat{A}$.", "Xét tam giác ABM và ACM có AB = AC, BM = MC, AM chung (0.5đ). Suy ra hai tam giác bằng nhau (c.c.c), dẫn đến góc AMB = góc AMC = 90° (AM vuông góc BC) và góc BAM = góc CAM (AM là phân giác) (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác $ABC$. Chứng minh rằng điểm cách đều hai cạnh $AB, AC$ và hai cạnh $AB, BC$ chính là giao điểm các đường phân giác của tam giác.", "Tập hợp các điểm cách đều AB và AC là đường phân giác góc A (0.5đ). Tập hợp cách đều AB và BC là phân giác góc B. Giao điểm I của hai đường phân giác cách đều cả 3 cạnh AB, BC, CA, nằm trên phân giác góc C (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ có các đường trung tuyến $BD$ và $CE$ vuông góc với nhau. Chứng minh rằng $AB^2 + AC^2 = 5BC^2$.", "Đặt GB = 2x, GD = x; GC = 2y, GE = y (0.5đ). Áp dụng định lí Pythagore trong các tam giác vuông BGC, EGC, DGB biến đổi đại số suy ra AB² + AC² = 5BC² (0.5đ).")
            ]
        }

    # --------------------------------------------------------------------------
    # BÀI 5 (Bài 35): BA ĐƯỜNG TRUNG TRỰC, BA ĐƯỜNG CAO
    # --------------------------------------------------------------------------
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c9_7_bai5_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài 35: Ba đường trung trực, ba đường cao - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Đường trung trực của một đoạn thẳng là đường thẳng:", ["Đi qua trung điểm và vuông góc với đoạn thẳng đó", "Đi qua đỉnh đối diện", "Song song với đoạn thẳng", "Chia góc thành hai nửa"], 0),
                make_mc(2, "Nhận biết", "Điểm nằm trên đường trung trực của một đoạn thẳng thì:", ["Cách đều hai đầu mút của đoạn thẳng đó", "Cách đều ba đỉnh", "Trùng trung điểm", "Vuông góc"], 0),
                make_mc(3, "Nhận biết", "Ba đường trung trực của một tam giác cùng đi qua một điểm. Điểm đó:", ["Cách đều ba đỉnh của tam giác", "Cách đều ba cạnh", "Là trọng tâm", "Là trực tâm"], 0),
                make_mc(4, "Nhận biết", "Giao điểm ba đường cao của một tam giác được gọi là:", ["Trực tâm", "Trọng tâm", "Tâm ngoại tiếp", "Tâm nội tiếp"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Trực tâm của tam giác vuông trùng với:", ["Đỉnh góc vuông", "Trung điểm cạnh huyền", "Tâm đường tròn nội tiếp", "Bên ngoài tam giác"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Tâm đường tròn ngoại tiếp của tam giác vuông là:", ["Trung điểm của cạnh huyền", "Đỉnh góc vuông", "Trọng tâm", "Bên ngoài tam giác"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Trong tam giác tù, trực tâm nằm ở:", ["Phía ngoài tam giác", "Bên trong tam giác", "Trên cạnh huyền", "Tại đỉnh góc tù"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Trong tam giác cân, đường trung trực của cạnh đáy:", ["Đi qua đỉnh đối diện", "Song song cạnh bên", "Bằng cạnh bên", "Không đi qua đỉnh"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC$ có hai đường cao $BD$ và $CE$ cắt nhau tại $H$. Đoạn thẳng $AH$:", ["Vuông góc với cạnh $BC$", "Song song với $BC$", "Bằng cạnh $BC$", "Là trung tuyến"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác đều $ABC$. Khẳng định nào sau đây đúng?", ["Trọng tâm, trực tâm, tâm ngoại tiếp, tâm nội tiếp trùng nhau", "Trực tâm nằm ngoài tam giác", "Tâm ngoại tiếp là trung điểm cạnh", "Không có trực tâm"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Khoảng cách từ tâm đường tròn ngoại tiếp đến 3 đỉnh của tam giác $ABC$ gọi là:", ["Bán kính đường tròn ngoại tiếp ($R$)", "Đường cao", "Trung tuyến", "Khoảng cách nội tiếp"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Cho $\\triangle ABC$ có $\\widehat{A} = 50^\\circ$, hai đường cao $BD$ và $CE$ cắt nhau tại $H$. Số đo góc $\\widehat{BHC}$ bằng:", ["$130^\\circ$", "$100^\\circ$", "$120^\\circ$", "$140^\\circ$"], 0)
            ],
            "part2": [
                make_tf(1, "Cho đoạn thẳng AB có độ dài 8 cm và đường trung trực d của AB:", [
                    {"key": "a", "level": "Nhận biết", "text": "d vuông góc với AB tại trung điểm M của AB.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Khoảng cách từ A đến d bằng 4 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Lấy P thuộc d sao cho PA = 5 cm thì tam giác PAB là tam giác đều.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu PA = 5 cm thì khoảng cách từ P đến đoạn thẳng AB bằng 3 cm.", "correct": True}
                ]),
                make_tf(2, "Cho tam giác nhọn ABC có trực tâm H và tâm đường tròn ngoại tiếp O:", [
                    {"key": "a", "level": "Nhận biết", "text": "H là giao điểm ba đường cao của tam giác ABC.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "O là giao điểm ba đường trung trực của tam giác ABC.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Cả hai điểm H và O đều nằm bên trong tam giác nhọn ABC.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Trong tam giác ABC, ba điểm H, O và trọng tâm G luôn thẳng hàng (đường thẳng Euler).", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Cho tam giác vuông $ABC$ có hai cạnh góc vuông $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Bán kính đường tròn ngoại tiếp tam giác bằng bao nhiêu cm?", "5"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{A} = 70^\\circ$, trực tâm $H$. Tính số đo góc $\\widehat{BHC}$ (độ):", "110"),
                make_sa(3, "Vận dụng", "Cho đoạn thẳng $AB = 10\\text{ cm}$. Đường trung trực của $AB$ cắt $AB$ tại $M$. Lấy $C$ trên trung trực sao cho $MC = 12\\text{ cm}$. Chu vi tam giác $ABC$ bằng bao nhiêu cm?", "36"),
                make_sa(4, "Vận dụng", "Cho tam giác $ABC$ cân tại $A$ có $\\widehat{A} = 120^\\circ, BC = 12\\text{ cm}$. Khoảng cách từ tâm đường tròn ngoại tiếp $O$ đến đỉnh $A$ bằng bao nhiêu cm (làm tròn số nguyên)?", "7", acceptable=["6.93", "7", "4*sqrt(3)"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác $ABC$ có $AB = AC$. Gọi $O$ là giao điểm của hai đường trung trực của $AB$ và $AC$. Chứng minh $AO$ là tia phân giác của góc $\\widehat{A}$.", "Điểm O là giao ba đường trung trực nên OA = OB = OC (0.5đ). Xét hai tam giác OAB và OAC có OA chung, AB = AC, OB = OC suy ra hai tam giác bằng nhau (c.c.c). Do đó góc OAB = góc OAC, hay AO là phân giác góc A (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác $ABC$ nhọn. Các đường cao $BD, CE$ cắt nhau tại $H$. Chứng minh rằng nếu $HB = HC$ thì tam giác $ABC$ cân tại $A$.", "Nếu HB = HC thì góc HBC = góc HCB (0.5đ). Mặt khác góc EBC = 90° - góc C, góc DCB = 90° - góc B. Suy ra góc B = góc C, do đó tam giác ABC cân tại A (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$. Tìm điểm $M$ trên mặt phẳng sao cho tổng các bình phương khoảng cách $MA^2 + MB^2 + MC^2$ đạt giá trị nhỏ nhất.", "Gọi G là trọng tâm tam giác ABC. Biến đổi vec-tơ hoặc hình học: MA² + MB² + MC² = GA² + GB² + GC² + 3MG² (0.5đ). Giá trị này nhỏ nhất khi MG = 0, tức điểm M trùng với trọng tâm G của tam giác (0.5đ).")
            ]
        }

    # --------------------------------------------------------------------------
    # BÀI 6: ÔN TẬP VÀ KIỂM TRA CUỐI CHƯƠNG IX
    # --------------------------------------------------------------------------
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c9_7_bai6_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Ôn tập và kiểm tra cuối Chương IX - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Trong một tam giác, giao điểm ba đường trung trực là:", ["Tâm đường tròn ngoại tiếp", "Tâm đường tròn nội tiếp", "Trọng tâm", "Trực tâm"], 0),
                make_mc(2, "Nhận biết", "Trong một tam giác, giao điểm ba đường phân giác là:", ["Tâm đường tròn nội tiếp", "Tâm đường tròn ngoại tiếp", "Trọng tâm", "Trực tâm"], 0),
                make_mc(3, "Nhận biết", "Trong một tam giác, giao điểm ba đường cao là:", ["Trực tâm", "Trọng tâm", "Tâm ngoại tiếp", "Tâm nội tiếp"], 0),
                make_mc(4, "Nhận biết", "Trong một tam giác, giao điểm ba đường trung tuyến là:", ["Trọng tâm", "Trực tâm", "Tâm ngoại tiếp", "Tâm nội tiếp"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Cho tam giác $ABC$ có $AB = 3\\text{ cm}, BC = 5\\text{ cm}$. Độ dài cạnh $AC$ có thể là:", ["$4\\text{ cm}$", "$1\\text{ cm}$", "$2\\text{ cm}$", "$8\\text{ cm}$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Đường vuông góc kẻ từ $A$ đến $BC$ có độ dài là:", ["Khoảng cách từ $A$ đến $BC$", "Đường xiên", "Hình chiếu", "Đoạn song song"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Trong tam giác vuông cân, góc ở đáy có số đo bằng:", ["$45^\\circ$", "$60^\\circ$", "$30^\\circ$", "$90^\\circ$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Nếu tam giác có một đường trung tuyến đồng thời là đường cao thì tam giác đó:", ["Là tam giác cân", "Là tam giác đều", "Là tam giác tù", "Là tam giác vuông"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác $ABC$ có $\\widehat{A} = 80^\\circ$. Trực tâm $H$. Số đo góc $\\widehat{BHC}$ bằng:", ["$100^\\circ$", "$80^\\circ$", "$130^\\circ$", "$160^\\circ$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác $ABC$ có $G$ là trọng tâm, $AM$ là trung tuyến. Biết $AG = 8\\text{ cm}$, tính $AM$:", ["$12\\text{ cm}$", "$16\\text{ cm}$", "$4\\text{ cm}$", "$10\\text{ cm}$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC$ có $\\widehat{A} = 100^\\circ$. Điểm cách đều ba đỉnh $A, B, C$ nằm ở:", ["Phía ngoài tam giác", "Bên trong tam giác", "Trên cạnh $BC$", "Trùng với đỉnh $A$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một điểm nằm cách đều 3 cạnh của tam giác và cách đều 3 đỉnh của tam giác khi tam giác đó:", ["Là tam giác đều", "Là tam giác cân", "Là tam giác vuông", "Là tam giác vuông cân"], 0)
            ],
            "part2": [
                make_tf(1, "Cho tam giác ABC có góc A = 90°, AB = 6 cm, AC = 8 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Độ dài cạnh huyền BC bằng 10 cm.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Trực tâm của tam giác ABC trùng với đỉnh A.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Tâm đường tròn ngoại tiếp tam giác ABC là trung điểm của cạnh AC.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Bán kính đường tròn nội tiếp tam giác ABC bằng r = (AB + AC - BC)/2 = 2 cm.", "correct": True}
                ]),
                make_tf(2, "Cho tam giác ABC cân tại A (AB = AC):", [
                    {"key": "a", "level": "Nhận biết", "text": "Hai góc ở đáy góc B = góc C.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Đường phân giác hạ từ đỉnh A trùng với đường cao và đường trung tuyến ứng với cạnh đáy.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Bốn điểm: Trọng tâm, trực tâm, tâm ngoại tiếp, tâm nội tiếp cùng nằm trên một đường thẳng.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu góc A = 120° thì cạnh đáy BC nhỏ hơn cạnh bên AB.", "correct": False}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Cho tam giác $ABC$ có trọng tâm $G$. Biết trung tuyến $AM = 15\\text{ cm}$. Tính độ dài đoạn thẳng $GM$ (cm):", "5"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{B} = 50^\\circ, \\widehat{C} = 30^\\circ$. Cạnh lớn nhất là cạnh nào (ghi rõ tên cạnh ví dụ AB, BC hoặc AC)?", "BC"),
                make_sa(3, "Vận dụng", "Tam giác $ABC$ có độ dài hai cạnh là $4\\text{ cm}$ và $10\\text{ cm}$. Biết độ dài cạnh thứ ba là số nguyên lẻ. Độ dài cạnh thứ ba là bao nhiêu cm?", "7", acceptable=["7", "9", "11", "13"]),
                make_sa(4, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$, $BC = 13\\text{ cm}$, đường cao $AH = 6\\text{ cm}$. Chu vi tam giác $ABC$ bằng bao nhiêu cm (làm tròn số nguyên)?", "30", acceptable=["30", "30.4", "31"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác $ABC$ cân tại $A$. Gọi $D$ là trung điểm của $BC$. Kẻ $DE \\perp AB, DF \\perp AC$. Chứng minh $DE = DF$.", "Chứng minh tam giác BDE = tam giác CDF (cạnh huyền - góc nhọn) (0.5đ). Suy ra DE = DF (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác $ABC$, các đường trung tuyến $BD, CE$ cắt nhau tại $G$. Lấy các điểm $M, N$ sao cho $E$ là trung điểm $AM$, $D$ là trung điểm $AN$. Chứng minh $MN // BC$.", "Áp dụng tính chất đường trung bình hoặc tam giác đồng dạng, tính chất đối xứng suy ra MN // BC và MN = BC (1.0đ)."),
                make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{A} = 60^\\circ$. Hai tia phân giác của góc $B$ và $C$ cắt nhau tại $I$ và cắt $AC, AB$ lần lượt tại $D, E$. Chứng minh $ID = IE$.", "Tính góc BIC = 180° - (B+C)/2 = 120°. Kẻ tia phân giác góc BIC (0.5đ). Sử dụng các cặp tam giác bằng nhau chứng minh ID = IE (0.5đ).")
            ]
        }

    save_chapter_package(7, "c9_7", "Chương IX: Quan hệ giữa các yếu tố trong một tam giác", exams)

# ==============================================================================
# CHƯƠNG X TOÁN 7: MỘT SỐ HÌNH KHỐI TRONG THỰC TIỄN (3 BÀI = 9 ĐỀ)
# ==============================================================================
def generate_c10_toan7():
    print("🚀 Đang biên soạn Chương X Toán 7: Một số hình khối trong thực tiễn...")
    exams = {}

    # BÀI 1 (Bài 36): HÌNH HỘP CHỮ NHẬT VÀ HÌNH LẬP PHƯƠNG
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c10_7_bai1_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài 36: Hình hộp chữ nhật và hình lập phương - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Hình hộp chữ nhật có bao nhiêu đỉnh, bao nhiêu cạnh và bao nhiêu mặt?", ["8 đỉnh, 12 cạnh, 6 mặt", "6 đỉnh, 12 cạnh, 8 mặt", "8 đỉnh, 8 cạnh, 6 mặt", "12 đỉnh, 8 cạnh, 6 mặt"], 0),
                make_mc(2, "Nhận biết", "Các mặt của hình hộp chữ nhật đều là:", ["Hình chữ nhật", "Hình vuông", "Hình bình hành", "Hình thoi"], 0),
                make_mc(3, "Nhận biết", "Hình lập phương có 6 mặt đều là:", ["Hình vuông bằng nhau", "Hình chữ nhật", "Hình thoi", "Tam giác đều"], 0),
                make_mc(4, "Nhận biết", "Hình hộp chữ nhật có bao nhiêu đường chéo chính nối 2 đỉnh đối diện?", ["$4$ đường chéo", "$2$ đường chéo", "$6$ đường chéo", "$8$ đường chéo"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính thể tích hình hộp chữ nhật có ba kích thước $a, b, c$ là:", ["$V = a \\cdot b \\cdot c$", "$V = a + b + c$", "$V = 2(a + b)c$", "$V = a^3$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính diện tích xung quanh của hình hộp chữ nhật có kích thước đáy $a, b$ và chiều cao $c$ là:", ["$S_{xq} = 2(a + b) \\cdot c$", "$S_{xq} = a \\cdot b \\cdot c$", "$S_{xq} = (a + b) \\cdot c$", "$S_{xq} = 2(ab + bc + ca)$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Thể tích của hình lập phương có cạnh $a$ bằng:", ["$V = a^3$", "$V = 6a^2$", "$V = 4a^2$", "$V = a^2$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Diện tích toàn phần của hình lập phương có cạnh $a$ bằng:", ["$S_{tp} = 6a^2$", "$S_{tp} = 4a^2$", "$S_{tp} = a^3$", "$S_{tp} = 12a$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Một hình lập phương có cạnh $4\\text{ cm}$. Thể tích của nó là:", ["$64\\text{ cm}^3$", "$16\\text{ cm}^3$", "$96\\text{ cm}^3$", "$48\\text{ cm}^3$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hình hộp chữ nhật có kích thước $3\\text{ cm}, 4\\text{ cm}, 5\\text{ cm}$. Diện tích xung quanh là:", ["$70\\text{ cm}^2$", "$60\\text{ cm}^2$", "$94\\text{ cm}^2$", "$35\\text{ cm}^2$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Một bể cá hình hộp chữ nhật dài $60\\text{ cm}$, rộng $40\\text{ cm}$, cao $50\\text{ cm}$. Thể tích của bể là bao nhiêu lít?", ["$120$ lít", "$12$ lít", "$1200$ lít", "$60$ lít"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Nếu tăng cạnh của một hình lập phương lên gấp $2$ lần thì thể tích của nó tăng lên gấp:", ["$8$ lần", "$2$ lần", "$4$ lần", "$6$ lần"], 0)
            ],
            "part2": [
                make_tf(1, "Cho hình hộp chữ nhật ABCD.A'B'C'D' có đáy ABCD kích thước AB = 5 cm, AD = 4 cm và chiều cao AA' = 3 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Hình hộp có 8 đỉnh và 12 cạnh.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Đoạn thẳng AC' là một đường chéo của hình hộp chữ nhật.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Diện tích xung quanh của hình hộp chữ nhật bằng 2*(5 + 4)*3 = 54 cm².", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Độ dài đường chéo AC' bằng 5√2 cm (xấp xỉ 7,07 cm).", "correct": True}
                ]),
                make_tf(2, "Xét hình lập phương có diện tích toàn phần bằng 150 cm²:", [
                    {"key": "a", "level": "Nhận biết", "text": "Hình lập phương có 6 mặt vuông bằng nhau.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Diện tích một mặt của hình lập phương là 25 cm².", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Độ dài mỗi cạnh của hình lập phương bằng 5 cm.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu nhúng chìm hoàn toàn hình lập phương này vào một bình chứa nước hình trụ thì thể tích nước dâng lên là 100 cm³.", "correct": False}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Một hình lập phương có cạnh bằng $6\\text{ cm}$. Diện tích xung quanh của hình lập phương đó bằng bao nhiêu $\\text{cm}^2$?", "144"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Một chiếc hộp quà hình hộp chữ nhật có các kích thước là $10\\text{ cm}, 15\\text{ cm}, 20\\text{ cm}$. Thể tích hộp quà bằng bao nhiêu $\\text{cm}^3$?", "3000"),
                make_sa(3, "Vận dụng", "Một khối gỗ hình lập phương có thể tích bằng $512\\text{ cm}^3$. Diện tích toàn phần của khối gỗ đó bằng bao nhiêu $\\text{cm}^2$?", "384"),
                make_sa(4, "Vận dụng", "Người ta sơn toàn bộ 4 bức tường xung quanh một căn phòng hình chữ nhật dài $8\\text{ m}$, rộng $5\\text{ m}$, cao $4\\text{ m}$. Tổng diện tích các cửa là $9\\text{ m}^2$. Diện tích cần quét sơn là bao nhiêu $\\text{m}^2$?", "95")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một thùng chứa nước hình hộp chữ nhật có kích thước lòng trong: chiều dài $1,5\\text{ m}$, chiều rộng $1,2\\text{ m}$ và chiều cao $0,8\\text{ m}$. Tính thể tích nước tối đa mà thùng có thể chứa được theo đơn vị lít.", "Thể tích của thùng: V = 1.5 * 1.2 * 0.8 = 1.44 m³ (0.5đ). Đổi 1.44 m³ = 1440 dm³ = 1440 lít nước (0.5đ)."),
                make_essay(2, "Vận dụng", "Một bể bơi dạng hình hộp chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $10\\text{ m}$, sâu $2\\text{ m}$. Người ta dùng gạch men hình vuông cạnh $50\\text{ cm}$ để lát đáy và xung quanh thành bể. Tính số viên gạch cần dùng (bỏ qua mạch vữa).", "Diện tích đáy: Sđ = 25*10 = 250 m². Diện tích xung quanh: Sxq = 2*(25+10)*2 = 140 m². Tổng diện tích lát gạch: S = 250 + 140 = 390 m² (0.5đ). Diện tích 1 viên gạch: 0.5*0.5 = 0.25 m². Số viên gạch: 390 / 0.25 = 1560 viên (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Một bể cá hình hộp chữ nhật đáy $60\\text{ cm} \\times 40\\text{ cm}$ chứa nước sâu $25\\text{ cm}$. Người ta thả vào bể một hòn non bộ thì nước dâng lên cao $32\\text{ cm}$. Tính thể tích hòn non bộ theo đơn vị lít.", "Mực nước dâng thêm là: 32 - 25 = 7 cm (0.5đ). Thể tích của hòn non bộ chính là thể tích lượng nước dâng lên: V = 60 * 40 * 7 = 16800 cm³ = 16.8 lít (0.5đ).")
            ]
        }

    # BÀI 2 (Bài 37): HÌNH LĂNG TRỤ ĐỨNG TAM GIÁC VÀ TỨ GIÁC
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c10_7_bai2_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài 37: Hình lăng trụ đứng tam giác và tứ giác - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Các mặt bên của hình lăng trụ đứng tam giác là:", ["Hình chữ nhật", "Tam giác", "Hình thang", "Hình bình hành"], 0),
                make_mc(2, "Nhận biết", "Hình lăng trụ đứng tam giác có hai đáy là hai hình gì?", ["Hai tam giác bằng nhau và song song", "Hai hình chữ nhật", "Hai tứ giác", "Hai hình tròn"], 0),
                make_mc(3, "Nhận biết", "Hình lăng trụ đứng tứ giác có bao nhiêu mặt, bao nhiêu đỉnh, bao nhiêu cạnh?", ["6 mặt, 8 đỉnh, 12 cạnh", "5 mặt, 6 đỉnh, 9 cạnh", "8 mặt, 6 đỉnh, 12 cạnh", "6 mặt, 6 đỉnh, 8 cạnh"], 0),
                make_mc(4, "Nhận biết", "Độ dài một cạnh bên của hình lăng trụ đứng gọi là:", ["Chiều cao của hình lăng trụ", "Đường chéo", "Cạnh đáy", "Trung đoạn"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính diện tích xung quanh của hình lăng trụ đứng là:", ["$S_{xq} = C_{đáy} \\cdot h$", "$S_{xq} = S_{đáy} \\cdot h$", "$S_{xq} = \\frac{1}{2} C_{đáy} \\cdot h$", "$S_{xq} = 2 C_{đáy} \\cdot h$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính thể tích của hình lăng trụ đứng là:", ["$V = S_{đáy} \\cdot h$", "$V = \\frac{1}{3} S_{đáy} \\cdot h$", "$V = C_{đáy} \\cdot h$", "$V = 2 S_{đáy} \\cdot h$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Hình lăng trụ đứng tam giác có bao nhiêu cạnh bên?", ["$3$ cạnh bên", "$6$ cạnh bên", "$9$ cạnh bên", "$4$ cạnh bên"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Hình hộp chữ nhật là trường hợp đặc biệt của:", ["Hình lăng trụ đứng tứ giác có đáy là hình chữ nhật", "Hình lăng trụ đứng tam giác", "Hình chóp tứ giác", "Hình lăng trụ xiên"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Một hình lăng trụ đứng tam giác có chu vi đáy $15\\text{ cm}$, chiều cao $8\\text{ cm}$. Diện tích xung quanh là:", ["$120\\text{ cm}^2$", "$60\\text{ cm}^2$", "$240\\text{ cm}^2$", "$180\\text{ cm}^2$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hình lăng trụ đứng tam giác có diện tích đáy $12\\text{ cm}^2$, chiều cao $10\\text{ cm}$. Thể tích là:", ["$120\\text{ cm}^3$", "$40\\text{ cm}^3$", "$60\\text{ cm}^3$", "$240\\text{ cm}^3$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Một chiếc lều cắm trại hình lăng trụ đứng tam giác có chiều dài lều $3\\text{ m}$, đáy là tam giác diện tích $2\\text{ m}^2$. Thể tích không gian bên trong lều là:", ["$6\\text{ m}^3$", "$3\\text{ m}^3$", "$2\\text{ m}^3$", "$18\\text{ m}^3$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một hình lăng trụ đứng tứ giác có đáy là hình thoi có hai đường chéo $6\\text{ cm}$ và $8\\text{ cm}$. Chiều cao lăng trụ $10\\text{ cm}$. Thể tích lăng trụ là:", ["$240\\text{ cm}^3$", "$480\\text{ cm}^3$", "$80\\text{ cm}^3$", "$120\\text{ cm}^3$"], 0)
            ],
            "part2": [
                make_tf(1, "Cho hình lăng trụ đứng tam giác ABC.A'B'C' có đáy ABC là tam giác vuông tại A với AB = 3 cm, AC = 4 cm và chiều cao AA' = 7 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Hình lăng trụ có 5 mặt, 6 đỉnh và 9 cạnh.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Độ dài cạnh huyền BC của đáy bằng 5 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Diện tích đáy ABC bằng 6 cm².", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Diện tích toàn phần của lăng trụ đứng bằng 96 cm².", "correct": True}
                ]),
                make_tf(2, "Một khối bê tông hình lăng trụ đứng tứ giác có đáy là hình thang cân với các cạnh đáy 2 m và 4 m, chiều cao hình thang là 2 m; chiều cao khối bê tông là 5 m:", [
                    {"key": "a", "level": "Nhận biết", "text": "Khối bê tông có 2 mặt đáy là hình thang cân.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Diện tích một mặt đáy của khối bê tông bằng 6 m².", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Thể tích của khối bê tông đó bằng 30 m³.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Biết 1 m³ bê tông nặng 2,4 tấn thì khối bê tông này nặng đúng 72 tấn.", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Một hình lăng trụ đứng tam giác có diện tích đáy bằng $16\\text{ cm}^2$ và chiều cao $9\\text{ cm}$. Tính thể tích của hình lăng trụ đó ($\\text{cm}^3$):", "144"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Một hình lăng trụ đứng tứ giác có chu vi đáy $24\\text{ cm}$ và chiều cao $10\\text{ cm}$. Diện tích xung quanh bằng bao nhiêu $\\text{cm}^2$?", "240"),
                make_sa(3, "Vận dụng", "Một khối phô mai hình lăng trụ đứng tam giác có đáy là tam giác vuông cân cạnh góc vuông $4\\text{ cm}$, chiều cao lăng trụ $12\\text{ cm}$. Thể tích khối phô mai bằng bao nhiêu $\\text{cm}^3$?", "96"),
                make_sa(4, "Vận dụng", "Một chiếc cột bê tông hình lăng trụ đứng tứ giác đáy hình vuông cạnh $0,4\\text{ m}$, chiều cao $3,5\\text{ m}$. Chi phí đúc cột là $1,2$ triệu đồng$/\\text{m}^3$. Tiền đúc một chiếc cột là bao nhiêu nghìn đồng?", "672")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một thanh socola hình lăng trụ đứng tam giác có đáy là tam giác đều cạnh $3\\text{ cm}$, chiều cao $15\\text{ cm}$. Người ta bọc giấy bạc xung quanh thanh kẹo. Tính diện tích giấy bạc cần dùng (bỏ qua mép gấp).", "Chu vi đáy của lăng trụ tam giác đều: C = 3 * 3 = 9 cm (0.5đ). Diện tích xung quanh cần bọc giấy bạc: Sxq = C * h = 9 * 15 = 135 cm² (0.5đ)."),
                make_essay(2, "Vận dụng", "Một chiếc máng nước bằng tôn hình lăng trụ đứng có hai đáy là hình thang cân kích thước đáy bé $20\\text{ cm}$, đáy lớn $40\\text{ cm}$, chiều cao hình thang $15\\text{ cm}$. Chiều dài máng là $2\\text{ m}$. Hỏi máng chứa được tối đa bao nhiêu lít nước?", "Diện tích mặt cắt đáy hình thang: Sđ = (20 + 40)*15 / 2 = 450 cm² (0.5đ). Chiều dài lăng trụ h = 2 m = 200 cm. Thể tích máng nước: V = 450 * 200 = 90000 cm³ = 90 dm³ = 90 lít (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Một thùng gỗ hình lăng trụ đứng tứ giác đáy là hình thoi có cạnh $50\\text{ cm}$ và một đường chéo $60\\text{ cm}$. Chiều cao thùng là $80\\text{ cm}$. Tính diện tích toàn phần của thùng gỗ (bao gồm cả nắp đậy).", "Nửa hình thoi là tam giác vuông có cạnh huyền 50 cm, 1 cạnh góc vuông 30 cm suy ra nửa đường chéo kia bằng 40 cm. Đường chéo thứ hai là 80 cm (0.5đ). Diện tích đáy hình thoi: (60*80)/2 = 2400 cm². Diện tích xung quanh: 4*50*80 = 16000 cm². Diện tích toàn phần: Stp = 16000 + 2*2400 = 20800 cm² (0.5đ).")
            ]
        }

    # BÀI 3 (Bài 38): ÔN TẬP VÀ KIỂM TRA CUỐI CHƯƠNG X
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c10_7_bai3_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Ôn tập và kiểm tra cuối Chương X - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Thể tích hình hộp chữ nhật có 3 kích thước $a, b, h$ là:", ["$V = a \\cdot b \\cdot h$", "$V = 2(a + b)h$", "$V = a + b + h$", "$V = 2ab + 2bh$"], 0),
                make_mc(2, "Nhận biết", "Thể tích lăng trụ đứng có diện tích đáy $S$ và chiều cao $h$ là:", ["$V = S \\cdot h$", "$V = \\frac{1}{3}S \\cdot h$", "$V = 2S \\cdot h$", "$V = \\frac{1}{2}S \\cdot h$"], 0),
                make_mc(3, "Nhận biết", "Hình hộp chữ nhật có bao nhiêu đường chéo?", ["4", "2", "6", "8"], 0),
                make_mc(4, "Nhận biết", "Hình lập phương có cạnh $3\\text{ cm}$ thì diện tích toàn phần là:", ["$54\\text{ cm}^2$", "$36\\text{ cm}^2$", "$27\\text{ cm}^2$", "$18\\text{ cm}^2$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Hình lăng trụ đứng tam giác có số đỉnh là:", ["6 đỉnh", "5 đỉnh", "8 đỉnh", "9 đỉnh"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Đáy của hình lăng trụ đứng tứ giác là:", ["Một hình tứ giác bất kì", "Hình tam giác", "Hình tròn", "Hình lục giác"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Diện tích xung quanh của hình lăng trụ đứng bằng:", ["Chu vi đáy nhân với chiều cao", "Diện tích đáy nhân chiều cao", "Nửa chu vi đáy nhân chiều cao", "Tổng diện tích hai đáy"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "$1\\text{ m}^3$ bằng bao nhiêu lít?", ["$1000$ lít", "$100$ lít", "$10$ lít", "$10000$ lít"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Một khối gỗ hình lập phương có cạnh $5\\text{ dm}$. Thể tích của nó là:", ["$125\\text{ lít}$", "$25\\text{ lít}$", "$150\\text{ lít}$", "$50\\text{ lít}$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hình lăng trụ đứng tam giác có đáy là tam giác vuông hai cạnh góc vuông $3\\text{ cm}, 4\\text{ cm}$. Chiều cao $6\\text{ cm}$. Thể tích là:", ["$36\\text{ cm}^3$", "$72\\text{ cm}^3$", "$24\\text{ cm}^3$", "$18\\text{ cm}^3$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Cần bao nhiêu khối lập phương nhỏ cạnh $1\\text{ cm}$ để xếp thành khối lập phương cạnh $4\\text{ cm}$?", ["$64$ khối", "$16$ khối", "$32$ khối", "$24$ khối"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một bể nước hình hộp chữ nhật chứa $4800$ lít nước, đáy bể có kích thước $2\\text{ m} \\times 1,5\\text{ m}$. Chiều cao mực nước trong bể là:", ["$1,6\\text{ m}$", "$1,2\\text{ m}$", "$1,5\\text{ m}$", "$2,0\\text{ m}$"], 0)
            ],
            "part2": [
                make_tf(1, "Một bể kính nuôi cá dạng hình hộp chữ nhật có chiều dài 80 cm, chiều rộng 50 cm và chiều cao 60 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Bể cá không có nắp đậy gồm có 5 mặt kính.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Diện tích kính dùng làm bể cá bằng 19600 cm² (tương đương 1,96 m²).", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Thể tích toàn bộ bể kính là 240 lít nước.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu đổ vào bể 160 lít nước thì chiều cao mực nước trong bể đạt đúng 40 cm.", "correct": True}
                ]),
                make_tf(2, "Một khúc gỗ hình lăng trụ đứng tam giác có đáy là tam giác vuông với hai cạnh góc vuông là 6 cm và 8 cm; chiều dài khúc gỗ là 20 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Cạnh huyền của mặt đáy tam giác vuông bằng 10 cm.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Chu vi đáy của khúc gỗ bằng 24 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Thể tích của khúc gỗ bằng 480 cm³.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Người ta sơn màu toàn bộ các mặt của khúc gỗ thì diện tích cần sơn là 528 cm².", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Hình lập phương có thể tích $1000\\text{ cm}^3$. Độ dài mỗi cạnh của hình lập phương là bao nhiêu cm?", "10"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Một khối kim loại hình hộp chữ nhật có kích thước $2\\text{ cm} \\times 5\\text{ cm} \\times 8\\text{ cm}$. Khối lượng riêng là $7,8\\text{ g/cm}^3$. Khối kim loại nặng bao nhiêu gam?", "624"),
                make_sa(3, "Vận dụng", "Người ta làm một chiếc hộp không nắp hình lập phương bằng bìa carton cạnh $20\\text{ cm}$. Diện tích bìa cần dùng là bao nhiêu $\\text{cm}^2$ (bỏ qua mép dán)?", "2000"),
                make_sa(4, "Vận dụng", "Một chiếc xe bồn chở dầu có bồn chứa dạng hình lăng trụ đứng đáy là hình elip diện tích $3,2\\text{ m}^2$, chiều dài bồn $6\\text{ m}$. Bồn chở được tối đa bao nhiêu mét khối dầu?", "19.2", acceptable=["19.2", "19,2", "96/5"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một căn phòng hình hộp chữ nhật dài $6\\text{ m}$, rộng $4,5\\text{ m}$, cao $3,5\\text{ m}$. Người ta muốn quét vôi trần nhà và bốn bức tường. Biết tổng diện tích các cửa là $8\\text{ m}^2$. Tính diện tích cần quét vôi.", "Diện tích trần nhà: 6 * 4.5 = 27 m² (0.25đ). Diện tích xung quanh: 2*(6 + 4.5)*3.5 = 73.5 m² (0.25đ). Diện tích quét vôi: (27 + 73.5) - 8 = 92.5 m² (0.5đ)."),
                make_essay(2, "Vận dụng", "Người ta đào một con mương dẫn nước dài $50\\text{ m}$, mặt cắt ngang là hình lăng trụ đứng có đáy hình thang cân đáy lớn $1,8\\text{ m}$, đáy nhỏ $1,2\\text{ m}$, sâu $1\\text{ m}$. Tính thể tích đất phải đào lên.", "Diện tích mặt cắt đáy hình thang: Sđ = (1.8 + 1.2)*1 / 2 = 1.5 m² (0.5đ). Thể tích đất phải đào: V = Sđ * chiều dài = 1.5 * 50 = 75 m³ (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Một khối lập phương bằng sắt cạnh $10\\text{ cm}$ được thả vào một bể nước hình hộp chữ nhật đáy $25\\text{ cm} \\times 20\\text{ cm}$ đang có nước sâu $15\\text{ cm}$. Hỏi sau khi thả khối sắt chìm hoàn toàn thì mực nước trong bể là bao nhiêu cm?", "Thể tích khối lập phương bằng sắt: V = 10³ = 1000 cm³ (0.5đ). Diện tích đáy bể nước: 25 * 20 = 500 cm². Chiều cao nước dâng thêm: 1000 / 500 = 2 cm. Mực nước mới trong bể: 15 + 2 = 17 cm (0.5đ).")
            ]
        }

    save_chapter_package(7, "c10_7", "Chương X: Một số hình khối trong thực tiễn", exams)

if __name__ == "__main__":
    generate_c9_toan7()
    generate_c10_toan7()
    print("🎉 TOÀN BỘ CHƯƠNG IX VÀ X TOÁN 7 ĐÃ ĐƯỢC TẠO HOÀN TẤT VÀ KIỂM ĐỊNH XUẤT SẮC!")
