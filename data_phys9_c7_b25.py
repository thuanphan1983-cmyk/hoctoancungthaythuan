# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 25: MÁY BIẾN THẾ
Bao gồm 3 đề thi độc lập 100%: phys9_c7_b25_test1, phys9_c7_b25_test2, phys9_c7_b25_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c7"
CH_TITLE = "Chương VII: Điện từ"

# =============================================================================
# BÀI 25: MÁY BIẾN THẾ (3 ĐỀ)
# =============================================================================

# --- phys9_c7_b25_test1 ---
p1_b25_t1 = [
    make_mc(1, "Nhận biết", "Máy biến thế (máy biến áp) là một thiết bị điện dùng để:", [
        "Biến đổi hiệu điện thế của dòng điện xoay chiều mà không làm thay đổi tần số",
        "Biến đổi dòng điện xoay chiều thành dòng điện một chiều",
        "Tạo ra điện năng từ năng lượng gió",
        "Tích trữ điện năng như một bình ắc quy"
    ], 0, "Máy biến thế dùng để biến đổi hiệu điện thế xoay chiều."),
    make_mc(2, "Nhận biết", "Hai bộ phận chính của một máy biến áp là:", [
        "Lõi sắt (hoặc thép) pha silic và hai cuộn dây có số vòng dây khác nhau quấn cách điện",
        "Nam châm vĩnh cửu và cổ góp điện",
        "Bình chứa dung dịch axit và hai bản cực chì",
        "Một bóng đèn sợi đốt và một công tắc"
    ], 0, "Hai bộ phận chính là lõi thép kỹ thuật và hai cuộn dây dẫn cách điện."),
    make_mc(3, "Nhận biết", "Cuộn dây của máy biến áp được nối trực tiếp với nguồn điện xoay chiều được gọi là:", [
        "Cuộn sơ cấp",
        "Cuộn thứ cấp",
        "Cuộn dây phụ",
        "Cuộn khử từ"
    ], 0, "Cuộn nối với nguồn điện gọi là cuộn sơ cấp (N1, U1)."),
    make_mc(4, "Nhận biết", "Cuộn dây của máy biến áp lấy hiệu điện thế ra cấp cho các thiết bị tiêu thụ điện được gọi là:", [
        "Cuộn thứ cấp",
        "Cuộn sơ cấp",
        "Cuộn tiếp địa",
        "Cuộn cảm kháng"
    ], 0, "Cuộn lấy điện ra nối với tải gọi là cuộn thứ cấp (N2, U2)."),
    make_mc(5, "Nhận biết", "Mối liên hệ giữa hiệu điện thế ở hai đầu các cuộn dây và số vòng dây của máy biến áp là:", [
        "U1 / U2 = N1 / N2",
        "U1 / U2 = N2 / N1",
        "U1 × U2 = N1 × N2",
        "U1 + U2 = N1 + N2"
    ], 0, "U1 / U2 = N1 / N2."),
    make_mc(6, "Nhận biết", "Máy tăng áp là máy biến áp có số vòng dây cuộn thứ cấp N2 so với cuộn sơ cấp N1 thoả mãn:", [
        "N2 > N1 (U2 > U1)",
        "N2 < N1 (U2 < U1)",
        "N2 = N1 (U2 = U1)",
        "N2 = 0"
    ], 0, "Máy tăng áp có N2 > N1 dẫn đến U2 > U1."),
    make_mc(7, "Thông hiểu", "Một máy hạ áp cắm vào nguồn điện sinh hoạt 220 V có số vòng dây N1 = 1000 vòng và N2 = 50 vòng. Hiệu điện thế U2 lấy ra ở cuộn thứ cấp là:", [
        "11 V",
        "44 V",
        "22 V",
        "110 V"
    ], 0, "U2 = U1 × (N2 / N1) = 220 × (50 / 1000) = 11 V."),
    make_mc(8, "Thông hiểu", "Nếu đặt vào hai đầu cuộn sơ cấp của máy biến áp một nguồn pin một chiều không đổi 12 V thì hiệu điện thế đo được ở hai đầu cuộn thứ cấp bằng:", [
        "0 V",
        "12 V",
        "24 V",
        "6 V"
    ], 0, "Dòng điện một chiều không đổi sinh ra từ trường không biến thiên nên từ thông không đổi, U2 = 0 V."),
    make_mc(9, "Thông hiểu", "Khi truyền tải điện năng đi xa trên đường dây tải điện, công suất hao phí do tỏa nhiệt trên đường dây tỉ lệ:", [
        "Nghịch với bình phương hiệu điện thế đặt vào hai đầu đường dây truyền tải",
        "Thuận với bình phương hiệu điện thế",
        "Nghịch với điện trở đường dây",
        "Thuận với thời gian truyền tải"
    ], 0, "Php = R × P^2 / U^2 nên tỉ lệ nghịch với U^2."),
    make_mc(10, "Thông hiểu", "Để giảm công suất hao phí do tỏa nhiệt trên đường dây truyền tải điện đi 100 lần thì người ta cần:", [
        "Tăng hiệu điện thế ở hai đầu đường dây truyền tải lên 10 lần",
        "Tăng hiệu điện thế lên 100 lần",
        "Giảm hiệu điện thế đi 10 lần",
        "Giảm điện trở đường dây đi 10.000 lần"
    ], 0, "Php giảm 100 lần khi U tăng √100 = 10 lần."),
    make_mc(11, "Thông hiểu", "Tại các trạm phát điện của nhà máy điện, trước khi đưa điện năng lên đường dây cao thế truyền đi xa, người ta phải lắp đặt:", [
        "Máy tăng áp",
        "Máy hạ áp",
        "Bình ắc quy",
        "Máy phát điện một chiều"
    ], 0, "Phải dùng máy tăng áp để tăng U lên hàng trăm kilôvôn giảm hao phí nhiệt."),
    make_mc(12, "Thông hiểu", "Lõi thép của máy biến áp được cấu tạo từ nhiều lá thép mỏng ghép cách điện với nhau thay vì một khối thép đặc nhằm mục đích:", [
        "Làm giảm dòng điện xoáy Foucault gây nóng lõi và hao phí điện năng",
        "Làm máy biến áp nhẹ hơn",
        "Làm tăng điện trở của cuộn dây đồng",
        "Chống rỉ sét bên ngoài"
    ], 0, "Ghép các lá mỏng cách điện triệt tiêu dòng Foucault chạy quẩn trong lõi thép, giảm tổn thất không tải.")
]

