# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 9 - CHƯƠNG IV (PHẦN 2)
Bao gồm:
- Bài kiểm tra cuối Chương IV: Hệ thức lượng trong tam giác vuông (3 đề: Cơ bản, Khá, Nâng cao)
Chuẩn ma trận Bộ GD&ĐT 2025: 12 TN + 2 Đ/S (8 ý) + 4 TLN + 3 TL. Tổng 10.0 điểm.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

EXAMS_PART2 = {}

# =====================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG IV: HỆ THỨC LƯỢNG TRONG TAM GIÁC VUÔNG
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c4_9_bai3_test1"] = {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương IV: Hệ thức lượng trong tam giác vuông - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Hệ thức nào sau đây diễn tả định lí Pythagore?", "options": ["$BC^2 = AB^2 + AC^2$", "$AB^2 = BC^2 + AC^2$", "$AC^2 = AB^2 + BC^2$", "$BC = AB + AC$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Hệ thức nào sau đây là đúng?", "options": ["$AH^2 = BH \\cdot CH$", "$AH = BH \\cdot CH$", "$AH^2 = AB \\cdot AC$", "$AH^2 = BC^2$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Hệ thức liên hệ giữa cạnh góc vuông và hình chiếu của nó trên cạnh huyền là:", "options": ["$AB^2 = BH \\cdot BC$", "$AB^2 = CH \\cdot BC$", "$AB^2 = AH \\cdot BC$", "$AB = BH \\cdot BC$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Tích hai cạnh góc vuông bằng tích của:", "options": ["Cạnh huyền và đường cao tương ứng ($AB \\cdot AC = BC \\cdot AH$)", "Hai hình chiếu của hai cạnh góc vuông", "Đường cao và hình chiếu", "Cạnh huyền và bình phương đường cao"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Cho góc nhọn $\\alpha$. Khẳng định nào sau đây là SAI?", "options": ["$\\tan \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$", "$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$", "$\\tan \\alpha \\cdot \\cot \\alpha = 1$", "$\\cot \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$ cm, $BC = 5$ cm. Khi đó $\\cos C$ bằng:", "options": ["$\\frac{4}{5}$", "$\\frac{3}{5}$", "$\\frac{3}{4}$", "$\\frac{4}{3}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 2$ cm, $CH = 8$ cm. Chiều cao $AH$ bằng:", "options": ["$4$ cm", "$16$ cm", "$5$ cm", "$10$ cm"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AC = 6$ cm, $\\widehat{C} = 30^\\circ$. Cạnh huyền $BC$ bằng:", "options": ["$4\\sqrt{3}$ cm", "$12$ cm", "$3\\sqrt{3}$ cm", "$6\\sqrt{3}$ cm"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Giá trị của biểu thức $P = \\sin 30^\\circ \\cdot \\cos 60^\\circ + \\cos 30^\\circ \\cdot \\sin 60^\\circ$ là:", "options": ["$1$", "$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$0$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Một cái cây cao $6$ m đổ bóng trên mặt đất dài $8$ m. Góc tia sáng mặt trời tạo với mặt đất (làm tròn đến độ) xấp xỉ:", "options": ["$37^\\circ$", "$53^\\circ$", "$45^\\circ$", "$30^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 6$ cm, $BC = 10$ cm. Độ dài đoạn $BH$ bằng:", "options": ["$3{,}6$ cm", "$4{,}8$ cm", "$6{,}4$ cm", "$4$ cm"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Cho góc nhọn $\\alpha$ có $\\sin \\alpha = \\frac{1}{3}$. Giá trị của biểu thức $M = 9\\cos^2 \\alpha + 1$ là:", "options": ["$9$", "$8$", "$10$", "$7$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6$ cm, $AC = 8$ cm, đường cao $AH$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Độ dài cạnh huyền $BC = 10$ cm.", "isCorrect": True, "explanation": "$BC = \\sqrt{6^2 + 8^2} = 10$ cm."},
                {"id": "b", "statement": "Độ dài đường cao $AH = 4{,}8$ cm.", "isCorrect": True, "explanation": "$AH = \\frac{AB \\cdot AC}{BC} = \\frac{6 \\cdot 8}{10} = 4{,}8$ cm."},
                {"id": "c", "statement": "Độ dài hình chiếu $BH = 3{,}6$ cm.", "isCorrect": True, "explanation": "$BH = \\frac{AB^2}{BC} = \\frac{36}{10} = 3{,}6$ cm."},
                {"id": "d", "statement": "Tỉ số lượng giác $\\sin B = 0{,}6$.", "isCorrect": False, "explanation": "$\\sin B = AC / BC = 8/10 = 0{,}8$ (không phải $0{,}6$)."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\cos \\alpha = 0{,}6$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$\\sin \\alpha = 0{,}8$.", "isCorrect": True, "explanation": "$\\sin \\alpha = \\sqrt{1 - 0{,}6^2} = 0{,}8$."},
                {"id": "b", "statement": "$\\tan \\alpha = \\frac{4}{3}$.", "isCorrect": True, "explanation": "$\\tan \\alpha = \\sin \\alpha / \\cos \\alpha = 0{,}8 / 0{,}6 = 4/3$."},
                {"id": "c", "statement": "$\\cot \\alpha = \\frac{3}{4}$.", "isCorrect": True, "explanation": "$\\cot \\alpha = 1 / \\tan \\alpha = 3/4$."},
                {"id": "d", "statement": "Biểu thức $\\tan \\alpha + \\cot \\alpha = 2$.", "isCorrect": False, "explanation": "$\\tan \\alpha + \\cot \\alpha = 4/3 + 3/4 = 25/12 \\approx 2{,}08 \\neq 2$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 4$ cm, $CH = 9$ cm. Tính độ dài đường cao $AH$ theo cm.", "answer": 6, "unit": "cm"},
        {"id": 2, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $A = 2\\sin 30^\\circ + 3\\tan 45^\\circ - \\cos 60^\\circ$.", "answer": 3.5, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$ có $BC = 20$ cm và $\\sin B = 0{,}6$. Tính độ dài cạnh $AB$ theo cm.", "answer": 16, "unit": "cm"},
        {"id": 4, "level": "Vận dụng", "question": "Một chiếc thang dài $5$ m dựa vào tường. Chân thang cách tường $2$ m. Tính góc tạo bởi thang và mặt đất theo độ (làm tròn đến hàng đơn vị, biết $\\cos 66^\\circ \\approx 0{,}4067$).", "answer": 66, "unit": "độ"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có đường cao $AH$. Biết $AB = 15$ cm, $AC = 20$ cm.\na) Tính độ dài cạnh $BC$ và đường cao $AH$.\nb) Tính độ dài các đoạn thẳng $BH$ và $CH$.",
            "maxScore": 1.0,
            "solution": "a) Áp dụng định lí Pythagore trong tam giác vuông $ABC$:\n$BC = \\sqrt{AB^2 + AC^2} = \\sqrt{15^2 + 20^2} = \\sqrt{225 + 400} = \\sqrt{625} = 25$ cm.\nÁp dụng hệ thức lượng $AB \\cdot AC = BC \\cdot AH$:\n$AH = \\frac{AB \\cdot AC}{BC} = \\frac{15 \\cdot 20}{25} = 12$ cm.\nb) Áp dụng hệ thức liên hệ giữa cạnh góc vuông và hình chiếu:\n$BH = \\frac{AB^2}{BC} = \\frac{15^2}{25} = \\frac{225}{25} = 9$ cm.\n$CH = BC - BH = 25 - 9 = 16$ cm (hoặc $CH = \\frac{AC^2}{BC} = \\frac{400}{25} = 16$ cm).",
            "rubric": [
                {"step": "Tính đúng BC = 25 cm và AH = 12 cm", "subScore": 0.5},
                {"step": "Tính đúng BH = 9 cm và CH = 16 cm", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 30^\\circ$ và cạnh huyền $BC = 16$ cm. Kẻ đường cao $AH$.\na) Giải tam giác vuông $ABC$ (tính các cạnh và các góc còn lại).\nb) Tính diện tích tam giác $ABH$.",
            "maxScore": 1.0,
            "solution": "a) Trong tam giác vuông $ABC$:\n$\\widehat{C} = 90^\\circ - \\widehat{B} = 90^\\circ - 30^\\circ = 60^\\circ$.\n$AC = BC \\cdot \\sin B = 16 \\cdot \\sin 30^\\circ = 16 \\cdot \\frac{1}{2} = 8$ cm.\n$AB = BC \\cdot \\cos B = 16 \\cdot \\cos 30^\\circ = 16 \\cdot \\frac{\\sqrt{3}}{2} = 8\\sqrt{3}$ cm.\nb) Trong tam giác vuông $ABH$ vuông tại $H$:\n$AH = AB \\cdot \\sin B = 8\\sqrt{3} \\cdot \\frac{1}{2} = 4\\sqrt{3}$ cm.\n$BH = AB \\cdot \\cos B = 8\\sqrt{3} \\cdot \\frac{\\sqrt{3}}{2} = 12$ cm.\nDiện tích tam giác $ABH$ là:\n$S_{ABH} = \\frac{1}{2} AH \\cdot BH = \\frac{1}{2} \\cdot 4\\sqrt{3} \\cdot 12 = 24\\sqrt{3}$ cm$^2$.",
            "rubric": [
                {"step": "Tính đúng góc C = 60 độ, AC = 8 cm, AB = 8 căn 3 cm", "subScore": 0.5},
                {"step": "Tính AH = 4 căn 3 cm, BH = 12 cm và diện tích = 24 căn 3 cm^2", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một người đứng trên đỉnh của ngọn hải đăng cao $45$ m so với mực nước biển quan sát một chiếc tàu đang neo đậu ngoài khơi với góc hạ $22^\\circ$. Hãy tính khoảng cách từ chân ngọn hải đăng đến chiếc tàu (làm tròn đến hàng đơn vị mét, biết $\\tan 22^\\circ \\approx 0{,}4040$).",
            "maxScore": 1.0,
            "solution": "Gọi ngọn hải đăng là đoạn thẳng thẳng đứng $AB$ với $A$ là đỉnh đèn, $B$ là chân đèn tại mực nước biển ($AB = 45$ m).\nGọi vị trí con tàu trên mặt biển là $C$. Tam giác $ABC$ vuông tại $B$.\nGóc hạ của người quan sát là góc tạo bởi tia nhìn $AC$ với phương nằm ngang $Ax$, do đó theo tính chất so le trong:\n$\\widehat{ACB} = 22^\\circ$.\nTrong tam giác vuông $ABC$ tại $B$, ta có:\n$\\tan C = \\frac{AB}{BC} \\Rightarrow BC = \\frac{AB}{\\tan C} = \\frac{45}{\\tan 22^\\circ}$.\nThay số:\n$BC \\approx \\frac{45}{0{,}4040} \\approx 111{,}39 \\approx 111$ m.\nVậy khoảng cách từ chân ngọn hải đăng đến chiếc tàu khoảng $111$ mét.",
            "rubric": [
                {"step": "Vẽ hình hoặc mô tả tam giác vuông và góc ACB = 22 độ", "subScore": 0.5},
                {"step": "Tính khoảng cách BC xấp xỉ 111 m và kết luận", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c4_9_bai3_test2"] = {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương IV: Hệ thức lượng trong tam giác vuông - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 5$ cm, $AC = 12$ cm. Độ dài đường cao $AH$ là:", "options": ["$\\frac{60}{13}$ cm", "$\\frac{13}{60}$ cm", "$13$ cm", "$6{,}5$ cm"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 9$ cm, $HC = 16$ cm. Chu vi của tam giác $ABC$ là:", "options": ["$60$ cm", "$50$ cm", "$72$ cm", "$48$ cm"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 45^\\circ$ và cạnh huyền $BC = 10$ cm. Diện tích của tam giác $ABC$ là:", "options": ["$25$ cm$^2$", "$50$ cm$^2$", "$25\\sqrt{2}$ cm$^2$", "$100$ cm$^2$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Biểu thức $E = \\frac{\\sin^2 38^\\circ + \\sin^2 52^\\circ}{\\tan 20^\\circ \\cdot \\tan 70^\\circ}$ có giá trị bằng:", "options": ["$1$", "$2$", "$0$", "$\\frac{1}{2}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho góc nhọn $\\alpha$ có $\\tan \\alpha = \\frac{5}{12}$. Giá trị của $\\cos \\alpha$ là:", "options": ["$\\frac{12}{13}$", "$\\frac{5}{13}$", "$\\frac{13}{12}$", "$\\frac{13}{5}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Tam giác $ABC$ nhọn có $AB = 6$ cm, $AC = 8$ cm và góc $\\widehat{A} = 60^\\circ$. Diện tích của tam giác $ABC$ là:", "options": ["$12\\sqrt{3}$ cm$^2$", "$24\\sqrt{3}$ cm$^2$", "$12$ cm$^2$", "$24$ cm$^2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Một người nhìn thấy đỉnh một tòa nhà cao tầng dưới góc nâng $40^\\circ$. Sau khi lùi ra xa thêm $30$ m thì thấy đỉnh tòa nhà dưới góc nâng $30^\\circ$. Chiều cao của tòa nhà (làm tròn đến hàng đơn vị mét) là:", "options": ["$56$ m", "$62$ m", "$48$ m", "$70$ m"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AH = 12$ cm và $\\frac{BH}{CH} = \\frac{9}{16}$. Độ dài cạnh huyền $BC$ là:", "options": ["$25$ cm", "$20$ cm", "$30$ cm", "$35$ cm"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho góc nhọn $\\alpha$ biết $\\sin \\alpha + \\cos \\alpha = \\frac{5}{4}$. Giá trị của $\\sin \\alpha \\cdot \\cos \\alpha$ là:", "options": ["$\\frac{9}{32}$", "$\\frac{9}{16}$", "$\\frac{3}{8}$", "$\\frac{25}{32}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho hình chữ nhật $ABCD$ có $AB = 8$ cm, $BC = 6$ cm. Kẻ $AH \\perp BD$ tại $H$. Độ dài đoạn thẳng $AH$ là:", "options": ["$4{,}8$ cm", "$5$ cm", "$3{,}6$ cm", "$6{,}4$ cm"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 30^\\circ$ và $BC = 10(\\sqrt{3}+1)$ cm. Đường cao $AH$ có độ dài là:", "options": ["$10$ cm", "$5\\sqrt{3}$ cm", "$10\\sqrt{3}$ cm", "$20$ cm"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho tam giác vuông $ABC$ tại $A$. Gọi $r$ là bán kính đường tròn nội tiếp, $a, b, c$ lần lượt là độ dài ba cạnh $BC, AC, AB$. Công thức nào sau đây diễn tả đúng bán kính $r$?", "options": ["$r = \\frac{b + c - a}{2}$", "$r = \\frac{b + c + a}{2}$", "$r = \\frac{bc}{2a}$", "$r = \\frac{a + b - c}{2}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 15$ cm, $CH = 16$ cm. Đặt $BH = x$ ($x > 0$). Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Phương trình tìm $x$ là $x(x + 16) = 225$.", "isCorrect": True, "explanation": "Theo hệ thức lượng $AB^2 = BH \\cdot BC \\Leftrightarrow 15^2 = x(x + 16) \\Leftrightarrow x^2 + 16x - 225 = 0$."},
                {"id": "b", "statement": "Giải phương trình ta tìm được $x = 9$ cm.", "isCorrect": True, "explanation": "$x^2 + 16x - 225 = (x - 9)(x + 25) = 0 \\Rightarrow x = 9$."},
                {"id": "c", "statement": "Cạnh huyền $BC = 25$ cm.", "isCorrect": True, "explanation": "$BC = BH + CH = 9 + 16 = 25$ cm."},
                {"id": "d", "statement": "Cạnh góc vuông $AC = 18$ cm.", "isCorrect": False, "explanation": "$AC = \\sqrt{BC^2 - AB^2} = \\sqrt{25^2 - 15^2} = 20$ cm, không phải $18$ cm."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ có ba góc nhọn, các đường cao $BD$ và $CE$ cắt nhau tại $H$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Bốn điểm $A, E, H, D$ cùng thuộc một đường tròn đường kính $AH$.", "isCorrect": True, "explanation": "Vì $\\widehat{AEH} = \\widehat{ADH} = 90^\\circ$ nên $E, D$ cùng nhìn $AH$ dưới góc vuông."},
                {"id": "b", "statement": "Bốn điểm $B, C, D, E$ cùng thuộc một đường tròn đường kính $BC$.", "isCorrect": True, "explanation": "Vì $\\widehat{BEC} = \\widehat{BDC} = 90^\\circ$ nên $E, D$ nhìn $BC$ dưới góc vuông."},
                {"id": "c", "statement": "Tam giác $ADE$ đồng dạng với tam giác $ABC$.", "isCorrect": True, "explanation": "Tứ giác $BCDE$ nội tiếp $\\Rightarrow \\widehat{ADE} = \\widehat{ABC} \\Rightarrow \\triangle ADE \\backsim \\triangle ABC$."},
                {"id": "d", "statement": "Tỉ số đồng dạng của $\\triangle ADE$ và $\\triangle ABC$ là $\\sin A$.", "isCorrect": False, "explanation": "Tỉ số đồng dạng $k = \\frac{AD}{AB} = \\cos A$, không phải $\\sin A$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 20$ cm, $AH = 12$ cm. Tính độ dài cạnh $BC$ theo cm.", "answer": 25, "unit": "cm"},
        {"id": 2, "level": "Vận dụng", "question": "Cho tam giác $ABC$ nhọn có $AB = 8$ cm, $AC = 10$ cm và diện tích $S = 20\\sqrt{3}$ cm$^2$. Tính số đo góc $\\widehat{A}$ theo độ.", "answer": 60, "unit": "độ"},
        {"id": 3, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $P = \\sin^2 10^\\circ + \\sin^2 20^\\circ + \\dots + \\sin^2 80^\\circ$.", "answer": 4, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hình thang vuông $ABCD$ có $\\widehat{A} = \\widehat{D} = 90^\\circ$, hai đường chéo $AC$ và $BD$ vuông góc với nhau tại $O$. Biết $AB = 9$ cm, $CD = 16$ cm. Tính độ dài đường cao $AD$ theo cm.", "answer": 12, "unit": "cm"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AH = 6$ cm và $BC = 13$ cm.\na) Tính tích $BH \\cdot CH$.\nb) Tìm độ dài các đoạn thẳng $BH, CH$ và các cạnh góc vuông $AB, AC$ (giả sử $BH < CH$).",
            "maxScore": 1.0,
            "solution": "a) Theo hệ thức lượng trong tam giác vuông: $BH \\cdot CH = AH^2 = 6^2 = 36$ cm$^2$.\nb) Ta có hệ:\n$\\begin{cases} BH + CH = BC = 13 \\\\ BH \\cdot CH = 36 \\end{cases}$\nTheo định lí Viète đảo, $BH$ và $CH$ là nghiệm của phương trình:\n$t^2 - 13t + 36 = 0 \\Leftrightarrow (t - 4)(t - 9) = 0$.\nVì $BH < CH$ nên $BH = 4$ cm và $CH = 9$ cm.\nTính $AB, AC$:\n$AB^2 = BH \\cdot BC = 4 \\cdot 13 = 52 \\Rightarrow AB = \\sqrt{52} = 2\\sqrt{13}$ cm.\n$AC^2 = CH \\cdot BC = 9 \\cdot 13 = 117 \\Rightarrow AC = \\sqrt{117} = 3\\sqrt{13}$ cm.",
            "rubric": [
                {"step": "Tính BH . CH = 36 cm^2", "subScore": 0.3},
                {"step": "Giải hệ tìm được BH = 4 cm, CH = 9 cm", "subScore": 0.4},
                {"step": "Tính AB = 2 căn 13 cm, AC = 3 căn 13 cm", "subScore": 0.3}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ có ba góc nhọn, đường cao $AH$. Gọi $D$ và $E$ lần lượt là hình chiếu vuông góc của $H$ trên $AB$ và $AC$.\na) Chứng minh $AD \\cdot AB = AE \\cdot AC = AH^2$.\nb) Chứng minh rằng $\\triangle ADE \\backsim \\triangle ACB$.",
            "maxScore": 1.0,
            "solution": "a) Xét tam giác vuông $ABH$ vuông tại $H$, đường cao $HD$:\n$AD \\cdot AB = AH^2$ (hệ thức lượng giữa cạnh góc vuông và hình chiếu).\nXét tam giác vuông $ACH$ vuông tại $H$, đường cao $HE$:\n$AE \\cdot AC = AH^2$ (hệ thức lượng giữa cạnh góc vuông và hình chiếu).\nTừ đó suy ra $AD \\cdot AB = AE \\cdot AC = AH^2$ (đpcm).\nb) Từ $AD \\cdot AB = AE \\cdot AC$, ta có tỉ lệ thức:\n$\\frac{AD}{AC} = \\frac{AE}{AB}$.\nXét hai tam giác $ADE$ và $ACB$ có:\n- Góc $\\widehat{A}$ chung;\n- $\\frac{AD}{AC} = \\frac{AE}{AB}$ (chứng minh trên).\nDo đó $\\triangle ADE \\backsim \\triangle ACB$ (c-g-c) (đpcm).",
            "rubric": [
                {"step": "Áp dụng hệ thức lượng chứng minh AD.AB = AE.AC = AH^2", "subScore": 0.5},
                {"step": "Lập tỉ số cạnh và chứng minh hai tam giác ADE và ACB đồng dạng", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một người đứng tại điểm $A$ trên bờ biển muốn đo khoảng cách đến chiếc thuyền đang neo tại điểm $C$ trên biển. Người đó tiến hành như sau: đi dọc bờ biển thẳng một đoạn $AB = 80$ m, tại $A$ đo được $\\widehat{CAB} = 70^\\circ$ và tại $B$ đo được $\\widehat{CBA} = 65^\\circ$. Hãy tính khoảng cách từ $A$ đến chiếc thuyền $C$ (làm tròn đến hàng phần mười mét).",
            "maxScore": 1.0,
            "solution": "Xét tam giác $ABC$ có:\n$\\widehat{ACB} = 180^\\circ - (\\widehat{CAB} + \\widehat{CBA}) = 180^\\circ - (70^\\circ + 65^\\circ) = 45^\\circ$.\nÁp dụng định lí sin trong tam giác $ABC$:\n$\\frac{AC}{\\sin \\widehat{B}} = \\frac{AB}{\\sin \\widehat{C}} \\Rightarrow AC = \\frac{AB \\cdot \\sin B}{\\sin C}$.\nThay các giá trị vào:\n$AC = \\frac{80 \\cdot \\sin 65^\\circ}{\\sin 45^\\circ}$.\nTa có $\\sin 65^\\circ \\approx 0{,}9063$ và $\\sin 45^\\circ = \\frac{\\sqrt{2}}{2} \\approx 0{,}7071$.\n$AC \\approx \\frac{80 \\cdot 0{,}9063}{0{,}7071} = \\frac{72{,}504}{0{,}7071} \\approx 102{,}5$ m.\nVậy khoảng cách từ vị trí $A$ đến chiếc thuyền $C$ xấp xỉ $102{,}5$ mét.",
            "rubric": [
                {"step": "Tính góc C = 45 độ", "subScore": 0.4},
                {"step": "Áp dụng định lí sin tính khoảng cách AC xấp xỉ 102,5 m", "subScore": 0.6}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c4_9_bai3_test3"] = {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương IV: Hệ thức lượng trong tam giác vuông - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $\\frac{AB}{AC} = \\frac{3}{4}$ và $BC = 25$ cm. Chiều cao $AH$ có độ dài là:", "options": ["$12$ cm", "$15$ cm", "$20$ cm", "$10$ cm"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho góc nhọn $\\alpha$. Biểu thức $T = (\\tan \\alpha + \\cot \\alpha)^2 - (\\tan \\alpha - \\cot \\alpha)^2$ có giá trị bằng:", "options": ["$4$", "$2$", "$1$", "$0$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho tam giác vuông $ABC$ tại $A$, đường cao $AH$. Khẳng định nào sau đây là SAI?", "options": ["$\\frac{1}{AH} = \\frac{1}{AB} + \\frac{1}{AC}$", "$\\frac{1}{AH^2} = \\frac{1}{AB^2} + \\frac{1}{AC^2}$", "$AH \\cdot BC = AB \\cdot AC$", "$AH^2 = BH \\cdot CH$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông cân tại $A$. Gọi $M$ là trung điểm của $AC$. Giá trị của $\\tan \\widehat{ABM}$ bằng:", "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$\\frac{1}{3}$", "$1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có $AB = 5$ cm, $AC = 7$ cm và $\\widehat{A} = 60^\\circ$. Độ dài cạnh $BC$ bằng:", "options": ["$\\sqrt{39}$ cm", "$\\sqrt{74}$ cm", "$6$ cm", "$2\\sqrt{10}$ cm"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\tan \\alpha + \\cot \\alpha = 4$. Giá trị của $\\sin 2\\alpha$ là:", "options": ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$1$", "$\\frac{3}{4}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 1$ cm, $CH = 4$ cm. Diện tích của tam giác $ABC$ là:", "options": ["$5$ cm$^2$", "$10$ cm$^2$", "$4$ cm$^2$", "$2$ cm$^2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho hình thang vuông $ABCD$ ($\\widehat{A} = \\widehat{D} = 90^\\circ$) ngoại tiếp đường tròn bán kính $R = 3$ cm. Biết cạnh đáy lớn $CD = 8$ cm. Diện tích hình thang $ABCD$ bằng:", "options": ["$42$ cm$^2$", "$48$ cm$^2$", "$36$ cm$^2$", "$54$ cm$^2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ nhọn có ba đường cao $AD, BE, CF$ đồng quy tại trực tâm $H$. Tỉ số $\\frac{HD}{AD} + \\frac{HE}{BE} + \\frac{HF}{CF}$ luôn bằng:", "options": ["$1$", "$2$", "$\\frac{3}{2}$", "$\\frac{1}{2}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ vuông tại $A$. Gọi $D$ là điểm trên cạnh huyền $BC$. Đẳng thức nào sau đây luôn thỏa mãn?", "options": ["$AD^2 \\cdot BC = AB^2 \\cdot CD + AC^2 \\cdot BD - BC \\cdot BD \\cdot CD$ (Định lí Stewart)", "$AD^2 = AB \\cdot AC$", "$AD = \\frac{AB + AC}{2}$", "$AD^2 = BD \\cdot CD$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho góc nhọn $\\alpha$. Giá trị nhỏ nhất của biểu thức $F = \\frac{1}{1 + \\sin \\alpha} + \\frac{1}{1 - \\sin \\alpha}$ là:", "options": ["$2$ (đạt khi $\\alpha \\to 0^+$)", "$1$", "$4$", "Không có GTNN"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Gọi $D, E$ lần lượt là hình chiếu của $H$ trên $AB, AC$. Hệ thức nào sau đây là đúng?", "options": ["$DE^3 = BC \\cdot BD \\cdot CE$", "$DE^2 = BD \\cdot CE$", "$DE = BD + CE$", "$DE^2 = BC \\cdot AH$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Gọi $D$ và $E$ lần lượt là hình chiếu của $H$ trên $AB$ và $AC$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tứ giác $ADHE$ là hình chữ nhật và $DE = AH$.", "isCorrect": True, "explanation": "Tứ giác có 3 góc vuông $\\widehat{A} = \\widehat{D} = \\widehat{E} = 90^\\circ$ nên là hình chữ nhật $\\Rightarrow DE = AH$."},
                {"id": "b", "statement": "Tam giác $ADE$ đồng dạng với tam giác $ABC$.", "isCorrect": True, "explanation": "$\\widehat{ADE} = \\widehat{AHE} = \\widehat{C} \\Rightarrow \\triangle ADE \\backsim \\triangle ACB$."},
                {"id": "c", "statement": "$BD \\cdot CE \\cdot BC = AH^3$.", "isCorrect": True, "explanation": "$BD = \\frac{BH^2}{AB}, CE = \\frac{CH^2}{AC} \\Rightarrow BD \\cdot CE = \\frac{BH^2 CH^2}{AB \\cdot AC} = \\frac{AH^4}{BC \\cdot AH} = \\frac{AH^3}{BC} \\Rightarrow BD \\cdot CE \\cdot BC = AH^3$."},
                {"id": "d", "statement": "$\\frac{BD}{CE} = \\frac{AB^2}{AC^2}$.", "isCorrect": False, "explanation": "Ta có $\\frac{BD}{CE} = \\frac{AB^3}{AC^3}$ chứ không phải bình phương."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác nhọn $ABC$ có ba đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$H$ là tâm đường tròn nội tiếp tam giác $DEF$ (tam giác trực phân).", "isCorrect": True, "explanation": "Các đường cao $AD, BE, CF$ chính là các đường phân giác trong của tam giác $DEF$."},
                {"id": "b", "statement": "$DH \\cdot DA = DB \\cdot DC$.", "isCorrect": True, "explanation": "$\\triangle HDB \\backsim \\triangle CDA \\Rightarrow \\frac{DH}{DC} = \\frac{DB}{DA} \\Rightarrow DH \\cdot DA = DB \\cdot DC$."},
                {"id": "c", "statement": "$\\cos^2 A + \\cos^2 B + \\cos^2 C < 1$.", "isCorrect": False, "explanation": "Với tam giác nhọn, $\\cos^2 A + \\cos^2 B + \\cos^2 C = 1 - 2\\cos A \\cos B \\cos C < 1$ là mệnh đề ĐÚNG, nhưng nếu nói luôn nhỏ hơn 1 thì đúng, tuy nhiên xét câu hỏi đẳng thức $\\cos^2 A + \\cos^2 B + \\cos^2 C + 2\\cos A\\cos B\\cos C = 1$."},
                {"id": "d", "statement": "Diện tích tam giác $DEF$ bằng $(1 - \\cos^2 A - \\cos^2 B - \\cos^2 C) S_{ABC}$.", "isCorrect": False, "explanation": "$S_{DEF} = (1 - \\cos^2 A - \\cos^2 B - \\cos^2 C) S_{ABC}$ không đúng hệ số chuẩn ($S_{AEF} = S_{ABC}\\cos^2 A \\Rightarrow S_{DEF} = S(1 - \\cos^2 A - \\cos^2 B - \\cos^2 C)$ chỉ đúng khi $A,B,C$ rời rạc)."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Cho tam giác vuông $ABC$ tại $A$, đường cao $AH$. Biết $AB = 6$ cm, $AC = 8$ cm. Gọi $M$ là trung điểm của $BC$. Tính độ dài đoạn $AM$ theo cm.", "answer": 5, "unit": "cm"},
        {"id": 2, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Gọi $D, E$ lần lượt là hình chiếu của $H$ trên $AB, AC$. Biết $BD = 2$ cm, $CE = 16$ cm. Tính độ dài cạnh huyền $BC$ theo cm.", "answer": 20, "unit": "cm"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\sin \\alpha \\cdot \\cos \\alpha = \\frac{2}{5}$. Tính giá trị của biểu thức $P = \\sin^4 \\alpha + \\cos^4 \\alpha$.", "answer": 0.68, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ vuông tại $A$ có phân giác $AD = 6\\sqrt{2}$ cm và $\\frac{AB}{AC} = \\frac{3}{4}$. Tính diện tích tam giác $ABC$ theo cm$^2$.", "answer": 150, "unit": "cm$^2$"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Kẻ $HD \\perp AB$ tại $D$ và $HE \\perp AC$ tại $E$.\na) Chứng minh rằng $AH^3 = BC \\cdot BD \\cdot CE$.\nb) Chứng minh rằng $DE^3 = BC \\cdot BD \\cdot CE$.\nc) Chứng minh $\\sqrt[3]{BD^2} + \\sqrt[3]{CE^2} = \\sqrt[3]{BC^2}$.",
            "maxScore": 1.0,
            "solution": "a) Trong tam giác vuông $ABH$ vuông tại $H$, đường cao $HD$:\n$BD = \\frac{BH^2}{AB}$.\nTrong tam giác vuông $ACH$ vuông tại $H$, đường cao $HE$:\n$CE = \\frac{CH^2}{AC}$.\nNhân hai đẳng thức lại:\n$BD \\cdot CE = \\frac{BH^2 \\cdot CH^2}{AB \\cdot AC} = \\frac{(BH \\cdot CH)^2}{AB \\cdot AC} = \\frac{(AH^2)^2}{BC \\cdot AH} = \\frac{AH^4}{BC \\cdot AH} = \\frac{AH^3}{BC}$.\nSuy ra: $AH^3 = BC \\cdot BD \\cdot CE$ (đpcm).\nb) Vì tứ giác $ADHE$ có 3 góc vuông $\\widehat{A} = \\widehat{D} = \\widehat{E} = 90^\\circ$ nên $ADHE$ là hình chữ nhật.\nSuy ra $DE = AH$.\nThay $AH = DE$ vào kết quả câu a, ta được: $DE^3 = BC \\cdot BD \\cdot CE$ (đpcm).\nc) Ta có:\n$BD = \\frac{BH^2}{AB} = \\frac{(AB^2/BC)^2}{AB} = \\frac{AB^3}{BC^2} \\Rightarrow \\sqrt[3]{BD} = \\frac{AB}{\\sqrt[3]{BC^2}} \\Rightarrow \\sqrt[3]{BD^2} = \\frac{AB^2}{\\sqrt[3]{BC^4}}$.\nTương tự: $CE = \\frac{AC^3}{BC^2} \\Rightarrow \\sqrt[3]{CE^2} = \\frac{AC^2}{\\sqrt[3]{BC^4}}$.\nCộng hai vế lại:\n$\\sqrt[3]{BD^2} + \\sqrt[3]{CE^2} = \\frac{AB^2 + AC^2}{\\sqrt[3]{BC^4}} = \\frac{BC^2}{\\sqrt[3]{BC^4}} = \\frac{BC^2}{BC^{4/3}} = BC^{2/3} = \\sqrt[3]{BC^2}$ (đpcm).",
            "rubric": [
                {"step": "Chứng minh AH^3 = BC . BD . CE", "subScore": 0.4},
                {"step": "Chứng minh DE = AH và suy ra DE^3 = BC . BD . CE", "subScore": 0.3},
                {"step": "Biểu diễn BD, CE theo AB, AC, BC và suy ra hệ thức căn bậc ba", "subScore": 0.3}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ có ba góc nhọn, đường cao $AH$, $M$ là trung điểm của $BC$. Kẻ $BK \\perp AC$ tại $K$, $CL \\perp AB$ tại $L$. Gọi $S$ là diện tích tam giác $ABC$.\nChứng minh rằng: $S_{AKL} = S \\cdot \\cos^2 A$.",
            "maxScore": 1.0,
            "solution": "Xét hai tam giác vuông $ABK$ và $ACL$ có:\n$\\cos A = \\frac{AK}{AB}$ (trong tam giác vuông $ABK$ tại $K$).\n$\\cos A = \\frac{AL}{AC}$ (trong tam giác vuông $ACL$ tại $L$).\nDo đó: $\\frac{AK}{AB} = \\frac{AL}{AC} = \\cos A$.\nXét hai tam giác $AKL$ và $ABC$ có:\n- Góc $\\widehat{A}$ chung;\n- $\\frac{AK}{AC} = \\frac{AL}{AB}$ (suy từ tỉ lệ trên).\nDo đó $\\triangle AKL \\backsim \\triangle ABC$ (c-g-c) theo tỉ số đồng dạng $k = \\frac{AK}{AC} = \\frac{AK}{AB} \\cdot \\frac{AB}{AC} = \\cos A$.\nTỉ số diện tích của hai tam giác đồng dạng bằng bình phương tỉ số đồng dạng:\n$\\frac{S_{AKL}}{S_{ABC}} = k^2 = \\cos^2 A$.\nSuy ra $S_{AKL} = S_{ABC} \\cdot \\cos^2 A = S \\cdot \\cos^2 A$ (đpcm).",
            "rubric": [
                {"step": "Thiết lập tỉ lệ AK/AB = AL/AC = cos A", "subScore": 0.5},
                {"step": "Chứng minh hai tam giác đồng dạng với tỉ số k = cos A và kết luận diện tích", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một người đứng tại bờ biển $A$ muốn đến một địa điểm $C$ trên một hòn đảo. Khoảng cách từ $C$ đến bờ biển (đoạn vuông góc $CH$) là $6$ km, và khoảng cách từ $A$ đến chân đường vuông góc $H$ là $10$ km. Người đó đi bộ dọc theo bờ biển từ $A$ đến một điểm $P$ giữa $A$ và $H$ với vận tốc $5$ km/h, sau đó chèo thuyền từ $P$ đến hòn đảo $C$ với vận tốc $3$ km/h.\nHỏi điểm $P$ phải cách $H$ bao nhiêu kilômét để tổng thời gian di chuyển từ $A$ đến $C$ là ngắn nhất? Tính thời gian ngắn nhất đó.",
            "maxScore": 1.0,
            "solution": "Đặt $PH = x$ (km) với $0 \\le x \\le 10$.\nKhi đó đoạn đi bộ $AP = AH - PH = 10 - x$ (km).\nĐoạn chèo thuyền $PC$ trong tam giác vuông $PHC$ có độ dài:\n$PC = \\sqrt{PH^2 + CH^2} = \\sqrt{x^2 + 6^2} = \\sqrt{x^2 + 36}$ (km).\nTổng thời gian di chuyển là:\n$T(x) = \\frac{AP}{5} + \\frac{PC}{3} = \\frac{10 - x}{5} + \\frac{\\sqrt{x^2 + 36}}{3} = 2 - \\frac{x}{5} + \\frac{\\sqrt{x^2 + 36}}{3}$.\nĐể tìm $x$ làm $T(x)$ nhỏ nhất, ta xét đạo hàm (hoặc bất đẳng thức hình học):\n$T'(x) = -\\frac{1}{5} + \\frac{x}{3\\sqrt{x^2 + 36}}$.\nCho $T'(x) = 0 \\Leftrightarrow \\frac{x}{3\\sqrt{x^2 + 36}} = \\frac{1}{5} \\Leftrightarrow 5x = 3\\sqrt{x^2 + 36}$.\nBình phương hai vế:\n$25x^2 = 9(x^2 + 36) = 9x^2 + 324 \\Leftrightarrow 16x^2 = 324 \\Leftrightarrow x^2 = \\frac{324}{16} = \\frac{81}{4}$.\nDo $x > 0$ nên $x = \\frac{9}{2} = 4{,}5$ km (thỏa mãn $0 \\le x \\le 10$).\nThời gian ngắn nhất là:\n$T(4{,}5) = 2 - \\frac{4{,}5}{5} + \\frac{\\sqrt{4{,}5^2 + 36}}{3} = 2 - 0{,}9 + \\frac{\\sqrt{20{,}25 + 36}}{3} = 1{,}1 + \\frac{\\sqrt{56{,}25}}{3} = 1{,}1 + \\frac{7{,}5}{3} = 1{,}1 + 2{,}5 = 3{,}6$ giờ (tức $3$ giờ $36$ phút).\nVậy điểm $P$ phải cách $H$ một khoảng $4{,}5$ km và thời gian ngắn nhất là $3{,}6$ giờ.",
            "rubric": [
                {"step": "Thiết lập hàm thời gian T(x) theo ẩn x = PH", "subScore": 0.4},
                {"step": "Giải phương trình đạo hàm tìm nghiệm x = 4,5 km", "subScore": 0.4},
                {"step": "Tính thời gian nhỏ nhất T = 3,6 giờ và kết luận", "subScore": 0.2}
            ]
        }
    ]
}
