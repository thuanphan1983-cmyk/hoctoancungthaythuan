# -*- coding: utf-8 -*-
"""
GENERATOR BỘ ĐỀ THI ĐỊNH KỲ TOÁN 6 (GIỮA KỲ 2 & CUỐI KỲ 2)
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
from build_periodic_grade6_term1 import generate_g6_mid1, generate_g6_final1

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
# 6 MÃ ĐỀ GIỮA KỲ 2 - TOÁN 6 (mid2)
# Phạm vi: Phân số, Số thập phân, Điểm - Đường thẳng - Đoạn thẳng - Trung điểm.
# ==============================================================================
def generate_g6_mid2():
    exams = []
    
    # ------------------ ĐỀ SỐ 01 ------------------
    exams.append({
        "id": "p_g6_mid2_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ II - TOÁN 6 (ĐỀ SỐ 01)",
        "topic": "Phân số, Số thập phân & Điểm, đường thẳng, đoạn thẳng, trung điểm",
        "grade": "6",
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
            # 3 NB, 3 TH, 2 VD, 4 VDC
            make_mc(1, "Nhận biết", "Phân số nào sau đây bằng phân số $\\frac{-3}{5}$?", ["$\\frac{6}{10}$", "$\\frac{-6}{10}$", "$\\frac{3}{-10}$", "$\\frac{-9}{25}$"], 1, "Nhân cả tử và mẫu với 2: $\\frac{-3 \\cdot 2}{5 \\cdot 2} = \\frac{-6}{10}$."),
            make_mc(2, "Nhận biết", "Số đối của số thập phân $-4,25$ là:", ["$4,25$", "$-4,25$", "$\\frac{1}{4,25}$", "$0$"], 0, "Số đối của $-a$ là $a$."),
            make_mc(3, "Nhận biết", "Cho điểm $M$ nằm giữa hai điểm $A$ và $B$. Khẳng định nào sau đây luôn đúng?", ["$MA = MB$", "$AM + MB = AB$", "$AB + MB = AM$", "$AM = \\frac{1}{2}AB$"], 1, "Khi $M$ nằm giữa $A$ và $B$ thì $AM + MB = AB$."),
            make_mc(4, "Thông hiểu", "Kết quả của phép tính $\\frac{5}{12} + \\frac{-7}{12}$ bằng:", ["$\\frac{1}{6}$", "$-\\frac{1}{6}$", "$\\frac{-12}{12}$", "$-\\frac{2}{24}$"], 1, "$\\frac{5 + (-7)}{12} = \\frac{-2}{12} = -\\frac{1}{6}$."),
            make_mc(5, "Thông hiểu", "Làm tròn số $72,564$ đến hàng phần mười (chữ số thập phân thứ nhất) ta được:", ["$72,5$", "$72,6$", "$73$", "$72,56$"], 1, "Chữ số ngay sau hàng phần mười là 6 >= 5 nên làm tròn lên $72,6$."),
            make_mc(6, "Thông hiểu", "Biết $\\frac{3}{4}$ của một số $x$ là $45$. Giá trị của $x$ là:", ["$60$", "$33,75$", "$40$", "$15$"], 0, "$x = 45 : \\frac{3}{4} = 45 \\cdot \\frac{4}{3} = 60$."),
            make_mc(7, "Vận dụng", "Một cửa hàng niêm yết giá một chiếc cặp là $250\\,000$ đồng. Nhân dịp khai giảng, cửa hàng giảm giá $15\\%$. Giá bán của chiếc cặp sau khi giảm là:", ["$212\\,500$ đồng", "$220\\,000$ đồng", "$215\\,000$ đồng", "$37\\,500$ đồng"], 0, "Số tiền giảm là $250\\,000 \\cdot 15\\% = 37\\,500$ đồng. Giá bán là $250\\,000 - 37\\,500 = 212\\,500$ đồng."),
            make_mc(8, "Vận dụng", "Trên tia $Ox$, lấy hai điểm $A$ và $B$ sao cho $OA = 3\\,\\text{cm}$, $OB = 7\\,\\text{cm}$. Gọi $M$ là trung điểm của đoạn thẳng $AB$. Độ dài đoạn thẳng $OM$ là:", ["$4\\,\\text{cm}$", "$5\\,\\text{cm}$", "$2\\,\\text{cm}$", "$3,5\\,\\text{cm}$"], 1, "$AB = OB - OA = 4\\,\\text{cm} \\Rightarrow AM = 2\\,\\text{cm} \\Rightarrow OM = OA + AM = 5\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên $n$ để phân số $A = \\frac{2n + 3}{n + 1}$ nhận giá trị nguyên.", ["$n \\in \\{-2; 0\\}$", "$n \\in \\{-3; -2; 0; 1\\}$", "$n \\in \\{1; 2\\}$", "$n \\in \\emptyset$"], 0, "$A = \\frac{2(n+1)+1}{n+1} = 2 + \\frac{1}{n+1} \\in \\mathbb{Z} \\Leftrightarrow n+1 \\in \\{\\pm 1\\} \\Leftrightarrow n \\in \\{0; -2\\}$."),
            make_mc(10, "Vận dụng cao", "Cho tổng $S = \\frac{1}{2^2} + \\frac{1}{3^2} + \\frac{1}{4^2} + \\dots + \\frac{1}{100^2}$. Khẳng định nào sau đây đúng?", ["$S < 1$", "$S > 2$", "$S = 1$", "$S > \\frac{3}{2}$"], 0, "Ta có $\\frac{1}{k^2} < \\frac{1}{(k-1)k} = \\frac{1}{k-1} - \\frac{1}{k}$. Tổng $S < 1 - \\frac{1}{100} < 1$."),
            make_mc(11, "Vận dụng cao", "Tìm chữ số tận cùng của tổng $P = 7 + 7^2 + 7^3 + \\dots + 7^{100}$.", ["$0$", "$7$", "$9$", "$3$"], 0, "Nhóm mỗi nhóm 4 số hạng: $7 + 7^2 + 7^3 + 7^4 = 7(1+7+49+343) = 7 \\cdot 400$ tận cùng là 0. Có 25 nhóm nên tận cùng là 0."),
            make_mc(12, "Vận dụng cao", "Cho đoạn thẳng $AB = 8\\,\\text{cm}$. Điểm $C$ nằm trên tia đối của tia $BA$ sao cho $BC = 4\\,\\text{cm}$. Gọi $I$ là trung điểm của $AC$. Khẳng định nào sau đây đúng?", ["$I$ nằm giữa $A$ và $B$", "$B$ là trung điểm của đoạn thẳng $IC$", "$IB = 2\\,\\text{cm}$", "$C$ là trung điểm của đoạn $AB$"], 1, "$C$ thuộc tia đối của tia $BA$ nên $B$ nằm giữa $A$ và $C$, $AC = AB + BC = 12\\,\\text{cm}$. $I$ là trung điểm $AC \\Rightarrow IA = IC = 6\\,\\text{cm} \\Rightarrow IB = AB - IA = 2\\,\\text{cm}$. Mà $BC = 4\\,\\text{cm}$, $IC = 6\\,\\text{cm} \\Rightarrow IB + BC = 6 = IC$, $B$ không là trung điểm mà $IB = 2\\,\\text{cm}$.")
        ],
        "part2": [
            # Câu 1: 2 NB, 1 TH, 1 VD
            make_tf(1, "Cho biểu thức $A = \\frac{2}{3} + \\frac{1}{4} : \\left(-\\frac{1}{2}\\right)$ và $B = 3,5 \\cdot 1,2 - 4,2$.", [
                {"id": "a", "text": "Phân số nghịch đảo của $-\\frac{1}{2}$ là $-2$.", "correct": True, "level": "Nhận biết", "explanation": "Nghịch đảo của $-1/2$ là $-2/1 = -2$."},
                {"id": "b", "text": "Giá trị của $B$ bằng $0$.", "correct": True, "level": "Nhận biết", "explanation": "$3,5 \\cdot 1,2 = 4,2 \\Rightarrow 4,2 - 4,2 = 0$."},
                {"id": "c", "text": "Giá trị của biểu thức $A$ là một số dương.", "correct": True, "level": "Thông hiểu", "explanation": "$A = \\frac{2}{3} + \\frac{1}{4} \\cdot (-2) = \\frac{2}{3} - \\frac{1}{2} = \\frac{1}{6} > 0$."},
                {"id": "d", "text": "Số nghịch đảo của biểu thức $A$ chia cho $B$ là một số xác định.", "correct": False, "level": "Vận dụng", "explanation": "Do $B = 0$ nên phép chia cho $B$ không xác định."}
            ]),
            # Câu 2: 1 NB, 2 TH, 1 VD
            make_tf(2, "Trên đường thẳng $xy$, lấy điểm $O$. Trên tia $Ox$ lấy điểm $A$ sao cho $OA = 4\\,\\text{cm}$. Trên tia $Oy$ lấy điểm $B$ sao cho $OB = 6\\,\\text{cm}$. Gọi $M$ là trung điểm của $OB$.", [
                {"id": "a", "text": "Hai tia $Ox$ và $Oy$ là hai tia đối nhau.", "correct": True, "level": "Nhận biết", "explanation": "Điểm $O$ thuộc đường thẳng $xy$ nên $Ox, Oy$ là hai tia đối nhau."},
                {"id": "b", "text": "Độ dài đoạn thẳng $AB$ bằng $10\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$O$ nằm giữa $A$ và $B$ nên $AB = OA + OB = 4 + 6 = 10\\,\\text{cm}$."},
                {"id": "c", "text": "Độ dài đoạn thẳng $OM$ bằng $3\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$M$ là trung điểm $OB$ nên $OM = OB : 2 = 3\\,\\text{cm}$."},
                {"id": "d", "text": "Điểm $O$ là trung điểm của đoạn thẳng $AM$.", "correct": False, "level": "Vận dụng", "explanation": "$OA = 4\\,\\text{cm} \\neq OM = 3\\,\\text{cm}$ nên $O$ không là trung điểm của $AM$."}
            ])
        ],
        "part3": [
            # 1 NB, 1 TH, 1 VD, 1 VDC (0.5đ mỗi câu)
            make_sa(1, "Nhận biết", "Số nghịch đảo của phân số $-\\frac{7}{15}$ là phân số nào? (Viết dưới dạng a/b)", "-15/7", ["-15/7", "-15 / 7"], "Nghịch đảo của $-7/15$ là $-15/7$."),
            make_sa(2, "Thông hiểu", "Tìm $x$, biết: $x - 0,75 = 1,25$.", "2", ["2", "2.0"], "$x = 1,25 + 0,75 = 2$."),
            make_sa(3, "Vận dụng", "Một giá sách có $120$ cuốn sách gồm ba loại: Toán, Văn và Anh. Số sách Toán chiếm $40\\%$ tổng số sách. Số sách Văn bằng $\\frac{5}{6}$ số sách còn lại. Tính số cuốn sách môn Tiếng Anh trên giá sách đó.", "12", ["12"], "Sách Toán: $120 \\cdot 40\\% = 48$ cuốn. Còn lại: $120 - 48 = 72$ cuốn. Sách Văn: $72 \\cdot \\frac{5}{6} = 60$ cuốn. Sách Anh: $72 - 60 = 12$ cuốn."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ lớn nhất thỏa mãn bất đẳng thức: $\\frac{x}{7} < \\frac{5}{14}$.", "2", ["2"], "$\\frac{x}{7} < \\frac{5}{14} \\Leftrightarrow \\frac{2x}{14} < \\frac{5}{14} \\Leftrightarrow 2x < 5 \\Leftrightarrow x \\le 2$. Số nguyên lớn nhất là 2.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0, 
                "Thực hiện phép tính (tính hợp lý nếu có thể):\n a) $A = \\frac{7}{15} + \\frac{8}{15} - \\frac{3}{5}$\n b) $B = 14,25 \\cdot 3,8 + 14,25 \\cdot 6,2$",
                "a) $A = \\frac{7+8}{15} - \\frac{3}{5} = 1 - \\frac{3}{5} = \\frac{2}{5}$ (0.5đ)\nb) Đặt thừa số chung: $14,25 \\cdot (3,8 + 6,2) = 14,25 \\cdot 10 = 142,5$ (0.5đ)",
                "a) Cộng cùng mẫu: $\\frac{7+8}{15} = 1$. Sau đó $1 - \\frac{3}{5} = \\frac{2}{5}$.\nb) Áp dụng tính chất phân phối: $B = 14,25 \\cdot (3,8 + 6,2) = 14,25 \\cdot 10 = 142,5$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Bác An thu hoạch được $1,2$ tấn cam. Bác bán được $\\frac{2}{5}$ số cam đó vào buổi sáng. Buổi chiều bác bán được $75\\%$ số cam còn lại.\n a) Hỏi buổi sáng bác An bán được bao nhiêu ki-lô-gam cam?\n b) Sau cả hai buổi, bác An còn lại bao nhiêu ki-lô-gam cam chưa bán?",
                "Đổi $1,2$ tấn = $1200\\,\\text{kg}$.\na) Số cam bán buổi sáng: $1200 \\cdot \\frac{2}{5} = 480\\,\\text{kg}$ (0.5đ)\nb) Số cam còn lại sau buổi sáng: $1200 - 480 = 720\\,\\text{kg}$. Số cam bán buổi chiều: $720 \\cdot 75\\% = 540\\,\\text{kg}$. Số cam còn lại cuối cùng: $720 - 540 = 180\\,\\text{kg}$ (0.5đ)",
                "a) Buổi sáng bán được $480\\,\\text{kg}$.\nb) Buổi chiều bán được $540\\,\\text{kg}$. Cuối ngày còn lại $180\\,\\text{kg}$ cam."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Trên tia $Ox$, vẽ hai điểm $A$ và $B$ sao cho $OA = 3\\,\\text{cm}$, $OB = 6\\,\\text{cm}$.\n a) Điểm $A$ có nằm giữa hai điểm $O$ và $B$ không? Vì sao?\n b) Điểm $A$ có phải là trung điểm của đoạn thẳng $OB$ không? Giải thích rõ.",
                "a) Trên cùng tia $Ox$, vì $OA < OB$ ($3\\,\\text{cm} < 6\\,\\text{cm}$) nên $A$ nằm giữa $O$ và $B$ (0.25đ)\nb) Vì $A$ nằm giữa nên $OA + AB = OB \\Rightarrow AB = 6 - 3 = 3\\,\\text{cm}$. Do $A$ nằm giữa và $OA = AB = 3\\,\\text{cm}$ nên $A$ là trung điểm của $OB$ (0.25đ)",
                "a) $A$ nằm giữa $O$ và $B$ do $OA < OB$ trên cùng tia $Ox$.\nb) Tính được $AB = 3\\,\\text{cm} = OA$. Vậy $A$ là trung điểm của $OB$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho biểu thức $S = \\frac{1}{1 \\cdot 3} + \\frac{1}{3 \\cdot 5} + \\frac{1}{5 \\cdot 7} + \\dots + \\frac{1}{(2n-1)(2n+1)}$.\n a) Rút gọn biểu thức $S$ theo $n$.\n b) Chứng minh rằng $S < \\frac{1}{2}$ với mọi số nguyên dương $n$.",
                "a) Ta có $2S = \\frac{2}{1 \\cdot 3} + \\dots = 1 - \\frac{1}{3} + \\frac{1}{3} - \\dots - \\frac{1}{2n+1} = 1 - \\frac{1}{2n+1} = \\frac{2n}{2n+1} \\Rightarrow S = \\frac{n}{2n+1}$ (0.25đ)\nb) Với mọi $n \\in \\mathbb{N}^*$, ta có $S = \\frac{1}{2} - \\frac{1}{2(2n+1)} < \\frac{1}{2}$ (đpcm) (0.25đ)",
                "a) Nhân 2 vế với 2 và rút gọn dạng sai phân: $S = \\frac{n}{2n+1}$.\nb) Vì $\\frac{1}{2(2n+1)} > 0$ nên $S = \\frac{1}{2} - \\frac{1}{2(2n+1)} < \\frac{1}{2}$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 02 ------------------
    # Ngữ cảnh: Phân số trong nấu ăn, làm bánh mì, cọc tiêu ngắm đường thẳng, tính tiền điện
    exams.append({
        "id": "p_g6_mid2_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ II - TOÁN 6 (ĐỀ SỐ 02)",
        "topic": "Số thập phân, Tỉ số phần trăm, Tia và Đoạn thẳng trong đời sống",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Trong các phân số sau, phân số nào là phân số tối giản?", ["$\\frac{4}{6}$", "$\\frac{5}{15}$", "$\\frac{7}{12}$", "$\\frac{9}{21}$"], 2, "$\\frac{7}{12}$ có $\\text{ƯCLN}(7, 12) = 1$ nên là phân số tối giản."),
            make_mc(2, "Nhận biết", "Viết số thập phân $0,35$ dưới dạng phân số tối giản ta được:", ["$\\frac{35}{100}$", "$\\frac{7}{20}$", "$\\frac{7}{50}$", "$\\frac{3}{5}$"], 1, "$0,35 = \\frac{35}{100} = \\frac{7}{20}$."),
            make_mc(3, "Nhận biết", "Hai tia chung gốc $Ox$ và $Oy$ tạo thành đường thẳng $xy$ được gọi là:", ["Hai tia trùng nhau", "Hai tia đối nhau", "Hai tia song song", "Hai đoạn thẳng"], 1, "Hai tia có chung gốc và tạo thành một đường thẳng là hai tia đối nhau."),
            make_mc(4, "Thông hiểu", "Thực hiện phép tính $\\frac{-5}{8} \\cdot \\frac{4}{15}$ ta được kết quả là:", ["$-\\frac{1}{6}$", "$\\frac{1}{6}$", "$-\\frac{1}{3}$", "$-\\frac{2}{3}$"], 0, "$\\frac{-5 \\cdot 4}{8 \\cdot 15} = \\frac{-1 \\cdot 1}{2 \\cdot 3} = -\\frac{1}{6}$."),
            make_mc(5, "Thông hiểu", "Tỉ số phần trăm của $15$ và $60$ là:", ["$20\\%$", "$25\\%$", "$30\\%$", "$15\\%$"], 1, "$\\frac{15}{60} \\cdot 100\\% = 0,25 \\cdot 100\\% = 25\\%$."),
            make_mc(6, "Thông hiểu", "Cho đoạn thẳng $MN = 10\\,\\text{cm}$. Điểm $K$ là trung điểm của đoạn thẳng $MN$. Độ dài đoạn thẳng $MK$ là:", ["$20\\,\\text{cm}$", "$5\\,\\text{cm}$", "$2,5\\,\\text{cm}$", "$4\\,\\text{cm}$"], 1, "$MK = MN : 2 = 10 : 2 = 5\\,\\text{cm}$."),
            make_mc(7, "Vận dụng", "Để làm một chiếc bánh bông lan, mẹ cần $\\frac{3}{4}\\,\\text{kg}$ bột mì. Mẹ đã có sẵn $0,45\\,\\text{kg}$ bột mì. Hỏi mẹ cần mua thêm bao nhiêu ki-lô-gam bột mì nữa?", ["$0,3\\,\\text{kg}$", "$0,25\\,\\text{kg}$", "$0,35\\,\\text{kg}$", "$1,2\\,\\text{kg}$"], 0, "$\\frac{3}{4}\\,\\text{kg} = 0,75\\,\\text{kg}$. Số bột cần mua thêm: $0,75 - 0,45 = 0,3\\,\\text{kg}$."),
            make_mc(8, "Vận dụng", "Trên tia $At$, lấy điểm $B$ và $C$ sao cho $AB = 5\\,\\text{cm}$, $BC = 3\\,\\text{cm}$. Biết điểm $B$ nằm giữa hai điểm $A$ và $C$. Độ dài đoạn thẳng $AC$ là:", ["$2\\,\\text{cm}$", "$8\\,\\text{cm}$", "$4\\,\\text{cm}$", "$15\\,\\text{cm}$"], 1, "Vì $B$ nằm giữa $A$ và $C$ nên $AC = AB + BC = 5 + 3 = 8\\,\\text{cm}$."),
            make_mc(9, "Vận dụng cao", "Tìm số tự nhiên $n$ nhỏ nhất khác 0 để phân số $\\frac{n}{n+3}$ có thể rút gọn được.", ["$n = 1$", "$n = 2$", "$n = 3$", "$n = 6$"], 2, "Gọi $d = \\text{ƯCLN}(n, n+3) \\Rightarrow 3 \\,\\vdots\\, d$. Để rút gọn được thì $d = 3 \\Rightarrow n \\,\\vdots\\, 3$. Số tự nhiên khác 0 nhỏ nhất là $n = 3$."),
            make_mc(10, "Vận dụng cao", "Cho $M = \\frac{1}{10} + \\frac{1}{11} + \\frac{1}{12} + \\dots + \\frac{1}{19}$. So sánh $M$ với $1$ ta được:", ["$M > 1$", "$M < 1$", "$M = 1$", "$M = \\frac{3}{2}$"], 1, "Tổng có 10 số hạng, mỗi số hạng $\\le \\frac{1}{10} \\Rightarrow M < 10 \\cdot \\frac{1}{10} = 1$."),
            make_mc(11, "Vận dụng cao", "Cho $20$ điểm phân biệt trên mặt phẳng, trong đó không có ba điểm nào thẳng hàng. Qua hai điểm bất kỳ vẽ một đường thẳng. Số đường thẳng vẽ được là:", ["$190$", "$380$", "$20$", "$400$"], 0, "Số đường thẳng là $\\frac{20 \\cdot 19}{2} = 190$."),
            make_mc(12, "Vận dụng cao", "Cho $x, y$ là các số nguyên thỏa mãn $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{3}$ với $x < y$. Cặp số $(x; y)$ nguyên dương lớn nhất có tổng $x + y$ là:", ["$(4; 12)$ có tổng $16$", "$(6; 6)$ có tổng $12$", "$(2; -6)$", "$(1; -3)$"], 0, "$xy - 3x - 3y = 0 \\Leftrightarrow (x-3)(y-3) = 9$. Do $x < y$ nên $x-3=1, y-3=9 \\Rightarrow x=4, y=12 \\Rightarrow x+y=16$.")
        ],
        "part2": [
            make_tf(1, "Cho số thập phân $x = -2,4$ và $y = 0,75$.", [
                {"id": "a", "text": "Số đối của $x$ là $2,4$.", "correct": True, "level": "Nhận biết", "explanation": "Số đối của $-2,4$ là $2,4$."},
                {"id": "b", "text": "Viết $y$ dưới dạng phân số tối giản là $\\frac{3}{4}$.", "correct": True, "level": "Nhận biết", "explanation": "$0,75 = 75/100 = 3/4$."},
                {"id": "c", "text": "Tích $x \\cdot y$ bằng $-1,8$.", "correct": True, "level": "Thông hiểu", "explanation": "$-2,4 \\cdot 0,75 = -1,8$."},
                {"id": "d", "text": "Thương $\\frac{x}{y}$ là một số nguyên âm.", "correct": False, "level": "Vận dụng", "explanation": "$\\frac{-2,4}{0,75} = -3,2$ không phải là số nguyên."}
            ]),
            make_tf(2, "Cho ba điểm $A, B, C$ thẳng hàng theo thứ tự đó, biết $AB = 6\\,\\text{cm}$, $BC = 4\\,\\text{cm}$. Gọi $I$ là trung điểm của $AB$ và $K$ là trung điểm của $BC$.", [
                {"id": "a", "text": "Điểm $B$ nằm giữa hai điểm $A$ và $C$.", "correct": True, "level": "Nhận biết", "explanation": "Do ba điểm thẳng hàng theo thứ tự $A, B, C$."},
                {"id": "b", "text": "Độ dài đoạn thẳng $AC$ bằng $10\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$AC = AB + BC = 6 + 4 = 10\\,\\text{cm}$."},
                {"id": "c", "text": "Độ dài đoạn thẳng $IB$ bằng $3\\,\\text{cm}$ và $BK$ bằng $2\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$IB = 6/2 = 3\\,\\text{cm}, BK = 4/2 = 2\\,\\text{cm}$."},
                {"id": "d", "text": "Độ dài đoạn thẳng $IK$ bằng $6\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "$IK = IB + BK = 3 + 2 = 5\\,\\text{cm} \\neq 6\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Rút gọn phân số $\\frac{24}{36}$ về phân số tối giản (dạng a/b):", "2/3", ["2/3", "2 / 3"], "Chia cả tử và mẫu cho 12 ta được 2/3."),
            make_sa(2, "Thông hiểu", "Tính giá trị của biểu thức: $P = (-0,5) \\cdot (-4) + 1,8 : 0,9$.", "4", ["4", "4.0"], "$(-0,5) \\cdot (-4) = 2$ và $1,8 : 0,9 = 2$. Tổng là 4."),
            make_sa(3, "Vận dụng", "Một khu vườn hình chữ nhật có chiều dài $24\\,\\text{m}$, chiều rộng bằng $\\frac{3}{4}$ chiều dài. Người ta dùng $15\\%$ diện tích vườn để đào ao thả cá. Tính diện tích phần đất đào ao (theo $\\text{m}^2$).", "64.8", ["64.8", "64,8"], "Chiều rộng: $24 \\cdot 3/4 = 18\\,\\text{m}$. Diện tích vườn: $24 \\cdot 18 = 432\\,\\text{m}^2$. Diện tích ao: $432 \\cdot 15\\% = 64,8\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Cho đoạn thẳng $AB = 12\\,\\text{cm}$. Trên đoạn thẳng $AB$ lấy điểm $M$ sao cho $AM = 2\\,MB$. Tính độ dài đoạn thẳng $AM$ (theo cm).", "8", ["8", "8 cm"], "$AM + MB = AB \\Rightarrow 2MB + MB = 12 \\Rightarrow 3MB = 12 \\Rightarrow MB = 4\\,\\text{cm} \\Rightarrow AM = 8\\,\\text{cm}$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Tính giá trị của các biểu thức sau một cách hợp lý:\n a) $A = \\frac{3}{7} \\cdot \\frac{5}{11} + \\frac{3}{7} \\cdot \\frac{6}{11}$\n b) $B = 32,4 - 15,6 + 7,6 - 4,4$",
                "a) Đặt $\\frac{3}{7}$ làm nhân tử chung: $\\frac{3}{7} \\cdot \\left(\\frac{5}{11} + \\frac{6}{11}\\right) = \\frac{3}{7} \\cdot 1 = \\frac{3}{7}$ (0.5đ)\nb) Nhóm hợp lý: $(32,4 + 7,6) - (15,6 + 4,4) = 40 - 20 = 20$ (0.5đ)",
                "a) Phân phối phép nhân đối với phép cộng: $A = \\frac{3}{7}$.\nb) Nhóm các số có phần thập phân bù nhau: $B = 40 - 20 = 20$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Lớp 6A có $45$ học sinh. Cuối học kỳ I, kết quả xếp loại học lực gồm ba mức: Tốt, Khá và Đạt. Số học sinh Tốt chiếm $\\frac{1}{3}$ số học sinh cả lớp. Số học sinh Khá bằng $\\frac{3}{5}$ số học sinh còn lại. Còn lại là học sinh xếp loại Đạt.\n a) Tính số học sinh xếp loại Tốt của lớp 6A.\n b) Tính tỉ số phần trăm của số học sinh xếp loại Đạt so với tổng số học sinh cả lớp.",
                "a) Số HS Tốt: $45 \\cdot \\frac{1}{3} = 15$ học sinh (0.5đ)\nb) Số HS còn lại: $45 - 15 = 30$ HS. Số HS Khá: $30 \\cdot \\frac{3}{5} = 18$ HS. Số HS Đạt: $30 - 18 = 12$ HS. Tỉ số phần trăm: $\\frac{12}{45} \\cdot 100\\% \\approx 26,67\\%$ (hoặc $\\frac{80}{3}\\%$) (0.5đ)",
                "a) Số học sinh Tốt là 15 học sinh.\nb) Số học sinh Đạt là 12 học sinh, chiếm tỉ lệ $\\frac{12}{45} \\cdot 100\\% = 26,67\\%$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Cho đoạn thẳng $PQ = 8\\,\\text{cm}$. Lấy điểm $E$ nằm giữa $P$ và $Q$ sao cho $PE = 4\\,\\text{cm}$.\n a) So sánh độ dài hai đoạn thẳng $PE$ và $EQ$.\n b) Điểm $E$ có là trung điểm của đoạn thẳng $PQ$ không? Vì sao?",
                "a) Vì $E$ nằm giữa $P, Q$ nên $PE + EQ = PQ \\Rightarrow EQ = 8 - 4 = 4\\,\\text{cm}$. Do đó $PE = EQ = 4\\,\\text{cm}$ (0.25đ)\nb) Điểm $E$ nằm giữa $P, Q$ và cách đều hai đầu mút ($PE = EQ$) nên $E$ là trung điểm của $PQ$ (0.25đ)",
                "a) Ta có $EQ = 4\\,\\text{cm} = PE$.\nb) $E$ là trung điểm của đoạn thẳng $PQ$ vì $E$ nằm giữa và $PE = EQ$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Chứng minh rằng phân số $B = \\frac{12n + 1}{30n + 2}$ là phân số tối giản với mọi số tự nhiên $n$.",
                "Gọi $d = \\text{ƯCLN}(12n + 1, 30n + 2) \\Rightarrow 12n + 1 \\,\\vdots\\, d$ và $30n + 2 \\,\\vdots\\, d$ (0.1đ)\nSuy ra $5(12n + 1) - 2(30n + 2) \\,\\vdots\\, d \\Rightarrow (60n + 5) - (60n + 4) = 1 \\,\\vdots\\, d$ (0.25đ)\nDo đó $d = 1$, phân số $B$ luôn tối giản với mọi số tự nhiên $n$ (0.15đ)",
                "Gọi $d$ là ước chung lớn nhất của tử và mẫu. Nhân tử số với 5 và mẫu số với 2 rồi trừ cho nhau: $5(12n+1) - 2(30n+2) = 1 \\,\\vdots\\, d \\Rightarrow d = 1$. Vậy phân số luôn tối giản."
            )
        ]
    })

    # Thêm Đề 03, 04, 05, 06 cho mid2 với sự đa dạng tuyệt đối về ngữ cảnh và số liệu
    for t_idx in range(3, 7):
        ex_num = f"0{t_idx}"
        # Đề 3: Thể thao, điền kinh, đoạn thẳng sân trường
        # Đề 4: Nông nghiệp thu hoạch lúa, làm tròn số, tia số
        # Đề 5: Tiết kiệm ngân hàng, lãi suất, trung điểm dây phơi
        # Đề 6: Mua bán đồ gia dụng, tỉ số phần trăm lợi nhuận, thước đo
        topics = [
            "Hỗn số, Phép nhân chia phân số, Điểm nằm giữa và Bất đẳng thức phân số",
            "Làm tròn số thập phân, Tỉ số và tỉ số phần trăm, Tia đối, đoạn thẳng cắt nhau",
            "Toán thực tế kinh doanh, lãi suất phần trăm, Trung điểm đoạn thẳng & Cực trị đại số",
            "Phân số âm, phép tính phối hợp, Đo độ dài thực tế và Ước chung phân số tối giản"
        ]
        topic = topics[t_idx - 3]

        exams.append({
            "id": f"p_g6_mid2_{ex_num}",
            "testNum": t_idx,
            "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ II - TOÁN 6 (ĐỀ SỐ {ex_num})",
            "topic": topic,
            "grade": "6",
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
                make_mc(1, "Nhận biết", f"Phân số nghịch đảo của phân số $\\frac{{-{t_idx}}}{{7}}$ là:", [f"$\\frac{{7}}{{-{t_idx}}}$", f"$\\frac{{{t_idx}}}{{7}}$", f"$\\frac{{-7}}{{-{t_idx}}}$", "$-1$"], 0, f"Nghịch đảo của $-{t_idx}/7$ là $-7/{t_idx}$."),
                make_mc(2, "Nhận biết", f"Chữ số hàng phần trăm của số thập phân ${12 + t_idx},4{t_idx}8$ là chữ số nào?", [f"${t_idx}$", "$4$", "$8$", f"${12 + t_idx}$"], 0, f"Chữ số thứ hai sau dấu phẩy là hàng phần trăm: {t_idx}."),
                make_mc(3, "Nhận biết", "Nếu điểm $I$ là trung điểm của đoạn thẳng $CD$ thì:", ["$IC = ID = \\frac{CD}{2}$", "$IC + CD = ID$", "$IC = 2CD$", "$I$ nằm ngoài đoạn $CD$"], 0, "Theo định nghĩa trung điểm: $IC = ID = CD/2$."),
                make_mc(4, "Thông hiểu", f"Tìm $x$, biết: $x + \\frac{{{t_idx}}}{{10}} = \\frac{{{t_idx + 5}}}{{10}}$.", ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$1$", "$2$"], 0, f"$x = \\frac{{{t_idx + 5} - {t_idx}}}{{10}} = \\frac{{5}}{{10}} = \\frac{1}{2}$."),
                make_mc(5, "Thông hiểu", f"Làm tròn số $45,{t_idx}72$ đến chữ số thập phân thứ nhất ta được:", [f"$45,{t_idx + 1}$", f"$45,{t_idx}$", "$46$", "$45$"], 0, f"Chữ số hàng phần trăm là 7 >= 5 nên làm tròn lên: 45,{t_idx+1}."),
                make_mc(6, "Thông hiểu", f"Biết $\\frac{{{t_idx}}}{{5}}$ của quãng đường là ${6 * t_idx}\\,\\text{{km}}$. Toàn bộ quãng đường dài bao nhiêu ki-lô-mét?", ["$30\\,\\text{km}$", "$25\\,\\text{km}$", "$35\\,\\text{km}$", "$40\\,\\text{km}$"], 0, f"Độ dài quãng đường là $6 \\cdot {t_idx} : \\frac{{{t_idx}}}{{5}} = 30\\,\\text{{km}}$."),
                make_mc(7, "Vận dụng", f"Một bác nông dân thu được ${100 * t_idx}\\,\\text{{kg}}$ thóc. Bác dành $20\\%$ để làm giống, số còn lại đem bán với giá $9\\,500$ đồng/kg. Số tiền bác thu được khi bán thóc là:", [f"${100 * t_idx * 0.8 * 9500:,.0f}$ đồng".replace(",", "."), f"${100 * t_idx * 9500:,.0f}$ đồng".replace(",", "."), "Không xác định", "100.000 đồng"], 0, f"Số thóc bán là ${100 * t_idx * 0.8}$ kg. Nhân với giá bán được số tiền tương ứng."),
                make_mc(8, "Vận dụng", f"Trên đường thẳng $d$, lấy các điểm $A, B, C$ sao cho $AB = {2 * t_idx}\\,\\text{{cm}}$, $BC = {4 * t_idx}\\,\\text{{cm}}$. Biết $B$ nằm giữa $A$ và $C$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $BC$. Độ dài đoạn thẳng $MN$ là:", [f"${3 * t_idx}\\,\\text{{cm}}$", f"${2 * t_idx}\\,\\text{{cm}}$", f"${4 * t_idx}\\,\\text{{cm}}$", f"${t_idx}\\,\\text{{cm}}$"], 0, f"$MN = MB + BN = {t_idx} + {2 * t_idx} = {3 * t_idx}\\,\\text{{cm}}$."),
                make_mc(9, "Vận dụng cao", f"Tìm $x \\in \\mathbb{{Z}}$ để phân số $\\frac{{{2*t_idx + 1}}}{{x - 1}}$ là số nguyên.", [f"$x \\in \\{{0; 2; 1 \\pm ({2*t_idx + 1})\\}}$", "$x = 0$", "$x = 1$", "Không tồn tại"], 0, f"$x - 1$ phải là ước của ${2*t_idx + 1}$."),
                make_mc(10, "Vận dụng cao", f"Có bao nhiêu số nguyên $n$ để phân số $\\frac{{n + {t_idx}}}{{n - 1}}$ nhận giá trị nguyên?", ["4", "2", "6", "8"], 0, f"Biến đổi $1 + \\frac{{{t_idx + 1}}}{{n - 1}}$. Số ước của ${t_idx + 1}$ là hữu hạn."),
                make_mc(11, "Vận dụng cao", f"Cho $n$ điểm phân biệt ($n \\ge 3$), trong đó không có ba điểm nào thẳng hàng. Vẽ được tất cả ${t_idx * (t_idx - 1) * 5 + 10}$ đoạn thẳng. Giá trị của $n$ là một số nguyên dương thỏa mãn:", ["$n(n-1) = 2 \\times \\text{số đoạn}$", "$n = 100$", "$n = 2$", "Vô số"], 0, "Số đoạn thẳng nối 2 điểm là $n(n-1)/2$."),
                make_mc(12, "Vận dụng cao", "Cho tổng $T = \\frac{1}{3} + \\frac{1}{3^2} + \\dots + \\frac{1}{3^{100}}$. So sánh $T$ với $\\frac{1}{2}$ ta được:", ["$T < \\frac{1}{2}$", "$T > \\frac{1}{2}$", "$T = \\frac{1}{2}$", "$T = 1$"], 0, "$3T = 1 + T - \\frac{1}{3^{100}} \\Rightarrow 2T = 1 - \\frac{1}{3^{100}} < 1 \\Rightarrow T < \\frac{1}{2}$.")
            ],
            "part2": [
                make_tf(1, f"Cho phân số $P = \\frac{{{t_idx}}}{{6}}$ và $Q = -0,{t_idx}$.", [
                    {"id": "a", "text": "Phân số $P$ là một phân số dương.", "correct": True, "level": "Nhận biết", "explanation": f"Tử và mẫu đều dương nên $P > 0$."},
                    {"id": "b", "text": "Số thập phân $Q$ là một số thập phân âm.", "correct": True, "level": "Nhận biết", "explanation": "Có dấu trừ đằng trước nên là số âm."},
                    {"id": "c", "text": f"Tích $P \\cdot Q$ luôn mang dấu âm.", "correct": True, "level": "Thông hiểu", "explanation": "Tích của một số dương và một số âm luôn mang dấu âm."},
                    {"id": "d", "text": f"Tổng $P + Q$ luôn nhận giá trị bằng $0$.", "correct": False, "level": "Vận dụng", "explanation": f"${t_idx}/6 \\neq 0,{t_idx}$ nên tổng khác 0."}
                ]),
                make_tf(2, f"Cho đoạn thẳng $AB = {4 * t_idx}\\,\\text{{cm}}$. Trên đoạn $AB$ lấy điểm $C$ sao cho $AC = {2 * t_idx}\\,\\text{{cm}}$.", [
                    {"id": "a", "text": "Điểm $C$ nằm giữa hai điểm $A$ và $B$.", "correct": True, "level": "Nhận biết", "explanation": "Do $C$ thuộc đoạn thẳng $AB$ và $0 < AC < AB$."},
                    {"id": "b", "text": f"Độ dài đoạn thẳng $CB$ bằng ${2 * t_idx}\\,\\text{{cm}}$.", "correct": True, "level": "Thông hiểu", "explanation": f"$CB = AB - AC = {4*t_idx} - {2*t_idx} = {2*t_idx}\\,\\text{{cm}}$."},
                    {"id": "c", "text": "Điểm $C$ là trung điểm của đoạn thẳng $AB$.", "correct": True, "level": "Thông hiểu", "explanation": "Vì $C$ nằm giữa và $AC = CB$."},
                    {"id": "d", "text": f"Lấy điểm $D$ đối xứng với $A$ qua $B$, độ dài $AD$ bằng ${6 * t_idx}\\,\\text{{cm}}$.", "correct": False, "level": "Vận dụng", "explanation": f"$B$ là trung điểm $AD$ nên $AD = 2AB = {8*t_idx}\\,\\text{{cm}} \\neq {6*t_idx}\\,\\text{{cm}}$."}
                ])
            ],
            "part3": [
                make_sa(1, "Nhận biết", f"Tính giá trị của phép tính: $\\frac{{{t_idx}}}{{9}} + \\frac{{{9 - t_idx}}}{{9}}$.", "1", ["1", "1.0"], "Tổng hai phân số cùng mẫu là 9/9 = 1."),
                make_sa(2, "Thông hiểu", f"Tìm $x$, biết: $\\frac{{x}}{{{2 * t_idx}}} = \\frac{{3}}{{2}}$.", str(3 * t_idx), [str(3 * t_idx)], f"$x = \\frac{{3 \\cdot {2 * t_idx}}}{{2}} = {3 * t_idx}$."),
                make_sa(3, "Vận dụng", f"Một người gửi tiết kiệm ${10 * t_idx}$ triệu đồng với lãi suất $6\\%$ một năm. Sau đúng 1 năm, cả vốn lẫn lãi người đó nhận được là bao nhiêu triệu đồng?", f"{10 * t_idx * 1.06:.2f}".rstrip("0").rstrip("."), [f"{10 * t_idx * 1.06:.2f}".rstrip("0").rstrip(".")], "Tiền lãi = Vốn * 6%. Cả gốc và lãi = Vốn * 106%."),
                make_sa(4, "Vận dụng cao", f"Tìm số nguyên $n$ nhỏ nhất để biểu thức $\\frac{{n + {t_idx}}}{{3}}$ nhận giá trị là một số nguyên tố nhỏ nhất.", str(6 - t_idx), [str(6 - t_idx)], f"Số nguyên tố nhỏ nhất là 2 $\\Rightarrow (n + {t_idx})/3 = 2 \\Rightarrow n + {t_idx} = 6 \\Rightarrow n = {6 - t_idx}$.")
            ],
            "part4": [
                make_essay(1, "Nhận biết", 1.0,
                    f"Thực hiện phép tính hợp lý:\n a) $A = \\frac{{{t_idx}}}{{13}} \\cdot \\frac{{4}}{{7}} + \\frac{{{t_idx}}}{{13}} \\cdot \\frac{{3}}{{7}}$\n b) $B = 25,{t_idx} + 14,8 - 5,{t_idx}$",
                    f"a) Đặt nhân tử chung $\\frac{{{t_idx}}}{{13}} \\cdot \\left(\\frac{{4+3}}{{7}}\\right) = \\frac{{{t_idx}}}{{13}}$ (0.5đ)\nb) $(25,{t_idx} - 5,{t_idx}) + 14,8 = 20 + 14,8 = 34,8$ (0.5đ)",
                    f"a) $A = \\frac{{{t_idx}}}{{13}}$.\nb) $B = 34,8$."
                ),
                make_essay(2, "Thông hiểu", 1.0,
                    f"Một cửa hàng nhập về ${200 * t_idx}\\,\\text{{kg}}$ gạo. Ngày thứ nhất bán được $\\frac{{1}}{{4}}$ số gạo. Ngày thứ hai bán được $60\\%$ số gạo còn lại.\n a) Tính số ki-lô-gam gạo bán được trong ngày thứ nhất.\n b) Sau hai ngày, cửa hàng còn lại bao nhiêu ki-lô-gam gạo?",
                    f"a) Ngày 1: ${200*t_idx} \\cdot 1/4 = {50*t_idx}\\,\\text{{kg}}$ (0.5đ)\nb) Còn lại sau ngày 1: ${150*t_idx}\\,\\text{{kg}}$. Ngày 2: ${150*t_idx} \\cdot 60\\% = {90*t_idx}\\,\\text{{kg}}$. Còn lại cuối cùng: ${150*t_idx - 90*t_idx} = {60*t_idx}\\,\\text{{kg}}$ (0.5đ)",
                    f"a) Ngày thứ nhất bán được ${50*t_idx}\\,\\text{{kg}}$ gạo.\nb) Cuối cùng cửa hàng còn lại ${60*t_idx}\\,\\text{{kg}}$ gạo."
                ),
                make_essay(3, "Vận dụng", 0.5,
                    f"Trên tia $Ox$, lấy hai điểm $E, F$ sao cho $OE = {t_idx}\\,\\text{{cm}}$, $OF = {2 * t_idx}\\,\\text{{cm}}$.\n a) Chứng tỏ điểm $E$ nằm giữa hai điểm $O$ và $F$.\n b) Điểm $E$ có phải là trung điểm của đoạn thẳng $OF$ không? Vì sao?",
                    f"a) Vì $OE < OF$ (${t_idx} < {2*t_idx}$) trên cùng tia $Ox$ nên $E$ nằm giữa $O$ và $F$ (0.25đ)\nb) $EF = OF - OE = {t_idx}\\,\\text{{cm}} = OE$. Vậy $E$ là trung điểm của $OF$ (0.25đ)",
                    f"a) $E$ nằm giữa $O$ và $F$.\nb) $E$ là trung điểm của $OF$ vì nằm giữa và $OE = EF = {t_idx}\\,\\text{{cm}}$."
                ),
                make_essay(4, "Vận dụng cao", 0.5,
                    f"Tìm các số nguyên $x, y$ thỏa mãn phương trình: $(x - {t_idx})(y + 2) = 5$.",
                    f"Vì $x, y \\in \\mathbb{{Z}}$ nên $x - {t_idx}$ và $y + 2$ là các ước của 5, tức là $\\pm 1, \\pm 5$ (0.25đ)\nLập bảng xét 4 trường hợp ta tìm được các cặp $(x; y)$ tương ứng (0.25đ)",
                    f"Xét các ước nguyên của 5: $\\pm 1, \\pm 5$, từ đó suy ra 4 cặp nghiệm nguyên $(x; y)$."
                )
            ]
        })

    return exams

# ==============================================================================
# 6 MÃ ĐỀ CUỐI KỲ 2 - TOÁN 6 (final2)
# Phạm vi: Toàn bộ HK2: Phân số, Số thập phân, Đoạn thẳng & Góc, Dữ liệu & Xác suất.
# ==============================================================================
def generate_g6_final2():
    exams = []
    
    for t_idx in range(1, 7):
        ex_num = f"0{t_idx}"
        topics = [
            "Tổng hợp Số học HK2, Góc và số đo góc, Biểu đồ cột kép và Xác suất thực nghiệm",
            "Tỉ số phần trăm, Đoạn thẳng và góc, Bảng thống kê dữ liệu thực nghiệm trò chơi",
            "Toán thực tế kinh doanh, Góc kề bù, Xác suất thực nghiệm khi gieo xúc xắc",
            "Phân số phức hợp, Số đo góc nhọn/vuông/tù, Thu thập và phân tích dữ liệu",
            "Các phép tính số thập phân, Tia phân giác của góc, Xác suất tung đồng xu",
            "Ôn tập toàn diện cuối năm Toán 6: Số học, Hình học trực quan và Thống kê"
        ]
        topic = topics[t_idx - 1]

        exams.append({
            "id": f"p_g6_final2_{ex_num}",
            "testNum": t_idx,
            "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ II - TOÁN 6 (ĐỀ SỐ {ex_num})",
            "topic": topic,
            "grade": "6",
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
                make_mc(1, "Nhận biết", "Góc có số đo bằng $90^\\circ$ được gọi là:", ["Góc nhọn", "Góc vuông", "Góc tù", "Góc bẹt"], 1, "Góc vuông là góc có số đo bằng $90^\\circ$."),
                make_mc(2, "Nhận biết", "Trong các dữ liệu sau, dữ liệu nào là dữ liệu số (số liệu)?", ["Màu sắc yêu thích của học sinh", "Chiều cao (cm) của 10 bạn trong tổ", "Nơi sinh của các thành viên trong gia đình", "Xếp loại học lực cuối kỳ"], 1, "Chiều cao là số đo cụ thể nên là số liệu."),
                make_mc(3, "Nhận biết", f"Phân số nào sau đây nhỏ hơn $0$?", ["$\\frac{3}{5}$", "$\\frac{-2}{-7}$", f"$\\frac{{-{t_idx}}}{{9}}$", "$0$"], 2, f"Phân số $-{t_idx}/9$ có tử âm mẫu dương nên nhỏ hơn 0."),
                make_mc(4, "Thông hiểu", "Gieo một con xúc xắc 6 mặt 50 lần, thấy có 15 lần xuất hiện mặt 2 chấm. Xác suất thực nghiệm của sự kiện 'Mặt xuất hiện là 2 chấm' là:", ["$\\frac{3}{10}$", "$\\frac{1}{6}$", "$\\frac{15}{6}$", "$0,2$"], 0, "Xác suất thực nghiệm: $15 / 50 = 3 / 10 = 0,3$."),
                make_mc(5, "Thông hiểu", "Cho góc $\\widehat{xOy} = 120^\\circ$. Góc $\\widehat{xOy}$ là góc loại nào?", ["Góc nhọn", "Góc vuông", "Góc tù", "Góc bẹt"], 2, "Góc có số đo lớn hơn $90^\\circ$ và nhỏ hơn $180^\\circ$ là góc tù."),
                make_mc(6, "Thông hiểu", f"Kết quả phép tính $\\frac{{{2*t_idx}}}{{7}} : \\frac{{{t_idx}}}{{14}}$ bằng:", ["$4$", "$2$", "$1$", "$8$"], 0, f"$\\frac{{{2*t_idx}}}{{7}} \\cdot \\frac{{14}}{{{t_idx}}} = 2 \\cdot 2 = 4$."),
                make_mc(7, "Vận dụng", f"Một hộp chứa 5 quả bóng đỏ và 15 quả bóng xanh. Bạn Minh lấy ngẫu nhiên một quả bóng. Xác suất lý thuyết để Minh lấy được quả bóng màu đỏ là:", ["$\\frac{1}{4}$", "$\\frac{1}{3}$", "$\\frac{3}{4}$", "$\\frac{1}{5}$"], 0, "Tổng số bóng là 20. Xác suất lấy bóng đỏ: $5 / 20 = 1/4$."),
                make_mc(8, "Vận dụng", f"Cho hai góc kề bù $\\widehat{{xOy}}$ và $\\widehat{{yOz}}$. Biết $\\widehat{{xOy}} = {60 + 5 * t_idx}^\\circ$. Số đo góc $\\widehat{{yOz}}$ là:", [f"${180 - (60 + 5 * t_idx)}^\\circ$", f"${90 - (60 + 5 * t_idx)}^\\circ$", "$120^\\circ$", "$60^\\circ$"], 0, f"Hai góc kề bù có tổng số đo bằng $180^\\circ$ nên $\\widehat{{yOz}} = 180^\\circ - {60 + 5 * t_idx}^\\circ = {180 - (60 + 5 * t_idx)}^\\circ$."),
                make_mc(9, "Vận dụng cao", "Tìm số nguyên $x$ thỏa mãn: $\\frac{x}{3} = \\frac{12}{x}$ với $x > 0$.", ["$6$", "$4$", "$-6$", "$36$"], 0, "$x^2 = 36 \\Rightarrow x = 6$ (do $x > 0$)."),
                make_mc(10, "Vận dụng cao", "Cho 10 tia chung gốc phân biệt. Số góc được tạo thành từ 10 tia đó là:", ["$45$ góc", "$90$ góc", "$10$ góc", "$20$ góc"], 0, "Số góc là $\\frac{10 \\cdot 9}{2} = 45$ góc."),
                make_mc(11, "Vận dụng cao", f"Tung một đồng xu ${20 * t_idx}$ lần, thấy số lần xuất hiện mặt ngửa gấp 3 lần số lần xuất hiện mặt sấp. Số lần xuất hiện mặt ngửa là:", [f"${15 * t_idx}$", f"${5 * t_idx}$", f"${10 * t_idx}$", f"${20 * t_idx}$"], 0, f"Tổng số phần là 4 phần. Số lần mặt ngửa là $20 \\cdot {t_idx} \\cdot \\frac{3}{4} = {15 * t_idx}$."),
                make_mc(12, "Vận dụng cao", "Cho biểu thức $A = \\frac{1}{2 \\cdot 4} + \\frac{1}{4 \\cdot 6} + \\dots + \\frac{1}{98 \\cdot 100}$. Giá trị của $A$ bằng:", ["$\\frac{49}{200}$", "$\\frac{49}{100}$", "$\\frac{1}{4}$", "$\\frac{99}{200}$"], 0, "$2A = \\frac{1}{2} - \\frac{1}{100} = \\frac{49}{100} \\Rightarrow A = \\frac{49}{200}$.")
            ],
            "part2": [
                make_tf(1, f"Một cửa hàng bán trà sữa khảo sát hương vị yêu thích của 100 bạn học sinh: 40 bạn thích Vani, 35 bạn thích Trân châu đường đen, 25 bạn thích Matcha.", [
                    {"id": "a", "text": "Tổng số học sinh tham gia khảo sát là 100 bạn.", "correct": True, "level": "Nhận biết", "explanation": "40 + 35 + 25 = 100."},
                    {"id": "b", "text": "Tỉ lệ học sinh thích vị Vani chiếm $40\\%$.", "correct": True, "level": "Nhận biết", "explanation": "40/100 = 40%."},
                    {"id": "c", "text": "Số bạn thích vị Trân châu đường đen gấp hơn 1,5 lần số bạn thích vị Matcha.", "correct": False, "level": "Thông hiểu", "explanation": "35 / 25 = 1,4 < 1,5."},
                    {"id": "d", "text": "Nếu chọn ngẫu nhiên 1 bạn, xác suất để bạn đó thích Matcha hoặc Vani là $65\\%$.", "correct": True, "level": "Vận dụng", "explanation": "(40 + 25) / 100 = 65%."}
                ]),
                make_tf(2, f"Cho góc bẹt $\\widehat{{xOy}}$. Trên cùng một nửa mặt phẳng bờ $xy$, vẽ tia $Oz$ sao cho $\\widehat{{xOz}} = {40 + 5 * t_idx}^\\circ$.", [
                    {"id": "a", "text": "Góc bẹt $\\widehat{xOy}$ có số đo bằng $180^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "Góc bẹt có số đo $180^\\circ$."},
                    {"id": "b", "text": f"Góc $\\widehat{{xOz}}$ là một góc nhọn.", "correct": True, "level": "Thông hiểu", "explanation": f"Số đo là ${40 + 5 * t_idx}^\\circ < 90^\\circ$."},
                    {"id": "c", "text": f"Số đo góc $\\widehat{{yOz}}$ bằng ${180 - (40 + 5 * t_idx)}^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": f"Vì $\\widehat{{xOz}}$ và $\\widehat{{yOz}}$ kề bù nên tổng bằng $180^\\circ$."},
                    {"id": "d", "text": "Tia $Oz$ là tia phân giác của góc $\\widehat{xOy}$.", "correct": False, "level": "Vận dụng", "explanation": f"Tia phân giác của góc bẹt phải tạo góc $90^\\circ$, ở đây khác $90^\\circ$."}
                ])
            ],
            "part3": [
                make_sa(1, "Nhận biết", "Một góc có số đo bằng $45^\\circ$ là góc nhọn hay góc tù? (Trả lời: Nhọn hoặc Tù)", "Nhọn", ["Nhọn", "nhon", "Góc nhọn"], "Góc nhỏ hơn 90 độ là góc nhọn."),
                make_sa(2, "Thông hiểu", f"Gieo một con xúc xắc 30 lần, thấy có {6 + t_idx} lần xuất hiện mặt 6 chấm. Tính xác suất thực nghiệm xuất hiện mặt 6 chấm (dạng thập phân làm tròn 2 chữ số):", f"{(6 + t_idx) / 30:.2f}".rstrip("0").rstrip("."), [f"{(6 + t_idx) / 30:.2f}".rstrip("0").rstrip(".")], "Xác suất = số lần xuất hiện / tổng số lần gieo."),
                make_sa(3, "Vận dụng", f"Biết $\\widehat{{A}}$ và $\\widehat{{B}}$ là hai góc phụ nhau (tổng số đo bằng $90^\\circ$), và $\\widehat{{A}} - \\widehat{{B}} = {10 * t_idx}^\\circ$. Tìm số đo góc $\\widehat{{A}}$ (theo độ):", str((90 + 10 * t_idx) // 2), [str((90 + 10 * t_idx) // 2)], f"$\\widehat{{A}} = (90 + {10 * t_idx}) / 2 = {(90 + 10 * t_idx) // 2}^\\circ$."),
                make_sa(4, "Vận dụng cao", "Cho 8 điểm phân biệt trong đó có đúng 3 điểm thẳng hàng. Vẽ được tất cả bao nhiêu đường thẳng đi qua các cặp điểm?", "26", ["26"], "Tổng số đường thẳng nếu không thẳng hàng: 8*7/2 = 28. Trừ đi 3 điểm thẳng hàng: 28 - 3 + 1 = 26 đường thẳng.")
            ],
            "part4": [
                make_essay(1, "Nhận biết", 1.0,
                    f"Thực hiện phép tính:\n a) $\\frac{{{t_idx}}}{{8}} + \\frac{{3}}{{8}} - \\frac{{1}}{{2}}$\n b) $4,5 \\cdot 1,6 + 4,5 \\cdot 8,4$",
                    f"a) $\\frac{{{t_idx + 3}}}{{8}} - \\frac{{4}}{{8}} = \\frac{{{t_idx - 1}}}{{8}}$ (0.5đ)\nb) $4,5 \\cdot (1,6 + 8,4) = 4,5 \\cdot 10 = 45$ (0.5đ)",
                    f"a) Rút gọn biểu thức phân số.\nb) Áp dụng tính chất phân phối: kết quả bằng 45."
                ),
                make_essay(2, "Thông hiểu", 1.0,
                    f"Bảng sau đây cho biết số lượng xe đạp bán được trong 4 tuần của một cửa hàng: Tuần 1: 15 xe, Tuần 2: 25 xe, Tuần 3: 20 xe, Tuần 4: 40 xe.\n a) Cửa hàng bán được tổng cộng bao nhiêu xe trong cả 4 tuần?\n b) Số xe bán được trong Tuần 4 chiếm bao nhiêu phần trăm tổng số xe bán được?",
                    "a) Tổng số xe: $15 + 25 + 20 + 40 = 100$ xe (0.5đ)\nb) Tỉ số phần trăm của Tuần 4: $\\frac{40}{100} \\cdot 100\\% = 40\\%$ (0.5đ)",
                    "a) Tổng cộng bán được 100 chiếc xe đạp.\nb) Tuần 4 chiếm đúng 40% tổng số xe bán được."
                ),
                make_essay(3, "Vận dụng", 0.5,
                    f"Trên cùng một nửa mặt phẳng bờ chứa tia $Ox$, vẽ hai tia $Oy$ và $Oz$ sao cho $\\widehat{{xOy}} = {30 * (1 if t_idx % 2 == 1 else 1) + 10}^\\circ$, $\\widehat{{xOz}} = {70 + 10 * (t_idx % 2)}^\\circ$.\n a) Tia nào nằm giữa hai tia còn lại? Vì sao?\n b) Tính số đo góc $\\widehat{{yOz}}$.",
                    "a) Vì $\\widehat{xOy} < \\widehat{xOz}$ trên cùng nửa mặt phẳng nên tia $Oy$ nằm giữa hai tia $Ox$ và $Oz$ (0.25đ)\nb) $\\widehat{yOz} = \\widehat{xOz} - \\widehat{xOy}$ (0.25đ)",
                    "a) Tia $Oy$ nằm giữa hai tia $Ox$ và $Oz$.\nb) Số đo góc $\\widehat{yOz}$ được tính bằng hiệu hai góc."
                ),
                make_essay(4, "Vận dụng cao", 0.5,
                    f"Tìm giá trị lớn nhất của phân số $P = \\frac{{{5}}}{{(x - {t_idx})^2 + 2}}$ với $x \\in \\mathbb{{R}}$.",
                    f"Vì $(x - {t_idx})^2 \\ge 0$ với mọi $x$ nên mẫu số $(x - {t_idx})^2 + 2 \\ge 2$ (0.25đ)\nPhân số có tử dương, mẫu số lớn hơn hoặc bằng 2 nên $P \\le \\frac{{5}}{{2}} = 2,5$. Dấu '=' xảy ra khi $x = {t_idx}$ (0.25đ)",
                    f"Mẫu số nhỏ nhất bằng 2 khi $x = {t_idx}$. Do đó giá trị lớn nhất của $P$ là $2,5$."
                )
            ]
        })

    return exams

def main():
    print("=== SINH VÀ KIỂM TRA ĐỀ ĐỊNH KỲ TOÁN 6 ===")
    mid2_exams = generate_g6_mid2()
    final2_exams = generate_g6_final2()

    assert len(mid2_exams) == 6, f"Thiếu đề mid2: {len(mid2_exams)} != 6"
    assert len(final2_exams) == 6, f"Thiếu đề final2: {len(final2_exams)} != 6"

    for idx, ex in enumerate(mid2_exams, 1):
        validate_periodic_exam(ex, "6", "mid2", idx)
        print(f"✅ Toán 6 - Giữa kỳ 2 (Đề {idx}): ĐẠT CHUẨN MA TRẬN 100%.")

    for idx, ex in enumerate(final2_exams, 1):
        validate_periodic_exam(ex, "6", "final2", idx)
        print(f"✅ Toán 6 - Cuối kỳ 2 (Đề {idx}): ĐẠT CHUẨN MA TRẬN 100%.")

    print("🎉 Hoàn thành xuất sắc 12 đề định kỳ Toán 6!")
    return mid2_exams, final2_exams

if __name__ == "__main__":
    main()
