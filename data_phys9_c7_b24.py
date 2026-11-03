# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 24: HIỆN TƯỢNG CẢM ỨNG ĐIỆN TỪ. DÒNG ĐIỆN XOAY CHIỀU
Bao gồm 3 đề thi độc lập 100%: phys9_c7_b24_test1, phys9_c7_b24_test2, phys9_c7_b24_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c7"
CH_TITLE = "Chương VII: Điện từ"

# =============================================================================
# BÀI 24: HIỆN TƯỢNG CẢM ỨNG ĐIỆN TỪ. DÒNG ĐIỆN XOAY CHIỀU (3 ĐỀ)
# =============================================================================

# --- phys9_c7_b24_test1 ---
p1_b24_t1 = [
    make_mc(1, "Nhận biết", "Dòng điện cảm ứng xuất hiện trong một cuộn dây dẫn kín khi:", [
        "Số đường sức từ xuyên qua tiết diện của cuộn dây dẫn kín biến thiên (tăng lên hoặc giảm đi)",
        "Đặt một nam châm đứng yên bất động bên trong lòng cuộn dây",
        "Nối cuộn dây với một thỏi pin một chiều",
        "Cuộn dây được nhúng trong nước đá lạnh"
    ], 0, "Dòng điện cảm ứng chỉ sinh ra khi số đường sức từ qua tiết diện cuộn dây kín biến thiên."),
    make_mc(2, "Nhận biết", "Hiện tượng xuất hiện dòng điện cảm ứng trong cuộn dây dẫn kín được gọi là:", [
        "Hiện tượng cảm ứng điện từ",
        "Hiện tượng nhiễm điện do cọ xát",
        "Hiện tượng đoản mạch điện",
        "Hiện tượng phát quang catôt"
    ], 0, "Hiện tượng này gọi là hiện tượng cảm ứng điện từ."),
    make_mc(3, "Nhận biết", "Dòng điện xoay chiều (AC) là dòng điện có đặc điểm:", [
        "Chiều và cường độ luân phiên biến đổi theo thời gian",
        "Chiều không bao giờ thay đổi theo thời gian",
        "Cường độ luôn luôn bằng 0",
        "Chỉ chạy được trong chất lỏng"
    ], 0, "Dòng điện xoay chiều luân phiên đổi chiều theo thời gian."),
    make_mc(4, "Nhận biết", "Hai bộ phận chính của một máy phát điện xoay chiều là:", [
        "Roto (phần quay) và Stato (phần đứng yên)",
        "Vôn kế và ampe kế",
        "Bình ắc quy và khóa điện",
        "Ống nhòm và kính tiềm vọng"
    ], 0, "Máy phát điện gồm hai bộ phận chính: Roto (quay) và Stato (đứng yên)."),
    make_mc(5, "Nhận biết", "Tần số của dòng điện xoay chiều trong mạng lưới điện sinh hoạt quốc gia tại Việt Nam là:", [
        "50 Hz",
        "100 Hz",
        "60 Hz",
        "220 Hz"
    ], 0, "Tần số điện lưới quốc gia Việt Nam chuẩn là 50 Hz."),
    make_mc(6, "Nhận biết", "Dụng cụ đo hiệu điện thế và cường độ của dòng điện xoay chiều có kí hiệu quy ước trên mặt đồng hồ là:", [
        "Kí hiệu AC hoặc dấu ngã (~)",
        "Kí hiệu DC hoặc dấu gạch ngang (-)",
        "Kí hiệu dấu cộng (+)",
        "Kí hiệu chữ W"
    ], 0, "Đồng hồ đo xoay chiều ký hiệu AC hoặc dấu ~."),
    make_mc(7, "Thông hiểu", "Trường hợp nào sau đây KHÔNG làm xuất hiện dòng điện cảm ứng trong cuộn dây dẫn kín?", [
        "Để một thanh nam châm đứng yên bất động bên trong lòng cuộn dây",
        "Đưa cực Bắc của thanh nam châm lại gần cuộn dây",
        "Kéo thanh nam châm ra xa cuộn dây",
        "Quay thanh nam châm trước mặt cuộn dây"
    ], 0, "Nam châm đứng yên thì số đường sức từ không biến thiên nên không có dòng cảm ứng."),
    make_mc(8, "Thông hiểu", "Khi cho nam châm quay liên tục trước một cuộn dây dẫn kín thì trong cuộn dây xuất hiện:", [
        "Dòng điện xoay chiều",
        "Dòng điện một chiều không đổi",
        "Sóng siêu âm",
        "Tia bức xạ hồng ngoại"
    ], 0, "Số đường sức từ tăng giảm luân phiên nên sinh ra dòng điện xoay chiều."),
    make_mc(9, "Thông hiểu", "Một máy phát điện xoay chiều loại lớn trong nhà máy thủy điện thường có cấu tạo roto là:", [
        "Nam châm điện công suất lớn quay tròn",
        "Cuộn dây dẫn quay tròn có chổi quét",
        "Các tấm pin mặt trời",
        "Các bánh răng bằng gỗ"
    ], 0, "Máy phát điện công suất lớn dùng nam châm quay (roto) để tránh phải dùng chổi quét chịu dòng lớn."),
    make_mc(10, "Thông hiểu", "Khi dòng điện xoay chiều chạy qua một bóng đèn sợi đốt, hiện tượng xảy ra là:", [
        "Đèn vẫn phát sáng liên tục bình thường do dây tóc nóng sáng nhờ tác dụng nhiệt của dòng điện",
        "Đèn nhấp nháy làm mắt nhìn thấy rõ từng lần tắt bật",
        "Đèn không bao giờ sáng được",
        "Đèn bị cháy đứt tóc ngay lập tức"
    ], 0, "Dây tóc nóng sáng liên tục nhờ quán tính nhiệt, mắt không thấy nhấp nháy ở tần số 50 Hz."),
    make_mc(11, "Thông hiểu", "Trong một giây, dòng điện xoay chiều có tần số 50 Hz thực hiện đổi chiều bao nhiêu lần?", [
        "100 lần",
        "50 lần",
        "25 lần",
        "200 lần"
    ], 0, "Mỗi chu kỳ dòng điện đổi chiều 2 lần, với 50 Hz (50 chu kỳ/giây) dòng điện đổi chiều 100 lần/giây."),
    make_mc(12, "Thông hiểu", "Tác dụng nào sau đây của dòng điện xoay chiều KHÔNG phụ thuộc vào chiều của dòng điện?", [
        "Tác dụng nhiệt và tác dụng quang",
        "Tác dụng từ",
        "Tác dụng sinh học",
        "Tác dụng hóa học mạ điện"
    ], 0, "Nhiệt lượng Q = I^2.R.t không phụ thuộc chiều dòng điện, đèn sợi đốt sáng không phụ thuộc chiều.")
]

