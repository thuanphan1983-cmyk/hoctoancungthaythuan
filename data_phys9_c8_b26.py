# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 26: VÒNG NĂNG LƯỢNG TRÊN TRÁI ĐẤT. NĂNG LƯỢNG TÁI TẠO
Bao gồm 3 đề thi độc lập 100%: phys9_c8_b26_test1, phys9_c8_b26_test2, phys9_c8_b26_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c8"
CH_TITLE = "Chương VIII: Năng lượng và sự biến đổi năng lượng"

# =============================================================================
# BÀI 26: VÒNG NĂNG LƯỢNG TRÊN TRÁI ĐẤT. NĂNG LƯỢNG TÁI TẠO (3 ĐỀ)
# =============================================================================

# --- phys9_c8_b26_test1 ---
p1_b26_t1 = [
    make_mc(1, "Nhận biết", "Nguồn gốc ban đầu của hầu hết các dạng năng lượng trên Trái Đất (như gió, sóng biển, dòng chảy sông ngòi, nhiên liệu hóa thạch) bắt nguồn từ:", [
        "Năng lượng bức xạ phát ra từ Mặt Trời",
        "Năng lượng phóng xạ trong lòng đất",
        "Lực hút thủy triều của Mặt Trăng",
        "Gió bão vũ trụ"
    ], 0, "Bức xạ Mặt Trời là nguồn cội của hầu hết các dạng năng lượng trên Trái Đất."),
    make_mc(2, "Nhận biết", "Nguồn năng lượng nào sau đây là nguồn năng lượng tái tạo?", [
        "Năng lượng ánh sáng mặt trời, năng lượng gió, năng lượng thủy điện",
        "Than đá khai thác từ mỏ",
        "Dầu mỏ thô dưới lòng biển",
        "Khí thiên nhiên hóa lỏng"
    ], 0, "Năng lượng mặt trời, gió, thủy điện là năng lượng tái tạo sạch."),
    make_mc(3, "Nhận biết", "Nhiên liệu nào sau đây là nguồn năng lượng hóa thạch không thể tái tạo?", [
        "Than đá, dầu mỏ, khí đốt thiên nhiên",
        "Năng lượng sóng biển",
        "Năng lượng sinh khối rơm rạ",
        "Năng lượng địa nhiệt"
    ], 0, "Than đá, dầu mỏ, khí đốt hình thành hàng trăm triệu năm và không tái tạo."),
    make_mc(4, "Nhận biết", "Trong nhà máy thủy điện, dạng năng lượng nào của dòng nước được chuyển hóa thành điện năng?", [
        "Cơ năng (thế năng và động năng của dòng nước)",
        "Năng lượng hóa học",
        "Năng lượng nhiệt hạt nhân",
        "Năng lượng từ trường tự nhiên"
    ], 0, "Thế năng dòng nước chuyển thành động năng quay tuabin phát điện."),
    make_mc(5, "Nhận biết", "Nguồn năng lượng nào sau đây KHÔNG có nguồn gốc từ năng lượng Mặt Trời?", [
        "Năng lượng thủy triều và năng lượng địa nhiệt",
        "Năng lượng gió",
        "Năng lượng sinh khối",
        "Năng lượng than đá"
    ], 0, "Thủy triều sinh ra do lực hấp dẫn Mặt Trăng, địa nhiệt sinh ra từ lòng Trái Đất."),
    make_mc(6, "Nhận biết", "Pin mặt trời (pin quang điện) là thiết bị chuyển hóa trực tiếp:", [
        "Năng lượng ánh sáng thành năng lượng điện",
        "Nhiệt năng thành cơ năng",
        "Hóa năng thành quang năng",
        "Điện năng thành nhiệt năng"
    ], 0, "Pin quang điện chuyển trực tiếp quang năng thành điện năng."),
    make_mc(7, "Thông hiểu", "Việc lạm dụng đốt nhiên liệu hóa thạch (than đá, dầu mỏ) gây ra hậu quả môi trường nghiêm trọng nhất là:", [
        "Phát thải khí nhà kính CO2 làm biến đổi khí hậu toàn cầu và ô nhiễm không khí",
        "Làm Trái Đất quay chậm lại",
        "Làm cạn kiệt tầng nước ngầm",
        "Làm tăng lực hấp dẫn Trái Đất"
    ], 0, "Phát thải CO2 gây hiệu ứng nhà kính và biến đổi khí hậu toàn cầu."),
    make_mc(8, "Thông hiểu", "Tại sao năng lượng sinh khối (Biomass) từ bã mía, rơm rạ, trấu được xếp vào nhóm năng lượng tái tạo?", [
        "Vì cây trồng nông nghiệp liên tục được gieo trồng và thu hoạch bổ sung theo từng vụ mùa",
        "Vì sinh khối không bao giờ cháy hết",
        "Vì rơm rạ không chứa nguyên tố cacbon",
        "Vì sinh khối không tỏa nhiệt"
    ], 0, "Sinh khối được tái sinh liên tục theo các chu kỳ mùa vụ trồng trọt nông nghiệp."),
    make_mc(9, "Thông hiểu", "Tại Việt Nam, khu vực nào sau đây có tiềm năng phát triển điện gió ngoài khơi lớn nhất?", [
        "Vùng ven biển Nam Trung Bộ và Tây Nam Bộ",
        "Vùng trung du đồi núi Tây Bắc",
        "Vùng đồng bằng sông Hồng nội địa",
        "Các thung lũng kín gió ở Tây Nguyên"
    ], 0, "Ven biển Nam Trung Bộ và Tây Nam Bộ có gió biển mạnh quanh năm, tốc độ gió cao ổn định."),
    make_mc(10, "Thông hiểu", "Một tua bin điện gió biến đổi động năng của luồng gió thành điện năng với công suất phát điện phụ thuộc lớn nhất vào:", [
        "Tốc độ của luồng gió thổi qua cánh quạt",
        "Độ ẩm của không khí",
        "Màu sơn của tháp gió",
        "Nhiệt độ sôi của dầu bôi trơn"
    ], 0, "Công suất gió tỉ lệ với lũy thừa bậc ba của tốc độ gió (P tỉ lệ v^3)."),
    make_mc(11, "Thông hiểu", "Khí sinh học (Biogas) được sản xuất từ hầm ủ phân gia súc có thành phần cháy sinh nhiệt chính là:", [
        "Khí mêtan (CH4)",
        "Khí oxi (O2)",
        "Khí nitơ (N2)",
        "Khí cacbonic (CO2)"
    ], 0, "Biogas chứa 60-70% khí methane (CH4) là khí đốt sinh học cháy sạch."),
    make_mc(12, "Thông hiểu", "Cam kết của Việt Nam tại Hội nghị biến đổi khí hậu COP26 đạt mức phát thải ròng bằng '0' (Net Zero) vào năm:", [
        "Năm 2050",
        "Năm 2030",
        "Năm 2025",
        "Năm 2100"
    ], 0, "Việt Nam cam kết đạt phát thải ròng bằng '0' (Net Zero) vào năm 2050.")
]

