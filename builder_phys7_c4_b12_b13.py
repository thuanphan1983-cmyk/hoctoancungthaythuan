# -*- coding: utf-8 -*-
"""
CHƯƠNG IV: ÂM THANH - BÀI 12 & BÀI 13 (6 ĐỀ ĐỘC LẬP 100%)
- phys7_c4_b12: Bài 12: Sóng âm (3 đề: test1, test2, test3)
- phys7_c4_b13: Bài 13: Độ to và độ cao của âm (3 đề: test1, test2, test3)
Không trùng lặp, không tiền tố "Đề X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

b12_b13_exams = {}

# =========================================================================
# BÀI 12: SÓNG ÂM (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b12_b13_exams["phys7_c4_b12_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 12: Sóng âm - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b12", "lessonName": "Bài 12: Sóng âm",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Âm thanh được phát ra từ các vật khi chúng:", ["Đang dao động", "Đang đứng yên", "Được chiếu sáng", "Bị nung nóng"], 0, "Tất cả các vật phát ra âm thanh đều đang dao động."),
        make_mc(2, "Nhận biết", "Sóng âm truyền được trong các môi trường nào sau đây?", ["Chất rắn, chất lỏng và chất khí", "Chỉ truyền được trong chất khí", "Chỉ truyền được trong chất rắn", "Truyền được trong chân không"], 0, "Sóng âm truyền được trong cả chất rắn, chất lỏng và chất khí."),
        make_mc(3, "Nhận biết", "Môi trường nào sau đây KHÔNG THỂ truyền được sóng âm?", ["Chân không", "Nước cất", "Không khí", "Thanh thép"], 0, "Chân không không có các hạt vật chất nên không truyền được dao động âm."),
        make_mc(4, "Nhận biết", "So sánh tốc độ truyền âm trong ba trạng thái của vật chất theo thứ tự giảm dần:", ["Chất rắn > Chất lỏng > Chất khí", "Chất khí > Chất lỏng > Chất rắn", "Chất lỏng > Chất khí > Chất rắn", "Chất khí > Chất rắn > Chất lỏng"], 0, "Tốc độ truyền âm giảm dần từ chất rắn đến chất lỏng và chậm nhất trong chất khí."),
        make_mc(5, "Nhận biết", "Tốc độ truyền âm trong không khí ở nhiệt độ 20 °C xấp xỉ bằng:", ["340 m/s", "1500 m/s", "5000 m/s", "300.000 km/s"], 0, "Tốc độ âm trong không khí ở 20 °C là khoảng 340 m/s."),
        make_mc(6, "Nhận biết", "Bộ phận dao động phát ra âm thanh khi gõ vào dùi trống là:", ["Mặt trống", "Thân trống", "Dùi trống", "Chân giá đỡ trống"], 0, "Khi gõ, dùi làm mặt trống dao động đàn hồi phát ra âm thanh."),
        make_mc(7, "Thông hiểu", "Khi một người nói chuyện, bộ phận nào trong cơ thể dao động phát ra âm thanh?", ["Hai dây thanh quản trong thanh quản", "Lưỡi", "Răng", "Vòm họng"], 0, "Luồng khí từ phổi đi qua làm rung hai dây thanh quản phát ra âm thanh tiếng nói."),
        make_mc(8, "Thông hiểu", "Các nhà du hành vũ trụ khi làm việc ngoài không gian bên ngoài tàu vũ trụ không thể nói chuyện trực tiếp với nhau bằng giọng nói mà phải dùng bộ đàm vì:", ["Không gian vũ trụ là môi trường chân không, không thể truyền được âm thanh", "Ngoài vũ trụ quá lạnh", "Mũ phi hành gia quá dày", "Âm thanh bị gió thổi bay"], 0, "Chân không không có phần tử vật chất để truyền sóng âm."),
        make_mc(9, "Thông hiểu", "Người ta gõ một nhát búa vào thanh kim loại dài. Người ở đầu kia nghe thấy âm thanh truyền qua:", ["Kim loại trước rồi mới đến âm thanh truyền qua không khí", "Không khí trước rồi mới đến kim loại", "Cả hai âm cùng một lúc", "Chỉ nghe thấy âm truyền qua không khí"], 0, "Tốc độ âm trong kim loại (rắn) lớn hơn nhiều so với trong không khí (khí) nên âm qua kim loại tới trước."),
        make_mc(10, "Thông hiểu", "Tốc độ truyền âm trong nước biển xấp xỉ bằng:", ["1500 m/s", "340 m/s", "3000 m/s", "1000 km/h"], 0, "Trong chất lỏng (nước biển), tốc độ âm khoảng 1500 m/s."),
        make_mc(11, "Thông hiểu", "Khi áp tai xuống mặt đất, người lính xưa có thể nghe thấy tiếng vó ngựa từ xa trước khi nghe qua không khí vì:", ["Mặt đất (chất rắn) truyền âm thanh nhanh hơn và ít bị suy giảm năng lượng hơn không khí", "Dưới đất có đường hầm", "Mặt đất phát ra âm thanh", "Vó ngựa đập vào đá"], 0, "Chất rắn truyền âm nhanh hơn và bảo toàn năng lượng tốt hơn chất khí."),
        make_mc(12, "Thông hiểu", "Sóng âm là gì?", ["Là sự lan truyền dao động âm trong môi trường vật chất", "Là các tia sáng chiếu vào mắt", "Là dòng các hạt electron", "Là luồng gió thổi"], 0, "Sóng âm là sự lan truyền các dao động cơ học trong môi trường.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét bản chất và sự truyền sóng âm trong các môi trường:", [
            ("a", "Mọi vật phát ra âm thanh đều có nguồn gốc từ sự dao động.", True),
            ("b", "Khi gảy đàn guitar, các sợi dây đàn dao động phát ra âm thanh.", True),
            ("c", "Sóng âm có thể truyền qua lớp tường bê tông của căn phòng.", True),
            ("d", "Âm thanh truyền trong không khí nhanh hơn trong nước.", False)
        ], "Âm truyền trong nước (lỏng ~ 1500 m/s) nhanh hơn nhiều so với trong không khí (khí ~ 340 m/s)."),
        make_tf(2, "Thông hiểu", "Về thí nghiệm đặt chuông điện đang reo trong bình thủy tinh rồi hút dần không khí ra ngoài:", [
            ("a", "Khi bình còn đầy không khí, ta nghe thấy tiếng chuông reo rõ ràng.", True),
            ("b", "Khi bắt đầu hút không khí ra, tiếng chuông reo nghe nhỏ dần.", True),
            ("c", "Khi trong bình gần như là chân không hoàn toàn, ta hầu như không còn nghe thấy tiếng chuông nữa.", True),
            ("d", "Nếu mở van cho không khí tràn trở lại vào bình thì tiếng chuông vẫn bị mất vĩnh viễn.", False)
        ], "Khi không khí vào lại, tiếng chuông lại truyền qua không khí đến tai người nghe rõ ràng."),
        make_tf(3, "Vận dụng", "Hai bạn học sinh chơi trò 'điện thoại ống bơ' bằng hai lon sữa bò nối với nhau bởi một sợi dây dù căng thẳng dài 15 m:", [
            ("a", "Khi bạn A nói vào miệng lon, đáy lon A dao động.", True),
            ("b", "Dao động của đáy lon truyền dọc theo sợi dây dù căng đến đáy lon B.", True),
            ("c", "Đáy lon B dao động làm rung không khí truyền đến tai bạn B.", True),
            ("d", "Nếu sợi dây dù bị chùng xuống hoặc bị tay người khác giữ chặt thì âm thanh vẫn truyền tốt.", False)
        ], "Sợi dây bị chùng hoặc bị bóp chặt sẽ triệt tiêu dao động cơ học, âm thanh không truyền được."),
        make_tf(4, "Vận dụng", "Một tia sét đánh xuống mặt đất cách người quan sát 1020 m trong một ngày mưa giông:", [
            ("a", "Ánh sáng chớp truyền đến mắt người gần như tức thời.", True),
            ("b", "Tốc độ truyền âm thanh trong không khí là 340 m/s.", True),
            ("c", "Thời gian từ lúc thấy tia chớp đến khi nghe thấy tiếng sấm là 3,0 giây.", True),
            ("d", "Nếu sau 5 giây mới nghe thấy tiếng sấm thì vị trí sét đánh cách xa 2000 m.", False)
        ], "s = v × t = 340 × 5 = 1700 m (câu d ghi 2000 m là sai).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Tốc độ truyền âm trong không khí ở 20 °C là bao nhiêu m/s?", "340", "340 m/s."),
        make_sa(2, "Thông hiểu", "Tốc độ truyền âm trong nước biển xấp xỉ bằng bao nhiêu m/s?", "1500", "1500 m/s."),
        make_sa(3, "Vận dụng", "Một người nhìn thấy tia chớp rồi sau 2,0 giây nghe thấy tiếng sấm. Biết v = 340 m/s. Nơi sét đánh cách người đó bao nhiêu mét?", "680", "s = 340 × 2 = 680 m."),
        make_sa(4, "Vận dụng", "Âm thanh truyền trong chất thép với tốc độ 5000 m/s. Để truyền đi quãng đường 1000 m trong thanh ray thép, âm thanh mất thời gian bao nhiêu giây?", "0.2", "t = 1000 / 5000 = 0,2 s."),
        make_sa(5, "Vận dụng cao", "Một người gõ búa vào đầu ống kim loại dài 680 m. Người ở đầu kia nghe thấy tiếng gõ truyền qua không khí (v = 340 m/s) sau bao nhiêu giây?", "2", "t = 680 / 340 = 2 s."),
        make_sa(6, "Vận dụng cao", "Tàu nghiên cứu hải dương phát xung âm thanh xuống đáy biển và thu lại tín hiệu sau 1,4 giây. Với tốc độ âm trong nước là 1500 m/s, độ sâu của biển là bao nhiêu mét?", "1050", "d = 1500 × 1,4 / 2 = 1050 m.")
    ],
    "part4": [
        make_vdc(1, "Một người gõ một nhát búa vào một đầu ống kim loại bằng thép dài 510 m. Người thứ hai áp tai vào đầu kia của ống nghe thấy hai tiếng gõ liên tiếp: một tiếng truyền qua thép và một tiếng truyền qua cột không khí bên trong ống. Biết tốc độ âm trong không khí là 340 m/s và trong thép là 5100 m/s. Khoảng thời gian giữa hai lần nghe thấy tiếng gõ là:", ["1,4 giây", "1,5 giây", "0,1 giây", "1,0 giây"], 0, "t_khí = 510 / 340 = 1,5 s. t_thép = 510 / 5100 = 0,1 s => Khoảng thời gian: 1,5 - 0,1 = 1,4 s."),
        make_vdc(2, "Một người đứng tại một điểm nhìn thấy một công nhân gõ búa lên mặt đe sắt ở đằng xa. Cứ sau mỗi lần búa chạm đe sắt thì đúng 0,5 giây sau người đó mới nghe thấy tiếng đe vang tới tai. Biết tốc độ âm trong không khí là 340 m/s. Khoảng cách từ người quan sát đến vị trí công nhân làm việc là:", ["170 m", "340 m", "85 m", "200 m"], 0, "s = v × t = 340 × 0,5 = 170 m."),
        make_vdc(3, "Tại sao khi đặt ngón tay chạm nhẹ vào thanh quản ở cổ lúc đang phát âm (nói hoặc hát) ta cảm thấy ngón tay bị rung lên?", ["Vì thanh quản đang dao động đàn hồi để phát ra âm thanh", "Vì máu chảy qua mạnh", "Vì ngón tay bị giật điện", "Vì tim đập nhanh"], 0, "Dây thanh quản rung dao động truyền lực làm ngón tay cảm nhận sự rung động."),
        make_vdc(4, "Một người đứng trước một vách núi đá hoa cương lớn hét to một tiếng, sau 0,8 giây người đó nghe thấy tiếng hét của mình dội ngược lại từ vách núi. Biết tốc độ âm trong không khí là 340 m/s. Khoảng cách từ người đó đến vách núi là:", ["136 m", "272 m", "170 m", "340 m"], 0, "Quãng đường âm đi và về: 2d = v × t => d = 340 × 0,8 / 2 = 136 m.")
    ]
}

# --- ĐỀ 2 ---
b12_b13_exams["phys7_c4_b12_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 12: Sóng âm - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b12", "lessonName": "Bài 12: Sóng âm",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật phát ra âm thanh được gọi là:", ["Nguồn âm", "Gương phẳng", "Nhiệt kế", "Pin điện"], 0, "Vật phát ra âm thanh gọi là nguồn âm."),
        make_mc(2, "Nhận biết", "Khi gảy một sợi dây đàn bầu, vật phát ra âm thanh là:", ["Sợi dây đàn đang rung động", "Bầu đàn", "Cần đàn", "Móng gảy"], 0, "Sợi dây đàn dao động là nguồn phát ra âm chính."),
        make_mc(3, "Nhận biết", "Sóng âm lan truyền được trong chất rắn, lỏng, khí là nhờ:", ["Sự dao động của các hạt phần tử cấu tạo nên môi trường", "Ánh sáng chiếu vào", "Điện tích di chuyển", "Từ trường"], 0, "Các hạt phân tử vật chất truyền dao động cho nhau tạo thành sóng âm."),
        make_mc(4, "Nhận biết", "Trên Mặt Trăng không có bầu khí quyển (môi trường chân không). Nếu hai phi hành gia đứng cạnh nhau gõ hai viên đá vào nhau thì:", ["Họ không thể nghe thấy tiếng gõ qua không khí", "Họ nghe thấy rất to", "Họ bị điếc tai", "Viên đá phát sáng"], 0, "Chân không không truyền được âm thanh."),
        make_mc(5, "Nhận biết", "Trong môi trường nào sau đây sóng âm truyền đi với tốc độ lớn nhất?", ["Thanh sắt (chất rắn)", "Nước biển (chất lỏng)", "Không khí (chất khí)", "Khí hydro"], 0, "Chất rắn có liên kết phân tử dày đặc nên truyền âm nhanh nhất."),
        make_mc(6, "Nhận biết", "Âm thanh truyền từ nguồn âm đến tai người nghe thông qua:", ["Sự lan truyền sóng âm trong không khí", "Tia phóng xạ", "Tia laser", "Gió thổi"], 0, "Sóng âm lan truyền làm màng nhĩ tai dao động."),
        make_mc(7, "Thông hiểu", "Khi thổi sáo trúc, cột không khí bên trong ống sáo dao động phát ra âm thanh. Nguồn âm ở đây là:", ["Cột không khí bên trong ống sáo", "Vỏ ngoài ống sáo", "Ngón tay bấm", "Miệng người thổi"], 0, "Luồng hơi làm cột không khí bên trong lòng ống sáo dao động phát ra âm."),
        make_mc(8, "Thông hiểu", "Một người lặn dưới nước vẫn có thể nghe thấy tiếng động cơ của chiếc thuyền chạy trên mặt nước. Điều này chứng tỏ:", ["Sóng âm có thể truyền được trong chất lỏng", "Chất lỏng không truyền được âm", "Người đó có khả năng đặc biệt", "Nước biến thành không khí"], 0, "Chứng minh chất lỏng (nước) là môi trường truyền âm tốt."),
        make_mc(9, "Thông hiểu", "Một tia sét đánh cách người quan sát 1360 m. Thời gian từ lúc thấy ánh chớp đến khi nghe tiếng sấm (v = 340 m/s) là:", ["4,0 giây", "2,0 giây", "3,0 giây", "5,0 giây"], 0, "t = s / v = 1360 / 340 = 4,0 s."),
        make_mc(10, "Thông hiểu", "Tại sao người ta thường làm tường phòng hát karaoke bằng vật liệu mút xốp đục lỗ hoặc bọc vải nỉ nhung?", ["Để ngăn cản và hấp thụ sóng âm, giảm sự truyền âm ra bên ngoài", "Để phòng hát sáng hơn", "Để tường không bị bụi", "Để phòng mát hơn"], 0, "Vật liệu xốp mềm tiêu âm, hạn chế âm thanh truyền ra các phòng xung quanh."),
        make_mc(11, "Thông hiểu", "Tốc độ âm trong không khí ở 0 °C khoảng 331 m/s, ở 20 °C khoảng 340 m/s. Nhận xét nào đúng?", ["Nhiệt độ không khí tăng thì tốc độ truyền âm tăng lên", "Nhiệt độ tăng tốc độ truyền âm giảm", "Tốc độ âm không phụ thuộc nhiệt độ", "Tốc độ âm giảm về 0"], 0, "Nhiệt độ môi trường tăng làm các phân tử chuyển động nhiệt nhanh hơn, tốc độ âm tăng."),
        make_mc(12, "Thông hiểu", "Cá voi và cá heo có thể giao tiếp với nhau ở khoảng cách hàng chục kilômét trong đại dương nhờ:", ["Sóng âm truyền rất xa và nhanh trong môi trường nước", "Chúng dùng ánh sáng", "Chúng bơi lại gần nhau", "Chúng dùng mùi hương"], 0, "Nước biển truyền sóng âm cực tốt và ít bị hấp thụ ở tần số thấp.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc điểm của nguồn âm trong tự nhiên:", [
            ("a", "Mặt trống dao động khi đánh trống phát ra tiếng kêu tùng tùng.", True),
            ("b", "Cánh ong vỗ rất nhanh trong không khí phát ra tiếng vo ve.", True),
            ("c", "Tất cả các nguồn âm đều đứng yên hoàn toàn khi phát ra âm thanh.", False),
            ("d", "Khi âm thoa phát ra âm thanh, các nhánh của nó dao động rất nhanh.", True)
        ], "Mọi nguồn âm bắt buộc phải dao động đàn hồi."),
        make_tf(2, "Thông hiểu", "Về sự lan truyền âm thanh trong đời sống hàng ngày:", [
            ("a", "Tiếng chuông nhà thờ truyền qua không khí đến tai người nghe.", True),
            ("b", "Người áp tai vào vách tường có thể nghe thấy tiếng nói thì thầm từ phòng bên cạnh truyền qua chất rắn.", True),
            ("c", "Nếu đặt một chiếc đồng hồ báo thức vào bình hút chân không thì ta không nghe thấy chuông reo.", True),
            ("d", "Tốc độ truyền âm trong không khí lớn hơn tốc độ truyền âm trong bê tông cốt thép.", False)
        ], "Trong bê tông cốt thép (chất rắn), âm truyền nhanh gấp hơn 10 lần trong không khí."),
        make_tf(3, "Vận dụng", "Học sinh làm thí nghiệm chứng minh mặt trống dao động khi phát ra âm:", [
            ("a", "Rắc vài mẩu giấy vụn nhỏ hoặc hạt xốp lên mặt trống.", True),
            ("b", "Gõ mạnh vào mặt trống, các mẩu giấy vụn nảy lên tung tóe.", True),
            ("c", "Tiếng trống càng to thì các mẩu giấy vụn nảy lên càng cao.", True),
            ("d", "Khi dùng tay giữ chặt mặt trống, mặt trống ngừng dao động nhưng tiếng trống vẫn vang mãi.", False)
        ], "Khi mặt trống ngừng dao động thì âm thanh lập tức tắt hẳn."),
        make_tf(4, "Vận dụng", "Một vụ nổ mìn phá đá tại mỏ đá cách khu dân cư 1700 m:", [
            ("a", "Người dân nhìn thấy cột khói bốc lên trước khi nghe thấy tiếng nổ.", True),
            ("b", "Thời gian âm thanh truyền từ mỏ đá đến khu dân cư qua không khí là 5,0 giây.", True),
            ("c", "Nếu có một đường ray sắt nối thẳng từ mỏ đá về khu dân cư thì âm truyền qua ray sắt mất khoảng 0,34 giây.", True),
            ("d", "Người áp tai xuống mặt đất sẽ nghe thấy tiếng nổ sau người đứng thẳng nghe qua không khí.", False)
        ], "Âm truyền qua mặt đất (chất rắn) nhanh hơn nhiều qua không khí nên người áp tai nghe trước.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một chiếc âm thoa phát ra âm, nhánh âm thoa thực hiện dao động. Nguồn phát ra âm ở đây là gì? (Nhánh âm thoa hay Cán âm thoa)", "Nhánh âm thoa", "Nhánh âm thoa dao động tạo ra âm."),
        make_sa(2, "Thông hiểu", "Tốc độ âm trong một thanh nhôm là khoảng 6420 m/s. Thanh nhôm thuộc thể nào của vật chất? (Rắn, Lỏng hay Khí)", "Rắn", "Nhôm là kim loại thể rắn."),
        make_sa(3, "Vận dụng", "Người nhìn thấy pháo hoa nổ sáng trên bầu trời rồi sau 1,5 giây mới nghe thấy tiếng nổ. Biết v = 340 m/s. Điểm nổ pháo hoa cách người đó bao nhiêu mét?", "510", "s = 340 × 1,5 = 510 m."),
        make_sa(4, "Vận dụng", "Âm thanh truyền trong nước biển với tốc độ 1500 m/s. Trong 0,6 giây, âm truyền đi được bao nhiêu mét?", "900", "s = 1500 × 0,6 = 900 m."),
        make_sa(5, "Vận dụng cao", "Một người đứng cách vách đá hét to, sau 1,2 giây nghe thấy âm phản xạ. Biết v = 340 m/s. Khoảng cách đến vách đá là bao nhiêu mét?", "204", "d = 340 × 1,2 / 2 = 204 m."),
        make_sa(6, "Vận dụng cao", "Tàu đánh cá dùng máy đo hồi âm phát sóng âm xuống đáy biển và nhận lại tín hiệu sau 0,8 giây. Biết tốc độ âm trong nước là 1500 m/s. Độ sâu đáy biển là bao nhiêu mét?", "600", "d = 1500 × 0,8 / 2 = 600 m.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng tại một bờ sông rộng, nhìn sang bờ bên kia thấy một người thợ đóng cọc gỗ bằng búa. Cứ sau mỗi nhát búa đập vào cọc gỗ thì đúng 0,75 giây sau người này mới nghe thấy âm thanh phát ra. Biết tốc độ âm trong không khí là 340 m/s. Bề rộng của khúc sông tại vị trí đó là:", ["255 m", "340 m", "170 m", "510 m"], 0, "s = 340 × 0,75 = 255 m."),
        make_vdc(2, "Để đo khoảng cách giữa hai mỏm núi A và B, một nhà địa chất đứng tại mỏm núi A bắn một phát súng hiệu và đo được thời gian từ lúc bắn đến khi nghe thấy tiếng vang dội lại từ mỏm B là 2,5 giây. Biết tốc độ âm trong không khí là 340 m/s. Khoảng cách giữa hai mỏm núi là:", ["425 m", "850 m", "680 m", "340 m"], 0, "d = 340 × 2,5 / 2 = 425 m."),
        make_vdc(3, "Tại sao khi ta dán chặt một miếng băng dính hoặc đặt bàn tay đè lên mặt trống đang rung thì tiếng trống lập tức tắt ngay?", ["Vì bàn tay cản trở và dập tắt sự dao động của mặt trống, khi nguồn âm ngừng dao động thì âm thanh dừng phát ra", "Vì bàn tay hút hết âm thanh", "Vì dùi trống bị gãy", "Vì không khí bị đẩy ra ngoài"], 0, "Nguồn âm ngừng dao động thì âm thanh ngừng phát ra."),
        make_vdc(4, "Một người gõ một hồi búa vào một đầu ống dẫn nước bằng gang dài 680 m. Người thứ hai ở đầu kia đặt một tai áp sát vào thành ống và tai kia hướng ra ngoài không khí. Người đó sẽ nghe thấy hai tiếng gõ cách nhau một khoảng thời gian là bao nhiêu? Biết tốc độ âm trong không khí là 340 m/s và trong gang là 3400 m/s.", ["1,8 giây", "2,0 giây", "0,2 giây", "1,5 giây"], 0, "t_khí = 680 / 340 = 2,0 s; t_gang = 680 / 3400 = 0,2 s => Cách nhau: 2,0 - 0,2 = 1,8 s.")
    ]
}

# --- ĐỀ 3 ---
b12_b13_exams["phys7_c4_b12_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 12: Sóng âm - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b12", "lessonName": "Bài 12: Sóng âm",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Dụng cụ thí nghiệm hình chữ U bằng thép dùng để tạo ra âm thanh chuẩn trong phòng thí nghiệm là:", ["Âm thoa (tuning fork)", "Lực kế", "Nhiệt kế", "Kính hiển vi"], 0, "Âm thoa là dụng cụ chuẩn phát âm thanh thanh khi gõ."),
        make_mc(2, "Nhận biết", "Khi gõ vào một chiếc cồng chiêng Tây Nguyên, âm thanh phát ra từ:", ["Mặt cồng chiêng đang dao động đàn hồi", "Dùi gõ chiêng", "Khung treo chiêng", "Mặt đất"], 0, "Thân và mặt chiêng dao động phát ra âm thanh trầm vang."),
        make_mc(3, "Nhận biết", "Sóng âm truyền trong không khí theo dạng:", ["Sự lan truyền liên tiếp các lớp không khí co lại (nén) và dãn ra", "Đường thẳng tắp không dao động", "Đường tròn tĩnh", "Tia sáng"], 0, "Sóng âm trong chất khí là các lớp sóng nén và dãn lan truyền."),
        make_mc(4, "Nhận biết", "Trong các môi trường: nước biển, thanh nhôm, không khí và chân không, môi trường có tốc độ truyền âm nhỏ nhất (khác 0) là:", ["Không khí", "Nước biển", "Thanh nhôm", "Chân không"], 0, "Tốc độ âm trong không khí (~ 340 m/s) là nhỏ nhất trong các môi trường vật chất trên."),
        make_mc(5, "Nhận biết", "Màng nhĩ trong tai người có vai trò gì khi nghe âm thanh?", ["Dao động cùng tần số với sóng âm truyền tới và truyền tín hiệu thần kinh lên não", "Phát ra âm thanh", "Lọc sạch bụi", "Chắn gió"], 0, "Màng nhĩ dao động cảm nhận sóng âm truyền đến."),
        make_mc(6, "Nhận biết", "Hiện tượng sóng âm truyền từ vật phát ra âm tới tai người nghe chứng tỏ:", ["Sóng âm mang theo năng lượng", "Sóng âm không có năng lượng", "Sóng âm là ánh sáng", "Sóng âm làm nóng môi trường"], 0, "Sóng âm mang năng lượng làm dao động màng nhĩ tai."),
        make_mc(7, "Thông hiểu", "Một người đứng xem bắn pháo hoa thấy chùm pháo hoa lóe sáng rồi 3,0 giây sau mới nghe thấy tiếng nổ. Biết v = 340 m/s. Khoảng cách đến pháo hoa là:", ["1020 m", "340 m", "680 m", "1500 m"], 0, "s = 340 × 3,0 = 1020 m."),
        make_mc(8, "Thông hiểu", "Vì sao người ta có thể dùng ống nghe y tế (ống nghe bác sĩ) để nghe rõ nhịp tim và tiếng thở của bệnh nhân?", ["Vì ống nghe dẫn sóng âm truyền qua chất rắn và chất khí bên trong ống đến tai bác sĩ mà ít bị thất thoát năng lượng", "Vì ống nghe khuếch đại dòng điện", "Vì ống nghe phát ra siêu âm", "Vì ống nghe làm tim đập to hơn"], 0, "Ống nghe định hướng sóng âm tập trung truyền thẳng vào tai bác sĩ."),
        make_mc(9, "Thông hiểu", "Khi một con ruồi hoặc muỗi bay qua tai, ta nghe thấy tiếng vo ve là do:", ["Đôi cánh của chúng vỗ (dao động) rất nhanh trong không khí", "Miệng chúng kêu", "Chân chúng cọ vào nhau", "Mắt chúng chớp"], 0, "Cánh muỗi/ruồi dao động hàng trăm lần trong 1 giây phát ra âm thanh."),
        make_mc(10, "Thông hiểu", "Khi áp tai vào một chiếc cốc thủy tinh rỗng úp lên mặt bàn gỗ rồi gõ nhẹ vào đầu bàn kia, ta nghe thấy tiếng gõ rất rõ. Điều đó chứng tỏ:", ["Chất rắn truyền âm rất tốt", "Cốc thủy tinh phát ra âm thanh", "Bàn gỗ không truyền được âm", "Mặt bàn bị vỡ"], 0, "Gỗ và thủy tinh (chất rắn) truyền dao động âm rất hiệu quả."),
        make_mc(11, "Thông hiểu", "Sự truyền âm trong chất rắn nhanh hơn trong chất khí chủ yếu là do:", ["Các phân tử trong chất rắn liên kết chặt chẽ và ở gần nhau hơn nhiều so với chất khí", "Chất rắn nặng hơn chất khí", "Chất rắn trong suốt hơn", "Chất khí cản trở âm thanh"], 0, "Khoảng cách giữa các hạt phân tử chất rắn rất nhỏ nên việc truyền xung lượng dao động diễn ra nhanh hơn."),
        make_mc(12, "Thông hiểu", "Khi lặn sâu dưới hồ bơi, nếu có người gõ hai viên đá vào nhau dưới nước thì người thợ lặn:", ["Nghe thấy tiếng gõ rất rõ ràng", "Hoàn toàn không nghe thấy gì", "Chỉ nhìn thấy bọt khí", "Nghe thấy tiếng sét"], 0, "Nước truyền âm rất tốt nên thợ lặn nghe rất rõ.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các hiện tượng liên quan đến nguồn âm trong thực tế:", [
            ("a", "Thổi sáo trúc làm cột không khí bên trong ống sáo dao động phát ra âm thanh.", True),
            ("b", "Khi gảy đàn guitar, chỉ có thùng đàn dao động chứ dây đàn không chuyển động.", False),
            ("c", "Khi bật loa phát nhạc, màng loa chuyển động rung qua lại liên tục.", True),
            ("d", "Dây chun kéo căng khi gảy nhẹ sẽ dao động và phát ra âm thanh nhỏ.", True)
        ], "Dây đàn bắt buộc phải dao động khi gảy."),
        make_tf(2, "Thông hiểu", "Về khả năng truyền âm của các môi trường:", [
            ("a", "Tường gạch và cửa kính đều có thể truyền được âm thanh.", True),
            ("b", "Các loài cá dưới nước có thể nghe được tiếng chân người bước trên bờ để bơi đi lẩn trốn.", True),
            ("c", "Trong chân không, tốc độ truyền âm đạt tới 300.000 km/s.", False),
            ("d", "Nhiệt độ không khí càng cao thì tốc độ truyền âm trong không khí càng tăng nhẹ.", True)
        ], "Trong chân không hoàn toàn không truyền được âm (tốc độ bằng 0). 300.000 km/s là tốc độ ánh sáng."),
        make_tf(3, "Vận dụng", "Thí nghiệm gõ một nhánh âm thoa rồi nhúng nhẹ đầu nhánh vào một cốc nước:", [
            ("a", "Các giọt nước trong cốc bắn tung tóe ra xung quanh.", True),
            ("b", "Hiện tượng nước bắn tung tóe chứng tỏ nhánh âm thoa đang dao động đàn hồi.", True),
            ("c", "Nếu không gõ âm thoa mà nhúng vào nước thì nước vẫn bắn tung tóe như vậy.", False),
            ("d", "Khi âm thoa ngừng kêu thì nước trong cốc trở lại trạng thái mặt phẳng lặng.", True)
        ], "Nếu không gõ thì âm thoa không dao động, nước không thể bắn tung tóe."),
        make_tf(4, "Vận dụng", "Một người thợ lặn ở độ sâu 15 m dưới đáy hồ nước nghe thấy tiếng nổ phát ra từ một chiếc cano trên mặt hồ:", [
            ("a", "Sóng âm truyền từ động cơ cano qua lớp nước hồ tới tai người thợ lặn.", True),
            ("b", "Tốc độ âm trong nước lớn hơn trong không khí nên sóng âm đến thợ lặn rất nhanh.", True),
            ("c", "Nếu thợ lặn ở trên Mặt Trăng lặn trong hồ cồn không có khí quyển thì vẫn nghe thấy âm thanh truyền trong chất lỏng.", True),
            ("d", "Âm thanh hoàn toàn không thể truyền từ không khí vào trong nước.", False)
        ], "Âm thanh truyền được qua ranh giới giữa không khí và nước.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một chiếc chuông đồng khi đánh phát ra âm thanh. Bộ phận nào dao động? (Thành chuông hay Dây treo)", "Thành chuông", "Thành chuông đồng dao động phát ra âm thanh."),
        make_sa(2, "Thông hiểu", "Sóng âm có truyền được qua bức tường bê tông không? (Có hay Không)", "Có", "Bê tông là chất rắn truyền âm tốt."),
        make_sa(3, "Vận dụng", "Một tiếng sấm rền vang sau tia chớp 4,0 giây. Tốc độ âm trong không khí là 340 m/s. Khoảng cách từ tia sét đến người quan sát là bao nhiêu mét?", "1360", "s = 340 × 4 = 1360 m."),
        make_sa(4, "Vận dụng", "Âm thanh truyền trong nước biển với tốc độ 1500 m/s. Để truyền đi quãng đường 3000 m, âm thanh cần thời gian bao nhiêu giây?", "2", "t = 3000 / 1500 = 2 s."),
        make_sa(5, "Vận dụng cao", "Một người gõ búa vào thanh kim loại dài 850 m. Âm truyền qua không khí (v = 340 m/s) mất thời gian bao nhiêu giây?", "2.5", "t = 850 / 340 = 2,5 s."),
        make_sa(6, "Vận dụng cao", "Tàu nghiên cứu đáy đại dương phát xung âm sonar xuống đáy biển và nhận lại tín hiệu sau 2,0 giây. Độ sâu của đáy đại dương là bao nhiêu mét? (v = 1500 m/s)", "1500", "d = 1500 × 2 / 2 = 1500 m.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng cách một vách núi đá vôi thẳng đứng và bắn một phát súng hiệu. Sau 1,6 giây, người đó nghe thấy tiếng vang của phát súng dội lại từ vách núi. Biết tốc độ truyền âm trong không khí là 340 m/s. Khoảng cách từ vị trí bắn súng đến vách núi là:", ["272 m", "544 m", "170 m", "340 m"], 0, "Quãng đường âm đi và về: 2d = 340 × 1,6 = 544 m => d = 272 m."),
        make_vdc(2, "Một người gõ búa vào đường ray xe lửa bằng thép. Một người khác ở cách đó 1700 m áp tai vào đường ray sắt. Biết tốc độ âm trong thép là 5100 m/s và trong không khí là 340 m/s. Người này nghe thấy tiếng gõ truyền qua đường ray thép sớm hơn tiếng gõ truyền qua không khí một khoảng thời gian là:", ["4,67 giây", "5,00 giây", "0,33 giây", "4,00 giây"], 0, "t_khí = 1700 / 340 = 5,0 s. t_thép = 1700 / 5100 = 0,333 s => Chênh lệch: 5,0 - 0,333 ≈ 4,67 s."),
        make_vdc(3, "Trong một bộ phim khoa học viễn tưởng, một con tàu vũ trụ bị nổ tung ngoài không gian chân không kèm theo tiếng nổ vang dội làm rung chuyển một con tàu vũ trụ khác ở gần đó. Xét về mặt vật lý học, cảnh phim này có điểm nào không chính xác?", ["Trong không gian chân không không có môi trường truyền âm nên người trên tàu vũ trụ bên cạnh hoàn toàn không thể nghe thấy tiếng nổ", "Tàu vũ trụ không thể nổ", "Không thể có ánh sáng", "Tàu vũ trụ chạy chậm"], 0, "Chân không không truyền được âm thanh, không thể nghe thấy tiếng nổ ngoài không gian."),
        make_vdc(4, "Một đoàn xe quân sự di chuyển trên đường đất. Người bảo vệ đứng cách đó 680 m áp tai xuống mặt đất nghe thấy tiếng rung của động cơ sau 0,4 giây. Tốc độ truyền âm thanh đo được trong nền đất cát ở khu vực này là:", ["1700 m/s", "340 m/s", "1500 m/s", "850 m/s"], 0, "v = s / t = 680 / 0,4 = 1700 m/s.")
    ]
}

# =========================================================================
# BÀI 13: ĐỘ TO VÀ ĐỘ CAO CỦA ÂM (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b12_b13_exams["phys7_c4_b13_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 13: Độ to và độ cao của âm - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b13", "lessonName": "Bài 13: Độ to và độ cao của âm",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Số dao động mà một vật thực hiện được trong thời gian 1 giây được gọi là:", ["Tần số dao động", "Biên độ dao động", "Độ to của âm", "Tốc độ âm"], 0, "Tần số dao động là số dao động trong 1 giây."),
        make_mc(2, "Nhận biết", "Đơn vị đo của tần số dao động là:", ["Hertz (Hz)", "Decibel (dB)", "Mét trên giây (m/s)", "Giây (s)"], 0, "Đơn vị đo tần số là Hertz, kí hiệu là Hz."),
        make_mc(3, "Nhận biết", "Độ cao của âm (âm bổng hay âm trầm) phụ thuộc vào đại lượng nào sau đây?", ["Tần số dao động của nguồn âm", "Biên độ dao động của nguồn âm", "Khoảng cách từ nguồn đến tai", "Khối lượng nguồn âm"], 0, "Độ cao của âm gắn liền với tần số dao động."),
        make_mc(4, "Nhận biết", "Độ to của âm nghe được phụ thuộc trực tiếp vào đại lượng nào?", ["Biên độ dao động của nguồn âm", "Tần số dao động của nguồn âm", "Hình dạng nguồn âm", "Vật liệu làm nguồn âm"], 0, "Biên độ dao động càng lớn thì âm phát ra nghe càng to."),
        make_mc(5, "Nhận biết", "Đơn vị thường dùng để đo mức độ to của âm (mức cường độ âm) là:", ["Decibel (dB)", "Hertz (Hz)", "Mét (m)", "Kilôgam (kg)"], 0, "Độ to của âm được đo bằng đơn vị Decibel (dB)."),
        make_mc(6, "Nhận biết", "Tai người bình thường có thể nghe được âm thanh trong dải tần số từ:", ["16 Hz đến 20.000 Hz", "Dưới 16 Hz", "Trên 20.000 Hz", "100 Hz đến 1.000 Hz"], 0, "Dải tần số tai người cảm nhận được là 16 Hz - 20.000 Hz."),
        make_mc(7, "Thông hiểu", "Một vật trong thời gian 5 giây thực hiện được 200 dao động. Tần số dao động của vật là:", ["40 Hz", "1000 Hz", "200 Hz", "50 Hz"], 0, "f = 200 / 5 = 40 Hz."),
        make_mc(8, "Thông hiểu", "Khi gảy một dây đàn guitar thật mạnh, ta nghe thấy âm thanh phát ra:", ["To hơn vì biên độ dao động của dây đàn lớn hơn", "Bổng hơn", "Trầm hơn", "Không đổi"], 0, "Gảy mạnh làm dây đàn lệch nhiều hơn khỏi VTCB (biên độ lớn) => âm to hơn."),
        make_mc(9, "Thông hiểu", "Âm thanh có tần số nhỏ hơn 16 Hz được gọi là:", ["Hạ âm", "Siêu âm", "Tạp âm", "Âm bổng"], 0, "Dưới 16 Hz gọi là hạ âm."),
        make_mc(10, "Thông hiểu", "Âm thanh có tần số lớn hơn 20.000 Hz được gọi là:", ["Siêu âm", "Hạ âm", "Âm trầm", "Nhạc âm"], 0, "Trên 20.000 Hz gọi là siêu âm."),
        make_mc(11, "Thông hiểu", "Để đàn phát ra âm bổng hơn, người nhạc công thường vặn khóa đàn để:", ["Làm dây đàn căng hơn", "Làm dây đàn chùng hơn", "Làm dây đàn dài hơn", "Làm dây đàn nặng hơn"], 0, "Dây đàn căng hơn sẽ dao động nhanh hơn (tần số lớn hơn) => âm phát ra bổng hơn."),
        make_mc(12, "Thông hiểu", "Tiếng nói thầm thì có độ to khoảng bao nhiêu decibel (dB)?", ["Khoảng 20 - 30 dB", "Khoảng 80 - 90 dB", "Khoảng 120 dB", "0 dB"], 0, "Tiếng thì thầm có mức cường độ âm khoảng 20 - 30 dB.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về mối quan hệ giữa dao động và đặc tính của âm thanh:", [
            ("a", "Vật dao động càng nhanh (tần số càng lớn) thì âm phát ra càng bổng.", True),
            ("b", "Vật dao động càng chậm (tần số càng nhỏ) thì âm phát ra càng trầm.", True),
            ("c", "Độ lệch lớn nhất của vật dao động so với vị trí cân bằng gọi là biên độ dao động.", True),
            ("d", "Biên độ dao động càng lớn thì âm phát ra càng bổng.", False)
        ], "Biên độ dao động quyết định độ to của âm, không quyết định độ cao."),
        make_tf(2, "Thông hiểu", "Về khả năng cảm nhận âm thanh của con người và các loài động vật:", [
            ("a", "Tai người không thể nghe được sóng hạ âm (tần số dưới 16 Hz).", True),
            ("b", "Tai người không thể nghe được sóng siêu âm (tần số trên 20.000 Hz).", True),
            ("c", "Loài dơi và cá heo sử dụng sóng siêu âm để định vị săn mồi trong bóng tối.", True),
            ("d", "Chó có thể nghe được các âm thanh siêu âm mà tai người không nghe thấy.", True)
        ], "Các ý đều đúng với sinh học và vật lý âm thanh."),
        make_tf(3, "Vận dụng", "Xét hai chiếc lá thép 1 và 2 đàn hồi kẹp chặt một đầu trên mặt bàn:", [
            ("a", "Lá thép 1 thực hiện 150 dao động trong 3 giây, tần số là 50 Hz.", True),
            ("b", "Lá thép 2 thực hiện 360 dao động trong 6 giây, tần số là 60 Hz.", True),
            ("c", "Âm do lá thép 1 phát ra nghe bổng hơn âm do lá thép 2 phát ra.", False),
            ("d", "Tai người hoàn toàn có thể nghe được âm thanh do cả hai lá thép phát ra.", True)
        ], "f2 = 60 Hz > f1 = 50 Hz nên lá thép 2 phát ra âm bổng hơn lá thép 1."),
        make_tf(4, "Vận dụng", "Khi chỉnh âm lượng của một chiếc loa nghe nhạc từ mức nhỏ lên mức to cực đại:", [
            ("a", "Màng loa dao động với biên độ lớn hơn nhiều.", True),
            ("b", "Tần số dao động của nốt nhạc phát ra bị thay đổi thành nốt khác.", False),
            ("c", "Âm thanh phát ra to hơn và truyền đi được xa hơn.", True),
            ("d", "Nếu độ to vượt quá ngưỡng 130 dB có thể gây đau nhức màng nhĩ tai.", True)
        ], "Tăng âm lượng chỉ làm tăng biên độ dao động, không làm thay đổi tần số (cao độ) của nốt nhạc.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một vật thực hiện 120 dao động trong 2 giây. Tần số dao động của vật là bao nhiêu Hz?", "60", "f = 120 / 2 = 60 Hz."),
        make_sa(2, "Thông hiểu", "Đơn vị đo độ to của âm có kí hiệu là gì?", "dB", "Decibel, kí hiệu là dB."),
        make_sa(3, "Vận dụng", "Âm thanh có tần số 25.000 Hz thuộc vùng sóng nào? (Siêu âm hay Hạ âm)", "Siêu âm", "f > 20.000 Hz là siêu âm."),
        make_sa(4, "Vận dụng", "Một con muỗi đập cánh 1200 lần trong 2 giây. Tần số đập cánh của muỗi là bao nhiêu Hz?", "600", "f = 1200 / 2 = 600 Hz."),
        make_sa(5, "Vận dụng cao", "Một vật dao động với chu kì thực hiện 1 dao động mất 0,005 giây. Tần số dao động của vật là bao nhiêu Hz?", "200", "f = 1 / 0,005 = 200 Hz."),
        make_sa(6, "Vận dụng cao", "Mức giới hạn độ to của âm thanh mà nếu kéo dài liên tục sẽ gây nguy hại cho thính giác của con người là bao nhiêu decibel (dB)?", "85", "Tiếng ồn trên 85 dB kéo dài gây hại cho thính giác.")
    ],
    "part4": [
        make_vdc(1, "Một người gảy một sợi dây đàn guitar dài 60 cm phát ra nốt La chuẩn (tần số 440 Hz). Khi người này dùng ngón tay bấm chặt vào phím đàn chia đôi sợi dây đàn (chiều dài còn 30 cm) rồi gảy với cùng lực như trước thì âm phát ra sẽ thay đổi như thế nào?", ["Âm phát ra bổng hơn gấp đôi (tần số tăng lên 880 Hz)", "Âm phát ra trầm hơn", "Âm phát ra to hơn gấp 4 lần", "Âm không đổi"], 0, "Chiều dài dây giảm một nửa thì tần số dao động tăng gấp đôi, âm bổng hơn."),
        make_vdc(2, "Máy siêu âm dùng trong y khoa chẩn đoán hình ảnh ổ bụng hoặc theo dõi thai nhi thường phát sóng âm có tần số trong khoảng 2 MHz đến 10 MHz (1 MHz = 1.000.000 Hz). Phát biểu nào sau đây đúng về loại sóng này?", ["Là sóng siêu âm có tần số rất cao, tai người hoàn toàn không nghe thấy và an toàn cho mô sống", "Là sóng hạ âm tai người nghe rõ", "Là tia phóng xạ nguy hiểm", "Là sóng ánh sáng nhìn thấy"], 0, "Sóng siêu âm y tế có tần số hàng triệu Hz, an toàn và tai người không nghe thấy."),
        make_vdc(3, "Cho 3 vật dao động: Vật A thực hiện 80 dao động trong 4 giây; Vật B thực hiện 150 dao động trong 5 giây; Vật C thực hiện 180 dao động trong 3 giây. Sắp xếp các vật theo thứ tự phát ra âm từ trầm nhất đến bổng nhất:", ["Vật A (20 Hz) < Vật B (30 Hz) < Vật C (60 Hz)", "Vật C < Vật B < Vật A", "Vật B < Vật A < Vật C", "Vật A < Vật C < Vật B"], 0, "fA = 80/4 = 20 Hz; fB = 150/5 = 30 Hz; fC = 180/3 = 60 Hz => Trầm nhất là A, bổng nhất là C."),
        make_vdc(4, "Trong dàn nhạc giao hưởng, tiếng kèn tuba phát ra âm trầm sâu lắng (tần số khoảng 40 Hz), trong khi tiếng sáo piccolo phát ra âm rất cao và bổng (tần số khoảng 4000 Hz). So sánh số dao động của cột không khí trong hai nhạc cụ này trong thời gian 1 giây:", ["Cột không khí trong sáo piccolo dao động nhiều gấp 100 lần so với trong kèn tuba", "Cột không khí trong kèn tuba dao động nhiều hơn", "Cả hai dao động bằng nhau", "Không thể so sánh"], 0, "Piccolo 4000 dao động/giây, Tuba 40 dao động/giây => Gấp: 4000 / 40 = 100 lần.")
    ]
}

# --- ĐỀ 2 ---
b12_b13_exams["phys7_c4_b13_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 13: Độ to và độ cao của âm - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b13", "lessonName": "Bài 13: Độ to và độ cao của âm",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Âm phát ra càng bổng (càng cao) khi:", ["Tần số dao động của nguồn âm càng lớn", "Tần số dao động càng nhỏ", "Biên độ dao động càng lớn", "Biên độ dao động càng nhỏ"], 0, "Tần số càng lớn âm phát ra càng bổng."),
        make_mc(2, "Nhận biết", "Âm phát ra càng trầm (càng thấp) khi:", ["Tần số dao động của nguồn âm càng nhỏ", "Tần số dao động càng lớn", "Vật dao động càng mạnh", "Vật đứng yên"], 0, "Tần số nhỏ làm âm trầm."),
        make_mc(3, "Nhận biết", "Độ lệch lớn nhất của vật dao động so với vị trí cân bằng được gọi là:", ["Biên độ dao động", "Tần số dao động", "Độ cao của âm", "Vận tốc âm"], 0, "Biên độ là khoảng cách lệch lớn nhất so với VTCB."),
        make_mc(4, "Nhận biết", "Âm nghe được càng to khi:", ["Biên độ dao động của nguồn âm càng lớn", "Biên độ dao động càng nhỏ", "Tần số dao động càng nhỏ", "Khoảng cách đến nguồn âm càng xa"], 0, "Biên độ lớn thì âm nghe to."),
        make_mc(5, "Nhận biết", "Tiếng ồn của máy bay phản lực cất cánh ở cự li gần có thể đạt độ to khoảng:", ["120 - 130 dB (ngưỡng đau nhức tai)", "40 dB", "60 dB", "10 dB"], 0, "Tiếng máy bay phản lực cất cánh đạt tới 120 - 130 dB."),
        make_mc(6, "Nhận biết", "Hạ âm là âm thanh có tần số:", ["Dưới 16 Hz", "Từ 16 Hz đến 20.000 Hz", "Trên 20.000 Hz", "Trên 1.000 Hz"], 0, "Hạ âm có tần số dưới 16 Hz."),
        make_mc(7, "Thông hiểu", "Một con lắc thực hiện 60 dao động trong thời gian 30 giây. Tần số dao động của con lắc là:", ["2 Hz", "0,5 Hz", "1800 Hz", "30 Hz"], 0, "f = 60 / 30 = 2 Hz."),
        make_mc(8, "Thông hiểu", "Âm thanh do con lắc ở câu trên phát ra có nghe được bằng tai người không?", ["Không nghe được vì tần số 2 Hz nhỏ hơn 16 Hz (thuộc vùng hạ âm)", "Nghe được rất rõ", "Nghe thấy tiếng vo ve", "Nghe thấy tiếng rít"], 0, "2 Hz < 16 Hz là hạ âm, tai người không nghe được."),
        make_mc(9, "Thông hiểu", "Khi nói to và nói thì thầm, đặc tính nào của âm thanh bị thay đổi chủ yếu?", ["Độ to của âm thay đổi (do biên độ dao động của dây thanh quản thay đổi)", "Độ cao của âm", "Tốc độ truyền âm trong không khí", "Bản chất sóng âm"], 0, "Nói to làm biên độ dao động lớn hơn, độ to tăng lên."),
        make_mc(10, "Thông hiểu", "Loài voi có thể giao tiếp với nhau qua khoảng cách hàng chục kilômét bằng loại sóng âm nào?", ["Sóng hạ âm truyền qua mặt đất và không khí", "Sóng siêu âm", "Sóng radio", "Ánh sáng"], 0, "Voi phát ra hạ âm tần số dưới 16 Hz truyền rất xa."),
        make_mc(11, "Thông hiểu", "Khi gõ nhẹ vào mặt trống rồi gõ mạnh hơn, đại lượng nào sau đây của âm phát ra thay đổi?", ["Độ to của âm tăng lên", "Độ cao của âm tăng lên", "Tần số âm tăng lên", "Tốc độ âm tăng lên"], 0, "Gõ mạnh làm tăng biên độ dao động, âm to hơn."),
        make_mc(12, "Thông hiểu", "Giọng nói của phụ nữ thường bổng hơn giọng nói của nam giới là do:", ["Dây thanh quản của phụ nữ thường ngắn và mỏng hơn nên dao động với tần số cao hơn", "Dây thanh quản của phụ nữ dày hơn", "Phụ nữ nói to hơn", "Dây thanh quản của nam giới dao động nhanh hơn"], 0, "Dây thanh quản ngắn và mảnh dao động nhanh hơn => giọng bổng hơn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc trưng sinh lý và vật lý của âm thanh:", [
            ("a", "Độ cao của âm gắn liền với tần số dao động.", True),
            ("b", "Độ to của âm gắn liền với biên độ dao động.", True),
            ("c", "Âm có tần số 1000 Hz nghe trầm hơn âm có tần số 200 Hz.", False),
            ("d", "Khi lại gần nguồn âm, ta nghe thấy âm to hơn so với khi ở xa.", True)
        ], "1000 Hz bổng hơn nhiều so với 200 Hz."),
        make_tf(2, "Thông hiểu", "Về sóng siêu âm và các ứng dụng khoa học công nghệ:", [
            ("a", "Sóng siêu âm có tần số vượt quá 20.000 Hz.", True),
            ("b", "Máy rửa siêu âm dùng rung động siêu âm tần số cao để làm sạch trang sức và linh kiện đồng hồ.", True),
            ("c", "Dơi phát sóng siêu âm và thu tiếng vang dội lại để tránh chướng ngại vật khi bay đêm.", True),
            ("d", "Tai người có thể nghe được tiếng dơi phát ra khi bay săn mồi.", False)
        ], "Dơi phát siêu âm tai người hoàn toàn không nghe thấy."),
        make_tf(3, "Vận dụng", "Một lá thép kẹp chặt trên ê tô có chiều dài phần tự do thay đổi được:", [
            ("a", "Khi để phần tự do dài 20 cm, gảy nhẹ lá thép dao động chậm, phát ra âm trầm.", True),
            ("b", "Khi rút ngắn phần tự do còn 10 cm, gảy nhẹ lá thép dao động nhanh hơn, phát ra âm bổng hơn.", True),
            ("c", "Chiều dài tự do của lá thép càng ngắn thì tần số dao động càng lớn.", True),
            ("d", "Nếu gảy thật mạnh ở cả hai trường hợp thì âm phát ra đều có độ to bằng nhau tuyệt đối.", False)
        ], "Độ to phụ thuộc vào biên độ gảy mạnh hay nhẹ."),
        make_tf(4, "Vận dụng", "Xét tiếng ve kêu râm ran vào mùa hè trên các cành cây:", [
            ("a", "Ve sầu đực phát ra âm thanh nhờ các màng phát âm đặc biệt ở dưới bụng rung động cực nhanh.", True),
            ("b", "Tần số dao động của màng phát âm ve sầu có thể đạt vài nghìn Hertz nên tiếng ve kêu rất chói tai.", True),
            ("c", "Độ to tiếng ve kêu vào buổi trưa hè có thể đạt tới 70 - 80 dB.", True),
            ("d", "Âm thanh của ve sầu là sóng hạ âm nên người điếc cũng nghe được.", False)
        ], "Tiếng ve sầu thuộc dải âm nghe được có tần số cao, không phải hạ âm.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một vật thực hiện được 50 dao động trong 1 giây. Tần số dao động là bao nhiêu Hz?", "50", "50 Hz."),
        make_sa(2, "Thông hiểu", "Âm thanh có tần số 10 Hz thuộc vùng sóng nào? (Hạ âm hay Siêu âm)", "Hạ âm", "f < 16 Hz là hạ âm."),
        make_sa(3, "Vận dụng", "Con ong mật khi bay đập cánh 440 lần trong 1 giây. Tần số dao động của cánh ong là bao nhiêu Hz?", "440", "440 Hz."),
        make_sa(4, "Vận dụng", "Một thanh kim loại dao động với tần số 100 Hz. Trong 5 giây thanh kim loại thực hiện được bao nhiêu dao động?", "500", "N = f × t = 100 × 5 = 500 dao động."),
        make_sa(5, "Vận dụng cao", "Độ to của tiếng nói chuyện bình thường giữa hai người ở khoảng cách 1 mét vào khoảng bao nhiêu decibel (dB)?", "60", "Khoảng 50 - 60 dB."),
        make_sa(6, "Vận dụng cao", "Một vật dao động thực hiện 1500 dao động trong 3 giây. Tần số dao động là bao nhiêu Hz?", "500", "f = 1500 / 3 = 500 Hz.")
    ],
    "part4": [
        make_vdc(1, "Một âm thoa được chế tạo để phát ra nốt La chuẩn có tần số 440 Hz. Trong thời gian một buổi biểu diễn hòa nhạc kéo dài 15 giây độc tấu, nhánh âm thoa đã thực hiện được tổng cộng bao nhiêu dao động?", ["6600 dao động", "440 dao động", "1500 dao động", "8800 dao động"], 0, "N = f × t = 440 × 15 = 6600 dao động."),
        make_vdc(2, "Người ta dùng một chiếc máy đo tần số ghi nhận âm thanh phát ra từ tiếng đập cánh của ba loài côn trùng: Muỗi đực (600 Hz); Ong bắp cày (250 Hz); Ruồi nhà (350 Hz). Âm thanh phát ra từ tiếng vỗ cánh của loài nào nghe bổng nhất và loài nào trầm nhất?", ["Muỗi đực bổng nhất, ong bắp cày trầm nhất", "Ruồi nhà bổng nhất, muỗi đực trầm nhất", "Ong bắp cày bổng nhất, muỗi đực trầm nhất", "Ba loài phát âm như nhau"], 0, "Tần số cao nhất (600 Hz - muỗi) nghe bổng nhất; tần số thấp nhất (250 Hz - ong) nghe trầm nhất."),
        make_vdc(3, "Một ca sĩ opera khi hát một nốt cao có thể làm rung và vỡ một chiếc ly thủy tinh mỏng đặt ở gần. Hiện tượng này xảy ra là do:", ["Tần số âm thanh của giọng hát trùng với tần số dao động riêng của chiếc ly gây ra hiện tượng cộng hưởng cơ học làm biên độ dao động của ly tăng cực đại", "Giọng ca sĩ quá nóng làm chảy ly", "Sóng âm làm nứt sàn nhà", "Gió từ miệng ca sĩ thổi vỡ ly"], 0, "Cộng hưởng âm học làm biên độ dao động của ly thủy tinh tăng vọt vượt giới hạn đàn hồi gây vỡ ly."),
        make_vdc(4, "Khi gõ nhẹ vào miệng một chiếc chai thủy tinh rỗng, âm thanh phát ra có độ cao nhất định. Nếu đổ thêm nước vào nửa chai rồi gõ nhẹ vào miệng chai thì âm phát ra sẽ thay đổi như thế nào?", ["Âm phát ra trầm hơn vì khối lượng nước và chai tăng lên làm tần số dao động của thành chai giảm đi", "Âm phát ra bổng hơn", "Âm không đổi", "Không nghe thấy âm nữa"], 0, "Khi gõ vào thành chai, thêm nước làm tăng quán tính của hệ dao động khiến thành chai dao động chậm lại, âm trầm hơn.")
    ]
}

# --- ĐỀ 3 ---
b12_b13_exams["phys7_c4_b13_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 13: Độ to và độ cao của âm - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c4", "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b13", "lessonName": "Bài 13: Độ to và độ cao của âm",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Đại lượng nào sau đây đo bằng đơn vị Hertz (Hz)?", ["Tần số dao động", "Biên độ dao động", "Độ to của âm", "Tốc độ âm"], 0, "Tần số dao động đo bằng Hertz (Hz)."),
        make_mc(2, "Nhận biết", "Dao động càng nhanh thì tần số dao động:", ["Càng lớn", "Càng nhỏ", "Bằng 0", "Không đổi"], 0, "Dao động nhanh nghĩa là thực hiện nhiều dao động trong 1 giây => tần số lớn."),
        make_mc(3, "Nhận biết", "Biên độ dao động của nguồn âm là:", ["Độ lệch lớn nhất của vật khỏi vị trí cân bằng", "Khoảng cách vật đi trong 1 giây", "Số dao động trong 1 giây", "Độ dài của vật"], 0, "Biên độ là khoảng cách lệch cực đại so với vị trí cân bằng."),
        make_mc(4, "Nhận biết", "Khi dùng dùi gõ nhẹ vào mặt trống, màng trống dao động với biên độ nhỏ thì âm phát ra:", ["Nghe nhỏ", "Nghe to", "Nghe bổng", "Nghe trầm"], 0, "Biên độ nhỏ thì âm nghe nhỏ."),
        make_mc(5, "Nhận biết", "Ngưỡng đau nhức màng nhĩ tai của con người bắt đầu từ độ to khoảng:", ["130 dB", "60 dB", "80 dB", "20 dB"], 0, "Ngưỡng đau tai là 130 dB."),
        make_mc(6, "Nhận biết", "Dải tần số sóng siêu âm là dải tần số:", ["Lớn hơn 20.000 Hz", "Nhỏ hơn 16 Hz", "Từ 16 Hz đến 20.000 Hz", "Từ 0 đến 100 Hz"], 0, "Siêu âm có tần số trên 20.000 Hz."),
        make_mc(7, "Thông hiểu", "Một quả lắc đồng hồ trong 1 phút thực hiện được 60 dao động. Tần số dao động của quả lắc là:", ["1 Hz", "60 Hz", "3600 Hz", "0,5 Hz"], 0, "1 phút = 60 s => f = 60 / 60 = 1 Hz."),
        make_mc(8, "Thông hiểu", "Tại sao tai người không thể nghe được âm do quả lắc đồng hồ ở câu trên phát ra?", ["Vì tần số 1 Hz thuộc vùng hạ âm dưới 16 Hz", "Vì quả lắc không dao động", "Vì quả lắc bị cách âm", "Vì quả lắc phát ra siêu âm"], 0, "1 Hz < 16 Hz nên tai người không nghe được."),
        make_mc(9, "Thông hiểu", "Một người gảy dây đàn số 1 (dây mảnh) và dây số 6 (dây dày) của cùng một cây đàn guitar. Dây nào phát ra âm bổng hơn?", ["Dây số 1 (dây mảnh) phát ra âm bổng hơn", "Dây số 6 phát ra âm bổng hơn", "Hai dây phát ra âm bổng như nhau", "Không xác định được"], 0, "Dây mảnh dao động nhanh hơn (tần số lớn hơn) nên phát ra âm bổng hơn."),
        make_mc(10, "Thông hiểu", "Một chiếc còi siêu âm dành cho việc huấn luyện chó cảnh: người thổi không nghe thấy tiếng còi nhưng chú chó lập tức chạy lại. Giải thích nào đúng?", ["Còi phát ra sóng siêu âm có tần số trên 20.000 Hz, tai chó nghe được còn tai người không nghe được", "Chó nhìn thấy hơi thở người thổi", "Còi không phát ra âm gì", "Chó ngửi thấy mùi còi"], 0, "Chó có thính giác cảm nhận được siêu âm tới 40.000 - 50.000 Hz."),
        make_mc(11, "Thông hiểu", "Để tăng độ to của tiếng kèn trumpet, người thổi kèn cần:", ["Thổi một luồng hơi mạnh hơn vào kèn làm cột không khí dao động với biên độ lớn hơn", "Bấm phím kèn nhanh hơn", "Cắt ngắn ống kèn", "Bịt miệng kèn"], 0, "Thổi hơi mạnh làm tăng biên độ dao động, âm phát ra to hơn."),
        make_mc(12, "Thông hiểu", "Âm thanh của tiếng thì thầm trong thư viện có độ to khoảng 30 dB, trong khi tiếng nói chuyện bình thường khoảng 60 dB. Âm thanh nói chuyện bình thường có năng lượng:", ["Lớn hơn nhiều so với tiếng thì thầm", "Nhỏ hơn tiếng thì thầm", "Bằng tiếng thì thầm", "Bằng 0"], 0, "Mức dB càng lớn thì biên độ và năng lượng âm càng lớn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc tính âm thanh và cảm nhận của tai người:", [
            ("a", "Tần số dao động quyết định độ cao của âm.", True),
            ("b", "Biên độ dao động quyết định độ to của âm.", True),
            ("c", "Tần số âm càng lớn thì âm nghe càng to.", False),
            ("d", "Hai âm có cùng độ cao vẫn có thể phân biệt được nếu do hai nhạc cụ khác nhau phát ra.", True)
        ], "Tần số lớn làm âm bổng, không phải làm âm to. Âm sắc giúp phân biệt các nhạc cụ."),
        make_tf(2, "Thông hiểu", "Về hạ âm và các hiện tượng tự nhiên:", [
            ("a", "Các cơn địa chấn động đất và sóng thần thường phát ra các đợt sóng hạ âm rất mạnh.", True),
            ("b", "Một số loài động vật như chim, voi cảm nhận được hạ âm nên có phản xạ tháo chạy trước khi động đất xảy ra.", True),
            ("c", "Sóng hạ âm hoàn toàn không thể truyền qua lớp đất đá của Trái Đất.", False),
            ("d", "Con người sử dụng các máy đo địa chấn thu sóng hạ âm để cảnh báo sớm động đất.", True)
        ], "Hạ âm truyền cực kì tốt qua đất đá và nước biển trên cự li hàng nghìn kilômét."),
        make_tf(3, "Vận dụng", "Học sinh sử dụng phần mềm đo tần số trên điện thoại thông minh để phân tích âm thanh giọng nói:", [
            ("a", "Giọng của bạn nam ghi nhận tần số cơ bản khoảng 120 Hz.", True),
            ("b", "Giọng của bạn nữ ghi nhận tần số cơ bản khoảng 240 Hz.", True),
            ("c", "Giọng của bạn nữ có tần số cao hơn nên nghe bổng hơn giọng bạn nam.", True),
            ("d", "Giọng bạn nào nghe to hơn chứng tỏ bạn đó có tần số giọng nói lớn hơn.", False)
        ], "Nghe to hơn là do biên độ dao động lớn hơn, không phải do tần số lớn hơn."),
        make_tf(4, "Vận dụng", "Khi điều chỉnh dây đàn vĩ cầm (violin):", [
            ("a", "Vặn khóa căng dây đàn làm tăng độ cao của nốt nhạc.", True),
            ("b", "Dùng ngón tay bấm trên phím đàn làm giảm chiều dài đoạn dây tự do rung động, âm phát ra bổng hơn.", True),
            ("c", "Kéo vĩ đàn mạnh hơn làm âm phát ra to hơn.", True),
            ("d", "Kéo vĩ đàn thật mạnh sẽ làm biến đổi nốt Đồ thành nốt Rê.", False)
        ], "Kéo mạnh chỉ làm tăng độ to của nốt nhạc, không làm đổi cao độ của nốt nhạc.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Số dao động thực hiện trong 1 giây được gọi là gì?", "Tần số", "Tần số dao động."),
        make_sa(2, "Thông hiểu", "Âm có tần số 30.000 Hz là hạ âm hay siêu âm?", "Siêu âm", "f > 20.000 Hz là siêu âm."),
        make_sa(3, "Vận dụng", "Một lá thép thực hiện 300 dao động trong 6 giây. Tần số dao động là bao nhiêu Hz?", "50", "f = 300 / 6 = 50 Hz."),
        make_sa(4, "Vận dụng", "Cánh của chim ruồi đập 1400 lần trong 20 giây. Tần số đập cánh của chim ruồi là bao nhiêu Hz?", "70", "f = 1400 / 20 = 70 Hz."),
        make_sa(5, "Vận dụng cao", "Một vật dao động với tần số 250 Hz. Trong thời gian 4 giây, vật thực hiện được bao nhiêu dao động?", "1000", "N = 250 × 4 = 1000 dao động."),
        make_sa(6, "Vận dụng cao", "Độ to của tiếng động cơ xe máy đang chạy trên đường phố vào khoảng bao nhiêu decibel (dB)?", "80", "Khoảng 75 - 80 dB.")
    ],
    "part4": [
        make_vdc(1, "Một âm thoa dao động với tần số 256 Hz (nốt Đồ chuẩn). Người ta gõ vào âm thoa rồi đưa lại gần miệng một ống nghiệm chứa nước. Khi điều chỉnh mực nước trong ống nghiệm đến độ cao thích hợp, người ta nghe thấy âm thanh phát ra to bất thường. Hiện tượng này được giải thích là do:", ["Hiện tượng cộng hưởng âm thanh khi tần số dao động của cột không khí trong ống nghiệm bằng đúng 256 Hz", "Nước phản chiếu ánh sáng", "Nước sôi bốc hơi", "Ống nghiệm bị vỡ"], 0, "Cộng hưởng âm học làm tăng biên độ dao động của cột không khí trong ống nghiệm, âm phát ra cực to."),
        make_vdc(2, "Để đo tốc độ di chuyển của dòng máu trong động mạch, các bác sĩ sử dụng thiết bị 'Siêu âm Doppler'. Thiết bị này hoạt động dựa trên nguyên lí:", ["Sóng siêu âm phản xạ từ các tế bào hồng cầu đang chuyển động có tần số bị thay đổi so với tần số phát ban đầu", "Sóng hạ âm làm đông máu", "Tia X làm nóng mạch máu", "Ánh sáng đổi màu máu"], 0, "Hiệu ứng Doppler: tần số sóng siêu âm phản xạ thay đổi tỉ lệ với tốc độ chuyển động của dòng hồng cầu."),
        make_vdc(3, "Một sợi dây đàn guitar có chiều dài 64 cm khi dao động phát ra âm có tần số 330 Hz (nốt Mi). Để phát ra âm có tần số 660 Hz (cao hơn một quãng tám), người chơi đàn cần bấm phím đàn để chiều dài đoạn dây tự do dao động còn lại bao nhiêu cm?", ["32 cm", "16 cm", "48 cm", "20 cm"], 0, "Tần số tỉ lệ nghịch với chiều dài dây đàn: tần số tăng gấp đôi thì chiều dài dây phải giảm một nửa: 64 / 2 = 32 cm."),
        make_vdc(4, "Một người gõ búa vào một thanh thép mỏng gắn trên bàn cân điện tử có gắn cảm biến rung. Thiết bị ghi nhận được đồ thị dao động hình sin có biên độ 2 mm và tần số 100 Hz. Nếu người đó gõ mạnh gấp đôi nhưng giữ nguyên vị trí kẹp thanh thép thì thông số nào của đồ thị dao động sẽ tăng lên?", ["Biên độ dao động tăng lên (lớn hơn 2 mm) trong khi tần số vẫn giữ nguyên 100 Hz", "Tần số tăng lên 200 Hz", "Cả biên độ và tần số đều tăng gấp đôi", "Đồ thị biến thành đường thẳng"], 0, "Gõ mạnh làm tăng biên độ dao động; tần số dao động riêng của thanh thép không đổi.")
    ]
}