p2_b25_t1 = [
    make_tf(1, "Thông hiểu", "Về nguyên tắc hoạt động của máy biến áp:", [
        ("a", "Máy biến áp hoạt động dựa trên hiện tượng cảm ứng điện từ.", True),
        ("b", "Máy biến áp chỉ hoạt động với dòng điện xoay chiều, không hoạt động với dòng điện một chiều không đổi.", True),
        ("c", "Máy biến áp có thể làm tăng hoặc giảm tần số của dòng điện xoay chiều.", False),
        ("d", "Từ trường trong lõi thép của máy biến áp là từ trường biến thiên liên tục.", True)
    ], "Máy biến áp chỉ biến đổi hiệu điện thế và cường độ dòng điện, tần số f không bao giờ thay đổi."),
    make_tf(2, "Thông hiểu", "Về việc truyền tải điện năng đi xa:", [
        ("a", "Hao phí điện năng chủ yếu trên đường dây tải điện là do hiện tượng tỏa nhiệt Joules - Lenz trên dây dẫn.", True),
        ("b", "Biện pháp kinh tế và hiệu quả nhất để giảm hao phí là tăng hiệu điện thế truyền tải bằng máy biến áp.", True),
        ("c", "Biện pháp tăng tiết diện dây dẫn lên gấp trăm lần là giải pháp tối ưu và tiết kiệm nhất.", False),
        ("d", "Đường dây tải điện siêu cao thế 500 kV Bắc - Nam của Việt Nam nhằm giảm thiểu tối đa hao phí trên khoảng cách dài.", True)
    ], "Tăng tiết diện dây đồng làm dây quá nặng, cột điện phải to lớn tốn kém chi phí kim loại khổng lồ."),
    make_tf(3, "Vận dụng", "Một máy biến áp có cuộn sơ cấp N1 = 4400 vòng, cuộn thứ cấp N2 = 220 vòng. Hiệu điện thế sơ cấp U1 = 220 V:", [
        ("a", "Tỉ số biến áp N1 / N2 = 20.", True),
        ("b", "Đây là một máy hạ áp.", True),
        ("c", "Hiệu điện thế ở hai đầu cuộn thứ cấp là U2 = 11 V.", True),
        ("d", "Nếu đổi nguồn cấp vào cuộn thứ cấp (U2 = 220 V) thì ở cuộn N1 sẽ cho hiệu điện thế 11 V.", False)
    ], "U2 = 220 / 20 = 11 V. Nếu cắm 220V vào N2 thì U1_ra = 220 × 20 = 4400 V (máy tăng áp)."),
    make_tf(4, "Vận dụng", "Truyền tải một công suất điện P = 100 kW bằng đường dây có điện trở R = 10 Ω dưới hiệu điện thế U = 10 kV (10.000 V):", [
        ("a", "Cường độ dòng điện trên đường dây truyền tải là I = 10 A.", True),
        ("b", "Công suất hao phí do tỏa nhiệt trên đường dây là Php = 1 kW (1000 W).", True),
        ("c", "Hiệu suất truyền tải điện đạt 99%.", True),
        ("d", "Nếu tăng hiệu điện thế lên U = 20 kV thì công suất hao phí giảm đi 2 lần.", False)
    ], "Tăng U lên 2 lần thì Php giảm đi 2^2 = 4 lần (còn 250 W, hiệu suất 99,75%).")
]

p3_b25_t1 = [
    make_sa(1, "Thông hiểu", "Máy biến áp có N1 = 1000 vòng, N2 = 4000 vòng là máy tăng áp hay hạ áp?", "Tăng áp", "N2 > N1 nên là máy tăng áp."),
    make_sa(2, "Thông hiểu", "Máy biến thế có hoạt động được với dòng điện một chiều không đổi từ pin không? (Trả lời: Có hoặc Không)", "Không", "Không hoạt động với dòng DC không đổi."),
    make_sa(3, "Vận dụng", "Một máy biến áp có N1 = 500 vòng, N2 = 2500 vòng. Đặt vào cuộn sơ cấp U1 = 220 V. Hiệu điện thế U2 bằng bao nhiêu Volt?", "1100", "U2 = 220 × (2500 / 500) = 1100 V."),
    make_sa(4, "Vận dụng", "Muốn giảm công suất hao phí do tỏa nhiệt trên đường dây truyền tải đi 16 lần thì cần tăng hiệu điện thế lên bao nhiêu lần?", "4", "4^2 = 16 lần."),
    make_sa(5, "Vận dụng cao", "Một máy hạ áp sạc điện thoại có N1 = 2200 vòng nối vào mạng 220 V để lấy ra điện áp U2 = 5 V. Số vòng dây cuộn thứ cấp N2 bằng bao nhiêu vòng?", "50", "N2 = 2200 × (5 / 220) = 50 vòng."),
    make_sa(6, "Vận dụng cao", "Đường dây tải điện có điện trở R = 20 Ω truyền công suất P = 200 kW dưới hiệu điện thế U = 20 kV (20.000 V). Công suất hao phí trên đường dây là bao nhiêu kW?", "2", "I = 200.000 / 20.000 = 10 A. Php = I^2 × R = 100 × 20 = 2000 W = 2 kW.")
]

