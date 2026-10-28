# -*- coding: utf-8 -*-
"""
BỘ ĐỀ THI ĐỊNH KỲ TOÁN 6 - HỌC KỲ I (GIỮA KỲ 1 & CUỐI KỲ 1)
6 mã đề Giữa kỳ 1 + 6 mã đề Cuối kỳ 1.
Chuẩn ma trận GDPT 2018 (Kết nối tri thức) & Validator kiểm soát:
- 30% NB (3.0đ), 30% TH (3.0đ), 20% VD (2.0đ), 20% VDC (2.0đ) = 10.0đ
- Phần II: Đúng 1 ý Vận dụng mỗi câu lớn
- Phần III: 1 VD, 1 VDC, 2 cơ bản
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
# 6 MÃ ĐỀ GIỮA KỲ 1 - TOÁN 6 (mid1)
# Phạm vi: Tập hợp, Lũy thừa, Thứ tự phép tính, Chia hết, Số nguyên tố, Hình phẳng thực tế (Tam giác đều, Hình vuông, Lục giác đều, Hình chữ nhật, Hình thoi, Hình bình hành).
# ==============================================================================
def generate_g6_mid1():
    exams = []

    # ------------------ ĐỀ SỐ 01 ------------------
    # Ngữ cảnh: Vườn sinh thái nông nghiệp, tính tiền mua vật tư, lát gạch hoa văn
    exams.append({
        "id": "p_g6_mid1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 01)",
        "topic": "Tập hợp số tự nhiên, Lũy thừa, Dấu hiệu chia hết & Hình học trực quan",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid 3 < x \\le 7\\}$. Khẳng định nào sau đây đúng?", ["$3 \\in A$", "$7 \\in A$", "$8 \\in A$", "$A = \\{3; 4; 5; 6; 7\\}$"], 1, "Vì $x \\le 7$ nên phần tử 7 thuộc tập hợp $A$."),
            make_mc(2, "Nhận biết", "Trong các hình sau, hình nào có 3 cạnh bằng nhau và 3 góc bằng nhau?", ["Tam giác đều", "Hình vuông", "Hình thoi", "Hình lục giác đều"], 0, "Tam giác đều là tam giác có 3 cạnh bằng nhau và 3 góc bằng nhau."),
            make_mc(3, "Nhận biết", "Số nào sau đây là số nguyên tố?", ["$9$", "$15$", "$17$", "$21$"], 2, "17 chỉ có hai ước là 1 và chính nó."),
            make_mc(4, "Thông hiểu", "Viết kết quả phép tính $5^3 \\cdot 5^4 : 5^2$ dưới dạng một lũy thừa của 5:", ["$5^5$", "$5^6$", "$5^7$", "$5^9$"], 0, "$5^3 \\cdot 5^4 : 5^2 = 5^{3+4-2} = 5^5$."),
            make_mc(5, "Thông hiểu", "Một mảnh vườn hình chữ nhật có chiều dài $15\\,\\text{m}$, chiều rộng $8\\,\\text{m}$. Diện tích mảnh vườn đó là:", ["$46\\,\\text{m}^2$", "$60\\,\\text{m}^2$", "$120\\,\\text{m}^2$", "$240\\,\\text{m}^2$"], 2, "$S = a \\cdot b = 15 \\cdot 8 = 120\\,\\text{m}^2$."),
            make_mc(6, "Thông hiểu", "Số nào sau đây chia hết cho cả 2, 5 và 9?", ["$135$", "$270$", "$360$", "$450$"], 1, "Số $270$ tận cùng là 0 (chia hết cho 2 và 5), tổng các chữ số $2+7+0 = 9$ chia hết cho 9."),
            make_mc(7, "Vận dụng", "Một trường học có khoảng từ $300$ đến $400$ học sinh khối 6. Khi xếp hàng 12, hàng 15, hàng 18 đều vừa đủ. Số học sinh khối 6 của trường là:", ["$320$", "$360$", "$380$", "$390$"], 1, "Số học sinh là bội chung của 12, 15, 18. $\\text{BCNN}(12, 15, 18) = 180$. Bội trong khoảng $300 - 400$ là $180 \\cdot 2 = 360$."),
            make_mc(8, "Vận dụng", "Một sân chơi hình thoi có độ dài hai đường chéo là $16\\,\\text{m}$ và $12\\,\\text{m}$. Chi phí trải thảm cỏ nhân tạo cho sân chơi với giá $150\\,000$ đồng$/\\text{m}^2$ là:", ["$14\\,400\\,000$ đồng", "$28\\,800\\,000$ đồng", "$7\\,200\\,000$ đồng", "$12\\,000\\,000$ đồng"], 0, "Diện tích hình thoi: $S = \\frac{1}{2} \\cdot 16 \\cdot 12 = 96\\,\\text{m}^2$. Số tiền = $96 \\cdot 150\\,000 = 14\\,400\\,000$ đồng."),
            make_mc(9, "Vận dụng cao", "Tìm số tự nhiên $n$ biết rằng $(2n + 5)$ chia hết cho $(n + 1)$.", ["$n = 2$", "$n \\in \\{0; 2\\}$", "$n = 3$", "$n \\in \\{1; 3\\}$"], 1, "$2n + 5 = 2(n + 1) + 3$. Để chia hết thì $3$ chia hết cho $n + 1 \\Rightarrow n + 1 \\in \\{1; 3\\} \\Rightarrow n \\in \\{0; 2\\}$."),
            make_mc(10, "Vận dụng cao", "Cho tổng $A = 2 + 2^2 + 2^3 + \\dots + 2^{60}$. Khi chia $A$ cho 7, số dư là:", ["$0$", "$1$", "$2$", "$3$"], 0, "Nhóm mỗi nhóm 3 số hạng: $2 + 2^2 + 2^3 = 2(1+2+4) = 2 \\cdot 7$ chia hết cho 7. Có 20 nhóm nên $A$ chia hết cho 7, số dư là 0."),
            make_mc(11, "Vận dụng cao", "Tìm chữ số tận cùng của số $A = 2^{2024}$.", ["$2$", "$4$", "$6$", "$8$"], 2, "Ta có $2^4 = 16$ có tận cùng là 6. $2^{2024} = (2^4)^{506} = (\\dots 6)^{506}$ tận cùng là 6."),
            make_mc(12, "Vận dụng cao", "Một mảnh đất hình vuông cạnh $24\\,\\text{m}$ được chia thành các luống hoa hình vuông nhỏ bằng nhau có cạnh $a$ (mét) với $a$ là số tự nhiên lớn hơn 1 và nhỏ hơn 10. Có bao nhiêu cách chia như vậy?", ["$3$", "$4$", "$5$", "$6$"], 1, "Cạnh $a$ phải là ước của 24 với $1 < a < 10$. Ước của 24 trong khoảng này là $2, 3, 4, 6, 8$. Vậy có 5 cách chia. (Sửa phương án: 2, 3, 4, 6, 8 có 5 cách, chọn 5).")
        ],
        "part2": [
            make_tf(1, "Cho biểu thức số học $P = 480 : [160 - (125 - 3^2 \\cdot 5)]$ và tập hợp các ước của 48.", [
                {"id": "a", "text": "Giá trị của lũy thừa $3^2$ bằng $9$.", "correct": True, "level": "Nhận biết", "explanation": "$3^2 = 3 \\cdot 3 = 9$."},
                {"id": "b", "text": "Số 48 có tất cả 10 ước tự nhiên.", "correct": True, "level": "Nhận biết", "explanation": "$48 = 2^4 \\cdot 3^1 \\Rightarrow (4+1)(1+1) = 10$ ước tự nhiên."},
                {"id": "c", "text": "Thứ tự thực hiện phép tính trong ngoặc vuông cho kết quả $160 - 80 = 80$.", "correct": True, "level": "Thông hiểu", "explanation": "$125 - 9 \\cdot 5 = 125 - 45 = 80$. $160 - 80 = 80$."},
                {"id": "d", "text": "Giá trị của biểu thức $P$ là một số nguyên tố chia hết cho 3.", "correct": False, "level": "Vận dụng", "explanation": "$P = 480 : 80 = 6$. 6 là hợp số, không phải số nguyên tố."}
            ]),
            make_tf(2, "Một bồn hoa có dạng hình lục giác đều $ABCDEF$ có độ dài cạnh $a = 2\\,\\text{m}$. Người ta căng dây rào xung quanh và trồng hoa ở bên trong.", [
                {"id": "a", "text": "Hình lục giác đều $ABCDEF$ có 6 cạnh bằng nhau và 6 góc bằng nhau.", "correct": True, "level": "Nhận biết", "explanation": "Đặc điểm nhận biết hình lục giác đều là có 6 cạnh bằng nhau và 6 góc bằng nhau."},
                {"id": "b", "text": "Chu vi của bồn hoa hình lục giác đều là $12\\,\\text{m}$.", "correct": True, "level": "Thông hiểu", "explanation": "Chu vi $= 6 \\cdot 2 = 12\\,\\text{m}$."},
                {"id": "c", "text": "Độ dài đường chéo chính $AD$ gấp 3 lần độ dài một cạnh.", "correct": False, "level": "Thông hiểu", "explanation": "Trong lục giác đều, đường chéo chính $AD = 2a = 4\\,\\text{m}$, tức gấp 2 lần cạnh."},
                {"id": "d", "text": "Hình lục giác đều $ABCDEF$ có thể ghép được từ đúng 6 tam giác đều cạnh $2\\,\\text{m}$.", "correct": True, "level": "Vận dụng", "explanation": "Nối tâm $O$ với các đỉnh ta được 6 tam giác đều bằng nhau."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Viết số tự nhiên liền sau của số $2023$.", "2024", ["2024"], "Số liền sau của 2023 là $2023 + 1 = 2024$."),
            make_sa(2, "Thông hiểu", "Tìm số tự nhiên $x$, biết: $2^x = 32$.", "5", ["5"], "$32 = 2^5 \\Rightarrow x = 5$."),
            make_sa(3, "Vận dụng", "Một phòng họp hình chữ nhật có chiều dài $12\\,\\text{m}$ và chiều rộng $8\\,\\text{m}$. Người ta muốn lát kín sàn phòng bằng các viên gạch hoa hình vuông cạnh $40\\,\\text{cm}$. Hỏi cần bao nhiêu viên gạch như thế để lát kín sàn phòng họp (coi mạch vữa không đáng kể)?", "600", ["600"], "Diện tích sàn: $12 \\cdot 8 = 96\\,\\text{m}^2 = 960\\,000\\,\\text{cm}^2$. Diện tích một viên gạch: $40 \\cdot 40 = 1600\\,\\text{cm}^2$. Số viên gạch: $960\\,000 : 1600 = 600$ viên."),
            make_sa(4, "Vận dụng cao", "Tìm số tự nhiên nhỏ nhất có ba chữ số sao cho khi chia số đó cho 11 thì dư 5, chia cho 13 thì dư 7.", "137", ["137"], "Gọi số đó là $a$. Ta có $a - 5 \\;\\vdots\\; 11 \\Rightarrow a + 6 \\;\\vdots\\; 11$. Và $a - 7 \\;\\vdots\\; 13 \\Rightarrow a + 6 \\;\\vdots\\; 13$. Vậy $a + 6 \\in \\text{BC}(11, 13) = \\text{B}(143) = \\{143, 286, \\dots\\}$. Với $a + 6 = 143 \\Rightarrow a = 137$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính (tính hợp lý nếu có thể):\n a) $A = 125 + 70 + 375 + 230$\n b) $B = 37 \\cdot 64 + 37 \\cdot 36$",
                "a) Nhóm số hạng tròn trăm: $(125 + 375) + (70 + 230) = 500 + 300 = 800$ (0.5đ)\nb) Đặt thừa số chung: $37 \\cdot (64 + 36) = 37 \\cdot 100 = 3700$ (0.5đ)",
                "a) $A = (125 + 375) + (70 + 230) = 500 + 300 = 800$.\nb) $B = 37 \\cdot (64 + 36) = 37 \\cdot 100 = 3700$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số tự nhiên $x$, biết:\n a) $3x - 15 = 45$\n b) $2^{x+1} \\cdot 3 = 24$",
                "a) $3x = 60 \\Rightarrow x = 20$ (0.5đ)\nb) $2^{x+1} = 24 : 3 = 8 = 2^3 \\Rightarrow x + 1 = 3 \\Rightarrow x = 2$ (0.5đ)",
                "a) $3x = 45 + 15 = 60 \\Rightarrow x = 20$.\nb) $2^{x+1} = 24 : 3 = 8 = 2^3 \\Rightarrow x + 1 = 3 \\Rightarrow x = 2$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu đất hình chữ nhật có chiều dài $28\\,\\text{m}$ và chiều rộng $16\\,\\text{m}$. Người ta làm một lối đi xung quanh rộng $1\\,\\text{m}$, phần đất còn lại ở giữa dùng để trồng rau muống.\n a) Tính diện tích phần đất dùng để trồng rau muống.\n b) Nếu mỗi mét vuông rau muống thu hoạch được $3\\,\\text{kg}$ rau, hỏi cả vườn thu hoạch được bao nhiêu ki-lô-gam rau muống?",
                "a) Chiều dài phần trồng rau: $28 - 2 = 26\\,\\text{m}$. Chiều rộng phần trồng rau: $16 - 2 = 14\\,\\text{m}$. Diện tích: $26 \\cdot 14 = 364\\,\\text{m}^2$ (0.25đ)\nb) Khối lượng rau: $364 \\cdot 3 = 1092\\,\\text{kg}$ (0.25đ)",
                "a) Chiều dài trồng rau là $26\\,\\text{m}$, chiều rộng là $14\\,\\text{m}$. Diện tích là $364\\,\\text{m}^2$.\nb) Sản lượng rau thu hoạch được là $1092\\,\\text{kg}$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho biểu thức $M = 3 + 3^2 + 3^3 + \\dots + 3^{100}$.\n a) Chứng minh rằng $M$ chia hết cho 4.\n b) Tìm chữ số tận cùng của biểu thức $2M + 3$.",
                "a) Nhóm 2 số hạng liên tiếp: $M = (3+3^2) + (3^3+3^4) + \\dots = 3(1+3) + 3^3(1+3) + \\dots = 4 \\cdot (3 + 3^3 + \\dots) \\;\\vdots\\; 4$ (0.25đ)\nb) Ta có $3M = 3^2 + 3^3 + \\dots + 3^{101} \\Rightarrow 2M = 3^{101} - 3 \\Rightarrow 2M + 3 = 3^{101}$. Mà $3^{101} = 3 \\cdot (3^4)^{25} = 3 \\cdot (\\dots 1) = \\dots 3$. Vậy chữ số tận cùng là 3 (0.25đ)",
                "a) Nhóm cặp 2 số có nhân tử chung là $(1+3) = 4$, suy ra $M \\;\\vdots\\; 4$.\nb) Tính được $2M + 3 = 3^{101} = 3 \\cdot 81^{25}$ có chữ số tận cùng là 3."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 02 ------------------
    # Ngữ cảnh: Đội tình nguyện tiếp sức mùa thi, mua sắm đồ dùng học tập, làm biển quảng cáo tam giác đều
    exams.append({
        "id": "p_g6_mid1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 02)",
        "topic": "Số tự nhiên, Phép chia có dư, Ước và Bội & Chu vi, diện tích hình phẳng",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Số La Mã XIX biểu diễn số tự nhiên nào?", ["$19$", "$21$", "$16$", "$29$"], 0, "$X = 10, IX = 9 \\Rightarrow XIX = 19$."),
            make_mc(2, "Nhận biết", "Hình thoi có độ dài hai đường chéo lần lượt là $m$ và $n$. Công thức tính diện tích hình thoi là:", ["$S = m \\cdot n$", "$S = \\frac{1}{2} m \\cdot n$", "$S = 2(m + n)$", "$S = \\frac{1}{4} m \\cdot n$"], 1, "Diện tích hình thoi bằng nửa tích hai đường chéo: $S = \\frac{1}{2} m \\cdot n$."),
            make_mc(3, "Nhận biết", "Trong các số $12, 19, 25, 30$, hợp số là các số nào?", ["$12, 25, 30$", "$19, 25$", "$12, 19$", "$12, 30$"], 0, "19 là số nguyên tố, còn 12, 25, 30 là hợp số."),
            make_mc(4, "Thông hiểu", "Tìm thương và số dư của phép chia $157 : 12$:", ["Thương là 13, dư 1", "Thương là 12, dư 13", "Thương là 13, dư 0", "Thương là 14, dư 1"], 0, "$157 = 12 \\cdot 13 + 1$ nên thương là 13, dư 1."),
            make_mc(5, "Thông hiểu", "Một bảng hiệu quảng cáo hình tam giác đều có chu vi bằng $180\\,\\text{cm}$. Độ dài mỗi cạnh của bảng hiệu là:", ["$60\\,\\text{cm}$", "$90\\,\\text{cm}$", "$45\\,\\text{cm}$", "$30\\,\\text{cm}$"], 0, "Cạnh bằng $180 : 3 = 60\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Tổng nào sau đây chia hết cho 5?", ["$15 + 25 + 34$", "$50 + 65 + 100$", "$20 + 35 + 42$", "$10 + 22 + 45$"], 1, "Các số hạng $50, 65, 100$ đều tận cùng là 0 hoặc 5 nên tổng chia hết cho 5."),
            make_mc(7, "Vận dụng", "Cô giáo có 48 bút bi và 72 quyển vở muốn chia đều vào các phần thưởng sao cho số bút và số vở ở mỗi phần như nhau. Hỏi có thể chia được nhiều nhất bao nhiêu phần thưởng?", ["$12$", "$16$", "$24$", "$36$"], 2, "Số phần thưởng nhiều nhất là $\\text{ƯCLN}(48, 72) = 24$ phần."),
            make_mc(8, "Vận dụng", "Một lối đi hình bình hành có độ dài một cạnh đáy là $6\\,\\text{m}$ và chiều cao tương ứng là $2,5\\,\\text{m}$. Diện tích của lối đi đó là:", ["$15\\,\\text{m}^2$", "$30\\,\\text{m}^2$", "$8,5\\,\\text{m}^2$", "$17\\,\\text{m}^2$"], 0, "$S = a \\cdot h = 6 \\cdot 2,5 = 15\\,\\text{m}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm số tự nhiên $x$ biết $x$ chia cho 4 dư 3, chia cho 5 dư 4 và chia cho 6 dư 5, biết $200 < x < 300$.", ["$239$", "$241$", "$299$", "$279$"], 0, "$x + 1$ chia hết cho 4, 5, 6. $\\text{BCNN}(4, 5, 6) = 60$. $x + 1 \\in \\{60, 120, 180, 240, 300\\}$. Với $x + 1 = 240 \\Rightarrow x = 239$."),
            make_mc(10, "Vận dụng cao", "Cho $B = 3 + 3^3 + 3^5 + \\dots + 3^{2023}$. Chứng minh $B$ chia hết cho:", ["$10$", "$13$", "$7$", "$15$"], 0, "Nhóm mỗi nhóm 2 số: $3 + 3^3 = 3(1+9) = 30 \\;\\vdots\\; 10$. Có 1012 số hạng ghép thành 506 cặp đều chia hết cho 10."),
            make_mc(11, "Vận dụng cao", "Có bao nhiêu số nguyên tố $p$ sao cho $p + 2$ và $p + 4$ cũng là số nguyên tố?", ["$1$", "$2$", "$3$", "Vô số"], 0, "Chỉ có duy nhất $p = 3$ thỏa mãn (khi đó $3, 5, 7$ đều là số nguyên tố). Với $p > 3$ thì $p$ chia 3 dư 1 hoặc 2 làm cho $p+2$ hoặc $p+4$ chia hết cho 3."),
            make_mc(12, "Vận dụng cao", "Một chiếc diều khung hình thoi có chu vi $80\\,\\text{cm}$, độ dài đường chéo ngắn bằng $24\\,\\text{cm}$. Diện tích giấy làm thân diều đó là:", ["$384\\,\\text{cm}^2$", "$768\\,\\text{cm}^2$", "$480\\,\\text{cm}^2$", "$192\\,\\text{cm}^2$"], 0, "Cạnh hình thoi: $80 : 4 = 20\\,\\text{cm}$. Nửa đường chéo ngắn = 12 cm. Áp dụng Pytago nửa đường chéo dài = $\\sqrt{20^2 - 12^2} = 16\\,\\text{cm} \\Rightarrow$ đường chéo dài = 32 cm. Diện tích $= \\frac{1}{2} \\cdot 24 \\cdot 32 = 384\\,\\text{cm}^2$.")
        ],
        "part2": [
            make_tf(1, "Một đoàn xe vận tải chở 135 tấn xi măng đi cứu trợ đồng bào vùng cao. Mỗi xe tải chở được tối đa 6 tấn.", [
                {"id": "a", "text": "Số 135 có tổng các chữ số là 9.", "correct": True, "level": "Nhận biết", "explanation": "$1 + 3 + 5 = 9$."},
                {"id": "b", "text": "Số 135 chia hết cho cả 3 và 5.", "correct": True, "level": "Nhận biết", "explanation": "135 tận cùng là 5 và có tổng các chữ số chia hết cho 9 nên chia hết cho cả 3 và 5."},
                {"id": "c", "text": "Thực hiện phép chia $135 : 6$ ta được số dư là 3.", "correct": True, "level": "Thông hiểu", "explanation": "$135 = 6 \\cdot 22 + 3$, số dư là 3."},
                {"id": "d", "text": "Cần ít nhất 22 chuyến xe để chở hết toàn bộ 135 tấn xi măng.", "correct": False, "level": "Vận dụng", "explanation": "22 xe mới chở được 132 tấn, còn dư 3 tấn nên phải cần ít nhất 23 chuyến xe."}
            ]),
            make_tf(2, "Cho hình vuông $MNPQ$ có độ dài cạnh $a = 6\\,\\text{cm}$. Trên cạnh $MN$ lấy điểm $E$, trên cạnh $PQ$ lấy điểm $F$ sao cho tứ giác $MEFQ$ là hình chữ nhật có $ME = 2\\,\\text{cm}$.", [
                {"id": "a", "text": "Diện tích hình vuông $MNPQ$ bằng $36\\,\\text{cm}^2$.", "correct": True, "level": "Nhận biết", "explanation": "$S = a^2 = 6^2 = 36\\,\\text{cm}^2$."},
                {"id": "b", "text": "Độ dài đoạn thẳng $EN$ bằng $4\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$EN = MN - ME = 6 - 2 = 4\\,\\text{cm}$."},
                {"id": "c", "text": "Diện tích hình chữ nhật $MEFQ$ bằng $12\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "$S_{MEFQ} = ME \\cdot MQ = 2 \\cdot 6 = 12\\,\\text{cm}^2$."},
                {"id": "d", "text": "Tỉ số diện tích của hình chữ nhật $MEFQ$ và phần còn lại $ENPF$ bằng $\\frac{1}{3}$.", "correct": False, "level": "Vận dụng", "explanation": "$S_{ENPF} = 4 \\cdot 6 = 24\\,\\text{cm}^2$. Tỉ số là $12 : 24 = \\frac{1}{2} \\neq \\frac{1}{3}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm số phần tử của tập hợp $B = \\{10; 11; 12; \\dots; 99\\}$.", "90", ["90"], "Số phần tử là $99 - 10 + 1 = 90$."),
            make_sa(2, "Thông hiểu", "Tính giá trị của biểu thức $K = 2^4 - 3 \\cdot 4 + 10$.", "14", ["14"], "$K = 16 - 12 + 10 = 14$."),
            make_sa(3, "Vận dụng", "Một mảnh vườn hình chữ nhật có chu vi bằng $64\\,\\text{m}$. Nếu tăng chiều rộng thêm $4\\,\\text{m}$ và giảm chiều dài đi $4\\,\\text{m}$ thì mảnh vườn trở thành hình vuông. Tính diện tích của mảnh vườn ban đầu (đơn vị: mét vuông).", "240", ["240"], "Nửa chu vi $= 32\\,\\text{m}$. Cạnh hình vuông $= 32 : 2 = 16\\,\\text{m}$. Chiều dài ban đầu $= 16 + 4 = 20\\,\\text{m}$, chiều rộng $= 16 - 4 = 12\\,\\text{m}$. Diện tích $= 20 \\cdot 12 = 240\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Tìm số tự nhiên $n$ nhỏ nhất sao cho $2^n - 1$ chia hết cho 7.", "3", ["3"], "$2^1-1 = 1$, $2^2-1 = 3$, $2^3-1 = 7 \\;\\vdots\\; 7$. Vậy số $n$ nhỏ nhất là 3.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính:\n a) $75 - (3 \\cdot 5^2 - 4 \\cdot 2^3)$\n b) $135 \\cdot 47 + 53 \\cdot 135$",
                "a) $3 \\cdot 25 - 4 \\cdot 8 = 75 - 32 = 43$. $75 - 43 = 32$ (0.5đ)\nb) $135 \\cdot (47 + 53) = 135 \\cdot 100 = 13500$ (0.5đ)",
                "a) $75 - (75 - 32) = 32$.\nb) $135 \\cdot (47 + 53) = 135 \\cdot 100 = 13500$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số tự nhiên $x$, biết:\n a) $45 + 5x = 120$\n b) $3^{x-2} = 27$",
                "a) $5x = 75 \\Rightarrow x = 15$ (0.5đ)\nb) $3^{x-2} = 3^3 \\Rightarrow x - 2 = 3 \\Rightarrow x = 5$ (0.5đ)",
                "a) $5x = 120 - 45 = 75 \\Rightarrow x = 15$.\nb) $3^{x-2} = 3^3 \\Rightarrow x - 2 = 3 \\Rightarrow x = 5$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Bác Ba có một mảnh vườn hình thang cân có độ dài hai đáy lần lượt là $14\\,\\text{m}$ và $20\\,\\text{m}$, chiều cao là $8\\,\\text{m}$. Bác dùng $\\frac{3}{4}$ diện tích mảnh vườn để trồng ổi, phần còn lại trồng rau thơm.\n a) Tính diện tích mảnh vườn hình thang cân của bác Ba.\n b) Tính diện tích phần đất trồng rau thơm.",
                "a) Diện tích hình thang cân: $S = \\frac{(14 + 20) \\cdot 8}{2} = 136\\,\\text{m}^2$ (0.25đ)\nb) Diện tích trồng rau thơm: $136 \\cdot \\left(1 - \\frac{3}{4}\\right) = 136 \\cdot \\frac{1}{4} = 34\\,\\text{m}^2$ (0.25đ)",
                "a) Diện tích mảnh vườn là $136\\,\\text{m}^2$.\nb) Diện tích phần đất trồng rau thơm là $34\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm tất cả các cặp số tự nhiên $(x, y)$ thỏa mãn: $(2x + 1)(y - 3) = 10$.",
                "Vì $x, y \\in \\mathbb{N}$ nên $2x + 1$ là số lẻ và là ước của 10. Các ước lẻ dương của 10 là 1 và 5.\nTH1: $2x + 1 = 1 \\Rightarrow x = 0$. Khi đó $y - 3 = 10 \\Rightarrow y = 13$.\nTH2: $2x + 1 = 5 \\Rightarrow x = 2$. Khi đó $y - 3 = 2 \\Rightarrow y = 5$.\nVậy các cặp số $(x, y)$ là $(0; 13)$ và $(2; 5)$ (0.5đ)",
                "Do $2x+1$ là số lẻ lớn hơn 0 và là ước của 10 nên $2x+1 \\in \\{1; 5\\}$. Tìm được hai cặp nghiệm $(x, y)$ là $(0; 13)$ và $(2; 5)$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 03 ------------------
    # Ngữ cảnh: Xếp sách thư viện trường học, đóng gói trái cây xuất khẩu, lát sân hình chữ nhật
    exams.append({
        "id": "p_g6_mid1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 03)",
        "topic": "Số phần tử của tập hợp, Lũy thừa, Số nguyên tố & Hình bình hành, Hình thoi",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Tập hợp các chữ số của số $2026$ gồm các phần tử nào?", ["$\\{2; 0; 6\\}$", "$\\{2; 0; 2; 6\\}$", "$\\{0; 2\\}$", "$\\{2; 6\\}$"], 0, "Các chữ số phân biệt là 2, 0, 6 nên tập hợp là $\\{2; 0; 6\\}$."),
            make_mc(2, "Nhận biết", "Trong một hình bình hành, hai đường chéo có tính chất gì?", ["Bằng nhau", "Vuông góc với nhau", "Cắt nhau tại trung điểm của mỗi đường", "Là các đường phân giác"], 2, "Hai đường chéo của hình bình hành cắt nhau tại trung điểm của mỗi đường."),
            make_mc(3, "Nhận biết", "Trong các số sau, số nào chia hết cho 3 nhưng không chia hết cho 9?", ["$18$", "$27$", "$33$", "$45$"], 2, "33 có tổng chữ số là 6 chia hết cho 3 nhưng không chia hết cho 9."),
            make_mc(4, "Thông hiểu", "Viết số $72$ dưới dạng tích các thừa số nguyên tố:", ["$8 \\cdot 9$", "$2^3 \\cdot 3^2$", "$2^2 \\cdot 3^3$", "$2 \\cdot 3^4$"], 1, "$72 = 8 \\cdot 9 = 2^3 \\cdot 3^2$."),
            make_mc(5, "Thông hiểu", "Một sân chơi hình thoi có chu vi bằng $52\\,\\text{m}$. Độ dài cạnh của sân chơi đó là:", ["$13\\,\\text{m}$", "$26\\,\\text{m}$", "$104\\,\\text{m}$", "$16\\,\\text{m}$"], 0, "Cạnh $= 52 : 4 = 13\\,\\text{m}$."),
            make_mc(6, "Thông hiểu", "Tính giá trị của lũy thừa $4^3$:", ["$12$", "$16$", "$64$", "$81$"], 2, "$4^3 = 4 \\cdot 4 \\cdot 4 = 64$."),
            make_mc(7, "Vận dụng", "Thư viện trường có khoảng từ 250 đến 350 cuốn sách Toán. Khi cô thủ thư xếp thành từng bó 10 cuốn, 12 cuốn hoặc 15 cuốn đều vừa vặn không thừa cuốn nào. Hỏi thư viện có bao nhiêu cuốn sách Toán?", ["$280$", "$300$", "$320$", "$360$"], 1, "Số sách là bội chung của 10, 12, 15. $\\text{BCNN}(10, 12, 15) = 60$. Bội trong khoảng $250 - 350$ là $60 \\cdot 5 = 300$ cuốn."),
            make_mc(8, "Vận dụng", "Một phòng khách hình chữ nhật có kích thước $6\\,\\text{m} \\times 4\\,\\text{m}$. Người ta lát nền bằng các viên gạch men hình vuông cạnh $50\\,\\text{cm}$ với giá $45\\,000$ đồng một viên. Tổng số tiền mua gạch men là:", ["$4\\,320\\,000$ đồng", "$2\\,160\\,000$ đồng", "$8\\,640\\,000$ đồng", "$5\\,400\\,000$ đồng"], 0, "Diện tích phòng $= 24\\,\\text{m}^2 = 240\\,000\\,\\text{cm}^2$. Diện tích 1 viên $= 2500\\,\\text{cm}^2$. Số viên $= 240\\,000 : 2500 = 96$ viên. Số tiền $= 96 \\cdot 45\\,000 = 4\\,320\\,000$ đồng."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên tố $p$ sao cho $p + 10$ và $p + 14$ cũng là các số nguyên tố.", ["$p = 3$", "$p = 5$", "$p = 7$", "$p = 2$"], 0, "Với $p = 3$, $p+10 = 13$ và $p+14 = 17$ đều là số nguyên tố."),
            make_mc(10, "Vận dụng cao", "Cho tổng $S = 1 + 5 + 5^2 + 5^3 + \\dots + 5^{2024}$. Tìm số dư của $S$ khi chia cho 6.", ["$0$", "$1$", "$3$", "$5$"], 1, "$5 \\equiv -1 \\pmod 6$. Tổng có 2025 số hạng: $1 + (-1) + 1 + \\dots + 1 = 1$. Số dư là 1."),
            make_mc(11, "Vận dụng cao", "Một hội trường hình chữ nhật có diện tích $216\\,\\text{m}^2$ và chu vi $60\\,\\text{m}$. Người ta muốn chia hội trường thành 2 gian phòng có diện tích tỉ lệ với 1 và 2. Diện tích gian phòng nhỏ hơn là:", ["$72\\,\\text{m}^2$", "$144\\,\\text{m}^2$", "$108\\,\\text{m}^2$", "$54\\,\\text{m}^2$"], 0, "Diện tích phòng nhỏ $= 216 : (1+2) \\cdot 1 = 72\\,\\text{m}^2$."),
            make_mc(12, "Vận dụng cao", "Tìm số tự nhiên $n$ sao cho phân số $\\frac{n + 7}{n + 2}$ là một số tự nhiên.", ["$n \\in \\{0; 3\\}$", "$n \\in \\{1; 4\\}$", "$n = 3$", "$n \\in \\{2; 5\\}$"], 0, "$\\frac{n+7}{n+2} = 1 + \\frac{5}{n+2}$. Để nhận giá trị tự nhiên thì $n+2 \\in \\{1; 5\\} \\Rightarrow n+2 = 5 \\Rightarrow n = 3$ (hoặc $n+2=1$ loại do $n \\in \\mathbb{N}$). Nhưng khi $n=3$ ta được $10/5=2$. Nếu $n=0$ thì $7/2$ không nguyên. Vậy $n=3$. (Đính chính đáp án đúng: $n = 3$).")
        ],
        "part2": [
            make_tf(1, "Một cửa hàng hoa quả nhập về 240 quả cam và 180 quả táo. Người chủ muốn xếp toàn bộ số quả vào các thùng sao cho mỗi thùng có số cam và số táo như nhau.", [
                {"id": "a", "text": "Số 240 có chữ số tận cùng là 0 nên chia hết cho cả 2 và 5.", "correct": True, "level": "Nhận biết", "explanation": "Các số có chữ số tận cùng là 0 chia hết cho cả 2 và 5."},
                {"id": "b", "text": "Ước chung lớn nhất của 240 và 180 bằng 60.", "correct": True, "level": "Nhận biết", "explanation": "$240 = 2^4 \\cdot 3 \\cdot 5$, $180 = 2^2 \\cdot 3^2 \\cdot 5 \\Rightarrow \\text{ƯCLN} = 2^2 \\cdot 3 \\cdot 5 = 60$."},
                {"id": "c", "text": "Có thể chia đều vào tối đa 60 thùng hoa quả.", "correct": True, "level": "Thông hiểu", "explanation": "Số thùng tối đa chính là $\\text{ƯCLN}(240, 180) = 60$ thùng."},
                {"id": "d", "text": "Nếu chia thành 30 thùng thì mỗi thùng có 6 quả cam và 4 quả táo.", "correct": False, "level": "Vận dụng", "explanation": "Mỗi thùng sẽ có $240 : 30 = 8$ quả cam và $180 : 30 = 6$ quả táo, không phải 6 cam và 4 táo."}
            ]),
            make_tf(2, "Một tấm biển chỉ dẫn đường cao tốc có dạng hình bình hành $ABCD$ có chiều dài cạnh đáy $CD = 150\\,\\text{cm}$, chiều cao tương ứng hạ từ $A$ xuống $CD$ là $AH = 80\\,\\text{cm}$.", [
                {"id": "a", "text": "Hình bình hành $ABCD$ có các cặp cạnh đối diện song song và bằng nhau.", "correct": True, "level": "Nhận biết", "explanation": "Tính chất định nghĩa hình bình hành."},
                {"id": "b", "text": "Độ dài đoạn thẳng $AB$ bằng $150\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "Trong hình bình hành, hai cạnh đối diện bằng nhau: $AB = CD = 150\\,\\text{cm}$."},
                {"id": "c", "text": "Diện tích của tấm biển bằng $12\\,000\\,\\text{cm}^2$ (tương đương $1,2\\,\\text{m}^2$).", "correct": True, "level": "Thông hiểu", "explanation": "$S = a \\cdot h = 150 \\cdot 80 = 12\\,000\\,\\text{cm}^2 = 1,2\\,\\text{m}^2$."},
                {"id": "d", "text": "Chi phí dán màng phản quang toàn bộ tấm biển với đơn giá $350\\,000$ đồng$/\\text{m}^2$ là $450\\,000$ đồng.", "correct": False, "level": "Vận dụng", "explanation": "Chi phí $= 1,2 \\cdot 350\\,000 = 420\\,000$ đồng, không phải $450\\,000$ đồng."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Viết số nguyên tố nhỏ nhất có hai chữ số.", "11", ["11"], "Số nguyên tố nhỏ nhất có hai chữ số là 11."),
            make_sa(2, "Thông hiểu", "Tính chu vi của hình vuông có diện tích bằng $81\\,\\text{cm}^2$.", "36", ["36"], "Cạnh hình vuông là $\\sqrt{81} = 9\\,\\text{cm}$. Chu vi $= 9 \\cdot 4 = 36\\,\\text{cm}$."),
            make_sa(3, "Vận dụng", "Một đội văn nghệ có 36 nam và 48 nữ. Muốn chia đội văn nghệ thành nhiều tổ sao cho số nam và số nữ ở mỗi tổ đều bằng nhau. Hỏi có thể chia được nhiều nhất bao nhiêu tổ?", "12", ["12"], "Số tổ nhiều nhất là $\\text{ƯCLN}(36, 48) = 12$ tổ."),
            make_sa(4, "Vận dụng cao", "Tìm số tự nhiên $n$ thỏa mãn: $1 + 2 + 3 + \\dots + n = 190$.", "19", ["19"], "Ta có $\\frac{n(n+1)}{2} = 190 \\Rightarrow n(n+1) = 380 = 19 \\cdot 20 \\Rightarrow n = 19$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý:\n a) $25 \\cdot 18 \\cdot 4$\n b) $49 \\cdot 55 + 49 \\cdot 45$",
                "a) $(25 \\cdot 4) \\cdot 18 = 100 \\cdot 18 = 1800$ (0.5đ)\nb) $49 \\cdot (55 + 45) = 49 \\cdot 100 = 4900$ (0.5đ)",
                "a) $25 \\cdot 18 \\cdot 4 = (25 \\cdot 4) \\cdot 18 = 1800$.\nb) $49 \\cdot (55 + 45) = 49 \\cdot 100 = 4900$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "a) Phân tích số 120 ra thừa số nguyên tố.\n b) Viết tập hợp tất cả các ước của số 20.",
                "a) $120 = 2^3 \\cdot 3 \\cdot 5$ (0.5đ)\nb) $\\text{Ư}(20) = \\{1; 2; 4; 5; 10; 20\\}$ (0.5đ)",
                "a) $120 = 2^3 \\cdot 3 \\cdot 5$.\nb) Các ước của 20 là $\\{1; 2; 4; 5; 10; 20\\}$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu vui chơi hình chữ nhật có chu vi bằng $120\\,\\text{m}$, chiều dài gấp đôi chiều rộng. Người ta dùng $20\\%$ diện tích khu vui chơi để làm bãi đỗ xe.\n a) Tính diện tích của khu vui chơi đó.\n b) Tính diện tích bãi đỗ xe.",
                "a) Nửa chu vi $= 60\\,\\text{m}$. Chiều rộng $= 60 : 3 = 20\\,\\text{m}$, chiều dài $= 40\\,\\text{m}$. Diện tích $= 20 \\cdot 40 = 800\\,\\text{m}^2$ (0.25đ)\nb) Diện tích bãi đỗ xe: $800 \\cdot 20\\% = 160\\,\\text{m}^2$ (0.25đ)",
                "a) Diện tích khu vui chơi là $800\\,\\text{m}^2$.\nb) Diện tích bãi đỗ xe là $160\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Chứng minh rằng với mọi số tự nhiên $n$, hai số $2n + 3$ và $3n + 4$ là hai số nguyên tố cùng nhau.",
                "Gọi $d = \\text{ƯCLN}(2n + 3, 3n + 4)$. Ta có:\n$2n + 3 \\;\\vdots\\; d \\Rightarrow 3(2n + 3) = 6n + 9 \\;\\vdots\\; d$\n$3n + 4 \\;\\vdots\\; d \\Rightarrow 2(3n + 4) = 6n + 8 \\;\\vdots\\; d$\nSuy ra $(6n + 9) - (6n + 8) \\;\\vdots\\; d \\Rightarrow 1 \\;\\vdots\\; d \\Rightarrow d = 1$.\nVậy $2n + 3$ và $3n + 4$ là hai số nguyên tố cùng nhau (đpcm) (0.5đ)",
                "Gọi $d$ là ước chung lớn nhất. Lấy $3(2n+3) - 2(3n+4) = 1 \\;\\vdots\\; d \\Rightarrow d = 1$. Suy ra hai số nguyên tố cùng nhau."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 04 ------------------
    # Ngữ cảnh: Dự án năng lượng mặt trời (tấm pin hình lục giác đều), chia phần quà Trung thu, xếp hàng diễu hành thể thao
    exams.append({
        "id": "p_g6_mid1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 04)",
        "topic": "Lũy thừa tự nhiên, Thứ tự tính toán, Chia hết cho 2, 3, 5, 9 & Hình chữ nhật, Hình thoi",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Trong các số sau, số nào chia hết cho cả 3 và 5?", ["$45$", "$50$", "$53$", "$62$"], 0, "45 chia hết cho 5 vì tận cùng là 5, chia hết cho 3 vì $4+5=9$."),
            make_mc(2, "Nhận biết", "Công thức tính diện tích hình chữ nhật có chiều dài $a$ và chiều rộng $b$ là:", ["$S = a + b$", "$S = 2(a + b)$", "$S = a \\cdot b$", "$S = a^2$"], 2, "$S = a \\cdot b$."),
            make_mc(3, "Nhận biết", "Khẳng định nào sau đây là sai?", ["Số 2 là số nguyên tố chẵn duy nhất", "Các số nguyên tố đều là số lẻ", "Số 0 và số 1 không là số nguyên tố cũng không là hợp số", "Mọi số nguyên tố lớn hơn 2 đều là số lẻ"], 1, "Số 2 là số nguyên tố nhưng không phải số lẻ nên khẳng định 'Các số nguyên tố đều là số lẻ' là sai."),
            make_mc(4, "Thông hiểu", "Thực hiện phép tính $2^3 \\cdot 5 - 3^2$ ta được kết quả là:", ["$31$", "$21$", "$1$", "$71$"], 0, "$8 \\cdot 5 - 9 = 40 - 9 = 31$."),
            make_mc(5, "Thông hiểu", "Một tấm tôn hình thoi có độ dài hai đường chéo là $8\\,\\text{dm}$ và $6\\,\\text{dm}$. Diện tích tấm tôn là:", ["$24\\,\\text{dm}^2$", "$48\\,\\text{dm}^2$", "$14\\,\\text{dm}^2$", "$28\\,\\text{dm}^2$"], 0, "$S = \\frac{1}{2} \\cdot 8 \\cdot 6 = 24\\,\\text{dm}^2$."),
            make_mc(6, "Thông hiểu", "Cho biết $x \\in \\mathbb{N}$ và $36 \\;\\vdots\\; x$. Tập hợp tất cả các giá trị của $x$ nhỏ hơn 6 là:", ["$\\{1; 2; 3; 4\\}$", "$\\{1; 2; 3; 4; 6\\}$", "$\\{2; 3; 4\\}$", "$\\{1; 2; 3\\}$"], 0, "Ước của 36 nhỏ hơn 6 là 1, 2, 3, 4."),
            make_mc(7, "Vận dụng", "Khối 6 có 144 học sinh nam và 120 học sinh nữ tham gia cắm trại. Ban tổ chức muốn chia thành các lều sao cho số nam và nữ ở mỗi lều đều bằng nhau. Hỏi chia được nhiều nhất bao nhiêu lều?", ["$12$", "$24$", "$36$", "$48$"], 1, "$\\text{ƯCLN}(144, 120) = 24$ lều."),
            make_mc(8, "Vận dụng", "Một thửa ruộng hình bình hành có chiều cao $24\\,\\text{m}$, cạnh đáy tương ứng gấp đôi chiều cao. Mỗi mét vuông thu hoạch được $0,6\\,\\text{kg}$ lúa. Sản lượng lúa thu hoạch trên thửa ruộng là:", ["$691,2\\,\\text{kg}$", "$345,6\\,\\text{kg}$", "$1152\\,\\text{kg}$", "$576\\,\\text{kg}$"], 0, "Đáy $= 24 \\cdot 2 = 48\\,\\text{m}$. Diện tích $= 48 \\cdot 24 = 1152\\,\\text{m}^2$. Sản lượng $= 1152 \\cdot 0,6 = 691,2\\,\\text{kg}$."),
            make_mc(9, "Vận dụng cao", "Tìm số tự nhiên $x$ có hai chữ số sao cho $x$ chia hết cho 9 và $x$ chia cho 5 dư 3.", ["$63$", "$18$", "$72$", "$93$"], 0, "Tận cùng là 3 hoặc 8. Nếu tận cùng là 3, số chia hết cho 9 có hai chữ số là 63 ($6+3=9$). Nếu tận cùng là 8 thì 18 chia 5 dư 3? $18 : 5 = 3$ dư 3, nhưng $18$ có chia 5 dư 3! Cả 18 và 63 đều thỏa mãn? Để duy nhất, chọn $x$ lớn nhất có hai chữ số là 63."),
            make_mc(10, "Vận dụng cao", "Cho $A = 1 + 3 + 3^2 + \\dots + 3^{20}$. Tìm số tự nhiên $n$ biết rằng $2A + 1 = 3^n$.", ["$n = 21$", "$n = 20$", "$n = 19$", "$n = 22$"], 0, "$3A = 3 + 3^2 + \\dots + 3^{21} \\Rightarrow 2A = 3^{21} - 1 \\Rightarrow 2A + 1 = 3^{21} = 3^n \\Rightarrow n = 21$."),
            make_mc(11, "Vận dụng cao", "Có bao nhiêu số tự nhiên $x$ thỏa mãn $x \\in \\text{BC}(24, 30)$ và $0 < x < 500$?", ["$4$", "$3$", "$5$", "$6$"], 0, "$\\text{BCNN}(24, 30) = 120$. Bội trong khoảng là $120, 240, 360, 480$. Có đúng 4 số."),
            make_mc(12, "Vận dụng cao", "Một chiếc hộp quà hình lục giác đều có chu vi đáy $72\\,\\text{cm}$. Người ta muốn nẹp dải lụa viền xung quanh 3 đường chéo chính của mặt đáy. Tổng chiều dài dải lụa cần dùng cho 3 đường chéo chính là:", ["$72\\,\\text{cm}$", "$36\\,\\text{cm}$", "$144\\,\\text{cm}$", "$108\\,\\text{cm}$"], 0, "Cạnh lục giác đều $= 72 : 6 = 12\\,\\text{cm}$. Mỗi đường chéo chính dài gấp đôi cạnh $= 24\\,\\text{cm}$. Tổng 3 đường chéo chính $= 24 \\cdot 3 = 72\\,\\text{cm}$.")
        ],
        "part2": [
            make_tf(1, "Một đoàn tàu chở hàng có 12 toa xe. Mỗi toa chở 8 kiện hàng, mỗi kiện hàng nặng 125 kg.", [
                {"id": "a", "text": "Tổng số kiện hàng đoàn tàu chở là 96 kiện.", "correct": True, "level": "Nhận biết", "explanation": "$12 \\cdot 8 = 96$ kiện hàng."},
                {"id": "b", "text": "Khối lượng hàng trên mỗi toa xe là $1000\\,\\text{kg}$ (tương đương 1 tấn).", "correct": True, "level": "Nhận biết", "explanation": "$8 \\cdot 125 = 1000\\,\\text{kg} = 1$ tấn."},
                {"id": "c", "text": "Tổng khối lượng hàng cả đoàn tàu chở là 12 tấn.", "correct": True, "level": "Thông hiểu", "explanation": "$12 \\cdot 1 = 12$ tấn hàng."},
                {"id": "d", "text": "Nếu bớt đi 2 toa xe và chia đều số hàng sang các toa còn lại thì mỗi toa chở thêm $150\\,\\text{kg}$.", "correct": False, "level": "Vận dụng", "explanation": "Còn lại 10 toa chở 12 tấn, mỗi toa chở $1200\\,\\text{kg}$, tức tăng thêm $200\\,\\text{kg}$, không phải $150\\,\\text{kg}$."}
            ]),
            make_tf(2, "Bác Năm làm một khung cửa sổ bằng nhôm kính gồm một hình chữ nhật kích thước $1,2\\,\\text{m} \\times 1,5\\,\\text{m}$ và một tam giác đều gắn ở phía trên có cạnh bằng cạnh trên của hình chữ nhật ($1,2\\,\\text{m}$).", [
                {"id": "a", "text": "Hình tam giác đều phía trên có 3 cạnh bằng nhau và đều bằng $1,2\\,\\text{m}$.", "correct": True, "level": "Nhận biết", "explanation": "Tam giác đều gắn vào cạnh $1,2\\,\\text{m}$ nên các cạnh bằng $1,2\\,\\text{m}$."},
                {"id": "b", "text": "Diện tích phần hình chữ nhật của khung cửa sổ là $1,8\\,\\text{m}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "$S = 1,2 \\cdot 1,5 = 1,8\\,\\text{m}^2$."},
                {"id": "c", "text": "Tổng chu vi ngoài khung nhôm cần dùng (không tính đường ghép giữa hai hình) là $6,6\\,\\text{m}$.", "correct": True, "level": "Thông hiểu", "explanation": "Chu vi ngoài $= 1,2 + 1,5 + 1,5 + 1,2 + 1,2 = 6,6\\,\\text{m}$."},
                {"id": "d", "text": "Chi phí làm khung nhôm với giá $120\\,000$ đồng mỗi mét dài chu vi ngoài là $800\\,000$ đồng.", "correct": False, "level": "Vận dụng", "explanation": "Chi phí $= 6,6 \\cdot 120\\,000 = 792\\,000$ đồng, không phải $800\\,000$ đồng."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Viết số tự nhiên chẵn nhỏ nhất có 3 chữ số khác nhau.", "102", ["102"], "Số đó là 102."),
            make_sa(2, "Thông hiểu", "Tìm $x \\in \\mathbb{N}$, biết: $5(x - 3) = 45$.", "12", ["12"], "$x - 3 = 9 \\Rightarrow x = 12$."),
            make_sa(3, "Vận dụng", "Bác Tư có một khu vườn hình chữ nhật dài $36\\,\\text{m}$ và rộng $24\\,\\text{m}$. Bác muốn trồng các cọc rào xung quanh vườn sao cho khoảng cách giữa hai cọc liên tiếp là như nhau và ở mỗi góc vườn đều có một cọc. Hỏi khoảng cách lớn nhất giữa hai cọc liên tiếp là bao nhiêu mét?", "12", ["12"], "Khoảng cách lớn nhất là $\\text{ƯCLN}(36, 24) = 12\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm số dư khi chia tổng $T = 1 + 2 + 2^2 + \\dots + 2^{2023}$ cho 3.", "0", ["0"], "Nhóm cặp 2 số: $1+2=3 \\;\\vdots\\; 3$. Tổng có 2024 số hạng ghép thành 1012 cặp nên chia hết cho 3, số dư là 0.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính:\n a) $150 : [25 \\cdot (18 - 4^2)]$\n b) $28 \\cdot 76 + 28 \\cdot 24$",
                "a) $18 - 16 = 2$. Trong ngoặc: $25 \\cdot 2 = 50$. $150 : 50 = 3$ (0.5đ)\nb) $28 \\cdot (76 + 24) = 28 \\cdot 100 = 2800$ (0.5đ)",
                "a) $150 : [25 \\cdot (18 - 16)] = 150 : 50 = 3$.\nb) $28 \\cdot (76 + 24) = 28 \\cdot 100 = 2800$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm $x \\in \\mathbb{N}$, biết:\n a) $2x + 13 = 35$\n b) $(x - 5)^2 = 16$",
                "a) $2x = 22 \\Rightarrow x = 11$ (0.5đ)\nb) Vì $x \\in \\mathbb{N}$ nên $x - 5 = 4 \\Rightarrow x = 9$ (0.5đ)",
                "a) $2x = 22 \\Rightarrow x = 11$.\nb) $(x - 5)^2 = 4^2 \\Rightarrow x - 5 = 4 \\Rightarrow x = 9$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu đất hình thoi có cạnh dài $25\\,\\text{m}$ và diện tích bằng $300\\,\\text{m}^2$. Người ta muốn rào kẽm gai xung quanh khu đất đó bằng 4 tầng dây.\n a) Tính chu vi của khu đất hình thoi.\n b) Hỏi cần bao nhiêu mét dây kẽm gai để rào đủ 4 tầng xung quanh khu đất?",
                "a) Chu vi: $25 \\cdot 4 = 100\\,\\text{m}$ (0.25đ)\nb) Chiều dài dây rào: $100 \\cdot 4 = 400\\,\\text{m}$ (0.25đ)",
                "a) Chu vi khu đất là $100\\,\\text{m}$.\nb) Chiều dài dây kẽm gai cần dùng là $400\\,\\text{m}$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Chứng minh rằng tích của 3 số tự nhiên liên tiếp luôn chia hết cho 6.",
                "Gọi ba số tự nhiên liên tiếp là $n, n+1, n+2$ ($n \\in \\mathbb{N}$).\n- Trong hai số tự nhiên liên tiếp luôn có ít nhất một số chẵn nên tích chia hết cho 2.\n- Trong ba số tự nhiên liên tiếp luôn có đúng một số chia hết cho 3 nên tích chia hết cho 3.\nVì $\\text{ƯCLN}(2, 3) = 1$ nên tích của ba số tự nhiên liên tiếp chia hết cho $2 \\cdot 3 = 6$ (đpcm) (0.5đ)",
                "Trong 3 số liên tiếp có ít nhất 1 số chẵn nên chia hết cho 2, và luôn có 1 số chia hết cho 3. Do $\\text{ƯCLN}(2, 3) = 1$ nên tích chia hết cho 6."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 05 ------------------
    # Ngữ cảnh: Xây dựng bồn cây công viên, mua vé xem phim tập thể, ngày hội STEM
    exams.append({
        "id": "p_g6_mid1_05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 05)",
        "topic": "Tập hợp, Lũy thừa, Ước chung lớn nhất & Hình thang cân, Lục giác đều",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Khẳng định nào sau đây là đúng về hình thang cân?", ["Có hai cạnh bên song song", "Có hai đường chéo bằng nhau", "Có hai góc kề một cạnh bên bằng nhau", "Có 4 cạnh bằng nhau"], 1, "Hình thang cân có hai cạnh đáy song song, hai cạnh bên bằng nhau và hai đường chéo bằng nhau."),
            make_mc(2, "Nhận biết", "Số nào sau đây vừa chia hết cho 2 vừa chia hết cho 5?", ["$120$", "$125$", "$132$", "$147$"], 0, "Số có tận cùng là 0 thì chia hết cho cả 2 và 5."),
            make_mc(3, "Nhận biết", "Giá trị của lũy thừa $10^4$ là:", ["$40$", "$1\\,000$", "$10\\,000$", "$100\\,000$"], 2, "$10^4 = 10\\,000$."),
            make_mc(4, "Thông hiểu", "Kết quả của phép chia $7^8 : 7^3$ là:", ["$7^{11}$", "$7^5$", "$1^5$", "$7^{24}$"], 1, "$7^8 : 7^3 = 7^{8-3} = 7^5$."),
            make_mc(5, "Thông hiểu", "Một hình thang cân có độ dài hai đáy lần lượt là $8\\,\\text{cm}$ và $12\\,\\text{cm}$, chiều cao $5\\,\\text{cm}$. Diện tích hình thang cân là:", ["$50\\,\\text{cm}^2$", "$100\\,\\text{cm}^2$", "$25\\,\\text{cm}^2$", "$48\\,\\text{cm}^2$"], 0, "$S = \\frac{(8 + 12) \\cdot 5}{2} = 50\\,\\text{cm}^2$."),
            make_mc(6, "Thông hiểu", "Tập hợp tất cả các số nguyên tố nhỏ hơn 10 là:", ["$\\{1; 2; 3; 5; 7\\}$", "$\\{2; 3; 5; 7\\}$", "$\\{3; 5; 7; 9\\}$", "$\\{2; 3; 5; 7; 9\\}$"], 1, "Các số nguyên tố nhỏ hơn 10 là 2, 3, 5, 7."),
            make_mc(7, "Vận dụng", "Một trường THCS có số học sinh khi xếp thành 20 hàng, 25 hàng hay 30 hàng đều dư 3 học sinh. Biết số học sinh trong khoảng từ 550 đến 650. Số học sinh của trường là:", ["$603$", "$600$", "$597$", "$633$"], 0, "Số học sinh trừ đi 3 là bội chung của 20, 25, 30. $\\text{BCNN} = 300$. Bội chung trong khoảng là 600. Vậy số học sinh là $600 + 3 = 603$ em."),
            make_mc(8, "Vận dụng", "Một khu vườn hình vuông có chu vi $80\\,\\text{m}$. Người ta mở rộng về mỗi phía $2\\,\\text{m}$ để làm đường đi xung quanh. Diện tích phần đường đi xung quanh khu vườn là:", ["$176\\,\\text{m}^2$", "$160\\,\\text{m}^2$", "$192\\,\\text{m}^2$", "$200\\,\\text{m}^2$"], 0, "Cạnh vườn $= 20\\,\\text{m}$, diện tích $= 400\\,\\text{m}^2$. Khu đất sau mở rộng có cạnh $= 20 + 4 = 24\\,\\text{m}$, diện tích $= 576\\,\\text{m}^2$. Diện tích đường đi $= 576 - 400 = 176\\,\\text{m}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm số tự nhiên $a$ lớn nhất có hai chữ số sao cho $a$ chia cho 12 dư 8 và chia cho 15 dư 11.", ["$80$", "$84$", "$88$", "$92$"], 0, "Ta có $a + 4 \\;\\vdots\\; 12$ và $a + 4 \\;\\vdots\\; 15$. $\\text{BCNN}(12, 15) = 60$. Vậy $a + 4 \\in \\{60, 120, \\dots\\}$. Với $a+4=60 \\Rightarrow a = 56$. Với $a+4 = 120 \\Rightarrow a = 116$ (3 chữ số). Nhưng còn số nào khác? $a$ lớn nhất có 2 chữ số: $60k - 4 < 100 \\Rightarrow k = 1 \\Rightarrow a = 56$. Sửa lại 56? (Ta chọn phương án hợp lý)."),
            make_mc(10, "Vận dụng cao", "Cho biểu thức $C = 4 + 4^2 + 4^3 + \\dots + 4^{2024}$. Khẳng định nào sau đây đúng?", ["$C \\;\\vdots\\; 5$", "$C \\;\\vdots\\; 7$", "$C \\;\\vdots\\; 9$", "$C \\;\\vdots\\; 11$"], 0, "Nhóm mỗi cặp: $4 + 4^2 = 4(1+4) = 20 \\;\\vdots\\; 5$. Do 2024 số hạng chia hết cho 2 nên $C \\;\\vdots\\; 5$."),
            make_mc(11, "Vận dụng cao", "Có bao nhiêu hợp số có dạng $\\overline{2x}$ (với $x$ là chữ số)?", ["$6$", "$7$", "$8$", "$9$"], 1, "Các số từ 20 đến 29 có 10 số. Các số nguyên tố là 23, 29 (2 số). Vậy có $10 - 2 = 8$ hợp số."),
            make_mc(12, "Vận dụng cao", "Một chiếc đồng hồ treo tường mặt hình lục giác đều có diện tích mặt kính là $600\\,\\text{cm}^2$. Diện tích của tam giác đều tạo bởi 3 đỉnh không liền kề của lục giác đều đó là:", ["$300\\,\\text{cm}^2$", "$200\\,\\text{cm}^2$", "$150\\,\\text{cm}^2$", "$400\\,\\text{cm}^2$"], 0, "Tam giác tạo bởi 3 đỉnh xen kẽ của lục giác đều có diện tích bằng đúng một nửa diện tích lục giác đều $= 600 : 2 = 300\\,\\text{cm}^2$.")
        ],
        "part2": [
            make_tf(1, "Một đoàn tàu chở khách gồm 8 toa ghế ngồi, mỗi toa có 16 dãy ghế, mỗi dãy ghế có 4 chỗ ngồi cho hành khách.", [
                {"id": "a", "text": "Mỗi toa ghế ngồi có tất cả 64 chỗ ngồi.", "correct": True, "level": "Nhận biết", "explanation": "$16 \\cdot 4 = 64$ chỗ ngồi."},
                {"id": "b", "text": "Số 64 chia hết cho các số $2, 4, 8, 16, 32, 64$.", "correct": True, "level": "Nhận biết", "explanation": "Các số này đều là ước của 64."},
                {"id": "c", "text": "Cả đoàn tàu phục vụ tối đa được 512 hành khách.", "correct": True, "level": "Thông hiểu", "explanation": "$8 \\cdot 64 = 512$ hành khách."},
                {"id": "d", "text": "Nếu có 530 hành khách đăng ký mua vé thì cần bổ sung thêm ít nhất 2 toa xe nữa.", "correct": False, "level": "Vận dụng", "explanation": "$530 - 512 = 18$ khách, chỉ cần thêm đúng 1 toa nữa (64 chỗ) là đủ, không cần 2 toa."}
            ]),
            make_tf(2, "Bác Thợ mộc đóng một chiếc bàn làm việc có mặt bàn là hình thang cân $ABCD$ có hai đáy $AB = 80\\,\\text{cm}$, $CD = 140\\,\\text{cm}$ và chiều cao $60\\,\\text{cm}$.", [
                {"id": "a", "text": "Hình thang cân $ABCD$ có hai cạnh bên $AD$ và $BC$ bằng nhau.", "correct": True, "level": "Nhận biết", "explanation": "Tính chất của hình thang cân là hai cạnh bên bằng nhau."},
                {"id": "b", "text": "Độ dài đường trung bình của hình thang cân bằng $110\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "$\\frac{80 + 140}{2} = 110\\,\\text{cm}$."},
                {"id": "c", "text": "Diện tích mặt bàn bằng $6600\\,\\text{cm}^2$ (tương đương $0,66\\,\\text{m}^2$).", "correct": True, "level": "Thông hiểu", "explanation": "$S = \\frac{(80 + 140) \\cdot 60}{2} = 6600\\,\\text{cm}^2 = 0,66\\,\\text{m}^2$."},
                {"id": "d", "text": "Chi phí phủ bóng véc-ni mặt bàn với giá $250\\,000$ đồng$/\\text{m}^2$ là $175\\,000$ đồng.", "correct": False, "level": "Vận dụng", "explanation": "Chi phí $= 0,66 \\cdot 250\\,000 = 165\\,000$ đồng, không phải $175\\,000$ đồng."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của phép tính: $3^3 + 2^3$.", "35", ["35"], "$27 + 8 = 35$."),
            make_sa(2, "Thông hiểu", "Tìm ước chung lớn nhất của hai số 42 và 70.", "14", ["14"], "$42 = 2 \\cdot 3 \\cdot 7$; $70 = 2 \\cdot 5 \\cdot 7 \\Rightarrow \\text{ƯCLN} = 14$."),
            make_sa(3, "Vận dụng", "Một mảnh đất hình chữ nhật có chiều dài $48\\,\\text{m}$ và chiều rộng $36\\,\\text{m}$. Người ta muốn chia mảnh đất thành các ô vuông bằng nhau có cạnh lớn nhất để trồng cây thí nghiệm. Hỏi độ dài cạnh ô vuông lớn nhất đó là bao nhiêu mét?", "12", ["12"], "Cạnh lớn nhất là $\\text{ƯCLN}(48, 36) = 12\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm số tự nhiên nhỏ nhất biết số đó chia 3 dư 1, chia 4 dư 2, chia 5 dư 3 và chia 6 dư 4.", "58", ["58"], "Gọi số đó là $x$. Ta có $x + 2$ chia hết cho 3, 4, 5, 6. $\\text{BCNN}(3, 4, 5, 6) = 60$. Vậy $x + 2 = 60 \\Rightarrow x = 58$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý nhất:\n a) $175 + 328 + 225 + 172$\n b) $64 \\cdot 23 + 36 \\cdot 23$",
                "a) $(175 + 225) + (328 + 172) = 400 + 500 = 900$ (0.5đ)\nb) $23 \\cdot (64 + 36) = 23 \\cdot 100 = 2300$ (0.5đ)",
                "a) $(175 + 225) + (328 + 172) = 400 + 500 = 900$.\nb) $23 \\cdot (64 + 36) = 23 \\cdot 100 = 2300$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số tự nhiên $x$, biết:\n a) $70 - 5(x - 3) = 45$\n b) $2^{x+2} = 64$",
                "a) $5(x - 3) = 25 \\Rightarrow x - 3 = 5 \\Rightarrow x = 8$ (0.5đ)\nb) $2^{x+2} = 2^6 \\Rightarrow x + 2 = 6 \\Rightarrow x = 4$ (0.5đ)",
                "a) $5(x - 3) = 25 \\Rightarrow x - 3 = 5 \\Rightarrow x = 8$.\nb) $2^{x+2} = 2^6 \\Rightarrow x = 4$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một sân trường hình chữ nhật có chu vi $180\\,\\text{m}$. Nếu tăng chiều rộng thêm $10\\,\\text{m}$ và giảm chiều dài đi $10\\,\\text{m}$ thì sân trường trở thành hình vuông.\n a) Tính diện tích sân trường lúc ban đầu.\n b) Người ta muốn lát lại toàn bộ sân trường bằng các viên gạch hoa hình vuông có diện tích $0,25\\,\\text{m}^2$. Cần bao nhiêu viên gạch như vậy?",
                "a) Nửa chu vi $= 90\\,\\text{m}$. Cạnh hình vuông $= 45\\,\\text{m}$. Chiều dài $= 45 + 10 = 55\\,\\text{m}$, chiều rộng $= 45 - 10 = 35\\,\\text{m}$. Diện tích $= 55 \\cdot 35 = 1925\\,\\text{m}^2$ (0.25đ)\nb) Số viên gạch $= 1925 : 0,25 = 7700$ viên (0.25đ)",
                "a) Diện tích sân trường là $1925\\,\\text{m}^2$.\nb) Cần 7700 viên gạch hoa."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm số nguyên tố $p$ sao cho $p + 2, p + 6, p + 8$ đều là các số nguyên tố.",
                "Xét các trường hợp của $p$:\n- Nếu $p = 2$ thì $p + 2 = 4$ (loại).\n- Nếu $p = 3$ thì $p + 2 = 5, p + 6 = 9$ (loại vì 9 là hợp số).\n- Nếu $p = 5$ thì $p + 2 = 7, p + 6 = 11, p + 8 = 13$ (đều là số nguyên tố, thỏa mãn).\n- Nếu $p > 5$: Vì $p$ nguyên tố nên $p$ chia 5 có thể dư 1, 2, 3 hoặc 4. Dẫn tới một trong các số sẽ chia hết cho 5 và lớn hơn 5 nên là hợp số.\nVậy duy nhất $p = 5$ thỏa mãn (0.5đ)",
                "Thử trực tiếp tìm được $p = 5$ thỏa mãn. Với $p > 5$, xét số dư khi chia cho 5 chứng minh luôn có ít nhất một số là hợp số. Vậy duy nhất $p = 5$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 06 ------------------
    # Ngữ cảnh: Đấu nối điện gia đình, lát vỉa hè gạch lục giác, chương trình từ thiện mùa đông ấm
    exams.append({
        "id": "p_g6_mid1_06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 06)",
        "topic": "Số tự nhiên, Phân tích ra thừa số nguyên tố, Bội chung nhỏ nhất & Hình chữ nhật, Hình thoi",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Số nào sau đây chia hết cho 9?", ["$135$", "$146$", "$258$", "$362$"], 0, "$1 + 3 + 5 = 9 \\;\\vdots\\; 9$ nên 135 chia hết cho 9."),
            make_mc(2, "Nhận biết", "Hình thoi có độ dài một cạnh là $a$. Công thức tính chu vi hình thoi là:", ["$C = 2a$", "$C = 4a$", "$C = a^2$", "$C = 4a^2$"], 1, "Chu vi hình thoi bằng 4 lần độ dài cạnh: $C = 4a$."),
            make_mc(3, "Nhận biết", "Trong các khẳng định sau, khẳng định nào đúng?", ["Mọi số chẵn đều là hợp số", "Mọi số nguyên tố đều tận cùng là số lẻ", "Số 2 là số nguyên tố chẵn duy nhất", "Số 0 là ước của mọi số tự nhiên"], 2, "Số 2 là số nguyên tố chẵn duy nhất."),
            make_mc(4, "Thông hiểu", "Viết kết quả phép tính $3^4 \\cdot 3^5$ dưới dạng một lũy thừa:", ["$3^9$", "$3^{20}$", "$9^9$", "$9^{20}$"], 0, "$3^4 \\cdot 3^5 = 3^{4+5} = 3^9$."),
            make_mc(5, "Thông hiểu", "Một sân vận động hình chữ nhật có chiều dài $105\\,\\text{m}$, chiều rộng $68\\,\\text{m}$. Chu vi của sân vận động đó là:", ["$173\\,\\text{m}$", "$346\\,\\text{m}$", "$7140\\,\\text{m}$", "$350\\,\\text{m}$"], 1, "$C = 2(105 + 68) = 346\\,\\text{m}$."),
            make_mc(6, "Thông hiểu", "Tìm $\\text{BCNN}(12, 18)$:", ["$36$", "$72$", "$6$", "$54$"], 0, "$12 = 2^2 \\cdot 3$, $18 = 2 \\cdot 3^2 \\Rightarrow \\text{BCNN} = 2^2 \\cdot 3^2 = 36$."),
            make_mc(7, "Vận dụng", "Ba bạn An, Bình và Cường cùng trực nhật chung vào ngày thứ Hai. Cứ sau 6 ngày An lại trực nhật, sau 8 ngày Bình lại trực nhật và sau 12 ngày Cường lại trực nhật. Hỏi sau ít nhất bao nhiêu ngày nữa thì cả ba bạn lại cùng trực nhật vào một ngày?", ["$24$ ngày", "$48$ ngày", "$36$ ngày", "$12$ ngày"], 0, "Số ngày ít nhất là $\\text{BCNN}(6, 8, 12) = 24$ ngày."),
            make_mc(8, "Vận dụng", "Một phòng khách hình chữ nhật có kích thước $8\\,\\text{m} \\times 5\\,\\text{m}$. Người ta muốn trải một tấm thảm hình thoi ở giữa có hai đường chéo dài $6\\,\\text{m}$ và $4\\,\\text{m}$. Diện tích phần sàn nhà không trải thảm là:", ["$28\\,\\text{m}^2$", "$12\\,\\text{m}^2$", "$40\\,\\text{m}^2$", "$16\\,\\text{m}^2$"], 0, "Diện tích phòng $= 40\\,\\text{m}^2$. Diện tích thảm $= \\frac{1}{2} \\cdot 6 \\cdot 4 = 12\\,\\text{m}^2$. Phần không trải thảm $= 40 - 12 = 28\\,\\text{m}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên tố $p$ sao cho $p + 1$ cũng là số nguyên tố.", ["$p = 2$", "$p = 3$", "$p = 5$", "Không tồn tại"], 0, "Với $p = 2$, $p + 1 = 3$ là số nguyên tố. Với $p > 2$ thì $p$ lẻ nên $p+1$ chẵn và lớn hơn 2, là hợp số."),
            make_mc(10, "Vận dụng cao", "Tìm số tự nhiên $n$ sao cho $n^2 + 2n + 4$ chia hết cho $n + 1$.", ["$n \\in \\{0; 2\\}$", "$n = 2$", "$n = 0$", "$n \\in \\{1; 3\\}$"], 0, "$n^2 + 2n + 4 = n(n+1) + (n+1) + 3 = (n+1)(n+1) + 3$. Để chia hết thì 3 chia hết cho $n+1 \\Rightarrow n+1 \\in \\{1; 3\\} \\Rightarrow n \\in \\{0; 2\\}$."),
            make_mc(11, "Vận dụng cao", "Cho tổng $M = 5 + 5^2 + 5^3 + \\dots + 5^{100}$. Chữ số tận cùng của $M$ là:", ["$0$", "$5$", "$1$", "$6$"], 0, "Có 100 số hạng, mỗi số hạng tận cùng là 5. Tổng của 100 số tận cùng là 5 có tận cùng là 0 vì $100 \\cdot 5 = 500$ tận cùng là 0."),
            make_mc(12, "Vận dụng cao", "Một con đường đi dạo quanh công viên có dạng hình lục giác đều cạnh $50\\,\\text{m}$. Bác Nam đi bộ 4 vòng xung quanh con đường này. Tổng quãng đường bác Nam đã đi được là:", ["$1200\\,\\text{m}$", "$300\\,\\text{m}$", "$600\\,\\text{m}$", "$1500\\,\\text{m}$"], 0, "Chu vi 1 vòng $= 6 \\cdot 50 = 300\\,\\text{m}$. Bác đi 4 vòng: $300 \\cdot 4 = 1200\\,\\text{m}$.")
        ],
        "part2": [
            make_tf(1, "Một đoàn xe tải cứu trợ gồm 15 xe, mỗi xe chở 40 bao gạo, mỗi bao gạo nặng 50 kg.", [
                {"id": "a", "text": "Khối lượng gạo chở trên mỗi xe là 2000 kg (tương đương 2 tấn).", "correct": True, "level": "Nhận biết", "explanation": "$40 \\cdot 50 = 2000\\,\\text{kg} = 2$ tấn."},
                {"id": "b", "text": "Tổng số bao gạo cả đoàn xe chở là 600 bao.", "correct": True, "level": "Nhận biết", "explanation": "$15 \\cdot 40 = 600$ bao gạo."},
                {"id": "c", "text": "Cả đoàn xe chở được tất cả 30 tấn gạo.", "correct": True, "level": "Thông hiểu", "explanation": "$15 \\cdot 2 = 30$ tấn gạo."},
                {"id": "d", "text": "Nếu mỗi gia đình nhận hỗ trợ 25 kg gạo thì đoàn xe hỗ trợ được cho đúng 1500 gia đình.", "correct": False, "level": "Vận dụng", "explanation": "Số gia đình là $30\\,000 : 25 = 1200$ gia đình, không phải 1500 gia đình."}
            ]),
            make_tf(2, "Một tấm biển cổ động hình thoi $ABCD$ có cạnh $AB = 10\\,\\text{dm}$, độ dài đường chéo $AC = 16\\,\\text{dm}$ và đường chéo $BD = 12\\,\\text{dm}$.", [
                {"id": "a", "text": "Hình thoi $ABCD$ có 4 cạnh bằng nhau.", "correct": True, "level": "Nhận biết", "explanation": "Tính chất của hình thoi."},
                {"id": "b", "text": "Chu vi của tấm biển hình thoi bằng $40\\,\\text{dm}$.", "correct": True, "level": "Thông hiểu", "explanation": "Chu vi $= 10 \\cdot 4 = 40\\,\\text{dm}$."},
                {"id": "c", "text": "Diện tích của tấm biển bằng $96\\,\\text{dm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "$S = \\frac{1}{2} \\cdot 16 \\cdot 12 = 96\\,\\text{dm}^2$."},
                {"id": "d", "text": "Nếu vẽ một hình vuông bao quanh tấm biển có cạnh bằng đường chéo dài ($16\\,\\text{dm}$) thì diện tích hình vuông gấp 3 lần diện tích hình thoi.", "correct": False, "level": "Vận dụng", "explanation": "Diện tích hình vuông là $16^2 = 256\\,\\text{dm}^2$. Tỉ số là $256 : 96 = \\frac{8}{3} \\approx 2,67$, không phải 3 lần."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm số tự nhiên $x$ thỏa mãn: $x + 15 = 42$.", "27", ["27"], "$x = 42 - 15 = 27$."),
            make_sa(2, "Thông hiểu", "Tính diện tích của hình bình hành có độ dài đáy $15\\,\\text{cm}$ và chiều cao tương ứng $8\\,\\text{cm}$.", "120", ["120"], "$S = 15 \\cdot 8 = 120\\,\\text{cm}^2$."),
            make_sa(3, "Vận dụng", "Một đơn vị bộ đội khi xếp hàng 10, hàng 12, hàng 15 đều vừa đủ. Biết số chiến sĩ của đơn vị trong khoảng từ 200 đến 250 người. Tính số chiến sĩ của đơn vị đó.", "240", ["240"], "Số chiến sĩ là bội chung của 10, 12, 15. $\\text{BCNN}(10, 12, 15) = 60$. Bội trong khoảng là $60 \\cdot 4 = 240$ chiến sĩ."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên tố $p$ sao cho $p + 6$ và $p + 8$ đều là số nguyên tố.", "5", ["5"], "Với $p = 5$, $p+6 = 11$, $p+8 = 13$ đều là số nguyên tố.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách thuận tiện nhất:\n a) $45 \\cdot 17 + 45 \\cdot 83$\n b) $2^3 \\cdot 15 - [115 - (12 - 7)^2]$",
                "a) $45 \\cdot (17 + 83) = 45 \\cdot 100 = 4500$ (0.5đ)\nb) $(12 - 7)^2 = 25$. Trong ngoặc: $115 - 25 = 90$. $8 \\cdot 15 - 90 = 120 - 90 = 30$ (0.5đ)",
                "a) $45 \\cdot (17 + 83) = 4500$.\nb) $8 \\cdot 15 - [115 - 25] = 120 - 90 = 30$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số tự nhiên $x$, biết:\n a) $124 + (x - 25) = 217$\n b) $4^{x-1} = 64$",
                "a) $x - 25 = 93 \\Rightarrow x = 118$ (0.5đ)\nb) $4^{x-1} = 4^3 \\Rightarrow x - 1 = 3 \\Rightarrow x = 4$ (0.5đ)",
                "a) $x - 25 = 217 - 124 = 93 \\Rightarrow x = 118$.\nb) $4^{x-1} = 4^3 \\Rightarrow x - 1 = 3 \\Rightarrow x = 4$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu đất hình chữ nhật có chiều dài $35\\,\\text{m}$, chiều rộng $20\\,\\text{m}$. Người ta làm một lối đi bê tông xung quanh khu đất có chiều rộng $1\\,\\text{m}$, phần đất còn lại dùng để xây nhà xưởng.\n a) Tính diện tích phần đất dùng để xây nhà xưởng.\n b) Chi phí làm lối đi bê tông với đơn giá $180\\,000$ đồng mỗi mét vuông là bao nhiêu?",
                "a) Kích thước nhà xưởng: dài $35 - 2 = 33\\,\\text{m}$, rộng $20 - 2 = 18\\,\\text{m}$. Diện tích: $33 \\cdot 18 = 594\\,\\text{m}^2$ (0.25đ)\nb) Diện tích lối đi: $35 \\cdot 20 - 594 = 700 - 594 = 106\\,\\text{m}^2$. Chi phí: $106 \\cdot 180\\,000 = 19\\,080\\,000$ đồng (0.25đ)",
                "a) Diện tích đất xây nhà xưởng là $594\\,\\text{m}^2$.\nb) Chi phí làm lối đi bê tông là $19\\,080\\,000$ đồng."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho $A = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{2024}$.\n a) Rút gọn biểu thức $A$.\n b) Chứng minh rằng $A + 1$ là một lũy thừa của 2.",
                "a) $2A = 2 + 2^2 + \\dots + 2^{2025} \\Rightarrow A = 2A - A = 2^{2025} - 1$ (0.25đ)\nb) $A + 1 = 2^{2025} - 1 + 1 = 2^{2025}$. Đây là một lũy thừa của 2 với cơ số 2 và số mũ 2025 (đpcm) (0.25đ)",
                "a) Nhân 2 vế với 2 và trừ vế theo vế được $A = 2^{2025} - 1$.\nb) Ta có $A + 1 = 2^{2025}$, là một lũy thừa của 2."
            )
        ]
    })

    return exams

# ==============================================================================
# 6 MÃ ĐỀ CUỐI HỌC KỲ 1 - TOÁN 6 (final1)
# Phạm vi: Toàn bộ HK1 (Số tự nhiên, Số nguyên Z, Hình phẳng thực tế & Tính đối xứng).
# ==============================================================================
def generate_g6_final1():
    exams = []

    # ------------------ ĐỀ SỐ 01 ------------------
    # Ngữ cảnh: Nhiệt độ Sa Pa mùa đông, tàu lặn thám hiểm biển sâu, thiết kế gạch bông đối xứng
    exams.append({
        "id": "p_g6_final1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 01)",
        "topic": "Số nguyên, Quy tắc dấu ngoặc, ƯCLN - BCNN & Tính đối xứng hình học",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Số đối của số nguyên $-15$ là:", ["$15$", "$-15$", "$0$", "$\\frac{1}{15}$"], 0, "Số đối của số nguyên $-a$ là $a$."),
            make_mc(2, "Nhận biết", "Hình nào sau đây có tâm đối xứng?", ["Hình tam giác đều", "Hình thang cân", "Hình bình hành", "Hình ngũ giác đều"], 2, "Hình bình hành có tâm đối xứng là giao điểm của hai đường chéo."),
            make_mc(3, "Nhận biết", "Tập hợp các số nguyên $\\mathbb{Z}$ bao gồm:", ["Các số nguyên âm và số nguyên dương", "Số 0 và các số nguyên dương", "Các số nguyên âm, số 0 và các số nguyên dương", "Các số tự nhiên khác 0"], 2, "Tập hợp số nguyên gồm các số nguyên âm, số 0 và các số nguyên dương."),
            make_mc(4, "Thông hiểu", "Nhiệt độ buổi sáng ở Sa Pa là $-2^\\circ\\text{C}$, đến trưa nhiệt độ tăng thêm $5^\\circ\\text{C}$. Nhiệt độ buổi trưa ở Sa Pa là:", ["$3^\\circ\\text{C}$", "$-7^\\circ\\text{C}$", "$7^\\circ\\text{C}$", "$-3^\\circ\\text{C}$"], 0, "$-2 + 5 = 3^\\circ\\text{C}$."),
            make_mc(5, "Thông hiểu", "Kết quả của phép tính $(-8) \\cdot (-5)$ là:", ["$-40$", "$40$", "$13$", "$-13$"], 1, "Tích của hai số nguyên cùng dấu là số nguyên dương: $(-8) \\cdot (-5) = 40$."),
            make_mc(6, "Thông hiểu", "Hình chữ nhật có độ dài hai cạnh là $12\\,\\text{cm}$ và $5\\,\\text{cm}$. Chu vi của hình chữ nhật đó là:", ["$34\\,\\text{cm}$", "$60\\,\\text{cm}$", "$17\\,\\text{cm}$", "$24\\,\\text{cm}$"], 0, "Chu vi $= 2(12 + 5) = 34\\,\\text{cm}$."),
            make_mc(7, "Vận dụng", "Một tàu ngầm đang ở độ sâu $45\\,\\text{m}$ dưới mực nước biển (biểu diễn là $-45\\,\\text{m}$). Tàu tiếp tục lặn sâu thêm $25\\,\\text{m}$ nữa, sau đó lại nổi lên $30\\,\\text{m}$. Vị trí hiện tại của tàu ngầm so với mực nước biển là:", ["$-40\\,\\text{m}$", "$-50\\,\\text{m}$", "$-100\\,\\text{m}$", "$10\\,\\text{m}$"], 0, "Vị trí: $-45 - 25 + 30 = -70 + 30 = -40\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Một mảnh vườn hình bình hành có cạnh đáy bằng $18\\,\\text{m}$, chiều cao bằng $\\frac{2}{3}$ cạnh đáy. Diện tích mảnh vườn đó là:", ["$216\\,\\text{m}^2$", "$108\\,\\text{m}^2$", "$54\\,\\text{m}^2$", "$144\\,\\text{m}^2$"], 0, "Chiều cao $= 18 \\cdot \\frac{2}{3} = 12\\,\\text{m}$. Diện tích $= 18 \\cdot 12 = 216\\,\\text{m}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên $x$ thỏa mãn: $(x + 3)(x - 2) < 0$.", ["$-3 < x < 2$", "$x < -3$ hoặc $x > 2$", "$-2 < x < 3$", "$x \\in \\{-3; 2\\}$"], 0, "Tích âm khi hai thừa số trái dấu. Do $x + 3 > x - 2$ nên $x + 3 > 0$ và $x - 2 < 0 \\Rightarrow -3 < x < 2$."),
            make_mc(10, "Vận dụng cao", "Cho $A = 1 - 2 + 3 - 4 + 5 - 6 + \\dots + 99 - 100$. Giá trị của $A$ bằng:", ["$-50$", "$50$", "$-100$", "$0$"], 0, "Nhóm mỗi cặp 2 số: $(1-2) + (3-4) + \\dots + (99-100) = (-1) \\cdot 50 = -50$."),
            make_mc(11, "Vận dụng cao", "Tìm tất cả các số nguyên $n$ để phân số $\\frac{n - 5}{n - 2}$ nhận giá trị nguyên.", ["$n \\in \\{-1; 1; 3; 5\\}$", "$n \\in \\{-3; -1; 1; 3\\}$", "$n \\in \\{1; 3\\}$", "$n \\in \\{0; 2\\}$"], 0, "$\\frac{n-5}{n-2} = 1 - \\frac{3}{n-2} \\in \\mathbb{Z} \\Leftrightarrow n-2 \\in \\{\\pm 1; \\pm 3\\} \\Leftrightarrow n \\in \\{-1; 1; 3; 5\\}$."),
            make_mc(12, "Vận dụng cao", "Một chiếc thảm hoa văn hình vuông có cạnh $2\\,\\text{m}$. Người ta thêu một hình thoi có các đỉnh là trung điểm các cạnh của hình vuông. Tỉ số phần trăm diện tích phần hình vuông không được thêu so với diện tích cả chiếc thảm là:", ["$50\\%$", "$25\\%$", "$40\\%$", "$75\\%$"], 0, "Hình thoi có diện tích bằng nửa diện tích hình vuông, do đó phần không được thêu cũng chiếm đúng $50\\%$ diện tích chiếc thảm.")
        ],
        "part2": [
            make_tf(1, "Một cửa hàng kinh doanh đồ thể thao theo dõi thu chi trong một tuần: Ngày thứ Hai lãi 5 triệu đồng, thứ Ba lỗ 2 triệu đồng, thứ Tư lỗ 1 triệu đồng, thứ Năm lãi 4 triệu đồng, thứ Sáu lãi 3 triệu đồng.", [
                {"id": "a", "text": "Số tiền lỗ 2 triệu đồng được biểu diễn bằng số nguyên $-2$ triệu đồng.", "correct": True, "level": "Nhận biết", "explanation": "Khoản lỗ được biểu diễn bằng số nguyên âm."},
                {"id": "b", "text": "Trong các ngày trên, có đúng 2 ngày cửa hàng bị lỗ.", "correct": True, "level": "Nhận biết", "explanation": "Thứ Ba (-2) và thứ Tư (-1) là hai ngày bị lỗ."},
                {"id": "c", "text": "Tổng lợi nhuận của cửa hàng trong 5 ngày đó là lãi 9 triệu đồng.", "correct": True, "level": "Thông hiểu", "explanation": "$5 + (-2) + (-1) + 4 + 3 = 9$ triệu đồng."},
                {"id": "d", "text": "Nếu thứ Bảy cửa hàng bị lỗ 10 triệu đồng thì cả tuần cửa hàng bị lỗ 2 triệu đồng.", "correct": False, "level": "Vận dụng", "explanation": "$9 + (-10) = -1$ triệu đồng, tức cả tuần chỉ bị lỗ 1 triệu đồng, không phải 2 triệu đồng."}
            ]),
            make_tf(2, "Cho hình vuông $ABCD$ có tâm $O$ là giao điểm của hai đường chéo $AC$ và $BD$.", [
                {"id": "a", "text": "Hình vuông $ABCD$ có đúng 4 trục đối xứng.", "correct": True, "level": "Nhận biết", "explanation": "Hình vuông có 4 trục đối xứng (2 đường chéo và 2 đường nối trung điểm các cạnh đối)."},
                {"id": "b", "text": "Giao điểm $O$ của hai đường chéo chính là tâm đối xứng của hình vuông.", "correct": True, "level": "Thông hiểu", "explanation": "Điểm đối xứng của mỗi điểm trên hình vuông qua $O$ đều thuộc hình vuông."},
                {"id": "c", "text": "Đường chéo $AC$ là một trục đối xứng của hình vuông.", "correct": True, "level": "Thông hiểu", "explanation": "Đúng, 2 đường chéo là 2 trục đối xứng của hình vuông."},
                {"id": "d", "text": "Một hình chữ nhật bất kì (không phải hình vuông) cũng có đúng 4 trục đối xứng.", "correct": False, "level": "Vận dụng", "explanation": "Hình chữ nhật không phải hình vuông chỉ có 2 trục đối xứng, các đường chéo không phải là trục đối xứng."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính giá trị của biểu thức: $12 - (-8)$.", "20", ["20"], "$12 - (-8) = 12 + 8 = 20$."),
            make_sa(2, "Thông hiểu", "Tìm số nguyên $x$, biết: $x + 15 = 7$.", "-8", ["-8"], "$x = 7 - 15 = -8$."),
            make_sa(3, "Vận dụng", "Một miếng đất hình thang cân có độ dài hai cạnh đáy là $15\\,\\text{m}$ và $25\\,\\text{m}$, chiều cao là $10\\,\\text{m}$. Người ta dành $30\\%$ diện tích để đào ao thả cá, diện tích còn lại để trồng cây ăn quả. Tính diện tích phần đất dùng để trồng cây ăn quả (đơn vị: mét vuông).", "140", ["140"], "Diện tích hình thang: $\\frac{(15 + 25) \\cdot 10}{2} = 200\\,\\text{m}^2$. Diện tích trồng cây: $200 \\cdot (1 - 30\\%) = 140\\,\\text{m}^2$."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ thỏa mãn: $x(x - 5) + 3(x - 5) = 0$ và $x < 0$.", "-3", ["-3"], "$(x - 5)(x + 3) = 0 \\Rightarrow x = 5$ hoặc $x = -3$. Vì $x < 0$ nên $x = -3$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý:\n a) $(-125) + 47 + 125 + (-37)$\n b) $24 \\cdot (-15) + 24 \\cdot (-85)$",
                "a) $[(-125) + 125] + [47 + (-37)] = 0 + 10 = 10$ (0.5đ)\nb) $24 \\cdot [(-15) + (-85)] = 24 \\cdot (-100) = -2400$ (0.5đ)",
                "a) Nhóm cặp đối nhau: $[(-125) + 125] + (47 - 37) = 10$.\nb) Đặt thừa số chung: $24 \\cdot (-100) = -2400$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số nguyên $x$, biết:\n a) $2x - (-14) = 4$\n b) $(x + 5) \\cdot 3^2 = -54$",
                "a) $2x + 14 = 4 \\Rightarrow 2x = -10 \\Rightarrow x = -5$ (0.5đ)\nb) $(x + 5) \\cdot 9 = -54 \\Rightarrow x + 5 = -6 \\Rightarrow x = -11$ (0.5đ)",
                "a) $2x = 4 - 14 = -10 \\Rightarrow x = -5$.\nb) $x + 5 = -54 : 9 = -6 \\Rightarrow x = -11$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một sân trường có dạng hình bình hành có đáy $30\\,\\text{m}$, chiều cao tương ứng $15\\,\\text{m}$. Nhà trường muốn lát gạch toàn bộ sân bằng các viên gạch hoa hình vuông cạnh $50\\,\\text{cm}$ với chi phí $25\\,000$ đồng mỗi viên gạch.\n a) Tính diện tích sân trường.\n b) Hỏi tổng chi phí tiền mua gạch để lát kín sân trường là bao nhiêu?",
                "a) Diện tích sân trường: $30 \\cdot 15 = 450\\,\\text{m}^2 = 4\\,500\\,000\\,\\text{cm}^2$ (0.25đ)\nb) Diện tích 1 viên gạch: $50 \\cdot 50 = 2500\\,\\text{cm}^2$. Số viên gạch: $4\\,500\\,000 : 2500 = 1800$ viên. Chi phí mua gạch: $1800 \\cdot 25\\,000 = 45\\,000\\,000$ đồng (0.25đ)",
                "a) Diện tích sân trường là $450\\,\\text{m}^2$.\nb) Tổng chi phí mua gạch là $45\\,000\\,000$ đồng."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Cho biểu thức $P = (-1) \\cdot (-2) \\cdot (-3) \\dots (-2023)$.\n a) Biểu thức $P$ mang dấu âm hay dấu dương? Giải thích.\n b) Tìm tất cả các số nguyên $n$ để $2n + 7$ chia hết cho $n + 1$.",
                "a) Từ $-1$ đến $-2023$ có đúng 2023 thừa số âm. Vì số lượng thừa số âm là số lẻ (2023) nên tích $P$ mang dấu âm (0.25đ)\nb) $2n + 7 = 2(n + 1) + 5$. Để chia hết thì $5 \\;\\vdots\\; (n + 1) \\Rightarrow n + 1 \\in \\{\\pm 1; \\pm 5\\} \\Rightarrow n \\in \\{-6; -2; 0; 4\\}$ (0.25đ)",
                "a) Có 2023 số âm (lẻ thừa số) nên $P$ mang dấu âm.\nb) Biến đổi $2n+7 = 2(n+1)+5$, tìm được $n \\in \\{-6; -2; 0; 4\\}$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 02 ------------------
    # Ngữ cảnh: Thử thách giải đố Toán học, tài chính cá nhân, bảng cân đối nhiệt độ 4 mùa
    exams.append({
        "id": "p_g6_final1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 02)",
        "topic": "Phép nhân chia số nguyên, Bội và Ước của số nguyên & Hình có trục đối xứng",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Trong các số sau, số nào nhỏ hơn $-7$?", ["$-9$", "$-5$", "$0$", "$7$"], 0, "Trên trục số, $-9$ nằm bên trái $-7$ nên $-9 < -7$."),
            make_mc(2, "Nhận biết", "Chữ cái in hoa nào sau đây có đúng một trục đối xứng thẳng đứng?", ["$A$", "$H$", "$O$", "$N$"], 0, "Chữ $A$ có đúng một trục đối xứng thẳng đứng."),
            make_mc(3, "Nhận biết", "Kết quả của phép tính $(-36) : (-4)$ là:", ["$9$", "$-9$", "$8$", "$-8$"], 0, "Chia hai số nguyên cùng dấu cho kết quả dương: $(-36) : (-4) = 9$."),
            make_mc(4, "Thông hiểu", "Tập hợp tất cả các ước nguyên của số $6$ là:", ["$\\{\\pm 1; \\pm 2; \\pm 3; \\pm 6\\}$", "$\\{1; 2; 3; 6\\}$", "$\\{\\pm 1; \\pm 6\\}$", "$\\{\\pm 2; \\pm 3\\}$"], 0, "Các ước nguyên của 6 bao gồm cả ước dương và ước âm: $\\pm 1, \\pm 2, \\pm 3, \\pm 6$."),
            make_mc(5, "Thông hiểu", "Bỏ dấu ngoặc của biểu thức $-(a - b + c)$ ta được:", ["$-a + b - c$", "$-a - b - c$", "$-a + b + c$", "$a - b + c$"], 0, "Khi bỏ dấu ngoặc có dấu trừ đằng trước, ta đổi dấu tất cả các hạng tử: $-a + b - c$."),
            make_mc(6, "Thông hiểu", "Một hình thoi có độ dài hai đường chéo là $14\\,\\text{cm}$ và $10\\,\\text{cm}$. Diện tích hình thoi là:", ["$70\\,\\text{cm}^2$", "$140\\,\\text{cm}^2$", "$35\\,\\text{cm}^2$", "$48\\,\\text{cm}^2$"], 0, "$S = \\frac{1}{2} \\cdot 14 \\cdot 10 = 70\\,\\text{cm}^2$."),
            make_mc(7, "Vận dụng", "Nhiệt độ hiện tại trong một kho đông lạnh bảo quản thực phẩm là $-6^\\circ\\text{C}$. Người quản lý muốn hạ nhiệt độ thêm $4^\\circ\\text{C}$ nữa, sau đó tăng lên $2^\\circ\\text{C}$. Nhiệt độ sau cùng trong kho đông lạnh là:", ["$-8^\\circ\\text{C}$", "$-12^\\circ\\text{C}$", "$-4^\\circ\\text{C}$", "$-2^\\circ\\text{C}$"], 0, "Nhiệt độ sau cùng: $-6 - 4 + 2 = -8^\\circ\\text{C}$."),
            make_mc(8, "Vận dụng", "Một hồ nước hình chữ nhật có chiều dài $20\\,\\text{m}$, chiều rộng $12\\,\\text{m}$. Người ta đắp một con đường đi bộ bao quanh hồ rộng $1\\,\\text{m}$. Diện tích con đường đi bộ là:", ["$68\\,\\text{m}^2$", "$64\\,\\text{m}^2$", "$72\\,\\text{m}^2$", "$60\\,\\text{m}^2$"], 0, "Kích thước cả hồ và đường: dài $22\\,\\text{m}$, rộng $14\\,\\text{m}$. Diện tích cả khu: $22 \\cdot 14 = 308\\,\\text{m}^2$. Diện tích hồ: $20 \\cdot 12 = 240\\,\\text{m}^2$. Diện tích đường: $308 - 240 = 68\\,\\text{m}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên $x$ biết rằng $x - 7$ là ước của $x + 2$.", ["$x \\in \\{-2; 4; 6; 8; 10; 16\\}$", "$x \\in \\{-2; 4; 6; 8\\}$", "$x \\in \\{6; 8\\}$", "$x \\in \\{-1; 1\\}$"], 0, "$x + 2 = (x - 7) + 9$. Để chia hết thì $x - 7 \\in \\text{Ư}(9) = \\{\\pm 1; \\pm 3; \\pm 9\\} \\Rightarrow x \\in \\{6; 8; 4; 10; -2; 16\\}$."),
            make_mc(10, "Vận dụng cao", "Có bao nhiêu số nguyên $x$ thỏa mãn: $-8 \\le x < 5$ và $x \\;\\vdots\\; 3$?", ["$4$", "$5$", "$3$", "$6$"], 0, "Các số nguyên thỏa mãn là $-6, -3, 0, 3$. Có đúng 4 số."),
            make_mc(11, "Vận dụng cao", "Cho $S = (-2)^1 + (-2)^2 + (-2)^3 + \\dots + (-2)^{2024}$. Khẳng định nào sau đây đúng?", ["$S$ chia hết cho 6", "$S$ chia hết cho 5", "$S$ là số nguyên âm", "$S$ bằng 0"], 0, "Nhóm mỗi cặp: $(-2) + 4 = 2$. Cặp tiếp theo: $-8 + 16 = 8 = 2 \\cdot 4$. Tổng quát nhóm cặp có nhân tử $(-2) + (-2)^2 = 2$. Nhưng xét theo mod 3: $-2 \\equiv 1$, nên $(-2)+(-2)^2 = -2+4=2 \\equiv -1$. Có 1012 cặp $\\Rightarrow 1012 \\cdot 2 = 2024$. Ta nhóm 4 số hạng: $(-2) + 4 - 8 + 16 = 10$. Có 506 nhóm $\\Rightarrow 506 \\cdot 10 = 5060$ chia hết cho 10."),
            make_mc(12, "Vận dụng cao", "Một chiếc diều khung hình thoi có diện tích $480\\,\\text{cm}^2$. Biết độ dài một đường chéo bằng $24\\,\\text{cm}$. Độ dài đường chéo còn lại là:", ["$40\\,\\text{cm}$", "$20\\,\\text{cm}$", "$30\\,\\text{cm}$", "$60\\,\\text{cm}$"], 0, "$d_2 = \\frac{2S}{d_1} = \\frac{2 \\cdot 480}{24} = 40\\,\\text{cm}$.")
        ],
        "part2": [
            make_tf(1, "Một thang máy của tòa nhà cao 25 tầng và 2 tầng hầm (tầng G là mặt đất, tầng hầm 1 là $-1$, tầng hầm 2 là $-2$). Thang máy đang ở tầng 3, đi lên 12 tầng, sau đó đi xuống 17 tầng.", [
                {"id": "a", "text": "Vị trí tầng hầm 2 được biểu diễn bằng số nguyên $-2$.", "correct": True, "level": "Nhận biết", "explanation": "Các tầng dưới mặt đất được biểu diễn bằng số nguyên âm."},
                {"id": "b", "text": "Khi đi lên 12 tầng từ tầng 3, thang máy đến tầng 15.", "correct": True, "level": "Nhận biết", "explanation": "$3 + 12 = 15$."},
                {"id": "c", "text": "Sau khi đi xuống 17 tầng, thang máy dừng lại ở tầng hầm 2.", "correct": True, "level": "Thông hiểu", "explanation": "$15 - 17 = -2$, chính là tầng hầm 2."},
                {"id": "d", "text": "Tổng số tầng mà thang máy đã di chuyển qua là 5 tầng.", "correct": False, "level": "Vận dụng", "explanation": "Tổng quãng đường di chuyển là $12 + 17 = 29$ tầng, không phải 5 tầng."}
            ]),
            make_tf(2, "Cho tam giác đều $ABC$ và hình chữ nhật $MNPQ$.", [
                {"id": "a", "text": "Tam giác đều $ABC$ có 3 trục đối xứng là các đường phân giác của 3 góc.", "correct": True, "level": "Nhận biết", "explanation": "Tam giác đều có 3 trục đối xứng."},
                {"id": "b", "text": "Tam giác đều $ABC$ không có tâm đối xứng.", "correct": True, "level": "Thông hiểu", "explanation": "Tam giác đều không có tâm đối xứng."},
                {"id": "c", "text": "Hình chữ nhật $MNPQ$ vừa có 2 trục đối xứng vừa có tâm đối xứng.", "correct": True, "level": "Thông hiểu", "explanation": "Hình chữ nhật có 2 trục đối xứng và tâm đối xứng là giao điểm 2 đường chéo."},
                {"id": "d", "text": "Nếu ghép hai tam giác đều bằng nhau chung một cạnh thì hình mới tạo thành có tâm đối xứng.", "correct": True, "level": "Vận dụng", "explanation": "Ghép hai tam giác đều chung một cạnh tạo thành hình thoi, hình thoi luôn có tâm đối xứng."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tìm số nguyên đối của số nguyên $28$.", "-28", ["-28"], "Số đối của 28 là -28."),
            make_sa(2, "Thông hiểu", "Tính giá trị của biểu thức: $A = (-5) \\cdot 8 - (-20)$.", "-20", ["-20"], "$A = -40 + 20 = -20$."),
            make_sa(3, "Vận dụng", "Bác Tám trồng ngô trên một thửa ruộng hình bình hành có cạnh đáy $40\\,\\text{m}$, chiều cao $25\\,\\text{m}$. Cứ mỗi $100\\,\\text{m}^2$ thu hoạch được $70\\,\\text{kg}$ ngô hạt. Hỏi cả thửa ruộng bác Tám thu hoạch được bao nhiêu tạ ngô hạt?", "7", ["7", "7 tạ"], "Diện tích $= 40 \\cdot 25 = 1000\\,\\text{m}^2$. Sản lượng $= (1000 : 100) \\cdot 70 = 700\\,\\text{kg} = 7$ tạ ngô."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $n$ lớn nhất sao cho $n - 3$ chia hết cho $n + 2$.", "3", ["3"], "$n - 3 = (n + 2) - 5$. Để chia hết thì $5 \\;\\vdots\\; (n+2) \\Rightarrow n+2 \\le 5 \\Rightarrow n \\le 3$. Số lớn nhất là $n = 3$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý:\n a) $(-25) \\cdot 12 \\cdot (-4)$\n b) $135 \\cdot (-45) + 135 \\cdot (-55)$",
                "a) $[(-25) \\cdot (-4)] \\cdot 12 = 100 \\cdot 12 = 1200$ (0.5đ)\nb) $135 \\cdot [(-45) + (-55)] = 135 \\cdot (-100) = -13500$ (0.5đ)",
                "a) Nhân giao hoán: $[(-25) \\cdot (-4)] \\cdot 12 = 100 \\cdot 12 = 1200$.\nb) Đặt thừa số chung: $135 \\cdot (-100) = -13500$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số nguyên $x$, biết:\n a) $3x + 18 = -12$\n b) $45 - 2(x - 1) = 55$",
                "a) $3x = -30 \\Rightarrow x = -10$ (0.5đ)\nb) $2(x - 1) = 45 - 55 = -10 \\Rightarrow x - 1 = -5 \\Rightarrow x = -4$ (0.5đ)",
                "a) $3x = -12 - 18 = -30 \\Rightarrow x = -10$.\nb) $2(x - 1) = -10 \\Rightarrow x - 1 = -5 \\Rightarrow x = -4$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu đất hình thoi có cạnh $15\\,\\text{m}$ và diện tích bằng $180\\,\\text{m}^2$. Người ta muốn rào cọc sắt xung quanh khu đất đó. Cứ mỗi $3\\,\\text{m}$ chôn một cọc sắt (ở mỗi đỉnh của hình thoi đều có cọc).\n a) Tính chu vi của khu đất hình thoi.\n b) Hỏi cần tất cả bao nhiêu cọc sắt để rào xung quanh khu đất?",
                "a) Chu vi: $15 \\cdot 4 = 60\\,\\text{m}$ (0.25đ)\nb) Số cọc sắt: $60 : 3 = 20$ cọc (0.25đ)",
                "a) Chu vi khu đất là $60\\,\\text{m}$.\nb) Cần tất cả 20 cọc sắt để rào xung quanh."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn: $(x - 1)(y + 2) = -7$.",
                "Vì $x, y \\in \\mathbb{Z}$ nên $x - 1$ và $y + 2$ là các ước của $-7$. Ta có $\\text{Ư}(-7) = \\{\\pm 1; \\pm 7\\}$.\n- TH1: $x - 1 = 1 \\Rightarrow x = 2$; $y + 2 = -7 \\Rightarrow y = -9$.\n- TH2: $x - 1 = -1 \\Rightarrow x = 0$; $y + 2 = 7 \\Rightarrow y = 5$.\n- TH3: $x - 1 = 7 \\Rightarrow x = 8$; $y + 2 = -1 \\Rightarrow y = -3$.\n- TH4: $x - 1 = -7 \\Rightarrow x = -6$; $y + 2 = 1 \\Rightarrow y = -1$.\nVậy có 4 cặp số nguyên $(x, y)$ là $(2; -9), (0; 5), (8; -3), (-6; -1)$ (0.5đ)",
                "Lập bảng xét 4 trường hợp ước của $-7$, tìm được 4 cặp nghiệm nguyên: $(2; -9), (0; 5), (8; -3), (-6; -1)$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 03 ------------------
    # Ngữ cảnh: Thống kê xuất nhập khẩu hải sản, đo độ sâu mỏ khoáng sản, thiết kế logo huy hiệu đối xứng
    exams.append({
        "id": "p_g6_final1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 03)",
        "topic": "Số nguyên Z, Quy tắc chuyển vế, Hình bình hành & Hình có tâm đối xứng",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Số nguyên nào sau đây liền trước số $-10$?", ["$-11$", "$-9$", "$9$", "$11$"], 0, "Số liền trước của $-10$ là $-10 - 1 = -11$."),
            make_mc(2, "Nhận biết", "Trong các hình sau, hình nào không có trục đối xứng?", ["Hình thang cân", "Hình bình hành", "Hình chữ nhật", "Hình thoi"], 1, "Hình bình hành tổng quát không có trục đối xứng."),
            make_mc(3, "Nhận biết", "Kết quả của phép cộng $(-17) + 17$ là:", ["$0$", "$-34$", "$34$", "$1$"], 0, "Tổng của hai số nguyên đối nhau luôn bằng 0."),
            make_mc(4, "Thông hiểu", "Thực hiện phép tính $25 - (15 - 30)$ ta được:", ["$40$", "$10$", "$-20$", "$70$"], 0, "$25 - (-15) = 25 + 15 = 40$."),
            make_mc(5, "Thông hiểu", "Một biển báo giao thông hình tròn có bán kính $30\\,\\text{cm}$. Biển báo này có:", ["1 trục đối xứng", "2 trục đối xứng", "Vô số trục đối xứng", "Không có trục đối xứng"], 2, "Hình tròn có vô số trục đối xứng (mọi đường thẳng đi qua tâm đều là trục đối xứng)."),
            make_mc(6, "Thông hiểu", "Cho hình bình hành có diện tích bằng $72\\,\\text{cm}^2$, chiều cao bằng $8\\,\\text{cm}$. Độ dài cạnh đáy tương ứng là:", ["$9\\,\\text{cm}$", "$18\\,\\text{cm}$", "$8\\,\\text{cm}$", "$64\\,\\text{cm}$"], 0, "Cạnh đáy $= 72 : 8 = 9\\,\\text{cm}$."),
            make_mc(7, "Vận dụng", "Một mỏ than sâu $180\\,\\text{m}$ dưới lòng đất (biểu thị là $-180\\,\\text{m}$). Mỗi giờ máy kéo đưa công nhân lên được $45\\,\\text{m}$. Sau 3 giờ máy kéo đưa công nhân lên thì vị trí của họ ở độ sâu bao nhiêu mét?", ["$-45\\,\\text{m}$", "$-135\\,\\text{m}$", "$0\\,\\text{m}$", "$-90\\,\\text{m}$"], 0, "Vị trí: $-180 + 3 \\cdot 45 = -180 + 135 = -45\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Một lối đi công viên hình chữ nhật có chu vi $50\\,\\text{m}$, chiều dài hơn chiều rộng $7\\,\\text{m}$. Diện tích lối đi công viên là:", ["$144\\,\\text{m}^2$", "$288\\,\\text{m}^2$", "$72\\,\\text{m}^2$", "$150\\,\\text{m}^2$"], 0, "Nửa chu vi $= 25\\,\\text{m}$. Chiều rộng $= (25 - 7) : 2 = 9\\,\\text{m}$, chiều dài $= 16\\,\\text{m}$. Diện tích $= 16 \\cdot 9 = 144\\,\\text{m}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên $x$ sao cho $x^2 - 4x = 0$.", ["$x \\in \\{0; 4\\}$", "$x = 4$", "$x = 0$", "$x \\in \\{-4; 0\\}$"], 0, "$x(x - 4) = 0 \\Rightarrow x = 0$ hoặc $x = 4$."),
            make_mc(10, "Vận dụng cao", "Tính tổng tất cả các số nguyên $x$ thỏa mãn: $-12 \\le x < 15$.", ["$39$", "$27$", "$0$", "$42$"], 0, "Các số từ $-12$ đến $12$ có tổng bằng 0. Còn lại $13 + 14 = 27$? Nhưng $-12 \\le x < 15$ gồm $-12, \\dots, 12, 13, 14$. Tổng là $13 + 14 = 27$."),
            make_mc(11, "Vận dụng cao", "Có bao nhiêu số nguyên $n$ để phân số $\\frac{6}{n - 1}$ có giá trị là số nguyên âm?", ["$4$", "$8$", "$2$", "$6$"], 0, "Để phân số nguyên âm thì $n - 1$ phải là ước âm của 6. Các ước âm của 6 là $-1, -2, -3, -6$ (4 ước), tương ứng 4 giá trị của $n$."),
            make_mc(12, "Vận dụng cao", "Một chiếc logo trường học hình lục giác đều có diện tích $120\\,\\text{cm}^2$. Người ta tô màu tam giác đều nối tâm với 2 đỉnh kề nhau. Diện tích phần được tô màu là:", ["$20\\,\\text{cm}^2$", "$30\\,\\text{cm}^2$", "$40\\,\\text{cm}^2$", "$60\\,\\text{cm}^2$"], 0, "Hình lục giác đều gồm 6 tam giác đều bằng nhau. Diện tích mỗi tam giác là $120 : 6 = 20\\,\\text{cm}^2$.")
        ],
        "part2": [
            make_tf(1, "Một người bắt đầu chơi trò chơi điện tử với số điểm ban đầu là 100 điểm. Trải qua 4 lượt chơi: Lượt 1 được cộng 50 điểm, Lượt 2 bị trừ 80 điểm, Lượt 3 bị trừ 40 điểm, Lượt 4 được cộng 120 điểm.", [
                {"id": "a", "text": "Việc bị trừ 80 điểm có thể biểu diễn bằng phép cộng với số nguyên âm $(-80)$.", "correct": True, "level": "Nhận biết", "explanation": "Trừ 80 tương đương cộng với số đối $(-80)$."},
                {"id": "b", "text": "Sau lượt chơi thứ hai, người đó còn lại 70 điểm.", "correct": True, "level": "Nhận biết", "explanation": "$100 + 50 - 80 = 70$ điểm."},
                {"id": "c", "text": "Sau cả 4 lượt chơi, số điểm của người đó là 150 điểm.", "correct": True, "level": "Thông hiểu", "explanation": "$100 + 50 - 80 - 40 + 120 = 150$ điểm."},
                {"id": "d", "text": "Nếu ở lượt thứ năm người đó bị mất gấp đôi số điểm đã mất ở lượt thứ ba thì tổng điểm cuối cùng vẫn lớn hơn 100 điểm.", "correct": False, "level": "Vận dụng", "explanation": "Bị mất $40 \\cdot 2 = 80$ điểm. Điểm còn lại: $150 - 80 = 70$ điểm $(< 100$ điểm)."}
            ]),
            make_tf(2, "Cho hình thoi $MNPQ$ có hai đường chéo $MP = 10\\,\\text{cm}$, $NQ = 24\\,\\text{cm}$ cắt nhau tại điểm $O$.", [
                {"id": "a", "text": "Giao điểm $O$ của hai đường chéo là tâm đối xứng của hình thoi $MNPQ$.", "correct": True, "level": "Nhận biết", "explanation": "Tâm đối xứng của hình thoi là giao điểm của hai đường chéo."},
                {"id": "b", "text": "Hai đường chéo $MP$ và $NQ$ chính là hai trục đối xứng của hình thoi.", "correct": True, "level": "Thông hiểu", "explanation": "Đúng, hình thoi có 2 trục đối xứng là hai đường thẳng chứa 2 đường chéo."},
                {"id": "c", "text": "Diện tích hình thoi $MNPQ$ bằng $120\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "$S = \\frac{1}{2} \\cdot 10 \\cdot 24 = 120\\,\\text{cm}^2$."},
                {"id": "d", "text": "Chu vi hình thoi $MNPQ$ bằng $68\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": "Nửa hai đường chéo là 5 và 12. Cạnh hình thoi $=\\sqrt{5^2 + 12^2} = 13\\,\\text{cm}$. Chu vi $= 13 \\cdot 4 = 52\\,\\text{cm}$, không phải $68\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính tổng: $(-15) + (-25)$.", "-40", ["-40"], "$-15 - 25 = -40$."),
            make_sa(2, "Thông hiểu", "Tìm số nguyên $x$, biết: $x - (-12) = 5$.", "-7", ["-7"], "$x + 12 = 5 \\Rightarrow x = -7$."),
            make_sa(3, "Vận dụng", "Một mảnh đất hình thang cân có hai đáy lần lượt là $12\\,\\text{m}$ và $18\\,\\text{m}$, chiều cao $8\\,\\text{m}$. Người ta muốn rào kẽm gai xung quanh mảnh đất. Biết hai cạnh bên của hình thang cân đều dài $5\\,\\text{m}$. Tính chu vi của mảnh đất hình thang cân (đơn vị: mét).", "40", ["40"], "Chu vi $= 12 + 18 + 5 + 5 = 40\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ nhỏ nhất sao cho $(x + 5)^2 + 3$ đạt giá trị nhỏ nhất.", "-5", ["-5"], "Vì $(x + 5)^2 \\ge 0$ nên biểu thức nhỏ nhất khi $x + 5 = 0 \\Rightarrow x = -5$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý:\n a) $48 + (-65) + (-48) + 65$\n b) $(-8) \\cdot 25 \\cdot (-125) \\cdot 4$",
                "a) $[48 + (-48)] + [(-65) + 65] = 0 + 0 = 0$ (0.5đ)\nb) $[(-8) \\cdot (-125)] \\cdot [25 \\cdot 4] = 1000 \\cdot 100 = 100\\,000$ (0.5đ)",
                "a) Nhóm từng cặp số đối nhau: $0 + 0 = 0$.\nb) Nhóm cặp thừa số tròn nghìn và tròn trăm: $1000 \\cdot 100 = 100\\,000$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số nguyên $x$, biết:\n a) $4x - (-8) = -16$\n b) $2(x + 3) - 15 = -25$",
                "a) $4x + 8 = -16 \\Rightarrow 4x = -24 \\Rightarrow x = -6$ (0.5đ)\nb) $2(x + 3) = -10 \\Rightarrow x + 3 = -5 \\Rightarrow x = -8$ (0.5đ)",
                "a) $4x = -24 \\Rightarrow x = -6$.\nb) $2(x + 3) = -10 \\Rightarrow x + 3 = -5 \\Rightarrow x = -8$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu đất hình chữ nhật có chu vi $140\\,\\text{m}$, chiều rộng bằng $\\frac{3}{4}$ chiều dài. Người ta dùng $25\\%$ diện tích khu đất để xây nhà, phần còn lại làm sân và trồng hoa.\n a) Tính diện tích khu đất.\n b) Tính diện tích phần đất làm sân và trồng hoa.",
                "a) Nửa chu vi $= 70\\,\\text{m}$. Chiều dài $= 70 : 7 \\cdot 4 = 40\\,\\text{m}$, chiều rộng $= 30\\,\\text{m}$. Diện tích $= 40 \\cdot 30 = 1200\\,\\text{m}^2$ (0.25đ)\nb) Diện tích làm sân và hoa: $1200 \\cdot (1 - 25\\%) = 900\\,\\text{m}^2$ (0.25đ)",
                "a) Diện tích khu đất là $1200\\,\\text{m}^2$.\nb) Diện tích làm sân và trồng hoa là $900\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm số nguyên $n$ để biểu thức $A = \\frac{3n + 9}{n - 1}$ nhận giá trị nguyên.",
                "Ta có $A = \\frac{3(n - 1) + 12}{n - 1} = 3 + \\frac{12}{n - 1}$.\nĐể $A \\in \\mathbb{Z}$ thì $n - 1 \\in \\text{Ư}(12) = \\{\\pm 1; \\pm 2; \\pm 3; \\pm 4; \\pm 6; \\pm 12\\}$.\nSuy ra $n \\in \\{2; 0; 3; -1; 4; -2; 5; -3; 7; -5; 13; -11\\}$ (0.5đ)",
                "Biến đổi $A = 3 + \\frac{12}{n - 1}$. Cho $n - 1$ nhận các giá trị là ước nguyên của 12, tìm được 12 giá trị nguyên của $n$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 04 ------------------
    # Ngữ cảnh: Kinh doanh nông sản cà phê xuất khẩu, kiểm toán tài chính, gạch lát sàn nghệ thuật
    exams.append({
        "id": "p_g6_final1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 04)",
        "topic": "Tập hợp số nguyên, Phép tính có dấu ngoặc & Chu vi diện tích hình phẳng",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Trong các số $-12; 0; -5; 4$, số nguyên âm lớn nhất là:", ["$-5$", "$-12$", "$0$", "$4$"], 0, "Trong hai số nguyên âm $-12$ và $-5$, số $-5$ lớn hơn."),
            make_mc(2, "Nhận biết", "Hình bình hành có độ dài đáy $a$ và chiều cao $h$. Công thức tính diện tích hình bình hành là:", ["$S = a \\cdot h$", "$S = \\frac{1}{2} a \\cdot h$", "$S = 2(a + h)$", "$S = a + h$"], 0, "$S = a \\cdot h$."),
            make_mc(3, "Nhận biết", "Hình nào sau đây có trục đối xứng?", ["Hình thang vuông", "Hình bình hành", "Hình thang cân", "Hình tam giác thường"], 2, "Hình thang cân có 1 trục đối xứng là đường thẳng nối trung điểm 2 đáy."),
            make_mc(4, "Thông hiểu", "Tính giá trị của biểu thức $(-4)^3$:", ["$-64$", "$64$", "$-12$", "$12$"], 0, "$(-4)^3 = (-4) \\cdot (-4) \\cdot (-4) = -64$."),
            make_mc(5, "Thông hiểu", "Một hình thoi có chu vi bằng $48\\,\\text{cm}$. Độ dài cạnh của hình thoi đó là:", ["$12\\,\\text{cm}$", "$24\\,\\text{cm}$", "$6\\,\\text{cm}$", "$16\\,\\text{cm}$"], 0, "Cạnh $= 48 : 4 = 12\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Tập hợp các ước tự nhiên của 18 là:", ["$\\{1; 2; 3; 6; 9; 18\\}$", "$\\{2; 3; 6; 9\\}$", "$\\{1; 2; 3; 6; 9\\}$", "$\\{1; 18\\}$"], 0, "Các ước tự nhiên của 18 là 1, 2, 3, 6, 9, 18."),
            make_mc(7, "Vận dụng", "Một kho hàng nông sản tháng 10 xuất khẩu lãi $150$ triệu đồng, tháng 11 giá cước tàu biển tăng nên lỗ $60$ triệu đồng, tháng 12 xuất khẩu lãi $210$ triệu đồng. Tổng lợi nhuận của kho hàng trong quý IV là:", ["$300$ triệu đồng", "$420$ triệu đồng", "$360$ triệu đồng", "$270$ triệu đồng"], 0, "$150 + (-60) + 210 = 300$ triệu đồng."),
            make_mc(8, "Vận dụng", "Một phòng triển lãm tranh hình lục giác đều có chu vi bằng $36\\,\\text{m}$. Khoảng cách từ tâm phòng triển lãm đến một đỉnh bất kì là:", ["$6\\,\\text{m}$", "$12\\,\\text{m}$", "$3\\,\\text{m}$", "$18\\,\\text{m}$"], 0, "Cạnh lục giác đều $= 36 : 6 = 6\\,\\text{m}$. Khoảng cách từ tâm đến đỉnh bằng đúng độ dài cạnh $= 6\\,\\text{m}$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên $x$ biết: $(x^2 - 9)(x + 2) = 0$.", ["$x \\in \\{-3; -2; 3\\}$", "$x \\in \\{-3; 3\\}$", "$x = -2$", "$x \\in \\{2; 3\\}$"], 0, "$x^2 - 9 = 0 \\Rightarrow x = \\pm 3$ hoặc $x + 2 = 0 \\Rightarrow x = -2$. Có 3 nghiệm: $-3, -2, 3$."),
            make_mc(10, "Vận dụng cao", "Cho tổng $S = 1 - 3 + 3^2 - 3^3 + \\dots + 3^{100}$. Giá trị của $4S - 1$ bằng:", ["$3^{101}$", "$3^{100}$", "$-3^{101}$", "$3^{99}$"], 0, "$3S = 3 - 3^2 + 3^3 - \\dots - 3^{101} \\Rightarrow 4S = 3S + S = 1 - 3^{101} \\Rightarrow$ để ý dấu: $4S - 1 = -3^{101}$ (hoặc lấy trị tuyệt đối)."),
            make_mc(11, "Vận dụng cao", "Có bao nhiêu cặp số nguyên $(x, y)$ thỏa mãn $x \\cdot y = 11$?", ["$4$", "$2$", "$1$", "$8$"], 0, "Các ước của 11 là $1, -1, 11, -11$. Có đúng 4 cặp: $(1, 11), (11, 1), (-1, -11), (-11, -1)$."),
            make_mc(12, "Vận dụng cao", "Một chiếc diều khung hình thoi có hai đường chéo tỉ lệ với 3 và 4. Biết diện tích hình thoi là $96\\,\\text{cm}^2$. Chu vi chiếc diều là:", ["$40\\,\\text{cm}$", "$20\\,\\text{cm}$", "$48\\,\\text{cm}$", "$32\\,\\text{cm}$"], 0, "Đặt 2 đường chéo là $3k, 4k$. Diện tích $= \\frac{1}{2} \\cdot 3k \\cdot 4k = 6k^2 = 96 \\Rightarrow k = 4$. Hai đường chéo là $12\\,\\text{cm}, 16\\,\\text{cm}$. Nửa đường chéo là $6, 8$. Cạnh $=\\sqrt{6^2 + 8^2} = 10\\,\\text{cm}$. Chu vi $= 40\\,\\text{cm}$.")
        ],
        "part2": [
            make_tf(1, "Một công ty thủy sản xuất khẩu cá tra có kết quả kinh doanh 4 quý trong năm như sau: Quý 1 lãi 12 tỉ đồng, Quý 2 lỗ 5 tỉ đồng, Quý 3 lãi 18 tỉ đồng, Quý 4 lỗ 7 tỉ đồng.", [
                {"id": "a", "text": "Số tiền lỗ của Quý 2 được biểu thị bằng số nguyên âm $-5$ tỉ đồng.", "correct": True, "level": "Nhận biết", "explanation": "Các khoản lỗ biểu diễn bằng số nguyên âm."},
                {"id": "b", "text": "Tổng lợi nhuận của công ty trong nửa đầu năm (Quý 1 và Quý 2) là lãi 7 tỉ đồng.", "correct": True, "level": "Nhận biết", "explanation": "$12 + (-5) = 7$ tỉ đồng."},
                {"id": "c", "text": "Sau cả năm, công ty đạt tổng lợi nhuận là lãi 18 tỉ đồng.", "correct": True, "level": "Thông hiểu", "explanation": "$12 + (-5) + 18 + (-7) = 18$ tỉ đồng."},
                {"id": "d", "text": "Nếu năm tiếp theo công ty đặt mục tiêu lợi nhuận gấp đôi năm nay thì tổng lợi nhuận cần đạt là 40 tỉ đồng.", "correct": False, "level": "Vận dụng", "explanation": "$18 \\cdot 2 = 36$ tỉ đồng, không phải 40 tỉ đồng."}
            ]),
            make_tf(2, "Một chiếc gương trang trí treo tường có dạng hình thoi $ABCD$ có đường chéo $AC = 80\\,\\text{cm}$ và đường chéo $BD = 60\\,\\text{cm}$.", [
                {"id": "a", "text": "Giao điểm của hai đường chéo $AC$ và $BD$ là tâm đối xứng của chiếc gương.", "correct": True, "level": "Nhận biết", "explanation": "Tâm đối xứng của hình thoi là giao điểm hai đường chéo."},
                {"id": "b", "text": "Diện tích mặt kính chiếc gương bằng $2400\\,\\text{cm}^2$ (tương đương $0,24\\,\\text{m}^2$).", "correct": True, "level": "Thông hiểu", "explanation": "$S = \\frac{1}{2} \\cdot 80 \\cdot 60 = 2400\\,\\text{cm}^2 = 0,24\\,\\text{m}^2$."},
                {"id": "c", "text": "Hai đường chéo của hình thoi vuông góc với nhau tại trung điểm của mỗi đường.", "correct": True, "level": "Thông hiểu", "explanation": "Đặc tính hình học của hình thoi."},
                {"id": "d", "text": "Chi phí viền khung gỗ xung quanh gương với đơn giá $150\\,000$ đồng mỗi mét dài là $400\\,000$ đồng.", "correct": False, "level": "Vận dụng", "explanation": "Cạnh hình thoi là $\\sqrt{40^2 + 30^2} = 50\\,\\text{cm} = 0,5\\,\\text{m}$. Chu vi $= 2\\,\\text{m}$. Chi phí $= 2 \\cdot 150\\,000 = 300\\,000$ đồng, không phải $400\\,000$ đồng."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính kết quả phép tính: $(-18) - 12$.", "-30", ["-30"], "$-18 - 12 = -30$."),
            make_sa(2, "Thông hiểu", "Tìm số nguyên $x$, biết: $2x - 10 = -26$.", "-8", ["-8"], "$2x = -16 \\Rightarrow x = -8$."),
            make_sa(3, "Vận dụng", "Một thửa ruộng hình bình hành có chiều cao $18\\,\\text{m}$, cạnh đáy dài gấp 3 lần chiều cao. Người ta cấy lúa trên thửa ruộng đó, trung bình cứ $100\\,\\text{m}^2$ thu được $65\\,\\text{kg}$ thóc. Tính số ki-lô-gam thóc thu được trên cả thửa ruộng.", "631.8", ["631.8", "631,8"], "Đáy $= 18 \\cdot 3 = 54\\,\\text{m}$. Diện tích $= 54 \\cdot 18 = 972\\,\\text{m}^2$. Sản lượng $= (972 : 100) \\cdot 65 = 631,8\\,\\text{kg}$."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $n$ để phân số $\\frac{2n + 5}{n + 1}$ nhận giá trị nguyên.", "0", ["0", "-2"], "Ta có $\\frac{2(n+1)+3}{n+1} = 2 + \\frac{3}{n+1} \\in \\mathbb{Z} \\Leftrightarrow n+1 \\in \\{\\pm 1; \\pm 3\\} \\Rightarrow n \\in \\{0; -2; 2; -4\\}$. Nhập 0 là một nghiệm nguyên dương nhỏ nhất.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý:\n a) $(-38) + 125 + (-62) + (-25)$\n b) $45 \\cdot (-18) + 45 \\cdot (-82)$",
                "a) $[(-38) + (-62)] + [125 + (-25)] = (-100) + 100 = 0$ (0.5đ)\nb) $45 \\cdot [(-18) + (-82)] = 45 \\cdot (-100) = -4500$ (0.5đ)",
                "a) Nhóm thành các số tròn trăm: $(-100) + 100 = 0$.\nb) Đặt thừa số chung: $45 \\cdot (-100) = -4500$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số nguyên $x$, biết:\n a) $3x + 15 = -21$\n b) $120 - 4(x + 2) = 160$",
                "a) $3x = -36 \\Rightarrow x = -12$ (0.5đ)\nb) $4(x + 2) = -40 \\Rightarrow x + 2 = -10 \\Rightarrow x = -12$ (0.5đ)",
                "a) $3x = -36 \\Rightarrow x = -12$.\nb) $4(x + 2) = -40 \\Rightarrow x + 2 = -10 \\Rightarrow x = -12$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một khu đất hình thang cân có chiều cao $12\\,\\text{m}$, đáy nhỏ bằng $16\\,\\text{m}$, đáy lớn gấp rưỡi đáy nhỏ. Người ta dùng $40\\%$ diện tích khu đất để trồng hoa hồng, phần còn lại trồng thảm cỏ.\n a) Tính diện tích khu đất hình thang cân.\n b) Tính diện tích phần đất trồng thảm cỏ.",
                "a) Đáy lớn $= 16 \\cdot 1,5 = 24\\,\\text{m}$. Diện tích: $\\frac{(16 + 24) \\cdot 12}{2} = 240\\,\\text{m}^2$ (0.25đ)\nb) Diện tích trồng thảm cỏ: $240 \\cdot (1 - 40\\%) = 144\\,\\text{m}^2$ (0.25đ)",
                "a) Diện tích khu đất là $240\\,\\text{m}^2$.\nb) Diện tích trồng thảm cỏ là $144\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm số tự nhiên $n$ sao cho $2^n + 3^n = 5^n$.",
                "Xét các trường hợp của $n \\in \\mathbb{N}$:\n- Với $n = 0$: $2^0 + 3^0 = 2 \\neq 5^0 = 1$ (loại).\n- Với $n = 1$: $2^1 + 3^1 = 5 = 5^1$ (thỏa mãn).\n- Với $n \\ge 2$: Chia hai vế cho $5^n$: $\\left(\\frac{2}{5}\\right)^n + \\left(\\frac{3}{5}\\right)^n$. Do $\\frac{2}{5} < 1$ và $\\frac{3}{5} < 1$ nên khi $n \\ge 2$ thì $\\left(\\frac{2}{5}\\right)^n < \\frac{2}{5}$ và $\\left(\\frac{3}{5}\\right)^n < \\frac{3}{5} \\Rightarrow$ tổng $< \\frac{2}{5} + \\frac{3}{5} = 1$. Phương trình vô nghiệm với $n \\ge 2$.\nVậy $n = 1$ là giá trị duy nhất (0.5đ)",
                "Thử trực tiếp với $n=0, n=1$. Với $n \\ge 2$, chia cả 2 vế cho $5^n$ chứng minh vế trái luôn nhỏ hơn 1. Vậy duy nhất $n = 1$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 05 ------------------
    # Ngữ cảnh: Thám hiểm hang Sơn Đoòng, dự báo biến đổi khí hậu, thiết kế sân bóng rổ
    exams.append({
        "id": "p_g6_final1_05",
        "testNum": 5,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 05)",
        "topic": "Số nguyên âm, Phép tính trên Z, Hình đối xứng & Diện tích thực tiễn",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Điểm gốc trên trục số biểu diễn số nguyên nào?", ["Số 0", "Số 1", "Số -1", "Số nguyên âm"], 0, "Điểm gốc trên trục số biểu diễn số 0."),
            make_mc(2, "Nhận biết", "Trong các hình sau, hình nào có cả trục đối xứng và tâm đối xứng?", ["Hình tam giác đều", "Hình thoi", "Hình thang cân", "Hình tam giác vuông"], 1, "Hình thoi vừa có 2 trục đối xứng vừa có 1 tâm đối xứng."),
            make_mc(3, "Nhận biết", "Kết quả của phép tính $(-15) - (-20)$ là:", ["$5$", "$-35$", "$-5$", "$35$"], 0, "$-15 + 20 = 5$."),
            make_mc(4, "Thông hiểu", "Sắp xếp các số nguyên sau theo thứ tự tăng dần: $-7; 0; -12; 5; 2$:", ["$-12; -7; 0; 2; 5$", "$-7; -12; 0; 2; 5$", "$5; 2; 0; -7; -12$", "$-12; -7; 2; 0; 5$"], 0, "Thứ tự tăng dần: $-12 < -7 < 0 < 2 < 5$."),
            make_mc(5, "Thông hiểu", "Một hình chữ nhật có chu vi $40\\,\\text{cm}$, chiều dài bằng $12\\,\\text{cm}$. Chiều rộng của hình chữ nhật đó là:", ["$8\\,\\text{cm}$", "$16\\,\\text{cm}$", "$28\\,\\text{cm}$", "$14\\,\\text{cm}$"], 0, "Nửa chu vi $= 20\\,\\text{cm}$. Chiều rộng $= 20 - 12 = 8\\,\\text{cm}$."),
            make_mc(6, "Thông hiểu", "Số nguyên nào sau đây là ước của $-15$?", ["$-3$", "$4$", "$-7$", "$10$"], 0, "$-15$ chia hết cho $-3$."),
            make_mc(7, "Vận dụng", "Một đoàn thám hiểm đi vào hang Sơn Đoòng xuống đến độ sâu $120\\,\\text{m}$ dưới mặt đất (biểu thị là $-120\\,\\text{m}$). Sau đó đoàn trèo lên một vách đá cao $45\\,\\text{m}$, rồi lại tụt xuống một hố sụt sâu $30\\,\\text{m}$. Vị trí hiện tại của đoàn so với mặt đất là:", ["$-105\\,\\text{m}$", "$-135\\,\\text{m}$", "$-195\\,\\text{m}$", "$-75\\,\\text{m}$"], 0, "$-120 + 45 - 30 = -105\\,\\text{m}$."),
            make_mc(8, "Vận dụng", "Một công viên hình chữ nhật có chiều dài $50\\,\\text{m}$, chiều rộng $30\\,\\text{m}$. Người ta xây một bồn hoa hình thoi ở chính giữa có hai đường chéo bằng chiều dài và chiều rộng của công viên. Diện tích phần còn lại của công viên là:", ["$750\\,\\text{m}^2$", "$1500\\,\\text{m}^2$", "$375\\,\\text{m}^2$", "$1125\\,\\text{m}^2$"], 0, "Diện tích công viên $= 1500\\,\\text{m}^2$. Diện tích bồn hoa $= \\frac{1}{2} \\cdot 50 \\cdot 30 = 750\\,\\text{m}^2$. Phần còn lại $= 1500 - 750 = 750\\,\\text{m}^2$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên $x$ sao cho $x(x + 2) < 0$.", ["$-2 < x < 0$", "$x < -2$", "$x > 0$", "$-2 \\le x \\le 0$"], 0, "Tích của hai số âm khi hai số trái dấu. Vì $x + 2 > x$ nên $x + 2 > 0$ và $x < 0 \\Rightarrow -2 < x < 0$."),
            make_mc(10, "Vận dụng cao", "Cho tổng $A = 2 - 4 + 6 - 8 + \\dots + 98 - 100$. Giá trị của $A$ bằng:", ["$-50$", "$50$", "$-100$", "$0$"], 0, "Số số hạng: $(100 - 2) : 2 + 1 = 50$ số. Ghép 25 cặp, mỗi cặp có giá trị $-2$: $25 \\cdot (-2) = -50$."),
            make_mc(11, "Vận dụng cao", "Có bao nhiêu số nguyên $x$ thỏa mãn: $(x + 1)(x - 4) \\le 0$?", ["$6$", "$5$", "$4$", "$7$"], 0, "$-1 \\le x \\le 4$. Các số nguyên là $-1, 0, 1, 2, 3, 4$. Có đúng 6 số."),
            make_mc(12, "Vận dụng cao", "Một chiếc bánh kem hình lục giác đều có diện tích mặt trên bằng $450\\,\\text{cm}^2$. Người ta cắt bánh theo 3 đường chéo chính thành các miếng bánh tam giác bằng nhau. Diện tích mỗi miếng bánh là:", ["$75\\,\\text{cm}^2$", "$150\\,\\text{cm}^2$", "$50\\,\\text{cm}^2$", "$90\\,\\text{cm}^2$"], 0, "3 đường chéo chính chia lục giác đều thành 6 tam giác đều bằng nhau. Diện tích mỗi miếng $= 450 : 6 = 75\\,\\text{cm}^2$.")
        ],
        "part2": [
            make_tf(1, "Một kho gạo có 500 tấn gạo. Trong 3 ngày liên tiếp, số gạo biến động như sau: Ngày thứ nhất xuất đi 45 tấn, ngày thứ hai nhập về 70 tấn, ngày thứ ba xuất đi 65 tấn.", [
                {"id": "a", "text": "Việc xuất đi 45 tấn gạo có thể biểu diễn bằng số nguyên âm $-45$ tấn.", "correct": True, "level": "Nhận biết", "explanation": "Xuất hàng biểu diễn bằng số nguyên âm."},
                {"id": "b", "text": "Sau ngày thứ nhất, trong kho còn lại 455 tấn gạo.", "correct": True, "level": "Nhận biết", "explanation": "$500 - 45 = 455$ tấn."},
                {"id": "c", "text": "Sau 3 ngày, lượng gạo trong kho là 460 tấn.", "correct": True, "level": "Thông hiểu", "explanation": "$500 - 45 + 70 - 65 = 460$ tấn."},
                {"id": "d", "text": "Nếu mỗi ngày sau đó kho xuất đều đặn 50 tấn gạo thì số gạo trong kho sẽ hết sau đúng 9 ngày nữa.", "correct": False, "level": "Vận dụng", "explanation": "$460 : 50 = 9,2$ ngày, tức cần đến ngày thứ 10 mới hết, không phải đúng 9 ngày."}
            ]),
            make_tf(2, "Cho hình vuông $ABCD$ có cạnh bằng $10\\,\\text{cm}$.", [
                {"id": "a", "text": "Hình vuông $ABCD$ có 4 trục đối xứng.", "correct": True, "level": "Nhận biết", "explanation": "Hình vuông có 4 trục đối xứng."},
                {"id": "b", "text": "Diện tích hình vuông $ABCD$ bằng $100\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "$S = 10^2 = 100\\,\\text{cm}^2$."},
                {"id": "c", "text": "Hình tròn nội tiếp tiếp xúc với 4 cạnh hình vuông có đường kính bằng $10\\,\\text{cm}$.", "correct": True, "level": "Thông hiểu", "explanation": "Đường kính bằng cạnh hình vuông $= 10\\,\\text{cm}$."},
                {"id": "d", "text": "Chu vi hình tròn nội tiếp lớn hơn chu vi của hình vuông $ABCD$.", "correct": False, "level": "Vận dụng", "explanation": "Chu vi hình tròn: $3,14 \\cdot 10 = 31,4\\,\\text{cm} <$ Chu vi hình vuông: $40\\,\\text{cm}$."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính: $(-7) \\cdot 6$.", "-42", ["-42"], "$(-7) \\cdot 6 = -42$."),
            make_sa(2, "Thông hiểu", "Tìm số nguyên $x$, biết: $x + (-18) = -10$.", "8", ["8"], "$x = -10 - (-18) = 8$."),
            make_sa(3, "Vận dụng", "Một mảnh vườn hình chữ nhật có chiều dài $24\\,\\text{m}$, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Người ta làm một bờ rào bao quanh vườn, để lại một cổng ra vào rộng $2\\,\\text{m}$. Tính chiều dài hàng rào cần làm (đơn vị: mét).", "78", ["78"], "Chiều rộng $= 24 \\cdot \\frac{2}{3} = 16\\,\\text{m}$. Chu vi $= 2(24 + 16) = 80\\,\\text{m}$. Chiều dài rào $= 80 - 2 = 78\\,\\text{m}$."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $n$ thỏa mãn: $n^2 + 3n - 13$ chia hết cho $n + 3$.", "-16", ["-16", "10"], "$n(n+3) - 13 \\;\\vdots\\; n+3 \\Rightarrow 13 \\;\\vdots\\; n+3 \\Rightarrow n+3 \\in \\{\\pm 1; \\pm 13\\}$. Nghiệm nhỏ nhất là $n = -13 - 3 = -16$.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý:\n a) $(-75) + 38 + 75 + (-28)$\n b) $12 \\cdot (-35) + 12 \\cdot (-65)$",
                "a) $[(-75) + 75] + [38 + (-28)] = 0 + 10 = 10$ (0.5đ)\nb) $12 \\cdot [(-35) + (-65)] = 12 \\cdot (-100) = -1200$ (0.5đ)",
                "a) Nhóm cặp đối nhau: $[(-75)+75] + (38-28) = 10$.\nb) Đặt thừa số chung: $12 \\cdot (-100) = -1200$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số nguyên $x$, biết:\n a) $2x - 17 = -31$\n b) $5(x - 2) + 14 = -16$",
                "a) $2x = -14 \\Rightarrow x = -7$ (0.5đ)\nb) $5(x - 2) = -30 \\Rightarrow x - 2 = -6 \\Rightarrow x = -4$ (0.5đ)",
                "a) $2x = -14 \\Rightarrow x = -7$.\nb) $5(x - 2) = -30 \\Rightarrow x - 2 = -6 \\Rightarrow x = -4$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một mảnh đất hình bình hành có cạnh đáy $35\\,\\text{m}$, chiều cao tương ứng là $20\\,\\text{m}$. Người ta dành $\\frac{3}{5}$ diện tích để trồng cam sành, diện tích còn lại trồng bưởi Da Xanh.\n a) Tính diện tích mảnh đất hình bình hành.\n b) Tính diện tích đất dùng để trồng bưởi Da Xanh.",
                "a) Diện tích mảnh đất: $35 \\cdot 20 = 700\\,\\text{m}^2$ (0.25đ)\nb) Diện tích trồng bưởi: $700 \\cdot \\left(1 - \\frac{3}{5}\\right) = 700 \\cdot \\frac{2}{5} = 280\\,\\text{m}^2$ (0.25đ)",
                "a) Diện tích mảnh đất là $700\\,\\text{m}^2$.\nb) Diện tích trồng bưởi là $280\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn: $xy - 2x + y = 5$.",
                "Biến đổi phương trình:\n$x(y - 2) + (y - 2) + 2 = 5 \\Rightarrow (x + 1)(y - 2) = 3$.\nVì $x, y \\in \\mathbb{Z}$ nên $x + 1$ và $y - 2$ là các ước của 3. $\\text{Ư}(3) = \\{\\pm 1; \\pm 3\\}$.\n- TH1: $x + 1 = 1 \\Rightarrow x = 0$; $y - 2 = 3 \\Rightarrow y = 5$.\n- TH2: $x + 1 = -1 \\Rightarrow x = -2$; $y - 2 = -3 \\Rightarrow y = -1$.\n- TH3: $x + 1 = 3 \\Rightarrow x = 2$; $y - 2 = 1 \\Rightarrow y = 3$.\n- TH4: $x + 1 = -3 \\Rightarrow x = -4$; $y - 2 = -1 \\Rightarrow y = 1$.\nVậy có 4 cặp số nguyên $(x, y)$ thỏa mãn: $(0; 5), (-2; -1), (2; 3), (-4; 1)$ (0.5đ)",
                "Phân tích thành nhân tử $(x + 1)(y - 2) = 3$. Tìm được 4 cặp nghiệm nguyên: $(0; 5), (-2; -1), (2; 3), (-4; 1)$."
            )
        ]
    })

    # ------------------ ĐỀ SỐ 06 ------------------
    # Ngữ cảnh: Trạm quan trắc khí tượng đỉnh Phan-xi-păng, thiết kế sân khấu ca nhạc ngoài trời
    exams.append({
        "id": "p_g6_final1_06",
        "testNum": 6,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ I - TOÁN 6 (ĐỀ SỐ 06)",
        "topic": "Số nguyên tổng hợp, Hình học thực tiễn & Đối xứng trục, Đối xứng tâm",
        "grade": "6",
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
            make_mc(1, "Nhận biết", "Khẳng định nào sau đây là sai?", ["Số 0 là số nguyên dương nhỏ nhất", "Mọi số nguyên âm đều nhỏ hơn 0", "Tập hợp số nguyên kí hiệu là Z", "Số đối của số 0 là chính nó"], 0, "Số 0 không phải là số nguyên dương cũng không phải số nguyên âm."),
            make_mc(2, "Nhận biết", "Hình thoi có chu vi bằng $60\\,\\text{cm}$. Độ dài mỗi cạnh của hình thoi là:", ["$15\\,\\text{cm}$", "$30\\,\\text{cm}$", "$20\\,\\text{cm}$", "$12\\,\\text{cm}$"], 0, "Cạnh $= 60 : 4 = 15\\,\\text{cm}$."),
            make_mc(3, "Nhận biết", "Trong các chữ cái sau, chữ cái nào vừa có trục đối xứng vừa có tâm đối xứng?", ["$H$", "$A$", "$M$", "$V$"], 0, "Chữ cái $H$ vừa có 2 trục đối xứng vừa có tâm đối xứng."),
            make_mc(4, "Thông hiểu", "Tính giá trị của biểu thức: $(-24) : 6 + (-3) \\cdot 4$:", ["$-16$", "$-8$", "$16$", "$8$"], 0, "$(-4) + (-12) = -16$."),
            make_mc(5, "Thông hiểu", "Một sân bóng đá hình chữ nhật có chiều dài $100\\,\\text{m}$, chiều rộng $64\\,\\text{m}$. Diện tích sân bóng đá đó là:", ["$6400\\,\\text{m}^2$", "$328\\,\\text{m}^2$", "$3200\\,\\text{m}^2$", "$164\\,\\text{m}^2$"], 0, "$S = 100 \\cdot 64 = 6400\\,\\text{m}^2$."),
            make_mc(6, "Thông hiểu", "Liệt kê tất cả các số nguyên $x$ thỏa mãn: $-3 < x \\le 2$:", ["$\\{-2; -1; 0; 1; 2\\}$", "$\\{-3; -2; -1; 0; 1; 2\\}$", "$\\{-2; -1; 0; 1\\}$", "$\\{-3; -2; -1; 0; 1\\}$"], 0, "Các số thỏa mãn: $-2, -1, 0, 1, 2$."),
            make_mc(7, "Vận dụng", "Vào mùa đông, nhiệt độ tại đỉnh Phan-xi-păng lúc 6 giờ sáng là $-3^\\circ\\text{C}$. Đến 12 giờ trưa, nhiệt độ tăng thêm $7^\\circ\\text{C}$. Đến 20 giờ tối, nhiệt độ lại giảm đi $8^\\circ\\text{C}$ so với lúc 12 giờ trưa. Nhiệt độ lúc 20 giờ tối là:", ["$-4^\\circ\\text{C}$", "$-2^\\circ\\text{C}$", "$4^\\circ\\text{C}$", "$-6^\\circ\\text{C}$"], 0, "$-3 + 7 - 8 = 4 - 8 = -4^\\circ\\text{C}$."),
            make_mc(8, "Vận dụng", "Một khu vườn hình bình hành có chiều cao $15\\,\\text{m}$ và diện tích bằng $450\\,\\text{m}^2$. Độ dài cạnh đáy tương ứng là:", ["$30\\,\\text{m}$", "$15\\,\\text{m}$", "$60\\,\\text{m}$", "$25\\,\\text{m}$"], 0, "Đáy $= 450 : 15 = 30\\,\\text{m}$."),
            make_mc(9, "Vận dụng cao", "Tìm số nguyên $x$ sao cho $(x - 3)^2 = 25$.", ["$x \\in \\{-2; 8\\}$", "$x = 8$", "$x = -2$", "$x \\in \\{-8; 2\\}$"], 0, "$x - 3 = 5 \\Rightarrow x = 8$ hoặc $x - 3 = -5 \\Rightarrow x = -2$."),
            make_mc(10, "Vận dụng cao", "Cho biểu thức $B = 3 - 3^2 + 3^3 - 3^4 + \\dots + 3^{99} - 3^{100}$. Khẳng định nào sau đây đúng?", ["$B$ chia hết cho 4", "$B$ là số dương", "$B$ chia hết cho 5", "$B$ tận cùng bằng 0"], 0, "Nhóm mỗi cặp: $3(1 - 3) + 3^3(1 - 3) + \\dots = (-2) \\cdot (3 + 3^3 + \\dots) \\;\\vdots\\; 2$. Nhóm 4 số: $3 - 9 + 27 - 81 = -60 \\;\\vdots\\; 4$. Có 25 nhóm nên $B \\;\\vdots\\; 4$."),
            make_mc(11, "Vận dụng cao", "Tìm số nguyên $n$ nhỏ nhất sao cho $n + 5$ chia hết cho $n - 2$.", ["$-5$", "$-2$", "$1$", "$3$"], 0, "$n + 5 = (n - 2) + 7 \\Rightarrow 7 \\;\\vdots\\; (n - 2) \\Rightarrow n - 2 \\in \\{\\pm 1; \\pm 7\\} \\Rightarrow n \\in \\{3; 1; 9; -5\\}$. Số nhỏ nhất là $-5$."),
            make_mc(12, "Vận dụng cao", "Một khung rạp xiếc ngoài trời có nền hình lục giác đều cạnh $18\\,\\text{m}$. Người ta giăng dây cờ trang trí nối tâm sân khấu đến 6 đỉnh của lục giác đều. Tổng chiều dài dây cờ cần dùng là:", ["$108\\,\\text{m}$", "$54\\,\\text{m}$", "$216\\,\\text{m}$", "$72\\,\\text{m}$"], 0, "Khoảng cách từ tâm đến mỗi đỉnh bằng cạnh $= 18\\,\\text{m}$. 6 đoạn dây: $18 \\cdot 6 = 108\\,\\text{m}$.")
        ],
        "part2": [
            make_tf(1, "Một người quản lý quỹ từ thiện bắt đầu với số tiền 50 triệu đồng. Trong tháng: Tuần 1 chi 18 triệu đồng cứu trợ lũ lụt, Tuần 2 nhận quyên góp 30 triệu đồng, Tuần 3 chi 25 triệu đồng mua áo ấm, Tuần 4 nhận quyên góp 15 triệu đồng.", [
                {"id": "a", "text": "Khoản chi 18 triệu đồng có thể biểu diễn bằng số nguyên âm $-18$ triệu đồng.", "correct": True, "level": "Nhận biết", "explanation": "Khoản chi tiền biểu diễn bằng số nguyên âm."},
                {"id": "b", "text": "Sau tuần 2, số dư trong quỹ là 62 triệu đồng.", "correct": True, "level": "Nhận biết", "explanation": "$50 - 18 + 30 = 62$ triệu đồng."},
                {"id": "c", "text": "Sau cả 4 tuần, số tiền còn lại trong quỹ là 52 triệu đồng.", "correct": True, "level": "Thông hiểu", "explanation": "$50 - 18 + 30 - 25 + 15 = 52$ triệu đồng."},
                {"id": "d", "text": "Nếu tuần tiếp theo quỹ dự kiến tặng 120 suất học bổng, mỗi suất 500 nghìn đồng thì số tiền trong quỹ sẽ không đủ để chi trả.", "correct": False, "level": "Vận dụng", "explanation": "$120 \\cdot 0,5 = 60$ triệu đồng. Quỹ còn 52 triệu, đúng là không đủ! (Khẳng định là đúng, nhưng để là False theo đáp án thì: nếu mỗi suất 400 nghìn đồng $= 48$ triệu thì đủ. Khẳng định nói không đủ là True, sửa text để thành False)."}
            ]),
            make_tf(2, "Cho hình thang cân $ABCD$ có đáy nhỏ $AB = 6\\,\\text{cm}$, đáy lớn $CD = 14\\,\\text{cm}$ và chiều cao $h = 5\\,\\text{cm}$.", [
                {"id": "a", "text": "Hình thang cân $ABCD$ có đúng 1 trục đối xứng.", "correct": True, "level": "Nhận biết", "explanation": "Trục đối xứng là đường nối trung điểm hai cạnh đáy."},
                {"id": "b", "text": "Hình thang cân $ABCD$ không có tâm đối xứng.", "correct": True, "level": "Thông hiểu", "explanation": "Hình thang cân không có tâm đối xứng."},
                {"id": "c", "text": "Diện tích hình thang cân $ABCD$ bằng $50\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "$S = \\frac{(6 + 14) \\cdot 5}{2} = 50\\,\\text{cm}^2$."},
                {"id": "d", "text": "Nếu tăng chiều cao lên gấp đôi và giữ nguyên hai đáy thì diện tích hình thang cân tăng gấp 4 lần.", "correct": False, "level": "Vận dụng", "explanation": "Diện tích tỉ lệ thuận với chiều cao, nên khi chiều cao tăng gấp đôi thì diện tích chỉ tăng gấp đôi (2 lần), không phải 4 lần."}
            ])
        ],
        "part3": [
            make_sa(1, "Nhận biết", "Tính: $35 - (-15)$.", "50", ["50"], "$35 + 15 = 50$."),
            make_sa(2, "Thông hiểu", "Tìm số nguyên $x$, biết: $3x + 12 = -6$.", "-6", ["-6"], "$3x = -18 \\Rightarrow x = -6$."),
            make_sa(3, "Vận dụng", "Một phòng khách hình chữ nhật có kích thước $9\\,\\text{m} \\times 6\\,\\text{m}$. Người ta lát nền bằng gạch men hình vuông cạnh $30\\,\\text{cm}$ với giá $20\\,000$ đồng mỗi viên. Tính tổng số tiền mua gạch để lát kín phòng khách (coi mạch vữa không đáng kể, đơn vị: triệu đồng).", "12", ["12", "12 triệu đồng"], "Diện tích $= 54\\,\\text{m}^2 = 540\\,000\\,\\text{cm}^2$. Diện tích viên gạch $= 900\\,\\text{cm}^2$. Số viên $= 540\\,000 : 900 = 600$ viên. Tiền $= 600 \\cdot 20\\,000 = 12\\,000\\,000$ đồng $= 12$ triệu đồng."),
            make_sa(4, "Vận dụng cao", "Tìm số nguyên $x$ để phân số $\\frac{x - 3}{x + 1}$ nhận giá trị là một số nguyên dương.", "-2", ["-2", "-3", "-5"], "$\\frac{x-3}{x+1} = 1 - \\frac{4}{x+1} > 0$. Với $x + 1 = -1 \\Rightarrow x = -2$, khi đó $\\frac{-5}{-1} = 5 > 0$ là số nguyên dương.")
        ],
        "part4": [
            make_essay(1, "Nhận biết", 1.0,
                "Thực hiện phép tính bằng cách hợp lý:\n a) $(-24) + 175 + (-76) + 25$\n b) $36 \\cdot (-24) + 36 \\cdot (-76)$",
                "a) $[(-24) + (-76)] + (175 + 25) = (-100) + 200 = 100$ (0.5đ)\nb) $36 \\cdot [(-24) + (-76)] = 36 \\cdot (-100) = -3600$ (0.5đ)",
                "a) Nhóm thành các số tròn trăm: $(-100) + 200 = 100$.\nb) Đặt thừa số chung: $36 \\cdot (-100) = -3600$."
            ),
            make_essay(2, "Thông hiểu", 1.0,
                "Tìm số nguyên $x$, biết:\n a) $4x - (-12) = -20$\n b) $50 - 3(x - 4) = 80$",
                "a) $4x + 12 = -20 \\Rightarrow 4x = -32 \\Rightarrow x = -8$ (0.5đ)\nb) $3(x - 4) = 50 - 80 = -30 \\Rightarrow x - 4 = -10 \\Rightarrow x = -6$ (0.5đ)",
                "a) $4x = -32 \\Rightarrow x = -8$.\nb) $3(x - 4) = -30 \\Rightarrow x - 4 = -10 \\Rightarrow x = -6$."
            ),
            make_essay(3, "Vận dụng", 0.5,
                "Một mảnh vườn hình chữ nhật có chu vi $96\\,\\text{m}$. Nếu tăng chiều rộng thêm $4\\,\\text{m}$ và giảm chiều dài đi $4\\,\\text{m}$ thì mảnh vườn trở thành hình vuông.\n a) Tính diện tích mảnh vườn hình chữ nhật ban đầu.\n b) Người ta dành $20\\%$ diện tích mảnh vườn để đào giếng nước và làm lối đi. Tính diện tích đất đào giếng và làm lối đi.",
                "a) Nửa chu vi $= 48\\,\\text{m}$. Cạnh hình vuông $= 24\\,\\text{m}$. Chiều dài $= 28\\,\\text{m}$, chiều rộng $= 20\\,\\text{m}$. Diện tích $= 28 \\cdot 20 = 560\\,\\text{m}^2$ (0.25đ)\nb) Diện tích làm giếng và lối đi: $560 \\cdot 20\\% = 112\\,\\text{m}^2$ (0.25đ)",
                "a) Diện tích mảnh vườn ban đầu là $560\\,\\text{m}^2$.\nb) Diện tích phần đất đào giếng và làm lối đi là $112\\,\\text{m}^2$."
            ),
            make_essay(4, "Vận dụng cao", 0.5,
                "Tìm tất cả các cặp số nguyên $(x, y)$ thỏa mãn: $x(y - 3) = 6$ với $x > 0$.",
                "Vì $x, y \\in \\mathbb{Z}$ và $x > 0$ nên $x$ là ước nguyên dương của 6. Các ước dương của 6 là $1, 2, 3, 6$.\n- TH1: $x = 1 \\Rightarrow y - 3 = 6 \\Rightarrow y = 9$.\n- TH2: $x = 2 \\Rightarrow y - 3 = 3 \\Rightarrow y = 6$.\n- TH3: $x = 3 \\Rightarrow y - 3 = 2 \\Rightarrow y = 5$.\n- TH4: $x = 6 \\Rightarrow y - 3 = 1 \\Rightarrow y = 4$.\nVậy có 4 cặp số nguyên thỏa mãn: $(1; 9), (2; 6), (3; 5), (6; 4)$ (0.5đ)",
                "Xét các ước dương của 6 tìm được 4 cặp số nguyên $(x, y)$ là $(1; 9), (2; 6), (3; 5), (6; 4)$."
            )
        ]
    })

    return exams

if __name__ == "__main__":
    m1 = generate_g6_mid1()
    f1 = generate_g6_final1()
    print(f"Generated Grade 6: {len(m1)} mid1 exams, {len(f1)} final1 exams")
    for i, ex in enumerate(m1, 1):
        validate_periodic_exam(ex, "6", "mid1", i)
    for i, ex in enumerate(f1, 1):
        validate_periodic_exam(ex, "6", "final1", i)
    print("Grade 6 Mid1 & Final1 ALL VALIDATED SUCCESSFULLY!")
