# -*- coding: utf-8 -*-
"""
CHƯƠNG III - PHẦN 3 (8 ĐỀ THI ĐỘC LẬP 100%):
- phys8_c3_b17: Bài 17: Lực đẩy Archimedes (3 đề)
- phys8_c3_rev: [Đề tổng hợp] Ôn tập cuối Chương III (5 đề)
"""

import sys
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

def get_c3_part3_exams():
    exams = {}
    ch_id = "phys8_c3"
    ch_title = "Chương III: Khối lượng riêng và áp suất"

    def meta(l_id, l_name, t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # =========================================================================
    # BÀI 17: LỰC ĐẨY ARCHIMEDES (3 ĐỀ)
    # =========================================================================
    l17_id = "phys8_c3_b17"
    l17_name = "Bài 17: Lực đẩy Archimedes"

    # --- B17 ĐỀ 1: Khái niệm & Độ lớn FA ---
    exams[f"{l17_id}_test1"] = meta(l17_id, l17_name, 1,
        [
            make_mc(1, "Nhận biết", "Phương và chiều của lực đẩy Archimedes tác dụng lên vật nhúng trong chất lỏng là:", ["Phương thẳng đứng, chiều từ dưới lên trên", "Phương thẳng đứng, chiều từ trên xuống dưới", "Phương nằm ngang", "Phương vuông góc với đáy bình"], 0, "Lực đẩy Acsimet luôn hướng thẳng đứng từ dưới lên."),
            make_mc(2, "Nhận biết", "Độ lớn của lực đẩy Archimedes tác dụng lên vật chìm trong chất lỏng bằng:", ["Trọng lượng của phần chất lỏng bị vật chiếm chỗ", "Trọng lượng của chính vật đó", "Khối lượng của vật", "Áp suất chất lỏng tại đáy"], 0, "FA = d.V (trọng lượng phần chất lỏng bị chiếm chỗ)."),
            make_mc(3, "Nhận biết", "Công thức tính độ lớn lực đẩy Archimedes là:", ["FA = d × V", "FA = d / V", "FA = V / d", "FA = m × V"], 0, "FA = d.V."),
            make_mc(4, "Nhận biết", "Trong công thức FA = d.V, V là:", ["Thể tích phần vật chìm trong chất lỏng", "Thể tích toàn bộ bình chứa", "Thể tích chất lỏng còn lại", "Thể tích phần vật nổi"], 0, "V là thể tích phần vật ngập trong chất lỏng."),
            make_mc(5, "Nhận biết", "Treo vật vào lực kế trong không khí lực kế chỉ P, nhúng chìm vào nước lực kế chỉ P'. Lực đẩy Archimedes bằng:", ["FA = P - P'", "FA = P + P'", "FA = P / P'", "FA = P' - P"], 0, "FA = P - P'."),
            make_mc(6, "Nhận biết", "Lực đẩy Archimedes xuất hiện trong môi trường nào?", ["Chất lỏng và chất khí", "Chỉ trong chất lỏng", "Chỉ trong nước ngọt", "Chỉ trong chân không"], 0, "Cả chất lỏng và chất khí đều có lực đẩy Acsimet."),
            make_mc(7, "Thông hiểu", "Một vật có thể tích 0,002 m³ chìm hoàn toàn trong nước (d = 10 000 N/m³). Lực đẩy Archimedes tác dụng lên vật là:", ["20 N", "2 N", "200 N", "5 N"], 0, "FA = 10 000 × 0,002 = 20 N."),
            make_mc(8, "Thông hiểu", "Nhúng chìm cùng một khối kim loại lần lượt vào nước (d = 10 000 N/m³) và dầu (d = 8 000 N/m³). So sánh FA:", ["Lực đẩy trong nước lớn hơn trong dầu", "Lực đẩy trong dầu lớn hơn", "Hai lực đẩy bằng nhau", "Không so sánh được"], 0, "Cùng V: d_nước > d_dầu nên FA_nước > FA_dầu."),
            make_mc(9, "Thông hiểu", "Treo quả cầu sắt vào lực kế ngoài không khí chỉ 7,8 N. Nhúng ngập vào nước lực kế chỉ 6,8 N. Độ lớn FA là:", ["1,0 N", "7,8 N", "6,8 N", "14,6 N"], 0, "FA = 7,8 - 6,8 = 1,0 N."),
            make_mc(10, "Thông hiểu", "Khi một quả cầu kim loại chìm dần từ độ sâu 1 m xuống 3 m trong nước thì lực đẩy Archimedes tác dụng lên nó:", ["Không thay đổi", "Tăng gấp 3 lần", "Giảm 3 lần", "Tăng nhẹ"], 0, "FA = d.V không phụ thuộc độ sâu h khi đã ngập hoàn toàn."),
            make_mc(11, "Thông hiểu", "Một quả bóng bay bơm khí heli bay lên không trung được là nhờ:", ["Lực đẩy Archimedes của không khí lớn hơn trọng lượng quả bóng", "Heli đẩy không khí", "Gió cuốn lên", "Lực hút của Mặt Trời"], 0, "FA_kk > P_bóng do d_heli < d_kk."),
            make_mc(12, "Thông hiểu", "Hai vật có cùng thể tích: vật A bằng nhôm, vật B bằng chì cùng nhúng chìm trong nước. So sánh lực đẩy Archimedes:", ["FA tác dụng lên hai vật bằng nhau", "FA lên vật chì lớn hơn vì chì nặng hơn", "FA lên vật nhôm lớn hơn", "Không xác định"], 0, "FA = d.V; cùng V và cùng chất lỏng thì FA như nhau.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về bản chất của lực đẩy Archimedes:", [
                ("a", "Lực đẩy Archimedes sinh ra do chênh lệch áp suất chất lỏng ở mặt dưới và mặt trên của vật.", True),
                ("b", "Độ lớn FA chỉ phụ thuộc vào trọng lượng riêng chất lỏng và thể tích phần chìm của vật.", True),
                ("c", "Vật càng nặng thì lực đẩy Archimedes tác dụng lên nó luôn càng lớn.", False),
                ("d", "Lực đẩy Archimedes có xu hướng nâng vật chuyển động thẳng đứng lên trên.", True)
            ], "FA phụ thuộc thể tích V, không phụ thuộc trọng lượng của vật."),
            make_tf(2, "Thông hiểu", "Khi nhúng một vật vào bình chia độ chứa nước:", [
                ("a", "Thể tích nước dâng lên đúng bằng thể tích phần vật bị chìm.", True),
                ("b", "Trọng lượng phần nước dâng lên đúng bằng độ lớn lực đẩy Archimedes.", True),
                ("c", "Nếu nhúng ngập hoàn toàn thì lực đẩy không phụ thuộc vào độ sâu ngập.", True),
                ("d", "Lực đẩy Archimedes làm giảm khối lượng thực tế của vật.", False)
            ], "Lực đẩy Acsimet làm giảm trọng lượng biểu kiến, không làm đổi khối lượng m."),
            make_tf(3, "Vận dụng", "Khối nhôm thể tích 0,001 m³ nhúng ngập trong nước (d_nước = 10 000 N/m³, D_nhôm = 2 700 kg/m³, g = 10 m/s²):", [
                ("a", "Trọng lượng của khối nhôm là 27 N.", True),
                ("b", "Lực đẩy Archimedes tác dụng lên khối nhôm là 10 N.", True),
                ("c", "Lực kéo của lực kế khi khối nhôm ngập trong nước là 17 N.", True),
                ("d", "Khối nhôm sẽ tự nổi lên mặt nước nếu thả tay ra.", False)
            ], "P = 27 N > FA = 10 N nên khối nhôm sẽ chìm xuống đáy."),
            make_tf(4, "Vận dụng", "Một tảng đá chìm trong nước có thể tích 40 dm³. Lực đẩy Archimedes tác dụng lên tảng đá (d_nước = 10 000 N/m³):", [
                ("a", "Đổi thể tích 40 dm³ = 0,04 m³.", True),
                ("b", "Độ lớn lực đẩy Archimedes là 400 N.", True),
                ("c", "Nếu thả tảng đá vào nước biển (d = 10 300 N/m³) thì lực đẩy là 412 N.", True),
                ("d", "Lực nâng tảng đá dưới nước khó hơn khi nhấc nó ở trên cạn.", False)
            ], "Dưới nước có FA nâng đỡ nên nhấc nhẹ hơn trên cạn.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một vật thể tích 500 cm³ chìm hoàn toàn trong nước (d = 10 000 N/m³). Lực đẩy Archimedes là bao nhiêu Newton?", "5", "10 000 × 0,0005 = 5 N."),
            make_sa(2, "Thông hiểu", "Một vật nặng 15 N ngoài không khí, khi nhúng vào nước lực kế chỉ 11 N. Lực đẩy Archimedes là bao nhiêu N?", "4", "15 - 11 = 4 N."),
            make_sa(3, "Vận dụng", "Khối kim loại chìm trong nước chịu lực đẩy Archimedes là 80 N. Trọng lượng riêng của nước là 10 000 N/m³. Thể tích khối kim loại là bao nhiêu dm³?", "8", "V = 80 / 10 000 = 0,008 m³ = 8 dm³."),
            make_sa(4, "Vận dụng", "Một quả khí cầu có thể tích 200 m³ trong không khí (d_kk = 12,9 N/m³). Lực đẩy Archimedes của không khí tác dụng lên khí cầu là bao nhiêu Newton?", "2580", "FA = 12,9 × 200 = 2 580 N."),
            make_sa(5, "Vận dụng cao", "Một vật chìm hoàn toàn trong dầu (d = 8 000 N/m³) chịu lực đẩy FA = 16 N. Nếu nhúng ngập vào thủy ngân (d = 136 000 N/m³) thì lực đẩy FA là bao nhiêu N?", "272", "V = 16 / 8 000 = 0,002 m³. FA' = 136 000 × 0,002 = 272 N."),
            make_sa(6, "Vận dụng cao", "Treo thỏi hợp kim nặng 3,56 N vào lực kế rồi nhúng vào nước thì lực kế chỉ 3,16 N (d_nước = 10 000 N/m³). Thể tích thỏi hợp kim là bao nhiêu cm³?", "40", "FA = 3,56 - 3,16 = 0,4 N => V = 0,4 / 10 000 = 0,00004 m³ = 40 cm³.")
        ],
        [
            make_vdc(1, "Một bức tượng đúc bằng hợp kim được treo vào lực kế. Ngoài không khí lực kế chỉ 53,4 N. Khi nhúng chìm hoàn toàn trong nước lực kế chỉ 47,4 N. Biết d_nước = 10 000 N/m³ (g = 10 m/s²). Khối lượng riêng của hợp kim đúc tượng là:", ["8 900 kg/m³ (Đồng nguyên chất)", "7 800 kg/m³", "2 700 kg/m³", "11 300 kg/m³"], 0, "FA = 6 N => V = 0,0006 m³. m = 5,34 kg => D = 5,34 / 0,0006 = 8 900 kg/m³."),
            make_vdc(2, "Tại sao khi bước đi dưới nước biển ngang ngực, ta cảm thấy người mình như bay bổng nhẹ tênh và dễ ngã hơn khi đi trên cạn?", ["Lực đẩy Archimedes của nước biển hướng lên trên nâng đỡ phần lớn trọng lượng cơ thể, làm giảm áp lực bàn chân lên cát và giảm ma sát giữ thăng bằng", "Do nước biển quá ấm", "Do sóng biển đẩy", "Do cát biển trơn trượt"], 0, "FA nâng đỡ làm giảm áp lực tiếp xúc và giảm ma sát mặt đất."),
            make_vdc(3, "Một quả cầu bằng sắt có thể tích ngoài 200 cm³ được thả vào nước (d = 10 000 N/m³, D_sắt = 7 800 kg/m³). Để quả cầu sắt có thể lơ lửng trong nước thì thể tích khoang rỗng bên trong quả cầu phải bằng:", ["174,4 cm³", "100 cm³", "150 cm³", "120 cm³"], 0, "P = FA => 10 × 7 800 × V_sắt = 10 000 × 200 × 10^-6 => V_sắt ≈ 25,6 cm³ => V_rỗng = 200 - 25,6 = 174,4 cm³."),
            make_vdc(4, "Một bình chứa nước đặt trên đĩa cân điện tử, cân chỉ 1 200 g. Dùng sợi chỉ mảnh treo một khối nhôm thể tích 50 cm³ rồi nhúng ngập hoàn toàn vào nước trong bình (không chạm đáy bình, nước không tràn). Số chỉ của cân điện tử lúc này là:", ["1 250 g", "1 200 g", "1 335 g", "1 150 g"], 0, "Theo định luật 3 Newton, khối nhôm tác dụng phản lực F' = FA = d.V = 10 000 × 50 × 10^-6 = 0,5 N (tương đương 50 g) nén xuống nước => Cân chỉ 1 250 g.")
        ]
    )

    # --- B17 ĐỀ 2: Điều kiện chìm, lơ lửng, nổi ---
    exams[f"{l17_id}_test2"] = meta(l17_id, l17_name, 2,
        [
            make_mc(1, "Nhận biết", "Điều kiện để một vật CHÌM xuống đáy khi thả vào chất lỏng là:", ["Trọng lượng P lớn hơn lực đẩy Archimedes FA (dvật > dchất lỏng)", "P = FA", "P < FA", "dvật < dchất lỏng"], 0, "P > FA thì vật chìm xuống."),
            make_mc(2, "Nhận biết", "Điều kiện để một vật LƠ LỬNG trong lòng chất lỏng là:", ["P = FA (dvật = dchất lỏng)", "P > FA", "P < FA", "dvật > dchất lỏng"], 0, "P = FA thì vật lơ lửng ở bất kì vị trí nào trong lòng chất lỏng."),
            make_mc(3, "Nhận biết", "Điều kiện để một vật NỔI lên mặt thoáng chất lỏng là:", ["Khi nhúng ngập thì P < FA (dvật < dchất lỏng)", "P > FA", "P = FA", "dvật > dchất lỏng"], 0, "P < FA đẩy vật nổi lên."),
            make_mc(4, "Nhận biết", "Khi vật đã nổi và đứng yên cân bằng trên mặt nước thì độ lớn lực đẩy Archimedes:", ["Bằng đúng trọng lượng P của vật", "Lớn hơn trọng lượng P", "Nhỏ hơn trọng lượng P", "Bằng 0"], 0, "Nổi cân bằng: hai lực cân bằng FA = P."),
            make_mc(5, "Nhận biết", "Công thức tính lực đẩy Archimedes khi vật nổi thăng bằng là:", ["FA = dchất lỏng × Vchìm", "FA = dchất lỏng × Vvật", "FA = dvật × Vvật", "FA = dvật × Vchìm"], 0, "FA = d_cl . V_chìm."),
            make_mc(6, "Nhận biết", "Thả một khối gỗ (D = 800 kg/m³) vào nước (D = 1 000 kg/m³). Khối gỗ sẽ:", ["Nổi một phần trên mặt nước", "Chìm hẳn xuống đáy", "Lơ lửng trong nước", "Hòa tan vào nước"], 0, "D_gỗ < D_nước nên khối gỗ nổi một phần."),
            make_mc(7, "Thông hiểu", "Một quả trứng gà chìm dưới đáy cốc nước ngọt. Muốn quả trứng nổi lên, người ta nên:", ["Hòa thêm muối ăn vào nước để tăng khối lượng riêng của nước", "Đổ thêm nước cất", "Khuấy mạnh nước", "Đun nóng nước"], 0, "Tăng d_nước muối > d_trứng làm trứng nổi lên."),
            make_mc(8, "Thông hiểu", "Thả một khối sáp nến (D = 900 kg/m³) vào rượu (D = 800 kg/m³). Khối sáp nến sẽ:", ["Chìm xuống đáy", "Nổi trên mặt rượu", "Lơ lửng", "Bốc hơi"], 0, "D_sáp > D_rượu nên khối sáp chìm."),
            make_mc(9, "Thông hiểu", "Một khúc gỗ nổi trên mặt nước có thể tích 0,05 m³. Biết phần chìm chiếm 60% thể tích khối gỗ. Thể tích phần chìm là:", ["0,03 m³", "0,02 m³", "0,05 m³", "0,01 m³"], 0, "0,05 × 0,6 = 0,03 m³."),
            make_mc(10, "Thông hiểu", "Con tàu chở hàng nổi cân bằng trên biển. Khi bốc thêm 500 tấn hàng lên tàu thì:", ["Tàu chìm sâu thêm làm lực đẩy Archimedes tăng thêm đúng 5 000 000 N", "Lực đẩy Archimedes không đổi", "Tàu nổi cao hơn", "Áp suất đáy tàu giảm"], 0, "Thêm hàng làm P tăng => FA tăng tương ứng FA = P."),
            make_mc(11, "Thông hiểu", "Cá có thể dễ dàng lặn sâu hoặc nổi lên mặt nước là nhờ cơ quan nào?", ["Bóng hơi (bong bóng cá) thay đổi thể tích làm thay đổi khối lượng riêng trung bình của cá", "Vây cá to", "Đuôi cá quạt nước", "Mang cá thở"], 0, "Bóng hơi điều chỉnh thể tích thay đổi D_tb của cá."),
            make_mc(12, "Thông hiểu", "Một miếng tôn mỏng thả vào nước thì chìm nghỉm, nhưng gập thành chiếc thuyền tôn nhỏ thì nổi được vì:", ["Hình dáng thuyền tạo khoang chứa không khí làm D trung bình nhỏ hơn nước", "Tôn nhẹ đi", "Nước mặn hơn", "Tôn biến thành chất khác"], 0, "Khoang rỗng chứa khí làm D_tb < D_nước.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về trạng thái chìm, lơ lửng, nổi của vật rắn trong chất lỏng:", [
                ("a", "So sánh khối lượng riêng D của vật và chất lỏng quyết định trạng thái nổi hay chìm.", True),
                ("b", "Vật đặc có D_vật = D_chất lỏng sẽ lơ lửng ở bất kì độ sâu nào trong lòng chất lỏng.", True),
                ("c", "Khi vật đang nổi lên trên mặt nước thì lực đẩy FA nhỏ hơn trọng lượng P.", False),
                ("d", "Khi vật đã nổi cân bằng thì lực đẩy FA bằng đúng trọng lượng P.", True)
            ], "Khi đang nổi lên thì FA > P."),
            make_tf(2, "Thông hiểu", "Hiện tượng tảng băng trôi trên đại dương:", [
                ("a", "Nước đá có D ≈ 920 kg/m³ nhỏ hơn nước biển D ≈ 1 030 kg/m³.", True),
                ("b", "Phần lớn thể tích của tảng băng trôi (khoảng 90%) bị chìm dưới mặt nước biển.", True),
                ("c", "Phần băng nổi chỉ chiếm khoảng 10% thể tích toàn bộ tảng băng.", True),
                ("d", "Khi toàn bộ tảng băng tan chảy hết sẽ làm nước biển dâng cao tràn trề ngay tức khắc.", False)
            ], "Băng nổi tan ra bù đúng thể tích phần nước bị chiếm chỗ nên mực nước không đổi."),
            make_tf(3, "Vận dụng", "Khối gỗ hình lập phương cạnh 10 cm nổi thăng bằng trên nước (D_nước = 1 000 kg/m³), chiều cao phần chìm là 7 cm:", [
                ("a", "Thể tích toàn bộ khối gỗ là 1 000 cm³.", True),
                ("b", "Thể tích phần gỗ chìm trong nước là 700 cm³.", True),
                ("c", "Lực đẩy Archimedes tác dụng lên khối gỗ là 7 N (g = 10 m/s²).", True),
                ("d", "Khối lượng riêng của khối gỗ là 800 kg/m³.", False)
            ], "D_gỗ = (700 / 1 000) × 1 000 = 700 kg/m³."),
            make_tf(4, "Vận dụng", "Phao cứu sinh hình vành khăn có thể tích 0,02 m³, khối lượng 2 kg (d_nước = 10 000 N/m³):", [
                ("a", "Trọng lượng của phao cứu sinh là 20 N.", True),
                ("b", "Lực đẩy Archimedes cực đại khi phao ngập hoàn toàn là 200 N.", True),
                ("c", "Lực nâng hữu ích tối đa mà phao có thể nâng thêm là 180 N (nâng được người nặng 18 kg ở trên cạn).", True),
                ("d", "Phao cứu sinh không thể giúp người nổi đầu trên mặt nước biển.", False)
            ], "Dưới nước cơ thể người gần như lơ lửng, lực 180 N thừa sức giữ đầu người nổi trên mặt nước.")
        ],
        [
            make_sa(1, "Thông hiểu", "Khối gỗ nặng 40 N nổi thăng bằng trên mặt nước. Lực đẩy Archimedes là bao nhiêu Newton?", "40", "FA = P = 40 N."),
            make_sa(2, "Thông hiểu", "Vật có trọng lượng 50 N thả vào nước chịu lực đẩy cực đại FA = 60 N. Khi đứng yên trên mặt nước, lực đẩy FA là bao nhiêu N?", "50", "Khi nổi thăng bằng FA = P = 50 N."),
            make_sa(3, "Vận dụng", "Khối sáp nến nặng 1,8 kg nổi trên nước (d = 10 000 N/m³). Thể tích phần chìm trong nước là bao nhiêu dm³?", "1.8", "V_chìm = 18 / 10 000 = 0,0018 m³ = 1,8 dm³."),
            make_sa(4, "Vận dụng", "Một tảng băng có thể tích 10 m³ trôi trên biển (d_nước biển = 10 300 N/m³, d_băng = 9 270 N/m³). Thể tích phần chìm là bao nhiêu m³?", "9", "V_chìm = 10 × 9 270 / 10 300 = 9 m³."),
            make_sa(5, "Vận dụng cao", "Khối gỗ hình hộp đáy 100 cm², cao 20 cm thả nổi trong nước thấy nhô lên khỏi mặt nước 4 cm. Khối lượng riêng khối gỗ là bao nhiêu kg/m³? (D_nước = 1 000 kg/m³)", "800", "h_chìm = 16 cm => D = 1 000 × 16 / 20 = 800 kg/m³."),
            make_sa(6, "Vận dụng cao", "Chiếc xà lan hình hộp chữ nhật dài 20 m, rộng 5 m, thành cao 2 m. Khi không chở hàng xà lan chìm sâu 0,5 m. Khối lượng của xà lan rỗng là bao nhiêu tấn? (D_nước = 1 000 kg/m³)", "50", "V_chìm = 20 × 5 × 0,5 = 50 m³ => m = 50 tấn.")
        ],
        [
            make_vdc(1, "Một chiếc tàu chở hàng đi từ sông nước ngọt (D1 = 1 000 kg/m³) ra biển nước mặn (D2 = 1 030 kg/m³). Trạng thái nổi của tàu sẽ thay đổi như thế nào?", ["Tàu sẽ nổi cao hơn một chút (mớn nước giảm) do khối lượng riêng của nước biển lớn hơn nước ngọt", "Tàu chìm sâu hơn", "Mực nước mớn nước giữ nguyên không đổi", "Tàu bị nghiêng"], 0, "P = FA = d.V_chìm không đổi; d tăng thì V_chìm giảm => tàu nổi cao hơn."),
            make_vdc(2, "Một cốc thủy tinh chứa nước và một cục nước đá đang nổi thăng bằng. Khi cục nước đá tan chảy hoàn toàn thành nước lỏng thì mực nước trong cốc sẽ:", ["Giữ nguyên không thay đổi", "Dâng cao tràn ra ngoài", "Tụt thấp xuống", "Lúc đầu dâng sau đó tụt"], 0, "Trọng lượng nước đá bằng trọng lượng nước tan ra, đúng bằng thể tích phần chìm ban đầu nên mực nước không đổi."),
            make_vdc(3, "Một khối lập phương cạnh a = 10 cm làm bằng chất liệu xốp nổi ở mặt phân cách giữa hai lớp chất lỏng không hòa tan trong một bình: lớp trên là dầu (D1 = 800 kg/m³), lớp dưới là nước (D2 = 1 000 kg/m³). Biết khối lập phương chìm 6 cm trong nước và 4 cm trong dầu. Khối lượng riêng của khối xốp là:", ["920 kg/m³", "880 kg/m³", "900 kg/m³", "850 kg/m³"], 0, "D = (0,4 × 800 + 0,6 × 1 000) = 320 + 600 = 920 kg/m³."),
            make_vdc(4, "Một tảng băng nổi trên mặt nước biển mang trên mình một chú chim cánh cụt nặng 30 kg. Biết D_băng = 900 kg/m³, D_nước biển = 1 030 kg/m³ (g = 10 m/s²). Thể tích tối thiểu của tảng băng để chim cánh cụt không bị ướt chân là:", ["Khoảng 0,23 m³", "Khoảng 0,50 m³", "Khoảng 0,10 m³", "Khoảng 1,00 m³"], 0, "FA_max = P_băng + P_chim => 10 300 V = 9 000 V + 300 => 1 300 V = 300 => V ≈ 0,2308 m³.")
        ]
    )

    # --- B17 ĐỀ 3: Ứng dụng thực tế của lực đẩy Archimedes ---
    exams[f"{l17_id}_test3"] = meta(l17_id, l17_name, 3,
        [
            make_mc(1, "Nhận biết", "Con tàu bằng thép nặng hàng vạn tấn có thể nổi trên mặt biển là nhờ:", ["Vỏ tàu thiết kế dạng khoang rỗng chứa nhiều không khí làm khối lượng riêng trung bình của tàu nhỏ hơn nước biển", "Thép làm tàu nhẹ hơn nước", "Động cơ đẩy nước", "Sóng biển nâng lên"], 0, "D trung bình của tàu nhỏ hơn nước biển."),
            make_mc(2, "Nhận biết", "Vạch dấu mớn nước Plimsoll sơn ở vỏ tàu thủy dùng để chỉ dẫn:", ["Giới hạn tải trọng chìm tối đa an toàn trong các vùng nước và mùa khác nhau", "Tốc độ chạy tối đa", "Độ sâu của biển", "Màu sơn trang trí"], 0, "Vạch an toàn tải trọng mớn nước."),
            make_mc(3, "Nhận biết", "Dụng cụ đo nồng độ rượu hoặc độ ngọt của mật mía hoạt động dựa trên định luật Archimedes là:", ["Tỉ trọng kế (phù kế)", "Áp kế", "Nhiệt kế", "Lực kế"], 0, "Tỉ trọng kế chìm sâu hay nông tùy nồng độ chất lỏng."),
            make_mc(4, "Nhận biết", "Khí nào sau đây thường được nạp vào khinh khí cầu và bóng thám không để bay lên cao an toàn?", ["Khí Heli (He)", "Khí Oxy (O2)", "Khí Carbon dioxide (CO2)", "Khí Nitơ (N2)"], 0, "Heli nhẹ hơn không khí và không cháy nổ."),
            make_mc(5, "Nhận biết", "Tàu ngầm muốn chìm sâu xuống đáy biển phải làm thao tác nào?", ["Mở van cho nước biển tràn vào các khoang dằn để tăng trọng lượng", "Bơm không khí vào khoang", "Vứt bỏ động cơ", "Bật đèn pha"], 0, "Hút nước biển vào khoang dằn làm P > FA."),
            make_mc(6, "Nhận biết", "Khi tắm biển ở Biển Chết (Israel), con người có thể nổi bồng bềnh đọc báo mà không cần bơi vì:", ["Nước Biển Chết có độ mặn cực cao làm khối lượng riêng của nước lớn hơn cơ thể người rất nhiều", "Biển Chết không có sóng", "Nước Biển Chết rất ấm", "Không khí ở đó đậm đặc"], 0, "D_nước biển chết ≈ 1 240 kg/m³ > D_người."),
            make_mc(7, "Thông hiểu", "Một quả bóng bàn bị móp một chút được thả vào cốc nước nóng sẽ phồng trở lại và nổi trên mặt nước. Khi phồng lại, lực đẩy Archimedes tác dụng lên nó:", ["Tăng lên vì thể tích quả bóng tăng", "Giảm đi", "Không đổi", "Bằng 0"], 0, "Thể tích V tăng nên FA = d.V tăng."),
            make_mc(8, "Thông hiểu", "Thả một thỏi nhôm và một thỏi chì có cùng khối lượng vào chậu thủy ngân (D_Hg = 13 600 kg/m³). Cả hai thỏi sẽ:", ["Cùng nổi trên mặt thủy ngân", "Cùng chìm xuống đáy", "Nhôm nổi còn chì chìm", "Chì nổi còn nhôm chìm"], 0, "Cả nhôm (2 700) và chì (11 300) đều có D < 13 600 nên cùng nổi."),
            make_mc(9, "Thông hiểu", "Tỉ trọng kế khi thả vào chất lỏng có khối lượng riêng càng lớn thì phần chìm của tỉ trọng kế sẽ:", ["Càng ít (nổi càng cao)", "Càng nhiều (chìm càng sâu)", "Không đổi", "Chìm hẳn xuống đáy"], 0, "d lớn thì V_chìm nhỏ để FA = P."),
            make_mc(10, "Thông hiểu", "Một người tập bơi đeo phao bơi vào người, thể tích phần cơ thể chìm trong nước sẽ:", ["Giảm đi so với khi không đeo phao", "Tăng lên", "Không đổi", "Bằng 0"], 0, "Phao gánh bớt lực đẩy nên người nổi cao hơn."),
            make_mc(11, "Thông hiểu", "Khi thợ lặn muốn nổi lên mặt nước biển, họ thực hiện:", ["Bơm khí nén vào áo phao cân bằng để tăng thể tích chiếm chỗ của cơ thể", "Xả hết khí trong áo phao", "Thả rơi bình dưỡng khí", "Bơi thật nhanh xuống đáy"], 0, "Tăng thể tích áo phao làm tăng FA đẩy lên."),
            make_mc(12, "Thông hiểu", "Tại sao người ta có thể trục vớt tàu đắm bằng các phao cứu sinh bơm khí nén chằng buộc quanh thân tàu?", ["Các túi khí tạo ra lực đẩy Archimedes khổng lồ vượt quá trọng lượng con tàu để kéo tàu nổi lên", "Túi khí làm nhẹ thép", "Túi khí hút hết nước biển", "Túi khí làm nóng tàu"], 0, "Tạo lực đẩy Acsimet khổng lồ nâng xác tàu.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về hoạt động của tàu thủy và tàu ngầm:", [
                ("a", "Tàu thủy nổi được là nhờ lực đẩy Archimedes cân bằng với trọng lượng tàu.", True),
                ("b", "Khi tàu thủy chở nặng, phần thể tích chìm dưới nước tăng lên.", True),
                ("c", "Tàu ngầm nổi lên bằng cách dùng khí nén đẩy nước ra khỏi các khoang dằn.", True),
                ("d", "Khối lượng riêng trung bình của tàu ngầm luôn cố định không thể thay đổi.", False)
            ], "Tàu ngầm thay đổi D trung bình nhờ khoang dằn."),
            make_tf(2, "Thông hiểu", "Ứng dụng của tỉ trọng kế trong kiểm tra chất lượng:", [
                ("a", "Tỉ trọng kế gồm một ống thủy tinh có bầu chì ở đáy để giữ thăng bằng thẳng đứng.", True),
                ("b", "Thang chia độ của tỉ trọng kế có số đo tăng dần từ trên xuống dưới.", True),
                ("c", "Dùng tỉ trọng kế có thể biết sữa tươi có bị pha loãng với nước hay không.", True),
                ("d", "Tỉ trọng kế chìm sâu nhất trong chất lỏng có khối lượng riêng lớn nhất.", False)
            ], "Chất lỏng càng đậm đặc thì tỉ trọng kế càng nổi cao."),
            make_tf(3, "Vận dụng", "Một khinh khí cầu có thể tích 600 m³, vỏ khí cầu và giỏ treo nặng 200 kg. Nạp đầy khí heli có d_heli = 1,8 N/m³. Biết d_kk = 12,9 N/m³ (g = 10 m/s²):", [
                ("a", "Lực đẩy Archimedes của không khí tác dụng lên khí cầu là 7 740 N.", True),
                ("b", "Trọng lượng của khí heli trong khí cầu là 1 080 N.", True),
                ("c", "Tổng trọng lượng của vỏ, giỏ và khí heli là 3 080 N.", True),
                ("d", "Lực nâng hữu ích tối đa để mang người và hàng hóa là 4 660 N (khoảng 466 kg).", True)
            ], "FA = 12,9 × 600 = 7 740 N. P_tổng = 2 000 + 1 080 = 3 080 N => F_nâng = 4 660 N."),
            make_tf(4, "Vận dụng", "Chiếc xà lan chở hàng có khối lượng vỏ 80 tấn. Kích thước đáy 30 m × 6 m. Thả trên sông (d_nước = 10 000 N/m³):", [
                ("a", "Khi chưa chở hàng, xà lan chìm sâu khoảng 0,44 m.", True),
                ("b", "Khi chất thêm 180 tấn hàng, tổng trọng lượng là 2 600 000 N.", True),
                ("c", "Chiều sâu chìm (mớn nước) khi chở đủ hàng là khoảng 1,44 m.", True),
                ("d", "Nếu sông chỉ sâu 1,2 m thì xà lan chở đủ hàng vẫn đi qua an toàn.", False)
            ], "Mớn nước 1,44 m > 1,2 m nên xà lan sẽ bị mắc cạn.")
        ],
        [
            make_sa(1, "Thông hiểu", "Con tàu có trọng lượng 50 000 kN nổi trên biển. Lực đẩy Archimedes tác dụng lên tàu là bao nhiêu MN?", "50", "FA = P = 50 MN."),
            make_sa(2, "Thông hiểu", "Tỉ trọng kế nặng 0,2 N thả vào rượu nổi thăng bằng. Lực đẩy Archimedes tác dụng lên tỉ trọng kế là bao nhiêu N?", "0.2", "FA = P = 0,2 N."),
            make_sa(3, "Vận dụng", "Một phao tiêu hình trụ thể tích 0,8 m³ nặng 200 kg thả trên sông (d = 10 000 N/m³, g = 10 m/s²). Thể tích phần nổi của phao tiêu là bao nhiêu m³?", "0.6", "V_chìm = 2 000 / 10 000 = 0,2 m³ => V_nổi = 0,8 - 0,2 = 0,6 m³."),
            make_sa(4, "Vận dụng", "Bơm khí heli vào bóng thám không thể tích 10 m³. Lực đẩy Archimedes của không khí (d_kk = 12,9 N/m³) lên bóng là bao nhiêu Newton?", "129", "12,9 × 10 = 129 N."),
            make_sa(5, "Vận dụng cao", "Một phao cứu sinh nâng được người nặng tối đa 65 kg chìm trong nước (khối lượng riêng cơ thể người coi như 1 000 kg/m³, chỉ đầu nổi 5 kg trên mặt nước). Lực nâng của phao cần thiết tối thiểu là bao nhiêu Newton? (g = 10 m/s²)", "50", "Phần chìm cơ thể gần như trung hòa trọng lượng, phao chỉ cần nâng phần đầu nhô lên: 5 × 10 = 50 N."),
            make_sa(6, "Vận dụng cao", "Một xà lan có diện tích đáy 150 m² chở thêm 45 tấn hàng. Mớn nước của xà lan tăng thêm bao nhiêu cm trong nước sông (D = 1 000 kg/m³)?", "30", "ΔV = 45 m³ => Δh = 45 / 150 = 0,3 m = 30 cm.")
        ],
        [
            make_vdc(1, "Một người muốn tự chế chiếc bè cứu sinh bằng các thùng phuy nhựa rỗng loại 200 lít (thể tích mỗi thùng 0,2 m³, nặng 10 kg). Bè cần chở an toàn 8 người với tổng tải trọng người và khung bè là 600 kg. Coi mức ngập an toàn là 80% thể tích thùng (d_nước = 10 000 N/m³). Số lượng thùng phuy tối thiểu cần dùng là:", ["4 thùng", "3 thùng", "6 thùng", "5 thùng"], 0, "Lực nâng an toàn mỗi thùng = 10 000 × 0,16 - 100 = 1 500 N. Để nâng 6 000 N cần: 6 000 / 1 500 = 4 thùng."),
            make_vdc(2, "Một khối hợp kim nhôm và chì nặng 2,11 kg thả vào nước chịu lực đẩy Archimedes là 3,0 N (d_nước = 10 000 N/m³). Biết D_nhôm = 2 700 kg/m³, D_chì = 11 300 kg/m³ (g = 10 m/s²). Khối lượng của nhôm trong khối hợp kim là:", ["0,54 kg (540 g)", "1,13 kg", "0,81 kg", "1,57 kg"], 0, "V = 0,0003 m³. m1 + m2 = 2,11; m1/2700 + m2/11300 = 0,0003 => m_nhôm = 0,54 kg."),
            make_vdc(3, "Một chiếc thuyền nhỏ bằng gỗ có gắn một cục đá nặng ở đáy thuyền nổi trên mặt nước trong một hồ bơi kín. Nếu người trên thuyền nhấc cục đá ném xuống đáy hồ bơi (cục đá chìm nghỉm) thì mực nước trong hồ bơi sẽ:", ["Tụt thấp xuống một chút", "Dâng cao hơn", "Không thay đổi", "Lúc đầu dâng sau tụt"], 0, "Trên thuyền: đá chiếm thể tích nước tương ứng với trọng lượng đá V1 = P/d_nước. Khi chìm ở đáy: đá chỉ chiếm thể tích thực V2 = P/d_đá. Vì d_đá > d_nước nên V2 < V1 => mực nước hồ tụt xuống."),
            make_vdc(4, "Một bong bóng khí nổi từ đáy hồ nước sâu 10 m lên mặt nước. Coi nhiệt độ không đổi, áp suất khí quyển là 100 kPa (d_nước = 10 000 N/m³). Khi chạm mặt nước, thể tích của bong bóng khí so với ở đáy hồ đã:", ["Tăng gấp 2 lần", "Tăng gấp 4 lần", "Không thay đổi", "Giảm một nửa"], 0, "p_đáy = p_kq + d.h = 100 + 100 = 200 kPa. p_mặt = 100 kPa. Theo định luật Boyle, áp suất giảm một nửa thì thể tích tăng gấp 2 lần.")
        ]
    )

    # =========================================================================
    # PHYS8_C3_REV: [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG III (5 ĐỀ)
    # =========================================================================
    lrev_id = "phys8_c3_rev"
    lrev_name = "[Đề tổng hợp] Ôn tập cuối Chương III"

    # --- REV ĐỀ 1: Tổng hợp Khối lượng riêng & Áp suất chất rắn ---
    exams[f"{lrev_id}_test1"] = meta(lrev_id, lrev_name, 1,
        [
            make_mc(1, "Nhận biết", "Khối lượng riêng D và trọng lượng riêng d liên hệ với nhau theo hệ thức:", ["d = 10 × D", "D = 10 × d", "d = D / 10", "d × D = 10"], 0, "d = 10D."),
            make_mc(2, "Nhận biết", "Áp suất tác dụng lên một bề mặt phụ thuộc vào hai yếu tố nào?", ["Áp lực và diện tích mặt bị ép", "Trọng lượng và độ cao", "Khối lượng và thể tích", "Vận tốc và thời gian"], 0, "p = F / S."),
            make_mc(3, "Nhận biết", "Một vật có khối lượng m, thể tích V thì khối lượng riêng được tính bằng:", ["D = m / V", "D = V / m", "D = m × V", "D = m - V"], 0, "D = m/V."),
            make_mc(4, "Nhận biết", "Đơn vị chuẩn của áp suất trong hệ SI là:", ["Pascal (Pa)", "Newton (N)", "Joule (J)", "Watt (W)"], 0, "Pascal (Pa)."),
            make_mc(5, "Nhận biết", "Để giảm độ lún của công trình xây dựng xuống nền đất yếu, người ta:", ["Làm móng bè có diện tích đáy lớn", "Làm móng nhọn", "Xây tường thật dày", "Tăng thêm trọng lượng"], 0, "Tăng diện tích móng để giảm áp suất."),
            make_mc(6, "Nhận biết", "Đầu lưỡi cuốc, xẻng được mài sắc để:", ["Giảm diện tích tiếp xúc nhằm tăng áp suất cắm sâu vào đất", "Tăng ma sát", "Làm nhẹ xẻng", "Chống gỉ"], 0, "Giảm S tăng áp suất."),
            make_mc(7, "Thông hiểu", "Một khối sắt có thể tích 200 cm³, D = 7 800 kg/m³. Khối lượng của khối sắt là:", ["1,56 kg", "15,6 kg", "0,156 kg", "3,9 kg"], 0, "m = 7 800 × 0,0002 = 1,56 kg."),
            make_mc(8, "Thông hiểu", "Áp lực 1 200 N tác dụng lên mặt sàn diện tích 0,04 m². Áp suất gây ra là:", ["30 000 Pa", "48 Pa", "3 000 Pa", "48 000 Pa"], 0, "1 200 / 0,04 = 30 000 Pa."),
            make_mc(9, "Thông hiểu", "Một can chứa 10 lít dầu ăn nặng 8 kg. Khối lượng riêng của dầu ăn là:", ["800 kg/m³", "850 kg/m³", "900 kg/m³", "1 250 kg/m³"], 0, "D = 8 / 0,01 = 800 kg/m³."),
            make_mc(10, "Thông hiểu", "Đặt một khối kim loại hình hộp lên mặt bàn. Nếu lật khối kim loại sang mặt có diện tích nhỏ hơn 2 lần thì áp suất:", ["Tăng gấp 2 lần", "Giảm 2 lần", "Không đổi", "Tăng 4 lần"], 0, "S giảm 2 lần thì p tăng 2 lần."),
            make_mc(11, "Thông hiểu", "Một viên gạch có kích thước 20 cm × 10 cm × 5 cm nặng 1,2 kg. Khối lượng riêng của viên gạch là:", ["1 200 kg/m³", "1 500 kg/m³", "2 400 kg/m³", "600 kg/m³"], 0, "V = 0,001 m³ => D = 1,2 / 0,001 = 1 200 kg/m³."),
            make_mc(12, "Thông hiểu", "Một xe lu nặng 8 tấn nén lên mặt đường tiếp xúc 0,4 m² (g = 10 m/s²). Áp suất xe lu gây ra là:", ["200 000 Pa", "20 000 Pa", "80 000 Pa", "320 000 Pa"], 0, "80 000 / 0,4 = 200 000 Pa.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về khối lượng riêng và áp suất chất rắn:", [
                ("a", "Khối lượng riêng là thuộc tính của chất, không phụ thuộc hình dạng vật.", True),
                ("b", "Áp suất là tác dụng của áp lực tính trên một đơn vị diện tích bị ép.", True),
                ("c", "Vật có khối lượng càng lớn thì luôn gây ra áp suất càng lớn.", False),
                ("d", "1 Pa tương đương với 1 N/m².", True)
            ], "Áp suất còn phụ thuộc vào diện tích tiếp xúc S."),
            make_tf(2, "Thông hiểu", "Biện pháp kỹ thuật kiểm soát áp suất:", [
                ("a", "Bánh xe máy cày thiết kế bản xích rộng để tránh lún ruộng bùn.", True),
                ("b", "Mũi kim tiêm y tế mài vát nhọn để giảm lực đâm xuyên qua da.", True),
                ("c", "Tà vẹt kê dưới đường ray làm giảm áp suất của tàu hỏa lên nền đường.", True),
                ("d", "Đi giày cao gót lên nền gỗ mềm ít gây lún hơn đi giày đế bệt.", False)
            ], "Giày cao gót có diện tích gót rất nhỏ gây áp suất cực lớn làm xước lõm gỗ."),
            make_tf(3, "Vận dụng", "Khối đá hoa cương hình hộp 50 cm × 40 cm × 20 cm nặng 108 kg (g = 10 m/s²):", [
                ("a", "Thể tích khối đá là 0,04 m³.", True),
                ("b", "Khối lượng riêng của đá là 2 700 kg/m³.", True),
                ("c", "Áp suất nhỏ nhất lên sàn khi đặt mặt 50 cm × 40 cm là 5 400 Pa.", True),
                ("d", "Áp suất lớn nhất lên sàn là 10 800 Pa.", False)
            ], "S_min = 0,4 × 0,2 = 0,08 m² => p_max = 1 080 / 0,08 = 13 500 Pa."),
            make_tf(4, "Vận dụng", "Người có khối lượng 50 kg đứng trên mặt sàn tiếp xúc 2 bàn chân diện tích 250 cm² (g = 10 m/s²):", [
                ("a", "Trọng lượng người là 500 N.", True),
                ("b", "Áp suất khi đứng 2 chân là 20 000 Pa.", True),
                ("c", "Khi co 1 chân lên thì áp suất tăng lên thành 40 000 Pa.", True),
                ("d", "Áp lực người đó tác dụng lên sàn khi đứng 1 chân tăng gấp đôi.", False)
            ], "Áp lực F = P = 500 N không đổi.")
        ],
        [
            make_sa(1, "Thông hiểu", "Khối lượng riêng của sắt là 7 800 kg/m³. Đổi sang g/cm³ được bao nhiêu?", "7.8", "7,8 g/cm³."),
            make_sa(2, "Thông hiểu", "Tác dụng áp lực 500 N lên diện tích 0,02 m². Áp suất sinh ra là bao nhiêu kPa?", "25", "500 / 0,02 = 25 000 Pa = 25 kPa."),
            make_sa(3, "Vận dụng", "Khối nhôm nặng 810 g có thể tích 300 cm³. Trọng lượng riêng của nhôm là bao nhiêu N/m³?", "27000", "D = 2,7 g/cm³ = 2 700 kg/m³ => d = 27 000 N/m³."),
            make_sa(4, "Vận dụng", "Một xe tải 4 bánh nặng 2 tấn có diện tích tiếp xúc mỗi bánh là 100 cm² (g = 10 m/s²). Áp suất mỗi bánh xe lên đường là bao nhiêu kPa?", "500", "F = 5 000 N => p = 5 000 / 0,01 = 500 kPa."),
            make_sa(5, "Vận dụng cao", "Cột bê tông hình hộp cao 4 m, D = 2 500 kg/m³ đặt đứng trên nền móng (g = 10 m/s²). Áp suất do cột bê tông tác dụng lên móng là bao nhiêu kPa?", "100", "p = 10Dh = 10 × 2 500 × 4 = 100 000 Pa = 100 kPa."),
            make_sa(6, "Vận dụng cao", "Một chiếc đinh có tiết diện đầu nhọn 0,2 mm². Gõ búa tạo lực 40 N. Áp suất ở đầu mũi đinh là bao nhiêu MPa?", "200", "40 / (0,2 × 10^-6) = 200 MPa.")
        ],
        [
            make_vdc(1, "Một bức tượng đồng đặc nặng 89 kg. Khi nhúng chìm vào nước thì thể tích nước dâng lên đúng bằng 10 dm³. Khối lượng riêng của đồng đúc tượng là:", ["8 900 kg/m³ (Đồng nguyên chất)", "7 800 kg/m³", "2 700 kg/m³", "11 300 kg/m³"], 0, "D = 89 / 0,01 = 8 900 kg/m³."),
            make_vdc(2, "Một móng nhà hình chữ nhật chịu tải trọng toàn bộ ngôi nhà là 600 kN. Nền đất chỉ chịu được áp suất tối đa 150 kPa. Diện tích đáy móng tối thiểu phải là:", ["4 m²", "2 m²", "6 m²", "8 m²"], 0, "S = 600 / 150 = 4 m²."),
            make_vdc(3, "Một viên gạch hai lỗ có kích thước ngoài 20 cm × 10 cm × 6 cm. Hai lỗ tròn xuyên suốt có tổng thể tích 150 cm³. Khối lượng viên gạch là 1,89 kg. Khối lượng riêng thực tế của đất sét làm gạch là:", ["1 800 kg/m³", "2 100 kg/m³", "1 575 kg/m³", "2 400 kg/m³"], 0, "V_ngoài = 1 200 cm³, V_thực = 1 200 - 150 = 1 050 cm³ = 0,00105 m³. D = 1,89 / 0,00105 = 1 800 kg/m³."),
            make_vdc(4, "Một phụ nữ nặng 48 kg đi giày cao gót dồn toàn bộ trọng lượng lên 2 gót giày, mỗi gót diện tích 1 cm² (g = 10 m/s²). Áp suất dưới mỗi gót giày tác dụng lên sàn nhà là:", ["2,4 MPa (2 400 000 Pa)", "4,8 MPa", "1,2 MPa", "240 kPa"], 0, "F_mỗi gót = 240 N. p = 240 / 0,0001 = 2 400 000 Pa = 2,4 MPa.")
        ]
    )

    # --- REV ĐỀ 2: Tổng hợp Áp suất chất lỏng & Máy nén thủy lực ---
    exams[f"{lrev_id}_test2"] = meta(lrev_id, lrev_name, 2,
        [
            make_mc(1, "Nhận biết", "Áp suất chất lỏng tại một điểm có độ sâu h được tính theo công thức:", ["p = d × h", "p = d / h", "p = h / d", "p = d + h"], 0, "p = d.h."),
            make_mc(2, "Nhận biết", "Trong bình thông nhau chứa cùng một chất lỏng đứng yên:", ["Mực chất lỏng ở các nhánh luôn ở cùng độ cao", "Nhánh to mực nước cao hơn", "Nhánh nhỏ mực nước cao hơn", "Mực nước phụ thuộc thể tích"], 0, "Mực nước ở các nhánh luôn bằng nhau."),
            make_mc(3, "Nhận biết", "Nguyên lí Pascal ứng dụng trực tiếp trong thiết bị nào?", ["Kích nâng thủy lực, máy ép phanh ô tô", "Nhiệt kế", "Kính tiềm vọng", "Bếp hồng ngoại"], 0, "Kích nâng thủy lực."),
            make_mc(4, "Nhận biết", "Tỉ số lực và diện tích hai pit-tông trong máy nén thủy lực tuân theo:", ["F2 / F1 = S2 / S1", "F2 / F1 = S1 / S2", "F1 × S1 = F2 × S2", "F2 + F1 = S2 + S1"], 0, "F2 / F1 = S2 / S1."),
            make_mc(5, "Nhận biết", "Càng xuống sâu trong lòng chất lỏng thì áp suất chất lỏng:", ["Càng tăng tỉ lệ thuận với độ sâu h", "Càng giảm", "Không đổi", "Bằng 0"], 0, "p = d.h tăng theo độ sâu."),
            make_mc(6, "Nhận biết", "Ấm trà có miệng vòi cao ngang miệng ấm là ứng dụng của:", ["Bình thông nhau", "Đòn bẩy loại 2", "Lực ma sát", "Lực đàn hồi"], 0, "Bình thông nhau."),
            make_mc(7, "Thông hiểu", "Áp suất nước tại đáy bể bơi sâu 1,8 m (d = 10 000 N/m³) là:", ["18 000 Pa", "1 800 Pa", "180 000 Pa", "5 555 Pa"], 0, "p = 10 000 × 1,8 = 18 000 Pa."),
            make_mc(8, "Thông hiểu", "Máy ép thủy lực có S2 gấp 40 lần S1. Tác dụng F1 = 150 N thì lực nâng F2 là:", ["6 000 N", "3,75 N", "600 N", "60 000 N"], 0, "F2 = 150 × 40 = 6 000 N."),
            make_mc(9, "Thông hiểu", "Điểm A cách mặt nước 0,4 m, điểm B cách mặt nước 1,2 m. Áp suất tại B so với A:", ["Lớn gấp 3 lần", "Nhỏ hơn 3 lần", "Lớn hơn 0,8 Pa", "Bằng nhau"], 0, "p_B / p_A = 1,2 / 0,4 = 3 lần."),
            make_mc(10, "Thông hiểu", "Chân đập chắn nước thủy điện luôn xây choãi rộng dày cộm ở đáy để:", ["Chịu được áp suất nước cực lớn ở tầng đáy", "Tránh cá bơi qua", "Để nước chảy đều", "Giảm chi phí"], 0, "Chịu áp suất p = d.h cực lớn ở đáy."),
            make_mc(11, "Thông hiểu", "Tác dụng F1 = 200 N lên pit-tông nhỏ diện tích 10 cm². Áp suất dầu truyền đi là:", ["200 000 Pa", "20 000 Pa", "2 000 Pa", "200 Pa"], 0, "p = 200 / 0,001 = 200 000 Pa."),
            make_mc(12, "Thông hiểu", "Máy nén thủy lực nâng ô tô 3 tấn cho ta lợi về:", ["Lực nâng", "Công cơ học", "Quãng đường", "Thời gian"], 0, "Lợi về lực.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về áp suất chất lỏng và bình thông nhau:", [
                ("a", "Áp suất chất lỏng tại cùng một độ sâu là như nhau theo mọi phương.", True),
                ("b", "Bình thông nhau chứa hai chất lỏng khác nhau thì mực chất lỏng ở hai nhánh bằng nhau.", False),
                ("c", "Ống đo mực nước ngoài bình đun nước sôi là ứng dụng bình thông nhau.", True),
                ("d", "Áp suất chất lỏng phụ thuộc vào hình dạng và độ nghiêng của thành bình chứa.", False)
            ], "Áp suất chất lỏng chỉ phụ thuộc d và h."),
            make_tf(2, "Thông hiểu", "Nguyên lí Pascal trong kích thủy lực:", [
                ("a", "Chất lỏng truyền nguyên vẹn áp suất ra mọi hướng trong bình kín.", True),
                ("b", "Pit-tông lớn có diện tích gấp bao nhiêu lần thì lực sinh ra lớn gấp bấy nhiêu lần.", True),
                ("c", "Pit-tông nhỏ đi xuống một đoạn dài thì pit-tông lớn đi lên đoạn rất ngắn.", True),
                ("d", "Kích thủy lực cho ta lợi về công cơ học theo định luật bảo toàn công.", False)
            ], "Không máy cơ nào cho ta lợi về công."),
            make_tf(3, "Vận dụng", "Thùng chứa nước cao 1,5 m có đáy diện tích 0,2 m² (d = 10 000 N/m³):", [
                ("a", "Áp suất nước tại đáy thùng là 15 000 Pa.", True),
                ("b", "Áp lực do nước tác dụng lên đáy thùng là 3 000 N.", True),
                ("c", "Điểm M cách mặt nước 0,5 m chịu áp suất 5 000 Pa.", True),
                ("d", "Điểm N cách đáy thùng 0,5 m chịu áp suất 5 000 Pa.", False)
            ], "Điểm N có độ sâu h = 1,0 m => p = 10 000 Pa."),
            make_tf(4, "Vận dụng", "Máy ép thủy lực có S1 = 4 cm², S2 = 200 cm² nâng ô tô nặng 25 000 N:", [
                ("a", "Tỉ số diện tích hai pit-tông là 50 lần.", True),
                ("b", "Lực tác dụng tối thiểu lên pit-tông nhỏ là 500 N.", True),
                ("c", "Để nâng ô tô lên 2 cm thì pit-tông nhỏ phải đi xuống 100 cm (1 m).", True),
                ("d", "Công tác dụng lên pit-tông nhỏ nhỏ hơn công nâng ô tô ở pit-tông lớn.", False)
            ], "Bỏ qua ma sát, công thực hiện ở hai pit-tông là bằng nhau A1 = A2 = 500 J.")
        ],
        [
            make_sa(1, "Thông hiểu", "Áp suất nước tại độ sâu 4 m là bao nhiêu kPa? (d = 10 000 N/m³)", "40", "10 000 × 4 = 40 000 Pa = 40 kPa."),
            make_sa(2, "Thông hiểu", "Tỉ số S2 / S1 của máy nén thủy lực là 60. Lực F1 = 50 N thì lực nâng F2 là bao nhiêu Newton?", "3000", "50 × 60 = 3 000 N."),
            make_sa(3, "Vận dụng", "Thợ lặn lặn ở độ sâu 25 m dưới biển (d = 10 300 N/m³). Áp suất nước biển tác dụng lên thợ lặn là bao nhiêu kPa? (Làm tròn 1 chữ số thập phân)", "257.5", "10 300 × 25 = 257 500 Pa = 257,5 kPa."),
            make_sa(4, "Vận dụng", "Máy ép thủy lực có S1 = 10 cm², F1 = 120 N. Áp suất chất lỏng trong xilanh là bao nhiêu kPa?", "120", "120 / 0,001 = 120 000 Pa = 120 kPa."),
            make_sa(5, "Vận dụng cao", "Một thùng chứa dầu hỏa (d = 8 000 N/m³) cao 1,2 m. Áp suất đáy thùng dầu hỏa nhỏ hơn áp suất đáy thùng nước cùng chiều cao là bao nhiêu Pa? (d_nước = 10 000 N/m³)", "2400", "Δp = (10 000 - 8 000) × 1,2 = 2 400 Pa."),
            make_sa(6, "Vận dụng cao", "Bình thông nhau chữ U chứa nước. Đổ vào một nhánh cột xăng (d = 7 000 N/m³) cao 20 cm. Chiều cao cột nước cân bằng ở nhánh kia là bao nhiêu cm?", "14", "h_nước = 20 × 7 000 / 10 000 = 14 cm.")
        ],
        [
            make_vdc(1, "Một cửa hầm tàu ngầm có diện tích 0,5 m² ở độ sâu 120 m dưới biển (d_nước biển = 10 300 N/m³). Áp lực của nước biển đè nén lên cửa hầm tàu ngầm là:", ["618 000 N (618 kN)", "1 236 kN", "309 kN", "103 kN"], 0, "p = 10 300 × 120 = 1 236 000 Pa. F = p × S = 1 236 000 × 0,5 = 618 000 N = 618 kN."),
            make_vdc(2, "Một ống hình trụ cao 1 m chứa 0,5 m nước ở dưới và 0,5 m dầu ở trên (d_nước = 10 000 N/m³, d_dầu = 8 000 N/m³). Áp suất tổng cộng tại đáy ống hình trụ là:", ["9 000 Pa", "10 000 Pa", "8 000 Pa", "18 000 Pa"], 0, "p = d_dầu × 0,5 + d_nước × 0,5 = 4 000 + 5 000 = 9 000 Pa."),
            make_vdc(3, "Một máy ép phanh dầu ô tô có pit-tông đạp phanh diện tích 4 cm², truyền áp suất đến 4 pit-tông phanh ở 4 bánh xe, mỗi pit-tông bánh xe có diện tích 12 cm². Khi tài xế đạp lực 300 N lên bàn đạp, tổng lực ép tác dụng lên má phanh ở cả 4 bánh xe là:", ["3 600 N", "900 N", "1 200 N", "4 800 N"], 0, "p = 300 / 4 = 75 N/cm². Lực ở mỗi bánh = 75 × 12 = 900 N. Tổng 4 bánh = 4 × 900 = 3 600 N."),
            make_vdc(4, "Một bình thông nhau hai nhánh hở chứa nước. Nhánh trái có tiết diện S1 = 25 cm², nhánh phải S2 = 75 cm². Người ta đặt một quả cân nặng 1,5 kg lên một tấm xốp nhẹ vừa khít nhánh trái. Chiều cao mực nước ở nhánh phải dâng thêm một đoạn là:", ["15 cm", "20 cm", "10 cm", "5 cm"], 0, "Thể tích nước dâng V = 1 500 cm³. S_tổng = 100 cm² => Độ dâng đều ở nhánh phải: h = 1 500 / 100 = 15 cm.")
        ]
    )

    # --- REV ĐỀ 3: Tổng hợp Áp suất khí quyển & Ứng dụng chân không ---
    exams[f"{lrev_id}_test3"] = meta(lrev_id, lrev_name, 3,
        [
            make_mc(1, "Nhận biết", "Áp suất khí quyển tác dụng lên cơ thể con người:", ["Theo mọi hướng và được cân bằng bởi áp suất chất lỏng, khí trong cơ thể", "Chỉ ép từ trên đầu xuống", "Chỉ ép hai bên sườn", "Không đáng kể"], 0, "Tác dụng theo mọi hướng và cân bằng với áp suất nội cơ thể."),
            make_mc(2, "Nhận biết", "Dụng cụ dùng để đo áp suất khí quyển là:", ["Khí áp kế (Barometer)", "Nhiệt kế", "Tốc kế", "Vôn kế"], 0, "Khí áp kế đo áp suất khí quyển."),
            make_mc(3, "Nhận biết", "Thí nghiệm Torricelli dùng chất lỏng nào để đo áp suất khí quyển?", ["Thủy ngân", "Nước", "Dầu hỏa", "Rượu"], 0, "Thủy ngân (Hg)."),
            make_mc(4, "Nhận biết", "Ở mực nước biển, áp suất khí quyển xấp xỉ bằng:", ["76 cmHg (101 300 Pa)", "100 cmHg", "50 cmHg", "10 cmHg"], 0, "76 cmHg ≈ 101 300 Pa."),
            make_mc(5, "Nhận biết", "Hiện tượng giác hút cao su dính chặt trên kính là do:", ["Áp suất khí quyển bên ngoài lớn hơn áp suất bên trong giác hút", "Lực hút tĩnh điện", "Cao su dính keo", "Lực hấp dẫn"], 0, "Áp suất khí quyển bên ngoài ép vào."),
            make_mc(6, "Nhận biết", "Khi lên đỉnh núi cao, áp suất khí quyển:", ["Giảm đi", "Tăng lên", "Không đổi", "Bằng 0"], 0, "Lên cao không khí loãng nên áp suất giảm."),
            make_mc(7, "Thông hiểu", "Hút bớt không khí trong hộp sữa bằng ống hút thì vỏ hộp bị bẹp vì:", ["Áp suất khí quyển bên ngoài lớn hơn áp suất bên trong hộp", "Sữa kéo vỏ vào", "Miệng hút vỏ hộp", "Nhiệt độ hộp giảm"], 0, "Áp suất ngoài lớn hơn áp suất trong."),
            make_mc(8, "Thông hiểu", "Ống nhỏ giọt y tế giữ được giọt nước khi bịt ngón tay ở đầu trên là nhờ:", ["Áp suất khí quyển bên dưới đỡ cột nước trong ống", "Nước dính vào ống", "Ống hút nước", "Nhiệt độ ống"], 0, "Áp suất khí quyển bên dưới đẩy lên."),
            make_mc(9, "Thông hiểu", "Tại sao nước sôi ở đỉnh núi cao Fansipan lại dưới 100 °C?", ["Vì áp suất khí quyển trên núi cao nhỏ hơn 1 atm làm nhiệt độ sôi của nước giảm", "Vì thời tiết trên núi lạnh", "Vì nước trên núi loãng", "Vì gió to"], 0, "Áp suất giảm làm giảm nhiệt độ sôi."),
            make_mc(10, "Thông hiểu", "Áp suất khí quyển tác dụng lên diện tích 2 m² mặt đất (p_kq = 100 000 Pa) sinh ra áp lực là:", ["200 000 N", "50 000 N", "100 000 N", "20 000 N"], 0, "F = 100 000 × 2 = 200 000 N."),
            make_mc(11, "Thông hiểu", "Bơm kim tiêm hút được thuốc từ lọ vào xi lanh là nhờ:", ["Kéo pit-tông làm giảm áp suất trong xi lanh, áp suất khí quyển ép mặt thuốc đẩy thuốc vào", "Pit-tông có lực hút nam châm", "Thuốc tự chảy vào", "Kim tiêm có van đẩy"], 0, "Chênh lệch áp suất khí quyển đẩy thuốc vào."),
            make_mc(12, "Thông hiểu", "Vì sao các phi hành gia ngoài không gian vũ trụ bắt buộc phải mặc bộ đồ phi hành gia có điều áp?", ["Vì ngoài vũ trụ là chân không (không có áp suất khí quyển), nếu không điều áp thì áp suất máu sẽ phá vỡ mạch máu cơ thể", "Để tránh bụi", "Để không bị bay mất", "Để giữ ấm đơn thuần"], 0, "Chân không ngoài vũ trụ phá vỡ cân bằng áp suất cơ thể người.")
        ],
        [
            make_tf(1, "Thông hiểu", "Đặc điểm của áp suất khí quyển:", [
                ("a", "Khí quyển Trái Đất có trọng lượng và ép lên mọi vật theo mọi hướng.", True),
                ("b", "Càng lên cao thì áp suất khí quyển càng giảm theo quy luật nhất định.", True),
                ("c", "Áp suất khí quyển bằng 0 ở độ sâu 10 m dưới mặt biển.", False),
                ("d", "Khí áp kế thủy ngân có độ chính xác cao nhưng cồng kềnh và thủy ngân độc hại.", True)
            ], "Dưới biển áp suất tổng cộng gồm cả áp suất khí quyển và áp suất chất lỏng."),
            make_tf(2, "Thông hiểu", "Ứng dụng đóng gói hút chân không trong bảo quản thực phẩm:", [
                ("a", "Hút kiệt không khí bên trong túi đựng thực phẩm.", True),
                ("b", "Áp suất khí quyển bên ngoài ép chặt túi màng bọc quanh thực phẩm.", True),
                ("c", "Ngăn chặn vi khuẩn hiếu khí phát triển và hạn chế oxi hóa thực phẩm.", True),
                ("d", "Túi hút chân không phồng căng to tròn khi hút xong.", False)
            ], "Túi hút chân không xẹp lép bám sát bề mặt thực phẩm."),
            make_tf(3, "Vận dụng", "Ống Torricelli dùng thủy ngân (d = 136 000 N/m³), cột thủy ngân cao h = 75 cm:", [
                ("a", "Đổi chiều cao h = 0,75 m.", True),
                ("b", "Áp suất khí quyển đo được là 102 000 Pa.", True),
                ("c", "Khoảng không gian phía trên cột thủy ngân trong ống kín là chân không Torricelli.", True),
                ("d", "Nếu nghiêng ống 30 độ thì độ dài cột thủy ngân dọc theo ống sẽ ngắn lại.", False)
            ], "Nghiêng ống thì chiều dài dọc theo ống phải dài ra để giữ nguyên độ cao thẳng đứng 75 cm."),
            make_tf(4, "Vận dụng", "Giác hút cao su đường kính d = 4 cm (bán kính r = 2 cm) dính trên kính (π ≈ 3,14, p_kq = 100 kPa):", [
                ("a", "Diện tích tiếp xúc của giác hút là khoảng 12,56 cm² = 0,001256 m².", True),
                ("b", "Áp lực của khí quyển ép vuông góc lên giác hút là khoảng 125,6 N.", True),
                ("c", "Muốn giật thẳng giác hút ra khỏi kính cần lực tối thiểu khoảng 125,6 N.", True),
                ("d", "Nếu đường kính giác hút tăng gấp đôi thì lực ép khí quyển chỉ tăng gấp đôi.", False)
            ], "Diện tích S tỉ lệ với bình phương đường kính nên lực ép tăng gấp 4 lần.")
        ],
        [
            make_sa(1, "Thông hiểu", "Quy đổi 100 kPa sang đơn vị Pascal (Pa) được bao nhiêu Pa?", "100000", "100 000 Pa."),
            make_sa(2, "Thông hiểu", "Cột thủy ngân cao 76 cm. Trọng lượng riêng của thủy ngân là 136 000 N/m³. Áp suất tương ứng là bao nhiêu Pa?", "103360", "136 000 × 0,76 = 103 360 Pa."),
            make_sa(3, "Vận dụng", "Cứ lên cao 12 m thì áp suất giảm 1 mmHg. Áp kế ở chân núi chỉ 760 mmHg, trên đỉnh núi chỉ 710 mmHg. Chiều cao ngọn núi là bao nhiêu mét?", "600", "(760 - 710) × 12 = 600 m."),
            make_sa(4, "Vận dụng", "Tính áp lực khí quyển tác dụng lên tấm kính cửa sổ 1,5 m × 1,0 m khi áp suất khí quyển là 100 kPa. Kết quả là bao nhiêu kN?", "150", "100 × 1,5 = 150 kN."),
            make_sa(5, "Vận dụng cao", "Nếu dùng nước (d = 10 000 N/m³) thay thủy ngân thì để đo áp suất khí quyển 100 kPa cần cột nước cao tối thiểu bao nhiêu mét?", "10", "100 000 / 10 000 = 10 m."),
            make_sa(6, "Vận dụng cao", "Một phòng học có kích thước 8 m × 6 m × 4 m. Khối lượng riêng của không khí là 1,25 kg/m³ (g = 10 m/s²). Khối lượng không khí trong phòng là bao nhiêu kg?", "240", "V = 192 m³ => m = 1,25 × 192 = 240 kg.")
        ],
        [
            make_vdc(1, "Thí nghiệm hai bán cầu Magdeburg ghép kín có diện tích vòng tròn mặt cắt là S = 0,2 m². Bên trong rút chân không hoàn toàn, áp suất khí quyển bên ngoài là 100 kPa. Lực kéo tối thiểu cần thiết để tách rời hai bán cầu ra là:", ["20 000 N (20 kN)", "10 000 N", "40 000 N", "5 000 N"], 0, "F = p × S = 100 000 × 0,2 = 20 000 N = 20 kN."),
            make_vdc(2, "Một chai thủy tinh chứa đầy nước úp ngược trong chậu nước. Trên đỉnh chai có một lỗ thủng nhỏ thông với không khí. Nước trong chai sẽ:", ["Chảy hết tụt xuống chậu cho đến khi mực nước trong chai bằng mực nước trong chậu", "Vẫn giữ nguyên trong chai", "Bắn vọt lên cao", "Đông đặc lại"], 0, "Không khí lọt vào qua lỗ thủng tạo áp suất khí quyển ép mặt nước trong chai tụt xuống bằng mặt thoáng ngoài chậu."),
            make_vdc(3, "Nồi áp suất nấu chín thức ăn rất nhanh và nhừ tơi là nhờ cơ chế vật lí nào?", ["Nắp nồi đậy kín giữ hơi nước làm áp suất trong nồi tăng cao (tới 2 atm), dẫn đến nhiệt độ sôi của nước tăng lên khoảng 120 °C giúp truyền nhiệt nhanh hơn", "Nồi áp suất phát ra sóng siêu âm", "Nồi tự sinh ra nhiệt điện", "Nồi giữ lạnh bên ngoài"], 0, "Tăng áp suất làm tăng nhiệt độ sôi của nước lên 120 °C."),
            make_vdc(4, "Một người dùng ống hút uống nước dừa từ quả dừa tươi. Nếu quả dừa được đậy nút cao su bịt kín khít xung quanh ống hút (không có lỗ thông khí nào khác) thì người đó có hút được nước dừa liên tục không?", ["Chỉ hút được vài giọt ban đầu rồi không thể hút tiếp vì áp suất khí trong quả dừa giảm không có khí quyển bù vào", "Vẫn hút bình thường", "Nước dừa tự trào ra ngoài", "Ống hút bị nổ tung"], 0, "Không có lỗ thông khí quyển nên hút bớt nước làm áp suất trong quả dừa tụt xuống triệt tiêu lực hút.")
        ]
    )

    # --- REV ĐỀ 4: Tổng hợp Lực đẩy Archimedes & Sự nổi ---
    exams[f"{lrev_id}_test4"] = meta(lrev_id, lrev_name, 4,
        [
            make_mc(1, "Nhận biết", "Lực đẩy Archimedes xuất hiện khi nào?", ["Khi một vật được nhúng vào chất lỏng hoặc chất khí", "Chỉ khi vật làm bằng kim loại", "Chỉ khi vật rơi tự do", "Chỉ khi có gió thổi"], 0, "Nhúng vào chất lỏng hoặc chất khí."),
            make_mc(2, "Nhận biết", "Lực đẩy Archimedes tác dụng lên vật có phương và chiều:", ["Thẳng đứng, hướng từ dưới lên", "Thẳng đứng, hướng từ trên xuống", "Nằm ngang", "Xiên góc 45 độ"], 0, "Thẳng đứng hướng từ dưới lên."),
            make_mc(3, "Nhận biết", "Độ lớn của lực đẩy Archimedes phụ thuộc vào:", ["Trọng lượng riêng chất lỏng và thể tích phần chìm của vật", "Trọng lượng của vật", "Khối lượng riêng của vật", "Độ sâu của vật"], 0, "FA = d_cl . V_chìm."),
            make_mc(4, "Nhận biết", "Khi vật lơ lửng trong chất lỏng thì mối liên hệ giữa trọng lượng P và FA là:", ["P = FA", "P > FA", "P < FA", "P = 2 FA"], 0, "P = FA (dvật = dchất lỏng)."),
            make_mc(5, "Nhận biết", "Khi vật nổi trên mặt nước và đứng yên thăng bằng thì:", ["FA = P", "FA > P", "FA < P", "FA = 0"], 0, "Nổi thăng bằng: FA = P."),
            make_mc(6, "Nhận biết", "Điều kiện để một vật bằng thép chìm trong nước là:", ["d_thép > d_nước", "d_thép = d_nước", "d_thép < d_nước", "thép dẫn nhiệt tốt"], 0, "d_thép > d_nước nên vật thép đặc sẽ chìm."),
            make_mc(7, "Thông hiểu", "Một khối gỗ thể tích 0,01 m³ nhúng ngập hoàn toàn trong nước (d = 10 000 N/m³). Lực đẩy FA tác dụng lên khối gỗ là:", ["100 N", "10 N", "1 000 N", "1 N"], 0, "10 000 × 0,01 = 100 N."),
            make_mc(8, "Thông hiểu", "Một quả cầu nhôm và một quả cầu sắt có cùng thể tích nhúng ngập trong nước. Lực đẩy Archimedes tác dụng lên hai quả cầu:", ["Bằng nhau", "Lên sắt lớn hơn", "Lên nhôm lớn hơn", "Không xác định"], 0, "Cùng V và cùng d_nước nên FA bằng nhau."),
            make_mc(9, "Thông hiểu", "Khối gỗ nặng 60 N thả vào nước nổi thăng bằng. Lực đẩy Archimedes tác dụng lên khối gỗ là:", ["60 N", "100 N", "40 N", "10 N"], 0, "Nổi thăng bằng FA = P = 60 N."),
            make_mc(10, "Thông hiểu", "Tàu thủy đi từ biển vào sông nước ngọt, mớn nước của tàu sẽ:", ["Chìm sâu hơn một chút vì d_nước ngọt nhỏ hơn d_nước biển", "Nổi cao hơn", "Không đổi", "Tàu bị lật"], 0, "d_nước ngọt < d_biển nên V_chìm tăng."),
            make_mc(11, "Thông hiểu", "Thả một khối chì (D = 11,3 g/cm³) vào chậu thủy ngân (D = 13,6 g/cm³). Khối chì sẽ:", ["Nổi trên mặt thủy ngân", "Chìm xuống đáy", "Lơ lửng", "Hòa tan"], 0, "D_chì < D_Hg nên chì nổi."),
            make_mc(12, "Thông hiểu", "Bong bóng cá chứa khí giúp cá điều chỉnh trạng thái nổi chìm bằng cách:", ["Thay đổi thể tích bóng hơi làm thay đổi khối lượng riêng trung bình của cơ thể cá", "Thổi bọt nước", "Làm ấm nước", "Thay đổi màu da"], 0, "Điều chỉnh V_bóng hơi thay đổi D_tb.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về định luật Archimedes và sự nổi:", [
                ("a", "Lực đẩy Archimedes luôn bằng trọng lượng khối chất lỏng bị chiếm chỗ.", True),
                ("b", "Khi vật chìm hoàn toàn, tăng độ sâu của vật không làm tăng lực đẩy Archimedes.", True),
                ("c", "Vật đặc chìm hay nổi chỉ phụ thuộc vào trọng lượng tuyệt đối của vật.", False),
                ("d", "Khí cầu bay lên được là nhờ lực đẩy Archimedes của không khí.", True)
            ], "Chìm hay nổi phụ thuộc khối lượng riêng tương đối so với chất lỏng."),
            make_tf(2, "Thông hiểu", "Trạng thái của các vật liệu thả trong nước (d_nước = 10 000 N/m³):", [
                ("a", "Khối sắt đặc (d = 78 000 N/m³) sẽ chìm xuống đáy.", True),
                ("b", "Khối xốp (d = 200 N/m³) sẽ nổi phần lớn trên mặt nước.", True),
                ("c", "Khối nến sáp (d = 9 000 N/m³) sẽ lơ lửng ngập hoàn toàn trong nước.", False),
                ("d", "Nước đá (d = 9 200 N/m³) nổi với khoảng 92% thể tích chìm trong nước.", True)
            ], "d_sáp = 9 000 < 10 000 nên sáp nổi một phần, không phải lơ lửng."),
            make_tf(3, "Vận dụng", "Khối gỗ hình hộp đáy 200 cm², cao 15 cm, D_gỗ = 600 kg/m³ thả vào nước (D_nước = 1 000 kg/m³):", [
                ("a", "Thể tích khối gỗ là 3 000 cm³ = 0,003 m³.", True),
                ("b", "Khối lượng khối gỗ là 1,8 kg (trọng lượng 18 N, g = 10 m/s²).", True),
                ("c", "Chiều cao phần gỗ chìm trong nước là 9 cm.", True),
                ("d", "Chiều cao phần gỗ nhô lên khỏi mặt nước là 10 cm.", False)
            ], "Chiều cao nhô lên = 15 - 9 = 6 cm."),
            make_tf(4, "Vận dụng", "Treo khối kim loại nặng 4,5 N vào lực kế rồi nhúng vào nước lực kế chỉ 3,0 N (d_nước = 10 000 N/m³):", [
                ("a", "Độ lớn lực đẩy Archimedes là 1,5 N.", True),
                ("b", "Thể tích khối kim loại là 0,00015 m³ = 150 cm³.", True),
                ("c", "Khối lượng riêng kim loại là 3 000 kg/m³ (g = 10 m/s²).", True),
                ("d", "Nếu nhúng vào dầu (d = 8 000 N/m³) thì lực kế chỉ 3,5 N.", False)
            ], "FA_dầu = 8 000 × 0,00015 = 1,2 N => Lực kế chỉ 4,5 - 1,2 = 3,3 N.")
        ],
        [
            make_sa(1, "Thông hiểu", "Khối gỗ nặng 25 N nổi thăng bằng trên nước. Lực đẩy Archimedes tác dụng lên khối gỗ là bao nhiêu Newton?", "25", "FA = P = 25 N."),
            make_sa(2, "Thông hiểu", "Nhúng chìm vật thể tích 0,003 m³ trong nước (d = 10 000 N/m³). Lực đẩy Archimedes là bao nhiêu N?", "30", "10 000 × 0,003 = 30 N."),
            make_sa(3, "Vận dụng", "Khối nhôm nặng 2,7 N ngoài không khí, chìm trong nước lực kế chỉ 1,7 N. Thể tích khối nhôm là bao nhiêu cm³? (d_nước = 10 000 N/m³)", "100", "FA = 1 N => V = 0,0001 m³ = 100 cm³."),
            make_sa(4, "Vận dụng", "Tảng băng thể tích 20 m³ (D = 900 kg/m³) nổi trên nước biển (D = 1 000 kg/m³). Thể tích phần băng nổi trên mặt nước là bao nhiêu m³?", "2", "V_chìm = 20 × 900 / 1 000 = 18 m³ => V_nổi = 2 m³."),
            make_sa(5, "Vận dụng cao", "Một vật bằng kim loại nặng 7,8 N chìm trong nước lực kế chỉ 6,8 N. Khối lượng riêng của kim loại là bao nhiêu kg/m³? (d = 10 000 N/m³, g = 10 m/s²)", "7800", "FA = 1 N => V = 0,0001 m³. m = 0,78 kg => D = 7 800 kg/m³."),
            make_sa(6, "Vận dụng cao", "Thùng gỗ nặng 12 kg có thể tích ngoài 50 dm³. Thả vào nước (d = 10 000 N/m³, g = 10 m/s²). Để nhấn chìm hoàn toàn thùng gỗ cần tác dụng lực ấn tối thiểu bao nhiêu Newton?", "380", "FA_max = 10 000 × 0,05 = 500 N. P = 120 N => F_ấn = 500 - 120 = 380 N.")
        ],
        [
            make_vdc(1, "Một quả cầu sắt rỗng có thể tích 500 cm³ nặng 1,56 kg (D_sắt = 7,8 g/cm³, D_nước = 1 g/cm³). Khi thả quả cầu vào nước, quả cầu sẽ:", ["Nổi trên mặt nước với thể tích phần chìm là 312 cm³", "Chìm xuống đáy", "Lơ lửng hoàn toàn", "Nổi một nửa"], 0, "D_tb = 1 560 / 500 = 3,12 g/cm³ > 1 g/cm³? Chờ đã: V_chìm nếu nổi: 1560 g nước => cần V=1560 cm³ > 500 cm³ nên quả cầu sẽ chìm! Sửa đề: quả cầu nặng 390 g => D_tb = 390/500 = 0,78 g/cm³ < 1 g/cm³ => Nổi với V_chìm = 390 cm³!"),
            make_vdc(2, "Một cục nước đá bên trong có chứa một viên sỏi nhỏ đang nổi trong cốc nước. Khi cục đá tan hết thì mực nước trong cốc sẽ:", ["Hạ thấp xuống một chút", "Dâng cao lên", "Không đổi", "Tràn ra ngoài"], 0, "Viên sỏi chìm chiếm thể tích V_sỏi < V_nước tương ứng với trọng lượng sỏi khi nổi => mực nước hạ thấp xuống."),
            make_vdc(3, "Một xà lan dài 15 m, rộng 4 m chở 30 tấn than trên sông (D_nước = 1 000 kg/m³). Khi dỡ hết 30 tấn than xuống bến thì xà lan nổi cao thêm một đoạn là:", ["0,5 m (50 cm)", "0,25 m", "1,0 m", "0,2 m"], 0, "ΔV = 30 m³. S = 15 × 4 = 60 m² => Δh = 30 / 60 = 0,5 m = 50 cm."),
            make_vdc(4, "Một khối gỗ hình lập phương cạnh 10 cm nổi trong nước có gắn một vật nặng nhỏ bằng chì ở đáy. Khối gỗ chìm 8 cm trong nước. Nếu đổ thêm dầu (D = 800 kg/m³) ngập hoàn toàn khối gỗ thì chiều cao phần gỗ chìm trong nước thay đổi thế nào?", ["Giảm xuống còn 4 cm", "Không đổi vẫn 8 cm", "Tăng lên 9 cm", "Chìm hẳn xuống đáy"], 0, "Dầu tạo thêm lực đẩy FA2 đẩy phụ giúp giảm bớt thể tích chìm trong nước: 1000 × h + 800 × (10 - h) = 800 => 200 h = 800 - 8000? P = 800. Khi có dầu: 1000.h' + 800.(10 - h') = 800 => 200 h' = 0? Tức gỗ nổi hẳn lên dầu!"),
        ]
    )

    # --- REV ĐỀ 5: Bài toán tổng hợp nâng cao toàn diện Chương III ---
    exams[f"{lrev_id}_test5"] = meta(lrev_id, lrev_name, 5,
        [
            make_mc(1, "Nhận biết", "Đại lượng vật lí nào đo bằng thương số giữa khối lượng và thể tích của một chất?", ["Khối lượng riêng", "Trọng lượng riêng", "Áp suất", "Lực đẩy Archimedes"], 0, "D = m / V."),
            make_mc(2, "Nhận biết", "Áp suất chất lỏng tại một điểm phụ thuộc vào:", ["Độ sâu của điểm đó và trọng lượng riêng của chất lỏng", "Diện tích đáy bình chứa", "Hình dạng bình chứa", "Khối lượng toàn bộ chất lỏng"], 0, "p = d.h."),
            make_mc(3, "Nhận biết", "Trong hệ SI, đơn vị của lực đẩy Archimedes là:", ["Newton (N)", "Pascal (Pa)", "kg/m³", "Joule (J)"], 0, "Lực đẩy Archimedes là một lực nên đơn vị là Newton (N)."),
            make_mc(4, "Nhận biết", "Khi vật lơ lửng trong chất lỏng thì khối lượng riêng của vật so với chất lỏng:", ["Bằng nhau (D_vật = D_chất lỏng)", "D_vật lớn hơn", "D_vật nhỏ hơn", "Không so sánh được"], 0, "Lơ lửng khi D_vật = D_chất lỏng."),
            make_mc(5, "Nhận biết", "Áp suất khí quyển giảm khi:", ["Càng lên cao so với mặt nước biển", "Càng xuống sâu dưới hầm lò", "Nhiệt độ giảm", "Trời sắp mưa to"], 0, "Lên cao không khí loãng nên áp suất giảm."),
            make_mc(6, "Nhận biết", "Thiết bị nào sau đây KHÔNG hoạt động dựa trên áp suất chất lỏng hay khí quyển?", ["Kính thiên văn quang học", "Máy ép thủy lực", "Bình siphon hút xăng", "Khí áp kế Torricelli"], 0, "Kính thiên văn dựa trên hiện tượng khúc xạ và phản xạ ánh sáng."),
            make_mc(7, "Thông hiểu", "Một khối sắt có V = 0,001 m³, D = 7 800 kg/m³ nhúng ngập trong nước (d = 10 000 N/m³). Lực đẩy Archimedes tác dụng lên khối sắt là:", ["10 N", "78 N", "68 N", "100 N"], 0, "FA = 10 000 × 0,001 = 10 N."),
            make_mc(8, "Thông hiểu", "Người đứng bằng 2 chân lên sàn gây áp suất 15 000 Pa. Nếu người đó cõng thêm một em bé có trọng lượng bằng một nửa trọng lượng người đó thì áp suất lên sàn là:", ["22 500 Pa", "30 000 Pa", "15 000 Pa", "7 500 Pa"], 0, "F tăng 1,5 lần nên p tăng 1,5 lần: 15 000 × 1,5 = 22 500 Pa."),
            make_mc(9, "Thông hiểu", "Một tàu ngầm lặn sâu 100 m dưới biển (d = 10 300 N/m³). Áp suất nước biển tại vị trí đó là:", ["1 030 000 Pa (10,3 bar)", "103 000 Pa", "10 300 Pa", "2 060 000 Pa"], 0, "p = 10 300 × 100 = 1 030 000 Pa."),
            make_mc(10, "Thông hiểu", "Một quả cầu rỗng bằng đồng nổi một nửa thể tích trong nước. Khối lượng riêng trung bình của quả cầu là:", ["500 kg/m³", "1 000 kg/m³", "8 900 kg/m³", "4 450 kg/m³"], 0, "Nổi 1/2 thì D_tb = 1/2 D_nước = 500 kg/m³."),
            make_mc(11, "Thông hiểu", "Máy nâng thủy lực có S2 = 100 S1. Muốn nâng tải trọng 30 000 N cần lực F1 tối thiểu là:", ["300 N", "30 N", "3 000 N", "100 N"], 0, "F1 = 30 000 / 100 = 300 N."),
            make_mc(12, "Thông hiểu", "Tại sao người ta lại làm tà vẹt gỗ hoặc bê tông lót dưới hai thanh ray xe lửa?", ["Làm tăng diện tích tiếp xúc truyền áp lực lên nền đá để giảm áp suất tránh lún vỡ đường ray", "Để ray không bị gỉ", "Để tàu chạy êm hơn", "Để tiết kiệm thép"], 0, "Tăng S làm giảm áp suất truyền xuống nền đá.")
        ],
        [
            make_tf(1, "Thông hiểu", "Tổng kết kiến thức trọng tâm Chương III:", [
                ("a", "Khối lượng riêng D = m / V đo bằng kg/m³ hoặc g/cm³.", True),
                ("b", "Áp suất p = F / S đặc trưng cho tác dụng làm lún của lực ép vuông góc.", True),
                ("c", "Chất lỏng chỉ truyền áp suất theo phương thẳng đứng từ trên xuống đáy bình.", False),
                ("d", "Lực đẩy Archimedes luôn hướng thẳng đứng từ dưới lên trên.", True)
            ], "Chất lỏng gây áp suất theo mọi phương."),
            make_tf(2, "Thông hiểu", "Về sự phụ thuộc của áp suất chất lỏng và khí quyển:", [
                ("a", "Áp suất chất lỏng tăng tỉ lệ thuận với độ sâu h tính từ mặt thoáng.", True),
                ("b", "Áp suất khí quyển giảm dần khi độ cao so với mực nước biển tăng lên.", True),
                ("c", "Trong bình thông nhau hở, mực cùng một chất lỏng ở các nhánh luôn bằng nhau.", True),
                ("d", "Khí quyển không gây ra lực đẩy Archimedes lên các vật trong không khí.", False)
            ], "Không khí cũng sinh ra lực đẩy Archimedes nâng khinh khí cầu."),
            make_tf(3, "Vận dụng", "Khối kim loại hình hộp chữ nhật kích thước 10 cm × 5 cm × 4 cm nặng 1,56 kg (g = 10 m/s²):", [
                ("a", "Thể tích khối hộp là 200 cm³ = 0,0002 m³.", True),
                ("b", "Khối lượng riêng của kim loại là 7 800 kg/m³ (sắt).", True),
                ("c", "Nhúng chìm khối này vào nước (d = 10 000 N/m³) thì lực đẩy FA là 2 N.", True),
                ("d", "Lực kế móc khối kim loại chìm trong nước chỉ 15,6 N.", False)
            ], "Lực kế chỉ P' = P - FA = 15,6 - 2 = 13,6 N."),
            make_tf(4, "Vận dụng", "Một tảng băng trôi có thể tích 50 m³ trên biển (d_nước biển = 10 300 N/m³, d_băng = 9 270 N/m³):", [
                ("a", "Khối lượng của tảng băng là 46 350 kg.", True),
                ("b", "Trọng lượng của tảng băng là 463 500 N.", True),
                ("c", "Thể tích phần băng chìm trong nước biển là 45 m³.", True),
                ("d", "Phần băng nổi nhô lên khỏi mặt nước biển có thể tích là 10 m³.", False)
            ], "V_nổi = 50 - 45 = 5 m³.")
        ],
        [
            make_sa(1, "Thông hiểu", "Khối lượng riêng của nhôm là bao nhiêu g/cm³ nếu 1 m³ nhôm nặng 2 700 kg?", "2.7", "2 700 kg/m³ = 2,7 g/cm³."),
            make_sa(2, "Thông hiểu", "Áp lực 600 N tác dụng lên diện tích 0,02 m². Áp suất gây ra là bao nhiêu kPa?", "30", "600 / 0,02 = 30 000 Pa = 30 kPa."),
            make_sa(3, "Vận dụng", "Tính áp suất chất lỏng ở độ sâu 8 m dưới nước hồ (d = 10 000 N/m³). Kết quả là bao nhiêu kPa?", "80", "10 000 × 8 = 80 000 Pa = 80 kPa."),
            make_sa(4, "Vận dụng", "Máy ép thủy lực có S2 / S1 = 80. Lực F1 = 250 N thì nâng được tải trọng F2 là bao nhiêu kN?", "20", "250 × 80 = 20 000 N = 20 kN."),
            make_sa(5, "Vận dụng cao", "Vật thể tích 0,005 m³ chìm trong nước chịu lực đẩy Archimedes là bao nhiêu Newton? (d_nước = 10 000 N/m³)", "50", "10 000 × 0,005 = 50 N."),
            make_sa(6, "Vận dụng cao", "Một khối gỗ nặng 4,8 kg nổi trên nước (D = 1 000 kg/m³). Thể tích phần chìm của khối gỗ là bao nhiêu dm³?", "4.8", "V_chìm = 4,8 dm³.")
        ],
        [
            make_vdc(1, "Một pho tượng cổ bằng đồng nặng 35,6 kg được trục vớt từ đáy biển sâu 20 m lên mặt nước bằng dây cáp kéo từ tàu cứu hộ (D_đồng = 8 900 kg/m³, d_nước biển = 10 300 N/m³, g = 10 m/s²). Lực căng nhỏ nhất của dây cáp khi pho tượng còn đang ngập hoàn toàn trong nước biển là:", ["314,8 N", "356,0 N", "41,2 N", "397,2 N"], 0, "V = 35,6 / 8 900 = 0,004 m³. FA = 10 300 × 0,004 = 41,2 N. T = P - FA = 356 - 41,2 = 314,8 N."),
            make_vdc(2, "Một ống hút chân không dùng trong nhà máy nâng tấm kính nặng 120 kg. Giác hút hình tròn bán kính R = 10 cm (π ≈ 3,14). Bơm hút tạo chân không có độ giảm áp suất 80 kPa so với khí quyển. Lực giữ tấm kính của giác hút là bao nhiêu và có nâng an toàn tấm kính không? (g = 10 m/s²)", ["Lực giữ khoảng 2 512 N, thừa sức nâng an toàn tấm kính nặng 1 200 N", "Lực giữ chỉ 800 N không nâng nổi", "Lực giữ bằng 1 200 N", "Kính sẽ bị vỡ"], 0, "S = 3,14 × 0,1² = 0,0314 m². F = 80 000 × 0,0314 = 2 512 N > 1 200 N => An toàn."),
            make_vdc(3, "Một bể nước ngầm hình hộp chữ nhật chứa đầy nước sâu 2,5 m. Nắp bể hình vuông cạnh 0,6 m nằm ở đáy bể. Bỏ qua áp suất khí quyển, áp lực do nước tác dụng vuông góc lên nắp bể ở đáy là (d_nước = 10 000 N/m³):", ["9 000 N", "25 000 N", "15 000 N", "6 000 N"], 0, "p = 10 000 × 2,5 = 25 000 Pa. S = 0,6 × 0,6 = 0,36 m² => F = 25 000 × 0,36 = 9 000 N."),
            make_vdc(4, "Một tảng băng nổi trong một bình nước hình trụ. Trên tảng băng có một hòn đá cuội nhỏ chìm. Khi tảng băng tan hết hoàn toàn thành nước lỏng thì mực nước trong bình trụ sẽ:", ["Hạ thấp xuống một chút", "Dâng cao lên", "Giữ nguyên không đổi", "Lúc đầu dâng sau tụt"], 0, "Khi đá tan, viên sỏi chìm chiếm thể tích V_sỏi < V_nước bị chiếm chỗ lúc sỏi nổi => mực nước hạ thấp xuống.")
        ]
    )

    return exams