p4_b25_t1 = [
    make_vdc(1, "Tại sao trên toàn tuyến lưới điện quốc gia Việt Nam cũng như trên thế giới, điện năng từ các nhà máy điện (thủy điện, nhiệt điện, điện khí) bắt buộc phải được truyền tải dưới dạng dòng điện xoay chiều (AC) điện áp cao thế (như 110 kV, 220 kV, 500 kV) mà không dùng điện một chiều hạ thế 220 V?", [
        "Vì dòng điện xoay chiều có thể dễ dàng tăng hiệu điện thế lên cực cao bằng máy biến áp để giảm thiểu tổn thất truyền tải hàng trăm triệu lần, sau đó lại hạ thế an toàn tại các khu dân cư",
        "Vì dòng điện một chiều không thể chạy trong dây đồng",
        "Vì dòng xoay chiều không bao giờ bị giật điện",
        "Vì dòng một chiều làm dây điện bị rỉ sét nhanh hơn"
    ], 0, "Khả năng biến đổi điện áp linh hoạt và hiệu suất cao của máy biến áp xoay chiều là lý do quyết định AC thống trị truyền tải điện toàn cầu."),
    make_vdc(2, "Máy hàn điện hồ quang (hàn que) dùng trong cơ khí chế tạo thực chất là một máy biến áp đặc biệt. Khi hàn, người thợ cần dòng điện cực lớn (từ 100 A đến 300 A) để nung chảy que hàn kim loại nhưng điện áp chỉ cần khoảng 30 V đến 50 V để an toàn. Máy hàn này là loại máy gì?", [
        "Máy hạ áp có cuộn thứ cấp ít vòng dây nhưng dây quấn rất to để chịu được dòng điện cực lớn",
        "Máy tăng áp có cuộn thứ cấp nhiều vòng dây",
        "Máy phát điện gió mini",
        "Bình ắc quy hóa học"
    ], 0, "Máy hàn là máy hạ áp: U2 nhỏ nhưng I2 cực lớn, dây cuộn thứ cấp phải rất to bản để chịu dòng hàng trăm ampe sinh nhiệt nung chảy sắt."),
    make_vdc(3, "Một trạm biến áp phân phối hạ thế 22 kV / 0,4 kV đặt trong khu đô thị sử dụng máy biến áp ngâm dầu làm mát. Dầu biến áp chuyên dụng trong thùng máy biến áp có hai chức năng tối quan trọng là:", [
        "Cách điện tuyệt đối giữa các cuộn dây với vỏ máy và tản nhiệt truyền nhiệt lượng tỏa ra từ lõi thép ra các cánh tản nhiệt bên ngoài",
        "Bôi trơn các bánh răng quay bên trong máy biến áp",
        "Làm nhiên liệu đốt nóng máy biến áp",
        "Lọc sạch không khí khu dân cư"
    ], 0, "Dầu biến áp có độ cách điện cao và truyền nhiệt đối lưu làm mát cuộn dây và lõi thép ra cánh tản nhiệt."),
    make_vdc(4, "Một hộ gia đình ở vùng nông thôn cuối nguồn điện lưới bị sụt áp (điện chỉ còn 160 V khiến điều hòa và tủ lạnh không chạy được) đã mua một chiếc ổn áp tự động (Lioa). Bản chất của chiếc máy ổn áp Lioa thực chất là:", [
        "Một máy biến áp tự ngẫu có chổi than quét tự động điều chỉnh số vòng dây cuộn thứ cấp bằng động cơ servo để luôn giữ điện áp đầu ra ổn định ở mức 220 V",
        "Một máy phát điện chạy xăng dự phòng mini",
        "Một bình ắc quy lưu trữ điện ban đêm",
        "Một cầu dao ngắt điện tự động"
    ], 0, "Ổn áp là máy biến áp tự ngẫu điều khiển tự động vị trí chổi than trên cuộn dây để bù sụt áp giữ U_ra = 220V.")
]

exams["phys9_c7_b25_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b25", "Bài 25: Máy biến thế", 1, p1_b25_t1, p2_b25_t1, p3_b25_t1, p4_b25_t1)

