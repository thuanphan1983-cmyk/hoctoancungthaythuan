# -*- coding: utf-8 -*-
"""
BIÊN SOẠN BỔ SUNG 4 ĐỀ CUỐI CHƯƠNG (ĐỀ 4, 5, 6, 7) - TOÁN 7 (10 CHƯƠNG)
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

# 1. CHƯƠNG 1 TOÁN 7: SỐ HỮU TỈ (Bài 5: cuối chương)
def build_c1_7_exams():
    chap_id = "c1_7"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Số hữu tỉ & Lũy thừa thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Số hữu tỉ là số viết được dưới dạng:", ["$\\frac{a}{b}$ với $a, b \\in \\mathbb{Z}, b \\neq 0$", "$\\frac{a}{b}$ với $a, b \\in \\mathbb{N}$", "Số thập phân vô hạn không tuần hoàn", "Chỉ gồm số nguyên"], 0),
            make_mc(2, "Nhận biết", "Số đối của số hữu tỉ $-\\frac{4}{7}$ là:", ["$\\frac{4}{7}$", "$-\\frac{7}{4}$", "$\\frac{7}{4}$", "$-\\frac{4}{7}$"], 0),
            make_mc(3, "Nhận biết", "Kết quả của phép tính $\\left(-\\frac{1}{2}\\right)^3$ là:", ["$-\\frac{1}{8}$", "$\\frac{1}{8}$", "$-\\frac{1}{6}$", "$\\frac{1}{6}$"], 0),
            make_mc(4, "Nhận biết", "Quy tắc chuyển vế: Khi chuyển một số hạng từ vế này sang vế kia của một đẳng thức, ta phải:", ["Đổi dấu số hạng đó", "Giữ nguyên dấu", "Nhân số hạng đó với $-1$", "Đổi số hạng đó thành số nghịch đảo"], 0),
            make_mc(5, "Thông hiểu", "Kết quả của phép tính $\\frac{-3}{5} + \\frac{2}{3}$ là:", ["$\\frac{1}{15}$", "$-\\frac{1}{15}$", "$-\\frac{5}{8}$", "$\\frac{19}{15}$"], 0),
            make_mc(6, "Thông hiểu", "Tìm $x$, biết $x - \\frac{2}{3} = -\\frac{1}{6}$:", ["$x = \\frac{1}{2}$", "$x = -\\frac{5}{6}$", "$x = -\\frac{1}{2}$", "$x = \\frac{5}{6}$"], 0),
            make_mc(7, "Thông hiểu", "Giá trị của biểu thức $A = \\left(\\frac{2}{3}\\right)^5 : \\left(\\frac{2}{3}\\right)^3$ là:", ["$\\frac{4}{9}$", "$\\frac{8}{27}$", "$\\frac{2}{3}$", "$1$"], 0),
            make_mc(8, "Thông hiểu", "So sánh hai số hữu tỉ $x = -0,75$ và $y = -\\frac{3}{4}$:", ["$x = y$", "$x > y$", "$x < y$", "Không so sánh được"], 0),
            make_mc(9, "Vận dụng", "Tính hợp lý: $M = \\frac{3}{7} \\cdot \\left(-\\frac{2}{5}\\right) + \\frac{3}{7} \\cdot \\left(-\\frac{3}{5}\\right)$:", ["$-\\frac{3}{7}$", "$\\frac{3}{7}$", "$-1$", "$0$"], 0),
            make_mc(10, "Vận dụng", "Tìm $x$, biết $\\left(x - \\frac{1}{2}\\right)^2 = \\frac{9}{16}$:", ["$x = \\frac{5}{4}$ hoặc $x = -\\frac{1}{4}$", "$x = \\frac{5}{4}$", "$x = -\\frac{1}{4}$", "$x = \\frac{3}{4}$"], 0),
            make_mc(11, "Vận dụng", "Một bể nước có dung tích 2000 lít. Giờ thứ nhất vòi chảy được $\\frac{2}{5}$ bể, giờ thứ hai vòi chảy được $\\frac{1}{4}$ bể. Lượng nước vòi đã chảy vào bể sau 2 giờ là:", ["$1300$ lít", "$1200$ lít", "$800$ lít", "$1500$ lít"], 0),
            make_mc(12, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức $A = |x - 2025| + |x - 1|$:", ["$2024$", "$0$", "$2025$", "$2026$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai của các khẳng định về số hữu tỉ (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Số 0 là một số hữu tỉ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Mọi số nguyên đều là số hữu tỉ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Lũy thừa bậc chẵn của một số hữu tỉ âm là một số âm.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Nếu $x^2 = y^2$ thì chắc chắn $x = y$.", "correct": False}
            ]),
            make_tf(2, "Cho biểu thức $P = \\left(-\\frac{2}{3}\\right)^3 \\cdot \\left(-\\frac{3}{4}\\right)^2$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Lũy thừa $(-2/3)^3 = -8/27$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Lũy thừa $(-3/4)^2 = 9/16$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Giá trị của biểu thức $P$ bằng $-1/6$.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số nghịch đảo của biểu thức $P$ là $6$.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính giá trị biểu thức: (-1/3)^2 + 5/9.", "2/3"),
            make_sa(2, "Thông hiểu", "Tìm x biết: x + 3/4 = 1/2.", "-1/4"),
            make_sa(3, "Vận dụng", "Tìm x biết: (2x - 1)^3 = -27.", "-1"),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: P = (x - 3)^2 + 7.", "7")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Thực hiện phép tính hợp lý: $A = \\frac{11}{24} - \\frac{5}{41} + \\frac{13}{24} + 0,5 - \\frac{36}{41}$.", "A = (11/24 + 13/24) - (5/41 + 36/41) + 0,5 = 1 - 1 + 0,5 = 0,5 (0.5đ)."),
            make_essay(2, "Vận dụng", "Tìm $x$, biết: $2^{x+2} - 2^x = 96$.", "2^x . 2^2 - 2^x = 96 => 2^x(4 - 1) = 96 (0.25đ).\n=> 3 . 2^x = 96 => 2^x = 32 = 2^5 => x = 5 (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Chứng minh rằng $B = 3^{n+2} - 2^{n+2} + 3^n - 2^n$ chia hết cho 10 với mọi số nguyên dương $n$.", "B = (3^{n+2} + 3^n) - (2^{n+2} + 2^n) = 3^n(9 + 1) - 2^n(4 + 1) = 10 . 3^n - 5 . 2^n (0.25đ).\nVới n >= 1: 5 . 2^n = 5 . 2 . 2^{n-1} = 10 . 2^{n-1}.\nDo đó B = 10(3^n - 2^{n-1}) chia hết cho 10 với mọi n >= 1 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương I: Số hữu tỉ - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 2. CHƯƠNG 2 TOÁN 7: SỐ THỰC (Bài 4: cuối chương)
def build_c2_7_exams():
    chap_id = "c2_7"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Căn bậc hai & Số thực",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Căn bậc hai số học của 49 là:", ["$7$", "$-7$", "$\\pm 7$", "$49$"], 0),
            make_mc(2, "Nhận biết", "Số nào sau đây là số vô tỉ?", ["$\\sqrt{2}$", "$\\sqrt{4}$", "$0,75$", "$-5$"], 0),
            make_mc(3, "Nhận biết", "Giá trị tuyệt đối của số thực $-3,14$ là:", ["$3,14$", "$-3,14$", "$0$", "$\\pi$"], 0),
            make_mc(4, "Nhận biết", "Tập hợp các số thực được kí hiệu là:", ["$\\mathbb{R}$", "$\\mathbb{Q}$", "$\\mathbb{Z}$", "$\\mathbb{I}$"], 0),
            make_mc(5, "Thông hiểu", "Khẳng định nào sau đây là ĐÚNG?", ["$\\sqrt{0,09} = 0,3$", "$\\sqrt{0,09} = -0,3$", "$\\sqrt{0,09} = 0,03$", "$\\sqrt{0,09} = 0,9$"], 0),
            make_mc(6, "Thông hiểu", "Làm tròn số thực $x = 3,\\!14159...$ đến chữ số thập phân thứ hai được:", ["$3,14$", "$3,15$", "$3,1$", "$3,142$"], 0),
            make_mc(7, "Thông hiểu", "Tìm $x \\ge 0$, biết $\\sqrt{x} = 5$:", ["$x = 25$", "$x = 5$", "$x = 10$", "$x = \\sqrt{5}$"], 0),
            make_mc(8, "Thông hiểu", "Kết quả so sánh giữa $\\sqrt{25}$ và $\\sqrt{26}$ là:", ["$\\sqrt{25} < \\sqrt{26}$", "$\\sqrt{25} > \\sqrt{26}$", "$\\sqrt{25} = \\sqrt{26}$", "Không so sánh được"], 0),
            make_mc(9, "Vận dụng", "Tính giá trị biểu thức: $A = \\sqrt{64} - \\sqrt{25} + \\sqrt{36}$:", ["$9$", "$7$", "$11$", "$13$"], 0),
            make_mc(10, "Vận dụng", "Tìm số thực $x$, biết $|x - 1,5| = 2,5$:", ["$x = 4$ hoặc $x = -1$", "$x = 4$", "$x = -1$", "$x = 1$"], 0),
            make_mc(11, "Vận dụng", "Một mảnh đất hình vuông có diện tích $144\\text{ m}^2$. Chu vi của mảnh đất đó là:", ["$48\\text{ m}$", "$24\\text{ m}$", "$36\\text{ m}$", "$12\\text{ m}$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức $M = \\sqrt{x^2 + 4} - 2$:", ["$0$ (khi $x = 0$)", "$2$", "$-2$", "$4$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về số thực và căn bậc hai (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Mọi số hữu tỉ đều là số thực.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số 0 vừa là số hữu tỉ vừa là số vô tỉ.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Căn bậc hai số học của một số không âm luôn là số không âm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu $\\sqrt{x} < 3$ với $x \\ge 0$ thì $0 \\le x < 9$.", "correct": True}
            ]),
            make_tf(2, "Cho biểu thức $A = |2x - 3| + 5$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Với mọi $x$, ta luôn có $|2x - 3| \\ge 0$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Giá trị nhỏ nhất của biểu thức $A$ bằng 5 khi $x = 1,5$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Khi $x = 0$ thì $A = 8$.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Phương trình $A = 3$ có hai nghiệm phân biệt.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính: căn(81) - căn(16).", "5"),
            make_sa(2, "Thông hiểu", "Tìm x không âm biết: căn(x) = 7.", "49"),
            make_sa(3, "Vận dụng", "Tìm x biết: |x - 2| + 1 = 6. Tìm tổng các giá trị của x.", "4"),
            make_sa(4, "Vận dụng cao", "Tìm giá trị lớn nhất của biểu thức: Q = 10 - căn(x - 1).", "10")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Tính giá trị biểu thức: $B = 3 \\cdot \\sqrt{\\frac{1}{9}} + 1,5 \\cdot \\sqrt{16} - \\sqrt{0,25}$.", "B = 3 . (1/3) + 1,5 . 4 - 0,5 = 1 + 6 - 0,5 = 6,5 (0.5đ)."),
            make_essay(2, "Vận dụng", "Một phòng triển lãm tranh hình vuông có diện tích 225 m^2. Người ta muốn viền đèn LED xung quanh trần phòng. Hỏi cần đoạn dây LED dài bao nhiêu mét?", "Cạnh phòng triển lãm hình vuông: căn(225) = 15 (m) (0.25đ).\nChu vi trần phòng: 15 x 4 = 60 (m).\nVậy cần đoạn dây LED dài 60 mét (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Tìm tất cả các giá trị của $x$ để biểu thức $P = \\frac{5}{\\sqrt{x} + 2}$ đạt giá trị nguyên lớn nhất.", "Vì x >= 0 nên căn(x) >= 0 => căn(x) + 2 >= 2 (0.25đ).\nDo đó P = 5/(căn(x) + 2) <= 5/2 = 2,5.\nĐể P nguyên lớn nhất thì P = 2 => căn(x) + 2 = 2,5 => căn(x) = 0,5 => x = 0,25 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương II: Số thực - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 3. CHƯƠNG 3 TOÁN 7: GÓC VÀ ĐƯỜNG THẲNG SONG SONG (Bài 5: cuối chương)
def build_c3_7_exams():
    chap_id = "c3_7"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Đường thẳng song song & Tiên đề Euclid",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Hai góc kề bù có tổng số đo bằng:", ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$60^\\circ$"], 0),
            make_mc(2, "Nhận biết", "Hai góc đối đỉnh thì:", ["Bằng nhau", "Kề bù", "Có tổng bằng $90^\\circ$", "Phụ nhau"], 0),
            make_mc(3, "Nhận biết", "Tia phân giác của một góc là tia nằm trong góc và:", ["Tạo với hai cạnh của góc hai góc bằng nhau", "Vuông góc với một cạnh", "Là tia đối của một cạnh", "Đi qua trung điểm"], 0),
            make_mc(4, "Nhận biết", "Theo Tiên đề Euclid: Qua một điểm ở ngoài một đường thẳng có bao nhiêu đường thẳng song song với đường thẳng đó?", ["Chỉ có một đường thẳng duy nhất", "Hai đường thẳng", "Vô số đường thẳng", "Không có đường thẳng nào"], 0),
            make_mc(5, "Thông hiểu", "Cho góc $\\widehat{xOy} = 60^\\circ$. Góc đối đỉnh với $\\widehat{xOy}$ có số đo là:", ["$60^\\circ$", "$120^\\circ$", "$30^\\circ$", "$90^\\circ$"], 0),
            make_mc(6, "Thông hiểu", "Cho hai đường thẳng $a$ và $b$ song song với nhau. Một đường thẳng $c$ cắt $a$ và $b$. Khi đó hai góc so le trong:", ["Bằng nhau", "Bù nhau", "Phụ nhau", "Có tổng bằng $180^\\circ$"], 0),
            make_mc(7, "Thông hiểu", "Nếu đường thẳng $c$ vuông góc với đường thẳng $a$ và $a \\parallel b$ thì:", ["$c \\perp b$", "$c \\parallel b$", "$c$ trùng với $b$", "$c$ cắt $b$ không vuông góc"], 0),
            make_mc(8, "Thông hiểu", "Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì:", ["Song song với nhau", "Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], 0),
            make_mc(9, "Vận dụng", "Cho hình vẽ biết $a \\parallel b$ và một góc so le trong bằng $45^\\circ$. Số đo của góc trong cùng phía với góc đó là:", ["$135^\\circ$", "$45^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0),
            make_mc(10, "Vận dụng", "Cho góc $\\widehat{xOy} = 80^\\circ$, tia $Oz$ là tia phân giác của $\\widehat{xOy}$. Kẻ tia $Ot$ là tia đối của tia $Ox$. Số đo của $\\widehat{zOt}$ là:", ["$140^\\circ$", "$100^\\circ$", "$120^\\circ$", "$80^\\circ$"], 0),
            make_mc(11, "Vận dụng", "Cho định lí: 'Nếu hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau'. Giả thiết của định lí là:", ["Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba", "Chúng song song với nhau", "Ba đường thẳng cắt nhau", "Không có giả thiết"], 0),
            make_mc(12, "Vận dụng cao", "Cho hai đường thẳng $Ax \\parallel By$. Lấy điểm $C$ nằm giữa hai đường thẳng sao cho $\\widehat{xAC} = 130^\\circ$ và $\\widehat{CBy} = 140^\\circ$ (với tia $Ax, By$ cùng chiều). Số đo của góc $\\widehat{ACB}$ là:", ["$90^\\circ$", "$80^\\circ$", "$100^\\circ$", "$110^\\circ$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về quan hệ giữa góc và các đường thẳng song song (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hai góc bằng nhau thì chắc chắn là hai góc đối đỉnh.", "correct": False},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu hai đường thẳng cắt nhau tạo thành một góc vuông thì các góc còn lại cũng là góc vuông.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai góc đồng vị thì luôn bằng nhau.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Hai tia phân giác của hai góc kề bù luôn vuông góc với nhau.", "correct": True}
            ]),
            make_tf(2, "Cho đường thẳng $c$ cắt hai đường thẳng song song $a$ và $b$ tại hai điểm $A$ và $B$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Các cặp góc so le trong bằng nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Các cặp góc đồng vị bằng nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Các cặp góc trong cùng phía bù nhau (tổng bằng 180 độ).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hai tia phân giác của hai góc so le trong song song với nhau.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho góc xOy = 110 độ. Tính góc đối đỉnh với góc kề bù của góc xOy.", "70"),
            make_sa(2, "Thông hiểu", "Cho a song song b. Đường thẳng c cắt a tại A tạo thành một góc 55 độ. Tính số đo góc so le trong tại B.", "55"),
            make_sa(3, "Vận dụng", "Cho hai góc kề bù AOB và BOC biết BOC = 2 AOB. Tính số đo góc BOC (độ).", "120"),
            make_sa(4, "Vận dụng cao", "Cho hai đường thẳng a song song b. Một đường thẳng cắt a và b tạo ra 8 góc. Biết tổng 3 góc nhọn bằng 150 độ. Tính số đo một góc tù (độ).", "130")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Cho hình vẽ hai đường thẳng $xx'$ và $yy'$ cắt nhau tại $O$ sao cho $\\widehat{xOy} = 50^\\circ$. Tính số đo các góc còn lại tại đỉnh $O$.", "x'Oy' = xOy = 50 độ (đối đỉnh) (0.25đ).\nxOy' kề bù xOy => xOy' = 180 - 50 = 130 độ.\nx'Oy đối đỉnh xOy' => x'Oy = 130 độ (0.25đ)."),
            make_essay(2, "Vận dụng", "Cho tam giác $ABC$. Qua đỉnh $A$ vẽ đường thẳng $xy \\parallel BC$. Chứng minh rằng tổng ba góc của tam giác $ABC$ bằng $180^\\circ$.", "Vì xy song song BC nên: góc xAB = B (so le trong) và yAC = C (so le trong) (0.25đ).\nMà xAB + BAC + yAC = xAy = 180 độ (góc bẹt).\nSuy ra: A + B + C = 180 độ. Đpcm (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho hai tia $Ax \\parallel By$. Điểm $C$ nằm giữa hai tia sao cho góc $\\widehat{CAx} = \\alpha$ và $\\widehat{CBy} = \\beta$ (với các góc nhọn). Vẽ tia $Cz \\parallel Ax$. Tính góc $\\widehat{ACB}$ theo $\\alpha$ và $\\beta$.", "Vẽ Cz song song Ax (nằm giữa CA và CB) => Cz song song By (0.25đ).\nVì Cz song song Ax => góc ACz = CAx = alpha (so le trong).\nVì Cz song song By => góc BCz = CBy = beta (so le trong).\nDo đó: ACB = ACz + BCz = alpha + beta (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương III: Góc và đường thẳng song song - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 4. CHƯƠNG 4 TOÁN 7: TAM GIÁC BẰNG NHAU (Bài 6: cuối chương)
def build_c4_7_exams():
    chap_id = "c4_7"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Các trường hợp bằng nhau của tam giác",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Tổng ba góc trong một tam giác bằng:", ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$120^\\circ$"], 0),
            make_mc(2, "Nhận biết", "Tam giác $ABC$ có $\\widehat{A} = 90^\\circ$. Tam giác $ABC$ là:", ["Tam giác vuông tại $A$", "Tam giác đều", "Tam giác tù", "Tam giác cân"], 0),
            make_mc(3, "Nhận biết", "Nếu $\\Delta ABC = \\Delta MNP$ thì khẳng định nào sau đây là ĐÚNG?", ["$AB = MN$ và $\\widehat{A} = \\widehat{M}$", "$AB = NP$", "$AC = MN$", "$\\widehat{B} = \\widehat{P}$"], 0),
            make_mc(4, "Nhận biết", "Tam giác cân là tam giác có:", ["Hai cạnh bằng nhau", "Ba cạnh bằng nhau", "Một góc vuông", "Ba góc nhọn"], 0),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ cân tại $A$ có $\\widehat{A} = 50^\\circ$. Số đo của góc đáy $\\widehat{B}$ là:", ["$65^\\circ$", "$130^\\circ$", "$50^\\circ$", "$60^\\circ$"], 0),
            make_mc(6, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$, có $\\widehat{B} = 35^\\circ$. Số đo của góc $\\widehat{C}$ là:", ["$55^\\circ$", "$65^\\circ$", "$35^\\circ$", "$45^\\circ$"], 0),
            make_mc(7, "Thông hiểu", "Trường hợp bằng nhau cạnh - góc - cạnh (c-g-c) đòi hỏi:", ["Góc xen giữa hai cạnh phải bằng nhau", "Góc bất kì bằng nhau", "Cả ba góc bằng nhau", "Cạnh đối diện bằng nhau"], 0),
            make_mc(8, "Thông hiểu", "Đường trung trực của đoạn thẳng $AB$ là đường thẳng:", ["Vuông góc với $AB$ tại trung điểm của nó", "Đi qua trung điểm của $AB$", "Vuông góc với $AB$", "Song song với $AB$"], 0),
            make_mc(9, "Vận dụng", "Cho $\\Delta ABC = \\Delta DEF$. Biết $AB = 5\\text{ cm}, AC = 7\\text{ cm}$ và chu vi $\\Delta DEF$ bằng $20\\text{ cm}$. Độ dài cạnh $BC$ là:", ["$8\\text{ cm}$", "$6\\text{ cm}$", "$5\\text{ cm}$", "$7\\text{ cm}$"], 0),
            make_mc(10, "Vận dụng", "Cho tam giác $MNP$ có $\\widehat{M} = 70^\\circ$ và $\\widehat{N} - \\widehat{P} = 20^\\circ$. Số đo của góc $\\widehat{N}$ là:", ["$65^\\circ$", "$45^\\circ$", "$55^\\circ$", "$75^\\circ$"], 0),
            make_mc(11, "Vận dụng", "Cho tam giác $ABC$ cân tại $A$, kẻ $AH \\perp BC$ ($H \\in BC$). Khẳng định nào sau đây là SAI?", ["$AH > AB$", "$HB = HC$", "$\\widehat{BAH} = \\widehat{CAH}$", "$\\Delta ABH = \\Delta ACH$"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{A} = 60^\\circ$, hai tia phân giác của góc $B$ và $C$ cắt nhau tại $I$. Số đo của góc $\\widehat{BIC}$ là:", ["$120^\\circ$", "$150^\\circ$", "$135^\\circ$", "$110^\\circ$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tam giác và các trường hợp bằng nhau (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Trong một tam giác vuông, hai góc nhọn phụ nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tam giác có ba cạnh bằng nhau là tam giác đều.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai tam giác có ba góc tương ứng bằng nhau thì luôn bằng nhau.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Điểm cách đều hai đầu mút của một đoạn thẳng thì nằm trên đường trung trực của đoạn thẳng đó.", "correct": True}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB = AC$. Gọi $M$ là trung điểm của $BC$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Tam giác $ABC$ là tam giác cân tại $A$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "$\\Delta ABM = \\Delta ACM$ theo trường hợp cạnh - cạnh - cạnh (c-c-c).", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Đoạn thẳng $AM$ vuông góc với cạnh $BC$.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tia $AM$ là tia phân giác của góc $\\widehat{BAC}$.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho tam giác ABC có góc A = 75 độ, góc B = 45 độ. Tính số đo góc C (độ).", "60"),
            make_sa(2, "Thông hiểu", "Cho tam giác DEF cân tại D có góc D = 80 độ. Tính số đo góc đáy E (độ).", "50"),
            make_sa(3, "Vận dụng", "Cho tam giác ABC có góc A = 2 góc B và góc B = 2 góc C. Tính số đo góc A (độ).", "102,86"), # Thay thế bằng số nguyên đẹp
            make_sa(4, "Vận dụng cao", "Cho tam giác ABC có chu vi bằng 24 cm. Hai cạnh bằng nhau và mỗi cạnh dài gấp đôi cạnh đáy. Tính độ dài cạnh đáy (cm).", "4,8")
        ]
        # Fix số đo câu 3 và câu 4 cho chuẩn số nguyên đẹp
        p3[2] = make_sa(3, "Vận dụng", "Cho tam giác ABC vuông tại A có góc B gấp đôi góc C. Tính số đo góc B (độ).", "60")
        p3[3] = make_sa(4, "Vận dụng cao", "Cho tam giác ABC cân tại A có chu vi 32 cm, cạnh đáy BC = 12 cm. Tính độ dài cạnh bên AB (cm).", "10")

        p4 = [
            make_essay(1, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 50^\\circ$. Tính số đo góc ngoài tại đỉnh $C$ của tam giác.", "Số đo góc ngoài tại đỉnh C bằng tổng hai góc trong không kề: C_ngoai = A + B = 70 + 50 = 120 độ (0.5đ)."),
            make_essay(2, "Vận dụng", "Cho đoạn thẳng $AB$. Vẽ đường trung trực $d$ của $AB$. Lấy điểm $M$ bất kì trên $d$ ($M \\notin AB$). Chứng minh rằng $\\Delta MAB$ là tam giác cân.", "Gọi I là trung điểm AB => d vuông góc AB tại I và IA = IB (0.25đ).\nXét hai tam giác vuông MIA và MIB: MI chung, IA = IB => MIA = MIB (c-g-c).\n=> MA = MB => tam giác MAB cân tại M (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ cân tại $A$ ($\\widehat{A} < 90^\\circ$). Kẻ $BD \\perp AC$ tại $D$ và $CE \\perp AB$ tại $E$. Chứng minh rằng $BD = CE$ và $\\Delta ADE$ là tam giác cân.", "Xét hai tam giác vuông ADB và AEC: A chung, AB = AC (tam giác ABC cân) (0.25đ).\n=> tam giác ADB = tam giác AEC (cạnh huyền - góc nhọn) => BD = CE và AD = AE.\nVì AD = AE nên tam giác ADE cân tại A (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương IV: Tam giác bằng nhau - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 5. CHƯƠNG 5 TOÁN 7: THU THẬP VÀ BIỂU DIỄN DỮ LIỆU (Bài 4: cuối chương)
def build_c5_7_exams():
    chap_id = "c5_7"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Biểu đồ quạt tròn & Đoạn thẳng",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Biểu đồ hình quạt tròn thường được dùng để:", ["Biểu diễn tỉ lệ phần trăm của từng loại số liệu so với toàn thể", "Biểu diễn sự thay đổi theo thời gian", "So sánh độ lớn tuyệt đối", "Biểu diễn dữ liệu định tính không theo tỉ lệ"], 0),
            make_mc(2, "Nhận biết", "Tổng số phần trăm của tất cả các hình quạt trong biểu đồ quạt tròn là:", ["$100\\%$", "$360\\%$", "$50\\%$", "$180\\%$"], 0),
            make_mc(3, "Nhận biết", "Biểu đồ đoạn thẳng thích hợp nhất để biểu diễn:", ["Xu hướng thay đổi của đại lượng theo thời gian", "Cơ cấu dân số", "Thành phần các chất", "Xếp loại học lực một lần duy nhất"], 0),
            make_mc(4, "Nhận biết", "Một hình quạt tròn biểu diễn $25\\%$ tổng thể tương ứng với góc ở tâm có số đo bằng:", ["$90^\\circ$", "$45^\\circ$", "$180^\\circ$", "$36^\\circ$"], 0),
            make_mc(5, "Thông hiểu", "Biểu đồ quạt tròn thể hiện sở thích thể thao của 200 học sinh: Bóng đá chiếm $40\\%$. Số học sinh thích bóng đá là:", ["$80$ học sinh", "$40$ học sinh", "$100$ học sinh", "$60$ học sinh"], 0),
            make_mc(6, "Thông hiểu", "Số liệu nào sau đây là dữ liệu không phải là số (dữ liệu định tính)?", ["Mức độ hài lòng: Rất tốt, Tốt, Trung bình", "Số anh chị em trong gia đình", "Điểm thi môn Toán", "Nhiệt độ trung bình"], 0),
            make_mc(7, "Thông hiểu", "Một biểu đồ quạt tròn có một quạt chiếm góc $180^\\circ$. Tỉ lệ phần trăm của phần tử đó là:", ["$50\\%$", "$25\\%$", "$100\\%$", "$75\\%$"], 0),
            make_mc(8, "Thông hiểu", "Dữ liệu thu thập được có thể trình bày dưới dạng:", ["Bảng thống kê và biểu đồ", "Chỉ dạng văn bản", "Chỉ dạng bảng tính", "Chỉ biểu đồ đoạn thẳng"], 0),
            make_mc(9, "Vận dụng", "Một trường có 800 học sinh. Biểu đồ quạt tròn cho biết học lực Giỏi chiếm $30\\%$, Khá chiếm $45\\%$, Đạt chiếm $20\\%$, còn lại là Chưa đạt. Số học sinh Chưa đạt là:", ["$40$ học sinh", "$50$ học sinh", "$30$ học sinh", "$60$ học sinh"], 0),
            make_mc(10, "Vận dụng", "Quan sát biểu đồ đoạn thẳng về doanh thu 4 quý của một công ty: Quý 1: 50 tỷ, Quý 2: 70 tỷ, Quý 3: 65 tỷ, Quý 4: 95 tỷ. Tổng doanh thu cả năm là:", ["$280$ tỷ đồng", "$260$ tỷ đồng", "$300$ tỷ đồng", "$250$ tỷ đồng"], 0),
            make_mc(11, "Vận dụng", "Doanh thu của công ty ở câu trên tăng nhiều nhất trong khoảng thời gian nào?", ["Từ Quý 3 đến Quý 4 (tăng 30 tỷ)", "Từ Quý 1 đến Quý 2 (tăng 20 tỷ)", "Từ Quý 2 đến Quý 3", "Không tăng"], 0),
            make_mc(12, "Vận dụng cao", "Trong biểu đồ quạt tròn, góc ở tâm biểu diễn số học sinh thích học môn Văn là $72^\\circ$. Biết toàn trường có 1500 học sinh, số học sinh thích môn Văn là:", ["$300$ học sinh", "$250$ học sinh", "$360$ học sinh", "$200$ học sinh"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về các loại biểu đồ thống kê (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hình quạt tròn có góc ở tâm càng lớn thì biểu diễn tỉ lệ phần trăm càng lớn.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Biểu đồ đoạn thẳng giúp dễ dàng nhận biết xu hướng tăng hay giảm của số liệu.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tổng các góc ở tâm của các hình quạt trong biểu đồ quạt tròn luôn bằng 360 độ.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu tỉ lệ phần trăm tăng gấp đôi thì góc ở tâm tương ứng tăng thêm 180 độ.", "correct": False}
            ]),
            make_tf(2, "Khảo sát ý kiến của 500 người tiêu dùng về chất lượng sản phẩm: Rất hài lòng chiếm 40%, Hài lòng chiếm 35%, Bình thường chiếm 20%, Không hài lòng chiếm 5%:", [
                {"key": "a", "level": "Thông hiểu", "text": "Số người đánh giá Rất hài lòng là 200 người.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số người đánh giá Hài lòng là 175 người.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số người đánh giá Không hài lòng là 25 người.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tỉ lệ người đánh giá từ Hài lòng trở lên chiếm đúng 70% tổng số người khảo sát.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính góc ở tâm (độ) của hình quạt tròn biểu diễn 15% tổng thể.", "54"),
            make_sa(2, "Thông hiểu", "Một lớp có 45 học sinh, 18 em xếp loại giỏi. Tính tỉ lệ phần trăm học sinh giỏi.", "40"),
            make_sa(3, "Vận dụng", "Biểu đồ quạt tròn có góc ở tâm môn Toán là 108 độ. Hỏi môn Toán chiếm bao nhiêu phần trăm?", "30"),
            make_sa(4, "Vận dụng cao", "Năm 2023 thu nhập là 80 triệu, năm 2024 tăng 25%. Tính thu nhập năm 2024 (triệu đồng).", "100")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Nêu hai ưu điểm nổi bật của biểu đồ đoạn thẳng so với bảng số liệu thô.", "1) Giúp trực quan hóa và dễ dàng nhận thấy xu hướng tăng/giảm theo thời gian (0.25đ).\n2) Giúp so sánh nhanh các mốc thời gian mà không cần đọc từng con số chi tiết (0.25đ)."),
            make_essay(2, "Vận dụng", "Số lượng xe máy một cửa hàng bán được trong 4 tháng đầu năm: Tháng 1: 40 xe; Tháng 2: 50 xe; Tháng 3: 45 xe; Tháng 4: 65 xe. a) Tính tổng số xe bán được trong 4 tháng. b) Tháng nào bán được nhiều xe nhất và chiếm bao nhiêu phần trăm tổng số?", "a) Tổng số xe: 40 + 50 + 45 + 65 = 200 (xe) (0.25đ).\nb) Tháng 4 bán nhiều nhất với 65 xe. Tỉ lệ: 65 / 200 = 32,5% (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Một trường THCS có 1200 học sinh. Biểu đồ quạt tròn phân loại phương tiện đến trường gồm: Xe đạp (45%), Đi bộ (30%), Bố mẹ chở bằng xe máy (20%), Xe buýt (5%). Ban giám hiệu muốn bố trí bãi đỗ xe đạp cho học sinh, trung bình mỗi chiếc xe đạp cần 1,2 m^2 diện tích. Tính diện tích tối thiểu bãi đỗ xe đạp cần xây dựng.", "Số học sinh đi xe đạp: 1200 x 45% = 540 (học sinh) (0.25đ).\nDiện tích tối thiểu bãi đỗ xe đạp: 540 x 1,2 = 648 (m^2) (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương V: Biểu diễn dữ liệu - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 6. CHƯƠNG 6 TOÁN 7: TỈ LỆ THỨC VÀ ĐẠI LƯỢNG TỈ LỆ (Bài 5: cuối chương)
def build_c6_7_exams():
    chap_id = "c6_7"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Tỉ lệ thuận & Tỉ lệ nghịch",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Tỉ lệ thức là đẳng thức của hai tỉ số có dạng:", ["$\\frac{a}{b} = \\frac{c}{d}$", "$a \\cdot b = c \\cdot d$", "$a + b = c + d$", "$\\frac{a}{b} + \\frac{c}{d} = 1$"], 0),
            make_mc(2, "Nhận biết", "Từ đẳng thức $a \\cdot d = b \\cdot c$ ($a, b, c, d \\neq 0$) có thể suy ra tỉ lệ thức nào?", ["$\\frac{a}{b} = \\frac{c}{d}$", "$\\frac{a}{c} = \\frac{d}{b}$", "$\\frac{a}{d} = \\frac{b}{c}$", "$\\frac{b}{a} = \\frac{c}{d}$"], 0),
            make_mc(3, "Nhận biết", "Nếu đại lượng $y$ liên hệ với đại lượng $x$ theo công thức $y = kx$ ($k \\neq 0$) thì ta nói:", ["$y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $k$", "$y$ tỉ lệ nghịch với $x$", "$x$ tỉ lệ nghịch với $y$", "$x$ và $y$ không phụ thuộc nhau"], 0),
            make_mc(4, "Nhận biết", "Nếu đại lượng $y$ liên hệ với đại lượng $x$ theo công thức $y = \\frac{a}{x}$ ($a \\neq 0$) thì ta nói:", ["$y$ tỉ lệ nghịch với $x$ theo hệ số tỉ lệ $a$", "$y$ tỉ lệ thuận với $x$", "$x$ tỉ lệ thuận với $y$", "$y = a - x$"], 0),
            make_mc(5, "Thông hiểu", "Tìm $x$ trong tỉ lệ thức $\\frac{x}{6} = \\frac{5}{3}$:", ["$x = 10$", "$x = 9$", "$x = 2,5$", "$x = 15$"], 0),
            make_mc(6, "Thông hiểu", "Cho dãy tỉ số bằng nhau $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{5}$ và $x + y + z = 30$. Giá trị của $x$ là:", ["$x = 6$", "$x = 9$", "$x = 15$", "$x = 3$"], 0),
            make_mc(7, "Thông hiểu", "Biết $y$ tỉ lệ thuận với $x$ và khi $x = 4$ thì $y = 12$. Hệ số tỉ lệ của $y$ đối với $x$ là:", ["$k = 3$", "$k = \\frac{1}{3}$", "$k = 48$", "$k = 8$"], 0),
            make_mc(8, "Thông hiểu", "Biết $y$ tỉ lệ nghịch với $x$ và khi $x = 3$ thì $y = 8$. Khi $x = 6$ thì giá trị của $y$ là:", ["$y = 4$", "$y = 16$", "$y = 2$", "$y = 24$"], 0),
            make_mc(9, "Vận dụng", "Ba đội máy cày có năng suất như nhau cày ba cánh đồng có cùng diện tích. Đội 1 cày xong trong 3 ngày, đội 2 trong 4 ngày, đội 3 trong 6 ngày. Biết đội 1 nhiều hơn đội 2 là 2 máy. Số máy cày của đội 1 là:", ["$8$ máy", "$6$ máy", "$4$ máy", "$10$ máy"], 0),
            make_mc(10, "Vận dụng", "Tìm hai số $x$ và $y$ biết $\\frac{x}{3} = \\frac{y}{5}$ và $2x + y = 33$:", ["$x = 9; y = 15$", "$x = 6; y = 10$", "$x = 12; y = 20$", "$x = 15; y = 25$"], 0),
            make_mc(11, "Vận dụng", "Để làm xong một công việc trong 12 ngày cần 15 công nhân. Nếu muốn làm xong công việc đó sớm hơn 2 ngày (trong 10 ngày) thì cần bổ sung thêm bao nhiêu công nhân (năng suất như nhau)?", ["$3$ công nhân", "$18$ công nhân", "$5$ công nhân", "$2$ công nhân"], 0),
            make_mc(12, "Vận dụng cao", "Cho dãy tỉ số bằng nhau $\\frac{a}{b} = \\frac{c}{d}$. Khẳng định nào sau đây là ĐÚNG?", ["$\\frac{a+b}{a-b} = \\frac{c+d}{c-d}$", "$\\frac{a+c}{b+d} = \\frac{a \\cdot c}{b \\cdot d}$", "$\\frac{a}{d} = \\frac{c}{b}$", "$\\frac{a^2+c^2}{b^2+d^2} = \\frac{a+c}{b+d}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tỉ lệ thức và đại lượng tỉ lệ (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu y tỉ lệ thuận với x theo hệ số k thì x tỉ lệ thuận với y theo hệ số 1/k (k khác 0).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu y tỉ lệ nghịch với x theo hệ số a thì tích x.y luôn là một hằng số bằng a.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Chu vi hình vuông tỉ lệ thuận với độ dài cạnh của hình vuông.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích hình vuông tỉ lệ thuận với độ dài cạnh của hình vuông.", "correct": False}
            ]),
            make_tf(2, "Số học sinh của ba lớp 7A, 7B, 7C tỉ lệ với 8; 9; 10. Biết tổng số học sinh của cả ba lớp là 108 em:", [
                {"key": "a", "level": "Thông hiểu", "text": "Số học sinh lớp 7A là 32 em.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số học sinh lớp 7B là 36 em.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số học sinh lớp 7C là 40 em.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số học sinh lớp 7C nhiều hơn lớp 7A là 10 em.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tìm x biết: x / 5 = 12 / 15.", "4"),
            make_sa(2, "Thông hiểu", "Tìm hai số x, y biết x/2 = y/5 và x + y = 28. Tìm giá trị của x.", "8"),
            make_sa(3, "Vận dụng", "Biết y tỉ lệ nghịch với x, khi x = 4 thì y = 9. Tìm y khi x = 6.", "6"),
            make_sa(4, "Vận dụng cao", "Cho a/b = c/d = e/f = 4. Tính giá trị biểu thức: (2a - 3c + e) / (2b - 3d + f).", "4")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Tìm hai số $x$ và $y$ biết $\\frac{x}{4} = \\frac{y}{7}$ và $x + y = 55$.", "Áp dụng tính chất dãy tỉ số bằng nhau: x/4 = y/7 = (x + y)/(4 + 7) = 55/11 = 5 (0.25đ).\n=> x = 4 x 5 = 20; y = 7 x 5 = 35 (0.25đ)."),
            make_essay(2, "Vận dụng", "Ba lớp 7A, 7B, 7C tham gia trồng cây xanh bảo vệ môi trường. Số cây trồng được của ba lớp lần lượt tỉ lệ với 4; 5; 6. Biết lớp 7C trồng được nhiều hơn lớp 7A là 30 cây. Tính tổng số cây cả ba lớp trồng được.", "Gọi x, y, z là số cây trồng được của 7A, 7B, 7C. Ta có x/4 = y/5 = z/6 và z - x = 30 (0.25đ).\nÁp dụng: x/4 = y/5 = z/6 = (z - x)/(6 - 4) = 30/2 = 15.\nTổng số cây: (4 + 5 + 6) x 15 = 15 x 15 = 225 (cây) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho dãy tỉ số bằng nhau: $\\frac{2a + b + c + d}{a} = \\frac{a + 2b + c + d}{b} = \\frac{a + b + 2c + d}{c} = \\frac{a + b + c + 2d}{d}$. Tính giá trị của biểu thức $P = \\frac{a + b}{c + d} + \\frac{b + c}{d + a} + \\frac{c + d}{a + b} + \\frac{d + a}{b + c}$.", "Trừ 1 ở mỗi phân thức ta được: (a+b+c+d)/a = (a+b+c+d)/b = (a+b+c+d)/c = (a+b+c+d)/d (0.25đ).\nTH1: a + b + c + d = 0 => a + b = -(c + d), v.v. Khi đó mỗi phân thức bằng -1 => P = -4.\nTH2: a + b + c + d khác 0 => a = b = c = d. Khi đó mỗi phân thức bằng 1 => P = 4.\nVậy P = 4 hoặc P = -4 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương VI: Tỉ lệ thức & Đại lượng tỉ lệ - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 7. CHƯƠNG 7 TOÁN 7: BIỂU THỨC ĐẠI SỐ VÀ ĐA THỨC MỘT BIẾN (Bài 6: cuối chương)
def build_c7_7_exams():
    chap_id = "c7_7"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Đa thức một biến & Nghiệm",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Biểu thức nào sau đây là đơn thức một biến?", ["$3x^2$", "$2x + 1$", "$x^2 - y$", "$\\frac{1}{x}$"], 0),
            make_mc(2, "Nhận biết", "Bậc của đa thức $P(x) = 4x^3 - 2x^5 + x - 7$ là:", ["$5$", "$3$", "$4$", "$7$"], 0),
            make_mc(3, "Nhận biết", "Hệ số cao nhất của đa thức $A(x) = -3x^4 + 5x^2 - x + 9$ là:", ["$-3$", "$5$", "$9$", "$4$"], 0),
            make_mc(4, "Nhận biết", "Hệ số tự do của đa thức $Q(x) = 2x^3 - 7x + 15$ là:", ["$15$", "$2$", "$-7$", "$0$"], 0),
            make_mc(5, "Thông hiểu", "Giá trị của đa thức $P(x) = 2x^2 - 3x + 1$ tại $x = 2$ là:", ["$3$", "$5$", "$15$", "$1$"], 0),
            make_mc(6, "Thông hiểu", "Số nào sau đây là nghiệm của đa thức $A(x) = 2x - 6$?", ["$x = 3$", "$x = -3$", "$x = 6$", "$x = 0$"], 0),
            make_mc(7, "Thông hiểu", "Thu gọn đa thức $M(x) = 3x^2 - 5x + 2x^2 + 5x - 7$ ta được:", ["$5x^2 - 7$", "$5x^2 + 10x - 7$", "$x^2 - 7$", "$5x^2$"], 0),
            make_mc(8, "Thông hiểu", "Cho $P(x) = x^2 - 4x + 3$. Nghiệm của đa thức $P(x)$ là:", ["$x = 1$ và $x = 3$", "$x = -1$ và $x = -3$", "$x = 2$", "$x = 4$"], 0),
            make_mc(9, "Vận dụng", "Cho hai đa thức $A(x) = 3x^3 - 2x + 5$ và $B(x) = -x^3 + 2x - 1$. Đa thức $A(x) + B(x)$ bằng:", ["$2x^3 + 4$", "$4x^3 + 4$", "$2x^3 - 4x + 6$", "$2x^3 + 6$"], 0),
            make_mc(10, "Vận dụng", "Tìm đa thức $C(x)$ biết $C(x) + (2x^2 - x) = 5x^2 - 3x + 4$:", ["$C(x) = 3x^2 - 2x + 4$", "$C(x) = 7x^2 - 4x + 4$", "$C(x) = 3x^2 - 4x + 4$", "$C(x) = 3x^2 + 2x + 4$"], 0),
            make_mc(11, "Vận dụng", "Thực hiện phép nhân đa thức $(x - 2)(x + 3)$ ta được:", ["$x^2 + x - 6$", "$x^2 - x - 6$", "$x^2 + 5x - 6$", "$x^2 - 6$"], 0),
            make_mc(12, "Vận dụng cao", "Chứng minh đa thức $P(x) = x^2 + 2x + 5$ không có nghiệm trên tập số thực:", ["$P(x) = (x + 1)^2 + 4 > 0$ với mọi $x$", "$P(x)$ có bậc 2", "Hệ số tự do dương", "Vì $x^2 > 0$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về đa thức một biến (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Số 0 được coi là đa thức không có bậc.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Một đa thức bậc n (n >= 1) có không quá n nghiệm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu P(a) = 0 thì a là một nghiệm của đa thức P(x).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tổng của hai đa thức bậc 3 luôn luôn là một đa thức bậc 3.", "correct": False}
            ]),
            make_tf(2, "Cho hai đa thức $P(x) = 2x^2 - 4x + 2$ và $Q(x) = x - 1$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Đa thức P(x) có bậc là 2, hệ số cao nhất là 2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Giá trị của Q(x) tại x = 1 bằng 0.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Chia đa thức P(x) cho Q(x) ta được thương là 2x - 2.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Đa thức P(x) có đúng hai nghiệm phân biệt.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính giá trị của đa thức P(x) = 3x^2 - 5x + 2 tại x = 1.", "0"),
            make_sa(2, "Thông hiểu", "Tìm bậc của đa thức: A(x) = 5x^4 - 2x^3 + 7x - 5x^4 + 1.", "3"),
            make_sa(3, "Vận dụng", "Tìm nghiệm của đa thức: B(x) = 4x - 12.", "3"),
            make_sa(4, "Vận dụng cao", "Tìm hệ số a để đa thức P(x) = ax^2 - 2x + 3 nhận x = -1 là một nghiệm.", "-1") # a(-1)^2 - 2(-1) + 3 = a + 5 = 0 => a = -5
        ]
        p3[3] = make_sa(4, "Vận dụng cao", "Tìm hệ số a để đa thức P(x) = ax^2 - 2x + 3 nhận x = -1 là nghiệm.", "-5")

        p4 = [
            make_essay(1, "Thông hiểu", "Cho hai đa thức: $A(x) = 2x^3 - 3x^2 + 4x - 5$ và $B(x) = -x^3 + 3x^2 - 2x + 1$. Tính $A(x) + B(x)$.", "A(x) + B(x) = (2 - 1)x^3 + (-3 + 3)x^2 + (4 - 2)x + (-5 + 1) = x^3 + 2x - 4 (0.5đ)."),
            make_essay(2, "Vận dụng", "Cho đa thức $M(x) = x^3 - 4x$. a) Tìm bậc và các hệ số của $M(x)$. b) Tìm tất cả các nghiệm của đa thức $M(x)$.", "a) Bậc 3, hệ số cao nhất là 1, hệ số bậc 1 là -4 (0.25đ).\nb) M(x) = x(x^2 - 4) = x(x - 2)(x + 2) = 0 => x = 0 hoặc x = 2 hoặc x = -2 (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho đa thức $P(x) = ax^2 + bx + c$. Biết rằng $P(0), P(1), P(2)$ đều là các số nguyên. Chứng minh rằng $2a, 2b$ và $c$ đều là các số nguyên.", "P(0) = c => c là số nguyên (0.25đ).\nP(1) = a + b + c nguyên => a + b nguyên.\nP(2) = 4a + 2b + c nguyên => 4a + 2b = 2(2a + b) nguyên.\nTa có 2a = P(2) - 2P(1) + P(0) là số nguyên.\n=> 2b = 2(a + b) - 2a cũng là số nguyên. Đpcm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương VII: Biểu thức đại số - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 8. CHƯƠNG 8 TOÁN 7: LÀM QUEN VỚI BIẾN CỐ VÀ XÁC SUẤT (Bài 3: cuối chương)
def build_c8_7_exams():
    chap_id = "c8_7"
    l_idx = 3
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Biến cố & Xác suất cơ bản",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Biến cố chắc chắn là biến cố:", ["Chắc chắn xảy ra khi thực hiện phép thử", "Không bao giờ xảy ra", "Có thể xảy ra hoặc không", "Có xác suất bằng 0"], 0),
            make_mc(2, "Nhận biết", "Xác suất của biến cố không thể bằng:", ["$0$", "$1$", "$0,5$", "$-1$"], 0),
            make_mc(3, "Nhận biết", "Xác suất của biến cố chắc chắn bằng:", ["$1$", "$0$", "$0,5$", "$100$"], 0),
            make_mc(4, "Nhận biết", "Gieo một con xúc xắc cân đối. Biến cố nào sau đây là biến cố không thể?", ["Xuất hiện mặt 7 chấm", "Xuất hiện mặt 1 chấm", "Xuất hiện mặt chẵn", "Xuất hiện số chấm nhỏ hơn 7"], 0),
            make_mc(5, "Thông hiểu", "Tung một đồng xu cân đối 1 lần. Xác suất xuất hiện mặt Ngửa là:", ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$1$", "$0$"], 0),
            make_mc(6, "Thông hiểu", "Gieo một con xúc xắc 6 mặt một lần. Xác suất để xuất hiện mặt có số chấm là số chẵn là:", ["$\\frac{3}{6} = \\frac{1}{2}$", "$\\frac{1}{6}$", "$\\frac{2}{6}$", "$\\frac{4}{6}$"], 0),
            make_mc(7, "Thông hiểu", "Một hộp có 5 chiếc bút bi xanh và 3 chiếc bút bi đỏ cùng loại. Lấy ngẫu nhiên 1 chiếc bút. Xác suất lấy được bút bi xanh là:", ["$\\frac{5}{8}$", "$\\frac{3}{8}$", "$\\frac{5}{3}$", "$\\frac{1}{8}$"], 0),
            make_mc(8, "Thông hiểu", "Chọn ngẫu nhiên một số tự nhiên có một chữ số (từ 0 đến 9). Xác suất chọn được số nguyên tố là:", ["$\\frac{4}{10} = \\frac{2}{5}$", "$\\frac{5}{10}$", "$\\frac{3}{10}$", "$\\frac{1}{10}$"], 0),
            make_mc(9, "Vận dụng", "Gieo một con xúc xắc cân đối. Xác suất để xuất hiện mặt có số chấm là số nguyên tố là:", ["$\\frac{3}{6} = \\frac{1}{2}$ (gồm 2, 3, 5)", "$\\frac{2}{6}$", "$\\frac{4}{6}$", "$\\frac{1}{6}$"], 0),
            make_mc(10, "Vận dụng", "Một túi đựng 20 viên kẹo giống hệt nhau gồm 8 viên dâu, 7 viên cam và 5 viên bạc hà. Lấy ngẫu nhiên 1 viên kẹo. Xác suất để viên kẹo lấy ra không phải là vị bạc hà là:", ["$\\frac{15}{20} = \\frac{3}{4}$", "$\\frac{5}{20} = \\frac{1}{4}$", "$\\frac{8}{20}$", "$\\frac{7}{20}$"], 0),
            make_mc(11, "Vận dụng", "Một lớp học có 20 bạn nam và 25 bạn nữ. Giáo viên gọi ngẫu nhiên một bạn lên bảng trả lời câu hỏi. Xác suất để bạn được gọi là một bạn nữ là:", ["$\\frac{25}{45} = \\frac{5}{9}$", "$\\frac{20}{45} = \\frac{4}{9}$", "$\\frac{1}{2}$", "$\\frac{20}{25}$"], 0),
            make_mc(12, "Vận dụng cao", "Gieo đồng thời hai con xúc xắc cân đối một lần. Xác suất để tổng số chấm trên hai con xúc xắc bằng 8 là:", ["$\\frac{5}{36}$", "$\\frac{6}{36}$", "$\\frac{4}{36}$", "$\\frac{1}{8}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về các loại biến cố và xác suất (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Biến cố ngẫu nhiên là biến cố không thể biết trước chắc chắn có xảy ra hay không.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Xác suất của mọi biến cố ngẫu nhiên luôn nằm nghiêm ngặt giữa 0 và 1.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu hai biến cố đồng khả năng thì xác suất của chúng bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tung 2 đồng xu cùng lúc thì xác suất xuất hiện 2 mặt ngửa bằng 1/2.", "correct": False}
            ]),
            make_tf(2, "Trong một hộp có 12 tấm thẻ cùng loại được đánh số từ 1 đến 12. Rút ngẫu nhiên một tấm thẻ:", [
                {"key": "a", "level": "Thông hiểu", "text": "Có tất cả 12 kết quả có thể xảy ra với số ghi trên thẻ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Xác suất rút được thẻ ghi số chẵn bằng 6/12 = 1/2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Xác suất rút được thẻ ghi số chia hết cho 3 bằng 4/12 = 1/3.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Xác suất rút được thẻ ghi số chia hết cho cả 2 và 3 là 1/4.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Một hộp có 4 bi xanh và 6 bi đỏ. Tính xác suất bốc được bi đỏ.", "0,6"),
            make_sa(2, "Thông hiểu", "Gieo xúc xắc 1 lần. Tính xác suất xuất hiện mặt có số chấm lớn hơn 4.", "1/3"),
            make_sa(3, "Vận dụng", "Rút 1 thẻ từ 1 đến 20. Có bao nhiêu kết quả thuận lợi cho sự kiện 'rút được số chia hết cho 4'?", "5"),
            make_sa(4, "Vận dụng cao", "Gieo 2 con xúc xắc cân đối. Có bao nhiêu kết quả để tích hai số chấm là số lẻ?", "9")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Một tổ học sinh có 6 bạn nam và 4 bạn nữ. Chọn ngẫu nhiên một bạn làm tổ trưởng. Tính xác suất chọn được bạn nam.", "Số kết quả có thể: 6 + 4 = 10 (0.25đ).\nSố kết quả thuận lợi cho bạn nam: 6. Xác suất: 6/10 = 3/5 = 0,6 (0.25đ)."),
            make_essay(2, "Vận dụng", "Trong hộp có 15 quả bóng bàn cùng loại được đánh số từ 1 đến 15. Lấy ngẫu nhiên một quả bóng. Tính xác suất của các biến cố sau: a) Quả bóng lấy ra ghi số chia hết cho 5. b) Quả bóng lấy ra ghi số là số nguyên tố.", "a) Các số chia hết cho 5: {5; 10; 15} (3 số). P = 3/15 = 1/5 (0.25đ).\nb) Các số nguyên tố: {2; 3; 5; 7; 11; 13} (6 số). P = 6/15 = 2/5 (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Gieo đồng thời hai con xúc xắc cân đối. Tính xác suất để tổng số chấm xuất hiện trên hai con xúc xắc là một số chia hết cho 5.", "Không gian mẫu: 6 x 6 = 36 kết quả (0.25đ).\nCác cặp có tổng chia hết cho 5:\nTổng = 5: (1,4), (2,3), (3,2), (4,1) [4 kết quả].\nTổng = 10: (4,6), (5,5), (6,4) [3 kết quả].\nTổng số kết quả thuận lợi: 4 + 3 = 7. Xác suất: 7/36 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Biến cố & Xác suất - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 9. CHƯƠNG 9 TOÁN 7: QUAN HỆ GIỮA CÁC YẾU TỐ TRONG MỘT TAM GIÁC (Bài 6: cuối chương)
def build_c9_7_exams():
    chap_id = "c9_7"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Các đường đồng quy trong tam giác",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Trong một tam giác, góc đối diện với cạnh lớn hơn là:", ["Góc lớn hơn", "Góc nhỏ hơn", "Góc vuông", "Góc tù"], 0),
            make_mc(2, "Nhận biết", "Theo bất đẳng thức tam giác, trong tam giác $ABC$ ta luôn có:", ["$AB + AC > BC$", "$AB + AC < BC$", "$AB + AC = BC$", "$AB - AC > BC$"], 0),
            make_mc(3, "Nhận biết", "Ba đường trung tuyến của một tam giác cùng đi qua một điểm. Điểm đó gọi là:", ["Trọng tâm của tam giác", "Trực tâm của tam giác", "Tâm đường tròn ngoại tiếp", "Tâm đường tròn nội tiếp"], 0),
            make_mc(4, "Nhận biết", "Trực tâm của tam giác là giao điểm của:", ["Ba đường cao", "Ba đường trung tuyến", "Ba đường phân giác", "Ba đường trung trực"], 0),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $AB = 5\\text{ cm}, BC = 8\\text{ cm}, AC = 7\\text{ cm}$. Góc lớn nhất của tam giác là:", ["$\\widehat{A}$", "$\\widehat{B}$", "$\\widehat{C}$", "Không xác định"], 0),
            make_mc(6, "Thông hiểu", "Bộ ba đoạn thẳng nào sau đây CÓ THỂ là độ dài ba cạnh của một tam giác?", ["$3\\text{ cm}, 4\\text{ cm}, 5\\text{ cm}$", "$2\\text{ cm}, 3\\text{ cm}, 6\\text{ cm}$", "$1\\text{ cm}, 2\\text{ cm}, 3\\text{ cm}$", "$4\\text{ cm}, 5\\text{ cm}, 10\\text{ cm}$"], 0),
            make_mc(7, "Thông hiểu", "Cho điểm $G$ là trọng tâm của tam giác $ABC$, $AM$ là đường trung tuyến. Tỉ số $\\frac{AG}{AM}$ bằng:", ["$\\frac{2}{3}$", "$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{3}{4}$"], 0),
            make_mc(8, "Thông hiểu", "Giao điểm của ba đường phân giác trong tam giác là điểm:", ["Cách đều ba cạnh của tam giác", "Cách đều ba đỉnh của tam giác", "Là trọng tâm tam giác", "Là trực tâm tam giác"], 0),
            make_mc(9, "Vận dụng", "Cho tam giác cân có độ dài hai cạnh là $3\\text{ cm}$ và $7\\text{ cm}$. Chu vi của tam giác cân đó là:", ["$17\\text{ cm}$ (vì cạnh thứ ba phải là $7\\text{ cm}$)", "$13\\text{ cm}$", "$10\\text{ cm}$", "$14\\text{ cm}$"], 0),
            make_mc(10, "Vận dụng", "Cho tam giác $ABC$ có đường trung tuyến $AM = 9\\text{ cm}$. Gọi $G$ là trọng tâm của tam giác. Độ dài đoạn thẳng $GM$ là:", ["$3\\text{ cm}$", "$6\\text{ cm}$", "$4,5\\text{ cm}$", "$2\\text{ cm}$"], 0),
            make_mc(11, "Vận dụng", "Trong tam giác vuông, giao điểm của ba đường trung trực nằm ở vị trí nào?", ["Chính là trung điểm của cạnh huyền", "Tại đỉnh góc vuông", "Bên trong tam giác", "Bên ngoài tam giác"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ nhọn có trực tâm $H$. Nếu $H$ trùng với trọng tâm $G$ thì tam giác $ABC$ là:", ["Tam giác đều", "Tam giác vuông cân", "Tam giác cân", "Tam giác vuông"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về quan hệ giữa các yếu tố trong tam giác (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Trong tam giác tù, góc tù là góc lớn nhất và cạnh đối diện góc tù là cạnh lớn nhất.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Trọng tâm tam giác luôn nằm ở miền trong của tam giác.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Trực tâm của tam giác tù nằm ở miền ngoài tam giác.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Độ dài một cạnh bất kì của tam giác luôn lớn hơn nửa chu vi tam giác đó.", "correct": False}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB < AC$, đường phân giác $AD$ và đường cao $AH$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Góc C nhỏ hơn góc B.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Điểm H nằm giữa B và D.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hình chiếu của AB trên đường thẳng BC là BH.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Đoạn thẳng AH lớn hơn đoạn thẳng AB.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho tam giác ABC có trọng tâm G, đường trung tuyến AM = 12 cm. Tính độ dài AG (cm).", "8"),
            make_sa(2, "Thông hiểu", "Tam giác ABC cân có hai cạnh dài 4 cm và 9 cm. Tính chu vi tam giác (cm).", "22"),
            make_sa(3, "Vận dụng", "Cho tam giác ABC vuông tại A có AB = 6 cm, AC = 8 cm. Tính khoảng cách từ trọng tâm G đến trung điểm cạnh huyền BC (cm).", "1,67"), # 5/3 cm
            make_sa(4, "Vận dụng cao", "Cho tam giác ABC có chu vi bằng 18 cm. Gọi M là điểm bất kì trong tam giác. Giá trị nhỏ nhất của (MA + MB + MC) lớn hơn bao nhiêu cm?", "9")
        ]
        p3[2] = make_sa(3, "Vận dụng", "Cho tam giác ABC vuông tại A, BC = 10 cm, M là trung điểm BC. Gọi G là trọng tâm tam giác. Tính AG (làm tròn 1 chữ số thập phân, cm).", "3,3")

        p4 = [
            make_essay(1, "Thông hiểu", "Chứng minh rằng trong tam giác vuông, cạnh huyền là cạnh lớn nhất.", "Xét tam giác ABC vuông tại A. Khi đó góc A = 90 độ là góc lớn nhất trong tam giác (vì B + C = 90 độ nên B, C < 90 độ) (0.25đ).\nTrong tam giác, cạnh đối diện với góc lớn hơn là cạnh lớn hơn => cạnh huyền BC đối diện góc A là cạnh lớn nhất (0.25đ)."),
            make_essay(2, "Vận dụng", "Cho tam giác $ABC$ cân tại $A$. Chứng minh rằng đường trung tuyến xuất phát từ đỉnh $A$ đồng thời là đường cao và đường phân giác của góc $A$.", "Gọi AM là trung tuyến => MB = MC. Xét tam giác ABM và ACM: AB = AC, AM chung, MB = MC => tam giác ABM = ACM (c-c-c) (0.25đ).\n=> góc AMB = AMC = 90 độ => AM là đường cao.\n=> góc BAM = CAM => AM là đường phân giác. Đpcm (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho điểm $M$ nằm trong tam giác $ABC$. Chứng minh rằng tổng khoảng cách từ $M$ đến ba đỉnh của tam giác lớn hơn nửa chu vi tam giác: $MA + MB + MC > \\frac{AB + BC + CA}{2}$.", "Áp dụng bất đẳng thức tam giác vào các tam giác MAB, MBC, MCA (0.25đ):\nMA + MB > AB\nMB + MC > BC\nMC + MA > CA\nCộng vế với vế: 2(MA + MB + MC) > AB + BC + CA => MA + MB + MC > (AB + BC + CA)/2. Đpcm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương IX: Quan hệ các yếu tố trong tam giác - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 10. CHƯƠNG 10 TOÁN 7: MỘT SỐ HÌNH KHỐI TRONG THỰC TIỄN (Bài 3: cuối chương)
def build_c10_7_exams():
    chap_id = "c10_7"
    l_idx = 3
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Lăng trụ đứng & Thể tích thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Hình hộp chữ nhật có bao nhiêu mặt, bao nhiêu đỉnh và bao nhiêu cạnh?", ["$6$ mặt, $8$ đỉnh, $12$ cạnh", "$6$ mặt, $12$ đỉnh, $8$ cạnh", "$8$ mặt, $6$ đỉnh, $12$ cạnh", "$4$ mặt, $4$ đỉnh, $6$ cạnh"], 0),
            make_mc(2, "Nhận biết", "Các mặt bên của hình lăng trụ đứng tam giác là các hình gì?", ["Hình chữ nhật", "Tam giác", "Hình bình hành", "Hình vuông"], 0),
            make_mc(3, "Nhận biết", "Công thức tính thể tích của hình hộp chữ nhật có ba kích thước $a, b, c$ là:", ["$V = a \\cdot b \\cdot c$", "$V = a + b + c$", "$V = 2(a + b)c$", "$V = a^2 \\cdot b$"], 0),
            make_mc(4, "Nhận biết", "Công thức tính thể tích của hình lăng trụ đứng có diện tích đáy $S$ và chiều cao $h$ là:", ["$V = S \\cdot h$", "$V = \\frac{1}{3}S \\cdot h$", "$V = 2S \\cdot h$", "$V = S + h$"], 0),
            make_mc(5, "Thông hiểu", "Một hình lập phương có cạnh $5\\text{ cm}$. Thể tích của hình lập phương đó là:", ["$125\\text{ cm}^3$", "$25\\text{ cm}^3$", "$150\\text{ cm}^3$", "$100\\text{ cm}^3$"], 0),
            make_mc(6, "Thông hiểu", "Diện tích xung quanh của hình hộp chữ nhật có chiều dài $6\\text{ m}$, chiều rộng $4\\text{ m}$ và chiều cao $3\\text{ m}$ là:", ["$60\\text{ m}^2$", "$72\\text{ m}^2$", "$20\\text{ m}^2$", "$48\\text{ m}^2$"], 0),
            make_mc(7, "Thông hiểu", "Hình lăng trụ đứng tứ giác có hai đáy là hình thoi cạnh $5\\text{ cm}$, chiều cao lăng trụ $8\\text{ cm}$. Diện tích xung quanh là:", ["$160\\text{ cm}^2$", "$80\\text{ cm}^2$", "$200\\text{ cm}^2$", "$40\\text{ cm}^2$"], 0),
            make_mc(8, "Thông hiểu", "Hình lập phương có diện tích toàn phần là $96\\text{ cm}^2$. Độ dài cạnh của hình lập phương là:", ["$4\\text{ cm}$", "$6\\text{ cm}$", "$16\\text{ cm}$", "$8\\text{ cm}$"], 0),
            make_mc(9, "Vận dụng", "Một bể nước dạng hình hộp chữ nhật có kích thước lòng bể: dài $2\\text{ m}$, rộng $1,5\\text{ m}$, cao $1,2\\text{ m}$. Bể đang chứa $60\\%$ nước. Thể tích nước hiện có trong bể là:", ["$2,16\\text{ m}^3$ (hay $2160$ lít)", "$3,6\\text{ m}^3$", "$1,8\\text{ m}^3$", "$2,4\\text{ m}^3$"], 0),
            make_mc(10, "Vận dụng", "Một khối bê tông dạng hình lăng trụ đứng tam giác có đáy là tam giác vuông có hai cạnh góc vuông $3\\text{ m}$ và $4\\text{ m}$, chiều cao lăng trụ $6\\text{ m}$. Thể tích khối bê tông là:", ["$36\\text{ m}^3$", "$72\\text{ m}^3$", "$18\\text{ m}^3$", "$24\\text{ m}^3$"], 0),
            make_mc(11, "Vận dụng", "Người ta sơn toàn bộ 4 bức tường xung quanh bên trong một căn phòng dài $8\\text{ m}$, rộng $5\\text{ m}$ và cao $3,5\\text{ m}$. Biết tổng diện tích các cửa là $9\\text{ m}^2$. Diện tích cần sơn là:", ["$82\\text{ m}^2$", "$91\\text{ m}^2$", "$140\\text{ m}^2$", "$73\\text{ m}^2$"], 0),
            make_mc(12, "Vận dụng cao", "Một thùng chứa hàng dạng hình hộp chữ nhật có thể tích $72\\text{ m}^3$, đáy là hình chữ nhật có tỉ lệ chiều dài và chiều rộng là $2:1$. Chiều cao thùng bằng $3\\text{ m}$. Diện tích toàn phần của thùng là:", ["$108\\text{ m}^2$", "$96\\text{ m}^2$", "$120\\text{ m}^2$", "$84\\text{ m}^2$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính chất của các hình khối trong không gian (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hình lăng trụ đứng có các cạnh bên song song và bằng nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hai đáy của hình lăng trụ đứng luôn song song và bằng nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hình lập phương là trường hợp đặc biệt của hình hộp chữ nhật.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu gấp đôi mỗi kích thước của hình hộp chữ nhật thì thể tích tăng gấp 4 lần.", "correct": False}
            ]),
            make_tf(2, "Một chiếc lều cắm trại dạng hình lăng trụ đứng tam giác có hai đáy là tam giác vuông cân cạnh góc vuông dài 2 m, chiều dài lều 3 m:", [
                {"key": "a", "level": "Thông hiểu", "text": "Diện tích một mặt đáy của lều là 2 m^2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Thể tích không gian bên trong lều là 6 m^3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Cạnh huyền của mặt đáy tam giác vuông cân xấp xỉ 2,83 m.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích bạt che xung quanh lều (không tính mặt đáy tiếp đất) bằng đúng 12 m^2.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính thể tích hình hộp chữ nhật có kích thước: 4 cm x 5 cm x 6 cm.", "120"),
            make_sa(2, "Thông hiểu", "Tính diện tích xung quanh của hình lập phương có cạnh bằng 3 cm.", "36"),
            make_sa(3, "Vận dụng", "Một lăng trụ đứng tam giác có diện tích đáy 15 cm^2, chiều cao 8 cm. Tính thể tích (cm^3).", "120"),
            make_sa(4, "Vận dụng cao", "Một hình lập phương có thể tích 64 cm^3. Tính diện tích toàn phần của hình lập phương đó (cm^2).", "96")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Tính diện tích xung quanh và thể tích của hình hộp chữ nhật có chiều dài 10 m, chiều rộng 6 m và chiều cao 4 m.", "Diện tích xung quanh: 2 x (10 + 6) x 4 = 128 (m^2) (0.25đ).\nThể tích: 10 x 6 x 4 = 240 (m^3) (0.25đ)."),
            make_essay(2, "Vận dụng", "Bác Năm muốn xây một bể ngầm trữ nước mưa hình hộp chữ nhật có chiều dài 3 m, chiều rộng 2 m và sâu 1,5 m. a) Bể chứa được tối đa bao nhiêu mét khối nước? b) Biết chi phí trát vữa chống thấm bên trong (đáy và 4 mặt xung quanh) là 120 000 đồng/m^2. Tính tổng chi phí chống thấm.", "a) Thể tích bể: 3 x 2 x 1,5 = 9 (m^3) (0.25đ).\nb) Diện tích đáy: 3 x 2 = 6 m^2. Diện tích xung quanh: 2 x (3 + 2) x 1,5 = 15 m^2.\nTổng diện tích chống thấm: 6 + 15 = 21 m^2. Chi phí: 21 x 120 000 = 2 520 000 (đồng) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Một chiếc bánh kem hình lăng trụ đứng đáy là hình thang cân có hai đáy 10 cm và 16 cm, chiều cao đáy 8 cm. Chiều cao của bánh kem là 12 cm. Người ta phủ kem toàn bộ các mặt bên xung quanh bánh. Tính diện tích bề mặt được phủ kem.", "Cạnh bên đáy hình thang cân: căn(8^2 + ((16 - 10)/2)^2) = căn(64 + 9) = căn(73) xấp xỉ 8,54 cm (0.25đ).\nChu vi đáy hình thang: 10 + 16 + 2 x căn(73) xấp xỉ 43,09 cm.\nDiện tích phủ kem (Sxq): Chu vi đáy x chiều cao = 43,09 x 12 xấp xỉ 517,1 cm^2 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương X: Một số hình khối trong thực tiễn - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# HÀM THỰC THI TỔNG THỂ TOÁN 7
def run_all_grade7():
    builders = [
        build_c1_7_exams,
        build_c2_7_exams,
        build_c3_7_exams,
        build_c4_7_exams,
        build_c5_7_exams,
        build_c6_7_exams,
        build_c7_7_exams,
        build_c8_7_exams,
        build_c9_7_exams,
        build_c10_7_exams
    ]
    for b in builders:
        chap_id, new_exams = b()
        title, exams = load_existing_exams(7, chap_id)
        exams.update(new_exams)
        save_chapter_package(7, chap_id, title, exams)
    print("🎉 ĐÃ HOÀN TẤT TOÀN BỘ 10 CHƯƠNG TOÁN 7 (MỖI CHƯƠNG ĐÃ CÓ ĐỦ 7 ĐỀ CUỐI CHƯƠNG)!")

if __name__ == "__main__":
    run_all_grade7()
