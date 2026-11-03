# -*- coding: utf-8 -*-
"""
CHƯƠNG III: KHỐI LƯỢNG RIÊNG VÀ ÁP SUẤT
Tạo 20 đề thi chuẩn mực, 100% độc lập, không trùng lặp trong từng bài học:
- phys8_c3_b13: 3 đề
- phys8_c3_b14: 3 đề
- phys8_c3_b15: 3 đề
- phys8_c3_b16: 3 đề
- phys8_c3_b17: 3 đề
- phys8_c3_rev: 5 đề
"""

import sys, json
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid, "level": level, "question": q_text,
        "options": options, "correct": correct_idx, "explanation": explanation
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid, "level": level, "question": prompt,
        "statements": [{"subId": s[0], "text": s[1], "correct": s[2]} for s in statements],
        "explanation": explanation
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid, "level": level, "question": q_text,
        "correctAnswer": str(answer).strip(), "explanation": explanation
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid, "level": "Vận dụng cao", "question": q_text,
        "options": options, "correct": correct_idx, "explanation": explanation
    }

def get_c3_exams():
    exams = {}
    ch_id = "phys8_c3"
    ch_title = "Chương III: Khối lượng riêng và áp suất"

    def exam_meta(l_id, l_name, t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # =========================================================================
    # BÀI 13: KHỐI LƯỢNG RIÊNG (3 ĐỀ)
    # =========================================================================
    l13_id = "phys8_c3_b13"
    l13_name = "Bài 13: Khối lượng riêng"

    # --- ĐỀ 1 ---
    p1 = [
        make_mc(1, "Nhận biết", "Khối lượng riêng của một chất là khối lượng của:", ["Một đơn vị thể tích chất đó", "Toàn bộ vật thể làm bằng chất đó", "Một phân tử chất đó", "Một centimet khối chất lỏng bất kì"], 0, "D = m/V là khối lượng của một đơn vị thể tích."),
        make_mc(2, "Nhận biết", "Công thức xác định khối lượng riêng D theo khối lượng m và thể tích V là:", ["D = m / V", "D = m × V", "D = V / m", "D = m + V"], 0, "D = m / V."),
        make_mc(3, "Nhận biết", "Đơn vị chuẩn của khối lượng riêng trong hệ đo lường quốc tế SI là:", ["kg/m³", "g/cm³", "kg/L", "N/m³"], 0, "kg/m³ là đơn vị chuẩn SI."),
        make_mc(4, "Nhận biết", "Mối liên hệ giữa 1 g/cm³ và kg/m³ là:", ["1 g/cm³ = 1 000 kg/m³", "1 g/cm³ = 100 kg/m³", "1 g/cm³ = 10 kg/m³", "1 g/cm³ = 0,001 kg/m³"], 0, "1 g/cm³ = 1000 kg/m³."),
        make_mc(5, "Nhận biết", "Khối lượng riêng của nước nguyên chất ở 4 °C xấp xỉ bằng:", ["1 000 kg/m³", "800 kg/m³", "1 200 kg/m³", "100 kg/m³"], 0, "Ở 4 °C D_nước = 1000 kg/m³."),
        make_mc(6, "Nhận biết", "Để xác định khối lượng riêng của một chất ta cần đo:", ["Khối lượng và thể tích của vật", "Trọng lượng và độ cao của vật", "Áp suất và nhiệt độ của vật", "Thể tích và diện tích bề mặt"], 0, "Cần đo m và V."),
        make_mc(7, "Thông hiểu", "Một khối sắt có thể tích 0,5 m³ và D = 7 800 kg/m³. Khối lượng của khối sắt là:", ["3 900 kg", "7 800 kg", "15 600 kg", "1 560 kg"], 0, "m = D.V = 7800 × 0,5 = 3900 kg."),
        make_mc(8, "Thông hiểu", "Một bình chứa 2 lít dầu ăn nặng 1,6 kg. Khối lượng riêng của dầu ăn là:", ["800 kg/m³", "850 kg/m³", "900 kg/m³", "1 600 kg/m³"], 0, "D = 1,6 / 0,002 = 800 kg/m³."),
        make_mc(9, "Thông hiểu", "Cưa một thanh gỗ đồng chất thành 2 nửa bằng nhau thì khối lượng riêng mỗi nửa:", ["Không đổi", "Tăng gấp đôi", "Giảm đi một nửa", "Giảm 4 lần"], 0, "Khối lượng riêng là đặc tính của chất, không đổi."),
        make_mc(10, "Thông hiểu", "Cho D_nhôm = 2 700 kg/m³, D_sắt = 7 800 kg/m³. So sánh thể tích của hai khối nhôm và sắt cùng khối lượng:", ["Thể tích khối nhôm lớn hơn thể tích khối sắt", "Thể tích khối sắt lớn hơn", "Hai khối có thể tích bằng nhau", "Khối nhôm có thể tích bằng một nửa khối sắt"], 0, "V = m/D. D_nhôm < D_sắt nên V_nhôm > V_sắt."),
        make_mc(11, "Thông hiểu", "Một can chứa 5 lít cồn có D = 800 kg/m³. Khối lượng cồn trong can là:", ["4 kg", "4,5 kg", "5 kg", "6,25 kg"], 0, "m = 800 × 0,005 = 4 kg."),
        make_mc(12, "Thông hiểu", "Khi đun nóng nước từ 20 °C lên 80 °C thì:", ["Khối lượng không đổi nhưng khối lượng riêng giảm", "Cả khối lượng và khối lượng riêng đều tăng", "Khối lượng tăng, khối lượng riêng giảm", "Khối lượng riêng không đổi"], 0, "Nước nở ra nên V tăng, m không đổi => D = m/V giảm.")
    ]
    p2 = [
        make_tf(1, "Thông hiểu", "Cho biết khối lượng riêng của nước là 1 000 kg/m³ và của chì là 11 300 kg/m³:", [
            ("a", "Một mét khối nước có khối lượng là 1 000 kg.", True),
            ("b", "Chì có khối lượng riêng lớn gấp 11,3 lần nước.", True),
            ("c", "Nếu lấy cùng thể tích 1 lít thì chì nhẹ hơn nước.", False),
            ("d", "Khối lượng riêng của chì là 11,3 g/cm³.", True)
        ], "11 300 kg/m³ = 11,3 g/cm³; chì nặng hơn nước cùng thể tích."),
        make_tf(2, "Thông hiểu", "Xét các tính chất của khối lượng riêng:", [
            ("a", "Khối lượng riêng là khối lượng của một đơn vị thể tích chất đó.", True),
            ("b", "Khi cắt khối đồng thành 4 phần thì khối lượng riêng mỗi phần giảm 4 lần.", False),
            ("c", "Hai vật cùng làm bằng một chất thì có cùng khối lượng riêng.", True),
            ("d", "Khối lượng riêng phụ thuộc vào nhiệt độ của chất.", True)
        ], "Khối lượng riêng không đổi khi chia nhỏ vật."),
        make_tf(3, "Vận dụng", "Một khối đá hình hộp chữ nhật kích thước 0,8 m × 0,5 m × 0,2 m nặng 208 kg:", [
            ("a", "Thể tích của khối đá là 0,08 m³.", True),
            ("b", "Khối lượng riêng của khối đá là 2 600 kg/m³.", True),
            ("c", "Khối đá này nặng hơn một khối sắt có cùng thể tích (D_sắt = 7 800 kg/m³).", False),
            ("d", "1 m³ loại đá trên nặng 2,6 tấn.", True)
        ], "V = 0,08 m³; D = 2600 kg/m³ = 2,6 tấn/m³ < D_sắt."),
        make_tf(4, "Vận dụng", "Bình thủy tinh đựng đầy 500 mL nước nặng tổng cộng 650 g. Biết D_nước = 1 g/cm³:", [
            ("a", "Khối lượng nước trong bình là 500 g.", True),
            ("b", "Khối lượng vỏ bình thủy tinh là 150 g.", True),
            ("c", "Nếu đựng đầy 500 mL rượu (D = 0,8 g/cm³) thì lượng rượu nặng 400 g.", True),
            ("d", "Tổng khối lượng bình và rượu khi đầy là 600 g.", False)
        ], "Tổng khối lượng khi đầy rượu = 150 + 400 = 550 g.")
    ]
    p3 = [
        make_sa(1, "Thông hiểu", "Khối lượng riêng của vàng nguyên chất là bao nhiêu g/cm³ nếu 1 m³ vàng nặng 19 300 kg?", "19.3", "19 300 kg/m³ = 19,3 g/cm³."),
        make_sa(2, "Thông hiểu", "Một can chứa 10 lít nước tinh khiết (D = 1 000 kg/m³). Khối lượng của nước là bao nhiêu kg?", "10", "10 lít = 0,01 m³; m = 1 000 × 0,01 = 10 kg."),
        make_sa(3, "Vận dụng", "Một thỏi kim loại có khối lượng 540 g và thể tích 200 cm³. Khối lượng riêng của thỏi kim loại theo đơn vị kg/m³ là bao nhiêu?", "2700", "D = 540 / 200 = 2,7 g/cm³ = 2 700 kg/m³."),
        make_sa(4, "Vận dụng", "Cần bao nhiêu mét khối cát xây dựng có D = 1 500 kg/m³ để có khối lượng tổng cộng là 4,5 tấn?", "3", "4 500 / 1 500 = 3 m³."),
        make_sa(5, "Vận dụng cao", "Một bể ngầm hình hộp chữ nhật có đáy 2 m × 1,5 m và sâu 1,2 m. Khi bể chứa đầy nước thì khối lượng nước là bao nhiêu tấn?", "3.6", "V = 2 × 1,5 × 1,2 = 3,6 m³ => m = 3,6 tấn."),
        make_sa(6, "Vận dụng cao", "Một chiếc vòng hợp kim vàng và đồng nặng 146,8 g, thể tích 10 cm³. Biết D_vàng = 19,3 g/cm³, D_đồng = 8,9 g/cm³. Khối lượng vàng có trong vòng là bao nhiêu gam? (Làm tròn 1 chữ số thập phân)", "107.5", "m1 + m2 = 146,8; m1/19,3 + m2/8,9 = 10 => m1 ≈ 107,5 g.")
    ]
    p4 = [
        make_vdc(1, "Một bức tượng cổ bằng kim loại đồng chất nặng 8,9 kg. Nhúng chìm hoàn toàn vào bình tràn đầy nước thì lượng nước tràn ra đúng 1 lít. Khối lượng riêng của kim loại làm bức tượng là:", ["8 900 kg/m³ (Đồng nguyên chất)", "7 800 kg/m³ (Sắt)", "2 700 kg/m³ (Nhôm)", "11 300 kg/m³ (Chì)"], 0, "D = 8,9 / 0,001 = 8 900 kg/m³ (Đồng)."),
        make_vdc(2, "Pha dung dịch nước muối sinh lí nồng độ 0,9%: hòa tan 9 g muối vào 991 g nước cất thu được 1 000 g dung dịch có thể tích 995 mL. Khối lượng riêng của dung dịch nước muối xấp xỉ bằng:", ["1 005 kg/m³", "1 000 kg/m³", "995 kg/m³", "1 050 kg/m³"], 0, "D = 1 000 / 0,995 ≈ 1 005 kg/m³."),
        make_vdc(3, "Một khối bê tông kè chắn sóng có thể tích ngoài 1,5 m³, bên trong có khoang rỗng 0,3 m³. Biết D_bê tông = 2 400 kg/m³. Khối lượng khối bê tông là:", ["2 880 kg", "3 600 kg", "720 kg", "4 320 kg"], 0, "V_thực = 1,5 - 0,3 = 1,2 m³ => m = 2 400 × 1,2 = 2 880 kg."),
        make_vdc(4, "Một bình cầu chứa đầy không khí ở đktc có thể tích 2 lít nặng 152,58 g. Hút hết không khí trong bình ra rồi cân lại thì nặng 150 g. Khối lượng riêng của không khí ở đktc là:", ["1,29 kg/m³", "1,15 kg/m³", "1,42 kg/m³", "0,85 kg/m³"], 0, "m = 2,58 g. V = 2 000 cm³ => D = 2,58 / 2 000 = 0,00129 g/cm³ = 1,29 kg/m³.")
    ]
    exams[f"{l13_id}_test1"] = exam_meta(l13_id, l13_name, 1, p1, p2, p3, p4)

    # --- ĐỀ 2 ---
    p1 = [
        make_mc(1, "Nhận biết", "Đại lượng nào cho biết mức độ tập trung khối lượng trong một đơn vị thể tích của chất?", ["Khối lượng riêng", "Trọng lượng", "Thể tích", "Diện tích tiếp xúc"], 0, "Khối lượng riêng biểu thị mật độ khối lượng."),
        make_mc(2, "Nhận biết", "Kí hiệu thông dụng của khối lượng riêng trong vật lí là:", ["D hoặc ρ", "m", "V", "P"], 0, "Kí hiệu D hoặc ρ."),
        make_mc(3, "Nhận biết", "Công thức tính thể tích V của vật khi biết khối lượng m và khối lượng riêng D là:", ["V = m / D", "V = m × D", "V = D / m", "V = m + D"], 0, "V = m / D."),
        make_mc(4, "Nhận biết", "Chất nào sau đây có khối lượng riêng lớn nhất ở nhiệt độ phòng?", ["Thủy ngân", "Sắt", "Nhôm", "Nước"], 0, "Thủy ngân D ≈ 13 600 kg/m³."),
        make_mc(5, "Nhận biết", "Mối liên hệ giữa trọng lượng riêng d và khối lượng riêng D là (lấy g ≈ 10 m/s²):", ["d = 10 × D", "d = D / 10", "d = 10 / D", "d = D + 10"], 0, "d = 10D."),
        make_mc(6, "Nhận biết", "Đơn vị nào dưới đây KHÔNG phải đơn vị của khối lượng riêng?", ["N/m³", "kg/m³", "g/cm³", "g/mL"], 0, "N/m³ là đơn vị của trọng lượng riêng."),
        make_mc(7, "Thông hiểu", "Một bình chứa 500 cm³ thủy ngân (D = 13 600 kg/m³). Khối lượng thủy ngân đó là:", ["6,8 kg", "13,6 kg", "68 kg", "0,68 kg"], 0, "m = 13 600 × 0,0005 = 6,8 kg."),
        make_mc(8, "Thông hiểu", "Khối gỗ lập phương cạnh 10 cm nặng 700 g. Khối lượng riêng của khối gỗ là:", ["700 kg/m³", "800 kg/m³", "900 kg/m³", "0,7 kg/m³"], 0, "V = 1 000 cm³ => D = 0,7 g/cm³ = 700 kg/m³."),
        make_mc(9, "Thông hiểu", "Ba khối đồng chất nhôm, sắt, chì có cùng thể tích 1 dm³. Khối nào có khối lượng lớn nhất?", ["Khối chì", "Khối sắt", "Khối nhôm", "Cả ba khối bằng nhau"], 0, "Cùng V: Chì có D lớn nhất (11 300 kg/m³)."),
        make_mc(10, "Thông hiểu", "Một xe bồn chở 12 m³ xăng (D = 700 kg/m³). Khối lượng xăng trên xe là:", ["8 400 kg", "7 000 kg", "12 000 kg", "1 714 kg"], 0, "m = 700 × 12 = 8 400 kg."),
        make_mc(11, "Thông hiểu", "Nước đá nổi trên mặt nước lỏng là vì:", ["Khối lượng riêng của nước đá nhỏ hơn của nước lỏng", "Nước đá lạnh hơn", "Nước đá chứa nhiều bọt khí", "Nước đá có góc cạnh"], 0, "D_đá ≈ 900-920 kg/m³ < 1 000 kg/m³."),
        make_mc(12, "Thông hiểu", "Nếu khối lượng m tăng 3 lần và thể tích V tăng 3 lần thì khối lượng riêng D:", ["Không đổi", "Tăng 9 lần", "Tăng 3 lần", "Giảm 3 lần"], 0, "D' = (3m)/(3V) = m/V = D.")
    ]
    p2 = [
        make_tf(1, "Thông hiểu", "Về khối lượng riêng của các chất lỏng thông dụng:", [
            ("a", "Dầu ăn nổi lên trên mặt nước khi trộn lẫn vì nhẹ hơn nước.", True),
            ("b", "Cồn y tế có khối lượng riêng nhỏ hơn nước cất.", True),
            ("c", "Thủy ngân là chất lỏng có khối lượng riêng nhỏ hơn nước.", False),
            ("d", "Nước biển có khối lượng riêng lớn hơn nước ngọt do hòa tan muối.", True)
        ], "Thủy ngân rất nặng D ≈ 13 600 kg/m³ gấp 13,6 lần nước."),
        make_tf(2, "Thông hiểu", "So sánh giữa khối lượng và khối lượng riêng:", [
            ("a", "Khối lượng thay đổi theo lượng chất của vật thể.", True),
            ("b", "Khối lượng riêng là đặc trưng cho bản chất của chất làm nên vật.", True),
            ("c", "Thanh sắt 1 m có khối lượng riêng lớn hơn đinh sắt nhỏ.", False),
            ("d", "Khối lượng riêng của chất phụ thuộc vào nhiệt độ.", True)
        ], "Thanh sắt và đinh sắt cùng chất nên cùng D."),
        make_tf(3, "Vận dụng", "Khối kim loại đồng chất nặng 1,89 kg và có thể tích 0,0007 m³:", [
            ("a", "Thể tích khối kim loại là 700 cm³.", True),
            ("b", "Khối lượng riêng của kim loại là 2 700 kg/m³.", True),
            ("c", "Kim loại này là nhôm.", True),
            ("d", "1 m³ kim loại này nặng 1 890 kg.", False)
        ], "1 m³ nhôm nặng 2 700 kg."),
        make_tf(4, "Vận dụng", "Bình rỗng nặng 200 g. Đổ đầy nước thì nặng 1 200 g (D_nước = 1 g/cm³):", [
            ("a", "Dung tích bình là 1 000 cm³.", True),
            ("b", "Khối lượng nước là 1 000 g.", True),
            ("c", "Đổ đầy dầu (D = 0,8 g/cm³) thì lượng dầu nặng 800 g.", True),
            ("d", "Tổng khối lượng bình khi đầy dầu là 900 g.", False)
        ], "Tổng khối lượng khi đầy dầu = 200 + 800 = 1 000 g.")
    ]
    p3 = [
        make_sa(1, "Thông hiểu", "Khối lượng riêng của bạc là 10 500 kg/m³. Đổi sang đơn vị g/cm³ được bao nhiêu?", "10.5", "10 500 kg/m³ = 10,5 g/cm³."),
        make_sa(2, "Thông hiểu", "Tính thể tích của 5,4 kg nhôm nguyên chất (D = 2 700 kg/m³). Kết quả là bao nhiêu dm³?", "2", "5,4 / 2 700 = 0,002 m³ = 2 dm³."),
        make_sa(3, "Vận dụng", "Cột bê tông hình trụ có đáy 0,2 m², cao 3 m, D = 2 500 kg/m³. Khối lượng cột là bao nhiêu tấn?", "1.5", "m = 2 500 × 0,2 × 3 = 1 500 kg = 1,5 tấn."),
        make_sa(4, "Vận dụng", "Khối đồng nặng 890 g có thể tích 100 cm³. Trọng lượng riêng của đồng là bao nhiêu N/m³?", "89000", "D = 8 900 kg/m³ => d = 10D = 89 000 N/m³."),
        make_sa(5, "Vận dụng cao", "Chiếc can rỗng nặng 0,5 kg. Đổ đầy 5 lít dầu hỏa thì can nặng 4,5 kg. Khối lượng riêng dầu hỏa là bao nhiêu kg/m³?", "800", "m = 4 kg; V = 0,005 m³ => D = 800 kg/m³."),
        make_sa(6, "Vận dụng cao", "Hợp kim gồm 60% thiếc (D = 7 300 kg/m³) và 40% chì (D = 11 300 kg/m³) theo khối lượng. Bỏ qua độ co ngót thể tích, khối lượng riêng hợp kim xấp xỉ bao nhiêu kg/m³? (Làm tròn đến hàng đơn vị)", "8502", "1/D = 0,6/7300 + 0,4/11300 => D ≈ 8 502 kg/m³.")
    ]
    p4 = [
        make_vdc(1, "Chiếc vương miện nặng 386 g. Thả chìm hoàn toàn vào bình tràn đầy nước thấy nước tràn ra 25 cm³. Biết D_vàng = 19,3 g/cm³, D_bạc = 10,5 g/cm³. Khối lượng riêng thực tế của vương miện là:", ["15,44 g/cm³ (chứng tỏ vương miện bị pha tạp chất)", "19,30 g/cm³", "10,50 g/cm³", "13,60 g/cm³"], 0, "D = 386 / 25 = 15,44 g/cm³ < 19,3 g/cm³ => đã bị pha tạp."),
        make_vdc(2, "Xây bức tường gạch dài 5 m, cao 2 m, dày 0,2 m gồm 80% gạch (D = 1 800 kg/m³) và 20% vữa (D = 2 000 kg/m³) theo thể tích. Khối lượng bức tường là:", ["3 680 kg", "4 000 kg", "3 600 kg", "4 250 kg"], 0, "V = 2 m³. m = 1,6 × 1 800 + 0,4 × 2 000 = 3 680 kg."),
        make_vdc(3, "Bể cá cảnh dài 80 cm, rộng 50 cm. Thả khối đá nặng 26 kg (D = 2 600 kg/m³) chìm hoàn toàn vào bể. Mực nước trong bể dâng thêm một đoạn là:", ["2,5 cm", "1,5 cm", "3,0 cm", "2,0 cm"], 0, "V = 26 / 2 600 = 0,01 m³ = 10 000 cm³. h = 10 000 / (80 × 50) = 2,5 cm."),
        make_vdc(4, "Một bình chứa 1 lít nước ở 4 °C (D = 1 000 kg/m³). Đun nóng đến 90 °C thì thể tích nước tăng thêm 3,6%. Khối lượng riêng của nước ở 90 °C xấp xỉ bằng:", ["965 kg/m³", "980 kg/m³", "950 kg/m³", "1 036 kg/m³"], 0, "D' = 1 000 / 1,036 ≈ 965 kg/m³.")
    ]
    exams[f"{l13_id}_test2"] = exam_meta(l13_id, l13_name, 2, p1, p2, p3, p4)

    # --- ĐỀ 3 ---
    p1 = [
        make_mc(1, "Nhận biết", "Muốn tính khối lượng m của vật khi biết thể tích V và khối lượng riêng D, ta dùng công thức:", ["m = D × V", "m = D / V", "m = V / D", "m = D + V"], 0, "m = D × V."),
        make_mc(2, "Nhận biết", "Phát biểu nào sau đây đúng về khối lượng riêng của một chất?", ["Là đặc trưng vật lí của chất ở nhiệt độ và áp suất xác định", "Thay đổi khi hình dạng vật thay đổi", "Tỉ lệ thuận với thể tích vật", "Bằng nhau đối với mọi chất"], 0, "Khối lượng riêng là đặc trưng của chất."),
        make_mc(3, "Nhận biết", "Để đổi từ đơn vị kg/m³ sang g/cm³, ta phải thực hiện phép tính:", ["Chia cho 1 000", "Nhân với 1 000", "Chia cho 100", "Nhân với 100"], 0, "1 g/cm³ = 1 000 kg/m³ nên chia cho 1 000."),
        make_mc(4, "Nhận biết", "Trọng lượng P của vật có thể tích V và khối lượng riêng D là (lấy g ≈ 10 m/s²):", ["P = 10 × D × V", "P = D × V / 10", "P = 10 × D / V", "P = D / (10 × V)"], 0, "P = 10m = 10DV."),
        make_mc(5, "Nhận biết", "Trong cùng điều kiện nhiệt độ và áp suất, chất nào thường có khối lượng riêng nhỏ nhất?", ["Chất khí", "Chất lỏng", "Chất rắn", "Kim loại"], 0, "Chất khí có khoảng cách phân tử lớn nên D rất nhỏ."),
        make_mc(6, "Nhận biết", "Số liệu 7 800 kg/m³ cho biết điều gì về sắt?", ["1 m³ sắt có khối lượng là 7 800 kg", "1 kg sắt có thể tích 7 800 m³", "1 m³ sắt có trọng lượng 7 800 N", "Khối sắt bất kì luôn nặng 7 800 kg"], 0, "Ý nghĩa khối lượng riêng của sắt."),
        make_mc(7, "Thông hiểu", "Một quả cầu đồng có thể tích 40 cm³, D = 8,9 g/cm³. Khối lượng quả cầu là:", ["356 g", "35,6 g", "400 g", "222,5 g"], 0, "m = 8,9 × 40 = 356 g."),
        make_mc(8, "Thông hiểu", "Một bình chứa đầy 60 lít nước tinh khiết (D = 1 000 kg/m³). Khối lượng nước trong bình là:", ["60 kg", "6 kg", "600 kg", "0,06 tấn"], 0, "m = 1 000 × 0,06 = 60 kg."),
        make_mc(9, "Thông hiểu", "Vật A và B cùng khối lượng. Thể tích vật A gấp đôi vật B. Khối lượng riêng vật A so với vật B là:", ["Bằng một nửa vật B", "Gấp đôi vật B", "Bằng vật B", "Gấp 4 lần vật B"], 0, "D_A = m/(2V_B) = D_B / 2."),
        make_mc(10, "Thông hiểu", "Tấm tôn hình chữ nhật 2 m × 1 m, dày 1 mm, D = 7 800 kg/m³. Khối lượng tấm tôn là:", ["15,6 kg", "156 kg", "1,56 kg", "31,2 kg"], 0, "V = 2 × 1 × 0,001 = 0,002 m³ => m = 7 800 × 0,002 = 15,6 kg."),
        make_mc(11, "Thông hiểu", "Khi xảy ra cháy dầu mỡ, không dùng nước dập lửa vì:", ["Dầu mỡ nhẹ hơn nước nên nổi lên trên và tiếp tục cháy lan rộng", "Nước phản ứng nổ với dầu", "Nước làm dầu nóng hơn", "Nước dẫn điện"], 0, "D_dầu < D_nước nên dầu nổi và cháy lan."),
        make_mc(12, "Thông hiểu", "Khối kim loại thể tích 100 cm³ nặng 1,13 kg. Kim loại này là:", ["Chì (11 300 kg/m³)", "Sắt (7 800 kg/m³)", "Đồng (8 900 kg/m³)", "Nhôm (2 700 kg/m³)"], 0, "D = 1 130 / 100 = 11,3 g/cm³ = 11 300 kg/m³ (Chì).")
    ]
    p2 = [
        make_tf(1, "Thông hiểu", "Ý nghĩa thực tiễn của việc xác định khối lượng riêng vật liệu:", [
            ("a", "Giúp tính toán tải trọng công trình để thiết kế móng phù hợp.", True),
            ("b", "Giúp phát hiện gian lận vàng pha tạp chất.", True),
            ("c", "Giúp lựa chọn vật liệu nhẹ, bền như hợp kim nhôm trong chế tạo máy bay.", True),
            ("d", "Khối lượng riêng càng lớn thì vật liệu càng dễ bị ăn mòn hóa học.", False)
        ], "Tính ăn mòn hóa học không phụ thuộc khối lượng riêng."),
        make_tf(2, "Thông hiểu", "Về khối lượng riêng của không khí ở các nhiệt độ khác nhau:", [
            ("a", "Khi nhiệt độ không khí tăng thì không khí dãn nở làm thể tích tăng.", True),
            ("b", "Không khí nóng có khối lượng riêng nhỏ hơn không khí lạnh.", True),
            ("c", "Không khí nóng nhẹ hơn nên bốc lên cao tạo thành dòng đối lưu.", True),
            ("d", "Khinh khí cầu bay lên bằng cách làm lạnh không khí bên trong khí cầu.", False)
        ], "Khinh khí cầu đốt nóng không khí bên trong để giảm D."),
        make_tf(3, "Vận dụng", "Khối đá hoa cương thể tích 0,25 m³ nặng 687,5 kg:", [
            ("a", "Khối lượng riêng của đá là 2 750 kg/m³.", True),
            ("b", "Đổi ra đơn vị g/cm³ là 2,75 g/cm³.", True),
            ("c", "Khối nhôm cùng thể tích nặng hơn khối đá này (D_nhôm = 2 700 kg/m³).", False),
            ("d", "Trọng lượng khối đá hoa cương là 6 875 N.", True)
        ], "D_đá = 2 750 kg/m³ > D_nhôm nên đá nặng hơn nhôm cùng V."),
        make_tf(4, "Vận dụng", "Pha 200 mL nước ngọt nặng 216 g với 300 mL nước khoáng nặng 300 g:", [
            ("a", "Khối lượng riêng nước ngọt ban đầu là 1,08 g/cm³.", True),
            ("b", "Khối lượng riêng nước khoáng là 1,00 g/cm³.", True),
            ("c", "Tổng thể tích dung dịch coi như không đổi là 500 mL.", True),
            ("d", "Khối lượng riêng dung dịch hỗn hợp là 1,04 g/cm³.", False)
        ], "D = 516 / 500 = 1,032 g/cm³.")
    ]
    p3 = [
        make_sa(1, "Thông hiểu", "Khối lượng riêng của dầu hỏa là 800 kg/m³. 2 m³ dầu hỏa nặng bao nhiêu kg?", "1600", "800 × 2 = 1 600 kg."),
        make_sa(2, "Thông hiểu", "Quả cầu nhôm nặng 1,35 kg (D = 2 700 kg/m³). Thể tích quả cầu là bao nhiêu cm³?", "500", "V = 1,35 / 2 700 = 0,0005 m³ = 500 cm³."),
        make_sa(3, "Vận dụng", "Thanh ray đường sắt dài 12 m, tiết diện 50 cm², D = 7 850 kg/m³. Khối lượng thanh ray là bao nhiêu kg?", "471", "V = 12 × 0,005 = 0,06 m³ => m = 7 850 × 0,06 = 471 kg."),
        make_sa(4, "Vận dụng", "Viên gạch 2 lỗ có kích thước ngoài 22 cm × 10 cm × 6 cm. Hai lỗ tròn xuyên suốt có tổng thể tích 120 cm³. Thể tích đất sét thực tế là bao nhiêu cm³?", "1200", "1 320 - 120 = 1 200 cm³."),
        make_sa(5, "Vận dụng cao", "Một thùng chứa 200 lít xăng (D = 700 kg/m³). Trọng lượng xăng trong thùng là bao nhiêu Newton?", "1400", "P = 10 × 700 × 0,2 = 1 400 N."),
        make_sa(6, "Vận dụng cao", "Quả cầu sắt rỗng có thể tích phần vỏ sắt 50 cm³, khoang rỗng 150 cm³ (D_sắt = 7,8 g/cm³). Khối lượng riêng trung bình của quả cầu là bao nhiêu g/cm³?", "1.95", "m = 7,8 × 50 = 390 g. V_tổng = 200 cm³ => D_tb = 390 / 200 = 1,95 g/cm³.")
    ]
    p4 = [
        make_vdc(1, "Tượng Phật bằng đồng nặng 178 kg. Thả vào bể nước thấy nước dâng lên 0,024 m³. Biết D_đồng = 8 900 kg/m³. Thể tích khoang rỗng bên trong tượng là:", ["0,004 m³ (4 lít)", "0,002 m³", "0,020 m³", "Không bị rỗng"], 0, "V_đồng = 178 / 8 900 = 0,020 m³ => V_rỗng = 0,024 - 0,020 = 0,004 m³ = 4 lít."),
        make_vdc(2, "Xe tải chở 15 m³ cát ẩm có độ ẩm 10% theo khối lượng. Biết D_cát khô = 1 400 kg/m³. Khối lượng toàn bộ cát ẩm trên xe xấp xỉ bằng:", ["23 333 kg", "21 000 kg", "25 200 kg", "19 500 kg"], 0, "m_khô = 21 000 kg => m_tổng = 21 000 / 0,9 ≈ 23 333 kg."),
        make_vdc(3, "Đúc chi tiết máy bằng hợp kim gồm 70% nhôm (2 700 kg/m³) và 30% kẽm (7 100 kg/m³) theo thể tích. Khối lượng riêng hợp kim là:", ["4 020 kg/m³", "4 900 kg/m³", "3 580 kg/m³", "5 100 kg/m³"], 0, "D = 0,7 × 2 700 + 0,3 × 7 100 = 4 020 kg/m³."),
        make_vdc(4, "Thùng sắt lập phương cạnh ngoài 40 cm, thành dày 1 cm, không nắp (D_sắt = 7 800 kg/m³). Khối lượng thùng sắt xấp xỉ bằng:", ["60 kg", "75 kg", "48 kg", "92 kg"], 0, "V_ngoài = 64 000 cm³, V_trong = 38 × 38 × 39 = 56 316 cm³. V_sắt = 7 684 cm³ => m ≈ 60 kg.")
    ]
    exams[f"{l13_id}_test3"] = exam_meta(l13_id, l13_name, 3, p1, p2, p3, p4)

    return exams

if __name__ == "__main__":
    exs = get_c3_exams()
    print("Generated:", len(exs))
