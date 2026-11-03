# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 27: SỰ BẢO TOÀN VÀ CHUYỂN HÓA NĂNG LƯỢNG
Bao gồm 3 đề thi độc lập 100%: phys9_c8_b27_test1, phys9_c8_b27_test2, phys9_c8_b27_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c8"
CH_TITLE = "Chương VIII: Năng lượng và sự biến đổi năng lượng"

# =============================================================================
# BÀI 27: SỰ BẢO TOÀN VÀ CHUYỂN HÓA NĂNG LƯỢNG (3 ĐỀ)
# =============================================================================

# --- phys9_c8_b27_test1 ---
p1_b27_t1 = [
    make_mc(1, "Nhận biết", "Định luật bảo toàn và chuyển hóa năng lượng khẳng định rằng: Năng lượng:", [
        "Không tự sinh ra cũng không tự mất đi, chỉ chuyển hóa từ dạng này sang dạng khác hoặc truyền từ vật này sang vật khác",
        "Tự sinh ra thêm khi vật chuyển động với tốc độ cao",
        "Mất dần hoàn toàn biến mất khỏi vũ trụ theo thời gian",
        "Chỉ có thể tồn tại vĩnh viễn dưới dạng cơ năng"
    ], 0, "Định luật bảo toàn và chuyển hóa năng lượng."),
    make_mc(2, "Nhận biết", "Khi một chiếc quạt điện đang quay bình thường, điện năng tiêu thụ chủ yếu được chuyển hóa thành:", [
        "Cơ năng làm quay cánh quạt (có ích) và một phần nhiệt năng làm nóng động cơ (hao phí)",
        "Quang năng chiếu sáng",
        "Hóa năng tích lũy trong quạt",
        "Năng lượng hạt nhân nguyên tử"
    ], 0, "Điện năng chuyển thành cơ năng có ích và nhiệt năng hao phí."),
    make_mc(3, "Nhận biết", "Hiệu suất H của một quá trình chuyển hóa năng lượng được tính bằng công thức:", [
        "H = (Năng lượng có ích / Năng lượng toàn phần) × 100%",
        "H = (Năng lượng hao phí / Năng lượng toàn phần) × 100%",
        "H = Năng lượng có ích + Năng lượng hao phí",
        "H = Năng lượng toàn phần / Năng lượng có ích"
    ], 0, "H = (A_có_ích / A_toàn_phần) × 100%."),
    make_mc(4, "Nhận biết", "Trong mọi quá trình chuyển hóa năng lượng trong thực tế đời sống, năng lượng hao phí thường xuất hiện dưới dạng:", [
        "Nhiệt năng tỏa ra môi trường xung quanh do ma sát hoặc điện trở",
        "Năng lượng hạt nhân",
        "Năng lượng hấp dẫn",
        "Năng lượng hóa học vĩnh cửu"
    ], 0, "Năng lượng hao phí chủ yếu là nhiệt năng tỏa ra môi trường do ma sát."),
    make_mc(5, "Nhận biết", "Khi nạp pin cho điện thoại thông minh, năng lượng điện từ củ sạc được chuyển hóa chủ yếu thành:", [
        "Hóa năng tích trữ trong các hợp chất hóa học của pin",
        "Cơ năng làm rung máy",
        "Quang năng màn hình",
        "Nhiệt năng làm nóng pin"
    ], 0, "Điện năng chuyển thành hóa năng tích trữ trong pin Lithium."),
    make_mc(6, "Nhận biết", "Một động cơ vĩnh cửu có thể tự hoạt động liên tục và sinh công mãi mãi mà không cần cung cấp bất kỳ năng lượng nào từ bên ngoài là:", [
        "Hoàn toàn không thể chế tạo được vì vi phạm định luật bảo toàn năng lượng",
        "Rất dễ chế tạo bằng cách dùng nam châm vĩnh cửu",
        "Đã được chế tạo thành công trong các phòng thí nghiệm",
        "Có thể mua được ngoài thị trường"
    ], 0, "Động cơ vĩnh cửu loại 1 vi phạm định luật bảo toàn năng lượng nên không thể tồn tại."),
    make_mc(7, "Thông hiểu", "Một bóng đèn LED tiêu thụ 10 J điện năng và phát ra 8 J năng lượng ánh sáng. Hiệu suất phát quang của bóng đèn LED này là:", [
        "80%",
        "20%",
        "100%",
        "125%"
    ], 0, "H = (8 / 10) × 100% = 80%."),
    make_mc(8, "Thông hiểu", "Khi một chiếc xe máy chạy trên đường trường, năng lượng hóa thạch từ xăng bị tiêu hao phần lớn vào việc:", [
        "Tỏa nhiệt làm nóng động cơ xe, két nước làm mát và thải nhiệt ra ngoài khí quyển theo ống pô",
        "Làm phát sáng đèn pha",
        "Sạc điện cho bình ắc quy",
        "Tạo tiếng còi xe"
    ], 0, "Động cơ đốt trong có hiệu suất thấp (~25-30%), 70-75% năng lượng xăng thất thoát dưới dạng nhiệt xả ra môi trường."),
    make_mc(9, "Thông hiểu", "Tại sao hiệu suất của bất kỳ động cơ nhiệt hoặc máy móc nào trong thực tế đều KHÔNG THỂ đạt 100%?", [
        "Vì luôn luôn có một phần năng lượng bị hao phí do ma sát giữa các bộ phận cơ học và tỏa nhiệt ra môi trường",
        "Vì định luật bảo toàn năng lượng bị sai lệch",
        "Vì kim loại chế tạo máy quá nhẹ",
        "Vì dòng điện chạy quá nhanh"
    ], 0, "Ma sát cơ học và tỏa nhiệt không thể triệt tiêu hoàn toàn nên hiệu suất luôn < 100%."),
    make_mc(10, "Thông hiểu", "Một quả bóng cao su được thả rơi tự do từ độ cao 2 m xuống sàn nhà bê tông. Sau khi nảy lên, quả bóng chỉ đạt độ cao 1,5 m. Cơ năng của quả bóng đã không được bảo toàn vì:", [
        "Một phần cơ năng đã chuyển hóa thành nhiệt năng làm nóng quả bóng, mặt sàn và năng lượng âm thanh khi va chạm",
        "Trọng lực của Trái Đất bị mất đi",
        "Không khí đã hút sạch năng lượng của quả bóng",
        "Khối lượng quả bóng bị giảm đi một nửa"
    ], 0, "Va chạm không đàn hồi làm biến đổi một phần cơ năng thành nhiệt năng và âm thanh."),
    make_mc(11, "Thông hiểu", "Thiết bị điện gia dụng nào sau đây có hiệu suất chuyển hóa điện năng thành nhiệt năng có ích đạt xấp xỉ cao nhất (gần 95 - 98%)?", [
        "Ấm đun nước siêu tốc ngâm sợi đốt trong nước",
        "Bóng đèn sợi đốt chiếu sáng",
        "Máy hút bụi cầm tay",
        "Quạt máy để bàn"
    ], 0, "Ấm siêu tốc có dây mayso ngập trực tiếp trong nước nên hầu như toàn bộ nhiệt lượng truyền thẳng vào nước, hiệu suất đạt ~95-98%."),
    make_mc(12, "Thông hiểu", "Trên các thiết bị điện tử gia dụng (như tủ lạnh, điều hòa không khí) thường dán 'Nhãn năng lượng' có từ 1 sao đến 5 sao của Bộ Công Thương. Ý nghĩa của thiết bị đạt mức 5 sao là:", [
        "Thiết bị có hiệu suất năng lượng cao nhất, tiết kiệm điện năng nhất trong cùng chủng loại",
        "Thiết bị có giá bán đắt nhất",
        "Thiết bị nặng nhất",
        "Thiết bị tạo ra tiếng ồn lớn nhất"
    ], 0, "Nhãn năng lượng 5 sao biểu thị cấp hiệu suất năng lượng tối ưu, tiết kiệm điện nhất.")
]

