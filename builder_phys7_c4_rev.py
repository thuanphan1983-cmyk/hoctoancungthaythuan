# -*- coding: utf-8 -*-
"""
CHƯƠNG IV: ÂM THANH - ÔN TẬP CUỐI CHƯƠNG IV (5 ĐỀ ĐỘC LẬP 100%)
- phys7_c4_rev: [Đề tổng hợp] Ôn tập cuối Chương IV (5 đề: test1..test5)
Không trùng lặp, không tiền tố "Đề X - " hoặc "Đề tổng hợp X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

c4_rev_exams = {}

# =========================================================================
# ĐỀ TỔNG HỢP ÔN TẬP CUỐI CHƯƠNG IV (5 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
c4_rev_exams["phys7_c4_rev_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Mọi vật phát ra âm thanh đều:", ["Đang dao động", "Đang chuyển động thẳng", "Có nhiệt độ rất cao", "Đang đứng yên"], 0, "Dao động là nguồn gốc của mọi âm thanh."),
        make_mc(2, "Nhận biết", "Sóng âm truyền được trong môi trường nào sau đây?", ["Chất rắn, chất lỏng và chất khí", "Chỉ chất khí", "Chỉ chất lỏng", "Chân không tuyệt đối"], 0, "Sóng âm truyền trong rắn, lỏng, khí."),
        make_mc(3, "Nhận biết", "Tần số dao động là số dao động vật thực hiện được trong:", ["1 giây", "1 phút", "1 giờ", "1 ngày"], 0, "Tần số là số dao động trong 1 giây (Hz)."),
        make_mc(4, "Nhận biết", "Độ cao của âm phụ thuộc vào:", ["Tần số dao động của nguồn âm", "Biên độ dao động", "Độ to của âm", "Khoảng cách truyền âm"], 0, "Tần số quyết định độ cao (bổng/trầm)."),
        make_mc(5, "Nhận biết", "Vật liệu nào sau đây phản xạ âm tốt?", ["Gạch men bóng phẳng", "Rèm vải nhung", "Tấm mút xốp", "Bông gòn mềm"], 0, "Gạch men bóng cứng phản xạ âm tốt."),
        make_mc(6, "Nhận biết", "Biện pháp nào sau đây giúp hạn chế tiếng ồn từ động cơ xe máy phát ra?", ["Lắp bộ giảm thanh (ống xả tiêu âm) đạt chuẩn", "Tháo bỏ ống xả", "Bấm còi to", "Tăng ga mạnh"], 0, "Ống giảm thanh giảm độ to ngay tại nguồn phát."),
        make_mc(7, "Thông hiểu", "Một vật thực hiện 240 dao động trong 6 giây. Tần số dao động của vật là:", ["40 Hz", "1440 Hz", "240 Hz", "60 Hz"], 0, "f = 240 / 6 = 40 Hz."),
        make_mc(8, "Thông hiểu", "Âm thanh có tần số 35.000 Hz thuộc dải sóng nào?", ["Sóng siêu âm", "Sóng hạ âm", "Âm nghe được", "Sóng vô tuyến"], 0, "f > 20.000 Hz là sóng siêu âm."),
        make_mc(9, "Thông hiểu", "Một người gõ búa vào thanh thép dài. Tốc độ âm trong thép xấp xỉ khoảng:", ["5000 m/s", "340 m/s", "1500 m/s", "300.000 km/s"], 0, "Tốc độ âm trong thép khoảng 5000 m/s."),
        make_mc(10, "Thông hiểu", "Khoảng cách tối thiểu từ người phát âm đến bức tường để nghe được tiếng vang trong không khí (v = 340 m/s) là:", ["Khoảng 11,3 mét", "Khoảng 5,5 mét", "Khoảng 22,7 mét", "Khoảng 34 mét"], 0, "d_min = 340 × (1/15) / 2 ≈ 11,3 m."),
        make_mc(11, "Thông hiểu", "Gảy dây đàn guitar càng mạnh thì biên độ dao động càng lớn, âm phát ra sẽ:", ["Nghe càng to", "Càng bổng hơn", "Càng trầm hơn", "Không thay đổi"], 0, "Biên độ lớn làm độ to của âm tăng lên."),
        make_mc(12, "Thông hiểu", "Biển báo cấm sử dụng còi xe đặt gần cổng trường học nhằm:", ["Ngăn chặn ô nhiễm tiếng ồn, tạo không gian yên tĩnh cho học sinh học tập", "Để xe chạy nhanh hơn", "Tránh hỏng còi xe", "Để người đi bộ không giật mình"], 0, "Hạn chế ô nhiễm tiếng ồn bảo vệ môi trường sư phạm.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về sự lan truyền và cảm nhận sóng âm của con người:", [
            ("a", "Sóng âm mang năng lượng và làm màng nhĩ trong tai dao động.", True),
            ("b", "Trong chân không, sóng âm truyền đi với tốc độ bằng tốc độ ánh sáng.", False),
            ("c", "Tốc độ truyền âm giảm dần: chất rắn > chất lỏng > chất khí.", True),
            ("d", "Dải tần số âm tai người cảm nhận được là từ 16 Hz đến 20.000 Hz.", True)
        ], "Sóng âm hoàn toàn không truyền được trong chân không."),
        make_tf(2, "Thông hiểu", "Về mối quan hệ giữa dao động và âm thanh:", [
            ("a", "Dao động càng nhanh thì tần số dao động càng lớn, âm nghe càng bổng.", True),
            ("b", "Độ lệch lớn nhất của vật khỏi vị trí cân bằng gọi là biên độ dao động.", True),
            ("c", "Âm có độ to 140 dB gây cảm giác êm tai và dễ chịu.", False),
            ("d", "Tiếng sấm rền kéo dài là do hiện tượng âm phản xạ liên tiếp giữa mây và đất.", True)
        ], "140 dB vượt ngưỡng đau tai (130 dB), gây đau đớn và thủng màng nhĩ."),
        make_tf(3, "Vận dụng", "Thí nghiệm khảo sát tiếng vang trong một hầm bê tông dài 68 m:", [
            ("a", "Một người đứng ở đầu hầm vỗ tay một tiếng ngắn dứt khoát.", True),
            ("b", "Sóng âm truyền đến cuối hầm dội vào vách tường phẳng rồi quay lại tai người.", True),
            ("c", "Thời gian âm phản xạ truyền về tai là 0,40 giây (biết v = 340 m/s).", True),
            ("d", "Người đó không thể nghe thấy tiếng vang vì khoảng cách quá gần.", False)
        ], "0,40 s > 1/15 s (≈ 0,067 s) nên người đó nghe thấy tiếng vang rất to và rõ."),
        make_tf(4, "Vận dụng", "Về sóng siêu âm và các ứng dụng trong đời sống:", [
            ("a", "Sóng siêu âm có tần số trên 20.000 Hz, tai người không nghe thấy được.", True),
            ("b", "Dơi dùng sóng siêu âm để săn muỗi và định vị đường bay trong đêm tối.", True),
            ("c", "Tàu ngầm dùng máy phát sóng siêu âm sonar để đo độ sâu đáy biển.", True),
            ("d", "Sóng siêu âm bị cản lại và không thể truyền qua lớp nước biển.", False)
        ], "Sóng siêu âm truyền cực kì tốt trong nước biển.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một vật thực hiện 180 dao động trong 3 giây. Tần số dao động là bao nhiêu Hz?", "60", "f = 180 / 3 = 60 Hz."),
        make_sa(2, "Thông hiểu", "Tốc độ truyền âm trong không khí ở nhiệt độ 20 °C là bao nhiêu m/s?", "340", "340 m/s."),
        make_sa(3, "Vận dụng", "Âm thanh có tần số 12 Hz thuộc dải sóng nào? (Hạ âm hay Siêu âm)", "Hạ âm", "f < 16 Hz là hạ âm."),
        make_sa(4, "Vận dụng", "Một người nhìn thấy ánh chớp rồi sau 2,5 giây nghe thấy tiếng sấm. Biết v = 340 m/s. Nơi sét đánh cách người đó bao nhiêu mét?", "850", "s = 340 × 2,5 = 850 m."),
        make_sa(5, "Vận dụng cao", "Một người đứng trước vách đá hét to và nghe thấy tiếng vang sau 0,8 giây. Khoảng cách đến vách đá là bao nhiêu mét? (v = 340 m/s)", "136", "d = 340 × 0,8 / 2 = 136 m."),
        make_sa(6, "Vận dụng cao", "Máy đo hồi âm sonar trên tàu phát xung siêu âm xuống đáy biển và thu lại tín hiệu sau 1,6 giây. Với v = 1500 m/s, độ sâu đáy biển là bao nhiêu mét?", "1200", "d = 1500 × 1,6 / 2 = 1200 m.")
    ],
    "part4": [
        make_vdc(1, "Một người gõ búa vào thanh ray xe lửa bằng thép dài 1020 m. Người thứ hai áp tai vào thanh ray nghe thấy hai tiếng gõ liên tiếp cách nhau 2,8 giây: một tiếng truyền qua thép và một tiếng truyền qua không khí (v = 340 m/s). Tốc độ truyền âm trong thép của thanh ray là:", ["5100 m/s", "3400 m/s", "4800 m/s", "6000 m/s"], 0, "t_khí = 1020 / 340 = 3,0 s. t_thép = 3,0 - 2,8 = 0,2 s => v_thép = 1020 / 0,2 = 5100 m/s."),
        make_vdc(2, "Một người đứng cách một vách núi đá vôi 340 m hét to một tiếng. Sau bao lâu kể từ lúc phát âm người đó nghe thấy tiếng vang dội lại từ vách núi? (Biết tốc độ âm trong không khí là 340 m/s).", ["2,0 giây", "1,0 giây", "1,5 giây", "0,5 giây"], 0, "t = 2d / v = 2 × 340 / 340 = 2,0 s."),
        make_vdc(3, "Tại sao khi bước vào một ngôi nhà mới xây chưa có đồ đạc, tiếng bước chân và tiếng nói chuyện của ta nghe rất vang, nhưng khi đã kê đầy bàn ghế, giường tủ và treo rèm cửa thì hiện tượng này biến mất?", ["Vì đồ đạc gỗ và rèm vải xốp mềm đã hấp thụ phần lớn năng lượng sóng âm phản xạ, làm triệt tiêu tiếng vang", "Vì không khí trong nhà bị ấm lên", "Vì sàn nhà bị lún", "Vì mắt nhìn thấy đồ đạc"], 0, "Đồ đạc và rèm vải tiêu âm hiệu quả, triệt tiêu phản xạ âm thanh."),
        make_vdc(4, "Một máy phát sóng siêu âm phát một tín hiệu thẳng đứng từ mạn thuyền xuống đáy một hồ nước sâu và nhận lại tín hiệu phản xạ sau 0,12 giây. Biết tốc độ âm trong nước hồ là 1500 m/s. Độ sâu của hồ nước tại vị trí khảo sát là:", ["90 m", "180 m", "45 m", "120 m"], 0, "d = 1500 × 0,12 / 2 = 90 m.")
    ]
}

# --- ĐỀ 2 ---
c4_rev_exams["phys7_c4_rev_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật phát ra âm thanh khi nào?", ["Khi vật đang dao động đàn hồi", "Khi vật được nung nóng", "Khi vật đứng yên tuyệt đối", "Khi có dòng điện chạy qua"], 0, "Mọi vật phát ra âm thanh đều đang dao động."),
        make_mc(2, "Nhận biết", "Sóng âm KHÔNG THỂ truyền được qua môi trường nào?", ["Chân không", "Khí oxi", "Nước cất", "Thanh đồng"], 0, "Chân không không truyền được sóng âm."),
        make_mc(3, "Nhận biết", "Đơn vị dùng để đo mức độ to của âm thanh là:", ["Decibel (dB)", "Hertz (Hz)", "Mét (m)", "Jun (J)"], 0, "Độ to của âm đo bằng Decibel (dB)."),
        make_mc(4, "Nhận biết", "Âm thanh phát ra nghe càng bổng khi:", ["Tần số dao động của nguồn âm càng lớn", "Tần số dao động càng nhỏ", "Biên độ dao động càng nhỏ", "Nguồn âm đứng yên"], 0, "Tần số càng lớn âm càng bổng."),
        make_mc(5, "Nhận biết", "Vật nào sau đây phản xạ âm kém nhất (hấp thụ âm tốt nhất)?", ["Tấm xốp cách âm", "Tấm gương kính", "Tường đá hoa cương", "Mặt kim loại nhẵn"], 0, "Xốp mềm có bề mặt rỗng xốp tiêu âm tốt nhất."),
        make_mc(6, "Nhận biết", "Chụp tai chống ồn có tác dụng chính là:", ["Bảo vệ màng nhĩ khỏi tác hại của tiếng ồn cường độ cao", "Giúp nghe rõ tiếng thì thầm", "Tránh bụi bẩn", "Làm ấm tai"], 0, "Bảo vệ màng nhĩ tai người lao động."),
        make_mc(7, "Thông hiểu", "Một con lắc dao động 150 lần trong thời gian 30 giây. Tần số dao động là:", ["5 Hz", "150 Hz", "4500 Hz", "0,2 Hz"], 0, "f = 150 / 30 = 5 Hz."),
        make_mc(8, "Thông hiểu", "Sóng âm có tần số 14 Hz thuộc vùng sóng nào?", ["Hạ âm", "Siêu âm", "Âm nghe được", "Sóng ánh sáng"], 0, "14 Hz < 16 Hz là hạ âm."),
        make_mc(9, "Thông hiểu", "Tốc độ truyền âm trong nước biển khoảng 1500 m/s. Thời gian âm truyền đi quãng đường 4500 m trong nước là:", ["3,0 giây", "1,5 giây", "2,0 giây", "4,5 giây"], 0, "t = 4500 / 1500 = 3,0 s."),
        make_mc(10, "Thông hiểu", "Một người hét to trước vách núi cách 170 m. Sau bao lâu người đó nghe thấy tiếng vang dội lại? (v = 340 m/s)", ["1,0 giây", "0,5 giây", "2,0 giây", "1,5 giây"], 0, "t = 2 × 170 / 340 = 1,0 s."),
        make_mc(11, "Thông hiểu", "Gõ mạnh vào mặt trống làm màng trống dao động với biên độ lớn thì:", ["Âm phát ra nghe to hơn", "Âm phát ra bổng hơn", "Âm phát ra trầm hơn", "Âm bị tắt đi"], 0, "Biên độ lớn làm tăng độ to của âm."),
        make_mc(12, "Thông hiểu", "Hành vi nào sau đây góp phần chống ô nhiễm tiếng ồn trong khu dân cư?", ["Không bấm còi xe inh ỏi và không mở loa công suất lớn lúc đêm khuya", "Bóp còi liên tục", "Mở nhạc đám cưới suốt đêm", "Cắt ống xả xe máy"], 0, "Tôn trọng sự yên tĩnh chung của cộng đồng.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất dao động của các nguồn âm thông dụng:", [
            ("a", "Dây đàn bầu dao động khi người nghệ sĩ gảy đàn.", True),
            ("b", "Cột không khí bên trong ống sáo dao động khi thổi sáo.", True),
            ("c", "Màng loa rung qua lại liên tục khi đang phát nhạc.", True),
            ("d", "Tiếng sấm phát ra từ các đám mây hoàn toàn không liên quan đến dao động không khí.", False)
        ], "Tiếng sấm là do không khí bị giãn nở đột ngột và dao động dữ dội phát ra âm thanh."),
        make_tf(2, "Thông hiểu", "Về khả năng nghe của tai người và động vật:", [
            ("a", "Tai người nghe được âm từ 16 Hz đến 20.000 Hz.", True),
            ("b", "Hạ âm có tần số nhỏ hơn 16 Hz.", True),
            ("c", "Siêu âm có tần số lớn hơn 20.000 Hz.", True),
            ("d", "Loài dơi không thể phát ra sóng siêu âm.", False)
        ], "Dơi phát sóng siêu âm cực tốt để định vị săn mồi."),
        make_tf(3, "Vận dụng", "Học sinh làm thí nghiệm chứng minh sự truyền âm qua chất rắn bằng thước nhựa dài 1 m:", [
            ("a", "Bạn A áp tai vào một đầu thước nhựa.", True),
            ("b", "Bạn B cào nhẹ đầu móng tay vào đầu kia của thước nhựa.", True),
            ("c", "Bạn A nghe thấy tiếng cào truyền qua thước nhựa rất rõ ràng.", True),
            ("d", "Người đứng ngoài cách 1 m trong không khí nghe thấy tiếng cào to hơn bạn A.", False)
        ], "Chất rắn truyền âm tốt hơn nhiều so với không khí nên bạn A nghe rõ hơn nhiều người đứng ngoài."),
        make_tf(4, "Vận dụng", "Ứng dụng vật liệu cách âm trong các công trình hiện đại:", [
            ("a", "Cửa kính hộp hai lớp có lớp chân không ở giữa giúp cách âm cách nhiệt hoàn hảo.", True),
            ("b", "Phòng karaoke thường bọc mút gai tiêu âm để chống tiếng ồn lọt ra ngoài.", True),
            ("c", "Tấm tôn kim loại phẳng nhẵn có khả năng tiêu âm tốt hơn tấm đệm cao su non.", False),
            ("d", "Trồng cây xanh tán rộng quanh trường học giúp cản bớt tiếng ồn đường phố.", True)
        ], "Tấm kim loại phản xạ âm tốt chứ không tiêu âm tốt bằng cao su non.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một lá thép dao động 250 lần trong 5 giây. Tần số dao động là bao nhiêu Hz?", "50", "f = 250 / 5 = 50 Hz."),
        make_sa(2, "Thông hiểu", "Đơn vị đo tần số dao động là gì?", "Hz", "Hertz (Hz)."),
        make_sa(3, "Vận dụng", "Sóng âm có tần số 28.000 Hz thuộc vùng sóng nào? (Hạ âm hay Siêu âm)", "Siêu âm", "f > 20.000 Hz là siêu âm."),
        make_sa(4, "Vận dụng", "Sau khi nhìn thấy tia sét, đúng 3,0 giây sau nghe thấy tiếng sấm. Biết v = 340 m/s. Khoảng cách đến tia sét là bao nhiêu mét?", "1020", "s = 340 × 3 = 1020 m."),
        make_sa(5, "Vận dụng cao", "Một người đứng trước vách đá hét to và nghe thấy tiếng vang sau 0,6 giây. Khoảng cách đến vách đá là bao nhiêu mét? (v = 340 m/s)", "102", "d = 340 × 0,6 / 2 = 102 m."),
        make_sa(6, "Vận dụng cao", "Tàu thăm dò đáy biển phát sóng âm sonar xuống biển và nhận lại tiếng vang sau 2,0 giây. Với v = 1500 m/s, độ sâu đáy biển là bao nhiêu mét?", "1500", "d = 1500 × 2 / 2 = 1500 m.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng cách bức tường của một sân khấu ngoài trời 68 m vỗ tay một cái. Sau bao lâu người đó nghe thấy tiếng vang dội lại từ bức tường? (Biết tốc độ âm trong không khí là 340 m/s).", ["0,4 giây", "0,2 giây", "0,5 giây", "0,8 giây"], 0, "t = 2 × 68 / 340 = 0,4 s."),
        make_vdc(2, "Một người đứng giữa hai vách đá thẳng đứng song song trong hẻm núi. Người này bắn một phát súng hiệu thì sau 0,8 giây nghe thấy tiếng vang thứ nhất và sau 1,2 giây nghe thấy tiếng vang thứ hai dội lại từ vách đối diện. Bề rộng của hẻm núi là bao nhiêu mét? (Biết tốc độ âm trong không khí là 340 m/s).", ["340 m", "680 m", "170 m", "510 m"], 0, "d1 = 340 × 0,8 / 2 = 136 m; d2 = 340 × 1,2 / 2 = 204 m => Bề rộng = 136 + 204 = 340 m."),
        make_vdc(3, "Tại sao khi ta đứng ở gần đường tàu hỏa, người ta thường khuyên nên áp tai vào đường ray để biết tàu hỏa đang đến gần từ xa?", ["Vì thanh ray thép truyền âm nhanh hơn và ít bị suy giảm năng lượng hơn nhiều so với không khí", "Vì đường ray phát ra âm thanh", "Vì không khí bị gió thổi ngược", "Vì mặt đất rung lên"], 0, "Thép (chất rắn) truyền âm với tốc độ ~ 5000 m/s và bảo toàn năng lượng tốt hơn không khí."),
        make_vdc(4, "Một đoàn thám hiểm sử dụng máy đo hồi âm siêu âm để khảo sát độ sâu của một rãnh nứt dưới đáy biển. Tín hiệu siêu âm phát đi truyền với tốc độ 1500 m/s và nhận lại sau 0,48 giây. Độ sâu của rãnh nứt đó là:", ["360 m", "720 m", "180 m", "540 m"], 0, "d = 1500 × 0,48 / 2 = 360 m.")
    ]
}

# --- ĐỀ 3 ---
c4_rev_exams["phys7_c4_rev_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Âm thanh truyền nhanh nhất trong môi trường nào?", ["Chất rắn", "Chất lỏng", "Chất khí", "Chân không"], 0, "Tốc độ âm trong chất rắn là lớn nhất."),
        make_mc(2, "Nhận biết", "Độ cao của âm gắn liền với đại lượng nào của nguồn âm?", ["Tần số dao động", "Biên độ dao động", "Độ to của âm", "Thể tích nguồn âm"], 0, "Tần số dao động quyết định độ cao của âm."),
        make_mc(3, "Nhận biết", "Mức độ to của âm phụ thuộc vào:", ["Biên độ dao động của nguồn âm", "Tần số dao động của nguồn âm", "Tốc độ truyền sóng âm", "Hình dạng vật phát âm"], 0, "Biên độ dao động quyết định độ to của âm."),
        make_mc(4, "Nhận biết", "Âm thanh có tần số nhỏ hơn 16 Hz được gọi là:", ["Hạ âm", "Siêu âm", "Âm nghe được", "Sóng điện từ"], 0, "f < 16 Hz là hạ âm."),
        make_mc(5, "Nhận biết", "Vật liệu nào sau đây thường dùng làm tường cách âm phòng thu âm?", ["Mút xốp đục lỗ, rèm nhung dạ", "Tấm nhôm sáng bóng", "Mặt gương kính phẳng", "Tấm đá granit mài bóng"], 0, "Vật mềm xốp tiêu âm tốt."),
        make_mc(6, "Nhận biết", "Thiết bị giảm thanh (bộ phận tiêu âm) gắn ở đuôi xe máy có tác dụng gì?", ["Giảm độ to của âm thanh xả khí từ động cơ", "Tăng tốc độ của xe", "Làm mát buồng đốt", "Tăng âm lượng còi xe"], 0, "Giảm tiếng ồn khí xả động cơ."),
        make_mc(7, "Thông hiểu", "Một quả lắc đồng hồ dao động 120 lần trong 2 phút (120 s). Tần số dao động là:", ["1 Hz", "60 Hz", "120 Hz", "2 Hz"], 0, "f = 120 / 120 = 1 Hz."),
        make_mc(8, "Thông hiểu", "Sóng siêu âm có tần số nằm trong khoảng nào?", ["Trên 20.000 Hz", "Dưới 16 Hz", "Từ 16 Hz đến 20.000 Hz", "0 đến 100 Hz"], 0, "Siêu âm trên 20.000 Hz."),
        make_mc(9, "Thông hiểu", "Đứng cách bức tường phẳng 34 m hét to, sau bao lâu ta nghe thấy tiếng vang dội lại? (v = 340 m/s)", ["0,20 giây", "0,10 giây", "0,40 giây", "0,50 giây"], 0, "t = 2 × 34 / 340 = 0,20 s."),
        make_mc(10, "Thông hiểu", "Người xưa thường dùng tiếng trống lệnh đồng để truyền tin báo động trong quân đội vì:", ["Mặt trống đồng dao động phát ra âm thanh trầm vang truyền đi rất xa trong không khí", "Trống đồng phát ra ánh sáng", "Trống đồng rất nhẹ", "Trống đồng không bị gỉ"], 0, "Mặt trống đồng vang xa, truyền tin hiệu quả."),
        make_mc(11, "Thông hiểu", "Khi căng dây đàn guitar chặt hơn rồi gảy, âm phát ra sẽ:", ["Bổng hơn vì tần số dao động của dây đàn tăng lên", "Trầm hơn", "Không đổi", "Nghe nhỏ đi"], 0, "Dây căng hơn dao động nhanh hơn => âm bổng hơn."),
        make_mc(12, "Thông hiểu", "Biện pháp nào sau đây giúp phân tán tiếng ồn trên đường truyền?", ["Trồng nhiều cây xanh có tán lá rộng xum xuê ven đường", "Bịt chặt tai", "Lắp ống xả giảm thanh", "Cấm xe chạy"], 0, "Cây xanh làm phân tán sóng âm.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc trưng của sóng âm trong các môi trường:", [
            ("a", "Sóng âm truyền dao động qua các phân tử vật chất của môi trường.", True),
            ("b", "Trong không khí ở 20 °C, âm thanh truyền với tốc độ khoảng 340 m/s.", True),
            ("c", "Tốc độ âm trong nước biển nhỏ hơn trong không khí.", False),
            ("d", "Các phi hành gia trên Mặt Trăng phải dùng sóng vô tuyến (bộ đàm) để giao tiếp.", True)
        ], "Tốc độ âm trong nước (~ 1500 m/s) lớn hơn nhiều so với trong không khí (~ 340 m/s)."),
        make_tf(2, "Thông hiểu", "Về tần số và biên độ dao động:", [
            ("a", "Tần số đo bằng đơn vị Hertz (Hz).", True),
            ("b", "Biên độ dao động càng lớn thì âm nghe càng to.", True),
            ("c", "Vật dao động càng nhanh thì âm phát ra càng trầm.", False),
            ("d", "Âm có tần số 50 Hz nghe trầm hơn âm có tần số 500 Hz.", True)
        ], "Dao động nhanh làm âm bổng hơn, không phải trầm hơn."),
        make_tf(3, "Vận dụng", "Khảo sát âm thanh phát ra từ một chiếc loa điện gắn trên giá thí nghiệm:", [
            ("a", "Rắc vài mẩu xốp nhỏ lên màng loa, khi bật nhạc màng loa rung làm các mẩu xốp nảy lên.", True),
            ("b", "Khi vặn nút âm lượng to lên, các hạt xốp nảy lên cao hơn do biên độ tăng.", True),
            ("c", "Tần số nốt nhạc phát ra không bị thay đổi khi ta tăng hoặc giảm âm lượng.", True),
            ("d", "Nếu chụp kín chiếc chuông thủy tinh đã hút chân không lên loa thì ta vẫn nghe thấy tiếng nhạc to như cũ.", False)
        ], "Chân không không truyền được âm nên tiếng nhạc bị tắt hẳn."),
        make_tf(4, "Vận dụng", "Ứng dụng tiếng vang để đo độ sâu đáy biển:", [
            ("a", "Máy sonar phát chùm sóng siêu âm định hướng xuống đáy biển.", True),
            ("b", "Sóng siêu âm phản xạ từ đáy biển dội ngược lên tàu.", True),
            ("c", "Thời gian sóng đi và về là 1,0 s thì độ sâu của biển là 1500 m (biết v = 1500 m/s).", False),
            ("d", "Độ sâu thực tế của biển trong trường hợp này là d = 1500 × 1,0 / 2 = 750 m.", True)
        ], "Độ sâu phải chia đôi: 1500 × 1,0 / 2 = 750 m (câu c ghi 1500 m là sai).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một vật dao động thực hiện 400 dao động trong 8 giây. Tần số dao động là bao nhiêu Hz?", "50", "f = 400 / 8 = 50 Hz."),
        make_sa(2, "Thông hiểu", "Âm thanh có tần số 8 Hz thuộc vùng sóng nào? (Hạ âm hay Siêu âm)", "Hạ âm", "f < 16 Hz là hạ âm."),
        make_sa(3, "Vận dụng", "Khoảng cách từ người đến vách núi là 85 m. Sau bao nhiêu giây người đó nghe thấy tiếng vang? (v = 340 m/s)", "0.5", "t = 2 × 85 / 340 = 0,5 s."),
        make_sa(4, "Vận dụng", "Sóng âm truyền trong không khí mất 3,5 giây để đến tai người nghe. Biết v = 340 m/s. Khoảng cách nguồn âm là bao nhiêu mét?", "1190", "s = 340 × 3,5 = 1190 m."),
        make_sa(5, "Vận dụng cao", "Tàu ngầm thu được tiếng vang phản xạ từ đáy vực sau 0,8 giây. Với v = 1500 m/s, độ sâu đáy vực là bao nhiêu mét?", "600", "d = 1500 × 0,8 / 2 = 600 m."),
        make_sa(6, "Vận dụng cao", "Độ to của tiếng động cơ phản lực ở cự li gần có thể đạt tới bao nhiêu decibel (dB)?", "130", "Khoảng 120 - 130 dB.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng tại miệng một giếng sâu khô cạn hét to một tiếng xuống đáy giếng và nghe thấy tiếng vang vọng lại sau 0,25 giây. Biết tốc độ âm trong không khí là 340 m/s. Độ sâu của chiếc giếng đó là:", ["42,5 m", "85,0 m", "21,25 m", "50,0 m"], 0, "h = 340 × 0,25 / 2 = 42,5 m."),
        make_vdc(2, "Một người gõ một nhát búa vào đường ống kim loại bằng gang dài 1360 m. Người thứ hai áp tai vào đầu kia của ống nghe thấy tiếng gõ truyền qua gang sau 0,4 giây và tiếng gõ truyền qua không khí sau 4,0 giây. Tốc độ truyền âm trong gang đo được là:", ["3400 m/s", "5100 m/s", "1700 m/s", "4000 m/s"], 0, "v_gang = 1360 / 0,4 = 3400 m/s."),
        make_vdc(3, "Tại sao khi một đoàn máy bay chiến đấu bay qua khu dân cư ở độ cao thấp, các cửa kính của các tòa nhà cao tầng thường bị rung lên bần bật?", ["Vì sóng âm thanh có năng lượng cơ học rất lớn truyền trong không khí tác dụng lực làm rung các tấm kính", "Vì máy bay hút hết không khí", "Vì cửa kính bị nhiễm điện", "Vì nhiệt độ tăng cao"], 0, "Sóng âm mang năng lượng cơ học lớn tác động vào các tấm kính gây rung động mạnh."),
        make_vdc(4, "Một người đứng cách một vách núi đá 119 m bắn một phát súng hiệu. Biết tốc độ âm trong không khí là 340 m/s. Sau bao lâu người đó nghe thấy tiếng vang dội lại?", ["0,7 giây", "0,35 giây", "1,4 giây", "0,5 giây"], 0, "t = 2 × 119 / 340 = 0,7 s.")
    ]
}

# --- ĐỀ 4 ---
c4_rev_exams["phys7_c4_rev_test4"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 04",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 4, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Nguồn âm là:", ["Vật tự nó phát ra âm thanh", "Vật hứng âm thanh", "Vật phản xạ ánh sáng", "Vật trong suốt"], 0, "Vật phát ra âm thanh gọi là nguồn âm."),
        make_mc(2, "Nhận biết", "Âm thanh truyền được trong:", ["Chất rắn, lỏng, khí", "Chỉ chân không", "Chỉ chất rắn", "Chỉ chất khí"], 0, "Âm truyền trong cả 3 thể rắn, lỏng, khí."),
        make_mc(3, "Nhận biết", "Số dao động vật thực hiện được trong một giây gọi là:", ["Tần số dao động", "Biên độ", "Quãng đường", "Thời gian"], 0, "Tần số là số dao động trong 1 giây."),
        make_mc(4, "Nhận biết", "Âm phát ra càng trầm khi tần số dao động:", ["Càng nhỏ", "Càng lớn", "Bằng 20.000 Hz", "Cực đại"], 0, "Tần số nhỏ âm phát ra trầm."),
        make_mc(5, "Nhận biết", "Tiếng vang là âm phản xạ nghe được cách âm trực tiếp ít nhất:", ["1/15 giây", "1 giây", "1/2 giây", "1/100 giây"], 0, "Ít nhất 1/15 giây để tạo tiếng vang."),
        make_mc(6, "Nhận biết", "Vật liệu mềm, xốp, có bề mặt gồ ghề là vật liệu:", ["Hấp thụ âm tốt (tiêu âm tốt)", "Phản xạ âm rất tốt", "Không truyền âm", "Phát ra âm to"], 0, "Vật mềm xốp tiêu âm tốt."),
        make_mc(7, "Thông hiểu", "Một vật dao động thực hiện 300 dao động trong 10 giây. Tần số dao động là:", ["30 Hz", "3000 Hz", "300 Hz", "3 Hz"], 0, "f = 300 / 10 = 30 Hz."),
        make_mc(8, "Thông hiểu", "Sóng âm có tần số 40.000 Hz thuộc dải sóng nào?", ["Sóng siêu âm", "Sóng hạ âm", "Âm nghe được", "Sóng điện từ"], 0, "f > 20.000 Hz là siêu âm."),
        make_mc(9, "Thông hiểu", "Nhìn thấy tia chớp rồi 1,5 giây sau nghe thấy tiếng sấm (v = 340 m/s). Nơi sét đánh cách người quan sát là:", ["510 m", "340 m", "680 m", "1020 m"], 0, "s = 340 × 1,5 = 510 m."),
        make_mc(10, "Thông hiểu", "Khi một người nói to hơn bình thường thì màng nhĩ người nghe sẽ:", ["Dao động với biên độ lớn hơn", "Dao động với tần số cao hơn", "Đứng yên", "Bị thủng ngay"], 0, "Âm to làm màng nhĩ dao động với biên độ lớn hơn."),
        make_mc(11, "Thông hiểu", "Vật nào sau đây phản xạ âm tốt nhất?", ["Tấm gương phẳng phẳng bóng", "Rèm vải nhung", "Tấm mút xốp", "Bao cát"], 0, "Mặt gương phẳng bóng phản xạ âm rất tốt."),
        make_mc(12, "Thông hiểu", "Biện pháp nào sau đây giúp giảm tiếng ồn tại nguồn âm?", ["Gắn ống xả giảm thanh cho động cơ xe máy", "Trồng cây xanh", "Đeo nút tai", "Lắp kính hai lớp"], 0, "Ống giảm thanh giảm ồn tại nguồn phát.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc tính vật lý của sóng âm:", [
            ("a", "Sóng âm là sóng cơ học lan truyền trong môi trường đàn hồi.", True),
            ("b", "Âm thanh không truyền được trong môi trường chân không.", True),
            ("c", "Tốc độ âm trong thép lớn hơn tốc độ âm trong không khí.", True),
            ("d", "Tai người có thể nghe được âm thanh ở mọi tần số từ 0 đến vô cùng.", False)
        ], "Tai người chỉ nghe được dải tần số 16 Hz - 20.000 Hz."),
        make_tf(2, "Thông hiểu", "Về mối quan hệ giữa độ to và biên độ âm:", [
            ("a", "Độ to của âm được đo bằng đơn vị Decibel (dB).", True),
            ("b", "Biên độ dao động càng lớn thì âm nghe càng to.", True),
            ("c", "Tiếng nói thầm thì có độ to khoảng 80 dB.", False),
            ("d", "Ngưỡng đau màng nhĩ của tai người là khoảng 130 dB.", True)
        ], "Nói thì thầm chỉ khoảng 20 - 30 dB (80 dB là tiếng xe cộ rất to)."),
        make_tf(3, "Vận dụng", "Một người gõ một tiếng búa vào đầu thanh ray đường sắt bằng thép dài 680 m:", [
            ("a", "Tốc độ truyền âm trong thép khoảng 5100 m/s.", True),
            ("b", "Thời gian âm truyền qua thanh ray thép là xấp xỉ 0,133 giây.", True),
            ("c", "Thời gian âm truyền qua không khí (v = 340 m/s) là 2,0 giây.", True),
            ("d", "Người ở đầu kia nghe thấy âm truyền qua không khí trước âm truyền qua thép.", False)
        ], "Âm truyền qua thép (rắn) tới trước rất nhanh so với qua không khí."),
        make_tf(4, "Vận dụng", "Các biện pháp chống ô nhiễm tiếng ồn trong đời sống đô thị:", [
            ("a", "Trồng cây xanh ven đường làm tán xạ phân tán sóng âm.", True),
            ("b", "Lắp cửa kính cách âm hai lớp ngăn chặn đường truyền âm.", True),
            ("c", "Sử dụng vật liệu tiêu âm trong phòng thu âm để triệt tiêu tiếng vang.", True),
            ("d", "Xây dựng các nhà máy cưa sắt thép ngay cạnh bệnh viện trung tâm.", False)
        ], "Nhà máy phát tiếng ồn lớn phải xây dựng xa khu dân cư và bệnh viện.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một vật dao động thực hiện 160 dao động trong 4 giây. Tần số dao động là bao nhiêu Hz?", "40", "f = 160 / 4 = 40 Hz."),
        make_sa(2, "Thông hiểu", "Sóng âm có tần số 5 Hz thuộc vùng nào? (Hạ âm hay Siêu âm)", "Hạ âm", "f < 16 Hz là hạ âm."),
        make_sa(3, "Vận dụng", "Khoảng cách từ người đến vách núi là 170 m. Sau bao lâu người đó nghe thấy tiếng vang? (v = 340 m/s)", "1", "t = 2 × 170 / 340 = 1 s."),
        make_sa(4, "Vận dụng", "Âm thanh truyền trong nước biển với tốc độ 1500 m/s trong 1,2 giây. Quãng đường âm đi được là bao nhiêu mét?", "1800", "s = 1500 × 1,2 = 1800 m."),
        make_sa(5, "Vận dụng cao", "Khoảng cách ngắn nhất để nghe được tiếng vang trong không khí là bao nhiêu mét? (Làm tròn 1 chữ số)", "11.3", "11,3 m."),
        make_sa(6, "Vận dụng cao", "Đơn vị đo tần số dao động viết tắt là gì?", "Hz", "Hertz (Hz).")
    ],
    "part4": [
        make_vdc(1, "Một người đứng trước vách đá cách 136 m và hét to. Biết tốc độ âm trong không khí là 340 m/s. Sau bao lâu người đó nghe thấy tiếng vang dội lại?", ["0,8 giây", "0,4 giây", "1,0 giây", "1,2 giây"], 0, "t = 2 × 136 / 340 = 0,8 s."),
        make_vdc(2, "Một người đứng tại một điểm nhìn thấy tia chớp rồi sau 5,0 giây nghe thấy tiếng sấm rền vang. Biết v = 340 m/s. Điểm sét đánh cách người đó bao nhiêu mét?", ["1700 m", "1500 m", "2000 m", "1360 m"], 0, "s = 340 × 5 = 1700 m."),
        make_vdc(3, "Một thiết bị phát sóng siêu âm sonar trên tàu ngầm gửi xung âm xuống đáy biển và thu lại tín hiệu sau 1,5 giây. Biết tốc độ âm trong nước là 1500 m/s. Độ sâu đáy biển là:", ["1125 m", "2250 m", "1500 m", "1000 m"], 0, "d = 1500 × 1,5 / 2 = 1125 m."),
        make_vdc(4, "Tại sao khi nói chuyện trong hang đá rộng, tiếng nói nghe vang và kéo dài rền rĩ?", ["Do âm thanh phản xạ liên tiếp nhiều lần qua lại giữa các vách đá trong hang tới tai ở các thời điểm khác nhau", "Do hang đá có ma thuật", "Do hang đá tự phát âm", "Do không khí đứng yên"], 0, "Âm phản xạ nhiều lần tạo chuỗi tiếng vang kéo dài.")
    ]
}

# --- ĐỀ 5 ---
c4_rev_exams["phys7_c4_rev_test5"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 05",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 5, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Bộ phận dao động phát ra âm thanh của chiếc đàn ghita khi chơi là:", ["Các sợi dây đàn", "Thùng đàn", "Cần đàn", "Phím đàn"], 0, "Dây đàn dao động là nguồn âm chính."),
        make_mc(2, "Nhận biết", "Trong môi trường nào sau đây âm thanh truyền đi chậm nhất (khác 0)?", ["Chất khí (không khí)", "Chất lỏng (nước)", "Chất rắn (thép)", "Chất rắn (gỗ)"], 0, "Tốc độ âm trong chất khí chậm nhất."),
        make_mc(3, "Nhận biết", "Âm nghe càng bổng khi nguồn âm dao động có:", ["Tần số càng lớn", "Tần số càng nhỏ", "Biên độ càng nhỏ", "Biên độ càng lớn"], 0, "Tần số lớn thì âm bổng."),
        make_mc(4, "Nhận biết", "Âm nghe càng to khi nguồn âm dao động có:", ["Biên độ càng lớn", "Biên độ càng nhỏ", "Tần số càng nhỏ", "Tần số càng lớn"], 0, "Biên độ lớn thì âm to."),
        make_mc(5, "Nhận biết", "Dải tần số tai người bình thường nghe được là:", ["16 Hz đến 20.000 Hz", "Dưới 16 Hz", "Trên 20.000 Hz", "Từ 0 đến 100 Hz"], 0, "Dải nghe được: 16 - 20.000 Hz."),
        make_mc(6, "Nhận biết", "Hiện tượng âm dội ngược trở lại khi gặp mặt chắn gọi là:", ["Sự phản xạ âm", "Sự khúc xạ âm", "Sự truyền thẳng", "Sự hấp thụ âm"], 0, "Phản xạ âm khi gặp mặt chắn."),
        make_mc(7, "Thông hiểu", "Một vật dao động thực hiện 450 dao động trong 9 giây. Tần số dao động là:", ["50 Hz", "4050 Hz", "45 Hz", "5 Hz"], 0, "f = 450 / 9 = 50 Hz."),
        make_mc(8, "Thông hiểu", "Âm thanh có tần số 50.000 Hz thuộc dải sóng nào?", ["Sóng siêu âm", "Sóng hạ âm", "Âm nghe được", "Sóng ánh sáng"], 0, "f > 20.000 Hz là siêu âm."),
        make_mc(9, "Thông hiểu", "Nhìn thấy tia chớp rồi 2,0 giây sau nghe thấy tiếng sấm (v = 340 m/s). Nơi sét đánh cách xa:", ["680 m", "340 m", "1020 m", "1500 m"], 0, "s = 340 × 2 = 680 m."),
        make_mc(10, "Thông hiểu", "Khoảng cách ngắn nhất từ người đến vật cản để nghe tiếng vang trong không khí là:", ["Khoảng 11,3 m", "Khoảng 5,0 m", "Khoảng 20,0 m", "Khoảng 34,0 m"], 0, "d_min ≈ 11,3 m."),
        make_mc(11, "Thông hiểu", "Vật liệu nào sau đây dùng để tiêu âm hiệu quả nhất trong phòng karaoke?", ["Tấm mút xốp tổ ong", "Tấm gương kính", "Tấm nhôm", "Tường xi măng bóng"], 0, "Mút xốp tiêu âm tốt nhất."),
        make_mc(12, "Thông hiểu", "Biện pháp nào sau đây ngăn chặn tiếng ồn truyền vào phòng học?", ["Đóng kín cửa và lắp cửa kính cách âm", "Bật quạt to", "Bật loa to", "Mở hết cửa sổ"], 0, "Cửa kính kín cách âm ngăn chặn tiếng ồn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất dao động và sự truyền sóng âm:", [
            ("a", "Nguồn âm là vật phát ra âm thanh do đang dao động.", True),
            ("b", "Chân không không có các hạt phân tử nên không truyền được sóng âm.", True),
            ("c", "Tốc độ truyền âm trong chất lỏng nhỏ hơn trong chất khí.", False),
            ("d", "Sóng âm mang theo năng lượng khi truyền đi.", True)
        ], "Tốc độ âm trong lỏng lớn hơn trong khí (1500 m/s > 340 m/s)."),
        make_tf(2, "Thông hiểu", "Về các đặc tính cao độ và độ to của âm:", [
            ("a", "Tần số dao động càng lớn thì âm phát ra càng bổng.", True),
            ("b", "Biên độ dao động càng lớn thì âm phát ra càng to.", True),
            ("c", "Đơn vị đo tần số là Hertz (Hz).", True),
            ("d", "Âm có tần số 10.000 Hz nghe trầm hơn âm có tần số 100 Hz.", False)
        ], "10.000 Hz bổng hơn nhiều so với 100 Hz."),
        make_tf(3, "Vận dụng", "Khảo sát thí nghiệm phản xạ âm trong phòng lớn trống trải:", [
            ("a", "Người hét to cách bức tường 51 m nghe thấy tiếng vang sau 0,3 giây.", True),
            ("b", "Bức tường cứng nhẵn phản xạ âm rất tốt.", True),
            ("c", "Nếu treo các tấm rèm nhung dày khắp tường thì tiếng vang bị giảm hẳn.", True),
            ("d", "Nếu đứng cách tường 2 m thì vẫn nghe thấy tiếng vang tách rời.", False)
        ], "Cách 2 m âm phản xạ về sau 0,012 s < 1/15 s nên không tạo tiếng vang tách rời."),
        make_tf(4, "Vận dụng", "Ứng dụng và tác hại của âm thanh trong đời sống:", [
            ("a", "Sóng siêu âm dùng để chẩn đoán hình ảnh y khoa an toàn cho con người.", True),
            ("b", "Dơi dùng sóng siêu âm định vị tránh va chạm trong đêm tối.", True),
            ("c", "Tiếng ồn kéo dài trên 85 dB không ảnh hưởng gì đến sức khỏe.", False),
            ("d", "Trồng cây xanh tán rộng ven đường giúp giảm thiểu ô nhiễm tiếng ồn.", True)
        ], "Tiếng ồn trên 85 dB kéo dài gây hại cho thính giác và thần kinh.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một vật thực hiện 200 dao động trong 4 giây. Tần số dao động là bao nhiêu Hz?", "50", "f = 200 / 4 = 50 Hz."),
        make_sa(2, "Thông hiểu", "Âm thanh có tần số 30.000 Hz là hạ âm hay siêu âm?", "Siêu âm", "f > 20.000 Hz là siêu âm."),
        make_sa(3, "Vận dụng", "Người nhìn thấy tia chớp rồi 4,0 giây sau nghe tiếng sấm. Điểm sét đánh cách người đó bao nhiêu mét? (v = 340 m/s)", "1360", "s = 340 × 4 = 1360 m."),
        make_sa(4, "Vận dụng", "Khoảng cách từ người đến vách núi là 204 m. Sau bao nhiêu giây người đó nghe thấy tiếng vang? (v = 340 m/s)", "1.2", "t = 2 × 204 / 340 = 1,2 s."),
        make_sa(5, "Vận dụng cao", "Máy đo siêu âm phát xung âm xuống biển thu lại sau 0,4 giây. Độ sâu biển là bao nhiêu mét? (v = 1500 m/s)", "300", "d = 1500 × 0,4 / 2 = 300 m."),
        make_sa(6, "Vận dụng cao", "Khoảng cách ngắn nhất giữa người và tường để nghe tiếng vang trong không khí là bao nhiêu mét? (Làm tròn 1 chữ số)", "11.3", "11,3 m.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng trước vách đá cách 170 m hét to một tiếng. Sau bao lâu người đó nghe thấy tiếng vang dội lại? (v = 340 m/s)", ["1,0 giây", "0,5 giây", "2,0 giây", "1,5 giây"], 0, "t = 2 × 170 / 340 = 1,0 s."),
        make_vdc(2, "Một người gõ búa vào thanh ray thép dài 1530 m. Người thứ hai áp tai vào đầu kia của ray nghe thấy tiếng gõ truyền qua thanh ray thép sau 0,3 giây. Tốc độ truyền âm trong thép của thanh ray là:", ["5100 m/s", "3400 m/s", "4500 m/s", "6000 m/s"], 0, "v = 1530 / 0,3 = 5100 m/s."),
        make_vdc(3, "Tại sao các phòng hòa nhạc thính phòng thường được thiết kế trần nhà và các bức tường lồi lõm zích zắc không theo mặt phẳng đều?", ["Để tán xạ sóng âm theo nhiều hướng ngẫu nhiên, giúp âm thanh phân bố đồng đều khắp khán phòng mà không bị dội tiếng vang tập trung vào một điểm", "Để phòng hòa nhạc trông lạ mắt", "Để chống sét", "Để phòng mát hơn"], 0, "Tán xạ âm giúp trường âm thanh đồng đều khắp phòng khán giả."),
        make_vdc(4, "Tàu đánh cá sử dụng thiết bị dò cá bằng sóng siêu âm (v = 1500 m/s). Sóng siêu âm phát ra gặp đàn cá phản xạ trở lại sau 0,08 giây. Đàn cá đang bơi ở độ sâu cách tàu bao nhiêu mét?", ["60 m", "120 m", "30 m", "90 m"], 0, "d = 1500 × 0,08 / 2 = 60 m.")
    ]
}