p2_b24_t1 = [
    make_tf(1, "Thông hiểu", "Về điều kiện xuất hiện hiện tượng cảm ứng điện từ:", [
        ("a", "Dòng điện cảm ứng chỉ sinh ra khi số đường sức từ xuyên qua tiết diện cuộn dây kín biến thiên.", True),
        ("b", "Đưa nam châm lại gần cuộn dây thì số đường sức từ tăng lên.", True),
        ("c", "Kéo nam châm ra xa cuộn dây thì số đường sức từ giảm đi.", True),
        ("d", "Nếu giữ cuộn dây và nam châm chuyển động cùng vận tốc theo cùng một hướng thì dòng điện cảm ứng sinh ra rất lớn.", False)
    ], "Chuyển động cùng vận tốc thì khoảng cách không đổi, số đường sức từ không biến thiên nên không có dòng cảm ứng."),
    make_tf(2, "Thông hiểu", "Về máy phát điện xoay chiều:", [
        ("a", "Máy phát điện biến đổi cơ năng thành điện năng.", True),
        ("b", "Máy phát điện công suất lớn có roto là các cuộn dây dẫn và stato là nam châm vĩnh cửu.", False),
        ("c", "Máy phát điện xe đạp (đinamô) dùng nam châm vĩnh cửu quay trước cuộn dây để thắp sáng đèn xe.", True),
        ("d", "Dòng điện sinh ra từ máy phát điện xoay chiều có chiều luân phiên thay đổi.", True)
    ], "Máy phát điện công suất lớn có roto là nam châm điện và stato là các cuộn dây dẫn."),
    make_tf(3, "Vận dụng", "Thí nghiệm với một cuộn dây dẫn kín nối với điện kế nhạy G và một thanh nam châm thẳng:", [
        ("a", "Khi ấn nhanh cực Bắc của nam châm vào cuộn dây, kim điện kế lệch sang phải.", True),
        ("b", "Khi rút nhanh nam châm ra xa cuộn dây, kim điện kế lệch sang trái.", True),
        ("c", "Khi giữ nam châm đứng yên bên trong cuộn dây, kim điện kế chỉ số 0.", True),
        ("d", "Nếu ấn nam châm vào càng chậm thì kim điện kế lệch càng nhiều.", False)
    ], "Ấn vào càng nhanh thì tốc độ biến thiên từ thông càng lớn, dòng cảm ứng sinh ra càng mạnh."),
    make_tf(4, "Vận dụng", "Một mạng điện gia đình sử dụng điện áp xoay chiều có ghi 220 V - 50 Hz:", [
        ("a", "Số 220 V là giá trị hiệu dụng của hiệu điện thế xoay chiều.", True),
        ("b", "Tần số 50 Hz cho biết dòng điện thực hiện 50 chu kỳ biến thiên trong một giây.", True),
        ("c", "Có thể dùng ampe kế một chiều (kí hiệu DC) để đo cường độ dòng điện xoay chiều này một cách chuẩn xác.", False),
        ("d", "Một bóng đèn sợi đốt cắm vào mạng điện này phát sáng bình thường.", True)
    ], "Ampe kế DC chỉ đo được dòng điện một chiều, đo dòng xoay chiều kim chỉ số 0 hoặc rung tại chỗ.")
]

p3_b24_t1 = [
    make_sa(1, "Thông hiểu", "Tần số của dòng điện xoay chiều sinh hoạt ở Việt Nam là bao nhiêu Hz?", "50", "50 Hz."),
    make_sa(2, "Thông hiểu", "Hiện tượng xuất hiện dòng điện cảm ứng khi từ thông biến thiên được phát minh bởi nhà bác học nào? (Chỉ ghi họ)", "Faraday", "Michael Faraday (1831)."),
    make_sa(3, "Vận dụng", "Trong 1 giây, dòng điện xoay chiều có tần số 60 Hz luân phiên đổi chiều bao nhiêu lần?", "120", "60 × 2 = 120 lần."),
    make_sa(4, "Vận dụng", "Một đinamô xe đạp tạo ra dòng điện xoay chiều khi bánh xe quay. Khi xe đạp đi nhanh hơn, độ sáng của đèn xe đạp tăng hay giảm?", "Tăng", "Xe đi nhanh hơn, nam châm quay nhanh hơn sinh điện áp cảm ứng lớn hơn làm đèn sáng hơn."),
    make_sa(5, "Vận dụng cao", "Roto của một máy phát điện xoay chiều có 4 cặp cực từ quay với tốc độ n = 15 vòng/giây (900 vòng/phút). Tần số f của dòng điện xoay chiều sinh ra là bao nhiêu Hz?", "60", "f = p × n = 4 × 15 = 60 Hz."),
    make_sa(6, "Vận dụng cao", "Một máy phát điện xoay chiều có roto gồm 2 cặp cực từ. Để tạo ra dòng điện xoay chiều có tần số f = 50 Hz, tốc độ quay của roto phải là bao nhiêu vòng/giây?", "25", "n = f / p = 50 / 2 = 25 vòng/giây (1500 vòng/phút).")
]

