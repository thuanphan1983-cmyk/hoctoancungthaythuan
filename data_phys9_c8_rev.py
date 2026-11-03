# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG VIII: NĂNG LƯỢNG VÀ SỰ BIẾN ĐỔI NĂNG LƯỢNG
Bao gồm 5 đề thi độc lập 100%: phys9_c8_rev_test1 đến phys9_c8_rev_test5
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c8"
CH_TITLE = "Chương VIII: Năng lượng và sự biến đổi năng lượng"
L_ID = "phys9_c8_rev"
L_NAME = "[Đề tổng hợp] Ôn tập cuối Chương VIII"

# =============================================================================
# phys9_c8_rev_test1
# =============================================================================
p1_rev_t1 = [
    make_mc(1, "Nhận biết", "Định luật bảo toàn năng lượng khẳng định rằng trong một hệ kín:", [
        "Tổng năng lượng toàn phần luôn được bảo toàn",
        "Năng lượng tự sinh ra khi vật nóng lên",
        "Năng lượng mất dần theo thời gian",
        "Cơ năng luôn luôn tăng dần"
    ], 0, "Tổng năng lượng trong hệ kín được bảo toàn."),
    make_mc(2, "Nhận biết", "Nguồn năng lượng nào sau đây là nguồn năng lượng tái tạo?", [
        "Năng lượng mặt trời, năng lượng gió, năng lượng sinh khối",
        "Than đá khai thác mỏ",
        "Dầu mỏ dưới lòng biển",
        "Khí tự nhiên hóa lỏng"
    ], 0, "Mặt trời, gió, sinh khối là năng lượng tái tạo."),
    make_mc(3, "Nhận biết", "Nhiên liệu nào sau đây là nhiên liệu hóa thạch không thể tái tạo?", [
        "Than đá, dầu mỏ, khí đốt thiên nhiên",
        "Năng lượng sóng biển",
        "Năng lượng địa nhiệt",
        "Năng lượng thủy triều"
    ], 0, "Than đá, dầu mỏ, khí đốt là nhiên liệu hóa thạch."),
    make_mc(4, "Nhận biết", "Công thức tính hiệu suất H của một quá trình biến đổi năng lượng là:", [
        "H = (Năng lượng có ích / Năng lượng toàn phần) × 100%",
        "H = (Năng lượng hao phí / Năng lượng toàn phần) × 100%",
        "H = Năng lượng có ích + Năng lượng hao phí",
        "H = Năng lượng toàn phần / Năng lượng có ích"
    ], 0, "H = (A_ích / A_tp) × 100%."),
    make_mc(5, "Nhận biết", "Nguồn gốc ban đầu của hầu hết các dạng năng lượng trên Trái Đất là từ:", [
        "Năng lượng bức xạ của Mặt Trời",
        "Năng lượng phóng xạ lõi Trái Đất",
        "Lực hút thủy triều Mặt Trăng",
        "Gió bão không gian"
    ], 0, "Mặt Trời là cội nguồn của hầu hết năng lượng trên Trái Đất."),
    make_mc(6, "Nhận biết", "Trong nhà máy thủy điện, thế năng của dòng nước được chuyển hóa thành:", [
        "Cơ năng quay tuabin rồi thành điện năng",
        "Hóa năng tích lũy",
        "Năng lượng hạt nhân",
        "Quang năng chiếu sáng"
    ], 0, "Thế năng chuyển thành cơ năng quay tuabin rồi thành điện năng."),
    make_mc(7, "Thông hiểu", "Khi quạt điện hoạt động, điện năng tiêu thụ chủ yếu được chuyển hóa thành:", [
        "Cơ năng của cánh quạt quay và một phần nhiệt năng hao phí",
        "Quang năng",
        "Hóa năng",
        "Năng lượng hạt nhân"
    ], 0, "Cơ năng có ích và nhiệt năng hao phí."),
    make_mc(8, "Thông hiểu", "Một bóng đèn LED tiêu thụ 100 J điện năng và phát ra 85 J năng lượng ánh sáng. Hiệu suất của đèn LED là:", [
        "85%",
        "15%",
        "100%",
        "50%"
    ], 0, "H = 85 / 100 = 85%."),
    make_mc(9, "Thông hiểu", "Việc đốt quá nhiều nhiên liệu hóa thạch gây ra hậu quả môi trường nguy hiểm nhất là:", [
        "Phát thải khí CO2 gây hiệu ứng nhà kính làm biến đổi khí hậu toàn cầu",
        "Làm Trái Đất quay chậm lại",
        "Làm cạn kiệt tầng ozone vũ trụ",
        "Làm tăng lượng mưa đá"
    ], 0, "Phát thải CO2 gây hiệu ứng nhà kính và biến đổi khí hậu."),
    make_mc(10, "Thông hiểu", "Pin mặt trời (quang điện) chuyển hóa trực tiếp năng lượng ánh sáng thành:", [
        "Điện năng",
        "Hóa năng",
        "Cơ năng",
        "Năng lượng âm thanh"
    ], 0, "Chuyển quang năng thành điện năng trực tiếp."),
    make_mc(11, "Thông hiểu", "Biện pháp sử dụng năng lượng tiết kiệm và hiệu quả trong gia đình là:", [
        "Tắt thiết bị điện khi không sử dụng, tận dụng ánh sáng tự nhiên, dùng đèn LED",
        "Bật đèn suốt ngày đêm",
        "Mở cửa phòng khi đang bật điều hòa",
        "Để tủ lạnh mở toang"
    ], 0, "Tắt điện khi không dùng và dùng thiết bị hiệu suất cao."),
    make_mc(12, "Thông hiểu", "Tại sao không thể chế tạo được động cơ vĩnh cửu hoạt động mãi mãi không cần cấp năng lượng?", [
        "Vì vi phạm định luật bảo toàn năng lượng và luôn có ma sát tỏa nhiệt hao phí",
        "Vì kim loại chế tạo máy quá nhẹ",
        "Vì điện tích quá nhỏ",
        "Vì Trái Đất quay tròn"
    ], 0, "Động cơ vĩnh cửu vi phạm định luật bảo toàn năng lượng nên không thể tồn tại.")
]

p2_rev_t1 = [
    make_tf(1, "Thông hiểu", "Về định luật bảo toàn và chuyển hóa năng lượng:", [
        ("a", "Năng lượng toàn phần của một hệ kín luôn luôn được bảo toàn.", True),
        ("b", "Trong mọi quá trình chuyển hóa năng lượng, luôn có một phần năng lượng bị hao phí.", True),
        ("c", "Hiệu suất của bất kì động cơ cơ học nào trong thực tế đều không thể vượt quá 100%.", True),
        ("d", "Có thể chế tạo được một động cơ vĩnh cửu tự chạy mãi mãi không tốn năng lượng.", False)
    ], "Động cơ vĩnh cửu vi phạm định luật bảo toàn năng lượng."),
    make_tf(2, "Thông hiểu", "Về năng lượng tái tạo và phát triển bền vững:", [
        ("a", "Năng lượng gió và năng lượng mặt trời là nguồn năng lượng sạch không phát thải khí nhà kính.", True),
        ("b", "Việt Nam có bờ biển dài giàu tiềm năng phát triển điện gió ngoài khơi.", True),
        ("c", "Nhiên liệu hóa thạch là nguồn tài nguyên vô tận không bao giờ cạn kiệt.", False),
        ("d", "Năng lượng sinh khối tận dụng phụ phẩm nông nghiệp như rơm rạ, bã mía.", True)
    ], "Nhiên liệu hóa thạch là hữu hạn và sẽ cạn kiệt."),
    make_tf(3, "Vận dụng", "Một động cơ điện tiêu thụ công suất 2 kW và nâng một vật nặng có trọng lượng 1500 N lên cao 10 m trong thời gian 10 giây:", [
        ("a", "Điện năng toàn phần tiêu thụ trong 10 giây là 20.000 J (20 kJ).", True),
        ("b", "Công có ích để nâng vật lên cao là 15.000 J (15 kJ).", True),
        ("c", "Năng lượng hao phí do tỏa nhiệt và ma sát là 5.000 J (5 kJ).", True),
        ("d", "Hiệu suất của động cơ điện là 80%.", False)
    ], "A_tp = 2000 × 10 = 20.000 J. A_ích = 1500 × 10 = 15.000 J. H = 15.000 / 20.000 = 75% (không phải 80%)."),
    make_tf(4, "Vận dụng", "Một nhà máy nhiệt điện đốt than có hiệu suất 35%:", [
        ("a", "35% năng lượng từ đốt than được chuyển hóa thành điện năng có ích.", True),
        ("b", "65% năng lượng bị thất thoát dưới dạng nhiệt tỏa ra môi trường và khí xả.", True),
        ("c", "Đốt than phát thải lượng lớn khí CO2 và bụi mịn.", True),
        ("d", "Nhiệt điện than là nguồn năng lượng tái tạo thân thiện môi trường nhất.", False)
    ], "Nhiệt điện than phát thải CO2 lớn và ô nhiễm môi trường, không phải năng lượng tái tạo.")
]