# --- phys9_c7_b25_test2 ---
p1_b25_t2 = [
    make_mc(1, "Nhận biết", "Máy hạ áp là máy biến áp có:", [
        "Hiệu điện thế cuộn thứ cấp nhỏ hơn hiệu điện thế cuộn sơ cấp (U2 < U1)",
        "Hiệu điện thế cuộn thứ cấp lớn hơn cuộn sơ cấp (U2 > U1)",
        "Số vòng dây cuộn thứ cấp lớn hơn cuộn sơ cấp (N2 > N1)",
        "Điện trở cuộn thứ cấp bằng 0"
    ], 0, "Máy hạ áp có U2 < U1 (và N2 < N1)."),
    make_mc(2, "Nhận biết", "Nguyên tắc hoạt động của máy biến thế dựa trên hiện tượng vật lý nào?", [
        "Hiện tượng cảm ứng điện từ",
        "Hiện tượng khúc xạ ánh sáng",
        "Hiện tượng tán sắc ánh sáng",
        "Hiện tượng phản xạ toàn phần"
    ], 0, "Máy biến thế hoạt động dựa trên hiện tượng cảm ứng điện từ."),
    make_mc(3, "Nhận biết", "Trong một máy biến áp, tỉ số giữa hiệu điện thế ở hai đầu cuộn sơ cấp và thứ cấp (U1 / U2) bằng:", [
        "Tỉ số giữa số vòng dây cuộn sơ cấp và thứ cấp (N1 / N2)",
        "Nghịch đảo tỉ số số vòng dây (N2 / N1)",
        "Bình phương tỉ số số vòng dây",
        "Căn bậc hai của tỉ số số vòng dây"
    ], 0, "U1 / U2 = N1 / N2."),
    make_mc(4, "Nhận biết", "Để giảm hao phí điện năng do tỏa nhiệt trên đường dây truyền tải, phương án tối ưu và hiệu quả nhất là:", [
        "Tăng hiệu điện thế ở đầu đường dây truyền tải",
        "Giảm hiệu điện thế ở đầu đường dây truyền tải",
        "Tăng chiều dài của đường dây truyền tải",
        "Dùng dây dẫn có điện trở suất thật lớn"
    ], 0, "Tăng U là phương án tối ưu nhất vì giảm hao phí tỉ lệ với U^2."),
    make_mc(5, "Nhận biết", "Cục sạc pin điện thoại thông minh cắm vào ổ điện 220 V để lấy ra điện áp 5 V thực chất chứa bên trong một:", [
        "Máy hạ áp kết hợp mạch chỉnh lưu điện",
        "Máy tăng áp công suất lớn",
        "Động cơ điện mini",
        "Máy phát điện gió"
    ], 0, "Cục sạc điện thoại hạ áp từ 220V xuống 5V và nắn dòng thành một chiều DC."),
    make_mc(6, "Nhận biết", "Nếu số vòng dây cuộn sơ cấp N1 gấp 4 lần số vòng dây cuộn thứ cấp N2 thì máy biến áp này làm hiệu điện thế:", [
        "Giảm đi 4 lần (máy hạ áp)",
        "Tăng lên 4 lần (máy tăng áp)",
        "Giảm đi 16 lần",
        "Tăng lên 16 lần"
    ], 0, "N1 / N2 = 4 => U1 / U2 = 4 => U2 = U1 / 4 (giảm 4 lần)."),
    make_mc(7, "Thông hiểu", "Một máy biến áp có cuộn sơ cấp 500 vòng, cuộn thứ cấp 1500 vòng. Đặt vào cuộn sơ cấp điện áp 110 V thì điện áp cuộn thứ cấp là:", [
        "330 V",
        "55 V",
        "110 V",
        "440 V"
    ], 0, "U2 = 110 × (1500 / 500) = 330 V."),
    make_mc(8, "Thông hiểu", "Khi tăng hiệu điện thế ở hai đầu đường dây truyền tải lên gấp 3 lần thì công suất hao phí do tỏa nhiệt trên đường dây sẽ:", [
        "Giảm đi 9 lần",
        "Giảm đi 3 lần",
        "Tăng lên 9 lần",
        "Tăng lên 3 lần"
    ], 0, "Php tỉ lệ nghịch với U^2: tăng U lên 3 lần thì Php giảm 3^2 = 9 lần."),
    make_mc(9, "Thông hiểu", "Vì sao không thể dùng dòng điện một chiều không đổi từ pin để chạy máy biến áp?", [
        "Vì dòng điện không đổi sinh ra từ trường không đổi, không có sự biến thiên từ thông để tạo dòng cảm ứng ở cuộn thứ cấp",
        "Vì pin có hiệu điện thế quá lớn",
        "Vì pin làm máy biến áp bị nhiễm từ vĩnh viễn",
        "Vì dòng một chiều không chạy được qua dây đồng"
    ], 0, "Từ trường không đổi thì từ thông qua cuộn thứ cấp không biến thiên, không sinh ra suất điện động cảm ứng."),
    make_mc(10, "Thông hiểu", "Một máy biến áp lý tưởng có U1 = 220 V, U2 = 11 V. Nếu cường độ dòng điện ở cuộn sơ cấp là I1 = 0,1 A thì cường độ dòng điện ở cuộn thứ cấp I2 bằng:", [
        "2 A",
        "0,005 A",
        "0,1 A",
        "1 A"
    ], 0, "Máy lý tưởng: P1 = P2 => U1 × I1 = U2 × I2 => 220 × 0,1 = 11 × I2 => I2 = 2 A."),
    make_mc(11, "Thông hiểu", "Vật liệu làm lõi thép máy biến áp thường được pha thêm nguyên tố silic (thép kỹ thuật điện) nhằm mục đích:", [
        "Tăng điện trở suất của thép để triệt tiêu dòng điện xoáy Foucault gây nóng lõi",
        "Làm lõi thép phát sáng trong bóng tối",
        "Làm lõi thép mềm dẻo như cao su",
        "Làm tăng khối lượng máy biến áp"
    ], 0, "Pha silic làm tăng điện trở của thép, hạn chế dòng Foucault chạy trong lõi."),
    make_mc(12, "Thông hiểu", "Đường dây truyền tải điện Bắc - Nam của Việt Nam có cấp điện áp cao nhất là:", [
        "500 kV (500.000 V)",
        "220 V",
        "110 V",
        "35 kV"
    ], 0, "Đường dây siêu cao thế Bắc - Nam có cấp điện áp 500 kV.")
]

