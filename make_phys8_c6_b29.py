# -*- coding: utf-8 -*-
"""
Dữ liệu 3 đề thi độc lập Bài 29: Sự nở vì nhiệt (phys8_c6_b29)
- Đề 1: Sự nở vì nhiệt của chất rắn, khe co giãn đường sắt và cầu thép
- Đề 2: Sự nở vì nhiệt của chất lỏng, hiện tượng dị thường của nước ở 4°C
- Đề 3: Sự nở vì nhiệt của chất khí và ứng dụng của băng kép (rơle nhiệt)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {"id": qid, "level": level, "question": q_text, "options": options, "correct": correct_idx, "explanation": explanation}

def make_tf(qid, level, prompt, statements, explanation=""):
    return {"id": qid, "level": level, "question": prompt, "statements": [{"subId": s[0], "text": s[1], "correct": s[2]} for s in statements], "explanation": explanation}

def make_sa(qid, level, q_text, answer, explanation=""):
    return {"id": qid, "level": level, "question": q_text, "correctAnswer": str(answer).strip(), "explanation": explanation}

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {"id": qid, "level": "Vận dụng cao", "question": q_text, "options": options, "correct": correct_idx, "explanation": explanation}

def get_b29_exams():
    exams = {}
    ch_id = "phys8_c6"
    ch_title = "Chương VI: Nhiệt"
    l_id = "phys8_c6_b29"
    l_name = "Bài 29: Sự nở vì nhiệt"

    def meta(t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # ĐỀ 1: Sự nở vì nhiệt của Chất rắn & Khe co giãn công trình
    exams[f"{l_id}_test1"] = meta(1,
        [
            make_mc(1, "Nhận biết", "Hiện tượng chất rắn nở ra khi nóng lên và co lại khi lạnh đi được gọi là:", ["Sự nở vì nhiệt của chất rắn", "Sự nóng chảy", "Sự bay hơi", "Sự ngưng tụ"], 0, "Nở ra khi nóng, co lại khi lạnh là sự nở vì nhiệt."),
            make_mc(2, "Nhận biết", "Khi nung nóng một quả cầu kim loại, thể tích và khối lượng riêng của quả cầu thay đổi như thế nào?", ["Thể tích tăng lên, khối lượng riêng giảm đi", "Thể tích giảm, khối lượng riêng tăng", "Cả hai đều tăng", "Cả hai đều giảm"], 0, "Thể tích V tăng, m không đổi nên D = m/V giảm."),
            make_mc(3, "Nhận biết", "Trong các kim loại: nhôm, đồng, sắt; kim loại nào nở vì nhiệt nhiều nhất khi tăng cùng nhiệt độ?", ["Nhôm (Al)", "Đồng (Cu)", "Sắt (Fe)", "Cả ba nở như nhau"], 0, "Độ nở vì nhiệt: Nhôm > Đồng > Sắt."),
            make_mc(4, "Nhận biết", "Tại sao ở chỗ tiếp nối giữa hai thanh ray đường sắt người ta luôn để lại một khe hở nhỏ?", ["Để khi trời nắng nóng thanh ray nở dài ra không bị chèn ép gây uốn cong vênh đường ray", "Để tiết kiệm thép", "Để tàu chạy êm hơn", "Để thoát nước mưa"], 0, "Khe hở để thanh ray giãn nở tự do khi nhiệt độ tăng."),
            make_mc(5, "Nhận biết", "Tại một đầu của các cây cầu thép lớn thường được đặt tựa lên các con lăn tròn nhằm mục đích:", ["Cho phép nhịp cầu co giãn nở dài tự do khi nhiệt độ thời tiết thay đổi mà không phá hủy mố cầu", "Để cầu chuyển động", "Làm cầu nhẹ hơn", "Chống động đất"], 0, "Con lăn giúp nhịp cầu giãn nở tự do không sinh lực phá hủy."),
            make_mc(6, "Nhận biết", "Khi tra khâu sắt vào cán dao gỗ, người thợ rèn thường nung nóng đỏ khâu sắt rồi mới tra vào cán vì:", ["Khâu sắt nở rộng ra dễ tra vào cán, khi nguội co lại siết chặt lấy cán gỗ", "Khâu sắt mềm hơn", "Để cán gỗ không bị cháy", "Để khâu sắt không bị gỉ"], 0, "Nung nóng khâu sắt nở ra, khi nguội co lại siết chặt cán dao."),
            make_mc(7, "Thông hiểu", "Một chiếc vòng kim loại vừa khít một quả cầu ở nhiệt độ phòng. Để quả cầu lọt qua vòng một cách dễ dàng, ta có thể:", ["Nung nóng chiếc vòng hoặc làm lạnh quả cầu", "Nung nóng cả hai như nhau", "Nung nóng quả cầu", "Làm lạnh chiếc vòng"], 0, "Nung nóng vòng làm lỗ nở to ra, hoặc làm lạnh quả cầu co nhỏ lại."),
            make_mc(8, "Thông hiểu", "Vì sao các đường ống dẫn hơi nước nóng dài bằng kim loại thường được uốn cong thành các đoạn hình chữ U?", ["Để ống có thể co giãn đàn hồi khi nhiệt độ thay đổi mà không bị bẻ gãy đứt mối hàn", "Để nước chảy chậm lại", "Để trang trí", "Để lọc cặn bẩn"], 0, "Đoạn uốn cong co giãn đàn hồi triệt tiêu ứng suất nhiệt."),
            make_mc(9, "Thông hiểu", "Bê tông cốt thép được ứng dụng cực kì rộng rãi và bền vững trong xây dựng vì:", ["Bê tông và thép có độ nở vì nhiệt xấp xỉ như nhau khi nhiệt độ thay đổi", "Thép nhẹ hơn bê tông", "Bê tông hút nước", "Thép không dẫn nhiệt"], 0, "Hệ số nở nhiệt của thép và bê tông gần bằng nhau nên không nứt vỡ."),
            make_mc(10, "Thông hiểu", "Khi hơ nóng một chiếc đinh ốc bị kẹt chặt vào đai ốc (bu-lông), người ta thường hơ nóng nhanh phần đai ốc bên ngoài để:", ["Đai ốc nở ra trước làm lỏng mối ren dễ vặn tháo ra", "Làm chảy đinh ốc", "Làm đinh ốc co lại", "Để đai ốc đổi màu"], 0, "Đai ốc nở rộng ra trước giúp vặn ốc dễ dàng."),
            make_mc(11, "Thông hiểu", "Thí nghiệm nung nóng thanh kim loại bị chặn chặt hai đầu bằng chốt thép cho thấy hiện tượng chốt thép bị bẻ gãy gập chứng tỏ:", ["Sự nở vì nhiệt của chất rắn khi bị ngăn cản có thể sinh ra lực rất lớn", "Thanh kim loại quá yếu", "Chốt thép làm bằng chì", "Kim loại bị nung chảy"], 0, "Sự co giãn vì nhiệt bị cản trở sinh ra ngoại lực vô cùng lớn."),
            make_mc(12, "Thông hiểu", "Một thanh đồng dài 1 m ở 20°C. Khi nhiệt độ tăng lên 60°C (tăng 40°C), chiều dài của thanh đồng sẽ:", ["Tăng thêm một đoạn nhỏ tỉ lệ thuận với độ tăng nhiệt độ", "Giảm đi", "Không đổi", "Tăng gấp đôi chiều dài ban đầu"], 0, "ΔL = α * L0 * Δt tỉ lệ thuận với độ tăng nhiệt độ.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về bản chất và quy luật nở vì nhiệt của chất rắn đề 1:", [
                ("a", "Chất rắn nở ra khi nhiệt độ tăng và co lại khi nhiệt độ giảm.", True),
                ("b", "Các chất rắn khác nhau có mức độ nở vì nhiệt khác nhau khi cùng tăng một lượng nhiệt độ.", True),
                ("c", "Khi một quả cầu sắt rỗng bị nung nóng thì thể tích khoang rỗng bên trong bị co hẹp lại.", False),
                ("d", "Khối lượng của vật rắn không thay đổi trong suốt quá trình giãn nở vì nhiệt.", True)
            ], "Khi nung nóng vật rỗng, khoang rỗng bên trong nở to ra giống như khi nó đặc."),
            make_tf(2, "Thông hiểu", "Về các biện pháp kỹ thuật xử lý sự co giãn nhiệt trong công trình đề 1:", [
                ("a", "Đường ray xe lửa luôn được hàn liền thành một khối thép dài hàng nghìn kilômét không để khe hở.", False),
                ("b", "Khe co giãn trên mặt cầu và mặt đường bê tông giúp tránh nứt gãy mặt đường vào mùa hè nắng gắt.", True),
                ("c", "Đầu nhịp cầu đặt trên các con lăn thép cho phép dầm cầu trượt tự do theo phương ngang.", True),
                ("d", "Các đường ống dẫn dầu khí trên mặt đất thường được bố trí uốn lượn ziczac để triệt tiêu lực kéo nén nhiệt.", True)
            ], "Hàn liền không khe hở trên đường sắt thông thường sẽ gây vênh ray trật bánh tàu."),
            make_tf(3, "Thông hiểu", "Về hiện tượng lực xuất hiện khi sự co giãn vì nhiệt bị cản trở đề 1:", [
                ("a", "Khi nở vì nhiệt bị cản trở, vật rắn có thể sinh ra lực cực lớn đủ làm gãy các thanh thép chịu lực.", True),
                ("b", "Khi co lại vì nhiệt bị giữ chặt hai đầu, thanh kim loại sẽ sinh ra lực kéo có thể làm đứt gãy kết cấu.", True),
                ("c", "Đổ nước sôi vào cốc thủy tinh có thành rất mỏng cốc sẽ dễ vỡ hơn nhiều so với cốc có thành dày.", False),
                ("d", "Rót từ từ một ít nước nóng tráng đều lòng cốc thủy tinh trước khi đổ đầy nước sôi giúp cốc không bị nứt vỡ.", True)
            ], "Cốc mỏng truyền nhiệt nhanh qua hai mặt nên ít bị vỡ hơn cốc dày."),
            make_tf(4, "Thông hiểu", "Về độ dãn nở dài của các vật liệu kỹ thuật thường gặp đề 1:", [
                ("a", "Nhôm nở dài nhiều hơn đồng khoảng 1,4 lần khi cùng tăng nhiệt độ.", True),
                ("b", "Đồng nở dài nhiều hơn sắt thép khi cùng chịu độ tăng nhiệt độ.", True),
                ("c", "Thạch anh nung chảy có hệ số nở nhiệt cực nhỏ nên chịu sốc nhiệt thay đổi nhiệt độ đột ngột rất tốt.", True),
                ("d", "Sứ cách điện nở vì nhiệt nhiều hơn kim loại nhôm gấp hàng chục lần.", False)
            ], "Sứ có độ nở vì nhiệt nhỏ hơn kim loại nhiều lần.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một thanh ray đường sắt bằng thép dài 12,5 m ở 20°C. Khi nhiệt độ mùa hè tăng lên 50°C (tăng 30°C), thanh ray nở dài thêm 4,5 mm. Nếu nhiệt độ tăng 60°C thì thanh ray nở dài thêm bao nhiêu milimét (mm)?", "9", "ΔL tỉ lệ thuận với Δt: 4,5 * (60 / 30) = 9 mm."),
            make_sa(2, "Thông hiểu", "Một nhịp cầu thép dài 100 m có hệ số nở dài 1,2 . 10^-5 K^-1. Khi nhiệt độ tăng thêm 25°C, nhịp cầu nở dài thêm bao nhiêu xentimét (cm)?", "3", "ΔL = 100 * (1,2e-5) * 25 = 0,03 m = 3 cm."),
            make_sa(3, "Thông hiểu", "Để tránh vênh đường ray khi nhiệt độ tăng tối đa 40°C, khe hở giữa hai đầu thanh ray 10 m phải để tối thiểu là 4,8 mm. Nếu dùng thanh ray dài 20 m trong cùng điều kiện thì khe hở tối thiểu phải là bao nhiêu milimét (mm)?", "9.6", "ΔL tỉ lệ với L0: 4,8 * 2 = 9,6 mm."),
            make_sa(4, "Thông hiểu", "Một quả cầu kim loại có thể tích ban đầu 1000 cm3 ở 20°C. Khi nung nóng lên 120°C (tăng 100°C), thể tích quả cầu tăng thêm 3,6 cm3. Thể tích của quả cầu ở 120°C là bao nhiêu cm3?", "1003.6", "V = 1000 + 3,6 = 1003,6 cm3."),
            make_sa(5, "Vận dụng", "Khối lượng quả cầu ở câu trên là 2,7 kg (2700 g). Khối lượng riêng của quả cầu ở 20°C là bao nhiêu g/cm3?", "2.7", "D = 2700 / 1000 = 2,7 g/cm3 (đây là nhôm)."),
            make_sa(6, "Vận dụng", "Một thanh thép có diện tích tiết diện S = 0,001 m2. Khi bị nung nóng mà bị chặn cứng hai đầu, lực nén nhiệt xuất hiện được tính bằng F = E * S * α * Δt. Biết E = 2 . 10^11 N/m2, α = 1,2 . 10^-5 K^-1, Δt = 50°C. Lực nén sinh ra là bao nhiêu kiloniutơn (kN)?", "120", "F = 2e11 * 1e-3 * 1,2e-5 * 50 = 120 000 N = 120 kN.")
        ],
        [
            make_vdc(1, "Tuyến đường sắt Bắc - Nam sử dụng các đoạn thanh ray bằng thép tiêu chuẩn dài L0 = 25 m ở nhiệt độ mùa đông 15°C. Nhiệt độ mặt ray cao nhất vào trưa hè nắng gắt có thể lên tới 65°C (chênh lệch nhiệt độ cực đại Δt = 50°C). Biết hệ số nở dài của thép đường ray là α = 1,2 . 10^-5 K^-1. Để các thanh ray không bị chèn ép uốn cong vênh vào mùa hè, khe hở kỹ thuật tối thiểu cần chừa ra giữa hai đầu thanh ray khi lắp đặt ở 15°C là:", [
                "15 mm (1,5 cm)", "10 mm", "20 mm", "5 mm"
            ], 0, "ΔL = L0 * α * Δt = 25 * (1,2 . 10^-5) * 50 = 0,015 m = 15 mm."),
            make_vdc(2, "Một cây cầu dầm thép dài L0 = 500 m bắc qua sông được thi công ở nhiệt độ 20°C. Nhiệt độ môi trường trong năm biến thiên từ 5°C (mùa đông) đến 45°C (mùa hè). Cho hệ số nở dài của thép làm dầm cầu là α = 1,2 . 10^-5 K^-1. Biên độ co giãn chiều dài tối đa của toàn bộ cây cầu thép giữa hai mùa khắc nghiệt nhất trong năm là:", [
                "24 cm (0,24 m)", "12 cm", "48 cm", "6 cm"
            ], 0, "Độ biến thiên nhiệt độ cực đại: Δt = 45 - 5 = 40°C. Biên độ co giãn: ΔL = 500 * (1,2 . 10^-5) * 40 = 0,24 m = 24 cm."),
            make_vdc(3, "Một chiếc đai sắt tròn có đường kính trong d1 = 49,8 mm ở 20°C cần được lồng vào một trục bánh xe bằng thép có đường kính ngoài d2 = 50,0 mm. Cho hệ số nở dài của sắt là α = 1,2 . 10^-5 K^-1. Để lọt đai sắt vào trục bánh xe dễ dàng, cần nung nóng đai sắt lên nhiệt độ tối thiểu xấp xỉ bằng:", [
                "355°C", "200°C", "500°C", "280°C"
            ], 0, "Độ giãn nở đường kính: Δd = d2 - d1 = 50,0 - 49,8 = 0,2 mm. Δd = d1 * α * Δt => Δt = 0,2 / (49,8 * 1,2e-5) ≈ 334,7°C => t = 20 + 334,7 ≈ 354,7°C ≈ 355°C."),
            make_vdc(4, "Một thanh đồng và một thanh sắt ở 0°C có chiều dài ban đầu lần lượt là L0_đồng = 100 cm và L0_sắt = 100,5 cm. Biết hệ số nở dài của đồng là α_đồng = 1,7 . 10^-5 K^-1, của sắt là α_sắt = 1,2 . 10^-5 K^-1. Nhiệt độ t mà ở đó hai thanh có chiều dài bằng nhau là:", [
                "1000°C", "500°C", "800°C", "1200°C"
            ], 0, "L_đồng(t) = L_sắt(t) => 100*(1 + 1,7e-5*t) = 100,5*(1 + 1,2e-5*t) => 100 + 170e-5*t = 100,5 + 120,6e-5*t => 49,4e-5*t = 0,5 => t ≈ 1012°C ≈ 1000°C.")
        ]
    )

    # ĐỀ 2: Sự nở vì nhiệt của Chất lỏng & Hiện tượng dị thường của Nước
    exams[f"{l_id}_test2"] = meta(2,
        [
            make_mc(1, "Nhận biết", "Quy luật chung về sự nở vì nhiệt của chất lỏng là:", ["Chất lỏng nở ra khi nóng lên và co lại khi lạnh đi", "Chất lỏng co lại khi nóng lên", "Chất lỏng không đổi thể tích", "Chất lỏng biến thành chất rắn khi nung"], 0, "Chất lỏng nở ra khi nóng lên, co lại khi lạnh đi."),
            make_mc(2, "Nhận biết", "Các chất lỏng khác nhau (rượu, dầu, nước) có mức độ nở vì nhiệt như thế nào khi cùng tăng nhiệt độ?", ["Nở vì nhiệt khác nhau (rượu nở nhiều hơn dầu, dầu nở nhiều hơn nước)", "Nở vì nhiệt giống hệt nhau", "Không chất nào nở", "Đều nở gấp 10 lần chất khí"], 0, "Các chất lỏng khác nhau nở vì nhiệt khác nhau."),
            make_mc(3, "Nhận biết", "Hiện tượng dị thường của nước xảy ra trong khoảng nhiệt độ nào?", ["Từ 0°C đến 4°C", "Từ 4°C đến 100°C", "Từ 100°C trở lên", "Dưới 0°C"], 0, "Từ 0°C đến 4°C nước có hiện tượng nở nhiệt dị thường."),
            make_mc(4, "Nhận biết", "Khi tăng nhiệt độ từ 0°C lên 4°C, thể tích và khối lượng riêng của nước thay đổi như thế nào?", ["Thể tích co lại (giảm đi), khối lượng riêng tăng lên và đạt cực đại ở 4°C", "Thể tích tăng lên, khối lượng riêng giảm", "Thể tích không đổi", "Nước đóng băng cứng lại"], 0, "Nước co lại từ 0 đến 4°C, khối lượng riêng đạt cực đại 1000 kg/m3 ở 4°C."),
            make_mc(5, "Nhận biết", "Tại sao vào mùa đông ở các nước xứ lạnh, lớp băng đá luôn đóng ở trên mặt hồ còn ở đáy hồ nước vẫn giữ 4°C giúp cá sinh sống?", ["Vì băng đá (0°C) nhẹ hơn nước và nước ở 4°C có khối lượng riêng lớn nhất nên chìm xuống đáy", "Vì cá làm ấm nước ở đáy", "Vì bùn ở đáy sinh nhiệt", "Vì ánh sáng không chiếu tới đáy"], 0, "Nước 4°C nặng nhất chìm dưới đáy hồ, băng 0°C nhẹ hơn nổi trên mặt."),
            make_mc(6, "Nhận biết", "Khi đun nước trong một chiếc ấm, ta không nên đổ nước thật đầy ấm vì:", ["Khi đun nóng, nước nở ra tăng thể tích sẽ tràn ra ngoài gây tắt bếp nguy hiểm", "Để nước sôi nhanh hơn", "Ấm sẽ bị nứt đáy", "Nước sẽ không sôi được"], 0, "Nước nóng nở ra tràn ra ngoài gây nguy hiểm chập cháy tắt bếp."),
            make_mc(7, "Thông hiểu", "Nhiệt kế chất lỏng (nhiệt kế thủy ngân, nhiệt kế rượu) hoạt động dựa trên nguyên tắc:", ["Sự nở vì nhiệt của chất lỏng chứa trong bầu nhiệt kế", "Sự dẫn điện của chất lỏng", "Sự đổi màu hóa học", "Áp suất khí quyển"], 0, "Chất lỏng trong bầu nở ra dâng cao trong ống mao dẫn khi nhiệt độ tăng."),
            make_mc(8, "Thông hiểu", "Tại sao ống mao dẫn của nhiệt kế chất lỏng thường được làm rất nhỏ và hẹp?", ["Để khi chất lỏng trong bầu nở ra một ít thì cột chất lỏng dâng lên một đoạn dài dễ quan sát", "Để nhiệt kế nhẹ hơn", "Để tiết kiệm thủy ngân", "Để nhiệt kế khó vỡ"], 0, "Ống mao dẫn nhỏ làm tăng độ nhạy hiển thị chiều cao cột chất lỏng."),
            make_mc(9, "Thông hiểu", "Khi nhúng một bình cầu đựng đầy nước có cắm ống thủy tinh vào nước nóng, thoạt đầu mực nước trong ống tụt xuống một chút rồi sau đó mới dâng cao vì:", ["Bình thủy tinh tiếp xúc nước nóng trước nở ra trước, sau đó nước bên trong mới nóng lên và nở nhiều hơn bình", "Nước bị bay hơi mất", "Thủy tinh hút nước", "Bình bị nứt"], 0, "Vỏ bình nở trước làm tụt mực nước, sau đó nước nở nhiều hơn dâng cao vọt lên."),
            make_mc(10, "Thông hiểu", "Người ta không đóng nước ngọt có ga đầy ắp sát nút chai thủy tinh mà luôn để lại một khoảng trống nhỏ ở cổ chai vì:", ["Để khi nhiệt độ môi trường tăng lên, chất lỏng nở ra không làm bật nắp hoặc nổ vỡ chai", "Để người uống dễ mở", "Để tiết kiệm nước ngọt", "Để khí ga không thoát ra"], 0, "Khoảng trống dự phòng cho sự giãn nở nhiệt của chất lỏng."),
            make_mc(11, "Thông hiểu", "Nếu đặt một chai nước ngọt thủy tinh đầy kín vào ngăn đá tủ lạnh (-18°C) thì sau một thời gian chai có thể bị nứt vỡ vì:", ["Nước khi đóng băng thành đá ở 0°C bị tăng thể tích bất thường (nở ra khi đông đặc)", "Thủy tinh bị co lại quá nhiều", "Khí ga trong chai nổ", "Đá hút vỡ thủy tinh"], 0, "Nước đóng băng thể tích tăng lên khoảng 9% làm vỡ chai thủy tinh."),
            make_mc(12, "Thông hiểu", "Tại sao người ta không dùng nước làm chất lỏng đo nhiệt độ trong các nhiệt kế thông thường?", ["Vì nước nở nhiệt không đều (co lại từ 0°C đến 4°C) và khoảng đo nhiệt độ hẹp (đóng băng ở 0°C, sôi ở 100°C)", "Vì nước quá đắt tiền", "Vì nước không màu khó nhìn", "Vì nước dẫn điện"], 0, "Hiện tượng dị thường ở 0-4°C làm nhiệt kế nước không chia độ chuẩn xác được.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về sự nở vì nhiệt của các chất lỏng thông thường đề 2:", [
                ("a", "Rượu nở vì nhiệt nhiều hơn dầu hỏa khi cùng tăng một khoảng nhiệt độ.", True),
                ("b", "Dầu hỏa nở vì nhiệt nhiều hơn nước cất khi cùng chịu độ tăng nhiệt độ.", True),
                ("c", "Tất cả các chất lỏng đều có hệ số nở nhiệt hoàn toàn bằng nhau.", False),
                ("d", "Khối lượng riêng của chất lỏng thông thường giảm đi khi nhiệt độ của nó tăng lên.", True)
            ], "Các chất lỏng khác nhau nở vì nhiệt khác nhau."),
            make_tf(2, "Thông hiểu", "Về tính chất đặc biệt dị thường của nước đề 2:", [
                ("a", "Khi đun nóng nước từ 0°C lên 4°C, thể tích của nước bị co lại.", True),
                ("b", "Ở 4°C, nước nguyên chất có khối lượng riêng lớn nhất đạt đúng 1000 kg/m3.", True),
                ("c", "Khi hạ nhiệt độ từ 4°C xuống 0°C, nước lại nở ra tăng thể tích.", True),
                ("d", "Khối lượng riêng của nước đá ở 0°C lớn hơn khối lượng riêng của nước lỏng ở 0°C.", False)
            ], "Khối lượng riêng của đá (917 kg/m3) nhỏ hơn nước lỏng nên đá nổi trên mặt nước."),
            make_tf(3, "Thông hiểu", "Về nguyên tắc hoạt động của các loại nhiệt kế chất lỏng đề 2:", [
                ("a", "Nhiệt kế thủy ngân có thang đo rộng từ -39°C đến khoảng 357°C.", True),
                ("b", "Nhiệt kế rượu thường dùng để đo nhiệt độ môi trường ở các vùng xứ lạnh băng tuyết vì rượu đóng băng ở -114°C.", True),
                ("c", "Bầu chứa chất lỏng càng lớn và ống mao dẫn càng hẹp thì nhiệt kế càng nhạy.", True),
                ("d", "Chất lỏng trong nhiệt kế dâng lên hay hạ xuống là do áp suất khí quyển ép vào bầu.", False)
            ], "Chất lỏng dâng lên do sự dãn nở vì nhiệt tự thân của chất lỏng đó."),
            make_tf(4, "Thông hiểu", "Về các sự cố nhiệt liên quan đến chất lỏng trong đời sống đề 2:", [
                ("a", "Bình xăng xe máy đổ quá đầy nắp khi để ngoài trời nắng gắt có thể bị trào xăng gây cháy nổ.", True),
                ("b", "Lon nước ngọt có ga để trong ngăn đá tủ lạnh có nguy cơ phát nổ do nước ngọt đóng băng nở thể tích.", True),
                ("c", "Dầu nhờn bôi trơn động cơ xe máy bị loãng ra (giảm độ nhớt) khi động cơ nóng lên.", True),
                ("d", "Đun nước trong nồi đậy vung kín mít không có lỗ thoát hơi sẽ làm giảm nguy cơ trào nước.", False)
            ], "Vung kín không lỗ thoát làm tăng áp suất và làm nước trào phụt mạnh hơn.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một bình chứa 1000 cm3 cồn ở 20°C. Khi tăng lên 50°C (tăng 30°C), thể tích cồn tăng thêm 33 cm3. Độ tăng thể tích tương đối trên mỗi độ C là bao nhiêu cm3/°C?", "1.1", "33 / 30 = 1,1 cm3/°C."),
            make_sa(2, "Thông hiểu", "Một lít nước (1000 cm3) ở 20°C có khối lượng 1000 g. Khi nung nóng lên 80°C, thể tích tăng thành 1029 cm3. Khối lượng riêng của nước ở 80°C là bao nhiêu g/cm3? (Làm tròn đến 3 chữ số thập phân).", "0.972", "D = 1000 / 1029 ≈ 0,972 g/cm3."),
            make_sa(3, "Thông hiểu", "Hệ số nở thể tích của rượu là 0,0011 K^-1, của nước là 0,00021 K^-1. Rượu nở vì nhiệt nhiều gấp khoảng mấy lần nước? (Làm tròn đến hàng đơn vị).", "5", "0,0011 / 0,00021 ≈ 5,2 ≈ 5 lần."),
            make_sa(4, "Thông hiểu", "Khối lượng riêng của nước ở 4°C là 1000 kg/m3. Một khối nước đá có thể tích 1 m3 có khối lượng 917 kg. Khối lượng riêng của nước đá là bao nhiêu kg/m3?", "917", "D_đá = 917 / 1 = 917 kg/m3."),
            make_sa(5, "Vận dụng", "Một bình thủy tinh chứa đầy 500 cm3 dầu hỏa ở 10°C. Khi nhiệt độ tăng lên 60°C (tăng 50°C), lượng dầu tràn ra khỏi bình là 22 cm3 (bỏ qua nở nhiệt của thủy tinh). Độ nở thể tích của 1 cm3 dầu khi tăng 1°C là bao nhiêu phần triệu (10^-6)?", "880", "β = 22 / (500 * 50) = 0,00088 = 880 . 10^-6 K^-1."),
            make_sa(6, "Vận dụng", "Một tảng băng trôi nổi trên biển. Khối lượng riêng của băng là 920 kg/m3, của nước biển là 1025 kg/m3. Phần thể tích chìm dưới nước biển chiếm bao nhiêu phần trăm (%) thể tích tảng băng? (Làm tròn đến hàng đơn vị).", "90", "V_chim / V_tong = 920 / 1025 ≈ 0,8975 ≈ 90%.")
        ],
        [
            make_vdc(1, "Một bình đong bằng thủy tinh có dung tích V0 = 1000 cm3 ở 20°C chứa đầy dầu hỏa. Khi nhiệt độ của cả bình và dầu tăng lên 70°C (tăng Δt = 50°C), có một lượng dầu bị tràn ra ngoài. Cho biết hệ số nở thể tích của dầu hỏa là β_dầu = 1,0 . 10^-3 K^-1 và hệ số nở thể tích của thủy tinh là β_tt = 2,7 . 10^-5 K^-1. Thể tích dầu hỏa thực tế tràn ra khỏi bình là:", [
                "48,65 cm3", "50,0 cm3", "1,35 cm3", "25,5 cm3"
            ], 0, "ΔV_dau = 1000 * (1,0 . 10^-3) * 50 = 50 cm3. ΔV_binh = 1000 * (2,7 . 10^-5) * 50 = 1,35 cm3. Thể tích tràn: V_tran = ΔV_dau - ΔV_binh = 50 - 1,35 = 48,65 cm3."),
            make_vdc(2, "Một ống nhiệt kế thủy ngân có bầu chứa thể tích V0 = 0,5 cm3 ở 0°C. Phần ống mao dẫn hình trụ có đường kính trong d = 0,1 mm (tiết diện S = π * d^2 / 4 ≈ 7,854 . 10^-5 cm2). Biết hệ số nở thể tích biểu kiến của thủy ngân trong thủy tinh là β' = 1,8 . 10^-4 K^-1. Khoảng cách giữa hai vạch chia 0°C và 100°C trên thang đo nhiệt kế (chiều dài 100 độ) là:", [
                "11,46 cm", "5,73 cm", "22,9 cm", "1,15 cm"
            ], 0, "Độ tăng thể tích thủy ngân khi tăng 100°C: ΔV = V0 * β' * 100 = 0,5 * (1,8 . 10^-4) * 100 = 0,009 cm3. Chiều dài cột dâng: L = ΔV / S = 0,009 / (7,854 . 10^-5) ≈ 114,6 mm = 11,46 cm."),
            make_vdc(3, "Một tảng băng hình hộp chữ nhật nổi trên mặt hồ nước ngọt. Khối lượng riêng của băng là D_băng = 917 kg/m3 và của nước hồ là D_nước = 1000 kg/m3. Phần tảng băng nhô lên khỏi mặt nước có thể tích V_nổi = 25 m3. Tổng thể tích và khối lượng của toàn bộ tảng băng này xấp xỉ bằng:", [
                "V_tổng ≈ 301,2 m3; m ≈ 276,2 tấn", "V_tổng ≈ 150 m3; m ≈ 137,5 tấn", "V_tổng ≈ 500 m3; m ≈ 450 tấn", "V_tổng ≈ 250 m3; m ≈ 229 tấn"
            ], 0, "V_chim / V_tong = D_bang / D_nuoc = 917 / 1000 = 0,917 => V_noi = V_tong * (1 - 0,917) = 0,083 * V_tong = 25 m3 => V_tong = 25 / 0,083 ≈ 301,2 m3. m = 301,2 * 917 ≈ 276 200 kg ≈ 276,2 tấn."),
            make_vdc(4, "Một bình thủy tinh dung tích 2 lít chứa đầy nước ở 4°C. Khi đun nóng bình nước lên 80°C thì có một lượng nước tràn ra. Sau đó, làm nguội bình nước này từ 80°C về đúng 4°C thì thể tích nước còn lại trong bình so với dung tích ban đầu của bình sẽ:", [
                "Bị thiếu hụt đúng bằng thể tích lượng nước đã tràn ra lúc đun nóng", "Vẫn đầy khít bình", "Tràn thêm lần nữa", "Tăng gấp đôi thể tích"
            ], 0, "Lượng nước tràn ra ở 80°C đã thoát khỏi bình vĩnh viễn, khi làm nguội về 4°C khối lượng nước còn lại ít hơn nên co lại làm hụt thể tích đúng bằng phần đã tràn.")
        ]
    )

    # ĐỀ 3: Sự nở vì nhiệt của Chất khí & Ứng dụng Băng kép (Rơle nhiệt)
    p1_t3 = [
            make_mc(1, "Nhận biết", "Quy luật nở vì nhiệt của các chất khí khác nhau (không khí, khí oxi, khí hiđro) là:", ["Các chất khí khác nhau nở vì nhiệt giống nhau", "Các chất khí khác nhau nở vì nhiệt khác nhau", "Khí nhẹ nở nhiều hơn khí nặng", "Chất khí không nở vì nhiệt"], 0, "Điểm đặc biệt: Mọi chất khí khác nhau đều nở vì nhiệt giống nhau."),
            make_mc(2, "Nhận biết", "So sánh sự nở vì nhiệt của ba trạng thái vật chất (rắn, lỏng, khí) khi cùng tăng nhiệt độ:", ["Chất khí nở nhiều hơn chất lỏng, chất lỏng nở nhiều hơn chất rắn", "Chất rắn nở nhiều nhất", "Chất lỏng nở nhiều nhất", "Cả ba trạng thái nở như nhau"], 0, "Thứ tự nở nhiệt: Khí > Lỏng > Rắn."),
            make_mc(3, "Nhận biết", "Cấu tạo của một băng kép (thanh lưỡng kim) gồm có:", ["Hai thanh kim loại có bản chất khác nhau được tán chặt dọc theo chiều dài", "Hai thanh đồng giống hệt nhau", "Một thanh kim loại bọc nhựa", "Hai thanh thủy tinh ghép đôi"], 0, "Hai thanh kim loại khác nhau tán chặt vào nhau."),
            make_mc(4, "Nhận biết", "Khi bị nung nóng, một băng kép gồm thanh đồng và thanh thép sẽ bị uốn cong về phía nào?", ["Uốn cong về phía thanh thép vì đồng nở dài nhiều hơn thép", "Uốn cong về phía thanh đồng", "Vẫn thẳng đứng", "Bị xoắn tròn"], 0, "Đồng nở dài nhiều hơn thép nên uốn cong về phía thanh thép ngắn hơn."),
            make_mc(5, "Nhận biết", "Khi bị làm lạnh, băng kép đồng - thép nói trên sẽ bị uốn cong về phía nào?", ["Uốn cong về phía thanh đồng vì đồng co lại nhiều hơn thép", "Uốn cong về phía thanh thép", "Thẳng đứng", "Không bị cong"], 0, "Lạnh thì đồng co nhiều hơn nên cong về phía thanh đồng."),
            make_mc(6, "Nhận biết", "Thiết bị nào sau đây trong đời sống ứng dụng hoạt động uốn cong của băng kép?", ["Rơle nhiệt tự động ngắt điện trong bàn là, nồi cơm điện", "Quạt trần", "Bóng đèn sợi đốt", "Chuông điện"], 0, "Băng kép dùng làm rơle nhiệt đóng ngắt tự động."),
            make_mc(7, "Thông hiểu", "Khi một quả bóng bàn bị bẹp móp nhưng chưa bị rách thủng, ta nhúng quả bóng vào nước nóng thì quả bóng phồng trở lại vì:", ["Không khí bên trong quả bóng nóng lên, nở ra tạo áp suất đẩy vỏ bóng phồng lên", "Vỏ bóng hút nước", "Nước nóng làm bóng mềm ra", "Nước chui vào trong bóng"], 0, "Không khí trong bóng nở nhiệt sinh áp suất đẩy vỏ phồng tròn lại."),
            make_mc(8, "Thông hiểu", "Vì sao không nên bơm bánh xe đạp hoặc xe máy quá căng vào mùa hè nắng gắt?", ["Không khí bên trong săm xe nở nhiệt làm tăng áp suất có thể gây nổ lốp xe", "Bánh xe sẽ bị mòn nhanh hơn", "Xe chạy quá nhanh", "Bánh xe bị co lại"], 0, "Không khí trong săm nở nhiệt làm nổ lốp xe."),
            make_mc(9, "Thông hiểu", "Trong thí nghiệm áp hai bàn tay vào bình cầu có cắm ống thủy tinh chứa giọt nước màu, giọt nước màu chuyển động ra phía ngoài chứng tỏ:", ["Không khí trong bình cầu nóng lên nở ra đẩy giọt nước màu dịch chuyển", "Không khí trong bình co lại", "Tay hút giọt nước", "Thủy tinh co lại"], 0, "Không khí nhận nhiệt từ bàn tay nở ra đẩy giọt nước màu."),
            make_mc(10, "Thông hiểu", "Khinh khí cầu bay lên được trong không khí là nhờ nguyên lí:", ["Đốt nóng không khí bên trong làm khí nở ra, khối lượng riêng giảm đi nhẹ hơn không khí xung quanh", "Quạt gió đẩy lên", "Khí bên trong bị đóng băng", "Lực hút của Mặt Trời"], 0, "Không khí nóng nhẹ hơn không khí lạnh sinh lực nâng Archimedes."),
            make_mc(11, "Thông hiểu", "Tại sao nút chai thủy tinh để lâu ngày bị kẹt chặt, người ta có thể hơ nóng cổ chai để mở nút?", ["Cổ chai bằng thủy tinh nóng lên nở to ra giúp rút nút ra dễ dàng", "Nút chai co lại", "Nước bên trong bốc hơi", "Làm lỏng chất kết dính"], 0, "Hơ nóng cổ chai làm miệng chai nở to ra trước."),
            make_mc(12, "Thông hiểu", "Rơle nhiệt trong bàn là điện hoạt động tự động giữ nhiệt độ ổn định bằng cách:", ["Băng kép uốn cong làm hở tiếp điểm ngắt điện khi quá nóng, khi nguội thẳng lại đóng điện tiếp tục", "Đo dòng điện bằng ampe kế", "Dùng đồng hồ hẹn giờ", "Nhờ người dùng bấm nút"], 0, "Băng kép tự uốn cong đóng ngắt tiếp điểm theo nhiệt độ.")
    ]

    p2_t3 = [
        make_tf(1, "Thông hiểu", "Về các đặc tính nở vì nhiệt của chất khí đề 3:", [
            ("a", "Chất khí nở ra khi nóng lên và co lại khi lạnh đi.", True),
            ("b", "Các chất khí khác nhau (oxi, nitơ, cacbonic) nở vì nhiệt hoàn toàn giống nhau.", True),
            ("c", "Chất khí nở vì nhiệt nhiều hơn chất lỏng và nhiều hơn chất rắn rất nhiều lần.", True),
            ("d", "Khối lượng riêng của chất khí tăng lên khi nhiệt độ của nó tăng cao.", False)
        ], "Khi nóng lên, thể tích khí tăng làm khối lượng riêng giảm đi."),
        make_tf(2, "Thông hiểu", "Về cấu tạo và nguyên lí uốn cong của băng kép đề 3:", [
            ("a", "Băng kép hoạt động dựa trên sự nở vì nhiệt khác nhau của hai kim loại thành phần.", True),
            ("b", "Khi nung nóng, băng kép luôn uốn cong về phía kim loại có độ nở nhiệt nhỏ hơn.", True),
            ("c", "Khi làm lạnh dưới nhiệt độ ban đầu, băng kép sẽ uốn cong về phía kim loại có độ nở nhiệt lớn hơn.", True),
            ("d", "Nếu ghép hai thanh kim loại hoàn toàn giống nhau thì băng kép vẫn uốn cong bình thường.", False)
        ], "Hai kim loại giống nhau nở bằng nhau nên thanh luôn giữ thẳng, không uốn cong."),
        make_tf(3, "Thông hiểu", "Về ứng dụng thực tế của sự nở vì nhiệt chất khí và băng kép đề 3:", [
            ("a", "Nồi cơm điện tự động bật nút chuyển sang chế độ ủ ấm nhờ rơle nhiệt cảm ứng.", True),
            ("b", "Hệ thống báo cháy tự động dùng băng kép đóng mạch chuông reo khi nhiệt độ phòng tăng cao.", True),
            ("c", "Bình xịt côn trùng để gần bếp gas đang đun nấu có nguy cơ phát nổ do khí bên trong tăng áp suất.", True),
            ("d", "Khí nóng luôn có xu hướng chìm xuống đáy phòng do khối lượng riêng tăng lên.", False)
        ], "Khí nóng nở ra nhẹ hơn luôn bốc lên cao."),
        make_tf(4, "Thông hiểu", "Về so sánh và đánh giá các trạng thái nở nhiệt đề 3:", [
            ("a", "Độ nở thể tích của 1 lít không khí khi tăng 1°C lớn hơn độ nở thể tích của 1 lít nước khoảng hơn 10 lần.", True),
            ("b", "Không khí là chất dẫn nhiệt kém nhưng nở vì nhiệt rất mạnh mẽ.", True),
            ("c", "Sự nở vì nhiệt của chất khí trong xi lanh động cơ xe máy sinh công đẩy pít-tông sinh lực chuyển động.", True),
            ("d", "Chất khí bị nung nóng trong bình kín không thay đổi áp suất lên thành bình.", False)
        ], "Trong bình kín thể tích không đổi, nung nóng làm áp suất khí tăng vọt.")
    ]

    p3_t3 = [
        make_sa(1, "Thông hiểu", "Một quả bóng chứa 2,0 lít không khí ở 20°C. Khi nung nóng lên 50°C trong điều kiện áp suất không đổi, thể tích bóng tăng lên thành 2,2 lít. Độ tăng thể tích của quả bóng là bao nhiêu lít?", "0.2", "2,2 - 2,0 = 0,2 lít."),
        make_sa(2, "Thông hiểu", "Một bình kín chứa khí ở áp suất 1,0 atm và 27°C (300 K). Khi nung nóng lên 127°C (400 K), áp suất khí trong bình tăng lên bao nhiêu atm? (Làm tròn đến 2 chữ số thập phân).", "1.33", "p2 = p1 * (T2 / T1) = 1,0 * (400 / 300) ≈ 1,33 atm."),
        make_sa(3, "Thông hiểu", "Hệ số nở thể tích của mọi chất khí ở 0°C đều xấp xỉ bằng 1 / 273 (K^-1). Một thể tích 273 cm3 không khí ở 0°C khi tăng thêm 1°C sẽ tăng thêm bao nhiêu cm3?", "1", "ΔV = 273 * (1 / 273) * 1 = 1 cm3."),
        make_sa(4, "Thông hiểu", "Một băng kép đồng - thép dài 20 cm ở 20°C. Khi nung nóng lên 100°C, thanh đồng nở dài thêm 0,27 mm, thanh thép nở dài thêm 0,19 mm. Thanh đồng nở dài hơn thanh thép bao nhiêu milimét (mm)?", "0.08", "0,27 - 0,19 = 0,08 mm."),
        make_sa(5, "Vận dụng", "Một khinh khí cầu có thể tích V = 500 m3 chứa không khí nóng có khối lượng riêng 1,0 kg/m3. Không khí lạnh bên ngoài có khối lượng riêng 1,2 kg/m3. Lực nâng Archimedes tác dụng lên khinh khí cầu là bao nhiêu Niutơn (N)? (Lấy g = 10 m/s2).", "6000", "F_A = d_ngoai * V = (1,2 * 10) * 500 = 6000 N."),
        make_sa(6, "Vận dụng", "Trọng lượng của khí nóng bên trong quả cầu ở câu trên là P = (1,0 * 10) * 500 = 5000 N. Lực nâng có ích cực đại (tải trọng nâng tối đa của khinh khí cầu) là bao nhiêu Niutơn (N)?", "1000", "F_nang = F_A - P = 6000 - 5000 = 1000 N.")
    ]

    p4_t3 = [
        make_vdc(1, "Một bình xịt bọt cạo râu bằng kim loại chứa khí nén ở áp suất p1 = 2,5 atm ở nhiệt độ phòng 25°C (298 K). Vỏ bình có thể chịu được áp suất tối đa p_max = 5,0 atm trước khi bị nổ tung. Nếu vô tình ném bình xịt này vào một đống lửa rác đang cháy thì nhiệt độ tối thiểu mà bình xịt sẽ phát nổ là:", [
            "323°C (khoảng 596 K)", "250°C", "500°C", "150°C"
        ], 0, "Quá trình đẳng tích: p1 / T1 = p_max / T_max => T_max = 298 * (5,0 / 2,5) = 596 K => t_max = 596 - 273 = 323°C."),
        make_vdc(2, "Một khinh khí cầu du lịch có thể tích khí cầu V = 2400 m3 chứa không khí được đốt nóng bởi vòi phun gas. Không khí môi trường xung quanh có nhiệt độ 20°C và khối lượng riêng D0 = 1,20 kg/m3. Tổng khối lượng của vỏ khí cầu, giỏ mây và hành khách là m_tai = 600 kg. Lấy g = 10 m/s2. Để khinh khí cầu bắt đầu nhấc mình bay lên khỏi mặt đất, khối lượng riêng tối đa của luồng không khí nóng bên trong quả cầu phải đạt:", [
            "0,95 kg/m3", "1,00 kg/m3", "0,80 kg/m3", "1,10 kg/m3"
        ], 0, "Lực đẩy F_A = D0 * g * V = 1,20 * 10 * 2400 = 28 800 N. Trọng lượng tổng cộng P_tong = (m_tai + m_khi) * g = 6000 + D_khi * 2400 * 10 = 6000 + 24 000 * D_khi. Để bay lên: P_tong <= F_A => 24 000 * D_khi <= 22 800 => D_khi <= 22800 / 24000 = 0,95 kg/m3."),
        make_vdc(3, "Một rơle nhiệt của bàn là điện sử dụng một băng kép thẳng dài L0 = 10 cm gồm lá đồng và lá thép dày cùng d = 0,5 mm (tổng độ dày băng kép là 2d = 1 mm) được gắn cố định một đầu. Cho biết hệ số nở dài của đồng là α1 = 1,7 . 10^-5 K^-1 và của thép là α2 = 1,2 . 10^-5 K^-1. Khi nhiệt độ của bàn là tăng thêm Δt = 150°C, đầu tự do của băng kép uốn cong làm tiếp điểm dịch chuyển một đoạn xấp xỉ bằng:", [
            "1,125 mm", "2,5 mm", "0,5 mm", "5,0 mm"
        ], 0, "Độ dịch chuyển đầu tự do của băng kép gắn 1 đầu: δ ≈ (3 * (α1 - α2) * Δt * L0^2) / (4 * d) = (3 * 0,5e-5 * 150 * 0,1^2) / (4 * 0,5e-3) = (2,25e-5 * 10^-2) / (2e-3) = 2,25e-7 / 2e-3 ≈ 0,001125 m = 1,125 mm."),
        make_vdc(4, "Một ống thủy tinh hình trụ kín hai đầu nằm ngang, chính giữa có một giọt thủy ngân dài 4 cm ngăn cách hai khối không khí giống hệt nhau có cùng chiều dài l0 = 40 cm ở nhiệt độ 27°C (300 K). Nếu nung nóng khối khí bên trái lên 57°C (330 K) và giữ nguyên khối khí bên phải ở 27°C thì giọt thủy ngân sẽ dịch chuyển sang bên phải một đoạn x bằng:", [
            "1,90 cm", "3,80 cm", "0,95 cm", "4,0 cm"
        ], 0, "Khi cân bằng, áp suất hai bên bằng nhau: p' = p1' = p2'. Với thể tích V ~ l: l1 / T1 = l2 / T2 => (40 + x) / 330 = (40 - x) / 300 => 300*(40 + x) = 330*(40 - x) => 630*x = 1200 => x = 1200 / 630 ≈ 1,905 cm ≈ 1,90 cm.")
    ]

    exams[f"{l_id}_test3"] = meta(3, p1_t3, p2_t3, p3_t3, p4_t3)

    return exams
