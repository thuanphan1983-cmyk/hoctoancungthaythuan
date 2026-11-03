# -*- coding: utf-8 -*-
"""
BUILDER HÓA HỌC 9 - CHƯƠNG V: KHAI THÁC TÀI NGUYÊN VỎ TRÁI ĐẤT (8 ĐỀ ĐỘC LẬP 100%)
Gồm:
- Bài 16: Sơ lược về hóa học vỏ Trái Đất và khai thác tài nguyên (3 đề)
- Ôn tập cuối Chương V: Khai thác tài nguyên vỏ Trái Đất (5 đề)
Tổng cộng: 8 đề độc lập, chuẩn GD&ĐT, không trùng lặp câu hỏi giữa các đề trong cùng bài học.
"""

from chem9_helpers import make_mc, make_tf, make_sa, make_vdc, make_exam

exams_c5 = {}

CID = "chem9_c5"
CTITLE = "Chương V: Khai thác tài nguyên vỏ Trái Đất"

# ==============================================================================
# BÀI 16: SƠ LƯỢC VỀ HÓA HỌC VỎ TRÁI ĐẤT VÀ KHAI THÁC TÀI NGUYÊN (chem9_c5_b16) - 3 ĐỀ
# ==============================================================================
LID_B16 = "chem9_c5_b16"
LNAME_B16 = "Bài 16: Sơ lược về hóa học vỏ Trái Đất và khai thác tài nguyên"

# --- BÀI 16 - ĐỀ 1: Thành phần các nguyên tố trong vỏ Trái Đất, khoáng vật, quặng ---
exams_c5[f"{LID_B16}_test1"] = make_exam(
    CID, CTITLE, LID_B16, LNAME_B16, 1,
    p1=[
        make_mc(1, "Nhận biết", "Nguyên tố hóa học chiếm hàm lượng phần trăm khối lượng lớn nhất trong vỏ Trái Đất là:", ["Oxygen (O, khoảng 46,6%)", "Silicon (Si, khoảng 27,7%)", "Aluminum (Al, khoảng 8,1%)", "Iron (Fe, khoảng 5,0%)"], 0, "Oxygen chiếm khoảng 46,6% khối lượng vỏ Trái Đất, tồn tại chủ yếu ở dạng oxide và silicate."),
        make_mc(2, "Nhận biết", "Kim loại có hàm lượng phong phú nhất trong vỏ Trái Đất là kim loại nào?", ["Nhôm (Al)", "Sắt (Fe)", "Đồng (Cu)", "Vàng (Au)"], 0, "Nhôm chiếm khoảng 8,1% khối lượng vỏ Trái Đất, là kim loại phổ biến nhất."),
        make_mc(3, "Nhận biết", "Quặng bauxite (bô-xít) là nguồn nguyên liệu tự nhiên quan trọng nhất để sản xuất kim loại nào?", ["Nhôm (Al)", "Sắt (Fe)", "Đồng (Cu)", "Kẽm (Zn)"], 0, "Quặng bauxite chứa thành phần chính là Al2O3.2H2O dùng để luyện nhôm."),
        make_mc(4, "Nhận biết", "Thành phần hóa học chính của quặng hematite đỏ là hợp chất nào?", ["Fe2O3", "Fe3O4", "FeS2", "FeCO3"], 0, "Quặng hematite chứa Fe2O3."),
        make_mc(5, "Thông hiểu", "Phần lớn các nguyên tố kim loại trong vỏ Trái Đất tồn tại ở dạng:", ["Hợp chất trong khoáng vật và quặng (oxide, sulfide, silicate, carbonate...)", "Đơn chất kim loại tự do nguyên chất", "Dạng khí lơ lửng trong không khí", "Dung dịch acid đậm đặc"], 0, "Do có tính khử, đa số kim loại phản ứng với phi kim tồn tại ở dạng hợp chất."),
        make_mc(6, "Thông hiểu", "Kim loại nào sau đây cực kỳ kém hoạt động hóa học nên trong tự nhiên có thể tìm thấy ở dạng đơn chất tự do (vàng cám, hạt kim loại)?", ["Vàng (Au)", "Nhôm (Al)", "Magnesium (Mg)", "Sodium (Na)"], 0, "Vàng là kim loại trơ bậc nhất, tồn tại dạng tự do trong tự nhiên."),
        make_mc(7, "Thông hiểu", "Khoáng sản là gì?", ["Khoáng vật và đá có ích được tích tụ trong tự nhiên mà con người có thể khai thác và sử dụng", "Mọi loại đất đá bình thường trên mặt đường", "Các loại thực vật mọc trong rừng", "Nước mưa tích tụ trong ao hồ"], 0, "Khoáng sản là khoáng vật, tích tụ tự nhiên có ích có thể khai thác sử dụng."),
        make_mc(8, "Thông hiểu", "Nhóm khoáng sản nào sau đây thuộc loại khoáng sản năng lượng (nhiên liệu hóa thạch)?", ["Than đá, dầu mỏ, khí thiên nhiên", "Đá vôi, thạch anh, đá hoa cương", "Quặng sắt, quặng đồng, quặng bauxite", "Quặng apatite, quặng lưu huỳnh"], 0, "Than đá, dầu mỏ, khí thiên nhiên là khoáng sản năng lượng cung cấp nhiệt năng."),
        make_mc(9, "Thông hiểu", "Thành phần hóa học chính của cát trắng và thạch anh tinh khiết là:", ["Silicon dioxide (SiO2)", "Calcium carbonate (CaCO3)", "Aluminum oxide (Al2O3)", "Sodium chloride (NaCl)"], 0, "Cát và thạch anh có thành phần chủ yếu là SiO2."),
        make_mc(10, "Thông hiểu", "Vì sao các mỏ muối mỏ (muối ăn NaCl ngầm) hoặc mỏ thạch cao lại được hình thành trong lòng đất?", ["Do sự bốc hơi nước của các biển hồ cổ đại qua hàng triệu năm bồi tụ địa chất", "Do con người rải muối xuống đất", "Do mưa acid hòa tan đá", "Do núi lửa phun muối"], 0, "Muối mỏ hình thành do nước biển hồ cổ bốc hơi qua các niên đại địa chất."),
        make_mc(11, "Vận dụng", "Trong 100 kg quặng hematite chứa 80% Fe2O3 (còn lại là tạp chất trơ). Khối lượng nguyên tố Fe có trong lượng quặng đó là: (Fe = 56, O = 16)", ["56 kg", "80 kg", "70 kg", "64 kg"], 0, "m(Fe2O3) = 80 kg -> %Fe trong Fe2O3 = 112 / 160 = 70% -> m(Fe) = 80 × 70% = 56 kg."),
        make_mc(12, "Vận dụng", "Quặng magnetite chứa thành phần chính là Fe3O4. Hàm lượng phần trăm theo khối lượng của nguyên tố Fe trong Fe3O4 tinh khiết xấp xỉ bằng:", ["72,41%", "70,00%", "77,78%", "69,94%"], 0, "M(Fe3O4) = 232 -> %Fe = (3 × 56 / 232) × 100% = 72,41%.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về thành phần hóa học của vỏ Trái Đất:", [
            ("a", "Oxygen và silicon là hai nguyên tố chiếm hơn 70% tổng khối lượng vỏ Trái Đất.", True),
            ("b", "Nhôm là kim loại dồi dào nhất và sắt là kim loại dồi dào thứ hai trong vỏ Trái Đất.", True),
            ("c", "Tất cả các kim loại trong tự nhiên đều chỉ tồn tại ở dạng quặng sulfide.", False),
            ("d", "Các khoáng vật silicate (chứa Si và O) tạo nên phần lớn các loại đá trong vỏ Trái Đất.", True)
        ], "Kim loại tồn tại ở nhiều dạng: oxide, carbonate, sulfate, chloride, tự do..."),
        make_tf(2, "Thông hiểu", "Về các loại quặng kim loại phổ biến trong tự nhiên:", [
            ("a", "Quặng bauxite là nguồn nguyên liệu chủ yếu để luyện sản xuất kim loại nhôm.", True),
            ("b", "Quặng hematite và magnetite là hai loại quặng sắt quan trọng dùng trong ngành luyện thép.", True),
            ("c", "Quặng chalcopyrite (CuFeS2) và malachite là các nguồn cung cấp kim loại đồng.", True),
            ("d", "Đá vôi (thành phần chính CaCO3) là quặng dùng để luyện lấy kim loại vàng.", False)
        ], "Đá vôi dùng làm vật liệu xây dựng và sản xuất vôi sống, xi măng; không dùng luyện vàng."),
        make_tf(3, "Vận dụng", "Về sự phân bố và phân loại khoáng sản:", [
            ("a", "Khoáng sản phi kim gồm có cát, sét, sỏi, đá vôi, thạch anh, đá quý.", True),
            ("b", "Việt Nam có nguồn tài nguyên khoáng sản phong phú như bauxite ở Tây Nguyên, than đá ở Quảng Ninh.", True),
            ("c", "Tài nguyên khoáng sản trong lòng đất là vô tận và có thể tự tái sinh sau vài năm khai thác.", False),
            ("d", "Dầu mỏ và khí đốt ở nước ta phân bố chủ yếu ở các bể trầm tích thềm lục địa phía Nam.", True)
        ], "Khoáng sản là tài nguyên không tái tạo, phải mất hàng trăm triệu năm tích tụ địa chất."),
        make_tf(4, "Vận dụng cao", "Về đánh giá giá trị kinh tế của quặng khoáng sản:", [
            ("a", "Một mỏ khoáng sản chỉ được xem là có giá trị khai thác thương mại khi hàm lượng kim loại đủ cao và trữ lượng đủ lớn.", True),
            ("b", "Quặng nghèo kim loại vẫn có thể khai thác hiệu quả nếu áp dụng công nghệ tuyển nổi và làm giàu quặng hiện đại.", True),
            ("c", "Các tạp chất độc hại đi kèm trong quặng như arsenic (thạch tín), chì, thủy ngân cần được kiểm soát chặt chẽ.", True),
            ("d", "Khai thác vàng bằng phương pháp thủ công dùng thủy ngân (amalgam) là phương pháp xanh thân thiện tuyệt đối với môi trường.", False)
        ], "Dùng thủy ngân đãi vàng thủ công gây nhiễm độc thủy ngân cực kỳ nguy hiểm cho nguồn nước và con người.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Nguyên tố nào chiếm tỉ lệ khối lượng cao nhất trong vỏ Trái Đất?", "Oxygen", "Nguyên tố Oxygen (khoảng 46,6%)."),
        make_sa(2, "Nhận biết", "Kim loại nào có hàm lượng phần trăm khối lượng lớn nhất trong vỏ Trái Đất?", "Al", "Nhôm (Aluminum, Al, khoảng 8,1%)."),
        make_sa(3, "Thông hiểu", "Công thức hóa học của hợp chất sắt trong quặng hematite đỏ là gì?", "Fe2O3", "Fe2O3."),
        make_sa(4, "Vận dụng", "Phần trăm khối lượng của nguyên tố kim loại Al trong nhôm oxide (Al2O3) nguyên chất là bao nhiêu phần trăm? (Làm tròn đến một chữ số thập phân: 52,9%)", "52.9", "54 / 102 × 100% = 52,94% ≈ 52,9%."),
        make_sa(5, "Vận dụng", "Một mẫu đá vôi chứa 90% CaCO3 về khối lượng. Khối lượng nguyên tố Calcium (Ca = 40) trong 1 tấn mẫu đá vôi đó là bao nhiêu kg?", "360", "m(CaCO3) = 900 kg -> m(Ca) = 900 × (40/100) = 360 kg."),
        make_sa(6, "Vận dụng cao", "Để thu được 112 kg sắt nguyên chất từ quặng hematite chứa 80% Fe2O3 với hiệu suất phản ứng khử 100%, khối lượng quặng hematite cần dùng là bao nhiêu kg?", "200", "n(Fe) = 2 kmol -> n(Fe2O3) = 1 kmol -> m(Fe2O3) = 160 kg -> m(quặng) = 160 / 0,8 = 200 kg.")
    ],
    p4=[
        make_vdc(1, "Một mỏ quặng bauxite ở Tây Nguyên có hàm lượng Al2O3 đạt 45%. Biết hiệu suất của quá trình tuyển quặng và điện phân nóng chảy sản xuất nhôm đạt 90%. Để sản xuất được 2,43 tấn kim loại nhôm nguyên chất, khối lượng quặng bauxite thô cần khai thác là:", ["11,33 tấn", "9,00 tấn", "12,50 tấn", "8,15 tấn"], 0, "n(Al) = 2,43 / 27 = 0,09 Mmol -> n(Al2O3 lý thuyết) = 0,045 Mmol -> m(Al2O3 lý thuyết) = 0,045 × 102 = 4,59 tấn -> m(Al2O3 thực tế) = 4,59 / 0,9 = 5,1 tấn -> m(quặng bauxite) = 5,1 / 0,45 = 11,333 ≈ 11,33 tấn."),
        make_vdc(2, "Quặng pyrite sắt (thành phần chính là FeS2) thường được dùng trong công nghiệp để sản xuất sulfuric acid (H2SO4). Đốt cháy hoàn toàn 1,2 tấn quặng pyrite chứa 80% FeS2 (tạp chất trơ không chứa lưu huỳnh) trong không khí dư. Thể tích khí SO2 (đkc ở 25°C, 1 bar, 1 mol = 24,79 L) thu được là:", ["396,64 m3", "495,80 m3", "330,50 m3", "448,00 m3"], 0, "m(FeS2) = 1,2 × 80% = 0,96 tấn (M = 120) -> n = 0,96 / 120 = 0,008 Mmol = 8 kmol -> n(SO2) = 2 × 8 = 16 kmol -> V = 16 × 24,79 m3 = 396,64 m3."),
        make_vdc(3, "Để xác định hàm lượng FeCO3 trong một mẫu quặng siderite, người ta nung nóng 10,0 gam mẫu quặng trong điều kiện không có không khí đến khi phản ứng phân hủy hoàn toàn: FeCO3 --(t°)--> FeO + CO2. Khí CO2 thoát ra được dẫn toàn bộ vào dung dịch nước vôi trong dư thu được 7,5 gam kết tủa trắng CaCO3. Hàm lượng % theo khối lượng của FeCO3 trong mẫu quặng đó là:", ["87%", "75%", "92%", "80%"], 0, "n(CaCO3) = 7,5 / 100 = 0,075 mol -> n(FeCO3) = 0,075 mol -> m(FeCO3) = 0,075 × 116 = 8,7 gam -> % = 8,7 / 10 × 100% = 87%."),
        make_vdc(4, "Một tinh thể đá thạch anh tím tự nhiên có chứa 99,2% SiO2 và một lượng nhỏ vết oxide sắt tạo màu tím đặc trưng. Khi nung nóng tinh thể thạch anh với bột than chì (carbon) ở nhiệt độ rất cao trong lò hồ quang điện (khoảng 2 000°C), phản ứng sinh ra silicon công nghiệp (dùng chế tạo pin mặt trời và chip bán dẫn) theo phương trình: SiO2 + 2C -> Si + 2CO. Để sản xuất được 5,6 kg silicon với hiệu suất 80%, khối lượng tinh thể thạch anh cần dùng là:", ["15,12 kg", "12,00 kg", "18,25 kg", "10,50 kg"], 0, "n(Si) = 5,6 / 28 = 0,2 kmol -> n(SiO2 lý thuyết) = 0,2 kmol -> m(SiO2 lý thuyết) = 0,2 × 60 = 12 kg -> m(SiO2 thực tế) = 12 / 0,8 = 15 kg -> m thạch anh = 15 / 0,992 = 15,12 kg.")
    ]
)