p2_b26_t1 = [
    make_tf(1, "Thông hiểu", "Về vòng năng lượng trên Trái Đất:", [
        ("a", "Năng lượng bức xạ Mặt Trời cung cấp cho quá trình quang hợp của thực vật.", True),
        ("b", "Năng lượng Mặt Trời làm nước bốc hơi tạo thành mây mưa, duy trì dòng chảy thủy điện.", True),
        ("c", "Than đá và dầu mỏ thực chất là năng lượng mặt trời được tích trữ cổ đại dạng hóa năng.", True),
        ("d", "Tất cả các dạng năng lượng trên Trái Đất đều có nguồn gốc từ năng lượng gió.", False)
    ], "Gió cũng là sản phẩm do Mặt Trời làm nóng không khí không đều sinh ra."),
    make_tf(2, "Thông hiểu", "Về năng lượng tái tạo và phát triển bền vững:", [
        ("a", "Năng lượng gió và năng lượng mặt trời không phát thải khí nhà kính khi vận hành.", True),
        ("b", "Nguồn năng lượng hóa thạch sẽ cạn kiệt trong tương lai gần nếu tiếp tục khai thác quá mức.", True),
        ("c", "Năng lượng tái tạo hoàn toàn không phụ thuộc vào điều kiện thời tiết tự nhiên.", False),
        ("d", "Việt Nam có tiềm năng rất lớn về phát triển điện mặt trời và điện gió ngoài khơi.", True)
    ], "Năng lượng mặt trời và gió phụ thuộc nhiều vào thời tiết (nắng, mây, tốc độ gió)."),
    make_tf(3, "Vận dụng", "Một trang trại bò sữa xây dựng hầm ủ Biogas thể tích 100 m3 để xử lý chất thải chăn nuôi:", [
        ("a", "Chất thải hữu cơ được vi khuẩn yếm khí phân hủy sinh ra khí Biogas.", True),
        ("b", "Khí Biogas được dẫn lên bếp làm nhiên liệu đun nấu và chạy máy phát điện.", True),
        ("c", "Giải pháp này giúp giảm mùi hôi thối và ngăn ngừa khí mêtan phát thải tự do vào khí quyển.", True),
        ("d", "Nước thải sau hầm biogas không thể dùng làm phân bón hữu cơ cho đồng cỏ.", False)
    ], "Nước xả sau ủ biogas là phân bón hữu cơ lỏng giàu dinh dưỡng rất tốt cho cây trồng."),
    make_tf(4, "Vận dụng", "Một nhà máy điện mặt trời có công suất lắp đặt 50 MW hoạt động trung bình 5 giờ nắng hiệu quả mỗi ngày:", [
        ("a", "Sản lượng điện tạo ra trong 1 ngày là 250 MWh (250.000 kWh).", True),
        ("b", "Vào ban đêm, nhà máy vẫn tự phát điện mặt trời với công suất 50 MW bình thường.", False),
        ("c", "Để cung cấp điện ổn định ban đêm, cần kết hợp hệ thống pin lưu trữ năng lượng (BESS).", True),
        ("d", "Nhà máy điện mặt trời này giúp giảm lượng lớn than đá đốt ở các nhà máy nhiệt điện.", True)
    ], "Ban đêm không có ánh sáng mặt trời nên pin quang điện không phát ra điện năng.")
]

p3_b26_t1 = [
    make_sa(1, "Thông hiểu", "Năng lượng gió là năng lượng tái tạo hay không tái tạo?", "Tái tạo", "Năng lượng tái tạo."),
    make_sa(2, "Thông hiểu", "Thành phần khí cháy chủ yếu trong hầm Biogas là khí gì?", "Metan", "Khí metan (CH4)."),
    make_sa(3, "Vận dụng", "Việt Nam cam kết đạt mức phát thải ròng bằng '0' (Net Zero) vào năm nào?", "2050", "Năm 2050."),
    make_sa(4, "Vận dụng", "Một tuabin gió phát ra công suất 2 MW trong 10 giờ. Điện năng sinh ra là bao nhiêu MWh?", "20", "A = 2 MW × 10 h = 20 MWh."),
    make_sa(5, "Vận dụng cao", "Một gia đình lắp pin mặt trời công suất 3 kW. Trung bình mỗi ngày có 4 giờ nắng. Trong 30 ngày của một tháng, hệ thống sinh ra bao nhiêu kWh điện?", "360", "A = 3 kW × 4 h/ngày × 30 ngày = 360 kWh."),
    make_sa(6, "Vận dụng cao", "Một nhà máy thủy điện có cột nước cao 50 m. Khối lượng nước qua tuabin là 40.000 kg mỗi giây. Lấy g = 10 m/s2. Thế năng trọng trường của lượng nước này trong 1 giây là bao nhiêu MegaJun (MJ)?", "20", "E = m × g × h = 40.000 × 10 × 50 = 20.000.000 J = 20 MJ.")
]