p2_b25_t2 = [
    make_tf(1, "Thông hiểu", "Về cấu tạo và thông số máy biến áp:", [
        ("a", "Cuộn sơ cấp và cuộn thứ cấp hoàn toàn cách điện với nhau về mặt điện học.", True),
        ("b", "Năng lượng điện được truyền từ cuộn sơ cấp sang cuộn thứ cấp thông qua từ trường biến thiên trong lõi thép.", True),
        ("c", "Máy biến áp có thể tạo ra năng lượng điện mới từ hư không.", False),
        ("d", "Lõi thép của máy biến áp khép kín mạch từ để dẫn từ thông.", True)
    ], "Máy biến áp tuân theo định luật bảo toàn năng lượng, công suất ra luôn nhỏ hơn hoặc bằng công suất vào (P2 ≤ P1)."),
    make_tf(2, "Thông hiểu", "Về máy biến áp tăng áp và hạ áp:", [
        ("a", "Máy tăng áp có số vòng dây cuộn thứ cấp lớn hơn cuộn sơ cấp (N2 > N1).", True),
        ("b", "Máy tăng áp cho ta lợi về hiệu điện thế nhưng thiệt về cường độ dòng điện (I2 < I1).", True),
        ("c", "Máy biến áp lý tưởng cho ta lợi về cả hiệu điện thế và công suất điện.", False),
        ("d", "Máy hạ áp thường được lắp đặt ở đầu các khu dân cư để cấp điện an toàn 220 V.", True)
    ], "Không máy biến áp nào cho lợi về công suất (P2 = U2.I2 ≤ P1 = U1.I1)."),
    make_tf(3, "Vận dụng", "Một máy biến áp có N1 = 2000 vòng, N2 = 100 vòng. Cuộn sơ cấp cắm vào nguồn U1 = 220 V:", [
        ("a", "Tỉ số biến áp là N1 / N2 = 20.", True),
        ("b", "Hiệu điện thế cuộn thứ cấp là U2 = 11 V.", True),
        ("c", "Nếu cuộn thứ cấp nối với điện trở R = 5,5 Ω thì dòng điện thứ cấp là I2 = 2 A.", True),
        ("d", "Cường độ dòng điện chạy trong cuộn sơ cấp lớn hơn cường độ dòng điện cuộn thứ cấp.", False)
    ], "Hạ áp 20 lần thì dòng điện sơ cấp nhỏ hơn thứ cấp 20 lần: I1 = I2 / 20 = 2 / 20 = 0,1 A."),
    make_tf(4, "Vận dụng", "Đường dây tải điện dài có điện trở R = 5 Ω truyền công suất P = 500 kW ở hiệu điện thế U = 50 kV (50.000 V):", [
        ("a", "Cường độ dòng điện trên đường dây là I = 10 A.", True),
        ("b", "Công suất hao phí do tỏa nhiệt là Php = 500 W (0,5 kW).", True),
        ("c", "Tỉ lệ phần trăm hao phí là 0,1%.", True),
        ("d", "Nếu giảm hiệu điện thế xuống còn 25 kV thì công suất hao phí giảm đi một nửa.", False)
    ], "I = 500.000 / 50.000 = 10 A. Php = 10^2 × 5 = 500 W. Giảm U xuống một nửa thì Php tăng gấp 4 lần lên 2000 W.")
]

p3_b25_t2 = [
    make_sa(1, "Thông hiểu", "Máy biến áp có N1 = 2000 vòng, N2 = 500 vòng là máy tăng áp hay hạ áp?", "Hạ áp", "N2 < N1 nên là máy hạ áp."),
    make_sa(2, "Thông hiểu", "Đơn vị đo hiệu điện thế thường dùng là Volt (V), 1 kV bằng bao nhiêu Volt?", "1000", "1 kV = 1000 V."),
    make_sa(3, "Vận dụng", "Một máy biến áp có N1 = 400 vòng, N2 = 2000 vòng. Đặt vào cuộn sơ cấp U1 = 120 V. Hiệu điện thế U2 bằng bao nhiêu Volt?", "600", "U2 = 120 × (2000 / 400) = 600 V."),
    make_sa(4, "Vận dụng", "Nếu tăng hiệu điện thế đường dây truyền tải lên 5 lần thì công suất hao phí tỏa nhiệt giảm đi bao nhiêu lần?", "25", "5^2 = 25 lần."),
    make_sa(5, "Vận dụng cao", "Một máy hạ áp có U1 = 220 V, U2 = 12 V. Biết cuộn sơ cấp có 1100 vòng. Cuộn thứ cấp có bao nhiêu vòng dây?", "60", "N2 = 1100 × (12 / 220) = 60 vòng."),
    make_sa(6, "Vận dụng cao", "Một đường dây điện có R = 15 Ω truyền tải công suất 300 kW ở hiệu điện thế 30 kV. Công suất hao phí tỏa nhiệt trên đường dây là bao nhiêu kW? (Lấy số thập phân)", "1.5", "I = 300.000 / 30.000 = 10 A. Php = 10^2 × 15 = 1500 W = 1,5 kW.")
]

