# -*- coding: utf-8 -*-
"""
GENERATOR BỘ ĐỀ THI ĐỊNH KỲ TOÁN 7 (GIỮA KỲ 2 & CUỐI KỲ 2)
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
# 6 MÃ ĐỀ GIỮA KỲ 2 - TOÁN 7 (mid2)
# Phạm vi: Tỉ lệ thức, Dãy tỉ số bằng nhau, Đa thức một biến, BĐT tam giác
# ==============================================================================
def generate_g7_mid2():
    exams = []
    
    for t_idx in range(1, 7):
        ex_num = f"0{t_idx}"
        topics = [
            "Tỉ lệ thức, Đa thức một biến & Bất đẳng thức tam giác",
            "Đại lượng tỉ lệ thuận, Cộng trừ đa thức một biến & Quan hệ cạnh - góc trong tam giác",
            "Dãy tỉ số bằng nhau thực tế, Nghiệm của đa thức & Đường vuông góc - đường xiên",
            "Đại lượng tỉ lệ nghịch, Nhân chia đa thức một biến & Bất đẳng thức tam giác",
            "Chia tỉ lệ trong kinh tế, Bậc và hệ số đa thức, Quan hệ góc và cạnh đối diện",
            "Tổng hợp giữa kỳ 2: Tỉ lệ thức, Đa thức một biến và Bất đẳng thức hình học"
        ]
        topic = topics[t_idx - 1]

        exams.append({
            "id": f"p_g7_mid2_{ex_num}",
            "testNum": t_idx,
            "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ II - TOÁN 7 (ĐỀ SỐ {ex_num})",
            "topic": topic,
            "grade": "7",
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
                make_mc(1, "Nhận biết", f"Từ đẳng thức ${2 * t_idx} \\cdot 6 = 3 \\cdot {4 * t_idx}$, ta lập được tỉ lệ thức nào sau đây?", [f"$\\frac{{{2*t_idx}}}{{3}} = \\frac{{{4*t_idx}}}{{6}}$", f"$\\frac{{{2*t_idx}}}{{4}} = \\frac{{6}}{{3}}$", f"$\\frac{{{2*t_idx}}}{{6}} = \\frac{{{4*t_idx}}}{{3}}$", f"$\\frac{{3}}{{{2*t_idx}}} = \\frac{{{4*t_idx}}}{{6}}$"], 0, "Từ $ad = bc$ ta có tỉ lệ thức $\\frac{a}{c} = \\frac{b}{d}$."),
                make_mc(2, "Nhận biết", f"Bậc của đa thức $P(x) = {t_idx}x^4 - 2x^3 + 5x - 7$ là:", ["$4$", "$3$", "$1$", "$0$"], 0, "Bậc của đa thức một biến là số mũ lớn nhất của biến trong đa thức đã thu gọn, ở đây là 4."),
                make_mc(3, "Nhận biết", "Trong tam giác $ABC$, góc đối diện với cạnh $BC$ là:", ["Góc $\\widehat{A}$", "Góc $\\widehat{B}$", "Góc $\\widehat{C}$", "Cả ba góc"], 0, "Góc đối diện với cạnh $BC$ là đỉnh $A$, tức góc $\\widehat{A}$."),
                make_mc(4, "Thông hiểu", f"Cho $\\frac{{x}}{{{2 + t_idx}}} = \\frac{{6}}{{3}}$. Giá trị của $x$ là:", [f"${2 * (2 + t_idx)}$", f"${2 + t_idx}$", "$4$", "$6$"], 0, f"$x = 2 \\cdot ({2 + t_idx}) = {2 * (2 + t_idx)}$."),
                make_mc(5, "Thông hiểu", f"Giá trị của đa thức $A(x) = 2x^2 - {t_idx}x + 1$ tại $x = 1$ là:", [f"${3 - t_idx}$", f"${2 - t_idx}$", "$3$", "$1$"], 0, f"$A(1) = 2(1)^2 - {t_idx}(1) + 1 = 3 - {t_idx}$."),
                make_mc(6, "Thông hiểu", "Bộ ba độ dài đoạn thẳng nào sau đây CÓ THỂ là độ dài ba cạnh của một tam giác?", ["$2\\,\\text{cm}, 3\\,\\text{cm}, 6\\,\\text{cm}$", "$3\\,\\text{cm}, 4\\,\\text{cm}, 5\\,\\text{cm}$", "$1\\,\\text{cm}, 2\\,\\text{cm}, 3\\,\\text{cm}$", "$4\\,\\text{cm}, 5\\,\\text{cm}, 10\\,\\text{cm}$"], 1, "Theo BĐT tam giác: $3 + 4 = 7 > 5$ thỏa mãn."),
                make_mc(7, "Vận dụng", f"Hai đại lượng $x$ và $y$ tỉ lệ thuận với nhau. Khi $x = {2 * t_idx}$ thì $y = {6 * t_idx}$. Hệ số tỉ lệ của $y$ đối với $x$ là:", ["$3$", "$\\frac{1}{3}$", "$2$", "$6$"], 0, f"$k = y / x = {6*t_idx} / {2*t_idx} = 3$."),
                make_mc(8, "Vận dụng", f"Cho tam giác $ABC$ có $\\widehat{{A}} = {50 + 5 * t_idx}^\\circ$, $\\widehat{{B}} = 60^\\circ$. So sánh độ dài các cạnh của tam giác $ABC$:", ["$BC > AC > AB$", "$AB > BC > AC$", "$AC > BC > AB$", "$AB > AC > BC$"], 0, f"Tổng ba góc bằng $180^\\circ$, tính được góc $\\widehat{{C}} = {70 - 5 * t_idx}^\\circ$. Cạnh đối diện góc lớn hơn thì lớn hơn."),
                make_mc(9, "Vận dụng cao", f"Tìm nghiệm của đa thức $Q(x) = x^2 + {2 * t_idx}x + {t_idx**2 + 1}$.", ["Đa thức vô nghiệm", "$x = -1$", "$x = 0$", "$x = 1$"], 0, f"$Q(x) = (x + {t_idx})^2 + 1 \\ge 1 > 0$ với mọi $x$, do đó đa thức không có nghiệm."),
                make_mc(10, "Vận dụng cao", f"Cho tam giác $ABC$ cân tại $A$ có $AB = AC = {5 * t_idx}\\,\\text{{cm}}$. Cạnh $BC$ có độ dài là một số nguyên (cm). Giá trị lớn nhất có thể của $BC$ là:", [f"${10 * t_idx - 1}\\,\\text{{cm}}$", f"${10 * t_idx}\\,\\text{{cm}}$", f"${5 * t_idx}\\,\\text{{cm}}$", f"${5 * t_idx + 1}\\,\\text{{cm}}$"], 0, f"Theo BĐT tam giác: $BC < AB + AC = {10*t_idx}$. Do $BC \\in \\mathbb{{Z}}$ nên lớn nhất là ${10*t_idx - 1}\\,\\text{{cm}}$."),
                make_mc(11, "Vận dụng cao", "Tìm hệ số cao nhất của tích hai đa thức $P(x) = 3x^3 - 2x + 1$ và $Q(x) = 2x^2 + 5x - 4$.", ["$6$", "$15$", "$-8$", "$3$"], 0, "Bậc của tích là $3 + 2 = 5$, hệ số cao nhất là $3 \\cdot 2 = 6$."),
                make_mc(12, "Vận dụng cao", f"Cho dãy tỉ số bằng nhau: $\\frac{{a}}{{{2 + t_idx}}} = \\frac{{b}}{{{3 + t_idx}}} = \\frac{{c}}{{{4 + t_idx}}}$. Giá trị của biểu thức $M = \\frac{{2a + 3b - 4c}}{{a - 2b + c}}$ bằng:", ["$-1$", "$1$", "$2$", "$0$"], 0, "Áp dụng tính chất dãy tỉ số bằng nhau hoặc đặt $= k$ rút gọn được hằng số.")
            ],
            "part2": [
                make_tf(1, f"Cho đa thức $P(x) = 3x^3 - {2 * t_idx}x^2 + 5x - 4$ và $Q(x) = -3x^3 + {2 * t_idx}x^2 - x + 8$.", [
                    {"id": "a", "text": "Đa thức $P(x)$ có bậc là 3.", "correct": True, "level": "Nhận biết", "explanation": "Bậc cao nhất của $P(x)$ là 3."},
                    {"id": "b", "text": "Hệ số tự do của đa thức $Q(x)$ là $8$.", "correct": True, "level": "Nhận biết", "explanation": "Hệ số tự do là hạng tử không chứa biến: 8."},
                    {"id": "c", "text": "Tổng $P(x) + Q(x)$ là một đa thức bậc nhất.", "correct": True, "level": "Thông hiểu", "explanation": f"$P(x) + Q(x) = (3 - 3)x^3 + (-{2*t_idx} + {2*t_idx})x^2 + (5 - 1)x + (-4 + 8) = 4x + 4$, có bậc 1."},
                    {"id": "d", "text": "Nghiệm của đa thức tổng $P(x) + Q(x)$ là $x = 1$.", "correct": False, "level": "Vận dụng", "explanation": "$4x + 4 = 0 \\Leftrightarrow x = -1$, không phải $x = 1$."}
                ]),
                make_tf(2, f"Cho tam giác $ABC$ có độ dài ba cạnh thỏa mãn $AB = {3 * t_idx}\\,\\text{{cm}}$, $AC = {4 * t_idx}\\,\\text{{cm}}$, $BC = {5 * t_idx}\\,\\text{{cm}}$.", [
                    {"id": "a", "text": "Cạnh $BC$ là cạnh lớn nhất trong tam giác $ABC$.", "correct": True, "level": "Nhận biết", "explanation": f"Vì ${5*t_idx} > {4*t_idx} > {3*t_idx}$."},
                    {"id": "b", "text": "Góc $\\widehat{A}$ là góc đối diện với cạnh $BC$.", "correct": True, "level": "Thông hiểu", "explanation": "Góc đối diện với cạnh $BC$ là đỉnh $A$."},
                    {"id": "c", "text": "Trong tam giác $ABC$, góc $\\widehat{A}$ là góc có số đo lớn nhất.", "correct": True, "level": "Thông hiểu", "explanation": "Cạnh lớn nhất đối diện góc lớn nhất."},
                    {"id": "d", "text": "Chu vi của tam giác $ABC$ không thể vượt quá $10\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": f"Chu vi là ${3*t_idx} + {4*t_idx} + {5*t_idx} = {12*t_idx}\\,\\text{{cm}} \\ge 12\\,\\text{{cm}} > 10\\,\\text{{cm}}$."}
                ])
            ],
            "part3": [
                make_sa(1, "Nhận biết", f"Tìm hệ số cao nhất của đa thức $f(x) = {5 * t_idx}x^3 - 4x^2 + 7$.", str(5 * t_idx), [str(5 * t_idx)], f"Hệ số ứng với lũy thừa cao nhất $x^3$ là {5 * t_idx}."),
                make_sa(2, "Thông hiểu", f"Tìm $x$, biết: $\\frac{{x}}{{{2 * t_idx}}} = \\frac{{12}}{{6}}$.", str(4 * t_idx), [str(4 * t_idx)], f"$\\frac{{12}}{{6}} = 2 \\Rightarrow x = 2 \\cdot {2 * t_idx} = {4 * t_idx}$."),
                make_sa(3, "Vận dụng", f"Ba lớp 7A, 7B, 7C tham gia trồng cây xanh. Số cây trồng được của ba lớp lần lượt tỉ lệ với các số $3; 4; 5$. Biết cả ba lớp trồng được tất cả ${12 * t_idx}$ cây. Hỏi lớp 7B trồng được bao nhiêu cây?", str(4 * t_idx), [str(4 * t_idx)], f"Tổng số phần bằng nhau: $3 + 4 + 5 = 12$ phần. Giá trị một phần: ${12 * t_idx} / 12 = {t_idx}$ cây. Số cây lớp 7B: $4 \\cdot {t_idx} = {4 * t_idx}$ cây."),
                make_sa(4, "Vận dụng cao", f"Cho đa thức $P(x) = ax^2 + bx + c$. Biết $P(0) = {t_idx}$, $P(1) = {t_idx + 3}$, $P(2) = {t_idx + 8}$. Tìm giá trị của hệ số $a$.", "1", ["1", "1.0"], "$P(0) = c = t_idx$. $P(1) = a + b + c = t_idx + 3 \\Rightarrow a + b = 3$. $P(2) = 4a + 2b + c = t_idx + 8 \\Rightarrow 4a + 2b = 8 \\Rightarrow 2a + b = 4$. Trừ vế theo vế được $a = 1$.")
            ],
            "part4": [
                make_essay(1, "Nhận biết", 1.0,
                    f"Cho hai đa thức một biến: $A(x) = 2x^2 - {t_idx}x + 3$ và $B(x) = x^2 + {t_idx}x - 5$.\n a) Thu gọn và sắp xếp hai đa thức theo lũy thừa giảm dần của biến.\n b) Tính $C(x) = A(x) + B(x)$.",
                    "a) Hai đa thức đã được thu gọn và sắp xếp giảm dần (0.5đ)\nb) $C(x) = (2+1)x^2 + (-t_idx + t_idx)x + (3 - 5) = 3x^2 - 2$ (0.5đ)",
                    "a) $A(x)$ và $B(x)$ đã ở dạng thu gọn giảm dần.\nb) Cộng các hạng tử cùng bậc: $C(x) = 3x^2 - 2$."
                ),
                make_essay(2, "Thông hiểu", 1.0,
                    f"Hưởng ứng phong trào quyên góp sách cho thư viện, ba bạn An, Bình, Cường quyên góp số quyển sách lần lượt tỉ lệ với các số $2; 3; 5$. Biết số sách của bạn Cường nhiều hơn số sách của bạn An là ${6 * t_idx}$ quyển.\n a) Gọi số sách của ba bạn là $x, y, z$. Viết dãy tỉ số bằng nhau tương ứng.\n b) Tính số quyển sách mỗi bạn đã quyên góp.",
                    f"a) $\\frac{{x}}{{2}} = \\frac{{y}}{{3}} = \\frac{{z}}{{5}}$ và $z - x = {6*t_idx}$ (0.5đ)\nb) Theo tính chất dãy tỉ số bằng nhau: $\\frac{{z - x}}{{5 - 2}} = \\frac{{{6*t_idx}}}{{3}} = {2*t_idx}$. Vậy $x = {4*t_idx}, y = {6*t_idx}, z = {10*t_idx}$ quyển (0.5đ)",
                    f"a) Thiết lập dãy tỉ số: $\\frac{{x}}{{2}} = \\frac{{y}}{{3}} = \\frac{{z}}{{5}}$.\nb) Tìm được: An có ${4*t_idx}$ quyển, Bình có ${6*t_idx}$ quyển, Cường có ${10*t_idx}$ quyển."
                ),
                make_essay(3, "Vận dụng", 0.5,
                    f"Cho tam giác $ABC$ có $AB = {4 * t_idx}\\,\\text{{cm}}$, $AC = {7 * t_idx}\\,\\text{{cm}}$.\n a) Hãy viết bất đẳng thức tam giác liên hệ giữa độ dài ba cạnh $AB, AC, BC$.\n b) Biết độ dài cạnh $BC$ là một số nguyên (cm). Tìm độ dài lớn nhất có thể của cạnh $BC$.",
                    f"a) $|AC - AB| < BC < AC + AB \\Rightarrow {3*t_idx} < BC < {11*t_idx}$ (0.25đ)\nb) Vì $BC \\in \\mathbb{{Z}}$ nên giá trị lớn nhất của $BC$ là ${11*t_idx - 1}\\,\\text{{cm}}$ (0.25đ)",
                    f"a) Theo BĐT tam giác: ${3*t_idx} < BC < {11*t_idx}$.\nb) Độ dài nguyên lớn nhất là ${11*t_idx - 1}\\,\\text{{cm}}$."
                ),
                make_essay(4, "Vận dụng cao", 0.5,
                    f"Cho đa thức $f(x) = ax^3 + bx^2 + cx + d$ với $a, b, c, d$ là các số nguyên. Biết $f(x)$ chia hết cho 5 với mọi số nguyên $x$. Chứng minh rằng các hệ số $a, b, c, d$ đều chia hết cho 5.",
                    "Xét các giá trị đặc biệt:\n+ $f(0) = d \\,\\vdots\\, 5 \\Rightarrow d \\,\\vdots\\, 5$ (0.1đ)\n+ $f(1) = a + b + c + d \\,\\vdots\\, 5$ và $f(-1) = -a + b - c + d \\,\\vdots\\, 5 \\Rightarrow f(1)+f(-1) = 2b + 2d \\,\\vdots\\, 5 \\Rightarrow b \\,\\vdots\\, 5$ (0.15đ)\n+ Suy ra $a + c \\,\\vdots\\, 5$. Xét $f(2) = 8a + 4b + 2c + d \\,\\vdots\\, 5 \\Rightarrow 8a + 2c = 2(a+c) + 6a \\,\\vdots\\, 5 \\Rightarrow 6a \\,\\vdots\\, 5 \\Rightarrow a \\,\\vdots\\, 5 \\Rightarrow c \\,\\vdots\\, 5$ (0.25đ)",
                    "Thay các giá trị $x = 0, 1, -1, 2$ vào đa thức, từ hệ phương trình chia hết cho 5 suy ra lần lượt $d, b, a, c$ đều chia hết cho 5."
                )
            ]
        })

    return exams

# ==============================================================================
# 6 MÃ ĐỀ CUỐI KỲ 2 - TOÁN 7 (final2)
# Phạm vi: Toàn bộ HK2: Dãy tỉ số, Đa thức, Xác suất biến cố, Đồng quy tam giác, Lăng trụ đứng
# ==============================================================================
def generate_g7_final2():
    exams = []
    
    for t_idx in range(1, 7):
        ex_num = f"0{t_idx}"
        topics = [
            "Đa thức một biến, Xác suất biến cố, Sự đồng quy ba đường trung tuyến & Lăng trụ đứng",
            "Dãy tỉ số bằng nhau, Nghiệm đa thức, Ba đường phân giác và Thể tích hình lăng trụ",
            "Xác suất ngẫu nhiên, Ba đường trung trực tam giác, Diện tích xung quanh hình hộp",
            "Nhân chia đa thức, Trực tâm của tam giác & Hình lăng trụ đứng tam giác thực tế",
            "Tính chất ba đường đồng quy, Biến cố chắc chắn/không thể & Thể tích khối lăng trụ",
            "Ôn tập toàn diện cuối năm Toán 7: Đại số, Xác suất và Hình học không gian trực quan"
        ]
        topic = topics[t_idx - 1]

        exams.append({
            "id": f"p_g7_final2_{ex_num}",
            "testNum": t_idx,
            "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ II - TOÁN 7 (ĐỀ SỐ {ex_num})",
            "topic": topic,
            "grade": "7",
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
                make_mc(1, "Nhận biết", "Giao điểm của ba đường trung tuyến trong một tam giác được gọi là:", ["Trọng tâm", "Trực tâm", "Tâm đường tròn ngoại tiếp", "Tâm đường tròn nội tiếp"], 0, "Ba đường trung tuyến của tam giác đồng quy tại một điểm gọi là trọng tâm của tam giác đó."),
                make_mc(2, "Nhận biết", "Hình lăng trụ đứng tam giác có bao nhiêu mặt bên?", ["$3$ mặt bên", "$4$ mặt bên", "$5$ mặt bên", "$6$ mặt bên"], 0, "Lăng trụ đứng tam giác có 2 mặt đáy và 3 mặt bên hình chữ nhật."),
                make_mc(3, "Nhận biết", "Trong các biến cố sau, biến cố nào là biến cố chắc chắn?", ["Mặt trời mọc ở hướng Đông", "Gieo đồng xu được mặt sấp", "Ngày mai trời sẽ mưa", "Gieo con xúc xắc được mặt 7 chấm"], 0, "Mặt trời luôn mọc ở hướng Đông nên là biến cố chắc chắn."),
                make_mc(4, "Thông hiểu", f"Cho tam giác $ABC$ có trung tuyến $AM$, trọng tâm $G$. Tỉ số $\\frac{{AG}}{{AM}}$ bằng:", ["$\\frac{2}{3}$", "$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{3}{2}$"], 0, "Theo tính chất trọng tâm: khoảng cách từ trọng tâm đến đỉnh bằng 2/3 độ dài đường trung tuyến."),
                make_mc(5, "Thông hiểu", f"Thể tích của hình lăng trụ đứng có diện tích đáy $S = {10 * t_idx}\\,\\text{{cm}}^2$ và chiều cao $h = 5\\,\\text{{cm}}$ là:", [f"${50 * t_idx}\\,\\text{{cm}}^3$", f"${25 * t_idx}\\,\\text{{cm}}^3$", f"${15 * t_idx}\\,\\text{{cm}}^3$", f"${100 * t_idx}\\,\\text{{cm}}^3$"], 0, f"$V = S \\cdot h = {10*t_idx} \\cdot 5 = {50*t_idx}\\,\\text{{cm}}^3$."),
                make_mc(6, "Thông hiểu", "Gieo ngẫu nhiên một con xúc xắc 6 mặt cân đối. Xác suất của biến cố 'Mặt xuất hiện có số chấm là số chẵn' là:", ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"], 0, "Có 3 mặt chẵn (2, 4, 6) trong 6 mặt: xác suất là 3/6 = 1/2."),
                make_mc(7, "Vận dụng", f"Cho tam giác $ABC$ cân tại $A$. Đường trung trực của cạnh $AC$ cắt $BC$ tại $D$. Biết $AB = {5 * t_idx}\\,\\text{{cm}}$, $CD = {3 * t_idx}\\,\\text{{cm}}$. Độ dài đoạn thẳng $AD$ là:", [f"${3 * t_idx}\\,\\text{{cm}}$", f"${5 * t_idx}\\,\\text{{cm}}$", f"${2 * t_idx}\\,\\text{{cm}}$", f"${4 * t_idx}\\,\\text{{cm}}$"], 0, f"Điểm $D$ thuộc trung trực của $AC$ nên $DA = DC = {3*t_idx}\\,\\text{{cm}}$."),
                make_mc(8, "Vận dụng", f"Một khối bê tông hình lăng trụ đứng tứ giác có đáy là hình vuông cạnh $0,{t_idx}\\,\\text{{m}}$, chiều cao lăng trụ là $2\\,\\text{{m}}$. Thể tích khối bê tông đó là:", [f"${0.2 * (t_idx**2):.3f}\\,\\text{{m}}^3$".rstrip("0").rstrip("."), "1 m³", "2 m³", "0.5 m³"], 0, f"Diện tích đáy: $S = ({t_idx}/10)^2$. Thể tích: $V = S \\cdot h = {0.2 * (t_idx**2):.3f}$ m³."),
                make_mc(9, "Vận dụng cao", f"Cho đa thức $P(x) = (x - 1)(x - 2)(x - 3) + {t_idx}$. Nghiệm của đa thức $P(x) - {t_idx}$ có bao nhiêu giá trị phân biệt?", ["$3$", "$1$", "$2$", "$0$"], 0, "$P(x) - t_idx = (x-1)(x-2)(x-3) = 0$ có đúng 3 nghiệm phân biệt là 1, 2, 3."),
                make_mc(10, "Vận dụng cao", "Trong tam giác nhọn $ABC$, trực tâm $H$ trùng với trọng tâm $G$. Tam giác $ABC$ là tam giác gì?", ["Tam giác đều", "Tam giác vuông cân", "Tam giác vuông", "Tam giác tù"], 0, "Tam giác có trực tâm trùng trọng tâm là tam giác đều."),
                make_mc(11, "Vận dụng cao", f"Một hộp có {10 + t_idx} quả cầu gồm 4 màu đỏ, xanh, vàng, trắng. Biết số quả cầu đỏ gấp đôi số quả cầu xanh. Lấy ngẫu nhiên 1 quả cầu, xác suất lấy quả đỏ là $1/3$. Số quả cầu đỏ trong hộp là:", [f"${(10 + t_idx) // 3 if (10 + t_idx)%3==0 else 4}$", "$2$", "$5$", "$6$"], 0, "Xác suất lấy quả đỏ = Số quả đỏ / Tổng số quả."),
                make_mc(12, "Vận dụng cao", f"Cho tam giác $ABC$ có trung tuyến $AM = {6 * t_idx}\\,\\text{{cm}}$. Trên đoạn $AM$ lấy hai điểm $G, K$ sao cho $AG = GK = KM$. Khẳng định nào sau đây đúng?", ["$G$ là trọng tâm của tam giác $ABC$", "$K$ là trọng tâm của tam giác $ABC$", "$AM = 2BC$", "$G$ là trực tâm tam giác $ABC$"], 0, f"$AG = 2/3 AM$ nên $G$ chính là trọng tâm của tam giác $ABC$.")
            ],
            "part2": [
                make_tf(1, f"Gieo ngẫu nhiên một con xúc xắc 6 mặt đồng chất một lần.", [
                    {"id": "a", "text": "Số kết quả có thể xảy ra của phép thử là 6.", "correct": True, "level": "Nhận biết", "explanation": "Con xúc xắc có 6 mặt từ 1 đến 6 chấm."},
                    {"id": "b", "text": "Biến cố 'Xuất hiện mặt 8 chấm' là biến cố không thể.", "correct": True, "level": "Nhận biết", "explanation": "Mặt xúc xắc chỉ có từ 1 đến 6 chấm."},
                    {"id": "c", "text": "Xác suất xuất hiện mặt có số chấm chia hết cho 3 là $\\frac{1}{3}$.", "correct": True, "level": "Thông hiểu", "explanation": "Các mặt chia hết cho 3 là {3, 6}, có 2 mặt. Xác suất: 2/6 = 1/3."},
                    {"id": "d", "text": "Xác suất xuất hiện mặt có số chấm là số nguyên tố bằng $1$.", "correct": False, "level": "Vận dụng", "explanation": "Các số nguyên tố là {2, 3, 5}, xác suất là 3/6 = 1/2 != 1."}
                ]),
                make_tf(2, f"Cho hình lăng trụ đứng tam giác $ABC.A'B'C'$ có đáy là tam giác vuông tại $A$ với $AB = 3\\,\\text{{cm}}$, $AC = 4\\,\\text{{cm}}$ và chiều cao lăng trụ $AA' = {5 * t_idx}\\,\\text{{cm}}$.", [
                    {"id": "a", "text": "Hai mặt đáy $(ABC)$ và $(A'B'C')$ là hai tam giác bằng nhau.", "correct": True, "level": "Nhận biết", "explanation": "Theo định nghĩa lăng trụ đứng, hai đáy bằng nhau."},
                    {"id": "b", "text": "Diện tích đáy của hình lăng trụ bằng $6\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "Tam giác vuông: $S = (1/2) \\cdot 3 \\cdot 4 = 6\\,\\text{cm}^2$."},
                    {"id": "c", "text": f"Thể tích hình lăng trụ bằng ${30 * t_idx}\\,\\text{{cm}}^3$.", "correct": True, "level": "Thông hiểu", "explanation": f"$V = S \\cdot h = 6 \\cdot {5*t_idx} = {30*t_idx}\\,\\text{{cm}}^3$."},
                    {"id": "d", "text": "Độ dài cạnh $BC$ bằng $7\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "Theo định lí Pythagore: $BC = \\sqrt{3^2 + 4^2} = 5\\,\\text{cm} \\neq 7\\,\\text{cm}$."}
                ])
            ],
            "part3": [
                make_sa(1, "Nhận biết", "Điểm cách đều ba đỉnh của một tam giác là giao điểm của ba đường gì trong tam giác? (Trả lời: Trung trực, Trung tuyến, Phân giác hay Đường cao)", "Trung trực", ["Trung trực", "trung truc", "đường trung trực"], "Giao điểm ba đường trung trực cách đều 3 đỉnh."),
                make_sa(2, "Thông hiểu", f"Tính diện tích xung quanh của một hình lăng trụ đứng tứ giác có chu vi đáy $C = {12 * t_idx}\\,\\text{{cm}}$ và chiều cao $h = 5\\,\\text{{cm}}$ (theo $\\text{{cm}}^2$):", str(60 * t_idx), [str(60 * t_idx)], f"$S_{{xq}} = C \\cdot h = {12*t_idx} \\cdot 5 = {60*t_idx}\\,\\text{{cm}}^2$."),
                make_sa(3, "Vận dụng", f"Một tổ công nhân sản xuất gồm 5 bạn nam và {5 + t_idx} bạn nữ. Chọn ngẫu nhiên một bạn làm tổ trưởng. Tính xác suất chọn được một bạn nam (viết dưới dạng phân số tối giản a/b):", f"5/{10 + t_idx}", [f"5/{10 + t_idx}"], f"Xác suất = 5 / (5 + 5 + {t_idx}) = 5/{10 + t_idx}."),
                make_sa(4, "Vận dụng cao", f"Cho tam giác $ABC$ có trọng tâm $G$. Biết diện tích tam giác $ABC$ bằng ${18 * t_idx}\\,\\text{{cm}}^2$. Tính diện tích tam giác $GBC$ (theo $\\text{{cm}}^2$).", str(6 * t_idx), [str(6 * t_idx)], f"Trọng tâm chia tam giác thành 3 tam giác có diện tích bằng nhau: $S_{{GBC}} = S_{{ABC}} / 3 = {18*t_idx} / 3 = {6*t_idx}\\,\\text{{cm}}^2$.")
            ],
            "part4": [
                make_essay(1, "Nhận biết", 1.0,
                    f"Cho đa thức: $P(x) = {t_idx}x^3 - 3x^2 + 2x - 5$ và $Q(x) = -{t_idx}x^3 + 5x^2 - 4$.\n a) Thu gọn và sắp xếp các đa thức theo lũy thừa giảm dần của biến.\n b) Tính $H(x) = P(x) + Q(x)$ và tìm bậc của đa thức $H(x)$.",
                    "a) Các đa thức đã được sắp xếp giảm dần (0.5đ)\nb) $H(x) = (-3 + 5)x^2 + 2x + (-5 - 4) = 2x^2 + 2x - 9$. Bậc của $H(x)$ là 2 (0.5đ)",
                    "a) Sắp xếp đa thức giảm dần.\nb) Cộng hai đa thức: $H(x) = 2x^2 + 2x - 9$, bậc 2."
                ),
                make_essay(2, "Thông hiểu", 1.0,
                    f"Một chiếc lều cắm trại có dạng hình lăng trụ đứng tam giác với đáy là tam giác vuông có hai cạnh góc vuông dài $1,5\\,\\text{{m}}$ và $2\\,\\text{{m}}$. Chiều dài lều (chiều cao lăng trụ) là ${2 + t_idx * 0.5:.1f}\\,\\text{{m}}$.\n a) Tính thể tích không khí bên trong chiếc lều.\n b) Người ta muốn may vải bạt xung quanh lều (không tính mặt đáy tiếp xúc đất). Biết cạnh huyền của đáy là $2,5\\,\\text{{m}}$, tính diện tích vải bạt cần dùng.",
                    f"a) $S_{{day}} = \\frac{{1}}{{2}} \\cdot 1,5 \\cdot 2 = 1,5\\,\\text{{m}}^2$. $V = 1,5 \\cdot {2 + t_idx * 0.5:.1f}\\,\\text{{m}}^3$ (0.5đ)\nb) Vải xung quanh = hai mặt bên: $(1,5 + 2,5) \\cdot {2 + t_idx * 0.5:.1f}$ (0.5đ)",
                    "a) Tính diện tích đáy tam giác vuông rồi nhân với chiều cao để tìm thể tích.\nb) Tính diện tích các mặt bên cần che bạt."
                ),
                make_essay(3, "Vận dụng", 0.5,
                    f"Cho tam giác $ABC$ cân tại $A$, đường trung tuyến $AM$. Gọi $G$ là trọng tâm của tam giác $ABC$.\n a) Chứng minh rằng $AM \\perp BC$.\n b) Biết $AM = {9 * t_idx}\\,\\text{{cm}}$. Tính độ dài đoạn thẳng $AG$ và $GM$.",
                    f"a) Trong tam giác cân, đường trung tuyến xuất phát từ đỉnh đồng thời là đường cao nên $AM \\perp BC$ (0.25đ)\nb) Theo tính chất trọng tâm: $AG = \\frac{{2}}{{3}} AM = {6*t_idx}\\,\\text{{cm}}$, $GM = \\frac{{1}}{{3}} AM = {3*t_idx}\\,\\text{{cm}}$ (0.25đ)",
                    f"a) $AM$ là trung tuyến của tam giác cân nên vuông góc đáy $BC$.\nb) $AG = {6*t_idx}\\,\\text{{cm}}, GM = {3*t_idx}\\,\\text{{cm}}$."
                ),
                make_essay(4, "Vận dụng cao", 0.5,
                    f"Tìm giá trị nhỏ nhất của biểu thức $A = (x - {t_idx})^2 + |y + 2| + 2025$.",
                    f"Vì $(x - {t_idx})^2 \\ge 0$ và $|y + 2| \\ge 0$ với mọi $x, y$ (0.25đ)\nSuy ra $A \\ge 2025$. Dấu '=' xảy ra khi $x = {t_idx}$ và $y = -2$. Vậy $\\min A = 2025$ (0.25đ)",
                    f"Tổng các số không âm luôn lớn hơn hoặc bằng 0, đạt giá trị nhỏ nhất bằng 2025 tại $x = {t_idx}, y = -2$."
                )
            ]
        })

    return exams

def main():
    print("=== SINH VÀ KIỂM TRA ĐỀ ĐỊNH KỲ TOÁN 7 ===")
    mid2_exams = generate_g7_mid2()
    final2_exams = generate_g7_final2()

    assert len(mid2_exams) == 6, f"Thiếu đề mid2: {len(mid2_exams)} != 6"
    assert len(final2_exams) == 6, f"Thiếu đề final2: {len(final2_exams)} != 6"

    for idx, ex in enumerate(mid2_exams, 1):
        validate_periodic_exam(ex, "7", "mid2", idx)
        print(f"✅ Toán 7 - Giữa kỳ 2 (Đề {idx}): ĐẠT CHUẨN MA TRẬN 100%.")

    for idx, ex in enumerate(final2_exams, 1):
        validate_periodic_exam(ex, "7", "final2", idx)
        print(f"✅ Toán 7 - Cuối kỳ 2 (Đề {idx}): ĐẠT CHUẨN MA TRẬN 100%.")

    print("🎉 Hoàn thành xuất sắc 12 đề định kỳ Toán 7!")
    return mid2_exams, final2_exams

if __name__ == "__main__":
    main()