p4_b24_t1 = [
    make_vdc(1, "Bếp từ nấu ăn gia đình hoạt động dựa trên ứng dụng của hiện tượng cảm ứng điện từ: Bên dưới mặt kính bếp có một mâm dây đồng phát ra từ trường biến thiên tần số cao (khoảng 20 kHz đến 40 kHz). Khi đặt nồi lên bếp, đáy nồi phải làm bằng vật liệu gì để nấu chín thức ăn nhanh chóng?", [
        "Kim loại sắt từ (như thép hoặc inox hít nam châm) để dòng điện xoáy Foucault cảm ứng sinh nhiệt tức thì ở đáy nồi",
        "Thủy tinh cách nhiệt",
        "Đất sét gốm sứ nung",
        "Nhựa chịu nhiệt tổng hợp"
    ], 0, "Nồi kim loại sắt từ hấp thụ từ trường biến thiên sinh dòng Foucault cảm ứng mạnh làm đáy nồi tự nóng lên trực tiếp."),
    make_vdc(2, "Công nghệ sạc pin không dây chuẩn Qi trên điện thoại thông minh: Đế sạc cắm nguồn điện có chứa một cuộn dây phát, còn bên trong mặt lưng điện thoại có gắn một cuộn dây thu. Năng lượng điện truyền qua khoảng cách vài milimét không khí từ đế sạc vào pin điện thoại là nhờ:", [
        "Hiện tượng cảm ứng điện từ giữa cuộn dây phát dòng xoay chiều cao tần và cuộn dây thu",
        "Bức xạ nhiệt của bếp hồng ngoại",
        "Sóng âm thanh tần số siêu cao",
        "Tia laser chiếu thẳng vào pin"
    ], 0, "Dòng xoay chiều ở cuộn phát sinh từ trường biến thiên cảm ứng dòng điện sang cuộn thu bên trong điện thoại."),
    make_vdc(3, "Thẻ từ xe buýt thông minh (thẻ NFC hoặc thẻ RFID) không cần gắn bất kỳ thỏi pin nào bên trong nhưng khi chạm vào đầu đọc thẻ ở cửa soát vé thì đầu đọc vẫn nhận diện được dữ liệu. Nguồn năng lượng nuôi chip điện tử trong thẻ lấy từ đâu?", [
        "Ăng-ten cuộn dây trong thẻ cảm ứng điện từ từ trường phát ra từ đầu đọc thẻ, sinh dòng điện cảm ứng nuôi chip",
        "Nhiệt lượng từ ngón tay người cầm thẻ",
        "Thẻ tự tích điện từ ánh sáng phòng vé",
        "Sóng phát thanh radio xa hàng trăm kilômét"
    ], 0, "Ăng-ten trong thẻ thu năng lượng từ trường biến thiên từ đầu đọc bằng hiện tượng cảm ứng điện từ nuôi chip phát sóng đáp lại."),
    make_vdc(4, "Một máy phát điện mini gắn ở phuộc xe đạp (đinamô) có một núm xoay tì sát vào lốp xe. Khi xe chạy trên đường trời mưa trơn trượt, đèn xe đạp đôi khi bị chập chờn hoặc tối đi rõ rệt. Nguyên nhân vật lý chính của hiện tượng này là:", [
        "Nước mưa làm giảm ma sát giữa núm xoay và lốp xe gây hiện tượng trượt, làm giảm tốc độ quay của nam châm trong đinamô",
        "Nước mưa làm mất điện áp của bóng đèn",
        "Nước mưa hút hết từ trường của nam châm",
        "Dây đồng trong đinamô bị hòa tan trong nước"
    ], 0, "Mưa làm trơn trượt làm núm đinamô quay chậm hơn tốc độ bánh xe, từ thông biến thiên chậm làm điện áp phát ra giảm khiến đèn mờ.")
]

exams["phys9_c7_b24_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b24", "Bài 24: Hiện tượng cảm ứng điện từ. Dòng điện xoay chiều", 1, p1_b24_t1, p2_b24_t1, p3_b24_t1, p4_b24_t1)

