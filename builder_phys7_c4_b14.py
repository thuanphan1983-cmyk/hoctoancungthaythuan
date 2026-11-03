# -*- coding: utf-8 -*-
"""
CHƯƠNG IV: ÂM THANH - BÀI 14: PHẢN XẠ ÂM, CHỐNG Ô NHIỄM TIẾNG ỒN (3 ĐỀ ĐỘC LẬP 100%)
- phys7_c4_b14: Bài 14 (3 đề: test1, test2, test3)
Không trùng lặp, không tiền tố "Đề X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

b14_exams = {}

# =========================================================================
# BÀI 14: PHẢN XẠ ÂM, CHỐNG Ô NHIỄM TIẾNG ỒN (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b14_exams["phys7_c4_b14_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b14", "lessonName": "Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Hiện tượng sóng âm khi gặp một mặt chắn bị dội ngược trở lại môi trường cũ được gọi là:", ["Sự phản xạ âm", "Sự khúc xạ âm", "Sự nhiễu xạ âm", "Sự truyền thẳng của âm"], 0, "Sóng âm bị dội lại khi gặp mặt chắn gọi là phản xạ âm."),
        make_mc(2, "Nhận biết", "Âm phản xạ nghe được cách âm trực tiếp một khoảng thời gian ít nhất là bao lâu thì được gọi là tiếng vang?", ["1/15 giây", "1/2 giây", "1 giây", "1/60 giây"], 0, "Tiếng vang là âm phản xạ nghe cách âm trực tiếp ít nhất 1/15 giây."),
        make_mc(3, "Nhận biết", "Vật nào sau đây phản xạ âm tốt (hấp thụ âm kém)?", ["Tấm kính phẳng, nhẵn bóng", "Tấm mút xốp", "Rèm vải nhung", "Tấm đệm cao su"], 0, "Vật cứng có bề mặt nhẵn bóng phản xạ âm tốt."),
        make_mc(4, "Nhận biết", "Vật liệu nào sau đây là vật liệu hấp thụ âm tốt (tiêu âm) thường dùng để cách âm phòng hát?", ["Mút xốp bọt biển, dạ, rèm nhung", "Tấm kim loại phẳng nhẵn", "Mặt gương kính", "Tường bê tông mài bóng"], 0, "Vật liệu mềm xốp, bề mặt gồ ghề hấp thụ âm tốt."),
        make_mc(5, "Nhận biết", "Tiếng ồn gây ô nhiễm là tiếng ồn:", ["To, kéo dài ảnh hưởng tiêu cực đến sức khỏe, sinh hoạt và làm việc của con người", "Nhỏ thì thầm", "Êm dịu du dương", "Chỉ xuất hiện vào ban ngày trong 1 giây"], 0, "Ô nhiễm tiếng ồn là tiếng ồn lớn kéo dài ảnh hưởng xấu đến đời sống và sức khỏe."),
        make_mc(6, "Nhận biết", "Biện pháp nào sau đây giúp phân tán âm thanh trên đường truyền?", ["Trồng nhiều dải cây xanh có tán lá rộng ven đường", "Đóng kín cửa sổ", "Đeo nút bịt tai", "Tắt máy xe"], 0, "Cây xanh có tán lá rậm rạp làm tán xạ và hấp thụ âm thanh trên đường truyền."),
        make_mc(7, "Thông hiểu", "Để nghe được tiếng vang của giọng nói trong không khí (v = 340 m/s), khoảng cách ngắn nhất từ người nói đến bức tường phản xạ phải là:", ["Khoảng 11,3 mét", "Khoảng 5,0 mét", "Khoảng 20,0 mét", "Khoảng 34,0 mét"], 0, "d_min = v × t / 2 = 340 × (1/15) / 2 ≈ 11,33 m."),
        make_mc(8, "Thông hiểu", "Tại sao khi nói chuyện trong một căn phòng rộng trống không có đồ đạc, ta lại nghe thấy tiếng vang hoặc âm bị nhòe?", ["Vì âm thanh phản xạ nhiều lần từ các bức tường nhẵn gồ ghề tới tai gần như cùng lúc", "Vì phòng quá tối", "Vì không khí trong phòng đứng yên", "Vì trần nhà quá thấp"], 0, "Phòng trống có tường cứng nhẵn phản xạ âm tốt, âm phản xạ dội lại làm nhòe tiếng."),
        make_mc(9, "Thông hiểu", "Biện pháp nào sau đây tác động trực tiếp nhằm giảm độ to tại nguồn âm?", ["Cấm bóp còi xe hơi gần bệnh viện và trường học", "Đeo nút bịt tai khi ngủ", "Trồng cây xanh ven đường", "Lắp cửa kính 2 lớp"], 0, "Cấm bấm còi là biện pháp can thiệp trực tiếp tại nguồn phát âm."),
        make_mc(10, "Thông hiểu", "Loài dơi bay săn mồi trong đêm tối mà không bị va vào các nhánh cây hay bức tường là nhờ:", ["Phát ra sóng siêu âm và thu nhận tín hiệu âm phản xạ từ chướng ngại vật (định vị bằng tiếng vang)", "Mắt dơi sáng như đèn pha", "Dơi ngửi thấy chướng ngại vật", "Dơi bay rất chậm"], 0, "Dơi sử dụng cơ chế định vị bằng tiếng vang sóng siêu âm (echolocation)."),
        make_mc(11, "Thông hiểu", "Trong các rạp chiếu phim hiện đại, tường và trần nhà thường được thiết kế uốn lượn và ốp các tấm thạch cao đục lỗ nhằm:", ["Hấp thụ và triệt tiêu âm phản xạ, tránh hiện tượng tiếng vang giúp âm thanh trung thực", "Để tường không bị nứt vỡ", "Để phòng chiếu ấm hơn", "Để trang trí mỹ thuật"], 0, "Tiêu âm và triệt tiêu tiếng vang giúp chất lượng âm thanh trong rạp chuẩn xác."),
        make_mc(12, "Thông hiểu", "Trường hợp nào sau đây là biểu hiện của ô nhiễm tiếng ồn?", ["Nhà ở cạnh xưởng cơ khí cưa sắt, gò hàn kim loại hoạt động ầm ĩ suốt ngày đêm", "Tiếng lá cây rơi xào xạc trong vườn", "Tiếng đồng hồ tích tắc trong đêm", "Tiếng suối chảy róc rách xa xa"], 0, "Tiếng xưởng cưa gò sắt kéo dài liên tục gây ô nhiễm tiếng ồn nghiêm trọng.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về tính chất phản xạ của sóng âm trên các bề mặt vật liệu:", [
            ("a", "Bề mặt phẳng nhẵn và cứng phản xạ âm rất tốt.", True),
            ("b", "Bề mặt gồ ghề, xốp mềm hấp thụ âm tốt và phản xạ âm kém.", True),
            ("c", "Tấm gương kính phản xạ âm kém hơn tấm rèm nhung.", False),
            ("d", "Các vật liệu tiêu âm thường được dùng để lót sàn và ốp tường phòng thu âm.", True)
        ], "Gương kính phẳng nhẵn phản xạ âm tốt hơn nhiều so với rèm nhung xốp mềm."),
        make_tf(2, "Thông hiểu", "Về hiện tượng tiếng vang trong đời sống:", [
            ("a", "Tiếng vang là âm phản xạ nghe được tách biệt hẳn với âm trực tiếp.", True),
            ("b", "Đứng trước một vách đá lớn hét to, ta có thể nghe thấy tiếng vang dội lại.", True),
            ("c", "Trong mọi căn phòng dù lớn hay nhỏ, ta đều luôn nghe thấy tiếng vang rõ ràng.", False),
            ("d", "Tiếng sấm rền kéo dài trong cơn mưa giông là do âm phản xạ nhiều lần giữa các đám mây và mặt đất.", True)
        ], "Phòng nhỏ có khoảng cách ngắn (d < 11,3 m) thì âm phản xạ hòa lẫn vào âm trực tiếp, không nghe thành tiếng vang riêng."),
        make_tf(3, "Vận dụng", "Một người đứng trong một hang động đá vôi lớn cách vách hang 34 m và vỗ tay một cái thật mạnh:", [
            ("a", "Tốc độ âm trong không khí trong hang là 340 m/s.", True),
            ("b", "Thời gian âm thanh đi từ người đến vách hang rồi dội ngược trở lại tai là 0,2 giây.", True),
            ("c", "Vì 0,2 giây lớn hơn 1/15 giây (khoảng 0,067 s) nên người đó nghe thấy tiếng vang rất rõ.", True),
            ("d", "Nếu người đó tiến lại gần vách hang cách 5 m thì vẫn nghe thấy tiếng vang tách rời.", False)
        ], "Ở cự li 5 m, t = 10 / 340 ≈ 0,029 s < 1/15 s nên không nghe thấy tiếng vang tách rời."),
        make_tf(4, "Vận dụng", "Các giải pháp chống ô nhiễm tiếng ồn cho khu dân cư cạnh trục đường giao thông lớn:", [
            ("a", "Xây dựng các bức tường chắn cách âm bằng vật liệu tiêu âm cao dọc hai bên đường cao tốc.", True),
            ("b", "Trồng nhiều cây xanh có tán lá rậm rạp giữa dải phân cách và hành lang đường bộ.", True),
            ("c", "Khuyến khích các hộ gia đình lắp đặt hệ thống cửa kính cách âm hai lớp chân không.", True),
            ("d", "Cho phép các phương tiện bấm còi hơi công suất lớn để giải tỏa ách tắc giao thông.", False)
        ], "Bấm còi hơi gây ô nhiễm tiếng ồn nghiêm trọng hơn, bị nghiêm cấm.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Âm phản xạ nghe được cách âm trực tiếp ít nhất bao nhiêu giây thì tạo thành tiếng vang? (Viết dưới dạng phân số tối giản)", "1/15", "1/15 giây."),
        make_sa(2, "Thông hiểu", "Mút xốp là vật liệu phản xạ âm tốt hay kém?", "Kém", "Mút xốp hấp thụ âm tốt, phản xạ âm kém."),
        make_sa(3, "Vận dụng", "Khoảng cách tối thiểu từ người đến vách phản xạ để nghe được tiếng vang trong không khí (v = 340 m/s) là bao nhiêu mét? (Làm tròn 1 chữ số thập phân)", "11.3", "d_min = 340 × (1/15) / 2 ≈ 11,33 m ≈ 11,3 m."),
        make_sa(4, "Vận dụng", "Một người đứng trước một tòa nhà cao tầng hét to và nghe thấy âm dội lại sau 0,4 giây. Biết v = 340 m/s. Tòa nhà cách người đó bao nhiêu mét?", "68", "d = 340 × 0,4 / 2 = 68 m."),
        make_sa(5, "Vận dụng cao", "Máy định vị bằng sóng siêu âm sonar của tàu tuần tra phát xung âm xuống rạn san hô dưới biển và nhận lại tín hiệu sau 0,6 giây. Biết v_nước = 1500 m/s. Độ sâu của rạn san hô là bao nhiêu mét?", "450", "d = 1500 × 0,6 / 2 = 450 m."),
        make_sa(6, "Vận dụng cao", "Tiếng ồn kéo dài vượt quá bao nhiêu decibel (dB) được coi là ngưỡng gây ô nhiễm tiếng ồn có hại cho thính giác?", "85", "Trên 85 dB.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng trước một vách núi đá hoa cương cao vút. Người đó dùng súng phát lệnh bắn một phát lên trời và dùng đồng hồ đo được thời gian từ lúc nổ súng đến khi nghe thấy tiếng vang dội lại từ vách núi là 1,4 giây. Biết tốc độ truyền âm trong không khí là 340 m/s. Khoảng cách từ vị trí người đó đứng đến vách núi là:", ["238 m", "476 m", "170 m", "340 m"], 0, "Quãng đường âm đi và về: 2d = 340 × 1,4 = 476 m => d = 238 m."),
        make_vdc(2, "Một căn phòng học có chiều dài 8 mét, chiều rộng 6 mét, tường quét vôi phẳng nhẵn. Khi một học sinh nói to trong phòng, học sinh đó có nghe thấy tiếng vang của chính giọng nói mình không? Vì sao?", ["Không nghe thấy tiếng vang vì khoảng cách từ học sinh đến tường lớn nhất chỉ khoảng 8 m, nhỏ hơn khoảng cách tối thiểu 11,3 m để tạo tiếng vang", "Có nghe thấy tiếng vang rất to", "Nghe thấy tiếng vang sau 1 giây", "Nghe thấy tiếng vang liên tục"], 0, "Khoảng cách trong phòng học (≤ 8 m) nhỏ hơn cự li tối thiểu 11,3 m nên âm phản xạ đến tai sớm hơn 1/15 s, hòa vào âm trực tiếp làm âm to hơn chứ không tạo tiếng vang riêng."),
        make_vdc(3, "Tại các bệnh viện và trường học, người ta thường cắm biển báo giao thông cấm bấm còi (biển P.128 có hình chiếc còi bị gạch chéo đỏ). Biện pháp chống ô nhiễm tiếng ồn này thuộc nhóm biện pháp nào?", ["Tác động trực tiếp làm giảm độ to tại nguồn phát âm", "Ngăn chặn trên đường truyền âm", "Phân tán âm thanh", "Bảo vệ tai người nghe"], 0, "Cấm bấm còi là biện pháp triệt tiêu tiếng ồn ngay tại nguồn âm."),
        make_vdc(4, "Một người đứng giữa hai bức tường thẳng đứng song song A và B trong một hội trường lớn. Bức tường A cách người đó 17 m, bức tường B cách người đó 51 m. Người đó vỗ tay một cái dứt khoát. Biết tốc độ âm trong không khí là 340 m/s. Người đó sẽ lần lượt nghe thấy hai tiếng vang dội lại từ hai bức tường sau các khoảng thời gian là:", ["0,10 giây và 0,30 giây", "0,05 giây và 0,15 giây", "0,20 giây và 0,60 giây", "0,15 giây và 0,45 giây"], 0, "t_A = 2 × 17 / 340 = 0,10 s; t_B = 2 × 51 / 340 = 0,30 s.")
    ]
}

# --- ĐỀ 2 ---
b14_exams["phys7_c4_b14_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b14", "lessonName": "Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Âm phản xạ là:", ["Âm dội ngược trở lại khi gặp một mặt chắn", "Âm phát ra từ nguồn âm ban đầu", "Âm truyền thẳng qua chướng ngại vật", "Âm bị tắt hẳn trong môi trường"], 0, "Âm dội lại khi gặp mặt chắn gọi là âm phản xạ."),
        make_mc(2, "Nhận biết", "Khi nào thì tai ta nghe được tiếng vang?", ["Khi âm phản xạ đến tai cách âm trực tiếp ít nhất 1/15 giây", "Khi âm phản xạ đến cùng lúc với âm trực tiếp", "Khi âm trực tiếp lớn hơn 100 dB", "Khi ở trong phòng kín nhỏ"], 0, "Tiếng vang xuất hiện khi khoảng cách thời gian giữa âm trực tiếp và âm phản xạ từ 1/15 s trở lên."),
        make_mc(3, "Nhận biết", "Vật liệu nào sau đây phản xạ âm kém nhất (hấp thụ âm tốt nhất)?", ["Tấm xốp cách âm", "Tấm tôn sắt phẳng", "Bức tường gạch trát vữa nhẵn", "Tấm đá hoa cương"], 0, "Xốp mềm có nhiều lỗ khí li ti hấp thụ âm tốt nhất."),
        make_mc(4, "Nhận biết", "Trong các biện pháp sau, biện pháp nào ngăn chặn sự truyền âm vào phòng ngủ?", ["Lắp cửa kính hai lớp cách âm và kéo rèm cửa bằng vải nhung dày", "Mở toang tất cả các cửa sổ", "Bật quạt chạy hết công suất", "Bật loa đài to"], 0, "Cửa kính hộp hai lớp và rèm nhung dày ngăn chặn hiệu quả âm thanh truyền vào phòng."),
        make_mc(5, "Nhận biết", "Tác hại của ô nhiễm tiếng ồn kéo dài đối với sức khỏe con người là:", ["Gây căng thẳng thần kinh, mất ngủ, giảm khả năng tập trung và suy giảm thính lực", "Làm tăng chiều cao", "Làm sáng mắt", "Làm tim đập chậm lại vĩnh viễn"], 0, "Tiếng ồn kéo dài gây hại cho thần kinh, tim mạch và thính giác."),
        make_mc(6, "Nhận biết", "Thiết bị bảo vệ cá nhân nào thường được công nhân làm việc ở công trường máy khoan hoặc sân bay sử dụng?", ["Chụp tai chống ồn (chụp tai giảm âm)", "Kính bảo hộ", "Găng tay da", "Ủng cao su"], 0, "Chụp tai chống ồn ngăn sóng âm cường độ cao tác động vào màng nhĩ."),
        make_mc(7, "Thông hiểu", "Một người đứng trước vách đá cách 85 m hét to một tiếng. Sau bao lâu người đó nghe thấy tiếng vang? (v = 340 m/s)", ["0,5 giây", "0,25 giây", "1,0 giây", "2,0 giây"], 0, "t = 2d / v = (2 × 85) / 340 = 170 / 340 = 0,5 s."),
        make_mc(8, "Thông hiểu", "Vì sao trong các phòng thu âm chuyên nghiệp, người ta không sơn tường bóng loáng mà lại ốp mút gai tam giác hoặc thạch cao đục lỗ?", ["Để triệt tiêu hiện tượng phản xạ âm, tạo môi trường âm học trung thực không bị vang vọng", "Để phòng thu đẹp hơn", "Để phòng thu ấm hơn", "Để chống ẩm"], 0, "Mút gai tán xạ và triệt tiêu sóng âm phản xạ giúp bản thu âm không bị vang dội."),
        make_mc(9, "Thông hiểu", "Biện pháp nào sau đây thuộc nhóm phân tán âm trên đường truyền?", ["Trồng nhiều hàng cây xanh có tán lá rậm rạp giữa khu dân cư và đường quốc lộ", "Yêu cầu tài xế giảm tốc độ", "Xử phạt người bấm còi", "Đeo nút bịt tai"], 0, "Tán lá cây rậm rạp phân tán sóng âm ra nhiều hướng làm giảm năng lượng âm truyền tới."),
        make_mc(10, "Thông hiểu", "Tàu ngầm quân sự phát hiện chướng ngại vật ngầm dưới biển (như rạn san hô, tàu khác) nhờ ứng dụng:", ["Hệ thống định vị sóng âm phản xạ (Sonar)", "Kính thiên văn", "Đèn pha cực mạnh", "Sóng nhiệt"], 0, "Hệ thống Sonar phát xung sóng âm và thu âm phản xạ để định vị vật cản dưới nước."),
        make_mc(11, "Thông hiểu", "Khi hét to trong một hang đá sâu và rộng, ta nghe thấy tiếng vang kéo dài lặp lại nhiều lần. Hiện tượng này là do:", ["Sóng âm phản xạ liên tiếp nhiều lần qua lại giữa các vách đá trong hang", "Hang đá tự phát ra tiếng kêu", "Có người khác nhại lại tiếng", "Gió thổi mạnh trong hang"], 0, "Âm phản xạ nhiều lần giữa các vách đá tạo chuỗi tiếng vang rền."),
        make_mc(12, "Thông hiểu", "Một xưởng cưa gỗ hoạt động phát ra tiếng ồn 95 dB nằm cạnh một trường tiểu học. Biện pháp cấp thiết nhất để bảo vệ học sinh là:", ["Xây tường cách âm cao, chuyển máy cưa vào phòng kín cách âm và yêu cầu xưởng hoạt động ngoài giờ học", "Phát kẹo cho học sinh", "Cho học sinh nghỉ học vĩnh viễn", "Phạt xưởng 10.000 đồng"], 0, "Xây tường cách âm, cách li nguồn ồn và điều chỉnh giờ hoạt động là biện pháp căn cơ.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về sự phản xạ âm trên các bề mặt vật chất khác nhau:", [
            ("a", "Bề mặt tấm thép phẳng phản xạ âm tốt hơn mặt tấm đệm mút.", True),
            ("b", "Mặt hồ nước phẳng lặng có thể phản xạ sóng âm.", True),
            ("c", "Tường nhám, sần sùi phản xạ âm tốt hơn tường quét vôi nhẵn bóng.", False),
            ("d", "Các vật có bề mặt xốp mềm có khả năng tiêu âm (hấp thụ âm) rất tốt.", True)
        ], "Tường nhẵn bóng phản xạ âm tốt hơn tường nhám gồ ghề."),
        make_tf(2, "Thông hiểu", "Về các điều kiện để hình thành tiếng vang:", [
            ("a", "Phải có bề mặt chướng ngại vật cản để phản xạ sóng âm.", True),
            ("b", "Âm phản xạ phải đến tai chậm hơn âm trực tiếp ít nhất 1/15 giây.", True),
            ("c", "Trong không khí ở 20 °C, khoảng cách từ người nói đến vật cản phải từ 11,3 m trở lên.", True),
            ("d", "Nếu đứng cách vật cản 3 m ta vẫn nghe thấy tiếng vang tách bạch.", False)
        ], "Ở cự li 3 m, âm phản xạ đến sau âm trực tiếp khoảng 0,018 s < 1/15 s nên không thành tiếng vang."),
        make_tf(3, "Vận dụng", "Một người gõ búa xuống sàn bê tông của một nhà kho rộng lớn trống không cách bức tường 51 m:", [
            ("a", "Tốc độ âm trong không khí là 340 m/s.", True),
            ("b", "Thời gian âm đi từ vị trí gõ đến tường rồi dội về tai là 0,30 giây.", True),
            ("c", "Người đó nghe thấy tiếng vang của tiếng búa sau đúng 0,30 giây.", True),
            ("d", "Nếu kê đầy các kiện hàng bằng thùng xốp và bông vải vào nhà kho thì tiếng vang sẽ càng to hơn.", False)
        ], "Thùng xốp và bông vải hấp thụ âm cực tốt làm triệt tiêu tiếng vang."),
        make_tf(4, "Vận dụng", "Quy chuẩn tiếng ồn trong khu dân cư đô thị theo tiêu chuẩn môi trường Việt Nam:", [
            ("a", "Giới hạn tiếng ồn tối đa từ 6h đến 21h trong khu dân cư là 70 dB.", True),
            ("b", "Giới hạn tiếng ồn tối đa từ 21h đến 6h sáng hôm sau trong khu dân cư là 55 dB.", True),
            ("c", "Tiếng hát karaoke kẹo kéo ban đêm vượt quá 80 dB là hành vi vi phạm pháp luật về môi trường.", True),
            ("d", "Người dân được phép tự do gây tiếng ồn bất kì lúc nào tại nhà riêng mà không ai có quyền can thiệp.", False)
        ], "Gây tiếng ồn vượt quy chuẩn sau 22h đêm bị xử phạt hành chính theo quy định pháp luật.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Vật có bề mặt nhẵn bóng phản xạ âm tốt hay kém?", "Tốt", "Phản xạ âm tốt."),
        make_sa(2, "Thông hiểu", "Rèm vải nhung dày có tác dụng hấp thụ âm hay phản xạ âm?", "Hấp thụ âm", "Hấp thụ âm tốt."),
        make_sa(3, "Vận dụng", "Một người hét to trước vách núi và nghe thấy tiếng vang sau 1,0 giây. Biết v = 340 m/s. Khoảng cách đến vách núi là bao nhiêu mét?", "170", "d = 340 × 1,0 / 2 = 170 m."),
        make_sa(4, "Vận dụng", "Khoảng cách từ người đến vách phản xạ là 34 m. Sau bao nhiêu giây người đó nghe thấy tiếng vang? (v = 340 m/s)", "0.2", "t = 2 × 34 / 340 = 0,2 s."),
        make_sa(5, "Vận dụng cao", "Tàu nghiên cứu đáy biển dùng sóng siêu âm (v = 1500 m/s) phát xuống vực thẳm và thu lại tín hiệu sau 1,8 giây. Độ sâu của vực thẳm là bao nhiêu mét?", "1350", "d = 1500 × 1,8 / 2 = 1350 m."),
        make_sa(6, "Vận dụng cao", "Đơn vị đo mức độ to của tiếng ồn là gì?", "dB", "Decibel (dB).")
    ],
    "part4": [
        make_vdc(1, "Một người đứng tại vị trí cách một vách núi đá 255 m bắn một phát súng hiệu. Biết tốc độ âm trong không khí là 340 m/s. Sau bao lâu kể từ lúc nổ súng người đó nghe thấy tiếng vang của phát súng dội lại?", ["1,5 giây", "0,75 giây", "1,0 giây", "2,0 giây"], 0, "Quãng đường âm đi và về: 2d = 2 × 255 = 510 m => t = 510 / 340 = 1,5 s."),
        make_vdc(2, "Một căn phòng hòa nhạc có chiều dài từ sân khấu đến bức tường cuối phòng là 20,4 mét. Nếu bức tường cuối phòng là tường bê tông nhẵn bóng thì khi ca sĩ hát một nốt nhạc, âm phản xạ từ tường dội lại sân khấu sau thời gian bao lâu và có gây ra tiếng vang khó chịu không? (Biết v = 340 m/s).", ["Sau 0,12 giây và có gây ra tiếng vang làm nhòe âm thanh", "Sau 0,06 giây và không gây tiếng vang", "Sau 0,20 giây", "Sau 1,0 giây"], 0, "t = 2 × 20,4 / 340 = 0,12 s. Vì 0,12 s > 1/15 s (≈ 0,067 s) nên sẽ tạo ra tiếng vang gây nhòe âm thanh nếu không tiêu âm tường."),
        make_vdc(3, "Để giảm thiểu tác động của tiếng ồn giao thông từ đường cao tốc trên cao vào các khu chung cư cao tầng hai bên đường, giải pháp công trình kiến trúc nào sau đây được đánh giá là hiệu quả và hiện đại nhất?", ["Lắp đặt hệ thống vách chống ồn chuyên dụng bằng vật liệu hấp thụ âm cao cấp bọc quanh hai bên mép đường cao tốc", "Trồng cỏ dưới chân cột cầu", "Sơn lan can cầu màu trắng", "Cấm xe chạy ban ngày"], 0, "Tường chống ồn (noise barrier) lắp đặt trực tiếp trên lan can đường cao tốc ngăn chặn đường truyền âm thanh."),
        make_vdc(4, "Một người đứng cách một vách núi một khoảng d hét to một tiếng. Đúng 0,6 giây sau người đó nghe thấy âm phản xạ đầu tiên dội lại từ vách núi. Nếu người này lùi xa thêm 34 m nữa rồi lại hét to thì sau bao lâu người đó sẽ nghe thấy âm phản xạ dội lại? (Biết tốc độ âm trong không khí là 340 m/s).", ["0,8 giây", "0,7 giây", "0,9 giây", "1,0 giây"], 0, "d = 340 × 0,6 / 2 = 102 m. Khi lùi thêm 34 m: d' = 102 + 34 = 136 m => t' = 2 × 136 / 340 = 0,8 s.")
    ]
}

# --- ĐỀ 3 ---
b14_exams["phys7_c4_b14_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b14", "lessonName": "Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật phản xạ âm tốt là những vật có đặc điểm:", ["Cứng và có bề mặt nhẵn bóng", "Mềm và có bề mặt xốp gồ ghề", "Trong suốt và rất nhẹ", "Hình cầu rỗng"], 0, "Vật cứng có mặt phẳng nhẵn phản xạ âm tốt."),
        make_mc(2, "Nhận biết", "Vật hấp thụ âm tốt (tiêu âm) là những vật có đặc điểm:", ["Mềm, xốp và có bề mặt gồ ghề", "Cứng và phẳng lỳ", "Bằng kim loại sáng bóng", "Bằng đá granit nhẵn"], 0, "Vật mềm xốp, bề mặt gồ ghề tiêu âm tốt."),
        make_mc(3, "Nhận biết", "Âm phản xạ nghe được cách âm trực tiếp ít nhất một khoảng thời gian bằng bao nhiêu thì tai phân biệt được tiếng vang?", ["1/15 giây (xấp xỉ 0,067 s)", "1 giây", "0,5 giây", "1/100 giây"], 0, "1/15 giây là khoảng thời gian tối thiểu phân biệt âm phản xạ tách rời."),
        make_mc(4, "Nhận biết", "Biện pháp nào sau đây giúp ngăn chặn sự truyền âm trực tiếp từ bên ngoài vào trong nhà?", ["Đóng kín các cửa phòng và lắp cửa kính cách âm", "Mở quạt thông gió", "Bật đèn sáng", "Lát sàn gạch men bóng"], 0, "Đóng kín cửa và dùng cửa kính cách âm ngăn chặn âm truyền qua không khí."),
        make_mc(5, "Nhận biết", "Biển báo giao thông P.128 cấm sử dụng còi xe thường được đặt ở:", ["Khu vực gần bệnh viện, viện điều dưỡng và trường học", "Trên đường cao tốc hoang vắng", "Tại các mỏ than", "Ở ngã ba đường đồi núi"], 0, "Cấm còi ở khu vực cần sự yên tĩnh cho người bệnh và học sinh."),
        make_mc(6, "Nhận biết", "Nút bịt tai bằng cao su non hoặc bọt biển được sử dụng nhằm mục đích:", ["Bảo vệ thính giác của người sử dụng khỏi tác hại của tiếng ồn cường độ cao", "Làm ấm tai vào mùa đông", "Để trang trí", "Để nghe nhạc hay hơn"], 0, "Nút bịt tai giảm cường độ âm tác động vào màng nhĩ."),
        make_mc(7, "Thông hiểu", "Một người đứng trước một vách đá lớn cách 51 m và hét to. Thời gian để người đó nghe thấy tiếng vang dội lại là bao nhiêu? (Biết tốc độ âm trong không khí là 340 m/s)", ["0,30 giây", "0,15 giây", "0,60 giây", "0,45 giây"], 0, "t = 2d / v = (2 × 51) / 340 = 102 / 340 = 0,30 s."),
        make_mc(8, "Thông hiểu", "Tại sao trong các nhà thờ cổ hoặc giảng đường đại học lớn, khi một người nói thì tiếng nói nghe rất vang và to hơn bình thường?", ["Vì âm trực tiếp và các âm phản xạ liên tiếp từ tường, trần nhà đến tai gần nhau làm tăng độ to của âm", "Vì trần nhà hút hết âm", "Vì trong nhà thờ không có không khí", "Vì có micro khuếch đại"], 0, "Âm phản xạ gộp cùng âm trực tiếp làm tăng độ to của âm thanh."),
        make_mc(9, "Thông hiểu", "Biện pháp giảm thiểu tiếng ồn bằng cách trồng dải cây xanh tán lá rậm rạp ven đường dựa trên nguyên lí:", ["Tán lá cây làm phân tán sóng âm theo nhiều hướng khác nhau và hấp thụ một phần năng lượng âm", "Cây xanh làm mát không khí", "Lá cây phát ra âm thanh át tiếng còi", "Cây xanh hút hết bụi"], 0, "Tán lá cây đóng vai trò như các mặt tán xạ âm tự nhiên."),
        make_mc(10, "Thông hiểu", "Dơi bắt được những con muỗi nhỏ bay trong đêm tối là nhờ:", ["Sóng siêu âm do dơi phát ra phản xạ lại từ cơ thể con muỗi giúp dơi xác định chính xác vị trí con mồi", "Dơi có mắt nhìn ban đêm cực rõ", "Muỗi phát ra ánh sáng", "Dơi bẫy muỗi bằng mùi hương"], 0, "Sóng siêu âm phản xạ từ con mồi giúp dơi định vị chính xác cự li và phương hướng."),
        make_mc(11, "Thông hiểu", "Tấm thảm len dày trải trên sàn phòng khách có tác dụng âm học là:", ["Hấp thụ âm thanh va đập và tiếng bước chân, giảm thiểu tiếng vang trong phòng", "Làm sàn nhà trơn hơn", "Làm phòng khách tối hơn", "Phản xạ âm thanh to hơn"], 0, "Thảm len tiêu âm và giảm tiếng ồn va đập bước chân."),
        make_mc(12, "Thông hiểu", "Khi một chiếc máy bay phản lực cất cánh, mức cường độ âm đo được ở khoảng cách 50 m có thể đạt 130 dB. Mức âm thanh này:", ["Đạt tới ngưỡng đau tai của con người và có thể làm tổn thương màng nhĩ nếu không có thiết bị bảo hộ", "Rất êm ái", "Bằng tiếng nói thầm", "Hoàn toàn vô hại"], 0, "130 dB là ngưỡng đau tai, gây nguy hiểm cho thính giác.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về khả năng phản xạ và hấp thụ âm thanh của các vật liệu thông dụng:", [
            ("a", "Bức tường ốp đá hoa cương phẳng lỳ phản xạ âm rất tốt.", True),
            ("b", "Tấm xốp đục lỗ tổ ong có khả năng tiêu âm rất cao.", True),
            ("c", "Rèm vải voan mỏng manh cách âm tốt hơn rèm nhung dày hai lớp.", False),
            ("d", "Gỗ dán công nghiệp ép phẳng phản xạ âm tốt hơn bông thủy tinh cách nhiệt.", True)
        ], "Rèm nhung dày cách âm tốt hơn nhiều so với rèm vải mỏng."),
        make_tf(2, "Thông hiểu", "Về sự hình thành tiếng vang trong các không gian khác nhau:", [
            ("a", "Trong một đường hầm dài bằng bê tông, tiếng còi xe vang dội kéo dài rất lâu.", True),
            ("b", "Trong phòng ngủ nhỏ có nhiều chăn ga gối đệm, ta hầu như không nghe thấy tiếng vang.", True),
            ("c", "Để nghe được tiếng vang trong không khí, vật cản phải cách người phát âm ít nhất khoảng 11,3 m.", True),
            ("d", "Nếu đứng cách bức tường 10 m thì người nói sẽ nghe thấy tiếng vang tách rời hoàn toàn với âm phát ra.", False)
        ], "Ở cự li 10 m, âm phản xạ về sau 0,059 s < 1/15 s nên không tạo tiếng vang tách rời."),
        make_tf(3, "Vận dụng", "Học sinh đo khoảng cách đến vách núi bằng phương pháp phản xạ âm thanh:", [
            ("a", "Dùng súng hiệu phát một tiếng nổ ngắn và sắc bén.", True),
            ("b", "Đồng hồ bấm giây đo được thời gian từ lúc súng nổ đến khi nghe tiếng vang là 1,8 giây.", True),
            ("c", "Với tốc độ âm trong không khí là 340 m/s, khoảng cách đến vách núi tính được là 306 m.", True),
            ("d", "Nếu tiến lại gần vách núi một nửa cự li thì thời gian thu tiếng vang sẽ tăng lên gấp đôi.", False)
        ], "Tiến lại gần thì khoảng cách giảm một nửa nên thời gian thu tiếng vang giảm một nửa (còn 0,9 s)."),
        make_tf(4, "Vận dụng", "Phân tích các biện pháp kiểm soát tiếng ồn tại các đô thị lớn:", [
            ("a", "Quy hoạch các khu công nghiệp, nhà máy chế biến xa các khu dân cư tập trung.", True),
            ("b", "Xây dựng các công viên cây xanh và hồ nước sinh thái xen kẽ các khu đô thị.", True),
            ("c", "Khuyến khích người dân sử dụng phương tiện giao thông chạy bằng điện ít tiếng ồn hơn xe động cơ xăng.", True),
            ("d", "Khuyến khích xe tải chở hàng chạy vào các tuyến phố nhỏ lúc nửa đêm để tránh ùn tắc.", False)
        ], "Xe tải lớn chạy vào ngõ phố ban đêm gây ô nhiễm tiếng ồn nghiêm trọng làm mất ngủ người dân.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Tường nhẵn bóng phản xạ âm tốt hay kém?", "Tốt", "Phản xạ âm tốt."),
        make_sa(2, "Thông hiểu", "Tấm mút gai có tác dụng phản xạ âm hay tiêu âm?", "Tiêu âm", "Tiêu âm (hấp thụ âm)."),
        make_sa(3, "Vận dụng", "Một người đứng trước vách đá cách 68 m hét to. Sau bao nhiêu giây người đó nghe thấy tiếng vang? (v = 340 m/s)", "0.4", "t = 2 × 68 / 340 = 0,4 s."),
        make_sa(4, "Vận dụng", "Thời gian từ lúc phát âm đến khi nhận tiếng vang là 0,8 giây. Vận tốc âm là 340 m/s. Khoảng cách đến vách đá là bao nhiêu mét?", "136", "d = 340 × 0,8 / 2 = 136 m."),
        make_sa(5, "Vận dụng cao", "Tàu ngầm phát sóng âm xuống đáy biển và thu lại tiếng vang sau 1,2 giây. Biết tốc độ âm trong nước biển là 1500 m/s. Độ sâu của biển là bao nhiêu mét?", "900", "d = 1500 × 1,2 / 2 = 900 m."),
        make_sa(6, "Vận dụng cao", "Khoảng cách ngắn nhất giữa người phát âm và bức tường phẳng để nghe được tiếng vang trong không khí (v = 340 m/s) là bao nhiêu mét? (Làm tròn 1 chữ số thập phân)", "11.3", "11,3 m.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng trong một thung lũng giữa hai vách núi đá vôi thẳng đứng song song. Người đó bắn một phát súng hiệu thì sau 1,0 giây nghe thấy tiếng vang thứ nhất và sau 1,5 giây nghe thấy tiếng vang thứ hai dội lại từ vách núi đối diện. Biết tốc độ truyền âm trong không khí là 340 m/s. Bề rộng của thung lũng (khoảng cách giữa hai vách núi) là:", ["425 m", "850 m", "510 m", "340 m"], 0, "d1 = 340 × 1,0 / 2 = 170 m; d2 = 340 × 1,5 / 2 = 255 m => Bề rộng thung lũng = d1 + d2 = 170 + 255 = 425 m."),
        make_vdc(2, "Một người đứng trước một bức tường phẳng cao của một sân vận động và vỗ tay thật mạnh. Người đó nhận thấy rằng nếu đứng cách tường từ 12 mét trở lên thì nghe thấy tiếng vang rất rõ, còn nếu đứng gần hơn 10 mét thì không nghe thấy tiếng vang tách rời nữa. Giải thích nào sau đây là chuẩn xác nhất?", ["Vì ở khoảng cách lớn hơn 11,3 m, thời gian âm phản xạ dội lại tai lớn hơn 1/15 giây nên tai phân biệt được âm phản xạ riêng biệt", "Vì bức tường hút hết âm thanh ở cự li gần", "Vì người vỗ tay yếu đi", "Vì không khí bị dồn nén"], 0, "Thời gian phản xạ vượt quá 1/15 giây giúp màng nhĩ phân biệt được hai xung âm riêng biệt."),
        make_vdc(3, "Để phòng ngủ của một căn nhà gần mặt đường quốc lộ được yên tĩnh, gia chủ đã áp dụng đồng thời các giải pháp: lắp cửa sổ kính hộp 2 lớp cách âm chân không, treo rèm cửa bằng vải nhung dày 2 lớp và trồng một hàng cau cảnh tán rậm trước hiên nhà. Các giải pháp này đã ngăn chặn tiếng ồn theo nguyên lí nào?", ["Kết hợp ngăn chặn đường truyền âm (cửa kính, rèm nhung) và phân tán sóng âm (hàng cây cảnh)", "Chỉ giảm âm tại nguồn phát", "Chỉ làm tăng độ to của âm", "Chỉ đổi tần số âm"], 0, "Kết hợp đa giải pháp cản đường truyền và phân tán tiêu âm."),
        make_vdc(4, "Một thiết bị đo độ sâu đáy biển bằng chùm sóng siêu âm Sonar gắn dưới đáy tàu thủy phát ra một xung sóng siêu âm hướng thẳng đứng xuống đáy biển. Sau 0,64 giây, cảm biến trên tàu ghi nhận được xung phản xạ dội lại từ đáy biển. Biết tốc độ truyền sóng siêu âm trong nước biển là 1500 m/s. Độ sâu của đáy biển tại vị trí tàu đang neo đậu là:", ["480 m", "960 m", "320 m", "600 m"], 0, "d = v × t / 2 = 1500 × 0,64 / 2 = 480 m.")
    ]
}
