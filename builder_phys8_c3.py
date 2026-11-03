# -*- coding: utf-8 -*-
"""
BUILDER FOR CHƯƠNG III: KHỐI LƯỢNG RIÊNG VÀ ÁP SUẤT (20 ĐỀ THI)
- phys8_c3_b13: 3 đề
- phys8_c3_b14: 3 đề
- phys8_c3_b15: 3 đề
- phys8_c3_b16: 3 đề
- phys8_c3_b17: 3 đề
- phys8_c3_rev: 5 đề
Độc lập 100%, không trùng lặp câu hỏi trong cùng một bài học.
Không có tiền tố 'Đề X - ' hay dòng chờ 'Đáp số: ......'.
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

def build_c3():
    exams = {}
    ch_id = "phys8_c3"
    ch_title = "Chương III: Khối lượng riêng và áp suất"

    # =========================================================================
    # BÀI 13: KHỐI LƯỢNG RIÊNG (3 ĐỀ)
    # =========================================================================
    # --- TEST 1 ---
    exams["phys8_c3_b13_test1"] = {
        "title": "Đề kiểm tra KHTN 8 (Vật lý) - Bài 13: Khối lượng riêng - Đề số 01",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title,
        "lessonId": "phys8_c3_b13", "lessonName": "Bài 13: Khối lượng riêng",
        "testNum": 1, "duration": "45 phút", "points": 10.0,
        "part1": [
            make_mc(1, "Nhận biết", "Khối lượng riêng của một chất là:", ["Khối lượng của một đơn vị thể tích chất đó", "Trọng lượng của một mét khối chất đó", "Thể tích của một kilôgam chất đó", "Khối lượng của toàn bộ vật thể"], 0, "Khối lượng riêng D = m / V đặc trưng cho khối lượng của 1 đơn vị thể tích chất đó."),
            make_mc(2, "Nhận biết", "Công thức tính khối lượng riêng của một vật là:", ["D = m / V", "D = m × V", "D = V / m", "D = P / V"], 0, "D = m / V."),
            make_mc(3, "Nhận biết", "Đơn vị hợp pháp của khối lượng riêng trong hệ SI là:", ["kg/m³", "g/cm³", "kg/L", "N/m³"], 0, "Đơn vị đo khối lượng riêng trong hệ SI là kg/m³."),
            make_mc(4, "Nhận biết", "Mối liên hệ giữa 1 g/cm³ và kg/m³ là:", ["1 g/cm³ = 1 000 kg/m³", "1 g/cm³ = 100 kg/m³", "1 g/cm³ = 10 kg/m³", "1 g/cm³ = 0,001 kg/m³"], 0, "1 g/cm³ = 10^-3 kg / 10^-6 m³ = 1 000 kg/m³."),
            make_mc(5, "Nhận biết", "Khối lượng riêng của nước cất ở nhiệt độ 4 °C xấp xỉ bằng:", ["1 000 kg/m³", "100 kg/m³", "10 kg/m³", "800 kg/m³"], 0, "Ở 4 °C nước có khối lượng riêng lớn nhất là 1 000 kg/m³."),
            make_mc(6, "Nhận biết", "Để xác định khối lượng riêng của một chất cần biết hai đại lượng là:", ["Khối lượng và thể tích của vật", "Trọng lượng và độ cao của vật", "Diện tích đáy và chiều cao của vật", "Áp suất và nhiệt độ của vật"], 0, "Biết khối lượng m và thể tích V thì tính được D = m/V."),
            make_mc(7, "Thông hiểu", "Một khối sắt có thể tích 0,5 m³ và khối lượng riêng 7 800 kg/m³. Khối lượng của khối sắt là:", ["3 900 kg", "7 800 kg", "15 600 kg", "1 560 kg"], 0, "m = D × V = 7 800 × 0,5 = 3 900 kg."),
            make_mc(8, "Thông hiểu", "Một bình chứa 2 lít dầu ăn có khối lượng 1,6 kg. Khối lượng riêng của dầu ăn là:", ["800 kg/m³", "850 kg/m³", "900 kg/m³", "1 600 kg/m³"], 0, "V = 2 L = 0,002 m³. D = 1,6 / 0,002 = 800 kg/m³."),
            make_mc(9, "Thông hiểu", "Khi cưa một thanh gỗ đồng chất thành hai nửa bằng nhau thì khối lượng riêng của mỗi nửa thanh gỗ:", ["Không đổi", "Tăng gấp đôi", "Giảm đi một nửa", "Giảm đi bốn lần"], 0, "Khối lượng riêng là thuộc tính của chất, không phụ thuộc vào kích thước hay khối lượng vật."),
            make_mc(10, "Thông hiểu", "Biết khối lượng riêng của nhôm là 2 700 kg/m³, của sắt là 7 800 kg/m³. So sánh thể tích của hai khối nhôm và sắt có cùng khối lượng:", ["Khối nhôm có thể tích lớn hơn khoảng 2,89 lần khối sắt", "Khối sắt có thể tích lớn hơn khối nhôm", "Hai khối có thể tích bằng nhau", "Khối nhôm có thể tích nhỏ hơn một nửa khối sắt"], 0, "Cùng m: V = m/D. Vì D_nhôm < D_sắt nên V_nhôm > V_sắt (7800 / 2700 ≈ 2,89 lần)."),
            make_mc(11, "Thông hiểu", "Một chiếc can chứa 5 lít cồn có khối lượng riêng 800 kg/m³. Khối lượng của lượng cồn trong can là:", ["4 kg", "4,5 kg", "5 kg", "6,25 kg"], 0, "V = 5 L = 0,005 m³. m = D × V = 800 × 0,005 = 4 kg."),
            make_mc(12, "Thông hiểu", "Khi đun nóng một lượng nước từ 20 °C đến 80 °C thì:", ["Khối lượng không đổi nhưng khối lượng riêng giảm", "Cả khối lượng và khối lượng riêng đều tăng", "Khối lượng tăng còn khối lượng riêng giảm", "Cả khối lượng và thể tích đều không đổi"], 0, "Khi đun nóng, nước nở ra làm thể tích V tăng trong khi m không đổi, do đó D = m/V giảm.")
        ],
        "part2": [
            make_tf(1, "Thông hiểu", "Cho biết khối lượng riêng của nước là 1 000 kg/m³ và của chì là 11 300 kg/m³:", [
                ("a", "Một mét khối nước có khối lượng là 1 000 kg.", True),
                ("b", "Chì có khối lượng riêng lớn hơn nước gấp 11,3 lần.", True),
                ("c", "Nếu lấy cùng thể tích 1 lít thì khối lượng của chì nhẹ hơn nước.", False),
                ("d", "Khối lượng riêng của chì là 11,3 g/cm³.", True)
            ], "11 300 kg/m³ = 11,3 g/cm³. Cùng 1 lít thì chì nặng 11,3 kg còn nước nặng 1 kg."),
            make_tf(2, "Thông hiểu", "Xét các tính chất liên quan đến khối lượng riêng của một chất rắn đồng nhất:", [
                ("a", "Khối lượng riêng là khối lượng của một đơn vị thể tích của chất đó.", True),
                ("b", "Khi cắt một khối đồng thành 4 phần thì khối lượng riêng của mỗi phần giảm đi 4 lần.", False),
                ("c", "Hai vật làm từ cùng một chất có thể có thể tích khác nhau nhưng khối lượng riêng bằng nhau.", True),
                ("d", "Đơn vị g/cm³ lớn hơn đơn vị kg/m³.", True)
            ], "Khối lượng riêng không đổi khi chia nhỏ vật. 1 g/cm³ = 1000 kg/m³."),
            make_tf(3, "Vận dụng", "Một khối đá hình hộp chữ nhật có kích thước dài 0,8 m, rộng 0,5 m, cao 0,2 m và có khối lượng 208 kg:", [
                ("a", "Thể tích của khối đá là 0,08 m³.", True),
                ("b", "Khối lượng riêng của loại đá này là 2 600 kg/m³.", True),
                ("c", "Khối đá này nặng hơn một khối sắt có cùng thể tích (D_sắt = 7 800 kg/m³).", False),
                ("d", "Nếu lấy 1 m³ loại đá trên thì khối lượng của nó là 2,6 tấn.", True)
            ], "V = 0,8 × 0,5 × 0,2 = 0,08 m³. D = 208 / 0,08 = 2 600 kg/m³ = 2,6 tấn/m³ < D_sắt."),
            make_tf(4, "Vận dụng", "Một bình thủy tinh chứa đầy 500 mL nước có khối lượng tổng cộng là 650 g. Biết khối lượng riêng của nước là 1 g/cm³:", [
                ("a", "Khối lượng của lượng nước trong bình là 500 g.", True),
                ("b", "Khối lượng của vỏ bình thủy tinh rỗng là 150 g.", True),
                ("c", "Nếu thay nước bằng 500 mL rượu có khối lượng riêng 0,8 g/cm³ thì khối lượng rượu là 400 g.", True),
                ("d", "Khi đựng đầy rượu thì tổng khối lượng cả bình và rượu là 600 g.", False)
            ], "Tổng khối lượng khi đựng rượu = 150 g + 400 g = 550 g.")
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Khối lượng riêng của vàng nguyên chất là bao nhiêu g/cm³ nếu 1 m³ vàng nặng 19 300 kg?", "19.3", "19 300 kg/m³ = 19,3 g/cm³."),
            make_sa(2, "Thông hiểu", "Một can chứa 10 lít nước tinh khiết (D = 1 000 kg/m³). Khối lượng của nước trong can là bao nhiêu kilôgam?", "10", "10 lít = 0,01 m³; m = 1 000 × 0,01 = 10 kg."),
            make_sa(3, "Vận dụng", "Một thỏi kim loại có khối lượng 540 g và thể tích 200 cm³. Khối lượng riêng của thỏi kim loại theo đơn vị kg/m³ là bao nhiêu?", "2700", "D = 540 / 200 = 2,7 g/cm³ = 2 700 kg/m³ (Nhôm)."),
            make_sa(4, "Vận dụng", "Cần bao nhiêu mét khối cát xây dựng có khối lượng riêng 1 500 kg/m³ để có khối lượng tổng cộng là 4,5 tấn?", "3", "4,5 tấn = 4 500 kg; V = 4 500 / 1 500 = 3 m³."),
            make_sa(5, "Vận dụng cao", "Một bể nước ngầm dạng hình hộp chữ nhật có kích thước đáy 2 m × 1,5 m và chiều cao 1,2 m. Khi bể chứa đầy nước thì khối lượng nước trong bể là bao nhiêu tấn?", "3.6", "V = 2 × 1,5 × 1,2 = 3,6 m³. m = 3,6 × 1 000 = 3 600 kg = 3,6 tấn."),
            make_sa(6, "Vận dụng cao", "Một chiếc vòng đeo tay bằng hợp kim vàng và đồng có khối lượng 146,8 g và thể tích 10 cm³. Biết D_vàng = 19,3 g/cm³, D_đồng = 8,9 g/cm³. Khối lượng vàng có trong chiếc vòng là bao nhiêu gam? (Làm tròn đến 1 chữ số thập phân)", "107.5", "m1 + m2 = 146,8; m1/19,3 + m2/8,9 = 10 => m1 ≈ 107,5 g.")
        ],
        "part4": [
            make_vdc(1, "Một bức tượng cổ bằng kim loại đồng chất có khối lượng 8,9 kg. Khi nhúng chìm hoàn toàn bức tượng vào một bình tràn chứa đầy nước thì lượng nước tràn ra có thể tích đúng bằng 1 lít. Khối lượng riêng của kim loại làm bức tượng là:", ["8 900 kg/m³ (Đồng nguyên chất)", "7 800 kg/m³ (Sắt)", "2 700 kg/m³ (Nhôm)", "11 300 kg/m³ (Chì)"], 0, "V = 1 L = 0,001 m³. D = 8,9 / 0,001 = 8 900 kg/m³ => Đồng."),
            make_vdc(2, "Để pha dung dịch nước muối sinh lí có nồng độ muối khoảng 0,9%, người ta hòa tan 9 g muối ăn tinh khiết vào 991 g nước cất để thu được 1 000 g dung dịch có thể tích 995 mL. Khối lượng riêng của dung dịch nước muối sinh lí này xấp xỉ bằng:", ["1 005 kg/m³", "1 000 kg/m³", "995 kg/m³", "1 050 kg/m³"], 0, "D = 1 000 g / 995 cm³ ≈ 1,005 g/cm³ = 1 005 kg/m³."),
            make_vdc(3, "Một khối bê tông rỗng dùng trong xây dựng kè chắn sóng có thể tích ngoài là 1,5 m³, bên trong có khoang rỗng thể tích 0,3 m³. Biết khối lượng riêng của bê tông là 2 400 kg/m³. Khối lượng của khối bê tông kè chắn sóng này là:", ["2 880 kg", "3 600 kg", "720 kg", "4 320 kg"], 0, "V_thực = 1,5 - 0,3 = 1,2 m³. m = 2 400 × 1,2 = 2 880 kg."),
            make_vdc(4, "Một bình cầu chứa đầy không khí ở điều kiện tiêu chuẩn có thể tích 2 lít. Đem cân thấy khối lượng cả bình và không khí nặng 152,58 g. Dùng bơm hút hết không khí trong bình ra rồi cân lại thì thấy nặng 150 g. Khối lượng riêng của không khí ở điều kiện trên là:", ["1,29 kg/m³", "1,15 kg/m³", "1,42 kg/m³", "0,85 kg/m³"], 0, "m_kk = 152,58 - 150 = 2,58 g. V = 2 L = 2 000 cm³. D = 2,58 / 2 000 = 0,00129 g/cm³ = 1,29 kg/m³.")
        ]
    }

    # --- TEST 2 ---
    exams["phys8_c3_b13_test2"] = {
        "title": "Đề kiểm tra KHTN 8 (Vật lý) - Bài 13: Khối lượng riêng - Đề số 02",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title,
        "lessonId": "phys8_c3_b13", "lessonName": "Bài 13: Khối lượng riêng",
        "testNum": 2, "duration": "45 phút", "points": 10.0,
        "part1": [
            make_mc(1, "Nhận biết", "Đại lượng nào sau đây cho biết mức độ đặc hay xốp của các hạt vật chất cấu tạo nên vật?", ["Khối lượng riêng", "Trọng lượng", "Thể tích", "Diện tích tiếp xúc"], 0, "Khối lượng riêng phản ánh mức độ tập trung khối lượng trong một đơn vị thể tích."),
            make_mc(2, "Nhận biết", "Kí hiệu thông dụng của khối lượng riêng là:", ["D (hoặc ρ)", "m", "V", "P"], 0, "Khối lượng riêng kí hiệu là D hoặc chữ Hy Lạp ρ (rho)."),
            make_mc(3, "Nhận biết", "Từ công thức D = m/V, công thức suy ra dùng để tính thể tích V là:", ["V = m / D", "V = m × D", "V = D / m", "V = m + D"], 0, "V = m / D."),
            make_mc(4, "Nhận biết", "Trong các chất sau đây, chất nào có khối lượng riêng lớn nhất ở điều kiện thường?", ["Chì", "Sắt", "Nhôm", "Nước"], 0, "D_chì (11 300) > D_sắt (7 800) > D_nhôm (2 700) > D_nước (1 000 kg/m³)."),
            make_mc(5, "Nhận biết", "Trọng lượng riêng d liên hệ với khối lượng riêng D theo công thức (lấy g ≈ 10 m/s²):", ["d = 10 × D", "d = D / 10", "d = 10 / D", "d = D + 10"], 0, "d = P/V = 10m/V = 10D."),
            make_mc(6, "Nhận biết", "Đơn vị nào dưới đây KHÔNG phải là đơn vị của khối lượng riêng?", ["N/m³", "kg/m³", "g/cm³", "g/mL"], 0, "N/m³ là đơn vị của trọng lượng riêng, không phải khối lượng riêng."),
            make_mc(7, "Thông hiểu", "Một bình chứa 500 cm³ thủy ngân nguyên chất có khối lượng riêng 13 600 kg/m³. Khối lượng của lượng thủy ngân đó là:", ["6,8 kg", "13,6 kg", "68 kg", "0,68 kg"], 0, "V = 500 cm³ = 0,0005 m³. m = 13 600 × 0,0005 = 6,8 kg."),
            make_mc(8, "Thông hiểu", "Một khối gỗ hình lập phương có cạnh 10 cm, khối lượng 700 g. Khối lượng riêng của khối gỗ là:", ["700 kg/m³", "800 kg/m³", "900 kg/m³", "0,7 kg/m³"], 0, "V = 10³ = 1000 cm³; D = 700/1000 = 0,7 g/cm³ = 700 kg/m³."),
            make_mc(9, "Thông hiểu", "Có 3 khối kim loại đồng chất: nhôm, sắt, chì có cùng thể tích 1 dm³. Khối nào có khối lượng lớn nhất?", ["Khối chì", "Khối sắt", "Khối nhôm", "Cả 3 khối bằng nhau"], 0, "Cùng V thì m tỉ lệ thuận với D. Chì có D lớn nhất (11 300 kg/m³)."),
            make_mc(10, "Thông hiểu", "Một chiếc xe bồn chở 12 m³ xăng. Biết khối lượng riêng của xăng là 700 kg/m³. Khối lượng xăng trên xe là:", ["8 400 kg", "7 000 kg", "12 000 kg", "1 714 kg"], 0, "m = D × V = 700 × 12 = 8 400 kg."),
            make_mc(11, "Thông hiểu", "Tại sao nước đá (băng) lại nổi trên mặt nước lỏng?", ["Vì khối lượng riêng của nước đá nhỏ hơn khối lượng riêng của nước lỏng", "Vì nước đá lạnh hơn", "Vì nước đá có nhiều bọt khí", "Vì nước đá có hình dạng góc cạnh"], 0, "D_nước đá (≈ 900 - 920 kg/m³) nhỏ hơn D_nước lỏng (1 000 kg/m³)."),
            make_mc(12, "Thông hiểu", "Từ công thức D = m/V, nếu khối lượng m tăng gấp 3 lần và thể tích V tăng gấp 3 lần thì khối lượng riêng D:", ["Không thay đổi", "Tăng 9 lần", "Tăng 3 lần", "Giảm 3 lần"], 0, "D' = (3m)/(3V) = m/V = D không đổi.")
        ],
        "part2": [
            make_tf(1, "Thông hiểu", "Xét các khẳng định về khối lượng riêng của một số chất lỏng thông dụng ở 20 °C:", [
                ("a", "Dầu ăn nhẹ hơn nước nên nổi lên trên mặt nước khi trộn lẫn.", True),
                ("b", "Cồn y tế 70 độ có khối lượng riêng nhỏ hơn nước cất.", True),
                ("c", "Thủy ngân là kim loại thể lỏng có khối lượng riêng nhỏ hơn nước.", False),
                ("d", "Khối lượng riêng của nước biển lớn hơn khối lượng riêng của nước ngọt do có chứa muối.", True)
            ], "Thủy ngân rất nặng, D ≈ 13 600 kg/m³ gấp 13,6 lần nước."),
            make_tf(2, "Thông hiểu", "Một học sinh so sánh giữa khối lượng và khối lượng riêng:", [
                ("a", "Khối lượng thay đổi tùy thuộc vào lượng chất cấu tạo nên vật.", True),
                ("b", "Khối lượng riêng phụ thuộc vào bản chất của chất cấu tạo nên vật.", True),
                ("c", "Một thanh sắt dài 1 m có khối lượng riêng lớn hơn một chiếc đinh sắt nhỏ.", False),
                ("d", "Khối lượng riêng của một chất phụ thuộc vào nhiệt độ của chất đó.", True)
            ], "Hai vật cùng làm bằng sắt thì có cùng khối lượng riêng."),
            make_tf(3, "Vận dụng", "Một khối kim loại đồng chất có khối lượng 1,89 kg và thể tích 0,0007 m³:", [
                ("a", "Thể tích của khối kim loại là 700 cm³.", True),
                ("b", "Khối lượng riêng của kim loại này là 2 700 kg/m³.", True),
                ("c", "Kim loại cấu tạo nên khối này nhiều khả năng là nhôm.", True),
                ("d", "Nếu nung chảy kim loại này rồi đúc thành một vật có thể tích 1 m³ thì vật sẽ nặng 1 890 kg.", False)
            ], "1 m³ nhôm có khối lượng là 2 700 kg."),
            make_tf(4, "Vận dụng", "Một bình rỗng nặng 200 g. Khi đổ đầy nước vào bình thì khối lượng tổng cộng là 1 200 g. Biết D_nước = 1 g/cm³:", [
                ("a", "Dung tích của bình là 1 000 cm³ (tức 1 lít).", True),
                ("b", "Khối lượng của nước trong bình là 1 000 g.", True),
                ("c", "Nếu đổ đầy dầu có khối lượng riêng 0,8 g/cm³ vào bình thì dầu nặng 800 g.", True),
                ("d", "Tổng khối lượng bình khi đổ đầy dầu là 900 g.", False)
            ], "Tổng khối lượng khi đổ đầy dầu = 200 g + 800 g = 1 000 g.")
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Khối lượng riêng của bạc là 10 500 kg/m³. Đổi sang đơn vị g/cm³ ta được giá trị là bao nhiêu?", "10.5", "10 500 kg/m³ = 10,5 g/cm³."),
            make_sa(2, "Thông hiểu", "Tính thể tích của 5,4 kg nhôm nguyên chất biết khối lượng riêng của nhôm là 2 700 kg/m³. Kết quả là bao nhiêu dm³?", "2", "V = 5,4 / 2 700 = 0,002 m³ = 2 dm³."),
            make_sa(3, "Vận dụng", "Một cột bê tông hình trụ có diện tích đáy 0,2 m² và chiều cao 3 m. Biết D_bê tông = 2 500 kg/m³. Khối lượng của cột bê tông là bao nhiêu tấn?", "1.5", "V = 0,2 × 3 = 0,6 m³; m = 2 500 × 0,6 = 1 500 kg = 1,5 tấn."),
            make_sa(4, "Vận dụng", "Một khối đồng nặng 890 g có thể tích 100 cm³. Trọng lượng riêng của đồng là bao nhiêu N/m³?", "89000", "D = 890/100 = 8,9 g/cm³ = 8 900 kg/m³ => d = 10D = 89 000 N/m³."),
            make_sa(5, "Vận dụng cao", "Một chiếc can rỗng nặng 0,5 kg. Khi đổ đầy 5 lít dầu hỏa thì can nặng 4,5 kg. Khối lượng riêng của dầu hỏa là bao nhiêu kg/m³?", "800", "m_dầu = 4,5 - 0,5 = 4 kg. V = 5 L = 0,005 m³. D = 4 / 0,005 = 800 kg/m³."),
            make_sa(6, "Vận dụng cao", "Một mẫu hợp kim gồm 60% thiếc và 40% chì theo khối lượng. Biết D_thiếc = 7 300 kg/m³, D_chì = 11 300 kg/m³. Bỏ qua sự thay đổi thể tích khi pha trộn, khối lượng riêng của hợp kim xấp xỉ bằng bao nhiêu kg/m³? (Làm tròn đến hàng đơn vị)", "8502", "1/D = 0,6/7300 + 0,4/11300 => D ≈ 8 502 kg/m³.")
        ],
        "part4": [
            make_vdc(1, "Một người thợ kim hoàn muốn kiểm tra chiếc vương miện nghi làm bằng vàng pha bạc. Chiếc vương miện nặng 386 g. Khi thả chìm hoàn toàn vào bình tràn chứa nước thì thể tích nước dâng lên tràn ra là 25 cm³. Biết D_vàng = 19,3 g/cm³, D_bạc = 10,5 g/cm³. Khối lượng riêng thực tế của vương miện là:", ["15,44 g/cm³ (chứng tỏ vương miện đã bị pha tạp chất)", "19,30 g/cm³ (vàng ròng nguyên chất)", "10,50 g/cm³ (hoàn toàn là bạc)", "13,60 g/cm³ (bằng thủy ngân)"], 0, "D = 386 / 25 = 15,44 g/cm³ < 19,3 g/cm³ nên vương miện không phải vàng ròng."),
            make_vdc(2, "Để xây một bức tường gạch dài 5 m, cao 2 m và dày 0,2 m, người thợ xây dùng gạch đặc có khối lượng riêng 1 800 kg/m³ và vữa xi măng có khối lượng riêng 2 000 kg/m³. Biết vữa chiếm 20% thể tích toàn bộ bức tường, còn lại là gạch. Khối lượng tổng cộng của bức tường (chưa kể trát ngoài) là:", ["3 680 kg", "4 000 kg", "3 600 kg", "4 250 kg"], 0, "V = 5 × 2 × 0,2 = 2 m³. V_vữa = 0,4 m³ (m = 800 kg). V_gạch = 1,6 m³ (m = 2 880 kg). m_tổng = 3 680 kg."),
            make_vdc(3, "Một bể kính nuôi cá cảnh dạng hình hộp chữ nhật dài 80 cm, rộng 50 cm. Mực nước trong bể cao 40 cm. Người ta thả vào bể một khối đá nặng 26 kg có khối lượng riêng 2 600 kg/m³. Giả sử khối đá chìm hoàn toàn và nước không tràn ra ngoài, mực nước trong bể dâng thêm một đoạn là:", ["2,5 cm", "1,5 cm", "3,0 cm", "2,0 cm"], 0, "V_đá = 26 / 2 600 = 0,01 m³ = 10 000 cm³. S_đáy = 80 × 50 = 4 000 cm². Độ dâng h = 10 000 / 4 000 = 2,5 cm."),
            make_vdc(4, "Một bình thủy tinh chứa 1 lít nước ở 4 °C. Khi đun nóng nước đến 90 °C thì thể tích của nước tăng thêm khoảng 3,6%. Biết khối lượng riêng của nước ở 4 °C là 1 000 kg/m³. Khối lượng riêng của nước ở 90 °C xấp xỉ bằng:", ["965 kg/m³", "980 kg/m³", "950 kg/m³", "1 036 kg/m³"], 0, "V' = 1,036 V. D' = m / (1,036 V) = 1 000 / 1,036 ≈ 965,25 kg/m³.")
        ]
    }

    # --- TEST 3 ---
    exams["phys8_c3_b13_test3"] = {
        "title": "Đề kiểm tra KHTN 8 (Vật lý) - Bài 13: Khối lượng riêng - Đề số 03",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title,
        "lessonId": "phys8_c3_b13", "lessonName": "Bài 13: Khối lượng riêng",
        "testNum": 3, "duration": "45 phút", "points": 10.0,
        "part1": [
            make_mc(1, "Nhận biết", "Muốn tính khối lượng m của một vật thể từ thể tích V và khối lượng riêng D, ta dùng công thức:", ["m = D × V", "m = D / V", "m = V / D", "m = D + V"], 0, "m = D × V."),
            make_mc(2, "Nhận biết", "Phát biểu nào sau đây đúng về khối lượng riêng của một chất?", ["Là một đặc trưng vật lí của chất đó ở một nhiệt độ và áp suất xác định", "Thay đổi khi hình dạng vật thể thay đổi", "Tỉ lệ thuận với thể tích của vật", "Có giá trị như nhau đối với mọi chất"], 0, "Mỗi chất có một khối lượng riêng đặc trưng ở điều kiện xác định."),
            make_mc(3, "Nhận biết", "Để đổi từ đơn vị kg/m³ sang g/cm³, ta phải làm phép tính:", ["Chia giá trị đó cho 1 000", "Nhân giá trị đó với 1 000", "Chia giá trị đó cho 100", "Nhân giá trị đó với 100"], 0, "1 000 kg/m³ = 1 g/cm³ nên cần chia cho 1 000."),
            make_mc(4, "Nhận biết", "Trọng lượng P của một vật có thể tích V và khối lượng riêng D được tính theo biểu thức:", ["P = 10 × D × V", "P = D × V / 10", "P = 10 × D / V", "P = D / (10 × V)"], 0, "P = 10m = 10 × D × V."),
            make_mc(5, "Nhận biết", "Chất nào sau đây thường có khối lượng riêng nhỏ nhất trong cùng điều kiện nhiệt độ và áp suất?", ["Chất khí", "Chất lỏng", "Chất rắn", "Kim loại"], 0, "Các phân tử chất khí ở rất xa nhau nên khối lượng riêng của chất khí nhỏ hơn nhiều so với chất lỏng và rắn."),
            make_mc(6, "Nhận biết", "Số liệu 7 800 kg/m³ cho biết điều gì về sắt?", ["Một mét khối sắt có khối lượng là 7 800 kg", "Một kilôgam sắt có thể tích 7 800 m³", "Trọng lượng của một mét khối sắt là 7 800 N", "Khối sắt bất kì luôn nặng 7 800 kg"], 0, "Ý nghĩa khối lượng riêng của sắt."),
            make_mc(7, "Thông hiểu", "Một quả cầu bằng đồng có thể tích 40 cm³, khối lượng riêng của đồng là 8,9 g/cm³. Khối lượng của quả cầu là:", ["356 g", "35,6 g", "400 g", "222,5 g"], 0, "m = D × V = 8,9 × 40 = 356 g."),
            make_mc(8, "Thông hiểu", "Một bình chứa đầy 60 lít nước tinh khiết (D = 1 000 kg/m³). Khối lượng nước trong bình bằng:", ["60 kg", "6 kg", "600 kg", "0,06 tấn"], 0, "60 L = 0,06 m³; m = 1 000 × 0,06 = 60 kg."),
            make_mc(9, "Thông hiểu", "Hai vật A và B có cùng khối lượng. Biết thể tích của vật A gấp 2 lần thể tích vật B. Khối lượng riêng của vật A so với vật B là:", ["Bằng một nửa vật B", "Gấp đôi vật B", "Bằng vật B", "Gấp 4 lần vật B"], 0, "D = m/V, V_A = 2V_B nên D_A = D_B / 2."),
            make_mc(10, "Thông hiểu", "Một tấm tôn hình chữ nhật có kích thước 2 m × 1 m và dày 1 mm. Biết khối lượng riêng của tôn là 7 800 kg/m³. Khối lượng của tấm tôn là:", ["15,6 kg", "156 kg", "1,56 kg", "31,2 kg"], 0, "V = 2 × 1 × 0,001 = 0,002 m³. m = 7 800 × 0,002 = 15,6 kg."),
            make_mc(11, "Thông hiểu", "Vì sao khi xảy ra cháy do dầu mỡ, người ta tuyệt đối không được dùng nước để dập lửa?", ["Vì dầu mỡ nhẹ hơn nước (khối lượng riêng nhỏ hơn) nên nổi lên trên mặt nước và tiếp tục cháy lan rộng", "Vì nước kết hợp với dầu tạo chất nổ", "Vì nước làm dầu mỡ nóng hơn", "Vì nước dẫn điện"], 0, "D_dầu < D_nước nên dầu nổi trên nước làm đám cháy lan rộng."),
            make_mc(12, "Thông hiểu", "Một khối kim loại có thể tích 100 cm³ và khối lượng 1,13 kg. Kim loại này là:", ["Chì (D = 11 300 kg/m³)", "Sắt (D = 7 800 kg/m³)", "Đồng (D = 8 900 kg/m³)", "Nhôm (D = 2 700 kg/m³)"], 0, "D = 1 130 g / 100 cm³ = 11,3 g/cm³ = 11 300 kg/m³ (Chì).")
        ],
        "part2": [
            make_tf(1, "Thông hiểu", "Xét ý nghĩa thực tiễn của việc xác định khối lượng riêng của các vật liệu:", [
                ("a", "Giúp tính toán khối lượng công trình trước khi thi công để thiết kế móng vững chắc.", True),
                ("b", "Giúp phát hiện gian lận vàng pha tạp chất trong ngành hoàn kim.", True),
                ("c", "Giúp lựa chọn vật liệu nhẹ có độ bền cao như hợp kim nhôm, sợi carbon trong chế tạo máy bay.", True),
                ("d", "Khối lượng riêng của vật liệu càng lớn thì vật liệu đó càng dễ bị ăn mòn hóa học.", False)
            ], "Khối lượng riêng là thuộc tính cơ học, không quy định tính ăn mòn hóa học."),
            make_tf(2, "Thông hiểu", "Cho biết khối lượng riêng của không khí ở 0 °C là 1,29 kg/m³ và ở 100 °C là khoảng 0,95 kg/m³:", [
                ("a", "Khi nhiệt độ không khí tăng thì không khí nở ra làm thể tích tăng.", True),
                ("b", "Không khí nóng có khối lượng riêng nhỏ hơn không khí lạnh.", True),
                ("c", "Không khí nóng nhẹ hơn nên luôn có xu hướng bốc lên cao.", True),
                ("d", "Khinh khí cầu bay lên được là do không khí bên trong khinh khí cầu được làm lạnh.", False)
            ], "Khinh khí cầu bay lên do đốt nóng không khí bên trong làm giảm khối lượng riêng."),
            make_tf(3, "Vận dụng", "Một khối đá hoa cương đồng chất có thể tích 0,25 m³ và có khối lượng 687,5 kg:", [
                ("a", "Khối lượng riêng của đá hoa cương này là 2 750 kg/m³.", True),
                ("b", "Đổi sang đơn vị g/cm³ thì khối lượng riêng của nó là 2,75 g/cm³.", True),
                ("c", "Một khối nhôm có cùng thể tích sẽ nặng hơn khối đá hoa cương này (D_nhôm = 2 700 kg/m³).", False),
                ("d", "Trọng lượng của khối đá hoa cương là 6 875 N.", True)
            ], "D_đá = 687,5 / 0,25 = 2 750 kg/m³ > D_nhôm nên khối đá nặng hơn khối nhôm cùng thể tích."),
            make_tf(4, "Vận dụng", "Một người pha 200 mL nước ngọt có khối lượng 216 g với 300 mL nước khoáng có khối lượng 300 g:", [
                ("a", "Khối lượng riêng của nước ngọt ban đầu là 1,08 g/cm³.", True),
                ("b", "Khối lượng riêng của nước khoáng ban đầu là 1,00 g/cm³.", True),
                ("c", "Tổng thể tích dung dịch sau khi pha trộn (coi như không co ngót) là 500 mL.", True),
                ("d", "Khối lượng riêng của hỗn hợp sau khi pha là 1,04 g/cm³.", False)
            ], "D_hh = (216 + 300) / 500 = 516 / 500 = 1,032 g/cm³.")
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Khối lượng riêng của dầu hỏa là 800 kg/m³. 2 m³ dầu hỏa có khối lượng là bao nhiêu kilôgam?", "1600", "m = 800 × 2 = 1 600 kg."),
            make_sa(2, "Thông hiểu", "Một quả cầu nhôm có khối lượng 1,35 kg (D = 2 700 kg/m³). Thể tích của quả cầu là bao nhiêu cm³?", "500", "V = 1,35 / 2 700 = 0,0005 m³ = 500 cm³."),
            make_sa(3, "Vận dụng", "Một thanh ray đường sắt bằng thép có chiều dài 12 m và diện tích tiết diện ngang là 50 cm². Biết D_thép = 7 850 kg/m³. Khối lượng thanh ray là bao nhiêu kilôgam?", "471", "V = 12 × 0,0050 = 0,06 m³. m = 7 850 × 0,06 = 471 kg."),
            make_sa(4, "Vận dụng", "Một viên gạch hai lỗ có kích thước ngoài 22 cm × 10 cm × 6 cm. Mỗi lỗ có đường kính đáy tròn với diện tích 10 cm² xuyên suốt chiều cao 6 cm. Thể tích đất sét thực tế của viên gạch là bao nhiêu cm³?", "1200", "V_ngoài = 22 × 10 × 6 = 1 320 cm³. V_2lỗ = 2 × 10 × 6 = 120 cm³. V_thực = 1 200 cm³."),
            make_sa(5, "Vận dụng cao", "Một chiếc phuy hình trụ chứa 200 lít xăng (D = 700 kg/m³). Trọng lượng của lượng xăng trong phuy là bao nhiêu Newton?", "1400", "V = 0,2 m³; m = 700 × 0,2 = 140 kg => P = 10m = 1 400 N."),
            make_sa(6, "Vận dụng cao", "Một quả cầu rỗng bằng sắt có bán kính ngoài và bán kính trong sao cho thể tích phần vỏ sắt là 50 cm³, phần rỗng bên trong là 150 cm³. Khối lượng riêng trung bình của quả cầu rỗng này là bao nhiêu g/cm³? (Biết D_sắt = 7,8 g/cm³)", "1.95", "m = 7,8 × 50 = 390 g. V_toàn = 50 + 150 = 200 cm³. D_tb = 390 / 200 = 1,95 g/cm³.")
        ],
        "part4": [
            make_vdc(1, "Một bức tượng Phật đúc bằng đồng có khối lượng 178 kg. Để kiểm tra tượng có bị rỗng bên trong hay không, người ta đo thể tích của tượng bằng cách thả vào một bể nước lớn thấy nước dâng lên 0,024 m³. Biết khối lượng riêng của đồng nguyên chất là 8 900 kg/m³. Thể tích khoang rỗng bên trong bức tượng là:", ["0,004 m³ (4 lít)", "0,002 m³ (2 lít)", "0,020 m³ (20 lít)", "Hoàn toàn đặc, không có phần rỗng"], 0, "V_đồng thực = 178 / 8 900 = 0,020 m³. V_rỗng = 0,024 - 0,020 = 0,004 m³ = 4 lít."),
            make_vdc(2, "Một xe tải chở 15 m³ cát ẩm có độ ẩm 10% (nghĩa là khối lượng nước chiếm 10% tổng khối lượng cát ẩm). Biết khối lượng riêng của cát khô là 1 400 kg/m³ và khối lượng riêng của nước là 1 000 kg/m³. Coi thể tích cát ẩm bằng thể tích cát khô. Khối lượng toàn bộ chuyến cát ẩm trên xe tải xấp xỉ bằng:", ["23 333 kg", "21 000 kg", "25 200 kg", "19 500 kg"], 0, "m_cát khô = 1 400 × 15 = 21 000 kg. m_khô = 90% m_tổng => m_tổng = 21 000 / 0,9 ≈ 23 333 kg."),
            make_vdc(3, "Để đúc một chi tiết máy bằng hợp kim gồm 70% nhôm và 30% kẽm theo thể tích. Biết khối lượng riêng của nhôm là 2 700 kg/m³ và của kẽm là 7 100 kg/m³. Khối lượng riêng của hợp kim này (bỏ qua hao hụt thể tích khi nấu chảy) là:", ["4 020 kg/m³", "4 900 kg/m³", "3 580 kg/m³", "5 100 kg/m³"], 0, "D = 0,7 × 2 700 + 0,3 × 7 100 = 1 890 + 2 130 = 4 020 kg/m³."),
            make_vdc(4, "Một thùng sắt hình lập phương có cạnh ngoài 40 cm, thành thùng dày 1 cm, không có nắp đậy. Biết khối lượng riêng của sắt là 7 800 kg/m³. Khối lượng của chiếc thùng sắt này xấp xỉ bằng:", ["60,9 kg", "75,2 kg", "48,5 kg", "92,1 kg"], 0, "V_ngoài = 40 × 40 × 40 = 64 000 cm³. Kích thước trong: đáy dày 1cm nên sâu 39cm, rộng 38cm, dài 38cm. V_trong = 38 × 38 × 39 = 56 316 cm³. V_sắt = 64 000 - 56 316 = 7 684 cm³ = 0,007684 m³. m = 7 800 × 0,007684 ≈ 59,9 - 60,9 kg.")
        ]
    }

    return exams
