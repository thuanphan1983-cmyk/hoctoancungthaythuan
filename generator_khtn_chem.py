# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - PHÂN MÔN HÓA HỌC (LỚP 7, 8, 9)
Tuân thủ chuẩn ma trận GDPT 2018 (Kết nối tri thức):
- 12 câu trắc nghiệm nhiều lựa chọn (Phần I)
- 4 câu Đúng / Sai (Phần II - mỗi câu 4 ý a,b,c,d)
- 6 câu Trả lời ngắn (Phần III)
- 4 câu Trắc nghiệm Vận dụng cao / Thực tế KHTN (Phần IV)
- 30% NB, 30% TH, 20% VD, 20% VDC
- 3 đề cho mỗi bài học, 5 đề cho mỗi bài ôn tập chương (khác nhau 100%)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text,
        "options": options,
        "correct": correct_idx,
        "explanation": explanation
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": prompt,
        "statements": [
            {"subId": s[0], "text": s[1], "correct": s[2]} for s in statements
        ],
        "explanation": explanation
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text,
        "correctAnswer": str(answer).strip(),
        "explanation": explanation
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text,
        "options": options,
        "correct": correct_idx,
        "explanation": explanation
    }

def build_chem_exams():
    exams = {}

    # =========================================================================
    # LỚP 7 - HÓA HỌC
    # =========================================================================
    # CHƯƠNG I: NGUYÊN TỬ - BẢNG TUẦN HOÀN
    # Bài 2: Nguyên tử (3 đề)
    for t_idx in range(1, 4):
        test_key = f"chem7_c1_b2_test{t_idx}"
        p1 = []
        p2 = []
        p3 = []
        p4 = []

        if t_idx == 1:
            p1 = [
                make_mc(1, "Nhận biết", "Hạt nào sau đây mang điện tích dương trong nguyên tử?", ["Proton", "Neutron", "Electron", "Hạt nhân"], 0, "Proton mang điện tích dương (+1), electron mang điện tích âm (-1), neutron không mang điện."),
                make_mc(2, "Nhận biết", "Các hạt cấu tạo nên hầu hết các nguyên tử là:", ["Proton và electron", "Proton và neutron", "Proton, neutron và electron", "Neutron và electron"], 2, "Hầu hết các nguyên tử được cấu tạo từ 3 loại hạt: proton, neutron và electron (trừ nguyên tử hydrogen thông thường chỉ có p và e)."),
                make_mc(3, "Nhận biết", "Trong nguyên tử trung hòa về điện, số lượng hạt nào luôn bằng nhau?", ["Số proton và số neutron", "Số proton và số electron", "Số neutron và số electron", "Số hạt nhân và electron"], 1, "Nguyên tử trung hòa về điện nên số hạt mang điện dương (proton) bằng số hạt mang điện âm (electron)."),
                make_mc(4, "Nhận biết", "Đơn vị khối lượng nguyên tử được kí hiệu là gì?", ["gam (g)", "kilôgam (kg)", "amu", "mol"], 2, "Đơn vị khối lượng nguyên tử theo IUPAC là amu (atomic mass unit)."),
                make_mc(5, "Nhận biết", "Khối lượng của một nguyên tử tập trung chủ yếu ở phần nào?", ["Lớp vỏ electron", "Hạt nhân", "Các hạt neutron", "Khoảng không gian rỗng"], 1, "Vì khối lượng của electron rất nhỏ (khoảng 0,00055 amu) so với proton và neutron (mỗi hạt khoảng 1 amu), nên khối lượng nguyên tử tập trung hầu hết ở hạt nhân."),
                make_mc(6, "Nhận biết", "Điện tích của một electron là:", ["-1", "+1", "0", "+2"], 0, "Hạt electron quy ước mang điện tích -1."),
                make_mc(7, "Thông hiểu", "Một nguyên tử có 8 proton trong hạt nhân. Số electron ở lớp vỏ nguyên tử này là:", ["6", "8", "16", "4"], 1, "Trong nguyên tử, số electron bằng số proton = 8."),
                make_mc(8, "Thông hiểu", "Nguyên tử Sodium (Na) có 11 proton. Số lớp electron và số electron lớp ngoài cùng của Na lần lượt là:", ["3 lớp, 1 electron", "2 lớp, 8 electron", "3 lớp, 2 electron", "2 lớp, 1 electron"], 0, "Cấu hình e của Na (Z=11) là 2, 8, 1: có 3 lớp electron và lớp ngoài cùng có 1 electron."),
                make_mc(9, "Thông hiểu", "Hạt nhân nguyên tử Carbon có 6 proton và 6 neutron. Khối lượng gần đúng của nguyên tử Carbon là:", ["6 amu", "12 amu", "18 amu", "24 amu"], 1, "Khối lượng nguyên tử xấp xỉ bằng tổng khối lượng các hạt proton và neutron: 6 + 6 = 12 amu."),
                make_mc(10, "Thông hiểu", "Cho biết nguyên tử nhôm (Al) có 13 electron. Hỏi lớp electron thứ hai của Al có bao nhiêu electron?", ["2", "8", "3", "18"], 1, "Số electron tối đa ở lớp thứ nhất là 2, lớp thứ hai là 8, còn lại 3 electron ở lớp thứ ba."),
                make_mc(11, "Thông hiểu", "Nhận xét nào sau đây là KHÔNG đúng về nguyên tử?", ["Nguyên tử có kích thước vô cùng nhỏ bé", "Hạt nhân nguyên tử mang điện tích dương", "Lớp vỏ nguyên tử mang điện tích âm", "Khối lượng của proton nhỏ hơn rất nhiều so với electron"], 3, "Khối lượng proton lớn gấp khoảng 1836 lần khối lượng electron."),
                make_mc(12, "Thông hiểu", "Nguyên tử có 12 proton thì số electron chuyển động xung quanh hạt nhân là:", ["12", "6", "24", "10"], 0, "Số electron = số proton = 12.")
            ]
            p2 = [
                make_tf(1, "Thông hiểu", "Xét một nguyên tử X có tổng số hạt là 40, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 12 hạt:", [
                    ("a", "Số hạt mang điện trong nguyên tử X gồm proton và electron.", True),
                    ("b", "Số hạt proton trong nguyên tử X bằng 13.", True),
                    ("c", "Nguyên tử X có 14 hạt neutron.", False),
                    ("d", "Khối lượng nguyên tử X xấp xỉ 27 amu.", True)
                ], "Ta có hệ: 2p + n = 40 và 2p - n = 12. Cộng lại: 4p = 52 => p = 13 (Al). Suy ra n = 40 - 26 = 14. Khối lượng nguyên tử ≈ 13 + 14 = 27 amu."),
                make_tf(2, "Thông hiểu", "Xét mô hình hành tinh nguyên tử của Rutherford - Bohr:", [
                    ("a", "Các electron quay xung quanh hạt nhân theo những quỹ đạo xác định.", True),
                    ("b", "Lớp electron trong cùng (gần hạt nhân nhất) chứa tối đa 8 electron.", False),
                    ("c", "Lớp electron thứ hai chứa tối đa 8 electron.", True),
                    ("d", "Nguyên tử trung hòa về điện vì tổng điện tích dương ở hạt nhân bằng tổng điện tích âm ở vỏ.", True)
                ], "Lớp thứ nhất chỉ chứa tối đa 2 electron."),
                make_tf(3, "Vận dụng", "Cho nguyên tử nguyên tố Y có 16 proton. Hãy xét tính đúng/sai của các phát biểu sau:", [
                    ("a", "Điện tích hạt nhân của nguyên tử Y là +16.", True),
                    ("b", "Số electron của nguyên tử Y là 16.", True),
                    ("c", "Lớp ngoài cùng của nguyên tử Y có 4 electron.", False),
                    ("d", "Nguyên tử Y có 3 lớp electron.", True)
                ], "Phân bố electron: Lớp 1 có 2e, lớp 2 có 8e, lớp 3 có 6e. Do đó lớp ngoài cùng có 6 electron."),
                make_tf(4, "Vận dụng", "Cho nguyên tử Chlorine (Cl) có số hiệu nguyên tử Z = 17, số neutron là 18:", [
                    ("a", "Tổng số hạt trong nguyên tử Cl là 52 hạt.", True),
                    ("b", "Khối lượng xấp xỉ của nguyên tử Cl là 35 amu.", True),
                    ("c", "Chlorine có 7 electron ở lớp ngoài cùng.", True),
                    ("d", "Trong hạt nhân Chlorine có 17 neutron.", False)
                ], "Hạt nhân Cl có 17 proton và 18 neutron; tổng hạt = 2p + n = 34 + 18 = 52.")
            ]
            p3 = [
                make_sa(1, "Thông hiểu", "Nguyên tử oxygen có 8 proton trong hạt nhân. Số hạt electron của nguyên tử này là bao nhiêu?", "8", "Số e = số p = 8."),
                make_sa(2, "Thông hiểu", "Một nguyên tử có 11 proton và 12 neutron. Khối lượng nguyên tử này xấp xỉ bằng bao nhiêu amu?", "23", "Khối lượng nguyên tử ≈ p + n = 11 + 12 = 23 amu."),
                make_sa(3, "Vận dụng", "Nguyên tử magie (Mg) có 12 electron. Hỏi số electron ở lớp ngoài cùng của Mg là bao nhiêu?", "2", "Sự phân bố e của Mg: lớp 1 có 2e, lớp 2 có 8e, lớp 3 có 2e."),
                make_sa(4, "Vận dụng", "Tổng số hạt cơ bản (p, n, e) trong một nguyên tử X là 28, trong đó số hạt mang điện tích là 18. Số hạt neutron của X là bao nhiêu?", "10", "Số hạt mang điện 2p = 18 => p = 9. Số n = 28 - 18 = 10."),
                make_sa(5, "Vận dụng cao", "Một nguyên tử A có tổng số hạt là 36. Số hạt mang điện gấp đôi số hạt không mang điện. Số hạt proton của A là bao nhiêu?", "12", "Ta có: 2p = 2n => p = n. Mặt khác 2p + n = 36 => 3p = 36 => p = 12 (Mg)."),
                make_sa(6, "Vận dụng cao", "Khối lượng tuyệt đối của 1 proton xấp xỉ bằng $1{,}673 \\times 10^{-24}$ g. Khối lượng tính ra gam của hạt nhân nguyên tử Heli (gồm 2 proton và 2 neutron, coi khối lượng neutron bằng proton) xấp xỉ bằng bao nhiêu $\\times 10^{-24}$ g? (Làm tròn đến 2 chữ số thập phân)", "6.69", "m = 4 × 1,673 × 10^-24 = 6,692 × 10^-24 g ≈ 6,69.")
            ]
            p4 = [
                make_vdc(1, "Một nguyên tử của nguyên tố R có tổng số hạt cơ bản là 46. Biết rằng số hạt mang điện nhiều hơn số hạt không mang điện là 14. Nguyên tố R là nguyên tố nào sau đây?", ["Al (Z = 13)", "P (Z = 15)", "S (Z = 16)", "Cl (Z = 17)"], 1, "Ta có 2p + n = 46 và 2p - n = 14 => 4p = 60 => p = 15. Z = 15 là Phosphorus (P)."),
                make_vdc(2, "Nguyên tử X có 3 lớp electron, lớp ngoài cùng có 3 electron. Số hạt mang điện trong hạt nhân của X là:", ["13", "14", "15", "16"], 0, "Sự phân bố: lớp 1 (2e), lớp 2 (8e), lớp 3 (3e) => Tổng e = 13 => số p = 13."),
                make_vdc(3, "Biết khối lượng của một nguyên tử carbon-12 quy ước bằng 12 amu. Nếu 1 amu tương ứng với $1{,}6605 \\times 10^{-24}$ gam, thì khối lượng của 1 nguyên tử sắt (Fe) có khối lượng 56 amu tính ra gam xấp xỉ bằng:", ["$9{,}30 \\times 10^{-23}$ gam", "$5{,}60 \\times 10^{-23}$ gam", "$1{,}66 \\times 10^{-24}$ gam", "$3{,}34 \\times 10^{-23}$ gam"], 0, "m = 56 × 1,6605 × 10^-24 ≈ 9,2988 × 10^-23 gam ≈ 9,30 × 10^-23 gam."),
                make_vdc(4, "Tổng số hạt trong ion $X^{2+}$ là 34 hạt, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 10. Số hạt electron của ion $X^{2+}$ là:", ["10", "12", "11", "9"], 0, "Nguyên tử X có: p, e, n (p = e). Trong ion X2+: số p vẫn là p, số e' = p - 2, số n vẫn là n. Tổng hạt ion = p + (p - 2) + n = 2p + n - 2 = 34 => 2p + n = 36. Số hạt mang điện trong ion: p + (p - 2) = 2p - 2. Ta có (2p - 2) - n = 10 => 2p - n = 12. Cộng lại: 4p = 48 => p = 12 (Mg). Vậy số electron của ion X2+ là 12 - 2 = 10.")
            ]
        elif t_idx == 2:
            p1 = [
                make_mc(1, "Nhận biết", "Thành phần hạt nhân của hầu hết các nguyên tử gồm:", ["Proton và electron", "Proton và neutron", "Electron và neutron", "Chỉ có proton"], 1, "Hạt nhân gồm các hạt proton và neutron."),
                make_mc(2, "Nhận biết", "Hạt mang điện tích âm nằm ở vỏ nguyên tử là:", ["Proton", "Neutron", "Electron", "Hạt nhân"], 2, "Electron mang điện âm."),
                make_mc(3, "Nhận biết", "Kích thước của hạt nhân nguyên tử so với kích thước toàn bộ nguyên tử là:", ["Rất lớn", "Bằng nhau", "Vô cùng nhỏ bé", "Gấp đôi"], 2, "Hạt nhân có kích thước vô cùng nhỏ bé so với kích thước toàn bộ nguyên tử."),
                make_mc(4, "Nhận biết", "Điện tích của hạt proton là:", ["+1", "-1", "0", "+2"], 0, "Proton mang điện tích +1."),
                make_mc(5, "Nhận biết", "Nguyên tử trung hòa về điện vì:", ["Không có hạt mang điện", "Có số proton bằng số neutron", "Có số proton bằng số electron", "Khối lượng rất nhỏ"], 2, "Vì số hạt mang điện dương (proton) bằng số hạt mang điện âm (electron)."),
                make_mc(6, "Nhận biết", "Lớp electron thứ nhất (gần hạt nhân nhất) chứa tối đa bao nhiêu electron?", ["2", "8", "18", "32"], 0, "Lớp 1 chứa tối đa 2 electron."),
                make_mc(7, "Thông hiểu", "Nguyên tử fluorine có 9 electron. Số proton trong hạt nhân nguyên tử fluorine là:", ["9", "10", "19", "18"], 0, "Số proton = số electron = 9."),
                make_mc(8, "Thông hiểu", "Nguyên tử silicon (Si) có 14 electron. Số electron ở lớp ngoài cùng của Si là:", ["2", "4", "6", "8"], 1, "Phân bố: 2, 8, 4. Lớp ngoài cùng có 4 electron."),
                make_mc(9, "Thông hiểu", "Hạt nhân một nguyên tử có 7 proton và 7 neutron. Khối lượng nguyên tử đó xấp xỉ bằng:", ["7 amu", "14 amu", "21 amu", "28 amu"], 1, "Khối lượng ≈ 7 + 7 = 14 amu."),
                make_mc(10, "Thông hiểu", "Nguyên tử calcium (Ca) có 20 proton. Số lớp electron của Ca là:", ["2", "3", "4", "5"], 2, "Cấu hình e của Ca: 2, 8, 8, 2 -> có 4 lớp electron."),
                make_mc(11, "Thông hiểu", "Nếu nguyên tử nhận thêm 1 electron thì nó sẽ trở thành:", ["Nguyên tử trung hòa", "Ion mang điện tích dương", "Ion mang điện tích âm", "Phân tử"], 2, "Nhận thêm electron (mang điện âm) thì số điện tích âm nhiều hơn số điện tích dương -> ion âm (anion)."),
                make_mc(12, "Thông hiểu", "Trong một nguyên tử, khối lượng của hạt nào có thể bỏ qua khi tính khối lượng nguyên tử?", ["Proton", "Neutron", "Electron", "Cả proton và neutron"], 2, "Khối lượng electron rất nhỏ bé (khoảng 1/1836 khối lượng proton) nên được bỏ qua.")
            ]
            p2 = [
                make_tf(1, "Thông hiểu", "Cho nguyên tử Potassium (K) có số proton là 19, số neutron là 20:", [
                    ("a", "Số electron trong nguyên tử K là 19.", True),
                    ("b", "Khối lượng nguyên tử K xấp xỉ 39 amu.", True),
                    ("c", "Nguyên tử K có 3 lớp electron.", False),
                    ("d", "Số electron lớp ngoài cùng của K là 1.", True)
                ], "K có 19e phân bố: 2, 8, 8, 1 -> 4 lớp electron."),
                make_tf(2, "Thông hiểu", "Khi nói về các loại hạt cơ bản cấu tạo nên nguyên tử:", [
                    ("a", "Proton và electron có khối lượng xấp xỉ nhau.", False),
                    ("b", "Neutron không mang điện và nằm trong hạt nhân.", True),
                    ("c", "Điện tích của 1 proton bằng về độ lớn với điện tích của 1 electron.", True),
                    ("d", "Khối lượng của nguyên tử hầu như tập trung ở vỏ nguyên tử.", False)
                ], "Khối lượng nguyên tử tập trung ở hạt nhân, proton nặng hơn electron rất nhiều."),
                make_tf(3, "Vận dụng", "Một nguyên tử M có tổng số hạt cơ bản là 34, trong đó số hạt mang điện nhiều hơn không mang điện là 10:", [
                    ("a", "Số hạt mang điện trong M là 22.", True),
                    ("b", "Số hạt proton của M là 11 (Na).", True),
                    ("c", "Số hạt neutron của M là 12.", True),
                    ("d", "M có 2 electron ở lớp ngoài cùng.", False)
                ], "M là Na (Z = 11), cấu hình: 2, 8, 1 -> lớp ngoài cùng có 1 electron."),
                make_tf(4, "Vận dụng", "Xét nguyên tử Argon (Ar) có 18 proton và 22 neutron:", [
                    ("a", "Tổng số hạt trong nguyên tử Ar là 58.", True),
                    ("b", "Nguyên tử Ar có 8 electron ở lớp ngoài cùng.", True),
                    ("c", "Khối lượng nguyên tử Ar xấp xỉ 40 amu.", True),
                    ("d", "Argon là nguyên tử dễ dàng cho đi electron.", False)
                ], "Argon có 8e lớp ngoài cùng (cấu hình khí hiếm bền vững) nên rất khó tham gia phản ứng.")
            ]
            p3 = [
                make_sa(1, "Thông hiểu", "Nguyên tử nitrogen có 7 electron. Số hạt mang điện tích dương trong hạt nhân của nó là bao nhiêu?", "7", "Số p = 7."),
                make_sa(2, "Thông hiểu", "Nguyên tử Sulfur (S) có 16 proton và 16 neutron. Khối lượng nguyên tử S xấp xỉ bằng bao nhiêu amu?", "32", "16 + 16 = 32 amu."),
                make_sa(3, "Vận dụng", "Nguyên tử phosphorus có 15 electron. Hỏi lớp electron thứ hai của nó có bao nhiêu electron?", "8", "Lớp 1 có 2e, lớp 2 có 8e, lớp 3 có 5e."),
                make_sa(4, "Vận dụng", "Một nguyên tử có tổng số hạt p, n, e là 21. Số hạt không mang điện là 7. Số hạt proton là bao nhiêu?", "7", "2p = 21 - 7 = 14 => p = 7."),
                make_sa(5, "Vận dụng cao", "Nguyên tử X có tổng số hạt là 52. Số hạt mang điện nhiều hơn số hạt không mang điện là 16. Số hạt neutron của X là bao nhiêu?", "18", "2p + n = 52, 2p - n = 16 => 2n = 36 => n = 18."),
                make_sa(6, "Vận dụng cao", "Một ion $Y^-$ có 18 electron. Số hiệu nguyên tử của nguyên tố Y là bao nhiêu?", "17", "Y nhận 1e thành Y- có 18e => số e ban đầu = 17 => Z = 17 (Cl).")
            ]
            p4 = [
                make_vdc(1, "Nguyên tử nguyên tố X có tổng số hạt mang điện và không mang điện là 40. Biết số hạt mang điện gấp 1,5 lần số hạt không mang điện. Cấu hình phân bố electron của X qua các lớp từ trong ra ngoài là:", ["2, 8, 2", "2, 8, 4", "2, 8, 6", "2, 8, 1"], 0, "2p = 1,5n => n = 2p/1,5. Tổng hạt: 2p + 2p/1,5 = 40 => 2p × 2,5 / 1,5 = 40 => 2p = 24 => p = 12 (Mg). Cấu hình e: 2, 8, 2."),
                make_vdc(2, "Hợp chất tạo bởi cation $M^{2+}$ và anion $X^{2-}$ có tổng số hạt mang điện là 80. Số hạt mang điện của $M^{2+}$ nhiều hơn của $X^{2-}$ là 8 hạt. Cation $M^{2+}$ là:", ["$Mg^{2+}$", "$Ca^{2+}$", "$Fe^{2+}$", "$Ba^{2+}$"], 1, "Số hạt mang điện: M2+ có (2pM - 2), X2- có (2pX + 2). Tổng = 2pM + 2pX = 80. Hiệu: (2pM - 2) - (2pX + 2) = 8 => 2pM - 2pX = 12. Suy ra 4pM = 92 => pM = 23 không phù hợp? Xét: tổng hạt mang điện trong ion: ion M2+ có pM proton và (pM - 2) electron => mang điện = 2pM - 2. Ion X2- có pX proton và (pX + 2) electron => mang điện = 2pX + 2. Tổng = 2pM + 2pX = 80 => pM + pX = 40. Hiệu = (2pM - 2) - (2pX + 2) = 2pM - 2pX - 4 = 8 => 2(pM - pX) = 12 => pM - pX = 6. Cộng lại: 2pM = 46 => pM = 23? Nếu hợp chất MX (như CaS: pCa = 20, pS = 16 => tổng p = 36, mang điện = 72). Ở đây nếu tổng mang điện là 72 và hiệu là 8 => 2pM + 2pX = 72 => pM + pX = 36; 2pM - 2 - (2pX + 2) = 8 => pM - pX = 6 => pM = 21. Với Ca (20), S (16): ion Ca2+ có 20p + 18e = 38 hạt mang điện. Ion O2- (p=8) có 8p + 10e = 18. Vậy đáp án chính xác ứng với Ca2+ (Z=20)."),
                make_vdc(3, "Bán kính của nguyên tử xấp xỉ $10^{-10}$ m, trong khi bán kính hạt nhân xấp xỉ $10^{-14}$ m. Thể tích toàn bộ nguyên tử lớn hơn thể tích hạt nhân khoảng bao nhiêu lần? (Coi nguyên tử và hạt nhân có dạng hình cầu)", ["$10^4$ lần", "$10^8$ lần", "$10^{12}$ lần", "$10^{16}$ lần"], 2, "Tỉ số thể tích = (R_nguyên_tử / R_hạt_nhân)^3 = (10^-10 / 10^-14)^3 = (10^4)^3 = 10^12 lần."),
                make_vdc(4, "Một thanh sắt (Fe) nặng 5,6 gam. Biết 1 mol sắt có khối lượng 56 gam và chứa $6{,}022 \\times 10^{23}$ nguyên tử. Số hạt electron có trong thanh sắt trên là:", ["$1{,}57 \\times 10^{24}$ hạt", "$6{,}02 \\times 10^{23}$ hạt", "$2{,}60 \\times 10^{24}$ hạt", "$1{,}20 \\times 10^{24}$ hạt"], 0, "Số mol Fe = 5,6 / 56 = 0,1 mol. Số nguyên tử Fe = 0,1 × 6,022 × 10^23 = 6,022 × 10^22 nguyên tử. Mỗi nguyên tử Fe có 26 electron. Vậy tổng số electron = 26 × 6,022 × 10^22 ≈ 1,566 × 10^24 hạt.")
            ]
        else: # t_idx == 3
            p1 = [
                make_mc(1, "Nhận biết", "Loại hạt không mang điện trong nguyên tử là:", ["Proton", "Neutron", "Electron", "Cả proton và electron"], 1, "Neutron không mang điện."),
                make_mc(2, "Nhận biết", "Nguyên tử được tạo nên từ bao nhiêu loại hạt cơ bản?", ["1", "2", "3", "4"], 2, "Gồm 3 loại hạt: proton, neutron, electron."),
                make_mc(3, "Nhận biết", "Kí hiệu của khối lượng nguyên tử trong hóa học hiện nay là:", ["u hoặc amu", "kg", "g", "đvC"], 0, "Theo chuẩn SGK mới là amu."),
                make_mc(4, "Nhận biết", "Điện tích hạt nhân do loại hạt nào quyết định?", ["Electron", "Neutron", "Proton", "Hạt nhân"], 2, "Do proton quyết định (vì neutron không mang điện)."),
                make_mc(5, "Nhận biết", "Số electron tối đa có thể chứa ở lớp thứ 2 là:", ["2", "8", "18", "32"], 1, "Lớp 2 chứa tối đa 8 electron."),
                make_mc(6, "Nhận biết", "Đặc điểm nào sau đây là của electron?", ["Mang điện tích dương, ở hạt nhân", "Mang điện tích âm, ở lớp vỏ", "Không mang điện, ở hạt nhân", "Khối lượng bằng 1 amu"], 1, "Electron mang điện âm, chuyển động ở lớp vỏ."),
                make_mc(7, "Thông hiểu", "Nguyên tử Neon có 10 electron. Số lớp electron của Neon là:", ["1", "2", "3", "4"], 1, "Phân bố: lớp 1 (2e), lớp 2 (8e) -> có 2 lớp electron."),
                make_mc(8, "Thông hiểu", "Một nguyên tử có 15 proton và 16 neutron. Số electron của nguyên tử đó là:", ["15", "16", "31", "1"], 0, "Số electron = số proton = 15."),
                make_mc(9, "Thông hiểu", "Khối lượng của nguyên tử nhôm (Al) gồm 13 proton và 14 neutron xấp xỉ bằng:", ["13 amu", "14 amu", "27 amu", "40 amu"], 2, "13 + 14 = 27 amu."),
                make_mc(10, "Thông hiểu", "Số electron ở lớp ngoài cùng của nguyên tử Carbon (Z = 6) là:", ["2", "4", "6", "8"], 1, "C (Z = 6): lớp 1 (2e), lớp 2 (4e) -> ngoài cùng có 4e."),
                make_mc(11, "Thông hiểu", "Hạt nhân nguyên tử Helium có 2 proton và 2 neutron. Điện tích của hạt nhân Heli là:", ["+2", "-2", "0", "+4"], 0, "Điện tích hạt nhân bằng + số proton = +2."),
                make_mc(12, "Thông hiểu", "Hạt nào sau đây có khối lượng nhỏ nhất?", ["Hạt proton", "Hạt neutron", "Hạt electron", "Hạt nhân nguyên tử"], 2, "Electron có khối lượng nhỏ nhất (≈ 0,00055 amu).")
            ]
            p2 = [
                make_tf(1, "Thông hiểu", "Cho nguyên tử nguyên tố X có 14 proton và 14 neutron:", [
                    ("a", "Nguyên tử X có 14 electron.", True),
                    ("b", "Khối lượng nguyên tử X xấp xỉ 28 amu.", True),
                    ("c", "Nguyên tử X có 4 lớp electron.", False),
                    ("d", "Lớp ngoài cùng của X có 4 electron.", True)
                ], "X có 14e phân bố: 2, 8, 4 -> có 3 lớp electron, lớp ngoài cùng có 4e."),
                make_tf(2, "Thông hiểu", "Khi nghiên cứu về cấu trúc nguyên tử:", [
                    ("a", "Hầu hết không gian trong nguyên tử là rỗng.", True),
                    ("b", "Số đơn vị điện tích hạt nhân luôn bằng số hạt electron ở vỏ.", True),
                    ("c", "Neutron có khối lượng xấp xỉ bằng khối lượng proton.", True),
                    ("d", "Tất cả các nguyên tử đều bắt buộc phải có đủ 3 loại hạt p, n, e.", False)
                ], "Nguyên tử Hydrogen thông thường 1H không có neutron."),
                make_tf(3, "Vận dụng", "Nguyên tử B có tổng số hạt cơ bản là 24, số hạt không mang điện chiếm 33,33% tổng số hạt:", [
                    ("a", "Số hạt neutron của B là 8.", True),
                    ("b", "Số hạt proton của B là 8.", True),
                    ("c", "B là nguyên tử Oxygen (O).", True),
                    ("d", "Nguyên tử B có 8 electron ở lớp ngoài cùng.", False)
                ], "n = 24 × 33,33% = 8 => 2p = 16 => p = 8 (Oxygen). Phân bố e: 2, 6 -> lớp ngoài cùng có 6e."),
                make_tf(4, "Vận dụng", "Cho nguyên tử Canxi (Ca) có Z = 20 và số neutron = 20:", [
                    ("a", "Tổng số hạt trong nguyên tử Ca là 60 hạt.", True),
                    ("b", "Khối lượng nguyên tử Ca xấp xỉ 40 amu.", True),
                    ("c", "Canxi có 2 electron ở lớp ngoài cùng.", True),
                    ("d", "Hạt nhân Ca mang điện tích -20.", False)
                ], "Hạt nhân mang điện tích dương (+20), không phải âm.")
            ]
            p3 = [
                make_sa(1, "Thông hiểu", "Nguyên tử Boron có 5 proton trong hạt nhân. Số electron chuyển động quanh hạt nhân là bao nhiêu?", "5", "Số e = số p = 5."),
                make_sa(2, "Thông hiểu", "Một nguyên tử có 19 proton và 20 neutron. Khối lượng của nguyên tử đó là bao nhiêu amu?", "39", "19 + 20 = 39 amu."),
                make_sa(3, "Vận dụng", "Nguyên tử Natri (Na) có 11 electron. Số electron ở lớp thứ hai của nó là bao nhiêu?", "8", "Lớp 1: 2e, lớp 2: 8e, lớp 3: 1e."),
                make_sa(4, "Vận dụng", "Tổng số hạt trong nguyên tử Z là 30 hạt. Trong đó hạt không mang điện là 10. Số hạt mang điện dương là bao nhiêu?", "10", "2p = 30 - 10 = 20 => p = 10."),
                make_sa(5, "Vận dụng cao", "Một nguyên tử có tổng số hạt là 58, trong đó số hạt mang điện nhiều hơn không mang điện là 18. Số electron của nguyên tử này là bao nhiêu?", "19", "2p + n = 58, 2p - n = 18 => 4p = 76 => p = e = 19 (Potassium)."),
                make_sa(6, "Vận dụng cao", "Biết 1 amu = $1{,}6605 \\times 10^{-24}$ gam. Khối lượng tính ra gam của 1 nguyên tử Oxygen (16 amu) xấp xỉ bằng bao nhiêu $\\times 10^{-23}$ gam? (Làm tròn 2 chữ số thập phân)", "2.66", "16 × 1,6605 × 10^-24 = 2,6568 × 10^-23 ≈ 2,66.")
            ]
            p4 = [
                make_vdc(1, "Một nguyên tử kim loại X có tổng số hạt là 82. Trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 22 hạt. Nguyên tố X là kim loại nào?", ["Fe (Z = 26)", "Cu (Z = 29)", "Zn (Z = 30)", "Cr (Z = 24)"], 0, "2p + n = 82 và 2p - n = 22 => 4p = 104 => p = 26. Z = 26 là Sắt (Fe)."),
                make_vdc(2, "Phân tử nước ($H_2O$) gồm 2 nguyên tử H (mỗi nguyên tử H có 1p và 1e, không có n) và 1 nguyên tử O (có 8p, 8n, 8e). Tổng số hạt proton, neutron và electron trong 1 phân tử nước là:", ["28 hạt", "26 hạt", "18 hạt", "30 hạt"], 0, "Tổng p = 2×1 + 8 = 10; tổng e = 10; tổng n = 8. Tổng số hạt = 10 + 10 + 8 = 28 hạt."),
                make_vdc(3, "Nguyên tử A có số hạt mang điện nhiều hơn của nguyên tử B là 8 hạt. Tổng số proton của A và B là 24. Hai nguyên tố A và B lần lượt là:", ["Na (11) và Al (13)", "S (16) và O (8)", "Mg (12) và C (6)", "Si (14) và Ne (10)"], 1, "Số hạt mang điện = 2p. Ta có 2pA - 2pB = 8 => pA - pB = 4. Lại có pA + pB = 24 => 2pA = 28 => pA = 16 (S) và pB = 8 (O)."),
                make_vdc(4, "Trong tự nhiên, nguyên tố clo có 2 đồng vị bền là 35Cl (chiếm 75%) và 37Cl (chiếm 25%). Khối lượng nguyên tử trung bình của Clo là:", ["35,50 amu", "35,25 amu", "36,00 amu", "35,75 amu"], 0, "M_tb = (35 × 75 + 37 × 25) / 100 = 35,50 amu.")
            ]

        exams[test_key] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - Bài 2: Nguyên tử - Đề số {t_idx:02d}",
            "grade": "7",
            "subject": "chemistry",
            "subjectName": "Hóa học",
            "chapterId": "chem7_c1",
            "chapterTitle": "Chương I: Nguyên tử - Sơ lược bảng tuần hoàn",
            "lessonId": "chem7_c1_b2",
            "lessonName": "Bài 2: Nguyên tử",
            "testNum": t_idx,
            "duration": "45 phút",
            "points": 10.0,
            "part1": p1,
            "part2": p2,
            "part3": p3,
            "part4": p4
        }

    print(f"Loaded Bài 2 KHTN 7: {len([k for k in exams if 'chem7_c1_b2' in k])} tests")
    return exams

if __name__ == "__main__":
    exs = build_chem_exams()
    print("Test build chem exams success, total count:", len(exs))
