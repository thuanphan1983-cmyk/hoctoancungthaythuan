# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG VII: ĐIỆN TỪ
Bao gồm 5 đề thi độc lập 100%: phys9_c7_rev_test1 đến phys9_c7_rev_test5
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c7"
CH_TITLE = "Chương VII: Điện từ"
L_ID = "phys9_c7_rev"
L_NAME = "[Đề tổng hợp] Ôn tập cuối Chương VII"

# =============================================================================
# phys9_c7_rev_test1
# =============================================================================
p1_rev_t1 = [
    make_mc(1, "Nhận biết", "Quy tắc nắm tay phải dùng để xác định:", [
        "Chiều của đường sức từ trong lòng ống dây có dòng điện chạy qua",
        "Chiều của lực điện từ tác dụng lên đoạn dây",
        "Chiều dòng điện cảm ứng trong máy phát điện",
        "Chiều quay của động cơ điện"
    ], 0, "Quy tắc nắm tay phải xác định chiều đường sức từ trong ống dây."),
    make_mc(2, "Nhận biết", "Trong quy tắc bàn tay trái, ngón tay cái choãi ra 90 độ chỉ chiều của:", [
        "Lực điện từ tác dụng lên đoạn dây dẫn",
        "Dòng điện trong dây dẫn",
        "Đường sức từ ngoài không gian",
        "Trục quay của khung dây"
    ], 0, "Ngón tay cái choãi 90° chỉ chiều lực điện từ."),
    make_mc(3, "Nhận biết", "Dòng điện cảm ứng xuất hiện trong cuộn dây dẫn kín khi:", [
        "Số đường sức từ xuyên qua tiết diện cuộn dây biến thiên",
        "Nam châm đứng yên bất động trong cuộn dây",
        "Cuộn dây không có từ trường",
        "Dòng điện trong mạch không đổi"
    ], 0, "Dòng cảm ứng xuất hiện khi số đường sức từ qua cuộn dây biến thiên."),
    make_mc(4, "Nhận biết", "Máy biến thế là thiết bị dùng để:", [
        "Biến đổi hiệu điện thế xoay chiều mà không làm thay đổi tần số",
        "Biến đổi dòng một chiều thành dòng xoay chiều",
        "Tạo ra điện năng từ cơ năng",
        "Đo cường độ dòng điện trong mạch"
    ], 0, "Máy biến thế biến đổi hiệu điện thế xoay chiều."),
    make_mc(5, "Nhận biết", "Tần số của dòng điện xoay chiều trong lưới điện quốc gia Việt Nam là:", [
        "50 Hz",
        "60 Hz",
        "100 Hz",
        "220 Hz"
    ], 0, "Tần số điện lưới chuẩn là 50 Hz."),
    make_mc(6, "Nhận biết", "Biện pháp hiệu quả và kinh tế nhất để giảm hao phí khi truyền tải điện năng đi xa là:", [
        "Tăng hiệu điện thế ở đầu đường dây truyền tải bằng máy tăng áp",
        "Tăng tiết diện dây dẫn lên gấp trăm lần",
        "Hạ hiệu điện thế xuống mức 12 V",
        "Dùng dây dẫn bằng vàng nguyên chất"
    ], 0, "Tăng U giúp giảm hao phí tỉ lệ với U^2."),
    make_mc(7, "Thông hiểu", "Một ống dây có dòng điện chạy qua, đầu A đẩy cực Bắc (N) của kim nam châm thử. Đầu A của ống dây là cực:", [
        "Cực Bắc (N)",
        "Cực Nam (S)",
        "Cực âm",
        "Cực dương"
    ], 0, "Đẩy cực Bắc (N) thì đầu đó phải là cực Bắc (N)."),
    make_mc(8, "Thông hiểu", "Một đoạn dây dẫn mang dòng điện đặt song song với các đường sức từ thì lực điện từ tác dụng lên dây có độ lớn bằng:", [
        "0 N",
        "Cực đại",
        "Bằng tích B × I",
        "Bằng vô cực"
    ], 0, "Đoạn dây song song với đường sức từ thì lực từ F = 0."),
    make_mc(9, "Thông hiểu", "Khi cho nam châm quay đều trước một cuộn dây dẫn kín thì trong cuộn dây xuất hiện:", [
        "Dòng điện xoay chiều",
        "Dòng điện một chiều không đổi",
        "Tia laser",
        "Sóng siêu âm"
    ], 0, "Số đường sức từ biến thiên luân phiên sinh dòng điện xoay chiều."),
    make_mc(10, "Thông hiểu", "Một máy biến áp có N1 = 2000 vòng, N2 = 100 vòng. Cắm cuộn sơ cấp vào nguồn U1 = 220 V thì U2 là:", [
        "11 V",
        "44 V",
        "22 V",
        "110 V"
    ], 0, "U2 = 220 × (100 / 2000) = 11 V."),
    make_mc(11, "Thông hiểu", "Nếu tăng hiệu điện thế đường dây truyền tải lên 10 lần thì công suất hao phí tỏa nhiệt sẽ:", [
        "Giảm đi 100 lần",
        "Giảm đi 10 lần",
        "Tăng lên 100 lần",
        "Không thay đổi"
    ], 0, "Php tỉ lệ nghịch với U^2: giảm 10^2 = 100 lần."),
    make_mc(12, "Thông hiểu", "Hai bộ phận chính của máy phát điện xoay chiều là:", [
        "Roto (phần quay) và Stato (phần đứng yên)",
        "Hai cuộn dây giống hệt nhau",
        "Ắc quy và công tắc",
        "Vôn kế và bóng đèn"
    ], 0, "Roto và stato (nam châm và cuộn dây).")
]

p2_rev_t1 = [
    make_tf(1, "Thông hiểu", "Về từ trường của dòng điện và nam châm điện:", [
        ("a", "Từ phổ bên ngoài ống dây có dòng điện giống từ phổ của thanh nam châm thẳng.", True),
        ("b", "Lõi sắt non làm tăng lực từ của ống dây lên hàng nghìn lần.", True),
        ("c", "Khi ngắt điện, lõi sắt non vẫn giữ nguyên từ tính vĩnh cửu như thanh thép.", False),
        ("d", "Tăng cường độ dòng điện qua ống dây giúp tăng lực từ của nam châm điện.", True)
    ], "Lõi sắt non mất hết từ tính ngay khi ngắt dòng điện."),
    make_tf(2, "Thông hiểu", "Về hiện tượng cảm ứng điện từ và dòng xoay chiều:", [
        ("a", "Dòng điện xoay chiều có chiều luân phiên thay đổi theo thời gian.", True),
        ("b", "Đưa nam châm lại gần hoặc ra xa cuộn dây kín đều sinh dòng cảm ứng.", True),
        ("c", "Để nam châm đứng yên trong cuộn dây kín thì dòng điện cảm ứng liên tục sinh ra.", False),
        ("d", "Máy phát điện xoay chiều biến đổi cơ năng thành điện năng.", True)
    ], "Nam châm đứng yên thì từ thông không biến thiên, không có dòng cảm ứng."),
    make_tf(3, "Vận dụng", "Một đoạn dây dẫn dài L = 10 cm mang dòng điện I = 2 A đặt vuông góc trong từ trường đều B = 0,5 T:", [
        ("a", "Lực điện từ tác dụng lên đoạn dây là F = 0,1 N.", True),
        ("b", "Nếu tăng dòng điện lên I = 4 A thì lực từ là F = 0,2 N.", True),
        ("c", "Nếu xoay đoạn dây song song với đường sức từ thì lực từ bằng 0.", True),
        ("d", "Nếu đổi chiều dòng điện thì lực từ vẫn giữ nguyên chiều cũ.", False)
    ], "F = 0,5 × 2 × 0,1 = 0,1 N. Đổi chiều dòng điện thì lực từ đổi chiều ngược lại."),
    make_tf(4, "Vận dụng", "Một máy biến áp cuộn sơ cấp có 1000 vòng, cuộn thứ cấp có 5000 vòng. Đặt vào cuộn sơ cấp điện áp U1 = 220 V:", [
        ("a", "Đây là máy tăng áp.", True),
        ("b", "Tỉ số biến áp N1 / N2 = 0,2.", True),
        ("c", "Hiệu điện thế cuộn thứ cấp là U2 = 1100 V.", True),
        ("d", "Nếu cắm vào nguồn pin 12V một chiều thì điện áp thứ cấp là 60 V.", False)
    ], "U2 = 220 × 5 = 1100 V. Dòng DC không đổi cho U2 = 0 V.")
]

