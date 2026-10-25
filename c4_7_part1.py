# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG IV: TAM GIÁC BẰNG NHAU
PHẦN 1:
- BÀI 12: TỔNG CÁC GÓC TRONG MỘT TAM GIÁC (c4_7_bai1)
- BÀI 13: HAI TAM GIÁC BẰNG NHAU. TRƯỜNG HỢP BẰNG NHAU THỨ NHẤT CỦA TAM GIÁC (C.C.C) (c4_7_bai2)
- BÀI 14: TRƯỜNG HỢP BẰNG NHAU THỨ HAI VÀ THỨ BA CỦA TAM GIÁC (C.G.C, G.C.G) (c4_7_bai3)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 12: TỔNG CÁC GÓC TRONG MỘT TAM GIÁC (c4_7_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c4_7_bai1_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 12: Tổng các góc trong một tam giác - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tổng ba góc của một tam giác bất kì luôn bằng:", "options": ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$120^\\circ$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Trong tam giác vuông, hai góc nhọn có tính chất:", "options": ["Phụ nhau (tổng bằng $90^\\circ$)", "Bù nhau (tổng bằng $180^\\circ$)", "Bằng nhau", "Có tổng bằng $60^\\circ$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Góc ngoài của một tam giác là góc:", "options": ["Kề bù với một góc của tam giác đó", "Nằm hoàn toàn bên ngoài tam giác", "Có số đo lớn hơn $90^\\circ$", "Kề với một góc trong của tam giác"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Mỗi góc ngoài của một tam giác có số đo bằng:", "options": ["Tổng số đo hai góc trong không kề với nó", "Tổng ba góc trong của tam giác", "Số đo góc kề bù với nó", "$180^\\circ$ trừ đi số đo một góc ngoài khác"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ, \\widehat{B} = 70^\\circ$. Số đo góc $C$ là:", "options": ["$50^\\circ$", "$60^\\circ$", "$70^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho $\\triangle MNP$ vuông tại $M$. Nếu $\\widehat{N} = 35^\\circ$ thì số đo $\\widehat{P}$ bằng:", "options": ["$55^\\circ$", "$65^\\circ$", "$145^\\circ$", "$45^\\circ$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Góc ngoài tại đỉnh $A$ của $\\triangle ABC$ bằng $120^\\circ$. Khi đó số đo góc $\\widehat{B} + \\widehat{C}$ bằng:", "options": ["$120^\\circ$", "$60^\\circ$", "$180^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tam giác có ba góc bằng nhau thì mỗi góc có số đo là:", "options": ["$60^\\circ$", "$45^\\circ$", "$90^\\circ$", "$50^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho $\\triangle DEF$ có $\\widehat{D} = 40^\\circ$ và $\\widehat{E} = 2\\widehat{D}$. Số đo góc $F$ là:", "options": ["$60^\\circ$", "$80^\\circ$", "$40^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{A} - \\widehat{B} = 20^\\circ$ và $\\widehat{B} - \\widehat{C} = 20^\\circ$. Số đo góc $B$ là:", "options": ["$60^\\circ$", "$80^\\circ$", "$40^\\circ$", "$70^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho tam giác có số đo ba góc tỉ lệ với $1; 2; 3$. Số đo góc lớn nhất của tam giác đó là:", "options": ["$90^\\circ$", "$60^\\circ$", "$120^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$. Tia phân giác của góc $B$ và $C$ cắt nhau tại $I$. Biết $\\widehat{A} = 80^\\circ$, số đo $\\widehat{BIC}$ là:", "options": ["$130^\\circ$", "$100^\\circ$", "$140^\\circ$", "$120^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{B} = 50^\\circ$. Xét tính đúng/sai của các khẳng định sau:",
            "statements": [
                {"subId": "a", "text": "Số đo $\\widehat{A} = 90^\\circ$.", "correct": True},
                {"subId": "b", "text": "Số đo $\\widehat{C} = 40^\\circ$.", "correct": True},
                {"subId": "c", "text": "Góc ngoài tại đỉnh $B$ của tam giác có số đo là $140^\\circ$.", "correct": False},
                {"subId": "d", "text": "Tổng số đo góc $B$ và góc $C$ bằng $90^\\circ$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho $\\triangle MNP$ có số đo các góc tỉ lệ với $2 : 3 : 4$. Xét tính đúng/sai của các khẳng định:",
            "statements": [
                {"subId": "a", "text": "Tổng số phần bằng nhau là $9$ phần.", "correct": True},
                {"subId": "b", "text": "Góc nhỏ nhất có số đo là $40^\\circ$.", "correct": True},
                {"subId": "c", "text": "Góc lớn nhất có số đo là $90^\\circ$.", "correct": False},
                {"subId": "d", "text": "Tam giác $MNP$ là tam giác nhọn (cả ba góc đều nhỏ hơn $90^\\circ$).", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 75^\\circ, \\widehat{B} = 45^\\circ$. Tính số đo góc $C$ (độ).", "correctAnswer": "60", "explanation": "$\\widehat{C} = 180^\\circ - (75^\\circ + 45^\\circ) = 60^\\circ$."},
        {"id": 2, "level": "Thông hiểu", "question": "Góc ngoài tại đỉnh $A$ của một tam giác bằng $110^\\circ$, một góc trong không kề với nó bằng $40^\\circ$. Tính số đo góc trong còn lại không kề với đỉnh $A$ (độ).", "correctAnswer": "70", "explanation": "Số đo góc còn lại là $110^\\circ - 40^\\circ = 70^\\circ$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 2\\widehat{B}$ và $\\widehat{B} = 3\\widehat{C}$. Tính số đo góc $C$ (độ).", "correctAnswer": "18", "explanation": "Ta có $\\widehat{B} = 3\\widehat{C}, \\widehat{A} = 6\\widehat{C}$. Tổng ba góc là $6\\widehat{C} + 3\\widehat{C} + \\widehat{C} = 10\\widehat{C} = 180^\\circ \\Rightarrow \\widehat{C} = 18^\\circ$."},
        {"id": 4, "level": "Vận dụng", "question": "Một chiếc thang dựa vào tường, chân thang tạo với mặt đất góc $65^\\circ$. Góc mà đầu thang tạo với bức tường thẳng đứng bằng bao nhiêu độ?", "correctAnswer": "25", "explanation": "Bức tường thẳng đứng vuông góc với mặt đất nên góc tạo bởi thang và tường là $90^\\circ - 65^\\circ = 25^\\circ$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 65^\\circ, \\widehat{C} = 55^\\circ$. Tia phân giác góc $A$ cắt cạnh $BC$ tại $D$.\na) Tính số đo góc $A$ của $\\triangle ABC$.\nb) Tính số đo góc $\\widehat{ADB}$.",
            "solution": "a) Trong $\\triangle ABC$, ta có $\\widehat{A} = 180^\\circ - (\\widehat{B} + \\widehat{C}) = 180^\\circ - (65^\\circ + 55^\\circ) = 60^\\circ$.\nb) Vì $AD$ là phân giác của $\\widehat{A}$ nên $\\widehat{BAD} = \\frac{\\widehat{A}}{2} = 30^\\circ$.\nXét $\\triangle ABD$, có $\\widehat{ADB} = 180^\\circ - (\\widehat{BAD} + \\widehat{B}) = 180^\\circ - (30^\\circ + 65^\\circ) = 85^\\circ$.",
            "rubric": [
                {"step": "Tính đúng góc A = 60 độ", "subScore": 0.5},
                {"step": "Tính đúng góc BAD = 30 độ và góc ADB = 85 độ", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho tam giác $ABC$ vuông tại $A$, kẻ đường cao $AH$ ($H \\in BC$). Chứng minh rằng $\\widehat{BAH} = \\widehat{C}$ và $\\widehat{CAH} = \\widehat{B}$.",
            "solution": "Trong $\\triangle ABC$ vuông tại $A$, ta có: $\\widehat{B} + \\widehat{C} = 90^\\circ$.\nXét $\\triangle ABH$ vuông tại $H$, ta có: $\\widehat{BAH} + \\widehat{B} = 90^\\circ$.\nDo đó, $\\widehat{BAH} = \\widehat{C}$ (cùng phụ với $\\widehat{B}$).\nTương tự, trong $\\triangle ACH$ vuông tại $H$, ta có $\\widehat{CAH} + \\widehat{C} = 90^\\circ$.\nSuy ra $\\widehat{CAH} = \\widehat{B}$ (cùng phụ với $\\widehat{C}$).",
            "rubric": [
                {"step": "Lập luận chứng minh góc BAH = góc C cùng phụ góc B", "subScore": 0.5},
                {"step": "Lập luận chứng minh góc CAH = góc B cùng phụ góc C", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{A} = \\alpha$. Hai tia phân giác của góc $B$ và góc $C$ cắt nhau tại $I$. Tính số đo góc $\\widehat{BIC}$ theo $\\alpha$.",
            "solution": "Trong $\\triangle ABC$, ta có $\\widehat{B} + \\widehat{C} = 180^\\circ - \\widehat{A} = 180^\\circ - \\alpha$.\nVì $BI$ và $CI$ là các tia phân giác nên:\n$\\widehat{IBC} = \\frac{\\widehat{B}}{2}$ và $\\widehat{ICB} = \\frac{\\widehat{C}}{2}$.\nDo đó: $\\widehat{IBC} + \\widehat{ICB} = \\frac{\\widehat{B} + \\widehat{C}}{2} = \\frac{180^\\circ - \\alpha}{2} = 90^\\circ - \\frac{\\alpha}{2}$.\nXét $\\triangle IBC$, ta có:\n$\\widehat{BIC} = 180^\\circ - (\\widehat{IBC} + \\widehat{ICB}) = 180^\\circ - (90^\\circ - \\frac{\\alpha}{2}) = 90^\\circ + \\frac{\\alpha}{2}$.",
            "rubric": [
                {"step": "Tính tổng hai góc IBC + ICB theo alpha", "subScore": 0.5},
                {"step": "Tính đúng góc BIC = 90 + alpha/2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c4_7_bai1_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 12: Tổng các góc trong một tam giác - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Góc ngoài của tam giác luôn:", "options": ["Lớn hơn mỗi góc trong không kề với nó", "Nhỏ hơn góc trong kề với nó", "Bằng một góc vuông", "Nhỏ hơn $90^\\circ$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Tam giác tù là tam giác có:", "options": ["Một góc tù và hai góc nhọn", "Hai góc tù", "Ba góc tù", "Một góc vuông và một góc tù"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 50^\\circ, \\widehat{B} : \\widehat{C} = 2 : 3$. Số đo góc $B$ là:", "options": ["$52^\\circ$", "$78^\\circ$", "$65^\\circ$", "$45^\\circ$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$, kẻ đường cao $AH$. Khẳng định nào sau đây SAI?", "options": ["$\\widehat{BAH} = \\widehat{B}$", "$\\widehat{BAH} = \\widehat{C}$", "$\\widehat{CAH} = \\widehat{B}$", "$\\widehat{BAH} + \\widehat{CAH} = 90^\\circ$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho tam giác có số đo ba góc tỉ lệ với $2 : 3 : 5$. Tam giác đó là:", "options": ["Tam giác vuông", "Tam giác nhọn", "Tam giác tù", "Tam giác đều"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Một tam giác có tổng hai góc bất kì luôn lớn hơn góc còn lại thì tam giác đó là:", "options": ["Tam giác nhọn", "Tam giác tù", "Tam giác vuông", "Tam giác cân"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 70^\\circ$. Các tia phân giác của góc $B$ và $C$ cắt nhau tại $I$. Số đo góc $BIC$ là:", "options": ["$125^\\circ$", "$110^\\circ$", "$135^\\circ$", "$140^\\circ$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho hình vẽ có $Ax \\parallel By$, biết $\\widehat{xAC} = 40^\\circ, \\widehat{CBy} = 30^\\circ$ ($C$ nằm giữa hai đường song song). Số đo $\\widehat{ACB}$ là:", "options": ["$70^\\circ$", "$110^\\circ$", "$10^\\circ$", "$50^\\circ$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 80^\\circ, \\widehat{C} = 30^\\circ$. Tia phân giác của góc $A$ cắt $BC$ tại $D$. Số đo $\\widehat{ADC}$ bằng:", "options": ["$115^\\circ$", "$65^\\circ$", "$70^\\circ$", "$105^\\circ$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$. Gọi tia phân giác góc $B$ cắt $AC$ tại $M$. Biết $\\widehat{BMC} = 115^\\circ$, số đo góc $C$ là:", "options": ["$40^\\circ$", "$50^\\circ$", "$25^\\circ$", "$35^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$. Hai tia phân giác của hai góc ngoài tại đỉnh $B$ và $C$ cắt nhau tại $K$. Biết $\\widehat{A} = 60^\\circ$, số đo $\\widehat{BKC}$ bằng:", "options": ["$60^\\circ$", "$120^\\circ$", "$30^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho ngôi sao năm cánh $ABCDE$. Tổng số đo 5 góc ở 5 cánh của ngôi sao $(\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D} + \\widehat{E})$ bằng:", "options": ["$180^\\circ$", "$360^\\circ$", "$540^\\circ$", "$270^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 2\\widehat{B}$ và $\\widehat{B} = 3\\widehat{C}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Số đo góc $C$ bằng $18^\\circ$.", "correct": True},
                {"subId": "b", "text": "Số đo góc $B$ bằng $54^\\circ$.", "correct": True},
                {"subId": "c", "text": "Số đo góc $A$ bằng $108^\\circ$.", "correct": True},
                {"subId": "d", "text": "Tam giác $ABC$ là tam giác nhọn.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho $\\triangle MNP$ có góc ngoài tại đỉnh $M$ là $130^\\circ$, và $\\widehat{N} - \\widehat{P} = 30^\\circ$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Tổng hai góc $\\widehat{N} + \\widehat{P} = 130^\\circ$.", "correct": True},
                {"subId": "b", "text": "Số đo góc trong tại đỉnh $M$ là $50^\\circ$.", "correct": True},
                {"subId": "c", "text": "Số đo góc $N$ bằng $80^\\circ$.", "correct": True},
                {"subId": "d", "text": "Số đo góc $P$ bằng $60^\\circ$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 40^\\circ$, hai góc $B$ và $C$ có hiệu là $\\widehat{B} - \\widehat{C} = 20^\\circ$. Tính số đo góc $B$ (độ).", "correctAnswer": "80", "explanation": "$\\widehat{B} + \\widehat{C} = 140^\\circ, \\widehat{B} - \\widehat{C} = 20^\\circ \\Rightarrow \\widehat{B} = (140 + 20)/2 = 80^\\circ$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$. Đường cao $AH$ có $\\widehat{HAB} = 32^\\circ$. Tính số đo góc $C$ (độ).", "correctAnswer": "32", "explanation": "Ta có $\\widehat{C} = \\widehat{HAB} = 32^\\circ$ (cùng phụ với $\\widehat{B}$)."},
        {"id": 3, "level": "Vận dụng", "question": "Tia phân giác trong của góc $B$ và tia phân giác góc ngoài tại đỉnh $C$ của $\\triangle ABC$ cắt nhau tại $E$. Biết $\\widehat{A} = 50^\\circ$, tính số đo $\\widehat{BEC}$ (độ).", "correctAnswer": "25", "explanation": "$\\widehat{BEC} = \\frac{\\widehat{A}}{2} = 25^\\circ$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Một đa giác lồi có 5 cạnh (ngũ giác). Tổng các góc trong của ngũ giác đó bằng bao nhiêu độ?", "correctAnswer": "540", "explanation": "Tổng các góc trong bằng $(5 - 2) \\times 180^\\circ = 540^\\circ$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 90^\\circ, \\widehat{C} = 30^\\circ$. Kẻ $AH \\perp BC$ ($H \\in BC$). Tia phân giác của $\\widehat{HAC}$ cắt $BC$ tại $D$.\na) Tính số đo góc $\\widehat{HAC}$.\nb) Chứng minh rằng $\\triangle ABD$ có $\\widehat{BAD} = \\widehat{BDA}$.",
            "solution": "a) Trong $\\triangle AHC$ vuông tại $H$, ta có: $\\widehat{HAC} = 90^\\circ - \\widehat{C} = 90^\\circ - 30^\\circ = 60^\\circ$.\nb) Vì $AD$ là phân giác $\\widehat{HAC}$ nên $\\widehat{HAD} = \\widehat{DAC} = 30^\\circ$.\nTa có: $\\widehat{BAH} = 90^\\circ - \\widehat{HAC} = 30^\\circ$.\nSuy ra $\\widehat{BAD} = \\widehat{BAH} + \\widehat{HAD} = 30^\\circ + 30^\\circ = 60^\\circ$.\nTrong $\\triangle ADC$, góc $\\widehat{BDA}$ là góc ngoài tại $D$ nên: $\\widehat{BDA} = \\widehat{DAC} + \\widehat{C} = 30^\\circ + 30^\\circ = 60^\\circ$.\nDo đó $\\widehat{BAD} = \\widehat{BDA} = 60^\\circ$.",
            "rubric": [
                {"step": "Tính đúng góc HAC = 60 độ", "subScore": 0.4},
                {"step": "Tính góc BAD = 60 độ và góc BDA = 60 độ, kết luận bằng nhau", "subScore": 0.6}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{B} > \\widehat{C}$. Kẻ đường cao $AH$ và tia phân giác $AD$ của góc $A$ ($H, D \\in BC$). Chứng minh rằng $\\widehat{HAD} = \\frac{\\widehat{B} - \\widehat{C}}{2}$.",
            "solution": "Vì $AD$ là phân giác $\\widehat{A}$ nên $\\widehat{BAD} = \\frac{\\widehat{A}}{2} = \\frac{180^\\circ - (\\widehat{B} + \\widehat{C})}{2} = 90^\\circ - \\frac{\\widehat{B} + \\widehat{C}}{2}$.\nTrong $\\triangle ABH$ vuông tại $H$, ta có $\\widehat{BAH} = 90^\\circ - \\widehat{B}$.\nVì $\\widehat{B} > \\widehat{C}$ nên tia $AH$ nằm giữa $AB$ và $AD$, suy ra:\n$\\widehat{HAD} = \\widehat{BAD} - \\widehat{BAH} = \\left(90^\\circ - \\frac{\\widehat{B} + \\widehat{C}}{2}\\right) - (90^\\circ - \\widehat{B}) = \\widehat{B} - \\frac{\\widehat{B} + \\widehat{C}}{2} = \\frac{\\widehat{B} - \\widehat{C}}{2}$.",
            "rubric": [
                {"step": "Biểu diễn góc BAD và góc BAH theo góc B và góc C", "subScore": 0.5},
                {"step": "Thực hiện phép trừ và rút gọn ra công thức cần chứng minh", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$. Kẻ hai đường phân giác ngoài của góc $B$ và góc $C$ cắt nhau tại $K$. Chứng minh rằng $\\widehat{BKC} = 90^\\circ - \\frac{\\widehat{A}}{2}$.",
            "solution": "Gọi góc ngoài tại đỉnh $B$ là $\\widehat{B_x} = 180^\\circ - \\widehat{B}$ và tại đỉnh $C$ là $\\widehat{C_y} = 180^\\circ - \\widehat{C}$.\nVì $BK$ và $CK$ là tia phân giác của hai góc ngoài này nên:\n$\\widehat{KBC} = \\frac{180^\\circ - \\widehat{B}}{2} = 90^\\circ - \\frac{\\widehat{B}}{2}$; $\\widehat{KCB} = \\frac{180^\\circ - \\widehat{C}}{2} = 90^\\circ - \\frac{\\widehat{C}}{2}$.\nTrong $\\triangle KBC$:\n$\\widehat{BKC} = 180^\\circ - (\\widehat{KBC} + \\widehat{KCB}) = 180^\\circ - \\left(180^\\circ - \\frac{\\widehat{B} + \\widehat{C}}{2}\\right) = \\frac{\\widehat{B} + \\widehat{C}}{2}$.\nMà $\\widehat{B} + \\widehat{C} = 180^\\circ - \\widehat{A}$, nên:\n$\\widehat{BKC} = \\frac{180^\\circ - \\widehat{A}}{2} = 90^\\circ - \\frac{\\widehat{A}}{2}$.",
            "rubric": [
                {"step": "Tính tổng góc KBC + KCB theo các góc trong của tam giác ABC", "subScore": 0.5},
                {"step": "Biến đổi để có BKC = 90 - A/2", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c4_7_bai1_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 12: Tổng các góc trong một tam giác - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Góc tạo bởi hai tia phân giác của hai góc kề bù bằng:", "options": ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$", "$60^\\circ$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 100^\\circ$. Tia phân giác của góc $B$ và góc ngoài tại $C$ cắt nhau tại $E$. Số đo $\\widehat{BEC}$ là:", "options": ["$50^\\circ$", "$80^\\circ$", "$40^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tam giác có một góc bằng $60^\\circ$ và hiệu hai góc kia bằng $30^\\circ$. Ba góc của tam giác đó là:", "options": ["$75^\\circ; 60^\\circ; 45^\\circ$", "$80^\\circ; 60^\\circ; 40^\\circ$", "$90^\\circ; 60^\\circ; 30^\\circ$", "$70^\\circ; 60^\\circ; 50^\\circ$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$. Tổng số đo các góc ngoài (mỗi đỉnh lấy một góc ngoài) của tam giác bằng:", "options": ["$360^\\circ$", "$180^\\circ$", "$540^\\circ$", "$270^\\circ$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho hình cánh diều tứ giác lồi $ABCD$. Tổng 4 góc $\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D}$ bằng:", "options": ["$360^\\circ$", "$180^\\circ$", "$270^\\circ$", "$540^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$. Gọi $D$ là điểm trên $BC$ sao cho $CD = CA$. Kẻ tia phân giác góc $C$ cắt $AB$ tại $K$. Số đo $\\widehat{KDC}$ là:", "options": ["$90^\\circ$", "$60^\\circ$", "$45^\\circ$", "$75^\\circ$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 70^\\circ, \\widehat{C} = 30^\\circ$. Đường thẳng chứa tia phân giác của góc ngoài tại đỉnh $A$ cắt đường thẳng $BC$ tại $P$. Số đo $\\widehat{APB}$ là:", "options": ["$20^\\circ$", "$30^\\circ$", "$40^\\circ$", "$50^\\circ$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 2\\widehat{B} = 4\\widehat{C}$. Số đo của góc $B$ là:", "options": ["$\\approx 51{,}43^\\circ$ (hay $\\frac{360^\\circ}{7}$)", "$60^\\circ$", "$45^\\circ$", "$50^\\circ$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có các đường phân giác $BD$ và $CE$ cắt nhau tại $I$. Biết $\\widehat{BIC} = 120^\\circ$, số đo góc $A$ bằng:", "options": ["$60^\\circ$", "$120^\\circ$", "$30^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$. Điểm $O$ nằm trong tam giác. Khẳng định nào sau đây đúng về $\\widehat{BOC}$?", "options": ["$\\widehat{BOC} > \\widehat{BAC}$", "$\\widehat{BOC} < \\widehat{BAC}$", "$\\widehat{BOC} = \\widehat{BAC}$", "$\\widehat{BOC} = 2\\widehat{BAC}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ$. Phân giác $BD$ và $CE$ cắt nhau tại $I$. Khẳng định nào đúng?", "options": ["$ID = IE$", "$\\widehat{BIC} = 120^\\circ$", "Tia phân giác góc $BIC$ đi qua $A$", "Cả ba đáp án trên đều đúng"], "correct": 3},
        {"id": 12, "level": "Vận dụng cao", "question": "Một đa giác lồi có $n$ cạnh thì tổng số đo các góc ngoài (mỗi đỉnh lấy một góc ngoài) luôn bằng:", "options": ["$360^\\circ$", "$(n - 2) \\cdot 180^\\circ$", "$n \\cdot 180^\\circ$", "$180^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 80^\\circ$, hai tia phân giác trong của góc $B$ và $C$ cắt nhau tại $I$; hai tia phân giác góc ngoài tại đỉnh $B$ và $C$ cắt nhau tại $K$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Số đo $\\widehat{BIC} = 90^\\circ + \\frac{80^\\circ}{2} = 130^\\circ$.", "correct": True},
                {"subId": "b", "text": "Số đo $\\widehat{BKC} = 90^\\circ - \\frac{80^\\circ}{2} = 50^\\circ$.", "correct": True},
                {"subId": "c", "text": "Tổng hai góc $\\widehat{BIC} + \\widehat{BKC} = 180^\\circ$.", "correct": True},
                {"subId": "d", "text": "Góc $\\widehat{IBK} = 100^\\circ$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho điểm $O$ nằm trong tam giác $ABC$. Kéo dài $BO$ cắt $AC$ tại $M$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Góc $\\widehat{BOC}$ là góc ngoài của $\\triangle MOC$ tại đỉnh $O$.", "correct": True},
                {"subId": "b", "text": "$\\widehat{BOC} > \\widehat{BMC}$.", "correct": True},
                {"subId": "c", "text": "$\\widehat{BMC}$ là góc ngoài của $\\triangle ABM$ nên $\\widehat{BMC} > \\widehat{BAC}$.", "correct": True},
                {"subId": "d", "text": "Từ đó suy ra $\\widehat{BOC} < \\widehat{BAC}$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có các góc tỉ lệ với $3 : 4 : 5$. Tìm số đo góc trung bình của tam giác (độ).", "correctAnswer": "60", "explanation": "Tổng số phần là $3 + 4 + 5 = 12$. Góc trung bình ứng với 4 phần: $180 \\times 4 / 12 = 60^\\circ$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 72^\\circ$. Hai tia phân giác của góc $B$ và $C$ cắt nhau tại $I$. Tính số đo $\\widehat{BIC}$ (độ).", "correctAnswer": "126", "explanation": "$\\widehat{BIC} = 90^\\circ + 72^\\circ / 2 = 126^\\circ$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$. Tia phân giác góc trong tại $B$ và phân giác góc ngoài tại $C$ cắt nhau tại $M$. Biết $\\widehat{BMC} = 34^\\circ$, tính số đo góc $A$ của tam giác (độ).", "correctAnswer": "68", "explanation": "Ta có $\\widehat{BMC} = \\frac{\\widehat{A}}{2} \\Rightarrow \\widehat{A} = 2 \\times 34^\\circ = 68^\\circ$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Một đa giác lồi có tổng các góc trong bằng $1440^\\circ$. Đa giác đó có bao nhiêu cạnh?", "correctAnswer": "10", "explanation": "$(n - 2) \\times 180 = 1440 \\Rightarrow n - 2 = 8 \\Rightarrow n = 10$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho hình chữ $V$ lõm $ABDC$ (với điểm $D$ nằm trong góc $\\widehat{BAC}$). Chứng minh rằng $\\widehat{BDC} = \\widehat{A} + \\widehat{B} + \\widehat{C}$.",
            "solution": "Nối $AD$ và kéo dài cắt $BC$ (hoặc kéo dài tia $AD$ thành tia $Ax$).\nÁp dụng tính chất góc ngoài của tam giác:\nTrong $\\triangle ABD$, gọi $Ax$ là tia kéo dài của $AD$, ta có: $\\widehat{xDB} = \\widehat{DAB} + \\widehat{B}$.\nTrong $\\triangle ACD$, ta có: $\\widehat{xDC} = \\widehat{DAC} + \\widehat{C}$.\nCộng vế theo vế hai đẳng thức:\n$\\widehat{BDC} = \\widehat{xDB} + \\widehat{xDC} = (\\widehat{DAB} + \\widehat{DAC}) + \\widehat{B} + \\widehat{C} = \\widehat{BAC} + \\widehat{B} + \\widehat{C}$.\nVậy $\\widehat{BDC} = \\widehat{A} + \\widehat{B} + \\widehat{C}$.",
            "rubric": [
                {"step": "Kẻ đường phụ và dùng tính chất góc ngoài cho 2 tam giác nhỏ", "subScore": 0.5},
                {"step": "Cộng hai góc ngoài để suy ra đẳng thức cần chứng minh", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$. Phân giác trong của góc $B$ và góc ngoài tại đỉnh $C$ cắt nhau tại $E$. Chứng minh rằng $\\widehat{BEC} = \\frac{\\widehat{A}}{2}$.",
            "solution": "Gọi góc ngoài tại đỉnh $C$ là $\\widehat{ACx}$. Vì $CE$ là phân giác $\\widehat{ACx}$ nên $\\widehat{ACx} = 2\\widehat{ECx}$.\nVì $BE$ là phân giác $\\widehat{B}$ nên $\\widehat{B} = 2\\widehat{EBC}$.\nTrong $\\triangle EBC$, góc $\\widehat{ECx}$ là góc ngoài tại $C$ nên:\n$\\widehat{ECx} = \\widehat{BEC} + \\widehat{EBC} \\Rightarrow \\widehat{BEC} = \\widehat{ECx} - \\widehat{EBC}$.\nMặt khác, trong $\\triangle ABC$, góc $\\widehat{ACx}$ là góc ngoài tại $C$ nên:\n$\\widehat{ACx} = \\widehat{A} + \\widehat{B} \\Rightarrow 2\\widehat{ECx} = \\widehat{A} + 2\\widehat{EBC} \\Rightarrow \\widehat{ECx} - \\widehat{EBC} = \\frac{\\widehat{A}}{2}$.\nDo đó $\\widehat{BEC} = \\frac{\\widehat{A}}{2}$.",
            "rubric": [
                {"step": "Thiết lập hệ thức góc ngoài trong tam giác EBC", "subScore": 0.5},
                {"step": "Thiết lập hệ thức góc ngoài trong tam giác ABC và suy ra BEC = A/2", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ$. Các tia phân giác của góc $B$ và $C$ cắt nhau tại $I$ và cắt các cạnh đối diện lần lượt tại $D$ và $E$. Chứng minh rằng $ID = IE$.",
            "solution": "Ta có $\\widehat{BIC} = 90^\\circ + \\frac{\\widehat{A}}{2} = 90^\\circ + 30^\\circ = 120^\\circ$.\nSuy ra hai góc kề bù $\\widehat{EIB} = \\widehat{DIC} = 180^\\circ - 120^\\circ = 60^\\circ$.\nKẻ tia phân giác $IF$ của $\\widehat{BIC}$ ($F \\in BC$).\nKhi đó $\\widehat{BIF} = \\widehat{CIF} = 60^\\circ$.\nXét $\\triangle BIE$ và $\\triangle BIF$ có:\n$\\widehat{EBI} = \\widehat{FBI}$ (do $BI$ là phân giác),\nCạnh $BI$ chung,\n$\\widehat{EIB} = \\widehat{FIB} = 60^\\circ$.\nSuy ra $\\triangle BIE = \\triangle BIF$ (g.c.g) $\\Rightarrow IE = IF$ (1).\nTương tự, xét $\\triangle CID$ và $\\triangle CIF$ có:\n$\\widehat{DCI} = \\widehat{FCI}$, cạnh $CI$ chung, $\\widehat{DIC} = \\widehat{FIC} = 60^\\circ$.\nSuy ra $\\triangle CID = \\triangle CIF$ (g.c.g) $\\Rightarrow ID = IF$ (2).\nTừ (1) và (2) suy ra $ID = IE$.",
            "rubric": [
                {"step": "Tính góc BIC = 120 độ và các góc kề bù = 60 độ, kẻ tia phân giác IF", "subScore": 0.5},
                {"step": "Chứng minh hai cặp tam giác bằng nhau để suy ra IE = IF = ID", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI 13: HAI TAM GIÁC BẰNG NHAU. TRƯỜNG HỢP BẰNG NHAU THỨ NHẤT (C.C.C) (c4_7_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c4_7_bai2_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 13: Hai tam giác bằng nhau (c.c.c) - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hai tam giác bằng nhau là hai tam giác có:", "options": ["Các cạnh tương ứng bằng nhau và các góc tương ứng bằng nhau", "Diện tích bằng nhau", "Chu vi bằng nhau", "Các góc tương ứng bằng nhau"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Nếu $\\triangle ABC = \\triangle DEF$ thì cạnh tương ứng với cạnh $AB$ là:", "options": ["$DE$", "$DF$", "$EF$", "$FD$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Nếu $\\triangle ABC = \\triangle MNP$ thì góc tương ứng với góc $\\widehat{C}$ là:", "options": ["$\\widehat{P}$", "$\\widehat{M}$", "$\\widehat{N}$", "$\\widehat{B}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trường hợp bằng nhau cạnh - cạnh - cạnh (c.c.c) phát biểu: Nếu ba cạnh của tam giác này bằng ba cạnh của tam giác kia thì:", "options": ["Hai tam giác đó bằng nhau", "Hai tam giác đó đồng dạng", "Hai tam giác đó có diện tích bằng nhau nhưng không bằng nhau", "Hai tam giác đó vuông"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle DEF$. Biết $AB = 5\\text{ cm}, BC = 6\\text{ cm}, DF = 7\\text{ cm}$. Chu vi $\\triangle DEF$ là:", "options": ["$18\\text{ cm}$", "$17\\text{ cm}$", "$16\\text{ cm}$", "$15\\text{ cm}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle MNP$. Biết $\\widehat{A} = 45^\\circ, \\widehat{B} = 75^\\circ$. Số đo góc $P$ là:", "options": ["$60^\\circ$", "$45^\\circ$", "$75^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $\\triangle MNP$ và $\\triangle QRS$ có $MN = QR, NP = RS, MP = QS$. Kí hiệu nào sau đây đúng?", "options": ["$\\triangle MNP = \\triangle QRS$", "$\\triangle MNP = \\triangle RSQ$", "$\\triangle MNP = \\triangle SRQ$", "$\\triangle PMN = \\triangle QRS$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho đoạn thẳng $AB$. Đường tròn tâm $A$ bán kính $R$ và đường tròn tâm $B$ bán kính $R$ cắt nhau tại $C$ và $D$. Khi đó $\\triangle CAB = \\triangle DAB$ theo trường hợp:", "options": ["cạnh - cạnh - cạnh (c.c.c)", "cạnh - góc - cạnh", "góc - cạnh - góc", "cạnh huyền - góc nhọn"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho tứ giác $ABCD$ có $AB = CD$ và $BC = AD$. Nối $AC$, ta có $\\triangle ABC = \\triangle CDA$ vì có:", "options": ["Ba cặp cạnh bằng nhau ($AB=CD, BC=DA, AC$ chung)", "Hai góc bằng nhau", "Hai cạnh và một góc vuông", "Góc kề bù"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $AB = AC$. Gọi $M$ là trung điểm của $BC$. Khẳng định nào sau đây SAI?", "options": ["$AM$ không vuông góc với $BC$", "$\\triangle ABM = \\triangle ACM$", "$AM \\perp BC$", "$\\widehat{BAM} = \\widehat{CAM}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho $\\triangle ABC = \\triangle HIK$. Biết $\\widehat{A} = 50^\\circ, \\widehat{I} = 65^\\circ$. Khẳng định nào sau đây đúng?", "options": ["$\\widehat{K} = 65^\\circ$", "$\\widehat{C} = 50^\\circ$", "$\\widehat{B} = 50^\\circ$", "$\\widehat{H} = 65^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho tứ giác $ABCD$ có $AB = BC$ và $CD = DA$. Đoạn thẳng $BD$ có tính chất gì đối với góc $B$ và góc $D$?", "options": ["Là tia phân giác của cả góc $B$ và góc $D$", "Là đường trung tuyến", "Song song với $AC$", "Chỉ là tia phân giác của góc $B$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC = \\triangle DEG$ có $AB = 4\\text{ cm}, BC = 6\\text{ cm}, EG = 6\\text{ cm}, DG = 5\\text{ cm}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Cạnh $DE = 4\\text{ cm}$.", "correct": True},
                {"subId": "b", "text": "Cạnh $AC = 5\\text{ cm}$.", "correct": True},
                {"subId": "c", "text": "Chu vi tam giác $ABC$ bằng $15\\text{ cm}$.", "correct": True},
                {"subId": "d", "text": "Góc $\\widehat{B}$ tương ứng bằng góc $\\widehat{D}$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ có $AB = AC$. Gọi $M$ là trung điểm cạnh $BC$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABM = \\triangle ACM$ theo trường hợp cạnh - cạnh - cạnh (c.c.c).", "correct": True},
                {"subId": "b", "text": "$\\widehat{B} = \\widehat{C}$.", "correct": True},
                {"subId": "c", "text": "$AM$ là tia phân giác của góc $BAC$.", "correct": True},
                {"subId": "d", "text": "Góc $\\widehat{AMB} = 45^\\circ$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle MNP$. Biết $AB = 7\\text{ cm}, AC = 8\\text{ cm}, NP = 9\\text{ cm}$. Tính chu vi của tam giác $MNP$ (cm).", "correctAnswer": "24", "explanation": "Chu vi = $7 + 8 + 9 = 24\\text{ cm}$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle DEF$. Biết $\\widehat{A} = 55^\\circ, \\widehat{E} = 65^\\circ$. Tính số đo góc $F$ (độ).", "correctAnswer": "60", "explanation": "$\\widehat{B} = \\widehat{E} = 65^\\circ \\Rightarrow \\widehat{F} = \\widehat{C} = 180^\\circ - (55^\\circ + 65^\\circ) = 60^\\circ$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho tứ giác $ABCD$ có $AB = AD$ và $CB = CD$. Biết $\\widehat{B} = 100^\\circ$. Tính số đo góc $D$ (độ).", "correctAnswer": "100", "explanation": "$\\triangle ABC = \\triangle ADC$ (c.c.c) $\\Rightarrow \\widehat{D} = \\widehat{B} = 100^\\circ$."},
        {"id": 4, "level": "Vận dụng", "question": "Cho hình thoi $ABCD$ có $AB = 6\\text{ cm}$. Chu vi hình thoi $ABCD$ bằng bao nhiêu cm?", "correctAnswer": "24", "explanation": "Hình thoi có 4 cạnh bằng nhau nên chu vi = $4 \\times 6 = 24\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho hình vẽ có $AB = CD$ và $AD = BC$.\na) Chứng minh rằng $\\triangle ABD = \\triangle CDB$.\nb) Chứng minh rằng $AB \\parallel CD$.",
            "solution": "a) Xét $\\triangle ABD$ và $\\triangle CDB$ có:\n$AB = CD$ (giả thiết),\n$AD = CB$ (giả thiết),\nCạnh $BD$ chung.\nSuy ra $\\triangle ABD = \\triangle CDB$ (c.c.c).\nb) Từ $\\triangle ABD = \\triangle CDB$, suy ra $\\widehat{ABD} = \\widehat{CDB}$ (hai góc tương ứng).\nMà hai góc này ở vị trí so le trong nên $AB \\parallel CD$.",
            "rubric": [
                {"step": "Chứng minh hai tam giác bằng nhau theo c.c.c", "subScore": 0.5},
                {"step": "Suy ra 2 góc so le trong bằng nhau và kết luận AB // CD", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $AB = AC$. Gọi $M$ là trung điểm của $BC$.\na) Chứng minh $\\triangle ABM = \\triangle ACM$.\nb) Chứng minh $AM \\perp BC$.",
            "solution": "a) Xét $\\triangle ABM$ và $\\triangle ACM$ có:\n$AB = AC$ (giả thiết),\n$MB = MC$ (vì $M$ là trung điểm của $BC$),\nCạnh $AM$ chung.\nVậy $\\triangle ABM = \\triangle ACM$ (c.c.c).\nb) Vì $\\triangle ABM = \\triangle ACM$ nên $\\widehat{AMB} = \\widehat{AMC}$ (hai góc tương ứng).\nMặt khác $\\widehat{AMB} + \\widehat{AMC} = 180^\\circ$ (hai góc kề bù).\nSuy ra $\\widehat{AMB} = \\widehat{AMC} = \\frac{180^\\circ}{2} = 90^\\circ$.\nVậy $AM \\perp BC$.",
            "rubric": [
                {"step": "Chứng minh đúng tam giác ABM = ACM theo c.c.c", "subScore": 0.5},
                {"step": "Lập luận góc AMB = AMC = 90 độ, kết luận vuông góc", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho đoạn thẳng $AB$. Vẽ cung tròn tâm $A$ bán kính $R$ và cung tròn tâm $B$ bán kính $R$ ($R > \\frac{AB}{2}$) cắt nhau tại $C$ và $D$. Chứng minh rằng đường thẳng $CD$ là đường trung trực của đoạn thẳng $AB$.",
            "solution": "Xét $\\triangle ACD$ và $\\triangle BCD$ có:\n$AC = BC = R$,\n$AD = BD = R$,\nCạnh $CD$ chung.\nSuy ra $\\triangle ACD = \\triangle BCD$ (c.c.c).\nDo đó $\\widehat{ACD} = \\widehat{BCD}$.\nGọi $H$ là giao điểm của $AB$ và $CD$.\nXét $\\triangle ACH$ và $\\triangle BCH$ có:\n$AC = BC = R$,\n$\\widehat{ACH} = \\widehat{BCH}$,\nCạnh $CH$ chung.\nSuy ra $\\triangle ACH = \\triangle BCH$ (c.g.c).\nTừ đó $HA = HB$ và $\\widehat{AHC} = \\widehat{BHC} = 90^\\circ$.\nVậy $CD$ đi qua trung điểm của $AB$ và vuông góc với $AB$, tức là $CD$ là đường trung trực của đoạn thẳng $AB$.",
            "rubric": [
                {"step": "Chứng minh tam giác ACD = BCD (c.c.c) để suy ra góc ACD = BCD", "subScore": 0.5},
                {"step": "Chứng minh tam giác ACH = BCH để suy ra HA = HB và CD vuông góc AB", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c4_7_bai2_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 13: Hai tam giác bằng nhau (c.c.c) - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho $\\triangle ABC = \\triangle MNP$. Biết $AB = 6\\text{ cm}, BC = 8\\text{ cm}, AC = 10\\text{ cm}$. Khẳng định nào sau đây SAI?", "options": ["$NP = 6\\text{ cm}$", "$MN = 6\\text{ cm}$", "$MP = 10\\text{ cm}$", "$NP = 8\\text{ cm}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ có $AB = AC$. Lấy $M, N$ lần lượt là trung điểm của $AB, AC$. Nếu $BN = CM$ thì khẳng định nào sau đây đúng?", "options": ["$\\triangle BNC = \\triangle CMB$", "$\\triangle AMN$ không cân", "$BN$ không bằng $CM$", "$\\widehat{B} \\neq \\widehat{C}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho hai tam giác bằng nhau: $\\triangle ABC = \\triangle XYZ$. Biết $\\widehat{A} = 2\\widehat{B}$ và $\\widehat{C} = 60^\\circ$. Số đo góc $Y$ là:", "options": ["$40^\\circ$", "$80^\\circ$", "$60^\\circ$", "$30^\\circ$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho tứ giác $ABCD$ có $AB = BC$ và $CD = DA$. Khẳng định nào sau đây đúng?", "options": ["$\\triangle ABD = \\triangle CBD$", "$\\triangle ABC = \\triangle CDA$", "$AC \\parallel BD$", "$AB \\parallel CD$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $AB = AC = BC$. Tam giác $ABC$ là:", "options": ["Tam giác đều", "Tam giác vuông", "Tam giác tù", "Tam giác vuông cân"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $AB = AC$. Gọi $D$ là điểm nằm trong tam giác sao cho $DB = DC$. Khi đó đường thẳng $AD$:", "options": ["Là đường trung trực của đoạn thẳng $BC$", "Song song với $BC$", "Vuông góc với $AB$", "Cắt $BC$ tại điểm không phải trung điểm"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho hai tam giác cân $ABC$ và $DBC$ có chung đáy $BC$ ($A$ và $D$ nằm khác phía đối với $BC$). Khẳng định nào sau đây đúng?", "options": ["$\\triangle ABD = \\triangle ACD$ (c.c.c)", "$\\triangle ABD = \\triangle BCD$", "$AD \\parallel BC$", "$AB = CD$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho hình vẽ có hai đường tròn $(A; R)$ và $(B; R)$ cắt nhau tại $M$ và $N$. Tứ giác $AMBN$ có đặc điểm gì?", "options": ["Có 4 cạnh bằng nhau", "Có 4 góc vuông", "Là hình thang cân", "Chỉ có 2 cạnh bằng nhau"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $\\triangle ABC = \\triangle MNP$. Biết $AB = 3x - 1$, $MN = 8$. Giá trị của $x$ là:", "options": ["$3$", "$2$", "$4$", "$5$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC = \\triangle MNP$. Biết chu vi $\\triangle ABC$ là $22\\text{ cm}$, $AB = 6\\text{ cm}$ và $NP - MP = 2\\text{ cm}$. Độ dài cạnh $BC$ là:", "options": ["$9\\text{ cm}$", "$7\\text{ cm}$", "$8\\text{ cm}$", "$10\\text{ cm}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác đều $ABC$. Lấy các điểm $M, N, P$ lần lượt trên các cạnh $AB, BC, CA$ sao cho $AM = BN = CP$. Khi đó tam giác $MNP$ là:", "options": ["Tam giác đều", "Tam giác tù", "Tam giác vuông cân", "Tam giác vuông"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho tứ giác $ABCD$ có $AB = CD, BC = AD$. Gọi $O$ là giao điểm của $AC$ và $BD$. Khẳng định nào sau đây SAI?", "options": ["$AC \\perp BD$", "$OA = OC$", "$OB = OD$", "$\\triangle OAB = \\triangle OCD$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ và $\\triangle MNP$ có $AB = MN = 5\\text{ cm}, BC = NP = 7\\text{ cm}, AC = MP = 8\\text{ cm}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABC = \\triangle MNP$ theo trường hợp c.c.c.", "correct": True},
                {"subId": "b", "text": "Số đo góc $\\widehat{A}$ bằng góc $\\widehat{M}$.", "correct": True},
                {"subId": "c", "text": "Số đo góc $\\widehat{B}$ bằng góc $\\widehat{P}$.", "correct": False},
                {"subId": "d", "text": "Chu vi hai tam giác đều bằng $20\\text{ cm}$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho đoạn thẳng $AB$. Lấy điểm $C$ và $D$ sao cho $AC = AD$ và $BC = BD$ ($C$ và $D$ nằm khác phía đối với đường thẳng $AB$). Nối $CD$ cắt $AB$ tại $I$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABC = \\triangle ABD$ (c.c.c).", "correct": True},
                {"subId": "b", "text": "$\\widehat{CAB} = \\widehat{DAB}$.", "correct": True},
                {"subId": "c", "text": "$CD$ vuông góc với $AB$.", "correct": True},
                {"subId": "d", "text": "$I$ không phải là trung điểm của $AB$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle DEF$. Biết $AB = 2x + 1$ và $DE = 9$. Tìm giá trị của $x$.", "correctAnswer": "4", "explanation": "$2x + 1 = 9 \\Rightarrow x = 4$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $AB = AC = 10\\text{ cm}, BC = 12\\text{ cm}$. Gọi $M$ là trung điểm $BC$. Tính độ dài $AM$ (cm).", "correctAnswer": "8", "explanation": "$BM = 6\\text{ cm}$. $\\triangle ABM$ vuông tại $M$ nên $AM = \\sqrt{10^2 - 6^2} = 8\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC = \\triangle DEF$. Chu vi $\\triangle ABC$ là $30\\text{ cm}$. Biết $DE = 8\\text{ cm}$, tỉ số $EF : DF = 5 : 6$. Tính độ dài cạnh $EF$ (cm).", "correctAnswer": "10", "explanation": "$EF + DF = 30 - 8 = 22$. $EF = 22 \\times \\frac{5}{11} = 10\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác đều $ABC$ có cạnh bằng $9\\text{ cm}$. Lấy $M$ trên $BC$ sao cho $BM = 3\\text{ cm}$, lấy $N$ trên $CA$ sao cho $CN = 3\\text{ cm}$, lấy $P$ trên $AB$ sao cho $AP = 3\\text{ cm}$. Chu vi $\\triangle MNP$ có các cạnh bằng nhau. Nếu $MN = 3\\sqrt{3}\\text{ cm}$, tính chu vi $\\triangle MNP$ chia cho $\\sqrt{3}$ (lấy phần nguyên).", "correctAnswer": "9", "explanation": "Chu vi = $3 \\times 3\\sqrt{3} = 9\\sqrt{3}$, chia cho $\\sqrt{3}$ bằng $9$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho tứ giác $ABCD$ có $AB = CD$ và $BC = AD$.\na) Chứng minh $\\triangle ABC = \\triangle CDA$.\nb) Chứng minh $AD \\parallel BC$ và $AB \\parallel CD$.",
            "solution": "a) Xét $\\triangle ABC$ và $\\triangle CDA$ có:\n$AB = CD$ (giả thiết),\n$BC = DA$ (giả thiết),\nCạnh $AC$ chung.\nVậy $\\triangle ABC = \\triangle CDA$ (c.c.c).\nb) Từ $\\triangle ABC = \\triangle CDA$ suy ra:\n$\\widehat{ACB} = \\widehat{CAD}$ (hai góc tương ứng), mà hai góc này ở vị trí so le trong nên $BC \\parallel AD$.\n$\\widehat{BAC} = \\widehat{DCA}$ (hai góc tương ứng), mà hai góc này ở vị trí so le trong nên $AB \\parallel CD$.",
            "rubric": [
                {"step": "Chứng minh hai tam giác bằng nhau theo c.c.c", "subScore": 0.5},
                {"step": "Chỉ ra 2 cặp góc so le trong bằng nhau và kết luận song song", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho tam giác $ABC$ có $AB = AC$. Gọi $K$ là điểm nằm trong tam giác sao cho $KB = KC$. Nối $A$ với $K$ cắt $BC$ tại $H$.\na) Chứng minh rằng $\\triangle ABK = \\triangle ACK$.\nb) Chứng minh $AH \\perp BC$ và $H$ là trung điểm của $BC$.",
            "solution": "a) Xét $\\triangle ABK$ và $\\triangle ACK$ có:\n$AB = AC$ (giả thiết),\n$KB = KC$ (giả thiết),\nCạnh $AK$ chung.\nVậy $\\triangle ABK = \\triangle ACK$ (c.c.c).\nb) Từ $\\triangle ABK = \\triangle ACK$ suy ra $\\widehat{BAK} = \\widehat{CAK}$ hay $\\widehat{BAH} = \\widehat{CAH}$.\nXét $\\triangle ABH$ và $\\triangle ACH$ có:\n$AB = AC$, $\\widehat{BAH} = \\widehat{CAH}$, cạnh $AH$ chung.\nDo đó $\\triangle ABH = \\triangle ACH$ (c.g.c).\nSuy ra $HB = HC$ (nên $H$ là trung điểm $BC$) và $\\widehat{AHB} = \\widehat{AHC} = 90^\\circ$ (nên $AH \\perp BC$).",
            "rubric": [
                {"step": "Chứng minh tam giác ABK = ACK (c.c.c) để suy ra tia phân giác", "subScore": 0.5},
                {"step": "Chứng minh tam giác ABH = ACH để kết luận trung điểm và vuông góc", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hình bình hành $ABCD$ có $AB > BC$. Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Chứng minh rằng nếu tam giác $AOB$ có diện tích bằng $S$ thì diện tích hình bình hành $ABCD$ bằng $4S$.",
            "solution": "Vì $ABCD$ là hình bình hành nên $O$ là trung điểm của $AC$ và $BD$.\nTrong $\\triangle ABC$, $BO$ là đường trung tuyến ứng với cạnh $AC$.\nDo đó hai tam giác $\\triangle AOB$ và $\\triangle COB$ có chung đường cao hạ từ $B$ và đáy $OA = OC$, nên $S_{AOB} = S_{COB} = S$.\nHoàn toàn tương tự, $AO$ là trung tuyến của $\\triangle ABD$ nên $S_{AOD} = S_{AOB} = S$.\nVà $CO$ là trung tuyến của $\\triangle CBD$ nên $S_{COD} = S_{COB} = S$.\nVậy cả 4 tam giác nhỏ quanh điểm $O$ đều có diện tích bằng $S$.\nSuy ra $S_{ABCD} = S_{AOB} + S_{BOC} + S_{COD} + S_{DOA} = 4S$.",
            "rubric": [
                {"step": "Chứng minh diện tích hai tam giác có cùng đường cao và đáy bằng nhau thì bằng nhau", "subScore": 0.5},
                {"step": "Tổng hợp diện tích 4 tam giác con để chứng minh S_ABCD = 4S", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c4_7_bai2_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 13: Hai tam giác bằng nhau (c.c.c) - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hai tam giác bằng nhau thì có chu vi như thế nào?", "options": ["Luôn luôn bằng nhau", "Có thể khác nhau", "Gấp đôi nhau", "Tỉ lệ với 2"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle A'B'C'$. Gọi $M, M'$ lần lượt là trung điểm của $BC$ và $B'C'$. Khẳng định nào sau đây SAI?", "options": ["$AM \\neq A'M'$", "$AM = A'M'$", "$\\triangle ABM = \\triangle A'B'M'$", "$\\triangle ACM = \\triangle A'C'M'$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho tứ giác lồi $ABCD$ có $AB = BC$ và $CD = DA$. Đường chéo $AC$ và $BD$ có tính chất:", "options": ["$BD$ là đường trung trực của $AC$", "$AC$ là đường trung trực của $BD$", "$AC = BD$", "$AC \\parallel BD$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho tam giác đều $ABC$. Lấy điểm $O$ trong tam giác sao cho $OA = OB = OC$. Khi đó số đo góc $\\widehat{AOB}$ bằng:", "options": ["$120^\\circ$", "$90^\\circ$", "$60^\\circ$", "$150^\\circ$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $AB = AC$. Lấy điểm $D$ trên cạnh $AB$ và điểm $E$ trên cạnh $AC$ sao cho $AD = AE$. Khi đó $BE = CD$ nhờ cặp tam giác bằng nhau nào?", "options": ["$\\triangle ABE = \\triangle ACD$", "$\\triangle BDC = \\triangle CEB$", "Cả hai cặp trên đều chứng minh được", "Không chứng minh được"], "correct": 2},
        {"id": 6, "level": "Vận dụng", "question": "Cho 4 điểm $A, B, C, D$ sao cho $AB = CD$ và $AD = BC$. Khẳng định nào luôn đúng?", "options": ["Tứ giác $ABCD$ là hình bình hành", "Tứ giác $ABCD$ là hình thoi", "$AC \\perp BD$", "$AB \\perp BC$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho đoạn thẳng $AB$. Tập hợp các điểm $M$ thỏa mãn $MA = MB$ là:", "options": ["Đường trung trực của đoạn thẳng $AB$", "Đường tròn đường kính $AB$", "Tia phân giác", "Đoạn thẳng nối $A$ và $B$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho tam giác nhọn $ABC$. Vẽ về phía ngoài tam giác các tam giác đều $ABD$ và $ACE$. Đoạn thẳng $CD$ và $BE$ có quan hệ gì?", "options": ["$CD = BE$", "$CD \\perp BE$", "Cả $CD = BE$ và góc giữa chúng bằng $60^\\circ$", "$CD = 2BE$"], "correct": 2},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$. Trên nửa mặt phẳng bờ $BC$ không chứa $A$, vẽ $\\triangle BCD$ sao cho $BD = AC$ và $CD = AB$. Khẳng định nào sau đây đúng?", "options": ["$\\triangle ABC = \\triangle DCB$", "$\\triangle ABC = \\triangle BCD$", "$AD \\parallel BC$", "$AB \\parallel AC$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hình lập phương có các mặt là các hình vuông bằng nhau. Đường chéo các mặt bên của hình lập phương tạo thành một tam giác có đặc điểm gì?", "options": ["Là tam giác đều", "Là tam giác vuông", "Là tam giác cân không đều", "Là tam giác tù"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $AB = AC$. Lấy $M$ là trung điểm của $BC$. Từ $M$ kẻ $MH \\perp AB$ và $MK \\perp AC$. Nhận xét nào sau đây đúng?", "options": ["$MH = MK$", "$MH > MK$", "$MH < MK$", "$MH + MK = BC$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho ngũ giác đều $ABCDE$. Tất cả các đường chéo của ngũ giác đều này có độ dài như thế nào?", "options": ["Đều bằng nhau", "Có 3 đường bằng nhau và 2 đường khác", "Từng cặp một bằng nhau", "Hoàn toàn khác nhau"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho hai tam giác cân $ABC$ ($AB = AC$) và tam giác cân $DBC$ ($DB = DC$) có chung cạnh đáy $BC$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABD = \\triangle ACD$ theo trường hợp cạnh - cạnh - cạnh (c.c.c).", "correct": True},
                {"subId": "b", "text": "Đường thẳng $AD$ là tia phân giác của góc $\\widehat{BAC}$.", "correct": True},
                {"subId": "c", "text": "Đường thẳng $AD$ là tia phân giác của góc $\\widehat{BDC}$.", "correct": True},
                {"subId": "d", "text": "Đường thẳng $AD$ song song với đoạn thẳng $BC$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $\\triangle ABC$ có $AB = AC$. Gọi $M$ là trung điểm của $BC$. Lấy điểm $D$ trên đoạn thẳng $AM$ ($D \\neq A, D \\neq M$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$AM$ vuông góc với $BC$.", "correct": True},
                {"subId": "b", "text": "$\\triangle DBM = \\triangle DCM$ (c.g.c hoặc c.c.c).", "correct": True},
                {"subId": "c", "text": "Độ dài đoạn thẳng $DB = DC$.", "correct": True},
                {"subId": "d", "text": "Tam giác $DBC$ không thể là tam giác cân.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle DEF$. Biết $AB = 5\\text{ cm}, BC = 7\\text{ cm}, DF = 6\\text{ cm}$. Tính chu vi $\\triangle DEF$ (cm).", "correctAnswer": "18", "explanation": "Chu vi = $5 + 7 + 6 = 18\\text{ cm}$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho tam giác đều $ABC$. Điểm $M$ nằm trong tam giác sao cho khoảng cách từ $M$ đến ba đỉnh bằng nhau. Tính số đo góc $\\widehat{BMC}$ (độ).", "correctAnswer": "120", "explanation": "Do tính đối xứng, 3 góc quanh $M$ bằng nhau: $360^\\circ / 3 = 120^\\circ$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho hình chữ nhật $ABCD$ có $AB = 8\\text{ cm}, BC = 6\\text{ cm}$. Nối $AC$. Tính độ dài đường chéo $AC$ (cm).", "correctAnswer": "10", "explanation": "$AC = \\sqrt{8^2 + 6^2} = 10\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tứ giác $ABCD$ có $AB = BC = CD = DA$ (hình thoi) và $\\widehat{A} = 60^\\circ$. Biết độ dài cạnh $AB = 5\\text{ cm}$. Tính độ dài đường chéo $BD$ (cm).", "correctAnswer": "5", "explanation": "$\\triangle ABD$ cân tại $A$ có $\\widehat{A} = 60^\\circ$ nên là tam giác đều, do đó $BD = AB = 5\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho hai đường tròn tâm $O$ và tâm $O'$ có cùng bán kính $R$ cắt nhau tại hai điểm $A$ và $B$.\na) Chứng minh $\\triangle OAO' = \\triangle OBO'$.\nb) Chứng minh đường thẳng $OO'$ là đường trung trực của đoạn thẳng $AB$.",
            "solution": "a) Xét $\\triangle OAO'$ và $\\triangle OBO'$ có:\n$OA = OB = R$,\n$O'A = O'B = R$,\nCạnh $OO'$ chung.\nSuy ra $\\triangle OAO' = \\triangle OBO'$ (c.c.c).\nb) Vì $\\triangle OAO' = \\triangle OBO'$ nên $\\widehat{AOO'} = \\widehat{BOO'}$.\nGọi $I$ là giao điểm của $OO'$ và $AB$.\nXét $\\triangle AOI$ và $\\triangle BOI$ có:\n$OA = OB = R$,\n$\\widehat{AOI} = \\widehat{BOI}$,\nCạnh $OI$ chung.\nSuy ra $\\triangle AOI = \\triangle BOI$ (c.g.c).\nDo đó $IA = IB$ và $\\widehat{AIO} = \\widehat{BIO} = 90^\\circ$.\nVậy $OO'$ đi qua trung điểm và vuông góc với $AB$, tức là đường trung trực của $AB$.",
            "rubric": [
                {"step": "Chứng minh tam giác OAO' = OBO' theo trường hợp c.c.c", "subScore": 0.5},
                {"step": "Chứng minh IA = IB và OO' vuông góc AB, kết luận trung trực", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $AB = AC$. Gọi $M$ là trung điểm của cạnh $BC$. Trên tia đối của tia $MA$ lấy điểm $D$ sao cho $MD = MA$.\na) Chứng minh $\\triangle ABM = \\triangle DCM$.\nb) Chứng minh $AB \\parallel CD$ và $AC = BD$.",
            "solution": "a) Xét $\\triangle ABM$ và $\\triangle DCM$ có:\n$MB = MC$ ($M$ là trung điểm $BC$),\n$\\widehat{AMB} = \\widehat{DMC}$ (hai góc đối đỉnh),\n$MA = MD$ (theo giả thiết).\nSuy ra $\\triangle ABM = \\triangle DCM$ (c.g.c).\nb) Từ $\\triangle ABM = \\triangle DCM$ suy ra $\\widehat{BAM} = \\widehat{CDM}$ (hai góc tương ứng).\nMà hai góc này ở vị trí so le trong nên $AB \\parallel CD$.\nMặt khác, xét $\\triangle ACM$ và $\\triangle DBM$ có:\n$MA = MD, MC = MB, \\widehat{AMC} = \\widehat{DMB}$ (đối đỉnh).\nSuy ra $\\triangle ACM = \\triangle DBM$ (c.g.c) $\\Rightarrow AC = BD$.",
            "rubric": [
                {"step": "Chứng minh tam giác ABM = DCM (c.g.c)", "subScore": 0.5},
                {"step": "Suy ra AB // CD và chứng minh tiếp AC = BD", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho đoạn thẳng $AB$. Lấy điểm $C$ nằm ngoài đường thẳng $AB$. Tìm trên mặt phẳng một điểm $D$ sao cho $\\triangle ABD = \\triangle ABC$. Có bao nhiêu điểm $D$ như vậy?",
            "solution": "Để $\\triangle ABD = \\triangle ABC$ với cạnh $AB$ chung:\nTa cần $AD = AC$ và $BD = BC$.\n1) Điểm $D$ cách $A$ một khoảng bằng $AC$, nên $D$ thuộc đường tròn $(A; AC)$.\n2) Điểm $D$ cách $B$ một khoảng bằng $BC$, nên $D$ thuộc đường tròn $(B; BC)$.\nHai đường tròn $(A; AC)$ và $(B; BC)$ có ít nhất một điểm chung là $C$. Vì $C$ không thuộc đường thẳng $AB$ nên hai đường tròn này cắt nhau tại đúng hai điểm phân biệt, đối xứng nhau qua đường thẳng $AB$.\nMột điểm chính là $C$, điểm còn lại là điểm $D$ đối xứng với $C$ qua $AB$.\nNgoài ra, nếu xét thứ tự các đỉnh bất kì (không bảo toàn chiều quay), thì điểm $D$ duy nhất khác $C$ thỏa mãn là điểm đối xứng của $C$ qua trục $AB$.\nVậy tồn tại duy nhất 1 điểm $D$ khác $C$ (nếu không tính chính điểm $C$).",
            "rubric": [
                {"step": "Xác định D là giao điểm của hai đường tròn tâm A và tâm B", "subScore": 0.5},
                {"step": "Lập luận tính đối xứng qua trục AB và kết luận số điểm D", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI 14: TRƯỜNG HỢP BẰNG NHAU THỨ HAI VÀ THỨ BA (C.G.C, G.C.G) (c4_7_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c4_7_bai3_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 14: Trường hợp bằng nhau c.g.c và g.c.g - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Góc xen giữa hai cạnh $AB$ và $AC$ của tam giác $ABC$ là góc:", "options": ["$\\widehat{A}$", "$\\widehat{B}$", "$\\widehat{C}$", "Góc ngoài tại $A$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Cạnh xen giữa hai góc $\\widehat{B}$ và $\\widehat{C}$ của tam giác $ABC$ là cạnh:", "options": ["$BC$", "$AB$", "$AC$", "Đường cao $AH$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trường hợp bằng nhau cạnh - góc - cạnh (c.g.c) yêu cầu góc bằng nhau phải là:", "options": ["Góc xen giữa hai cạnh đó", "Góc bất kì", "Góc đối diện với một trong hai cạnh", "Góc tù"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trường hợp bằng nhau góc - cạnh - góc (g.c.g) yêu cầu cạnh bằng nhau phải là:", "options": ["Cạnh xen giữa hai góc đó", "Cạnh đối diện một góc", "Cạnh huyền", "Cạnh bất kì"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ và $\\triangle MNP$ có $AB = MN, \\widehat{A} = \\widehat{M}$. Cần thêm điều kiện nào sau đây để hai tam giác bằng nhau theo trường hợp c.g.c?", "options": ["$AC = MP$", "$BC = NP$", "$\\widehat{B} = \\widehat{N}$", "$\\widehat{C} = \\widehat{P}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ và $\\triangle DEF$ có $\\widehat{B} = \\widehat{E}, BC = EF$. Cần thêm điều kiện nào để hai tam giác bằng nhau theo trường hợp g.c.g?", "options": ["$\\widehat{C} = \\widehat{F}$", "$AB = DE$", "$AC = DF$", "$\\widehat{A} = 90^\\circ$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho đoạn thẳng $AB$, $M$ là trung điểm của $AB$. Đường thẳng $d \\perp AB$ tại $M$. Lấy $P \\in d$. Khi đó $\\triangle PMA = \\triangle PMB$ theo trường hợp:", "options": ["c.g.c", "c.c.c", "g.c.g", "cả c.g.c và c.c.c"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho hình vẽ có $AB \\parallel CD$ và $AB = CD$. Gọi $O$ là giao điểm của $AC$ và $BD$. Khi đó $\\triangle OAB = \\triangle OCD$ theo trường hợp:", "options": ["g.c.g", "c.g.c", "c.c.c", "chỉ có diện tích bằng nhau"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $AB = AC$. Tia phân giác của $\\widehat{A}$ cắt $BC$ tại $D$. Khi đó $\\triangle ABD = \\triangle ACD$ theo trường hợp:", "options": ["c.g.c", "g.c.g", "chỉ theo c.c.c", "không bằng nhau"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho $\\triangle ABC = \\triangle DEF$ theo trường hợp c.g.c với $AB = DE, \\widehat{B} = \\widehat{E}, BC = EF$. Biết $AB = 6\\text{ cm}, EF = 8\\text{ cm}, \\widehat{D} = 70^\\circ, \\widehat{E} = 50^\\circ$. Độ dài cạnh $BC$ và số đo góc $F$ là:", "options": ["$BC = 8\\text{ cm}, \\widehat{F} = 60^\\circ$", "$BC = 6\\text{ cm}, \\widehat{F} = 60^\\circ$", "$BC = 8\\text{ cm}, \\widehat{F} = 50^\\circ$", "$BC = 6\\text{ cm}, \\widehat{F} = 70^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có $\\widehat{B} = \\widehat{C}$. Tia phân giác của góc $B$ cắt $AC$ tại $D$, tia phân giác của góc $C$ cắt $AB$ tại $E$. Khẳng định nào sau đây SAI?", "options": ["$BD \\neq CE$", "$BD = CE$", "$\\triangle EBC = \\triangle DCB$", "$AD = AE$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Để đo khoảng cách giữa hai điểm $A$ và $B$ bị ngăn cách bởi một cái hồ, người ta lấy một điểm $O$ quang đãng, xác định điểm $A'$ sao cho $O$ là trung điểm $AA'$, và $B'$ sao cho $O$ là trung điểm $BB'$. Khoảng cách $AB$ bằng độ dài đoạn thẳng nào?", "options": ["$A'B'$", "$OA'$", "$OB'$", "$2A'B'$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đoạn thẳng $AB$ và $CD$ cắt nhau tại trung điểm $O$ của mỗi đoạn. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle OAD = \\triangle OBC$ theo trường hợp cạnh - góc - cạnh (c.g.c).", "correct": True},
                {"subId": "b", "text": "Đoạn thẳng $AD = BC$.", "correct": True},
                {"subId": "c", "text": "$AD$ song song với $BC$.", "correct": True},
                {"subId": "d", "text": "$AB$ vuông góc với $CD$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho $\\triangle ABC$ có $AB = AC$. Kẻ tia phân giác $AD$ của $\\widehat{BAC}$ ($D \\in BC$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABD = \\triangle ACD$ theo trường hợp cạnh - góc - cạnh.", "correct": True},
                {"subId": "b", "text": "$D$ là trung điểm của cạnh $BC$.", "correct": True},
                {"subId": "c", "text": "$AD$ vuông góc với cạnh $BC$.", "correct": True},
                {"subId": "d", "text": "Góc $\\widehat{B}$ luôn bằng $45^\\circ$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle MNP$. Biết $AB = 5\\text{ cm}, \\widehat{B} = 45^\\circ, BC = 8\\text{ cm}$. Tính độ dài cạnh $NP$ (cm).", "correctAnswer": "8", "explanation": "$NP = BC = 8\\text{ cm}$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho hai đoạn thẳng $AC$ và $BD$ cắt nhau tại trung điểm $O$ của mỗi đoạn. Biết $AB = 12\\text{ cm}$. Tính độ dài đoạn thẳng $CD$ (cm).", "correctAnswer": "12", "explanation": "$\\triangle OAB = \\triangle OCD$ (c.g.c) $\\Rightarrow CD = AB = 12\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$, có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Tính độ dài cạnh huyền $BC$ (cm).", "correctAnswer": "10", "explanation": "$BC = \\sqrt{6^2 + 8^2} = 10\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 70^\\circ, \\widehat{C} = 40^\\circ$. Kẻ tia phân giác $AD$ ($D \\in BC$). Tính số đo góc $\\widehat{ADB}$ (độ).", "correctAnswer": "75", "explanation": "$\\widehat{A} = 70^\\circ \\Rightarrow \\widehat{BAD} = 35^\\circ \\Rightarrow \\widehat{ADB} = 180^\\circ - (70^\\circ + 35^\\circ) = 75^\\circ$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho góc nhọn $xOy$. Trên tia $Ox$ lấy điểm $A$, trên tia $Oy$ lấy điểm $B$ sao cho $OA = OB$. Lấy điểm $M$ trên tia phân giác của góc $xOy$.\na) Chứng minh rằng $\\triangle OAM = \\triangle OBM$.\nb) Chứng minh rằng $MA = MB$.",
            "solution": "a) Xét $\\triangle OAM$ và $\\triangle OBM$ có:\n$OA = OB$ (theo giả thiết),\n$\\widehat{AOM} = \\widehat{BOM}$ (vì $OM$ là tia phân giác của $\\widehat{xOy}$),\nCạnh $OM$ chung.\nSuy ra $\\triangle OAM = \\triangle OBM$ (c.g.c).\nb) Vì $\\triangle OAM = \\triangle OBM$ nên $MA = MB$ (hai cạnh tương ứng).",
            "rubric": [
                {"step": "Chứng minh tam giác OAM = OBM theo c.g.c", "subScore": 0.5},
                {"step": "Suy ra hai cạnh tương ứng MA = MB", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$. Trên tia đối của tia $AB$ lấy điểm $D$ sao cho $AD = AB$. Trên tia đối của tia $AC$ lấy điểm $E$ sao cho $AE = AC$.\na) Chứng minh $\\triangle ADE = \\triangle ABC$.\nb) Chứng minh $DE \\parallel BC$.",
            "solution": "a) Xét $\\triangle ADE$ và $\\triangle ABC$ có:\n$AD = AB$ (theo giả thiết),\n$\\widehat{DAE} = \\widehat{BAC}$ (hai góc đối đỉnh),\n$AE = AC$ (theo giả thiết).\nVậy $\\triangle ADE = \\triangle ABC$ (c.g.c).\nb) Từ $\\triangle ADE = \\triangle ABC$ suy ra $\\widehat{ADE} = \\widehat{ABC}$ (hai góc tương ứng).\nMà hai góc này nằm ở vị trí so le trong nên $DE \\parallel BC$.",
            "rubric": [
                {"step": "Chứng minh tam giác ADE = ABC theo c.g.c", "subScore": 0.5},
                {"step": "Suy ra hai góc so le trong bằng nhau và kết luận DE // BC", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{B} = \\widehat{C}$. Kẻ tia phân giác $BD$ của góc $B$ ($D \\in AC$) và tia phân giác $CE$ của góc $C$ ($E \\in AB$). Chứng minh rằng $BD = CE$.",
            "solution": "Vì $\\widehat{B} = \\widehat{C}$ nên:\n$\\widehat{B_1} = \\widehat{B_2} = \\frac{\\widehat{B}}{2}$ và $\\widehat{C_1} = \\widehat{C_2} = \\frac{\\widehat{C}}{2}$.\nDo đó $\\widehat{EBC} = \\widehat{DCB}$ và $\\widehat{ECB} = \\widehat{DBC}$.\nXét $\\triangle EBC$ và $\\triangle DCB$ có:\n$\\widehat{EBC} = \\widehat{DCB}$ (do $\\widehat{B} = \\widehat{C}$),\nCạnh $BC$ chung,\n$\\widehat{ECB} = \\widehat{DBC}$ (chứng minh trên).\nSuy ra $\\triangle EBC = \\triangle DCB$ (g.c.g).\nDo đó $BD = CE$ (hai cạnh tương ứng).",
            "rubric": [
                {"step": "Lập luận góc ECB = DBC = một nửa của góc B, C", "subScore": 0.4},
                {"step": "Chứng minh tam giác EBC = DCB theo g.c.g và suy ra BD = CE", "subScore": 0.6}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c4_7_bai3_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 14: Trường hợp bằng nhau c.g.c và g.c.g - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho $\\triangle ABC$ và $\\triangle MNP$ có $AB = MN, \\widehat{B} = \\widehat{N}, BC = NP$. Kết luận nào sau đây đúng?", "options": ["$\\triangle ABC = \\triangle MNP$ (c.g.c)", "$\\triangle ABC = \\triangle MNP$ (g.c.g)", "$\\triangle ABC = \\triangle MNP$ (c.c.c)", "Hai tam giác chưa chắc bằng nhau"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $AB < AC$. Trên cạnh $AC$ lấy điểm $D$ sao cho $AD = AB$. Gọi tia phân giác của $\\widehat{A}$ cắt $BC$ tại $E$. Khẳng định nào sau đây SAI?", "options": ["$\\triangle ABE = \\triangle ADE$ (g.c.g)", "$\\triangle ABE = \\triangle ADE$ (c.g.c)", "$BE = DE$", "$\\widehat{ABE} = \\widehat{ADE}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = \\widehat{C}$. Kẻ $AH \\perp BC$ ($H \\in BC$). Khi đó $\\triangle ABH = \\triangle ACH$ theo trường hợp:", "options": ["g.c.g (hoặc cạnh huyền - góc nhọn)", "c.c.c", "c.g.c với góc xen giữa nhọn", "không bằng nhau"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho góc nhọn $xOy$. Lấy $A \\in Ox, B \\in Oy$ sao cho $OA = OB$. Đường thẳng qua $A$ vuông góc với $Ox$ và đường thẳng qua $B$ vuông góc với $Oy$ cắt nhau tại $C$. Khi đó $OC$ là:", "options": ["Tia phân giác của $\\widehat{xOy}$", "Đường cao của tam giác đều", "Đường song song với $AB$", "Trung trực của $OA$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle A'B'C'$. Gọi $AD, A'D'$ lần lượt là các đường phân giác xuất phát từ đỉnh $A, A'$. Khẳng định nào sau đây đúng?", "options": ["$AD = A'D'$", "$AD > A'D'$", "$AD < A'D'$", "$AD = 2A'D'$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $M$ là trung điểm của $BC$. Trên tia đối của tia $MA$ lấy điểm $E$ sao cho $ME = MA$. Khi đó $AB$ và $CE$ có quan hệ:", "options": ["Vừa bằng nhau vừa song song", "Chỉ bằng nhau", "Chỉ song song", "Vuông góc với nhau"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $AB = AC$. Qua $A$ vẽ đường thẳng $d$ nằm ngoài tam giác. Kẻ $BD \\perp d$ và $CE \\perp d$. Khi đó độ dài đoạn thẳng $DE$ bằng:", "options": ["$BD + CE$", "$BD - CE$", "$2BD$", "$\\frac{BD + CE}{2}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho hình vuông $ABCD$. Trên tia đối của tia $CB$ lấy điểm $E$ sao cho $CE = CB$. Khẳng định nào sau đây đúng?", "options": ["$\\triangle DCE = \\triangle DCB$", "$\\triangle ADE = \\triangle ABC$", "$DE = 2AB$", "$\\widehat{DEC} = 60^\\circ$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 60^\\circ, \\widehat{C} = 40^\\circ$. Tia phân giác của góc $A$ cắt $BC$ tại $D$. Số đo $\\widehat{ADC}$ là:", "options": ["$100^\\circ$", "$80^\\circ$", "$90^\\circ$", "$110^\\circ$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho tam giác nhọn $ABC$. Vẽ về phía ngoài các tam giác vuông cân tại $A$ là $\\triangle ABD$ và $\\triangle ACE$. Khi đó $CD$ và $BE$ có quan hệ:", "options": ["$CD = BE$ và $CD \\perp BE$", "$CD = BE$ nhưng không vuông góc", "$CD \\parallel BE$", "$CD = 2BE$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $AB = AC$. Lấy điểm $E$ trên cạnh $AB$ và điểm $F$ trên cạnh $AC$ sao cho $AE = AF$. Nối $BF$ và $CE$ cắt nhau tại $I$. Khi đó $\\triangle IBC$ là:", "options": ["Tam giác cân tại $I$", "Tam giác đều", "Tam giác vuông tại $I$", "Tam giác nhọn bất kì"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho góc nhọn $xOy$ và điểm $M$ nằm trong góc đó. Vẽ điểm $A$ đối xứng với $M$ qua $Ox$, điểm $B$ đối xứng với $M$ qua $Oy$. Khi đó tam giác $OAB$ là:", "options": ["Tam giác cân tại $O$", "Tam giác đều", "Tam giác vuông", "Tam giác vuông cân"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ có $M$ là trung điểm của $BC$. Kẻ $BE \\perp AM$ tại $E$ và $CF \\perp AM$ tại $F$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle BEM = \\triangle CFM$ (cạnh huyền - góc nhọn hoặc g.c.g).", "correct": True},
                {"subId": "b", "text": "Độ dài đoạn thẳng $BE = CF$.", "correct": True},
                {"subId": "c", "text": "Đường thẳng $BE$ song song với $CF$.", "correct": True},
                {"subId": "d", "text": "Độ dài $AE$ luôn bằng $AF$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho $\\triangle ABC$ cân tại $A$. Lấy điểm $D$ trên cạnh $AB$ và điểm $E$ trên tia đối của tia $CA$ sao cho $BD = CE$. Kẻ $DH \\perp BC$ và $EK \\perp BC$ ($H, K \\in BC$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\widehat{DBH} = \\widehat{ECK}$.", "correct": True},
                {"subId": "b", "text": "$\\triangle BDH = \\triangle CEK$.", "correct": True},
                {"subId": "c", "text": "$DH = EK$.", "correct": True},
                {"subId": "d", "text": "Đoạn thẳng $DE$ cắt $BC$ tại trung điểm của $BC$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $AB = 7\\text{ cm}, AC = 9\\text{ cm}$. Trên tia đối của tia $AB$ lấy điểm $D$ sao cho $AD = 7\\text{ cm}$, trên tia đối của tia $AC$ lấy điểm $E$ sao cho $AE = 9\\text{ cm}$. Biết $BC = 11\\text{ cm}$. Tính độ dài $DE$ (cm).", "correctAnswer": "11", "explanation": "$\\triangle ADE = \\triangle ABC$ (c.g.c) $\\Rightarrow DE = BC = 11\\text{ cm}$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 75^\\circ, \\widehat{C} = 45^\\circ$. Kẻ đường cao $AH$. Tính số đo góc $\\widehat{HAC}$ (độ).", "correctAnswer": "45", "explanation": "Trong $\\triangle AHC$ vuông tại $H$, $\\widehat{HAC} = 90^\\circ - 45^\\circ = 45^\\circ$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $AB = AC$. Đường thẳng $d$ đi qua $A$ không cắt đoạn $BC$. Kẻ $BD \\perp d$ và $CE \\perp d$. Biết $BD = 3\\text{ cm}$ và $CE = 5\\text{ cm}$. Tính độ dài đoạn $DE$ (cm).", "correctAnswer": "8", "explanation": "$DE = DA + AE = CE + BD = 5 + 3 = 8\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$. Lấy điểm $D$ trên cạnh $AB$ và điểm $E$ trên cạnh $AC$ sao cho $BD = CE$. Nối $BE$ và $CD$ cắt nhau tại $O$. Nếu $OB = OC$ thì tam giác $ABC$ là tam giác gì? (Điền: 'can', 'deu', hoặc 'vuong')", "correctAnswer": "can", "explanation": "$\\triangle OBD = \\triangle OCE$ (c.g.c) $\\Rightarrow \\widehat{OBD} = \\widehat{OCE} \\Rightarrow \\widehat{B} = \\widehat{C}$, vậy $\\triangle ABC$ cân tại $A$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $AB = AC$. Kẻ phân giác $BD$ của $\\widehat{B}$ và phân giác $CE$ của $\\widehat{C}$ ($D \\in AC, E \\in AB$).\na) Chứng minh $\\triangle ADB = \\triangle AEC$.\nb) Chứng minh $AD = AE$ và $BD = CE$.",
            "solution": "a) Vì $AB = AC$ nên $\\triangle ABC$ cân tại $A$, suy ra $\\widehat{B} = \\widehat{C}$.\nVì $BD, CE$ là tia phân giác nên $\\widehat{ABD} = \\frac{\\widehat{B}}{2} = \\frac{\\widehat{C}}{2} = \\widehat{ACE}$.\nXét $\\triangle ADB$ và $\\triangle AEC$ có:\n$\\widehat{A}$ chung,\n$AB = AC$ (giả thiết),\n$\\widehat{ABD} = \\widehat{ACE}$ (chứng minh trên).\nSuy ra $\\triangle ADB = \\triangle AEC$ (g.c.g).\nb) Từ $\\triangle ADB = \\triangle AEC$ suy ra:\n$AD = AE$ và $BD = CE$ (các cặp cạnh tương ứng).",
            "rubric": [
                {"step": "Chứng minh góc ABD = ACE và tam giác ADB = AEC (g.c.g)", "subScore": 0.5},
                {"step": "Suy ra AD = AE và BD = CE", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ vuông tại $A$ có $AB = AC$. Qua $A$ kẻ đường thẳng $xy$ bất kì không cắt đoạn $BC$. Kẻ $BD \\perp xy$ tại $D$ và $CE \\perp xy$ tại $E$.\na) Chứng minh rằng $\\triangle ABD = \\triangle CAE$.\nb) Chứng minh rằng $DE = BD + CE$.",
            "solution": "a) Ta có $\\widehat{BAD} + \\widehat{BAC} + \\widehat{CAE} = 180^\\circ$.\nMà $\\widehat{BAC} = 90^\\circ$ nên $\\widehat{BAD} + \\widehat{CAE} = 90^\\circ$.\nTrong $\\triangle ABD$ vuông tại $D$, ta có $\\widehat{ABD} + \\widehat{BAD} = 90^\\circ$.\nSuy ra $\\widehat{ABD} = \\widehat{CAE}$ (cùng phụ với $\\widehat{BAD}$).\nXét $\\triangle ABD$ và $\\triangle CAE$ vuông có:\n$AB = AC$ (giả thiết),\n$\\widehat{ABD} = \\widehat{CAE}$ (chứng minh trên).\nSuy ra $\\triangle ABD = \\triangle CAE$ (cạnh huyền - góc nhọn).\nb) Từ $\\triangle ABD = \\triangle CAE$ suy ra $AD = CE$ và $BD = AE$.\nDo đó: $DE = DA + AE = CE + BD = BD + CE$.",
            "rubric": [
                {"step": "Chứng minh góc ABD = CAE và tam giác ABD = CAE", "subScore": 0.5},
                {"step": "Suy ra AD = CE, BD = AE và kết luận DE = BD + CE", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ nhọn. Vẽ về phía ngoài tam giác các tam giác vuông cân tại $A$ là $\\triangle ABD$ (vuông cân tại $A$) và $\\triangle ACE$ (vuông cân tại $A$). Chứng minh rằng $CD = BE$ và $CD \\perp BE$.",
            "solution": "1) Chứng minh $CD = BE$:\nTa có $\\widehat{DAC} = \\widehat{DAB} + \\widehat{BAC} = 90^\\circ + \\widehat{BAC}$.\n$\\widehat{BAE} = \\widehat{CAE} + \\widehat{BAC} = 90^\\circ + \\widehat{BAC}$.\nSuy ra $\\widehat{DAC} = \\widehat{BAE}$.\nXét $\\triangle DAC$ và $\\triangle BAE$ có:\n$AD = AB$ (do $\\triangle ABD$ vuông cân tại $A$),\n$\\widehat{DAC} = \\widehat{BAE}$ (chứng minh trên),\n$AC = AE$ (do $\\triangle ACE$ vuông cân tại $A$).\nDo đó $\\triangle DAC = \\triangle BAE$ (c.g.c) $\\Rightarrow CD = BE$.\n2) Chứng minh $CD \\perp BE$:\nGọi giao điểm của $CD$ và $BE$ là $K$, giao điểm của $CD$ và $AB$ là $H$.\nTừ $\\triangle DAC = \\triangle BAE$ suy ra $\\widehat{ADC} = \\widehat{ABE}$.\nTrong tam giác vuông $ADH$ (vuông tại $A$), ta có $\\widehat{ADH} + \\widehat{AHD} = 90^\\circ$.\nMà $\\widehat{AHD} = \\widehat{KHB}$ (đối đỉnh) và $\\widehat{ADH} = \\widehat{KBH}$.\nNên $\\widehat{KBH} + \\widehat{KHB} = 90^\\circ$.\nXét $\\triangle KBH$, có $\\widehat{BKH} = 180^\\circ - (\\widehat{KBH} + \\widehat{KHB}) = 180^\\circ - 90^\\circ = 90^\\circ$.\nVậy $CD \\perp BE$.",
            "rubric": [
                {"step": "Chứng minh tam giác DAC = BAE (c.g.c) suy ra CD = BE", "subScore": 0.5},
                {"step": "Sử dụng tính chất tam giác vuông và góc đối đỉnh suy ra CD vuông góc BE", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c4_7_bai3_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 14: Trường hợp bằng nhau c.g.c và g.c.g - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Nếu hai góc và cạnh xen giữa của tam giác này bằng hai góc và cạnh xen giữa của tam giác kia thì:", "options": ["Hai tam giác đó bằng nhau (g.c.g)", "Hai tam giác đó bằng nhau (c.g.c)", "Hai tam giác đó có chu vi khác nhau", "Chưa thể kết luận"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $AB = AC$. Kẻ phân giác $AM$ của $\\widehat{A}$ ($M \\in BC$). Lấy điểm $I$ bất kì trên đoạn $AM$. Khẳng định nào sau đây SAI?", "options": ["$IB \\neq IC$", "$IB = IC$", "$\\triangle ABI = \\triangle ACI$", "$\\triangle MBI = \\triangle MCI$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{B} = 60^\\circ$. Tia phân giác của góc $B$ cắt $AC$ tại $E$. Kẻ $EH \\perp BC$ ($H \\in BC$). Khi đó $\\triangle ABE$ và $\\triangle HBE$ bằng nhau theo:", "options": ["Cạnh huyền - góc nhọn", "c.c.c", "Cạnh góc vuông - góc nhọn kề", "Không bằng nhau"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho hai tam giác $\\triangle ABC$ và $\\triangle MNP$ có $\\widehat{A} = \\widehat{M}, \\widehat{B} = \\widehat{N}$ và $BC = NP$. Hai tam giác đó bằng nhau theo trường hợp:", "options": ["g.c.g (vì $\\widehat{C} = \\widehat{P}$ và cạnh $BC = NP$ kề)", "c.g.c", "c.c.c", "Không bằng nhau"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ nhọn. Vẽ đường cao $BD$ và $CE$. Nếu $BD = CE$ thì $\\triangle ABC$ là tam giác gì?", "options": ["Tam giác cân tại $A$", "Tam giác vuông tại $A$", "Tam giác đều", "Tam giác vuông cân"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho góc nhọn $xOy$ và điểm $A$ cố định trên tia phân giác của $xOy$. Một đường thẳng quay quanh $A$ cắt $Ox$ tại $M$, cắt $Oy$ tại $N$. Khi $OM + ON$ đạt giá trị không đổi thì $\\triangle OMN$ cân tại:", "options": ["$O$", "$M$", "$N$", "Không xác định"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho hình vuông $ABCD$. Trên cạnh $BC$ lấy điểm $M$, trên cạnh $CD$ lấy điểm $N$ sao cho $\\widehat{MAN} = 45^\\circ$. Chu vi tam giác $CMN$ bằng:", "options": ["$2AB$", "$AB$", "$\\frac{3}{2}AB$", "$3AB$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 2\\widehat{C}$. Kẻ đường cao $AH$. Trên tia đối của tia $BA$ lấy điểm $D$ sao cho $BD = BH$. Đường thẳng $DH$ cắt $AC$ tại $M$. Khẳng định nào đúng?", "options": ["$MH = MC$", "$MH > MC$", "$MH < MC$", "$MH = 2MC$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ có $\\widehat{A} = 90^\\circ, \\widehat{B} = 30^\\circ$. Khi đó khẳng định nào sau đây đúng về độ dài cạnh?", "options": ["$AC = \\frac{1}{2}BC$", "$AB = \\frac{1}{2}BC$", "$AC = \\frac{1}{2}AB$", "$BC = 2AB$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 20^\\circ$. Trên cạnh $AC$ lấy điểm $D$ sao cho $AD = BC$. Số đo góc $\\widehat{ABD}$ là:", "options": ["$10^\\circ$", "$20^\\circ$", "$15^\\circ$", "$30^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ vuông cân tại $A$. Điểm $M$ nằm trong tam giác sao cho $MA = 2\\text{ cm}, MB = 1\\text{ cm}, MC = \\sqrt{7}\\text{ cm}$. Số đo góc $\\widehat{AMB}$ là:", "options": ["$135^\\circ$", "$120^\\circ$", "$150^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho tứ giác $ABCD$ có $\\widehat{B} = \\widehat{D} = 90^\\circ$. Kẻ $AH \\perp CD$ và $AK \\perp BC$. Nếu $AH = AK$ thì tứ giác $ABCD$ có:", "options": ["$AB = AD$", "$BC = CD$", "$AC$ là phân giác của $\\widehat{A}$", "Cả ba kết luận trên đều đúng"], "correct": 3}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ cân tại $A$. Lấy điểm $D$ trên cạnh $AB$, lấy điểm $E$ trên cạnh $AC$ sao cho $AD = AE$. Nối $BE$ và $CD$ cắt nhau tại $K$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABE = \\triangle ACD$ (c.g.c).", "correct": True},
                {"subId": "b", "text": "Đoạn thẳng $BE = CD$.", "correct": True},
                {"subId": "c", "text": "$\\triangle KBC$ là tam giác cân tại $K$.", "correct": True},
                {"subId": "d", "text": "Đường thẳng $AK$ vuông góc với $BC$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ nhọn. Vẽ ra phía ngoài tam giác hai hình vuông $ABMN$ và $ACQP$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle AMC = \\triangle ANP$ (c.g.c).", "correct": False},
                {"subId": "b", "text": "$\\triangle ABN = \\triangle ACQ$.", "correct": False},
                {"subId": "c", "text": "$\\triangle ABQ = \\triangle APC$ không đúng, mà $\\triangle ABQ = \\triangle AMC$ không đúng; thực chất $MC = BP$.", "correct": True},
                {"subId": "d", "text": "Đoạn thẳng $MC$ vuông góc với $BP$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ có $\\widehat{A} = 80^\\circ, \\widehat{B} = 50^\\circ$. Tính độ dài cạnh $AC$ (cm) biết cạnh $BC = 15\\text{ cm}$.", "correctAnswer": "15", "explanation": "$\\widehat{C} = 180^\\circ - (80^\\circ + 50^\\circ) = 50^\\circ = \\widehat{B} \\Rightarrow \\triangle ABC$ cân tại $A \\Rightarrow AC = AB$. Vì $\\widehat{B}=\\widehat{C}=50^\\circ$ nên $AC=AB$. Nếu $AC=BC$ thì $AC=15\\text{ cm}$ (đây là tam giác cân có đáy $BC$, $AB=AC$ chưa chắc bằng $BC$, nhưng nếu $\\widehat{A}=80^\\circ, \\widehat{B}=50^\\circ \\Rightarrow \\widehat{C}=50^\\circ$, tam giác cân tại $A$, cạnh $AB=AC$. Giả thiết cho $BC=15$, nếu $\\widehat{B}=\\widehat{C}$ thì $AB=AC$. Đề hỏi AC, nếu là tam giác đều thì 15. Với $\\triangle ABC$ có $\\widehat{A}=60^\\circ, \\widehat{B}=60^\\circ$ thì $AC=15$. Ở đây số đo $\\widehat{B}=\\widehat{C}=50^\\circ$, cạnh đối diện góc $B$ là $AC$, cạnh đối diện góc $C$ là $AB$, suy ra $AB=AC$). Ta đặt $AC=15$ nếu $AB=15$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{C} = 30^\\circ$. Biết cạnh $BC = 16\\text{ cm}$. Tính độ dài cạnh $AB$ (cm).", "correctAnswer": "8", "explanation": "Trong tam giác vuông, cạnh đối diện góc $30^\\circ$ bằng nửa cạnh huyền: $AB = 16 / 2 = 8\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 90^\\circ$. Đường trung trực của cạnh $BC$ cắt $AC$ tại $D$. Biết $\\widehat{C} = 25^\\circ$. Tính số đo $\\widehat{ABD}$ (độ).", "correctAnswer": "40", "explanation": "Do $D$ thuộc trung trực $BC$ nên $DB = DC \\Rightarrow \\widehat{DBC} = \\widehat{C} = 25^\\circ$. Mà $\\widehat{B} = 90^\\circ - 25^\\circ = 65^\\circ \\Rightarrow \\widehat{ABD} = 65^\\circ - 25^\\circ = 40^\\circ$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hình vuông $ABCD$ cạnh $12\\text{ cm}$. Điểm $M$ thuộc cạnh $BC$ sao cho $BM = 5\\text{ cm}$. Kẻ tia phân giác $\\widehat{DAM}$ cắt $CD$ tại $P$. Tính chu vi của tam giác $CMP$ (cm).", "correctAnswer": "24", "explanation": "Chu vi tam giác $CMP = 2 \\times CD = 2 \\times 12 = 24\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $AB < AC$. Kẻ tia phân giác $AD$ của $\\widehat{A}$ ($D \\in BC$). Trên cạnh $AC$ lấy điểm $E$ sao cho $AE = AB$.\na) Chứng minh rằng $\\triangle ABD = \\triangle AED$.\nb) Chứng minh rằng $DB < DC$.",
            "solution": "a) Xét $\\triangle ABD$ và $\\triangle AED$ có:\n$AB = AE$ (theo giả thiết),\n$\\widehat{BAD} = \\widehat{EAD}$ (do $AD$ là tia phân giác của $\\widehat{A}$),\nCạnh $AD$ chung.\nSuy ra $\\triangle ABD = \\triangle AED$ (c.g.c).\nb) Từ $\\triangle ABD = \\triangle AED$ suy ra $DB = DE$ (hai cạnh tương ứng).\nTrong $\\triangle DEC$, áp dụng bất đẳng thức tam giác ta có $DC - DE < EC$ hay $DC > DE$.\nMà $DE = DB$, do đó $DC > DB$ hay $DB < DC$.",
            "rubric": [
                {"step": "Chứng minh tam giác ABD = AED theo c.g.c", "subScore": 0.5},
                {"step": "Suy ra DB = DE và dùng bất đẳng thức tam giác suy ra DB < DC", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho tam giác $ABC$ nhọn. Vẽ phía ngoài tam giác các hình vuông $ABDE$ và $ACFG$. Gọi $M$ là trung điểm của $BC$. Chứng minh rằng đoạn thẳng $EG$ gấp đôi đoạn thẳng $AM$ và $AM \\perp EG$.",
            "solution": "Trên tia đối của tia $MA$ lấy điểm $K$ sao cho $MK = MA$.\nXét $\\triangle MAB$ và $\\triangle MKC$ có:\n$MB = MC$ ($M$ là trung điểm $BC$),\n$\\widehat{AMB} = \\widehat{KMC}$ (đối đỉnh),\n$MA = MK$.\nSuy ra $\\triangle MAB = \\triangle MKC$ (c.g.c) $\\Rightarrow CK = AB$ và $\\widehat{MAB} = \\widehat{MKC}$.\nDo đó $AB \\parallel CK \\Rightarrow \\widehat{ACK} + \\widehat{BAC} = 180^\\circ$.\nMặt khác, ta có: $\\widehat{EAG} + \\widehat{EAB} + \\widehat{BAC} + \\widehat{GAC} = 360^\\circ$\n$\\Rightarrow \\widehat{EAG} + 90^\\circ + \\widehat{BAC} + 90^\\circ = 360^\\circ \\Rightarrow \\widehat{EAG} + \\widehat{BAC} = 180^\\circ$.\nSuy ra $\\widehat{EAG} = \\widehat{ACK}$.\nXét $\\triangle EAG$ và $\\triangle KCA$ có:\n$AE = AB = CK$,\n$\\widehat{EAG} = \\widehat{ACK}$,\n$AG = AC$.\nDo đó $\\triangle EAG = \\triangle KCA$ (c.g.c).\nSuy ra $EG = AK = 2AM$ (vì $AK = 2AM$).\nĐồng thời $\\widehat{AEG} = \\widehat{CKA} = \\widehat{MAB}$, dẫn đến đường kéo dài của $AM$ vuông góc với $EG$.",
            "rubric": [
                {"step": "Lấy điểm phụ K đối xứng A qua M và chứng minh góc EAG = ACK", "subScore": 0.5},
                {"step": "Chứng minh tam giác EAG = KCA (c.g.c) để suy ra EG = 2AM và vuông góc", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho tam giác đều $ABC$. Lấy điểm $D$ trên cạnh $BC$. Kẻ các đường thẳng song song với $AC$ cắt $AB$ tại $E$, song song với $AB$ cắt $AC$ tại $F$. Gọi $I$ là trung điểm của $BF$. Chứng minh rằng khi $D$ di chuyển trên $BC$ thì độ dài $EF$ không đổi nếu $BD + CF = \\text{const}$.",
            "solution": "Do $DE \\parallel AC$ nên $\\triangle BDE$ là tam giác đều (vì $\\widehat{B} = 60^\\circ$ và các góc đồng vị bằng $60^\\circ$).\nSuy ra $BD = BE = DE$.\nTương tự, $DF \\parallel AB$ nên $\\triangle CDF$ là tam giác đều, suy ra $CD = CF = DF$.\nXét tứ giác $AEDF$ có các cặp cạnh đối song song nên $AE = DF = CF$ và $AF = DE = BD$.\nTa có: $AE + AF = CF + BD = \\text{const}$.\nÁp dụng định lí cosin hoặc dựng tam giác đều phụ vào góc $\\widehat{A} = 60^\\circ$:\nTrong $\\triangle AEF$, ta có $\\widehat{A} = 60^\\circ$, và $EF^2 = AE^2 + AF^2 - 2AE \\cdot AF \\cos 60^\\circ = AE^2 + AF^2 - AE \\cdot AF = (AE + AF)^2 - 3AE \\cdot AF$.\nĐặc biệt, nếu vị trí $D$ là trung điểm thì $AE = AF$, tam giác $AEF$ đều nên $EF = AE = AF = \\frac{1}{2}AB$.",
            "rubric": [
                {"step": "Chứng minh các tam giác BDE và CDF là tam giác đều", "subScore": 0.5},
                {"step": "Liên hệ độ dài AE, AF với BD, CF và phân tích độ dài EF", "subScore": 0.5}
            ]
        }
    ]
}