p2_b27_t1 = [
    make_tf(1, "Thông hiểu", "Về định luật bảo toàn và chuyển hóa năng lượng:", [
        ("a", "Tổng năng lượng của một hệ cô lập hoàn toàn luôn được bảo toàn.", True),
        ("b", "Năng lượng có thể tự biến mất mà không để lại bất kỳ dấu vết nào.", False),
        ("c", "Năng lượng có thể truyền từ vật này sang vật khác dưới dạng thực hiện công hoặc truyền nhiệt.", True),
        ("d", "Trong mọi quá trình biến đổi năng lượng, năng lượng toàn phần luôn bằng năng lượng có ích cộng năng lượng hao phí.", True)
    ], "Năng lượng không bao giờ tự mất đi, chỉ chuyển hóa sang dạng khác hoặc phân tán vào môi trường."),
    make_tf(2, "Thông hiểu", "Về hiệu suất của các thiết bị biến đổi năng lượng:", [
        ("a", "Hiệu suất của một máy móc thực tế luôn nhỏ hơn 100%.", True),
        ("b", "Máy móc càng hiện đại thì năng lượng hao phí càng được giảm thiểu tối đa.", True),
        ("c", "Có thể chế tạo được một động cơ cơ học có hiệu suất đạt 120%.", False),
        ("d", "Bóng đèn LED có hiệu suất phát quang cao hơn nhiều so với bóng đèn sợi đốt.", True)
    ], "Hiệu suất không bao giờ vượt quá 100% (vi phạm định luật bảo toàn năng lượng)."),
    make_tf(3, "Vận dụng", "Một động cơ điện kéo một thang máy tải hàng có trọng lượng 4000 N lên cao 10 m trong thời gian 20 giây. Điện năng toàn phần mà động cơ tiêu thụ trong thời gian này là 50.000 J (50 kJ):", [
        ("a", "Công có ích để nâng tải hàng lên cao là 40.000 J (40 kJ).", True),
        ("b", "Năng lượng hao phí do tỏa nhiệt và ma sát là 10.000 J (10 kJ).", True),
        ("c", "Hiệu suất của động cơ thang máy đạt 80%.", True),
        ("d", "Công suất toàn phần của động cơ là 5.000 W.", False)
    ], "A_ích = P × h = 4000 × 10 = 40.000 J. H = 40.000 / 50.000 = 80%. P_tp = A_tp / t = 50.000 / 20 = 2500 W (không phải 5000 W)."),
    make_tf(4, "Vận dụng", "Một bình nóng lạnh cắm điện tiêu thụ 2 kWh điện năng và đun nóng một lượng nước thu được nhiệt lượng có ích là 6,48 MJ (biết 1 kWh = 3,6 MJ):", [
        ("a", "Điện năng toàn phần tiêu thụ là 7,2 MJ.", True),
        ("b", "Nhiệt lượng hao phí tỏa ra môi trường xung quanh là 0,72 MJ.", True),
        ("c", "Hiệu suất đun nước của bình nóng lạnh đạt 90%.", True),
        ("d", "Toàn bộ 2 kWh điện năng đã biến mất không để lại dấu tích nhiệt nào.", False)
    ], "A_tp = 2 × 3,6 = 7,2 MJ. A_hp = 7,2 - 6,48 = 0,72 MJ. H = 6,48 / 7,2 = 90%.")
]