p4_b26_t1 = [
    make_vdc(1, "Mô hình thủy điện tích năng (Pumped Storage Hydropower): Vào ban đêm khi nhu cầu tiêu thụ điện thấp và giá điện rẻ (giờ thấp điểm), người ta dùng điện dư thừa từ phong điện để bơm nước từ hồ dưới lên hồ chứa trên đỉnh núi cao. Vào ban ngày khi nhu cầu điện đạt đỉnh (giờ cao điểm), nước từ hồ trên được xả qua tuabin phát điện cấp vào lưới. Vai trò chiến lược của nhà máy thủy điện tích năng là:", [
        "Hoạt động như một 'viên pin khổng lồ' lưu trữ năng lượng cơ học sạch, giúp ổn định và cân bằng tần số lưới điện quốc gia",
        "Làm tăng lượng mưa tự nhiên cho cả vùng",
        "Lọc sạch nước uống cho toàn thành phố",
        "Tạo ra sóng thần nhân tạo"
    ], 0, "Thủy điện tích năng là công nghệ lưu trữ năng lượng quy mô lưới lớn nhất thế giới, nạp điện lúc thừa và phát điện lúc thiếu."),
    make_vdc(2, "Hiện tượng hiệu ứng nhà kính nhân tạo làm Trái Đất nóng lên: Khí CO2 sinh ra từ đốt than đá và xăng dầu tích tụ trong khí quyển hoạt động như thế nào đối với bức xạ nhiệt?", [
        "Cho ánh sáng mặt trời truyền qua chiếu xuống mặt đất, nhưng hấp thụ mạnh bức xạ nhiệt hồng ngoại từ mặt đất phát ngược lên và giữ lại làm nóng tầng đối lưu",
        "Phản xạ 100% ánh sáng mặt trời quay lại vũ trụ",
        "Làm mất hoàn toàn từ trường Trái Đất",
        "Hút sạch khí oxi trong bầu khí quyển"
    ], 0, "Khí nhà kính giữ lại bức xạ nhiệt sóng dài của bề mặt Trái Đất, làm tăng nhiệt độ trung bình toàn cầu."),
    make_vdc(3, "Công nghệ sản xuất 'Hydro xanh' (Green Hydrogen) từ năng lượng tái tạo: Người ta dùng nguồn điện dư thừa từ điện gió ngoài khơi và điện mặt trời để điện phân nước biển thành khí hydro (H2) và oxy (O2). Khí hydro sau đó được dùng làm nhiên liệu cho xe tải nặng và luyện kim xanh. Vì sao loại hydro này được gọi là 'Hydro xanh'?", [
        "Vì toàn bộ quy trình sản xuất sử dụng 100% năng lượng tái tạo sạch và hoàn toàn không phát thải khí nhà kính CO2",
        "Vì khí hydro có màu xanh lá cây rực rỡ",
        "Vì hydro được chiết xuất từ lá cây xanh",
        "Vì hydro hòa tan trong nước biển làm nước đổi màu xanh"
    ], 0, "Hydro xanh (Green H2) được điện phân hoàn toàn bằng năng lượng tái tạo, không phát thải carbon trong toàn chuỗi."),
    make_vdc(4, "Một ngôi nhà năng lượng số không (Net Zero Energy Building): Mái nhà lợp ngói pin mặt trời tạo ra 8000 kWh điện mỗi năm. Cả năm ngôi nhà tiêu thụ 6500 kWh điện cho sinh hoạt và nạp xe điện. Lượng điện dư thừa 1500 kWh được bán ngược lên lưới điện. Điều này chứng minh rằng:", [
        "Ngôi nhà tự chủ hoàn toàn về năng lượng sạch và trở thành nguồn cung cấp điện năng ròng cho cộng đồng",
        "Ngôi nhà không hề dùng bất kỳ thiết bị điện nào",
        "Ngôi nhà làm giảm nhiệt độ của Mặt Trời",
        "Ngôi nhà vi phạm định luật bảo toàn năng lượng"
    ], 0, "Net Zero Building tự sản xuất năng lượng tái tạo vượt quá nhu cầu tiêu thụ trong cả năm, trung hòa phát thải carbon.")
]

exams["phys9_c8_b26_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c8_b26", "Bài 26: Vòng năng lượng trên Trái Đất. Năng lượng tái tạo", 1, p1_b26_t1, p2_b26_t1, p3_b26_t1, p4_b26_t1)

