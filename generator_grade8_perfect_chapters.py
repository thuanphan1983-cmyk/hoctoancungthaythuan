# -*- coding: utf-8 -*-
"""
BUILD COMPLETE GRADE 8 EXAMS (10 CHAPTERS x 7 TESTS = 70 TESTS)
Direct execution to generate and package JSON/JS files directly without string interpolation issues!
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package, OUTPUT_DIR

def load_existing_exams(chap_id, grade=8):
    json_path = os.path.join(OUTPUT_DIR, f"grade{grade}_{chap_id}_exams.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            d = json.load(f)
            return d.get("exams", {})
    return {}

# ------------------------------------------------------------------------------
# CHƯƠNG I: Đa thức (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c1_8():
    chap_id = "c1_8"
    l_idx = 6
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    real_apps = [
        ("Khu đô thị sinh thái", "lối đi lát đá hình chữ nhật", 15, 2),
        ("Khu công nghiệp", "kho chứa hàng hóa đa năng", 24, 12),
        ("Khu resort biển", "hồ bơi ngoài trời", 20, 8),
        ("Trang trại nông nghiệp", "luống rau sạch công nghệ cao", 30, 4),
        ("Trường học chuẩn quốc gia", "sân bóng rổ mini", 22, 14),
        ("Công viên cây xanh", "bồn hoa hình chữ nhật", 18, 5),
        ("Khu triển lãm", "gian hàng hội chợ ngoài trời", 16, 6)
    ]

    for t in range(1, 8):
        app = real_apps[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", f"Biểu thức nào sau đây là đơn thức nhiều biến (Đề {t:02d})?", [f"${t+1}x^2y$", f"${t}x + y$", f"\\frac{{{t}}}{{x}}", f"$x^2 - {t}$"], 0),
            make_mc(2, "Nhận biết", f"Bậc của đơn thức $M = {t+2}x^3y^2z$ là:", ["6", "5", "3", "2"], 0),
            make_mc(3, "Nhận biết", "Trong các đơn thức sau, đơn thức nào đồng dạng với đơn thức $-3x^2y$?", ["$5x^2y$", "$3xy^2$", "$-3x^2y^2$", "$2x^3y$"], 0),
            make_mc(4, "Nhận biết", "Đa thức là một tổng của những:", ["Đơn thức", "Số tự nhiên", "Phân số", "Căn thức"], 0),
            make_mc(5, "Thông hiểu", f"Thu gọn đa thức $P = {t+2}x^2y - {t}xy + 3x^2y + {t}xy$ ta được:", [f"${t+5}x^2y$", f"${t+5}x^2y - {2*t}xy$", f"${t+2}x^2y$", "$3x^2y$"], 0),
            make_mc(6, "Thông hiểu", f"Tích của đơn thức ${2*t}x$ với đa thức $(x^2 - {t}y)$ là:", [f"${2*t}x^3 - {2*t*t}xy$", f"${2*t}x^3 - {t}y$", f"${2*t}x^2 - {2*t}xy$", f"$x^3 - {t}xy$"], 0),
            make_mc(7, "Thông hiểu", f"Kết quả của phép chia $({6*t}x^3y^2 - {4*t}x^2y^2) : (2x^2y)$ là:", [f"${3*t}xy - {2*t}y$", f"${3*t}x - {2*t}y$", f"${3*t}y - {2*t}$", f"${3*t}x^2y - {2*t}$"], 0),
            make_mc(8, "Thông hiểu", f"Giá trị của đa thức $A = 2x^2 - 3xy$ tại $x = {t}, y = -1$ là:", [f"${2*t*t + 3*t}$", f"${2*t*t - 3*t}$", f"${-2*t*t + 3*t}$", "$0$"], 0),
            make_mc(9, "Vận dụng", f"Tại {app[0]}, người ta làm {app[1]} có chiều dài $x + {app[2]}$ mét và chiều rộng $x - {app[3]}$ mét. Đa thức biểu thị diện tích là:", [f"$x^2 + {app[2]-app[3]}x - {app[2]*app[3]}$", f"$x^2 - {app[2]*app[3]}$", f"$x^2 + {app[2]+app[3]}x$", f"$2x + {app[2]-app[3]}$"], 0),
            make_mc(10, "Vận dụng", f"Bác thợ mộc đóng một hộp gỗ hình hộp chữ nhật có đáy hình vuông cạnh $x$ mét và chiều cao $x + {t}$ mét. Đa thức biểu diễn thể tích khối hộp gỗ là:", [f"$x^3 + {t}x^2$", f"$x^2 + {t}x$", f"$3x + {t}$", f"$x^3 + {t}$"], 0),
            make_mc(11, "Vận dụng", f"Một công ty may đo xuất khẩu sản xuất được $100x^2 + {50*t}x$ bộ quần áo trong $5x$ ngày. Trung bình mỗi ngày công ty sản xuất được số bộ quần áo là:", [f"$20x + {10*t}$", f"$20x^2 + {10*t}x$", f"$50x + {25*t}$", f"$20x + {5*t}$"], 0),
            make_mc(12, "Vận dụng cao", f"Giá trị nhỏ nhất của đa thức $P = x^2 - {2*t}x + {t*t + 5}$ đạt được khi $x$ bằng:", [f"${t}$", f"${-t}$", f"${2*t}$", "$0$"], 0)
        ]
        p2 = [
            make_tf(1, f"Cho hai đa thức $A = {2*t}x^2y + 3xy^2 - 5$ và $B = x^2y - 3xy^2 + {t}$ (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "A và B đều là các đa thức bậc 3 đối với hai biến x và y.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Tổng A + B là đa thức có chứa hạng tử ({2*t + 1})x^2y.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Trong đa thức tổng A + B, hạng tử chứa xy^2 đã bị triệt tiêu bằng 0.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": f"Tại x = 1, y = 1 thì giá trị của hiệu A - B bằng {2*t - 1}.", "correct": False}
            ]),
            make_tf(2, f"Bài toán kinh tế xây dựng (Mã đề {t:02d}): Một mảnh sân trường hình chữ nhật có chiều dài (2x + {t*2}) mét và chiều rộng (x + {t}) mét. Giữa sân người ta xây một bồn hoa hình vuông cạnh x mét.", [
                {"key": "a", "level": "Nhận biết", "text": "Diện tích toàn bộ sân trường được biểu diễn bằng tích (2x + 2t)(x + t).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích bồn hoa hình vuông là x^2 m^2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Diện tích phần sân còn lại sau khi trừ bồn hoa là x^2 + {4*t}x + {2*t*t} m^2.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu x = 10 mét thì diện tích phần sân lát gạch lớn hơn 500 m^2 với mọi giá trị của t.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính bậc của đa thức: P = 5x^{3+t}y^2 - 3x^2y^{2+t} + 7.", f"{5+t}"),
            make_sa(2, "Thông hiểu", f"Thu gọn đơn thức M = (-2x^2y) * ({t}xy^3) rồi tính hệ số của M.", f"{-2*t}"),
            make_sa(3, "Vận dụng", f"Một bể nước hình hộp chữ nhật có kích thước đáy là 2x m và 3x m, chiều cao x + {t} m. Khi x = 2 m và t = {t}, thể tích của bể nước là bao nhiêu m^3?", f"{24 * (2 + t)}"),
            make_sa(4, "Vận dụng", f"Biết rằng đa thức A chia cho đơn thức 2x^2y được thương là 3xy - {t}. Tính giá trị của A khi x = 1, y = 1 và t = {t}.", f"{6 - 2*t}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Thực hiện phép tính rút gọn đa thức: $M = (2x - 1)(x + {t}) - 2x(x + {t - 1})$.",
                       "\n".join([
                           f"Nhân đa thức với đa thức: (2x - 1)(x + {t}) = 2x^2 + {2*t - 1}x - {t} (0.25đ).",
                           f"Nhân đơn thức với đa thức: -2x(x + {t - 1}) = -2x^2 - {2*t - 2}x (0.25đ).",
                           f"Cộng các hạng tử đồng dạng: M = x - {t} (0.25đ).",
                           f"Kết luận biểu thức rút gọn là M = x - {t} (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một công viên hình chữ nhật có chiều dài là $(3x + {t*4})$ mét và chiều rộng là $(2x + {t*2})$ mét. Người ta làm một lối đi xung quanh rộng $1$ mét thuộc phần đất phía trong của công viên. Viết đa thức biểu thị diện tích phần đất còn lại để trồng hoa và tính diện tích đó khi $x = 10$ mét.",
                       "\n".join([
                           f"Chiều dài phần đất trồng hoa: (3x + {t*4}) - 2 = 3x + {t*4 - 2} (m) (0.25đ).",
                           f"Chiều rộng phần đất trồng hoa: (2x + {t*2}) - 2 = 2x + {t*2 - 2} (m) (0.25đ).",
                           "Biểu thức diện tích S = (3x + a)(2x + b) theo x (0.25đ).",
                           "Thay x = 10 vào biểu thức ta tính được diện tích cụ thể (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Tìm giá trị nhỏ nhất của đa thức: $A = x^2 + y^2 - 2x + {2*t}y + {t*t + 10}$.",
                       "\n".join([
                           f"Biến đổi A thành tổng các bình phương: A = (x - 1)^2 + (y + {t})^2 + 9 (0.25đ).",
                           "Vì (x - 1)^2 >= 0 và bình phương luôn không âm với mọi x, y (0.25đ).",
                           "Suy ra A >= 9 với mọi giá trị x, y (0.25đ).",
                           f"Dấu '=' xảy ra khi x = 1 và y = {-t}. Vậy GTNN của A là 9 (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương I: Đa thức - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương I: Đa thức", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG II: Hằng đẳng thức đáng nhớ và ứng dụng (l_idx = 5)
# ------------------------------------------------------------------------------
def build_c2_8():
    chap_id = "c2_8"
    l_idx = 5
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    real_apps = [
        ("Mở rộng khuôn viên trường THCS", "sân bóng chuyền hình vuông", 12, 3),
        ("Quy hoạch quảng trường trung tâm", "khu vực sân khấu vuông", 20, 5),
        ("Cải tạo vườn thực nghiệm sinh học", "nhà lưới hình vuông", 15, 4),
        ("Xây dựng khu vui chơi trẻ em", "sân trượt cỏ hình vuông", 18, 6),
        ("Mở rộng bể bơi cộng đồng", "bể thi đấu hình vuông", 25, 5),
        ("Nâng cấp bãi đỗ xe thông minh", "khu đỗ xe buýt vuông", 30, 8),
        ("Dự án sân golf mini gia đình", "khu tập gạt bóng vuông", 16, 4)
    ]

    for t in range(1, 8):
        app = real_apps[t - 1]
        p1 = [
            make_mc(1, "Nhận biết", f"Khai triển của hằng đẳng thức $(A + B)^2$ là (Đề {t:02d}):", ["$A^2 + 2AB + B^2$", "$A^2 + AB + B^2$", "$A^2 - 2AB + B^2$", "$A^2 + B^2$"], 0),
            make_mc(2, "Nhận biết", "Biểu thức $x^2 - y^2$ được phân tích thành:", ["$(x - y)(x + y)$", "$(x - y)^2$", "$(x + y)^2$", "$x^2 - 2xy + y^2$"], 0),
            make_mc(3, "Nhận biết", "Hằng đẳng thức lập phương của một hiệu $(A - B)^3$ bằng:", ["$A^3 - 3A^2B + 3AB^2 - B^3$", "$A^3 - B^3$", "$A^3 - 3A^2B - 3AB^2 - B^3$", "$A^3 + 3A^2B + 3AB^2 + B^3$"], 0),
            make_mc(4, "Nhận biết", "Phân tích đa thức thành nhân tử là biến đổi đa thức đó thành:", ["Một tích của những đa thức", "Một tổng của các đơn thức", "Một hiệu của hai bình phương", "Một thương của hai đa thức"], 0),
            make_mc(5, "Thông hiểu", f"Khai triển hằng đẳng thức $(x + {t})^2$ ta được kết quả là:", [f"$x^2 + {2*t}x + {t*t}$", f"$x^2 + {t}x + {t*t}$", f"$x^2 + {2*t}x + {2*t}$", f"$x^2 + {t*t}$"], 0),
            make_mc(6, "Thông hiểu", f"Phân tích đa thức $x^2 - {4*t*t}$ thành nhân tử ta được:", [f"$(x - {2*t})(x + {2*t})$", f"$(x - {2*t})^2$", f"$(x - {4*t})(x + {4*t})$", f"$(x + {2*t})^2$"], 0),
            make_mc(7, "Thông hiểu", f"Giá trị của biểu thức $P = x^2 - {2*t}x + {t*t}$ tại $x = {t + 10}$ là:", ["100", f"${t*t}$", "200", "50"], 0),
            make_mc(8, "Thông hiểu", f"Phân tích đa thức $x^3 - {8*t*t*t}$ thành nhân tử ta được:", [f"$(x - {2*t})(x^2 + {2*t}x + {4*t*t})$", f"$(x - {2*t})(x^2 - {2*t}x + {4*t*t})$", f"$(x - {2*t})^3$", f"$(x - {8*t})(x^2 + {8*t}x + {64*t*t})$"], 0),
            make_mc(9, "Vận dụng", f"Tại dự án {app[0]}, một {app[1]} ban đầu có cạnh $x$ mét. Sau khi mở rộng mỗi cạnh thêm ${app[3]}$ mét thì diện tích tăng thêm là:", [f"${2*app[3]}x + {app[3]*app[3]}$ mét vuông", f"${app[3]}x + {app[3]*app[3]}$ mét vuông", f"$x^2 + {app[3]*app[3]}$ mét vuông", f"${4*app[3]}x$ mét vuông"], 0),
            make_mc(10, "Vận dụng", f"Tính nhanh giá trị diện tích khu đất khi hiệu hai bình phương là: ${100 + t}^2 - {100 - t}^2$:", [f"${400*t}$", f"${200*t}$", f"${100*t}$", f"${4*t*t}$"], 0),
            make_mc(11, "Vận dụng", f"Một khối bê tông hình lập phương có cạnh ban đầu là $x$ cm. Người ta giảm mỗi cạnh đi ${t}$ cm. Biểu thức thể tích phần bê tông bị giảm đi là:", [f"$3{t}x^2 - 3{t*t}x + {t*t*t}$", f"$x^3 - {t*t*t}$", f"${3*t}x^2$", f"${t*t*t}$"], 0),
            make_mc(12, "Vận dụng cao", f"Giá trị nhỏ nhất của biểu thức $P = x^2 - {4*t}x + y^2 + {2*t}y + {5*t*t + 7}$ là:", ["7", "5", f"${t*t}$", "10"], 0)
        ]
        p2 = [
            make_tf(1, f"Cho biểu thức $A = (x + {t})^3 - (x - {t})^3$ (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Biểu thức A được tạo bởi hiệu của hai lập phương.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Khai triển hằng đẳng thức ta được A = {6*t}x^2 + {2*t*t*t}.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Biểu thức A luôn nhận giá trị dương với mọi số thực x khác 0.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": f"Với x = 2, giá trị của A luôn là một số chia hết cho 10 khi t = {t}.", "correct": False}
            ]),
            make_tf(2, f"Bài toán cắt dán kim loại kỹ thuật (Đề {t:02d}): Một tấm tôn hình vuông cạnh (x + {t*2}) cm bị khoét đi một hình vuông ở chính giữa có cạnh (x - {t*2}) cm.", [
                {"key": "a", "level": "Nhận biết", "text": "Diện tích tấm tôn ban đầu là (x + 2t)^2 cm^2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích phần bị khoét đi là (x - 2t)^2 cm^2.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Diện tích phần tôn còn lại là hiệu hai bình phương bằng {8*t}x cm^2.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích phần tôn còn lại phụ thuộc vào bình phương của x.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính giá trị của biểu thức P = x^2 - {6*t}x + {9*t*t} tại x = {3*t + 5}.", "25"),
            make_sa(2, "Thông hiểu", f"Tìm x biết: (x - {t})^2 - (x - {t})(x + {t}) = 0.", f"{t//2 if t%2==0 else t}"),
            make_sa(3, "Vận dụng", f"Một mảnh đất hình chữ nhật có diện tích x^2 + {7*t}x + {12*t*t} m^2, chiều rộng là x + {3*t} m. Chiều dài mảnh đất hơn chiều rộng bao nhiêu mét khi t = {t}?", f"{t}"),
            make_sa(4, "Vận dụng", f"Cho x + y = {10 + t} và xy = {2*t}. Tính giá trị của biểu thức x^2 + y^2.", f"{(10+t)**2 - 4*t}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Phân tích đa thức sau thành nhân tử: $A = x^3 - {2*t}x^2 + {t*t}x - 4x$.",
                       "\n".join([
                           f"Đặt nhân tử chung x ra ngoài: A = x(x^2 - {2*t}x + {t*t} - 4) (0.25đ).",
                           f"Nhóm ba hạng tử đầu thành hằng đẳng thức: A = x[(x - {t})^2 - 2^2] (0.25đ).",
                           f"Dùng hằng đẳng thức hiệu hai bình phương: A = x(x - {t} - 2)(x - {t} + 2) (0.25đ).",
                           "Kết luận dạng nhân tử của đa thức (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Bác nông dân có một mảnh vườn hình vuông cạnh $a$ mét. Bác mở rộng về một phía thêm ${t*2}$ mét và mở rộng về phía vuông góc thêm ${t*3}$ mét để được một mảnh vườn hình chữ nhật mới. Biết diện tích mảnh vườn mới lớn hơn diện tích ban đầu là ${50*t}$ mét vuông. Tính độ dài cạnh $a$ của mảnh vườn hình vuông ban đầu.",
                       "\n".join([
                           f"Diện tích mảnh vườn mới là: (a + {t*2})(a + {t*3}) = a^2 + {5*t}a + {6*t*t} (m^2) (0.25đ).",
                           f"Diện tích phần tăng thêm: (a^2 + {5*t}a + {6*t*t}) - a^2 = {5*t}a + {6*t*t} (m^2) (0.25đ).",
                           f"Phương trình: {5*t}a + {6*t*t} = {50*t} <=> 5a + {6*t} = 50 <=> a = (50 - {6*t})/5 (0.25đ).",
                           "Kết luận cạnh mảnh vườn ban đầu a (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Chứng minh rằng biểu thức $M = x^2 - {2*t}x + y^2 + {4*t}y + {6*t*t + 1}$ luôn nhận giá trị dương với mọi số thực $x, y$.",
                       "\n".join([
                           f"Biến đổi M về tổng các bình phương: M = (x - {t})^2 + (y + {2*t})^2 + {t*t + 1} (0.25đ).",
                           "Vì (x - a)^2 >= 0 và (y + b)^2 >= 0 với mọi x, y (0.25đ).",
                           f"Do đó M >= {t*t + 1} > 0 với mọi x, y (0.25đ).",
                           "Đẳng thức được chứng minh hoàn tất (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương II: Hằng đẳng thức đáng nhớ và ứng dụng - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương II: Hằng đẳng thức đáng nhớ và ứng dụng", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG III: Tứ giác (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c3_8():
    chap_id = "c3_8"
    l_idx = 6
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Tổng các góc của một tứ giác lồi luôn bằng (Đề {t:02d}):", ["$360^\\circ$", "$180^\\circ$", "$90^\\circ$", "$720^\\circ$"], 0),
            make_mc(2, "Nhận biết", "Hình thang cân là hình thang có:", ["Hai góc kề một đáy bằng nhau", "Hai cạnh bên song song", "Hai góc đối bằng nhau", "Bốn góc vuông"], 0),
            make_mc(3, "Nhận biết", "Hình bình hành có hai đường chéo vuông góc với nhau là:", ["Hình thoi", "Hình chữ nhật", "Hình thang cân", "Hình vuông"], 0),
            make_mc(4, "Nhận biết", "Hình chữ nhật có hai cạnh kề bằng nhau là:", ["Hình vuông", "Hình thoi", "Hình thang", "Hình bình hành"], 0),
            make_mc(5, "Thông hiểu", f"Cho tứ giác $ABCD$ có $\\widehat{{A}} = {80+t}^\\circ, \\widehat{{B}} = {100-t}^\\circ, \\widehat{{C}} = 90^\\circ$. Số đo góc $D$ là:", ["$90^\\circ$", "$100^\\circ$", "$80^\\circ$", "$110^\\circ$"], 0),
            make_mc(6, "Thông hiểu", f"Hình thang cân $ABCD$ ($AB // CD$) có $\\widehat{{C}} = {60 + t}^\\circ$. Số đo góc $A$ là:", [f"${120 - t}^\\circ$", f"${60 + t}^\\circ$", f"${180 - t}^\\circ$", "$90^\\circ$"], 0),
            make_mc(7, "Thông hiểu", f"Một hình thoi có độ dài hai đường chéo lần lượt là ${6*t}$ cm và ${8*t}$ cm. Độ dài cạnh của hình thoi là:", [f"${5*t}$ cm", f"${10*t}$ cm", f"${7*t}$ cm", f"${14*t}$ cm"], 0),
            make_mc(8, "Thông hiểu", f"Hình chữ nhật có độ dài đường chéo là ${10*t}$ cm, một cạnh bằng ${6*t}$ cm. Diện tích của hình chữ nhật là:", [f"${48*t*t}$ cm$^2$", f"${60*t*t}$ cm$^2$", f"${30*t*t}$ cm$^2$", f"${24*t*t}$ cm$^2$"], 0),
            make_mc(9, "Vận dụng", f"Người ta làm một con diều hình thoi có hai thanh tre làm đường chéo dài ${40+t*5}$ cm và ${60+t*5}$ cm. Diện tích giấy màu cần để dán phủ mặt diều là:", [f"${((40+t*5)*(60+t*5))//2}$ cm$^2$", f"${(40+t*5)*(60+t*5)}$ cm$^2$", "1000 cm$^2$", "1500 cm$^2$"], 0),
            make_mc(10, "Vận dụng", f"Một khung cửa sổ bằng nhôm kính hình chữ nhật có chiều dài ${120+t*10}$ cm và chiều rộng ${90+t*5}$ cm. Để đảm bảo khung cửa vuông vắn, bác thợ đo hai đường chéo thì độ dài mỗi đường chéo phải xấp xỉ bằng:", [f"${round(((120+t*10)**2 + (90+t*5)**2)**0.5)}$ cm", "150 cm", "200 cm", "180 cm"], 0),
            make_mc(11, "Vận dụng", f"Một mảnh đất hình bình hành có đáy dài ${30+t*2}$ mét, chiều cao tương ứng bằng $15$ mét. Người ta dùng $20\\%$ diện tích để trồng hoa. Diện tích trồng hoa là:", [f"${(30+t*2)*15*0.2:.1f}$ mét vuông", "100 mét vuông", "120 mét vuông", "90 mét vuông"], 0),
            make_mc(12, "Vận dụng cao", "Cho hình vuông $ABCD$ cạnh $a$. Gọi $M, N$ lần lượt là trung điểm của $BC, CD$. Đoạn thẳng $AM$ vuông góc với đoạn thẳng:", ["$BN$", "$DN$", "$BD$", "$AC$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về hình thang cân và hình thoi (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Trong hình thang cân, hai đường chéo luôn có độ dài bằng nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hình thoi có bốn cạnh bằng nhau và hai đường chéo vuông góc với nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tứ giác có hai đường chéo cắt nhau tại trung điểm mỗi đường là hình bình hành.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Một hình thoi có một góc vuông thì trở thành hình bình hành.", "correct": False}
            ]),
            make_tf(2, f"Cho tam giác $ABC$ vuông tại $A$, đường trung tuyến $AM$. Gọi $D$ là điểm đối xứng với $A$ qua $M$ (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Tứ giác ABDC có hai đường chéo AD và BC cắt nhau tại trung điểm M.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tứ giác ABDC có một góc vuông tại A nên là hình chữ nhật.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Độ dài đường trung tuyến AM bằng một nửa độ dài cạnh huyền BC.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Khi tam giác ABC vuông cân tại A thì tứ giác ABDC là hình thoi nhưng không phải hình vuông.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Cho hình bình hành ABCD có góc A = {110 - t} độ. Tính số đo góc B (độ).", f"{70 + t}"),
            make_sa(2, "Thông hiểu", f"Một hình thoi có cạnh bằng {5*t} cm, chu vi của hình thoi đó là bao nhiêu cm?", f"{20*t}"),
            make_sa(3, "Vận dụng", f"Một mảnh vườn hình chữ nhật có chu vi {100 + 10*t} mét, chiều dài hơn chiều rộng {10 + 2*t} mét. Tính diện tích mảnh vườn (m^2).", f"{( (100+10*t)/4 + (10+2*t)/4 ) * ( (100+10*t)/4 - (10+2*t)/4 ):.0f}"),
            make_sa(4, "Vận dụng", f"Một chiếc thang xếp khi mở ra tạo thành hình thang cân có hai cạnh bên dài 2 mét, đáy nhỏ 0,6 mét, đáy lớn 1,8 mét. Tính chiều cao của chiếc thang (làm tròn 1 chữ số thập phân, mét).", "1.9")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho hình chữ nhật $ABCD$ có $AB = {8*t}$ cm, $BC = {6*t}$ cm. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Tính độ dài $AC$ và $OA$.",
                       "\n".join([
                           f"Áp dụng định lí Pythagore trong tam giác vuông ABC: AC^2 = AB^2 + BC^2 = {100*t*t} (0.25đ).",
                           f"Suy ra AC = {10*t} cm (0.25đ).",
                           "Vì ABCD là hình chữ nhật nên hai đường chéo cắt nhau tại trung điểm O: OA = AC / 2 (0.25đ).",
                           f"Suy ra OA = {5*t} cm. Kết luận độ dài AC và OA (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Người ta thiết kế một bồn hoa hình vuông ở sân trường. Xung quanh bồn hoa, bác bảo vệ dự định rào một hàng rào bằng lưới thép. Biết diện tích bồn hoa là ${16 + t*4}$ mét vuông. Tính chu vi bồn hoa để mua số mét lưới thép vừa đủ.",
                       "\n".join([
                           f"Gọi cạnh bồn hoa hình vuông là a (m, a > 0) (0.25đ).",
                           f"Theo bài ra: a^2 = {16 + t*4} => a = căn({16 + t*4}) (m) (0.25đ).",
                           f"Chu vi bồn hoa hình vuông: P = 4 . a = 4 . căn({16 + t*4}) (m) (0.25đ).",
                           "Kết luận số mét lưới thép cần mua (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Cho hình vuông $ABCD$. Trên cạnh $BC$ lấy điểm $E$, trên tia đối của tia $CD$ lấy điểm $F$ sao cho $BE = DF$. Chứng minh rằng tam giác $AEF$ là tam giác vuông cân.",
                       "\n".join([
                           "Xét tam giác ABE và ADF có: AB = AD, góc ABE = ADF = 90 độ, BE = DF (0.25đ).",
                           "Suy ra tam giác ABE = tam giác ADF (c.g.c) => AE = AF và góc BAE = DAF (0.25đ).",
                           "Tính được góc EAF = góc EAD + góc DAF = góc EAD + góc BAE = 90 độ (0.25đ).",
                           "Tam giác AEF có AE = AF và góc vuông nên là tam giác vuông cân tại A (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương III: Tứ giác - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương III: Tứ giác", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG IV: Định lí Thalès (l_idx = 4)
# ------------------------------------------------------------------------------
def build_c4_8():
    chap_id = "c4_8"
    l_idx = 4
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Đoạn thẳng $AB = {2*t}$ cm, $CD = {6*t}$ cm. Tỉ số của hai đoạn thẳng $AB$ và $CD$ là (Đề {t:02d}):", ["$\\frac{1}{3}$", "$3$", "$\\frac{1}{2}$", "$\\frac{2}{3}$"], 0),
            make_mc(2, "Nhận biết", "Nếu một đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn lại thì nó định ra trên hai cạnh đó:", ["Những đoạn thẳng tương ứng tỉ lệ", "Những đoạn thẳng bằng nhau", "Những góc bằng nhau", "Những tam giác bằng nhau"], 0),
            make_mc(3, "Nhận biết", "Đường trung bình của tam giác là đoạn thẳng nối:", ["Trung điểm hai cạnh của tam giác", "Đỉnh và trung điểm cạnh đối diện", "Đỉnh và trực tâm", "Hai đỉnh bất kì"], 0),
            make_mc(4, "Nhận biết", "Đường trung bình của tam giác thì song song với cạnh thứ ba và bằng:", ["Nửa cạnh thứ ba", "Cạnh thứ ba", "Hai lần cạnh thứ ba", "Một phần ba cạnh thứ ba"], 0),
            make_mc(5, "Thông hiểu", f"Cho tam giác $ABC$, $MN // BC$ ($M \\in AB, N \\in AC$). Biết $AM = {2*t}$ cm, $MB = {3*t}$ cm, $AN = 4$ cm. Độ dài đoạn thẳng $NC$ là:", ["6 cm", "8 cm", "4 cm", "5 cm"], 0),
            make_mc(6, "Thông hiểu", f"Cho tam giác $ABC$ có chu vi bằng ${18*t}$ cm. Gọi $D, E, F$ lần lượt là trung điểm của $AB, BC, CA$. Chu vi tam giác $DEF$ là:", [f"${9*t}$ cm", f"${6*t}$ cm", f"${12*t}$ cm", f"${4.5*t}$ cm"], 0),
            make_mc(7, "Thông hiểu", f"Cho tam giác $ABC$ có $AD$ là đường phân giác trong của góc $A$ ($D \\in BC$). Biết $AB = {4*t}$ cm, $AC = {6*t}$ cm, $BD = 2$ cm. Độ dài đoạn $DC$ là:", ["3 cm", "4 cm", "2 cm", "5 cm"], 0),
            make_mc(8, "Thông hiểu", "Cho hình thang $ABCD$ ($AB // CD$). Đoạn thẳng nối trung điểm hai cạnh bên của hình thang được gọi là:", ["Đường trung bình của hình thang", "Đường chéo", "Chiều cao", "Cạnh đáy"], 0),
            make_mc(9, "Vận dụng", f"Để đo chiều cao một cái cây, bạn Nam cắm một cọc tiêu cao $1,5$ mét thẳng đứng trên mặt đất cách gốc cây ${10+t}$ mét. Khi ngắm từ ngọn cọc tiêu thấy ngọn cây và bóng của cọc trên mặt đất dài $2$ mét. Chiều cao của cây là:", [f"{1.5 * (12+t) / 2:.2f} mét", "10 mét", "8 mét", "12 mét"], 0),
            make_mc(10, "Vận dụng", f"Hai bên bờ sông có hai vị trí $A$ và $B$. Để đo khoảng cách $AB$, người ta chọn điểm $C$ trên bờ và xác định đường trung bình nối trung điểm của $CA$ và $CB$ đo được ${25+t*5}$ mét. Khoảng cách $AB$ giữa hai bờ sông là:", [f"${50+t*10}$ mét", f"${25+t*5}$ mét", f"${100+t*20}$ mét", "60 mét"], 0),
            make_mc(11, "Vận dụng", f"Một người đứng dưới ánh đèn đường có cột đèn cao 6 mét. Người đó cao 1,6 mét và đứng cách chân cột đèn ${t+4}$ mét. Chiều dài bóng của người đó trên mặt đất là:", [f"{(1.6 * (t+4)) / (6 - 1.6):.2f} mét", "2 mét", "3 mét", "1,5 mét"], 0),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$. Gọi $M$ là trung điểm của $AB$, $N$ là điểm trên cạnh $AC$ sao cho $AN = 2 NC$. Đoạn thẳng $MN$ cắt đường trung tuyến $AI$ tại điểm $K$. Tỉ số $\\frac{AK}{AI}$ bằng:", ["$\\frac{4}{5}$", "$\\frac{3}{4}$", "$\\frac{2}{3}$", "$\\frac{1}{2}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về định lí Thalès trong tam giác (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Nếu một đường thẳng cắt hai cạnh của một tam giác và định ra trên hai cạnh này những đoạn thẳng tương ứng tỉ lệ thì đường thẳng đó song song với cạnh thứ ba.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Đường phân giác ngoài của một góc trong tam giác cũng chia cạnh đối diện thành hai đoạn thẳng tỉ lệ với hai cạnh kề.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Đường trung bình của tam giác có độ dài bằng một nửa độ dài cạnh đáy tương ứng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tỉ số diện tích hai tam giác tạo bởi đường thẳng song song với một cạnh luôn bằng tỉ số hai cạnh tương ứng.", "correct": False}
            ]),
            make_tf(2, f"Cho tam giác $ABC$ có $AB = {6*t}$ cm, $AC = {9*t}$ cm. Trên cạnh $AB$ lấy điểm $M$ sao cho $AM = {2*t}$ cm, trên cạnh $AC$ lấy điểm $N$ sao cho $AN = {3*t}$ cm (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Tỉ số AM/AB = 1/3 và AN/AC = 1/3.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Theo định lí Thalès đảo, đoạn thẳng MN song song với cạnh BC.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Độ dài đoạn thẳng MN bằng 1/3 độ dài cạnh BC.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích tam giác AMN bằng một nửa diện tích tam giác ABC.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Cho tam giác ABC có MN // BC (M thuộc AB, N thuộc AC). Biết AM/MB = 2/3, AN = {2*t} cm. Tính độ dài đoạn NC (cm).", f"{3*t}"),
            make_sa(2, "Thông hiểu", f"Một hình thang có đáy nhỏ 8 cm, đáy lớn {14+2*t} cm. Tính độ dài đường trung bình của hình thang (cm).", f"{11+t}"),
            make_sa(3, "Vận dụng", f"Đo bóng của một cột ăng-ten truyền hình trên mặt đất dài {30+t*5} mét, cùng lúc đó một chiếc cọc cao 2 mét có bóng dài 1,5 mét. Tính chiều cao cột ăng-ten (mét).", f"{(30+t*5)*2/1.5:.0f}"),
            make_sa(4, "Vận dụng", f"Cho tam giác ABC, AD là phân giác góc A (D thuộc BC). Biết AB = 12 cm, AC = 18 cm, BC = {15+t} cm. Tính độ dài đoạn BD (làm tròn 1 chữ số thập phân, cm).", f"{12*(15+t)/30:.1f}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho tam giác $ABC$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$. Biết $BC = {10+2*t}$ cm. Chứng minh rằng $MN // BC$ và tính độ dài $MN$.",
                       "\n".join([
                           "Vì M, N là trung điểm của AB và AC nên MN là đường trung bình tam giác ABC (0.25đ).",
                           "Theo tính chất: MN // BC (0.25đ).",
                           f"Độ dài MN = BC / 2 = ({10+2*t}) / 2 = {5+t} cm (0.25đ).",
                           f"Kết luận MN // BC và MN = {5+t} cm (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một người muốn đo chiều cao của một tòa nhà cao tầng mà không thể leo lên đỉnh. Người đó đặt một gương phẳng nằm ngang trên mặt đất tại điểm $C$ cách chân tòa nhà $d = {40+t*5}$ mét. Người đó lùi xa gương một khoảng $1,6$ mét thì thấy ảnh của đỉnh tòa nhà qua gương. Biết mắt người đó cách mặt đất $1,5$ mét. Tính chiều cao tòa nhà.",
                       "\n".join([
                           f"Khoảng cách từ chân tháp đến gương là BC = {40+t*5} m (0.25đ).",
                           "Khoảng cách từ người đến gương là CD = 1,6 m, chiều cao mắt là DE = 1,5 m (0.25đ).",
                           "Hai tam giác vuông đồng dạng: AB / DE = BC / CD (0.25đ).",
                           f"Suy ra AB = 1,5 . ({40+t*5}) / 1,6. Tính ra chiều cao tòa nhà (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Cho hình thang $ABCD$ ($AB // CD$). Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Qua $O$ kẻ đường thẳng song song với hai đáy, cắt $AD$ tại $M$ và cắt $BC$ tại $N$. Chứng minh rằng $OM = ON$.",
                       "\n".join([
                           "Xét tam giác ADC có OM // CD => OM/CD = AO/AC (0.25đ).",
                           "Xét tam giác BDC có ON // CD => ON/CD = BO/BD (0.25đ).",
                           "Vì AB // CD nên theo hệ quả định lí Thalès: AO/AC = BO/BD (0.25đ).",
                           "Suy ra OM/CD = ON/CD => OM = ON (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương IV: Định lí Thalès - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương IV: Định lí Thalès", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG V: Dữ liệu và biểu đồ (l_idx = 4)
# ------------------------------------------------------------------------------
def build_c5_8():
    chap_id = "c5_8"
    l_idx = 4
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Dữ liệu nào sau đây là dữ liệu định lượng (Đề {t:02d})?", ["Chiều cao của các học sinh trong lớp", "Màu sắc yêu thích của các bạn", "Nơi sinh của các thành viên trong tổ", "Xếp loại học lực của học sinh"], 0),
            make_mc(2, "Nhận biết", "Để biểu diễn tỉ lệ phần trăm các thành phần trong toàn bộ tổng thể, biểu đồ thích hợp nhất là:", ["Biểu đồ hình quạt tròn", "Biểu đồ cột đơn", "Biểu đồ đoạn thẳng", "Biểu đồ tranh"], 0),
            make_mc(3, "Nhận biết", "Biểu đồ đoạn thẳng thường được sử dụng để biểu diễn:", ["Sự thay đổi của một đại lượng theo thời gian", "Cơ cấu phần trăm", "Số lượng các mặt hàng riêng biệt", "So sánh hai tập dữ liệu"], 0),
            make_mc(4, "Nhận biết", "Tổng số đo các góc ở tâm của các hình quạt trong một biểu đồ hình quạt tròn luôn bằng:", ["$360^\\circ$", "$180^\\circ$", "$100^\\circ$", "$90^\\circ$"], 0),
            make_mc(5, "Thông hiểu", f"Trong một biểu đồ hình quạt tròn, hình quạt biểu diễn số liệu chiếm ${20+t*5}\\%$ có góc ở tâm tương ứng là:", [f"{(20+t*5)*3.6:.1f}^\\circ$", "$72^\\circ$", "$90^\\circ$", "$100^\\circ$"], 0),
            make_mc(6, "Thông hiểu", f"Một cuộc điều tra về sở thích của {100+t*10} học sinh thấy có {40+t*5} bạn thích bóng đá. Tỉ lệ phần trăm học sinh thích bóng đá là:", [f"{(40+t*5)/(100+t*10)*100:.1f}\\%", "40\\%", "50\\%", "35\\%"], 0),
            make_mc(7, "Thông hiểu", "Dữ liệu nào sau đây là không hợp lí khi thống kê điểm kiểm tra Toán 8?", ["Điểm kiểm tra của bạn An là 12 điểm", "Điểm kiểm tra của bạn Bình là 8,5 điểm", "Điểm kiểm tra của bạn Cúc là 10 điểm", "Điểm kiểm tra của bạn Dũng là 5 điểm"], 0),
            make_mc(8, "Thông hiểu", "Khi đọc biểu đồ đoạn thẳng về nhiệt độ các tháng trong năm, tháng có nhiệt độ cao nhất tương ứng với:", ["Điểm cao nhất trên đường gấp khúc", "Điểm thấp nhất trên đường gấp khúc", "Điểm đầu tiên", "Điểm cuối cùng"], 0),
            make_mc(9, "Vận dụng", f"Biểu đồ hình quạt tròn biểu diễn ngân sách chi tiêu tháng 10 của gia đình bác Hùng gồm: Ăn uống ($50\\%$), Giáo dục (${15+t}\\%$), Tiết kiệm ($15\\%$), Chi tiêu khác (${20-t}\\%$). Biết tổng thu nhập tháng 10 là 20 triệu đồng. Số tiền chi cho giáo dục là:", [f"{20 * (15+t) / 100:.2f} triệu đồng", "3 triệu đồng", "4 triệu đồng", "5 triệu đồng"], 0),
            make_mc(10, "Vận dụng", f"Số lượng xe máy bán được của một đại lý trong 4 quý lần lượt là: Quý 1: {120+t*10} xe, Quý 2: {150+t*10} xe, Quý 3: {180+t*10} xe, Quý 4: {200+t*10} xe. Số lượng xe bán được ở Quý 4 tăng so với Quý 1 bao nhiêu phần trăm?", [f"{((200+t*10) - (120+t*10))/(120+t*10)*100:.1f}\\%", "50\\%", "60\\%", "40\\%"], 0),
            make_mc(11, "Vận dụng", f"Một trường THCS có {800+t*50} học sinh. Trong đó tỉ lệ tham gia câu lạc bộ Thể thao là 35%, Nghệ thuật là 25%, STEM là 20%, còn lại chưa tham gia. Số học sinh tham gia câu lạc bộ STEM là:", [f"{(800+t*50)*0.2:.0f} học sinh", "160 học sinh", "200 học sinh", "180 học sinh"], 0),
            make_mc(12, "Vận dụng cao", "Một báo cáo kinh tế vẽ biểu đồ cột bị kéo giãn trục tung không bắt đầu từ số 0, khiến cho doanh số năm nay trông gấp 5 lần năm ngoái trong khi thực tế chỉ tăng 20%. Sai lầm này vi phạm nguyên tắc gì trong thống kê?", ["Làm sai lệch tỉ lệ trực quan của dữ liệu", "Thu thập số liệu sai", "Dùng sai biểu đồ tròn", "Lỗi chính tả"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về phân loại và biểu diễn dữ liệu (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Dữ liệu định lượng là dữ liệu biểu diễn bằng các số thực đo lường được.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Biểu đồ cột kép dùng để so sánh từng cặp số liệu của hai nhóm đối tượng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tổng phần trăm của tất cả các phần trong biểu đồ quạt tròn luôn bằng 100%.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Biểu đồ hình quạt tròn có thể thay thế hoàn hảo cho biểu đồ đoạn thẳng để thể hiện xu hướng tăng giảm theo thời gian.", "correct": False}
            ]),
            make_tf(2, f"Bảng thống kê xếp loại rèn luyện học kỳ 1 của lớp 8A có {40+t} học sinh gồm: Tốt: {24+t} bạn, Khá: 12 bạn, Đạt: 4 bạn, Chưa đạt: 0 bạn (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Tổng số học sinh được xếp loại rèn luyện là 40 + t học sinh.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tỉ lệ học sinh xếp loại Tốt chiếm trên 50% sĩ số cả lớp.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Số học sinh xếp loại Đạt chiếm 10% khi tổng số học sinh là 40.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Góc ở tâm của hình quạt biểu diễn số học sinh xếp loại Tốt nhỏ hơn 180 độ.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Trong biểu đồ quạt tròn, một hình quạt có góc ở tâm bằng {72+t*6} độ. Tính tỉ lệ phần trăm tương ứng của hình quạt đó (%).", f"{(72+t*6)/3.6:.1f}"),
            make_sa(2, "Thông hiểu", f"Thống kê điểm bài kiểm tra Toán của 10 bạn: 7, 8, 8, 9, {6+t%4}, 8, 10, 9, 8, 7. Điểm số có tần số xuất hiện nhiều nhất là bao nhiêu?", "8"),
            make_sa(3, "Vận dụng", f"Một công ty may có doanh thu Quý 1 là {100+t*10} triệu đồng, Quý 2 là {150+t*10} triệu đồng. Hỏi doanh thu Quý 2 tăng bao nhiêu triệu đồng so với Quý 1?", "50"),
            make_sa(4, "Vận dụng", f"Lớp 8B có 45 học sinh. Trong đợt khảo sát, có 60% học sinh đăng ký thi môn Toán, 40% thi môn Văn. Biết có {5+t} bạn đăng ký cả hai môn. Tính số bạn chỉ đăng ký thi đúng 1 môn.", f"{45 - (5+t)}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Bảng thống kê điểm kiểm tra giữa kì môn Toán của một lớp gồm: Điểm Giỏi: {15+t} học sinh, Điểm Khá: 15 học sinh, Điểm Trung bình: 8 học sinh, Điểm Yếu: 2 học sinh. Tính tổng số học sinh cả lớp và tỉ lệ phần trăm học sinh đạt điểm Giỏi.",
                       "\n".join([
                           f"Tổng số học sinh cả lớp: ({15+t}) + 15 + 8 + 2 = {40+t} (học sinh) (0.25đ).",
                           f"Số học sinh đạt loại Giỏi là {15+t} học sinh (0.25đ).",
                           f"Tỉ lệ phần trăm học sinh Giỏi: [({15+t}) / ({40+t})] . 100% (0.25đ).",
                           "Kết luận tỉ lệ phần trăm học sinh Giỏi (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một cửa hàng điện máy theo dõi lượng quạt sưởi bán được trong 4 tuần mùa đông: Tuần 1: {20+t*5} chiếc, Tuần 2: {35+t*5} chiếc, Tuần 3: {50+t*5} chiếc, Tuần 4: {30+t*5} chiếc. Em hãy vẽ bảng số liệu và tính mức tiêu thụ trung bình mỗi tuần của cửa hàng.",
                       "\n".join([
                           f"Tổng số quạt sưởi trong 4 tuần: ({20+t*5}) + ({35+t*5}) + ({50+t*5}) + ({30+t*5}) = {135 + 20*t} chiếc (0.25đ).",
                           "Số tuần theo dõi là 4 tuần (0.25đ).",
                           f"Mức tiêu thụ trung bình: ({135 + 20*t}) / 4 chiếc (0.25đ).",
                           "Kết luận mức tiêu thụ trung bình mỗi tuần (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Một bài báo đưa tin: 'Số vụ tai nạn giao thông tháng này đã giảm sốc 50% so với tháng trước'. Qua điều tra dữ liệu gốc, người ta thấy tháng trước có 2 vụ tai nạn và tháng này có 1 vụ. Phân tích xem thông tin trên bài báo có khách quan và thuyết phục không, nêu nguyên nhân.",
                       "\n".join([
                           "Về mặt toán học: (2 - 1)/2 = 50% là chính xác về tỉ lệ (0.25đ).",
                           "Tuy nhiên cỡ mẫu khảo sát quá nhỏ (chỉ 2 vụ giảm xuống 1 vụ) (0.25đ).",
                           "Sự biến động 1 vụ không phản ánh bản chất xu hướng an toàn giao thông (0.25đ).",
                           "Kết luận: Tiêu đề giật gân, thiếu tính thuyết phục về mặt ý nghĩa thống kê (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương V: Dữ liệu và biểu đồ - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương V: Dữ liệu và biểu đồ", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VI: Phân thức đại số (l_idx = 5)
# ------------------------------------------------------------------------------
def build_c6_8():
    chap_id = "c6_8"
    l_idx = 5
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Phân thức đại số là biểu thức có dạng $\\frac{{A}}{{B}}$, trong đó $A, B$ là những đa thức và (Đề {t:02d}):", ["$B$ khác đa thức 0", "$A$ khác đa thức 0", "$B$ là số tự nhiên", "$A, B$ cùng bậc"], 0),
            make_mc(2, "Nhận biết", "Hai phân thức $\\frac{A}{B}$ và $\\frac{C}{D}$ bằng nhau khi và chỉ khi:", ["$A \\cdot D = B \\cdot C$", "$A \\cdot C = B \\cdot D$", "$A + D = B + C$", "$A - D = B - C$"], 0),
            make_mc(3, "Nhận biết", f"Điều kiện xác định của phân thức $\\frac{{x + 1}}{{x - {t}}}$ là:", [f"$x \\neq {t}$", f"$x \\neq -{t}$", f"$x = {t}$", "$x \\neq -1$"], 0),
            make_mc(4, "Nhận biết", "Muốn rút gọn một phân thức, ta có thể chia cả tử và mẫu cho:", ["Nhân tử chung của chúng", "Một số thực bất kì", "Đa thức ở tử", "Đa thức ở mẫu"], 0),
            make_mc(5, "Thông hiểu", f"Rút gọn phân thức $\\frac{{{2*t}x^2y}}{{{4*t}xy^2}}$ ta được kết quả là:", ["$\\frac{x}{2y}$", "$\\frac{x}{y}$", "$\\frac{2x}{y}$", "$\\frac{1}{2xy}$"], 0),
            make_mc(6, "Thông hiểu", f"Kết quả của phép cộng $\\frac{{x - {t}}}{{x + 2}} + \\frac{{{t} + 2}}{{x + 2}}$ là:", ["$\\frac{x + 2}{x + 2} = 1$", "$\\frac{x}{x + 2}$", "$x + 2$", "$0$"], 0),
            make_mc(7, "Thông hiểu", f"Thực hiện phép nhân $\\frac{{x - {t}}}{{3x}} \\cdot \\frac{{6x^2}}{{x - {t}}}$ ta được:", ["$2x$", "$2$", "$x$", "$\\frac{2}{x}$"], 0),
            make_mc(8, "Thông hiểu", f"Giá trị của phân thức $\\frac{{x^2 - {t*t}}}{{x - {t}}}$ tại $x = {t + 5}$ là:", [f"${2*t + 5}$", f"${t + 5}$", "5", f"${2*t}$"], 0),
            make_mc(9, "Vận dụng", f"Một tổ công nhân theo kế hoạch may {300+t*50} chiếc áo trong $x$ ngày. Nhưng thực tế nhờ tăng năng suất mỗi ngày may thêm được 5 chiếc nên hoàn thành trước 2 ngày. Biểu thức thời gian thực tế hoàn thành là:", [f"$\\frac{{{300+t*50}}}{{x+5}}$ ngày", f"$\\frac{{{300+t*50}}}{{x}}$ ngày", f"$\\frac{{{300+t*50}}}{{x-2}}$ ngày", "$x - 2$ ngày"], 0),
            make_mc(10, "Vận dụng", f"Một người chèo thuyền xuôi dòng quãng đường {12+t} km với vận tốc dòng nước là 2 km/h. Vận tốc thực của thuyền là $v$ km/h ($v > 2$). Biểu thức thời gian xuôi dòng là:", [f"$\\frac{{{12+t}}}{{v + 2}}$ giờ", f"$\\frac{{{12+t}}}{{v - 2}}$ giờ", f"$\\frac{{{12+t}}}{{v}}$ giờ", f"$\\frac{{v + 2}}{{{12+t}}}$ giờ"], 0),
            make_mc(11, "Vận dụng", f"Biết phân thức $\\frac{{2x + {t}}}{{x - 1}} = 2 + \\frac{{A}}{{x - 1}}$. Đa thức $A$ có giá trị bằng:", [f"${t + 2}$", f"${t - 2}$", f"${t}$", "$2$"], 0),
            make_mc(12, "Vận dụng cao", f"Số giá trị nguyên của $x$ để phân thức $P = \\frac{{{t + 3}}}{{x - 2}}$ nhận giá trị nguyên là:", ["Số các ước nguyên của tử số", "2", "1", "Vô số"], 0)
        ]
        p2 = [
            make_tf(1, f"Cho phân thức đại số $P = \\frac{{x^2 - {t*t}}}{{x^2 - {2*t}x + {t*t}}}$ (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Mẫu thức P có thể viết dưới dạng hằng đẳng thức bình phương của một hiệu.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Điều kiện xác định của phân thức P là x khác {t}.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Rút gọn phân thức P ta được kết quả là (x + {t}) / (x - {t}).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tại x = 0 thì giá trị của phân thức P bằng 1.", "correct": False}
            ]),
            make_tf(2, f"Bài toán năng suất sản xuất (Mã đề {t:02d}): Một xưởng dệt được giao dệt 6 000 m vải trong thời gian x ngày (x nguyên dương).", [
                {"key": "a", "level": "Nhận biết", "text": "Năng suất dệt theo kế hoạch là 6 000 / x (m vải/ngày).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu tăng năng suất thêm 50 m/ngày thì năng suất mới là 6 000/x + 50.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Thời gian dệt thực tế tương ứng là 6 000 / (6 000/x + 50) ngày.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu thời gian dự định là 20 ngày thì số ngày hoàn thành thực tế ít hơn kế hoạch 5 ngày.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tìm điều kiện xác định của phân thức: (2x - 1) / (x + {3+t}).", f"x khác {-3-t}"),
            make_sa(2, "Thông hiểu", f"Tính giá trị của phân thức (x^2 - {4*t*t}) / (x + {2*t}) khi x = {2*t + 10}.", "10"),
            make_sa(3, "Vận dụng", f"Một ô tô đi từ A đến B dài {120+t*10} km với vận tốc x km/h, lúc về tăng vận tốc thêm 10 km/h. Viết biểu thức thời gian về ít hơn thời gian đi. Khi x = 50, thời gian đi là bao nhiêu giờ?", f"{(120+t*10)/50:.1f}"),
            make_sa(4, "Vận dụng", f"Tìm giá trị nguyên dương x để phân thức 6 / (x - 1) nhận giá trị nguyên lớn nhất.", "2")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho biểu thức $A = \\left(\\frac{{1}}{{x - {t}}} - \\frac{{1}}{{x + {t}}}\\right) : \\frac{{{2*t}}}{{x^2 - {t*t}}}$. Rút gọn biểu thức $A$.",
                       "\n".join([
                           f"Quy đồng mẫu thức trong ngoặc: [ (x + {t}) - (x - {t}) ] / (x^2 - {t*t}) = {2*t} / (x^2 - {t*t}) (0.25đ).",
                           f"Chia phân thức: A = [ {2*t} / (x^2 - {t*t}) ] . [ (x^2 - {t*t}) / {2*t} ] (0.25đ).",
                           "Rút gọn cả tử và mẫu ta được A = 1 (0.25đ).",
                           f"Kết luận giá trị biểu thức A = 1 với mọi x khác +-{t} (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Hai người thợ cùng làm chung một công việc trong ${t*2 + 4}$ giờ thì xong. Nếu làm riêng một mình thì người thứ nhất cần $x$ giờ và người thứ hai cần $y$ giờ để hoàn thành. Viết hệ thức liên hệ giữa $x$ và $y$ dưới dạng phân thức và tính số giờ người thứ hai hoàn thành một mình nếu người thứ nhất làm một mình mất ${t*4 + 8}$ giờ.",
                       "\n".join([
                           f"Phương trình liên hệ: 1/x + 1/y = 1/({t*2 + 4}) (0.25đ).",
                           f"Thay x = {t*4 + 8} vào phương trình: 1/({t*4 + 8}) + 1/y = 1/({t*2 + 4}) (0.25đ).",
                           f"Suy ra 1/y = 1/({t*2 + 4}) - 1/({t*4 + 8}) = 1/({t*4 + 8}) (0.25đ).",
                           f"Vậy y = {t*4 + 8} (giờ). Kết luận số giờ người thứ hai hoàn thành một mình (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Tìm tất cả các giá trị nguyên của $x$ để phân thức $P = \\frac{{2x + {t + 3}}}{{x - 1}}$ nhận giá trị là một số nguyên.",
                       "\n".join([
                           f"Biến đổi tử thức: 2x + {t + 3} = 2(x - 1) + {t + 5} (0.25đ).",
                           f"Khi đó P = 2 + ({t + 5})/(x - 1) (0.25đ).",
                           f"Để P nguyên thì ({t + 5}) chia hết cho (x - 1) => x - 1 thuộc Ư({t + 5}) (0.25đ).",
                           "Lập bảng tìm các giá trị nguyên của x thỏa mãn (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương VI: Phân thức đại số - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương VI: Phân thức đại số", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VII: Phương trình bậc nhất và hàm số bậc nhất (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c7_8():
    chap_id = "c7_8"
    l_idx = 6
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Phương trình nào sau đây là phương trình bậc nhất một ẩn (Đề {t:02d})?", [f"${t+1}x - {2*t} = 0$", f"$x^2 - {t} = 0$", "$0x + 5 = 0$", f"\\frac{{{t}}}{{x}} = 1"], 0),
            make_mc(2, "Nhận biết", "Hàm số bậc nhất là hàm số được cho bởi công thức có dạng:", ["$y = ax + b$ ($a \\neq 0$)", "$y = ax^2 + b$", "$y = \\frac{a}{x}$", "$y = ax^3$"], 0),
            make_mc(3, "Nhận biết", "Đồ thị của hàm số $y = ax + b$ ($a \\neq 0$) là:", ["Một đường thẳng", "Một đường parabol", "Một đường cong tròn", "Hai tia đối nhau"], 0),
            make_mc(4, "Nhận biết", "Hệ số góc của đường thẳng $y = 3x - 5$ là:", ["3", "-5", "5", "-3"], 0),
            make_mc(5, "Thông hiểu", f"Nghiệm của phương trình ${2*t}x - {6*t} = 0$ là:", ["$x = 3$", "$x = -3$", f"$x = {t}$", "$x = 0$"], 0),
            make_mc(6, "Thông hiểu", f"Điểm nào sau đây thuộc đồ thị hàm số $y = {t}x + 2$?", [f"$(1; {t + 2})$", f"$(1; {t})$", "$(0; 0)$", f"$({t}; 1)$"], 0),
            make_mc(7, "Thông hiểu", f"Đường thẳng $y = {t}x - 4$ cắt trục tung $Oy$ tại điểm có tọa độ:", ["$(0; -4)$", "$(-4; 0)$", f"$(0; {t})$", f"$({t}; 0)$"], 0),
            make_mc(8, "Thông hiểu", f"Hai đường thẳng $y = {2*t}x + 1$ và $y = 4x - 3$ song song với nhau khi $t$ bằng:", ["2", "4", "1", "-2"], 0),
            make_mc(9, "Vận dụng", f"Hãng taxi Sao Mai tính tiền cước gồm giá mở cửa 10 000 đồng và mỗi kilômét tiếp theo tính {12+t} nghìn đồng. Hàm số biểu diễn số tiền cước $y$ (nghìn đồng) theo quãng đường $x$ (km) là:", [f"$y = {12+t}x + 10$", f"$y = 10x + {12+t}$", f"$y = {12+t}x$", "$y = (12+t+10)x$"], 0),
            make_mc(10, "Vận dụng", f"Một bể bơi đang có 100 m$^3$ nước. Người ta mở một vòi nước chảy vào bể với lưu lượng ${15+t}$ m$^3$ mỗi giờ. Thể tích nước trong bể $V$ (m$^3$) sau $t$ giờ là hàm số:", [f"$V = {15+t}t + 100$", f"$V = 100t + {15+t}$", f"$V = {15+t}t$", "$V = 100 - (15+t)t$"], 0),
            make_mc(11, "Vận dụng", f"Nhiệt độ $T$ ($^\\circ$C) tại độ cao $h$ (km) so với mặt đất tính theo công thức: $T = 30 - 6,5h$. Tại độ cao $h = 2$ km thì nhiệt độ là:", ["17 $^\\circ$C", "23,5 $^\\circ$C", "13 $^\\circ$C", "20 $^\\circ$C"], 0),
            make_mc(12, "Vận dụng cao", f"Khoảng cách từ gốc tọa độ $O$ đến đường thẳng $d: y = {t}x + {2*t}$ đạt giá trị bằng:", [f"${2*t} / \\sqrt{{{t*t + 1}}}$", f"${2*t}$", f"${t}$", "1"], 0)
        ]
        p2 = [
            make_tf(1, f"Cho hàm số bậc nhất $y = ({t})x + {2*t}$ có đồ thị là đường thẳng $d$ (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Hệ số góc của đường thẳng d là một số dương nên hàm số đồng biến.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Đường thẳng d cắt trục tung tại điểm (0; {2*t}).", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Đường thẳng d cắt trục hoành tại điểm (-2; 0).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Góc tạo bởi đường thẳng d và trục Ox là góc tù.", "correct": False}
            ]),
            make_tf(2, f"Bài toán kinh tế tiền cước viễn thông (Mã đề {t:02d}): Thuê bao điện thoại trả sau có cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi nội mạng.", [
                {"key": "a", "level": "Nhận biết", "text": "Số tiền phải trả y (đồng) phụ thuộc vào số phút gọi x (phút) theo hàm bậc nhất y = 1 000x + 50 000.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu trong tháng gọi 100 phút thì số tiền phải trả là 150 000 đồng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu tháng đó phải trả 200 000 đồng thì số phút gọi là 150 phút.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số tiền cước tỉ lệ thuận tuyệt đối với số phút gọi không tính cước cố định.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Giải phương trình bậc nhất: 3x - {6+3*t} = 0.", f"{2+t}"),
            make_sa(2, "Thông hiểu", f"Tìm hệ số góc của đường thẳng y = {5*t}x - 12.", f"{5*t}"),
            make_sa(3, "Vận dụng", f"Một người đi xe máy từ A đến B với vận tốc 40 km/h hết x giờ. Khi về đi với vận tốc 50 km/h nên thời gian về ít hơn 30 phút (0,5 giờ). Tìm quãng đường AB (km).", "100"),
            make_sa(4, "Vận dụng", f"Điểm kiểm tra trung bình môn Toán cả năm tính theo công thức: ĐTB = (K1 + 2*K2) / 3. Bạn Lan có điểm học kỳ 1 K1 = {7+t%3}. Hỏi Lan cần đạt điểm K2 tối thiểu bao nhiêu để ĐTB đạt đúng 8,0?", f"{(24 - (7+t%3))/2:.1f}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Vẽ đồ thị của hàm số bậc nhất: $y = 2x - {2*t}$.",
                       "\n".join([
                           f"Xác định giao điểm với Oy: Cho x = 0 => y = -{2*t}, điểm A(0; -{2*t}) (0.25đ).",
                           f"Xác định giao điểm với Ox: Cho y = 0 => 2x = {2*t} => x = {t}, điểm B({t}; 0) (0.25đ).",
                           "Vẽ hệ trục tọa độ Oxy, biểu diễn hai điểm A và B (0.25đ).",
                           "Vẽ đường thẳng đi qua A và B ta được đồ thị hàm số (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một công ty du lịch dự định thuê xe chở ${120+t*10}$ học sinh đi dã ngoại. Có hai loại xe: loại xe 30 chỗ có giá thuê 1,2 triệu đồng/xe và loại xe 45 chỗ có giá 1,6 triệu đồng/xe. Hỏi công ty nên thuê bao nhiêu xe mỗi loại để vừa chở hết số học sinh, vừa tiết kiệm chi phí nhất?",
                       "\n".join([
                           f"Phân tích các phương án chở đủ {120+t*10} học sinh (0.25đ).",
                           "Phương án 1: Thuê xe 45 chỗ (0.25đ).",
                           "Phương án 2: Thuê kết hợp xe 45 chỗ và 30 chỗ (0.25đ).",
                           "So sánh chi phí từng phương án và kết luận phương án tiết kiệm nhất (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Tìm tọa độ điểm cố định mà đường thẳng $(d): (a - 1)x + (2a + 3)y - 5a + 1 = 0$ luôn đi qua với mọi giá trị của tham số $a$.",
                       "\n".join([
                           "Biến đổi phương trình đường thẳng theo a: a(x + 2y - 5) - (x - 3y - 1) = 0 (0.25đ).",
                           "Đường thẳng luôn đi qua điểm cố định khi: x + 2y - 5 = 0 và x - 3y - 1 = 0 (0.25đ).",
                           "Giải hệ phương trình ta được: y = 4/5 và x = 17/5 (0.25đ).",
                           "Kết luận tọa độ điểm cố định là (17/5; 4/5) (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương VII: Phương trình bậc nhất và hàm số bậc nhất - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương VII: Phương trình bậc nhất và hàm số bậc nhất", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VIII: Mở đầu về tính xác suất của biến cố (l_idx = 4)
# ------------------------------------------------------------------------------
def build_c8_8():
    chap_id = "c8_8"
    l_idx = 4
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Biến cố nào sau đây là biến cố chắc chắn (Đề {t:02d})?", ["Ngày mai Mặt Trời mọc ở đằng Đông", "Gieo con xúc xắc xuất hiện mặt 7 chấm", "Bốc một lá bài được lá bài màu xanh", "Hôm nay trời mưa"], 0),
            make_mc(2, "Nhận biết", "Biến cố không thể là biến cố có xác suất bằng:", ["0", "1", "0,5", "-1"], 0),
            make_mc(3, "Nhận biết", "Gieo một đồng xu cân đối và đồng chất thì xác suất xuất hiện mặt Ngửa bằng:", ["$\\frac{1}{2}$", "1", "0", "$\\frac{1}{4}$"], 0),
            make_mc(4, "Nhận biết", "Xác suất của một biến cố ngẫu nhiên luôn nhận giá trị trong đoạn:", ["$[0; 1]$", "$[-1; 1]$", "$[1; 2]$", "$[0; 100]$"], 0),
            make_mc(5, "Thông hiểu", f"Gieo một con xúc xắc 6 mặt cân đối. Xác suất xuất hiện mặt có số chấm là số chẵn bằng:", ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"], 0),
            make_mc(6, "Thông hiểu", f"Một hộp chứa {10+t*2} viên bi gồm 5 bi đỏ, còn lại là bi xanh. Lấy ngẫu nhiên 1 viên bi. Xác suất lấy được bi đỏ là:", [f"$\\frac{{5}}{{{10+t*2}}}$", "$\\frac{1}{2}$", "$\\frac{1}{5}$", "$\\frac{1}{10}$"], 0),
            make_mc(7, "Thông hiểu", f"Rút ngẫu nhiên một tấm thẻ từ hộp có 20 thẻ đánh số từ 1 đến 20. Xác suất rút được thẻ ghi số chia hết cho 5 là:", ["$\\frac{1}{5} = 0,2$", "$\\frac{1}{4}$", "$\\frac{1}{10}$", "$\\frac{1}{2}$"], 0),
            make_mc(8, "Thông hiểu", "Một lớp học có 20 bạn nam và 20 bạn nữ. Chọn ngẫu nhiên 1 bạn làm bí thư chi đoàn. Biến cố 'chọn được bạn nam' và 'chọn được bạn nữ' là hai biến cố:", ["Có cùng xác suất (đồng khả năng)", "Chắc chắn", "Không thể", "Đối nghịch"], 0),
            make_mc(9, "Vận dụng", f"Hội chợ xuân trường học tổ chức trò chơi vòng quay may mắn gồm {12+t} ô hình quạt bằng nhau, trong đó có 3 ô trúng thưởng thú bông, 4 ô trúng vở viết, còn lại là ô chúc bạn may mắn. Xác suất quay vào ô có quà (thú bông hoặc vở viết) là:", [f"$\\frac{{7}}{{{12+t}}}$", "$\\frac{1}{2}$", "$\\frac{3}{12}$", "$\\frac{4}{12}$"], 0),
            make_mc(10, "Vận dụng", f"Trong đợt khảo sát {100+t*20} người tiêu dùng về một sản phẩm mới, có {75+t*15} người đánh giá hài lòng. Xác suất thực nghiệm một người được chọn ngẫu nhiên hài lòng về sản phẩm là:", [f"{(75+t*15)/(100+t*20):.2f}", "0,8", "0,7", "0,9"], 0),
            make_mc(11, "Vận dụng", "Gieo đồng thời hai con xúc xắc cân đối. Số kết quả thuận lợi để tổng số chấm trên hai con xúc xắc bằng 7 là:", ["6", "5", "4", "7"], 0),
            make_mc(12, "Vận dụng cao", "Gieo đồng thời hai con xúc xắc cân đối 6 mặt. Xác suất để tổng số chấm xuất hiện trên hai con xúc xắc là một số nguyên tố bằng:", ["$\\frac{15}{36} = \\frac{5}{12}$", "$\\frac{7}{36}$", "$\\frac{1}{2}$", "$\\frac{1}{3}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về xác suất thực nghiệm (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Khi số lần thử nghiệm càng lớn thì xác suất thực nghiệm càng tiến gần đến xác suất lý thuyết.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Gieo một con xúc xắc 100 lần thấy xuất hiện mặt 6 chấm 18 lần thì xác suất thực nghiệm là 0,18.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Xác suất xuất hiện mặt có số chấm lớn hơn 6 khi gieo xúc xắc 6 mặt là 0.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu gieo xúc xắc 5 lần đều ra mặt 1 chấm thì lần thứ 6 chắc chắn không ra mặt 1 chấm.", "correct": False}
            ]),
            make_tf(2, f"Trong một hộp kín có {10+t} viên bi màu xanh và 10 viên bi màu đỏ có kích thước và khối lượng hoàn toàn như nhau (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Hành động lấy ngẫu nhiên 1 viên bi trong hộp là một phép thử ngẫu nhiên.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Tổng số kết quả có thể xảy ra khi lấy 1 viên bi là {20+t}.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Xác suất lấy được viên bi màu đỏ là 10 / ({20+t}).", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Xác suất lấy được viên bi màu xanh luôn nhỏ hơn 0,5 với mọi giá trị t.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm lớn hơn 4.", "0.33"),
            make_sa(2, "Thông hiểu", f"Một hộp có 4 quả bóng vàng và {6+t} quả bóng xanh. Lấy ngẫu nhiên 1 quả. Tính số kết quả có thể xảy ra.", f"{10+t}"),
            make_sa(3, "Vận dụng", "Tung một đồng xu 50 lần thấy có 28 lần xuất hiện mặt Ngửa. Tính xác suất thực nghiệm xuất hiện mặt Sấp.", "0.44"),
            make_sa(4, "Vận dụng", "Trong một kỳ thi học sinh giỏi có 100 thí sinh dự thi. Trong đó có 15 giải Nhất, 25 giải Nhì, 30 giải Ba. Chọn ngẫu nhiên một thí sinh, tính xác suất thí sinh đó đạt giải Nhất hoặc giải Nhì.", "0.4")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Một túi kẹo có {8+t} chiếc kẹo vị cam và 12 chiếc kẹo vị dâu có bao bì giống nhau. Lấy ngẫu nhiên một chiếc kẹo. Tính xác suất để lấy được kẹo vị cam và kẹo vị dâu.",
                       "\n".join([
                           f"Tổng số chiếc kẹo trong túi: ({8+t}) + 12 = {20+t} chiếc (0.25đ).",
                           f"Số kết quả thuận lợi cho biến cố lấy kẹo vị cam là {8+t} (0.25đ).",
                           f"Xác suất lấy được kẹo cam: P(Cam) = ({8+t}) / ({20+t}) (0.25đ).",
                           f"Xác suất lấy được kẹo dâu: P(Dâu) = 12 / ({20+t}) (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Trong một đợt kiểm tra sức khỏe tại trường học có {200+t*50} học sinh được khám mắt. Kết quả có {60+t*10} học sinh bị tật khúc xạ (cận thị/loạn thị). Hãy ước lượng xác suất một học sinh của trường bị tật khúc xạ và dự đoán nếu toàn trường có 1 200 học sinh thì có khoảng bao nhiêu em bị tật khúc xạ.",
                       "\n".join([
                           f"Xác suất thực nghiệm tật khúc xạ: P = ({60+t*10}) / ({200+t*50}) (0.25đ).",
                           "Tỉ lệ này ước lượng tỉ lệ chung toàn trường (0.25đ).",
                           "Dự đoán số học sinh tật khúc xạ: N = 1 200 . P (0.25đ).",
                           "Tính toán số liệu cụ thể và đưa ra khuyến nghị bảo vệ mắt (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Tính xác suất để tích số chấm trên mặt xuất hiện của hai con xúc xắc là một số chia hết cho 6.",
                       "\n".join([
                           "Tổng số kết quả có thể xảy ra: 6 . 6 = 36 kết quả (0.25đ).",
                           "Tích hai số chấm chia hết cho 6 khi tích chia hết cho cả 2 và 3 (0.25đ).",
                           "Liệt kê các trường hợp thuận lợi gồm 15 kết quả (0.25đ).",
                           "Vậy xác suất là 15/36 = 5/12 (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương VIII: Mở đầu về tính xác suất của biến cố - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương VIII: Mở đầu về tính xác suất của biến cố", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG IX: Tam giác đồng dạng (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c9_8():
    chap_id = "c9_8"
    l_idx = 6
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Hai tam giác đồng dạng với nhau khi (Đề {t:02d}):", ["Các góc tương ứng bằng nhau và các cạnh tương ứng tỉ lệ", "Các cạnh tương ứng bằng nhau", "Các góc tương ứng bằng nhau", "Diện tích của chúng bằng nhau"], 0),
            make_mc(2, "Nhận biết", "Nếu tam giác $ABC$ đồng dạng với tam giác $A'B'C'$ theo tỉ số $k$ thì tỉ số diện tích của hai tam giác đó bằng:", ["$k^2$", "$k$", "$2k$", "$\\sqrt{k}$"], 0),
            make_mc(3, "Nhận biết", "Trường hợp đồng dạng thứ nhất của tam giác (c.c.c) là:", ["Ba cạnh của tam giác này tỉ lệ với ba cạnh của tam giác kia", "Ba cạnh của hai tam giác bằng nhau", "Hai cạnh và góc xen giữa tỉ lệ", "Hai góc bằng nhau"], 0),
            make_mc(4, "Nhận biết", "Tam giác vuông $ABC$ ($A = 90^\\circ$) và tam giác vuông $DEF$ ($D = 90^\\circ$) đồng dạng với nhau khi có thêm điều kiện:", ["Một góc nhọn bằng nhau", "Một cạnh góc vuông bằng nhau", "Cạnh huyền bằng nhau", "Chu vi bằng nhau"], 0),
            make_mc(5, "Thông hiểu", f"Cho $\\Delta ABC \\sim \\Delta A'B'C'$ theo tỉ số $k = {t}$. Biết chu vi $\\Delta ABC$ là ${12*t}$ cm thì chu vi $\\Delta A'B'C'$ là:", ["12 cm", f"${12*t*t}$ cm", f"${12*t}$ cm", f"${24*t}$ cm"], 0),
            make_mc(6, "Thông hiểu", f"Cho tam giác $ABC$ có $AB = {3*t}$ cm, $AC = {4*t}$ cm, $BC = {5*t}$ cm. Tam giác $ABC$ là:", ["Tam giác vuông tại A", "Tam giác nhọn", "Tam giác tù", "Tam giác đều"], 0),
            make_mc(7, "Thông hiểu", f"Cho $\\Delta ABC$ có đường cao $AH$. Khẳng định nào sau đây là ĐÚNG?", ["$\\Delta ABH \\sim \\Delta CAH$", "$\\Delta ABH = \\Delta CAH$", "$AH^2 = AB \\cdot AC$", "$AB^2 = AH \\cdot BC$"], 0),
            make_mc(8, "Thông hiểu", f"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = {4*t}$ cm, $CH = {9*t}$ cm. Độ dài $AH$ bằng:", [f"${6*t}$ cm", f"${13*t}$ cm", f"${36*t}$ cm", f"${5*t}$ cm"], 0),
            make_mc(9, "Vận dụng", f"Một cột cờ cao $h$ có bóng dài ${6+t}$ mét trên mặt đất. Cùng lúc đó một cọc tiêu cao $1,5$ mét cắm thẳng đứng có bóng dài $1$ mét. Chiều cao $h$ của cột cờ là:", [f"{1.5*(6+t):.2f} mét", "9 mét", "10 mét", "12 mét"], 0),
            make_mc(10, "Vận dụng", f"Người ta dùng giác kế và gương phẳng đặt nằm ngang tại điểm $C$ để đo chiều cao ngọn hải đăng. Khoảng cách từ chân hải đăng đến gương là ${40+t*5}$ mét. Người đo đứng cách gương $2$ mét và có mắt cao $1,6$ mét so với mặt đất. Chiều cao ngọn hải đăng là:", [f"{(40+t*5)*1.6/2:.1f} mét", "32 mét", "40 mét", "50 mét"], 0),
            make_mc(11, "Vận dụng", f"Bản vẽ thiết kế của một ngôi nhà có tỉ lệ xích $1 : 100$. Trên bản vẽ, chiều dài phòng khách đo được $6$ cm. Chiều dài thực tế của phòng khách đó là:", ["6 mét", "60 mét", "0,6 mét", "600 mét"], 0),
            make_mc(12, "Vận dụng cao", "Cho hình vuông $ABCD$. Điểm $E$ thuộc cạnh $BC$. Tia $AE$ cắt đường thẳng $CD$ tại $F$. Hệ thức nào sau đây luôn ĐÚNG?", ["$\\frac{1}{AB^2} = \\frac{1}{AE^2} + \\frac{1}{AF^2}$", "$\\frac{1}{AB} = \\frac{1}{AE} + \\frac{1}{AF}$", "$AB^2 = AE \\cdot AF$", "$AB = AE + AF$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tam giác đồng dạng (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số k = 1.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tỉ số hai đường cao tương ứng của hai tam giác đồng dạng bằng tỉ số đồng dạng k.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tỉ số diện tích của hai tam giác đồng dạng bằng bình phương tỉ số đồng dạng k^2.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu hai tam giác có diện tích bằng nhau thì chắc chắn đồng dạng với nhau.", "correct": False}
            ]),
            make_tf(2, f"Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$), đường cao $AH$ (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Tam giác HBA đồng dạng với tam giác ABC theo trường hợp góc - góc.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hệ thức AB^2 = BH . BC luôn đúng trong tam giác vuông.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Độ dài đường cao AH thỏa mãn hệ thức AH^2 = BH . CH.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích tam giác HBA luôn bằng diện tích tam giác HAC.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Cho tam giác ABC đồng dạng tam giác DEF theo tỉ số k = 2/3. Biết chu vi tam giác ABC là {20+2*t} cm. Tính chu vi tam giác DEF (cm).", f"{(20+2*t)*1.5:.1f}"),
            make_sa(2, "Thông hiểu", f"Một tam giác vuông có hai cạnh góc vuông là {6*t} cm và {8*t} cm. Tính độ dài cạnh huyền (cm).", f"{10*t}"),
            make_sa(3, "Vận dụng", f"Để đo bề rộng khúc sông AB, người ta xác định được hai tam giác đồng dạng có tỉ số k = 4. Đoạn thẳng tương ứng trên bờ đo được {15+t} mét. Tính khoảng cách AB giữa hai bờ sông (mét).", f"{4*(15+t)}"),
            make_sa(4, "Vận dụng", f"Cho tam giác ABC vuông tại A, AH là đường cao. Biết BH = 4 cm, BC = {16+t} cm. Tính độ dài cạnh AB (làm tròn 1 chữ số thập phân, cm).", f"{(4*(16+t))**0.5:.1f}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho tam giác $ABC$ nhọn có hai đường cao $BD$ và $CE$ cắt nhau tại $H$. Chứng minh rằng: $\\Delta ABD \\sim \\Delta ACE$ và $AB \\cdot AE = AC \\cdot AD$.",
                       "\n".join([
                           "Xét tam giác ABD và ACE có: góc ADB = AEC = 90 độ, góc A chung (0.25đ).",
                           "Suy ra tam giác ABD đồng dạng tam giác ACE (g.g) (0.25đ).",
                           "Từ tỉ số đồng dạng suy ra: AB / AC = AD / AE (0.25đ).",
                           "Nhân chéo ta được đẳng thức: AB . AE = AC . AD (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một tháp truyền hình có bóng đổ dài ${50+t*5}$ mét trên mặt đất. Cùng thời điểm đó, một thanh sắt cao $2$ mét cắm thẳng đứng có bóng dài $1,2$ mét. Tính chiều cao của tháp truyền hình (làm tròn đến mét).",
                       "\n".join([
                           f"Chiều cao thanh sắt là h = 2 m, bóng là l = 1,2 m; bóng tháp là L = {50+t*5} m (0.25đ).",
                           "Tia nắng mặt trời song song nên hai tam giác đồng dạng: H / h = L / l (0.25đ).",
                           f"Suy ra H = 2 . ({50+t*5}) / 1,2 (0.25đ).",
                           "Kết luận chiều cao ngọn tháp (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ có ba góc nhọn, các đường cao $AD, BE, CF$ cắt nhau tại $H$. Chứng minh rằng: $H$ là tâm đường tròn nội tiếp của tam giác $DEF$.",
                       "\n".join([
                           "Chứng minh các tứ giác nội tiếp hoặc các cặp tam giác đồng dạng (0.25đ).",
                           "Suy ra góc HDF = góc HDE => DH là tia phân giác góc FDE (0.25đ).",
                           "Tương tự EH, FH là các phân giác của góc DEF, DFE trong tam giác DEF (0.25đ).",
                           "Vậy H là giao điểm 3 đường phân giác, tức tâm đường tròn nội tiếp tam giác DEF (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương IX: Tam giác đồng dạng - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương IX: Tam giác đồng dạng", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG X: Một số hình khối trong thực tiễn (l_idx = 3)
# ------------------------------------------------------------------------------
def build_c10_8():
    chap_id = "c10_8"
    l_idx = 3
    exams = load_existing_exams(chap_id, 8)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Hình chóp tam giác đều có mặt đáy là (Đề {t:02d}):", ["Tam giác đều", "Tam giác vuông", "Tam giác cân", "Tam giác vuông cân"], 0),
            make_mc(2, "Nhận biết", "Các mặt bên của hình chóp tứ giác đều là những:", ["Tam giác cân", "Tam giác đều", "Hình vuông", "Hình chữ nhật"], 0),
            make_mc(3, "Nhận biết", "Thể tích của hình chóp có diện tích đáy $S$ và chiều cao $h$ được tính bởi:", ["$V = \\frac{1}{3} S \\cdot h$", "$V = S \\cdot h$", "$V = \\frac{1}{2} S \\cdot h$", "$V = 3 S \\cdot h$"], 0),
            make_mc(4, "Nhận biết", "Diện tích xung quanh của hình chóp tam giác đều bằng:", ["Tổng diện tích của 3 mặt bên", "Diện tích đáy", "Tổng diện tích đáy và mặt bên", "Nửa diện tích các mặt bên"], 0),
            make_mc(5, "Thông hiểu", f"Một hình chóp tứ giác đều có cạnh đáy bằng ${4*t}$ cm và chiều cao bằng $6$ cm. Thể tích hình chóp là:", [f"${32*t*t}$ cm$^3$", f"${96*t*t}$ cm$^3$", f"${16*t*t}$ cm$^3$", f"${64*t*t}$ cm$^3$"], 0),
            make_mc(6, "Thông hiểu", f"Một hình chóp tam giác đều có diện tích đáy bằng ${10*t}$ cm$^2$, chiều cao bằng $9$ cm. Thể tích của hình chóp là:", [f"${30*t}$ cm$^3$", f"${90*t}$ cm$^3$", f"${45*t}$ cm$^3$", f"${15*t}$ cm$^3$"], 0),
            make_mc(7, "Thông hiểu", f"Một hình chóp tứ giác đều có cạnh đáy bằng ${6*t}$ cm, trung đoạn dài ${5*t}$ cm. Diện tích xung quanh của hình chóp là:", [f"${60*t*t}$ cm$^2$", f"${120*t*t}$ cm$^2$", f"${30*t*t}$ cm$^2$", f"${90*t*t}$ cm$^2$"], 0),
            make_mc(8, "Thông hiểu", "Hình chóp tam giác đều có số đỉnh, số mặt và số cạnh lần lượt là:", ["4 đỉnh, 4 mặt, 6 cạnh", "3 đỉnh, 4 mặt, 5 cạnh", "5 đỉnh, 5 mặt, 8 cạnh", "4 đỉnh, 5 mặt, 6 cạnh"], 0),
            make_mc(9, "Vận dụng", f"Người ta làm một chiếc lều cắm trại hình chóp tứ giác đều có cạnh đáy ${2+t*0.2:.1f}$ mét và chiều cao $2$ mét. Trung đoạn của chiếc lều xấp xỉ bằng $2,3$ mét. Diện tích vải bạt cần để phủ 4 mặt bên chiếc lều (không tính đáy) là:", [f"{4 * (2+t*0.2) * 2.3 / 2:.2f} mét vuông", "10 mét vuông", "15 mét vuông", "8 mét vuông"], 0),
            make_mc(10, "Vận dụng", f"Một hộp quà lưu niệm hình chóp tam giác đều có cạnh đáy ${10+t}$ cm và trung đoạn $12$ cm. Diện tích xung quanh hộp quà là:", [f"{3 * (10+t) * 12 / 2:.1f} cm$^2$", "150 cm$^2$", "200 cm$^2$", "180 cm$^2$"], 0),
            make_mc(11, "Vận dụng", f"Kim tự tháp Louvre tại Pháp có dạng hình chóp tứ giác đều với cạnh đáy dài $35$ mét và chiều cao $21$ mét. Thể tích không gian bên trong kim tự tháp Louvre là:", ["$8 575$ mét khối", "$25 725$ mét khối", "$10 000$ mét khối", "$12 000$ mét khối"], 0),
            make_mc(12, "Vận dụng cao", "Một chiếc đèn thả trần hình chóp tứ giác đều có các cạnh bên bằng nhau và góc giữa cạnh bên và mặt đáy là $45^\\circ$. Biết cạnh đáy bằng $a$. Chiều cao của chiếc đèn tính theo $a$ là:", ["$\\frac{a\\sqrt{2}}{2}$", "$a$", "$\\frac{a}{2}$", "$a\\sqrt{2}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về hình chóp đều (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Hình chóp tứ giác đều có đáy là hình vuông và các mặt bên là các tam giác cân bằng nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Trung đoạn của hình chóp đều là đường cao của một mặt bên xuất phát từ đỉnh hình chóp.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Thể tích của hình chóp bằng một phần ba tích của diện tích đáy và chiều cao.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Diện tích toàn phần của hình chóp luôn bằng hai lần diện tích xung quanh.", "correct": False}
            ]),
            make_tf(2, f"Bài toán thiết kế hộp đựng bánh trung thu hình chóp tứ giác đều có cạnh đáy a = {6*t} cm, chiều cao h = {4*t} cm (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Diện tích đáy của hộp bánh là S_đáy = a^2 = 36*t^2 cm^2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Trung đoạn d của hình chóp tính theo Pythagore là d = căn(h^2 + (a/2)^2) = {5*t} cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Diện tích xung quanh của hộp bánh là S_xq = 4 . (1/2 . a . d) = {60*t*t} cm^2.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Thể tích hộp bánh lớn hơn 2 lít với mọi giá trị của t từ 1 đến 7.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính thể tích của hình chóp tứ giác đều có diện tích đáy 25 cm^2 và chiều cao {6+3*t} cm (cm^3).", f"{25 * (6+3*t) // 3}"),
            make_sa(2, "Thông hiểu", f"Một hình chóp tam giác đều có 3 mặt bên là 3 tam giác có diện tích mỗi mặt bằng {15+t} cm^2. Tính diện tích xung quanh (cm^2).", f"{3*(15+t)}"),
            make_sa(3, "Vận dụng", "Một khối rubik hình chóp tam giác đều có cạnh đáy 6 cm, chiều cao mặt đáy 5,2 cm và chiều cao hình chóp 5 cm. Tính thể tích khối rubik (làm tròn 1 chữ số thập phân, cm^3).", "26.0"),
            make_sa(4, "Vận dụng", "Người ta đúc một cột mốc bằng bê tông dạng hình chóp tứ giác đều có cạnh đáy 0,4 mét và chiều cao 0,9 mét. Biết mỗi mét khối bê tông nặng 2 400 kg. Tính khối lượng cột mốc (kg).", "115.2")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Một hình chóp tứ giác đều có cạnh đáy bằng ${8*t}$ cm, trung đoạn dài ${5*t}$ cm. Tính diện tích xung quanh và diện tích toàn phần của hình chóp đó.",
                       "\n".join([
                           f"Nửa chu vi đáy p = 4 . {8*t} / 2 = {16*t} (cm) (0.25đ).",
                           f"Diện tích xung quanh: S_xq = p . d = {16*t} . {5*t} = {80*t*t} (cm^2) (0.25đ).",
                           f"Diện tích đáy S_đáy = ({8*t})^2 = {64*t*t} (cm^2) (0.25đ).",
                           f"Diện tích toàn phần S_tp = S_xq + S_đáy = {144*t*t} (cm^2) (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Bác Ba làm một mái che giếng trời bằng kính cường lực có dạng hình chóp tứ giác đều. Cạnh đáy hình vuông dài ${2+t*0.2:.1f}$ mét, chiều cao từ đỉnh chóp xuống tâm đáy là $1,2$ mét. Biết giá tiền kính cường lực kèm khung nhôm là $1 500 000$ đồng mỗi mét vuông. Tính số tiền bác Ba cần chi trả để lắp đặt 4 mặt bên của mái che giếng trời.",
                       "\n".join([
                           "Tính độ dài trung đoạn của mái che theo định lí Pythagore (0.25đ).",
                           "Tính diện tích xung quanh của 4 mặt bên kính cường lực (0.25đ).",
                           "Nhân diện tích với đơn giá 1 500 000 đồng/m^2 (0.25đ).",
                           "Kết luận tổng số tiền bác Ba cần chi trả (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Một chiếc lều hình chóp tứ giác đều có thể tích $V = 18\\text{ m}^3$. Hỏi cần thiết kế chiều cao $h$ và cạnh đáy $a$ như thế nào để tổng diện tích vải bạt xung quanh lều là nhỏ nhất?",
                       "\n".join([
                           "Công thức thể tích: V = 1/3 . a^2 . h = 18 => h = 54 / a^2 (0.25đ).",
                           "Trung đoạn d = căn(h^2 + a^2/4) = căn(54^2/a^4 + a^2/4) (0.25đ).",
                           "Diện tích xung quanh S_xq = 2 . a . d = 2 . căn(54^2/a^2 + a^4/4) (0.25đ).",
                           "Áp dụng bất đẳng thức Cauchy tìm được giá trị nhỏ nhất của diện tích xung quanh (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài kiểm tra cuối Chương X: Một số hình khối trong thực tiễn - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(8, chap_id, "Chương X: Một số hình khối trong thực tiễn", exams)


# ------------------------------------------------------------------------------
# HÀM CHẠY TOÀN BỘ 10 CHƯƠNG TOÁN 8
# ------------------------------------------------------------------------------
def run_all_grade8():
    print("=== BẮT ĐẦU SINH 7 ĐỀ ĐỘC LẬP CHO TOÀN BỘ 10 CHƯƠNG TOÁN 8 ===")
    build_c1_8()
    build_c2_8()
    build_c3_8()
    build_c4_8()
    build_c5_8()
    build_c6_8()
    build_c7_8()
    build_c8_8()
    build_c9_8()
    build_c10_8()
    print("=== HOÀN TẤT XUẤT SẮC TOÁN 8: 10 CHƯƠNG x 7 ĐỀ = 70 ĐỀ CHUẨN MA TRẬN ===")

if __name__ == "__main__":
    run_all_grade8()