p3_b27_t1 = [
    make_sa(1, "Thông hiểu", "Một quá trình chuyển hóa năng lượng có năng lượng toàn phần là 100 J, năng lượng có ích là 75 J. Hiệu suất H bằng bao nhiêu %?", "75", "H = 75 / 100 = 75%."),
    make_sa(2, "Thông hiểu", "Động cơ vĩnh cửu có thể chế tạo được trong thực tế không? (Trả lời: Có hoặc Không)", "Không", "Không thể chế tạo được động cơ vĩnh cửu."),
    make_sa(3, "Vận dụng", "Một bóng đèn sợi đốt tiêu thụ 100 J điện năng nhưng chỉ phát ra 5 J quang năng. Hiệu suất phát quang của đèn sợi đốt là bao nhiêu %?", "5", "H = 5 / 100 = 5%."),
    make_sa(4, "Vận dụng", "Một động cơ điện tiêu thụ 1000 J điện năng sinh ra công có ích 850 J. Năng lượng hao phí tỏa nhiệt là bao nhiêu Jun?", "150", "A_hp = 1000 - 850 = 150 J."),
    make_sa(5, "Vận dụng cao", "Một máy bơm nước có công suất định mức 800 W hoạt động với hiệu suất 75%. Công suất có ích để bơm nước lên cao là bao nhiêu Watt?", "600", "P_ích = 800 × 75% = 600 W."),
    make_sa(6, "Vận dụng cao", "Một cần cẩu nâng một khối bê tông có trọng lượng P = 6000 N lên cao 5 m trong 10 giây. Động cơ tiêu thụ công suất điện 4000 W. Hiệu suất của cần cẩu là bao nhiêu %?", "75", "A_ích = 6000 × 5 = 30.000 J. A_tp = 4000 × 10 = 40.000 J. H = 30.000 / 40.000 = 75%.")
]

p4_b27_t1 = [
    make_vdc(1, "So sánh hiệu suất sử dụng năng lượng giữa xe ô tô điện (EV) và xe ô tô chạy xăng truyền thống: Xe điện đạt hiệu suất chuyển đổi năng lượng từ pin ra bánh xe lên tới 85 - 90%, trong khi xe chạy xăng hiệu suất động cơ đốt trong chỉ đạt khoảng 20 - 25%. Nguyên nhân căn bản dẫn đến sự chênh lệch hiệu suất khổng lồ này là:", [
        "Động cơ đốt trong bị thất thoát từ 75% đến 80% năng lượng dưới dạng nhiệt lượng tỏa ra két nước làm mát và khí thải xả nóng ra môi trường, trong khi động cơ điện tổn thất nhiệt rất nhỏ",
        "Xe điện chạy chậm hơn xe xăng gấp mười lần",
        "Xăng dầu không chứa năng lượng hóa học",
        "Xe điện không phải chịu lực cản ma sát mặt đường"
    ], 0, "Động cơ nhiệt bị giới hạn bởi chu trình nhiệt Carnot, thất thoát phần lớn nhiệt ra két nước và khí xả; động cơ điện biến trực tiếp điện thành cơ năng với tổn thất cực nhỏ."),
    make_vdc(2, "Một người muốn làm mát căn phòng ngủ bằng cách mở toang cánh cửa của chiếc tủ lạnh đang cắm điện hoạt động trong phòng kín. Sau vài giờ, nhiệt độ trung bình của không khí trong phòng kín sẽ thay đổi như thế nào?", [
        "Nhiệt độ phòng tăng lên vì động cơ máy nén tủ lạnh tiêu thụ điện năng và tỏa thêm nhiệt ra không khí trong phòng lớn hơn nhiệt lượng hấp thụ từ buồng lạnh",
        "Nhiệt độ phòng giảm xuống lạnh buốt như trong ngăn đá",
        "Nhiệt độ phòng hoàn toàn không thay đổi",
        "Nhiệt độ phòng hạ xuống dưới 0 độ C"
    ], 0, "Tủ lạnh lấy nhiệt trong buồng phả ra giàn nóng phía sau. Khi mở cửa, buồng lạnh và giàn nóng cùng trong phòng, cộng thêm điện năng tiêu thụ chuyển thành nhiệt làm phòng nóng lên."),
    make_vdc(3, "Công nghệ thu hồi năng lượng nhiệt thải (Waste Heat Recovery) trong các nhà máy xi măng và luyện kim: Người ta lắp đặt hệ thống nồi hơi tận dụng nhiệt của dòng khí xả nóng 400 độ C để tạo hơi nước quay tuabin phát điện cấp lại cho nhà máy. Ý nghĩa công nghệ và kinh tế của giải pháp này là:", [
        "Biến năng lượng hao phí vô ích thành điện năng có ích, nâng cao hiệu suất tổng thể của nhà máy và giảm chi phí tiền điện hàng tỷ đồng mỗi năm",
        "Làm tăng nhiệt độ khí xả lên mức sôi",
        "Loại bỏ hoàn toàn bụi xi măng",
        "Làm nguội các sản phẩm thép"
    ], 0, "Thu hồi nhiệt khí thải phát điện giúp tái chế năng lượng hao phí, tối ưu hóa hiệu suất nhiệt của toàn bộ dây chuyền sản xuất."),
    make_vdc(4, "Một vận động viên thể thao tiêu thụ thức ăn cung cấp năng lượng 2500 kcal mỗi ngày (khoảng 10,5 MJ). Cơ thể người chuyển hóa năng lượng này thành công cơ học chạy nhảy (hiệu suất cơ thể khoảng 20%) và nhiệt lượng tỏa ra duy trì thân nhiệt 37 độ C. Nhiệt lượng mà cơ thể vận động viên này tỏa ra môi trường trong một ngày là:", [
        "8,4 MJ (8400 kJ)",
        "2,1 MJ",
        "10,5 MJ",
        "0 MJ"
    ], 0, "Năng lượng hao phí nhiệt = 10,5 MJ × (100% - 20%) = 10,5 × 80% = 8,4 MJ.")
]

exams["phys9_c8_b27_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c8_b27", "Bài 27: Sự bảo toàn và chuyển hóa năng lượng", 1, p1_b27_t1, p2_b27_t1, p3_b27_t1, p4_b27_t1)