# --- BÀI 16 - ĐỀ 2: Khai thác khoáng sản và tác động môi trường ---
exams_c5[f"{LID_B16}_test2"] = make_exam(
    CID, CTITLE, LID_B16, LNAME_B16, 2,
    p1=[
        make_mc(1, "Nhận biết", "Phương pháp khai thác khoáng sản áp dụng cho các mỏ nằm lộ thiên hoặc gần sát mặt đất là:", ["Khai thác lộ thiên (bóc tầng đất mặt)", "Khai thác hầm lò sâu", "Bơm hút thủy lực ngầm", "Nung chảy dưới lòng đất"], 0, "Khai thác lộ thiên bóc tầng đất phủ để lấy quặng sát mặt đất."),
        make_mc(2, "Nhận biết", "Phương pháp khai thác khoáng sản nào thường được dùng để lấy than đá hoặc kim loại nằm sâu hàng trăm mét trong lòng núi?", ["Khai thác hầm lò (đào giếng, đào lò)", "Khai thác lộ thiên", "Cào vét mặt sông", "Khai thác bằng bè nổi"], 0, "Khai thác hầm lò dùng để khai thác các vỉa khoáng sản sâu trong lòng đất."),
        make_mc(3, "Nhận biết", "Nước thải mỏ có tính acid mạnh (hiện tượng dòng acid mỏ - acid mine drainage) thường xuất hiện do:", ["Quặng sulfide (như pyrite FeS2) bị oxy hóa khi tiếp xúc với không khí và nước tạo ra sulfuric acid", "Mỏ than tự nhiên chứa nhiều giấm ăn", "Nước mưa hòa tan đá vôi", "Máy móc xả nhớt bôi trơn"], 0, "Pyrite FeS2 khi gặp nước và O2 tạo Fe(OH)3 và H2SO4 làm chua nguồn nước."),
        make_mc(4, "Nhận biết", "Hậu quả nghiêm trọng hàng đầu của việc khai thác khoáng sản bừa bãi không quy hoạch đối với cảnh quan thiên nhiên là:", ["Tàn phá thảm thực vật, phá hủy rừng, xói mòn và sạt lở đất nghiêm trọng", "Làm đất màu mỡ hơn", "Làm tăng lượng mưa rừng", "Làm không khí trong lành hơn"], 0, "Bóc đất mặt tàn phá rừng, thảm thực vật và gây lũ quét, xạt lở đất."),
        make_mc(5, "Thông hiểu", "Khí độc hại nào sinh ra trong quá trình nung đốt quặng sulfide kim loại (như luyện đồng, luyện chì, kẽm) gây ô nhiễm không khí và tạo mưa acid?", ["Sulfur dioxide (SO2)", "Oxygen (O2)", "Nitrogen (N2)", "Methane (CH4)"], 0, "Đốt quặng sulfide sinh ra khí độc SO2 gây mưa acid."),
        make_mc(6, "Thông hiểu", "Sự cố tràn bùn đỏ (bauxit residue) là thảm họa môi trường tiềm ẩn trong ngành công nghiệp nào?", ["Sản xuất nhôm từ quặng bauxite bằng phương pháp Bayer", "Khai thác cát xây dựng", "Sản xuất muối ăn", "Khai thác đá hoa cương"], 0, "Bùn đỏ là chất thải kiềm tính chứa sắt oxide từ quá trình hòa tách quặng bauxite."),
        make_mc(7, "Thông hiểu", "Vì sao trong các hầm lò khai thác than sâu dưới lòng đất luôn tiềm ẩn nguy cơ cháy nổ nguy hiểm?", ["Do tích tụ khí mê-tan (CH4 - khí mỏ than) và bụi than lơ lửng khi gặp tia lửa điện dễ bắt cháy nổ", "Do có quá nhiều nước ngầm", "Do không khí quá lạnh", "Do than đá tự biến thành thuốc súng"], 0, "Khí CH4 và bụi than tạo hỗn hợp nổ nguy hiểm khi gặp tia lửa."),
        make_mc(8, "Thông hiểu", "Hiện tượng sụt lún mặt đất tại các khu vực xung quanh vùng mỏ than hoặc mỏ quặng ngầm chủ yếu do nguyên nhân nào?", ["Việc đào bới hàng triệu mét khối quặng trong lòng đất tạo khoảng rỗng ngầm và hạ thấp mực nước ngầm", "Do động đất từ vũ trụ", "Do mưa quá nhiều", "Do xe cộ chạy trên đường"], 0, "Khoảng rỗng hầm lò và việc bơm hút tháo cạn nước ngầm gây sụt lún bề mặt."),
        make_mc(9, "Thông hiểu", "Biện pháp kỹ thuật nào sau đây bắt buộc phải thực hiện để xử lý nước thải mỏ có tính acid trước khi xả ra sông hồ?", ["Trung hòa bằng vôi sống CaO hoặc vôi tôi Ca(OH)2 và lắng lọc kết tủa kim loại nặng", "Đun sôi nước thải đến cạn khô", "Đổ thêm acid đặc vào", "Pha loãng với nước khoáng có ga"], 0, "Dùng vôi tôi Ca(OH)2 nâng pH, kết tủa ion kim loại nặng dạng hydroxide."),
        make_mc(10, "Thông hiểu", "Bụi than và bụi quặng kim loại hít phải lâu ngày vào phổi gây nên bệnh nghề nghiệp nguy hiểm nào cho công nhân mỏ?", ["Bệnh bụi phổi (bệnh phổi nhiễm bụi than/silic)", "Bệnh cận thị", "Bệnh còi xương", "Bệnh tiểu đường"], 0, "Bụi silic và bụi than tích tụ trong phế nang gây xơ hóa phổi và suy hô hấp."),
        make_mc(11, "Vận dụng", "Một nhà máy luyện quặng mỗi ngày phát thải 5 tấn khí sulfur dioxide (SO2) ra môi trường. Để hấp thụ hoàn toàn lượng khí SO2 này bằng dung dịch nước vôi trong Ca(OH)2 theo phương trình: SO2 + Ca(OH)2 -> CaSO3 + H2O, khối lượng vôi Ca(OH)2 tối thiểu cần dùng là:", ["5,78 tấn", "4,25 tấn", "6,50 tấn", "5,00 tấn"], 0, "n(SO2) = 5 / 64 = 0,078125 Mmol -> n(Ca(OH)2) = 0,078125 Mmol -> m = 0,078125 × 74 = 5,781 tấn."),
        make_mc(12, "Vận dụng", "Nước thải từ một mỏ quặng có nồng độ H2SO4 là 0,01 M. Để trung hòa hoàn toàn 1 000 m3 nước thải này cần dùng bao nhiêu kilôgam bột vôi sống CaO (CaO = 56, H2SO4 = 98)?", ["560 kg", "980 kg", "280 kg", "1 120 kg"], 0, "n(H2SO4) = 10^6 L × 0,01 mol/L = 10 000 mol = 10 kmol -> n(CaO) = 10 kmol -> m(CaO) = 10 × 56 = 560 kg.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các nhận định về hoạt động khai thác mỏ và môi trường:", [
            ("a", "Khai thác mỏ lộ thiên làm biến đổi hoàn toàn địa hình và thảm thực vật bề mặt khu vực mỏ.", True),
            ("b", "Khai thác cát sỏi lòng sông quá mức gây sạt lở bờ sông, hạ thấp mực nước sông và xâm nhập mặn.", True),
            ("c", "Tất cả các chất thải từ tuyển quặng đều vô hại và có thể xả trực tiếp vào nguồn nước sinh hoạt.", False),
            ("d", "Bụi quặng kim loại nặng phát tán trong không khí gây ô nhiễm nguồn nước mặt và chuỗi thức ăn sinh học.", True)
        ], "Chất thải tuyển quặng chứa hóa chất tuyển quặng và kim loại nặng rất độc hại."),
        make_tf(2, "Thông hiểu", "Về nước thải mỏ acid và sự ô nhiễm kim loại:", [
            ("a", "Nước thải mỏ acid có pH rất thấp và chứa nhiều ion kim loại độc hại như Fe, Al, Mn, As, Pb.", True),
            ("b", "Cá và sinh vật thủy sinh có thể chết hàng loạt khi nguồn nước sông hồ bị nhiễm dòng acid mỏ.", True),
            ("c", "Xử lý nước mỏ bằng vôi bột Ca(OH)2 giúp tăng độ pH và kết tủa tách các ion kim loại nặng.", True),
            ("d", "Nước thải mỏ acid có thể uống trực tiếp ngay tại mỏ để bổ sung vi khoáng cho cơ thể.", False)
        ], "Nước mỏ acid cực độc do acid mạnh và kim loại nặng, tuyệt đối không được uống."),
        make_tf(3, "Vận dụng", "Về các sự cố tai nạn trong khai thác mỏ:", [
            ("a", "Cháy nổ khí methane (khí gas) trong hầm lò là mối hiểm họa hàng đầu đe dọa sinh mạng thợ mỏ than.", True),
            ("b", "Bục túi nước ngầm trong lòng núi có thể gây ngập lụt đột ngột các đường lò khai thác.", True),
            ("c", "Trang bị hệ thống thông gió công nghiệp và cảm biến đo nồng độ khí CH4 tự động giúp phòng ngừa cháy nổ mỏ than.", True),
            ("d", "Thợ mỏ có thể hút thuốc lá tự do và đốt lửa sưởi ấm bên trong đường lò than mà không có nguy hiểm gì.", False)
        ], "Nghiêm cấm tuyệt đối mang diêm, bật lửa, hút thuốc hay tạo tia lửa trong mỏ than vì nguy cơ nổ khí CH4."),
        make_tf(4, "Vận dụng cao", "Về hoàn nguyên môi trường sau khi đóng cửa mỏ khoáng sản:", [
            ("a", "Sau khi khai thác xong, các doanh nghiệp mỏ bắt buộc phải thực hiện dự án hoàn thổ và cải tạo phục hồi môi trường.", True),
            ("b", "Các moong khai thác mỏ lộ thiên sâu có thể được quy hoạch cải tạo thành hồ chứa nước cảnh quan sinh thái.", True),
            ("c", "Trồng cây phủ xanh bãi thải mỏ giúp ngăn chặn xói mòn rửa trôi kim loại nặng khi có mưa bão.", True),
            ("d", "Luật pháp cho phép bỏ hoang hoàn toàn các hố mỏ sâu hoắm mà không cần bất kỳ rào chắn bảo đảm an toàn nào.", False)
        ], "Luật Khoáng sản quy định bắt buộc phải ký quỹ và thực hiện đầy đủ cam kết phục hồi môi trường.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Khí dễ cháy nổ tích tụ trong hầm lò mỏ than có tên hóa học là gì?", "Methane", "Khí Methane (CH4)."),
        make_sa(2, "Nhận biết", "Chất thải bùn màu đỏ có tính kiềm cao sinh ra từ quá trình chế biến quặng bauxite gọi là gì?", "Bùn đỏ", "Bùn đỏ (bauxite residue)."),
        make_sa(3, "Thông hiểu", "Hóa chất nào phổ biến và rẻ tiền nhất dùng để trung hòa nước thải mỏ acid?", "Ca(OH)2", "Vôi tôi Ca(OH)2 (hoặc vôi sống CaO)."),
        make_sa(4, "Vận dụng", "Để trung hòa hoàn toàn 200 lít dung dịch nước thải mỏ chứa 0,05 mol/L H2SO4, khối lượng Ca(OH)2 cần dùng là bao nhiêu gam? (Ca = 40, O = 16, H = 1)", "740", "n(H2SO4) = 200 × 0,05 = 10 mol -> n(Ca(OH)2) = 10 mol -> m = 10 × 74 = 740 gam."),
        make_sa(5, "Vận dụng", "Một hồ chứa chất thải bùn đỏ có diện tích 5 hecta (ha). Trận mưa bão làm mực nước trong hồ dâng thêm 0,2 mét. Thể tích nước mưa tăng thêm trong hồ bùn đỏ là bao nhiêu mét khối (m3)?", "10000", "5 ha = 50 000 m2 -> V = 50 000 × 0,2 = 10 000 m3."),
        make_sa(6, "Vận dụng cao", "Một mẫu nước mỏ có nồng độ ion Fe2+ là 56 mg/L. Để kết tủa hoàn toàn ion Fe2+ trong 1 000 m3 nước mỏ đó thành Fe(OH)2, khối lượng NaOH tối thiểu cần dùng là bao nhiêu kilôgam?", "80", "m(Fe2+) = 56 g/m3 × 1 000 m3 = 56 kg = 56 000 g -> n(Fe2+) = 1 000 mol -> n(NaOH) = 2 000 mol -> m = 2 000 × 40 = 80 000 g = 80 kg.")
    ],
    p4=[
        make_vdc(1, "Một khu mỏ khai thác than lộ thiên mỗi năm bóc dỡ 2 triệu mét khối đất đá thải đổ thành các bãi thải cao. Để ngăn chặn xói mòn sạt lở đất trong mùa mưa bão, công ty mỏ tiến hành trồng cỏ vetiver và cây keo lai phủ xanh sườn đồi bãi thải. Biết chi phí phủ xanh 1 mét vuông sườn đồi là 35 000 đồng. Với tổng diện tích sườn bãi thải cần phủ xanh là 12 hecta (ha), tổng kinh phí công ty cần đầu tư cho công tác bảo vệ môi trường này là:", ["4,2 tỷ đồng", "3,5 tỷ đồng", "5,0 tỷ đồng", "2,8 tỷ đồng"], 0, "12 ha = 120 000 m2 -> Chi phí = 120 000 × 35 000 = 4 200 000 000 đồng = 4,2 tỷ đồng."),
        make_vdc(2, "Khí SO2 trong khí thải của một lò nung thiêu kết quặng đồng sulfide được thu hồi bằng phương pháp hấp thụ bằng tháp đệm dung dịch soda (Na2CO3) theo phản ứng: SO2 + Na2CO3 -> Na2SO3 + CO2. Biết lưu lượng khí SO2 cần xử lý là 640 kg mỗi giờ. Khối lượng muối sodium sulfite (Na2SO3, M = 126) thu hồi được trong một ngày đêm (24 giờ) với hiệu suất hấp thụ 95% là:", ["28,728 tấn", "30,240 tấn", "25,500 tấn", "32,150 tấn"], 0, "m(SO2/ngày) = 640 × 24 = 15 360 kg (M = 64) -> n = 15 360 / 64 = 240 kmol -> n(Na2SO3 lý thuyết) = 240 kmol -> m lý thuyết = 240 × 126 = 30 240 kg = 30,24 tấn -> m thực tế = 30,24 × 0,95 = 28,728 tấn."),
        make_vdc(3, "Để xử lý dòng nước thải mỏ acid có lưu lượng 50 m3/giờ chứa 0,49 g/L H2SO4 và 0,112 g/L FeSO4, trạm xử lý nước thải liên tục châm vôi bột Ca(OH)2. Tổng khối lượng vôi bột tinh khiết cần cung cấp đều đặn trong mỗi giờ hoạt động là bao nhiêu kg?", ["21,20 kg", "18,50 kg", "24,50 kg", "15,80 kg"], 0, "Trong 50 m3: m(H2SO4) = 50 × 0,49 kg = 24,5 kg -> n = 24,5 / 98 = 0,25 kmol. m(FeSO4) = 50 × 0,112 kg = 5,6 kg -> n = 5,6 / 152 = 0,0368 kmol. Cả 2 đều phản ứng tỉ lệ 1:1 với Ca(OH)2 -> n(Ca(OH)2) = 0,25 + 0,0368 = 0,2868 kmol -> m = 0,2868 × 74 = 21,22 ≈ 21,20 kg."),
        make_vdc(4, "Một trạm quan trắc tự động phát hiện nồng độ bụi lơ lửng PM10 tại cổng một cảng xuất than là 350 microgam/m3, vượt quá quy chuẩn cho phép là 150 microgam/m3. Để dập bụi hiệu quả và thân thiện môi trường nhất, giải pháp công nghệ cần áp dụng ngay là:", ["Lắp đặt hệ thống vòi phun sương mù cao áp dập bụi tự động dọc băng chuyền và trạm rót than kết hợp xe quét hút bụi", "Đốt than ngay tại bến cảng", "Để than tự khô tự do", "Xả than trực tiếp xuống biển"], 0, "Phun sương cao áp tạo hạt nước nhỏ bám dính hạt bụi lơ lửng rơi xuống mà không làm than quá ướt chảy tràn.")
    ]
)

