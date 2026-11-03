# -*- coding: utf-8 -*-
"""
CHƯƠNG III: TỐC ĐỘ - ÔN TẬP CUỐI CHƯƠNG III (5 ĐỀ ĐỘC LẬP 100%)
- phys7_c3_rev: [Đề tổng hợp] Ôn tập cuối Chương III (5 đề: test1..test5)
Không trùng lặp, không tiền tố "Đề X - " hoặc "Đề tổng hợp X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

c3_rev_exams = {}

# =========================================================================
# ĐỀ TỔNG HỢP ÔN TẬP CUỐI CHƯƠNG III (5 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
c3_rev_exams["phys7_c3_rev_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Đại lượng nào sau đây cho biết mức độ chuyển động nhanh hay chậm của một vật?", ["Tốc độ chuyển động", "Khối lượng của vật", "Thể tích của vật", "Nhiệt độ của vật"], 0, "Tốc độ cho biết mức độ nhanh hay chậm của chuyển động."),
        make_mc(2, "Nhận biết", "Trong hệ đo lường chuẩn quốc tế SI, đơn vị của tốc độ là:", ["Mét trên giây (m/s)", "Kilômét trên giờ (km/h)", "Dặm trên giờ (mph)", "Hải lí trên giờ (knot)"], 0, "Đơn vị chuẩn SI là m/s."),
        make_mc(3, "Nhận biết", "Hệ thống thiết bị đo thời gian hiện đại trong phòng thực hành gồm:", ["Cổng quang điện và đồng hồ đo thời gian hiện số", "Thước dây và cân đòn", "Bình tràn và lực kế", "Nhiệt kế thủy ngân"], 0, "Cổng quang điện kết hợp đồng hồ hiện số."),
        make_mc(4, "Nhận biết", "Trên đồ thị quãng đường - thời gian (s - t), đoạn đồ thị nằm ngang song song trục Ot thể hiện:", ["Vật đang đứng yên", "Vật chuyển động thẳng đều", "Vật tăng tốc đột ngột", "Vật quay lại điểm xuất phát"], 0, "Đoạn nằm ngang biểu thị quãng đường không đổi, vật đứng yên."),
        make_mc(5, "Nhận biết", "Biển báo hiệu giao thông hình tròn, viền đỏ, nền trắng bên trong có số 50 màu đen là biển:", ["Hạn chế tốc độ tối đa 50 km/h", "Tốc độ tối thiểu 50 km/h", "Khoảng cách xe 50 m", "Cấm xe trọng tải 50 tấn"], 0, "Biển hạn chế tốc độ tối đa cho phép."),
        make_mc(6, "Nhận biết", "Quy tắc 'Khoảng cách 3 giây' áp dụng trên đường nhằm mục đích:", ["Đảm bảo khoảng cách an toàn giúp lái xe kịp phản xạ và phanh dừng khi xe trước gặp sự cố", "Tăng tốc vượt xe khác", "Tiết kiệm xăng", "Chạy xe đúng làn đường"], 0, "Quy tắc 3 giây tạo cự li an toàn để phản ứng và phanh xe."),
        make_mc(7, "Thông hiểu", "Một bạn học sinh đi xe đạp từ nhà đến trường dài 3,6 km mất thời gian 15 phút. Tốc độ của bạn là:", ["14,4 km/h", "10,0 km/h", "12,0 km/h", "15,0 km/h"], 0, "15 phút = 0,25 h. v = 3,6 / 0,25 = 14,4 km/h."),
        make_mc(8, "Thông hiểu", "Đổi giá trị tốc độ 25 m/s sang đơn vị km/h ta được:", ["90 km/h", "60 km/h", "72 km/h", "100 km/h"], 0, "25 × 3,6 = 90 km/h."),
        make_mc(9, "Thông hiểu", "Một tấm chắn sáng có bề rộng 0,02 m đi qua cổng quang điện trong thời gian 0,04 s. Tốc độ tức thời của xe là:", ["0,5 m/s", "0,2 m/s", "1,0 m/s", "0,8 m/s"], 0, "v = 0,02 / 0,04 = 0,5 m/s."),
        make_mc(10, "Thông hiểu", "Đồ thị s - t của một ô tô là đường thẳng đi qua gốc tọa độ O và điểm A(2 h; 110 km). Tốc độ của ô tô là:", ["55 km/h", "60 km/h", "50 km/h", "110 km/h"], 0, "v = 110 / 2 = 55 km/h."),
        make_mc(11, "Thông hiểu", "Khi một chiếc ô tô tăng tốc độ từ 40 km/h lên 80 km/h (gấp đôi) thì động năng và mức độ va chạm sẽ tăng lên:", ["4 lần", "2 lần", "8 lần", "16 lần"], 0, "Động năng Wđ tỉ lệ với v^2: tăng 2 lần tốc độ làm động năng tăng 2^2 = 4 lần."),
        make_mc(12, "Thông hiểu", "Theo quy định, trên đoạn đường cao tốc khô ráo khi xe lưu thông với tốc độ từ 60 km/h đến 80 km/h thì khoảng cách an toàn tối thiểu là:", ["55 m", "35 m", "70 m", "100 m"], 0, "Khoảng cách an toàn tối thiểu tương ứng là 55 m.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các khái niệm cơ bản của tốc độ chuyển động trong Chương III:", [
            ("a", "Tốc độ trung bình bằng tổng quãng đường chia cho tổng thời gian đi hết quãng đường đó.", True),
            ("b", "1 m/s tương đương với 3,6 km/h.", True),
            ("c", "Tốc kế trên xe chỉ tốc độ trung bình của xe từ đầu bến đến cuối bến.", False),
            ("d", "Chuyển động đều có tốc độ tức thời tại mọi thời điểm bằng nhau.", True)
        ], "Tốc kế chỉ tốc độ tức thời tại thời điểm đang chạy."),
        make_tf(2, "Thông hiểu", "Về phép đo tốc độ trong thực hành và kiểm tra giao thông:", [
            ("a", "Phép đo tốc độ bằng thước và đồng hồ bấm giây luôn có sai số do phản xạ tay người.", True),
            ("b", "Cổng quang điện giúp đo thời gian với độ chính xác cao đến phần nghìn giây.", True),
            ("c", "Súng bắn tốc độ sử dụng sóng radar hoặc sóng laser để đo tốc độ phương tiện giao thông.", True),
            ("d", "Để kết quả đo chính xác nhất thì chỉ cần thực hiện đo đúng 1 lần duy nhất.", False)
        ], "Cần đo lặp lại nhiều lần để lấy giá trị trung bình giảm sai số ngẫu nhiên."),
        make_tf(3, "Vận dụng", "Phân tích đồ thị chuyển động s - t của một người đi bộ từ nhà qua chợ rồi đến công viên:", [
            ("a", "Chặng 1 từ nhà đến chợ dài 1,5 km người đó đi trong 20 phút (1/3 giờ) với tốc độ 4,5 km/h.", True),
            ("b", "Tại chợ người đó dừng mua sắm trong 10 phút, đồ thị là đoạn nằm ngang.", True),
            ("c", "Chặng 2 từ chợ đến công viên dài 2,0 km đi trong 30 phút với tốc độ 4,0 km/h.", True),
            ("d", "Tốc độ trung bình trên toàn tuyến tính cả thời gian mua sắm tại chợ là 4,25 km/h.", False)
        ], "Tổng s = 1,5 + 2 = 3,5 km. Tổng t = 20 + 10 + 30 = 60 phút = 1 h => v_tb = 3,5 / 1 = 3,5 km/h."),
        make_tf(4, "Vận dụng", "Xét trường hợp một xe tải chở hàng lưu thông trên đường:", [
            ("a", "Tài xế lái xe chạy với tốc độ 60 km/h (xấp xỉ 16,7 m/s).", True),
            ("b", "Thời gian phản xạ của tài xế là 0,9 giây, quãng đường xe đi trước khi phanh là 15 m.", True),
            ("c", "Quãng đường hãm phanh của xe tải dài hơn so với xe con chạy cùng tốc độ do tải trọng lớn hơn.", True),
            ("d", "Khi trời mưa đường trơn trượt, tài xế có thể rút ngắn khoảng cách với xe trước để dễ bám theo.", False)
        ], "Trời mưa đường trơn bắt buộc phải tăng khoảng cách an toàn."),
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đổi tốc độ 18 km/h sang m/s ta được kết quả là bao nhiêu?", "5", "18 / 3,6 = 5 m/s."),
        make_sa(2, "Thông hiểu", "Một người bơi 100 m hết 50 giây. Tốc độ bơi trung bình là bao nhiêu m/s?", "2", "v = 100 / 50 = 2 m/s."),
        make_sa(3, "Vận dụng", "Một xe khách chạy trên cao tốc với tốc độ 80 km/h trong thời gian 2,25 giờ. Quãng đường đi được là bao nhiêu km?", "180", "s = 80 × 2,25 = 180 km."),
        make_sa(4, "Vận dụng", "Khoảng cách an toàn tối thiểu theo luật khi xe chạy với tốc độ từ trên 80 km/h đến 100 km/h trên đường khô ráo là bao nhiêu mét?", "70", "70 m."),
        make_sa(5, "Vận dụng cao", "Xe máy chạy nửa quãng đường đầu với tốc độ 30 km/h và nửa quãng đường sau với tốc độ 60 km/h. Tốc độ trung bình trên cả quãng đường là bao nhiêu km/h?", "40", "v_tb = 2 × 30 × 60 / (30 + 60) = 3600 / 90 = 40 km/h."),
        make_sa(6, "Vận dụng cao", "Một máy bay siêu thanh bay với tốc độ Mach 2 (gấp đôi tốc độ âm thanh trong không khí 340 m/s). Tốc độ của máy bay tính theo đơn vị m/s là bao nhiêu?", "680", "340 × 2 = 680 m/s.")
    ],
    "part4": [
        make_vdc(1, "Hai ô tô cùng xuất phát từ bến A lúc 6h30 sáng đi về bến B cách A một khoảng 150 km. Xe thứ nhất chạy đều với tốc độ 50 km/h. Xe thứ hai chạy đều với tốc độ 60 km/h. Xe thứ hai đến bến B trước xe thứ nhất một khoảng thời gian là bao nhiêu phút?", ["30 phút", "20 phút", "15 phút", "45 phút"], 0, "t1 = 150 / 50 = 3,0 h = 180 phút. t2 = 150 / 60 = 2,5 h = 150 phút. Trước: 180 - 150 = 30 phút."),
        make_vdc(2, "Một đoàn tàu hỏa dài 180 m chạy qua một chiếc hầm đường sắt dài 540 m với tốc độ không đổi 54 km/h (15 m/s). Khoảng thời gian từ lúc đầu tàu bắt đầu chui vào hầm đến khi toa cuối cùng ra khỏi hầm hoàn toàn là:", ["48 giây", "36 giây", "40 giây", "50 giây"], 0, "s = 540 + 180 = 720 m. t = 720 / 15 = 48 s."),
        make_vdc(3, "Một ô tô chạy trên cao tốc với tốc độ 100 km/h (xấp xỉ 27,8 m/s). Bất ngờ phía trước có xe dừng sự cố. Thời gian phản xạ của tài xế là 0,8 s và quãng đường hãm phanh đến khi dừng hẳn là 45 m. Để dừng lại cách xe sự cố ít nhất 10 m thì khoảng cách tối thiểu từ lúc nhìn thấy xe sự cố phải là:", ["77,24 m", "67,24 m", "55,00 m", "80,00 m"], 0, "s_dừng = (27,8 × 0,8) + 45 = 22,24 + 45 = 67,24 m. Cách 10 m => Khoảng cách = 67,24 + 10 = 77,24 m."),
        make_vdc(4, "Một ca nô chạy xuôi dòng trên khúc sông từ A đến B hết 2 giờ và chạy ngược dòng từ B về A hết 3 giờ. Khúc sông AB dài 60 km. Vận tốc của dòng nước so với bờ sông là bao nhiêu km/h?", ["5 km/h", "10 km/h", "2,5 km/h", "25 km/h"], 0, "v_xuôi = 60 / 2 = 30 km/h; v_ngược = 60 / 3 = 20 km/h => v_nước = (30 - 20) / 2 = 5 km/h.")
    ]
}

# --- ĐỀ 2 ---
c3_rev_exams["phys7_c3_rev_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Muốn biết vật nào chuyển động nhanh hơn khi chúng chuyển động trong cùng một khoảng thời gian, ta so sánh:", ["Quãng đường đi được của các vật", "Khối lượng của các vật", "Hướng chuyển động của các vật", "Màu sắc của các vật"], 0, "Trong cùng thời gian, vật nào đi quãng đường dài hơn thì chuyển động nhanh hơn."),
        make_mc(2, "Nhận biết", "Công thức nào sau đây xác định quãng đường s khi biết tốc độ v và thời gian t?", ["s = v × t", "s = v / t", "s = t / v", "s = v + t"], 0, "s = v × t."),
        make_mc(3, "Nhận biết", "Khi dùng cổng quang điện để đo thời gian, bộ phận nào của xe đóng vai trò ngắt chùm tia sáng?", ["Tấm chắn sáng gắn trên xe", "Bánh xe", "Động cơ xe", "Dây kéo xe"], 0, "Tấm chắn sáng che chùm tia quang điện khi đi qua cổng quang."),
        make_mc(4, "Nhận biết", "Trong đồ thị s - t, nếu đường đồ thị dốc thẳng đứng (vuông góc với trục Ot) thì điều đó:", ["Không thể xảy ra trong thực tế vì vật không thể đi được quãng đường mà không tốn thời gian", "Vật chạy với tốc độ âm", "Vật đứng yên", "Vật đang rơi"], 0, "Thời gian luôn trôi về phía trước, không thể đi quãng đường trong thời gian t = 0 (tốc độ vô hạn)."),
        make_mc(5, "Nhận biết", "Biển báo hiệu R.306 hình tròn nền xanh có số 60 màu trắng là biển:", ["Tốc độ tối thiểu cho phép 60 km/h", "Tốc độ tối đa 60 km/h", "Khoảng cách 60 m", "Biển báo nguy hiểm"], 0, "Biển R.306 quy định tốc độ tối thiểu cho phép."),
        make_mc(6, "Nhận biết", "Thiết bị an toàn nào trên ô tô được thiết kế để bung ra như một chiếc đệm khí bảo vệ đầu và ngực khi va chạm mạnh?", ["Túi khí (Airbag)", "Dây an toàn", "Phanh tay", "Còi xe"], 0, "Túi khí tự động bung ra trong mili-giây để bảo vệ hành khách."),
        make_mc(7, "Thông hiểu", "Một ô tô chạy trên đoạn đường 105 km hết 1 giờ 45 phút (1,75 giờ). Tốc độ của ô tô là:", ["60 km/h", "55 km/h", "70 km/h", "65 km/h"], 0, "v = 105 / 1,75 = 60 km/h."),
        make_mc(8, "Thông hiểu", "Đổi 20 m/s sang đơn vị km/h ta được kết quả là:", ["72 km/h", "36 km/h", "54 km/h", "90 km/h"], 0, "20 × 3,6 = 72 km/h."),
        make_mc(9, "Thông hiểu", "Tấm chắn sáng rộng 4 cm (0,04 m) đi qua cổng quang điện trong thời gian 0,08 s. Tốc độ tức thời là:", ["0,5 m/s", "0,4 m/s", "2,0 m/s", "1,0 m/s"], 0, "v = 0,04 / 0,08 = 0,5 m/s."),
        make_mc(10, "Thông hiểu", "Đồ thị s - t của một người đạp xe: trong 30 phút đầu đi được 6 km, trong 30 phút sau đi được 9 km. Tốc độ trung bình trên cả 1 giờ là:", ["15 km/h", "12 km/h", "18 km/h", "10 km/h"], 0, "Tổng s = 6 + 9 = 15 km, tổng t = 1 h => v_tb = 15 / 1 = 15 km/h."),
        make_mc(11, "Thông hiểu", "Theo quy định, khoảng cách an toàn tối thiểu giữa hai xe chạy trên đường cao tốc khô ráo ở tốc độ từ trên 100 km/h đến 120 km/h là:", ["100 m", "70 m", "55 m", "35 m"], 0, "Khoảng cách an toàn quy định là 100 m."),
        make_mc(12, "Thông hiểu", "Khi lái xe gặp trời mưa to, mặt đường ngập nước, người điều khiển xe nên làm gì để đảm bảo an toàn?", ["Giảm tốc độ và tăng khoảng cách an toàn so với xe chạy phía trước", "Bật đèn pha chiếu xa và tăng tốc", "Đi bám sát đuôi xe trước", "Chạy vào làn khẩn cấp ở tốc độ tối đa"], 0, "Giảm tốc độ và nới rộng cự li an toàn do đường trơn trượt.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đơn vị và công thức đo tốc độ trong bài học:", [
            ("a", "Biểu thức tính thời gian là t = s / v.", True),
            ("b", "Đơn vị hải lí trên giờ (nút) thường dùng cho tàu thuyền trên biển.", True),
            ("c", "Để đổi km/h sang m/s ta lấy giá trị nhân với 3,6.", False),
            ("d", "Tốc độ trung bình phản ánh mức độ nhanh chậm của cả một quãng đường chuyển động.", True)
        ], "Đổi km/h sang m/s phải chia cho 3,6."),
        make_tf(2, "Thông hiểu", "Về các thiết bị đo tốc độ trong đời sống:", [
            ("a", "Tốc kế trên xe máy hoạt động nhờ cảm biến đo vòng quay của bánh xe.", True),
            ("b", "Thiết bị bắn tốc độ chỉ có thể đo được xe chạy ban ngày, không đo được ban đêm.", False),
            ("c", "Camera phạt nguội ghi lại hình ảnh biển số xe và tốc độ tại thời điểm vi phạm.", True),
            ("d", "Đồng hồ đo thời gian hiện số giúp đo được khoảng thời gian rất ngắn tới 0,001 giây.", True)
        ], "Thiết bị bắn tốc độ hồng ngoại đo chính xác cả ban đêm."),
        make_tf(3, "Vận dụng", "Hành trình của một gia đình đi du lịch bằng ô tô từ thành phố về quê:", [
            ("a", "Chặng 1 xe chạy trên cao tốc dài 80 km với tốc độ 80 km/h hết 1 giờ.", True),
            ("b", "Gia đình dừng nghỉ uống nước tại trạm dừng nghỉ trong 20 phút (1/3 giờ).", True),
            ("c", "Chặng 2 xe chạy trên quốc lộ dài 40 km với tốc độ 60 km/h hết 40 phút (2/3 giờ).", True),
            ("d", "Tốc độ trung bình trên toàn tuyến đường 120 km tính cả thời gian nghỉ là 60 km/h.", True)
        ], "Tổng s = 80 + 40 = 120 km, tổng t = 1 + 1/3 + 2/3 = 2 h => v_tb = 120 / 2 = 60 km/h."),
        make_tf(4, "Vận dụng", "Một xe con chạy trên cao tốc với tốc độ 108 km/h (30 m/s):", [
            ("a", "Thời gian phản xạ của tài xế là 0,7 giây, xe đi được 21 m trong lúc phản xạ.", True),
            ("b", "Quãng đường hãm phanh của xe đến khi dừng hẳn là 39 m.", True),
            ("c", "Tổng quãng đường dừng xe an toàn là 60 m.", True),
            ("d", "Khoảng cách an toàn theo quy tắc 3 giây ở tốc độ này là 60 m.", False)
        ], "Khoảng cách theo quy tắc 3 giây là 30 × 3 = 90 m, không phải 60 m.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đổi tốc độ 10 m/s sang đơn vị km/h ta được kết quả là bao nhiêu?", "36", "10 × 3,6 = 36 km/h."),
        make_sa(2, "Thông hiểu", "Một ô tô chạy quãng đường 150 km trong 3 giờ. Tốc độ của ô tô là bao nhiêu km/h?", "50", "v = 150 / 3 = 50 km/h."),
        make_sa(3, "Vận dụng", "Đoạn đường có biển báo tốc độ tối đa 60 km/h. Một xe máy chạy với tốc độ 18 m/s có bị vi phạm quá tốc độ không? (Trả lời: Có hoặc Không)", "Có", "18 m/s = 64,8 km/h > 60 km/h => Có vi phạm."),
        make_sa(4, "Vận dụng", "Theo quy định, khoảng cách an toàn tối thiểu khi chạy xe trên đường khô ráo với tốc độ từ 60 km/h trở xuống là bao nhiêu mét?", "35", "35 m."),
        make_sa(5, "Vận dụng cao", "Một người đi xe đạp đi nửa thời gian đầu với tốc độ 12 km/h và nửa thời gian sau với tốc độ 16 km/h. Tốc độ trung bình của người đó là bao nhiêu km/h?", "14", "Khi nửa thời gian: v_tb = (12 + 16)/2 = 14 km/h."),
        make_sa(6, "Vận dụng cao", "Khoảng cách từ Trái Đất đến Mặt Trăng là khoảng 384.000 km. Tín hiệu sóng vô tuyến truyền với tốc độ ánh sáng 300.000 km/s từ Trái Đất đến Mặt Trăng mất khoảng bao nhiêu giây? (Làm tròn 1 chữ số thập phân)", "1.3", "t = 384.000 / 300.000 = 1,28 s ≈ 1,3 s.")
    ],
    "part4": [
        make_vdc(1, "Hai thành phố A và B cách nhau 180 km. Lúc 7h00 sáng, xe ô tô thứ nhất xuất phát từ A đến B với tốc độ 60 km/h, xe ô tô thứ hai xuất phát từ B đến A với tốc độ 40 km/h. Hai xe gặp nhau lúc mấy giờ?", ["8h48 sáng", "9h00 sáng", "8h30 sáng", "9h15 sáng"], 0, "Thời gian gặp nhau: t = 180 / (60 + 40) = 1,8 h = 1h 48 phút. Thời điểm: 7h00 + 1h48 = 8h48 sáng."),
        make_vdc(2, "Một đoàn tàu hỏa dài 200 m đang chạy với tốc độ đều 72 km/h (20 m/s) chạy song song và vượt qua một người đi bộ ngược chiều với tốc độ 4 km/h (1,11 m/s). Khoảng thời gian từ lúc đầu tàu gặp người đi bộ đến lúc đuôi tàu đi qua người đó là:", ["9,47 giây", "10,00 giây", "12,50 giây", "8,50 giây"], 0, "v_tương_đối = 20 + (4/3,6) ≈ 21,11 m/s. t = 200 / 21,11 ≈ 9,47 s."),
        make_vdc(3, "Một ô tô chạy trên cao tốc với tốc độ 90 km/h (25 m/s). Tài xế nhìn thấy biển báo chướng ngại vật ở cách 65 m. Thời gian phản xạ là 0,8 s và quãng đường hãm phanh là 36 m. Ô tô có dừng kịp không và còn cách chướng ngại vật bao nhiêu mét?", ["Có dừng kịp, còn cách 9 m", "Không kịp, đâm vào chướng ngại vật", "Dừng cách 15 m", "Dừng chạm đúng chướng ngại vật"], 0, "s_dừng = (25 × 0,8) + 36 = 20 + 36 = 56 m < 65 m. Cách: 65 - 56 = 9 m."),
        make_vdc(4, "Một thuyền máy xuôi dòng sông từ A đến B mất 1 giờ và ngược dòng từ B về A mất 1,5 giờ. Biết vận tốc của dòng nước là 3 km/h. Chiều dài khúc sông AB là:", ["18 km", "24 km", "15 km", "12 km"], 0, "(v_thuyền + 3) × 1 = (v_thuyền - 3) × 1,5 => v_thuyền = 15 km/h => s = (15 + 3) × 1 = 18 km.")
    ]
}

# --- ĐỀ 3 ---
c3_rev_exams["phys7_c3_rev_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Tốc độ của một vật là quãng đường vật đi được trong:", ["Một đơn vị thời gian", "Cả quãng đường", "Một giờ duy nhất", "Một ngày đêm"], 0, "Định nghĩa tốc độ là quãng đường vật đi được trong một đơn vị thời gian."),
        make_mc(2, "Nhận biết", "Trong các chuyển động sau đây, chuyển động nào có thể coi là chuyển động thẳng đều?", ["Chuyển động của một điểm trên băng tải than đang vận hành ổn định", "Chuyển động của xe buýt khi vào bến", "Chuyển động của quả bưởi rụng từ trên cây", "Chuyển động của con lắc đồng hồ"], 0, "Băng tải hoạt động ổn định có tốc độ không đổi."),
        make_mc(3, "Nhận biết", "Thiết bị nào sau đây dùng để đo tốc độ tức thời của ô tô một cách chính xác khi đang chạy?", ["Tốc kế (đồng hồ đo tốc độ trên xe)", "Thước cuộn", "Đồng hồ bấm giây", "Bình chia độ"], 0, "Tốc kế trên xe hiển thị tức thì tốc độ xe đang chạy."),
        make_mc(4, "Nhận biết", "Đồ thị quãng đường - thời gian của một vật chuyển động có độ dốc càng nhỏ chứng tỏ:", ["Vật chuyển động càng chậm", "Vật chuyển động càng nhanh", "Vật đứng yên", "Vật quay lại mốc"], 0, "Độ dốc nhỏ ứng với tốc độ nhỏ, vật chuyển động chậm."),
        make_mc(5, "Nhận biết", "Biển báo hiệu R.420 (bắt đầu khu đông dân cư) yêu cầu người lái xe phải:", ["Giảm tốc độ và tuân thủ quy định tốc độ tối đa cho phép trong khu vực đông dân cư", "Tăng tốc chạy thật nhanh", "Bật còi liên tục", "Tắt hết đèn chiếu sáng"], 0, "Biển báo nhắc nhở giảm tốc độ khi vào khu đông dân cư."),
        make_mc(6, "Nhận biết", "Hệ thống chống bó cứng phanh ABS giúp phương tiện:", ["Tránh bị khóa cứng bánh xe gây mất lái và trượt lật khi phanh gấp", "Chạy nhanh hơn", "Tiết kiệm dầu máy", "Phanh dừng ngay tức thì trong 0 giây"], 0, "Hệ thống ABS duy trì khả năng điều khiển lái khi phanh gấp."),
        make_mc(7, "Thông hiểu", "Một vận động viên điền kinh chạy cự li 400 m hết 48 giây. Tốc độ trung bình của vận động viên xấp xỉ bằng:", ["8,33 m/s", "10,00 m/s", "7,50 m/s", "9,20 m/s"], 0, "v = 400 / 48 ≈ 8,33 m/s."),
        make_mc(8, "Thông hiểu", "Đổi tốc độ 90 km/h sang m/s ta được kết quả là:", ["25 m/s", "30 m/s", "20 m/s", "15 m/s"], 0, "90 / 3,6 = 25 m/s."),
        make_mc(9, "Thông hiểu", "Dùng cổng quang điện đo được tấm chắn sáng 2 cm (0,02 m) đi qua cổng trong 0,05 s. Tốc độ tức thời là:", ["0,4 m/s", "0,1 m/s", "2,5 m/s", "1,0 m/s"], 0, "v = 0,02 / 0,05 = 0,4 m/s."),
        make_mc(10, "Thông hiểu", "Đồ thị s - t biểu diễn một người đi xe máy: sau 1,5 giờ đi được 60 km. Tốc độ của người đó là:", ["40 km/h", "50 km/h", "30 km/h", "45 km/h"], 0, "v = 60 / 1,5 = 40 km/h."),
        make_mc(11, "Thông hiểu", "Lực ma sát giữa lốp xe và mặt đường có tác dụng gì quan trọng nhất khi hãm phanh?", ["Tạo lực hãm làm giảm tốc độ và giúp xe dừng lại", "Làm mòn lốp xe", "Tạo tiếng kêu rít", "Làm nóng động cơ"], 0, "Ma sát trượt/nghỉ giữa lốp và mặt đường giữ xe dừng lại an toàn."),
        make_mc(12, "Thông hiểu", "Một người lái xe ở tốc độ 80 km/h (xấp xỉ 22,2 m/s). Trong 1 giây phản xạ, xe đã đi được quãng đường xấp xỉ:", ["22,2 m", "80,0 m", "10,0 m", "15,5 m"], 0, "s = 22,2 × 1 = 22,2 m.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về mối liên hệ giữa các đại lượng trong chuyển động đều:", [
            ("a", "Quãng đường s tỉ lệ thuận với thời gian chuyển động t.", True),
            ("b", "Thời gian t tỉ lệ nghịch với tốc độ v trên cùng quãng đường.", True),
            ("c", "Tốc độ v tăng gấp đôi thì thời gian đi hết cùng quãng đường tăng gấp đôi.", False),
            ("d", "Đồ thị s - t của chuyển động đều là một đường thẳng đi qua gốc tọa độ O.", True)
        ], "Tốc độ tăng gấp đôi thì thời gian đi phải giảm một nửa."),
        make_tf(2, "Thông hiểu", "Về các phương pháp thực nghiệm xác định tốc độ:", [
            ("a", "Đo thời gian bằng cổng quang điện loại bỏ được sai số phản xạ con người.", True),
            ("b", "Thước đo có độ chia nhỏ nhất càng nhỏ thì kết quả đo càng chi tiết.", True),
            ("c", "Súng bắn tốc độ chỉ đo được khi xe đứng yên.", False),
            ("d", "Lấy giá trị trung bình cộng nhiều lần đo giúp giảm thiểu sai số ngẫu nhiên.", True)
        ], "Súng bắn tốc độ chuyên dùng để đo các vật đang chuyển động."),
        make_tf(3, "Vận dụng", "Chuyến đi phượt của hai bạn trẻ bằng xe máy qua đoạn đường đèo dài 45 km:", [
            ("a", "Chặng leo đèo dài 20 km chạy với tốc độ 25 km/h hết 48 phút (0,8 h).", True),
            ("b", "Dừng lại chụp ảnh ngắm cảnh trên đỉnh đèo mất 30 phút (0,5 h).", True),
            ("c", "Chặng đổ đèo dài 25 km chạy cẩn thận với tốc độ 30 km/h hết 50 phút (5/6 h).", True),
            ("d", "Tốc độ trung bình trên toàn bộ chuyến đi tính cả thời gian chụp ảnh là 21,1 km/h.", True)
        ], "Tổng t = 0,8 + 0,5 + 5/6 = 2,133 h. v_tb = 45 / 2,133 ≈ 21,1 km/h."),
        make_tf(4, "Vận dụng", "Tình huống tham gia giao thông trên đường cao tốc lúc trời sương mù:", [
            ("a", "Tầm nhìn bị hạn chế nên tài xế phải giảm tốc độ dưới tốc độ tối đa cho phép.", True),
            ("b", "Bật đèn sương mù và giữ khoảng cách lớn hơn khoảng cách quy định lúc trời khô ráo.", True),
            ("c", "Được phép vượt xe khác ở những khúc cua bị khuất tầm nhìn.", False),
            ("d", "Quy tắc 3 giây có thể kéo dài thành quy tắc 4 hoặc 5 giây trong điều kiện thời tiết xấu.", True)
        ], "Tuyệt đối không vượt xe tại khúc cua khuất tầm nhìn trong sương mù.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đổi tốc độ 15 m/s sang đơn vị km/h ta được kết quả là bao nhiêu?", "54", "15 × 3,6 = 54 km/h."),
        make_sa(2, "Thông hiểu", "Một máy bay chở khách bay được 1800 km trong 2,5 giờ. Tốc độ của máy bay là bao nhiêu km/h?", "720", "v = 1800 / 2,5 = 720 km/h."),
        make_sa(3, "Vận dụng", "Khoảng cách an toàn tối thiểu theo quy định khi xe chạy với tốc độ từ trên 60 km/h đến 80 km/h trên đường khô ráo là bao nhiêu mét?", "55", "55 m."),
        make_sa(4, "Vận dụng", "Một xe ô tô chạy tốc độ 20 m/s. Quãng đường phản xạ là 14 m, quãng đường hãm phanh là 26 m. Tổng quãng đường dừng xe là bao nhiêu mét?", "40", "14 + 26 = 40 m."),
        make_sa(5, "Vận dụng cao", "Xe ô tô đi 1/3 quãng đường đầu với tốc độ 40 km/h và 2/3 quãng đường sau với tốc độ 60 km/h. Tốc độ trung bình cả quãng đường là bao nhiêu km/h? (Làm tròn số nguyên)", "51", "t1 = (s/3)/40 = s/120; t2 = (2s/3)/60 = s/90. Tổng t = s/120 + s/90 = 7s/360 => v_tb = 360/7 ≈ 51,43 ≈ 51 km/h."),
        make_sa(6, "Vận dụng cao", "Một chiếc xe cứu thương chạy với tốc độ 108 km/h (30 m/s) trên đường thẳng. Trong 25 giây, xe đi được bao nhiêu mét?", "750", "s = 30 × 25 = 750 m.")
    ],
    "part4": [
        make_vdc(1, "Một ô tô khởi hành từ Hà Nội lúc 7h00 sáng để đi Hải Phòng trên quãng đường dài 100 km. Trong 40 km đầu xe chạy với tốc độ 40 km/h; trong 60 km còn lại chạy trên cao tốc với tốc độ 100 km/h. Xe đến Hải Phòng vào thời điểm nào?", ["8h36 sáng", "8h30 sáng", "9h00 sáng", "8h45 sáng"], 0, "t1 = 40 / 40 = 1 h. t2 = 60 / 100 = 0,6 h = 36 phút. Tổng t = 1h 36 phút. Đến nơi: 7h00 + 1h36 = 8h36 sáng."),
        make_vdc(2, "Một đoàn tàu dài 160 m đang chạy với tốc độ 36 km/h (10 m/s) vượt qua một cây cầu dài 440 m. Thời gian kể từ khi đầu tàu bước lên cầu đến khi toa cuối cùng qua khỏi cầu là:", ["60 giây", "44 giây", "50 giây", "16 giây"], 0, "s = 440 + 160 = 600 m. t = 600 / 10 = 60 s."),
        make_vdc(3, "Một ô tô chạy trên đường cao tốc với tốc độ 90 km/h (25 m/s). Phía trước có vật cản cách xe 70 m. Thời gian phản xạ của tài xế là 0,8 giây và quãng đường hãm phanh là 35 m. Ô tô có dừng kịp không và còn cách vật cản bao nhiêu mét?", ["Có dừng kịp, còn cách vật cản 15 m", "Không kịp, đâm vào vật cản", "Dừng cách 20 m", "Dừng cách 5 m"], 0, "Quãng đường dừng: (25 × 0,8) + 35 = 20 + 35 = 55 m < 70 m. Cách vật cản: 70 - 55 = 15 m."),
        make_vdc(4, "Một người chèo thuyền trên khúc sông dài 12 km. Khi xuôi dòng mất 1 giờ, khi ngược dòng mất 2 giờ. Tốc độ chảy của dòng nước là:", ["3 km/h", "6 km/h", "2 km/h", "1,5 km/h"], 0, "v_xuôi = 12 / 1 = 12 km/h; v_ngược = 12 / 2 = 6 km/h => v_nước = (12 - 6)/2 = 3 km/h.")
    ]
}

# --- ĐỀ 4 ---
c3_rev_exams["phys7_c3_rev_test4"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 04",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 4, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Để xác định thời gian chuyển động t từ công thức v = s / t, ta dùng biểu thức:", ["t = s / v", "t = v / s", "t = s × v", "t = s - v"], 0, "t = s / v."),
        make_mc(2, "Nhận biết", "Trong các đơn vị sau, đơn vị nào dùng để đo tốc độ?", ["km/h", "km.h", "m.s", "kg/m"], 0, "km/h là đơn vị đo tốc độ."),
        make_mc(3, "Nhận biết", "Dụng cụ nào dùng để đo độ dài quãng đường trong giờ thực hành đo tốc độ?", ["Thước cuộn", "Đồng hồ bấm giây", "Cổng quang điện", "Ampe kế"], 0, "Thước cuộn dùng để đo độ dài quãng đường."),
        make_mc(4, "Nhận biết", "Giao điểm của hai đường đồ thị quãng đường - thời gian của hai vật cho biết:", ["Thời điểm và vị trí hai vật gặp nhau", "Tốc độ cực đại", "Thời điểm xuất phát", "Khoảng cách xa nhất giữa hai vật"], 0, "Giao điểm xác định thời điểm và vị trí gặp nhau."),
        make_mc(5, "Nhận biết", "Biển báo P.127 có ghi số 80 bên trong báo hiệu:", ["Tốc độ tối đa cho phép là 80 km/h", "Tốc độ tối thiểu là 80 km/h", "Đoạn đường dài 80 km", "Cấm xe 80 tấn"], 0, "Biển hạn chế tốc độ tối đa cho phép."),
        make_mc(6, "Nhận biết", "Tác dụng quan trọng nhất của dây an toàn trên xe ô tô khi xe phanh gấp là:", ["Ngăn hành khách văng về phía trước theo quán tính va chạm vào kính chắn gió hoặc vô lăng", "Giúp hành khách ngồi êm hơn", "Làm xe dừng lại nhanh hơn", "Chống buồn ngủ"], 0, "Dây an toàn giữ người ngồi cố định theo quán tính."),
        make_mc(7, "Thông hiểu", "Một xe buýt đi quãng đường 30 km trong 45 phút (0,75 giờ). Tốc độ của xe buýt là:", ["40 km/h", "30 km/h", "45 km/h", "50 km/h"], 0, "v = 30 / 0,75 = 40 km/h."),
        make_mc(8, "Thông hiểu", "Đổi tốc độ 12 m/s sang đơn vị km/h ta được:", ["43,2 km/h", "36,0 km/h", "24,0 km/h", "48,0 km/h"], 0, "12 × 3,6 = 43,2 km/h."),
        make_mc(9, "Thông hiểu", "Tấm chắn sáng rộng 0,03 m đi qua cổng quang điện trong 0,06 s. Tốc độ của vật là:", ["0,5 m/s", "0,2 m/s", "1,8 m/s", "0,18 m/s"], 0, "v = 0,03 / 0,06 = 0,5 m/s."),
        make_mc(10, "Thông hiểu", "Đồ thị s - t của một ô tô là đường thẳng qua điểm (1,2 h; 72 km). Tốc độ của ô tô là:", ["60 km/h", "72 km/h", "50 km/h", "80 km/h"], 0, "v = 72 / 1,2 = 60 km/h."),
        make_mc(11, "Thông hiểu", "Khi tham gia giao thông trên đường, việc giữ khoảng cách an toàn giúp tài xế:", ["Đủ quãng đường để hãm phanh dừng xe an toàn khi xe phía trước dừng đột ngột", "Chạy xe với tốc độ cao hơn", "Vượt xe khác dễ hơn", "Tiết kiệm xăng"], 0, "Khoảng cách an toàn tạo không gian phanh dừng tránh va chạm dồn toa."),
        make_mc(12, "Thông hiểu", "Một người đi xe máy với tốc độ 36 km/h (10 m/s). Trong thời gian phản xạ 0,8 giây, xe đã đi được:", ["8 m", "10 m", "6 m", "12 m"], 0, "s = 10 × 0,8 = 8 m.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất của chuyển động trong tự nhiên:", [
            ("a", "Tốc độ ánh sáng trong chân không là giới hạn tốc độ lớn nhất trong vũ trụ (~ 300.000 km/s).", True),
            ("b", "Tốc độ âm thanh trong không khí lớn hơn tốc độ truyền ánh sáng.", False),
            ("c", "Tốc độ của kim giờ đồng hồ nhỏ hơn tốc độ của kim phút đồng hồ.", True),
            ("d", "Chuyển động không đều có tốc độ thay đổi theo thời gian.", True)
        ], "Tốc độ ánh sáng (300.000 km/s) lớn hơn rất nhiều tốc độ âm thanh (340 m/s)."),
        make_tf(2, "Thông hiểu", "Về quy trình đo đạc thực nghiệm trong môn KHTN 7:", [
            ("a", "Cần chọn thước đo có giới hạn đo lớn hơn độ dài cần đo.", True),
            ("b", "Khi bấm đồng hồ bấm giây, cần tập trung quan sát điểm xuất phát và đích đến.", True),
            ("c", "Cổng quang điện chỉ đo được các vật có bề mặt nhẵn bóng như gương.", False),
            ("d", "Viết kết quả đo cần ghi kèm theo đơn vị đo hợp pháp.", True)
        ], "Cổng quang điện nhận diện được mọi vật chắn cản quang, không cần mặt gương nhẵn."),
        make_tf(3, "Vận dụng", "Một xe ô tô tải vận chuyển vật tư qua 2 chặng đường:", [
            ("a", "Chặng 1 đường gồ ghề dài 20 km chạy với tốc độ 30 km/h hết 40 phút (2/3 h).", True),
            ("b", "Chặng 2 đường nhựa phẳng dài 60 km chạy với tốc độ 60 km/h hết 60 phút (1 h).", True),
            ("c", "Tổng thời gian di chuyển của xe là 1 giờ 40 phút (5/3 h).", True),
            ("d", "Tốc độ trung bình trên toàn bộ quãng đường 80 km là 45 km/h.", False)
        ], "Tổng s = 80 km, tổng t = 5/3 h => v_tb = 80 / (5/3) = 48 km/h."),
        make_tf(4, "Vận dụng", "Các quy tắc an toàn giao thông đường bộ đối với người đi xe máy:", [
            ("a", "Bắt buộc phải đội mũ bảo hiểm có cài quai đúng quy cách khi tham gia giao thông.", True),
            ("b", "Không được chở quá số người quy định (trừ trường hợp chở trẻ em dưới 14 tuổi, người đi cấp cứu).", True),
            ("c", "Được phép sử dụng ô (dù), điện thoại di động khi đang lái xe máy.", False),
            ("d", "Tuân thủ tốc độ tối đa cho phép trên từng đoạn đường.", True)
        ], "Tuyệt đối không sử dụng ô, điện thoại khi đang điều khiển xe máy.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đổi tốc độ 8 m/s sang đơn vị km/h ta được kết quả là bao nhiêu? (Làm tròn 1 chữ số thập phân)", "28.8", "8 × 3,6 = 28,8 km/h."),
        make_sa(2, "Thông hiểu", "Một chiếc cano đi quãng đường 60 km trong 1,5 giờ. Tốc độ của cano là bao nhiêu km/h?", "40", "v = 60 / 1,5 = 40 km/h."),
        make_sa(3, "Vận dụng", "Khoảng cách an toàn tối thiểu quy định khi xe chạy với tốc độ trên 100 km/h đến 120 km/h trên đường cao tốc khô ráo là bao nhiêu mét?", "100", "100 m."),
        make_sa(4, "Vận dụng", "Một xe ô tô chạy tốc độ 25 m/s. Quãng đường phản xạ là 20 m, quãng đường hãm phanh là 35 m. Tổng quãng đường dừng xe là bao nhiêu mét?", "55", "20 + 35 = 55 m."),
        make_sa(5, "Vận dụng cao", "Một người đi bộ nửa quãng đường đầu với tốc độ 4 km/h và nửa quãng đường sau với tốc độ 6 km/h. Tốc độ trung bình trên cả quãng đường là bao nhiêu km/h?", "4.8", "v_tb = 2 × 4 × 6 / (4 + 6) = 48 / 10 = 4,8 km/h."),
        make_sa(6, "Vận dụng cao", "Một chiếc tàu ngầm phát tín hiệu siêu âm xuống đáy biển và nhận lại tín hiệu phản xạ sau 1,6 giây. Biết tốc độ âm trong nước biển là 1500 m/s. Độ sâu của đáy biển tại vị trí đó là bao nhiêu mét?", "1200", "d = 1500 × 1,6 / 2 = 1200 m.")
    ],
    "part4": [
        make_vdc(1, "Một đoàn tàu hỏa chạy từ ga A đến ga B cách nhau 240 km. Trong nửa quãng đường đầu tàu chạy với tốc độ 60 km/h, trong nửa quãng đường sau tàu chạy với tốc độ 80 km/h. Thời gian tàu chạy từ A đến B (không kể thời gian đỗ ga) là:", ["3,5 giờ", "3,0 giờ", "4,0 giờ", "3,2 giờ"], 0, "t1 = 120 / 60 = 2,0 h. t2 = 120 / 80 = 1,5 h. Tổng t = 3,5 h."),
        make_vdc(2, "Một người đứng tại một điểm nhìn thấy tia chớp lóe lên từ đám mây, sau đó đúng 4,5 giây mới nghe thấy tiếng sấm nổ rền. Biết tốc độ âm trong không khí là 340 m/s và ánh sáng truyền đi gần như tức thì. Vị trí tia sét đánh cách người đó khoảng bao nhiêu mét?", ["1530 m", "1360 m", "1700 m", "1500 m"], 0, "s = 340 × 4,5 = 1530 m."),
        make_vdc(3, "Một ô tô chạy trên cao tốc với tốc độ 108 km/h (30 m/s). Phía trước có xe phanh gấp cách 85 m. Thời gian phản xạ của tài xế là 0,7 giây và quãng đường hãm phanh xe dừng hẳn là 45 m. Ô tô có dừng lại kịp không và còn cách xe trước bao nhiêu mét?", ["Có dừng kịp, còn cách 19 m", "Không kịp, đâm vào xe trước", "Dừng cách 10 m", "Dừng cách 25 m"], 0, "Quãng đường dừng: (30 × 0,7) + 45 = 21 + 45 = 66 m < 85 m. Cách xe trước: 85 - 66 = 19 m."),
        make_vdc(4, "Một ca nô chạy xuôi dòng một khúc sông dài 48 km hết 1,5 giờ, sau đó ngược dòng trở về hết 2,4 giờ. Tốc độ của ca nô khi nước đứng yên và tốc độ dòng nước lần lượt là:", ["26 km/h và 6 km/h", "25 km/h và 5 km/h", "30 km/h và 2 km/h", "20 km/h và 4 km/h"], 0, "v_xuôi = 48 / 1,5 = 32 km/h; v_ngược = 48 / 2,4 = 20 km/h => v_thuyền = (32 + 20)/2 = 26 km/h; v_nước = (32 - 20)/2 = 6 km/h.")
    ]
}

# --- ĐỀ 5 ---
c3_rev_exams["phys7_c3_rev_test5"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 05",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 5, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Đại lượng nào xác định bằng thương số giữa quãng đường đi được và thời gian đi hết quãng đường đó?", ["Tốc độ chuyển động", "Gia tốc", "Khối lượng riêng", "Áp suất"], 0, "Thương số s/t là tốc độ chuyển động."),
        make_mc(2, "Nhận biết", "Trong các đơn vị sau, đơn vị nào KHÔNG dùng để đo tốc độ?", ["m/s^2", "m/s", "km/h", "cm/s"], 0, "m/s^2 là đơn vị của gia tốc, không phải tốc độ."),
        make_mc(3, "Nhận biết", "Cổng quang điện dùng trong thí nghiệm thực hành đo tốc độ hoạt động nhờ:", ["Cảm biến thu phát tia hồng ngoại", "Cảm biến nhiệt", "Cảm biến âm thanh", "Cảm biến trọng lực"], 0, "Cổng quang điện ứng dụng cảm biến quang hồng ngoại."),
        make_mc(4, "Nhận biết", "Trên đồ thị s - t, nếu đoạn đồ thị là đường thẳng xiên góc dốc lên thì:", ["Vật chuyển động thẳng đều", "Vật đứng yên", "Vật quay lại mốc", "Vật rơi tự do"], 0, "Đường xiên dốc lên biểu diễn chuyển động thẳng đều."),
        make_mc(5, "Nhận biết", "Biển báo P.127 có số 100 viền đỏ cho biết:", ["Tốc độ tối đa không được vượt quá 100 km/h", "Tốc độ tối thiểu phải đạt 100 km/h", "Khoảng cách cách xe 100 m", "Cấm xe 100 tấn"], 0, "Biển hạn chế tốc độ tối đa cho phép 100 km/h."),
        make_mc(6, "Nhận biết", "Mũ bảo hiểm đạt chuẩn cho người đi mô tô, xe máy có tác dụng bảo vệ bộ phận nào quan trọng nhất?", ["Hộp sọ và não bộ", "Khuỷu tay", "Bàn chân", "Đầu gối"], 0, "Mũ bảo hiểm bảo vệ đầu và não bộ khỏi chấn thương sọ não nguy hiểm."),
        make_mc(7, "Thông hiểu", "Một vận động viên bơi cự li 50 m hết 20 giây. Tốc độ bơi trung bình là:", ["2,5 m/s", "2,0 m/s", "1,5 m/s", "3,0 m/s"], 0, "v = 50 / 20 = 2,5 m/s."),
        make_mc(8, "Thông hiểu", "Đổi tốc độ 108 km/h sang m/s ta được kết quả là:", ["30 m/s", "25 m/s", "35 m/s", "40 m/s"], 0, "108 / 3,6 = 30 m/s."),
        make_mc(9, "Thông hiểu", "Tấm chắn sáng rộng 1 cm (0,01 m) đi qua cổng quang điện trong thời gian 0,025 s. Tốc độ tức thời là:", ["0,4 m/s", "0,25 m/s", "4,0 m/s", "0,025 m/s"], 0, "v = 0,01 / 0,025 = 0,4 m/s."),
        make_mc(10, "Thông hiểu", "Đồ thị s - t của một ô tô là đường thẳng qua điểm (0,5 h; 35 km). Tốc độ của ô tô là:", ["70 km/h", "35 km/h", "50 km/h", "60 km/h"], 0, "v = 35 / 0,5 = 70 km/h."),
        make_mc(11, "Thông hiểu", "Theo quy định, khoảng cách an toàn tối thiểu giữa hai xe chạy trên đường khô ráo với tốc độ từ trên 80 km/h đến 100 km/h là:", ["70 m", "55 m", "35 m", "100 m"], 0, "Cự li an toàn tối thiểu là 70 m."),
        make_mc(12, "Thông hiểu", "Một người lái xe ở tốc độ 72 km/h (20 m/s). Trong thời gian phản xạ 0,7 giây, xe đã đi được quãng đường là:", ["14 m", "20 m", "10 m", "15 m"], 0, "s = 20 × 0,7 = 14 m.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất và công thức của tốc độ trong đời sống:", [
            ("a", "Tốc độ biểu thị quãng đường vật đi được trong một giây hoặc trong một giờ.", True),
            ("b", "Xe có tốc độ 60 km/h chạy nhanh hơn xe có tốc độ 15 m/s.", True),
            ("c", "Tốc độ trung bình luôn luôn bằng trung bình cộng vận tốc lớn nhất và nhỏ nhất.", False),
            ("d", "Tốc kế trên ô tô đo tốc độ tức thời của ô tô tại thời điểm đang chạy.", True)
        ], "15 m/s = 54 km/h < 60 km/h. Tốc độ trung bình không phải trung bình cộng hai vận tốc cực trị."),
        make_tf(2, "Thông hiểu", "Về các thiết bị kiểm soát tốc độ phương tiện trên cao tốc:", [
            ("a", "Hệ thống camera nhận dạng biển số tự động hoạt động liên tục 24/7.", True),
            ("b", "Cảnh sát giao thông sử dụng máy đo tốc độ có ghi hình ảnh làm căn cứ xử phạt.", True),
            ("c", "Các phương tiện lưu thông được phép che biển số để tránh camera phạt nguội.", False),
            ("d", "Việc giám sát tốc độ tự động giúp giảm đáng kể tai nạn thảm khốc do phóng nhanh vượt ẩu.", True)
        ], "Hành vi che biển số, làm mờ biển số là vi phạm pháp luật nghiêm trọng."),
        make_tf(3, "Vận dụng", "Hành trình di chuyển của một chiếc xe con trên lộ trình 150 km:", [
            ("a", "Đoạn 1 đi qua thành phố dài 30 km với tốc độ 40 km/h hết 45 phút (0,75 h).", True),
            ("b", "Dừng lại đổ xăng và kiểm tra lốp xe mất 15 phút (0,25 h).", True),
            ("c", "Đoạn 2 đi trên cao tốc dài 120 km với tốc độ 80 km/h hết 90 phút (1,5 h).", True),
            ("d", "Tốc độ trung bình trên toàn tuyến đường 150 km tính cả thời gian đổ xăng là 60 km/h.", True)
        ], "Tổng t = 0,75 + 0,25 + 1,5 = 2,5 h => v_tb = 150 / 2,5 = 60 km/h."),
        make_tf(4, "Vận dụng", "Xét trường hợp một xe ô tô chạy tốc độ 120 km/h (xấp xỉ 33,3 m/s) trên cao tốc:", [
            ("a", "Thời gian phản xạ của tài xế là 0,8 s, quãng đường xe đi trước khi phanh là 26,6 m.", True),
            ("b", "Quãng đường hãm phanh đến khi dừng hẳn là 53,4 m.", True),
            ("c", "Tổng quãng đường dừng xe an toàn là 80 m.", True),
            ("d", "Khoảng cách an toàn tối thiểu theo quy định (100 m) đủ lớn để đảm bảo dừng xe an toàn trong trường hợp này.", True)
        ], "Tổng quãng đường dừng là 80 m < 100 m nên khoảng cách quy định 100 m hoàn toàn an toàn.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đổi tốc độ 25 m/s sang đơn vị km/h ta được kết quả là bao nhiêu?", "90", "25 × 3,6 = 90 km/h."),
        make_sa(2, "Thông hiểu", "Một ô tô chạy quãng đường 210 km trong 3,5 giờ. Tốc độ của ô tô là bao nhiêu km/h?", "60", "v = 210 / 3,5 = 60 km/h."),
        make_sa(3, "Vận dụng", "Một bạn học sinh đi xe máy điện với tốc độ 25 km/h. Để đi hết quãng đường 15 km từ nhà đến trường ngoại thành, bạn cần bao nhiêu phút?", "36", "t = 15 / 25 = 0,6 h = 36 phút."),
        make_sa(4, "Vận dụng", "Một xe ô tô chạy tốc độ 20 m/s. Quãng đường phản xạ là 16 m, quãng đường hãm phanh là 34 m. Tổng quãng đường dừng xe là bao nhiêu mét?", "50", "16 + 34 = 50 m."),
        make_sa(5, "Vận dụng cao", "Một người đi xe đạp đi nửa quãng đường đầu với tốc độ 10 km/h và nửa quãng đường sau với tốc độ 15 km/h. Tốc độ trung bình cả quãng đường là bao nhiêu km/h?", "12", "v_tb = 2 × 10 × 15 / (10 + 15) = 300 / 25 = 12 km/h."),
        make_sa(6, "Vận dụng cao", "Một chiếc ca nô chạy với tốc độ 36 km/h (10 m/s). Trong thời gian 45 giây, ca nô đi được quãng đường bao nhiêu mét?", "450", "s = 10 × 45 = 450 m.")
    ],
    "part4": [
        make_vdc(1, "Một xe khách khởi hành từ Hà Nội lúc 6h00 sáng để đi Vinh trên quãng đường dài 300 km. Trong 180 km đầu xe chạy trên cao tốc với tốc độ 90 km/h; sau đó xe nghỉ ăn sáng 30 phút; đoạn còn lại 120 km chạy trên quốc lộ với tốc độ 60 km/h. Xe đến Vinh vào thời điểm nào?", ["10h30 sáng", "10h00 sáng", "11h00 trưa", "11h30 trưa"], 0, "t1 = 180 / 90 = 2 h. t_nghỉ = 0,5 h. t2 = 120 / 60 = 2 h. Tổng t = 4,5 h. Đến nơi: 6h00 + 4h30 = 10h30 sáng."),
        make_vdc(2, "Một đoàn tàu chở khách dài 150 m đang chạy với tốc độ 54 km/h (15 m/s) chạy qua một người đứng quan sát bên đường ray. Thời gian người đó nhìn thấy đoàn tàu chạy qua trước mặt mình là:", ["10 giây", "15 giây", "12 giây", "8 giây"], 0, "t = 150 / 15 = 10 s."),
        make_vdc(3, "Một ô tô chạy trên cao tốc với tốc độ 80 km/h (xấp xỉ 22,2 m/s). Phía trước có vật cản cách xe 60 m. Thời gian phản xạ của tài xế là 0,7 giây và quãng đường hãm phanh là 32 m. Ô tô có dừng lại kịp trước vật cản không và còn cách vật cản bao nhiêu mét?", ["Có dừng kịp, còn cách 12,46 m", "Không kịp, đâm vào vật cản", "Dừng cách 20 m", "Dừng chạm đúng vật cản"], 0, "s_dừng = (22,2 × 0,7) + 32 = 15,54 + 32 = 47,54 m < 60 m. Cách vật cản: 60 - 47,54 = 12,46 m."),
        make_vdc(4, "Một người chèo thuyền trên sông từ bến A đến bến B cách nhau 15 km mất 1 giờ 15 phút (1,25 h) khi xuôi dòng. Khi ngược dòng từ B về A mất 2,5 giờ. Vận tốc của dòng nước là:", ["3 km/h", "6 km/h", "2 km/h", "1,5 km/h"], 0, "v_xuôi = 15 / 1,25 = 12 km/h; v_ngược = 15 / 2,5 = 6 km/h => v_nước = (12 - 6)/2 = 3 km/h.")
    ]
}