# --- phys9_c8_b27_test2 ---
p1_b27_t2 = [
    make_mc(1, "Nhận biết", "Trong một chu trình chuyển hóa năng lượng, phần năng lượng đáp ứng đúng mục đích sử dụng ban đầu được gọi là:", [
        "Năng lượng có ích",
        "Năng lượng hao phí",
        "Năng lượng toàn phần",
        "Năng lượng thất thoát"
    ], 0, "Năng lượng phục vụ đúng mục đích gọi là năng lượng có ích."),
    make_mc(2, "Nhận biết", "Phần năng lượng sinh ra ngoài ý muốn của con người trong quá trình vận hành thiết bị được gọi là:", [
        "Năng lượng hao phí",
        "Năng lượng có ích",
        "Năng lượng hữu dụng",
        "Công có ích"
    ], 0, "Năng lượng sinh ra ngoài ý muốn là năng lượng hao phí."),
    make_mc(3, "Nhận biết", "Khi bật bóng đèn sợi đốt, mục đích sử dụng chính là để chiếu sáng. Dạng năng lượng có ích ở đây là:", [
        "Quang năng (năng lượng ánh sáng)",
        "Nhiệt năng làm nóng bóng đèn",
        "Cơ năng làm rung dây tóc",
        "Hóa năng trong bóng đèn"
    ], 0, "Quang năng là năng lượng có ích cho mục đích chiếu sáng."),
    make_mc(4, "Nhận biết", "Khi cắm máy khoan điện cầm tay để khoan tường, năng lượng có ích là:", [
        "Cơ năng của mũi khoan quay tròn",
        "Nhiệt năng làm nóng mô tơ máy khoan",
        "Âm thanh tiếng rít chói tai",
        "Tia lửa điện ở chổi than"
    ], 0, "Cơ năng quay mũi khoan là năng lượng có ích."),
    make_mc(5, "Nhận biết", "Tỉ số giữa năng lượng có ích và năng lượng toàn phần được gọi là:", [
        "Hiệu suất",
        "Công suất",
        "Điện trở",
        "Nhiệt dung riêng"
    ], 0, "Tỉ số giữa A_ích và A_tp là hiệu suất H."),
    make_mc(6, "Nhận biết", "Định luật bảo toàn năng lượng nghiệm đúng cho:", [
        "Tất cả các hiện tượng tự nhiên và mọi quá trình chuyển hóa năng lượng",
        "Chỉ riêng các hiện tượng cơ học",
        "Chỉ riêng các hiện tượng nhiệt học",
        "Chỉ riêng trong phòng thí nghiệm"
    ], 0, "Định luật bảo toàn năng lượng là định luật phổ quát của toàn bộ vũ trụ."),
    make_mc(7, "Thông hiểu", "Một động cơ điện tiêu thụ 500 J điện năng và sinh ra 400 J cơ năng có ích. Năng lượng hao phí tỏa ra môi trường là:", [
        "100 J",
        "900 J",
        "500 J",
        "400 J"
    ], 0, "A_hp = A_tp - A_ích = 500 - 400 = 100 J."),
    make_mc(8, "Thông hiểu", "Một bếp gas tiêu thụ lượng gas có năng lượng 10.000 J để đun nước nhưng nước chỉ nhận được 6.000 J nhiệt lượng. Hiệu suất của bếp gas là:", [
        "60%",
        "40%",
        "100%",
        "160%"
    ], 0, "H = (6000 / 10.000) × 100% = 60%."),
    make_mc(9, "Thông hiểu", "Khi phanh xe đạp gấp trên đường nhựa, xe dừng lại và lốp xe bị nóng lên. Cơ năng của xe đạp đã chuyển hóa thành:", [
        "Nhiệt năng làm nóng lốp xe và mặt đường",
        "Hóa năng của cao su",
        "Điện năng nạp vào đèn xe",
        "Quang năng chiếu sáng"
    ], 0, "Ma sát chuyển hóa cơ năng thành nhiệt năng làm nóng lốp và mặt đường."),
    make_mc(10, "Thông hiểu", "Trong các loại đèn chiếu sáng gia đình hiện nay, loại đèn nào có hiệu suất phát quang cao nhất và tiết kiệm điện nhất?", [
        "Đèn LED công nghệ bán dẫn",
        "Đèn sợi đốt dây tóc vonfram",
        "Đèn dầu hỏa truyền thống",
        "Đèn cầy nến sáp"
    ], 0, "Đèn LED có hiệu suất phát quang cao nhất (lên tới 80-90%), tỏa rất ít nhiệt."),
    make_mc(11, "Thông hiểu", "Khi thả một hòn bi sắt rơi từ đỉnh dốc nghiêng xuống chân dốc, dạng năng lượng nào đã chuyển hóa thành động năng của hòn bi?", [
        "Thế năng trọng trường của hòn bi",
        "Hóa năng của sắt",
        "Nhiệt năng của không khí",
        "Năng lượng hạt nhân"
    ], 0, "Thế năng ở đỉnh dốc chuyển hóa thành động năng ở chân dốc."),
    make_mc(12, "Thông hiểu", "Biện pháp nào sau đây giúp nâng cao hiệu suất hoạt động của các máy móc cơ khí?", [
        "Thường xuyên tra dầu mỡ bôi trơn các trục xoay và vòng bi để giảm ma sát",
        "Tăng tải trọng lên vượt quá công suất định mức",
        "Để máy móc ngoài trời mưa ẩm ướt",
        "Chạy máy ở tốc độ quá tải liên tục"
    ], 0, "Bôi trơn dầu mỡ giảm ma sát, giảm hao phí nhiệt, tăng hiệu suất máy móc.")
]

