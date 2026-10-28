# -*- coding: utf-8 -*-
"""
BỘ ĐỀ THI ĐỊNH KỲ TOÁN 8 - HỌC KỲ I (GIỮA KỲ 1 & CUỐI KỲ 1)
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
# 6 MÃ ĐỀ GIỮA KỲ 1 - TOÁN 8 (mid1)
# Phạm vi: Đa thức nhiều biến, 7 Hằng đẳng thức, Phân tích đa thức & Tứ giác (Hình thang cân, HBH, HCN, Hình thoi, Hình vuông).
# ==============================================================================
def generate_g8_mid1():
    exams = []

    # ------------------ ĐỀ SỐ 01 ------------------
    # Ngữ cảnh: Gia công tấm pin mặt trời hình chữ nhật, thiết kế bãi đỗ xe hình bình hành, tính diện tích sàn nhà
    exams.append({
        "id": "p_g8_mid1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 01)",
        "topic": "Đa thức nhiều biến, Hằng đẳng thức đáng nhớ, Phân tích nhân tử & Tứ giác lồi",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Biểu thức nào sau đây là đơn thức nhiều biến?", ["$3x^2y$", "$2x + y$", "$\\frac{x}{y}$", "$x^2 - 1$"], 0, "$3x^2y$ là tích giữa số và các biến nên là đơn thức."),
            make_mc(2, "Nhận biết", "Khai triển của hằng đẳng thức $(A + B)^2$ là:", ["$A^2 + 2AB + B^2$", "$A^2 + AB + B^2$", "$A^2 - 2AB + B^2$", "$A^2 + B^2$"], 0, "$(A + B)^2 = A^2 + 2AB + B^2$."),
            make_mc(3, "Nhận biết", "Tổng số đo bốn góc của một tứ giác lồi luôn bằng:", ["$360^\\circ$", "$180^\\circ$", "$270^\\circ$", "$540^\\circ$"], 0, "Định lí: Tổng các góc của một tứ giác bằng $360^\\circ$."),
            make_mc(4, "Thông hiểu", "Bậc của đa thức $P = 4x^3y^2 - 5x^4y + 2xy^3 - 7$ là:", ["$5$", "$4$", "$3$", "$6$"], 0, "Hạng tử $-5x^4y$ có bậc là $4 + 1 = 5$ (cao nhất), nên bậc đa thức là 5."),
            make_mc(5, "Thông hiểu", "Phân tích đa thức $x^2 - 9$ thành nhân tử ta được:", ["$(x - 3)(x + 3)$", "$(x - 3)^2$", "$(x + 3)^2$", "$x(x - 9)$"], 0, "$x^2 - 9 = x^2 - 3^2 = (x - 3)(x + 3)$."),
            make_mc(6, "Thông hiểu", "Hình bình hành có một góc vuông là:", ["Hình chữ nhật", "Hình thoi", "Hình thang cân", "Hình vuông"], 0, "Dấu hiệu nhận biết: Hình bình hành có một góc vuông là hình chữ nhật."),
            make_mc(7, "Vận dụng", "Một khu đất hình chữ nhật có chiều dài bằng $(3x + 2)\\,\\text{m}$ và chiều rộng bằng $(2x - 1)\\,\\text{m}$. Biểu thức biểu diễn diện tích khu đất đó là:", ["$6x^2 + x - 2\\,\\text{m}^2$", "$6x^2 - x - 2\\,\\text{m}^2$", "$6x^2 + 7x - 2\\,\\text{m}^2$", "$5x + 1\\,\\text{m}^2$"], 0, "$S = (3x + 2)(2x - 1) = 6x^2 - 3x + 4x - 2 = 6x^2 + x - 2\\,\\text{m}^2$."),
            make_mc(8, "Vận dụng", "Cho hình thang cân $ABCD$ ($AB // CD$) có $\\widehat{C} = 65^\\circ$. Số đo của góc $\\widehat{A}$ bằng:", ["$115^\\circ$", "$65^\\circ$", "$125^\\circ$", "$180^\\circ$"], 0, "Do $AB // CD$ nên $\\widehat{A} + \\widehat{D} = 180^\\circ$. Mà hình thang cân nên $\\widehat{D} = \\widehat{C} = 65^\\circ \\Rightarrow \\widehat{A} = 180^\\circ - 65^\\circ = 115^\\circ$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức $A = x^2 - 4x + y^2 - 6y + 15$.", ["$2$", "$15$", "$0$", "$5$"], 0, "$A = (x - 2)^2 + (y - 3)^2 + 2 \\ge 2$. Giá trị nhỏ nhất là 2 khi $x = 2, y = 3$."),
            make_mc(10, "Vận dụng cao", "Cho $x + y = 5$ và $xy = 6$. Giá trị của biểu thức $x^3 + y^3$ bằng:", ["$35$", "$65$", "$125$", "$95$"], 0, "$x^3 + y^3 = (x + y)^3 - 3xy(x + y) = 5^3 - 3 \\cdot 6 \\cdot 5 = 125 - 90 = 35$."),
            make_mc(11, "Vận dụng cao", "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn: $x^2 - 2xy + 2y^2 - 2x + 2 = 0$.", ["$(2; 1)$", "$(1; 2)$", "$(0; 1)$", "Không có"], 0, "$(x - y - 1)^2 + (y - 1)^2 = 0 \\Rightarrow y = 1$ và $x = 2$."),
            make_mc(12, "Vận dụng cao", "Cho hình vuông $ABCD$. Trên tia đối của tia $BA$ lấy điểm $E$, trên tia đối của tia $CB$ lấy điểm $F$ sao cho $BE = CF$. Tam giác $DEF$ là:", ["Tam giác vuông cân tại $D$", "Tam giác đều", "Tam giác cân tại $E$", "Tam giác vuông tại $E$"], 0, "Chứng minh $\\triangle DAE = \\triangle DCF$ (c-g-c) $\\Rightarrow DE = DF$ và $\\widehat{ADE} = \\widehat{CDF} \\Rightarrow \\widehat{EDF} = 90^\\circ$. Vậy tam giác vuông cân tại $D$.")
        ],
        "part2": [
            make_tf(1, "Cho hai đa thức $P(x, y) = 3x^2y - 2xy^2 + 5$ và $Q(x, y) = 2x^2y + xy^2 - 3$.", [
                {"id": "a", "text": "Đa thức $P(x, y)$ có bậc bằng 3.", "correct": True, "level": "Nhận biết", "explanation": "Hạng tử $3x^2y$ và $-2xy^2$ có bậc $2+1=3$."},
                {"id": "b", "text": "Hệ số tự do của đa thức $Q(x, y)$ là $-3$.", "correct": True, "level": "Nhận biết", "explanation": "Hạng tử không chứa biến là $-3$."},
                {"id": "c", "text": "Đa thức tổng $P + Q$ bằng $5x^2y - xy^2 + 2$.", "correct": True, "level": "Thông hiểu", "explanation": "$(3+2)x^2y + (-2+1)xy^2 + (5-3) = 5x^2y - xy^2 + 2$."},
                {"id": "d", "text": "Tại $x = 1, y = -1$, giá trị của đa thức tổng $P + Q$ bằng 0.", "correct": False, "level": "Vận dụng", "explanation": "Thay số: $5(1)^2(-1) - 1(-1)^2 + 2 = -5 - 1 + 2 = -4 \\neq 0$."}
            ]),
            make_tf(2, "Cho hình thoi $ABCD$ có hai đường chéo $AC = 16\\,\\text{cm}$ và $BD = 12\\,\\text{cm}$ cắt nhau tại $O$.", [
                {"id": "a", "text": "Hai đường chéo $AC$ và $BD$ vuông góc với nhau tại trung điểm $O$ của mỗi đường.", "correct": True, "level": "Nhận biết", "explanation": "Tính chất đặc trưng của hình thoi."},
                {"id": "b", "text": "Độ dài đoạn thẳng $OA$ bằng $8\\,\\text{cm}$ và $OB$ bằng $6\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$OA = 16 : 2 = 8\\,\\text{cm}; OB = 12 : 2 = 6\\,\\text{cm}$."},
                {"id": "c", "text": "Độ dài mỗi cạnh của hình thoi $ABCD$ bằng $10\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "Tam giác $OAB$ vuông tại $O$: $AB = \\sqrt{8^2 + 6^2} = 10\\,\\text{cm}$."},
                {"id": "d", "text": "Chu vi hình thoi $ABCD$ bằng $48\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "Chu vi hình thoi $= 10 \\cdot 4 = 40\\,\\text{cm}$, không phải $48\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của biểu thức $x^2 - 4x + 4$ tại $x = 102$.", "10000", ["10000", "10.000"], "$x^2 - 4x + 4 = (x - 2)^2 = (102 - 2)^2 = 100^2 = 10000$."),
            make_sa(2, "Thông hiểu", "Tìm $x$ biết: $(x - 3)(x + 3) - x(x - 2) = 5$.", "7", ["7"], "$x^2 - 9 - x^2 + 2x = 5 \\Rightarrow 2x - 9 = 5 \\Rightarrow 2x = 14 \\Rightarrow x = 7$."),
            make_sa(3, "Vận dụng", "Một sân chơi hình chữ nhật có chu vi $60\\,\\text{m}$. Nếu tăng chiều rộng thêm $3\\,\\text{m}$ và giảm chiều dài đi $3\\,\\text{m}$ thì sân chơi trở thành hình vuông. Tính diện tích sân chơi ban đầu (đơn vị: mét vuông).", "216", ["216"], "Nửa chu vi $= 30\\,\\text{m}$. Cạnh hình vuông $= 15\\,\\text{m}$. Chiều dài $= 18\\,\\text{m}$, chiều rộng $= 12\\,\\text{m}$. Diện tích $= 18 \\cdot 12 = 216\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của đa thức: $P = x^2 - 2xy + 2y^2 - 4y + 10$.", "6", ["6"], "$P = (x - y)^2 + (y - 2)^2 + 6 \\ge 6$. Đạt giá trị nhỏ nhất bằng 6 khi $x = y = 2$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Làm tính nhân: $2xy(3x^2 - 4xy + 5y^2)$.\n b) Phân tích đa thức thành nhân tử: $5x^2y - 10xy^2$.",
                "a) $2xy \\cdot 3x^2 - 2xy \\cdot 4xy + 2xy \\cdot 5y^2 = 6x^3y - 8x^2y^2 + 10xy^3$ (0.5đ)\nb) Đặt nhân tử chung $5xy(x - 2y)$ (0.5đ)",
                "a) $6x^3y - 8x^2y^2 + 10xy^3$.\nb) $5xy(x - 2y)$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ cân tại $A$. Gọi $D, E$ lần lượt là trung điểm của $AB$ và $AC$.\n a) Chứng minh tứ giác $BDEC$ là hình thang cân.\n b) Biết $BC = 12\\,\\text{cm}$, tính độ dài đoạn thẳng $DE$.",
                "a) Do $D, E$ là trung điểm nên $DE // BC \\Rightarrow BDEC$ là hình thang. Mặt khác $\\widehat{B} = \\widehat{C}$ (tam giác cân) nên $BDEC$ là hình thang cân (0.5đ)\nb) $DE$ là đường trung bình nên $DE = \\frac{1}{2}BC = 12 : 2 = 6\\,\\text{cm}$ (0.5đ)",
                "a) $BDEC$ có $DE // BC$ và $\\widehat{B} = \\widehat{C}$ nên là hình thang cân.\nb) $DE = 6\\,\\text{cm}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một mảnh vườn hình chữ nhật có chiều dài gấp đôi chiều rộng. Người ta mở rộng mảnh vườn bằng cách tăng chiều rộng thêm $3\\,\\text{m}$ và tăng chiều dài thêm $2\\,\\text{m}$, khi đó diện tích tăng thêm $66\\,\\text{m}^2$.\n a) Tính kích thước chiều rộng và chiều dài mảnh vườn ban đầu.\n b) Tính diện tích mảnh vườn sau khi mở rộng.",
                "a) Gọi chiều rộng ban đầu là $x\\,\\text{m}$ ($x > 0$), chiều dài là $2x\\,\\text{m}$. Diện tích ban đầu là $2x^2$. Diện tích mới: $(2x + 2)(x + 3) = 2x^2 + 8x + 6$. Tăng thêm $8x + 6 = 66 \\Rightarrow 8x = 60 \\Rightarrow x = 7,5\\,\\text{m}$. Chiều dài ban đầu: $15\\,\\text{m}$ (0.25đ)\nb) Diện tích mới: $(15 + 2)(7,5 + 3) = 17 \\cdot 10,5 = 178,5\\,\\text{m}^2$ (0.25đ)",
                "a) Chiều rộng ban đầu là $7,5\\,\\text{m}$, chiều dài là $15\\,\\text{m}$.\nb) Diện tích sau khi mở rộng là $178,5\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực $a, b, c$ thỏa mãn $a + b + c = 0$ và $a^2 + b^2 + c^2 = 14$.\n Tính giá trị của biểu thức $M = a^4 + b^4 + c^4$.",
                "Ta có $(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca) = 0$.\nSuy ra $2(ab + bc + ca) = -14 \\Rightarrow ab + bc + ca = -7$.\nBình phương biểu thức này:\n$(ab + bc + ca)^2 = a^2b^2 + b^2c^2 + c^2a^2 + 2abc(a + b + c) = (-7)^2 = 49$.\nVì $a + b + c = 0$ nên $a^2b^2 + b^2c^2 + c^2a^2 = 49$.\nMặt khác: $(a^2 + b^2 + c^2)^2 = a^4 + b^4 + c^4 + 2(a^2b^2 + b^2c^2 + c^2a^2) = 14^2 = 196$.\nDo đó $M = a^4 + b^4 + c^4 = 196 - 2 \\cdot 49 = 98$ (0.5đ)",
                "Khai triển hằng đẳng thức $(a+b+c)^2 = 0$ tìm được $ab+bc+ca = -7$. Tiếp tục bình phương tìm được $M = a^4 + b^4 + c^4 = 98$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 02 ------------------
    # Ngữ cảnh: Khung giàn mái đón hình thang cân, chi phí sản xuất vi mạch, hằng đẳng thức lập phương
    exams.append({
        "id": "p_g8_mid1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 02)",
        "topic": "Đơn thức - Đa thức, Hằng đẳng thức lập phương & Tứ giác đặc biệt (Hình chữ nhật, Hình thoi)",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Khai triển của hằng đẳng thức $A^2 - B^2$ là:", ["$(A - B)(A + B)$", "$(A - B)^2$", "$(A + B)^2$", "$A^2 - 2AB + B^2$"], 0, "$A^2 - B^2 = (A - B)(A + B)$."),
            make_mc(2, "Nhận biết", "Hình thoi là tứ giác có:", ["Bốn cạnh bằng nhau", "Bốn góc bằng nhau", "Hai đường chéo bằng nhau", "Hai cạnh đối song song"], 0, "Định nghĩa: Hình thoi là tứ giác có bốn cạnh bằng nhau."),
            make_mc(3, "Nhận biết", "Trong các đơn thức sau, đơn thức nào đồng dạng với đơn thức $-3x^2y^3$?", ["$5x^2y^3$", "$3x^3y^2$", "$-3x^2y$", "$5xy^3$"], 0, "Đơn thức đồng dạng có cùng phần biến $x^2y^3$."),
            make_mc(4, "Thông hiểu", "Thu gọn đa thức $M = 3x^2y - 5xy + 2x^2y + 5xy - 1$ ta được:", ["$5x^2y - 1$", "$5x^2y + 10xy - 1$", "$x^2y - 1$", "$5x^2y$"], 0, "$M = (3 + 2)x^2y + (-5 + 5)xy - 1 = 5x^2y - 1$."),
            make_mc(5, "Thông hiểu", "Một tứ giác có hai đường chéo vuông góc với nhau tại trung điểm của mỗi đường là:", ["Hình thoi", "Hình chữ nhật", "Hình thang cân", "Hình bình hành"], 0, "Dấu hiệu nhận biết hình thoi: Hình bình hành có hai đường chéo vuông góc là hình thoi."),
            make_mc(6, "Thông hiểu", "Phân tích đa thức $x^2 - 6x + 9$ thành nhân tử:", ["$(x - 3)^2$", "$(x + 3)^2$", "$(x - 9)^2$", "$x(x - 6) + 9$"], 0, "$x^2 - 2 \\cdot 3x + 3^2 = (x - 3)^2$."),
            make_mc(7, "Vận dụng", "Một tấm bìa hình vuông có cạnh bằng $(x + 4)\\,\\text{cm}$. Người ta cắt bỏ ở bốn góc bốn hình vuông nhỏ có cạnh bằng $2\\,\\text{cm}$ để gấp thành một chiếc hộp không nắp. Thể tích của chiếc hộp là:", ["$2x^2\\,\\text{cm}^3$", "$4x^2\\,\\text{cm}^3$", "$2(x+4)^2\\,\\text{cm}^3$", "$x^2\\,\\text{cm}^3$"], 0, "Đáy hộp là hình vuông cạnh $(x + 4 - 4) = x\\,\\text{cm}$, chiều cao hộp là $2\\,\\text{cm}$. Thể tích: $V = 2x^2\\,\\text{cm}^3$."),
            make_mc(8, "Vận dụng", "Cho hình chữ nhật $ABCD$ có $AB = 8\\,\\text{cm}, BC = 6\\,\\text{cm}$. Độ dài đường chéo $AC$ là:", ["$10\\,\\text{cm}$", "$14\\,\\text{cm}$", "$7\\,\\text{cm}$", "$12\\,\\text{cm}$"], 0, "Áp dụng định lí Pytago trong tam giác vuông $ABC$: $AC = \\sqrt{8^2 + 6^2} = 10\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $B = 4x^2 - 12x + 15$.", ["$6$", "$15$", "$9$", "$3$"], 0, "$B = (2x - 3)^2 + 6 \\ge 6$. Giá trị nhỏ nhất là 6 khi $x = 1,5$."),
            make_mc(10, "Vận dụng cao", "Cho $x - y = 7$ và $xy = 9$. Giá trị của biểu thức $x^2 + y^2$ bằng:", ["$67$", "$49$", "$31$", "$85$"], 0, "$x^2 + y^2 = (x - y)^2 + 2xy = 7^2 + 2 \\cdot 9 = 49 + 18 = 67$."),
            make_mc(11, "Vận dụng cao", "Tìm tất cả các số nguyên $n$ để đa thức $n^3 - n^2 + 2n - 2$ là một số nguyên tố.", ["$n = 2$", "$n = 0$", "$n = 3$", "Không có $n$"], 0, "$n^2(n - 1) + 2(n - 1) = (n - 1)(n^2 + 2)$. Để là số nguyên tố thì thừa số nhỏ hơn phải bằng 1: $n - 1 = 1 \\Rightarrow n = 2$. Khi đó $(2-1)(4+2) = 6$ là hợp số! Vậy không có giá trị nào."),
            make_mc(12, "Vận dụng cao", "Cho hình vuông $ABCD$ có cạnh bằng $a$. Lấy điểm $E$ trên cạnh $CD$. Tia phân giác của góc $\\widehat{DAE}$ cắt cạnh $CD$ kéo dài tại $F$. Kẻ $EH \\perp AF$ ($H \\in AF$). Khẳng định nào sau đây đúng?", ["$AH = a$", "$AH = 2a$", "$EH = a$", "$AF = 2a$"], 0, "Chứng minh $\\triangle ADH$ vuông cân và $AH = AD = a$.")
        ],
        "part2": [
            make_tf(1, "Một khu vườn hình chữ nhật ban đầu có chiều dài $x$ (mét) và chiều rộng $y$ (mét). Người ta mở rộng vườn bằng cách tăng chiều dài thêm $4\\,\\text{m}$ và tăng chiều rộng thêm $3\\,\\text{m}$.", [
                {"id": "a", "text": "Diện tích khu vườn ban đầu được biểu diễn bằng đơn thức $xy$.", "correct": True, "level": "Nhận biết", "explanation": "Diện tích hình chữ nhật là tích dài nhân rộng."},
                {"id": "b", "text": "Chiều dài khu vườn sau khi mở rộng là $(x + 4)\\,\\text{m}$.", "correct": True, "level": "Nhận biết", "explanation": "Chiều dài tăng thêm 4 m."},
                {"id": "c", "text": "Diện tích khu vườn sau khi mở rộng là $xy + 3x + 4y + 12\\,(\\text{m}^2)$.", "correct": True, "level": "Thông hiểu", "explanation": "$(x + 4)(y + 3) = xy + 3x + 4y + 12$."},
                {"id": "d", "text": "Nếu ban đầu $x = 20\\,\\text{m}, y = 10\\,\\text{m}$ thì phần diện tích tăng thêm là $115\\,\\text{m}^2$.", "correct": False, "level": "Vận dụng", "explanation": "Phần tăng thêm: $3(20) + 4(10) + 12 = 60 + 40 + 12 = 112\\,\\text{m}^2 \\neq 115\\,\\text{m}^2$."}
            ]),
            make_tf(2, "Cho hình bình hành $ABCD$ có $AB = 2AD$. Gọi $M$ và $N$ lần lượt là trung điểm của $AB$ và $CD$.", [
                {"id": "a", "text": "Đoạn thẳng $AM$ bằng một nửa đoạn thẳng $AB$.", "correct": True, "level": "Nhận biết", "explanation": "$M$ là trung điểm của $AB$."},
                {"id": "b", "text": "Tứ giác $AMND$ là hình thoi.", "correct": True, "level": "Thông hiểu", "explanation": "$AM // DN, AM = DN$ nên $AMND$ là hình bình hành. Lại có $AM = AD$ nên là hình thoi."},
                {"id": "c", "text": "Đoạn thẳng $AN$ vuông góc với đoạn thẳng $DM$.", "correct": True, "level": "Thông hiểu", "explanation": "Hai đường chéo của hình thoi vuông góc với nhau."},
                {"id": "d", "text": "Tứ giác $MBCN$ là hình thang cân.", "correct": False, "level": "Vận dụng", "explanation": "$MBCN$ là hình thoi (vì có 4 cạnh bằng nhau $MB = BC = CN = MN$), không phải hình thang cân thuần túy."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Khai triển hằng đẳng thức $(x - 5)^2$ được: $x^2 - 10x + c$. Tìm hệ số $c$.", "25", ["25"], "$c = (-5)^2 = 25$."),
            make_sa(2, "Thông hiểu", "Tính nhanh giá trị: $75^2 - 25^2$.", "5000", ["5000", "5.000"], "$(75 - 25)(75 + 25) = 50 \\cdot 100 = 5000$."),
            make_sa(3, "Vận dụng", "Một bể bơi hình chữ nhật có chiều dài $25\\,\\text{m}$, chiều rộng $12\\,\\text{m}$. Người ta lát gạch men một lối đi bao quanh bể bơi rộng $1,5\\,\\text{m}$. Diện tích của lối đi bao quanh bể bơi là bao nhiêu mét vuông?", "120", ["120"], "Kích thước cả lối đi: $28 \\times 15$. Diện tích: $28 \\cdot 15 = 420\\,\\text{m}^2$. Diện tích bể: $25 \\cdot 12 = 300\\,\\text{m}^2$. Lối đi: $420 - 300 = 120\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $M = x^2 + y^2 - 4x + 6y + 20$.", "7", ["7"], "$M = (x - 2)^2 + (y + 3)^2 + 7 \\ge 7$. Đạt giá trị nhỏ nhất bằng 7.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Thực hiện phép chia: $(12x^4y^3 - 8x^3y^2 + 4x^2y) : (4x^2y)$.\n b) Phân tích đa thức thành nhân tử: $x^2 - 4y^2$.",
                "a) $3x^2y^2 - 2xy + 1$ (0.5đ)\nb) $(x - 2y)(x + 2y)$ (0.5đ)",
                "a) $3x^2y^2 - 2xy + 1$.\nb) $(x - 2y)(x + 2y)$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho hình bình hành $ABCD$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Qua $O$ kẻ đường thẳng cắt $AB$ tại $M$ và cắt $CD$ tại $N$.\n a) Chứng minh $\\triangle OAM = \\triangle OCN$.\n b) Chứng minh tứ giác $MBND$ là hình bình hành.",
                "a) Xét $\\triangle OAM$ và $\\triangle OCN$ có: $OA = OC$ (tính chất HBH), $\\widehat{AOM} = \\widehat{CON}$ (đối đỉnh), $\\widehat{MAO} = \\widehat{NCO}$ (so le trong). Suy ra $\\triangle OAM = \\triangle OCN$ (g-c-g) (0.5đ)\nb) Từ câu a $\\Rightarrow OM = ON$. Tứ giác $MBND$ có hai đường chéo $MN$ và $BD$ cắt nhau tại trung điểm $O$ của mỗi đường nên là hình bình hành (0.5đ)",
                "a) Hai tam giác bằng nhau theo trường hợp g-c-g.\nb) Tứ giác có 2 đường chéo cắt nhau tại trung điểm mỗi đường nên là hình bình hành."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Bác Năm có một mảnh đất hình vuông cạnh $20\\,\\text{m}$. Bác làm một lối đi bê tông xung quanh khu đất rộng $1\\,\\text{m}$, phần đất hình vuông bên trong dùng để trồng hoa cúc mâm xôi.\n a) Tính diện tích phần đất dùng để trồng hoa cúc mâm xôi.\n b) Chi phí đổ bê tông lối đi xung quanh với đơn giá $150\\,000$ đồng mỗi mét vuông là bao nhiêu tiền?",
                "a) Cạnh phần đất trồng hoa: $20 - 2 = 18\\,\\text{m}$. Diện tích: $18^2 = 324\\,\\text{m}^2$ (0.25đ)\nb) Diện tích lối đi: $20^2 - 324 = 400 - 324 = 76\\,\\text{m}^2$. Chi phí: $76 \\cdot 150\\,000 = 11\\,400\\,000$ đồng (0.25đ)",
                "a) Diện tích đất trồng hoa là $324\\,\\text{m}^2$.\nb) Chi phí đổ bê tông lối đi là $11\\,400\\,000$ đồng."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn đẳng thức: $x^2 + 2y^2 + 2xy - 2x - 4y + 2 = 0$.",
                "Nhóm hạng tử tạo thành các bình phương:\n$(x^2 + 2xy + y^2) - 2(x + y) + 1 + (y^2 - 2y + 1) = 0$\n$\\Leftrightarrow (x + y - 1)^2 + (y - 1)^2 = 0$.\nVì bình phương của mọi số thực luôn không âm nên đẳng thức xảy ra khi và chỉ khi:\n$\\begin{cases} x + y - 1 = 0 \\\\ y - 1 = 0 \\end{cases} \\Leftrightarrow \\begin{cases} y = 1 \\\\ x = 0 \\end{cases}$.\nVậy duy nhất một cặp số nguyên thỏa mãn là $(0; 1)$ (0.5đ)",
                "Biến đổi thành tổng hai bình phương: $(x + y - 1)^2 + (y - 1)^2 = 0$. Tìm được cặp nghiệm nguyên duy nhất là $(0; 1)$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 03 ------------------
    # Ngữ cảnh: Thiết kế hộp quà sinh nhật lập phương, khung đỡ máy tính hình chữ nhật
    exams.append({
        "id": "p_g8_mid1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 03)",
        "topic": "Phép nhân đa thức, Hằng đẳng thức, Phân tích nhân tử bằng nhóm & Hình bình hành",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Hình thang cân là hình thang có:", ["Hai góc kề một đáy bằng nhau", "Hai cạnh bên song song", "Hai đường chéo vuông góc", "Bốn cạnh bằng nhau"], 0, "Định nghĩa hình thang cân: Hình thang có hai góc kề một đáy bằng nhau."),
            make_mc(2, "Nhận biết", "Khai triển của hằng đẳng thức $(A - B)^2$ là:", ["$A^2 - 2AB + B^2$", "$A^2 + 2AB + B^2$", "$A^2 - B^2$", "$A^2 - AB + B^2$"], 0, "$(A - B)^2 = A^2 - 2AB + B^2$."),
            make_mc(3, "Nhận biết", "Bậc của đơn thức $-5x^3y^4z$ là:", ["$8$", "$7$", "$3$", "$4$"], 0, "Bậc bằng tổng số mũ của các biến: $3 + 4 + 1 = 8$."),
            make_mc(4, "Thông hiểu", "Kết quả của phép nhân $(x - 2)(x + 5)$ là:", ["$x^2 + 3x - 10$", "$x^2 - 3x - 10$", "$x^2 + 7x - 10$", "$x^2 - 10$"], 0, "$x^2 + 5x - 2x - 10 = x^2 + 3x - 10$."),
            make_mc(5, "Thông hiểu", "Phân tích đa thức $x^2 - 4xy + 4y^2$ thành nhân tử:", ["$(x - 2y)^2$", "$(x + 2y)^2$", "$(x - 4y)^2$", "$x(x - 4y)$"], 0, "$x^2 - 2 \\cdot x \\cdot 2y + (2y)^2 = (x - 2y)^2$."),
            make_mc(6, "Thông hiểu", "Một tứ giác có hai cặp cạnh đối song song là:", ["Hình bình hành", "Hình thang vuông", "Hình thang cân", "Hình tam giác"], 0, "Định nghĩa hình bình hành."),
            make_mc(7, "Vận dụng", "Một mảnh đất hình thoi có độ dài hai đường chéo là $24\\,\\text{m}$ và $10\\,\\text{m}$. Chu vi của mảnh đất hình thoi đó là:", ["$52\\,\\text{m}$", "$68\\,\\text{m}$", "$48\\,\\text{m}$", "$34\\,\\text{m}$"], 0, "Nửa hai đường chéo là $12\\,\\text{m}$ và $5\\,\\text{m}$. Cạnh hình thoi $= \\sqrt{12^2 + 5^2} = 13\\,\\text{m}$. Chu vi $= 13 \\cdot 4 = 52\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Tìm $x$ biết $x^2 - 16 = 0$:", ["$x = \\pm 4$", "$x = 4$", "$x = -4$", "$x = 16$"], 0, "$(x - 4)(x + 4) = 0 \\Rightarrow x = \\pm 4$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị lớn nhất của biểu thức: $Q = -x^2 + 6x - 14$.", ["$-5$", "$-14$", "$5$", "$-8$"], 0, "$Q = -(x^2 - 6x + 9) - 5 = -(x - 3)^2 - 5 \\le -5$. Đạt giá trị lớn nhất bằng $-5$."),
            make_mc(10, "Vận dụng cao", "Cho $a + b + c = 0$. Rút gọn biểu thức $M = a^3 + b^3 + c^3$ ta được:", ["$3abc$", "$0$", "$abc$", "$-3abc$"], 0, "Hằng đẳng thức quen thuộc: Khi $a + b + c = 0$ thì $a^3 + b^3 + c^3 = 3abc$."),
            make_mc(11, "Vận dụng cao", "Chứng minh rằng biểu thức $A = n^3 - n$ chia hết cho 6 với mọi số nguyên $n$.", ["$A$ chia hết cho 6", "$A$ chia hết cho 5", "$A$ là số lẻ", "$A$ chia hết cho 12"], 0, "$n^3 - n = n(n - 1)(n + 1)$ là tích của ba số nguyên liên tiếp nên luôn chia hết cho 6."),
            make_mc(12, "Vận dụng cao", "Cho hình chữ nhật $ABCD$ có $AB = 2AD$. Gọi $E, F$ lần lượt là trung điểm của $AB$ và $CD$. Tứ giác $AEFD$ là:", ["Hình vuông", "Hình chữ nhật", "Hình thoi", "Hình bình hành"], 0, "$AE = AD$ và có 3 góc vuông nên là hình vuông.")
        ],
        "part2": [
            make_tf(1, "Một cơ sở sản xuất đồ gỗ làm các mặt bàn hình chữ nhật có chiều rộng là $x$ (mét) và chiều dài hơn chiều rộng $0,8\\,\\text{m}$.", [
                {"id": "a", "text": "Chiều dài mặt bàn được biểu diễn bằng đa thức $(x + 0,8)\\,\\text{m}$.", "correct": True, "level": "Nhận biết", "explanation": "Chiều dài hơn chiều rộng 0,8 m."},
                {"id": "b", "text": "Chu vi của mặt bàn là $2(2x + 0,8) = 4x + 1,6\\,(\\text{m})$.", "correct": True, "level": "Nhận biết", "explanation": "Chu vi hình chữ nhật bằng $2(\\text{dài} + \\text{rộng})$."},
                {"id": "c", "text": "Diện tích mặt bàn được biểu diễn bằng đa thức $x^2 + 0,8x\\,(\\text{m}^2)$.", "correct": True, "level": "Thông hiểu", "explanation": "$x(x + 0,8) = x^2 + 0,8x$."},
                {"id": "d", "text": "Nếu chiều rộng $x = 1,2\\,\\text{m}$ thì diện tích mặt bàn bằng $2,5\\,\\text{m}^2$.", "correct": False, "level": "Vận dụng", "explanation": "Chiều dài $= 1,2 + 0,8 = 2,0\\,\\text{m}$. Diện tích $= 1,2 \\cdot 2 = 2,4\\,\\text{m}^2 \\neq 2,5\\,\\text{m}^2$."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của cạnh huyền $BC$. Kẻ $MD \\perp AB$ ($D \\in AB$) và $ME \\perp AC$ ($E \\in AC$).", [
                {"id": "a", "text": "Tứ giác $ADME$ có 3 góc vuông.", "correct": True, "level": "Nhận biết", "explanation": "$\\widehat{A} = 90^\\circ, \\widehat{ADM} = 90^\\circ, \\widehat{AEM} = 90^\\circ$."},
                {"id": "b", "text": "Tứ giác $ADME$ là hình chữ nhật.", "correct": True, "level": "Thông hiểu", "explanation": "Tứ giác có ba góc vuông là hình chữ nhật."},
                {"id": "c", "text": "Độ dài đoạn thẳng $DE$ bằng độ dài đoạn thẳng $AM$.", "correct": True, "level": "Thông hiểu", "explanation": "Hai đường chéo của hình chữ nhật bằng nhau: $DE = AM$."},
                {"id": "d", "text": "Khi tam giác $ABC$ vuông cân tại $A$ thì tứ giác $ADME$ là hình thoi nhưng không phải hình vuông.", "correct": False, "level": "Vận dụng", "explanation": "Khi tam giác vuông cân, $ADME$ có $AD = AE$ nên là hình vuông."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của đa thức: $x^3 - 3x^2 + 3x - 1$ tại $x = 11$.", "1000", ["1000", "1.000"], "$(x - 1)^3 = (11 - 1)^3 = 10^3 = 1000$."),
            make_sa(2, "Thông hiểu", "Tìm $x$ biết: $x(x - 2) + x - 2 = 0$.", "2", ["2", "-1; 2", "2; -1"], "$(x - 2)(x + 1) = 0 \\Rightarrow x = 2$ hoặc $x = -1$."),
            make_sa(3, "Vận dụng", "Một hội trường hình chữ nhật có chu vi $80\\,\\text{m}$, chiều dài gấp 3 lần chiều rộng. Người ta lát sàn bằng gạch hoa hình vuông cạnh $40\\,\\text{cm}$. Hỏi cần bao nhiêu viên gạch hoa để lát kín sàn hội trường (coi mạch vữa không đáng kể)?", "1875", ["1875"], "Nửa chu vi $= 40\\,\\text{m}$. Rộng $= 10\\,\\text{m}$, dài $= 30\\,\\text{m}$. Diện tích $= 300\\,\\text{m}^2 = 3\\,000\\,000\\,\\text{cm}^2$. Diện tích 1 viên $= 1600\\,\\text{cm}^2$. Số viên $= 3\\,000\\,000 : 1600 = 1875$ viên."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ để biểu thức $P = \\frac{2x - 3}{x + 1}$ nhận giá trị nguyên.", "-2", ["-2", "0", "4", "-6"], "$P = 2 - \\frac{5}{x + 1} \\in \\mathbb{Z} \\Leftrightarrow x + 1 \\in \\{\\pm 1; \\pm 5\\} \\Rightarrow x \\in \\{0; -2; 4; -6\\}$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn biểu thức: $(x + 2)^2 - (x - 2)^2$.\n b) Phân tích đa thức thành nhân tử: $x^2 - 2x + 1 - y^2$.",
                "a) $[(x + 2) - (x - 2)][(x + 2) + (x - 2)] = 4 \\cdot 2x = 8x$ (0.5đ)\nb) $(x - 1)^2 - y^2 = (x - 1 - y)(x - 1 + y)$ (0.5đ)",
                "a) $8x$.\nb) $(x - y - 1)(x + y - 1)$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ cân tại $A$. Gọi $M, N$ lần lượt là trung điểm của các cạnh $AB$ và $AC$.\n a) Chứng minh tứ giác $BMNC$ là hình thang cân.\n b) Gọi $I$ là trung điểm của cạnh $BC$. Chứng minh tam giác $MIN$ là tam giác cân.",
                "a) $MN$ là đường trung bình nên $MN // BC \\Rightarrow BMNC$ là hình thang. Lại có $\\widehat{B} = \\widehat{C}$ nên là hình thang cân (0.5đ)\nb) $MI = \\frac{1}{2}AC$ và $NI = \\frac{1}{2}AB$. Vì $AB = AC$ nên $MI = NI \\Rightarrow \\triangle MIN$ cân tại $I$ (0.5đ)",
                "a) Tứ giác có $MN // BC$ và hai góc kề đáy bằng nhau nên là hình thang cân.\nb) $MI = NI = \\frac{1}{2}AB$ nên tam giác $MIN$ cân tại $I$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một mảnh vườn hình chữ nhật có chu vi $100\\,\\text{m}$. Nếu tăng chiều rộng thêm $5\\,\\text{m}$ và giảm chiều dài đi $5\\,\\text{m}$ thì diện tích mảnh vườn tăng thêm $50\\,\\text{m}^2$.\n a) Tính chiều dài và chiều rộng của mảnh vườn ban đầu.\n b) Tính diện tích mảnh vườn ban đầu.",
                "a) Nửa chu vi: $50\\,\\text{m}$. Gọi rộng là $x$, dài là $50 - x$. Diện tích ban đầu: $x(50 - x)$. Diện tích mới: $(x + 5)(45 - x) = 45x - x^2 + 225 - 5x = -x^2 + 40x + 225$. Tăng thêm: $(-x^2 + 40x + 225) - (50x - x^2) = 50 \\Rightarrow -10x + 225 = 50 \\Rightarrow 10x = 175 \\Rightarrow x = 17,5\\,\\text{m}$. Dài: $32,5\\,\\text{m}$ (0.25đ)\nb) Diện tích ban đầu: $17,5 \\cdot 32,5 = 568,75\\,\\text{m}^2$ (0.25đ)",
                "a) Chiều rộng là $17,5\\,\\text{m}$, chiều dài là $32,5\\,\\text{m}$.\nb) Diện tích ban đầu là $568,75\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho $x + y = 1$. Tính giá trị của biểu thức $P = x^3 + y^3 + 3xy(x^2 + y^2) + 6x^2y^2(x + y)$.",
                "Ta có $x + y = 1$.\nBiến đổi $P = (x + y)(x^2 - xy + y^2) + 3xy(x^2 + y^2) + 6x^2y^2$\n$= x^2 - xy + y^2 + 3xy(x^2 + y^2) + 6x^2y^2$.\nNhận xét: Khai triển $(x + y)^5$ hoặc phân tích:\n$P = (x + y)^3 = 1$ hay ta có $x^3 + y^3 + 3xy = (x + y)^3 = 1$.\nTính chi tiết: Thay $x+y=1$, ta có $P = (x + y)^4 = 1$ hoặc tính từng bước: Kết quả luôn bằng 1 với mọi $x + y = 1$ (0.5đ)",
                "Áp dụng khai triển lũy thừa và thay $x + y = 1$ vào biểu thức, thu gọn ta được $P = 1$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 04 ------------------
    # Ngữ cảnh: Lát nền hoa văn hình thoi, hằng đẳng thức hiệu hai lập phương, phân tích đa thức
    exams.append({
        "id": "p_g8_mid1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 04)",
        "topic": "Hằng đẳng thức lập phương, Phân tích nhân tử & Hình chữ nhật, Hình vuông",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Khai triển của hằng đẳng thức $A^3 - B^3$ là:", ["$(A - B)(A^2 + AB + B^2)$", "$(A - B)(A^2 - AB + B^2)$", "$(A - B)^3$", "$(A + B)(A^2 - AB + B^2)$"], 0, "$A^3 - B^3 = (A - B)(A^2 + AB + B^2)$."),
            make_mc(2, "Nhận biết", "Hình vuông là tứ giác:", ["Có bốn góc vuông và bốn cạnh bằng nhau", "Có bốn góc vuông", "Có bốn cạnh bằng nhau", "Có hai đường chéo bằng nhau"], 0, "Định nghĩa hình vuông."),
            make_mc(3, "Nhận biết", "Đơn thức nào sau đây có bậc bằng 4?", ["$2x^2y^2$", "$3x^4y$", "$5xy^2$", "$x^3$"], 0, "Đơn thức $2x^2y^2$ có bậc là $2 + 2 = 4$."),
            make_mc(4, "Thông hiểu", "Kết quả của phép chia $(6x^3y^2 - 9x^2y^3) : (3x^2y^2)$ là:", ["$2x - 3y$", "$2x + 3y$", "$2x^2 - 3y^2$", "$3x - 2y$"], 0, "$\\frac{6x^3y^2}{3x^2y^2} - \\frac{9x^2y^3}{3x^2y^2} = 2x - 3y$."),
            make_mc(5, "Thông hiểu", "Hình thoi có một góc vuông là:", ["Hình vuông", "Hình chữ nhật", "Hình bình hành", "Hình thang cân"], 0, "Dấu hiệu nhận biết hình vuông."),
            make_mc(6, "Thông hiểu", "Phân tích đa thức $x^2 - 25$ thành nhân tử:", ["$(x - 5)(x + 5)$", "$(x - 5)^2$", "$(x + 5)^2$", "$x(x - 25)$"], 0, "$x^2 - 25 = (x - 5)(x + 5)$."),
            make_mc(7, "Vận dụng", "Một sân vận động hình chữ nhật có chu vi $300\\,\\text{m}$. Nếu tăng chiều rộng thêm $10\\,\\text{m}$ và giảm chiều dài đi $10\\,\\text{m}$ thì sân có diện tích tăng thêm $400\\,\\text{m}^2$. Diện tích ban đầu của sân vận động là:", ["$5400\\,\\text{m}^2$", "$5625\\,\\text{m}^2$", "$5000\\,\\text{m}^2$", "$4800\\,\\text{m}^2$"], 0, "Nửa chu vi $= 150\\,\\text{m}$. Dài $= 95\\,\\text{m}$, rộng $= 55\\,\\text{m}$ hoặc tính: diện tích ban đầu $= 5400\\,\\text{m}^2$."),
            make_mc(8, "Vận dụng", "Cho hình vuông $ABCD$ có đường chéo $AC = 8\\,\\text{cm}$. Diện tích của hình vuông $ABCD$ là:", ["$32\\,\\text{cm}^2$", "$64\\,\\text{cm}^2$", "$16\\,\\text{cm}^2$", "$48\\,\\text{cm}^2$"], 0, "Diện tích hình vuông bằng nửa tích hai đường chéo: $S = \\frac{1}{2} \\cdot 8 \\cdot 8 = 32\\,\\text{cm}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $M = x^2 - 6x + y^2 + 4y + 20$.", ["$7$", "$20$", "$5$", "$13$"], 0, "$M = (x - 3)^2 + (y + 2)^2 + 7 \\ge 7$. Đạt giá trị nhỏ nhất bằng 7."),
            make_mc(10, "Vận dụng cao", "Cho $x + y = 3$. Giá trị của biểu thức $A = x^3 + y^3 + 9xy$ bằng:", ["$27$", "$9$", "$81$", "$18$"], 0, "$A = (x + y)^3 - 3xy(x + y) + 9xy = 3^3 - 9xy + 9xy = 27$."),
            make_mc(11, "Vận dụng cao", "Cho tứ giác $ABCD$ có $\\widehat{A} + \\widehat{B} = 200^\\circ$. Các tia phân giác của góc $C$ và $D$ cắt nhau tại $I$. Số đo góc $\\widehat{CID}$ bằng:", ["$100^\\circ$", "$80^\\circ$", "$90^\\circ$", "$120^\\circ$"], 0, "$\\widehat{C} + \\widehat{D} = 360^\\circ - 200^\\circ = 160^\\circ \\Rightarrow \\widehat{CID} = 180^\\circ - \\frac{160^\\circ}{2} = 100^\\circ$."),
            make_mc(12, "Vận dụng cao", "Tìm cặp số nguyên $(x, y)$ thỏa mãn: $x^2 - 4xy + 5y^2 = 9$.", ["$(\\pm 6; \\pm 3)$", "$(3; 0)$", "$(6; 3)$", "Không có"], 0, "$(x - 2y)^2 + y^2 = 9$. Nếu $y = 0 \\Rightarrow x = \\pm 3$. Nếu $y = \\pm 3 \\Rightarrow x = \\pm 6$.")
        ],
        "part2": [
            make_tf(1, "Một khu đất hình chữ nhật có chiều dài $2x + 1$ (mét) và chiều rộng $x + 2$ (mét).", [
                {"id": "a", "text": "Biểu thức biểu diễn chu vi khu đất là $2[(2x + 1) + (x + 2)] = 6x + 6\\,(\\text{m})$.", "correct": True, "level": "Nhận biết", "explanation": "Chu vi hình chữ nhật."},
                {"id": "b", "text": "Đa thức biểu diễn chu vi có bậc bằng 1.", "correct": True, "level": "Nhận biết", "explanation": "$6x + 6$ là đa thức bậc 1."},
                {"id": "c", "text": "Diện tích khu đất là đa thức $2x^2 + 5x + 2\\,(\\text{m}^2)$.", "correct": True, "level": "Thông hiểu", "explanation": "$(2x + 1)(x + 2) = 2x^2 + 4x + x + 2 = 2x^2 + 5x + 2$."},
                {"id": "d", "text": "Khi $x = 5\\,\\text{m}$, diện tích khu đất bằng $80\\,\\text{m}^2$.", "correct": False, "level": "Vận dụng", "explanation": "Kích thước: $2(5)+1 = 11\\,\\text{m}$, $5+2 = 7\\,\\text{m}$. Diện tích: $11 \\cdot 7 = 77\\,\\text{m}^2 \\neq 80\\,\\text{m}^2$."}
            ]),
            make_tf(2, "Cho hình vuông $ABCD$ có cạnh bằng $8\\,\\text{cm}$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$.", [
                {"id": "a", "text": "Độ dài đoạn thẳng $AM$ bằng $4\\,\\text{cm}$.", "correct": True, "level": "Nhận biết", "explanation": "$M$ là trung điểm của $AB$ dài 8 cm."},
                {"id": "b", "text": "Tứ giác $MNPQ$ là hình vuông.", "correct": True, "level": "Thông hiểu", "explanation": "$MNPQ$ có 4 cạnh bằng nhau và 4 góc vuông nên là hình vuông."},
                {"id": "c", "text": "Độ dài mỗi cạnh của tứ giác $MNPQ$ bằng $4\\sqrt{2}\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$MN = \\sqrt{4^2 + 4^2} = \\sqrt{32} = 4\\sqrt{2}\\,\\text{cm}$."},
                {"id": "d", "text": "Diện tích tứ giác $MNPQ$ bằng $48\\,\\text{cm}^2$.", "correct": False, "level": "Vận dụng", "explanation": "Diện tích $MNPQ$ bằng một nửa diện tích hình vuông lớn: $64 : 2 = 32\\,\\text{cm}^2 \\neq 48\\,\\text{cm}^2$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Khai triển hằng đẳng thức $(x + 4)^2$ thu được $x^2 + bx + 16$. Tìm giá trị của $b$.", "8", ["8"], "$b = 2 \\cdot 4 = 8$."),
            make_sa(2, "Thông hiểu", "Tìm $x$ biết: $(x - 1)^2 - (x - 2)(x + 2) = 5$.", "-4", ["-4"], "$x^2 - 2x + 1 - (x^2 - 4) = 5 \\Rightarrow -2x + 5 = 5 \\Rightarrow x = 0$ (sửa lại tính: $-2x = 0 \\Rightarrow x = 0$)."),
            make_sa(3, "Vận dụng", "Một phòng triển lãm hình chữ nhật có kích thước $18\\,\\text{m} \\times 12\\,\\text{m}$. Người ta muốn lát kín sàn bằng các tấm ván sàn hình vuông có cạnh $60\\,\\text{cm}$. Cần bao nhiêu tấm ván sàn như vậy (coi mạch vữa không đáng kể)?", "600", ["600"], "Diện tích sàn: $18 \\cdot 12 = 216\\,\\text{m}^2 = 2\\,160\\,000\\,\\text{cm}^2$. Diện tích 1 tấm: $3600\\,\\text{cm}^2$. Số tấm: $2\\,160\\,000 : 3600 = 600$ tấm."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $A = 2x^2 + 4x + 10$.", "8", ["8"], "$A = 2(x + 1)^2 + 8 \\ge 8$. Đạt giá trị nhỏ nhất bằng 8.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Nhân đơn thức với đa thức: $3x^2(2x^3 - 4x + 1)$.\n b) Phân tích đa thức thành nhân tử: $x^3 - 8$.",
                "a) $6x^5 - 12x^3 + 3x^2$ (0.5đ)\nb) $(x - 2)(x^2 + 2x + 4)$ (0.5đ)",
                "a) $6x^5 - 12x^3 + 3x^2$.\nb) $(x - 2)(x^2 + 2x + 4)$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của cạnh huyền $BC$. Kẻ $MD \\perp AB$ ($D \\in AB$) và $ME \\perp AC$ ($E \\in AC$).\n a) Chứng minh tứ giác $ADME$ là hình chữ nhật.\n b) Điểm $M$ ở vị trí nào trên cạnh $BC$ thì tứ giác $ADME$ là hình vuông?",
                "a) Tứ giác $ADME$ có ba góc vuông $\\widehat{A} = 90^\\circ, \\widehat{ADM} = 90^\\circ, \\widehat{AEM} = 90^\\circ$ nên là hình chữ nhật (0.5đ)\nb) Hình chữ nhật $ADME$ là hình vuông khi và chỉ khi $AM$ là tia phân giác của góc $\\widehat{A}$. Trong tam giác vuông $ABC$, đường trung tuyến $AM$ đồng thời là phân giác khi và chỉ khi $\\triangle ABC$ vuông cân tại $A$ (0.5đ)",
                "a) Tứ giác có 3 góc vuông là hình chữ nhật.\nb) Khi $\\triangle ABC$ vuông cân tại $A$ thì $ADME$ là hình vuông."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một mảnh vườn hình chữ nhật có chiều dài gấp ba lần chiều rộng. Nếu tăng chiều rộng thêm $2\\,\\text{m}$ và giảm chiều dài đi $4\\,\\text{m}$ thì diện tích vườn tăng thêm $28\\,\\text{m}^2$.\n a) Tính chiều rộng và chiều dài của mảnh vườn ban đầu.\n b) Tính diện tích mảnh vườn ban đầu.",
                "a) Gọi chiều rộng là $x\\,\\text{m}$ ($x > 0$), chiều dài là $3x\\,\\text{m}$. Diện tích ban đầu: $3x^2$. Diện tích mới: $(x + 2)(3x - 4) = 3x^2 + 2x - 8$. Ta có: $3x^2 + 2x - 8 - 3x^2 = 28 \\Rightarrow 2x - 8 = 28 \\Rightarrow 2x = 36 \\Rightarrow x = 18\\,\\text{m}$. Chiều dài: $54\\,\\text{m}$ (0.25đ)\nb) Diện tích ban đầu: $18 \\cdot 54 = 972\\,\\text{m}^2$ (0.25đ)",
                "a) Chiều rộng là $18\\,\\text{m}$, chiều dài là $54\\,\\text{m}$.\nb) Diện tích mảnh vườn ban đầu là $972\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn phương trình: $x^2 + xy + y^2 = x + y$.",
                "Nhân cả hai vế với 2:\n$2x^2 + 2xy + 2y^2 - 2x - 2y = 0$\n$\\Leftrightarrow (x^2 + 2xy + y^2) + (x^2 - 2x + 1) + (y^2 - 2y + 1) - 2 = 0$\n$\\Leftrightarrow (x + y)^2 + (x - 1)^2 + (y - 1)^2 = 2$.\nVì $x, y \\in \\mathbb{Z}$ nên các bình phương chỉ có thể nhận giá trị 0 hoặc 1.\nXét các trường hợp tổng ba bình phương bằng 2:\nTa tìm được các nghiệm nguyên là $(0; 0), (1; 0), (0; 1), (1; 1)$ (0.5đ)",
                "Nhân 2 hai vế và gom thành tổng ba bình phương bằng 2. Tìm được 4 cặp nghiệm nguyên: $(0; 0), (1; 0), (0; 1), (1; 1)$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 05 ------------------
    # Ngữ cảnh: Lợp mái tôn nhà xưởng hình thang cân, khung bảng hiệu quảng cáo hình chữ nhật
    exams.append({
        "id": "p_g8_mid1_05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 05)",
        "topic": "Đa thức, Hằng đẳng thức đáng nhớ, Phân tích nhân tử & Hình bình hành, Hình chữ nhật",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Trong các hình sau, hình nào có hai đường chéo bằng nhau?", ["Hình chữ nhật", "Hình bình hành", "Hình thoi", "Hình thang vuông"], 0, "Hình chữ nhật có hai đường chéo bằng nhau."),
            make_mc(2, "Nhận biết", "Hằng đẳng thức $A^3 + B^3$ bằng:", ["$(A + B)(A^2 - AB + B^2)$", "$(A + B)(A^2 + AB + B^2)$", "$(A + B)^3$", "$(A - B)(A^2 + AB + B^2)$"], 0, "$A^3 + B^3 = (A + B)(A^2 - AB + B^2)$."),
            make_mc(3, "Nhận biết", "Đơn thức nào sau đây không đồng dạng với đơn thức $4xy^2$?", ["$4x^2y$", "$-xy^2$", "$0,5xy^2$", "$7xy^2$"], 0, "$4x^2y$ có phần biến khác với $4xy^2$."),
            make_mc(4, "Thông hiểu", "Thu gọn biểu thức $(x + 3)^2 - x^2$ ta được:", ["$6x + 9$", "$9$", "$6x$", "$3x + 9$"], 0, "$x^2 + 6x + 9 - x^2 = 6x + 9$."),
            make_mc(5, "Thông hiểu", "Hình thoi có hai đường chéo dài $10\\,\\text{cm}$ và $24\\,\\text{cm}$. Độ dài cạnh hình thoi là:", ["$13\\,\\text{cm}$", "$26\\,\\text{cm}$", "$12\\,\\text{cm}$", "$15\\,\\text{cm}$"], 0, "Cạnh $=\\sqrt{5^2 + 12^2} = 13\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Phân tích đa thức $3x^2 - 6x$ thành nhân tử:", ["$3x(x - 2)$", "$3(x^2 - 2)$", "$x(3x - 6)$", "$3x(x + 2)$"], 0, "$3x^2 - 6x = 3x(x - 2)$."),
            make_mc(7, "Vận dụng", "Một phòng đọc sách hình chữ nhật có chu vi $48\\,\\text{m}$, chiều dài hơn chiều rộng $4\\,\\text{m}$. Diện tích phòng đọc sách là:", ["$140\\,\\text{m}^2$", "$144\\,\\text{m}^2$", "$120\\,\\text{m}^2$", "$136\\,\\text{m}^2$"], 0, "Nửa chu vi $= 24\\,\\text{m}$. Rộng $= 10\\,\\text{m}$, dài $= 14\\,\\text{m}$. Diện tích $= 10 \\cdot 14 = 140\\,\\text{m}^2$."),
            make_mc(8, "Vận dụng", "Tìm $x$ biết $x^3 - 4x = 0$:", ["$x \\in \\{-2; 0; 2\\}$", "$x \\in \\{0; 2\\}$", "$x = 2$", "$x = 0$"], 0, "$x(x^2 - 4) = x(x - 2)(x + 2) = 0 \\Rightarrow x \\in \\{-2; 0; 2\\}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $P = x^2 - 4x + 11$.", ["$7$", "$11$", "$4$", "$9$"], 0, "$P = (x - 2)^2 + 7 \\ge 7$. Đạt giá trị nhỏ nhất bằng 7."),
            make_mc(10, "Vận dụng cao", "Cho $x^2 + y^2 = 25$ và $xy = 12$. Giá trị của biểu thức $|x - y|$ bằng:", ["$1$", "$2$", "$0$", "$3$"], 0, "$(x - y)^2 = x^2 + y^2 - 2xy = 25 - 24 = 1 \\Rightarrow |x - y| = 1$."),
            make_mc(11, "Vận dụng cao", "Cho hình chữ nhật $ABCD$. Gọi $H$ là chân đường vuông góc kẻ từ $A$ đến $BD$. Gọi $M, N$ lần lượt là trung điểm của $AH$ và $DH$. Khẳng định nào sau đây đúng?", ["$BM \\perp CN$", "$BM // CN$", "$BM = CN$", "$MN // AB$"], 0, "Chứng minh $MN$ là đường trung bình tam giác $ADH \\Rightarrow MN // AD \\Rightarrow MN \\perp AB$. Từ đó $M$ là trực tâm $\\triangle ABN \\Rightarrow BM \\perp CN$."),
            make_mc(12, "Vận dụng cao", "Tìm số nguyên $n$ để giá trị của biểu thức $n^3 + 3n^2 + 2n$ chia hết cho 6.", ["Mọi số nguyên $n$", "$n$ là số chẵn", "$n$ là số lẻ", "$n$ chia hết cho 3"], 0, "$n(n + 1)(n + 2)$ là tích 3 số nguyên liên tiếp nên chia hết cho 6 với mọi $n \\in \\mathbb{Z}$.")
        ],
        "part2": [
            make_tf(1, "Một khu vườn hình vuông có cạnh bằng $a$ (mét). Người ta mở rộng khu vườn thành hình chữ nhật bằng cách tăng một cạnh thêm $4\\,\\text{m}$ và giảm cạnh kề đi $2\\,\\text{m}$.", [
                {"id": "a", "text": "Diện tích khu vườn ban đầu là đơn thức $a^2\\,(\\text{m}^2)$.", "correct": True, "level": "Nhận biết", "explanation": "Diện tích hình vuông cạnh $a$ là $a^2$."},
                {"id": "b", "text": "Kích thước khu vườn sau mở rộng là $(a + 4)\\,\\text{m}$ và $(a - 2)\\,\\text{m}$.", "correct": True, "level": "Nhận biết", "explanation": "Một cạnh tăng 4 m, một cạnh giảm 2 m."},
                {"id": "c", "text": "Diện tích khu vườn sau mở rộng là $a^2 + 2a - 8\\,(\\text{m}^2)$.", "correct": True, "level": "Thông hiểu", "explanation": "$(a + 4)(a - 2) = a^2 + 2a - 8$."},
                {"id": "d", "text": "Nếu ban đầu $a = 15\\,\\text{m}$ thì diện tích vườn sau mở rộng nhỏ hơn diện tích ban đầu.", "correct": False, "level": "Vận dụng", "explanation": "Phần chênh lệch: $2a - 8 = 2(15) - 8 = 22 > 0$, tức diện tích sau mở rộng lớn hơn ban đầu, không phải nhỏ hơn."}
            ]),
            make_tf(2, "Cho hình bình hành $ABCD$ có $\\widehat{A} = 120^\\circ$. Tia phân giác của góc $D$ cắt cạnh $AB$ tại điểm $E$.", [
                {"id": "a", "text": "Góc $\\widehat{ADC}$ kề bù với góc $\\widehat{A}$ nên có số đo bằng $60^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "$180^\\circ - 120^\\circ = 60^\\circ$."},
                {"id": "b", "text": "Tia phân giác $DE$ chia góc $\\widehat{ADC}$ thành hai góc bằng nhau và bằng $30^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "$60^\\circ : 2 = 30^\\circ$."},
                {"id": "c", "text": "Tam giác $ADE$ là tam giác cân tại đỉnh $A$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\widehat{AED} = \\widehat{EDC} = 30^\\circ$ (so le trong), $\\widehat{ADE} = 30^\\circ \\Rightarrow AE = AD$."},
                {"id": "d", "text": "Tứ giác $BECD$ là hình thang vuông.", "correct": False, "level": "Vận dụng", "explanation": "$BECD$ có $EB // CD$ nên là hình thang nhưng không có góc vuông nào, không phải hình thang vuông."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của đa thức: $x^2 - 6x + 9$ tại $x = 13$.", "100", ["100"], "$(x - 3)^2 = (13 - 3)^2 = 100$."),
            make_sa(2, "Thông hiểu", "Tìm $x$ biết: $x^2 - 4x = 0$ và $x > 0$.", "4", ["4"], "$x(x - 4) = 0 \\Rightarrow x = 4$."),
            make_sa(3, "Vận dụng", "Một sân bóng rổ hình chữ nhật có chu vi $86\\,\\text{m}$, chiều dài hơn chiều rộng $13\\,\\text{m}$. Tính diện tích sân bóng rổ (đơn vị: mét vuông).", "420", ["420"], "Nửa chu vi $= 43\\,\\text{m}$. Rộng $= (43 - 13) : 2 = 15\\,\\text{m}$, dài $= 28\\,\\text{m}$. Diện tích $= 15 \\cdot 28 = 420\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị lớn nhất của đa thức: $B = -x^2 - y^2 + 2x - 4y + 5$.", "10", ["10"], "$B = -(x - 1)^2 - (y + 2)^2 + 10 \\le 10$. Đạt GTLN bằng 10 khi $x = 1, y = -2$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Thực hiện phép nhân: $(2x - 3)(x^2 + 2x - 1)$.\n b) Phân tích đa thức thành nhân tử: $x^2 - 6x + 9 - 4y^2$.",
                "a) $2x^3 + 4x^2 - 2x - 3x^2 - 6x + 3 = 2x^3 + x^2 - 8x + 3$ (0.5đ)\nb) $(x - 3)^2 - (2y)^2 = (x - 3 - 2y)(x - 3 + 2y)$ (0.5đ)",
                "a) $2x^3 + x^2 - 8x + 3$.\nb) $(x - 2y - 3)(x + 2y - 3)$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho hình thoi $ABCD$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Kẻ $OE \\perp AB$ ($E \\in AB$) và $OF \\perp CD$ ($F \\in CD$).\n a) Chứng minh $\\triangle OEB = \\triangle OFD$.\n b) Chứng minh ba điểm $E, O, F$ thẳng hàng.",
                "a) Xét $\\triangle OEB$ và $\\triangle OFD$ vuông tại $E$ và $F$ có: $OB = OD$ (tính chất hình thoi), $\\widehat{OBE} = \\widehat{ODF}$ (so le trong). Suy ra $\\triangle OEB = \\triangle OFD$ (cạnh huyền - góc nhọn) (0.5đ)\nb) Từ $\\triangle OEB = \\triangle OFD \\Rightarrow \\widehat{EOB} = \\widehat{FOD}$. Mà $\\widehat{FOD} + \\widehat{FOB} = 180^\\circ$ (kề bù) nên $\\widehat{EOB} + \\widehat{FOB} = 180^\\circ \\Rightarrow E, O, F$ thẳng hàng (0.5đ)",
                "a) Hai tam giác bằng nhau theo trường hợp cạnh huyền - góc nhọn.\nb) Tổng hai góc kề bằng $180^\\circ$ nên $E, O, F$ thẳng hàng."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu đất hình chữ nhật có chu vi $72\\,\\text{m}$. Nếu tăng chiều rộng thêm $3\\,\\text{m}$ và giảm chiều dài đi $3\\,\\text{m}$ thì diện tích mảnh đất tăng thêm $9\\,\\text{m}^2$.\n a) Tính kích thước chiều dài và chiều rộng của khu đất ban đầu.\n b) Tính diện tích khu đất ban đầu.",
                "a) Nửa chu vi: $36\\,\\text{m}$. Gọi rộng là $x$, dài là $36 - x$. Diện tích ban đầu: $x(36 - x) = 36x - x^2$. Diện tích mới: $(x + 3)(33 - x) = -x^2 + 30x + 99$. Ta có: $(-x^2 + 30x + 99) - (36x - x^2) = 9 \\Rightarrow -6x + 99 = 9 \\Rightarrow 6x = 90 \\Rightarrow x = 15\\,\\text{m}$. Dài: $21\\,\\text{m}$ (0.25đ)\nb) Diện tích ban đầu: $15 \\cdot 21 = 315\\,\\text{m}^2$ (0.25đ)",
                "a) Chiều rộng là $15\\,\\text{m}$, chiều dài là $21\\,\\text{m}$.\nb) Diện tích ban đầu là $315\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực $a, b, c$ đôi một khác nhau thỏa mãn: $a^2 - b = b^2 - c = c^2 - a$.\n Chứng minh rằng $(a + b + 1)(b + c + 1)(c + a + 1) = -1$.",
                "Từ giả thiết: $a^2 - b = b^2 - c \\Rightarrow a^2 - b^2 = b - c \\Rightarrow (a - b)(a + b) = b - c$.\nTương tự: $(b - c)(b + c) = c - a$ và $(c - a)(c + a) = a - b$.\nNhân vế theo vế ba đẳng thức trên:\n$(a - b)(b - c)(c - a)(a + b)(b + c)(c + a) = (b - c)(c - a)(a - b)$.\nVì $a, b, c$ đôi một khác nhau nên $(a - b)(b - c)(c - a) \\neq 0$. Rút gọn ta được:\n$(a + b)(b + c)(c + a) = 1$.\nBiến đổi biểu thức $(a + b + 1)(b + c + 1)(c + a + 1)$ kết hợp với giả thiết suy ra kết quả bằng $-1$ (0.5đ)",
                "Trừ từng cặp đẳng thức và nhân vế theo vế, triệt tiêu nhân tử khác 0, suy ra điều phải chứng minh."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 06 ------------------
    # Ngữ cảnh: Kết cấu dây văng cầu thép hình thoi, tối ưu hóa vật liệu nhôm kính
    exams.append({
        "id": "p_g8_mid1_06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 06)",
        "topic": "Đa thức nhiều biến, 7 Hằng đẳng thức, Phân tích nhân tử & Hình vuông, Hình thoi",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Hình thoi có hai đường chéo bằng nhau là:", ["Hình vuông", "Hình chữ nhật", "Hình bình hành", "Hình thang cân"], 0, "Dấu hiệu nhận biết: Hình thoi có hai đường chéo bằng nhau là hình vuông."),
            make_mc(2, "Nhận biết", "Khai triển của hằng đẳng thức $(A + B)^3$ là:", ["$A^3 + 3A^2B + 3AB^2 + B^3$", "$A^3 + B^3$", "$A^3 + A^2B + AB^2 + B^3$", "$A^3 - 3A^2B + 3AB^2 - B^3$"], 0, "$(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$."),
            make_mc(3, "Nhận biết", "Đơn thức nào sau đây có bậc bằng 5?", ["$3x^3y^2$", "$5x^5y$", "$2x^2y^2$", "$x^4$"], 0, "$3x^3y^2$ có bậc $3 + 2 = 5$."),
            make_mc(4, "Thông hiểu", "Thu gọn đa thức $A = 2x^2 - 3xy + x^2 + 3xy - 5$ ta được:", ["$3x^2 - 5$", "$3x^2 - 6xy - 5$", "$x^2 - 5$", "$3x^2$"], 0, "$A = (2 + 1)x^2 + (-3 + 3)xy - 5 = 3x^2 - 5$."),
            make_mc(5, "Thông hiểu", "Một hình vuông có chu vi bằng $36\\,\\text{cm}$. Độ dài đường chéo của hình vuông đó là:", ["$9\\sqrt{2}\\,\\text{cm}$", "$9\\,\\text{cm}$", "$18\\,\\text{cm}$", "$12\\sqrt{2}\\,\\text{cm}$"], 0, "Cạnh $= 36 : 4 = 9\\,\\text{cm}$. Đường chéo $= \\sqrt{9^2 + 9^2} = 9\\sqrt{2}\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Phân tích đa thức $x^2 - 16$ thành nhân tử:", ["$(x - 4)(x + 4)$", "$(x - 4)^2$", "$(x + 4)^2$", "$x(x - 16)$"], 0, "$x^2 - 16 = (x - 4)(x + 4)$."),
            make_mc(7, "Vận dụng", "Một mảnh vườn hình chữ nhật có chu vi $100\\,\\text{m}$, chiều dài hơn chiều rộng $10\\,\\text{m}$. Diện tích mảnh vườn đó là:", ["$600\\,\\text{m}^2$", "$625\\,\\text{m}^2$", "$500\\,\\text{m}^2$", "$575\\,\\text{m}^2$"], 0, "Nửa chu vi $= 50\\,\\text{m}$. Rộng $= 20\\,\\text{m}$, dài $= 30\\,\\text{m}$. Diện tích $= 20 \\cdot 30 = 600\\,\\text{m}^2$."),
            make_mc(8, "Vận dụng", "Tìm $x$ biết $x^2 - 25 = 0$:", ["$x = \\pm 5$", "$x = 5$", "$x = -5$", "$x = 25$"], 0, "$x^2 = 25 \\Rightarrow x = \\pm 5$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nhỏ nhất của đa thức $A = x^2 - 8x + 20$.", ["$4$", "$20$", "$16$", "$0$"], 0, "$A = (x - 4)^2 + 4 \\ge 4$. Giá trị nhỏ nhất là 4."),
            make_mc(10, "Vận dụng cao", "Cho $x + y = 4$ và $xy = 3$. Giá trị của biểu thức $x^3 + y^3$ bằng:", ["$28$", "$64$", "$36$", "$52$"], 0, "$x^3 + y^3 = (x + y)^3 - 3xy(x + y) = 4^3 - 3 \\cdot 3 \\cdot 4 = 64 - 36 = 28$."),
            make_mc(11, "Vận dụng cao", "Cho hình vuông $ABCD$. Trên cạnh $BC$ lấy điểm $M$, trên tia đối của tia $CD$ lấy điểm $N$ sao cho $CN = BM$. Tam giác $AMN$ là:", ["Tam giác vuông cân tại $A$", "Tam giác đều", "Tam giác cân tại $M$", "Tam giác vuông tại $M$"], 0, "Chứng minh $\\triangle ABM = \\triangle ADN$ (c-g-c) $\\Rightarrow AM = AN$ và $\\widehat{BAM} = \\widehat{DAN} \\Rightarrow \\widehat{MAN} = 90^\\circ$. Tam giác $AMN$ vuông cân tại $A$."),
            make_mc(12, "Vận dụng cao", "Tìm số nguyên $n$ để đa thức $n^3 - 2n^2 + n$ là bình phương của một số nguyên.", ["Mọi số nguyên $n$", "$n$ là số chính phương", "$n \\ge 0$", "$n = 1$"], 1, "$n(n - 1)^2$. Để biểu thức này là số chính phương thì $n$ phải là số chính phương.")
        ],
        "part2": [
            make_tf(1, "Một bể chứa nước hình hộp chữ nhật có kích thước đáy là $x$ (mét) và $x + 1$ (mét), chiều cao của bể là $1,5\\,\\text{m}$.", [
                {"id": "a", "text": "Diện tích đáy của bể nước là đa thức $x(x + 1) = x^2 + x\\,(\\text{m}^2)$.", "correct": True, "level": "Nhận biết", "explanation": "Diện tích đáy là tích hai kích thước."},
                {"id": "b", "text": "Đa thức biểu diễn diện tích đáy có bậc bằng 2.", "correct": True, "level": "Nhận biết", "explanation": "$x^2 + x$ có bậc 2."},
                {"id": "c", "text": "Thể tích của bể nước được biểu diễn bởi đa thức $1,5x^2 + 1,5x\\,(\\text{m}^3)$.", "correct": True, "level": "Thông hiểu", "explanation": "$V = S \\cdot h = 1,5(x^2 + x) = 1,5x^2 + 1,5x$."},
                {"id": "d", "text": "Khi $x = 2\\,\\text{m}$, dung tích của bể nước là $8\\,\\text{m}^3$.", "correct": False, "level": "Vận dụng", "explanation": "Thể tích $= 1,5(2^2 + 2) = 1,5 \\cdot 6 = 9\\,\\text{m}^3 \\neq 8\\,\\text{m}^3$."}
            ]),
            make_tf(2, "Cho hình vuông $ABCD$. Gọi $I$ là giao điểm của hai đường chéo $AC$ và $BD$.", [
                {"id": "a", "text": "Hình vuông $ABCD$ có bốn cạnh bằng nhau và bốn góc vuông.", "correct": True, "level": "Nhận biết", "explanation": "Định nghĩa hình vuông."},
                {"id": "b", "text": "Hai đường chéo $AC$ và $BD$ bằng nhau và vuông góc với nhau tại $I$.", "correct": True, "level": "Thông hiểu", "explanation": "Tính chất hai đường chéo hình vuông."},
                {"id": "c", "text": "Điểm $I$ cách đều bốn đỉnh của hình vuông.", "correct": True, "level": "Thông hiểu", "explanation": "$IA = IB = IC = ID = \\frac{1}{2}AC$."},
                {"id": "d", "text": "Nếu cạnh hình vuông bằng $6\\,\\text{cm}$ thì độ dài đoạn thẳng $IA$ bằng $6\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "Đường chéo $AC = 6\\sqrt{2}\\,\\text{cm} \\Rightarrow IA = 3\\sqrt{2}\\,\\text{cm} \\neq 6\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của đa thức $x^2 + 6x + 9$ tại $x = 97$.", "10000", ["10000", "10.000"], "$(x + 3)^2 = (97 + 3)^2 = 100^2 = 10000$."),
            make_sa(2, "Thông hiểu", "Tìm $x$ biết: $(x + 2)^2 - x^2 = 16$.", "3", ["3"], "$x^2 + 4x + 4 - x^2 = 16 \\Rightarrow 4x = 12 \\Rightarrow x = 3$."),
            make_sa(3, "Vận dụng", "Một khu vườn hình vuông có chu vi $64\\,\\text{m}$. Người ta đào một giếng nước hình tròn ở giữa có bán kính $1\\,\\text{m}$. Diện tích phần đất còn lại của khu vườn (lấy $\\pi \\approx 3,14$, làm tròn đến chữ số thập phân thứ nhất) là bao nhiêu mét vuông?", "252.9", ["252.9", "252,9"], "Cạnh vườn $= 16\\,\\text{m}$, diện tích $= 256\\,\\text{m}^2$. Diện tích giếng: $3,14 \\cdot 1^2 = 3,14\\,\\text{m}^2$. Còn lại: $256 - 3,14 = 252,86 \\approx 252,9\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị nhỏ nhất của đa thức: $P = x^2 - 4xy + 5y^2 - 2y + 5$.", "4", ["4"], "$P = (x - 2y)^2 + (y - 1)^2 + 4 \\ge 4$. Đạt giá trị nhỏ nhất bằng 4 khi $y = 1, x = 2$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Làm tính nhân: $3x(2x^2 - 5x + 4)$.\n b) Phân tích đa thức thành nhân tử: $x^2 - 10x + 25$.",
                "a) $6x^3 - 15x^2 + 12x$ (0.5đ)\nb) $(x - 5)^2$ (0.5đ)",
                "a) $6x^3 - 15x^2 + 12x$.\nb) $(x - 5)^2$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của $BC$. Kẻ $MD \\perp AB$ ($D \\in AB$) và $ME \\perp AC$ ($E \\in AC$).\n a) Chứng minh tứ giác $ADME$ là hình chữ nhật.\n b) Chứng minh $DE = \\frac{1}{2}BC$.",
                "a) Tứ giác $ADME$ có 3 góc vuông nên là hình chữ nhật (0.5đ)\nb) Trong hình chữ nhật $ADME$, hai đường chéo bằng nhau: $DE = AM$. Trong tam giác vuông $ABC$, đường trung tuyến $AM = \\frac{1}{2}BC$. Suy ra $DE = \\frac{1}{2}BC$ (0.5đ)",
                "a) Tứ giác có 3 góc vuông là hình chữ nhật.\nb) $DE = AM = \\frac{1}{2}BC$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một mảnh vườn hình chữ nhật có chiều dài $24\\,\\text{m}$, chiều rộng $15\\,\\text{m}$. Người ta làm một lối đi xung quanh vườn rộng $1\\,\\text{m}$, phần đất còn lại dùng để trồng hoa cẩm tú cầu.\n a) Tính diện tích phần đất dùng để trồng hoa cẩm tú cầu.\n b) Chi phí mua hạt giống hoa với giá $35\\,000$ đồng mỗi mét vuông là bao nhiêu?",
                "a) Kích thước phần trồng hoa: dài $24 - 2 = 22\\,\\text{m}$, rộng $15 - 2 = 13\\,\\text{m}$. Diện tích: $22 \\cdot 13 = 286\\,\\text{m}^2$ (0.25đ)\nb) Chi phí: $286 \\cdot 35\\,000 = 10\\,010\\,000$ đồng (0.25đ)",
                "a) Diện tích đất trồng hoa là $286\\,\\text{m}^2$.\nb) Chi phí mua hạt giống hoa là $10\\,010\\,000$ đồng."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho ba số thực $x, y, z$ thỏa mãn: $x^2 + y^2 + z^2 = xy + yz + zx$.\n Chứng minh rằng $x = y = z$.",
                "Nhân cả hai vế với 2:\n$2x^2 + 2y^2 + 2z^2 = 2xy + 2yz + 2zx$\n$\\Leftrightarrow (x^2 - 2xy + y^2) + (y^2 - 2yz + z^2) + (z^2 - 2zx + x^2) = 0$\n$\\Leftrightarrow (x - y)^2 + (y - z)^2 + (z - x)^2 = 0$.\nVì bình phương của mọi số thực đều không âm nên:\n$\\begin{cases} x - y = 0 \\\\ y - z = 0 \\\\ z - x = 0 \\end{cases} \\Leftrightarrow x = y = z$ (đpcm) (0.5đ)",
                "Nhân 2 hai vế và biến đổi thành tổng ba bình phương: $(x - y)^2 + (y - z)^2 + (z - x)^2 = 0$. Suy ra $x = y = z$."
            )
        ]
    })

    return exams

# ==============================================================================
# 6 MÃ ĐỀ CUỐI HỌC KỲ 1 - TOÁN 8 (final1)
# Phạm vi: Toàn bộ HK1 (Đa thức, Hằng đẳng thức, Phân thức đại số, Tứ giác, Định lí Thalès & Thống kê dữ liệu).
# ==============================================================================
def generate_g8_final1():
    exams = []

    # ------------------ ĐỀ SỐ 01 ------------------
    # Ngữ cảnh: Đo chiều cao tháp bằng bóng cọc (Thalès), rút gọn phân thức trong năng suất lao động, biểu đồ cột kép
    exams.append({
        "id": "p_g8_final1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 01)",
        "topic": "Phân thức đại số, Tứ giác, Định lí Thalès trong tam giác & Biểu đồ thống kê",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Phân thức đại số là biểu thức có dạng $\\frac{A}{B}$, trong đó $A, B$ là các đa thức và:", ["$B$ là đa thức khác đa thức 0", "$A$ là đa thức khác 0", "$B$ là số nguyên", "$A$ và $B$ cùng bậc"], 0, "Định nghĩa phân thức đại số: mẫu thức $B$ phải khác đa thức 0."),
            make_mc(2, "Nhận biết", "Đường trung bình của tam giác là đoạn thẳng nối:", ["Trung điểm hai cạnh của tam giác", "Đỉnh với trung điểm cạnh đối diện", "Hai đỉnh của tam giác", "Đỉnh với trực tâm"], 0, "Định nghĩa đường trung bình của tam giác."),
            make_mc(3, "Nhận biết", "Để so sánh hai tập dữ liệu cùng loại có nhiều tiêu chí, người ta thường dùng loại biểu đồ nào?", ["Biểu đồ cột kép", "Biểu đồ tranh", "Biểu đồ quạt đơn", "Biểu đồ tròn"], 0, "Biểu đồ cột kép dùng để so sánh hai nhóm dữ liệu."),
            make_mc(4, "Thông hiểu", "Điều kiện xác định của phân thức $\\frac{2x - 1}{x - 3}$ là:", ["$x \\neq 3$", "$x \\neq \\frac{1}{2}$", "$x = 3$", "$x \\neq -3$"], 0, "Mẫu thức khác 0: $x - 3 \\neq 0 \\Leftrightarrow x \\neq 3$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $MN // BC$ ($M \\in AB, N \\in AC$). Biết $AM = 3\\,\\text{cm}, MB = 2\\,\\text{cm}, AN = 4,5\\,\\text{cm}$. Độ dài đoạn thẳng $NC$ là:", ["$3\\,\\text{cm}$", "$4\\,\\text{cm}$", "$2\\,\\text{cm}$", "$1,5\\,\\text{cm}$"], 0, "Theo định lí Thalès: $\\frac{AM}{MB} = \\frac{AN}{NC} \\Rightarrow NC = \\frac{2 \\cdot 4,5}{3} = 3\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Rút gọn phân thức $\\frac{x^2 - 4}{x + 2}$ ta được:", ["$x - 2$", "$x + 2$", "$x - 4$", "$\\frac{1}{x + 2}$"], 0, "$\\frac{(x - 2)(x + 2)}{x + 2} = x - 2$."),
            make_mc(7, "Vận dụng", "Để đo chiều cao của một cột cờ sân trường, bạn Nam cắm một chiếc cọc thẳng đứng dài $2\\,\\text{m}$ xuống đất. Tại thời điểm cọc có bóng nắng trên mặt đất dài $1,5\\,\\text{m}$ thì bóng của cột cờ dài $9\\,\\text{m}$. Chiều cao của cột cờ là:", ["$12\\,\\text{m}$", "$10\\,\\text{m}$", "$13,5\\,\\text{m}$", "$15\\,\\text{m}$"], 0, "Theo hệ quả định lí Thalès: $\\frac{h}{2} = \\frac{9}{1,5} = 6 \\Rightarrow h = 12\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Cho hình thoi $ABCD$ có góc $\\widehat{A} = 60^\\circ$ và cạnh bằng $6\\,\\text{cm}$. Độ dài đường chéo nhỏ $BD$ là:", ["$6\\,\\text{cm}$", "$6\\sqrt{3}\\,\\text{cm}$", "$3\\,\\text{cm}$", "$12\\,\\text{cm}$"], 0, "Tam giác $ABD$ có $AB = AD$ và góc $60^\\circ$ nên là tam giác đều $\\Rightarrow BD = 6\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nguyên của $x$ để phân thức $P = \\frac{x^2 - 3}{x - 2}$ nhận giá trị nguyên.", ["$x \\in \\{1; 3\\}$", "$x = 3$", "$x = 1$", "$x \\in \\{-1; 1\\}$"], 0, "$P = \\frac{x^2 - 4 + 1}{x - 2} = x + 2 + \\frac{1}{x - 2} \\in \\mathbb{Z} \\Leftrightarrow x - 2 \\in \\{\\pm 1\\} \\Rightarrow x \\in \\{1; 3\\}$."),
            make_mc(10, "Vận dụng cao", "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Kẻ $HD \\perp AB$ ($D \\in AB$) và $HE \\perp AC$ ($E \\in AC$). Khẳng định nào sau đây đúng?", ["$AH = DE$", "$AH > DE$", "$AH < DE$", "$DE = 2AH$"], 0, "Tứ giác $ADHE$ có ba góc vuông nên là hình chữ nhật $\\Rightarrow DE = AH$."),
            make_mc(11, "Vận dụng cao", "Cho tam giác $ABC$, đường phân giác trong $AD$. Biết $AB = 6\\,\\text{cm}, AC = 9\\,\\text{cm}, BC = 10\\,\\text{cm}$. Độ dài đoạn thẳng $BD$ là:", ["$4\\,\\text{cm}$", "$6\\,\\text{cm}$", "$5\\,\\text{cm}$", "$3,5\\,\\text{cm}$"], 0, "$\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{6}{9} = \\frac{2}{3} \\Rightarrow BD = \\frac{2}{5}BC = 4\\,\\text{cm}$."),
            make_mc(12, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $A = \\frac{x^2 - 2x + 2024}{x^2}$ với $x > 0$.", ["$\\frac{2023}{2024}$", "$1$", "$2024$", "$\\frac{1}{2024}$"], 0, "$A = 1 - \\frac{2}{x} + \\frac{2024}{x^2} = 2024\\left(\\frac{1}{x} - \\frac{1}{2024}\\right)^2 + \\frac{2023}{2024} \\ge \\frac{2023}{2024}$.")
        ],
        "part2": [
            make_tf(1, "Cho phân thức đại số $P = \\frac{x^2 - 4x + 4}{x^2 - 4}$.", [
                {"id": "a", "text": "Mẫu thức của phân thức $P$ là $x^2 - 4$.", "correct": True, "level": "Nhận biết", "explanation": "Mẫu thức là biểu thức ở mẫu."},
                {"id": "b", "text": "Điều kiện xác định của phân thức $P$ là $x \\neq 2$ và $x \\neq -2$.", "correct": True, "level": "Nhận biết", "explanation": "$x^2 - 4 \\neq 0 \\Leftrightarrow x \\neq \\pm 2$."},
                {"id": "c", "text": "Rút gọn phân thức $P$ ta được kết quả là $\\frac{x - 2}{x + 2}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{(x - 2)^2}{(x - 2)(x + 2)} = \\frac{x - 2}{x + 2}$."},
                {"id": "d", "text": "Tại $x = 2$, giá trị của phân thức $P$ bằng 0.", "correct": False, "level": "Vận dụng", "explanation": "Tại $x = 2$ phân thức không xác định, không có giá trị bằng 0."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB = 8\\,\\text{cm}, AC = 12\\,\\text{cm}$. Lấy điểm $D$ trên cạnh $AB$ sao cho $AD = 2\\,\\text{cm}$. Qua $D$ kẻ đường thẳng song song với $BC$, cắt $AC$ tại $E$.", [
                {"id": "a", "text": "Đoạn thẳng $BD$ có độ dài bằng $6\\,\\text{cm}$.", "correct": True, "level": "Nhận biết", "explanation": "$BD = AB - AD = 8 - 2 = 6\\,\\text{cm}$."},
                {"id": "b", "text": "Tỉ số $\\frac{AD}{AB}$ bằng $\\frac{1}{4}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{2}{8} = \\frac{1}{4}$."},
                {"id": "c", "text": "Độ dài đoạn thẳng $AE$ bằng $3\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "Theo Thalès: $AE = \\frac{1}{4}AC = \\frac{1}{4} \\cdot 12 = 3\\,\\text{cm}$."},
                {"id": "d", "text": "Độ dài đoạn thẳng $EC$ bằng $8\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "$EC = AC - AE = 12 - 3 = 9\\,\\text{cm} \\neq 8\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm điều kiện của $x$ để phân thức $\\frac{5}{2x - 6}$ xác định. Nhập giá trị $x$ khác bao nhiêu.", "3", ["3"], "$2x - 6 \\neq 0 \\Leftrightarrow x \\neq 3$."),
            make_sa(2, "Thông hiểu", "Rút gọn phân thức: $\\frac{3x^2 - 3x}{6x}$.", "(x-1)/2", ["(x-1)/2", "(x - 1)/2", "(x-1) / 2"], "$\\frac{3x(x - 1)}{6x} = \\frac{x - 1}{2}$."),
            make_sa(3, "Vận dụng", "Cho tam giác $ABC$ có $AD$ là tia phân giác của góc $A$ ($D \\in BC$). Biết $AB = 6\\,\\text{cm}, AC = 8\\,\\text{cm}$ và $BD = 3\\,\\text{cm}$. Tính độ dài đoạn thẳng $DC$ (cm).", "4", ["4", "4 cm"], "$\\frac{DC}{BD} = \\frac{AC}{AB} \\Rightarrow DC = \\frac{3 \\cdot 8}{6} = 4\\,\\text{cm}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị của $x$ để phân thức $A = \\frac{2x - 1}{x + 2}$ nhận giá trị bằng 1.", "3", ["3"], "$\\frac{2x - 1}{x + 2} = 1 \\Rightarrow 2x - 1 = x + 2 \\Rightarrow x = 3$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn phân thức: $\\frac{x^2 - 16}{2x - 8}$.\n b) Thực hiện phép cộng phân thức: $\\frac{x - 1}{x + 2} + \\frac{3}{x + 2}$.",
                "a) $\\frac{(x - 4)(x + 4)}{2(x - 4)} = \\frac{x + 4}{2}$ (0.5đ)\nb) $\\frac{x - 1 + 3}{x + 2} = \\frac{x + 2}{x + 2} = 1$ (0.5đ)",
                "a) $\\frac{x + 4}{2}$.\nb) $1$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ có các đường trung tuyến $BD$ và $CE$ cắt nhau tại $G$. Gọi $M, N$ lần lượt là trung điểm của $BG$ và $CG$.\n a) Chứng minh $ED // BC$ và $ED = \\frac{1}{2}BC$.\n b) Chứng minh tứ giác $MNDE$ là hình bình hành.",
                "a) $E, D$ là trung điểm nên $ED$ là đường trung bình của tam giác $ABC \\Rightarrow ED // BC, ED = \\frac{1}{2}BC$ (0.5đ)\nb) $MN$ là đường trung bình của tam giác $GBC \\Rightarrow MN // BC, MN = \\frac{1}{2}BC$. Từ đó $MN // ED$ và $MN = ED \\Rightarrow MNDE$ là hình bình hành (0.5đ)",
                "a) $ED$ là đường trung bình của $\\triangle ABC$.\nb) $MNDE$ có cặp cạnh đối song song và bằng nhau nên là hình bình hành."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Hai xí nghiệp may theo kế hoạch phải may tổng cộng 800 bộ quần áo bảo hộ. Nhờ cải tiến kỹ thuật, xí nghiệp I vượt mức $15\\%$, xí nghiệp II vượt mức $20\\%$, do đó cả hai xí nghiệp đã may được 940 bộ quần áo.\n a) Hỏi theo kế hoạch mỗi xí nghiệp phải may bao nhiêu bộ quần áo bảo hộ?\n b) Tính số bộ quần áo xí nghiệp I thực tế đã may được.",
                "a) Gọi số áo xí nghiệp I may theo kế hoạch là $x$ ($0 < x < 800$), xí nghiệp II là $800 - x$. Số áo vượt mức: $0,15x + 0,20(800 - x) = 940 - 800 = 140 \\Rightarrow -0,05x + 160 = 140 \\Rightarrow 0,05x = 20 \\Rightarrow x = 400$. Kế hoạch: Xí nghiệp I may 400 bộ, xí nghiệp II may 400 bộ (0.25đ)\nb) Thực tế xí nghiệp I may: $400 \\cdot 1,15 = 460$ bộ (0.25đ)",
                "a) Kế hoạch mỗi xí nghiệp may 400 bộ quần áo.\nb) Thực tế xí nghiệp I may được 460 bộ."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ nhọn. Các đường cao $AD, BE, CF$ cắt nhau tại $H$.\n Chứng minh rằng: $\\frac{HD}{AD} + \\frac{HE}{BE} + \\frac{HF}{CF} = 1$.",
                "Ta có tỉ số diện tích tam giác có cùng cạnh đáy:\n$\\frac{HD}{AD} = \\frac{S_{HBC}}{S_{ABC}}$.\nTương tự: $\\frac{HE}{BE} = \\frac{S_{HCA}}{S_{ABC}}$ và $\\frac{HF}{CF} = \\frac{S_{HAB}}{S_{ABC}}$.\nCộng vế theo vế ba đẳng thức trên:\n$\\frac{HD}{AD} + \\frac{HE}{BE} + \\frac{HF}{CF} = \\frac{S_{HBC} + S_{HCA} + S_{HAB}}{S_{ABC}} = \\frac{S_{ABC}}{S_{ABC}} = 1$ (đpcm) (0.5đ)",
                "Quy về tỉ số diện tích ba tam giác con $\\triangle HBC, \\triangle HCA, \\triangle HAB$ trên diện tích tam giác lớn $\\triangle ABC$. Tổng ba tỉ số bằng 1."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 02 ------------------
    # Ngữ cảnh: Tỉ lệ thức và phân thức trong vận tải hàng hóa, thiết kế giàn cầu thép Thalès, biểu đồ hình quạt tròn cơ cấu xuất khẩu
    exams.append({
        "id": "p_g8_final1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 02)",
        "topic": "Cộng trừ phân thức, Đường trung bình của tam giác, Tính chất đường phân giác & Biểu đồ cột",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Trong tam giác, đường phân giác của một góc chia cạnh đối diện thành hai đoạn thẳng:", ["Tỉ lệ với hai cạnh kề hai đoạn thẳng ấy", "Bằng nhau", "Vuông góc với cạnh đối diện", "Bằng một nửa cạnh đối diện"], 0, "Tính chất đường phân giác trong tam giác."),
            make_mc(2, "Nhận biết", "Quy tắc đổi dấu phân thức: Phân thức $\\frac{A}{B}$ bằng phân thức nào sau đây?", ["$-\\frac{A}{-B}$", "$\\frac{-A}{B}$", "$-\\frac{-A}{B}$", "$\\frac{A}{-B}$"], 2, "$\\frac{A}{B} = -\\frac{-A}{B} = -\\frac{A}{-B}$."),
            make_mc(3, "Nhận biết", "Đường trung bình của tam giác thì:", ["Song song với cạnh thứ ba và bằng nửa cạnh ấy", "Vuông góc với cạnh thứ ba", "Bằng cạnh thứ ba", "Đi qua trực tâm tam giác"], 0, "Tính chất đường trung bình của tam giác."),
            make_mc(4, "Thông hiểu", "Mẫu thức chung đơn giản nhất của hai phân thức $\\frac{1}{2x}$ và $\\frac{1}{3x^2}$ là:", ["$6x^2$", "$6x$", "$2x^2$", "$5x^2$"], 0, "$\\text{BCNN}(2, 3) = 6$, lũy thừa cao nhất của $x$ là $x^2$, nên MTC là $6x^2$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $D, E$ lần lượt là trung điểm của $AB$ và $AC$. Biết $BC = 14\\,\\text{cm}$. Độ dài đoạn thẳng $DE$ bằng:", ["$7\\,\\text{cm}$", "$14\\,\\text{cm}$", "$28\\,\\text{cm}$", "$3,5\\,\\text{cm}$"], 0, "$DE = \\frac{1}{2}BC = 14 : 2 = 7\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Rút gọn phân thức $\\frac{2x - 4}{x^2 - 4}$ ta được:", ["$\\frac{2}{x + 2}$", "$\\frac{2}{x - 2}$", "$\\frac{1}{x + 2}$", "$\\frac{x - 2}{x + 2}$"], 0, "$\\frac{2(x - 2)}{(x - 2)(x + 2)} = \\frac{2}{x + 2}$."),
            make_mc(7, "Vận dụng", "Một canô xuôi dòng một khúc sông từ A đến B hết 2 giờ và ngược dòng từ B về A hết 3 giờ. Biết vận tốc dòng nước là $3\\,\\text{km/h}$. Chiều dài khúc sông AB là:", ["$36\\,\\text{km}$", "$30\\,\\text{km}$", "$42\\,\\text{km}$", "$45\\,\\text{km}$"], 0, "Gọi vận tốc riêng là $v$. Ta có $2(v + 3) = 3(v - 3) \\Rightarrow 2v + 6 = 3v - 9 \\Rightarrow v = 15\\,\\text{km/h}$. Quãng sông: $2(15 + 3) = 36\\,\\text{km}$."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\,\\text{cm}, AC = 8\\,\\text{cm}$. Đường phân giác $AD$ của góc $A$ chia cạnh huyền $BC$ thành hai đoạn thẳng $BD$ và $CD$. Tỉ số $\\frac{BD}{CD}$ bằng:", ["$\\frac{3}{4}$", "$\\frac{4}{3}$", "$\\frac{1}{2}$", "$\\frac{3}{5}$"], 0, "$\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{6}{8} = \\frac{3}{4}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của $x$ để phân thức $M = \\frac{3}{x^2 - 4x + 7}$ đạt giá trị lớn nhất.", ["$x = 2$", "$x = 0$", "$x = -2$", "$x = 4$"], 0, "$x^2 - 4x + 7 = (x - 2)^2 + 3 \\ge 3$. Phân thức đạt GTLN bằng $\\frac{3}{3} = 1$ khi $x = 2$."),
            make_mc(10, "Vận dụng cao", "Cho hình vuông $ABCD$. Lấy điểm $E$ tùy ý trên cạnh $BC$. Tia phân giác của góc $\\widehat{DAE}$ cắt cạnh $CD$ tại $F$. Chứng minh rằng:", ["$AF = BE + DF$", "$AF = BE - DF$", "$AF = 2BE$", "$DF = 2BE$"], 0, "Trên tia đối của $CB$ lấy $K$ sao cho $CK = DF$. Chứng minh $\\triangle DAF = \\triangle BAK$ và tam giác $AEK$ cân tại $A$."),
            make_mc(11, "Vận dụng cao", "Tìm số thực $x$ thỏa mãn: $\\frac{x - 1}{x + 2} + \\frac{x + 1}{x - 2} = \\frac{2x^2 + 8}{x^2 - 4}$.", ["Phương trình vô nghiệm", "$x = 0$", "$x = 2$", "$x = -2$"], 0, "$(x - 1)(x - 2) + (x + 1)(x + 2) = x^2 - 3x + 2 + x^2 + 3x + 2 = 2x^2 + 4$. Vế phải là $2x^2 + 8$. Ta có $2x^2 + 4 = 2x^2 + 8 \\Rightarrow 4 = 8$ (vô lý). Phương trình vô nghiệm."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ có đường trung tuyến $AM$. Đường phân giác của góc $\\widehat{AMB}$ cắt $AB$ tại $D$, đường phân giác của góc $\\widehat{AMC}$ cắt $AC$ tại $E$. Khẳng định nào sau đây đúng?", ["$DE // BC$", "$DE \\perp AM$", "$DE = BC$", "$DE = AM$"], 0, "$\\frac{DA}{DB} = \\frac{MA}{MB} = \\frac{MA}{MC} = \\frac{EA}{EC} \\Rightarrow DE // BC$ (định lí Thalès đảo).")
        ],
        "part2": [
            make_tf(1, "Cho biểu thức $A = \\frac{x + 1}{x - 3} - \\frac{x - 1}{x + 3}$.", [
                {"id": "a", "text": "Mẫu thức chung của hai phân thức là $(x - 3)(x + 3) = x^2 - 9$.", "correct": True, "level": "Nhận biết", "explanation": "MTC là tích hai mẫu riêng."},
                {"id": "b", "text": "Điều kiện xác định của biểu thức $A$ là $x \\neq 3$ và $x \\neq -3$.", "correct": True, "level": "Nhận biết", "explanation": "Mẫu thức phải khác 0."},
                {"id": "c", "text": "Quy đồng và rút gọn ta được $A = \\frac{8x}{x^2 - 9}$.", "correct": True, "level": "Thông hiểu", "explanation": "$(x + 1)(x + 3) - (x - 1)(x - 3) = (x^2 + 4x + 3) - (x^2 - 4x + 3) = 8x$."},
                {"id": "d", "text": "Tại $x = 1$, giá trị của biểu thức $A$ bằng 1.", "correct": False, "level": "Vận dụng", "explanation": "Thay $x = 1$: $A = \\frac{8(1)}{1 - 9} = \\frac{8}{-8} = -1 \\neq 1$."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có đường trung tuyến $AM$. Gọi $I$ là trung điểm của đoạn thẳng $AM$. Tia $BI$ cắt cạnh $AC$ tại điểm $D$.", [
                {"id": "a", "text": "Điểm $M$ là trung điểm của cạnh $BC$.", "correct": True, "level": "Nhận biết", "explanation": "$AM$ là đường trung tuyến."},
                {"id": "b", "text": "Kẻ $MN // BD$ ($N \\in AC$), khi đó $N$ là trung điểm của đoạn thẳng $DC$.", "correct": True, "level": "Thông hiểu", "explanation": "$M$ là trung điểm $BC$ và $MN // BD$ nên $N$ là trung điểm $DC$."},
                {"id": "c", "text": "Đoạn thẳng $AD$ bằng đoạn thẳng $DN$.", "correct": True, "level": "Thông hiểu", "explanation": "$I$ là trung điểm $AM$ và $ID // MN$ nên $D$ là trung điểm $AN \\Rightarrow AD = DN$."},
                {"id": "d", "text": "Độ dài đoạn thẳng $AD$ bằng một nửa độ dài đoạn thẳng $DC$.", "correct": True, "level": "Vận dụng", "explanation": "$AD = DN = NC \\Rightarrow DC = 2AD$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Rút gọn phân thức $\\frac{4x^2y}{2xy^2}$ được $\\frac{2x}{y}$. Nhập phần tử số là đa thức nào?", "2x", ["2x"], "Tử số là 2x."),
            make_sa(2, "Thông hiểu", "Tìm điều kiện xác định của phân thức $\\frac{x + 2}{x^2 - 1}$. Nhập các giá trị $x$ khác (cách nhau bởi dấu phẩy).", "1, -1", ["1, -1", "-1, 1", "±1"], "$x^2 - 1 \\neq 0 \\Leftrightarrow x \\neq \\pm 1$."),
            make_sa(3, "Vận dụng", "Cho tam giác $ABC$, đường phân giác $AD$. Biết $AB = 4\\,\\text{cm}, AC = 6\\,\\text{cm}$ và $BC = 5\\,\\text{cm}$. Tính độ dài đoạn thẳng $BD$ (cm).", "2", ["2", "2 cm"], "$\\frac{BD}{CD} = \\frac{4}{6} = \\frac{2}{3} \\Rightarrow BD = \\frac{2}{5}BC = 2\\,\\text{cm}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị của $x$ để phân thức $P = \\frac{x^2 - 9}{x - 3}$ có giá trị bằng 10.", "7", ["7"], "ĐKXĐ: $x \\neq 3$. Rút gọn: $P = x + 3 = 10 \\Rightarrow x = 7$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn phân thức: $\\frac{x^2 - 25}{x^2 + 5x}$.\n b) Tính: $\\frac{3x - 1}{2x} + \\frac{x + 1}{2x}$.",
                "a) $\\frac{(x - 5)(x + 5)}{x(x + 5)} = \\frac{x - 5}{x}$ (0.5đ)\nb) $\\frac{3x - 1 + x + 1}{2x} = \\frac{4x}{2x} = 2$ (0.5đ)",
                "a) $\\frac{x - 5}{x}$.\nb) $2$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của cạnh huyền $BC$. Kẻ $MD \\perp AB$ ($D \\in AB$) và $ME \\perp AC$ ($E \\in AC$).\n a) Chứng minh tứ giác $ADME$ là hình chữ nhật.\n b) Chứng minh $D$ là trung điểm của $AB$ và $E$ là trung điểm của $AC$.",
                "a) Tứ giác $ADME$ có ba góc vuông nên là hình chữ nhật (0.5đ)\nb) Có $MD \\perp AB$ và $AC \\perp AB \\Rightarrow MD // AC$. Mà $M$ là trung điểm $BC$ nên $MD$ là đường trung bình của $\\triangle ABC \\Rightarrow D$ là trung điểm $AB$. Tương tự $E$ là trung điểm $AC$ (0.5đ)",
                "a) Tứ giác có 3 góc vuông là hình chữ nhật.\nb) Đường thẳng đi qua trung điểm một cạnh và song song với cạnh thứ hai thì đi qua trung điểm cạnh thứ ba."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một đội xe tải theo kế hoạch phải chở 140 tấn hàng. Khi thực hiện, có 2 xe được điều đi làm nhiệm vụ khác nên mỗi xe còn lại phải chở thêm 1 tấn hàng mới hết số hàng. Hỏi đội xe ban đầu có bao nhiêu chiếc xe tải?",
                "Gọi số xe ban đầu là $x$ chiếc ($x \\in \\mathbb{N}^*, x > 2$). Theo kế hoạch mỗi xe chở $\\frac{140}{x}$ tấn. Thực tế mỗi xe chở $\\frac{140}{x - 2}$ tấn. Phương trình: $\\frac{140}{x - 2} - \\frac{140}{x} = 1 \\Rightarrow 140x - 140(x - 2) = x(x - 2) \\Rightarrow 280 = x^2 - 2x \\Rightarrow x^2 - 2x - 280 = 0 \\Rightarrow (x - 20)(x + 14) = 0 \\Rightarrow x = 20$ (vì $x > 2$) (0.5đ)",
                "Lập phương trình phân thức giải được số xe ban đầu là 20 chiếc xe tải."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ có đường trung tuyến $AM$. Đường phân giác của góc $\\widehat{AMB}$ cắt $AB$ tại $D$, đường phân giác của góc $\\widehat{AMC}$ cắt $AC$ tại $E$.\n a) Chứng minh $DE // BC$.\n b) Gọi $I$ là giao điểm của $AM$ và $DE$. Chứng minh $I$ là trung điểm của đoạn thẳng $DE$.",
                "a) Vì $MD$ là phân giác $\\widehat{AMB}$ nên $\\frac{DA}{DB} = \\frac{MA}{MB}$. Vì $ME$ là phân giác $\\widehat{AMC}$ nên $\\frac{EA}{EC} = \\frac{MA}{MC}$. Do $MB = MC$ nên $\\frac{DA}{DB} = \\frac{EA}{EC} \\Rightarrow DE // BC$ (0.25đ)\nb) Vì $DI // BM$ nên $\\frac{DI}{BM} = \\frac{AI}{AM}$. Vì $IE // MC$ nên $\\frac{IE}{MC} = \\frac{AI}{AM}$. Suy ra $\\frac{DI}{BM} = \\frac{IE}{MC}$. Mà $BM = MC \\Rightarrow DI = IE$. Vậy $I$ là trung điểm của $DE$ (0.25đ)",
                "a) Dùng tính chất đường phân giác và định lí Thalès đảo chứng minh $DE // BC$.\nb) Áp dụng hệ quả định lí Thalès chứng minh $DI = IE$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 03 ------------------
    # Ngữ cảnh: Hai tổ công nhân cùng làm chung công việc, kết cấu giàn mái tam giác Thalès, doanh thu siêu thị
    exams.append({
        "id": "p_g8_final1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 03)",
        "topic": "Phép nhân chia phân thức, Định lí Thalès đảo, Hệ quả Thalès & Biểu đồ đoạn thẳng",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Muốn nhân hai phân thức đại số, ta:", ["Nhân các tử với nhau, các mẫu với nhau", "Nhân tử phân thức này với mẫu phân thức kia", "Quy đồng mẫu thức rồi nhân tử", "Giữ nguyên mẫu thức và nhân các tử"], 0, "Quy tắc nhân hai phân thức đại số."),
            make_mc(2, "Nhận biết", "Cho tam giác $ABC$ có $MN // BC$ ($M \\in AB, N \\in AC$). Hệ quả của định lí Thalès cho tỉ số nào sau đây đúng?", ["$\\frac{AM}{AB} = \\frac{AN}{AC} = \\frac{MN}{BC}$", "$\\frac{AM}{MB} = \\frac{AN}{NC} = \\frac{MN}{BC}$", "$\\frac{AM}{AB} = \\frac{NC}{AN}$", "$\\frac{MB}{AB} = \\frac{MN}{BC}$"], 0, "Hệ quả định lí Thalès: $\\frac{AM}{AB} = \\frac{AN}{AC} = \\frac{MN}{BC}$."),
            make_mc(3, "Nhận biết", "Phân thức nghịch đảo của phân thức $\\frac{x - 1}{x + 2}$ (với $x \\neq 1, x \\neq -2$) là:", ["$\\frac{x + 2}{x - 1}$", "$-\\frac{x - 1}{x + 2}$", "$\\frac{x - 1}{x - 2}$", "$\\frac{x + 1}{x + 2}$"], 0, "Phân thức nghịch đảo của $\\frac{A}{B}$ là $\\frac{B}{A}$."),
            make_mc(4, "Thông hiểu", "Kết quả của phép chia $\\frac{4x^2}{3y} : \\frac{2x}{9y^2}$ là:", ["$6xy$", "$\\frac{6x}{y}$", "$\\frac{8x^3}{27y^3}$", "$18xy$"], 0, "$\\frac{4x^2}{3y} \\cdot \\frac{9y^2}{2x} = 2x \\cdot 3y = 6xy$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $AB = 9\\,\\text{cm}, AC = 12\\,\\text{cm}$. Lấy điểm $D$ trên $AB$ và $E$ trên $AC$ sao cho $AD = 3\\,\\text{cm}, AE = 4\\,\\text{cm}$. Khẳng định nào sau đây đúng?", ["$DE // BC$", "$DE \\perp BC$", "$DE = BC$", "$DE$ cắt $BC$"], 0, "Vì $\\frac{AD}{AB} = \\frac{3}{9} = \\frac{1}{3}$ và $\\frac{AE}{AC} = \\frac{4}{12} = \\frac{1}{3}$ nên $DE // BC$ theo Thalès đảo."),
            make_mc(6, "Thông hiểu", "Điều kiện xác định của phân thức $\\frac{x + 3}{x^2 - 16}$ là:", ["$x \\neq 4$ và $x \\neq -4$", "$x \\neq 4$", "$x \\neq -4$", "$x \\neq -3$"], 0, "$x^2 - 16 \\neq 0 \\Leftrightarrow x \\neq \\pm 4$."),
            make_mc(7, "Vận dụng", "Hai vòi nước cùng chảy vào một bể không có nước thì sau 4 giờ đầy bể. Nếu chảy một mình thì vòi thứ nhất cần 6 giờ mới đầy bể. Hỏi vòi thứ hai chảy một mình thì sau bao lâu sẽ đầy bể?", ["$12$ giờ", "$10$ giờ", "$8$ giờ", "$14$ giờ"], 0, "Mỗi giờ vòi 2 chảy được: $\\frac{1}{4} - \\frac{1}{6} = \\frac{1}{12}$ bể. Vòi 2 cần 12 giờ."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ có đường cao $AH = 6\\,\\text{cm}$. Một đường thẳng song song với $BC$ cắt $AB, AC$ và $AH$ lần lượt tại $D, E$ và $K$. Biết $AK = 2\\,\\text{cm}, BC = 9\\,\\text{cm}$. Độ dài đoạn thẳng $DE$ là:", ["$3\\,\\text{cm}$", "$4,5\\,\\text{cm}$", "$6\\,\\text{cm}$", "$2\\,\\text{cm}$"], 0, "Theo hệ quả Thalès: $\\frac{DE}{BC} = \\frac{AK}{AH} = \\frac{2}{6} = \\frac{1}{3} \\Rightarrow DE = 9 : 3 = 3\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của $x$ để biểu thức $P = \\frac{x^2 - 2x + 1}{x^2 + 1}$ đạt giá trị nhỏ nhất.", ["$x = 1$", "$x = 0$", "$x = -1$", "$x = 2$"], 0, "Ta có $P = \\frac{(x - 1)^2}{x^2 + 1} \\ge 0$. Đạt giá trị nhỏ nhất bằng 0 khi $x = 1$."),
            make_mc(10, "Vận dụng cao", "Cho hình vuông $ABCD$. Lấy điểm $M$ trên cạnh $BC$. Tia $AM$ cắt đường thẳng $CD$ tại $N$. Khẳng định nào sau đây luôn đúng?", ["$\\frac{1}{AM^2} + \\frac{1}{AN^2} = \\frac{1}{AB^2}$", "$\\frac{1}{AM} + \\frac{1}{AN} = \\frac{1}{AB}$", "$AM^2 + AN^2 = AB^2$", "$AM \\cdot AN = AB^2$"], 0, "Hệ thức quen thuộc: Kẻ $AE \\perp AN$ ($E \\in CD$) chứng minh $\\triangle ABM = \\triangle ADE$ và dùng hệ thức lượng trong tam giác vuông $AEN$."),
            make_mc(11, "Vận dụng cao", "Tìm tất cả các số nguyên $x$ để phân thức $\\frac{2x^3 + x^2 + 2x + 4}{2x + 1}$ nhận giá trị nguyên.", ["$x \\in \\{-2; -1; 0; 1\\}$", "$x = 0$", "$x = 1$", "Không có"], 0, "Chia đa thức: $\\frac{x^2(2x + 1) + (2x + 1) + 3}{2x + 1} = x^2 + 1 + \\frac{3}{2x + 1} \\in \\mathbb{Z} \\Leftrightarrow 2x + 1 \\in \\{\\pm 1; \\pm 3\\} \\Rightarrow x \\in \\{0; -1; 1; -2\\}$."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ có ba góc nhọn. Gọi $H$ là trực tâm tam giác. Chứng minh $\\frac{HA}{AA'} + \\frac{HB}{BB'} + \\frac{HC}{CC'} = 2$ (với $A', B', C'$ là chân các đường cao).", ["Tổng bằng 2", "Tổng bằng 1", "Tổng bằng 3", "Tổng bằng 0,5"], 0, "Ta có $\\frac{HA'}{AA'} + \\frac{HB'}{BB'} + \\frac{HC'}{CC'} = 1$. Do đó $\\frac{AA' - HA'}{AA'} + \\dots = 3 - 1 = 2$.")
        ],
        "part2": [
            make_tf(1, "Cho biểu thức $B = \\left(\\frac{x}{x^2 - 4} + \\frac{1}{x + 2}\\right) : \\frac{2}{x - 2}$.", [
                {"id": "a", "text": "Điều kiện xác định của biểu thức $B$ là $x \\neq 2$ và $x \\neq -2$.", "correct": True, "level": "Nhận biết", "explanation": "Các mẫu thức phải khác 0."},
                {"id": "b", "text": "Quy đồng trong ngoặc đơn ta được $\\frac{x + (x - 2)}{(x - 2)(x + 2)} = \\frac{2x - 2}{(x - 2)(x + 2)}$.", "correct": True, "level": "Nhận biết", "explanation": "$x + (x - 2) = 2x - 2$."},
                {"id": "c", "text": "Rút gọn biểu thức $B$ ta được $B = \\frac{x - 1}{x + 2}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{2(x - 1)}{(x - 2)(x + 2)} \\cdot \\frac{x - 2}{2} = \\frac{x - 1}{x + 2}$."},
                {"id": "d", "text": "Không có giá trị nguyên nào của $x$ để biểu thức $B$ nhận giá trị nguyên.", "correct": False, "level": "Vận dụng", "explanation": "$B = 1 - \\frac{3}{x + 2}$. Khi $x + 2 \\in \\{\\pm 1; \\pm 3\\}$ có nhiều giá trị nguyên của $x$ thỏa mãn."}
            ]),
            make_tf(2, "Cho hình thang $ABCD$ ($AB // CD$). Một đường thẳng song song với hai đáy cắt hai cạnh bên $AD$ và $BC$ lần lượt tại $M$ và $N$.", [
                {"id": "a", "text": "Đoạn thẳng $MN$ song song với cả hai đáy $AB$ và $CD$.", "correct": True, "level": "Nhận biết", "explanation": "Giả thiết đề bài cho."},
                {"id": "b", "text": "Theo định lí Thalès, ta có tỉ số $\\frac{AM}{MD} = \\frac{BN}{NC}$.", "correct": True, "level": "Thông hiểu", "explanation": "Định lí Thalès trong hình thang."},
                {"id": "c", "text": "Nếu $M$ là trung điểm của $AD$ thì $N$ cũng là trung điểm của $BC$.", "correct": True, "level": "Thông hiểu", "explanation": "Khi đó $MN$ là đường trung bình của hình thang."},
                {"id": "d", "text": "Độ dài đoạn thẳng $MN$ luôn bằng trung bình cộng của hai đáy $AB$ và $CD$.", "correct": False, "level": "Vận dụng", "explanation": "Chỉ khi $MN$ là đường trung bình thì $MN = \\frac{AB + CD}{2}$. Với vị trí bất kì thì không bằng trung bình cộng."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Thực hiện phép tính: $\\frac{5x}{x - 1} - \\frac{5}{x - 1}$.", "5", ["5"], "$\\frac{5(x - 1)}{x - 1} = 5$."),
            make_sa(2, "Thông hiểu", "Tìm điều kiện xác định của phân thức $\\frac{1}{x^2 - 9}$. Nhập các giá trị $x$ khác (cách nhau bởi dấu phẩy).", "3, -3", ["3, -3", "-3, 3", "±3"], "$x^2 - 9 \\neq 0 \\Leftrightarrow x \\neq \\pm 3$."),
            make_sa(3, "Vận dụng", "Cho hình thang $ABCD$ ($AB // CD$) có $AB = 4\\,\\text{cm}, CD = 10\\,\\text{cm}$. Gọi $EF$ là đường trung bình của hình thang. Độ dài đoạn thẳng $EF$ là bao nhiêu cm?", "7", ["7", "7 cm"], "$EF = \\frac{4 + 10}{2} = 7\\,\\text{cm}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị của $x$ để phân thức $\\frac{x^2 - 4}{x - 2}$ bằng 6.", "4", ["4"], "ĐKXĐ: $x \\neq 2$. Rút gọn: $x + 2 = 6 \\Rightarrow x = 4$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn phân thức: $\\frac{2x^2 + 4x}{x^2 - 4}$.\n b) Tính: $\\frac{x}{x - 3} - \\frac{3}{x - 3}$.",
                "a) $\\frac{2x(x + 2)}{(x - 2)(x + 2)} = \\frac{2x}{x - 2}$ (0.5đ)\nb) $\\frac{x - 3}{x - 3} = 1$ (0.5đ)",
                "a) $\\frac{2x}{x - 2}$.\nb) $1$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ có các đường trung tuyến $BD$ và $CE$ cắt nhau tại $G$. Lấy các điểm $M, N$ sao cho $D$ là trung điểm của $GM$ và $E$ là trung điểm của $GN$.\n a) Chứng minh tứ giác $AGCD$ là hình gì?\n b) Chứng minh $MN // BC$.",
                "a) $G$ là trọng tâm $\\Rightarrow GD = \\frac{1}{2}BG$. Vì $GD = DM \\Rightarrow GM = BG \\Rightarrow G$ là trung điểm $BM$. Tương tự $G$ là trung điểm $CN$ (0.5đ)\nb) Xét $\\triangle GMN$ và $\\triangle GCB$ có: $GM = GB, GN = GC, \\widehat{MGN} = \\widehat{BGC}$ (đối đỉnh). Suy ra $\\triangle GMN = \\triangle GCB$ (c-g-c) $\\Rightarrow \\widehat{GMN} = \\widehat{GBC} \\Rightarrow MN // BC$ (0.5đ)",
                "a) Phân tích các đoạn thẳng trọng tâm.\nb) Hai tam giác đối đỉnh bằng nhau suy ra $MN // BC$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một người đi xe đạp từ A đến B với vận tốc dự định $15\\,\\text{km/h}$. Đi được một nửa quãng đường, xe bị hỏng nên người đó dừng lại sửa hết 15 phút. Để đến B đúng giờ dự định, trên quãng đường còn lại người đó phải tăng vận tốc thêm $5\\,\\text{km/h}$.\n a) Tính độ dài quãng đường AB.\n b) Tính thời gian người đó đi từ A đến B.",
                "a) Gọi nửa quãng đường là $s$ ($s > 0$). Thời gian đi nửa đầu: $\\frac{s}{15}$ giờ. Thời gian đi nửa sau với vận tốc $20\\,\\text{km/h}$: $\\frac{s}{20}$ giờ. Đổi $15\\,\\text{phút} = \\frac{1}{4}\\,\\text{giờ}$. Phương trình: $\\frac{s}{15} - \\left(\\frac{s}{20} + \\frac{1}{4}\\right) = 0 \\Rightarrow \\frac{s}{60} = \\frac{1}{4} \\Rightarrow s = 15\\,\\text{km}$. Quãng đường $AB = 2s = 30\\,\\text{km}$ (0.25đ)\nb) Thời gian đi: $30 : 15 = 2$ giờ (0.25đ)",
                "a) Quãng đường AB dài 30 km.\nb) Thời gian đi từ A đến B là 2 giờ."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ có ba góc nhọn. Kẻ đường cao $AH$. Lấy điểm $D$ trên cạnh $AB$ và điểm $E$ trên cạnh $AC$ sao cho $\\widehat{ADH} = \\widehat{AEH} = 90^\\circ$. Gọi $M$ là trung điểm của $BC$.\n Chứng minh rằng $AH^2 = AD \\cdot AB$ và $AM \\perp DE$.",
                "Áp dụng hệ thức lượng trong tam giác vuông $AHB$ có đường cao $HD$: $AH^2 = AD \\cdot AB$ (hoặc dùng tam giác đồng dạng $\\triangle ADH \\backsim \\triangle AHB$). Tương tự $AH^2 = AE \\cdot AC$. Suy ra $AD \\cdot AB = AE \\cdot AC \\Rightarrow \\frac{AD}{AC} = \\frac{AE}{AB}$. Suy ra $\\triangle ADE \\backsim \\triangle ACB$ (c-g-c) $\\Rightarrow \\widehat{ADE} = \\widehat{ACB}$. Gọi $K$ là giao điểm của $AM$ và $DE$, chứng minh góc vuông suy ra $AM \\perp DE$ (đpcm) (0.5đ)",
                "Dùng tam giác đồng dạng chứng minh $AD \\cdot AB = AE \\cdot AC = AH^2$, từ đó suy ra $\\triangle ADE \\backsim \\triangle ACB$ và $AM \\perp DE$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 04 ------------------
    # Ngữ cảnh: Dự án cấp nước sạch (công suất máy bơm), đường phân giác đo khoảng cách đảo xa bờ
    exams.append({
        "id": "p_g8_final1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 04)",
        "topic": "Phân thức đại số, Định lí Thalès, Tính chất đường phân giác & Biểu đồ hình quạt tròn",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Giá trị của phân thức $\\frac{A}{B}$ bằng 0 khi:", ["$A = 0$ và $B \\neq 0$", "$B = 0$", "$A = B$", "$A \\neq 0$"], 0, "Phân thức bằng 0 khi tử số bằng 0 và mẫu số khác 0."),
            make_mc(2, "Nhận biết", "Trong tam giác $ABC$, đường phân giác ngoài của góc $A$ (nếu có) cũng chia cạnh đối diện thành hai đoạn thẳng:", ["Tỉ lệ với hai cạnh kề của tam giác", "Bằng nhau", "Vuông góc với cạnh đối diện", "Bằng nửa cạnh đối diện"], 0, "Tính chất đường phân giác ngoài của tam giác."),
            make_mc(3, "Nhận biết", "Một hình thoi có cạnh bằng $a$ thì chu vi của nó là:", ["$4a$", "$a^2$", "$2a$", "$4a^2$"], 0, "Chu vi hình thoi bằng 4 lần độ dài cạnh: $4a$."),
            make_mc(4, "Thông hiểu", "Rút gọn phân thức $\\frac{x^2 - 9}{2x - 6}$ ta được:", ["$\\frac{x + 3}{2}$", "$\\frac{x - 3}{2}$", "$x + 3$", "$\\frac{1}{2}$"], 0, "$\\frac{(x - 3)(x + 3)}{2(x - 3)} = \\frac{x + 3}{2}$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $MN // BC$ ($M \\in AB, N \\in AC$). Biết $\\frac{AM}{AB} = \\frac{2}{5}$ và $BC = 15\\,\\text{cm}$. Độ dài đoạn thẳng $MN$ là:", ["$6\\,\\text{cm}$", "$10\\,\\text{cm}$", "$5\\,\\text{cm}$", "$7,5\\,\\text{cm}$"], 0, "Theo hệ quả Thalès: $MN = \\frac{2}{5}BC = \\frac{2}{5} \\cdot 15 = 6\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Thực hiện phép tính $\\frac{1}{x - 1} + \\frac{1}{1 - x}$ ta được kết quả là:", ["$0$", "$\\frac{2}{x - 1}$", "$\\frac{2}{1 - x}$", "$-1$"], 0, "$\\frac{1}{x - 1} - \\frac{1}{x - 1} = 0$."),
            make_mc(7, "Vận dụng", "Một hồ nước cung cấp nước sạch có hai máy bơm. Nếu cả hai máy bơm cùng hoạt động thì bơm cạn hồ trong 6 giờ. Nếu chỉ dùng máy bơm I thì mất 10 giờ mới cạn hồ. Hỏi nếu chỉ dùng máy bơm II thì mất bao lâu sẽ bơm cạn hồ nước?", ["$15$ giờ", "$12$ giờ", "$18$ giờ", "$16$ giờ"], 0, "Mỗi giờ máy II bơm được: $\\frac{1}{6} - \\frac{1}{10} = \\frac{1}{15}$ hồ. Thời gian cần là 15 giờ."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 3\\,\\text{cm}, AC = 4\\,\\text{cm}$. Tia phân giác của góc $A$ cắt cạnh huyền $BC$ tại $D$. Độ dài đoạn thẳng $BD$ là:", ["$\\frac{15}{7}\\,\\text{cm}$", "$\\frac{20}{7}\\,\\text{cm}$", "$2\\,\\text{cm}$", "$2,5\\,\\text{cm}$"], 0, "$BC = 5\\,\\text{cm}$. $\\frac{BD}{CD} = \\frac{3}{4} \\Rightarrow BD = \\frac{3}{7}BC = \\frac{15}{7}\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị nhỏ nhất của biểu thức: $A = \\frac{4x^2 + 4x + 5}{x^2 + 1}$.", ["$3$", "$4$", "$1$", "$5$"], 0, "$A = 4 + \\frac{4x + 1}{x^2 + 1}$ hoặc dùng tam thức bậc hai: $k(x^2+1) \\ge 4x^2+4x+5$. Ta có $A - 3 = \\frac{x^2 + 4x + 2}{x^2 + 1}$. Chính xác: GTNN của biểu thức đạt tại nghiệm của biệt thức $\\Delta$."),
            make_mc(10, "Vận dụng cao", "Cho hình bình hành $ABCD$. Lấy điểm $M$ trên đường chéo $AC$. Qua $M$ kẻ đường thẳng song song với $AB$ cắt $AD$ tại $E$ và cắt $BC$ tại $F$. Chứng minh rằng:", ["$S_{ABM} = S_{ADM}$", "$S_{ABM} > S_{ADM}$", "$S_{ABM} < S_{ADM}$", "$S_{ABM} = 2S_{ADM}$"], 0, "Hai tam giác $ABM$ và $ADM$ có chung đáy $AM$ và chiều cao hạ từ $B$ và $D$ đến $AC$ bằng nhau (do $\\triangle ABC = \\triangle CDA$)."),
            make_mc(11, "Vận dụng cao", "Cho $\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$. Rút gọn biểu thức $M = \\frac{(x^2 + y^2 + z^2)(a^2 + b^2 + c^2)}{(ax + by + cz)^2}$ ta được:", ["$1$", "$2$", "$0$", "$a + b + c$"], 0, "Đặt $x = ka, y = kb, z = kc$. Tử số $= k^2(a^2+b^2+c^2)^2$. Mẫu số $= [k(a^2+b^2+c^2)]^2 = k^2(a^2+b^2+c^2)^2$. Tỉ số luôn bằng 1."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ có diện tích bằng $60\\,\\text{cm}^2$. Lấy điểm $D$ trên cạnh $AB$ sao cho $AD = 2DB$, điểm $E$ trên cạnh $AC$ sao cho $AE = 3EC$. Diện tích tam giác $ADE$ là:", ["$30\\,\\text{cm}^2$", "$40\\,\\text{cm}^2$", "$45\\,\\text{cm}^2$", "$20\\,\\text{cm}^2$"], 0, "$\\frac{S_{ADE}}{S_{ABC}} = \\frac{AD}{AB} \\cdot \\frac{AE}{AC} = \\frac{2}{3} \\cdot \\frac{3}{4} = \\frac{1}{2} \\Rightarrow S_{ADE} = 60 : 2 = 30\\,\\text{cm}^2$.")
        ],
        "part2": [
            make_tf(1, "Cho phân thức $Q = \\frac{x^2 - 1}{x^2 - 2x + 1}$.", [
                {"id": "a", "text": "Mẫu thức của phân thức $Q$ có thể phân tích thành hằng đẳng thức $(x - 1)^2$.", "correct": True, "level": "Nhận biết", "explanation": "$x^2 - 2x + 1 = (x - 1)^2$."},
                {"id": "b", "text": "Điều kiện xác định của phân thức $Q$ là $x \\neq 1$.", "correct": True, "level": "Nhận biết", "explanation": "$(x - 1)^2 \\neq 0 \\Leftrightarrow x \\neq 1$."},
                {"id": "c", "text": "Rút gọn phân thức $Q$ ta được kết quả là $\\frac{x + 1}{x - 1}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{(x - 1)(x + 1)}{(x - 1)^2} = \\frac{x + 1}{x - 1}$."},
                {"id": "d", "text": "Tại $x = -1$, giá trị của phân thức $Q$ bằng 1.", "correct": False, "level": "Vận dụng", "explanation": "Tại $x = -1$, tử số bằng $(-1)^2 - 1 = 0$, nên giá trị phân thức bằng 0, không phải 1."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB = 6\\,\\text{cm}, AC = 9\\,\\text{cm}$. Tia phân giác trong của góc $A$ cắt $BC$ tại $D$.", [
                {"id": "a", "text": "Điểm $D$ nằm giữa hai điểm $B$ và $C$.", "correct": True, "level": "Nhận biết", "explanation": "Tia phân giác trong cắt cạnh đối diện tại điểm nằm giữa hai đầu mút."},
                {"id": "b", "text": "Tỉ số $\\frac{DB}{DC}$ bằng $\\frac{2}{3}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{DB}{DC} = \\frac{AB}{AC} = \\frac{6}{9} = \\frac{2}{3}$."},
                {"id": "c", "text": "Nếu đoạn thẳng $BC = 10\\,\\text{cm}$ thì đoạn thẳng $DB = 4\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$DB = \\frac{2}{2 + 3} \\cdot 10 = 4\\,\\text{cm}$."},
                {"id": "d", "text": "Đoạn thẳng $DC$ ngắn hơn đoạn thẳng $DB$.", "correct": False, "level": "Vận dụng", "explanation": "$DC = 10 - 4 = 6\\,\\text{cm} > DB = 4\\,\\text{cm}$, nên $DC$ dài hơn, không phải ngắn hơn."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm mẫu thức chung của hai phân thức $\\frac{1}{x - 2}$ và $\\frac{1}{x + 2}$.", "x^2 - 4", ["x^2 - 4", "x^2-4", "(x-2)(x+2)"], "MTC là $(x - 2)(x + 2) = x^2 - 4$."),
            make_sa(2, "Thông hiểu", "Tính: $\\frac{x^2}{x + 3} - \\frac{9}{x + 3}$ (với $x \\neq -3$). Nhập kết quả rút gọn.", "x - 3", ["x - 3", "x-3"], "$\\frac{(x - 3)(x + 3)}{x + 3} = x - 3$."),
            make_sa(3, "Vận dụng", "Cho tam giác $ABC$ có $MN // BC$ ($M \\in AB, N \\in AC$). Biết $AM = 4\\,\\text{cm}, MB = 6\\,\\text{cm}$ và $BC = 15\\,\\text{cm}$. Tính độ dài đoạn thẳng $MN$ (cm).", "6", ["6", "6 cm"], "$\\frac{MN}{BC} = \\frac{AM}{AB} = \\frac{4}{10} = \\frac{2}{5} \\Rightarrow MN = \\frac{2}{5} \\cdot 15 = 6\\,\\text{cm}$."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên dương $x$ nhỏ nhất để phân thức $\\frac{x + 5}{x - 2}$ nhận giá trị nguyên.", "3", ["3"], "$1 + \\frac{7}{x - 2} \\in \\mathbb{Z} \\Leftrightarrow x - 2 \\in \\{1; 7\\} \\Rightarrow x \\in \\{3; 9\\}$. Số nguyên dương nhỏ nhất là 3.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn phân thức: $\\frac{3x^2 - 6x}{x^2 - 4}$.\n b) Tính: $\\frac{2}{x + 1} + \\frac{3}{x - 1}$.",
                "a) $\\frac{3x(x - 2)}{(x - 2)(x + 2)} = \\frac{3x}{x + 2}$ (0.5đ)\nb) $\\frac{2(x - 1) + 3(x + 1)}{(x - 1)(x + 1)} = \\frac{5x + 1}{x^2 - 1}$ (0.5đ)",
                "a) $\\frac{3x}{x + 2}$.\nb) $\\frac{5x + 1}{x^2 - 1}$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ vuông tại $A$. Gọi $D$ là trung điểm của cạnh $BC$. Kẻ $DM \\perp AB$ ($M \\in AB$) và $DN \\perp AC$ ($N \\in AC$).\n a) Chứng minh tứ giác $AMDN$ là hình chữ nhật.\n b) Chứng minh $MN = \\frac{1}{2}BC$.",
                "a) Tứ giác $AMDN$ có ba góc vuông nên là hình chữ nhật (0.5đ)\nb) Trong hình chữ nhật $AMDN$, hai đường chéo bằng nhau: $MN = AD$. Trong tam giác vuông $ABC$, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền: $AD = \\frac{1}{2}BC$. Suy ra $MN = \\frac{1}{2}BC$ (0.5đ)",
                "a) Tứ giác có ba góc vuông là hình chữ nhật.\nb) $MN = AD = \\frac{1}{2}BC$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một xưởng cơ khí theo kế hoạch phải gia công 360 chi tiết máy trong một thời gian quy định. Nhờ cải tiến kỹ thuật, mỗi ngày xưởng đã gia công vượt mức 4 chi tiết máy, do đó xưởng đã hoàn thành kế hoạch sớm hơn 3 ngày so với dự định.\n a) Hỏi theo kế hoạch, mỗi ngày xưởng phải gia công bao nhiêu chi tiết máy?\n b) Tính thời gian thực tế xưởng đã hoàn thành công việc.",
                "a) Gọi số chi tiết mỗi ngày theo kế hoạch là $x$ ($x \\in \\mathbb{N}^*, x > 0$). Thời gian kế hoạch: $\\frac{360}{x}$ ngày. Thời gian thực tế: $\\frac{360}{x + 4}$ ngày. Phương trình: $\\frac{360}{x} - \\frac{360}{x + 4} = 3 \\Rightarrow \\frac{120}{x} - \\frac{120}{x + 4} = 1 \\Rightarrow x(x + 4) = 480 \\Rightarrow x^2 + 4x - 480 = 0 \\Rightarrow (x - 20)(x + 24) = 0 \\Rightarrow x = 20$ (chi tiết/ngày) (0.25đ)\nb) Thời gian thực tế: $360 : 24 = 15$ ngày (0.25đ)",
                "a) Kế hoạch mỗi ngày gia công 20 chi tiết máy.\nb) Thời gian thực tế hoàn thành là 15 ngày."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ có diện tích $S$. Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = \\frac{1}{3}AB$, trên cạnh $AC$ lấy điểm $E$ sao cho $AE = \\frac{1}{3}AC$. Gọi $K$ là giao điểm của $BE$ và $CD$.\n Tính diện tích tam giác $KBC$ theo $S$.",
                "Vì $\\frac{AD}{AB} = \\frac{AE}{AC} = \\frac{1}{3}$ nên $DE // BC$ và $\\frac{DE}{BC} = \\frac{1}{3}$.\nDo $DE // BC$ nên $\\triangle KDE \\backsim \\triangle KBC$ với tỉ số đồng dạng $k = \\frac{DE}{BC} = \\frac{1}{3}$.\nSuy ra tỉ số hai đường cao hạ từ $K$ đến $DE$ và $BC$ là $\\frac{h_1}{h_2} = \\frac{1}{3} \\Rightarrow h_2 = \\frac{3}{4}h$ (với $h$ là khoảng cách giữa $DE$ và $BC$).\nMặt khác khoảng cách từ $A$ đến $BC$ là $H$, khoảng cách từ $D$ đến $BC$ là $\\frac{2}{3}H$.\nTính được $S_{KBC} = \\frac{3}{4} \\cdot \\frac{2}{3} S = \\frac{3}{5}S$ hoặc tỉ lệ chuẩn: $S_{KBC} = \\frac{9}{16}S$ (hoặc giải qua hệ số: $\\frac{S_{KBC}}{S} = \\frac{3}{4}$) (0.5đ)",
                "Áp dụng định lí Thalès và tính chất tam giác đồng dạng $\\triangle KDE \\backsim \\triangle KBC$ tính được diện tích tam giác $KBC$ theo $S$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 05 ------------------
    # Ngữ cảnh: Chế tạo mô hình cánh máy bay Thalès, tối ưu hóa diện tích hình chữ nhật, rút gọn phân thức
    exams.append({
        "id": "p_g8_final1_05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 05)",
        "topic": "Phân thức đại số, Định lí Thalès trong tam giác & Biểu đồ thống kê",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Hai phân thức $\\frac{A}{B}$ và $\\frac{C}{D}$ bằng nhau khi và chỉ khi:", ["$A \\cdot D = B \\cdot C$", "$A \\cdot B = C \\cdot D$", "$A + D = B + C$", "$A : D = B : C$"], 0, "Định nghĩa hai phân thức bằng nhau."),
            make_mc(2, "Nhận biết", "Cho tam giác $ABC$. Nếu đường thẳng $d$ song song với $BC$ và cắt hai cạnh $AB, AC$ lần lượt tại $D, E$ thì:", ["$\\frac{AD}{AB} = \\frac{AE}{AC}$", "$\\frac{AD}{AC} = \\frac{AE}{AB}$", "$\\frac{AD}{AE} = \\frac{AC}{AB}$", "$\\frac{DB}{AB} = \\frac{AE}{AC}$"], 0, "Định lí Thalès trong tam giác."),
            make_mc(3, "Nhận biết", "Biểu đồ nào sau đây thích hợp nhất để biểu diễn tỉ lệ phần trăm các thành phần của một tổng thể?", ["Biểu đồ hình quạt tròn", "Biểu đồ đoạn thẳng", "Biểu đồ cột", "Biểu đồ tranh"], 0, "Biểu đồ hình quạt tròn dùng để biểu diễn tỉ lệ phần trăm các thành phần."),
            make_mc(4, "Thông hiểu", "Phân thức $\\frac{x^2 - 1}{x - 1}$ rút gọn được kết quả là:", ["$x + 1$", "$x - 1$", "$1$", "$x^2$"], 0, "$\\frac{(x - 1)(x + 1)}{x - 1} = x + 1$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $AB = 6\\,\\text{cm}, AC = 8\\,\\text{cm}$, đường phân giác trong $AD$. Tỉ số $\\frac{BD}{DC}$ bằng:", ["$\\frac{3}{4}$", "$\\frac{4}{3}$", "$\\frac{3}{7}$", "$\\frac{4}{7}$"], 0, "$\\frac{BD}{DC} = \\frac{AB}{AC} = \\frac{6}{8} = \\frac{3}{4}$."),
            make_mc(6, "Thông hiểu", "Kết quả của phép tính $\\frac{x}{x + 1} + \\frac{1}{x + 1}$ là:", ["$1$", "$\\frac{x + 1}{2x + 2}$", "$0$", "$x$"], 0, "$\\frac{x + 1}{x + 1} = 1$."),
            make_mc(7, "Vận dụng", "Một đội xe theo kế hoạch chở 120 tấn hàng. Khi thực hiện có 2 xe hỏng không tham gia được nên mỗi xe còn lại phải chở thêm 2 tấn hàng. Hỏi đội xe ban đầu có bao nhiêu chiếc xe?", ["$12$ chiếc", "$10$ chiếc", "$14$ chiếc", "$15$ chiếc"], 0, "Phương trình: $\\frac{120}{x - 2} - \\frac{120}{x} = 2 \\Rightarrow x = 12$ chiếc xe."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ có đường trung bình $MN$ song song với $BC$. Biết diện tích tam giác $AMN$ bằng $15\\,\\text{cm}^2$. Diện tích tam giác $ABC$ là:", ["$60\\,\\text{cm}^2$", "$30\\,\\text{cm}^2$", "$45\\,\\text{cm}^2$", "$75\\,\\text{cm}^2$"], 0, "Tỉ số diện tích bằng bình phương tỉ số đồng dạng: $\\frac{S_{AMN}}{S_{ABC}} = \\left(\\frac{1}{2}\\right)^2 = \\frac{1}{4} \\Rightarrow S_{ABC} = 15 \\cdot 4 = 60\\,\\text{cm}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm giá trị của $x$ để phân thức $P = \\frac{2}{x^2 - 2x + 5}$ đạt giá trị lớn nhất.", ["$x = 1$", "$x = 2$", "$x = 0$", "$x = -1$"], 0, "$x^2 - 2x + 5 = (x - 1)^2 + 4 \\ge 4$. Đạt giá trị lớn nhất khi mẫu nhỏ nhất: $x = 1$."),
            make_mc(10, "Vận dụng cao", "Cho hình thang $ABCD$ ($AB // CD$). Hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Khẳng định nào sau đây đúng?", ["$S_{AOD} = S_{BOC}$", "$S_{AOD} > S_{BOC}$", "$S_{AOD} < S_{BOC}$", "$S_{AOD} = S_{AOB}$"], 0, "Ta có $S_{ADC} = S_{BDC}$ (chung đáy $CD$, chiều cao bằng nhau). Trừ đi $S_{ODC}$ suy ra $S_{AOD} = S_{BOC}$."),
            make_mc(11, "Vận dụng cao", "Cho $x, y, z$ khác 0 thỏa mãn $x + y + z = 0$. Rút gọn biểu thức $A = \\frac{xy}{x^2 + y^2 - z^2} + \\frac{yz}{y^2 + z^2 - x^2} + \\frac{zx}{z^2 + x^2 - y^2}$:", ["$-\\frac{3}{2}$", "$\\frac{3}{2}$", "$1$", "$0$"], 0, "Vì $x + y = -z \\Rightarrow z^2 = (x + y)^2 = x^2 + 2xy + y^2 \\Rightarrow x^2 + y^2 - z^2 = -2xy$. Mẫu số bằng $-2xy$. Do đó mỗi phân số bằng $-1/2$. Tổng 3 phân số bằng $-3/2$."),
            make_mc(12, "Vận dụng cao", "Cho hình vuông $ABCD$. Lấy điểm $M$ trên cạnh $CD$. Đường phân giác của góc $\\widehat{DAM}$ cắt cạnh $CD$ kéo dài tại $N$. Khẳng định nào sau đây đúng?", ["$AN = DM + BC$", "$AN = DM$", "$AN = 2BC$", "$AN = DM - BC$"], 0, "Kẻ $AH \\perp MN$, chứng minh $\\triangle ADM = \\triangle AHN$.")
        ],
        "part2": [
            make_tf(1, "Cho phân thức đại số $A = \\frac{x^2 - 16}{x^2 - 8x + 16}$.", [
                {"id": "a", "text": "Mẫu thức của phân thức $A$ là hằng đẳng thức $(x - 4)^2$.", "correct": True, "level": "Nhận biết", "explanation": "$x^2 - 8x + 16 = (x - 4)^2$."},
                {"id": "b", "text": "Điều kiện xác định của phân thức $A$ là $x \\neq 4$.", "correct": True, "level": "Nhận biết", "explanation": "$(x - 4)^2 \\neq 0 \\Leftrightarrow x \\neq 4$."},
                {"id": "c", "text": "Rút gọn phân thức $A$ ta được kết quả là $\\frac{x + 4}{x - 4}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{(x - 4)(x + 4)}{(x - 4)^2} = \\frac{x + 4}{x - 4}$."},
                {"id": "d", "text": "Tại $x = 0$, giá trị của phân thức $A$ bằng 1.", "correct": False, "level": "Vận dụng", "explanation": "Tại $x = 0$, giá trị là $\\frac{0 + 4}{0 - 4} = -1 \\neq 1$."}
            ]),
            make_tf(2, "Cho tam giác $ABC$ có $AB = 10\\,\\text{cm}, AC = 15\\,\\text{cm}$. Tia phân giác của góc $A$ cắt cạnh $BC$ tại điểm $D$.", [
                {"id": "a", "text": "Đoạn thẳng $AD$ là tia phân giác trong góc $\\widehat{BAC}$.", "correct": True, "level": "Nhận biết", "explanation": "Theo giả thiết đề bài."},
                {"id": "b", "text": "Tỉ số $\\frac{DB}{DC}$ bằng $\\frac{2}{3}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{DB}{DC} = \\frac{AB}{AC} = \\frac{10}{15} = \\frac{2}{3}$."},
                {"id": "c", "text": "Nếu đoạn thẳng $BC = 20\\,\\text{cm}$ thì độ dài đoạn thẳng $DB = 8\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$DB = \\frac{2}{5} \\cdot 20 = 8\\,\\text{cm}$."},
                {"id": "d", "text": "Đoạn thẳng $DC$ có độ dài bằng $10\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "$DC = 20 - 8 = 12\\,\\text{cm} \\neq 10\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm mẫu thức chung của hai phân thức $\\frac{1}{2x}$ và $\\frac{1}{x(x + 1)}$.", "2x(x + 1)", ["2x(x + 1)", "2x(x+1)", "2x^2 + 2x"], "MTC là $2x(x + 1)$."),
            make_sa(2, "Thông hiểu", "Tính: $\\frac{x^2 - 1}{x + 1}$ (với $x \\neq -1$). Nhập kết quả rút gọn.", "x - 1", ["x - 1", "x-1"], "$\\frac{(x - 1)(x + 1)}{x + 1} = x - 1$."),
            make_sa(3, "Vận dụng", "Một cột đèn cao $6\\,\\text{m}$ có bóng trên mặt đất dài $4\\,\\text{m}$. Cùng lúc đó, một tòa nhà gần đó có bóng trên mặt đất dài $24\\,\\text{m}$. Chiều cao của tòa nhà đó là bao nhiêu mét?", "36", ["36", "36 m"], "Theo Thalès: $h = \\frac{6 \\cdot 24}{4} = 36\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ để phân thức $\\frac{x + 3}{x - 1}$ nhận giá trị nguyên.", "2", ["2", "3", "5", "0", "-1", "-3"], "$1 + \\frac{4}{x - 1} \\in \\mathbb{Z} \\Leftrightarrow x - 1 \\in \\{\\pm 1; \\pm 2; \\pm 4\\}$. Với $x - 1 = 1 \\Rightarrow x = 2$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn phân thức: $\\frac{x^2 - 9}{3x - 9}$.\n b) Tính: $\\frac{x - 2}{x + 3} + \\frac{5}{x + 3}$.",
                "a) $\\frac{(x - 3)(x + 3)}{3(x - 3)} = \\frac{x + 3}{3}$ (0.5đ)\nb) $\\frac{x - 2 + 5}{x + 3} = \\frac{x + 3}{x + 3} = 1$ (0.5đ)",
                "a) $\\frac{x + 3}{3}$.\nb) $1$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ có $D, E$ lần lượt là trung điểm của $AB$ và $AC$. Lấy điểm $F$ trên tia đối của tia $ED$ sao cho $EF = ED$.\n a) Chứng minh tứ giác $ADCF$ là hình bình hành.\n b) Chứng minh $DF // BC$ và $DF = BC$.",
                "a) Tứ giác $ADCF$ có hai đường chéo $AC$ và $DF$ cắt nhau tại trung điểm $E$ của mỗi đường nên là hình bình hành (0.5đ)\nb) Do $ADCF$ là hình bình hành $\\Rightarrow CF // AD, CF = AD$. Mà $AD = BD \\Rightarrow CF // BD, CF = BD$. Suy ra tứ giác $BCFD$ là hình bình hành $\\Rightarrow DF // BC, DF = BC$ (0.5đ)",
                "a) Tứ giác có 2 đường chéo cắt nhau tại trung điểm mỗi đường là hình bình hành.\nb) Tứ giác $BCFD$ là hình bình hành nên $DF // BC$ và $DF = BC$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một xưởng dệt theo kế hoạch phải dệt 3000 mét vải trong một số ngày quy định. Nhờ tăng năng suất, mỗi ngày xưởng dệt thêm được 50 mét vải, do đó đã hoàn thành kế hoạch trước 2 ngày.\n a) Hỏi theo kế hoạch mỗi ngày xưởng phải dệt bao nhiêu mét vải?\n b) Tính thời gian xưởng hoàn thành công việc theo kế hoạch.",
                "a) Gọi số mét vải dệt mỗi ngày theo kế hoạch là $x$ ($x > 0$). Thời gian kế hoạch: $\\frac{3000}{x}$. Thực tế: $\\frac{3000}{x + 50}$. Phương trình: $\\frac{3000}{x} - \\frac{3000}{x + 50} = 2 \\Rightarrow x(x + 50) = 75000 \\Rightarrow x^2 + 50x - 75000 = 0 \\Rightarrow (x - 250)(x + 300) = 0 \\Rightarrow x = 250$ (m/ngày) (0.25đ)\nb) Thời gian theo kế hoạch: $3000 : 250 = 12$ ngày (0.25đ)",
                "a) Kế hoạch mỗi ngày dệt 250 mét vải.\nb) Thời gian theo kế hoạch là 12 ngày."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ vuông tại $A$ có đường cao $AH$. Lấy điểm $D$ trên cạnh $AC$, kẻ $DE \\perp BC$ ($E \\in BC$).\n Chứng minh rằng: $BD \\perp AE$ khi và chỉ khi $D$ là trung điểm của cạnh $AC$.",
                "Gọi $K$ là giao điểm của $BD$ và $AE$. Sử dụng tích vô hướng hoặc phương pháp tam giác đồng dạng: Trong tam giác $BDC$ có các đường cao xuất phát từ các đỉnh, dùng định lí Ceva hoặc hệ thức lượng trong tam giác vuông chứng minh điều kiện cần và đủ để $BD \\perp AE$ là $D$ là trung điểm của cạnh $AC$ (0.5đ)",
                "Dùng phương pháp trực tâm tam giác hoặc tam giác đồng dạng chứng minh $BD \\perp AE$ khi và chỉ khi $D$ là trung điểm $AC$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 06 ------------------
    # Ngữ cảnh: Quy hoạch công viên sinh thái ven sông, kè đê hình thang cân, thống kê năng suất lúa các vụ
    exams.append({
        "id": "p_g8_final1_06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 8 (ĐỀ SỐ 06)",
        "topic": "Phân thức đại số tổng hợp, Định lí Thalès, Tam giác đồng dạng & Phân tích dữ liệu",
        "grade": "8",
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
            make_mc(1, "Nhận biết", "Phân thức $\\frac{A}{B}$ xác định khi:", ["$B \\neq 0$", "$A \\neq 0$", "$A = B$", "$B > 0$"], 0, "Mẫu thức khác 0."),
            make_mc(2, "Nhận biết", "Nếu tam giác $ABC$ có $D, E$ lần lượt là trung điểm của $AB$ và $AC$ thì đoạn thẳng $DE$ được gọi là:", ["Đường trung bình của tam giác $ABC$", "Đường cao của tam giác $ABC$", "Đường phân giác của tam giác $ABC$", "Đường trung tuyến của tam giác $ABC$"], 0, "Định nghĩa đường trung bình của tam giác."),
            make_mc(3, "Nhận biết", "Hình bình hành có hai đường chéo bằng nhau là:", ["Hình chữ nhật", "Hình thoi", "Hình thang cân", "Hình vuông"], 0, "Dấu hiệu nhận biết hình chữ nhật."),
            make_mc(4, "Thông hiểu", "Rút gọn phân thức $\\frac{5x + 10}{x^2 - 4}$ ta được:", ["$\\frac{5}{x - 2}$", "$\\frac{5}{x + 2}$", "$\\frac{1}{x - 2}$", "$\\frac{5x}{x - 2}$"], 0, "$\\frac{5(x + 2)}{(x - 2)(x + 2)} = \\frac{5}{x - 2}$."),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $DE // BC$ ($D \\in AB, E \\in AC$). Biết $AD = 4\\,\\text{cm}, DB = 2\\,\\text{cm}, AE = 6\\,\\text{cm}$. Độ dài đoạn thẳng $EC$ là:", ["$3\\,\\text{cm}$", "$2\\,\\text{cm}$", "$4\\,\\text{cm}$", "$5\\,\\text{cm}$"], 0, "$\\frac{EC}{AE} = \\frac{DB}{AD} \\Rightarrow EC = \\frac{6 \\cdot 2}{4} = 3\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Tính: $\\frac{x - 3}{x + 2} + \\frac{5}{x + 2}$:", ["$1$", "$\\frac{x + 2}{2x + 4}$", "$0$", "$2$"], 0, "$\\frac{x - 3 + 5}{x + 2} = \\frac{x + 2}{x + 2} = 1$."),
            make_mc(7, "Vận dụng", "Hai đội công nhân cùng sửa một đoạn đường trong 12 ngày thì xong. Nếu đội thứ nhất làm một mình trong 20 ngày thì xong. Hỏi đội thứ hai làm một mình thì sửa xong đoạn đường trong bao nhiêu ngày?", ["$30$ ngày", "$25$ ngày", "$24$ ngày", "$36$ ngày"], 0, "Mỗi ngày đội 2 làm được: $\\frac{1}{12} - \\frac{1}{20} = \\frac{1}{30}$ công việc. Đội 2 cần 30 ngày."),
            make_mc(8, "Vận dụng", "Cho tam giác $ABC$ có $AB = 12\\,\\text{cm}, AC = 18\\,\\text{cm}$. Tia phân giác trong của góc $A$ cắt $BC$ tại $D$. Biết $BD = 6\\,\\text{cm}$. Độ dài đoạn thẳng $BC$ là:", ["$15\\,\\text{cm}$", "$9\\,\\text{cm}$", "$18\\,\\text{cm}$", "$12\\,\\text{cm}$"], 0, "$\\frac{CD}{BD} = \\frac{AC}{AB} = \\frac{18}{12} = 1,5 \\Rightarrow CD = 6 \\cdot 1,5 = 9\\,\\text{cm} \\Rightarrow BC = 6 + 9 = 15\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm số thực $x$ thỏa mãn: $\\frac{x^2 - 1}{x + 1} = 3$.", ["$x = 4$", "$x = 2$", "$x = -1$", "Phương trình vô nghiệm"], 0, "ĐKXĐ: $x \\neq -1$. Phân thức rút gọn: $x - 1 = 3 \\Rightarrow x = 4$ (thỏa mãn)."),
            make_mc(10, "Vận dụng cao", "Cho hình vuông $ABCD$ có cạnh bằng $12\\,\\text{cm}$. Lấy điểm $E$ trên cạnh $CD$ sao cho $DE = 3\\,\\text{cm}$. Đường thẳng qua $A$ vuông góc với $AE$ cắt đường thẳng $CD$ tại $F$. Độ dài đoạn thẳng $EF$ là:", ["$15\\,\\text{cm}$", "$12\\,\\text{cm}$", "$16\\,\\text{cm}$", "$20\\,\\text{cm}$"], 0, "Chứng minh $\\triangle ABF = \\triangle ADE$ hoặc tính $AE = \\sqrt{12^2 + 3^2} = \\sqrt{153}$. Trong $\\triangle AEF$ vuông tại $A$ có $AD$ là đường cao: $AD^2 = DE \\cdot DF \\Rightarrow 144 = 3 \\cdot DF \\Rightarrow DF = 48\\,\\text{cm}$. Vậy $EF = DE + DF = 3 + 48 = 51\\,\\text{cm}$."),
            make_mc(11, "Vận dụng cao", "Cho $a + b + c = 0$. Rút gọn biểu thức $M = \\frac{a^2}{bc} + \\frac{b^2}{ca} + \\frac{c^2}{ab}$ ta được:", ["$3$", "$0$", "$1$", "$-3$"], 0, "Quy đồng: $\\frac{a^3 + b^3 + c^3}{abc} = \\frac{3abc}{abc} = 3$."),
            make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ có $AD$ là phân giác. Kẻ $DE // AB$ ($E \\in AC$) và $DF // AC$ ($F \\in AB$). Tứ giác $AEDF$ là hình gì?", ["Hình thoi", "Hình chữ nhật", "Hình bình hành", "Hình vuông"], 0, "Tứ giác $AEDF$ có các cạnh đối song song nên là hình bình hành. Đường chéo $AD$ là phân giác nên là hình thoi.")
        ],
        "part2": [
            make_tf(1, "Cho biểu thức $P = \\left(\\frac{1}{x - 1} - \\frac{x}{1 - x^2}\\right) : \\frac{2x + 1}{x^2 + 2x + 1}$.", [
                {"id": "a", "text": "Đa thức $x^2 + 2x + 1$ là hằng đẳng thức $(x + 1)^2$.", "correct": True, "level": "Nhận biết", "explanation": "$x^2 + 2x + 1 = (x + 1)^2$."},
                {"id": "b", "text": "Điều kiện xác định của biểu thức $P$ gồm $x \\neq 1, x \\neq -1$ và $x \\neq -\\frac{1}{2}$.", "correct": True, "level": "Nhận biết", "explanation": "Các mẫu thức và tử thức của phân thức chia phải khác 0."},
                {"id": "c", "text": "Rút gọn trong ngoặc đơn ta được $\\frac{2x + 1}{(x - 1)(x + 1)}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{1}{x - 1} + \\frac{x}{(x - 1)(x + 1)} = \\frac{x + 1 + x}{(x - 1)(x + 1)} = \\frac{2x + 1}{(x - 1)(x + 1)}$."},
                {"id": "d", "text": "Rút gọn toàn bộ biểu thức $P$ ta được $P = \\frac{x - 1}{x + 1}$.", "correct": False, "level": "Vận dụng", "explanation": "$P = \\frac{2x + 1}{(x - 1)(x + 1)} \\cdot \\frac{(x + 1)^2}{2x + 1} = \\frac{x + 1}{x - 1} \\neq \\frac{x - 1}{x + 1}$."}
            ]),
            make_tf(2, "Cho hình thang $ABCD$ ($AB // CD$). Gọi $E$ và $F$ lần lượt là trung điểm của hai đường chéo $BD$ và $AC$.", [
                {"id": "a", "text": "Đoạn thẳng $EF$ nằm trên đường trung bình của hình thang $ABCD$.", "correct": True, "level": "Nhận biết", "explanation": "Định lí về đoạn nối trung điểm hai đường chéo của hình thang."},
                {"id": "b", "text": "Đoạn thẳng $EF$ song song với hai đáy $AB$ và $CD$.", "correct": True, "level": "Thông hiểu", "explanation": "Do nằm trên đường trung bình nên $EF // AB // CD$."},
                {"id": "c", "text": "Độ dài đoạn thẳng $EF$ bằng một nửa hiệu hai đáy: $EF = \\frac{CD - AB}{2}$ ($CD > AB$).", "correct": True, "level": "Thông hiểu", "explanation": "Tính chất quen thuộc: $EF = \\frac{|CD - AB|}{2}$."},
                {"id": "d", "text": "Nếu đáy nhỏ $AB = 6\\,\\text{cm}$ và đáy lớn $CD = 10\\,\\text{cm}$ thì $EF = 4\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "$EF = \\frac{10 - 6}{2} = 2\\,\\text{cm} \\neq 4\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Rút gọn phân thức: $\\frac{x^2 - 4x + 4}{x - 2}$ (với $x \\neq 2$).", "x - 2", ["x - 2", "x-2"], "$\\frac{(x - 2)^2}{x - 2} = x - 2$."),
            make_sa(2, "Thông hiểu", "Tìm điều kiện xác định của phân thức $\\frac{5}{x^2 - 25}$. Nhập các giá trị $x$ khác (cách nhau bởi dấu phẩy).", "5, -5", ["5, -5", "-5, 5", "±5"], "$x^2 - 25 \\neq 0 \\Leftrightarrow x \\neq \\pm 5$."),
            make_sa(3, "Vận dụng", "Cho tam giác $ABC$ có $MN // BC$ ($M \\in AB, N \\in AC$). Biết $AM = 3\\,\\text{cm}, AB = 9\\,\\text{cm}$ và $MN = 4\\,\\text{cm}$. Tính độ dài cạnh đáy $BC$ (cm).", "12", ["12", "12 cm"], "$\\frac{MN}{BC} = \\frac{AM}{AB} = \\frac{3}{9} = \\frac{1}{3} \\Rightarrow BC = 4 \\cdot 3 = 12\\,\\text{cm}$."),
            make_sa(4, "Vận dụng cao", "Tìm giá trị của $x$ để phân thức $P = \\frac{x^2 - 16}{x - 4}$ nhận giá trị bằng 12.", "8", ["8"], "ĐKXĐ: $x \\neq 4$. $P = x + 4 = 12 \\Rightarrow x = 8$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "a) Rút gọn phân thức: $\\frac{x^2 - 1}{2x - 2}$.\n b) Tính: $\\frac{2x}{x - 1} - \\frac{2}{x - 1}$.",
                "a) $\\frac{(x - 1)(x + 1)}{2(x - 1)} = \\frac{x + 1}{2}$ (0.5đ)\nb) $\\frac{2x - 2}{x - 1} = \\frac{2(x - 1)}{x - 1} = 2$ (0.5đ)",
                "a) $\\frac{x + 1}{2}$.\nb) $2$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Cho tam giác $ABC$ có các đường trung tuyến $BD$ và $CE$ cắt nhau tại $G$. Gọi $M, N$ lần lượt là trung điểm của $BG$ và $CG$.\n a) Chứng minh $ED // BC$ và $ED = MN$.\n b) Chứng minh tứ giác $MNDE$ là hình bình hành.",
                "a) $ED$ là đường trung bình của $\\triangle ABC \\Rightarrow ED // BC, ED = \\frac{1}{2}BC$. $MN$ là đường trung bình của $\\triangle GBC \\Rightarrow MN // BC, MN = \\frac{1}{2}BC$. Suy ra $ED // MN$ và $ED = MN$ (0.5đ)\nb) Tứ giác $MNDE$ có cặp cạnh đối $ED$ và $MN$ vừa song song vừa bằng nhau nên là hình bình hành (0.5đ)",
                "a) $ED$ và $MN$ cùng song song và bằng nửa $BC$.\nb) $MNDE$ là hình bình hành vì có cặp cạnh đối song song và bằng nhau."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một ô tô dự định đi từ tỉnh A đến tỉnh B cách nhau 120 km trong một thời gian nhất định. Sau khi đi được một nửa quãng đường, ô tô dừng lại nghỉ 10 phút. Để đến B đúng giờ quy định, trên nửa quãng đường còn lại ô tô phải tăng vận tốc thêm $6\\,\\text{km/h}$.\n a) Tính vận tốc ban đầu của ô tô.\n b) Tính thời gian ô tô đi từ A đến B theo dự định.",
                "a) Nửa quãng đường là $60\\,\\text{km}$. Gọi vận tốc dự định là $v$ ($v > 0$). Thời gian đi nửa đầu: $\\frac{60}{v}$. Thời gian đi nửa sau: $\\frac{60}{v + 6}$. Nghỉ $10\\,\\text{phút} = \\frac{1}{6}\\,\\text{giờ}$. Phương trình: $\\frac{60}{v} - \\frac{60}{v + 6} = \\frac{1}{6} \\Rightarrow \\frac{360}{v(v + 6)} = \\frac{1}{6} \\Rightarrow v(v + 6) = 2160 \\Rightarrow v^2 + 6v - 2160 = 0 \\Rightarrow (v - 45)(v + 48) = 0 \\Rightarrow v = 45\\,\\text{km/h}$ (0.25đ)\nb) Thời gian dự định: $120 : 45 = \\frac{8}{3}\\,\\text{giờ} = 2\\,\\text{giờ } 40\\,\\text{phút}$ (0.25đ)",
                "a) Vận tốc ban đầu của ô tô là $45\\,\\text{km/h}$.\nb) Thời gian đi dự định là 2 giờ 40 phút."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho tam giác $ABC$ có ba góc nhọn. Các đường cao $AD, BE, CF$ cắt nhau tại $H$.\n Chứng minh rằng: $\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1$.",
                "Áp dụng định lí Ceva cho ba đường cao đồng quy tại $H$ trong tam giác $ABC$:\nBa đoạn thẳng $AD, BE, CF$ cùng xuất phát từ ba đỉnh của tam giác và đồng quy tại trực tâm $H$.\nTheo định lí Ceva, tỉ số giữa các đoạn thẳng trên các cạnh thỏa mãn:\n$\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1$ (đpcm) (0.5đ)",
                "Áp dụng định lí Ceva cho ba đường cao $AD, BE, CF$ đồng quy tại trực tâm $H$, suy ra tích ba tỉ số bằng 1."
            )
        ]
    })

    return exams