p3_rev_t1 = [
    make_sa(1, "Thông hiểu", "Dòng điện xoay chiều 50 Hz đổi chiều bao nhiêu lần trong 1 giây?", "100", "50 × 2 = 100 lần."),
    make_sa(2, "Thông hiểu", "Máy biến áp có N1 = 500 vòng, N2 = 2000 vòng là máy tăng áp hay hạ áp?", "Tăng áp", "N2 > N1 nên là máy tăng áp."),
    make_sa(3, "Vận dụng", "Máy biến thế có N1 = 400 vòng, N2 = 2000 vòng. Cắm vào nguồn U1 = 110 V thì U2 bằng bao nhiêu Volt?", "550", "U2 = 110 × (2000 / 400) = 550 V."),
    make_sa(4, "Vận dụng", "Muốn giảm hao phí tỏa nhiệt trên đường dây truyền tải đi 25 lần thì cần tăng hiệu điện thế lên mấy lần?", "5", "5^2 = 25 lần."),
    make_sa(5, "Vận dụng cao", "Đoạn dây dài 0,2 m đặt vuông góc trong từ trường B = 0,5 T chịu lực từ F = 0,6 N. Cường độ dòng điện qua dây là bao nhiêu Ampe?", "6", "I = 0,6 / (0,5 × 0,2) = 6 A."),
    make_sa(6, "Vận dụng cao", "Đường dây có R = 10 Ω truyền công suất 200 kW ở điện áp 20 kV. Công suất hao phí là bao nhiêu kW?", "1", "I = 200.000 / 20.000 = 10 A. Php = 10^2 × 10 = 1000 W = 1 kW.")
]

p4_rev_t1 = [
    make_vdc(1, "Đường dây tải điện siêu cao thế 500 kV Bắc - Nam của Việt Nam dài hơn 1500 km truyền điện năng từ các nhà máy thủy điện lớn ở miền Bắc và miền Trung vào miền Nam. Lý do bắt buộc phải dùng cấp điện áp cực cao 500.000 V là:", [
        "Giảm thiểu tối đa tổn thất hao phí do tỏa nhiệt trên chiều dài hơn 1500 km đường dây",
        "Làm dòng điện chạy nhanh hơn tốc độ ánh sáng",
        "Để dây điện không bao giờ bị đứt",
        "Để làm đẹp cảnh quan môi trường"
    ], 0, "Điện áp 500 kV giảm hao phí nhiệt hàng trăm triệu lần so với điện áp hạ thế, giúp truyền tải công suất lớn xuyên quốc gia hiệu quả."),
    make_vdc(2, "Động cơ điện một chiều và động cơ điện xoay chiều hoạt động dựa trên tác dụng nào sau đây?", [
        "Tác dụng của lực từ lên cuộn dây mang dòng điện đặt trong từ trường làm roto quay liên tục",
        "Tác dụng nhiệt làm nóng trục quay",
        "Lực ma sát cơ học giữa các bánh răng",
        "Trọng lực Trái Đất"
    ], 0, "Lực từ tác dụng lên cuộn dây mang dòng điện đặt trong từ trường sinh mômen quay roto."),
    make_vdc(3, "Bếp từ nấu ăn gia đình làm nóng đáy nồi kim loại rất nhanh mà mặt kính bếp hầu như không nóng là nhờ hiện tượng:", [
        "Dòng điện Foucault (dòng điện xoáy) cảm ứng sinh ra trực tiếp trong đáy nồi kim loại khi đặt trong từ trường biến thiên tần số cao của mâm từ",
        "Bếp phát ra lửa hồng ngoại vô hình",
        "Bếp truyền nhiệt trực tiếp qua kính",
        "Sóng âm công suất cực lớn"
    ], 0, "Mâm từ phát từ trường cao tần cảm ứng dòng Foucault nung nóng trực tiếp đáy nồi kim loại sắt từ."),
    make_vdc(4, "Bộ sạc không dây cho điện thoại thông minh truyền năng lượng điện từ đế sạc sang pin điện thoại qua khoảng cách vài milimét là ứng dụng của:", [
        "Hiện tượng cảm ứng điện từ giữa cuộn dây phát trong đế sạc và cuộn dây thu trong điện thoại",
        "Bức xạ nhiệt",
        "Tia laser chiếu qua không khí",
        "Sóng âm thanh"
    ], 0, "Cảm ứng điện từ giữa cuộn phát và cuộn thu truyền năng lượng không dây an toàn và tiện lợi.")
]

exams["phys9_c7_rev_test1"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 1, p1_rev_t1, p2_rev_t1, p3_rev_t1, p4_rev_t1)

# =============================================================================
# phys9_c7_rev_test2
# =============================================================================
p1_rev_t2 = [
    make_mc(1, "Nhận biết", "Trong quy tắc nắm tay phải, chiều bốn ngón tay uốn cong chỉ theo:", [
        "Chiều dòng điện chạy qua các vòng dây",
        "Chiều đường sức từ trong ống dây",
        "Chiều của trục ống dây",
        "Chiều lực hút nam châm"
    ], 0, "Bốn ngón tay chỉ theo chiều dòng điện qua các vòng dây."),
    make_mc(2, "Nhận biết", "Quy tắc bàn tay trái dùng để xác định chiều của đại lượng nào?", [
        "Lực điện từ tác dụng lên đoạn dây dẫn mang dòng điện",
        "Đường sức từ của nam châm thẳng",
        "Dòng điện trong lòng đất",
        "Hiệu điện thế cảm ứng"
    ], 0, "Quy tắc bàn tay trái xác định chiều của lực điện từ."),
    make_mc(3, "Nhận biết", "Dòng điện xoay chiều có thể chạy qua được thiết bị nào sau đây và làm thiết bị hoạt động bình thường?", [
        "Bóng đèn sợi đốt, bàn là, quạt điện",
        "Bình điện phân mạ bạc một chiều",
        "Bộ sạc ắc quy không có mạch nắn dòng",
        "Nam châm vĩnh cửu"
    ], 0, "Bóng đèn sợi đốt, bàn là, quạt điện hoạt động bình thường với dòng xoay chiều."),
    make_mc(4, "Nhận biết", "Máy hạ áp là máy biến thế có:", [
        "N2 < N1 (U2 < U1)",
        "N2 > N1 (U2 > U1)",
        "N2 = N1",
        "N1 = 0"
    ], 0, "Máy hạ áp có N2 < N1 và U2 < U1."),
    make_mc(5, "Nhận biết", "Kí hiệu của ampe kế và vôn kế dùng để đo dòng điện xoay chiều là:", [
        "Kí hiệu AC hoặc dấu ngã (~)",
        "Kí hiệu DC hoặc dấu gạch (-)",
        "Kí hiệu dấu cộng (+)",
        "Kí hiệu chữ P"
    ], 0, "Kí hiệu AC hoặc dấu ngã (~)."),
    make_mc(6, "Nhận biết", "Lực điện từ tác dụng lên đoạn dây dẫn mang dòng điện đổi chiều khi:", [
        "Đổi chiều dòng điện hoặc đổi chiều đường sức từ",
        "Tăng cường độ dòng điện",
        "Giảm chiều dài đoạn dây",
        "Sơn lại vỏ dây dẫn"
    ], 0, "Lực từ đổi chiều khi đổi chiều dòng điện hoặc đổi chiều đường sức từ."),
    make_mc(7, "Thông hiểu", "Một ống dây có dòng điện chạy qua hút cực Nam của một kim nam châm tự do. Đầu đó của ống dây là cực:", [
        "Cực Bắc (N)",
        "Cực Nam (S)",
        "Cực âm",
        "Cực dương"
    ], 0, "Hút cực Nam thì đầu đó phải là cực Bắc (N)."),
    make_mc(8, "Thông hiểu", "Một khung dây dẫn mang dòng điện đặt trong từ trường đều có mặt phẳng khung dây vuông góc với các đường sức từ. Khung dây sẽ:", [
        "Ở trạng thái cân bằng không quay",
        "Quay với tốc độ nhanh nhất",
        "Bị kéo tịnh tiến sang phải",
        "Tự động đổi chiều dòng điện"
    ], 0, "Mặt khung vuông góc đường sức từ thì mômen quay bằng 0, khung cân bằng."),
    make_mc(9, "Thông hiểu", "Khi một nam châm rơi tự do xuyên qua một cuộn dây dẫn kín, trong cuộn dây xuất hiện:", [
        "Dòng điện cảm ứng",
        "Dòng điện một chiều không đổi",
        "Tia X",
        "Sóng radio"
    ], 0, "Từ thông biến thiên làm xuất hiện dòng điện cảm ứng."),
    make_mc(10, "Thông hiểu", "Một máy biến áp có N1 = 1500 vòng, N2 = 300 vòng. Cuộn sơ cấp cắm vào nguồn U1 = 220 V. Hiệu điện thế U2 là:", [
        "44 V",
        "110 V",
        "88 V",
        "22 V"
    ], 0, "U2 = 220 × (300 / 1500) = 44 V."),
    make_mc(11, "Thông hiểu", "Khi truyền tải điện năng đi xa, nếu tăng hiệu điện thế lên 4 lần thì công suất hao phí tỏa nhiệt trên đường dây sẽ:", [
        "Giảm đi 16 lần",
        "Giảm đi 4 lần",
        "Tăng lên 16 lần",
        "Không thay đổi"
    ], 0, "Php giảm 4^2 = 16 lần."),
    make_mc(12, "Thông hiểu", "Động cơ điện chuyển hóa dạng năng lượng nào thành cơ năng?", [
        "Điện năng",
        "Hóa năng",
        "Năng lượng hạt nhân",
        "Quang năng"
    ], 0, "Động cơ điện biến điện năng thành cơ năng.")
]