p4_b25_t2 = [
    make_vdc(1, "Trong lưới điện thông minh (Smart Grid), tại sao các trạm biến áp trung gian phân phối điện năng lại phải trải qua nhiều cấp hạ thế liên tiếp (500 kV -> 220 kV -> 110 kV -> 22 kV -> 0,4 kV) trước khi đưa vào từng hộ gia đình thay vì hạ thẳng từ 500 kV xuống 220 V bằng 1 máy biến áp duy nhất?", [
        "Hạ áp nhiều cấp giúp phân phối điện theo từng vùng lãnh thổ, đảm bảo an toàn cách điện thực tế, giảm chi phí chế tạo cách điện cho thiết bị và tối ưu hóa điều phối phụ tải",
        "Vì không thể chế tạo được máy biến áp có tỉ số vòng dây lớn",
        "Vì dòng điện hạ thế không truyền được quá 1 mét",
        "Vì máy biến áp một cấp tự động phát nổ"
    ], 0, "Phân cấp điện áp giúp quản lý mạng lưới linh hoạt, an toàn khoảng cách phóng điện và tối ưu kinh tế cho từng cấp phụ tải."),
    make_vdc(2, "Máy biến áp đánh lửa trong động cơ xe máy (Mô bin sườn - Ignition Coil) dùng để tạo ra tia lửa điện ở bu-gi đốt cháy hòa khí xăng gió. Mô bin sườn nhận xung điện áp 12 V từ ắc quy và kích lên hiệu điện thế cuộn thứ cấp lên tới 15.000 V đến 25.000 V. Nhận xét đúng về cấu tạo của mô bin sườn là:", [
        "Là máy tăng áp cực lớn có số vòng dây cuộn thứ cấp gấp hàng nghìn lần cuộn sơ cấp",
        "Là máy hạ áp",
        "Là một động cơ điện mini",
        "Là một tụ điện phân cực"
    ], 0, "Môbin là máy biến áp tăng áp xung cực mạnh (N2/N1 hàng nghìn lần) để tạo tia lửa điện cao thế phóng qua khe hở bu-gi."),
    make_vdc(3, "Một hộ gia đình sử dụng điện năng 200 kWh mỗi tháng. Nếu toàn bộ hệ thống truyền tải điện lưới quốc gia giảm được công suất hao phí nhiệt từ 8% xuống còn 5% nhờ nâng cấp các đường dây siêu cao thế 500 kV mạch 3 thì ý nghĩa kinh tế và môi trường lớn nhất là:", [
        "Tiết kiệm hàng tỷ kWh điện năng mỗi năm, giảm bớt nhu cầu đốt hàng triệu tấn than đá và giảm phát thải hàng triệu tấn khí CO2 gây hiệu ứng nhà kính",
        "Làm giá điện tăng lên gấp mười lần",
        "Làm Trái Đất quay nhanh hơn",
        "Làm các bóng đèn trong nhà sáng gấp đôi"
    ], 0, "Giảm hao phí truyền tải giúp tiết kiệm nguồn tài nguyên nhiên liệu hóa thạch và cắt giảm phát thải khí nhà kính bảo vệ khí hậu."),
    make_vdc(4, "Một máy biến áp lý tưởng hoạt động với công suất toàn phần P = 2,2 kW. Cuộn sơ cấp cắm vào nguồn U1 = 220 V. Cuộn thứ cấp cấp điện cho một lò sưởi điện 110 V. Cường độ dòng điện ở cuộn sơ cấp I1 và cuộn thứ cấp I2 lần lượt là:", [
        "I1 = 10 A và I2 = 20 A",
        "I1 = 20 A và I2 = 10 A",
        "I1 = 1 A và I2 = 2 A",
        "I1 = 5 A và I2 = 10 A"
    ], 0, "I1 = P / U1 = 2200 / 220 = 10 A. I2 = P / U2 = 2200 / 110 = 20 A.")
]

exams["phys9_c7_b25_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b25", "Bài 25: Máy biến thế", 2, p1_b25_t2, p2_b25_t2, p3_b25_t2, p4_b25_t2)

# --- phys9_c7_b25_test3 ---
p1_b25_t3 = [
    make_mc(1, "Nhận biết", "Máy biến áp không có khả năng biến đổi đại lượng nào sau đây của dòng điện xoay chiều?", [
        "Tần số của dòng điện",
        "Hiệu điện thế của dòng điện",
        "Cường độ của dòng điện",
        "Biên độ điện áp"
    ], 0, "Máy biến áp giữ nguyên tần số f của dòng điện."),
    make_mc(2, "Nhận biết", "Công thức tính công suất hao phí do tỏa nhiệt trên đường dây truyền tải điện là:", [
        "Php = R × P^2 / U^2",
        "Php = U × I",
        "Php = R × U^2 / P",
        "Php = P × U / R"
    ], 0, "Php = R × P^2 / U^2."),
    make_mc(3, "Nhận biết", "Trong máy biến áp, cuộn sơ cấp và cuộn thứ cấp có số vòng dây N1 và N2. Khi N1 > N2 thì đây là:", [
        "Máy hạ áp",
        "Máy tăng áp",
        "Máy phát điện",
        "Động cơ điện"
    ], 0, "N1 > N2 => U1 > U2 nên là máy hạ áp."),
    make_mc(4, "Nhận biết", "Trong máy biến áp, khi N1 < N2 thì hiệu điện thế cuộn thứ cấp so với cuộn sơ cấp là:", [
        "U2 > U1 (máy tăng áp)",
        "U2 < U1 (máy hạ áp)",
        "U2 = U1",
        "U2 = 0"
    ], 0, "N2 > N1 => U2 > U1 (máy tăng áp)."),
    make_mc(5, "Nhận biết", "Khi truyền tải cùng một công suất điện P trên cùng một đường dây dẫn, nếu hiệu điện thế tăng lên 4 lần thì công suất hao phí do tỏa nhiệt sẽ:", [
        "Giảm đi 16 lần",
        "Giảm đi 4 lần",
        "Tăng lên 16 lần",
        "Không thay đổi"
    ], 0, "Php tỉ lệ nghịch với U^2: 4^2 = 16 lần."),
    make_mc(6, "Nhận biết", "Thiết bị nào sau đây dùng để biến đổi hiệu điện thế xoay chiều 220 V thành 110 V cho các thiết bị điện nhập khẩu từ Nhật Bản hoặc Mỹ?", [
        "Máy biến áp hạ áp",
        "Máy biến áp tăng áp",
        "Máy phát điện xoay chiều",
        "Bình ắc quy khô"
    ], 0, "Cần dùng máy hạ áp 220V xuống 110V."),
    make_mc(7, "Thông hiểu", "Một máy biến áp có cuộn sơ cấp N1 = 1200 vòng và cuộn thứ cấp N2 = 300 vòng. Nếu đặt vào cuộn sơ cấp điện áp U1 = 240 V thì điện áp U2 là:", [
        "60 V",
        "480 V",
        "120 V",
        "30 V"
    ], 0, "U2 = 240 × (300 / 1200) = 60 V."),
    make_mc(8, "Thông hiểu", "Một máy hạ áp lý tưởng có tỉ số biến áp N1 / N2 = 10. Khi cường độ dòng điện ở cuộn sơ cấp là I1 = 0,5 A thì cường độ dòng điện ở cuộn thứ cấp là:", [
        "5 A",
        "0,05 A",
        "0,5 A",
        "50 A"
    ], 0, "Máy lý tưởng: I2 / I1 = N1 / N2 = 10 => I2 = 0,5 × 10 = 5 A."),
    make_mc(9, "Thông hiểu", "Nếu thay một đường dây tải điện bằng dây dẫn cùng chiều dài nhưng có tiết diện lớn gấp đôi thì công suất hao phí tỏa nhiệt trên đường dây sẽ:", [
        "Giảm đi một nửa",
        "Tăng lên gấp đôi",
        "Giảm đi 4 lần",
        "Không thay đổi"
    ], 0, "Tiết diện tăng gấp đôi thì điện trở R giảm một nửa, Php = I^2.R giảm một nửa."),
    make_mc(10, "Thông hiểu", "Tại sao máy biến áp KHÔNG thể dùng để biến đổi dòng điện một chiều của pin 9V thành 220V?", [
        "Vì dòng điện một chiều không đổi không tạo ra từ trường biến thiên để sinh ra dòng điện cảm ứng",
        "Vì pin 9V quá đắt",
        "Vì cuộn dây máy biến áp chỉ nhận dòng điện màu xanh",
        "Vì lõi thép máy biến áp chỉ hút dòng xoay chiều"
    ], 0, "Dòng DC không đổi thì từ thông không đổi, U2 = 0."),
    make_mc(11, "Thông hiểu", "Trong một máy biến áp, năng lượng điện bị hao phí chủ yếu dưới dạng:", [
        "Nhiệt năng tỏa ra trên dây quấn bằng đồng và lõi thép",
        "Quang năng phát sáng",
        "Hóa năng tích tụ",
        "Cơ năng làm máy bay lên"
    ], 0, "Hao phí biến áp gồm tổn thất đồng (I^2.R cuộn dây) và tổn thất sắt (dòng Foucault và từ trễ trong lõi thép)."),
    make_mc(12, "Thông hiểu", "Một trạm biến áp trung gian có công suất truyền tải P = 10 MW (10.000 kW) ở điện áp 110 kV. Nếu nâng điện áp lên 220 kV thì công suất hao phí trên đường dây sẽ:", [
        "Giảm đi 4 lần",
        "Giảm đi 2 lần",
        "Tăng lên 4 lần",
        "Không đổi"
    ], 0, "Điện áp tăng từ 110 kV lên 220 kV (tăng 2 lần) thì hao phí giảm 2^2 = 4 lần.")
]

