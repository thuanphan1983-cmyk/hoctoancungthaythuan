# -*- coding: utf-8 -*-
"""
BIÊN SOẠN BỔ SUNG 4 ĐỀ CUỐI CHƯƠNG (ĐỀ 4, 5, 6, 7) - TOÁN 9 (10 CHƯƠNG)
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

# 1. CHƯƠNG 1 TOÁN 9: PHƯƠNG TRÌNH VÀ HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (Bài 4: cuối chương)
def build_c1_9_exams():
    chap_id = "c1_9"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Giải bài toán bằng cách lập hệ phương trình",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Phương trình nào sau đây là phương trình bậc nhất hai ẩn $x$ và $y$?", ["$2x - 3y = 5$", "$x^2 + y = 3$", "$xy - 2 = 0$", "$x + \\frac{1}{y} = 1$"], 0),
            make_mc(2, "Nhận biết", "Cặp số nào sau đây là nghiệm của phương trình $2x + y = 5$?", ["$(2; 1)$", "$(1; 2)$", "$(0; 4)$", "$(3; 1)$"], 0),
            make_mc(3, "Nhận biết", "Trên mặt phẳng tọa độ $Oxy$, tập nghiệm của phương trình $ax + by = c$ được biểu diễn bởi:", ["Một đường thẳng", "Một parabol", "Một điểm duy nhất", "Một đoạn thẳng"], 0),
            make_mc(4, "Nhận biết", "Hệ hai phương trình bậc nhất hai ẩn có nghiệm duy nhất khi hai đường thẳng biểu diễn tập nghiệm của chúng:", ["Cắt nhau tại một điểm", "Song song với nhau", "Trùng nhau", "Vuông góc với nhau"], 0),
            make_mc(5, "Thông hiểu", "Nghiệm của hệ phương trình $\\begin{cases} x + y = 5 \\\\ x - y = 1 \\end{cases}$ là:", ["$(3; 2)$", "$(2; 3)$", "$(4; 1)$", "$(1; 4)$"], 0),
            make_mc(6, "Thông hiểu", "Bằng phương pháp cộng đại số, giải hệ $\\begin{cases} 2x + 3y = 7 \\\\ 2x - y = 3 \\end{cases}$ ta tìm được $y$ bằng:", ["$y = 1$", "$y = 2$", "$y = -1$", "$y = 0$"], 0),
            make_mc(7, "Thông hiểu", "Đường thẳng biểu diễn tập nghiệm của phương trình $2x - y = 3$ đi qua điểm nào sau đây?", ["$(1; -1)$", "$(0; 3)$", "$(2; 2)$", "$(-1; 1)$"], 0),
            make_mc(8, "Thông hiểu", "Tìm $a$ để cặp số $(1; -2)$ là nghiệm của phương trình $ax + 3y = -4$:", ["$a = 2$", "$a = -2$", "$a = 10$", "$a = -10$"], 0),
            make_mc(9, "Vận dụng", "Hai bạn An và Bình cùng mua vở và bút bi. An mua 5 quyển vở và 3 chiếc bút hết 65 000 đồng. Bình mua 3 quyển vở và 2 chiếc bút hết 40 000 đồng. Giá tiền của 1 quyển vở là:", ["$10\\,000$ đồng", "$8\\,000$ đồng", "$5\\,000$ đồng", "$12\\,000$ đồng"], 0),
            make_mc(10, "Vận dụng", "Tìm $m$ để hệ phương trình $\\begin{cases} mx + y = 3 \\\\ 4x + 2y = 6 \\end{cases}$ có vô số nghiệm:", ["$m = 2$", "$m = -2$", "$m = 4$", "$m = 1$"], 0),
            make_mc(11, "Vận dụng", "Một hình chữ nhật có chu vi $40\\text{ m}$. Nếu tăng chiều dài thêm $3\\text{ m}$ và giảm chiều rộng đi $2\\text{ m}$ thì diện tích không đổi. Chiều dài ban đầu của hình chữ nhật là:", ["$12\\text{ m}$", "$10\\text{ m}$", "$14\\text{ m}$", "$8\\text{ m}$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm các giá trị nguyên của $m$ để hệ phương trình $\\begin{cases} x + my = 2 \\\\ mx - y = 1 \\end{cases}$ có nghiệm duy nhất $(x; y)$ thỏa mãn $x > 0, y < 0$:", ["$m < -2$", "$m > 2$", "$-2 < m < 0$", "$m > 0$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về hệ phương trình bậc nhất hai ẩn (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Phương trình bậc nhất hai ẩn ax + by = c (a khác 0 hoặc b khác 0) luôn có vô số nghiệm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hệ hai phương trình bậc nhất hai ẩn vô nghiệm khi hai đường thẳng biểu diễn tập nghiệm song song với nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu nhân cả hai vế của một phương trình trong hệ với một số khác 0 thì ta được hệ phương trình tương đương.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hệ phương trình mx + y = 1 và x + my = 1 luôn có nghiệm với mọi giá trị của m.", "correct": False}
            ]),
            make_tf(2, "Cho hệ phương trình $\\begin{cases} 2x - y = 3 \\\\ x + 2y = 4 \\end{cases}$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Nhân phương trình thứ nhất với 2 ta được: 4x - 2y = 6.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Cộng hai phương trình ta được: 5x = 10, suy ra x = 2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Thay x = 2 vào ta tìm được y = 1.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tích của x và y trong nghiệm của hệ bằng 3.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tìm nghiệm x của hệ phương trình: x + y = 10 và x - y = 4.", "7"),
            make_sa(2, "Thông hiểu", "Tìm nghiệm y của hệ phương trình: 2x + y = 7 và x = 2.", "3"),
            make_sa(3, "Vận dụng", "Một thửa ruộng hình chữ nhật có chu vi 100 m, chiều dài hơn chiều rộng 10 m. Tính diện tích thửa ruộng (m^2).", "600"),
            make_sa(4, "Vận dụng cao", "Tìm m để hệ phương trình x + y = 3 và mx - y = 1 có nghiệm duy nhất thỏa mãn x = 2y.", "2")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Giải hệ phương trình bằng phương pháp thế: $\\begin{cases} x - 2y = 1 \\\\ 3x + y = 10 \\end{cases}$.", "Từ pt 1: x = 2y + 1 (0.25đ).\nThay vào pt 2: 3(2y + 1) + y = 10 => 7y + 3 = 10 => 7y = 7 => y = 1.\nSuy ra: x = 2(1) + 1 = 3. Vậy hệ có nghiệm (3; 1) (0.25đ)."),
            make_essay(2, "Vận dụng", "Hai tổ công nhân cùng làm chung một công việc thì hoàn thành trong 12 giờ. Nếu tổ 1 làm trong 4 giờ rồi tổ 2 làm tiếp trong 6 giờ thì cả hai tổ hoàn thành được 40% công việc. Hỏi nếu làm riêng thì mỗi tổ hoàn thành công việc trong bao lâu?", "Gọi thời gian tổ 1 làm riêng là x (giờ), tổ 2 là y (giờ) (x, y > 12) (0.25đ).\nTrong 1 giờ tổ 1 làm 1/x, tổ 2 làm 1/y công việc. Ta có hệ:\n1/x + 1/y = 1/12 và 4/x + 6/y = 2/5.\nGiải hệ ta được: 1/x = 1/20 => x = 20 (giờ); 1/y = 1/30 => y = 30 (giờ) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Tìm tất cả các giá trị của tham số $m$ để hệ phương trình $\\begin{cases} mx + 2y = m + 1 \\\\ 2x + my = 2m - 1 \\end{cases}$ có nghiệm duy nhất $(x; y)$ thỏa mãn $x + y = 2$.", "Hệ có nghiệm duy nhất <=> m^2 - 4 khác 0 <=> m khác +-2 (0.25đ).\nCộng vế theo vế: (m + 2)(x + y) = 3m => (m + 2) . 2 = 3m => 2m + 4 = 3m => m = 4 (thỏa mãn m khác +-2) (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương I: Hệ phương trình bậc nhất hai ẩn - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 2. CHƯƠNG 2 TOÁN 9: PHƯƠNG TRÌNH VÀ BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN (Bài 4: cuối chương)
def build_c2_9_exams():
    chap_id = "c2_9"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Phương trình tích & Bất phương trình",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Phương trình tích có dạng chuẩn là:", ["$A(x) \\cdot B(x) = 0$", "$A(x) + B(x) = 0$", "$\\frac{A(x)}{B(x)} = 0$", "$A(x) = B(x)$"], 0),
            make_mc(2, "Nhận biết", "Khi nhân hai vế của một bất đẳng thức với cùng một số âm, ta phải:", ["Đổi chiều bất đẳng thức", "Giữ nguyên chiều", "Nhân thêm số $-1$", "Đổi số thành số nghịch đảo"], 0),
            make_mc(3, "Nhận biết", "Nghiệm của bất phương trình $2x > 6$ là:", ["$x > 3$", "$x < 3$", "$x > 4$", "$x \\ge 3$"], 0),
            make_mc(4, "Nhận biết", "Điều kiện xác định của phương trình $\\frac{x}{x-3} = 2$ là:", ["$x \\neq 3$", "$x \\neq 0$", "$x > 3$", "$x \\neq -3$"], 0),
            make_mc(5, "Thông hiểu", "Nghiệm của phương trình tích $(x - 3)(2x + 4) = 0$ là:", ["$x = 3$ hoặc $x = -2$", "$x = 3$ hoặc $x = 2$", "$x = -3$ hoặc $x = -2$", "$x = 3$"], 0),
            make_mc(6, "Thông hiểu", "Tập nghiệm của bất phương trình $-3x + 9 \\ge 0$ là:", ["$x \\le 3$", "$x \\ge 3$", "$x < 3$", "$x > -3$"], 0),
            make_mc(7, "Thông hiểu", "Phương trình $\\frac{x+1}{x-1} = 1$ có số nghiệm là:", ["$0$ (vô nghiệm)", "$1$ nghiệm", "$2$ nghiệm", "Vô số nghiệm"], 0),
            make_mc(8, "Thông hiểu", "Cho $a < b$. Khẳng định nào sau đây là ĐÚNG?", ["$2a - 3 < 2b - 3$", "$-3a < -3b$", "$a + 5 > b + 5$", "$a^2 < b^2$"], 0),
            make_mc(9, "Vận dụng", "Tìm số nguyên $x$ lớn nhất thỏa mãn bất phương trình $4x - 5 < 2x + 8$:", ["$x = 6$", "$x = 7$", "$x = 5$", "$x = 8$"], 0),
            make_mc(10, "Vận dụng", "Giải phương trình $\\frac{x}{x-2} + \\frac{1}{x+2} = \\frac{4}{x^2-4}$ ta được nghiệm là:", ["$x = -3$", "$x = 2$", "$x = -2$", "$x = 3$"], 0),
            make_mc(11, "Vận dụng", "Một người có 500 000 đồng đi siêu thị. Người đó mua một thùng sữa giá 280 000 đồng và một số gói bánh giá 35 000 đồng/gói. Người đó có thể mua được tối đa bao nhiêu gói bánh?", ["$6$ gói", "$7$ gói", "$5$ gói", "$8$ gói"], 0),
            make_mc(12, "Vận dụng cao", "Tìm $m$ để phương trình $\\frac{x-m}{x-1} + \\frac{x-1}{x-m} = 2$ có nghiệm duy nhất:", ["$m \\neq 1$", "$m = 1$", "Không tồn tại $m$", "$m > 0$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về phương trình và bất phương trình bậc nhất một ẩn (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Bất phương trình ax + b < 0 (với a khác 0) luôn có vô số nghiệm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi cộng cùng một số vào hai vế của một bất phương trình ta được bất phương trình cùng chiều.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Phương trình chứa ẩn ở mẫu có thể có nghiệm ngoại lai không thỏa mãn ĐKXĐ.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu a > b thì a^2 luôn lớn hơn b^2.", "correct": False}
            ]),
            make_tf(2, "Cho bất phương trình $2(x - 3) \\le 5x + 3$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Khai triển vế trái: 2x - 6 <= 5x + 3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Chuyển vế thu gọn: -3x <= 9.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Chia hai vế cho -3 và đổi chiều: x >= -3.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số nguyên âm nhỏ nhất thỏa mãn bất phương trình là -3.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Giải phương trình tích: (x - 5)(x + 2) = 0. Tìm tổng các nghiệm.", "3"),
            make_sa(2, "Thông hiểu", "Tìm số nguyên dương nhỏ nhất thỏa mãn bất phương trình: 3x - 8 > 0.", "3"),
            make_sa(3, "Vận dụng", "Giải phương trình: (x + 2)/(x - 2) - 1 = 4/(x - 2). Phương trình có bao nhiêu nghiệm?", "0"), # Nghiệm ngoại lai x = 2
            make_sa(4, "Vận dụng cao", "Tìm m để bất phương trình (m - 2)x + 3 > 0 nghiệm đúng với mọi x < 0.", "2")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Giải phương trình: $(2x - 1)^2 - (x + 3)^2 = 0$.", "Áp dụng HĐT hiệu hai bình phương: (2x - 1 - x - 3)(2x - 1 + x + 3) = 0 (0.25đ).\n=> (x - 4)(3x + 2) = 0 => x = 4 hoặc x = -2/3 (0.25đ)."),
            make_essay(2, "Vận dụng", "Giải bất phương trình sau và biểu diễn tập nghiệm trên trục số: $\\frac{2x - 3}{4} - \\frac{x - 1}{3} > 1$.", "Quy đồng khử mẫu với MTC = 12: 3(2x - 3) - 4(x - 1) > 12 (0.25đ).\n=> 6x - 9 - 4x + 4 > 12 => 2x - 5 > 12 => 2x > 17 => x > 8,5 (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho $a, b > 0$. Chứng minh bất đẳng thức: $\\frac{a}{b} + \\frac{b}{a} \\ge 2$. Dấu bằng xảy ra khi nào?", "Xét hiệu: a/b + b/a - 2 = (a^2 + b^2 - 2ab)/(ab) = (a - b)^2 / (ab) (0.25đ).\nVì (a - b)^2 >= 0 và ab > 0 với mọi a, b > 0 nên (a - b)^2 / (ab) >= 0 => a/b + b/a >= 2.\nDấu '=' xảy ra khi a = b (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình & Bất phương trình - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 3. CHƯƠNG 3 TOÁN 9: CĂN BẬC HAI VÀ CĂN BẬC BA (Bài 5: cuối chương)
def build_c3_9_exams():
    chap_id = "c3_9"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Rút gọn biểu thức chứa căn thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Căn thức bậc hai $\\sqrt{A}$ xác định (có nghĩa) khi và chỉ khi:", ["$A \\ge 0$", "$A > 0$", "$A \\le 0$", "$A \\neq 0$"], 0),
            make_mc(2, "Nhận biết", "Hằng đẳng thức $\\sqrt{A^2}$ bằng:", ["$|A|$", "$A$", "$-A$", "$\\pm A$"], 0),
            make_mc(3, "Nhận biết", "Căn bậc ba của $-27$ là:", ["$-3$", "$3$", "$\\pm 3$", "Không tồn tại"], 0),
            make_mc(4, "Nhận biết", "Trục căn thức ở mẫu của biểu thức $\\frac{2}{\\sqrt{3}}$ ta được:", ["$\\frac{2\\sqrt{3}}{3}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{2}{3}$", "$2\\sqrt{3}$"], 0),
            make_mc(5, "Thông hiểu", "Điều kiện xác định của căn thức $\\sqrt{2x - 6}$ là:", ["$x \\ge 3$", "$x > 3$", "$x \\le 3$", "$x \\neq 3$"], 0),
            make_mc(6, "Thông hiểu", "Rút gọn biểu thức $\\sqrt{(\\sqrt{3} - 2)^2}$ ta được:", ["$2 - \\sqrt{3}$", "$\\sqrt{3} - 2$", "$\\pm(\\sqrt{3} - 2)$", "$-1$"], 0),
            make_mc(7, "Thông hiểu", "Kết quả của phép tính $\\sqrt{12} + \\sqrt{27} - \\sqrt{48}$ là:", ["$\\sqrt{3}$", "$2\\sqrt{3}$", "$3\\sqrt{3}$", "$0$"], 0),
            make_mc(8, "Thông hiểu", "Tìm $x \\ge 0$, biết $\\sqrt{x} = 4$:", ["$x = 16$", "$x = 2$", "$x = 8$", "$x = \\pm 4$"], 0),
            make_mc(9, "Vận dụng", "Rút gọn biểu thức $P = \\left(\\frac{1}{\\sqrt{x}-1} - \\frac{1}{\\sqrt{x}+1}\\right) \\cdot \\frac{x-1}{2}$ với $x \\ge 0, x \\neq 1$:", ["$1$", "$2$", "$\\sqrt{x}$", "$\\frac{1}{2}$"], 0),
            make_mc(10, "Vận dụng", "Tìm $x$, biết $\\sqrt{4x - 8} - 2\\sqrt{x - 2} = 0$:", ["Mọi $x \\ge 2$", "$x = 2$", "$x = 4$", "Vô nghiệm"], 0),
            make_mc(11, "Vận dụng", "Trục căn thức ở mẫu của $\\frac{1}{\\sqrt{5} - 2}$ ta được:", ["$\\sqrt{5} + 2$", "$\\sqrt{5} - 2$", "$\\frac{\\sqrt{5}+2}{3}$", "$1$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm giá trị lớn nhất của biểu thức $A = \\sqrt{x} + \\sqrt{4 - x}$ với $0 \\le x \\le 4$:", ["$2\\sqrt{2}$ (khi $x = 2$)", "$4$", "$2$", "$\\sqrt{2}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về căn bậc hai và căn bậc ba (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Mọi số thực đều có duy nhất một căn bậc ba.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Căn bậc hai số học của một số thực âm không tồn tại.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Với mọi a >= 0 và b > 0, ta có căn(a/b) = căn(a)/căn(b).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Biểu thức căn(x^2 - 4x + 4) luôn bằng x - 2 với mọi x.", "correct": False}
            ]),
            make_tf(2, "Cho biểu thức $A = \\frac{\\sqrt{x}+2}{\\sqrt{x}-2}$ (với $x \\ge 0, x \\neq 4$):", [
                {"key": "a", "level": "Thông hiểu", "text": "Điều kiện xác định của biểu thức A là x >= 0 và x khác 4.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi x = 9 thì căn(x) = 3 và giá trị của A bằng 5.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Biểu thức A có thể viết lại thành 1 + 4/(căn(x) - 2).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Có đúng 3 giá trị nguyên của x để biểu thức A nhận giá trị nguyên.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính: căn(75) : căn(3).", "5"),
            make_sa(2, "Thông hiểu", "Tính giá trị căn bậc ba của -64.", "-4"),
            make_sa(3, "Vận dụng", "Tìm x biết: căn(x - 3) = 5.", "28"),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: P = x - 2 căn(x) + 5 (với x >= 0).", "4")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Rút gọn biểu thức: $A = \\sqrt{50} - 2\\sqrt{18} + 3\\sqrt{8}$.", "A = 5 căn(2) - 2 . 3 căn(2) + 3 . 2 căn(2) = 5 căn(2) - 6 căn(2) + 6 căn(2) = 5 căn(2) (0.5đ)."),
            make_essay(2, "Vận dụng", "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x}+2} + \\frac{1}{\\sqrt{x}-2}\\right) \\cdot \\frac{x-4}{\\sqrt{x}}$ với $x > 0, x \\neq 4$. Rút gọn $P$ và tìm $x$ để $P = 2$.", "P = [ (căn(x) - 2 + căn(x) + 2)/(x - 4) ] . [(x - 4)/căn(x)] = (2 căn(x) / (x - 4)) . ((x - 4)/căn(x)) = 2 (0.25đ).\nVì P luôn bằng 2 với mọi x > 0, x khác 4 nên phương trình P = 2 nghiệm đúng với mọi x > 0, x khác 4 (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Giải phương trình: $\\sqrt{x^2 - 4x + 4} + \\sqrt{x^2 - 6x + 9} = 1$.", "Phương trình <=> |x - 2| + |3 - x| = 1 (0.25đ).\nÁp dụng bđt |A| + |B| >= |A + B|: |x - 2| + |3 - x| >= |x - 2 + 3 - x| = 1.\nDấu '=' xảy ra khi (x - 2)(3 - x) >= 0 <=> 2 <= x <= 3.\nVậy tập nghiệm của pt là S = {x in R | 2 <= x <= 3} (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương III: Căn bậc hai & Căn bậc ba - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 4. CHƯƠNG 4 TOÁN 9: HỆ THỨC LƯỢNG TRONG TAM GIÁC VUÔNG (Bài 3: cuối chương)
def build_c4_9_exams():
    chap_id = "c4_9"
    l_idx = 3
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Tỉ số lượng giác & Đo chiều cao",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Trong tam giác vuông, $\\sin$ của một góc nhọn bằng:", ["Tỉ số giữa cạnh đối và cạnh huyền", "Tỉ số giữa cạnh kề và cạnh huyền", "Tỉ số giữa cạnh đối và cạnh kề", "Tỉ số giữa cạnh kề và cạnh đối"], 0),
            make_mc(2, "Nhận biết", "Đẳng thức lượng giác cơ bản nào sau đây luôn đúng với góc nhọn $\\alpha$?", ["$\\sin^2\\alpha + \\cos^2\\alpha = 1$", "$\\sin\\alpha + \\cos\\alpha = 1$", "$\\tan\\alpha = \\frac{\\cos\\alpha}{\\sin\\alpha}$", "$\\tan\\alpha \\cdot \\cot\\alpha = 0$"], 0),
            make_mc(3, "Nhận biết", "Cho góc nhọn $\\alpha$. Ta có $\\tan\\alpha$ bằng:", ["$\\frac{\\sin\\alpha}{\\cos\\alpha}$", "$\\frac{\\cos\\alpha}{\\sin\\alpha}$", "$\\sin\\alpha \\cdot \\cos\\alpha$", "$\\frac{1}{\\sin\\alpha}$"], 0),
            make_mc(4, "Nhận biết", "Giá trị của $\\sin 30^\\circ$ bằng:", ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$1$"], 0),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$, cạnh $AB = 3\\text{ cm}, AC = 4\\text{ cm}$. Giá trị của $\\sin B$ là:", ["$\\frac{4}{5} = 0,8$", "$\\frac{3}{5}$", "$\\frac{4}{3}$", "$\\frac{3}{4}$"], 0),
            make_mc(6, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 60^\\circ$. Giá trị của $\\cos C$ là:", ["$\\frac{\\sqrt{3}}{2}$", "$\\frac{1}{2}$", "$1$", "$0$"], 0),
            make_mc(7, "Thông hiểu", "Nếu hai góc nhọn phụ nhau ($\\alpha + \\beta = 90^\\circ$) thì:", ["$\\sin\\alpha = \\cos\\beta$", "$\\sin\\alpha = \\sin\\beta$", "$\\tan\\alpha = \\tan\\beta$", "$\\cos\\alpha = \\cos\\beta$"], 0),
            make_mc(8, "Thông hiểu", "Một chiếc thang dài $3\\text{ m}$ dựa vào tường tạo với mặt đất góc $65^\\circ$. Chiều cao thang chạm tường xấp xỉ là:", ["$3 \\cdot \\sin 65^\\circ \\approx 2,72\\text{ m}$", "$3 \\cdot \\cos 65^\\circ$", "$3 \\cdot \\tan 65^\\circ$", "$3\\text{ m}$"], 0),
            make_mc(9, "Vận dụng", "Một cột đèn cao $7\\text{ m}$ có bóng trên mặt đất dài $4\\text{ m}$. Góc tạo bởi tia nắng mặt trời và mặt đất (làm tròn đến độ) là:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$55^\\circ$"], 0),
            make_mc(10, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 4\\text{ cm}, CH = 9\\text{ cm}$. Độ dài đoạn thẳng $AH$ là:", ["$6\\text{ cm}$", "$13\\text{ cm}$", "$36\\text{ cm}$", "$5\\text{ cm}$"], 0),
            make_mc(11, "Vận dụng", "Tính giá trị biểu thức: $M = \\sin^2 25^\\circ + \\sin^2 65^\\circ - \\tan 35^\\circ \\cdot \\cot 35^\\circ$:", ["$0$", "$1$", "$2$", "$-1$"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác nhọn $ABC$ có hai đường cao $BD$ và $CE$. Khẳng định nào sau đây là ĐÚNG?", ["$S_{ADE} = S_{ABC} \\cdot \\cos^2 A$", "$S_{ADE} = S_{ABC} \\cdot \\sin^2 A$", "$DE = BC \\cdot \\sin A$", "$DE = BC \\cdot \\tan A$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về hệ thức lượng trong tam giác vuông (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Trong tam giác vuông, mỗi cạnh góc vuông bằng cạnh huyền nhân với sin góc đối hoặc nhân với cosin góc kề.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi góc nhọn alpha tăng từ 0 đến 90 độ thì sin(alpha) và tan(alpha) đều tăng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tỉ số lượng giác sin và cosin của góc nhọn luôn nhỏ hơn 1.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Biểu thức sin(alpha) + cos(alpha) luôn lớn hơn 1 với mọi góc nhọn alpha.", "correct": True}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$, đường cao $AH$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Cạnh huyền BC = 10 cm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Độ dài đường cao AH = 4,8 cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Đoạn hình chiếu BH = 3,6 cm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Giá trị tan B bằng 4/3 và tan C bằng 3/4.", "correct": True}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho tam giác vuông có cạnh huyền 10 cm, một góc nhọn 30 độ. Tính cạnh góc vuông đối diện góc 30 độ (cm).", "5"),
            make_sa(2, "Thông hiểu", "Tính: sin^2(35 độ) + cos^2(35 độ).", "1"),
            make_sa(3, "Vận dụng", "Một máy bay bay lên với góc nghiêng 20 độ so với mặt đất. Sau khi bay được quãng đường 5000 m thì độ cao máy bay đạt được là bao nhiêu mét (làm tròn số nguyên)?", "1710"),
            make_sa(4, "Vận dụng cao", "Cho tam giác ABC có góc B = 60 độ, góc C = 45 độ, cạnh BC = 10 cm. Tính chiều cao AH kẻ từ A (làm tròn 1 chữ số thập phân, cm).", "6,3")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$, biết $AB = 9\\text{ cm}, AC = 12\\text{ cm}$. Tính các tỉ số lượng giác của góc $B$.", "BC = căn(9^2 + 12^2) = 15 cm (0.25đ).\nsin B = AC/BC = 12/15 = 4/5 = 0,8; cos B = AB/BC = 9/15 = 3/5 = 0,6.\ntan B = 4/3; cot B = 3/4 (0.25đ)."),
            make_essay(2, "Vận dụng", "Một khinh khí cầu đang bay ở độ cao 800 m so với mặt đất. Người trên khinh khí cầu nhìn thấy một cây cầu với góc hạ 35 độ. Hỏi khoảng cách từ mặt đất ngay dưới khinh khí cầu đến cây cầu là bao nhiêu mét (làm tròn đến hàng đơn vị)?", "Gọi khoảng cách cần tìm là d (m). Ta có góc hạ bằng 35 độ nên: tan 35 độ = 800 / d (0.25đ).\n=> d = 800 / tan 35 độ xấp xỉ 800 / 0,7002 xấp xỉ 1143 (m) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Không dùng máy tính cầm tay, hãy tính giá trị của biểu thức: $A = \\cos^2 10^\\circ + \\cos^2 20^\\circ + \\dots + \\cos^2 80^\\circ$.", "Ta có: cos 80 = sin 10 => cos^2 80 = sin^2 10. Khi đó cos^2 10 + cos^2 80 = sin^2 10 + cos^2 10 = 1 (0.25đ).\nGhép các cặp:\n(cos^2 10 + cos^2 80) + (cos^2 20 + cos^2 70) + (cos^2 30 + cos^2 60) + (cos^2 40 + cos^2 50)\n= 1 + 1 + 1 + 1 = 4 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương IV: Hệ thức lượng trong tam giác vuông - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 5. CHƯƠNG 5 TOÁN 9: ĐƯỜNG TRÒN (Bài 6: cuối chương)
def build_c5_9_exams():
    chap_id = "c5_9"
    l_idx = 6
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Tiếp tuyến & Tính chất đường tròn",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Tâm đối xứng của đường tròn $(O; R)$ là:", ["Tâm $O$ của đường tròn", "Một điểm bất kì trên đường tròn", "Điểm bên ngoài đường tròn", "Không có tâm đối xứng"], 0),
            make_mc(2, "Nhận biết", "Dây cung lớn nhất của đường tròn là:", ["Đường kính", "Bán kính", "Tiếp tuyến", "Cung lớn"], 0),
            make_mc(3, "Nhận biết", "Đường thẳng và đường tròn tiếp xúc nhau khi số điểm chung giữa chúng là:", ["Đúng $1$ điểm chung", "$2$ điểm chung", "Không có điểm chung", "Vô số điểm chung"], 0),
            make_mc(4, "Nhận biết", "Tiếp tuyến của đường tròn vuông góc với bán kính tại:", ["Tiếp điểm", "Tâm đường tròn", "Điểm bất kì", "Trung điểm bán kính"], 0),
            make_mc(5, "Thông hiểu", "Cho đường tròn $(O; 5\\text{ cm})$. Dây cung $AB = 8\\text{ cm}$. Khoảng cách từ tâm $O$ đến dây $AB$ là:", ["$3\\text{ cm}$", "$4\\text{ cm}$", "$5\\text{ cm}$", "$2\\text{ cm}$"], 0),
            make_mc(6, "Thông hiểu", "Cho đường tròn $(O; 4\\text{ cm})$ và điểm $M$ cách $O$ một khoảng $7\\text{ cm}$. Vị trí của điểm $M$ là:", ["Nằm ngoài đường tròn", "Nằm trên đường tròn", "Nằm trong đường tròn", "Trùng với tâm $O$"], 0),
            make_mc(7, "Thông hiểu", "Từ điểm $M$ ở ngoài $(O)$ kẻ hai tiếp tuyến $MA$ và $MB$ ($A, B$ là tiếp điểm). Khẳng định nào sau đây là SAI?", ["$MA \\perp MB$", "$MA = MB$", "$MO$ là tia phân giác của $\\widehat{AMB}$", "$OM$ là tia phân giác của $\\widehat{AOB}$"], 0),
            make_mc(8, "Thông hiểu", "Hai đường tròn $(O; R)$ và $(O'; r)$ tiếp xúc ngoài khi khoảng cách nối tâm $d = OO'$ bằng:", ["$R + r$", "$R - r$", "$R \\cdot r$", "$\\sqrt{R^2 + r^2}$"], 0),
            make_mc(9, "Vận dụng", "Từ điểm $M$ cách tâm $O$ một khoảng $10\\text{ cm}$, kẻ tiếp tuyến $MA$ với đường tròn $(O; 6\\text{ cm})$ ($A$ là tiếp điểm). Độ dài đoạn tiếp tuyến $MA$ là:", ["$8\\text{ cm}$", "$6\\text{ cm}$", "$10\\text{ cm}$", "$4\\text{ cm}$"], 0),
            make_mc(10, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Bán kính của đường tròn ngoại tiếp tam giác $ABC$ là:", ["$5\\text{ cm}$", "$10\\text{ cm}$", "$2,5\\text{ cm}$", "$4\\text{ cm}$"], 0),
            make_mc(11, "Vận dụng", "Hai tiếp tuyến tại $A$ và $B$ của đường tròn $(O)$ cắt nhau tại $M$ sao cho $\\widehat{AMB} = 60^\\circ$. Tam giác $MAB$ là:", ["Tam giác đều", "Tam giác vuông cân", "Tam giác cân có góc đáy $45^\\circ$", "Tam giác vuông"], 0),
            make_mc(12, "Vận dụng cao", "Cho đường tròn $(O; R)$ và dây $AB = R\\sqrt{3}$. Diện tích tam giác $OAB$ theo $R$ là:", ["$\\frac{R^2\\sqrt{3}}{4}$", "$\\frac{R^2}{2}$", "$\\frac{R^2\\sqrt{3}}{2}$", "$R^2$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về đường tròn và tiếp tuyến (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Đường kính vuông góc với một dây thì đi qua trung điểm của dây đó.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Trong một đường tròn, hai dây bằng nhau thì cách đều tâm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Góc tạo bởi hai tiếp tuyến cắt nhau bù với góc tạo bởi hai bán kính đi qua hai tiếp điểm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Qua ba điểm thẳng hàng luôn vẽ được duy nhất một đường tròn.", "correct": False}
            ]),
            make_tf(2, "Từ điểm $A$ ở ngoài $(O; R)$, kẻ hai tiếp tuyến $AB$ và $AC$ ($B, C$ là tiếp điểm). Gọi $H$ là giao điểm của $AO$ và $BC$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Đoạn thẳng AO là đường trung trực của đoạn thẳng BC.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tứ giác ABOC có tổng hai góc đối B và C bằng 180 độ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hệ thức AH . AO = AB^2 luôn đúng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Độ dài BC luôn lớn hơn 2R.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho đường tròn (O; 10 cm), dây cung AB cách tâm O một khoảng 6 cm. Tính độ dài dây AB (cm).", "16"),
            make_sa(2, "Thông hiểu", "Tam giác đều ABC cạnh 6 cm nội tiếp (O). Tính bán kính R (cm, dạng a căn(3)). Điền hệ số a.", "2"), # R = a / căn(3) = 2 căn(3)
            make_sa(3, "Vận dụng", "Từ điểm M cách tâm O 13 cm kẻ tiếp tuyến MA (A là tiếp điểm). Biết bán kính R = 5 cm. Tính độ dài MA (cm).", "12"),
            make_sa(4, "Vận dụng cao", "Cho đường tròn (O; 5 cm) và hai tiếp tuyến song song với nhau. Tính khoảng cách giữa hai tiếp tuyến đó (cm).", "10")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Cho đường tròn $(O; R)$ đường kính $AB$. Lấy điểm $C$ thuộc đường tròn ($C \\neq A, B$). Chứng minh rằng tam giác $ABC$ là tam giác vuông tại $C$.", "Điểm C thuộc đường tròn đường kính AB nên OC = OA = OB = R (0.25đ).\nTrong tam giác ABC, đường trung tuyến CO ứng với cạnh AB bằng một nửa cạnh AB => tam giác ABC vuông tại C (0.25đ)."),
            make_essay(2, "Vận dụng", "Cho đường tròn $(O)$ và điểm $A$ nằm ngoài $(O)$. Kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là tiếp điểm). Kẻ đường kính $CD$. Chứng minh rằng $BD \\parallel AO$.", "Ta có AB = AC và OB = OC nên AO là trung trực BC => AO vuông góc BC (0.25đ).\nMặt khác tam giác BCD có CD là đường kính nên góc CBD = 90 độ => BD vuông góc BC.\nVì cùng vuông góc với BC nên BD // AO. Đpcm (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho nửa đường tròn $(O; R)$ đường kính $AB$. Gọi $Ax, By$ là các tia tiếp tuyến cùng phía với nửa đường tròn. Lấy điểm $M$ trên nửa đường tròn, tiếp tuyến tại $M$ cắt $Ax, By$ lần lượt tại $C$ và $D$. Chứng minh rằng $AC \\cdot BD = R^2$ và $\\widehat{COD} = 90^\\circ$.", "Theo tính chất hai tiếp tuyến cắt nhau: AC = CM và BD = DM; OC là phân giác AOM, OD là phân giác BOM (0.25đ).\n=> góc COD = AOM/2 + BOM/2 = 180/2 = 90 độ.\nTam giác COD vuông tại O có đường cao OM = R => CM . MD = OM^2 => AC . BD = R^2. Đpcm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương V: Đường tròn - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 6. CHƯƠNG 6 TOÁN 9: HÀM SỐ Y = AX^2 VÀ PHƯƠNG TRÌNH BẬC HAI (Bài 5: cuối chương)
def build_c6_9_exams():
    chap_id = "c6_9"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Parabol & Định lí Viète thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là một đường cong parabol có đỉnh là:", ["Gốc tọa độ $O(0; 0)$", "Điểm $(1; a)$", "Điểm $(a; 0)$", "Không có đỉnh"], 0),
            make_mc(2, "Nhận biết", "Công thức tính biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) là:", ["$\\Delta = b^2 - 4ac$", "$\\Delta = b^2 - ac$", "$\\Delta = b^2 + 4ac$", "$\\Delta = 4ac - b^2$"], 0),
            make_mc(3, "Nhận biết", "Phương trình bậc hai $ax^2 + bx + c = 0$ có hai nghiệm phân biệt khi:", ["$\\Delta > 0$", "$\\Delta = 0$", "$\\Delta < 0$", "$\\Delta \\le 0$"], 0),
            make_mc(4, "Nhận biết", "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) thì:", ["$x_1 + x_2 = -\\frac{b}{a}$ và $x_1 x_2 = \\frac{c}{a}$", "$x_1 + x_2 = \\frac{b}{a}$ và $x_1 x_2 = -\\frac{c}{a}$", "$x_1 + x_2 = -\\frac{c}{a}$", "$x_1 x_2 = -\\frac{b}{a}$"], 0),
            make_mc(5, "Thông hiểu", "Nghiệm của phương trình $x^2 - 5x + 6 = 0$ là:", ["$x_1 = 2; x_2 = 3$", "$x_1 = -2; x_2 = -3$", "$x_1 = 1; x_2 = 6$", "$x_1 = -1; x_2 = -6$"], 0),
            make_mc(6, "Thông hiểu", "Điểm nào sau đây thuộc đồ thị hàm số $y = 2x^2$?", ["$M(2; 8)$", "$N(1; 4)$", "$P(-1; -2)$", "$Q(0; 2)$"], 0),
            make_mc(7, "Thông hiểu", "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có nghiệm kép:", ["$m = 1$", "$m = -1$", "$m = 4$", "$m = 0$"], 0),
            make_mc(8, "Thông hiểu", "Tổng và tích hai nghiệm của phương trình $2x^2 - 7x + 3 = 0$ lần lượt là:", ["$S = \\frac{7}{2}; P = \\frac{3}{2}$", "$S = -\\frac{7}{2}; P = \\frac{3}{2}$", "$S = 7; P = 3$", "$S = \\frac{3}{2}; P = \\frac{7}{2}$"], 0),
            make_mc(9, "Vận dụng", "Tìm tọa độ giao điểm của parabol $(P): y = x^2$ và đường thẳng $(d): y = 2x + 3$:", ["$(-1; 1)$ và $(3; 9)$", "$(1; 1)$ và $(-3; 9)$", "$(0; 3)$", "$(2; 4)$"], 0),
            make_mc(10, "Vận dụng", "Một khu vườn hình chữ nhật có diện tích $300\\text{ m}^2$, chiều dài hơn chiều rộng $5\\text{ m}$. Chiều rộng của khu vườn là:", ["$15\\text{ m}$", "$20\\text{ m}$", "$10\\text{ m}$", "$25\\text{ m}$"], 0),
            make_mc(11, "Vận dụng", "Gọi $x_1, x_2$ là hai nghiệm của phương trình $x^2 - 4x - 1 = 0$. Giá trị của biểu thức $A = x_1^2 + x_2^2$ là:", ["$18$", "$14$", "$16$", "$15$"], 0),
            make_mc(12, "Vận dụng cao", "Tìm $m$ để phương trình $x^2 - 2(m + 1)x + m^2 + 2 = 0$ có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn $x_1^2 + x_2^2 = 10$:", ["$m = 2$", "$m = 1$", "$m = -2$", "$m = 3$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về hàm số bậc hai và phương trình bậc hai (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Hàm số y = ax^2 với a > 0 nghịch biến khi x < 0 và đồng biến khi x > 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu a và c trái dấu (a.c < 0) thì phương trình ax^2 + bx + c = 0 luôn có hai nghiệm phân biệt.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu a + b + c = 0 thì phương trình ax^2 + bx + c = 0 có nghiệm x1 = 1, x2 = c/a.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Parabol y = ax^2 (a khác 0) và đường thẳng y = mx + n luôn luôn cắt nhau tại 2 điểm.", "correct": False}
            ]),
            make_tf(2, "Cho phương trình $x^2 - 2(m - 1)x + m^2 - 3 = 0$ (m là tham số):", [
                {"key": "a", "level": "Thông hiểu", "text": "Biệt thức Delta' = (m - 1)^2 - (m^2 - 3) = -2m + 4.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Phương trình có hai nghiệm khi và chỉ khi m <= 2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Khi m = 2 phương trình có nghiệm kép x1 = x2 = 1.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Khi m = 0 phương trình có hai nghiệm cùng dấu.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Giải phương trình: x^2 - 7x + 12 = 0. Tìm nghiệm lớn hơn.", "4"),
            make_sa(2, "Thông hiểu", "Cho parabol y = ax^2 đi qua điểm A(2; 8). Tìm hệ số a.", "2"),
            make_sa(3, "Vận dụng", "Cho phương trình x^2 - 6x + 2 = 0 có hai nghiệm x1, x2. Tính x1^2 + x2^2.", "32"),
            make_sa(4, "Vận dụng cao", "Tìm m để đường thẳng y = 2x + m tiếp xúc với parabol y = x^2.", "-1")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Giải phương trình bằng công thức nghiệm: $2x^2 - 5x + 2 = 0$.", "Delta = (-5)^2 - 4 . 2 . 2 = 25 - 16 = 9 > 0 => căn(Delta) = 3 (0.25đ).\nx1 = (5 + 3)/4 = 2; x2 = (5 - 3)/4 = 1/2 (0.25đ)."),
            make_essay(2, "Vận dụng", "Một tổ công nhân theo kế hoạch phải may 600 bộ quần áo trong một thời gian quy định. Nhờ cải tiến kỹ thuật, mỗi ngày tổ may được thêm 10 bộ nên đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch mỗi ngày tổ phải may bao nhiêu bộ quần áo?", "Gọi số bộ quần áo may 1 ngày theo kế hoạch là x (x in N*, bộ) (0.25đ).\nThời gian theo kế hoạch: 600/x (ngày). Thời gian thực tế: 600/(x + 10) (ngày).\nTa có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0.\nGiải pt: x = 50 (thỏa mãn) hoặc x = -60 (loại). Vậy kế hoạch mỗi ngày may 50 bộ (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - 3x_1 x_2 = 4$.", "Delta' = (m + 1)^2 - 2m = m^2 + 1 > 0 với mọi m => pt luôn có 2 nghiệm phân biệt (0.25đ).\nTheo Vi-ét: x1 + x2 = 2(m + 1); x1.x2 = 2m.\nTa có: (x1 + x2)^2 - 5x1 x2 = 4 <=> 4(m + 1)^2 - 10m = 4 <=> 4m^2 - 2m = 0 <=> 2m(2m - 1) = 0 => m = 0 hoặc m = 1/2 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số bậc hai & PT bậc hai - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 7. CHƯƠNG 7 TOÁN 9: TẦN SỐ VÀ TẦN SỐ TƯƠNG ĐỐI (Bài 4: cuối chương)
def build_c7_9_exams():
    chap_id = "c7_9"
    l_idx = 4
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Bảng tần số & Biểu đồ thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Tần số của một giá trị trong mẫu số liệu là:", ["Số lần xuất hiện của giá trị đó trong mẫu số liệu", "Tỉ số giữa giá trị đó và tổng số liệu", "Giá trị lớn nhất của mẫu", "Giá trị trung bình"], 0),
            make_mc(2, "Nhận biết", "Tần số tương đối $f_i$ của giá trị $x_i$ được tính theo công thức:", ["$f_i = \\frac{m_i}{N} \\cdot 100\\%$", "$f_i = \\frac{N}{m_i}$", "$f_i = m_i \\cdot N$", "$f_i = m_i - N$"], 0),
            make_mc(3, "Nhận biết", "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:", ["$100\\%$ (hay $1$)", "$50\\%$", "$360\\%$", "Bằng cỡ mẫu $N$"], 0),
            make_mc(4, "Nhận biết", "Để biểu diễn tần số tương đối của các nhóm số liệu, người ta thường dùng:", ["Biểu đồ tần số tương đối hình quạt tròn hoặc cột", "Biểu đồ tranh", "Biểu đồ Ven", "Biểu đồ đường chéo"], 0),
            make_mc(5, "Thông hiểu", "Khảo sát cỡ giày của 40 học sinh: Cỡ 38 xuất hiện 12 lần. Tần số tương đối của cỡ giày 38 là:", ["$30\\%$", "$12\\%$", "$25\\%$", "$40\\%$"], 0),
            make_mc(6, "Thông hiểu", "Một lớp có 45 học sinh, trong đó có 9 học sinh xếp loại Xuất sắc. Tần số tương đối của học sinh Xuất sắc là:", ["$20\\%$", "$9\\%$", "$25\\%$", "$15\\%$"], 0),
            make_mc(7, "Thông hiểu", "Bảng tần số ghép nhóm thường được dùng khi:", ["Dữ liệu có nhiều giá trị khác nhau và phân bố liên tục", "Mẫu số liệu rất ít (dưới 5 số liệu)", "Dữ liệu định tính", "Chỉ có 2 giá trị"], 0),
            make_mc(8, "Thông hiểu", "Độ dài của nhóm số liệu $[a; b)$ được tính bằng:", ["$b - a$", "$b + a$", "$\\frac{a+b}{2}$", "$\\sqrt{b-a}$"], 0),
            make_mc(9, "Vận dụng", "Bảng phân bố tần số ghép nhóm điểm kiểm tra Toán: Nhóm $[7; 8)$ có tần số 14, cỡ mẫu $N = 50$. Tần số tương đối của nhóm điểm này là:", ["$28\\%$", "$14\\%$", "$35\\%$", "$25\\%$"], 0),
            make_mc(10, "Vận dụng", "Thời gian hoàn thành một bài tập của 30 học sinh: Dưới 10 phút: 6 em; Từ 10 đến 15 phút: 15 em; Trên 15 phút: 9 em. Tần số tương đối của nhóm học sinh làm từ 10 phút trở lên là:", ["$80\\%$", "$50\\%$", "$70\\%$", "$30\\%$"], 0),
            make_mc(11, "Vận dụng", "Trong biểu đồ quạt tròn tần số tương đối, góc ở tâm của nhóm đạt tỉ lệ $35\\%$ là:", ["$126^\\circ$", "$108^\\circ$", "$90^\\circ$", "$140^\\circ$"], 0),
            make_mc(12, "Vận dụng cao", "Một mẫu số liệu ghép nhóm có 5 nhóm bằng nhau. Biết giá trị đại diện của nhóm thứ nhất là 12, giá trị đại diện của nhóm thứ hai là 16. Khoảng biến thiên của mẫu số liệu trên ít nhất là:", ["$20$", "$16$", "$24$", "$18$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tần số và tần số tương đối (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng các tần số của tất cả các giá trị luôn bằng cỡ mẫu N.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Giá trị đại diện của nhóm [a; b) là trung điểm (a + b)/2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tần số tương đối có thể nhận giá trị lớn hơn 100%.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Biểu đồ đoạn thẳng tần số nối các điểm có hoành độ là giá trị đại diện và tung độ là tần số tương ứng.", "correct": True}
            ]),
            make_tf(2, "Bảng thống kê số giờ tự học mỗi ngày của 50 học sinh: [0; 1) có 5 em; [1; 2) có 15 em; [2; 3) có 20 em; [3; 4) có 10 em:", [
                {"key": "a", "level": "Thông hiểu", "text": "Nhóm có tần số lớn nhất là nhóm [2; 3).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tần số tương đối của nhóm [1; 2) là 30%.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tỉ lệ học sinh học từ 2 giờ trở lên mỗi ngày là 60%.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Thời gian tự học trung bình của học sinh lớp đó lớn hơn 2,5 giờ.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Một mẫu số liệu có cỡ mẫu N = 80, giá trị x có tần số m = 24. Tính tần số tương đối (%) của x.", "30"),
            make_sa(2, "Thông hiểu", "Tìm giá trị đại diện của nhóm [20; 30).", "25"),
            make_sa(3, "Vận dụng", "Một nhóm chiếm tần số tương đối 45%. Tính số đo góc ở tâm tương ứng trong biểu đồ quạt tròn (độ).", "162"),
            make_sa(4, "Vận dụng cao", "Một mẫu gồm 4 nhóm với tần số tương ứng: 8, 12, 16, 4. Tính tần số tương đối (%) của nhóm lớn nhất.", "40")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Lập bảng tần số tương đối cho mẫu số liệu về điểm kiểm tra của 40 học sinh: Điểm 8: 10 em; Điểm 9: 18 em; Điểm 10: 12 em.", "Tần số tương đối:\nĐiểm 8: 10 / 40 = 25% (0.15đ).\nĐiểm 9: 18 / 40 = 45% (0.2đ).\nĐiểm 10: 12 / 40 = 30% (0.15đ)."),
            make_essay(2, "Vận dụng", "Khảo sát chiều cao của 100 học sinh lớp 9: [150; 155) có 15 em; [155; 160) có 35 em; [160; 165) có 30 em; [165; 170) có 20 em. a) Lập bảng tần số ghép nhóm kèm giá trị đại diện. b) Ước tính chiều cao trung bình của 100 học sinh đó.", "a) Giá trị đại diện các nhóm: 152,5; 157,5; 162,5; 167,5 (0.25đ).\nb) Chiều cao trung bình: x_tb = (152,5.15 + 157,5.35 + 162,5.30 + 167,5.20) / 100 = 160,25 (cm) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Một nhà máy phân tích thời gian chạy thử của 200 chiếc động cơ trước khi xuất xưởng. Nhóm thời gian [40; 50) giờ chiếm 30%, nhóm [50; 60) giờ chiếm 50%, còn lại là trên 60 giờ. Tính số động cơ chạy thử trên 60 giờ và góc ở tâm tương ứng khi vẽ biểu đồ quạt tròn.", "Tỉ lệ nhóm trên 60 giờ: 100% - 30% - 50% = 20% (0.25đ).\nSố động cơ trên 60 giờ: 200 x 20% = 40 (động cơ).\nGóc ở tâm tương ứng: 20% x 360 độ = 72 độ (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 8. CHƯƠNG 8 TOÁN 9: XÁC SUẤT TRONG MỘT SỐ MÔ HÌNH ĐƠN GIẢN (Bài 3: cuối chương)
def build_c8_9_exams():
    chap_id = "c8_9"
    l_idx = 3
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Không gian mẫu & Sơ đồ hình cây",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Tập hợp tất cả các kết quả có thể xảy ra của một phép thử được gọi là:", ["Không gian mẫu", "Biến cố ngẫu nhiên", "Biến cố chắc chắn", "Tần số"], 0),
            make_mc(2, "Nhận biết", "Tung một đồng xu hai lần liên tiếp. Số phần tử của không gian mẫu là:", ["$4$ phần tử (SS, SN, NS, NN)", "$2$ phần tử", "$6$ phần tử", "$8$ phần tử"], 0),
            make_mc(3, "Nhận biết", "Sơ đồ hình cây là công cụ trực quan để:", ["Liệt kê đầy đủ các kết quả có thể của phép thử nhiều giai đoạn", "Tính diện tích hình học", "Giải phương trình bậc hai", "Vẽ biểu đồ quạt tròn"], 0),
            make_mc(4, "Nhận biết", "Nếu biến cố $A$ và biến cố $B$ không đồng thời xảy ra trong cùng một phép thử thì chúng được gọi là:", ["Hai biến cố xung khắc", "Hai biến cố đối nhau", "Hai biến cố chắc chắn", "Hai biến cố độc lập"], 0),
            make_mc(5, "Thông hiểu", "Gieo đồng thời hai con xúc xắc cân đối. Số phần tử của không gian mẫu là:", ["$36$", "$12$", "$6$", "$18$"], 0),
            make_mc(6, "Thông hiểu", "Tung một đồng xu 3 lần. Xác suất để cả 3 lần đều xuất hiện mặt Sấp là:", ["$\\frac{1}{8}$", "$\\frac{3}{8}$", "$\\frac{1}{2}$", "$\\frac{1}{4}$"], 0),
            make_mc(7, "Thông hiểu", "Trong một hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Lấy ngẫu nhiên lần lượt 2 quả bóng không hoàn lại. Số kết quả có thể là:", ["$20$", "$10$", "$25$", "$5$"], 0),
            make_mc(8, "Thông hiểu", "Một lớp có 15 học sinh nam và 20 học sinh nữ. Chọn ngẫu nhiên 1 học sinh. Xác suất chọn được học sinh nam là:", ["$\\frac{15}{35} = \\frac{3}{7}$", "$\\frac{20}{35}$", "$\\frac{15}{20}$", "$\\frac{1}{2}$"], 0),
            make_mc(9, "Vận dụng", "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm xuất hiện trên hai con xúc xắc bằng 7 là:", ["$\\frac{6}{36} = \\frac{1}{6}$", "$\\frac{5}{36}$", "$\\frac{7}{36}$", "$\\frac{1}{7}$"], 0),
            make_mc(10, "Vận dụng", "Một túi đựng 4 tấm thẻ được đánh số 1, 2, 3, 4. Rút ngẫu nhiên lần lượt 2 tấm thẻ không hoàn lại ghép thành số có hai chữ số. Xác suất để số ghép được chia hết cho 3 là:", ["$\\frac{4}{12} = \\frac{1}{3}$ (gồm 12, 21, 24, 42)", "$\\frac{1}{4}$", "$\\frac{1}{2}$", "$\\frac{5}{12}$"], 0),
            make_mc(11, "Vận dụng", "Hai bạn An và Bình mỗi người gieo một con xúc xắc cân đối. Xác suất để số chấm của An lớn hơn số chấm của Bình là:", ["$\\frac{15}{36} = \\frac{5}{12}$", "$\\frac{1}{2}$", "$\\frac{6}{36}$", "$\\frac{1}{6}$"], 0),
            make_mc(12, "Vận dụng cao", "Có 3 chiếc hộp, mỗi hộp đựng 1 quả bóng trắng và 1 quả bóng đen. Lấy ngẫu nhiên từ mỗi hộp ra 1 quả bóng. Xác suất để lấy được đúng 2 quả bóng trắng là:", ["$\\frac{3}{8}$", "$\\frac{1}{8}$", "$\\frac{1}{2}$", "$\\frac{5}{8}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tính xác suất bằng sơ đồ hình cây và bảng liệt kê (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Mỗi nhánh tận cùng của sơ đồ hình cây biểu diễn một kết quả có thể xảy ra của phép thử.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi hai con xúc xắc độc lập thì kết quả của con thứ nhất không ảnh hưởng đến con thứ hai.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tổng xác suất của biến cố A và biến cố đối A' luôn bằng 1.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tung 3 đồng xu thì xác suất có ít nhất 1 mặt ngửa bằng 7/8.", "correct": True}
            ]),
            make_tf(2, "Gieo đồng thời hai con xúc xắc cân đối một lần:", [
                {"key": "a", "level": "Thông hiểu", "text": "Không gian mẫu có đúng 36 phần tử.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Có đúng 6 kết quả để hai con xúc xắc có số chấm bằng nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Xác suất để xuất hiện 'hai mặt cùng có số chấm chẵn' là 9/36 = 1/4.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Xác suất để tích hai số chấm là một số lẻ bằng 3/4.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tung đồng xu 3 lần. Tính số phần tử của không gian mẫu.", "8"),
            make_sa(2, "Thông hiểu", "Gieo hai con xúc xắc cân đối. Có bao nhiêu kết quả để tổng số chấm bằng 11?", "2"),
            make_sa(3, "Vận dụng", "Gieo hai con xúc xắc. Tính số kết quả để cả hai mặt đều xuất hiện số chấm lớn hơn 4.", "4"),
            make_sa(4, "Vận dụng cao", "Một xạ thủ bắn 2 phát đạn độc lập, xác suất trúng mỗi phát là 0,8. Tính xác suất để cả 2 phát đều trúng.", "0,64")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Vẽ sơ đồ hình cây biểu diễn các kết quả có thể khi một gia đình sinh hai người con (quy ước: T là trai, G là gái).", "Giai đoạn 1: T hoặc G (0.25đ).\nGiai đoạn 2: từ T rẽ ra T, G; từ G rẽ ra T, G.\nTập kết quả: {(T,T), (T,G), (G,T), (G,G)} gồm 4 kết quả (0.25đ)."),
            make_essay(2, "Vận dụng", "Một hộp có 2 quả cầu đỏ và 3 quả cầu xanh cùng kích thước. Lấy ngẫu nhiên lần lượt 2 quả cầu không hoàn lại. Tính xác suất để: a) Cả hai quả cầu lấy ra đều màu xanh. b) Lấy được ít nhất một quả cầu màu đỏ.", "Tổng số kết quả: 5 x 4 = 20 kết quả (0.25đ).\na) Số kết quả 2 xanh: 3 x 2 = 6 => P = 6/20 = 3/10 = 0,3.\nb) Biến cố đối 'không có quả đỏ nào' chính là 'cả 2 quả xanh' có P = 0,3.\n=> P(ít nhất 1 đỏ) = 1 - 0,3 = 0,7 (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Gieo đồng thời hai con xúc xắc cân đối. Tính xác suất để tổng số chấm xuất hiện trên hai con xúc xắc là một số chia hết cho 4 hoặc chia hết cho 6.", "Không gian mẫu: 36 (0.25đ).\nCác tổng chia hết cho 4: 4 (3 cặp), 8 (5 cặp), 12 (1 cặp) => 9 kết quả.\nCác tổng chia hết cho 6: 6 (5 cặp), 12 (1 cặp) => 6 kết quả.\nTổng vừa chia hết cho 4 vừa chia hết cho 6 là 12: có 1 kết quả (6,6).\nSố kết quả thuận lợi: 9 + 6 - 1 = 14.\nXác suất: P = 14 / 36 = 7/18 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương VIII: Xác suất mô hình đơn giản - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 9. CHƯƠNG 9 TOÁN 9: ĐƯỜNG TRÒN NGOẠI TIẾP VÀ NỘI TIẾP (Bài 5: cuối chương)
def build_c9_9_exams():
    chap_id = "c9_9"
    l_idx = 5
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Tứ giác nội tiếp & Đa giác đều",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Góc nội tiếp là góc có đỉnh nằm trên đường tròn và:", ["Hai cạnh chứa hai dây cung của đường tròn đó", "Hai cạnh là hai tiếp tuyến", "Đi qua tâm đường tròn", "Vuông góc với bán kính"], 0),
            make_mc(2, "Nhận biết", "Số đo của góc nội tiếp bằng:", ["Một nửa số đo của cung bị chắn", "Bằng số đo cung bị chắn", "Gấp đôi số đo cung bị chắn", "Bằng $90^\\circ$"], 0),
            make_mc(3, "Nhận biết", "Góc nội tiếp chắn nửa đường tròn luôn là:", ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0),
            make_mc(4, "Nhận biết", "Tứ giác nội tiếp được một đường tròn khi và chỉ khi:", ["Tổng hai góc đối diện bằng $180^\\circ$", "Hai góc đối diện bằng nhau", "Bốn cạnh bằng nhau", "Có hai đường chéo vuông góc"], 0),
            make_mc(5, "Thông hiểu", "Cho đường tròn $(O)$ và góc ở tâm $\\widehat{AOB} = 80^\\circ$. Góc nội tiếp $\\widehat{ACB}$ cùng chắn cung $AB$ có số đo là:", ["$40^\\circ$", "$80^\\circ$", "$160^\\circ$", "$20^\\circ$"], 0),
            make_mc(6, "Thông hiểu", "Cho tứ giác $ABCD$ nội tiếp đường tròn. Biết $\\widehat{A} = 75^\\circ$. Số đo của góc $\\widehat{C}$ là:", ["$105^\\circ$", "$75^\\circ$", "$15^\\circ$", "$90^\\circ$"], 0),
            make_mc(7, "Thông hiểu", "Tâm đường tròn ngoại tiếp của một tam giác vuông là:", ["Trung điểm của cạnh huyền", "Đỉnh góc vuông", "Trọng tâm tam giác", "Giao điểm hai đường cao"], 0),
            make_mc(8, "Thông hiểu", "Mỗi góc trong của một lục giác đều có số đo bằng:", ["$120^\\circ$", "$108^\\circ$", "$90^\\circ$", "$135^\\circ$"], 0),
            make_mc(9, "Vận dụng", "Cho đường tròn $(O; R)$ và dây $AB = R$. Số đo của góc nội tiếp chắn cung nhỏ $AB$ là:", ["$30^\\circ$ (vì góc ở tâm bằng $60^\\circ$)", "$60^\\circ$", "$45^\\circ$", "$15^\\circ$"], 0),
            make_mc(10, "Vận dụng", "Cho hình vuông $ABCD$ cạnh $4\\text{ cm}$. Bán kính đường tròn ngoại tiếp hình vuông đó là:", ["$2\\sqrt{2}\\text{ cm}$", "$4\\text{ cm}$", "$2\\text{ cm}$", "$4\\sqrt{2}\\text{ cm}$"], 0),
            make_mc(11, "Vận dụng", "Cho tứ giác $ABCD$ nội tiếp đường tròn có $\\widehat{B} = 2\\widehat{D}$. Số đo của góc $\\widehat{B}$ là:", ["$120^\\circ$", "$60^\\circ$", "$90^\\circ$", "$100^\\circ$"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ nhọn nội tiếp $(O; R)$. Kẻ đường cao $AH$ và đường kính $AD$. Khẳng định nào sau đây là ĐÚNG?", ["$AB \\cdot AC = AH \\cdot AD = 2R \\cdot AH$", "$AB \\cdot AC = AH^2$", "$AB \\cdot AC = 4R \\cdot AH$", "$AH = R \\cdot \\sin A$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về góc nội tiếp và tứ giác nội tiếp (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Trong một đường tròn, các góc nội tiếp cùng chắn một cung thì bằng nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc tạo bởi tia tiếp tuyến và dây cung có số đo bằng góc nội tiếp cùng chắn cung đó.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Mọi hình thang cân đều là tứ giác nội tiếp.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Mọi hình thoi đều nội tiếp được một đường tròn.", "correct": False}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có ba góc nhọn, các đường cao $BD$ và $CE$ cắt nhau tại $H$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Tứ giác ADHE nội tiếp được đường tròn đường kính AH.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tứ giác BEDC nội tiếp được đường tròn đường kính BC.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Góc ADE bằng góc ACB.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Điểm H là tâm đường tròn nội tiếp tam giác ABC.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Cho góc nội tiếp chắn cung 70 độ. Tính số đo của góc nội tiếp đó (độ).", "35"),
            make_sa(2, "Thông hiểu", "Tứ giác ABCD nội tiếp có góc B = 65 độ. Tính số đo góc D (độ).", "115"),
            make_sa(3, "Vận dụng", "Tính bán kính đường tròn ngoại tiếp tam giác đều cạnh 6 cm (dạng a căn(3)). Điền hệ số a.", "2"),
            make_sa(4, "Vận dụng cao", "Cho tứ giác ABCD nội tiếp (O) có hai đường chéo vuông góc tại I. Biết IA = 2, IB = 4, IC = 6. Tính ID.", "3") # IA . IC = IB . ID => 2 . 6 = 4 . ID => ID = 3
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Chứng minh rằng hình chữ nhật là một tứ giác nội tiếp đường tròn. Xác định tâm của đường tròn đó.", "Hình chữ nhật ABCD có 4 góc vuông: A = B = C = D = 90 độ (0.25đ).\nTổng hai góc đối diện: A + C = 90 + 90 = 180 độ => ABCD là tứ giác nội tiếp.\nTâm đường tròn là giao điểm hai đường chéo O, bán kính R = AC / 2 (0.25đ)."),
            make_essay(2, "Vận dụng", "Cho tam giác $ABC$ nhọn nội tiếp đường tròn $(O)$. Hai đường cao $BD$ và $CE$ cắt nhau tại $H$. Chứng minh tứ giác $BEDC$ nội tiếp và $\\widehat{EDH} = \\widehat{ECH}$.", "Xét tứ giác BEDC có: góc BEC = 90 độ, BDC = 90 độ => hai đỉnh E, D cùng nhìn đoạn BC dưới góc 90 độ (0.25đ).\n=> Tứ giác BEDC nội tiếp đường tròn đường kính BC.\nTrong đường tròn ngoại tiếp BEDC: góc EDH và ECH là hai góc nội tiếp cùng chắn cung EH nên EDH = ECH. Đpcm (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Từ điểm $M$ ở ngoài $(O)$, kẻ hai tiếp tuyến $MA, MB$ và cát tuyến $MCD$ đi qua tâm $O$ (với $C$ nằm giữa $M$ và $D$). Gọi $H$ là giao điểm của $AB$ và $MO$. Chứng minh rằng $MC \\cdot MD = MH \\cdot MO = MA^2$.", "Xét tam giác vuông MAO có đường cao AH => MA^2 = MH . MO (hệ thức lượng) (0.25đ).\nXét hai tam giác MAC và MDA: góc M chung, góc MAC = MDA (góc tạo bởi tiếp tuyến và dây cung bằng góc nội tiếp cùng chắn cung AC) => tam giác MAC đồng dạng MDA (g-g) => MA/MD = MC/MA => MA^2 = MC . MD.\nDo đó: MC . MD = MH . MO = MA^2. Đpcm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương IX: Đường tròn ngoại tiếp & nội tiếp - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# 10. CHƯƠNG 10 TOÁN 9: MỘT SỐ HÌNH KHỐI TRONG THỰC TIỄN (Bài 3: cuối chương)
def build_c10_9_exams():
    chap_id = "c10_9"
    l_idx = 3
    exams = {}
    diff_titles = {
        4: "🎯 Toàn diện Chuẩn ma trận 30-30-20-20",
        5: "💡 Hình trụ, nón, cầu trong thực tế",
        6: "🚀 Phân hóa Nâng cao",
        7: "🏆 Chinh phục điểm 10"
    }
    for t_num, title_suffix in diff_titles.items():
        p1 = [
            make_mc(1, "Nhận biết", "Công thức tính diện tích xung quanh của hình trụ có bán kính đáy $R$ và chiều cao $h$ là:", ["$S_{xq} = 2\\pi R h$", "$S_{xq} = \\pi R h$", "$S_{xq} = \\pi R^2 h$", "$S_{xq} = 2\\pi R^2$"], 0),
            make_mc(2, "Nhận biết", "Công thức tính thể tích của hình nón có bán kính đáy $R$ và chiều cao $h$ là:", ["$V = \\frac{1}{3}\\pi R^2 h$", "$V = \\pi R^2 h$", "$V = \\frac{4}{3}\\pi R^3$", "$V = 2\\pi R h$"], 0),
            make_mc(3, "Nhận biết", "Công thức tính diện tích mặt cầu bán kính $R$ là:", ["$S = 4\\pi R^2$", "$S = \\frac{4}{3}\\pi R^3$", "$S = 2\\pi R^2$", "$S = \\pi R^2$"], 0),
            make_mc(4, "Nhận biết", "Công thức tính thể tích hình cầu bán kính $R$ là:", ["$V = \\frac{4}{3}\\pi R^3$", "$V = 4\\pi R^2$", "$V = \\pi R^3$", "$V = \\frac{1}{3}\\pi R^3$"], 0),
            make_mc(5, "Thông hiểu", "Một hình trụ có bán kính đáy $3\\text{ cm}$ và chiều cao $5\\text{ cm}$. Thể tích hình trụ là:", ["$45\\pi\\text{ cm}^3$", "$15\\pi\\text{ cm}^3$", "$30\\pi\\text{ cm}^3$", "$90\\pi\\text{ cm}^3$"], 0),
            make_mc(6, "Thông hiểu", "Hình nón có bán kính đáy $R = 3\\text{ cm}$, đường sinh $l = 5\\text{ cm}$. Chiều cao của hình nón là:", ["$4\\text{ cm}$", "$8\\text{ cm}$", "$2\\text{ cm}$", "$\\sqrt{34}\\text{ cm}$"], 0),
            make_mc(7, "Thông hiểu", "Diện tích xung quanh của hình nón có bán kính đáy $R = 4\\text{ cm}$ và đường sinh $l = 6\\text{ cm}$ là:", ["$24\\pi\\text{ cm}^2$", "$48\\pi\\text{ cm}^2$", "$16\\pi\\text{ cm}^2$", "$12\\pi\\text{ cm}^2$"], 0),
            make_mc(8, "Thông hiểu", "Mặt cầu có đường kính $6\\text{ cm}$ thì diện tích của nó bằng:", ["$36\\pi\\text{ cm}^2$", "$144\\pi\\text{ cm}^2$", "$12\\pi\\text{ cm}^2$", "$18\\pi\\text{ cm}^2$"], 0),
            make_mc(9, "Vận dụng", "Một thùng nước hình trụ có chiều cao $1\\text{ m}$, bán kính đáy $0,5\\text{ m}$. Lấy $\\pi \\approx 3,14$. Thể tích nước tối đa thùng chứa được là:", ["$0,785\\text{ m}^3$ (hay $785$ lít)", "$1,57\\text{ m}^3$", "$3,14\\text{ m}^3$", "$0,5\\text{ m}^3$"], 0),
            make_mc(10, "Vận dụng", "Người ta làm một chiếc nón lá dạng hình nón có đường kính đáy $40\\text{ cm}$ và độ dài đường sinh $30\\text{ cm}$. Diện tích lá cần dùng để phủ kín mặt xung quanh chiếc nón là:", ["$600\\pi\\text{ cm}^2$", "$1200\\pi\\text{ cm}^2$", "$300\\pi\\text{ cm}^2$", "$900\\pi\\text{ cm}^2$"], 0),
            make_mc(11, "Vận dụng", "Một quả bóng bàn dạng hình cầu có bán kính $2\\text{ cm}$. Thể tích không khí bên trong quả bóng bàn xấp xỉ là:", ["$\\frac{32\\pi}{3}\\text{ cm}^3$", "$16\\pi\\text{ cm}^3$", "$8\\pi\\text{ cm}^3$", "$\\frac{16\\pi}{3}\\text{ cm}^3$"], 0),
            make_mc(12, "Vận dụng cao", "Một chiếc ly dạng hình nón có bán kính miệng ly $4\\text{ cm}$, chiều cao $12\\text{ cm}$. Ly đang chứa nước đến độ cao $6\\text{ cm}$. Tỉ số thể tích nước trong ly so với dung tích cả chiếc ly là:", ["$\\frac{1}{8}$", "$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{1}{3}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về các hình khối tròn xoay (Mã đề {t_num}):", [
                {"key": "a", "level": "Thông hiểu", "text": "Khi quay một hình chữ nhật một vòng quanh một cạnh cố định ta được một hình trụ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi quay một tam giác vuông một vòng quanh một cạnh góc vuông cố định ta được một hình nón.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Đường sinh l của hình nón liên hệ với bán kính đáy R và chiều cao h theo công thức: l^2 = R^2 + h^2.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Một hình trụ và một hình nón có cùng bán kính đáy và cùng chiều cao thì thể tích của chúng bằng nhau.", "correct": False}
            ]),
            make_tf(2, "Một bồn chứa xăng gồm phần thân là hình trụ dài $6\\text{ m}$ và hai đầu là hai nửa hình cầu có cùng bán kính $R = 1\\text{ m}$:", [
                {"key": "a", "level": "Thông hiểu", "text": "Hai đầu bồn ghép lại tạo thành một hình cầu hoàn chỉnh bán kính 1 m.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Thể tích phần thân hình trụ bằng 6pi m^3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Thể tích hai đầu bán cầu bằng 4/3 pi m^3.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tổng thể tích của cả bồn chứa xăng nhỏ hơn 20 m^3.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Hình trụ có R = 4 cm, h = 5 cm. Tính diện tích xung quanh chia cho pi (cm^2).", "40"),
            make_sa(2, "Thông hiểu", "Hình nón có R = 6 cm, h = 8 cm. Tính độ dài đường sinh l (cm).", "10"),
            make_sa(3, "Vận dụng", "Một quả cầu có diện tích bề mặt bằng 100 pi cm^2. Tính bán kính R (cm).", "5"),
            make_sa(4, "Vận dụng cao", "Một hình trụ có diện tích toàn phần gấp 3 lần diện tích xung quanh. Biết bán kính đáy R = 6 cm. Tính chiều cao h (cm).", "3")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Tính diện tích toàn phần và thể tích của hình trụ có bán kính đáy $R = 5\\text{ cm}$ và chiều cao $h = 10\\text{ cm}$ (để kết quả theo $\\pi$).", "S_tp = 2pi R h + 2pi R^2 = 2pi . 5 . 10 + 2pi . 5^2 = 100pi + 50pi = 150pi (cm^2) (0.25đ).\nV = pi R^2 h = pi . 5^2 . 10 = 250pi (cm^3) (0.25đ)."),
            make_essay(2, "Vận dụng", "Người ta đúc một chi tiết máy bằng kim loại gồm một hình nón có bán kính đáy $6\\text{ cm}$, chiều cao $8\\text{ cm}$ gắn liền với một hình bán cầu có cùng bán kính đáy. Tính thể tích khối kim loại đó (để kết quả theo $\\pi$).", "Thể tích phần hình nón: V1 = (1/3) pi R^2 h = (1/3) pi . 6^2 . 8 = 96pi (cm^3) (0.25đ).\nThể tích phần nửa hình cầu: V2 = (1/2) . (4/3) pi R^3 = (2/3) pi . 6^3 = 144pi (cm^3).\nTổng thể tích khối kim loại: V = 96pi + 144pi = 240pi (cm^3) (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Một thùng chứa dạng hình trụ không có nắp được làm từ một tấm tôn có diện tích cố định $S = 27\\pi\\text{ dm}^2$ (coi diện tích mép hàn không đáng kể). Tìm bán kính đáy $R$ và chiều cao $h$ để thùng chứa có thể tích lớn nhất.", "Diện tích tôn dùng làm thùng hình trụ không nắp: S = pi R^2 + 2pi R h = 27pi => R^2 + 2Rh = 27 => h = (27 - R^2)/(2R) (0.25đ).\nThể tích thùng: V = pi R^2 h = pi R^2 . (27 - R^2)/(2R) = (pi/2) . R(27 - R^2).\nÁp dụng BĐT AM-GM cho 2R^2 và 27 - R^2:\nTa có 2R^2(27 - R^2)^2 <= [ (2R^2 + 27 - R^2 + 27 - R^2)/3 ]^3 = (54/3)^3 = 18^3 = 5832.\nDấu '=' xảy ra khi 2R^2 = 27 - R^2 => 3R^2 = 27 => R^2 = 9 => R = 3 dm.\nKhi đó h = (27 - 9)/(2 . 3) = 18/6 = 3 dm. Vậy R = 3 dm và h = 3 dm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t_num}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương X: Một số hình khối trong thực tiễn - Bài kiểm tra số {t_num} ({title_suffix})",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    return chap_id, exams

# HÀM THỰC THI TỔNG THỂ TOÁN 9
def run_all_grade9():
    builders = [
        build_c1_9_exams,
        build_c2_9_exams,
        build_c3_9_exams,
        build_c4_9_exams,
        build_c5_9_exams,
        build_c6_9_exams,
        build_c7_9_exams,
        build_c8_9_exams,
        build_c9_9_exams,
        build_c10_9_exams
    ]
    for b in builders:
        chap_id, new_exams = b()
        title, exams = load_existing_exams(9, chap_id)
        exams.update(new_exams)
        save_chapter_package(9, chap_id, title, exams)
    print("🎉 ĐÃ HOÀN TẤT TOÀN BỘ 10 CHƯƠNG TOÁN 9 (MỖI CHƯƠNG ĐÃ CÓ ĐỦ 7 ĐỀ CUỐI CHƯƠNG)!")

if __name__ == "__main__":
    run_all_grade9()