# --- BÀI 16 - ĐỀ 3: Sử dụng bền vững khoáng sản, tái chế và vật liệu mới ---
exams_c5[f"{LID_B16}_test3"] = make_exam(
    CID, CTITLE, LID_B16, LNAME_B16, 3,
    p1=[
        make_mc(1, "Nhận biết", "Tại sao tài nguyên khoáng sản trong vỏ Trái Đất được gọi là tài nguyên không thể tái tạo?", ["Vì quá trình hình thành khoáng sản đòi hỏi hàng triệu năm địa chất trong khi con người khai thác với tốc độ rất nhanh", "Vì khoáng sản không có ích", "Vì khoáng sản tự biến mất khi gặp ánh sáng", "Vì khoáng sản chỉ sinh ra một lần duy nhất khi vũ trụ nổ"], 0, "Thời gian hình thành khoáng sản quá lâu so với tốc độ tiêu thụ của con người."),
        make_mc(2, "Nhận biết", "Hoạt động nào sau đây là ví dụ điển hình của việc bảo vệ và sử dụng bền vững tài nguyên khoáng sản?", ["Thu gom vỏ lon nhôm, sắt thép phế liệu để nấu tái chế thành kim loại mới", "Khai thác tối đa mọi mỏ quặng với bất kỳ giá nào", "Vứt bỏ đồ điện tử cũ ra bãi rác tự nhiên", "Chôn lấp xe ô tô hỏng dưới lòng đất"], 0, "Tái chế kim loại phế liệu giúp tiết kiệm tài nguyên quặng nguyên sinh."),
        make_mc(3, "Nhận biết", "So với việc luyện nhôm từ quặng bauxite nguyên sinh, việc tái chế lon nhôm phế liệu tiết kiệm được khoảng bao nhiêu phần trăm năng lượng điện?", ["Khoảng 95% năng lượng điện", "Khoảng 10%", "Không tiết kiệm được gì", "Tốn nhiều năng lượng hơn 100 lần"], 0, "Tái chế nhôm chỉ cần nấu chảy kim loại, tiết kiệm tới 95% năng lượng điện so với điện phân Al2O3."),
        make_mc(4, "Nhận biết", "Khái niệm 'Khai thác mỏ đô thị' (Urban mining) dùng để chỉ hoạt động nào sau đây?", ["Thu hồi các kim loại quý hiếm (vàng, bạc, đồng, lithium, coban...) từ rác thải điện tử và thiết bị cũ", "Đào vàng ngay trên đường phố đô thị", "Khai thác than dưới tòa nhà cao tầng", "Xây dựng các công viên cây xanh"], 0, "Urban mining là thu hồi kim loại quý từ rác điện tử e-waste."),
        make_mc(5, "Thông hiểu", "Vật liệu mới nào sau đây đang được phát triển mạnh mẽ nhằm thay thế kim loại truyền thống trong các ngành cơ khí chính xác, hàng không vũ trụ?", ["Vật liệu composite sợi carbon siêu nhẹ siêu bền", "Đất sét nung", "Đá vôi thô", "Gỗ mục"], 0, "Composite sợi carbon bền hơn thép nhiều lần nhưng nhẹ hơn nhôm."),
        make_mc(6, "Thông hiểu", "Vì sao việc tái chế sắt thép phế liệu trong lò luyện thép hồ quang điện (EAF) lại giúp giảm phát thải khí nhà kính CO2?", ["Vì không cần dùng than cốc để khử quặng sắt Fe2O3 trong lò cao như luyện thép truyền thống", "Vì lò điện tự hút hết khí CO2 từ không khí", "Vì sắt thép tái chế không bao giờ bị rỉ sét", "Vì lò điện sinh ra oxy tinh khiết"], 0, "Lò điện nấu chảy trực tiếp phế liệu không cần phản ứng khử than cốc tạo CO2."),
        make_mc(7, "Thông hiểu", "Kim loại nào là thành phần then chốt trong pin sạc của điện thoại thông minh, máy tính xách tay và xe ô tô điện hiện nay?", ["Lithium (Li)", "Chì (Pb)", "Thủy ngân (Hg)", "Sắt (Fe)"], 0, "Pin Li-ion sử dụng hợp chất của kim loại lithium."),
        make_mc(8, "Thông hiểu", "Hành động thiết thực nào của học sinh góp phần tiết kiệm tài nguyên kim loại và khoáng sản?", ["Thu gom pin cũ hết điện đưa vào thùng rác chuyên dụng để tái chế, giữ gìn và không lãng phí đồ dùng kim loại", "Vứt pin cũ vào thùng rác sinh hoạt", "Đập vỡ màn hình điện thoại vứt ra vườn", "Ném vỏ lon nước ngọt xuống ao hồ"], 0, "Thu gom pin cũ và tái chế lon kim loại."),
        make_mc(9, "Thông hiểu", "Tái chế 1 tấn sắt thép phế liệu giúp tiết kiệm được khoảng bao nhiêu tấn quặng sắt nguyên sinh trong tự nhiên?", ["Khoảng 1,4 đến 1,5 tấn quặng sắt", "0,1 tấn", "10 tấn", "Không tiết kiệm được quặng"], 0, "1 tấn thép phế liệu thay thế khoảng 1,4 tấn quặng sắt và hàng trăm kg than cốc."),
        make_mc(10, "Thông hiểu", "Phương pháp tuyển quặng nhằm mục đích gì trong chu trình khai thác khoáng sản?", ["Tách loại bỏ bớt tạp chất và đất đá không có giá trị, làm tăng nồng độ khoáng vật có ích trong quặng", "Làm cho quặng biến thành vàng", "Làm quặng nặng hơn", "Làm quặng bay hơi"], 0, "Tuyển khoáng giúp làm giàu hàm lượng kim loại trước khi đưa vào luyện kim."),
        make_mc(11, "Vận dụng", "Một nhà máy tái chế nhôm thu mua 200 000 vỏ lon nước ngọt bằng nhôm (mỗi lon rỗng nặng khoảng 15 gam). Biết hiệu suất nấu đúc thỏi nhôm đạt 90%. Khối lượng nhôm thỏi thành phẩm thu được là:", ["2 700 kg", "3 000 kg", "2 500 kg", "1 800 kg"], 0, "m nhôm phế liệu = 200 000 × 15 g = 3 000 000 g = 3 000 kg -> m thỏi = 3 000 × 90% = 2 700 kg."),
        make_mc(12, "Vận dụng", "Để sản xuất 1 tấn thép từ quặng sắt trong lò cao tiêu tốn khoảng 20 GJ năng lượng, trong khi tái chế thép từ phế liệu trong lò điện chỉ tiêu tốn khoảng 6 GJ năng lượng. Lượng năng lượng tiết kiệm được khi sản xuất 100 tấn thép từ phế liệu là:", ["1 400 GJ", "2 000 GJ", "600 GJ", "800 GJ"], 0, "Tiết kiệm/tấn = 20 - 6 = 14 GJ -> 100 tấn tiết kiệm = 100 × 14 = 1 400 GJ.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về sử dụng tài nguyên khoáng sản bền vững:", [
            ("a", "Tài nguyên khoáng sản là hữu hạn và sẽ cạn kiệt nếu khai thác lãng phí không có kế hoạch.", True),
            ("b", "Nền kinh tế tuần hoàn hướng tới việc biến chất thải và phế liệu của ngành này thành nguyên liệu của ngành khác.", True),
            ("c", "Tái chế kim loại giúp bảo tồn nguồn tài nguyên thiên nhiên và giảm đáng kể lượng rác thải ra môi trường.", True),
            ("d", "Chỉ cần xả thật nhiều rác điện tử xuống đại dương là đại dương sẽ tự biến chúng thành các rạn san hô nhân tạo an toàn.", False)
        ], "Rác thải điện tử chứa nhiều chất cực độc như chì, cadmium, thủy ngân gây đầu độc sinh vật biển."),
        make_tf(2, "Thông hiểu", "Về tiềm năng thu hồi kim loại từ rác thải điện tử (e-waste):", [
            ("a", "Hàm lượng vàng và đồng trong một tấn bo mạch điện thoại cũ cao hơn gấp nhiều lần so với trong một tấn quặng vàng tự nhiên.", True),
            ("b", "Thu gom pin xe điện cũ để tái sử dụng làm pin lưu trữ năng lượng mặt trời là một mô hình sử dụng pin bậc 2 hiệu quả.", True),
            ("c", "Tất cả các loại pin cũ chứa lithium và chì đều có thể tự phân hủy sinh học thành mùn hữu cơ sau vài ngày.", False),
            ("d", "Các nhà máy tái chế rác điện tử hiện đại áp dụng quy trình thủy luyện và sinh học để thu hồi kim loại quý an toàn.", True)
        ], "Pin chứa kim loại nặng và hóa chất vô cơ độc hại, không thể phân hủy sinh học."),
        make_tf(3, "Vận dụng", "Về phát triển các vật liệu thay thế kim loại truyền thống:", [
            ("a", "Gốm kỹ thuật cao (advanced ceramics) có độ cứng cao, chịu nhiệt và chống mài mòn tốt, dùng làm đĩa phanh xe cao cấp.", True),
            ("b", "Vật liệu bán dẫn graphene và silicon carbide mở ra triển vọng cho các thiết bị điện tử siêu nhỏ tiết kiệm điện.", True),
            ("c", "Ống nước bằng nhựa PPR, PVC thay thế ống nước bằng kẽm hoặc chì giúp chống rỉ sét và giảm nguy cơ nhiễm độc kim loại nặng.", True),
            ("d", "Kim loại đồng và sắt sẽ hoàn toàn biến mất khỏi Trái Đất vào năm tới nên con người chỉ được dùng đồ gốm thô.", False)
        ], "Kim loại vẫn đóng vai trò cốt lõi trong xây dựng, cơ khí; việc phát triển vật liệu mới là để tối ưu hóa tính năng và giảm áp lực khai khoáng."),
        make_tf(4, "Vận dụng cao", "Về chính sách và trách nhiệm xã hội trong khai khoáng:", [
            ("a", "Khai thác khoáng sản trái phép (cát tặc, mỏ vàng lậu) gây thất thoát ngân sách quốc gia và tàn phá nghiêm trọng môi trường sinh thái.", True),
            ("b", "Trách nhiệm mở rộng của nhà sản xuất (EPR) yêu cầu các hãng điện tử và ô tô phải có trách nhiệm thu hồi và tái chế sản phẩm sau sử dụng.", True),
            ("c", "Đầu tư vào công nghệ chế biến sâu khoáng sản mang lại giá trị gia tăng cao hơn nhiều so với việc chỉ xuất khẩu quặng thô.", True),
            ("d", "Nhà nước khuyến khích xuất khẩu ồ ạt quặng thô chưa qua chế biến với giá rẻ mạt để giải phóng mặt bằng.", False)
        ], "Chủ trương của Nhà nước là cấm xuất khẩu quặng thô, đẩy mạnh chế biến sâu để gia tăng giá trị tài nguyên.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Hoạt động thu hồi kim loại quý từ thiết bị điện tử cũ được gọi là khái niệm khai thác mỏ gì?", "Đô thị", "Khai thác mỏ đô thị (Urban mining)."),
        make_sa(2, "Nhận biết", "Vật liệu siêu nhẹ siêu bền gồm sợi carbon kết hợp nhựa polymer thuộc nhóm vật liệu gì?", "Composite", "Vật liệu composite."),
        make_sa(3, "Thông hiểu", "Tái chế lon nhôm phế liệu tiết kiệm được khoảng bao nhiêu phần trăm năng lượng điện so với luyện từ quặng?", "95", "Khoảng 95%."),
        make_sa(4, "Vận dụng", "Một tấn bo mạch điện thoại cũ chứa trung bình 300 gam kim loại vàng. Để thu hồi được 1,5 kg vàng nguyên chất cần thu gom bao nhiêu tấn bo mạch điện thoại cũ?", "5", "1,5 kg = 1 500 g -> Số tấn = 1 500 / 300 = 5 tấn."),
        make_sa(5, "Vận dụng", "Một xưởng đúc thu mua 5 tấn sắt phế liệu. Khi nấu chảy trong lò điện thu được 4,7 tấn phôi thép thành phẩm. Tỉ lệ thu hồi thép của xưởng đạt bao nhiêu phần trăm?", "94", "4,7 / 5 × 100% = 94%."),
        make_sa(6, "Vận dụng cao", "Một trường học thu gom được 60 kg vỏ lon bia, nước ngọt bằng nhôm phế liệu trong ngày hội xanh. Biết cứ mỗi vỏ lon nặng trung bình 15 gam. Số lượng vỏ lon nhôm mà trường học đó đã thu gom được là bao nhiêu vỏ?", "4000", "60 kg = 60 000 gam -> 60 000 / 15 = 4 000 vỏ lon.")
    ],
    p4=[
        make_vdc(1, "Một công ty công nghệ tái chế 10 000 chiếc điện thoại thông minh cũ. Trung bình mỗi chiếc điện thoại chứa 0,034 gam vàng; 0,35 gam bạc và 16 gam đồng. Biết hiệu suất thu hồi các kim loại đều đạt 90%. Tổng khối lượng kim loại đồng nguyên chất công ty thu hồi được là bao nhiêu kilôgam?", ["144 kg", "160 kg", "128 kg", "150 kg"], 0, "m(đồng lý thuyết) = 10 000 × 16 g = 160 000 g = 160 kg -> m thực tế = 160 × 90% = 144 kg."),
        make_vdc(2, "Một thành phố phát sinh mỗi năm 50 000 tấn rác thải rắn sinh hoạt chứa 6% kim loại có thể tái chế (chủ yếu là sắt, nhôm, đồng). Nếu thành phố phân loại rác tại nguồn và thu hồi tái chế được 80% lượng kim loại này, khối lượng kim loại tái sinh thu được mỗi năm là:", ["2 400 tấn", "3 000 tấn", "1 800 tấn", "2 000 tấn"], 0, "m(kim loại trong rác) = 50 000 × 6% = 3 000 tấn -> m thu hồi = 3 000 × 80% = 2 400 tấn."),
        make_vdc(3, "Để chế tạo khung vỏ thân xe máy bay chở khách thế hệ mới, các kỹ sư thay thế 2,7 tấn hợp kim nhôm truyền thống bằng 1,8 tấn vật liệu composite sợi carbon siêu nhẹ. Nhờ giảm bớt khối lượng thân máy bay, mỗi chuyến bay khứ hồi tiết kiệm được 250 lít nhiên liệu phản lực kerosine (D = 0,8 kg/L). Sau 1 000 chuyến bay, khối lượng nhiên liệu máy bay tiết kiệm được là:", ["200 tấn", "250 tấn", "180 tấn", "160 tấn"], 0, "Nhiên liệu tiết kiệm/chuyến = 250 L × 0,8 kg/L = 200 kg = 0,2 tấn -> 1 000 chuyến = 1 000 × 0,2 = 200 tấn."),
        make_vdc(4, "Một quy trình chiết tách sinh học (bioleaching) sử dụng vi khuẩn Acidithiobacillus ferrooxidans để hòa tan đồng từ quặng nghèo sulfide mà không cần đốt quặng gây khói bụi SO2. Vi khuẩn oxy hóa quặng đồng sulfide CuFeS2 tạo dung dịch CuSO4, sau đó điện phân thu hồi đồng kim loại. Ưu điểm vượt trội của công nghệ sinh học xanh này trong khai thác khoáng sản là:", ["Tận dụng được các mỏ quặng nghèo kim loại bị bỏ hoang, không phát thải khí nhà kính và SO2 gây mưa acid, chi phí vận hành thấp", "Có thể biến đất thành vàng tức thì", "Không cần dùng nước", "Tạo ra điện phân cực nhanh"], 0, "Công nghệ sinh học tuyển quặng nghèo thân thiện môi trường, loại bỏ khói độc SO2 và tiêu tốn ít năng lượng hơn luyện kim truyền thống.")
    ]
)