p2_b25_t3 = [
    make_tf(1, "Thông hiểu", "Về các đặc tính của máy biến áp:", [
        ("a", "Máy biến áp chỉ làm việc với dòng điện xoay chiều.", True),
        ("b", "Tỉ số hiệu điện thế bằng tỉ số số vòng dây của hai cuộn dây: U1 / U2 = N1 / N2.", True),
        ("c", "Máy tăng áp làm tăng hiệu điện thế đồng thời làm tăng cả cường độ dòng điện.", False),
        ("d", "Lõi thép của máy biến áp gồm các lá thép kỹ thuật mỏng sơn cách điện ghép lại.", True)
    ], "Tăng hiệu điện thế thì cường độ dòng điện phải giảm tương ứng (P = U.I không đổi)."),
    make_tf(2, "Thông hiểu", "Về vấn đề giảm hao phí điện năng khi truyền tải:", [
        ("a", "Công suất hao phí tỉ lệ nghịch với bình phương hiệu điện thế truyền tải.", True),
        ("b", "Tăng hiệu điện thế truyền tải là giải pháp tối ưu nhất.", True),
        ("c", "Dùng dây dẫn bạc nguyên chất là biện pháp phổ biến và kinh tế nhất trong thực tế.", False),
        ("d", "Máy tăng áp được đặt tại nhà máy phát điện, máy hạ áp đặt tại nơi tiêu thụ.", True)
    ], "Bạc nguyên chất cực kỳ đắt tiền, không thể dùng làm dây truyền tải dài hàng nghìn km."),
    make_tf(3, "Vận dụng", "Một máy biến áp có cuộn sơ cấp 1000 vòng, cuộn thứ cấp 200 vòng. Cuộn sơ cấp nối với nguồn điện xoay chiều 220 V:", [
        ("a", "Đây là máy hạ áp có tỉ số N1 / N2 = 5.", True),
        ("b", "Hiệu điện thế ở hai đầu cuộn thứ cấp là U2 = 44 V.", True),
        ("c", "Nếu cuộn thứ cấp hở mạch (không nối tải) thì U2 vẫn bằng 44 V.", True),
        ("d", "Nếu cắm cuộn sơ cấp vào bình ắc quy 12 V thì U2 bằng 2,4 V.", False)
    ], "U2 = 220 / 5 = 44 V. Mạch hở vẫn có hiệu điện thế cảm ứng. Cắm vào ắc quy DC thì U2 = 0 V."),
    make_tf(4, "Vận dụng", "Đường dây tải điện có điện trở tổng cộng R = 8 Ω truyền tải công suất P = 400 kW dưới điện áp U = 20 kV (20.000 V):", [
        ("a", "Cường độ dòng điện trên đường dây là I = 20 A.", True),
        ("b", "Công suất hao phí tỏa nhiệt trên đường dây là Php = 3,2 kW (3200 W).", True),
        ("c", "Hiệu suất truyền tải đạt 99,2%.", True),
        ("d", "Nếu tăng hiệu điện thế lên 40 kV thì công suất hao phí giảm còn 1,6 kW.", False)
    ], "I = 400.000 / 20.000 = 20 A. Php = 20^2 × 8 = 3200 W = 3,2 kW. Tăng U lên 2 lần thì Php giảm 4 lần còn 0,8 kW (không phải 1,6 kW).")
]

