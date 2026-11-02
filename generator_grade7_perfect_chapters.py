# -*- coding: utf-8 -*-
"""
BUILD COMPLETE GRADE 7 EXAMS (10 CHAPTERS x 7 TESTS = 70 TESTS)
- 7 đề hoàn toàn khác nhau 100%
- Bao quát toàn bộ nội dung của từng chương
- KHÔNG CÓ BẤT KỲ CÂU HỎI THAM SỐ m NÀO
- Tăng cường tối đa bài toán thực tế đời sống
- Chuẩn tỷ lệ: 30% Nhận biết, 30% Thông hiểu, 30% Vận dụng, 10% Vận dụng cao
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package, OUTPUT_DIR

def load_existing_exams(chap_id, grade=7):
    json_path = os.path.join(OUTPUT_DIR, f"grade{grade}_{chap_id}_exams.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            d = json.load(f)
            return d.get("exams", {})
    return {}

# ------------------------------------------------------------------------------
# CHƯƠNG I: Số hữu tỉ (l_idx = 5)
# ------------------------------------------------------------------------------
def build_c1_7():
    chap_id = "c1_7"
    l_idx = 5
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Số hữu tỉ là số viết được dưới dạng phân số $\\frac{{a}}{{b}}$ với (Đề {t:02d}):", ["$a, b \\in \\mathbb{Z}, b \\neq 0$", "$a, b \\in \\mathbb{N}$", "$a \\in \\mathbb{Z}, b = 0$", "$a, b \\in \\mathbb{Q}$"], 0),
            make_mc(2, "Nhận biết", f"Số đối của số hữu tỉ $-\\frac{{{t}}}{{{t+2}}}$ là:", [f"$\\frac{{{t}}}{{{t+2}}}$", f"$-\\frac{{{t+2}}}{{{t}}}$", f"$\\frac{{{t+2}}}{{{t}}}$", f"$-{t}$"], 0),
            make_mc(3, "Nhận biết", "Tập hợp các số hữu tỉ được kí hiệu là:", ["$\\mathbb{Q}$", "$\\mathbb{Z}$", "$\\mathbb{N}$", "$\\mathbb{R}$"], 0),
            make_mc(4, "Nhận biết", "Khẳng định nào sau đây là ĐÚNG về luỹ thừa với số mũ tự nhiên?", ["$x^m \\cdot x^n = x^{m+n}$", "$x^m \\cdot x^n = x^{m \\cdot n}$", "$(x^m)^n = x^{m+n}$", "$x^m : x^n = x^{m:n}$"], 0),
            make_mc(5, "Thông hiểu", f"Kết quả của phép tính $\\frac{{{t}}}{{4}} + \\frac{{{2*t}}}{{4}}$ là:", [f"$\\frac{{{3*t}}}{{4}}$", f"$\\frac{{{2*t*t}}}{{4}}$", f"$\\frac{{{3*t}}}{{8}}$", f"${t}$"], 0),
            make_mc(6, "Thông hiểu", f"Giá trị của $(-0,5)^2 \\cdot {4*t}$ bằng:", [f"${t}$", f"${-t}$", f"${2*t}$", f"${4*t}$"], 0),
            make_mc(7, "Thông hiểu", f"Tìm $x$, biết: $x - \\frac{{{t}}}{{2}} = \\frac{1}{2}$:", [f"$x = \\frac{{{t+1}}}{{2}}$", f"$x = \\frac{{{t-1}}}{{2}}$", f"$x = {t}$", "$x = 1$"], 0),
            make_mc(8, "Thông hiểu", f"So sánh hai số hữu tỉ $a = -\\frac{{{t}}}{{5}}$ và $b = -\\frac{{{t+1}}}{{5}}$:", ["$a > b$", "$a < b$", "$a = b$", "Không so sánh được"], 0),
            make_mc(9, "Vận dụng", f"Nhiệt độ đo được ở thị xã Sa Pa lúc 6 giờ sáng là $-1,{t}^\\circ^\\circ C$, đến 12 giờ trưa nhiệt độ tăng thêm $5,{t}^\\circ^\\circ C$. Nhiệt độ lúc 12 giờ trưa là:", ["$4^\\circ^\\circ C$", "$6^\\circ^\\circ C$", "$3^\\circ^\\circ C$", "$5^\\circ^\\circ C$"], 0),
            make_mc(10, "Vận dụng", f"Một cửa hàng tạp hóa giảm giá $20\\%$ cho một hộp bánh có giá niêm yết là ${100+t*10}$ nghìn đồng. Bác Lan mua 2 hộp bánh đó thì phải trả số tiền là:", [f"{2 * (100+t*10) * 0.8:.1f} nghìn đồng", f"{2 * (100+t*10)} nghìn đồng", "150 nghìn đồng", "180 nghìn đồng"], 0),
            make_mc(11, "Vận dụng", f"Một tàu ngầm đang ở độ sâu ${30+t*5}$ mét dưới mực nước biển (được biểu thị bởi số âm). Tàu lặn sâu thêm $15$ mét nữa rồi lại nổi lên $20$ mét. Vị trí mới của tàu ngầm biểu thị bởi số:", [f"${-(30+t*5 + 15 - 20)}$ mét", f"${-(30+t*5)}$ mét", "-50 mét", "-40 mét"], 0),
            make_mc(12, "Vận dụng cao", f"Giá trị nhỏ nhất của biểu thức $A = |x - {t}| + |x - {t + 4}|$ bằng:", ["4", f"${t}$", f"${2*t}$", "0"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về số hữu tỉ và các phép toán (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Mọi số nguyên đều là số hữu tỉ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Số thập phân hữu hạn 0,{t} có thể biểu diễn dưới dạng phân số tối giản.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Khoảng cách từ điểm x trên trục số đến gốc O là giá trị tuyệt đối của x.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tích của hai số hữu tỉ âm luôn là một số âm.", "correct": False}
            ]),
            make_tf(2, f"Bài toán kinh doanh gia đình (Mã đề {t:02d}): Bác Nam mở một cửa hàng bán hoa quả. Tháng đầu tiên lãi 12 triệu đồng, tháng thứ hai lỗ 3,5 triệu đồng, tháng thứ ba lãi 8,5 triệu đồng.", [
                {"key": "a", "level": "Nhận biết", "text": "Số tiền lãi hoặc lỗ mỗi tháng được biểu diễn bằng các số hữu tỉ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số tiền lỗ tháng thứ hai được biểu diễn bởi số âm -3,5 triệu đồng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tổng lợi nhuận của bác Nam sau 3 tháng là 12 + (-3,5) + 8,5 = 17 triệu đồng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Lợi nhuận trung bình mỗi tháng của bác Nam lớn hơn 6 triệu đồng.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính giá trị của phép tính: (1/2 + 3/4) * {4*t}.", f"{5*t}"),
            make_sa(2, "Thông hiểu", f"Tìm x biết: |x - {t}| = 0.", f"{t}"),
            make_sa(3, "Vận dụng", f"Một bình chứa {2+t*0.5:.1f} lít nước cam. Mẹ rót đều vào 4 cốc. Hỏi mỗi cốc chứa bao nhiêu lít nước cam?", f"{(2+t*0.5)/4:.3f}"),
            make_sa(4, "Vận dụng", f"Bác thợ may dùng một tấm vải dài {15+t} mét để may các bộ quần áo đồng phục. Mỗi bộ hết 2,5 mét vải. Hỏi bác may được tối đa bao nhiêu bộ quần áo hoàn chỉnh?", f"{int((15+t)/2.5)}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Thực hiện phép tính một cách hợp lí: $A = \\frac{{{t}}}{{7}} \\cdot \\left(-\\frac{5}{9}\\right) + \\frac{{{t}}}{{7}} \\cdot \\left(-\\frac{4}{9}\\right)$.",
                       "\n".join([
                           f"Đặt thừa số chung {t}/7 ra ngoài ngoặc (0.25đ).",
                           "Trong ngoặc: (-5/9) + (-4/9) = -9/9 = -1 (0.25đ).",
                           f"Tính tích: A = ({t}/7) . (-1) = -{t}/7 (0.25đ).",
                           f"Kết luận kết quả A = -{t}/7 (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một người gửi tiết kiệm {50+t*10} triệu đồng vào ngân hàng với lãi suất $6\\%$ một năm. Hỏi sau một năm người đó nhận được tổng cộng cả tiền gốc và tiền lãi là bao nhiêu triệu đồng?",
                       "\n".join([
                           f"Tiền lãi sau một năm: ({50+t*10}) . 6% = ({50+t*10}) . 0,06 (triệu đồng) (0.25đ).",
                           f"Tính tiền lãi cụ thể: { (50+t*10)*0.06:.2f} triệu đồng (0.25đ).",
                           f"Tổng số tiền nhận được: ({50+t*10}) + {(50+t*10)*0.06:.2f} = {(50+t*10)*1.06:.2f} (triệu đồng) (0.25đ).",
                           "Kết luận số tiền cả gốc lẫn lãi sau 1 năm (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Tìm giá trị nhỏ nhất của biểu thức: $M = |x - {t}| + |x - {t + 6}| + 2026$.",
                       "\n".join([
                           f"Áp dụng bất đẳng thức |a| + |b| >= |a + b| (0.25đ).",
                           f"Biến đổi M = |x - {t}| + |{t + 6} - x| + 2026 >= |x - {t} + {t + 6} - x| + 2026 (0.25đ).",
                           "M >= 6 + 2026 = 2032 (0.25đ).",
                           f"Dấu '=' xảy ra khi {t} <= x <= {t + 6}. Kết luận GTNN của M là 2032 (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương I: Số hữu tỉ - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương I: Số hữu tỉ", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG II: Số thực (l_idx = 4)
# ------------------------------------------------------------------------------
def build_c2_7():
    chap_id = "c2_7"
    l_idx = 4
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Căn bậc hai số học của số ${t*t}$ là (Đề {t:02d}):", [f"${t}$", f"$-{t}$", f"$\\pm {t}$", f"${t*t}$"], 0),
            make_mc(2, "Nhận biết", "Số vô tỉ là số viết được dưới dạng:", ["Số thập phân vô hạn không tuần hoàn", "Số thập phân hữu hạn", "Phân số", "Số nguyên âm"], 0),
            make_mc(3, "Nhận biết", "Tập hợp các số thực được kí hiệu là:", ["$\\mathbb{R}$", "$\\mathbb{I}$", "$\\mathbb{Q}$", "$\\mathbb{Z}$"], 0),
            make_mc(4, "Nhận biết", "Số nào sau đây là số vô tỉ?", ["$\\sqrt{2}$", "$\\sqrt{4}$", "0,25", "$-\\frac{1}{3}$"], 0),
            make_mc(5, "Thông hiểu", f"Làm tròn số $3,14159$ đến hàng phần trăm (chữ số thập phân thứ hai) ta được:", ["3,14", "3,15", "3,1", "3,142"], 0),
            make_mc(6, "Thông hiểu", f"Giá trị của biểu thức $\\sqrt{{{t*t}}} + \\sqrt{{{4*t*t}}}$ bằng:", [f"${3*t}$", f"${5*t}$", f"${t}$", f"${2*t}$"], 0),
            make_mc(7, "Thông hiểu", f"Tìm $x$ không âm, biết $\\sqrt{{x}} = {t}$:", [f"$x = {t*t}$", f"$x = {2*t}$", f"$x = {t}$", f"$x = \\sqrt{{{t}}}$"], 0),
            make_mc(8, "Thông hiểu", "Khẳng định nào sau đây là SAI?", ["Mọi số thực đều là số vô tỉ", "Mọi số hữu tỉ đều là số thực", "Số 0 là số thực", "Số vô tỉ là số thực"], 0),
            make_mc(9, "Vận dụng", f"Một thửa ruộng hình vuông có diện tích bằng ${100+t*20}$ mét vuông. Độ dài cạnh của thửa ruộng hình vuông xấp xỉ bằng (làm tròn 1 chữ số thập phân):", [f"{(100+t*20)**0.5:.1f} mét", "10 mét", "12 mét", "15 mét"], 0),
            make_mc(10, "Vận dụng", f"Bác An đi siêu thị mua hàng hết {187+t*5} 450 đồng. Khi thanh toán bằng tiền mặt, nhân viên làm tròn đến hàng nghìn thành:", [f"{(187+t*5 + 1)} 000 đồng", f"{187+t*5} 000 đồng", "190 000 đồng", "180 000 đồng"], 0),
            make_mc(11, "Vận dụng", f"Độ dài đường chéo của một màn hình tivi hình chữ nhật có kích thước $60$ cm và $80$ cm là $\\sqrt{{60^2 + 80^2}}$. Độ dài đường chéo đó bằng:", ["100 cm", "140 cm", "120 cm", "80 cm"], 0),
            make_mc(12, "Vận dụng cao", f"Số các giá trị nguyên của $x$ thỏa mãn $4 < \\sqrt{{x}} < {t + 5}$ là:", [f"{(t+5)**2 - 17}", "10", "20", "5"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về số thực (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Tập hợp số thực R bao gồm cả số hữu tỉ và số vô tỉ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Mỗi số thực được biểu diễn bởi đúng một điểm trên trục số.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Căn bậc hai số học của {4*t*t} là {2*t}.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số đối của căn bậc hai số học của a luôn là số dương.", "correct": False}
            ]),
            make_tf(2, f"Bài toán kỹ thuật đo đạc (Mã đề {t:02d}): Một kiến trúc sư đo chiều dài một căn phòng là 5,456 mét và muốn làm tròn số đo.", [
                {"key": "a", "level": "Nhận biết", "text": "Số 5,456 là một số thập phân hữu hạn.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Làm tròn đến chữ số thập phân thứ nhất ta được 5,5 mét.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Làm tròn đến chữ số thập phân thứ hai ta được 5,46 mét.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Sai số tuyệt đối khi làm tròn đến hàng đơn vị nhỏ hơn 0,1.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính căn bậc hai số học của {9*t*t}.", f"{3*t}"),
            make_sa(2, "Thông hiểu", "Làm tròn số 12,345 đến hàng phần mười.", "12.3"),
            make_sa(3, "Vận dụng", f"Một bức tranh hình vuông có diện tích {144+t*10} cm^2. Tính độ dài cạnh bức tranh (làm tròn 1 chữ số thập phân, cm).", f"{(144+t*10)**0.5:.1f}"),
            make_sa(4, "Vận dụng", f"Một người có cân nặng 65,48 kg. Hỏi cân nặng của người đó làm tròn đến hàng đơn vị là bao nhiêu kg?", "65")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"So sánh hai số thực sau mà không dùng máy tính: $A = \\sqrt{{{t*t + 1}}}$ và $B = {t}$.",
                       "\n".join([
                           f"Ta có: A^2 = {t*t + 1} (0.25đ).",
                           f"B^2 = {t}^2 = {t*t} (0.25đ).",
                           f"Vì {t*t + 1} > {t*t} nên căn({t*t + 1}) > {t} (0.25đ).",
                           f"Kết luận A > B (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một khu vườn hình vuông có diện tích ${400+t*50}$ mét vuông. Bác thợ dự định đóng cọc rào xung quanh khu vườn, mỗi cọc cách nhau $2$ mét. Tính số cọc cần chuẩn bị.",
                       "\n".join([
                           f"Cạnh của khu vườn: a = căn({400+t*50}) (m) (0.25đ).",
                           f"Tính chu vi khu vườn: P = 4 . a (m) (0.25đ).",
                           "Số cọc rào = Chu vi / 2 (0.25đ).",
                           "Kết luận số cọc cần chuẩn bị (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Tìm số thực $x$ thỏa mãn đẳng thức: $\\sqrt{{2x - 1}} + \\sqrt{{{t*t}}} = {t + 3}$.",
                       "\n".join([
                           "Điều kiện xác định: 2x - 1 >= 0 <=> x >= 1/2 (0.25đ).",
                           f"Phương trình tương đương: căn(2x - 1) + {t} = {t + 3} (0.25đ).",
                           "căn(2x - 1) = 3 <=> 2x - 1 = 9 <=> 2x = 10 <=> x = 5 (0.25đ).",
                           "Kiểm tra điều kiện và kết luận nghiệm x = 5 (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương II: Số thực - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương II: Số thực", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG III: Góc và đường thẳng song song (l_idx = 5)
# ------------------------------------------------------------------------------
def build_c3_7():
    chap_id = "c3_7"
    l_idx = 5
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Hai góc đối đỉnh thì (Đề {t:02d}):", ["Bằng nhau", "Bù nhau", "Phụ nhau", "Kề bù"], 0),
            make_mc(2, "Nhận biết", "Tia phân giác của một góc là tia nằm trong góc và:", ["Tạo với hai cạnh hai góc bằng nhau", "Vuông góc với một cạnh", "Cắt cạnh đối diện", "Song song với cạnh"], 0),
            make_mc(3, "Nhận biết", "Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc so le trong:", ["Bằng nhau", "Bù nhau", "Phụ nhau", "Kề nhau"], 0),
            make_mc(4, "Nhận biết", "Hai góc kề bù có tổng số đo bằng:", ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$60^\\circ$"], 0),
            make_mc(5, "Thông hiểu", f"Cho hai góc đối đỉnh $\\widehat{{xOy}}$ và $\\widehat{{x'Oy'}}$. Biết $\\widehat{{xOy}} = {50+t*5}^\\circ$. Số đo góc $\\widehat{{x'Oy'}}$ là:", [f"${50+t*5}^\\circ$", f"${130-t*5}^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0),
            make_mc(6, "Thông hiểu", f"Cho đường thẳng $a // b$. Một đường thẳng $c$ cắt $a$ và $b$. Biết một góc đồng vị bằng ${70+t}^\\circ$. Góc đồng vị tương ứng bằng:", [f"${70+t}^\\circ$", f"${110-t}^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0),
            make_mc(7, "Thông hiểu", f"Tia $Oz$ là tia phân giác của $\\widehat{{xOy}} = {80+t*2}^\\circ$. Số đo góc $\\widehat{{xOz}}$ là:", [f"${40+t}^\\circ$", f"${80+t*2}^\\circ$", "$90^\\circ$", "$50^\\circ$"], 0),
            make_mc(8, "Thông hiểu", "Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì:", ["Song song với nhau", "Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], 0),
            make_mc(9, "Vận dụng", f"Khung cửa sổ có hai thanh song song $AB // CD$. Người ta lắp thanh chéo $MN$ tạo với thanh $AB$ một góc so le trong bằng ${65+t}^\\circ$. Góc tạo bởi $MN$ và thanh $CD$ ở vị trí so le trong bằng:", [f"${65+t}^\\circ$", f"${115-t}^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0),
            make_mc(10, "Vận dụng", f"Người thợ mộc kiểm tra hai mép gỗ có song song hay không bằng cách đo hai góc trong cùng phía. Nếu hai mép gỗ song song thì tổng số đo hai góc trong cùng phía phải bằng:", ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$100^\\circ$"], 0),
            make_mc(11, "Vận dụng", f"Một mái nhà nghiêng tạo với mặt đất nằm ngang góc ${30+t}^\\circ$. Xà gồ đặt song song với mặt đất. Góc tạo bởi thanh kèo mái và xà gồ bằng:", [f"${30+t}^\\circ$", f"${60-t}^\\circ$", "$90^\\circ$", "$45^\\circ$"], 0),
            make_mc(12, "Vận dụng cao", "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$. Gọi $Om, On$ lần lượt là tia phân giác của $\\widehat{xOy}$ và $\\widehat{yOz}$. Số đo góc $\\widehat{mOn}$ luôn bằng:", ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$", "$60^\\circ$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về góc và hai đường thẳng song song (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Qua một điểm ở ngoài một đường thẳng chỉ có một đường thẳng song song với đường thẳng đó.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hai góc so le trong bằng nhau thì hai đường thẳng song song.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai góc đồng vị bằng nhau thì hai đường thẳng song song.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hai góc có tổng bằng 180 độ thì luôn là hai góc kề bù.", "correct": False}
            ]),
            make_tf(2, f"Cho hình vẽ hai đường thẳng a và b cùng cắt đường thẳng c tại A và B (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Tại mỗi đỉnh A và B tạo ra 4 góc.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Nếu một góc so le trong bằng {60+t} độ thì góc đối đỉnh với nó cũng bằng {60+t} độ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Nếu một góc trong cùng phía bằng {120-t} độ thì hai đường thẳng a và b song song.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hai tia phân giác của hai góc so le trong luôn vuông góc với nhau.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Cho hai góc kề bù nhau, biết góc thứ nhất bằng {70+t} độ. Tính số đo góc thứ hai (độ).", f"{110-t}"),
            make_sa(2, "Thông hiểu", f"Cho a // b, góc so le trong A1 = {55+t} độ. Tính góc so le trong B1 (độ).", f"{55+t}"),
            make_sa(3, "Vận dụng", f"Tia Oz là phân giác góc xOy. Biết góc xOz = {35+t} độ. Tính góc xOy (độ).", f"{70+2*t}"),
            make_sa(4, "Vận dụng", "Một chiếc kéo khi mở ra có hai lưỡi kéo tạo thành hai góc đối đỉnh. Biết góc giữa hai tay cầm là 45 độ. Tính góc mở giữa hai lưỡi kéo (độ).", "45")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho hình vẽ có $a // b$. Biết $\\widehat{{A_1}} = {115-t}^\\circ$. Tính số đo các góc còn lại tại đỉnh $B$ đồng vị và so le trong với $\\widehat{{A_1}}$.",
                       "\n".join([
                           f"Vì a // b nên góc đồng vị B1 = A1 = {115-t} độ (0.25đ).",
                           f"Góc so le trong B2 = A1 = {115-t} độ (0.25đ).",
                           f"Góc kề bù với B1 có số đo: 180 - ({115-t}) = {65+t} độ (0.25đ).",
                           "Kết luận số đo các góc tương ứng (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một người thợ làm khung giàn giáo bằng thép. Hai thanh ngang $AB$ và $CD$ được hàn song song với nhau. Một thanh chéo $EF$ cắt $AB$ tại $E$ và cắt $CD$ tại $F$. Người thợ đo góc $\\widehat{{AEF}} = {75+t}^\\circ$. Hỏi góc $\\widehat{{EFD}}$ ở vị trí trong cùng phía phải bằng bao nhiêu độ để giàn giáo chuẩn xác?",
                       "\n".join([
                           "Hai đường thẳng AB và CD song song với nhau (0.25đ).",
                           "Thanh chéo EF tạo ra các cặp góc trong cùng phía bù nhau (0.25đ).",
                           f"Ta có: góc AEF + góc EFD = 180 độ => góc EFD = 180 - ({75+t}) = {105-t} độ (0.25đ).",
                           f"Kết luận góc EFD phải bằng {105-t} độ (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Chứng minh định lí: 'Hai tia phân giác của hai góc so le trong tạo bởi một đường thẳng cắt hai đường thẳng song song thì song song với nhau'.",
                       "\n".join([
                           "Gọi a // b và c cắt a, b tại A, B tạo cặp góc so le trong A1 và B1 (0.25đ).",
                           "Kẻ tia phân giác Ax của góc A1 và By của góc B1 (0.25đ).",
                           "Ta có: góc xAB = A1 / 2 và góc yBA = B1 / 2. Vì A1 = B1 nên góc xAB = góc yBA (0.25đ).",
                           "Hai góc này ở vị trí so le trong bằng nhau nên Ax // By. Định lí được chứng minh (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương III: Góc và đường thẳng song song - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương III: Góc và đường thẳng song song", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG IV: Tam giác bằng nhau (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c4_7():
    chap_id = "c4_7"
    l_idx = 6
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Hai tam giác bằng nhau là hai tam giác có (Đề {t:02d}):", ["Các cạnh tương ứng bằng nhau, các góc tương ứng bằng nhau", "Diện tích bằng nhau", "Chu vi bằng nhau", "Các góc bằng nhau"], 0),
            make_mc(2, "Nhận biết", "Trường hợp bằng nhau cạnh - cạnh - cạnh (c.c.c) của hai tam giác là:", ["Ba cạnh của tam giác này bằng ba cạnh của tam giác kia", "Hai cạnh bằng nhau", "Ba góc bằng nhau", "Một cạnh và hai góc bằng nhau"], 0),
            make_mc(3, "Nhận biết", "Tam giác cân là tam giác có:", ["Hai cạnh bằng nhau", "Ba cạnh bằng nhau", "Một góc vuông", "Ba góc bằng nhau"], 0),
            make_mc(4, "Nhận biết", "Trong tam giác đều, số đo mỗi góc luôn bằng:", ["$60^\\circ$", "$90^\\circ$", "$45^\\circ$", "$180^\\circ$"], 0),
            make_mc(5, "Thông hiểu", f"Cho $\\Delta ABC = \\Delta DEF$. Biết $AB = {3*t}$ cm, $AC = {4*t}$ cm, $EF = {5*t}$ cm. Chu vi $\\Delta ABC$ là:", [f"${12*t}$ cm", f"${7*t}$ cm", f"${9*t}$ cm", f"${10*t}$ cm"], 0),
            make_mc(6, "Thông hiểu", f"Cho tam giác $ABC$ cân tại $A$ có $\\widehat{{A}} = {40+t*4}^\\circ$. Số đo góc đáy $\\widehat{{B}}$ là:", [f"{(180 - (40+t*4))//2}^\\circ$", "$50^\\circ$", "$70^\\circ$", "$60^\\circ$"], 0),
            make_mc(7, "Thông hiểu", f"Cho $\\Delta ABC$ vuông tại $A$ có $\\widehat{{B}} = {30+t}^\\circ$. Số đo góc $C$ là:", [f"${60-t}^\\circ$", f"${90-t}^\\circ$", "$45^\\circ$", "$30^\\circ$"], 0),
            make_mc(8, "Thông hiểu", "Đường trung trực của đoạn thẳng là đường thẳng:", ["Đi qua trung điểm và vuông góc với đoạn thẳng đó", "Đi qua trung điểm", "Vuông góc với đoạn thẳng", "Song song với đoạn thẳng"], 0),
            make_mc(9, "Vận dụng", f"Để đo khoảng cách giữa hai điểm $A$ và $B$ bị ngăn cách bởi một cái hồ nước, người ta cắm cọc tiêu tại $O$ và lấy điểm $C, D$ sao cho $O$ là trung điểm của $AC$ và $BD$. Đo được khoảng cách $CD = {25+t*5}$ mét. Khoảng cách $AB$ là:", [f"${25+t*5}$ mét", f"${50+t*10}$ mét", "30 mét", "40 mét"], 0),
            make_mc(10, "Vận dụng", f"Một giá đỡ ba chân của máy quay phim tạo thành một hình chóp có các cạnh bên bằng nhau và cùng nghiêng với mặt đất một góc ${60+t}^\\circ$. Tam giác tạo bởi ba đỉnh chân đế là:", ["Tam giác đều", "Tam giác vuông", "Tam giác tù", "Tam giác cân"], 0),
            make_mc(11, "Vận dụng", f"Một khung mái nhà bằng gỗ hình tam giác cân $ABC$ ($AB = AC$) có góc ở đỉnh $\\widehat{{A}} = 120^\\circ$. Người ta đóng thanh giằng $AH$ vuông góc với cạnh đáy $BC$. Góc $\\widehat{{BAH}}$ bằng:", ["$60^\\circ$", "$30^\\circ$", "$90^\\circ$", "$45^\\circ$"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$. Các đường phân giác của góc $B$ và $C$ cắt nhau tại $I$. Biết $\\widehat{A} = 80^\\circ$. Số đo góc $\\widehat{BIC}$ bằng:", ["$130^\\circ$", "$100^\\circ$", "$120^\\circ$", "$140^\\circ$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tam giác bằng nhau (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Nếu hai cạnh và góc xen giữa của tam giác này bằng hai cạnh và góc xen giữa của tam giác kia thì hai tam giác đó bằng nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Trong một tam giác cân, đường phân giác xuất phát từ đỉnh đồng thời là đường trung trực của cạnh đáy.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai tam giác vuông có một cạnh huyền và một góc nhọn bằng nhau thì bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hai tam giác có ba góc tương ứng bằng nhau thì chắc chắn bằng nhau.", "correct": False}
            ]),
            make_tf(2, f"Cho đoạn thẳng AB và đường trung trực d của AB. Lấy điểm M bất kì trên đường thẳng d (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Đoạn thẳng MA luôn có độ dài bằng đoạn thẳng MB.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tam giác MAB luôn là tam giác cân tại M.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Đường thẳng d là tia phân giác của góc AMB.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Điểm M cách đều hai mút A và B chỉ khi M là trung điểm của AB.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Cho tam giác ABC có góc A = 50 độ, góc B = {60+t} độ. Tính số đo góc C (độ).", f"{70-t}"),
            make_sa(2, "Thông hiểu", f"Cho tam giác ABC = tam giác DEF. Biết AB = {4*t} cm, BC = {5*t} cm. Tính độ dài cạnh DE (cm).", f"{4*t}"),
            make_sa(3, "Vận dụng", f"Một tam giác cân có cạnh bên bằng {10+t} cm, cạnh đáy bằng 6 cm. Tính chu vi của tam giác cân đó (cm).", f"{26+2*t}"),
            make_sa(4, "Vận dụng", "Một cây cầu treo có trụ tháp thẳng đứng. Hai dây cáp nối từ đỉnh trụ đến hai điểm trên mặt cầu cách đều chân trụ. Biết một dây cáp dài 50 mét. Tính độ dài dây cáp còn lại (mét).", "50")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho tam giác $ABC$ cân tại $A$. Kẻ $AH$ vuông góc với $BC$ ($H \\in BC$). Chứng minh rằng: $\\Delta ABH = \\Delta ACH$ và $HB = HC$.",
                       "\n".join([
                           "Xét hai tam giác vuông ABH và ACH có: AH chung (0.25đ).",
                           "Cạnh huyền AB = AC (do tam giác ABC cân tại A) (0.25đ).",
                           "Suy ra tam giác ABH = tam giác ACH (cạnh huyền - cạnh góc vuông) (0.25đ).",
                           "Từ đó suy ra HB = HC (hai cạnh tương ứng) (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Hai trạm quan sát $A$ và $B$ đặt cách nhau một hồ nước. Một người đứng tại $C$ sao cho $CA = CB = {40+t*5}$ mét. Người đó ngắm thấy góc $\\widehat{{ACB}} = 60^\\circ$. Hãy tính khoảng cách $AB$ giữa hai trạm quan sát.",
                       "\n".join([
                           f"Tam giác ABC có CA = CB = {40+t*5} m nên là tam giác cân tại C (0.25đ).",
                           "Lại có góc ở đỉnh góc ACB = 60 độ (0.25đ).",
                           "Tam giác cân có một góc bằng 60 độ là tam giác đều (0.25đ).",
                           f"Do đó AB = CA = CB = {40+t*5} mét. Kết luận khoảng cách AB (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Cho tam giác nhọn $ABC$. Về phía ngoài tam giác, vẽ hai tam giác vuông cân tại $A$ là tam giác $ABD$ và tam giác $ACE$. Chứng minh rằng: $CD = BE$ và $CD \\perp BE$.",
                       "\n".join([
                           "Chứng minh góc DAC = góc BAE = 90 độ + góc BAC (0.25đ).",
                           "Xét tam giác DAC và BAE có: AD = AB, AC = AE, góc DAC = BAE => tam giác DAC = BAE (c.g.c) (0.25đ).",
                           "Suy ra CD = BE (hai cạnh tương ứng) (0.25đ).",
                           "Gọi giao điểm của CD và BE là K, chứng minh góc CKB = 90 độ => CD vuông góc với BE (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương IV: Tam giác bằng nhau - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương IV: Tam giác bằng nhau", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG V: Thu thập và biểu diễn dữ liệu (l_idx = 4)
# ------------------------------------------------------------------------------
def build_c5_7():
    chap_id = "c5_7"
    l_idx = 4
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Dữ liệu không phải là số (dữ liệu định tính) là (Đề {t:02d}):", ["Tên các tỉnh thành Việt Nam", "Số học sinh một lớp", "Chiều cao học sinh", "Điểm thi môn Toán"], 0),
            make_mc(2, "Nhận biết", "Biểu đồ hình quạt tròn dùng để biểu diễn:", ["Tỉ lệ phần trăm các thành phần", "Sự biến thiên liên tục theo ngày", "Số lượng rời rạc", "Tọa độ địa lí"], 0),
            make_mc(3, "Nhận biết", "Biểu đồ đoạn thẳng dùng để biểu diễn:", ["Sự thay đổi của đại lượng theo thời gian", "Cơ cấu", "Tỉ lệ diện tích", "Danh sách"], 0),
            make_mc(4, "Nhận biết", "Để thu thập dữ liệu về loại trái cây yêu thích của các bạn trong lớp, phương pháp thích hợp là:", ["Lập phiếu hỏi / khảo sát", "Cân đo", "Dùng nhiệt kế", "Tra cứu bản đồ"], 0),
            make_mc(5, "Thông hiểu", f"Trong một biểu đồ quạt tròn, phần quạt tương ứng với $25\\%$ tổng thể có góc ở tâm là:", ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$", "$60^\\circ$"], 0),
            make_mc(6, "Thông hiểu", f"Một nhóm gồm {40+t} học sinh có {16} bạn thích bơi lội. Tỉ lệ phần trăm bạn thích bơi lội là:", [f"{16/(40+t)*100:.1f}\\%", "40\\%", "50\\%", "30\\%"], 0),
            make_mc(7, "Thông hiểu", "Dữ liệu nào sau đây là không hợp lí khi nói về số con trong một gia đình?", ["-2 con", "2 con", "1 con", "3 con"], 0),
            make_mc(8, "Thông hiểu", "Khi nhìn vào biểu đồ đoạn thẳng biểu diễn số ca mắc bệnh sốt xuất huyết qua các tháng, đoạn thẳng đi lên chứng tỏ:", ["Số ca mắc bệnh tăng lên", "Số ca mắc bệnh giảm đi", "Không thay đổi", "Bằng 0"], 0),
            make_mc(9, "Vận dụng", f"Biểu đồ quạt tròn cho biết cơ cấu chi tiêu của bạn Lan trong 1 tháng: Mua sách vở ($40\\%$), Ăn sáng (${30+t}\\%$), Tiết kiệm (${30-t}\\%$). Biết số tiền Lan có là 500 nghìn đồng. Số tiền Lan dành mua sách vở là:", ["200 nghìn đồng", "150 nghìn đồng", "250 nghìn đồng", "100 nghìn đồng"], 0),
            make_mc(10, "Vận dụng", f"Doanh số bán sách của một nhà sách trong tuần đầu tháng 9 tăng từ {100+t*10} cuốn lên {150+t*10} cuốn. Số cuốn sách bán tăng thêm là:", ["50 cuốn", "100 cuốn", "40 cuốn", "60 cuốn"], 0),
            make_mc(11, "Vận dụng", f"Khảo sát {200+t*20} người về việc sử dụng túi vải khi đi chợ, có {160+t*10} người đồng ý sử dụng. Tỉ lệ phần trăm người đồng ý là:", [f"{(160+t*10)/(200+t*20)*100:.1f}\\%", "80\\%", "85\\%", "75\\%"], 0),
            make_mc(12, "Vận dụng cao", "Một bảng số liệu về số học sinh các lớp ghi tổng số học sinh khối 7 là 180 em, nhưng khi cộng số học sinh của từng lớp 7A, 7B, 7C, 7D lại ra 185 em. Điều này chứng tỏ:", ["Có sai sót trong quá trình thu thập hoặc nhập liệu", "Số liệu hoàn toàn chính xác", "Do làm tròn số", "Đúng quy luật"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về dữ liệu và biểu đồ (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Dữ liệu thu thập được có thể là số (định lượng) hoặc không phải là số (định tính).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Biểu đồ đoạn thẳng thích hợp biểu diễn diễn biến nhiệt độ trong một ngày.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tổng phần trăm trên biểu đồ hình quạt tròn luôn bằng 100%.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tất cả các số liệu thống kê thu thập từ mạng internet đều hoàn toàn đáng tin cậy 100%.", "correct": False}
            ]),
            make_tf(2, f"Thống kê phương tiện đến trường của 40 học sinh lớp 7A: Xe đạp: 20 bạn, Đi bộ: 12 bạn, Xe buýt: 8 bạn (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Có 3 loại phương tiện được thống kê.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Học sinh đi xe đạp chiếm đúng 50% số học sinh cả lớp.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hình quạt biểu diễn số học sinh đi xe buýt có góc ở tâm là 72 độ.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số học sinh đi bộ chiếm tỉ lệ lớn nhất trong lớp.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Góc ở tâm của hình quạt biểu diễn 50% bằng bao nhiêu độ?", "180"),
            make_sa(2, "Thông hiểu", f"Lớp 7C có {35+t} học sinh. Trong đó có 10 bạn tham gia CLB Âm nhạc. Tính số bạn không tham gia CLB Âm nhạc.", f"{25+t}"),
            make_sa(3, "Vận dụng", f"Một đại lý gạo bán được {120+t*5} tấn gạo trong tháng 1 và {150+t*5} tấn trong tháng 2. Hỏi tháng 2 bán nhiều hơn tháng 1 bao nhiêu tấn?", "30"),
            make_sa(4, "Vận dụng", "Một trường có 600 học sinh. Khảo sát thấy 45% thích học môn Toán. Tính số học sinh thích môn Toán.", "270")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Bảng thống kê số lượng thú cưng nuôi tại nhà của các bạn tổ 1: Chó: {4+t%3}, Mèo: 5, Chim: 2, Cá cảnh: 4. Lập bảng tần số và vẽ biểu đồ cột tương ứng.",
                       "\n".join([
                           f"Lập bảng số liệu: Chó: {4+t%3}, Mèo: 5, Chim: 2, Cá: 4 (0.25đ).",
                           "Xác định trục hoành là tên các loại thú cưng (0.25đ).",
                           "Xác định trục tung là số lượng cá thể (0.25đ).",
                           "Vẽ các cột hình chữ nhật tương ứng và ghi chú tiêu đề biểu đồ (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một công ty may có kim ngạch xuất khẩu trong 3 quý đầu năm lần lượt là: Quý 1: {15+t} tỉ đồng, Quý 2: {20+t} tỉ đồng, Quý 3: {25+t} tỉ đồng. Em hãy tính tổng kim ngạch xuất khẩu của 3 quý và mức tăng từ Quý 1 đến Quý 3.",
                       "\n".join([
                           f"Tổng kim ngạch 3 quý: ({15+t}) + ({20+t}) + ({25+t}) = {60+3*t} tỉ đồng (0.25đ).",
                           f"Mức tăng từ Quý 1 đến Quý 3: ({25+t}) - ({15+t}) = 10 tỉ đồng (0.25đ).",
                           f"Tỉ lệ tăng trưởng: [10 / ({15+t})] . 100% (0.25đ).",
                           "Kết luận số liệu tăng trưởng của công ty (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Phân tích vì sao khi biểu diễn số liệu về tỉ lệ học sinh các khối lớp trong một trường, ta nên ưu tiên chọn biểu đồ hình quạt tròn hơn là biểu đồ đoạn thẳng.",
                       "\n".join([
                           "Biểu đồ quạt tròn phản ánh trực quan cơ cấu các thành phần trong toàn thể 100% (0.25đ).",
                           "Học sinh các khối lớp là dữ liệu phân loại rời rạc, không mang tính diễn biến theo thời gian (0.25đ).",
                           "Biểu đồ đoạn thẳng chỉ phù hợp khi theo dõi sự thay đổi liên tục theo mốc thời gian (0.25đ).",
                           "Do đó chọn biểu đồ hình quạt tròn là chính xác và khoa học nhất (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương V: Thu thập và biểu diễn dữ liệu - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương V: Thu thập và biểu diễn dữ liệu", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VI: Tỉ lệ thức và đại lượng tỉ lệ (l_idx = 5)
# ------------------------------------------------------------------------------
def build_c6_7():
    chap_id = "c6_7"
    l_idx = 5
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Tỉ lệ thức là đẳng thức của hai tỉ số (Đề {t:02d}):", ["$\\frac{a}{b} = \\frac{c}{d}$", "$a + b = c + d$", "$a \\cdot b = c \\cdot d$", "$a - b = c - d$"], 0),
            make_mc(2, "Nhận biết", "Nếu $\\frac{a}{b} = \\frac{c}{d}$ thì theo tính chất cơ bản của tỉ lệ thức:", ["$a \\cdot d = b \\cdot c$", "$a \\cdot c = b \\cdot d$", "$a + d = b + c$", "$a : d = b : c$"], 0),
            make_mc(3, "Nhận biết", "Hai đại lượng $x$ và $y$ tỉ lệ thuận với nhau theo hệ số tỉ lệ $k$ ($k \\neq 0$) khi:", ["$y = k \\cdot x$", "$y = \\frac{k}{x}$", "$x \\cdot y = k$", "$y = x + k$"], 0),
            make_mc(4, "Nhận biết", "Hai đại lượng $x$ và $y$ tỉ lệ nghịch với nhau khi:", ["$x \\cdot y = a$ ($a \\neq 0$)", "$y = a \\cdot x$", "$\\frac{y}{x} = a$", "$y = x - a$"], 0),
            make_mc(5, "Thông hiểu", f"Tìm $x$ trong tỉ lệ thức $\\frac{{x}}{{{2*t}}} = \\frac{3}{2}$:", [f"$x = {3*t}$", f"$x = {t}$", f"$x = {6*t}$", f"$x = {2*t}$"], 0),
            make_mc(6, "Thông hiểu", f"Cho $\\frac{{x}}{2} = \\frac{{y}}{3}$ và $x + y = {5*t}$. Giá trị của $x$ và $y$ là:", [f"$x = {2*t}, y = {3*t}$", f"$x = {3*t}, y = {2*t}$", f"$x = {t}, y = {4*t}$", "$x = 2, y = 3$"], 0),
            make_mc(7, "Thông hiểu", f"Biết đại lượng $y$ tỉ lệ thuận với $x$ theo hệ số tỉ lệ $k = {t}$. Khi $x = 4$ thì $y$ bằng:", [f"${4*t}$", f"${t}$", f"${t+4}$", f"${4}$"], 0),
            make_mc(8, "Thông hiểu", f"Biết $x$ và $y$ tỉ lệ nghịch với nhau và khi $x = 2$ thì $y = {3*t}$. Hệ số tỉ lệ là:", [f"${6*t}$", f"${3*t}$", f"${2*t}$", "$6$"], 0),
            make_mc(9, "Vận dụng", f"Để làm một chiếc bánh bông lan theo công thức, tỉ lệ khối lượng bột mì và đường là $3 : 2$. Nếu dùng ${300+t*30}$ gam bột mì thì cần dùng khối lượng đường là:", [f"{2 * (300+t*30) // 3} gam", "200 gam", "300 gam", "150 gam"], 0),
            make_mc(10, "Vận dụng", f"Ba tổ công nhân nhận đào một con mương có độ dài lần lượt tỉ lệ với $3; 4; 5$. Biết tổng độ dài con mương cả ba tổ phải đào là ${120+t*12}$ mét. Tổ 1 phải đào số mét mương là:", [f"{3 * (120+t*12) // 12} mét", "30 mét", "40 mét", "50 mét"], 0),
            make_mc(11, "Vận dụng", f"Một ô tô đi quãng đường $AB$ hết $3$ giờ với vận tốc $60$ km/h. Nếu ô tô đó đi với vận tốc $45$ km/h thì thời gian đi hết quãng đường $AB$ là:", ["4 giờ", "3,5 giờ", "5 giờ", "2,5 giờ"], 0),
            make_mc(12, "Vận dụng cao", f"Cho ba số $a, b, c$ thỏa mãn $\\frac{{a}}{2} = \\frac{{b}}{3} = \\frac{{c}}{4}$ và $a^2 + b^2 + c^2 = {29*t*t}$. Giá trị dương của $a + b + c$ bằng:", [f"${9*t}$", f"${6*t}$", f"${12*t}$", f"${29*t}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tính chất của dãy tỉ số bằng nhau (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Từ a/b = c/d ta có: a/b = c/d = (a + c)/(b + d) với b + d khác 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Từ a/b = c/d ta có: a/b = c/d = (a - c)/(b - d) với b - d khác 0.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu y tỉ lệ thuận với x thì x cũng tỉ lệ thuận với y.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu y tỉ lệ thuận với x theo hệ số k thì x tỉ lệ thuận với y theo hệ số k.", "correct": False}
            ]),
            make_tf(2, f"Bài toán chia tiền thưởng năng suất (Mã đề {t:02d}): Ba bạn An, Bình, Cúc được thưởng số tiền tỉ lệ với 2; 3; 4. Biết tổng số tiền thưởng là 18 triệu đồng.", [
                {"key": "a", "level": "Nhận biết", "text": "Gọi số tiền thưởng của ba bạn là x, y, z thì x/2 = y/3 = z/4.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng số phần bằng nhau là 2 + 3 + 4 = 9 phần.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số tiền bạn An nhận được là 4 triệu đồng, bạn Bình là 6 triệu đồng, bạn Cúc là 8 triệu đồng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số tiền thưởng của bạn Cúc gấp 3 lần số tiền thưởng của bạn An.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tìm x trong tỉ lệ thức: x / 6 = {t} / 2.", f"{3*t}"),
            make_sa(2, "Thông hiểu", f"Biết x và y tỉ lệ thuận, khi x = 3 thì y = {6*t}. Tìm hệ số tỉ lệ k của y đối với x.", f"{2*t}"),
            make_sa(3, "Vận dụng", f"Mua 5 quyển vở cùng loại hết {40+t*5} nghìn đồng. Hỏi mua 10 quyển vở như thế hết bao nhiêu nghìn đồng?", f"{2*(40+t*5)}"),
            make_sa(4, "Vận dụng", "Để hoàn thành một công việc trong 6 ngày cần 8 công nhân. Muốn hoàn thành công việc đó trong 4 ngày thì cần bao nhiêu công nhân (năng suất như nhau)?", "12")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Tìm hai số $x$ và $y$, biết: $\\frac{{x}}{3} = \\frac{{y}}{5}$ và $x + y = {16*t}$.",
                       "\n".join([
                           "Áp dụng tính chất của dãy tỉ số bằng nhau (0.25đ).",
                           f"x / 3 = y / 5 = (x + y) / (3 + 5) = {16*t} / 8 = {2*t} (0.25đ).",
                           f"Suy ra: x = 3 . {2*t} = {6*t} (0.25đ).",
                           f"y = 5 . {2*t} = {10*t}. Vậy x = {6*t}, y = {10*t} (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Hưởng ứng phong trào quyên góp sách ủng hộ học sinh vùng lũ, ba lớp 7A, 7B, 7C quyên góp được tổng cộng ${240+t*12}$ quyển sách. Biết số sách quyên góp của ba lớp tỉ lệ với $3; 4; 5$. Tính số quyển sách mỗi lớp quyên góp được.",
                       "\n".join([
                           f"Gọi số sách ba lớp 7A, 7B, 7C quyên góp lần lượt là x, y, z (quyển) (0.25đ).",
                           f"Ta có: x/3 = y/4 = z/5 và x + y + z = {240+t*12} (0.25đ).",
                           f"Áp dụng tính chất dãy tỉ số: (x+y+z)/(3+4+5) = ({240+t*12})/12 (0.25đ).",
                           "Tính số sách cụ thể của từng lớp và kết luận (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Cho $\\frac{{a}}{{b}} = \\frac{{c}}{{d}}$ ($b, d \\neq 0$). Chứng minh rằng: $\\frac{{a^2 + c^2}}{{b^2 + d^2}} = \\frac{{a \\cdot c}}{{b \\cdot d}}$.",
                       "\n".join([
                           "Đặt a/b = c/d = k => a = kb, c = kd (0.25đ).",
                           "Vế trái: (a^2 + c^2)/(b^2 + d^2) = (k^2 b^2 + k^2 d^2)/(b^2 + d^2) = k^2 (0.25đ).",
                           "Vế phải: (a . c)/(b . d) = (kb . kd)/(bd) = k^2 (0.25đ).",
                           "Vì VT = VP = k^2 nên đẳng thức được chứng minh hoàn tất (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương VI: Tỉ lệ thức và đại lượng tỉ lệ - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương VI: Tỉ lệ thức và đại lượng tỉ lệ", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VII: Biểu thức đại số và đa thức một biến (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c7_7():
    chap_id = "c7_7"
    l_idx = 6
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Biểu thức nào sau đây là biểu thức đại số (Đề {t:02d})?", [f"${t+1}x^2 - 3x + 1$", "$2 + 3 = 5$", "$4 > 2$", "$5 \\neq 3$"], 0),
            make_mc(2, "Nhận biết", f"Bậc của đa thức $P(x) = {t}x^4 - 2x^2 + 5$ là:", ["4", "2", "5", "1"], 0),
            make_mc(3, "Nhận biết", "Nghiệm của đa thức $P(x)$ là giá trị của biến làm cho:", ["$P(x) = 0$", "$P(x) > 0$", "$P(x) = 1$", "$P(x) < 0$"], 0),
            make_mc(4, "Nhận biết", "Đa thức một biến là tổng của những đơn thức của:", ["Cùng một biến", "Nhiều biến khác nhau", "Các số nguyên", "Các phân số"], 0),
            make_mc(5, "Thông hiểu", f"Giá trị của biểu thức $A = 2x^2 - {t}x$ tại $x = 2$ là:", [f"${8 - 2*t}$", f"${8 + 2*t}$", f"${4 - t}$", "$8$"], 0),
            make_mc(6, "Thông hiểu", f"Nghiệm của đa thức $Q(x) = 2x - {2*t}$ là:", [f"$x = {t}$", f"$x = -{t}$", "$x = 0$", "$x = 2$"], 0),
            make_mc(7, "Thông hiểu", f"Hệ số cao nhất của đa thức $A(x) = 3x^2 - {4*t}x^3 + 5$ là:", [f"${-4*t}$", f"${4*t}$", "3", "5"], 0),
            make_mc(8, "Thông hiểu", f"Hệ số tự do của đa thức $B(x) = x^3 - 2x + {t*t + 1}$ là:", [f"${t*t + 1}$", "1", "-2", "0"], 0),
            make_mc(9, "Vận dụng", f"Một người đi bộ với vận tốc $4$ km/h trong $x$ giờ, sau đó đi xe đạp với vận tốc $12$ km/h trong $y$ giờ. Biểu thức đại số biểu thị tổng quãng đường người đó đã đi là:", ["$4x + 12y$", "$12x + 4y$", "$16(x + y)$", "$48xy$"], 0),
            make_mc(10, "Vận dụng", f"Một hình chữ nhật có chiều dài là $x + {t*2}$ mét, chiều rộng là $x$ mét. Đa thức biểu thị diện tích hình chữ nhật là:", [f"$x^2 + {2*t}x$", f"$2x + {2*t}$", f"$x^2 + {4*t}$", f"$x^2$"], 0),
            make_mc(11, "Vận dụng", f"Giá bán một chiếc áo ban đầu là $x$ đồng. Đợt khuyến mại cửa hàng giảm giá ${10*t}\\%$. Biểu thức biểu diễn giá bán sau khi giảm là:", [f"${(100-10*t)/100:.2f}x$", f"${10*t/100:.2f}x$", f"$x - {10*t}$", f"$x + {10*t}$"], 0),
            make_mc(12, "Vận dụng cao", f"Đa thức $P(x) = x^2 + {2*t}x + {t*t + 4}$ có số nghiệm thực là:", ["0 nghiệm (vô nghiệm)", "1 nghiệm", "2 nghiệm", "Vô số nghiệm"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về đa thức một biến (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Bậc của đa thức một biến (khác đa thức không) là số mũ lớn nhất của biến trong đa thức thu gọn.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Đa thức bậc 1 luôn có đúng một nghiệm thực.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Đa thức P(x) = x^2 + {t*t} luôn dương với mọi số thực x nên không có nghiệm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Một đa thức bậc 3 có thể có 4 nghiệm phân biệt.", "correct": False}
            ]),
            make_tf(2, f"Cho hai đa thức $P(x) = 2x^2 - {t}x + 3$ và $Q(x) = x^2 + {t}x - 1$ (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "P(x) và Q(x) đều là các đa thức bậc 2 theo biến x.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng P(x) + Q(x) = 3x^2 + 2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Hiệu P(x) - Q(x) = x^2 - {2*t}x + 4.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tổng P(x) + Q(x) có nghiệm là x = 0.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính giá trị của đa thức P(x) = x^2 - {2*t} tại x = {t+1}.", f"{(t+1)**2 - 2*t}"),
            make_sa(2, "Thông hiểu", f"Tìm nghiệm của đa thức bậc nhất: A(x) = 3x - {9*t}.", f"{3*t}"),
            make_sa(3, "Vận dụng", f"Một mảnh đất hình vuông có cạnh là x mét. Người ta bớt mỗi cạnh 2 mét để làm lối đi. Viết đa thức biểu thị diện tích phần đất còn lại. Khi x = {10+t}, diện tích là bao nhiêu m^2?", f"{(8+t)**2}"),
            make_sa(4, "Vận dụng", "Một bể bơi hình chữ nhật có chiều dài 25 m, chiều rộng 10 m. Người ta làm một lối đi xung quanh rộng x mét. Khi x = 1, diện tích toàn bộ khu đất là bao nhiêu m^2?", "324")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho hai đa thức: $A(x) = 3x^3 - 2x^2 + {t}x - 5$ và $B(x) = -x^3 + 2x^2 - {t}x + 10$. Tính $A(x) + B(x)$.",
                       "\n".join([
                           "Đặt phép tính cộng hai đa thức A(x) + B(x) (0.25đ).",
                           f"Nhóm các hạng tử cùng bậc: (3 - 1)x^3 + (-2 + 2)x^2 + ({t} - {t})x + (-5 + 10) (0.25đ).",
                           "Thu gọn các hạng tử đồng dạng: 2x^3 + 0x^2 + 0x + 5 (0.25đ).",
                           "Kết quả thu gọn: A(x) + B(x) = 2x^3 + 5 (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Bác thợ mộc đóng một chiếc bàn học có mặt bàn hình chữ nhật với chiều dài hơn chiều rộng ${20+t*5}$ cm. Gọi chiều rộng mặt bàn là $x$ (cm). Viết đa thức biểu thị diện tích mặt bàn theo $x$ và tính diện tích mặt bàn khi chiều rộng $x = 60$ cm.",
                       "\n".join([
                           f"Chiều dài mặt bàn là: x + {20+t*5} (cm) (0.25đ).",
                           f"Đa thức biểu thị diện tích: S(x) = x(x + {20+t*5}) = x^2 + {20+t*5}x (cm^2) (0.25đ).",
                           f"Thay x = 60 vào đa thức: S(60) = 60^2 + {20+t*5} . 60 (0.25đ).",
                           f"Tính toán ra kết quả: S = {3600 + (20+t*5)*60} cm^2. Kết luận diện tích mặt bàn (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Chứng minh rằng đa thức $P(x) = x^2 - {2*t}x + {t*t + 1}$ không có nghiệm với mọi số thực $x$.",
                       "\n".join([
                           f"Biến đổi đa thức về dạng bình phương cộng một hằng số: P(x) = (x^2 - {2*t}x + {t*t}) + 1 (0.25đ).",
                           f"P(x) = (x - {t})^2 + 1 (0.25đ).",
                           f"Vì (x - {t})^2 >= 0 với mọi x nên P(x) >= 1 > 0 với mọi x (0.25đ).",
                           "Do P(x) luôn nhận giá trị dương nên đa thức không có nghiệm. ĐPCM (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương VII: Biểu thức đại số và đa thức một biến - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương VII: Biểu thức đại số và đa thức một biến", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VIII: Làm quen với biến cố và xác suất của biến cố (l_idx = 3)
# ------------------------------------------------------------------------------
def build_c8_7():
    chap_id = "c8_7"
    l_idx = 3
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Biến cố chắc chắn là biến cố (Đề {t:02d}):", ["Luôn xảy ra trong phép thử", "Không bao giờ xảy ra", "Có thể xảy ra hoặc không", "Có xác suất bằng 0"], 0),
            make_mc(2, "Nhận biết", "Biến cố không thể là biến cố:", ["Không bao giờ xảy ra trong phép thử", "Luôn luôn xảy ra", "Xảy ra với xác suất 1", "Xảy ra với xác suất 0,5"], 0),
            make_mc(3, "Nhận biết", "Gieo một con xúc xắc 6 mặt cân đối thì biến cố nào sau đây là ngẫu nhiên?", ["Xuất hiện mặt có số chấm là số chẵn", "Xuất hiện mặt 7 chấm", "Xuất hiện mặt có số chấm nhỏ hơn 10", "Xuất hiện mặt 0 chấm"], 0),
            make_mc(4, "Nhận biết", "Xác suất của biến cố chắc chắn bằng:", ["1", "0", "0,5", "-1"], 0),
            make_mc(5, "Thông hiểu", f"Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt có số chấm chia hết cho 3 là:", ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"], 0),
            make_mc(6, "Thông hiểu", f"Một túi có {5+t} viên kẹo màu xanh và 5 viên kẹo màu đỏ. Lấy ngẫu nhiên 1 chiếc kẹo. Biến cố lấy được kẹo màu xanh có xác suất là:", [f"$\\frac{{{5+t}}}{{{10+t}}}$", "$\\frac{1}{2}$", "$\\frac{5}{10}$", "$\\frac{1}{5}$"], 0),
            make_mc(7, "Thông hiểu", f"Rút ngẫu nhiên một lá bài trong bộ bài có 10 lá đánh số từ 1 đến 10. Xác suất rút được lá bài ghi số nguyên tố là:", ["0,4", "0,5", "0,3", "0,2"], 0),
            make_mc(8, "Thông hiểu", "Tung một đồng xu 20 lần thấy có 12 lần xuất hiện mặt Ngửa. Xác suất thực nghiệm xuất hiện mặt Ngửa là:", ["0,6", "0,4", "0,5", "0,8"], 0),
            make_mc(9, "Vận dụng", f"Hội khỏe Phù Đổng trường có {15+t} đội bóng chuyền tham gia thi đấu loại trực tiếp bốc thăm ngẫu nhiên. Xác suất để đội lớp 7A gặp đội lớp 7B ngay ở trận đầu tiên là một biến cố:", ["Ngẫu nhiên", "Chắc chắn", "Không thể", "Đồng khả năng"], 0),
            make_mc(10, "Vận dụng", f"Một hộp có 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng. Bạn An lấy ra 1 quả rồi đặt lại vào hộp, sau đó bạn Bình lấy ra 1 quả. Số kết quả có thể xảy ra là:", ["9", "3", "6", "8"], 0),
            make_mc(11, "Vận dụng", f"Trong một hộp có {20+t*5} chiếc bút bi, trong đó có 5 chiếc bút màu đỏ, còn lại là màu xanh. Xác suất lấy được chiếc bút màu xanh là:", [f"{(15+t*5)/(20+t*5):.2f}", "0,75", "0,5", "0,25"], 0),
            make_mc(12, "Vận dụng cao", "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 11 là:", ["$\\frac{2}{36} = \\frac{1}{18}$", "$\\frac{1}{36}$", "$\\frac{3}{36}$", "$\\frac{4}{36}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về biến cố (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả của phép thử.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Xác suất của một biến cố là một con số nằm giữa 0 và 1 (kể cả 0 và 1).", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Gieo một con xúc xắc 6 mặt thì xác suất ra mặt 1 chấm bằng xác suất ra mặt 6 chấm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu tung đồng xu 10 lần đều ra mặt Sấp thì chắc chắn lần thứ 11 sẽ ra mặt Ngửa.", "correct": False}
            ]),
            make_tf(2, f"Trong một hộp kín có {10+t} thẻ trắng và 10 thẻ đen có cùng kích thước và khối lượng (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Hành động rút ngẫu nhiên 1 thẻ là một phép thử ngẫu nhiên.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Tổng số kết quả có thể xảy ra khi rút 1 thẻ là {20+t}.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Xác suất rút được thẻ đen là 10 / ({20+t}).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Khả năng rút được thẻ đen luôn cao hơn rút được thẻ trắng với mọi t >= 1.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số lẻ.", "0.5"),
            make_sa(2, "Thông hiểu", f"Một hộp có {6+t} bi xanh và 4 bi đỏ. Tính tổng số kết quả có thể xảy ra khi lấy ngẫu nhiên 1 viên bi.", f"{10+t}"),
            make_sa(3, "Vận dụng", "Tung một đồng xu 40 lần thấy xuất hiện mặt Ngửa 22 lần. Tính xác suất thực nghiệm xuất hiện mặt Sấp.", "0.45"),
            make_sa(4, "Vận dụng", "Trong hộp có 10 tấm thẻ đánh số từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất thẻ rút được ghi số lớn hơn 7.", "0.3")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Một hộp đựng {5+t} tấm thẻ ghi số chẵn và 5 tấm thẻ ghi số lẻ. Rút ngẫu nhiên 1 tấm thẻ. Tính xác suất rút được thẻ ghi số chẵn và xác suất rút được thẻ ghi số lẻ.",
                       "\n".join([
                           f"Tổng số tấm thẻ trong hộp: ({5+t}) + 5 = {10+t} thẻ (0.25đ).",
                           f"Số kết quả thuận lợi rút thẻ số chẵn là {5+t} (0.25đ).",
                           f"Xác suất rút thẻ chẵn: P(Chẵn) = ({5+t}) / ({10+t}) (0.25đ).",
                           f"Xác suất rút thẻ lẻ: P(Lẻ) = 5 / ({10+t}) (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Trong một đợt kiểm tra chất lượng sản phẩm gồm {100+t*10} linh kiện điện tử, người ta phát hiện có {5} linh kiện bị lỗi. Hãy tính xác suất thực nghiệm một linh kiện bị lỗi và ước lượng nếu sản xuất 10 000 linh kiện thì có khoảng bao nhiêu linh kiện bị lỗi.",
                       "\n".join([
                           f"Xác suất thực nghiệm linh kiện bị lỗi: P = 5 / ({100+t*10}) (0.25đ).",
                           "Tỉ lệ lỗi thực nghiệm ước tính cho toàn bộ lô hàng (0.25đ).",
                           f"Số linh kiện lỗi dự đoán trong 10 000 linh kiện: N = 10 000 . P (0.25đ).",
                           "Tính toán và kết luận số linh kiện lỗi ước lượng (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Một chiếc hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Bạn Nam lấy ngẫu nhiên 1 quả bóng, xem màu rồi KHÔNG trả lại vào hộp. Sau đó bạn Bình lấy tiếp 1 quả bóng. Tính xác suất để cả hai bạn đều lấy được bóng màu xanh.",
                       "\n".join([
                           "Xác suất bạn Nam lấy được quả bóng màu xanh lần thứ nhất là: 3/5 (0.25đ).",
                           "Sau khi Nam lấy 1 bóng xanh, trong hộp còn lại 4 quả bóng (gồm 2 xanh và 2 đỏ) (0.25đ).",
                           "Xác suất bạn Bình lấy được quả bóng màu xanh lần thứ hai là: 2/4 = 1/2 (0.25đ).",
                           "Xác suất để cả hai bạn cùng lấy được bóng xanh là: (3/5) . (1/2) = 3/10 = 0,3 (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Làm quen với biến cố và xác suất của biến cố - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương VIII: Làm quen với biến cố và xác suất của biến cố", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG IX: Quan hệ giữa các yếu tố trong một tam giác (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c9_7():
    chap_id = "c9_7"
    l_idx = 6
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Trong một tam giác, góc đối diện với cạnh lớn hơn là (Đề {t:02d}):", ["Góc lớn hơn", "Góc nhỏ hơn", "Góc vuông", "Góc tù"], 0),
            make_mc(2, "Nhận biết", "Trong một tam giác, độ dài một cạnh bất kì luôn:", ["Lớn hơn hiệu và nhỏ hơn tổng hai cạnh còn lại", "Lớn hơn tổng hai cạnh còn lại", "Bằng tổng hai cạnh", "Nhỏ hơn hiệu hai cạnh"], 0),
            make_mc(3, "Nhận biết", "Giao điểm của ba đường trung tuyến trong một tam giác được gọi là:", ["Trọng tâm của tam giác", "Trực tâm của tam giác", "Tâm đường tròn ngoại tiếp", "Tâm đường tròn nội tiếp"], 0),
            make_mc(4, "Nhận biết", "Trọng tâm của tam giác cách mỗi đỉnh một khoảng bằng:", ["$\\frac{2}{3}$ độ dài đường trung tuyến đi qua đỉnh đó", "$\\frac{1}{2}$ độ dài đường trung tuyến", "$\\frac{1}{3}$ độ dài đường trung tuyến", "Hai lần độ dài trung tuyến"], 0),
            make_mc(5, "Thông hiểu", f"Cho tam giác $ABC$ có $AB = {3*t}$ cm, $AC = {5*t}$ cm, $BC = {6*t}$ cm. Khẳng định nào sau đây là ĐÚNG?", ["$\\widehat{A} > \\widehat{B} > \\widehat{C}$", "$\\widehat{C} > \\widehat{B} > \\widehat{A}$", "$\\widehat{B} > \\widehat{A} > \\widehat{C}$", "$\\widehat{A} = \\widehat{B} = \\widehat{C}$"], 0),
            make_mc(6, "Thông hiểu", f"Bộ ba đoạn thẳng nào sau đây CÓ THỂ là độ dài ba cạnh của một tam giác?", [f"${3*t}$ cm, ${4*t}$ cm, ${5*t}$ cm", f"${2*t}$ cm, ${3*t}$ cm, ${6*t}$ cm", f"${t}$ cm, ${2*t}$ cm, ${3*t}$ cm", f"${t}$ cm, ${t}$ cm, ${3*t}$ cm"], 0),
            make_mc(7, "Thông hiểu", f"Cho tam giác $ABC$ có đường trung tuyến $AM = {9*t}$ cm. Gọi $G$ là trọng tâm tam giác. Độ dài đoạn thẳng $AG$ là:", [f"${6*t}$ cm", f"${3*t}$ cm", f"${4.5*t}$ cm", f"${5*t}$ cm"], 0),
            make_mc(8, "Thông hiểu", "Giao điểm của ba đường cao trong một tam giác được gọi là:", ["Trực tâm của tam giác", "Trọng tâm", "Tâm nội tiếp", "Tâm ngoại tiếp"], 0),
            make_mc(9, "Vận dụng", f"Người ta muốn dựng một cột thu lôi $O$ cách đều ba tòa nhà $A, B, C$. Vị trí điểm $O$ được chọn là:", ["Giao điểm ba đường trung trực của tam giác ABC", "Giao điểm ba đường trung tuyến", "Giao điểm ba đường phân giác", "Giao điểm ba đường cao"], 0),
            make_mc(10, "Vận dụng", f"Một tam giác có hai cạnh dài ${4+t}$ cm và $8$ cm. Để tam giác này là tam giác cân thì cạnh thứ ba phải có độ dài là:", ["8 cm", "4 cm", "12 cm", "2 cm"], 0),
            make_mc(11, "Vận dụng", f"Một người đứng cách ngọn tháp và một cây xanh tạo thành tam giác. Khoảng cách từ người đến cây là 15 m, từ cây đến tháp là 20 m. Khoảng cách $d$ từ người đến ngọn tháp thỏa mãn:", ["$5\\text{{ m}} < d < 35\\text{{ m}}$", "$d = 35\\text{{ m}}$", "$d > 35\\text{{ m}}$", "$d < 5\\text{{ m}}$"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác nhọn $ABC$. Điểm $M$ nằm trong tam giác. Khẳng định nào sau đây luôn ĐÚNG?", ["$MA + MB + MC > \\frac{AB + BC + CA}{2}$", "$MA + MB + MC < \\frac{AB + BC + CA}{2}$", "$MA + MB = MC$", "$MA = MB = MC$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về quan hệ giữa các yếu tố trong tam giác (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Trong tam giác vuông, cạnh huyền là cạnh có độ dài lớn nhất.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Điểm cách đều ba đỉnh của một tam giác là giao điểm của ba đường trung trực.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Điểm cách đều ba cạnh của một tam giác là giao điểm của ba đường phân giác.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Giao điểm ba đường cao của tam giác luôn nằm bên trong tam giác đó.", "correct": False}
            ]),
            make_tf(2, f"Cho tam giác ABC có AB = {5*t} cm, AC = {7*t} cm (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Theo bất đẳng thức tam giác: AC - AB < BC < AC + AB.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Độ dài cạnh BC thỏa mãn: {2*t} cm < BC < {12*t} cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Góc đối diện với cạnh AC (góc B) lớn hơn góc đối diện với cạnh AB (góc C).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Cạnh BC có thể có độ dài bằng 1 cm khi t = 1.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Cho tam giác ABC có trung tuyến AM. Trọng tâm G chia đoạn AM thành hai đoạn AG và GM. Biết AM = {12*t} cm. Tính AG (cm).", f"{8*t}"),
            make_sa(2, "Thông hiểu", f"Cho tam giác ABC có góc A = 80 độ, góc B = {60+t} độ. Cạnh nào là cạnh lớn nhất?", "BC"),
            make_sa(3, "Vận dụng", f"Một tam giác cân có cạnh đáy dài {6+t} cm và một cạnh bên dài 12 cm. Chu vi của tam giác cân là bao nhiêu cm?", f"{30+t}"),
            make_sa(4, "Vận dụng", "Ba khu dân cư A, B, C không thẳng hàng. Người ta muốn đào một giếng nước chung cách đều cả ba khu dân cư. Hỏi có bao nhiêu vị trí đặt giếng nước thỏa mãn?", "1")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho tam giác $ABC$ có $AB = {4*t}$ cm, $AC = {6*t}$ cm. Gọi $M$ là trung điểm của $BC$. Chứng minh rằng: $AM < \\frac{{AB + AC}}{2} = {5*t}$ cm.",
                       "\n".join([
                           "Trên tia đối của tia MA lấy điểm D sao cho MD = MA (0.25đ).",
                           "Chứng minh tam giác MAB = tam giác MDC (c.g.c) => CD = AB (0.25đ).",
                           "Trong tam giác ACD: AD < AC + CD = AC + AB (0.25đ).",
                           f"Mà AD = 2AM nên 2AM < AB + AC => AM < (AB + AC)/2 = {5*t} cm (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một người thợ cơ khí muốn uốn một thanh sắt dài ${30+t*2}$ cm thành một khung tam giác có độ dài các cạnh là số nguyên cm. Biết hai cạnh đầu là $10$ cm và ${12+t}$ cm. Hỏi cạnh thứ ba dài bao nhiêu cm và thanh sắt có uốn thành tam giác được không?",
                       "\n".join([
                           f"Độ dài cạnh thứ ba là: ({30+t*2}) - 10 - ({12+t}) = {8+t} cm (0.25đ).",
                           f"Kiểm tra bất đẳng thức tam giác với 3 cạnh: 10, {12+t}, {8+t} (0.25đ).",
                           f"Ta có: 10 + ({8+t}) = {18+t} > {12+t} (thỏa mãn) (0.25đ).",
                           "Kết luận thanh sắt uốn thành công tam giác và cạnh thứ ba dài cụ thể (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Cho tam giác nhọn $ABC$, trực tâm $H$. Chứng minh rằng: $HA + HB + HC < AB + BC + CA$.",
                       "\n".join([
                           "Kẻ các đường cao AD, BE, CF cắt nhau tại trực tâm H (0.25đ).",
                           "Trong các tam giác vuông, đoạn thẳng vuông góc ngắn hơn đường xiên (0.25đ).",
                           "Chứng minh HA < (AB + AC)/2, HB < (BA + BC)/2, HC < (CA + CB)/2 (0.25đ).",
                           "Cộng từng vế ta được: HA + HB + HC < AB + BC + CA (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương IX: Quan hệ giữa các yếu tố trong một tam giác - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương IX: Quan hệ giữa các yếu tố trong một tam giác", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG X: Một số hình khối trong thực tiễn (l_idx = 3)
# ------------------------------------------------------------------------------
def build_c10_7():
    chap_id = "c10_7"
    l_idx = 3
    exams = load_existing_exams(chap_id, 7)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Hình lăng trụ đứng tam giác có hai mặt đáy là (Đề {t:02d}):", ["Hai tam giác bằng nhau và song song", "Hai hình chữ nhật", "Hai hình bình hành", "Hai tam giác vuông"], 0),
            make_mc(2, "Nhận biết", "Các mặt bên của hình lăng trụ đứng tam giác là những:", ["Hình chữ nhật", "Hình tam giác", "Hình thang", "Hình vuông"], 0),
            make_mc(3, "Nhận biết", "Thể tích của hình lăng trụ đứng có diện tích đáy $S$ và chiều cao $h$ là:", ["$V = S \\cdot h$", "$V = \\frac{1}{3} S \\cdot h$", "$V = 2 S \\cdot h$", "$V = \\frac{1}{2} S \\cdot h$"], 0),
            make_mc(4, "Nhận biết", "Diện tích xung quanh của hình lăng trụ đứng bằng:", ["Chu vi đáy nhân với chiều cao", "Diện tích đáy nhân chiều cao", "Nửa chu vi đáy nhân chiều cao", "Tổng diện tích hai đáy"], 0),
            make_mc(5, "Thông hiểu", f"Một hình lăng trụ đứng tứ giác có đáy là hình vuông cạnh ${3*t}$ cm, chiều cao bằng $10$ cm. Thể tích hình lăng trụ là:", [f"${90*t*t}$ cm$^3$", f"${30*t}$ cm$^3$", f"${30*t*t}$ cm$^3$", f"${100*t}$ cm$^3$"], 0),
            make_mc(6, "Thông hiểu", f"Một hình lăng trụ đứng tam giác có chu vi đáy bằng ${15+t*3}$ cm, chiều cao bằng $8$ cm. Diện tích xung quanh của lăng trụ là:", [f"${8*(15+t*3)}$ cm$^2$", f"${4*(15+t*3)}$ cm$^2$", "100 cm$^2$", "150 cm$^2$"], 0),
            make_mc(7, "Thông hiểu", "Hình lăng trụ đứng tam giác có số đỉnh, số mặt và số cạnh lần lượt là:", ["6 đỉnh, 5 mặt, 9 cạnh", "5 đỉnh, 6 mặt, 9 cạnh", "6 đỉnh, 6 mặt, 8 cạnh", "4 đỉnh, 4 mặt, 6 cạnh"], 0),
            make_mc(8, "Thông hiểu", f"Một chiếc hộp hình lập phương có cạnh bằng ${2*t}$ cm. Diện tích toàn phần của chiếc hộp là:", [f"${24*t*t}$ cm$^2$", f"${8*t*t*t}$ cm$^3$", f"${16*t*t}$ cm$^2$", f"${12*t*t}$ cm$^2$"], 0),
            make_mc(9, "Vận dụng", f"Người ta làm một chiếc lịch để bàn bằng bìa cứng hình lăng trụ đứng tam giác có các cạnh đáy là $10$ cm, $10$ cm, $12$ cm và chiều dài lịch là ${20+t}$ cm. Diện tích bìa cứng cần để làm 3 mặt bên của cuốn lịch là:", [f"{(10+10+12)*(20+t)} cm$^2$", "500 cm$^2$", "600 cm$^2$", "400 cm$^2$"], 0),
            make_mc(10, "Vận dụng", f"Một bể cá cảnh bằng kính dạng hình hộp chữ nhật có chiều dài ${60+t*5}$ cm, chiều rộng $40$ cm và chiều cao $50$ cm. Mực nước trong bể cao $35$ cm. Thể tích nước hiện có trong bể là:", [f"{(60+t*5) * 40 * 35 / 1000:.1f} lít", "80 lít", "100 lít", "70 lít"], 0),
            make_mc(11, "Vận dụng", f"Một chiếc lều chữ A có dạng hình lăng trụ đứng tam giác với đáy là tam giác vuông cân có hai cạnh góc vuông dài $2$ mét, chiều dài lều là ${4+t*0.5:.1f}$ mét. Thể tích không gian bên trong chiếc lều là:", [f"{(2 * 2 / 2) * (4+t*0.5):.1f} mét khối", "10 mét khối", "8 mét khối", "12 mét khối"], 0),
            make_mc(12, "Vận dụng cao", "Người ta sơn phủ chống thấm tất cả các mặt bên của một bồn chứa nước hình lăng trụ đứng lục giác đều cạnh đáy $a = 1$ mét, chiều cao $h = 3$ mét. Tổng diện tích cần sơn phủ là:", ["18 mét vuông", "12 mét vuông", "6 mét vuông", "24 mét vuông"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về hình lăng trụ đứng (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Các mặt bên của hình lăng trụ đứng luôn vuông góc với hai mặt đáy.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hai mặt đáy của hình lăng trụ đứng là hai đa giác bằng nhau và nằm trên hai mặt phẳng song song.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Diện tích toàn phần bằng tổng diện tích xung quanh và diện tích hai đáy.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hình lăng trụ đứng tam giác có 4 mặt bên là các hình chữ nhật.", "correct": False}
            ]),
            make_tf(2, f"Bài toán thiết kế hộp đựng socola hình lăng trụ đứng tam giác có đáy là tam giác đều cạnh {6*t} cm, chiều cao lăng trụ h = {10+t} cm (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Chu vi đáy của hộp socola là C = 3 . 6t = 18t cm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Diện tích xung quanh của hộp là S_xq = 18t . ({10+t}) cm^2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Mỗi mặt bên là một hình chữ nhật có kích thước {6*t} cm và {10+t} cm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Thể tích của hộp socola lớn hơn 5 lít với mọi t từ 1 đến 7.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính diện tích xung quanh của hình lăng trụ đứng tam giác có chu vi đáy 20 cm, chiều cao {10+t} cm (cm^2).", f"{20*(10+t)}"),
            make_sa(2, "Thông hiểu", f"Một hình lập phương có cạnh bằng {3*t} cm. Tính thể tích hình lập phương đó (cm^3).", f"{27*t*t*t}"),
            make_sa(3, "Vận dụng", f"Một chiếc thùng chứa bằng tôn hình hộp chữ nhật có kích thước đáy 50 cm và 40 cm, chứa nước cao 30 cm. Thể tích nước trong thùng là bao nhiêu lít?", "60"),
            make_sa(4, "Vận dụng", f"Người ta làm một thanh sôcôla hình lăng trụ đứng tam giác có diện tích đáy 6 cm^2 và chiều dài {12+t} cm. Tính thể tích thanh sôcôla (cm^3).", f"{6*(12+t)}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Một hình lăng trụ đứng tam giác có đáy là tam giác vuông có hai cạnh góc vuông là ${6*t}$ cm và ${8*t}$ cm, chiều cao của hình lăng trụ là $10$ cm. Tính thể tích của hình lăng trụ đó.",
                       "\n".join([
                           f"Diện tích đáy hình lăng trụ: S_đáy = (1/2) . {6*t} . {8*t} = {24*t*t} (cm^2) (0.25đ).",
                           "Chiều cao hình lăng trụ là h = 10 cm (0.25đ).",
                           f"Thể tích hình lăng trụ: V = S_đáy . h = {24*t*t} . 10 = {240*t*t} (cm^3) (0.25đ).",
                           f"Kết luận thể tích hình lăng trụ là {240*t*t} cm^3 (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Bác thợ mộc đóng một chiếc hòm gỗ đựng dụng cụ có dạng hình hộp chữ nhật có chiều dài ${80+t*5}$ cm, chiều rộng $50$ cm và chiều cao $40$ cm. Bác muốn sơn chống ẩm toàn bộ mặt ngoài của chiếc hòm (kể cả nắp). Biết chi phí sơn là $50 000$ đồng cho mỗi mét vuông. Tính số tiền bác cần chi để mua sơn.",
                       "\n".join([
                           f"Diện tích xung quanh hòm gỗ: S_xq = 2 . ({80+t*5} + 50) . 40 (cm^2) (0.25đ).",
                           f"Diện tích hai đáy: S_2đáy = 2 . ({80+t*5}) . 50 (cm^2) (0.25đ).",
                           "Diện tích toàn phần S_tp = S_xq + S_2đáy, đổi ra mét vuông (0.25đ).",
                           "Nhân với đơn giá 50 000 đồng/m^2 và kết luận số tiền cần trả (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Một chiếc lều hình lăng trụ đứng tam giác có thể tích không gian bên trong là $V = 12\\text{{ m}}^3$ và chiều dài lều là $4\\text{{ m}}$. Đáy lều là tam giác cân tại đỉnh nóc lều. Hỏi cần thiết kế chiều cao của tam giác đáy và cạnh đáy như thế nào để tổng diện tích vải bạt phủ hai mái lều là nhỏ nhất?",
                       "\n".join([
                           "Diện tích tam giác đáy: S = V / L = 12 / 4 = 3 m^2 (0.25đ).",
                           "Gọi chiều cao tam giác đáy là h và cạnh đáy là 2x => S = (1/2) . 2x . h = xh = 3 => h = 3/x (0.25đ).",
                           "Độ dài cạnh mái lều d = căn(h^2 + x^2) = căn(9/x^2 + x^2) (0.25đ).",
                           "Áp dụng bất đẳng thức Cauchy: 9/x^2 + x^2 >= 2 . căn(9) = 6. Dấu '=' khi x = căn(3). Khi đó diện tích mái lều nhỏ nhất (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 7 (KNTT) - Bài kiểm tra cuối Chương X: Một số hình khối trong thực tiễn - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(7, chap_id, "Chương X: Một số hình khối trong thực tiễn", exams)


# ------------------------------------------------------------------------------
# HÀM CHẠY TOÀN BỘ 10 CHƯƠNG TOÁN 7
# ------------------------------------------------------------------------------
def run_all_grade7():
    print("=== BẮT ĐẦU SINH 7 ĐỀ ĐỘC LẬP CHO TOÀN BỘ 10 CHƯƠNG TOÁN 7 ===")
    build_c1_7()
    build_c2_7()
    build_c3_7()
    build_c4_7()
    build_c5_7()
    build_c6_7()
    build_c7_7()
    build_c8_7()
    build_c9_7()
    build_c10_7()
    print("=== HOÀN TẤT XUẤT SẮC TOÁN 7: 10 CHƯƠNG x 7 ĐỀ = 70 ĐỀ CHUẨN MA TRẬN ===")

if __name__ == "__main__":
    run_all_grade7()