p2_rev_t2 = [
    make_tf(1, "Thông hiểu", "Về nam châm điện và ứng dụng:", [
        ("a", "Nam châm điện gồm ống dây dẫn có dòng điện và lõi sắt non bên trong.", True),
        ("b", "Lực từ của nam châm điện tăng khi tăng số vòng dây và tăng dòng điện.", True),
        ("c", "Cần cẩu điện dọn phế liệu dùng nam châm vĩnh cửu thay cho nam châm điện.", False),
        ("d", "Rơ le điện từ dùng nam châm điện để đóng ngắt mạch điện tự động.", True)
    ], "Cần cẩu phế liệu bắt buộc dùng nam châm điện để có thể nhả phế liệu khi ngắt điện."),
    make_tf(2, "Thông hiểu", "Về máy biến thế và truyền tải điện năng:", [
        ("a", "Máy biến thế chỉ hoạt động với dòng điện xoay chiều.", True),
        ("b", "Máy hạ áp có hiệu điện thế thứ cấp nhỏ hơn sơ cấp (U2 < U1).", True),
        ("c", "Máy biến áp lý tưởng làm tăng cả hiệu điện thế và công suất điện.", False),
        ("d", "Tăng hiệu điện thế truyền tải giúp giảm hao phí do tỏa nhiệt trên đường dây.", True)
    ], "Máy biến áp không làm tăng công suất điện (P2 ≤ P1)."),
    make_tf(3, "Vận dụng", "Một đoạn dây dẫn dài L = 20 cm mang dòng điện I = 3 A đặt vuông góc trong từ trường đều B = 0,4 T:", [
        ("a", "Lực điện từ tác dụng lên đoạn dây là F = 0,24 N.", True),
        ("b", "Nếu đổi chiều dòng điện thì lực từ đổi chiều ngược lại.", True),
        ("c", "Nếu đồng thời đổi chiều cả dòng điện và từ trường thì lực từ đổi chiều.", False),
        ("d", "Nếu đặt đoạn dây song song với đường sức từ thì lực từ bằng 0.", True)
    ], "F = 0,4 × 3 × 0,2 = 0,24 N. Đổi chiều cả 2 yếu tố thì lực từ giữ nguyên chiều cũ."),
    make_tf(4, "Vận dụng", "Máy biến áp cuộn sơ cấp có 2200 vòng nối nguồn xoay chiều 220 V, cuộn thứ cấp có 100 vòng:", [
        ("a", "Tỉ số biến áp là N1 / N2 = 22.", True),
        ("b", "Hiệu điện thế cuộn thứ cấp là U2 = 10 V.", True),
        ("c", "Nếu nối thứ cấp với điện trở 5 Ω thì dòng điện thứ cấp là I2 = 2 A.", True),
        ("d", "Cường độ dòng điện cuộn sơ cấp là I1 = 44 A.", False)
    ], "I1 = I2 / 22 = 2 / 22 ≈ 0,091 A (không phải 44 A).")
]

p3_rev_t2 = [
    make_sa(1, "Thông hiểu", "Quy tắc nào xác định chiều lực từ tác dụng lên đoạn dây có dòng điện?", "Bàn tay trái", "Quy tắc bàn tay trái."),
    make_sa(2, "Thông hiểu", "Thiết bị dùng để biến đổi hiệu điện thế xoay chiều có tên là gì?", "Máy biến áp", "Máy biến áp (máy biến thế)."),
    make_sa(3, "Vận dụng", "Đoạn dây vuông góc từ trường chịu lực từ F = 0,4 N. Nếu tăng dòng điện lên gấp 3 lần thì lực từ bằng bao nhiêu Newton? (Lấy số thập phân)", "1.2", "F' = 0,4 × 3 = 1,2 N."),
    make_sa(4, "Vận dụng", "Máy biến thế có N1 = 600 vòng, N2 = 3000 vòng. Cuộn sơ cấp cắm nguồn U1 = 120 V. Hiệu điện thế U2 bằng bao nhiêu Volt?", "600", "U2 = 120 × (3000 / 600) = 600 V."),
    make_sa(5, "Vận dụng cao", "Nếu tăng hiệu điện thế truyền tải lên 8 lần thì công suất hao phí nhiệt giảm đi bao nhiêu lần?", "64", "8^2 = 64 lần."),
    make_sa(6, "Vận dụng cao", "Đường dây điện có R = 5 Ω truyền công suất 100 kW ở điện áp 10 kV. Công suất hao phí là bao nhiêu kW? (Lấy số thập phân)", "0.5", "I = 100.000 / 10.000 = 10 A. Php = 10^2 × 5 = 500 W = 0,5 kW.")
]

p4_rev_t2 = [
    make_vdc(1, "Một người thợ sửa chữa lắp đặt hệ thống chuông điện báo khách ở cổng nhà. Khi có khách nhấn chuông ở cổng, nam châm điện trong hộp chuông hút búa gõ đập vào chuông kính coong. Nếu người khách giữ chặt nút chuông không nhả thì chuông vẫn gõ liên hồi là nhờ cơ cấu:", [
        "Tiếp điểm tự ngắt mạch điện gắn ở lá thép đàn hồi của búa gõ tự động đóng ngắt dòng điện liên tục",
        "Nút bấm tự nhảy lên xuống",
        "Dòng điện một chiều tự đổi thành xoay chiều",
        "Một động cơ xăng mini kéo búa"
    ], 0, "Cơ cấu lá thép tiếp điểm tự ngắt mạch: Khi búa gõ đập chuông thì mạch hở làm nam châm nhả búa, búa lùi lại đóng mạch lặp lại chu kỳ."),
    make_vdc(2, "Phanh từ trường hãm chậm không tiếp xúc (Eddy Current Brake) trên các đoàn tàu cao tốc Eurostar: Khi tàu chạy với vận tốc 300 km/h, má phanh cơ học ma sát truyền thống dễ bị bốc cháy và mòn nhanh chóng. Hệ thống phanh từ trường hãm tàu bằng cách:", [
        "Cho dòng điện vào nam châm điện tạo từ trường mạnh xuyên qua đĩa phanh hoặc thanh ray, sinh dòng Foucault cản trở chuyển động quay của bánh xe êm ái mà không bị mòn má phanh",
        "Phun cát vào bánh xe",
        "Dùng dù cản gió phía sau tàu",
        "Ngắt toàn bộ điện của đoàn tàu"
    ], 0, "Phanh từ trường tạo lực hãm Foucault phi tiếp xúc, triệt tiêu mài mòn cơ khí và hoạt động cực kỳ an toàn ở tốc độ cao."),
    make_vdc(3, "Đồng hồ đo điện năng (Công tơ điện cơ khí) gắn trước cửa mỗi ngôi nhà có một đĩa nhôm tròn quay chậm rãi khi gia đình bật thiết bị điện. Đĩa nhôm quay được là nhờ:", [
        "Từ trường của cuộn dòng và cuộn áp tạo ra dòng điện xoáy trong đĩa nhôm, tương tác từ làm đĩa nhôm quay với tốc độ tỉ lệ với công suất tiêu thụ",
        "Gió thổi làm quay đĩa nhôm",
        "Dòng nước chảy qua công tơ",
        "Động cơ lò xo lên dây cót"
    ], 0, "Nguyên lý cảm ứng Ferraris: Từ trường xoay chiều của cuộn dòng và cuộn áp tương tác với dòng xoáy trong đĩa nhôm làm đĩa quay."),
    make_vdc(4, "Một máy biến áp lý tưởng công suất P = 1,1 kW có U1 = 220 V và U2 = 110 V. Cường độ dòng điện ở cuộn sơ cấp I1 và cuộn thứ cấp I2 lần lượt là:", [
        "I1 = 5 A và I2 = 10 A",
        "I1 = 10 A và I2 = 5 A",
        "I1 = 2,5 A và I2 = 5 A",
        "I1 = 1 A và I2 = 2 A"
    ], 0, "I1 = 1100 / 220 = 5 A; I2 = 1100 / 110 = 10 A.")
]