# --- phys9_c7_b24_test2 ---
p1_b24_t2 = [
    make_mc(1, "Nhận biết", "Trong thí nghiệm tạo dòng điện cảm ứng, cách nào sau đây làm tăng số đường sức từ xuyên qua tiết diện cuộn dây?", [
        "Đưa cực của thanh nam châm từ ngoài lại gần cuộn dây",
        "Kéo thanh nam châm từ trong cuộn dây ra ngoài xa",
        "Để thanh nam châm đứng yên bên ngoài cuộn dây",
        "Làm nóng thanh nam châm lên 500 độ C"
    ], 0, "Đưa nam châm lại gần làm tăng số đường sức từ xuyên qua cuộn dây."),
    make_mc(2, "Nhận biết", "Dòng điện cảm ứng xuất hiện trong cuộn dây dẫn kín đổi chiều khi:", [
        "Số đường sức từ xuyên qua cuộn dây chuyển từ trạng thái đang tăng sang đang giảm (hoặc ngược lại)",
        "Giữ nguyên trạng thái đứng yên của nam châm",
        "Sơn lại vỏ cuộn dây",
        "Nối thêm điện trở phụ vào mạch"
    ], 0, "Dòng điện cảm ứng đổi chiều khi chiều biến thiên của từ thông đổi (từ tăng sang giảm hoặc ngược lại)."),
    make_mc(3, "Nhận biết", "Đinamô gắn trên xe đạp là một máy phát điện xoay chiều nhỏ, nó có cấu tạo gồm:", [
        "Một thanh nam châm vĩnh cửu gắn với trục quay và một cuộn dây cố định",
        "Một bình ắc quy chì mini",
        "Một bóng đèn pin và một công tắc",
        "Một động cơ xăng mini"
    ], 0, "Đinamô gồm nam châm vĩnh cửu quay trước cuộn dây có lõi sắt."),
    make_mc(4, "Nhận biết", "Khi máy phát điện xoay chiều hoạt động, năng lượng được chuyển hóa như thế nào?", [
        "Cơ năng chuyển hóa thành điện năng",
        "Điện năng chuyển hóa thành cơ năng",
        "Nhiệt năng chuyển hóa thành hóa năng",
        "Quang năng chuyển hóa thành cơ năng"
    ], 0, "Máy phát điện biến cơ năng thành điện năng."),
    make_mc(5, "Nhận biết", "Hiệu điện thế xoay chiều hiệu dụng được đo bằng vôn kế xoay chiều cho biết:", [
        "Giá trị tương đương với hiệu điện thế một chiều về mặt tác dụng nhiệt",
        "Giá trị lớn nhất của hiệu điện thế",
        "Giá trị tức thời tại một thời điểm",
        "Giá trị trung bình luôn bằng 0"
    ], 0, "Giá trị hiệu dụng đo bằng tác dụng nhiệt tương đương với dòng một chiều."),
    make_mc(6, "Nhận biết", "Tác dụng từ của dòng điện xoay chiều thể hiện qua hiện tượng:", [
        "Cuộn dây có dòng điện xoay chiều hút các mẩu sắt thép",
        "Dòng điện làm nóng dây dẫn",
        "Dòng điện làm sáng bóng đèn",
        "Dòng điện làm giật cơ bắp"
    ], 0, "Cuộn dây có dòng AC sinh từ trường hút sắt là tác dụng từ."),
    make_mc(7, "Thông hiểu", "Một cuộn dây dẫn kín được nối với một bóng đèn LED. Khi đưa một thanh nam châm dịch chuyển ra xa cuộn dây thì đèn LED lóe sáng. Khi dừng chuyển động của nam châm thì đèn LED:", [
        "Tắt ngay lập tức",
        "Vẫn tiếp tục sáng mãi mãi",
        "Sáng chói rực rỡ hơn",
        "Bị nổ tung"
    ], 0, "Khi dừng chuyển động, số đường sức từ ngừng biến thiên nên dòng cảm ứng biến mất, đèn tắt."),
    make_mc(8, "Thông hiểu", "Quay một thanh nam châm trước cuộn dây dẫn kín với tốc độ quay càng nhanh thì:", [
        "Dòng điện cảm ứng sinh ra trong cuộn dây có cường độ càng lớn",
        "Dòng điện cảm ứng biến mất hoàn toàn",
        "Dòng điện đổi thành dòng một chiều",
        "Cuộn dây bị nhiễm từ vĩnh viễn"
    ], 0, "Quay càng nhanh thì tốc độ biến thiên từ thông càng lớn, cường độ dòng cảm ứng càng mạnh."),
    make_mc(9, "Thông hiểu", "Tại các nhà máy thủy điện lớn (như Thủy điện Sơn La, Hòa Bình), tuabin nước quay làm bộ phận nào của máy phát điện quay theo?", [
        "Roto nam châm điện của máy phát điện",
        "Stato cuộn dây đứng yên",
        "Các đường dây tải điện 500 kV",
        "Các trạm biến áp hạ thế"
    ], 0, "Tuabin nước nối trực tiếp làm quay roto của máy phát điện xoay chiều."),
    make_mc(10, "Thông hiểu", "Khi cắm quạt điện xoay chiều vào ổ điện 220V trong nhà, động cơ quạt quay được là nhờ:", [
        "Tác dụng từ của dòng điện xoay chiều",
        "Tác dụng nhiệt nung nóng trục quạt",
        "Tác dụng phát sáng của dòng điện",
        "Tác dụng hóa học của dòng điện"
    ], 0, "Động cơ điện hoạt động dựa trên tác dụng từ của dòng điện."),
    make_mc(11, "Thông hiểu", "Một khung dây dẫn kín quay đều trong từ trường đều của một nam châm, mặt phẳng khung dây cắt các đường sức từ. Trong một vòng quay (360 độ), dòng điện cảm ứng trong khung dây đổi chiều mấy lần?", [
        "2 lần",
        "1 lần",
        "4 lần",
        "Không đổi chiều"
    ], 0, "Trong 1 vòng quay, từ thông tăng rồi giảm, dòng cảm ứng đổi chiều 2 lần."),
    make_mc(12, "Thông hiểu", "Khi sử dụng bút thử điện cắm vào một trong hai lỗ của ổ cắm điện sinh hoạt xoay chiều 220V, bóng đèn khí neon trong bút thử điện sáng lên khi cắm vào:", [
        "Dây pha (dây nóng)",
        "Dây trung tính (dây nguội)",
        "Dây tiếp địa chống sét",
        "Vỏ nhựa ổ cắm"
    ], 0, "Bút thử điện sáng khi cắm vào dây pha (dây nóng) có điện thế 220V so với đất.")
]