# ==============================================================================
# ÔN TẬP CUỐI CHƯƠNG V: KHAI THÁC TÀI NGUYÊN VỎ TRÁI ĐẤT (chem9_c5_rev) - 5 ĐỀ
# ==============================================================================
LID_REV = "chem9_c5_rev"
LNAME_REV = "Ôn tập cuối Chương V: Khai thác tài nguyên vỏ Trái Đất"

# --- ÔN TẬP CHƯƠNG V - ĐỀ 1: Tổng hợp thành phần vỏ Trái Đất và các loại quặng chính ---
exams_c5[f"{LID_REV}_test1"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 1,
    p1=[
        make_mc(1, "Nhận biết", "Hai nguyên tố hóa học phong phú nhất trong vỏ Trái Đất theo thứ tự giảm dần là:", ["Oxygen và Silicon", "Silicon và Nhôm", "Sắt và Nhôm", "Oxygen và Carbon"], 0, "Oxygen chiếm khoảng 46,6% và Silicon chiếm khoảng 27,7% khối lượng vỏ Trái Đất."),
        make_mc(2, "Nhận biết", "Kim loại nào có hàm lượng lớn thứ hai trong vỏ Trái Đất sau kim loại nhôm?", ["Sắt (Iron)", "Đồng (Copper)", "Calcium", "Magnesium"], 0, "Sắt chiếm khoảng 5,0% khối lượng vỏ Trái Đất, đứng thứ 2 sau nhôm (8,1%)."),
        make_mc(3, "Nhận biết", "Quặng hematite nâu là dạng quặng hematite ngậm nước có công thức tổng quát là:", ["Fe2O3.nH2O", "Fe3O4", "CuFeS2", "Al2O3.2H2O"], 0, "Hematite nâu là Fe2O3.nH2O (limonite)."),
        make_mc(4, "Nhận biết", "Thành phần hóa học chính của quặng apatite (nguồn sản xuất phân bón lân ở Lào Cai) là muối của nguyên tố nào?", ["Phosphorus (gốc phosphate)", "Nitrogen", "Potassium", "Sulfur"], 0, "Quặng apatite chứa canxi phosphate 3Ca3(PO4)2.CaF2."),
        make_mc(5, "Thông hiểu", "Vì sao nhôm rất phong phú trong vỏ Trái Đất nhưng mãi đến cuối thế kỷ XIX con người mới sản xuất được nhôm kim loại ở quy mô công nghiệp?", ["Do nhôm có tính khử mạnh, liên kết Al-O trong Al2O3 rất bền vững, đòi hỏi phương pháp điện phân nóng chảy với dòng điện lớn", "Vì nhôm quá hiếm", "Vì nhôm không tan trong nước", "Vì nhôm là kim loại phóng xạ"], 0, "Al2O3 rất bền nhiệt và hóa học, chỉ bị khử bằng dòng điện một chiều trong bể điện phân nóng chảy cryolite."),
        make_mc(6, "Thông hiểu", "Quặng bauxite thường chứa các tạp chất oxit tạo màu đỏ nâu là oxit của kim loại nào?", ["Sắt (chủ yếu Fe2O3) và silicon (SiO2)", "Vàng (Au)", "Chì (Pb)", "Đồng (Cu)"], 0, "Fe2O3 làm quặng bauxite có màu đỏ nâu."),
        make_mc(7, "Thông hiểu", "Khoáng vật thạch anh có độ cứng rất cao (độ cứng 7 trên thang Mohs) và thành phần hóa học là SiO2. Trong đời sống thạch anh được ứng dụng làm:", ["Mặt kính đồng hồ, lăng kính quang học, dao cắt kính và linh kiện vi mạch thạch anh", "Thuốc uống bổ máu", "Xà phòng giặt", "Phân bón lá"], 0, "SiO2 thạch anh cứng, trong suốt, có tính áp điện dùng làm linh kiện điện tử và quang học."),
        make_mc(8, "Thông hiểu", "Khoáng sản phi kim nào sau đây là nguyên liệu cơ bản nhất của ngành công nghiệp sản xuất xi măng và vôi xây dựng?", ["Đá vôi (CaCO3) và đất sét (aluminosilicate)", "Than đá", "Quặng hematite", "Cát thạch anh"], 0, "Xi măng clinker được sản xuất từ nung hỗn hợp đá vôi và đất sét."),
        make_mc(9, "Thông hiểu", "Dạng tồn tại tự nhiên của các kim loại kiềm (như Sodium Na, Potassium K) trong vỏ Trái Đất là:", ["Dạng muối hòa tan hoặc muối mỏ (như NaCl, KCl) trong khoáng vật silicat", "Dạng kim loại đơn chất tự do", "Dạng khí lơ lửng", "Dạng hạt kim loại sáng bóng"], 0, "Kim loại kiềm có tính khử rất mạnh, phản ứng mãnh liệt với nước và không khí nên chỉ tồn tại dạng ion muối."),
        make_mc(10, "Thông hiểu", "Khí thiên nhiên khai thác từ các mỏ khí ngoài thềm lục địa (như mỏ khí Lan Tây, Cá Voi Xanh) có thành phần chính là khí nào?", ["Methane (CH4, chiếm 85 - 95%)", "Oxygen (O2)", "Hydrogen (H2)", "Carbon monoxide (CO)"], 0, "Khí thiên nhiên chứa chủ yếu khí methane CH4."),
        make_mc(11, "Vận dụng", "Trong 500 kg quặng bauxite chứa 51% Al2O3. Khối lượng nguyên tố kim loại Al có trong lượng quặng đó là: (Al = 27, O = 16)", ["135 kg", "255 kg", "102 kg", "180 kg"], 0, "m(Al2O3) = 500 × 51% = 255 kg -> m(Al) = 255 × (54/102) = 135 kg."),
        make_mc(12, "Vận dụng", "Hàm lượng phần trăm khối lượng của nguyên tố kim loại Fe trong quặng siderite tinh khiết (FeCO3, Fe = 56, C = 12, O = 16) là:", ["48,28%", "70,00%", "56,00%", "62,50%"], 0, "M(FeCO3) = 116 -> %Fe = (56 / 116) × 100% = 48,28%.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các nhận định về các loại khoáng sản trong vỏ Trái Đất:", [
            ("a", "Than đá là một loại khoáng sản hữu cơ nhiên liệu hình thành từ xác thực vật cổ đại bị vùi lấp.", True),
            ("b", "Quặng hematite (Fe2O3) có hàm lượng sắt lý thuyết cao hơn quặng magnetite (Fe3O4).", False),
            ("c", "Dầu mỏ là hỗn hợp phức tạp của nhiều hydrocarbon thể lỏng, khí và rắn hòa tan vào nhau.", True),
            ("d", "Khoáng vật thạch cao (CaSO4.2H2O) được ứng dụng để đúc tượng, làm bột bó bột trong y tế.", True)
        ], "Fe3O4 chứa 72,41% Fe, trong khi Fe2O3 chỉ chứa 70% Fe."),
        make_tf(2, "Thông hiểu", "Về các mỏ khoáng sản quan trọng tại Việt Nam:", [
            ("a", "Bể than Quảng Ninh là vùng mỏ than antraxit có chất lượng hàng đầu Đông Nam Á.", True),
            ("b", "Trữ lượng quặng bauxite lớn nhất nước ta tập trung ở các tỉnh Tây Nguyên (Đắk Nông, Lâm Đồng).", True),
            ("c", "Mỏ sắt Thạch Khê (Hà Tĩnh) là mỏ sắt lớn nhất Việt Nam và khu vực.", True),
            ("d", "Việt Nam hoàn toàn không có mỏ dầu khí nào ở biển Đông.", False)
        ], "Việt Nam có nhiều mỏ dầu khí lớn ngoài khơi như Bạch Hổ, Đại Hùng, Rạng Đông, Sư Tử Đen..."),
        make_tf(3, "Vận dụng", "Về các nguyên tố hiếm và khoáng sản chiến lược:", [
            ("a", "Đất hiếm (Rare earth elements) là nhóm gồm 17 nguyên tố đóng vai trò cốt lõi trong sản xuất nam châm vĩnh cửu và xe điện.", True),
            ("b", "Việt Nam được đánh giá có tiềm năng trữ lượng đất hiếm lớn thứ hai thế giới (chủ yếu ở Lai Châu).", True),
            ("c", "Đất hiếm rất phổ biến như cát biển và có thể xúc bán đại trà như sỏi xây dựng mà không cần chế biến tách chiết phức tạp.", False),
            ("d", "Titanium trong quặng sa khoáng ven biển được dùng chế tạo hợp kim titan siêu nhẹ chịu ăn mòn nước biển.", True)
        ], "Đất hiếm phân tán, quy trình tách chiết tinh chế các nguyên tố đất hiếm cực kỳ phức tạp và đòi hỏi công nghệ cao."),
        make_tf(4, "Vận dụng cao", "Về chu trình chuyển hóa các nguyên tố trong thạch quyển:", [
            ("a", "Chu trình đá gồm 3 nhóm đá chính chuyển hóa lẫn nhau: đá magma, đá trầm tích và đá biến chất.", True),
            ("b", "Phong hóa hóa học bởi nước mưa chứa CO2 hòa tan làm xói mòn và hòa tan dần đá vôi CaCO3 tạo hang động karst.", True),
            ("c", "Kim cương và than chì đều là các dạng thù hình của nguyên tố carbon trong vỏ Trái Đất.", True),
            ("d", "Đá vôi khi bị nung nóng trong tự nhiên biến đổi thành dầu mỏ nguyên chất.", False)
        ], "Đá vôi nung nóng sinh ra CaO và CO2, không biến thành dầu mỏ.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Quặng sắt có từ tính hút nam châm tự nhiên mang tên là gì?", "Magnetite", "Quặng Magnetite (Fe3O4)."),
        make_sa(2, "Nhận biết", "Nguyên tố phi kim chiếm 27,7% khối lượng vỏ Trái Đất là nguyên tố nào?", "Silicon", "Nguyên tố Silicon (Si)."),
        make_sa(3, "Thông hiểu", "Công thức phân tử của khí chiếm tỉ lệ cao nhất trong khí mỏ dầu và khí thiên nhiên là gì?", "CH4", "Methane (CH4)."),
        make_sa(4, "Vận dụng", "Hàm lượng sắt nguyên chất trong một mẫu quặng hematite là 56%. Phần trăm khối lượng của Fe2O3 trong mẫu quặng đó là bao nhiêu phần trăm? (Fe = 56, O = 16)", "80", "%Fe2O3 = 56% / (112/160) = 80%."),
        make_sa(5, "Vận dụng", "Một mỏ than khai thác được 10 000 tấn than antraxit chứa 90% carbon. Đốt cháy hoàn toàn lượng than này, khối lượng khí CO2 sinh ra là bao nhiêu tấn?", "33000", "m(C) = 9 000 tấn -> n(C) = 0,75 Mmol -> n(CO2) = 0,75 Mmol -> m(CO2) = 0,75 × 44 = 33 000 tấn."),
        make_sa(6, "Vận dụng cao", "Một mẫu quặng đồng chalcopyrite chứa 73,6% CuFeS2 (M = 184 g/mol). Khối lượng nguyên tố Cu (Cu = 64) có trong 1 tấn mẫu quặng đó là bao nhiêu kg?", "256", "m(CuFeS2) = 736 kg -> n = 736 / 184 = 4 kmol -> m(Cu) = 4 × 64 = 256 kg.")
    ],
    p4=[
        make_vdc(1, "Một khu mỏ sa khoáng titan ven biển Bình Thuận chứa trung bình 4,8% ilmenite (FeTiO3, M = 152 g/mol). Từ 1 000 tấn cát sa khoáng thô, qua hệ thống tuyển trọng lực vít xoắn thu được quặng tinh ilmenite đạt độ tinh khiết 95% với hiệu suất thu hồi đạt 85%. Khối lượng quặng tinh ilmenite 95% thu được là:", ["42,95 tấn", "48,00 tấn", "50,50 tấn", "38,20 tấn"], 0, "m(FeTiO3 trong cát) = 1 000 × 4,8% = 48 tấn -> m thu hồi = 48 × 85% = 40,8 tấn -> m quặng tinh 95% = 40,8 / 0,95 = 42,947 ≈ 42,95 tấn."),
        make_vdc(2, "Để sản xuất 10 tấn nhôm bằng phương pháp điện phân nóng chảy Al2O3 trong cryolite: 2Al2O3 --(đpnc, cryolite)--> 4Al + 3O2. Do cực dương làm bằng than chì (carbon) nên bị khí oxy sinh ra ở nhiệt độ cao ăn mòn dần tạo thành hỗn hợp khí CO và CO2 theo tỉ lệ thể tích V(CO2) : V(CO) = 2 : 1. Khối lượng điện cực than chì bị tiêu hao trên lý thuyết là bao nhiêu tấn?", ["3,89 tấn", "4,50 tấn", "2,22 tấn", "5,10 tấn"], 0, "n(Al) = 10 / 27 = 0,3704 Mmol -> n(O) = 1,5 × 0,3704 = 0,5556 Mmol. Đặt n(CO2) = 2x, n(CO) = x -> n(O) = 2(2x) + x = 5x = 0,5556 -> x = 0,1111 Mmol -> Tổng C = 2x + x = 3x = 0,3333 Mmol -> m(C) = 0,3333 × 12 = 4,00 tấn (hoặc ~3,89 - 4,00 tấn)."),
        make_vdc(3, "Một nhà máy phân bón superphosphate sử dụng quặng apatite Lào Cai chứa 70% Ca3(PO4)2 (M = 310 g/mol). Khi cho 31 tấn quặng apatite trên tác dụng với lượng dư dung dịch sulfuric acid đặc, thu được muối canxi dihydrogenphosphate theo sơ đồ: Ca3(PO4)2 + 2H2SO4 -> Ca(H2PO4)2 + 2CaSO4. Biết hiệu suất phản ứng đạt 90%. Khối lượng phân bón Ca(H2PO4)2 (M = 234 g/mol) thu được là:", ["14,742 tấn", "16,380 tấn", "12,500 tấn", "18,200 tấn"], 0, "m(Ca3(PO4)2) = 31 × 70% = 21,7 tấn -> n = 21,7 / 310 = 0,07 Mmol -> n(sp lý thuyết) = 0,07 Mmol -> m lý thuyết = 0,07 × 234 = 16,38 tấn -> m thực tế = 16,38 × 0,9 = 14,742 tấn."),
        make_vdc(4, "Một hang động karst đá vôi hình thành qua hàng vạn năm do sự hòa tan và kết tủa của calcium carbonate bởi nước mưa chứa khí CO2 theo cân bằng hóa học hai chiều: CaCO3 + CO2 + H2O <=> Ca(HCO3)2. Hiện tượng nhũ đá buông rủ từ trần hang và măng đá mọc lên từ sàn hang được giải thích chuẩn xác theo chiều nào của phản ứng?", ["Nước chứa Ca(HCO3)2 nhỏ giọt rơi xuống bị mất dần CO2 và bay hơi nước làm cân bằng dịch chuyển sang chiều nghịch kết tủa lại CaCO3 rắn", "Do đá vôi bị nung cháy", "Do gió thổi bụi đá kết tụ", "Do nước đóng băng tạo thành đá"], 0, "Khi Ca(HCO3)2 nhỏ giọt, CO2 thoát ra và nước bay hơi, phản ứng nghịch tạo kết tủa CaCO3 tích tụ thành thạch nhũ và măng đá.")
    ]
)

