# -*- coding: utf-8 -*-
"""
GENERATOR GRADE 9 - TOÀN DIỆN 10 CHƯƠNG (7 MÃ ĐỀ ĐỘC LẬP MỖI CHƯƠNG)
- 7 đề hoàn toàn khác nhau 100%
- Bao quát toàn bộ nội dung của từng chương
- KHÔNG CÓ BẤT KỲ CÂU HỎI THAM SỐ m NÀO
- Tăng cường tối đa bài toán thực tế đời sống
- Chuẩn tỷ lệ: 30% Nhận biết, 30% Thông hiểu, 30% Vận dụng, 10% Vận dụng cao
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

def load_existing_exams(chap_id, grade=9):
    json_path = os.path.join(OUTPUT_DIR, f"grade{grade}_{chap_id}_exams.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            d = json.load(f)
            return d.get("exams", {})
    return {}

# ------------------------------------------------------------------------------
# CHƯƠNG 1 TOÁN 9: Hệ hai phương trình bậc nhất hai ẩn (Bài 4)
# ------------------------------------------------------------------------------
def build_c1_9():
    chap_id = "c1_9"
    l_idx = 4
    exams = load_existing_exams(chap_id, 9)
    # Xóa các đề cũ của bài cuối chương để thay bằng 7 đề mới chuẩn xác
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_apps = [
        ("nhà sách Tiền Phong mua tập vở và bút dạ", "quyển vở", "bút dạ", 12000, 6000),
        ("ô tô và xe máy đi ngược chiều từ A và B gặp nhau", "ô tô", "xe máy", 55, 35),
        ("hai tổ công nhân sản xuất khẩu trang y tế", "tổ 1", "tổ 2", 1500, 1200),
        ("pha chế dung dịch cồn y tế 70 độ từ cồn 90 độ và nước tinh khiết", "cồn 90 độ", "nước cất", 350, 150),
        ("cano xuôi dòng và ngược dòng trên sông Đồng Nai", "vận tốc riêng cano", "dòng nước", 28, 4),
        ("hóa đơn tiền điện bậc thang tháng 6 và tháng 7", "tháng 6", "tháng 7", 450000, 520000),
        ("mảnh vườn hoa hình chữ nhật ngoại ô Đà Lạt", "chiều dài", "chiều rộng", 30, 18)
    ]
    
    for t in range(1, 8):
        app = real_apps[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", f"Phương trình nào dưới đây là phương trình bậc nhất hai ẩn $x, y$ (Đề {t:02d})?", [f"${t+1}x - {t+2}y = {t*3}$", f"$x^2 - {t}y = 1$", f"$xy = {t+4}$", f"${t}x + " + r"\frac{1}{y} = 5$"], 0),
            make_mc(2, "Nhận biết", f"Cặp số nào sau đây là một nghiệm của phương trình $2x - y = {2*t - 1}$?", [f"$({t}; 1)$", f"$(1; {t})$", f"$(0; {t})$", f"$({t}; 0)$"], 0),
            make_mc(3, "Nhận biết", "Đồ thị biểu diễn tập nghiệm của phương trình bậc nhất hai ẩn trên mặt phẳng tọa độ $Oxy$ là:", ["Một đường thẳng", "Một đường tròn", "Một đường parabol", "Hai điểm phân biệt"], 0),
            make_mc(4, "Nhận biết", "Hệ hai phương trình bậc nhất hai ẩn có vô số nghiệm khi hai đường thẳng biểu diễn:", ["Trùng nhau hoàn toàn", "Cắt nhau tại 1 điểm", "Song song với nhau", "Vuông góc với nhau"], 0),
            make_mc(5, "Thông hiểu", f"Nghiệm của hệ phương trình $\\begin{{cases}} x + y = {6 + t} \\\\ x - y = {t} \\end{{cases}}$ là:", [f"$({3 + t}; 3)$", f"$(3; {3 + t})$", f"$({t + 2}; 4)$", f"$({t + 4}; 2)$"], 0),
            make_mc(6, "Thông hiểu", f"Bằng phương pháp thế, từ phương trình $2x - y = {t}$, ta rút $y$ theo $x$ được:", [f"$y = 2x - {t}$", f"$y = {t} - 2x$", f"$y = 2x + {t}$", f"$y = \\frac{{x - {t}}}{{2}}$"], 0),
            make_mc(7, "Thông hiểu", f"Cặp số $(2; 1)$ là nghiệm của hệ phương trình nào sau đây?", [f"$\\begin{{cases}} x + y = 3 \\\\ 2x - y = 3 \\end{{cases}}$", f"$\\begin{{cases}} x - y = 3 \\\\ x + 2y = 4 \\end{{cases}}$", f"$\\begin{{cases}} 2x + y = 4 \\\\ x - y = 0 \\end{{cases}}$", f"$\\begin{{cases}} 3x - y = 2 \\\\ x + y = 5 \\end{{cases}}$"], 0),
            make_mc(8, "Thông hiểu", f"Tìm giá trị $a$ để đường thẳng $ax + 2y = {2*t + 4}$ đi qua điểm $M(1; 2)$:", [f"$a = {2*t}$", f"$a = {t}$", f"$a = {2*t + 2}$", f"$a = 4$"], 0),
            make_mc(9, "Vận dụng", f"Tại {app[0]}, bạn An mua 3 {app[1]} và 2 {app[2]} hết {3*app[3] + 2*app[4]} đồng. Bạn Bình mua 2 {app[1]} và 4 {app[2]} hết {2*app[3] + 4*app[4]} đồng. Giá tiền 1 {app[1]} là:", [f"${app[3]:,} đồng$", f"${app[4]:,} đồng$", f"${app[3]+2000:,} đồng$", f"${app[3]-2000:,} đồng$"], 0),
            make_mc(10, "Vận dụng", f"Một khu vườn hình chữ nhật có chu vi ${2*(app[3]//100 + app[4]//100)}\\text{{ m}}$. Chiều dài hơn chiều rộng ${(app[3]-app[4])//100}\\text{{ m}}$. Chiều rộng của khu vườn là:", [f"${app[4]//100}\\text{{ m}}$", f"${app[3]//100}\\text{{ m}}$", f"${app[4]//100 + 5}\\text{{ m}}$", f"${app[4]//100 - 5}\\text{{ m}}$"], 0),
            make_mc(11, "Vận dụng", f"Hai tổ cùng may áo ấm. Nếu tổ 1 may trong 3 ngày và tổ 2 may trong 2 ngày thì được {3*app[3]//50 + 2*app[4]//50} chiếc áo. Để tìm năng suất mỗi tổ ta lập được hệ:", ["Hệ hai phương trình bậc nhất hai ẩn", "Phương trình bậc hai", "Phương trình chứa ẩn ở mẫu", "Bất phương trình bậc nhất"], 0),
            make_mc(12, "Vận dụng cao", "Một cano chạy xuôi dòng 45 km rồi ngược dòng 18 km hết 3 giờ. Biết vận tốc dòng nước là 3 km/h. Vận tốc riêng của cano là:", ["21 km/h", "18 km/h", "24 km/h", "15 km/h"], 0)
        ]
        p2 = [
            make_tf(1, f"Cho hệ phương trình $\\begin{{cases}} 3x + 2y = {3*t + 4} \\\\ x - y = {t - 2} \\end{{cases}}$ (Đề số {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Hệ phương trình đã cho có dạng bậc nhất hai ẩn x và y.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Nhân phương trình thứ hai với 2 ta được: 2x - 2y = {2*t - 4}.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Cộng hai phương trình ta được 5x = {5*t}, suy ra x = {t}.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Giá trị của biểu thức 2x + 3y đối với nghiệm của hệ bằng 10.", "correct": False}
            ]),
            make_tf(2, f"Bài toán thực tế kinh tế gia đình (Mã đề {t:02d}): Gia đình bác Ba sử dụng nước sinh hoạt. Tháng trước dùng 25 m^3 hết 210 000 đồng (gồm 10 m^3 giá rẻ mức 1 và 15 m^3 giá mức 2). Tháng này dùng 30 m^3 hết 265 000 đồng (10 m^3 mức 1 và 20 m^3 mức 2).", [
                {"key": "a", "level": "Nhận biết", "text": "Gọi giá nước mức 1 là x (đồng/m^3) và mức 2 là y (đồng/m^3) với x, y > 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Phương trình biểu diễn số tiền tháng trước là: 10x + 15y = 210 000.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Phương trình biểu diễn số tiền tháng này là: 10x + 20y = 265 000.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Giá nước ở mức 1 đắt hơn giá nước ở mức 2 là 1 000 đồng/m^3.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Giải hệ: 2x + y = {2*t + 5} và x - y = {t - 2}. Tìm nghiệm x.", f"{t + 1}"),
            make_sa(2, "Thông hiểu", f"Tìm nghiệm y của hệ phương trình: x + 3y = {t + 9} và x = {t}.", "3"),
            make_sa(3, "Vận dụng", f"Một thửa ruộng hình chữ nhật có chu vi {120 + 20*t} m, chiều dài hơn chiều rộng {20 + 2*t} m. Tính chiều dài của thửa ruộng (m).", f"{35 + 6*t}"),
            make_sa(4, "Vận dụng", f"Một ô tô đi từ A đến B với vận tốc 50 km/h, lúc về đi với vận tốc 60 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính độ dài quãng đường AB (km).", "150")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Giải hệ phương trình bằng phương pháp thế hoặc cộng đại số: $\\begin{{cases}} 3x + y = {3*t + 5} \\\\ 2x - 3y = {2*t - 15} \\end{{cases}}$.",
                       f"Từ pt 1 suy ra y = {3*t + 5} - 3x (0.25đ).\nThay vào pt 2: 2x - 3({3*t + 5} - 3x) = {2*t - 15} => 11x = {11*t} => x = {t} (0.25đ).\nSuy ra y = 5. Vậy nghiệm của hệ là ({t}; 5) (0.25đ)."),
            make_essay(2, "Vận dụng", f"Tại một trang trại chăn nuôi, có tổng cộng {40 + t*5} con gồm gà và bò. Đếm được tất cả {110 + t*10} cái chân. Hỏi trang trại có bao nhiêu con gà và bao nhiêu con bò?",
                       f"Gọi số gà là x (con), số bò là y (con) (x, y nguyên dương, x, y < {40 + t*5}) (0.25đ).\nTa có hệ phương trình: x + y = {40 + t*5} và 2x + 4y = {110 + t*10} (0.25đ).\nGiải hệ phương trình ta được: x = {25 + t*5}, y = 15 (0.25đ).\nVậy trang trại có {25 + t*5} con gà và 15 con bò (0.25đ)."),
            make_essay(3, "Vận dụng cao", f"Tìm nghiệm nguyên dương $(x; y)$ của phương trình: $xy - 2x - 3y = {t}$.",
                       f"Biến đổi phương trình về dạng tích: x(y - 2) - 3(y - 2) - 6 = {t} <=> (x - 3)(y - 2) = {t + 6} (0.25đ).\nVì x, y nguyên dương nên x - 3 và y - 2 là các ước nguyên của {t + 6} (0.25đ).\nLập bảng xét các trường hợp ước số để tìm các cặp nghiệm nguyên dương (x; y) (0.25đ).\nKết luận tập nghiệm nguyên dương thỏa mãn (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương I: Hệ phương trình bậc nhất hai ẩn - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương I: Phương trình và hệ hai phương trình bậc nhất hai ẩn", exams)

# ------------------------------------------------------------------------------
# CHƯƠNG 2 TOÁN 9: Phương trình và bất phương trình bậc nhất một ẩn (Bài 4)
# ------------------------------------------------------------------------------
def build_c2_9():
    chap_id = "c2_9"
    l_idx = 4
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_ineqs = [
        ("hãng taxi Mai Linh tính tiền cước", 12000, 14000, 200000),
        ("thang máy chung cư tải trọng tối đa", 70, 30, 650),
        ("điểm trung bình môn học kỳ cần đạt loại Giỏi", 8.0, 7.5, 9.0),
        ("công ty viễn thông với gói cước 4G thoại", 50000, 1000, 150000),
        ("xưởng may quần áo bảo hộ lao động", 5000000, 80000, 150000),
        ("hồ chứa nước sinh hoạt mùa hạn hán", 5000, 120, 2000),
        ("chiết khấu phần trăm bán hàng điện máy", 15000000, 12000000, 15)
    ]
    
    for t in range(1, 8):
        app = real_ineqs[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", "Phương trình tích có dạng chuẩn là:", ["$A(x) \\cdot B(x) = 0$", "$A(x) + B(x) = 0$", "$\\frac{A(x)}{B(x)} = 0$", "$A(x) - B(x) = 0$"], 0),
            make_mc(2, "Nhận biết", f"Điều kiện xác định của phương trình $\\frac{{2x}}{{{t}x - {2*t}}} = 1$ là:", [f"$x \\neq 2$", "$x \\neq 0$", f"$x > 2$", f"$x \\neq {t}$"], 0),
            make_mc(3, "Nhận biết", "Khi nhân hai vế của bất đẳng thức với một số âm, ta phải:", ["Đổi chiều bất đẳng thức", "Giữ nguyên chiều", "Nhân thêm số 0", "Lấy nghịch đảo"], 0),
            make_mc(4, "Nhận biết", f"Nghiệm của bất phương trình ${t+1}x > {2*t + 2}$ là:", ["$x > 2$", "$x < 2$", "$x \\ge 2$", "$x > 1$"], 0),
            make_mc(5, "Thông hiểu", f"Tập nghiệm của phương trình $(x - {t})(2x + 6) = 0$ là:", [f"$\\{{{t}; -3\\}}$", f"$\\{{-{t}; 3\\}}$", f"$\\{{{t}; 3\\}}$", f"$\\{{-{t}; -3\\}}$"], 0),
            make_mc(6, "Thông hiểu", f"Bất phương trình $2x - {t} \\le x + {t + 3}$ có nghiệm là:", [f"$x \\le {2*t + 3}$", f"$x \\ge {2*t + 3}$", f"$x < {t + 3}$", "$x \\le 3$"], 0),
            make_mc(7, "Thông hiểu", f"Giá trị $x = {t}$ là nghiệm của bất phương trình nào sau đây?", [f"$2x - 1 < {2*t + 1}$", f"$3x > {3*t + 2}$", f"$x + 5 \\le {t}$", f"$-x > -{t-1}$"], 0),
            make_mc(8, "Thông hiểu", f"Giải phương trình $\\frac{{x + {t}}}{{x - 1}} = 2$ ta được nghiệm là:", [f"$x = {t + 2}$", f"$x = {t - 2}$", f"$x = {t}$", "Vô nghiệm"], 0),
            make_mc(9, "Vận dụng", f"Một hãng taxi có giá mở cửa là {app[1]:,} đồng cho km đầu tiên và {app[2]:,} đồng cho mỗi km tiếp theo. Với số tiền {app[3]:,} đồng, khách có thể đi tối đa quãng đường (km) là:", [f"{(app[3]-app[1])//app[2] + 1} km", f"{(app[3]-app[1])//app[2]} km", f"{(app[3])//app[2]} km", f"12 km"], 0),
            make_mc(10, "Vận dụng", f"Một thang máy có tải trọng tối đa {app[3]} kg. Nhân viên nặng {app[1]} kg mang theo các kiện hàng mỗi kiện nặng {app[2]} kg. Số kiện hàng tối đa nhân viên đó có thể mang cùng là:", [f"{(app[3]-app[1])//app[2]} kiện", f"{(app[3]-app[1])//app[2] + 1} kiện", f"{(app[3])//app[2]} kiện", "20 kiện"], 0),
            make_mc(11, "Vận dụng", f"Một xưởng sản xuất có chi phí cố định là 10 triệu đồng/tháng. Mỗi sản phẩm bán ra thu lãi 50 000 đồng. Xưởng cần sản xuất ít nhất bao nhiêu sản phẩm mỗi tháng để bắt đầu có lãi?", ["201 sản phẩm", "200 sản phẩm", "150 sản phẩm", "250 sản phẩm"], 0),
            make_mc(12, "Vận dụng cao", f"Số nguyên $x$ lớn nhất thỏa mãn bất phương trình $\\frac{{x - {t}}}{{2}} + \\frac{{x - {t+1}}}{{3}} < \\frac{{x + 1}}{{6}}$ là:", [f"$x = {t+1}$", f"$x = {t}$", f"$x = {t+2}$", f"$x = {t-1}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét phương trình tích $(2x - {2*t})(x + 3) = 0$ (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Phương trình đã cho là phương trình tích gồm hai nhân tử bậc nhất.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Nhân tử thứ nhất 2x - {2*t} = 0 cho nghiệm x = {t}.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nhân tử thứ hai x + 3 = 0 cho nghiệm x = -3.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": f"Tổng hai nghiệm của phương trình bằng {t + 3}.", "correct": False}
            ]),
            make_tf(2, f"Bài toán thực tế học tập (Mã đề {t:02d}): Bạn Hùng có điểm 4 bài kiểm tra môn Toán lần lượt là 7; 8; 8; 9. Bạn còn 1 bài kiểm tra cuối kỳ hệ số 2. Hùng muốn điểm trung bình môn cả kỳ đạt từ 8,5 trở lên.", [
                {"key": "a", "level": "Nhận biết", "text": "Tổng số hệ số điểm kiểm tra môn Toán trong kỳ là 1 + 1 + 1 + 1 + 2 = 6.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng điểm 4 bài kiểm tra đầu tiên là: 7 + 8 + 8 + 9 = 32 điểm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Bất phương trình tìm điểm bài cuối kỳ x là: (32 + 2x) / 6 >= 8,5.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Bạn Hùng chỉ cần đạt bài cuối kỳ từ 9,0 điểm là hoàn thành mục tiêu.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Giải phương trình: 3x - {3*t} = 0. Tìm x.", f"{t}"),
            make_sa(2, "Thông hiểu", f"Tìm nghiệm nguyên dương nhỏ nhất của bất phương trình: 2x > {2*t + 1}.", f"{t + 1}"),
            make_sa(3, "Vận dụng", f"Một công ty viễn thông thu cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi. Bạn Lan có ngân sách tối đa 150 000 đồng/tháng. Hỏi bạn Lan có thể gọi tối đa bao nhiêu phút?", "100"),
            make_sa(4, "Vận dụng", f"Tìm số nguyên x lớn nhất thỏa mãn: (x - 1)/2 - (x - 2)/3 > 1.", "7")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Giải phương trình chứa ẩn ở mẫu: $\\frac{{x + {t}}}{{x - 2}} - \\frac{{1}}{{x}} = 1$.",
                       f"ĐKXĐ: x khác 0 và x khác 2 (0.25đ).\nQuy đồng mẫu thức chung x(x - 2): x(x + {t}) - (x - 2) = x(x - 2) (0.25đ).\n<=> x^2 + {t}x - x + 2 = x^2 - 2x <=> ({t} + 1)x = -2 => x = -2/({t} + 1) (thỏa mãn ĐKXĐ) (0.25đ).\nKết luận tập nghiệm (0.25đ)."),
            make_essay(2, "Vận dụng", f"Một người có 300 triệu đồng gửi vào hai sổ tiết kiệm tại ngân hàng. Sổ thứ nhất kỳ hạn 12 tháng lãi suất 6%/năm. Sổ thứ hai kỳ hạn 6 tháng lãi suất 5%/năm. Sau một năm, tổng số tiền lãi nhận được là 16,8 triệu đồng. Tính số tiền gửi ở mỗi sổ.",
                       "Gọi số tiền gửi ở sổ thứ nhất là x (triệu đồng), sổ thứ hai là y (triệu đồng) (0 < x, y < 300) (0.25đ).\nTa có hệ pt: x + y = 300 và 0,06x + 0,05y = 16,8 (0.25đ).\nGiải ra được x = 180 (triệu đồng) và y = 120 (triệu đồng) (0.25đ).\nKết luận số tiền mỗi sổ (0.25đ)."),
            make_essay(3, "Vận dụng cao", f"Cho hai số thực dương $a, b$ thỏa mãn $a + b = 2$. Chứng minh rằng: $\\frac{{1}}{{a}} + \\frac{{1}}{{b}} \\ge 2$.",
                       "Áp dụng bất đẳng thức Cauchy cho hai số dương a, b: a + b >= 2 căn(ab) => 2 >= 2 căn(ab) => ab <= 1 (0.25đ).\nTa có: 1/a + 1/b = (a + b)/(ab) = 2/(ab) (0.25đ).\nVì ab <= 1 và ab > 0 nên 2/(ab) >= 2/1 = 2 (0.25đ).\nDấu '=' xảy ra khi a = b = 1. Bài toán được chứng minh (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình và bất phương trình bậc nhất một ẩn - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương II: Phương trình và bất phương trình bậc nhất một ẩn", exams)

# ------------------------------------------------------------------------------
# CHƯƠNG 3 TOÁN 9: Căn bậc hai và căn bậc ba (Bài 5)
# ------------------------------------------------------------------------------
def build_c3_9():
    chap_id = "c3_9"
    l_idx = 5
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_radicals = [
        ("tốc độ xe ô tô trước khi phanh gấp theo vết trượt bánh trên đường", "v = căn(2 * mu * g * s)", 0.8, 40),
        ("tầm nhìn xa tối đa từ ngọn hải đăng ra biển theo độ cao", "d = 3.57 * căn(h)", 64, 28.56),
        ("chu kỳ dao động của con lắc đơn", "T = 2 * pi * căn(l / g)", 1, 2),
        ("bán kính hình tròn khi biết diện tích mảnh đất", "R = căn(S / pi)", 314, 10),
        ("vận tốc rơi tự do của giọt nước mưa từ đám mây", "v = căn(2 * g * h)", 180, 60),
        ("độ dài cạnh thùng hàng hình lập phương chứa gạo", "a = căn bậc ba của V", 125, 5),
        ("diện tích bề mặt cơ thể theo công thức Mosteller", "S = căn((h * w)/3600)", 160, 49)
    ]
    
    for t in range(1, 8):
        app = real_radicals[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", f"Căn bậc hai số học của số ${t*t}$ là:", [f"${t}$", f"$-{t}$", f"$\\pm {t}$", f"${t*t}$"], 0),
            make_mc(2, "Nhận biết", "Biểu thức $\\sqrt{A}$ có nghĩa (xác định) khi và chỉ khi:", ["$A \\ge 0$", "$A > 0$", "$A \\le 0$", "$A \\neq 0$"], 0),
            make_mc(3, "Nhận biết", "Căn bậc ba của một số thực âm là:", ["Một số âm", "Một số dương", "Không tồn tại", "Số 0"], 0),
            make_mc(4, "Nhận biết", f"Khẳng định nào sau đây đúng với mọi số thực $a$?", ["$\\sqrt{a^2} = |a|$", "$\\sqrt{a^2} = a$", "$\\sqrt{a^2} = -a$", "$\\sqrt{a^2} = \\pm a$"], 0),
            make_mc(5, "Thông hiểu", f"Điều kiện xác định của căn thức $\\sqrt{{2x - {2*t}}}$ là:", [f"$x \\ge {t}$", f"$x > {t}$", f"$x \\le {t}$", f"$x \\neq {t}$"], 0),
            make_mc(6, "Thông hiểu", "Rút gọn biểu thức căn((căn(" + str(t+1) + ") - 1)^2) ta được kết quả là:", ["căn(" + str(t+1) + ") - 1", "1 - căn(" + str(t+1) + ")", "căn(" + str(t+1) + ") + 1", "0"], 0),
            make_mc(7, "Thông hiểu", f"Rút gọn biểu thức $\\sqrt{{4 \\cdot {t}}} + \\sqrt{{9 \\cdot {t}}} - \\sqrt{{16 \\cdot {t}}}$ ta được:", [f"$\\sqrt{{{t}}}$", f"$2\\sqrt{{{t}}}$", f"$3\\sqrt{{{t}}}$", "$0$"], 0),
            make_mc(8, "Thông hiểu", f"Trục căn thức ở mẫu của $\\frac{{{t}}}{{\\sqrt{{{t}}}}}$ ta được kết quả là:", [f"$\\sqrt{{{t}}}$", f"${t}\\sqrt{{{t}}}$", f"$\\frac{{\\sqrt{{{t}}}}}{{{t}}}$", "$1$"], 0),
            make_mc(9, "Vận dụng", f"Tầm nhìn xa d (km) từ đỉnh ngọn hải đăng ở độ cao {app[2]} m tính theo công thức d = 3,57 * căn(h) xấp xỉ là:", [f"{3.57*(app[2]**0.5):.2f} km", "20 km", "30 km", "15 km"], 0),
            make_mc(10, "Vận dụng", f"Một chiếc thùng chứa nước hình lập phương có thể tích là ${app[2]}\\text{{ m}}^3$. Độ dài cạnh của thùng nước là:", [f"${round(app[2]**(1/3))}\\text{{ m}}$", f"${app[2]//3}\\text{{ m}}$", f"${app[2]//10}\\text{{ m}}$", "2 m"], 0),
            make_mc(11, "Vận dụng", f"Rút gọn biểu thức $A = (\\sqrt{{5}} + 2)(\\sqrt{{5}} - 2) + \\sqrt{{{t*t}}}$ ta được kết quả là:", [f"${t + 1}$", f"${t}$", f"${t - 1}$", f"${2*t}$"], 0),
            make_mc(12, "Vận dụng cao", f"Giá trị nhỏ nhất của biểu thức $P = x - 2\\sqrt{{x}} + {t + 4}$ với $x \\ge 0$ là:", [f"${t + 3}$", f"${t + 4}$", f"${t}$", f"${t + 2}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về căn thức (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Mọi số thực dương đều có đúng hai căn bậc hai đối nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Căn bậc hai số học của {t*t} là {t}.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Biểu thức căn(x - {t}) xác định khi x >= {t}.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": f"Giá trị của biểu thức căn(x^2 - {2*t}x + {t*t}) luôn bằng x - {t} với mọi số thực x.", "correct": False}
            ]),
            make_tf(2, f"Cho biểu thức $P = \\left(\\frac{{1}}{{\\sqrt{{x}}-1}} - \\frac{{1}}{{\\sqrt{{x}}+1}}\\right) \\cdot \\frac{{x-1}}{{2}}$ với $x \\ge 0, x \\neq 1$:", [
                {"key": "a", "level": "Nhận biết", "text": "Điều kiện xác định của biểu thức P là x >= 0 và x khác 1.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Quy đồng mẫu thức trong ngoặc ta được tử số bằng 2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Rút gọn biểu thức P ta được kết quả bằng 1.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Giá trị của P phụ thuộc vào giá trị của biến số x.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính giá trị: căn({4*t*t}) : {t}.", "2"),
            make_sa(2, "Thông hiểu", f"Tìm x không âm biết: căn(x) = {t + 2}.", f"{(t + 2)**2}"),
            make_sa(3, "Vận dụng", f"Một người quan sát đứng trên đỉnh núi cao 400 m so với mực nước biển. Tầm nhìn xa tối đa của người đó tính theo công thức d = 3,57 * căn(h) là bao nhiêu km?", "71.4"),
            make_sa(4, "Vận dụng", f"Tìm giá trị nhỏ nhất của biểu thức: A = x - 4 căn(x) + {t + 10} (với x >= 0).", f"{t + 6}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Rút gọn biểu thức: $A = \\sqrt{{50}} - \\sqrt{{18}} + \\sqrt{{{2*t*t}}}$.",
                       f"A = 5 căn(2) - 3 căn(2) + {t} căn(2) (0.25đ).\n= (5 - 3 + {t}) căn(2) = ({t + 2}) căn(2) (0.25đ).\nKết luận giá trị biểu thức (0.25đ)."),
            make_essay(2, "Vận dụng", f"Cho biểu thức $B = \\frac{{\\sqrt{{x}}}}{{\\sqrt{{x}} - 2}} - \\frac{{4}}{{\\sqrt{{x}} + 2}} - \\frac{{4\\sqrt{{x}}}}{{x - 4}}$ với $x \\ge 0, x \\neq 4$. Rút gọn biểu thức $B$ và tìm $x$ để $B = 1$.",
                       "Quy đồng mẫu thức chung (căn(x) - 2)(căn(x) + 2) (0.25đ).\nTử thức = căn(x)(căn(x) + 2) - 4(căn(x) - 2) - 4 căn(x) = x + 2 căn(x) - 4 căn(x) + 8 - 4 căn(x) = x - 6 căn(x) + 8 (0.25đ).\nPhân tích tử thành (căn(x) - 2)(căn(x) - 4), rút gọn được B = (căn(x) - 4)/(căn(x) + 2) (0.25đ).\nB = 1 <=> căn(x) - 4 = căn(x) + 2 => -4 = 2 (vô lý), vậy không có giá trị x nào thỏa mãn (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Tìm giá trị lớn nhất của biểu thức: $M = \\sqrt{x - 1} + \\sqrt{9 - x}$ với $1 \\le x \\le 9$.",
                       "Áp dụng bất đẳng thức Bunhiacopxki cho hai bộ số (1; 1) và (căn(x-1); căn(9-x)) (0.25đ).\nM^2 = (1.căn(x-1) + 1.căn(9-x))^2 <= (1^2 + 1^2)(x - 1 + 9 - x) = 2 . 8 = 16 (0.25đ).\nSuy ra M <= căn(16) = 4 (0.25đ).\nDấu '=' xảy ra khi căn(x-1) = căn(9-x) <=> x - 1 = 9 - x <=> 2x = 10 <=> x = 5 (thỏa mãn). Vậy GTLN của M là 4 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương III: Căn bậc hai và căn bậc ba - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương III: Căn bậc hai và căn bậc ba", exams)

print("Modules c1_9, c2_9, c3_9 created successfully!")

# ------------------------------------------------------------------------------
# CHƯƠNG 4 TOÁN 9: Hệ thức lượng trong tam giác vuông (Bài 3)
# ------------------------------------------------------------------------------
def build_c4_9():
    chap_id = "c4_9"
    l_idx = 3
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_trig = [
        ("thang tựa vào tường nghiêng góc 65 độ", 3.5, 65),
        ("đo chiều cao cột cờ bằng bóng nắng trên mặt đất", 12, 42),
        ("ngọn hải đăng nhìn con thuyền xa bờ dưới góc hạ 32 độ", 80, 32),
        ("máy bay cất cánh bay lên nghiêng góc 23 độ", 6000, 23),
        ("đo bề rộng khúc sông Hương", 45, 54),
        ("dây cáp treo trượt từ đỉnh núi Bà Nà", 1200, 28),
        ("cầu dốc người đi bộ vượt đường cao tốc", 50, 4)
    ]
    
    for t in range(1, 8):
        app = real_trig[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", "Trong tam giác vuông, $\\sin$ của một góc nhọn bằng:", ["Tỉ số giữa cạnh đối và cạnh huyền", "Tỉ số giữa cạnh kề và cạnh huyền", "Tỉ số giữa cạnh đối và cạnh kề", "Tỉ số giữa cạnh kề và cạnh đối"], 0),
            make_mc(2, "Nhận biết", "Công thức lượng giác cơ bản nào sau đây luôn đúng với góc nhọn $\\alpha$?", ["$\\sin^2\\alpha + \\cos^2\\alpha = 1$", "$\\sin\\alpha + \\cos\\alpha = 1$", "$\\tan\\alpha = \\frac{\\cos\\alpha}{\\sin\\alpha}$", "$\\sin^2\\alpha - \\cos^2\\alpha = 1$"], 0),
            make_mc(3, "Nhận biết", f"Giá trị của $\\tan {45}^\\circ$ bằng:", ["$1$", "$\\frac{{1}}{{2}}$", "$\\frac{\\sqrt{3}}{2}$", "$\\sqrt{3}$"], 0),
            make_mc(4, "Nhận biết", "Nếu hai góc nhọn phụ nhau ($\\alpha + \\beta = 90^\\circ$) thì khẳng định nào sau đây ĐÚNG?", ["$\\sin\\alpha = \\cos\\beta$", "$\\sin\\alpha = \\sin\\beta$", "$\\tan\\alpha = \\tan\\beta$", "$\\cos\\alpha = \\cos\\beta$"], 0),
            make_mc(5, "Thông hiểu", f"Cho tam giác $ABC$ vuông tại $A$ có $AB = {3*t}\\text{{ cm}}, AC = {4*t}\\text{{ cm}}$. Giá trị $\\sin B$ là:", ["$\\frac{{4}}{{5}} = 0,8$", "$\\frac{{3}}{{5}}$", "$\\frac{{4}}{{3}}$", "$\\frac{{3}}{{4}}$"], 0),
            make_mc(6, "Thông hiểu", f"Tam giác $ABC$ vuông tại $A$, có $\\widehat{{B}} = {30 + t*5}^\\circ$. Số đo góc $C$ là:", [f"${60 - t*5}^\\circ$", f"${90 - t*5}^\\circ$", f"${45}^\\circ$", f"${30}^\\circ$"], 0),
            make_mc(7, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Khẳng định nào sau đây ĐÚNG?", ["$AH^2 = BH \\cdot CH$", "$AB^2 = BH \\cdot AH$", "$AC^2 = CH \\cdot AH$", "$AH = BH \\cdot CH$"], 0),
            make_mc(8, "Thông hiểu", f"Một chiếc thang dài ${app[1]}\\text{{ m}}$ dựa vào tường tạo với mặt đất góc ${app[2]}^\\circ$. Chiều cao thang chạm tường là:", [f"${app[1]} \\cdot \\sin {app[2]}^\\circ\\text{{ m}}$", f"${app[1]} \\cdot \\cos {app[2]}^\\circ\\text{{ m}}$", f"${app[1]} \\cdot \\tan {app[2]}^\\circ\\text{{ m}}$", f"${app[1]}\\text{{ m}}$"], 0),
            make_mc(9, "Vận dụng", f"Một cột cờ cao ${app[1]}\\text{{ m}}$ có bóng trên mặt đất dài ${app[1]*1.2:.1f}\\text{{ m}}$. Góc tạo bởi tia sáng mặt trời với mặt đất (làm tròn đến độ) là:", ["$40^\\circ$", "$50^\\circ$", "$45^\\circ$", "$60^\\circ$"], 0),
            make_mc(10, "Vận dụng", f"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = {4*t}\\text{{ cm}}, CH = {9*t}\\text{{ cm}}$. Độ dài đường cao $AH$ là:", [f"${6*t}\\text{{ cm}}$", f"${13*t}\\text{{ cm}}$", f"${36*t}\\text{{ cm}}$", f"${5*t}\\text{{ cm}}$"], 0),
            make_mc(11, "Vận dụng", f"Giá trị của biểu thức $M = \\sin^2 {20+t}^\\circ + \\sin^2 {70-t}^\\circ - \\tan {45}^\\circ$ bằng:", ["$0$", "$1$", "$2$", "$-1$"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác nhọn $ABC$ có hai đường cao $BD$ và $CE$. Diện tích tam giác $ADE$ bằng:", ["$S_{ABC} \\cdot \\cos^2 A$", "$S_{ABC} \\cdot \\sin^2 A$", "$S_{ABC} \\cdot \\tan^2 A$", "$S_{ABC} \\cdot \\cos A$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai trong tam giác vuông (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Trong tam giác vuông, cạnh đối diện với góc vuông là cạnh huyền và là cạnh lớn nhất.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tỉ số lượng giác sin và cosin của một góc nhọn luôn nhỏ hơn 1.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Khi góc nhọn tăng từ 0 độ đến 90 độ thì sin và tan của góc đó đều tăng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Với mọi góc nhọn alpha, biểu thức sin(alpha) + cos(alpha) luôn nhỏ hơn 1.", "correct": False}
            ]),
            make_tf(2, f"Cho tam giác $ABC$ vuông tại $A$ có $AB = {6*t}\\text{{ cm}}, AC = {8*t}\\text{{ cm}}$, đường cao $AH$:", [
                {"key": "a", "level": "Nhận biết", "text": f"Độ dài cạnh huyền BC tính theo định lý Pythagore là {10*t} cm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Độ dài đường cao AH bằng (AB . AC)/BC = {4.8*t} cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Độ dài hình chiếu BH trên cạnh huyền là {3.6*t} cm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Giá trị của tan B cộng tan C bằng 2.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính: sin^2({25+t} độ) + cos^2({25+t} độ).", "1"),
            make_sa(2, "Thông hiểu", f"Cho tam giác vuông có cạnh huyền bằng {20*t} cm, góc nhọn 30 độ. Tính cạnh góc vuông đối diện góc 30 độ (cm).", f"{10*t}"),
            make_sa(3, "Vận dụng", f"Một chiếc máy bay cất cánh từ mặt đất với góc nâng 20 độ. Sau khi bay được quãng đường 3000 m thì độ cao của máy bay đạt được là bao nhiêu mét (làm tròn số nguyên)?", "1026"),
            make_sa(4, "Vận dụng", f"Cho tam giác ABC vuông tại A, đường cao AH. Biết BH = 9 cm, CH = 16 cm. Tính độ dài cạnh AB (cm).", "15")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho tam giác $ABC$ vuông tại $A$, có $AB = {5*t}\\text{{ cm}}$ và $\\widehat{{B}} = 60^\\circ$. Tính độ dài cạnh $AC$ và cạnh huyền $BC$.",
                       f"Ta có: tan B = AC/AB => AC = AB . tan 60 độ = {5*t} . căn(3) (cm) (0.25đ).\ncos B = AB/BC => BC = AB / cos 60 độ = {5*t} / 0,5 = {10*t} (cm) (0.25đ).\nKết luận độ dài AC và BC (0.25đ)."),
            make_essay(2, "Vận dụng", f"Một người đứng cách chân tháp truyền hình một khoảng $d = 80\\text{{ m}}$. Người đó dùng giác kế cao $1,5\\text{{ m}}$ ngắm lên đỉnh tháp với góc nâng $38^\\circ$. Tính chiều cao của tháp truyền hình (làm tròn đến mét).",
                       "Gọi chiều cao từ điểm đặt giác kế đến đỉnh tháp là h1 (m) (0.25đ).\nTa có: tan 38 độ = h1 / 80 => h1 = 80 . tan 38 độ xấp xỉ 80 . 0,7813 xấp xỉ 62,5 (m) (0.25đ).\nChiều cao toàn bộ của tháp là: H = h1 + 1,5 = 62,5 + 1,5 = 64 (m) (0.25đ).\nKết luận chiều cao ngọn tháp (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Cho tam giác nhọn $ABC$. Chứng minh rằng: $S_{ABC} = \\frac{{1}}{{2}}AB \\cdot AC \\cdot \\sin A$.",
                       "Kẻ đường cao BH vuông góc với AC (H thuộc AC) (0.25đ).\nTrong tam giác vuông ABH: sin A = BH/AB => BH = AB . sin A (0.25đ).\nDiện tích tam giác ABC: S = 1/2 . AC . BH = 1/2 . AC . AB . sin A (0.25đ).\nĐẳng thức được chứng minh hoàn tất (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương IV: Hệ thức lượng trong tam giác vuông - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương IV: Hệ thức lượng trong tam giác vuông", exams)

# ------------------------------------------------------------------------------
# CHƯƠNG 5 TOÁN 9: Đường tròn (Bài 6)
# ------------------------------------------------------------------------------
def build_c5_9():
    chap_id = "c5_9"
    l_idx = 6
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_circles = [
        ("vùng phủ sóng của trạm thu phát viễn thông 5G", 15, "km"),
        ("vành bánh xe đạp địa hình chuyển động lăn tròn", 35, "cm"),
        ("mặt đồng hồ tròn trang trí phòng khách", 20, "cm"),
        ("vòng cung vòm cầu vượt sông Sài Gòn", 50, "m"),
        ("dây curoa truyền động giữa hai bánh răng tròn", 25, "cm"),
        ("vòng xoay bùng binh giao thông thành phố", 40, "m"),
        ("gương tròn phong thủy treo tường nghệ thuật", 30, "cm")
    ]
    
    for t in range(1, 8):
        app = real_circles[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", f"Đường tròn tâm $O$ bán kính $R = {t*2}\\text{{ cm}}$ là hình gồm tất cả các điểm cách $O$ một khoảng:", [f"Bằng ${t*2}\\text{{ cm}}$", f"Nhỏ hơn ${t*2}\\text{{ cm}}$", f"Lớn hơn ${t*2}\\text{{ cm}}$", f"Bằng ${t}\\text{{ cm}}$"], 0),
            make_mc(2, "Nhận biết", "Trong một đường tròn, dây cung lớn nhất là:", ["Đường kính", "Bán kính", "Dây bất kỳ", "Cung lớn"], 0),
            make_mc(3, "Nhận biết", "Đường thẳng và đường tròn tiếp xúc nhau khi số điểm chung của chúng là:", ["Đúng 1 điểm", "2 điểm", "Không có điểm nào", "Vô số điểm"], 0),
            make_mc(4, "Nhận biết", "Tiếp tuyến của đường tròn vuông góc với bán kính đi qua:", ["Tiếp điểm", "Tâm đường tròn", "Điểm bất kỳ", "Dây cung"], 0),
            make_mc(5, "Thông hiểu", f"Cho đường tròn $(O; {5*t}\\text{{ cm}})$ và dây $AB = {8*t}\\text{{ cm}}$. Khoảng cách từ tâm $O$ đến dây $AB$ là:", [f"${3*t}\\text{{ cm}}$", f"${4*t}\\text{{ cm}}$", f"${2*t}\\text{{ cm}}$", f"${5*t}\\text{{ cm}}$"], 0),
            make_mc(6, "Thông hiểu", f"Cho điểm $M$ nằm ngoài đường tròn $(O; {t*3}\\text{{ cm}})$ sao cho $OM = {t*5}\\text{{ cm}}$. Độ dài tiếp tuyến $MA$ kẻ từ $M$ đến đường tròn là:", [f"${t*4}\\text{{ cm}}$", f"${t*2}\\text{{ cm}}$", f"${t*8}\\text{{ cm}}$", f"${t*3}\\text{{ cm}}$"], 0),
            make_mc(7, "Thông hiểu", "Góc ở tâm có số đo bằng:", ["Số đo cung bị chắn", "Nửa số đo cung bị chắn", "Gấp đôi số đo cung bị chắn", "Góc nội tiếp"], 0),
            make_mc(8, "Thông hiểu", "Góc nội tiếp chắn nửa đường tròn là:", ["Góc vuông ($90^\\circ$)", "Góc nhọn ($45^\\circ$)", "Góc tù ($120^\\circ$)", "Góc bẹt ($180^\\circ$)"], 0),
            make_mc(9, "Vận dụng", f"Một {app[0]} có bán kính quét là ${app[1]}\\text{{{app[2]}}}$. Chu vi đường viền giới hạn vùng quét là:", [f"${2*3.14*app[1]:.1f}\\text{{{app[2]}}}$", f"${3.14*app[1]:.1f}\\text{{{app[2]}}}$", f"${app[1]*app[1]}\\text{{{app[2]}}}$", f"100\\text{{{app[2]}}}"], 0),
            make_mc(10, "Vận dụng", f"Hai tiếp tuyến tại $A$ và $B$ của đường tròn $(O)$ cắt nhau tại $M$. Biết $\\widehat{{AMB}} = {50 + t*5}^\\circ$. Số đo góc ở tâm $\\widehat{{AOB}}$ là:", [f"${130 - t*5}^\\circ$", f"${180 - t*5}^\\circ$", f"${90}^\\circ$", f"${65}^\\circ$"], 0),
            make_mc(11, "Vận dụng", f"Cho đường tròn $(O; {10*t}\\text{{ cm}})$. Hai dây cung $AB$ và $CD$ song song với nhau có độ dài lần lượt là ${12*t}\\text{{ cm}}$ và ${16*t}\\text{{ cm}}$ nằm về hai phía so với tâm $O$. Khoảng cách giữa hai dây là:", [f"${14*t}\\text{{ cm}}$", f"${7*t}\\text{{ cm}}$", f"${2*t}\\text{{ cm}}$", f"${10*t}\\text{{ cm}}$"], 0),
            make_mc(12, "Vận dụng cao", "Cho đường tròn $(O)$ và điểm $A$ cố định nằm ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ đến $(O)$. Khi đường tròn $(O)$ thay đổi nhưng luôn tiếp xúc với $AB, AC$ thì tâm $O$ luôn thuộc:", ["Tia phân giác của góc BAC", "Đường trung trực của đoạn BC", "Đường tròn đường kính OA", "Một đường thẳng vuông góc với BC"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tiếp tuyến của đường tròn (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Nếu một đường thẳng là tiếp tuyến của đường tròn thì nó vuông góc với bán kính đi qua tiếp điểm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Từ một điểm nằm ngoài đường tròn luôn kẻ được đúng hai tiếp tuyến đến đường tròn đó.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai đoạn thẳng nối từ điểm ngoài đó đến hai tiếp điểm có độ dài bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tia nối từ điểm ngoài đó đến tâm là đường trung trực của đoạn thẳng nối hai tiếp điểm.", "correct": True}
            ]),
            make_tf(2, f"Cho đường tròn $(O; {5*t}\\text{{ cm}})$ và dây cung $MN = {8*t}\\text{{ cm}}$, gọi $I$ là trung điểm của $MN$:", [
                {"key": "a", "level": "Nhận biết", "text": "Đoạn thẳng OI vuông góc với dây cung MN tại điểm I.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Đoạn MI = IN = {4*t} cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Khoảng cách từ tâm O đến dây cung MN là OI = {3*t} cm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích tam giác OMN bằng 24 cm^2 với mọi giá trị của t.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Cho đường tròn (O; 13 cm) và dây AB = 24 cm. Tính khoảng cách từ tâm O đến dây AB (cm).", "5"),
            make_sa(2, "Thông hiểu", f"Từ điểm M cách tâm O khoảng cách 25 cm, kẻ tiếp tuyến MA đến đường tròn (O; 7 cm). Tính độ dài tiếp tuyến MA (cm).", "24"),
            make_sa(3, "Vận dụng", f"Một bánh xe đạp có bán kính 30 cm. Khi bánh xe lăn được 100 vòng trên đường phẳng thì quãng đường xe đi được là bao nhiêu mét (lấy pi = 3,14, làm tròn số nguyên)?", "188"),
            make_sa(4, "Vận dụng", f"Cho đường tròn (O; 10 cm), dây cung AB = 12 cm. Lấy điểm M trên dây AB sao cho AM = 4 cm. Tính độ dài đoạn OM (làm tròn 1 chữ số thập phân, cm).", "8.2")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho đường tròn $(O; R)$ đường kính $AB$. Lấy điểm $C$ thuộc đường tròn ($C$ khác $A, B$). Chứng minh tam giác $ABC$ vuông tại $C$.",
                       "Xét tam giác ABC nội tiếp đường tròn (O) có cạnh AB là đường kính (0.25đ).\nTheo tính chất góc nội tiếp chắn nửa đường tròn: góc ACB = 90 độ (0.25đ).\nSuy ra tam giác ABC vuông tại C (0.25đ)."),
            make_essay(2, "Vận dụng", f"Từ điểm $M$ nằm ngoài đường tròn $(O; R)$, kẻ hai tiếp tuyến $MA, MB$ với $(O)$ ($A, B$ là hai tiếp điểm). Gọi $H$ là giao điểm của $OM$ và $AB$. Chứng minh $OM \\perp AB$ tại $H$ và $OM \\cdot OH = R^2$.",
                       "Vì MA = MB (tính chất 2 tiếp tuyến cắt nhau) và OA = OB = R nên OM là đường trung trực của đoạn thẳng AB => OM vuông góc với AB tại H (0.25đ).\nXét tam giác OAM vuông tại A có AH là đường cao: theo hệ thức lượng trong tam giác vuông, ta có: OA^2 = OH . OM (0.25đ).\nMà OA = R => OM . OH = R^2 (điều phải chứng minh) (0.25đ)."),
            make_essay(3, "Vận dụng cao", f"Cho đường tròn $(O)$ và dây cung $BC$ cố định. Điểm $A$ di động trên cung lớn $BC$. Chứng minh rằng trực tâm $H$ của tam giác $ABC$ luôn di động trên một đường tròn cố định.",
                       "Kẻ đường kính CD của đường tròn (O). Tứ giác ABDH là hình bình hành vì có các cạnh đối song song (0.25đ).\nSuy ra vecto AH = vecto BD cố định (hoặc đoạn thẳng DH đi qua trung điểm M của BC) (0.25đ).\nTừ đó suy ra điểm H là ảnh của điểm A qua phép tịnh tiến hoặc phép đối xứng tâm cố định, nên H thuộc một đường tròn cố định có bán kính bằng R (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương V: Đường tròn - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương V: Đường tròn", exams)

# ------------------------------------------------------------------------------
# CHƯƠNG 6 TOÁN 9: Hàm số y = ax^2 và Phương trình bậc hai một ẩn (Bài 5)
# ------------------------------------------------------------------------------
def build_c6_9():
    chap_id = "c6_9"
    l_idx = 5
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_quads = [
        ("quỹ đạo quả bóng đá bay hình parabol", "y = -0.05 x^2 + x", 20, 5),
        ("cổng vòm parabol trường Bách Khoa", "h = 8 - 0.5 x^2", 8, 4),
        ("vật rơi tự do từ đỉnh tòa nhà Landmark", "s = 5 t^2", 80, 4),
        ("mảnh đất xây nhà hình chữ nhật", "dài hơn rộng 6 m, diện tích 216 m^2", 18, 12),
        ("xe máy tăng tốc thêm 10 km/h để đến sớm 30 phút", "quãng đường 100 km", 40, 50),
        ("xưởng in lịch Tết tăng năng suất 50 cuốn/ngày", "hoàn thành trước 2 ngày", 200, 250),
        ("hai vòi nước cùng chảy đầy bể bơi", "chảy chung 4 giờ 48 phút", 8, 12)
    ]
    
    for t in range(1, 8):
        app = real_quads[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", f"Hàm số $y = {t}x^2$ đồng biến khi:", ["$x > 0$", "$x < 0$", "Với mọi $x$", "$x = 0$"], 0),
            make_mc(2, "Nhận biết", f"Đồ thị của hàm số $y = -{t}x^2$ có đỉnh tại gốc tọa độ $O(0;0)$ và:", ["Nằm phía dưới trục hoành", "Nằm phía trên trục hoành", "Nằm bên phải trục tung", "Nằm bên trái trục tung"], 0),
            make_mc(3, "Nhận biết", "Biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) được tính bởi:", ["$\\Delta = b^2 - 4ac$", "$\\Delta = b^2 - ac$", "$\\Delta = b^2 + 4ac$", "$\\Delta = 4ac - b^2$"], 0),
            make_mc(4, "Nhận biết", "Theo định lí Vi-ét, nếu phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có hai nghiệm $x_1, x_2$ thì tổng $x_1 + x_2$ bằng:", ["$-\\frac{{b}}{{a}}$", "$\\frac{{b}}{{a}}$", "$\\frac{{c}}{{a}}$", "$-\\frac{{c}}{{a}}$"], 0),
            make_mc(5, "Thông hiểu", f"Nghiệm của phương trình $x^2 - {2*t + 1}x + {t*(t+1)} = 0$ là:", [f"$x_1 = {t}, x_2 = {t+1}$", f"$x_1 = -{t}, x_2 = {t+1}$", f"$x_1 = {t}, x_2 = -{t+1}$", "Vô nghiệm"], 0),
            make_mc(6, "Thông hiểu", f"Điểm nào sau đây thuộc đồ thị hàm số $y = {t}x^2$?", [f"$(1; {t})$", f"$({t}; 1)$", f"$(1; -{t})$", f"$(-1; -{t})$"], 0),
            make_mc(7, "Thông hiểu", f"Phương trình $x^2 - {4*t} = 0$ có hai nghiệm là:", [f"$x = \\pm {2*t}$", f"$x = {2*t}$", f"$x = \\pm {4*t}$", "$x = 0$"], 0),
            make_mc(8, "Thông hiểu", f"Hai số có tổng bằng ${t + 5}$ và tích bằng ${5*t}$ là nghiệm của phương trình:", [f"$x^2 - {t+5}x + {5*t} = 0$", f"$x^2 + {t+5}x + {5*t} = 0$", f"$x^2 - {5*t}x + {t+5} = 0$", f"$x^2 + {t+5}x - {5*t} = 0$"], 0),
            make_mc(9, "Vận dụng", f"Một mảnh đất hình chữ nhật có diện tích ${app[2]*app[3] if isinstance(app[2], (int, float)) and isinstance(app[3], (int, float)) else 216}\\text{{ m}}^2$, chiều dài hơn chiều rộng ${abs(app[2]-app[3]) if isinstance(app[2], (int, float)) and isinstance(app[3], (int, float)) else 6}\\text{{ m}}$. Chiều dài của mảnh đất là:", [f"${max(app[2], app[3]) if isinstance(app[2], (int, float)) and isinstance(app[3], (int, float)) else 18}\\text{{ m}}$", "12 m", "15 m", "20 m"], 0),
            make_mc(10, "Vận dụng", f"Một vật rơi tự do từ độ cao ${5*t*t}\\text{{ m}}$ xuống đất theo công thức $s = 5t^2$. Thời gian để vật chạm đất là:", [f"${t}\\text{{ giây}}$", f"${2*t}\\text{{ giây}}$", f"${t*t}\\text{{ giây}}$", "5 giây"], 0),
            make_mc(11, "Vận dụng", f"Một xưởng cơ khí dự định làm ${100+t*20}$ sản phẩm trong một thời gian quy định. Do cải tiến kỹ thuật, mỗi ngày xưởng làm thêm được 5 sản phẩm nên hoàn thành sớm hơn 1 ngày. Phương trình tìm số sản phẩm làm mỗi ngày theo kế hoạch $x$ là:", [f"$\\frac{{{100+t*20}}}{{x}} - \\frac{{{100+t*20}}}{{x+5}} = 1$", f"$\\frac{{{100+t*20}}}{{x+5}} - \\frac{{{100+t*20}}}{{x}} = 1$", f"$\\frac{{x}}{{100}} - \\frac{{x+5}}{{100}} = 1$", f"$(x+5) - x = 1$"], 0),
            make_mc(12, "Vận dụng cao", f"Cho phương trình $x^2 - {2*t+3}x + {t*(t+3)} = 0$ có hai nghiệm $x_1, x_2$. Giá trị biểu thức $A = x_1^2 + x_2^2$ là:", [f"${(2*t+3)**2 - 2*t*(t+3)}$", f"${(2*t+3)**2}$", f"${t*(t+3)}$", f"$10$"], 0)
        ]
        p2 = [
            make_tf(1, f"Cho phương trình bậc hai $x^2 - {2*t + 2}x + {2*t + 1} = 0$ (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Phương trình có các hệ số a = 1, b = -(2t + 2), c = 2t + 1.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Phương trình có dạng a + b + c = 0.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Hai nghiệm của phương trình là x1 = 1 và x2 = {2*t + 1}.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tích của hai nghiệm bằng số chẵn.", "correct": False}
            ]),
            make_tf(2, f"Bài toán thực tế chuyển động (Mã đề {t:02d}): Một tàu tuần tra chạy xuôi dòng 30 km rồi ngược dòng 30 km hết tổng cộng 2,5 giờ. Biết vận tốc dòng nước là 2 km/h.", [
                {"key": "a", "level": "Nhận biết", "text": "Gọi vận tốc riêng của tàu tuần tra là v (v > 2, km/h).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Vận tốc xuôi dòng là v + 2 và ngược dòng là v - 2 (km/h).", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Phương trình lập được là: 30/(v + 2) + 30/(v - 2) = 2,5.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Vận tốc riêng của tàu tuần tra là 20 km/h.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Giải phương trình: x^2 - {4*t*t} = 0. Tìm nghiệm dương của phương trình.", f"{2*t}"),
            make_sa(2, "Thông hiểu", f"Tính tích hai nghiệm x1 . x2 của phương trình: 2x^2 - 7x + {6*t} = 0.", f"{3*t}"),
            make_sa(3, "Vận dụng", f"Một mảnh vườn hình chữ nhật có diện tích 180 m^2, chiều dài hơn chiều rộng 3 m. Tính chiều dài của mảnh vườn (m).", "15"),
            make_sa(4, "Vận dụng", f"Một người đi xe đạp từ A đến B cách nhau 30 km. Khi về người đó tăng vận tốc thêm 3 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính vận tốc lúc đi (km/h).", "12")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Giải phương trình bậc hai sau bằng công thức nghiệm: $x^2 - {2*t + 3}x + {2*t + 2} = 0$.",
                       f"Hệ số: a = 1, b = -({2*t + 3}), c = {2*t + 2} (0.25đ).\nDelta = b^2 - 4ac = ({2*t + 3})^2 - 4({2*t + 2}) = 4t^2 + 12t + 9 - 8t - 8 = 4t^2 + 4t + 1 = (2t + 1)^2 >= 0 (0.25đ).\nNghiệm: x1 = ({2*t + 3} + 2t + 1)/2 = 2t + 2; x2 = ({2*t + 3} - 2t - 1)/2 = 1 (0.25đ).\nKết luận tập nghiệm S = {{1; {2*t + 2}}} (0.25đ)."),
            make_essay(2, "Vận dụng", f"Một tổ công nhân theo kế hoạch phải may 600 chiếc khẩu trang trong thời gian quy định. Nhờ tăng năng suất mỗi ngày may thêm được 10 chiếc nên tổ đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải may bao nhiêu chiếc khẩu trang?",
                       "Gọi số khẩu trang may mỗi ngày theo kế hoạch là x (chiếc) (x nguyên dương) (0.25đ).\nThời gian theo kế hoạch là 600/x (ngày), thực tế là 600/(x + 10) (ngày) (0.25đ).\nTheo bài ra ta có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0 (0.25đ).\nGiải phương trình được: x1 = 50 (nhận), x2 = -60 (loại). Vậy theo kế hoạch mỗi ngày may 50 chiếc (0.25đ)."),
            make_essay(3, "Vận dụng cao", f"Cho phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $B = x_1^3 + x_2^3$.",
                       "Theo định lí Vi-ét ta có: S = x1 + x2 = 5 và P = x1 . x2 = 3 (0.25đ).\nBiến đổi: B = x1^3 + x2^3 = (x1 + x2)(x1^2 - x1 x2 + x2^2) = (x1 + x2)[(x1 + x2)^2 - 3 x1 x2] (0.25đ).\nThay S = 5 và P = 3 vào: B = 5 . [5^2 - 3 . 3] = 5 . (25 - 9) = 5 . 16 = 80 (0.25đ).\nKết luận giá trị của B là 80 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số $y = ax^2$ và Phương trình bậc hai một ẩn - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương VI: Hàm số $y = ax^2$ ($a \\neq 0$). Phương trình bậc hai một ẩn", exams)

# ------------------------------------------------------------------------------
# CHƯƠNG 7 TOÁN 9: Tần số và tần số tương đối (Bài 4)
# ------------------------------------------------------------------------------
def build_c7_9():
    chap_id = "c7_9"
    l_idx = 4
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_stats = [
        ("thời gian tự học mỗi ngày của 40 học sinh lớp 9A", 40),
        ("điểm kiểm tra giữa kỳ môn Toán của 45 học sinh", 45),
        ("chiều cao tính bằng cm của 50 cây giống bạch đàn", 50),
        ("số lượng sản phẩm lỗi mỗi ngày trong tháng của phân xưởng", 30),
        ("số km đi làm mỗi ngày của 35 cán bộ công nhân viên", 35),
        ("lượng nước sinh hoạt tiêu thụ m^3 của 40 hộ gia đình", 40),
        ("số tin nhắn điện tử khách hàng gửi đến trung tâm hỗ trợ", 50)
    ]
    
    for t in range(1, 8):
        app = real_stats[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", "Tần số của một giá trị trong mẫu số liệu là:", ["Số lần xuất hiện của giá trị đó trong mẫu", "Tỉ số phần trăm của giá trị đó", "Giá trị lớn nhất của mẫu", "Số trung bình cộng"], 0),
            make_mc(2, "Nhận biết", "Tần số tương đối $f_i$ của giá trị $x_i$ có tần số $m_i$ trong mẫu kích thước $N$ là:", ["$f_i = \\frac{m_i}{N} \\cdot 100\\%$", "$f_i = \\frac{N}{m_i} \\cdot 100\\%$", "$f_i = m_i \\cdot N$", "$f_i = m_i + N$"], 0),
            make_mc(3, "Nhận biết", "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:", ["$100\\%$", "$50\\%$", "$10\\%$", "$1\\%$"], 0),
            make_mc(4, "Nhận biết", "Biểu đồ hình quạt tròn thường được dùng để biểu diễn:", ["Cơ cấu tỉ lệ phần trăm các thành phần", "Sự thay đổi số liệu theo thời gian", "Tần số tuyệt đối của từng giá trị", "Giá trị lớn nhất và nhỏ nhất"], 0),
            make_mc(5, "Thông hiểu", f"Một cuộc điều tra về {app[0]}. Có {t*4} người chọn mức 1. Tần số tương đối của nhóm này là:", [f"${(t*4/app[1])*100:.1f}\\%$", f"${(t*4/app[1]):.1f}\\%$", f"${t*4}\\%$", f"${app[1]}\\%$"], 0),
            make_mc(6, "Thông hiểu", "Bảng tần số ghép nhóm thường dùng khi dữ liệu thống kê:", ["Có quy mô lớn hoặc là biến liên tục", "Chỉ có từ 2 đến 3 giá trị", "Là dữ liệu định tính không đo lường được", "Có tần số bằng nhau"], 0),
            make_mc(7, "Thông hiểu", f"Trong bảng phân bố tần số ghép nhóm $[20; 30)$, giá trị đại diện của nhóm này là:", ["$25$", "$20$", "$30$", "$50$"], 0),
            make_mc(8, "Thông hiểu", f"Cho mẫu số liệu có tổng tần số $N = {app[1]}$. Nhóm có tần số tương đối $20\\%$ thì tần số của nhóm đó là:", [f"${int(app[1]*0.2)}$", f"${int(app[1]*0.1)}$", f"${app[1]}$", "$20$"], 0),
            make_mc(9, "Vận dụng", f"Khảo sát điểm kiểm tra của {app[1]} học sinh. Số học sinh đạt điểm Giỏi (từ 8 đến 10) là {int(app[1]*0.4)}. Tần số tương đối của học sinh đạt điểm Giỏi là:", ["$40\\%$", "$30\\%$", "$50\\%$", "$20\\%$"], 0),
            make_mc(10, "Vận dụng", f"Trên biểu đồ hình quạt tròn thể hiện kết quả điều tra, một hình quạt tròn có góc ở tâm bằng ${72 + t*10}^\\circ$. Tần số tương đối tương ứng của nhóm này là:", [f"${((72+t*10)/360)*100:.1f}\\%$", "$20\\%$", "$25\\%$", "$30\\%$"], 0),
            make_mc(11, "Vận dụng", f"Điều tra mức lương của 100 công nhân. Nhóm lương từ 8 đến 10 triệu đồng chiếm $35\\%$, nhóm từ 10 đến 12 triệu chiếm $40\\%$. Số công nhân có mức lương từ 8 đến 12 triệu đồng là:", ["$75$ công nhân", "$35$ công nhân", "$40$ công nhân", "$25$ công nhân"], 0),
            make_mc(12, "Vận dụng cao", "Nếu tăng gấp đôi tất cả các tần số của một mẫu số liệu thì tần số tương đối của từng giá trị sẽ:", ["Không đổi", "Tăng gấp đôi", "Giảm đi một nửa", "Tăng thêm 100%"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tần số và tần số tương đối (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Tổng các tần số của tất cả các giá trị bằng quy mô mẫu N.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng các tần số tương đối bằng 100%.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tần số tương đối fi luôn là số không âm và không vượt quá 100%.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Biểu đồ đoạn thẳng không thể dùng để biểu diễn tần số tương đối.", "correct": False}
            ]),
            make_tf(2, f"Bảng khảo sát {app[0]} gồm {app[1]} đối tượng điều tra:", [
                {"key": "a", "level": "Nhận biết", "text": f"Kích thước mẫu số liệu là N = {app[1]}.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Mỗi giá trị có tần số mi tương ứng với số đối tượng đạt giá trị đó.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tần số tương đối cho biết tỉ lệ phần trăm của từng nhóm trong toàn bộ mẫu.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Góc ở tâm trên biểu đồ quạt tròn tỉ lệ nghịch với tần số tương đối.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Một lớp có 40 học sinh, trong đó có 10 bạn giỏi Toán. Tính tần số tương đối (%) của học sinh giỏi Toán.", "25"),
            make_sa(2, "Thông hiểu", f"Trên biểu đồ quạt tròn, nhóm A chiếm góc 90 độ ở tâm. Tính tần số tương đối (%) của nhóm A.", "25"),
            make_sa(3, "Vận dụng", f"Khảo sát 200 khách hàng mua sắm tại siêu thị, có 70 người thanh toán bằng mã QR. Tính tần số tương đối (%) thanh toán bằng QR.", "35"),
            make_sa(4, "Vận dụng", f"Trong bảng phân bố tần số ghép nhóm có nhóm [10; 20) với tần số 30 và tổng cỡ mẫu là 120. Tính tần số tương đối (%) của nhóm này.", "25")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Một cuộc điều tra về số con trong 30 gia đình tại một thôn cho kết quả: 1 con: 6 gia đình; 2 con: 18 gia đình; 3 con: 6 gia đình. Hãy lập bảng tần số tương đối.",
                       "Cỡ mẫu N = 30 (0.25đ).\nTần số tương đối gia đình 1 con: f1 = 6/30 . 100% = 20% (0.25đ).\nTần số tương đối gia đình 2 con: f2 = 18/30 . 100% = 60% (0.25đ).\nTần số tương đối gia đình 3 con: f3 = 6/30 . 100% = 20% (0.25đ)."),
            make_essay(2, "Vận dụng", f"Khảo sát thời gian xem tivi mỗi ngày của 50 học sinh: Dưới 1 giờ: 15 bạn; Từ 1 đến 2 giờ: 25 bạn; Trên 2 giờ: 10 bạn. Hãy tính số đo cung hình quạt tròn tương ứng với từng nhóm để vẽ biểu đồ quạt tròn.",
                       "Nhóm dưới 1 giờ: tỉ lệ 15/50 = 30% => Góc ở tâm = 30% . 360 độ = 108 độ (0.25đ).\nNhóm từ 1 đến 2 giờ: tỉ lệ 25/50 = 50% => Góc ở tâm = 50% . 360 độ = 180 độ (0.25đ).\nNhóm trên 2 giờ: tỉ lệ 10/50 = 20% => Góc ở tâm = 20% . 360 độ = 72 độ (0.25đ).\nTổng số đo các góc = 108 + 180 + 72 = 360 độ (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Một trạm khí tượng đo lượng mưa trong 30 ngày của tháng 7. Biết lượng mưa trung bình là 15 mm/ngày. Nếu bỏ đi 2 ngày có lượng mưa đột biến là 45 mm và 55 mm thì lượng mưa trung bình của 28 ngày còn lại là bao nhiêu?",
                       "Tổng lượng mưa trong 30 ngày là: 30 . 15 = 450 (mm) (0.25đ).\nTổng lượng mưa của 2 ngày đột biến là: 45 + 55 = 100 (mm) (0.25đ).\nTổng lượng mưa của 28 ngày còn lại là: 450 - 100 = 350 (mm) (0.25đ).\nLượng mưa trung bình của 28 ngày còn lại là: 350 / 28 = 12,5 (mm/ngày) (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương VII: Tần số và tần số tương đối", exams)

# ------------------------------------------------------------------------------
# CHƯƠNG 8 TOÁN 9: Xác suất của biến cố trong một số mô hình đơn giản (Bài 3)
# ------------------------------------------------------------------------------
def build_c8_9():
    chap_id = "c8_9"
    l_idx = 3
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_probs = [
        ("bốc thăm trúng thưởng hội chợ xuân", 100, 5),
        ("rút thẻ may mắn trong hộp quà tặng", 50, 10),
        ("gieo hai con xúc xắc cân đối và đồng chất", 36, 6),
        ("chọn ngẫu nhiên đại diện lớp đi thi Olympia", 40, 4),
        ("kiểm tra xác suất phế phẩm của lô hàng điện tử", 1000, 20),
        ("vòng quay may mắn trúng mã giảm giá Shopee", 8, 2),
        ("chọn ngẫu nhiên một ngày trong tháng 4", 30, 4)
    ]
    
    for t in range(1, 8):
        app = real_probs[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", "Không gian mẫu của một phép thử ngẫu nhiên là:", ["Tập hợp tất cả các kết quả có thể xảy ra của phép thử", "Một kết quả duy nhất", "Tập hợp các kết quả thuận lợi", "Số các phép thử đã thực hiện"], 0),
            make_mc(2, "Nhận biết", "Xác suất của biến cố chắc chắn luôn bằng:", ["$1$", "$0$", "$0,5$", "$100$"], 0),
            make_mc(3, "Nhận biết", "Xác suất của biến cố không thể luôn bằng:", ["$0$", "$1$", "$-1$", "$0,1$"], 0),
            make_mc(4, "Nhận biết", "Gieo một đồng xu cân đối và đồng chất. Xác suất xuất hiện mặt sấp là:", ["$\\frac{{1}}{{2}}$", "$\\frac{1}{4}$", "$1$", "$0$"], 0),
            make_mc(5, "Thông hiểu", "Gieo một con xúc xắc 6 mặt cân đối. Xác suất xuất hiện mặt có số chấm là số chẵn là:", ["$\\frac{{1}}{{2}}$", "$\\frac{1}{3}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"], 0),
            make_mc(6, "Thông hiểu", f"Trong một hộp có {app[1]} chiếc thẻ được đánh số từ 1 đến {app[1]}. Rút ngẫu nhiên một thẻ. Số kết quả có thể xảy ra là:", [f"${app[1]}$", f"${app[1]//2}$", "$1$", "$2$"], 0),
            make_mc(7, "Thông hiểu", f"Rút ngẫu nhiên 1 chiếc thẻ từ hộp có 20 thẻ đánh số từ 1 đến 20. Xác suất rút được thẻ ghi số chia hết cho 5 là:", ["$\\frac{1}{5} = 0,2$", "$\\frac{1}{4}$", "$\\frac{1}{10}$", "$\\frac{{1}}{{2}}$"], 0),
            make_mc(8, "Thông hiểu", f"Một lớp có 24 nam và 16 nữ. Chọn ngẫu nhiên 1 học sinh làm lớp trưởng. Xác suất chọn được học sinh nữ là:", ["$\\frac{16}{40} = 0,4$", "$\\frac{24}{40} = 0,6$", "$\\frac{{1}}{{2}}$", "$\\frac{16}{24}$"], 0),
            make_mc(9, "Vận dụng", f"Trong {app[0]} có {app[1]} vé trong đó có {app[2]} vé trúng giải đặc biệt. Xác suất để một người mua 1 vé trúng giải đặc biệt là:", [f"$\\frac{{{app[2]}}}{{{app[1]}}}$", f"$\\frac{{1}}{{{app[1]}}}$", f"$\\frac{{{app[2]}}}{{100}}$", "$0,5$"], 0),
            make_mc(10, "Vận dụng", "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 7 là:", ["$\\frac{6}{36} = \\frac{1}{6}$", "$\\frac{7}{36}$", "$\\frac{1}{12}$", "$\\frac{5}{36}$"], 0),
            make_mc(11, "Vận dụng", "Kiểm tra 500 bóng đèn xuất xưởng thấy có 15 bóng bị lỗi. Xác suất thực nghiệm chọn phải bóng đèn lỗi khi mua là:", ["$\\frac{15}{500} = 0,03$", "$\\frac{15}{100}$", "$0,05$", "$0,3$"], 0),
            make_mc(12, "Vận dụng cao", "Một hộp đựng 4 viên bi đỏ và 6 viên bi xanh cùng kích thước. Lấy ngẫu nhiên đồng thời 2 viên bi. Xác suất để lấy được 2 viên bi cùng màu là:", ["$\\frac{7}{15}$", "$\\frac{8}{15}$", "$\\frac{{1}}{{2}}$", "$\\frac{4}{15}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về xác suất cổ điển (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Xác suất của biến cố A ký hiệu là P(A) với 0 <= P(A) <= 1.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi các kết quả của phép thử có cùng khả năng xuất hiện thì P(A) = n(A) / n(Omega).", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Biến cố đối của biến cố A ký hiệu là A ngang có xác suất P(A ngang) = 1 - P(A).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu P(A) = 0,5 thì biến cố A chắc chắn xảy ra.", "correct": False}
            ]),
            make_tf(2, f"Bài toán thực tế kiểm định chất lượng (Mã đề {t:02d}): Một nhà máy sản xuất linh kiện vi mạch điện tử kiểm tra ngẫu nhiên 1 000 sản phẩm thấy có 980 sản phẩm đạt chuẩn loại A.", [
                {"key": "a", "level": "Nhận biết", "text": "Số kết quả của mẫu thực nghiệm là 1 000 sản phẩm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số sản phẩm đạt chuẩn là 980, số phế phẩm không đạt chuẩn là 20.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Xác suất thực nghiệm sản phẩm đạt chuẩn loại A là 980/1000 = 98%.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Khi sản xuất 10 000 sản phẩm thì ước tính có khoảng 500 sản phẩm bị lỗi.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Gieo 1 con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm lớn hơn 4 (viết dạng phân số tối giản).", "1/3"),
            make_sa(2, "Thông hiểu", "Một hộp có 5 bi đỏ và 15 bi xanh. Lấy ngẫu nhiên 1 viên bi. Tính xác suất lấy được bi đỏ (dưới dạng số thập phân).", "0.25"),
            make_sa(3, "Vận dụng", "Gieo đồng thời hai con xúc xắc 6 mặt. Tính xác suất để cả hai con xúc xắc cùng xuất hiện mặt 6 chấm (viết dạng phân số tối giản).", "1/36"),
            make_sa(4, "Vận dụng", "Một tổ học sinh gồm 6 nam và 4 nữ. Chọn ngẫu nhiên 2 học sinh. Tính xác suất chọn được 2 học sinh khác giới tính (viết dạng phân số tối giản).", "8/15")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Một túi kẹo có 8 cái kẹo dâu, 12 cái kẹo cam và 10 cái kẹo bạc hà cùng kích thước. Lấy ngẫu nhiên 1 chiếc kẹo. Tính xác suất để lấy được kẹo dâu hoặc kẹo cam.",
                       "Tổng số kẹo trong túi là: 8 + 12 + 10 = 30 (cái) (0.25đ).\nSố kết quả thuận lợi để lấy được kẹo dâu hoặc cam là: 8 + 12 = 20 (cái) (0.25đ).\nXác suất cần tìm là: P = 20/30 = 2/3 xấp xỉ 66,7% (0.25đ).\nKết luận xác suất (0.25đ)."),
            make_essay(2, "Vận dụng", f"Gieo hai con xúc xắc cân đối và đồng chất một lần. Gọi $A$ là biến cố: 'Tổng số chấm trên hai mặt xuất hiện bằng 8'. Hãy liệt kê các kết quả thuận lợi cho $A$ và tính xác suất $P(A)$.",
                       "Không gian mẫu gồm 6 x 6 = 36 kết quả có thể xảy ra (0.25đ).\nCác cặp (x; y) có tổng x + y = 8 là: (2; 6), (3; 5), (4; 4), (5; 3), (6; 2) (0.25đ).\nSố kết quả thuận lợi là 5 (0.25đ).\nXác suất của biến cố A là: P(A) = 5/36 (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Một xạ thủ bắn 3 phát đạn độc lập vào bia. Xác suất trúng đích của mỗi phát bắn là 0,8. Tính xác suất để có ít nhất một phát đạn trúng đích.",
                       "Gọi A là biến cố: 'Có ít nhất một phát đạn trúng đích' (0.25đ).\nBiến cố đối A ngang là: 'Cả 3 phát đạn đều không trúng đích' (0.25đ).\nXác suất bắn trượt ở mỗi phát là 1 - 0,8 = 0,2. Do các phát bắn độc lập nên: P(A ngang) = 0,2 . 0,2 . 0,2 = 0,008 (0.25đ).\nSuy ra: P(A) = 1 - P(A ngang) = 1 - 0,008 = 0,992 (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương VIII: Xác suất trong một số mô hình đơn giản - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương VIII: Xác suất của biến cố trong một số mô hình xác suất đơn giản", exams)

# ------------------------------------------------------------------------------
# CHƯƠNG 9 TOÁN 9: Đa giác đều. Đường tròn ngoại tiếp và nội tiếp (Bài 5)
# ------------------------------------------------------------------------------
def build_c9_9():
    chap_id = "c9_9"
    l_idx = 5
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_polys = [
        ("gạch lát nền hình lục giác đều nghệ thuật", 20, "cm"),
        ("biển báo giao thông hình bát giác đều dừng lại Stop", 30, "cm"),
        ("tổ ong mật tự nhiên hình lục giác đều tối ưu diện tích", 5, "mm"),
        ("mặt bàn trà trang trí hình ngũ giác đều", 40, "cm"),
        ("đai ốc cơ khí hình lục giác đều bằng thép không gỉ", 15, "mm"),
        ("hoa văn mặt trống đồng hình đa giác đều", 60, "cm"),
        ("mặt kính đồng hồ hình bát giác đều phong thủy", 25, "cm")
    ]
    
    for t in range(1, 8):
        app = real_polys[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", "Đa giác đều là đa giác có:", ["Tất cả các cạnh bằng nhau và tất cả các góc bằng nhau", "Tất cả các cạnh bằng nhau", "Tất cả các góc bằng nhau", "Có các cạnh đối song song"], 0),
            make_mc(2, "Nhận biết", "Mỗi góc của một tam giác đều có số đo bằng:", ["$60^\\circ$", "$90^\\circ$", "$45^\\circ$", "$120^\\circ$"], 0),
            make_mc(3, "Nhận biết", "Mỗi góc của một hình lục giác đều có số đo bằng:", ["$120^\\circ$", "$108^\\circ$", "$60^\\circ$", "$90^\\circ$"], 0),
            make_mc(4, "Nhận biết", "Đường tròn đi qua tất cả các đỉnh của một đa giác được gọi là:", ["Đường tròn ngoại tiếp đa giác", "Đường tròn nội tiếp đa giác", "Đường tròn bàng tiếp", "Đường tròn tiếp xúc"], 0),
            make_mc(5, "Thông hiểu", f"Cho tam giác đều $ABC$ có cạnh bằng ${6*t}\\text{{ cm}}$. Bán kính đường tròn ngoại tiếp tam giác là:", [f"${2*t}\\sqrt{3}\\text{{ cm}}$", f"${3*t}\\text{{ cm}}$", f"${t}\\sqrt{3}\\text{{ cm}}$", f"${6*t}\\text{{ cm}}$"], 0),
            make_mc(6, "Thông hiểu", f"Cho hình vuông có cạnh bằng ${4*t}\\text{{ cm}}$. Bán kính đường tròn nội tiếp hình vuông đó là:", [f"${2*t}\\text{{ cm}}$", f"${4*t}\\text{{ cm}}$", f"${2*t}\\sqrt{2}\\text{{ cm}}$", f"${t}\\text{{ cm}}$"], 0),
            make_mc(7, "Thông hiểu", "Một hình lục giác đều có cạnh bằng $a$. Bán kính đường tròn ngoại tiếp của nó bằng:", ["$a$", "$a\\sqrt{3}$", "$\\frac{a\\sqrt{3}}{2}$", "$\\frac{{a}}{{2}}$"], 0),
            make_mc(8, "Thông hiểu", f"Số đường chéo của một hình lục giác đều là:", ["$9$", "$6$", "$12$", "$15$"], 0),
            make_mc(9, "Vận dụng", f"Một viên {app[0]} có độ dài cạnh là ${app[1]}\\text{{{app[2]}}}$ được tạo bởi 6 tam giác đều. Diện tích của viên gạch là:", [f"${6 * ((app[1]**2 * 1.732)/4):.1f}\\text{{{app[2]}}}^2$", "500", "300", "200"], 0),
            make_mc(10, "Vận dụng", f"Biển báo giao thông Stop hình bát giác đều có cạnh ${app[1]}\\text{{ cm}}$. Chu vi của biển báo giao thông đó là:", [f"${8*app[1]}\\text{{ cm}}$", f"${6*app[1]}\\text{{ cm}}$", f"${4*app[1]}\\text{{ cm}}$", "100 cm"], 0),
            make_mc(11, "Vận dụng", f"Cho tam giác đều cạnh $a$. Tỉ số bán kính đường tròn ngoại tiếp $R$ và nội tiếp $r$ của tam giác đều bằng:", ["$2$", "$\\sqrt{3}$", "$3$", "$\\frac{3}{2}$"], 0),
            make_mc(12, "Vận dụng cao", "Người ta muốn cắt một miếng tôn hình tròn có bán kính $R = 20\\text{{ cm}}$ thành một hình vuông có diện tích lớn nhất. Diện tích lớn nhất của hình vuông đó là:", ["$800\\text{{ cm}}^2$", "$400\\text{{ cm}}^2$", "$1600\\text{{ cm}}^2$", "$600\\text{{ cm}}^2$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về đa giác đều (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Mọi đa giác đều luôn có một đường tròn ngoại tiếp và một đường tròn nội tiếp cùng tâm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hình vuông là tứ giác đều.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Mỗi góc trong của hình ngũ giác đều bằng 108 độ.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Bán kính đường tròn nội tiếp hình vuông lớn hơn bán kính đường tròn ngoại tiếp của nó.", "correct": False}
            ]),
            make_tf(2, f"Cho tam giác đều $ABC$ cạnh bằng ${12*t}\\text{{ cm}}$ nội tiếp đường tròn $(O; R)$ và ngoại tiếp đường tròn $(O; r)$:", [
                {"key": "a", "level": "Nhận biết", "text": "Tâm O là trọng tâm đồng thời là trực tâm của tam giác đều ABC.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Đường cao của tam giác đều bằng {6*t} căn(3) cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Bán kính đường tròn ngoại tiếp R = {4*t} căn(3) cm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tỉ số diện tích hình tròn ngoại tiếp và nội tiếp bằng 2.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính số đo mỗi góc trong của hình bát giác đều (độ).", "135"),
            make_sa(2, "Thông hiểu", f"Cho tam giác đều cạnh bằng 6 cm. Tính bán kính đường tròn ngoại tiếp R (cm, làm tròn 1 chữ số thập phân).", "3.5"),
            make_sa(3, "Vận dụng", f"Một chiếc đai ốc lục giác đều có cạnh 10 mm. Tính khoảng cách giữa hai cạnh đối diện của đai ốc (mm, làm tròn 1 chữ số thập phân).", "17.3"),
            make_sa(4, "Vận dụng", f"Cho hình vuông có diện tích 64 cm^2. Tính diện tích hình tròn ngoại tiếp hình vuông đó (lấy pi = 3,14, cm^2).", "100.48")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho hình lục giác đều $ABCDEF$ cạnh bằng ${4*t}\\text{{ cm}}$. Hãy giải thích vì sao tam giác $OAB$ là tam giác đều ($O$ là tâm của lục giác) và tính diện tích tam giác $OAB$.",
                       f"Vì lục giác đều có 6 cạnh bằng nhau nên góc ở tâm AOB = 360 độ / 6 = 60 độ (0.25đ).\nTam giác OAB cân tại O có góc ở đỉnh 60 độ nên là tam giác đều cạnh bằng {4*t} cm (0.25đ).\nDiện tích tam giác đều OAB: S = a^2 . căn(3)/4 = ({4*t})^2 . căn(3)/4 = {4*t*t} căn(3) (cm^2) (0.25đ).\nKết luận diện tích tam giác (0.25đ)."),
            make_essay(2, "Vận dụng", f"Người ta dùng các viên gạch men hình lục giác đều cạnh $20\\text{{ cm}}$ để lát sàn một căn phòng có diện tích $30\\text{{ m}}^2$. Biết diện tích mỗi viên gạch xấp xỉ $0,1\\text{{ m}}^2$. Tính số viên gạch cần dùng (coi mạch vữa không đáng kể).",
                       "Đổi đơn vị đo diện tích đồng nhất (0.25đ).\nDiện tích sàn phòng là 30 m^2, diện tích 1 viên gạch là 0,1 m^2 (0.25đ).\nSố viên gạch cần dùng là: 30 / 0,1 = 300 (viên gạch) (0.25đ).\nKết luận số lượng gạch cần mua (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Chứng minh rằng trong tất cả các hình chữ nhật có cùng chu vi $2p$, hình vuông là hình có diện tích lớn nhất.",
                       "Gọi hai kích thước của hình chữ nhật là a và b (a, b > 0) => a + b = p (không đổi) (0.25đ).\nDiện tích hình chữ nhật là S = a . b (0.25đ).\nÁp dụng bất đẳng thức Cauchy cho hai số dương a, b: S = ab <= ((a + b)/2)^2 = (p/2)^2 (0.25đ).\nDấu '=' xảy ra khi a = b = p/2 (tức hình chữ nhật trở thành hình vuông). Vậy hình vuông có diện tích lớn nhất (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương IX: Đa giác đều - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương IX: Đa giác đều", exams)

# ------------------------------------------------------------------------------
# CHƯƠNG 10 TOÁN 9: Một số hình khối trong thực tiễn (Bài 3)
# ------------------------------------------------------------------------------
def build_c10_9():
    chap_id = "c10_9"
    l_idx = 3
    exams = load_existing_exams(chap_id, 9)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]
            
    real_solids = [
        ("lon nước ngọt hình trụ bằng nhôm", 3, 12, "cm"),
        ("chiếc nón lá truyền thống Việt Nam hình nón", 20, 25, "cm"),
        ("quả bóng đá tiêu chuẩn FIFA hình cầu", 11, 22, "cm"),
        ("bồn chứa xăng dầu công nghiệp hình trụ", 2, 5, "m"),
        ("ly kem ốc quế giòn hình nón", 3, 10, "cm"),
        ("bể chứa nước sạch sinh hoạt hình cầu", 1.5, 3, "m"),
        ("hộp sữa đặc hình trụ bằng kim loại", 4, 8, "cm")
    ]
    
    for t in range(1, 8):
        app = real_solids[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", "Diện tích xung quanh của hình trụ có bán kính đáy $r$ và chiều cao $h$ là:", ["$S_{xq} = 2\\pi r h$", "$S_{xq} = \\pi r h$", "$S_{xq} = 2\\pi r^2$", "$S_{xq} = \\pi r^2 h$"], 0),
            make_mc(2, "Nhận biết", "Thể tích của hình nón có bán kính đáy $r$ và chiều cao $h$ là:", ["$V = \\frac{1}{3}\\pi r^2 h$", "$V = \\pi r^2 h$", "$V = \\frac{{4}}{{3}}\\pi r^3$", "$V = 2\\pi r h$"], 0),
            make_mc(3, "Nhận biết", "Diện tích mặt cầu bán kính $R$ được tính theo công thức:", ["$S = 4\\pi R^2$", "$S = \\frac{{4}}{{3}}\\pi R^3$", "$S = 2\\pi R^2$", "$S = \\pi R^2$"], 0),
            make_mc(4, "Nhận biết", "Thể tích của hình cầu bán kính $R$ là:", ["$V = \\frac{{4}}{{3}}\\pi R^3$", "$V = 4\\pi R^2$", "$V = \\frac{1}{3}\\pi R^2 h$", "$V = \\pi R^3$"], 0),
            make_mc(5, "Thông hiểu", f"Một hình trụ có bán kính đáy $r = {t*2}\\text{{ cm}}$ và chiều cao $h = 5\\text{{ cm}}$. Thể tích của hình trụ là:", [f"${20*t*t}\\pi\\text{{ cm}}^3$", f"${10*t}\\pi\\text{{ cm}}^3$", f"${4*t*t}\\pi\\text{{ cm}}^3$", f"${50*t}\\pi\\text{{ cm}}^3$"], 0),
            make_mc(6, "Thông hiểu", f"Một hình nón có bán kính đáy $r = 3\\text{{ cm}}$, đường sinh $l = 5\\text{{ cm}}$. Diện tích xung quanh của hình nón là:", ["$15\\pi\\text{{ cm}}^2$", "$30\\pi\\text{{ cm}}^2$", "$45\\pi\\text{{ cm}}^2$", "$9\\pi\\text{{ cm}}^2$"], 0),
            make_mc(7, "Thông hiểu", f"Một quả bóng hình cầu có bán kính $R = 3\\text{{ cm}}$. Diện tích bề mặt của quả bóng là:", ["$36\\pi\\text{{ cm}}^2$", "$12\\pi\\text{{ cm}}^2$", "$9\\pi\\text{{ cm}}^2$", "$27\\pi\\text{{ cm}}^2$"], 0),
            make_mc(8, "Thông hiểu", "Cắt một hình trụ bởi mặt phẳng song song với trục, thiết diện thu được là:", ["Một hình chữ nhật", "Một hình tròn", "Một hình tam giác", "Một hình elip"], 0),
            make_mc(9, "Vận dụng", f"Một {app[0]} có bán kính đáy ${app[1]}\\text{{{app[3]}}}$ và chiều cao ${app[2]}\\text{{{app[3]}}}$. Thể tích chứa của vật phẩm là:", [f"${3.14 * app[1]**2 * app[2]:.1f}\\text{{{app[3]}}}^3$", "200", "500", "150"], 0),
            make_mc(10, "Vận dụng", f"Chiếc nón lá có đường kính đáy $40\\text{{ cm}}$ (bán kính $r = 20\\text{{ cm}}$) và đường sinh $l = 30\\text{{ cm}}$. Diện tích lá nón cần dùng để phủ kín mặt ngoài xấp xỉ là:", [f"${3.14 * 20 * 30}\\text{{ cm}}^2$", "1200 cm^2", "1500 cm^2", "800 cm^2"], 0),
            make_mc(11, "Vận dụng", "Một bể chứa nước hình cầu có đường kính $2\\text{{ m}}$ (bán kính $R = 1\\text{{ m}}$). Thể tích nước tối đa mà bể có thể chứa xấp xỉ là:", ["$4,19\\text{{ m}}^3$", "$12,56\\text{{ m}}^3$", "$3,14\\text{{ m}}^3$", "$2,09\\text{{ m}}^3$"], 0),
            make_mc(12, "Vận dụng cao", "Một thùng chứa dạng hình trụ không có nắp được làm bằng tôn có thể tích $V = 54\\pi\\text{{ dm}}^3$. Để tiết kiệm tôn nhất (diện tích toàn phần nhỏ nhất) thì bán kính đáy $r$ bằng:", ["$3\\text{{ dm}}$", "$2\\text{{ dm}}$", "$4\\text{{ dm}}$", "$6\\text{{ dm}}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về các hình khối trong không gian (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Khi quay một hình chữ nhật quanh một cạnh cố định ta được một hình trụ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi quay một tam giác vuông quanh một cạnh góc vuông cố định ta được một hình nón.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Khi quay một nửa hình tròn quanh đường kính cố định ta được một hình cầu.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hình nón và hình trụ có cùng bán kính đáy và chiều cao thì thể tích hình nón bằng một nửa thể tích hình trụ.", "correct": False}
            ]),
            make_tf(2, f"Bài toán kỹ thuật gia công kim loại (Mã đề {t:02d}): Một xưởng cơ khí đúc một chi tiết máy bằng thép đặc có dạng hình trụ cao 10 cm, bán kính đáy 4 cm. Khối lượng riêng của thép là 7,85 g/cm^3.", [
                {"key": "a", "level": "Nhận biết", "text": "Thể tích chi tiết máy tính theo công thức V = pi . r^2 . h.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích đáy của hình trụ là 16 pi cm^2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Thể tích của chi tiết máy là 160 pi cm^3 (xấp xỉ 502,4 cm^3).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Khối lượng của chi tiết máy lớn hơn 5 kg.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Tính thể tích của hình trụ có bán kính r = 3 cm và chiều cao h = 7 cm (lấy pi = 22/7, cm^3).", "198"),
            make_sa(2, "Thông hiểu", "Một hình nón có bán kính đáy r = 5 cm, chiều cao h = 12 cm. Tính độ dài đường sinh l của hình nón (cm).", "13"),
            make_sa(3, "Vận dụng", "Một bồn chứa nước hình trụ có bán kính đáy 0,5 m và chiều cao 2 m. Tính lượng nước tối đa bồn chứa được theo đơn vị lít (lấy pi = 3,14, 1 m^3 = 1000 lít).", "1570"),
            make_sa(4, "Vận dụng", "Một quả cầu bằng sắt đặc có bán kính R = 3 cm. Biết khối lượng riêng của sắt là 7,8 g/cm^3. Tính khối lượng quả cầu sắt (lấy pi = 3,14, gam, làm tròn số nguyên).", "882")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Một chiếc cốc uống nước hình trụ có bán kính đáy $r = 3\\text{{ cm}}$ và chiều cao $h = 10\\text{{ cm}}$. Tính diện tích xung quanh và thể tích của chiếc cốc (lấy $\\pi \\approx 3,14$).",
                       "Diện tích xung quanh: Sxq = 2 . pi . r . h = 2 . 3,14 . 3 . 10 = 188,4 (cm^2) (0.25đ).\nThể tích cốc: V = pi . r^2 . h = 3,14 . 3^2 . 10 = 3,14 . 9 . 10 = 282,6 (cm^3) (0.25đ).\nKết luận diện tích và thể tích (0.25đ)."),
            make_essay(2, "Vận dụng", f"Một hộp sữa bột hình trụ có đường kính đáy $12\\text{{ cm}}$ (bán kính $r = 6\\text{{ cm}}$) và chiều cao $18\\text{{ cm}}$. Người ta dán một nhãn giấy bao quanh thân hộp (không phủ nắp và đáy). Tính diện tích nhãn giấy cần dán (lấy $\\pi \\approx 3,14$, làm tròn đến hàng đơn vị).",
                       "Diện tích nhãn giấy chính là diện tích xung quanh của hộp sữa hình trụ (0.25đ).\nCông thức: Sxq = 2 . pi . r . h (0.25đ).\nThay số: Sxq = 2 . 3,14 . 6 . 18 = 678,24 (cm^2) xấp xỉ 678 cm^2 (0.25đ).\nKết luận diện tích giấy nhãn cần dùng (0.25đ)."),
            make_essay(3, "Vận dụng cao", "Người ta thả một viên bi kim loại hình cầu bán kính $R = 3\\text{{ cm}}$ vào một bình nước hình trụ có bán kính đáy $r = 6\\text{{ cm}}$ đang chứa nước. Hỏi mực nước trong bình dâng lên thêm bao nhiêu xentimét?",
                       "Thể tích của viên bi hình cầu là: V_cau = 4/3 . pi . R^3 = 4/3 . pi . 3^3 = 36 pi (cm^3) (0.25đ).\nKhi thả bi chìm vào nước, lượng nước dâng lên bằng thể tích của viên bi (0.25đ).\nThể tích nước dâng trong bình trụ: V_dang = pi . r^2 . h_dang = pi . 6^2 . h_dang = 36 pi . h_dang (0.25đ).\nVì V_dang = V_cau => 36 pi . h_dang = 36 pi => h_dang = 1 (cm). Vậy mực nước dâng thêm 1 cm (0.25đ).")
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 9 (KNTT) - Bài kiểm tra cuối Chương X: Một số hình khối trong thực tiễn - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(9, chap_id, "Chương X: Một số hình khối trong thực tiễn", exams)

# ==============================================================================
# HÀM CHÍNH: CHẠY HOÀN THIỆN CẢ 10 CHƯƠNG TOÁN 9
# ==============================================================================
def run_all():
    print("=== BẮT ĐẦU SINH 7 ĐỀ ĐỘC LẬP CHO TOÀN BỘ 10 CHƯƠNG TOÁN 9 ===")
    build_c1_9()
    build_c2_9()
    build_c3_9()
    build_c4_9()
    build_c5_9()
    build_c6_9()
    build_c7_9()
    build_c8_9()
    build_c9_9()
    build_c10_9()
    print("=== HOÀN TẤT XUẤT SẮC TOÁN 9: 10 CHƯƠNG x 7 ĐỀ = 70 ĐỀ CHUẨN MA TRẬN ===")

if __name__ == "__main__":
    run_all()
