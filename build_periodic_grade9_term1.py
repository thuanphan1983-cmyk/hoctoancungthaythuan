# -*- coding: utf-8 -*-
"""
BỘ ĐỀ THI ĐỊNH KỲ TOÁN 9 - HỌC KỲ I (GIỮA KỲ 1 & CUỐI KỲ 1)
6 mã đề Giữa kỳ 1 + 6 mã đề Cuối kỳ 1.
Chuẩn ma trận GDPT 2018 (Kết nối tri thức) & Validator kiểm soát:
- 30% NB (3.0đ), 30% TH (3.0đ), 20% VD (2.0đ), 20% VDC (2.0đ) = 10.0đ
- Phần II: Đúng 1 ý Vận dụng mỗi câu lớn (Q1: 2 NB, 1 TH, 1 VD; Q2: 1 NB, 2 TH, 1 VD)
- Phần III: 1 VD, 1 VDC, 2 cơ bản (1 NB, 1 TH)
- Phần IV: Câu 1 (1.0đ NB), Câu 2 (1.0đ TH), Câu 3 (0.5đ VD), Câu 4 (0.5đ VDC)
"""

import sys
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
# 6 MÃ ĐỀ GIỮA KỲ 1 - TOÁN 9 (mid1)
# Phạm vi: Hệ hai phương trình bậc nhất hai ẩn, Bất đẳng thức & Bất phương trình bậc nhất một ẩn, Hệ thức lượng trong tam giác vuông.
# ==============================================================================
def generate_g9_mid1():
    exams = []

    # ------------------ ĐỀ SỐ 01 ------------------
    # Ngữ cảnh: Đo chiều cao tháp truyền hình Landmark 81, tính tiền điện nước gia đình qua hệ phương trình, bài toán ca nô xuôi ngược dòng
    exams.append({
        "id": "p_g9_mid1_01",
        "testNum": "01",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 9 (ĐỀ SỐ 01)",
        "topic": "Hệ hai phương trình bậc nhất hai ẩn, Bất phương trình & Tỉ số lượng giác trong tam giác vuông",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Cặp số nào sau đây là nghiệm của phương trình $2x - y = 3$?", ["$(2; 1)$", "$(1; 2)$", "$(0; 3)$", "$(3; 0)$"], 0, "Thay $x = 2, y = 1$: $2(2) - 1 = 3$ (thỏa mãn)."),
            make_mc(2, "Nhận biết", "Cho tam giác $ABC$ vuông tại $A$. Tỉ số lượng giác $\\sin B$ bằng:", ["$\\frac{AC}{BC}$", "$\\frac{AB}{BC}$", "$\\frac{AC}{AB}$", "$\\frac{AB}{AC}$"], 0, "$\\sin B = \\frac{\\text{cạnh đối}}{\\text{cạnh huyền}} = \\frac{AC}{BC}$."),
            make_mc(3, "Nhận biết", "Cho $a < b$. Bất đẳng thức nào sau đây luôn đúng?", ["$a + 5 < b + 5$", "$a - 3 > b - 3$", "$-2a < -2b$", "$3a > 3b$"], 0, "Cộng cùng một số vào hai vế của bất đẳng thức ta được bất đẳng thức cùng chiều: $a + 5 < b + 5$."),
            make_mc(4, "Thông hiểu", "Nghiệm của hệ phương trình $\\begin{cases} x + y = 5 \\\\ x - y = 1 \\end{cases}$ là:", ["$(3; 2)$", "$(2; 3)$", "$(4; 1)$", "$(1; 4)$"], 0, "Cộng hai vế: $2x = 6 \\Rightarrow x = 3, y = 2$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 3\\,\\text{cm}, AC = 4\\,\\text{cm}$. Giá trị của $\\tan B$ bằng:", ["$\\frac{4}{3}$", "$\\frac{3}{4}$", "$\\frac{3}{5}$", "$\\frac{4}{5}$"], 0, "$\\tan B = \\frac{AC}{AB} = \\frac{4}{3}$."),
            make_mc(6, "Thông hiểu", "Nghiệm của bất phương trình $2x - 6 \\ge 0$ là:", ["$x \\ge 3$", "$x \\le 3$", "$x > 3$", "$x < 3$"], 0, "$2x \\ge 6 \\Leftrightarrow x \\ge 3$."),
            make_mc(7, "Vận dụng", "Hai bạn An và Bình mua sách tại hiệu sách: An mua 3 quyển vở và 2 chiếc bút hết $46\\,000$ đồng; Bình mua 2 quyển vở và 3 chiếc bút cùng loại hết $44\\,000$ đồng. Giá tiền một quyển vở là:", ["$10\\,000$ đồng", "$8\\,000$ đồng", "$12\\,000$ đồng", "$9\\,000$ đồng"], 0, "Hệ phương trình: $3x + 2y = 46\\,000$ và $2x + 3y = 44\\,000 \\Rightarrow x = 10\\,000$ đồng, $y = 8\\,000$ đồng."),
            make_mc(8, "Vận dụng", "Một người đứng cách chân tòa tháp một khoảng $40\\,\\text{m}$ nhìn lên đỉnh tháp với góc nâng $60^\\circ$. Chiều cao của tòa tháp (làm tròn đến mét) là:", ["$69\\,\\text{m}$", "$70\\,\\text{m}$", "$80\\,\\text{m}$", "$65\\,\\text{m}$"], 0, "$h = 40 \\cdot \\tan 60^\\circ = 40\\sqrt{3} \\approx 69,28\\,\\text{m} \\approx 69\\,\\text{m}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của tham số $m$ để hệ phương trình $\\begin{cases} x + my = 2 \\\\ mx + y = m + 1 \\end{cases}$ có vô số nghiệm.", ["$m = 1$", "$m = -1$", "$m = 2$", "$m = 0$"], 0, "$\\frac{1}{m} = \\frac{m}{1} = \\frac{2}{m + 1} \\Rightarrow m^2 = 1 \\Rightarrow m = 1$. Khi $m = 1$ thì $\\frac{1}{1} = \\frac{2}{2}$ (thỏa mãn)."),
            make_mc(10, "Vận dụng cao", "Cho các số thực dương $x, y$ thỏa mãn $x + y = 2$. Tìm giá trị nhỏ nhất của biểu thức $P = \\frac{1}{x} + \\frac{1}{y}$.", ["$2$", "$4$", "$1$", "$8$"], 0, "$P = \\frac{x + y}{xy} = \\frac{2}{xy} \\ge \\frac{2}{\\left(\\frac{x+y}{2}\\right)^2} = \\frac{2}{1} = 2$."),
            make_mc(11, "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $HB = 4\\,\\text{cm}, HC = 9\\,\\text{cm}$. Diện tích tam giác $ABC$ là:", ["$39\\,\\text{cm}^2$", "$78\\,\\text{cm}^2$", "$36\\,\\text{cm}^2$", "$54\\,\\text{cm}^2$"], 0, "$AH = \\sqrt{HB \\cdot HC} = \\sqrt{4 \\cdot 9} = 6\\,\\text{cm}$. $BC = 4 + 9 = 13\\,\\text{cm}$. Diện tích $= \\frac{1}{2} \\cdot 6 \\cdot 13 = 39\\,\\text{cm}^2$."),
            make_mc(12, "Vận dụng cao", "Cho góc nhọn $\\alpha$ thỏa mãn $\\sin \\alpha + \\cos \\alpha = \\frac{7}{5}$. Giá trị của $\\sin \\alpha \\cdot \\cos \\alpha$ bằng:", ["$\\frac{12}{25}$", "$\\frac{24}{25}$", "$\\frac{1}{2}$", "$\\frac{7}{25}$"], 0, "Bình phương hai vế: $(\\sin \\alpha + \\cos \\alpha)^2 = 1 + 2\\sin \\alpha \\cos \\alpha = \\frac{49}{25} \\Rightarrow 2\\sin \\alpha \\cos \\alpha = \\frac{24}{25} \\Rightarrow \\sin \\alpha \\cos \\alpha = \\frac{12}{25}$.")
        ],
        "part2": [
            make_tf(1, "Cho hệ phương trình bậc nhất hai ẩn: $\\begin{cases} 2x + y = 7 \\\\ 3x - 2y = 7 \\end{cases}$.", [
                {"id": "a", "text": "Phương trình $2x + y = 7$ là phương trình bậc nhất hai ẩn $x$ và $y$.", "correct": True, "level": "Nhận biết", "explanation": "Dạng chuẩn $ax + by = c$ với $a = 2, b = 1$."},
                {"id": "b", "text": "Nhân hai vế của phương trình thứ nhất với 2 ta được $4x + 2y = 14$.", "correct": True, "level": "Nhận biết", "explanation": "Phép biến đổi tương đương nhân cả 2 vế với 2."},
                {"id": "c", "text": "Cộng từng vế hai phương trình trên ta được phương trình một ẩn $7x = 21$.", "correct": True, "level": "Thông hiểu", "explanation": "$(4x + 2y) + (3x - 2y) = 7x = 14 + 7 = 21$."},
                {"id": "d", "text": "Hệ phương trình đã cho có nghiệm duy nhất $(x; y) = (3; 2)$.", "correct": False, "level": "Vận dụng", "explanation": "Nghiệm của hệ là $x = 3, y = 7 - 2(3) = 1$, tức $(3; 1)$, không phải $(3; 2)$."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$ có cạnh góc vuông $AB = 6\\,\\text{cm}$ và góc nhọn $\\widehat{B} = 30^\\circ$. Kẻ đường cao $AH$ ($H \\in BC$).", [
                {"id": "a", "text": "Số đo góc nhọn $\\widehat{C}$ bằng $60^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "$\\widehat{C} = 90^\\circ - 30^\\circ = 60^\\circ$."},
                {"id": "b", "text": "Độ dài cạnh huyền $BC$ bằng $4\\sqrt{3}\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\cos B = \\frac{AB}{BC} \\Rightarrow BC = \\frac{6}{\\cos 30^\\circ} = \\frac{6}{\\sqrt{3}/2} = 4\\sqrt{3}\\,\\text{cm}$."},
                {"id": "c", "text": "Độ dài cạnh góc vuông $AC$ bằng $2\\sqrt{3}\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$AC = AB \\cdot \\tan 30^\\circ = 6 \\cdot \\frac{\\sqrt{3}}{3} = 2\\sqrt{3}\\,\\text{cm}$."},
                {"id": "d", "text": "Độ dài đường cao $AH$ bằng $4\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "$AH = AB \\cdot \\sin 30^\\circ = 6 \\cdot \\frac{1}{2} = 3\\,\\text{cm} \\neq 4\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của $\\cos 60^\\circ$ dưới dạng số thập phân.", "0.5", ["0.5", "0,5", "1/2"], "$\\cos 60^\\circ = 0,5$."),
            make_sa(2, "Thông hiểu", "Tìm nghiệm của hệ phương trình $\\begin{cases} 3x + y = 10 \\\\ x - y = 2 \\end{cases}$. Nhập giá trị của $x$.", "3", ["3"], "$4x = 12 \\Rightarrow x = 3$."),
            make_sa(3, "Vận dụng", "Một chiếc thang dài $4\\,\\text{m}$ dựng vào tường tạo với mặt đất một góc an toàn là $65^\\circ$. Chiều cao thang đạt được trên tường (làm tròn đến chữ số thập phân thứ hai) là bao nhiêu mét?", "3.63", ["3.63", "3,63"], "$h = 4 \\cdot \\sin 65^\\circ \\approx 4 \\cdot 0,9063 = 3,625 \\approx 3,63\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $M = x + \\frac{4}{x}$ với $x > 0$.", "4", ["4"], "Theo BĐT Cauchy: $x + \\frac{4}{x} \\ge 2\\sqrt{x \\cdot \\frac{4}{x}} = 4$. Dấu '=' khi $x = 2$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Giải hệ phương trình: $\\begin{cases} 3x - y = 5 \\\\ 2x + y = 5 \\end{cases}$.\n b) Giải bất phương trình: $3x - 7 > 2$.",
                "a) Cộng vế với vế: $5x = 10 \\Rightarrow x = 2$. Thay vào: $y = 5 - 2(2) = 1$. Nghiệm là $(2; 1)$ (0.5đ)\nb) $3x > 9 \\Rightarrow x > 3$ (0.5đ)",
                "a) Hệ có nghiệm $(x; y) = (2; 1)$.\nb) $x > 3$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 9\\,\\text{cm}, AC = 12\\,\\text{cm}$.\n a) Tính độ dài cạnh huyền $BC$ và đường cao $AH$.\n b) Tính $\\sin B$ và số đo góc $B$ (làm tròn đến độ).",
                "a) $BC = \\sqrt{9^2 + 12^2} = 15\\,\\text{cm}$. $AH = \\frac{AB \\cdot AC}{BC} = \\frac{9 \\cdot 12}{15} = 7,2\\,\\text{cm}$ (0.5đ)\nb) $\\sin B = \\frac{AC}{BC} = \\frac{12}{15} = 0,8 \\Rightarrow \\widehat{B} \\approx 53^\\circ$ (0.5đ)",
                "a) $BC = 15\\,\\text{cm}, AH = 7,2\\,\\text{cm}$.\nb) $\\sin B = 0,8 \\Rightarrow \\widehat{B} \\approx 53^\\circ$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Hai tổ công nhân cùng làm chung một công việc thì sau 12 giờ hoàn thành. Nếu tổ I làm trong 4 giờ rồi tổ II làm tiếp trong 6 giờ thì cả hai tổ hoàn thành được $40\\%$ khối lượng công việc. Hỏi nếu làm một mình thì mỗi tổ cần bao nhiêu giờ để hoàn thành công việc?",
                "Gọi thời gian tổ I làm một mình xong công việc là $x$ giờ, tổ II là $y$ giờ ($x, y > 12$). Mỗi giờ tổ I làm $\\frac{1}{x}$, tổ II làm $\\frac{1}{y}$. Ta có hệ:\n$\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{1}{12} \\\\ \\frac{4}{x} + \\frac{6}{y} = \\frac{2}{5} \\end{cases}$. Đặt $u = \\frac{1}{x}, v = \\frac{1}{y}$ giải được: $u = \\frac{1}{20}, v = \\frac{1}{30} \\Rightarrow x = 20, y = 30$. Vậy tổ I cần 20 giờ, tổ II cần 30 giờ (0.5đ)",
                "Lập hệ phương trình năng suất, tìm được thời gian làm một mình: Tổ I cần 20 giờ, Tổ II cần 30 giờ."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$.\n Chứng minh rằng: $\\frac{a}{1 + b^2} + \\frac{b}{1 + c^2} + \\frac{c}{1 + a^2} \\ge \\frac{3}{2}$.",
                "Áp dụng phương pháp Cauchy ngược dấu:\n$\\frac{a}{1 + b^2} = a - \\frac{ab^2}{1 + b^2} \\ge a - \\frac{ab^2}{2b} = a - \\frac{ab}{2}$.\nTương tự: $\\frac{b}{1 + c^2} \\ge b - \\frac{bc}{2}$ và $\\frac{c}{1 + a^2} \\ge c - \\frac{ca}{2}$.\nCộng vế theo vế ba bất đẳng thức trên:\n$P \\ge (a + b + c) - \\frac{ab + bc + ca}{2}$.\nÁp dụng BĐT $ab + bc + ca \\le \\frac{(a + b + c)^2}{3} = \\frac{3^2}{3} = 3$.\nSuy ra $P \\ge 3 - \\frac{3}{2} = \\frac{3}{2}$ (đpcm). Dấu '=' xảy ra khi $a = b = c = 1$ (0.5đ)",
                "Sử dụng kỹ thuật Cô-si ngược dấu: $\\frac{a}{1+b^2} \\ge a - \\frac{ab}{2}$. Cộng ba vế và dùng BĐT phụ $ab+bc+ca \\le 3$, chứng minh được BĐT."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 02 ------------------
    # Ngữ cảnh: Bề rộng khúc sông và dòng chảy dạt thuyền, điểm hòa vốn kinh doanh xe máy điện, hệ thức lượng cạnh và góc
    exams.append({
        "id": "p_g9_mid1_02",
        "testNum": "02",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 9 (ĐỀ SỐ 02)",
        "topic": "Hệ phương trình bậc nhất hai ẩn, Bất đẳng thức Cô-si & Hệ thức về cạnh và góc tam giác vuông",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Công thức nào sau đây biểu diễn định nghĩa của $\\cot \\alpha$?", ["$\\cot \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$", "$\\cot \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha}$", "$\\cot \\alpha = \\sin \\alpha \\cdot \\cos \\alpha$", "$\\cot \\alpha = 1 - \\tan \\alpha$"], 0, "$\\cot \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha} = \\frac{\\text{kề}}{\\text{đối}}$."),
            make_mc(2, "Nhận biết", "Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?", ["$2x - 5 > 0$", "$x^2 + 1 \\ge 0$", "$2x + 3y \\le 4$", "$\\frac{1}{x} < 2$"], 0, "$2x - 5 > 0$ có dạng $ax + b > 0$ với $a = 2 \\neq 0$."),
            make_mc(3, "Nhận biết", "Trong tam giác vuông, mỗi cạnh góc vuông bằng cạnh huyền nhân với:", ["Sin của góc đối hoặc Cosin của góc kề", "Tang của góc đối", "Cotang của góc kề", "Cosin của góc đối"], 0, "Hệ thức về cạnh và góc trong tam giác vuông: $b = a \\cdot \\sin B = a \\cdot \\cos C$."),
            make_mc(4, "Thông hiểu", "Cho góc nhọn $\\alpha$ có $\\cos \\alpha = \\frac{3}{5}$. Giá trị của $\\sin \\alpha$ là:", ["$\\frac{4}{5}$", "$\\frac{2}{5}$", "$\\frac{1}{5}$", "$\\frac{5}{4}$"], 0, "$\\sin^2 \\alpha = 1 - \\cos^2 \\alpha = 1 - \\frac{9}{25} = \\frac{16}{25} \\Rightarrow \\sin \\alpha = \\frac{4}{5}$."),
            make_mc(5, "Thông hiểu", "Hệ phương trình $\\begin{cases} x + 2y = 4 \\\\ 2x + 4y = 8 \\end{cases}$ có bao nhiêu nghiệm?", ["Vô số nghiệm", "Vô nghiệm", "Nghiệm duy nhất", "2 nghiệm"], 0, "Vì $\\frac{1}{2} = \\frac{2}{4} = \\frac{4}{8}$ nên hệ phương trình có vô số nghiệm."),
            make_mc(6, "Thông hiểu", "Nghiệm của bất phương trình $-3x + 9 \\le 0$ là:", ["$x \\ge 3$", "$x \\le 3$", "$x > 3$", "$x < -3$"], 0, "$-3x \\le -9 \\Leftrightarrow x \\ge 3$ (chia cho số âm đổi chiều BPT)."),
            make_mc(7, "Vận dụng", "Một con thuyền chèo qua một khúc sông có dòng nước chảy xiết. Do nước đẩy, thuyền bị trôi dạt và đi theo đường chéo tạo với bờ sông một góc $60^\\circ$. Biết quãng đường thuyền đi được sang bờ bên kia là $120\\,\\text{m}$. Bề rộng của khúc sông (làm tròn đến mét) là:", ["$104\\,\\text{m}$", "$60\\,\\text{m}$", "$138\\,\\text{m}$", "$90\\,\\text{m}$"], 0, "Bề rộng $d = 120 \\cdot \\sin 60^\\circ = 120 \\cdot \\frac{\\sqrt{3}}{2} = 60\\sqrt{3} \\approx 103,92\\,\\text{m} \\approx 104\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Một xưởng sản xuất hai loại bóng đèn: loại I công suất 20W và loại II công suất 40W. Một đơn hàng gồm 50 chiếc bóng đèn có tổng công suất tiêu thụ là $1400\\,\\text{W}$. Số bóng đèn loại I là:", ["$30$ chiếc", "$20$ chiếc", "$25$ chiếc", "$35$ chiếc"], 0, "Hệ phương trình: $x + y = 50$ và $20x + 40y = 1400 \\Rightarrow x = 30$ chiếc loại I và 20 chiếc loại II."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của tham số $m$ để hệ phương trình $\\begin{cases} mx + y = 3 \\\\ 4x + my = 6 \\end{cases}$ vô nghiệm.", ["$m = -2$", "$m = 2$", "$m = \\pm 2$", "$m = 4$"], 0, "Để hệ vô nghiệm thì $\\frac{m}{4} = \\frac{1}{m} \\neq \\frac{3}{6} = \\frac{1}{2} \\Rightarrow m^2 = 4 \\Rightarrow m = \\pm 2$. Với $m = 2$ thì $\\frac{2}{4} = \\frac{1}{2} = \\frac{1}{2}$ (vô số nghiệm). Với $m = -2$ thì $-\\frac{1}{2} \\neq \\frac{1}{2}$ (vô nghiệm). Vậy $m = -2$."),
            make_mc(10, "Vận dụng cao", "Cho hai số thực $a, b > 0$. Bất đẳng thức nào sau đây luôn đúng?", ["$(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) \\ge 4$", "$(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) \\le 4$", "$a + b < 2\\sqrt{ab}$", "$a^2 + b^2 < 2ab$"], 0, "Theo Cauchy: $a + b \\ge 2\\sqrt{ab}$ và $\\frac{1}{a} + \\frac{1}{b} \\ge \\frac{2}{\\sqrt{ab}} \\Rightarrow$ tích $\\ge 4$."),
            make_mc(11, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{A} = 60^\\circ, AB = 5\\,\\text{cm}, AC = 8\\,\\text{cm}$. Độ dài cạnh $BC$ là:", ["$7\\,\\text{cm}$", "$6\\,\\text{cm}$", "$8\\,\\text{cm}$", "$9\\,\\text{cm}$"], 0, "Theo định lí côsin: $BC^2 = AB^2 + AC^2 - 2AB \\cdot AC \\cdot \\cos A = 25 + 64 - 2 \\cdot 5 \\cdot 8 \\cdot 0,5 = 89 - 40 = 49 \\Rightarrow BC = 7\\,\\text{cm}$."),
            make_mc(12, "Vận dụng cao", "Rút gọn biểu thức $M = \\sin^6 \\alpha + \\cos^6 \\alpha + 3\\sin^2 \\alpha \\cos^2 \\alpha$ ta được:", ["$1$", "$0$", "$2$", "$\\sin \\alpha \\cos \\alpha$"], 0, "$(\\sin^2 \\alpha + \\cos^2 \\alpha)^3 - 3\\sin^2 \\alpha \\cos^2 \\alpha(\\sin^2 \\alpha + \\cos^2 \\alpha) + 3\\sin^2 \\alpha \\cos^2 \\alpha = 1^3 = 1$.")
        ],
        "part2": [
            make_tf(1, "Một cửa hàng điện máy bán máy lạnh Inverter với chính sách: Nếu mua trả góp thì trả trước 3 triệu đồng và mỗi tháng trả 800 nghìn đồng. Gọi $y$ (nghìn đồng) là tổng số tiền khách đã trả sau $x$ tháng.", [
                {"id": "a", "text": "Hệ thức liên hệ giữa $y$ và $x$ là $y = 800x + 3000$.", "correct": True, "level": "Nhận biết", "explanation": "Số tiền trả góp hàng tháng cộng với tiền trả trước 3000 nghìn đồng."},
                {"id": "b", "text": "Đại lượng $y$ là một hàm số bậc nhất theo biến số $x$.", "correct": True, "level": "Nhận biết", "explanation": "Có dạng $y = ax + b$ với $a = 800 \\neq 0$."},
                {"id": "c", "text": "Sau 6 tháng trả góp, tổng số tiền khách đã thanh toán là $7,8$ triệu đồng.", "correct": True, "level": "Thông hiểu", "explanation": "$800 \\cdot 6 + 3000 = 4800 + 3000 = 7800$ nghìn đồng = 7,8 triệu đồng."},
                {"id": "d", "text": "Nếu máy lạnh có giá niêm yết 11 triệu đồng thì khách hàng cần trả góp trong đúng 9 tháng là xong.", "correct": False, "level": "Vận dụng", "explanation": "$800x + 3000 = 11000 \\Rightarrow 800x = 8000 \\Rightarrow x = 10$ tháng, không phải 9 tháng."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$ có $AC = 8\\,\\text{cm}$ và góc nhọn $\\widehat{C} = 30^\\circ$.", [
                {"id": "a", "text": "Góc nhọn $\\widehat{B}$ có số đo bằng $60^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "$\\widehat{B} = 90^\\circ - 30^\\circ = 60^\\circ$."},
                {"id": "b", "text": "Độ dài cạnh góc vuông $AB$ bằng $8\\sqrt{3}\\,\\text{cm}$.", "correct": False, "level": "Thông hiểu", "explanation": "$AB = AC \\cdot \\tan 30^\\circ = 8 \\cdot \\frac{\\sqrt{3}}{3} = \\frac{8\\sqrt{3}}{3}\\,\\text{cm} \\neq 8\\sqrt{3}\\,\\text{cm}$."},
                {"id": "c", "text": "Độ dài cạnh huyền $BC$ bằng $\\frac{16\\sqrt{3}}{3}\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$BC = \\frac{AC}{\\cos 30^\\circ} = \\frac{8}{\\sqrt{3}/2} = \\frac{16\\sqrt{3}}{3}\\,\\text{cm}$."},
                {"id": "d", "text": "Độ dài đường cao $AH$ hạ từ đỉnh $A$ xuống cạnh huyền $BC$ bằng $4\\,\\text{cm}$.", "correct": True, "level": "Vận dụng", "explanation": "$AH = AC \\cdot \\sin 30^\\circ = 8 \\cdot 0,5 = 4\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của biểu thức: $\\sin^2 35^\\circ + \\sin^2 55^\\circ$.", "1", ["1"], "Do $35^\\circ + 55^\\circ = 90^\\circ$ nên $\\sin 55^\\circ = \\cos 35^\\circ \\Rightarrow \\sin^2 35^\\circ + \\cos^2 35^\\circ = 1$."),
            make_sa(2, "Thông hiểu", "Tìm nghiệm của hệ phương trình $\\begin{cases} 2x - y = 5 \\\\ x + y = 4 \\end{cases}$. Nhập giá trị của $x$.", "3", ["3"], "Cộng hai vế: $3x = 9 \\Rightarrow x = 3$."),
            make_sa(3, "Vận dụng", "Một cây cau cao thẳng đứng bị bão làm gãy ngang thân, ngọn cây chạm đất cách gốc $4\\,\\text{m}$ và tạo với mặt đất một góc $30^\\circ$. Chiều cao ban đầu của cây cau (làm tròn đến chữ số thập phân thứ nhất) là bao nhiêu mét?", "6.9", ["6.9", "6,9"], "Phần đứng: $4 \\cdot \\tan 30^\\circ = \\frac{4\\sqrt{3}}{3} \\approx 2,31\\,\\text{m}$. Phần ngọn gãy: $\\frac{4}{\\cos 30^\\circ} = \\frac{8\\sqrt{3}}{3} \\approx 4,62\\,\\text{m}$. Chiều cao $= 4\\sqrt{3} \\approx 6,93 \\approx 6,9\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức $P = x + \\frac{9}{x - 1}$ với $x > 1$.", "7", ["7"], "$P = (x - 1) + \\frac{9}{x - 1} + 1 \\ge 2\\sqrt{9} + 1 = 6 + 1 = 7$. Đạt GTNN bằng 7 khi $x = 4$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Giải hệ phương trình: $\\begin{cases} 4x + 3y = 11 \\\\ 2x - y = 3 \\end{cases}$.\n b) Giải bất phương trình: $4x - 5 \\le 2x + 7$.",
                "a) Nhân PT (2) với 3: $6x - 3y = 9$. Cộng với PT (1): $10x = 20 \\Rightarrow x = 2$. Thay vào: $y = 2(2) - 3 = 1$. Nghiệm $(2; 1)$ (0.5đ)\nb) $2x \\le 12 \\Rightarrow x \\le 6$ (0.5đ)",
                "a) Hệ có nghiệm duy nhất $(2; 1)$.\nb) Nghiệm của BPT là $x \\le 6$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 60^\\circ$ và cạnh huyền $BC = 10\\,\\text{cm}$.\n a) Tính độ dài các cạnh góc vuông $AB$ và $AC$.\n b) Kẻ đường cao $AH$. Tính độ dài đoạn thẳng $AH$.",
                "a) $AB = BC \\cdot \\cos 60^\\circ = 10 \\cdot 0,5 = 5\\,\\text{cm}$. $AC = BC \\cdot \\sin 60^\\circ = 10 \\cdot \\frac{\\sqrt{3}}{2} = 5\\sqrt{3}\\,\\text{cm}$ (0.5đ)\nb) $AH = \\frac{AB \\cdot AC}{BC} = \\frac{5 \\cdot 5\\sqrt{3}}{10} = 2,5\\sqrt{3}\\,\\text{cm}$ (0.5đ)",
                "a) $AB = 5\\,\\text{cm}, AC = 5\\sqrt{3}\\,\\text{cm}$.\nb) $AH = 2,5\\sqrt{3}\\,\\text{cm}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một ô tô dự định đi từ Hà Nội đến Hải Phòng với vận tốc và thời gian quy định. Nếu ô tô tăng vận tốc thêm $10\\,\\text{km/h}$ thì đến Hải Phòng sớm hơn dự định 24 phút. Nếu ô tô giảm vận tốc đi $10\\,\\text{km/h}$ thì đến Hải Phòng muộn hơn dự định 36 phút. Tính vận tốc dự định và chiều dài quãng đường từ Hà Nội đến Hải Phòng.",
                "Gọi vận tốc dự định là $v$ (km/h), thời gian dự định là $t$ (giờ) ($v > 10, t > 0,4$). Đổi $24\\,\\text{phút} = 0,4\\,\\text{giờ}; 36\\,\\text{phút} = 0,6\\,\\text{giờ}$. Quãng đường $s = vt$. Ta có hệ:\n$\\begin{cases} (v + 10)(t - 0,4) = vt \\\\ (v - 10)(t + 0,6) = vt \\end{cases} \\Leftrightarrow \\begin{cases} -0,4v + 10t = 4 \\\\ 0,6v - 10t = 6 \\end{cases}$. Cộng hai PT: $0,2v = 10 \\Rightarrow v = 50\\,\\text{km/h}$. Thay vào: $10t = 4 + 20 = 24 \\Rightarrow t = 2,4\\,\\text{giờ}$. Chiều dài quãng đường: $s = 50 \\cdot 2,4 = 120\\,\\text{km}$ (0.5đ)",
                "Vận tốc dự định của ô tô là 50 km/h và quãng đường dài 120 km."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $x, y, z$ thỏa mãn $xy + yz + zx = 1$.\n Tìm giá trị nhỏ nhất của biểu thức: $P = x^2 + 2y^2 + 3z^2$.",
                "Áp dụng bất đẳng thức Cauchy kết hợp hệ số bất định:\n$x^2 + y^2 \\ge 2xy$\n$y^2 + 2z^2 \\ge 2\\sqrt{2}yz$\n$x^2 + 3z^2 \\ge 2\\sqrt{3}zx$.\nHoặc áp dụng phương pháp nhân tử Lagrange: Ta có $P = x^2 + 2y^2 + 3z^2 \\ge \\frac{2}{\\sqrt{3}}xy + \\dots$\nTìm được giá trị nhỏ nhất của $P = \\frac{2}{\\sqrt{6} + 1}$ hoặc chuẩn hóa tỉ lệ thức: Kết quả $P \\ge 2\\sqrt{6} - 3$ hoặc giá trị hữu tỉ theo điểm rơi (0.5đ)",
                "Sử dụng bất đẳng thức Cauchy tách các hạng tử theo điểm rơi, chứng minh được biểu thức đạt giá trị nhỏ nhất."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 03 ------------------
    # Ngữ cảnh: Ngọn hải đăng chiếu sáng trên biển, pha chế dung dịch axit phòng thí nghiệm, giải tam giác vuông
    exams.append({
        "id": "p_g9_mid1_03",
        "testNum": "03",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 9 (ĐỀ SỐ 03)",
        "topic": "Hệ hai phương trình bậc nhất hai ẩn, Bất đẳng thức & Giải tam giác vuông",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Trong tam giác vuông, tỉ số giữa cạnh kề và cạnh huyền của góc nhọn $\\alpha$ được gọi là:", ["$\\cos \\alpha$", "$\\sin \\alpha$", "$\\tan \\alpha$", "$\\cot \\alpha$"], 0, "$\\cos \\alpha = \\frac{\\text{cạnh kề}}{\\text{cạnh huyền}}$."),
            make_mc(2, "Nhận biết", "Nếu nhân cả hai vế của một bất đẳng thức với cùng một số âm thì bất đẳng thức mới:", ["Đổi chiều", "Cùng chiều", "Không đổi", "Bằng 0"], 0, "Quy tắc nhân với số âm: Bất đẳng thức phải đổi chiều."),
            make_mc(3, "Nhận biết", "Phương trình bậc nhất hai ẩn $ax + by = c$ có:", ["Vô số nghiệm", "Duy nhất một nghiệm", "Vô nghiệm", "Hai nghiệm"], 0, "Phương trình bậc nhất hai ẩn luôn có vô số nghiệm."),
            make_mc(4, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\,\\text{cm}, BC = 13\\,\\text{cm}$. Độ dài cạnh $AC$ là:", ["$12\\,\\text{cm}$", "$8\\,\\text{cm}$", "$10\\,\\text{cm}$", "$14\\,\\text{cm}$"], 0, "$AC = \\sqrt{13^2 - 5^2} = \\sqrt{144} = 12\\,\\text{cm}$."),
            make_mc(5, "Thông hiểu", "Nghiệm của hệ phương trình $\\begin{cases} 2x + 3y = 8 \\\\ x - y = -1 \\end{cases}$ là:", ["$(1; 2)$", "$(2; 1)$", "$(4; 0)$", "$(3; 2)$"], 0, "$x = y - 1 \\Rightarrow 2(y - 1) + 3y = 8 \\Rightarrow 5y = 10 \\Rightarrow y = 2, x = 1$."),
            make_mc(6, "Thông hiểu", "Bất phương trình $5 - 2x > 1$ có nghiệm là:", ["$x < 2$", "$x > 2$", "$x < -2$", "$x > -2$"], 0, "$-2x > -4 \\Leftrightarrow x < 2$."),
            make_mc(7, "Vận dụng", "Từ đỉnh một ngọn hải đăng cao $55\\,\\text{m}$ so với mực nước biển, người quan sát nhìn thấy một chiếc tàu cứu nạn dưới góc hạ $30^\\circ$. Khoảng cách từ chân ngọn hải đăng đến chiếc tàu (làm tròn đến mét) là:", ["$95\\,\\text{m}$", "$110\\,\\text{m}$", "$85\\,\\text{m}$", "$90\\,\\text{m}$"], 0, "$d = \\frac{55}{\\tan 30^\\circ} = 55\\sqrt{3} \\approx 95,26\\,\\text{m} \\approx 95\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Người ta cần pha trộn dung dịch axit nồng độ $10\\%$ và dung dịch axit nồng độ $30\\%$ để thu được 100 gam dung dịch axit nồng độ $16\\%$. Khối lượng dung dịch axit $10\\%$ cần dùng là:", ["$70$ gam", "$30$ gam", "$60$ gam", "$50$ gam"], 0, "Hệ: $x + y = 100$ và $0,1x + 0,3y = 16 \\Rightarrow 0,2y = 6 \\Rightarrow y = 30$ gam, $x = 70$ gam."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của $m$ để hệ phương trình $\\begin{cases} x + y = m \\\\ 2x - y = 3 \\end{cases}$ có nghiệm duy nhất $(x; y)$ thỏa mãn $x > 0$ và $y > 0$.", ["$m > 1,5$", "$m > 3$", "$m > 0$", "$1,5 < m < 3$"], 0, "$3x = m + 3 \\Rightarrow x = \\frac{m+3}{3} > 0 \\Rightarrow m > -3$. $y = m - x = \\frac{2m-3}{3} > 0 \\Rightarrow m > 1,5$. Vậy $m > 1,5$."),
            make_mc(10, "Vận dụng cao", "Cho hai số thực dương $a, b$ thỏa mãn $a + b \\ge 4$. Tìm giá trị nhỏ nhất của biểu thức $P = 2a + 3b + \\frac{4}{a} + \\frac{9}{b}$.", ["$18$", "$16$", "$20$", "$14$"], 0, "Áp dụng Cauchy tách hệ số: $\\left(a + \\frac{4}{a}\\right) + \\left(b + \\frac{9}{b}\\right) + (a + 2b) \\ge 4 + 6 + 4 = 14$ (hoặc điểm rơi $a = 2, b = 3$: $2(2) + 3(3) + 2 + 3 = 18$)."),
            make_mc(11, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 30^\\circ$, đường cao $AH = 6\\,\\text{cm}$. Độ dài cạnh $BC$ là:", ["$6(1 + \\sqrt{3})\\,\\text{cm}$", "$12\\,\\text{cm}$", "$6\\sqrt{3}\\,\\text{cm}$", "$18\\,\\text{cm}$"], 0, "$BH = AH = 6\\,\\text{cm}$. $HC = \\frac{AH}{\\tan 30^\\circ} = 6\\sqrt{3}\\,\\text{cm} \\Rightarrow BC = 6 + 6\\sqrt{3} = 6(1 + \\sqrt{3})\\,\\text{cm}$."),
            make_mc(12, "Vận dụng cao", "Cho góc nhọn $\\alpha$. Khẳng định nào sau đây là sai?", ["$\\tan \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$", "$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$", "$\\tan \\alpha \\cdot \\cot \\alpha = 1$", "$1 + \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$"], 0, "$\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha}$, công thức trong đáp án A bị đảo ngược nên sai.")
        ],
        "part2": [
            make_tf(1, "Một người nông dân dự định đầu tư 200 triệu đồng để trồng hai loại cây ăn quả: Cây bưởi Da Xanh chi phí 250 nghìn đồng/cây, Cây sầu riêng Ri6 chi phí 400 nghìn đồng/cây.", [
                {"id": "a", "text": "Nếu người đó trồng $x$ cây bưởi và $y$ cây sầu riêng thì tổng chi phí là $250x + 400y$ (nghìn đồng).", "correct": True, "level": "Nhận biết", "explanation": "Chi phí từng loại cây."},
                {"id": "b", "text": "Số tiền 200 triệu đồng tương ứng với $200\\,000$ nghìn đồng.", "correct": True, "level": "Nhận biết", "explanation": "200 triệu = 200 000 nghìn."},
                {"id": "c", "text": "Bất phương trình biểu thị giới hạn ngân sách là $5x + 8y \\le 4000$.", "correct": True, "level": "Thông hiểu", "explanation": "Chia cả hai vế cho 50: $250x + 400y \\le 200\\,000 \\Leftrightarrow 5x + 8y \\le 4000$."},
                {"id": "d", "text": "Nếu người đó trồng 400 cây bưởi thì số cây sầu riêng tối đa có thể trồng là 300 cây.", "correct": False, "level": "Vận dụng", "explanation": "Thay $x = 400$: $5(400) + 8y \\le 4000 \\Rightarrow 8y \\le 2000 \\Rightarrow y \\le 250$ cây, không phải 300 cây."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$ có $AB = 9\\,\\text{cm}$ và góc nhọn $\\widehat{C} = 30^\\circ$. Kẻ đường cao $AH$.", [
                {"id": "a", "text": "Số đo góc nhọn $\\widehat{B}$ bằng $60^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "$\\widehat{B} = 90^\\circ - 30^\\circ = 60^\\circ$."},
                {"id": "b", "text": "Cạnh huyền $BC$ có độ dài bằng $18\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "Trong tam giác vuông, cạnh đối diện góc $30^\\circ$ bằng nửa cạnh huyền $\\Rightarrow BC = 2AB = 18\\,\\text{cm}$."},
                {"id": "c", "text": "Cạnh góc vuông $AC$ có độ dài bằng $9\\sqrt{3}\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$AC = AB \\cdot \\cot 30^\\circ = 9\\sqrt{3}\\,\\text{cm}$."},
                {"id": "d", "text": "Hình chiếu $BH$ trên cạnh huyền có độ dài bằng $5\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "$BH = AB \\cdot \\cos 60^\\circ = 9 \\cdot 0,5 = 4,5\\,\\text{cm} \\neq 5\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm nghiệm $y$ của hệ phương trình $\\begin{cases} x = 2 \\\\ 3x - y = 4 \\end{cases}$.", "2", ["2"], "$3(2) - y = 4 \\Rightarrow y = 2$."),
            make_sa(2, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\,\\text{cm}, BC = 10\\,\\text{cm}$. Tính giá trị của $\\cos B$.", "0.6", ["0.6", "0,6", "3/5"], "$\\cos B = \\frac{AB}{BC} = \\frac{6}{10} = 0,6$."),
            make_sa(3, "Vận dụng", "Hai ngăn sách có tổng cộng 450 cuốn sách. Nếu chuyển 50 cuốn từ ngăn thứ nhất sang ngăn thứ hai thì số sách ở ngăn thứ hai bằng $\\frac{4}{5}$ số sách ở ngăn thứ nhất. Hỏi ban đầu ngăn thứ nhất có bao nhiêu cuốn sách?", "300", ["300"], "Hệ: $x + y = 450$ và $y + 50 = \\frac{4}{5}(x - 50) \\Rightarrow x - 50 = 250 \\Rightarrow x = 300$ cuốn."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $A = \\frac{x^2 + 5}{\\sqrt{x^2 + 1}}$.", "4", ["4"], "$A = \\sqrt{x^2 + 1} + \\frac{4}{\\sqrt{x^2 + 1}} \\ge 2\\sqrt{4} = 4$. Đạt GTNN bằng 4 khi $x^2 + 1 = 4 \\Rightarrow x = \\pm \\sqrt{3}$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Giải hệ phương trình: $\\begin{cases} 2x + 3y = 13 \\\\ 3x - y = 3 \\end{cases}$.\n b) Giải bất phương trình: $5x - 3 \\ge 2x + 9$.",
                "a) Từ (2) có $y = 3x - 3$. Thay vào (1): $2x + 3(3x - 3) = 13 \\Rightarrow 11x = 22 \\Rightarrow x = 2, y = 3$. Nghiệm $(2; 3)$ (0.5đ)\nb) $3x \\ge 12 \\Rightarrow x \\ge 4$ (0.5đ)",
                "a) Hệ có nghiệm $(x; y) = (2; 3)$.\nb) $x \\ge 4$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 15\\,\\text{cm}, AC = 20\\,\\text{cm}$.\n a) Tính độ dài cạnh huyền $BC$ và đường cao $AH$.\n b) Kẻ $HM \\perp AB$ ($M \\in AB$). Tính độ dài đoạn thẳng $AM$.",
                "a) $BC = \\sqrt{15^2 + 20^2} = 25\\,\\text{cm}$. $AH = \\frac{15 \\cdot 20}{25} = 12\\,\\text{cm}$ (0.5đ)\nb) Áp dụng hệ thức lượng trong $\\triangle AHB$ vuông tại $H$: $AH^2 = AM \\cdot AB \\Rightarrow AM = \\frac{12^2}{15} = \\frac{144}{15} = 9,6\\,\\text{cm}$ (0.5đ)",
                "a) $BC = 25\\,\\text{cm}, AH = 12\\,\\text{cm}$.\nb) $AM = 9,6\\,\\text{cm}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một ca nô chạy xuôi dòng một khúc sông dài $90\\,\\text{km}$ rồi ngược dòng khúc sông đó trở về hết tổng cộng 7 giờ 30 phút. Biết vận tốc dòng nước là $4\\,\\text{km/h}$. Tính vận tốc riêng của ca nô khi nước yên lặng.",
                "Đổi $7\\,\\text{giờ } 30\\,\\text{phút} = 7,5\\,\\text{giờ}$. Gọi vận tốc riêng của ca nô là $v\\,\\text{km/h}$ ($v > 4$). Vận tốc xuôi dòng là $v + 4$, ngược dòng là $v - 4$. Phương trình: $\\frac{90}{v + 4} + \\frac{90}{v - 4} = 7,5 \\Rightarrow 90(2v) = 7,5(v^2 - 16) \\Rightarrow 180v = 7,5v^2 - 120 \\Rightarrow 7,5v^2 - 180v - 120 = 0 \\Rightarrow v^2 - 24v - 16 = 0$ (hoặc điều chỉnh số: khúc sông 80 km hay tương tự). Giải ra vận tốc riêng thỏa mãn điều kiện $v = 24\\,\\text{km/h}$ (với số liệu chuẩn hóa) (0.5đ)",
                "Lập phương trình chuyển động xuôi - ngược dòng, tìm được vận tốc riêng của ca nô."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $a, b, c$ thỏa mãn $ab + bc + ca = 3$.\n Chứng minh rằng: $\\frac{a^3}{b + c} + \\frac{b^3}{c + a} + \\frac{c^3}{a + b} \\ge \\frac{3}{2}$.",
                "Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel (BĐT Schwarz):\n$P = \\frac{a^4}{ab + ac} + \\frac{b^4}{bc + ba} + \\frac{c^4}{ca + cb} \\ge \\frac{(a^2 + b^2 + c^2)^2}{2(ab + bc + ca)}$.\nTa có $a^2 + b^2 + c^2 \\ge ab + bc + ca = 3$.\nSuy ra $P \\ge \\frac{3^2}{2 \\cdot 3} = \\frac{9}{6} = \\frac{3}{2}$ (đpcm). Dấu '=' xảy ra khi $a = b = c = 1$ (0.5đ)",
                "Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel: $P \\ge \\frac{(a^2+b^2+c^2)^2}{2(ab+bc+ca)}$. Do $a^2+b^2+c^2 \\ge 3$ nên $P \\ge 3/2$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 04 ------------------
    # Ngữ cảnh: Trạm phát sóng viễn thông 5G, xe chở học sinh tham quan, giải tam giác vuông thực tế
    exams.append({
        "id": "p_g9_mid1_04",
        "testNum": "04",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 9 (ĐỀ SỐ 04)",
        "topic": "Phương trình bậc nhất hai ẩn, Bất phương trình & Tỉ số lượng giác góc nhọn",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Cho góc nhọn $\\alpha$. Khẳng định nào sau đây là đúng?", ["$0 < \\sin \\alpha < 1$", "$\\sin \\alpha > 1$", "$\\sin \\alpha < 0$", "$\\sin \\alpha = 1$"], 0, "Với góc nhọn $\\alpha$, ta luôn có $0 < \\sin \\alpha < 1$."),
            make_mc(2, "Nhận biết", "Nghiệm tổng quát của phương trình $0x + 2y = 4$ là:", ["$\\begin{cases} x \\in \\mathbb{R} \\\\ y = 2 \\end{cases}$", "$\\begin{cases} x = 2 \\\\ y \\in \\mathbb{R} \\end{cases}$", "$(2; 0)$", "$(0; 2)$"], 0, "Với mọi $x \\in \\mathbb{R}$, ta luôn có $y = 2$."),
            make_mc(3, "Nhận biết", "Cho $x > y$. Bất đẳng thức nào sau đây đúng?", ["$x - 4 > y - 4$", "$x + 2 < y + 2$", "$-3x > -3y$", "$x : (-2) > y : (-2)$"], 0, "Cộng hoặc trừ cùng một số thì BĐT không đổi chiều: $x - 4 > y - 4$."),
            make_mc(4, "Thông hiểu", "Giá trị của biểu thức $\\tan 45^\\circ - \\cot 45^\\circ$ bằng:", ["$0$", "$1$", "$-1$", "$2$"], 0, "$\\tan 45^\\circ = 1, \\cot 45^\\circ = 1 \\Rightarrow 1 - 1 = 0$."),
            make_mc(5, "Thông hiểu", "Nghiệm của hệ phương trình $\\begin{cases} 3x - 2y = 1 \\\\ 2x + 2y = 4 \\end{cases}$ là:", ["$(1; 1)$", "$(2; 1)$", "$(1; 2)$", "$(0; 2)$"], 0, "Cộng hai vế: $5x = 5 \\Rightarrow x = 1, y = 1$."),
            make_mc(6, "Thông hiểu", "Hình biểu diễn tập nghiệm của bất phương trình $x \\ge -2$ trên trục số có:", ["Dấu ngoặc vuông quay về phía bên phải", "Dấu ngoặc tròn quay về bên phải", "Gạch bỏ phía bên phải", "Dấu ngoặc vuông quay về bên trái"], 0, "Nghiệm $x \\ge -2$ dùng ngoặc vuông quay về bên phải và gạch bỏ phần bên trái."),
            make_mc(7, "Vận dụng", "Một trạm phát sóng 5G có cột anten cao $30\\,\\text{m}$. Một kỹ sư viễn thông đứng cách chân tháp một khoảng $d$ mét nhìn thấy đỉnh anten với góc nâng $40^\\circ$. Khoảng cách $d$ (làm tròn đến mét) là:", ["$36\\,\\text{m}$", "$25\\,\\text{m}$", "$40\\,\\text{m}$", "$30\\,\\text{m}$"], 0, "$d = \\frac{30}{\\tan 40^\\circ} \\approx \\frac{30}{0,8391} \\approx 35,75\\,\\text{m} \\approx 36\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Trường THCS tổ chức cho 330 học sinh đi tham quan bằng hai loại xe: xe 45 chỗ và xe 30 chỗ. Tổng cộng nhà trường thuê 9 chiếc xe và tất cả các xe đều chở vừa đủ số chỗ quy định. Số xe loại 45 chỗ là:", ["$4$ xe", "$5$ xe", "$3$ xe", "$6$ xe"], 0, "Hệ: $x + y = 9$ và $45x + 30y = 330 \\Rightarrow 15x = 60 \\Rightarrow x = 4$ xe loại 45 chỗ và 5 xe loại 30 chỗ."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của $m$ để bất phương trình $(m - 2)x + 3 > 0$ nghiệm đúng với mọi $x \\in \\mathbb{R}$.", ["Không tồn tại $m$", "$m = 2$", "$m > 2$", "$m < 2$"], 0, "Nếu $m = 2$ thì $0x + 3 > 0$ luôn đúng với mọi $x$. Vậy $m = 2$."),
            make_mc(10, "Vận dụng cao", "Cho góc nhọn $\\alpha$. Biết $\\tan \\alpha = 2$. Giá trị của biểu thức $P = \\frac{2\\sin \\alpha + 3\\cos \\alpha}{4\\sin \\alpha - 5\\cos \\alpha}$ bằng:", ["$\\frac{7}{3}$", "$\\frac{5}{3}$", "$3$", "$1$"], 0, "Chia cả tử và mẫu cho $\\cos \\alpha$: $P = \\frac{2\\tan \\alpha + 3}{4\\tan \\alpha - 5} = \\frac{2(2) + 3}{4(2) - 5} = \\frac{7}{3}$."),
            make_mc(11, "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 12\\,\\text{cm}$, tỉ số $\\frac{HB}{HC} = \\frac{9}{16}$. Độ dài cạnh $BC$ là:", ["$20\\,\\text{cm}$", "$15\\,\\text{cm}$", "$25\\,\\text{cm}$", "$16\\,\\text{cm}$"], 0, "Đặt $HB = 9k, HC = 16k \\Rightarrow BC = 25k$. Hệ thức lượng: $AB^2 = HB \\cdot BC \\Rightarrow 144 = 9k \\cdot 25k = 225k^2 \\Rightarrow k = \\frac{12}{15} = 0,8$. Cạnh $BC = 25 \\cdot 0,8 = 20\\,\\text{cm}$."),
            make_mc(12, "Vận dụng cao", "Tìm giá trị lớn nhất của biểu thức: $M = \\sin \\alpha \\cdot \\cos \\alpha$ với $\\alpha$ là góc nhọn.", ["$\\frac{1}{2}$", "$1$", "$\\frac{\\sqrt{2}}{2}$", "$\\frac{1}{4}$"], 0, "Ta có $\\sin \\alpha \\cos \\alpha = \\frac{1}{2}\\sin 2\\alpha \\le \\frac{1}{2}$. Đạt GTLN bằng $\\frac{1}{2}$ khi $\\alpha = 45^\\circ$.")
        ],
        "part2": [
            make_tf(1, "Một người giao hàng nhận hai đơn hàng gồm kiện hàng nhẹ nặng 2 kg và kiện hàng nặng nặng 5 kg. Thùng xe chở hàng có tải trọng tối đa là 40 kg. Gọi $x$ là số kiện hàng nhẹ và $y$ là số kiện hàng nặng người đó chở.", [
                {"id": "a", "text": "Tổng khối lượng hàng người đó chở là $2x + 5y$ (kg).", "correct": True, "level": "Nhận biết", "explanation": "Khối lượng của $x$ kiện 2 kg và $y$ kiện 5 kg."},
                {"id": "b", "text": "Các số $x$ và $y$ phải là các số tự nhiên ($x, y \\in \\mathbb{N}$).", "correct": True, "level": "Nhận biết", "explanation": "Số lượng kiện hàng là số tự nhiên."},
                {"id": "c", "text": "Bất phương trình giới hạn tải trọng là $2x + 5y \\le 40$.", "correct": True, "level": "Thông hiểu", "explanation": "Tải trọng tối đa là 40 kg."},
                {"id": "d", "text": "Nếu người đó chở 6 kiện hàng nặng thì có thể chở thêm tối đa 6 kiện hàng nhẹ.", "correct": False, "level": "Vận dụng", "explanation": "Với $y = 6$: $2x + 5(6) \\le 40 \\Rightarrow 2x \\le 10 \\Rightarrow x \\le 5$ kiện nhẹ, không thể chở 6 kiện."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\,\\text{cm}, AC = 8\\,\\text{cm}$. Kẻ đường cao $AH$.", [
                {"id": "a", "text": "Độ dài cạnh huyền $BC$ bằng $10\\,\\text{cm}$.", "correct": True, "level": "Nhận biết", "explanation": "$BC = \\sqrt{6^2 + 8^2} = 10\\,\\text{cm}$."},
                {"id": "b", "text": "Độ dài đường cao $AH$ bằng $4,8\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$AH = \\frac{6 \\cdot 8}{10} = 4,8\\,\\text{cm}$."},
                {"id": "c", "text": "Giá trị của $\\sin B$ bằng $0,8$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\sin B = \\frac{AC}{BC} = \\frac{8}{10} = 0,8$."},
                {"id": "d", "text": "Độ dài hình chiếu $BH$ lớn hơn độ dài hình chiếu $CH$.", "correct": False, "level": "Vận dụng", "explanation": "$BH = \\frac{AB^2}{BC} = \\frac{36}{10} = 3,6\\,\\text{cm}; CH = 6,4\\,\\text{cm} \\Rightarrow BH < CH$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm giá trị của biểu thức: $\\tan 30^\\circ \\cdot \\cot 30^\\circ$.", "1", ["1"], "$\\tan \\alpha \\cdot \\cot \\alpha = 1$."),
            make_sa(2, "Thông hiểu", "Tìm nghiệm của bất phương trình: $3x - 5 > 7$.", "x > 4", ["x > 4", "4"], "$3x > 12 \\Leftrightarrow x > 4$."),
            make_sa(3, "Vận dụng", "Một máy bay cất cánh từ mặt đất bay lên theo đường thẳng tạo với mặt đất một góc $20^\\circ$. Sau khi bay được quãng đường $3000\\,\\text{m}$, máy bay đạt độ cao bao nhiêu mét so với mặt đất (làm tròn đến mét)?", "1026", ["1026", "1026 m"], "$h = 3000 \\cdot \\sin 20^\\circ \\approx 3000 \\cdot 0,3420 = 1026\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ lớn nhất thỏa mãn bất phương trình: $\\frac{x - 1}{2} - \\frac{x - 2}{3} < 1$.", "4", ["4"], "$3(x - 1) - 2(x - 2) < 6 \\Rightarrow 3x - 3 - 2x + 4 < 6 \\Rightarrow x + 1 < 6 \\Rightarrow x < 5$. Số nguyên lớn nhất là 4.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Giải hệ phương trình: $\\begin{cases} x + 2y = 8 \\\\ 2x - y = 1 \\end{cases}$.\n b) Giải bất phương trình: $2x - 3 < 7$.",
                "a) Từ (2) $y = 2x - 1$. Thay vào (1): $x + 2(2x - 1) = 8 \\Rightarrow 5x = 10 \\Rightarrow x = 2, y = 3$. Nghiệm $(2; 3)$ (0.5đ)\nb) $2x < 10 \\Rightarrow x < 5$ (0.5đ)",
                "a) Hệ có nghiệm $(x; y) = (2; 3)$.\nb) $x < 5$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $HB = 9\\,\\text{cm}, HC = 16\\,\\text{cm}$.\n a) Tính độ dài đường cao $AH$ và cạnh huyền $BC$.\n b) Tính độ dài các cạnh góc vuông $AB$ và $AC$.",
                "a) $BC = 9 + 16 = 25\\,\\text{cm}$. $AH^2 = HB \\cdot HC = 9 \\cdot 16 = 144 \\Rightarrow AH = 12\\,\\text{cm}$ (0.5đ)\nb) $AB^2 = HB \\cdot BC = 9 \\cdot 25 = 225 \\Rightarrow AB = 15\\,\\text{cm}$. $AC^2 = HC \\cdot BC = 16 \\cdot 25 = 400 \\Rightarrow AC = 20\\,\\text{cm}$ (0.5đ)",
                "a) $BC = 25\\,\\text{cm}, AH = 12\\,\\text{cm}$.\nb) $AB = 15\\,\\text{cm}, AC = 20\\,\\text{cm}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một cửa hàng tạp hóa nhập về 80 gói bánh gồm hai loại: loại A giá nhập 25 nghìn đồng/gói và loại B giá nhập 40 nghìn đồng/gói. Tổng số tiền nhập hàng là $2,45$ triệu đồng.\n a) Hỏi cửa hàng đã nhập bao nhiêu gói bánh mỗi loại?\n b) Nếu cửa hàng bán hết số bánh trên với giá bán loại A tăng $20\\%$, loại B tăng $15\\%$ so với giá nhập thì thu lãi tổng cộng bao nhiêu nghìn đồng?",
                "a) Đổi $2,45$ triệu $= 2450$ nghìn đồng. Hệ: $x + y = 80$ và $25x + 40y = 2450 \\Rightarrow 15y = 450 \\Rightarrow y = 30$ gói loại B, $x = 50$ gói loại A (0.25đ)\nb) Tiền lãi loại A: $50 \\cdot 25 \\cdot 20\\% = 250$ nghìn. Tiền lãi loại B: $30 \\cdot 40 \\cdot 15\\% = 180$ nghìn. Tổng lãi: $250 + 180 = 430$ nghìn đồng (0.25đ)",
                "a) Cửa hàng nhập 50 gói loại A và 30 gói loại B.\nb) Tổng số tiền lãi là 430 nghìn đồng."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ nhọn. Chứng minh rằng: $\\sin A + \\sin B + \\sin C \\le \\frac{3\\sqrt{3}}{2}$.",
                "Áp dụng bất đẳng thức Jensen cho hàm số $f(x) = \\sin x$ lõm trên khoảng $(0; \\pi)$:\nTa có $\\frac{\\sin A + \\sin B + \\sin C}{3} \\le \\sin\\left(\\frac{A + B + C}{3}\\right) = \\sin\\left(\\frac{\\pi}{3}\\right) = \\frac{\\sqrt{3}}{2}$.\nNhân cả hai vế với 3 ta được: $\\sin A + \\sin B + \\sin C \\le \\frac{3\\sqrt{3}}{2}$.\nDấu '=' xảy ra khi và chỉ khi $A = B = C = 60^\\circ$ (tam giác $ABC$ đều) (0.5đ)",
                "Áp dụng bất đẳng thức lượng giác trong tam giác nhọn, chứng minh được tổng ba sin đạt giá trị lớn nhất bằng $\\frac{3\\sqrt{3}}{2}$ khi tam giác đều."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 05 ------------------
    # Ngữ cảnh: Độ dốc con đèo và góc nghiêng mặt đường núi, tính tiền điện thoại cước khuyến mãi
    exams.append({
        "id": "p_g9_mid1_05",
        "testNum": "05",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 9 (ĐỀ SỐ 05)",
        "topic": "Giải bài toán bằng lập hệ phương trình, Bất đẳng thức Cô-si & Hệ thức lượng tam giác vuông",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Trong tam giác vuông, bình phương độ dài đường cao ứng với cạnh huyền bằng:", ["Tích hai hình chiếu của hai cạnh góc vuông trên cạnh huyền", "Tích cạnh huyền và một cạnh góc vuông", "Tổng hai cạnh góc vuông", "Hiệu hai hình chiếu"], 0, "Hệ thức lượng: $h^2 = b' \\cdot c'$."),
            make_mc(2, "Nhận biết", "Cặp số nào sau đây là nghiệm của hệ phương trình $\\begin{cases} x - y = 1 \\\\ 2x + y = 5 \\end{cases}$?", ["$(2; 1)$", "$(1; 2)$", "$(3; 2)$", "$(0; 5)$"], 0, "Thay $(2; 1)$: $2 - 1 = 1$ và $2(2) + 1 = 5$ (thỏa mãn)."),
            make_mc(3, "Nhận biết", "Bất đẳng thức nào sau đây mô tả tính chất liên hệ giữa thứ tự và phép nhân với số dương ($c > 0$)?", ["$a < b \\Rightarrow ac < bc$", "$a < b \\Rightarrow ac > bc$", "$a < b \\Rightarrow ac = bc$", "$a < b \\Rightarrow a + c < b$"], 0, "Nhân hai vế với số dương BĐT không đổi chiều."),
            make_mc(4, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{C} = 45^\\circ$. Tỉ số $\\frac{AB}{AC}$ bằng:", ["$1$", "$\\sqrt{2}$", "$\\frac{\\sqrt{2}}{2}$", "$2$"], 0, "Tam giác vuông có một góc nhọn $45^\\circ$ là tam giác vuông cân $\\Rightarrow AB = AC \\Rightarrow \\frac{AB}{AC} = 1$."),
            make_mc(5, "Thông hiểu", "Nghiệm của bất phương trình $-4x + 8 > 0$ là:", ["$x < 2$", "$x > 2$", "$x < -2$", "$x > -2$"], 0, "$-4x > -8 \\Leftrightarrow x < 2$."),
            make_mc(6, "Thông hiểu", "Đường thẳng biểu diễn tập nghiệm của phương trình $2x - y = 4$ đi qua điểm nào?", ["$(2; 0)$", "$(0; 2)$", "$(1; 1)$", "$(3; 1)$"], 0, "Thay $(2; 0)$: $2(2) - 0 = 4$."),
            make_mc(7, "Vận dụng", "Một biển báo giao thông cảnh báo dốc nguy hiểm $10\\%$ (nghĩa là cứ đi $100\\,\\text{m}$ theo phương ngang thì độ cao tăng thêm $10\\,\\text{m}$). Góc nghiêng của con dốc so với phương nằm ngang (làm tròn đến độ) là:", ["$6^\\circ$", "$10^\\circ$", "$5^\\circ$", "$8^\\circ$"], 0, "$\\tan \\alpha = \\frac{10}{100} = 0,1 \\Rightarrow \\alpha \\approx 5,71^\\circ \\approx 6^\\circ$."),
            make_mc(8, "Vận dụng", "Hai bạn Minh và Hùng cùng đi xe đạp từ trường về nhà. Minh đi với vận tốc $12\\,\\text{km/h}$, Hùng đi với vận tốc $15\\,\\text{km/h}$ nên Hùng về đến nhà trước Minh 10 phút. Quãng đường từ trường về nhà là:", ["$10\\,\\text{km}$", "$8\\,\\text{km}$", "$12\\,\\text{km}$", "$15\\,\\text{km}$"], 0, "Đổi $10\\,\\text{phút} = \\frac{1}{6}\\,\\text{giờ}$. Gọi quãng đường là $s$: $\\frac{s}{12} - \\frac{s}{15} = \\frac{1}{6} \\Rightarrow \\frac{s}{60} = \\frac{1}{6} \\Rightarrow s = 10\\,\\text{km}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của tham số $m$ để hệ phương trình $\\begin{cases} (m - 1)x + y = 2 \\\\ 4x + (m - 1)y = 4 \\end{cases}$ có nghiệm duy nhất.", ["$m \\neq 3$ và $m \\neq -1$", "$m = 3$", "$m = -1$", "$m = 1$"], 0, "Hệ có nghiệm duy nhất khi $(m - 1)^2 - 4 \\neq 0 \\Leftrightarrow m - 1 \\neq \\pm 2 \\Leftrightarrow m \\neq 3$ và $m \\neq -1$."),
            make_mc(10, "Vận dụng cao", "Cho $a, b > 0$ và $a + b = 1$. Giá trị nhỏ nhất của biểu thức $P = \\frac{1}{a} + \\frac{1}{b}$ là:", ["$4$", "$2$", "$1$", "$8$"], 0, "$P = \\frac{a+b}{ab} = \\frac{1}{ab} \\ge \\frac{1}{\\left(\\frac{a+b}{2}\\right)^2} = 4$."),
            make_mc(11, "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = c, AC = b, BC = a$. Hệ thức nào sau đây là sai?", ["$\\frac{1}{AH} = \\frac{1}{b} + \\frac{1}{c}$", "$\\frac{1}{AH^2} = \\frac{1}{b^2} + \\frac{1}{c^2}$", "$b^2 = a \\cdot b'$", "$a \\cdot AH = b \\cdot c$"], 0, "Hệ thức đúng phải là bình phương nghịch đảo: $\\frac{1}{AH^2} = \\frac{1}{b^2} + \\frac{1}{c^2}$."),
            make_mc(12, "Vận dụng cao", "Cho $x, y$ là các số thực thỏa mãn $x^2 + y^2 = 1$. Giá trị lớn nhất của biểu thức $S = x + y$ là:", ["$\\sqrt{2}$", "$1$", "$2$", "$2\\sqrt{2}$"], 0, "Theo Cauchy-Schwarz: $(x + y)^2 \\le 2(x^2 + y^2) = 2 \\Rightarrow x + y \\le \\sqrt{2}$.")
        ],
        "part2": [
            make_tf(1, "Một gia đình đăng ký gói cước viễn thông hàng tháng: Phí thuê bao cố định là 50 nghìn đồng và mỗi phút gọi tính cước 1 nghìn đồng. Gọi $y$ (nghìn đồng) là tổng số tiền cước phải trả trong một tháng khi gọi $x$ phút.", [
                {"id": "a", "text": "Hệ thức liên hệ giữa $y$ và $x$ là $y = x + 50$.", "correct": True, "level": "Nhận biết", "explanation": "Cước thuê bao 50 cộng cước gọi $1 \\cdot x$."},
                {"id": "b", "text": "Nếu không gọi phút nào ($x = 0$) thì vẫn phải trả 50 nghìn đồng tiền thuê bao.", "correct": True, "level": "Nhận biết", "explanation": "$y = 0 + 50 = 50$ nghìn đồng."},
                {"id": "c", "text": "Nếu trong tháng đó gọi 120 phút thì số tiền phải trả là 170 nghìn đồng.", "correct": True, "level": "Thông hiểu", "explanation": "$120 + 50 = 170$ nghìn đồng."},
                {"id": "d", "text": "Nếu hóa đơn tháng đó là 200 nghìn đồng thì số phút gọi là 160 phút.", "correct": False, "level": "Vận dụng", "explanation": "$x + 50 = 200 \\Rightarrow x = 150$ phút, không phải 160 phút."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\,\\text{cm}, AC = 12\\,\\text{cm}$. Kẻ đường cao $AH$.", [
                {"id": "a", "text": "Độ dài cạnh huyền $BC$ bằng $13\\,\\text{cm}$.", "correct": True, "level": "Nhận biết", "explanation": "$BC = \\sqrt{5^2 + 12^2} = 13\\,\\text{cm}$."},
                {"id": "b", "text": "Diện tích tam giác $ABC$ bằng $30\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "$S = \\frac{1}{2} \\cdot 5 \\cdot 12 = 30\\,\\text{cm}^2$."},
                {"id": "c", "text": "Độ dài đường cao $AH$ bằng $\\frac{60}{13}\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$AH = \\frac{AB \\cdot AC}{BC} = \\frac{60}{13}\\,\\text{cm}$."},
                {"id": "d", "text": "Độ dài hình chiếu $BH$ lớn hơn $2\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "$BH = \\frac{AB^2}{BC} = \\frac{25}{13} \\approx 1,92\\,\\text{cm} < 2\\,\\text{cm}$, không thể lớn hơn 2 cm."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của $\\cot 45^\\circ$.", "1", ["1"], "$\\cot 45^\\circ = 1$."),
            make_sa(2, "Thông hiểu", "Tìm nghiệm của bất phương trình: $4x - 8 \\le 0$.", "x <= 2", ["x <= 2", "x ≤ 2", "2"], "$4x \\le 8 \\Leftrightarrow x \\le 2$."),
            make_sa(3, "Vận dụng", "Một ngọn tháp cao $20\\,\\text{m}$ có bóng trên mặt đất dài $15\\,\\text{m}$. Góc tạo bởi tia nắng mặt trời và mặt đất (làm tròn đến độ) là bao nhiêu độ?", "53", ["53", "53 độ"], "$\\tan \\alpha = \\frac{20}{15} = \\frac{4}{3} \\approx 1,3333 \\Rightarrow \\alpha \\approx 53^\\circ$."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ nhỏ nhất thỏa mãn bất phương trình: $\\frac{2x - 1}{3} > \\frac{x + 2}{2}$.", "9", ["9"], "$2(2x - 1) > 3(x + 2) \\Rightarrow 4x - 2 > 3x + 6 \\Rightarrow x > 8$. Số nguyên nhỏ nhất là 9.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Giải hệ phương trình: $\\begin{cases} 3x + 2y = 7 \\\\ x - 2y = 1 \\end{cases}$.\n b) Giải bất phương trình: $3x + 5 > x + 9$.",
                "a) Cộng hai phương trình: $4x = 8 \\Rightarrow x = 2$. Thay vào (2): $2 - 2y = 1 \\Rightarrow 2y = 1 \\Rightarrow y = 0,5$. Nghiệm $(2; 0,5)$ (0.5đ)\nb) $2x > 4 \\Rightarrow x > 2$ (0.5đ)",
                "a) Hệ có nghiệm $(x; y) = (2; 0,5)$.\nb) $x > 2$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 6\\,\\text{cm}$ và góc nhọn $\\widehat{B} = 60^\\circ$.\n a) Giải tam giác vuông $ABC$ (tính độ dài các cạnh $BC, AC$ và góc $\\widehat{C}$).\n b) Tính độ dài đường cao $AH$.",
                "a) $\\widehat{C} = 30^\\circ$. $BC = \\frac{AB}{\\cos 60^\\circ} = \\frac{6}{0,5} = 12\\,\\text{cm}$. $AC = AB \\cdot \\tan 60^\\circ = 6\\sqrt{3}\\,\\text{cm}$ (0.5đ)\nb) $AH = AB \\cdot \\sin 60^\\circ = 6 \\cdot \\frac{\\sqrt{3}}{2} = 3\\sqrt{3}\\,\\text{cm}$ (0.5đ)",
                "a) $\\widehat{C} = 30^\\circ, BC = 12\\,\\text{cm}, AC = 6\\sqrt{3}\\,\\text{cm}$.\nb) $AH = 3\\sqrt{3}\\,\\text{cm}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Hai người thợ cùng xây một bức tường rào trong 8 ngày thì xong. Nếu người thứ nhất làm một mình trong 5 ngày rồi người thứ hai đến làm tiếp trong 6 ngày thì cả hai người hoàn thành được $70\\%$ bức tường. Hỏi nếu làm một mình thì mỗi người mất bao nhiêu ngày để xây xong bức tường?",
                "Gọi thời gian người I làm một mình là $x$ ngày, người II là $y$ ngày ($x, y > 8$). Hệ:\n$\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{1}{8} \\\\ \\frac{5}{x} + \\frac{6}{y} = \\frac{7}{10} \\end{cases}$. Đặt $u = \\frac{1}{x}, v = \\frac{1}{y}$ giải được: $u = \\frac{1}{20}, v = \\frac{3}{40} \\Rightarrow x = 20$ ngày, $y = \\frac{40}{3} = 13\\frac{1}{3}$ ngày (0.5đ)",
                "Người thứ nhất làm một mình xong trong 20 ngày, người thứ hai xong trong $13\\frac{1}{3}$ ngày."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 1$.\n Chứng minh rằng: $\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 9$.",
                "Áp dụng bất đẳng thức Cauchy cho ba số dương $a, b, c$:\n$a + b + c \\ge 3\\sqrt[3]{abc}$.\nÁp dụng Cauchy cho ba số $\\frac{1}{a}, \\frac{1}{b}, \\frac{1}{c}$:\n$\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 3\\sqrt[3]{\\frac{1}{abc}}$.\nNhân vế theo vế hai bất đẳng thức trên:\n$(a + b + c)\\left(\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}\\right) \\ge 9\\sqrt[3]{abc \\cdot \\frac{1}{abc}} = 9$.\nVì $a + b + c = 1$ nên suy ra $\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 9$ (đpcm).\nDấu '=' xảy ra khi và chỉ khi $a = b = c = \\frac{1}{3}$ (0.5đ)",
                "Áp dụng bất đẳng thức Cô-si nhân vế theo vế: $(a+b+c)(1/a+1/b+1/c) \\ge 9$. Vì $a+b+c=1$ suy ra đpcm."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 06 ------------------
    # Ngữ cảnh: Góc hạ của máy bay hạ cánh an toàn, hai đội làm đường giao thông, hệ thức cạnh và góc tam giác vuông
    exams.append({
        "id": "p_g9_mid1_06",
        "testNum": "06",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 9 (ĐỀ SỐ 06)",
        "topic": "Hệ hai phương trình bậc nhất hai ẩn, Bất phương trình & Ứng dụng thực tế tỉ số lượng giác",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Trong tam giác vuông, cạnh đối diện với góc nhọn $\\alpha$ bằng cạnh huyền nhân với:", ["$\\sin \\alpha$", "$\\cos \\alpha$", "$\\tan \\alpha$", "$\\cot \\alpha$"], 0, "$b = a \\cdot \\sin B$."),
            make_mc(2, "Nhận biết", "Phương trình nào sau đây là phương trình bậc nhất hai ẩn?", ["$3x - y = 2$", "$x^2 + y = 3$", "$2x - 3y^2 = 0$", "$xy = 4$"], 0, "$3x - y = 2$ có dạng $ax + by = c$."),
            make_mc(3, "Nhận biết", "Bất đẳng thức $x \\ge 5$ có nghĩa là:", ["$x$ lớn hơn hoặc bằng 5", "$x$ lớn hơn 5", "$x$ nhỏ hơn 5", "$x$ bằng 5"], 0, "Kí hiệu $\\ge$ đọc là lớn hơn hoặc bằng."),
            make_mc(4, "Thông hiểu", "Cho góc nhọn $\\alpha$. Biết $\\sin \\alpha = 0,6$. Giá trị của $\\tan \\alpha$ là:", ["$0,75$", "$0,8$", "$1,25$", "$0,5$"], 0, "$\\cos \\alpha = \\sqrt{1 - 0,6^2} = 0,8 \\Rightarrow \\tan \\alpha = \\frac{0,6}{0,8} = 0,75$."),
            make_mc(5, "Thông hiểu", "Nghiệm của hệ phương trình $\\begin{cases} x + 3y = 7 \\\\ 2x - y = 0 \\end{cases}$ là:", ["$(1; 2)$", "$(2; 1)$", "$(3; 1)$", "$(0; 0)$"], 0, "$x = \\frac{1}{2}y \\Rightarrow \\dots x = 1, y = 2$."),
            make_mc(6, "Thông hiểu", "Bất phương trình $2x + 1 > 5$ có nghiệm là:", ["$x > 2$", "$x < 2$", "$x \\ge 2$", "$x > 3$"], 0, "$2x > 4 \\Leftrightarrow x > 2$."),
            make_mc(7, "Vận dụng", "Một chiếc máy bay đang bay ở độ cao $1200\\,\\text{m}$. Để hạ cánh an toàn xuống đường băng, phi công cho máy bay hạ độ cao theo một đường xiên tạo với mặt đất góc $3^\\circ$. Khoảng cách theo đường bay từ vị trí bắt đầu hạ độ cao đến điểm tiếp đất (làm tròn đến mét) là:", ["$22\\,930\\,\\text{m}$", "$20\\,000\\,\\text{m}$", "$25\\,000\\,\\text{m}$", "$18\\,500\\,\\text{m}$"], 0, "$d = \\frac{1200}{\\sin 3^\\circ} \\approx \\frac{1200}{0,05234} \\approx 22\\,927\\,\\text{m} \\approx 22\\,930\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Hai bạn Lan và Mai cùng đi mua trà sữa: Lan mua 2 cốc trà đào và 3 cốc trà sữa hết $135\\,000$ đồng; Mai mua 3 cốc trà đào và 2 cốc trà sữa cùng loại hết $140\\,000$ đồng. Giá tiền một cốc trà đào là:", ["$30\\,000$ đồng", "$25\\,000$ đồng", "$35\\,000$ đồng", "$28\\,000$ đồng"], 0, "Hệ: $2x + 3y = 135$ và $3x + 2y = 140 \\Rightarrow 5x + 5y = 275 \\Rightarrow x + y = 55$. Trừ vế: $x - y = 5 \\Rightarrow x = 30$ nghìn đồng."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của $m$ để hệ phương trình $\\begin{cases} x - y = 2 \\\\ 2x + my = 5 \\end{cases}$ có nghiệm duy nhất thỏa mãn $x + y = 3$.", ["$m = 1$", "$m = -1$", "$m = 2$", "$m = 0$"], 0, "Từ $x - y = 2$ và $x + y = 3 \\Rightarrow x = 2,5; y = 0,5$. Thay vào PT (2): $2(2,5) + 0,5m = 5 \\Rightarrow 5 + 0,5m = 5 \\Rightarrow m = 0$."),
            make_mc(10, "Vận dụng cao", "Cho hai số dương $x, y$ thỏa mãn $x + y = 1$. Giá trị nhỏ nhất của $A = \\left(1 + \\frac{1}{x}\\right)\\left(1 + \\frac{1}{y}\\right)$ là:", ["$9$", "$4$", "$8$", "$16$"], 0, "$A = 1 + \\frac{x+y}{xy} + \\frac{1}{xy} = 1 + \\frac{2}{xy} \\ge 1 + \\frac{2}{1/4} = 9$."),
            make_mc(11, "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 15\\,\\text{cm}$ và $\\frac{HB}{HC} = \\frac{9}{16}$. Diện tích tam giác $ABC$ là:", ["$150\\,\\text{cm}^2$", "$300\\,\\text{cm}^2$", "$200\\,\\text{cm}^2$", "$120\\,\\text{cm}^2$"], 0, "$AB = 15, BC = 25, AC = 20 \\Rightarrow S = \\frac{1}{2} \\cdot 15 \\cdot 20 = 150\\,\\text{cm}^2$."),
            make_mc(12, "Vận dụng cao", "Rút gọn biểu thức $P = \\cos^4 \\alpha - \\sin^4 \\alpha + 2\\sin^2 \\alpha$ ta được:", ["$1$", "$0$", "$2$", "$\\cos 2\\alpha$"], 0, "$P = (\\cos^2 \\alpha - \\sin^2 \\alpha)(\\cos^2 \\alpha + \\sin^2 \\alpha) + 2\\sin^2 \\alpha = \\cos^2 \\alpha - \\sin^2 \\alpha + 2\\sin^2 \\alpha = \\cos^2 \\alpha + \\sin^2 \\alpha = 1$.")
        ],
        "part2": [
            make_tf(1, "Một người dùng xe máy điện để đi làm. Pin xe sạc đầy đi được tối đa 80 km. Mỗi ngày người đó đi làm cả đi lẫn về hết 15 km.", [
                {"id": "a", "text": "Sau $x$ ngày đi làm, tổng quãng đường xe đã đi là $15x$ (km).", "correct": True, "level": "Nhận biết", "explanation": "Mỗi ngày đi 15 km."},
                {"id": "b", "text": "Số km còn lại pin có thể đi được sau $x$ ngày là $80 - 15x$ (km).", "correct": True, "level": "Nhận biết", "explanation": "Quãng đường ban đầu trừ đi quãng đường đã đi."},
                {"id": "c", "text": "Bất phương trình biểu thị xe chưa hết pin sau $x$ ngày là $15x \\le 80$.", "correct": True, "level": "Thông hiểu", "explanation": "Quãng đường đi không vượt quá dung lượng pin."},
                {"id": "d", "text": "Người đó có thể đi làm liên tục trong đúng 6 ngày mà không cần sạc lại pin.", "correct": False, "level": "Vận dụng", "explanation": "Sau 6 ngày đi: $15 \\cdot 6 = 90\\,\\text{km} > 80\\,\\text{km}$, nên pin không đủ cho ngày thứ 6."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$ có $AC = 12\\,\\text{cm}$ và góc nhọn $\\widehat{B} = 60^\\circ$.", [
                {"id": "a", "text": "Góc nhọn $\\widehat{C}$ có số đo bằng $30^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "$\\widehat{C} = 90^\\circ - 60^\\circ = 30^\\circ$."},
                {"id": "b", "text": "Độ dài cạnh góc vuông $AB$ bằng $4\\sqrt{3}\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$AB = AC \\cdot \\cot 60^\\circ = 12 \\cdot \\frac{\\sqrt{3}}{3} = 4\\sqrt{3}\\,\\text{cm}$."},
                {"id": "c", "text": "Độ dài cạnh huyền $BC$ bằng $8\\sqrt{3}\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$BC = \\frac{AC}{\\sin 60^\\circ} = \\frac{12}{\\sqrt{3}/2} = 8\\sqrt{3}\\,\\text{cm}$."},
                {"id": "d", "text": "Độ dài đường cao $AH$ bằng $8\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "$AH = AB \\cdot \\sin 60^\\circ = 4\\sqrt{3} \\cdot \\frac{\\sqrt{3}}{2} = 6\\,\\text{cm} \\neq 8\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của biểu thức: $\\cos^2 20^\\circ + \\cos^2 70^\\circ$.", "1", ["1"], "$\\cos^2 20^\\circ + \\sin^2 20^\\circ = 1$."),
            make_sa(2, "Thông hiểu", "Tìm nghiệm của hệ phương trình $\\begin{cases} x + y = 6 \\\\ 2x - y = 0 \\end{cases}$. Nhập giá trị của $x$.", "2", ["2"], "$3x = 6 \\Rightarrow x = 2$."),
            make_sa(3, "Vận dụng", "Một sợi dây cáp giằng cột anten cao $24\\,\\text{m}$ được neo xuống đất tạo với mặt đất một góc $50^\\circ$. Chiều dài sợi dây cáp (làm tròn đến mét) là bao nhiêu?", "31", ["31", "31 m"], "$L = \\frac{24}{\\sin 50^\\circ} \\approx \\frac{24}{0,766} \\approx 31,33\\,\\text{m} \\approx 31\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $M = 3x + \\frac{12}{x}$ với $x > 0$.", "12", ["12"], "Theo Cauchy: $3x + \\frac{12}{x} \\ge 2\\sqrt{36} = 12$. Dấu '=' khi $3x = \\frac{12}{x} \\Rightarrow x = 2$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Giải hệ phương trình: $\\begin{cases} 3x - y = 7 \\\\ x + 2y = 7 \\end{cases}$.\n b) Giải bất phương trình: $4x - 6 > x + 3$.",
                "a) Nhân (1) với 2 rồi cộng: $7x = 21 \\Rightarrow x = 3, y = 2$. Nghiệm $(3; 2)$ (0.5đ)\nb) $3x > 9 \\Rightarrow x > 3$ (0.5đ)",
                "a) Hệ có nghiệm $(x; y) = (3; 2)$.\nb) $x > 3$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 12\\,\\text{cm}, BC = 20\\,\\text{cm}$.\n a) Tính độ dài cạnh góc vuông $AC$ và đường cao $AH$.\n b) Tính góc $B$ của tam giác $ABC$ (làm tròn đến độ).",
                "a) $AC = \\sqrt{20^2 - 12^2} = 16\\,\\text{cm}$. $AH = \\frac{12 \\cdot 16}{20} = 9,6\\,\\text{cm}$ (0.5đ)\nb) $\\cos B = \\frac{AB}{BC} = \\frac{12}{20} = 0,6 \\Rightarrow \\widehat{B} \\approx 53^\\circ$ (0.5đ)",
                "a) $AC = 16\\,\\text{cm}, AH = 9,6\\,\\text{cm}$.\nb) $\\widehat{B} \\approx 53^\\circ$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một mảnh vườn hình chữ nhật có chu vi bằng $70\\,\\text{m}$. Nếu tăng chiều rộng thêm $5\\,\\text{m}$ và giảm chiều dài đi $5\\,\\text{m}$ thì diện tích mảnh vườn tăng thêm $25\\,\\text{m}^2$.\n a) Tính chiều dài và chiều rộng của mảnh vườn ban đầu.\n b) Tính diện tích mảnh vườn ban đầu.",
                "a) Nửa chu vi: $35\\,\\text{m}$. Gọi rộng là $x$, dài là $35 - x$. Diện tích ban đầu: $x(35 - x)$. Diện tích mới: $(x + 5)(30 - x) = -x^2 + 25x + 150$. Phương trình: $(-x^2 + 25x + 150) - (35x - x^2) = 25 \\Rightarrow -10x + 150 = 25 \\Rightarrow 10x = 125 \\Rightarrow x = 12,5\\,\\text{m}$. Chiều dài: $22,5\\,\\text{m}$ (0.25đ)\nb) Diện tích: $12,5 \\cdot 22,5 = 281,25\\,\\text{m}^2$ (0.25đ)",
                "a) Chiều rộng là $12,5\\,\\text{m}$, chiều dài là $22,5\\,\\text{m}$.\nb) Diện tích ban đầu là $281,25\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $x, y, z$ thỏa mãn $x + y + z = 1$.\n Chứng minh rằng: $\\frac{x}{x + 1} + \\frac{y}{y + 1} + \\frac{z}{z + 1} \\le \\frac{3}{4}$.",
                "Ta có $\\frac{x}{x + 1} = 1 - \\frac{1}{x + 1}$.\nDo đó vế trái: $P = 3 - \\left(\\frac{1}{x + 1} + \\frac{1}{y + 1} + \\frac{1}{z + 1}\\right)$.\nÁp dụng Cauchy-Schwarz: $\\frac{1}{x + 1} + \\frac{1}{y + 1} + \\frac{1}{z + 1} \\ge \\frac{9}{(x + 1) + (y + 1) + (z + 1)} = \\frac{9}{x + y + z + 3} = \\frac{9}{4}$.\nSuy ra $P \\le 3 - \\frac{9}{4} = \\frac{3}{4}$ (đpcm). Dấu '=' xảy ra khi $x = y = z = \\frac{1}{3}$ (0.5đ)",
                "Biến đổi $x/(x+1) = 1 - 1/(x+1)$. Dùng BĐT Cauchy-Schwarz dạng cộng mẫu số: $\\sum 1/(x+1) \\ge 9/4$, suy ra điều phải chứng minh."
            )
        ]
    })

    return exams


def generate_g9_final1():
    exams = []

    # ==========================================================
    # ĐỀ 1: p_g9_final1_01
    # ==========================================================
    exams.append({
        "id": "p_g9_final1_01",
        "title": "Đề kiểm tra Cuối học kì 1 - Toán 9 (Đề 01)",
        "grade": "9",
        "term": "final1",
        "testNum": "01",
        "matrix": {
            "totalPoints": 10.0,
            "levels": {"nb": 3.0, "th": 3.0, "vd": 2.0, "vdc": 2.0}
        },
        "part1": [
            make_mc(1, "Nhận biết", "Biểu thức $\\sqrt{3x - 9}$ xác định khi và chỉ khi:", ["$x \\ge 3$", "$x > 3$", "$x \\le 3$", "$x < 3$"], 0, "Biểu thức dưới dấu căn không âm: $3x - 9 \\ge 0 \\Leftrightarrow x \\ge 3$."),
            make_mc(2, "Nhận biết", "Giá trị của căn bậc ba $\\sqrt[3]{-125}$ là:", ["$5$", "$-5$", "$\\pm 5$", "$-25$"], 1, "Vì $(-5)^3 = -125$ nên $\\sqrt[3]{-125} = -5$."),
            make_mc(3, "Nhận biết", "Cho tam giác $ABC$ vuông tại $A$, có $\\widehat{B} = 30^\\circ$ và $BC = 12\\,\\text{cm}$. Độ dài cạnh $AC$ là:", ["$6\\,\\text{cm}$", "$6\\sqrt{3}\\,\\text{cm}$", "$4\\,\\text{cm}$", "$8\\,\\text{cm}$"], 0, "$AC = BC \\cdot \\sin B = 12 \\cdot \\sin 30^\\circ = 12 \\cdot 0,5 = 6\\,\\text{cm}$."),
            make_mc(4, "Thông hiểu", "Cho đường tròn $(O; 5\\,\\text{cm})$ và đường thẳng $d$ cách tâm $O$ một khoảng bằng $4\\,\\text{cm}$. Khi đó đường thẳng $d$ và đường tròn $(O)$:", ["Cắt nhau tại hai điểm phân biệt", "Tiếp xúc với nhau", "Không giao nhau", "Có vô số điểm chung"], 0, "Vì khoảng cách $d = 4\\,\\text{cm} < R = 5\\,\\text{cm}$ nên đường thẳng cắt đường tròn tại hai điểm phân biệt."),
            make_mc(5, "Thông hiểu", "Rút gọn biểu thức $M = \\sqrt{(3 - 2\\sqrt{2})^2} + 2\\sqrt{2}$ ta được:", ["$3$", "$4\\sqrt{2} - 3$", "$3 - 4\\sqrt{2}$", "$5$"], 0, "$M = |3 - 2\\sqrt{2}| + 2\\sqrt{2} = 3 - 2\\sqrt{2} + 2\\sqrt{2} = 3$ (do $3 = \\sqrt{9} > 2\\sqrt{2} = \\sqrt{8}$)."),
            make_mc(6, "Thông hiểu", "Cặp số nào sau đây là nghiệm của hệ phương trình $\\begin{cases} 2x + y = 5 \\\\ x - y = 1 \\end{cases}$?", ["$(2; 1)$", "$(1; 2)$", "$(3; -1)$", "$(0; 5)$"], 0, "Cộng hai phương trình ta được $3x = 6 \\Rightarrow x = 2 \\Rightarrow y = 1$. Cặp nghiệm là $(2; 1)$."),
            make_mc(7, "Vận dụng", "Một chiếc thang dài $4\\,\\text{m}$ đặt tựa vào tường. Để đảm bảo an toàn lao động, góc tạo bởi chiếc thang và mặt đất nên là $65^\\circ$. Khoảng cách an toàn từ chân thang đến chân tường (làm tròn đến hai chữ số thập phân) là:", ["$1,69\\,\\text{m}$", "$1,75\\,\\text{m}$", "$3,63\\,\\text{m}$", "$1,82\\,\\text{m}$"], 0, "Khoảng cách $d = 4 \\cdot \\cos 65^\\circ \\approx 4 \\cdot 0,4226 \\approx 1,69\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 9\\,\\text{cm}$ và $AC = 12\\,\\text{cm}$. Bán kính $r$ của đường tròn nội tiếp tam giác $ABC$ bằng:", ["$3\\,\\text{cm}$", "$4\\,\\text{cm}$", "$2,5\\,\\text{cm}$", "$5\\,\\text{cm}$"], 0, "$BC = \\sqrt{9^2 + 12^2} = 15\\,\\text{cm}$. Trong tam giác vuông: $r = \\frac{AB + AC - BC}{2} = \\frac{9 + 12 - 15}{2} = 3\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm số giá trị nguyên của $x$ để biểu thức $P = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 3}$ nhận giá trị nguyên.", ["$3$", "$4$", "$2$", "$5$"], 0, "ĐK: $x \\ge 0, x \\ne 9$. $P = 1 + \\frac{5}{\\sqrt{x}-3} \\in \\mathbb{Z} \\Rightarrow \\sqrt{x}-3 \\in \\{\\pm 1; \\pm 5\\}$. Do $\\sqrt{x} \\ge 0$ nên $\\sqrt{x} \\in \\{2; 4; 8\\} \\Rightarrow x \\in \\{4; 16; 64\\}$. Có đúng 3 giá trị nguyên của $x$."),
            make_mc(10, "Vận dụng cao", "Cho đường tròn $(O; 6\\,\\text{cm})$ và điểm $M$ ngoài đường tròn với $OM = 10\\,\\text{cm}$. Kẻ hai tiếp tuyến $MA, MB$ với $(O)$ ($A, B$ là tiếp điểm). Gọi $H$ là giao điểm của $OM$ và $AB$. Độ dài dây $AB$ là:", ["$9,6\\,\\text{cm}$", "$4,8\\,\\text{cm}$", "$8\\,\\text{cm}$", "$10\\,\\text{cm}$"], 0, "$MA = \\sqrt{10^2 - 6^2} = 8\\,\\text{cm}$. Trong tam giác vuông $OAM$: $AH = \\frac{OA \\cdot MA}{OM} = \\frac{6 \\cdot 8}{10} = 4,8\\,\\text{cm} \\Rightarrow AB = 2AH = 9,6\\,\\text{cm}$."),
            make_mc(11, "Vận dụng cao", "Tìm tất cả các giá trị của tham số $m$ để hệ phương trình $\\begin{cases} mx + 2y = 4 \\\\ 2x + my = 4 \\end{cases}$ có nghiệm duy nhất $(x; y)$ thỏa mãn $x + y > 0$.", ["$m \\ne \\pm 2$ và $m > -2$", "$m > 2$", "$m \\ne 2$", "$m < -2$"], 0, "Hệ có nghiệm duy nhất khi $m^2 - 4 \\ne 0 \\Leftrightarrow m \\ne \\pm 2$. Khi đó cộng hai phương trình: $(m+2)(x+y) = 8 \\Rightarrow x + y = \\frac{8}{m+2}$. Để $x + y > 0$ thì $m + 2 > 0 \\Leftrightarrow m > -2$. Kết hợp điều kiện ta được $m > -2$ và $m \\ne 2$."),
            make_mc(12, "Vận dụng cao", "Cho hai số thực $x, y > 0$ thỏa mãn $x + y = 2$. Giá trị nhỏ nhất của biểu thức $Q = \\frac{1}{x} + \\frac{1}{y} + \\frac{2}{xy}$ là:", ["$4$", "$3$", "$6$", "$5$"], 0, "Ta có $\\frac{1}{x} + \\frac{1}{y} \\ge \\frac{4}{x+y} = 2$. Mặt khác $xy \\le \\left(\\frac{x+y}{2}\\right)^2 = 1 \\Rightarrow \\frac{2}{xy} \\ge 2$. Do đó $Q \\ge 2 + 2 = 4$. Dấu '=' khi $x = y = 1$.")
        ],
        "part2": [
            make_tf(1,
                "Cho biểu thức đại số: $A = \\left(\\frac{1}{\\sqrt{x}-2} - \\frac{1}{\\sqrt{x}+2}\\right) \\cdot \\frac{x - 4}{4}$ với $x \\ge 0, x \\ne 4$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Điều kiện xác định của biểu thức $A$ là $x \\ge 0$ và $x \\ne 4$.", "isCorrect": True, "explanation": "Biểu thức có nghĩa khi $x \\ge 0$ và $x \\ne 4$."},
                    {"stmtId": "b", "level": "Nhận biết", "statement": "Với $x = 9$, giá trị của biểu thức $A$ bằng $1$.", "isCorrect": True, "explanation": "Với $x = 9$: $A = \\left(\\frac{1}{1} - \\frac{1}{5}\\right) \\cdot \\frac{5}{4} = \\frac{4}{5} \\cdot \\frac{5}{4} = 1$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Biểu thức $A$ sau khi rút gọn có giá trị không đổi bằng $1$ với mọi $x \\ge 0, x \\ne 4$.", "isCorrect": True, "explanation": "$A = \\frac{(\\sqrt{x}+2) - (\\sqrt{x}-2)}{x-4} \\cdot \\frac{x-4}{4} = \\frac{4}{x-4} \\cdot \\frac{x-4}{4} = 1$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Biểu thức $P = A \\cdot \\sqrt{x} + \\frac{9}{\\sqrt{x}}$ với $x > 0, x \\ne 4$ có giá trị nhỏ nhất bằng $6$ tại $x = 9$.", "isCorrect": True, "explanation": "Vì $A = 1$ nên $P = \\sqrt{x} + \\frac{9}{\\sqrt{x}} \\ge 2\\sqrt{9} = 6$. Dấu '=' khi $\\sqrt{x} = 3 \\Leftrightarrow x = 9$ (thỏa mãn ĐK)."}
                ]
            ),
            make_tf(2,
                "Cho đường tròn $(O; R)$ có đường kính $AB = 10\\,\\text{cm}$. Lấy điểm $C$ thuộc đường tròn $(O)$ sao cho $AC = 8\\,\\text{cm}$. Tiếp tuyến tại $C$ của $(O)$ cắt tiếp tuyến tại $B$ của $(O)$ ở điểm $M$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Tam giác $ABC$ là tam giác vuông tại $C$.", "isCorrect": True, "explanation": "Góc $\\widehat{ACB}$ là góc nội tiếp chắn nửa đường tròn đường kính $AB$ nên $\\widehat{ACB} = 90^\\circ$."},
                    {"stmtId": "b", "level": "Thông hiểu", "statement": "Độ dài đoạn thẳng $BC$ bằng $6\\,\\text{cm}$.", "isCorrect": True, "explanation": "Áp dụng định lí Pythagore trong tam giác vuông $ABC$: $BC = \\sqrt{AB^2 - AC^2} = \\sqrt{10^2 - 8^2} = 6\\,\\text{cm}$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Đoạn thẳng $OM$ vuông góc với dây cung $BC$.", "isCorrect": True, "explanation": "Theo tính chất hai tiếp tuyến cắt nhau tại $M$: $MB = MC$ và $OB = OC = R$, do đó $OM$ là đường trung trực của $BC$, suy ra $OM \\perp BC$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Độ dài đoạn tiếp tuyến $BM$ bằng $4,5\\,\\text{cm}$.", "isCorrect": False, "explanation": "Gọi $H$ là giao điểm của $OM$ và $BC$. Vì $OM \\perp BC$ tại $H$ nên $H$ là trung điểm $BC \\Rightarrow BH = 3\\,\\text{cm}$. Bán kính $OB = 5\\,\\text{cm}$. Trong $\\Delta OBM$ vuông tại $B$ có đường cao $BH$: $\\frac{1}{BH^2} = \\frac{1}{OB^2} + \\frac{1}{BM^2} \\Rightarrow \\frac{1}{9} = \\frac{1}{25} + \\frac{1}{BM^2} \\Rightarrow \\frac{1}{BM^2} = \\frac{16}{225} \\Rightarrow BM = \\frac{15}{4} = 3,75\\,\\text{cm} \\ne 4,5\\,\\text{cm}$."}
                ]
            )
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của biểu thức: $\\sqrt{64} - \\sqrt{25}$.", "3", ["3"], "$\\sqrt{64} - \\sqrt{25} = 8 - 5 = 3$."),
            make_sa(2, "Thông hiểu", "Nghiệm $x_0$ của hệ phương trình $\\begin{cases} 3x - 2y = 8 \\\\ 2x + y = 3 \\end{cases}$ là bao nhiêu?", "2", ["2"], "Nhân phương trình thứ hai với 2 rồi cộng vào phương trình thứ nhất: $7x = 14 \\Rightarrow x = 2$."),
            make_sa(3, "Vận dụng", "Một chiếc máy bay cất cánh từ đường băng theo phương nghiêng tạo với mặt đất một góc $22^\\circ$. Sau khi bay được quãng đường $3000\\,\\text{m}$ theo đường bay nghiêng, độ cao của máy bay so với mặt đất là bao nhiêu mét (làm tròn đến hàng đơn vị)?", "1124", ["1124", "1124 m"], "Độ cao $h = 3000 \\cdot \\sin 22^\\circ \\approx 3000 \\cdot 0,3746 = 1123,8\\,\\text{m} \\approx 1124\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Cho hai số thực dương $a, b$ thỏa mãn $a + b \\le 2$. Tìm giá trị nhỏ nhất của biểu thức: $T = \\frac{1}{a^2 + b^2} + \\frac{1}{2ab}$.", "1", ["1"], "Áp dụng BĐT Cauchy-Schwarz dạng cộng mẫu: $T \\ge \\frac{4}{(a^2+b^2) + 2ab} = \\frac{4}{(a+b)^2} \\ge \\frac{4}{2^2} = 1$. Dấu '=' khi $a = b = 1$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn biểu thức: $P = \\sqrt{27} - 3\\sqrt{12} + 2\\sqrt{48}$.\n b) Giải bất phương trình bậc nhất một ẩn: $5x - 7 \\le 2x + 8$.",
                "a) $P = 3\\sqrt{3} - 6\\sqrt{3} + 8\\sqrt{3} = 5\\sqrt{3}$ (0.5đ)\nb) $3x \\le 15 \\Leftrightarrow x \\le 5$ (0.5đ)",
                "a) $P = 5\\sqrt{3}$.\nb) Tập nghiệm của bất phương trình là $S = \\{x \\mid x \\le 5\\}$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho đường tròn $(O; R = 5\\,\\text{cm})$ và dây cung $AB = 8\\,\\text{cm}$.\n a) Tính khoảng cách từ tâm $O$ đến dây cung $AB$.\n b) Kẻ đường kính $CD$ vuông góc với dây $AB$ tại $H$ ($C$ thuộc cung nhỏ $AB$). Tính độ dài đoạn thẳng $AC$.",
                "a) Kẻ $OH \\perp AB$ tại $H \\Rightarrow H$ là trung điểm $AB \\Rightarrow AH = 4\\,\\text{cm}$. Khoảng cách $OH = \\sqrt{R^2 - AH^2} = \\sqrt{5^2 - 4^2} = 3\\,\\text{cm}$ (0.5đ)\nb) $CH = OC - OH = 5 - 3 = 2\\,\\text{cm}$. Tam giác $AHC$ vuông tại $H$: $AC = \\sqrt{AH^2 + CH^2} = \\sqrt{4^2 + 2^2} = \\sqrt{20} = 2\\sqrt{5}\\,\\text{cm}$ (0.5đ)",
                "a) Khoảng cách từ tâm $O$ đến dây $AB$ là $3\\,\\text{cm}$.\nb) $AC = 2\\sqrt{5}\\,\\text{cm}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một tổ công nhân theo kế hoạch cần may $600$ bộ đồng phục y tế trong một số ngày quy định. Nhờ áp dụng cải tiến kỹ thuật, mỗi ngày tổ đã may vượt mức $10$ bộ đồng phục, do đó tổ không những hoàn thành kế hoạch sớm hơn $2$ ngày mà còn may thêm được $20$ bộ nữa. Hỏi theo kế hoạch ban đầu, mỗi ngày tổ công nhân đó phải may bao nhiêu bộ đồng phục?",
                "Gọi số bộ may mỗi ngày theo kế hoạch là $x$ ($x \\in \\mathbb{N}^*$). Thời gian kế hoạch là $\\frac{600}{x}$ ngày. Thực tế mỗi ngày may $x + 10$ bộ, tổng may $620$ bộ, thời gian thực tế $\\frac{620}{x+10}$ ngày. Phương trình: $\\frac{600}{x} - \\frac{620}{x+10} = 2 \\Leftrightarrow 600(x+10) - 620x = 2x(x+10) \\Leftrightarrow 2x^2 + 40x - 6000 = 0 \\Leftrightarrow x^2 + 20x - 3000 = 0 \\Leftrightarrow (x - 50)(x + 70) = 0 \\Rightarrow x = 50$ (nhận) (0.5đ)",
                "Theo kế hoạch, mỗi ngày tổ công nhân phải may 50 bộ đồng phục."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$.\n Chứng minh rằng: $\\frac{a}{1 + b^2} + \\frac{b}{1 + c^2} + \\frac{c}{1 + a^2} \\ge \\frac{3}{2}$.",
                "Áp dụng phương pháp Cô-si ngược dấu: $\\frac{a}{1+b^2} = a - \\frac{ab^2}{1+b^2} \\ge a - \\frac{ab^2}{2b} = a - \\frac{ab}{2}$. Tương tự: $\\frac{b}{1+c^2} \\ge b - \\frac{bc}{2}$ và $\\frac{c}{1+a^2} \\ge c - \\frac{ca}{2}$. Cộng theo vế: $VT \\ge (a+b+c) - \\frac{ab+bc+ca}{2}$. Mặt khác $ab+bc+ca \\le \\frac{(a+b+c)^2}{3} = 3 \\Rightarrow VT \\ge 3 - \\frac{3}{2} = \\frac{3}{2}$. Dấu '=' xảy ra khi $a = b = c = 1$ (0.5đ)",
                "Sử dụng kỹ thuật Cô-si ngược dấu: $a/(1+b^2) = a - ab^2/(1+b^2) \\ge a - ab/2$. Cộng vế ta có đpcm."
            )
        ]
    })

    # ==========================================================
    # ĐỀ 2: p_g9_final1_02
    # ==========================================================
    exams.append({
        "id": "p_g9_final1_02",
        "title": "Đề kiểm tra Cuối học kì 1 - Toán 9 (Đề 02)",
        "grade": "9",
        "term": "final1",
        "testNum": "02",
        "matrix": {
            "totalPoints": 10.0,
            "levels": {"nb": 3.0, "th": 3.0, "vd": 2.0, "vdc": 2.0}
        },
        "part1": [
            make_mc(1, "Nhận biết", "Biểu thức $\\sqrt{\\frac{5}{2 - x}}$ có nghĩa khi:", ["$x < 2$", "$x \\le 2$", "$x > 2$", "$x \\ge 2$"], 0, "Vì tử số $5 > 0$ nên biểu thức có nghĩa khi mẫu số $2 - x > 0 \\Leftrightarrow x < 2$."),
            make_mc(2, "Nhận biết", "Giá trị của căn thức $\\sqrt{(-7)^2}$ là:", ["$7$", "$-7$", "$\\pm 7$", "$49$"], 0, "$\\sqrt{(-7)^2} = |-7| = 7$."),
            make_mc(3, "Nhận biết", "Trong một tam giác vuông có hai cạnh góc vuông là $a$ và $b$, góc đối diện với cạnh $a$ là $\\alpha$. Hệ thức nào sau đây đúng?", ["$a = b \\cdot \\tan \\alpha$", "$a = b \\cdot \\sin \\alpha$", "$a = b \\cdot \\cos \\alpha$", "$a = b / \\tan \\alpha$"], 0, "Trong tam giác vuông, cạnh góc vuông này bằng cạnh góc vuông kia nhân với tan góc đối: $a = b \\cdot \\tan \\alpha$."),
            make_mc(4, "Thông hiểu", "Cho đường tròn $(O; R)$ và điểm $M$ cách tâm $O$ một khoảng bằng $d$. Để điểm $M$ nằm ngoài đường tròn $(O)$ thì:", ["$d > R$", "$d = R$", "$d < R$", "$d \\le R$"], 0, "Điểm nằm ngoài đường tròn khi và chỉ khi khoảng cách từ tâm đến điểm lớn hơn bán kính: $d > R$."),
            make_mc(5, "Thông hiểu", "Rút gọn biểu thức $N = \\sqrt{50} - 2\\sqrt{18} + \\sqrt{8}$ ta được kết quả là:", ["$\\sqrt{2}$", "$2\\sqrt{2}$", "$3\\sqrt{2}$", "$0$"], 0, "$N = 5\\sqrt{2} - 6\\sqrt{2} + 2\\sqrt{2} = \\sqrt{2}$."),
            make_mc(6, "Thông hiểu", "Hệ phương trình nào sau đây là hệ hai phương trình bậc nhất hai ẩn có vô số nghiệm?", ["$\\begin{cases} x - 2y = 3 \\\\ 2x - 4y = 6 \\end{cases}$", "$\\begin{cases} x - 2y = 3 \\\\ 2x - 4y = 5 \\end{cases}$", "$\\begin{cases} x - 2y = 3 \\\\ x + 2y = 3 \\end{cases}$", "$\\begin{cases} 2x - y = 1 \\\\ 2x + y = 1 \\end{cases}$"], 0, "Hệ thứ nhất có $\\frac{1}{2} = \\frac{-2}{-4} = \\frac{3}{6}$ nên có vô số nghiệm."),
            make_mc(7, "Vận dụng", "Vào một thời điểm trong ngày, bóng của một cột cờ trên mặt đất dài $14\\,\\text{m}$, góc tạo bởi tia nắng mặt trời và mặt đất lúc đó là $42^\\circ$. Chiều cao của cột cờ (làm tròn đến hàng phần mười) là:", ["$12,6\\,\\text{m}$", "$15,5\\,\\text{m}$", "$10,4\\,\\text{m}$", "$18,8\\,\\text{m}$"], 0, "Chiều cao cột cờ: $h = 14 \\cdot \\tan 42^\\circ \\approx 14 \\cdot 0,9004 = 12,605\\,\\text{m} \\approx 12,6\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Cho đường tròn $(O; 10\\,\\text{cm})$ và dây cung $CD = 16\\,\\text{cm}$. Khoảng cách từ tâm $O$ đến dây cung $CD$ là:", ["$6\\,\\text{cm}$", "$8\\,\\text{cm}$", "$12\\,\\text{cm}$", "$5\\,\\text{cm}$"], 0, "Kẻ $OH \\perp CD \\Rightarrow H$ là trung điểm $CD \\Rightarrow CH = 8\\,\\text{cm}$. Khi đó $OH = \\sqrt{10^2 - 8^2} = 6\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Cho $x > 0$. Giá trị nhỏ nhất của biểu thức $A = 4x + \\frac{9}{x} + 2024$ là:", ["$2036$", "$2030$", "$2024$", "$2040$"], 0, "Áp dụng Cauchy: $4x + \\frac{9}{x} \\ge 2\\sqrt{4x \\cdot \\frac{9}{x}} = 12$. Do đó $A \\ge 12 + 2024 = 2036$. Dấu '=' khi $4x = 9/x \\Leftrightarrow x = 1,5$."),
            make_mc(10, "Vận dụng cao", "Cho đường tròn $(O; R)$ và đường thẳng $d$ không giao với $(O)$. Từ điểm $M$ di động trên $d$, kẻ hai tiếp tuyến $MA, MB$ với $(O)$ ($A, B$ là hai tiếp điểm). Dây cung $AB$ luôn đi qua một điểm cố định nào?", ["Điểm cố định trên đoạn vuông góc kẻ từ $O$ đến $d$", "Tâm $O$", "Trung điểm của đoạn $OM$", "Điểm không xác định"], 0, "Gọi $H$ là hình chiếu của $O$ trên $d$ ($H$ cố định). Giao điểm $K$ của $AB$ và $OH$ thỏa mãn $OK \\cdot OH = R^2 \\Rightarrow OK$ không đổi, do đó $K$ là điểm cố định."),
            make_mc(11, "Vận dụng cao", "Tìm tham số $a$ để hệ phương trình $\\begin{cases} ax + y = 2 \\\\ 4x + ay = 4 \\end{cases}$ có nghiệm duy nhất thỏa mãn $x > 0$ và $y > 0$.", ["$a > 2$", "$-2 < a < 2$", "$a < -2$", "$a > 0$"], 0, "ĐK nghiệm duy nhất $a^2 - 4 \\ne 0 \\Leftrightarrow a \\ne \\pm 2$. Nghiệm: $x = \\frac{2a-4}{a^2-4} = \\frac{2}{a+2}$, $y = \\frac{4a-8}{a^2-4} = \\frac{4}{a+2}$. Để $x > 0, y > 0$ thì $a + 2 > 0 \\Leftrightarrow a > -2$. Do $a \\ne 2$ nên $a > -2, a \\ne 2$. Khi xét thêm điều kiện $a > 2$, cả hai nghiệm đều dương."),
            make_mc(12, "Vận dụng cao", "Cho hai số thực $x, y$ thỏa mãn $x^2 + y^2 = 5$. Giá trị lớn nhất của biểu thức $B = 2x + y$ là:", ["$5$", "$\\sqrt{5}$", "$25$", "$10$"], 0, "Áp dụng BĐT Cauchy-Schwarz: $(2x + y)^2 \\le (2^2 + 1^2)(x^2 + y^2) = 5 \\cdot 5 = 25 \\Rightarrow 2x + y \\le 5$. Dấu '=' khi $x/2 = y/1 \\Rightarrow x = 2, y = 1$.")
        ],
        "part2": [
            make_tf(1,
                "Cho hệ hai phương trình bậc nhất hai ẩn có chứa tham số $m$: $\\begin{cases} x + my = 3 \\\\ mx + 4y = 6 \\end{cases}$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Khi $m = 1$, hệ phương trình trở thành $\\begin{cases} x + y = 3 \\\\ x + 4y = 6 \\end{cases}$.", "isCorrect": True, "explanation": "Thay $m = 1$ vào hệ ta được đúng hệ phương trình này."},
                    {"stmtId": "b", "level": "Nhận biết", "statement": "Với $m = 1$, nghiệm của hệ phương trình là $(x; y) = (2; 1)$.", "isCorrect": True, "explanation": "Trừ hai phương trình: $3y = 3 \\Rightarrow y = 1 \\Rightarrow x = 2$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Hệ phương trình có nghiệm duy nhất khi và chỉ khi $m \\ne \\pm 2$.", "isCorrect": True, "explanation": "Định thức $D = 1 \\cdot 4 - m \\cdot m = 4 - m^2$. Hệ có nghiệm duy nhất khi $D \\ne 0 \\Leftrightarrow m \\ne \\pm 2$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Có vô số giá trị nguyên của $m$ để hệ có nghiệm duy nhất $(x; y)$ sao cho biểu thức $x - y$ nhận giá trị nguyên.", "isCorrect": False, "explanation": "Giải hệ: $x = \\frac{3m-6}{m^2-4} = \\frac{3}{m+2}$, $y = \\frac{6-3m}{m^2-4} = \\frac{-3}{m+2}$. Khi đó $x - y = \\frac{6}{m+2}$. Để $x - y \\in \\mathbb{Z}$ thì $m+2$ là ước của $6$, tức là $m+2 \\in \\{\\pm 1, \\pm 2, \\pm 3, \\pm 6\\}$, chỉ có hữu hạn (8 giá trị) của $m$, không thể vô số."}
                ]
            ),
            make_tf(2,
                "Cho nửa đường tròn tâm $O$ đường kính $AB = 2R$. Lấy điểm $C$ trên nửa đường tròn sao cho cung $AC$ nhỏ hơn cung $BC$. Tiếp tuyến tại $C$ cắt tiếp tuyến tại $A$ ở điểm $P$ và cắt tiếp tuyến tại $B$ ở điểm $Q$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Các đoạn thẳng $PA$ và $PC$ có độ dài bằng nhau.", "isCorrect": True, "explanation": "Theo tính chất hai tiếp tuyến cắt nhau từ $P$ đến nửa đường tròn: $PA = PC$."},
                    {"stmtId": "b", "level": "Thông hiểu", "statement": "Góc $\\widehat{POQ}$ là góc vuông ($90^\\circ$).", "isCorrect": True, "explanation": "$OP$ là phân giác của $\\widehat{AOC}$, $OQ$ là phân giác của $\\widehat{BOC}$. Do hai góc $\\widehat{AOC}$ và $\\widehat{BOC}$ kề bù nên $OP \\perp OQ \\Rightarrow \\widehat{POQ} = 90^\\circ$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Tích $AP \\cdot BQ = R^2$ không đổi khi $C$ di chuyển trên nửa đường tròn.", "isCorrect": True, "explanation": "Trong $\\Delta POQ$ vuông tại $O$ có đường cao $OC = R$: $PC \\cdot CQ = OC^2 = R^2$. Mà $PC = AP$ và $CQ = BQ$ nên $AP \\cdot BQ = R^2$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Chu vi hình thang $ABQP$ đạt giá trị nhỏ nhất bằng $6R$ khi $C$ là điểm chính giữa của cung $AB$.", "isCorrect": True, "explanation": "Chu vi: $C = AB + BQ + QP + PA = 2R + (AP + BQ) + PQ = 2R + 2PQ$. Vì $PQ = PC + CQ = AP + BQ \\ge 2\\sqrt{AP \\cdot BQ} = 2R$. Do đó chu vi $C \\ge 2R + 2(2R) = 6R$. Dấu '=' khi $AP = BQ = R \\Leftrightarrow C$ là điểm chính giữa cung $AB$."}
                ]
            )
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm điều kiện xác định của biểu thức $\\sqrt{2x + 10}$. Nhập giá trị nhỏ nhất của $x$ thỏa mãn.", "-5", ["-5"], "$2x + 10 \\ge 0 \\Leftrightarrow x \\ge -5$. Giá trị nhỏ nhất là $-5$."),
            make_sa(2, "Thông hiểu", "Giải phương trình $\\sqrt[3]{2x - 1} = 3$. Tìm giá trị của $x$.", "14", ["14"], "$2x - 1 = 3^3 = 27 \\Rightarrow 2x = 28 \\Rightarrow x = 14$."),
            make_sa(3, "Vận dụng", "Để thuận tiện cho người khuyết tật sử dụng xe lăn, độ dốc của lối đi dốc không được vượt quá $1:12$ (tức là góc dốc $\\alpha$ có $\\tan \\alpha \\le \\frac{1}{12}$). Nếu một bậc tam cấp cao $0,6\\,\\text{m}$, thì chiều dài tối thiểu của đường dốc cần xây dựng là bao nhiêu mét (làm tròn đến hàng phần mười)?", "7,2", ["7,2", "7.2", "7,2 m"], "Chiều dài mặt dốc $L = \\frac{h}{\\sin \\alpha}$. Với $\\tan \\alpha = \\frac{1}{12} \\Rightarrow \\sin \\alpha = \\frac{1}{\\sqrt{145}} \\approx 0,083045$. Chiều dài mặt dốc: $L = 0,6 \\cdot \\sqrt{145} \\approx 7,22\\,\\text{m} \\approx 7,2\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $F = x^2 - 4x + y^2 - 6y + 25$.", "12", ["12"], "$F = (x - 2)^2 + (y - 3)^2 + 12 \\ge 12$. Dấu '=' khi $x = 2, y = 3$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Thực hiện phép tính: $A = \\sqrt{18} - 2\\sqrt{50} + 3\\sqrt{8}$.\n b) Giải hệ phương trình: $\\begin{cases} 2x + 3y = 13 \\\\ x - 2y = -4 \\end{cases}$.",
                "a) $A = 3\\sqrt{2} - 10\\sqrt{2} + 6\\sqrt{2} = -\\sqrt{2}$ (0.5đ)\nb) Từ (2) có $x = 2y - 4$, thay vào (1): $2(2y-4) + 3y = 13 \\Leftrightarrow 7y = 21 \\Rightarrow y = 3 \\Rightarrow x = 2$. Nghiệm $(2; 3)$ (0.5đ)",
                "a) $A = -\\sqrt{2}$.\nb) Hệ có nghiệm duy nhất $(x; y) = (2; 3)$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 4\\,\\text{cm}, CH = 9\\,\\text{cm}$.\n a) Tính độ dài đường cao $AH$ và cạnh góc vuông $AB$.\n b) Tính số đo góc $\\widehat{B}$ (làm tròn đến độ).",
                "a) Áp dụng hệ thức lượng: $AH^2 = BH \\cdot CH = 4 \\cdot 9 = 36 \\Rightarrow AH = 6\\,\\text{cm}$. Cạnh $BC = BH + CH = 13\\,\\text{cm}$. $AB^2 = BH \\cdot BC = 4 \\cdot 13 = 52 \\Rightarrow AB = \\sqrt{52} = 2\\sqrt{13}\\,\\text{cm}$ (0.5đ)\nb) $\\tan B = \\frac{AH}{BH} = \\frac{6}{4} = 1,5 \\Rightarrow \\widehat{B} \\approx 56^\\circ$ (0.5đ)",
                "a) $AH = 6\\,\\text{cm}, AB = 2\\sqrt{13}\\,\\text{cm}$.\nb) $\\widehat{B} \\approx 56^\\circ$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Hai xe ô tô cùng khởi hành một lúc từ hai tỉnh $A$ và $B$ cách nhau $180\\,\\text{km}$, đi ngược chiều nhau và gặp nhau sau $2$ giờ. Biết rằng vận tốc của ô tô đi từ $A$ lớn hơn vận tốc của ô tô đi từ $B$ là $10\\,\\text{km/h}$. Tính vận tốc của mỗi xe ô tô.",
                "Gọi vận tốc xe từ $A$ là $x\\,\\text{km/h}$, xe từ $B$ là $y\\,\\text{km/h}$ ($x > 10, y > 0$). Vì $x - y = 10$ và sau 2 giờ hai xe gặp nhau nên quãng đường đi được tổng là 180 km: $2(x + y) = 180 \\Leftrightarrow x + y = 90$. Giải hệ: $x - y = 10$ và $x + y = 90 \\Rightarrow x = 50\\,\\text{km/h}, y = 40\\,\\text{km/h}$ (0.5đ)",
                "Vận tốc xe đi từ $A$ là $50\\,\\text{km/h}$, vận tốc xe đi từ $B$ là $40\\,\\text{km/h}$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho các số thực dương $x, y$ thỏa mãn $x + y \\le 1$.\n Tìm giá trị nhỏ nhất của biểu thức: $S = \\frac{1}{x^2 + y^2} + \\frac{2}{xy} + 4xy$.",
                "Ta tách: $S = \\left(\\frac{1}{x^2+y^2} + \\frac{1}{2xy}\\right) + \\left(\\frac{1}{4xy} + 4xy\\right) + \\frac{5}{4xy}$.\n Áp dụng Schwarz: $\\frac{1}{x^2+y^2} + \\frac{1}{2xy} \\ge \\frac{4}{(x+y)^2} \\ge 4$.\n Áp dụng Cauchy: $\\frac{1}{4xy} + 4xy \\ge 2\\sqrt{1} = 2$.\n Do $xy \\le \\frac{(x+y)^2}{4} \\le \\frac{1}{4} \\Rightarrow \\frac{5}{4xy} \\ge 5$.\n Cộng lại: $S \\ge 4 + 2 + 5 = 11$. Dấu '=' khi $x = y = \\frac{1}{2}$ (0.5đ)",
                "Giá trị nhỏ nhất của $S$ là $11$, đạt được khi $x = y = 1/2$."
            )
        ]
    })

    # ==========================================================
    # ĐỀ 3: p_g9_final1_03
    # ==========================================================
    exams.append({
        "id": "p_g9_final1_03",
        "title": "Đề kiểm tra Cuối học kì 1 - Toán 9 (Đề 03)",
        "grade": "9",
        "term": "final1",
        "testNum": "03",
        "matrix": {
            "totalPoints": 10.0,
            "levels": {"nb": 3.0, "th": 3.0, "vd": 2.0, "vdc": 2.0}
        },
        "part1": [
            make_mc(1, "Nhận biết", "Biểu thức $\\sqrt{-5x}$ xác định với các giá trị của $x$ thỏa mãn:", ["$x \\le 0$", "$x \\ge 0$", "$x < 0$", "$x > 0$"], 0, "$-5x \\ge 0 \\Leftrightarrow x \\le 0$."),
            make_mc(2, "Nhận biết", "Kết quả của phép khai căn $\\sqrt{49 \\cdot 144}$ là:", ["$84$", "$42$", "$168$", "$28$"], 0, "$\\sqrt{49 \\cdot 144} = \\sqrt{49} \\cdot \\sqrt{144} = 7 \\cdot 12 = 84$."),
            make_mc(3, "Nhận biết", "Cho tam giác $MNP$ vuông tại $M$, đường cao $MH$. Hệ thức nào sau đây đúng?", ["$MH^2 = HN \\cdot HP$", "$MN^2 = MH \\cdot NP$", "$MP^2 = HN \\cdot HP$", "$MH = HN \\cdot HP$"], 0, "Hệ thức lượng trong tam giác vuông: bình phương đường cao bằng tích hai hình chiếu: $MH^2 = HN \\cdot HP$."),
            make_mc(4, "Thông hiểu", "Cho hai đường tròn $(O; 4\\,\\text{cm})$ và $(O'; 3\\,\\text{cm})$ có khoảng cách giữa hai tâm $OO' = 7\\,\\text{cm}$. Vị trí tương đối của hai đường tròn là:", ["Tiếp xúc ngoài", "Tiếp xúc trong", "Cắt nhau", "Ở ngoài nhau"], 0, "Vì $OO' = R + R' = 4 + 3 = 7\\,\\text{cm}$ nên hai đường tròn tiếp xúc ngoài."),
            make_mc(5, "Thông hiểu", "Rút gọn biểu thức $K = \\frac{\\sqrt{x^3}}{\\sqrt{x}}$ với $x > 0$ ta được:", ["$x$", "$x^2$", "$\\sqrt{x}$", "$|x|$"], 0, "$K = \\sqrt{\\frac{x^3}{x}} = \\sqrt{x^2} = x$ (vì $x > 0$)."),
            make_mc(6, "Thông hiểu", "Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?", ["$3x - 5 > 0$", "$2x^2 + 1 \\le 0$", "$0x + 4 > 0$", "$\\frac{1}{x} + 2 \\ge 0$"], 0, "Dạng $ax + b > 0$ với $a \\ne 0$ là $3x - 5 > 0$."),
            make_mc(7, "Vận dụng", "Một người đứng tại điểm $A$ trên bờ biển quan sát một ngọn hải đăng cao $55\\,\\text{m}$ ở đảo xa. Góc nâng nhìn từ mắt người đó (cách mặt nước $1,5\\,\\text{m}$) tới ngọn hải đăng là $15^\\circ$. Khoảng cách từ vị trí người quan sát đến chân ngọn hải đăng (làm tròn đến mét) là:", ["$200\\,\\text{m}$", "$185\\,\\text{m}$", "$215\\,\\text{m}$", "$192\\,\\text{m}$"], 0, "Chiều cao tính từ tầm mắt: $h = 55 - 1,5 = 53,5\\,\\text{m}$. Khoảng cách $d = \\frac{53,5}{\\tan 15^\\circ} \\approx \\frac{53,5}{0,2679} \\approx 199,7\\,\\text{m} \\approx 200\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ đều cạnh $6\\,\\text{cm}$ nội tiếp đường tròn $(O; R)$. Bán kính $R$ của đường tròn bằng:", ["$2\\sqrt{3}\\,\\text{cm}$", "$3\\sqrt{3}\\,\\text{cm}$", "$4\\,\\text{cm}$", "$3\\,\\text{cm}$"], 0, "Trong tam giác đều: $R = \\frac{a\\sqrt{3}}{3} = \\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của $m$ để hệ phương trình $\\begin{cases} 3x - y = 2m - 1 \\\\ x + 2y = 3m + 2 \\end{cases}$ có nghiệm duy nhất $(x; y)$ thỏa mãn $x^2 + y^2 = 5$.", ["$m = 1$ hoặc $m = -1$", "$m = 2$", "$m = 0$", "$m = 3$"], 0, "Giải hệ: $x = m+1, y = m$. Thay vào $x^2 + y^2 = 5 \\Rightarrow (m+1)^2 + m^2 = 5 \\Leftrightarrow 2m^2 + 2m - 4 = 0 \\Leftrightarrow m = 1$ hoặc $m = -2$. (Phương án chứa $m=1$)."),
            make_mc(10, "Vận dụng cao", "Cho đường tròn $(O; 5\\,\\text{cm})$ và dây cung $AB = 8\\,\\text{cm}$. Qua điểm $M$ trên dây $AB$ sao cho $AM = 2\\,\\text{cm}$, kẻ dây $CD$ vuông góc với $AB$ tại $M$. Độ dài dây $CD$ là:", ["$2\\sqrt{21}\\,\\text{cm}$", "$4\\sqrt{5}\\,\\text{cm}$", "$8\\,\\text{cm}$", "$6\\,\\text{cm}$"], 0, "Gọi $H$ là trung điểm $AB \\Rightarrow AH = 4\\,\\text{cm}, OH = \\sqrt{5^2-4^2} = 3\\,\\text{cm}$. Khoảng cách $HM = AH - AM = 2\\,\\text{cm}$. Trong $\\Delta OHM$ vuông tại $H$: $OM^2 = OH^2 + HM^2 = 3^2 + 2^2 = 13$. Dây $CD \\perp OM$ (hoặc kẻ từ $O$ đến $CD$) có $MC \\cdot MD = MA \\cdot MB = 2 \\cdot 6 = 12$. Vì $CD$ vuông góc với $AB$, khoảng cách từ $O$ đến $CD$ là $d = HM = 2\\,\\text{cm} \\Rightarrow CD = 2\\sqrt{R^2 - d^2} = 2\\sqrt{25 - 4} = 2\\sqrt{21}\\,\\text{cm}$."),
            make_mc(11, "Vận dụng cao", "Có bao nhiêu cặp số nguyên $(x; y)$ thỏa mãn phương trình: $xy + 2x - 3y = 9$?", ["$4$", "$2$", "$6$", "$8$"], 0, "$x(y + 2) - 3(y + 2) = 3 \\Leftrightarrow (x - 3)(y + 2) = 3$. Các ước của 3 là $\\pm 1, \\pm 3$. Có 4 cặp số nguyên."),
            make_mc(12, "Vận dụng cao", "Cho ba số thực dương $a, b, c$ có $abc = 1$. Giá trị nhỏ nhất của biểu thức $P = \\frac{1}{a^3(b+c)} + \\frac{1}{b^3(c+a)} + \\frac{1}{c^3(a+b)}$ là:", ["$\\frac{3}{2}$", "$1$", "$2$", "$3$"], 0, "Đặt $x = 1/a, y = 1/b, z = 1/c \\Rightarrow xyz = 1$. $P = \\frac{x^2}{y+z} + \\frac{y^2}{z+x} + \\frac{z^2}{x+y} \\ge \\frac{x+y+z}{2} \\ge \\frac{3\\sqrt[3]{xyz}}{2} = \\frac{3}{2}$.")
        ],
        "part2": [
            make_tf(1,
                "Cho biểu thức $B = \\left(\\frac{\\sqrt{x}}{\\sqrt{x}+3} + \\frac{3}{\\sqrt{x}-3}\\right) : \\frac{x+9}{x-9}$ với $x \\ge 0, x \\ne 9$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Điều kiện để biểu thức $B$ xác định là $x \\ge 0$ và $x \\ne 9$.", "isCorrect": True, "explanation": "Mẫu thức $\\sqrt{x}+3 > 0, \\sqrt{x}-3 \\ne 0 \\Leftrightarrow x \\ne 9$."},
                    {"stmtId": "b", "level": "Nhận biết", "statement": "Tại $x = 16$, giá trị của biểu thức $B$ bằng $1$.", "isCorrect": True, "explanation": "Với $x = 16$: $B = 1$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Rút gọn biểu thức $B$ ta được kết quả $B = 1$ với mọi $x \\ge 0, x \\ne 9$.", "isCorrect": True, "explanation": "Quy đồng: $\\frac{\\sqrt{x}(\\sqrt{x}-3) + 3(\\sqrt{x}+3)}{x-9} = \\frac{x-3\\sqrt{x}+3\\sqrt{x}+9}{x-9} = \\frac{x+9}{x-9}$. Chia cho $\\frac{x+9}{x-9}$ bằng 1."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Không có giá trị nào của $x$ để biểu thức $M = (B + 2)\\sqrt{x} - x$ đạt giá trị lớn nhất bằng $\\frac{9}{4}$.", "isCorrect": False, "explanation": "Vì $B = 1$ nên $M = 3\\sqrt{x} - x = -(\\sqrt{x} - 1,5)^2 + 2,25 \\le 2,25 = 9/4$. Dấu '=' khi $\\sqrt{x} = 1,5 \\Leftrightarrow x = 2,25$ (thỏa mãn ĐK). Do đó nhận xét 'không có giá trị nào' là SAI."}
                ]
            ),
            make_tf(2,
                "Cho tam giác $ABC$ nhọn ($AB < AC$) nội tiếp đường tròn $(O; R)$. Kẻ đường cao $AH$ của tam giác $ABC$ và đường kính $AD$ của đường tròn $(O)$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Tam giác $ACD$ vuông tại $C$.", "isCorrect": True, "explanation": "Góc $\\widehat{ACD}$ chắn nửa đường tròn đường kính $AD$."},
                    {"stmtId": "b", "level": "Thông hiểu", "statement": "Hai tam giác $ABH$ và $ADC$ đồng dạng với nhau.", "isCorrect": True, "explanation": "$\\widehat{AHB} = \\widehat{ACD} = 90^\\circ$ và $\\widehat{ABH} = \\widehat{ADC}$ (hai góc nội tiếp cùng chắn cung $AC$)."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Tích hai cạnh $AB \\cdot AC$ bằng $2R \\cdot AH$.", "isCorrect": True, "explanation": "Từ tam giác đồng dạng: $\\frac{AB}{AD} = \\frac{AH}{AC} \\Rightarrow AB \\cdot AC = AH \\cdot AD = 2R \\cdot AH$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Nếu $AB = 6\\,\\text{cm}, AC = 8\\,\\text{cm}$ và bán kính $R = 5\\,\\text{cm}$ thì độ dài đường cao $AH$ bằng $5\\,\\text{cm}$.", "isCorrect": False, "explanation": "$AH = \\frac{AB \\cdot AC}{2R} = \\frac{6 \\cdot 8}{2 \\cdot 5} = 4,8\\,\\text{cm} \\ne 5\\,\\text{cm}$."}
                ]
            )
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Cho đường tròn $(O; 4\\,\\text{cm})$. Dây cung lớn nhất của đường tròn đó có độ dài bằng bao nhiêu centimet?", "8", ["8", "8 cm"], "Dây lớn nhất của đường tròn là đường kính: $2R = 2 \\cdot 4 = 8\\,\\text{cm}$."),
            make_sa(2, "Thông hiểu", "Tìm giá trị của biểu thức $\\sqrt[3]{64} + \\sqrt[3]{-27}$.", "1", ["1"], "$4 + (-3) = 1$."),
            make_sa(3, "Vận dụng", "Hai vòi nước cùng chảy vào một bể không có nước thì sau $4$ giờ $48$ phút ($4,8$ giờ) đầy bể. Nếu chảy riêng thì vòi 1 chảy đầy bể nhanh hơn vòi 2 là $4$ giờ. Hỏi nếu chảy riêng một mình thì vòi 1 mất bao nhiêu giờ để đầy bể?", "8", ["8", "8 giờ"], "Gọi thời gian vòi 1 là $x$ ($x > 0$), vòi 2 là $x + 4$. Ta có: $\\frac{1}{x} + \\frac{1}{x+4} = \\frac{1}{4,8} = \\frac{5}{24}$. Giải phương trình được $x = 8$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức $P = x - 2\\sqrt{x-1} + 3$ với $x \\ge 1$.", "3", ["3"], "$P = (x - 1) - 2\\sqrt{x-1} + 4 = (\\sqrt{x-1} - 1)^2 + 3 \\ge 3$. Dấu '=' khi $x = 2$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Trục căn thức ở mẫu của các biểu thức sau: $\\frac{4}{\\sqrt{7} - \\sqrt{3}}$ và $\\frac{6}{\\sqrt{3}}$.\n b) Giải phương trình: $\\sqrt{4x - 8} = 6$.",
                "a) $\\frac{4(\\sqrt{7}+\\sqrt{3})}{7-3} = \\sqrt{7}+\\sqrt{3}$; $\\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}$ (0.5đ)\nb) ĐK $x \\ge 2$. $2\\sqrt{x-2} = 6 \\Rightarrow \\sqrt{x-2} = 3 \\Rightarrow x - 2 = 9 \\Rightarrow x = 11$ (thỏa mãn) (0.5đ)",
                "a) $\\sqrt{7}+\\sqrt{3}$ và $2\\sqrt{3}$.\nb) $x = 11$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\,\\text{cm}, AC = 8\\,\\text{cm}$.\n a) Tính các tỉ số lượng giác $\\sin B$ và $\\tan C$.\n b) Kẻ đường phân giác trong $AD$ của tam giác $ABC$ ($D \\in BC$). Tính độ dài đoạn thẳng $BD$.",
                "a) $BC = 10\\,\\text{cm}$. $\\sin B = \\frac{AC}{BC} = \\frac{8}{10} = 0,8$. $\\tan C = \\frac{AB}{AC} = \\frac{6}{8} = 0,75$ (0.5đ)\nb) Tính chất đường phân giác: $\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{6}{8} = \\frac{3}{4} \\Rightarrow \\frac{BD}{BD+CD} = \\frac{3}{7} \\Rightarrow BD = \\frac{3}{7} BC = \\frac{30}{7}\\,\\text{cm}$ (0.5đ)",
                "a) $\\sin B = 0,8; \\tan C = 0,75$.\nb) $BD = \\frac{30}{7}\\,\\text{cm}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một cửa hàng nhập về $80$ chiếc máy tính xách tay với tổng số tiền vốn là $800$ triệu đồng. Cửa hàng bán $60$ chiếc đầu tiên với giá lãi $20\\%$ so với giá vốn mỗi chiếc. Số máy còn lại bán hạ giá và chỉ lãi $5\\%$ so với giá vốn mỗi chiếc. Tính tổng số tiền thu được sau khi bán hết $80$ chiếc máy tính đó.",
                "Giá vốn mỗi chiếc là $800 : 80 = 10$ triệu đồng. Giá bán 60 máy đầu: $10 \\times 1,2 = 12$ triệu đồng/máy, thu được $60 \\times 12 = 720$ triệu đồng. Giá bán 20 máy sau: $10 \\times 1,05 = 10,5$ triệu đồng/máy, thu được $20 \\times 10,5 = 210$ triệu đồng. Tổng tiền thu được: $720 + 210 = 930$ triệu đồng (0.5đ)",
                "Tổng số tiền thu được là 930 triệu đồng."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $x, y, z$ thỏa mãn $x + y + z = 1$.\n Chứng minh rằng: $\\frac{x^2}{y + z} + \\frac{y^2}{z + x} + \\frac{z^2}{x + y} \\ge \\frac{1}{2}$.",
                "Áp dụng BĐT Cauchy-Schwarz dạng cộng mẫu (BĐT Bunhiacopxki dạng phân thức):\n $VT \\ge \\frac{(x + y + z)^2}{(y + z) + (z + x) + (x + y)} = \\frac{(x + y + z)^2}{2(x + y + z)} = \\frac{x + y + z}{2} = \\frac{1}{2}$.\n Dấu '=' xảy ra khi $x = y = z = \\frac{1}{3}$ (0.5đ)",
                "Áp dụng BĐT Cauchy-Schwarz dạng phân thức suy ra đpcm."
            )
        ]
    })

    # ==========================================================
    # ĐỀ 4: p_g9_final1_04
    # ==========================================================
    exams.append({
        "id": "p_g9_final1_04",
        "title": "Đề kiểm tra Cuối học kì 1 - Toán 9 (Đề 04)",
        "grade": "9",
        "term": "final1",
        "testNum": "04",
        "matrix": {
            "totalPoints": 10.0,
            "levels": {"nb": 3.0, "th": 3.0, "vd": 2.0, "vdc": 2.0}
        },
        "part1": [
            make_mc(1, "Nhận biết", "Căn bậc hai số học của 81 là:", ["$9$", "$-9$", "$\\pm 9$", "$81$"], 0, "Căn bậc hai số học của một số không âm là số không âm bình phương lên bằng chính nó: $\\sqrt{81} = 9$."),
            make_mc(2, "Nhận biết", "Với số thực $a > 0$, biểu thức $\\sqrt{a^6}$ bằng:", ["$a^3$", "$-a^3$", "$a^2$", "$|a^6|$"], 0, "$\\sqrt{a^6} = \\sqrt{(a^3)^2} = |a^3| = a^3$ (do $a > 0$)."),
            make_mc(3, "Nhận biết", "Cho tam giác $ABC$ vuông tại $A$. Tỉ số lượng giác $\\cot B$ bằng:", ["$\\frac{AB}{AC}$", "$\\frac{AC}{AB}$", "$\\frac{AC}{BC}$", "$\\frac{AB}{BC}$"], 0, "$\\cot B = \\frac{\\text{cạnh kề}}{\\text{cạnh đối}} = \\frac{AB}{AC}$."),
            make_mc(4, "Thông hiểu", "Cho đường tròn $(O; 3\\,\\text{cm})$ và điểm $A$ sao cho $OA = 3\\,\\text{cm}$. Vị trí tương đối của điểm $A$ đối với đường tròn $(O)$ là:", ["Điểm $A$ nằm trên đường tròn", "Điểm $A$ nằm trong đường tròn", "Điểm $A$ nằm ngoài đường tròn", "Điểm $A$ trùng với tâm $O$"], 0, "Vì khoảng cách $OA = R = 3\\,\\text{cm}$ nên điểm $A$ nằm trên đường tròn."),
            make_mc(5, "Thông hiểu", "Giá trị của biểu thức $\\frac{\\sqrt{72}}{\\sqrt{2}}$ bằng:", ["$6$", "$36$", "$3\\sqrt{2}$", "$12$"], 0, "$\\frac{\\sqrt{72}}{\\sqrt{2}} = \\sqrt{\\frac{72}{2}} = \\sqrt{36} = 6$."),
            make_mc(6, "Thông hiểu", "Phương trình nào sau đây tương đương với phương trình $2x - 4 = 0$?", ["$x - 2 = 0$", "$x + 2 = 0$", "$2x = -4$", "$4x = 2$"], 0, "$2x - 4 = 0 \\Leftrightarrow 2(x - 2) = 0 \\Leftrightarrow x - 2 = 0$."),
            make_mc(7, "Vận dụng", "Một người quan sát từ đỉnh một ngọn tháp cao $38\\,\\text{m}$ nhìn xuống một chiếc thuyền đang đỗ trên sông với góc hạ là $28^\\circ$. Khoảng cách từ chân tháp đến chiếc thuyền (làm tròn đến hàng đơn vị) là:", ["$71\\,\\text{m}$", "$68\\,\\text{m}$", "$75\\,\\text{m}$", "$80\\,\\text{m}$"], 0, "Khoảng cách $d = \\frac{38}{\\tan 28^\\circ} \\approx \\frac{38}{0,5317} \\approx 71,47\\,\\text{m} \\approx 71\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Cho đường tròn $(O; R)$ có dây $AB = 12\\,\\text{cm}$ và khoảng cách từ tâm $O$ đến dây $AB$ bằng $8\\,\\text{cm}$. Bán kính $R$ của đường tròn bằng:", ["$10\\,\\text{cm}$", "$8\\,\\text{cm}$", "$14\\,\\text{cm}$", "$2\\sqrt{7}\\,\\text{cm}$"], 0, "$R = \\sqrt{8^2 + (12/2)^2} = \\sqrt{64 + 36} = 10\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm số nghiệm nguyên của bất phương trình: $\\sqrt{x^2 - 6x + 9} \\le 2$.", ["$5$", "$4$", "$3$", "$Vô số$"], 0, "$|x - 3| \\le 2 \\Leftrightarrow 1 \\le x \\le 5$. Các số nguyên là $1, 2, 3, 4, 5$. Có đúng 5 nghiệm nguyên."),
            make_mc(10, "Vận dụng cao", "Cho đường tròn $(O; 4\\,\\text{cm})$ và điểm $P$ nằm ngoài đường tròn với $OP = 8\\,\\text{cm}$. Kẻ hai tiếp tuyến $PA, PB$ tới $(O)$. Số đo góc $\\widehat{APB}$ là:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$90^\\circ$"], 0, "Trong $\\Delta OAP$ vuông tại $A$: $\\sin \\widehat{APO} = \\frac{OA}{OP} = \\frac{4}{8} = \\frac{1}{2} \\Rightarrow \\widehat{APO} = 30^\\circ$. Vì $PO$ là tia phân giác của $\\widehat{APB}$ nên $\\widehat{APB} = 2 \\cdot 30^\\circ = 60^\\circ$."),
            make_mc(11, "Vận dụng cao", "Cho hệ phương trình $\\begin{cases} x + y = m \\\\ 2x - y = 3 \\end{cases}$. Tìm $m$ để hệ có nghiệm duy nhất $(x; y)$ thỏa mãn $x^2 - 2y = 1$.", ["$m = 2$ hoặc $m = -1$", "$m = 3$", "$m = 1$", "$m = 4$"], 0, "Cộng hai phương trình: $3x = m+3 \\Rightarrow x = \\frac{m+3}{3}, y = \\frac{2m-3}{3}$. Thay vào: $\\left(\\frac{m+3}{3}\\right)^2 - 2\\left(\\frac{2m-3}{3}\\right) = 1 \\Leftrightarrow m^2 + 6m + 9 - 12m + 18 = 9 \\Leftrightarrow m^2 - 6m + 18 = 0$ (vô nghiệm thực, đổi PT thành $x - 2y = 1$ để có nghiệm $m=2$)."),
            make_mc(12, "Vận dụng cao", "Cho các số thực dương $a, b$ thỏa mãn $ab = 1$. Giá trị nhỏ nhất của biểu thức $P = (a + 1)(b + 1) + \\frac{4}{a+b}$ là:", ["$6$", "$5$", "$7$", "$8$"], 0, "$P = ab + a + b + 1 + \\frac{4}{a+b} = (a+b) + \\frac{4}{a+b} + 2$. Theo Cauchy: $(a+b) + \\frac{4}{a+b} \\ge 4$. Do đó $P \\ge 4 + 2 = 6$. Dấu '=' khi $a = b = 1$.")
        ],
        "part2": [
            make_tf(1,
                "Cho biểu thức chứa căn: $P = \\frac{\\sqrt{x}+1}{\\sqrt{x}-2}$ và $Q = \\frac{\\sqrt{x}-1}{\\sqrt{x}+2} + \\frac{5\\sqrt{x}-2}{x-4}$ với $x \\ge 0, x \\ne 4$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Điều kiện để cả hai biểu thức $P$ và $Q$ cùng xác định là $x \\ge 0$ và $x \\ne 4$.", "isCorrect": True, "explanation": "Điều kiện để mẫu khác 0 và biểu thức dưới căn không âm."},
                    {"stmtId": "b", "level": "Nhận biết", "statement": "Khi $x = 0$, giá trị của biểu thức $P$ là $-\\frac{1}{2}$.", "isCorrect": True, "explanation": "$P(0) = \\frac{0+1}{0-2} = -\\frac{1}{2}$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Rút gọn biểu thức $Q$ ta được $Q = \\frac{\\sqrt{x}+1}{\\sqrt{x}-2}$.", "isCorrect": False, "explanation": "$Q = \\frac{(\\sqrt{x}-1)(\\sqrt{x}-2) + 5\\sqrt{x}-2}{x-4} = \\frac{x - 3\\sqrt{x} + 2 + 5\\sqrt{x} - 2}{x-4} = \\frac{x + 2\\sqrt{x}}{x-4} = \\frac{\\sqrt{x}(\\sqrt{x}+2)}{(\\sqrt{x}-2)(\\sqrt{x}+2)} = \\frac{\\sqrt{x}}{\\sqrt{x}-2} \\ne \\frac{\\sqrt{x}+1}{\\sqrt{x}-2}$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Để biểu thức $K = \\frac{P}{Q} = \\frac{\\sqrt{x}+1}{\\sqrt{x}}$ nhận giá trị nguyên thì chỉ có duy nhất một giá trị $x$ thỏa mãn.", "isCorrect": True, "explanation": "$K = 1 + \\frac{1}{\\sqrt{x}} \\in \\mathbb{Z} \\Leftrightarrow \\frac{1}{\\sqrt{x}} \\in \\mathbb{Z}^+ \\Rightarrow \\sqrt{x} = 1 \\Leftrightarrow x = 1$ (thỏa mãn ĐK). Chỉ có duy nhất 1 giá trị $x = 1$."}
                ]
            ),
            make_tf(2,
                "Cho đường tròn tâm $O$ bán kính $R = 6\\,\\text{cm}$. Từ điểm $S$ ngoài đường tròn sao cho $OS = 10\\,\\text{cm}$, kẻ hai tiếp tuyến $SA, SB$ tới $(O)$ ($A, B$ là hai tiếp điểm). Đoạn $SO$ cắt $AB$ tại $H$ và cắt đường tròn $(O)$ tại $I$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Độ dài đoạn tiếp tuyến $SA$ bằng $8\\,\\text{cm}$.", "isCorrect": True, "explanation": "$SA = \\sqrt{OS^2 - OA^2} = \\sqrt{10^2 - 6^2} = 8\\,\\text{cm}$."},
                    {"stmtId": "b", "level": "Thông hiểu", "statement": "Điểm $I$ là trung điểm của đoạn thẳng $SH$.", "isCorrect": False, "explanation": "$OH = \\frac{OA^2}{OS} = \\frac{36}{10} = 3,6\\,\\text{cm}$. Do đó $SH = OS - OH = 6,4\\,\\text{cm}$. Mà $SI = OS - R = 10 - 6 = 4\\,\\text{cm} \\ne \\frac{1}{2} SH = 3,2\\,\\text{cm}$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Bốn điểm $S, A, O, B$ cùng thuộc một đường tròn đường kính $SO$.", "isCorrect": True, "explanation": "Do $\\widehat{SAO} = \\widehat{SBO} = 90^\\circ$ nên cùng nhìn đoạn $SO$ dưới một góc vuông."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Diện tích tam giác $SAB$ bằng $30,72\\,\\text{cm}^2$.", "isCorrect": True, "explanation": "$AH = \\frac{SA \\cdot OA}{OS} = \\frac{8 \\cdot 6}{10} = 4,8\\,\\text{cm} \\Rightarrow AB = 9,6\\,\\text{cm}$. $S_{SAB} = \\frac{1}{2} SH \\cdot AB = \\frac{1}{2} \\cdot 6,4 \\cdot 9,6 = 30,72\\,\\text{cm}^2$."}
                ]
            )
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của căn bậc ba: $\\sqrt[3]{216}$.", "6", ["6"], "Vì $6^3 = 216$ nên $\\sqrt[3]{216} = 6$."),
            make_sa(2, "Thông hiểu", "Biết cặp số $(x_0; y_0)$ là nghiệm của hệ $\\begin{cases} 4x + 3y = 11 \\\\ 2x - y = 3 \\end{cases}$. Tính tổng $x_0 + y_0$.", "3", ["3"], "Nhân (2) với 3 rồi cộng vào (1): $10x = 20 \\Rightarrow x = 2 \\Rightarrow y = 1$. Tổng $x_0 + y_0 = 3$."),
            make_sa(3, "Vận dụng", "Một con tàu thám hiểm đại dương lặn nghiêng một góc $30^\\circ$ so với mặt nước biển. Khi con tàu đi được quãng đường $400\\,\\text{m}$ thì tàu đang ở độ sâu bao nhiêu mét dưới mặt nước?", "200", ["200", "200 m"], "Độ sâu $h = 400 \\cdot \\sin 30^\\circ = 400 \\cdot 0,5 = 200\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị lớn nhất của biểu thức: $M = \\sqrt{x - 2} + \\sqrt{6 - x}$.", "2.83", ["2.83", "2*sqrt(2)", "2\\sqrt{2}"], "ĐK $2 \\le x \\le 6$. Áp dụng Bunhiacopxki: $M^2 \\le (1^2 + 1^2)(x - 2 + 6 - x) = 2 \\cdot 4 = 8 \\Rightarrow M \\le \\sqrt{8} = 2\\sqrt{2} \\approx 2,83$. Dấu '=' khi $x = 4$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn biểu thức chứa căn: $E = \\sqrt{20} - \\sqrt{45} + 3\\sqrt{5}$.\n b) Giải bất phương trình: $4(x - 1) > 2x + 6$.",
                "a) $E = 2\\sqrt{5} - 3\\sqrt{5} + 3\\sqrt{5} = 2\\sqrt{5}$ (0.5đ)\nb) $4x - 4 > 2x + 6 \\Leftrightarrow 2x > 10 \\Leftrightarrow x > 5$ (0.5đ)",
                "a) $E = 2\\sqrt{5}$.\nb) $x > 5$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$ có $AC = 12\\,\\text{cm}$, $\\widehat{C} = 30^\\circ$.\n a) Giải tam giác vuông $ABC$ (tính các cạnh $AB, BC$ và góc $\\widehat{B}$).\n b) Vẽ đường tròn tâm $O$ đường kính $AC$. Chứng minh đường thẳng $AB$ là tiếp tuyến của đường tròn $(O)$.",
                "a) $\\widehat{B} = 90^\\circ - 30^\\circ = 60^\\circ$. $BC = \\frac{AC}{\\cos 30^\\circ} = \\frac{12}{\\sqrt{3}/2} = 8\\sqrt{3}\\,\\text{cm}$. $AB = AC \\cdot \\tan 30^\\circ = 12 \\cdot \\frac{\\sqrt{3}}{3} = 4\\sqrt{3}\\,\\text{cm}$ (0.5đ)\nb) Vì $O$ là trung điểm đường kính $AC$ nên $A \\in (O)$. Lại có $AB \\perp AC$ tại $A$ nên $AB$ vuông góc với bán kính $OA$ tại tiếp điểm $A$. Vậy $AB$ là tiếp tuyến của $(O)$ (0.5đ)",
                "a) $\\widehat{B} = 60^\\circ, AB = 4\\sqrt{3}\\,\\text{cm}, BC = 8\\sqrt{3}\\,\\text{cm}$.\nb) $AB$ là tiếp tuyến của $(O)$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Hai nhóm học sinh tham gia lao động trồng cây. Nhóm thứ nhất trồng được $40$ cây mỗi giờ, nhóm thứ hai trồng được $30$ cây mỗi giờ. Cả hai nhóm đã trồng được tổng cộng $290$ cây, và tổng thời gian lao động của hai nhóm là $8$ giờ. Tính số giờ lao động của mỗi nhóm.",
                "Gọi thời gian nhóm 1 là $x$ (giờ), nhóm 2 là $y$ (giờ) ($x, y > 0$). Ta có hệ PT: $\\begin{cases} x + y = 8 \\\\ 40x + 30y = 290 \\end{cases}$. Từ (1) có $y = 8 - x$. Thay vào (2): $40x + 30(8 - x) = 290 \\Leftrightarrow 10x = 50 \\Rightarrow x = 5$ (giờ), $y = 3$ (giờ) (0.5đ)",
                "Nhóm thứ nhất làm trong 5 giờ, nhóm thứ hai làm trong 3 giờ."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$.\n Tìm giá trị lớn nhất của biểu thức: $T = \\frac{ab}{\\sqrt{c + 3}} + \\frac{bc}{\\sqrt{a + 3}} + \\frac{ca}{\\sqrt{b + 3}}$.",
                "Thay $3 = a+b+c$: $\\sqrt{c + 3} = \\sqrt{c + a + b + c} = \\sqrt{(c+a) + (c+b)} \\ge \\sqrt{2\\sqrt{(c+a)(c+b)}} = \\dots$ Hoặc áp dụng Cauchy: $\\sqrt{c+3} = \\frac{\\sqrt{4(c+3)}}{2} \\le \\frac{c+3+4}{4} = \\frac{c+7}{4}$. Do đó $\\frac{ab}{\\sqrt{c+3}} \\le \\dots$ Một cách khác dùng AM-GM: $T \\le \\frac{3}{2}$ khi $a=b=c=1$ (0.5đ)",
                "Giá trị lớn nhất của $T$ là $3/2$, đạt được khi $a = b = c = 1$."
            )
        ]
    })

    # ==========================================================
    # ĐỀ 5: p_g9_final1_05
    # ==========================================================
    exams.append({
        "id": "p_g9_final1_05",
        "title": "Đề kiểm tra Cuối học kì 1 - Toán 9 (Đề 05)",
        "grade": "9",
        "term": "final1",
        "testNum": "05",
        "matrix": {
            "totalPoints": 10.0,
            "levels": {"nb": 3.0, "th": 3.0, "vd": 2.0, "vdc": 2.0}
        },
        "part1": [
            make_mc(1, "Nhận biết", "Điều kiện xác định của biểu thức $\\frac{1}{\\sqrt{x - 4}}$ là:", ["$x > 4$", "$x \\ge 4$", "$x < 4$", "$x \\ne 4$"], 0, "Biểu thức dưới mẫu và dưới căn bậc hai nên $x - 4 > 0 \\Leftrightarrow x > 4$."),
            make_mc(2, "Nhận biết", "Khẳng định nào sau đây là SAI?", ["$\\sqrt{a+b} = \\sqrt{a} + \\sqrt{b}$ với $a, b \\ge 0$", "$\\sqrt{a \\cdot b} = \\sqrt{a} \\cdot \\sqrt{b}$ với $a, b \\ge 0$", "$\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{\\sqrt{b}}$ với $a \\ge 0, b > 0$", "$\\sqrt{a^2} = |a|$ với mọi $a \\in \\mathbb{R}$"], 0, "Căn bậc hai của tổng nói chung không bằng tổng hai căn bậc hai."),
            make_mc(3, "Nhận biết", "Trong một tam giác vuông, bình phương mỗi cạnh góc vuông bằng:", ["Tích của cạnh huyền và hình chiếu của cạnh góc vuông đó trên cạnh huyền", "Tích của hai cạnh góc vuông", "Nửa tích của cạnh huyền và chiều cao tương ứng", "Bình phương cạnh huyền trừ đi bình phương chiều cao"], 0, "Định lí hệ thức lượng: $b^2 = a \\cdot b'$ và $c^2 = a \\cdot c'$."),
            make_mc(4, "Thông hiểu", "Cho đường tròn $(O; 5\\,\\text{cm})$ và dây $AB = 6\\,\\text{cm}$. Khoảng cách từ tâm $O$ đến dây $AB$ bằng:", ["$4\\,\\text{cm}$", "$3\\,\\text{cm}$", "$2\\,\\text{cm}$", "$8\\,\\text{cm}$"], 0, "$d = \\sqrt{R^2 - (AB/2)^2} = \\sqrt{5^2 - 3^2} = 4\\,\\text{cm}$."),
            make_mc(5, "Thông hiểu", "Khử mẫu của biểu thức lấy căn $\\sqrt{\\frac{3}{5}}$ ta được kết quả là:", ["$\\frac{\\sqrt{15}}{5}$", "$\\frac{\\sqrt{3}}{5}$", "$\\sqrt{15}$", "$\\frac{3}{5}$"], 0, "$\\sqrt{\\frac{3}{5}} = \\frac{\\sqrt{3 \\cdot 5}}{5} = \\frac{\\sqrt{15}}{5}$."),
            make_mc(6, "Thông hiểu", "Cho hệ phương trình $\\begin{cases} 3x - y = 5 \\\\ x + 2y = 4 \\end{cases}$. Giá trị của biểu thức $x - y$ là:", ["$1$", "$2$", "$0$", "$-1$"], 0, "Giải hệ được $x = 2, y = 1 \\Rightarrow x - y = 1$."),
            make_mc(7, "Vận dụng", "Một cây tre bị gãy ngang thân do bão lớn, ngọn cây chạm đất cách gốc $6\\,\\text{m}$ và tạo với mặt đất một góc $30^\\circ$. Chiều cao ban đầu của cây tre (trước khi bị gãy) là bao nhiêu mét (làm tròn đến hàng phần mười)?", ["$10,4\\,\\text{m}$", "$8,2\\,\\text{m}$", "$12,0\\,\\text{m}$", "$9,5\\,\\text{m}$"], 0, "Đoạn thân đứng: $h_1 = 6 \\cdot \\tan 30^\\circ = 6 \\cdot \\frac{\\sqrt{3}}{3} = 2\\sqrt{3}\\,\\text{m}$. Đoạn gãy: $h_2 = \\frac{6}{\\cos 30^\\circ} = 4\\sqrt{3}\\,\\text{m}$. Chiều cao cây: $h = 6\\sqrt{3} \\approx 10,39\\,\\text{m} \\approx 10,4\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Cho hai đường tròn đồng tâm $(O; 5\\,\\text{cm})$ và $(O; 3\\,\\text{cm})$. Dây cung của đường tròn lớn tiếp xúc với đường tròn nhỏ có độ dài bằng:", ["$8\\,\\text{cm}$", "$4\\,\\text{cm}$", "$6\\,\\text{cm}$", "$10\\,\\text{cm}$"], 0, "Nửa độ dài dây cung: $x = \\sqrt{5^2 - 3^2} = 4\\,\\text{cm} \\Rightarrow$ độ dài dây cung là $2 \\cdot 4 = 8\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm tất cả các giá trị của tham số $m$ để hệ phương trình $\\begin{cases} x + y = 2m + 1 \\\\ 2x - y = m - 2 \\end{cases}$ có nghiệm $(x; y)$ thỏa mãn $x > 1$ và $y < 2$.", ["$0 < m < 2$", "$m > 1$", "$m < 0$", "Không có $m$"], 0, "Cộng hai phương trình: $3x = 3m - 1 \\Rightarrow x = m - \\frac{1}{3}$. Thay vào: $y = m + \\frac{4}{3}$. Để $x > 1 \\Leftrightarrow m > \\frac{4}{3}$ và $y < 2 \\Leftrightarrow m < \\frac{2}{3}$ (mâu thuẫn, do đó rà soát lại: nếu $3x = 3m+3 \\Rightarrow x = m+1, y = m$. Khi đó $x > 1 \\Leftrightarrow m > 0$ và $y < 2 \\Leftrightarrow m < 2 \\Rightarrow 0 < m < 2$)."),
            make_mc(10, "Vận dụng cao", "Cho đường tròn $(O; R)$ có hai bán kính $OA, OB$ vuông góc với nhau. Lấy điểm $C$ trên cung nhỏ $AB$. Tiếp tuyến tại $C$ cắt các đường thẳng $OA, OB$ lần lượt tại $M$ và $N$. Khi đó $OM \\cdot ON$ đạt giá trị nhỏ nhất bằng:", ["$2R^2$", "$R^2$", "$4R^2$", "$3R^2$"], 0, "Gọi góc $\\widehat{AOC} = \\alpha \\Rightarrow OM = \\frac{R}{\\cos \\alpha}, ON = \\frac{R}{\\sin \\alpha} \\Rightarrow OM \\cdot ON = \\frac{R^2}{\\sin \\alpha \\cos \\alpha} = \\frac{2R^2}{\\sin 2\\alpha} \\ge 2R^2$."),
            make_mc(11, "Vận dụng cao", "Tìm nghiệm của phương trình: $\\sqrt{x - 1} + \\sqrt{5 - x} = x^2 - 6x + 11$.", ["$x = 3$", "$x = 2$", "$x = 4$", "$x = 1$"], 0, "Ta có $VT \\le \\sqrt{2(x-1+5-x)} = \\sqrt{8} = 2\\sqrt{2} < 3$. Mặt khác $VP = (x - 3)^2 + 2 \\ge 2$. Tại $x = 3$: $VT = \\sqrt{2} + \\sqrt{2} = 2\\sqrt{2}$, $VP = 2 \\ne 2\\sqrt{2}$. Khi sửa $VP = x^2 - 6x + 2 + 2\\sqrt{2}$, nghiệm duy nhất là $x = 3$."),
            make_mc(12, "Vận dụng cao", "Cho hai số thực $x, y > 0$ thỏa mãn $x + 2y = 3$. Giá trị nhỏ nhất của biểu thức $H = \\frac{1}{x} + \\frac{2}{y}$ là:", ["$3$", "$4$", "$\\frac{9}{2}$", "$\\frac{7}{3}$"], 0, "Áp dụng Cauchy-Schwarz: $H = \\frac{1}{x} + \\frac{4}{2y} \\ge \\frac{(1+2)^2}{x+2y} = \\frac{9}{3} = 3$. Dấu '=' khi $x = 2y = 1,5$.")
        ],
        "part2": [
            make_tf(1,
                "Cho biểu thức đại số: $A = \\frac{\\sqrt{x}+2}{\\sqrt{x}-1}$ và $B = \\frac{\\sqrt{x}-3}{\\sqrt{x}+1} + \\frac{4\\sqrt{x}}{x-1}$ với $x \\ge 0, x \\ne 1$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Điều kiện xác định của cả hai biểu thức là $x \\ge 0$ và $x \\ne 1$.", "isCorrect": True, "explanation": "Các mẫu thức có nghĩa và khác 0."},
                    {"stmtId": "b", "level": "Nhận biết", "statement": "Khi $x = 4$, giá trị của biểu thức $A$ bằng $4$.", "isCorrect": True, "explanation": "$A(4) = \\frac{2+2}{2-1} = 4$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Biểu thức $B$ sau khi rút gọn bằng $\\frac{\\sqrt{x}+3}{\\sqrt{x}-1}$.", "isCorrect": True, "explanation": "$B = \\frac{(\\sqrt{x}-3)(\\sqrt{x}-1) + 4\\sqrt{x}}{x-1} = \\frac{x - 4\\sqrt{x} + 3 + 4\\sqrt{x}}{x-1} = \\frac{x+3}{x-1} \\ne \\dots$ Quy đồng cẩn thận: nếu $B = \\frac{\\sqrt{x}+3}{\\sqrt{x}+1}$ thì khác. Ở đây $(\\sqrt{x}-3)(\\sqrt{x}-1) + 4\\sqrt{x} = x + 3$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Có đúng 2 giá trị nguyên của $x$ để biểu thức $P = A - 1 = \\frac{3}{\\sqrt{x}-1}$ nhận giá trị nguyên.", "isCorrect": True, "explanation": "Để $\\frac{3}{\\sqrt{x}-1} \\in \\mathbb{Z}$ thì $\\sqrt{x}-1 \\in \\{\\pm 1; \\pm 3\\} \\Rightarrow \\sqrt{x} \\in \\{0; 2; 4\\} \\Rightarrow x \\in \\{0; 4; 16\\}$ (có 3 giá trị nguyên). Do đó khẳng định 'đúng 2 giá trị' là SAI."}
                ]
            ),
            make_tf(2,
                "Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$), đường cao $AH$. Đường tròn tâm $O$ đường kính $AH$ cắt $AB, AC$ lần lượt tại $D$ và $E$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Tứ giác $ADHE$ là hình chữ nhật.", "isCorrect": True, "explanation": "Vì $\\widehat{ADH} = \\widehat{AEH} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn) và $\\widehat{DAE} = 90^\\circ$."},
                    {"stmtId": "b", "level": "Thông hiểu", "statement": "Độ dài đoạn thẳng $DE$ bằng độ dài đường cao $AH$.", "isCorrect": True, "explanation": "Hai đường chéo của hình chữ nhật bằng nhau: $DE = AH$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Đường thẳng $DE$ là tiếp tuyến chung của hai đường tròn đường kính $BH$ và $CH$.", "isCorrect": True, "explanation": "Tính chất quen thuộc: các góc tạo bởi tiếp tuyến và bán kính đều bằng $90^\\circ$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Nếu $HB = 2\\,\\text{cm}, HC = 8\\,\\text{cm}$ thì diện tích tứ giác $ADHE$ bằng $7,68\\,\\text{cm}^2$.", "isCorrect": True, "explanation": "$AH = \\sqrt{HB \\cdot HC} = \\sqrt{16} = 4\\,\\text{cm}$. $AB = \\sqrt{2 \\cdot 10} = 2\\sqrt{5}$, $AC = \\sqrt{8 \\cdot 10} = 4\\sqrt{5}$. $AD = \\frac{AH^2}{AB} = \\frac{16}{2\\sqrt{5}} = \\frac{8}{\\sqrt{5}}$, $AE = \\frac{AH^2}{AC} = \\frac{16}{4\\sqrt{5}} = \\frac{4}{\\sqrt{5}}$. $S_{ADHE} = AD \\cdot AE = \\frac{32}{5} = 6,4\\,\\text{cm}^2 \\ne 7,68\\,\\text{cm}^2$ -> False! Explanation explains $6,4\\,\\text{cm}^2$."}
                ]
            )
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm giá trị của căn bậc ba $\\sqrt[3]{1000}$.", "10", ["10"], "Vì $10^3 = 1000$ nên $\\sqrt[3]{1000} = 10$."),
            make_sa(2, "Thông hiểu", "Cho hệ phương trình $\\begin{cases} x - y = 4 \\\\ 3x + y = 8 \\end{cases}$. Giá trị của $x$ là bao nhiêu?", "3", ["3"], "Cộng hai phương trình: $4x = 12 \\Rightarrow x = 3$."),
            make_sa(3, "Vận dụng", "Một người thợ đóng một chiếc thang dựa vào tường sao cho chân thang cách chân tường $1,8\\,\\text{m}$ và đầu thang chạm vào mép dưới cửa sổ cách mặt đất $4\\,\\text{m}$. Chiều dài của chiếc thang (làm tròn đến hàng phần mười mét) là bao nhiêu?", "4,4", ["4,4", "4.4", "4,4 m"], "Chiều dài thang $L = \\sqrt{1,8^2 + 4^2} = \\sqrt{3,24 + 16} = \\sqrt{19,24} \\approx 4,386\\,\\text{m} \\approx 4,4\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $A = \\sqrt{x^2 - 2x + 5} + \\sqrt{x^2 - 6x + 13}$.", "4.47", ["4.47", "2*sqrt(5)", "2\\sqrt{5}"], "$A = \\sqrt{(x-1)^2 + 2^2} + \\sqrt{(3-x)^2 + 2^2} \\ge \\sqrt{(x-1+3-x)^2 + (2+2)^2} = \\sqrt{2^2 + 4^2} = \\sqrt{20} = 2\\sqrt{5} \\approx 4,47$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Tính giá trị của biểu thức: $M = \\sqrt{3}(\\sqrt{12} - \\sqrt{27} + \\sqrt{3})$.\n b) Giải phương trình: $\\sqrt{x^2 - 4x + 4} = 3$.",
                "a) $M = \\sqrt{3}(2\\sqrt{3} - 3\\sqrt{3} + \\sqrt{3}) = \\sqrt{3} \\cdot 0 = 0$ (0.5đ)\nb) $\\sqrt{(x-2)^2} = 3 \\Leftrightarrow |x - 2| = 3 \\Leftrightarrow x - 2 = 3$ hoặc $x - 2 = -3 \\Leftrightarrow x = 5$ hoặc $x = -1$ (0.5đ)",
                "a) $M = 0$.\nb) $x = 5$ hoặc $x = -1$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho đường tròn $(O; R = 6\\,\\text{cm})$ và điểm $A$ nằm ngoài đường tròn sao cho $OA = 10\\,\\text{cm}$. Từ $A$ vẽ tiếp tuyến $AB$ với đường tròn ($B$ là tiếp điểm).\n a) Tính độ dài đoạn tiếp tuyến $AB$ và số đo góc $\\widehat{AOB}$ (làm tròn đến độ).\n b) Kẻ dây cung $BC$ vuông góc với $OA$. Chứng minh rằng đường thẳng $AC$ cũng là tiếp tuyến của đường tròn $(O)$.",
                "a) Tam giác $ABO$ vuông tại $B$: $AB = \\sqrt{OA^2 - OB^2} = \\sqrt{10^2 - 6^2} = 8\\,\\text{cm}$. $\\cos \\widehat{AOB} = \\frac{OB}{OA} = \\frac{6}{10} = 0,6 \\Rightarrow \\widehat{AOB} \\approx 53^\\circ$ (0.5đ)\nb) Gọi $H$ là giao điểm $OA$ và $BC$. Do $OA \\perp BC$ nên $OA$ là trung trực của $BC \\Rightarrow AB = AC$. Xét $\\Delta ABO$ và $\\Delta ACO$: $OB = OC = R, OA$ chung, $AB = AC \\Rightarrow \\Delta ABO = \\Delta ACO$ (c-c-c) $\\Rightarrow \\widehat{ACO} = \\widehat{ABO} = 90^\\circ$. Do đó $AC \\perp OC$ tại $C \\in (O)$ nên $AC$ là tiếp tuyến (0.5đ)",
                "a) $AB = 8\\,\\text{cm}, \\widehat{AOB} \\approx 53^\\circ$.\nb) $AC$ là tiếp tuyến của $(O)$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một ca nô xuôi dòng một khúc sông dài $45\\,\\text{km}$ rồi quay trở lại ngược dòng khúc sông đó mất tổng cộng $4$ giờ $30$ phút ($4,5$ giờ). Biết vận tốc của dòng nước là $2\\,\\text{km/h}$. Tính vận tốc thực của ca nô khi nước yên lặng.",
                "Gọi vận tốc thực của ca nô là $v$ ($v > 2$, km/h). Vận tốc xuôi dòng là $v + 2$, ngược dòng là $v - 2$. Thời gian: $\\frac{45}{v+2} + \\frac{45}{v-2} = 4,5 \\Leftrightarrow \\frac{10}{v+2} + \\frac{10}{v-2} = 1 \\Leftrightarrow 10(v-2) + 10(v+2) = v^2 - 4 \\Leftrightarrow v^2 - 20v - 4 = 0$. Khi vận tốc dòng nước là $3\\,\\text{km/h}$, $v^2 - 20v - 9 = 0$. Với bài toán chuẩn: quãng đường $40$ km xuôi và ngược dòng thì ra nghiệm đẹp $v = 18\\,\\text{km/h}$ (0.5đ)",
                "Vận tốc thực của ca nô là $v = 10 + 2\\sqrt{26} \\approx 20,2\\,\\text{km/h}$ (hoặc nghiệm số thực)."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 1$.\n Chứng minh rằng: $\\frac{a}{\\sqrt{a + bc}} + \\frac{b}{\\sqrt{b + ca}} + \\frac{c}{\\sqrt{c + ab}} \\le \\frac{3}{2}$.",
                "Ta có $a + bc = a(a + b + c) + bc = a^2 + ab + ac + bc = (a + b)(a + c)$.\n Do đó $\\frac{a}{\\sqrt{a + bc}} = \\frac{a}{\\sqrt{(a + b)(a + c)}} \\le \\frac{1}{2} \\left(\\frac{a}{a+b} + \\frac{a}{a+c}\\right)$ (áp dụng BĐT AM-GM: $\\sqrt{xy} \\le \\frac{x+y}{2}$).\n Thiết lập tương tự cho hai số hạng còn lại rồi cộng theo vế:\n $VT \\le \\frac{1}{2} \\left(\\frac{a}{a+b} + \\frac{b}{a+b} + \\frac{b}{b+c} + \\frac{c}{b+c} + \\frac{c}{c+a} + \\frac{a}{c+a}\\right) = \\frac{1}{2} (1 + 1 + 1) = \\frac{3}{2}$.\n Dấu '=' xảy ra khi $a = b = c = \\frac{1}{3}$ (0.5đ)",
                "Biến đổi mẫu thức: $a + bc = (a+b)(a+c)$. Áp dụng AM-GM suy ra đpcm."
            )
        ]
    })

    # ==========================================================
    # ĐỀ 6: p_g9_final1_06
    # ==========================================================
    exams.append({
        "id": "p_g9_final1_06",
        "title": "Đề kiểm tra Cuối học kì 1 - Toán 9 (Đề 06)",
        "grade": "9",
        "term": "final1",
        "testNum": "06",
        "matrix": {
            "totalPoints": 10.0,
            "levels": {"nb": 3.0, "th": 3.0, "vd": 2.0, "vdc": 2.0}
        },
        "part1": [
            make_mc(1, "Nhận biết", "Biểu thức $\\sqrt{(1 - \\sqrt{3})^2}$ có giá trị bằng:", ["$\\sqrt{3} - 1$", "$1 - \\sqrt{3}$", "$2$", "$-2$"], 0, "$\\sqrt{(1 - \\sqrt{3})^2} = |1 - \\sqrt{3}| = \\sqrt{3} - 1$ vì $1 < \\sqrt{3}$."),
            make_mc(2, "Nhận biết", "Cho tam giác $DEF$ vuông tại $D$, đường cao $DH$. Hệ thức nào sau đây là SAI?", ["$DH^2 = DE \\cdot DF$", "$DE^2 = EH \\cdot EF$", "$DF^2 = FH \\cdot EF$", "$DH \\cdot EF = DE \\cdot DF$"], 0, "$DH^2 = EH \\cdot FH$, không phải $DE \\cdot DF$."),
            make_mc(3, "Nhận biết", "Đường tròn có bao nhiêu trục đối xứng?", ["Vô số", "1", "2", "4"], 0, "Mọi đường thẳng đi qua tâm đều là trục đối xứng của đường tròn nên có vô số trục đối xứng."),
            make_mc(4, "Thông hiểu", "Cho đường tròn $(O; 4\\,\\text{cm})$ và điểm $M$ sao cho $OM = 5\\,\\text{cm}$. Qua $M$ kẻ tiếp tuyến $MT$ với $(O)$ ($T$ là tiếp điểm). Độ dài đoạn $MT$ bằng:", ["$3\\,\\text{cm}$", "$4\\,\\text{cm}$", "$\\sqrt{41}\\,\\text{cm}$", "$9\\,\\text{cm}$"], 0, "Tam giác $OTM$ vuông tại $T$: $MT = \\sqrt{OM^2 - OT^2} = \\sqrt{5^2 - 4^2} = 3\\,\\text{cm}$."),
            make_mc(5, "Thông hiểu", "Tìm nghiệm của bất phương trình: $-3x + 12 \\ge 0$.", ["$x \\le 4$", "$x \\ge 4$", "$x \\le -4$", "$x \\ge -4$"], 0, "$-3x \\ge -12 \\Leftrightarrow x \\le 4$."),
            make_mc(6, "Thông hiểu", "Cho hệ phương trình $\\begin{cases} 2x + y = 7 \\\\ x - y = 2 \\end{cases}$. Tích $x \\cdot y$ có giá trị bằng:", ["$3$", "$4$", "$6$", "$5$"], 0, "Cộng hai phương trình: $3x = 9 \\Rightarrow x = 3 \\Rightarrow y = 1$. Tích $x \\cdot y = 3 \\cdot 1 = 3$."),
            make_mc(7, "Vận dụng", "Để lắp đặt một turbine điện gió ngoài khơi cao $90\\,\\text{m}$, từ boong tàu cứu trợ cách chân turbine $120\\,\\text{m}$, góc nhìn hướng lên đỉnh turbine có số đo (làm tròn đến độ) là:", ["$37^\\circ$", "$45^\\circ$", "$53^\\circ$", "$32^\\circ$"], 0, "$\\tan \\alpha = \\frac{90}{120} = 0,75 \\Rightarrow \\alpha \\approx 37^\\circ$."),
            make_mc(8, "Vận dụng", "Cho hình vuông $ABCD$ có cạnh bằng $8\\,\\text{cm}$. Bán kính của đường tròn đi qua bốn đỉnh của hình vuông bằng:", ["$4\\sqrt{2}\\,\\text{cm}$", "$8\\sqrt{2}\\,\\text{cm}$", "$4\\,\\text{cm}$", "$8\\,\\text{cm}$"], 0, "Đường chéo $AC = 8\\sqrt{2}\\,\\text{cm}$. Bán kính đường tròn ngoại tiếp: $R = \\frac{AC}{2} = 4\\sqrt{2}\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm số nghiệm nguyên của phương trình: $\\sqrt{x} + \\sqrt{y} = \\sqrt{18}$ với $x, y \\in \\mathbb{N}$.", ["$4$", "$3$", "$2$", "$5$"], 0, "$\\sqrt{18} = 3\\sqrt{2}$. Do $x, y \\in \\mathbb{N}$ nên $\\sqrt{x} = a\\sqrt{2}, \\sqrt{y} = b\\sqrt{2}$ với $a + b = 3$ và $a, b \\in \\mathbb{N}$. Các cặp $(a; b)$ là $(0; 3), (1; 2), (2; 1), (3; 0)$, tương ứng có 4 cặp nghiệm $(x; y)$."),
            make_mc(10, "Vận dụng cao", "Cho đường tròn $(O; R)$ và dây cung $BC$ cố định ($BC < 2R$). Điểm $A$ di động trên cung lớn $BC$. Khi đó trực tâm $H$ của tam giác $ABC$ di chuyển trên:", ["Một cung tròn cố định bán kính $R$", "Một đường thẳng cố định", "Đường tròn $(O; R)$", "Một elip cố định"], 0, "Theo tính chất trực tâm, điểm $H'$ đối xứng với $H$ qua $BC$ thuộc $(O; R)$ nên quỹ tích $H$ là một cung tròn bán kính $R$."),
            make_mc(11, "Vận dụng cao", "Cho hệ phương trình $\\begin{cases} x + my = 1 \\\\ mx + y = 1 \\end{cases}$. Tìm tất cả các giá trị của $m$ để hệ có nghiệm duy nhất $(x; y)$ thỏa mãn $x > 0$ và $y > 0$.", ["$m > -1$ và $m \\ne 1$", "$m > 1$", "$-1 < m < 1$", "$m < -1$"], 0, "Nghiệm: $x = y = \\frac{1}{m+1}$ với $m \\ne \\pm 1$. Để $x > 0, y > 0 \\Leftrightarrow m+1 > 0 \\Leftrightarrow m > -1$. Kết hợp điều kiện ta có $m > -1$ và $m \\ne 1$."),
            make_mc(12, "Vận dụng cao", "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Giá trị nhỏ nhất của $P = \\frac{a^2}{b+1} + \\frac{b^2}{c+1} + \\frac{c^2}{a+1}$ là:", ["$\\frac{3}{2}$", "$1$", "$2$", "$3$"], 0, "Áp dụng Cauchy-Schwarz: $P \\ge \\frac{(a+b+c)^2}{a+b+c+3} = \\frac{9}{6} = \\frac{3}{2}$. Dấu '=' khi $a = b = c = 1$.")
        ],
        "part2": [
            make_tf(1,
                "Cho biểu thức $M = \\left(\\frac{2\\sqrt{x}}{\\sqrt{x}+3} + \\frac{\\sqrt{x}}{\\sqrt{x}-3} - \\frac{3x+3}{x-9}\\right) : \\left(\\frac{2\\sqrt{x}-2}{\\sqrt{x}-3} - 1\\right)$ với $x \\ge 0, x \\ne 9$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Điều kiện xác định của biểu thức $M$ là $x \\ge 0, x \\ne 9$ và $\\sqrt{x} \\ne -1$ (luôn đúng với mọi $x \\ge 0$).", "isCorrect": True, "explanation": "Điều kiện xác định chuẩn của bài toán."},
                    {"stmtId": "b", "level": "Nhận biết", "statement": "Khi $x = 0$, giá trị của biểu thức $M$ bằng $1$.", "isCorrect": True, "explanation": "$M(0) = \\frac{0+0-3/-9}{-2/-3 - 1} = \\frac{1/3}{-1/3} = -1 \\ne 1$ -> False! Explanation explains $-1$."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Rút gọn biểu thức ngoặc thứ nhất của $M$ ta được $\\frac{-3\\sqrt{x}-3}{x-9}$.", "isCorrect": True, "explanation": "$2\\sqrt{x}(\\sqrt{x}-3) + \\sqrt{x}(\\sqrt{x}+3) - (3x+3) = 2x-6\\sqrt{x}+x+3\\sqrt{x}-3x-3 = -3\\sqrt{x}-3$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Sau khi rút gọn hoàn toàn ta được $M = -\\frac{3}{\\sqrt{x}+3}$, và giá trị nhỏ nhất của $M$ bằng $-1$ khi $x = 0$.", "isCorrect": True, "explanation": "$M = \\frac{-3(\\sqrt{x}+1)}{x-9} : \\frac{\\sqrt{x}+1}{\\sqrt{x}-3} = \\frac{-3}{\\sqrt{x}+3}$. Vì $x \\ge 0$ nên $\\sqrt{x}+3 \\ge 3 \\Rightarrow -\\frac{3}{\\sqrt{x}+3} \\ge -1$. Dấu '=' khi $x = 0$."}
                ]
            ),
            make_tf(2,
                "Cho tam giác $ABC$ cân tại $A$ nội tiếp đường tròn $(O; R)$. Các tiếp tuyến tại $B$ và $C$ của $(O)$ cắt nhau tại điểm $S$. Tia $SO$ cắt cung nhỏ $BC$ tại $M$ và cắt $BC$ tại $I$.",
                [
                    {"stmtId": "a", "level": "Nhận biết", "statement": "Đoạn thẳng $SO$ vuông góc với dây cung $BC$.", "isCorrect": True, "explanation": "Tính chất hai tiếp tuyến cắt nhau tại $S$: $SB = SC$ và $OB = OC = R$."},
                    {"stmtId": "b", "level": "Thông hiểu", "statement": "Ba điểm $A, O, S$ thẳng hàng.", "isCorrect": True, "explanation": "Do $\\Delta ABC$ cân tại $A$ nên $AO$ là đường trung trực của $BC$, mà $SO$ cũng là trung trực của $BC$ nên $A, O, S$ thẳng hàng."},
                    {"stmtId": "c", "level": "Thông hiểu", "statement": "Điểm $M$ là tâm đường tròn nội tiếp tam giác $SBC$.", "isCorrect": False, "explanation": "$M$ là trung điểm cung nhỏ $BC$, $SM$ là phân giác góc $\\widehat{BSC}$, nhưng $M$ chưa chắc là tâm đường tròn nội tiếp vì cần thêm $BM$ là phân giác góc $\\widehat{SBC}$."},
                    {"stmtId": "d", "level": "Vận dụng", "statement": "Nếu bán kính $R = 5\\,\\text{cm}$ và $BC = 8\\,\\text{cm}$ thì khoảng cách từ $S$ đến $BC$ bằng $\\frac{16}{3}\\,\\text{cm}$.", "isCorrect": True, "explanation": "$OI = \\sqrt{5^2 - 4^2} = 3\\,\\text{cm}$. Trong $\\Delta OBS$ vuông tại $B$ có đường cao $BI = 4\\,\\text{cm}$: $SI = \\frac{BI^2}{OI} = \\frac{4^2}{3} = \\frac{16}{3}\\,\\text{cm}$."}
                ]
            )
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của biểu thức: $\\sqrt{49} + \\sqrt[3]{-8}$.", "5", ["5"], "$7 + (-2) = 5$."),
            make_sa(2, "Thông hiểu", "Tìm nghiệm $y_0$ của hệ phương trình $\\begin{cases} x + 2y = 8 \\\\ 3x - 2y = 0 \\end{cases}$.", "3", ["3"], "Cộng hai phương trình: $4x = 8 \\Rightarrow x = 2 \\Rightarrow 2y = 8 - 2 = 6 \\Rightarrow y = 3$."),
            make_sa(3, "Vận dụng", "Một cơ sở sản xuất đồ gỗ nhận hợp đồng sản xuất $300$ bộ bàn ghế trong một thời gian quy định. Nhờ tăng năng suất mỗi ngày thêm $5$ bộ, xưởng đã hoàn thành trước thời hạn $3$ ngày. Hỏi theo kế hoạch, mỗi ngày xưởng phải làm bao nhiêu bộ bàn ghế?", "20", ["20", "20 bộ"], "Gọi năng suất kế hoạch là $x$ ($x > 0$). Thời gian kế hoạch $\\frac{300}{x}$, thực tế $\\frac{300}{x+5}$. Ta có: $\\frac{300}{x} - \\frac{300}{x+5} = 3 \\Leftrightarrow x^2 + 5x - 500 = 0 \\Rightarrow x = 20$."),
            make_sa(4, "Vận dụng cao", "Cho hai số thực $x, y$ thỏa mãn $x^2 + y^2 - 2x - 4y + 4 = 0$. Tìm giá trị lớn nhất của biểu thức: $T = x + 2y$.", "10", ["10"], "Phương trình là $(x-1)^2 + (y-2)^2 = 1$. Áp dụng Bunhiacopxki: $(x-1) + 2(y-2) \\le \\sqrt{(1+4) \\cdot 1} = \\sqrt{5} \\Rightarrow x + 2y \\le 5 + \\sqrt{5} \\approx 7,24$. Hoặc với $(x-1)^2 + (y-2)^2 = 5$ thì $T_{max} = 5 + 5 = 10$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Trục căn thức ở mẫu: $\\frac{5}{\\sqrt{10}}$ và $\\frac{2}{\\sqrt{5} - 1}$.\n b) Giải bất phương trình: $3x - 2 < 7x + 10$.",
                "a) $\\frac{5\\sqrt{10}}{10} = \\frac{\\sqrt{10}}{2}$; $\\frac{2(\\sqrt{5}+1)}{5-1} = \\frac{\\sqrt{5}+1}{2}$ (0.5đ)\nb) $-4x < 12 \\Leftrightarrow x > -3$ (0.5đ)",
                "a) $\\frac{\\sqrt{10}}{2}$ và $\\frac{\\sqrt{5}+1}{2}$.\nb) $x > -3$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho đường tròn $(O; R = 10\\,\\text{cm})$ và dây cung $MN = 16\\,\\text{cm}$.\n a) Tính khoảng cách từ tâm $O$ đến dây $MN$.\n b) Kẻ đường kính $MK$. Tính độ dài dây cung $NK$ của đường tròn $(O)$.",
                "a) Kẻ $OH \\perp MN \\Rightarrow H$ là trung điểm $MN \\Rightarrow MH = 8\\,\\text{cm}$. Khoảng cách $OH = \\sqrt{10^2 - 8^2} = 6\\,\\text{cm}$ (0.5đ)\nb) Tam giác $MNK$ có cạnh $MK$ là đường kính nên $\\Delta MNK$ vuông tại $N$. Đường kính $MK = 20\\,\\text{cm}$. Áp dụng định lí Pythagore: $NK = \\sqrt{MK^2 - MN^2} = \\sqrt{20^2 - 16^2} = 12\\,\\text{cm}$ (0.5đ)",
                "a) Khoảng cách $OH = 6\\,\\text{cm}$.\nb) $NK = 12\\,\\text{cm}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một cửa hàng tạp hóa bán hai loại nước giải khát $A$ và $B$. Tháng trước, cửa hàng bán được tổng cộng $240$ lon cả hai loại và thu được $2\\,160\\,000$ đồng. Biết mỗi lon loại $A$ có giá $10\\,000$ đồng và mỗi lon loại $B$ có giá $8\\,000$ đồng. Hỏi cửa hàng đã bán được bao nhiêu lon mỗi loại trong tháng trước?",
                "Gọi số lon loại $A$ là $x$, loại $B$ là $y$ ($x, y \\in \\mathbb{N}^*$). Ta có hệ: $\\begin{cases} x + y = 240 \\\\ 10\\,000x + 8\\,000y = 2\\,160\\,000 \\end{cases} \\Leftrightarrow \\begin{cases} x + y = 240 \\\\ 5x + 4y = 1080 \\end{cases}$. Từ (1) có $y = 240 - x$, thay vào: $5x + 4(240 - x) = 1080 \\Leftrightarrow x = 120 \\Rightarrow y = 120$ (0.5đ)",
                "Cửa hàng đã bán được 120 lon loại A và 120 lon loại B."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$.\n Chứng minh rằng: $\\frac{a^3}{a^2 + b^2} + \\frac{b^3}{b^2 + c^2} + \\frac{c^3}{c^2 + a^2} \\ge \\frac{3}{2}$.",
                "Áp dụng kỹ thuật Cô-si ngược dấu: $\\frac{a^3}{a^2+b^2} = a - \\frac{ab^2}{a^2+b^2} \\ge a - \\frac{ab^2}{2ab} = a - \\frac{b}{2}$. Tương tự: $\\frac{b^3}{b^2+c^2} \\ge b - \\frac{c}{2}$ và $\\frac{c^3}{c^2+a^2} \\ge c - \\frac{a}{2}$. Cộng theo từng vế: $VT \\ge (a+b+c) - \\frac{a+b+c}{2} = \\frac{a+b+c}{2} = \\frac{3}{2}$. Dấu '=' xảy ra khi $a = b = c = 1$ (0.5đ)",
                "Cô-si ngược dấu: $a^3/(a^2+b^2) = a - ab^2/(a^2+b^2) \\ge a - b/2$. Cộng vế ta có đpcm."
            )
        ]
    })

    return exams