exams["phys9_c7_rev_test2"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 2, p1_rev_t2, p2_rev_t2, p3_rev_t2, p4_rev_t2)

# =============================================================================
# phys9_c7_rev_test3
# =============================================================================
p1_rev_t3 = [
    make_mc(1, "Nhận biết", "Đường sức từ trong lòng ống dây có dòng điện chạy qua có chiều đi từ:", [
        "Cực Nam sang cực Bắc",
        "Cực Bắc sang cực Nam",
        "Từ tâm ra hai đầu",
        "Từ ngoài vỏ vào tâm"
    ], 0, "Trong lòng ống dây, đường sức từ đi từ cực Nam sang cực Bắc."),
    make_mc(2, "Nhận biết", "Quy tắc bàn tay trái áp dụng để tìm chiều của lực từ tác dụng lên đoạn dây dẫn yêu cầu:", [
        "Các đường sức từ phải đâm xuyên vào lòng bàn tay trái",
        "Các đường sức từ đâm vào mu bàn tay",
        "Các đường sức từ song song với ngón tay cái",
        "Các đường sức từ đi vòng quanh cổ tay"
    ], 0, "Đường sức từ đâm thẳng vào lòng bàn tay trái."),
    make_mc(3, "Nhận biết", "Trong máy phát điện xoay chiều lớn, bộ phận đứng yên chứa các cuộn dây phát điện được gọi là:", [
        "Stato",
        "Roto",
        "Trục quay",
        "Cổ góp"
    ], 0, "Stato là phần đứng yên."),
    make_mc(4, "Nhận biết", "Công thức máy biến áp lý tưởng liên hệ giữa U1, U2 và N1, N2 là:", [
        "U1 / U2 = N1 / N2",
        "U1 / U2 = N2 / N1",
        "U1 × U2 = N1 × N2",
        "U1 - U2 = N1 - N2"
    ], 0, "U1 / U2 = N1 / N2."),
    make_mc(5, "Nhận biết", "Cổ góp điện trong động cơ điện một chiều làm nhiệm vụ:", [
        "Đổi chiều dòng điện trong khung dây sau mỗi nửa vòng quay",
        "Tăng điện áp nguồn",
        "Đo nhiệt độ khung dây",
        "Cố định trục quay đứng yên"
    ], 0, "Đổi chiều dòng điện sau mỗi nửa vòng quay."),
    make_mc(6, "Nhận biết", "Tác dụng nhiệt của dòng điện xoay chiều được ứng dụng trong thiết bị nào sau đây?", [
        "Bình nóng lạnh, ấm điện, nồi cơm điện",
        "Quạt máy, máy bơm",
        "Loa phóng thanh",
        "Chuông điện"
    ], 0, "Bình nóng lạnh, ấm điện, nồi cơm điện hoạt động nhờ tác dụng nhiệt."),
    make_mc(7, "Thông hiểu", "Một ống dây có dòng điện đặt cạnh một thanh sắt non. Hiện tượng xảy ra là:", [
        "Ống dây hút thanh sắt non",
        "Ống dây đẩy thanh sắt non ra xa",
        "Không có hiện tượng gì",
        "Thanh sắt non bốc cháy"
    ], 0, "Ống dây có từ trường hút thanh sắt non bị nhiễm từ."),
    make_mc(8, "Thông hiểu", "Khi đoạn dây dẫn có dòng điện đặt vuông góc với từ trường, nếu tăng dòng điện lên gấp đôi thì lực từ sẽ:", [
        "Tăng lên gấp đôi",
        "Giảm đi một nửa",
        "Không đổi",
        "Bằng 0"
    ], 0, "Lực từ tỉ lệ thuận với dòng điện I."),
    make_mc(9, "Thông hiểu", "Một khung dây dẫn kín quay trong từ trường sinh ra dòng điện cảm ứng xoay chiều vì:", [
        "Số đường sức từ xuyên qua tiết diện khung dây luân phiên tăng giảm",
        "Từ trường của nam châm tự mất đi",
        "Khung dây bị cọ xát với không khí",
        "Khung dây tự phát sinh điện tích"
    ], 0, "Số đường sức từ qua tiết diện khung dây biến thiên luân phiên."),
    make_mc(10, "Thông hiểu", "Một máy tăng áp có N1 = 500 vòng, N2 = 2500 vòng. Cắm vào nguồn U1 = 100 V thì U2 bằng:", [
        "500 V",
        "20 V",
        "250 V",
        "1000 V"
    ], 0, "U2 = 100 × (2500 / 500) = 500 V."),
    make_mc(11, "Thông hiểu", "Muốn giảm công suất hao phí tỏa nhiệt trên đường dây truyền tải điện đi 4 lần thì cần:", [
        "Tăng hiệu điện thế lên 2 lần",
        "Tăng hiệu điện thế lên 4 lần",
        "Giảm hiệu điện thế đi 2 lần",
        "Giảm hiệu điện thế đi 4 lần"
    ], 0, "Tăng U lên 2 lần thì Php giảm 2^2 = 4 lần."),
    make_mc(12, "Thông hiểu", "Một nam châm điện có lõi sắt non hút được 20 chiếc đinh sắt. Nếu rút lõi sắt non ra thì:", [
        "Số đinh sắt hút được giảm đi rất nhiều (gần như rơi hết)",
        "Số đinh sắt hút được tăng lên gấp đôi",
        "Không có thay đổi gì",
        "Các đinh sắt bị đẩy bắn ra xa"
    ], 0, "Không có lõi sắt non thì từ trường giảm hàng nghìn lần, đinh sắt rơi hết.")
]

p2_rev_t3 = [
    make_tf(1, "Thông hiểu", "Về các quy tắc bàn tay trong Điện từ học lớp 9:", [
        ("a", "Quy tắc nắm tay phải dùng cho ống dây có dòng điện.", True),
        ("b", "Quy tắc bàn tay trái dùng cho đoạn dây dẫn mang dòng điện đặt trong từ trường.", True),
        ("c", "Hai quy tắc này hoàn toàn giống nhau về cách đặt bàn tay.", False),
        ("d", "Áp dụng đúng quy tắc giúp xác định chuẩn xác cực từ và lực điện từ.", True)
    ], "Quy tắc nắm tay phải và bàn tay trái dùng cho hai hiện tượng hoàn toàn khác nhau."),
    make_tf(2, "Thông hiểu", "Về dòng điện xoay chiều và máy biến áp:", [
        ("a", "Lưới điện sinh hoạt gia đình ở Việt Nam là điện xoay chiều 220 V - 50 Hz.", True),
        ("b", "Máy biến áp có thể biến đổi điện một chiều của pin 1,5 V lên 220 V.", False),
        ("c", "Máy biến áp hoạt động nhờ hiện tượng cảm ứng điện từ.", True),
        ("d", "Máy tăng áp được dùng ở đầu đường dây tải điện để giảm hao phí.", True)
    ], "Máy biến áp không hoạt động với dòng DC không đổi của pin."),
    make_tf(3, "Vận dụng", "Một đoạn dây dẫn dài L = 0,5 m mang dòng điện I = 2 A đặt vuông góc trong từ trường đều B = 0,2 T:", [
        ("a", "Lực điện từ tác dụng lên đoạn dây là F = 0,2 N.", True),
        ("b", "Nếu giảm chiều dài đoạn dây xuống còn 0,25 m thì lực từ là F = 0,1 N.", True),
        ("c", "Nếu xoay đoạn dây nghiêng góc 0 độ so với đường sức từ thì lực từ là F = 0,2 N.", False),
        ("d", "Lực điện từ luôn có phương vuông góc với đoạn dây dẫn.", True)
    ], "F = 0,2 × 2 × 0,5 = 0,2 N. Khi góc = 0° (song song) thì F = 0."),
    make_tf(4, "Vận dụng", "Máy hạ áp sạc xe đạp điện có N1 = 2200 vòng cắm vào nguồn xoay chiều 220 V, lấy ra điện áp U2 = 48 V:", [
        ("a", "Tỉ số biến áp N1 / N2 xấp xỉ bằng 4,58.", True),
        ("b", "Số vòng dây cuộn thứ cấp N2 là 480 vòng.", True),
        ("c", "Đây là một máy hạ áp.", True),
        ("d", "Dòng điện ở cuộn thứ cấp luôn nhỏ hơn dòng điện ở cuộn sơ cấp.", False)
    ], "N2 = 2200 × (48 / 220) = 480 vòng. Máy hạ áp thì dòng thứ cấp I2 lớn hơn dòng sơ cấp I1.")
]