p3_rev_t1 = [
    make_sa(1, "Thông hiểu", "Năng lượng mặt trời là nguồn năng lượng tái tạo hay không tái tạo?", "Tái tạo", "Năng lượng tái tạo."),
    make_sa(2, "Thông hiểu", "Động cơ vĩnh cửu có thể chế tạo được trong thực tế không? (Trả lời: Có hoặc Không)", "Không", "Không thể chế tạo được."),
    make_sa(3, "Vận dụng", "Một bóng đèn sợi đốt tiêu thụ 100 J điện năng nhưng chỉ phát ra 5 J năng lượng ánh sáng. Hiệu suất phát quang của bóng đèn là bao nhiêu %?", "5", "5 / 100 = 5%."),
    make_sa(4, "Vận dụng", "Một tấm pin mặt trời nhận được 2000 J năng lượng ánh sáng và sinh ra 400 J điện năng. Hiệu suất của pin mặt trời là bao nhiêu %?", "20", "400 / 2000 = 20%."),
    make_sa(5, "Vận dụng cao", "Một máy bơm nước có công suất 750 W hoạt động với hiệu suất 80%. Công suất có ích để bơm nước lên cao là bao nhiêu Watt?", "600", "750 × 80% = 600 W."),
    make_sa(6, "Vận dụng cao", "Một nhà máy thủy điện có cột nước cao 50 m. Lưu lượng nước qua tuabin là 20.000 kg/s. Lấy g = 10 m/s2, hiệu suất nhà máy là 85%. Công suất phát điện của nhà máy là bao nhiêu MW? (Lấy số thập phân)", "8.5", "P_tp = 20.000 × 10 × 50 = 10 MW. P_ích = 10 × 85% = 8,5 MW.")
]

p4_rev_t1 = [
    make_vdc(1, "Cam kết của Việt Nam tại Hội nghị biến đổi khí hậu COP26 đạt mức phát thải ròng bằng '0' (Net Zero) vào năm 2050 đòi hỏi chiến lược chuyển dịch năng lượng trọng tâm là:", [
        "Chuyển dịch mạnh mẽ từ nhiệt điện than sang phát triển điện gió ngoài khơi, điện mặt trời và năng lượng hydro xanh",
        "Đốt than đá nhiều hơn",
        "Ngừng phát triển kinh tế đất nước",
        "Nhập khẩu toàn bộ điện năng từ nước ngoài"
    ], 0, "Chuyển dịch sang năng lượng tái tạo và hydro xanh để đạt Net Zero 2050."),
    make_vdc(2, "Xe ô tô điện (EV) có hiệu suất sử dụng năng lượng từ pin đến bánh xe đạt tới 85 - 90%, trong khi xe chạy xăng truyền thống hiệu suất động cơ đốt trong chỉ đạt khoảng 20 - 25%. Sự chênh lệch hiệu suất lớn này là do xe chạy xăng:", [
        "Bị thất thoát tới 75 - 80% năng lượng dưới dạng nhiệt lượng tỏa ra két nước làm mát và khí xả nóng",
        "Xe điện không dùng pin",
        "Xe xăng chạy nhanh hơn",
        "Xe điện không chịu lực ma sát"
    ], 0, "Động cơ đốt trong thất thoát phần lớn nhiệt ra két nước và khí xả."),
    make_vdc(3, "Ngôi nhà năng lượng số không (Net Zero Energy House) là mô hình nhà ở thông minh:", [
        "Tự sản xuất đủ lượng điện năng từ pin mặt trời trên mái bằng hoặc lớn hơn lượng điện tiêu thụ trong suốt cả năm",
        "Không dùng bóng đèn chiếu sáng",
        "Không có cửa sổ",
        "Nhà bằng tre nứa không có điện"
    ], 0, "Tự sản xuất điện tái tạo đủ bù đắp điện tiêu thụ cả năm."),
    make_vdc(4, "Tận dụng năng lượng biogas từ hầm ủ chất thải chăn nuôi lợn, bò ở nông thôn mang lại lợi ích kép vừa cung cấp khí gas đun nấu miễn phí vừa:", [
        "Xử lý triệt để ô nhiễm chất thải chăn nuôi, giảm mùi hôi và ngăn phát thải khí mêtan vào khí quyển",
        "Làm tăng lượng rác thải nông nghiệp",
        "Gây ô nhiễm đất canh tác",
        "Làm mất nguồn phân bón hữu cơ"
    ], 0, "Bảo vệ môi trường nông thôn và tạo năng lượng sinh học sạch.")
]

exams["phys9_c8_rev_test1"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 1, p1_rev_t1, p2_rev_t1, p3_rev_t1, p4_rev_t1)

# =============================================================================
# phys9_c8_rev_test2
# =============================================================================
p1_rev_t2 = [
    make_mc(1, "Nhận biết", "Trong một chu trình chuyển hóa năng lượng, tổng năng lượng có ích và năng lượng hao phí luôn bằng:", [
        "Năng lượng toàn phần cung cấp cho quá trình",
        "Hai lần năng lượng có ích",
        "Năng lượng hao phí nhân đôi",
        "Bằng 0"
    ], 0, "A_toàn_phần = A_có_ích + A_hao_phí."),
    make_mc(2, "Nhận biết", "Nguồn năng lượng nào sau đây có nguồn gốc từ lực hấp dẫn của Mặt Trăng tác dụng lên các đại dương Trái Đất?", [
        "Năng lượng thủy triều",
        "Năng lượng gió",
        "Năng lượng sinh khối",
        "Năng lượng mặt trời"
    ], 0, "Thủy triều sinh ra do lực hấp dẫn của Mặt Trăng."),
    make_mc(3, "Nhận biết", "Năng lượng địa nhiệt được lấy từ nguồn nào?", [
        "Nhiệt lượng tự nhiên từ sâu trong lòng Trái Đất",
        "Ánh nắng mặt trời trên đồi cao",
        "Gió biển thổi vào bờ",
        "Sóng biển vỗ bờ"
    ], 0, "Địa nhiệt lấy từ lòng đất."),
    make_mc(4, "Nhận biết", "Dạng năng lượng tích trữ trong thức ăn và pin hóa học là:", [
        "Hóa năng",
        "Cơ năng",
        "Quang năng",
        "Thế năng đàn hồi"
    ], 0, "Thức ăn và pin hóa học tích trữ hóa năng."),
    make_mc(5, "Nhận biết", "Trong nhà máy điện gió, động năng của luồng gió quay tuabin được chuyển hóa thành:", [
        "Điện năng",
        "Hóa năng",
        "Nhiệt năng hạt nhân",
        "Thế năng trọng trường"
    ], 0, "Động năng của gió chuyển thành điện năng."),
    make_mc(6, "Nhận biết", "Bếp từ nấu ăn chuyển hóa điện năng chủ yếu thành dạng năng lượng có ích nào?", [
        "Nhiệt năng làm nóng xoong nồi",
        "Quang năng chiếu sáng",
        "Cơ năng quay",
        "Hóa năng"
    ], 0, "Điện năng chuyển thành nhiệt năng có ích nấu chín thức ăn."),
    make_mc(7, "Thông hiểu", "Một động cơ điện tiêu thụ 400 J điện năng sinh ra 300 J cơ năng có ích. Hiệu suất của động cơ là:", [
        "75%",
        "25%",
        "100%",
        "133%"
    ], 0, "H = (300 / 400) × 100% = 75%."),
    make_mc(8, "Thông hiểu", "Một bếp gas đốt cháy lượng gas có nhiệt lượng 20.000 J nhưng nước trong nồi chỉ hấp thụ được 12.000 J. Năng lượng hao phí tỏa ra không khí là:", [
        "8.000 J",
        "12.000 J",
        "20.000 J",
        "32.000 J"
    ], 0, "A_hp = 20.000 - 12.000 = 8000 J."),
    make_mc(9, "Thông hiểu", "Tại sao năng lượng mặt trời được coi là nguồn năng lượng tái tạo bền vững nhất của loài người?", [
        "Vì Mặt Trời sẽ tiếp tục tỏa sáng ổn định trong hàng tỷ năm nữa mà không bị cạn kiệt",
        "Vì pin mặt trời không bao giờ hỏng",
        "Vì ánh sáng mặt trời không mang nhiệt",
        "Vì Mặt Trời quay quanh Trái Đất"
    ], 0, "Mặt Trời tồn tại và bức xạ liên tục trong hàng tỷ năm."),
    make_mc(10, "Thông hiểu", "Khí mêtan (CH4) thu được từ hầm ủ Biogas chất thải chăn nuôi có thể dùng để:", [
        "Đun nấu thức ăn và chạy máy phát điện sinh hoạt",
        "Làm đông đá thực phẩm",
        "Dập tắt đám cháy rừng",
        "Lọc sạch nước biển"
    ], 0, "Biogas dùng làm nhiên liệu đun nấu sạch và phát điện."),
    make_mc(11, "Thông hiểu", "Thiết bị điện gia dụng nào sau đây thường có hiệu suất chuyển hóa năng lượng đạt cao nhất?", [
        "Bình nóng lạnh hoặc ấm siêu tốc (đạt ~90 - 95%)",
        "Động cơ xe máy xăng (đạt ~25%)",
        "Bóng đèn sợi đốt (đạt ~5%)",
        "Động cơ hơi nước cổ điển (đạt ~10%)"
    ], 0, "Ấm siêu tốc và bình nóng lạnh chuyển trực tiếp điện thành nhiệt với hiệu suất rất cao."),
    make_mc(12, "Thông hiểu", "Khi một vật trượt có ma sát từ đỉnh dốc xuống chân dốc, cơ năng ở chân dốc nhỏ hơn thế năng ở đỉnh dốc. Điều này có vi phạm định luật bảo toàn năng lượng không?", [
        "Không vi phạm, vì một phần cơ năng đã chuyển hóa thành nhiệt năng làm nóng vật và mặt dốc",
        "Có vi phạm vì cơ năng bị mất đi",
        "Có vi phạm vì thế năng tự sinh ra",
        "Do trọng lực Trái Đất bị suy giảm"
    ], 0, "Cơ năng hao hụt đã chuyển hóa thành nhiệt năng do ma sát, tổng năng lượng vẫn bảo toàn.")
]

