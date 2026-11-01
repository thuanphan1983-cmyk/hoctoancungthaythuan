# -*- coding: utf-8 -*-
"""
BIÊN SOẠN BỔ SUNG 4 ĐỀ CUỐI CHƯƠNG (ĐỀ 4, 5, 6, 7) - TOÁN 8 (10 CHƯƠNG)
Tuân thủ nghiêm ngặt 8 quy tắc của Bộ GD&ĐT:
- Ma trận: 30% Nhận biết, 30% Thông hiểu, 20% Vận dụng, 20% Vận dụng cao.
- Phần I: 12 câu trắc nghiệm khách quan 4 lựa chọn (3.0 điểm)
- Phần II: 2 câu Đúng/Sai (4.0 điểm), mỗi câu đúng 1 ý Vận dụng
- Phần III: 4 câu Trả lời ngắn (2.0 điểm), đúng 2 câu Vận dụng/VDC
- Phần IV: 3 bài Tự luận (1.0 điểm), có ý Vận dụng cao chốt điểm 10
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')
PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package, OUTPUT_DIR
from build_grade6_chapter_ends import load_existing_exams

# 1. CHƯƠNG 1 TOÁN 8: ĐA THỨC (Bài 6: cuối chương)
def build_c1_8_exams():
    chap_id = "c1_8"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Đa thức nhiều biến thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Biểu thức nào sau đây là đơn thức nhiều biến?", ["$-3x^2y$", "$2x + y$", "$x^2 - y^2$", "$\\frac{x}{y}$"], 0),
            make_mc(2, "Nhận biết", "Bậc của đơn thức $4x^3y^2z$ là:", ["$6$", "$5$", "$3$", "$1$"], 0),
            make_mc(3, "Nhận biết", "Đơn thức nào sau đây đồng dạng với đơn thức $-5x^2y$?", ["$3x^2y$", "$5xy^2$", "$-5xy$", "$2x^3y$"], 0),
            make_mc(4, "Nhận biết", "Bậc của đa thức $A = 2x^4y - 3x^2y^3 + 5$ là:", ["$5$", "$4$", "$3$", "$2$"], 0),
            make_mc(5, "Thông hiểu", "Thu gọn đa thức $P = 3x^2y - 5xy + 2x^2y + 5xy$ ta được:", ["$5x^2y$", "$5x^2y - 10xy$", "$x^2y$", "$0$"], 0),
            make_mc(6, "Thông hiểu", "Tích của đơn thức $2xy$ với đa thức $(x^2 - 3y)$ là:", ["$2x^3y - 6xy^2$", "$2x^3y - 3y$", "$2x^2y - 6xy$", "$2x^3y + 6xy^2$"], 0),
            make_mc(7, "Thông hiểu", "Kết quả của phép chia $(6x^4y^3 - 9x^2y^2) : (3x^2y)$ là:", ["$2x^2y^2 - 3y$", "$2x^2y - 3$", "$2x^2y^2 - 3x$", "$3x^2y^2 - 3y$"], 0),
            make_mc(8, "Thông hiểu", "Giá trị của đa thức $M = x^2 - 2xy + y^2$ tại $x = 3, y = 1$ là:", ["$4$", "$2$", "$8$", "$16$"], 0),
            make_mc(9, "Vận dụng", "Tính tích $(2x - y)(x + 3y)$ ta được kết quả là:", ["$2x^2 + 5xy - 3y^2$", "$2x^2 - 5xy - 3y^2$", "$2x^2 + 6xy - 3y^2$", "$2x^2 - 3y^2$"], 0),
            make_mc(10, "Vận dụng", "Tìm đa thức $B$ biết $B - (2x^2y - 3xy^2) = 5x^2y + xy^2$:", ["$B = 7x^2y - 2xy^2$", "$B = 3x^2y + 4xy^2$", "$B = 7x^2y + 4xy^2$", "$B = 3x^2y - 2xy^2$"], 0),
            make_mc(11, "Vận dụng", "Một mảnh vườn hình chữ nhật có chiều dài $(2x + 3)\\text{ m}$ và chiều rộng $(x + 1)\\text{ m}$. Diện tích mảnh vườn theo $x$ là:", ["$2x^2 + 5x + 3$", "$2x^2 + 3$", "$3x + 4$", "$2x^2 + 4x + 3$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm giá trị nhỏ nhất của đa thức hai biến $A = x^2 + y^2 - 4x + 2y + 10$:", ["$5$ (khi $x = 2, y = -1$)", "$10$", "$0$", "$1$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về đơn thức và đa thức nhiều biến (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Đơn thức là biểu thức đại số chỉ gồm một số, hoặc một biến, hoặc một tích giữa các số và các biến.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Bậc của đa thức là bậc của hạng tử có bậc cao nhất trong dạng thu gọn của đa thức đó.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Phép chia đa thức cho đơn thức chỉ thực hiện được khi mọi hạng tử của đa thức đều chia hết cho đơn thức.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tích của hai đa thức bậc 2 luôn là một đa thức bậc 4.", "correct": True}
            ]),
            make_tf(2, "Cho hai đa thức $P = 4x^2 - 2xy + y^2$ và $Q = x^2 + 2xy - 3y^2$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng P + Q = 5x^2 - 2y^2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hiệu P - Q = 3x^2 - 4xy + 4y^2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tại x = 1, y = 1 thì P = 3.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Đa thức P luôn nhận giá trị dương với mọi cặp số thực (x, y) khác (0, 0).", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tìm bậc của đa thức: P = 5x^3y^2 - 2x^4y + x^2 - 1.", "5"),
            make_sa(2, "Thông hiểu", "Tính giá trị của đa thức A = x^2 - 4xy tại x = 2, y = -1.", "12"),
            make_sa(3, "Vận dụng", "Tính giá trị của biểu thức P = (x + y)(x - y) tại x = 15, y = 5.", "200"),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của đa thức: M = x^2 - 6x + y^2 + 4y + 20.", "7")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Thu gọn đa thức sau: $A = 2x^2y - 3xy^2 + 5 - x^2y + 4xy^2 - 2$.", "A = (2 - 1)x^2y + (-3 + 4)xy^2 + (5 - 2) = x^2y + xy^2 + 3 (0.5đ)."),
            make_essay(2, "Vận dụng", "Thực hiện phép tính: $(2x - 3y)(4x^2 + 6xy + 9y^2)$.", "= (2x)^3 - (3y)^3 = 8x^3 - 27y^3 (0.5đ)."),
            make_essay(3, "Vận dụng cao", "Cho $x + y = 5$ và $xy = 2$. Tính giá trị của biểu thức $P = x^3 + y^3$.", "Ta có: x^3 + y^3 = (x + y)^3 - 3xy(x + y) (0.25đ).\nThay x + y = 5 và xy = 2:\nP = 5^3 - 3 . 2 . 5 = 125 - 30 = 95 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương I: Đa thức - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 2. CHƯƠNG 2 TOÁN 8: HẰNG ĐẲNG THỨC ĐÁNG NHỚ VÀ ỨNG DỤNG (Bài 5: cuối chương)
def build_c2_8_exams():
    chap_id = "c2_8"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Hằng đẳng thức & Phân tích nhân tử",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Khai triển của hằng đẳng thức $(a + b)^2$ là:", ["$a^2 + 2ab + b^2$", "$a^2 - 2ab + b^2$", "$a^2 + b^2$", "$a^2 + ab + b^2$"], 0),
            make_mc(2, "Nhận biết", "Hằng đẳng thức hiệu hai bình phương là:", ["$a^2 - b^2 = (a - b)(a + b)$", "$a^2 - b^2 = (a - b)^2$", "$(a - b)^2 = a^2 - 2ab + b^2$", "$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$"], 0),
            make_mc(3, "Nhận biết", "Biểu thức $x^2 - 4$ được phân tích thành nhân tử là:", ["$(x - 2)(x + 2)$", "$(x - 2)^2$", "$(x + 2)^2$", "$(x - 4)(x + 4)$"], 0),
            make_mc(4, "Nhận biết", "Phân tích đa thức $3x^2 - 6x$ thành nhân tử bằng phương pháp đặt nhân tử chung:", ["$3x(x - 2)$", "$3(x^2 - 2)$", "$x(3x - 6)$", "$3x(x + 2)$"], 0),
            make_mc(5, "Thông hiểu", "Khai triển biểu thức $(2x - 1)^2$ ta được:", ["$4x^2 - 4x + 1$", "$4x^2 - 2x + 1$", "$4x^2 + 4x + 1$", "$2x^2 - 4x + 1$"], 0),
            make_mc(6, "Thông hiểu", "Tính nhanh $101^2$ áp dụng hằng đẳng thức:", ["$(100 + 1)^2 = 10\\,201$", "$10\\,101$", "$10\\,001$", "$10\\,200$"], 0),
            make_mc(7, "Thông hiểu", "Biểu thức $x^3 + 8$ viết dưới dạng tích là:", ["$(x + 2)(x^2 - 2x + 4)$", "$(x + 2)(x^2 + 2x + 4)$", "$(x - 2)(x^2 + 2x + 4)$", "$(x + 2)^3$"], 0),
            make_mc(8, "Thông hiểu", "Tìm $x$, biết $x^2 - 9 = 0$:", ["$x = 3$ hoặc $x = -3$", "$x = 3$", "$x = 9$", "$x = -9$"], 0),
            make_mc(9, "Vận dụng", "Phân tích đa thức $x^2 - 2xy + y^2 - 9$ thành nhân tử:", ["$(x - y - 3)(x - y + 3)$", "$(x - y - 9)(x - y + 9)$", "$(x + y - 3)(x + y + 3)$", "$(x - y - 3)^2$"], 0),
            make_mc(10, "Vận dụng", "Tìm $x$, biết $x^3 - 4x = 0$:", ["$x = 0, x = 2, x = -2$", "$x = 0, x = 4$", "$x = 2, x = -2$", "$x = 0, x = 2$"], 0),
            make_mc(11, "Vận dụng", "Giá trị của biểu thức $P = x^3 - 3x^2 + 3x - 1$ tại $x = 101$ là:", ["$1\\,000\\,000$", "$100\\,000$", "$10\\,000$", "$1\\,000$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm giá trị lớn nhất của biểu thức $B = 5 - x^2 + 2x$:", ["$6$ (khi $x = 1$)", "$5$", "$4$", "$7$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về 7 hằng đẳng thức đáng nhớ (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hằng đẳng thức (a - b)^2 và (b - a)^2 luôn bằng nhau với mọi a, b.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khai triển (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Biểu thức a^2 + b^2 luôn luôn phân tích được thành nhân tử trên tập số thực.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Với mọi số thực x, biểu thức x^2 - x + 1 luôn nhận giá trị dương.", "correct": True}
            ]),
            make_tf(2, "Cho biểu thức $A = (x + 2)^2 - (x - 2)^2$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Áp dụng hằng đẳng thức hiệu hai bình phương: A = (x + 2 - x + 2)(x + 2 + x - 2).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Rút gọn được A = 8x.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Khi x = -2 thì A = -16.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Phương trình A = x^2 có đúng một nghiệm duy nhất x = 0.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính nhanh: 52^2 - 48^2.", "400"),
            make_sa(2, "Thông hiểu", "Tìm x biết: (x - 3)^2 = 0.", "3"),
            make_sa(3, "Vận dụng", "Tìm x biết: x^2 - 5x + 6 = 0. Tính tổng các nghiệm của phương trình.", "5"),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: P = x^2 - 4x + 13.", "9")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Phân tích đa thức sau thành nhân tử: $A = x^3 - 2x^2 + x$.", "A = x(x^2 - 2x + 1) = x(x - 1)^2 (0.5đ)."),
            make_essay(2, "Vận dụng", "Phân tích đa thức sau thành nhân tử: $B = x^2 - y^2 + 4x + 4$.", "B = (x^2 + 4x + 4) - y^2 = (x + 2)^2 - y^2 = (x + 2 - y)(x + 2 + y) (0.5đ)."),
            make_essay(3, "Vận dụng cao", "Chứng minh rằng với mọi số nguyên $n$, biểu thức $M = (n + 2)^2 - (n - 2)^2$ luôn chia hết cho 8.", "M = (n + 2 - n + 2)(n + 2 + n - 2) = 4 . 2n = 8n (0.25đ).\nVì n in Z nên 8n luôn chia hết cho 8 với mọi số nguyên n (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương II: Hằng đẳng thức - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 3. CHƯƠNG 3 TOÁN 8: TỨ GIÁC (Bài 6: cuối chương)
def build_c3_8_exams():
    chap_id = "c3_8"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Tứ giác đặc biệt trong thực tiễn",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Tổng các góc trong một tứ giác bằng:", ["$360^\\circ$", "$180^\\circ$", "$540^\\circ$", "$90^\\circ$"], 0),
            make_mc(2, "Nhận biết", "Hình thang cân là hình thang có:", ["Hai góc kề một đáy bằng nhau", "Hai cạnh bên song song", "Hai đường chéo vuông góc", "Bốn cạnh bằng nhau"], 0),
            make_mc(3, "Nhận biết", "Hình bình hành có hai đường chéo:", ["Cắt nhau tại trung điểm của mỗi đường", "Bằng nhau", "Vuông góc với nhau", "Là các đường phân giác"], 0),
            make_mc(4, "Nhận biết", "Hình chữ nhật là tứ giác có:", ["Bốn góc vuông", "Bốn cạnh bằng nhau", "Hai đường chéo vuông góc", "Hai cạnh bên bằng nhau"], 0),
            make_mc(5, "Thông hiểu", "Cho tứ giác $ABCD$ có $\\widehat{A} = 100^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 110^\\circ$. Số đo của góc $\\widehat{D}$ là:", ["$70^\\circ$", "$80^\\circ$", "$90^\\circ$", "$60^\\circ$"], 0),
            make_mc(6, "Thông hiểu", "Hình thoi có hai đường chéo dài $6\\text{ cm}$ và $8\\text{ cm}$. Cạnh của hình thoi đó bằng:", ["$5\\text{ cm}$", "$10\\text{ cm}$", "$7\\text{ cm}$", "$14\\text{ cm}$"], 0),
            make_mc(7, "Thông hiểu", "Hình thoi có thêm điều kiện nào sau đây thì trở thành hình vuông?", ["Có một góc vuông", "Hai đường chéo vuông góc", "Bốn cạnh bằng nhau", "Hai đường chéo cắt nhau tại trung điểm"], 0),
            make_mc(8, "Thông hiểu", "Hình chữ nhật có thêm điều kiện nào sau đây thì trở thành hình vuông?", ["Hai đường chéo vuông góc với nhau", "Hai đường chéo bằng nhau", "Bốn góc vuông", "Các cạnh đối song song"], 0),
            make_mc(9, "Vận dụng", "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $\\widehat{C} = 60^\\circ$. Số đo của góc $\\widehat{A}$ là:", ["$120^\\circ$", "$60^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0),
            make_mc(10, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$, đường trung tuyến $AM = 5\\text{ cm}$. Độ dài cạnh huyền $BC$ là:", ["$10\\text{ cm}$", "$5\\text{ cm}$", "$2,5\\text{ cm}$", "$15\\text{ cm}$"], 0),
            make_mc(11, "Vận dụng", "Một khung cửa sổ hình vuông có đường chéo dài $1,4\\text{ m}$. Diện tích của khung cửa sổ đó là:", ["$0,98\\text{ m}^2$", "$1,96\\text{ m}^2$", "$1,4\\text{ m}^2$", "$0,7\\text{ m}^2$"], 0),
            make_mc(12, "Vận dụng cao", "Cho hình vuông $ABCD$. Trên cạnh $BC$ lấy $E$, tia phân giác của $\\widehat{DAE}$ cắt $CD$ tại $F$. Chu vi tam giác $CEF$ bằng:", ["$2 AB$ (khi $E$ trùng $B$)", "Luôn bằng $2 CD$", "$AB + CD$", "Không đổi"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về các loại tứ giác đặc biệt (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hình chữ nhật có hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hình thoi có hai đường chéo vuông góc với nhau và là đường phân giác các góc.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tứ giác có hai đường chéo vuông góc luôn là hình thoi.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Các trung điểm của bốn cạnh của một hình chữ nhật tạo thành một hình thoi.", "correct": True}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của $BC$. Kẻ $MD \\perp AB$ tại $D$ và $ME \\perp AC$ tại $E$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Tứ giác ADME là hình chữ nhật.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Điểm D là trung điểm của AB và E là trung điểm của AC.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Độ dài đoạn thẳng DE bằng AM.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu tam giác ABC vuông cân tại A thì tứ giác ADME là hình vuông.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tứ giác ABCD có góc A = 70, B = 80, C = 100 độ. Tính góc D (độ).", "110"),
            make_sa(2, "Thông hiểu", "Hình thoi có cạnh bằng 10 cm, một đường chéo 12 cm. Tính độ dài đường chéo kia (cm).", "16"),
            make_sa(3, "Vận dụng", "Cho hình thang cân có đáy nhỏ 4 cm, đáy lớn 10 cm, cạnh bên 5 cm. Tính chiều cao hình thang (cm).", "4"),
            make_sa(4, "Vận dụng cao", "Cho hình chữ nhật ABCD có AB = 8 cm, BC = 6 cm. Tính khoảng cách từ đỉnh A đến đường chéo BD (cm).", "4,8")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Chứng minh rằng hình thang có hai đường chéo bằng nhau là hình thang cân.", "Qua đỉnh B kẻ đường thẳng song song với AC cắt đường thẳng DC tại E => ABEC là hình bình hành => BE = AC = BD (0.25đ).\n=> tam giác BDE cân tại B => góc BDC = E = ACD => tam giác ADC = BCD (c-g-c) => AD = BC => ABCD là hình thang cân (0.25đ)."),
            make_essay(2, "Vận dụng", "Cho tam giác $ABC$ cân tại $A$. Gọi $D, E$ lần lượt là trung điểm của $AB, AC$. Chứng minh tứ giác $BDEC$ là hình thang cân.", "Vì D, E là trung điểm AB, AC nên DE là đường trung bình => DE // BC => BDEC là hình thang (0.25đ).\nMặt khác tam giác ABC cân tại A => góc B = góc C.\nHình thang có hai góc kề một đáy bằng nhau nên BDEC là hình thang cân (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho hình bình hành $ABCD$. Kẻ $AH \\perp CD$ và $AK \\perp BC$. Biết $\\widehat{HAK} = 50^\\circ$. Tính các góc của hình bình hành $ABCD$.", "Xét tứ giác AHCK có góc H = 90 độ, K = 90 độ => C + HAK = 180 độ (0.25đ).\n=> góc C = 180 - 50 = 130 độ.\nVì ABCD là hình bình hành nên: A = C = 130 độ; B = D = 180 - 130 = 50 độ (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương III: Tứ giác - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 4. CHƯƠNG 4 TOÁN 8: ĐỊNH LÍ THALÈS (Bài 4: cuối chương)
def build_c4_8_exams():
    chap_id = "c4_8"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Định lí Thalès & Ứng dụng thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Định lí Thalès trong tam giác khẳng định: Nếu một đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn lại thì:", ["Nó định ra trên hai cạnh đó những đoạn thẳng tương ứng tỉ lệ", "Nó đi qua trung điểm hai cạnh đó", "Hai cạnh đó bằng nhau", "Tạo ra tam giác vuông"], 0),
            make_mc(2, "Nhận biết", "Đường trung bình của tam giác là đoạn thẳng nối:", ["Trung điểm hai cạnh của tam giác", "Đỉnh với trung điểm cạnh đối diện", "Hai điểm bất kì trên hai cạnh", "Tâm đường tròn ngoại tiếp"], 0),
            make_mc(3, "Nhận biết", "Độ dài đường trung bình của tam giác bằng:", ["Một nửa độ dài cạnh đáy tương ứng", "Bằng cạnh đáy", "Gấp đôi cạnh đáy", "Một phần ba cạnh đáy"], 0),
            make_mc(4, "Nhận biết", "Đường phân giác trong của một góc trong tam giác chia cạnh đối diện thành hai đoạn thẳng:", ["Tỉ lệ với hai cạnh kề hai đoạn thẳng đó", "Bằng nhau", "Bằng một nửa cạnh đối diện", "Vuông góc với cạnh đối diện"], 0),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$, $MN \\parallel BC$ ($M \\in AB, N \\in AC$). Biết $AM = 2\\text{ cm}, MB = 4\\text{ cm}, AN = 3\\text{ cm}$. Độ dài $NC$ là:", ["$6\\text{ cm}$", "$4\\text{ cm}$", "$5\\text{ cm}$", "$9\\text{ cm}$"], 0),
            make_mc(6, "Thông hiểu", "Cho tam giác $ABC$ có cạnh $BC = 12\\text{ cm}$. Đoạn thẳng nối trung điểm của $AB$ và $AC$ có độ dài là:", ["$6\\text{ cm}$", "$24\\text{ cm}$", "$4\\text{ cm}$", "$8\\text{ cm}$"], 0),
            make_mc(7, "Thông hiểu", "Cho tam giác $ABC$ có đường phân giác $AD$ ($D \\in BC$). Biết $AB = 4\\text{ cm}, AC = 6\\text{ cm}, BD = 2\\text{ cm}$. Độ dài $DC$ là:", ["$3\\text{ cm}$", "$4\\text{ cm}$", "$2\\text{ cm}$", "$5\\text{ cm}$"], 0),
            make_mc(8, "Thông hiểu", "Nếu $\\frac{AM}{AB} = \\frac{AN}{AC}$ thì theo định lí Thalès đảo ta suy ra:", ["$MN \\parallel BC$", "$MN \\perp BC$", "$MN = BC$", "$MN = \\frac{1}{2}BC$"], 0),
            make_mc(9, "Vận dụng", "Để đo chiều cao của một cái cây, người ta cắm một cọc thẳng đứng cao $2\\text{ m}$ cách gốc cây $15\\text{ m}$. Khi bóng của cọc trên mặt đất dài $1,5\\text{ m}$ thì bóng của cây dài bao nhiêu biết cây và cọc cùng phương nắng chiếu?", ["Chiều cao cây tỉ lệ với chiều dài bóng", "$20\\text{ m}$", "$18\\text{ m}$", "$15\\text{ m}$"], 0),
            make_mc(10, "Vận dụng", "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $M, N$ lần lượt là trung điểm của $AD, BC$. Biết $AB = 6\\text{ cm}, CD = 10\\text{ cm}$. Độ dài đoạn thẳng $MN$ là:", ["$8\\text{ cm}$", "$16\\text{ cm}$", "$4\\text{ cm}$", "$7\\text{ cm}$"], 0),
            make_mc(11, "Vận dụng", "Cho tam giác $ABC$ có chu vi $18\\text{ cm}$. Nối trung điểm ba cạnh của tam giác $ABC$ ta được tam giác mới có chu vi là:", ["$9\\text{ cm}$", "$6\\text{ cm}$", "$4,5\\text{ cm}$", "$12\\text{ cm}$"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$, đường trung tuyến $AM$. Gọi $I$ là trung điểm của $AM$, tia $CI$ cắt $AB$ tại $K$. Tỉ số $\\frac{AK}{AB}$ bằng:", ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{2}{3}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về định lí Thalès và tính chất đường phân giác (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hệ quả của định lí Thalès áp dụng được cho cả trường hợp đường thẳng cắt phần kéo dài của hai cạnh.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Đường trung bình của tam giác song song với cạnh thứ ba và bằng nửa cạnh đó.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Đường phân giác ngoài của một góc trong tam giác cũng chia cạnh đối diện theo tỉ số hai cạnh kề.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu MN // BC thì tỉ số diện tích tam giác AMN và ABC bằng tỉ số AM/AB.", "correct": False}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB = 6\\text{ cm}, AC = 9\\text{ cm}$, đường phân giác $AD$ ($D \\in BC$):", [
                {"key": "a", "level": "Thông hiểu", "text": "Tỉ số BD/CD = AB/AC = 2/3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Đoạn thẳng CD lớn hơn đoạn thẳng BD.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu BC = 10 cm thì BD = 4 cm và CD = 6 cm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tỉ số diện tích của hai tam giác ABD và ACD bằng 2/3.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho tam giác ABC, MN // BC. Biết AM = 3 cm, MB = 6 cm, AN = 4 cm. Tính AC (cm).", "12"),
            make_sa(2, "Thông hiểu", "Hình thang có hai đáy 8 cm và 14 cm. Tính độ dài đường trung bình của hình thang (cm).", "11"),
            make_sa(3, "Vận dụng", "Tam giác ABC có AB = 8 cm, AC = 12 cm, BC = 10 cm, AD là phân giác trong. Tính BD (cm).", "4"),
            make_sa(4, "Vận dụng cao", "Cho tam giác ABC vuông tại A có AB = 6 cm, AC = 8 cm, đường cao AH. Kẻ HD // AC (D thuộc AB). Tính độ dài HD (cm).", "3,84")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Cho tam giác $ABC$, một đường thẳng song song với $BC$ cắt $AB$ tại $D$ và $AC$ tại $E$. Biết $AD = 4\\text{ cm}, DB = 2\\text{ cm}, AE = 6\\text{ cm}$. Tính độ dài $EC$.", "Theo định lí Thalès: AD/DB = AE/EC => 4/2 = 6/EC => EC = 2 x 6 / 4 = 3 (cm) (0.5đ)."),
            make_essay(2, "Vận dụng", "Để đo khoảng cách giữa hai điểm $A$ và $B$ bị ngăn cách bởi một hồ nước, người ta chọn một điểm $C$ trên bờ nhìn rõ cả $A$ và $B$. Lấy $M, N$ lần lượt là trung điểm của $CA$ và $CB$. Đo được $MN = 45\\text{ m}$. Tính khoảng cách $AB$.", "Trong tam giác ABC, vì M, N là trung điểm của CA và CB nên MN là đường trung bình (0.25đ).\n=> AB = 2 MN = 2 x 45 = 90 (m). Vậy khoảng cách AB là 90 m (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Qua $O$ kẻ đường thẳng song song với $AB$ cắt $AD$ tại $M$ và $BC$ tại $N$. Chứng minh rằng $OM = ON$.", "Áp dụng hệ quả định lí Thalès:\nTrong tam giác ADC có MO // CD => OM/CD = AO/AC (0.25đ).\nTrong tam giác BDC có ON // CD => ON/CD = BO/BD.\nMặt khác vì AB // CD nên AO/AC = BO/BD.\nSuy ra: OM/CD = ON/CD => OM = ON. Đpcm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương IV: Định lí Thalès - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 5. CHƯƠNG 5 TOÁN 8: DỮ LIỆU VÀ BIỂU ĐỒ (Bài 4: cuối chương)
def build_c5_8_exams():
    chap_id = "c5_8"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Thống kê & Phân tích biểu đồ",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Dữ liệu thu thập được có thể là:", ["Số liệu hoặc dữ liệu không phải là số", "Chỉ gồm số nguyên dương", "Chỉ gồm chữ viết", "Chỉ gồm hình ảnh"], 0),
            make_mc(2, "Nhận biết", "Biểu đồ nào sau đây thích hợp nhất để biểu diễn tỉ lệ phần trăm các thành phần của một tổng thể?", ["Biểu đồ hình quạt tròn", "Biểu đồ cột", "Biểu đồ đoạn thẳng", "Biểu đồ tranh"], 0),
            make_mc(3, "Nhận biết", "Để nhận biết xu hướng tăng, giảm của một đại lượng theo thời gian, ta dùng:", ["Biểu đồ đoạn thẳng", "Biểu đồ tranh", "Biểu đồ quạt tròn", "Bảng dữ liệu chữ"], 0),
            make_mc(4, "Nhận biết", "Biểu đồ cột kép thường dùng để:", ["So sánh hai tập dữ liệu cùng loại trên cùng một tiêu chí", "Biểu diễn tỉ lệ phần trăm", "Biểu diễn số liệu liên tục", "Vẽ hình học phẳng"], 0),
            make_mc(5, "Thông hiểu", "Khảo sát thời gian tự học ở nhà của học sinh: Dữ liệu thu được thuộc loại:", ["Dữ liệu số (định lượng)", "Dữ liệu định tính", "Dữ liệu không đo đếm được", "Dữ liệu hình ảnh"], 0),
            make_mc(6, "Thông hiểu", "Một biểu đồ quạt tròn biểu diễn cơ cấu chi tiêu: Ăn uống $45\\%$, Nhà ở $25\\%$, Giáo dục $20\\%$, Tiết kiệm $10\\%$. Khoản chi tiêu nhiều nhất là:", ["Ăn uống ($45\\%$)", "Nhà ở", "Giáo dục", "Tiết kiệm"], 0),
            make_mc(7, "Thông hiểu", "Một bảng số liệu có số học sinh nam các lớp 8A, 8B, 8C lần lượt là 22, 20, 24; số học sinh nữ là 18, 22, 21. Biểu đồ thích hợp nhất để so sánh nam và nữ là:", ["Biểu đồ cột kép", "Biểu đồ quạt tròn", "Biểu đồ đoạn thẳng", "Biểu đồ tranh"], 0),
            make_mc(8, "Thông hiểu", "Lựa chọn biểu đồ thích hợp giúp người đọc:", ["Nắm bắt thông tin nhanh chóng, chính xác và trực quan", "Tránh phải tính toán", "Làm đẹp báo cáo", "Thay đổi được bản chất số liệu"], 0),
            make_mc(9, "Vận dụng", "Quan sát biểu đồ cột về số lượng sách bán được của một nhà sách trong 4 tuần: Tuần 1: 300 cuốn, Tuần 2: 450 cuốn, Tuần 3: 400 cuốn, Tuần 4: 650 cuốn. Số lượng sách bán trung bình mỗi tuần là:", ["$450$ cuốn", "$400$ cuốn", "$500$ cuốn", "$600$ cuốn"], 0),
            make_mc(10, "Vận dụng", "Tốc độ tăng trưởng doanh thu tuần 4 so với tuần 1 ở câu trên là:", ["Tăng hơn gấp đôi ($650$ so với $300$ cuốn)", "Tăng $50\\%$", "Giảm $20\\%$", "Không đổi"], 0),
            make_mc(11, "Vận dụng", "Một trường có 1000 học sinh. Biểu đồ quạt tròn cho biết học sinh đi xe buýt chiếm $15\\%$. Số học sinh đi xe buýt là:", ["$150$ học sinh", "$100$ học sinh", "$200$ học sinh", "$250$ học sinh"], 0),
            make_mc(12, "Vận dụng cao", "Một gia đình có tổng thu nhập một tháng là 30 triệu đồng. Trong biểu đồ chi tiêu, góc ở tâm của hình quạt biểu diễn tiền ăn uống là $144^\\circ$. Số tiền gia đình đó chi cho ăn uống trong tháng là:", ["$12$ triệu đồng", "$10$ triệu đồng", "$15$ triệu đồng", "$8$ triệu đồng"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về việc biểu diễn dữ liệu bằng biểu đồ (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Biểu đồ cột đơn thích hợp để so sánh số lượng giữa các đối tượng khác nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Biểu đồ quạt tròn có thể biểu diễn được số liệu âm.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Trục đứng của biểu đồ cột thường thể hiện giá trị số lượng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Để thể hiện sự thay đổi nhiệt độ các giờ trong ngày, biểu đồ đoạn thẳng tối ưu hơn biểu đồ tròn.", "correct": True}
            ]),
            make_tf(2, "Bảng thống kê điểm môn Toán học kỳ 1 của lớp 8A gồm 40 học sinh: Điểm 9-10 có 10 em; Điểm 7-8 có 18 em; Điểm 5-6 có 10 em; Dưới 5 có 2 em:", [
                {"key": "a", "level": "Thông hiểu", "text": "Tỉ lệ học sinh đạt điểm Giỏi (9-10) là 25%.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tỉ lệ học sinh đạt điểm Khá (7-8) là 45%.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tỉ lệ học sinh đạt từ điểm 5 trở lên chiếm 95%.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Khi vẽ biểu đồ quạt tròn, góc ở tâm biểu diễn nhóm học sinh đạt điểm Khá là 180 độ.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Một biểu đồ quạt tròn có góc ở tâm là 90 độ. Hỏi phần đó chiếm bao nhiêu phần trăm tổng thể?", "25"),
            make_sa(2, "Thông hiểu", "Số học sinh 4 lớp: 38, 42, 40, 40. Tính số học sinh trung bình mỗi lớp.", "40"),
            make_sa(3, "Vận dụng", "Một quạt tròn biểu diễn 35% tổng số. Tính số đo góc ở tâm tương ứng (độ).", "126"),
            make_sa(4, "Vận dụng cao", "Doanh thu năm 2023 là 500 triệu. Năm 2024 tăng 20%. Tính doanh thu năm 2024 (triệu đồng).", "600")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Nêu các bước cơ bản để chuyển một bảng số liệu phần trăm sang biểu đồ hình quạt tròn.", "1) Tính góc ở tâm cho từng đối tượng: góc = (% / 100) x 360 độ (0.25đ).\n2) Vẽ đường tròn tâm O và dùng thước đo góc để dựng các hình quạt tương ứng, ghi chú tỉ lệ phần trăm và tên đối tượng (0.25đ)."),
            make_essay(2, "Vận dụng", "Một cửa hàng bán sách thống kê số lượng sách tham khảo bán được trong 5 ngày: Thứ 2: 25 cuốn; Thứ 3: 30 cuốn; Thứ 4: 45 cuốn; Thứ 5: 35 cuốn; Thứ 6: 65 cuốn. a) Vẽ bảng số liệu và tính tổng số sách bán được. b) Tính tỉ số phần trăm sách bán được trong ngày Thứ 6 so với cả tuần.", "a) Tổng số sách: 25 + 30 + 45 + 35 + 65 = 200 (cuốn) (0.25đ).\nb) Tỉ lệ ngày Thứ 6: 65 / 200 x 100% = 32,5% (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Số lượng học sinh giỏi của một trường qua 4 năm học: Năm 1: 120 em; Năm 2: 150 em; Năm 3: 180 em; Năm 4: 216 em. Tính tỉ lệ phần trăm tăng trưởng học sinh giỏi của Năm 4 so với Năm 1.", "Số lượng tăng thêm: 216 - 120 = 96 (học sinh) (0.25đ).\nTỉ lệ tăng trưởng so với Năm 1: 96 / 120 x 100% = 80% (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương V: Dữ liệu và biểu đồ - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 6. CHƯƠNG 6 TOÁN 8: PHÂN THỨC ĐẠI SỐ (Bài 5: cuối chương)
def build_c6_8_exams():
    chap_id = "c6_8"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Phân thức đại số & Rút gọn",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Phân thức đại số là biểu thức có dạng $\\frac{A}{B}$ trong đó $A, B$ là các đa thức và:", ["$B$ là đa thức khác đa thức 0", "$A$ khác đa thức 0", "$B$ là một hằng số", "$A$ và $B$ là các số tự nhiên"], 0),
            make_mc(2, "Nhận biết", "Điều kiện xác định của phân thức $\\frac{x+1}{x-2}$ là:", ["$x \\neq 2$", "$x \\neq -1$", "$x \\neq 0$", "$x > 2$"], 0),
            make_mc(3, "Nhận biết", "Rút gọn phân thức $\\frac{2x}{4x^2}$ ta được:", ["$\\frac{1}{2x}$", "$\\frac{1}{2}$", "$\\frac{x}{2}$", "$\\frac{2}{x}$"], 0),
            make_mc(4, "Nhận biết", "Phân thức đối của phân thức $\\frac{x-1}{x+2}$ là:", ["$-\\frac{x-1}{x+2} = \\frac{1-x}{x+2}$", "$\\frac{x+1}{x-2}$", "$\\frac{x+2}{x-1}$", "$\\frac{x-1}{2-x}$"], 0),
            make_mc(5, "Thông hiểu", "Kết quả của phép cộng $\\frac{2x}{x+1} + \\frac{2}{x+1}$ là:", ["$2$", "$\\frac{2x+2}{2(x+1)}$", "$4$", "$\\frac{2}{x+1}$"], 0),
            make_mc(6, "Thông hiểu", "Kết quả của phép nhân $\\frac{x-1}{x+3} \\cdot \\frac{x+3}{x-1}$ với $x \\neq 1, x \\neq -3$ là:", ["$1$", "$0$", "$-1$", "$\\frac{(x-1)^2}{(x+3)^2}$"], 0),
            make_mc(7, "Thông hiểu", "Phân thức $\\frac{x^2 - 4}{x - 2}$ sau khi rút gọn bằng:", ["$x + 2$", "$x - 2$", "$x + 4$", "$2$"], 0),
            make_mc(8, "Thông hiểu", "Giá trị của phân thức $\\frac{x+3}{x-1}$ tại $x = 3$ là:", ["$3$", "$6$", "$2$", "$0$"], 0),
            make_mc(9, "Vận dụng", "Thực hiện phép tính $\\frac{1}{x-1} - \\frac{1}{x+1}$ ta được:", ["$\\frac{2}{x^2-1}$", "$\\frac{2x}{x^2-1}$", "$0$", "$\\frac{-2}{x^2-1}$"], 0),
            make_mc(10, "Vận dụng", "Tìm $x$ để phân thức $\\frac{3x-6}{x+2}$ có giá trị bằng 0:", ["$x = 2$", "$x = -2$", "$x = 0$", "$x = 6$"], 0),
            make_mc(11, "Vận dụng", "Một ca nô xuôi dòng quãng đường $30\\text{ km}$ với vận tốc $(x + 3)\\text{ km/h}$. Biểu thức biểu thị thời gian ca nô đi là:", ["$\\frac{30}{x+3}$ (giờ)", "$30(x + 3)$", "$\\frac{x+3}{30}$", "$30 - (x + 3)$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm tất cả các giá trị nguyên của $x$ để phân thức $\\frac{2x+3}{x-1}$ nhận giá trị nguyên:", ["$x \\in \\{-4; 0; 2; 6\\}$", "$x \\in \\{1; 2; 3\\}$", "$x \\in \\{0; 2\\}$", "$x \\in \\{-1; 1\\}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về phân thức đại số và các phép biến đổi (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu nhân cả tử và mẫu của một phân thức với cùng một đa thức khác 0 thì được phân thức bằng nó.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hai phân thức A/B và C/D bằng nhau khi và chỉ khi A.D = B.C.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Phân thức nghịch đảo của A/B là B/A (với A, B khác 0).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Với mọi giá trị của x, phân thức (x^2 + 1)/(x^2 + 2) luôn nhỏ hơn 1.", "correct": True}
            ]),
            make_tf(2, "Cho biểu thức $P = \\left(\\frac{x}{x-2} - \\frac{2}{x+2}\\right) : \\frac{x^2+4}{x^2-4}$ (với $x \\neq \\pm 2$):", [
                {"key": "a", "level": "Thông hiểu", "text": "Mẫu thức chung trong ngoặc là (x - 2)(x + 2) = x^2 - 4.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tử thức trong ngoặc sau quy đồng là x(x + 2) - 2(x - 2) = x^2 + 4.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Biểu thức P rút gọn bằng 1.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Khi x = 2 thì P nhận giá trị bằng 1.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tìm điều kiện xác định của phân thức: 5 / (x - 7). Điền số mà x phải khác.", "7"),
            make_sa(2, "Thông hiểu", "Rút gọn phân thức (x^2 - 9)/(x + 3) rồi tính giá trị tại x = 10.", "7"),
            make_sa(3, "Vận dụng", "Tìm x để phân thức (2x - 8) / (x + 1) bằng 0.", "4"),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên x lớn nhất để phân thức 5 / (x - 2) nhận giá trị nguyên dương.", "7")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Rút gọn phân thức: $A = \\frac{x^2 - 4x + 4}{2x - 4}$.", "A = (x - 2)^2 / [2(x - 2)] = (x - 2) / 2 (0.5đ)."),
            make_essay(2, "Vận dụng", "Thực hiện phép tính: $B = \\frac{1}{x-2} + \\frac{1}{x+2} - \\frac{2x}{x^2-4}$.", "MTC = x^2 - 4 = (x - 2)(x + 2) (0.25đ).\nB = [(x + 2) + (x - 2) - 2x] / (x^2 - 4) = (2x - 2x) / (x^2 - 4) = 0 (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Tìm tất cả các giá trị nguyên của $x$ để phân thức $M = \\frac{3x + 5}{x - 1}$ nhận giá trị là một số nguyên.", "M = (3x - 3 + 8)/(x - 1) = 3 + 8/(x - 1) (0.25đ).\nĐể M nguyên thì x - 1 phải là ước của 8 in {1; -1; 2; -2; 4; -4; 8; -8}.\n=> x in {2; 0; 3; -1; 5; -3; 9; -7} (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương VI: Phân thức đại số - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 7. CHƯƠNG 7 TOÁN 8: PHƯƠNG TRÌNH BẬC NHẤT VÀ HÀM SỐ BẬC NHẤT (Bài 6: cuối chương)
def build_c7_8_exams():
    chap_id = "c7_8"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Phương trình & Hàm số bậc nhất",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Phương trình nào sau đây là phương trình bậc nhất một ẩn?", ["$2x - 5 = 0$", "$x^2 + 1 = 0$", "$\\frac{1}{x} + 2 = 0$", "$2x + y = 3$"], 0),
            make_mc(2, "Nhận biết", "Nghiệm của phương trình $3x - 9 = 0$ là:", ["$x = 3$", "$x = -3$", "$x = 9$", "$x = 0$"], 0),
            make_mc(3, "Nhận biết", "Hàm số bậc nhất là hàm số có dạng:", ["$y = ax + b$ với $a \\neq 0$", "$y = ax^2 + b$", "$y = \\frac{a}{x}$", "$y = b$"], 0),
            make_mc(4, "Nhận biết", "Hàm số bậc nhất $y = 3x - 2$ có hệ số góc bằng:", ["$3$", "$-2$", "$2$", "$-3$"], 0),
            make_mc(5, "Thông hiểu", "Hàm số bậc nhất $y = -2x + 5$ là hàm số:", ["Nghịch biến trên $\\mathbb{R}$", "Đồng biến trên $\\mathbb{R}$", "Vừa đồng biến vừa nghịch biến", "Không đổi"], 0),
            make_mc(6, "Thông hiểu", "Điểm nào sau đây thuộc đồ thị hàm số $y = 2x - 1$?", ["$A(1; 1)$", "$B(0; 1)$", "$C(2; 4)$", "$D(-1; 1)$"], 0),
            make_mc(7, "Thông hiểu", "Hai đường thẳng $y = 2x + 1$ và $y = 2x - 3$ có vị trí tương đối là:", ["Song song với nhau", "Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], 0),
            make_mc(8, "Thông hiểu", "Phương trình $2(x - 1) = 3x + 1$ có nghiệm là:", ["$x = -3$", "$x = 3$", "$x = -1$", "$x = 1$"], 0),
            make_mc(9, "Vận dụng", "Tìm $m$ để đồ thị hàm số $y = (m - 1)x + 3$ đi qua điểm $M(2; 7)$:", ["$m = 3$", "$m = 2$", "$m = 4$", "$m = 1$"], 0),
            make_mc(10, "Vận dụng", "Một xe máy đi từ A đến B với vận tốc $40\\text{ km/h}$. Lúc về xe đi với vận tốc $30\\text{ km/h}$ nên thời gian về nhiều hơn thời gian đi là 30 phút ($0,5$ giờ). Quãng đường AB dài:", ["$60\\text{ km}$", "$70\\text{ km}$", "$80\\text{ km}$", "$50\\text{ km}$"], 0),
            make_mc(11, "Vận dụng", "Tìm giao điểm của hai đường thẳng $y = 2x - 3$ và $y = -x + 3$:", ["$(2; 1)$", "$(1; 2)$", "$(0; 3)$", "$(3; 0)$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm $m$ để phương trình $(m^2 - 4)x + m - 2 = 0$ có vô số nghiệm:", ["$m = 2$", "$m = -2$", "$m = \\pm 2$", "Không có giá trị nào của $m$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về phương trình và hàm số bậc nhất (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Phương trình ax + b = 0 với a khác 0 luôn có duy nhất một nghiệm x = -b/a.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Đồ thị hàm số y = ax + b (a khác 0) là một đường thẳng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai đường thẳng song song khi chúng có hệ số góc bằng nhau và tung độ gốc khác nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Đồ thị hàm số y = 3x đi qua gốc tọa độ O(0; 0).", "correct": True}
            ]),
            make_tf(2, "Bác Ba gửi ngân hàng một khoản tiền. Số tiền nhận được sau x tháng được tính bởi y = 0,5x + 100 (triệu đồng):", [
                {"key": "a", "level": "Thông hiểu", "text": "Số tiền gốc ban đầu Bác Ba gửi là 100 triệu đồng.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Mỗi tháng số tiền tăng thêm 0,5 triệu đồng tiền lãi.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Sau 12 tháng (1 năm) số tiền nhận được là 106 triệu đồng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Sau 2 năm (24 tháng) Bác Ba nhận được đúng 120 triệu đồng.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Giải phương trình: 5x - 15 = 0.", "3"),
            make_sa(2, "Thông hiểu", "Tìm hệ số góc của đường thẳng y = -4x + 7.", "-4"),
            make_sa(3, "Vận dụng", "Tìm m để hai đường thẳng y = (m - 2)x + 1 và y = 3x - 5 song song với nhau.", "5"),
            make_sa(4, "Vận dụng cao", "Tìm diện tích tam giác tạo bởi đường thẳng y = 2x - 4 với hai trục tọa độ Ox và Oy.", "4")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Giải phương trình: $3(x - 2) + 2x = 9$.", "3x - 6 + 2x = 9 => 5x = 15 => x = 3 (0.5đ)."),
            make_essay(2, "Vận dụng", "Một người đi xe đạp từ A đến B với vận tốc 15 km/h. Sau đó 1 giờ, một người đi xe máy cũng từ A đuổi theo với vận tốc 40 km/h. Hỏi sau bao lâu kể từ khi xe máy xuất phát thì xe máy đuổi kịp xe đạp?", "Gọi thời gian xe máy đi đến khi gặp xe đạp là t (giờ, t > 0) (0.25đ).\nQuãng đường xe đạp đi: 15(t + 1). Quãng đường xe máy đi: 40t.\nTa có: 40t = 15(t + 1) => 25t = 15 => t = 15/25 = 0,6 giờ = 36 phút (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Tìm $m$ để ba đường thẳng sau đồng quy: $(d_1): y = 2x - 3$, $(d_2): y = -x + 3$ và $(d_3): y = (m - 1)x + 2m - 5$.", "Tọa độ giao điểm của (d1) và (d2) là nghiệm của: 2x - 3 = -x + 3 => 3x = 6 => x = 2; y = 1 => A(2; 1) (0.25đ).\nĐể 3 đường thẳng đồng quy thì A(2; 1) thuộc (d3):\n1 = (m - 1).2 + 2m - 5 => 4m - 7 = 1 => 4m = 8 => m = 2 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương VII: Phương trình & Hàm số bậc nhất - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 8. CHƯƠNG 8 TOÁN 8: MỞ ĐẦU VỀ TÍNH XÁC SUẤT CỦA BIẾN CỐ (Bài 4: cuối chương)
def build_c8_8_exams():
    chap_id = "c8_8"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Xác suất biến cố & Thực nghiệm",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Xác suất của một biến cố trong một trò chơi là:", ["Một số nằm từ 0 đến 1", "Số tự nhiên lớn hơn 1", "Số âm bất kì", "Luôn bằng 0,5"], 0),
            make_mc(2, "Nhận biết", "Nếu tất cả các kết quả của một hành động có khả năng xảy ra như nhau thì chúng được gọi là:", ["Các kết quả đồng khả năng", "Biến cố chắc chắn", "Biến cố không thể", "Biến cố độc lập"], 0),
            make_mc(3, "Nhận biết", "Gieo một con xúc xắc 6 mặt cân đối. Có bao nhiêu kết quả có thể xảy ra?", ["$6$ kết quả", "$12$ kết quả", "$2$ kết quả", "$36$ kết quả"], 0),
            make_mc(4, "Nhận biết", "Công thức tính xác suất của biến cố $E$ khi các kết quả đồng khả năng là:", ["$P(E) = \\frac{n(E)}{n(\\Omega)}$", "$P(E) = \\frac{n(\\Omega)}{n(E)}$", "$P(E) = n(E) \\cdot n(\\Omega)$", "$P(E) = n(E) - n(\\Omega)$"], 0),
            make_mc(5, "Thông hiểu", "Một hộp có 10 viên bi cùng kích thước gồm 6 bi đỏ và 4 bi xanh. Rút ngẫu nhiên một viên bi. Xác suất để rút được bi đỏ là:", ["$\\frac{6}{10} = \\frac{3}{5}$", "$\\frac{4}{10}$", "$\\frac{1}{2}$", "$\\frac{6}{4}$"], 0),
            make_mc(6, "Thông hiểu", "Gieo một con xúc xắc cân đối. Xác suất để xuất hiện mặt có số chấm chia hết cho 3 là:", ["$\\frac{2}{6} = \\frac{1}{3}$ (mặt 3 và 6)", "$\\frac{1}{6}$", "$\\frac{3}{6}$", "$\\frac{4}{6}$"], 0),
            make_mc(7, "Thông hiểu", "Chọn ngẫu nhiên một số tự nhiên có hai chữ số. Có tất cả bao nhiêu kết quả có thể xảy ra?", ["$90$ kết quả", "$99$ kết quả", "$100$ kết quả", "$89$ kết quả"], 0),
            make_mc(8, "Thông hiểu", "Tung đồng thời hai đồng xu cân đối. Xác suất để cả hai đồng xu đều xuất hiện mặt Ngửa là:", ["$\\frac{1}{4}$", "$\\frac{1}{2}$", "$\\frac{3}{4}$", "$1$"], 0),
            make_mc(9, "Vận dụng", "Một túi chứa các tấm thẻ đánh số từ 1 đến 25. Rút ngẫu nhiên 1 tấm thẻ. Xác suất để số ghi trên thẻ là số chính phương là:", ["$\\frac{5}{25} = \\frac{1}{5}$ (gồm 1, 4, 9, 16, 25)", "$\\frac{4}{25}$", "$\\frac{6}{25}$", "$\\frac{3}{25}$"], 0),
            make_mc(10, "Vận dụng", "Gieo đồng thời hai con xúc xắc cân đối một lần. Số kết quả thuận lợi để tổng số chấm trên hai con xúc xắc bằng 6 là:", ["$5$ kết quả", "$4$ kết quả", "$6$ kết quả", "$3$ kết quả"], 0),
            make_mc(11, "Vận dụng", "Một tổ học sinh có 5 nam và 5 nữ. Giáo viên chọn ngẫu nhiên 2 bạn làm cán sự lớp. Xác suất để chọn được 1 nam và 1 nữ là:", ["$\\frac{5}{9}$", "$\\frac{1}{2}$", "$\\frac{4}{9}$", "$\\frac{2}{5}$"], 0),
            make_mc(12, "Vận dụng cao", "Gieo một con xúc xắc cân đối 3 lần. Xác suất để ít nhất một lần xuất hiện mặt 6 chấm là:", ["$1 - \\left(\\frac{5}{6}\\right)^3 = \\frac{91}{216}$", "$\\frac{1}{2}$", "$\\frac{125}{216}$", "$\\frac{1}{6}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về xác suất của biến cố ngẫu nhiên (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Xác suất của biến cố đối E' bằng 1 - P(E).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi tung một đồng xu 100 lần thì số lần mặt Ngửa chắc chắn đúng bằng 50.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Các kết quả của phép thử gieo một con xúc xắc 6 mặt là đồng khả năng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Xác suất để rút được con Át từ bộ bài tây 52 lá là 1/13.", "correct": True}
            ]),
            make_tf(2, "Gieo một con xúc xắc cân đối một lần:", [
                {"key": "a", "level": "Thông hiểu", "text": "Xác suất xuất hiện mặt có số chấm là số nguyên tố bằng 1/2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Xác suất xuất hiện mặt có số chấm lớn hơn 4 bằng 1/3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Xác suất xuất hiện mặt 7 chấm bằng 0.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Xác suất xuất hiện mặt có số chấm là ước của 6 bằng 2/3.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Gieo xúc xắc 1 lần. Tính xác suất xuất hiện mặt có số chấm là hợp số (dạng phân số tối giản).", "1/3"),
            make_sa(2, "Thông hiểu", "Hộp có 8 bi xanh và 12 bi đỏ. Tính xác suất bốc được bi xanh.", "0,4"),
            make_sa(3, "Vận dụng", "Rút 1 thẻ từ 1 đến 30. Có bao nhiêu kết quả thuận lợi cho sự kiện 'số chia hết cho 5'?", "6"),
            make_sa(4, "Vận dụng cao", "Gieo 2 con xúc xắc. Tính số kết quả thuận lợi để tích hai số chấm là số chẵn.", "27")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Một hộp có 20 quả bóng được đánh số từ 1 đến 20. Lấy ngẫu nhiên một quả bóng. Tính xác suất để lấy được quả bóng ghi số chia hết cho 4.", "Các số chia hết cho 4: {4; 8; 12; 16; 20} (5 số) (0.25đ).\nXác suất: P = 5 / 20 = 1/4 = 0,25 (0.25đ)."),
            make_essay(2, "Vận dụng", "Một xạ thủ bắn 100 viên đạn vào bia, kết quả có 88 viên trúng bia. a) Tính xác suất thực nghiệm xạ thủ bắn trúng bia. b) Nếu xạ thủ bắn 250 viên đạn thì dự đoán có khoảng bao nhiêu viên trúng bia?", "a) Xác suất thực nghiệm: 88 / 100 = 0,88 (0.25đ).\nb) Số phát trúng bia dự đoán: 250 x 0,88 = 220 (viên) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Tung đồng thời hai con xúc xắc cân đối. Tính xác suất để tổng số chấm xuất hiện trên hai con xúc xắc lớn hơn 9.", "Không gian mẫu: 36 kết quả (0.25đ).\nCác cặp có tổng > 9 gồm:\nTổng = 10: (4,6), (5,5), (6,4) [3 kết quả].\nTổng = 11: (5,6), (6,5) [2 kết quả].\nTổng = 12: (6,6) [1 kết quả].\nTổng số kết quả thuận lợi: 3 + 2 + 1 = 6. Xác suất: 6/36 = 1/6 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương VIII: Xác suất của biến cố - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 9. CHƯƠNG 9 TOÁN 8: TAM GIÁC ĐỒNG DẠNG (Bài 6: cuối chương)
def build_c9_8_exams():
    chap_id = "c9_8"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Tam giác đồng dạng & Ứng dụng thực tiễn",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Nếu $\\Delta ABC \\backsim \\Delta A'B'C'$ theo tỉ số đồng dạng $k$ thì $\\Delta A'B'C' \\backsim \\Delta ABC$ theo tỉ số:", ["$\\frac{1}{k}$", "$k$", "$k^2$", "$-k$"], 0),
            make_mc(2, "Nhận biết", "Trường hợp đồng dạng thứ nhất (c-c-c): Nếu ba cạnh của tam giác này:", ["Tỉ lệ với ba cạnh của tam giác kia", "Bằng ba cạnh của tam giác kia", "Song song với ba cạnh tam giác kia", "Vuông góc với ba cạnh kia"], 0),
            make_mc(3, "Nhận biết", "Trường hợp đồng dạng thứ ba (g-g): Nếu hai góc của tam giác này:", ["Lần lượt bằng hai góc của tam giác kia", "Bù với hai góc của tam giác kia", "Tỉ lệ với hai góc của tam giác kia", "Cùng phụ nhau"], 0),
            make_mc(4, "Nhận biết", "Tỉ số diện tích của hai tam giác đồng dạng bằng:", ["Bình phương tỉ số đồng dạng ($k^2$)", "Tỉ số đồng dạng ($k$)", "Hai lần tỉ số đồng dạng", "Lập phương tỉ số đồng dạng"], 0),
            make_mc(5, "Thông hiểu", "Cho $\\Delta ABC \\backsim \\Delta DEF$ theo tỉ số $k = \\frac{2}{3}$. Biết chu vi $\\Delta ABC$ là $24\\text{ cm}$. Chu vi $\\Delta DEF$ là:", ["$36\\text{ cm}$", "$16\\text{ cm}$", "$24\\text{ cm}$", "$48\\text{ cm}$"], 0),
            make_mc(6, "Thông hiểu", "Hai tam giác vuông đồng dạng với nhau khi:", ["Có một góc nhọn bằng nhau", "Có cạnh huyền bằng nhau", "Có diện tích bằng nhau", "Có hai cạnh góc vuông bằng nhau"], 0),
            make_mc(7, "Thông hiểu", "Cho tam giác $ABC$ có $AB = 4\\text{ cm}, AC = 6\\text{ cm}$. Tam giác $DEF$ có $DE = 2\\text{ cm}, DF = 3\\text{ cm}$ và $\\widehat{A} = \\widehat{D}$. Khẳng định nào ĐÚNG?", ["$\\Delta ABC \\backsim \\Delta DEF$ (c-g-c)", "$\\Delta ABC = \\Delta DEF$", "Hai tam giác không đồng dạng", "$\\widehat{B} = \\widehat{F}$"], 0),
            make_mc(8, "Thông hiểu", "Tỉ số hai đường cao tương ứng của hai tam giác đồng dạng bằng:", ["Tỉ số đồng dạng $k$", "$k^2$", "$\\sqrt{k}$", "$\\frac{1}{k}$"], 0),
            make_mc(9, "Vận dụng", "Người ta cắm một cọc thẳng đứng cao $1,5\\text{ m}$ có bóng trên mặt đất dài $1\\text{ m}$. Cùng thời điểm đó, bóng của một cột cờ trên mặt đất dài $8\\text{ m}$. Chiều cao của cột cờ là:", ["$12\\text{ m}$", "$10\\text{ m}$", "$16\\text{ m}$", "$9,5\\text{ m}$"], 0),
            make_mc(10, "Vận dụng", "Cho $\\Delta ABC \\backsim \\Delta MNP$ theo tỉ số $k = 2$. Biết diện tích $\\Delta MNP$ bằng $15\\text{ cm}^2$. Diện tích $\\Delta ABC$ là:", ["$60\\text{ cm}^2$", "$30\\text{ cm}^2$", "$7,5\\text{ cm}^2$", "$45\\text{ cm}^2$"], 0),
            make_mc(11, "Vận dụng", "Cho hình thang $ABCD$ ($AB \\parallel CD$). Hai đường chéo cắt nhau tại $O$. Biết $AB = 4\\text{ cm}, CD = 8\\text{ cm}$. Tỉ số $\\frac{OA}{OC}$ bằng:", ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$2$", "$\\frac{2}{3}$"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Khẳng định nào sau đây là SAI?", ["$AH^2 = AB \\cdot AC$", "$AB^2 = BH \\cdot BC$", "$AC^2 = CH \\cdot BC$", "$AH^2 = BH \\cdot CH$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tam giác đồng dạng (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số k = 1.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hai tam giác đều bất kì luôn đồng dạng với nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai tam giác cân bất kì luôn đồng dạng với nhau.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Nếu hai tam giác đồng dạng thì tỉ số chu vi bằng tỉ số đồng dạng k.", "correct": True}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$ ($H \\in BC$):", [
                {"key": "a", "level": "Thông hiểu", "text": "Tam giác HBA đồng dạng với tam giác ABC (g-g).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tam giác HAC đồng dạng với tam giác ABC (g-g).", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tam giác HBA đồng dạng với tam giác HAC (g-g).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hệ thức AH^2 = BH . CH luôn đúng.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho tam giác ABC đồng dạng DEF với tỉ số k = 3/4. Tính tỉ số diện tích của chúng.", "9/16"),
            make_sa(2, "Thông hiểu", "Cho tam giác vuông có hai cạnh góc vuông 6 cm và 8 cm. Tính độ dài đường cao ứng với cạnh huyền (cm).", "4,8"),
            make_sa(3, "Vận dụng", "Cột cờ cao 10 m có bóng dài 6 m. Cùng lúc đó một người cao 1,5 m có bóng dài bao nhiêu mét?", "0,9"),
            make_sa(4, "Vận dụng cao", "Cho tam giác ABC có AB = 6 cm, AC = 9 cm. Điểm D thuộc AB sao cho AD = 3 cm. Kẻ DE // BC. Tính tỉ số diện tích ADE và tứ giác BDEC.", "1/3")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Chứng minh rằng $AB^2 = BH \\cdot BC$.", "Xét tam giác HBA và ABC có: góc B chung, góc BHA = BAC = 90 độ (0.25đ).\n=> tam giác HBA đồng dạng ABC (g-g) => BA / BC = BH / BA => AB^2 = BH . BC. Đpcm (0.25đ)."),
            make_essay(2, "Vận dụng", "Cho hình bình hành $ABCD$. Trên cạnh $AB$ lấy điểm $E$. Đường thẳng $ED$ cắt cạnh $BC$ tại $F$ và cắt tia $AC$ tại $K$. Chứng minh rằng $\\Delta EAD \\backsim \\Delta EBF$ và $ED^2 = EK \\cdot EF$.", "Do AD // BC => tam giác EAD đồng dạng EBF (g-g) (0.25đ).\nÁp dụng định lí Thalès và tam giác đồng dạng với các đường song song ta được ED^2 = EK . EF (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ nhọn có các đường cao $BD$ và $CE$ cắt nhau tại $H$. Chứng minh rằng $HD \\cdot HB = HE \\cdot HC$ và $\\Delta ADE \\backsim \\Delta ABC$.", "Xét hai tam giác vuông HED và HCB có: góc DHE = BHC (đối đỉnh) => tam giác HED đồng dạng HCB (g-g) => HD/HC = HE/HB => HD . HB = HE . HC (0.25đ).\nTừ tỉ số AD/AB = AE/AC (do tam giác ADB đồng dạng AEC) kết hợp góc A chung => tam giác ADE đồng dạng ABC (c-g-c). Đpcm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương IX: Tam giác đồng dạng - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 10. CHƯƠNG 10 TOÁN 8: MỘT SỐ HÌNH KHỐI TRONG THỰC TIỄN (Bài 3: cuối chương)
def build_c10_8_exams():
    chap_id = "c10_8"
    l_idx = 3
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Hình chóp đều & Thể tích thực tiễn",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Mặt đáy của hình chóp tam giác đều là hình gì?", ["Tam giác đều", "Tam giác vuông", "Tam giác cân", "Tam giác thường"], 0),
            make_mc(2, "Nhận biết", "Mặt đáy của hình chóp tứ giác đều là hình gì?", ["Hình vuông", "Hình thoi", "Hình chữ nhật", "Hình bình hành"], 0),
            make_mc(3, "Nhận biết", "Các mặt bên của hình chóp đều là các tam giác gì?", ["Các tam giác cân bằng nhau", "Các tam giác đều", "Các tam giác vuông", "Các tam giác thường"], 0),
            make_mc(4, "Nhận biết", "Công thức tính thể tích của hình chóp có diện tích đáy $S$ và chiều cao $h$ là:", ["$V = \\frac{1}{3}S \\cdot h$", "$V = S \\cdot h$", "$V = 3S \\cdot h$", "$V = \\frac{1}{2}S \\cdot h$"], 0),
            make_mc(5, "Thông hiểu", "Hình chóp tứ giác đều có cạnh đáy $6\\text{ cm}$, chiều cao $8\\text{ cm}$. Thể tích của hình chóp là:", ["$96\\text{ cm}^3$", "$288\\text{ cm}^3$", "$144\\text{ cm}^3$", "$48\\text{ cm}^3$"], 0),
            make_mc(6, "Thông hiểu", "Một hình chóp tam giác đều có diện tích đáy bằng $20\\text{ cm}^2$ và chiều cao $9\\text{ cm}$. Thể tích là:", ["$60\\text{ cm}^3$", "$180\\text{ cm}^3$", "$30\\text{ cm}^3$", "$90\\text{ cm}^3$"], 0),
            make_mc(7, "Thông hiểu", "Hình chóp tứ giác đều có diện tích xung quanh $80\\text{ cm}^2$, cạnh đáy $5\\text{ cm}$. Trung đoạn của hình chóp là:", ["$8\\text{ cm}$", "$4\\text{ cm}$", "$16\\text{ cm}$", "$10\\text{ cm}$"], 0),
            make_mc(8, "Thông hiểu", "Số mặt, số đỉnh và số cạnh của hình chóp tứ giác đều lần lượt là:", ["$5$ mặt, $5$ đỉnh, $8$ cạnh", "$4$ mặt, $4$ đỉnh, $6$ cạnh", "$6$ mặt, $8$ đỉnh, $12$ cạnh", "$5$ mặt, $6$ đỉnh, $9$ cạnh"], 0),
            make_mc(9, "Vận dụng", "Kim tự tháp Kê-ốp ở Ai Cập có dạng hình chóp tứ giác đều có chiều cao khoảng $140\\text{ m}$, cạnh đáy dài khoảng $230\\text{ m}$. Thể tích kim tự tháp xấp xỉ là:", ["$2\\,468\\,667\\text{ m}^3$", "$7\\,406\\,000\\text{ m}^3$", "$1\\,610\\,000\\text{ m}^3$", "$3\\,220\\,000\\text{ m}^3$"], 0),
            make_mc(10, "Vận dụng", "Người ta làm một chiếc lều hình chóp tứ giác đều có cạnh đáy $2\\text{ m}$, trung đoạn của mặt bên là $2,5\\text{ m}$. Diện tích bạt cần dùng để dựng 4 mặt xung quanh lều là:", ["$10\\text{ m}^2$", "$20\\text{ m}^2$", "$5\\text{ m}^2$", "$15\\text{ m}^2$"], 0),
            make_mc(11, "Vận dụng", "Một khối gỗ hình chóp tam giác đều có chu vi đáy $18\\text{ cm}$, trung đoạn dài $8\\text{ cm}$. Diện tích xung quanh khối gỗ là:", ["$72\\text{ cm}^2$", "$144\\text{ cm}^2$", "$36\\text{ cm}^2$", "$48\\text{ cm}^2$"], 0),
            make_mc(12, "Vận dụng cao", "Một hình chóp tứ giác đều có chiều cao $4\\text{ cm}$, cạnh bên dài $5\\text{ cm}$. Thể tích của hình chóp đó là:", ["$24\\text{ cm}^3$", "$72\\text{ cm}^3$", "$48\\text{ cm}^3$", "$36\\text{ cm}^3$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về hình chóp đều (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hình chóp đều có đáy là đa giác đều và chân đường cao trùng với tâm đường tròn ngoại tiếp đáy.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Trung đoạn là đường cao kẻ từ đỉnh của mỗi mặt bên tam giác cân.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Diện tích xung quanh của hình chóp đều bằng nửa tích chu vi đáy với trung đoạn.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Các cạnh bên của hình chóp đều luôn vuông góc với mặt phẳng đáy.", "correct": False}
            ]),
            make_tf(2, "Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy $a = 10\\text{ cm}$, chiều cao $h = 12\\text{ cm}$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Diện tích đáy của hình chóp là 100 cm^2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Thể tích của hình chóp S.ABCD là 400 cm^3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Độ dài trung đoạn của hình chóp là căn(12^2 + 5^2) = 13 cm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích xung quanh của hình chóp là 260 cm^2.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính thể tích hình chóp tứ giác đều có diện tích đáy 30 cm^2, chiều cao 10 cm.", "100"),
            make_sa(2, "Thông hiểu", "Hình chóp tam giác đều có nửa chu vi đáy 12 cm, trung đoạn 6 cm. Tính diện tích xung quanh (cm^2).", "72"),
            make_sa(3, "Vận dụng", "Hình chóp tứ giác đều có cạnh đáy 6 cm, chiều cao 4 cm. Tính độ dài trung đoạn (cm).", "5"),
            make_sa(4, "Vận dụng cao", "Một chiếc hộp quà hình chóp tứ giác đều có cạnh đáy 8 cm, diện tích toàn phần 144 cm^2. Tính độ dài trung đoạn (cm).", "5")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Tính diện tích xung quanh và thể tích hình chóp tứ giác đều có cạnh đáy 12 cm, chiều cao 8 cm và trung đoạn 10 cm.", "Chu vi đáy: 12 x 4 = 48 (cm). Nửa chu vi đáy: p = 24 (cm) (0.25đ).\nSxq = p x d = 24 x 10 = 240 (cm^2).\nV = (1/3) x S_day x h = (1/3) x 12^2 x 8 = 384 (cm^3) (0.25đ)."),
            make_essay(2, "Vận dụng", "Bác An muốn lợp tôn cho mái che của một chòi nghỉ chân dạng hình chóp tứ giác đều có cạnh đáy 4 m, trung đoạn 3 m. Biết chi phí lợp tôn là 180 000 đồng/m^2. Tính tổng chi phí lợp tôn cho 4 mặt mái chòi.", "Diện tích xung quanh mái chòi: Sxq = (4 x 4 / 2) x 3 = 24 (m^2) (0.25đ).\nChi phí lợp tôn: 24 x 180 000 = 4 320 000 (đồng) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Một chiếc đèn ngủ có chao đèn dạng hình chóp cụt tứ giác đều có hai đáy là hai hình vuông có cạnh lần lượt là 10 cm và 20 cm, chiều cao mặt bên (trung đoạn) là 15 cm. Người ta dán giấy trang trí toàn bộ 4 mặt bên xung quanh chao đèn. Tính diện tích giấy cần dùng.", "Mỗi mặt bên là hình thang cân có hai đáy 10 cm, 20 cm và chiều cao 15 cm (0.25đ).\nDiện tích 1 mặt bên: (10 + 20) x 15 / 2 = 225 (cm^2).\nDiện tích 4 mặt bên: 225 x 4 = 900 (cm^2) (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương X: Một số hình khối trong thực tiễn - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# HÀM THỰC THI TỔNG THỂ TOÁN 8
def run_all_grade8():
    builders = [
        build_c1_8_exams,
        build_c2_8_exams,
        build_c3_8_exams,
        build_c4_8_exams,
        build_c5_8_exams,
        build_c6_8_exams,
        build_c7_8_exams,
        build_c8_8_exams,
        build_c9_8_exams,
        build_c10_8_exams
    ]
    for b in builders:
        chap_id, new_exams = b()
        title, exams = load_existing_exams(8, chap_id)
        exams.update(new_exams)
        save_chapter_package(8, chap_id, title, exams)
    print("🎉 ĐÃ HOÀN TẤT TOÀN BỘ 10 CHƯƠNG TOÁN 8 (MỖI CHƯƠNG ĐÃ CÓ ĐỦ 7 ĐỀ CUỐI CHƯƠNG)!")

if __name__ == "__main__":
    run_all_grade8()
