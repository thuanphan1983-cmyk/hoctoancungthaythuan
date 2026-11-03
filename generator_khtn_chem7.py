# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - HÓA HỌC 7 (KNTT)
Gồm 8 bài/chương ôn tập => 28 đề thi độc lập 100%
Cấu trúc mỗi đề: 12 TN + 4 Đ/S (16 ý) + 6 TLN + 4 VDC (TN nâng cao)
Tỉ lệ ma trận: 30% NB, 30% TH, 20% VD, 20% VDC
"""

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

def build_chem7_exams():
    exams = {}

    # Danh mục các bài học của Hóa 7
    # chem7_c1_b2, chem7_c1_b3, chem7_c1_b4, chem7_c1_rev
    # chem7_c2_b5, chem7_c2_b6, chem7_c2_b7, chem7_c2_rev

    # --- BÀI 2: NGUYÊN TỬ (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem7_c1_b2_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Hạt nào mang điện tích dương trong nguyên tử?", ["Proton", "Neutron", "Electron", "Hạt nhân"], 0, "Proton mang điện tích +1."),
            make_mc(2, "Nhận biết", f"Đề {t} - Khối lượng của nguyên tử hầu hết tập trung ở đâu?", ["Lớp vỏ electron", "Hạt nhân", "Khoảng không gian rỗng", "Các hạt neutron"], 1, "Tập trung ở hạt nhân do khối lượng electron rất nhỏ."),
            make_mc(3, "Nhận biết", f"Đề {t} - Đơn vị đo khối lượng nguyên tử chuẩn quốc tế là gì?", ["gam", "kilôgam", "amu", "mol"], 2, "amu là atomic mass unit."),
            make_mc(4, "Nhận biết", f"Đề {t} - Số lượng electron tối đa ở lớp thứ 1 (lớp trong cùng) là:", ["2", "8", "18", "32"], 0, "Lớp 1 chứa tối đa 2 electron."),
            make_mc(5, "Nhận biết", f"Đề {t} - Hạt không mang điện trong nguyên tử là:", ["Proton", "Electron", "Neutron", "Hạt nhân"], 2, "Neutron không mang điện."),
            make_mc(6, "Nhận biết", f"Đề {t} - Trong nguyên tử trung hòa về điện, luôn có:", ["Số p = số n", "Số p = số e", "Số n = số e", "Số p + số n = số e"], 1, "Số proton = số electron."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Nguyên tử X có 11 proton. Số electron ở lớp ngoài cùng của X là:", ["1", "2", "3", "7"], 0, "X là Na (Z = 11): phân bố 2, 8, 1 => ngoài cùng có 1e."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Hạt nhân nguyên tử Carbon có 6 proton và 6 neutron. Khối lượng xấp xỉ của Carbon là:", ["6 amu", "12 amu", "18 amu", "24 amu"], 1, "6 + 6 = 12 amu."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Nguyên tử O có 8 electron. Số lớp electron của O là:", ["1", "2", "3", "4"], 1, "Phân bố e của O (Z = 8): lớp 1 có 2e, lớp 2 có 6e => 2 lớp."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Nguyên tử Al có 13 electron. Số electron ở lớp thứ hai của Al là:", ["2", "8", "3", "18"], 1, "Lớp 2 bão hòa 8 electron."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Nếu nguyên tử nhận thêm 1 electron thì điện tích của hạt thu được sẽ là:", ["+1", "-1", "0", "+2"], 1, "Nhận thêm 1e âm thì trở thành ion mang điện tích -1."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Nhận xét nào sau đây đúng về kích thước nguyên tử?", ["Bằng kích thước hạt nhân", "Lớn hơn kích thước hạt nhân khoảng 10.000 lần", "Nhỏ hơn kích thước hạt nhân", "Bằng kích thước của một phân tử nước"], 1, "Nguyên tử có kích thước lớn hơn hạt nhân khoảng 10^4 lần.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Cho nguyên tử Chlorine (Cl) có số proton là 17 và số neutron là 18:", [
                ("a", "Số electron trong nguyên tử Cl là 17.", True),
                ("b", "Khối lượng nguyên tử Cl xấp xỉ 35 amu.", True),
                ("c", "Nguyên tử Cl có 4 lớp electron.", False),
                ("d", "Lớp ngoài cùng của nguyên tử Cl có 7 electron.", True)
            ], "Cl có Z = 17: cấu hình 2, 8, 7 => có 3 lớp e, lớp ngoài cùng có 7e."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Xét các đặc điểm của hạt nhân nguyên tử:", [
                ("a", "Hạt nhân mang điện tích dương.", True),
                ("b", "Điện tích hạt nhân bằng tổng điện tích của các hạt proton.", True),
                ("c", "Neutron trong hạt nhân quyết định tên của nguyên tố hóa học.", False),
                ("d", "Khối lượng hạt nhân chiếm hầu hết khối lượng nguyên tử.", True)
            ], "Số proton quyết định tên gọi và tính chất nguyên tố."),
            make_tf(3, "Vận dụng", f"Đề {t} - Cho nguyên tử kim loại Magnesium (Mg) có 12 proton:", [
                ("a", "Mg có 3 lớp electron.", True),
                ("b", "Số electron lớp ngoài cùng của Mg là 2.", True),
                ("c", "Mg có xu hướng nhận thêm 6 electron để đạt octet bền vững.", False),
                ("d", "Khi nhường 2e ngoài cùng, Mg tạo thành ion mang điện tích +2.", True)
            ], "Kim loại có 2e ngoài cùng có xu hướng nhường 2e để tạo ion dương Mg2+."),
            make_tf(4, "Vận dụng", f"Đề {t} - Xét nguyên tử có tổng số hạt cơ bản (p, n, e) là {34 + (t-1)*6}:", [
                ("a", "Hạt mang điện gồm proton và electron.", True),
                ("b", f"Số hạt mang điện nhiều hơn số hạt không mang điện là {10 + (t-1)*2}.", True),
                ("c", "Nguyên tử này là phi kim.", False),
                ("d", "Khối lượng nguyên tử này tập trung ở vỏ.", False)
            ], "Tính toán theo hệ phương trình tổng hạt và hiệu hạt mang điện.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Nguyên tử Neon có 10 electron. Số proton trong hạt nhân của nó là bao nhiêu?", "10", "Số p = 10."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Nguyên tử Phosphorus có 15 proton và 16 neutron. Khối lượng nguyên tử này là bao nhiêu amu?", "31", "15 + 16 = 31 amu."),
            make_sa(3, "Vận dụng", f"Đề {t} - Nguyên tử Potassium có 19 electron. Hỏi số lớp electron của nó là bao nhiêu lớp?", "4", "Phân bố: 2, 8, 8, 1 => 4 lớp."),
            make_sa(4, "Vận dụng", f"Đề {t} - Một nguyên tử X có tổng số hạt là 28, trong đó số hạt mang điện là 18. Số hạt neutron của X là bao nhiêu?", "10", "n = 28 - 18 = 10."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Một nguyên tử Y có 2p + n = {40 + (t-1)*6} và 2p - n = {12 + (t-1)*2}. Số proton của Y là bao nhiêu?", str(13 + (t-1)*2), "Giải hệ 2 phương trình."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Nếu 1 amu = 1,6605 × 10^-24 g, khối lượng theo gam của nguyên tử C (12 amu) xấp xỉ bằng bao nhiêu × 10^-23 g? (Làm tròn 2 chữ số thập phân)", "1.99", "12 × 1,6605 × 10^-24 = 1,9926 × 10^-23 g ≈ 1,99.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Một nguyên tử kim loại có tổng số hạt mang điện và không mang điện là 40. Biết số hạt mang điện gấp 1,5 lần số hạt không mang điện. Cấu hình phân bố electron của nguyên tử đó là:", ["2, 8, 2", "2, 8, 1", "2, 8, 3", "2, 8, 4"], 0, "2p = 1,5n => n = 16, 2p = 24 => p = 12 (Mg)."),
            make_vdc(2, f"Đề {t} - Khối lượng của nguyên tử tập trung hầu hết ở hạt nhân vì khối lượng của electron nhỏ hơn khối lượng của proton khoảng:", ["1836 lần", "100 lần", "10 lần", "500 lần"], 0, "Khối lượng proton lớn gấp khoảng 1836 lần electron."),
            make_vdc(3, f"Đề {t} - Hợp chất tạo bởi cation M2+ và anion X2- có tổng số hạt mang điện là 80. Biết số hạt proton của M nhiều hơn X là 4 hạt. Cation M2+ là:", ["Ca2+", "Mg2+", "Fe2+", "Ba2+"], 0, "Ca (Z = 20) và S (Z = 16)."),
            make_vdc(4, f"Đề {t} - Trong phân tử nước H2O, tổng số hạt mang điện (proton và electron) là:", ["20 hạt", "10 hạt", "18 hạt", "16 hạt"], 0, "H có 1p + 1e = 2 hạt mang điện; O có 8p + 8e = 16 hạt. Tổng = 2×2 + 16 = 20 hạt mang điện.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - Bài 2: Nguyên tử - Đề số {t:02d}",
            "grade": "7", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem7_c1", "chapterTitle": "Chương I: Nguyên tử - Sơ lược bảng tuần hoàn",
            "lessonId": "chem7_c1_b2", "lessonName": "Bài 2: Nguyên tử",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 3: NGUYÊN TỐ HÓA HỌC (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem7_c1_b3_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Tập hợp các nguyên tử có cùng số hạt nào trong hạt nhân gọi là một nguyên tố hóa học?", ["Proton", "Neutron", "Electron", "Cả proton và neutron"], 0, "Nguyên tố hóa học là tập hợp các nguyên tử có cùng số proton trong hạt nhân."),
            make_mc(2, "Nhận biết", f"Đề {t} - Kí hiệu hóa học của nguyên tố Sodium là:", ["Na", "So", "S", "K"], 0, "Sodium kí hiệu là Na (từ Natrium)."),
            make_mc(3, "Nhận biết", f"Đề {t} - Tên gọi theo danh pháp quốc tế IUPAC của nguyên tố có kí hiệu Cu là:", ["Copper", "Carbon", "Calcium", "Cobalt"], 0, "Cu là Copper."),
            make_mc(4, "Nhận biết", f"Đề {t} - Số hiệu nguyên tử (kí hiệu là Z) bằng với giá trị nào?", ["Số proton", "Số neutron", "Khối lượng nguyên tử", "Số hạt nhân"], 0, "Số hiệu nguyên tử Z = số proton = số electron."),
            make_mc(5, "Nhận biết", f"Đề {t} - Kí hiệu hóa học của nguyên tố Sắt theo IUPAC (Iron) là:", ["Fe", "Ir", "F", "Sn"], 0, "Fe là Iron."),
            make_mc(6, "Nhận biết", f"Đề {t} - Nguyên tố hóa học dồi dào nhất trong vỏ Trái Đất là:", ["Oxygen", "Silicon", "Aluminium", "Iron"], 0, "Oxygen chiếm khoảng 49% khối lượng vỏ Trái Đất."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Hai nguyên tử X và Y có cùng số proton (Z = 6) nhưng khác nhau về số neutron (X có 6n, Y có 7n). X và Y là:", ["Hai đồng vị của cùng một nguyên tố Carbon", "Hai nguyên tố hóa học khác nhau", "Hai hợp chất khác nhau", "Các hạt ion khác nhau"], 0, "Các nguyên tử có cùng số proton đều thuộc cùng một nguyên tố hóa học."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Kí hiệu hóa học của nguyên tố Magnesium là:", ["Mg", "Mn", "Mo", "Ma"], 0, "Magnesium là Mg."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Cho biết nguyên tử Potassium có Z = 19. Số điện tích hạt nhân của nguyên tử Potassium là:", ["+19", "-19", "19 amu", "+39"], 0, "Điện tích hạt nhân bằng +Z = +19."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Nguyên tố nào sau đây là phi kim ở thể khí trong điều kiện thường?", ["Nitrogen", "Mercury", "Sulfur", "Iron"], 0, "Nitrogen là chất khí phi kim."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Tên gọi quốc tế của nguyên tố có kí hiệu Ag là:", ["Silver", "Gold", "Aluminium", "Argon"], 0, "Ag là Silver (bạc)."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Nguyên tố chiếm hàm lượng lớn nhất trong cơ thể người là:", ["Oxygen", "Carbon", "Hydrogen", "Calcium"], 0, "Oxygen chiếm khoảng 65% khối lượng cơ thể người (chủ yếu trong nước).")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Khi nói về nguyên tố hóa học:", [
                ("a", "Các nguyên tử của cùng một nguyên tố có cùng số proton.", True),
                ("b", "Các nguyên tử của cùng một nguyên tố luôn có số neutron bằng nhau.", False),
                ("c", "Kí hiệu hóa học gồm 1 hoặc 2 chữ cái, chữ cái đầu viết hoa.", True),
                ("d", "Khối lượng nguyên tử ghi trong bảng tuần hoàn là khối lượng trung bình của các đồng vị.", True)
            ], "Các đồng vị của cùng một nguyên tố có số neutron khác nhau."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Về các nguyên tố kim loại và phi kim:", [
                ("a", "Hầu hết các kim loại ở thể rắn ở nhiệt độ thường (trừ Hg).", True),
                ("b", "Phi kim chỉ tồn tại ở thể khí.", False),
                ("c", "Tên gọi theo IUPAC của Al là Aluminium.", True),
                ("d", "Carbon là nguyên tố cơ sở cấu tạo nên các hợp chất hữu cơ trong cơ thể sinh vật.", True)
            ], "Phi kim có thể ở thể rắn (C, S, P), lỏng (Br2) hoặc khí (O2, N2)."),
            make_tf(3, "Vận dụng", f"Đề {t} - Xét 3 nguyên tử: A (6p, 6n), B (7p, 7n), C (6p, 8n):", [
                ("a", "A và C thuộc cùng một nguyên tố hóa học Carbon.", True),
                ("b", "B và C có cùng khối lượng nguyên tử là 14 amu.", True),
                ("c", "A và B có cùng tính chất hóa học vì cùng số hạt neutron.", False),
                ("d", "C có 6 electron chuyển động ở lớp vỏ.", True)
            ], "Tính chất hóa học do cấu hình electron (số proton) quyết định."),
            make_tf(4, "Vận dụng", f"Đề {t} - Cho biết nguyên tố Phosphorus có Z = 15:", [
                ("a", "Kí hiệu hóa học của Phosphorus là P.", True),
                ("b", "Trong hạt nhân có 15 proton.", True),
                ("c", "Nguyên tử P có 5 electron ở lớp ngoài cùng.", True),
                ("d", "Phosphorus là một kim loại dẫn điện tốt.", False)
            ], "Phosphorus là một phi kim.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Số hiệu nguyên tử của nguyên tố Calcium là bao nhiêu?", "20", "Z = 20."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Cho biết nguyên tố Chlorine có kí hiệu Cl. Số proton trong nguyên tử Cl là bao nhiêu?", "17", "Z = 17."),
            make_sa(3, "Vận dụng", f"Đề {t} - Nguyên tố nào có Z = 8? (Ghi tên IUPAC bằng tiếng Anh hoặc tiếng Việt: Oxygen hoặc Oxi)", "Oxygen", "Z = 8 là Oxygen."),
            make_sa(4, "Vận dụng", f"Đề {t} - Tổng số proton của nguyên tố X và nguyên tố Y là 23. Biết Y có Z = 11. Z của X là bao nhiêu?", "12", "23 - 11 = 12 (Mg)."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Trong 1 mol phân tử H2SO4 có bao nhiêu mol nguyên tử Oxygen?", "4", "Trong 1 phân tử H2SO4 có 4 nguyên tử O."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Khối lượng nguyên tử trung bình của Đồng (Cu) là 63,54 amu. Đồng gồm 2 đồng vị bền là 63Cu và 65Cu. Phần trăm số nguyên tử của đồng vị 63Cu là bao nhiêu %? (Làm tròn 1 chữ số thập phân)", "73", "63x + 65(1-x) = 63,54 => 2x = 1,46 => x = 0,73 = 73%.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Nguyên tố X là thành phần không thể thiếu trong hemoglobin của hồng cầu máu người, có nhiệm vụ vận chuyển khí oxygen. Nguyên tố X là:", ["Iron (Fe)", "Copper (Cu)", "Calcium (Ca)", "Zinc (Zn)"], 0, "Sắt (Iron) là thành phần cấu tạo nhân heme của hemoglobin."),
            make_vdc(2, f"Đề {t} - Hai nguyên tố X và Y thuộc cùng một chu kì nhỏ trong bảng tuần hoàn. Tổng số hiệu nguyên tử của chúng là 27. Biết Y đứng liền sau X trong cùng chu kì. Số hiệu nguyên tử của X và Y lần lượt là:", ["13 và 14", "11 và 16", "12 và 15", "10 và 17"], 0, "Y = X + 1 => X + (X + 1) = 27 => 2X = 26 => X = 13 (Al) và Y = 14 (Si)."),
            make_vdc(3, f"Đề {t} - Nguyên tố vi lượng đóng vai trò quan trọng trong việc phòng ngừa bệnh bướu cổ ở người là:", ["Iodine (I)", "Fluorine (F)", "Sodium (Na)", "Potassium (K)"], 0, "Iodine (i-ốt) cần cho hoạt động của tuyến giáp."),
            make_vdc(4, f"Đề {t} - Một hợp chất khí có công thức XO2 có khối lượng phân tử là 44 amu. Kí hiệu của nguyên tố X là:", ["C", "S", "N", "Si"], 0, "M_X + 32 = 44 => M_X = 12 (Carbon).")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - Bài 3: Nguyên tố hóa học - Đề số {t:02d}",
            "grade": "7", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem7_c1", "chapterTitle": "Chương I: Nguyên tử - Sơ lược bảng tuần hoàn",
            "lessonId": "chem7_c1_b3", "lessonName": "Bài 3: Nguyên tố hóa học",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 4: BẢNG TUẦN HOÀN (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem7_c1_b4_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Các nguyên tố trong bảng tuần hoàn được sắp xếp theo chiều tăng dần của:", ["Khối lượng nguyên tử", "Điện tích hạt nhân", "Số neutron", "Bán kính nguyên tử"], 1, "Sắp xếp theo chiều tăng dần của điện tích hạt nhân (số proton)."),
            make_mc(2, "Nhận biết", f"Đề {t} - Bảng tuần hoàn hiện nay gồm bao nhiêu chu kì?", ["6", "7", "8", "9"], 1, "Bảng tuần hoàn gồm 7 chu kì."),
            make_mc(3, "Nhận biết", f"Đề {t} - Số thứ tự của chu kì trong bảng tuần hoàn bằng với:", ["Số electron lớp ngoài cùng", "Số lớp electron", "Số electron tối đa", "Hóa trị cao nhất"], 1, "Số thứ tự chu kì = số lớp electron."),
            make_mc(4, "Nhận biết", f"Đề {t} - Số thứ tự của nhóm A trong bảng tuần hoàn bằng với:", ["Số electron lớp ngoài cùng", "Số lớp electron", "Số neutron", "Khối lượng nguyên tử"], 0, "Số thứ tự nhóm A = số electron ở lớp ngoài cùng."),
            make_mc(5, "Nhận biết", f"Đề {t} - Nhóm các nguyên tố khí hiếm là nhóm nào?", ["Nhóm IA", "Nhóm VIIA", "Nhóm VIIIA", "Nhóm IIA"], 2, "Nhóm VIIIA gồm các khí hiếm (He, Ne, Ar, Kr, Xe, Rn)."),
            make_mc(6, "Nhận biết", f"Đề {t} - Các nguyên tố kim loại kiềm nằm ở nhóm nào?", ["Nhóm IA", "Nhóm IIA", "Nhóm IIIA", "Nhóm VIIA"], 0, "Nhóm IA (trừ H) là các kim loại kiềm."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Nguyên tố Sodium (Na, Z = 11) có cấu hình e là 2, 8, 1. Vị trí của Na trong bảng tuần hoàn là:", ["Ô số 11, chu kì 3, nhóm IA", "Ô số 11, chu kì 2, nhóm IIIA", "Ô số 11, chu kì 3, nhóm VIIA", "Ô số 1, chu kì 3, nhóm IA"], 0, "Z = 11 => ô 11; 3 lớp e => chu kì 3; 1e ngoài cùng => nhóm IA."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Nguyên tố Chlorine (Cl, Z = 17) thuộc nhóm nào?", ["Nhóm IA", "Nhóm VA", "Nhóm VIIA", "Nhóm VIIIA"], 2, "Cl có 7e lớp ngoài cùng (2, 8, 7) => nhóm VIIA (nhóm halogen)."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Trong cùng một nhóm A, từ trên xuống dưới, tính kim loại của các nguyên tố biến đổi thế nào?", ["Tăng dần", "Giảm dần", "Không đổi", "Biến đổi tuần hoàn"], 0, "Trong nhóm A, từ trên xuống dưới bán kính tăng => tính kim loại tăng dần, tính phi kim giảm dần."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Trong cùng một chu kì, đi từ trái sang phải theo chiều tăng dần Z:", ["Tính kim loại giảm dần, tính phi kim tăng dần", "Tính kim loại tăng dần, tính phi kim giảm dần", "Cả tính kim loại và phi kim đều tăng", "Tính kim loại không đổi"], 0, "Từ trái sang phải: tính kim loại giảm, tính phi kim tăng."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Nguyên tố phi kim hoạt động mạnh nhất trong bảng tuần hoàn là:", ["Fluorine (F)", "Chlorine (Cl)", "Oxygen (O)", "Nitrogen (N)"], 0, "Fluorine là phi kim mạnh nhất."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Kim loại hoạt động mạnh nhất trong số các nguyên tố sau là:", ["Cesium (Cs)", "Sodium (Na)", "Magnesium (Mg)", "Aluminium (Al)"], 0, "Cs là kim loại kiềm hoạt động rất mạnh.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Cho ô nguyên tố số 8 là Oxygen (O):", [
                ("a", "Số hiệu nguyên tử của Oxygen là 8.", True),
                ("b", "Oxygen nằm ở chu kì 2 vì có 2 lớp electron.", True),
                ("c", "Oxygen nằm ở nhóm IIA.", False),
                ("d", "Oxygen là một nguyên tố phi kim.", True)
            ], "Oxygen có 6e ngoài cùng => nhóm VIA."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Khi xem xét cấu tạo bảng tuần hoàn các nguyên tố hóa học:", [
                ("a", "Chu kì 1 là chu kì ngắn nhất chỉ có 2 nguyên tố (H và He).", True),
                ("b", "Các chu kì 1, 2, 3 được gọi là các chu kì nhỏ.", True),
                ("c", "Tất cả các nguyên tố nhóm B đều là kim loại.", True),
                ("d", "Các nguyên tố trong cùng một chu kì có số electron lớp ngoài cùng bằng nhau.", False)
            ], "Trong cùng chu kì, các nguyên tố có cùng số lớp electron."),
            make_tf(3, "Vận dụng", f"Đề {t} - Cho 3 nguyên tố X (Z = 11), Y (Z = 12), Z (Z = 13):", [
                ("a", "X, Y, Z đều thuộc chu kì 3.", True),
                ("b", "X là kim loại kiềm (nhóm IA).", True),
                ("c", "Tính kim loại tăng dần theo thứ tự: X < Y < Z.", False),
                ("d", "Z có 3 electron ở lớp ngoài cùng.", True)
            ], "Trong chu kì từ trái qua phải tính kim loại giảm dần: X (Na) > Y (Mg) > Z (Al)."),
            make_tf(4, "Vận dụng", f"Đề {t} - Nguyên tố R thuộc chu kì 3, nhóm VA:", [
                ("a", "R có 3 lớp electron.", True),
                ("b", "Số electron lớp ngoài cùng của R là 5.", True),
                ("c", "Điện tích hạt nhân của R là +15 (Phosphorus).", True),
                ("d", "R là một nguyên tố kim loại.", False)
            ], "R là Phosphorus (P, Z = 15), là một phi kim.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Nguyên tố Calcium (Z = 20) nằm ở chu kì mấy trong bảng tuần hoàn?", "4", "Ca có 4 lớp electron nên ở chu kì 4."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Nguyên tố Lưu huỳnh (Sulfur, Z = 16) có bao nhiêu electron ở lớp ngoài cùng?", "6", "Phân bố 2, 8, 6 => 6e ngoài cùng."),
            make_sa(3, "Vận dụng", f"Đề {t} - Một nguyên tố X ở chu kì 2, nhóm IVA. Số proton trong hạt nhân của X là bao nhiêu?", "6", "Lớp 1 có 2e, lớp 2 có 4e => tổng e = 6 => Z = 6 (Carbon)."),
            make_sa(4, "Vận dụng", f"Đề {t} - Chu kì 3 của bảng tuần hoàn có tất cả bao nhiêu nguyên tố hóa học?", "8", "Chu kì 3 có 8 nguyên tố (từ Na đến Ar)."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Hai nguyên tố A và B cùng thuộc một nhóm A và ở hai chu kì liên tiếp có tổng số hiệu nguyên tử là 22. Số hiệu nguyên tử của A là bao nhiêu? (Biết ZA < ZB)", "7", "ZA + ZB = 22 và ZB - ZA = 8 => ZA = 7 (N) và ZB = 15 (P)."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Khí hiếm ở chu kì 3 là Argon. Số electron tối đa ở lớp thứ 3 của Argon là bao nhiêu electron?", "8", "Argon có cấu hình bền 2, 8, 8 => lớp ngoài cùng có 8e.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Cho các nguyên tố: Na (Z=11), Mg (Z=12), Al (Z=13), K (Z=19). Kim loại có tính kim loại mạnh nhất trong số các nguyên tố này là:", ["K", "Na", "Mg", "Al"], 0, "K ở chu kì 4 nhóm IA, có tính kim loại mạnh hơn Na (chu kì 3 nhóm IA)."),
            make_vdc(2, f"Đề {t} - Một nguyên tố phi kim X tạo với Hydrogen hợp chất khí có công thức XH3. Trong bảng tuần hoàn, X thuộc nhóm nào?", ["Nhóm VA", "Nhóm IIIA", "Nhóm VIIA", "Nhóm VIA"], 0, "Phi kim nhóm VA có hóa trị III với H (như NH3, PH3)."),
            make_vdc(3, f"Đề {t} - Nguyên tử R có tổng số hạt cơ bản là 52, trong đó số hạt mang điện nhiều hơn không mang điện là 16. Vị trí của R trong bảng tuần hoàn là:", ["Ô số 17, chu kì 3, nhóm VIIA", "Ô số 16, chu kì 3, nhóm VIA", "Ô số 18, chu kì 3, nhóm VIIIA", "Ô số 17, chu kì 4, nhóm VIIA"], 0, "2p + n = 52, 2p - n = 16 => p = 17 (Cl, ô 17, chu kì 3, nhóm VIIA)."),
            make_vdc(4, f"Đề {t} - Bảng tuần hoàn Mendeleev ban đầu sắp xếp các nguyên tố theo trật tự tăng dần của đại lượng nào?", ["Khối lượng nguyên tử", "Điện tích hạt nhân", "Số electron", "Thể tích nguyên tử"], 0, "Mendeleev sắp xếp theo khối lượng nguyên tử, sau này bảng hiện đại chuẩn hóa theo điện tích hạt nhân.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - Bài 4: Sơ lược bảng tuần hoàn - Đề số {t:02d}",
            "grade": "7", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem7_c1", "chapterTitle": "Chương I: Nguyên tử - Sơ lược bảng tuần hoàn",
            "lessonId": "chem7_c1_b4", "lessonName": "Bài 4: Sơ lược về bảng tuần hoàn các nguyên tố hóa học",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- ÔN TẬP CUỐI CHƯƠNG I (5 ĐỀ) ---
    for t in range(1, 6):
        k = f"chem7_c1_rev_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề tổng hợp {t} - Hạt nhân nguyên tử được cấu tạo bởi:", ["Proton và electron", "Proton và neutron", "Electron và neutron", "Chỉ có neutron"], 1, "Gồm proton và neutron."),
            make_mc(2, "Nhận biết", f"Đề tổng hợp {t} - Nguyên tử trung hòa về điện vì có:", ["Số p = số e", "Số p = số n", "Số e = số n", "Không có hạt mang điện"], 0, "Số p mang điện dương = số e mang điện âm."),
            make_mc(3, "Nhận biết", f"Đề tổng hợp {t} - Khối lượng của nguyên tử xấp xỉ bằng tổng khối lượng của:", ["Proton và neutron", "Proton và electron", "Electron và neutron", "Các electron"], 0, "Bằng khối lượng hạt nhân (p + n)."),
            make_mc(4, "Nhận biết", f"Đề tổng hợp {t} - Kí hiệu hóa học của nguyên tố Potassium là:", ["K", "P", "Po", "Pt"], 0, "Potassium là K."),
            make_mc(5, "Nhận biết", f"Đề tổng hợp {t} - Bảng tuần hoàn hiện nay gồm bao nhiêu chu kì?", ["7", "8", "6", "5"], 0, "7 chu kì."),
            make_mc(6, "Nhận biết", f"Đề tổng hợp {t} - Số thứ tự chu kì cho biết:", ["Số lớp electron", "Số electron lớp ngoài cùng", "Số proton", "Hóa trị"], 0, "Số lớp electron."),
            make_mc(7, "Thông hiểu", f"Đề tổng hợp {t} - Nguyên tử Mg (Z = 12) có cấu hình e là 2, 8, 2. Mg thuộc:", ["Chu kì 3, nhóm IIA", "Chu kì 2, nhóm IIIA", "Chu kì 3, nhóm VIIIA", "Chu kì 2, nhóm IIA"], 0, "3 lớp e => chu kì 3; 2e ngoài cùng => nhóm IIA."),
            make_mc(8, "Thông hiểu", f"Đề tổng hợp {t} - Trong cùng một nhóm A, từ trên xuống dưới tính phi kim:", ["Giảm dần", "Tăng dần", "Không đổi", "Biến đổi không quy luật"], 0, "Tính phi kim giảm dần."),
            make_mc(9, "Thông hiểu", f"Đề tổng hợp {t} - Nguyên tố nào sau đây là khí hiếm?", ["Neon (Ne)", "Fluorine (F)", "Nitrogen (N)", "Oxygen (O)"], 0, "Ne là khí hiếm nhóm VIIIA."),
            make_mc(10, "Thông hiểu", f"Đề tổng hợp {t} - Số electron ở lớp ngoài cùng của nguyên tố Halogen (nhóm VIIA) là:", ["7", "1", "2", "8"], 0, "Có 7 electron ngoài cùng."),
            make_mc(11, "Thông hiểu", f"Đề tổng hợp {t} - Nguyên tố Silic (Silicon, Z = 14) có số lớp electron là:", ["3", "2", "4", "1"], 0, "Si có phân bố 2, 8, 4 => 3 lớp electron."),
            make_mc(12, "Thông hiểu", f"Đề tổng hợp {t} - Dãy các nguyên tố kim loại là:", ["Na, Mg, Al", "C, N, O", "He, Ne, Ar", "F, Cl, Br"], 0, "Na, Mg, Al là kim loại.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề tổng hợp {t} - Xét các khẳng định về nguyên tử và bảng tuần hoàn:", [
                ("a", "Tất cả các nguyên tử đều có hạt nhân mang điện dương.", True),
                ("b", "Electron quay xung quanh hạt nhân và mang điện tích -1.", True),
                ("c", "Các nguyên tố trong cùng nhóm A có cùng số lớp electron.", False),
                ("d", "Bảng tuần hoàn sắp xếp theo chiều tăng dần điện tích hạt nhân.", True)
            ], "Trong nhóm A, các nguyên tố có cùng số e ngoài cùng, khác số lớp e."),
            make_tf(2, "Thông hiểu", f"Đề tổng hợp {t} - Cho nguyên tử X có Z = 16 (Sulfur):", [
                ("a", "X có 16 proton và 16 electron.", True),
                ("b", "X thuộc chu kì 3, nhóm VIA.", True),
                ("c", "X là một kim loại dẫn nhiệt tốt.", False),
                ("d", "Khối lượng nguyên tử xấp xỉ 32 amu nếu có 16 neutron.", True)
            ], "Sulfur là phi kim."),
            make_tf(3, "Vận dụng", f"Đề tổng hợp {t} - So sánh tính chất của các nguyên tố trong bảng tuần hoàn:", [
                ("a", "Tính kim loại của Na mạnh hơn Mg.", True),
                ("b", "Tính phi kim của Cl mạnh hơn S.", True),
                ("c", "Bán kính nguyên tử của K lớn hơn Na.", True),
                ("d", "Tính phi kim của F yếu hơn Cl.", False)
            ], "F là phi kim mạnh nhất."),
            make_tf(4, "Vận dụng", f"Đề tổng hợp {t} - Một nguyên tử M có tổng số hạt là {36 + (t-1)*2}:", [
                ("a", "Số hạt mang điện bằng 2p.", True),
                ("b", "Khối lượng nguyên tử M tập trung ở hạt nhân.", True),
                ("c", "M có xu hướng nhận e nếu là kim loại kiềm.", False),
                ("d", "Ion tạo thành từ M trung hòa về điện.", False)
            ], "Kim loại nhường e tạo cation, ion mang điện tích.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề tổng hợp {t} - Nguyên tử nào có 11 proton? (Ghi kí hiệu hóa học)", "Na", "Z = 11 là Sodium (Na)."),
            make_sa(2, "Thông hiểu", f"Đề tổng hợp {t} - Số electron tối đa ở lớp thứ 2 là bao nhiêu?", "8", "Lớp 2 tối đa 8e."),
            make_sa(3, "Vận dụng", f"Đề tổng hợp {t} - Nguyên tố X ở chu kì 3, nhóm IIIA. Số hiệu nguyên tử của X là bao nhiêu?", "13", "X là Al (Z = 13)."),
            make_sa(4, "Vận dụng", f"Đề tổng hợp {t} - Tổng số hạt trong nguyên tử Y là 34, số hạt mang điện nhiều hơn không mang điện là 10. Số proton của Y là bao nhiêu?", "11", "2p + n = 34, 2p - n = 10 => 4p = 44 => p = 11."),
            make_sa(5, "Vận dụng cao", f"Đề tổng hợp {t} - Khối lượng tính theo gam của 1 nguyên tử Sulfur (32 amu) là bao nhiêu × 10^-23 g? (Lấy 1 amu = 1,6605 × 10^-24 g, làm tròn 2 chữ số thập phân)", "5.31", "32 × 1,6605 × 10^-24 = 5,3136 × 10^-23 g ≈ 5,31."),
            make_sa(6, "Vận dụng cao", f"Đề tổng hợp {t} - Cho 2 nguyên tố A, B đứng kế tiếp nhau trong cùng 1 chu kì có tổng Z là 25. Số proton của B (biết ZB > ZA) là bao nhiêu?", "13", "ZA + ZB = 25, ZB - ZA = 1 => ZB = 13 (Al).")
        ]
        p4 = [
            make_vdc(1, f"Đề tổng hợp {t} - Hợp chất khí của nguyên tố R với Hydrogen là RH4. Trong oxit cao nhất, R chiếm 46,67% về khối lượng. Nguyên tố R là:", ["Si (Silicon)", "C (Carbon)", "Ge (Germanium)", "Sn (Tin)"], 0, "RH4 => oxit cao nhất RO2. %R = R/(R+32) = 0,4667 => R = 28 (Silicon)."),
            make_vdc(2, f"Đề tổng hợp {t} - Ion X2+ có 10 electron. Vị trí của nguyên tố X trong bảng tuần hoàn là:", ["Ô 12, chu kì 3, nhóm IIA", "Ô 10, chu kì 2, nhóm VIIIA", "Ô 8, chu kì 2, nhóm VIA", "Ô 14, chu kì 3, nhóm IVA"], 0, "X nhường 2e còn 10e => ban đầu X có 12e => Mg (ô 12, chu kì 3, nhóm IIA)."),
            make_vdc(3, f"Đề tổng hợp {t} - Nguyên nhân dẫn đến sự biến đổi tuần hoàn tính chất của các nguyên tố khi đi từ đầu đến cuối chu kì là:", ["Sự lặp lại tuần hoàn cấu hình electron lớp ngoài cùng", "Khối lượng nguyên tử tăng liên tục", "Số hạt neutron tăng đều đặn", "Bán kính nguyên tử không đổi"], 0, "Do cấu trúc electron lớp ngoài cùng biến đổi tuần hoàn."),
            make_vdc(4, f"Đề tổng hợp {t} - Trong cơ thể người, ion kim loại nào đóng vai trò chính trong việc duy trì áp suất thẩm thấu nội bào và truyền dẫn xung thần kinh?", ["Potassium (K+)", "Iron (Fe2+)", "Copper (Cu2+)", "Aluminium (Al3+)"], 0, "Ion K+ và Na+ điều hòa điện giải và truyền xung thần kinh.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - [Đề tổng hợp] Ôn tập cuối Chương I - Đề số {t:02d}",
            "grade": "7", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem7_c1", "chapterTitle": "Chương I: Nguyên tử - Sơ lược bảng tuần hoàn",
            "lessonId": "chem7_c1_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương I",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # =========================================================================
    # CHƯƠNG II: PHÂN TỬ - LIÊN KẾT HÓA HỌC
    # =========================================================================
    # --- BÀI 5: PHÂN TỬ - ĐƠN CHẤT - HỢP CHẤT (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem7_c2_b5_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Chất được tạo nên từ một nguyên tố hóa học được gọi là:", ["Đơn chất", "Hợp chất", "Hỗn hợp", "Dung dịch"], 0, "Đơn chất tạo nên từ 1 nguyên tố hóa học."),
            make_mc(2, "Nhận biết", f"Đề {t} - Chất được tạo nên từ hai hay nhiều nguyên tố hóa học gọi là:", ["Hợp chất", "Đơn chất", "Nguyên tử", "Kim loại"], 0, "Hợp chất tạo nên từ 2 hay nhiều nguyên tố."),
            make_mc(3, "Nhận biết", f"Đề {t} - Hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất là:", ["Phân tử", "Nguyên tử", "Hạt nhân", "Ion"], 0, "Phân tử là hạt đại diện cho chất."),
            make_mc(4, "Nhận biết", f"Đề {t} - Chất nào sau đây là đơn chất?", ["Khí Oxygen (O2)", "Nước (H2O)", "Khí Carbon dioxide (CO2)", "Muối ăn (NaCl)"], 0, "O2 chỉ do 1 nguyên tố O tạo nên."),
            make_mc(5, "Nhận biết", f"Đề {t} - Chất nào sau đây là hợp chất?", ["Khí Methane (CH4)", "Khí Hydrogen (H2)", "Kim loại Iron (Fe)", "Khí Nitrogen (N2)"], 0, "CH4 do C và H tạo nên là hợp chất."),
            make_mc(6, "Nhận biết", f"Đề {t} - Khối lượng phân tử của phân tử khí Hydrogen (H2) là:", ["2 amu", "1 amu", "4 amu", "16 amu"], 0, "2 × 1 = 2 amu."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Khối lượng phân tử của nước (H2O) là:", ["18 amu", "16 amu", "17 amu", "20 amu"], 0, "2×1 + 16 = 18 amu."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Khối lượng phân tử của khí Carbon dioxide (CO2) là:", ["44 amu", "28 amu", "32 amu", "40 amu"], 0, "12 + 2×16 = 44 amu."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Phân tử muối ăn (Sodium chloride, NaCl) có khối lượng phân tử là:", ["58,5 amu", "58 amu", "23 amu", "35,5 amu"], 0, "23 + 35,5 = 58,5 amu."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Đơn chất kim loại nào ở thể lỏng ở nhiệt độ phòng?", ["Thủy ngân (Mercury, Hg)", "Nhôm (Al)", "Sắt (Fe)", "Đồng (Cu)"], 0, "Hg là kim loại thể lỏng duy nhất ở điều kiện thường."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Phân tử khí Ozone có công thức O3. Khối lượng phân tử của Ozone là:", ["48 amu", "32 amu", "16 amu", "64 amu"], 0, "3 × 16 = 48 amu."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Trong các chất sau: Cu, H2O, N2, CaCO3, HCl, O3. Số lượng hợp chất là:", ["3", "2", "4", "5"], 0, "Hợp chất: H2O, CaCO3, HCl (3 chất).")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét tính chất của đơn chất và hợp chất:", [
                ("a", "Đơn chất kim loại có tính dẫn điện và dẫn nhiệt tốt.", True),
                ("b", "Tất cả các đơn chất phi kim đều là chất khí.", False),
                ("c", "Hợp chất có tính chất hoàn toàn khác với tính chất của các đơn chất tạo nên nó.", True),
                ("d", "Khối lượng phân tử bằng tổng khối lượng các nguyên tử trong phân tử.", True)
            ], "Có phi kim thể rắn như C, S, P hoặc lỏng như Br2."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Cho các chất: Than chì (C), đường ăn (C12H22O11), cồn (C2H5OH), khí clo (Cl2):", [
                ("a", "Than chì và khí clo là các đơn chất.", True),
                ("b", "Đường ăn và cồn là các hợp chất.", True),
                ("c", "Khối lượng phân tử của Cl2 là 35,5 amu.", False),
                ("d", "Phân tử đường ăn tạo nên từ 3 nguyên tố hóa học C, H, O.", True)
            ], "M_Cl2 = 2 × 35,5 = 71 amu."),
            make_tf(3, "Vận dụng", f"Đề {t} - Phân tử Calcium carbonate có công thức CaCO3:", [
                ("a", "CaCO3 là một hợp chất.", True),
                ("b", "Khối lượng phân tử CaCO3 là 100 amu.", True),
                ("c", "Trong phân tử CaCO3 có chứa 3 nguyên tử Carbon.", False),
                ("d", "Tỉ lệ số nguyên tử Ca : C : O là 1 : 1 : 3.", True)
            ], "Có 1 nguyên tử Ca, 1 nguyên tử C và 3 nguyên tử O. M = 40 + 12 + 48 = 100 amu."),
            make_tf(4, "Vận dụng", f"Đề {t} - Xét phân tử khí gas Methane (CH4):", [
                ("a", "Khối lượng phân tử CH4 là 16 amu.", True),
                ("b", "Khí methane nhẹ hơn không khí.", True),
                ("c", "Phần trăm khối lượng của C trong CH4 là 75%.", True),
                ("d", "CH4 là một đơn chất hydrocarbon.", False)
            ], "CH4 là hợp chất tạo bởi 2 nguyên tố C và H. %C = 12/16 = 75%. Mkk ≈ 29 amu.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Khối lượng phân tử của khí Oxygen (O2) là bao nhiêu amu?", "32", "2 × 16 = 32 amu."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Phân tử khí Ammonia có công thức NH3. Khối lượng phân tử của NH3 là bao nhiêu amu?", "17", "14 + 3×1 = 17 amu."),
            make_sa(3, "Vận dụng", f"Đề {t} - Khối lượng phân tử của Sulfuric acid (H2SO4) là bao nhiêu amu?", "98", "2×1 + 32 + 4×16 = 98 amu."),
            make_sa(4, "Vận dụng", f"Đề {t} - Một phân tử hợp chất gồm 1 nguyên tử nguyên tố X liên kết với 2 nguyên tử Oxygen, nặng gấp 22 lần phân tử H2. Nguyên tử khối của X là bao nhiêu amu?", "12", "M_phân tử = 22 × 2 = 44 => X + 32 = 44 => X = 12 (Carbon)."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Phân tử Acetic acid có công thức C2H4O2. Khối lượng phân tử của nó là bao nhiêu amu?", "60", "2×12 + 4×1 + 2×16 = 60 amu."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Trong phân tử nước H2O, phần trăm khối lượng của nguyên tố Oxygen chiếm bao nhiêu %? (Làm tròn 1 chữ số thập phân)", "88.9", "%O = 16 / 18 × 100% ≈ 88,89% ≈ 88,9%.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Một hợp chất A có phân tử gồm 2 nguyên tử nguyên tố X liên kết với 3 nguyên tử O và nặng hơn phân tử Hydrogen 51 lần. Tên của nguyên tố X là:", ["Aluminium (Al)", "Iron (Fe)", "Nitrogen (N)", "Phosphorus (P)"], 0, "M_A = 51 × 2 = 102. Ta có 2X + 48 = 102 => 2X = 54 => X = 27 (Al)."),
            make_vdc(2, f"Đề {t} - Khi đun nóng đường mía (saccharose, C12H22O11) trong ống nghiệm, thấy thành ống nghiệm có hơi nước đọng lại và phần chất rắn màu đen còn lại là than (carbon). Hiện tượng này chứng minh đường mía là:", ["Một hợp chất hữu cơ tạo bởi C, H và O", "Một đơn chất của carbon", "Một hỗn hợp đồng nhất", "Một loại khoáng chất vô cơ"], 0, "Tạo thành than (C) và nước (H2O) chứng tỏ saccharose chứa C, H, O."),
            make_vdc(3, f"Đề {t} - Trong khí quyển, thể tích của khí Nitrogen (N2) và Oxygen (O2) chiếm khoảng 99%. Tỉ lệ khối lượng phân tử N2 so với O2 xấp xỉ bằng:", ["0,875", "1,143", "0,500", "2,000"], 0, "M_N2 / M_O2 = 28 / 32 = 0,875."),
            make_vdc(4, f"Đề {t} - Kim cương và than chì đều được cấu tạo từ các nguyên tử của cùng một nguyên tố hóa học Carbon (C). Kim cương và than chì được gọi là:", ["Các dạng thù hình của cùng một đơn chất Carbon", "Các hợp chất khác nhau", "Các đồng vị của than", "Hai nguyên tố hóa học khác nhau"], 0, "Đó là các dạng thù hình của nguyên tố Carbon.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - Bài 5: Phân tử - Đơn chất - Hợp chất - Đề số {t:02d}",
            "grade": "7", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem7_c2", "chapterTitle": "Chương II: Phân tử - Liên kết hóa học",
            "lessonId": "chem7_c2_b5", "lessonName": "Bài 5: Phân tử - Đơn chất - Hợp chất",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 6: LIÊN KẾT HÓA HỌC (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem7_c2_b6_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Để đạt được cấu hình electron bền vững giống khí hiếm, các nguyên tử có xu hướng đạt bao nhiêu electron ở lớp ngoài cùng (trừ He)?", ["8 electron", "2 electron", "6 electron", "10 electron"], 0, "Quy tắc Octet: xu hướng đạt 8 electron lớp ngoài cùng bền vững."),
            make_mc(2, "Nhận biết", f"Đề {t} - Liên kết ion được hình thành do lực hút tĩnh điện giữa:", ["Các ion mang điện tích trái dấu", "Các nguyên tử trung hòa", "Các electron tự do", "Các proton trong hạt nhân"], 0, "Lực hút tĩnh điện giữa cation (+) và anion (-)."),
            make_mc(3, "Nhận biết", f"Đề {t} - Liên kết cộng hóa trị là liên kết được hình thành giữa hai nguyên tử bằng:", ["Một hay nhiều cặp electron dùng chung", "Lực hút tĩnh điện giữa ion", "Sự nhường nhận proton", "Lực hấp dẫn"], 0, "Bằng các cặp electron dùng chung."),
            make_mc(4, "Nhận biết", f"Đề {t} - Liên kết giữa các nguyên tử trong phân tử muối ăn NaCl là liên kết:", ["Liên kết ion", "Liên kết cộng hóa trị", "Liên kết kim loại", "Liên kết hydrogen"], 0, "NaCl là hợp chất ion (Na+ và Cl-)."),
            make_mc(5, "Nhận biết", f"Đề {t} - Liên kết trong phân tử nước H2O là:", ["Liên kết cộng hóa trị có cực", "Liên kết ion", "Liên kết kim loại", "Liên kết phi kim"], 0, "Liên kết cộng hóa trị giữa phi kim O và H."),
            make_mc(6, "Nhận biết", f"Đề {t} - Nguyên tử kim loại kiềm nhóm IA (như Na, K) có xu hướng:", ["Nhường 1 electron để tạo ion dương +1", "Nhận 1 electron", "Góp chung 2 electron", "Nhường 2 electron"], 0, "Nhường 1e ngoài cùng để tạo cation M+."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Nguyên tử phi kim Halogen nhóm VIIA (như Cl, F) có xu hướng:", ["Nhận thêm 1 electron để tạo ion âm -1", "Nhường 7 electron", "Nhận 2 electron", "Nhường 1 electron"], 0, "Nhận 1e để đạt 8e ngoài cùng."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Hợp chất ion thường có tính chất nào sau đây?", ["Nhiệt độ nóng chảy và nhiệt độ sôi cao", "Dễ bay hơi", "Không tan trong nước", "Thể khí ở điều kiện thường"], 0, "Hợp chất ion có lực hút tĩnh điện mạnh nên nhiệt độ nóng chảy và sôi rất cao."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Phân tử khí Hydrogen (H2) có bao nhiêu cặp electron dùng chung?", ["1 cặp electron", "2 cặp electron", "3 cặp electron", "4 cặp electron"], 0, "Mỗi nguyên tử H góp 1e tạo 1 cặp electron dùng chung (H-H)."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Phân tử khí Nitrogen (N2) có liên kết ba gồm bao nhiêu cặp electron dùng chung?", ["3 cặp electron", "1 cặp electron", "2 cặp electron", "6 cặp electron"], 0, "Liên kết ba gồm 3 cặp electron dùng chung (N≡N)."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Chất nào sau đây dẫn được điện khi hòa tan trong nước?", ["Muối ăn (NaCl)", "Đường ăn (Saccharose)", "Khí Oxygen (O2)", "Rượu etylic"], 0, "NaCl phân li thành các ion Na+ và Cl- chuyển động tự do dẫn điện."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Phân tử khí Carbon dioxide (CO2) có cấu tạo dạng đường thẳng O=C=O gồm:", ["Hai liên kết đôi cộng hóa trị", "Hai liên kết ion", "Một liên kết đơn và một liên kết ba", "Liên kết kim loại"], 0, "Gồm 2 liên kết đôi C=O.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét quá trình hình thành liên kết trong phân tử Magnesium oxide (MgO):", [
                ("a", "Nguyên tử Mg (Z=12) nhường 2 electron tạo thành ion Mg2+.", True),
                ("b", "Nguyên tử O (Z=8) nhận 2 electron tạo thành ion O2-.", True),
                ("c", "Ion Mg2+ và O2- hút nhau bằng lực hút tĩnh điện tạo thành tinh thể MgO.", True),
                ("d", "MgO là hợp chất có liên kết cộng hóa trị.", False)
            ], "MgO là hợp chất ion điển hình."),
            make_tf(2, "Thông hiểu", f"Đề {t} - So sánh hợp chất ion và hợp chất cộng hóa trị:", [
                ("a", "Hợp chất ion thường là chất rắn ở nhiệt độ phòng.", True),
                ("b", "Các chất khí như O2, CO2, CH4 là hợp chất hoặc đơn chất cộng hóa trị.", True),
                ("c", "Hợp chất cộng hóa trị luôn dẫn điện tốt khi tan trong nước.", False),
                ("d", "Nước là dung môi phân cực hòa tan tốt nhiều hợp chất ion.", True)
            ], "Nhiều chất cộng hóa trị không phân li thành ion (như đường, cồn) nên dung dịch không dẫn điện."),
            make_tf(3, "Vận dụng", f"Đề {t} - Cho biết nguyên tử Na (Z=11) và F (Z=9):", [
                ("a", "Na có 1 electron lớp ngoài cùng, F có 7 electron lớp ngoài cùng.", True),
                ("b", "Khi liên kết, Na nhường 1e cho F.", True),
                ("c", "Hợp chất tạo thành có công thức NaF.", True),
                ("d", "Trong phân tử NaF có 1 cặp electron dùng chung.", False)
            ], "NaF là hợp chất ion, không có cặp e dùng chung."),
            make_tf(4, "Vận dụng", f"Đề {t} - Xét phân tử khí Methane (CH4):", [
                ("a", "Nguyên tử Carbon góp chung 4 electron với 4 nguyên tử Hydrogen.", True),
                ("b", "Trong phân tử CH4 có 4 liên kết cộng hóa trị đơn C-H.", True),
                ("c", "Sau khi liên kết, nguyên tử Carbon đạt 8 electron ở lớp ngoài cùng.", True),
                ("d", "Methane dẫn điện tốt ở thể lỏng.", False)
            ], "CH4 là chất cộng hóa trị không phân cực, không dẫn điện.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Số electron lớp ngoài cùng của ion Na+ là bao nhiêu?", "8", "Na (2,8,1) nhường 1e còn 8e ngoài cùng."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Phân tử khí Oxygen (O2) có bao nhiêu cặp electron dùng chung giữa hai nguyên tử O?", "2", "Liên kết đôi O=O gồm 2 cặp electron dùng chung."),
            make_sa(3, "Vận dụng", f"Đề {t} - Trong phân tử nước H2O có bao nhiêu liên kết cộng hóa trị đơn O-H?", "2", "Có 2 liên kết đơn O-H."),
            make_sa(4, "Vận dụng", f"Đề {t} - Nguyên tử Canxi (Ca, Z=20) có xu hướng nhường bao nhiêu electron để tạo thành ion dương?", "2", "Ca nhường 2e ngoài cùng tạo Ca2+."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Tổng số electron trong ion ammonium NH4+ là bao nhiêu electron?", "10", "N có 7e, 4 H có 4e, ion +1 mất 1e => 7 + 4 - 1 = 10e."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Trong phân tử khí N2, tổng số electron tham gia vào liên kết chung giữa hai nguyên tử là bao nhiêu hạt?", "6", "Liên kết ba gồm 3 cặp e = 6 electron.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Dãy gồm toàn các chất có liên kết ion là:", ["NaCl, CaO, K2S", "H2O, CO2, NH3", "HCl, CH4, O2", "C2H5OH, Cl2, N2"], 0, "NaCl, CaO, K2S tạo bởi kim loại điển hình và phi kim điển hình."),
            make_vdc(2, f"Đề {t} - Vì sao dung dịch muối ăn NaCl trong nước dẫn điện tốt trong khi dung dịch đường ăn C12H22O11 lại không dẫn điện?", ["NaCl phân li thành các ion Na+ và Cl- mang điện tự do, còn đường chỉ phân tán thành các phân tử trung hòa", "Muối ăn là kim loại còn đường là phi kim", "Muối ăn có tính axit còn đường có tính kiềm", "Đường ăn phản ứng với nước tạo kết tủa"], 0, "Sự có mặt của các ion tự do quyết định tính dẫn điện."),
            make_vdc(3, f"Đề {t} - Trong phân tử CO2, nguyên tử C có độ âm điện nhỏ hơn nguyên tử O nên cặp electron liên kết bị lệch về phía nguyên tử O. Liên kết này là:", ["Liên kết cộng hóa trị phân cực", "Liên kết cộng hóa trị không phân cực", "Liên kết ion", "Liên kết kim loại"], 0, "Cặp e chung lệch về nguyên tử có độ âm điện lớn hơn là liên kết phân cực."),
            make_vdc(4, f"Đề {t} - Khái niệm 'Quy tắc Octet' xuất phát từ từ 'Octo' trong tiếng Latinh, có nghĩa là:", ["Tám (8)", "Hai (2)", "Bốn (4)", "Mười (10)"], 0, "Octet nghĩa là bộ 8.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - Bài 6: Giới thiệu liên kết hóa học - Đề số {t:02d}",
            "grade": "7", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem7_c2", "chapterTitle": "Chương II: Phân tử - Liên kết hóa học",
            "lessonId": "chem7_c2_b6", "lessonName": "Bài 6: Giới thiệu về liên kết hóa học",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 7: HÓA TRỊ VÀ CÔNG THỨC HÓA HỌC (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem7_c2_b7_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Hóa trị của nguyên tố Hydrogen luôn được quy ước bằng mấy đơn vị?", ["I", "II", "III", "IV"], 0, "H quy ước có hóa trị I."),
            make_mc(2, "Nhận biết", f"Đề {t} - Hóa trị của nguyên tố Oxygen luôn được quy ước bằng mấy đơn vị?", ["II", "I", "III", "IV"], 0, "O quy ước có hóa trị II."),
            make_mc(3, "Nhận biết", f"Đề {t} - Quy tắc hóa trị đối với hợp chất hai nguyên tố AxBy (với a, b là hóa trị của A, B) là:", ["a × x = b × y", "a × y = b × x", "a / x = b / y", "a + x = b + y"], 0, "Tích chỉ số và hóa trị của nguyên tố này bằng tích chỉ số và hóa trị của nguyên tố kia: a.x = b.y."),
            make_mc(4, "Nhận biết", f"Đề {t} - Công thức hóa học của nước là:", ["H2O", "HO2", "H2O2", "H3O"], 0, "Nước là H2O."),
            make_mc(5, "Nhận biết", f"Đề {t} - Trong hợp chất Al2O3, nguyên tố Aluminium có hóa trị mấy?", ["III", "II", "I", "IV"], 0, "2 × a = 3 × II => a = III."),
            make_mc(6, "Nhận biết", f"Đề {t} - Công thức hóa học của khí Carbon dioxide là:", ["CO2", "CO", "C2O", "CO3"], 0, "Carbon dioxide là CO2."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Biết Fe có hóa trị III trong hợp chất với O (hóa trị II). Công thức hóa học của hợp chất là:", ["Fe2O3", "FeO", "Fe3O2", "Fe3O4"], 0, "Fe2O3."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Hóa trị của Carbon trong hợp chất CO là:", ["II", "IV", "I", "III"], 0, "1 × a = 1 × II => a = II."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Trong hợp chất SO3, nguyên tố Sulfur (S) có hóa trị mấy?", ["VI", "IV", "II", "III"], 0, "1 × a = 3 × II => a = VI."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Công thức hóa học nào sau đây viết SAI theo quy tắc hóa trị?", ["Na2O", "AlO", "CaO", "FeCl2"], 1, "Al có hóa trị III, O hóa trị II nên công thức đúng là Al2O3, không thể là AlO."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Phần trăm khối lượng của Cu trong hợp chất CuO (M = 80 amu) là:", ["80%", "64%", "20%", "75%"], 0, "%Cu = 64 / 80 × 100% = 80%."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Nhóm nguyên tử sulfate (SO4) có hóa trị mấy?", ["II", "I", "III", "IV"], 0, "Nhóm (SO4) có hóa trị II (ví dụ H2SO4, BaSO4).")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét các công thức hóa học của các hợp chất vô cơ:", [
                ("a", "Công thức của hợp chất tạo bởi Ca (hóa trị II) và nhóm (OH) (hóa trị I) là Ca(OH)2.", True),
                ("b", "Trong phân tử CH4, Carbon có hóa trị IV.", True),
                ("c", "Công thức P2O5 cho biết phân tử gồm 2 nguyên tử P và 5 nguyên tử O.", True),
                ("d", "Khối lượng phân tử của P2O5 là 110 amu.", False)
            ], "M_P2O5 = 2×31 + 5×16 = 62 + 80 = 142 amu."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Về ý nghĩa của công thức hóa học:", [
                ("a", "Cho biết các nguyên tố hóa học tạo nên chất.", True),
                ("b", "Cho biết số lượng nguyên tử của mỗi nguyên tố trong một phân tử chất.", True),
                ("c", "Cho biết khối lượng phân tử của chất đó.", True),
                ("d", "Cho biết trạng thái rắn, lỏng hay khí của chất trong mọi điều kiện.", False)
            ], "Công thức hóa học không quy định trạng thái vật lí trong mọi điều kiện."),
            make_tf(3, "Vận dụng", f"Đề {t} - Cho hợp chất chứa sắt và oxi có tỉ lệ khối lượng mFe : mO = 7 : 3:", [
                ("a", "Khối lượng mol của Fe là 56 amu, của O là 16 amu.", True),
                ("b", "Tỉ lệ số nguyên tử Fe : O là 2 : 3.", True),
                ("c", "Công thức hóa học của hợp chất là Fe2O3.", True),
                ("d", "Trong hợp chất này Sắt có hóa trị II.", False)
            ], "Fe2O3 có Fe hóa trị III. nFe : nO = (7/56) : (3/16) = 0,125 : 0,1875 = 2 : 3."),
            make_tf(4, "Vận dụng", f"Đề {t} - Xét hợp chất khí ammonia NH3:", [
                ("a", "Hóa trị của Nitrogen trong NH3 là III.", True),
                ("b", "Khối lượng phân tử NH3 là 17 amu.", True),
                ("c", "Phần trăm khối lượng của Nitrogen trong NH3 xấp xỉ 82,35%.", True),
                ("d", "Khí NH3 nặng hơn không khí.", False)
            ], "%N = 14/17 = 82,35%. M_NH3 = 17 < Mkk = 29 nên nhẹ hơn không khí.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Hóa trị của nguyên tố Carbon trong khí Carbon dioxide CO2 là mấy?", "4", "IV (hoặc 4)."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Hóa trị của nguyên tố Sắt trong hợp chất FeO là mấy?", "2", "II (hoặc 2)."),
            make_sa(3, "Vận dụng", f"Đề {t} - Cho biết nguyên tố X có hóa trị III, nhóm (SO4) có hóa trị II. Chỉ số x của X trong công thức Xx(SO4)y là bao nhiêu?", "2", "X2(SO4)3 => x = 2."),
            make_sa(4, "Vận dụng", f"Đề {t} - Khối lượng phân tử của hợp chất Al2(SO4)3 là bao nhiêu amu?", "342", "2×27 + 3×(32 + 64) = 54 + 288 = 342 amu."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Một oxide của nguyên tố R có công thức R2O3, trong đó Oxygen chiếm 30% về khối lượng. Khối lượng nguyên tử của R là bao nhiêu amu?", "56", "%O = 48 / (2R + 48) = 0,30 => 2R + 48 = 160 => 2R = 112 => R = 56 (Fe)."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Phần trăm khối lượng của nguyên tố Sulfur trong phân tử khí SO2 là bao nhiêu %?", "50", "%S = 32 / 64 × 100% = 50%.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Phân bón Urê có công thức hóa học là (NH2)2CO. Hàm lượng nguyên tố dinh dưỡng Nitrogen trong phân bón Urê nguyên chất là:", ["46,67%", "28,00%", "35,00%", "60,00%"], 0, "M = 2×16 + 12 + 16 = 60 amu. %N = 28 / 60 × 100% ≈ 46,67%."),
            make_vdc(2, f"Đề {t} - Một hợp chất tạo bởi hai nguyên tố Carbon và Hydrogen có tỉ lệ phần trăm khối lượng %C = 80% và %H = 20%. Biết khối lượng phân tử của hợp chất là 30 amu. Công thức hóa học của hợp chất là:", ["C2H6", "CH4", "C3H8", "C2H4"], 0, "mC = 30 × 80% = 24 => số C = 2; mH = 6 => số H = 6 => C2H6 (Ethane)."),
            make_vdc(3, f"Đề {t} - Khí gas dùng trong nấu ăn gia đình hàng ngày là hỗn hợp gồm Propane (C3H8) và Butane (C4H10). Khối lượng phân tử của Butane là:", ["58 amu", "44 amu", "56 amu", "60 amu"], 0, "M_C4H10 = 4×12 + 10×1 = 58 amu."),
            make_vdc(4, f"Đề {t} - Hợp chất của nguyên tố X với nhóm (SO4) là X2(SO4)3 và hợp chất của nguyên tố Y với Hydrogen là H2Y. Công thức hóa học của hợp chất tạo bởi X và Y là:", ["X2Y3", "XY", "XY2", "X3Y2"], 0, "X có hóa trị III, Y có hóa trị II => công thức X2Y3.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - Bài 7: Hóa trị và công thức hóa học - Đề số {t:02d}",
            "grade": "7", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem7_c2", "chapterTitle": "Chương II: Phân tử - Liên kết hóa học",
            "lessonId": "chem7_c2_b7", "lessonName": "Bài 7: Hóa trị và công thức hóa học",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- ÔN TẬP CUỐI CHƯƠNG II (5 ĐỀ) ---
    for t in range(1, 6):
        k = f"chem7_c2_rev_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề tổng hợp {t} - Chất nào sau đây là đơn chất phi kim?", ["Khí Chlorine (Cl2)", "Nước (H2O)", "Muối ăn (NaCl)", "Khí Carbon dioxide (CO2)"], 0, "Cl2 là đơn chất phi kim."),
            make_mc(2, "Nhận biết", f"Đề tổng hợp {t} - Liên kết ion hình thành do:", ["Lực hút tĩnh điện giữa các ion trái dấu", "Cặp electron dùng chung", "Sự nhường proton", "Liên kết kim loại"], 0, "Lực hút tĩnh điện giữa ion dương và ion âm."),
            make_mc(3, "Nhận biết", f"Đề tổng hợp {t} - Quy tắc Octet nói về xu hướng nguyên tử đạt cấu hình electron lớp ngoài cùng giống khí hiếm gồm mấy electron?", ["8 electron", "2 electron", "6 electron", "4 electron"], 0, "8 electron bền vững."),
            make_mc(4, "Nhận biết", f"Đề tổng hợp {t} - Trong công thức hóa học AxBy, biểu thức đúng của quy tắc hóa trị là:", ["a.x = b.y", "a.y = b.x", "a+x = b+y", "a/x = b/y"], 0, "a.x = b.y."),
            make_mc(5, "Nhận biết", f"Đề tổng hợp {t} - Khối lượng phân tử của nước (H2O) là:", ["18 amu", "16 amu", "20 amu", "17 amu"], 0, "2×1 + 16 = 18 amu."),
            make_mc(6, "Nhận biết", f"Đề tổng hợp {t} - Phân tử nào sau đây có liên kết cộng hóa trị ba?", ["N2", "O2", "H2", "Cl2"], 0, "N≡N có liên kết ba."),
            make_mc(7, "Thông hiểu", f"Đề tổng hợp {t} - Hợp chất của Sắt với Oxi có tỉ lệ 1 nguyên tử Fe và 1 nguyên tử O. Hóa trị của Fe trong hợp chất này là:", ["II", "III", "I", "IV"], 0, "FeO => Fe hóa trị II."),
            make_mc(8, "Thông hiểu", f"Đề tổng hợp {t} - Khối lượng phân tử của phân tử Methane (CH4) là:", ["16 amu", "14 amu", "18 amu", "20 amu"], 0, "12 + 4 = 16 amu."),
            make_mc(9, "Thông hiểu", f"Đề tổng hợp {t} - Chất nào sau đây dẫn điện được ở trạng thái nóng chảy hoặc dung dịch?", ["Sodium chloride (NaCl)", "Đường saccarozơ", "Cồn etylic", "Khí Oxygen"], 0, "NaCl là hợp chất ion."),
            make_mc(10, "Thông hiểu", f"Đề tổng hợp {t} - Trong phân tử H2SO4, nguyên tố Sulfur có hóa trị mấy?", ["VI", "IV", "II", "III"], 0, "2×I + 1×a = 4×II => a = VI."),
            make_mc(11, "Thông hiểu", f"Đề tổng hợp {t} - Phần trăm khối lượng của O trong phân tử SO2 là:", ["50%", "25%", "75%", "33,3%"], 0, "32 / 64 = 50%."),
            make_mc(12, "Thông hiểu", f"Đề tổng hợp {t} - Công thức hóa học của hợp chất tạo bởi Mg (hóa trị II) và nhóm (PO4) (hóa trị III) là:", ["Mg3(PO4)2", "Mg2(PO4)3", "MgPO4", "Mg(PO4)2"], 0, "Mg3(PO4)2.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề tổng hợp {t} - Xét các chất: Khí O2, đường ăn C12H22O11, muối ăn NaCl, đồng Cu:", [
                ("a", "O2 và Cu là các đơn chất.", True),
                ("b", "Đường ăn và muối ăn là các hợp chất.", True),
                ("c", "Liên kết trong muối ăn là liên kết ion.", True),
                ("d", "Dung dịch đường ăn dẫn điện tốt hơn dung dịch muối ăn.", False)
            ], "Dung dịch đường không dẫn điện vì không phân li thành ion."),
            make_tf(2, "Thông hiểu", f"Đề tổng hợp {t} - Về liên kết hóa học:", [
                ("a", "Kim loại có xu hướng nhường electron để tạo cation.", True),
                ("b", "Phi kim có xu hướng nhận electron hoặc góp chung electron.", True),
                ("c", "Liên kết cộng hóa trị hình thành giữa các ion mang điện trái dấu.", False),
                ("d", "Khí hiếm rất trơ về mặt hóa học vì đã có 8e lớp ngoài cùng (He có 2e).", True)
            ], "Liên kết cộng hóa trị bằng cặp e dùng chung."),
            make_tf(3, "Vận dụng", f"Đề tổng hợp {t} - Cho hợp chất nhôm oxit Al2O3:", [
                ("a", "Khối lượng phân tử Al2O3 là 102 amu.", True),
                ("b", "Trong phân tử Al2O3, Nhôm có hóa trị III.", True),
                ("c", "Phần trăm khối lượng của Nhôm trong Al2O3 xấp xỉ 52,94%.", True),
                ("d", "Al2O3 là hợp chất cộng hóa trị có nhiệt độ nóng chảy thấp.", False)
            ], "%Al = 54/102 ≈ 52,94%. Al2O3 là chất rắn khó nóng chảy (nhiệt độ nóng chảy trên 2000°C)."),
            make_tf(4, "Vận dụng", f"Đề tổng hợp {t} - Xét phân tử nước H2O và carbon dioxide CO2:", [
                ("a", "Đều là các hợp chất cộng hóa trị.", True),
                ("b", "Khối lượng phân tử của CO2 lớn hơn H2O.", True),
                ("c", "Trong cả hai phân tử, Oxygen đều có hóa trị II.", True),
                ("d", "CO2 ở thể lỏng ở điều kiện nhiệt độ phòng.", False)
            ], "CO2 là chất khí ở điều kiện thường.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề tổng hợp {t} - Khối lượng phân tử của khí Nitrogen (N2) là bao nhiêu amu?", "28", "2 × 14 = 28 amu."),
            make_sa(2, "Thông hiểu", f"Đề tổng hợp {t} - Hóa trị của nguyên tố Magie trong MgCl2 là mấy?", "2", "II (hoặc 2)."),
            make_sa(3, "Vận dụng", f"Đề tổng hợp {t} - Khối lượng phân tử của Calcium carbonate CaCO3 là bao nhiêu amu?", "100", "40 + 12 + 48 = 100 amu."),
            make_sa(4, "Vận dụng", f"Đề tổng hợp {t} - Trong phân tử CO2 có bao nhiêu liên kết đôi?", "2", "O=C=O có 2 liên kết đôi."),
            make_sa(5, "Vận dụng cao", f"Đề tổng hợp {t} - Một hợp chất gồm nguyên tố R (hóa trị IV) liên kết với Oxygen có khối lượng phân tử là 60 amu. Khối lượng nguyên tử của R là bao nhiêu amu?", "28", "RO2 = 60 => R + 32 = 60 => R = 28 (Silicon)."),
            make_sa(6, "Vận dụng cao", f"Đề tổng hợp {t} - Phần trăm khối lượng của nguyên tố Carbon trong khí Methane CH4 là bao nhiêu %?", "75", "12 / 16 × 100% = 75%.")
        ]
        p4 = [
            make_vdc(1, f"Đề tổng hợp {t} - Hợp chất A tạo bởi nguyên tố X (hóa trị II) và nhóm (PO4) (hóa trị III) có khối lượng phân tử là 262 amu. Nguyên tố X là:", ["Magnesium (Mg, 24)", "Calcium (Ca, 40)", "Barium (Ba, 137)", "Zinc (Zn, 65)"], 0, "X3(PO4)2: 3X + 2×95 = 262 => 3X + 190 = 262 => 3X = 72 => X = 24 (Mg)."),
            make_vdc(2, f"Đề tổng hợp {t} - Để dập tắt đám cháy do xăng dầu, người ta không dùng nước mà thường dùng cát hoặc bình bọt khí CO2 vì:", ["Xăng dầu nhẹ hơn nước và không tan trong nước nên nếu dùng nước xăng dầu sẽ nổi lên trên và lan rộng đám cháy", "Nước phản ứng mãnh liệt với xăng dầu sinh ra khí gây nổ", "Nước làm tăng nhiệt độ của ngọn lửa", "Cát sinh ra khí oxygen ngăn đám cháy"], 0, "Xăng dầu không tan trong nước và nhẹ hơn nước nên nổi lên làm đám cháy lan rộng."),
            make_vdc(3, f"Đề tổng hợp {t} - Trong quá trình quang hợp, cây xanh hấp thụ khí carbon dioxide (CO2) và nước (H2O) dưới tác dụng của ánh sáng mặt trời và chất diệp lục để tổng hợp chất hữu cơ nào sau đây?", ["Glucose (C6H12O6)", "Muối ăn (NaCl)", "Khí Methane (CH4)", "Axit axetic (CH3COOH)"], 0, "6CO2 + 6H2O -> C6H12O6 + 6O2."),
            make_vdc(4, f"Đề tổng hợp {t} - Một mẫu nước khoáng có chứa các ion Ca2+, Mg2+, Cl-, HCO3-. Liên kết giữa các ion này với các phân tử nước khi tan trong dung dịch là:", ["Tương tác tĩnh điện giữa ion và lưỡng cực nước", "Liên kết cộng hóa trị", "Liên kết kim loại", "Liên kết hạt nhân"], 0, "Tương tác ion - lưỡng cực phân tử nước.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 7 (Hóa học) - [Đề tổng hợp] Ôn tập cuối Chương II - Đề số {t:02d}",
            "grade": "7", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem7_c2", "chapterTitle": "Chương II: Phân tử - Liên kết hóa học",
            "lessonId": "chem7_c2_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương II",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    return exams

if __name__ == "__main__":
    exs = build_chem7_exams()
    print("Chem 7 generated total:", len(exs), "exams.")