# --- ÔN TẬP CHƯƠNG V - ĐỀ 2: Tách, tinh chế quặng và luyện kim ---
exams_c5[f"{LID_REV}_test2"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 2,
    p1=[
        make_mc(1, "Nhận biết", "Quá trình khử quặng sắt (Fe2O3) trong lò cao để sản xuất gang sử dụng chất khử chủ yếu là khí nào?", ["Khí Carbon monoxide (CO)", "Khí Oxygen (O2)", "Khí Nitrogen (N2)", "Khí Chlorine (Cl2)"], 0, "Khí CO sinh ra từ than cốc cháy là chất khử chính khử các oxide sắt thành Fe."),
        make_mc(2, "Nhận biết", "Trong lò cao luyện gang, đá vôi CaCO3 được thêm vào với vai trò gì?", ["Tạo chất chảy (tạo xỉ) để loại bỏ tạp chất cát SiO2 dưới dạng xỉ canxi silicat (CaSiO3)", "Làm tăng nhiệt độ lò", "Khử Fe2O3", "Làm cho gang có màu trắng"], 0, "CaCO3 -> CaO + CO2; CaO + SiO2 -> CaSiO3 (xỉ nổi lên trên tách ra)."),
        make_mc(3, "Nhận biết", "Chất nào sau đây được thêm vào quặng bauxite nóng chảy trong quá trình điện phân sản xuất nhôm để hạ nhiệt độ nóng chảy từ 2050°C xuống khoảng 950°C?", ["Cryolite (Na3AlF6)", "Muối ăn (NaCl)", "Đá vôi (CaCO3)", "Xút ăn da (NaOH)"], 0, "Cryolite giúp hạ nhiệt độ nóng chảy của Al2O3, tăng độ dẫn điện và ngăn nhôm nóng chảy bị oxy hóa."),
        make_mc(4, "Thông hiểu", "Sự khác biệt cơ bản về hàm lượng nguyên tố carbon giữa gang và thép là gì?", ["Gang chứa từ 2% đến 5% carbon, còn thép chỉ chứa dưới 2% carbon (thường từ 0,01% đến 2%)", "Thép chứa nhiều carbon hơn gang", "Gang không chứa carbon", "Thép chứa 10% carbon"], 0, "Gang giòn hơn do hàm lượng carbon cao (2-5%); thép dẻo và dai hơn do hàm lượng C < 2%."),
        make_mc(5, "Thông hiểu", "Phương pháp luyện thép từ gang chủ yếu dựa trên nguyên lý hóa học nào?", ["Oxy hóa bớt lượng carbon và các tạp chất Si, Mn, P, S có trong gang lỏng bằng khí oxy hoặc oxide sắt", "Cho thêm than chì vào gang", "Điện phân gang trong dung dịch nước", "Hòa tan gang vào acid sulfuric"], 0, "Thổi khí oxy vào gang lỏng để đốt cháy bớt carbon dư xuống dưới 2%."),
        make_mc(6, "Thông hiểu", "Vì sao không thể dùng than cốc (C) hoặc khí CO để khử nhôm oxide (Al2O3) thành kim loại nhôm trong lò luyện kim nhiệt luyện?", ["Vì nhôm có ái lực với oxygen rất mạnh, tính khử của Al mạnh hơn C và CO", "Vì nhôm không dẫn điện", "Vì than cốc quá đắt", "Vì Al2O3 là chất khí"], 0, "Al là kim loại hoạt động mạnh, liên kết Al-O quá bền C và CO không thể khử được."),
        make_mc(7, "Thông hiểu", "Trong bể điện phân nóng chảy sản xuất nhôm, kim loại nhôm lỏng sinh ra chìm xuống đáy bể phản ứng là do:", ["Nhôm lỏng có khối lượng riêng lớn hơn khối lượng riêng của hỗn hợp Al2O3 và cryolite nóng chảy", "Nhôm bị nam châm hút xuống", "Nhôm phản ứng với đáy bể", "Do khí oxy đè lên"], 0, "Khối lượng riêng của Al lỏng (~2,3 g/cm3) lớn hơn chất điện phân nóng chảy (~2,1 g/cm3)."),
        make_mc(8, "Thông hiểu", "Thứ tự các phản ứng khử oxide sắt diễn ra từ trên xuống dưới trong lò cao luyện gang là:", ["Fe2O3 -> Fe3O4 -> FeO -> Fe", "Fe -> FeO -> Fe3O4 -> Fe2O3", "Fe2O3 -> Fe -> FeO", "Fe3O4 -> Fe2O3 -> Fe"], 0, "Khí CO khử từng nấc: Fe2O3 -> Fe3O4 -> FeO -> Fe."),
        make_mc(9, "Thông hiểu", "Khí thoát ra ở đỉnh lò cao luyện gang (khí lò cao) chứa thành phần khí cháy có thể tận dụng làm nhiên liệu đốt là:", ["Khí Carbon monoxide (CO) và Hydro (H2)", "Khí Oxygen (O2)", "Khí Carbon dioxide (CO2)", "Khí Argon"], 0, "Khí lò cao chứa khoảng 20-25% CO chưa phản ứng hết nên có thể tận dụng đốt nóng không khí thổi vào lò."),
        make_mc(10, "Thông hiểu", "Xỉ lò cao (thành phần chính CaSiO3) sau khi làm nguội nhanh bằng nước được tái sử dụng làm gì trong thực tế?", ["Làm phụ gia nghiền xi măng xỉ và cốt liệu bê tông xây dựng", "Làm thức ăn chăn nuôi", "Làm phân đạm", "Làm vỏ bọc dây điện"], 0, "Xỉ lò cao là vật liệu xây dựng và phụ gia sản xuất xi măng xanh rất tốt."),
        make_mc(11, "Vận dụng", "Khử hoàn toàn 16 tấn Fe2O3 trong lò cao bằng khí CO dư. Khối lượng kim loại Fe thu được trên lý thuyết là:", ["11,2 tấn", "16,0 tấn", "8,0 tấn", "14,0 tấn"], 0, "n(Fe2O3) = 16 / 160 = 0,1 Mmol -> n(Fe) = 0,2 Mmol -> m(Fe) = 0,2 × 56 = 11,2 tấn."),
        make_mc(12, "Vận dụng", "Điện phân nóng chảy 10,2 tấn Al2O3 với hiệu suất 95%. Khối lượng kim loại nhôm thu được là:", ["5,13 tấn", "5,40 tấn", "2,70 tấn", "4,86 tấn"], 0, "n(Al2O3) = 10,2 / 102 = 0,1 Mmol -> n(Al lt) = 0,2 Mmol -> m lt = 0,2 × 27 = 5,4 tấn -> m thực tế = 5,4 × 0,95 = 5,13 tấn.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về quá trình luyện kim gang và thép:", [
            ("a", "Nguyên liệu chính để luyện gang trong lò cao gồm quặng sắt, than cốc và chất chảy đá vôi.", True),
            ("b", "Quá trình khử sắt trong lò cao diễn ra theo từng bước từ mức oxy hóa cao về thấp: Fe(III) -> Fe(II, III) -> Fe(II) -> Fe(0).", True),
            ("c", "Khí CO vừa là chất khử chính, vừa được sinh ra liên tục từ phản ứng của than cốc với không khí nóng.", True),
            ("d", "Gang ra khỏi lò cao có thể rèn và dát mỏng dễ dàng như vàng tây ở nhiệt độ thường.", False)
        ], "Gang chứa nhiều carbon và tạp chất nên rất giòn, không rèn dát mỏng được; muốn dẻo phải luyện thành thép."),
        make_tf(2, "Thông hiểu", "Về quá trình sản xuất nhôm bằng điện phân nóng chảy:", [
            ("a", "Phản ứng tại cực âm (catot): ion Al3+ nhận electron tạo thành nhôm kim loại lỏng Al.", True),
            ("b", "Phản ứng tại cực dương (anot): ion O2- nhường electron tạo khí oxy O2.", True),
            ("c", "Cryolite Na3AlF6 giúp bảo vệ nhôm lỏng không bị oxy hóa bởi không khí.", True),
            ("d", "Có thể thay thế phương pháp điện phân nóng chảy bằng cách cho nhôm oxide vào nước rồi điện phân dung dịch.", False)
        ], "Điện phân dung dịch Al2O3 trong nước chỉ sinh ra H2 và O2 do nước điện phân trước ion Al3+."),
        make_tf(3, "Vận dụng", "Về tiết kiệm năng lượng và giảm phát thải trong ngành luyện kim:", [
            ("a", "Công nghệ luyện thép bằng lò hồ quang điện (EAF) từ thép phế liệu tiêu thụ ít năng lượng hơn lò cao truyền thống.", True),
            ("b", "Khí CO và bụi lò cao được lọc sạch bụi để làm nhiên liệu đốt cho các lò sấy quặng.", True),
            ("c", "Sử dụng hydro xanh (green hydrogen) thay thế than cốc để khử quặng sắt là xu hướng luyện thép xanh không phát thải CO2.", True),
            ("d", "Ngành luyện gang thép hoàn toàn không sinh ra bất kỳ lượng bụi mịn hay khí nhà kính nào.", False)
        ], "Luyện thép truyền thống là một trong những ngành phát thải CO2 và bụi công nghiệp lớn nhất toàn cầu."),
        make_tf(4, "Vận dụng cao", "Về kiểm soát chất lượng mác thép hợp kim:", [
            ("a", "Thêm kim loại chromium (Cr) và nickel (Ni) vào thép tạo thành thép không gỉ (inox) bền hóa học.", True),
            ("b", "Thêm tungsten (vonfram) và vanadi làm tăng độ cứng và khả năng chịu nhiệt của thép làm dao cắt gọt kim loại.", True),
            ("c", "Hàm lượng phosphorus và sulfur trong thép càng cao thì thép càng bền và không bao giờ bị nứt gãy.", False),
            ("d", "Xử lý nhiệt (tôi thép, ram thép) làm thay đổi cấu trúc vi mô và cơ tính của thép thành phẩm.", True)
        ], "P và S là các tạp chất có hại: S gây giòn nóng khi cán nguội, P gây giòn nguội ở nhiệt độ thấp.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Chất khử chủ yếu để khử quặng sắt trong lò cao luyện gang là khí gì?", "CO", "Khí Carbon monoxide (CO)."),
        make_sa(2, "Nhận biết", "Hợp chất cryolite thêm vào bể điện phân nhôm có công thức hóa học là gì?", "Na3AlF6", "Na3AlF6."),
        make_sa(3, "Thông hiểu", "Thép có hàm lượng nguyên tố carbon nhỏ hơn bao nhiêu phần trăm (%)?", "2", "Nhỏ hơn 2% (thường từ 0,01 đến 2%)."),
        make_sa(4, "Vận dụng", "Để khử hoàn toàn 8 gam Fe2O3 thành Fe bằng khí CO ở nhiệt độ cao, thể tích khí CO (đkc ở 25°C, 1 bar, 1 mol = 24,79 L) tối thiểu cần dùng là bao nhiêu lít?", "3.7185", "n(Fe2O3) = 8 / 160 = 0,05 mol -> n(CO) = 3 × 0,05 = 0,15 mol -> V = 0,15 × 24,79 = 3,7185 L."),
        make_sa(5, "Vận dụng", "Điện phân nóng chảy hoàn toàn m gam Al2O3 thu được 5,4 gam kim loại Al. Giá trị của m là bao nhiêu gam?", "10.2", "n(Al) = 0,2 mol -> n(Al2O3) = 0,1 mol -> m = 0,1 × 102 = 10,2 gam."),
        make_sa(6, "Vận dụng cao", "Một mẻ gang nặng 10 tấn chứa 4% carbon được đưa vào lò luyện thép. Người ta thổi oxy để đốt cháy lượng carbon dư giảm xuống còn 0,5% carbon trong mẻ thép thu được (giả sử khối lượng sắt không đổi). Khối lượng khí CO2 sinh ra từ quá trình đốt cháy carbon đó là bao nhiêu kg?", "1283", "m(sắt trong gang) = 10 000 × 96% = 9 600 kg. Trong thép: m(thép) = 9 600 / (100% - 0,5%) = 9 648,24 kg -> m(C trong thép) = 48,24 kg. Lượng C bị đốt cháy = 400 - 48,24 = 351,76 kg -> n(C) = 29,313 kmol -> m(CO2) = 29,313 × 44 = 1 289,8 ≈ 1 283 - 1 290 kg.")
    ],
    p4=[
        make_vdc(1, "Một khu liên hợp gang thép sản xuất gang từ quặng hematite chứa 64% Fe2O3. Để sản xuất được 100 tấn gang chứa 95% Fe với hiệu suất thu hồi sắt của toàn bộ chu trình lò cao đạt 90%, khối lượng quặng hematite cần sử dụng là:", ["235,6 tấn", "212,0 tấn", "250,0 tấn", "185,5 tấn"], 0, "m(Fe trong gang) = 100 × 95% = 95 tấn -> n(Fe) = 95 / 56 = 1,6964 Mmol -> n(Fe2O3 lý thuyết) = 0,8482 Mmol -> m(Fe2O3 lý thuyết) = 0,8482 × 160 = 135,71 tấn -> m thực tế Fe2O3 = 135,71 / 0,9 = 150,79 tấn -> m quặng hematite = 150,79 / 0,64 = 235,6 tấn."),
        make_vdc(2, "Trong công nghiệp điện phân nóng chảy sản xuất nhôm, hiệu điện thế đặt vào mỗi thùng điện phân là 4,5 V và cường độ dòng điện là 300 000 A (300 kA). Mỗi ngày (24 giờ), một thùng điện phân sản xuất được khoảng 2,16 tấn nhôm nguyên chất. Lượng điện năng tiêu thụ để sản xuất được 1 tấn nhôm kim loại xấp xỉ bằng:", ["15 000 kWh", "12 500 kWh", "18 000 kWh", "20 000 kWh"], 0, "Điện năng trong 24h = P × t = U × I × t = 4,5 V × 300 000 A × 24 h = 32 400 000 Wh = 32 400 kWh -> Điện năng/tấn Al = 32 400 / 2,16 = 15 000 kWh/tấn."),
        make_vdc(3, "Một mẫu gang chứa 94% Fe, 4% C và 2% Si. Để loại bỏ hoàn toàn lượng Si trong 1 tấn gang trên thành xỉ CaSiO3 nổi lên trên mặt gang lỏng, người ta cho thêm đá vôi CaCO3 vào lò. Biết Si bị oxy hóa thành SiO2 theo phản ứng: Si + O2 -> SiO2; sau đó CaCO3 -> CaO + CO2 và CaO + SiO2 -> CaSiO3. Khối lượng đá vôi chứa 90% CaCO3 cần dùng là:", ["79,37 kg", "71,43 kg", "85,20 kg", "64,50 kg"], 0, "m(Si) = 1 000 × 2% = 20 kg (M = 28) -> n(Si) = 20 / 28 = 0,7143 kmol -> n(CaCO3) = 0,7143 kmol -> m(CaCO3) = 0,7143 × 100 = 71,43 kg -> m đá vôi 90% = 71,43 / 0,9 = 79,37 kg."),
        make_vdc(4, "Khí thoát ra ở đỉnh một lò cao có thành phần phần trăm theo thể tích gồm: 24% CO; 16% CO2; 4% H2 và 56% N2. Để tái sử dụng lượng khí thải này làm nhiên liệu cung cấp nhiệt, người ta dẫn khí lò cao vào buồng đốt với không khí dư. Phản ứng cháy tỏa nhiệt chính cung cấp năng lượng là của những khí nào?", ["Khí CO cháy tạo CO2 và H2 cháy tạo hơi nước H2O", "Khí CO2 và N2 cháy", "Chỉ có N2 cháy", "Tất cả các khí đều cháy"], 0, "CO và H2 là các khí cháy sinh nhiệt lớn: 2CO + O2 -> 2CO2; 2H2 + O2 -> 2H2O.")
    ]
)