p2_b24_t2 = [
    make_tf(1, "Thông hiểu", "Xét hiện tượng cảm ứng điện từ khi dùng nam châm điện:", [
        ("a", "Đặt một cuộn dây thứ hai kín gần một nam châm điện có công tắc.", True),
        ("b", "Khi đóng ngắt công tắc điện của nam châm điện, trong cuộn dây thứ hai xuất hiện dòng điện cảm ứng.", True),
        ("c", "Khi giữ dòng điện trong nam châm điện ổn định không đổi, trong cuộn dây thứ hai liên tục có dòng điện cảm ứng mạnh.", False),
        ("d", "Nếu thay đổi vị trí con chạy của biến trở trong mạch nam châm điện thì cuộn dây thứ hai cũng xuất hiện dòng cảm ứng.", True)
    ], "Dòng ổn định thì từ trường không đổi, số đường sức từ qua cuộn 2 không biến thiên nên không có dòng cảm ứng."),
    make_tf(2, "Thông hiểu", "Về máy phát điện xoay chiều công nghiệp:", [
        ("a", "Roto là phần quay, stato là phần đứng yên.", True),
        ("b", "Năng lượng đầu vào có thể là cơ năng của dòng nước (thủy điện) hoặc sức gió (điện gió).", True),
        ("c", "Máy phát điện xoay chiều chỉ có thể tạo ra dòng điện một chiều không đổi.", False),
        ("d", "Dòng điện sinh ra đưa lên lưới điện truyền tải đi khắp đất nước.", True)
    ], "Máy phát điện xoay chiều tạo ra dòng điện xoay chiều AC."),
    make_tf(3, "Vận dụng", "Một vòng dây kim loại kín diện tích S đặt nằm ngang. Đưa cực Nam của một thanh nam châm rơi tự do thẳng đứng xuyên qua vòng dây:", [
        ("a", "Khi thanh nam châm rơi lại gần vòng dây, trong vòng dây xuất hiện dòng điện cảm ứng.", True),
        ("b", "Lực từ do dòng điện cảm ứng sinh ra có xu hướng chống lại chuyển động rơi của nam châm (đẩy nam châm lên).", True),
        ("c", "Gia tốc rơi của thanh nam châm khi đi qua vòng dây nhỏ hơn gia tốc trọng trường g.", True),
        ("d", "Năng lượng điện sinh ra trong vòng dây được tự sinh ra từ hư không.", False)
    ], "Theo định luật bảo toàn năng lượng, điện năng sinh ra từ sự giảm động năng của thanh nam châm."),
    make_tf(4, "Vận dụng", "Một dòng điện xoay chiều chạy qua một điện trở R = 100 Ω có hiệu điện thế hiệu dụng U = 220 V:", [
        ("a", "Cường độ dòng điện hiệu dụng chạy qua điện trở là I = 2,2 A.", True),
        ("b", "Công suất tỏa nhiệt trên điện trở là P = 484 W.", True),
        ("c", "Nhiệt lượng tỏa ra trên điện trở trong 1 phút là 29.040 J.", True),
        ("d", "Nếu mắc điện trở vào nguồn điện một chiều 220 V thì công suất tỏa nhiệt bị giảm đi một nửa.", False)
    ], "I = 220 / 100 = 2,2 A. P = U × I = 220 × 2,2 = 484 W. Q = 484 × 60 = 29.040 J. Dòng DC 220V tỏa nhiệt cùng công suất 484 W.")
]

p3_b24_t2 = [
    make_sa(1, "Thông hiểu", "Bộ phận quay trong máy phát điện xoay chiều được gọi là gì?", "Roto", "Roto là phần quay."),
    make_sa(2, "Thông hiểu", "Bộ phận đứng yên trong máy phát điện xoay chiều được gọi là gì?", "Stato", "Stato là phần đứng yên."),
    make_sa(3, "Vận dụng", "Một máy phát điện xoay chiều có 1 cặp cực từ. Roto quay với tốc độ 50 vòng/giây. Tần số dòng điện phát ra là bao nhiêu Hz?", "50", "f = p × n = 1 × 50 = 50 Hz."),
    make_sa(4, "Vận dụng", "Dòng điện xoay chiều có chu kỳ T = 0,02 giây thì tần số f bằng bao nhiêu Hz?", "50", "f = 1 / T = 1 / 0,02 = 50 Hz."),
    make_sa(5, "Vận dụng cao", "Roto của máy phát điện có 6 cặp cực từ. Để phát ra dòng điện tần số 50 Hz thì tốc độ quay của roto là bao nhiêu vòng/phút?", "500", "n = f / p = 50 / 6 vòng/s = (50 / 6) × 60 = 500 vòng/phút."),
    make_sa(6, "Vận dụng cao", "Một bóng đèn 220V - 100W cắm vào mạng điện xoay chiều 220V hoạt động trong 2 giờ. Điện năng tiêu thụ của bóng đèn là bao nhiêu kWh? (Lấy số thập phân)", "0.2", "A = P × t = 0,1 kW × 2 h = 0,2 kWh.")
]

p4_b24_t2 = [
    make_vdc(1, "Trong máy quét kim loại an ninh tại sân bay: Hành khách bước qua một cổng vòm có các cuộn dây phát từ trường biến thiên tần số cao. Nếu hành khách mang theo một con dao găm bằng sắt trong người, hiện tượng gì sẽ kích hoạt còi báo động an ninh?", [
        "Từ trường biến thiên cảm ứng dòng điện Foucault trong con dao, dòng điện này sinh từ trường phụ làm biến đổi dòng điện trong cuộn dây thu của cổng, kích hoạt chuông báo",
        "Con dao tự động hút cổng an ninh đổ sập",
        "Tia X chiếu xuyên qua làm bốc cháy con dao",
        "Con dao phát ra âm thanh còi hú"
    ], 0, "Dòng điện xoáy cảm ứng trong vật kim loại làm biến đổi từ trường cuộn thu ở cổng từ an ninh, kích hoạt chuông báo."),
    make_vdc(2, "Đèn pin lắc tay khẩn cấp (Shake Flashlight) không cần dùng pin hóa học: Bên trong thân đèn có một cuộn dây đồng và một viên nam châm đất hiếm hình trụ có thể trượt tự do dọc theo thân đèn. Khi người dùng lắc mạnh đèn qua lại theo chiều dọc, hiện tượng gì xảy ra?", [
        "Nam châm chuyển động qua lại trong cuộn dây làm từ thông biến thiên, sinh dòng điện cảm ứng sạc vào tụ điện thắp sáng bóng đèn LED",
        "Ma sát cơ học giữa nam châm và thành ống sinh nhiệt phát sáng",
        "Nam châm bị cọ xát giải phóng khí hydro gây cháy",
        "Đèn phát sáng nhờ lực hút Trái Đất"
    ], 0, "Hiện tượng cảm ứng điện từ: lắc nam châm qua cuộn dây sinh dòng điện cảm ứng nạp vào tụ điện để thắp LED."),
    make_vdc(3, "Hệ thống sạc điện không dây tốc độ cao cho xe buýt điện công cộng: Khi xe buýt dừng đỗ đón trả khách tại trạm dừng, mâm sạc từ trường âm dưới mặt đường tự động kích hoạt truyền năng lượng lên mâm thu dưới gầm xe trong 30 giây để xe chạy tiếp trạm sau. Ưu điểm nổi bật của giải pháp này là:", [
        "Không cần dây cắm sạc cồng kềnh, tránh nguy cơ giật điện trong điều kiện trời mưa ngập và sạc nhanh tự động",
        "Xe buýt không cần bánh xe vẫn chạy được",
        "Không tiêu tốn bất kỳ năng lượng điện nào của trạm",
        "Làm nhiệt độ đường ray hạ xuống dưới 0 độ C"
    ], 0, "Sạc cảm ứng từ không dây dưới lòng đường an toàn tuyệt đối khi trời mưa ngập, tự động hóa và tiện lợi cho xe công cộng."),
    make_vdc(4, "Một người làm thí nghiệm thả một thanh nam châm mạnh hình trụ rơi tự do qua một ống đồng dày đặt thẳng đứng (biết đồng không phải chất từ tính, không hút nam châm). Người đó quan sát thấy thanh nam châm rơi qua ống đồng chậm hơn rất nhiều so với khi rơi tự do ngoài không khí. Hiện tượng này là do:", [
        "Dòng điện xoáy Foucault cảm ứng sinh ra trong thành ống đồng tạo ra từ trường ngược chiều cản trở chuyển động rơi của nam châm (theo định luật Lenz)",
        "Ống đồng hút dính nam châm bằng lực từ",
        "Không khí bên trong ống đồng có áp suất cực cao giữ nam châm lại",
        "Thanh nam châm bị khử hết từ tính khi vào ống đồng"
    ], 0, "Hiện tượng đệm từ cảm ứng Foucault (định luật Lenz): Dòng cảm ứng trong thành ống sinh từ trường hãm chuyển động rơi của nam châm.")
]