p2_b27_t2 = [
    make_tf(1, "Thông hiểu", "Xét các quá trình chuyển hóa năng lượng trong thiết bị gia đình:", [
        ("a", "Bàn là điện biến đổi điện năng thành nhiệt năng.", True),
        ("b", "Nồi cơm điện chuyển hóa điện năng thành nhiệt năng để nấu chín cơm.", True),
        ("c", "Máy giặt biến đổi điện năng thành hóa năng để tẩy sạch quần áo.", False),
        ("d", "Máy bơm nước biến đổi điện năng thành cơ năng đẩy nước lên cao.", True)
    ], "Máy giặt biến điện năng thành cơ năng quay lồng giặt (bột giặt mới thực hiện phản ứng hóa học)."),
    make_tf(2, "Thông hiểu", "Về định luật bảo toàn năng lượng và hiệu suất:", [
        ("a", "Năng lượng có thể tự mất đi vĩnh viễn nếu máy móc bị hư hỏng.", False),
        ("b", "Hiệu suất của một quá trình luôn bằng tỉ số giữa công có ích và công toàn phần.", True),
        ("c", "Năng lượng hao phí không biến mất mà truyền vào môi trường xung quanh.", True),
        ("d", "Giảm năng lượng hao phí giúp nâng cao hiệu suất của thiết bị.", True)
    ], "Năng lượng không tự mất đi, chỉ biến thành nhiệt tỏa ra môi trường."),
    make_tf(3, "Vận dụng", "Một ấm đun nước điện công suất 1500 W đun sôi 2 lít nước trong thời gian 8 phút (480 giây). Nhiệt lượng cần thiết để làm sôi nước là 648.000 J (648 kJ):", [
        ("a", "Điện năng toàn phần ấm tiêu thụ trong 8 phút là 720.000 J (720 kJ).", True),
        ("b", "Nhiệt lượng hao phí tỏa ra vỏ ấm và không khí là 72.000 J.", True),
        ("c", "Hiệu suất đun nước của ấm điện đạt 90%.", True),
        ("d", "Nếu bọc thêm lớp bông thủy tinh cách nhiệt quanh thân ấm thì hiệu suất đun sẽ giảm đi.", False)
    ], "A_tp = 1500 × 480 = 720.000 J. A_hp = 720.000 - 648.000 = 72.000 J. H = 648 / 720 = 90%. Cách nhiệt thân ấm giúp giảm thất thoát nhiệt, tăng hiệu suất."),
    make_tf(4, "Vận dụng", "Một ắc quy ô tô nạp điện với điện năng tiêu thụ 1,2 kWh. Khi phóng điện sử dụng, ắc quy cung cấp năng lượng có ích là 0,96 kWh:", [
        ("a", "Quá trình nạp biến điện năng thành hóa năng tích trữ.", True),
        ("b", "Năng lượng hao phí dưới dạng nhiệt tỏa ra khi nạp và xả là 0,24 kWh.", True),
        ("c", "Hiệu suất nạp xả của ắc quy là 80%.", True),
        ("d", "Ắc quy có thể hoạt động mãi mãi mà không bao giờ bị chai pin.", False)
    ], "H = 0,96 / 1,2 = 80%. Pin và ắc quy bị thoái hóa vật liệu sau nhiều chu kỳ nạp xả.")
]

p3_b27_t2 = [
    make_sa(1, "Thông hiểu", "Khi quả táo từ trên cành rơi xuống đất, thế năng của quả táo chuyển hóa thành dạng cơ năng nào?", "Động năng", "Thế năng chuyển thành động năng."),
    make_sa(2, "Thông hiểu", "Hiệu suất của một động cơ cơ học trong thực tế có thể bằng 100% không? (Trả lời: Có hoặc Không)", "Không", "Không thể bằng 100% do có ma sát."),
    make_sa(3, "Vận dụng", "Một động cơ điện tiêu thụ 2000 J điện năng và sinh ra 1600 J cơ năng có ích. Hiệu suất của động cơ là bao nhiêu %?", "80", "H = (1600 / 2000) × 100% = 80%."),
    make_sa(4, "Vận dụng", "Một bóng đèn compact tiêu thụ 20 J điện năng mỗi giây và phát ra 5 J năng lượng ánh sáng. Hiệu suất phát quang là bao nhiêu %?", "25", "H = (5 / 20) × 100% = 25%."),
    make_sa(5, "Vận dụng cao", "Một máy xúc đất thực hiện công có ích 150 kJ trong khi động cơ diesel tiêu hao năng lượng hóa học 500 kJ. Hiệu suất của máy xúc là bao nhiêu %?", "30", "H = (150 / 500) × 100% = 30%."),
    make_sa(6, "Vận dụng cao", "Một động cơ điện có công suất 1000 W hoạt động với hiệu suất 85%. Công suất hao phí tỏa nhiệt của động cơ là bao nhiêu Watt?", "150", "P_hp = 1000 × (100% - 85%) = 1000 × 15% = 150 W.")
]