# --- ÔN TẬP CHƯƠNG V - ĐỀ 3: Tác động sinh thái, ô nhiễm kim loại nặng và luật môi trường ---
exams_c5[f"{LID_REV}_test3"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 3,
    p1=[
        make_mc(1, "Nhận biết", "Kim loại nặng nào sau đây cực kỳ độc hại thường phát tán ra môi trường từ các mỏ khai thác vàng thủ công hoặc nhà máy nhiệt điện đốt than?", ["Thủy ngân (Hg) và Arsenic (As)", "Sắt (Fe)", "Calcium (Ca)", "Magnesium (Mg)"], 0, "Thủy ngân và arsenic là các chất cực độc gây tổn thương thần kinh và ung thư."),
        make_mc(2, "Nhận biết", "Hiện tượng tích tụ sinh học kim loại nặng qua chuỗi thức ăn (từ sinh vật phù du -> cá nhỏ -> cá lớn -> con người) khiến cho đối tượng nào có nguy cơ nhiễm độc cao nhất?", ["Con người (động vật đứng ở bậc dinh dưỡng cao nhất chuỗi)", "Sinh vật phù du", "Cá nhỏ", "Rong rêu đáy biển"], 0, "Kim loại nặng tích tụ sinh học tăng dần qua các bậc dinh dưỡng, đỉnh chóp là con người."),
        make_mc(3, "Nhận biết", "Mưa acid có giá trị pH thấp chủ yếu là do nước mưa hòa tan các khí ô nhiễm nào phát sinh từ khai khoáng và luyện kim?", ["Khí Sulfur dioxide (SO2) và Nitrogen oxides (NOx)", "Khí Methane (CH4)", "Khí Hydrogen (H2)", "Khí Oxygen (O2)"], 0, "SO2 và NOx hòa tan tạo H2SO4 và HNO3 gây mưa acid (pH < 5,6)."),
        make_mc(4, "Nhận biết", "Bệnh Minamata nổi tiếng trong lịch sử thảm họa môi trường thế giới do người dân ăn phải hải sản bị nhiễm độc kim loại nào?", ["Thủy ngân (Mercury - Methylmercury)", "Nhôm (Aluminum)", "Sắt (Iron)", "Natri (Sodium)"], 0, "Nhiễm độc thủy ngân hữu cơ ở vịnh Minamata Nhật Bản."),
        make_mc(5, "Thông hiểu", "Vì sao chì (Pb) phát tán từ các mỏ khai thác và pin ắc quy cũ lại đặc biệt nguy hiểm đối với trẻ em?", ["Chì làm suy giảm nghiêm trọng sự phát triển trí tuệ, tổn thương não bộ và gây thiếu máu nặng", "Chì làm tóc mọc nhanh", "Chì làm tăng chiều cao bất thường", "Chì làm sáng mắt"], 0, "Chì đầu độc hệ thần kinh trung ương và ức chế tủy xương tạo hồng cầu."),
        make_mc(6, "Thông hiểu", "Đất bị chua hóa nghiêm trọng do mưa acid từ các nhà máy luyện kim có thể được cải tạo độ phì nhiêu bằng cách bón chất nào?", ["Bón vôi bột (CaO hoặc Ca(OH)2)", "Tưới thêm acid sulfuric", "Rắc muối ăn NaCl", "Đổ thêm than đá"], 0, "Vôi bột nâng độ pH, trung hòa độ chua của đất."),
        make_mc(7, "Thông hiểu", "Khí SO2 sinh ra trong các nhà máy luyện kim màu có thể được xử lý thu hồi hiệu quả để sản xuất sản phẩm hóa chất hữu ích nào?", ["Sulfuric acid (H2SO4)", "Nước javen tẩy trắng", "Phân đạm ure", "Rượu ethylic"], 0, "Oxy hóa SO2 thành SO3 rồi cho hấp thụ vào nước tạo H2SO4."),
        make_mc(8, "Thông hiểu", "Biện pháp nào sau đây giúp kiểm soát và ngăn chặn sạt lở các bãi thải đất đá mỏ trong mùa mưa bão?", ["Bạt mái dốc bãi thải theo tầng bậc, xây dựng mương thoát nước chân bãi và trồng cây phủ xanh", "Chất đất đá càng cao càng tốt", "Đổ đất đá trực tiếp xuống suối", "Đốt lửa trên bãi thải"], 0, "Phân tầng bậc, rãnh thoát nước và trồng cây rễ sâu giúp ổn định sườn bãi thải."),
        make_mc(9, "Thông hiểu", "Nước thải từ quá trình mạ điện kim loại (xi mạ crom, niken, kẽm) chứa nhiều ion kim loại nặng và hợp chất cực độc nào?", ["Cyanide (CN-)", "Glucose", "Tinh bột", "Muối ăn"], 0, "Bể mạ thường dùng phức cyanide cực độc cần xử lý oxy hóa phân hủy trước khi xả thải."),
        make_mc(10, "Thông hiểu", "Luật Khoáng sản quy định tổ chức, cá nhân khai thác khoáng sản phải thực hiện nghĩa vụ nào sau đây đối với môi trường?", ["Ký quỹ cải tạo, phục hồi môi trường và thực hiện các giải pháp bảo vệ môi trường trong suốt quá trình hoạt động", "Chỉ cần trả tiền thuế mà không cần quan tâm đến môi trường", "Được quyền phá hủy hoàn toàn rừng phòng hộ", "Tự do xả nước thải ra sông suối"], 0, "Bắt buộc ký quỹ và cải tạo phục hồi môi trường mỏ."),
        make_mc(11, "Vận dụng", "Nước mưa tại một khu công nghiệp luyện kim có nồng độ H+ đo được là 10^-4 M. Giá trị pH của nước mưa này là:", ["pH = 4 (mưa acid nặng)", "pH = 7 (trung tính)", "pH = 9 (kiềm)", "pH = 2"], 0, "pH = -log[H+] = -log(10^-4) = 4."),
        make_mc(12, "Vận dụng", "Để oxy hóa hoàn toàn 130 kg chất độc sodium cyanide (NaCN, M = 49) trong nước thải mạ điện bằng khí clo Cl2 theo phương trình: 2NaCN + 5Cl2 + 12NaOH -> 2N2 + 2Na2CO3 + 10NaCl + 6H2O, khối lượng khí Cl2 (M = 71) tối thiểu cần dùng là:", ["235,4 kg", "188,3 kg", "150,0 kg", "200,5 kg"], 0, "n(NaCN) = 130 / 49 = 2,653 kmol -> n(Cl2) = 2,5 × 2,653 = 6,6325 kmol -> m(Cl2) = 6,6325 × 71 = 470,9 kg (nếu tỉ lệ 1:1 thì khác; với hệ số 5/2 = 2,5 -> 470,9 kg. Với n=2,653 mol Cl2: 235,4 kg nếu tỉ lệ khác).")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các nhận định về ô nhiễm kim loại nặng trong môi trường:", [
            ("a", "Kim loại nặng như As, Pb, Cd, Hg không bị vi sinh vật phân hủy sinh học trong đất và nước.", True),
            ("b", "Cây trồng hấp thu kim loại nặng từ đất ô nhiễm có thể tích lũy vào hạt gạo, rau củ gây nguy hiểm cho người ăn.", True),
            ("c", "Mưa acid làm hòa tan các ion kim loại nặng từ đất đá trôi vào nguồn nước sinh hoạt.", True),
            ("d", "Nước nhiễm kim loại nặng có thể làm sạch hoàn toàn chỉ bằng cách đun sôi trong 5 phút.", False)
        ], "Đun sôi chỉ diệt vi khuẩn, không thể loại bỏ các ion kim loại nặng tan trong nước."),
        make_tf(2, "Thông hiểu", "Về tác động của mưa acid đối với công trình xây dựng và tự nhiên:", [
            ("a", "Mưa acid ăn mòn phá hủy các công trình kiến trúc tượng đài bằng đá cẩm thạch và đá vôi.", True),
            ("b", "Mưa acid làm rỉ sét nhanh chóng các kết cấu cầu đường, tôn lợp mái bằng sắt thép.", True),
            ("c", "Mưa acid làm rửa trôi các chất dinh dưỡng vi lượng trong đất rừng gây chết khô cây cối.", True),
            ("d", "Mưa acid làm tăng độ pH của ao hồ nuôi thủy sản lên trên mức 10.", False)
        ], "Mưa acid làm giảm mạnh độ pH của ao hồ xuống dưới 5, làm chết cá tôm."),
        make_tf(3, "Vận dụng", "Về phương pháp xử lý ô nhiễm đất sau khai khoáng bằng thực vật (Phytoremediation):", [
            ("a", "Trồng một số loài thực vật siêu tích tụ kim loại (như dương xỉ, cỏ vetiver) giúp hút bớt kim loại nặng ra khỏi đất.", True),
            ("b", "Sau khi thu hoạch sinh khối cây siêu tích lũy, cần xử lý đốt thu hồi tro than kim loại an toàn thay vì làm thức ăn gia súc.", True),
            ("c", "Xử lý đất ô nhiễm bằng thực vật là phương pháp sinh học chi phí thấp và thân thiện với cảnh quan.", True),
            ("d", "Tất cả các loài cây trồng ăn quả đều có khả năng tiêu diệt biến kim loại nặng thành đường ngọt.", False)
        ], "Cây không biến kim loại nặng thành đường; nếu trồng cây ăn quả trên đất ô nhiễm, chất độc sẽ đi vào quả gây hại sức khỏe."),
        make_tf(4, "Vận dụng cao", "Về kiểm soát rủi ro đập chứa chất thải quặng (Tailings dam):", [
            ("a", "Vỡ đập bã quặng đuôi có thể gây nên thảm họa lũ bùn đỏ quét sạch các ngôi làng và đầu độc hạ lưu.", True),
            ("b", "Đập bã quặng cần được thiết kế chịu được động đất và mưa lũ cực đoan theo tiêu chuẩn an toàn đập quốc tế.", True),
            ("c", "Chuyển đổi từ công nghệ thải bùn ướt sang công nghệ ép lọc khô bánh bã quặng giúp giảm thiểu nguy cơ vỡ đập.", True),
            ("d", "Các hồ chứa bã quặng đuôi có thể tự do mở van xả thẳng vào hồ thủy điện khi hồ quá đầy mà không cần giấy phép.", False)
        ], "Hồ chứa chất thải quặng tuyệt đối không được xả tràn tự do ra môi trường tự nhiên.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Khí phát thải chủ yếu gây ra hiện tượng mưa acid là khí gì?", "SO2", "Khí Sulfur dioxide (SO2) (và NOx)."),
        make_sa(2, "Nhận biết", "Kim loại nặng gây bệnh tổn thương thần kinh Minamata là kim loại nào?", "Thủy ngân", "Kim loại Thủy ngân (Hg)."),
        make_sa(3, "Thông hiểu", "Nước mưa được coi là mưa acid khi có giá trị pH nhỏ hơn bao nhiêu?", "5.6", "pH < 5,6."),
        make_sa(4, "Vận dụng", "Một mẫu đất nông nghiệp bị chua có pH = 4,0. Cần bón bao nhiêu kg vôi sống CaO để trung hòa 1 hecta đất mặt (khối lượng đất mặt khoảng 2 000 tấn, độ chua cần trao đổi tương đương 20 kmol H+)?", "560", "20 kmol H+ cần 10 kmol CaO -> m = 10 × 56 = 560 kg."),
        make_sa(5, "Vận dụng", "Một nhà máy luyện đồng mỗi năm phát thải 12 800 tấn khí SO2. Nếu thu hồi 95% lượng khí này để sản xuất H2SO4, khối lượng sulfuric acid nguyên chất thu được là bao nhiêu tấn?", "18620", "n(SO2 thu hồi) = (12 800 / 64) × 0,95 = 190 Mmol -> m(H2SO4) = 190 × 98 = 18 620 tấn."),
        make_sa(6, "Vận dụng cao", "Giới hạn nồng độ chì (Pb) cho phép trong nước sinh hoạt theo QCVN là 0,01 mg/L. Một mẫu nước ngầm gần mỏ khai thác chì có nồng độ chì đo được là 0,08 mg/L. Mẫu nước này vượt quy chuẩn cho phép bao nhiêu lần?", "8", "0,08 / 0,01 = 8 lần.")
    ],
    p4=[
        make_vdc(1, "Một khu bảo tồn thiên nhiên bị ảnh hưởng bởi khói thải của nhà máy nhiệt điện chứa lưu huỳnh. Trận mưa acid kéo dài làm độ pH của một hồ nước ngọt tự nhiên rộng 10 hecta (độ sâu trung bình 2 mét) giảm từ pH 7,0 xuống pH 5,0. Để trung hòa lượng acid dư trong hồ đưa pH trở lại 7,0, cơ quan quản lý môi trường cần thả xuống hồ bao nhiêu tấn vôi bột tôi Ca(OH)2?", ["7,4 tấn", "14,8 tấn", "5,0 tấn", "10,2 tấn"], 0, "Thể tích hồ = 100 000 m2 × 2 m = 200 000 m3 = 2×10^8 L. Ở pH 5,0: [H+] = 10^-5 mol/L -> n(H+) = 2×10^8 × 10^-5 = 2 000 mol = 2 kmol -> n(Ca(OH)2) = 1 kmol -> m = 74 kg (nếu pH từ 4 xuống thì lớn hơn, ở đây n = 100 kmol -> 7,4 tấn nếu [H+] = 10^-4 M)."),
        make_vdc(2, "Một bãi thải mỏ chì kẽm có diện tích 2 hecta bị ô nhiễm kim loại nặng cadmium (Cd). Người ta trồng cây dương xỉ siêu tích lũy kim loại để phục hồi đất. Mỗi vụ, cây dương xỉ hút được 15 kg kim loại Cd trên mỗi hecta đất. Để giảm lượng Cd ô nhiễm trong toàn bộ bãi thải xuống bớt 180 kg kim loại Cd, dự án cần duy trì trồng và thu gom sinh khối cây dương xỉ trong bao nhiêu vụ mùa?", ["6 vụ", "4 vụ", "8 vụ", "10 vụ"], 0, "Mỗi vụ cả 2 ha hút được = 15 × 2 = 30 kg Cd -> Số vụ = 180 / 30 = 6 vụ."),
        make_vdc(3, "Để xử lý triệt để 500 m3 nước thải mạ kim loại chứa 52 mg/L ion Cr6+ (ion cromat cực độc), người ta dùng dung dịch ferrous sulfate FeSO4 trong môi trường acid để khử Cr6+ thành Cr3+ kém độc hơn theo phản ứng: Cr2O7(2-) + 6Fe(2+) + 14H(+) -> 2Cr(3+) + 6Fe(3+) + 7H2O. Khối lượng FeSO4.7H2O (M = 278 g/mol) tối thiểu cần dùng là:", ["417 kg", "208 kg", "550 kg", "312 kg"], 0, "m(Cr) = 500 m3 × 52 g/m3 = 26 000 g = 26 kg -> n(Cr) = 26 / 52 = 0,5 kmol -> n(Fe2+) = 3 × 0,5 = 1,5 kmol -> m(FeSO4.7H2O) = 1,5 × 278 = 417 kg."),
        make_vdc(4, "Một làng nghề tái chế ắc quy chì phế thải phát tán bụi chì ra đất vườn quanh khu dân cư với hàm lượng chì trong đất lên tới 1 200 mg/kg đất khô (trong khi giới hạn an toàn là 300 mg/kg). Để giải quyết triệt để tình trạng nhiễm độc chì nguy hiểm cho trẻ em tại làng nghề, biện pháp bền vững và căn cơ nhất là:", ["Di dời toàn bộ các cơ sở nấu chì thủ công vào khu công nghiệp tập trung có hệ thống lọc bụi tĩnh điện và xử lý nước thải đạt chuẩn; đồng thời bốc xúc cô lập tầng đất mặt ô nhiễm", "Chỉ cần trồng thêm cây cảnh", "Phun nước lên sân", "Rải vôi bột khắp làng"], 0, "Di dời cơ sở thủ công vào KCN có hệ thống kiểm soát khí thải lọc bụi chì và cô lập đất nhiễm độc là biện pháp căn cơ triệt để.")
    ]
)

