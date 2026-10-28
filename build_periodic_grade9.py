# -*- coding: utf-8 -*-
"""
GENERATOR BỘ ĐỀ THI ĐỊNH KỲ TOÁN 9 (GIỮA KỲ 2 & CUỐI KỲ 2)
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
# 6 MÃ ĐỀ GIỮA KỲ 2 - TOÁN 9 (mid2)
# Phạm vi: Hàm số y = ax^2, Phương trình bậc hai, Định lí Viète & Tứ giác nội tiếp
# ==============================================================================
def generate_g9_mid2():
    exams = []
    
    for t_idx in range(1, 7):
        ex_num = f"0{t_idx}"
        topics = [
            "Hàm số y = ax^2, Định lí Viète, Giải bài toán bằng cách lập PT bậc hai & Tứ giác nội tiếp",
            "Đồ thị parabol, Công thức nghiệm phương trình bậc hai & Dấu hiệu tứ giác nội tiếp",
            "Tương giao Parabol và đường thẳng, Hệ thức Viète đối xứng & Tứ giác nội tiếp",
            "Ứng dụng thực tế hàm số bậc hai, Định lí Viète tìm hai số & Góc nội tiếp đường tròn",
            "Bài toán chuyển động lập PT bậc hai, Phương trình quy về bậc hai & Chứng minh tứ giác nội tiếp",
            "Tổng hợp giữa kỳ 2: Hàm số Parabol, Viète nâng cao và Hình học tứ giác nội tiếp"
        ]
        topic = topics[t_idx - 1]

        exams.append({
            "id": f"p_g9_mid2_{ex_num}",
            "testNum": t_idx,
            "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ II - TOÁN 9 (ĐỀ SỐ {ex_num})",
            "topic": topic,
            "grade": "9",
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
                make_mc(1, "Nhận biết", f"Điểm nào sau đây thuộc đồ thị hàm số $y = {t_idx}x^2$?", [f"$A(1; {t_idx})$", "$B(1; -1)$", "$C(2; 1)$", "$D(-1; 0)$"], 0, f"Thay $x = 1 \\Rightarrow y = {t_idx} \\cdot 1^2 = {t_idx}$."),
                make_mc(2, "Nhận biết", "Trong một tứ giác nội tiếp đường tròn, tổng số đo hai góc đối diện bằng:", ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$120^\\circ$"], 0, "Định lí: Trong một tứ giác nội tiếp, tổng hai góc đối nhau bằng $180^\\circ$."),
                make_mc(3, "Nhận biết", f"Biệt thức $\\Delta$ của phương trình bậc hai $x^2 - {2 * t_idx}x + 3 = 0$ là:", [f"${4 * t_idx**2 - 12}$", f"${4 * t_idx**2 + 12}$", f"${t_idx**2 - 3}$", "$-12$"], 0, f"$\\Delta = b^2 - 4ac = (-{2*t_idx})^2 - 4 \\cdot 1 \\cdot 3 = {4*t_idx**2 - 12}$."),
                make_mc(4, "Thông hiểu", f"Cho phương trình $x^2 - {3 * t_idx}x + {2 * t_idx**2} = 0$. Theo định lí Viète, tổng hai nghiệm $x_1 + x_2$ bằng:", [f"${3 * t_idx}$", f"$-{3 * t_idx}$", f"${2 * t_idx**2}$", f"$-{2 * t_idx**2}$"], 0, f"$x_1 + x_2 = -b/a = -(-{3*t_idx}) = {3*t_idx}$."),
                make_mc(5, "Thông hiểu", f"Hàm số $y = -{t_idx}x^2$ đồng biến trên khoảng nào?", ["$(-\\infty; 0)$", "$(0; +\\infty)$", "$\\mathbb{R}$", "$(0; 1)$"], 0, f"Vì hệ số $a = -{t_idx} < 0$ nên hàm số đồng biến khi $x < 0$, tức trên khoảng $(-\\infty; 0)$."),
                make_mc(6, "Thông hiểu", "Cho tứ giác $ABCD$ nội tiếp đường tròn $(O)$. Biết $\\widehat{A} = 75^\\circ$. Số đo góc $\\widehat{C}$ đối diện là:", ["$105^\\circ$", "$75^\\circ$", "$15^\\circ$", "$90^\\circ$"], 0, "$\\widehat{C} = 180^\\circ - \\widehat{A} = 180^\\circ - 75^\\circ = 105^\\circ$."),
                make_mc(7, "Vận dụng", f"Tìm tọa độ giao điểm của parabol $(P): y = x^2$ và đường thẳng $(d): y = {t_idx + 1}x - {t_idx}$.", [f"$(1; 1)$ và $({t_idx}; {t_idx**2})$", "$(0; 0)$", "$(2; 4)$", "Vô nghiệm"], 0, f"Phương trình hoành độ giao điểm: $x^2 - ({t_idx + 1})x + {t_idx} = 0 \\Rightarrow x_1 = 1, x_2 = {t_idx}$."),
                make_mc(8, "Vận dụng", f"Một mảnh vườn hình chữ nhật có diện tích ${60 * t_idx}\\,\\text{{m}}^2$. Biết chiều dài hơn chiều rộng $4\\,\\text{{m}}$. Gọi chiều rộng mảnh vườn là $x\\,\\text{{m}}$ ($x > 0$), phương trình tìm $x$ là:", [f"$x(x + 4) = {60 * t_idx}$", f"$x(x - 4) = {60 * t_idx}$", f"$2x + 4 = {60 * t_idx}$", f"$x^2 + 4 = {60 * t_idx}$"], 0, f"Chiều dài là $x + 4$. Diện tích: $x(x + 4) = {60*t_idx}$."),
                make_mc(9, "Vận dụng cao", f"Tìm giá trị của tham số $m$ để phương trình $x^2 - {2 * t_idx}x + m - 1 = 0$ có nghiệm kép.", [f"$m = {t_idx**2 + 1}$", f"$m = {t_idx**2}$", f"$m = {t_idx**2 - 1}$", "$m = 0$"], 0, f"Phương trình có nghiệm kép khi $\\Delta' = {t_idx**2} - (m - 1) = 0 \\Leftrightarrow m = {t_idx**2 + 1}$."),
                make_mc(10, "Vận dụng cao", f"Cho phương trình $x^2 - 4x + 1 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Giá trị của biểu thức $T = x_1^2 + x_2^2 + {t_idx}$ bằng:", [f"${14 + t_idx}$", f"${16 + t_idx}$", f"${12 + t_idx}$", "$14$"], 0, "$x_1 + x_2 = 4, x_1 x_2 = 1 \\Rightarrow x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1 x_2 = 16 - 2 = 14$."),
                make_mc(11, "Vận dụng cao", "Cho tam giác nhọn $ABC$ nội tiếp $(O)$. Hai đường cao $BD, CE$ cắt nhau tại $H$. Tứ giác nào sau đây là tứ giác nội tiếp?", ["$ADHE$", "$ABDE$", "$BDEC$ có tâm là $H$", "$OBDC$"], 0, "Tứ giác $ADHE$ có $\\widehat{ADH} + \\widehat{AEH} = 90^\\circ + 90^\\circ = 180^\\circ$ nên nội tiếp."),
                make_mc(12, "Vận dụng cao", f"Cho phương trình $x^2 - ({t_idx} + 2)x + 2{t_idx} = 0$. Khẳng định nào sau đây đúng?", [f"Phương trình luôn có nghiệm $x = 2$ và $x = {t_idx}$", "Phương trình luôn vô nghiệm", "Phương trình có nghiệm duy nhất", "Phương trình có hai nghiệm âm"], 0, f"$a - b + c = 0$ hoặc nhẩm nghiệm: $x_1 = 2, x_2 = {t_idx}$ thỏa mãn $x_1 + x_2 = {t_idx} + 2, x_1 x_2 = 2{t_idx}$.")
            ],
            "part2": [
                make_tf(1, f"Cho hàm số bậc hai $(P): y = {t_idx}x^2$ và đường thẳng $(d): y = {2 * t_idx}x$.", [
                    {"id": "a", "text": "Đồ thị Parabol $(P)$ có đỉnh là gốc tọa độ $O(0; 0)$.", "correct": True, "level": "Nhận biết", "explanation": "Parabol $y = ax^2$ luôn có đỉnh là $O(0; 0)$."},
                    {"id": "b", "text": "Trục đối xứng của Parabol $(P)$ là trục tung $Oy$.", "correct": True, "level": "Nhận biết", "explanation": "Trục đối xứng là trục tung $x = 0$."},
                    {"id": "c", "text": "Phương trình hoành độ giao điểm của $(P)$ và $(d)$ có hai nghiệm phân biệt $x = 0$ và $x = 2$.", "correct": True, "level": "Thông hiểu", "explanation": f"${t_idx}x^2 - {2*t_idx}x = 0 \\Leftrightarrow {t_idx}x(x - 2) = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$."},
                    {"id": "d", "text": "Khoảng cách giữa hai giao điểm của $(P)$ và $(d)$ bằng $2\\,\\text{cm}$.", "correct": False, "level": "Vận dụng", "explanation": f"Hai giao điểm là $(0; 0)$ và $(2; {4*t_idx})$. Khoảng cách giữa chúng là $\\sqrt{{4 + {16 * t_idx**2}}} > 2$."}
                ]),
                make_tf(2, f"Cho tam giác nhọn $ABC$ nội tiếp đường tròn $(O)$. Hai đường cao $BM$ và $CN$ cắt nhau tại trực tâm $H$.", [
                    {"id": "a", "text": "Đoạn thẳng $BC$ nhìn các điểm $M$ và $N$ dưới một góc vuông $90^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "Do $BM \\perp AC$ và $CN \\perp AB$."},
                    {"id": "b", "text": "Tứ giác $BNMC$ là tứ giác nội tiếp đường tròn đường kính $BC$.", "correct": True, "level": "Thông hiểu", "explanation": "Hai đỉnh kề $M, N$ cùng nhìn cạnh $BC$ dưới góc $90^\\circ$."},
                    {"id": "c", "text": "Tứ giác $AMHN$ có tổng hai góc đối $\\widehat{AMH} + \\widehat{ANH} = 180^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Tổng hai góc vuông bằng $180^\\circ$."},
                    {"id": "d", "text": "Điểm $H$ là tâm của đường tròn ngoại tiếp tam giác $ABC$.", "correct": False, "level": "Vận dụng", "explanation": "$H$ là trực tâm, không phải tâm đường tròn ngoại tiếp (tâm ngoại tiếp là $O$)."}
                ])
            ],
            "part3": [
                make_sa(1, "Nhận biết", f"Tính tích hai nghiệm $x_1 \\cdot x_2$ của phương trình: $x^2 - 7x + {3 * t_idx} = 0$.", str(3 * t_idx), [str(3 * t_idx)], f"Theo định lí Viète: $x_1 x_2 = c/a = {3 * t_idx}$."),
                make_sa(2, "Thông hiểu", f"Giải phương trình: $x^2 - {2 * t_idx}x = 0$. Nghiệm dương của phương trình là:", str(2 * t_idx), [str(2 * t_idx)], f"$x(x - {2*t_idx}) = 0 \\Rightarrow x = {2*t_idx}$."),
                make_sa(3, "Vận dụng", f"Một khu vườn hình chữ nhật có chu vi bằng ${20 * t_idx}\\,\\text{{m}}$ và diện tích bằng ${24 * t_idx**2}\\,\\text{{m}}^2$. Tính chiều dài của khu vườn (theo m):", str(6 * t_idx), [str(6 * t_idx)], f"Nửa chu vi $S = {10*t_idx}$, tích $P = {24*t_idx**2}$. Chiều dài và rộng là nghiệm của $X^2 - {10*t_idx}X + {24*t_idx**2} = 0 \\Rightarrow X = {6*t_idx}$ và ${4*t_idx}$."),
                make_sa(4, "Vận dụng cao", f"Cho phương trình $x^2 - 2mx + m^2 - 1 = 0$. Biết phương trình có hai nghiệm $x_1, x_2$. Giá trị của biểu thức $(x_1 - x_2)^2$ bằng:", "4", ["4", "4.0"], "$(x_1 - x_2)^2 = (x_1 + x_2)^2 - 4x_1 x_2 = (2m)^2 - 4(m^2 - 1) = 4m^2 - 4m^2 + 4 = 4$.")
            ],
            "part4": [
                make_essay(1, "Nhận biết", 1.0,
                    f"Giải các phương trình bậc hai sau:\n a) $x^2 - {4 * t_idx} = 0$\n b) $x^2 - {t_idx + 3}x + {3 * t_idx} = 0$",
                    f"a) $x^2 = {4*t_idx} \\Rightarrow x = \\pm 2\\sqrt{{{t_idx}}}$ (0.5đ)\nb) Phân tích nhân tử: $(x - 3)(x - {t_idx}) = 0 \\Leftrightarrow x = 3$ hoặc $x = {t_idx}$ (0.5đ)",
                    f"a) $x = \\pm 2\\sqrt{{{t_idx}}}$.\nb) Phương trình có hai nghiệm $x = 3$ và $x = {t_idx}$."
                ),
                make_essay(2, "Thông hiểu", 1.0,
                    f"Cho phương trình bậc hai: $x^2 - 2(m + 1)x + 2m = 0$ ($m$ là tham số).\n a) Chứng minh rằng phương trình luôn có hai nghiệm phân biệt với mọi giá trị của $m$.\n b) Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 = {4 * t_idx + 2}$.",
                    "a) $\\Delta' = (m+1)^2 - 2m = m^2 + 1 > 0$ với mọi $m$ (0.5đ)\nb) $x_1 + x_2 = 2(m+1), x_1 x_2 = 2m$. $x_1^2 + x_2^2 = 4(m+1)^2 - 4m = 4m^2 + 4m + 4$. Cho bằng đề bài giải tìm $m$ (0.5đ)",
                    "a) $\\Delta' = m^2 + 1 > 0$ với mọi $m$ nên luôn có 2 nghiệm phân biệt.\nb) Áp dụng định lí Viète giải phương trình theo $m$."
                ),
                make_essay(3, "Vận dụng", 0.5,
                    f"Cho đường tròn $(O; R)$ và điểm $A$ nằm ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với đường tròn ($B, C$ là các tiếp điểm).\n a) Chứng minh tứ giác $ABOC$ là tứ giác nội tiếp đường tròn.\n b) Xác định tâm và đường kính của đường tròn ngoại tiếp tứ giác $ABOC$.",
                    "a) Do $AB, AC$ là tiếp tuyến nên $\\widehat{ABO} = \\widehat{ACO} = 90^\\circ \\Rightarrow \\widehat{ABO} + \\widehat{ACO} = 180^\\circ$, tứ giác nội tiếp (0.25đ)\nb) Tâm đường tròn ngoại tiếp là trung điểm của đoạn thẳng $OA$, đường kính là đoạn thẳng $OA$ (0.25đ)",
                    "a) Tứ giác có tổng hai góc đối bằng $180^\\circ$ nên nội tiếp.\nb) Tâm là trung điểm của $OA$, đường kính bằng $OA$."
                ),
                make_essay(4, "Vận dụng cao", 0.5,
                    f"Cho phương trình $x^2 - 2(m - 1)x + 2m - 5 = 0$. Tìm giá trị nhỏ nhất của biểu thức $A = x_1^2 + x_2^2 + {t_idx}$ khi $m$ thay đổi.",
                    f"$\\Delta' = (m-1)^2 - (2m - 5) = m^2 - 4m + 6 = (m-2)^2 + 2 > 0$ với mọi $m$ (0.1đ)\n$A = (x_1+x_2)^2 - 2x_1 x_2 + {t_idx} = 4(m-1)^2 - 2(2m-5) + {t_idx} = 4m^2 - 12m + 14 + {t_idx} = (2m - 3)^2 + 5 + {t_idx} \\ge 5 + {t_idx}$ (0.25đ)\nDấu '=' xảy ra khi $m = 3/2$. Vậy $\\min A = 5 + {t_idx}$ (0.15đ)",
                    f"Biến đổi biểu thức $A$ thành dạng bình phương cộng hằng số, tìm được $\\min A = 5 + {t_idx}$ khi $m = 1,5$."
                )
            ]
        })

    return exams

# ==============================================================================
# 6 MÃ ĐỀ CUỐI KỲ 2 - TOÁN 9 (final2)
# Phạm vi: Toàn bộ HK2: PT bậc hai & Viète, Thống kê, Xác suất, Tứ giác nội tiếp, Hình trụ - nón - cầu
# ==============================================================================
def generate_g9_final2():
    exams = []
    
    for t_idx in range(1, 7):
        ex_num = f"0{t_idx}"
        topics = [
            "Hình trụ - Nón - Cầu, Tứ giác nội tiếp, Bảng tần số & Viète ôn thi vào lớp 10",
            "Thể tích hình nón thực tế, Độ dài cung tròn, Tần số tương đối & Parabol tương giao",
            "Diện tích mặt cầu, Tiếp tuyến chung đường tròn, Xác suất thực nghiệm & Giải toán lập PT",
            "Hình trụ đựng nước, Cung tròn quạt tròn, Biểu đồ tần số ghép nhóm & Cực trị đại số",
            "Mô hình nón cụt / quả cầu trong đời sống, Đa giác đều & Phương trình chứa tham số m",
            "Đề thi thử tổng hợp toàn diện cấu trúc Tuyển sinh vào Lớp 10 THPT môn Toán"
        ]
        topic = topics[t_idx - 1]

        exams.append({
            "id": f"p_g9_final2_{ex_num}",
            "testNum": t_idx,
            "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KỲ II - TOÁN 9 (ĐỀ SỐ {ex_num})",
            "topic": topic,
            "grade": "9",
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
                make_mc(1, "Nhận biết", "Công thức tính thể tích của hình trụ có bán kính đáy $R$ và chiều cao $h$ là:", ["$V = \\pi R^2 h$", "$V = \\frac{1}{3} \\pi R^2 h$", "$V = 2\\pi R h$", "$V = \\frac{4}{3}\\pi R^3$"], 0, "Thể tích hình trụ là $V = \\pi R^2 h$."),
                make_mc(2, "Nhận biết", "Diện tích mặt cầu bán kính $R$ được tính theo công thức:", ["$S = 4\\pi R^2$", "$S = \\frac{4}{3}\\pi R^3$", "$S = 2\\pi R^2$", "$S = \\pi R^2$"], 0, "Diện tích mặt cầu $S = 4\\pi R^2$."),
                make_mc(3, "Nhận biết", "Tần số tương đối $f_i$ của một giá trị $x_i$ trong mẫu số liệu cỡ $N$ có tần số $n_i$ được tính bằng:", ["$f_i = \\frac{n_i}{N}$", "$f_i = \\frac{N}{n_i}$", "$f_i = n_i \\cdot N$", "$f_i = n_i - N$"], 0, "Tần số tương đối bằng tần số chia cho kích thước mẫu $N$."),
                make_mc(4, "Thông hiểu", f"Một hình nón có bán kính đáy $R = 3\\,\\text{{cm}}$ và đường sinh $l = {4 + t_idx}\\,\\text{{cm}}$. Diện tích xung quanh của hình nón là:", [f"${3 * (4 + t_idx)}\\pi\\,\\text{{cm}}^2$", f"${6 * (4 + t_idx)}\\pi\\,\\text{{cm}}^2$", "$12\\pi\\,\\text{cm}^2$", "$24\\pi\\,\\text{cm}^2$"], 0, f"$S_{{xq}} = \\pi R l = \\pi \\cdot 3 \\cdot ({4+t_idx}) = {3*(4+t_idx)}\\pi\\,\\text{{cm}}^2$."),
                make_mc(5, "Thông hiểu", f"Một quả bóng bàn có dạng hình cầu với bán kính $R = 2\\,\\text{{cm}}$. Thể tích của quả bóng bàn đó là:", ["$\\frac{32}{3}\\pi\\,\\text{cm}^3$", "$\\frac{16}{3}\\pi\\,\\text{cm}^3$", "$16\\pi\\,\\text{cm}^3$", "$8\\pi\\,\\text{cm}^3$"], 0, "$V = \\frac{4}{3} \\pi R^3 = \\frac{4}{3} \\pi \\cdot 8 = \\frac{32}{3}\\pi\\,\\text{cm}^3$."),
                make_mc(6, "Thông hiểu", "Cho đường tròn $(O; 4\\,\\text{cm})$. Độ dài cung tròn $90^\\circ$ của đường tròn này bằng:", ["$2\\pi\\,\\text{cm}$", "$4\\pi\\,\\text{cm}$", "$\\pi\\,\\text{cm}$", "$8\\pi\\,\\text{cm}$"], 0, "$l = \\frac{\\pi R n}{180} = \\frac{\\pi \\cdot 4 \\cdot 90}{180} = 2\\pi\\,\\text{cm}$."),
                make_mc(7, "Vận dụng", f"Một chiếc thùng hình trụ có bán kính đáy $R = 0,{t_idx}\\,\\text{{m}}$ và chiều cao $h = 1\\,\\text{{m}}$. Dung tích chứa nước tối đa của thùng là:", [f"$\\pi \\cdot {(t_idx/10)**2:.3f}\\,\\text{{m}}^3$".rstrip("0").rstrip("."), "1 m³", "2 m³", "0.5 m³"], 0, f"$V = \\pi R^2 h = \\pi \\cdot ({t_idx}/10)^2 \\cdot 1$ m³."),
                make_mc(8, "Vận dụng", f"Gieo ngẫu nhiên đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm xuất hiện trên hai con xúc xắc bằng 7 là:", ["$\\frac{1}{6}$", "$\\frac{1}{12}$", "$\\frac{7}{36}$", "$\\frac{1}{36}$"], 0, "Có 6 cặp có tổng bằng 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) trong 36 kết quả. Xác suất: 6/36 = 1/6."),
                make_mc(9, "Vận dụng cao", f"Một chiếc nón lá có dạng hình nón với đường kính đáy $40\\,\\text{{cm}}$ và chiều cao $20\\,\\text{{cm}}$. Diện tích lá cần dùng để phủ kín mặt xung quanh nón (lấy $\\pi \\approx 3,14$, làm tròn đến hàng đơn vị $\\text{{cm}}^2$) là:", [f"$\\approx {int(3.14 * 20 * (20**2 + 20**2)**0.5)}\\,\\text{{cm}}^2$", "1000 cm²", "1500 cm²", "2000 cm²"], 0, "Bán kính đáy $R = 20\\,\\text{cm}$. Đường sinh $l = \\sqrt{20^2 + 20^2} = 20\\sqrt{2}\\,\\text{cm}$. Diện tích xung quanh: $\\pi R l$."),
                make_mc(10, "Vận dụng cao", f"Cho phương trình $x^2 - {2 * t_idx}x + {t_idx**2 - 4} = 0$. Hai nghiệm của phương trình là:", [f"$x_1 = {t_idx - 2}, x_2 = {t_idx + 2}$", f"$x_1 = {t_idx}, x_2 = 4$", "$x = \\pm 2$", "Vô nghiệm"], 0, f"$\\Delta' = {t_idx**2} - ({t_idx**2 - 4}) = 4 \\Rightarrow x = {t_idx} \\pm 2$."),
                make_mc(11, "Vận dụng cao", "Một hình quạt tròn có bán kính $R = 6\\,\\text{cm}$ và diện tích bằng $6\\pi\\,\\text{cm}^2$. Số đo cung của hình quạt tròn đó là:", ["$60^\\circ$", "$90^\\circ$", "$45^\\circ$", "$120^\\circ$"], 0, "$S = \\frac{\\pi R^2 n}{360} \\Rightarrow 6\\pi = \\frac{36\\pi n}{360} = \\frac{\\pi n}{10} \\Rightarrow n = 60^\\circ$."),
                make_mc(12, "Vận dụng cao", f"Cho phương trình $x^2 - 2x - {t_idx} = 0$ có hai nghiệm $x_1, x_2$. Giá trị của biểu thức $K = x_1^3 + x_2^3$ bằng:", [f"${8 + 3 * 2 * t_idx}$", f"${8 - 6 * t_idx}$", "$8$", "$12$"], 0, "$x_1 + x_2 = 2, x_1 x_2 = -t_idx$. $K = (x_1+x_2)^3 - 3x_1 x_2(x_1+x_2) = 8 - 3(-t_idx)(2) = 8 + 6t_idx$.")
            ],
            "part2": [
                make_tf(1, f"Một lon sữa bò hình trụ có bán kính đáy $R = 3,5\\,\\text{{cm}}$ và chiều cao $h = 8\\,\\text{{cm}}$. Lấy $\\pi \\approx \\frac{{22}}{{7}}$.", [
                    {"id": "a", "text": "Diện tích đáy của lon sữa bằng $38,5\\,\\text{cm}^2$.", "correct": True, "level": "Nhận biết", "explanation": "S_day = (22/7) * 3,5² = 38,5 cm²."},
                    {"id": "b", "text": "Chu vi đáy của lon sữa bằng $22\\,\\text{cm}$.", "correct": True, "level": "Nhận biết", "explanation": "C = 2 * (22/7) * 3,5 = 22 cm."},
                    {"id": "c", "text": "Diện tích xung quanh của lon sữa bằng $176\\,\\text{cm}^2$.", "correct": True, "level": "Thông hiểu", "explanation": "S_xq = C * h = 22 * 8 = 176 cm²."},
                    {"id": "d", "text": "Thể tích lon sữa chứa được hơn $350\\,\\text{cm}^3$ chất lỏng.", "correct": False, "level": "Vận dụng", "explanation": "V = 38,5 * 8 = 308 cm³ < 350 cm³."}
                ]),
                make_tf(2, f"Cho tứ giác $ABCD$ nội tiếp đường tròn $(O; R)$ có $\\widehat{{ABC}} = 110^\\circ$ và $\\widehat{{BCD}} = 80^\\circ$.", [
                    {"id": "a", "text": "Tổng số đo bốn góc trong một tứ giác luôn bằng $360^\\circ$.", "correct": True, "level": "Nhận biết", "explanation": "Tổng 4 góc tứ giác bằng 360 độ."},
                    {"id": "b", "text": "Số đo góc $\\widehat{ADC}$ bằng $70^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Tứ giác nội tiếp: góc D đối diện góc B nên D = 180 - 110 = 70 độ."},
                    {"id": "c", "text": "Số đo góc $\\widehat{BAD}$ bằng $100^\\circ$.", "correct": True, "level": "Thông hiểu", "explanation": "Góc A đối diện góc C nên A = 180 - 80 = 100 độ."},
                    {"id": "d", "text": "Tứ giác $ABCD$ chắc chắn là một hình thang cân.", "correct": False, "level": "Vận dụng", "explanation": "Hai góc kề một đáy B và C không bằng nhau (110 != 80) và các cặp góc đối bù nhau không đủ để kết luận là thang cân."}
                ])
            ],
            "part3": [
                make_sa(1, "Nhận biết", "Một hình trụ có bán kính đáy bằng $5\\,\\text{cm}$ và chiều cao $h = 10\\,\\text{cm}$. Tính diện tích xung quanh theo $\\pi$ (nhập hệ số trước $\\pi$):", "100", ["100"], "$S_{xq} = 2\\pi R h = 2\\pi \\cdot 5 \\cdot 10 = 100\\pi$."),
                make_sa(2, "Thông hiểu", f"Tính thể tích hình cầu có bán kính $R = 3\\,\\text{{cm}}$ theo $\\pi$ (nhập hệ số trước $\\pi$):", "36", ["36"], "$V = \\frac{4}{3}\\pi R^3 = \\frac{4}{3} \\cdot 27 \\cdot \\pi = 36\\pi$."),
                make_sa(3, "Vận dụng", f"Một nhóm gồm 40 học sinh làm bài kiểm tra: có 10 bạn đạt 9 điểm, 15 bạn đạt 8 điểm, {10 + t_idx} bạn đạt 7 điểm, số còn lại đạt 6 điểm. Tần số tương đối của học sinh đạt 8 điểm là bao nhiêu phần trăm (nhập số %)?", "37.5", ["37.5", "37,5", "37.5%"], "Tần số tương đối = 15 / 40 = 37,5%."),
                make_sa(4, "Vận dụng cao", f"Cho hình nón có chiều cao $h = 4\\,\\text{{cm}}$ và thể tích $V = 12\\pi\\,\\text{{cm}}^3$. Tính độ dài đường sinh $l$ của hình nón (theo cm):", "5", ["5", "5 cm"], "$V = \\frac{1}{3}\\pi R^2 h \\Rightarrow 12\\pi = \\frac{4}{3}\\pi R^2 \\Rightarrow R^2 = 9 \\Rightarrow R = 3\\,\\text{cm}$. Đường sinh $l = \\sqrt{R^2 + h^2} = \\sqrt{9 + 16} = 5\\,\\text{cm}$.")
            ],
            "part4": [
                make_essay(1, "Nhận biết", 1.0,
                    f"Thực hiện các yêu cầu sau:\n a) Tính diện tích toàn phần của hình trụ có bán kính đáy $R = 3\\,\\text{{cm}}$ và chiều cao $h = 7\\,\\text{{cm}}$ (theo $\\pi$).\n b) Giải phương trình bậc hai: $x^2 - {2 * t_idx}x + {t_idx**2 - 1} = 0$.",
                    f"a) $S_{{tp}} = 2\\pi R h + 2\\pi R^2 = 2\\pi(3)(7) + 2\\pi(9) = 42\\pi + 18\\pi = 60\\pi\\,\\text{{cm}}^2$ (0.5đ)\nb) $\\Delta' = {t_idx**2} - ({t_idx**2 - 1}) = 1 \\Rightarrow x = {t_idx} \\pm 1$ (0.5đ)",
                    f"a) $S_{{tp}} = 60\\pi\\,\\text{{cm}}^2$.\nb) Phương trình có hai nghiệm $x_1 = {t_idx - 1}, x_2 = {t_idx + 1}$."
                ),
                make_essay(2, "Thông hiểu", 1.0,
                    f"Giải bài toán bằng cách lập hệ phương trình hoặc phương trình bậc hai:\nMột mảnh đất hình chữ nhật có chu vi bằng ${28 * t_idx}\\,\\text{{m}}$. Nếu tăng chiều rộng thêm $2\\,\\text{{m}}$ và giảm chiều dài đi $2\\,\\text{{m}}$ thì diện tích mảnh đất tăng thêm ${12 * t_idx}\\,\\text{{m}}^2$.\n a) Gọi chiều rộng và chiều dài mảnh đất lần lượt là $x$ và $y$ ($y > x > 0$). Viết phương trình liên hệ giữa $x$ và $y$ từ chu vi.\n b) Lập phương trình thứ hai về diện tích và tính kích thước ban đầu của mảnh đất.",
                    f"a) Nửa chu vi: $x + y = {14*t_idx}$ (0.5đ)\nb) $(x + 2)(y - 2) - xy = {12*t_idx} \\Rightarrow xy - 2x + 2y - 4 - xy = {12*t_idx} \\Rightarrow 2(y - x) = {12*t_idx + 4} \\Rightarrow y - x = {6*t_idx + 2}$. Giải hệ tìm được $x, y$ (0.5đ)",
                    "a) Phương trình chu vi: $x + y = 14$.\nb) Lập phương trình hiệu diện tích và giải hệ phương trình bậc nhất hai ẩn."
                ),
                make_essay(3, "Vận dụng", 0.5,
                    f"Cho đường tròn $(O; R)$ và dây cung $BC$ không đi qua tâm. Lấy điểm $A$ trên cung lớn $BC$. Kẻ đường cao $AD$ của tam giác $ABC$ và đường kính $AK$ của đường tròn $(O)$.\n a) Chứng minh tam giác $ABD$ đồng dạng với tam giác $AKC$.\n b) Chứng minh hệ thức $AB \\cdot AC = AD \\cdot AK$.",
                    "a) Xét $\\Delta ABD$ và $\\Delta AKC$ có $\\widehat{ADB} = \\widehat{ACK} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn), $\\widehat{ABD} = \\widehat{AKC}$ (hai góc nội tiếp cùng chắn cung $AC$). Suy ra $\\Delta ABD \\backsim \\Delta AKC$ (g.g) (0.25đ)\nb) Từ đồng dạng: $\\frac{AB}{AK} = \\frac{AD}{AC} \\Rightarrow AB \\cdot AC = AD \\cdot AK$ (0.25đ)",
                    "a) Chứng minh đồng dạng qua góc nội tiếp chắn nửa đường tròn.\nb) Suy ra tích các cạnh đối ứng."
                ),
                make_essay(4, "Vận dụng cao", 0.5,
                    f"Cho các số thực dương $x, y$ thỏa mãn $x + y = 1$. Tìm giá trị nhỏ nhất của biểu thức $P = \\frac{{1}}{{x^2 + y^2}} + \\frac{{1}}{{2xy}} + {t_idx}$.",
                    f"Áp dụng BĐT Cauchy-Schwarz: $\\frac{{1}}{{x^2 + y^2}} + \\frac{{1}}{{2xy}} \\ge \\frac{{4}}{{x^2 + y^2 + 2xy}} = \\frac{{4}}{{(x+y)^2}} = 4$ (0.25đ)\nSuy ra $P \\ge 4 + {t_idx}$. Dấu '=' xảy ra khi $x^2 + y^2 = 2xy \\Leftrightarrow x = y = 1/2$. Vậy $\\min P = 4 + {t_idx}$ (0.25đ)",
                    f"Sử dụng bất đẳng thức $\\frac{{1}}{{a}} + \\frac{{1}}{{b}} \\ge \\frac{{4}}{{a+b}}$, đạt giá trị nhỏ nhất là $4 + {t_idx}$ khi $x = y = 0,5$."
                )
            ]
        })

    return exams

def main():
    print("=== SINH VÀ KIỂM TRA ĐỀ ĐỊNH KỲ TOÁN 9 ===")
    mid2_exams = generate_g9_mid2()
    final2_exams = generate_g9_final2()

    assert len(mid2_exams) == 6, f"Thiếu đề mid2: {len(mid2_exams)} != 6"
    assert len(final2_exams) == 6, f"Thiếu đề final2: {len(final2_exams)} != 6"

    for idx, ex in enumerate(mid2_exams, 1):
        validate_periodic_exam(ex, "9", "mid2", idx)
        print(f"✅ Toán 9 - Giữa kỳ 2 (Đề {idx}): ĐẠT CHUẨN MA TRẬN 100%.")

    for idx, ex in enumerate(final2_exams, 1):
        validate_periodic_exam(ex, "9", "final2", idx)
        print(f"✅ Toán 9 - Cuối kỳ 2 (Đề {idx}): ĐẠT CHUẨN MA TRẬN 100%.")

    print("🎉 Hoàn thành xuất sắc 12 đề định kỳ Toán 9!")
    return mid2_exams, final2_exams

if __name__ == "__main__":
    main()
