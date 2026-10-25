# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 9 - CHƯƠNG IV (PHẦN 1)
Bao gồm:
- Bài 11: Tỉ số lượng giác của góc nhọn (3 đề: Cơ bản, Khá, Nâng cao)
- Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng (3 đề: Cơ bản, Khá, Nâng cao)
Chuẩn ma trận Bộ GD&ĐT 2025: 12 TN + 2 Đ/S (8 ý) + 4 TLN + 3 TL. Tổng 10.0 điểm.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

EXAMS_PART1 = {}

# =====================================================================
# BÀI 11: TỈ SỐ LƯỢNG GIÁC CỦA GÓC NHỌN
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c4_9_bai1_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 11: Tỉ số lượng giác của góc nhọn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$. Tỉ số $\\sin B$ bằng:", "options": ["$\\frac{AC}{BC}$", "$\\frac{AB}{BC}$", "$\\frac{AC}{AB}$", "$\\frac{AB}{AC}$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$. Tỉ số $\\cos B$ bằng:", "options": ["$\\frac{AB}{BC}$", "$\\frac{AC}{BC}$", "$\\frac{AC}{AB}$", "$\\frac{BC}{AB}$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$. Tỉ số $\\tan B$ bằng:", "options": ["$\\frac{AC}{AB}$", "$\\frac{AB}{AC}$", "$\\frac{AC}{BC}$", "$\\frac{AB}{BC}$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$. Tỉ số $\\cot B$ bằng:", "options": ["$\\frac{AB}{AC}$", "$\\frac{AC}{AB}$", "$\\frac{BC}{AC}$", "$\\frac{BC}{AB}$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Giá trị của $\\sin 30^\\circ$ bằng:", "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$1$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Giá trị của $\\cos 45^\\circ$ bằng:", "options": ["$\\frac{\\sqrt{2}}{2}$", "$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$1$"], "correct": 0},
        {"id": 7, "level": "Nhận biết", "question": "Giá trị của $\\tan 45^\\circ$ bằng:", "options": ["$1$", "$\\sqrt{3}$", "$\\frac{\\sqrt{3}}{3}$", "$0$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho hai góc $\\alpha$ và $\\beta$ phụ nhau ($\\alpha + \\beta = 90^\\circ$). Khẳng định nào sau đây là SAI?", "options": ["$\\sin \\alpha = \\cos \\beta$", "$\\tan \\alpha = \\cot \\beta$", "$\\cos \\alpha = \\sin \\beta$", "$\\sin \\alpha = \\tan \\beta$"], "correct": 3},
        {"id": 9, "level": "Thông hiểu", "question": "Cho góc nhọn $\\alpha$. Hệ thức nào sau đây luôn đúng?", "options": ["$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$", "$\\sin^2 \\alpha - \\cos^2 \\alpha = 1$", "$\\tan \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$", "$\\tan \\alpha \\cdot \\cot \\alpha = -1$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$ cm, $AC = 4$ cm. Độ dài cạnh huyền $BC$ và giá trị $\\sin B$ là:", "options": ["$BC = 5$ cm, $\\sin B = \\frac{4}{5}$", "$BC = 5$ cm, $\\sin B = \\frac{3}{5}$", "$BC = 7$ cm, $\\sin B = \\frac{4}{7}$", "$BC = 5$ cm, $\\sin B = \\frac{3}{4}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Cho góc nhọn $\\alpha$ có $\\tan \\alpha = \\frac{3}{4}$. Khi đó $\\cot \\alpha$ bằng:", "options": ["$\\frac{4}{3}$", "$\\frac{3}{4}$", "$\\frac{3}{5}$", "$\\frac{4}{5}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Giá trị của biểu thức $P = \\sin^2 25^\\circ + \\sin^2 65^\\circ$ là:", "options": ["$1$", "$0$", "$2$", "$\\frac{1}{2}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $MNP$ vuông tại $M$ có $MN = 6$ cm, $MP = 8$ cm. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Độ dài cạnh huyền $NP$ bằng $10$ cm.", "isCorrect": True, "explanation": "$NP = \\sqrt{MN^2 + MP^2} = \\sqrt{6^2 + 8^2} = 10$ cm."},
                {"id": "b", "statement": "$\\sin N = \\frac{MP}{NP} = \\frac{8}{10} = 0{,}8$.", "isCorrect": True, "explanation": "$\\sin N = \\text{đối}/\\text{huyền} = 8/10 = 0{,}8$."},
                {"id": "c", "statement": "$\\cos N = \\frac{MN}{NP} = 0{,}6$.", "isCorrect": True, "explanation": "$\\cos N = 6/10 = 0{,}6$."},
                {"id": "d", "statement": "$\\tan N = \\frac{MN}{MP} = 0{,}75$.", "isCorrect": False, "explanation": "$\\tan N = MP / MN = 8/6 = 4/3 \\approx 1{,}33$ chứ không phải $MN/MP$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho góc nhọn $\\alpha$. Xét tính đúng/sai của các khẳng định sau:",
            "statements": [
                {"id": "a", "statement": "$0 < \\sin \\alpha < 1$ và $0 < \\cos \\alpha < 1$.", "isCorrect": True, "explanation": "Với góc nhọn $\\alpha$, các tỉ số $\\sin$ và $\\cos$ luôn nằm trong $(0; 1)$."},
                {"id": "b", "statement": "$\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha}$.", "isCorrect": True, "explanation": "Đây là công thức định nghĩa của tang."},
                {"id": "c", "statement": "Nếu $\\alpha = 60^\\circ$ thì $\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$ và $\\cos 60^\\circ = \\frac{1}{2}$.", "isCorrect": True, "explanation": "Giá trị lượng giác của các góc đặc biệt."},
                {"id": "d", "statement": "$\\tan 30^\\circ \\cdot \\cot 60^\\circ = 1$.", "isCorrect": False, "explanation": "$\\tan 30^\\circ = \\frac{\\sqrt{3}}{3}$, $\\cot 60^\\circ = \\frac{\\sqrt{3}}{3} \\Rightarrow$ tích bằng $1/3 \\neq 1$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính giá trị của biểu thức $A = \\sin 30^\\circ + \\cos 60^\\circ$.", "answer": 1, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5$ cm, $BC = 13$ cm. Tính $\\tan B$ (kết quả viết dưới dạng phân số tối giản $a/b$, ví dụ 12/5).", "answer": "12/5", "unit": ""},
        {"id": 3, "level": "Thông hiểu", "question": "Cho góc nhọn $\\alpha$ biết $\\sin \\alpha = 0{,}6$. Tính giá trị của $\\cos \\alpha$.", "answer": 0.8, "unit": ""},
        {"id": 4, "level": "Vận dụng", "question": "Tính giá trị biểu thức: $M = \\sin^2 35^\\circ + \\sin^2 55^\\circ + \\tan 20^\\circ \\cdot \\tan 70^\\circ$.", "answer": 2, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 9$ cm, $AC = 12$ cm.\na) Tính độ dài cạnh $BC$.\nb) Tính các tỉ số lượng giác $\\sin B, \\cos B, \\tan B, \\cot B$.",
            "maxScore": 1.0,
            "solution": "a) Áp dụng định lí Pythagore trong tam giác vuông $ABC$:\n$BC = \\sqrt{AB^2 + AC^2} = \\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15$ cm.\nb) Các tỉ số lượng giác của góc $B$:\n$\\sin B = \\frac{AC}{BC} = \\frac{12}{15} = \\frac{4}{5} = 0{,}8$.\n$\\cos B = \\frac{AB}{BC} = \\frac{9}{15} = \\frac{3}{5} = 0{,}6$.\n$\\tan B = \\frac{AC}{AB} = \\frac{12}{9} = \\frac{4}{3}$.\n$\\cot B = \\frac{AB}{AC} = \\frac{9}{12} = \\frac{3}{4}$.",
            "rubric": [
                {"step": "Tính đúng BC = 15 cm", "subScore": 0.4},
                {"step": "Tính đúng sin B, cos B, tan B, cot B", "subScore": 0.6}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Không dùng máy tính cầm tay, hãy tính giá trị biểu thức:\n$B = \\cos^2 15^\\circ + \\cos^2 25^\\circ + \\cos^2 35^\\circ + \\cos^2 55^\\circ + \\cos^2 65^\\circ + \\cos^2 75^\\circ$.",
            "maxScore": 1.0,
            "solution": "Vì các cặp góc phụ nhau có $\\cos(90^\\circ - \\alpha) = \\sin \\alpha$, ta có:\n$\\cos 75^\\circ = \\sin 15^\\circ \\Rightarrow \\cos^2 15^\\circ + \\cos^2 75^\\circ = \\cos^2 15^\\circ + \\sin^2 15^\\circ = 1$.\n$\\cos 65^\\circ = \\sin 25^\\circ \\Rightarrow \\cos^2 25^\\circ + \\cos^2 65^\\circ = \\cos^2 25^\\circ + \\sin^2 25^\\circ = 1$.\n$\\cos 55^\\circ = \\sin 35^\\circ \\Rightarrow \\cos^2 35^\\circ + \\cos^2 55^\\circ = \\cos^2 35^\\circ + \\sin^2 35^\\circ = 1$.\nDo đó: $B = 1 + 1 + 1 = 3$.",
            "rubric": [
                {"step": "Áp dụng tỉ số lượng giác của hai góc phụ nhau ghép cặp", "subScore": 0.5},
                {"step": "Áp dụng công thức sin^2 + cos^2 = 1 tính ra kết quả B = 3", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\tan \\alpha = 2$. Tính giá trị của biểu thức $P = \\frac{2\\sin \\alpha + 3\\cos \\alpha}{4\\sin \\alpha - 5\\cos \\alpha}$.",
            "maxScore": 1.0,
            "solution": "Vì $\\tan \\alpha = 2$ nên $\\cos \\alpha \\neq 0$.\nChia cả tử và mẫu của biểu thức $P$ cho $\\cos \\alpha$, ta được:\n$P = \\frac{2\\frac{\\sin \\alpha}{\\cos \\alpha} + 3}{4\\frac{\\sin \\alpha}{\\cos \\alpha} - 5} = \\frac{2\\tan \\alpha + 3}{4\\tan \\alpha - 5}$.\nThay $\\tan \\alpha = 2$ vào:\n$P = \\frac{2(2) + 3}{4(2) - 5} = \\frac{4 + 3}{8 - 5} = \\frac{7}{3}$.\nVậy $P = \\frac{7}{3}$.",
            "rubric": [
                {"step": "Chia cả tử và mẫu cho cos alpha để đưa về tan alpha", "subScore": 0.5},
                {"step": "Thay số và tính đúng kết quả P = 7/3", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c4_9_bai1_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 11: Tỉ số lượng giác của góc nhọn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hệ thức nào sau đây diễn tả đúng mối liên hệ giữa $\\tan \\alpha$ và $\\cot \\alpha$ ($0^\\circ < \\alpha < 90^\\circ$)?", "options": ["$\\tan \\alpha \\cdot \\cot \\alpha = 1$", "$\\tan \\alpha + \\cot \\alpha = 1$", "$\\tan \\alpha = -\\cot \\alpha$", "$\\tan^2 \\alpha + \\cot^2 \\alpha = 1$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hệ thức nào sau đây liên hệ giữa $\\tan \\alpha$ và $\\cos \\alpha$ ($0^\\circ < \\alpha < 90^\\circ$)?", "options": ["$1 + \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$", "$1 + \\tan^2 \\alpha = \\cos^2 \\alpha$", "$1 - \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$", "$\\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Khi góc nhọn $\\alpha$ tăng từ $0^\\circ$ đến $90^\\circ$ thì:", "options": ["$\\sin \\alpha$ tăng, $\\cos \\alpha$ giảm", "$\\sin \\alpha$ giảm, $\\cos \\alpha$ tăng", "Cả $\\sin \\alpha$ và $\\cos \\alpha$ đều tăng", "Cả $\\sin \\alpha$ và $\\cos \\alpha$ đều giảm"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Khi góc nhọn $\\alpha$ tăng từ $0^\\circ$ đến $90^\\circ$ thì:", "options": ["$\\tan \\alpha$ tăng, $\\cot \\alpha$ giảm", "$\\tan \\alpha$ giảm, $\\cot \\alpha$ tăng", "Cả $\\tan \\alpha$ và $\\cot \\alpha$ đều tăng", "Cả $\\tan \\alpha$ và $\\cot \\alpha$ đều giảm"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6$ cm, $BC = 10$ cm. Giá trị của $\\cot C$ là:", "options": ["$\\frac{4}{3}$", "$\\frac{3}{4}$", "$\\frac{3}{5}$", "$\\frac{4}{5}$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho góc nhọn $\\alpha$ có $\\cos \\alpha = \\frac{5}{13}$. Giá trị của $\\sin \\alpha$ là:", "options": ["$\\frac{12}{13}$", "$\\frac{13}{12}$", "$\\frac{8}{13}$", "$\\frac{11}{13}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Giá trị của biểu thức $H = \\tan 25^\\circ \\cdot \\tan 65^\\circ - \\frac{\\sin 40^\\circ}{\\cos 50^\\circ}$ bằng:", "options": ["$0$", "$1$", "$-1$", "$2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có $\\widehat{B} = 60^\\circ, \\widehat{C} = 45^\\circ$, kẻ đường cao $AH = 6$ cm. Độ dài cạnh $AB$ bằng:", "options": ["$4\\sqrt{3}$ cm", "$6\\sqrt{3}$ cm", "$12$ cm", "$3\\sqrt{3}$ cm"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho $\\tan \\alpha = 3$. Giá trị của biểu thức $\\sin^2 \\alpha$ là:", "options": ["$\\frac{9}{10}$", "$\\frac{1}{10}$", "$\\frac{3}{10}$", "$\\frac{3}{\\sqrt{10}}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\sin \\alpha + \\cos \\alpha = \\frac{7}{5}$. Giá trị của tích $\\sin \\alpha \\cdot \\cos \\alpha$ là:", "options": ["$\\frac{12}{25}$", "$\\frac{24}{25}$", "$\\frac{6}{25}$", "$\\frac{49}{25}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 4$ cm, $CH = 9$ cm. Tỉ số $\\tan B$ bằng:", "options": ["$\\frac{3}{2}$", "$\\frac{2}{3}$", "$\\frac{4}{9}$", "$\\frac{9}{4}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ nhọn. Khẳng định nào sau đây là đúng về diện tích tam giác $ABC$?", "options": ["$S = \\frac{1}{2} AB \\cdot AC \\cdot \\sin A$", "$S = \\frac{1}{2} AB \\cdot AC \\cdot \\cos A$", "$S = AB \\cdot AC \\cdot \\sin A$", "$S = \\frac{1}{2} AB \\cdot AC \\cdot \\tan A$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có góc $B = 30^\\circ$ và cạnh huyền $BC = 12$ cm. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Góc $C$ có số đo là $60^\\circ$.", "isCorrect": True, "explanation": "$\\widehat{C} = 90^\\circ - 30^\\circ = 60^\\circ$."},
                {"id": "b", "statement": "Cạnh đối diện góc $30^\\circ$ là $AC = BC \\cdot \\sin 30^\\circ = 6$ cm.", "isCorrect": True, "explanation": "$AC = 12 \\cdot (1/2) = 6$ cm."},
                {"id": "c", "statement": "Cạnh $AB = BC \\cdot \\cos 30^\\circ = 6\\sqrt{3}$ cm.", "isCorrect": True, "explanation": "$AB = 12 \\cdot \\frac{\\sqrt{3}}{2} = 6\\sqrt{3}$ cm."},
                {"id": "d", "statement": "Đường cao $AH$ ứng với cạnh huyền có độ dài bằng $6$ cm.", "isCorrect": False, "explanation": "$AH = \\frac{AB \\cdot AC}{BC} = \\frac{6\\sqrt{3} \\cdot 6}{12} = 3\\sqrt{3} \\approx 5{,}2$ cm, không phải $6$ cm."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\tan \\alpha = \\frac{1}{2}$. Xét tính đúng/sai của các phát biểu sau:",
            "statements": [
                {"id": "a", "statement": "$\\cot \\alpha = 2$.", "isCorrect": True, "explanation": "$\\cot \\alpha = 1 / \\tan \\alpha = 2$."},
                {"id": "b", "statement": "$\\cos^2 \\alpha = \\frac{4}{5}$.", "isCorrect": True, "explanation": "$\\frac{1}{\\cos^2 \\alpha} = 1 + \\tan^2 \\alpha = 1 + 1/4 = 5/4 \\Rightarrow \\cos^2 \\alpha = 4/5$."},
                {"id": "c", "statement": "$\\sin^2 \\alpha = \\frac{1}{5}$.", "isCorrect": True, "explanation": "$\\sin^2 \\alpha = 1 - \\cos^2 \\alpha = 1/5$."},
                {"id": "d", "statement": "Giá trị của biểu thức $\\sin \\alpha \\cdot \\cos \\alpha = \\frac{3}{5}$.", "isCorrect": False, "explanation": "$\\sin \\alpha \\cos \\alpha = \\tan \\alpha \\cdot \\cos^2 \\alpha = \\frac{1}{2} \\cdot \\frac{4}{5} = \\frac{2}{5} \\neq \\frac{3}{5}$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho góc nhọn $\\alpha$ có $\\cos \\alpha = 0{,}8$. Tính $\\tan \\alpha$.", "answer": 0.75, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$, có đường cao $AH$. Biết $AB = 15$ cm và $\\sin B = 0{,}6$. Tính độ dài cạnh huyền $BC$ theo đơn vị cm.", "answer": 18.75, "unit": "cm"},
        {"id": 3, "level": "Vận dụng", "question": "Tính giá trị của biểu thức: $T = \\tan 10^\\circ \\cdot \\tan 20^\\circ \\cdot \\tan 30^\\circ \\cdot \\dots \\cdot \\tan 80^\\circ$.", "answer": 1, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho góc nhọn $\\alpha$ biết $\\sin \\alpha - \\cos \\alpha = 0{,}2$. Tính giá trị của $\\sin \\alpha \\cdot \\cos \\alpha$.", "answer": 0.48, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\sin \\alpha = \\frac{3}{5}$.\na) Tính $\\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.\nb) Tính giá trị của biểu thức $A = 5\\sin \\alpha + 10\\cos \\alpha - 4\\tan \\alpha$.",
            "maxScore": 1.0,
            "solution": "a) Vì $0^\\circ < \\alpha < 90^\\circ$ nên $\\cos \\alpha > 0$.\nTa có: $\\cos \\alpha = \\sqrt{1 - \\sin^2 \\alpha} = \\sqrt{1 - \\left(\\frac{3}{5}\\right)^2} = \\sqrt{\\frac{16}{25}} = \\frac{4}{5}$.\n$\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha} = \\frac{3/5}{4/5} = \\frac{3}{4}$.\n$\\cot \\alpha = \\frac{1}{\\tan \\alpha} = \\frac{4}{3}$.\nb) Thay các giá trị vào $A$:\n$A = 5 \\cdot \\frac{3}{5} + 10 \\cdot \\frac{4}{5} - 4 \\cdot \\frac{3}{4} = 3 + 8 - 3 = 8$.\nVậy $A = 8$.",
            "rubric": [
                {"step": "Tính đúng cos alpha = 4/5, tan alpha = 3/4, cot alpha = 4/3", "subScore": 0.6},
                {"step": "Tính đúng giá trị biểu thức A = 8", "subScore": 0.4}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Chứng minh các đẳng thức lượng giác sau (với góc nhọn $\\alpha$):\na) $\\frac{1}{\\cos^2 \\alpha} = 1 + \\tan^2 \\alpha$.\nb) $\\sin^4 \\alpha - \\cos^4 \\alpha = 2\\sin^2 \\alpha - 1$.",
            "maxScore": 1.0,
            "solution": "a) Ta có: $1 + \\tan^2 \\alpha = 1 + \\frac{\\sin^2 \\alpha}{\\cos^2 \\alpha} = \\frac{\\cos^2 \\alpha + \\sin^2 \\alpha}{\\cos^2 \\alpha}$.\nVì $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$ nên $1 + \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$ (đpcm).\nb) Vế trái $= \\sin^4 \\alpha - \\cos^4 \\alpha = (\\sin^2 \\alpha - \\cos^2 \\alpha)(\\sin^2 \\alpha + \\cos^2 \\alpha)$.\nDo $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$ nên vế trái $= \\sin^2 \\alpha - \\cos^2 \\alpha$.\nLại có $\\cos^2 \\alpha = 1 - \\sin^2 \\alpha$, nên:\nVế trái $= \\sin^2 \\alpha - (1 - \\sin^2 \\alpha) = 2\\sin^2 \\alpha - 1 = \\text{Vế phải}$ (đpcm).",
            "rubric": [
                {"step": "Chứng minh câu a đúng theo biến đổi quy đồng mẫu", "subScore": 0.5},
                {"step": "Dùng hằng đẳng thức hiệu hai bình phương và sin^2 + cos^2 = 1 chứng minh câu b", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ có ba góc nhọn, đường cao $AH$. Chứng minh rằng diện tích tam giác $ABC$ có thể tính bằng công thức:\n$S_{ABC} = \\frac{1}{2} AB \\cdot AC \\cdot \\sin A$.",
            "maxScore": 1.0,
            "solution": "Kẻ đường cao $CH$ vuông góc với $AB$ ($H \\in AB$).\nTrong tam giác vuông $AHC$ tại $H$, ta có:\n$\\sin A = \\frac{CH}{AC} \\Rightarrow CH = AC \\cdot \\sin A$.\nDiện tích tam giác $ABC$ là:\n$S_{ABC} = \\frac{1}{2} AB \\cdot CH = \\frac{1}{2} AB \\cdot (AC \\cdot \\sin A) = \\frac{1}{2} AB \\cdot AC \\cdot \\sin A$ (đpcm).",
            "rubric": [
                {"step": "Vẽ đường cao CH và thiết lập tỉ số sin A = CH/AC", "subScore": 0.5},
                {"step": "Thay CH vào công thức diện tích tam giác để kết luận", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c4_9_bai1_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 11: Tỉ số lượng giác của góc nhọn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Biểu thức $P = \\sin^6 \\alpha + \\cos^6 \\alpha + 3\\sin^2 \\alpha \\cos^2 \\alpha$ có giá trị bằng:", "options": ["$1$", "$2$", "$3$", "$0$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Biểu thức $Q = (\\sin \\alpha + \\cos \\alpha)^2 + (\\sin \\alpha - \\cos \\alpha)^2$ rút gọn được:", "options": ["$2$", "$1$", "$4\\sin \\alpha \\cos \\alpha$", "$0$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\tan \\alpha + \\cot \\alpha = 3$. Giá trị của $\\tan^2 \\alpha + \\cot^2 \\alpha$ là:", "options": ["$7$", "$9$", "$11$", "$5$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Giá trị của biểu thức $K = \\sin 10^\\circ - \\cos 80^\\circ + \\tan 25^\\circ - \\cot 65^\\circ$ là:", "options": ["$0$", "$1$", "$2$", "$-1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho tam giác $ABC$ nhọn có đường cao $AH$. Biết $AB = c, AC = b$ và góc $\\widehat{A} = 60^\\circ$. Diện tích tam giác $ABC$ là:", "options": ["$\\frac{\\sqrt{3}}{4} bc$", "$\\frac{1}{4} bc$", "$\\frac{\\sqrt{3}}{2} bc$", "$\\frac{1}{2} bc$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\sin \\alpha \\cdot \\cos \\alpha = \\frac{12}{25}$ và $\\sin \\alpha > \\cos \\alpha$. Hiệu $\\sin \\alpha - \\cos \\alpha$ bằng:", "options": ["$\\frac{1}{5}$", "$\\frac{2}{5}$", "$\\frac{7}{25}$", "$\\frac{1}{25}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Rút gọn biểu thức $A = \\sqrt{\\sin^4 \\alpha + 4\\cos^2 \\alpha} + \\sqrt{\\cos^4 \\alpha + 4\\sin^2 \\alpha}$ được:", "options": ["$3$", "$1$", "$2$", "$4$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho $\\tan \\alpha = 2$. Giá trị của biểu thức $M = \\frac{\\sin^3 \\alpha + \\cos^3 \\alpha}{\\sin \\alpha + 3\\cos \\alpha}$ là:", "options": ["$\\frac{9}{25}$", "$\\frac{7}{25}$", "$\\frac{11}{25}$", "$\\frac{1}{5}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 15^\\circ$ và $BC = 4$ cm. Diện tích của tam giác $ABC$ bằng:", "options": ["$2$ cm$^2$", "$4$ cm$^2$", "$1$ cm$^2$", "$2\\sqrt{3}$ cm$^2$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ cân tại $A$ có $\\widehat{A} = 120^\\circ$ và cạnh bên $AB = 6$ cm. Độ dài cạnh đáy $BC$ là:", "options": ["$6\\sqrt{3}$ cm", "$6$ cm", "$12$ cm", "$3\\sqrt{3}$ cm"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Giá trị nhỏ nhất của biểu thức $P = \\tan^2 \\alpha + \\cot^2 \\alpha$ ($0^\\circ < \\alpha < 90^\\circ$) là:", "options": ["$2$", "$1$", "$4$", "$\\sqrt{2}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho $x, y$ là hai góc nhọn thỏa mãn $x + y = 90^\\circ$. Giá trị nhỏ nhất của $\\frac{1}{\\sin^2 x} + \\frac{1}{\\sin^2 y}$ là:", "options": ["$4$", "$2$", "$8$", "$1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\tan \\alpha + \\cot \\alpha = m$ ($m \\ge 2$). Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$\\sin \\alpha \\cdot \\cos \\alpha = \\frac{1}{m}$.", "isCorrect": True, "explanation": "$\\tan \\alpha + \\cot \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha} + \\frac{\\cos \\alpha}{\\sin \\alpha} = \\frac{\\sin^2 \\alpha + \\cos^2 \\alpha}{\\sin \\alpha \\cos \\alpha} = \\frac{1}{\\sin \\alpha \\cos \\alpha} = m \\Rightarrow \\sin \\alpha \\cos \\alpha = 1/m$."},
                {"id": "b", "statement": "$\\tan^2 \\alpha + \\cot^2 \\alpha = m^2 - 2$.", "isCorrect": True, "explanation": "$\\tan^2 \\alpha + \\cot^2 \\alpha = (\\tan \\alpha + \\cot \\alpha)^2 - 2\\tan \\alpha \\cot \\alpha = m^2 - 2$."},
                {"id": "c", "statement": "Nếu $m = 2$ thì $\\alpha = 45^\\circ$.", "isCorrect": True, "explanation": "Khi $m = 2$, $(\\tan \\alpha - 1)^2 = 0 \\Rightarrow \\tan \\alpha = 1 \\Rightarrow \\alpha = 45^\\circ$."},
                {"id": "d", "statement": "Biểu thức $\\tan^3 \\alpha + \\cot^3 \\alpha = m^3 - 2m$.", "isCorrect": False, "explanation": "$\\tan^3 \\alpha + \\cot^3 \\alpha = (\\tan \\alpha + \\cot \\alpha)^3 - 3\\tan \\alpha \\cot \\alpha (\\tan \\alpha + \\cot \\alpha) = m^3 - 3m$ chứ không phải $m^3 - 2m$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 30^\\circ$ và cạnh $BC = 6 + 2\\sqrt{3}$ cm. Đường cao kẻ từ $A$ là $AH$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tam giác $ABH$ vuông cân tại $H$, do đó $BH = AH$.", "isCorrect": True, "explanation": "Vì $\\widehat{B} = 45^\\circ$ và tam giác $ABH$ vuông tại $H$ nên tam giác $ABH$ vuông cân $\\Rightarrow BH = AH$."},
                {"id": "b", "statement": "Trong tam giác $ACH$, $CH = AH \\cdot \\cot 30^\\circ = AH \\cdot \\sqrt{3}$.", "isCorrect": True, "explanation": "$\\cot 30^\\circ = \\sqrt{3} \\Rightarrow CH = AH\\sqrt{3}$."},
                {"id": "c", "statement": "Chiều cao $AH = 2\\sqrt{3}$ cm.", "isCorrect": True, "explanation": "$BC = BH + CH = AH(1 + \\sqrt{3}) = 6 + 2\\sqrt{3} = 2\\sqrt{3}(\\sqrt{3} + 1) \\Rightarrow AH = 2\\sqrt{3}$ cm."},
                {"id": "d", "statement": "Độ dài cạnh $AC$ bằng $4\\sqrt{3}$ cm.", "isCorrect": True, "explanation": "$AC = \\frac{AH}{\\sin 30^\\circ} = \\frac{2\\sqrt{3}}{1/2} = 4\\sqrt{3}$ cm."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\tan \\alpha + \\cot \\alpha = 2{,}5$. Tính tích $\\sin \\alpha \\cdot \\cos \\alpha$.", "answer": 0.4, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Tính giá trị của biểu thức $S = \\cos^2 1^\\circ + \\cos^2 2^\\circ + \\dots + \\cos^2 89^\\circ$.", "answer": 44.5, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho góc nhọn $\\alpha$ thỏa mãn $\\sin \\alpha + \\cos \\alpha = \\frac{\\sqrt{7}}{2}$. Tính giá trị của $|\\sin \\alpha - \\cos \\alpha|$ (viết dưới dạng số thập phân, làm tròn 0,5).", "answer": 0.5, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ vuông tại $A$ có phân giác góc $B$ cắt $AC$ tại $D$. Biết $AB = 6$ cm, $BC = 10$ cm. Tính độ dài đoạn $AD$ theo cm.", "answer": 3, "unit": "cm"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Chứng minh rằng với mọi góc nhọn $\\alpha$, biểu thức sau không phụ thuộc vào $\\alpha$:\n$E = 2(\\sin^6 \\alpha + \\cos^6 \\alpha) - 3(\\sin^4 \\alpha + \\cos^4 \\alpha)$.",
            "maxScore": 1.0,
            "solution": "Ta có các hằng đẳng thức:\n1) $\\sin^4 \\alpha + \\cos^4 \\alpha = (\\sin^2 \\alpha + \\cos^2 \\alpha)^2 - 2\\sin^2 \\alpha \\cos^2 \\alpha = 1 - 2\\sin^2 \\alpha \\cos^2 \\alpha$.\n2) $\\sin^6 \\alpha + \\cos^6 \\alpha = (\\sin^2 \\alpha + \\cos^2 \\alpha)(\\sin^4 \\alpha - \\sin^2 \\alpha \\cos^2 \\alpha + \\cos^4 \\alpha)$\n$= 1 \\cdot (1 - 2\\sin^2 \\alpha \\cos^2 \\alpha - \\sin^2 \\alpha \\cos^2 \\alpha) = 1 - 3\\sin^2 \\alpha \\cos^2 \\alpha$.\nThay vào biểu thức $E$:\n$E = 2(1 - 3\\sin^2 \\alpha \\cos^2 \\alpha) - 3(1 - 2\\sin^2 \\alpha \\cos^2 \\alpha)$\n$= 2 - 6\\sin^2 \\alpha \\cos^2 \\alpha - 3 + 6\\sin^2 \\alpha \\cos^2 \\alpha = -1$.\nVậy giá trị của $E$ luôn bằng $-1$, không phụ thuộc vào góc $\\alpha$.",
            "rubric": [
                {"step": "Biến đổi sin^4 + cos^4 và sin^6 + cos^6 theo sin^2.cos^2", "subScore": 0.6},
                {"step": "Thay vào rút gọn ra kết quả E = -1 không phụ thuộc alpha", "subScore": 0.4}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ có góc nhọn $\\widehat{A} = 2\\alpha$. Kẻ đường cao $AH$ và trung tuyến $AM$. Chứng minh công thức nhân đôi:\n$\\sin 2\\alpha = 2\\sin \\alpha \\cos \\alpha$.",
            "maxScore": 1.0,
            "solution": "Xét tam giác vuông $ABC$ có $\\widehat{A} = 90^\\circ$ không phụ hợp định nghĩa góc nhọn $2\\alpha$. Ta xét tam giác cân $OAB$ tại $O$ với bán kính $R = 1$ và góc ở đỉnh $\\widehat{AOB} = 2\\alpha$.\nKẻ đường cao $OH$ vuông góc $AB$ tại $H$. Khi đó $H$ là trung điểm của $AB$, và $OH$ cũng là phân giác nên $\\widehat{AOH} = \\alpha$.\nTrong tam giác vuông $OAH$ tại $H$:\n$AH = OA \\cdot \\sin \\alpha = 1 \\cdot \\sin \\alpha = \\sin \\alpha \\Rightarrow AB = 2AH = 2\\sin \\alpha$.\n$OH = OA \\cdot \\cos \\alpha = 1 \\cdot \\cos \\alpha = \\cos \\alpha$.\nDiện tích tam giác $OAB$ tính theo hai cách:\nCách 1: $S_{OAB} = \\frac{1}{2} OA \\cdot OB \\cdot \\sin \\widehat{AOB} = \\frac{1}{2} \\cdot 1 \\cdot 1 \\cdot \\sin 2\\alpha = \\frac{1}{2}\\sin 2\\alpha$.\nCách 2: $S_{OAB} = \\frac{1}{2} AB \\cdot OH = \\frac{1}{2} (2\\sin \\alpha) \\cdot \\cos \\alpha = \\sin \\alpha \\cos \\alpha$.\nTừ hai cách tính diện tích, ta có:\n$\\frac{1}{2}\\sin 2\\alpha = \\sin \\alpha \\cos \\alpha \\Leftrightarrow \\sin 2\\alpha = 2\\sin \\alpha \\cos \\alpha$ (đpcm).",
            "rubric": [
                {"step": "Thiết lập mô hình hình học tam giác cân với góc ở đỉnh 2alpha", "subScore": 0.4},
                {"step": "Tính diện tích theo hai cách và rút ra công thức sin 2alpha = 2 sin alpha cos alpha", "subScore": 0.6}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho góc nhọn $\\alpha$. Tìm giá trị nhỏ nhất của biểu thức:\n$P = \\frac{1}{\\sin^2 \\alpha} + \\frac{1}{\\cos^2 \\alpha} + \\frac{1}{\\sin^2 \\alpha \\cos^2 \\alpha}$.",
            "maxScore": 1.0,
            "solution": "Ta có: $\\frac{1}{\\sin^2 \\alpha} + \\frac{1}{\\cos^2 \\alpha} = \\frac{\\cos^2 \\alpha + \\sin^2 \\alpha}{\\sin^2 \\alpha \\cos^2 \\alpha} = \\frac{1}{\\sin^2 \\alpha \\cos^2 \\alpha}$.\nDo đó: $P = \\frac{2}{\\sin^2 \\alpha \\cos^2 \\alpha} = \\frac{2}{(\\sin \\alpha \\cos \\alpha)^2}$.\nÁp dụng bất đẳng thức Cô-si: $\\sin \\alpha \\cos \\alpha \\le \\frac{\\sin^2 \\alpha + \\cos^2 \\alpha}{2} = \\frac{1}{2}$.\nSuy ra: $(\\sin \\alpha \\cos \\alpha)^2 \\le \\frac{1}{4}$.\nDo đó: $P = \\frac{2}{(\\sin \\alpha \\cos \\alpha)^2} \\ge \\frac{2}{1/4} = 8$.\nDấu \"=\" xảy ra khi và chỉ khi $\\sin \\alpha = \\cos \\alpha \\Leftrightarrow \\alpha = 45^\\circ$.\nVậy giá trị nhỏ nhất của $P$ bằng $8$ khi $\\alpha = 45^\\circ$.",
            "rubric": [
                {"step": "Biến đổi P = 2 / (sin alpha cos alpha)^2", "subScore": 0.5},
                {"step": "Đánh giá bằng BĐT Cauchy và kết luận GTNN = 8 tại alpha = 45 độ", "subScore": 0.5}
            ]
        }
    ]
}

# =====================================================================
# BÀI 12: MỘT SỐ HỆ THỨC GIỮA CẠNH, GÓC TRONG TAM GIÁC VUÔNG VÀ ỨNG DỤNG
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c4_9_bai2_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 12: Một số hệ thức giữa cạnh và góc trong tam giác vuông - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$. Hệ thức nào sau đây diễn tả cạnh góc vuông theo cạnh huyền và góc nhọn?", "options": ["$b = a \\cdot \\sin B$", "$b = a \\cdot \\tan B$", "$b = a \\cdot \\cot B$", "$b = c \\cdot \\sin B$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Cho tam giác $ABC$ vuông tại $A$. Hệ thức nào sau đây diễn tả cạnh góc vuông $b$ theo cạnh góc vuông $c$?", "options": ["$b = c \\cdot \\tan B$", "$b = c \\cdot \\sin B$", "$b = c \\cdot \\cos B$", "$b = c / \\tan B$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trong tam giác vuông, mỗi cạnh góc vuông bằng cạnh huyền nhân với:", "options": ["Sin góc đối hoặc côsin góc kề", "Tang góc đối", "Côtang góc kề", "Côsin góc đối"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trong tam giác vuông, mỗi cạnh góc vuông bằng cạnh góc vuông kia nhân với:", "options": ["Tang góc đối hoặc côtang góc kề", "Sin góc đối", "Côsin góc kề", "Tang góc kề"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $BC = 10$ cm và $\\widehat{B} = 30^\\circ$. Độ dài cạnh $AC$ là:", "options": ["$5$ cm", "$5\\sqrt{3}$ cm", "$10\\sqrt{3}$ cm", "$2{,}5$ cm"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6$ cm và $\\widehat{B} = 60^\\circ$. Độ dài cạnh $AC$ là:", "options": ["$6\\sqrt{3}$ cm", "$2\\sqrt{3}$ cm", "$3$ cm", "$12$ cm"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AC = 8$ cm và $\\widehat{C} = 45^\\circ$. Độ dài cạnh $AB$ là:", "options": ["$8$ cm", "$8\\sqrt{2}$ cm", "$4\\sqrt{2}$ cm", "$4$ cm"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Một cột cờ cao $3{,}5$ m có bóng trên mặt đất dài $4{,}8$ m. Góc tạo bởi tia nắng mặt trời với mặt đất (làm tròn đến độ) xấp xỉ:", "options": ["$36^\\circ$", "$54^\\circ$", "$43^\\circ$", "$45^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Một thang dài $4$ m dựa vào tường tạo với mặt đất một góc $65^\\circ$. Chiều cao thang chạm tường (làm tròn đến hàng phần mười) là:", "options": ["$3{,}6$ m", "$1{,}7$ m", "$4{,}4$ m", "$3{,}2$ m"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Giải tam giác vuông là bài toán:", "options": ["Tìm tất cả các cạnh và các góc còn lại của tam giác vuông khi biết trước hai yếu tố (trong đó có ít nhất một cạnh)", "Tính chu vi tam giác vuông", "Tính diện tích tam giác vuông", "Vẽ hình tam giác vuông chính xác"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$ có $BC = 12$ cm và $\\widehat{B} = 35^\\circ$. Độ dài cạnh $AB$ (làm tròn đến 1 chữ số thập phân) là:", "options": ["$9{,}8$ cm", "$6{,}9$ cm", "$8{,}4$ cm", "$7{,}2$ cm"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Một máy bay bay lên với vận tốc $500$ km/h theo phương tạo với mặt đất góc $25^\\circ$. Sau $1{,}2$ phút máy bay đạt độ cao bao nhiêu km (làm tròn đến hàng phần mười)?", "options": ["$4{,}2$ km", "$9{,}1$ km", "$5{,}0$ km", "$3{,}8$ km"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có cạnh góc vuông $AB = 6$ cm và $\\widehat{B} = 30^\\circ$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Góc nhọn $\\widehat{C} = 60^\\circ$.", "isCorrect": True, "explanation": "$\\widehat{C} = 90^\\circ - 30^\\circ = 60^\\circ$."},
                {"id": "b", "statement": "Cạnh góc vuông $AC = AB \\cdot \\tan B = 6 \\cdot \\frac{\\sqrt{3}}{3} = 2\\sqrt{3}$ cm.", "isCorrect": True, "explanation": "$AC = c \\cdot \\tan B = 6 \\cdot \\tan 30^\\circ = 2\\sqrt{3}$ cm."},
                {"id": "c", "statement": "Cạnh huyền $BC = \\frac{AB}{\\cos B} = \\frac{6}{\\cos 30^\\circ} = 4\\sqrt{3}$ cm.", "isCorrect": True, "explanation": "$BC = 6 / (\\sqrt{3}/2) = 4\\sqrt{3}$ cm."},
                {"id": "d", "statement": "Diện tích tam giác $ABC$ bằng $12\\sqrt{3}$ cm$^2$.", "isCorrect": False, "explanation": "$S = \\frac{1}{2} AB \\cdot AC = \\frac{1}{2} \\cdot 6 \\cdot 2\\sqrt{3} = 6\\sqrt{3}$ cm$^2$, không phải $12\\sqrt{3}$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Một người đứng cách chân tháp $50$ m nhìn lên đỉnh tháp dưới một góc nghiêng $32^\\circ$. Mắt người cách mặt đất $1{,}6$ m. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Khoảng cách từ mắt người theo phương nằm ngang đến tháp là $50$ m.", "isCorrect": True, "explanation": "Theo đề bài, khoảng cách nằm ngang là 50 m."},
                {"id": "b", "statement": "Độ cao từ vị trí mắt đến đỉnh tháp tính theo công thức $h_1 = 50 \\cdot \\tan 32^\\circ$.", "isCorrect": True, "explanation": "Trong tam giác vuông, cạnh đối = cạnh kề nhân tang góc đối: $h_1 = 50 \\cdot \\tan 32^\\circ$."},
                {"id": "c", "statement": "Biết $\\tan 32^\\circ \\approx 0{,}6249$, độ cao $h_1 \\approx 31{,}2$ m.", "isCorrect": True, "explanation": "$50 \\cdot 0{,}6249 \\approx 31{,}25$ m."},
                {"id": "d", "statement": "Chiều cao của tháp (tính từ mặt đất) xấp xỉ bằng $31{,}2$ m.", "isCorrect": False, "explanation": "Chiều cao tháp phải cộng thêm chiều cao tầm mắt $1{,}6$ m: $h \\approx 31{,}25 + 1{,}6 = 32{,}85$ m."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $BC = 14$ cm, $\\widehat{C} = 30^\\circ$. Tính cạnh $AB$ theo cm.", "answer": 7, "unit": "cm"},
        {"id": 2, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AC = 5\\sqrt{3}$ cm và $\\widehat{B} = 60^\\circ$. Tính cạnh $AB$ theo cm.", "answer": 5, "unit": "cm"},
        {"id": 3, "level": "Vận dụng", "question": "Một cây tre bị gãy ngang thân ngọn chạm đất cách gốc $3$ m và tạo với mặt đất góc $30^\\circ$. Tính chiều cao ban đầu của cây tre theo mét (làm tròn đến số nguyên).", "answer": 5, "unit": "m"},
        {"id": 4, "level": "Vận dụng", "question": "Một khinh khí cầu đang ở độ cao $800$ m nhìn thấy một điểm trên mặt đất dưới góc hạ $37^\\circ$. Khoảng cách từ khinh khí cầu đến điểm đó theo đường chim bay là bao nhiêu mét (làm tròn đến hàng đơn vị, biết $\\sin 37^\\circ \\approx 0{,}6018$)?", "answer": 1329, "unit": "m"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Giải tam giác vuông $ABC$ tại $A$, biết $a = BC = 20$ cm và góc $\\widehat{B} = 35^\\circ$ (làm tròn độ dài đến chữ số thập phân thứ nhất).",
            "maxScore": 1.0,
            "solution": "Trong tam giác vuông $ABC$ vuông tại $A$:\n- Tính góc $\\widehat{C}$:\n$\\widehat{C} = 90^\\circ - \\widehat{B} = 90^\\circ - 35^\\circ = 55^\\circ$.\n- Tính cạnh góc vuông $b = AC$:\n$b = a \\cdot \\sin B = 20 \\cdot \\sin 35^\\circ \\approx 20 \\cdot 0{,}5736 \\approx 11{,}5$ cm.\n- Tính cạnh góc vuông $c = AB$:\n$c = a \\cdot \\cos B = 20 \\cdot \\cos 35^\\circ \\approx 20 \\cdot 0{,}8192 \\approx 16{,}4$ cm.\nKết luận: $\\widehat{C} = 55^\\circ, AC \\approx 11{,}5$ cm, $AB \\approx 16{,}4$ cm.",
            "rubric": [
                {"step": "Tính đúng góc C = 55 độ", "subScore": 0.3},
                {"step": "Tính đúng AC xấp xỉ 11,5 cm", "subScore": 0.35},
                {"step": "Tính đúng AB xấp xỉ 16,4 cm", "subScore": 0.35}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một chiếc tàu thủy rời cảng đi theo hướng tạo với bờ biển một góc $40^\\circ$ với vận tốc $30$ km/h. Sau $2$ giờ, tàu cách bờ biển bao nhiêu kilômét (biết bờ biển thẳng, làm tròn đến chữ số thập phân thứ nhất)?",
            "maxScore": 1.0,
            "solution": "Quãng đường tàu đi được sau 2 giờ là:\n$s = v \\cdot t = 30 \\cdot 2 = 60$ km.\nGọi vị trí xuất phát là cảng $A$, vị trí của tàu sau 2 giờ là $B$, và $H$ là hình chiếu vuông góc của $B$ lên bờ biển (khoảng cách từ tàu đến bờ biển).\nTrong tam giác vuông $AHB$ vuông tại $H$, góc $\\widehat{HAB} = 40^\\circ$, cạnh huyền $AB = 60$ km.\nKhoảng cách từ tàu đến bờ biển là độ dài đoạn $BH$:\n$BH = AB \\cdot \\sin 40^\\circ = 60 \\cdot \\sin 40^\\circ \\approx 60 \\cdot 0{,}6428 \\approx 38{,}6$ km.\nVậy sau 2 giờ tàu cách bờ biển khoảng $38{,}6$ km.",
            "rubric": [
                {"step": "Tính quãng đường AB = 60 km và mô tả tam giác vuông", "subScore": 0.4},
                {"step": "Áp dụng hệ thức cạnh góc vuông = cạnh huyền x sin góc đối tính BH = 38,6 km", "subScore": 0.6}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Để đo chiều cao của một tòa tháp $CD$, người ta chọn hai điểm $A$ và $B$ trên mặt đất thẳng hàng với chân tháp $D$, cách nhau $40$ m. Từ $A$ và $B$ đo được các góc nâng lên đỉnh tháp lần lượt là $30^\\circ$ và $45^\\circ$. Tính chiều cao $CD$ của tòa tháp (làm tròn đến hàng phần mười mét).",
            "maxScore": 1.0,
            "solution": "Gọi chiều cao tòa tháp là $h = CD$ ($h > 0$).\nTrong tam giác vuông $BCD$ vuông tại $D$, có $\\widehat{CBD} = 45^\\circ$ nên tam giác $BCD$ vuông cân tại $D$.\nSuy ra $BD = CD = h$.\nTrong tam giác vuông $ACD$ vuông tại $D$, có $\\widehat{CAD} = 30^\\circ$, ta có:\n$AD = CD \\cdot \\cot 30^\\circ = h\\sqrt{3}$.\nMặt khác, theo đề bài $A, B, D$ thẳng hàng và $AB = AD - BD = 40$ m.\nSuy ra: $h\\sqrt{3} - h = 40 \\Leftrightarrow h(\\sqrt{3} - 1) = 40$.\n$h = \\frac{40}{\\sqrt{3} - 1} = \\frac{40(\\sqrt{3} + 1)}{2} = 20(\\sqrt{3} + 1) \\approx 20(2{,}732) \\approx 54{,}6$ m.\nVậy chiều cao của tòa tháp xấp xỉ $54{,}6$ m.",
            "rubric": [
                {"step": "Biểu diễn BD = h và AD = h*sqrt(3)", "subScore": 0.5},
                {"step": "Thiết lập phương trình h(sqrt(3) - 1) = 40 và giải ra h xấp xỉ 54,6 m", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c4_9_bai2_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 12: Một số hệ thức giữa cạnh và góc trong tam giác vuông - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $b = 10$ cm, $\\widehat{C} = 40^\\circ$. Cạnh $c$ bằng:", "options": ["$10 \\cdot \\cot 40^\\circ$", "$10 \\cdot \\tan 40^\\circ$", "$10 / \\tan 40^\\circ$", "$10 \\cdot \\sin 40^\\circ$"], "correct": 1},
        {"id": 2, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 8$ cm, $AC = 6$ cm. Số đo góc $B$ (làm tròn đến độ) xấp xỉ:", "options": ["$37^\\circ$", "$53^\\circ$", "$45^\\circ$", "$30^\\circ$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Một người leo núi từ chân dốc lên đỉnh dốc dài $1200$ m, góc dốc nghiêng $18^\\circ$ so với phương ngang. Độ cao mà người đó đạt được là bao nhiêu mét (làm tròn đến hàng đơn vị, biết $\\sin 18^\\circ \\approx 0{,}3090$)?", "options": ["$371$ m", "$1141$ m", "$390$ m", "$400$ m"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Cho tam giác nhọn $ABC$ có $AB = 10$ cm, $\\widehat{B} = 45^\\circ$. Chiều cao $AH$ hạ từ đỉnh $A$ xuống $BC$ có độ dài:", "options": ["$5\\sqrt{2}$ cm", "$10\\sqrt{2}$ cm", "$5$ cm", "$5\\sqrt{3}$ cm"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tam giác $ABC$ cân tại $A$ có cạnh đáy $BC = 16$ cm và $\\widehat{B} = 50^\\circ$. Chiều cao $AH$ ứng với đáy xấp xỉ:", "options": ["$9{,}5$ cm", "$6{,}7$ cm", "$13{,}4$ cm", "$10{,}5$ cm"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có $\\widehat{B} = 60^\\circ, \\widehat{C} = 45^\\circ$ và $BC = 10$ cm. Kẻ đường cao $AH$. Chiều cao $AH$ có giá trị bằng:", "options": ["$\\frac{10}{\\frac{\\sqrt{3}}{3} + 1}$ cm", "$5\\sqrt{3}$ cm", "$5$ cm", "$10(\\sqrt{3}-1)$ cm"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Một con tàu ở ngoài biển quan sát thấy ngọn hải đăng có độ cao $75$ m dưới góc nâng $12^\\circ$. Khoảng cách từ tàu đến chân ngọn hải đăng xấp xỉ (lấy $\\tan 12^\\circ \\approx 0{,}2126$):", "options": ["$353$ m", "$360$ m", "$312$ m", "$405$ m"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Cho hình thang vuông $ABCD$ vuông tại $A$ và $D$ có đáy nhỏ $AB = 4$ cm, đáy lớn $CD = 10$ cm, góc $\\widehat{C} = 30^\\circ$. Chiều cao $AD$ của hình thang là:", "options": ["$2\\sqrt{3}$ cm", "$6\\sqrt{3}$ cm", "$3\\sqrt{3}$ cm", "$6$ cm"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Một bức tường cao $3$ m. Muốn kê một chiếc thang sao cho góc tạo bởi thang với mặt đất là $65^\\circ$ để đảm bảo an toàn thì độ dài chiếc thang cần chọn ít nhất là:", "options": ["$3{,}31$ m", "$3{,}50$ m", "$2{,}72$ m", "$4{,}00$ m"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có $AB = 5$ cm, $AC = 8$ cm và góc $\\widehat{A} = 30^\\circ$. Diện tích của tam giác $ABC$ là:", "options": ["$10$ cm$^2$", "$20$ cm$^2$", "$10\\sqrt{3}$ cm$^2$", "$20\\sqrt{3}$ cm$^2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một ca nô qua sông với vận tốc riêng $15$ km/h, hướng thẳng góc với bờ sông. Vận tốc dòng nước là $5$ km/h. Góc lệch của đường đi thực tế của ca nô so với hướng vuông góc với bờ sông (làm tròn đến độ) là:", "options": ["$18^\\circ$", "$72^\\circ$", "$15^\\circ$", "$20^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ vuông tại $A$, phân giác $AD$. Biết $AB = c, AC = b$. Khi đó độ dài đoạn phân giác $AD$ tính theo $b, c$ là:", "options": ["$\\frac{\\sqrt{2}bc}{b + c}$", "$\\frac{2bc}{b + c}$", "$\\frac{\\sqrt{2}(b+c)}{bc}$", "$\\frac{bc}{\\sqrt{2}(b + c)}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 9$ cm, $AC = 12$ cm, kẻ đường cao $AH$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Cạnh huyền $BC = 15$ cm.", "isCorrect": True, "explanation": "$BC = \\sqrt{9^2 + 12^2} = 15$ cm."},
                {"id": "b", "statement": "Góc nhọn $B$ có $\\sin B = 0{,}8$.", "isCorrect": True, "explanation": "$\\sin B = AC / BC = 12/15 = 0{,}8$."},
                {"id": "c", "statement": "Đường cao $AH = BC \\cdot \\sin B \\cdot \\cos B = 7{,}2$ cm.", "isCorrect": True, "explanation": "$AH = AB \\cdot AC / BC = (9 \\cdot 12) / 15 = 7{,}2$ cm."},
                {"id": "d", "statement": "Độ dài đoạn $BH$ bằng $6$ cm.", "isCorrect": False, "explanation": "$BH = AB^2 / BC = 81 / 15 = 5{,}4$ cm, không phải $6$ cm."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một người trên đỉnh một vách đá cao $100$ m so với mặt biển nhìn thấy hai chiếc thuyền đang neo đậu trên cùng một đường thẳng đi qua chân vách đá. Các góc hạ nhìn hai thuyền lần lượt là $30^\\circ$ và $45^\\circ$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Khoảng cách từ chân vách đá đến chiếc thuyền gần hơn là $100$ m.", "isCorrect": True, "explanation": "Chiếc thuyền có góc hạ $45^\\circ$ ở gần hơn, tam giác vuông cân nên khoảng cách $= 100$ m."},
                {"id": "b", "statement": "Khoảng cách từ chân vách đá đến chiếc thuyền xa hơn là $100\\sqrt{3}$ m.", "isCorrect": True, "explanation": "Chiếc thuyền có góc hạ $30^\\circ$ cách chân đá $= 100 \\cdot \\cot 30^\\circ = 100\\sqrt{3}$ m."},
                {"id": "c", "statement": "Khoảng cách giữa hai chiếc thuyền là $100(\\sqrt{3} - 1)$ m.", "isCorrect": True, "explanation": "$d = 100\\sqrt{3} - 100 = 100(\\sqrt{3} - 1)$ m."},
                {"id": "d", "statement": "Biết $\\sqrt{3} \\approx 1{,}732$, khoảng cách giữa hai thuyền xấp xỉ bằng $173{,}2$ m.", "isCorrect": False, "explanation": "Khoảng cách $= 100(1{,}732 - 1) = 73{,}2$ m, không phải $173{,}2$ m."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ có $\\widehat{A} = 60^\\circ, AB = 4$ cm, $AC = 6$ cm. Tính diện tích tam giác $ABC$ theo cm$^2$ (kết quả dạng $a\\sqrt{3}$, điền giá trị của $a$).", "answer": 6, "unit": ""},
        {"id": 2, "level": "Thông hiểu", "question": "Một người cao $1{,}6$ m đứng cách một bóng cây $6$ m. Biết bóng của người đó trên mặt đất dài $2$ m. Tính chiều cao ngọn cây theo mét.", "answer": 4.8, "unit": "m"},
        {"id": 3, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$ có $AC = 12$ cm và $\\tan C = 0{,}75$. Tính độ dài cạnh huyền $BC$ theo cm.", "answer": 15, "unit": "cm"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một khúc sông rộng $250$ m. Một chiếc thuyền chèo qua sông bị dòng nước đẩy xiên một góc $30^\\circ$ so với hướng vuông góc bờ sông. Chiều dài đường đi thực tế của thuyền là bao nhiêu mét (làm tròn đến hàng đơn vị)?", "answer": 289, "unit": "m"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 12$ cm và góc $\\widehat{B} = 40^\\circ$.\na) Tính các cạnh $AC$ và $BC$ của tam giác $ABC$ (làm tròn đến 1 chữ số thập phân).\nb) Tính độ dài đường cao $AH$.",
            "maxScore": 1.0,
            "solution": "a) Trong tam giác vuông $ABC$:\n$AC = AB \\cdot \\tan B = 12 \\cdot \\tan 40^\\circ \\approx 12 \\cdot 0{,}8391 \\approx 10{,}1$ cm.\n$BC = \\frac{AB}{\\cos B} = \\frac{12}{\\cos 40^\\circ} \\approx \\frac{12}{0{,}7660} \\approx 15{,}7$ cm.\nb) Trong tam giác vuông $AHB$ vuông tại $H$:\n$AH = AB \\cdot \\sin B = 12 \\cdot \\sin 40^\\circ \\approx 12 \\cdot 0{,}6428 \\approx 7{,}7$ cm.",
            "rubric": [
                {"step": "Tính đúng AC xấp xỉ 10,1 cm và BC xấp xỉ 15,7 cm", "subScore": 0.6},
                {"step": "Tính đúng AH xấp xỉ 7,7 cm", "subScore": 0.4}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Hai người cùng nhìn một khinh khí cầu từ hai địa điểm $A$ và $B$ trên mặt đất cách nhau $300$ m, cùng nằm trên một mặt phẳng thẳng đứng với khinh khí cầu và nằm cùng một phía so với khinh khí cầu. Góc nâng nhìn khinh khí cầu tại $A$ là $35^\\circ$ và tại $B$ là $50^\\circ$. Tính độ cao của khinh khí cầu (làm tròn đến hàng đơn vị mét).",
            "maxScore": 1.0,
            "solution": "Gọi $C$ là vị trí của khinh khí cầu và $H$ là hình chiếu vuông góc của $C$ trên mặt đất. Gọi độ cao $CH = h$ ($h > 0$).\nVì $A$ và $B$ nằm cùng một phía đối với $H$ và góc tại $B$ ($50^\\circ$) lớn hơn góc tại $A$ ($35^\\circ$), nên $B$ nằm giữa $A$ và $H$.\nTrong tam giác vuông $AHC$:\n$AH = h \\cdot \\cot 35^\\circ$.\nTrong tam giác vuông $BHC$:\n$BH = h \\cdot \\cot 50^\\circ$.\nTa có: $AB = AH - BH = h(\\cot 35^\\circ - \\cot 50^\\circ) = 300$.\nDo đó:\n$h = \\frac{300}{\\cot 35^\\circ - \\cot 50^\\circ} = \\frac{300}{\\frac{1}{\\tan 35^\\circ} - \\frac{1}{\\tan 50^\\circ}}$.\nBiết $\\tan 35^\\circ \\approx 0{,}7002 \\Rightarrow \\cot 35^\\circ \\approx 1{,}4281$.\n$\\tan 50^\\circ \\approx 1{,}1918 \\Rightarrow \\cot 50^\\circ \\approx 0{,}8391$.\nSuy ra $h = \\frac{300}{1{,}4281 - 0{,}8391} = \\frac{300}{0{,}589} \\approx 509$ m.\nVậy khinh khí cầu ở độ cao khoảng $509$ m.",
            "rubric": [
                {"step": "Thiết lập hệ thức AH = h cot 35 độ, BH = h cot 50 độ", "subScore": 0.5},
                {"step": "Giải phương trình hiệu khoảng cách tính ra h xấp xỉ 509 m", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $AD$ là đường phân giác trong của góc $A$ ($D \\in BC$).\nChứng minh rằng: $\\frac{1}{AB} + \\frac{1}{AC} = \\frac{\\sqrt{2}}{AD}$.",
            "maxScore": 1.0,
            "solution": "Kẻ phân giác $AD$ chia góc vuông $\\widehat{A}$ thành hai góc bằng $45^\\circ$: $\\widehat{BAD} = \\widehat{CAD} = 45^\\circ$.\nDiện tích tam giác $ABC$ bằng tổng diện tích hai tam giác $ABD$ và $ACD$:\n$S_{ABC} = S_{ABD} + S_{ACD}$.\nÁp dụng công thức tính diện tích qua sin của góc kẹp giữa:\n$S_{ABC} = \\frac{1}{2} AB \\cdot AC$.\n$S_{ABD} = \\frac{1}{2} AB \\cdot AD \\cdot \\sin 45^\\circ = \\frac{1}{2} AB \\cdot AD \\cdot \\frac{\\sqrt{2}}{2}$.\n$S_{ACD} = \\frac{1}{2} AC \\cdot AD \\cdot \\sin 45^\\circ = \\frac{1}{2} AC \\cdot AD \\cdot \\frac{\\sqrt{2}}{2}$.\nDo đó:\n$\\frac{1}{2} AB \\cdot AC = \\frac{\\sqrt{2}}{4} AD (AB + AC)$.\nNhân cả hai vế với 2 rồi chia cả hai vế cho $AB \\cdot AC \\cdot AD$:\n$\\frac{1}{AD} = \\frac{\\sqrt{2}}{2} \\cdot \\frac{AB + AC}{AB \\cdot AC} = \\frac{\\sqrt{2}}{2} \\left(\\frac{1}{AC} + \\frac{1}{AB}\\right)$.\nNhân cả hai vế với $\\sqrt{2}$:\n$\\frac{\\sqrt{2}}{AD} = \\frac{1}{AB} + \\frac{1}{AC}$ (đpcm).",
            "rubric": [
                {"step": "Sử dụng tổng diện tích S_ABC = S_ABD + S_ACD với sin 45 độ", "subScore": 0.6},
                {"step": "Biến đổi đại số rút ra hệ thức cần chứng minh", "subScore": 0.4}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c4_9_bai2_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 12: Một số hệ thức giữa cạnh và góc trong tam giác vuông - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 30^\\circ$ và cạnh $c = AB = 8$ cm. Chiều cao $AH$ có độ dài:", "options": ["$4\\sqrt{2}$ cm", "$4$ cm", "$8\\sqrt{2}$ cm", "$4\\sqrt{3}$ cm"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho tam giác $ABC$ nhọn. Định lí sin phát biểu rằng trong tam giác $ABC$ với $R$ là bán kính đường tròn ngoại tiếp:", "options": ["$\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$", "$\\frac{a}{\\sin A} = R$", "$\\frac{a}{\\cos A} = 2R$", "$\\frac{\\sin A}{a} = 2R$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có $\\widehat{A} = 105^\\circ, \\widehat{B} = 45^\\circ$ và $BC = 12$ cm. Độ dài cạnh $AC$ bằng:", "options": ["$6\\sqrt{2}$ cm", "$6\\sqrt{6}$ cm", "$4\\sqrt{6}$ cm", "$6$ cm"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho hình bình hành $ABCD$ có $AB = 6$ cm, $AD = 8$ cm và $\\widehat{A} = 60^\\circ$. Diện tích của hình bình hành $ABCD$ là:", "options": ["$24\\sqrt{3}$ cm$^2$", "$48$ cm$^2$", "$12\\sqrt{3}$ cm$^2$", "$48\\sqrt{3}$ cm$^2$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$ có chu vi $72$ cm và $\\tan B = \\frac{3}{4}$. Độ dài cạnh huyền $BC$ là:", "options": ["$30$ cm", "$24$ cm", "$18$ cm", "$25$ cm"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một người đứng tại bờ biển quan sát một ngọn hải đăng cao $50$ m. Ban đầu người đó thấy ngọn đèn với góc nâng $20^\\circ$, sau khi đi thẳng lại gần thêm $40$ m thấy ngọn đèn với góc nâng $x$. Góc $x$ (làm tròn đến độ) xấp xỉ:", "options": ["$27^\\circ$", "$35^\\circ$", "$22^\\circ$", "$30^\\circ$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Cho tam giác $ABC$ có trung tuyến $AM = 5$ cm và $AB = 6$ cm, $AC = 8$ cm. Tam giác $ABC$ là tam giác gì?", "options": ["Tam giác vuông tại $A$", "Tam giác đều", "Tam giác nhọn không đều", "Tam giác tù"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ nhọn có đường cao $AH$. Đẳng thức nào sau đây luôn đúng?", "options": ["$BC = AH(\\cot B + \\cot C)$", "$BC = AH(\\tan B + \\tan C)$", "$BC = AH(\\sin B + \\sin C)$", "$BC = \\frac{AH}{\\cot B + \\cot C}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Một cột truyền hình cao $80$ m được giữ bằng 3 sợi dây cáp thép nối từ đỉnh cột xuống các vị trí cố định trên mặt đất. Các sợi dây cáp đều tạo với mặt đất góc $60^\\circ$. Tổng chiều dài của 3 sợi dây cáp (bỏ qua đoạn nối buộc) xấp xỉ:", "options": ["$277$ m", "$240$ m", "$160$ m", "$300$ m"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hình chữ nhật $ABCD$ có $AB = 24$ cm, $AD = 10$ cm. Gọi $O$ là giao điểm hai đường chéo. Số đo góc nhọn giữa hai đường chéo (làm tròn đến phút) là:", "options": ["$45^\\circ 14'$", "$44^\\circ 46'$", "$22^\\circ 37'$", "$67^\\circ 23'$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ có diện tích $S = 24$ cm$^2$, nửa chu vi $p = 12$ cm. Bán kính đường tròn nội tiếp $r$ của tam giác là:", "options": ["$2$ cm", "$3$ cm", "$4$ cm", "$1$ cm"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho tam giác vuông $ABC$ tại $A$ có $b, c$ là hai cạnh góc vuông và $h$ là chiều cao ứng với cạnh huyền. Khi đó $\\frac{1}{b^2} + \\frac{1}{c^2}$ bằng:", "options": ["$\\frac{1}{h^2}$", "$h^2$", "$\\frac{1}{2h^2}$", "$\\frac{2}{h^2}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ có $\\widehat{B} = 60^\\circ, \\widehat{C} = 45^\\circ$, kẻ đường cao $AH = h = 6$ cm. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "$BH = \\frac{h}{\\tan 60^\\circ} = 2\\sqrt{3}$ cm.", "isCorrect": True, "explanation": "$BH = 6 / \\sqrt{3} = 2\\sqrt{3}$ cm."},
                {"id": "b", "statement": "$CH = \\frac{h}{\\tan 45^\\circ} = 6$ cm.", "isCorrect": True, "explanation": "$CH = 6 / 1 = 6$ cm."},
                {"id": "c", "statement": "Độ dài cạnh $BC = BH + CH = 6 + 2\\sqrt{3}$ cm.", "isCorrect": True, "explanation": "$BC = 6 + 2\\sqrt{3}$ cm."},
                {"id": "d", "statement": "Diện tích tam giác $ABC$ bằng $18 + 6\\sqrt{3}$ cm$^2$.", "isCorrect": True, "explanation": "$S = \\frac{1}{2} BC \\cdot AH = \\frac{1}{2}(6 + 2\\sqrt{3}) \\cdot 6 = 18 + 6\\sqrt{3}$ cm$^2$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Một người ngắm hai điểm $P$ và $Q$ ở hai bờ đối diện của một hồ nước từ đỉnh đài quan sát $T$ cao $40$ m. $T, P, Q$ cùng nằm trên một mặt phẳng thẳng đứng chứa chân đài quan sát $O$. Góc hạ ngắm điểm $P$ là $45^\\circ$ và điểm $Q$ là $25^\\circ$ ($P$ nằm giữa $O$ và $Q$). Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Khoảng cách $OP = 40$ m.", "isCorrect": True, "explanation": "Tam giác $TOP$ vuông cân tại $O$ vì góc hạ bằng $45^\\circ$, nên $OP = TO = 40$ m."},
                {"id": "b", "statement": "Khoảng cách $OQ = 40 \\cdot \\cot 25^\\circ$.", "isCorrect": True, "explanation": "Trong tam giác vuông $TOQ$, $OQ = TO \\cdot \\cot 25^\\circ$."},
                {"id": "c", "statement": "Biết $\\tan 25^\\circ \\approx 0{,}4663$, khoảng cách $OQ \\approx 85{,}8$ m.", "isCorrect": True, "explanation": "$OQ = 40 / 0{,}4663 \\approx 85{,}78$ m."},
                {"id": "d", "statement": "Chiều rộng hồ nước giữa hai điểm $P$ và $Q$ xấp xỉ bằng $55{,}8$ m.", "isCorrect": False, "explanation": "Chiều rộng $PQ = OQ - OP \\approx 85{,}78 - 40 = 45{,}78$ m, không phải $55{,}8$ m."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Cho hình thoi $ABCD$ có cạnh bằng $10$ cm và một góc bằng $60^\\circ$. Tính diện tích hình thoi theo cm$^2$ (kết quả dạng $a\\sqrt{3}$, điền giá trị của $a$).", "answer": 50, "unit": ""},
        {"id": 2, "level": "Vận dụng", "question": "Cho tam giác $ABC$ vuông tại $A$ có đường cao $AH = 4{,}8$ cm và $AB = 6$ cm. Tính độ dài cạnh $AC$ theo cm.", "answer": 8, "unit": "cm"},
        {"id": 3, "level": "Vận dụng cao", "question": "Một máy bay hạ cánh theo đường bay thẳng nghiêng một góc $3^\\circ$ so với mặt đất. Khi máy bay ở độ cao $600$ m, khoảng cách mặt đất từ vị trí máy bay đến điểm chạm bánh là bao nhiêu mét (làm tròn đến hàng chục, biết $\\tan 3^\\circ \\approx 0{,}0524$)?", "answer": 11450, "unit": "m"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác nhọn $ABC$ có $BC = 10$ cm, $\\widehat{B} = 45^\\circ, \\widehat{C} = 60^\\circ$. Kẻ đường cao $AH$. Tính $AH$ theo cm (lấy $\\sqrt{3} \\approx 1{,}732$, làm tròn đến hàng phần mười).", "answer": 6.3, "unit": "cm"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ có góc $\\widehat{A}$ nhọn. Kẻ đường cao $BD$ và $CE$ ($D \\in AC, E \\in AB$).\na) Chứng minh $AD = AB \\cdot \\cos A$ và $AE = AC \\cdot \\cos A$.\nb) Chứng minh rằng $\\triangle ADE \\backsim \\triangle ABC$ và $S_{ADE} = S_{ABC} \\cdot \\cos^2 A$.",
            "maxScore": 1.0,
            "solution": "a) Xét tam giác vuông $ABD$ vuông tại $D$:\n$\\cos A = \\frac{AD}{AB} \\Rightarrow AD = AB \\cdot \\cos A$.\nXét tam giác vuông $ACE$ vuông tại $E$:\n$\\cos A = \\frac{AE}{AC} \\Rightarrow AE = AC \\cdot \\cos A$.\nb) Từ câu a suy ra:\n$\\frac{AD}{AB} = \\frac{AE}{AC} = \\cos A$.\nXét hai tam giác $ADE$ và $ABC$ có:\n- Góc $\\widehat{A}$ chung;\n- $\\frac{AD}{AC} = \\frac{AE}{AB}$ (do cùng bằng $\\frac{AD \\cdot AE}{AB \\cdot AC}$).\nDo đó $\\triangle ADE \\backsim \\triangle ABC$ (c-g-c) theo tỉ số đồng dạng $k = \\cos A$.\nTỉ số diện tích của hai tam giác đồng dạng bằng bình phương tỉ số đồng dạng:\n$\\frac{S_{ADE}}{S_{ABC}} = k^2 = \\cos^2 A \\Rightarrow S_{ADE} = S_{ABC} \\cdot \\cos^2 A$ (đpcm).",
            "rubric": [
                {"step": "Chứng minh hệ thức AD và AE qua cos A", "subScore": 0.4},
                {"step": "Chứng minh tam giác ADE đồng dạng tam giác ABC với tỉ số k = cos A", "subScore": 0.3},
                {"step": "Suy ra tỉ số diện tích bằng cos^2 A", "subScore": 0.3}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Để đo khoảng cách giữa hai điểm $A$ và $B$ bị ngăn cách bởi một dòng sông sâu, một nhóm học sinh chọn hai điểm $C$ và $D$ trên cùng bờ sông sao cho $C, D, A, B$ cùng nhìn thấy nhau. Đo được $CD = 100$ m, $\\widehat{ACD} = 80^\\circ, \\widehat{BCD} = 30^\\circ, \\widehat{ADC} = 40^\\circ, \\widehat{BDC} = 75^\\circ$. Hãy tính khoảng cách $AB$ (làm tròn đến hàng đơn vị mét).",
            "maxScore": 1.0,
            "solution": "Xét tam giác $ACD$:\n$\\widehat{CAD} = 180^\\circ - (80^\\circ + 40^\\circ) = 60^\\circ$.\nÁp dụng định lí sin trong tam giác $ACD$:\n$\\frac{AC}{\\sin 40^\\circ} = \\frac{CD}{\\sin 60^\\circ} \\Rightarrow AC = \\frac{100 \\cdot \\sin 40^\\circ}{\\sin 60^\\circ} \\approx \\frac{100 \\cdot 0{,}6428}{0{,}8660} \\approx 74{,}2$ m.\nXét tam giác $BCD$:\n$\\widehat{CBD} = 180^\\circ - (30^\\circ + 75^\\circ) = 75^\\circ$.\nVì $\\widehat{CBD} = \\widehat{BDC} = 75^\\circ$ nên tam giác $BCD$ cân tại $C$.\nDo đó: $BC = CD = 100$ m.\nXét tam giác $ABC$ có:\n$\\widehat{ACB} = \\widehat{ACD} - \\widehat{BCD} = 80^\\circ - 30^\\circ = 50^\\circ$.\n$AC \\approx 74{,}2$ m, $BC = 100$ m.\nÁp dụng định lí côsin trong tam giác $ABC$:\n$AB^2 = AC^2 + BC^2 - 2AC \\cdot BC \\cdot \\cos 50^\\circ$\n$AB^2 \\approx 74{,}2^2 + 100^2 - 2(74{,}2)(100) \\cos 50^\\circ$\n$\\approx 5505{,}6 + 10000 - 14840 \\cdot 0{,}6428 \\approx 15505{,}6 - 9539{,}2 \\approx 5966{,}4$.\n$AB \\approx \\sqrt{5966{,}4} \\approx 77$ m.\nVậy khoảng cách $AB$ xấp xỉ $77$ m.",
            "rubric": [
                {"step": "Tính độ dài AC trong tam giác ACD bằng định lí sin", "subScore": 0.4},
                {"step": "Nhận ra tam giác BCD cân để tính BC = 100 m", "subScore": 0.3},
                {"step": "Áp dụng định lí cosin trong tam giác ABC tính ra AB xấp xỉ 77 m", "subScore": 0.3}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có đường cao $AH$, $M$ là trung điểm của cạnh $BC$. Cho biết $AH = 12$ cm và $AM = 13$ cm.\na) Tính độ dài cạnh huyền $BC$.\nb) Tính các cạnh góc vuông $AB, AC$ và các góc nhọn $\\widehat{B}, \\widehat{C}$ (làm tròn đến độ).",
            "maxScore": 1.0,
            "solution": "a) Trong tam giác vuông $ABC$, đường trung tuyến $AM$ ứng với cạnh huyền bằng nửa cạnh huyền:\n$AM = \\frac{BC}{2} \\Rightarrow BC = 2 \\cdot AM = 2 \\cdot 13 = 26$ cm.\nb) Trong tam giác vuông $AHM$ vuông tại $H$:\n$HM = \\sqrt{AM^2 - AH^2} = \\sqrt{13^2 - 12^2} = \\sqrt{169 - 144} = \\sqrt{25} = 5$ cm.\nVì $M$ là trung điểm $BC$ nên $BM = MC = 13$ cm.\nTa xét hai trường hợp của $H$ nằm giữa $B$ và $M$ (không mất tính tổng quát, giả sử $B$ gần $H$ hơn $C$):\n$BH = BM - HM = 13 - 5 = 8$ cm.\n$CH = CM + HM = 13 + 5 = 18$ cm.\nÁp dụng hệ thức lượng trong tam giác vuông $ABC$:\n$AB^2 = BH \\cdot BC = 8 \\cdot 26 = 208 \\Rightarrow AB = \\sqrt{208} = 4\\sqrt{13} \\approx 14{,}4$ cm.\n$AC^2 = CH \\cdot BC = 18 \\cdot 26 = 468 \\Rightarrow AC = \\sqrt{468} = 6\\sqrt{13} \\approx 21{,}6$ cm.\nTính các góc nhọn:\n$\\sin B = \\frac{AC}{BC} = \\frac{6\\sqrt{13}}{26} = \\frac{3\\sqrt{13}}{13} \\approx 0{,}832 \\Rightarrow \\widehat{B} \\approx 56^\\circ$.\n$\\widehat{C} = 90^\\circ - 56^\\circ = 34^\\circ$.",
            "rubric": [
                {"step": "Tính đúng BC = 26 cm từ tính chất trung tuyến", "subScore": 0.3},
                {"step": "Tính đúng HM = 5 cm, suy ra BH = 8 cm, CH = 18 cm", "subScore": 0.4},
                {"step": "Tính đúng AB, AC và các góc B xấp xỉ 56 độ, C xấp xỉ 34 độ", "subScore": 0.3}
            ]
        }
    ]
}