p3_rev_t3 = [
    make_sa(1, "Thông hiểu", "Dòng điện có chiều và cường độ luân phiên biến đổi theo thời gian gọi là dòng điện gì?", "Xoay chiều", "Dòng điện xoay chiều (AC)."),
    make_sa(2, "Thông hiểu", "Để giảm hao phí nhiệt trên đường dây truyền tải điện, người ta tăng đại lượng nào?", "Hiệu điện thế", "Tăng hiệu điện thế U."),
    make_sa(3, "Vận dụng", "Một đoạn dây vuông góc từ trường chịu lực từ F = 0,6 N khi dòng điện I = 2 A. Nếu tăng dòng điện lên I = 5 A thì lực từ bằng bao nhiêu Newton? (Lấy số thập phân)", "1.5", "F' = 0,6 × (5 / 2) = 1,5 N."),
    make_sa(4, "Vận dụng", "Máy biến thế có N1 = 1000 vòng, N2 = 250 vòng. Hiệu điện thế sơ cấp U1 = 220 V. Hiệu điện thế U2 là bao nhiêu Volt?", "55", "U2 = 220 × (250 / 1000) = 55 V."),
    make_sa(5, "Vận dụng cao", "Nếu tăng hiệu điện thế đường dây truyền tải lên 10 lần thì hao phí nhiệt giảm đi bao nhiêu lần?", "100", "10^2 = 100 lần."),
    make_sa(6, "Vận dụng cao", "Đường dây điện có R = 20 Ω truyền công suất 400 kW ở điện áp 40 kV. Công suất hao phí tỏa nhiệt là bao nhiêu kW?", "2", "I = 400.000 / 40.000 = 10 A. Php = 10^2 × 20 = 2000 W = 2 kW.")
]

p4_rev_t3 = [
    make_vdc(1, "Máy biến áp cao tần trong bộ nguồn xung máy tính (Nguồn PSU) có kích thước rất nhỏ gọn (chỉ bằng nắm tay) nhưng có thể truyền tải công suất lên tới 750 W - 1000 W. Bí quyết giúp thu nhỏ kích thước máy biến áp xung là:", [
        "Hoạt động ở tần số cực cao (từ 50 kHz đến 200 kHz) giúp giảm đáng kể kích thước lõi từ ferit và số vòng dây so với tần số 50 Hz truyền thống",
        "Lõi biến áp làm bằng vàng ròng",
        "Không dùng dây đồng bên trong",
        "Nguồn xung không tỏa nhiệt"
    ], 0, "Tần số cao f làm tăng tốc độ biến thiên từ thông, cho phép truyền công suất lớn với lõi ferit và số vòng dây rất nhỏ gọn."),
    make_vdc(2, "Hệ thống phanh điện từ của xe tải hạng nặng chở hàng đường đèo dốc (Retarder): Khi xe xuống dốc dài liên tục, người lái bật cần gạt phanh điện từ để giữ tốc độ xe an toàn mà không cần đạp phanh cơ liên tục. Tác dụng cứu sinh của phanh điện từ trong trường hợp này là:", [
        "Tránh hiện tượng cháy và mất phanh cơ học do ma sát quá nhiệt khi xuống dốc dài, đảm bảo an toàn tuyệt đối cho xe tải nặng",
        "Làm xe tải tự bay lên không trung",
        "Làm tăng tốc độ xe vượt đèo nhanh hơn",
        "Tắt hoàn toàn động cơ xe"
    ], 0, "Phanh từ Retarder hãm bằng dòng xoáy Foucault không ma sát, triệt tiêu nguy cơ cháy má phanh và mất phanh chết người trên đèo dốc."),
    make_vdc(3, "Một cảm biến dòng điện không tiếp xúc (Kìm bấm dòng Ampe kìm): Người thợ điện chỉ cần bấm mỏ kìm kẹp quanh một dây dẫn điện có dòng điện xoay chiều mà không cần cắt dây hay bóc vỏ cách điện vẫn đo được cường độ dòng điện lên tới hàng trăm Ampe. Kìm bấm dòng hoạt động dựa trên:", [
        "Hiện tượng cảm ứng điện từ: mỏ kìm là lõi thép của một máy biến dòng thu từ trường xoay chiều quanh dây dẫn để cảm ứng điện áp đo được",
        "Nhiệt lượng tỏa ra từ vỏ dây điện",
        "Ánh sáng phát ra từ dây điện",
        "Lực ma sát của không khí quanh dây"
    ], 0, "Kìm kẹp là máy biến dòng (Current Transformer - CT): Dây dẫn đóng vai trò cuộn sơ cấp 1 vòng, cuộn thứ cấp trong kìm sinh dòng cảm ứng tỉ lệ đưa vào đồng hồ đo."),
    make_vdc(4, "Một máy phát điện gió mini cung cấp điện cho trạm hải đăng trên đảo xa. Tuabin gió quay làm quay roto nam châm tạo ra dòng điện xoay chiều biến thiên theo tốc độ gió. Để nạp được vào hệ thống ắc quy lưu trữ 24 V của hải đăng, dòng điện phát ra bắt buộc phải đi qua thiết bị nào?", [
        "Một bộ chỉnh lưu (Diode Bridge) để biến đổi dòng điện xoay chiều thành dòng điện một chiều nạp cho ắc quy",
        "Một bóng đèn sợi đốt công suất lớn",
        "Một máy sấy tóc",
        "Một nhiệt kế điện tử"
    ], 0, "Ắc quy chỉ nạp được bằng dòng điện một chiều DC, do đó điện AC từ máy phát gió phải qua cầu chỉnh lưu diode nắn dòng thành DC.")
]

exams["phys9_c7_rev_test3"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 3, p1_rev_t3, p2_rev_t3, p3_rev_t3, p4_rev_t3)