p4_b27_t2 = [
    make_vdc(1, "Động cơ đốt trong ô tô Hybrid (kết hợp xăng và điện) tự động tắt máy xăng khi xe dừng đèn đỏ và sử dụng mô tơ điện khởi động êm ái khi xuất phát. Vào lúc phanh giảm tốc, động cơ điện hoạt động như máy phát nạp điện ngược lại vào pin. Ưu điểm nổi bật về mặt bảo toàn năng lượng của xe Hybrid là:", [
        "Thu hồi cơ năng hao phí khi phanh và tối ưu hóa vùng hoạt động hiệu suất cao của động cơ xăng, giúp tiết kiệm từ 30% đến 40% lượng nhiên liệu tiêu thụ",
        "Xe không cần đổ xăng vẫn chạy được mãi mãi",
        "Làm tăng khối lượng xe lên gấp mười lần",
        "Khử hoàn toàn trọng lực của xe"
    ], 0, "Xe Hybrid tái thu hồi động năng khi phanh và tắt máy khi dừng chờ, triệt tiêu hao phí nổ máy không tải và tối ưu hiệu suất động cơ."),
    make_vdc(2, "Bình giữ nhiệt chân không (phích nước nóng inox cao cấp) có thể giữ nước sôi nóng ấm suốt 24 giờ mà không cần cắm điện là nhờ:", [
        "Cấu tạo vỏ hai lớp kim loại với lớp chân không ở giữa triệt tiêu truyền nhiệt dẫn nhiệt và đối lưu, kết hợp lớp tráng bạc phản xạ bức xạ nhiệt trở lại",
        "Bình tự sinh ra năng lượng nhiệt bên trong ruột",
        "Bình chứa than đá âm ỉ bên trong",
        "Bình hấp thụ sóng điện từ xung quanh"
    ], 0, "Lớp chân không ngăn dẫn nhiệt và đối lưu, mặt tráng gương ngăn bức xạ nhiệt, khóa chặt nhiệt năng không cho thất thoát."),
    make_vdc(3, "Công nghệ sấy thăng hoa thực phẩm (Freeze Drying): Thực phẩm đông lạnh được đưa vào buồng chân không, nước đá thăng hoa trực tiếp từ thể rắn sang thể hơi mà không qua thể lỏng. Quá trình thăng hoa này đòi hỏi cung cấp nhiệt lượng thăng hoa. Năng lượng cung cấp được sử dụng để:", [
        "Phá vỡ liên kết giữa các phân tử nước đá ở thể rắn chuyển thẳng thành thể hơi, giữ nguyên vẹn cấu trúc tế bào và vitamin của thực phẩm",
        "Làm chín nhừ thực phẩm",
        "Đốt cháy lớp vỏ ngoài của thực phẩm",
        "Làm thực phẩm đông cứng thành kim loại"
    ], 0, "Nhiệt thăng hoa cung cấp năng lượng bẻ gãy liên kết tinh thể đá trong chân không, sấy khô thực phẩm mà không làm biến tính chất dinh dưỡng."),
    make_vdc(4, "Một máy điều hòa không khí Inverter có công suất làm lạnh 9000 BTU (tương đương công suất nhiệt 2640 W) chỉ tiêu thụ công suất điện năng 800 W. Tỉ số giữa công suất nhiệt làm lạnh và công suất điện tiêu thụ (hệ số COP) đạt tới 3,3 (tức 330%). Điều này có vi phạm định luật bảo toàn năng lượng không? Tại sao?", [
        "Hoàn toàn không vi phạm, vì máy điều hòa không tự sinh ra nhiệt mà là một máy bơm nhiệt dùng 800 W điện để 'bơm' 2640 W nhiệt lượng từ trong phòng phả ra ngoài trời",
        "Có vi phạm, vì hiệu suất không thể vượt quá 100%",
        "Vi phạm vì máy điều hòa là động cơ vĩnh cửu",
        "Do đồng hồ đo điện bị sai lệch"
    ], 0, "Máy điều hòa là máy bơm nhiệt (Heat Pump), điện năng chỉ dùng để chạy máy nén vận chuyển nhiệt từ nơi lạnh sang nơi nóng, hệ số hiệu quả COP > 1 hoàn toàn tuân theo định luật nhiệt động lực học.")
]

exams["phys9_c8_b27_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c8_b27", "Bài 27: Sự bảo toàn và chuyển hóa năng lượng", 2, p1_b27_t2, p2_b27_t2, p3_b27_t2, p4_b27_t2)