exams["phys9_c7_b24_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b24", "Bài 24: Hiện tượng cảm ứng điện từ. Dòng điện xoay chiều", 2, p1_b24_t2, p2_b24_t2, p3_b24_t2, p4_b24_t2)

# --- phys9_c7_b24_test3 ---
p1_b24_t3 = [
    make_mc(1, "Nhận biết", "Dòng điện cảm ứng trong cuộn dây dẫn kín được sinh ra khi:", [
        "Số đường sức từ xuyên qua tiết diện cuộn dây tăng hoặc giảm",
        "Số đường sức từ xuyên qua cuộn dây giữ nguyên không đổi",
        "Cuộn dây bị nung nóng trên ngọn lửa",
        "Đặt cuộn dây trong phòng kín không có không khí"
    ], 0, "Dòng điện cảm ứng xuất hiện khi số đường sức từ biến thiên."),
    make_mc(2, "Nhận biết", "Trong máy phát điện xoay chiều, khung dây dẫn đứng yên và nam châm quay quanh trục. Phần đứng yên được gọi là:", [
        "Stato",
        "Roto",
        "Cổ góp",
        "Chổi quét"
    ], 0, "Phần đứng yên luôn gọi là Stato."),
    make_mc(3, "Nhận biết", "Dòng điện xoay chiều trong đời sống có tác dụng nào sau đây?", [
        "Tác dụng nhiệt, tác dụng phát sáng, tác dụng từ và tác dụng sinh học",
        "Chỉ có tác dụng phát sáng duy nhất",
        "Chỉ có tác dụng nhiệt duy nhất",
        "Không có tác dụng nào"
    ], 0, "Dòng AC có đầy đủ các tác dụng nhiệt, quang, từ, sinh học."),
    make_mc(4, "Nhận biết", "Dòng điện xoay chiều 220V chạy qua cơ thể người có thể gây nguy hiểm chết người do:", [
        "Tác dụng sinh học làm co giật cơ bắp và ngừng tim",
        "Lực đẩy tĩnh điện thổi bay người",
        "Lực từ trường hút người dính vào dây điện",
        "Tác dụng tán sắc ánh sáng"
    ], 0, "Dòng điện tác động sinh học gây co giật cơ tim nguy hiểm tính mạng."),
    make_mc(5, "Nhận biết", "Ampe kế xoay chiều mắc vào mạch điện dùng để đo:", [
        "Cường độ dòng điện hiệu dụng của dòng điện xoay chiều",
        "Cường độ dòng điện cực đại",
        "Điện trở của nguồn điện",
        "Tần số của máy phát điện"
    ], 0, "Ampe kế xoay chiều đo giá trị hiệu dụng I."),
    make_mc(6, "Nhận biết", "Chu kỳ T và tần số f của dòng điện xoay chiều liên hệ với nhau theo công thức:", [
        "T = 1 / f",
        "T = f",
        "T = f^2",
        "T = 2 × f"
    ], 0, "T = 1 / f."),
    make_mc(7, "Thông hiểu", "Một cuộn dây dẫn kín đặt cạnh một nam châm điện. Trong trường hợp nào sau đây xuất hiện dòng điện cảm ứng trong cuộn dây?", [
        "Khi điều chỉnh con chạy của biến trở làm thay đổi cường độ dòng điện trong nam châm điện",
        "Khi nam châm điện hoạt động với dòng điện một chiều ổn định",
        "Khi ngắt hoàn toàn nguồn điện của nam châm điện và để yên",
        "Khi đặt hai cuộn dây song song cách xa nhau 10 mét"
    ], 0, "Thay đổi con chạy làm biến thiên cường độ dòng điện, từ trường biến thiên sinh dòng cảm ứng."),
    make_mc(8, "Thông hiểu", "Nếu đưa một thanh nam châm vào trong lòng một cuộn dây dẫn hở (hai đầu cuộn dây không nối với nhau) thì:", [
        "Hai đầu cuộn dây xuất hiện một hiệu điện thế cảm ứng nhưng không có dòng điện chạy trong mạch",
        "Vẫn có dòng điện cảm ứng rất mạnh chạy qua",
        "Thanh nam châm bị nóng chảy",
        "Cuộn dây tự động nối kín mạch lại"
    ], 0, "Mạch hở nên chỉ có suất điện động cảm ứng (hiệu điện thế cảm ứng) giữa 2 đầu mà không có dòng điện."),
    make_mc(9, "Thông hiểu", "Một khung dây quay đều trong từ trường, khi mặt phẳng khung dây ở vị trí song song với các đường sức từ thì số đường sức từ xuyên qua tiết diện khung dây bằng:", [
        "Bằng 0",
        "Đạt giá trị cực đại",
        "Bằng một nửa giá trị cực đại",
        "Bằng vô cực"
    ], 0, "Khi mặt phẳng khung song song đường sức từ thì không có đường sức từ nào đâm xuyên qua tiết diện: số đường sức từ bằng 0."),
    make_mc(10, "Thông hiểu", "Khi cắm một chiếc bàn là vào mạng điện xoay chiều 220V, bàn là nóng lên nhanh chóng là nhờ:", [
        "Tác dụng nhiệt của dòng điện xoay chiều qua dây điện trở mayso",
        "Tác dụng từ của dòng điện",
        "Tác dụng phát sáng của đèn LED báo",
        "Tác dụng hóa học"
    ], 0, "Tác dụng nhiệt của dòng điện làm nóng dây mayso truyền nhiệt ra mặt bàn là."),
    make_mc(11, "Thông hiểu", "Một máy phát điện gió quay tuabin biến đổi trực tiếp dạng năng lượng nào thành điện năng?", [
        "Động năng của luồng gió",
        "Năng lượng hóa học của không khí",
        "Nhiệt năng của mặt trời",
        "Thế năng hấp dẫn của gió"
    ], 0, "Động năng của gió làm quay tuabin máy phát điện biến thành điện năng."),
    make_mc(12, "Thông hiểu", "Để đo hiệu điện thế giữa hai lỗ cắm của ổ điện gia đình, ta phải chọn núm xoay của đồng hồ vạn năng ở chế độ:", [
        "ACV (đo hiệu điện thế xoay chiều) ở thang đo lớn hơn 220V (ví dụ thang 250V hoặc 750V)",
        "DCV thang đo 10V",
        "DCA thang đo 10A",
        "Thang đo điện trở Ôm"
    ], 0, "Phải chọn thang ACV lớn hơn 220V để đo điện áp lưới an toàn và chính xác.")
]