# =============================================================================
# phys9_c7_rev_test4
# =============================================================================
p1_rev_t4 = [
    make_mc(1, "Nhận biết", "Để xác định cực từ của một ống dây có dòng điện chạy qua, ta có thể dùng:", [
        "Quy tắc nắm tay phải hoặc dùng kim nam châm thử",
        "Thước dây cuộn",
        "Nhiệt kế rượu",
        "Cân đồng hồ"
    ], 0, "Dùng quy tắc nắm tay phải hoặc kim nam châm thử tự do."),
    make_mc(2, "Nhận biết", "Lực điện từ tác dụng lên đoạn dây dẫn mang dòng điện vuông góc với từ trường có chiều xác định bằng:", [
        "Quy tắc bàn tay trái",
        "Quy tắc bàn tay phải",
        "Quy tắc vặn nút chai",
        "Quy tắc ngón tay cái bên phải"
    ], 0, "Quy tắc bàn tay trái xác định chiều lực từ."),
    make_mc(3, "Nhận biết", "Dòng điện cảm ứng xuất hiện trong cuộn dây kín đổi chiều khi:", [
        "Chiều biến thiên của số đường sức từ qua cuộn dây đổi chiều",
        "Dòng điện trong mạch chính bằng 0",
        "Nhiệt độ phòng tăng lên",
        "Nam châm đứng yên hoàn toàn"
    ], 0, "Đổi chiều tăng/giảm của từ thông thì dòng cảm ứng đổi chiều."),
    make_mc(4, "Nhận biết", "Khi truyền tải điện năng đi xa, công suất hao phí do tỏa nhiệt Php được tính bằng công thức:", [
        "Php = R × P^2 / U^2",
        "Php = U^2 / R",
        "Php = P / U",
        "Php = R × I"
    ], 0, "Php = R × P^2 / U^2."),
    make_mc(5, "Nhận biết", "Trong máy biến thế, số vòng dây cuộn sơ cấp và thứ cấp là N1 và N2. Khi N2 > N1 thì đây là:", [
        "Máy tăng áp",
        "Máy hạ áp",
        "Máy biến dòng",
        "Động cơ điện"
    ], 0, "N2 > N1 là máy tăng áp (U2 > U1)."),
    make_mc(6, "Nhận biết", "Dòng điện xoay chiều có tác dụng phát sáng được ứng dụng trong:", [
        "Đèn tuýp huỳnh quang và đèn LED",
        "Bàn là điện",
        "Bình nóng lạnh",
        "Máy xay sinh tố"
    ], 0, "Chiếu sáng đèn huỳnh quang và LED là tác dụng phát sáng."),
    make_mc(7, "Thông hiểu", "Một ống dây có dòng điện đặt nằm ngang. Khi đưa cực Bắc của thanh nam châm lại gần đầu bên phải ống dây thấy hai vật hút nhau. Đầu bên phải ống dây là cực:", [
        "Cực Nam (S)",
        "Cực Bắc (N)",
        "Cực dương",
        "Cực âm"
    ], 0, "Hút cực Bắc thì đầu đó là cực Nam (S)."),
    make_mc(8, "Thông hiểu", "Đoạn dây dẫn mang dòng điện đặt trong từ trường đều chịu lực từ F = 0 khi góc giữa dây dẫn và đường sức từ bằng:", [
        "0 độ (hoặc 180 độ)",
        "90 độ",
        "45 độ",
        "60 độ"
    ], 0, "Khi đặt song song (0° hoặc 180°) thì lực từ F = 0."),
    make_mc(9, "Thông hiểu", "Một đinamô xe đạp phát điện thắp sáng bóng đèn khi xe chạy. Nếu xe dừng lại thì bóng đèn:", [
        "Tắt ngay lập tức vì nam châm ngừng quay",
        "Vẫn sáng mãi mãi",
        "Sáng chói hơn",
        "Bị cháy tóc"
    ], 0, "Xe dừng thì nam châm ngừng quay, từ thông ngừng biến thiên nên mất điện, đèn tắt."),
    make_mc(10, "Thông hiểu", "Một máy hạ áp có tỉ số N1 / N2 = 5. Đặt vào cuộn sơ cấp U1 = 110 V thì U2 là:", [
        "22 V",
        "550 V",
        "55 V",
        "11 V"
    ], 0, "U2 = 110 / 5 = 22 V."),
    make_mc(11, "Thông hiểu", "Để giảm công suất hao phí do tỏa nhiệt trên đường dây truyền tải điện đi 9 lần thì cần:", [
        "Tăng hiệu điện thế lên 3 lần",
        "Tăng hiệu điện thế lên 9 lần",
        "Giảm hiệu điện thế đi 3 lần",
        "Giảm hiệu điện thế đi 9 lần"
    ], 0, "Tăng U lên 3 lần thì Php giảm 3^2 = 9 lần."),
    make_mc(12, "Thông hiểu", "Khi sử dụng máy biến áp, ta có thể làm tăng hiệu điện thế nhưng:", [
        "Cường độ dòng điện ở cuộn thứ cấp sẽ giảm tương ứng",
        "Cường độ dòng điện cũng tăng theo",
        "Công suất điện tăng lên gấp đôi",
        "Tần số dòng điện tăng lên gấp đôi"
    ], 0, "Tăng điện áp thì dòng điện phải giảm tương ứng để P2 ≤ P1.")
]

p2_rev_t4 = [
    make_tf(1, "Thông hiểu", "Về từ trường và lực từ trong thực tế:", [
        ("a", "Dòng điện chạy qua dây dẫn sinh ra từ trường xung quanh dây dẫn.", True),
        ("b", "Từ trường tác dụng lực từ lên kim nam châm và dòng điện khác đặt trong nó.", True),
        ("c", "Hai dây dẫn có dòng điện ngược chiều nhau thì hút nhau.", False),
        ("d", "Lực điện từ có ứng dụng quyết định trong chế tạo động cơ điện.", True)
    ], "Hai dòng điện ngược chiều nhau thì đẩy nhau."),
    make_tf(2, "Thông hiểu", "Về máy phát điện và dòng xoay chiều:", [
        ("a", "Máy phát điện biến cơ năng thành điện năng.", True),
        ("b", "Động cơ điện biến điện năng thành cơ năng.", True),
        ("c", "Máy biến áp có thể dùng để phát ra điện năng mới.", False),
        ("d", "Dòng điện xoay chiều đổi chiều liên tục theo thời gian.", True)
    ], "Máy biến áp chỉ truyền và biến đổi điện áp, hoàn toàn không sinh ra năng lượng mới."),
    make_tf(3, "Vận dụng", "Một đoạn dây dẫn dài L = 0,25 m đặt vuông góc trong từ trường đều B = 0,6 T có dòng điện I = 2 A chạy qua:", [
        ("a", "Lực điện từ tác dụng lên đoạn dây là F = 0,3 N.", True),
        ("b", "Nếu tăng dòng điện lên 4 A thì lực từ là F = 0,6 N.", True),
        ("c", "Nếu xoay đoạn dây vuông góc thêm một lần nữa thì lực từ không đổi độ lớn.", True),
        ("d", "Lực điện từ có phương song song với đường sức từ.", False)
    ], "F = 0,6 × 2 × 0,25 = 0,3 N. Lực từ luôn vuông góc với đường sức từ."),
    make_tf(4, "Vận dụng", "Một máy biến áp có N1 = 4000 vòng, N2 = 200 vòng. Cuộn sơ cấp cắm nguồn U1 = 220 V:", [
        ("a", "Tỉ số biến áp là N1 / N2 = 20.", True),
        ("b", "Hiệu điện thế cuộn thứ cấp là U2 = 11 V.", True),
        ("c", "Thiết bị này có chức năng là một máy biến áp hạ thế (máy hạ áp).", True),
        ("d", "Tần số dòng điện ở cuộn thứ cấp nhỏ hơn tần số cuộn sơ cấp 20 lần.", False)
    ], "Tần số dòng điện ở cuộn thứ cấp luôn bằng tần số cuộn sơ cấp (f2 = f1 = 50 Hz).")
]

p3_rev_t4 = [
    make_sa(1, "Thông hiểu", "Bộ phận quay của động cơ điện được gọi là gì?", "Roto", "Roto là phần quay."),
    make_sa(2, "Thông hiểu", "Số lần đổi chiều trong 1 chu kỳ của dòng điện xoay chiều là mấy lần?", "2", "2 lần trong 1 chu kỳ."),
    make_sa(3, "Vận dụng", "Đoạn dây vuông góc từ trường chịu lực từ F = 0,5 N. Nếu từ trường B tăng gấp 3 lần thì lực từ bằng bao nhiêu Newton? (Lấy số thập phân)", "1.5", "F' = 0,5 × 3 = 1,5 N."),
    make_sa(4, "Vận dụng", "Máy biến thế có N1 = 500 vòng, N2 = 100 vòng. Cắm vào nguồn U1 = 220 V thì U2 bằng bao nhiêu Volt?", "44", "U2 = 220 × (100 / 500) = 44 V."),
    make_sa(5, "Vận dụng cao", "Nếu tăng hiệu điện thế truyền tải lên 7 lần thì công suất hao phí nhiệt giảm đi bao nhiêu lần?", "49", "7^2 = 49 lần."),
    make_sa(6, "Vận dụng cao", "Đường dây điện có R = 15 Ω truyền công suất 300 kW ở điện áp 30 kV. Công suất hao phí tỏa nhiệt là bao nhiêu kW? (Lấy số thập phân)", "1.5", "I = 300.000 / 30.000 = 10 A. Php = 10^2 × 15 = 1500 W = 1,5 kW.")
]