# --- phys9_c8_b27_test3 ---
p1_b27_t3 = [
    make_mc(1, "Nhận biết", "Phát biểu nào sau đây diễn đạt ĐÚNG định luật bảo toàn và chuyển hóa năng lượng?", [
        "Năng lượng không tự sinh ra cũng không tự mất đi, chỉ biến đổi từ dạng này sang dạng khác hoặc truyền từ vật này sang vật khác",
        "Năng lượng tự sinh ra khi đốt cháy nhiên liệu",
        "Năng lượng bị tiêu diệt hoàn toàn khi sinh công cơ học",
        "Năng lượng chỉ bảo toàn đối với dòng điện một chiều"
    ], 0, "Định luật bảo toàn và chuyển hóa năng lượng."),
    make_mc(2, "Nhận biết", "Trong một thiết bị cơ khí đang hoạt động, năng lượng toàn phần cung cấp cho máy luôn bằng:", [
        "Tổng của năng lượng có ích và năng lượng hao phí",
        "Hiệu của năng lượng có ích trừ đi năng lượng hao phí",
        "Tích của năng lượng có ích và năng lượng hao phí",
        "Bằng hai lần năng lượng có ích"
    ], 0, "A_toàn_phần = A_có_ích + A_hao_phí."),
    make_mc(3, "Nhận biết", "Khi nồi cơm điện nấu cơm, dạng năng lượng có ích là:", [
        "Nhiệt năng làm nóng xoong cơm để nấu chín gạo",
        "Quang năng của đèn báo màu đỏ",
        "Âm thanh tiếng 'tách' khi nhảy nấc",
        "Nhiệt năng thất thoát qua nắp nồi"
    ], 0, "Nhiệt năng làm nóng xoong nấu chín cơm là năng lượng có ích."),
    make_mc(4, "Nhận biết", "Khi ô tô chạy trên đường, dạng năng lượng có ích là:", [
        "Cơ năng làm quay bánh xe đẩy ô tô chuyển động",
        "Nhiệt năng khí thải xả ra ngoài",
        "Tiếng gầm rú của động cơ",
        "Nhiệt năng làm nóng lốp xe"
    ], 0, "Cơ năng đẩy xe chạy là năng lượng có ích."),
    make_mc(5, "Nhận biết", "Hiệu suất của một động cơ luôn thoả mãn điều kiện:", [
        "H < 100% (hoặc H ≤ 1)",
        "H > 100%",
        "H = 200%",
        "H luôn bằng 0"
    ], 0, "Hiệu suất máy móc thực tế luôn nhỏ hơn 100%."),
    make_mc(6, "Nhận biết", "Chế tạo động cơ vĩnh cửu là điều không thể thực hiện được vì:", [
        "Vi phạm các định luật nhiệt động lực học và định luật bảo toàn năng lượng",
        "Kim loại sắt thép quá nặng",
        "Trái Đất có từ trường",
        "Không khí quá lạnh"
    ], 0, "Động cơ vĩnh cửu vi phạm định luật bảo toàn năng lượng nên không thể chế tạo được."),
    make_mc(7, "Thông hiểu", "Một động cơ điện tiêu thụ 1000 J điện năng sinh ra 700 J cơ năng có ích. Hiệu suất của động cơ là:", [
        "70%",
        "30%",
        "100%",
        "143%"
    ], 0, "H = (700 / 1000) × 100% = 70%."),
    make_mc(8, "Thông hiểu", "Một bình nóng lạnh tiêu thụ 1 kWh điện năng và chuyển hóa thành 0,85 kWh nhiệt lượng làm nóng nước. Năng lượng hao phí là:", [
        "0,15 kWh",
        "0,85 kWh",
        "1,85 kWh",
        "0 kWh"
    ], 0, "A_hp = 1 - 0,85 = 0,15 kWh."),
    make_mc(9, "Thông hiểu", "Khi chiếc máy tính xách tay (laptop) hoạt động lâu, quạt tản nhiệt thổi ra luồng khí nóng. Luồng khí nóng này đại diện cho:", [
        "Nhiệt năng hao phí sinh ra do dòng điện chạy qua các vi mạch bán dẫn",
        "Năng lượng có ích giúp máy chạy nhanh hơn",
        "Quang năng màn hình",
        "Hóa năng của pin"
    ], 0, "Nhiệt năng tỏa ra trên vi mạch là năng lượng hao phí cần quạt tản nhiệt làm mát."),
    make_mc(10, "Thông hiểu", "Khi một quả lắc đồng hồ dao động trong không khí, biên độ dao động của nó giảm dần rồi dừng lại. Cơ năng của con lắc đã chuyển hóa thành:", [
        "Nhiệt năng làm nóng con lắc và các phần tử không khí xung quanh",
        "Hóa năng tích lũy trong con lắc",
        "Quang năng phát sáng",
        "Điện năng"
    ], 0, "Ma sát với không khí làm cơ năng chuyển hóa dần thành nhiệt năng tỏa vào môi trường."),
    make_mc(11, "Thông hiểu", "Công nghệ động cơ Inverter (biến tần) trong máy giặt và tủ lạnh giúp tiết kiệm điện năng là nhờ:", [
        "Tự động điều chỉnh linh hoạt tốc độ quay của động cơ theo tải thực tế, tránh đóng ngắt liên tục gây tổn thất năng lượng khởi động",
        "Cắt đứt dòng điện chạy qua máy giặt",
        "Làm tăng nhiệt độ phòng",
        "Tạo ra dòng điện miễn phí"
    ], 0, "Inverter điều khiển biến tần linh hoạt tốc độ động cơ theo tải thực tế, giảm tổn thất khởi động và tối ưu hóa tiêu thụ điện."),
    make_mc(12, "Thông hiểu", "Thao tác nào sau đây giúp tiết kiệm điện năng khi sử dụng điều hòa nhiệt độ vào mùa hè?", [
        "Cài đặt nhiệt độ phòng ở mức hợp lý từ 26 đến 28 độ C và kết hợp bật quạt gió thoang thoảng",
        "Cài đặt nhiệt độ ở mức 16 độ C liên tục suốt ngày đêm",
        "Mở toang cửa sổ phòng khi bật điều hòa",
        "Tắt bật điều hòa liên tục 5 phút một lần"
    ], 0, "Để 26-28°C kết hợp quạt gió vừa mát dịu vừa tiết kiệm điện năng tối đa.")
]

p2_b27_t3 = [
    make_tf(1, "Thông hiểu", "Về các dạng năng lượng và định luật bảo toàn:", [
        ("a", "Nhiệt năng có thể chuyển hóa hoàn toàn thành cơ năng mà không cần nguồn lạnh.", False),
        ("b", "Cơ năng có thể chuyển hóa hoàn toàn thành nhiệt năng thông qua lực ma sát.", True),
        ("c", "Điện năng có thể chuyển hóa thành quang năng, cơ năng, nhiệt năng và hóa năng.", True),
        ("d", "Trong một hệ kín cô lập, tổng cơ năng và nội năng của hệ là đại lượng không đổi.", True)
    ], "Theo nguyên lý II nhiệt động lực học, nhiệt năng không thể chuyển hóa 100% thành công mà không gây biến đổi môi trường xung quanh."),
    make_tf(2, "Thông hiểu", "Về việc tiết kiệm năng lượng và hiệu quả năng lượng:", [
        ("a", "Tiết kiệm năng lượng giúp giảm chi phí sinh hoạt cho gia đình.", True),
        ("b", "Sử dụng thiết bị dán nhãn năng lượng 5 sao giúp giảm phát thải khí nhà kính.", True),
        ("c", "Để thiết bị điện ở chế độ chờ (Standby) suốt nhiều tháng hoàn toàn không tốn chút điện nào.", False),
        ("d", "Bảo dưỡng định kỳ máy móc giúp duy trì hiệu suất làm việc cao.", True)
    ], "Chế độ chờ (Standby) của TV, lò vi sóng, máy tính vẫn tiêu thụ một lượng điện rò rỉ liên tục."),
    make_tf(3, "Vận dụng", "Một xe ô tô điện có bộ pin 60 kWh. Khi sạc đầy từ nguồn điện lưới với hiệu suất sạc 90%:", [
        ("a", "Lượng điện năng lưới phải cung cấp để sạc đầy pin là 66,7 kWh.", True),
        ("b", "Năng lượng hao phí nhiệt tỏa ra trên bộ sạc là 6,7 kWh.", True),
        ("c", "Bộ pin tích trữ 60 kWh dưới dạng hóa năng.", True),
        ("d", "Khi xe chạy hết 60 kWh điện thì không cần nạp lại xe vẫn chạy được 1000 km nữa.", False)
    ], "A_lưới = 60 / 90% ≈ 66,7 kWh. A_hp = 6,7 kWh. Hết pin thì xe dừng lại bắt buộc phải sạc tiếp."),
    make_tf(4, "Vận dụng", "Một động cơ điện tiêu thụ công suất 2000 W nâng một vật nặng 300 kg lên cao 8 m trong thời gian 15 giây (lấy g = 10 m/s2):", [
        ("a", "Trọng lượng của vật nặng là 3000 N.", True),
        ("b", "Công có ích để nâng vật là 24.000 J (24 kJ).", True),
        ("c", "Điện năng toàn phần động cơ tiêu thụ là 30.000 J (30 kJ).", True),
        ("d", "Hiệu suất của động cơ nâng này là 85%.", False)
    ], "P = 300 × 10 = 3000 N. A_ích = 3000 × 8 = 24.000 J. A_tp = 2000 × 15 = 30.000 J. H = 24.000 / 30.000 = 80% (không phải 85%).")
]