p2_rev_t2 = [
    make_tf(1, "Thông hiểu", "Về chu trình năng lượng và chuyển hóa năng lượng:", [
        ("a", "Năng lượng có thể chuyển hóa giữa các dạng cơ năng, nhiệt năng, điện năng, hóa năng.", True),
        ("b", "Trong chu trình nước tự nhiên, nhiệt năng Mặt Trời làm nước bốc hơi tạo thành mây mưa.", True),
        ("c", "Quá trình quang hợp của cây xanh biến đổi quang năng thành hóa năng.", True),
        ("d", "Năng lượng toàn phần sau quá trình biến đổi luôn lớn hơn năng lượng ban đầu.", False)
    ], "Năng lượng toàn phần luôn bằng năng lượng ban đầu (định luật bảo toàn năng lượng)."),
    make_tf(2, "Thông hiểu", "Về năng lượng tái tạo và giảm phát thải khí nhà kính:", [
        ("a", "Sử dụng xe ô tô điện góp phần giảm ô nhiễm không khí tại các thành phố lớn.", True),
        ("b", "Điện mặt trời mái nhà giúp gia đình giảm lượng điện mua từ lưới điện quốc gia.", True),
        ("c", "Năng lượng hóa thạch không bao giờ gây ra hiện tượng mưa axit.", False),
        ("d", "Khí CO2 và SO2 sinh ra từ đốt than đá là tác nhân gây mưa axit và hiệu ứng nhà kính.", True)
    ], "Đốt than đá thải lượng lớn SO2 và NOx gây mưa axit độc hại."),
    make_tf(3, "Vận dụng", "Một động cơ điện tiêu thụ công suất điện 1000 W hoạt động trong 1 giờ (3600 giây) để bơm nước lên bồn cao với hiệu suất 75%:", [
        ("a", "Điện năng toàn phần tiêu thụ là 3.600.000 J (1 kWh).", True),
        ("b", "Công có ích để bơm nước là 2.700.000 J (0,75 kWh).", True),
        ("c", "Nhiệt lượng hao phí tỏa ra làm nóng máy bơm là 900.000 J (0,25 kWh).", True),
        ("d", "Hiệu suất của máy bơm này là 100%.", False)
    ], "A_tp = 1000 × 3600 = 3,6 MJ. A_ích = 3,6 × 75% = 2,7 MJ. A_hp = 0,9 MJ. Hiệu suất là 75%."),
    make_tf(4, "Vận dụng", "Một nhà máy thủy điện có hồ chứa nước cung cấp thế năng toàn phần 40 MJ mỗi giây. Máy phát điện của nhà máy sinh ra công suất điện 32 MW (32 MJ/s):", [
        ("a", "Công suất toàn phần của dòng nước là 40 MW.", True),
        ("b", "Công suất điện có ích phát ra là 32 MW.", True),
        ("c", "Công suất hao phí do ma sát tuabin và dòng xoáy là 8 MW.", True),
        ("d", "Hiệu suất chuyển hóa năng lượng của nhà máy thủy điện là 80%.", True)
    ], "H = 32 / 40 = 80%.")
]

p3_rev_t2 = [
    make_sa(1, "Thông hiểu", "Dạng năng lượng tích trữ trong than đá và dầu mỏ là năng lượng gì?", "Hóa năng", "Hóa năng."),
    make_sa(2, "Thông hiểu", "Năng lượng sinh khối (Biomass) là năng lượng tái tạo hay không tái tạo?", "Tái tạo", "Năng lượng tái tạo."),
    make_sa(3, "Vận dụng", "Một bóng đèn LED tiêu thụ 20 J điện năng và phát ra 16 J quang năng. Hiệu suất phát quang của đèn là bao nhiêu %?", "80", "16 / 20 = 80%."),
    make_sa(4, "Vận dụng", "Một ấm đun nước điện có hiệu suất 90%. Nếu cung cấp 1.000.000 J điện năng thì nhiệt lượng có ích làm sôi nước là bao nhiêu Jun?", "900000", "1.000.000 × 90% = 900.000 J."),
    make_sa(5, "Vận dụng cao", "Một thang máy nâng một người nặng 60 kg lên cao 20 m trong 15 giây (g = 10 m/s2). Công có ích thực hiện được là bao nhiêu Jun?", "12000", "A_ích = m × g × h = 60 × 10 × 20 = 12.000 J."),
    make_sa(6, "Vận dụng cao", "Một gia đình dùng 4 bóng đèn LED 15W thay thế 4 bóng đèn sợi đốt 75W trong 5 giờ mỗi ngày. Điện năng tiết kiệm được mỗi ngày là bao nhiêu kWh? (Lấy số thập phân)", "1.2", "P_tiết_kiệm = (75 - 15) × 4 = 240 W = 0,24 kW. A = 0,24 × 5 = 1,2 kWh.")
]