p3_b25_t3 = [
    make_sa(1, "Thông hiểu", "Máy biến áp có N1 = 600 vòng, N2 = 3000 vòng là máy tăng áp hay hạ áp?", "Tăng áp", "N2 > N1 nên là máy tăng áp."),
    make_sa(2, "Thông hiểu", "Tỉ số U1/U2 bằng tỉ số nào giữa số vòng dây N1 và N2?", "N1/N2", "U1 / U2 = N1 / N2."),
    make_sa(3, "Vận dụng", "Một máy biến áp có N1 = 800 vòng, N2 = 200 vòng. Cuộn sơ cấp cắm vào điện áp 220 V. Hiệu điện thế cuộn thứ cấp U2 bằng bao nhiêu Volt?", "55", "U2 = 220 × (200 / 800) = 55 V."),
    make_sa(4, "Vận dụng", "Nếu tăng hiệu điện thế truyền tải lên 6 lần thì công suất hao phí tỏa nhiệt giảm đi bao nhiêu lần?", "36", "6^2 = 36 lần."),
    make_sa(5, "Vận dụng cao", "Một máy hạ áp có N1 = 4400 vòng nối vào mạng 220 V để lấy ra điện áp U2 = 6 V. Số vòng dây cuộn thứ cấp N2 bằng bao nhiêu vòng?", "120", "N2 = 4400 × (6 / 220) = 120 vòng."),
    make_sa(6, "Vận dụng cao", "Một đường dây điện có R = 12 Ω truyền công suất 600 kW ở hiệu điện thế 60 kV. Công suất hao phí tỏa nhiệt trên đường dây là bao nhiêu kW? (Lấy số thập phân)", "1.2", "I = 600.000 / 60.000 = 10 A. Php = 10^2 × 12 = 1200 W = 1,2 kW.")
]

p4_b25_t3 = [
    make_vdc(1, "Bếp nấu cảm ứng từ (bếp từ) hoạt động trên nguyên lý máy biến áp đặc biệt: Mâm từ dưới mặt kính đóng vai trò cuộn sơ cấp (nhiều vòng dây), còn đáy nồi kim loại đặt lên mặt bếp đóng vai trò như:", [
        "Một cuộn thứ cấp có đúng 1 vòng dây bị đoản mạch (ngắn mạch), sinh dòng điện cảm ứng Foucault khổng lồ làm nóng đỏ đáy nồi trực tiếp",
        "Một cuộn thứ cấp có hàng triệu vòng dây",
        "Một thanh nam châm vĩnh cửu",
        "Một tấm gương phản xạ ánh sáng"
    ], 0, "Đáy nồi kim loại hoạt động như cuộn thứ cấp 1 vòng bị ngắn mạch (R rất nhỏ), dòng Foucault cực lớn sinh nhiệt nấu chín thức ăn tức thì."),
    make_vdc(2, "Trong lò luyện kim bằng cảm ứng điện từ (Induction Furnace) dùng để nấu chảy thép phế liệu: Người ta cho dòng điện xoay chiều cao tần chạy qua cuộn dây đồng làm mát bằng nước bao quanh nồi nấu. Các khối thép vụn bên trong nồi bị nóng chảy thành thép lỏng ở 1600 độ C là nhờ:", [
        "Dòng điện xoáy Foucault cảm ứng sinh ra trực tiếp trong các khối thép với mật độ cực lớn làm thép tự nung chảy từ bên trong",
        "Lửa than đốt từ dưới đáy lò",
        "Tia laser chiếu từ trên nóc lò",
        "Khí gas cháy trong lò"
    ], 0, "Lò cảm ứng dùng dòng Foucault siêu mạnh cảm ứng trực tiếp trong khối thép, nấu chảy kim loại siêu sạch không lẫn tạp chất than."),
    make_vdc(3, "Một máy phát điện gió ngoài khơi tạo ra công suất 5 MW ở điện áp 690 V. Để truyền tải lượng điện này vào bờ biển cách xa 40 km qua tuyến cáp ngầm dưới đáy biển, ngay tại chân trụ tháp gió bắt buộc phải lắp đặt thiết bị nào?", [
        "Một máy biến áp tăng áp từ 690 V lên 33 kV hoặc 66 kV để giảm dòng điện truyền tải, tránh làm sôi nước biển xung quanh cáp ngầm",
        "Một máy hạ áp xuống 12 V",
        "Một động cơ điện kéo dây cáp",
        "Một bóng đèn cao áp chiếu sáng"
    ], 0, "Phải tăng áp lên 33 kV hoặc 66 kV để giảm dòng điện qua cáp ngầm, giảm hao phí nhiệt và chống quá nhiệt cáp dưới biển."),
    make_vdc(4, "Một máy biến áp tự ngẫu dùng trong phòng thí nghiệm (Variac) có cuộn dây quấn trên lõi sắt hình xuyến với một con trượt than có thể xoay tròn tiếp xúc trên các vòng dây. Người dùng xoay núm điều khiển để:", [
        "Thay đổi số vòng dây lấy ra ở cuộn thứ cấp, cho phép điều chỉnh điện áp đầu ra liên tục từ 0 V đến 250 V một cách êm ái",
        "Đổi tần số dòng điện từ 50 Hz lên 5000 Hz",
        "Biến dòng xoay chiều thành pin ắc quy",
        "Làm tăng công suất của nhà máy điện"
    ], 0, "Variac thay đổi tỉ số vòng dây liên tục nhờ con trượt than quét trên các vòng dây, cấp điện áp biến thiên liên tục 0-250V cho các bài thí nghiệm.")
]

exams["phys9_c7_b25_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b25", "Bài 25: Máy biến thế", 3, p1_b25_t3, p2_b25_t3, p3_b25_t3, p4_b25_t3)

print("Added phys9_c7_b25 (3 tests).")
