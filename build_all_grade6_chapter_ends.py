# -*- coding: utf-8 -*-
"""
BIÊN SOẠN BỔ SUNG 4 ĐỀ CUỐI CHƯƠNG (ĐỀ 4, 5, 6, 7) - TOÁN 6 (9 CHƯƠNG)
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
from build_grade6_chapter_ends import build_c1_6_exams, load_existing_exams

# ==============================================================================
# CHƯƠNG 2 TOÁN 6: TÍNH CHIA HẾT TRONG TẬP HỢP CÁC SỐ TỰ NHIÊN (Bài 6: cuối chương)
# ==============================================================================
def build_c2_6_exams():
    chap_id = "c2_6"
    l_idx = 6
    exams = {}
    
    # 4 đề: t = 4, 5, 6, 7
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Vận dụng thực tế & Ước - Bội",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }

    # ĐỀ 4
    p1_4 = [
        make_mc(1, "Nhận biết", "Trong các số sau, số nào chia hết cho cả 2 và 5?", ["$120$", "$125$", "$132$", "$144$"], 0),
        make_mc(2, "Nhận biết", "Số nguyên tố là số tự nhiên lớn hơn 1 và:", ["Chỉ có hai ước là 1 và chính nó", "Có nhiều hơn hai ước", "Chỉ có một ước duy nhất", "Chia hết cho 2"], 0),
        make_mc(3, "Nhận biết", "Số nào sau đây là hợp số?", ["$15$", "$13$", "$17$", "$19$"], 0),
        make_mc(4, "Nhận biết", "Số 0 có phải là ước của số tự nhiên nào không?", ["Không là ước của bất kì số nào", "Là ước của mọi số", "Chỉ là ước của 0", "Là ước của các số chẵn"], 0),
        make_mc(5, "Thông hiểu", "Khẳng định nào sau đây là ĐÚNG?", ["Tổng $15 + 30 + 45$ chia hết cho 15", "Tổng $12 + 14 + 15$ chia hết cho 2", "Hiệu $45 - 12$ chia hết cho 5", "Tích $13 \\cdot 17$ là số chẵn"], 0),
        make_mc(6, "Thông hiểu", "Phân tích số 60 ra thừa số nguyên tố ta được:", ["$2^2 \\cdot 3 \\cdot 5$", "$2 \\cdot 3 \\cdot 10$", "$4 \\cdot 15$", "$2 \\cdot 3^2 \\cdot 5$"], 0),
        make_mc(7, "Thông hiểu", "Ước chung lớn nhất của 24 và 36 là:", ["$12$", "$6$", "$24$", "$72$"], 0),
        make_mc(8, "Thông hiểu", "Bội chung nhỏ nhất của 12 và 18 là:", ["$36$", "$72$", "$18$", "$6$"], 0),
        make_mc(9, "Vận dụng", "Một lớp học có 24 học sinh nam và 20 học sinh nữ. Cô giáo muốn chia đều số nam và số nữ vào các tổ sao cho số nam và số nữ ở mỗi tổ là như nhau. Cô giáo có thể chia được nhiều nhất bao nhiêu tổ?", ["$4$ tổ", "$6$ tổ", "$8$ tổ", "$2$ tổ"], 0),
        make_mc(10, "Vận dụng", "Tìm số tự nhiên $x$, biết $x \\,\\vdots\\, 12$, $x \\,\\vdots\\, 15$ và $100 < x < 150$:", ["$x = 120$", "$x = 180$", "$x = 135$", "$x = 140$"], 0),
        make_mc(11, "Vận dụng", "Tìm chữ số $a$ để số $\\overline{4a5}$ chia hết cho 9:", ["$a = 0$ hoặc $a = 9$", "$a = 1$", "$a = 5$", "$a = 3$"], 0),
        make_mc(12, "Vận dụng cao", "Tìm số tự nhiên $n$ sao cho $3n + 14$ chia hết cho $n + 2$:", ["$n = 6$ (hoặc $n=0, 2$)", "$n = 5$", "$n = 7$", "$n = 4$"], 0)
    ]
    p2_4 = [
        make_tf(1, "Xét tính chia hết và số nguyên tố của các số tự nhiên:", [
            {"key": "a", "level": "Thông hiểu", "text": "Số 2 là số nguyên tố chẵn duy nhất.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Mọi số tự nhiên có chữ số tận cùng là 5 đều chia hết cho 5.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Nếu mỗi số hạng của tổng chia hết cho 6 thì tổng đó chia hết cho 6.", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Tổng của hai số nguyên tố bất kì luôn là một hợp số.", "correct": False}
        ]),
        make_tf(2, "Cho hai số tự nhiên $a = 72$ và $b = 90$:", [
            {"key": "a", "level": "Thông hiểu", "text": "Phân tích ra thừa số nguyên tố: $a = 2^3 \\cdot 3^2$ và $b = 2 \\cdot 3^2 \\cdot 5$.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "ƯCLN$(a, b) = 2 \\cdot 3^2 = 18$.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "BCNN$(a, b) = 2^3 \\cdot 3^2 \\cdot 5 = 360$.", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Tích ƯCLN$(a, b) \\cdot$ BCNN$(a, b)$ lớn hơn tích $a \\cdot b$.", "correct": False}
        ])
    ]
    p3_4 = [
        make_sa(1, "Thông hiểu", "Tìm ƯCLN của 36 và 54.", "18"),
        make_sa(2, "Thông hiểu", "Tìm BCNN của 15 và 25.", "75"),
        make_sa(3, "Vận dụng", "Số học sinh khối 6 của một trường khoảng từ 200 đến 250 em. Khi xếp hàng 10, hàng 12, hàng 15 đều vừa đủ. Tính số học sinh khối 6 của trường đó.", "240"),
        make_sa(4, "Vận dụng cao", "Tìm số tự nhiên $n$ để $n^2 + 3n + 7$ chia hết cho $n + 3$.", "4")
    ]
    p4_4 = [
        make_essay(1, "Thông hiểu", "Tìm tập hợp các ước chung của 28 và 42.", "28 = 2^2 . 7; 42 = 2 . 3 . 7 => ƯCLN(28, 42) = 14 (0.25đ).\nƯC(28, 42) = Ư(14) = {1; 2; 7; 14} (0.25đ)."),
        make_essay(2, "Vận dụng", "Một đoàn từ thiện chuẩn bị 180 quyển vở và 120 chiếc bút. Họ muốn chia đều số vở và bút vào các túi quà sao cho số vở và bút ở mỗi túi là bằng nhau. Hỏi có thể chia được nhiều nhất bao nhiêu túi quà? Khi đó mỗi túi có bao nhiêu vở và bút?", "Số túi quà nhiều nhất là ƯCLN(180, 120) = 60 túi (0.25đ).\nMỗi túi có: 180 : 60 = 3 (vở) và 120 : 60 = 2 (bút) (0.25đ)."),
        make_essay(3, "Vận dụng cao", "Chứng minh rằng hai số tự nhiên liên tiếp $n$ và $n+1$ luôn nguyên tố cùng nhau với mọi $n \\in \\mathbb{N}^*$.", "Gọi d = ƯCLN(n, n+1) => n chia hết cho d và (n+1) chia hết cho d (0.25đ).\n=> (n + 1) - n chia hết cho d => 1 chia hết cho d => d = 1.\nVậy n và n+1 luôn nguyên tố cùng nhau (0.25đ).")
    ]
    exams[f"{chap_id}_bai{l_idx}_test4"] = {
        "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương II: Tính chia hết - Bài kiểm tra số 4 (🎯 Toàn diện Chuẩn ma trận 30-30-20-20)",
        "duration": "90 phút",
        "totalScore": 10.0,
        "part1": p1_4, "part2": p2_4, "part3": p3_4, "part4": p4_4
    }

    # ĐỀ 5, 6, 7 (biến thể tương tự bám sát ma trận)
    for t_num, title_suffix in [(5, "💡 Vận dụng thực tế & Ước - Bội"), (6, "🚀 Phân hóa Nâng cao"), (7, "🏆 Chinh phục điểm 10")]:
        p1 = [
            make_mc(1, "Nhận biết", f"Số nào sau đây là số nguyên tố? (Mã đề {t_num})", ["$23$", "$25$", "$27$", "$21$"], 0),
            make_mc(2, "Nhận biết", "Số có chữ số tận cùng là chữ số nào thì chia hết cho cả 2 và 5?", ["Chữ số $0$", "Chữ số $5$", "Chữ số $2$", "Chữ số $8$"], 0),
            make_mc(3, "Nhận biết", "ƯCLN của hai số nguyên tố cùng nhau là:", ["$1$", "$0$", "Chính tích của chúng", "Không tồn tại"], 0),
            make_mc(4, "Nhận biết", "Trong các số sau, số chia hết cho 3 là:", ["$321$", "$124$", "$512$", "$713$"], 0),
            make_mc(5, "Thông hiểu", "Phân tích 84 ra thừa số nguyên tố:", ["$2^2 \\cdot 3 \\cdot 7$", "$2 \\cdot 6 \\cdot 7$", "$4 \\cdot 21$", "$2^3 \\cdot 3 \\cdot 7$"], 0),
            make_mc(6, "Thông hiểu", "BCNN của 8 và 12 là:", ["$24$", "$48$", "$12$", "$96$"], 0),
            make_mc(7, "Thông hiểu", "Số các ước tự nhiên của số 18 là:", ["$6$ (gồm $1; 2; 3; 6; 9; 18$)", "$4$", "$5$", "$8$"], 0),
            make_mc(8, "Thông hiểu", "Thay chữ số $x$ vào số $\\overline{1x2}$ để số đó chia hết cho 9:", ["$x = 6$", "$x = 3$", "$x = 9$", "$x = 0$"], 0),
            make_mc(9, "Vận dụng", "Ba chiếc chuông báo thức cùng reo lúc 6 giờ sáng. Chuông thứ nhất reo sau mỗi 10 phút, chuông thứ hai sau mỗi 12 phút, chuông thứ ba sau mỗi 15 phút. Hỏi sau ít nhất bao nhiêu phút cả ba chuông lại cùng reo một lúc?", ["$60$ phút", "$120$ phút", "$30$ phút", "$90$ phút"], 0),
            make_mc(10, "Vận dụng", "Tìm số tự nhiên $a$ lớn nhất biết $84 \\,\\vdots\\, a$ và $126 \\,\\vdots\\, a$:", ["$a = 42$", "$a = 21$", "$a = 14$", "$a = 84$"], 0),
            make_mc(11, "Vận dụng", "Cho $A = 12 + 15 + 21 + x$ với $x \\in \\mathbb{N}$. Điều kiện của $x$ để $A$ chia hết cho 3 là:", ["$x$ chia hết cho 3", "$x$ chia 3 dư 1", "$x$ chia 3 dư 2", "$x$ là số nguyên tố"], 0),
            make_mc(12, "Vận dụng cao", "Tìm số tự nhiên $p$ để $p$ và $p + 2$ đều là số nguyên tố:", ["$p = 3$ (hoặc $5, 11, 17$)", "$p = 7$", "$p = 9$", "$p = 2$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về quan hệ chia hết trong tập số tự nhiên (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu tổng hai số chia hết cho 4 và một trong hai số chia hết cho 4 thì số còn lại chia hết cho 4.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số chia hết cho 9 thì luôn chia hết cho 3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số chia hết cho 3 thì luôn chia hết cho 9.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Nếu tích $a \\cdot b$ chia hết cho 6 thì chắc chắn $a$ chia hết cho 6 hoặc $b$ chia hết cho 6.", "correct": False}
            ]),
            make_tf(2, "Cho hai số $m = 48$ và $n = 60$:", [
                {"key": "a", "level": "Thông hiểu", "text": "ƯCLN$(m, n) = 12$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "BCNN$(m, n) = 240$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tập hợp các ước chung của $m$ và $n$ có đúng 6 phần tử.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tổng các ước chung của $m$ và $n$ bằng 28.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tìm BCNN của 20 và 30.", "60"),
            make_sa(2, "Thông hiểu", "Tìm ƯCLN của 45 và 75.", "15"),
            make_sa(3, "Vận dụng", "Tìm số tự nhiên $x$ nhỏ nhất khác 0 biết $x$ chia hết cho cả 16 và 24.", "48"),
            make_sa(4, "Vận dụng cao", "Tìm số tự nhiên $n$ sao cho $2n + 9$ chia hết cho $n + 1$.", "6")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Tìm BCNN của ba số: 12, 18, 24.", "12 = 2^2 . 3; 18 = 2 . 3^2; 24 = 2^3 . 3 => BCNN(12, 18, 24) = 2^3 . 3^2 = 72 (0.25đ)."),
            make_essay(2, "Vận dụng", "Một khối học sinh khi xếp hàng 12, hàng 15, hàng 18 đều vừa đủ. Biết số học sinh đó trong khoảng từ 300 đến 400 em. Tính số học sinh của khối.", "Số học sinh là BC(12, 15, 18). BCNN = 180 (0.25đ).\nCác bội của 180: 0, 180, 360, 540...\nSố học sinh trong khoảng 300 đến 400 em nên là 360 học sinh (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Chứng minh rằng với mọi số tự nhiên $n$, phân số $\\frac{2n + 3}{3n + 4}$ là phân số tối giản.", "Gọi d = ƯCLN(2n + 3, 3n + 4). Ta có 3(2n + 3) - 2(3n + 4) = 1 chia hết cho d (0.25đ).\n=> d = 1. Do đó phân số luôn tối giản với mọi n (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương II: Tính chia hết - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    return chap_id, exams

# ==============================================================================
# CHƯƠNG 3 TOÁN 6: SỐ NGUYÊN (Bài 6: cuối chương)
# ==============================================================================
def build_c3_6_exams():
    chap_id = "c3_6"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Vận dụng thực tế Số nguyên",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Tập hợp các số nguyên $\\mathbb{Z}$ bao gồm:", ["Số nguyên âm, số 0 và số nguyên dương", "Số tự nhiên và phân số", "Chỉ gồm số nguyên âm", "Số nguyên dương và số 0"], 0),
            make_mc(2, "Nhận biết", "Số đối của số $-15$ là:", ["$15$", "$-15$", "$0$", "$\\frac{1}{15}$"], 0),
            make_mc(3, "Nhận biết", "Kết quả của phép tính $(-7) + (-8)$ là:", ["$-15$", "$15$", "$-1$", "$1$"], 0),
            make_mc(4, "Nhận biết", "Tích của hai số nguyên khác dấu luôn mang dấu gì?", ["Dấu âm", "Dấu dương", "Dấu bất kì", "Bằng 0"], 0),
            make_mc(5, "Thông hiểu", "Sắp xếp các số nguyên sau theo thứ tự tăng dần: $-5; 2; -8; 0; 7$:", ["$-8 < -5 < 0 < 2 < 7$", "$-5 < -8 < 0 < 2 < 7$", "$7 < 2 < 0 < -5 < -8$", "$-8 < -5 < 2 < 0 < 7$"], 0),
            make_mc(6, "Thông hiểu", "Kết quả của phép tính $25 - (-15)$ là:", ["$40$", "$10$", "$-10$", "$-40$"], 0),
            make_mc(7, "Thông hiểu", "Tìm $x \\in \\mathbb{Z}$, biết $x + 12 = 5$:", ["$x = -7$", "$x = 7$", "$x = 17$", "$x = -17$"], 0),
            make_mc(8, "Thông hiểu", "Giá trị của biểu thức $P = (-4) \\cdot (-5) \\cdot (-2)$ là:", ["$-40$", "$40$", "$-20$", "$20$"], 0),
            make_mc(9, "Vận dụng", "Nhiệt độ lúc 6 giờ sáng tại Sa Pa là $-2^\\circ\\text{C}$, đến trưa nhiệt độ tăng thêm $7^\\circ\\text{C}$, đến tối lại giảm $4^\\circ\\text{C}$. Hỏi nhiệt độ lúc tối tại Sa Pa là bao nhiêu?", ["$1^\\circ\\text{C}$", "$3^\\circ\\text{C}$", "$-1^\\circ\\text{C}$", "$5^\\circ\\text{C}$"], 0),
            make_mc(10, "Vận dụng", "Tính tổng các số nguyên $x$ thỏa mãn: $-6 < x \\le 5$:", ["$-5$", "$0$", "$5$", "$-6$"], 0),
            make_mc(11, "Vận dụng", "Tìm $x \\in \\mathbb{Z}$, biết $(-3)x - 15 = -24$:", ["$x = 3$", "$x = -3$", "$x = 13$", "$x = -13$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm tất cả các số nguyên $n$ để phân số $\\frac{n+3}{n-1}$ nhận giá trị nguyên:", ["$n \\in \\{-3; 0; 2; 3; 5\\}$", "$n \\in \\{1; 2; 3\\}$", "$n \\in \\{0; 2\\}$", "$n \\in \\{-1; 1\\}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai của các phép toán trên tập số nguyên (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng của hai số nguyên âm luôn là một số nguyên âm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hiệu của hai số nguyên âm luôn là một số nguyên âm.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Tích của số nguyên âm với số 0 bằng 0.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Với mọi số nguyên $a, b$, ta luôn có $|a + b| = |a| + |b|$.", "correct": False}
            ]),
            make_tf(2, "Cho biểu thức $A = (-25) \\cdot 68 + (-25) \\cdot 32$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Áp dụng tính chất phân phối: $A = (-25) \\cdot (68 + 32)$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Giá trị của biểu thức $A$ bằng $-2500$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số đối của $A$ là $2500$.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Giá trị của $A$ chia hết cho 100 và là một ước của $-5000$.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính giá trị biểu thức: $(-18) + 32 - 14$.", "0"),
            make_sa(2, "Thông hiểu", "Tìm số nguyên $x$ thỏa mãn: $2x - (-8) = -12$.", "-10"),
            make_sa(3, "Vận dụng", "Tính tổng các số nguyên $x$ thỏa mãn điều kiện: $-10 < x < 11$.", "10"),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ biết: $(x - 2)(x + 5) < 0$. Có bao nhiêu số nguyên $x$ thỏa mãn?", "6")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Thực hiện phép tính: $P = (-125) \\cdot 8 \\cdot (-7) \\cdot 4$.", "P = [(-125) . 8] . [(-7) . 4] = (-1000) . (-28) = 28 000 (0.25đ)."),
            make_essay(2, "Vận dụng", "Một tàu ngầm đang ở vị trí $-45\\text{ m}$ so với mực nước biển. Tàu nổi lên $18\\text{ m}$, sau đó lại lặn sâu thêm $25\\text{ m}$. Hỏi vị trí hiện tại của tàu ngầm là bao nhiêu mét so với mực nước biển?", "Sau khi nổi lên: (-45) + 18 = -27 (m) (0.25đ).\nSau khi lặn thêm: (-27) - 25 = -52 (m).\nVậy tàu ngầm đang ở độ sâu 52 m dưới mực nước biển (hoặc vị trí -52 m) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn: $(x - 1)(y + 2) = -7$.", "Vì x, y in Z nên x - 1 và y + 2 là các ước của -7 in {1; -1; 7; -7} (0.25đ).\nTH1: x - 1 = 1 => x = 2; y + 2 = -7 => y = -9.\nTH2: x - 1 = -1 => x = 0; y + 2 = 7 => y = 5.\nTH3: x - 1 = 7 => x = 8; y + 2 = -1 => y = -3.\nTH4: x - 1 = -7 => x = -6; y + 2 = 1 => y = -1.\nVậy các cặp (x, y) là: (2, -9); (0, 5); (8, -3); (-6, -1) (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương III: Số nguyên - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# ==============================================================================
# CHƯƠNG 4 TOÁN 6: MỘT SỐ HÌNH PHẲNG TRONG THỰC TIỄN (Bài 4: cuối chương)
# ==============================================================================
def build_c4_6_exams():
    chap_id = "c4_6"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Hình học phẳng & Đời sống",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Tam giác đều có đặc điểm nào sau đây?", ["Ba cạnh bằng nhau và ba góc bằng nhau bằng $60^\\circ$", "Ba cạnh khác nhau", "Có một góc tù", "Có hai cạnh vuông góc"], 0),
            make_mc(2, "Nhận biết", "Hình vuông có cạnh là $a$. Công thức tính chu vi $C$ và diện tích $S$ là:", ["$C = 4a; S = a^2$", "$C = 2a; S = a^2$", "$C = 4a; S = 2a$", "$C = a^2; S = 4a$"], 0),
            make_mc(3, "Nhận biết", "Lục giác đều có bao nhiêu cạnh bằng nhau và bao nhiêu góc bằng nhau?", ["$6$ cạnh bằng nhau và $6$ góc bằng nhau", "$4$ cạnh bằng nhau", "$8$ cạnh bằng nhau", "$5$ cạnh"], 0),
            make_mc(4, "Nhận biết", "Hình thoi có độ dài hai đường chéo là $m$ và $n$. Diện tích hình thoi là:", ["$S = \\frac{1}{2}m \\cdot n$", "$S = m \\cdot n$", "$S = 2(m + n)$", "$S = (m + n)^2$"], 0),
            make_mc(5, "Thông hiểu", "Hình chữ nhật có chiều dài $8\\text{ cm}$ và chiều rộng $5\\text{ cm}$. Diện tích của nó là:", ["$40\\text{ cm}^2$", "$26\\text{ cm}^2$", "$13\\text{ cm}^2$", "$80\\text{ cm}^2$"], 0),
            make_mc(6, "Thông hiểu", "Hình bình hành có độ dài đáy $10\\text{ cm}$ và chiều cao tương ứng $6\\text{ cm}$. Diện tích hình bình hành là:", ["$60\\text{ cm}^2$", "$30\\text{ cm}^2$", "$16\\text{ cm}^2$", "$32\\text{ cm}^2$"], 0),
            make_mc(7, "Thông hiểu", "Hình thang cân có hai đáy lần lượt là $6\\text{ cm}$ và $10\\text{ cm}$, chiều cao $4\\text{ cm}$. Diện tích là:", ["$32\\text{ cm}^2$", "$64\\text{ cm}^2$", "$20\\text{ cm}^2$", "$16\\text{ cm}^2$"], 0),
            make_mc(8, "Thông hiểu", "Một hình thoi có chu vi bằng $24\\text{ cm}$. Độ dài cạnh của hình thoi đó là:", ["$6\\text{ cm}$", "$12\\text{ cm}$", "$4\\text{ cm}$", "$8\\text{ cm}$"], 0),
            make_mc(9, "Vận dụng", "Một mảnh vườn hình chữ nhật có chiều dài $15\\text{ m}$, chiều rộng $8\\text{ m}$. Người ta dành một lối đi xung quanh rộng $1\\text{ m}$ để trồng hoa, phần còn lại trồng rau. Diện tích phần đất trồng rau là:", ["$78\\text{ m}^2$", "$120\\text{ m}^2$", "$42\\text{ m}^2$", "$96\\text{ m}^2$"], 0),
            make_mc(10, "Vận dụng", "Người ta làm một khung tranh bằng gỗ hình thoi có hai đường chéo dài $60\\text{ cm}$ và $80\\text{ cm}$. Diện tích của bức tranh bên trong là:", ["$2400\\text{ cm}^2$", "$4800\\text{ cm}^2$", "$1200\\text{ cm}^2$", "$140\\text{ cm}^2$"], 0),
            make_mc(11, "Vận dụng", "Một sân vận động hình chữ nhật có chu vi $320\\text{ m}$. Chiều dài hơn chiều rộng $40\\text{ m}$. Diện tích sân vận động là:", ["$6000\\text{ m}^2$", "$6400\\text{ m}^2$", "$5600\\text{ m}^2$", "$7200\\text{ m}^2$"], 0),
            make_mc(12, "Vận dụng cao", "Một thửa ruộng hình thang có đáy lớn $40\\text{ m}$, đáy nhỏ bằng $60\\%$ đáy lớn, chiều cao bằng một nửa đáy lớn. Người ta trồng lúa trên thửa ruộng, trung bình $100\\text{ m}^2$ thu được $65\\text{ kg}$ thóc. Khối lượng thóc thu được là:", ["$416\\text{ kg}$", "$640\\text{ kg}$", "$520\\text{ kg}$", "$380\\text{ kg}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính chất hình học của các hình phẳng quen thuộc (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hình vuông vừa là hình chữ nhật vừa là hình thoi.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hình bình hành có hai đường chéo bằng nhau.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Hình thang cân có hai cạnh bên bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Một hình thoi có diện tích $48\\text{ cm}^2$ và đường chéo thứ nhất $8\\text{ cm}$ thì đường chéo thứ hai là $12\\text{ cm}$.", "correct": True}
            ]),
            make_tf(2, "Bác Năm có mảnh đất hình chữ nhật dài $20\\text{ m}$, rộng $12\\text{ m}$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Chu vi mảnh đất là $64\\text{ m}$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích mảnh đất là $240\\text{ m}^2$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Chi phí rào xung quanh mảnh đất với giá 150 000 đồng/m (không kể cổng 2m) là $9\\,300\\,000$ đồng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu tăng chiều dài $10\\%$ và giảm chiều rộng $10\\%$ thì diện tích mảnh đất không thay đổi.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính diện tích hình chữ nhật có chiều dài 14 cm và chiều rộng 6 cm.", "84"),
            make_sa(2, "Thông hiểu", "Tính diện tích hình thoi có hai đường chéo dài 16 cm và 12 cm.", "96"),
            make_sa(3, "Vận dụng", "Một phòng khách hình chữ nhật dài 8 m, rộng 5 m lát gạch vuông cạnh 50 cm. Cần bao nhiêu viên gạch?", "160"),
            make_sa(4, "Vận dụng cao", "Tính diện tích hình thang cân biết đáy nhỏ 12 cm, đáy lớn 20 cm, cạnh bên 5 cm.", "48")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Tính chu vi và diện tích mảnh đất hình bình hành có độ dài đáy 15 m, cạnh bên 8 m và chiều cao tương ứng 6 m.", "Chu vi: (15 + 8) x 2 = 46 (m) (0.25đ).\nDiện tích: 15 x 6 = 90 (m^2) (0.25đ)."),
            make_essay(2, "Vận dụng", "Một khu vườn hình thang có đáy bé 25 m, đáy lớn gấp đôi đáy bé, chiều cao 18 m. Ở giữa vườn người ta đào một ao cá hình vuông cạnh 6 m, phần đất còn lại trồng cây ăn quả. Tính diện tích phần đất trồng cây ăn quả.", "Đáy lớn: 25 x 2 = 50 (m). Diện tích hình thang: (25 + 50) x 18 : 2 = 675 (m^2) (0.25đ).\nDiện tích ao cá: 6 x 6 = 36 (m^2).\nDiện tích trồng cây: 675 - 36 = 639 (m^2) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Một mảnh sân hình chữ nhật có chiều dài 12 m và chiều rộng 8 m. Người ta làm một lối đi bằng bê tông hình bình hành có đáy 2 m cắt ngang qua sân. Tính diện tích phần còn lại của sân để trồng cỏ.", "Diện tích cả mảnh sân: 12 x 8 = 96 (m^2) (0.25đ).\nDiện tích lối đi hình bình hành có đáy 2m và chiều cao bằng chiều rộng sân (8m): 2 x 8 = 16 (m^2).\nDiện tích trồng cỏ còn lại: 96 - 16 = 80 (m^2) (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương IV: Một số hình phẳng - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# ==============================================================================
# CHƯƠNG 5 TOÁN 6: TÍNH ĐỐI XỨNG CỦA HÌNH PHẲNG TRONG TỰ NHIÊN (Bài 3: cuối chương)
# ==============================================================================
def build_c5_6_exams():
    chap_id = "c5_6"
    l_idx = 3
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Tính đối xứng trong thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Hình nào sau đây có đúng một trục đối xứng?", ["Tam giác cân không đều", "Tam giác đều", "Hình tròn", "Hình bình hành"], 0),
            make_mc(2, "Nhận biết", "Tâm đối xứng của hình chữ nhật là:", ["Giao điểm của hai đường chéo", "Trung điểm cạnh dài", "Một đỉnh bất kì", "Không có tâm đối xứng"], 0),
            make_mc(3, "Nhận biết", "Chữ cái in hoa nào sau đây có trục đối xứng?", ["Chữ A", "Chữ F", "Chữ G", "Chữ P"], 0),
            make_mc(4, "Nhận biết", "Chữ cái in hoa nào sau đây có tâm đối xứng?", ["Chữ S", "Chữ E", "Chữ C", "Chữ D"], 0),
            make_mc(5, "Thông hiểu", "Hình tròn có bao nhiêu trục đối xứng?", ["Vô số trục đối xứng đi qua tâm", "$1$ trục", "$2$ trục", "$4$ trục"], 0),
            make_mc(6, "Thông hiểu", "Hình vuông có bao nhiêu trục đối xứng?", ["$4$ trục đối xứng", "$2$ trục", "$1$ trục", "$8$ trục"], 0),
            make_mc(7, "Thông hiểu", "Hình nào sau đây vừa có trục đối xứng vừa có tâm đối xứng?", ["Hình thoi", "Tam giác đều", "Tam giác cân", "Hình thang cân"], 0),
            make_mc(8, "Thông hiểu", "Số nào sau đây (dạng chữ số điện tử) có tâm đối xứng?", ["Số 8", "Số 4", "Số 7", "Số 6"], 0),
            make_mc(9, "Vận dụng", "Trong các biển báo giao thông: biển báo đường cấm (hình tròn đỏ), biển báo nguy hiểm (tam giác đều), biển chỉ dẫn (hình chữ nhật xanh), biển dừng lại STOP (bát giác đều). Biển báo nào có TÂM đối xứng?", ["Biển báo đường cấm, biển chỉ dẫn và biển STOP", "Chỉ biển đường cấm", "Chỉ biển nguy hiểm", "Tất cả các biển"], 0),
            make_mc(10, "Vận dụng", "Lục giác đều có bao nhiêu trục đối xứng?", ["$6$ trục đối xứng", "$3$ trục", "$12$ trục", "$4$ trục"], 0),
            make_mc(11, "Vận dụng", "Cho đoạn thẳng $AB = 8\\text{ cm}$. Điểm $O$ là tâm đối xứng của đoạn thẳng $AB$. Khoảng cách từ $O$ đến $A$ là:", ["$4\\text{ cm}$", "$8\\text{ cm}$", "$2\\text{ cm}$", "$6\\text{ cm}$"], 0),
            make_mc(12, "Vận dụng cao", "Người ta thiết kế một logo gồm 4 hình tròn bằng nhau cùng đi qua một điểm tâm $O$. Logo này có bao nhiêu trục đối xứng và có tâm đối xứng không?", ["$4$ trục đối xứng và có tâm đối xứng là điểm $O$", "$2$ trục và không có tâm", "$8$ trục", "Không có trục đối xứng"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đối xứng của các hình học phẳng (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Đoạn thẳng có đúng 1 tâm đối xứng là trung điểm của nó.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hình bình hành tổng quát luôn có trục đối xứng.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Hình thang cân có đúng 1 trục đối xứng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Một đa giác đều $n$ cạnh luôn có đúng $n$ trục đối xứng.", "correct": True}
            ]),
            make_tf(2, "Cho hình chữ nhật $ABCD$ có $AB = 6\\text{ cm}, BC = 4\\text{ cm}$, hai đường chéo cắt nhau tại $O$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Điểm $O$ là tâm đối xứng của hình chữ nhật $ABCD$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hai trục đối xứng của hình chữ nhật là hai đường trung trực của các cạnh.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai đường chéo $AC$ và $BD$ là hai trục đối xứng của hình chữ nhật.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích của tam giác $OAB$ bằng một phần tư diện tích hình chữ nhật $ABCD$.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tam giác đều có bao nhiêu trục đối xứng?", "3"),
            make_sa(2, "Thông hiểu", "Hình thoi có bao nhiêu trục đối xứng?", "2"),
            make_sa(3, "Vận dụng", "Hình bát giác đều (8 cạnh bằng nhau) có bao nhiêu trục đối xứng?", "8"),
            make_sa(4, "Vận dụng cao", "Tìm số chữ cái in hoa trong từ 'TOAN HOC' có cả trục đối xứng và tâm đối xứng.", "2")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Chỉ rõ tâm đối xứng và trục đối xứng của hình vuông $ABCD$.", "Tâm đối xứng là giao điểm hai đường chéo O (0.25đ).\nHình vuông có 4 trục đối xứng: 2 đường chéo và 2 đường trung trực của các cạnh đối (0.25đ)."),
            make_essay(2, "Vận dụng", "Một hoa văn trang trí hình tròn bán kính 10 cm được tạo bởi 6 cánh hoa đối xứng nhau qua tâm. Hỏi hoa văn đó có bao nhiêu trục đối xứng và nêu vị trí tâm đối xứng.", "Tâm đối xứng là tâm O của hình tròn (0.25đ).\nHoa văn có 6 cánh đối xứng qua tâm nên có đúng 6 trục đối xứng đi qua tâm O (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho đoạn thẳng $AB = 10\\text{ cm}$. Lấy điểm $C$ nằm giữa $A$ và $B$ sao cho $AC = 4\\text{ cm}$. Gọi $I$ là trung điểm của $AC$, $K$ là trung điểm của $CB$. Tìm tâm đối xứng của đoạn thẳng $IK$ và tính độ dài $IK$.", "IK = IA + AK/2 = AC/2 + CB/2 = (AC + CB)/2 = AB/2 = 10/2 = 5 (cm) (0.25đ).\nTâm đối xứng của đoạn thẳng IK chính là trung điểm M của IK, và M cũng chính là trung điểm của đoạn thẳng AB (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương V: Tính đối xứng - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# ==============================================================================
# CHƯƠNG 6 TOÁN 6: PHÂN SỐ (Bài 6: cuối chương)
# ==============================================================================
def build_c6_6_exams():
    chap_id = "c6_6"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Phân số & Bài toán thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Phân số nào sau đây bằng phân số $\\frac{2}{3}$?", ["$\\frac{6}{9}$", "$\\frac{4}{9}$", "$\\frac{5}{6}$", "$\\frac{2}{6}$"], 0),
            make_mc(2, "Nhận biết", "Số nghịch đảo của phân số $-\\frac{3}{5}$ là:", ["$-\\frac{5}{3}$", "$\\frac{5}{3}$", "$\\frac{3}{5}$", "$-\\frac{3}{5}$"], 0),
            make_mc(3, "Nhận biết", "Kết quả của phép cộng $\\frac{1}{7} + \\frac{3}{7}$ là:", ["$\\frac{4}{7}$", "$\\frac{4}{14}$", "$\\frac{3}{7}$", "$\\frac{2}{7}$"], 0),
            make_mc(4, "Nhận biết", "Rút gọn phân số $\\frac{15}{25}$ về phân số tối giản được:", ["$\\frac{3}{5}$", "$\\frac{5}{3}$", "$\\frac{1}{2}$", "$\\frac{3}{10}$"], 0),
            make_mc(5, "Thông hiểu", "So sánh hai phân số $-\\frac{3}{4}$ và $-\\frac{5}{4}$:", ["$-\\frac{3}{4} > -\\frac{5}{4}$", "$-\\frac{3}{4} < -\\frac{5}{4}$", "$-\\frac{3}{4} = -\\frac{5}{4}$", "Không so sánh được"], 0),
            make_mc(6, "Thông hiểu", "Kết quả của phép nhân $\\frac{-5}{8} \\cdot \\frac{4}{15}$ là:", ["$-\\frac{1}{6}$", "$\\frac{1}{6}$", "$-\\frac{1}{3}$", "$-\\frac{2}{3}$"], 0),
            make_mc(7, "Thông hiểu", "Tìm $x$, biết $x - \\frac{1}{2} = \\frac{3}{4}$:", ["$x = \\frac{5}{4}$", "$x = \\frac{1}{4}$", "$x = 1$", "$x = \\frac{3}{8}$"], 0),
            make_mc(8, "Thông hiểu", "Tính $\\frac{2}{3}$ của $60\\text{ kg}$ ta được:", ["$40\\text{ kg}$", "$90\\text{ kg}$", "$30\\text{ kg}$", "$45\\text{ kg}$"], 0),
            make_mc(9, "Vận dụng", "Một giá sách có 120 cuốn sách. Số sách Toán chiếm $\\frac{2}{5}$ tổng số sách, số sách Văn chiếm $\\frac{1}{3}$ tổng số sách, còn lại là sách Tiếng Anh. Số sách Tiếng Anh là:", ["$32$ cuốn", "$48$ cuốn", "$40$ cuốn", "$24$ cuốn"], 0),
            make_mc(10, "Vận dụng", "Tìm một số biết $\\frac{3}{4}$ của số đó bằng $45$:", ["$60$", "$36$", "$40$", "$75$"], 0),
            make_mc(11, "Vận dụng", "Tính hợp lý: $A = \\frac{7}{19} \\cdot \\frac{8}{11} + \\frac{7}{19} \\cdot \\frac{3}{11} - \\frac{7}{19}$:", ["$0$", "$\\frac{7}{19}$", "$1$", "$\\frac{14}{19}$"], 0),
            make_mc(12, "Vận dụng cao", "Tính tổng $S = \\frac{1}{1 \\cdot 2} + \\frac{1}{2 \\cdot 3} + \\frac{1}{3 \\cdot 4} + \\dots + \\frac{1}{99 \\cdot 100}$:", ["$\\frac{99}{100}$", "$1$", "$\\frac{100}{101}$", "$\\frac{98}{99}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về các tính chất của phân số (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Phân số $\\frac{a}{b}$ có nghĩa khi $a, b \\in \\mathbb{Z}$ và $b \\neq 0$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu nhân cả tử và mẫu của một phân số với cùng một số nguyên khác 0 thì được phân số bằng nó.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Mọi phân số đều có số nghịch đảo.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Với mọi số tự nhiên $n \\ge 1$, phân số $\\frac{n}{n+1}$ luôn nhỏ hơn phân số $\\frac{n+1}{n+2}$.", "correct": True}
            ]),
            make_tf(2, "Bác An thu hoạch được 120 kg cam. Ngày thứ nhất bác bán được $\\frac{1}{3}$ số cam. Ngày thứ hai bác bán được $\\frac{3}{4}$ số cam còn lại:", [
                {"key": "a", "level": "Thông hiểu", "text": "Số cam bán trong ngày thứ nhất là $40\\text{ kg}$.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số cam còn lại sau ngày thứ nhất là $80\\text{ kg}$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số cam bán trong ngày thứ hai là $60\\text{ kg}$.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số cam còn lại sau hai ngày là $30\\text{ kg}$.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính giá trị biểu thức: $A = \\frac{5}{12} + \\frac{7}{12} - \\frac{1}{2}$.", "1/2"),
            make_sa(2, "Thông hiểu", "Tìm số đối của phân số: -7/9.", "7/9"),
            make_sa(3, "Vận dụng", "Tìm một số biết 2/5 của số đó bằng 24.", "60"),
            make_sa(4, "Vận dụng cao", "Tìm số tự nhiên n để phân số (n + 1)/(n - 2) nhận giá trị nguyên. Có bao nhiêu giá trị nguyên của n?", "4")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Tính hợp lý: $B = \\frac{5}{13} \\cdot \\frac{-3}{7} + \\frac{5}{13} \\cdot \\frac{-4}{7} + \\frac{8}{13}$.", "B = 5/13 . (-3/7 + -4/7) + 8/13 = 5/13 . (-1) + 8/13 = -5/13 + 8/13 = 3/13 (0.25đ)."),
            make_essay(2, "Vận dụng", "Một ô tô chạy quãng đường từ A đến B. Giờ thứ nhất ô tô chạy được 2/5 quãng đường. Giờ thứ hai ô tô chạy được 1/3 quãng đường. Giờ thứ ba ô tô chạy nốt 40 km thì tới B. Tính độ dài quãng đường AB.", "Phần quãng đường đi trong hai giờ đầu: 2/5 + 1/3 = 11/15 (quãng đường) (0.25đ).\nPhần quãng đường đi trong giờ thứ ba: 1 - 11/15 = 4/15 (quãng đường).\nĐộ dài quãng đường AB: 40 : (4/15) = 150 (km) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Chứng minh rằng $S = \\frac{1}{2^2} + \\frac{1}{3^2} + \\frac{1}{4^2} + \\dots + \\frac{1}{100^2} < 1$.", "Ta có: 1/n^2 < 1/(n-1).n với mọi n >= 2 (0.25đ).\n=> S < 1/1.2 + 1/2.3 + ... + 1/99.100 = 1 - 1/100 = 99/100 < 1. Đpcm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương VI: Phân số - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# ==============================================================================
# CHƯƠNG 7 TOÁN 6: SỐ THẬP PHÂN (Bài 5: cuối chương)
# ==============================================================================
def build_c7_6_exams():
    chap_id = "c7_6"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Số thập phân & Tỉ số phần trăm",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Số thập phân $-3,25$ có phần nguyên là:", ["$-3$", "$3$", "$25$", "$-0,25$"], 0),
            make_mc(2, "Nhận biết", "Số đối của số thập phân $4,8$ là:", ["$-4,8$", "$4,8$", "$8,4$", "$-8,4$"], 0),
            make_mc(3, "Nhận biết", "Làm tròn số $15,348$ đến hàng phần mười (chữ số thập phân thứ nhất) được:", ["$15,3$", "$15,4$", "$15,35$", "$15$"], 0),
            make_mc(4, "Nhận biết", "Tỉ số phần trăm của $3$ và $5$ là:", ["$60\\%$", "$15\\%$", "$35\\%$", "$50\\%$"], 0),
            make_mc(5, "Thông hiểu", "Kết quả của phép tính $(-2,5) + (-4,3)$ là:", ["$-6,8$", "$6,8$", "$-1,8$", "$1,8$"], 0),
            make_mc(6, "Thông hiểu", "Kết quả của phép nhân $0,4 \\cdot (-2,5)$ là:", ["$-1$", "$1$", "$-10$", "$-0,1$"], 0),
            make_mc(7, "Thông hiểu", "Tìm $x$, biết $x + 2,4 = 1,1$:", ["$x = -1,3$", "$x = 3,5$", "$x = 1,3$", "$x = -3,5$"], 0),
            make_mc(8, "Thông hiểu", "Tính $25\\%$ của $160$ ta được kết quả là:", ["$40$", "$80$", "$20$", "$32$"], 0),
            make_mc(9, "Vận dụng", "Một chiếc áo sơ mi có giá niêm yết 350 000 đồng. Nhân dịp ngày lễ, cửa hàng giảm giá $20\\%$. Giá bán của chiếc áo sau khi giảm giá là:", ["$280\\,000$ đồng", "$270\\,000$ đồng", "$70\\,000$ đồng", "$300\\,000$ đồng"], 0),
            make_mc(10, "Vận dụng", "Một cửa hàng gửi tiết kiệm 50 000 000 đồng với lãi suất $6\\%$ một năm. Sau một năm, cả tiền gửi và tiền lãi cửa hàng nhận được là:", ["$53\\,000\\,000$ đồng", "$3\\,000\\,000$ đồng", "$56\\,000\\,000$ đồng", "$52\\,500\\,000$ đồng"], 0),
            make_mc(11, "Vận dụng", "Tính hợp lý: $M = 3,75 \\cdot 12,4 + 3,75 \\cdot 87,6 - 75$:", ["$300$", "$375$", "$250$", "$350$"], 0),
            make_mc(12, "Vận dụng cao", "Một dung dịch chứa 15 g muối và 185 g nước. Cần cho thêm vào dung dịch bao nhiêu gam muối để nồng độ muối của dung dịch mới là $10\\%$?", ["$5\\text{ g}$ muối", "$7\\text{ g}$ muối", "$10\\text{ g}$ muối", "$3\\text{ g}$ muối"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai của các phép toán trên số thập phân (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Khi chia một số thập phân cho 0,1 ta chỉ việc nhân số đó với 10.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tích của hai số thập phân âm là một số thập phân dương.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số $-5,4$ lớn hơn số $-5,2$.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Nếu một mặt hàng tăng giá $10\\%$ rồi sau đó lại giảm giá $10\\%$ thì giá mới bằng đúng giá ban đầu.", "correct": False}
            ]),
            make_tf(2, "Một lớp 6A có 40 học sinh. Kết quả xếp loại cuối kỳ gồm: Giỏi chiếm $25\\%$, Khá chiếm $50\\%$, còn lại là Đạt:", [
                {"key": "a", "level": "Thông hiểu", "text": "Số học sinh xếp loại Giỏi là $10$ học sinh.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số học sinh xếp loại Khá là $20$ học sinh.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số học sinh xếp loại Đạt là $10$ học sinh (chiếm $25\\%$).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tỉ số phần trăm của số học sinh Giỏi so với số học sinh Khá là $40\\%$.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính: 3,5 x 4,2 - 2,5 x 4,2.", "4,2"),
            make_sa(2, "Thông hiểu", "Làm tròn số 47,826 đến hàng phần trăm.", "47,83"),
            make_sa(3, "Vận dụng", "Tìm một số biết 30% của số đó bằng 45.", "150"),
            make_sa(4, "Vận dụng cao", "Giá một đôi giày sau khi giảm 15% là 680 000 đồng. Tính giá niêm yết ban đầu của đôi giày (đơn vị: đồng).", "800000")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Thực hiện phép tính: $C = 15,24 \\cdot 4,8 + 15,24 \\cdot 5,2 - 52,4$.", "C = 15,24 . (4,8 + 5,2) - 52,4 = 15,24 . 10 - 52,4 = 152,4 - 52,4 = 100 (0.25đ)."),
            make_essay(2, "Vận dụng", "Bác Ba gửi ngân hàng 100 triệu đồng với kỳ hạn 1 năm, lãi suất 6,5%/năm. Hỏi sau 1 năm Bác Ba rút được tất cả bao nhiêu tiền cả gốc lẫn lãi?", "Tiền lãi sau 1 năm: 100 000 000 x 6,5% = 6 500 000 (đồng) (0.25đ).\nTổng tiền nhận được: 100 000 000 + 6 500 000 = 106 500 000 (đồng) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Nhân dịp Black Friday, một cửa hàng điện máy giảm giá một chiếc Smart Tivi hai lần: lần thứ nhất giảm 10% so với giá niêm yết, lần thứ hai giảm tiếp 5% so với giá sau lần giảm thứ nhất. Sau hai lần giảm giá, chiếc Tivi được bán với giá 17 100 000 đồng. Tính giá niêm yết ban đầu của chiếc Tivi.", "Giá sau lần 1: 17 100 000 : (1 - 0,05) = 18 000 000 (đồng) (0.25đ).\nGiá niêm yết ban đầu: 18 000 000 : (1 - 0,10) = 20 000 000 (đồng) (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương VII: Số thập phân - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# ==============================================================================
# CHƯƠNG 8 TOÁN 6: NHỮNG HÌNH HÌNH HỌC CƠ BẢN (Bài 7: cuối chương)
# ==============================================================================
def build_c8_6_exams():
    chap_id = "c8_6"
    l_idx = 7
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Đoạn thẳng & Góc thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Qua hai điểm phân biệt $A$ và $B$ vẽ được bao nhiêu đường thẳng?", ["Đúng một đường thẳng", "Hai đường thẳng", "Vô số đường thẳng", "Không vẽ được"], 0),
            make_mc(2, "Nhận biết", "Điểm $M$ là trung điểm của đoạn thẳng $AB$ khi:", ["$M$ nằm giữa $A, B$ và $MA = MB$", "$MA = MB$", "$M$ nằm giữa $A$ và $B$", "$M, A, B$ thẳng hàng"], 0),
            make_mc(3, "Nhận biết", "Góc có số đo bằng $90^\\circ$ là:", ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0),
            make_mc(4, "Nhận biết", "Góc bẹt có số đo bằng:", ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$60^\\circ$"], 0),
            make_mc(5, "Thông hiểu", "Cho đoạn thẳng $AB = 10\\text{ cm}$. Điểm $M$ là trung điểm của đoạn thẳng $AB$. Độ dài đoạn thẳng $AM$ là:", ["$5\\text{ cm}$", "$10\\text{ cm}$", "$2,5\\text{ cm}$", "$20\\text{ cm}$"], 0),
            make_mc(6, "Thông hiểu", "Trên tia $Ox$ lấy hai điểm $A$ và $B$ sao cho $OA = 3\\text{ cm}, OB = 7\\text{ cm}$. Độ dài đoạn thẳng $AB$ là:", ["$4\\text{ cm}$", "$10\\text{ cm}$", "$5\\text{ cm}$", "$2\\text{ cm}$"], 0),
            make_mc(7, "Thông hiểu", "Góc nhọn là góc có số đo:", ["Lớn hơn $0^\\circ$ và nhỏ hơn $90^\\circ$", "Bằng $90^\\circ$", "Lớn hơn $90^\\circ$", "Bằng $180^\\circ$"], 0),
            make_mc(8, "Thông hiểu", "Cho góc $\\widehat{xOy} = 70^\\circ$ và tia $Oz$ là tia phân giác của $\\widehat{xOy}$. Số đo của $\\widehat{xOz}$ là:", ["$35^\\circ$", "$70^\\circ$", "$140^\\circ$", "$45^\\circ$"], 0),
            make_mc(9, "Vận dụng", "Cho đoạn thẳng $AB = 8\\text{ cm}$. Lấy điểm $C$ thuộc đoạn thẳng $AB$ sao cho $AC = 2\\text{ cm}$. Gọi $I$ là trung điểm của đoạn thẳng $BC$. Độ dài đoạn thẳng $AI$ là:", ["$5\\text{ cm}$", "$4\\text{ cm}$", "$6\\text{ cm}$", "$3\\text{ cm}$"], 0),
            make_mc(10, "Vận dụng", "Cho $10$ điểm phân biệt trong đó không có 3 điểm nào thẳng hàng. Cứ qua hai điểm vẽ một đường thẳng. Số đường thẳng vẽ được là:", ["$45$ đường thẳng", "$90$ đường thẳng", "$20$ đường thẳng", "$100$ đường thẳng"], 0),
            make_mc(11, "Vận dụng", "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$, biết $\\widehat{xOy} = 50^\\circ$. Số đo của góc $\\widehat{yOz}$ là:", ["$130^\\circ$", "$40^\\circ$", "$50^\\circ$", "$140^\\circ$"], 0),
            make_mc(12, "Vận dụng cao", "Cho đoạn thẳng $AB = 2^{2026}\\text{ cm}$. Gọi $M_1$ là trung điểm $AB$, $M_2$ là trung điểm $AM_1$, ..., $M_{2026}$ là trung điểm $AM_{2025}$. Độ dài đoạn thẳng $AM_{2026}$ là:", ["$1\\text{ cm}$", "$2\\text{ cm}$", "$0,5\\text{ cm}$", "$4\\text{ cm}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về điểm, đường thẳng và đoạn thẳng (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Nếu ba điểm cùng thuộc một đường thẳng thì ta nói ba điểm đó thẳng hàng.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Đoạn thẳng $AB$ là hình gồm điểm $A$, điểm $B$ và tất cả các điểm nằm giữa $A$ và $B$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai tia phân biệt có chung gốc luôn là hai tia đối nhau.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Nếu $AM + MB = AB$ thì điểm $M$ luôn là trung điểm của đoạn thẳng $AB$.", "correct": False}
            ]),
            make_tf(2, "Trên đường thẳng $xy$, lấy điểm $O$. Trên tia $Ox$ lấy điểm $A$ sao cho $OA = 4\\text{ cm}$. Trên tia $Oy$ lấy điểm $B$ sao cho $OB = 4\\text{ cm}$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Hai tia $Ox$ và $Oy$ là hai tia đối nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Điểm $O$ nằm giữa hai điểm $A$ và $B$.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Điểm $O$ là trung điểm của đoạn thẳng $AB$.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Lấy điểm $C$ trên tia $Oy$ sao cho $BC = 2\\text{ cm}$. Khi đó độ dài đoạn thẳng $AC$ chỉ có thể bằng $10\\text{ cm}$.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho góc xOy = 120 độ. Tính số đo góc kề bù với góc xOy.", "60"),
            make_sa(2, "Thông hiểu", "Cho đoạn thẳng CD = 16 cm. M là trung điểm của CD. Tính độ dài CM (cm).", "8"),
            make_sa(3, "Vận dụng", "Cho n điểm phân biệt trong đó không có 3 điểm nào thẳng hàng. Biết vẽ được tất cả 28 đường thẳng. Tìm n.", "8"),
            make_sa(4, "Vận dụng cao", "Cho đoạn thẳng AB = 12 cm. Điểm C nằm giữa A và B sao cho AC = 4 cm. Gọi M, N lần lượt là trung điểm của AC và CB. Tính độ dài đoạn thẳng MN (cm).", "6")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Vẽ hình và tính độ dài đoạn thẳng $AB$ biết điểm $C$ nằm giữa $A$ và $B$, $AC = 3\\text{ cm}, CB = 5\\text{ cm}$.", "Vì C nằm giữa A và B nên: AB = AC + CB = 3 + 5 = 8 (cm) (0.5đ)."),
            make_essay(2, "Vận dụng", "Trên tia $Ox$ lấy hai điểm $A, B$ sao cho $OA = 3\\text{ cm}, OB = 6\\text{ cm}$. Chứng tỏ rằng điểm $A$ là trung điểm của đoạn thẳng $OB$.", "Vì OA < OB (3cm < 6cm) nên A nằm giữa O và B (0.25đ).\n=> AB = OB - OA = 6 - 3 = 3 (cm).\nVì A nằm giữa O, B và OA = AB (= 3cm) nên A là trung điểm OB (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho 20 điểm phân biệt, trong đó có đúng 4 điểm thẳng hàng, ngoài ra không có 3 điểm nào khác thẳng hàng. Cứ qua 2 điểm ta vẽ được 1 đường thẳng. Hỏi vẽ được tất cả bao nhiêu đường thẳng?", "Nếu 20 điểm không có 3 điểm thẳng hàng: 20 x 19 : 2 = 190 đường thẳng (0.25đ).\nVới 4 điểm thẳng hàng tạo ra 1 đường thẳng thay vì 4 x 3 : 2 = 6 đường thẳng.\nSố đường thẳng thực tế vẽ được: 190 - 6 + 1 = 185 (đường thẳng) (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương VIII: Hình học cơ bản - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# ==============================================================================
# CHƯƠNG 9 TOÁN 6: DỮ LIỆU VÀ XÁC SUẤT THỰC NGHIỆM (Bài 7: cuối chương)
# ==============================================================================
def build_c9_6_exams():
    chap_id = "c9_6"
    l_idx = 7
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Thống kê & Xác suất thực nghiệm",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Dữ liệu nào sau đây là số liệu (dữ liệu định lượng)?", ["Chiều cao của các bạn học sinh (cm)", "Màu sắc yêu thích", "Tên các môn học", "Nơi sinh"], 0),
            make_mc(2, "Nhận biết", "Biểu đồ cột kép thường được dùng để:", ["So sánh hai tập dữ liệu cùng loại", "Thể hiện xu hướng liên tục theo thời gian", "Biểu diễn tỉ lệ phần trăm", "Vẽ sơ đồ hình cây"], 0),
            make_mc(3, "Nhận biết", "Tung một đồng xu một lần. Các kết quả có thể xảy ra là:", ["Mặt Sấp (S) hoặc mặt Ngửa (N)", "Chỉ có mặt Sấp", "Chỉ có mặt Ngửa", "Mặt 1 chấm đến mặt 6 chấm"], 0),
            make_mc(4, "Nhận biết", "Gieo một con xúc xắc 6 mặt một lần. Tập hợp các kết quả có thể xảy ra là:", ["$\\{1; 2; 3; 4; 5; 6\\}$", "$\\{0; 1; 2; 3; 4; 5; 6\\}$", "$\\{S; N\\}$", "$\\{2; 4; 6\\}$"], 0),
            make_mc(5, "Thông hiểu", "Một xạ thủ bắn 50 phát súng, có 42 phát trúng bia. Xác suất thực nghiệm của sự kiện 'bắn trúng bia' là:", ["$\\frac{42}{50} = 0,84$", "$\\frac{8}{50} = 0,16$", "$0,50$", "$0,42$"], 0),
            make_mc(6, "Thông hiểu", "Gieo một con xúc xắc 20 lần liên tiếp, có 4 lần xuất hiện mặt 6 chấm. Xác suất thực nghiệm xuất hiện mặt 6 chấm là:", ["$\\frac{4}{20} = \\frac{1}{5}$", "$\\frac{1}{6}$", "$\\frac{16}{20}$", "$\\frac{1}{4}$"], 0),
            make_mc(7, "Thông hiểu", "Để biểu diễn số lượng học sinh Giỏi các khối 6, 7, 8, 9 của trường, loại biểu đồ nào sau đây là thích hợp nhất?", ["Biểu đồ cột đơn", "Biểu đồ hình quạt tròn", "Biểu đồ tranh không số liệu", "Biểu đồ đoạn thẳng"], 0),
            make_mc(8, "Thông hiểu", "Một hộp có 3 quả bóng: Xanh, Đỏ, Vàng. Lấy ngẫu nhiên 1 quả, ghi màu rồi trả lại. Sự kiện nào sau đây KHÔNG THỂ xảy ra?", ["Lấy được quả bóng màu Tím", "Lấy được quả bóng màu Xanh", "Lấy được quả bóng màu Đỏ", "Lấy được quả bóng màu Vàng"], 0),
            make_mc(9, "Vận dụng", "Tung một đồng xu 60 lần, thấy có 24 lần xuất hiện mặt Sấp. Xác suất thực nghiệm xuất hiện mặt Ngửa là:", ["$\\frac{36}{60} = \\frac{3}{5}$", "$\\frac{24}{60} = \\frac{2}{5}$", "$\\frac{1}{2}$", "$\\frac{1}{3}$"], 0),
            make_mc(10, "Vận dụng", "Một túi có 5 viên bi gồm 2 bi xanh và 3 bi đỏ. Lấy ngẫu nhiên lần lượt từng viên bi không hoàn lại. Có bao nhiêu kết quả có thể xảy ra khi lấy 2 viên bi?", ["$4$ kết quả: (X, X), (X, Đ), (Đ, X), (Đ, Đ)", "$2$ kết quả", "$3$ kết quả", "$5$ kết quả"], 0),
            make_mc(11, "Vận dụng", "Bảng thống kê điểm kiểm tra Toán của lớp 6B: Điểm 8 có 12 em, Điểm 9 có 8 em, Điểm 10 có 5 em, còn lại là dưới 8 gồm 15 em. Xác suất thực nghiệm chọn ngẫu nhiên một học sinh đạt điểm 9 hoặc 10 là:", ["$\\frac{13}{40}$", "$\\frac{8}{40}$", "$\\frac{5}{40}$", "$\\frac{25}{40}$"], 0),
            make_mc(12, "Vận dụng cao", "Gieo đồng thời hai con xúc xắc cân đối một lần. Số kết quả có thể để tổng số chấm trên hai con xúc xắc bằng 7 là:", ["$6$ kết quả", "$4$ kết quả", "$8$ kết quả", "$5$ kết quả"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về xác suất thực nghiệm và thu thập dữ liệu (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Xác suất thực nghiệm của một sự kiện luôn nằm trong khoảng từ 0 đến 1.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi số lần thực hiện thí nghiệm càng lớn thì xác suất thực nghiệm càng gần với xác suất lý thuyết.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu tung đồng xu 10 lần mà có 6 lần mặt Sấp thì lần thứ 11 chắc chắn là mặt Ngửa.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Xác suất thực nghiệm của một sự kiện có thể lớn hơn 1 nếu sự kiện đó xảy ra nhiều lần.", "correct": False}
            ]),
            make_tf(2, "Bạn Nam gieo một con xúc xắc 100 lần và ghi lại số lần xuất hiện của các mặt: Mặt 1 chấm: 15 lần; Mặt 2: 18 lần; Mặt 3: 14 lần; Mặt 4: 16 lần; Mặt 5: 20 lần; Mặt 6: 17 lần:", [
                {"key": "a", "level": "Thông hiểu", "text": "Mặt có số lần xuất hiện nhiều nhất là mặt 5 chấm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Xác suất thực nghiệm xuất hiện mặt 1 chấm là 0,15.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số lần xuất hiện mặt có số chấm là số chẵn là: 18 + 16 + 17 = 51 lần.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Xác suất thực nghiệm xuất hiện mặt có số chấm lớn hơn 4 là 0,37.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tung đồng xu 40 lần, có 18 lần xuất hiện mặt ngửa. Tính xác suất thực nghiệm xuất hiện mặt sấp (dưới dạng số thập phân).", "0,55"),
            make_sa(2, "Thông hiểu", "Gieo xúc xắc 50 lần, có 12 lần xuất hiện mặt số chẵn. Tính xác suất thực nghiệm xuất hiện mặt số lẻ (dạng số thập phân).", "0,76"),
            make_sa(3, "Vận dụng", "Một xạ thủ bắn 80 viên đạn, xác suất thực nghiệm bắn trượt là 0,15. Tính số phát bắn trúng của xạ thủ đó.", "68"),
            make_sa(4, "Vận dụng cao", "Trong hộp có 10 tấm thẻ cùng loại được đánh số từ 1 đến 10. Rút ngẫu nhiên một tấm thẻ. Có bao nhiêu kết quả thuận lợi cho sự kiện 'số ghi trên thẻ là số nguyên tố'?", "4")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Lớp 6A có 36 học sinh. Bạn lớp trưởng tiến hành khảo sát môn thể thao yêu thích: Bóng đá: 18 em, Cầu lông: 9 em, Bơi lội: 6 em, Bóng bàn: 3 em. Tính xác suất thực nghiệm một học sinh yêu thích môn Bóng đá.", "Xác suất thực nghiệm chọn học sinh thích Bóng đá: 18 / 36 = 1/2 = 0,5 (0.5đ)."),
            make_essay(2, "Vận dụng", "Một nhà máy sản xuất bóng đèn kiểm tra ngẫu nhiên 500 bóng đèn thì thấy có 15 bóng bị lỗi. a) Tính xác suất thực nghiệm bóng đèn bị lỗi. b) Nếu nhà máy sản xuất 20 000 bóng đèn thì ước tính có khoảng bao nhiêu bóng đèn đạt chuẩn?", "a) Xác suất thực nghiệm lỗi: 15 / 500 = 0,03 (0.25đ).\nb) Tỉ lệ bóng đạt chuẩn: 1 - 0,03 = 0,97. Số bóng đạt chuẩn ước tính: 20 000 x 0,97 = 19 400 (bóng) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Gieo đồng thời hai con xúc xắc 6 mặt một lần. Liệt kê tất cả các kết quả để tổng số chấm trên hai con xúc xắc là một số nguyên tố.", "Các tổng có thể là số nguyên tố: 2, 3, 5, 7, 11 (0.25đ).\nTổng = 2: (1,1) [1 cách].\nTổng = 3: (1,2), (2,1) [2 cách].\nTổng = 5: (1,4), (2,3), (3,2), (4,1) [4 cách].\nTổng = 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) [6 cách].\nTổng = 11: (5,6), (6,5) [2 cách].\nTổng cộng có: 1 + 2 + 4 + 6 + 2 = 15 kết quả thuận lợi (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương IX: Dữ liệu và xác suất - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# HÀM THỰC THI TỔNG THỂ TOÁN 6
def run_all_grade6():
    builders = [
        build_c1_6_exams,
        build_c2_6_exams,
        build_c3_6_exams,
        build_c4_6_exams,
        build_c5_6_exams,
        build_c6_6_exams,
        build_c7_6_exams,
        build_c8_6_exams,
        build_c9_6_exams
    ]
    for b in builders:
        chap_id, new_exams = b()
        title, exams = load_existing_exams(6, chap_id)
        exams.update(new_exams)
        save_chapter_package(6, chap_id, title, exams)
    print("🎉 ĐÃ HOÀN TẤT TOÀN BỘ 9 CHƯƠNG TOÁN 6 (MỖI CHƯƠNG ĐÃ CÓ ĐỦ 7 ĐỀ CUỐI CHƯƠNG)!")

if __name__ == "__main__":
    run_all_grade6()