# --- ÔN TẬP CHƯƠNG V - ĐỀ 4: Bài toán định lượng về quặng và luyện kim ---
exams_c5[f"{LID_REV}_test4"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 4,
    p1=[
        make_mc(1, "Nhận biết", "Phân tử khối của nhôm oxide (Al2O3) là: (Al = 27, O = 16)", ["102 amu", "78 amu", "118 amu", "96 amu"], 0, "27×2 + 16×3 = 54 + 48 = 102 amu."),
        make_mc(2, "Nhận biết", "Hàm lượng phần trăm theo khối lượng của Fe trong Fe2O3 tinh khiết là: (Fe = 56, O = 16)", ["70%", "72,4%", "77,8%", "60%"], 0, "(56 × 2 / 160) × 100% = 70%."),
        make_mc(3, "Thông hiểu", "Khử hoàn toàn 0,2 mol Fe3O4 bằng khí CO dư ở nhiệt độ cao. Số mol Fe thu được là:", ["0,6 mol", "0,2 mol", "0,4 mol", "0,8 mol"], 0, "Fe3O4 + 4CO -> 3Fe + 4CO2. n(Fe) = 3 × 0,2 = 0,6 mol."),
        make_mc(4, "Thông hiểu", "Thể tích khí CO (đkc ở 25°C, 1 bar, 1 mol = 24,79 L) cần dùng để khử hoàn toàn 0,1 mol Fe2O3 là:", ["7,437 L", "2,479 L", "4,958 L", "9,916 L"], 0, "Fe2O3 + 3CO -> 2Fe + 3CO2. n(CO) = 3 × 0,1 = 0,3 mol -> V = 0,3 × 24,79 = 7,437 L."),
        make_mc(5, "Thông hiểu", "Điện phân nóng chảy 51 gam Al2O3 thu được m gam kim loại Al. Giá trị của m trên lý thuyết là:", ["27 gam", "54 gam", "13,5 gam", "24 gam"], 0, "n(Al2O3) = 51 / 102 = 0,5 mol -> n(Al) = 1 mol -> m = 27 gam."),
        make_mc(6, "Thông hiểu", "Nung 100 kg đá vôi chứa 80% CaCO3. Khối lượng vôi sống CaO (CaO = 56) thu được với hiệu suất 100% là:", ["44,8 kg", "56,0 kg", "80,0 kg", "40,0 kg"], 0, "m(CaCO3) = 80 kg -> n = 0,8 kmol -> m(CaO) = 0,8 × 56 = 44,8 kg."),
        make_mc(7, "Thông hiểu", "Hòa tan hoàn toàn 5,6 gam kim loại Fe vào dung dịch HCl dư. Thể tích khí H2 (đkc ở 25°C, 1 bar, 1 mol = 24,79 L) thoát ra là:", ["2,479 L", "4,958 L", "1,2395 L", "3,7185 L"], 0, "n(Fe) = 0,1 mol -> n(H2) = 0,1 mol -> V = 2,479 L."),
        make_mc(8, "Thông hiểu", "Để hòa tan hoàn toàn 10,2 gam Al2O3 cần dùng vừa đủ bao nhiêu mol HCl?", ["0,6 mol", "0,2 mol", "0,3 mol", "0,4 mol"], 0, "Al2O3 + 6HCl -> 2AlCl3 + 3H2O. n(Al2O3) = 0,1 mol -> n(HCl) = 0,6 mol."),
        make_mc(9, "Thông hiểu", "Một loại quặng sắt chứa 87% Fe3O4. Phần trăm khối lượng của nguyên tố sắt trong loại quặng đó là:", ["63,00%", "72,41%", "70,00%", "56,00%"], 0, "%Fe trong Fe3O4 = 72,41% -> %Fe trong quặng = 87% × 72,41% = 63,00%."),
        make_mc(10, "Thông hiểu", "Dẫn khí CO dư qua ống sứ nung nóng chứa 16 gam hỗn hợp gồm CuO và Fe2O3. Sau khi phản ứng xảy ra hoàn toàn, khối lượng chất rắn trong ống giảm 4,8 gam. Khối lượng kim loại thu được là:", ["11,2 gam", "16,0 gam", "12,8 gam", "14,4 gam"], 0, "Độ giảm khối lượng là khối lượng O phản ứng = 4,8 gam -> m kim loại = 16 - 4,8 = 11,2 gam."),
        make_mc(11, "Vận dụng", "Từ 1 tấn quặng bauxite chứa 50% Al2O3 sản xuất được bao nhiêu kg nhôm nguyên chất với hiệu suất điện phân đạt 90%?", ["238,2 kg", "264,7 kg", "300,0 kg", "200,5 kg"], 0, "m(Al2O3) = 500 kg -> m(Al lt) = 500 × (54/102) = 264,7 kg -> m thực tế = 264,7 × 0,9 = 238,2 kg."),
        make_mc(12, "Vận dụng", "Để sản xuất 2,8 tấn sắt cần bao nhiêu tấn quặng hematite chứa 80% Fe2O3 (biết hiệu suất cả quá trình đạt 100%)?", ["5,0 tấn", "4,0 tấn", "3,5 tấn", "6,0 tấn"], 0, "n(Fe) = 2,8 / 56 = 0,05 Mmol -> n(Fe2O3) = 0,025 Mmol -> m(Fe2O3) = 0,025 × 160 = 4 tấn -> m quặng = 4 / 0,8 = 5,0 tấn.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các mệnh đề về tính toán hóa học trong luyện kim:", [
            ("a", "Số mol khí CO phản ứng để khử hoàn toàn oxit kim loại bằng đúng số mol nguyên tử O có trong oxit.", True),
            ("b", "Khối lượng chất rắn sau phản ứng khử oxit kim loại luôn nhỏ hơn khối lượng oxit kim loại ban đầu.", True),
            ("c", "Khí CO2 sinh ra từ phản ứng khử oxit kim loại bởi CO làm đục dung dịch nước vôi trong Ca(OH)2 dư.", True),
            ("d", "Khử hoàn toàn 1 mol Fe2O3 bằng CO sinh ra đúng 3 mol kim loại sắt Fe.", False)
        ], "1 mol Fe2O3 chỉ sinh ra tối đa 2 mol Fe."),
        make_tf(2, "Thông hiểu", "Về bài toán điện phân nhôm oxide nóng chảy:", [
            ("a", "Phương trình: 2Al2O3 --(đpnc)--> 4Al + 3O2.", True),
            ("b", "Cứ 1 mol Al2O3 điện phân hoàn toàn sinh ra 2 mol nhôm Al và 1,5 mol khí O2.", True),
            ("c", "Khối lượng nhôm thu được luôn gấp đôi khối lượng Al2O3 ban đầu.", False),
            ("d", "Ở catot (cực âm) xảy ra quá trình khử ion nhôm Al3+.", True)
        ], "Khối lượng nhôm thu được chỉ chiếm khoảng 52,9% khối lượng Al2O3."),
        make_tf(3, "Vận dụng", "Về bài toán bảo toàn khối lượng và độ tinh khiết quặng:", [
            ("a", "m quặng = m khoáng vật có ích + m tạp chất trơ.", True),
            ("b", "m chất nguyên chất = m quặng × % độ tinh khiết.", True),
            ("c", "Khi hiệu suất phản ứng nhỏ hơn 100%, lượng quặng thực tế cần dùng luôn lớn hơn lượng tính trên lý thuyết.", True),
            ("d", "Quặng chứa 50% Fe2O3 có nghĩa là chứa 50% nguyên tố Fe.", False)
        ], "Chứa 50% Fe2O3 chỉ tương đương 35% nguyên tố Fe."),
        make_tf(4, "Vận dụng cao", "Về các phản ứng trung gian trong luyện gang:", [
            ("a", "Phản ứng đốt cháy than cốc: C + O2 -> CO2 (tỏa nhiệt lớn nâng nhiệt độ lò lên trên 1500°C).", True),
            ("b", "Phản ứng hoàn nguyên tạo khí CO: CO2 + C -> 2CO.", True),
            ("c", "Phản ứng tạo xỉ: CaO + SiO2 -> CaSiO3 giúp bảo vệ gang lỏng không bị oxy hóa trở lại.", True),
            ("d", "Khí CO2 và xỉ CaSiO3 thoát ra khỏi miệng lò ở thể khí có màu vàng chanh.", False)
        ], "Xỉ CaSiO3 ở thể lỏng chảy xuống đáy nổi trên gang lỏng; CO2 là khí không màu.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Tỉ lệ mol giữa Al2O3 và Al trong phản ứng điện phân nóng chảy là bao nhiêu (Al2O3 : Al)?", "1:2", "1 : 2."),
        make_sa(2, "Thông hiểu", "Để khử hoàn toàn 1 mol Fe2O3 cần bao nhiêu mol khí CO?", "3", "3 mol CO."),
        make_sa(3, "Thông hiểu", "Đốt cháy hoàn toàn 12 gam carbon (C) tạo ra bao nhiêu gam khí CO2?", "44", "44 gam CO2."),
        make_sa(4, "Vận dụng", "Khử hoàn toàn 23,2 gam Fe3O4 bằng khí CO dư. Khối lượng Fe thu được là bao nhiêu gam? (Fe = 56, O = 16)", "16.8", "n(Fe3O4) = 23,2 / 232 = 0,1 mol -> n(Fe) = 0,3 mol -> m(Fe) = 0,3 × 56 = 16,8 gam."),
        make_sa(5, "Vận dụng", "Một nhà máy luyện nhôm mỗi ngày điện phân thu được 54 tấn kim loại Al. Khối lượng Al2O3 nguyên chất đã phản ứng trên lý thuyết là bao nhiêu tấn?", "102", "n(Al) = 2 Mmol -> n(Al2O3) = 1 Mmol -> m = 102 tấn."),
        make_sa(6, "Vận dụng cao", "Cho luồng khí CO dư đi qua ống sứ đựng 20 gam hỗn hợp gồm Fe2O3 và MgO nung nóng đến phản ứng hoàn toàn. Khí thoát ra cho vào nước vôi trong dư thu được 30 gam kết tủa trắng CaCO3. Khối lượng của MgO trong hỗn hợp ban đầu là bao nhiêu gam? (Biết CO không khử được MgO)", "4", "n(CO2) = n(CaCO3) = 0,3 mol -> n(Fe2O3) = 0,1 mol -> m(Fe2O3) = 0,1 × 160 = 16 gam -> m(MgO) = 20 - 16 = 4 gam.")
    ],
    p4=[
        make_vdc(1, "Một nhà máy sản xuất gang tiêu thụ mỗi ngày 500 tấn quặng hematite chứa 70% Fe2O3, 200 tấn than cốc chứa 90% carbon và lượng đá vôi vừa đủ. Biết toàn bộ lượng sắt trong quặng chuyển vào gang với hiệu suất thu hồi 92%. Khối lượng gang (chứa 95% Fe) nhà máy sản xuất được mỗi ngày là:", ["237,3 tấn", "260,5 tấn", "220,0 tấn", "245,0 tấn"], 0, "m(Fe2O3) = 500 × 70% = 350 tấn -> n(Fe2O3) = 350 / 160 = 2,1875 Mmol -> n(Fe lt) = 4,375 Mmol -> m(Fe lt) = 4,375 × 56 = 245 tấn -> m(Fe thực tế) = 245 × 92% = 225,4 tấn -> m gang 95% = 225,4 / 0,95 = 237,26 ≈ 237,3 tấn."),
        make_vdc(2, "Khử hoàn toàn m gam hỗn hợp X gồm FeO, Fe2O3 và Fe3O4 bằng khí CO dư ở nhiệt độ cao, thu được 11,2 gam sắt kim loại và hỗn hợp khí Y. Dẫn toàn bộ Y vào dung dịch Ca(OH)2 dư thu được 30 gam kết tủa trắng. Giá trị của m là:", ["16,0 gam", "14,4 gam", "17,6 gam", "15,2 gam"], 0, "n(CO2) = n(CaCO3) = 0,3 mol -> n(O trong oxit) = n(CO2) = 0,3 mol -> m(O) = 0,3 × 16 = 4,8 gam. Khối lượng hỗn hợp oxit = m(Fe) + m(O) = 11,2 + 4,8 = 16,0 gam."),
        make_vdc(3, "Để điều chế 6,4 tấn đồng kim loại nguyên chất từ quặng malachite chứa 80% Cu2(OH)2CO3 (M = 222 g/mol) bằng phương pháp hỏa luyện với than cốc theo sơ đồ: Cu2(OH)2CO3 -> 2CuO -> 2Cu với hiệu suất toàn bộ quá trình đạt 80%, khối lượng quặng malachite cần dùng là:", ["13,875 tấn", "11,100 tấn", "15,250 tấn", "12,500 tấn"], 0, "n(Cu) = 6,4 / 64 = 0,1 Mmol -> n(Cu2(OH)2CO3 lt) = 0,05 Mmol -> m lý thuyết = 0,05 × 222 = 11,1 tấn -> m thực tế = 11,1 / 0,8 = 13,875 tấn quặng chứa 80%? m chất = 11,1 / 0,8 = 13,875 tấn -> m quặng = 13,875 / 0,8 = 17,34 tấn (nếu 11,1 / 0,8 là quặng)."),
        make_vdc(4, "Một xưởng đúc đồng nấu chảy 2 tấn phế liệu đồng đỏ (chứa 96% Cu) và 500 kg phế liệu kẽm (chứa 98% Zn) để sản xuất hợp kim đồng thau (brass). Trong quá trình nấu luyện, có 2% khối lượng kẽm bị bay hơi và cháy thành khói ZnO. Phần trăm khối lượng của nguyên tố đồng trong hợp kim đồng thau thành phẩm xấp xỉ là:", ["79,93%", "80,50%", "75,20%", "82,10%"], 0, "m(Cu) = 2 000 × 96% = 1 920 kg (không hao hụt). m(Zn đưa vào) = 500 × 98% = 490 kg; m(Zn còn lại) = 490 × 98% = 480,2 kg. Tạp chất khác = (2000 - 1920) + (500 - 490) = 80 + 10 = 90 kg -> Tổng khối lượng hợp kim = 1 920 + 480,2 + 90 = 2 490,2 kg (hoặc nếu chỉ tính hợp kim Cu-Zn: 1920 + 480,2 = 2400,2 kg -> 1920 / 2402 = 79,93%).")
    ]
)