p4_rev_t2 = [
    make_vdc(1, "Hệ thống nhà máy thủy điện tích năng (Pumped Storage Hydropower) giải quyết bài toán thừa thiếu điện năng của hệ thống điện quốc gia như thế nào?", [
        "Dùng điện dư thừa giá rẻ ban đêm bơm nước lên hồ cao tích trữ cơ năng, ban ngày giờ cao điểm xả nước xuống phát điện bổ sung cho lưới",
        "Tự động tạo ra nước mới trong mùa khô",
        "Làm tăng lượng mưa tự nhiên",
        "Lọc sạch nước hồ thành nước ngọt"
    ], 0, "Bơm nước lên cao ban đêm (nạp năng lượng) và phát điện giờ cao điểm ban ngày (xả năng lượng)."),
    make_vdc(2, "Tại sao các tấm pin quang điện mặt trời lắp đặt ngoài trời sau một thời gian bị bám bụi bẩn dầy đặc lại bị sụt giảm công suất phát điện từ 15% đến 25%?", [
        "Lớp bụi cản trở quang năng từ ánh sáng mặt trời chiếu vào bề mặt tế bào bán dẫn silicon",
        "Bụi bẩn làm pin bị nhiễm điện tích âm",
        "Bụi bẩn hút hết dòng điện trong dây dẫn",
        "Bụi bẩn làm tăng điện áp của pin"
    ], 0, "Bụi bẩn che khuất ánh sáng làm giảm mật độ photon chiếu vào tinh thể bán dẫn, làm sụt giảm dòng quang điện sinh ra."),
    make_vdc(3, "Công nghệ đệm từ trường và thu hồi động năng trên tàu điện đô thị (Metro): Khi đoàn tàu metro tiến vào ga và hãm phanh, hệ thống phanh tái sinh điện năng nạp ngược điện lên đường dây tiếp điện trên cao để cung cấp cho đoàn tàu khác đang khởi hành rời ga. Ý nghĩa bảo tồn năng lượng của hệ thống này là:", [
        "Tái sử dụng trực tiếp động năng của đoàn tàu giảm tốc để cấp cơ năng cho đoàn tàu tăng tốc, giảm tới 30% điện năng tiêu thụ toàn tuyến",
        "Làm đoàn tàu nhẹ hơn",
        "Làm tàu không cần đường ray",
        "Làm mát nhiệt độ trong toa tàu"
    ], 0, "Phanh tái sinh biến động năng hãm phanh thành điện năng cấp trực tiếp cho các đoàn tàu khác cùng tuyến đang tăng tốc."),
    make_vdc(4, "Một người muốn mua máy điều hòa không khí mới cho phòng ngủ gia đình. Giữa hai chiếc máy cùng công suất lạnh: Máy A đạt nhãn năng lượng 5 sao (công nghệ Inverter, giá đắt hơn 2 triệu đồng) và Máy B đạt nhãn năng lượng 2 sao (giá rẻ hơn). Lời khuyên đầu tư tối ưu về kinh tế lâu dài là:", [
        "Nên chọn Máy A nhãn 5 sao vì lượng điện năng tiết kiệm được mỗi tháng sẽ nhanh chóng bù đắp khoản tiền chênh lệch ban đầu và tiết kiệm chi phí tiền điện lớn trong suốt vòng đời sử dụng",
        "Nên chọn Máy B vì giá ban đầu rẻ hơn",
        "Cả hai máy tốn tiền điện hoàn toàn như nhau",
        "Máy A tốn điện hơn máy B gấp đôi"
    ], 0, "Máy 5 sao Inverter tiết kiệm 30-50% điện năng, tiền điện tiết kiệm trong 1-2 năm đủ bù tiền chênh lệch mua máy ban đầu.")
]

exams["phys9_c8_rev_test2"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 2, p1_rev_t2, p2_rev_t2, p3_rev_t2, p4_rev_t2)

# =============================================================================
# phys9_c8_rev_test3
# =============================================================================
p1_rev_t3 = [
    make_mc(1, "Nhận biết", "Trong một hệ thống chuyển hóa năng lượng, hiệu suất H không bao giờ vượt quá:", [
        "100%",
        "50%",
        "75%",
        "200%"
    ], 0, "Hiệu suất không bao giờ vượt quá 100%."),
    make_mc(2, "Nhận biết", "Năng lượng sinh khối (Biomass) có nguồn gốc từ:", [
        "Thực vật, cây trồng và chất thải hữu cơ nông nghiệp",
        "Các mỏ khoáng sản kim loại",
        "Nước biển sâu",
        "Bụi trong không khí"
    ], 0, "Sinh khối bắt nguồn từ thực vật và chất thải hữu cơ."),
    make_mc(3, "Nhận biết", "Khi nạp pin cho một xe máy điện, dạng năng lượng nào được tích trữ trong bộ pin?", [
        "Hóa năng",
        "Cơ năng",
        "Nhiệt năng",
        "Quang năng"
    ], 0, "Hóa năng tích trữ trong các phản ứng điện hóa của pin."),
    make_mc(4, "Nhận biết", "Năng lượng gió trên Trái Đất là một dạng năng lượng phái sinh từ:", [
        "Năng lượng Mặt Trời hun nóng khí quyển không đều",
        "Năng lượng hạt nhân",
        "Thủy triều Mặt Trăng",
        "Nhiệt độ tâm Trái Đất"
    ], 0, "Năng lượng Mặt Trời sinh ra sự chênh lệch áp suất tạo thành gió."),
    make_mc(5, "Nhận biết", "Tác nhân chính gây ra hiện tượng hiệu ứng nhà kính làm khí hậu Trái Đất nóng lên là khí:", [
        "Cacbon đioxit (CO2)",
        "Khí oxi (O2)",
        "Khí nitơ (N2)",
        "Khí hiđro (H2)"
    ], 0, "Khí CO2 là khí nhà kính chính."),
    make_mc(6, "Nhận biết", "Khi bóng đèn sợi đốt phát sáng, năng lượng hao phí xuất hiện dưới dạng:", [
        "Nhiệt năng làm nóng bóng đèn và không khí xung quanh",
        "Quang năng chiếu sáng",
        "Cơ năng làm rung dây tóc",
        "Hóa năng tích tụ"
    ], 0, "Nhiệt năng tỏa ra là năng lượng hao phí."),
    make_mc(7, "Thông hiểu", "Một động cơ điện kéo một vật nặng thực hiện công có ích là 1800 J trong khi tiêu thụ 2000 J điện năng. Năng lượng hao phí tỏa nhiệt là:", [
        "200 J",
        "1800 J",
        "2000 J",
        "3800 J"
    ], 0, "A_hp = 2000 - 1800 = 200 J."),
    make_mc(8, "Thông hiểu", "Một nhà máy thủy điện có hiệu suất 80%. Nếu thế năng của lượng nước chảy qua tuabin là 100 MJ thì điện năng sinh ra là:", [
        "80 MJ",
        "20 MJ",
        "100 MJ",
        "125 MJ"
    ], 0, "A_ích = 100 × 80% = 80 MJ."),
    make_mc(9, "Thông hiểu", "Tại sao việc sử dụng xe buýt điện thay thế xe buýt chạy dầu diesel giúp giảm ô nhiễm không khí đô thị?", [
        "Vì xe buýt điện không phát thải khói đen, bụi mịn PM2.5 và khí độc tại ống xả trong thành phố",
        "Vì xe buýt điện chạy nhanh hơn gấp mười lần",
        "Vì xe buýt điện không cần người lái",
        "Vì xe buýt điện làm giảm nhiệt độ mùa hè"
    ], 0, "Xe điện không phát thải khí xả tại chỗ, cải thiện trực tiếp chất lượng không khí đô thị."),
    make_mc(10, "Thông hiểu", "Khi một viên phấn rơi tự do từ bàn học xuống sàn nhà, sau khi va chạm chạm đất đứng yên, toàn bộ cơ năng của viên phấn đã biến thành:", [
        "Nhiệt năng làm nóng viên phấn, mặt sàn và năng lượng âm thanh tiếng 'cạch'",
        "Hóa năng làm viên phấn đổi màu",
        "Điện năng",
        "Quang năng phát sáng"
    ], 0, "Cơ năng chuyển thành nhiệt năng và âm thanh khi va chạm không đàn hồi."),
    make_mc(11, "Thông hiểu", "Nhãn năng lượng 5 sao trên tủ lạnh cho người tiêu dùng biết:", [
        "Tủ lạnh có mức tiêu thụ điện năng thấp nhất trong cùng phân khúc dung tích",
        "Tủ lạnh làm đá nhanh gấp 5 lần",
        "Tủ lạnh nặng gấp 5 lần",
        "Tủ lạnh có 5 cánh cửa"
    ], 0, "Nhãn 5 sao biểu thị hiệu suất năng lượng cao nhất, tiết kiệm điện nhất."),
    make_mc(12, "Thông hiểu", "Để hạn chế hao phí điện năng của tủ lạnh gia đình, thói quen sử dụng đúng đắn là:", [
        "Không để thức ăn còn đang nóng hổi vào trong tủ lạnh và đóng kín cửa tủ sau khi lấy đồ",
        "Mở toang cửa tủ lạnh cả ngày cho mát nhà",
        "Nhồi nhét thức ăn kín mít che hết các lỗ thông gió",
        "Cài đặt nhiệt độ ngăn mát ở mức lạnh nhất liên tục"
    ], 0, "Để đồ nguội mới cho vào tủ và đóng kín cửa tránh thất thoát nhiệt lạnh.")
]

