# -*- coding: utf-8 -*-
"""
GENERATOR BỘ ĐỀ THI ĐỊNH KỲ TOÁN 8 (GIỮA KỲ 2 & CUỐI KỲ 2)
6 mã đề Giữa kỳ 2 + 6 mã đề Cuối kỳ 2.
Chuẩn ma trận GDPT 2018 (Kết nối tri thức) & Validator kiểm soát:
- 30% NB (3.0đ), 30% TH (3.0đ), 20% VD (2.0đ), 20% VDC (2.0đ) = 10.0đ
- Phần II: Đúng 1 ý Vận dụng mỗi câu lớn
- Phần III: 1 VD, 1 VDC, 2 cơ bản
- Phần IV: Câu 1 (1.0đ NB), Câu 2 (1.0đ TH), Câu 3 (0.5đ VD), Câu 4 (0.5đ VDC)
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
from periodic_validator import validate_periodic_exam
from build_periodic_grade8_term1 import generate_g8_mid1, generate_g8_final1

def make_mc(qid, level, q_text, options, correct, exp):
    return {
        "id": qid,
        "level": level,
        "points": 0.25,
        "question": q_text,
        "options": options,
        "correct": correct,
        "explanation": exp
    }

def make_tf(qid, stem, stmts):
    return {
        "id": qid,
        "stem": stem,
        "statements": stmts
    }

def make_sa(qid, level, q_text, ans, acceptable, exp):
    if not acceptable:
        acceptable = [str(ans)]
    elif str(ans) not in acceptable:
        acceptable.insert(0, str(ans))
    return {
        "id": qid,
        "level": level,
        "points": 0.5,
        "question": q_text,
        "answer": str(ans),
        "acceptableAnswers": acceptable,
        "explanation": exp
    }

def make_essay(qid, level, points, q_text, rubric, model_sol):
    return {
        "id": qid,
        "level": level,
        "points": points,
        "question": q_text,
        "rubric": rubric,
        "modelSolution": model_sol
    }

# ==============================================================================
# 6 MÃ ĐỀ GIỮA KỲ 2 - TOÁN 8 (mid2)
# Phạm vi: Phân thức đại số, Phương trình & Hàm số bậc nhất, Tam giác đồng dạng
# ==============================================================================
def generate_g8_mid2():
    exams = []
    
    for t_idx in range(1, 7):
        ex_num = f"0{t_idx}"
        topics = [
            "Phân thức đại số, Phương trình bậc nhất một ẩn & Ba trường hợp tam giác đồng dạng",
            "Cộng trừ phân thức, Hàm số bậc nhất y = ax + b & Trường hợp đồng dạng góc - góc",
            "Rút gọn phân thức, Giải toán lập phương trình chuyển động & Tỉ số đồng dạng",
            "Nhân chia phân thức, Hệ số góc của đường thẳng & Tam giác đồng dạng cạnh - góc - cạnh",
            "Điều kiện xác định phân thức, Phương trình tích & Ứng dụng thực tế tam giác đồng dạng",
            "Tổng hợp giữa kỳ 2: Phân thức, Phương trình, Đồ thị hàm số & Hình học đồng dạng"
        ]
        topic = topics[t_idx - 1]

        exams.append({
            "id": f"p_g8_mid2_{ex_num}",
            "testNum": t_idx,
            "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ II - TOÁN 8 (ĐỀ SỐ {ex_num})",
            "topic": topic,
            "grade": "8",
            "term": "mid2",
            "termName": "Giữa Học kỳ II",
            "duration": "90 phút",
            "totalPoints": 10.0,
            "matrix": {
                "nhanBiet": "30% (3,0 điểm)",
                "thongHieu": "30% (3,0 điểm)",
                "vanDung": "20% (2,0 điểm)",
                "vanDungCao": "20% (2,0 điểm)"
            },
            "part1": [
                make_mc(1, "Nhận biết", f"Điều kiện xác định của phân thức $\\frac{{2x + 1}}{{x - {t_idx}}}$ là:", [f"$x \\neq {t_idx}$", f"$x \\neq -{t_idx}$", "$x \\neq 0$", "$x > 0$"], 0, f"Mẫu số phải khác 0: $x - {t_idx} \\neq 0 \\Leftrightarrow x \\neq {t_idx}$."),
                make_mc(2, "Nhận biết", f"Phương trình nào sau đây là phương trình bậc nhất một ẩn?", [f"${t_idx}x - 5 = 0$", "$x^2 - 4 = 0$", "$\\frac{1}{x} + 2 = 0$", "$0x + 3 = 0$"], 0, "Phương trình bậc nhất một ẩn có dạng $ax + b = 0$ ($a \\neq 0$)."),
                make_mc(3, "Nhận biết", "Nếu $\\Delta ABC \\backsim \\Delta DEF$ theo tỉ số đồng dạng $k = 2$ thì tỉ số $\\frac{AB}{DE}$ bằng:", ["$2$", "$\\frac{1}{2}$", "$4$", "$\\frac{1}{4}$"], 0, "Tỉ số hai cạnh tương ứng bằng tỉ số đồng dạng $k = 2$."),
                make_mc(4, "Thông hiểu", f"Nghiệm của phương trình $2x - {2 * t_idx} = 0$ là:", [f"$x = {t_idx}$", f"$x = -{t_idx}$", "$x = 0$", f"$x = {2 * t_idx}$"], 0, f"$2x = {2 * t_idx} \\Rightarrow x = {t_idx}$."),
                make_mc(5, "Thông hiểu", f"Rút gọn phân thức $\\frac{{x^2 - {t_idx**2}}}{{x - {t_idx}}}$ (với $x \\neq {t_idx}$) ta được:", [f"$x + {t_idx}$", f"$x - {t_idx}$", "$1$", "$x$"], 0, f"$\\frac{{(x - {t_idx})(x + {t_idx})}}{{x - {t_idx}}} = x + {t_idx}$."),
                make_mc(6, "Thông hiểu", "Cho $\\Delta ABC$ và $\\Delta MNP$ có $\\widehat{A} = \\widehat{M}$ và $\\widehat{B} = \\widehat{N}$. Khi đó hai tam giác đồng dạng theo trường hợp:", ["Góc - góc (g.g)", "Cạnh - cạnh - cạnh (c.c.c)", "Cạnh - góc - cạnh (c.g.c)", "Cạnh huyền - góc nhọn"], 0, "Nếu hai góc của tam giác này lần lượt bằng hai góc của tam giác kia thì hai tam giác đó đồng dạng (g.g)."),
                make_mc(7, "Vận dụng", f"Hệ số góc của đường thẳng $d: y = ({t_idx} + 1)x - 3$ là:", [f"${t_idx + 1}$", "$-3$", "$3$", "$\\frac{1}{t_idx + 1}$"], 0, f"Đường thẳng $y = ax + b$ có hệ số góc là $a = {t_idx + 1}$."),
                make_mc(8, "Vận dụng", f"Một người đi xe máy từ $A$ đến $B$ với vận tốc ${30 + 5 * t_idx}\\,\\text{{km/h}}$, thời gian đi hết $2$ giờ. Quãng đường $AB$ dài bao nhiêu ki-lô-mét?", [f"${2 * (30 + 5 * t_idx)}\\,\\text{{km}}$", f"${30 + 5 * t_idx}\\,\\text{{km}}$", "60 km", "100 km"], 0, f"$S = v \\cdot t = {30 + 5 * t_idx} \\cdot 2 = {2 * (30 + 5 * t_idx)}\\,\\text{{km}}$."),
                make_mc(9, "Vận dụng cao", f"Tìm giá trị nguyên của $x$ để phân thức $P = \\frac{{{t_idx}x + 1}}{{x - 1}}$ nhận giá trị nguyên.", [f"$x \\in \\mathbb{{Z}}$ thỏa mãn $(x - 1) \\mid ({t_idx + 1})$", "$x = 1$", "$x = 0$", "Không có giá trị nào"], 0, f"$P = {t_idx} + \\frac{{{t_idx + 1}}}{{x - 1}}$. Để $P \\in \\mathbb{{Z}}$ thì $x - 1$ là ước của ${t_idx + 1}$."),
                make_mc(10, "Vận dụng cao", f"Cho $\\Delta ABC \\backsim \\Delta A'B'C'$ theo tỉ số $k = \\frac{{1}}{{{t_idx}}}$. Tỉ số diện tích $\\frac{{S_{{ABC}}}}{{S_{{A'B'C'}}}}$ bằng:", [f"$\\frac{{1}}{{{t_idx**2}}}$", f"$\\frac{{1}}{{{t_idx}}}$", f"${t_idx**2}$", f"${t_idx}$"], 0, f"Tỉ số diện tích của hai tam giác đồng dạng bằng bình phương tỉ số đồng dạng: $k^2 = \\frac{{1}}{{{t_idx**2}}}$."),
                make_mc(11, "Vận dụng cao", f"Đường thẳng $y = (m - 1)x + 2$ song song với đường thẳng $y = {2 * t_idx}x - 5$ khi giá trị của $m$ bằng:", [f"${2 * t_idx + 1}$", f"${2 * t_idx}$", f"${2 * t_idx - 1}$", "1"], 0, f"Hai đường thẳng song song khi $a = a'$ và $b \\neq b'$. Ở đây $m - 1 = {2 * t_idx} \\Rightarrow m = {2 * t_idx + 1}$."),
                make_mc(12, "Vận dụng cao", f"Tìm nghiệm của phương trình tích: $(x - {t_idx})(x^2 + 1) = 0$.", [f"$x = {t_idx}$", f"$x = \\pm {t_idx}$", "$x = \\pm 1$", "Phương trình vô nghiệm"], 0, f"Vì $x^2 + 1 > 0$ với mọi $x$ nên $x - {t_idx} = 0 \\Leftrightarrow x = {t_idx}$.")
            ],
            "part2": [
                make_tf(1, f"Cho biểu thức $A = \\frac{{x}}{{x - {t_idx}}} - \\frac{{{t_idx}}}{{x + {t_idx}}}$ (với $x \\neq \\pm {t_idx}$).", [
                    {"id": "a", "text": f"Điều kiện xác định của biểu thức $A$ là $x \\neq {t_idx}$ và $x \\neq -{t_idx}$.", "correct": True, "level": "Nhận biết", "explanation": "Mẫu số khác 0."},
                    {"id": "b", "text": f"Mẫu thức chung của hai phân thức là $(x - {t_idx})(x + {t_idx}) = x^2 - {t_idx**2}$.", "correct": True, "level": "Nhận biết", "explanation": "Tích của hai mẫu thức nguyên tố cùng nhau."},
                    {"id": "c", "text": f"Khi quy đồng mẫu số, tử số của phân thức thu gọn là $x(x + {t_idx}) - {t_idx}(x - {t_idx}) = x^2 + {t_idx**2}$.", "correct": True, "level": "Thông hiểu", "explanation": f"$x^2 + {t_idx}x - {t_idx}x + {t_idx**2} = x^2 + {t_idx**2}$."},
                    {"id": "d", "text": "Biểu thức $A$ nhận giá trị bằng $0$ khi $x = 0$.", "correct": False, "level": "Vận dụng", "explanation": f"Tại $x = 0$, tử số là ${t_idx**2} \\neq 0$ nên $A \\neq 0$."}
                ]),
                make_tf(2, f"Cho tam giác $ABC$, đường thẳng $d$ song song với $BC$ cắt hai cạnh $AB$ và $AC$ lần lượt tại $D$ và $E$.", [
                    {"id": "a", "text": "Hai góc $\\widehat{ADE}$ và $\\widehat{ABC}$ là hai góc đồng vị bằng nhau.", "correct": True, "level": "Nhận biết", "explanation": "Do $DE \\parallel BC$ nên hai góc đồng vị bằng nhau."},
                    {"id": "b", "text": "Tam giác $ADE$ đồng dạng với tam giác $ABC$.", "correct": True, "level": "Thông hiểu", "explanation": "Định lí về tam giác đồng dạng khi có đường thẳng song song với một cạnh."},
                    {"id": "c", "text": "Tỉ số $\\frac{AD}{AB} = \\frac{AE}{AC} = \\frac{DE}{BC}$.", "correct": True, "level": "Thông hiểu", "explanation": "Hệ quả định lí Thalès và định nghĩa tam giác đồng dạng."},
                    {"id": "d", "text": "Nếu $D$ là trung điểm của $AB$ thì diện tích tam giác $ADE$ bằng một nửa diện tích tam giác $ABC$.", "correct": False, "level": "Vận dụng", "explanation": "Tỉ số diện tích bằng bình phương tỉ số đồng dạng: $(1/2)^2 = 1/4$, không phải $1/2$."}
                ])
            ],
            "part3": [
                make_sa(1, "Nhận biết", f"Tìm giá trị của hàm số $y = 3x - {t_idx}$ tại $x = 2$.", str(6 - t_idx), [str(6 - t_idx)], f"$y(2) = 3(2) - {t_idx} = {6 - t_idx}$."),
                make_sa(2, "Thông hiểu", f"Giải phương trình: $4x - {8 * t_idx} = 0$. Tìm $x$:", str(2 * t_idx), [str(2 * t_idx)], f"$4x = {8 * t_idx} \\Rightarrow x = {2 * t_idx}$."),
                make_sa(3, "Vận dụng", f"Một canô xuôi dòng một khúc sông từ $A$ đến $B$ mất 2 giờ và ngược dòng từ $B$ về $A$ mất 3 giờ. Biết vận tốc dòng nước là $3\\,\\text{{km/h}}$. Tính vận tốc thực của canô (theo km/h).", "15", ["15", "15 km/h"], "Gọi vận tốc thực là $v$. Ta có $2(v + 3) = 3(v - 3) \\Rightarrow 2v + 6 = 3v - 9 \\Rightarrow v = 15\\,\\text{km/h}$."),
                make_sa(4, "Vận dụng cao", f"Cho hai tam giác đồng dạng $\\Delta ABC \\backsim \\Delta DEF$ có chu vi lần lượt là ${15 * t_idx}\\,\\text{{cm}}$ và ${25 * t_idx}\\,\\text{{cm}}$. Biết cạnh lớn nhất của $\\Delta DEF$ là $10\\,\\text{{cm}}$. Tính độ dài cạnh tương ứng lớn nhất của $\\Delta ABC$ (theo cm).", "6", ["6", "6 cm"], "Tỉ số đồng dạng bằng tỉ số chu vi: $k = 15/25 = 3/5$. Cạnh tương ứng: $10 \\cdot (3/5) = 6\\,\\text{cm}$.")
            ],
            "part4": [
                make_essay(1, "Nhận biết", 1.0,
                    f"Rút gọn phân thức đại số sau:\n a) $P = \\frac{{{2 * t_idx}x - {4 * t_idx}}}{{x - 2}}$ (với $x \\neq 2$)\n b) $Q = \\frac{{x^2 - {t_idx**2}}}{{(x - {t_idx})^2}}$ (với $x \\neq {t_idx}$)",
                    f"a) Đặt nhân tử chung tử số: $\\frac{{{2*t_idx}(x - 2)}}{{x - 2}} = {2*t_idx}$ (0.5đ)\nb) Khai triển HĐT: $\\frac{{(x - {t_idx})(x + {t_idx})}}{{(x - {t_idx})^2}} = \\frac{{x + {t_idx}}}{{x - {t_idx}}}$ (0.5đ)",
                    f"a) Rút gọn được $P = {2*t_idx}$.\nb) Khai triển hằng đẳng thức và rút gọn thừa số chung $x - {t_idx}$."
                ),
                make_essay(2, "Thông hiểu", 1.0,
                    f"Giải bài toán bằng cách lập phương trình:\nMột đội thợ mỏ dự định khai thác ${300 * t_idx}$ tấn than trong một số ngày nhất định. Do cải tiến kỹ thuật, mỗi ngày đội khai thác vượt mức 5 tấn than, nên đội đã hoàn thành kế hoạch trước 3 ngày.\n a) Gọi số ngày dự định khai thác là $x$ (ngày). Viết biểu thức biểu thị lượng than khai thác mỗi ngày theo dự định.\n b) Lập phương trình và giải phương trình để tìm số ngày dự định hoàn thành kế hoạch.",
                    "a) Dự định mỗi ngày khai thác: $\\frac{300}{x}$ tấn (0.5đ)\nb) Thực tế mỗi ngày: $\\frac{300}{x - 3}$. Phương trình: $\\frac{300}{x-3} - \\frac{300}{x} = 5$. Giải PT tìm được nghiệm $x > 3$ thích hợp (0.5đ)",
                    "a) Biểu thức năng suất dự định: $\\frac{300}{x}$.\nb) Thiết lập phương trình hiệu năng suất và giải tìm được số ngày dự định."
                ),
                make_essay(3, "Vận dụng", 0.5,
                    f"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$.\n a) Chứng minh $\\Delta HBA \\backsim \\Delta ABC$.\n b) Suy ra hệ thức $AB^2 = BH \\cdot BC$. Biết $BH = {4 * t_idx}\\,\\text{{cm}}$, $BC = {9 * t_idx}\\,\\text{{cm}}$, tính độ dài cạnh $AB$.",
                    f"a) Xét hai tam giác có góc $\\widehat{{B}}$ chung, $\\widehat{{BHA}} = \\widehat{{BAC}} = 90^\\circ \\Rightarrow \\Delta HBA \\backsim \\Delta ABC$ (g.g) (0.25đ)\nb) Tỉ số đồng dạng: $\\frac{{BA}}{{BC}} = \\frac{{BH}}{{BA}} \\Rightarrow AB^2 = BH \\cdot BC = {36 * t_idx**2} \\Rightarrow AB = {6 * t_idx}\\,\\text{{cm}}$ (0.25đ)",
                    f"a) Chứng minh đồng dạng theo trường hợp (g.g).\nb) Suy ra hệ thức $AB^2 = BH \\cdot BC$, tính được $AB = {6*t_idx}\\,\\text{{cm}}$."
                ),
                make_essay(4, "Vận dụng cao", 0.5,
                    f"Tìm giá trị nhỏ nhất của phân thức $M = \\frac{{x^2 - 2x + {t_idx**2 + 5}}}{{2}}$ với $x \\in \\mathbb{{R}}$.",
                    f"Biến đổi tử số: $x^2 - 2x + {t_idx**2 + 5} = (x - 1)^2 + {t_idx**2 + 4} \\ge {t_idx**2 + 4}$ với mọi $x$ (0.25đ)\nSuy ra $M \\ge \\frac{{{t_idx**2 + 4}}}{{2}}$. Dấu '=' xảy ra khi $x = 1$. Vậy $\\min M = \\frac{{{t_idx**2 + 4}}}{{2}}$ (0.25đ)",
                    f"Tách bình phương hoàn chỉnh ở tử số, suy ra giá trị nhỏ nhất đạt được tại $x = 1$."
                )
            ]
        })

    return exams

# ==============================================================================
# 6 MÃ ĐỀ CUỐI KỲ 2 - TOÁN 8 (final2)
# Phạm vi: Toàn bộ HK2: Phân thức, PT & Hàm số, Xác suất, Tam giác vuông đồng dạng & Hình chóp đều
# ==============================================================================
def generate_g8_final2():
    exams = []
    
    for t_idx in range(1, 7):
        ex_num = f"0{t_idx}"
        topics = [
            "Hình chóp tam giác đều, Tam giác vuông đồng dạng, Xác suất thực nghiệm & Cực trị phân thức",
            "Hình chóp tứ giác đều, Định lí Pythagore ứng dụng, Biến cố đồng khả năng & Hàm số bậc nhất",
            "Thể tích hình chóp đều thực tế, Các trường hợp đồng dạng tam giác vuông & Phương trình bậc nhất",
            "Diện tích xung quanh hình chóp, Tính chiều cao cọc tiêu bằng tam giác đồng dạng & Xác suất",
            "Mô hình lều chóp tứ giác đều, Hệ thức lượng tam giác vuông qua đồng dạng & Phân thức đại số",
            "Ôn tập toàn diện cuối năm Toán 8: Đại số, Xác suất thống kê và Hình học không gian"
        ]
        topic = topics[t_idx - 1]

        exams.append({
            "id": f"p_g8_final2_{ex_num}",
            "testNum": t_idx,
            "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ II - TOÁN 8 (ĐỀ SỐ {ex_num})",
            "topic": topic,
            "grade": "8",
            "term": "final2",
            "termName": "Cuối Học kỳ II",
            "duration": "90 phút",
            "totalPoints": 10.0,
            "matrix": {
                "nhanBiet": "30% (3,0 điểm)",
                "thongHieu": "30% (3,0 điểm)",
                "vanDung": "20% (2,0 điểm)",
                "vanDungCao": "20% (2,0 điểm)"
            },
            "part1": [
                make_mc(1, "Nhận biết", "Hình chóp tứ giác đều có mặt đáy là hình gì?", ["Hình vuông", "Hình chữ nhật", "Hình thoi", "Hình bình hành"], 0, "Hình chóp tứ giác đều có đáy là hình vuông và các mặt bên là các tam giác cân bằng nhau."),
                make_mc(2, "Nhận biết", "Công thức tính thể tích của hình chóp đều có diện tích đáy $S$ và chiều cao $h$ là:", ["$V = \\frac{1}{3} S \\cdot h$", "$V = S \\cdot h$", "$V = \\frac{1}{2} S \\cdot h$", "$V = 3 S \\cdot h$"], 0, "Thể tích hình chóp bằng $1/3$ diện tích đáy nhân chiều cao."),
                make_mc(3, "Nhận biết", "Trong các hàm số sau, hàm số nào là hàm số bậc nhất đồng biến trên $\\mathbb{R}$?", ["$y = 2x - 3$", "$y = -3x + 1$", "$y = 5$", "$y = x^2$"], 0, "Hàm số bậc nhất $y = ax + b$ đồng biến khi $a > 0$ (ở đây $a = 2 > 0$)."),
                make_mc(4, "Thông hiểu", f"Một hình chóp tam giác đều có diện tích đáy $S = {12 * t_idx}\\,\\text{{cm}}^2$ và chiều cao $h = 6\\,\\text{{cm}}$. Thể tích của hình chóp đó là:", [f"${24 * t_idx}\\,\\text{{cm}}^3$", f"${72 * t_idx}\\,\\text{{cm}}^3$", f"${12 * t_idx}\\,\\text{{cm}}^3$", f"${36 * t_idx}\\,\\text{{cm}}^3$"], 0, f"$V = \\frac{1}{3} S \\cdot h = \\frac{1}{3} \\cdot {12*t_idx} \\cdot 6 = {24*t_idx}\\,\\text{{cm}}^3$."),
                make_mc(5, "Thông hiểu", f"Gieo một con xúc xắc 6 mặt cân đối 60 lần, thấy có {15 + t_idx} lần xuất hiện mặt 5 chấm. Xác suất thực nghiệm xuất hiện mặt 5 chấm là:", [f"$\\frac{{{15 + t_idx}}}{{60}}$", "$\\frac{1}{6}$", "$\\frac{5}{60}$", "$0,5$"], 0, f"Xác suất thực nghiệm bằng số lần xuất hiện chia cho tổng số lần gieo: $({15+t_idx})/60$."),
                make_mc(6, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\,\\text{cm}, AC = 8\\,\\text{cm}$. Độ dài cạnh huyền $BC$ bằng:", ["$10\\,\\text{cm}$", "$14\\,\\text{cm}$", "$2\\,\\text{cm}$", "$48\\,\\text{cm}$"], 0, "Theo định lí Pythagore: $BC = \\sqrt{6^2 + 8^2} = \\sqrt{100} = 10\\,\\text{cm}$."),
                make_mc(7, "Vận dụng", f"Một hình chóp tứ giác đều có cạnh đáy bằng ${4 * t_idx}\\,\\text{{cm}}$ và trung đoạn bằng $5\\,\\text{{cm}}$. Diện tích xung quanh của hình chóp là:", [f"${40 * t_idx}\\,\\text{{cm}}^2$", f"${20 * t_idx}\\,\\text{{cm}}^2$", f"${80 * t_idx}\\,\\text{{cm}}^2$", f"${10 * t_idx}\\,\\text{{cm}}^2$"], 0, f"Nửa chu vi đáy: $p = 4 \\cdot {4*t_idx} / 2 = {8*t_idx}\\,\\text{{cm}}$. Diện tích xung quanh: $S_{{xq}} = p \\cdot d = {8*t_idx} \\cdot 5 = {40*t_idx}\\,\\text{{cm}}^2$."),
                make_mc(8, "Vận dụng", f"Để đo chiều cao của một cột cờ, bạn Nam cắm một chiếc cọc cao $2\\,\\text{{m}}$ vuông góc với mặt đất, bóng của cọc dài $1,5\\,\\text{{m}}$. Cùng lúc đó bóng của cột cờ dài ${3 * t_idx}\\,\\text{{m}}$. Chiều cao của cột cờ là:", [f"${4 * t_idx}\\,\\text{{m}}$", f"${2 * t_idx}\\,\\text{{m}}$", f"${6 * t_idx}\\,\\text{{m}}$", "10 m"], 0, f"Theo tính chất tam giác đồng dạng: $h / {3*t_idx} = 2 / 1,5 = 4/3 \\Rightarrow h = {4*t_idx}\\,\\text{{m}}$."),
                make_mc(9, "Vận dụng cao", f"Cho tam giác $ABC$ vuông tại $A$ có đường cao $AH$. Biết $HB = {2 * t_idx}\\,\\text{{cm}}$, $HC = {8 * t_idx}\\,\\text{{cm}}$. Độ dài đường cao $AH$ là:", [f"${4 * t_idx}\\,\\text{{cm}}$", f"${16 * t_idx}\\,\\text{{cm}}$", f"${10 * t_idx}\\,\\text{{cm}}$", f"${5 * t_idx}\\,\\text{{cm}}$"], 0, f"Do $\\Delta HBA \\backsim \\Delta HAC \\Rightarrow AH^2 = HB \\cdot HC = {16 * t_idx**2} \\Rightarrow AH = {4 * t_idx}\\,\\text{{cm}}$."),
                make_mc(10, "Vận dụng cao", f"Một chiếc lều hình chóp tứ giác đều có cạnh đáy bằng $3\\,\\text{{m}}$, chiều cao bằng $2\\,\\text{{m}}$. Thể tích không gian bên trong lều là:", ["$6\\,\\text{m}^3$", "$18\\,\\text{m}^3$", "$12\\,\\text{m}^3$", "$9\\,\\text{m}^3$"], 0, "$S = 3^2 = 9\\,\\text{m}^2$. $V = \\frac{1}{3} \\cdot 9 \\cdot 2 = 6\\,\\text{m}^3$."),
                make_mc(11, "Vận dụng cao", "Tìm giá trị của $m$ để đồ thị hàm số $y = (2m - 4)x + 3$ đi qua điểm $A(1; 5)$.", ["$m = 3$", "$m = 2$", "$m = 1$", "$m = -1$"], 0, "Thay $x = 1, y = 5$ vào hàm số: $2m - 4 + 3 = 5 \\Leftrightarrow 2m - 1 = 5 \\Leftrightarrow m = 3$."),
                make_mc(12, "Vận dụng cao", f"Tung hai đồng xu cân đối đồng chất cùng lúc. Xác suất để cả hai đồng xu cùng xuất hiện mặt ngửa là:", ["$\\frac{1}{4}$", "$\\frac{1}{2}$", "$\\frac{3}{4}$", "$\\frac{1}{3}$"], 0, "Không gian mẫu có 4 kết quả: {NN, NS, SN, SS}. Chỉ có 1 kết quả cả 2 ngửa nên xác suất là 1/4.")
            ],
            "part2": [
                make_tf(1, f"Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy $AB = 6\\,\\text{{cm}}$, trung đoạn $SI = 5\\,\\text{{cm}}$ (với $I$ là trung điểm của cạnh đáy $CD$).", [
                    {"id": "a", "text": "Mặt đáy $ABCD$ là một hình vuông có chu vi bằng $24\\,\\text{cm}$.", "correct": True, "level": "Nhận biết", "explanation": "Chu vi hình vuông: 4 * 6 = 24 cm."},
                    {"id": "b", "text": "Nửa chu vi đáy của hình chóp bằng $12\\,\\text{cm}$.", "correct": True, "level": "Nhận biết", "explanation": "p = 24 / 2 = 12 cm."},
                    {"id": "c", "text": "Diện tích xung quanh của hình chóp bằng $60\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "S_xq = p * d = 12 * 5 = 60 cm²."},
                    {"id": "d", "text": "Chiều cao của hình chóp bằng $5\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "Gọi O là tâm đáy, OI = 3 cm. Chiều cao SO = sqrt(5² - 3²) = 4 cm != 5 cm."}
                ]),
                make_tf(2, f"Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\,\\text{{cm}}$, $AC = 8\\,\\text{{cm}}$. Kẻ đường cao $AH$ ($H \\in BC$).", [
                    {"id": "a", "text": "Độ dài cạnh huyền $BC$ bằng $10\\,\\text{cm}$.", "correct": True, "level": "Nhận biết", "explanation": "Theo định lí Pythagore: sqrt(6² + 8²) = 10 cm."},
                    {"id": "b", "text": "Diện tích tam giác $ABC$ bằng $24\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "S = (1/2) * 6 * 8 = 24 cm²."},
                    {"id": "c", "text": "Độ dài đường cao $AH$ bằng $4,8\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "AH = (AB * AC) / BC = (6 * 8) / 10 = 4,8 cm."},
                    {"id": "d", "text": "Hình chiếu $HB$ có độ dài lớn hơn hình chiếu $HC$.", "correct": False, "level": "Vận dụng", "explanation": "Vì AB < AC (6 < 8) nên HB < HC, không thể lớn hơn."}
                ])
            ],
            "part3": [
                make_sa(1, "Nhận biết", "Hình chóp tứ giác đều có tất cả bao nhiêu cạnh (cả cạnh đáy và cạnh bên)?", "8", ["8", "8 cạnh"], "Có 4 cạnh đáy và 4 cạnh bên: tổng cộng 8 cạnh."),
                make_sa(2, "Thông hiểu", f"Tính thể tích của hình chóp tứ giác đều có cạnh đáy $6\\,\\text{{cm}}$ và chiều cao $h = {2 * t_idx}\\,\\text{{cm}}$ (theo $\\text{{cm}}^3$):", str(24 * t_idx), [str(24 * t_idx)], f"$S = 6^2 = 36\\,\\text{{cm}}^2$. $V = \\frac{1}{3} \\cdot 36 \\cdot {2*t_idx} = {24*t_idx}\\,\\text{{cm}}^3$."),
                make_sa(3, "Vận dụng", f"Một hộp đựng {15 + t_idx} viên bi cùng kích thước gồm 5 bi đỏ, 5 bi xanh và {5 + t_idx} bi vàng. Lấy ngẫu nhiên một viên bi. Xác suất lấy được viên bi màu đỏ là phân số tối giản a/b:", f"5/{15 + t_idx}", [f"5/{15 + t_idx}"], f"Xác suất = 5 / {15 + t_idx}."),
                make_sa(4, "Vận dụng cao", f"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = {3 * t_idx}\\,\\text{{cm}}$, $AC = {4 * t_idx}\\,\\text{{cm}}$. Tính độ dài đoạn thẳng $BH$ (theo cm).", f"{1.8 * t_idx:.1f}".rstrip("0").rstrip("."), [f"{1.8 * t_idx:.1f}".rstrip("0").rstrip(".")], f"$BC = {5*t_idx}$. $AB^2 = BH \\cdot BC \\Rightarrow BH = {9*t_idx**2} / {5*t_idx} = {1.8*t_idx:.1f}\\,\\text{{cm}}$.")
            ],
            "part4": [
                make_essay(1, "Nhận biết", 1.0,
                    f"Thực hiện các yêu cầu sau:\n a) Tính giá trị của biểu thức $P = \\frac{{{t_idx}x + 2}}{{x - 3}}$ tại $x = 5$.\n b) Vẽ bảng giá trị và xác định hệ số góc của hàm số bậc nhất $y = 2x - {t_idx}$.",
                    f"a) Thay $x = 5$ vào $P$: $P = \\frac{{{5*t_idx + 2}}}{{2}}$ (0.5đ)\nb) Hàm số $y = 2x - {t_idx}$ có hệ số góc là $a = 2$. Bảng giá trị qua 2 điểm $(0; -{t_idx})$ và $(1; 2 - {t_idx})$ (0.5đ)",
                    f"a) Tính giá trị phân thức tại $x = 5$.\nb) Hệ số góc của hàm số bằng 2."
                ),
                make_essay(2, "Thông hiểu", 1.0,
                    f"Một chiếc mái nhà hình chóp tứ giác đều có cạnh đáy $8\\,\\text{{m}}$, chiều cao của hình chóp là $3\\,\\text{{m}}$.\n a) Tính thể tích phần không gian phía dưới mái nhà đó.\n b) Biết trung đoạn của hình chóp là $5\\,\\text{{m}}$, người ta cần lợp ngói toàn bộ 4 mặt bên của mái nhà. Tính diện tích ngói cần lợp.",
                    "a) Diện tích đáy: $S = 8^2 = 64\\,\\text{m}^2$. Thể tích: $V = \\frac{1}{3} \\cdot 64 \\cdot 3 = 64\\,\\text{m}^3$ (0.5đ)\nb) Nửa chu vi đáy: $p = 4 \\cdot 8 / 2 = 16\\,\\text{m}$. Diện tích xung quanh: $S_{xq} = p \\cdot d = 16 \\cdot 5 = 80\\,\\text{m}^2$ (0.5đ)",
                    "a) Thể tích không gian là $64\\,\\text{m}^3$.\nb) Diện tích ngói cần lợp là $80\\,\\text{m}^2$."
                ),
                make_essay(3, "Vận dụng", 0.5,
                    f"Cho tam giác $ABC$ nhọn có hai đường cao $BD$ và $CE$ cắt nhau tại $H$.\n a) Chứng minh rằng $\\Delta ABD \\backsim \\Delta ACE$.\n b) Chứng minh hệ thức $AD \\cdot AC = AE \\cdot AB$.",
                    "a) Hai tam giác vuông có chung góc $\\widehat{A}$ nên $\\Delta ABD \\backsim \\Delta ACE$ (g.g) (0.25đ)\nb) Tỉ số đồng dạng: $\\frac{AD}{AE} = \\frac{AB}{AC} \\Rightarrow AD \\cdot AC = AE \\cdot AB$ (0.25đ)",
                    "a) Chứng minh đồng dạng theo góc nhọn chung.\nb) Suy ra tỉ số cạnh và tích chéo."
                ),
                make_essay(4, "Vận dụng cao", 0.5,
                    f"Cho các số thực dương $a, b$ thỏa mãn $a + b = 2$. Tìm giá trị nhỏ nhất của biểu thức $P = \\frac{{1}}{{a}} + \\frac{{1}}{{b}} + {t_idx}$.",
                    f"Áp dụng BĐT Cauchy-Schwarz dạng Engel: $\\frac{{1}}{{a}} + \\frac{{1}}{{b}} \\ge \\frac{{(1+1)^2}}{{a+b}} = \\frac{{4}}{{2}} = 2$ (0.25đ)\nSuy ra $P \\ge 2 + {t_idx}$. Dấu '=' xảy ra khi $a = b = 1$. Vậy $\\min P = 2 + {t_idx}$ (0.25đ)",
                    f"Áp dụng bất đẳng thức cộng mẫu số, đạt cực tiểu khi $a = b = 1$."
                )
            ]
        })

    return exams

def main():
    print("=== SINH VÀ KIỂM TRA ĐỀ ĐỊNH KỲ TOÁN 8 ===")
    mid2_exams = generate_g8_mid2()
    final2_exams = generate_g8_final2()

    assert len(mid2_exams) == 6, f"Thiếu đề mid2: {len(mid2_exams)} != 6"
    assert len(final2_exams) == 6, f"Thiếu đề final2: {len(final2_exams)} != 6"

    for idx, ex in enumerate(mid2_exams, 1):
        validate_periodic_exam(ex, "8", "mid2", idx)
        print(f"✅ Toán 8 - Giữa kỳ 2 (Đề {idx}): ĐẠT CHUẨN MA TRẬN 100%.")

    for idx, ex in enumerate(final2_exams, 1):
        validate_periodic_exam(ex, "8", "final2", idx)
        print(f"✅ Toán 8 - Cuối kỳ 2 (Đề {idx}): ĐẠT CHUẨN MA TRẬN 100%.")

    print("🎉 Hoàn thành xuất sắc 12 đề định kỳ Toán 8!")
    return mid2_exams, final2_exams

if __name__ == "__main__":
    main()