p4_rev_t4 = [
    make_vdc(1, "Trong hệ thống phanh hãm của thang máy chở người tại các tòa nhà cao ốc: Một nam châm điện cực mạnh luôn được cấp điện để mở ngàm phanh cho cabin thang máy chạy lên xuống tự do. Khi có sự cố đứt dây điện hoặc mất điện toàn tòa nhà, cabin thang máy sẽ được bảo vệ như thế nào?", [
        "Nam châm điện mất điện lập tức mất từ tính, hệ thống lò xo cơ học cực mạnh tự động bung ra ép chặt các má phanh vào thanh ray dẫn hướng, khóa cứng cabin tại chỗ chống rơi tự do",
        "Cabin rơi tự do xuống hố thang",
        "Thang máy tự động bay lên nóc nhà",
        "Cửa thang máy tự động mở toang"
    ], 0, "Cơ cấu phanh an toàn Fail-Safe: Có điện thì nam châm hút mở ngàm phanh, mất điện thì lò xo tự bung kẹp chặt thanh ray chống rơi."),
    make_vdc(2, "Hệ thống trạm biến áp không người trực (Unmanned Substation) trong lưới điện thông minh 4.0: Toàn bộ quá trình đóng ngắt máy cắt cao thế, đo đạc thông số dòng điện, điện áp và cảnh báo nhiệt độ máy biến áp được truyền tín hiệu số hóa qua đường truyền cáp quang về trung tâm điều độ. Thiết bị đo dòng điện cao thế mà không cần tiếp xúc kim loại trực tiếp là:", [
        "Máy biến dòng quang học hoặc máy biến dòng cảm ứng điện từ",
        "Nhiệt kế thủy ngân",
        "Thước dây cuộn",
        "Cân điện tử"
    ], 0, "Máy biến dòng cảm ứng hoặc cảm biến quang đo dòng cao thế an toàn tuyệt đối và số hóa dữ liệu về trung tâm điều hành."),
    make_vdc(3, "Một hộ gia đình lắp đặt hệ thống pin năng lượng mặt trời trên mái nhà công suất 5 kWp. Điện do các tấm pin mặt trời sinh ra là dòng điện một chiều (DC). Để hòa lượng điện này vào lưới điện sinh hoạt gia đình 220 V xoay chiều (AC), thiết bị bắt buộc phải có là:", [
        "Bộ nghịch lưu điện (Inverter) biến đổi dòng điện một chiều DC thành dòng điện xoay chiều AC đồng pha và cùng tần số 50 Hz với lưới điện",
        "Máy phát điện chạy dầu diesel",
        "Một bình ắc quy xe máy",
        "Một công tắc đổi chiều cơ học"
    ], 0, "Inverter chuyển đổi DC từ pin mặt trời thành AC 220V - 50 Hz hòa vào lưới điện gia đình."),
    make_vdc(4, "Một máy biến áp hạ áp cung cấp điện cho xưởng may mini. Điện áp sơ cấp là U1 = 220 V, điện áp thứ cấp là U2 = 110 V. Nếu công suất tiêu thụ của xưởng may là 4,4 kW và máy biến áp có hiệu suất 100% thì cường độ dòng điện ở cuộn sơ cấp là:", [
        "20 A",
        "10 A",
        "40 A",
        "5 A"
    ], 0, "I1 = P / U1 = 4400 / 220 = 20 A.")
]

exams["phys9_c7_rev_test4"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 4, p1_rev_t4, p2_rev_t4, p3_rev_t4, p4_rev_t4)

# =============================================================================
# phys9_c7_rev_test5
# =============================================================================
p1_rev_t5 = [
    make_mc(1, "Nhận biết", "Trong lòng ống dây có dòng điện chạy qua, các đường sức từ có đặc điểm:", [
        "Là những đường thẳng song song cách đều nhau",
        "Là những đường tròn đồng tâm",
        "Là những đường gấp khúc",
        "Cắt nhau tại một điểm"
    ], 0, "Từ trường trong lòng ống dây là từ trường đều."),
    make_mc(2, "Nhận biết", "Quy tắc bàn tay trái dùng để xác định:", [
        "Chiều của lực điện từ",
        "Chiều của dòng điện cảm ứng",
        "Chiều của đường sức từ",
        "Chiều của điện trường"
    ], 0, "Quy tắc bàn tay trái xác định chiều lực từ."),
    make_mc(3, "Nhận biết", "Dòng điện cảm ứng xuất hiện trong cuộn dây kín khi:", [
        "Số đường sức từ qua tiết diện cuộn dây biến thiên",
        "Cuộn dây đứng yên trong từ trường đều",
        "Cắt đứt cuộn dây làm đôi",
        "Dòng điện trong cuộn dây không đổi"
    ], 0, "Dòng cảm ứng sinh ra khi từ thông biến thiên."),
    make_mc(4, "Nhận biết", "Máy biến thế là thiết bị hoạt động dựa trên hiện tượng:", [
        "Hiện tượng cảm ứng điện từ",
        "Hiện tượng quang điện",
        "Hiện tượng nhiệt điện",
        "Hiện tượng phóng điện hồ quang"
    ], 0, "Máy biến thế hoạt động dựa trên hiện tượng cảm ứng điện từ."),
    make_mc(5, "Nhận biết", "Để giảm hao phí điện năng khi truyền tải đi xa, giải pháp tối ưu nhất là:", [
        "Tăng hiệu điện thế ở đầu đường dây truyền tải",
        "Hạ hiệu điện thế",
        "Tăng điện trở đường dây",
        "Giảm chiều dài đường dây"
    ], 0, "Tăng U là giải pháp tối ưu nhất."),
    make_mc(6, "Nhận biết", "Một máy tăng áp có số vòng dây hai cuộn là N1 và N2 thoả mãn:", [
        "N2 > N1 (U2 > U1)",
        "N2 < N1 (U2 < U1)",
        "N2 = N1",
        "N1 = 0"
    ], 0, "Tăng áp: N2 > N1 dẫn tới U2 > U1."),
    make_mc(7, "Thông hiểu", "Một ống dây có dòng điện hút cực Bắc kim nam châm ở đầu trái. Đầu trái của ống dây là cực:", [
        "Cực Nam (S)",
        "Cực Bắc (N)",
        "Cực dương",
        "Cực âm"
    ], 0, "Hút cực Bắc thì đầu đó là cực Nam (S)."),
    make_mc(8, "Thông hiểu", "Khi cho một khung dây dẫn kín quay đều trong từ trường đều quanh một trục vuông góc với các đường sức từ thì trong khung dây xuất hiện:", [
        "Dòng điện xoay chiều",
        "Dòng điện một chiều không đổi",
        "Tia lửa điện tĩnh",
        "Sóng siêu âm tần số cao"
    ], 0, "Khung dây quay trong từ trường làm từ thông biến thiên tuần hoàn sinh ra dòng điện xoay chiều."),
    make_mc(9, "Thông hiểu", "Trong nhà máy nhiệt điện than, tuabin hơi nước làm quay bộ phận nào của máy phát điện xoay chiều?", [
        "Roto nam châm điện",
        "Stato cuộn dây",
        "Các cột điện cao thế",
        "Bình làm mát nước"
    ], 0, "Tuabin hơi nước làm quay roto nam châm điện của máy phát."),
    make_mc(10, "Thông hiểu", "Một máy biến áp có N1 = 1000 vòng, N2 = 50 vòng. Cắm vào nguồn U1 = 220 V thì U2 là:", [
        "11 V",
        "22 V",
        "44 V",
        "5 V"
    ], 0, "U2 = 220 × (50 / 1000) = 11 V."),
    make_mc(11, "Thông hiểu", "Nếu tăng hiệu điện thế đường dây truyền tải lên 2 lần thì công suất hao phí nhiệt sẽ:", [
        "Giảm đi 4 lần",
        "Giảm đi 2 lần",
        "Tăng lên 4 lần",
        "Không đổi"
    ], 0, "Php giảm 2^2 = 4 lần."),
    make_mc(12, "Thông hiểu", "Dòng điện xoay chiều 220V chạy qua bóng đèn sợi đốt làm đèn phát sáng nhờ:", [
        "Tác dụng nhiệt làm nóng sáng dây tóc vonfram",
        "Tác dụng từ",
        "Tác dụng sinh học",
        "Tác dụng hóa học"
    ], 0, "Tác dụng nhiệt nung nóng dây tóc phát sáng.")
]