p2_rev_t3 = [
    make_tf(1, "Thông hiểu", "Về các nguồn năng lượng và tính bền vững:", [
        ("a", "Năng lượng mặt trời là nguồn năng lượng tái tạo sạch.", True),
        ("b", "Năng lượng từ than đá không sinh ra khí thải độc hại.", False),
        ("c", "Năng lượng hạt nhân sử dụng nguồn nhiên liệu uranium hữu hạn.", True),
        ("d", "Khí Biogas là nguồn năng lượng sinh học tái tạo từ chất thải chăn nuôi.", True)
    ], "Đốt than đá thải lượng lớn CO2, SO2, tro xỉ và bụi mịn độc hại."),
    make_tf(2, "Thông hiểu", "Về định luật bảo toàn năng lượng:", [
        ("a", "Năng lượng trong tự nhiên không tự nhiên sinh ra.", True),
        ("b", "Năng lượng trong tự nhiên không tự nhiên mất đi.", True),
        ("c", "Động cơ vĩnh cửu có thể hoạt động mà không cần nạp bất kỳ nhiên liệu nào.", False),
        ("d", "Năng lượng có ích cộng năng lượng hao phí bằng năng lượng toàn phần.", True)
    ], "Động cơ vĩnh cửu không thể tồn tại trong thực tế."),
    make_tf(3, "Vận dụng", "Một tấm pin mặt trời diện tích 1,5 m2 nhận bức xạ mặt trời có công suất 1000 W/m2. Hiệu suất chuyển hóa của tấm pin là 18%:", [
        ("a", "Công suất bức xạ chiếu vào toàn bộ tấm pin là 1500 W.", True),
        ("b", "Công suất điện sinh ra từ tấm pin là 270 W.", True),
        ("c", "Công suất hao phí tỏa nhiệt trên tấm pin là 1230 W.", True),
        ("d", "Tấm pin này chuyển hóa 100% ánh sáng thành điện năng.", False)
    ], "P_tp = 1,5 × 1000 = 1500 W. P_ích = 1500 × 18% = 270 W. P_hp = 1500 - 270 = 1230 W. Hiệu suất là 18%."),
    make_tf(4, "Vận dụng", "Một xe ô tô điện tiêu thụ 15 kWh điện năng để đi được quãng đường 100 km:", [
        ("a", "Mức tiêu thụ năng lượng trung bình là 0,15 kWh cho mỗi kilômét.", True),
        ("b", "Nếu giá điện sinh hoạt là 2.500 đồng/kWh thì chi phí tiền điện cho 100 km là 37.500 đồng.", True),
        ("c", "Chi phí năng lượng của xe điện rẻ hơn đáng kể so với xe chạy xăng tiêu thụ 7 lít xăng/100 km (khoảng 160.000 đồng).", True),
        ("d", "Xe điện phát thải khí độc trực tiếp ra môi trường khi đang chạy.", False)
    ], "Xe điện không có ống xả, không phát thải khí độc tại chỗ.")
]

p3_rev_t3 = [
    make_sa(1, "Thông hiểu", "Phần năng lượng không phục vụ cho mục đích ban đầu gọi là năng lượng gì?", "Hao phí", "Năng lượng hao phí."),
    make_sa(2, "Thông hiểu", "Việt Nam có bờ biển dài trên 3260 km rất thuận lợi phát triển loại điện tái tạo nào ngoài biển?", "Điện gió", "Điện gió ngoài khơi."),
    make_sa(3, "Vận dụng", "Một động cơ điện tiêu thụ 800 J điện năng sinh ra công có ích 640 J. Hiệu suất của động cơ là bao nhiêu %?", "80", "640 / 800 = 80%."),
    make_sa(4, "Vận dụng", "Một gia đình thay 6 bóng đèn 60W bằng 6 bóng LED 10W. Công suất điện giảm được là bao nhiêu Watt?", "300", "(60 - 10) × 6 = 300 W."),
    make_sa(5, "Vận dụng cao", "Một máy bơm công suất 500 W hoạt động với hiệu suất 80% trong 2 giờ (7200 giây). Công có ích thực hiện được là bao nhiêu Kilôjun (kJ)?", "2880", "A_tp = 500 × 7200 = 3.600.000 J. A_ích = 3,6 MJ × 80% = 2,88 MJ = 2880 kJ."),
    make_sa(6, "Vận dụng cao", "Một hệ thống pin mặt trời sinh ra 5 kWh điện mỗi ngày. Trong 1 năm (365 ngày), hệ thống sinh ra bao nhiêu kWh điện?", "1825", "5 × 365 = 1825 kWh.")
]

p4_rev_t3 = [
    make_vdc(1, "Công nghệ tế bào quang điện màng mỏng Perovskite thế hệ mới: Các nhà khoa học kết hợp lớp vật liệu Perovskite trên nền silicon truyền thống để tạo pin mặt trời hai lớp (Tandem Solar Cell). Ưu điểm đột phá của pin Tandem là:", [
        "Hấp thụ được cả dải ánh sáng khả kiến và ánh sáng hồng ngoại, nâng hiệu suất chuyển hóa quang điện vượt ngưỡng 30%",
        "Làm pin mặt trời tự phát sáng ban đêm",
        "Làm pin mặt trời nhẹ như bóng bay",
        "Biến pin thành tấm gương phẳng soi mặt"
    ], 0, "Pin Tandem Perovskite-Silicon mở rộng dải phổ hấp thụ photon, nâng hiệu suất phòng thí nghiệm vượt trên 33%."),
    make_vdc(2, "Một nhà máy chế biến dừa ở Bến Tre tận dụng hàng nghìn tấn gáo dừa và vỏ dừa phế thải mỗi ngày để nung thành than hoạt tính và phát điện sinh khối cấp cho toàn bộ dây chuyền sản xuất. Ý nghĩa sinh thái của mô hình kinh tế tuần hoàn này là:", [
        "Biến phế phẩm nông nghiệp thành sản phẩm giá trị cao và tự chủ 100% năng lượng sạch, không xả rác thải ra môi trường",
        "Làm cây dừa sinh trưởng nhanh gấp mười lần",
        "Làm nước dừa ngọt hơn",
        "Khử hoàn toàn nước mặn ở sông Tiền"
    ], 0, "Tận dụng phụ phẩm gáo dừa phát điện sinh khối tạo vòng kinh tế tuần hoàn khép kín không rác thải."),
    make_vdc(3, "Tại sao trên nóc các tòa nhà hiện đại người ta thường sơn phản xạ nhiệt màu trắng (Cool Roof) kết hợp trồng vườn cây xanh trên mái?", [
        "Giảm hấp thụ nhiệt bức xạ mặt trời vào trần nhà, hạ nhiệt độ trong phòng từ 3 đến 5 độ C giúp giảm tiêu thụ điện năng của hệ thống điều hòa",
        "Để trang trí cho đẹp khi chụp ảnh từ vệ tinh",
        "Để thu hút chim về làm tổ",
        "Làm nhà nặng hơn để chống bão"
    ], 0, "Mái nhà mát phản xạ bức xạ nhiệt mặt trời và lớp cây xanh cách nhiệt tự nhiên, giảm tải làm lạnh cho điều hòa không khí."),
    make_vdc(4, "Một cần cẩu điện nâng một thùng hàng container nặng 20 tấn (20.000 kg) lên cao 15 m trong thời gian 30 giây (g = 10 m/s2). Động cơ cần cẩu tiêu thụ công suất điện 125 kW. Hiệu suất của cần cẩu điện này là:", [
        "80%",
        "75%",
        "85%",
        "90%"
    ], 0, "A_ích = 20.000 × 10 × 15 = 3.000.000 J = 3 MJ. A_tp = 125.000 × 30 = 3.750.000 J = 3,75 MJ. H = 3 / 3,75 = 80%.")
]

exams["phys9_c8_rev_test3"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 3, p1_rev_t3, p2_rev_t3, p3_rev_t3, p4_rev_t3)

