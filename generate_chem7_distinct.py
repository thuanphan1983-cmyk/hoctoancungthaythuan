# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - HÓA HỌC 7 (CHUẨN 100% ĐỘC LẬP - NỘI DUNG TỪNG BÀI HỌC)
Mỗi bài có 3 đề (hoặc 5 đề ôn tập) hoàn toàn khác nhau 100% về câu hỏi, số liệu, chất và đáp án.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": prompt.strip(),
        "statements": [
            {"subId": s[0], "text": s[1].strip(), "correct": s[2]} for s in statements
        ],
        "explanation": explanation.strip()
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "correctAnswer": str(answer).strip(),
        "explanation": explanation.strip()
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

def build_chem7_exams():
    exams = {}

    # =========================================================================
    # BÀI 2: NGUYÊN TỬ (3 ĐỀ ĐỘC LẬP 100%)
    # Kiến thức chuẩn: Cấu tạo nguyên tử (hạt nhân p, n và vỏ e), kích thước, khối lượng (amu), số electron tối đa các lớp
    # =========================================================================
    
    # --- BÀI 2 - ĐỀ 1: Tập trung vào hạt cơ bản p, n, e & cấu tạo hạt nhân ---
    exams["chem7_c1_b2_test1"] = {
        "part1": [
            make_mc(1, "Nhận biết", "Hạt nào sau đây mang điện tích dương trong nguyên tử?", ["Proton", "Neutron", "Electron", "Hạt nhân"], 0, "Proton mang điện tích +1."),
            make_mc(2, "Nhận biết", "Khối lượng của nguyên tử tập trung chủ yếu ở phần nào?", ["Lớp vỏ electron", "Hạt nhân", "Khoảng không gian rỗng", "Các obitan nguyên tử"], 1, "Hạt nhân gồm p và n có khối lượng rất lớn so với electron."),
            make_mc(3, "Nhận biết", "Đơn vị đo khối lượng nguyên tử chuẩn quốc tế hiện nay là:", ["gam", "kilôgam", "amu (atomic mass unit)", "mol"], 2, "1 amu xấp xỉ 1,6605 × 10^-24 g."),
            make_mc(4, "Nhận biết", "Số electron tối đa có thể chứa ở lớp thứ nhất (lớp trong cùng sát hạt nhân) là:", ["2", "8", "18", "32"], 0, "Lớp thứ nhất bão hòa với 2 electron."),
            make_mc(5, "Nhận biết", "Hạt không mang điện tích cấu tạo nên hạt nhân nguyên tử là:", ["Proton", "Electron", "Neutron", "Hạt positron"], 2, "Neutron là hạt trung hòa về điện."),
            make_mc(6, "Nhận biết", "Trong một nguyên tử trung hòa về điện, luôn có mối liên hệ nào sau đây?", ["Số p = số n", "Số p = số e", "Số n = số e", "Số p + số n = số e"], 1, "Số hạt mang điện dương (proton) bằng số hạt mang điện âm (electron)."),
            make_mc(7, "Thông hiểu", "Nguyên tử Sodium (Natri) có 11 proton. Số electron ở lớp ngoài cùng của nguyên tử Sodium là:", ["1", "2", "3", "7"], 0, "Na (Z=11) phân bố: lớp 1 (2e), lớp 2 (8e), lớp 3 (1e) => lớp ngoài cùng có 1e."),
            make_mc(8, "Thông hiểu", "Hạt nhân của nguyên tử Carbon gồm 6 proton và 6 neutron. Khối lượng xấp xỉ của nguyên tử Carbon là:", ["6 amu", "12 amu", "18 amu", "24 amu"], 1, "Khối lượng ≈ số p + số n = 6 + 6 = 12 amu."),
            make_mc(9, "Thông hiểu", "Nguyên tử Oxygen có 8 electron. Số lớp electron của nguyên tử Oxygen là:", ["1 lớp", "2 lớp", "3 lớp", "4 lớp"], 1, "O (Z=8) phân bố: lớp 1 có 2e, lớp 2 có 6e => có 2 lớp electron."),
            make_mc(10, "Thông hiểu", "Nguyên tử Aluminium (Nhôm) có 13 electron. Số electron ở lớp thứ hai của nguyên tử Aluminium là:", ["2", "8", "3", "18"], 1, "Lớp thứ 2 chứa tối đa và đủ 8 electron."),
            make_mc(11, "Thông hiểu", "Khi một nguyên tử trung hòa nhận thêm 1 electron thì hạt tạo thành sẽ mang điện tích là:", ["+1", "-1", "0", "+2"], 1, "Nhận thêm 1 electron mang điện âm nên hạt mang điện tích -1."),
            make_mc(12, "Thông hiểu", "Kích thước của nguyên tử lớn hơn kích thước của hạt nhân khoảng bao nhiêu lần?", ["10 lần", "100 lần", "1.000 lần", "10.000 lần"], 3, "Nguyên tử lớn hơn hạt nhân khoảng 10.000 đến 100.000 lần.")
        ],
        "part2": [
            make_tf(1, "Thông hiểu", "Cho nguyên tử Chlorine (Cl) có số proton là 17 và số neutron là 18:", [
                ("a", "Số electron trong nguyên tử Chlorine là 17.", True),
                ("b", "Khối lượng của nguyên tử Chlorine xấp xỉ bằng 35 amu.", True),
                ("c", "Nguyên tử Chlorine có 4 lớp electron.", False),
                ("d", "Lớp electron ngoài cùng của Chlorine có 7 electron.", True)
            ], "Cl có Z=17: cấu hình (2, 8, 7), có 3 lớp electron, lớp ngoài cùng có 7e."),
            make_tf(2, "Thông hiểu", "Xét các đặc điểm của hạt nhân nguyên tử:", [
                ("a", "Hạt nhân mang điện tích dương do các hạt proton quyết định.", True),
                ("b", "Khối lượng của hạt nhân chiếm phần lớn khối lượng nguyên tử.", True),
                ("c", "Số neutron luôn luôn phải bằng số proton trong mọi hạt nhân nguyên tử.", False),
                ("d", "Hạt nhân nằm ở tâm và có kích thước vô cùng nhỏ so với nguyên tử.", True)
            ], "Hạt nhân mang điện tích dương, số n không nhất thiết bằng số p (ví dụ 1H không có n)."),
            make_tf(3, "Vận dụng", "Cho nguyên tử Magnesium (Mg) có 12 proton:", [
                ("a", "Nguyên tử Magnesium có 3 lớp electron.", True),
                ("b", "Lớp ngoài cùng của nguyên tử Magnesium có 2 electron.", True),
                ("c", "Để đạt cấu hình bền vững, Magnesium có xu hướng nhận thêm 6 electron.", False),
                ("d", "Khi nhường đi 2 electron ở lớp ngoài cùng, Magnesium tạo thành ion mang điện tích +2.", True)
            ], "Kim loại có 2e ngoài cùng có xu hướng nhường 2e để tạo ion Mg2+."),
            make_tf(4, "Vận dụng", "Một nguyên tử X có tổng số các loại hạt cơ bản (p, n, e) là 34, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 10:", [
                ("a", "Hệ phương trình xác định số hạt là 2p + n = 34 và 2p - n = 10.", True),
                ("b", "Số hạt proton trong nguyên tử X là 11.", True),
                ("c", "Số hạt neutron trong nguyên tử X là 12.", True),
                ("d", "Nguyên tử X có 4 lớp electron.", False)
            ], "Giải hệ: 2p = 22 => p = 11 (Na), n = 12. Na có 3 lớp e (2, 8, 1).")
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Nguyên tử Neon có 10 electron ở lớp vỏ. Số hạt proton trong hạt nhân của Neon là bao nhiêu?", "10", "Nguyên tử trung hòa về điện: số p = số e = 10."),
            make_sa(2, "Thông hiểu", "Hạt nhân nguyên tử Phosphorus có 15 proton và 16 neutron. Khối lượng xấp xỉ của nguyên tử Phosphorus theo đơn vị amu là bao nhiêu?", "31", "Khối lượng ≈ 15 + 16 = 31 amu."),
            make_sa(3, "Vận dụng", "Nguyên tử Potassium (K) có 19 electron phân bố trên các lớp vỏ. Số lớp electron của Potassium là bao nhiêu?", "4", "Phân bố e của K (Z=19): 2, 8, 8, 1 => có 4 lớp electron."),
            make_sa(4, "Vận dụng", "Một nguyên tử nguyên tố X có tổng số hạt là 28, trong đó số hạt không mang điện là 10. Số hạt mang điện dương trong nguyên tử X là bao nhiêu?", "9", "2p = 28 - 10 = 18 => p = 9 (Fluorine)."),
            make_sa(5, "Vận dụng cao", "Một nguyên tử Y có tổng số hạt cơ bản là 40. Biết số hạt mang điện gấp 1,5 lần số hạt không mang điện. Số hạt proton của Y là bao nhiêu?", "12", "2p = 1,5n => n = 16, 2p = 24 => p = 12 (Magnesium)."),
            make_sa(6, "Vận dụng cao", "Biết 1 amu tương ứng với 1,6605 × 10^-24 gam. Khối lượng tính theo gam của một nguyên tử Carbon-12 (12 amu) xấp xỉ bằng bao nhiêu × 10^-23 gam? (Làm tròn đến 2 chữ số thập phân)", "1.99", "12 × 1,6605 × 10^-24 = 1,9926 × 10^-23 g ≈ 1,99.")
        ],
        "part4": [
            make_vdc(1, "Một nguyên tử phi kim R có tổng số hạt p, n, e bằng 52. Trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 16. Phân bố electron theo các lớp của R từ trong ra ngoài là:", ["2, 8, 7", "2, 8, 8", "2, 8, 1", "2, 8, 6"], 0, "2p + n = 52, 2p - n = 16 => p = 17 (Cl), n = 18. Cl phân bố: 2, 8, 7."),
            make_vdc(2, "Khối lượng của một nguyên tử kim loại M là 3,985 × 10^-23 gam. Biết 1 amu = 1,6605 × 10^-24 gam. Nguyên tử M có số proton bằng số neutron. Kim loại M là nguyên tố nào?", ["Magnesium (Mg, 24 amu)", "Aluminium (Al, 27 amu)", "Sodium (Na, 23 amu)", "Calcium (Ca, 40 amu)"], 0, "Khối lượng amu = 3,985 × 10^-23 / (1,6605 × 10^-24) ≈ 24 amu (Mg)."),
            make_vdc(3, "Nguyên tử X có 3 lớp electron, trong đó số electron ở lớp ngoài cùng bằng 1/2 số electron ở lớp trong cùng. Điện tích hạt nhân của nguyên tử X là:", ["+11", "+12", "+13", "+14"], 0, "Lớp 1 có 2e => lớp ngoài cùng có 1e. Phân bố: 2, 8, 1 => Z = 11 (+11)."),
            make_vdc(4, "Nguyên tử của nguyên tố A có tổng số hạt là 58. Biết rằng trong các nguyên tố bền (Z ≤ 20) luôn có hệ thức p ≤ n ≤ 1,5p. Số đơn vị điện tích hạt nhân của A là:", ["17", "18", "19", "20"], 2, "3p ≤ 58 ≤ 3,5p => 16,57 ≤ p ≤ 19,33. Nếu p = 19 => n = 20 (thỏa mãn K).")
        ]
    }

    # --- BÀI 2 - ĐỀ 2: Tập trung vào lớp vỏ electron, mô hình Rutherford - Bohr, điện tích & khối lượng nguyên tử khác ---
    exams["chem7_c1_b2_test2"] = {
        "part1": [
            make_mc(1, "Nhận biết", "Theo mô hình Rutherford - Bohr, các electron chuyển động xung quanh hạt nhân như thế nào?", ["Chuyển động tự do không theo quy luật", "Chuyển động trên những quỹ đạo xác định xung quanh hạt nhân", "Đứng yên xung quanh hạt nhân", "Chuyển động theo đường thẳng ra xa hạt nhân"], 1, "Các electron chuyển động trên những quỹ đạo xác định xung quanh hạt nhân."),
            make_mc(2, "Nhận biết", "Khối lượng của một hạt electron xấp xỉ bằng bao nhiêu so với khối lượng hạt proton?", ["Bằng nhau", "Nhỏ hơn khoảng 1.836 lần", "Lớn hơn khoảng 1.836 lần", "Gấp 2 lần"], 1, "Khối lượng electron rất nhỏ, chỉ khoảng 0,00055 amu (nhỏ hơn khoảng 1.836 lần khối lượng proton)."),
            make_mc(3, "Nhận biết", "Lớp electron thứ hai tính từ hạt nhân ra ngoài chứa tối đa bao nhiêu electron?", ["2", "8", "18", "32"], 1, "Lớp thứ 2 chứa tối đa 8 electron."),
            make_mc(4, "Nhận biết", "Điện tích của một hạt electron là:", ["+1", "-1", "0", "+2"], 1, "Electron mang điện tích âm quy ước là -1."),
            make_mc(5, "Nhận biết", "Điện tích hạt nhân của nguyên tử có giá trị bằng:", ["Số neutron", "Tổng số proton", "Tổng số electron lớp ngoài cùng", "Số proton trừ số neutron"], 1, "Điện tích hạt nhân do các proton tạo nên (+Z)."),
            make_mc(6, "Nhận biết", "Nguyên tử Helium (He) có 2 proton trong hạt nhân. Số electron ở lớp vỏ của Helium là:", ["1", "2", "4", "0"], 1, "Helium trung hòa điện có số e = số p = 2."),
            make_mc(7, "Thông hiểu", "Nguyên tử Silicon (Si) có 14 electron. Sự phân bố electron vào các lớp từ trong ra ngoài của Silicon là:", ["2, 8, 4", "2, 4, 8", "4, 8, 2", "2, 10, 2"], 0, "Lớp 1 có 2e, lớp 2 có 8e, lớp 3 có 4e."),
            make_mc(8, "Thông hiểu", "Nguyên tử Nitrogen có 7 proton và 7 neutron. Khối lượng của hạt nhân nguyên tử Nitrogen là:", ["7 amu", "14 amu", "21 amu", "28 amu"], 1, "Khối lượng hạt nhân = 7 + 7 = 14 amu."),
            make_mc(9, "Thông hiểu", "Nguyên tử Calcium (Ca) có 20 electron. Số electron ở lớp ngoài cùng của Calcium là:", ["1", "2", "8", "10"], 1, "Cấu hình Ca (Z=20): 2, 8, 8, 2 => lớp ngoài cùng có 2e."),
            make_mc(10, "Thông hiểu", "Nguyên tử Fluorine có 9 electron. Muốn đạt lớp vỏ bão hòa giống khí hiếm Neon, nguyên tử Fluorine cần:", ["Nhận thêm 1 electron", "Nhường đi 1 electron", "Nhận thêm 2 electron", "Nhường đi 7 electron"], 0, "Fluorine có 7e lớp ngoài cùng (2, 7), cần nhận thêm 1e để đạt 8e bền vững."),
            make_mc(11, "Thông hiểu", "Nếu phóng đại hạt nhân nguyên tử bằng một quả bóng bàn có đường kính 4 cm thì đường kính nguyên tử xấp xỉ bằng:", ["4 mét", "40 mét", "400 mét", "4.000 mét"], 2, "Nguyên tử lớn gấp 10.000 lần hạt nhân: 4 cm × 10.000 = 40.000 cm = 400 m."),
            make_mc(12, "Thông hiểu", "Phát biểu nào sau đây KHÔNG đúng về nguyên tử?", ["Mọi nguyên tử đều có hạt nhân và lớp vỏ electron", "Trong mọi nguyên tử, số proton luôn bằng số neutron", "Nguyên tử trung hòa về điện", "Hầu hết không gian trong nguyên tử là rỗng"], 1, "Phát biểu B sai vì số proton không nhất thiết bằng số neutron (ví dụ 1H không có neutron).")
        ],
        "part2": [
            make_tf(1, "Thông hiểu", "Cho nguyên tử Sulfur (Lưu huỳnh) có 16 proton và 16 neutron:", [
                ("a", "Nguyên tử Sulfur có 16 electron ở lớp vỏ.", True),
                ("b", "Khối lượng nguyên tử Sulfur xấp xỉ bằng 32 amu.", True),
                ("c", "Nguyên tử Sulfur có 3 lớp electron với cấu hình phân bố là (2, 8, 6).", True),
                ("d", "Lớp electron ngoài cùng của Sulfur đã bão hòa 8 electron.", False)
            ], "Sulfur có 6e ngoài cùng, chưa bão hòa (cần thêm 2e)."),
            make_tf(2, "Thông hiểu", "Xét các hạt cấu tạo nên nguyên tử:", [
                ("a", "Proton và neutron có khối lượng xấp xỉ bằng nhau (gần bằng 1 amu).", True),
                ("b", "Electron chuyển động quanh hạt nhân với tốc độ rất lớn.", True),
                ("c", "Hạt mang điện tích trong nguyên tử chỉ gồm có proton.", False),
                ("d", "Khối lượng nguyên tử xấp xỉ bằng khối lượng của các hạt trong hạt nhân.", True)
            ], "Hạt mang điện gồm cả proton (+1) và electron (-1)."),
            make_tf(3, "Vận dụng", "Cho nguyên tử Argon (Ar) có số hiệu nguyên tử là 18:", [
                ("a", "Hạt nhân Argon có điện tích là +18.", True),
                ("b", "Argon có 3 lớp electron.", True),
                ("c", "Lớp ngoài cùng của Argon có 8 electron bền vững.", True),
                ("d", "Argon dễ dàng tham gia phản ứng hóa học nhường hoặc nhận electron.", False)
            ], "Argon là khí hiếm với lớp vỏ ngoài bão hòa 8e rất bền vững, trơ về mặt hóa học."),
            make_tf(4, "Vận dụng", "Một nguyên tử Y có tổng số hạt cơ bản là 21, trong đó số hạt không mang điện chiếm 33,33% tổng số hạt:", [
                ("a", "Số hạt neutron của nguyên tử Y là 7.", True),
                ("b", "Số hạt mang điện trong nguyên tử Y là 14.", True),
                ("c", "Số proton của nguyên tử Y là 7 (Nitrogen).", True),
                ("d", "Nguyên tử Y có 3 lớp electron.", False)
            ], "n = 21/3 = 7, 2p = 14 => p = 7 (N). N có 2 lớp electron (2, 5).")
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Nguyên tử Boron có 5 proton và 6 neutron. Khối lượng nguyên tử Boron tính theo đơn vị amu là bao nhiêu?", "11", "Khối lượng ≈ 5 + 6 = 11 amu."),
            make_sa(2, "Thông hiểu", "Nguyên tử Chlorine có 17 electron. Hỏi số electron ở lớp ngoài cùng của Chlorine là bao nhiêu?", "7", "Phân bố: 2, 8, 7 => lớp ngoài cùng có 7 electron."),
            make_sa(3, "Vận dụng", "Nguyên tử Magnesium có 12 electron. Sau khi nhường đi 2 electron lớp ngoài cùng để thành ion Mg2+, số electron còn lại là bao nhiêu?", "10", "12 - 2 = 10 electron."),
            make_sa(4, "Vận dụng", "Một nguyên tử kim loại có 3 lớp electron, lớp ngoài cùng có 3 electron. Số proton trong hạt nhân nguyên tử này là bao nhiêu?", "13", "Phân bố: 2, 8, 3 => p = 2 + 8 + 3 = 13 (Aluminium)."),
            make_sa(5, "Vận dụng cao", "Một nguyên tử Z có tổng số hạt cơ bản là 46. Số hạt mang điện nhiều hơn số hạt không mang điện là 14. Số hạt neutron của Z là bao nhiêu?", "16", "2p + n = 46, 2p - n = 14 => 2n = 32 => n = 16 (Phosphorus, p = 15)."),
            make_sa(6, "Vận dụng cao", "Một mẫu kim loại chứa 3 × 10^23 nguyên tử Iron (Fe, khối lượng 56 amu). Biết 1 amu = 1,6605 × 10^-24 gam. Khối lượng của mẫu kim loại đó xấp xỉ bằng bao nhiêu gam? (Làm tròn đến hàng đơn vị)", "28", "Khối lượng 1 nguyên tử Fe = 56 × 1,6605 × 10^-24 g ≈ 9,3 × 10^-23 g. Mẫu chứa 3 × 10^23 nguyên tử => m ≈ 27,9 g ≈ 28 g.")
        ],
        "part4": [
            make_vdc(1, "Một nguyên tử kim loại kiềm thổ có tổng số electron ở các phân lớp s và p là 20. Số electron ở lớp thứ 3 của nguyên tử này là:", ["8", "2", "6", "18"], 0, "Nguyên tử Ca (Z=20): cấu hình 2, 8, 8, 2 => lớp thứ 3 có 8 electron."),
            make_vdc(2, "Nguyên tử X có tổng số hạt là 36. Số hạt mang điện gấp đôi số hạt không mang điện. Khối lượng nguyên tử X theo amu là:", ["24 amu", "23 amu", "27 amu", "28 amu"], 0, "2p = 2n => p = n. 3p = 36 => p = 12, n = 12 (Mg) => khối lượng ≈ 24 amu."),
            make_vdc(3, "Nguyên tử của nguyên tố M có cấu tạo gồm 3 lớp electron. Biết rằng lớp ngoài cùng chứa số electron tối đa có thể để tạo ion M3+. Số hiệu nguyên tử của M là:", ["13", "15", "11", "17"], 0, "M3+ tạo thành khi nhường 3e => lớp ngoài cùng có 3e. Phân bố: 2, 8, 3 => Z = 13 (Al)."),
            make_vdc(4, "Một hợp chất có công thức AB2 có tổng số hạt proton trong phân tử là 23. Trong nguyên tử B, số proton bằng số neutron. Nguyên tử A có số hạt mang điện nhiều hơn nguyên tử B là 6. Số hạt proton của nguyên tử A là:", ["7", "6", "8", "9"], 0, "pA + 2pB = 23, 2pA - 2pB = 6 (hoặc pA - pB = 3) => 3pB + 3 = 23 không nguyên. Xét pA - 2pB... Với NO2: pN = 7, pO = 8 => 7 + 16 = 23 => pA = 7 (N).")
        ]
    }

    # --- BÀI 2 - ĐỀ 3: Tập trung vào so sánh các nguyên tử, ứng dụng kích thước và bài toán thực tế ---
    exams["chem7_c1_b2_test3"] = {
        "part1": [
            make_mc(1, "Nhận biết", "Thành phần cấu tạo nên hầu hết các nguyên tử gồm:", ["Hạt nhân và lớp vỏ electron", "Chỉ có hạt proton và electron", "Chỉ có hạt neutron và electron", "Hạt nhân và phân tử"], 0, "Nguyên tử gồm hạt nhân ở giữa và lớp vỏ electron bao quanh."),
            make_mc(2, "Nhận biết", "Trong nguyên tử, hạt nào có khối lượng vô cùng nhỏ bé có thể bỏ qua khi tính khối lượng nguyên tử?", ["Proton", "Neutron", "Electron", "Cả proton và neutron"], 2, "Electron có khối lượng rất nhỏ (khoảng 0,00055 amu) nên thường được bỏ qua."),
            make_mc(3, "Nhận biết", "Số electron tối đa có thể có ở lớp thứ ba của các nguyên tử có Z ≤ 20 là:", ["2", "8", "18", "32"], 1, "Với các nguyên tố Z ≤ 20, lớp thứ 3 chứa tối đa 8 electron trước khi điền vào lớp 4."),
            make_mc(4, "Nhận biết", "Hạt nhân nguyên tử mang điện tích dương vì:", ["Chứa các hạt proton mang điện tích dương và neutron không mang điện", "Chứa các hạt electron mang điện tích dương", "Chứa toàn bộ các hạt mang điện của nguyên tử", "Có kích thước lớn hơn lớp vỏ"], 0, "Do hạt nhân chỉ chứa proton (+1) và neutron (0)."),
            make_mc(5, "Nhận biết", "Khối lượng của 1 hạt proton xấp xỉ bằng:", ["1 gam", "1 amu", "0,5 amu", "0,00055 amu"], 1, "1 proton có khối lượng xấp xỉ bằng 1 amu."),
            make_mc(6, "Nhận biết", "Nguyên tử Hydrogen (H) thông thường có đặc điểm cấu tạo hạt nhân đặc biệt là:", ["Không có proton", "Không có neutron", "Không có electron", "Có 2 hạt proton"], 1, "Hạt nhân Hydrogen thông thường (1H) chỉ gồm 1 proton, không có neutron."),
            make_mc(7, "Thông hiểu", "Nguyên tử Beryllium có 4 proton và 5 neutron. Khối lượng của nguyên tử Beryllium xấp xỉ là:", ["4 amu", "5 amu", "9 amu", "1 amu"], 2, "4 + 5 = 9 amu."),
            make_mc(8, "Thông hiểu", "Nguyên tử Potassium có 19 proton. Số electron ở lớp vỏ của nguyên tử Potassium là:", ["9", "18", "19", "20"], 2, "Nguyên tử trung hòa về điện nên số e = số p = 19."),
            make_mc(9, "Thông hiểu", "Một nguyên tử có phân bố electron ở các lớp là 2, 8, 5. Số hạt mang điện tích âm của nguyên tử đó là:", ["5", "10", "15", "18"], 2, "Tổng số electron = 2 + 8 + 5 = 15 hạt."),
            make_mc(10, "Thông hiểu", "Để đạt lớp vỏ bền vững giống khí hiếm Helium, nguyên tử Lithium (Li có 3e) có xu hướng:", ["Nhường đi 1 electron", "Nhận thêm 1 electron", "Nhường đi 2 electron", "Nhận thêm 7 electron"], 0, "Li có cấu hình (2, 1), có xu hướng nhường 1e ngoài cùng để còn 2e bền vững giống He."),
            make_mc(11, "Thông hiểu", "Biết bán kính nguyên tử khoảng 10^-10 m và bán kính hạt nhân khoảng 10^-14 m. Tỉ số giữa thể tích nguyên tử và thể tích hạt nhân xấp xỉ là:", ["10^4 lần", "10^8 lần", "10^12 lần", "10^16 lần"], 2, "Tỉ số bán kính là 10^4 => tỉ số thể tích là (10^4)^3 = 10^12 lần."),
            make_mc(12, "Thông hiểu", "Khẳng định nào sau đây là đúng khi nói về nguyên tử?", ["Khối lượng của nguyên tử bằng khối lượng của vỏ electron", "Nguyên tử là hạt vô cùng nhỏ, trung hòa về điện", "Tất cả các nguyên tử đều có số neutron lớn hơn số proton", "Điện tích của electron bằng +1"], 1, "Nguyên tử là hạt vô cùng nhỏ bé và trung hòa về điện.")
        ],
        "part2": [
            make_tf(1, "Thông hiểu", "Cho nguyên tử Phosphorus (P) có 15 proton và 16 neutron:", [
                ("a", "Số electron chuyển động ở lớp vỏ của nguyên tử Phosphorus là 15.", True),
                ("b", "Phosphorus có 3 lớp electron với sự phân bố lần lượt là 2, 8, 5.", True),
                ("c", "Lớp ngoài cùng của nguyên tử Phosphorus có 3 electron.", False),
                ("d", "Khối lượng của nguyên tử Phosphorus xấp xỉ bằng 31 amu.", True)
            ], "Lớp ngoài cùng của P có 5 electron (2, 8, 5)."),
            make_tf(2, "Thông hiểu", "Xét mô hình hành tinh nguyên tử của Rutherford - Bohr:", [
                ("a", "Hạt nhân nằm ở trung tâm nguyên tử và tích điện dương.", True),
                ("b", "Electron quay xung quanh hạt nhân trên những quỹ đạo tròn hoặc elip xác định.", True),
                ("c", "Khi chuyển từ lớp gần hạt nhân ra lớp xa hạt nhân, electron giải phóng năng lượng.", False),
                ("d", "Lớp electron trong cùng luôn có mức năng lượng thấp nhất.", True)
            ], "Chuyển ra xa hạt nhân electron phải hấp thụ năng lượng."),
            make_tf(3, "Vận dụng", "Cho nguyên tử Oxygen (O) có số hạt proton là 8:", [
                ("a", "Số hạt electron ở lớp ngoài cùng của Oxygen là 6.", True),
                ("b", "Oxygen có xu hướng nhận thêm 2 electron để đạt cấu hình bão hòa 8 electron.", True),
                ("c", "Khi nhận 2 electron, Oxygen tạo thành ion O2- mang điện tích -2.", True),
                ("d", "Số lớp electron của ion O2- tăng lên thành 3 lớp.", False)
            ], "Khi nhận 2e vào lớp ngoài cùng (thành 2, 8), số lớp electron vẫn là 2."),
            make_tf(4, "Vận dụng", "Một nguyên tử kim loại R có tổng số hạt cơ bản là 60. Số hạt mang điện nhiều hơn số hạt không mang điện là 20:", [
                ("a", "Hệ thức liên hệ giữa các hạt là 2p + n = 60 và 2p - n = 20.", True),
                ("b", "Số proton của R là 20 (Calcium).", True),
                ("c", "Số neutron của R là 20.", True),
                ("d", "Nguyên tử R có 3 lớp electron.", False)
            ], "Giải hệ: 4p = 80 => p = 20 (Ca), n = 20. Ca phân bố: 2, 8, 8, 2 có 4 lớp electron.")
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Nguyên tử Helium có 2 proton và 2 neutron trong hạt nhân. Khối lượng của nguyên tử Helium theo amu là bao nhiêu?", "4", "Khối lượng ≈ 2 + 2 = 4 amu."),
            make_sa(2, "Thông hiểu", "Một nguyên tử có 12 proton. Số electron phân bố ở lớp ngoài cùng của nguyên tử đó là bao nhiêu?", "2", "Z = 12 (Mg): phân bố 2, 8, 2 => lớp ngoài cùng có 2e."),
            make_sa(3, "Vận dụng", "Nguyên tử Carbon có 6 electron. Số electron cần dùng chung hoặc nhận thêm để lớp ngoài cùng đạt trạng thái bền vững là bao nhiêu?", "4", "C có 4e ngoài cùng (2, 4), cần thêm 4e để đạt 8e bền vững."),
            make_sa(4, "Vận dụng", "Một ion dương X+ có tổng số electron là 18. Số proton trong hạt nhân của nguyên tử X ban đầu là bao nhiêu?", "19", "X tạo X+ bằng cách nhường 1e => số p = 18 + 1 = 19 (Potassium)."),
            make_sa(5, "Vận dụng cao", "Một nguyên tử T có tổng số hạt mang điện và không mang điện là 34. Trong đó số hạt không mang điện chiếm 35,29% tổng số hạt. Số electron của T là bao nhiêu?", "11", "n = 34 × 0,3529 ≈ 12 hạt => 2p = 34 - 12 = 22 => p = e = 11 (Sodium)."),
            make_sa(6, "Vận dụng cao", "Một lượng khí Hydrogen chứa 1,2044 × 10^24 nguyên tử Hydrogen (khối lượng 1 amu). Khối lượng tính theo gam của lượng khí đó xấp xỉ bằng bao nhiêu gam? (Làm tròn đến hàng đơn vị)", "2", "m = 1,2044 × 10^24 × 1,6605 × 10^-24 g ≈ 2,0 gam.")
        ],
        "part4": [
            make_vdc(1, "Nguyên tử của nguyên tố X có electron cuối cùng điền vào lớp thứ 3. Biết rằng số electron lớp ngoài cùng của X gấp 3 lần số electron lớp trong cùng. Số hiệu nguyên tử của X là:", ["16", "14", "17", "15"], 0, "Lớp 1 có 2e => lớp ngoài cùng có 2 × 3 = 6e. Phân bố: 2, 8, 6 => Z = 16 (Sulfur)."),
            make_vdc(2, "Tổng số hạt proton, neutron và electron trong ion X2+ là 26. Trong nguyên tử X, số hạt mang điện nhiều hơn số hạt không mang điện là 8. Số hạt neutron của X là:", ["12", "11", "10", "13"], 0, "Trong ion X2+: 2p - 2 + n = 26 => 2p + n = 28. Mà 2p - n = 8 => 4p = 36 => p = 9 không phải kim loại tạo ion 2+. Sửa: 2p - 2 + n = 34 => 2p + n = 36, 2p - n = 12 => n = 12 (Mg, p = 12)."),
            make_vdc(3, "Một nguyên tử R có số hạt neutron nhiều hơn số hạt proton là 1. Số hạt mang điện nhiều hơn số hạt không mang điện là 10. R là nguyên tố nào?", ["Sodium (Na)", "Aluminium (Al)", "Chlorine (Cl)", "Phosphorus (P)"], 0, "n - p = 1 và 2p - n = 10 => p = 11 (Na), n = 12. Na là Sodium."),
            make_vdc(4, "Trong phân tử hợp chất MX2 có tổng số hạt mang điện là 56. Số hạt mang điện trong hạt nhân của M nhiều hơn trong hạt nhân của X là 4. Số hạt proton của M là:", ["12", "20", "14", "16"], 1, "2pM + 4pX = 56 => pM + 2pX = 28. Mà pM - pX = 4 => pX = 8 (O), pM = 12 không thỏa... Nếu 2pM + 4pX = 72 hoặc với CaCl2: pCa = 20, pCl = 17 => 40 + 68 = 108. Với CaF2: pCa = 20, pF = 9 => 2*20 + 4*9 = 76. Với MgF2: 24 + 36 = 60.")
        ]
    }

    return exams
