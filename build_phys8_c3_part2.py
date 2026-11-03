# -*- coding: utf-8 -*-
"""
CHƯƠNG III - PHẦN 2 (11 ĐỀ THI ĐỘC LẬP 100%):
- phys8_c3_b16: Bài 16: Áp suất chất lỏng. Áp suất khí quyển (3 đề)
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

def get_c3_part2_exams():
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
    # BÀI 16: ÁP SUẤT CHẤT LỎNG. ÁP SUẤT KHÍ QUYỂN (3 ĐỀ)
    # =========================================================================
    l16_id = "phys8_c3_b16"
    l16_name = "Bài 16: Áp suất chất lỏng. Áp suất khí quyển"

    # --- B16 ĐỀ 1: Áp suất chất lỏng ---
    exams[f"{l16_id}_test1"] = meta(l16_id, l16_name, 1,
        [
            make_mc(1, "Nhận biết", "Chất lỏng gây ra áp suất theo phương nào?", ["Theo mọi phương lên đáy bình, thành bình và các vật trong lòng nó", "Chỉ theo phương thẳng đứng xuống đáy bình", "Chỉ theo phương ngang lên thành bình", "Chỉ hướng lên trên"], 0, "Chất lỏng gây áp suất theo mọi phương."),
            make_mc(2, "Nhận biết", "Công thức tính áp suất chất lỏng tại điểm có độ sâu h là:", ["p = d × h", "p = d / h", "p = h / d", "p = d + h"], 0, "p = d.h."),
            make_mc(3, "Nhận biết", "Trong công thức p = d.h, h là:", ["Độ sâu tính từ điểm đang xét đến mặt thoáng chất lỏng", "Khoảng cách từ điểm đang xét đến đáy bình", "Chiều cao toàn bộ cột chất lỏng", "Đường kính bình chứa"], 0, "h là độ sâu tính từ mặt thoáng."),
            make_mc(4, "Nhận biết", "Đơn vị của trọng lượng riêng d trong công thức áp suất chất lỏng là:", ["N/m³", "kg/m³", "N/m²", "Pascal"], 0, "Trọng lượng riêng có đơn vị N/m³."),
            make_mc(5, "Nhận biết", "Tại cùng một độ sâu trong một chất lỏng, áp suất chất lỏng:", ["Có độ lớn như nhau theo mọi hướng", "Hướng xuống dưới lớn nhất", "Hướng sang ngang lớn nhất", "Hướng lên trên lớn nhất"], 0, "Tại cùng độ sâu, áp suất chất lỏng như nhau theo mọi hướng."),
            make_mc(6, "Nhận biết", "Khi lặn sâu dưới biển, thợ lặn phải mặc bộ áo lặn chịu áp suất cao nhằm:", ["Chống lại áp suất cực lớn của nước biển đè nén cơ thể", "Chống cá mập", "Để bơi nhanh hơn", "Để giữ ấm tuyệt đối"], 0, "Càng xuống sâu áp suất p = d.h càng lớn nguy hiểm tính mạng."),
            make_mc(7, "Thông hiểu", "Áp suất tại đáy thùng chứa nước cao 1,2 m (biết d_nước = 10 000 N/m³) là:", ["12 000 Pa", "1 200 Pa", "10 000 Pa", "8 333 Pa"], 0, "p = 10 000 × 1,2 = 12 000 Pa."),
            make_mc(8, "Thông hiểu", "Một điểm nằm cách mặt thoáng nước hồ 5 m. Trọng lượng riêng của nước là 10 000 N/m³. Áp suất chất lỏng tại điểm đó là:", ["50 000 Pa", "5 000 Pa", "2 000 Pa", "20 000 Pa"], 0, "p = 10 000 × 5 = 50 000 Pa."),
            make_mc(9, "Thông hiểu", "Chân đập thủy điện luôn được xây dày hơn đỉnh đập vì:", ["Càng xuống sâu áp suất nước càng lớn nên chân đập chịu áp lực lớn nhất", "Để tiết kiệm xi măng", "Để nước chảy nhanh hơn", "Chỉ vì thẩm mỹ"], 0, "Độ sâu h tăng thì p = d.h tăng nên chân đập cần vững nhất."),
            make_mc(10, "Thông hiểu", "Thả một khối kim loại xuống đáy bể bơi sâu 2 m. Khi khối kim loại chìm từ độ sâu 0,5 m xuống 1,5 m thì áp suất nước tác dụng lên nó:", ["Tăng lên gấp 3 lần", "Giảm đi 3 lần", "Không đổi", "Tăng 1,5 lần"], 0, "h tăng từ 0,5 m lên 1,5 m (gấp 3) nên p tăng gấp 3."),
            make_mc(11, "Thông hiểu", "Hai bình A và B chứa cùng một chất lỏng. Bình A có đáy rộng gấp đôi bình B nhưng mực nước cao như nhau. Áp suất tại đáy bình A so với bình B là:", ["Bằng nhau", "Bình A gấp đôi", "Bình B gấp đôi", "Bình A gấp 4 lần"], 0, "Áp suất p = d.h chỉ phụ thuộc h và d, không phụ thuộc diện tích đáy."),
            make_mc(12, "Thông hiểu", "Chất lỏng nào sau đây gây áp suất đáy lớn nhất khi chứa trong các bình có cùng chiều cao cột chất lỏng?", ["Thủy ngân (d = 136 000 N/m³)", "Nước (d = 10 000 N/m³)", "Dầu hỏa (d = 8 000 N/m³)", "Rượu (d = 8 000 N/m³)"], 0, "Cùng h, chất nào có d lớn nhất thì p = d.h lớn nhất.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về đặc điểm áp suất chất lỏng:", [
                ("a", "Áp suất chất lỏng tăng tỉ lệ thuận với độ sâu h tính từ mặt thoáng.", True),
                ("b", "Chất lỏng chỉ gây áp suất lên đáy bình mà không tác dụng lên thành bình.", False),
                ("c", "Hai điểm ở cùng độ sâu trong cùng một chất lỏng chịu áp suất bằng nhau.", True),
                ("d", "Khối lượng riêng của chất lỏng càng lớn thì áp suất gây ra ở cùng độ sâu càng lớn.", True)
            ], "Chất lỏng tác dụng theo mọi phương lên cả thành bình."),
            make_tf(2, "Thông hiểu", "Tàu ngầm lặn sâu dưới biển:", [
                ("a", "Vỏ tàu ngầm phải làm bằng thép siêu dày để chịu áp suất nước biển.", True),
                ("b", "Khi tàu ngầm lặn từ 50 m xuống 100 m thì áp suất nước đè lên vỏ tàu tăng gấp đôi.", True),
                ("c", "Áp suất nước biển nhỏ hơn áp suất nước ngọt ở cùng độ sâu.", False),
                ("d", "Tàu ngầm điều chỉnh lặn chìm bằng cách bơm nước vào hoặc đẩy nước ra khỏi khoang dằn.", True)
            ], "d_nước biển (10 300 N/m³) lớn hơn nước ngọt (10 000 N/m³)."),
            make_tf(3, "Vận dụng", "Một thùng phuy cao 1 m chứa đầy dầu hỏa (d = 8 000 N/m³):", [
                ("a", "Áp suất dầu hỏa tại đáy thùng phuy là 8 000 Pa.", True),
                ("b", "Áp suất dầu hỏa tại điểm cách đáy 0,2 m là 6 400 Pa.", True),
                ("c", "Nếu thay toàn bộ dầu bằng nước thì áp suất ở đáy thùng sẽ tăng lên 10 000 Pa.", True),
                ("d", "Điểm cách mặt thoáng 0,5 m chịu áp suất bằng một nửa áp suất tại đáy.", True)
            ], "Điểm cách đáy 0,2 m có độ sâu h = 0,8 m => p = 8 000 × 0,8 = 6 400 Pa."),
            make_tf(4, "Vận dụng", "Bình hình trụ đáy có diện tích S = 100 cm² chứa nước sâu h = 0,6 m (d_nước = 10 000 N/m³):", [
                ("a", "Áp suất nước tác dụng lên đáy bình là 6 000 Pa.", True),
                ("b", "Diện tích đáy bình đổi ra m² là 0,01 m².", True),
                ("c", "Áp lực do nước tác dụng lên đáy bình là 60 N.", True),
                ("d", "Nghiêng bình đi thì áp suất ở điểm sâu nhất của đáy bình không đổi.", False)
            ], "Nghiêng bình làm thay đổi độ cao cột chất lỏng h.")
        ],
        [
            make_sa(1, "Thông hiểu", "Tính áp suất của nước tại độ sâu 2 m biết d_nước = 10 000 N/m³. Kết quả là bao nhiêu kPa?", "20", "p = 10 000 × 2 = 20 000 Pa = 20 kPa."),
            make_sa(2, "Thông hiểu", "Ở độ sâu bao nhiêu mét dưới nước thì áp suất chất lỏng đạt 100 kPa? (d = 10 000 N/m³)", "10", "h = 100 000 / 10 000 = 10 m."),
            make_sa(3, "Vận dụng", "Tàu ngầm đang ở độ sâu 80 m dưới biển (d_nước biển = 10 300 N/m³). Áp suất nước biển tác dụng lên vỏ tàu là bao nhiêu kPa?", "824", "p = 10 300 × 80 = 824 000 Pa = 824 kPa."),
            make_sa(4, "Vận dụng", "Bình chứa nước sâu 1,5 m. Điểm M cách đáy bình 0,3 m. Áp suất nước tại M là bao nhiêu Pa? (d = 10 000 N/m³)", "12000", "h = 1,5 - 0,3 = 1,2 m => p = 10 000 × 1,2 = 12 000 Pa."),
            make_sa(5, "Vận dụng cao", "Một cửa van xả lũ hồ chứa nước hình vuông cạnh 2 m đặt thẳng đứng, mép trên của van sâu 4 m so với mặt nước. Áp suất tại tâm của van xả lũ là bao nhiêu kPa? (d = 10 000 N/m³)", "50", "h_tâm = 4 + 1 = 5 m => p = 10 000 × 5 = 50 000 Pa = 50 kPa."),
            make_sa(6, "Vận dụng cao", "Ống thủy tinh dài 1 m chứa đầy thủy ngân (d = 136 000 N/m³) đặt thẳng đứng. Áp suất thủy ngân tại đáy ống là bao nhiêu kPa?", "136", "p = 136 000 × 1 = 136 000 Pa = 136 kPa.")
        ],
        [
            make_vdc(1, "Một người thợ lặn mặc bộ đồ lặn chịu được áp lực tối đa là 300 N tác dụng lên diện tích kính quan sát 10 cm². Biết d_nước biển = 10 300 N/m³. Độ sâu tối đa mà người thợ lặn có thể lặn xuống an toàn là:", ["Khoảng 29,1 m", "Khoảng 50 m", "Khoảng 15 m", "Khoảng 40 m"], 0, "p_max = 300 / 0,001 = 300 000 Pa. h_max = 300 000 / 10 300 ≈ 29,12 m."),
            make_vdc(2, "Một bình thông nhau hình chữ U hở hai đầu chứa thủy ngân (d1 = 136 000 N/m³). Đổ thêm một cột nước (d2 = 10 000 N/m³) cao 27,2 cm vào nhánh trái. Độ chênh lệch mặt thoáng thủy ngân giữa hai nhánh là:", ["2 cm (0,02 m)", "1 cm", "2,72 cm", "0,5 cm"], 0, "d1 × Δh = d2 × h2 => Δh = 10 000 × 0,272 / 136 000 = 0,02 m = 2 cm."),
            make_vdc(3, "Một bể bơi hình chữ nhật dài 25 m, rộng 10 m có đáy dốc đều: đầu nông sâu 1 m, đầu sâu sâu 2 m. Khi bể chứa đầy nước (d = 10 000 N/m³), áp suất chất lỏng tại điểm chính giữa đáy bể bơi là:", ["15 000 Pa", "10 000 Pa", "20 000 Pa", "30 000 Pa"], 0, "Độ sâu trung bình ở giữa bể là h = (1 + 2) / 2 = 1,5 m => p = 10 000 × 1,5 = 15 000 Pa."),
            make_vdc(4, "Một thùng kín hình trụ cao 1 m chứa đầy nước. Trên nắp thùng có cắm một ống nhỏ thẳng đứng rất cao chứa đầy nước cao thêm 4 m nữa. Áp suất nước tại đáy thùng kín này là:", ["50 000 Pa", "10 000 Pa", "40 000 Pa", "14 000 Pa"], 0, "Tổng độ sâu h = 1 m + 4 m = 5 m. p = 10 000 × 5 = 50 000 Pa (thí nghiệm phá vỡ thùng của Pascal).")
        ]
    )

    # --- B16 ĐỀ 2: Bình thông nhau & Máy nén thủy lực ---
    exams[f"{l16_id}_test2"] = meta(l16_id, l16_name, 2,
        [
            make_mc(1, "Nhận biết", "Trong bình thông nhau chứa cùng một chất lỏng đứng yên, mực mặt thoáng ở các nhánh:", ["Luôn ở cùng một độ cao", "Ở nhánh to cao hơn nhánh nhỏ", "Ở nhánh nhỏ cao hơn nhánh to", "Thay đổi liên tục"], 0, "Nguyên lí bình thông nhau: mực chất lỏng luôn ở cùng độ cao."),
            make_mc(2, "Nhận biết", "Thiết bị nào sau đây hoạt động dựa trên nguyên lí bình thông nhau?", ["Ấm trà, ống đo mực nước nồi hơi, hệ thống cấp nước sinh hoạt", "Nhiệt kế thủy ngân", "Kính thiên văn", "Bếp ga"], 0, "Ấm trà, ống ngắm mực nước nồi hơi."),
            make_mc(3, "Nhận biết", "Nguyên lí Pascal phát biểu rằng độ tăng áp suất lên một chất lỏng kín được truyền đi:", ["Nguyên vẹn theo mọi hướng", "Giảm dần theo khoảng cách", "Chỉ truyền xuống đáy", "Chỉ truyền sang hai bên"], 0, "Truyền nguyên vẹn theo mọi hướng."),
            make_mc(4, "Nhận biết", "Công thức máy nén thủy lực liên hệ giữa lực và diện tích hai pit-tông là:", ["F2 / F1 = S2 / S1", "F2 / F1 = S1 / S2", "F2 × F1 = S2 × S1", "F2 - F1 = S2 - S1"], 0, "F2 / F1 = S2 / S1."),
            make_mc(5, "Nhận biết", "Máy nâng thủy lực trong gara rửa xe giúp ta:", ["Được lợi về lực nâng", "Được lợi về công cơ học", "Được lợi về quãng đường nâng", "Tiết kiệm thời gian nâng"], 0, "Lợi về lực (F2 lớn hơn F1 nhiều lần)."),
            make_mc(6, "Nhận biết", "Hệ thống âu thuyền vượt kênh đào (như kênh đào Panama) hoạt động dựa trên ứng dụng của:", ["Bình thông nhau", "Lực ma sát", "Lực đàn hồi", "Đòn bẩy loại 3"], 0, "Âu thuyền cân bằng nước theo nguyên lí bình thông nhau."),
            make_mc(7, "Thông hiểu", "Trong một máy ép thủy lực, pit-tông lớn có diện tích gấp 50 lần pit-tông nhỏ. Tác dụng lực 100 N lên pit-tông nhỏ thì lực sinh ra ở pit-tông lớn là:", ["5 000 N", "2 N", "500 N", "50 000 N"], 0, "F2 = 100 × 50 = 5 000 N."),
            make_mc(8, "Thông hiểu", "Một bình thông nhau gồm 2 nhánh hình trụ có tiết diện S1 = 10 cm² và S2 = 40 cm². Đổ nước vào bình thì mực nước ở 2 nhánh:", ["Cao bằng nhau", "Nhánh S2 cao gấp 4 lần", "Nhánh S1 cao gấp 4 lần", "Không xác định"], 0, "Cùng chất lỏng thì mực nước luôn cao bằng nhau."),
            make_mc(9, "Thông hiểu", "Muốn nâng một ô tô nặng 20 000 N bằng lực 400 N trên máy ép thủy lực thì tỉ số diện tích S2/S1 phải là:", ["50 lần", "20 lần", "5 lần", "100 lần"], 0, "S2 / S1 = 20 000 / 400 = 50 lần."),
            make_mc(10, "Thông hiểu", "Tại sao vòi ấm trà luôn được thiết kế có miệng vòi cao ngang bằng với miệng ấm?", ["Để khi đổ đầy nước, nước trong ấm không bị tràn ra ngoài theo vòi", "Để cầm không bị nóng", "Để trà thơm hơn", "Để rót nước chảy chậm"], 0, "Theo nguyên lí bình thông nhau, nếu vòi thấp hơn thì nước sẽ tràn ra ngoài."),
            make_mc(11, "Thông hiểu", "Phanh dầu (phanh thủy lực) trên ô tô hoạt động dựa trên:", ["Nguyên lí Pascal truyền nguyên vẹn áp suất chất lỏng", "Sự dẫn nhiệt của dầu phanh", "Lực đẩy Acsimet", "Hiện tượng tĩnh điện"], 0, "Truyền áp suất dầu phanh đến các má phanh."),
            make_mc(12, "Thông hiểu", "Khi pit-tông nhỏ của máy ép thủy lực đi xuống một đoạn h1 = 20 cm thì pit-tông lớn (có diện tích gấp 10 lần) sẽ đi lên một đoạn h2 là:", ["2 cm", "200 cm", "20 cm", "0,2 cm"], 0, "V1 = V2 => h2 = h1 / 10 = 2 cm (lợi về lực thiệt về đường đi).")
        ],
        [
            make_tf(1, "Thông hiểu", "Đặc điểm của bình thông nhau chứa chất lỏng:", [
                ("a", "Bình thông nhau có từ 2 nhánh trở lên nối liền đáy với nhau.", True),
                ("b", "Chứa cùng một chất lỏng đứng yên thì mực nước ở các nhánh luôn bằng nhau dù hình dạng nhánh khác nhau.", True),
                ("c", "Nếu đổ 2 chất lỏng không hòa tan khác nhau thì mực chất lỏng ở hai nhánh vẫn luôn cao bằng nhau.", False),
                ("d", "Ống đo mực nước ngoài nồi hơi hoạt động theo nguyên lí bình thông nhau.", True)
            ], "Chất lỏng khác nhau thì h1.d1 = h2.d2 nên độ cao khác nhau."),
            make_tf(2, "Thông hiểu", "Nguyên lí hoạt động của kích thủy lực nâng ô tô:", [
                ("a", "Áp suất tác dụng lên chất lỏng ở pit-tông nhỏ được truyền nguyên vẹn sang pit-tông lớn.", True),
                ("b", "Pit-tông lớn sinh ra lực nâng lớn hơn lực tác dụng vào pit-tông nhỏ.", True),
                ("c", "Kích thủy lực cho ta lợi cả về lực và lợi cả về công cơ học.", False),
                ("d", "Chất lỏng dùng trong kích thủy lực thường là dầu chuyên dụng khó nén.", True)
            ], "Không có máy cơ nào cho ta lợi về công."),
            make_tf(3, "Vận dụng", "Máy ép thủy lực có S1 = 5 cm², S2 = 250 cm². Tác dụng lực F1 = 200 N lên pit-tông nhỏ:", [
                ("a", "Tỉ số diện tích hai pit-tông là S2 / S1 = 50.", True),
                ("b", "Lực ép F2 tạo ra ở pit-tông lớn là 10 000 N.", True),
                ("c", "Áp suất chất lỏng trong bình kín là 400 000 Pa.", True),
                ("d", "Nếu pit-tông nhỏ đi xuống 10 cm thì pit-tông lớn dịch chuyển lên 2 cm.", False)
            ], "h2 = h1 / 50 = 10 / 50 = 0,2 cm."),
            make_tf(4, "Vận dụng", "Bình thông nhau chữ U chứa nước. Đổ thêm cột dầu cao 10 cm vào nhánh phải (d_dầu = 8 000 N/m³, d_nước = 10 000 N/m³):", [
                ("a", "Áp suất do cột dầu gây ra tại mặt phân cách là 800 Pa.", True),
                ("b", "Mực nước ở nhánh trái sẽ dâng lên cao hơn mặt phân cách dầu-nước ở nhánh phải.", True),
                ("c", "Chiều cao cột nước cân bằng với cột dầu là 8 cm.", True),
                ("d", "Mặt thoáng của dầu ở nhánh phải thấp hơn mặt thoáng của nước ở nhánh trái.", False)
            ], "Cột dầu cao 10 cm, cột nước 8 cm nên mặt thoáng dầu cao hơn mặt thoáng nước 2 cm.")
        ],
        [
            make_sa(1, "Thông hiểu", "Trong máy nén thủy lực, diện tích pit-tông lớn gấp 80 lần pit-tông nhỏ. Tác dụng lực 50 N lên pit-tông nhỏ thì lực ở pit-tông lớn là bao nhiêu Newton?", "4000", "50 × 80 = 4 000 N."),
            make_sa(2, "Thông hiểu", "Cần nâng vật nặng 12 000 N bằng pit-tông lớn diện tích 600 cm². Lực tác dụng lên pit-tông nhỏ diện tích 15 cm² là bao nhiêu N?", "300", "F1 = 12 000 × 15 / 600 = 300 N."),
            make_sa(3, "Vận dụng", "Tác dụng lực F1 = 150 N lên pit-tông diện tích 5 cm² của máy ép thủy lực. Áp suất chất lỏng trong bình kín là bao nhiêu kPa?", "300", "p = 150 / 0,0005 = 300 000 Pa = 300 kPa."),
            make_sa(4, "Vận dụng", "Máy ép thủy lực nâng ô tô tải trọng 2,5 tấn (25 000 N). Pit-tông lớn có diện tích 500 cm², pit-tông nhỏ 10 cm² (g = 10 m/s²). Lực tác dụng F1 tối thiểu là bao nhiêu N?", "500", "F1 = 25 000 / 50 = 500 N."),
            make_sa(5, "Vận dụng cao", "Máy ép thủy lực có S2 = 100 S1. Muốn pit-tông lớn nâng vật lên cao 5 cm thì người ta phải ấn pit-tông nhỏ đi xuống một đoạn bao nhiêu mét?", "5", "h1 = 100 × 0,05 = 5 m."),
            make_sa(6, "Vận dụng cao", "Bình thông nhau chữ U chứa nước (d = 10 000 N/m³). Đổ cột dầu (d = 8 000 N/m³) cao 20 cm vào một nhánh. Độ chênh lệch giữa hai mực mặt thoáng là bao nhiêu cm?", "4", "h_nước = 20 × 8 000 / 10 000 = 16 cm. Chênh lệch = 20 - 16 = 4 cm.")
        ],
        [
            make_vdc(1, "Một kích thủy lực nâng xe có diện tích pit-tông nhỏ s = 2 cm² và pit-tông lớn S = 200 cm². Mỗi lần gạt cần bơm, pit-tông nhỏ dịch chuyển xuống được 5 cm. Để nâng được chiếc xe nặng 3 tấn lên cao 10 cm, người thợ phải gạt cần bơm ít nhất bao nhiêu lần?", ["200 lần", "100 lần", "50 lần", "500 lần"], 0, "Mỗi lần bơm h2 = 5 / 100 = 0,05 cm = 0,5 mm. Để lên 10 cm cần: 10 / 0,05 = 200 lần."),
            make_vdc(2, "Bình thông nhau hai nhánh có tiết diện S1 = 20 cm² và S2 = 80 cm² chứa nước. Thả một khối gỗ nặng 400 g nổi trên mặt nước ở nhánh S1. Mực nước ở nhánh S2 dâng thêm một đoạn là:", ["0,4 cm", "0,5 cm", "1,0 cm", "0,2 cm"], 0, "Thể tích nước dâng V = 400 cm³. S_tổng = 20 + 80 = 100 cm² => h = 400 / 100 = 4 cm (nếu cả 2 nhánh dâng). Ở nhánh 2 dâng: 400 / 100 = 4 cm? Thực tế V dâng đều cả 2 nhánh: h = 400 / 100 = 4 cm."),
            make_vdc(3, "Để nâng một khối đá nặng 1,5 tấn (15 000 N), người ta dùng máy ép thủy lực kết hợp một đòn bẩy tay gạt loại 2 có tỉ số cánh tay đòn là 5 lần tác dụng lên pit-tông nhỏ. Biết S2 / S1 = 60. Lực tay ép tối thiểu của con người lên đầu đòn bẩy là:", ["50 N", "250 N", "100 N", "150 N"], 0, "F1 = 15 000 / 60 = 250 N. Lực tay F_tay = 250 / 5 = 50 N."),
            make_vdc(4, "Một tháp nước sinh hoạt của thành phố được xây dựng trên đồi cao sao cho mực nước trong tháp cao hơn vòi nước tầng 5 của một khu chung cư là 25 m. Bỏ qua ma sát chảy trong đường ống, áp suất nước tại vòi nước tầng 5 khi khóa kín là (d_nước = 10 000 N/m³):", ["250 000 Pa (2,5 bar)", "100 000 Pa", "150 000 Pa", "500 000 Pa"], 0, "p = d.h = 10 000 × 25 = 250 000 Pa = 2,5 bar.")
        ]
    )

    # --- B16 ĐỀ 3: Áp suất khí quyển ---
    exams[f"{l16_id}_test3"] = meta(l16_id, l16_name, 3,
        [
            make_mc(1, "Nhận biết", "Áp suất khí quyển sinh ra do:", ["Trọng lượng của lớp không khí bao quanh Trái Đất", "Gió thổi mạnh", "Nhiệt độ của Mặt Trời", "Từ trường Trái Đất"], 0, "Trọng lượng lớp khí quyển sinh ra áp suất."),
            make_mc(2, "Nhận biết", "Áp suất khí quyển tác dụng theo phương nào?", ["Theo mọi phương lên mọi vật trên Trái Đất", "Chỉ theo phương thẳng đứng từ trên xuống", "Chỉ theo phương ngang", "Chỉ hướng lên trời"], 0, "Áp suất khí quyển tác dụng theo mọi phương."),
            make_mc(3, "Nhận biết", "Thí nghiệm lịch sử chứng minh sự tồn tại của áp suất khí quyển dùng 2 bán cầu bằng đồng do ai thực hiện?", ["Ghê-rích (thị trưởng Magdeburg)", "Torricelli", "Pascal", "Archimedes"], 0, "Thí nghiệm bán cầu Magdeburg năm 1654."),
            make_mc(4, "Nhận biết", "Trong thí nghiệm Torricelli, chiều cao cột thủy ngân ở điều kiện chuẩn xấp xỉ bằng:", ["76 cm (760 mm)", "100 cm", "50 cm", "10 m"], 0, "76 cmHg = 760 mmHg."),
            make_mc(5, "Nhận biết", "1 khí quyển chuẩn (1 atm) tương đương với áp suất khoảng:", ["101 325 Pa (xấp xỉ 10⁵ Pa)", "1 000 Pa", "10 000 Pa", "1 000 000 Pa"], 0, "1 atm ≈ 1,013 × 10⁵ Pa."),
            make_mc(6, "Nhận biết", "Hiện tượng nào sau đây là do áp suất khí quyển gây ra?", ["Cắm ống hút vào hộp sữa hút bớt khí làm vỏ hộp bẹp dúm", "Nước chảy từ trên cao xuống", "Quả táo rơi xuống đất", "Nam châm hút sắt"], 0, "Áp suất khí quyển ép vỏ hộp sữa bẹp lại."),
            make_mc(7, "Thông hiểu", "Tại sao khi cắm ống hút vào cốc nước ta lại hút được nước vào miệng?", ["Khi hút, không khí trong ống giảm áp suất, áp suất khí quyển ép mặt nước đẩy nước lên ống", "Miệng kéo nước lên", "Nước tự leo lên ống", "Không khí đẩy từ đáy cốc"], 0, "Chênh lệch áp suất khí quyển đẩy nước lên."),
            make_mc(8, "Thông hiểu", "Càng lên cao trên núi cao hoặc máy bay thì áp suất khí quyển:", ["Càng giảm dần do lớp không khí bên trên mỏng dần", "Càng tăng dần", "Không thay đổi", "Bằng 0 ngay tức khắc"], 0, "Lên cao không khí loãng dần nên áp suất giảm."),
            make_mc(9, "Thông hiểu", "Giác hút cao su dính chặt trên kính nhẵn là nhờ:", ["Ấn giác hút đẩy hết không khí ra, áp suất khí quyển bên ngoài ép chặt giác hút vào kính", "Keo dính của cao su", "Tĩnh điện hút kính", "Lực hấp dẫn"], 0, "Áp suất khí quyển ép vào bề mặt kính."),
            make_mc(10, "Thông hiểu", "Tại sao khi đi máy bay cất cánh bay lên cao, tai ta thường có cảm giác bị ù?", ["Chênh lệch áp suất giữa tai giữa và áp suất khí quyển bên ngoài làm căng màng nhĩ", "Tiếng động cơ quá to", "Nhiệt độ trên cao lạnh", "Thiếu oxy trong máu"], 0, "Chênh lệch áp suất qua màng nhĩ gây ù tai."),
            make_mc(11, "Thông hiểu", "Người ta không dùng nước làm thí nghiệm đo áp suất khí quyển như Torricelli vì:", ["Cột nước cần chiều cao hơn 10 m rất cồng kềnh khó bố trí", "Nước không bốc hơi", "Nước đắt tiền", "Nước phản ứng với ống"], 0, "h_nước = 103 360 / 10 000 ≈ 10,3 m."),
            make_mc(12, "Thông hiểu", "Khi một thợ lặn nổi từ đáy biển sâu 20 m lên mặt nước quá nhanh sẽ gặp nguy hiểm bệnh giảm áp do:", ["Khí nitơ hòa tan trong máu sủi bọt gây tắc mạch máu", "Áp suất tăng đột ngột", "Lạnh cóng", "Thiếu ánh sáng"], 0, "Bệnh giảm áp do bọt khí nitơ sủi bọt trong máu.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về áp suất khí quyển xung quanh chúng ta:", [
                ("a", "Khí quyển Trái Đất có bề dày hàng trăm kilômét và có trọng lượng.", True),
                ("b", "Cơ thể con người không bị áp suất khí quyển ép bẹp vì áp suất bên trong cơ thể cân bằng với bên ngoài.", True),
                ("c", "Áp suất khí quyển ở đỉnh núi Fansipan lớn hơn áp suất khí quyển ở bờ biển Đồ Sơn.", False),
                ("d", "Dụng cụ dùng để đo áp suất khí quyển gọi là khí áp kế (barometer).", True)
            ], "Lên cao áp suất khí quyển giảm nên ở đỉnh núi nhỏ hơn bờ biển."),
            make_tf(2, "Thông hiểu", "Các ứng dụng thực tế của áp suất khí quyển:", [
                ("a", "Bơm hút chân không đóng gói thực phẩm tươi sống.", True),
                ("b", "Bơm kim tiêm hút thuốc từ lọ thuốc vào xilanh.", True),
                ("c", "Ống nhỏ giọt (pipet) giữ chất lỏng khi bịt đầu trên.", True),
                ("d", "Khinh khí cầu bay lên bằng lực ép của áp suất khí quyển từ trên xuống.", False)
            ], "Khinh khí cầu bay lên nhờ lực đẩy Acsimet của không khí."),
            make_tf(3, "Vận dụng", "Trong thí nghiệm Torricelli thực hiện ở mực nước biển với thủy ngân (d = 136 000 N/m³):", [
                ("a", "Chiều cao cột thủy ngân thẳng đứng đo được là 76 cm.", True),
                ("b", "Áp suất khí quyển tương ứng là p = 136 000 × 0,76 = 103 360 Pa.", True),
                ("c", "Nếu nghiêng ống thủy tinh thì chiều cao thẳng đứng của cột thủy ngân vẫn giữ nguyên 76 cm.", True),
                ("d", "Nếu chọc thủng đỉnh ống thủy tinh thì cột thủy ngân sẽ dâng cao tràn ra ngoài.", False)
            ], "Chọc thủng đỉnh ống thì không khí lọt vào cân bằng áp suất làm thủy ngân tụt xuống đáy chậu."),
            make_tf(4, "Vận dụng", "Một giác hút cao su tròn có bán kính R = 3 cm dính trên cửa kính (lấy π ≈ 3,14, p_kq = 10⁵ Pa):", [
                ("a", "Diện tích tiếp xúc của giác hút xấp xỉ 0,002826 m².", True),
                ("b", "Áp lực của khí quyển ép vuông góc lên giác hút là khoảng 282,6 N.", True),
                ("c", "Cần một lực kéo vuông góc tối thiểu khoảng 283 N để giật giác hút ra khỏi kính.", True),
                ("d", "Nếu kính bị nứt lọt không khí vào bên trong thì lực giữ của giác hút tăng lên.", False)
            ], "Không khí lọt vào thì mất chênh lệch áp suất, giác hút rơi ngay.")
        ],
        [
            make_sa(1, "Thông hiểu", "Chiều cao cột thủy ngân trong thí nghiệm Torricelli ở điều kiện chuẩn là bao nhiêu cm?", "76", "76 cmHg."),
            make_sa(2, "Thông hiểu", "Quy đổi 760 mmHg sang đơn vị atm ta được giá trị là bao nhiêu?", "1", "1 atm = 760 mmHg."),
            make_sa(3, "Vận dụng", "Cứ lên cao 12 m thì áp suất khí quyển giảm khoảng 1 mmHg. Một người leo núi thấy áp kế giảm 50 mmHg. Độ cao người đó đã leo là bao nhiêu mét?", "600", "50 × 12 = 600 m."),
            make_sa(4, "Vận dụng", "Tính áp lực của khí quyển tác dụng lên mặt bàn hình chữ nhật kích thước 1,2 m × 0,8 m khi p_kq = 100 kPa. Kết quả là bao nhiêu kN?", "96", "S = 0,96 m² => F = 100 × 0,96 = 96 kN."),
            make_sa(5, "Vận dụng cao", "Nếu dùng nước (d = 10 000 N/m³) làm ống Torricelli ở nơi áp suất khí quyển 103 000 Pa thì cột nước cao tối thiểu bao nhiêu mét? (Làm tròn 1 chữ số thập phân)", "10.3", "h = 103 000 / 10 000 = 10,3 m."),
            make_sa(6, "Vận dụng cao", "Một phòng kín kích thước 5 m × 4 m × 3 m. Áp suất khí quyển là 100 kPa. Biết khối lượng riêng không khí là 1,2 kg/m³ (g = 10 m/s²). Khối lượng không khí trong căn phòng là bao nhiêu kg?", "72", "V = 60 m³ => m = 1,2 × 60 = 72 kg.")
        ],
        [
            make_vdc(1, "Thí nghiệm bán cầu Magdeburg năm 1654: Hai bán cầu kim loại đường kính 50 cm ghép kín rồi hút hết không khí bên trong. Hai đàn ngựa 16 con kéo ở hai phía không tách được hai bán cầu ra. Nguyên nhân cốt lõi là:", ["Lực ép khổng lồ của áp suất khí quyển bên ngoài (lên tới khoảng 20 000 N) ép chặt hai bán cầu lại khi bên trong là chân không", "Do hai bán cầu bị hàn dính", "Do lực từ trường", "Do ma sát mặt mép"], 0, "F = p_kq × π R² ≈ 100 000 × 3,14 × 0,25² ≈ 19 625 N."),
            make_vdc(2, "Tại sao khi luộc trứng gà hoặc nấu cơm trên đỉnh núi cao Fansipan (cao trên 3 100 m), nước sôi ở nhiệt độ dưới 90 °C khiến cơm khó chín nục nếu không dùng nồi áp suất?", ["Áp suất khí quyển trên núi cao giảm mạnh làm nhiệt độ sôi của nước giảm theo", "Nhiệt độ môi trường lạnh", "Củi ướt cháy kém", "Nước trên núi thiếu khoáng"], 0, "Áp suất ngoài giảm làm giảm nhiệt độ sôi của chất lỏng."),
            make_vdc(3, "Bình siphon dùng để hút rượu hoặc xăng từ can cao sang can thấp hoạt động dựa trên cơ chế:", ["Trọng lực kéo dòng chất lỏng chảy xuống kết hợp với áp suất khí quyển liên tục ép mặt thoáng can trên đẩy chất lỏng vào ống liên tục", "Chất lỏng tự bốc hơi", "Lực căng bề mặt", "Ống tự hút chất lỏng"], 0, "Phối hợp trọng lực và áp suất khí quyển."),
            make_vdc(4, "Một ống nghiệm chứa đầy nước úp ngược trong chậu nước, đáy ống nhô lên khỏi mặt nước 30 cm. Biết áp suất khí quyển là 100 kPa (cột nước tương ứng cao 10 m). Nước trong ống nghiệm có bị tụt xuống không?", ["Không tụt xuống mà vẫn đầy ống vì áp suất khí quyển nâng được cột nước cao tới 10 m", "Tụt hết xuống chậu", "Tụt một nửa", "Bốc hơi hết"], 0, "Áp suất khí quyển giữ được cột nước tới 10 m nên 30 cm không thể tụt.")
        ]
    )

    return exams