# =============================================================================
# phys9_c8_rev_test4
# =============================================================================
p1_rev_t4 = [
    make_mc(1, "Nhận biết", "Trong một hệ cô lập không trao đổi năng lượng với bên ngoài, tổng năng lượng của hệ:", [
        "Là một đại lượng không đổi theo thời gian",
        "Tự động tăng dần về vô cực",
        "Tự động giảm dần về 0",
        "Biến đổi tuần hoàn hình sin"
    ], 0, "Tổng năng lượng của hệ cô lập là bất biến."),
    make_mc(2, "Nhận biết", "Dạng năng lượng nào sau đây được dự trữ trong lòng đất dưới dạng nhiệt độ cao của đất đá và nước ngầm?", [
        "Năng lượng địa nhiệt",
        "Năng lượng gió",
        "Năng lượng bức xạ mặt trời",
        "Năng lượng thủy triều"
    ], 0, "Nhiệt trong lòng đất là năng lượng địa nhiệt."),
    make_mc(3, "Nhận biết", "Khi nạp pin dự phòng cho điện thoại di động, năng lượng được chuyển hóa như thế nào?", [
        "Điện năng chuyển hóa thành hóa năng tích trữ",
        "Cơ năng chuyển hóa thành quang năng",
        "Hóa năng biến thành nhiệt năng",
        "Quang năng biến thành thế năng"
    ], 0, "Điện năng chuyển thành hóa năng tích trữ trong pin."),
    make_mc(4, "Nhận biết", "Công thức tính hiệu suất H là:", [
        "H = (A_có_ích / A_toàn_phần) × 100%",
        "H = (A_toàn_phần / A_có_ích) × 100%",
        "H = A_có_ích - A_hao_phí",
        "H = A_hao_phí / A_có_ích"
    ], 0, "H = (A_ích / A_tp) × 100%."),
    make_mc(5, "Nhận biết", "Mặt Trời cung cấp năng lượng cho Trái Đất dưới hình thức:", [
        "Bức xạ nhiệt và ánh sáng (bức xạ điện từ)",
        "Dẫn nhiệt trực tiếp qua thanh kim loại",
        "Đối lưu của không khí",
        "Dòng điện một chiều"
    ], 0, "Bức xạ điện từ (quang năng và nhiệt năng hồng ngoại)."),
    make_mc(6, "Nhận biết", "Khi quạt điện quay, dạng năng lượng có ích là:", [
        "Cơ năng làm quay cánh quạt tạo gió",
        "Nhiệt năng làm nóng vỏ mô tơ",
        "Tiếng vù vù của gió",
        "Tia lửa điện ở chổi than"
    ], 0, "Cơ năng quay cánh quạt tạo gió là năng lượng có ích."),
    make_mc(7, "Thông hiểu", "Một động cơ điện tiêu thụ 600 J điện năng sinh ra 450 J cơ năng có ích. Hiệu suất của động cơ là:", [
        "75%",
        "25%",
        "100%",
        "133%"
    ], 0, "H = 450 / 600 = 75%."),
    make_mc(8, "Thông hiểu", "Một bình nóng lạnh tiêu thụ 2 kWh điện năng và thất thoát 0,2 kWh nhiệt lượng ra không khí. Hiệu suất đun nước là:", [
        "90%",
        "10%",
        "80%",
        "95%"
    ], 0, "A_ích = 2 - 0,2 = 1,8 kWh. H = 1,8 / 2 = 90%."),
    make_mc(9, "Thông hiểu", "Tại sao năng lượng gió và năng lượng mặt trời lại được khuyến khích phát triển trên toàn cầu?", [
        "Vì sạch, không phát thải khí nhà kính và nguồn cung tự nhiên dồi dào",
        "Vì thiết bị lắp đặt không tốn tiền",
        "Vì có thể phát điện liên tục không cần pin lưu trữ",
        "Vì làm tăng nhiệt độ Trái Đất"
    ], 0, "Năng lượng tái tạo sạch, bền vững và cắt giảm phát thải carbon."),
    make_mc(10, "Thông hiểu", "Khi chiếc xe máy đang chạy bị hết xăng và tắt máy, xe tiếp tục trượt thêm một đoạn ngắn rồi dừng hẳn. Cơ năng của xe đã chuyển thành:", [
        "Nhiệt năng do ma sát giữa lốp xe với mặt đường và lực cản không khí",
        "Hóa năng tích tụ lại vào bình xăng",
        "Điện năng nạp vào ắc quy",
        "Năng lượng ánh sáng"
    ], 0, "Ma sát chuyển hóa cơ năng thành nhiệt năng tỏa vào mặt đường và không khí."),
    make_mc(11, "Thông hiểu", "Bóng đèn huỳnh quang compact tiêu thụ 20 W điện năng phát ra cùng độ sáng với bóng đèn sợi đốt 100 W. Điều này chứng minh:", [
        "Bóng đèn compact có hiệu suất phát quang cao gấp khoảng 5 lần đèn sợi đốt",
        "Bóng đèn compact tiêu tốn nhiều điện hơn",
        "Đèn sợi đốt không tỏa nhiệt",
        "Hai đèn có hiệu suất bằng nhau"
    ], 0, "Cùng độ sáng quang năng nhưng tiêu thụ 20W so với 100W chứng minh hiệu suất đèn compact cao gấp 5 lần."),
    make_mc(12, "Thông hiểu", "Hành động nào sau đây giúp tiết kiệm năng lượng điện khi sử dụng máy tính để bàn?", [
        "Cài đặt chế độ tự động ngủ (Sleep) khi không sử dụng và tắt màn hình khi rời bàn làm việc",
        "Bật màn hình sáng tối đa liên tục",
        "Cắm máy tính chạy liên tục suốt tuần không tắt",
        "Chạy nhiều phần mềm nặng cùng lúc khi không dùng"
    ], 0, "Chế độ Sleep và tắt màn hình giúp giảm thiểu điện năng tiêu thụ vô ích.")
]

p2_rev_t4 = [
    make_tf(1, "Thông hiểu", "Về chu trình năng lượng và bảo toàn năng lượng:", [
        ("a", "Năng lượng không tự sinh ra cũng không tự mất đi.", True),
        ("b", "Năng lượng Mặt Trời là nguồn gốc sơ cấp của than đá và dầu mỏ.", True),
        ("c", "Hiệu suất của bất kỳ quá trình cơ học nào đều có thể đạt 150%.", False),
        ("d", "Trong bóng đèn LED, điện năng chuyển hóa thành quang năng và một phần nhiệt năng.", True)
    ], "Hiệu suất không bao giờ vượt quá 100%."),
    make_tf(2, "Thông hiểu", "Về năng lượng tái tạo và bảo vệ môi trường:", [
        ("a", "Năng lượng gió là năng lượng tái tạo.", True),
        ("b", "Khí CO2 thải ra từ đốt than đá là nguyên nhân chính gây hiệu ứng nhà kính.", True),
        ("c", "Tất cả các nguồn năng lượng hóa thạch đều là nguồn năng lượng tái tạo.", False),
        ("d", "Khí sinh học Biogas là nguồn năng lượng sạch thân thiện môi trường.", True)
    ], "Nhiên liệu hóa thạch không thể tái tạo."),
    make_tf(3, "Vận dụng", "Một động cơ điện tiêu thụ công suất 1500 W hoạt động trong 20 giây để nâng một vật nặng 2000 N lên cao 12 m:", [
        ("a", "Công có ích để nâng vật là 24.000 J (24 kJ).", True),
        ("b", "Điện năng toàn phần tiêu thụ là 30.000 J (30 kJ).", True),
        ("c", "Năng lượng hao phí do tỏa nhiệt là 6.000 J (6 kJ).", True),
        ("d", "Hiệu suất của động cơ nâng này là 80%.", True)
    ], "A_ích = 2000 × 12 = 24.000 J. A_tp = 1500 × 20 = 30.000 J. H = 24.000 / 30.000 = 80%."),
    make_tf(4, "Vận dụng", "Một nhà máy thủy điện có công suất phát điện là 50 MW và hiệu suất chuyển đổi là 80%:", [
        ("a", "Công suất thế năng toàn phần của dòng nước là 62,5 MW.", True),
        ("b", "Công suất hao phí do ma sát và tổn thất dòng xoáy là 12,5 MW.", True),
        ("c", "Trong 10 giờ chạy hết công suất, nhà máy phát ra 500 MWh điện.", True),
        ("d", "Thủy điện là nguồn năng lượng hóa thạch phát thải khói bụi lớn.", False)
    ], "P_tp = 50 / 80% = 62,5 MW. P_hp = 12,5 MW. A = 50 × 10 = 500 MWh. Thủy điện là năng lượng tái tạo sạch.")
]

