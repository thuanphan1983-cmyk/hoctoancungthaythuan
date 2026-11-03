# -*- coding: utf-8 -*-
"""
Dữ liệu 3 đề thi độc lập Bài 28: Sự truyền nhiệt (phys8_c6_b28)
- Đề 1: Dẫn nhiệt ở chất rắn và vật liệu cách nhiệt
- Đề 2: Đối lưu ở chất lỏng, chất khí và hiện tượng tự nhiên
- Đề 3: Bức xạ nhiệt, bình thủy và ứng dụng tổng hợp
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

def get_b28_exams():
    exams = {}
    ch_id = "phys8_c6"
    ch_title = "Chương VI: Nhiệt"
    l_id = "phys8_c6_b28"
    l_name = "Bài 28: Sự truyền nhiệt"

    def meta(t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # ĐỀ 1: Dẫn nhiệt ở chất rắn & Vật liệu cách nhiệt
    exams[f"{l_id}_test1"] = meta(1,
        [
            make_mc(1, "Nhận biết", "Dẫn nhiệt là hình thức truyền nhiệt chủ yếu xảy ra ở trạng thái nào của vật chất?", ["Chất rắn (đặc biệt là kim loại)", "Chân không hoàn toàn", "Chất khí", "Chất lỏng ở nhiệt độ cao"], 0, "Dẫn nhiệt là hình thức truyền nhiệt chủ yếu ở chất rắn."),
            make_mc(2, "Nhận biết", "Trong các kim loại sau đây, kim loại nào dẫn nhiệt tốt nhất?", ["Bạc (Ag)", "Đồng (Cu)", "Nhôm (Al)", "Sắt (Fe)"], 0, "Bạc dẫn nhiệt tốt nhất, tiếp theo là đồng và nhôm."),
            make_mc(3, "Nhận biết", "Vật liệu nào sau đây dẫn nhiệt kém (vật liệu cách nhiệt tốt)?", ["Gỗ khô, xốp, sứ", "Thanh đồng", "Lá nhôm", "Thỏi sắt"], 0, "Gỗ, xốp, sứ dẫn nhiệt rất kém."),
            make_mc(4, "Nhận biết", "Tại sao đáy xoong nồi thường làm bằng kim loại (nhôm, inox, đồng) còn quai nồi làm bằng nhựa cách nhiệt?", ["Kim loại dẫn nhiệt tốt để nấu thức ăn nhanh chín, quai nhựa dẫn nhiệt kém để cầm không bị bỏng", "Kim loại nhẹ hơn nhựa", "Để trang trí đẹp", "Nhựa dễ tan chảy"], 0, "Đáy nồi cần dẫn nhiệt tốt, quai cầm cần cách nhiệt an toàn."),
            make_mc(5, "Nhận biết", "Chất lỏng và chất khí nói chung có khả năng dẫn nhiệt như thế nào?", ["Dẫn nhiệt rất kém", "Dẫn nhiệt rất tốt tương đương kim loại", "Dẫn nhiệt tốt hơn chất rắn", "Không bao giờ dẫn nhiệt"], 0, "Chất lỏng và khí dẫn nhiệt kém."),
            make_mc(6, "Nhận biết", "Vào mùa đông, khi chạm tay vào thanh sắt ta thấy lạnh hơn chạm vào thanh gỗ cùng nhiệt độ trong phòng vì:", ["Sắt dẫn nhiệt tốt nên nhiệt lượng từ tay truyền nhanh sang sắt, còn gỗ dẫn nhiệt kém", "Sắt có nhiệt độ thấp hơn gỗ", "Gỗ tự sinh ra nhiệt", "Sắt bị nhiễm từ"], 0, "Sắt dẫn nhiệt nhanh làm tay mất nhiệt nhanh cảm thấy lạnh hơn."),
            make_mc(7, "Thông hiểu", "Vì sao mùa đông mặc nhiều áo mỏng lại ấm hơn mặc một chiếc áo dày có cùng khối lượng?", ["Vì giữa các lớp áo mỏng có các lớp không khí tĩnh cách nhiệt rất tốt", "Áo mỏng có màu đẹp hơn", "Áo mỏng nhẹ hơn", "Nhiều áo tạo lực ép lớn"], 0, "Lớp không khí tĩnh giữa các áo dẫn nhiệt rất kém giữ nhiệt tốt."),
            make_mc(8, "Thông hiểu", "Khi đun nóng một đầu thanh kim loại, nhiệt lượng truyền dần về đầu kia là do:", ["Các nguyên tử ở đầu nóng dao động mạnh truyền xung động cho các nguyên tử lân cận", "Dòng kim loại lỏng chảy sang", "Gió thổi mang nhiệt", "Ánh sáng chiếu dọc theo thanh"], 0, "Cơ chế truyền dao động nhiệt giữa các hạt vi mô."),
            make_mc(9, "Thông hiểu", "Để giữ cho nước đá lâu tan vào mùa hè, người ta thường vùi các tảng đá vào lớp mùn cưa hoặc trấu vì:", ["Mùn cưa chứa nhiều không khí dẫn nhiệt rất kém ngăn nhiệt từ môi trường truyền vào đá", "Mùn cưa làm đá lạnh thêm", "Mùn cưa hút hết nước", "Mùn cưa phản xạ ánh sáng"], 0, "Mùn cưa và trấu là vật liệu cách nhiệt rất tốt."),
            make_mc(10, "Thông hiểu", "Một ống nghiệm đựng nước có một cục sáp nhỏ gắn ở đáy ống nghiệm. Dùng đèn cồn đun nóng phần trên miệng ống nghiệm, nước sôi ở trên nhưng cục sáp ở đáy vẫn chưa tan vì:", ["Nước là chất dẫn nhiệt kém", "Sáp không bao giờ tan", "Nước ở trên không thể truyền nhiệt", "Cục sáp tự làm mát"], 0, "Nước dẫn nhiệt kém, đun ở miệng thì nhiệt không dẫn xuống đáy được."),
            make_mc(11, "Thông hiểu", "Vật liệu xốp polystyrene (xốp EPS) được dùng rộng rãi làm thùng giữ lạnh vì:", ["Có cấu trúc bọt khí kín chiếm hơn 95% thể tích giúp cách nhiệt tuyệt hảo", "Xốp có nhiệt độ 0°C", "Xốp tự tạo ra băng tuyết", "Xốp cứng như thép"], 0, "Không khí bị giam trong bọt xốp cách nhiệt cực tốt."),
            make_mc(12, "Thông hiểu", "Khi rót nước sôi vào cốc thủy tinh dày thì cốc dễ vỡ hơn rót vào cốc thủy tinh mỏng vì:", ["Thủy tinh dẫn nhiệt kém, lớp trong cốc nở ra trước trong khi lớp ngoài chưa kịp nở gây ứng suất nứt vỡ", "Cốc dày giòn hơn", "Cốc mỏng đàn hồi tốt hơn", "Nước sôi ăn mòn thủy tinh dày"], 0, "Thủy tinh dẫn nhiệt kém gây giãn nở không đồng đều giữa mặt trong và mặt ngoài.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về bản chất và đặc điểm của hiện tượng dẫn nhiệt đề 1:", [
                ("a", "Dẫn nhiệt là sự truyền động năng nhiệt từ hạt phân tử này sang hạt phân tử khác khi có chênh lệch nhiệt độ.", True),
                ("b", "Trong chân không hoàn toàn, hiện tượng dẫn nhiệt diễn ra mạnh mẽ nhất.", False),
                ("c", "Kim loại dẫn nhiệt tốt nhất trong các chất rắn nhờ có các electron tự do tham gia truyền năng lượng.", True),
                ("d", "Khả năng dẫn nhiệt của các chất rắn khác nhau là hoàn toàn như nhau.", False)
            ], "Chân không không có hạt vật chất nên không có dẫn nhiệt."),
            make_tf(2, "Thông hiểu", "Về ứng dụng dẫn nhiệt và cách nhiệt trong đời sống đề 1:", [
                ("a", "Bát sứ đựng canh nóng giúp người cầm đỡ bị bỏng tay hơn so with bát kim loại.", True),
                ("b", "Tường nhà xây bằng gạch rỗng hai lớp có khả năng cách nhiệt chống nóng mùa hè tốt hơn tường gạch đặc cùng độ dày.", True),
                ("c", "Lông vũ của loài chim xù lên vào mùa đông giúp nhốt nhiều không khí tĩnh để giữ ấm cơ thể.", True),
                ("d", "Người ta làm vỏ tủ lạnh bằng kim loại đặc nguyên khối không có lớp xốp cách nhiệt.", False)
            ], "Vỏ tủ lạnh bắt buộc phải có lớp xốp cách nhiệt polyurethane dày."),
            make_tf(3, "Thông hiểu", "Về các thí nghiệm kiểm chứng khả năng dẫn nhiệt đề 1:", [
                ("a", "Gắn các que diêm bằng sáp dọc theo thanh đồng và thanh thủy tinh rồi nung nóng một đầu, các que diêm trên thanh đồng rụng trước.", True),
                ("b", "Thí nghiệm trên chứng minh đồng dẫn nhiệt tốt hơn thủy tinh nhiều lần.", True),
                ("c", "Nước ở đáy ống nghiệm không sôi khi đun ở miệng ống chứng minh nước dẫn nhiệt rất tốt.", False),
                ("d", "Không khí ẩm dẫn nhiệt tốt hơn một chút so với không khí khô hoàn toàn.", True)
            ], "Nước ở đáy không sôi chứng minh nước dẫn nhiệt kém."),
            make_tf(4, "Thông hiểu", "Về quy tắc an toàn nhiệt chống bỏng trong gia đình đề 1:", [
                ("a", "Luôn sử dụng găng tay vải lót cách nhiệt dày khi bê xoong nồi vừa đun sôi từ bếp ra.", True),
                ("b", "Mở nắp vung nồi canh đang sôi theo hướng phả thẳng hơi nước nóng vào mặt.", False),
                ("c", "Dùng đũa tre hoặc muôi gỗ đảo thức ăn trên chảo nóng để tránh nhiệt truyền lên tay.", True),
                ("d", "Khi bị bỏng nhiệt nhẹ, ngâm ngay vùng da bị bỏng vào nước sạch mát trong 15-20 phút.", True)
            ], "Mở vung nồi phải nghiêng về phía xa mặt tránh bỏng hơi nước.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một thanh kim loại dài 0,5 m có độ chênh lệch nhiệt độ giữa hai đầu là 40°C. Gradien nhiệt độ dọc theo thanh là bao nhiêu °C/m?", "80", "Grad = 40 / 0,5 = 80 °C/m."),
            make_sa(2, "Thông hiểu", "Một tấm tường xốp cách nhiệt dày 0,05 m có hệ số dẫn nhiệt k = 0,04 W/(m.K). Diện tích tường là 10 m2. Nhiệt độ mặt trong là 25°C, mặt ngoài là 35°C (chênh lệch 10°C). Nhiệt lượng truyền qua tường trong 1 giây là bao nhiêu Oát (W)?", "80", "Q/t = k * S * Δt / d = 0,04 * 10 * 10 / 0,05 = 80 W."),
            make_sa(3, "Thông hiểu", "Trong một thí nghiệm nung nóng, sáp trên thanh đồng nóng chảy sau 12 giây, sáp trên thanh sắt nóng chảy sau 36 giây. Thời gian sáp nóng chảy trên thanh sắt gấp mấy lần trên thanh đồng?", "3", "36 / 12 = 3 lần."),
            make_sa(4, "Thông hiểu", "Một cửa kính đơn dày 5 mm truyền nhiệt với công suất 200 W. Nếu thay bằng cửa kính hai lớp cách nhiệt có cùng diện tích làm giảm công suất truyền nhiệt còn 50 W. Công suất nhiệt thất thoát giảm đi bao nhiêu Oát (W)?", "150", "200 - 50 = 150 W."),
            make_sa(5, "Vận dụng", "Một tảng đá lạnh 10 kg được bọc kín bằng lớp chăn bông cách nhiệt. Mỗi giờ chỉ có 16 800 J nhiệt lượng từ không khí truyền vào tảng đá. Sau 5 giờ, nhiệt lượng truyền vào đá là bao nhiêu kilôjun (kJ)?", "84", "Q = 16 800 * 5 = 84 000 J = 84 kJ."),
            make_sa(6, "Vận dụng", "Hai thanh đồng và nhôm có cùng tiết diện và chiều dài. Hệ số dẫn nhiệt của đồng là 380 W/(m.K), của nhôm là 200 W/(m.K). Tỉ số dẫn nhiệt giữa đồng và nhôm là bao nhiêu? (Làm tròn đến 1 chữ số thập phân).", "1.9", "380 / 200 = 1,9.")
        ],
        [
            make_vdc(1, "Một bức tường gạch của phòng học có chiều dài 8 m, chiều cao 3,5 m và độ dày d = 20 cm (0,2 m). Hệ số dẫn nhiệt của gạch xây là k = 0,7 W/(m.K). Vào mùa đông, nhiệt độ mặt trong tường giữ ở 22°C và mặt ngoài tường là 8°C (chênh lệch Δt = 14°C). Nhiệt lượng truyền qua bức tường gạch này trong thời gian 1 giờ (3600 giây) là:", [
                "4,939 MJ (tương đương 1,372 kWh)", "2,5 MJ", "10,2 MJ", "0,5 kWh"
            ], 0, "S = 8 * 3,5 = 28 m2. Công suất truyền nhiệt P = k * S * Δt / d = 0,7 * 28 * 14 / 0,2 = 1372 W. Q = 1372 * 3600 = 4 939 200 J ≈ 4,94 MJ = 1,372 kWh."),
            make_vdc(2, "Một ống dẫn hơi nước nóng bằng thép đường kính ngoài 10 cm, dài 50 m có nhiệt độ bề mặt ngoài là 120°C đặt trong không khí 20°C. Nếu bọc thêm một lớp bông khoáng cách nhiệt dày 5 cm (k = 0,05 W/(m.K)), nhiệt lượng thất thoát ra môi trường giảm 85%. Nếu lượng nhiệt hao phí ban đầu khi chưa bọc bảo ôn là 15 kW thì công suất nhiệt tiết kiệm được sau khi bọc cách nhiệt là:", [
                "12,75 kW", "15,0 kW", "2,25 kW", "7,5 kW"
            ], 0, "P_tietkiem = 15 kW * 85% = 12,75 kW."),
            make_vdc(3, "Một chiếc thùng xốp đựng đá lạnh hình hộp chữ nhật có tổng diện tích toàn phần 6 mặt là S = 1,2 m2, độ dày thành xốp d = 3 cm (0,03 m). Hệ số dẫn nhiệt của xốp EPS là k = 0,036 W/(m.K). Bên trong thùng nhiệt độ là 0°C, nhiệt độ không khí bên ngoài là 30°C. Biết nhiệt nóng chảy của nước đá là λ = 3,34 . 10^5 J/kg. Khối lượng nước đá bị tan chảy do nhiệt truyền qua thành thùng trong thời gian 5 giờ xấp xỉ bằng:", [
                "2,33 kg", "5,0 kg", "1,2 kg", "0,85 kg"
            ], 0, "Công suất truyền nhiệt P = 0,036 * 1,2 * 30 / 0,03 = 43,2 W. Q_5h = 43,2 * (5 * 3600) = 777 600 J. m_tan = 777600 / (3,34 . 10^5) ≈ 2,328 kg ≈ 2,33 kg."),
            make_vdc(4, "Một người thiết kế cán của chiếc chảo xào nấu bằng kim loại. Cán chảo làm bằng thanh thép hình trụ dài 25 cm, đường kính 2 cm (S = 3,14 . 10^-4 m2, k_thép = 50 W/(m.K)). Đầu gắn vào chảo có nhiệt độ 200°C, đầu tay cầm tiếp xúc không khí 25°C. Để giảm truyền nhiệt lên tay cầm, người thợ bọc một ống gỗ dày cách nhiệt quanh cán chảo. Nhận xét nào sau đây là chuẩn xác nhất về sự truyền nhiệt trong thanh cán chảo:", [
                "Dòng nhiệt truyền dọc theo trục cán thép chủ yếu bằng dẫn nhiệt, lớp vỏ gỗ hạn chế nhiệt truyền ngang ra không khí và bảo vệ tay không chạm vào thép nóng",
                "Cán thép không dẫn nhiệt",
                "Gỗ dẫn nhiệt nhanh hơn thép",
                "Chỉ có bức xạ nhiệt trong cán chảo"
            ], 0, "Dẫn nhiệt truyền dọc lõi thép; vỏ gỗ cách nhiệt bảo vệ tay người cầm.")
        ]
    )

    # ĐỀ 2: Đối lưu ở Chất lỏng, Chất khí & Hiện tượng tự nhiên
    p1_t2 = [
            make_mc(1, "Nhận biết", "Đối lưu là hình thức truyền nhiệt chủ yếu xảy ra ở trạng thái nào của vật chất?", ["Chất lỏng và Chất khí", "Chỉ ở chất rắn", "Chân không", "Kim loại"], 0, "Đối lưu là hình thức truyền nhiệt chủ yếu ở chất lỏng và chất khí."),
            make_mc(2, "Nhận biết", "Cơ chế của hiện tượng đối lưu là sự truyền nhiệt nhờ:", ["Các dòng chất lỏng hoặc chất khí chuyển động tuần hoàn mang theo năng lượng nhiệt", "Dao động của nguyên tử đứng yên", "Các tia bức xạ điện từ", "Sự va chạm của electron tự do"], 0, "Truyền nhiệt bằng các dòng chất lỏng hoặc khí di chuyển."),
            make_mc(3, "Nhận biết", "Khi đun nóng chất lỏng hoặc chất khí từ phía dưới, lớp chất lỏng ở đáy bình sẽ:", ["Nóng lên, nở ra, khối lượng riêng giảm đi và nhẹ hơn nổi lên trên", "Nặng hơn chìm xuống", "Đứng yên tại chỗ", "Biến mất"], 0, "Chất nóng nở ra nhẹ hơn nổi lên tạo dòng đối lưu hướng lên."),
            make_mc(4, "Nhận biết", "Tại sao khi đun nước bằng ấm hoặc xoong, người ta luôn phải đặt ngọn lửa ở phía đáy nồi?", ["Để tạo ra các dòng đối lưu tự nhiên đưa nước nóng lên trên và nước lạnh chìm xuống giúp cả ấm nhanh sôi", "Để không làm đen quai nồi", "Vì nước chỉ sôi ở đáy", "Theo thói quen"], 0, "Đun ở đáy tạo dòng đối lưu tuần hoàn toàn bộ khối nước."),
            make_mc(5, "Nhận biết", "Tại sao máy điều hòa nhiệt độ (máy lạnh) trong phòng luôn được lắp ở vị trí trên cao sát trần nhà?", ["Vì luồng không khí lạnh nặng hơn sẽ chìm xuống dưới, đẩy khí nóng nhẹ lên trên tạo dòng đối lưu làm mát cả phòng", "Để trẻ em không với tới", "Để tiết kiệm dây điện", "Vì gió chỉ thổi xuống"], 0, "Khí lạnh nặng chìm xuống làm mát toàn phòng nhờ đối lưu."),
            make_mc(6, "Nhận biết", "Thiết bị sưởi ấm (lò sưởi, máy sưởi dầu) trong phòng mùa đông thường được đặt ở:", ["Dưới sàn nhà hoặc vị trí thấp", "Treo sát trần nhà", "Treo ngoài cửa sổ", "Đặt trên nóc tủ"], 0, "Khí nóng nhẹ bốc lên cao sưởi ấm cả phòng từ dưới lên."),
            make_mc(7, "Thông hiểu", "Gió biển thổi từ biển vào đất liền vào ban ngày hình thành do nguyên nhân nào?", ["Ban ngày đất liền nóng lên nhanh hơn mặt biển, không khí trên đất liền nhẹ hơn bốc lên tạo vùng áp thấp hút gió từ biển vào", "Nước biển dâng cao đẩy gió", "Tàu thuyền chạy ngoài biển", "Mặt trăng hút gió"], 0, "Chênh lệch nhiệt độ và đối lưu không khí giữa đất liền và biển."),
            make_mc(8, "Thông hiểu", "Vào ban đêm ở bờ biển, hướng gió tự nhiên thường thổi theo chiều nào?", ["Thổi từ đất liền ra biển (gió đất)", "Thổi từ biển vào đất liền", "Không có gió", "Gió xoáy thẳng đứng"], 0, "Ban đêm đất liền nguội nhanh hơn biển, khí nóng trên biển bốc lên hút gió từ đất ra."),
            make_mc(9, "Thông hiểu", "Ống khói của các nhà máy hoặc bếp lò luôn được xây dựng cao vút thẳng đứng nhằm mục đích:", ["Tạo lực hút đối lưu mạnh đưa khói và khí thải nóng nhẹ thoát nhanh lên tầng cao", "Để chim không bay vào", "Làm đẹp cảnh quan", "Để đỡ tốn diện tích"], 0, "Ống khói cao tạo chênh lệch áp suất đối lưu đẩy khói bay lên nhanh."),
            make_mc(10, "Thông hiểu", "Vì sao trong chân không hoàn toàn KHÔNG THỂ xảy ra hiện tượng đối lưu?", ["Vì chân không không có các phân tử vật chất để tạo thành dòng chuyển động", "Vì chân không quá lạnh", "Vì chân không không có trọng lực", "Vì chân không có màu đen"], 0, "Không có môi trường vật chất thì không có dòng đối lưu."),
            make_mc(11, "Thông hiểu", "Thí nghiệm thả vài hạt thuốc tím (KMnO4) vào đáy cốc nước rồi đun nhẹ đáy cốc quan sát thấy:", ["Các dòng nước màu tím di chuyển từ đáy lên mặt nước rồi tỏa ra chìm dần xuống tạo vòng khép kín", "Hạt thuốc tím chìm đứng yên", "Nước đổi màu trắng", "Cốc nước bị nứt ngay"], 0, "Thuốc tím giúp hiển thị rõ đường đi của dòng đối lưu trong chất lỏng."),
            make_mc(12, "Thông hiểu", "Quạt thông gió gắn trên tường phòng bếp hoặc phòng vệ sinh có tác dụng gì đối với sự đối lưu không khí?", ["Tạo ra sự đối lưu cưỡng bức giúp tống khứ khí thải, mùi hôi và hút không khí tươi mới từ ngoài vào", "Làm lạnh phòng như điều hòa", "Làm nóng thức ăn", "Hút ẩm biến thành nước"], 0, "Đối lưu cưỡng bức bằng quạt gió lưu thông không khí.")
    ]

    p2_t2 = [
        make_tf(1, "Thông hiểu", "Về cơ chế và điều kiện phát sinh hiện tượng đối lưu đề 2:", [
            ("a", "Hiện tượng đối lưu chỉ xảy ra trong môi trường chất lưu (chất lỏng và chất khí).", True),
            ("b", "Động lực thúc đẩy dòng đối lưu tự nhiên là lực đẩy Archimedes tác dụng lên phần chất lưu nóng nhẹ hơn.", True),
            ("c", "Nếu đun nóng chất lỏng từ miệng ống nghiệm xuống thì dòng đối lưu tự nhiên vẫn phát triển mạnh xuống đáy.", False),
            ("d", "Trong môi trường không trọng lượng (trên trạm vũ trụ), hiện tượng đối lưu tự nhiên bị triệt tiêu.", True)
        ], "Đun ở miệng ống nghiệm thì phần nước nóng nhẹ nằm yên ở trên, không tạo dòng đối lưu xuống đáy."),
        make_tf(2, "Thông hiểu", "Về các hiện tượng khí tượng khí quyển do đối lưu gây ra đề 2:", [
            ("a", "Hiện tượng gió trong khí quyển bản chất là sự chuyển động của các dòng đối lưu không khí quy mô lớn.", True),
            ("b", "Các luồng không khí nóng ẩm bốc lên cao gặp lạnh ngưng tụ tạo thành những đám mây dông tích điện.", True),
            ("c", "Nhiệt độ trên đỉnh núi cao luôn nóng hơn dưới chân núi do khí nóng bốc lên đỉnh núi tụ lại.", False),
            ("d", "Chim đại bàng và tàu lượn thường lợi dụng các cột không khí nóng đối lưu bốc lên (thermal) để lượn lên cao mà không tốn sức.", True)
        ], "Càng lên cao không khí càng loãng, nhiệt độ khí quyển giảm trung bình 0,6°C trên 100 m."),
        make_tf(3, "Thông hiểu", "Về ứng dụng đối lưu trong kiến trúc xây dựng nhà ở đề 2:", [
            ("a", "Giếng trời trong các ngôi nhà ống tạo dòng đối lưu tự nhiên hút gió mát và thoát khí nóng lên mái.", True),
            ("b", "Cửa thông gió nên bố trí ở vị trí sát sàn nhà và sát trần nhà để tối ưu hóa sự luân chuyển không khí.", True),
            ("c", "Bịt kín hoàn toàn mọi khe hở của ngôi nhà giúp không khí trong nhà luôn lưu thông thoáng mát tự nhiên.", False),
            ("d", "Quạt trần tạo ra đối lưu nhân tạo làm tăng tốc độ bay hơi mồ hôi giúp cơ thể cảm thấy mát mẻ.", True)
        ], "Bịt kín nhà làm không khí ngột ngạt tù đọng, ngăn cản đối lưu."),
        make_tf(4, "Thông hiểu", "Về an toàn thoát hiểm khi xảy ra hỏa hoạn trong tòa nhà đề 2:", [
            ("a", "Khói độc và khí nóng do đối lưu luôn bốc lên cao và tích tụ dày đặc sát trần nhà.", True),
            ("b", "Khi thoát hiểm trong đám cháy, cần cúi thấp người hoặc bò sát mặt sàn để hít thở lớp không khí còn dưỡng khí.", True),
            ("c", "Dùng khăn ướt bịt mũi miệng vừa lọc bớt bụi than vừa làm mát luồng khí hít vào.", True),
            ("d", "Chạy ngay vào thang máy điện bấm nút đi xuống tầng trệt khi chuông báo cháy đang reo vang.", False)
        ], "Tuyệt đối không đi thang máy khi hỏa hoạn vì thang máy có thể mất điện kẹt giữa chừng thành bẫy tử thần.")
    ]
    p3_t2 = [
        make_sa(1, "Thông hiểu", "Một bình đun chứa 2 lít nước ở đáy được nung nóng làm khối lượng riêng của lớp nước đáy giảm từ 1000 kg/m3 xuống 980 kg/m3. Độ giảm khối lượng riêng là bao nhiêu kg/m3?", "20", "1000 - 980 = 20 kg/m3."),
        make_sa(2, "Thông hiểu", "Một căn phòng có thể tích 60 m3. Một quạt thông gió có lưu lượng 300 m3/giờ. Thời gian để quạt thông gió thay mới toàn bộ thể tích không khí trong phòng là bao nhiêu phút?", "12", "t = 60 / 300 = 0,2 giờ = 12 phút."),
        make_sa(3, "Thông hiểu", "Một dòng đối lưu không khí nóng bốc lên với tốc độ 2,5 m/s. Quãng đường luồng khí nóng đi được trong 8 giây là bao nhiêu mét?", "20", "s = 2,5 * 8 = 20 m."),
        make_sa(4, "Thông hiểu", "Ống khói một lò gạch cao 24 m tạo dòng khí thải di chuyển từ đáy lên đỉnh mất 6 giây. Vận tốc trung bình của dòng khí đối lưu trong ống khói là bao nhiêu m/s?", "4", "v = 24 / 6 = 4 m/s."),
        make_sa(5, "Vận dụng", "Nhiệt độ ở chân núi là 30°C. Biết cứ lên cao 100 m nhiệt độ giảm 0,6°C. Nhiệt độ ở độ cao 1500 m trên đỉnh núi là bao nhiêu °C?", "21", "Δt = (1500 / 100) * 0,6 = 9°C => t = 30 - 9 = 21°C."),
        make_sa(6, "Vận dụng", "Một máy điều hòa 9000 BTU có công suất làm lạnh khoảng 2600 W. Trong 10 phút hoạt động, nhiệt lượng mà máy lấy đi từ không khí trong phòng là bao nhiêu kilôjun (kJ)?", "1560", "Q = 2600 * 600 = 1 560 000 J = 1560 kJ.")
    ]
    p4_t2 = [
        make_vdc(1, "Một phòng học có kích thước dài 8 m, rộng 6 m, cao 3,5 m (thể tích V = 168 m3). Khối lượng riêng của không khí ở 32°C là D1 = 1,16 kg/m3, nhiệt dung riêng c_kk = 1005 J/(kg.K). Để hạ nhiệt độ không khí trong phòng từ 32°C xuống 24°C (giảm 8°C) bằng hệ thống điều hòa đối lưu, nhiệt lượng cần rút ra khỏi toàn bộ khối không khí trong phòng (bỏ qua nhiệt hấp thụ của tường và đồ vật) là:", [
            "1,567 MJ (khoảng 1567 kJ)", "3,134 MJ", "800 kJ", "5,0 MJ"
        ], 0, "m_kk = 168 * 1,16 = 194,88 kg. Q = 194,88 * 1005 * 8 ≈ 1 566 700 J ≈ 1,567 MJ."),
        make_vdc(2, "Một giếng trời của ngôi nhà ống có tiết diện ngang thẳng đứng S = 2,0 m2. Không khí nóng ở tầng trệt thoát lên qua giếng trời với tốc độ đối lưu v = 0,8 m/s. Biết khối lượng riêng của không khí nóng là 1,15 kg/m3. Lưu lượng khối lượng không khí đối lưu thoát ra qua giếng trời trong mỗi phút (60 giây) là:", [
            "110,4 kg/phút", "55,2 kg/phút", "220,8 kg/phút", "18,4 kg/phút"
        ], 0, "Lưu lượng thể tích: V_giay = S * v = 2,0 * 0,8 = 1,6 m3/s. m_giay = 1,6 * 1,15 = 1,84 kg/s. m_phut = 1,84 * 60 = 110,4 kg/phút."),
        make_vdc(3, "Một bể bơi mini chứa 20 m3 nước ở 18°C. Người ta bơm sục nước nóng 80°C vào đáy bể với lưu lượng 0,5 m3/giờ kết hợp máy khuấy đối lưu tuần hoàn. Bỏ qua mất nhiệt ra môi trường. Thời gian bơm nước nóng để toàn bộ nước trong bể bơi đạt nhiệt độ cân bằng 28°C là:", [
            "7,69 giờ (khoảng 7 giờ 41 phút)", "10,0 giờ", "5,0 giờ", "3,85 giờ"
            ], 0, "Gọi V_nong là thể tích nước nóng cần bơm: 20 * (28 - 18) = V_nong * (80 - 28) => 200 = 52 * V_nong => V_nong ≈ 3,846 m3. Thời gian = 3,846 / 0,5 ≈ 7,692 giờ."),
        make_vdc(4, "Trong một lò sấy nông sản bằng luồng khí nóng đối lưu cưỡng bức, quạt gió thổi 1200 m3 không khí mỗi giờ qua giàn ống gia nhiệt làm không khí tăng từ 25°C lên 65°C. Cho khối lượng riêng của không khí là 1,2 kg/m3 và nhiệt dung riêng là 1000 J/(kg.K). Công suất nhiệt tối thiểu của giàn cấp nhiệt cho lò sấy là:", [
            "16 kW", "8 kW", "32 kW", "48 kW"
        ], 0, "m_kk = 1200 * 1,2 = 1440 kg/h = 0,4 kg/s. P = m_giay * c * Δt = 0,4 * 1000 * 40 = 16 000 W = 16 kW.")
    ]

    exams[f"{l_id}_test2"] = meta(2, p1_t2, p2_t2, p3_t2, p4_t2)

    # ĐỀ 3: Bức xạ nhiệt, Cấu tạo Bình thủy & Ứng dụng tổng hợp
    p1_t3 = [
            make_mc(1, "Nhận biết", "Bức xạ nhiệt là hình thức truyền nhiệt bằng:", ["Các tia nhiệt (tia hồng ngoại) truyền thẳng trong không gian", "Dòng chất lỏng chảy", "Sự dẫn nhiệt qua kim loại", "Dòng electron chạy"], 0, "Bức xạ nhiệt truyền bằng các tia nhiệt hồng ngoại."),
            make_mc(2, "Nhận biết", "Hình thức truyền nhiệt nào sau đây có thể truyền được qua môi trường chân không hoàn toàn?", ["Bức xạ nhiệt", "Dẫn nhiệt", "Đối lưu", "Cả dẫn nhiệt và đối lưu"], 0, "Bức xạ nhiệt là hình thức duy nhất truyền được qua chân không."),
            make_mc(3, "Nhận biết", "Năng lượng nhiệt từ Mặt Trời truyền xuyên qua không gian vũ trụ đến Trái Đất chủ yếu bằng hình thức nào?", ["Bức xạ nhiệt", "Dẫn nhiệt qua không khí", "Đối lưu khí quyển", "Truyền sóng cơ học"], 0, "Truyền qua chân không vũ trụ bằng bức xạ nhiệt."),
            make_mc(4, "Nhận biết", "Vật có bề mặt màu sắc và tính chất nào sau đây có khả năng hấp thụ và bức xạ nhiệt tốt nhất?", ["Bề mặt màu đen, xù xì, sẫm màu", "Bề mặt màu trắng, nhẵn bóng", "Bề mặt tráng gương bạc", "Bề mặt trong suốt"], 0, "Màu đen, xù xì hấp thụ và bức xạ nhiệt tốt nhất."),
            make_mc(5, "Nhận biết", "Vào mùa hè nắng nóng, người ta thường mặc trang phục màu sáng (trắng, vàng nhạt) vì:", ["Quần áo màu sáng phản xạ tốt các tia bức xạ nhiệt từ Mặt Trời giúp đỡ nóng hơn", "Màu sáng hút nhiệt tốt", "Màu sáng giữ ấm", "Màu sáng nặng hơn"], 0, "Màu sáng phản xạ bức xạ nhiệt tốt, ít hấp thụ nhiệt."),
            make_mc(6, "Nhận biết", "Vỏ ruột phích nước (bình thủy) được tráng bạc sáng bóng ở cả hai mặt nhằm mục đích gì?", ["Phản xạ các tia bức xạ nhiệt quay trở lại nước, ngăn thất thoát nhiệt do bức xạ", "Để soi gương", "Làm ruột phích nặng hơn", "Làm nước có vị ngọt"], 0, "Lớp tráng bạc phản xạ bức xạ nhiệt ngăn mất nhiệt."),
            make_mc(7, "Thông hiểu", "Khoảng không gian giữa hai lớp vỏ thủy tinh của ruột phích nước được rút hết không khí (tạo chân không) nhằm:", ["Ngăn chặn triệt để sự truyền nhiệt bằng dẫn nhiệt và đối lưu ra môi trường bên ngoài", "Để nước chảy vào", "Để giảm khối lượng phích", "Để phích không bị vỡ"], 0, "Chân không ngăn chặn hoàn toàn dẫn nhiệt và đối lưu."),
            make_mc(8, "Thông hiểu", "Nắp phích nước thường làm bằng vật liệu xốp hoặc gỗ bọc nhựa nhằm:", ["Ngăn chặn sự truyền nhiệt bằng đối lưu và sự bay hơi của nước nóng ra ngoài", "Để đậy cho đẹp", "Làm tăng áp suất nước", "Hút bớt hơi nước"], 0, "Nắp cách nhiệt ngăn đối lưu và bay hơi."),
            make_mc(9, "Thông hiểu", "Các tấm pin thu nhiệt năng lượng mặt trời trên mái nhà luôn được sơn phủ màu gì?", ["Màu đen tuyền mờ để hấp thụ tối đa bức xạ nhiệt từ ánh nắng", "Màu trắng sáng", "Màu vàng bóng", "Màu bạc gương"], 0, "Màu đen mờ hấp thụ tối đa bức xạ nhiệt."),
            make_mc(10, "Thông hiểu", "Hiện tượng hiệu ứng nhà kính trong nông nghiệp (trồng trọt trong nhà kính bọc màng nilon) giữ ấm cho cây trồng nhờ:", ["Kính cho bức xạ sóng ngắn mặt trời đi vào nhưng giữ lại bức xạ nhiệt sóng dài phát ra từ đất bên trong", "Nhà kính tự phát nhiệt", "Kính cản toàn bộ gió lạnh", "Đất tự nóng lên vĩnh viễn"], 0, "Bẫy bức xạ nhiệt sóng dài bên trong nhà kính."),
            make_mc(11, "Thông hiểu", "Một chiếc ấm đun nước bằng nhôm sáng bóng và một chiếc ấm bằng gang đen sì cùng chứa nước sôi để nguội trong phòng. Ấm nào sẽ nguội đi nhanh hơn?", ["Ấm gang đen sì vì bề mặt đen sẫm bức xạ nhiệt ra môi trường tốt hơn ấm nhôm sáng bóng", "Ấm nhôm sáng bóng", "Cả hai nguội như nhau", "Không ấm nào nguội"], 0, "Bề mặt đen bức xạ nhiệt nhanh hơn nhiều so với bề mặt sáng bóng."),
            make_mc(12, "Thông hiểu", "Tại sao người cứu hỏa khi tiếp cận đám cháy lớn thường mặc bộ trang phục tráng lớp nhôm bạc kim loại sáng lóa?", ["Lớp nhôm phản xạ phần lớn các tia bức xạ nhiệt khủng khiếp từ đám cháy bảo vệ cơ thể", "Để dễ nhận ra trong khói", "Để áo không bị ướt", "Để chống tĩnh điện"], 0, "Phản xạ bức xạ nhiệt cực mạnh từ ngọn lửa bảo vệ lính cứu hỏa.")
    ]

    p2_t3 = [
        make_tf(1, "Thông hiểu", "Về bản chất và định luật bức xạ nhiệt của các vật đề 3:", [
            ("a", "Mọi vật có nhiệt độ lớn hơn 0 Kelvin (-273,15°C) đều liên tục phát ra bức xạ nhiệt.", True),
            ("b", "Nhiệt độ của vật càng cao thì khả năng phát bức xạ nhiệt càng mạnh mẽ.", True),
            ("c", "Bức xạ nhiệt chỉ có thể truyền đi khi có môi trường không khí hoặc chất lỏng trung gian.", False),
            ("d", "Vật hấp thụ bức xạ nhiệt tốt thì đồng thời cũng có khả năng bức xạ nhiệt tốt.", True)
        ], "Bức xạ nhiệt truyền tốt nhất qua chân không hoàn toàn."),
        make_tf(2, "Thông hiểu", "Về cấu tạo hoàn hảo chống mất nhiệt của phích nước (bình thủy) đề 3:", [
            ("a", "Ruột phích gồm 2 lớp thủy tinh có khoảng chân không ngăn dẫn nhiệt và đối lưu.", True),
            ("b", "Hai mặt đối diện của khoảng chân không được tráng bạc ngăn thất thoát do bức xạ nhiệt.", True),
            ("c", "Nút bấc hoặc nắp xốp đậy kín miệng phích ngăn chặn hiện tượng đối lưu không khí.", True),
            ("d", "Nếu vỏ phích bị nứt thủng để không khí tràn vào khoảng chân không thì phích vẫn giữ nhiệt tốt như cũ.", False)
        ], "Mất chân không làm phích mất nhiệt nhanh chóng bằng dẫn nhiệt và đối lưu."),
        make_tf(3, "Thông hiểu", "Về vai trò của tầng khí quyển và hiệu ứng nhà kính khí quyển Trái Đất đề 3:", [
            ("a", "Khí quyển Trái Đất giữ nhiệt giúp nhiệt độ bề mặt Trái Đất duy trì ổn định cho sự sống phát triển.", True),
            ("b", "Khí carbon dioxide (CO2) và hơi nước là các khí nhà kính chính hấp thụ bức xạ nhiệt hồng ngoại.", True),
            ("c", "Nếu hoàn toàn không có hiệu ứng nhà kính tự nhiên thì nhiệt độ trung bình Trái Đất sẽ khoảng -18°C.", True),
            ("d", "Gia tăng nồng độ khí CO2 do đốt nhiên liệu hóa thạch không gây ảnh hưởng gì đến khí hậu toàn cầu.", False)
        ], "Tăng CO2 làm tăng hiệu ứng nhà kính nhân tạo gây biến đổi khí hậu toàn cầu."),
        make_tf(4, "Thông hiểu", "Về ứng dụng bức xạ nhiệt trong công nghệ và sinh hoạt đề 3:", [
            ("a", "Camera nhiệt hồng ngoại có thể quan sát và ghi lại hình ảnh người trong đêm tối hoàn toàn.", True),
            ("b", "Các dàn tản nhiệt của tủ lạnh và máy tính thường được sơn màu đen để tăng phát tán nhiệt.", True),
            ("c", "Máy bay tàng hình quân sự sử dụng sơn tản nhiệt để giảm phát xạ hồng ngoại tránh tên lửa tầm nhiệt.", True),
            ("d", "Bình chứa xăng dầu ở các kho bãi thường được sơn màu đen kịt để xăng bên trong không bị đóng băng.", False)
        ], "Bồn xăng luôn sơn màu trắng hoặc bạc sáng bóng để phản xạ ánh nắng chống cháy nổ.")
    ]
    p3_t3 = [
        make_sa(1, "Thông hiểu", "Một tấm pin mặt trời diện tích 1,5 m2 nhận bức xạ nhiệt với công suất 800 W/m2. Tổng công suất bức xạ chiếu vào tấm pin là bao nhiêu Oát (W)?", "1200", "P = 1,5 * 800 = 1200 W."),
        make_sa(2, "Thông hiểu", "Một phích nước chứa 2 kg nước sôi 100°C. Sau 24 giờ, nhiệt độ nước giảm còn 70°C. Biết c = 4200 J/(kg.K). Nhiệt lượng nước đã tỏa ra môi trường là bao nhiêu kilôjun (kJ)?", "252", "Q = 2 * 4200 * 30 = 252 000 J = 252 kJ."),
        make_sa(3, "Thông hiểu", "Công suất bức xạ nhiệt của một bếp hồng ngoại là 2000 W. Trong thời gian 15 phút (900 giây), bếp đã phát ra năng lượng nhiệt là bao nhiêu kilôjun (kJ)?", "1800", "A = 2000 * 900 = 1 800 000 J = 1800 kJ."),
        make_sa(4, "Thông hiểu", "Một bề mặt nhôm sáng bóng phản xạ 90% bức xạ nhiệt chiếu vào nó. Nếu có 500 J bức xạ chiếu tới thì năng lượng bị bề mặt hấp thụ là bao nhiêu Jun (J)?", "50", "Hấp thụ = 500 * (100% - 90%) = 50 J."),
        make_sa(5, "Vận dụng", "Một bề mặt sơn đen mờ hấp thụ 95% bức xạ nhiệt chiếu tới. Khi nhận bức xạ có công suất 1000 W, công suất nhiệt mà bề mặt này hấp thụ được là bao nhiêu Oát (W)?", "950", "P = 1000 * 95% = 950 W."),
        make_sa(6, "Vận dụng", "Khoảng cách từ Mặt Trời đến Trái Đất khoảng 150 triệu km (1,5 . 10^8 km). Biết tốc độ ánh sáng và bức xạ nhiệt là 300 000 km/s. Thời gian bức xạ nhiệt truyền từ Mặt Trời đến Trái Đất là bao nhiêu giây?", "500", "t = 150 000 000 / 300 000 = 500 giây (khoảng 8 phút 20 giây).")
    ]
    p4_t3 = [
        make_vdc(1, "Một bình nước nóng năng lượng mặt trời dạng ống chân không có 16 ống thu nhiệt, mỗi ống có diện tích thu nhiệt hữu ích S0 = 0,1 m2 (tổng diện tích S = 1,6 m2). Bức xạ mặt trời chiếu thẳng góc có cường độ trung bình 850 W/m2. Hiệu suất nhiệt của hệ thống ống chân không đạt 70%. Bình chứa 150 lít nước ở nhiệt độ ban đầu 25°C. Cho nhiệt dung riêng của nước c = 4200 J/(kg.K). Thời gian chiếu nắng liên tục cần thiết để đun nóng nước trong bình lên đến 60°C là:", [
            "6,46 giờ (khoảng 6 giờ 28 phút)", "4,5 giờ", "8,0 giờ", "3,2 giờ"
        ], 0, "P_thu = 1,6 * 850 * 0,7 = 952 W. Q_can = 150 * 4200 * 35 = 22 050 000 J. t = 22050000 / 952 ≈ 23 162 s ≈ 6,43 - 6,46 giờ."),
        make_vdc(2, "Một chiếc bình giữ nhiệt chân không bằng inox có dung tích 0,8 lít chứa đầy cà phê nóng ở nhiệt độ ban đầu 95°C. Đặt bình trong phòng điều hòa có nhiệt độ 20°C. Sau 10 giờ, nhiệt độ cà phê trong bình còn 65°C. Coi nhiệt dung riêng của cà phê bằng của nước c = 4200 J/(kg.K). Công suất mất mát nhiệt trung bình của bình giữ nhiệt trong 10 giờ đó là:", [
            "2,8 W", "5,6 W", "10,0 W", "1,4 W"
        ], 0, "m = 0,8 kg. Q_mat = 0,8 * 4200 * (95 - 65) = 100 800 J. t = 10 * 3600 = 36 000 s. P_mat = 100800 / 36000 = 2,8 W."),
        make_vdc(3, "Một vệ tinh nhân tạo quay quanh Trái Đất hoạt động trong môi trường chân không của vũ trụ. Thân vệ tinh có diện tích bề mặt S = 4,0 m2 được bọc lớp màng phản xạ nhiệt màu vàng kim phản xạ 85% bức xạ mặt trời. Cường độ bức xạ mặt trời trong không gian là 1360 W/m2. Công suất nhiệt bức xạ mà thân vệ tinh hấp thụ được khi hứng nắng vuông góc là:", [
            "816 W", "5440 W", "2720 W", "408 W"
        ], 0, "P_chieu = 4,0 * 1360 = 5440 W. P_hapthu = 5440 * (100% - 85%) = 5440 * 0,15 = 816 W."),
        make_vdc(4, "Một căn nhà kính trồng hoa lan có diện tích mái kính đón nắng S = 100 m2. Bức xạ nhiệt mặt trời chiếu vào nhà kính với công suất 600 W/m2, kính cho 80% bức xạ đi qua vào bên trong. Đất và cây cối bên trong hấp thụ và bức xạ lại nhiệt sóng dài, nhưng mái kính giữ lại 90% lượng bức xạ này bên trong nhà kính. Công suất nhiệt được giữ lại làm ấm nhà kính là:", [
            "43,2 kW", "48,0 kW", "60,0 kW", "30,0 kW"
        ], 0, "P_vao = 100 * 600 * 0,8 = 48 000 W = 48 kW. P_giu = 48 kW * 0,9 = 43,2 kW.")
    ]
    exams[f"{l_id}_test3"] = meta(3, p1_t3, p2_t3, p3_t3, p4_t3)

    return exams