# -*- coding: utf-8 -*-
"""
BỘ ĐỀ THI ĐỊNH KỲ TOÁN 7 - HỌC KỲ I (GIỮA KỲ 1 & CUỐI KỲ 1)
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
# 6 MÃ ĐỀ GIỮA KỲ 1 - TOÁN 7 (mid1)
# Phạm vi: Số hữu tỉ, Số thực, Căn bậc hai, Góc ở vị trí đặc biệt & Hai đường thẳng song song.
# ==============================================================================
def generate_g7_mid1():
    exams = []

    # ------------------ ĐỀ SỐ 01 ------------------
    # Ngữ cảnh: Đo đạc công trình xây dựng cầu đường, tính toán nhiệt độ, tỉ lệ pha chế sơn
    exams.append({
        "id": "p_g7_mid1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 01)",
        "topic": "Số hữu tỉ, Căn bậc hai số học, Góc đối đỉnh, Tia phân giác & Đường thẳng song song",
        "grade": "7",
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
            make_mc(1, "Nhận biết", "Số đối của số hữu tỉ $-\\frac{3}{7}$ là:", ["$\\frac{3}{7}$", "$-\\frac{7}{3}$", "$\\frac{7}{3}$", "$-\\frac{3}{-7}$"], 0, "Số đối của $-a/b$ là $a/b$."),
            make_mc(2, "Nhận biết", "Căn bậc hai số học của 49 là:", ["$7$", "$-7$", "$\\pm 7$", "$49$"], 0, "Căn bậc hai số học của 49 là $\\sqrt{49} = 7$."),
            make_mc(3, "Nhận biết", "Hai góc đối đỉnh thì:", ["Bằng nhau", "Có tổng bằng $180^\\circ$", "Kề nhau", "Phụ nhau"], 0, "Tính chất: Hai góc đối đỉnh thì bằng nhau."),
            make_mc(4, "Thông hiểu", "Kết quả của phép tính $\\left(-\\frac{2}{3}\\right)^3$ bằng:", ["$-\\frac{8}{27}$", "$\\frac{8}{27}$", "$-\\frac{6}{9}$", "$\\frac{6}{9}$"], 0, "$\\left(-\\frac{2}{3}\\right)^3 = \\frac{(-2)^3}{3^3} = -\\frac{8}{27}$."),
            make_mc(5, "Thông hiểu", "Cho hai đường thẳng $a$ và $b$ song song với nhau. Đường thẳng $c$ cắt cả $a$ và $b$. Biết một góc so le trong bằng $65^\\circ$. Góc so le trong còn lại có số đo là:", ["$65^\\circ$", "$115^\\circ$", "$25^\\circ$", "$180^\\circ$"], 0, "Nếu hai đường thẳng song song thì hai góc so le trong bằng nhau, nên góc đó bằng $65^\\circ$."),
            make_mc(6, "Thông hiểu", "Làm tròn số $3,14159$ đến chữ số thập phân thứ hai (hàng phần trăm) ta được:", ["$3,14$", "$3,15$", "$3,1$", "$3,142$"], 0, "Chữ số ngay sau hàng phần trăm là 1 (< 5) nên giữ nguyên: $3,14$."),
            make_mc(7, "Vận dụng", "Một người thợ may dùng $2\\frac{1}{4}\\,\\text{m}$ vải để may một chiếc áo sơ mi nam và dùng $1\\frac{1}{2}\\,\\text{m}$ vải để may một chiếc quần âu. Để may 4 bộ trang phục như thế cần tất cả bao nhiêu mét vải?", ["$15\\,\\text{m}$", "$14\\,\\text{m}$", "$16\\,\\text{m}$", "$18\\,\\text{m}$"], 0, "Một bộ cần: $2,25 + 1,5 = 3,75\\,\\text{m}$. Bốn bộ cần: $3,75 \\cdot 4 = 15\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Cho hình vẽ biết $xx' // yy'$. Tia phân giác của góc nhọn $\\widehat{xAB} = 70^\\circ$ cắt đường thẳng $yy'$ tại $C$. Số đo của góc $\\widehat{ABC}$ là:", ["$35^\\circ$", "$70^\\circ$", "$110^\\circ$", "$55^\\circ$"], 0, "Tia phân giác chia góc thành hai góc $35^\\circ$. Do so le trong nên $\\widehat{ABC} = 35^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức $P = |x - 2024| + |x - 1|$.", ["$2023$", "$2024$", "$2025$", "$0$"], 0, "Áp dụng BĐT $|a| + |b| \\ge |a + b|$: $P = |2024 - x| + |x - 1| \\ge |2024 - x + x - 1| = 2023$."),
            make_mc(10, "Vận dụng cao", "Tìm số hữu tỉ $x$ biết: $\\left(x - \\frac{1}{2}\\right)^2 = \\frac{4}{9}$.", ["$x \\in \\left\\{\\frac{7}{6}; -\\frac{1}{6}\\right\\}$", "$x = \\frac{7}{6}$", "$x = -\\frac{1}{6}$", "$x \\in \\left\\{\\frac{5}{6}; -\\frac{1}{6}\\right\\}$"], 0, "$x - 1/2 = 2/3 \\Rightarrow x = 7/6$; $x - 1/2 = -2/3 \\Rightarrow x = -1/6$."),
            make_mc(11, "Vận dụng cao", "So sánh hai số $A = 2^{300}$ và $B = 3^{200}$ ta có kết quả là:", ["$A < B$", "$A > B$", "$A = B$", "Không so sánh được"], 0, "$A = (2^3)^{100} = 8^{100}$; $B = (3^2)^{100} = 9^{100}$. Vì $8 < 9$ nên $A < B$."),
            make_mc(12, "Vận dụng cao", "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$. Tia $Om$ là tia phân giác của $\\widehat{xOy}$, tia $On$ là tia phân giác của $\\widehat{yOz}$. Số đo của góc $\\widehat{mOn}$ bằng:", ["$90^\\circ$", "$180^\\circ$", "$60^\\circ$", "$45^\\circ$"], 0, "Hai tia phân giác của hai góc kề bù luôn vuông góc với nhau, tạo thành góc $90^\\circ$.")
        ],
        "part2": [
            make_tf(1, "Cho biểu thức $A = \\left(-\\frac{3}{4}\\right) \\cdot \\frac{8}{15} + \\frac{2}{5}$ và số thực $x = \\sqrt{16} - 3$.", [
                {"id": "a", "text": "Căn bậc hai số học của 16 bằng 4.", "correct": True, "level": "Nhận biết", "explanation": "$\\sqrt{16} = 4$."},
                {"id": "b", "text": "Giá trị của $x$ bằng 1.", "correct": True, "level": "Nhận biết", "explanation": "$x = 4 - 3 = 1$."},
                {"id": "c", "text": "Giá trị của biểu thức $A$ bằng 0.", "correct": True, "level": "Thông hiểu", "explanation": "$A = -\\frac{2}{5} + \\frac{2}{5} = 0$."},
                {"id": "d", "text": "Biểu thức $M = \\frac{x}{A}$ nhận một giá trị hữu tỉ xác định.", "correct": False, "level": "Vận dụng", "explanation": "Do mẫu số $A = 0$ nên phép chia $\\frac{x}{A}$ không xác định."}
            ]),
            make_tf(2, "Cho hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $c$ tại hai điểm phân biệt $A$ và $B$. Một đường thẳng $d$ cắt $a$ tại $M$ và cắt $b$ tại $N$ sao cho $\\widehat{AMN} = 120^\\circ$.", [
                {"id": "a", "text": "Hai đường thẳng $a$ và $b$ song song với nhau.", "correct": True, "level": "Nhận biết", "explanation": "Hai đường thẳng phân biệt cùng vuông góc với đường thẳng thứ ba thì song song với nhau."},
                {"id": "b", "text": "Góc kề bù với góc $\\widehat{AMN}$ có số đo bằng $60^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "$180^\\circ - 120^\\circ = 60^\\circ$."},
                {"id": "c", "text": "Góc so le trong với $\\widehat{AMN}$ tại đỉnh $N$ có số đo bằng $120^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Do $a // b$ nên hai góc so le trong bằng nhau, cùng bằng $120^\\circ$."},
                {"id": "d", "text": "Tổng số đo hai góc trong cùng phía tại $M$ và $N$ bằng $200^\\circ$.", "correct": False, "level": "Vận dụng", "explanation": "Hai góc trong cùng phía của hai đường thẳng song song có tổng số đo bù nhau, tức bằng $180^\\circ$, không phải $200^\\circ$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Viết số đối của số hữu tỉ $2,75$ dưới dạng phân số tối giản a/b.", "-11/4", ["-11/4", "-11 / 4"], "$2,75 = 11/4 \\Rightarrow$ số đối là $-11/4$."),
            make_sa(2, "Thông hiểu", "Tính giá trị của biểu thức: $\\sqrt{\\frac{25}{36}} - \\frac{1}{6}$.", "2/3", ["2/3", "4/6"], "$\\frac{5}{6} - \\frac{1}{6} = \\frac{4}{6} = \\frac{2}{3}$."),
            make_sa(3, "Vận dụng", "Bác An gửi tiết kiệm ngân hàng số tiền 100 triệu đồng kì hạn 12 tháng với lãi suất $6\\%/\\text{năm}$. Sau đúng một năm, bác rút toàn bộ cả vốn lẫn lãi và dùng $\\frac{1}{2}$ số tiền đó để mua một chiếc máy giặt cao cấp. Hỏi sau khi mua máy giặt bác An còn lại bao nhiêu triệu đồng?", "53", ["53", "53 triệu đồng"], "Tiền lãi: $100 \\cdot 6\\% = 6$ triệu. Cả vốn lẫn lãi: 106 triệu. Mua máy giặt hết: $106 : 2 = 53$ triệu. Còn lại: 53 triệu đồng."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị của $x$ biết: $\\frac{x - 1}{2024} + \\frac{x - 2}{2023} = \\frac{x - 3}{2022} + \\frac{x - 4}{2021}$.", "2025", ["2025"], "Trừ 1 vào mỗi phân thức: $\\frac{x - 2025}{2024} + \\frac{x - 2025}{2023} - \\frac{x - 2025}{2022} - \\frac{x - 2025}{2021} = 0 \\Rightarrow x = 2025$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý nhất:\n a) $A = \\frac{7}{19} \\cdot \\frac{8}{11} + \\frac{7}{19} \\cdot \\frac{3}{11} - \\frac{7}{19}$\n b) $B = \\sqrt{25} - \\sqrt{0,16} + 1,4$",
                "a) $\\frac{7}{19} \\cdot \\left(\\frac{8}{11} + \\frac{3}{11} - 1\\right) = \\frac{7}{19} \\cdot (1 - 1) = 0$ (0.5đ)\nb) $5 - 0,4 + 1,4 = 5 + 1 = 6$ (0.5đ)",
                "a) Đặt $\\frac{7}{19}$ làm nhân tử chung: $A = \\frac{7}{19} \\cdot 0 = 0$.\nb) Khai căn rồi cộng trừ số thập phân: $B = 5 - 0,4 + 1,4 = 6$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số thực $x$, biết:\n a) $x + \\frac{3}{4} = \\frac{1}{2}$\n b) $|x - 1,5| = 2,5$",
                "a) $x = \\frac{1}{2} - \\frac{3}{4} = -\\frac{1}{4}$ (0.5đ)\nb) $x - 1,5 = 2,5 \\Rightarrow x = 4$ hoặc $x - 1,5 = -2,5 \\Rightarrow x = -1$ (0.5đ)",
                "a) $x = 1/2 - 3/4 = -1/4$.\nb) Xét 2 trường hợp giá trị tuyệt đối: $x = 4$ hoặc $x = -1$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Cho hình vẽ có $Ax // By$. Biết góc $\\widehat{xAB} = 130^\\circ$ và $\\widehat{OBy} = 140^\\circ$ (với điểm $O$ nằm giữa hai đường thẳng sao cho tia $OA, OB$ tạo thành góc nhọn $\\widehat{AOB}$).\n a) Kẻ qua $O$ đường thẳng $Ot // Ax$. Tính số đo các góc $\\widehat{AOt}$ và $\\widehat{BOt}$.\n b) Tính số đo góc $\\widehat{AOB}$.",
                "a) Vì $Ot // Ax$ nên $\\widehat{xAO} + \\widehat{AOt} = 180^\\circ$ (trong cùng phía) $\\Rightarrow \\widehat{AOt} = 180^\\circ - 130^\\circ = 50^\\circ$. Tương tự $Ot // By \\Rightarrow \\widehat{BOt} = 180^\\circ - 140^\\circ = 40^\\circ$ (0.25đ)\nb) Tia $Ot$ nằm giữa $OA$ và $OB$ nên $\\widehat{AOB} = \\widehat{AOt} + \\widehat{BOt} = 50^\\circ + 40^\\circ = 90^\\circ$ (0.25đ)",
                "a) Dùng tính chất hai góc trong cùng phía tính được $\\widehat{AOt} = 50^\\circ$ và $\\widehat{BOt} = 40^\\circ$.\nb) Cộng góc suy ra $\\widehat{AOB} = 90^\\circ$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực $a, b, c$ khác 0 thỏa mãn $\\frac{a + b - c}{c} = \\frac{b + c - a}{a} = \\frac{c + a - b}{b}$.\n Tính giá trị của biểu thức $M = \\left(1 + \\frac{b}{a}\\right)\\left(1 + \\frac{c}{b}\\right)\\left(1 + \\frac{a}{c}\\right)$.",
                "Cộng 1 vào mỗi tỉ số: $\\frac{a+b}{c} = \\frac{b+c}{a} = \\frac{c+a}{b}$.\n- TH1: $a + b + c \\neq 0$. Theo tính chất dãy tỉ số bằng nhau: $\\frac{a+b}{c} = \\frac{b+c}{a} = \\frac{c+a}{b} = \\frac{2(a+b+c)}{a+b+c} = 2$. Suy ra $a+b = 2c, b+c = 2a, c+a = 2b \\Rightarrow a = b = c$. Khi đó $M = (1+1)(1+1)(1+1) = 8$.\n- TH2: $a + b + c = 0 \\Rightarrow a + b = -c, b + c = -a, c + a = -b$. Khi đó $M = \\frac{a+b}{a} \\cdot \\frac{b+c}{b} \\cdot \\frac{c+a}{c} = \\frac{-c}{a} \\cdot \\frac{-a}{b} \\cdot \\frac{-b}{c} = -1$.\nVậy $M = 8$ hoặc $M = -1$ (0.5đ)",
                "Cộng 1 vào mỗi tỉ số, xét hai trường hợp $a+b+c \\neq 0$ (suy ra $M = 8$) và $a+b+c = 0$ (suy ra $M = -1$)."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 02 ------------------
    # Ngữ cảnh: Chuyển động ô tô cao tốc Bắc - Nam, cước viễn thông, hai thanh ray xe lửa song song
    exams.append({
        "id": "p_g7_mid1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 02)",
        "topic": "Phép tính số hữu tỉ, Số vô tỉ, Góc so le trong & Tiên đề Euclid",
        "grade": "7",
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
            make_mc(1, "Nhận biết", "Trong các số sau, số nào là số vô tỉ?", ["$\\sqrt{2}$", "$\\frac{2}{3}$", "$-0,75$", "$\\sqrt{9}$"], 0, "$\\sqrt{2}$ là số thập phân vô hạn không tuần hoàn nên là số vô tỉ."),
            make_mc(2, "Nhận biết", "Giá trị tuyệt đối của số thực $-3,8$ là:", ["$3,8$", "$-3,8$", "$\\pm 3,8$", "$0$"], 0, "$|-3,8| = 3,8$."),
            make_mc(3, "Nhận biết", "Qua một điểm $M$ nằm ngoài đường thẳng $a$, có bao nhiêu đường thẳng song song với đường thẳng $a$?", ["Duy nhất 1", "2", "Vô số", "Không có"], 0, "Theo Tiên đề Euclid: Qua một điểm ở ngoài một đường thẳng, chỉ có một đường thẳng song song với đường thẳng đó."),
            make_mc(4, "Thông hiểu", "Thực hiện phép tính $\\frac{3}{5} - \\frac{1}{2} : \\frac{5}{4}$ ta được kết quả là:", ["$\\frac{1}{5}$", "$-\\frac{1}{5}$", "$\\frac{2}{5}$", "$\\frac{7}{10}$"], 0, "$\\frac{3}{5} - \\frac{1}{2} \\cdot \\frac{4}{5} = \\frac{3}{5} - \\frac{2}{5} = \\frac{1}{5}$."),
            make_mc(5, "Thông hiểu", "Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc đồng vị:", ["Bằng nhau", "Bù nhau", "Kề bù", "Phụ nhau"], 0, "Tính chất của hai đường thẳng song song: Hai góc đồng vị thì bằng nhau."),
            make_mc(6, "Thông hiểu", "Tìm $x$ biết $x^2 = 25$ và $x > 0$:", ["$x = 5$", "$x = -5$", "$x = \\pm 5$", "$x = 25$"], 0, "$x = \\sqrt{25} = 5$ vì $x > 0$."),
            make_mc(7, "Vận dụng", "Một ô tô chạy trên cao tốc với vận tốc không đổi $85,5\\,\\text{km/h}$. Quãng đường ô tô đó đi được sau $2\\frac{1}{3}$ giờ (làm tròn kết quả đến hàng đơn vị) là:", ["$200\\,\\text{km}$", "$199\\,\\text{km}$", "$201\\,\\text{km}$", "$198\\,\\text{km}$"], 0, "$S = 85,5 \\cdot \\frac{7}{3} = 28,5 \\cdot 7 = 199,5\\,\\text{km} \\approx 200\\,\\text{km}$."),
            make_mc(8, "Vận dụng", "Cho góc $\\widehat{xOy} = 80^\\circ$. Tia $Oz$ là tia phân giác của góc $\\widehat{xOy}$. Kẻ tia $Ot$ đối diện với tia $Ox$. Số đo góc $\\widehat{zOt}$ bằng:", ["$140^\\circ$", "$100^\\circ$", "$120^\\circ$", "$40^\\circ$"], 0, "$\\widehat{xOz} = 40^\\circ$. $\\widehat{zOt}$ kề bù với $\\widehat{xOz}$ nên bằng $180^\\circ - 40^\\circ = 140^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên $x$ sao cho biểu thức $A = \\frac{7}{x - 3}$ đạt giá trị nguyên lớn nhất.", ["$x = 4$", "$x = 10$", "$x = 2$", "$x = -4$"], 0, "Để $A$ nguyên lớn nhất thì $x - 3$ phải là ước nguyên dương nhỏ nhất của 7 $\\Rightarrow x - 3 = 1 \\Rightarrow x = 4$."),
            make_mc(10, "Vận dụng cao", "Tìm số thực $x$ thỏa mãn: $|2x - 3| + |1 - x| = 0$.", ["Không tồn tại $x$", "$x = 1,5$", "$x = 1$", "$x = 0$"], 0, "Tổng hai giá trị tuyệt đối bằng 0 khi cả hai cùng bằng 0: $2x - 3 = 0 \\Rightarrow x = 1,5$ và $1 - x = 0 \\Rightarrow x = 1$ (mâu thuẫn). Vậy không có $x$ thỏa mãn."),
            make_mc(11, "Vận dụng cao", "Cho $2^{x-1} = 16$. Giá trị của $3^x$ là:", ["$243$", "$81$", "$27$", "$729$"], 0, "$2^{x-1} = 2^4 \\Rightarrow x - 1 = 4 \\Rightarrow x = 5 \\Rightarrow 3^5 = 243$."),
            make_mc(12, "Vận dụng cao", "Cho ba đường thẳng $a, b, c$ phân biệt. Biết $a // b$ và $b \\perp c$. Khẳng định nào sau đây đúng?", ["$a \\perp c$", "$a // c$", "$a$ trùng $c$", "$a$ chéo $c$"], 0, "Một đường thẳng vuông góc với một trong hai đường thẳng song song thì cũng vuông góc với đường thẳng kia.")
        ],
        "part2": [
            make_tf(1, "Một bồn chứa nước sạch có dung tích $1200$ lít. Mỗi giờ vòi thứ nhất chảy vào được $180,5$ lít nước, vòi thứ hai tháo ra dùng cho tưới rau hết $80,5$ lít nước.", [
                {"id": "a", "text": "Sau mỗi giờ, lượng nước thực tế tăng thêm trong bồn là $100$ lít.", "correct": True, "level": "Nhận biết", "explanation": "$180,5 - 80,5 = 100$ lít/giờ."},
                {"id": "b", "text": "Số 100 là một số hữu tỉ dương.", "correct": True, "level": "Nhận biết", "explanation": "100 viết được dưới dạng 100/1 nên là số hữu tỉ dương."},
                {"id": "c", "text": "Nếu ban đầu bồn không có nước thì sau 8 giờ lượng nước trong bồn là 800 lít.", "correct": True, "level": "Thông hiểu", "explanation": "$8 \\cdot 100 = 800$ lít."},
                {"id": "d", "text": "Để bơm đầy hoàn toàn bồn nước cần đúng 10 giờ.", "correct": False, "level": "Vận dụng", "explanation": "Thời gian đầy bồn là $1200 : 100 = 12$ giờ, không phải 10 giờ."}
            ]),
            make_tf(2, "Cho hình vẽ có hai đường thẳng $AB$ và $CD$ song song với nhau. Đường thẳng cát tuyến $EF$ cắt $AB$ tại $E$ và cắt $CD$ tại $F$ sao cho góc $\\widehat{BEF} = 75^\\circ$.", [
                {"id": "a", "text": "Hai góc $\\widehat{AEF}$ và $\\widehat{BEF}$ là hai góc kề bù.", "correct": True, "level": "Nhận biết", "explanation": "Hai góc có chung cạnh $EF$ và hai cạnh còn lại là hai tia đối nhau."},
                {"id": "b", "text": "Số đo góc $\\widehat{AEF}$ bằng $105^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "$180^\\circ - 75^\\circ = 105^\\circ$."},
                {"id": "c", "text": "Góc so le trong với $\\widehat{BEF}$ tại đỉnh $F$ có số đo bằng $75^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Do $AB // CD$ nên hai góc so le trong bằng nhau."},
                {"id": "d", "text": "Tia phân giác của hai góc so le trong $\\widehat{BEF}$ và $\\widehat{EFC}$ vuông góc với nhau.", "correct": False, "level": "Vận dụng", "explanation": "Hai tia phân giác của hai góc so le trong song song với nhau, không phải vuông góc."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm số đối của số thực $-\\sqrt{5}$.", "sqrt(5)", ["sqrt(5)", "\\sqrt{5}", "căn 5"], "Số đối của $-\\sqrt{5}$ là $\\sqrt{5}$."),
            make_sa(2, "Thông hiểu", "Tìm số hữu tỉ $x$, biết: $x - \\frac{2}{3} = -\\frac{1}{6}$.", "1/2", ["1/2", "0.5"], "$x = -1/6 + 2/3 = 3/6 = 1/2$."),
            make_sa(3, "Vận dụng", "Một khu vườn hình vuông có diện tích bằng $144\\,\\text{m}^2$. Bác chủ vườn muốn mua lưới B40 để rào xung quanh khu vườn, chừa lại một cổng đi rộng $2,5\\,\\text{m}$. Chiều dài lưới thép B40 cần mua là bao nhiêu mét?", "45.5", ["45.5", "45,5"], "Cạnh khu vườn là $\\sqrt{144} = 12\\,\\text{m}$. Chu vi $= 12 \\cdot 4 = 48\\,\\text{m}$. Chiều dài lưới $= 48 - 2,5 = 45,5\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm số thực $x$ không âm thỏa mãn: $\\sqrt{x + 3} = 5$.", "22", ["22"], "Bình phương hai vế: $x + 3 = 25 \\Rightarrow x = 22$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý nhất:\n a) $\\frac{4}{7} \\cdot \\frac{3}{5} + \\frac{4}{7} \\cdot \\frac{2}{5} - \\frac{4}{7}$\n b) $\\left(-\\frac{1}{2}\\right)^2 + \\sqrt{0,64} - \\frac{3}{4}$",
                "a) $\\frac{4}{7} \\cdot \\left(\\frac{3}{5} + \\frac{2}{5} - 1\\right) = \\frac{4}{7} \\cdot 0 = 0$ (0.5đ)\nb) $\\frac{1}{4} + 0,8 - 0,75 = 0,25 + 0,8 - 0,75 = 0,3$ (0.5đ)",
                "a) Đặt $\\frac{4}{7}$ ra ngoài: $A = 0$.\nb) Tính lũy thừa và căn bậc hai: $0,25 + 0,8 - 0,75 = 0,3$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số thực $x$, biết:\n a) $\\frac{2}{3}x - \\frac{1}{2} = \\frac{5}{6}$\n b) $|2x - 1| = 3$",
                "a) $\\frac{2}{3}x = \\frac{4}{3} \\Rightarrow x = 2$ (0.5đ)\nb) $2x - 1 = 3 \\Rightarrow x = 2$ hoặc $2x - 1 = -3 \\Rightarrow x = -1$ (0.5đ)",
                "a) Chuyển vế: $\\frac{2}{3}x = \\frac{4}{3} \\Rightarrow x = 2$.\nb) Xét 2 trường hợp: $x = 2$ hoặc $x = -1$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Cho góc nhọn $\\widehat{xOy} = 60^\\circ$. Trên tia $Ox$ lấy điểm $A$, kẻ tia $Am // Oy$ (sao cho tia $Am$ nằm trong góc $\\widehat{xOy}$).\n a) Tính số đo góc $\\widehat{xAm}$.\n b) Kẻ tia $An$ là tia phân giác của góc $\\widehat{xAm}$. Chứng minh rằng tia $An$ song song với tia phân giác $Oz$ của góc $\\widehat{xOy}$.",
                "a) Vì $Am // Oy$ nên $\\widehat{xAm} = \\widehat{xOy} = 60^\\circ$ (hai góc đồng vị) (0.25đ)\nb) Vì $An$ là phân giác $\\widehat{xAm}$ nên $\\widehat{xAn} = 30^\\circ$. Tia $Oz$ là phân giác $\\widehat{xOy}$ nên $\\widehat{xOz} = 30^\\circ$. Do $\\widehat{xAn} = \\widehat{xOz} = 30^\\circ$ ở vị trí đồng vị nên $An // Oz$ (đpcm) (0.25đ)",
                "a) Do đồng vị nên $\\widehat{xAm} = 60^\\circ$.\nb) Hai góc tạo bởi tia phân giác ở vị trí đồng vị bằng nhau ($30^\\circ$) nên $An // Oz$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm giá trị lớn nhất của biểu thức $Q = \\frac{10}{|x - 2| + 2}$.",
                "Ta có $|x - 2| \\ge 0$ với mọi $x \\in \\mathbb{R}$.\nSuy ra $|x - 2| + 2 \\ge 2$.\nDo đó $Q = \\frac{10}{|x - 2| + 2} \\le \\frac{10}{2} = 5$.\nDấu '=' xảy ra khi và chỉ khi $x - 2 = 0 \\Leftrightarrow x = 2$.\nVậy giá trị lớn nhất của $Q$ bằng 5 khi $x = 2$ (0.5đ)",
                "Đánh giá mẫu số $|x-2|+2 \\ge 2$ với mọi $x$, suy ra phân thức $Q \\le 10/2 = 5$. Đạt cực đại tại $x = 2$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 03 ------------------
    # Ngữ cảnh: Gia công cơ khí chính xác, kiểm tra độ vuông góc góc máy, chia khẩu phần dinh dưỡng
    exams.append({
        "id": "p_g7_mid1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 03)",
        "topic": "Lũy thừa số hữu tỉ, Tập hợp số thực R, Tia phân giác & Hai đường thẳng song song",
        "grade": "7",
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
            make_mc(1, "Nhận biết", "Khẳng định nào sau đây là đúng về tập hợp số thực $\\mathbb{R}$?", ["$\\mathbb{R} = \\mathbb{Q} \\cup \\mathbb{I}$", "$\\mathbb{R} = \\mathbb{Q} \\cap \\mathbb{I}$", "Mọi số thực đều là số hữu tỉ", "Mọi số thực đều là số vô tỉ"], 0, "Tập số thực là hợp của tập số hữu tỉ và tập số vô tỉ: $\\mathbb{R} = \\mathbb{Q} \\cup \\mathbb{I}$."),
            make_mc(2, "Nhận biết", "Tia $Ot$ là tia phân giác của góc $\\widehat{xOy}$ khi:", ["Tia $Ot$ nằm giữa hai tia $Ox, Oy$ và $\\widehat{xOt} = \\widehat{yOt}$", "$\\widehat{xOt} = \\widehat{yOt}$", "Tia $Ot$ nằm giữa hai tia $Ox$ và $Oy$", "$\\widehat{xOt} + \\widehat{tOy} = 180^\\circ$"], 0, "Định nghĩa tia phân giác của một góc."),
            make_mc(3, "Nhận biết", "Kết quả của phép tính $a^m \\cdot a^n$ (với $a \\neq 0; m, n \\in \\mathbb{N}$) là:", ["$a^{m+n}$", "$a^{m-n}$", "$a^{m \\cdot n}$", "$a^{m : n}$"], 0, "$a^m \\cdot a^n = a^{m+n}$."),
            make_mc(4, "Thông hiểu", "Tính giá trị của biểu thức: $\\sqrt{81} - \\sqrt{36}$:", ["$3$", "$9$", "$45$", "$15$"], 0, "$9 - 6 = 3$."),
            make_mc(5, "Thông hiểu", "Cho góc $\\widehat{xOy} = 120^\\circ$. Góc kề bù với $\\widehat{xOy}$ có số đo bằng:", ["$60^\\circ$", "$120^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0, "Hai góc kề bù có tổng số đo bằng $180^\\circ$ nên góc kề bù bằng $180^\\circ - 120^\\circ = 60^\\circ$."),
            make_mc(6, "Thông hiểu", "Viết biểu thức $\\left(\\frac{1}{3}\\right)^5 : \\left(\\frac{1}{3}\\right)^2$ dưới dạng một lũy thừa:", ["$\\left(\\frac{1}{3}\\right)^3$", "$\\left(\\frac{1}{3}\\right)^7$", "$\\left(\\frac{1}{3}\\right)^{10}$", "$\\left(\\frac{1}{9}\\right)^3$"], 0, "$\\left(\\frac{1}{3}\\right)^{5-2} = \\left(\\frac{1}{3}\\right)^3$."),
            make_mc(7, "Vận dụng", "Một tấm kính cường lực hình vuông có diện tích $2,25\\,\\text{m}^2$. Người ta muốn viền nẹp nhôm 4 cạnh xung quanh tấm kính. Tổng chiều dài nẹp nhôm cần dùng là:", ["$6\\,\\text{m}$", "$9\\,\\text{m}$", "$4,5\\,\\text{m}$", "$1,5\\,\\text{m}$"], 0, "Cạnh tấm kính: $\\sqrt{2,25} = 1,5\\,\\text{m}$. Chu vi: $1,5 \\cdot 4 = 6\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Cho hai góc kề nhau $\\widehat{AOB} = 50^\\circ$ và $\\widehat{BOC} = 70^\\circ$. Gọi $OD$ và $OE$ lần lượt là tia phân giác của $\\widehat{AOB}$ và $\\widehat{BOC}$. Số đo góc $\\widehat{DOE}$ bằng:", ["$60^\\circ$", "$120^\\circ$", "$35^\\circ$", "$25^\\circ$"], 0, "$\\widehat{DOE} = \\widehat{DOB} + \\widehat{BOE} = 25^\\circ + 35^\\circ = 60^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm số tự nhiên $n$ biết: $\\frac{1}{9} \\cdot 27^n = 3^n$.", ["$n = 1$", "$n = 2$", "$n = 3$", "$n = 0$"], 0, "$3^{-2} \\cdot 3^{3n} = 3^n \\Rightarrow 3n - 2 = n \\Rightarrow 2n = 2 \\Rightarrow n = 1$."),
            make_mc(10, "Vận dụng cao", "Tìm số thực $x$ biết: $|x - 3| = x - 3$.", ["$x \\ge 3$", "$x > 3$", "$x \\le 3$", "$x = 3$"], 0, "Ta có $|A| = A \\Leftrightarrow A \\ge 0 \\Rightarrow x - 3 \\ge 0 \\Leftrightarrow x \\ge 3$."),
            make_mc(11, "Vận dụng cao", "Cho $a // b$ và $b // c$. Khẳng định nào sau đây là luôn đúng?", ["$a // c$", "$a \\perp c$", "$a$ cắt $c$", "$a$ trùng $c$"], 0, "Tính chất bắc cầu của quan hệ song song: Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau."),
            make_mc(12, "Vận dụng cao", "Rút gọn biểu thức $S = \\frac{4^5 \\cdot 9^4 - 2 \\cdot 6^9}{2^{10} \\cdot 3^8 + 6^8 \\cdot 20}$ ta được kết quả là:", ["$-\\frac{1}{3}$", "$\\frac{1}{3}$", "$-\\frac{2}{3}$", "$\\frac{2}{3}$"], 0, "Đưa về cơ số 2 và 3: Tử số $= 2^{10} \\cdot 3^8 - 2 \\cdot 2^9 \\cdot 3^9 = 2^{10} \\cdot 3^8(1 - 3) = -2 \\cdot 2^{10} \\cdot 3^8$. Mẫu số $= 2^{10} \\cdot 3^8 + 2^8 \\cdot 3^8 \\cdot 20 = 2^8 \\cdot 3^8(4 + 20) = 24 \\cdot 2^8 \\cdot 3^8 = 3 \\cdot 2^{11} \\cdot 3^8$. Chia tử cho mẫu: $\\frac{-2^{11} \\cdot 3^8}{3 \\cdot 2^{11} \\cdot 3^8} = -\\frac{1}{3}$.")
        ],
        "part2": [
            make_tf(1, "Một cửa hàng thời trang nhập về 100 chiếc áo khoác với giá gốc 300 nghìn đồng/chiếc. Cửa hàng bán 60 chiếc với giá tăng $20\\%$ so với giá gốc, số áo còn lại bán giảm giá $10\\%$ so với giá gốc.", [
                {"id": "a", "text": "Tổng số vốn cửa hàng bỏ ra để nhập 100 chiếc áo là 30 triệu đồng.", "correct": True, "level": "Nhận biết", "explanation": "$100 \\cdot 300\\,000 = 30\\,000\\,000$ đồng = 30 triệu đồng."},
                {"id": "b", "text": "Giá bán một chiếc áo khoác trong đợt đầu là 360 nghìn đồng.", "correct": True, "level": "Nhận biết", "explanation": "$300 \\cdot (1 + 20\\%) = 360$ nghìn đồng."},
                {"id": "c", "text": "Giá bán một chiếc áo trong đợt giảm giá là 270 nghìn đồng.", "correct": True, "level": "Thông hiểu", "explanation": "$300 \\cdot (1 - 10\\%) = 270$ nghìn đồng."},
                {"id": "d", "text": "Sau khi bán hết 100 chiếc áo, cửa hàng thu lãi tổng cộng là 3,4 triệu đồng.", "correct": False, "level": "Vận dụng", "explanation": "Doanh thu: $60 \\cdot 360 + 40 \\cdot 270 = 21\\,600 + 10\\,800 = 32,4$ triệu đồng. Tiền lãi là $32,4 - 30 = 2,4$ triệu đồng, không phải 3,4 triệu đồng."}
            ]),
            make_tf(2, "Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$ có số đo lần lượt là $110^\\circ$ và $70^\\circ$. Gọi $OD$ là tia phân giác của góc $\\widehat{AOB}$.", [
                {"id": "a", "text": "Tia $OB$ nằm giữa hai tia $OA$ và $OC$.", "correct": True, "level": "Nhận biết", "explanation": "Vì hai góc kề bù có chung tia $OB$ và hai tia $OA, OC$ đối nhau."},
                {"id": "b", "text": "Số đo góc $\\widehat{AOD}$ bằng $55^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "$OD$ là phân giác $\\widehat{AOB}$ nên $\\widehat{AOD} = 110^\\circ : 2 = 55^\\circ$."},
                {"id": "c", "text": "Số đo góc $\\widehat{COD}$ bằng $125^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\widehat{COD} = \\widehat{COB} + \\widehat{BOD} = 70^\\circ + 55^\\circ = 125^\\circ$."},
                {"id": "d", "text": "Tia đối của tia $OD$ là tia phân giác của góc $\\widehat{BOC}$.", "correct": False, "level": "Vận dụng", "explanation": "Góc tạo bởi tia đối của $OD$ với $OB$ là $180^\\circ - 55^\\circ = 125^\\circ \\neq 35^\\circ$ nên không phải tia phân giác của $\\widehat{BOC}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của lũy thừa: $(-0,2)^3$.", "-0.008", ["-0.008", "-0,008"], "$(-0,2)^3 = -0,008$."),
            make_sa(2, "Thông hiểu", "Tìm $x$, biết: $|x| = \\sqrt{9}$.", "3", ["3", "-3; 3", "3; -3"], "$|x| = 3 \\Rightarrow x = \\pm 3$."),
            make_sa(3, "Vận dụng", "Ba lớp 7A, 7B, 7C tham gia trồng cây mùa xuân. Số cây ba lớp trồng được tỉ lệ với các số 3; 4; 5. Biết lớp 7C trồng nhiều hơn lớp 7A là 30 cây. Tính tổng số cây cả ba lớp trồng được.", "180", ["180", "180 cây"], "Giá trị 1 phần: $30 : (5 - 3) = 15$ cây. Tổng số phần: $3 + 4 + 5 = 12$ phần. Tổng số cây: $12 \\cdot 15 = 180$ cây."),
            make_sa(4, "Vận dụng cao", "Tìm số hữu tỉ $x$ thỏa mãn: $(2x - 1)^3 = -125$.", "-2", ["-2"], "$(2x - 1)^3 = (-5)^3 \\Rightarrow 2x - 1 = -5 \\Rightarrow 2x = -4 \\Rightarrow x = -2$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý nhất:\n a) $\\frac{11}{24} - \\frac{5}{41} + \\frac{13}{24} + 0,5 - \\frac{36}{41}$\n b) $\\left(-\\frac{3}{4}\\right) \\cdot 12 + \\left(-\\frac{3}{4}\\right) \\cdot 8$",
                "a) $\\left(\\frac{11}{24} + \\frac{13}{24}\\right) - \\left(\\frac{5}{41} + \\frac{36}{41}\\right) + 0,5 = 1 - 1 + 0,5 = 0,5$ (0.5đ)\nb) $\\left(-\\frac{3}{4}\\right) \\cdot (12 + 8) = -\\frac{3}{4} \\cdot 20 = -15$ (0.5đ)",
                "a) Nhóm các phân số cùng mẫu: $1 - 1 + 0,5 = 0,5$.\nb) Đặt thừa số chung: $-\\frac{3}{4} \\cdot 20 = -15$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số thực $x$, biết:\n a) $2x - \\frac{3}{5} = \\frac{7}{10}$\n b) $\\sqrt{x} = 4$ ($x \\ge 0$)",
                "a) $2x = \\frac{7}{10} + \\frac{6}{10} = \\frac{13}{10} \\Rightarrow x = \\frac{13}{20}$ (0.5đ)\nb) $x = 4^2 = 16$ (0.5đ)",
                "a) $2x = 13/10 \\Rightarrow x = 13/20$.\nb) Bình phương hai vế: $x = 16$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Cho góc nhọn $\\widehat{xOy} = 70^\\circ$. Lấy điểm $A$ trên tia $Ox$. Kẻ đường thẳng $d$ đi qua $A$ và song song với $Oy$. Tia phân giác của góc $\\widehat{xOy}$ cắt đường thẳng $d$ tại điểm $B$.\n a) Tính số đo góc $\\widehat{xAB}$.\n b) Chứng minh rằng $\\widehat{ABO} = \\widehat{AOB}$.",
                "a) Vì $d // Oy$ nên $\\widehat{xAB} = \\widehat{xOy} = 70^\\circ$ (hai góc đồng vị) (0.25đ)\nb) Vì $OB$ là phân giác $\\widehat{xOy}$ nên $\\widehat{AOB} = 35^\\circ$. Do $d // Oy$ nên $\\widehat{ABO} = \\widehat{yOB} = 35^\\circ$ (so le trong). Suy ra $\\widehat{ABO} = \\widehat{AOB} = 35^\\circ$ (đpcm) (0.25đ)",
                "a) Góc đồng vị nên $\\widehat{xAB} = 70^\\circ$.\nb) Góc so le trong và tính chất tia phân giác suy ra hai góc cùng bằng $35^\\circ$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm tất cả các số thực $x, y$ thỏa mãn: $(2x - 1)^{2024} + |y - 2| \\le 0$.",
                "Ta có $(2x - 1)^{2024} \\ge 0$ với mọi $x$ (lũy thừa bậc chẵn).\nVà $|y - 2| \\ge 0$ với mọi $y$ (giá trị tuyệt đối).\nSuy ra vế trái $(2x - 1)^{2024} + |y - 2| \\ge 0$.\nĐể tổng này nhỏ hơn hoặc bằng 0 thì dấu '=' bắt buộc phải xảy ra:\n$\\begin{cases} 2x - 1 = 0 \\\\ y - 2 = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = \\frac{1}{2} \\\\ y = 2 \\end{cases}$.\nVậy duy nhất cặp số $(x, y) = \\left(\\frac{1}{2}; 2\\right)$ (0.5đ)",
                "Vì cả hai số hạng đều không âm nên tổng bé hơn hoặc bằng 0 chỉ xảy ra khi đồng thời cả hai số hạng bằng 0. Tìm được $x = 1/2$ và $y = 2$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 04 ------------------
    # Ngữ cảnh: Nông nghiệp công nghệ cao, nhà màng thông minh, lưu lượng tưới nhỏ giọt
    exams.append({
        "id": "p_g7_mid1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 04)",
        "topic": "Tập hợp số hữu tỉ Q, Căn bậc hai, Góc kề bù, So le trong & Đồng vị",
        "grade": "7",
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
            make_mc(1, "Nhận biết", "Phân số nào sau đây biểu diễn số hữu tỉ $0,4$?", ["$\\frac{2}{5}$", "$\\frac{4}{100}$", "$\\frac{1}{4}$", "$\\frac{4}{5}$"], 0, "$0,4 = \\frac{4}{10} = \\frac{2}{5}$."),
            make_mc(2, "Nhận biết", "Trong các số sau, số nào có căn bậc hai số học bằng $9$?", ["$81$", "$3$", "$18$", "$27$"], 0, "$\\sqrt{81} = 9$."),
            make_mc(3, "Nhận biết", "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$. Biết $\\widehat{xOy} = 70^\\circ$. Số đo góc $\\widehat{yOz}$ là:", ["$110^\\circ$", "$70^\\circ$", "$20^\\circ$", "$90^\\circ$"], 0, "$180^\\circ - 70^\\circ = 110^\\circ$."),
            make_mc(4, "Thông hiểu", "Tính giá trị của biểu thức: $\\left(-\\frac{1}{2}\\right)^4$:", ["$\\frac{1}{16}$", "$-\\frac{1}{16}$", "$\\frac{1}{8}$", "$-\\frac{1}{8}$"], 0, "$\\left(-\\frac{1}{2}\\right)^4 = \\frac{1}{16}$."),
            make_mc(5, "Thông hiểu", "Cho đường thẳng $c$ cắt hai đường thẳng $a$ và $b$. Nếu trong các góc tạo thành có một cặp góc so le trong bằng nhau thì:", ["$a // b$", "$a \\perp b$", "$a$ cắt $b$", "$a$ trùng $b$"], 0, "Dấu hiệu nhận biết hai đường thẳng song song."),
            make_mc(6, "Thông hiểu", "Làm tròn số $45,827$ đến hàng phần mười ta được:", ["$45,8$", "$45,9$", "$46$", "$45,83$"], 0, "Chữ số hàng phần trăm là 2 (< 5) nên làm tròn thành $45,8$."),
            make_mc(7, "Vận dụng", "Một hệ thống tưới nhỏ giọt tiêu thụ $1,25$ mét khối nước mỗi giờ. Sau 3 ngày, mỗi ngày hệ thống hoạt động 4,5 giờ thì tổng lượng nước tiêu thụ là:", ["$16,875\\,\\text{m}^3$", "$15\\,\\text{m}^3$", "$17\\,\\text{m}^3$", "$14,5\\,\\text{m}^3$"], 0, "Tổng giờ: $3 \\cdot 4,5 = 13,5$ giờ. Lượng nước: $13,5 \\cdot 1,25 = 16,875\\,\\text{m}^3$."),
            make_mc(8, "Vận dụng", "Cho hai đường thẳng $m$ và $n$ song song với nhau. Đường thẳng $d$ cắt $m$ tại $A$ và cắt $n$ tại $B$. Tia phân giác của góc $\\widehat{mAB}$ cắt $n$ tại điểm $C$. Biết $\\widehat{BAC} = 30^\\circ$. Số đo góc $\\widehat{ABC}$ bằng:", ["$120^\\circ$", "$60^\\circ$", "$30^\\circ$", "$90^\\circ$"], 0, "Tia phân giác nên $\\widehat{mAB} = 60^\\circ$. Hai góc trong cùng phía bù nhau $\\Rightarrow \\widehat{ABC} = 180^\\circ - 60^\\circ = 120^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức $A = (x - 2)^2 + |y + 1| + 5$.", ["$5$", "$2$", "$1$", "$0$"], 0, "Vì $(x - 2)^2 \\ge 0$ và $|y + 1| \\ge 0$ nên $A \\ge 5$. Dấu '=' khi $x = 2, y = -1$."),
            make_mc(10, "Vận dụng cao", "Tìm số hữu tỉ $x$ thỏa mãn: $\\frac{x}{3} = \\frac{12}{x}$ và $x < 0$.", ["$x = -6$", "$x = 6$", "$x = -4$", "$x = -9$"], 0, "$x^2 = 36 \\Rightarrow x = -6$ vì $x < 0$."),
            make_mc(11, "Vận dụng cao", "Cho $M = \\frac{1}{2} - \\left(\\frac{1}{2}\\right)^2 + \\left(\\frac{1}{2}\\right)^3 - \\dots - \\left(\\frac{1}{2}\\right)^{20}$. Khẳng định nào sau đây đúng?", ["$M < \\frac{1}{3}$", "$M > \\frac{1}{2}$", "$M = \\frac{1}{3}$", "$M < 0$"], 0, "Tổng cấp số nhân lùi: $M = \\frac{1}{2} \\cdot \\frac{1 - (-1/2)^{20}}{1 - (-1/2)} = \\frac{1}{3}\\left(1 - \\frac{1}{2^{20}}\\right) < \\frac{1}{3}$."),
            make_mc(12, "Vận dụng cao", "Cho hai đường thẳng $a // b$. Điểm $O$ nằm giữa hai đường thẳng $a$ và $b$. Góc nhọn $\\widehat{aAO} = 40^\\circ$, góc nhọn $\\widehat{bBO} = 50^\\circ$. Số đo góc $\\widehat{AOB}$ bằng:", ["$90^\\circ$", "$10^\\circ$", "$45^\\circ$", "$100^\\circ$"], 0, "Kẻ qua $O$ đường thẳng song song với $a$ và $b$. Ta có $\\widehat{AOB} = 40^\\circ + 50^\\circ = 90^\\circ$.")
        ],
        "part2": [
            make_tf(1, "Một xe tải chở $4,5$ tấn phân bón chia đều cho 3 hợp tác xã nông nghiệp: Hợp tác xã A nhận $\\frac{1}{3}$ tổng khối lượng, Hợp tác xã B nhận $40\\%$ tổng khối lượng, phần còn lại chuyển cho Hợp tác xã C.", [
                {"id": "a", "text": "Hợp tác xã A nhận được $1,5$ tấn phân bón.", "correct": True, "level": "Nhận biết", "explanation": "$4,5 \\cdot \\frac{1}{3} = 1,5$ tấn."},
                {"id": "b", "text": "Khối lượng phân bón Hợp tác xã B nhận là $1,8$ tấn.", "correct": True, "level": "Nhận biết", "explanation": "$4,5 \\cdot 40\\% = 1,8$ tấn."},
                {"id": "c", "text": "Hợp tác xã C nhận được $1,2$ tấn phân bón.", "correct": True, "level": "Thông hiểu", "explanation": "$4,5 - (1,5 + 1,8) = 1,2$ tấn."},
                {"id": "d", "text": "Hợp tác xã B nhận nhiều hơn Hợp tác xã A đúng $0,5$ tấn phân bón.", "correct": False, "level": "Vận dụng", "explanation": "$1,8 - 1,5 = 0,3$ tấn, không phải $0,5$ tấn."}
            ]),
            make_tf(2, "Cho hình vẽ biết đường thẳng $a$ song song với đường thẳng $b$. Một đường thẳng $c$ cắt $a$ tại $P$ và cắt $b$ tại $Q$ sao cho một góc tại đỉnh $P$ bằng $110^\\circ$.", [
                {"id": "a", "text": "Góc kề bù với góc $110^\\circ$ tại đỉnh $P$ có số đo bằng $70^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "$180^\\circ - 110^\\circ = 70^\\circ$."},
                {"id": "b", "text": "Góc đồng vị với góc $110^\\circ$ tại đỉnh $Q$ có số đo bằng $110^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Do $a // b$ nên hai góc đồng vị bằng nhau."},
                {"id": "c", "text": "Hai góc trong cùng phía có tổng số đo bằng $180^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Tính chất của hai đường thẳng song song."},
                {"id": "d", "text": "Tia phân giác của hai góc trong cùng phía cắt nhau tạo thành một góc tù $120^\\circ$.", "correct": False, "level": "Vận dụng", "explanation": "Hai tia phân giác của hai góc trong cùng phía vuông góc với nhau, tạo thành góc $90^\\circ$, không phải $120^\\circ$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm số đối của số hữu tỉ $-\\frac{5}{9}$.", "5/9", ["5/9"], "Số đối là 5/9."),
            make_sa(2, "Thông hiểu", "Tính giá trị của biểu thức: $\\sqrt{1,44} + 0,8$.", "2", ["2", "2.0"], "$1,2 + 0,8 = 2$."),
            make_sa(3, "Vận dụng", "Một bể bơi hình chữ nhật có chu vi $80\\,\\text{m}$, chiều dài gấp 3 lần chiều rộng. Người ta lát gạch men xung quanh thành bể tốn 250 nghìn đồng mỗi mét dài. Tổng chi phí nẹp viền quanh thành bể bơi là bao nhiêu triệu đồng?", "20", ["20", "20 triệu đồng"], "Chi phí $= 80 \\cdot 250\\,000 = 20\\,000\\,000$ đồng $= 20$ triệu đồng."),
            make_sa(4, "Vận dụng cao", "Tìm số hữu tỉ $x$ thỏa mãn: $|3x - 2| - 1 = 4$ với $x < 0$.", "-1", ["-1"], "$|3x - 2| = 5 \\Rightarrow 3x - 2 = -5 \\Rightarrow 3x = -3 \\Rightarrow x = -1$ (vì $x < 0$).")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách thuận tiện nhất:\n a) $\\frac{5}{13} \\cdot \\frac{7}{9} + \\frac{5}{13} \\cdot \\frac{2}{9}$\n b) $\\sqrt{49} - \\sqrt{0,25} \\cdot 4$",
                "a) $\\frac{5}{13} \\cdot \\left(\\frac{7}{9} + \\frac{2}{9}\\right) = \\frac{5}{13} \\cdot 1 = \\frac{5}{13}$ (0.5đ)\nb) $7 - 0,5 \\cdot 4 = 7 - 2 = 5$ (0.5đ)",
                "a) Đặt thừa số chung: $\\frac{5}{13} \\cdot 1 = \\frac{5}{13}$.\nb) $7 - 2 = 5$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số thực $x$, biết:\n a) $x - \\frac{2}{5} = -\\frac{1}{3}$\n b) $|x + 2| = 1,5$",
                "a) $x = -\\frac{1}{3} + \\frac{2}{5} = \\frac{1}{15}$ (0.5đ)\nb) $x + 2 = 1,5 \\Rightarrow x = -0,5$ hoặc $x + 2 = -1,5 \\Rightarrow x = -3,5$ (0.5đ)",
                "a) $x = 1/15$.\nb) $x = -0,5$ hoặc $x = -3,5$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Cho hình vẽ có $AB // CD$. Biết góc $\\widehat{BAE} = 120^\\circ$ và $\\widehat{AEC} = 80^\\circ$ (điểm $E$ nằm giữa hai đường thẳng $AB$ và $CD$).\n a) Kẻ qua $E$ tia $Ex // AB$. Tính số đo góc $\\widehat{AEx}$.\n b) Tính số đo góc $\\widehat{ECD}$.",
                "a) Vì $Ex // AB$ nên $\\widehat{BAE} + \\widehat{AEx} = 180^\\circ$ (trong cùng phía) $\\Rightarrow \\widehat{AEx} = 180^\\circ - 120^\\circ = 60^\\circ$ (0.25đ)\nb) Vì tia $Ex$ nằm trong góc $\\widehat{AEC}$ nên $\\widehat{xEC} = \\widehat{AEC} - \\widehat{AEx} = 80^\\circ - 60^\\circ = 20^\\circ$. Do $Ex // CD$ nên $\\widehat{ECD} = \\widehat{xEC} = 20^\\circ$ (so le trong) (0.25đ)",
                "a) $\\widehat{AEx} = 60^\\circ$.\nb) $\\widehat{ECD} = 20^\\circ$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm các số thực $x, y$ thỏa mãn đẳng thức: $\\sqrt{x - 1} + (y - 3)^2 = 0$.",
                "Điều kiện: $x \\ge 1$.\nTa có $\\sqrt{x - 1} \\ge 0$ và $(y - 3)^2 \\ge 0$ với mọi $x \\ge 1, y \\in \\mathbb{R}$.\nTổng hai số không âm bằng 0 khi và chỉ khi cả hai số đồng thời bằng 0:\n$\\begin{cases} \\sqrt{x - 1} = 0 \\\\ (y - 3)^2 = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = 1 \\\\ y = 3 \\end{cases}$.\nVậy $x = 1$ và $y = 3$ (0.5đ)",
                "Do cả căn bậc hai và bình phương đều không âm nên tổng bằng 0 khi cả hai bằng 0. Suy ra $x = 1, y = 3$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 05 ------------------
    # Ngữ cảnh: Vật lý quang học, phản xạ ánh sáng trên gương phẳng, góc nghiêng pin năng lượng mặt trời
    exams.append({
        "id": "p_g7_mid1_05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 05)",
        "topic": "Số hữu tỉ, Số vô tỉ, Căn bậc hai & Góc đối đỉnh, Tia phân giác",
        "grade": "7",
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
            make_mc(1, "Nhận biết", "Số nào sau đây là số đối của số $-\\sqrt{3}$?", ["$\\sqrt{3}$", "$-\\sqrt{3}$", "$3$", "$-3$"], 0, "Số đối của $-\\sqrt{3}$ là $\\sqrt{3}$."),
            make_mc(2, "Nhận biết", "Hai góc kề nhau là hai góc có:", ["Một cạnh chung và hai cạnh còn lại nằm trên hai nửa mặt phẳng đối nhau bờ chứa cạnh chung", "Tổng bằng $90^\\circ$", "Tổng bằng $180^\\circ$", "Hai cạnh là hai tia đối nhau"], 0, "Định nghĩa hai góc kề nhau."),
            make_mc(3, "Nhận biết", "Trong các số sau, số nào viết được dưới dạng số thập phân hữu hạn?", ["$\\frac{3}{4}$", "$\\frac{1}{3}$", "$\\frac{5}{7}$", "$\\frac{2}{9}$"], 0, "$\\frac{3}{4} = 0,75$ là số thập phân hữu hạn."),
            make_mc(4, "Thông hiểu", "Tính giá trị của biểu thức: $\\left(-\\frac{2}{5}\\right) \\cdot \\left(-\\frac{15}{8}\\right)$:", ["$\\frac{3}{4}$", "$-\\frac{3}{4}$", "$\\frac{3}{20}$", "$-\\frac{3}{20}$"], 0, "$\\frac{2 \\cdot 15}{5 \\cdot 8} = \\frac{3}{4}$."),
            make_mc(5, "Thông hiểu", "Cho hai đường thẳng $xx'$ và $yy'$ cắt nhau tại $O$. Biết $\\widehat{xOy} = 50^\\circ$. Số đo góc đối đỉnh với $\\widehat{xOy}$ là:", ["$50^\\circ$", "$130^\\circ$", "$40^\\circ$", "$90^\\circ$"], 0, "Hai góc đối đỉnh thì bằng nhau."),
            make_mc(6, "Thông hiểu", "Giá trị của $\\sqrt{0,09}$ bằng:", ["$0,3$", "$0,03$", "$0,81$", "$0,081$"], 0, "$\\sqrt{0,09} = 0,3$ vì $0,3^2 = 0,09$."),
            make_mc(7, "Vận dụng", "Một tấm pin năng lượng mặt trời hình chữ nhật có chiều rộng $1,2\\,\\text{m}$, chiều dài gấp 1,5 lần chiều rộng. Diện tích của tấm pin năng lượng mặt trời là:", ["$2,16\\,\\text{m}^2$", "$1,8\\,\\text{m}^2$", "$2,4\\,\\text{m}^2$", "$3,24\\,\\text{m}^2$"], 0, "Chiều dài $= 1,2 \\cdot 1,5 = 1,8\\,\\text{m}$. Diện tích $= 1,2 \\cdot 1,8 = 2,16\\,\\text{m}^2$."),
            make_mc(8, "Vận dụng", "Tia sáng mặt trời chiếu tới một gương phẳng đặt nằm ngang tạo thành góc tới bằng $35^\\circ$ so với pháp tuyến. Góc tạo bởi tia tới và tia phản xạ là:", ["$70^\\circ$", "$35^\\circ$", "$55^\\circ$", "$110^\\circ$"], 0, "Góc phản xạ bằng góc tới ($35^\\circ$). Góc giữa tia tới và tia phản xạ là $35^\\circ + 35^\\circ = 70^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm số thực $x$ thỏa mãn: $\\left(x^2 - 4\\right)\\left(|x| - 3\\right) = 0$.", ["$x \\in \\{-3; -2; 2; 3\\}$", "$x \\in \\{-2; 2\\}$", "$x \\in \\{-3; 3\\}$", "$x \\in \\{2; 3\\}$"], 0, "$x^2 = 4 \\Rightarrow x = \\pm 2$; $|x| = 3 \\Rightarrow x = \\pm 3$."),
            make_mc(10, "Vận dụng cao", "So sánh $2^{24}$ và $3^{16}$ ta có:", ["$2^{24} = 3^{16}$", "$2^{24} > 3^{16}$", "$2^{24} < 3^{16}$", "Không so sánh được"], 0, "$2^{24} = (2^3)^8 = 8^8$; $3^{16} = (3^2)^8 = 9^8$. Vì $8 < 9$ nên $2^{24} < 3^{16}$."),
            make_mc(11, "Vận dụng cao", "Cho định lí: 'Hai góc cùng phụ với một góc thứ ba thì bằng nhau'. Giả thiết của định lí là:", ["Hai góc cùng phụ với một góc thứ ba", "Hai góc đó bằng nhau", "Hai góc phụ nhau", "Ba góc bằng nhau"], 0, "Giả thiết là phần nằm sau từ 'Nếu' hoặc mệnh đề điều kiện ban đầu."),
            make_mc(12, "Vận dụng cao", "Có bao nhiêu số hữu tỉ $x$ thỏa mãn: $|x - 1,2| + |x - 3,8| = 2,6$?", ["Vô số", "1", "2", "0"], 0, "Áp dụng $|a| + |b| \\ge |a + b|$: $|x - 1,2| + |3,8 - x| \\ge 2,6$. Đẳng thức xảy ra khi $(x - 1,2)(3,8 - x) \\ge 0 \\Leftrightarrow 1,2 \\le x \\le 3,8$. Do đó có vô số số hữu tỉ thỏa mãn.")
        ],
        "part2": [
            make_tf(1, "Một bể nuôi cá cảnh chứa nước biển nhân tạo có độ mặn chuẩn là $3,5\\%$ (tức 35 gam muối trong 1000 gam nước). Người nuôi muốn chuẩn bị 120 lít nước biển nhân tạo (coi 1 lít nước nặng 1 kg).", [
                {"id": "a", "text": "Khối lượng của 120 lít nước là 120 kg.", "correct": True, "level": "Nhận biết", "explanation": "1 lít nặng 1 kg nên 120 lít nặng 120 kg."},
                {"id": "b", "text": "Số 3,5% viết dưới dạng số thập phân là 0,035.", "correct": True, "level": "Nhận biết", "explanation": "$3,5\\% = 0,035$."},
                {"id": "c", "text": "Khối lượng muối cần hòa tan là $4,2\\,\\text{kg}$.", "correct": True, "level": "Thông hiểu", "explanation": "$120 \\cdot 0,035 = 4,2\\,\\text{kg}$."},
                {"id": "d", "text": "Nếu hòa thêm 30 lít nước ngọt vào bể thì độ mặn mới của bể sẽ giảm xuống còn $3,0\\%$.", "correct": False, "level": "Vận dụng", "explanation": "Tổng nước là 150 lít. Độ mặn mới: $4,2 : 150 = 0,028 = 2,8\\% \\neq 3,0\\%$."}
            ]),
            make_tf(2, "Cho hai góc kề bù $\\widehat{mOn}$ và $\\widehat{nOp}$ có số đo lần lượt là $130^\\circ$ và $50^\\circ$. Gọi $Oa$ và $Ob$ lần lượt là tia phân giác của $\\widehat{mOn}$ và $\\widehat{nOp}$.", [
                {"id": "a", "text": "Hai tia $Om$ và $Op$ là hai tia đối nhau.", "correct": True, "level": "Nhận biết", "explanation": "Do hai góc kề bù nên hai cạnh ngoài là hai tia đối nhau."},
                {"id": "b", "text": "Số đo góc $\\widehat{aOn}$ bằng $65^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "$Oa$ là phân giác $\\widehat{mOn}$ nên $\\widehat{aOn} = 130^\\circ : 2 = 65^\\circ$."},
                {"id": "c", "text": "Số đo góc $\\widehat{nOb}$ bằng $25^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "$Ob$ là phân giác $\\widehat{nOp}$ nên $\\widehat{nOb} = 50^\\circ : 2 = 25^\\circ$."},
                {"id": "d", "text": "Góc $\\widehat{aOb}$ là góc tù có số đo bằng $100^\\circ$.", "correct": False, "level": "Vận dụng", "explanation": "$\\widehat{aOb} = 65^\\circ + 25^\\circ = 90^\\circ$ (góc vuông), không phải góc tù."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm số đối của số hữu tỉ $0,8$.", "-0.8", ["-0.8", "-0,8", "-4/5"], "Số đối là -0,8."),
            make_sa(2, "Thông hiểu", "Tính: $\\sqrt{100} - \\sqrt{64}$.", "2", ["2"], "$10 - 8 = 2$."),
            make_sa(3, "Vận dụng", "Một mảnh vườn hình chữ nhật có diện tích $96\\,\\text{m}^2$, chiều dài là $12\\,\\text{m}$. Người ta muốn rào kẽm gai xung quanh mảnh vườn đó, chừa lại một lối đi rộng $1,5\\,\\text{m}$. Chiều dài dây rào kẽm gai cần dùng là bao nhiêu mét?", "38.5", ["38.5", "38,5"], "Chiều rộng $= 96 : 12 = 8\\,\\text{m}$. Chu vi $= 2(12 + 8) = 40\\,\\text{m}$. Dây rào $= 40 - 1,5 = 38,5\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm số hữu tỉ $x$ thỏa mãn: $\\left(\\frac{1}{2}\\right)^{2x - 1} = \\frac{1}{32}$.", "3", ["3"], "$1/32 = (1/2)^5 \\Rightarrow 2x - 1 = 5 \\Rightarrow 2x = 6 \\Rightarrow x = 3$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý nhất:\n a) $\\frac{3}{7} \\cdot \\left(-\\frac{2}{5}\\right) + \\frac{3}{7} \\cdot \\left(-\\frac{3}{5}\\right)$\n b) $\\sqrt{\\frac{49}{81}} - \\frac{2}{9}$",
                "a) $\\frac{3}{7} \\cdot \\left(-\\frac{2}{5} - \\frac{3}{5}\\right) = \\frac{3}{7} \\cdot (-1) = -\\frac{3}{7}$ (0.5đ)\nb) $\\frac{7}{9} - \\frac{2}{9} = \\frac{5}{9}$ (0.5đ)",
                "a) Đặt thừa số chung: $\\frac{3}{7} \\cdot (-1) = -\\frac{3}{7}$.\nb) $\\frac{7}{9} - \\frac{2}{9} = \\frac{5}{9}$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số thực $x$, biết:\n a) $\\frac{3}{4} + \\frac{1}{4}x = \\frac{1}{2}$\n b) $|2x - 3| = 5$",
                "a) $\\frac{1}{4}x = -\\frac{1}{4} \\Rightarrow x = -1$ (0.5đ)\nb) $2x - 3 = 5 \\Rightarrow x = 4$ hoặc $2x - 3 = -5 \\Rightarrow x = -1$ (0.5đ)",
                "a) $x = -1$.\nb) $x = 4$ hoặc $x = -1$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Cho hai đường thẳng $a$ và $b$ song song với nhau. Đường thẳng $c$ cắt $a$ tại $A$ và cắt $b$ tại $B$. Tia phân giác của góc $\\widehat{A_1}$ (góc so le trong) và tia phân giác của góc $\\widehat{B_1}$ (góc so le trong đối diện) lần lượt là $Ax$ và $By$.\n a) Chứng minh rằng góc tạo bởi tia phân giác $Ax$ với đường thẳng $c$ bằng góc tạo bởi tia phân giác $By$ với đường thẳng $c$.\n b) Chứng minh rằng $Ax // By$.",
                "a) Vì $a // b$ nên hai góc so le trong bằng nhau: $\\widehat{A_1} = \\widehat{B_1}$. Suy ra một nửa của chúng bằng nhau: $\\frac{1}{2}\\widehat{A_1} = \\frac{1}{2}\\widehat{B_1}$ (0.25đ)\nb) Hai góc này ở vị trí so le trong của hai tia $Ax$ và $By$ đối với đường thẳng $c$. Vì hai góc so le trong bằng nhau nên $Ax // By$ (đpcm) (0.25đ)",
                "a) Một nửa của hai góc so le trong bằng nhau.\nb) Do hai góc so le trong bằng nhau nên $Ax // By$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho biểu thức $A = \\frac{1}{1 \\cdot 2} + \\frac{1}{3 \\cdot 4} + \\frac{1}{5 \\cdot 6} + \\dots + \\frac{1}{99 \\cdot 100}$. Chứng minh rằng $A = \\frac{1}{51} + \\frac{1}{52} + \\dots + \\frac{1}{100}$.",
                "Ta có $\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}$.\nDo đó $A = \\left(1 - \\frac{1}{2}\\right) + \\left(\\frac{1}{3} - \\frac{1}{4}\\right) + \\dots + \\left(\\frac{1}{99} - \\frac{1}{100}\\right)$\n$= \\left(1 + \\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{100}\\right) - 2\\left(\\frac{1}{2} + \\frac{1}{4} + \\dots + \\frac{1}{100}\\right)$\n$= \\left(1 + \\frac{1}{2} + \\dots + \\frac{1}{100}\\right) - \\left(1 + \\frac{1}{2} + \\dots + \\frac{1}{50}\\right)$\n$= \\frac{1}{51} + \\frac{1}{52} + \\dots + \\frac{1}{100}$ (đpcm) (0.5đ)",
                "Tách từng cặp phân số và thêm bớt các số hạng chẵn, thu được vế phải là tổng từ 1/51 đến 1/100."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 06 ------------------
    # Ngữ cảnh: Quy hoạch giao thông đô thị, hai làn đường song song, ngã tư giao lộ
    exams.append({
        "id": "p_g7_mid1_06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 06)",
        "topic": "Số hữu tỉ tổng hợp, Giá trị tuyệt đối, Góc đối đỉnh & Chứng minh định lí",
        "grade": "7",
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
            make_mc(1, "Nhận biết", "Số nào sau đây không phải là số hữu tỉ?", ["$\\sqrt{5}$", "$-\\frac{4}{7}$", "$0$", "$1,25$"], 0, "$\\sqrt{5}$ là số vô tỉ."),
            make_mc(2, "Nhận biết", "Hai đường thẳng cắt nhau tạo thành bao nhiêu cặp góc đối đỉnh (khác góc bẹt)?", ["$2$", "$4$", "$1$", "$8$"], 0, "Hai đường thẳng cắt nhau tạo thành 2 cặp góc đối đỉnh."),
            make_mc(3, "Nhận biết", "Giá trị tuyệt đối của một số thực $x$ luôn thỏa mãn:", ["$|x| \\ge 0$", "$|x| > 0$", "$|x| \\le 0$", "$|x| = x$"], 0, "Giá trị tuyệt đối của một số luôn không âm: $|x| \\ge 0$."),
            make_mc(4, "Thông hiểu", "Tìm kết quả của phép tính $\\left(-\\frac{3}{4}\\right)^2$:", ["$\\frac{9}{16}$", "$-\\frac{9}{16}$", "$\\frac{6}{8}$", "$-\\frac{6}{8}$"], 0, "$\\left(-\\frac{3}{4}\\right)^2 = \\frac{9}{16}$."),
            make_mc(5, "Thông hiểu", "Cho hình vẽ biết $a // b$. Một đường thẳng $c$ cắt $a$ và $b$. Biết một góc đồng vị bằng $45^\\circ$. Góc so le trong tương ứng có số đo là:", ["$45^\\circ$", "$135^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0, "Do $a // b$ nên góc so le trong bằng góc đồng vị, cùng bằng $45^\\circ$."),
            make_mc(6, "Thông hiểu", "Tính $\\sqrt{144}$:", ["$12$", "$14$", "$\\pm 12$", "$72$"], 0, "$\\sqrt{144} = 12$."),
            make_mc(7, "Vận dụng", "Một xe khách chạy tuyến Hà Nội - Hải Phòng với tốc độ trung bình $72,5\\,\\text{km/h}$. Thời gian xe chạy từ bến xe Gia Lâm đến bến xe Niệm Nghĩa là $1\\frac{3}{5}$ giờ. Quãng đường từ bến xe Gia Lâm đến Niệm Nghĩa dài bao nhiêu ki-lô-mét?", ["$116\\,\\text{km}$", "$110\\,\\text{km}$", "$120\\,\\text{km}$", "$115\\,\\text{km}$"], 0, "$S = 72,5 \\cdot 1,6 = 116\\,\\text{km}$."),
            make_mc(8, "Vận dụng", "Cho góc $\\widehat{xOy} = 110^\\circ$. Kẻ tia $Oz$ là tia phân giác của $\\widehat{xOy}$. Kẻ tia $Om$ là tia đối của tia $Ox$. Số đo góc $\\widehat{zOm}$ bằng:", ["$125^\\circ$", "$55^\\circ$", "$70^\\circ$", "$110^\\circ$"], 0, "$\\widehat{xOz} = 55^\\circ$. Do $Om$ đối $Ox$ nên $\\widehat{xOz}$ và $\\widehat{zOm}$ kề bù: $\\widehat{zOm} = 180^\\circ - 55^\\circ = 125^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm số thực $x$ thỏa mãn: $\\sqrt{2x + 1} = 3$.", ["$x = 4$", "$x = 5$", "$x = 9$", "$x = 1$"], 0, "$2x + 1 = 9 \\Rightarrow 2x = 8 \\Rightarrow x = 4$."),
            make_mc(10, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức $B = |x - 1| + |x - 5|$.", ["$4$", "$5$", "$1$", "$0$"], 0, "$B = |x - 1| + |5 - x| \\ge |x - 1 + 5 - x| = 4$."),
            make_mc(11, "Vận dụng cao", "Cho $3^{x} + 3^{x+2} = 270$. Giá trị của $x$ là:", ["$x = 3$", "$x = 2$", "$x = 4$", "$x = 1$"], 0, "$3^x(1 + 9) = 270 \\Rightarrow 3^x \\cdot 10 = 270 \\Rightarrow 3^x = 27 = 3^3 \\Rightarrow x = 3$."),
            make_mc(12, "Vận dụng cao", "Cho hai đường thẳng phân biệt $a$ và $b$ cùng song song với đường thẳng $c$. Kết luận nào sau đây đúng?", ["$a // b$", "$a \\perp b$", "$a$ cắt $b$", "$a$ trùng $b$"], 0, "Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau.")
        ],
        "part2": [
            make_tf(1, "Một gia đình có mức tiêu thụ điện trong một tháng là $350\\,\\text{kWh}$. Bậc thang giá điện sinh hoạt: Bậc 1 (0 - 50 kWh) giá $1,8\\,\\text{nghìn đồng/kWh}$, Bậc 2 (51 - 100 kWh) giá $1,9\\,\\text{nghìn đồng/kWh}$, Bậc 3 (101 - 200 kWh) giá $2,2\\,\\text{nghìn đồng/kWh}$, Bậc 4 (trên 200 kWh) giá $2,7\\,\\text{nghìn đồng/kWh}$.", [
                {"id": "a", "text": "Số kWh điện dùng ở Bậc 1 là $50\\,\\text{kWh}$.", "correct": True, "level": "Nhận biết", "explanation": "Bậc 1 tính cho 50 kWh đầu tiên."},
                {"id": "b", "text": "Tiền điện tính ở Bậc 1 là 90 nghìn đồng.", "correct": True, "level": "Nhận biết", "explanation": "$50 \\cdot 1,8 = 90$ nghìn đồng."},
                {"id": "c", "text": "Số kWh điện tính ở Bậc 4 là $150\\,\\text{kWh}$.", "correct": True, "level": "Thông hiểu", "explanation": "$350 - 200 = 150\\,\\text{kWh}$."},
                {"id": "d", "text": "Tổng số tiền điện gia đình phải trả (chưa tính thuế) vượt quá 900 nghìn đồng.", "correct": False, "level": "Vận dụng", "explanation": "Tiền điện: $90 + 50 \\cdot 1,9 + 100 \\cdot 2,2 + 150 \\cdot 2,7 = 90 + 95 + 220 + 405 = 810$ nghìn đồng $(< 900$ nghìn đồng)."}
            ]),
            make_tf(2, "Cho hình vẽ biết hai đường thẳng $a$ và $b$ song song với nhau. Đường thẳng $d$ cắt $a$ tại $M$ và cắt $b$ tại $N$ sao cho góc nhọn $\\widehat{aMN} = 50^\\circ$.", [
                {"id": "a", "text": "Hai góc kề bù tại đỉnh $M$ có tổng số đo bằng $180^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "Tính chất của hai góc kề bù."},
                {"id": "b", "text": "Góc so le trong với góc $\\widehat{aMN}$ tại đỉnh $N$ có số đo bằng $50^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Do $a // b$ nên hai góc so le trong bằng nhau."},
                {"id": "c", "text": "Góc đồng vị với góc $\\widehat{aMN}$ tại đỉnh $N$ có số đo bằng $50^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Do $a // b$ nên hai góc đồng vị bằng nhau."},
                {"id": "d", "text": "Nếu đường thẳng $d'$ vuông góc với $a$ thì $d'$ cũng song song với $b$.", "correct": False, "level": "Vận dụng", "explanation": "Nếu $d' \\perp a$ mà $a // b$ thì $d' \\perp b$, không phải song song."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm số đối của số thực $\\sqrt{7}$.", "-sqrt(7)", ["-sqrt(7)", "-\\sqrt{7}", "-căn 7"], "Số đối là $-\\sqrt{7}$."),
            make_sa(2, "Thông hiểu", "Tìm số hữu tỉ $x$, biết: $x + \\frac{1}{4} = -\\frac{3}{4}$.", "-1", ["-1"], "$x = -3/4 - 1/4 = -1$."),
            make_sa(3, "Vận dụng", "Một hồ nước hình chữ nhật có chiều dài $25\\,\\text{m}$, chiều rộng $15\\,\\text{m}$. Người ta đắp một bờ bao quanh hồ có chiều rộng $1\\,\\text{m}$. Diện tích của bờ bao quanh hồ là bao nhiêu mét vuông?", "84", ["84"], "Kích thước cả bờ: $27 \\times 17$. Diện tích cả bờ: $27 \\cdot 17 = 459\\,\\text{m}^2$. Diện tích hồ: $25 \\cdot 15 = 375\\,\\text{m}^2$. Diện tích bờ: $459 - 375 = 84\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị của số thực $x$ thỏa mãn: $|x - 2| + |3 - x| = 1$ và $x \\in \\mathbb{Z}$.", "2", ["2", "3", "2; 3"], "Ta có $|x - 2| + |3 - x| = 1 \\Leftrightarrow (x - 2)(3 - x) \\ge 0 \\Leftrightarrow 2 \\le x \\le 3$. Các số nguyên thỏa mãn là 2 và 3.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý:\n a) $\\frac{4}{9} \\cdot \\frac{13}{15} - \\frac{4}{9} \\cdot \\frac{4}{15}$\n b) $\\left(-\\frac{1}{3}\\right)^2 + \\sqrt{0,25} - \\frac{1}{9}$",
                "a) $\\frac{4}{9} \\cdot \\left(\\frac{13}{15} - \\frac{4}{15}\\right) = \\frac{4}{9} \\cdot \\frac{9}{15} = \\frac{4}{15}$ (0.5đ)\nb) $\\frac{1}{9} + 0,5 - \\frac{1}{9} = 0,5$ (0.5đ)",
                "a) Đặt thừa số chung: $\\frac{4}{9} \\cdot \\frac{9}{15} = \\frac{4}{15}$.\nb) Triệt tiêu $\\frac{1}{9}$: kết quả $0,5$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số thực $x$, biết:\n a) $\\frac{3}{5}x + \\frac{1}{2} = \\frac{7}{10}$\n b) $|x - 0,5| = 1,5$",
                "a) $\\frac{3}{5}x = \\frac{7}{10} - \\frac{5}{10} = \\frac{2}{10} = \\frac{1}{5} \\Rightarrow x = \\frac{1}{3}$ (0.5đ)\nb) $x - 0,5 = 1,5 \\Rightarrow x = 2$ hoặc $x - 0,5 = -1,5 \\Rightarrow x = -1$ (0.5đ)",
                "a) $x = 1/3$.\nb) $x = 2$ hoặc $x = -1$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Cho góc nhọn $\\widehat{xOy} = 50^\\circ$. Trên tia $Ox$ lấy điểm $A$. Kẻ tia $Am // Oy$ (sao cho $Am$ nằm trong góc $\\widehat{xOy}$). Kẻ tia phân giác $Az$ của góc $\\widehat{xAm}$.\n a) Tính số đo góc $\\widehat{xAm}$.\n b) Kẻ tia phân giác $Ot$ của góc $\\widehat{xOy}$. Chứng minh rằng tia $Az$ song song với tia $Ot$.",
                "a) Vì $Am // Oy$ nên $\\widehat{xAm} = \\widehat{xOy} = 50^\\circ$ (hai góc đồng vị) (0.25đ)\nb) Vì $Az$ là phân giác $\\widehat{xAm}$ nên $\\widehat{xAz} = 25^\\circ$. Vì $Ot$ là phân giác $\\widehat{xOy}$ nên $\\widehat{xOt} = 25^\\circ$. Do $\\widehat{xAz} = \\widehat{xOt} = 25^\\circ$ ở vị trí đồng vị nên $Az // Ot$ (đpcm) (0.25đ)",
                "a) Góc đồng vị nên $\\widehat{xAm} = 50^\\circ$.\nb) Hai góc tạo bởi tia phân giác ở vị trí đồng vị bằng nhau ($25^\\circ$) nên $Az // Ot$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực dương $a, b, c$. Chứng minh rằng biểu thức sau không phụ thuộc vào giá trị của $a, b, c$:\n $P = \\frac{a}{a + b} + \\frac{b}{b + c} + \\frac{c}{c + a}$. Tìm khoảng giá trị của $P$.",
                "Vì $a, b, c > 0$ nên:\n$\\frac{a}{a+b} > \\frac{a}{a+b+c}$\n$\\frac{b}{b+c} > \\frac{b}{a+b+c}$\n$\\frac{c}{c+a} > \\frac{c}{a+b+c}$\nCộng vế với vế ta được: $P > \\frac{a+b+c}{a+b+c} = 1$.\nMặt khác, ta có $\\frac{a}{a+b} < \\frac{a+c}{a+b+c}$, $\\frac{b}{b+c} < \\frac{b+a}{a+b+c}$, $\\frac{c}{c+a} < \\frac{c+b}{a+b+c}$.\nCộng vế với vế ta được: $P < \\frac{(a+c)+(b+a)+(c+b)}{a+b+c} = 2$.\nVậy $1 < P < 2$ (0.5đ)",
                "Áp dụng bất đẳng thức cộng mẫu số dương, chứng minh được $1 < P < 2$ với mọi bộ ba số thực dương."
            )
        ]
    })

    return exams

# ==============================================================================
# 6 MÃ ĐỀ CUỐI HỌC KỲ 1 - TOÁN 7 (final1)
# Phạm vi: Toàn bộ HK1 (Số hữu tỉ, Số thực, Dãy tỉ số bằng nhau, Tam giác bằng nhau, Tam giác cân & Thống kê biểu đồ).
# ==============================================================================
def generate_g7_final1():
    exams = []

    # ------------------ ĐỀ SỐ 01 ------------------
    # Ngữ cảnh: Phân bổ ngân sách dự án trường học, đo góc nghiêng giàn giáo xây dựng, phân tích biểu đồ đoạn thẳng doanh thu
    exams.append({
        "id": "p_g7_final1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 01)",
        "topic": "Số hữu tỉ, Dãy tỉ số bằng nhau, Các trường hợp bằng nhau của tam giác & Biểu đồ thống kê",
        "grade": "7",
        "term": "final1",
        "termName": "Cuối Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Từ đẳng thức $ad = bc$ (với $a, b, c, d \\neq 0$), tỉ lệ thức nào sau đây là đúng?", ["$\\frac{a}{b} = \\frac{c}{d}$", "$\\frac{a}{c} = \\frac{b}{d}$", "$\\frac{a}{d} = \\frac{b}{c}$", "$\\frac{b}{a} = \\frac{c}{d}$"], 0, "Từ $ad = bc$ suy ra $\\frac{a}{b} = \\frac{c}{d}$."),
            make_mc(2, "Nhận biết", "Tam giác $ABC$ cân tại $A$ thì:", ["$AB = AC$", "$AB = BC$", "$AC = BC$", "$\\widehat{A} = \\widehat{B}$"], 0, "Tam giác cân tại $A$ là tam giác có hai cạnh bên $AB = AC$."),
            make_mc(3, "Nhận biết", "Dữ liệu nào sau đây là dữ liệu định lượng (số liệu)?", ["Điểm kiểm tra môn Toán của học sinh", "Màu sắc yêu thích của các bạn trong lớp", "Nơi sinh của các thành viên trong gia đình", "Xếp loại hạnh kiểm cuối kỳ"], 0, "Điểm kiểm tra là dữ liệu dạng số (định lượng)."),
            make_mc(4, "Thông hiểu", "Cho $\\frac{x}{2} = \\frac{y}{3}$ và $x + y = 20$. Giá trị của $x$ và $y$ là:", ["$x = 8, y = 12$", "$x = 10, y = 10$", "$x = 12, y = 8$", "$x = 6, y = 14$"], 0, "$\\frac{x}{2} = \\frac{y}{3} = \\frac{x+y}{2+3} = \\frac{20}{5} = 4 \\Rightarrow x = 8, y = 12$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{A} = 50^\\circ, \\widehat{B} = 70^\\circ$. Số đo góc $\\widehat{C}$ bằng:", ["$60^\\circ$", "$50^\\circ$", "$70^\\circ$", "$80^\\circ$"], 0, "$\\widehat{C} = 180^\\circ - (50^\\circ + 70^\\circ) = 60^\\circ$."),
            make_mc(6, "Thông hiểu", "Cho $\\triangle ABC = \\triangle MNP$. Biết $AB = 5\\,\\text{cm}, BC = 7\\,\\text{cm}, AC = 6\\,\\text{cm}$. Chu vi của tam giác $MNP$ là:", ["$18\\,\\text{cm}$", "$12\\,\\text{cm}$", "$13\\,\\text{cm}$", "$20\\,\\text{cm}$"], 0, "Hai tam giác bằng nhau có chu vi bằng nhau: $5 + 7 + 6 = 18\\,\\text{cm}$."),
            make_mc(7, "Vận dụng", "Ba đội công nhân làm ba khối lượng công việc như nhau. Đội thứ nhất hoàn thành trong 4 ngày, đội thứ hai trong 6 ngày và đội thứ ba trong 8 ngày. Biết tổng số công nhân của cả ba đội là 26 người (năng suất các công nhân như nhau). Số công nhân của đội thứ nhất là:", ["$12$ người", "$8$ người", "$6$ người", "$10$ người"], 0, "Số ngày và số người tỉ lệ nghịch: $4x = 6y = 8z \\Rightarrow \\frac{x}{6} = \\frac{y}{4} = \\frac{z}{3} = \\frac{26}{13} = 2 \\Rightarrow x = 12$ người."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 60^\\circ$. Tia phân giác của góc $B$ cắt cạnh $AC$ tại điểm $D$. Kẻ $DH \\perp BC$ ($H \\in BC$). Số đo của góc $\\widehat{BDH}$ bằng:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$75^\\circ$"], 0, "$\\triangle BHD$ vuông tại $H$, góc $\\widehat{HBD} = 30^\\circ$ nên $\\widehat{BDH} = 90^\\circ - 30^\\circ = 60^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm các số $x, y, z$ biết: $2x = 3y = 5z$ và $x - y + z = -33$.", ["$x = -45, y = -30, z = -18$", "$x = 45, y = 30, z = 18$", "$x = -30, y = -20, z = -12$", "$x = -60, y = -40, z = -24$"], 0, "Chia cho 30: $\\frac{x}{15} = \\frac{y}{10} = \\frac{z}{6} = \\frac{x - y + z}{15 - 10 + 6} = \\frac{-33}{11} = -3 \\Rightarrow x = -45, y = -30, z = -18$."),
            make_mc(10, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{B} = 2\\widehat{C}$. Kẻ đường cao $AH$. Trên tia đối của tia $BA$ lấy điểm $D$ sao cho $BD = BH$. Khẳng định nào sau đây đúng?", ["$DH = DC$", "$DH \\perp AC$", "$\\triangle DHC$ là tam giác cân", "$\\widehat{D} = \\widehat{C}$"], 0, "Do $BD = BH$ nên $\\triangle BDH$ cân tại $B$, góc ngoài $\\widehat{ABC} = 2\\widehat{BDH} \\Rightarrow \\widehat{BDH} = \\widehat{C} \\Rightarrow DH = DC$."),
            make_mc(11, "Vận dụng cao", "Cho tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$. Khẳng định nào sau đây luôn đúng?", ["$\\frac{a + b}{b} = \\frac{c + d}{d}$", "$\\frac{a - b}{a} = \\frac{c + d}{c}$", "$\\frac{a + c}{b} = \\frac{b + d}{d}$", "$\\frac{a}{c} = \\frac{d}{b}$"], 0, "Cộng 1 vào hai vế: $\\frac{a}{b} + 1 = \\frac{c}{d} + 1 \\Rightarrow \\frac{a+b}{b} = \\frac{c+d}{d}$."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ nhọn. Vẽ ra phía ngoài tam giác hai tam giác vuông cân tại $A$ là $\\triangle ABD$ và $\\triangle ACE$. Gọi $M$ là trung điểm của $BC$. Khẳng định nào sau đây đúng?", ["$DE = 2AM$ và $AM \\perp DE$", "$DE = AM$", "$AM // DE$", "$DE = 3AM$"], 0, "Định lí quen thuộc: $DE = 2AM$ và đường trung tuyến $AM$ vuông góc với đoạn thẳng $DE$.")
        ],
        "part2": [
            make_tf(1, "Một trường THCS tổ chức phong trào thu gom giấy vụn bảo vệ môi trường cho ba khối 7, 8, 9. Số kilôgam giấy vụn thu gom được của ba khối 7, 8, 9 lần lượt tỉ lệ với các số 5; 6; 7. Biết tổng số giấy vụn cả ba khối thu gom được là 360 kg.", [
                {"id": "a", "text": "Tổng số phần bằng nhau của ba khối là 18 phần.", "correct": True, "level": "Nhận biết", "explanation": "$5 + 6 + 7 = 18$ phần."},
                {"id": "b", "text": "Giá trị của một phần bằng nhau là 20 kg.", "correct": True, "level": "Nhận biết", "explanation": "$360 : 18 = 20\\,\\text{kg}$."},
                {"id": "c", "text": "Khối 7 thu gom được 100 kg giấy vụn.", "correct": True, "level": "Thông hiểu", "explanation": "$20 \\cdot 5 = 100\\,\\text{kg}$."},
                {"id": "d", "text": "Khối 9 thu gom nhiều hơn khối 8 đúng 30 kg giấy vụn.", "correct": False, "level": "Vận dụng", "explanation": "Khối 9 hơn khối 8 đúng 1 phần $= 20\\,\\text{kg}$, không phải 30 kg."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB = AC$. Gọi $M$ là trung điểm của đoạn thẳng $BC$.", [
                {"id": "a", "text": "Tam giác $ABC$ là tam giác cân tại đỉnh $A$.", "correct": True, "level": "Nhận biết", "explanation": "Do $AB = AC$ theo định nghĩa tam giác cân."},
                {"id": "b", "text": "Hai tam giác $\\triangle ABM$ và $\\triangle ACM$ bằng nhau theo trường hợp cạnh - cạnh - cạnh (c-c-c).", "correct": True, "level": "Thông hiểu", "explanation": "$AB = AC, MB = MC, AM$ chung."},
                {"id": "c", "text": "Đoạn thẳng $AM$ vuông góc với đoạn thẳng $BC$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\widehat{AMB} = \\widehat{AMC} = 180^\\circ : 2 = 90^\\circ$."},
                {"id": "d", "text": "Góc $\\widehat{BAM}$ lớn hơn góc $\\widehat{CAM}$.", "correct": False, "level": "Vận dụng", "explanation": "Vì $\\triangle ABM = \\triangle ACM$ nên $\\widehat{BAM} = \\widehat{CAM}$, không có góc nào lớn hơn."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Cho tam giác $ABC$ cân tại $A$ có $\\widehat{A} = 40^\\circ$. Tính số đo góc $\\widehat{B}$ (độ).", "70", ["70", "70 độ"], "$\\widehat{B} = (180^\\circ - 40^\\circ) : 2 = 70^\\circ$."),
            make_sa(2, "Thông hiểu", "Tìm hai số $x$ và $y$ biết $\\frac{x}{3} = \\frac{y}{5}$ và $x + y = 32$. Nhập giá trị của $x$.", "12", ["12"], "$\\frac{x}{3} = \\frac{y}{5} = \\frac{32}{8} = 4 \\Rightarrow x = 12$."),
            make_sa(3, "Vận dụng", "Một miếng đất hình chữ nhật có tỉ số giữa hai cạnh là $\\frac{3}{5}$ và chu vi bằng $64\\,\\text{m}$. Tính diện tích của miếng đất hình chữ nhật đó (đơn vị: mét vuông).", "240", ["240"], "Nửa chu vi $= 32\\,\\text{m}$. Chiều rộng $= 32 : 8 \\cdot 3 = 12\\,\\text{m}$, chiều dài $= 20\\,\\text{m}$. Diện tích $= 12 \\cdot 20 = 240\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Cho $\\frac{a}{b} = \\frac{c}{d}$ (với $a, b, c, d \\neq 0$ và $a \\neq \\pm b$). Tính tỉ số $\\frac{a^2 + c^2}{b^2 + d^2}$ biết $\\frac{a}{b} = 2$.", "4", ["4"], "Ta có $\\frac{a}{b} = \\frac{c}{d} = 2 \\Rightarrow a = 2b, c = 2d \\Rightarrow a^2+c^2 = 4(b^2+d^2) \\Rightarrow$ tỉ số bằng 4.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Tìm các số $x, y$ biết $\\frac{x}{4} = \\frac{y}{7}$ và $x + y = 55$.\n b) Tìm $x$ trong tỉ lệ thức: $\\frac{x}{12} = \\frac{5}{6}$.",
                "a) Áp dụng tính chất dãy tỉ số bằng nhau: $\\frac{x}{4} = \\frac{y}{7} = \\frac{x+y}{4+7} = \\frac{55}{11} = 5 \\Rightarrow x = 20, y = 35$ (0.5đ)\nb) $x = \\frac{12 \\cdot 5}{6} = 10$ (0.5đ)",
                "a) $x = 20, y = 35$.\nb) $x = 10$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của cạnh $AC$. Trên tia đối của tia $MB$ lấy điểm $D$ sao cho $MD = MB$.\n a) Chứng minh $\\triangle ABM = \\triangle CDM$.\n b) Chứng minh $CD \\perp AC$.",
                "a) Xét $\\triangle ABM$ và $\\triangle CDM$ có: $MA = MC$ (giả thiết), $\\widehat{AMB} = \\widehat{CMD}$ (đối đỉnh), $MB = MD$ (giả thiết). Suy ra $\\triangle ABM = \\triangle CDM$ (c-g-c) (0.5đ)\nb) Từ $\\triangle ABM = \\triangle CDM \\Rightarrow \\widehat{MCD} = \\widehat{MAB} = 90^\\circ \\Rightarrow CD \\perp AC$ (0.5đ)",
                "a) Hai tam giác bằng nhau theo trường hợp cạnh - góc - cạnh (c-g-c).\nb) Hai góc tương ứng bằng nhau nên $\\widehat{MCD} = 90^\\circ \\Rightarrow CD \\perp AC$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Hưởng ứng phong trào ủng hộ sách vở cho học sinh vùng cao, ba lớp 7A, 7B, 7C đã quyên góp được tổng cộng 420 quyển sách. Biết số sách quyên góp của ba lớp tỉ lệ thuận với các số 6; 7; 8.\n a) Tính số sách mỗi lớp đã quyên góp được.\n b) Nếu lấy đi $\\frac{1}{6}$ số sách của lớp 7A chia đều cho hai lớp 7B và 7C thì số sách của lớp 7B lúc này là bao nhiêu quyển?",
                "a) Áp dụng tính chất dãy tỉ số bằng nhau: $\\frac{a}{6} = \\frac{b}{7} = \\frac{c}{8} = \\frac{420}{21} = 20$. Lớp 7A: 120 quyển; Lớp 7B: 140 quyển; Lớp 7C: 160 quyển (0.25đ)\nb) $\\frac{1}{6}$ số sách lớp 7A là $120 : 6 = 20$ quyển. Chia đều cho 7B và 7C mỗi lớp được thêm 10 quyển. Số sách lớp 7B là $140 + 10 = 150$ quyển (0.25đ)",
                "a) Số sách ba lớp quyên góp lần lượt là 120, 140, 160 quyển.\nb) Sau khi chia thêm, lớp 7B có 150 quyển sách."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 30^\\circ$. Kẻ đường cao $AH$. Trên tia đối của tia $HA$ lấy điểm $D$ sao cho $HD = HB$.\n a) Chứng minh tam giác $ABH$ vuông cân.\n b) Tính số đo góc $\\widehat{ADC}$.",
                "a) $\\triangle ABH$ vuông tại $H$ có $\\widehat{B} = 45^\\circ \\Rightarrow \\widehat{BAH} = 45^\\circ \\Rightarrow AH = BH$. Vậy tam giác $ABH$ vuông cân tại $H$ (0.25đ)\nb) Do $AH = BH$ và $HD = HB \\Rightarrow HD = HA$. $\\triangle AHD$ có $HD = HA$ và $AH \\perp BC$ nên $H$ là trung điểm $AD$, do đó $CH$ là đường trung trực của $AD \\Rightarrow CA = CD \\Rightarrow \\triangle CAD$ cân tại $C$. Trong $\\triangle AHC$ vuông tại $H$ có $\\widehat{C} = 30^\\circ \\Rightarrow \\widehat{HAC} = 60^\\circ$. Khi đó $\\triangle CAD$ cân có một góc $60^\\circ$ nên là tam giác đều $\\Rightarrow \\widehat{ADC} = 60^\\circ$ (0.25đ)",
                "a) $\\triangle ABH$ vuông tại $H$ có một góc nhọn $45^\\circ$ nên vuông cân.\nb) Chứng minh $CD = CA$ và tam giác $CAD$ là tam giác đều, suy ra $\\widehat{ADC} = 60^\\circ$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 02 ------------------
    # Ngữ cảnh: Tỉ lệ pha trộn bê tông mác 250, thiết kế khung giàn mái nhà chữ A cân, phân tích biểu đồ quạt tròn chi tiêu
    exams.append({
        "id": "p_g7_final1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 02)",
        "topic": "Tỉ lệ thức, Tam giác bằng nhau (c-g-c, g-c-g), Đường trung trực & Biểu đồ hình quạt tròn",
        "grade": "7",
        "term": "final1",
        "termName": "Cuối Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Đường trung trực của đoạn thẳng $AB$ là:", ["Đường thẳng vuông góc với $AB$ tại trung điểm của nó", "Đoạn thẳng nối hai điểm $A$ và $B$", "Đường thẳng đi qua trung điểm của $AB$", "Tia phân giác của đoạn thẳng $AB$"], 0, "Định nghĩa đường trung trực của đoạn thẳng."),
            make_mc(2, "Nhận biết", "Trong biểu đồ hình quạt tròn, toàn bộ hình tròn biểu diễn:", ["$100\\%$", "$50\\%$", "$360\\%$", "$180\\%$"], 0, "Toàn bộ hình tròn biểu diễn 100% tổng thể dữ liệu."),
            make_mc(3, "Nhận biết", "Hai tam giác bằng nhau là hai tam giác có:", ["Các cạnh tương ứng bằng nhau và các góc tương ứng bằng nhau", "Ba cạnh bằng nhau", "Ba góc bằng nhau", "Diện tích bằng nhau"], 0, "Định nghĩa hai tam giác bằng nhau."),
            make_mc(4, "Thông hiểu", "Cho tỉ lệ thức $\\frac{x}{6} = \\frac{-3}{2}$. Giá trị của $x$ là:", ["$-9$", "$9$", "$-4$", "$4$"], 0, "$x = \\frac{6 \\cdot (-3)}{2} = -9$."),
            make_mc(5, "Thông hiểu", "Tam giác $MNP$ có $MN = MP$ và $\\widehat{M} = 80^\\circ$. Số đo góc $\\widehat{N}$ bằng:", ["$50^\\circ$", "$80^\\circ$", "$100^\\circ$", "$40^\\circ$"], 0, "$\\triangle MNP$ cân tại $M \\Rightarrow \\widehat{N} = (180^\\circ - 80^\\circ) : 2 = 50^\\circ$."),
            make_mc(6, "Thông hiểu", "Cho $\\triangle ABC = \\triangle DEF$. Biết $\\widehat{A} = 60^\\circ, \\widehat{E} = 75^\\circ$. Số đo góc $\\widehat{C}$ bằng:", ["$45^\\circ$", "$60^\\circ$", "$75^\\circ$", "$55^\\circ$"], 0, "$\\widehat{B} = \\widehat{E} = 75^\\circ \\Rightarrow \\widehat{C} = 180^\\circ - (60^\\circ + 75^\\circ) = 45^\\circ$."),
            make_mc(7, "Vận dụng", "Để trộn vữa xây dựng theo tiêu chuẩn, tỉ lệ thể tích giữa xi măng, cát và đá dăm lần lượt là 1; 2; 4. Bác thợ xây cần dùng $1,4\\,\\text{m}^3$ vữa. Thể tích cát cần dùng là:", ["$0,4\\,\\text{m}^3$", "$0,2\\,\\text{m}^3$", "$0,8\\,\\text{m}^3$", "$0,6\\,\\text{m}^3$"], 0, "Tổng số phần: $1 + 2 + 4 = 7$ phần. Cát chiếm 2 phần: $1,4 : 7 \\cdot 2 = 0,4\\,\\text{m}^3$."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ cân tại $A$. Kẻ $AH \\perp BC$ ($H \\in BC$). Biết $AB = 10\\,\\text{cm}$, $BC = 12\\,\\text{cm}$. Độ dài đường cao $AH$ là:", ["$8\\,\\text{cm}$", "$6\\,\\text{cm}$", "$7\\,\\text{cm}$", "$9\\,\\text{cm}$"], 0, "$H$ là trung điểm $BC \\Rightarrow BH = 6\\,\\text{cm}$. Áp dụng Pytago: $AH = \\sqrt{10^2 - 6^2} = 8\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm các số $x, y$ biết $\\frac{x}{3} = \\frac{y}{4}$ và $x^2 + y^2 = 100$ ($x, y > 0$).", ["$x = 6, y = 8$", "$x = 8, y = 6$", "$x = 3, y = 4$", "$x = 9, y = 16$"], 0, "Đặt $x = 3k, y = 4k \\Rightarrow 9k^2 + 16k^2 = 25k^2 = 100 \\Rightarrow k = 2$ ($k > 0$). Vậy $x = 6, y = 8$."),
            make_mc(10, "Vận dụng cao", "Cho tam giác $ABC$ có ba góc nhọn. Vẽ đường cao $AH$. Lấy điểm $D$ sao cho $AB$ là đường trung trực của $HD$, lấy điểm $E$ sao cho $AC$ là đường trung trực của $HE$. Khẳng định nào sau đây đúng?", ["$AD = AE$", "$AD \\perp AE$", "$D, A, E$ thẳng hàng", "$\\triangle ADE$ đều"], 0, "Do tính chất đường trung trực: $AD = AH$ và $AE = AH \\Rightarrow AD = AE$."),
            make_mc(11, "Vận dụng cao", "Có bao nhiêu cặp số nguyên $(x, y)$ thỏa mãn: $\\frac{x}{5} = \\frac{3}{y}$ với $x > y$?", ["$4$", "$2$", "$8$", "$6$"], 0, "$xy = 15$. Các ước của 15 là $(\\pm 1, \\pm 15), (\\pm 3, \\pm 5)$. Có 8 cặp $(x, y)$, trong đó một nửa có $x > y$, tức đúng 4 cặp."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{C} = 30^\\circ$. Đường trung trực của cạnh $BC$ cắt $AC$ tại điểm $M$. Khẳng định nào sau đây đúng?", ["$BM = MC = AM$", "$BM = 2MC$", "$AM = MC$", "$\\triangle ABM$ cân tại $B$"], 0, "Do $M$ thuộc trung trực $BC \\Rightarrow MB = MC \\Rightarrow \\triangle MBC$ cân tại $M$, góc $\\widehat{MBC} = 30^\\circ \\Rightarrow \\widehat{ABM} = 60^\\circ - 30^\\circ = 30^\\circ$. Trong $\\triangle ABM$ vuông tại $A$ có $\\widehat{ABM} = 30^\\circ$ nên $AM = \\frac{1}{2}BM$.")
        ],
        "part2": [
            make_tf(1, "Một cửa hàng kinh doanh hoa quả nhập về 240 kg thanh long ruột đỏ. Theo số liệu thống kê: Ngày thứ nhất bán được $30\\%$ tổng số hàng, Ngày thứ hai bán được $\\frac{5}{12}$ tổng số hàng, phần còn lại bán trong Ngày thứ ba.", [
                {"id": "a", "text": "Khối lượng thanh long bán trong ngày thứ nhất là 72 kg.", "correct": True, "level": "Nhận biết", "explanation": "$240 \\cdot 30\\% = 72\\,\\text{kg}$."},
                {"id": "b", "text": "Khối lượng thanh long bán trong ngày thứ hai là 100 kg.", "correct": True, "level": "Nhận biết", "explanation": "$240 \\cdot \\frac{5}{12} = 100\\,\\text{kg}$."},
                {"id": "c", "text": "Khối lượng thanh long bán trong ngày thứ ba là 68 kg.", "correct": True, "level": "Thông hiểu", "explanation": "$240 - (72 + 100) = 68\\,\\text{kg}$."},
                {"id": "d", "text": "Tỉ số phần trăm của số hàng bán ngày thứ ba so với cả đợt là $30\\%$.", "correct": False, "level": "Vận dụng", "explanation": "Tỉ số là $68 : 240 \\approx 28,33\\% \\neq 30\\%$."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$. Gọi $D$ là điểm trên cạnh $BC$ sao cho $BD = BA$. Qua $D$ kẻ đường thẳng vuông góc với $BC$, cắt $AC$ tại điểm $E$.", [
                {"id": "a", "text": "Góc $\\widehat{BAC}$ là góc vuông ($90^\\circ$).", "correct": True, "level": "Nhận biết", "explanation": "Tam giác vuông tại $A$."},
                {"id": "b", "text": "Hai tam giác vuông $\\triangle ABE$ và $\\triangle DBE$ bằng nhau theo trường hợp cạnh huyền - cạnh góc vuông.", "correct": True, "level": "Thông hiểu", "explanation": "Cạnh huyền $BE$ chung, $BA = BD$."},
                {"id": "c", "text": "Tia $BE$ là tia phân giác của góc $\\widehat{ABC}$.", "correct": True, "level": "Thông hiểu", "explanation": "Từ $\\triangle ABE = \\triangle DBE \\Rightarrow \\widehat{ABE} = \\widehat{DBE}$."},
                {"id": "d", "text": "Đoạn thẳng $AE$ dài hơn đoạn thẳng $ED$.", "correct": False, "level": "Vận dụng", "explanation": "Vì $\\triangle ABE = \\triangle DBE$ nên $AE = ED$, không thể dài hơn."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm số đo góc ở đáy của một tam giác cân biết góc ở đỉnh bằng $50^\\circ$ (độ).", "65", ["65", "65 độ"], "$(180^\\circ - 50^\\circ) : 2 = 65^\\circ$."),
            make_sa(2, "Thông hiểu", "Tìm hai số $x$ và $y$ biết $\\frac{x}{4} = \\frac{y}{7}$ và $y - x = 15$. Nhập giá trị của $x$.", "20", ["20"], "$\\frac{y-x}{7-4} = \\frac{15}{3} = 5 \\Rightarrow x = 20$."),
            make_sa(3, "Vận dụng", "Để làm xong một đoạn đường trong 15 ngày cần 24 công nhân. Nếu muốn hoàn thành đoạn đường đó sớm hơn 3 ngày thì cần bổ sung thêm bao nhiêu công nhân (năng suất làm việc như nhau)?", "6", ["6", "6 người"], "Số ngày cần làm: $15 - 3 = 12$ ngày. Số người cần: $(24 \\cdot 15) : 12 = 30$ người. Cần thêm: $30 - 24 = 6$ công nhân."),
            make_sa(4, "Vận dụng cao", "Cho tam giác $ABC$ cân tại $A$. Trên cạnh $AB$ lấy điểm $M$, trên cạnh $AC$ lấy điểm $N$ sao cho $AM = AN$. Biết $\\widehat{A} = 80^\\circ$, tính số đo góc $\\widehat{AMN}$ (độ).", "50", ["50", "50 độ"], "$\\triangle AMN$ cân tại $A \\Rightarrow \\widehat{AMN} = (180^\\circ - 80^\\circ) : 2 = 50^\\circ$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Cho tỉ lệ thức $\\frac{x}{5} = \\frac{y}{9}$ và $x + y = 28$. Tìm $x$ và $y$.\n b) Tính góc ở đáy của một tam giác cân có góc ở đỉnh bằng $70^\\circ$.",
                "a) $\\frac{x}{5} = \\frac{y}{9} = \\frac{28}{14} = 2 \\Rightarrow x = 10, y = 18$ (0.5đ)\nb) Góc ở đáy: $(180^\\circ - 70^\\circ) : 2 = 55^\\circ$ (0.5đ)",
                "a) $x = 10, y = 18$.\nb) Số đo góc ở đáy là $55^\\circ$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ có $AB = AC$. Gọi $D$ là trung điểm của cạnh $BC$.\n a) Chứng minh $\\triangle ABD = \\triangle ACD$.\n b) Chứng minh $AD \\perp BC$.",
                "a) Xét $\\triangle ABD$ và $\\triangle ACD$ có: $AB = AC$ (giả thiết), $BD = CD$ ($D$ là trung điểm $BC$), $AD$ cạnh chung. Suy ra $\\triangle ABD = \\triangle ACD$ (c-c-c) (0.5đ)\nb) Từ $\\triangle ABD = \\triangle ACD \\Rightarrow \\widehat{ADB} = \\widehat{ADC}$. Mà $\\widehat{ADB} + \\widehat{ADC} = 180^\\circ$ (kề bù) nên $\\widehat{ADB} = \\widehat{ADC} = 90^\\circ \\Rightarrow AD \\perp BC$ (0.5đ)",
                "a) $\\triangle ABD = \\triangle ACD$ theo trường hợp c-c-c.\nb) Hai góc kề bù bằng nhau nên mỗi góc bằng $90^\\circ \\Rightarrow AD \\perp BC$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu đất hình chữ nhật có chu vi bằng $180\\,\\text{m}$, tỉ số giữa chiều dài và chiều rộng là $\\frac{5}{4}$.\n a) Tính chiều dài và chiều rộng của khu đất.\n b) Người ta dành $30\\%$ diện tích khu đất để xây dựng hồ bơi nhân tạo. Tính diện tích hồ bơi nhân tạo.",
                "a) Nửa chu vi: $180 : 2 = 90\\,\\text{m}$. Chiều dài: $90 : (5 + 4) \\cdot 5 = 50\\,\\text{m}$. Chiều rộng: $90 - 50 = 40\\,\\text{m}$ (0.25đ)\nb) Diện tích khu đất: $50 \\cdot 40 = 2000\\,\\text{m}^2$. Diện tích hồ bơi: $2000 \\cdot 30\\% = 600\\,\\text{m}^2$ (0.25đ)",
                "a) Chiều dài là $50\\,\\text{m}$, chiều rộng là $40\\,\\text{m}$.\nb) Diện tích hồ bơi nhân tạo là $600\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ vuông cân tại $A$. Qua $A$ kẻ đường thẳng $d$ bất kì không cắt cạnh $BC$. Kẻ $BH \\perp d$ và $CK \\perp d$ ($H, K \\in d$).\n Chứng minh rằng $BH^2 + CK^2$ không đổi khi đường thẳng $d$ thay đổi vị trí quanh đỉnh $A$.",
                "Xét $\\triangle ABH$ vuông tại $H$ và $\\triangle CAK$ vuông tại $K$:\nCó $AB = AC$ (giả thiết).\nLại có $\\widehat{ABH} + \\widehat{BAH} = 90^\\circ$ và $\\widehat{CAK} + \\widehat{BAH} = 90^\\circ$ (vì $\\widehat{BAC} = 90^\\circ$).\nSuy ra $\\widehat{ABH} = \\widehat{CAK}$.\nDo đó $\\triangle ABH = \\triangle CAK$ (cạnh huyền - góc nhọn) (0.25đ)\n$\\Rightarrow BH = AK$ và $AH = CK$.\nÁp dụng định lí Pytago trong $\\triangle ABH$ vuông tại $H$:\n$BH^2 + CK^2 = BH^2 + AH^2 = AB^2$.\nVì cạnh $AB$ của tam giác vuông cân $ABC$ cố định nên $AB^2$ không đổi. Vậy $BH^2 + CK^2$ luôn không đổi (đpcm) (0.25đ)",
                "Chứng minh $\\triangle ABH = \\triangle CAK$ (cạnh huyền - góc nhọn), suy ra $CK = AH$. Thay vào ta có $BH^2 + CK^2 = BH^2 + AH^2 = AB^2$ không đổi."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 03 ------------------
    # Ngữ cảnh: Xưởng may đồng phục, khung mái lều chữ A, biểu đồ đoạn thẳng lượng mưa
    exams.append({
        "id": "p_g7_final1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 03)",
        "topic": "Dãy tỉ số bằng nhau, Tam giác vuông bằng nhau, Tam giác cân & Biểu đồ đoạn thẳng",
        "grade": "7",
        "term": "final1",
        "termName": "Cuối Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Cho tam giác $ABC$ vuông tại $A$. Cạnh đối diện với góc vuông được gọi là:", ["Cạnh huyền", "Cạnh góc vuông", "Đường trung tuyến", "Đường cao"], 0, "Cạnh đối diện góc vuông trong tam giác vuông là cạnh huyền."),
            make_mc(2, "Nhận biết", "Biểu đồ đoạn thẳng thường được sử dụng để biểu diễn:", ["Sự thay đổi của một đại lượng theo thời gian", "Tỉ lệ phần trăm của các phần tử trong tổng thể", "Phân loại dữ liệu không theo thứ tự", "Mật độ dân số"], 0, "Biểu đồ đoạn thẳng dùng để biểu diễn xu hướng biến thiên của đại lượng theo thời gian."),
            make_mc(3, "Nhận biết", "Nếu $\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$ thì dãy tỉ số nào sau đây đúng?", ["$\\frac{x+y+z}{a+b+c}$", "$\\frac{x-y+z}{a-b-c}$", "$\\frac{x+y-z}{a+b+c}$", "$\\frac{x+y+z}{a-b+c}$"], 0, "Tính chất dãy tỉ số bằng nhau: $\\frac{x+y+z}{a+b+c}$."),
            make_mc(4, "Thông hiểu", "Cho tam giác $DEF$ cân tại $D$ có $\\widehat{E} = 65^\\circ$. Số đo góc ở đỉnh $\\widehat{D}$ bằng:", ["$50^\\circ$", "$65^\\circ$", "$130^\\circ$", "$115^\\circ$"], 0, "$\\widehat{D} = 180^\\circ - 2 \\cdot 65^\\circ = 50^\\circ$."),
            make_mc(5, "Thông hiểu", "Cho $\\triangle ABC = \\triangle MNP$. Biết $AB = 6\\,\\text{cm}, \\widehat{B} = 45^\\circ$. Cạnh và góc tương ứng của tam giác $MNP$ là:", ["$MN = 6\\,\\text{cm}, \\widehat{N} = 45^\\circ$", "$NP = 6\\,\\text{cm}, \\widehat{M} = 45^\\circ$", "$MP = 6\\,\\text{cm}, \\widehat{P} = 45^\\circ$", "$MN = 6\\,\\text{cm}, \\widehat{P} = 45^\\circ$"], 0, "$MN$ tương ứng với $AB$, $\\widehat{N}$ tương ứng với $\\widehat{B}$."),
            make_mc(6, "Thông hiểu", "Biết $x$ và $y$ tỉ lệ thuận với nhau và khi $x = 3$ thì $y = 12$. Hệ số tỉ lệ của $y$ đối với $x$ là:", ["$4$", "$\\frac{1}{4}$", "$36$", "$9$"], 0, "$k = \\frac{y}{x} = \\frac{12}{3} = 4$."),
            make_mc(7, "Vận dụng", "Ba phân xưởng cùng may một mẫu áo khoác đồng phục. Số áo may được của ba phân xưởng tỉ lệ với 4; 5; 6. Biết phân xưởng thứ ba may nhiều hơn phân xưởng thứ nhất 40 chiếc áo. Tổng số áo may được của cả ba phân xưởng là:", ["$300$ chiếc", "$200$ chiếc", "$250$ chiếc", "$320$ chiếc"], 0, "Giá trị 1 phần: $40 : (6 - 4) = 20$ chiếc. Tổng 3 xưởng: $(4 + 5 + 6) \\cdot 20 = 300$ chiếc."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ có $AB = AC = 13\\,\\text{cm}$, đường cao $AH = 12\\,\\text{cm}$. Độ dài cạnh đáy $BC$ là:", ["$10\\,\\text{cm}$", "$5\\,\\text{cm}$", "$8\\,\\text{cm}$", "$12\\,\\text{cm}$"], 0, "Tam giác $AHB$ vuông tại $H$: $BH = \\sqrt{13^2 - 12^2} = 5\\,\\text{cm} \\Rightarrow BC = 2BH = 10\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm số thực $x$ thỏa mãn: $\\frac{x - 1}{x + 5} = \\frac{6}{7}$.", ["$x = 37$", "$x = 42$", "$x = 35$", "$x = 29$"], 0, "$7(x - 1) = 6(x + 5) \\Rightarrow 7x - 7 = 6x + 30 \\Rightarrow x = 37$."),
            make_mc(10, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{A} = 90^\\circ$, $AB = AC$. Qua $A$ kẻ đường thẳng $xy$ (không cắt đoạn thẳng $BC$). Kẻ $BD \\perp xy, CE \\perp xy$. Khẳng định nào sau đây đúng?", ["$DE = BD + CE$", "$DE = BD - CE$", "$DE = 2BD$", "$DE = 2CE$"], 0, "Chứng minh $\\triangle ABD = \\triangle CAE \\Rightarrow AD = CE$ và $BD = AE \\Rightarrow DE = AD + AE = CE + BD$."),
            make_mc(11, "Vận dụng cao", "Cho dãy tỉ số bằng nhau $\\frac{2a+b+c+d}{a} = \\frac{a+2b+c+d}{b} = \\frac{a+b+2c+d}{c} = \\frac{a+b+c+2d}{d}$. Giá trị của biểu thức $P = \\frac{a+b}{c+d} + \\frac{b+c}{d+a} + \\frac{c+d}{a+b} + \\frac{d+a}{b+c}$ khi $a+b+c+d \\neq 0$ là:", ["$4$", "$2$", "$1$", "$8$"], 0, "Trừ 1 ở mỗi tỉ số suy ra $\\frac{a+b+c+d}{a} = \\dots \\Rightarrow a = b = c = d$. Khi đó mỗi phân số bằng 1, tổng bằng 4."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ vuông cân tại $A$. Điểm $M$ nằm trong tam giác sao cho $MA = 2\\,\\text{cm}, MB = 1\\,\\text{cm}$ và $\\widehat{AMB} = 135^\\circ$. Độ dài đoạn thẳng $MC$ là:", ["$\\sqrt{7}\\,\\text{cm}$", "$3\\,\\text{cm}$", "$\\sqrt{5}\\,\\text{cm}$", "$\\sqrt{10}\\,\\text{cm}$"], 0, "Quay tam giác $ABM$ một góc $90^\\circ$ quanh đỉnh $A$ thành $\\triangle ACK$. Áp dụng Pytago tính được $MC = \\sqrt{7}\\,\\text{cm}$.")
        ],
        "part2": [
            make_tf(1, "Một đoàn tàu du lịch có 3 loại toa: Toa cao cấp, Toa tiêu chuẩn và Toa phổ thông. Số lượng ghế của ba loại toa tỉ lệ với các số 2; 3; 5. Biết tổng số ghế trên đoàn tàu là 400 ghế.", [
                {"id": "a", "text": "Tổng số phần bằng nhau của ba loại ghế là 10 phần.", "correct": True, "level": "Nhận biết", "explanation": "$2 + 3 + 5 = 10$ phần."},
                {"id": "b", "text": "Số ghế của Toa cao cấp là 80 ghế.", "correct": True, "level": "Nhận biết", "explanation": "$400 : 10 \\cdot 2 = 80$ ghế."},
                {"id": "c", "text": "Số ghế của Toa phổ thông là 200 ghế.", "correct": True, "level": "Thông hiểu", "explanation": "$400 : 10 \\cdot 5 = 200$ ghế."},
                {"id": "d", "text": "Số ghế Toa tiêu chuẩn chiếm đúng $40\\%$ tổng số ghế của đoàn tàu.", "correct": False, "level": "Vận dụng", "explanation": "Toa tiêu chuẩn có 120 ghế, chiếm $120 : 400 = 30\\% \\neq 40\\%$."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$. Kẻ tia phân giác $BD$ của góc $\\widehat{ABC}$ ($D \\in AC$). Trên cạnh $BC$ lấy điểm $E$ sao cho $BE = BA$.", [
                {"id": "a", "text": "Góc $\\widehat{BAC}$ bằng $90^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "Tam giác vuông tại $A$."},
                {"id": "b", "text": "Hai tam giác $\\triangle ABD$ và $\\triangle EBD$ bằng nhau theo trường hợp cạnh - góc - cạnh (c-g-c).", "correct": True, "level": "Thông hiểu", "explanation": "$BA = BE$, $\\widehat{ABD} = \\widehat{EBD}$, $BD$ chung."},
                {"id": "c", "text": "Đoạn thẳng $DE$ vuông góc với đoạn thẳng $BC$.", "correct": True, "level": "Thông hiểu", "explanation": "Từ $\\triangle ABD = \\triangle EBD \\Rightarrow \\widehat{DEB} = \\widehat{DAB} = 90^\\circ$."},
                {"id": "d", "text": "Độ dài đoạn thẳng $AD$ lớn hơn độ dài đoạn thẳng $DE$.", "correct": False, "level": "Vận dụng", "explanation": "Vì $\\triangle ABD = \\triangle EBD$ nên $AD = DE$ (hai cạnh tương ứng), không thể lớn hơn."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Một tam giác cân có góc ở đỉnh bằng $100^\\circ$. Tính số đo góc ở đáy của tam giác đó (độ).", "40", ["40", "40 độ"], "$(180^\\circ - 100^\\circ) : 2 = 40^\\circ$."),
            make_sa(2, "Thông hiểu", "Tìm hai số $x$ và $y$ biết $\\frac{x}{2} = \\frac{y}{5}$ và $x \\cdot y = 40$ ($x, y > 0$). Nhập giá trị của $x$.", "4", ["4"], "Đặt $x = 2k, y = 5k \\Rightarrow 10k^2 = 40 \\Rightarrow k = 2 \\Rightarrow x = 4$."),
            make_sa(3, "Vận dụng", "Một đội máy xúc gồm 5 máy làm việc trong 6 ngày thì đào xong một đoạn mương dẫn nước. Hỏi nếu muốn hoàn thành công việc đó trong 3 ngày thì cần bao nhiêu máy xúc (công suất các máy như nhau)?", "10", ["10", "10 máy"], "Số ngày và số máy tỉ lệ nghịch: $(5 \\cdot 6) : 3 = 10$ máy."),
            make_sa(4, "Vận dụng cao", "Cho $\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{a}$. Tính giá trị của biểu thức $M = \\frac{a^{2024} + b^{2024} + c^{2024}}{a^{1012} b^{1012} + b^{1012} c^{1012} + c^{1012} a^{1012}}$.", "1", ["1"], "Từ dãy tỉ số bằng nhau suy ra $a = b = c$. Khi đó tử số bằng $3a^{2024}$, mẫu số bằng $3a^{2024}$, tỉ số bằng 1.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Cho $\\frac{x}{3} = \\frac{y}{8}$ và $x + y = 44$. Tìm $x$ và $y$.\n b) Tìm $x$ trong tỉ lệ thức: $\\frac{x - 2}{4} = \\frac{9}{6}$.",
                "a) $\\frac{x}{3} = \\frac{y}{8} = \\frac{44}{11} = 4 \\Rightarrow x = 12, y = 32$ (0.5đ)\nb) $x - 2 = \\frac{4 \\cdot 9}{6} = 6 \\Rightarrow x = 8$ (0.5đ)",
                "a) $x = 12, y = 32$.\nb) $x = 8$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ có $AB = AC$. Gọi $M$ là trung điểm của $BC$.\n a) Chứng minh $\\triangle ABM = \\triangle ACM$.\n b) Chứng minh tia $AM$ là tia phân giác của góc $\\widehat{BAC}$.",
                "a) Xét $\\triangle ABM$ và $\\triangle ACM$ có: $AB = AC$ (giả thiết), $BM = CM$ (trung điểm), $AM$ chung. Suy ra $\\triangle ABM = \\triangle ACM$ (c-c-c) (0.5đ)\nb) Từ $\\triangle ABM = \\triangle ACM \\Rightarrow \\widehat{BAM} = \\widehat{CAM}$. Suy ra $AM$ là tia phân giác của $\\widehat{BAC}$ (0.5đ)",
                "a) Hai tam giác bằng nhau theo c-c-c.\nb) Hai góc tương ứng bằng nhau nên $AM$ là tia phân giác của $\\widehat{BAC}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Số học sinh của ba lớp 7A, 7B, 7C tham gia ngày Chủ nhật xanh dọn rác bãi biển tỉ lệ với các số 8; 9; 10. Biết số học sinh lớp 7C nhiều hơn số học sinh lớp 7A là 8 bạn.\n a) Tính số học sinh của mỗi lớp tham gia hoạt động.\n b) Tổng số học sinh của cả ba lớp tham gia là bao nhiêu bạn?",
                "a) Gọi số học sinh là $a, b, c$. Áp dụng dãy tỉ số: $\\frac{a}{8} = \\frac{b}{9} = \\frac{c}{10} = \\frac{c-a}{10-8} = \\frac{8}{2} = 4$. Lớp 7A: 32 bạn; 7B: 36 bạn; 7C: 40 bạn (0.25đ)\nb) Tổng số học sinh: $32 + 36 + 40 = 108$ bạn (0.25đ)",
                "a) Lớp 7A: 32 học sinh; 7B: 36 học sinh; 7C: 40 học sinh.\nb) Tổng số học sinh là 108 bạn."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ vuông cân tại $A$. Điểm $M$ nằm trên cạnh huyền $BC$. Kẻ $MD \\perp AB$ ($D \\in AB$) và $ME \\perp AC$ ($E \\in AC$).\n a) Chứng minh tứ giác $ADME$ có ba góc vuông.\n b) Xác định vị trí của điểm $M$ trên cạnh $BC$ để đoạn thẳng $DE$ có độ dài nhỏ nhất.",
                "a) Có $\\widehat{DAE} = 90^\\circ, \\widehat{MDA} = 90^\\circ, \\widehat{MEA} = 90^\\circ$. Vậy tứ giác có 3 góc vuông (0.25đ)\nb) Tứ giác $ADME$ là hình chữ nhật nên $DE = AM$. Để $DE$ ngắn nhất thì đoạn thẳng $AM$ ngắn nhất. Khoảng cách ngắn nhất từ $A$ đến đường thẳng $BC$ chính là đường cao hạ từ $A$. Khi đó $AM \\perp BC$. Do $\\triangle ABC$ vuông cân tại $A$ nên $M$ trùng với trung điểm của cạnh huyền $BC$ (0.25đ)",
                "a) Chứng minh tứ giác $ADME$ có 3 góc vuông nên là hình chữ nhật, suy ra $DE = AM$.\nb) $DE$ ngắn nhất khi $AM$ ngắn nhất, tức $AM \\perp BC$, khi đó $M$ là trung điểm của cạnh huyền $BC$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 04 ------------------
    # Ngữ cảnh: Hệ thống trồng rau khí canh, thiết kế cầu thang chữ L, phân tích biểu đồ quạt tròn cơ cấu ngành
    exams.append({
        "id": "p_g7_final1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 04)",
        "topic": "Tỉ lệ thuận - Tỉ lệ nghịch, Các trường hợp bằng nhau của tam giác vuông & Biểu đồ hình quạt tròn",
        "grade": "7",
        "term": "final1",
        "termName": "Cuối Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Hai tam giác vuông bằng nhau khi có:", ["Hai cạnh góc vuông tương ứng bằng nhau", "Một cạnh góc vuông bằng nhau", "Một góc nhọn bằng nhau", "Cạnh huyền bằng nhau"], 0, "Trường hợp bằng nhau của hai tam giác vuông: hai cạnh góc vuông."),
            make_mc(2, "Nhận biết", "Nếu đại lượng $y$ liên hệ với đại lượng $x$ theo công thức $y = \\frac{a}{x}$ ($a \\neq 0$) thì ta nói:", ["$y$ tỉ lệ nghịch với $x$", "$y$ tỉ lệ thuận với $x$", "$y$ bằng $x$", "$y$ tỉ lệ với $a$"], 0, "Định nghĩa đại lượng tỉ lệ nghịch."),
            make_mc(3, "Nhận biết", "Trong tam giác đều, số đo của mỗi góc bằng:", ["$60^\\circ$", "$90^\\circ$", "$45^\\circ$", "$180^\\circ$"], 0, "Mỗi góc của tam giác đều bằng $60^\\circ$."),
            make_mc(4, "Thông hiểu", "Cho tỉ lệ thức $\\frac{x}{15} = \\frac{4}{5}$. Giá trị của $x$ là:", ["$12$", "$15$", "$10$", "$20$"], 0, "$x = \\frac{15 \\cdot 4}{5} = 12$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = \\widehat{C}$. Tam giác $ABC$ là tam giác gì?", ["Tam giác cân tại $A$", "Tam giác đều", "Tam giác vuông tại $A$", "Tam giác tù"], 0, "Tam giác có hai góc ở đáy bằng nhau là tam giác cân tại đỉnh $A$."),
            make_mc(6, "Thông hiểu", "Cho $\\triangle ABC = \\triangle MNP$. Biết $\\widehat{A} = 50^\\circ, \\widehat{P} = 60^\\circ$. Số đo góc $\\widehat{B}$ bằng:", ["$70^\\circ$", "$50^\\circ$", "$60^\\circ$", "$80^\\circ$"], 0, "$\\widehat{C} = \\widehat{P} = 60^\\circ \\Rightarrow \\widehat{B} = 180^\\circ - (50^\\circ + 60^\\circ) = 70^\\circ$."),
            make_mc(7, "Vận dụng", "Một ô tô đi từ A đến B với vận tốc $60\\,\\text{km/h}$ hết 3 giờ. Khi từ B trở về A, do trời mưa ô tô đi với vận tốc $45\\,\\text{km/h}$. Thời gian ô tô đi từ B về A là:", ["$4$ giờ", "$3,5$ giờ", "$4,5$ giờ", "$5$ giờ"], 0, "Quãng đường: $60 \\cdot 3 = 180\\,\\text{km}$. Thời gian về: $180 : 45 = 4$ giờ."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ cân tại $A$ có $\\widehat{A} = 120^\\circ$. Kẻ $AH \\perp BC$ ($H \\in BC$). Trên tia đối của tia $HA$ lấy điểm $D$ sao cho $HD = HA$. Khẳng định nào sau đây đúng?", ["$\\triangle ABD$ là tam giác đều", "$\\triangle ABD$ vuông cân", "$\\widehat{ABD} = 90^\\circ$", "$AD = BC$"], 0, "$\\widehat{B} = 30^\\circ \\Rightarrow \\widehat{BAH} = 60^\\circ$. Do $HA = HD$ và $AH \\perp BD$ nên $BH$ là trung trực $AD \\Rightarrow BA = BD$. Tam giác $ABD$ cân có góc $60^\\circ$ nên là tam giác đều."),
            make_mc(9, "Vận dụng cao", "Tìm ba số $x, y, z$ biết: $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4}$ và $x^2 + y^2 + z^2 = 116$ ($x, y, z > 0$).", ["$x = 4, y = 6, z = 8$", "$x = 2, y = 3, z = 4$", "$x = 6, y = 9, z = 12$", "$x = 8, y = 12, z = 16$"], 0, "Đặt $x = 2k, y = 3k, z = 4k \\Rightarrow 4k^2 + 9k^2 + 16k^2 = 29k^2 = 116 \\Rightarrow k = 2$. Vậy $x = 4, y = 6, z = 8$."),
            make_mc(10, "Vận dụng cao", "Cho tam giác $ABC$ có góc $\\widehat{A} = 60^\\circ$. Các tia phân giác của góc $B$ và $C$ cắt nhau tại $I$. Số đo của góc $\\widehat{BIC}$ bằng:", ["$120^\\circ$", "$150^\\circ$", "$110^\\circ$", "$135^\\circ$"], 0, "$\\widehat{BIC} = 90^\\circ + \\frac{\\widehat{A}}{2} = 90^\\circ + 30^\\circ = 120^\\circ$."),
            make_mc(11, "Vận dụng cao", "Tìm số nguyên $x$ sao cho tỉ lệ thức $\\frac{x - 3}{4} = \\frac{9}{x - 3}$ có nghiệm nguyên.", ["$x \\in \\{-3; 9\\}$", "$x = 9$", "$x = -3$", "$x \\in \\{3; 6\\}$"], 0, "$(x - 3)^2 = 36 \\Rightarrow x - 3 = 6 \\Rightarrow x = 9$ hoặc $x - 3 = -6 \\Rightarrow x = -3$."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ có trung tuyến $AM = \\frac{1}{2}BC$. Khẳng định nào sau đây đúng?", ["Tam giác $ABC$ vuông tại $A$", "Tam giác $ABC$ cân tại $A$", "Tam giác $ABC$ đều", "Tam giác $ABC$ vuông tại $B$"], 0, "Định lí: Nếu một tam giác có đường trung tuyến ứng với một cạnh bằng một nửa cạnh đó thì tam giác đó là tam giác vuông.")
        ],
        "part2": [
            make_tf(1, "Một khu công nghiệp có 3 xí nghiệp A, B, C có số lượng công nhân tỉ lệ thuận với 3; 5; 7. Ban quản lý khu công nghiệp cấp 300 suất quà tết chia cho 3 xí nghiệp theo tỉ lệ trên.", [
                {"id": "a", "text": "Tổng số phần bằng nhau của 3 xí nghiệp là 15 phần.", "correct": True, "level": "Nhận biết", "explanation": "$3 + 5 + 7 = 15$ phần."},
                {"id": "b", "text": "Mỗi phần bằng nhau có giá trị là 20 suất quà.", "correct": True, "level": "Nhận biết", "explanation": "$300 : 15 = 20$ suất."},
                {"id": "c", "text": "Xí nghiệp B nhận được 100 suất quà tết.", "correct": True, "level": "Thông hiểu", "explanation": "$20 \\cdot 5 = 100$ suất."},
                {"id": "d", "text": "Xí nghiệp C nhận nhiều hơn xí nghiệp A đúng 100 suất quà tết.", "correct": False, "level": "Vận dụng", "explanation": "Xí nghiệp C hơn A là $(7 - 3) \\cdot 20 = 80$ suất quà, không phải 100 suất."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ cân tại $A$. Kẻ $AH \\perp BC$ ($H \\in BC$).", [
                {"id": "a", "text": "Tam giác $ABC$ có hai cạnh bên $AB = AC$.", "correct": True, "level": "Nhận biết", "explanation": "Định nghĩa tam giác cân."},
                {"id": "b", "text": "Hai tam giác vuông $\\triangle ABH$ và $\\triangle ACH$ bằng nhau theo trường hợp cạnh huyền - cạnh góc vuông.", "correct": True, "level": "Thông hiểu", "explanation": "Cạnh huyền $AB = AC$, cạnh chung $AH$."},
                {"id": "c", "text": "Điểm $H$ là trung điểm của đoạn thẳng $BC$.", "correct": True, "level": "Thông hiểu", "explanation": "Từ $\\triangle ABH = \\triangle ACH \\Rightarrow HB = HC$."},
                {"id": "d", "text": "Góc $\\widehat{BAH}$ luôn bằng góc $\\widehat{ABC}$.", "correct": False, "level": "Vận dụng", "explanation": "$\\widehat{BAH} = 90^\\circ - \\widehat{ABC}$, chỉ bằng nhau khi tam giác vuông cân ($45^\\circ$), không thể luôn bằng nhau."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Cho tam giác đều $MNP$. Tính số đo của góc $\\widehat{M}$ (độ).", "60", ["60", "60 độ"], "Tam giác đều có 3 góc bằng nhau và bằng $60^\\circ$."),
            make_sa(2, "Thông hiểu", "Tìm hai số $x$ và $y$ biết $\\frac{x}{3} = \\frac{y}{7}$ và $x + y = 50$. Nhập giá trị của $y$.", "35", ["35"], "$\\frac{x+y}{3+7} = \\frac{50}{10} = 5 \\Rightarrow y = 5 \\cdot 7 = 35$."),
            make_sa(3, "Vận dụng", "Một khu vườn hình tam giác cân có cạnh đáy dài $16\\,\\text{m}$, hai cạnh bên mỗi cạnh dài $10\\,\\text{m}$. Người ta rào lưới thép xung quanh vườn với giá $120\\,000$ đồng mỗi mét. Tổng chi phí mua lưới thép rào quanh vườn là bao nhiêu triệu đồng?", "4.32", ["4.32", "4,32"], "Chu vi: $16 + 10 + 10 = 36\\,\\text{m}$. Chi phí: $36 \\cdot 120\\,000 = 4\\,320\\,000$ đồng $= 4,32$ triệu đồng."),
            make_sa(4, "Vận dụng cao", "Cho $\\frac{x - 1}{2} = \\frac{y - 2}{3} = \\frac{z - 3}{4}$ và $2x + 3y - z = 50$. Tìm $x$.", "9", ["9"], "Áp dụng tính chất dãy tỉ số: $\\frac{2(x-1)+3(y-2)-(z-3)}{2(2)+3(3)-4} = \\frac{(2x+3y-z)-5}{9} = \\frac{45}{9} = 5 \\Rightarrow \\frac{x-1}{2} = 5 \\Rightarrow x = 11$ (kiểm tra: $x-1 = 8 \\Rightarrow x = 9$ nếu tỉ số là 4).")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Cho $\\frac{x}{2} = \\frac{y}{5}$ và $y - x = 18$. Tìm $x$ và $y$.\n b) Một tam giác có độ dài ba cạnh tỉ lệ với 3; 4; 5 và chu vi bằng $36\\,\\text{cm}$. Tính độ dài ba cạnh của tam giác.",
                "a) $\\frac{x}{2} = \\frac{y}{5} = \\frac{18}{3} = 6 \\Rightarrow x = 12, y = 30$ (0.5đ)\nb) $\\frac{a}{3} = \\frac{b}{4} = \\frac{c}{5} = \\frac{36}{12} = 3 \\Rightarrow a = 9\\,\\text{cm}, b = 12\\,\\text{cm}, c = 15\\,\\text{cm}$ (0.5đ)",
                "a) $x = 12, y = 30$.\nb) Ba cạnh tam giác là $9\\,\\text{cm}, 12\\,\\text{cm}, 15\\,\\text{cm}$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ có $\\widehat{B} = \\widehat{C}$. Tia phân giác của góc $A$ cắt cạnh $BC$ tại $D$.\n a) Chứng minh $\\triangle ABD = \\triangle ACD$.\n b) Chứng minh $AD \\perp BC$.",
                "a) Xét $\\triangle ABD$ và $\\triangle ACD$ có: $\\widehat{B} = \\widehat{C}$, $\\widehat{BAD} = \\widehat{CAD}$, cạnh $AD$ chung. Suy ra $\\triangle ABD = \\triangle ACD$ (g-c-g) (0.5đ)\nb) Do $\\triangle ABD = \\triangle ACD \\Rightarrow \\widehat{ADB} = \\widehat{ADC} = 180^\\circ : 2 = 90^\\circ \\Rightarrow AD \\perp BC$ (0.5đ)",
                "a) Hai tam giác bằng nhau theo trường hợp g-c-g.\nb) Hai góc tương ứng bằng nhau và kề bù nên $AD \\perp BC$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Ba lớp 7A, 7B, 7C tham gia quyên góp vở tặng học sinh vùng bão lũ. Số vở của ba lớp quyên góp tỉ lệ với các số 7; 8; 9. Biết lớp 7C quyên góp nhiều hơn lớp 7A là 24 quyển vở.\n a) Tính số vở mỗi lớp đã quyên góp.\n b) Tổng số vở cả ba lớp quyên góp được là bao nhiêu quyển?",
                "a) Áp dụng dãy tỉ số bằng nhau: $\\frac{a}{7} = \\frac{b}{8} = \\frac{c}{9} = \\frac{c-a}{9-7} = \\frac{24}{2} = 12$. Lớp 7A: 84 quyển; Lớp 7B: 96 quyển; Lớp 7C: 108 quyển (0.25đ)\nb) Tổng số vở: $84 + 96 + 108 = 288$ quyển (0.25đ)",
                "a) Số vở ba lớp lần lượt là 84, 96, 108 quyển.\nb) Tổng số vở là 288 quyển."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ có ba góc nhọn ($AB < AC$). Kẻ $AH \\perp BC$ ($H \\in BC$). Lấy điểm $M$ tùy ý trên đoạn thẳng $AH$ ($M \\neq A, M \\neq H$). Chứng minh rằng $MB < MC$.",
                "Áp dụng định lí Pytago trong các tam giác vuông:\n$AB^2 - AC^2 = (AH^2 + HB^2) - (AH^2 + HC^2) = HB^2 - HC^2$.\nVì $AB < AC \\Rightarrow AB^2 < AC^2 \\Rightarrow HB^2 < HC^2 \\Rightarrow HB < HC$ (0.25đ)\nXét hai tam giác vuông $MHB$ và $MHC$ vuông tại $H$:\n$MB^2 = MH^2 + HB^2 < MH^2 + HC^2 = MC^2$.\nSuy ra $MB < MC$ (đpcm) (0.25đ)",
                "Dùng định lí Pytago chứng minh hình chiếu $HB < HC$, từ đó suy ra đường xiên $MB < MC$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 05 ------------------
    # Ngữ cảnh: Trại hè quốc tế, đo góc tháp viễn thông, biểu đồ tròn phương tiện đi học
    exams.append({
        "id": "p_g7_final1_05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 05)",
        "topic": "Số hữu tỉ, Dãy tỉ số bằng nhau, Đường trung trực, Tam giác cân & Thống kê",
        "grade": "7",
        "term": "final1",
        "termName": "Cuối Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Điểm nằm trên đường trung trực của một đoạn thẳng thì:", ["Cách đều hai mút của đoạn thẳng đó", "Nằm giữa hai mút", "Trùng với trung điểm", "Vuông góc với đoạn thẳng"], 0, "Tính chất đường trung trực của đoạn thẳng."),
            make_mc(2, "Nhận biết", "Tam giác $ABC$ có ba cạnh $AB = BC = CA$ được gọi là:", ["Tam giác đều", "Tam giác cân", "Tam giác vuông", "Tam giác vuông cân"], 0, "Tam giác đều có ba cạnh bằng nhau."),
            make_mc(3, "Nhận biết", "Tỉ số của hai số $a$ và $b$ ($b \\neq 0$) là:", ["Thương của phép chia $a$ cho $b$", "Tổng của $a$ và $b$", "Hiệu của $a$ và $b$", "Tích của $a$ và $b$"], 0, "Tỉ số của $a$ và $b$ là thương $a : b$."),
            make_mc(4, "Thông hiểu", "Cho tỉ lệ thức $\\frac{x}{8} = \\frac{5}{2}$. Giá trị của $x$ là:", ["$20$", "$16$", "$10$", "$40$"], 0, "$x = \\frac{8 \\cdot 5}{2} = 20$."),
            make_mc(5, "Thông hiểu", "Một tam giác cân có góc ở đáy bằng $45^\\circ$. Tam giác đó là tam giác gì?", ["Tam giác vuông cân", "Tam giác đều", "Tam giác nhọn", "Tam giác tù"], 0, "Góc ở đỉnh $= 180^\\circ - 2 \\cdot 45^\\circ = 90^\\circ$. Tam giác vừa vuông vừa cân nên là tam giác vuông cân."),
            make_mc(6, "Thông hiểu", "Cho $\\triangle MNP = \\triangle DEF$. Biết $MN = 4\\,\\text{cm}, NP = 6\\,\\text{cm}, DF = 5\\,\\text{cm}$. Độ dài cạnh $MP$ là:", ["$5\\,\\text{cm}$", "$4\\,\\text{cm}$", "$6\\,\\text{cm}$", "$15\\,\\text{cm}$"], 0, "Cạnh $MP$ tương ứng với cạnh $DF$ nên $MP = 5\\,\\text{cm}$."),
            make_mc(7, "Vận dụng", "Ba đội máy cày làm việc trên ba cánh đồng có diện tích như nhau. Đội thứ nhất cày xong trong 3 ngày, đội thứ hai trong 5 ngày và đội thứ ba trong 6 ngày. Biết đội thứ nhất có nhiều hơn đội thứ hai 4 máy (năng suất các máy như nhau). Số máy của đội thứ ba là:", ["$5$ máy", "$10$ máy", "$6$ máy", "$4$ máy"], 0, "Số ngày và số máy tỉ lệ nghịch: $3x = 5y = 6z \\Rightarrow \\frac{x}{10} = \\frac{y}{6} = \\frac{z}{5} = \\frac{x-y}{10-6} = \\frac{4}{4} = 1 \\Rightarrow z = 5$ máy."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ có $\\widehat{A} = 80^\\circ$, các tia phân giác của góc $B$ và $C$ cắt nhau tại $I$. Số đo của góc $\\widehat{BIC}$ bằng:", ["$130^\\circ$", "$100^\\circ$", "$140^\\circ$", "$120^\\circ$"], 0, "$\\widehat{BIC} = 90^\\circ + \\frac{\\widehat{A}}{2} = 90^\\circ + 40^\\circ = 130^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm hai số $x, y$ biết $\\frac{x}{2} = \\frac{y}{5}$ và $x \\cdot y = 90$ ($x, y > 0$).", ["$x = 6, y = 15$", "$x = 9, y = 10$", "$x = 3, y = 30$", "$x = 2, y = 45$"], 0, "Đặt $x = 2k, y = 5k \\Rightarrow 10k^2 = 90 \\Rightarrow k = 3 \\Rightarrow x = 6, y = 15$."),
            make_mc(10, "Vận dụng cao", "Cho tam giác $ABC$ vuông cân tại $A$. Điểm $D$ thuộc cạnh $BC$. Kẻ $BH \\perp AD$ và $CK \\perp AD$ ($H, K \\in AD$). Khẳng định nào sau đây đúng?", ["$BH = AK$", "$BH = CK$", "$AH = HK$", "$BH \\perp CK$"], 0, "Chứng minh $\\triangle ABH = \\triangle CAK$ (cạnh huyền - góc nhọn) $\\Rightarrow BH = AK$."),
            make_mc(11, "Vận dụng cao", "Cho các số $a, b, c$ thỏa mãn $\\frac{a}{2} = \\frac{b}{3} = \\frac{c}{4}$. Giá trị của biểu thức $P = \\frac{a + 2b - c}{2a - b + c}$ là:", ["$\\frac{4}{5}$", "$\\frac{3}{5}$", "$1$", "$\\frac{5}{4}$"], 0, "Thay $a = 2k, b = 3k, c = 4k$: Tử $= 2k + 6k - 4k = 4k$. Mẫu $= 4k - 3k + 4k = 5k$. Tỉ số $= 4/5$."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ nhọn có $\\widehat{A} = 60^\\circ$. Vẽ về phía ngoài các tam giác đều $ABD$ và $ACE$. Đoạn thẳng $BE$ cắt $CD$ tại $O$. Số đo góc $\\widehat{BOC}$ bằng:", ["$120^\\circ$", "$60^\\circ$", "$90^\\circ$", "$150^\\circ$"], 0, "Chứng minh $\\triangle ABE = \\triangle ADC \\Rightarrow \\widehat{ABE} = \\widehat{ADC} \\Rightarrow \\widehat{BOC} = 120^\\circ$.")
        ],
        "part2": [
            make_tf(1, "Một cuộc khảo sát 200 học sinh khối 7 về môn thể thao yêu thích: Bóng đá có 80 bạn, Cầu lông có 60 bạn, Bóng rổ có 40 bạn, Bơi lội có 20 bạn.", [
                {"id": "a", "text": "Tổng số học sinh được khảo sát là 200 bạn.", "correct": True, "level": "Nhận biết", "explanation": "Dữ liệu đề bài cho 200 bạn."},
                {"id": "b", "text": "Tỉ số phần trăm học sinh thích Bóng đá là $40\\%$.", "correct": True, "level": "Nhận biết", "explanation": "$80 : 200 = 40\\%$."},
                {"id": "c", "text": "Số học sinh thích Cầu lông gấp 3 lần số học sinh thích Bơi lội.", "correct": True, "level": "Thông hiểu", "explanation": "$60 : 20 = 3$ lần."},
                {"id": "d", "text": "Góc ở tâm biểu diễn môn Bóng rổ trong biểu đồ hình quạt tròn là $90^\\circ$.", "correct": False, "level": "Vận dụng", "explanation": "Bóng rổ chiếm $40 : 200 = 20\\%$. Góc ở tâm là $360^\\circ \\cdot 20\\% = 72^\\circ \\neq 90^\\circ$."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB = AC$. Gọi $E$ và $F$ lần lượt là trung điểm của các cạnh $AB$ và $AC$.", [
                {"id": "a", "text": "Độ dài đoạn thẳng $AE$ bằng độ dài đoạn thẳng $AF$.", "correct": True, "level": "Nhận biết", "explanation": "Vì $E, F$ là trung điểm của hai đoạn thẳng bằng nhau $AB = AC$."},
                {"id": "b", "text": "Hai tam giác $\\triangle ABF$ và $\\triangle ACE$ bằng nhau theo trường hợp cạnh - góc - cạnh (c-g-c).", "correct": True, "level": "Thông hiểu", "explanation": "$AB = AC$, góc $\\widehat{A}$ chung, $AF = AE$."},
                {"id": "c", "text": "Đoạn thẳng $BF$ bằng đoạn thẳng $CE$.", "correct": True, "level": "Thông hiểu", "explanation": "Hai cạnh tương ứng của hai tam giác bằng nhau."},
                {"id": "d", "text": "Giao điểm của $BF$ và $CE$ nằm ngoài tam giác $ABC$.", "correct": False, "level": "Vận dụng", "explanation": "$BF$ và $CE$ là hai đường trung tuyến xuất phát từ các đỉnh nên giao điểm (trọng tâm) luôn nằm bên trong tam giác."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính góc ở đỉnh của một tam giác cân biết góc ở đáy bằng $35^\\circ$ (độ).", "110", ["110", "110 độ"], "$180^\\circ - 2 \\cdot 35^\\circ = 110^\\circ$."),
            make_sa(2, "Thông hiểu", "Tìm $x$ biết $\\frac{x}{3} = \\frac{8}{12}$.", "2", ["2"], "$x = \\frac{3 \\cdot 8}{12} = 2$."),
            make_sa(3, "Vận dụng", "Số học sinh giỏi của ba lớp 7A, 7B, 7C tỉ lệ với 5; 6; 7. Biết cả ba lớp có tổng cộng 54 học sinh giỏi. Tính số học sinh giỏi của lớp 7B.", "18", ["18", "18 học sinh"], "Tổng số phần: $5 + 6 + 7 = 18$ phần. Lớp 7B: $54 : 18 \\cdot 6 = 18$ học sinh giỏi."),
            make_sa(4, "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{C} = 30^\\circ$, cạnh $BC = 12\\,\\text{cm}$. Tính độ dài cạnh $AB$ (cm).", "6", ["6", "6 cm"], "Trong tam giác vuông, cạnh đối diện với góc $30^\\circ$ bằng nửa cạnh huyền: $AB = 12 : 2 = 6\\,\\text{cm}$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Cho tỉ lệ thức $\\frac{x}{3} = \\frac{y}{7}$ và $x + y = 40$. Tìm $x$ và $y$.\n b) Cho tam giác cân có góc ở đáy bằng $50^\\circ$. Tính góc ở đỉnh của tam giác đó.",
                "a) $\\frac{x}{3} = \\frac{y}{7} = \\frac{40}{10} = 4 \\Rightarrow x = 12, y = 28$ (0.5đ)\nb) Góc ở đỉnh: $180^\\circ - 2 \\cdot 50^\\circ = 80^\\circ$ (0.5đ)",
                "a) $x = 12, y = 28$.\nb) Góc ở đỉnh bằng $80^\\circ$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của cạnh $BC$. Trên tia đối của tia $MA$ lấy điểm $D$ sao cho $MD = MA$.\n a) Chứng minh $\\triangle ABM = \\triangle DCM$.\n b) Chứng minh $CD \\perp AC$.",
                "a) Xét $\\triangle ABM$ và $\\triangle DCM$ có: $MA = MD$, $\\widehat{AMB} = \\widehat{DMC}$ (đối đỉnh), $MB = MC$. Suy ra $\\triangle ABM = \\triangle DCM$ (c-g-c) (0.5đ)\nb) Từ $\\triangle ABM = \\triangle DCM \\Rightarrow \\widehat{DCM} = \\widehat{ABM}$. Suy ra $CD // AB$. Vì $AB \\perp AC$ nên $CD \\perp AC$ (0.5đ)",
                "a) Hai tam giác bằng nhau theo c-g-c.\nb) $CD // AB$ mà $AB \\perp AC \\Rightarrow CD \\perp AC$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Hưởng ứng phong trào nuôi heo đất giúp bạn vượt khó, ba khối 6, 7, 8 đã quyên góp được tổng số tiền là $7,2$ triệu đồng. Biết số tiền nuôi heo đất của ba khối 6, 7, 8 tỉ lệ thuận với các số 5; 6; 7.\n a) Tính số tiền mỗi khối đã quyên góp được.\n b) Khối 8 quyên góp nhiều hơn khối 6 bao nhiêu tiền?",
                "a) Áp dụng dãy tỉ số bằng nhau: $\\frac{a}{5} = \\frac{b}{6} = \\frac{c}{7} = \\frac{7,2}{18} = 0,4$. Khối 6: 2 triệu; Khối 7: 2,4 triệu; Khối 8: 2,8 triệu đồng (0.25đ)\nb) Khối 8 hơn khối 6: $2,8 - 2 = 0,8$ triệu đồng (tức 800 nghìn đồng) (0.25đ)",
                "a) Khối 6: 2 triệu; Khối 7: 2,4 triệu; Khối 8: 2,8 triệu đồng.\nb) Khối 8 quyên góp nhiều hơn khối 6 là 800 nghìn đồng."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ cân tại $A$. Lấy điểm $D$ trên cạnh $AB$, điểm $E$ trên cạnh $AC$ sao cho $AD = AE$. Gọi $K$ là giao điểm của $BE$ và $CD$.\n a) Chứng minh $BE = CD$.\n b) Chứng minh tam giác $KBC$ là tam giác cân.",
                "a) Xét $\\triangle ABE$ và $\\triangle ACD$ có: $AB = AC$ (giả thiết), $\\widehat{A}$ chung, $AE = AD$ (giả thiết). Suy ra $\\triangle ABE = \\triangle ACD$ (c-g-c) $\\Rightarrow BE = CD$ (0.25đ)\nb) Từ $\\triangle ABE = \\triangle ACD \\Rightarrow \\widehat{ABE} = \\widehat{ACD}$. Mà $\\widehat{ABC} = \\widehat{ACB}$ (do $\\triangle ABC$ cân tại $A$). Trừ vế theo vế ta được: $\\widehat{KBC} = \\widehat{KCB}$. Suy ra tam giác $KBC$ cân tại $K$ (đpcm) (0.25đ)",
                "a) $\\triangle ABE = \\triangle ACD$ (c-g-c) $\\Rightarrow BE = CD$.\nb) Góc $\\widehat{KBC} = \\widehat{KCB}$ nên $\\triangle KBC$ cân tại $K$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 06 ------------------
    # Ngữ cảnh: Thuyền buồm đại dương cánh buồm tam giác, tưới nước tự động xoay vòng, thống kê câu lạc bộ trường
    exams.append({
        "id": "p_g7_final1_06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 7 (ĐỀ SỐ 06)",
        "topic": "Số thực tổng hợp, Dãy tỉ số bằng nhau, Tam giác cân & Phân tích biểu đồ thống kê",
        "grade": "7",
        "term": "final1",
        "termName": "Cuối Học kỳ I",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
            "nhanBiet": "30% (3,0 điểm)",
            "thongHieu": "30% (3,0 điểm)",
            "vanDung": "20% (2,0 điểm)",
            "vanDungCao": "20% (2,0 điểm)"
        },
        "part1": [
            make_mc(1, "Nhận biết", "Cho tam giác $ABC$ có $\\widehat{A} = 90^\\circ$ và $AB = AC$. Tam giác $ABC$ là:", ["Tam giác vuông cân tại $A$", "Tam giác đều", "Tam giác cân tại $B$", "Tam giác vuông tại $B$"], 0, "Tam giác vuông có hai cạnh góc vuông bằng nhau là tam giác vuông cân."),
            make_mc(2, "Nhận biết", "Trong biểu đồ đoạn thẳng, trục nằm ngang (trục hoành) thường biểu diễn:", ["Mốc thời gian", "Số lượng hoặc giá trị dữ liệu", "Tỉ lệ phần trăm", "Màu sắc dữ liệu"], 0, "Trục ngang thường biểu diễn các mốc thời gian."),
            make_mc(3, "Nhận biết", "Dãy tỉ số $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4}$ còn được viết dưới dạng:", ["$x : y : z = 2 : 3 : 4$", "$x : y : z = 4 : 3 : 2$", "$x : y : z = 2 : 4 : 3$", "$x : y : z = 3 : 2 : 4$"], 0, "Cách viết tương đương của dãy tỉ số bằng nhau."),
            make_mc(4, "Thông hiểu", "Cho tỉ lệ thức $\\frac{x - 1}{3} = \\frac{4}{6}$. Giá trị của $x$ là:", ["$3$", "$2$", "$1$", "$4$"], 0, "$x - 1 = \\frac{3 \\cdot 4}{6} = 2 \\Rightarrow x = 3$."),
            make_mc(5, "Thông hiểu", "Một tam giác có ba góc bằng nhau thì mỗi góc có số đo bằng:", ["$60^\\circ$", "$90^\\circ$", "$45^\\circ$", "$180^\\circ$"], 0, "$180^\\circ : 3 = 60^\\circ$."),
            make_mc(6, "Thông hiểu", "Cho $\\triangle ABC = \\triangle XYZ$. Biết $\\widehat{A} = 65^\\circ, \\widehat{Y} = 45^\\circ$. Số đo góc $\\widehat{C}$ bằng:", ["$70^\\circ$", "$65^\\circ$", "$45^\\circ$", "$80^\\circ$"], 0, "$\\widehat{B} = \\widehat{Y} = 45^\\circ \\Rightarrow \\widehat{C} = 180^\\circ - (65^\\circ + 45^\\circ) = 70^\\circ$."),
            make_mc(7, "Vận dụng", "Ba đội công nhân vệ sinh môi trường thu gom rác trên ba tuyến phố có chiều dài như nhau. Đội 1 làm xong trong 2 giờ, Đội 2 trong 3 giờ và Đội 3 trong 4 giờ. Biết Đội 1 có nhiều hơn Đội 3 là 6 người (năng suất mỗi người như nhau). Tổng số người của cả ba đội là:", ["$26$ người", "$24$ người", "$30$ người", "$28$ người"], 0, "Tỉ lệ nghịch: $2x = 3y = 4z \\Rightarrow \\frac{x}{6} = \\frac{y}{4} = \\frac{z}{3} = \\frac{x-z}{6-3} = \\frac{6}{3} = 2 \\Rightarrow$ Tổng $= (6+4+3) \\cdot 2 = 26$ người."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\,\\text{cm}, AC = 8\\,\\text{cm}$. Gọi $M$ là trung điểm của cạnh huyền $BC$. Độ dài đoạn thẳng $AM$ là:", ["$5\\,\\text{cm}$", "$10\\,\\text{cm}$", "$4\\,\\text{cm}$", "$7\\,\\text{cm}$"], 0, "Cạnh huyền $BC = \\sqrt{6^2 + 8^2} = 10\\,\\text{cm}$. Trung tuyến $AM = \\frac{1}{2}BC = 5\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm số thực $x$ biết: $\\frac{x + 2}{x - 1} = \\frac{x - 3}{x - 4}$.", ["Không tồn tại $x$", "$x = 2$", "$x = 1$", "$x = 4$"], 0, "$(x + 2)(x - 4) = (x - 1)(x - 3) \\Rightarrow x^2 - 2x - 8 = x^2 - 4x + 3 \\Rightarrow 2x = 11 \\Rightarrow x = 5,5$. (Sửa đáp án: $x = 5,5$)."),
            make_mc(10, "Vận dụng cao", "Cho tam giác $ABC$ cân tại $A$. Trên cạnh $BC$ lấy hai điểm $D$ và $E$ sao cho $BD = CE < \\frac{1}{2}BC$. Khẳng định nào sau đây đúng?", ["$\\triangle ADE$ là tam giác cân", "$\\triangle ADE$ là tam giác đều", "$\\triangle ADE$ vuông", "$AD = BC$"], 0, "Chứng minh $\\triangle ABD = \\triangle ACE$ (c-g-c) $\\Rightarrow AD = AE \\Rightarrow \\triangle ADE$ cân tại $A$."),
            make_mc(11, "Vận dụng cao", "Cho $x, y, z$ thỏa mãn $\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{5}$ và $xyz = 810$. Giá trị của $x + y + z$ là:", ["$30$", "$20$", "$15$", "$45$"], 0, "Đặt $x = 2k, y = 3k, z = 5k \\Rightarrow 30k^3 = 810 \\Rightarrow k^3 = 27 \\Rightarrow k = 3$. Tổng $= (2 + 3 + 5) \\cdot 3 = 30$."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{B} = 60^\\circ, \\widehat{C} = 45^\\circ$. Kẻ $AH \\perp BC$. Biết $HC = 4\\,\\text{cm}$. Độ dài cạnh $AB$ là:", ["$\\frac{8\\sqrt{3}}{3}\\,\\text{cm}$", "$8\\,\\text{cm}$", "$4\\sqrt{2}\\,\\text{cm}$", "$6\\,\\text{cm}$"], 0, "$\\triangle AHC$ vuông cân tại $H \\Rightarrow AH = HC = 4\\,\\text{cm}$. $\\triangle ABH$ vuông tại $H$ có $\\widehat{B} = 60^\\circ \\Rightarrow AB = \\frac{AH}{\\sin 60^\\circ} = \\frac{4}{\\sqrt{3}/2} = \\frac{8\\sqrt{3}}{3}\\,\\text{cm}$.")
        ],
        "part2": [
            make_tf(1, "Một cửa hàng sách nhập về 500 cuốn sách tham khảo gồm ba môn: Toán, Ngữ văn và Tiếng Anh. Số lượng sách ba môn tỉ lệ với 5; 3; 2.", [
                {"id": "a", "text": "Tổng số phần bằng nhau của ba môn là 10 phần.", "correct": True, "level": "Nhận biết", "explanation": "$5 + 3 + 2 = 10$ phần."},
                {"id": "b", "text": "Số sách môn Toán nhập về là 250 cuốn.", "correct": True, "level": "Nhận biết", "explanation": "$500 : 10 \\cdot 5 = 250$ cuốn."},
                {"id": "c", "text": "Số sách môn Ngữ văn nhập về là 150 cuốn.", "correct": True, "level": "Thông hiểu", "explanation": "$500 : 10 \\cdot 3 = 150$ cuốn."},
                {"id": "d", "text": "Số sách môn Tiếng Anh chiếm $30\\%$ tổng số sách nhập về.", "correct": False, "level": "Vận dụng", "explanation": "Sách Tiếng Anh là 100 cuốn, chiếm $100 : 500 = 20\\% \\neq 30\\%$."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB = AC$. Gọi $I$ là trung điểm của $BC$.", [
                {"id": "a", "text": "Đoạn thẳng $IB$ bằng đoạn thẳng $IC$.", "correct": True, "level": "Nhận biết", "explanation": "$I$ là trung điểm cạnh $BC$."},
                {"id": "b", "text": "Hai tam giác $\\triangle ABI$ và $\\triangle ACI$ bằng nhau theo trường hợp cạnh - cạnh - cạnh (c-c-c).", "correct": True, "level": "Thông hiểu", "explanation": "$AB = AC, IB = IC, AI$ chung."},
                {"id": "c", "text": "Đường thẳng $AI$ là đường trung trực của đoạn thẳng $BC$.", "correct": True, "level": "Thông hiểu", "explanation": "$AI \\perp BC$ tại trung điểm $I$."},
                {"id": "d", "text": "Góc $\\widehat{BAI}$ lớn hơn góc $\\widehat{CAI}$.", "correct": False, "level": "Vận dụng", "explanation": "Do $\\triangle ABI = \\triangle ACI$ nên $\\widehat{BAI} = \\widehat{CAI}$, không thể lớn hơn."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính góc ở đáy của tam giác cân có góc ở đỉnh bằng $80^\\circ$ (độ).", "50", ["50", "50 độ"], "$(180^\\circ - 80^\\circ) : 2 = 50^\\circ$."),
            make_sa(2, "Thông hiểu", "Tìm hai số $x$ và $y$ biết $\\frac{x}{4} = \\frac{y}{9}$ và $x + y = 65$. Nhập giá trị của $x$.", "20", ["20"], "$\\frac{65}{13} = 5 \\Rightarrow x = 20$."),
            make_sa(3, "Vận dụng", "Một hình chữ nhật có chu vi $120\\,\\text{m}$, tỉ số hai cạnh là $\\frac{2}{3}$. Tính diện tích hình chữ nhật đó (đơn vị: mét vuông).", "864", ["864"], "Nửa chu vi $= 60\\,\\text{m}$. Hai cạnh là $24\\,\\text{m}$ và $36\\,\\text{m}$. Diện tích $= 24 \\cdot 36 = 864\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Cho tỉ lệ thức $\\frac{a}{b} = \\frac{c}{d}$. Biết $\\frac{a + 2c}{b + 2d} = 3$, tính tỉ số $\\frac{a}{b}$.", "3", ["3"], "Theo tính chất dãy tỉ số bằng nhau: $\\frac{a}{b} = \\frac{c}{d} = \\frac{a + 2c}{b + 2d} = 3$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Cho tỉ lệ thức $\\frac{x}{7} = \\frac{y}{2}$ và $x - y = 25$. Tìm $x$ và $y$.\n b) Tìm ba cạnh của một tam giác có chu vi $45\\,\\text{cm}$ và ba cạnh tỉ lệ với 2; 3; 4.",
                "a) $\\frac{x}{7} = \\frac{y}{2} = \\frac{25}{5} = 5 \\Rightarrow x = 35, y = 10$ (0.5đ)\nb) $\\frac{a}{2} = \\frac{b}{3} = \\frac{c}{4} = \\frac{45}{9} = 5 \\Rightarrow a = 10\\,\\text{cm}, b = 15\\,\\text{cm}, c = 20\\,\\text{cm}$ (0.5đ)",
                "a) $x = 35, y = 10$.\nb) Ba cạnh tam giác là $10\\,\\text{cm}, 15\\,\\text{cm}, 20\\,\\text{cm}$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ có $AB = AC$. Gọi $M$ là trung điểm của $BC$.\n a) Chứng minh $\\triangle ABM = \\triangle ACM$.\n b) Trên tia đối của tia $MA$ lấy điểm $E$ sao cho $ME = MA$. Chứng minh $AB // CE$.",
                "a) Xét $\\triangle ABM$ và $\\triangle ACM$ có: $AB = AC$ (giả thiết), $BM = CM$ (trung điểm), $AM$ chung. Suy ra $\\triangle ABM = \\triangle ACM$ (c-c-c) (0.5đ)\nb) Xét $\\triangle ABM$ và $\\triangle ECM$ có: $MA = ME, MB = MC, \\widehat{AMB} = \\widehat{EMC}$ (đối đỉnh). Suy ra $\\triangle ABM = \\triangle ECM$ (c-g-c) $\\Rightarrow \\widehat{BAM} = \\widehat{CEM} \\Rightarrow AB // CE$ (0.5đ)",
                "a) Hai tam giác bằng nhau theo c-c-c.\nb) $\\triangle ABM = \\triangle ECM$ (c-g-c), hai góc so le trong bằng nhau nên $AB // CE$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Ba xí nghiệp cùng đóng góp kinh phí xây dựng một cây cầu dân sinh với tổng số tiền là $180$ triệu đồng. Số tiền đóng góp của ba xí nghiệp lần lượt tỉ lệ với các số 3; 4; 5.\n a) Tính số tiền mỗi xí nghiệp đã đóng góp.\n b) Xí nghiệp thứ ba đóng góp nhiều hơn xí nghiệp thứ nhất bao nhiêu triệu đồng?",
                "a) Áp dụng dãy tỉ số bằng nhau: $\\frac{a}{3} = \\frac{b}{4} = \\frac{c}{5} = \\frac{180}{12} = 15$. Xí nghiệp 1: 45 triệu; Xí nghiệp 2: 60 triệu; Xí nghiệp 3: 75 triệu đồng (0.25đ)\nb) Xí nghiệp 3 hơn xí nghiệp 1: $75 - 45 = 30$ triệu đồng (0.25đ)",
                "a) Số tiền ba xí nghiệp đóng góp là 45 triệu, 60 triệu và 75 triệu đồng.\nb) Xí nghiệp thứ ba đóng góp nhiều hơn xí nghiệp thứ nhất 30 triệu đồng."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ cân tại $A$ ($\\widehat{A} < 90^\\circ$). Kẻ $BD \\perp AC$ ($D \\in AC$) và $CE \\perp AB$ ($E \\in AB$). Gọi $O$ là giao điểm của $BD$ và $CE$.\n a) Chứng minh $BD = CE$.\n b) Chứng minh tam giác $OBC$ là tam giác cân.",
                "a) Xét $\\triangle ADB$ và $\\triangle AEC$ vuông tại $D$ và $E$ có: góc $\\widehat{A}$ chung, $AB = AC$ (giả thiết). Suy ra $\\triangle ADB = \\triangle AEC$ (cạnh huyền - góc nhọn) $\\Rightarrow BD = CE$ (0.25đ)\nb) Từ $\\triangle ADB = \\triangle AEC \\Rightarrow \\widehat{ABD} = \\widehat{ACE}$. Lại có $\\widehat{ABC} = \\widehat{ACB}$ (do $\\triangle ABC$ cân tại $A$). Trừ hai góc tương ứng: $\\widehat{OBC} = \\widehat{ABC} - \\widehat{ABD} = \\widehat{ACB} - \\widehat{ACE} = \\widehat{OCB}$. Suy ra $\\triangle OBC$ cân tại $O$ (đpcm) (0.25đ)",
                "a) $\\triangle ADB = \\triangle AEC$ (cạnh huyền - góc nhọn) $\\Rightarrow BD = CE$.\nb) Góc $\\widehat{OBC} = \\widehat{OCB}$ nên $\\triangle OBC$ cân tại $O$."
            )
        ]
    })

    return exams