# --- phys9_c8_b26_test2 ---
p1_b26_t2 = [
    make_mc(1, "Nhận biết", "Nguồn năng lượng nào sau đây được bổ sung liên tục từ các quá trình tự nhiên và không bao giờ cạn kiệt?", [
        "Năng lượng tái tạo",
        "Nhiên liệu hóa thạch",
        "Năng lượng than bùn",
        "Quặng uranium nguyên chất"
    ], 0, "Năng lượng tái tạo tự bổ sung liên tục từ thiên nhiên."),
    make_mc(2, "Nhận biết", "Năng lượng địa nhiệt là nguồn năng lượng được khai thác từ:", [
        "Nhiệt lượng tỏa ra từ sâu trong lòng đất",
        "Ánh nắng mặt trời rọi trên mặt đất",
        "Gió thổi trên các đồi cao",
        "Sóng đánh vào bờ biển"
    ], 0, "Địa nhiệt là nhiệt lượng tự nhiên từ tâm lòng Trái Đất."),
    make_mc(3, "Nhận biết", "Dạng năng lượng tích trữ trong than đá và dầu mỏ là:", [
        "Hóa năng",
        "Cơ năng",
        "Nhiệt năng",
        "Năng lượng nguyên tử"
    ], 0, "Nhiên liệu hóa thạch tích trữ hóa năng trong các liên kết hóa học cacbon-hydro."),
    make_mc(4, "Nhận biết", "Năng lượng gió sinh ra từ chuyển động của các khối không khí do:", [
        "Mặt Trời đốt nóng bầu khí quyển không đồng đều giữa các vùng",
        "Trái Đất quay ngược chiều kim đồng hồ",
        "Thủy triều lên xuống ở biển",
        "Các nhà máy nhiệt điện phả khói"
    ], 0, "Mặt Trời hun nóng bề mặt Trái Đất không đều tạo chênh lệch áp suất sinh ra gió."),
    make_mc(5, "Nhận biết", "Nguồn năng lượng nào sau đây sinh ra do lực hấp dẫn giữa Mặt Trăng, Mặt Trời và Trái Đất?", [
        "Năng lượng thủy triều",
        "Năng lượng mặt trời",
        "Năng lượng gió",
        "Năng lượng sinh khối"
    ], 0, "Thủy triều sinh ra do lực hút hấp dẫn của Mặt Trăng và Mặt Trời."),
    make_mc(6, "Nhận biết", "Chất khí nào sau đây phát thải chủ yếu từ ống xả xe chạy xăng dầu gây hiệu ứng nhà kính?", [
        "Khí cacbon đioxit (CO2)",
        "Khí nitơ (N2)",
        "Khí oxi (O2)",
        "Khí hiđro (H2)"
    ], 0, "Đốt cháy xăng dầu thải CO2 là khí nhà kính chính."),
    make_mc(7, "Thông hiểu", "Tại sao năng lượng hạt nhân phân hạch uranium KHÔNG được xếp vào nhóm năng lượng tái tạo?", [
        "Vì quặng uranium trong vỏ Trái Đất có trữ lượng hữu hạn và không thể tự sinh sôi tái tạo",
        "Vì năng lượng hạt nhân không sinh ra nhiệt",
        "Vì hạt nhân không có khối lượng",
        "Vì hạt nhân không dẫn điện"
    ], 0, "Uranium là khoáng sản hữu hạn, cạn kiệt dần theo khai thác nên không tái tạo."),
    make_mc(8, "Thông hiểu", "Nhược điểm lớn nhất của năng lượng điện mặt trời và điện gió là:", [
        "Tính gián đoạn (chập chờn) và phụ thuộc lớn vào thời tiết, ngày đêm",
        "Phát thải quá nhiều khí CO2 độc hại",
        "Tạo ra bụi mịn gây ung thư",
        "Làm tăng nhiệt độ lõi Trái Đất"
    ], 0, "Điện mặt trời và gió gián đoạn theo thời tiết (ban đêm không có nắng, lúc lặng gió)."),
    make_mc(9, "Thông hiểu", "Hệ sinh thái rừng mưa nhiệt đới hấp thụ khí CO2 và thải ra khí O2 nhờ năng lượng nào?", [
        "Năng lượng ánh sáng Mặt Trời qua quá trình quang hợp",
        "Nhiệt năng trong lòng đất",
        "Năng lượng sóng biển",
        "Năng lượng từ trường Trái Đất"
    ], 0, "Quang hợp hấp thụ quang năng Mặt Trời chuyển hóa thành hóa năng trong cây cối."),
    make_mc(10, "Thông hiểu", "Sử dụng bình nước nóng năng lượng mặt trời (thái dương năng) trên mái nhà giúp gia đình:", [
        "Tiết kiệm điện năng đun nước và bảo vệ môi trường",
        "Tăng hóa đơn tiền điện",
        "Làm nhà bị nóng bức",
        "Tạo ra tiếng ồn lớn"
    ], 0, "Thái dương năng hấp thụ trực tiếp nhiệt mặt trời đun nước, tiết kiệm điện 100% ban ngày."),
    make_mc(11, "Thông hiểu", "Quá trình nào sau đây giải phóng năng lượng sạch không phát thải khí nhà kính?", [
        "Tua bin gió quay máy phát điện",
        "Đốt than đá trong nhà máy nhiệt điện",
        "Đốt rác thải nhựa ngoài trời",
        "Chạy động cơ diesel tàu thủy"
    ], 0, "Điện gió không phát thải khí nhà kính."),
    make_mc(12, "Thông hiểu", "Để chuyển đổi xanh ngành giao thông vận tải, phương án thay thế xe chạy xăng dầu được ưu tiên phát triển hàng đầu hiện nay là:", [
        "Xe ô tô điện (EV) và xe buýt điện",
        "Xe chạy bằng than đá",
        "Xe chạy bằng củi khô",
        "Xe chạy bằng dầu nhớt thải"
    ], 0, "Xe điện sử dụng pin sạc không phát thải khí xả tại chỗ, giảm thiểu ô nhiễm không khí đô thị.")
]