p3_rev_t4 = [
    make_sa(1, "Thông hiểu", "Năng lượng toàn phần bằng năng lượng có ích cộng với năng lượng gì?", "Hao phí", "Năng lượng hao phí."),
    make_sa(2, "Thông hiểu", "Tỉ số giữa năng lượng có ích và năng lượng toàn phần được gọi là gì?", "Hiệu suất", "Hiệu suất."),
    make_sa(3, "Vận dụng", "Một động cơ điện tiêu thụ 1200 J điện năng sinh ra công có ích 960 J. Hiệu suất của động cơ là bao nhiêu %?", "80", "960 / 1200 = 80%."),
    make_sa(4, "Vận dụng", "Một tấm pin mặt trời nhận 5000 J quang năng và sinh ra 900 J điện năng. Hiệu suất của tấm pin là bao nhiêu %?", "18", "900 / 5000 = 18%."),
    make_sa(5, "Vận dụng cao", "Một máy bơm nước tiêu thụ 600 W hoạt động với hiệu suất 75%. Công suất có ích để bơm nước là bao nhiêu Watt?", "450", "600 × 75% = 450 W."),
    make_sa(6, "Vận dụng cao", "Một gia đình thay 5 bóng đèn sợi đốt 100W bằng 5 bóng đèn LED 12W, dùng 4 giờ mỗi ngày. Điện năng tiết kiệm được trong 1 ngày là bao nhiêu kWh? (Lấy số thập phân)", "1.76", "P_tiết_kiệm = (100 - 12) × 5 = 440 W = 0,44 kW. A = 0,44 × 4 = 1,76 kWh.")
]

p4_rev_t4 = [
    make_vdc(1, "Công nghệ đê biển phát điện thủy triều đầm phá nhân tạo (Tidal Lagoon): Người ta xây dựng một con đê nhân tạo hình vòng cung khép kín ngoài vịnh biển tạo thành một đầm phá nước mặn gắn các tuabin phát điện hai chiều. Lợi thế môi trường nổi bật của đầm phá thủy triều so với đập thủy điện sông truyền thống là:", [
        "Hoàn toàn không làm ngập rừng tự nhiên, không phải di dời dân cư và bảo tồn nguyên vẹn hệ sinh thái các dòng sông nội địa",
        "Đầm phá thủy triều không có nước biển",
        "Tạo ra mỏ muối khô sau 1 ngày",
        "Làm tăng bão biển ngoài khơi"
    ], 0, "Thủy triều đầm phá nhân tạo ngoài vịnh không chiếm đất liền, không ảnh hưởng sinh thái sông ngòi và di dân."),
    make_vdc(2, "Hệ thống nhà máy nhiệt điện mặt trời tập trung (CSP - Concentrated Solar Power): Hàng nghìn tấm gương phẳng (Heliostat) tự động xoay theo Mặt Trời để hội tụ ánh sáng vào đỉnh tháp trung tâm nung muối nóng chảy lên tới 565 độ C. Muối nóng chảy giữ nhiệt suốt đêm để tạo hơi nước chạy tuabin phát điện 24/24. Ưu điểm vượt trội của CSP so với pin mặt trời quang điện (PV) là:", [
        "Khả năng lưu trữ nhiệt năng quy mô lớn giá rẻ để phát điện liên tục cả ban đêm và những lúc trời nhiều mây",
        "CSP không cần ánh sáng mặt trời vẫn chạy được",
        "CSP làm mát toàn bộ sa mạc",
        "CSP không tỏa bất kỳ nhiệt lượng nào"
    ], 0, "Muối nóng chảy trong nhà máy CSP lưu trữ nhiệt năng giá rẻ khổng lồ, cho phép phát điện ban đêm ổn định như nhiệt điện than."),
    make_vdc(3, "Xe ô tô điện Tesla sử dụng hệ thống làm mát pin bằng chất lỏng tuần hoàn thông minh qua các ống nhôm uốn lượn giữa các cell pin. Khi trời mùa đông băng tuyết lạnh giá (-20 độ C), hệ thống tự động làm nóng pin trước khi sạc. Tác dụng của việc giữ nhiệt độ pin trong khoảng tối ưu (20 - 35 độ C) là:", [
        "Duy trì hiệu suất phản ứng điện hóa tối đa, bảo vệ tuổi thọ pin không bị suy giảm dung lượng và rút ngắn thời gian sạc nhanh",
        "Làm tan chảy lốp xe",
        "Làm pin tự phát nổ",
        "Tăng trọng lượng của xe"
    ], 0, "Nhiệt độ tối ưu giúp ion Lithium dịch chuyển nhanh trong chất điện phân, nâng cao hiệu suất sạc xả và bảo vệ tuổi thọ pin."),
    make_vdc(4, "Một cần cẩu điện có công suất 20 kW kéo một khối sắt vụn nặng 3000 kg lên cao 10 m trong thời gian 20 giây (g = 10 m/s2). Hiệu suất nâng của cần cẩu điện này là:", [
        "75%",
        "80%",
        "70%",
        "85%"
    ], 0, "A_ích = 3000 × 10 × 10 = 300.000 J. A_tp = 20.000 × 20 = 400.000 J. H = 300.000 / 400.000 = 75%.")
]

exams["phys9_c8_rev_test4"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 4, p1_rev_t4, p2_rev_t4, p3_rev_t4, p4_rev_t4)

# =============================================================================
# phys9_c8_rev_test5
# =============================================================================
p1_rev_t5 = [
    make_mc(1, "Nhận biết", "Trong mọi quá trình biến đổi năng lượng, năng lượng toàn phần luôn được:", [
        "Bảo toàn (không tự sinh ra và không tự mất đi)",
        "Tự động tăng gấp đôi",
        "Tự động giảm dần về 0",
        "Biến thành sóng âm thanh hoàn toàn"
    ], 0, "Năng lượng toàn phần luôn được bảo toàn."),
    make_mc(2, "Nhận biết", "Nguồn năng lượng nào sau đây có nguồn gốc từ lực hấp dẫn giữa Mặt Trăng, Mặt Trời và Trái Đất làm nước biển dâng hạ theo chu kỳ?", [
        "Năng lượng thủy triều",
        "Năng lượng hạt nhân",
        "Năng lượng địa nhiệt",
        "Năng lượng hóa thạch"
    ], 0, "Sự chuyển động dâng hạ của triều cường sinh ra năng lượng thủy triều."),
    make_mc(3, "Nhận biết", "Loại khí thiên nhiên nào có thành phần chính là khí mêtan (CH4) được khai thác từ các mỏ khí dưới lòng đất?", [
        "Khí tự nhiên (khí mỏ)",
        "Khí oxy tinh khiết",
        "Khí nitơ lỏng",
        "Khí cacbonic"
    ], 0, "Khí tự nhiên có thành phần chính là CH4 khai thác từ lòng đất."),
    make_mc(4, "Nhận biết", "Hiệu suất H của một động cơ được tính bằng tỉ số giữa:", [
        "Công có ích và công toàn phần",
        "Công toàn phần và công có ích",
        "Công hao phí và công có ích",
        "Công toàn phần và công hao phí"
    ], 0, "H = A_có_ích / A_toàn_phần."),
    make_mc(5, "Nhận biết", "Nguồn cội ban đầu của các mỏ than đá và dầu mỏ trên Trái Đất là:", [
        "Năng lượng bức xạ Mặt Trời được tích trữ trong xác sinh vật cổ đại",
        "Lõi kim loại nóng chảy của Trái Đất",
        "Bụi sao băng vũ trụ",
        "Nước biển sâu"
    ], 0, "Than đá và dầu mỏ là năng lượng Mặt Trời tích trữ hóa năng cổ đại."),
    make_mc(6, "Nhận biết", "Trong máy phát điện gió, tuabin gió chuyển hóa dạng năng lượng nào thành điện năng?", [
        "Cơ năng (động năng của gió)",
        "Hóa năng",
        "Quang năng",
        "Thế năng đàn hồi"
    ], 0, "Động năng của gió chuyển thành điện năng."),
    make_mc(7, "Thông hiểu", "Một động cơ điện tiêu thụ 800 J điện năng và sinh ra 600 J cơ năng có ích. Hiệu suất của động cơ là:", [
        "75%",
        "25%",
        "100%",
        "133%"
    ], 0, "H = 600 / 800 = 75%."),
    make_mc(8, "Thông hiểu", "Một bóng đèn sợi đốt tiêu thụ 60 J điện năng mỗi giây và chỉ phát ra 3 J quang năng. Hiệu suất phát quang của bóng đèn là:", [
        "5%",
        "95%",
        "50%",
        "10%"
    ], 0, "H = 3 / 60 = 5%."),
    make_mc(9, "Thông hiểu", "Khí thải CO2 sinh ra từ các nhà máy nhiệt điện đốt than gây ra hiện tượng:", [
        "Hiệu ứng nhà kính làm Trái Đất ấm lên",
        "Làm Trái Đất quay chậm lại",
        "Làm cạn kiệt tầng ozone vũ trụ",
        "Làm tăng lượng mưa đá"
    ], 0, "CO2 gây hiệu ứng nhà kính và biến đổi khí hậu."),
    make_mc(10, "Thông hiểu", "Tấm pin năng lượng mặt trời chuyển hóa trực tiếp dạng năng lượng nào thành điện năng?", [
        "Quang năng",
        "Nhiệt năng",
        "Cơ năng",
        "Hóa năng"
    ], 0, "Quang năng thành điện năng trực tiếp."),
    make_mc(11, "Thông hiểu", "Thiết bị điện nào sau đây có hiệu suất chuyển hóa năng lượng thành nhiệt năng có ích cao nhất?", [
        "Ấm đun nước siêu tốc",
        "Động cơ xe máy xăng",
        "Bóng đèn sợi đốt",
        "Máy hút bụi"
    ], 0, "Ấm siêu tốc có hiệu suất đạt ~95%."),
    make_mc(12, "Thông hiểu", "Động cơ vĩnh cửu không thể tồn tại trong thực tế vì:", [
        "Vi phạm định luật bảo toàn năng lượng",
        "Kim loại sắt thép quá nặng",
        "Trái Đất có từ trường",
        "Không khí quá lạnh"
    ], 0, "Động cơ vĩnh cửu vi phạm định luật bảo toàn năng lượng.")
]

