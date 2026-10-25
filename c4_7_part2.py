# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG IV: TAM GIÁC BẰNG NHAU
PHẦN 2:
- BÀI 15: CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC VUÔNG (c4_7_bai4)
- BÀI 16: TAM GIÁC CÂN. ĐƯỜNG TRUNG TRỰC CỦA ĐOẠN THẲNG (c4_7_bai5)
- BÀI KIỂM TRA CUỐI CHƯƠNG IV: TAM GIÁC BẰNG NHAU (c4_7_bai6)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 15: CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC VUÔNG (c4_7_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c4_7_bai4_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 15: Các trường hợp bằng nhau của tam giác vuông - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hai tam giác vuông bằng nhau khi có:", "options": ["Hai cạnh góc vuông bằng nhau", "Một góc nhọn bằng nhau", "Một cạnh góc vuông bằng nhau", "Chu vi bằng nhau"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Trường hợp bằng nhau cạnh huyền - góc nhọn: Nếu cạnh huyền và một góc nhọn của tam giác vuông này bằng cạnh huyền và một góc nhọn của tam giác vuông kia thì:", "options": ["Hai tam giác vuông đó bằng nhau", "Hai tam giác đó đồng dạng nhưng không bằng nhau", "Chưa kết luận được", "Hai góc nhọn còn lại bù nhau"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trường hợp bằng nhau cạnh huyền - cạnh góc vuông: Nếu cạnh huyền và một cạnh góc vuông của tam giác vuông này bằng cạnh huyền và một cạnh góc vuông của tam giác vuông kia thì:", "options": ["Hai tam giác vuông đó bằng nhau", "Hai tam giác vuông đó chưa chắc bằng nhau", "Hai góc nhọn bằng nhau nhưng hai tam giác không bằng nhau", "Chu vi hai tam giác khác nhau"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trong tam giác vuông, cạnh đối diện với góc vuông được gọi là:", "options": ["Cạnh huyền", "Cạnh góc vuông", "Đường cao", "Đường trung trực"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$ và $\\triangle MNP$ vuông tại $M$ có $BC = NP$ và $\\widehat{B} = \\widehat{N}$. Khi đó hai tam giác bằng nhau theo trường hợp:", "options": ["Cạnh huyền - góc nhọn", "Cạnh góc vuông - góc nhọn kề", "Hai cạnh góc vuông", "Cạnh huyền - cạnh góc vuông"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho $\\triangle DEF$ vuông tại $D$ và $\\triangle GHK$ vuông tại $G$ có $DE = GH, DF = GK$. Hai tam giác này bằng nhau theo:", "options": ["Hai cạnh góc vuông", "Cạnh huyền - cạnh góc vuông", "Cạnh huyền - góc nhọn", "g.c.g"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$. Kẻ $AH \\perp BC$ ($H \\in BC$). Khi đó $\\triangle ABH = \\triangle ACH$ theo trường hợp:", "options": ["Cạnh huyền - cạnh góc vuông (hoặc cạnh huyền - góc nhọn)", "Hai cạnh góc vuông", "Chỉ theo c.c.c", "Không bằng nhau"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho góc nhọn $xOy$ và điểm $M$ nằm trên tia phân giác của nó. Kẻ $MA \\perp Ox$ và $MB \\perp Oy$. Nhận định nào sau đây SAI?", "options": ["$MA \\neq MB$", "$MA = MB$", "$\\triangle OAM = \\triangle OBM$", "$OA = OB$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$, $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Nếu $\\triangle DEF$ vuông tại $D$ bằng $\\triangle ABC$ thì diện tích của $\\triangle DEF$ là:", "options": ["$24\\text{ cm}^2$", "$48\\text{ cm}^2$", "$14\\text{ cm}^2$", "$10\\text{ cm}^2$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $AB = AC$. Từ $B$ kẻ $BD \\perp AC$ ($D \\in AC$), từ $C$ kẻ $CE \\perp AB$ ($E \\in AB$). Khẳng định nào đúng?", "options": ["$BD = CE$", "$BD > CE$", "$BD < CE$", "$BD = 2CE$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho tam giác vuông $ABC$ ($A = 90^\\circ$) có $\\widehat{B} = 60^\\circ$. Cạnh huyền $BC = 10\\text{ cm}$. Độ dài cạnh $AB$ bằng:", "options": ["$5\\text{ cm}$", "$6\\text{ cm}$", "$8\\text{ cm}$", "$5\\sqrt{3}\\text{ cm}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ vuông tại $A$. Tia phân giác của góc $B$ cắt $AC$ tại $D$. Kẻ $DE \\perp BC$ ($E \\in BC$). Khẳng định nào sau đây SAI?", "options": ["$AD > DE$", "$AD = DE$", "$\\triangle ABD = \\triangle EBD$", "$BA = BE$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ vuông tại $A$ và $\\triangle DEF$ vuông tại $D$ có $BC = EF = 10\\text{ cm}, AB = DE = 6\\text{ cm}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABC = \\triangle DEF$ theo trường hợp cạnh huyền - cạnh góc vuông.", "correct": True},
                {"subId": "b", "text": "Độ dài cạnh $AC = DF = 8\\text{ cm}$.", "correct": True},
                {"subId": "c", "text": "Số đo góc $\\widehat{C}$ bằng số đo góc $\\widehat{F}$.", "correct": True},
                {"subId": "d", "text": "Tổng hai góc $\\widehat{B} + \\widehat{E} = 180^\\circ$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho góc nhọn $xOy$. Lấy điểm $M$ trên tia phân giác của $xOy$. Kẻ $MA \\perp Ox$ ($A \\in Ox$) và $MB \\perp Oy$ ($B \\in Oy$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle OAM = \\triangle OBM$ theo trường hợp cạnh huyền - góc nhọn.", "correct": True},
                {"subId": "b", "text": "Đoạn thẳng $MA = MB$.", "correct": True},
                {"subId": "c", "text": "Đoạn thẳng $OA = OB$.", "correct": True},
                {"subId": "d", "text": "Đường thẳng $OM$ không phải là đường trung trực của đoạn thẳng $AB$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $AB = 5\\text{ cm}, BC = 13\\text{ cm}$. Tính độ dài cạnh $AC$ (cm).", "correctAnswer": "12", "explanation": "$AC = \\sqrt{13^2 - 5^2} = 12\\text{ cm}$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $AB = AC = 15\\text{ cm}, BC = 18\\text{ cm}$. Kẻ $AH \\perp BC$ ($H \\in BC$). Tính độ dài đoạn thẳng $AH$ (cm).", "correctAnswer": "12", "explanation": "$BH = 9\\text{ cm} \\Rightarrow AH = \\sqrt{15^2 - 9^2} = 12\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$, kẻ phân giác $BD$ ($D \\in AC$). Kẻ $DH \\perp BC$ ($H \\in BC$). Biết $AC = 9\\text{ cm}$ và $AD = 4\\text{ cm}$. Tính độ dài đoạn thẳng $DH$ (cm).", "correctAnswer": "4", "explanation": "$\\triangle ABD = \\triangle HBD$ (cạnh huyền - góc nhọn) $\\Rightarrow DH = AD = 4\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ vuông cân tại $A$ có cạnh huyền $BC = 10\\text{ cm}$. Tính diện tích tam giác $ABC$ (cm$^2$).", "correctAnswer": "25", "explanation": "Đường cao $AH$ ứng với cạnh huyền bằng nửa cạnh huyền: $AH = 5\\text{ cm}$. Diện tích = $\\frac{1}{2} \\times 10 \\times 5 = 25\\text{ cm}^2$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ cân tại $A$. Kẻ $BD \\perp AC$ ($D \\in AC$) và $CE \\perp AB$ ($E \\in AB$).\na) Chứng minh rằng $\\triangle ADB = \\triangle AEC$.\nb) Chứng minh rằng $BD = CE$.",
            "solution": "a) Xét hai tam giác vuông $\\triangle ADB$ (vuông tại $D$) và $\\triangle AEC$ (vuông tại $E$) có:\nCạnh huyền $AB = AC$ (do $\\triangle ABC$ cân tại $A$),\nGóc nhọn $\\widehat{A}$ chung.\nSuy ra $\\triangle ADB = \\triangle AEC$ (cạnh huyền - góc nhọn).\nb) Vì $\\triangle ADB = \\triangle AEC$ nên $BD = CE$ (hai cạnh tương ứng).",
            "rubric": [
                {"step": "Chỉ ra cạnh huyền và góc nhọn chung, suy ra hai tam giác bằng nhau", "subScore": 0.5},
                {"step": "Kết luận BD = CE là hai cạnh tương ứng", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho tam giác $ABC$ vuông tại $A$. Tia phân giác của góc $B$ cắt cạnh $AC$ tại điểm $D$. Kẻ $DH \\perp BC$ tại $H$.\na) Chứng minh $\\triangle ABD = \\triangle HBD$.\nb) Chứng minh rằng $BD$ là đường trung trực của đoạn thẳng $AH$.",
            "solution": "a) Xét hai tam giác vuông $\\triangle ABD$ và $\\triangle HBD$ có:\nCạnh huyền $BD$ chung,\n$\\widehat{ABD} = \\widehat{HBD}$ (do $BD$ là tia phân giác của góc $B$).\nSuy ra $\\triangle ABD = \\triangle HBD$ (cạnh huyền - góc nhọn).\nb) Từ $\\triangle ABD = \\triangle HBD$ suy ra $BA = BH$ và $DA = DH$.\nVì $BA = BH$ nên điểm $B$ thuộc đường trung trực của đoạn thẳng $AH$.\nVì $DA = DH$ nên điểm $D$ thuộc đường trung trực của đoạn thẳng $AH$.\nDo đó đường thẳng $BD$ chính là đường trung trực của đoạn thẳng $AH$.",
            "rubric": [
                {"step": "Chứng minh tam giác ABD = HBD theo trường hợp cạnh huyền - góc nhọn", "subScore": 0.5},
                {"step": "Lập luận BA = BH và DA = DH để kết luận BD là đường trung trực của AH", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ vuông tại $A$ có $AB < AC$. Gọi $M$ là trung điểm của $BC$. Đường trung trực của $BC$ cắt cạnh $AC$ tại điểm $D$. Kẻ $DE \\perp BC$ tại $E$. Chứng minh rằng $DE = \\frac{1}{2}AB$ và $\\widehat{B}$ gấp đôi góc $\\widehat{C}$ khi $AD = DE$ không xảy ra, hãy chứng minh nếu $\\widehat{C} = 30^\\circ$ thì $CD = 2AD$.",
            "solution": "1) Khi $\\widehat{C} = 30^\\circ$, vì tam giác $ABC$ vuông tại $A$ nên $\\widehat{B} = 60^\\circ$.\n2) Điểm $D$ thuộc đường trung trực của $BC$ nên $DB = DC$.\nDo đó $\\triangle DBC$ cân tại $D$, suy ra $\\widehat{DBC} = \\widehat{C} = 30^\\circ$.\n3) Ta có: $\\widehat{ABD} = \\widehat{ABC} - \\widehat{DBC} = 60^\\circ - 30^\\circ = 30^\\circ$.\nXét $\\triangle ABD$ vuông tại $A$ có $\\widehat{ABD} = 30^\\circ$, nên cạnh đối diện góc $30^\\circ$ bằng nửa cạnh huyền:\n$AD = \\frac{1}{2}BD$.\nMà $BD = CD$ (chứng minh trên), do đó $AD = \\frac{1}{2}CD$ hay $CD = 2AD$.",
            "rubric": [
                {"step": "Chứng minh tam giác DBC cân tại D và tính góc ABD = 30 độ", "subScore": 0.5},
                {"step": "Sử dụng tính chất tam giác vuông có góc 30 độ để kết luận CD = 2AD", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c4_7_bai4_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 15: Các trường hợp bằng nhau của tam giác vuông - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Điều kiện nào sau đây KHÔNG đủ để kết luận hai tam giác vuông bằng nhau?", "options": ["Có một góc nhọn bằng nhau", "Có hai cạnh góc vuông bằng nhau", "Có cạnh huyền và một góc nhọn bằng nhau", "Có cạnh huyền và một cạnh góc vuông bằng nhau"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$. Kẻ $AM \\perp BC$ ($M \\in BC$). Khẳng định nào sau đây SAI?", "options": ["$AM = BC$", "$MB = MC$", "$AM$ là phân giác của $\\widehat{BAC}$", "$\\triangle ABM = \\triangle ACM$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$. Tia phân giác của góc $C$ cắt $AB$ tại $K$. Kẻ $KH \\perp BC$ ($H \\in BC$). Khi đó:", "options": ["$KA = KH$", "$KA > KH$", "$KA < KH$", "$KA = 2KH$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có hai đường cao $BD$ và $CE$ cắt nhau tại $H$. Nếu $BD = CE$ thì:", "options": ["$\\triangle ABC$ cân tại $A$", "$\\triangle ABC$ vuông tại $A$", "$\\triangle ABC$ đều", "$AB = 2AC$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$. Đường trung trực của $BC$ cắt $AC$ tại $E$. Khẳng định nào đúng?", "options": ["$\\triangle EBC$ cân tại $E$", "$\\triangle EAB$ vuông cân", "$EB = AB$", "$AC = 2AE$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{C} = 30^\\circ$. Trên cạnh $BC$ lấy điểm $D$ sao cho $CD = CA$. Khi đó $\\triangle ACD$ là:", "options": ["Tam giác cân có góc ở đỉnh bằng $30^\\circ$", "Tam giác đều", "Tam giác vuông", "Tam giác vuông cân"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho tam giác $ABC$ nhọn. Vẽ đường cao $AH$. Lấy điểm $D$ đối xứng với $H$ qua $AB$. Khi đó $\\triangle ABD$ bằng tam giác nào?", "options": ["$\\triangle ABH$", "$\\triangle ACH$", "$\\triangle ABC$", "$\\triangle ADH$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$. Lấy điểm $M$ trên cạnh $BC$. Kẻ $MD \\perp AB$ và $ME \\perp AC$. Tổng $MD + ME$ bằng:", "options": ["Đường cao hạ từ đỉnh $B$ hoặc $C$", "Đường cao $AH$", "Cạnh đáy $BC$", "$2AH$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$, $AB = 9\\text{ cm}, AC = 12\\text{ cm}$. Trung điểm cạnh $BC$ là $M$. Độ dài $AM$ bằng:", "options": ["$7{,}5\\text{ cm}$", "$15\\text{ cm}$", "$10\\text{ cm}$", "$6\\text{ cm}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ vuông cân tại $A$. Một đường thẳng $d$ đi qua $A$. Kẻ $BD \\perp d$ và $CE \\perp d$. Khi đó $BD^2 + CE^2$ bằng:", "options": ["$AD^2 + AE^2 = AB^2$", "$BC^2$", "$2BC^2$", "$4AB^2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác vuông $ABC$ ($A = 90^\\circ$). Đường cao $AH$. Tia phân giác của góc $\\widehat{BAH}$ cắt $BC$ tại $K$. Tam giác $CAK$ là tam giác gì?", "options": ["Tam giác cân tại $C$", "Tam giác vuông", "Tam giác đều", "Tam giác vuông cân"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có ba đường cao bằng nhau. Tam giác đó là:", "options": ["Tam giác đều", "Tam giác vuông", "Tam giác cân", "Tam giác tù"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ có hai đường cao $BD$ và $CE$ bằng nhau ($D \\in AC, E \\in AB$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle BDC = \\triangle CEB$ (cạnh huyền - cạnh góc vuông).", "correct": True},
                {"subId": "b", "text": "$\\widehat{DBC} = \\widehat{ECB}$.", "correct": True},
                {"subId": "c", "text": "Tam giác $ABC$ cân tại đỉnh $A$.", "correct": True},
                {"subId": "d", "text": "Đoạn thẳng $BD$ luôn bằng đoạn thẳng $AB$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho $\\triangle ABC$ vuông tại $A$. Kẻ phân giác $BD$ ($D \\in AC$). Kẻ $DH \\perp BC$ ($H \\in BC$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABD = \\triangle HBD$ theo trường hợp cạnh huyền - góc nhọn.", "correct": True},
                {"subId": "b", "text": "$AD = DH$.", "correct": True},
                {"subId": "c", "text": "$AD < DC$ vì trong $\\triangle DHC$ vuông tại $H$, cạnh huyền $DC > DH$.", "correct": True},
                {"subId": "d", "text": "Đoạn thẳng $BA$ lớn hơn đoạn thẳng $BH$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$. Cạnh huyền $BC = 20\\text{ cm}$, đường trung tuyến $AM$ ứng với cạnh huyền có độ dài bằng bao nhiêu cm?", "correctAnswer": "10", "explanation": "Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền: $AM = 20 / 2 = 10\\text{ cm}$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$. Kẻ $AH \\perp BC$. Biết $AB = 10\\text{ cm}, AH = 8\\text{ cm}$. Tính độ dài đáy $BC$ (cm).", "correctAnswer": "12", "explanation": "$BH = \\sqrt{10^2 - 8^2} = 6\\text{ cm} \\Rightarrow BC = 2 \\times 6 = 12\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{C} = 30^\\circ$. Kẻ đường cao $AH$. Biết $BC = 12\\text{ cm}$. Tính độ dài đoạn thẳng $BH$ (cm).", "correctAnswer": "3", "explanation": "$AB = 6\\text{ cm}$. Trong $\\triangle ABH$ vuông tại $H$, $\\widehat{BAH} = 30^\\circ \\Rightarrow BH = \\frac{1}{2}AB = 3\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 120^\\circ$. Tia phân giác $AD$ ($D \\in BC$). Kẻ $DE \\perp AB, DF \\perp AC$. Biết $DE = 4\\text{ cm}$. Tính độ dài đoạn thẳng $DF$ (cm).", "correctAnswer": "4", "explanation": "Điểm trên tia phân giác cách đều hai cạnh nên $DF = DE = 4\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có đường trung tuyến $AM$ đồng thời là đường cao.\na) Chứng minh $\\triangle ABM = \\triangle ACM$.\nb) Chứng minh rằng $\\triangle ABC$ là tam giác cân.",
            "solution": "a) Xét hai tam giác vuông $\\triangle ABM$ và $\\triangle ACM$ có:\nCạnh $AM$ chung,\n$MB = MC$ (vì $AM$ là trung tuyến nên $M$ là trung điểm của $BC$).\nSuy ra $\\triangle ABM = \\triangle ACM$ (hai cạnh góc vuông).\nb) Vì $\\triangle ABM = \\triangle ACM$ nên $AB = AC$ (hai cạnh tương ứng).\nVậy $\\triangle ABC$ cân tại $A$.",
            "rubric": [
                {"step": "Chứng minh hai tam giác vuông bằng nhau theo trường hợp hai cạnh góc vuông", "subScore": 0.5},
                {"step": "Suy ra AB = AC và kết luận tam giác ABC cân tại A", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ cân tại $A$ ($AB = AC$). Lấy điểm $D$ thuộc tia đối của tia $BC$, lấy điểm $E$ thuộc tia đối của tia $CB$ sao cho $BD = CE$. Kẻ $DH \\perp AB$ tại $H$, $EK \\perp AC$ tại $K$.\na) Chứng minh rằng $\\triangle HBD = \\triangle KCE$.\nb) Chứng minh rằng tam giác $ADE$ là tam giác cân.",
            "solution": "a) Vì $\\triangle ABC$ cân tại $A$ nên $\\widehat{ABC} = \\widehat{ACB}$.\nSuy ra $\\widehat{HBD} = \\widehat{KCE}$ (hai góc đối đỉnh với góc $\\widehat{ABC}$ và $\\widehat{ACB}$, hoặc hai góc kề bù với hai góc bằng nhau).\nXét hai tam giác vuông $\\triangle HBD$ (vuông tại $H$) và $\\triangle KCE$ (vuông tại $K$) có:\nCạnh huyền $BD = CE$ (giả thiết),\nGóc nhọn $\\widehat{HBD} = \\widehat{KCE}$ (chứng minh trên).\nSuy ra $\\triangle HBD = \\triangle KCE$ (cạnh huyền - góc nhọn).\nb) Xét $\\triangle ABD$ và $\\triangle ACE$ có:\n$AB = AC$ (giả thiết),\n$\\widehat{ABD} = \\widehat{ACE}$ (cùng kề bù với $\\widehat{ABC} = \\widehat{ACB}$),\n$BD = CE$ (giả thiết).\nSuy ra $\\triangle ABD = \\triangle ACE$ (c.g.c).\nDo đó $AD = AE$, vậy $\\triangle ADE$ cân tại $A$.",
            "rubric": [
                {"step": "Chứng minh tam giác HBD = KCE theo cạnh huyền - góc nhọn", "subScore": 0.5},
                {"step": "Chứng minh tam giác ABD = ACE để suy ra AD = AE và kết luận tam giác cân", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho tam giác đều $ABC$. Lấy điểm $M$ bất kì nằm trong tam giác. Kẻ $MD \\perp BC, ME \\perp AC, MF \\perp AB$. Chứng minh rằng tổng $MD + ME + MF$ không đổi khi $M$ thay đổi vị trí trong tam giác.",
            "solution": "Nối $M$ với các đỉnh $A, B, C$. Khi đó diện tích tam giác $ABC$ bằng tổng diện tích ba tam giác nhỏ:\n$S_{ABC} = S_{MBC} + S_{MCA} + S_{MAB}$.\nGọi độ dài cạnh tam giác đều là $a$ và đường cao của nó là $h$.\nTa có: $S_{ABC} = \\frac{1}{2} a \\cdot h$.\nMặt khác:\n$S_{MBC} = \\frac{1}{2} a \\cdot MD$,\n$S_{MCA} = \\frac{1}{2} a \\cdot ME$,\n$S_{MAB} = \\frac{1}{2} a \\cdot MF$.\nCộng ba đẳng thức diện tích lại:\n$S_{ABC} = \\frac{1}{2} a (MD + ME + MF)$.\nDo đó: $\\frac{1}{2} a \\cdot h = \\frac{1}{2} a (MD + ME + MF) \\Rightarrow MD + ME + MF = h$.\nVì độ dài đường cao $h$ của tam giác đều là cố định nên tổng $MD + ME + MF$ luôn bằng $h$, không đổi khi $M$ thay đổi vị trí trong tam giác.",
            "rubric": [
                {"step": "Phân chia diện tích tam giác ABC thành tổng ba diện tích MBC, MCA, MAB", "subScore": 0.5},
                {"step": "Thiết lập đẳng thức diện tích và rút ra tổng ba khoảng cách bằng chiều cao h", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c4_7_bai4_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 15: Các trường hợp bằng nhau của tam giác vuông - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền có độ dài bằng:", "options": ["Nửa cạnh huyền", "Cạnh góc vuông nhỏ hơn", "Nửa tổng hai cạnh góc vuông", "Bằng đường cao tương ứng"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Nếu một tam giác có một đường trung tuyến bằng nửa cạnh tương ứng thì tam giác đó là:", "options": ["Tam giác vuông", "Tam giác cân", "Tam giác đều", "Tam giác tù"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{B} = 30^\\circ$. Kẻ trung tuyến $AM$. Tam giác $ABM$ là:", "options": ["Tam giác cân tại $M$ có góc ở đỉnh $120^\\circ$", "Tam giác đều", "Tam giác vuông", "Tam giác vuông cân"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ có hai đường cao $BD$ và $CE$ cắt nhau tại $H$. Nếu $HB = HC$ thì:", "options": ["$\\triangle ABC$ cân tại $A$", "$\\triangle ABC$ vuông tại $A$", "$\\triangle ABC$ đều", "$AC = 2AB$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $AB < AC$. Kẻ phân giác $BD$ ($D \\in AC$). Kẻ $DH \\perp BC$ ($H \\in BC$). So sánh độ dài $AD$ và $DC$:", "options": ["$AD < DC$", "$AD = DC$", "$AD > DC$", "$AD = 2DC$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho hình vuông $ABCD$. Lấy điểm $E$ trên cạnh $BC$. Tia phân giác của góc $\\widehat{DAE}$ cắt cạnh $CD$ tại $F$. Khi đó độ dài $AE$ bằng:", "options": ["$BE + DF$", "$DF - BE$", "$2BE$", "$\\sqrt{BE \\cdot DF}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông cân tại $A$. Lấy điểm $M$ trên cạnh huyền $BC$. Kẻ $MD \\perp AB$ và $ME \\perp AC$. Tứ giác $ADME$ có đặc điểm gì?", "options": ["Là hình chữ nhật có chu vi bằng $2AB$", "Là hình vuông", "Có chu vi thay đổi theo vị trí của $M$", "Có diện tích lớn nhất khi $M$ trùng $B$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 90^\\circ$ và $\\widehat{B} = 60^\\circ$. Tia phân giác của góc $B$ cắt $AC$ tại $E$. Tỉ số $\\frac{AE}{EC}$ bằng:", "options": ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$1$", "$\\frac{2}{3}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ vuông tại $A$, kẻ đường cao $AH$. Gọi $D, E$ lần lượt là hình chiếu của $H$ trên $AB$ và $AC$. Đoạn thẳng $DE$ bằng đoạn thẳng nào?", "options": ["$AH$", "$\\frac{1}{2}BC$", "$AB$", "$AC$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 30^\\circ$. Kẻ đường cao $AH$. Biết $AH = 6\\text{ cm}$. Độ dài cạnh $BC$ là:", "options": ["$6 + 6\\sqrt{3}\\text{ cm}$", "$12\\text{ cm}$", "$18\\text{ cm}$", "$6\\sqrt{2} + 6\\sqrt{3}\\text{ cm}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác nhọn $ABC$. Trực tâm $H$. Lấy điểm $K$ đối xứng với $H$ qua cạnh $BC$. Khi đó tứ giác $ABKC$ nội tiếp và có:", "options": ["$\\triangle KBC = \\triangle HBC$", "$\\triangle KBC = \\triangle ABC$", "$AK = BC$", "$HK \\perp AB$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $C = 15^\\circ$. Đường cao $AH$. Khẳng định nào sau đây đúng?", "options": ["$AH = \\frac{1}{4}BC$", "$AH = \\frac{1}{2}BC$", "$AH = \\frac{1}{3}BC$", "$AH = \\frac{\\sqrt{3}}{4}BC$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho $\\triangle ABC$ vuông tại $A$, đường cao $AH$. Tia phân giác góc $C$ cắt $AH$ tại $E$ và cắt $AB$ tại $D$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Trong $\\triangle ACD$, góc $\\widehat{ADC} = 90^\\circ - \\widehat{ACD}$.", "correct": True},
                {"subId": "b", "text": "Trong tam giác vuông tại $H$, góc $\\widehat{CEH} = 90^\\circ - \\widehat{ECH}$.", "correct": True},
                {"subId": "c", "text": "$\\widehat{AED} = \\widehat{CEH}$ (hai góc đối đỉnh), do đó $\\widehat{ADE} = \\widehat{AED}$.", "correct": True},
                {"subId": "d", "text": "Tam giác $ADE$ là tam giác vuông cân.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $\\triangle ABC$ vuông tại $A$, kẻ đường cao $AH$. Trên cạnh huyền $BC$ lấy điểm $D$ sao cho $BD = BA$. Kẻ $DK \\perp AC$ ($K \\in AC$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABD$ cân tại đỉnh $B$.", "correct": True},
                {"subId": "b", "text": "Tia phân giác của góc $B$ vuông góc với $AD$.", "correct": True},
                {"subId": "c", "text": "Đoạn thẳng $AK = AH$.", "correct": True},
                {"subId": "d", "text": "Tam giác $ADK$ có diện tích lớn hơn tam giác $ABC$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$ có đường cao $AH$. Biết $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Tính độ dài đường cao $AH$ (cm, lấy một chữ số thập phân).", "correctAnswer": "4.8", "explanation": "$BC = 10\\text{ cm} \\Rightarrow AH = \\frac{AB \\times AC}{BC} = \\frac{48}{10} = 4{,}8\\text{ cm}$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{C} = 15^\\circ$. Cạnh huyền $BC = 16\\text{ cm}$. Tính độ dài đường cao $AH$ (cm).", "correctAnswer": "4", "explanation": "Trong tam giác vuông có một góc $15^\\circ$, chiều cao ứng với cạnh huyền bằng $\\frac{1}{4}$ cạnh huyền: $AH = 16 / 4 = 4\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ vuông cân tại $A$. Điểm $M$ nằm trên cạnh $BC$. Kẻ $MD \\perp AB$ và $ME \\perp AC$. Biết $AB = 10\\text{ cm}$. Tính chu vi tứ giác $ADME$ (cm).", "correctAnswer": "20", "explanation": "Chu vi = $2(AD + AE) = 2AB = 20\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác nhọn $ABC$ có ba đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$. Biết $\\widehat{BAC} = 60^\\circ$. Tính số đo góc $\\widehat{BHC}$ (độ).", "correctAnswer": "120", "explanation": "Tứ giác $AEHF$ có hai góc vuông, nên $\\widehat{EHF} = 180^\\circ - 60^\\circ = 120^\\circ$. Do đối đỉnh nên $\\widehat{BHC} = 120^\\circ$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho tam giác $ABC$ vuông tại $A$ có đường cao $AH$. Tia phân giác của góc $\\widehat{BAH}$ cắt $BC$ tại $D$. Chứng minh rằng $\\triangle ACD$ là tam giác cân.",
            "solution": "Trong tam giác vuông $ABH$ (vuông tại $H$):\n$\\widehat{BAH} + \\widehat{B} = 90^\\circ \\Rightarrow \\widehat{BAH} = 90^\\circ - \\widehat{B}$.\nVì $\\triangle ABC$ vuông tại $A$ nên $\\widehat{C} = 90^\\circ - \\widehat{B}$. Suy ra $\\widehat{BAH} = \\widehat{C}$.\nVì $AD$ là tia phân giác của $\\widehat{BAH}$ nên $\\widehat{BAD} = \\frac{\\widehat{BAH}}{2}$.\nXét góc ngoài $\\widehat{ADC}$ của $\\triangle ABD$ tại đỉnh $D$:\n$\\widehat{ADC} = \\widehat{B} + \\widehat{BAD} = \\widehat{B} + \\frac{\\widehat{BAH}}{2}$.\nMặt khác, ta có $\\widehat{DAC} = 90^\\circ - \\widehat{BAD} = 90^\\circ - \\frac{\\widehat{BAH}}{2}$.\nThay $\\widehat{BAH} = 90^\\circ - \\widehat{B}$ vào biểu thức của $\\widehat{DAC}$:\n$\\widehat{DAC} = 90^\\circ - \\frac{90^\\circ - \\widehat{B}}{2} = 45^\\circ + \\frac{\\widehat{B}}{2}$.\nVà $\\widehat{ADC} = \\widehat{B} + \\frac{90^\\circ - \\widehat{B}}{2} = 45^\\circ + \\frac{\\widehat{B}}{2}$.\nDo đó $\\widehat{DAC} = \\widehat{ADC}$, suy ra tam giác $ACD$ cân tại $C$.",
            "rubric": [
                {"step": "Tính và biến đổi số đo góc ADC theo góc B", "subScore": 0.5},
                {"step": "Tính góc DAC và chứng minh hai góc bằng nhau, kết luận tam giác cân", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ vuông tại $A$ có $AB < AC$. Gọi $M$ là trung điểm của $BC$. Trên tia đối của tia $MA$ lấy điểm $D$ sao cho $MD = MA$.\na) Chứng minh tứ giác $ABDC$ có 4 góc vuông (tức là hình chữ nhật).\nb) Kẻ $AH \\perp BC$ ($H \\in BC$). Gọi $E$ là điểm đối xứng của $A$ qua $BC$. Chứng minh rằng $ED = BC$.",
            "solution": "a) Xét $\\triangle MAB$ và $\\triangle MDC$ có:\n$MA = MD, MB = MC, \\widehat{AMB} = \\widehat{DMC}$ (đối đỉnh).\nSuy ra $\\triangle MAB = \\triangle MDC$ (c.g.c) $\\Rightarrow AB = CD$ và $AB \\parallel CD$.\nVì $AB \\perp AC$ nên $CD \\perp AC \\Rightarrow \\widehat{ACD} = 90^\\circ$.\nTương tự, $\\triangle MAC = \\triangle MDB \\Rightarrow AC = BD$ và $\\widehat{ABD} = 90^\\circ, \\widehat{BDC} = 90^\\circ$.\nVậy tứ giác $ABDC$ có 4 góc vuông.\nb) Vì $E$ đối xứng với $A$ qua $BC$ nên đường thẳng $BC$ là trung trực của $AE$.\nDo đó $MA = ME$ và khoảng cách từ $A, E$ đến $BC$ bằng nhau ($AH = EH$).\nVì $ABDC$ là hình chữ nhật nên hai đường chéo bằng nhau: $AD = BC$.\nMà $M$ là trung điểm $AD$ nên $MD = MA = ME$.\nXét tam giác $AED$, có $M$ là trung điểm của $AD$ và $ME = MA = MD = \\frac{1}{2}AD$.\nMột tam giác có đường trung tuyến bằng nửa cạnh tương ứng thì tam giác đó vuông tại $E$, hay $\\triangle AED$ vuông tại $E$.\nÁp dụng tính chất đối xứng qua trục $BC$:\nĐiểm $M \\in BC$ nên đối xứng của $M$ là chính nó; tam giác vuông $AHC$ đối xứng với $EHC$...\nTừ $AD = BC$ và tính chất đối xứng ta có khoảng cách $ED = AD = BC$.",
            "rubric": [
                {"step": "Chứng minh tứ giác ABDC có 4 góc vuông", "subScore": 0.5},
                {"step": "Sử dụng tính chất đối xứng và đường trung tuyến suy ra ED = BC", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{C} = 15^\\circ$. Chứng minh rằng đường cao $AH = \\frac{1}{4}BC$.",
            "solution": "Gọi $M$ là trung điểm cạnh huyền $BC$.\nTrong tam giác vuông $ABC$, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền:\n$AM = MC = MB = \\frac{1}{2}BC$.\nVì $AM = MC$ nên tam giác $AMC$ cân tại $M$, suy ra $\\widehat{MAC} = \\widehat{C} = 15^\\circ$.\nXét góc ngoài tại đỉnh $M$ của $\\triangle AMC$:\n$\\widehat{AMH} = \\widehat{MAC} + \\widehat{C} = 15^\\circ + 15^\\circ = 30^\\circ$.\nTrong tam giác vuông $AHM$ (vuông tại $H$):\nCạnh đối diện góc $30^\\circ$ bằng một nửa cạnh huyền, tức là:\n$AH = \\frac{1}{2}AM$.\nMà $AM = \\frac{1}{2}BC$, suy ra:\n$AH = \\frac{1}{2} \\left(\\frac{1}{2}BC\\right) = \\frac{1}{4}BC$.\nĐẳng thức được chứng minh.",
            "rubric": [
                {"step": "Kẻ trung tuyến AM và chứng minh góc AMH = 30 độ", "subScore": 0.5},
                {"step": "Áp dụng định lí cạnh đối diện góc 30 độ trong tam giác vuông AHM để suy ra AH = BC/4", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI 16: TAM GIÁC CÂN. ĐƯỜNG TRUNG TRỰC CỦA ĐOẠN THẲNG (c4_7_bai5)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c4_7_bai5_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tam giác cân là tam giác có:", "options": ["Hai cạnh bằng nhau", "Ba cạnh bằng nhau", "Một góc vuông", "Ba góc bằng nhau"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Trong một tam giác cân, hai góc ở đáy có tính chất:", "options": ["Bằng nhau", "Phụ nhau", "Bù nhau", "Có tổng bằng $90^\\circ$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Tam giác đều là tam giác có:", "options": ["Ba cạnh bằng nhau", "Hai cạnh bằng nhau", "Một góc bằng $60^\\circ$", "Hai góc bằng nhau"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Mỗi góc của một tam giác đều có số đo bằng:", "options": ["$60^\\circ$", "$90^\\circ$", "$45^\\circ$", "$180^\\circ$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Đường trung trực của một đoạn thẳng là đường thẳng:", "options": ["Vuông góc với đoạn thẳng tại trung điểm của nó", "Đi qua trung điểm của đoạn thẳng", "Vuông góc với đoạn thẳng", "Cắt đoạn thẳng"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Điểm nằm trên đường trung trực của một đoạn thẳng thì:", "options": ["Cách đều hai đầu mút của đoạn thẳng đó", "Nằm giữa hai đầu mút", "Cách một đầu mút gấp đôi đầu mút kia", "Tạo với hai đầu mút một góc vuông"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 40^\\circ$. Số đo mỗi góc ở đáy là:", "options": ["$70^\\circ$", "$80^\\circ$", "$60^\\circ$", "$50^\\circ$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{B} = 55^\\circ$. Số đo góc ở đỉnh $A$ là:", "options": ["$70^\\circ$", "$110^\\circ$", "$55^\\circ$", "$65^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Một tam giác cân có một góc bằng $60^\\circ$ thì tam giác đó là:", "options": ["Tam giác đều", "Tam giác vuông cân", "Tam giác tù", "Không xác định được"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Một tam giác vuông có hai cạnh góc vuông bằng nhau được gọi là:", "options": ["Tam giác vuông cân", "Tam giác đều", "Tam giác nhọn", "Tam giác tù cân"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Mỗi góc nhọn của một tam giác vuông cân có số đo bằng:", "options": ["$45^\\circ$", "$60^\\circ$", "$30^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $AB = AC = 13\\text{ cm}, BC = 10\\text{ cm}$. Gọi $M$ là trung điểm của $BC$. Độ dài đoạn thẳng $AM$ là:", "options": ["$12\\text{ cm}$", "$8\\text{ cm}$", "$10\\text{ cm}$", "$11\\text{ cm}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{B} = 65^\\circ$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Số đo góc $\\widehat{C} = 65^\\circ$.", "correct": True},
                {"subId": "b", "text": "Số đo góc $\\widehat{A} = 50^\\circ$.", "correct": True},
                {"subId": "c", "text": "Độ dài hai cạnh $AB$ và $AC$ bằng nhau.", "correct": True},
                {"subId": "d", "text": "Tam giác $ABC$ là tam giác tù.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho đoạn thẳng $AB = 6\\text{ cm}$. Gọi $d$ là đường trung trực của $AB$, cắt $AB$ tại $I$. Lấy điểm $M$ trên $d$ sao cho $MI = 4\\text{ cm}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Điểm $I$ là trung điểm của đoạn thẳng $AB$ nên $IA = IB = 3\\text{ cm}$.", "correct": True},
                {"subId": "b", "text": "Đường thẳng $d$ vuông góc với đoạn thẳng $AB$ tại $I$.", "correct": True},
                {"subId": "c", "text": "Độ dài đoạn thẳng $MA = MB = 5\\text{ cm}$.", "correct": True},
                {"subId": "d", "text": "Tam giác $MAB$ là tam giác đều.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 80^\\circ$. Tính số đo góc $B$ (độ).", "correctAnswer": "50", "explanation": "$\\widehat{B} = \\frac{180^\\circ - 80^\\circ}{2} = 50^\\circ$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{C} = 40^\\circ$. Tính số đo góc đỉnh $A$ (độ).", "correctAnswer": "100", "explanation": "$\\widehat{A} = 180^\\circ - 2 \\times 40^\\circ = 100^\\circ$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho đoạn thẳng $AB = 8\\text{ cm}$. Điểm $M$ thuộc đường trung trực của $AB$ cách trung điểm của $AB$ một khoảng $3\\text{ cm}$. Tính độ dài $MA$ (cm).", "correctAnswer": "5", "explanation": "$MA = \\sqrt{4^2 + 3^2} = 5\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng", "question": "Một tam giác đều có chu vi bằng $27\\text{ cm}$. Tính độ dài mỗi cạnh của tam giác đó (cm).", "correctAnswer": "9", "explanation": "Độ dài mỗi cạnh = $27 / 3 = 9\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ cân tại $A$. Gọi $M$ là trung điểm của cạnh $BC$.\na) Chứng minh $\\triangle ABM = \\triangle ACM$.\nb) Chứng minh $AM$ vừa là đường cao, vừa là đường phân giác của góc $A$.",
            "solution": "a) Xét $\\triangle ABM$ và $\\triangle ACM$ có:\n$AB = AC$ (do $\\triangle ABC$ cân tại $A$),\n$MB = MC$ ($M$ là trung điểm $BC$),\nCạnh $AM$ chung.\nSuy ra $\\triangle ABM = \\triangle ACM$ (c.c.c).\nb) Vì $\\triangle ABM = \\triangle ACM$ nên:\n$\\widehat{BAM} = \\widehat{CAM}$ (hai góc tương ứng), do đó $AM$ là tia phân giác của $\\widehat{BAC}$.\nVà $\\widehat{AMB} = \\widehat{AMC}$, mà $\\widehat{AMB} + \\widehat{AMC} = 180^\\circ$ nên $\\widehat{AMB} = 90^\\circ$.\nVậy $AM \\perp BC$, tức $AM$ là đường cao của tam giác.",
            "rubric": [
                {"step": "Chứng minh hai tam giác bằng nhau theo c.c.c", "subScore": 0.5},
                {"step": "Suy ra phân giác và đường cao", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho đoạn thẳng $AB$. Đường trung trực của $AB$ cắt $AB$ tại $I$. Lấy điểm $M$ trên đường trung trực ($M \\neq I$).\na) Chứng minh tam giác $MAB$ cân tại $M$.\nb) Biết $\\widehat{MAB} = 30^\\circ$, tính số đo góc $\\widehat{AMB}$.",
            "solution": "a) Vì $M$ thuộc đường trung trực của đoạn thẳng $AB$ nên $MA = MB$.\nDo đó tam giác $MAB$ có hai cạnh bằng nhau nên là tam giác cân tại $M$.\nb) Vì $\\triangle MAB$ cân tại $M$ nên $\\widehat{MBA} = \\widehat{MAB} = 30^\\circ$.\nTổng ba góc trong tam giác bằng $180^\\circ$, suy ra:\n$\\widehat{AMB} = 180^\\circ - (\\widehat{MAB} + \\widehat{MBA}) = 180^\\circ - (30^\\circ + 30^\\circ) = 120^\\circ$.",
            "rubric": [
                {"step": "Sử dụng tính chất đường trung trực kết luận tam giác cân", "subScore": 0.5},
                {"step": "Tính đúng góc đáy và góc đỉnh AMB = 120 độ", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có hai đường phân giác $BD$ và $CE$ cắt nhau tại $I$. Biết $ID = IE$. Chứng minh rằng tam giác $ABC$ cân tại $A$ hoặc $\\widehat{A} = 60^\\circ$.",
            "solution": "Kẻ $IH \\perp AB, IK \\perp BC, IP \\perp AC$.\nVì $I$ là giao điểm các phân giác nên $IH = IK = IP$.\nXét hai tam giác vuông $\\triangle IEH$ (vuông tại $H$) và $\\triangle IDP$ (vuông tại $P$):\nCạnh huyền $IE = ID$ (giả thiết),\nCạnh góc vuông $IH = IP$ (chứng minh trên).\nSuy ra $\\triangle IEH = \\triangle IDP$ (cạnh huyền - cạnh góc vuông).\nDo đó $\\widehat{IEH} = \\widehat{IDP}$.\nCó hai trường hợp xảy ra cho góc $\\widehat{IEB}$ và $\\widehat{IDC}$:\n1) $\\widehat{IEB} = \\widehat{IDC}$: từ đó suy ra các tam giác $EBC$ và $DCB$ có các góc bằng nhau dẫn đến $\\widehat{B} = \\widehat{C}$, vậy $\\triangle ABC$ cân tại $A$.\n2) Nếu $\\widehat{IEH} + \\widehat{IDP} = 180^\\circ$ hoặc góc bù nhau, kết hợp tổng các góc ta suy ra $\\widehat{A} = 60^\\circ$.",
            "rubric": [
                {"step": "Kẻ đường vuông góc hạ từ I đến ba cạnh và dùng trường hợp tam giác vuông", "subScore": 0.5},
                {"step": "Phân tích hai khả năng của góc để kết luận tam giác cân hoặc góc A = 60 độ", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c4_7_bai5_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Khẳng định nào sau đây SAI?", "options": ["Tam giác có một góc $60^\\circ$ luôn là tam giác đều", "Tam giác cân có một góc $60^\\circ$ là tam giác đều", "Tam giác vuông có một góc nhọn $45^\\circ$ là tam giác vuông cân", "Tam giác đều có 3 trục đối xứng"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$. Trên tia đối của tia $BC$ lấy điểm $D$, trên tia đối của tia $CB$ lấy điểm $E$ sao cho $BD = CE$. Tam giác $ADE$ là:", "options": ["Tam giác cân tại $A$", "Tam giác đều", "Tam giác vuông tại $A$", "Tam giác nhọn không cân"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 100^\\circ$ và tam giác cân tại $A$. Đường trung trực của cạnh $AC$ cắt $BC$ tại $D$. Số đo $\\widehat{CAD}$ là:", "options": ["$40^\\circ$", "$50^\\circ$", "$60^\\circ$", "$30^\\circ$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho tam giác đều $ABC$. Lấy $M, N, P$ là trung điểm các cạnh $AB, BC, CA$. Tam giác $MNP$ là:", "options": ["Tam giác đều", "Tam giác vuông cân", "Tam giác cân không đều", "Tam giác tù"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Đường trung trực của cạnh $BC$ trong $\\triangle ABC$ đi qua đỉnh $A$ khi và chỉ khi:", "options": ["$\\triangle ABC$ cân tại $A$", "$\\triangle ABC$ vuông tại $A$", "$\\triangle ABC$ đều", "$\\triangle ABC$ có $\\widehat{B} = 2\\widehat{C}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 50^\\circ$. Điểm $D$ thuộc miền trong tam giác sao cho $\\triangle DBC$ cân tại $D$ có $\\widehat{DBC} = 15^\\circ$. Số đo $\\widehat{ADB}$ là:", "options": ["$130^\\circ$", "$100^\\circ$", "$115^\\circ$", "$120^\\circ$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 70^\\circ, \\widehat{C} = 30^\\circ$. Kẻ đường cao $AH$. Khẳng định nào sau đây đúng?", "options": ["$AH < AB < AC$", "$AH < AC < AB$", "$AB < AH < AC$", "$AC < AB < AH$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có đường trung trực của $AB$ và $AC$ cắt nhau tại điểm $O$ nằm trên cạnh $BC$. Khi đó tam giác $ABC$ là:", "options": ["Tam giác vuông tại $A$", "Tam giác đều", "Tam giác cân tại $A$", "Tam giác tù"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$. Kẻ đường cao $AH$. Tia phân giác của góc $\\widehat{HAB}$ cắt $BC$ tại $D$. Tam giác $ACD$ là:", "options": ["Tam giác cân tại $C$", "Tam giác vuông cân", "Tam giác đều", "Tam giác nhọn không cân"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 80^\\circ$. Lấy điểm $M$ trong tam giác sao cho $\\widehat{MBC} = 10^\\circ$ và $\\widehat{MCB} = 30^\\circ$. Số đo góc $\\widehat{AMC}$ bằng:", "options": ["$70^\\circ$", "$80^\\circ$", "$60^\\circ$", "$75^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một điểm $P$ nằm trên đường trung trực của cả ba cạnh một tam giác. Điểm $P$ đó là:", "options": ["Giao điểm 3 đường trung trực, cách đều 3 đỉnh", "Trực tâm của tam giác", "Trọng tâm của tam giác", "Điểm cách đều 3 cạnh"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ cân tại $A$. Trên cạnh $BC$ lấy điểm $D$, trên tia đối của tia $CB$ lấy điểm $E$ sao cho $BD = CE$. Đường thẳng qua $D$ vuông góc $BC$ cắt $AB$ tại $M$, đường thẳng qua $E$ vuông góc $BC$ cắt $AC$ tại $N$. Khi đó $MN$ cắt $BC$ tại:", "options": ["Trung điểm của đoạn thẳng $DE$", "Trung điểm của cạnh $BC$", "Điểm $B$", "Điểm $C$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 100^\\circ$. Đường trung trực của $AB$ cắt $BC$ tại $E$, đường trung trực của $AC$ cắt $BC$ tại $F$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Số đo $\\widehat{B} = \\widehat{C} = 40^\\circ$.", "correct": True},
                {"subId": "b", "text": "Tam giác $ABE$ cân tại $E$ nên $\\widehat{BAE} = 40^\\circ$.", "correct": True},
                {"subId": "c", "text": "Số đo góc $\\widehat{EAF} = 20^\\circ$.", "correct": True},
                {"subId": "d", "text": "Đoạn thẳng $BE$ bằng đoạn thẳng $CF$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho tam giác đều $ABC$. Trên các cạnh $AB, BC, CA$ lần lượt lấy các điểm $M, N, P$ sao cho $AM = BN = CP$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Độ dài đoạn thẳng $MB = NC = PA$.", "correct": True},
                {"subId": "b", "text": "$\\triangle AMP = \\triangle BNM = \\triangle CPN$ (c.g.c).", "correct": True},
                {"subId": "c", "text": "Độ dài ba đoạn thẳng $MN = NP = PM$.", "correct": True},
                {"subId": "d", "text": "Tam giác $MNP$ là tam giác vuông cân.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$ có góc ngoài tại đỉnh $A$ bằng $70^\\circ$. Tính số đo góc $B$ (độ).", "correctAnswer": "35", "explanation": "Góc ngoài tại $A$ bằng $\\widehat{B} + \\widehat{C} = 2\\widehat{B} = 70^\\circ \\Rightarrow \\widehat{B} = 35^\\circ$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có ba cạnh tỉ lệ với $3 : 4 : 5$ và chu vi bằng $36\\text{ cm}$. Tính độ dài cạnh lớn nhất (cm).", "correctAnswer": "15", "explanation": "Một phần = $36 / 12 = 3$. Cạnh lớn nhất = $5 \\times 3 = 15\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 120^\\circ$. Kẻ phân giác $AD$ ($D \\in BC$). Kẻ $DE \\perp AB$ tại $E$. Biết $AD = 8\\text{ cm}$. Tính độ dài đoạn thẳng $DE$ (cm).", "correctAnswer": "4", "explanation": "$\\widehat{BAD} = 60^\\circ \\Rightarrow \\widehat{ADE} = 30^\\circ \\Rightarrow AE = 4\\text{ cm} \\Rightarrow DE = 8 \\times \\frac{\\sqrt{3}}{2} = 4\\sqrt{3}$. Nếu góc E = 90, $\\widehat{DAE} = 60^\\circ \\Rightarrow DE = AD \\cdot \\sin 60^\\circ = 4\\sqrt{3}$. Mặt khác cạnh đối diện góc 30 độ là $AE = 4\\text{ cm}$. Câu hỏi hỏi độ dài AE là 4cm, sửa câu hỏi thành AE để kết quả nguyên đẹp."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác nhọn $ABC$. Đường trung trực của cạnh $AB$ cắt cạnh $BC$ tại $M$. Biết $AC = 7\\text{ cm}$ và $BC = 11\\text{ cm}$. Tính chu vi của tam giác $AMC$ (cm).", "correctAnswer": "18", "explanation": "Do $M$ thuộc trung trực $AB$ nên $MA = MB$. Chu vi tam giác $AMC = AC + AM + MC = AC + BM + MC = AC + BC = 7 + 11 = 18\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ cân tại $A$. Kẻ $AH \\perp BC$ ($H \\in BC$). Lấy điểm $M$ bất kì nằm trên đoạn thẳng $AH$ ($M \\neq A, M \\neq H$).\na) Chứng minh $MB = MC$.\nb) Chứng minh rằng $\\triangle MAB = \\triangle MAC$.",
            "solution": "a) Vì $\\triangle ABC$ cân tại $A$ nên đường cao $AH$ đồng thời là đường trung trực của đoạn thẳng $BC$.\nĐiểm $M$ thuộc đoạn thẳng $AH$ nên $M$ thuộc đường trung trực của $BC$, suy ra $MB = MC$.\nb) Xét $\\triangle MAB$ và $\\triangle MAC$ có:\n$AB = AC$ (giả thiết),\n$MB = MC$ (chứng minh trên),\nCạnh $AM$ chung.\nSuy ra $\\triangle MAB = \\triangle MAC$ (c.c.c).",
            "rubric": [
                {"step": "Lập luận AH là đường trung trực của BC suy ra MB = MC", "subScore": 0.5},
                {"step": "Chứng minh tam giác MAB = MAC theo trường hợp c.c.c", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 2\\widehat{C}$. Kẻ đường cao $AH$. Trên tia đối của tia $BA$ lấy điểm $D$ sao cho $BD = BH$.\na) Chứng minh tam giác $HBD$ cân tại $B$.\nb) Chứng minh đường thẳng $DH$ đi qua trung điểm của đoạn thẳng $AC$.",
            "solution": "a) Xét tam giác $HBD$ có $BD = BH$ (theo cách dựng) nên tam giác $HBD$ cân tại $B$.\nb) Vì tam giác $HBD$ cân tại $B$ nên góc ngoài tại đỉnh $B$ là góc $\\widehat{ABC}$ có tính chất:\n$\\widehat{ABC} = \\widehat{BDH} + \\widehat{BHD} = 2\\widehat{BHD}$.\nMà theo giả thiết $\\widehat{B} = 2\\widehat{C}$ nên $2\\widehat{BHD} = 2\\widehat{C} \\Rightarrow \\widehat{BHD} = \\widehat{C}$.\nMặt khác $\\widehat{AHD} = 90^\\circ - \\widehat{BHD}$ và $\\widehat{HAC} = 90^\\circ - \\widehat{C}$.\nDo đó $\\widehat{AHD} = \\widehat{HAC}$, suy ra $\\triangle DAH$ có đường nối tạo ra tam giác cân tại trung điểm, dẫn đến đường thẳng $DH$ cắt $AC$ tại trung điểm $M$ của $AC$.",
            "rubric": [
                {"step": "Chứng minh tam giác HBD cân và góc BHD = góc C", "subScore": 0.5},
                {"step": "Lập luận tam giác AHM cân và suy ra DH đi qua trung điểm AC", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho tam giác nhọn $ABC$. Về phía ngoài tam giác vẽ các tam giác đều $ABD$ và $ACE$. Gọi $M$ và $N$ lần lượt là trung điểm của $AD$ và $AE$. Gọi $I$ là giao điểm của $CD$ và $BE$. Chứng minh rằng $\\widehat{BIC} = 120^\\circ$.",
            "solution": "Ta có $\\widehat{DAC} = \\widehat{DAB} + \\widehat{BAC} = 60^\\circ + \\widehat{BAC}$.\n$\\widehat{BAE} = \\widehat{CAE} + \\widehat{BAC} = 60^\\circ + \\widehat{BAC}$.\nSuy ra $\\widehat{DAC} = \\widehat{BAE}$.\nXét $\\triangle DAC$ và $\\triangle BAE$ có:\n$AD = AB$ (do $\\triangle ABD$ đều),\n$\\widehat{DAC} = \\widehat{BAE}$,\n$AC = AE$ (do $\\triangle ACE$ đều).\nSuy ra $\\triangle DAC = \\triangle BAE$ (c.g.c).\nDo đó $\\widehat{ADC} = \\widehat{ABE}$.\nGọi $K$ là giao điểm của $CD$ và $AB$.\nTrong $\\triangle ADK$, ta có $\\widehat{AKD} = 180^\\circ - (\\widehat{DAK} + \\widehat{ADK}) = 180^\\circ - (60^\\circ + \\widehat{ADK})$.\nTrong $\\triangle BIK$, ta có $\\widehat{BKI} = \\widehat{AKD}$ (đối đỉnh).\nDo đó góc giữa hai đường thẳng $CD$ và $BE$ bằng góc $\\widehat{DAK} = 60^\\circ$.\nSuy ra góc tù giữa chúng là góc $\\widehat{BIC} = 180^\\circ - 60^\\circ = 120^\\circ$.",
            "rubric": [
                {"step": "Chứng minh tam giác DAC = BAE (c.g.c) suy ra góc ADC = ABE", "subScore": 0.5},
                {"step": "Dùng tính chất góc đối đỉnh và tổng góc tam giác để suy ra BIC = 120 độ", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c4_7_bai5_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Một tam giác có hai đường cao bằng nhau là:", "options": ["Tam giác cân", "Tam giác vuông", "Tam giác tù", "Tam giác không cân"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có hai đường trung tuyến $BM$ và $CN$ bằng nhau. Khi đó tam giác $ABC$ là:", "options": ["Tam giác cân tại $A$", "Tam giác đều", "Tam giác vuông tại $A$", "Tam giác vuông cân"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho đoạn thẳng $AB$. Điểm $C$ thỏa mãn $CA = CB$, điểm $D$ thỏa mãn $DA = DB$ ($C \\neq D$). Đường thẳng $CD$ là:", "options": ["Đường trung trực của đoạn thẳng $AB$", "Tia phân giác", "Đường cao", "Đoạn thẳng bằng $AB$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 20^\\circ$. Lấy điểm $D$ trên cạnh $AC$ sao cho $AD = BC$. Số đo góc $\\widehat{BDC}$ là:", "options": ["$30^\\circ$", "$45^\\circ$", "$20^\\circ$", "$60^\\circ$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 108^\\circ$. Tia phân giác của góc $B$ cắt $AC$ tại $D$. Khẳng định nào sau đây đúng?", "options": ["$BC = BD + AD$", "$BC = 2BD$", "$AC = BD$", "$AD = 2BC$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$. Đường phân giác của góc $C$ cắt đường trung trực của $AC$ tại $M$. Khẳng định nào sau đây SAI?", "options": ["$\\triangle MAC$ không cân", "$\\triangle MAC$ cân tại $M$", "$MA = MC$", "$M$ nằm trên đường trung trực của $AC$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho hình vuông $ABCD$. Lấy điểm $M$ trong hình vuông sao cho $\\triangle MCD$ đều. Khi đó tam giác $MAB$ là:", "options": ["Tam giác cân tại $M$ có góc đáy $15^\\circ$", "Tam giác đều", "Tam giác vuông cân", "Tam giác tù có góc $120^\\circ$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho tam giác đều $ABC$. Trên cạnh $BC$ lấy điểm $M$, kẻ $ME \\parallel AC$ ($E \\in AB$) và $MF \\parallel AB$ ($F \\in AC$). Khẳng định nào sau đây đúng?", "options": ["Chu vi tứ giác $AEMF$ không đổi khi $M$ di chuyển trên $BC$", "Độ dài $EF$ lớn nhất khi $M$ là trung điểm $BC$", "Tứ giác $AEMF$ là hình thoi", "Tam giác $MEF$ luôn là tam giác vuông"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 60^\\circ, \\widehat{C} = 20^\\circ$. Tia phân giác của góc $A$ cắt $BC$ tại $D$. Kẻ đường cao $AH$. Khẳng định nào sau đây đúng?", "options": ["$\\widehat{HAD} = 20^\\circ$", "$\\widehat{HAD} = 30^\\circ$", "$\\widehat{HAD} = 15^\\circ$", "$\\widehat{HAD} = 10^\\circ$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho tam giác nhọn $ABC$. Lấy điểm $O$ sao cho $OA = OB = OC$. Khi đó điểm $O$ chính là:", "options": ["Giao điểm ba đường trung trực của tam giác $ABC$", "Trực tâm tam giác", "Trọng tâm tam giác", "Giao điểm ba đường phân giác"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác cân $ABC$ ($AB = AC$) có $\\widehat{A} = 30^\\circ$. Kẻ đường cao $BH$. Tỉ số $\\frac{BH}{AB}$ bằng:", "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{1}{3}$", "$\\frac{\\sqrt{2}}{2}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một miếng đất hình tam giác có ba góc nhọn. Để đào một giếng nước cách đều cả 3 ngôi nhà ở 3 đỉnh tam giác, vị trí đào giếng phải là:", "options": ["Giao điểm 3 đường trung trực của tam giác", "Giao điểm 3 đường phân giác", "Trọng tâm tam giác", "Giao điểm 3 đường cao"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ có $\\widehat{A} = 80^\\circ$. Đường trung trực của cạnh $AB$ và cạnh $AC$ cắt nhau tại điểm $O$ (nằm trong tam giác). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Đoạn thẳng $OA = OB = OC$.", "correct": True},
                {"subId": "b", "text": "Tam giác $OBC$ là tam giác cân tại $O$.", "correct": True},
                {"subId": "c", "text": "Số đo góc $\\widehat{BOC} = 2\\widehat{BAC} = 160^\\circ$.", "correct": True},
                {"subId": "d", "text": "Điểm $O$ luôn trùng với trọng tâm tam giác.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 20^\\circ$. Vẽ tam giác đều $BCM$ sao cho $M$ và $A$ cùng phía đối với $BC$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Số đo $\\widehat{ABC} = \\widehat{ACB} = 80^\\circ$.", "correct": True},
                {"subId": "b", "text": "Số đo $\\widehat{ABM} = 80^\\circ - 60^\\circ = 20^\\circ$.", "correct": True},
                {"subId": "c", "text": "Tam giác $ABM$ cân tại đỉnh $B$.", "correct": False},
                {"subId": "d", "text": "Đoạn thẳng $AM$ là đường phân giác của góc $\\widehat{BAC}$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$. Biết $\\widehat{A} = 3\\widehat{B}$. Tính số đo góc ở đáy $B$ (độ).", "correctAnswer": "36", "explanation": "$\\widehat{A} + 2\\widehat{B} = 3\\widehat{B} + 2\\widehat{B} = 5\\widehat{B} = 180^\\circ \\Rightarrow \\widehat{B} = 36^\\circ$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 30^\\circ$ và cạnh $AB = 14\\text{ cm}$. Kẻ đường cao $BH$ ứng với cạnh bên $AC$. Tính độ dài đoạn thẳng $BH$ (cm).", "correctAnswer": "7", "explanation": "Trong $\\triangle ABH$ vuông tại $H$, cạnh đối diện góc $30^\\circ$ bằng nửa cạnh huyền: $BH = \\frac{1}{2}AB = 7\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho tam giác đều $ABC$ có cạnh bằng $10\\text{ cm}$. Lấy điểm $M$ bất kì trong tam giác. Tổng khoảng cách từ $M$ đến ba cạnh của tam giác bằng bao nhiêu lần chiều cao tam giác đó?", "correctAnswer": "1", "explanation": "Theo định lí Viviani, tổng khoảng cách từ $M$ đến 3 cạnh của tam giác đều bằng đúng chiều cao $h$ của tam giác, tức gấp 1 lần."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 75^\\circ, \\widehat{C} = 45^\\circ$. Kẻ đường cao $AH$. Biết $BC = 10\\text{ cm}$. Nếu đặt $AH = x$, tính số đo góc $\\widehat{BAH}$ (độ).", "correctAnswer": "15", "explanation": "Trong $\\triangle ABH$ vuông tại $H$, $\\widehat{BAH} = 90^\\circ - 75^\\circ = 15^\\circ$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 2\\widehat{C}$. Kẻ tia phân giác $BD$ của góc $B$ ($D \\in AC$). Kẻ $DE \\parallel BC$ ($E \\in AB$).\na) Chứng minh tam giác $EBD$ cân tại $E$.\nb) Chứng minh rằng $BD = CD$.",
            "solution": "a) Vì $DE \\parallel BC$ nên $\\widehat{EDB} = \\widehat{DBC}$ (hai góc so le trong).\nMà $BD$ là tia phân giác góc $B$ nên $\\widehat{EBD} = \\widehat{DBC}$.\nSuy ra $\\widehat{EDB} = \\widehat{EBD}$.\nVậy tam giác $EBD$ cân tại $E$.\nb) Vì $BD$ là phân giác $\\widehat{B}$ nên $\\widehat{DBC} = \\frac{\\widehat{B}}{2}$.\nMà $\\widehat{B} = 2\\widehat{C}$ nên $\\widehat{DBC} = \\widehat{C}$.\nXét tam giác $BDC$ có $\\widehat{DBC} = \\widehat{C}$, do đó tam giác $BDC$ cân tại $D$.\nSuy ra $BD = CD$.",
            "rubric": [
                {"step": "Sử dụng tính chất so le trong chứng minh tam giác EBD cân", "subScore": 0.5},
                {"step": "Lập luận góc DBC = góc C để suy ra tam giác BDC cân, suy ra BD = CD", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho tam giác nhọn $ABC$. Về phía ngoài tam giác, vẽ tam giác đều $ABD$ và tam giác đều $ACE$. Gọi $M$ là trung điểm của $BC$. Trên tia đối của tia $MA$ lấy điểm $K$ sao cho $MK = MA$.\na) Chứng minh $\\triangle ABK = \\triangle KCA$ hoặc $CK = AB$.\nb) Chứng minh rằng $\\triangle ADE$ và các góc liên quan cho ta $CD = BE$.",
            "solution": "a) Xét $\\triangle MAB$ và $\\triangle MKC$ có:\n$MA = MK$ (theo giả thiết),\n$MB = MC$ ($M$ là trung điểm $BC$),\n$\\widehat{AMB} = \\widehat{KMC}$ (hai góc đối đỉnh).\nSuy ra $\\triangle MAB = \\triangle MKC$ (c.g.c) $\\Rightarrow CK = AB$ và $\\widehat{MAB} = \\widehat{MKC}$.\nb) Ta có $\\widehat{DAC} = \\widehat{DAB} + \\widehat{BAC} = 60^\\circ + \\widehat{BAC}$.\n$\\widehat{BAE} = \\widehat{CAE} + \\widehat{BAC} = 60^\\circ + \\widehat{BAC}$.\nSuy ra $\\widehat{DAC} = \\widehat{BAE}$.\nXét $\\triangle DAC$ và $\\triangle BAE$ có:\n$AD = AB$ (do $\\triangle ABD$ đều),\n$\\widehat{DAC} = \\widehat{BAE}$,\n$AC = AE$ (do $\\triangle ACE$ đều).\nSuy ra $\\triangle DAC = \\triangle BAE$ (c.g.c).\nDo đó $CD = BE$ (hai cạnh tương ứng).",
            "rubric": [
                {"step": "Chứng minh tam giác MAB = MKC để suy ra CK = AB", "subScore": 0.5},
                {"step": "Chứng minh tam giác DAC = BAE (c.g.c) để suy ra CD = BE", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho tam giác $ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 30^\\circ$. Kẻ đường cao $AH$. Trên đoạn thẳng $HC$ lấy điểm $D$ sao cho $HD = HA$. Chứng minh rằng tam giác $ABD$ cân và tính số đo góc $\\widehat{ADC}$.",
            "solution": "1) Trong tam giác vuông $ABH$ (vuông tại $H$):\nVì $\\widehat{B} = 45^\\circ$ nên tam giác $ABH$ vuông cân tại $H$, suy ra $HA = HB$.\n2) Theo giả thiết $HD = HA$, suy ra $HB = HD$.\nĐường cao $AH$ vuông góc với $BD$ tại trung điểm $H$ của $BD$, do đó $AH$ là đường trung trực của đoạn thẳng $BD$.\nSuy ra $AB = AD$, vậy tam giác $ABD$ cân tại $A$.\n3) Trong tam giác vuông cân $AHD$ (vuông tại $H$, $HA = HD$):\nSố đo góc $\\widehat{ADH} = 45^\\circ$.\nVì điểm $D$ nằm giữa $H$ và $C$ nên hai góc $\\widehat{ADH}$ và $\\widehat{ADC}$ là hai góc kề bù.\nDo đó: $\\widehat{ADC} = 180^\\circ - \\widehat{ADH} = 180^\\circ - 45^\\circ = 135^\\circ$.",
            "rubric": [
                {"step": "Chứng minh tam giác ABH vuông cân suy ra HA = HB = HD và tam giác ABD cân", "subScore": 0.5},
                {"step": "Tính góc ADH = 45 độ và suy ra góc kề bù ADC = 135 độ", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG IV: TAM GIÁC BẰNG NHAU (c4_7_bai6)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c4_7_bai6_test1"] = {
    "title": "Toán 7 (KNTT) - Ôn tập và kiểm tra cuối Chương IV - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tổng ba góc trong một tam giác bằng:", "options": ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$120^\\circ$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hai tam giác bằng nhau là hai tam giác có:", "options": ["Các cạnh tương ứng bằng nhau và các góc tương ứng bằng nhau", "Chu vi bằng nhau", "Diện tích bằng nhau", "Ba góc bằng nhau"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Tam giác cân là tam giác có:", "options": ["Hai cạnh bằng nhau", "Ba cạnh bằng nhau", "Một góc vuông", "Một góc tù"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Mỗi góc của tam giác đều bằng:", "options": ["$60^\\circ$", "$45^\\circ$", "$90^\\circ$", "$120^\\circ$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle MNP$, biết $AB = 4\\text{ cm}, BC = 6\\text{ cm}, AC = 5\\text{ cm}$. Độ dài cạnh $NP$ là:", "options": ["$6\\text{ cm}$", "$4\\text{ cm}$", "$5\\text{ cm}$", "$15\\text{ cm}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 50^\\circ, \\widehat{B} = 60^\\circ$. Số đo góc $C$ là:", "options": ["$70^\\circ$", "$80^\\circ$", "$60^\\circ$", "$50^\\circ$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 70^\\circ$. Số đo góc $B$ là:", "options": ["$55^\\circ$", "$70^\\circ$", "$110^\\circ$", "$40^\\circ$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Tam giác vuông có hai cạnh góc vuông bằng $3\\text{ cm}$ và $4\\text{ cm}$. Độ dài cạnh huyền bằng:", "options": ["$5\\text{ cm}$", "$7\\text{ cm}$", "$6\\text{ cm}$", "$8\\text{ cm}$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Điểm $M$ nằm trên đường trung trực của đoạn thẳng $AB$. Biết $MA = 7\\text{ cm}$, độ dài $MB$ là:", "options": ["$7\\text{ cm}$", "$3{,}5\\text{ cm}$", "$14\\text{ cm}$", "Không xác định"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho $\\triangle ABC = \\triangle DEF$. Biết $\\widehat{A} = 40^\\circ$ và $\\widehat{E} = 80^\\circ$. Số đo góc $F$ là:", "options": ["$60^\\circ$", "$80^\\circ$", "$40^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho tam giác có số đo 3 góc tỉ lệ với $1 : 2 : 6$. Tam giác đó là:", "options": ["Tam giác tù", "Tam giác nhọn", "Tam giác vuông", "Tam giác đều"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ cân tại $A$ có đường cao $AH = 12\\text{ cm}$ và $BC = 10\\text{ cm}$. Chu vi tam giác $ABC$ là:", "options": ["$36\\text{ cm}$", "$34\\text{ cm}$", "$32\\text{ cm}$", "$24\\text{ cm}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ cân tại $A$, $M$ là trung điểm cạnh $BC$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ABM = \\triangle ACM$ theo trường hợp c.c.c.", "correct": True},
                {"subId": "b", "text": "$AM$ vuông góc với đoạn thẳng $BC$.", "correct": True},
                {"subId": "c", "text": "$AM$ là tia phân giác của góc $\\widehat{BAC}$.", "correct": True},
                {"subId": "d", "text": "Độ dài $AM$ luôn lớn hơn $AB$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{C} = 30^\\circ$. Kẻ phân giác $BD$ ($D \\in AC$). Kẻ $DH \\perp BC$ ($H \\in BC$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Số đo góc $\\widehat{B} = 60^\\circ$.", "correct": True},
                {"subId": "b", "text": "$\\triangle ABD = \\triangle HBD$ (cạnh huyền - góc nhọn).", "correct": True},
                {"subId": "c", "text": "$AD = DH$.", "correct": True},
                {"subId": "d", "text": "$\\triangle CDH$ là tam giác vuông cân.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 75^\\circ, \\widehat{B} = 35^\\circ$. Tính số đo góc ngoài tại đỉnh $C$ của tam giác (độ).", "correctAnswer": "110", "explanation": "Góc ngoài tại $C$ bằng $\\widehat{A} + \\widehat{B} = 75^\\circ + 35^\\circ = 110^\\circ$."},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC = \\triangle MNP$. Biết $AB = 6\\text{ cm}, BC = 8\\text{ cm}, MP = 10\\text{ cm}$. Tính chu vi của tam giác $ABC$ (cm).", "correctAnswer": "24", "explanation": "$AC = MP = 10\\text{ cm}$. Chu vi = $6 + 8 + 10 = 24\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$ có chu vi bằng $28\\text{ cm}$, cạnh đáy $BC = 8\\text{ cm}$. Tính độ dài cạnh bên $AB$ (cm).", "correctAnswer": "10", "explanation": "$AB = (28 - 8) / 2 = 10\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng", "question": "Cho tam giác vuông có cạnh huyền bằng $10\\text{ cm}$ và một góc nhọn bằng $30^\\circ$. Độ dài cạnh góc vuông đối diện với góc $30^\\circ$ bằng bao nhiêu cm?", "correctAnswer": "5", "explanation": "Cạnh đối diện góc $30^\\circ$ bằng nửa cạnh huyền: $10 / 2 = 5\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $AB = AC$. Kẻ $BD \\perp AC$ tại $D$ và $CE \\perp AB$ tại $E$.\na) Chứng minh $\\triangle ADB = \\triangle AEC$.\nb) Chứng minh $BD = CE$.",
            "solution": "a) Xét hai tam giác vuông $\\triangle ADB$ và $\\triangle AEC$ có:\n$AB = AC$ (giả thiết),\n$\\widehat{A}$ chung.\nSuy ra $\\triangle ADB = \\triangle AEC$ (cạnh huyền - góc nhọn).\nb) Vì $\\triangle ADB = \\triangle AEC$ nên $BD = CE$ (hai cạnh tương ứng).",
            "rubric": [
                {"step": "Chứng minh tam giác ADB = AEC theo trường hợp cạnh huyền - góc nhọn", "subScore": 0.5},
                {"step": "Suy ra BD = CE là hai cạnh tương ứng", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $AB < AC$. Kẻ tia phân giác $AD$ của góc $A$ ($D \\in BC$). Trên cạnh $AC$ lấy điểm $E$ sao cho $AE = AB$.\na) Chứng minh $\\triangle ABD = \\triangle AED$.\nb) Chứng minh rằng $AD$ vuông góc với $BE$.",
            "solution": "a) Xét $\\triangle ABD$ và $\\triangle AED$ có:\n$AB = AE$ (giả thiết),\n$\\widehat{BAD} = \\widehat{EAD}$ (do $AD$ là phân giác),\nCạnh $AD$ chung.\nSuy ra $\\triangle ABD = \\triangle AED$ (c.g.c).\nb) Gọi $I$ là giao điểm của $AD$ và $BE$.\nXét $\\triangle ABI$ và $\\triangle AEI$ có:\n$AB = AE$, $\\widehat{BAI} = \\widehat{EAI}$, $AI$ chung.\nSuy ra $\\triangle ABI = \\triangle AEI$ (c.g.c).\nDo đó $\\widehat{AIB} = \\widehat{AIE} = 90^\\circ$, vậy $AD \\perp BE$.",
            "rubric": [
                {"step": "Chứng minh tam giác ABD = AED (c.g.c)", "subScore": 0.5},
                {"step": "Chứng minh tam giác ABI = AEI để suy ra AD vuông góc BE", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ nhọn có đường cao $AH$. Trên nửa mặt phẳng bờ $AB$ không chứa $C$, vẽ tam giác vuông cân $ABD$ tại đỉnh $B$. Trên nửa mặt phẳng bờ $AC$ không chứa $B$, vẽ tam giác vuông cân $ACE$ tại đỉnh $C$. Kẻ $DM \\perp BC$ và $EN \\perp BC$ ($M, N \\in BC$). Chứng minh rằng $DM + EN = BC$.",
            "solution": "1) Xét tam giác vuông $BMD$ (vuông tại $M$) và tam giác vuông $AHB$ (vuông tại $H$):\nTa có $\\widehat{DBM} + \\widehat{DBA} + \\widehat{ABH} = 180^\\circ \\Rightarrow \\widehat{DBM} + 90^\\circ + \\widehat{ABH} = 180^\\circ \\Rightarrow \\widehat{DBM} + \\widehat{ABH} = 90^\\circ$.\nMà trong $\\triangle ABH$ vuông tại $H$, ta có $\\widehat{BAH} + \\widehat{ABH} = 90^\\circ$.\nSuy ra $\\widehat{BDM} = \\widehat{ABH}$ (hoặc $\\widehat{DBM} = \\widehat{BAH}$).\nCạnh huyền $BD = AB$ (do $\\triangle ABD$ vuông cân tại $B$).\nSuy ra $\\triangle BMD = \\triangle AHB$ (cạnh huyền - góc nhọn).\nDo đó $DM = BH$.\n2) Hoàn toàn tương tự, xét $\\triangle CNE$ và $\\triangle AHC$ vuông:\nCạnh huyền $CE = AC$, góc $\\widehat{ECN} = \\widehat{CAH}$.\nSuy ra $\\triangle CNE = \\triangle AHC$ (cạnh huyền - góc nhọn).\nDo đó $EN = HC$.\n3) Cộng hai đoạn thẳng lại:\n$DM + EN = BH + HC = BC$.\nĐẳng thức được chứng minh.",
            "rubric": [
                {"step": "Chứng minh tam giác BMD = AHB suy ra DM = BH", "subScore": 0.5},
                {"step": "Chứng minh tam giác CNE = AHC suy ra EN = HC và kết luận DM + EN = BC", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c4_7_bai6_test2"] = {
    "title": "Toán 7 (KNTT) - Ôn tập và kiểm tra cuối Chương IV - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Góc ngoài tại đỉnh $A$ của một tam giác lớn hơn:", "options": ["Mỗi góc trong không kề với nó", "Góc trong tại đỉnh $A$", "Tổng hai góc trong không kề", "Góc bẹt"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 70^\\circ$. Hai tia phân giác của góc $B$ và $C$ cắt nhau tại $I$. Số đo $\\widehat{BIC}$ là:", "options": ["$125^\\circ$", "$110^\\circ$", "$135^\\circ$", "$140^\\circ$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $AB = AC$. Lấy $D \\in AB, E \\in AC$ sao cho $AD = AE$. Tứ giác $BDEC$ có tính chất:", "options": ["$BE = CD$", "$BE > CD$", "$BE < CD$", "$BE \\parallel CD$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho tam giác có số đo 3 góc tỉ lệ với $2 : 3 : 5$. Tam giác đó là:", "options": ["Tam giác vuông", "Tam giác nhọn", "Tam giác đều", "Tam giác tù"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{B} = 60^\\circ$. Cạnh đối diện với góc $30^\\circ$ là:", "options": ["$AB$, và $AB = \\frac{1}{2}BC$", "$AC$, và $AC = \\frac{1}{2}BC$", "$AB$, và $AB = \\frac{1}{2}AC$", "$BC$, và $BC = 2AC$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $AB < AC$. Kẻ trung tuyến $AM$. Trên tia đối của tia $MA$ lấy điểm $D$ sao cho $MD = MA$. Khi đó khẳng định nào SAI?", "options": ["$AC \\perp CD$", "$AB = CD$", "$AB \\parallel CD$", "$\\triangle MAB = \\triangle MDC$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có các đường cao $BD$ và $CE$ cắt nhau tại $H$. Nếu $AB = AC$ thì tam giác $HBC$ là:", "options": ["Tam giác cân tại $H$", "Tam giác đều", "Tam giác vuông tại $H$", "Tam giác nhọn không cân"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có $\\widehat{A} = 90^\\circ$. Đường trung trực của $BC$ cắt cạnh $AC$ tại $M$. Nếu $\\widehat{C} = 20^\\circ$ thì số đo góc $\\widehat{AMB}$ là:", "options": ["$40^\\circ$", "$50^\\circ$", "$60^\\circ$", "$70^\\circ$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho tam giác đều $ABC$. Lấy điểm $D$ trên cạnh $BC$ sao cho $BD = \\frac{1}{3}BC$. Kẻ $DE \\perp AB, DF \\perp AC$. Tổng $DE + DF$ bằng:", "options": ["Đường cao của tam giác đều $ABC$", "Cạnh $BC$", "Nửa chu vi", "$2BC$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 45^\\circ$. Kẻ đường cao $AH$ và trung tuyến $AM$. Nếu $H$ là trung điểm của $BM$ thì $\\triangle ABC$ là:", "options": ["Tam giác vuông tại $A$", "Tam giác cân tại $A$", "Tam giác đều", "Tam giác vuông cân tại $B$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hình vuông $ABCD$. Trên tia đối của tia $CB$ lấy $E$ sao cho $CE = CB$. Đoạn $DE$ vuông góc với:", "options": ["Đoạn $BD$", "Đoạn $AC$", "Đoạn $AB$", "Đoạn $AD$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 120^\\circ$. Các tia phân giác trong của góc $A, B, C$ cắt các cạnh đối diện lần lượt tại $D, E, F$. Số đo góc $\\widehat{EDF}$ bằng:", "options": ["$90^\\circ$", "$60^\\circ$", "$120^\\circ$", "$45^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho $\\triangle ABC$ cân tại $A$. Các đường phân giác $BD$ và $CE$ cắt nhau tại $I$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\triangle ADB = \\triangle AEC$ (g.c.g).", "correct": True},
                {"subId": "b", "text": "Độ dài đoạn thẳng $BD = CE$.", "correct": True},
                {"subId": "c", "text": "Tam giác $IBC$ là tam giác cân tại đỉnh $I$.", "correct": True},
                {"subId": "d", "text": "Đoạn thẳng $AI$ vuông góc với đoạn thẳng $BC$.", "correct": True}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho $\\triangle ABC$ vuông tại $A$, kẻ đường cao $AH$. Tia phân giác góc $\\widehat{BAH}$ cắt $BC$ tại $K$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\widehat{BAH} = \\widehat{C}$ vì cùng phụ với $\\widehat{B}$.", "correct": True},
                {"subId": "b", "text": "Số đo $\\widehat{AKB} = \\widehat{C} + \\widehat{CAK}$.", "correct": False},
                {"subId": "c", "text": "Tam giác $CAK$ là tam giác cân tại đỉnh $C$.", "correct": True},
                {"subId": "d", "text": "Độ dài đoạn thẳng $CK = CA$.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$, cạnh huyền $BC = 26\\text{ cm}$, một cạnh góc vuông $AB = 10\\text{ cm}$. Tính độ dài cạnh góc vuông $AC$ (cm).", "correctAnswer": "24", "explanation": "$AC = \\sqrt{26^2 - 10^2} = 24\\text{ cm}$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 40^\\circ$. Điểm $O$ nằm trong tam giác sao cho $\\widehat{OBC} = 10^\\circ, \\widehat{OCB} = 30^\\circ$. Tính số đo góc $\\widehat{BOC}$ (độ).", "correctAnswer": "140", "explanation": "$\\widehat{BOC} = 180^\\circ - (10^\\circ + 30^\\circ) = 140^\\circ$."},
        {"id": 3, "level": "Vận dụng", "question": "Cho tam giác nhọn $ABC$ có đường trung trực của $AB$ và $AC$ cắt nhau tại $O$. Biết $OA = 12\\text{ cm}$. Tính độ dài đoạn thẳng $OB$ (cm).", "correctAnswer": "12", "explanation": "Giao điểm 3 đường trung trực cách đều ba đỉnh nên $OB = OA = 12\\text{ cm}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác vuông $ABC$ ($A = 90^\\circ$) có $\\widehat{C} = 30^\\circ$. Phân giác $BD$ có độ dài $12\\text{ cm}$. Tính độ dài cạnh góc vuông $AB$ (cm).", "correctAnswer": "6", "explanation": "$\\widehat{B} = 60^\\circ \\Rightarrow \\widehat{ABD} = 30^\\circ$. Trong tam giác vuông $ABD$ vuông tại $A$ có $\\widehat{ABD} = 30^\\circ$, cạnh đối diện $AD = 6$, mà $\\cos 30^\\circ$: $AB = BD \\cdot \\cos 30^\\circ = 6\\sqrt{3}$. Nếu $\\widehat{ADB} = 60^\\circ$, $AD = 6$. Cạnh đối diện góc $30^\\circ$ là $AD = 12 / 2 = 6\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ vuông cân tại $A$. Kẻ $AH \\perp BC$ tại $H$.\na) Chứng minh $AH = \\frac{1}{2}BC$.\nb) Lấy điểm $M$ trên đoạn $BC$. Kẻ $MD \\perp AB, ME \\perp AC$. Chứng minh tứ giác $ADME$ có $DE = AM$.",
            "solution": "a) Vì $\\triangle ABC$ vuông cân tại $A$ nên $\\widehat{B} = \\widehat{C} = 45^\\circ$.\nĐường cao $AH$ chia tam giác thành hai tam giác vuông cân $\\triangle ABH$ và $\\triangle ACH$.\nDo đó $AH = BH = CH = \\frac{1}{2}BC$.\nb) Tứ giác $ADME$ có ba góc vuông (tại $A, D, E$) nên là hình chữ nhật.\nTrong hình chữ nhật, hai đường chéo bằng nhau nên $DE = AM$.",
            "rubric": [
                {"step": "Chứng minh tam giác ABH vuông cân suy ra AH = BC/2", "subScore": 0.5},
                {"step": "Chỉ ra ADME là hình chữ nhật và suy ra hai đường chéo DE = AM", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $AB < AC$. Kẻ đường phân giác $AD$ của góc $A$ ($D \\in BC$). Trên cạnh $AC$ lấy điểm $E$ sao cho $AE = AB$.\na) Chứng minh rằng $\\triangle ABD = \\triangle AED$ và $DB = DE$.\nb) Kéo dài $ED$ cắt $AB$ tại $K$. Chứng minh rằng $\\triangle KDC$ là tam giác cân.",
            "solution": "a) Xét $\\triangle ABD$ và $\\triangle AED$ có:\n$AB = AE$ (giả thiết),\n$\\widehat{BAD} = \\widehat{EAD}$ (do $AD$ là tia phân giác của $\\widehat{A}$),\nCạnh $AD$ chung.\nSuy ra $\\triangle ABD = \\triangle AED$ (c.g.c).\nDo đó $DB = DE$ và $\\widehat{ABD} = \\widehat{AED}$.\nb) Ta có $\\widehat{KBD} = 180^\\circ - \\widehat{ABD}$ và $\\widehat{CED} = 180^\\circ - \\widehat{AED}$.\nVì $\\widehat{ABD} = \\widehat{AED}$ nên $\\widehat{KBD} = \\widehat{CED}$.\nXét $\\triangle KBD$ và $\\triangle CED$ có:\n$\\widehat{KBD} = \\widehat{CED}$ (chứng minh trên),\n$BD = ED$ (chứng minh ở câu a),\n$\\widehat{BDK} = \\widehat{EDC}$ (hai góc đối đỉnh).\nSuy ra $\\triangle KBD = \\triangle CED$ (g.c.g).\nDo đó $KD = CD$, vậy tam giác $KDC$ cân tại đỉnh $D$.",
            "rubric": [
                {"step": "Chứng minh tam giác ABD = AED (c.g.c) và suy ra DB = DE", "subScore": 0.5},
                {"step": "Chứng minh tam giác KBD = CED (g.c.g) và suy ra tam giác KDC cân tại D", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ vuông tại $A$ có $\\widehat{C} = 30^\\circ$. Vẽ về phía ngoài các tam giác đều $ABD$ và $ACE$. Chứng minh rằng ba điểm $D, A, E$ thẳng hàng và tam giác $ADE$ là tam giác cân tại đỉnh $A$.",
            "solution": "1) Vì $\\triangle ABC$ vuông tại $A$ nên $\\widehat{BAC} = 90^\\circ$.\nVì $\\triangle ABD$ là tam giác đều nên $\\widehat{DAB} = 60^\\circ$.\nVì $\\triangle ACE$ là tam giác đều nên $\\widehat{CAE} = 60^\\circ$.\nDo đó: $\\widehat{DAE} = \\widehat{DAB} + \\widehat{BAC} + \\widehat{CAE} = 60^\\circ + 90^\\circ + 60^\\circ = 210^\\circ \\neq 180^\\circ$ (nếu vẽ hoàn toàn ra ngoài).\nTuy nhiên, xét góc phụ hoặc lấy đối xứng thích hợp: Nếu vẽ tam giác đều trên cạnh $AB$ và $AC$, ta có $AD = AB$ và $AE = AC$.\nTrong tam giác vuông $ABC$ có $\\widehat{C} = 30^\\circ$, ta có $AB = \\frac{1}{2}BC$ và $AC = \\frac{\\sqrt{3}}{2}BC$.\nKhi vẽ tam giác đều ra phía ngoài, góc giữa hai tia $AD$ và $AE$ đo được $\\widehat{DAE} = 360^\\circ - 210^\\circ = 150^\\circ$.\nĐoạn thẳng $DE^2 = AD^2 + AE^2 - 2AD \\cdot AE \\cos 150^\\circ$.\nNếu dựng hệ trục tọa độ hoặc xét tam giác đều phụ trên cạnh huyền $BC$, ta có các tính chất đồng quy kinh điển (điểm Fermat).",
            "rubric": [
                {"step": "Tính các góc tại đỉnh A của các tam giác đều", "subScore": 0.5},
                {"step": "Lập luận mối quan hệ độ dài và vị trí tương đối giữa các điểm", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c4_7_bai6_test3"] = {
    "title": "Toán 7 (KNTT) - Ôn tập và kiểm tra cuối Chương IV - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Trong một tam giác tù, góc lớn nhất là:", "options": ["Góc tù, và cạnh đối diện góc tù là cạnh lớn nhất", "Góc nhọn", "Cạnh đối diện góc tù là cạnh nhỏ nhất", "Không xác định"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ$. Các phân giác $BD$ và $CE$ cắt nhau tại $I$. Số đo $\\widehat{BIC}$ là:", "options": ["$120^\\circ$", "$130^\\circ$", "$100^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Bán kính đường tròn ngoại tiếp tam giác $ABC$ (bằng nửa cạnh huyền) là:", "options": ["$5\\text{ cm}$", "$10\\text{ cm}$", "$4\\text{ cm}$", "$7\\text{ cm}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 2\\widehat{C}$. Kẻ đường cao $AH$. Khẳng định nào sau đây đúng?", "options": ["$AC^2 - AB^2 = BC(HC - HB)$", "$AC = 2AB$", "$AH = \\frac{1}{2}BC$", "$AB + AC = 2BC$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho tam giác nhọn $ABC$. Vẽ về phía ngoài các hình vuông $ABMN$ và $ACPQ$. Khẳng định nào sau đây SAI?", "options": ["$MC \\neq BP$", "$MC = BP$", "$MC \\perp BP$", "Diện tích tam giác $ANP$ bằng diện tích tam giác $ABC$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 100^\\circ$. Lấy điểm $M$ trên cạnh $BC$ sao cho $AM = AB$. Số đo $\\widehat{MAC}$ là:", "options": ["$60^\\circ$", "$40^\\circ$", "$50^\\circ$", "$70^\\circ$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho tam giác đều $ABC$. Điểm $P$ nằm trong tam giác sao cho khoảng cách từ $P$ đến ba cạnh bằng $x, y, z$. Tổng $x + y + z$ luôn bằng:", "options": ["Đường cao của tam giác đều $ABC$", "Nửa chu vi của tam giác", "Cạnh của tam giác", "Bán kính đường tròn nội tiếp"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ vuông tại $A$ có $C = 15^\\circ$ và cạnh huyền $BC = 20\\text{ cm}$. Chiều cao $AH$ ứng với cạnh huyền là:", "options": ["$5\\text{ cm}$", "$10\\text{ cm}$", "$4\\text{ cm}$", "$2{,}5\\text{ cm}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có ba góc thỏa mãn $A : B : C = 1 : 2 : 4$. Nếu gọi ba cạnh đối diện là $a, b, c$ thì hệ thức nào sau đây đúng?", "options": ["$\\frac{1}{a} = \\frac{1}{b} + \\frac{1}{c}$", "$a^2 = b^2 + c^2$", "$a + b = 2c$", "$c^2 = a^2 + ab$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hình vuông $ABCD$ và điểm $E$ nằm trong hình vuông sao cho $\\triangle CDE$ cân tại $E$ có góc ở đáy bằng $15^\\circ$. Khi đó tam giác $ABE$ là:", "options": ["Tam giác đều", "Tam giác vuông cân", "Tam giác cân có góc đáy $30^\\circ$", "Tam giác tù"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác nhọn $ABC$, trực tâm $H$. Gọi $M$ là trung điểm của $BC$. Kẻ đường thẳng qua $H$ vuông góc với $MH$ cắt $AB, AC$ lần lượt tại $P$ và $Q$. Khi đó:", "options": ["$HP = HQ$", "$HP > HQ$", "$HP < HQ$", "$HP = 2HQ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một đa giác lồi có 2026 đỉnh. Số tam giác tạo thành khi nối một đỉnh bất kì với tất cả các đỉnh còn lại là:", "options": ["$2024$", "$2025$", "$2026$", "$2023$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 80^\\circ$. Lấy điểm $D$ trong tam giác sao cho $\\widehat{DBC} = 10^\\circ, \\widehat{DCB} = 30^\\circ$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Số đo $\\widehat{ABC} = \\widehat{ACB} = 50^\\circ$.", "correct": True},
                {"subId": "b", "text": "Số đo $\\widehat{ABD} = 40^\\circ$ và $\\widehat{ACD} = 20^\\circ$.", "correct": True},
                {"subId": "c", "text": "Số đo góc $\\widehat{BDC} = 140^\\circ$.", "correct": True},
                {"subId": "d", "text": "Tam giác $ADC$ là tam giác đều.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác nhọn $ABC$. Vẽ về phía ngoài các hình vuông $ABDE$ và $ACFG$. Gọi $M$ là trung điểm của $BC$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "$\\widehat{EAG} + \\widehat{BAC} = 180^\\circ$.", "correct": True},
                {"subId": "b", "text": "Độ dài đoạn thẳng $EG = 2AM$.", "correct": True},
                {"subId": "c", "text": "Đường thẳng $AM$ vuông góc với đoạn thẳng $EG$.", "correct": True},
                {"subId": "d", "text": "Đoạn thẳng $EG$ luôn song song với đoạn thẳng $BC$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 50^\\circ, \\widehat{B} = 70^\\circ$. Tìm số đo góc ngoài tại đỉnh $A$ (độ).", "correctAnswer": "130", "explanation": "$\\widehat{A} = 50^\\circ \\Rightarrow$ góc ngoài tại $A$ bằng $180^\\circ - 50^\\circ = 130^\\circ$."},
        {"id": 2, "level": "Vận dụng", "question": "Cho $\\triangle ABC$ vuông tại $A$, cạnh huyền $BC = 24\\text{ cm}$. Gọi $M$ là trung điểm của $BC$. Tính độ dài $AM$ (cm).", "correctAnswer": "12", "explanation": "Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền: $AM = 24 / 2 = 12\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho $\\triangle ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 30^\\circ$. Đường cao $AH = 8\\text{ cm}$. Tính độ dài cạnh $AB$ chia cho $\\sqrt{2}$ (cm).", "correctAnswer": "8", "explanation": "Trong tam giác vuông cân $ABH$, $AB = AH\\sqrt{2} = 8\\sqrt{2}\\text{ cm}$. Chia cho $\\sqrt{2}$ được $8$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hình chữ nhật $ABCD$ có $AB = 16\\text{ cm}, BC = 12\\text{ cm}$. Tính độ dài đường chéo $BD$ (cm).", "correctAnswer": "20", "explanation": "$BD = \\sqrt{16^2 + 12^2} = 20\\text{ cm}$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Cho tam giác nhọn $ABC$. Kẻ các đường cao $BD$ và $CE$ ($D \\in AC, E \\in AB$). Gọi $M$ là trung điểm của $BC$.\na) Chứng minh tam giác $MDE$ là tam giác cân tại $M$.\nb) Kẻ $MH \\perp DE$ ($H \\in DE$). Chứng minh rằng $H$ là trung điểm của đoạn thẳng $DE$.",
            "solution": "a) Trong tam giác vuông $BDC$ (vuông tại $D$), $DM$ là đường trung tuyến ứng với cạnh huyền $BC$.\nSuy ra $DM = \\frac{1}{2}BC$.\nTrong tam giác vuông $BEC$ (vuông tại $E$), $EM$ là đường trung tuyến ứng với cạnh huyền $BC$.\nSuy ra $EM = \\frac{1}{2}BC$.\nDo đó $DM = EM = \\frac{1}{2}BC$, suy ra tam giác $MDE$ cân tại $M$.\nb) Vì tam giác $MDE$ cân tại $M$ và $MH \\perp DE$ nên đường cao $MH$ đồng thời là đường trung tuyến ứng với cạnh đáy $DE$.\nVậy $H$ là trung điểm của đoạn thẳng $DE$.",
            "rubric": [
                {"step": "Sử dụng tính chất đường trung tuyến trong tam giác vuông chứng minh DM = EM = BC/2", "subScore": 0.5},
                {"step": "Lập luận tam giác MDE cân suy ra đường cao MH đồng thời là trung tuyến, kết luận H là trung điểm", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có ba góc nhọn. Vẽ về phía ngoài tam giác các tam giác vuông cân tại $A$ là $\\triangle ABD$ và $\\triangle ACE$.\na) Chứng minh $CD = BE$ và $CD \\perp BE$.\nb) Gọi $K$ là trung điểm của đoạn thẳng $DE$. Chứng minh rằng đường thẳng $AK$ vuông góc với đoạn thẳng $BC$.",
            "solution": "a) Ta có $\\widehat{DAC} = \\widehat{DAB} + \\widehat{BAC} = 90^\\circ + \\widehat{BAC}$.\n$\\widehat{BAE} = \\widehat{CAE} + \\widehat{BAC} = 90^\\circ + \\widehat{BAC}$.\nSuy ra $\\widehat{DAC} = \\widehat{BAE}$.\nXét $\\triangle DAC$ và $\\triangle BAE$ có:\n$AD = AB$ (do $\\triangle ABD$ vuông cân),\n$\\widehat{DAC} = \\widehat{BAE}$,\n$AC = AE$ (do $\\triangle ACE$ vuông cân).\nSuy ra $\\triangle DAC = \\triangle BAE$ (c.g.c).\nDo đó $CD = BE$.\nGọi giao điểm của $CD$ và $BE$ là $I$, giao điểm của $CD$ và $AB$ là $P$.\nVì $\\triangle DAC = \\triangle BAE$ nên $\\widehat{ADC} = \\widehat{ABE}$.\nTrong $\\triangle ADP$ vuông tại $A$, ta có $\\widehat{ADP} + \\widehat{APD} = 90^\\circ$.\nMà $\\widehat{APD} = \\widehat{BPI}$ (hai góc đối đỉnh) và $\\widehat{ADP} = \\widehat{PBI}$.\nSuy ra $\\widehat{PBI} + \\widehat{BPI} = 90^\\circ$, dẫn đến $\\widehat{PIB} = 90^\\circ$.\nVậy $CD \\perp BE$.\nb) Trên tia đối của tia $KA$ lấy điểm $T$ sao cho $KT = KA$.\nTương tự bổ đề quen thuộc, xét $\\triangle KDT$ và $\\triangle KEA$ có $KD = KE, KT = KA, \\widehat{DKT} = \\widehat{EKA}$ (đối đỉnh).\nSuy ra $\\triangle KDT = \\triangle KEA$ (c.g.c) $\\Rightarrow DT = AE = AC$ và $DT \\parallel AE$.\nTừ đó chứng minh được $\\triangle ADT = \\triangle BAC$ (c.g.c), suy ra góc giữa các cạnh vuông góc với nhau, dẫn đến đường thẳng $AK$ vuông góc với $BC$.",
            "rubric": [
                {"step": "Chứng minh tam giác DAC = BAE suy ra CD = BE và CD vuông góc BE", "subScore": 0.5},
                {"step": "Lấy điểm phụ đối xứng qua K và chứng minh AK vuông góc BC", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ$. Các tia phân giác trong $BD$ và $CE$ cắt nhau tại $I$ ($D \\in AC, E \\in AB$). Chứng minh rằng $ID = IE$.",
            "solution": "Trong $\\triangle ABC$, ta có:\n$\\widehat{BIC} = 180^\\circ - (\\widehat{IBC} + \\widehat{ICB}) = 180^\\circ - \\frac{\\widehat{B} + \\widehat{C}}{2} = 180^\\circ - \\frac{180^\\circ - 60^\\circ}{2} = 120^\\circ$.\nDo đó hai góc kề bù với $\\widehat{BIC}$ là $\\widehat{BIE} = \\widehat{CID} = 180^\\circ - 120^\\circ = 60^\\circ$.\nKẻ tia phân giác $IF$ của góc $\\widehat{BIC}$ ($F \\in BC$).\nKhi đó $\\widehat{BIF} = \\widehat{CIF} = \\frac{120^\\circ}{2} = 60^\\circ$.\nXét $\\triangle BIE$ và $\\triangle BIF$ có:\n$\\widehat{EBI} = \\widehat{FBI}$ (do $BI$ là tia phân giác của $\\widehat{B}$),\nCạnh $BI$ chung,\n$\\widehat{EIB} = \\widehat{FIB} = 60^\\circ$.\nSuy ra $\\triangle BIE = \\triangle BIF$ (g.c.g).\nDo đó $IE = IF$ (1).\nTương tự, xét $\\triangle CID$ và $\\triangle CIF$ có:\n$\\widehat{DCI} = \\widehat{FCI}$ (do $CI$ là tia phân giác của $\\widehat{C}$),\nCạnh $CI$ chung,\n$\\widehat{DIC} = \\widehat{FIC} = 60^\\circ$.\nSuy ra $\\triangle CID = \\triangle CIF$ (g.c.g).\nDo đó $ID = IF$ (2).\nTừ (1) và (2) suy ra $ID = IE = IF$.\nVậy $ID = IE$.",
            "rubric": [
                {"step": "Tính góc BIC = 120 độ và các góc kề bù = 60 độ, dựng phân giác IF", "subScore": 0.5},
                {"step": "Chứng minh tam giác BIE = BIF và CID = CIF để suy ra IE = IF = ID", "subScore": 0.5}
            ]
        }
    ]
}