p2_b26_t2 = [
    make_tf(1, "Thông hiểu", "Về các nguồn năng lượng trên Trái Đất:", [
        ("a", "Nhiên liệu hóa thạch tích tụ năng lượng từ tàn dư sinh vật qua hàng triệu năm.", True),
        ("b", "Năng lượng gió là một dạng năng lượng phái sinh từ năng lượng Mặt Trời.", True),
        ("c", "Tất cả các nguồn năng lượng tái tạo đều không gây bất kỳ tác động môi trường nào.", False),
        ("d", "Năng lượng địa nhiệt có nguồn gốc từ bên trong Trái Đất chứ không bắt nguồn từ Mặt Trời.", True)
    ], "Xây đập thủy điện lớn có thể ảnh hưởng sinh thái hạ lưu và rừng, điện mặt trời cần xử lý pin thải sau 25 năm."),
    make_tf(2, "Thông hiểu", "Về năng lượng sạch và phát triển bền vững:", [
        ("a", "Năng lượng tái tạo giúp giảm phụ thuộc vào nhập khẩu nhiên liệu hóa thạch.", True),
        ("b", "Năng lượng mặt trời có thể chuyển hóa thành điện năng nhờ pin quang điện.", True),
        ("c", "Than đá là nguồn năng lượng tái tạo vô tận.", False),
        ("d", "Khí sinh học Biogas tận dụng chất thải chăn nuôi tạo ra năng lượng đun nấu hữu ích.", True)
    ], "Than đá là nhiên liệu hóa thạch không tái tạo và sẽ cạn kiệt."),
    make_tf(3, "Vận dụng", "Một tuabin gió có công suất định mức 3 MW. Khi tốc độ gió đạt chuẩn, tuabin hoạt động liên tục trong 8 giờ:", [
        ("a", "Điện năng tuabin phát ra trong 8 giờ là 24 MWh (24.000 kWh).", True),
        ("b", "Lượng điện này đủ cung cấp cho khoảng 2400 hộ gia đình tiêu thụ 10 kWh/ngày.", True),
        ("c", "Nếu tốc độ gió giảm xuống 0 (lặng gió hoàn toàn) thì tuabin vẫn tự phát ra 3 MW điện.", False),
        ("d", "Điện gió giúp giảm bớt lượng phát thải khí CO2 so với đốt than.", True)
    ], "Lặng gió thì tuabin dừng quay, công suất phát bằng 0."),
    make_tf(4, "Vận dụng", "Gia đình lắp một bình thái dương năng dung tích 200 lít trên mái nhà hấp thụ 15 MJ nhiệt năng từ Mặt Trời mỗi ngày:", [
        ("a", "Nhiệt năng làm nóng 200 lít nước dùng cho tắm giặt sinh hoạt.", True),
        ("b", "Lượng nhiệt 15 MJ tương đương khoảng 4,17 kWh điện năng nếu dùng bình nóng lạnh điện.", True),
        ("c", "Vào những ngày mưa bão kéo dài nhiều ngày, nhiệt độ nước trong bình vẫn sôi 100 độ C.", False),
        ("d", "Vào ngày mưa phùn không có nắng, cần dùng thêm thanh điện trở hỗ trợ phụ trợ.", True)
    ], "15.000.000 J / 3.600.000 J/kWh ≈ 4,17 kWh. Mưa kéo dài thì nhiệt độ nước giảm dần theo thời tiết.")
]

p3_b26_t2 = [
    make_sa(1, "Thông hiểu", "Năng lượng thủy triều sinh ra do lực hấp dẫn của thiên thể nào với Trái Đất?", "Mặt Trăng", "Mặt Trăng (và Mặt Trời)."),
    make_sa(2, "Thông hiểu", "Khí CO2 là nguyên nhân chính gây ra hiện tượng gì làm nóng khí quyển toàn cầu?", "Hiệu ứng nhà kính", "Hiệu ứng nhà kính."),
    make_sa(3, "Vận dụng", "Một tấm pin mặt trời diện tích 2 m2 nhận bức xạ 1000 W/m2. Tổng công suất ánh sáng chiếu vào tấm pin là bao nhiêu Watt?", "2000", "P = 2 × 1000 = 2000 W."),
    make_sa(4, "Vận dụng", "Một bóng đèn LED 20 W thay thế bóng đèn sợi đốt 100 W cùng độ sáng. Công suất tiết kiệm được là bao nhiêu Watt?", "80", "100 - 20 = 80 W."),
    make_sa(5, "Vận dụng cao", "Một gia đình tiết kiệm được 3 kWh điện mỗi ngày nhờ dùng đèn LED và thái dương năng. Trong 30 ngày, gia đình tiết kiệm được bao nhiêu kWh điện?", "90", "3 × 30 = 90 kWh."),
    make_sa(6, "Vận dụng cao", "Một tuabin điện gió có công suất 2,5 MW chạy trong 6 giờ. Điện năng sinh ra là bao nhiêu MWh?", "15", "2,5 × 6 = 15 MWh.")
]

p4_b26_t2 = [
    make_vdc(1, "Trong chiến lược an ninh năng lượng quốc gia, việc kết hợp điện mặt trời nổi trên mặt hồ thủy điện (Floating Solar) mang lại lợi ích kép đặc biệt là:", [
        "Tận dụng diện tích mặt nước không tốn đất nông nghiệp, mặt nước làm mát tấm pin tăng hiệu suất phát điện và giảm bốc hơi nước của hồ thủy điện",
        "Làm nước hồ đóng băng thành tuyết",
        "Làm tăng độ sâu đáy hồ lên gấp đôi",
        "Triệt tiêu hoàn toàn gió bão"
    ], 0, "Pin mặt trời nổi giảm diện tích đất chiếm dụng, nước làm mát tăng hiệu suất pin quang điện 5-10% và giảm tổn thất bốc hơi nước hồ."),
    make_vdc(2, "Tại sao các cánh tuabin gió hiện đại có chiều dài lên tới 80 - 100 mét được chế tạo bằng vật liệu composite sợi carbon hoặc sợi thủy tinh siêu nhẹ thay vì làm bằng thép kim loại?", [
        "Vật liệu composite có độ bền cơ học cực cao, chịu mỏi tốt, không bị rỉ sét do muối biển và khối lượng nhẹ giúp giảm tải trọng cho trụ tháp",
        "Vật liệu composite tự phát ra điện khi quay",
        "Composite rẻ hơn đất sét",
        "Composite hút gió nhanh hơn thép"
    ], 0, "Composite sợi thủy tinh/carbon nhẹ, cứng cáp, chống ăn mòn gió muối biển và chịu được tải trọng uốn mỏi hàng chục năm."),
    make_vdc(3, "Hệ thống điện rác (Waste-to-Energy) tại các thành phố lớn đốt rác thải sinh hoạt trong lò đốt nhiệt độ cao (trên 1000 độ C) để tạo hơi nước quay tuabin phát điện. Lợi ích quan trọng nhất của nhà máy điện rác là:", [
        "Giải quyết triệt để ô nhiễm rác thải đô thị, giảm 90-95% thể tích chôn lấp và tận dụng thu hồi điện năng",
        "Làm rác biến thành kim cương",
        "Tạo ra phân bón hạt nhân",
        "Hút sạch mây mưa trên bầu trời"
    ], 0, "Điểm rác biến rác thải thành năng lượng hữu ích, giải quyết bài toán khủng hoảng đất chôn lấp rác tại các đô thị lớn."),
    make_vdc(4, "Một trang trại nông nghiệp công nghệ cao kết hợp mô hình nông nghiệp - điện mặt trời (Agrivoltaics): Các tấm pin mặt trời lắp đặt trên khung cao 3 mét có khe hở vừa phải che bóng mát cho cây trồng ưa bóng (như nấm, dược liệu, rau xanh) phía dưới. Mô hình này giúp:", [
        "Tối ưu hóa hiệu quả sử dụng đất, vừa thu hoạch nông sản chất lượng cao vừa sản xuất điện sạch tự tiêu thụ và bán điện",
        "Cây trồng không cần tưới nước vẫn sống",
        "Đất tự sinh ra phân đạm hóa học",
        "Biến trang trại thành mỏ than đá"
    ], 0, "Mô hình kết hợp Agrivoltaics tối ưu đất đa mục đích, điều hòa nhiệt độ đất cho cây ưa bóng và tạo nguồn thu điện sạch ổn định.")
]