p2_rev_t5 = [
    make_tf(1, "Thông hiểu", "Về các nguyên lý chuyển hóa năng lượng:", [
        ("a", "Năng lượng có thể chuyển hóa từ dạng này sang dạng khác.", True),
        ("b", "Trong mọi quá trình chuyển hóa luôn có năng lượng hao phí tỏa ra môi trường.", True),
        ("c", "Hiệu suất của máy móc thực tế có thể vượt quá 100%.", False),
        ("d", "Tổng năng lượng trong vũ trụ là một đại lượng được bảo toàn.", True)
    ], "Hiệu suất không bao giờ vượt quá 100%."),
    make_tf(2, "Thông hiểu", "Về các nguồn năng lượng sạch:", [
        ("a", "Điện mặt trời không phát thải khí nhà kính khi vận hành.", True),
        ("b", "Điện gió tận dụng nguồn năng lượng tự nhiên của luồng gió.", True),
        ("c", "Than đá là nguồn năng lượng tái tạo sạch.", False),
        ("d", "Khí sinh học Biogas tái tạo năng lượng từ chất thải chăn nuôi.", True)
    ], "Than đá là nhiên liệu hóa thạch không tái tạo và ô nhiễm môi trường."),
    make_tf(3, "Vận dụng", "Một động cơ điện tiêu thụ công suất 2 kW nâng một tải trọng 2500 N lên cao 12 m trong 20 giây:", [
        ("a", "Công có ích để nâng vật là 30.000 J (30 kJ).", True),
        ("b", "Điện năng toàn phần tiêu thụ là 40.000 J (40 kJ).", True),
        ("c", "Năng lượng hao phí do tỏa nhiệt là 10.000 J (10 kJ).", True),
        ("d", "Hiệu suất của động cơ nâng là 75%.", True)
    ], "A_ích = 2500 × 12 = 30.000 J. A_tp = 2000 × 20 = 40.000 J. H = 30.000 / 40.000 = 75%."),
    make_tf(4, "Vận dụng", "Một bình nóng lạnh tiêu thụ 1,5 kWh điện năng và cung cấp nhiệt lượng có ích là 4,86 MJ làm nóng nước (1 kWh = 3,6 MJ):", [
        ("a", "Điện năng toàn phần tiêu thụ là 5,4 MJ.", True),
        ("b", "Nhiệt lượng hao phí là 0,54 MJ.", True),
        ("c", "Hiệu suất đun nước của bình đạt 90%.", True),
        ("d", "Nếu giảm bớt lớp cách nhiệt của bình thì hiệu suất đun sẽ tăng lên.", False)
    ], "A_tp = 1,5 × 3,6 = 5,4 MJ. A_hp = 5,4 - 4,86 = 0,54 MJ. H = 4,86 / 5,4 = 90%. Giảm cách nhiệt làm tăng thất thoát nhiệt, giảm hiệu suất.")
]

p3_rev_t5 = [
    make_sa(1, "Thông hiểu", "Năng lượng gió là năng lượng tái tạo hay không tái tạo?", "Tái tạo", "Năng lượng tái tạo."),
    make_sa(2, "Thông hiểu", "Năng lượng địa nhiệt khai thác từ lòng đất là năng lượng tái tạo hay không tái tạo?", "Tái tạo", "Năng lượng địa nhiệt là năng lượng tái tạo."),
    make_sa(3, "Vận dụng", "Một động cơ điện tiêu thụ 1500 J điện năng sinh ra công có ích 1200 J. Hiệu suất của động cơ là bao nhiêu %?", "80", "1200 / 1500 = 80%."),
    make_sa(4, "Vận dụng", "Một tấm pin mặt trời nhận 4000 J quang năng và phát ra 800 J điện năng. Hiệu suất của pin là bao nhiêu %?", "20", "800 / 4000 = 20%."),
    make_sa(5, "Vận dụng cao", "Một máy bơm nước tiêu thụ công suất 1000 W hoạt động với hiệu suất 70%. Công suất có ích để bơm nước là bao nhiêu Watt?", "700", "1000 × 70% = 700 W."),
    make_sa(6, "Vận dụng cao", "Một nhà máy thủy điện có lưu lượng nước 30.000 kg/s qua cột nước cao 40 m (g = 10 m/s2). Hiệu suất nhà máy là 80%. Công suất phát điện là bao nhiêu Megawatt (MW)? (Lấy số thập phân)", "9.6", "P_tp = 30.000 × 10 × 40 = 12 MW. P_ích = 12 × 80% = 9,6 MW.")
]

p4_rev_t5 = [
    make_vdc(1, "Mục tiêu cam kết của Việt Nam tại COP26 đạt phát thải ròng bằng '0' (Net Zero) vào năm 2050 đòi hỏi giải pháp chuyển dịch năng lượng trọng tâm là:", [
        "Phát triển mạnh mẽ điện gió ngoài khơi, điện mặt trời và năng lượng hydro xanh thay thế nhiệt điện than",
        "Đốt than nhiều hơn",
        "Ngừng phát triển kinh tế",
        "Nhập khẩu toàn bộ điện năng từ nước ngoài"
    ], 0, "Chuyển dịch năng lượng xanh và Net Zero 2050."),
    make_vdc(2, "Xe ô tô điện (EV) có hiệu suất sử dụng năng lượng vượt trội xe chạy xăng truyền thống gấp 3 đến 4 lần là do:", [
        "Động cơ điện có tổn thất nhiệt rất nhỏ, trong khi động cơ xăng xả phần lớn nhiệt năng ra két nước và ống xả",
        "Xe điện không dùng pin",
        "Xe xăng chạy nhanh hơn",
        "Xe điện không chịu ma sát"
    ], 0, "Động cơ đốt trong thất thoát phần lớn nhiệt ra két nước và khí thải."),
    make_vdc(3, "Việc kết hợp sản xuất nông nghiệp công nghệ cao bên dưới các tấm pin mặt trời (mô hình Agrivoltaics) mang lại hiệu quả ưu việt là:", [
        "Vừa thu hoạch nông sản chất lượng cao vừa phát điện sạch, tối ưu hóa hiệu quả sử dụng đất",
        "Làm cây trồng ngừng quang hợp hoàn toàn",
        "Tăng lượng phân bón hóa học cần dùng",
        "Giảm diện tích đất canh tác xuống 0"
    ], 0, "Mô hình nông nghiệp kết hợp điện mặt trời tối ưu hóa sử dụng đất và tăng thu nhập kép."),
    make_vdc(4, "Tận dụng năng lượng biogas từ hầm ủ chất thải chăn nuôi lợn, bò ở nông thôn mang lại lợi ích kép là:", [
        "Cung cấp khí gas đun nấu miễn phí và xử lý triệt để ô nhiễm chất thải chăn nuôi",
        "Làm tăng lượng rác thải nông nghiệp",
        "Gây ô nhiễm đất canh tác",
        "Làm mất nguồn phân bón"
    ], 0, "Cung cấp năng lượng sạch và bảo vệ môi trường nông thôn.")
]

exams["phys9_c8_rev_test5"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 5, p1_rev_t5, p2_rev_t5, p3_rev_t5, p4_rev_t5)

print("Added phys9_c8_rev (5 tests).")