p2_rev_t5 = [
    make_tf(1, "Thông hiểu", "Về từ trường của ống dây và nam châm điện:", [
        ("a", "Từ trường trong lòng ống dây có dòng điện là từ trường đều.", True),
        ("b", "Việc đặt lõi sắt non vào trong lòng ống dây giúp tập trung và làm tăng cường độ từ trường một cách đáng kể.", True),
        ("c", "Ống dây có dòng điện không có hai cực Bắc Nam.", False),
        ("d", "Ngắt dòng điện thì nam châm điện có lõi sắt non mất từ tính ngay lập tức.", True)
    ], "Ống dây có dòng điện có hai cực từ Bắc và Nam rõ rệt."),
    make_tf(2, "Thông hiểu", "Về máy biến áp và dòng xoay chiều:", [
        ("a", "Dòng điện xoay chiều có chiều và cường độ luân phiên biến đổi theo thời gian.", True),
        ("b", "Máy biến áp chỉ hoạt động với dòng xoay chiều, không hoạt động với dòng một chiều.", True),
        ("c", "Máy tăng áp làm tăng điện áp nhưng làm giảm cường độ dòng điện tương ứng.", True),
        ("d", "Máy hạ áp có cuộn thứ cấp nhiều vòng dây hơn cuộn sơ cấp.", False)
    ], "Máy hạ áp có N2 < N1 (ít vòng hơn)."),
    make_tf(3, "Vận dụng", "Một đoạn dây dẫn dài L = 0,4 m mang dòng điện I = 5 A đặt vuông góc trong từ trường đều B = 0,2 T:", [
        ("a", "Lực điện từ tác dụng lên đoạn dây là F = 0,4 N.", True),
        ("b", "Nếu tăng dòng điện lên I = 10 A thì lực từ là F = 0,8 N.", True),
        ("c", "Nếu xoay đoạn dây song song với đường sức từ thì lực từ là F = 0.", True),
        ("d", "Lực từ có phương trùng với phương của đoạn dây dẫn.", False)
    ], "F = 0,2 × 5 × 0,4 = 0,4 N. Lực từ luôn vuông góc với đoạn dây dẫn."),
    make_tf(4, "Vận dụng", "Máy biến thế có N1 = 2000 vòng, N2 = 500 vòng. Cuộn sơ cấp cắm nguồn xoay chiều 220 V:", [
        ("a", "Tỉ số biến áp là N1 / N2 = 4.", True),
        ("b", "Hiệu điện thế cuộn thứ cấp là U2 = 55 V.", True),
        ("c", "Vì U2 < U1 nên máy biến thế này đóng vai trò là máy giảm áp.", True),
        ("d", "Nếu cắm vào bình ắc quy 24V một chiều thì cuộn thứ cấp cho điện áp 6 V.", False)
    ], "U2 = 220 / 4 = 55 V. Dòng DC từ ắc quy cho U2 = 0 V.")
]

p3_rev_t5 = [
    make_sa(1, "Thông hiểu", "Lõi của nam châm điện làm bằng vật liệu gì để mất từ tính ngay khi ngắt điện?", "Sắt non", "Lõi sắt non."),
    make_sa(2, "Thông hiểu", "Thiết bị biến đổi cơ năng thành điện năng xoay chiều gọi là gì?", "Máy phát điện", "Máy phát điện xoay chiều."),
    make_sa(3, "Vận dụng", "Đoạn dây vuông góc từ trường chịu lực từ F = 0,8 N. Nếu dòng điện giảm đi một nửa thì lực từ bằng bao nhiêu Newton? (Lấy số thập phân)", "0.4", "F' = 0,8 / 2 = 0,4 N."),
    make_sa(4, "Vận dụng", "Máy biến thế có N1 = 400 vòng, N2 = 1200 vòng. Cắm vào nguồn U1 = 100 V thì U2 bằng bao nhiêu Volt?", "300", "U2 = 100 × (1200 / 400) = 300 V."),
    make_sa(5, "Vận dụng cao", "Nếu tăng hiệu điện thế truyền tải lên 12 lần thì công suất hao phí nhiệt giảm đi bao nhiêu lần?", "144", "12^2 = 144 lần."),
    make_sa(6, "Vận dụng cao", "Đường dây điện có R = 25 Ω truyền công suất 500 kW ở điện áp 50 kV. Công suất hao phí tỏa nhiệt là bao nhiêu kW? (Lấy số thập phân)", "2.5", "I = 500.000 / 50.000 = 10 A. Php = 10^2 × 25 = 2500 W = 2,5 kW.")
]

p4_rev_t5 = [
    make_vdc(1, "Một người thợ điện kiểm tra một máy biến áp gia đình bị hỏng: Khi cắm điện vào cuộn sơ cấp 220 V thì máy biến áp phát ra tiếng kêu 'u u' rung mạnh và thân máy rất nóng dù cuộn thứ cấp chưa cắm thiết bị tải nào. Nguyên nhân vật lý có khả năng cao nhất là:", [
        "Các lá thép kỹ thuật mỏng trong lõi thép bị lỏng hoặc lớp sơn cách điện giữa các lá thép bị bong tróc làm sinh dòng điện xoáy Foucault rất lớn gây nóng lõi và rung cơ học",
        "Có người đổ nước vào máy",
        "Dòng điện trong nhà biến thành dòng một chiều",
        "Dây đồng cuộn sơ cấp bị biến thành vàng"
    ], 0, "Bong tróc cách điện giữa các lá thép làm dòng Foucault tăng vọt chạy quẩn trong lõi, gây tổn thất sắt lớn làm máy rung u u và nóng rực."),
    make_vdc(2, "Trong các xưởng gia công cơ khí chính xác, bàn hút từ tính (Magnetic Chuck) trên máy mài phẳng sử dụng nam châm điện để kẹp giữ chặt phôi thép khi mài mà không cần dùng hàm kẹp bu-lông. Ưu điểm vượt trội của bàn hút từ tính này là:", [
        "Kẹp giữ phôi phẳng hoàn toàn không làm cong vênh mép phôi, lực kẹp phân bố đều trên khắp diện tích tiếp xúc và nhả phôi nhanh chóng chỉ bằng một nút bấm ngắt điện",
        "Làm phôi thép tự mài nhẵn không cần đá mài",
        "Làm nguội phôi thép xuống âm độ",
        "Tự động đo độ dày phôi thép"
    ], 0, "Bàn từ giữ phôi đều lực, không biến dạng cơ học, kẹp nhả tức thời bằng công tắc điện."),
    make_vdc(3, "Hệ thống truyền tải điện một chiều điện áp siêu cao thế (HVDC - High Voltage Direct Current): Trong các tuyến truyền tải điện ngầm xuyên biển dài hàng trăm kilômét (như giữa các quốc gia Bắc Âu), người ta nắn dòng AC thành DC siêu cao thế để truyền qua cáp ngầm, rồi đảo lại thành AC ở đầu nhận. Lý do HVDC vượt trội hơn AC trong cáp ngầm biển siêu dài là:", [
        "Triệt tiêu hoàn toàn tổn thất công suất phản kháng do dung kháng ký sinh lớn giữa lõi cáp và nước biển xung quanh",
        "Dòng một chiều không bao giờ bị tỏa nhiệt",
        "Cáp DC không cần vỏ bọc cách điện",
        "Cáp DC tự nổi trên mặt nước biển"
    ], 0, "Cáp ngầm biển dài có điện dung C ký sinh rất lớn gây tổn thất công suất phản kháng nặng với AC; HVDC triệt tiêu tổn thất này."),
    make_vdc(4, "Một máy biến áp lý tưởng có hiệu suất 100%. Cuộn sơ cấp N1 = 1000 vòng cắm vào nguồn U1 = 200 V. Cuộn thứ cấp N2 = 500 vòng nối với bóng đèn có công suất tiêu thụ P = 50 W. Cường độ dòng điện ở cuộn sơ cấp I1 là:", [
        "0,25 A",
        "0,5 A",
        "1,0 A",
        "0,1 A"
    ], 0, "P1 = P2 = 50 W => I1 = P1 / U1 = 50 / 200 = 0,25 A.")
]

exams["phys9_c7_rev_test5"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 5, p1_rev_t5, p2_rev_t5, p3_rev_t5, p4_rev_t5)

print("Added phys9_c7_rev (5 tests).")