exams["phys9_c8_b26_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c8_b26", "Bài 26: Vòng năng lượng trên Trái Đất. Năng lượng tái tạo", 2, p1_b26_t2, p2_b26_t2, p3_b26_t2, p4_b26_t2)

# --- phys9_c8_b26_test3 ---
p1_b26_t3 = [
    make_mc(1, "Nhận biết", "Quá trình hình thành than đá và dầu mỏ từ xác thực vật, vi sinh vật cổ đại bị chôn vùi dưới lòng đất diễn ra trong thời gian khoảng:", [
        "Hàng trăm triệu năm",
        "Vài tuần lễ",
        "Vài tháng",
        "Khoảng mười năm"
    ], 0, "Nhiên liệu hóa thạch cần hàng trăm triệu năm biến đổi địa chất dưới áp suất và nhiệt độ cao."),
    make_mc(2, "Nhận biết", "Nguồn năng lượng nào sau đây được coi là năng lượng sạch vì không phát thải khói bụi và khí độc khi phát điện?", [
        "Năng lượng mặt trời và năng lượng gió",
        "Đốt than cám",
        "Đốt dầu FO công nghiệp",
        "Đốt củi rừng tự nhiên"
    ], 0, "Mặt trời và gió không phát thải khói bụi ô nhiễm."),
    make_mc(3, "Nhận biết", "Trong các nguồn năng lượng sau, nguồn nào KHÔNG tái tạo?", [
        "Dầu mỏ",
        "Thủy điện",
        "Năng lượng gió",
        "Năng lượng mặt trời"
    ], 0, "Dầu mỏ là tài nguyên hóa thạch không tái tạo."),
    make_mc(4, "Nhận biết", "Năng lượng sinh khối (Biomass) có thể thu nhận từ nguồn nào sau đây?", [
        "Gỗ vụn, bã mía, rơm rạ, vỏ trấu, chất thải hữu cơ",
        "Quặng sắt phế liệu",
        "Cát biển thạch anh",
        "Nước cất tinh khiết"
    ], 0, "Sinh khối lấy từ phụ phẩm nông lâm nghiệp và chất thải hữu cơ."),
    make_mc(5, "Nhận biết", "Năng lượng sóng biển sinh ra chủ yếu do tác động của:", [
        "Gió thổi trên mặt biển",
        "Tàu thuyền qua lại",
        "Cá bơi dưới nước",
        "Bụi vũ trụ rơi xuống biển"
    ], 0, "Gió thổi trên mặt đại dương tạo nên sóng biển."),
    make_mc(6, "Nhận biết", "Sử dụng nguồn năng lượng tái tạo thay thế nhiên liệu hóa thạch là giải pháp cấp bách nhằm:", [
        "Ngăn chặn biến đổi khí hậu và bảo vệ môi trường Trái Đất",
        "Làm tăng lượng rác thải công nghiệp",
        "Làm cạn kiệt oxy vũ trụ",
        "Làm tăng chi phí y tế cộng đồng"
    ], 0, "Chuyển dịch năng lượng xanh giúp giảm biến đổi khí hậu và ô nhiễm môi trường sống."),
    make_mc(7, "Thông hiểu", "Một tấm pin năng lượng mặt trời nhận quang năng từ Mặt Trời và chuyển hóa thành điện năng với hiệu suất khoảng 20%. Điều này có nghĩa là:", [
        "Cứ 100 J quang năng chiếu vào thì tạo ra được 20 J điện năng có ích",
        "Cứ 100 J quang năng chiếu vào tạo ra 80 J điện năng",
        "Tấm pin chỉ hấp thụ được 20 hạt photon",
        "Tấm pin tỏa nhiệt 20%"
    ], 0, "Hiệu suất 20% nghĩa là chuyển hóa 20% năng lượng photon thành điện năng."),
    make_mc(8, "Thông hiểu", "Tại sao việc phá rừng đầu nguồn làm suy giảm nghiêm trọng tiềm năng phát điện của các nhà máy thủy điện?", [
        "Làm mất khả năng giữ nước, gây lũ quét mùa mưa và cạn kiệt dòng chảy mùa khô, đồng thời đất đá bồi lắng lòng hồ",
        "Rừng cây cản trở đường dây điện 500 kV",
        "Rừng cây tự hút hết nước trong hồ chứa",
        "Lá cây rơi làm nước biến thành axit"
    ], 0, "Mất rừng làm mất điều hòa nguồn nước, gây xói mòn bồi lấp dung tích hồ thủy điện."),
    make_mc(9, "Thông hiểu", "Xe ô tô chạy bằng pin nhiên liệu hydro (FCEV) xả ra môi trường chất thải duy nhất là:", [
        "Hơi nước tinh khiết (H2O)",
        "Khí CO2 và khói đen",
        "Khí SO2 gây mưa axit",
        "Bụi chì độc hại"
    ], 0, "Phản ứng 2H2 + O2 -> 2H2O sinh điện năng, khí thải duy nhất là hơi nước sạch."),
    make_mc(10, "Thông hiểu", "Năng lượng địa nhiệt được khai thác hiệu quả nhất tại các khu vực nào trên thế giới?", [
        "Vùng có hoạt động núi lửa hoặc suối nước nóng ngầm",
        "Các đảo băng trôi Bắc Cực",
        "Vùng sa mạc cát khô cằn",
        "Đáy rãnh đại dương sâu thẳm"
    ], 0, "Khu vực địa nhiệt tự nhiên gần nguồn magma núi lửa có hơi nước nóng ngầm nhiệt độ cao."),
    make_mc(11, "Thông hiểu", "Hành động nào sau đây của mỗi học sinh góp phần trực tiếp bảo vệ năng lượng và môi trường?", [
        "Tắt đèn, quạt khi rời khỏi phòng học và tận dụng ánh sáng tự nhiên",
        "Bật điều hòa ở mức 16 độ C và mở toang cửa sổ",
        "Vứt rác bừa bãi ra sân trường",
        "Để vòi nước chảy tự do cả ngày"
    ], 0, "Tắt thiết bị điện không dùng và tận dụng ánh sáng tự nhiên tiết kiệm điện năng."),
    make_mc(12, "Thông hiểu", "Chỉ số phát thải ròng bằng '0' (Net Zero) nghĩa là:", [
        "Lượng khí nhà kính phát thải vào khí quyển bằng lượng khí nhà kính được hấp thụ hoặc thu gom triệt tiêu",
        "Cấm hoàn toàn việc sử dụng điện năng trên toàn cầu",
        "Nhiệt độ Trái Đất bằng đúng 0 độ C",
        "Không có con người sinh sống"
    ], 0, "Net Zero là trạng thái cân bằng: phát thải bằng lượng hấp thụ (qua rừng, công nghệ thu giữ carbon CCS).")
]