p2_b24_t3 = [
    make_tf(1, "Thông hiểu", "Về các phương pháp tạo ra dòng điện cảm ứng:", [
        ("a", "Quay nam châm trước một cuộn dây dẫn kín tạo ra dòng điện cảm ứng.", True),
        ("b", "Quay cuộn dây dẫn kín trong từ trường tạo ra dòng điện cảm ứng.", True),
        ("c", "Đặt nam châm nằm yên bên trong cuộn dây kín tạo ra dòng điện cảm ứng liên tục.", False),
        ("d", "Cho nam châm điện chạy bằng dòng điện xoay chiều đặt gần cuộn dây kín sinh ra dòng điện cảm ứng trong cuộn dây.", True)
    ], "Nam châm đứng yên không làm biến thiên từ thông nên không có dòng cảm ứng."),
    make_tf(2, "Thông hiểu", "Về tác dụng của dòng điện xoay chiều:", [
        ("a", "Dòng điện xoay chiều có tác dụng nhiệt như dòng điện một chiều.", True),
        ("b", "Dòng điện xoay chiều không thể làm phát sáng bóng đèn huỳnh quang.", False),
        ("c", "Dòng điện xoay chiều chạy qua nam châm điện làm cực từ đổi chiều liên tục.", True),
        ("d", "Dòng điện xoay chiều có thể gây nguy hiểm giật điện nếu chạm vào dây nóng.", True)
    ], "Dòng điện xoay chiều thắp sáng bóng đèn huỳnh quang và đèn sợi đốt rất tốt."),
    make_tf(3, "Vận dụng", "Một nam châm thẳng rơi từ trên cao xuống xuyên qua một vòng nhôm kín treo bằng sợi chỉ mềm:", [
        ("a", "Khi nam châm rơi lại gần vòng nhôm, vòng nhôm bị đẩy lệch ra xa.", True),
        ("b", "Khi nam châm vừa chui qua khỏi vòng nhôm và rơi ra xa, vòng nhôm bị hút theo nam châm.", True),
        ("c", "Các hiện tượng trên tuân theo định luật Lenz về chiều dòng điện cảm ứng.", True),
        ("d", "Nếu vòng nhôm bị xẻ rãnh hở mạch thì lực tương tác giữa nam châm và vòng nhôm càng mạnh hơn.", False)
    ], "Vòng nhôm xẻ rãnh hở mạch thì không có dòng điện kín chạy qua nên lực từ tương tác bằng 0."),
    make_tf(4, "Vận dụng", "Một ấm điện xoay chiều công suất 1000 W được cắm vào hiệu điện thế 220 V trong thời gian 10 phút:", [
        ("a", "Cường độ dòng điện hiệu dụng qua ấm xấp xỉ bằng 4,55 A.", True),
        ("b", "Năng lượng điện tiêu thụ trong 10 phút là 600.000 J (600 kJ).", True),
        ("c", "Năng lượng điện tiêu thụ tương đương với 0,167 kWh.", True),
        ("d", "Nếu cắm ấm vào nguồn điện một chiều 110 V thì công suất của ấm vẫn bằng 1000 W.", False)
    ], "I = 1000 / 220 ≈ 4,55 A. A = 1000 × 600 = 600.000 J = 0,167 kWh. Cắm vào 110V thì công suất giảm 4 lần còn 250 W.")
]