p3_b27_t3 = [
    make_sa(1, "Thông hiểu", "Tổng năng lượng toàn phần trừ đi năng lượng có ích bằng năng lượng gì?", "Hao phí", "Năng lượng hao phí."),
    make_sa(2, "Thông hiểu", "Động cơ điện biến đổi điện năng thành dạng năng lượng có ích nào?", "Cơ năng", "Cơ năng."),
    make_sa(3, "Vận dụng", "Một động cơ điện tiêu thụ 5000 J điện năng sinh ra công có ích 4250 J. Hiệu suất của động cơ là bao nhiêu %?", "85", "H = (4250 / 5000) × 100% = 85%."),
    make_sa(4, "Vận dụng", "Một bóng đèn tiêu thụ 50 J điện năng mỗi giây và tỏa ra 40 J nhiệt lượng hao phí. Năng lượng ánh sáng có ích phát ra là bao nhiêu Jun?", "10", "A_ích = 50 - 40 = 10 J."),
    make_sa(5, "Vận dụng cao", "Một máy kéo có công suất 10 kW hoạt động với hiệu suất 70%. Công suất có ích của máy kéo là bao nhiêu kW?", "7", "P_ích = 10 × 70% = 7 kW."),
    make_sa(6, "Vận dụng cao", "Một động cơ nâng tiêu thụ 12.000 J điện năng để nâng vật nặng 500 N lên cao 18 m. Hiệu suất nâng của động cơ là bao nhiêu %?", "75", "A_ích = 500 × 18 = 9000 J. H = (9000 / 12.000) × 100% = 75%.")
]

p4_b27_t3 = [
    make_vdc(1, "Nguyên lý bảo tồn nhiệt trong thiết kế nhà thụ động (Passive House) tại các vùng khí hậu lạnh: Ngôi nhà được xây dựng với tường dày cách nhiệt siêu cấp, cửa sổ kính 3 lớp chân không và hệ thống thông gió thu hồi nhiệt (HRV). Hệ thống HRV thu hồi tới 90% nhiệt lượng từ không khí ấm thải ra để sưởi ấm luồng không khí tươi mát hút vào. Ý nghĩa của giải pháp này là:", [
        "Giảm tới 80 - 90% nhu cầu tiêu thụ năng lượng sưởi ấm mùa đông, giữ nhiệt độ trong nhà luôn ấm áp ổn định mà tiêu tốn cực kỳ ít điện năng",
        "Làm nhà không cần có mái",
        "Làm mất hoàn toàn không khí trong nhà",
        "Biến nhà thành tủ đông lạnh"
    ], 0, "Thu hồi nhiệt thông gió HRV giữ lại 90% nhiệt năng trong nhà, giảm chi phí sưởi ấm mùa đông xuống mức tối thiểu."),
    make_vdc(2, "Một nhà máy luyện nhôm điện phân tiêu thụ dòng điện khổng lồ hàng trăm nghìn Ampe để biến oxit nhôm (Al2O3) nóng chảy thành nhôm kim loại. Quá trình điện phân này là sự chuyển hóa năng lượng từ:", [
        "Điện năng thành hóa năng tích trữ trong liên kết kim loại nhôm nguyên chất và nhiệt năng tỏa ra lò",
        "Cơ năng thành quang năng",
        "Năng lượng hạt nhân thành điện năng",
        "Thế năng thành động năng"
    ], 0, "Điện phân nhôm biến điện năng thành hóa năng bẻ gãy liên kết Al-O và nhiệt năng tỏa ra bể điện phân."),
    make_vdc(3, "Bình xịt hơi cay tự vệ hoặc bình xịt bọt tuyết chữa cháy: Khi bấm van xịt khí nén, thân bình kim loại lập tức bị lạnh buốt và có thể đóng một lớp băng mỏng ngoài vỏ bình. Hiện tượng vỏ bình bị lạnh đi nhanh chóng là do:", [
        "Khí nén giãn nở đoạn nhiệt sinh công cơ học đẩy chất xịt ra ngoài làm nội năng của khối khí giảm mạnh, kéo theo nhiệt độ hạ xuống",
        "Bình xịt tự hút đá tuyết ngoài môi trường vào trong",
        "Có phản ứng cháy xảy ra trong bình",
        "Lớp sơn ngoài vỏ bình hấp thụ nhiệt độ nóng"
    ], 0, "Khí nén giãn nở đoạn nhiệt nhanh sinh công đẩy chất xịt làm giảm nội năng (ΔU = -A < 0), nhiệt độ khối khí hạ xuống làm vỏ bình lạnh buốt."),
    make_vdc(4, "Một cần trục điện hoạt động với công suất định mức 15 kW. Khi nâng tải trọng nặng 2000 kg lên cao 12 m hết thời gian 20 giây (lấy g = 10 m/s2). Hiệu suất thực tế của cần trục điện này là:", [
        "80%",
        "75%",
        "85%",
        "90%"
    ], 0, "A_ích = m × g × h = 2000 × 10 × 12 = 240.000 J. A_tp = P × t = 15.000 × 20 = 300.000 J. H = 240.000 / 300.000 = 80%.")
]

exams["phys9_c8_b27_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c8_b27", "Bài 27: Sự bảo toàn và chuyển hóa năng lượng", 3, p1_b27_t3, p2_b27_t3, p3_b27_t3, p4_b27_t3)

print("Added phys9_c8_b27 (3 tests).")