p2_b26_t3 = [
    make_tf(1, "Thông hiểu", "Về chu trình năng lượng tự nhiên trên hành tinh:", [
        ("a", "Mặt Trời truyền năng lượng tới Trái Đất dưới dạng bức xạ điện từ (sóng ánh sáng).", True),
        ("b", "Năng lượng Mặt Trời tạo ra các hoàn lưu khí quyển sinh ra gió trên biển và đất liền.", True),
        ("c", "Than đá có thể tái tạo lại chỉ sau vài năm chôn lấp rác.", False),
        ("d", "Năng lượng sóng biển có mật độ năng lượng tập trung cao ở các bờ biển lộng gió.", True)
    ], "Than đá cần hàng trăm triệu năm địa chất để hình thành, không thể tái tạo trong vài năm."),
    make_tf(2, "Thông hiểu", "Về sử dụng năng lượng tiết kiệm và chuyển dịch năng lượng xanh:", [
        ("a", "Đèn LED tiêu thụ ít điện năng hơn nhiều so với đèn sợi đốt cùng độ sáng.", True),
        ("b", "Xe buýt điện giúp giảm thiểu ô nhiễm khói bụi tại các đô thị đông đúc.", True),
        ("c", "Nhà máy nhiệt điện than sạch hơn nhà máy điện gió.", False),
        ("d", "Trồng cây gây rừng giúp hấp thụ khí CO2 và làm mát vi khí hậu.", True)
    ], "Nhiệt điện than phát thải CO2 lớn và ô nhiễm bụi xỉ than, điện gió sạch hơn nhiều."),
    make_tf(3, "Vận dụng", "Một hộ gia đình lắp hệ thống pin mặt trời áp mái 4 kWp tạo ra 16 kWh điện mỗi ngày:", [
        ("a", "Sản lượng điện trong 1 tháng (30 ngày) là 480 kWh.", True),
        ("b", "Nếu gia đình dùng hết 300 kWh/tháng thì lượng điện thừa phát lên lưới là 180 kWh.", True),
        ("c", "Hệ thống pin mặt trời này phát huy hiệu quả cao nhất vào ban ngày có nắng gắt.", True),
        ("d", "Vào những ngày trời râm mát có mây, pin mặt trời hoàn toàn không tạo ra chút điện nào.", False)
    ], "Trời râm mát vẫn có bức xạ tán xạ khuếch tán nên pin vẫn sinh điện ở mức 20-40% công suất."),
    make_tf(4, "Vận dụng", "Một tuabin điện gió ngoài khơi có công suất định mức 5 MW:", [
        ("a", "Khi chạy hết công suất trong 10 giờ, tuabin sinh ra 50 MWh điện.", True),
        ("b", "Gió biển ngoài khơi thổi mạnh và ổn định hơn so với gió trên đất liền.", True),
        ("c", "Chi phí lắp đặt móng trụ tuabin ngoài biển thấp hơn nhiều so với trên đất liền.", False),
        ("d", "Tuabin điện gió ngoài khơi không chiếm dụng đất canh tác nông nghiệp trên bờ liền.", True)
    ], "Móng trụ ngoài biển chịu sóng gió phức tạp nên chi phí thi công cao hơn nhiều so với đất liền.")
]