p3_b24_t3 = [
    make_sa(1, "Thông hiểu", "Điều kiện để xuất hiện dòng điện cảm ứng trong cuộn dây dẫn kín là số đường sức từ qua tiết diện cuộn dây phải làm sao?", "Biến thiên", "Phải biến thiên (tăng lên hoặc giảm đi)."),
    make_sa(2, "Thông hiểu", "Kí hiệu chữ cái viết tắt của dòng điện xoay chiều là gì?", "AC", "AC (Alternating Current)."),
    make_sa(3, "Vận dụng", "Dòng điện xoay chiều có tần số f = 50 Hz thì chu kỳ T bằng bao nhiêu giây? (Lấy số thập phân)", "0.02", "T = 1 / f = 1 / 50 = 0,02 s."),
    make_sa(4, "Vận dụng", "Một máy phát điện xoay chiều có 2 cặp cực từ. Roto quay với tốc độ 30 vòng/giây. Tần số dòng điện phát ra là bao nhiêu Hz?", "60", "f = 2 × 30 = 60 Hz."),
    make_sa(5, "Vận dụng cao", "Roto máy phát điện có 10 cặp cực từ quay với tốc độ n = 300 vòng/phút. Tần số dòng điện xoay chiều sinh ra bằng bao nhiêu Hz?", "50", "n = 300 / 60 = 5 vòng/s. f = p × n = 10 × 5 = 50 Hz."),
    make_sa(6, "Vận dụng cao", "Một máy giặt tiêu thụ công suất 500 W cắm vào mạng điện 220 V trong 3 giờ. Điện năng máy giặt tiêu thụ là bao nhiêu kWh?", "1.5", "A = 0,5 kW × 3 h = 1,5 kWh.")
]

p4_b24_t3 = [
    make_vdc(1, "Công nghệ sạc thông minh cho xe ô tô điện trên đường cao tốc (Electrified Highway): Một tuyến đường thử nghiệm được gắn các cuộn dây điện phát từ trường xoay chiều ngầm dưới mặt đường. Khi xe ô tô điện gắn cuộn dây thu chạy qua phía trên với tốc độ 100 km/h, xe vừa chạy vừa được nạp điện liên tục mà không cần dừng lại cắm sạc. Hiện tượng vật lý cốt lõi ứng dụng ở đây là:", [
        "Hiện tượng cảm ứng điện từ truyền năng lượng không dây qua từ trường biến thiên cộng hưởng",
        "Hiện tượng tĩnh điện ma sát giữa lốp xe và mặt đường",
        "Hiện tượng phản xạ toàn phần ánh sáng",
        "Hiện tượng phóng điện hồ quang sấm sét"
    ], 0, "Hệ thống truyền điện không dây động (Dynamic Wireless Power Transfer - DWPT) dựa trên cảm ứng điện từ cộng hưởng từ trường."),
    make_vdc(2, "Microphone điện động (Dynamic Mic) dùng cho ca sĩ biểu diễn trên sân khấu: Khi ca sĩ cất tiếng hát, sóng âm thanh làm màng rung gắn cuộn dây nhỏ dao động trong khe từ trường của một nam châm vĩnh cửu. Tín hiệu âm thanh được chuyển hóa thành tín hiệu điện là nhờ:", [
        "Hiện tượng cảm ứng điện từ sinh ra dòng điện cảm ứng biến thiên cùng tần số với giọng hát trong cuộn dây",
        "Sóng âm thanh biến thành nhiệt làm nóng dây",
        "Ca sĩ truyền điện tích từ cơ thể vào micro",
        "Tia laser bên trong micro thu nhận âm thanh"
    ], 0, "Cuộn âm dao động trong từ trường làm biến thiên từ thông sinh dòng điện cảm ứng âm tần."),
    make_vdc(3, "Đồng hồ đo tốc độ xe đạp điện tử (Speedometer gắn nan hoa): Người ta gắn một mẩu nam châm nhỏ lên nan hoa bánh xe và một cảm biến cuộn dây nhỏ cố định trên càng xe. Mỗi lần bánh xe quay được 1 vòng, nam châm quét qua cuộn dây sinh ra một xung điện cảm ứng. Bộ xử lý vi mạch dựa vào đâu để tính ra vận tốc xe?", [
        "Đếm tần số các xung điện cảm ứng theo thời gian và nhân với chu vi chu vi vòng tròn của bánh xe",
        "Đo nhiệt độ của nan hoa bánh xe",
        "Đo khối lượng của nam châm",
        "Đo lực cản không khí đập vào bánh xe"
    ], 0, "Tần số xung điện cho biết số vòng quay trong một giây, nhân chu vi bánh xe ra tốc độ di chuyển v = 2.pi.R.f."),
    make_vdc(4, "Một kỹ sư chế tạo một máy bay không người lái (Flycam) có thể hạ cánh sạc pin tự động không tiếp xúc: Trên chân đáp của flycam có gắn cuộn dây thu, khi đỗ lên bàn sạc phát từ trường xoay chiều 100 kHz, dòng điện cảm ứng xoay chiều được nắn thành dòng một chiều nạp vào pin Lithium. Hiệu suất truyền năng lượng không dây phụ thuộc lớn nhất vào yếu tố nào?", [
        "Khoảng cách và sự đồng trục căn chỉnh thẳng hàng giữa cuộn dây phát và cuộn dây thu",
        "Màu sơn vỏ ngoài của flycam",
        "Độ cao của flycam so với mực nước biển",
        "Dung lượng thẻ nhớ máy ảnh"
    ], 0, "Khoảng cách càng nhỏ và hai cuộn dây càng đồng trục thì hệ số ghép từ thông càng cao, hiệu suất truyền năng lượng cảm ứng càng lớn.")
]

exams["phys9_c7_b24_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b24", "Bài 24: Hiện tượng cảm ứng điện từ. Dòng điện xoay chiều", 3, p1_b24_t3, p2_b24_t3, p3_b24_t3, p4_b24_t3)

print("Added phys9_c7_b24 (3 tests).")