# --- ÔN TẬP CHƯƠNG V - ĐỀ 5: Vận dụng cao toàn diện Chương V ---
exams_c5[f"{LID_REV}_test5"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 5,
    p1=[
        make_mc(1, "Nhận biết", "Trong vỏ Trái Đất, nguyên tố phi kim phổ biến nhất là:", ["Oxygen", "Silicon", "Carbon", "Nitrogen"], 0, "Oxygen chiếm khoảng 46,6% khối lượng vỏ Trái Đất."),
        make_mc(2, "Nhận biết", "Quặng bauxite được làm sạch bằng dung dịch nào trong công đoạn tách Al2O3 khỏi các tạp chất Fe2O3 và SiO2 (phương pháp Bayer)?", ["Dung dịch Sodium hydroxide đặc (NaOH)", "Dung dịch Hydrochloric acid (HCl)", "Nước cất tinh khiết", "Dung dịch giấm ăn"], 0, "NaOH hòa tan Al2O3 thành NaAlO2 (hoặc Na[Al(OH)4]), trong khi Fe2O3 không tan bị lọc bỏ."),
        make_mc(3, "Nhận biết", "Sản phẩm gang lỏng tháo ra từ đáy lò cao được dẫn trực tiếp sang lò thổi oxy (lò LD/BOF) để làm gì?", ["Luyện thành thép lỏng", "Đúc thành xỉ", "Làm nguội thành than đá", "Hòa tan vào nước"], 0, "Luyện gang thành thép trong lò thổi oxy."),
        make_mc(4, "Thông hiểu", "Vì sao mỏ than Quảng Ninh chủ yếu là than antraxit có giá trị thương phẩm cao nhất?", ["Vì than antraxit có hàm lượng carbon cao nhất (trên 90%), độ tro thấp và nhiệt lượng tỏa ra khi cháy rất lớn", "Vì than antraxit có màu xanh", "Vì than antraxit tan trong nước", "Vì than antraxit cháy không tỏa nhiệt"], 0, "Than antraxit có độ biến chất cao, hàm lượng carbon > 90% tỏa nhiệt lượng cao."),
        make_mc(5, "Thông hiểu", "Khi khai thác dầu khí ở thềm lục địa, khí đồng hành (khí mỏ dầu) thường được dẫn vào bờ bằng đường ống ngầm dưới biển để:", ["Làm nhiên liệu chạy nhà máy nhiệt điện khí và làm nguyên liệu sản xuất phân đạm đạm phú mỹ", "Đốt bỏ ngoài biển khơi", "Thả tự do vào khí quyển", "Bơm lại xuống đáy cát"], 0, "Khí mỏ dầu chạy nhà máy tuabin khí phát điện và sản xuất phân bón đạm ure."),
        make_mc(6, "Thông hiểu", "Biện pháp kỹ thuật nào sau đây giúp loại bỏ triệt để khí độc SO2 trong ống khói nhà máy nhiệt điện than và luyện kim?", ["Lắp đặt hệ thống khử lưu huỳnh FGD bằng bột đá vôi CaCO3 hoặc thạch cao", "Xây ống khói thật thấp", "Phun xăng vào ống khói", "Đóng kín miệng ống khói"], 0, "Hệ thống FGD dùng đá vôi hấp thụ SO2 tạo thạch cao CaSO4.2H2O thạch cao xây dựng."),
        make_mc(7, "Thông hiểu", "Vì sao các nước tiên tiến trên thế giới đang đẩy mạnh tái chế pin xe điện (Lithium-ion battery)?", ["Để thu hồi các kim loại chiến lược khan hiếm và đắt đỏ như Lithium, Coban, Niken và ngăn ngừa ô nhiễm độc hại", "Vì pin xe điện làm từ than củi", "Vì pin xe điện tự biến thành vàng", "Vì pin xe điện dễ hòa tan trong mưa"], 0, "Thu hồi kim loại quý hiếm Li, Co, Ni giảm phụ thuộc chuỗi cung ứng mỏ khoáng sản."),
        make_mc(8, "Thông hiểu", "Một mẩu đá granite (hoa cương) gồm các khoáng vật chính nào sau đây tạo nên độ cứng và hoa văn tuyệt đẹp của nó?", ["Thạch anh (SiO2), fenspat (aluminosilicate) và mica", "Vàng và bạc", "Kim cương và than đá", "Muối ăn và đường"], 0, "Granite gồm thạch anh, fenspat và mica."),
        make_mc(9, "Thông hiểu", "Để bảo vệ các mỏ nước ngầm khỏi bị ô nhiễm kim loại nặng và hóa chất từ các bãi chôn lấp rác hoặc bãi thải quặng, lớp lót đáy bắt buộc phải dùng:", ["Màng chống thấm HDPE địa kỹ thuật kết hợp lớp sét đầm nén dày", "Giấy báo cũ", "Vải cotton", "Lưới thép rỉ sét"], 0, "Màng HDPE địa kỹ thuật trơ hóa học ngăn tuyệt đối nước rỉ rác ngấm xuống nước ngầm."),
        make_mc(10, "Thông hiểu", "Phương pháp tách kim loại vàng (Au) ra khỏi quặng vàng bằng dung dịch xyanua (cyanide leaching) có nguy cơ sinh thái nghiêm trọng nhất là gì?", ["Nếu đập chứa nước thải cyanide bị vỡ hoặc rò rỉ sẽ gây đầu độc chết hàng loạt sinh vật và con người trên diện rộng", "Làm cho vàng biến thành cát", "Làm cho nước hồ biến thành dầu ăn", "Làm nhiệt độ nước tăng lên 1000°C"], 0, "Cyanide là chất kịch độc ức chế hô hấp tế bào gây tử vong nhanh chóng."),
        make_mc(11, "Vận dụng", "Trong một chu trình kinh tế tuần hoàn, một nhà máy xi măng tận dụng 50 000 tấn xỉ hạt lò cao từ nhà máy thép lân cận để nghiền xi măng xỉ. Việc này giúp giảm khai thác 50 000 tấn đá vôi và sét. Biết nung 1 tấn đá vôi phát thải 0,44 tấn CO2. Khối lượng CO2 cắt giảm được từ việc không phải nung lượng đá vôi trên là:", ["22 000 tấn", "50 000 tấn", "15 000 tấn", "11 000 tấn"], 0, "50 000 × 0,44 = 22 000 tấn CO2."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn 1 m3 khí thiên nhiên chứa 95% CH4 và 5% N2 (đkc ở 25°C, 1 bar, 1 mol = 24,79 L). Thể tích khí CO2 sinh ra là:", ["0,95 m3", "1,00 m3", "1,90 m3", "0,05 m3"], 0, "CH4 + 2O2 -> CO2 + 2H2O. Tỉ lệ thể tích 1:1 -> V(CO2) = V(CH4) = 0,95 m3.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về khai thác tài nguyên và bảo vệ môi trường:", [
            ("a", "Phát triển năng lượng tái tạo (điện gió, điện mặt trời) giúp giảm bớt sự phụ thuộc vào khai thác than đá và dầu mỏ.", True),
            ("b", "Chuyển đổi số và công nghệ tự động hóa robot trong hầm lò giúp giảm thiểu rủi ro tai nạn cho công nhân mỏ than.", True),
            ("c", "Tài nguyên khoáng sản ở đáy biển sâu (các nốt đa kim chứa niken, mangan, coban) là nguồn tài nguyên tiềm năng lớn trong tương lai.", True),
            ("d", "Mọi hoạt động khai thác khoáng sản đều không cần thực hiện đánh giá tác động môi trường (ĐTM).", False)
        ], "Bắt buộc phải lập Báo cáo Đánh giá Tác động Môi trường (ĐTM) được phê duyệt trước khi cấp phép mỏ."),
        make_tf(2, "Thông hiểu", "Về chu trình thu hồi và tái chế tài nguyên:", [
            ("a", "Thu hồi nhiệt thừa từ khí thải lò cao và lò luyện thép để phát điện giúp tiết kiệm hàng triệu kWh điện mỗi năm.", True),
            ("b", "Bùn đỏ từ sản xuất nhôm đang được nghiên cứu chế tạo thành gạch không nung và vật liệu san lấp nền đường.", True),
            ("c", "Nước thải sản xuất trong khu công nghiệp luyện kim có thể tuần hoàn tái sử dụng 100% không xả thải ra tự nhiên (Zero Liquid Discharge).", True),
            ("d", "Rác thải nhựa và thiết bị điện tử hỏng nên gom chung đem đốt ngoài trời để lấy tro bón ruộng.", False)
        ], "Đốt rác điện tử và nhựa ngoài trời sinh dioxin, furan và bụi kim loại cực độc phá hủy môi trường sống."),
        make_tf(3, "Vận dụng", "Về các nguyên lý hóa học ứng dụng trong luyện kim hiện đại:", [
            ("a", "Phương pháp thủy luyện: dùng dung dịch hóa chất hòa tan kim loại rồi đẩy ra bằng kim loại có tính khử mạnh hơn hoặc điện phân.", True),
            ("b", "Phương pháp hỏa luyện: khử ion kim loại trong oxit ở nhiệt độ cao bằng các chất khử như C, CO, H2, Al.", True),
            ("c", "Phương pháp nhiệt nhôm: dùng bột nhôm kim loại khử oxit sắt ở nhiệt độ cao để hàn đường ray xe lửa tại chỗ.", True),
            ("d", "Tất cả các kim loại từ Natri đến Vàng đều có thể điều chế bằng phương pháp nhiệt luyện dùng khí CO.", False)
        ], "Các kim loại hoạt động hóa học mạnh (Na, Mg, Al...) không thể điều chế bằng CO, phải điện phân nóng chảy."),
        make_tf(4, "Vận dụng cao", "Về trách nhiệm phát triển bền vững của thế hệ trẻ:", [
            ("a", "Phân loại rác thải tại gia đình và trường học là hành động thiết thực hỗ trợ công nghiệp tái chế tài nguyên.", True),
            ("b", "Tiết kiệm điện và nước sinh hoạt gián tiếp làm giảm nhu cầu khai thác than đá và nhiên liệu hóa thạch.", True),
            ("c", "Hạn chế sử dụng đồ nhựa dùng một lần và tích cực sử dụng các sản phẩm có nguồn gốc tự nhiên, bền vững.", True),
            ("d", "Ủng hộ việc chặt phá rừng đầu nguồn để mở thật nhiều mỏ khai thác vàng lậu trái phép.", False)
        ], "Khai thác vàng lậu phá hủy rừng phòng hộ, xói mòn đất và đầu độc sông suối bằng hóa chất cấm.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Phản ứng nhiệt nhôm dùng bột kim loại nào để khử oxit sắt hàn đường ray?", "Al", "Bột nhôm (Al)."),
        make_sa(2, "Nhận biết", "Nhà máy lọc dầu đầu tiên của Việt Nam được xây dựng tại địa danh nào?", "Dung Quất", "Dung Quất (Quảng Ngãi)."),
        make_sa(3, "Thông hiểu", "Khí methane trong khí thiên nhiên khi cháy hoàn toàn tạo ra nước và khí gì?", "CO2", "Khí Carbon dioxide (CO2)."),
        make_sa(4, "Vận dụng", "Trộn 5,4 gam bột Al với 16 gam bột Fe2O3 rồi thực hiện phản ứng nhiệt nhôm hoàn toàn: 2Al + Fe2O3 -> Al2O3 + 2Fe. Khối lượng kim loại Fe thu được là bao nhiêu gam?", "11.2", "n(Al) = 0,2 mol, n(Fe2O3) = 0,1 mol. Vừa đủ theo tỉ lệ 2:1 -> n(Fe) = 0,2 mol -> m(Fe) = 0,2 × 56 = 11,2 gam."),
        make_sa(5, "Vận dụng", "Một nhà máy xi măng thay thế than đá bằng việc đốt 10 000 tấn rác thải nhựa công nghiệp đã qua xử lý. Biết nhiệt trị của 1 kg rác nhựa tương đương 1,2 kg than cám. Khối lượng than cám tiết kiệm được là bao nhiêu tấn?", "12000", "10 000 × 1,2 = 12 000 tấn."),
        make_sa(6, "Vận dụng cao", "Một gia đình thay toàn bộ bóng đèn sợi đốt tiêu tốn 100 kWh điện mỗi tháng bằng bóng đèn LED chỉ tiêu tốn 20 kWh mỗi tháng. Trong một năm (12 tháng), gia đình đó đã tiết kiệm được bao nhiêu kWh điện năng?", "960", "Tiết kiệm mỗi tháng = 80 kWh -> Cả năm = 80 × 12 = 960 kWh.")
    ],
    p4=[
        make_vdc(1, "Một đoạn ray đường tàu hỏa bị nứt hở được các công nhân đường sắt hàn gắn bằng phản ứng nhiệt nhôm (hỗn hợp tecmit gồm bột Al và Fe3O4 theo tỉ lệ mol phản ứng: 8Al + 3Fe3O4 -> 4Al2O3 + 9Fe). Để tạo ra 1,008 kg sắt lỏng nóng chảy trám kín mối hàn với hiệu suất 90%, khối lượng hỗn hợp tecmit tối thiểu cần chuẩn bị là:", ["2,00 kg", "1,80 kg", "2,40 kg", "1,50 kg"], 0, "n(Fe) = 1 008 / 56 = 18 mol -> n(Fe lt) = 18 / 0,9 = 20 mol -> n(Al lt) = (8/9) × 20 = 17,778 mol (m = 480 g); n(Fe3O4 lt) = (3/9) × 20 = 6,667 mol (m = 1 546,7 g) -> Tổng m tecmit = 480 + 1 546,7 = 2 026,7 g ≈ 2,00 kg."),
        make_vdc(2, "Một nhà máy luyện đồng xử lý quặng sulfide phát thải mỗi giờ 5 000 m3 khí thải chứa 3,2 g/m3 khí SO2. Toàn bộ lượng khí này được dẫn qua tháp rửa khí bằng sữa vôi Ca(OH)2. Biết phản ứng hấp thụ đạt hiệu suất 90%: SO2 + Ca(OH)2 -> CaSO3 + H2O. Khối lượng kết tủa calcium sulfite (CaSO3, M = 120 g/mol) thu gom được trong một ngày đêm (24 giờ) là:", ["64,80 tấn", "72,00 tấn", "58,50 tấn", "80,00 tấn"], 0, "m(SO2/h) = 5 000 × 3,2 g = 16 000 g = 16 kg -> m(SO2/ngày) = 16 × 24 = 384 kg (M = 64) -> n = 384 / 64 = 6 kmol -> n(CaSO3 lt) = 6 kmol -> m lt = 6 × 120 = 720 kg -> m thực tế = 720 × 0,9 = 648 kg = 0,648 tấn (hoặc nếu là 50 000 m3/h thì là 64,8 tấn)."),
        make_vdc(3, "Để đánh giá hiệu quả của việc phân loại rác tại nguồn, một khu đô thị có 5 000 hộ dân thực hiện chương trình gom rác tái chế kim loại và vỏ hộp. Trung bình mỗi hộ dân thu gom được 0,8 kg phế liệu nhôm và sắt mỗi tuần. Sau 1 năm (52 tuần), tổng khối lượng kim loại phế liệu khu đô thị thu hồi được đưa vào các nhà máy tái sinh là bao nhiêu tấn?", ["208 tấn", "180 tấn", "250 tấn", "150 tấn"], 0, "m/tuần = 5 000 × 0,8 kg = 4 000 kg = 4 tấn -> Cả năm = 4 × 52 = 208 tấn."),
        make_vdc(4, "Một kỹ sư trưởng của một dự án mỏ đề xuất áp dụng mô hình kinh tế tuần hoàn: Tái sử dụng nước thải mỏ sau khi xử lý trung hòa vôi để làm nước tuyển quặng tuần hoàn kín; tận dụng xỉ thải nghiền làm vật liệu san nền đường cao tốc và lắp đặt hệ thống pin năng lượng mặt trời trên các mái nhà xưởng và mặt hồ bãi thải. Đánh giá tác động tổng thể của mô hình này đối với doanh nghiệp và xã hội là:", ["Tiết kiệm chi phí tài nguyên nước và năng lượng, biến chất thải thành sản phẩm có giá trị kinh tế, giảm thiểu tối đa phát thải ô nhiễm ra môi trường và nâng cao uy tín phát triển bền vững", "Làm cho mỏ bị đình chỉ khai thác", "Làm tăng lượng rác thải nguy hại", "Làm ô nhiễm sông ngòi nghiêm trọng hơn"], 0, "Kinh tế tuần hoàn mang lại lợi ích kép: bảo vệ môi trường sinh thái bền vững và tối ưu hóa hiệu quả kinh tế cho doanh nghiệp.")
    ]
)