p3_b26_t3 = [
    make_sa(1, "Thông hiểu", "Nguồn năng lượng nào là cội nguồn của hầu hết năng lượng trên Trái Đất?", "Mặt Trời", "Mặt Trời."),
    make_sa(2, "Thông hiểu", "Xe ô tô điện viết tắt bằng tiếng Anh là gì?", "EV", "EV (Electric Vehicle)."),
    make_sa(3, "Vận dụng", "Một nhà máy điện mặt trời có công suất 100 MW. Trong 4 giờ nắng hiệu quả, nhà máy phát ra bao nhiêu MWh điện?", "400", "100 × 4 = 400 MWh."),
    make_sa(4, "Vận dụng", "Nếu thay 5 bóng đèn sợi đốt 60W bằng 5 bóng đèn LED 10W thì công suất tiết kiệm được là bao nhiêu Watt?", "250", "(60 - 10) × 5 = 50 × 5 = 250 W."),
    make_sa(5, "Vận dụng cao", "Một gia đình thay bếp gas bằng bếp từ và pin mặt trời, giảm phát thải 2 kg CO2 mỗi ngày. Trong 365 ngày của 1 năm, gia đình giảm phát thải bao nhiêu kg CO2?", "730", "2 × 365 = 730 kg CO2."),
    make_sa(6, "Vận dụng cao", "Một cột nước thủy điện cao 60 m có lưu lượng nước 50 m3/s (50.000 kg/s). Lấy g = 10 m/s2. Công suất thế năng toàn phần của dòng nước là bao nhiêu Megawatt (MW)?", "30", "P = m × g × h / t = 50.000 × 10 × 60 = 30.000.000 W = 30 MW.")
]

p4_b26_t3 = [
    make_vdc(1, "Công nghệ đập thủy triều hai chiều (Tidal Barrage): Tại cửa sông có biên độ thủy triều lớn (như nhà máy thủy triều Rance ở Pháp), đập ngăn giữ nước biển khi triều lên rồi xả nước khi triều xuống qua các tuabin hai chiều để phát điện. Điểm ưu việt tuyệt đối của năng lượng thủy triều so với điện gió và điện mặt trời là:", [
        "Tính chu kỳ hoàn toàn dự báo chuẩn xác được trước hàng trăm năm theo lịch thiên văn chu kỳ quay của Mặt Trăng mà không bị chi phối bởi mây mưa thất thường",
        "Nước biển tự biến thành nước ngọt",
        "Thủy triều không bao giờ ngừng lên xuống trong ngày",
        "Đập thủy triều ngăn được bão cấp 20"
    ], 0, "Thủy triều dự báo chính xác 100% theo thiên văn học Mặt Trăng, không phụ thuộc vào mây mù hay tốc độ gió."),
    make_vdc(2, "Hệ thống lưu trữ năng lượng pin Lithium công quy mô lưới điện (BESS - Battery Energy Storage System): Tại các trung tâm tích hợp năng lượng tái tạo lớn, các container chứa hàng nghìn khối pin lưu trữ BESS được lắp đặt để:", [
        "Sạc điện tích trữ vào ban ngày khi điện mặt trời dư thừa công suất phát và xả điện nhanh chóng lên lưới vào ban đêm (giờ cao điểm 18h - 21h) để chống quá tải lưới điện",
        "Biến năng lượng điện thành than đá",
        "Làm nguội các dây cáp truyền tải điện",
        "Hút sạch độ ẩm trong không khí"
    ], 0, "BESS đóng vai trò đệm lưu trữ năng lượng linh hoạt, giải quyết tính bất định của điện mặt trời và điện gió."),
    make_vdc(3, "Công nghệ thu giữ và lưu trữ carbon (CCS - Carbon Capture and Storage): Khí thải từ các nhà máy xi măng, luyện thép được thu hồi khí CO2, nén lỏng rồi bơm sâu xuống các mỏ khí cạn kiệt hoặc tầng ngậm nước ngầm dưới đáy biển cách mặt đất hàng nghìn mét. Mục tiêu sống còn của công nghệ CCS là:", [
        "Cô lập vĩnh viễn hàng triệu tấn khí nhà kính CO2 không cho thoát vào bầu khí quyển, hiện thực hóa mục tiêu Net Zero",
        "Làm tăng áp suất lòng đất",
        "Hóa lỏng lòng đất",
        "Tạo ra mỏ dầu mới sau 1 tuần"
    ], 0, "CCS cô lập khí CO2 công nghiệp trong các cấu trúc địa chất an toàn sâu dưới lòng đất, triệt tiêu phát thải ròng vào khí quyển."),
    make_vdc(4, "Một trang trại thông minh tuần hoàn khép kín: Phân bò nuôi giun quế và ủ Biogas phát điện thắp sáng trang trại; bã phân sau ủ làm phân bón hữu cơ trồng ngô; ngô làm thức ăn cho bò; mái chuồng bò lợp pin mặt trời cấp điện cho hệ thống làm mát tự động. Mô hình kinh tế tuần hoàn năng lượng này đem lại giá trị lớn nhất là:", [
        "Triệt tiêu hoàn toàn chất thải ô nhiễm ra môi trường, tự cung cấp 100% năng lượng và tối ưu hóa lợi nhuận kinh tế bền vững",
        "Không cần cho bò ăn vẫn lớn",
        "Bò tự phát sáng trong bóng tối",
        "Trang trại tự nổi lên trên mặt nước"
    ], 0, "Kinh tế tuần hoàn (Circular Economy) khép kín chuỗi vật chất và năng lượng, biến chất thải thành tài nguyên sạch.")
]

exams["phys9_c8_b26_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c8_b26", "Bài 26: Vòng năng lượng trên Trái Đất. Năng lượng tái tạo", 3, p1_b26_t3, p2_b26_t3, p3_b26_t3, p4_b26_t3)

print("Added phys9_c8_b26 (3 tests).")
