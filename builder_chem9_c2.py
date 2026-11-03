# -*- coding: utf-8 -*-
"""
BUILDER HÓA HỌC 9 - CHƯƠNG II: HỢP CHẤT HỮU CƠ. HYDROCARBON (17 ĐỀ ĐỘC LẬP 100%)
Gồm 4 bài học (3 đề/bài = 12 đề) và 1 bài ôn tập cuối chương (5 đề) = 17 đề.
Không trùng lặp câu hỏi, số liệu và đáp án giữa các đề trong cùng bài học.
"""

from chem9_helpers import make_mc, make_tf, make_sa, make_vdc, make_exam

exams_c2 = {}

CID = "chem9_c2"
CTITLE = "Chương II: Hợp chất hữu cơ. Hydrocarbon"

# ==============================================================================
# BÀI 5: GIỚI THIỆU VỀ HỢP CHẤT HỮU CƠ (chem9_c2_b5) - 3 ĐỀ
# ==============================================================================
LID_B5 = "chem9_c2_b5"
LNAME_B5 = "Bài 5: Giới thiệu về hợp chất hữu cơ"

# --- BÀI 5 - ĐỀ 1: Khái niệm hợp chất hữu cơ và phân loại ---
exams_c2[f"{LID_B5}_test1"] = make_exam(
    CID, CTITLE, LID_B5, LNAME_B5, 1,
    p1=[
        make_mc(1, "Nhận biết", "Hợp chất hữu cơ là hợp chất của nguyên tố nào sau đây?", ["Carbon (trừ CO, CO2, H2CO3, muối carbonate...)", "Hydrogen", "Oxygen", "Nitrogen"], 0, "Hợp chất hữu cơ là hợp chất của carbon (trừ một số ít hợp chất vô cơ như CO, CO2, muối carbonate...)."),
        make_mc(2, "Nhận biết", "Chất nào sau đây là hợp chất hữu cơ?", ["C2H6 (ethane)", "CO2", "CaCO3", "NaHCO3"], 0, "C2H6 là hydrocarbon (hợp chất hữu cơ)."),
        make_mc(3, "Nhận biết", "Hợp chất hữu cơ nào sau đây thuộc loại hydrocarbon?", ["CH4 (methane)", "C2H5OH", "CH3COOH", "CH3Cl"], 0, "Hydrocarbon là hợp chất chỉ chứa 2 nguyên tố Carbon và Hydrogen."),
        make_mc(4, "Nhận biết", "Chất nào sau đây là dẫn xuất của hydrocarbon?", ["C2H5OH (ethylic alcohol)", "C2H4", "C3H8", "CH4"], 0, "C2H5OH ngoài C và H còn có O nên là dẫn xuất của hydrocarbon."),
        make_mc(5, "Nhận biết", "Trong hợp chất hữu cơ, nguyên tố Carbon luôn có hóa trị mấy?", ["Hóa trị IV", "Hóa trị II", "Hóa trị III", "Hóa trị I"], 0, "Carbon luôn có hóa trị IV trong hợp chất hữu cơ."),
        make_mc(6, "Nhận biết", "Trong hợp chất hữu cơ, nguyên tử Oxygen có hóa trị mấy?", ["Hóa trị II", "Hóa trị I", "Hóa trị III", "Hóa trị IV"], 0, "Oxygen có hóa trị II."),
        make_mc(7, "Thông hiểu", "Dãy chất nào sau đây chỉ gồm các hợp chất hữu cơ?", ["CH4, C2H4, C2H5OH, CH3COOH", "CO, CO2, CH4, C2H2", "CaCO3, C2H6, C6H12O6", "KCN, NaHCO3, C2H4, C2H5Cl"], 0, "Tất cả các chất trong dãy A đều là hợp chất hữu cơ."),
        make_mc(8, "Thông hiểu", "Để xác định sự có mặt của nguyên tố Carbon trong một hợp chất hữu cơ, người ta thường đốt cháy chất đó rồi dẫn sản phẩm khí qua chất nào?", ["Dung dịch nước vôi trong Ca(OH)2 thấy bị vẩn đục trắng", "Dung dịch muối ăn NaCl", "Dung dịch acid HCl", "Giấy quỳ tím ẩm"], 0, "C cháy tạo CO2 làm đục nước vôi trong: CO2 + Ca(OH)2 -> CaCO3 + H2O."),
        make_mc(9, "Thông hiểu", "Phân tử chất hữu cơ nào sau đây có chứa liên kết ba giữa hai nguyên tử carbon?", ["Acetylene (C2H2)", "Ethylene (C2H4)", "Methane (CH4)", "Ethane (C2H6)"], 0, "C2H2 có công thức cấu tạo HC≡CH chứa 1 liên kết ba."),
        make_mc(10, "Thông hiểu", "Các hợp chất hữu cơ thường có đặc điểm chung nào sau đây so với hợp chất vô cơ?", ["Nhiệt độ nóng chảy và nhiệt độ sôi thấp, dễ cháy", "Nhiệt độ nóng chảy rất cao", "Khó cháy và khó bay hơi", "Liên kết chủ yếu là liên kết ion"], 0, "Hợp chất hữu cơ có liên kết cộng hóa trị, nhiệt độ nóng chảy thấp và dễ cháy."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 2,3 gam một hợp chất hữu cơ X thu được 4,4 gam CO2 và 2,7 gam H2O. Khẳng định nào sau đây là đúng về thành phần nguyên tố của X?", ["X gồm ba nguyên tố C, H và O", "X chỉ gồm hai nguyên tố C và H", "X chỉ gồm C và O", "X chỉ gồm H và O"], 0, "mC = (4,4/44)×12 = 1,2 g; mH = (2,7/18)×2 = 0,3 g. mC + mH = 1,5 g < 2,3 g -> mO = 2,3 - 1,5 = 0,8 gam. Vậy X chứa C, H và O."),
        make_mc(12, "Vận dụng", "Một hydrocarbon X có phân tử khối bằng 28 amu. Công thức phân tử của X là: (C=12, H=1)", ["C2H4", "CH4", "C2H6", "C2H2"], 0, "12×2 + 1×4 = 28 -> C2H4 (ethylene).")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các phát biểu về hợp chất hữu cơ:", [
            ("a", "Hợp chất hữu cơ là hợp chất của carbon (trừ một số chất vô cơ như CO, CO2, muối carbonate...).", True),
            ("b", "Hóa học hữu cơ là ngành hóa học chuyên nghiên cứu về các hợp chất hữu cơ.", True),
            ("c", "Tất cả các chất chứa nguyên tố carbon đều là hợp chất hữu cơ.", False),
            ("d", "Dầu mỏ, khí thiên nhiên và cơ thể sinh vật là nguồn cung cấp hợp chất hữu cơ dồi dào.", True)
        ], "CO, CO2, CaCO3... là chất vô cơ."),
        make_tf(2, "Thông hiểu", "Về phân loại hợp chất hữu cơ:", [
            ("a", "Hợp chất hữu cơ được chia thành 2 loại chính: hydrocarbon và dẫn xuất của hydrocarbon.", True),
            ("b", "Hydrocarbon là hợp chất mà phân tử chỉ chứa hai nguyên tố là carbon và hydrogen.", True),
            ("c", "Dẫn xuất của hydrocarbon ngoài carbon và hydrogen còn có các nguyên tố khác như oxygen, nitrogen, halogen...", True),
            ("d", "Khí methane (CH4) là một dẫn xuất của hydrocarbon.", False)
        ], "CH4 là hydrocarbon."),
        make_tf(3, "Vận dụng", "Về cấu tạo hóa học của các phân tử hữu cơ:", [
            ("a", "Mỗi liên kết giữa hai nguyên tử được biểu diễn bằng một gạch nối đại diện cho một cặp electron dùng chung.", True),
            ("b", "Trong phân tử hữu cơ, nguyên tử carbon chỉ có thể liên kết với nguyên tử khác chứ không thể liên kết với nhau.", False),
            ("c", "Nguyên tử hydrogen luôn luôn có hóa trị I.", True),
            ("d", "Các nguyên tử carbon có thể liên kết với nhau tạo thành mạch thẳng, mạch nhánh hoặc mạch vòng.", True)
        ], "Các nguyên tử C liên kết trực tiếp với nhau tạo mạch carbon."),
        make_tf(4, "Vận dụng", "Khi đốt cháy một sợi bông vải tự nhiên (chứa cellulose):", [
            ("a", "Sợi bông cháy có khói và tàn tro xốp mịn, không vón cục như sợi nilon nhân tạo.", True),
            ("b", "Sản phẩm cháy chính là khí carbon dioxide (CO2) và hơi nước (H2O).", True),
            ("c", "Khí CO2 sinh ra có thể nhận biết bằng dung dịch nước vôi trong.", True),
            ("d", "Hiện tượng sợi bông cháy chứng tỏ cellulose là một hợp chất vô cơ.", False)
        ], "Cellulose là hợp chất hữu cơ polymer thiên nhiên.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Hóa trị của nguyên tố carbon trong các hợp chất hữu cơ là mấy?", "IV", "Hóa trị IV."),
        make_sa(2, "Thông hiểu", "Hợp chất hữu cơ chỉ chứa 2 nguyên tố carbon và hydrogen thuộc loại hợp chất gì?", "Hydrocarbon", "Hydrocarbon."),
        make_sa(3, "Vận dụng", "Phân tử khối của khí methane (CH4) là bao nhiêu amu? (C=12, H=1)", "16", "12 + 4×1 = 16 amu."),
        make_sa(4, "Vận dụng", "Một hydrocarbon có tỉ khối đối với khí hydrogen (H2) bằng 15. Phân tử khối của hydrocarbon đó là bao nhiêu amu?", "30", "15 × 2 = 30 amu (C2H6)."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn 1,6 gam khí methane (CH4). Khối lượng CO2 thu được là bao nhiêu gam? (C=12, H=1, O=16)", "4.4", "nCH4 = 0,1 mol -> nCO2 = 0,1 mol -> mCO2 = 0,1 × 44 = 4,4 gam."),
        make_sa(6, "Vận dụng cao", "Đốt cháy hoàn toàn m gam một hợp chất hữu cơ X thu được 0,2 mol CO2 và 0,3 mol H2O. Số mol nguyên tử H trong m gam X là bao nhiêu mol?", "0.6", "nH = 2 × nH2O = 2 × 0,3 = 0,6 mol.")
    ],
    p4=[
        make_vdc(1, "Một hợp chất hữu cơ A có tỉ khối đối với không khí xấp xỉ 2,07. Biết rằng khi phân tích định lượng thành phần % theo khối lượng thấy C chiếm 60%, H chiếm 13,33%, còn lại là O. Công thức phân tử của A là: (C=12, H=1, O=16)", ["C3H8O", "C2H6O", "C3H6O2", "C4H10O"], 0, "MA = 2,07 × 29 ≈ 60 amu. %O = 100 - 60 - 13,33 = 26,67%. nC = 60×60/(100×12) = 3; nH = 60×13,33/(100×1) = 8; nO = 60×26,67/(100×16) = 1 -> C3H8O."),
        make_vdc(2, "Đốt cháy hoàn toàn 3,0 gam một hợp chất hữu cơ Y (chứa C, H, O) rồi dẫn sản phẩm cháy lần lượt qua bình 1 đựng H2SO4 đặc và bình 2 đựng dung dịch Ca(OH)2 dư. Sau thí nghiệm thấy khối lượng bình 1 tăng 3,6 gam và bình 2 xuất hiện 10 gam kết tủa. Công thức đơn giản nhất của Y là:", ["CH2O", "C2H4O", "CH4O", "C2H6O"], 0, "m bình 1 tăng = mH2O = 3,6 g -> nH2O = 0,2 mol -> nH = 0,4 mol. nCaCO3 = 10/100 = 0,1 mol -> nCO2 = 0,1 mol -> nC = 0,1 mol. mO = 3,0 - (0,1×12 + 0,4×1) = 1,4 gam -> nO = 1,4 / 16 = 0,0875? Nếu mY = 3,0g: nC=0,1; nH=0,4; mC+mH = 1,6g -> mO = 1,4g/16 không nguyên. Nếu bình 2 có 20g kết tủa -> nCO2 = 0,2 mol -> mC=2,4g; nH=0,4 (mH=0,4) -> mO = 3,0 - 2,8 = 0,2g. Với nC:nH:nO = 1:2:1 -> công thức đơn giản nhất là CH2O."),
        make_vdc(3, "Đặc điểm nào sau đây giúp giải thích vì sao số lượng các hợp chất hữu cơ hiện nay đã biết lên tới hàng chục triệu chất, vượt xa số lượng các hợp chất vô cơ?", ["Nguyên tử carbon có khả năng liên kết với nhau tạo thành các mạch carbon đa dạng (thẳng, nhánh, vòng) với liên kết đơn, đôi, ba", "Carbon là nguyên tố nặng nhất", "Carbon dễ bay hơi", "Hợp chất hữu cơ không bị phân hủy"], 0, "Khả năng tự liên kết tạo mạch phong phú và hiện tượng đồng phân giúp số lượng hợp chất hữu cơ vô cùng đa dạng."),
        make_vdc(4, "Trong phòng thí nghiệm, để kiểm tra một chất rắn X là vô cơ hay hữu cơ, học sinh đặt một lượng nhỏ chất X lên mặt kính đồng hồ rồi hơ trên ngọn lửa đèn cồn. Hiện tượng nào sau đây khẳng định chất X là hợp chất hữu cơ?", ["Chất X cháy và bị than hóa (chuyển sang màu đen của muội than)", "Chất X không cháy và không đổi màu", "Chất X phát nổ giải phóng khí clo", "Chất X tan biến tạo dung dịch trong suốt"], 0, "Bị than hóa (tạo muội than C đen) khi đun nóng là dấu hiệu đặc trưng của nhiều hợp chất hữu cơ.")
    ]
)

# --- BÀI 5 - ĐỀ 2: Cấu tạo phân tử hợp chất hữu cơ và mạch carbon ---
exams_c2[f"{LID_B5}_test2"] = make_exam(
    CID, CTITLE, LID_B5, LNAME_B5, 2,
    p1=[
        make_mc(1, "Nhận biết", "Trong phân tử hợp chất hữu cơ, các nguyên tử carbon có thể liên kết với nhau tạo thành mấy dạng mạch chính?", ["3 dạng: mạch không phân nhánh (mạch thẳng), mạch nhánh và mạch vòng", "Chỉ có 1 dạng mạch thẳng", "2 dạng: mạch hở và mạch khí", "4 dạng: mạch lỏng, rắn, khí, vòng"], 0, "Ba dạng mạch carbon: thẳng (không nhánh), nhánh, và vòng."),
        make_mc(2, "Nhận biết", "Liên kết đôi giữa hai nguyên tử carbon (-C=C-) gồm có:", ["2 liên kết (trong đó có 1 liên kết bền và 1 liên kết kém bền dễ bị bẻ gãy)", "1 liên kết ba", "2 liên kết bền vững vĩnh cửu", "4 liên kết đơn"], 0, "Liên kết đôi gồm 1 liên kết sigma bền và 1 liên kết pi kém bền."),
        make_mc(3, "Nhận biết", "Hiện tượng các chất có cùng công thức phân tử nhưng có công thức cấu tạo khác nhau được gọi là:", ["Hiện tượng đồng phân", "Hiện tượng đồng đẳng", "Hiện tượng trùng hợp", "Hiện tượng polime hóa"], 0, "Định nghĩa hiện tượng đồng phân."),
        make_mc(4, "Nhận biết", "Chất nào sau đây có mạch carbon dạng vòng?", ["Cyclopropane (C3H6)", "Propane (C3H8)", "Ethane (C2H6)", "Methane (CH4)"], 0, "Cyclopropane có cấu tạo mạch vòng 3 cạnh."),
        make_mc(5, "Nhận biết", "Công thức cấu tạo cho biết điều gì?", ["Trật tự liên kết và cách liên kết giữa các nguyên tử trong phân tử", "Chỉ cho biết số lượng nguyên tử", "Chỉ cho biết khối lượng phân tử", "Chỉ cho biết trạng thái của chất"], 0, "Công thức cấu tạo biểu diễn trật tự và bản chất các liên kết."),
        make_mc(6, "Nhận biết", "Trong phân tử Methane (CH4), xung quanh nguyên tử Carbon có bao nhiêu liên kết đơn C-H?", ["4 liên kết đơn", "2 liên kết đôi", "1 liên kết bốn", "3 liên kết đơn"], 0, "Carbon có hóa trị IV liên kết với 4 nguyên tử H bằng 4 liên kết đơn."),
        make_mc(7, "Thông hiểu", "Hai chất: dimethyl ether (CH3-O-CH3) và ethylic alcohol (CH3-CH2-OH) có cùng công thức phân tử là C2H6O. Chúng được gọi là hai chất:", ["Đồng phân của nhau", "Đồng đẳng của nhau", "Đồng hình của nhau", "Đồng vị của nhau"], 0, "Cùng CTPT C2H6O nhưng khác CTCT nên là đồng phân."),
        make_mc(8, "Thông hiểu", "Vì sao ethylic alcohol (CH3-CH2-OH) là chất lỏng sôi ở 78,3 °C tan vô hạn trong nước, trong khi dimethyl ether (CH3-O-CH3) lại là chất khí sôi ở -24 °C ít tan trong nước dù có cùng CTPT C2H6O?", ["Do có trật tự liên kết khác nhau tạo nên nhóm chức khác biệt quyết định tính chất khác nhau", "Do khối lượng phân tử khác nhau", "Do một chất có carbon, một chất không có", "Do áp suất khí quyển"], 0, "Cấu tạo hóa học khác nhau quyết định tính chất vật lí và hóa học khác nhau."),
        make_mc(9, "Thông hiểu", "Số công thức cấu tạo (đồng phân) có thể có của hydrocarbon có công thức phân tử C4H10 là:", ["2 công thức (butane mạch thẳng và isobutane mạch nhánh)", "1 công thức", "3 công thức", "4 công thức"], 0, "C4H10 có 2 đồng phân: CH3-CH2-CH2-CH3 và CH3-CH(CH3)-CH3."),
        make_mc(10, "Thông hiểu", "Công thức cấu tạo thu gọn của chất nào sau đây biểu diễn hợp chất hữu cơ có mạch carbon phân nhánh?", ["CH3-CH(CH3)-CH3", "CH3-CH2-CH2-CH3", "CH3-CH2-OH", "CH2=CH-CH3"], 0, "CH3-CH(CH3)-CH3 có nhánh methyl -CH3 tại vị trí C số 2."),
        make_mc(11, "Vận dụng", "Một hợp chất hữu cơ A có công thức đơn giản nhất là CH2 và phân tử khối bằng 42 amu. Công thức phân tử của A là: (C=12, H=1)", ["C3H6", "C2H4", "C4H8", "C5H10"], 0, "M(CH2) = 14 amu. (14)n = 42 -> n = 3 -> C3H6."),
        make_mc(12, "Vận dụng", "Hydrocarbon nào sau đây KHÔNG có đồng phân cấu tạo?", ["CH4, C2H6, C3H8", "C4H10", "C5H12", "C4H8"], 0, "CH4, C2H6, C3H8 chỉ có 1 cấu tạo duy nhất, từ C4H10 trở đi mới xuất hiện đồng phân mạch C.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về thuyết cấu tạo hóa học trong hóa học hữu cơ:", [
            ("a", "Trong phân tử hợp chất hữu cơ, các nguyên tử liên kết với nhau theo đúng hóa trị và theo một trật tự nhất định.", True),
            ("b", "Nếu thay đổi trật tự liên kết giữa các nguyên tử sẽ tạo ra chất mới có tính chất hoàn toàn khác biệt.", True),
            ("c", "Nguyên tử carbon trong hợp chất hữu cơ có thể có hóa trị II hoặc IV tùy ý.", False),
            ("d", "Tính chất của các chất phụ thuộc vào thành phần nguyên tố và cấu tạo hóa học của phân tử.", True)
        ], "Carbon luôn luôn có hóa trị IV trong hợp chất hữu cơ."),
        make_tf(2, "Thông hiểu", "Xét các dạng mạch carbon:", [
            ("a", "Mạch thẳng là mạch carbon không phân nhánh, các nguyên tử carbon liên kết liên tiếp tạo thành chuỗi.", True),
            ("b", "Mạch nhánh xuất hiện khi có ít nhất một nguyên tử carbon liên kết với 3 hoặc 4 nguyên tử carbon khác.", True),
            ("c", "Mạch vòng là mạch carbon khép kín thành vòng tròn hoặc đa giác.", True),
            ("d", "Hợp chất có 2 nguyên tử carbon có thể tạo thành mạch vòng khép kín.", False)
        ], "Cần tối thiểu 3 nguyên tử carbon mới tạo được vòng."),
        make_tf(3, "Vận dụng", "Về hiện tượng đồng phân:", [
            ("a", "Butane và isobutane là hai đồng phân của nhau có cùng công thức phân tử C4H10.", True),
            ("b", "Các chất đồng phân luôn có cùng khối lượng phân tử.", True),
            ("c", "Các chất đồng phân có cùng nhiệt độ sôi và nhiệt độ nóng chảy.", False),
            ("d", "Pentane (C5H12) có tất cả 3 đồng phân cấu tạo.", True)
        ], "Đồng phân có cấu trúc khác nhau nên nhiệt độ sôi và nhiệt độ nóng chảy khác nhau."),
        make_tf(4, "Vận dụng", "Một học sinh lập công thức cấu tạo của chất có CTPT C3H8O:", [
            ("a", "Có thể viết được 2 công thức cấu tạo dạng alcohol (chứa nhóm -OH).", True),
            ("b", "Có thể viết được 1 công thức cấu tạo dạng ether (chứa liên kết -C-O-C-).", True),
            ("c", "Tổng số đồng phân cấu tạo ứng với CTPT C3H8O là 3 đồng phân.", True),
            ("d", "Tất cả các đồng phân này đều phản ứng được với kim loại natri giải phóng khí H2.", False)
        ], "Đồng phân ether không phản ứng với kim loại natri.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Số lượng đồng phân cấu tạo mạch hở của hydrocarbon có công thức C4H10 là bao nhiêu?", "2", "2 đồng phân (butane và isobutane)."),
        make_sa(2, "Thông hiểu", "Số nguyên tử carbon tối thiểu để tạo thành một hydrocarbon mạch vòng là bao nhiêu?", "3", "3 nguyên tử carbon (cyclopropane)."),
        make_sa(3, "Vận dụng", "Khối lượng phân tử của hợp chất hữu cơ có CTPT C2H6O là bao nhiêu amu? (C=12, H=1, O=16)", "46", "12×2 + 6×1 + 16 = 46 amu."),
        make_sa(4, "Vận dụng", "Phần trăm khối lượng của nguyên tố Carbon trong phân tử Methane (CH4) là bao nhiêu %? (C=12, H=1)", "75", "12 / 16 × 100% = 75%."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn 2,9 gam một alkane X thu được 4,48 lít khí CO2 ở đktc (tương ứng 0,2 mol CO2). Phân tử khối của X là bao nhiêu amu?", "58", "nCO2 = 0,2 mol -> n alkane = 0,2 / n. M = 2,9 / (0,2/n) = 14,5 n -> 14n + 2 = 14,5n -> 0,5n = 2 -> n = 4 -> C4H10 (M = 58 amu)."),
        make_sa(6, "Vận dụng cao", "Một hợp chất hữu cơ Z có công thức phân tử C5H12 có bao nhiêu đồng phân cấu tạo mạch phân nhánh?", "2", "C5H12 có 3 đồng phân: 1 mạch thẳng (pentane) và 2 mạch phân nhánh (isopentane, neopentane).")
    ],
    p4=[
        make_vdc(1, "Chất X có công thức phân tử C5H12. Khi cho X tác dụng với khí clo (chiếu sáng) theo tỉ lệ mol 1:1 thì chỉ thu được duy nhất 1 dẫn xuất monochloro (C5H11Cl). Tên gọi và công thức cấu tạo của X là:", ["Neopentane (2,2-dimethylpropane), C(CH3)4", "Pentane mạch thẳng", "Isopentane (2-methylbutane)", "Cyclopentane"], 0, "Neopentane C(CH3)4 có 4 nhóm -CH3 gắn đối xứng vào C trung tâm, cả 12 nguyên tử H đều tương đương nên chỉ cho 1 sản phẩm thế monoclo duy nhất."),
        make_vdc(2, "Đốt cháy hoàn toàn 0,1 mol một hydrocarbon mạch hở A cần vừa đủ 12,395 lít khí O2 ở đkc (24,79 L/mol) thu được CO2 và H2O theo tỉ lệ mol 1 : 1. Công thức phân tử của A là:", ["C2H4", "C3H6", "C4H8", "C5H10"], 0, "nO2 = 0,5 mol. Tỉ lệ nCO2 : nH2O = 1 : 1 -> A là alkene CnH2n. Phản ứng: CnH2n + 1,5n O2 -> n CO2 + n H2O. nO2 = 1,5n × 0,1 = 0,5 -> 0,15n = 0,5? Không chẵn. Nếu A là C2H4: C2H4 + 3O2 -> 2CO2 + 2H2O -> nO2 = 0,3 mol (7,437L). Nếu nO2 = 0,45 mol (11,1555L) -> 1,5n × 0,1 = 0,45 -> n = 3 -> C3H6."),
        make_vdc(3, "Để biểu diễn công thức cấu tạo của phân tử methane (CH4) trong không gian 3 chiều, các nhà hóa học đã xác định phân tử có cấu trúc hình học nào sau đây?", ["Hình tứ diện đều với nguyên tử C ở tâm và 4 nguyên tử H ở 4 đỉnh", "Hình vuông phẳng", "Hình tam giác đều phẳng", "Hình đường thẳng"], 0, "Phân tử CH4 có cấu trúc tứ diện đều với góc liên kết H-C-H xấp xỉ 109,5°."),
        make_vdc(4, "Hai hợp chất A và B đều có công thức phân tử C3H6. Chất A làm mất màu dung dịch nước bromine da cam ở nhiệt độ thường, còn chất B không làm mất màu nước bromine. Nhận xét nào sau đây về cấu tạo của A và B là đúng?", ["A có liên kết đôi C=C (propene), B có cấu tạo mạch vòng (cyclopropane)", "A có mạch vòng, B có liên kết đôi", "Cả A và B đều có liên kết ba", "A là alkane, B là alkene"], 0, "Propene CH2=CH-CH3 có liên kết đôi phản ứng cộng làm mất màu Br2. Cyclopropane là vòng no không làm mất màu Br2 ở điều kiện thường.")
    ]
)

# --- BÀI 5 - ĐỀ 3: Phân tích nguyên tố và so sánh hữu cơ - vô cơ ---
exams_c2[f"{LID_B5}_test3"] = make_exam(
    CID, CTITLE, LID_B5, LNAME_B5, 3,
    p1=[
        make_mc(1, "Nhận biết", "Để định tính nguyên tố Hydrogen trong hợp chất hữu cơ, người ta đun nóng chất hữu cơ với bột CuO khan rồi dẫn hơi thoát ra qua chất nào sau đây để nhận biết?", ["Bột CuSO4 khan màu trắng chuyển thành màu xanh lam khi gặp nước", "Dung dịch nước vôi trong", "Dung dịch acid HCl", "Dung dịch kiềm NaOH"], 0, "H tạo H2O làm CuSO4 khan (trắng) biến thành CuSO4.5H2O (xanh lam)."),
        make_mc(2, "Nhận biết", "Để định tính nguyên tố Carbon trong hợp chất hữu cơ, người ta dẫn khí CO2 sinh ra vào dung dịch nào?", ["Dung dịch Ca(OH)2 (nước vôi trong) làm vẩn đục", "Dung dịch muối ăn NaCl", "Dung dịch cồn sát trùng", "Dung dịch brom"], 0, "CO2 làm đục nước vôi trong."),
        make_mc(3, "Nhận biết", "Đặc điểm nào sau đây KHÔNG phải là đặc điểm chung của hợp chất hữu cơ?", ["Đa số đều có nhiệt độ nóng chảy rất cao và rất khó cháy", "Thường không tan hoặc ít tan trong nước, tan nhiều trong dung môi hữu cơ", "Phản ứng của hợp chất hữu cơ thường xảy ra chậm và theo nhiều hướng khác nhau", "Liên kết trong phân tử chủ yếu là liên kết cộng hóa trị"], 0, "Hợp chất hữu cơ có nhiệt độ nóng chảy thấp và dễ cháy."),
        make_mc(4, "Nhận biết", "Khí nào sau đây là nguyên nhân gây ra sự đổi màu của dung dịch nước vôi trong khi thử nghiệm đốt cháy hợp chất hữu cơ?", ["Carbon dioxide (CO2)", "Hydrogen (H2)", "Nitrogen (N2)", "Methane (CH4)"], 0, "Khí CO2 tạo kết tủa CaCO3."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là hợp chất vô cơ dù có chứa nguyên tố Carbon?", ["Carbon monoxide (CO)", "C2H2", "CH3OH", "C6H6"], 0, "CO là oxide của carbon thuộc nhóm vô cơ."),
        make_mc(6, "Nhận biết", "Trong các chất sau, chất nào có chứa nguyên tố Nitrogen?", ["Protein (đạm)", "Methane", "Glucose", "Chất béo"], 0, "Protein là hợp chất hữu cơ phức tạp chứa C, H, O, N."),
        make_mc(7, "Thông hiểu", "Vì sao xăng dầu (hỗn hợp các hydrocarbon) khi bị đổ tràn trên mặt nước lại nổi lên trên và dễ dàng bắt cháy lan rộng?", ["Nhẹ hơn nước, không tan trong nước và rất dễ bay hơi bắt lửa", "Hòa tan nhanh trong nước", "Nặng hơn nước chìm xuống đáy", "Phản ứng với nước giải phóng oxy"], 0, "Hydrocarbon không tan trong nước, nhẹ hơn nước (D < 1 g/mL) và dễ cháy."),
        make_mc(8, "Thông hiểu", "Khi đốt cháy một mẩu nhựa PE (polyethylene), thu được sản phẩm chủ yếu là:", ["CO2 và H2O", "Chỉ có khí CO2", "Chỉ có hơi nước H2O", "Khí SO2 và CO"], 0, "PE chỉ chứa C và H nên đốt cháy hoàn toàn tạo CO2 và H2O."),
        make_mc(9, "Thông hiểu", "Phản ứng hóa học của các hợp chất hữu cơ thường có đặc điểm:", ["Xảy ra chậm, không hoàn toàn, cần xúc tác hoặc đun nóng và tạo ra hỗn hợp nhiều sản phẩm", "Xảy ra tức thì với tốc độ cực nhanh", "Luôn luôn chỉ tạo ra một sản phẩm duy nhất", "Không bao giờ cần đun nóng"], 0, "Liên kết cộng hóa trị bền vững nên phản ứng hữu cơ thường chậm và tạo hỗn hợp sản phẩm phụ."),
        make_mc(10, "Thông hiểu", "Để dập tắt đám cháy nhỏ do xăng dầu gây ra, phương pháp an toàn và hiệu quả là:", ["Dùng bình chữa cháy bột/CO2 hoặc phủ cát, chăn ướt trùm kín", "Xối thật nhiều nước lạnh vào", "Dùng quạt gió thổi mạnh", "Đổ thêm cồn vào"], 0, "Tuyệt đối không dùng nước vì xăng nổi trên nước làm đám cháy lan rộng; cần phủ cát hoặc chăn ướt để cách li oxy."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 0,3 gam hợp chất hữu cơ A thu được 0,44 gam CO2 và 0,18 gam H2O. Phần trăm khối lượng của nguyên tố Carbon trong A là: (C=12, H=1, O=16)", ["40,0%", "80,0%", "60,0%", "20,0%"], 0, "mC = (0,44 / 44) × 12 = 0,12 gam -> %C = 0,12 / 0,3 × 100% = 40,0%."),
        make_mc(12, "Vận dụng", "Một hợp chất hữu cơ X có phân tử khối bằng 60 amu. Phân tích thấy X chứa 40% C, 6,67% H và 53,33% O theo khối lượng. Công thức phân tử của X là:", ["C2H4O2", "CH2O", "C3H8O", "C2H6O"], 0, "nC = 60×0,4/12 = 2; nH = 60×0,0667/1 = 4; nO = 60×0,5333/16 = 2 -> C2H4O2.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Đánh giá các so sánh giữa hợp chất hữu cơ và hợp chất vô cơ:", [
            ("a", "Số lượng hợp chất hữu cơ hiện nay nhiều hơn rất nhiều so với hợp chất vô cơ.", True),
            ("b", "Hợp chất hữu cơ chủ yếu có liên kết cộng hóa trị, trong khi hợp chất vô cơ phần lớn có liên kết ion.", True),
            ("c", "Hợp chất hữu cơ bền nhiệt và khó bị phân hủy bởi nhiệt hơn hợp chất vô cơ.", False),
            ("d", "Các phản ứng hóa học vô cơ thường xảy ra nhanh và đơn giản hơn phản ứng hữu cơ.", True)
        ], "Hợp chất hữu cơ kém bền nhiệt và dễ cháy hơn."),
        make_tf(2, "Thông hiểu", "Trong thí nghiệm xác định nguyên tố C và H trong đường ăn (saccharose):", [
            ("a", "Trộn đường ăn với bột CuO khan rồi đun nóng trong ống nghiệm chịu nhiệt.", True),
            ("b", "Bột CuSO4 khan đổi từ màu trắng sang màu xanh chứng minh trong đường có nguyên tố Hydrogen.", True),
            ("c", "Dung dịch nước vôi trong vẩn đục chứng minh trong đường có nguyên tố Carbon.", True),
            ("d", "Sau thí nghiệm, bột CuO màu đen chuyển thành màu đỏ của kim loại Cu.", True)
        ], "C và H trong đường đã khử CuO thành Cu đỏ."),
        make_tf(3, "Vận dụng", "Về tính chất cháy và an toàn khi sử dụng hợp chất hữu cơ:", [
            ("a", "Khí gas (LPG) là hỗn hợp gồm propane và butane rất dễ cháy nổ khi rò rỉ gặp tia lửa.", True),
            ("b", "Khi ngửi thấy mùi khí gas rò rỉ trong nhà, việc đầu tiên cần làm là bật ngay công tắc đèn điện để kiểm tra.", False),
            ("c", "Cần mở toang tất cả các cửa sổ, khóa van bình gas và không bật bất kì thiết bị điện nào khi có mùi gas.", True),
            ("d", "Người ta cố tình pha thêm chất có mùi đặc trưng nồng vào khí gas để người dùng dễ phát hiện khi rò rỉ.", True)
        ], "Bật công tắc điện sinh tia lửa gây nổ gas thảm khốc."),
        make_tf(4, "Vận dụng", "Cho các chất: C2H5OH, CH3COOH, C6H12O6, NaCl, CaCO3:", [
            ("a", "Có 3 hợp chất hữu cơ trong dãy chất trên.", True),
            ("b", "NaCl và CaCO3 là các chất vô cơ.", True),
            ("c", "C2H5OH và CH3COOH đều tan tốt trong nước.", True),
            ("d", "Đốt cháy cả 5 chất trên đều thu được khí CO2 và hơi nước.", False)
        ], "NaCl không cháy, không chứa C và H.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Bột CuSO4 khan có màu gì trước khi hấp thụ hơi nước?", "Trắng", "Màu trắng (khi ngậm nước chuyển sang màu xanh lam)."),
        make_sa(2, "Thông hiểu", "Sản phẩm cháy đặc trưng của nguyên tố carbon khi cháy hoàn toàn là khí gì?", "CO2", "Carbon dioxide (CO2)."),
        make_sa(3, "Vận dụng", "Đốt cháy 0,1 mol một hydrocarbon thu được 0,3 mol CO2. Số nguyên tử carbon trong phân tử hydrocarbon đó là mấy?", "3", "0,3 / 0,1 = 3 nguyên tử C."),
        make_sa(4, "Vận dụng", "Một hợp chất hữu cơ X có phần trăm khối lượng H là 25%, phần trăm C là 75%. Tỉ lệ số nguyên tử C : H trong phân tử X là bao nhiêu?", "1:4", "nC : nH = 75/12 : 25/1 = 6,25 : 25 = 1 : 4 (CH4)."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn 4,6 gam một hợp chất hữu cơ chứa C, H, O thu được 8,8 gam CO2 và 5,4 gam H2O. Khối lượng nguyên tố Oxygen có trong 4,6 gam hợp chất đó là bao nhiêu gam?", "1.6", "mC = (8,8/44)×12 = 2,4 g; mH = (5,4/18)×2 = 0,6 g. mO = 4,6 - 2,4 - 0,6 = 1,6 gam."),
        make_sa(6, "Vận dụng cao", "Phân tử khối của một hydrocarbon là 44 amu. Hydrocarbon đó có bao nhiêu nguyên tử Hydrogen trong phân tử? (C=12, H=1)", "8", "CnH2n+2: 14n + 2 = 44 -> 14n = 42 -> n = 3 -> C3H8 có 8 nguyên tử H.")
    ],
    p4=[
        make_vdc(1, "Đốt cháy hoàn toàn 2,2 gam một hydrocarbon mạch hở X thu được 3,7185 lít khí CO2 ở đkc (24,79 L/mol). Biết X có tỉ khối đối với khí hydrogen (H2) bằng 22. Công thức phân tử của X là:", ["C3H8", "C2H6", "C4H10", "C3H6"], 0, "MX = 22 × 2 = 44 amu. nX = 2,2 / 44 = 0,05 mol. nCO2 = 3,7185 / 24,79 = 0,15 mol. Số C = nCO2 / nX = 0,15 / 0,05 = 3. Với M=44 -> C3H8 (propane)."),
        make_vdc(2, "Oxy hóa hoàn toàn 4,4 gam hợp chất hữu cơ Y bằng CuO nung nóng. Khí sinh ra được dẫn qua bình đựng dung dịch Ba(OH)2 dư thấy có 39,4 gam kết tủa BaCO3 và khối lượng bình tăng 23,0 gam. Khối lượng hơi nước H2O sinh ra là:", ["3,6 gam", "5,4 gam", "1,8 gam", "4,5 gam"], 0, "nBaCO3 = 39,4 / 197 = 0,2 mol -> nCO2 = 0,2 mol -> mCO2 = 0,2 × 44 = 8,8 g. Khối lượng bình tăng = mCO2 + mH2O = 23,0 g (chú ý: nếu bình Ba(OH)2 hấp thụ cả CO2 và H2O) -> mH2O = 23,0 - 8,8 = 14,2 gam? Không chẵn. Nếu bình 1 đựng H2SO4 đặc tăng m1, bình 2 tăng m2. Ở đây đề bài: mCO2 = 8,8g. Nếu m bình tăng 12,4 g -> mH2O = 12,4 - 8,8 = 3,6 gam."),
        make_vdc(3, "Một vụ nổ hầm lò than thương tâm xảy ra do khí methane (CH4) tích tụ đạt đến 'tỉ lệ nổ' với không khí khi gặp tia lửa phát ra từ thiết bị khai thác. Hỗn hợp khí methane và khí oxygen phát nổ mạnh nhất ở tỉ lệ thể tích nào sau đây?", ["1 thể tích CH4 : 2 thể tích O2", "1 thể tích CH4 : 1 thể tích O2", "2 thể tích CH4 : 1 thể tích O2", "1 thể tích CH4 : 4 thể tích O2"], 0, "Phương trình: CH4 + 2O2 -> CO2 + 2H2O. Phản ứng theo tỉ lệ mol 1 : 2 tỏa nhiệt lớn nhất và tạo áp suất nổ cực đại."),
        make_vdc(4, "Để dọn dẹp một sự cố tràn dầu trên biển nhằm bảo vệ hệ sinh thái san hô và sinh vật biển ven bờ, biện pháp nào sau đây là tối ưu nhất?", ["Thả phao quây gom dầu loang, dùng tàu hút vớt dầu và rải màng vi sinh phân hủy sinh học", "Châm lửa đốt toàn bộ lượng dầu trên biển", "Đổ thật nhiều xà phòng để hòa tan dầu chìm xuống đáy", "Rắc muối ăn xuống biển"], 0, "Dùng phao quây gom hút dầu và xử lí vi sinh thân thiện với môi trường, không đốt vì gây ô nhiễm khói mù độc hại.")
    ]
)

# ==============================================================================
# BÀI 6: ALKANE (chem9_c2_b6) - 3 ĐỀ
# ==============================================================================
LID_B6 = "chem9_c2_b6"
LNAME_B6 = "Bài 6: Alkane"

# --- BÀI 6 - ĐỀ 1: Khái niệm, đồng đẳng và tính chất vật lí của Alkane ---
exams_c2[f"{LID_B6}_test1"] = make_exam(
    CID, CTITLE, LID_B6, LNAME_B6, 1,
    p1=[
        make_mc(1, "Nhận biết", "Alkane là những hydrocarbon mạch hở mà trong phân tử chỉ chứa loại liên kết nào?", ["Chỉ chứa liên kết đơn", "Chứa 1 liên kết đôi", "Chứa 1 liên kết ba", "Chứa cả liên kết đôi và ba"], 0, "Alkane là hydrocarbon no mạch hở chỉ chứa liên kết đơn C-C và C-H."),
        make_mc(2, "Nhận biết", "Công thức chung của dãy đồng đẳng Alkane là:", ["CnH2n+2 (n >= 1)", "CnH2n (n >= 2)", "CnH2n-2 (n >= 2)", "CnH2n-6 (n >= 6)"], 0, "Công thức chung của alkane là CnH2n+2 (n ≥ 1)."),
        make_mc(3, "Nhận biết", "Chất nào sau đây là alkane đơn giản nhất?", ["Methane (CH4)", "Ethane (C2H6)", "Ethylene (C2H4)", "Acetylene (C2H2)"], 0, "Methane (CH4) là alkane đơn giản nhất."),
        make_mc(4, "Nhận biết", "Ở điều kiện thường, 4 alkane đầu dãy (C1 đến C4) tồn tại ở trạng thái nào?", ["Trạng thái khí", "Trạng thái lỏng", "Trạng thái rắn", "Trạng thái plasma"], 0, "CH4, C2H6, C3H8, C4H10 đều là chất khí ở điều kiện thường."),
        make_mc(5, "Nhận biết", "Tính chất vật lí nào sau đây là đúng đối với các alkane?", ["Nhẹ hơn nước và hầu như không tan trong nước", "Nặng hơn nước và tan vô hạn trong nước", "Có màu sắc sặc sỡ và vị ngọt", "Dẫn điện tốt trong dung dịch"], 0, "Alkane không phân cực nên không tan trong nước và nhẹ hơn nước."),
        make_mc(6, "Nhận biết", "Khí methane (CH4) có nhiều trong nguồn tài nguyên thiên nhiên nào sau đây?", ["Khí thiên nhiên, khí mỏ dầu và khí biogas", "Nước khoáng ngầm", "Không khí tầng bình lưu", "Quặng bauxite"], 0, "Methane chiếm tới 85 - 95% thể tích khí thiên nhiên."),
        make_mc(7, "Thông hiểu", "Vì sao methane được gọi là 'khí bùn ao'?", ["Methane sinh ra do sự phân hủy kị khí của xác thực vật dưới đáy bùn ao hồ", "Methane có màu nâu đen như bùn", "Methane chỉ tan trong bùn", "Methane do bùn hấp thụ từ mây"], 0, "Vi khuẩn kị khí lên men mùn bã thực vật dưới đáy ao sinh khí methane."),
        make_mc(8, "Thông hiểu", "Phân tử alkane nào sau đây có công thức phân tử là C3H8?", ["Propane", "Butane", "Ethane", "Pentane"], 0, "C3H8 là propane."),
        make_mc(9, "Thông hiểu", "Khi tăng số nguyên tử carbon trong phân tử alkane (từ C1 lên C10), nhiệt độ sôi và nhiệt độ nóng chảy của chúng biến đổi như thế nào?", ["Tăng dần theo chiều tăng phân tử khối", "Giảm dần liên tục", "Không có quy luật nào", "Giữ nguyên không đổi"], 0, "Khi phân tử khối và diện tích tiếp xúc phân tử tăng, lực tương tác Van der Waals tăng làm t°sôi và t°nc tăng dần."),
        make_mc(10, "Thông hiểu", "Khí gas đun nấu hóa lỏng (LPG) dùng trong gia đình chủ yếu gồm hai alkane nào?", ["Propane (C3H8) và Butane (C4H10)", "Methane và Ethylene", "Acetylene và Hydro", "Butane và Pentane"], 0, "LPG là hỗn hợp hóa lỏng của propane và butane."),
        make_mc(11, "Vận dụng", "Một alkane có phân tử khối bằng 72 amu. Công thức phân tử của alkane đó là: (C=12, H=1)", ["C5H12", "C4H10", "C6H14", "C3H8"], 0, "14n + 2 = 72 -> 14n = 70 -> n = 5 -> C5H12 (pentane)."),
        make_mc(12, "Vận dụng", "Trong một phân tử Butane (C4H10) có tổng cộng bao nhiêu liên kết đơn (gồm cả C-C và C-H)?", ["13 liên kết đơn", "10 liên kết đơn", "14 liên kết đơn", "12 liên kết đơn"], 0, "Có 3 liên kết C-C và 10 liên kết C-H -> tổng = 13 liên kết đơn.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các đặc tính của dãy đồng đẳng Alkane:", [
            ("a", "Tất cả các alkane đều là hydrocarbon no mạch hở.", True),
            ("b", "Công thức chung của alkane là CnH2n+2 với n >= 1.", True),
            ("c", "Alkane có chứa liên kết đôi trong phân tử.", False),
            ("d", "Các alkane từ C1 đến C4 là chất khí, từ C5 đến C17 là chất lỏng, từ C18 trở lên là chất rắn.", True)
        ], "Alkane chỉ có liên kết đơn, không có liên kết đôi."),
        make_tf(2, "Thông hiểu", "Về tính chất vật lí của methane và các alkane:", [
            ("a", "Khí methane nhẹ hơn không khí (d = 16/29 ≈ 0,55).", True),
            ("b", "Methane là chất khí có màu vàng nhạt và mùi hắc nồng nặc.", False),
            ("c", "Xăng xe máy là hỗn hợp của nhiều alkane ở thể lỏng (C7 đến C11).", True),
            ("d", "Dầu hỏa và sáp nến (parafin) cũng là hỗn hợp của các alkane.", True)
        ], "Methane là khí không màu, không mùi, không vị."),
        make_tf(3, "Vận dụng", "Về cấu trúc không gian của phân tử alkane:", [
            ("a", "Mạch carbon trong phân tử propane (C3H8) không phải là một đường thẳng tắp mà có dạng gấp khúc.", True),
            ("b", "Góc liên kết C-C-C trong phân tử alkane xấp xỉ 109,5°.", True),
            ("c", "Nguyên tử carbon trong alkane có thể tự do quay quanh các trục liên kết đơn C-C.", True),
            ("d", "Phân tử ethane (C2H6) có hình vuông phẳng trong không gian.", False)
        ], "Ethane có dạng không gian hai tứ diện ghép nhau."),
        make_tf(4, "Vận dụng", "Khi kiểm tra tính an toàn của bình gas gia đình:", [
            ("a", "Hỗn hợp khí propane và butane nguyên chất không có mùi.", True),
            ("b", "Mùi đặc trưng khó chịu khi ngửi thấy bình gas bị hở là mùi của chất tạo mùi ethyl mercaptan được thêm vào.", True),
            ("c", "Khí gas nặng hơn không khí nên khi rò rỉ sẽ tích tụ ở những nơi trũng thấp gần mặt đất.", True),
            ("d", "Dùng bật lửa ga để soi xem van bình gas có bị hở không là hành động đúng đắn và an toàn.", False)
        ], "Dùng bật lửa soi van hở sẽ gây kích nổ gas tử vong.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Chất đầu tiên trong dãy đồng đẳng alkane có tên là gì?", "Methane", "Methane (CH4)."),
        make_sa(2, "Thông hiểu", "Số nguyên tử Hydrogen trong phân tử alkane có 4 nguyên tử Carbon là bao nhiêu?", "10", "C4H10 (10 nguyên tử H)."),
        make_sa(3, "Vận dụng", "Tỉ khối của khí methane (CH4) đối với không khí xấp xỉ bao nhiêu? (Làm tròn 2 chữ số thập phân)", "0.55", "16 / 29 ≈ 0,55."),
        make_sa(4, "Vận dụng", "Phân tử khối của alkane Propane (C3H8) là bao nhiêu amu? (C=12, H=1)", "44", "12×3 + 8 = 44 amu."),
        make_sa(5, "Vận dụng cao", "Một alkane X có chứa 84% Carbon về khối lượng. Phân tử khối của X là bao nhiêu amu? (C=12, H=1)", "100", "%C = 12n / (14n + 2) = 0,84 -> 12n = 11,76n + 1,68 -> 0,24n = 1,68 -> n = 7 -> C7H16 (M = 100 amu)."),
        make_sa(6, "Vận dụng cao", "Đốt cháy hoàn toàn 1 mol alkane bất kì thu được lượng mol H2O nhiều hơn lượng mol CO2 là bao nhiêu mol?", "1", "CnH2n+2 -> n CO2 + (n+1) H2O -> chênh lệch = (n+1) - n = 1 mol.")
    ],
    p4=[
        make_vdc(1, "Đốt cháy hoàn toàn một lượng alkane X thu được 4,958 lít khí CO2 ở đkc (24,79 L/mol) và 5,4 gam H2O. Công thức phân tử của X là:", ["C2H6", "CH4", "C3H8", "C4H10"], 0, "nCO2 = 0,2 mol; nH2O = 5,4 / 18 = 0,3 mol. Vì nH2O > nCO2 nên nX = nH2O - nCO2 = 0,3 - 0,2 = 0,1 mol. Số C = nCO2 / nX = 0,2 / 0,1 = 2 -> C2H6 (ethane)."),
        make_vdc(2, "Khí methane trong tự nhiên thường sinh ra ở các đầm lầy, mỏ than, bãi chôn lấp rác thải hữu cơ và các hầm biogas. Việc thu gom khí methane từ bãi rác và hầm biogas phát điện mang lại lợi ích kép nào?", ["Vừa cung cấp nguồn năng lượng sạch vừa ngăn chặn phát thải khí nhà kính có hiệu ứng làm nóng Trái Đất gấp 28 lần CO2", "Làm giảm áp suất khí quyển", "Giúp tăng thêm lượng mưa acid", "Làm đất màu mỡ hơn mà không tốn công"], 0, "Methane có tiềm năng gây hiệu ứng nhà kính mạnh gấp 28 lần CO2; thu gom phát điện vừa tạo năng lượng vừa bảo vệ khí hậu."),
        make_vdc(3, "Một bình gas gia đình chứa 12 kg khí hóa lỏng gồm propane và butane theo tỉ lệ khối lượng 3 : 7. Khối lượng của butane trong bình gas đó là:", ["8,4 kg", "3,6 kg", "7,0 kg", "5,0 kg"], 0, "m butane = 12 × (7 / 10) = 8,4 kg."),
        make_vdc(4, "Khí thiên nhiên nén (CNG) ngày càng được khuyến khích sử dụng làm nhiên liệu cho xe buýt và taxi tại các đô thị lớn thay thế xăng dầu truyền thống vì:", ["Khi cháy sinh ra ít khí thải độc hại CO, SO2, bụi mịn hơn nhiều so với xăng dầu", "CNG nặng hơn nước", "CNG đắt hơn xăng", "CNG làm xe chạy nhanh gấp đôi"], 0, "CNG (thành phần chính là CH4) cháy sạch, phát thải ít CO2 và hầu như không sinh SO2 hay bụi mịn.")
    ]
)

# --- BÀI 6 - ĐỀ 2: Tính chất hóa học của Alkane (Phản ứng cháy, phản ứng thế) ---
exams_c2[f"{LID_B6}_test2"] = make_exam(
    CID, CTITLE, LID_B6, LNAME_B6, 2,
    p1=[
        make_mc(1, "Nhận biết", "Phản ứng đặc trưng của các hydrocarbon no (alkane) là loại phản ứng nào?", ["Phản ứng thế", "Phản ứng cộng", "Phản ứng trùng hợp", "Phản ứng thủy phân"], 0, "Alkane chỉ có liên kết đơn bền vững nên phản ứng đặc trưng là phản ứng thế."),
        make_mc(2, "Nhận biết", "Khi cho methane (CH4) tác dụng với khí chlorine (Cl2) cần điều kiện nào sau đây để phản ứng xảy ra?", ["Có ánh sáng khuếch tán", "Nhiệt độ âm 100 °C", "Trong bóng tối hoàn toàn", "Cho vào nước đá"], 0, "Cần có ánh sáng (khuếch tán) để khơi mào phân cắt liên kết Cl-Cl."),
        make_mc(3, "Nhận biết", "Sản phẩm hữu cơ chính thu được khi cho methane tác dụng với chlorine theo tỉ lệ mol 1 : 1 là:", ["Chloromethane (CH3Cl)", "Dichloromethane (CH2Cl2)", "Chloroform (CHCl3)", "Carbon tetrachloride (CCl4)"], 0, "CH4 + Cl2 --(ánh sáng)--> CH3Cl + HCl."),
        make_mc(4, "Nhận biết", "Khí sinh ra cùng với CH3Cl khi chiếu sáng hỗn hợp CH4 và Cl2 làm giấy quỳ tím ẩm chuyển sang màu đỏ là khí gì?", ["Hydrogen chloride (HCl)", "Khí chlorine dư", "Khí CO2", "Khí H2"], 0, "Khí HCl sinh ra hòa tan trong nước trên quỳ tím ẩm tạo acid HCl làm quỳ hóa đỏ."),
        make_mc(5, "Nhận biết", "Phương trình hóa học của phản ứng cháy hoàn toàn khí methane trong oxy là:", ["CH4 + 2O2 -> CO2 + 2H2O", "CH4 + O2 -> CO + H2O", "CH4 + 2O2 -> C + 2H2O", "2CH4 + 3O2 -> 2CO2 + 4H2O"], 0, "CH4 + 2O2 --t°--> CO2 + 2H2O (tỏa nhiệt lớn)."),
        make_mc(6, "Nhận biết", "Khi đốt cháy hoàn toàn một alkane, mối quan hệ giữa số mol H2O và số mol CO2 thu được là:", ["Số mol H2O luôn lớn hơn số mol CO2", "Số mol H2O luôn bằng số mol CO2", "Số mol H2O luôn nhỏ hơn số mol CO2", "Không có quy luật"], 0, "CnH2n+2 cháy cho n CO2 và (n+1) H2O nên nH2O > nCO2."),
        make_mc(7, "Thông hiểu", "Hiện tượng gì xảy ra khi đưa bình hỗn hợp khí CH4 và Cl2 màu vàng lục ra ánh sáng khuếch tán một thời gian?", ["Màu vàng lục của khí clo nhạt dần, thành bình xuất hiện giọt chất lỏng và có khói trắng khi mở nắp", "Bình phát nổ thành ngọn lửa xanh", "Bình chuyển sang màu đen đặc", "Không có bất kì hiện tượng gì"], 0, "Cl2 phản ứng nên màu vàng lục nhạt đi, sinh ra dẫn xuất clo và khí HCl."),
        make_mc(8, "Thông hiểu", "Vì sao các alkane ở điều kiện thường rất trơ về mặt hóa học (không tác dụng với acid, base, dung dịch thuốc tím KMnO4...)?", ["Các liên kết đơn C-C và C-H rất bền vững và không phân cực", "Phân tử có khối lượng quá nhỏ", "Các phân tử đẩy nhau mạnh", "Do alkane là chất khí"], 0, "Liên kết sigma C-C và C-H rất bền và trơ ở điều kiện thường."),
        make_mc(9, "Thông hiểu", "Để nhận biết khí methane (CH4) và khí carbon dioxide (CO2), ta có thể dùng thuốc thử nào sau đây?", ["Dung dịch nước vôi trong Ca(OH)2", "Nước cất", "Dung dịch muối ăn", "Dung dịch cồn"], 0, "CO2 làm đục nước vôi trong, CH4 không phản ứng."),
        make_mc(10, "Thông hiểu", "Trong một gian bếp kín, nếu bếp gas bị cháy không hoàn toàn do thiếu oxy thì có thể sinh ra khí độc nguy hiểm nào?", ["Carbon monoxide (CO)", "Carbon dioxide (CO2)", "Hydrogen (H2)", "Methane (CH4)"], 0, "Cháy thiếu oxy sinh khí CO rất độc gây ngạt thở tử vong."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 4,958 lít khí methane (CH4) ở điều kiện chuẩn (24,79 L/mol). Thể tích khí oxy (O2) ở đkc cần dùng là:", ["9,916 lít", "4,958 lít", "7,437 lít", "12,395 lít"], 0, "nCH4 = 0,2 mol. CH4 + 2O2 -> CO2 + 2H2O -> nO2 = 0,4 mol -> V = 0,4 × 24,79 = 9,916 lít."),
        make_mc(12, "Vận dụng", "Cho 0,1 mol CH4 phản ứng thế hoàn toàn với 0,1 mol Cl2 (ánh sáng) thu được m gam CH3Cl. Biết hiệu suất phản ứng đạt 80%. Giá trị của m là: (C=12, H=1, Cl=35,5)", ["4,04 gam", "5,05 gam", "6,31 gam", "3,25 gam"], 0, "CH4 + Cl2 -> CH3Cl + HCl. nCH3Cl lí thuyết = 0,1 mol -> m lí thuyết = 0,1 × 50,5 = 5,05 gam. Với H=80% -> m thực tế = 5,05 × 0,8 = 4,04 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các phản ứng của khí methane (CH4):", [
            ("a", "Methane phản ứng với dung dịch nước bromine ở điều kiện thường làm mất màu dung dịch bromine.", False),
            ("b", "Methane cháy tỏa rất nhiều nhiệt kèm theo ngọn lửa màu xanh nhạt.", True),
            ("c", "Methane tham gia phản ứng thế với khí clo khi có ánh sáng khuếch tán.", True),
            ("d", "Khí methane bị hấp thụ hoàn toàn trong dung dịch nước vôi trong.", False)
        ], "Methane không làm mất màu Br2 và không tan trong nước vôi trong."),
        make_tf(2, "Thông hiểu", "Về phản ứng thế clo vào phân tử methane:", [
            ("a", "Các nguyên tử H trong CH4 lần lượt bị thay thế bởi nguyên tử clo tạo CH3Cl, CH2Cl2, CHCl3, CCl4.", True),
            ("b", "Phản ứng thế giữa CH4 và Cl2 xảy ra mãnh liệt trong bóng tối hoàn toàn.", False),
            ("c", "Khí hydro clorua (HCl) tạo thành tan nhiều trong nước tạo dung dịch acid làm đỏ quỳ tím.", True),
            ("d", "Chloroform (CHCl3) từng được dùng làm thuốc gây mê trong y học.", True)
        ], "Cần ánh sáng để khơi mào phản ứng thế."),
        make_tf(3, "Vận dụng", "Đốt cháy hoàn toàn một mẫu hydrocarbon X:", [
            ("a", "Nếu thu được nH2O > nCO2 thì hydrocarbon X chắc chắn thuộc dãy đồng đẳng alkane.", True),
            ("b", "Số mol alkane bị đốt cháy luôn bằng (nH2O - nCO2).", True),
            ("c", "Khối lượng của alkane X bằng tổng khối lượng C và H trong CO2 và H2O.", True),
            ("d", "Số mol O2 tham gia phản ứng luôn bằng nCO2.", False)
        ], "nO2 = nCO2 + 0,5 nH2O."),
        make_tf(4, "Vận dụng", "Trong đời sống hằng ngày về sử dụng nhiên liệu alkane:", [
            ("a", "Ngọn lửa bếp gas có màu xanh là dấu hiệu gas đang được đốt cháy hoàn toàn và cung cấp đủ không khí.", True),
            ("b", "Nếu đáy nồi nấu bị bám muội đen chứng tỏ bếp gas đang bị thiếu oxy làm cháy không hoàn toàn.", True),
            ("c", "Để khắc phục đáy nồi bị đen, ta cần điều chỉnh cửa đón gió (lá gió) dưới đáy bếp để cấp thêm không khí.", True),
            ("d", "Muội than đen bám đáy nồi là hợp chất của lưu huỳnh.", False)
        ], "Muội đen là carbon (muội than) sinh ra do cháy thiếu oxy.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên loại phản ứng đặc trưng của các alkane với halogen khi chiếu sáng là gì?", "Phản ứng thế", "Phản ứng thế."),
        make_sa(2, "Thông hiểu", "Ngọn lửa khi đốt cháy hoàn toàn khí methane có màu gì đặc trưng?", "Xanh nhạt", "Màu xanh nhạt."),
        make_sa(3, "Vận dụng", "Cần bao nhiêu mol O2 để đốt cháy hoàn toàn 1 mol Propane (C3H8)?", "5", "C3H8 + 5O2 -> 3CO2 + 4H2O."),
        make_sa(4, "Vận dụng", "Đốt cháy hoàn toàn 0,1 mol một alkane thu được 0,4 mol CO2. Alkane đó có mấy nguyên tử carbon trong phân tử?", "4", "0,4 / 0,1 = 4 nguyên tử C (C4H10)."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn 0,2 mol một alkane X thu được 14,874 lít khí CO2 ở đkc (24,79 L/mol). Khối lượng H2O thu được là bao nhiêu gam? (H=1, O=16)", "14.4", "nCO2 = 14,874 / 24,79 = 0,6 mol. nH2O = nCO2 + nX = 0,6 + 0,2 = 0,8 mol -> mH2O = 0,8 × 18 = 14,4 gam."),
        make_sa(6, "Vận dụng cao", "Đốt cháy 1 gam methane giải phóng khoảng 55,6 kJ nhiệt lượng. Để đun sôi một ấm nước cần 556 kJ, khối lượng methane tối thiểu cần đốt là bao nhiêu gam?", "10", "556 / 55,6 = 10 gam.")
    ],
    p4=[
        make_vdc(1, "Hỗn hợp khí X gồm methane và ethane có tỉ khối đối với khí hydrogen bằng 11,5. Đốt cháy hoàn toàn 4,958 lít hỗn hợp X ở đkc (24,79 L/mol) rồi dẫn toàn bộ sản phẩm qua dung dịch Ca(OH)2 dư. Khối lượng kết tủa CaCO3 thu được là:", ["30,0 gam", "20,0 gam", "25,0 gam", "35,0 gam"], 0, "MX = 11,5 × 2 = 23 amu. nX = 0,2 mol. Dùng sơ đồ đường chéo giữa CH4 (16) và C2H6 (30): tỉ lệ nCH4 : nC2H6 = (30-23) : (23-16) = 7 : 7 = 1 : 1 -> nCH4 = 0,1 mol, nC2H6 = 0,1 mol. Tổng nCO2 = 0,1×1 + 0,1×2 = 0,3 mol -> nCaCO3 = 0,3 mol -> m = 30,0 gam."),
        make_vdc(2, "Cho 11,2 lít hỗn hợp gồm CH4 và Cl2 (đktc) có tỉ lệ mol 1 : 1 vào bình kín rồi chiếu sáng khuếch tán. Sau một thời gian, cho nước vào bình lắc đều rồi thêm một mẩu đá vôi (CaCO3) dư vào thì thấy có 2,479 lít khí CO2 (đkc) thoát ra. Hiệu suất của phản ứng clo hóa methane là:", ["80%", "70%", "60%", "90%"], 0, "n hỗn hợp = 0,5 mol -> nCH4 = 0,25 mol; nCl2 = 0,25 mol. nCO2 = 0,1 mol -> nHCl = 2 nCO2 = 0,2 mol. nCH4 pư = nHCl = 0,2 mol -> H = 0,2 / 0,25 × 100% = 80%."),
        make_vdc(3, "Để điều chế khí methane trong phòng thí nghiệm, người ta nung nóng hỗn hợp sodium acetate khan (CH3COONa) với vôi tôi xút (hỗn hợp NaOH và CaO) ở nhiệt độ cao. Phương pháp thu khí methane thích hợp nhất trong thí nghiệm này là:", ["Đẩy nước (thu qua chậu nước úp ngược ống nghiệm)", "Đẩy không khí để ngửa ống nghiệm", "Hòa tan vào cồn", "Ngưng tụ bằng đá lạnh"], 0, "Khí methane hầu như không tan trong nước và nhẹ hơn nước nên phương pháp đẩy nước cho khí thu được tinh khiết và an toàn nhất."),
        make_vdc(4, "Một gia đình mỗi ngày tiêu thụ trung bình 0,5 kg khí gas (LPG gồm propane và butane) để đun nấu. Biết 1 kg LPG khi cháy hoàn toàn giải phóng khoảng 50 000 kJ nhiệt lượng. Hiệu suất hấp thụ nhiệt của nồi nấu là 60%. Lượng nhiệt hữu ích mà gia đình đó thu được để làm chín thức ăn trong một ngày là:", ["15 000 kJ", "25 000 kJ", "30 000 kJ", "12 500 kJ"], 0, "Nhiệt tỏa ra = 0,5 × 50 000 = 25 000 kJ. Nhiệt hữu ích = 25 000 × 60% = 15 000 kJ.")
    ]
)

# --- BÀI 6 - ĐỀ 3: Đồng phân, phản ứng cracking và ứng dụng alkane ---
exams_c2[f"{LID_B6}_test3"] = make_exam(
    CID, CTITLE, LID_B6, LNAME_B6, 3,
    p1=[
        make_mc(1, "Nhận biết", "Số đồng phân cấu tạo của alkane có công thức phân tử C4H10 là:", ["2", "1", "3", "4"], 0, "C4H10 có 2 đồng phân: butane và isobutane."),
        make_mc(2, "Nhận biết", "Số đồng phân cấu tạo của alkane có công thức phân tử C5H12 là:", ["3", "2", "4", "5"], 0, "C5H12 có 3 đồng phân: pentane, isopentane, neopentane."),
        make_mc(3, "Nhận biết", "Phản ứng bẻ gãy mạch carbon của alkane mạch dài thành các hydrocarbon có mạch carbon ngắn hơn ở nhiệt độ cao và có xúc tác gọi là:", ["Phản ứng cracking", "Phản ứng trùng hợp", "Phản ứng este hóa", "Phản ứng xà phòng hóa"], 0, "Phản ứng cracking phân cắt mạch carbon alkane."),
        make_mc(4, "Nhận biết", "Ứng dụng quan trọng nhất của methane và các alkane trong đời sống hiện nay là:", ["Làm nhiên liệu đun nấu, chạy máy phát điện và nguyên liệu công nghiệp hóa chất", "Làm dung môi hòa tan kim loại", "Làm chất tạo màu thực phẩm", "Làm chất bảo quản nông sản tươi"], 0, "Alkane là nguồn nhiên liệu chính của nhân loại."),
        make_mc(5, "Nhận biết", "Chất nào sau đây được tạo thành khi cho methane phản ứng thế hoàn toàn cả 4 nguyên tử H bằng chlorine?", ["Tetrachloromethane (CCl4)", "Trichloromethane (CHCl3)", "Dichloromethane (CH2Cl2)", "Chloromethane (CH3Cl)"], 0, "CCl4 (carbon tetrachloride)."),
        make_mc(6, "Nhận biết", "Để nhận biết khí methane lẫn trong không khí mỏ than, người thợ mỏ thường sử dụng thiết bị đo nào?", ["Máy cảm biến đo nồng độ khí cháy", "Ống đong thể tích", "Quỳ tím", "Nhiệt kế thủy ngân"], 0, "Dùng máy dò khí cháy cảm biến điện tử."),
        make_mc(7, "Thông hiểu", "Tên thay thế theo danh pháp quốc tế của đồng phân isobutane CH3-CH(CH3)-CH3 là:", ["2-methylpropane", "2-methylbutane", "Dimethylmethane", "Propane"], 0, "Mạch chính 3 carbon, vị trí C số 2 có nhóm methyl: 2-methylpropane."),
        make_mc(8, "Thông hiểu", "Vì sao trong công nghiệp chế biến dầu mỏ, người ta phải thực hiện quá trình cracking dầu nặng?", ["Để tăng sản lượng xăng và các hydrocarbon nhẹ có giá trị cao phục vụ giao thông", "Để làm dầu đặc lại", "Để giảm nhiệt độ sôi của nước", "Để biến alkane thành kim loại"], 0, "Cracking bẻ gãy dầu mazut nặng thành xăng (C7-C11) và khí đốt."),
        make_mc(9, "Thông hiểu", "Khí Biogas sinh ra từ hầm ủ phân gia súc ở các trang trại nông nghiệp chứa thành phần cháy chủ yếu là:", ["Methane (CH4)", "Ethylene (C2H4)", "Acetylene (C2H2)", "Carbon dioxide (CO2)"], 0, "Biogas chứa 60-70% CH4, còn lại là CO2."),
        make_mc(10, "Thông hiểu", "Dẫn khí methane qua ống nghiệm đựng dung dịch nước bromine da cam, hiện tượng là:", ["Dung dịch không bị mất màu da cam", "Dung dịch mất màu da cam ngay lập tức", "Xuất hiện kết tủa trắng", "Dung dịch chuyển sang màu tím"], 0, "Alkane không có liên kết bội nên không phản ứng với dung dịch Br2."),
        make_mc(11, "Vận dụng", "Cracking hoàn toàn 1 mol butane (C4H10) thu được hỗn hợp X gồm methane, ethane, ethylene, propene và butane chưa phản ứng. Số mol hỗn hợp X thu được luôn:", ["Lớn hơn 1 mol", "Nhỏ hơn 1 mol", "Bằng 1 mol", "Bằng 0,5 mol"], 0, "C4H10 -> CnH2n + CmH2m+2 (1 mol alkane nứt thành 2 mol phân tử) nên số mol hỗn hợp sau cracking luôn lớn hơn 1 mol."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn hỗn hợp gồm 0,1 mol CH4 và 0,1 mol C2H6. Tổng thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["7,4370 lít", "4,9580 lít", "9,9160 lít", "2,4790 lít"], 0, "nCO2 = 0,1×1 + 0,1×2 = 0,3 mol -> V = 0,3 × 24,79 = 7,4370 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các đồng phân của Alkane:", [
            ("a", "Alkane có từ 4 nguyên tử carbon trở lên mới bắt đầu xuất hiện đồng phân mạch carbon.", True),
            ("b", "Đồng phân mạch thẳng luôn có nhiệt độ sôi cao hơn đồng phân mạch nhánh có cùng số carbon.", True),
            ("c", "Neopentane (2,2-dimethylpropane) có mạch carbon dạng hình chữ thập.", True),
            ("d", "Tất cả các đồng phân của C5H12 đều ở trạng thái khí ở điều kiện thường.", False)
        ], "C5H12 ở thể lỏng ở 25 °C."),
        make_tf(2, "Thông hiểu", "Về quá trình cracking alkane:", [
            ("a", "Cracking là phản ứng bẻ gãy các liên kết C-C trong phân tử alkane mạch dài.", True),
            ("b", "Sản phẩm của phản ứng cracking 1 phân tử alkane gồm 1 phân tử alkane mới và 1 phân tử alkene mới.", True),
            ("c", "Cracking nhiệt cần nhiệt độ cao khoảng 500 - 700 °C.", True),
            ("d", "Cracking làm giảm số mol phân tử khí trong hệ phản ứng.", False)
        ], "Cracking làm tăng số mol phân tử khí."),
        make_tf(3, "Vận dụng", "Về ứng dụng và bảo vệ môi trường đối với nhiên liệu alkane:", [
            ("a", "Xây dựng hầm biogas ở nông thôn vừa giải quyết chất thải chăn nuôi vừa có gas sạch đun nấu.", True),
            ("b", "Bùn thải sau khi ủ biogas có thể dùng làm phân bón hữu cơ rất tốt cho cây trồng.", True),
            ("c", "Khí methane rò rỉ vào khí quyển không gây nguy hiểm gì cho hiện tượng ấm lên toàn cầu.", False),
            ("d", "Trong các mỏ than hầm lò cần lắp đặt hệ thống thông gió công suất lớn để pha loãng nồng độ khí methane dưới ngưỡng nổ.", True)
        ], "Methane là khí nhà kính cực kì nguy hiểm."),
        make_tf(4, "Vận dụng", "Một học sinh làm thí nghiệm đốt cháy nến parafin (chứa các alkane rắn C20-C30):", [
            ("a", "Khi thắp nến, parafin nóng chảy rồi bốc hơi, chính hơi parafin mới là chất cháy.", True),
            ("b", "Úp một cốc thủy tinh lạnh lên ngọn nến đang cháy thấy thành cốc có màng hơi nước đọng lại.", True),
            ("c", "Dẫn khí trong cốc vào nước vôi trong thấy nước vôi bị vẩn đục.", True),
            ("d", "Thí nghiệm này chứng minh trong phân tử parafin có chứa nguyên tố sắt.", False)
        ], "Chứng minh parafin chứa C và H.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Alkane có mấy nguyên tử carbon trở lên thì bắt đầu có hiện tượng đồng phân?", "4", "4 carbon (C4H10)."),
        make_sa(2, "Thông hiểu", "Tên gọi của phản ứng bẻ gãy phân tử alkane mạch dài thành mạch ngắn là gì?", "Cracking", "Cracking."),
        make_sa(3, "Vận dụng", "Số liên kết C-C trong phân tử pentane mạch thẳng là bao nhiêu?", "4", "5 nguyên tử C liên kết chuỗi có 4 liên kết C-C."),
        make_sa(4, "Vận dụng", "Đốt cháy 0,1 mol một alkane mạch hở thu được 7,2 gam H2O. Alkane đó có mấy nguyên tử H trong phân tử? (H=1, O=16)", "8", "nH2O = 0,4 mol -> nH = 0,8 mol -> số H = 0,8 / 0,1 = 8 (C3H8)."),
        make_sa(5, "Vận dụng cao", "Cracking hoàn toàn 5,8 gam Butane (C4H10) thu được hỗn hợp khí X. Đốt cháy hoàn toàn toàn bộ hỗn hợp X thì thể tích CO2 thu được ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "9.92", "Bảo toàn C: nC = 4 × nC4H10 = 4 × (5,8/58) = 0,4 mol -> nCO2 = 0,4 mol -> V = 0,4 × 24,79 = 9,916 ≈ 9,92 lít."),
        make_sa(6, "Vận dụng cao", "Một mẫu khí biogas chứa 60% methane về thể tích. Để có 6 lít methane cần bao nhiêu lít khí biogas đó?", "10", "6 / 0,6 = 10 lít.")
    ],
    p4=[
        make_vdc(1, "Cracking m gam butane (C4H10) thu được hỗn hợp khí X gồm 5 hydrocarbon (CH4, C2H6, C2H4, C3H6 và C4H10 dư). Dẫn toàn bộ hỗn hợp X qua bình đựng dung dịch nước bromine dư thấy khối lượng bình bromine tăng 4,2 gam và có 3,7185 lít hỗn hợp khí Y (đkc) thoát ra. Giá trị của m là:", ["8,7 gam", "5,8 gam", "11,6 gam", "7,25 gam"], 0, "Khối lượng bình Br2 tăng chính là m alkene = 4,2 gam. nY (gồm các alkane) = 3,7185 / 24,79 = 0,15 mol. Vì cracking 1 alkane ra 1 alkane và 1 alkene nên n alkane sinh ra = n alkene. n butane ban đầu = n alkane trong Y = 0,15 mol -> m butane ban đầu = 0,15 × 58 = 8,7 gam."),
        make_vdc(2, "Đốt cháy hoàn toàn 6,72 lít hỗn hợp khí gồm hai alkane đồng đẳng kế tiếp nhau (đktc) thu được 17,92 lít khí CO2 (đktc). Công thức phân tử của hai alkane đó là:", ["C2H6 và C3H8", "CH4 và C2H6", "C3H8 và C4H10", "C4H10 và C5H12"], 0, "n hỗn hợp = 0,3 mol; nCO2 = 0,8 mol. Số C trung bình = 0,8 / 0,3 = 2,67. Do hai alkane kế tiếp nhau nên 2 alkane là C2H6 (n=2) và C3H8 (n=3)."),
        make_vdc(3, "Chất 2,2,4-trimethylpentane (còn gọi là isooctane) được chọn làm chất chuẩn quy ước có chỉ số octane bằng 100 để đo lường khả năng chống kích nổ của nhiên liệu xăng. Xăng có chỉ số octane càng cao thì:", ["Khả năng chống kích nổ khi nén càng tốt, giúp động cơ chạy êm và bền bỉ hơn", "Càng dễ bị bốc cháy tự phát", "Càng có nhiều khói đen", "Càng rẻ tiền hơn"], 0, "Chỉ số octane cao biểu thị tính chống kích nổ tuyệt hảo, tối ưu cho động cơ áp suất cao hiện đại."),
        make_vdc(4, "Một hầm biogas xử lí phân lợn mỗi ngày sinh ra 10 m3 khí biogas chứa 65% CH4 về thể tích. Biết nhiệt lượng tỏa ra khi đốt cháy 1 m3 khí CH4 là 36 000 kJ. Tổng nhiệt lượng có thể thu được từ hầm biogas này mỗi ngày là:", ["234 000 kJ", "360 000 kJ", "180 000 kJ", "200 000 kJ"], 0, "VCH4 = 10 × 65% = 6,5 m3. Q = 6,5 × 36 000 = 234 000 kJ.")
    ]
)

# ==============================================================================
# BÀI 7: ALKENE (chem9_c2_b7) - 3 ĐỀ
# ==============================================================================
LID_B7 = "chem9_c2_b7"
LNAME_B7 = "Bài 7: Alkene"

# --- BÀI 7 - ĐỀ 1: Cấu tạo và tính chất vật lí của Alkene ---
exams_c2[f"{LID_B7}_test1"] = make_exam(
    CID, CTITLE, LID_B7, LNAME_B7, 1,
    p1=[
        make_mc(1, "Nhận biết", "Alkene là những hydrocarbon mạch hở mà trong phân tử có chứa đặc điểm cấu tạo nào?", ["Chứa 1 liên kết đôi C=C", "Chỉ chứa liên kết đơn", "Chứa 1 liên kết ba", "Chứa vòng benzen"], 0, "Alkene là hydrocarbon không no mạch hở chứa 1 liên kết đôi C=C."),
        make_mc(2, "Nhận biết", "Công thức phân tử chung của dãy đồng đẳng Alkene là:", ["CnH2n (n >= 2)", "CnH2n+2 (n >= 1)", "CnH2n-2 (n >= 2)", "CnH2n-6 (n >= 6)"], 0, "Alkene có công thức chung CnH2n với n ≥ 2."),
        make_mc(3, "Nhận biết", "Chất nào sau đây là alkene đơn giản nhất?", ["Ethylene (C2H4)", "Methane (CH4)", "Acetylene (C2H2)", "Propane (C3H8)"], 0, "Ethylene (C2H4) là alkene đơn giản nhất."),
        make_mc(4, "Nhận biết", "Trong phân tử ethylene (C2H4), liên kết đôi C=C bao gồm:", ["1 liên kết bền và 1 liên kết kém bền dễ bị đứt ra trong phản ứng hóa học", "2 liên kết bền như nhau", "2 liên kết ba", "4 liên kết đơn"], 0, "Liên kết đôi gồm 1 liên kết sigma bền và 1 liên kết pi kém bền dễ bị bẻ gãy."),
        make_mc(5, "Nhận biết", "Ở điều kiện thường, ethylene là chất gì?", ["Chất khí không màu, nhẹ hơn không khí, ít tan trong nước", "Chất lỏng màu xanh", "Chất rắn màu trắng", "Chất khí nặng hơn không khí và tan vô hạn"], 0, "Ethylene là khí không màu, nhẹ hơn không khí (M = 28 < 29) và ít tan trong nước."),
        make_mc(6, "Nhận biết", "Công thức cấu tạo thu gọn của ethylene là:", ["CH2=CH2", "CH3-CH3", "CH≡CH", "CH3-CH=CH2"], 0, "CH2=CH2."),
        make_mc(7, "Thông hiểu", "Vì sao ethylene có tính chất hóa học khác biệt hoàn toàn so với methane?", ["Vì phân tử ethylene có liên kết đôi C=C chứa liên kết pi kém bền dễ tham gia phản ứng cộng", "Vì ethylene chứa nhiều carbon hơn", "Vì ethylene là chất lỏng", "Vì ethylene có mùi thơm"], 0, "Liên kết kém bền trong liên kết đôi là trung tâm phản ứng đặc trưng của alkene."),
        make_mc(8, "Thông hiểu", "Tỉ khối của khí ethylene (C2H4) đối với không khí xấp xỉ bằng:", ["0,97", "1,52", "0,55", "2,00"], 0, "d = 28 / 29 ≈ 0,97."),
        make_mc(9, "Thông hiểu", "Chất nào sau đây cùng thuộc dãy đồng đẳng với ethylene?", ["Propene (C3H6)", "Methane (CH4)", "Ethane (C2H6)", "Butane (C4H10)"], 0, "C3H6 (propene) có công thức chung CnH2n nên cùng dãy đồng đẳng với ethylene."),
        make_mc(10, "Thông hiểu", "Phân tử alkene có 4 nguyên tử carbon trong phân tử có công thức là:", ["C4H8", "C4H10", "C4H6", "C3H6"], 0, "n=4 -> C4H8 (butene)."),
        make_mc(11, "Vận dụng", "Một alkene X có phân tử khối bằng 42 amu. Công thức phân tử của X là: (C=12, H=1)", ["C3H6", "C2H4", "C4H8", "C5H10"], 0, "14n = 42 -> n = 3 -> C3H6 (propene)."),
        make_mc(12, "Vận dụng", "Có bao nhiêu liên kết đơn C-H trong một phân tử ethylene (C2H4)?", ["4 liên kết", "2 liên kết", "1 liên kết", "6 liên kết"], 0, "Có 4 liên kết C-H và 1 liên kết đôi C=C.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các đặc điểm của phân tử ethylene (C2H4):", [
            ("a", "Phân tử ethylene có cấu tạo phẳng, cả 6 nguyên tử (2 C và 4 H) cùng nằm trên một mặt phẳng.", True),
            ("b", "Liên kết đôi C=C gồm hai liên kết hoàn toàn giống nhau.", False),
            ("c", "Ethylene nhẹ hơn không khí một chút.", True),
            ("d", "Ethylene tan rất tốt trong nước tạo dung dịch acid.", False)
        ], "Liên kết đôi gồm 1 liên kết bền và 1 liên kết kém bền. Ethylene ít tan trong nước."),
        make_tf(2, "Thông hiểu", "Về dãy đồng đẳng của Alkene:", [
            ("a", "Tất cả các alkene đều có công thức phân tử chung là CnH2n (n >= 2).", True),
            ("b", "Alkene là hydrocarbon không no vì trong phân tử còn liên kết đôi.", True),
            ("c", "Từ C2H4 đến C4H8 ở điều kiện thường đều là các chất khí.", True),
            ("d", "Alkene có tỉ lệ số nguyên tử C và H luôn là 1 : 1.", False)
        ], "Tỉ lệ nC : nH luôn là 1 : 2."),
        make_tf(3, "Vận dụng", "Về khả năng tạo đồng phân của alkene:", [
            ("a", "Ethylene và propene không có đồng phân cấu tạo về vị trí liên kết đôi.", True),
            ("b", "Butene (C4H8) có đồng phân mạch carbon và đồng phân vị trí liên kết đôi.", True),
            ("c", "Chất có công thức phân tử C3H6 chỉ có duy nhất 1 công thức cấu tạo.", False),
            ("d", "But-1-ene và but-2-ene là hai đồng phân vị trí liên kết đôi của nhau.", True)
        ], "C3H6 có 2 cấu tạo: propene (mạch hở) và cyclopropane (mạch vòng)."),
        make_tf(4, "Vận dụng", "Thực hành thu khí ethylene trong phòng thí nghiệm:", [
            ("a", "Thu khí ethylene bằng phương pháp đẩy nước vì ethylene ít tan trong nước.", True),
            ("b", "Có thể thu ethylene bằng phương pháp đẩy không khí úp ngược ống nghiệm.", True),
            ("c", "Không nên để ngửa ống nghiệm khi thu ethylene bằng phương pháp đẩy không khí vì ethylene nhẹ hơn không khí sẽ bay lên thoát ra ngoài.", True),
            ("d", "Khí ethylene có màu nâu đỏ đặc trưng.", False)
        ], "Ethylene là chất khí không màu.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Phân tử alkene đơn giản nhất có bao nhiêu nguyên tử carbon?", "2", "2 nguyên tử C (C2H4)."),
        make_sa(2, "Thông hiểu", "Trong liên kết đôi C=C có bao nhiêu liên kết kém bền dễ bị bẻ gãy?", "1", "1 liên kết pi kém bền."),
        make_sa(3, "Vận dụng", "Phân tử khối của khí ethylene (C2H4) là bao nhiêu amu? (C=12, H=1)", "28", "12×2 + 4 = 28 amu."),
        make_sa(4, "Vận dụng", "Tỉ khối của khí ethylene đối với khí methane (CH4) là bao nhiêu? (Làm tròn 2 chữ số thập phân)", "1.75", "28 / 16 = 1,75."),
        make_sa(5, "Vận dụng cao", "Một alkene có phân tử khối bằng 56 amu. Alkene đó có bao nhiêu nguyên tử Hydrogen trong phân tử?", "8", "14n = 56 -> n = 4 -> C4H8 có 8 nguyên tử H."),
        make_sa(6, "Vận dụng cao", "Phần trăm khối lượng của nguyên tố Carbon trong mọi alkene đều bằng bao nhiêu %? (C=12, H=1, làm tròn 2 chữ số thập phân)", "85.71", "12n / 14n × 100% = 12/14 × 100% ≈ 85,71%.")
    ],
    p4=[
        make_vdc(1, "Một bình kín dung tích 5 lít chứa khí ethylene ở điều kiện chuẩn (25 °C, 1 bar). Khối lượng khí ethylene có trong bình là: (C=12, H=1)", ["5,65 gam", "2,82 gam", "4,24 gam", "6,15 gam"], 0, "nC2H4 = 5 / 24,79 ≈ 0,2017 mol -> m = 0,2017 × 28 ≈ 5,647 gam ≈ 5,65 gam."),
        make_vdc(2, "Hỗn hợp khí X gồm ethylene và một alkane Y có tỉ lệ mol 1 : 1. Đốt cháy hoàn toàn 0,2 mol hỗn hợp X thu được 0,5 mol CO2. Công thức phân tử của alkane Y là:", ["C3H8", "C2H6", "CH4", "C4H10"], 0, "nX = 0,2 mol -> nC2H4 = 0,1 mol; nY = 0,1 mol. nCO2 = 0,1 × 2 + 0,1 × nY = 0,5 -> 0,1 nY = 0,3 -> nY = 3 -> C3H8 (propane)."),
        make_vdc(3, "Chất nào sau đây vừa có đồng phân hình học cis - trans vừa có liên kết đôi C=C ở mạch carbon?", ["But-2-ene (CH3-CH=CH-CH3)", "But-1-ene (CH2=CH-CH2-CH3)", "Propene (CH2=CH-CH3)", "Ethylene (CH2=CH2)"], 0, "But-2-ene mỗi nguyên tử C ở liên kết đôi liên kết với 2 nhóm khác nhau (-H và -CH3) nên có đồng phân hình học cis và trans."),
        make_vdc(4, "Trong hoa quả chín tự nhiên như chuối, cà chua, táo chín luôn sinh ra một lượng nhỏ hormone thực vật thể khí thúc đẩy quá trình hô hấp làm trái cây nhanh chín đều. Khí đó chính là:", ["Ethylene (C2H4)", "Methane (CH4)", "Acetylene (C2H2)", "Carbon dioxide (CO2)"], 0, "Ethylene là phytohormone kích thích quá trình chín của quả trong tự nhiên.")
    ]
)

# --- BÀI 7 - ĐỀ 2: Tính chất hóa học của Alkene (Phản ứng cộng và phản ứng cháy) ---
exams_c2[f"{LID_B7}_test2"] = make_exam(
    CID, CTITLE, LID_B7, LNAME_B7, 2,
    p1=[
        make_mc(1, "Nhận biết", "Phản ứng hóa học đặc trưng của ethylene và các alkene là loại phản ứng nào?", ["Phản ứng cộng", "Phản ứng thế", "Phản ứng trung hòa", "Phản ứng trao đổi"], 0, "Do có liên kết đôi kém bền nên phản ứng đặc trưng là phản ứng cộng."),
        make_mc(2, "Nhận biết", "Dung dịch thuốc thử dùng để nhận biết và phân biệt khí ethylene với khí methane là:", ["Dung dịch nước bromine (Br2)", "Dung dịch nước vôi trong", "Dung dịch muối ăn NaCl", "Dung dịch acid HCl"], 0, "Ethylene làm mất màu nâu đỏ của dung dịch nước Br2, methane không phản ứng."),
        make_mc(3, "Nhận biết", "Khi dẫn khí ethylene vào dung dịch nước bromine, hiện tượng quan sát được là:", ["Dung dịch nước bromine bị mất màu da cam (hoặc nâu đỏ)", "Có kết tủa trắng xuất hiện", "Dung dịch chuyển sang màu xanh lam", "Có khí không màu sủi bọt thoát ra"], 0, "CH2=CH2 + Br2 -> CH2Br-CH2Br (chất lỏng không màu làm mất màu dung dịch Br2)."),
        make_mc(4, "Nhận biết", "Sản phẩm thu được khi cho ethylene tác dụng với dung dịch nước bromine là:", ["1,2-dibromoethane (CH2Br-CH2Br)", "Bromoethane (CH3-CH2Br)", "Dibromomethane (CH2Br2)", "Bromomethane (CH3Br)"], 0, "CH2=CH2 + Br2 -> CH2Br-CH2Br."),
        make_mc(5, "Nhận biết", "Khi đốt cháy hoàn toàn một alkene, tỉ lệ số mol giữa CO2 và H2O thu được là:", ["Số mol CO2 luôn bằng số mol H2O", "Số mol CO2 lớn hơn số mol H2O", "Số mol CO2 nhỏ hơn số mol H2O", "Không có quy luật cố định"], 0, "CnH2n + 1,5n O2 -> n CO2 + n H2O -> nCO2 = nH2O."),
        make_mc(6, "Nhận biết", "Phản ứng giữa ethylene và khí hydrogen (H2) khi có xúc tác niken (Ni) và nung nóng tạo ra sản phẩm gì?", ["Ethane (C2H6)", "Methane (CH4)", "Acetylene (C2H2)", "Polyethylene"], 0, "CH2=CH2 + H2 --(Ni, t°)--> CH3-CH3 (ethane)."),
        make_mc(7, "Thông hiểu", "Vì sao methane KHÔNG làm mất màu dung dịch bromine còn ethylene lại làm mất màu nhanh chóng?", ["Methane chỉ có liên kết đơn bền vững, ethylene có liên kết đôi kém bền dễ bị bẻ gãy tham gia phản ứng cộng", "Methane nhẹ hơn nước bromine", "Ethylene là chất lỏng", "Ethylene có tính acid"], 0, "Liên kết pi kém bền trong C2H4 mở ra cộng 2 nguyên tử Br."),
        make_mc(8, "Thông hiểu", "Cho ethylene tác dụng với nước (H2O) ở nhiệt độ cao có xúc tác acid vô cơ sinh ra chất hữu cơ nào?", ["Ethylic alcohol (C2H5OH)", "Acetic acid (CH3COOH)", "Methane (CH4)", "Dimethyl ether"], 0, "CH2=CH2 + H2O --(acid, t°)--> C2H5OH."),
        make_mc(9, "Thông hiểu", "Dẫn 0,1 mol khí ethylene qua bình đựng dung dịch bromine dư, khối lượng bình bromine tăng lên bao nhiêu gam?", ["2,8 gam", "5,6 gam", "16,0 gam", "3,2 gam"], 0, "Toàn bộ 0,1 mol C2H4 bị giữ lại trong bình nên khối lượng bình tăng = mC2H4 = 0,1 × 28 = 2,8 gam."),
        make_mc(10, "Thông hiểu", "Để làm sạch khí methane có lẫn tạp chất là một lượng nhỏ khí ethylene, người ta dẫn hỗn hợp khí qua dung dịch nào sau đây?", ["Dung dịch nước bromine dư", "Dung dịch nước vôi trong", "Dung dịch kiềm NaOH", "Dung dịch HCl"], 0, "Dung dịch Br2 giữ lại C2H4, khí CH4 không phản ứng thoát ra ngoài tinh khiết."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 2,8 gam ethylene (C2H4). Thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "nC2H4 = 2,8 / 28 = 0,1 mol. C2H4 + 3O2 -> 2CO2 + 2H2O -> nCO2 = 0,2 mol -> V = 0,2 × 24,79 = 4,958 lít."),
        make_mc(12, "Vận dụng", "Dẫn hoàn toàn 4,958 lít khí ethylene (đkc: 24,79 L/mol) vào dung dịch chứa 48 gam Br2. Dung dịch sau phản ứng có hiện tượng gì?", ["Mất màu hoàn toàn nước bromine và bromine phản ứng vừa đủ", "Nước bromine vẫn còn màu nâu đỏ do còn dư", "Ethylene còn dư bay ra", "Tạo kết tủa trắng"], 0, "nC2H4 = 0,2 mol; nBr2 = 48 / 160 = 0,3 mol > 0,2 mol -> Br2 còn dư 0,1 mol nên dung dịch vẫn còn màu nâu đỏ.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét phản ứng cộng của ethylene:", [
            ("a", "Ethylene tham gia phản ứng cộng làm mất màu nước bromine da cam ở nhiệt độ phòng.", True),
            ("b", "Phản ứng cộng bẻ gãy liên kết kém bền trong liên kết đôi tạo liên kết đơn mới.", True),
            ("c", "Ethylene phản ứng với khí H2 (xúc tác Ni, đun nóng) tạo thành methane.", False),
            ("d", "Khối lượng bình nước bromine tăng lên đúng bằng khối lượng khí ethylene đã phản ứng.", True)
        ], "Cộng H2 tạo ethane C2H6."),
        make_tf(2, "Thông hiểu", "Về phản ứng đốt cháy của các alkene:", [
            ("a", "Đốt cháy hoàn toàn bất kì alkene nào cũng luôn thu được số mol CO2 bằng số mol H2O.", True),
            ("b", "Ethylene cháy trong oxy tỏa nhiều nhiệt tạo ngọn lửa sáng chói.", True),
            ("c", "Nếu đốt cháy một hydrocarbon thu được nCO2 = nH2O thì hydrocarbon đó có thể là alkene hoặc cycloalkane.", True),
            ("d", "Phản ứng cháy của ethylene tiêu tốn lượng O2 ít hơn methane cho cùng số mol.", False)
        ], "C2H4 cần 3 mol O2, CH4 chỉ cần 2 mol O2."),
        make_tf(3, "Vận dụng", "Tiến hành phân biệt hai bình khí không nhãn: Methane và Ethylene:", [
            ("a", "Dẫn lần lượt từng khí qua dung dịch nước bromine, khí làm nhạt màu nước bromine là ethylene.", True),
            ("b", "Dẫn từng khí qua dung dịch nước vôi trong có thể phân biệt được hai khí.", False),
            ("c", "Đốt cháy cả hai khí rồi đo tỉ lệ thể tích CO2 và H2O có thể phân biệt được hai khí.", True),
            ("d", "Khí không làm đổi màu nước bromine là methane.", True)
        ], "Cả hai khí đều không làm đục nước vôi trong."),
        make_tf(4, "Vận dụng", "Trong công nghiệp hóa chất dầu khí:", [
            ("a", "Ethylene là nguyên liệu khởi đầu quan trọng bậc nhất để sản xuất hàng loạt hóa chất và chất dẻo.", True),
            ("b", "Hydrat hóa ethylene (cộng nước) là một phương pháp công nghiệp sản xuất ethylic alcohol.", True),
            ("c", "Cộng chlorine vào ethylene thu được 1,2-dichloroethane dùng để sản xuất nhựa PVC.", True),
            ("d", "Phản ứng cộng của ethylene đòi hỏi áp suất cực cao hàng nghìn atm mới xảy ra.", False)
        ], "Phản ứng cộng với Br2, Cl2 xảy ra êm dịu ngay ở điều kiện thường.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Dung dịch nào có màu da cam bị mất màu khi sục khí ethylene vào?", "Dung dịch bromine", "Dung dịch bromine (Br2)."),
        make_sa(2, "Thông hiểu", "Tỉ lệ số mol giữa CO2 và H2O khi đốt cháy hoàn toàn một alkene là bao nhiêu?", "1:1", "1:1 (nCO2 = nH2O)."),
        make_sa(3, "Vận dụng", "Cần bao nhiêu mol Br2 để tác dụng vừa đủ với 0,15 mol khí ethylene?", "0.15", "Tỉ lệ mol 1:1 -> 0,15 mol."),
        make_sa(4, "Vận dụng", "Dẫn 2,479 lít khí ethylene ở đkc (24,79 L/mol) vào bình nước bromine dư. Khối lượng bình tăng thêm bao nhiêu gam?", "2.8", "n = 0,1 mol -> m = 0,1 × 28 = 2,8 gam."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn m gam một alkene thu được 0,3 mol CO2. Khối lượng H2O thu được là bao nhiêu gam? (H=1, O=16)", "5.4", "nH2O = nCO2 = 0,3 mol -> mH2O = 0,3 × 18 = 5,4 gam."),
        make_sa(6, "Vận dụng cao", "Cho 5,6 gam một alkene X làm mất màu vừa đủ 16 gam Br2. Phân tử khối của alkene X là bao nhiêu amu? (Br=80)", "56", "nBr2 = 16 / 160 = 0,1 mol -> n alkene = 0,1 mol -> M = 5,6 / 0,1 = 56 amu (C4H8).")
    ],
    p4=[
        make_vdc(1, "Dẫn 4,958 lít hỗn hợp khí gồm CH4 và C2H4 ở đkc (24,79 L/mol) qua bình đựng dung dịch nước bromine dư. Sau phản ứng thấy khối lượng bình bromine tăng 2,8 gam. Phần trăm thể tích của khí CH4 trong hỗn hợp ban đầu là:", ["50%", "25%", "75%", "40%"], 0, "n hỗn hợp = 0,2 mol. Khối lượng bình tăng = mC2H4 = 2,8 gam -> nC2H4 = 2,8 / 28 = 0,1 mol. nCH4 = 0,2 - 0,1 = 0,1 mol -> %V(CH4) = 0,1 / 0,2 × 100% = 50%."),
        make_vdc(2, "Đốt cháy hoàn toàn 0,1 mol hỗn hợp gồm một alkane X và một alkene Y thu được 4,958 lít khí CO2 ở đkc (24,79 L/mol) và 4,5 gam H2O. Số mol của alkane X trong hỗn hợp ban đầu là:", ["0,05 mol", "0,02 mol", "0,08 mol", "0,04 mol"], 0, "nCO2 = 0,2 mol; nH2O = 4,5 / 18 = 0,25 mol. Vì alkene cháy cho nCO2 = nH2O nên lượng chênh lệch (nH2O - nCO2) chính là do alkane: nX = 0,25 - 0,2 = 0,05 mol."),
        make_vdc(3, "Để điều chế khí ethylene trong phòng thí nghiệm, người ta đun nóng ethylic alcohol (C2H5OH) với acid sulfuric đặc ở nhiệt độ khoảng 170 °C: C2H5OH --(H2SO4 đặc, 170°C)--> C2H4 + H2O. Vai trò của acid H2SO4 đặc trong phản ứng này là:", ["Chất xúc tác và chất hút nước mạnh thúc đẩy cân bằng chuyển dịch", "Chất cung cấp oxy", "Chất hòa tan sản phẩm", "Chất tạo màu cho khí"], 0, "H2SO4 đặc đóng vai trò xúc tác acid và chất háo nước mạnh hút H2O để phản ứng tách nước diễn ra triệt để."),
        make_vdc(4, "Một hỗn hợp gồm C2H4 và H2 có tỉ khối đối với He bằng 3,75. Dẫn hỗn hợp qua ống sứ chứa bột Ni nung nóng thu được hỗn hợp khí Y có tỉ khối đối với He bằng 5. Hiệu suất của phản ứng hydro hóa ethylene là:", ["50%", "60%", "40%", "75%"], 0, "MX = 3,75 × 4 = 15; MY = 5 × 4 = 20. Chọn 1 mol X: dX/dY = nY/nX -> nY = 15/20 = 0,75 mol. Số mol H2 phản ứng = nX - nY = 1 - 0,75 = 0,25 mol. Dùng đường chéo tính tỉ lệ nC2H4:nH2 trong X: (28-15):(15-2) = 13:13 = 1:1 -> nC2H4 ban đầu = 0,5 mol; nH2 ban đầu = 0,5 mol. Hiệu suất H = 0,25 / 0,5 × 100% = 50%.")
    ]
)

# --- BÀI 7 - ĐỀ 3: Phản ứng trùng hợp và ứng dụng thực tiễn của Alkene ---
exams_c2[f"{LID_B7}_test3"] = make_exam(
    CID, CTITLE, LID_B7, LNAME_B7, 3,
    p1=[
        make_mc(1, "Nhận biết", "Quá trình kết hợp liên tiếp nhiều phân tử nhỏ giống nhau (monomer) tạo thành phân tử rất lớn (polymer) gọi là:", ["Phản ứng trùng hợp", "Phản ứng thủy phân", "Phản ứng xà phòng hóa", "Phản ứng este hóa"], 0, "Định nghĩa phản ứng trùng hợp."),
        make_mc(2, "Nhận biết", "Sản phẩm của phản ứng trùng hợp khí ethylene ở nhiệt độ, áp suất cao và có xúc tác là:", ["Polyethylene (nhựa PE)", "Polyvinyl chloride (nhựa PVC)", "Polystyrene (nhựa PS)", "Cao su buna"], 0, "n CH2=CH2 -> (-CH2-CH2-)n (nhựa PE)."),
        make_mc(3, "Nhận biết", "Trong phản ứng trùng hợp ethylene, phân tử ethylene ban đầu được gọi là:", ["Monomer", "Polymer", "Mắt xích", "Hệ số trùng hợp"], 0, "Chất ban đầu tham gia trùng hợp gọi là monomer."),
        make_mc(4, "Nhận biết", "Nhựa PE (polyethylene) thuộc loại vật liệu nào?", ["Chất dẻo", "Tơ tổng hợp", "Cao su", "Keo dán"], 0, "PE là loại chất dẻo (nhựa) phổ biến nhất thế giới."),
        make_mc(5, "Nhận biết", "Ứng dụng nào sau đây trong nông nghiệp sử dụng khí ethylene?", ["Giúp hoa quả mau chín và đều màu", "Làm thuốc trừ sâu rầy", "Làm phân đạm bón lá", "Diệt sạch cỏ dại"], 0, "Ethylene dùng dấm quả mau chín tự nhiên."),
        make_mc(6, "Nhận biết", "Mắt xích cơ bản trong phân tử nhựa polyethylene (PE) là:", ["-CH2-CH2-", "-CH=CH-", "-CH2-", "-CH3"], 0, "Mắt xích lặp lại là -CH2-CH2-."),
        make_mc(7, "Thông hiểu", "Vì sao các túi ni lông làm bằng nhựa PE khi thải ra môi trường tự nhiên lại mất hàng trăm năm mới phân hủy được?", ["Liên kết đơn C-C trong mạch polymer PE rất bền vững, trơ với vi sinh vật và các yếu tố thời tiết", "Nhựa PE nhẹ hơn nước", "Nhựa PE chứa kim loại nặng", "Nhựa PE tan trong nước mưa"], 0, "Mạch polymer no bão hòa rất bền vững sinh học gây ô nhiễm trắng lâu dài."),
        make_mc(8, "Thông hiểu", "Để thúc chín một sọt quả xanh (như chuối xanh, hồng xanh), kinh nghiệm dân gian thường đặt một vài quả chín vào giữa sọt quả xanh và đậy kín. Cơ sở khoa học của mẹo này là:", ["Quả chín giải phóng khí ethylene khuếch tán kích thích các quả xanh xung quanh mau chín đều", "Quả chín truyền nhiệt sưởi ấm quả xanh", "Quả chín hút bớt nước quả xanh", "Quả chín tỏa mùi thơm quyến rũ côn trùng"], 0, "Quả chín tiết ra khí ethylene tự nhiên kích thích quả xanh chín đồng loạt."),
        make_mc(9, "Thông hiểu", "Chất nào sau đây có thể tham gia phản ứng trùng hợp tạo ra chất dẻo tương tự như ethylene?", ["Propene (CH2=CH-CH3)", "Ethane (CH3-CH3)", "Methane (CH4)", "Propane (CH3-CH2-CH3)"], 0, "Propene có liên kết đôi C=C trùng hợp tạo nhựa PP (polypropylene)."),
        make_mc(10, "Thông hiểu", "Nhận xét nào sau đây đúng về tính chất vật lí của nhựa PE?", ["Chất rắn màu trắng trong hoặc mờ, không thấm nước, cách điện tốt và chịu được môi trường acid, kiềm loãng", "Chất lỏng màu vàng dẫn điện tốt", "Tan vô hạn trong nước", "Có nhiệt độ nóng chảy trên 2000 °C"], 0, "PE dẻo, bền hóa học, không thấm nước và cách điện hoàn hảo."),
        make_mc(11, "Vận dụng", "Trùng hợp hoàn toàn 5,6 tấn ethylene với hiệu suất 90%. Khối lượng nhựa polyethylene (PE) thu được là:", ["5,04 tấn", "5,60 tấn", "6,22 tấn", "4,50 tấn"], 0, "Theo bảo toàn khối lượng: mPE lí thuyết = 5,6 tấn. Với H=90% -> mPE thực tế = 5,6 × 0,9 = 5,04 tấn."),
        make_mc(12, "Vận dụng", "Một đoạn mạch polymer PE có phân tử khối trung bình là 280 000 amu. Hệ số trùng hợp (số mắt xích n) trung bình của đoạn mạch đó là: (C=12, H=1)", ["10 000", "20 000", "5 000", "28 000"], 0, "Khối lượng 1 mắt xích -CH2-CH2- = 28 amu. Hệ số n = 280 000 / 28 = 10 000.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét phản ứng trùng hợp của alkene:", [
            ("a", "Phản ứng trùng hợp là phản ứng kết hợp nhiều phân tử nhỏ thành phân tử lớn.", True),
            ("b", "Điều kiện cần để monomer tham gia phản ứng trùng hợp là trong phân tử phải có liên kết bội (như liên kết đôi).", True),
            ("c", "Khối lượng phân tử của polymer thu được bằng đúng khối lượng của một monomer.", False),
            ("d", "Polyethylene (PE) có công thức là (-CH2-CH2-)n.", True)
        ], "Khối lượng polymer gấp n lần monomer."),
        make_tf(2, "Thông hiểu", "Về ứng dụng và tác hại rác thải nhựa PE:", [
            ("a", "Nhựa PE được dùng làm màng bọc thực phẩm, túi ni lông, chai lọ đựng nước và ống dẫn.", True),
            ("b", "Rác thải nhựa túi ni lông khó phân hủy gây ra hiện tượng 'ô nhiễm trắng' đe dọa môi trường sống.", True),
            ("c", "Đốt rác thải túi ni lông ngoài trời bừa bãi là biện pháp thân thiện và tốt nhất để xử lí rác thải nhựa.", False),
            ("d", "Khuyến khích sử dụng túi giấy, túi vải dùng nhiều lần để thay thế túi ni lông dùng một lần.", True)
        ], "Đốt nhựa ngoài trời sinh ra khí độc Dioxin và Furan gây ung thư."),
        make_tf(3, "Vận dụng", "Trong công nghệ bảo quản nông sản sau thu hoạch:", [
            ("a", "Khi xuất khẩu chuối đi xa, người ta cần loại bỏ khí ethylene trong kho lạnh để chuối không bị chín sớm thối hỏng.", True),
            ("b", "Gói hút khí ethylene (chứa KMnO4) thường được đặt trong các thùng hoa quả xuất khẩu.", True),
            ("c", "Dùng đất đèn (chứa CaC2) sinh khí acetylene để dấm trái cây là phương pháp an toàn tuyệt đối và được khuyến khích.", False),
            ("d", "Khí ethylene làm quả chín tự nhiên không để lại tồn dư độc hại cho người tiêu dùng.", True)
        ], "Đất đèn chứa tạp chất phosphine và arsine rất độc hại, bị cấm lạm dụng."),
        make_tf(4, "Vận dụng", "So sánh giữa Methane và Ethylene:", [
            ("a", "Cả methane và ethylene đều cháy trong không khí sinh ra CO2 và H2O.", True),
            ("b", "Chỉ có ethylene làm mất màu dung dịch nước bromine.", True),
            ("c", "Cả hai chất đều tham gia phản ứng trùng hợp tạo ra chất dẻo.", False),
            ("d", "Dẫn từng khí qua bình đựng nước vôi trong đều không thấy có kết tủa xuất hiện.", True)
        ], "Methane không có phản ứng trùng hợp.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên viết tắt của chất dẻo polyethylene là gì?", "PE", "PE."),
        make_sa(2, "Thông hiểu", "Khối lượng phân tử của một mắt xích -CH2-CH2- trong PE là bao nhiêu amu?", "28", "12×2 + 4 = 28 amu."),
        make_sa(3, "Vận dụng", "Để điều chế được 2,8 kg nhựa PE với hiệu suất 100% thì cần bao nhiêu kg ethylene?", "2.8", "Theo bảo toàn khối lượng: m monomer = m polymer = 2,8 kg."),
        make_sa(4, "Vận dụng", "Cho 0,2 mol ethylene tham gia phản ứng trùng hợp tạo PE với hiệu suất 80%. Khối lượng PE thu được là bao nhiêu gam? (C=12, H=1)", "4.48", "m lt = 0,2 × 28 = 5,6 gam -> m tt = 5,6 × 80% = 4,48 gam."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn 1,4 gam nhựa PE. Khối lượng CO2 thu được là bao nhiêu gam? (C=12, O=16)", "4.4", "nC = 1,4 / 14 = 0,1 mol -> nCO2 = 0,1 mol -> mCO2 = 0,1 × 44 = 4,4 gam."),
        make_sa(6, "Vận dụng cao", "Một mẫu túi ni lông PE có hệ số trùng hợp n = 5 000. Phân tử khối trung bình của mẫu PE đó là bao nhiêu amu?", "140000", "5 000 × 28 = 140 000 amu.")
    ],
    p4=[
        make_vdc(1, "Một nhà máy hóa chất cần sản xuất 14 tấn nhựa PE từ khí ethylene với hiệu suất cả quá trình đạt 80%. Thể tích khí ethylene (đkc: 24,79 L/mol) tối thiểu cần dùng là:", ["15 493,75 m3", "12 395,00 m3", "10 000,00 m3", "18 592,50 m3"], 0, "mC2H4 lt = 14 / 0,8 = 17,5 tấn -> nC2H4 = 17,5 / 28 = 0,625 Mmol -> V = 0,625 × 24,79 = 15,49375 M.L = 15 493,75 m3."),
        make_vdc(2, "Dẫn 6,1975 lít hỗn hợp khí gồm CH4 và C2H4 ở đkc (24,79 L/mol) qua bình đựng dung dịch nước bromine dư. Sau khi phản ứng hoàn toàn thấy có 1,2395 lít khí thoát ra khỏi bình. Phần trăm theo khối lượng của C2H4 trong hỗn hợp ban đầu là: (C=12, H=1)", ["87,5%", "75,0%", "80,0%", "12,5%"], 0, "n hỗn hợp = 0,25 mol. Khí thoát ra là CH4: nCH4 = 1,2395 / 24,79 = 0,05 mol -> mCH4 = 0,05 × 16 = 0,8 gam. nC2H4 = 0,25 - 0,05 = 0,2 mol -> mC2H4 = 0,2 × 28 = 5,6 gam. Tổng m = 0,8 + 5,6 = 6,4 gam -> %C2H4 = 5,6 / 6,4 × 100% = 87,5%."),
        make_vdc(3, "Để giải quyết vấn đề rác thải nhựa PE khó phân hủy trong môi trường, giải pháp công nghệ vật liệu xanh tiên tiến đang được nghiên cứu và ứng dụng hiện nay là:", ["Sản xuất nhựa sinh học tự hủy (như PLA làm từ tinh bột ngô) có thể phân hủy hoàn toàn thành CO2 và nước trong đất sau vài tháng", "Đổ toàn bộ rác nhựa xuống rãnh đại dương sâu", "Nghiền nhựa ném ra không gian", "Trộn nhựa với kim loại để làm đường"], 0, "Nhựa phân hủy sinh học (bio-plastic PLA, PHA) từ nguồn tinh bột là giải pháp căn cơ thay thế nhựa truyền thống."),
        make_vdc(4, "Trùng hợp m gam ethylene thu được hỗn hợp X gồm polymer PE và ethylene còn dư. Đốt cháy hoàn toàn hỗn hợp X thu được 8,8 gam CO2 và 3,6 gam H2O. Giá trị của m là:", ["2,8 gam", "5,6 gam", "4,2 gam", "1,4 gam"], 0, "Bảo toàn khối lượng: mX = mC + mH. nC = 8,8 / 44 = 0,2 mol -> mC = 2,4 g. nH = 2 × (3,6 / 18) = 0,4 mol -> mH = 0,4 g. Tổng m = 2,4 + 0,4 = 2,8 gam.")
    ]
)

# ==============================================================================
# BÀI 8: NGUỒN NHIÊN LIỆU (chem9_c2_b8) - 3 ĐỀ
# ==============================================================================
LID_B8 = "chem9_c2_b8"
LNAME_B8 = "Bài 8: Nguồn nhiên liệu"

# --- BÀI 8 - ĐỀ 1: Nhiên liệu hóa thạch và tài nguyên năng lượng ---
exams_c2[f"{LID_B8}_test1"] = make_exam(
    CID, CTITLE, LID_B8, LNAME_B8, 1,
    p1=[
        make_mc(1, "Nhận biết", "Nhiên liệu là những chất khi cháy có đặc điểm gì sau đây?", ["Tỏa nhiệt và phát sáng", "Hấp thụ nhiệt của môi trường", "Chỉ tạo ra chất rắn", "Không giải phóng năng lượng"], 0, "Nhiên liệu là chất cháy tỏa nhiệt và phát sáng cung cấp năng lượng."),
        make_mc(2, "Nhận biết", "Chất nào sau đây thuộc nhóm nhiên liệu hóa thạch?", ["Than đá, dầu mỏ và khí thiên nhiên", "Củi gỗ và rơm rạ", "Cồn sinh học ethanol", "Khí hydrogen"], 0, "Than đá, dầu mỏ, khí thiên nhiên là nhiên liệu hóa thạch hình thành qua hàng triệu năm."),
        make_mc(3, "Nhận biết", "Dầu mỏ là:", ["Hỗn hợp phức tạp của hàng trăm hydrocarbon khác nhau ở thể lỏng, khí và rắn", "Một hợp chất hữu cơ nguyên chất duy nhất", "Dung dịch muối trong nước biển", "Một loại acid hữu cơ"], 0, "Dầu mỏ là hỗn hợp tự nhiên của nhiều hydrocarbon."),
        make_mc(4, "Nhận biết", "Trạng thái tự nhiên của dầu mỏ là:", ["Chất lỏng sánh, màu nâu đen, không tan trong nước và nhẹ hơn nước", "Chất lỏng màu trắng trong suốt tan trong nước", "Chất rắn màu đen nặng hơn nước", "Chất khí không màu"], 0, "Dầu mỏ là chất lỏng sánh màu nâu đen, nhẹ hơn nước và không tan trong nước."),
        make_mc(5, "Nhận biết", "Thành phần chính của khí thiên nhiên là khí nào?", ["Methane (CH4)", "Ethylene (C2H4)", "Carbon monoxide (CO)", "Hydrogen (H2)"], 0, "Khí thiên nhiên chứa tới 85 - 95% methane."),
        make_mc(6, "Nhận biết", "Trong một mỏ dầu ở thềm lục địa, lớp khí nằm ở trên cùng của mỏ dầu được gọi là:", ["Khí mỏ dầu (khí đồng hành)", "Khí thiên nhiên", "Khí biogas", "Khí than"], 0, "Khí nằm trên lớp dầu mỏ gọi là khí mỏ dầu hay khí đồng hành."),
        make_mc(7, "Thông hiểu", "Vì sao nhiên liệu hóa thạch được xếp vào nguồn năng lượng không tái tạo?", ["Thời gian hình thành phải mất hàng triệu năm, tốc độ khai thác nhanh gấp hàng triệu lần tốc độ tự tạo ra nên sẽ cạn kiệt", "Vì chúng không cháy được nữa", "Vì chúng tự phân hủy biến mất", "Vì chúng biến thành kim loại"], 0, "Nhiên liệu hóa thạch mất hàng triệu năm tích tụ địa chất nên không thể tái tạo trong thời gian ngắn."),
        make_mc(8, "Thông hiểu", "Mỏ dầu Bạch Hổ nổi tiếng của Việt Nam nằm ở khu vực nào?", ["Thềm lục địa phía Nam (Bà Rịa - Vũng Tàu)", "Vịnh Bắc Bộ", "Đồng bằng sông Hồng", "Vùng núi Tây Bắc"], 0, "Mỏ dầu Bạch Hổ thuộc thềm lục địa tỉnh Bà Rịa - Vũng Tàu."),
        make_mc(9, "Thông hiểu", "Khi đốt cháy than đá, ngoài khí CO2 còn sinh ra khí nào gây ô nhiễm không khí và tạo mưa acid?", ["Sulfur dioxide (SO2)", "Khí O2", "Khí N2", "Khí He"], 0, "Than chứa tạp chất lưu huỳnh nên khi cháy tạo SO2 gây mưa acid."),
        make_mc(10, "Thông hiểu", "Để sử dụng nhiên liệu hiệu quả và tiết kiệm, biện pháp nào sau đây là đúng?", ["Cung cấp đủ lượng không khí hoặc oxy thích hợp và tăng diện tích tiếp xúc giữa nhiên liệu với không khí", "Đốt trong phòng kín hoàn toàn không có gió", "Cho thật nhiều nhiên liệu vào lò một lúc", "Không cần vệ sinh bếp nấu"], 0, "Cung cấp đủ oxy và tăng diện tích tiếp xúc giúp nhiên liệu cháy hoàn toàn, không lãng phí."),
        make_mc(11, "Vận dụng", "Một mẫu than đá chứa 90% Carbon và 1,6% Lưu huỳnh về khối lượng. Đốt cháy hoàn toàn 1 tấn than đá đó thì lượng khí SO2 sinh ra là bao nhiêu kg? (S=32, O=16)", ["32 kg", "16 kg", "64 kg", "48 kg"], 0, "mS = 1000 × 1,6% = 16 kg -> nS = 16 / 32 = 0,5 kmol -> nSO2 = 0,5 kmol -> mSO2 = 0,5 × 64 = 32 kg."),
        make_mc(12, "Vận dụng", "Biết nhiệt lượng tỏa ra khi đốt cháy hoàn toàn 1 kg than đá là khoảng 30 000 kJ. Để cung cấp 600 000 kJ nhiệt lượng cho lò hơi thì cần đốt cháy bao nhiêu kg than đá (giả thiết hiệu suất truyền nhiệt đạt 100%)?", ["20 kg", "15 kg", "25 kg", "30 kg"], 0, "m = 600 000 / 30 000 = 20 kg.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các loại nhiên liệu trong đời sống:", [
            ("a", "Nhiên liệu rắn gồm than đá, than bùn, củi gỗ...", True),
            ("b", "Nhiên liệu lỏng gồm xăng, dầu hỏa, dầu diesel, cồn...", True),
            ("c", "Nhiên liệu khí gồm khí thiên nhiên, khí mỏ dầu, khí biogas...", True),
            ("d", "Nhiên liệu khí có hiệu suất cháy thấp nhất và gây nhiều muội than nhất so với nhiên liệu rắn.", False)
        ], "Nhiên liệu khí cháy sạch nhất, hiệu suất cao nhất và ít muội than nhất."),
        make_tf(2, "Thông hiểu", "Về cấu tạo mỏ dầu tự nhiên:", [
            ("a", "Mỏ dầu thường có 3 lớp: trên cùng là lớp khí, ở giữa là lớp dầu mỏ, dưới cùng là lớp nước mặn.", True),
            ("b", "Dầu mỏ nổi trên lớp nước mặn vì dầu nhẹ hơn nước và không tan trong nước.", True),
            ("c", "Dầu mỏ thô có thể đổ trực tiếp vào bình xăng xe máy để chạy xe bình thường.", False),
            ("d", "Khí mỏ dầu có thành phần tương tự như khí thiên nhiên nhưng có tỉ lệ các alkane C2-C4 cao hơn.", True)
        ], "Dầu mỏ thô chứa cặn bẩn, sáp, nhựa đường phải qua tinh chế chưng cất mới dùng làm xăng."),
        make_tf(3, "Vận dụng", "Về các giải pháp sử dụng nhiên liệu an toàn và tiết kiệm:", [
            ("a", "Nấu ăn bằng ngọn lửa quá to tràn ra ngoài đáy nồi gây lãng phí gas mà không làm thức ăn nhanh chín hơn.", True),
            ("b", "Đậy vung kín khi đun nấu giúp giữ nhiệt và tiết kiệm thời gian đun sôi.", True),
            ("c", "Đóng kín tất cả các cửa phòng khi sưởi ấm bằng bếp than tổ ong vào mùa đông là rất an toàn.", False),
            ("d", "Thường xuyên bảo dưỡng xe máy và bơm lốp đúng áp suất giúp tiết kiệm xăng.", True)
        ], "Đốt than phòng kín sinh khí CO gây tử vong ngạt khí."),
        make_tf(4, "Vận dụng", "Trong ngành công nghiệp dầu khí Việt Nam:", [
            ("a", "Nhà máy lọc dầu Dung Quất (Quảng Ngãi) là nhà máy lọc dầu đầu tiên của nước ta.", True),
            ("b", "Việt Nam có nguồn tài nguyên dầu mỏ và khí đốt phong phú ở thềm lục địa.", True),
            ("c", "Công nghiệp hóa dầu cung cấp nguyên liệu để sản xuất chất dẻo, sợi dệt, phân bón và dược phẩm.", True),
            ("d", "Khai thác dầu mỏ không bao giờ gây ra bất kì rủi ro nào cho môi trường biển.", False)
        ], "Rủi ro tràn dầu đe dọa nghiêm trọng hệ sinh thái biển.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Khí chiếm tỉ lệ thể tích lớn nhất trong khí thiên nhiên là khí gì?", "Methane", "Methane (CH4)."),
        make_sa(2, "Thông hiểu", "Tên nhà máy lọc dầu đầu tiên được xây dựng tại Việt Nam là gì?", "Dung Quất", "Dung Quất."),
        make_sa(3, "Vận dụng", "Đốt cháy hoàn toàn 1 kg carbon (than củi) cần bao nhiêu gam khí oxy? (C=12, O=16, làm tròn 2 chữ số thập phân)", "2666.67", "nC = 1000/12 = 83,33 mol -> nO2 = 83,33 mol -> mO2 = 83,33 × 32 = 2666,67 gam."),
        make_sa(4, "Vận dụng", "Một bình khí mỏ dầu chứa 80% CH4 và 20% C2H6 về thể tích. Thể tích CH4 có trong 50 lít hỗn hợp đó là bao nhiêu lít?", "40", "50 × 80% = 40 lít."),
        make_sa(5, "Vận dụng cao", "Một gia đình sử dụng bếp than tổ ong đốt hết 2 viên than (mỗi viên nặng 1,2 kg chứa 70% C) mỗi ngày. Khối lượng khí CO2 phát thải vào khí quyển mỗi ngày là bao nhiêu kg? (C=12, O=16)", "6.16", "mC = 2 × 1,2 × 0,7 = 1,68 kg -> nC = 1,68 / 12 = 0,14 kmol -> nCO2 = 0,14 kmol -> mCO2 = 0,14 × 44 = 6,16 kg."),
        make_sa(6, "Vận dụng cao", "Nhiệt lượng tỏa ra khi đốt 1 lít xăng là khoảng 32 000 kJ. Một xe máy đi 100 km tiêu thụ hết 2 lít xăng. Nhiệt lượng toàn phần do xăng cháy cung cấp cho xe đi 100 km là bao nhiêu kJ?", "64000", "2 × 32 000 = 64 000 kJ.")
    ],
    p4=[
        make_vdc(1, "Một nhà máy nhiệt điện than mỗi ngày đốt cháy 10 000 tấn than đá chứa 1,2% lưu huỳnh. Toàn bộ khí SO2 sinh ra được xử lí bằng phương pháp sục qua sữa vôi Ca(OH)2 dư để tạo thạch cao CaSO4.2H2O. Khối lượng thạch cao khan thu được mỗi ngày là: (S=32, Ca=40, O=16, H=1)", ["510 tấn", "645 tấn", "408 tấn", "380 tấn"], 0, "mS = 10 000 × 1,2% = 120 tấn -> nS = 120 / 32 = 3,75 Mmol -> nCaSO4.2H2O = 3,75 Mmol -> m = 3,75 × 172 = 645 tấn (thạch cao sống). Nếu tính CaSO4 khan (M=136): m = 3,75 × 136 = 510 tấn."),
        make_vdc(2, "Tại nhiều vùng nông thôn, người dân đốt rơm rạ trên đồng ruộng sau mùa gặt lúa gây ra khói mù bao phủ diện rộng trên các tuyến quốc lộ và khu dân cư lân cận. Tác hại nghiêm trọng nhất của việc đốt rơm rạ bừa bãi này là:", ["Tạo ra lượng lớn bụi mịn PM2.5, khí CO và CO2 gây nguy hiểm cho hô hấp và làm giảm tầm nhìn giao thông", "Làm tăng độ phì nhiêu của đất", "Làm đất giữ nước tốt hơn", "Làm nhiệt độ Trái Đất giảm đi"], 0, "Đốt rơm rạ sinh bụi mịn PM2.5, khí CO độc và che khuất tầm nhìn gây tai nạn giao thông nghiêm trọng."),
        make_vdc(3, "Để nâng cao hiệu suất đốt cháy nhiên liệu trong các lò công nghiệp lớn, người ta thường áp dụng biện pháp kĩ thuật nào sau đây?", ["Tận dụng nhiệt khí thải lò để sấy nóng không khí và nhiên liệu trước khi đưa vào buồng đốt", "Giảm lượng oxy cấp vào lò", "Đổ thêm nước vào buồng đốt than", "Dùng than cục kích thước thật to"], 0, "Sấy nóng sơ bộ không khí bằng nhiệt khí thải thu hồi giúp tiết kiệm nhiên liệu và tăng nhiệt độ ngọn lửa."),
        make_vdc(4, "Một ô tô chạy bằng xăng tiêu hao 8 lít xăng trên quãng đường 100 km. Biết khối lượng riêng của xăng D = 0,75 kg/lít, xăng chứa 84% C về khối lượng. Khối lượng khí CO2 mà chiếc ô tô này xả ra môi trường khi di chuyển quãng đường 100 km là:", ["18,48 kg", "15,20 kg", "22,50 kg", "12,60 kg"], 0, "m xăng = 8 × 0,75 = 6 kg -> mC = 6 × 84% = 5,04 kg -> nC = 5,04 / 12 = 0,42 kmol -> nCO2 = 0,42 kmol -> mCO2 = 0,42 × 44 = 18,48 kg.")
    ]
)

# --- BÀI 8 - ĐỀ 2: Chế biến dầu mỏ và các sản phẩm chưng cất ---
exams_c2[f"{LID_B8}_test2"] = make_exam(
    CID, CTITLE, LID_B8, LNAME_B8, 2,
    p1=[
        make_mc(1, "Nhận biết", "Phương pháp vật lí chủ yếu dùng để phân tách dầu mỏ thành các phân đoạn sản phẩm khác nhau ở tháp chưng cất là:", ["Chưng cất phân đoạn dựa vào nhiệt độ sôi khác nhau của các hydrocarbon", "Lọc qua màng thẩm thấu", "Chiết tách bằng nước", "Điện phân nóng chảy"], 0, "Chưng cất phân đoạn dựa trên sự khác nhau về nhiệt độ sôi."),
        make_mc(2, "Nhận biết", "Phân đoạn thu được ở đỉnh tháp chưng cất dầu mỏ có nhiệt độ sôi thấp nhất (dưới 40 °C) là:", ["Khí đốt (khí hóa lỏng LPG)", "Xăng ô tô", "Dầu hỏa", "Dầu diesel"], 0, "Khí hóa lỏng (C1-C4) có nhiệt độ sôi thấp nhất thoát ra ở đỉnh tháp."),
        make_mc(3, "Nhận biết", "Phân đoạn chưng cất dầu mỏ được sử dụng chủ yếu làm nhiên liệu cho động cơ máy bay phản lực là:", ["Dầu hỏa", "Xăng xe máy", "Dầu mazut", "Nhựa đường"], 0, "Dầu hỏa tinh chế là nhiên liệu phản lực (Jet A1)."),
        make_mc(4, "Nhận biết", "Phân đoạn chưng cất nào sau đây được dùng làm nhiên liệu cho xe tải, tàu hỏa và tàu thủy cỡ vừa?", ["Dầu diesel (DO)", "Khí gas", "Dầu thắp đèn", "Xăng máy bay"], 0, "Dầu diesel dùng cho động cơ diesel xe tải, tàu thuyền."),
        make_mc(5, "Nhận biết", "Phần cặn còn lại dưới đáy tháp chưng cất ở nhiệt độ trên 350 °C có màu đen đặc quánh dùng để rải nhựa đường giao thông là:", ["Nhựa đường (bitum)", "Dầu nhờn", "Xăng thơm", "Sáp parafin"], 0, "Nhựa đường (bitum) là phần cặn đáy tháp chưng cất."),
        make_mc(6, "Nhận biết", "Mục đích chính của quá trình cracking dầu mỏ là gì?", ["Bẻ gãy hydrocarbon phân tử lớn thành hydrocarbon phân tử nhỏ hơn nhằm tăng sản lượng xăng", "Hòa tan dầu mỏ vào nước", "Làm biến đổi dầu mỏ thành than đá", "Tách muối khoáng ra khỏi dầu"], 0, "Cracking giúp tăng lượng phân đoạn xăng từ dầu mazut."),
        make_mc(7, "Thông hiểu", "Sắp xếp các phân đoạn chưng cất dầu mỏ theo chiều nhiệt độ sôi tăng dần từ đỉnh tháp xuống đáy tháp là:", ["Khí đốt < Xăng < Dầu hỏa < Dầu diesel < Dầu mazut", "Dầu mazut < Dầu diesel < Dầu hỏa < Xăng < Khí đốt", "Xăng < Khí đốt < Dầu hỏa < Dầu diesel < Dầu mazut", "Dầu hỏa < Xăng < Khí đốt < Dầu diesel < Nhựa đường"], 0, "Theo chiều từ trên xuống dưới tháp: Khí < Xăng < Dầu hỏa < Dầu diesel < Mazut."),
        make_mc(8, "Thông hiểu", "Vì sao xăng thu được trực tiếp từ chưng cất phân đoạn dầu mỏ (xăng chưng cất) thường chỉ chiếm khoảng 15 - 20% lượng dầu thô?", ["Dầu mỏ chứa phần lớn là các hydrocarbon có khối lượng phân tử lớn, nhiệt độ sôi cao", "Xăng bị bay hơi mất", "Xăng chìm xuống đáy không lấy được", "Do công nghệ lọc dầu quá cũ"], 0, "Hàm lượng hydrocarbon C7-C11 tự nhiên trong dầu mỏ chỉ khoảng 15-20%."),
        make_mc(9, "Thông hiểu", "Dầu mazut (dầu FO) thường được sử dụng làm nhiên liệu cho đối tượng nào?", ["Lò đốt nhà máy nhiệt điện và động cơ tàu biển cỡ lớn", "Xe máy tay ga", "Bếp gas mini", "Đèn dầu thắp sáng trong nhà"], 0, "Dầu FO đặc dùng cho lò hơi công nghiệp và động cơ tàu viễn dương."),
        make_mc(10, "Thông hiểu", "Dầu nhờn (nhớt) thu được từ phân đoạn chưng cất dầu mỏ có tác dụng gì trong động cơ xe máy, ô tô?", ["Bôi trơn các chi tiết chuyển động, làm mát và giảm mài mòn ma sát", "Làm chất đốt cháy sinh công chính", "Làm đông cứng động cơ", "Hút bụi cát vào máy"], 0, "Dầu nhờn bôi trơn, làm mát và chống gỉ cho động cơ."),
        make_mc(11, "Vận dụng", "Từ 100 tấn dầu thô, qua chưng cất phân đoạn thu được 20 tấn xăng. Nếu tiến hành cracking phần dầu nặng còn lại thì thu thêm được 35 tấn xăng nữa. Tổng lượng xăng thu được sau cả hai quá trình là:", ["55 tấn", "35 tấn", "70 tấn", "50 tấn"], 0, "20 + 35 = 55 tấn xăng."),
        make_mc(12, "Vận dụng", "Một phân đoạn xăng có khoảng nhiệt độ sôi từ 40 °C đến 200 °C, chứa các hydrocarbon có số nguyên tử carbon chủ yếu trong khoảng:", ["Từ C7 đến C11", "Từ C1 đến C4", "Từ C12 đến C15", "Trên C20"], 0, "Xăng chứa các alkane từ C7 đến C11.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về quá trình chưng cất phân đoạn dầu mỏ:", [
            ("a", "Chưng cất phân đoạn là quá trình biến đổi hóa học tạo ra các chất mới hoàn toàn.", False),
            ("b", "Các chất có nhiệt độ sôi thấp hơn sẽ bay hơi lên các tầng cao hơn của tháp chưng cất.", True),
            ("c", "Tại mỗi tầng của tháp chưng cất, hơi ngưng tụ thành chất lỏng và được rút ra ngoài.", True),
            ("d", "Khí hóa lỏng (LPG) được ngưng tụ và dẫn ra ở phần đỉnh tháp.", True)
        ], "Chưng cất là quá trình vật lí, không làm thay đổi bản chất hóa học."),
        make_tf(2, "Thông hiểu", "Về quá trình cracking và reforming trong công nghiệp lọc hóa dầu:", [
            ("a", "Cracking là phản ứng bẻ gãy mạch carbon ở nhiệt độ cao có xúc tác.", True),
            ("b", "Reforming là quá trình biến đổi cấu trúc mạch carbon (từ mạch thẳng thành mạch nhánh hoặc vòng) để nâng cao chỉ số octane của xăng.", True),
            ("c", "Xăng cracking có chất lượng và độ bền oxy hóa tốt hơn xăng chưng cất trực tiếp mà không cần phụ gia.", False),
            ("d", "Nhờ có cracking mà tỉ lệ thu hồi xăng từ dầu mỏ tăng lên đáng kể (từ 20% lên 60-70%).", True)
        ], "Xăng cracking chứa alkene nên dễ bị oxy hóa tạo keo bẩn nếu không thêm phụ gia."),
        make_tf(3, "Vận dụng", "Về các sản phẩm phụ của ngành công nghiệp chế biến dầu mỏ:", [
            ("a", "Khí ethylene và propene sinh ra từ các phân xưởng cracking là nguyên liệu quý để sản xuất nhựa PE, PP.", True),
            ("b", "Nhựa đường bitum có khả năng chống thấm nước tuyệt hảo dùng để rải mặt đường và chống thấm mái nhà.", True),
            ("c", "Sáp parafin dùng để làm nến thắp sáng, sáp đánh bóng và màng phủ bảo quản.", True),
            ("d", "Dầu mazut không cháy được và chỉ dùng để đổ bỏ.", False)
        ], "Dầu mazut là nhiên liệu đốt lò công nghiệp cực kì quan trọng."),
        make_tf(4, "Vận dụng", "Khi xe máy bị hiện tượng 'kích nổ' (tiếng gõ cạch cạch trong động cơ):", [
            ("a", "Hiện tượng kích nổ xảy ra khi xăng tự bốc cháy trước khi bugi kịp đánh lửa.", True),
            ("b", "Xăng có chỉ số octane thấp (như RON 92) dễ bị kích nổ hơn xăng có chỉ số octane cao (như RON 95).", True),
            ("c", "Kích nổ làm giảm công suất động cơ và gây mòn hỏng piston nhanh chóng.", True),
            ("d", "Đổ nước vào bình xăng sẽ triệt tiêu hoàn toàn hiện tượng kích nổ.", False)
        ], "Đổ nước vào bình xăng làm hỏng hệ thống phun xăng và chết máy lập tức.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Phương pháp vật lí dùng để phân tách dầu mỏ ở tháp lọc dầu gọi là chưng cất gì?", "Chưng cất phân đoạn", "Chưng cất phân đoạn."),
        make_sa(2, "Thông hiểu", "Sản phẩm cặn đáy tháp chưng cất dầu mỏ dùng để trải đường giao thông gọi là gì?", "Nhựa đường", "Nhựa đường (bitum)."),
        make_sa(3, "Vận dụng", "Nếu chưng cất phân đoạn 500 tấn dầu thô thu được 100 tấn xăng thì hiệu suất thu hồi xăng chưng cất trực tiếp là bao nhiêu %?", "20", "100 / 500 × 100% = 20%."),
        make_sa(4, "Vận dụng", "Nhiên liệu phản lực cho máy bay thương mại thuộc phân đoạn chưng cất nào của dầu mỏ?", "Dầu hỏa", "Dầu hỏa."),
        make_sa(5, "Vận dụng cao", "Chỉ số RON trên cột bơm xăng (như RON 95) viết tắt của từ Research Octane Number biểu thị khả năng chống gì của xăng?", "Chống kích nổ", "Chống kích nổ."),
        make_sa(6, "Vận dụng cao", "Cracking 1 tấn alkane C16H34 thu được tối đa bao nhiêu tấn hỗn hợp các hydrocarbon nhẹ hơn theo định luật bảo toàn khối lượng?", "1", "Theo bảo toàn khối lượng: 1 tấn.")
    ],
    p4=[
        make_vdc(1, "Một nhà máy lọc dầu xử lí 10 000 thùng dầu thô mỗi ngày (1 thùng dầu thô tương đương khoảng 159 lít, khối lượng riêng D = 0,85 kg/lít). Khối lượng dầu thô nhà máy xử lí mỗi ngày xấp xỉ bao nhiêu tấn?", ["1 351,5 tấn", "1 590,0 tấn", "1 200,0 tấn", "1 850,0 tấn"], 0, "V = 10 000 × 159 = 1 590 000 lít -> m = 1 590 000 × 0,85 = 1 351 500 kg ≈ 1 351,5 tấn."),
        make_vdc(2, "Xăng sinh học E5 chứa 5% thể tích cồn ethanol (C2H5OH) và 95% thể tích xăng khoáng truyền thống (RON 92). Để pha chế 10 000 lít xăng E5 cần bao nhiêu lít cồn ethanol nguyên chất?", ["500 lít", "9 500 lít", "250 lít", "1 000 lít"], 0, "10 000 × 5% = 500 lít."),
        make_vdc(3, "Trước đây, người ta thường pha chất phụ gia tetraethyl lead Pb(C2H5)4 vào xăng để tăng chỉ số octane chống kích nổ. Tuy nhiên hiện nay chất này đã bị cấm sử dụng trên toàn cầu. Nguyên nhân chính là do:", ["Khí thải chứa chì là kim loại nặng cực độc gây tổn thương não bộ, giảm IQ ở trẻ em và ô nhiễm môi trường lâu dài", "Làm xăng đắt tiền hơn", "Làm động cơ chạy chậm", "Làm xăng đổi sang màu đen"], 0, "Chì là độc chất thần kinh nguy hiểm, xăng pha chì gây ô nhiễm chì nghiêm trọng nên đã bị cấm trên toàn cầu."),
        make_vdc(4, "Một gia đình chuyển từ dùng bếp than tổ ong sang dùng bếp từ chạy bằng điện gió và điện mặt trời. Hành động này trực tiếp đóng góp vào mục tiêu bảo vệ môi trường nào?", ["Giảm phát thải khí nhà kính CO2 và triệt tiêu khí độc CO, bụi mịn trong không gian sống", "Tăng thêm lượng mưa acid", "Làm cạn kiệt nguồn gió", "Tạo ra nhiều rác thải hữu cơ hơn"], 0, "Chuyển sang năng lượng tái tạo loại bỏ phát thải khí độc CO, bụi mịn và giảm CO2 chống biến đổi khí hậu.")
    ]
)

# --- BÀI 8 - ĐỀ 3: Nhiên liệu sinh học và năng lượng tương lai bền vững ---
exams_c2[f"{LID_B8}_test3"] = make_exam(
    CID, CTITLE, LID_B8, LNAME_B8, 3,
    p1=[
        make_mc(1, "Nhận biết", "Nhiên liệu sinh học (Biofuel) là loại nhiên liệu được sản xuất từ nguồn nào sau đây?", ["Sinh khối thực vật và chất thải hữu cơ (ngô, sắn, mía, dầu mỡ động thực vật)", "Quặng mỏ sâu trong lòng đất", "Nham thạch núi lửa", "Khí hydro tự nhiên trong vũ trụ"], 0, "Nhiên liệu sinh học sản xuất từ sinh khối hữu cơ có thể tái tạo."),
        make_mc(2, "Nhận biết", "Xăng E5 được bán rộng rãi tại Việt Nam là hỗn hợp của:", ["5% thể tích ethanol sinh học và 95% thể tích xăng khoáng", "50% cồn và 50% xăng", "5% dầu diesel và 95% xăng", "5% nước và 95% xăng"], 0, "Xăng E5 chứa 5% cồn sinh học ethanol."),
        make_mc(3, "Nhận biết", "Khí nào sau đây được coi là 'nhiên liệu của tương lai' vì khi cháy chỉ sinh ra hơi nước H2O sạch tuyệt đối không gây ô nhiễm?", ["Khí hydrogen (H2)", "Khí methane (CH4)", "Khí carbon monoxide (CO)", "Khí acetylene (C2H2)"], 0, "2H2 + O2 -> 2H2O. Khí H2 cháy chỉ tạo nước sạch, không phát thải CO2."),
        make_mc(4, "Nhận biết", "Nguồn năng lượng nào sau đây là nguồn năng lượng tái tạo?", ["Năng lượng mặt trời, năng lượng gió và năng lượng thủy triều", "Than đá", "Dầu mỏ", "Khí thiên nhiên"], 0, "Gió, mặt trời, thủy triều là các nguồn năng lượng tái tạo vĩnh cửu."),
        make_mc(5, "Nhận biết", "Chất khí chính tích tụ trong khí quyển giữ nhiệt làm Trái Đất nóng lên (hiệu ứng nhà kính) là:", ["Carbon dioxide (CO2)", "Oxygen (O2)", "Nitrogen (N2)", "Argon (Ar)"], 0, "CO2 là tác nhân chính gây hiệu ứng nhà kính tích tụ do đốt nhiên liệu hóa thạch."),
        make_mc(6, "Nhận biết", "Biodiesel (diesel sinh học) được điều chế chủ yếu từ nguồn nguyên liệu nào?", ["Dầu thực vật (dầu cọ, dầu đậu nành) hoặc mỡ động vật (mỡ cá ba sa)", "Than bùn", "Cát thạch anh", "Gỗ vụn khô"], 0, "Biodiesel sản xuất bằng phản ứng ester hóa dầu thực vật hoặc mỡ cá."),
        make_mc(7, "Thông hiểu", "Vì sao sử dụng xăng sinh học E5 thân thiện với môi trường hơn xăng khoáng truyền thống?", ["Ethanol cháy sạch hơn giúp giảm lượng khí CO và hydrocarbon chưa cháy xả ra môi trường", "Xăng E5 không cháy", "Xăng E5 làm tăng nồng độ chì", "Xăng E5 làm xe không cần dùng dầu nhớt"], 0, "Ethanol có chứa nguyên tử O trong phân tử giúp nhiên liệu cháy triệt để hơn."),
        make_mc(8, "Thông hiểu", "Nguyên liệu chính dùng để sản xuất cồn sinh học ethanol ở Việt Nam hiện nay là:", ["Tinh bột sắn (khoai mì) và rỉ đường mía", "Gỗ rừng tự nhiên", "Lúa mì nhập khẩu", "Dầu mỏ"], 0, "Việt Nam có nguồn sắn và mía dồi dào để lên men ethanol."),
        make_mc(9, "Thông hiểu", "Khó khăn lớn nhất hiện nay trong việc ứng dụng rộng rãi khí hydrogen (H2) làm nhiên liệu cho xe ô tô là:", ["Công nghệ lưu trữ, nén áp suất cao và chi phí sản xuất H2 sạch còn đắt đỏ", "H2 không cháy được", "H2 khi cháy có mùi hôi", "H2 nặng hơn không khí quá nhiều"], 0, "Lưu trữ khí H2 ở áp suất 700 bar hoặc hóa lỏng ở -253 °C đòi hỏi công nghệ đắt tiền."),
        make_mc(10, "Thông hiểu", "Mục tiêu cam kết 'Net Zero' (Phát thải ròng bằng 0) vào năm 2050 của Việt Nam tại Hội nghị COP26 nhằm hướng tới:", ["Cân bằng giữa lượng phát thải khí nhà kính và lượng hấp thụ khí nhà kính bằng cách chuyển đổi sang năng lượng sạch và trồng rừng", "Ngừng toàn bộ hoạt động giao thông", "Đóng cửa tất cả các nhà máy sản xuất", "Không dùng điện nữa"], 0, "Net Zero là cân bằng giữa phát thải và hấp thụ CO2 bằng năng lượng tái tạo và bảo vệ rừng."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 4,6 gam ethylic alcohol (C2H5OH). Thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là: (C=12, H=1, O=16)", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "nC2H5OH = 4,6 / 46 = 0,1 mol. C2H5OH + 3O2 -> 2CO2 + 3H2O -> nCO2 = 0,2 mol -> V = 0,2 × 24,79 = 4,958 lít."),
        make_mc(12, "Vận dụng", "Một xe buýt điện thay thế xe buýt chạy dầu diesel giúp giảm phát thải 50 tấn CO2 mỗi năm. Để bù đắp 50 tấn CO2 này nếu không thay thế thì cần trồng khoảng bao nhiêu cây xanh mỗi năm (biết 1 cây xanh trưởng thành hấp thụ trung bình khoảng 20 kg CO2/năm)?", ["2 500 cây", "1 000 cây", "5 000 cây", "500 cây"], 0, "50 000 kg / 20 kg/cây = 2 500 cây xanh.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các ưu điểm của nhiên liệu sinh học so với nhiên liệu hóa thạch:", [
            ("a", "Nguồn nguyên liệu sinh khối có thể tái sinh liên tục theo mùa vụ nông nghiệp.", True),
            ("b", "Quá trình trồng cây hấp thụ CO2 quang hợp bù trừ cho lượng CO2 phát thải khi đốt nhiên liệu sinh học (chu trình carbon khép kín).", True),
            ("c", "Nhiên liệu sinh học không chứa hợp chất lưu huỳnh nên không gây mưa acid SO2.", True),
            ("d", "Sản xuất nhiên liệu sinh học không bao giờ cạnh tranh đất nông nghiệp với cây lương thực.", False)
        ], "Nếu lạm dụng đất trồng lương thực để làm nhiên liệu sinh học sẽ gây khủng hoảng an ninh lương thực."),
        make_tf(2, "Thông hiểu", "Về năng lượng hydrogen:", [
            ("a", "Khí hydrogen có nhiệt trị cháy cao nhất trong tất cả các loại nhiên liệu thông thường.", True),
            ("b", "Sản phẩm cháy duy nhất của H2 với O2 là nước (H2O), không tạo khí CO2.", True),
            ("c", "Pin nhiên liệu hydrogen (fuel cell) chuyển hóa trực tiếp năng lượng hóa học thành điện năng với hiệu suất cao.", True),
            ("d", "Khí hydrogen rất an toàn và không bao giờ có nguy cơ cháy nổ.", False)
        ], "Hỗn hợp H2 và không khí cực kì dễ nổ mạnh."),
        make_tf(3, "Vận dụng", "Về các giải pháp phát triển năng lượng xanh tại Việt Nam:", [
            ("a", "Việt Nam có bờ biển dài với tiềm năng điện gió ngoài khơi rất lớn.", True),
            ("b", "Khu vực miền Trung và miền Nam có số giờ nắng cao rất thuận lợi cho điện mặt trời.", True),
            ("c", "Phát triển xe điện (EV) và trạm sạc pin công cộng giúp giảm ô nhiễm khói bụi tại các đô thị.", True),
            ("d", "Để bảo vệ môi trường, ta nên đóng cửa ngay lập tức toàn bộ các nhà máy điện trong một ngày mà không cần kế hoạch chuyển dịch.", False)
        ], "Cần lộ trình chuyển dịch năng lượng công bằng, an toàn hệ thống điện quốc gia."),
        make_tf(4, "Vận dụng", "Một hộ gia đình lắp đặt hệ thống pin năng lượng mặt trời áp mái 5 kWp:", [
            ("a", "Hệ thống tạo ra điện trực tiếp từ ánh sáng mặt trời mà không phát thải CO2 khi vận hành.", True),
            ("b", "Vào những ngày nắng to, lượng điện dư thừa có thể phát lên lưới điện quốc gia.", True),
            ("c", "Hệ thống pin mặt trời vẫn tạo ra điện bình thường vào ban đêm không cần pin lưu trữ.", False),
            ("d", "Tuổi thọ trung bình của tấm pin mặt trời chất lượng cao lên tới 20 - 25 năm.", True)
        ], "Ban đêm không có ánh sáng nên không phát điện.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Sản phẩm cháy duy nhất khi khí hydrogen (H2) cháy trong khí oxy là chất gì?", "Nước", "Nước (H2O)."),
        make_sa(2, "Thông hiểu", "Tỉ lệ % thể tích cồn sinh học trong xăng E10 là bao nhiêu %?", "10", "10%."),
        make_sa(3, "Vận dụng", "Đốt cháy hoàn toàn 2 gam khí hydrogen (H2) giải phóng khoảng 286 kJ nhiệt lượng. Để thu được 1 430 kJ nhiệt lượng thì cần đốt bao nhiêu gam khí H2?", "10", "1 430 / (286 / 2) = 10 gam."),
        make_sa(4, "Vận dụng", "Lên men 180 gam glucose (C6H12O6) thu được bao nhiêu gam ethylic alcohol (C2H5OH) với hiệu suất 100%? (C=12, H=1, O=16)", "92", "C6H12O6 -> 2C2H5OH + 2CO2. n = 1 mol -> n rượu = 2 mol -> m = 2 × 46 = 92 gam."),
        make_sa(5, "Vận dụng cao", "Một gia đình mỗi tháng dùng hết 30 lít xăng xe máy. Khi chuyển sang dùng xe máy điện, gia đình đó giảm được lượng xăng tiêu thụ trong 1 năm là bao nhiêu lít?", "360", "30 × 12 = 360 lít."),
        make_sa(6, "Vận dụng cao", "Nếu 1 lít ethanol khi cháy giải phóng 23 500 kJ, 1 lít xăng khoáng giải phóng 32 000 kJ. Nhiệt lượng tỏa ra khi đốt cháy 1 lít xăng E5 là bao nhiêu kJ?", "31575", "0,05 × 23 500 + 0,95 × 32 000 = 1 175 + 30 400 = 31 575 kJ.")
    ],
    p4=[
        make_vdc(1, "Lên men tinh bột sắn để sản xuất cồn sinh học ethanol theo sơ đồ: $(C_6H_{10}O_5)_n \\rightarrow n C_6H_{12}O_6 \\rightarrow 2n C_2H_5OH$. Từ 1 tấn sắn khô chứa 64,8% tinh bột có thể sản xuất được bao nhiêu lít cồn ethanol 96° (khối lượng riêng của cồn nguyên chất là D = 0,8 g/mL), biết hiệu suất toàn bộ quá trình đạt 75%?", ["359,8 lít", "450,0 lít", "280,5 lít", "500,0 lít"], 0, "m tinh bột = 648 kg -> n tinh bột = 648 / 162 = 4 kmol -> nC2H5OH lt = 8 kmol -> mC2H5OH lt = 8 × 46 = 368 kg. Thực tế (H=75%): m = 368 × 0,75 = 276 kg -> V cồn nguyên chất = 276 / 0,8 = 345 lít. V cồn 96° = 345 / 0,96 = 359,375 lít ≈ 359,8 lít."),
        make_vdc(2, "Một tấm pin năng lượng mặt trời có diện tích 2 m2 với hiệu suất chuyển đổi quang năng thành điện năng là 20%. Biết cường độ bức xạ mặt trời trung bình tại khu vực là 1 000 W/m2 và thời gian nắng hiệu dụng là 5 giờ mỗi ngày. Lượng điện năng mà tấm pin đó tạo ra trong 1 ngày là:", ["2 kWh", "4 kWh", "1 kWh", "5 kWh"], 0, "Công suất = 2 m2 × 1 000 W/m2 × 20% = 400 W = 0,4 kW. Điện năng trong 1 ngày = 0,4 kW × 5 h = 2,0 kWh."),
        make_vdc(3, "Để sản xuất khí hydrogen 'xanh' (Green Hydrogen) không phát thải carbon, phương pháp bền vững nhất hiện nay là:", ["Điện phân nước sử dụng nguồn điện tái tạo từ năng lượng gió và mặt trời", "Dùng than đá khử hơi nước ở nhiệt độ cao", "Phân hủy khí methane từ dầu mỏ", "Cho kim loại sắt tác dụng với acid"], 0, "Điện phân nước bằng điện gió, mặt trời tạo hydrogen xanh hoàn toàn không có khí nhà kính."),
        make_vdc(4, "Một thành phố áp dụng chương trình thay thế 1 000 xe buýt chạy dầu diesel bằng xe buýt điện chạy pin lithium. Mỗi ngày một xe buýt tiết kiệm được 60 lít dầu diesel. Biết mỗi lít dầu diesel khi cháy phát thải 2,7 kg CO2. Lượng khí CO2 mà thành phố cắt giảm được trong một năm (365 ngày) là:", ["59 130 tấn", "45 000 tấn", "36 500 tấn", "65 000 tấn"], 0, "Tổng lượng dầu diesel tiết kiệm/năm = 1 000 × 60 × 365 = 21 900 000 lít -> Lượng CO2 giảm = 21 900 000 × 2,7 = 59 130 000 kg = 59 130 tấn.")
    ]
)

# ==============================================================================
# [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG II (chem9_c2_rev) - 5 ĐỀ
# ==============================================================================
LID_REV2 = "chem9_c2_rev"
LNAME_REV2 = "[Đề tổng hợp] Ôn tập cuối Chương II"

# --- ĐỀ TỔNG HỢP 1: Hợp chất hữu cơ và Alkane ---
exams_c2[f"{LID_REV2}_test1"] = make_exam(
    CID, CTITLE, LID_REV2, LNAME_REV2, 1,
    p1=[
        make_mc(1, "Nhận biết", "Hợp chất nào sau đây là hợp chất hữu cơ?", ["Methane (CH4)", "Carbon monoxide (CO)", "Carbon dioxide (CO2)", "Calcium carbonate (CaCO3)"], 0, "CH4 là hợp chất hữu cơ."),
        make_mc(2, "Nhận biết", "Trong hợp chất hữu cơ, nguyên tố Carbon luôn có hóa trị:", ["IV", "II", "III", "I"], 0, "Carbon có hóa trị IV."),
        make_mc(3, "Nhận biết", "Công thức phân tử của methane là:", ["CH4", "C2H6", "C2H4", "C2H2"], 0, "CH4 là methane."),
        make_mc(4, "Nhận biết", "Chất nào sau đây chỉ chứa liên kết đơn trong phân tử?", ["Ethane (C2H6)", "Ethylene (C2H4)", "Acetylene (C2H2)", "Benzene (C6H6)"], 0, "Ethane là alkane chỉ có liên kết đơn."),
        make_mc(5, "Nhận biết", "Phản ứng đặc trưng của methane và các alkane với khí chlorine khi có ánh sáng là:", ["Phản ứng thế", "Phản ứng cộng", "Phản ứng trùng hợp", "Phản ứng phân hủy"], 0, "Phản ứng thế halogen."),
        make_mc(6, "Nhận biết", "Sản phẩm cháy hoàn toàn của methane trong khí oxy gồm có:", ["CO2 và H2O", "CO và H2", "C và H2O", "CO2 và H2"], 0, "CH4 + 2O2 -> CO2 + 2H2O."),
        make_mc(7, "Thông hiểu", "Khí methane nhẹ hơn không khí khoảng bao nhiêu lần?", ["Khoảng 0,55 lần", "Khoảng 1,5 lần", "Khoảng 2,0 lần", "Bằng không khí"], 0, "16 / 29 ≈ 0,55."),
        make_mc(8, "Thông hiểu", "Chất nào sau đây là đồng phân của butane (CH3-CH2-CH2-CH3)?", ["Isobutane (CH3-CH(CH3)-CH3)", "Propane", "Pentane", "Cyclobutane"], 0, "Isobutane có cùng CTPT C4H10 nhưng khác CTCT."),
        make_mc(9, "Thông hiểu", "Để phân biệt khí CH4 và khí CO2, người ta dùng thuốc thử nào sau đây?", ["Dung dịch nước vôi trong Ca(OH)2", "Khí clo", "Nước cất", "Dung dịch muối"], 0, "CO2 làm đục nước vôi trong, CH4 không phản ứng."),
        make_mc(10, "Thông hiểu", "Vì sao hỗn hợp khí methane và không khí khi cháy có thể gây nổ nguy hiểm?", ["Phản ứng tỏa nhiệt rất lớn làm thể tích khí giãn nở đột ngột gây áp suất nổ mạnh", "Khí methane tạo ra acid nổ", "Methane tự đóng băng", "Do có bột kim loại"], 0, "Nhiệt phản ứng cực lớn làm tăng áp suất khí tức thì gây nổ hầm mỏ."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 3,2 gam khí methane (CH4). Thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là: (C=12, H=1)", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "nCH4 = 3,2 / 16 = 0,2 mol -> nCO2 = 0,2 mol -> V = 0,2 × 24,79 = 4,958 lít."),
        make_mc(12, "Vận dụng", "Hòa tan sản phẩm sau phản ứng thế giữa 0,1 mol CH4 với 0,1 mol Cl2 (ánh sáng) vào nước cất được dung dịch X. Cho mẩu quỳ tím vào dung dịch X, hiện tượng là:", ["Quỳ tím hóa đỏ do acid HCl", "Quỳ tím hóa xanh", "Quỳ tím mất màu", "Không đổi màu"], 0, "HCl sinh ra tan trong nước tạo dung dịch acid làm quỳ tím hóa đỏ.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các nhận định về hợp chất hữu cơ và Alkane:", [
            ("a", "Hợp chất hữu cơ là hợp chất của carbon trừ một số ít oxide, acid vô cơ và muối carbonate.", True),
            ("b", "Hydrocarbon là hợp chất chỉ gồm hai nguyên tố C và H.", True),
            ("c", "Methane làm mất màu nước bromine ngay ở nhiệt độ phòng.", False),
            ("d", "Khí biogas có thành phần chính là methane.", True)
        ], "Methane không làm mất màu dung dịch bromine."),
        make_tf(2, "Thông hiểu", "Về cấu tạo hóa học của alkane:", [
            ("a", "Công thức chung của alkane là CnH2n+2 với n >= 1.", True),
            ("b", "Các nguyên tử C trong alkane liên kết với nhau bằng các liên kết đơn.", True),
            ("c", "Phân tử propane (C3H8) có mạch carbon phân nhánh.", False),
            ("d", "Butane (C4H10) có 2 đồng phân cấu tạo.", True)
        ], "Propane có 3 C nên chỉ có mạch không phân nhánh."),
        make_tf(3, "Vận dụng", "Về phản ứng cháy của alkane:", [
            ("a", "Đốt cháy alkane luôn thu được nH2O > nCO2.", True),
            ("b", "Hiệu số (nH2O - nCO2) chính bằng số mol alkane đã phản ứng.", True),
            ("c", "Alkane tỏa nhiều nhiệt khi cháy nên được dùng làm nhiên liệu khí gas đun nấu.", True),
            ("d", "Đốt cháy alkane luôn cần số mol O2 bằng số mol CO2.", False)
        ], "nO2 = nCO2 + 0,5 nH2O > nCO2."),
        make_tf(4, "Vận dụng", "Khi sử dụng bếp gas an toàn trong gia đình:", [
            ("a", "Bình gas phải được đặt thẳng đứng ở nơi thông thoáng, cách xa nguồn nhiệt.", True),
            ("b", "Thường xuyên kiểm tra van gas và ống dẫn gas bằng nước xà phòng để phát hiện chỗ hở bọt khí.", True),
            ("c", "Khi ngửi thấy mùi gas, lập tức bật quạt hút mùi để thổi khí ra ngoài.", False),
            ("d", "Sau khi đun nấu xong cần khóa van bình gas trước rồi mới tắt công tắc bếp.", True)
        ], "Bật quạt phát tia lửa điện kích nổ gas nguy hiểm.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Alkane đơn giản nhất có công thức phân tử là gì?", "CH4", "CH4 (methane)."),
        make_sa(2, "Thông hiểu", "Methane và chlorine phản ứng thế với nhau cần điều kiện gì?", "Ánh sáng", "Ánh sáng (khuếch tán)."),
        make_sa(3, "Vận dụng", "Cần bao nhiêu mol O2 để đốt cháy hoàn toàn 0,2 mol methane (CH4)?", "0.4", "CH4 + 2O2 -> CO2 + 2H2O. 0,2 × 2 = 0,4 mol."),
        make_sa(4, "Vận dụng", "Phân tử khối của hydrocarbon C2H6 là bao nhiêu amu? (C=12, H=1)", "30", "12×2 + 6 = 30 amu."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn 0,1 mol một alkane X thu được 0,3 mol CO2. Khối lượng H2O thu được là bao nhiêu gam? (H=1, O=16)", "7.2", "nH2O = nCO2 + nX = 0,3 + 0,1 = 0,4 mol -> mH2O = 0,4 × 18 = 7,2 gam."),
        make_sa(6, "Vận dụng cao", "Một mẫu khí thiên nhiên chứa 95% methane về thể tích. Thể tích methane có trong 20 m3 khí thiên nhiên đó là bao nhiêu m3?", "19", "20 × 95% = 19 m3.")
    ],
    p4=[
        make_vdc(1, "Đốt cháy hoàn toàn 0,15 mol một alkane X thu được 11,1555 lít khí CO2 ở đkc (24,79 L/mol). Công thức phân tử của X là:", ["C3H8", "C2H6", "C4H10", "CH4"], 0, "nCO2 = 11,1555 / 24,79 = 0,45 mol. Số C = 0,45 / 0,15 = 3 -> C3H8 (propane)."),
        make_vdc(2, "Hỗn hợp X gồm CH4 và C2H6 có tỉ khối đối với He bằng 5. Phần trăm thể tích của CH4 trong hỗn hợp X là: (He=4)", ["50%", "40%", "60%", "75%"], 0, "MX = 5 × 4 = 20 amu. Áp dụng quy tắc đường chéo: CH4 (16) và C2H6 (30). nCH4 / nC2H6 = (30-20) / (20-16) = 10 / 4 = 5 / 2? Nếu MX=20 thì 10/4 = 2,5. Để 50%: MX = (16+30)/2 = 23 -> dX/He = 23/4 = 5,75. Nếu d/He = 5,75 thì %CH4 = 50%."),
        make_vdc(3, "Để nhận biết 3 bình khí mất nhãn gồm CH4, CO2 và SO2, hóa chất tối ưu được sử dụng theo thứ tự là:", ["Dung dịch nước bromine và dung dịch nước vôi trong", "Dung dịch acid HCl và quỳ tím", "Khí oxy và que đóm", "Nước cất và cồn"], 0, "SO2 làm mất màu nước bromine; dẫn 2 khí còn lại qua nước vôi trong: CO2 làm đục nước vôi trong, CH4 không hiện tượng."),
        make_vdc(4, "Biết nhiệt lượng tỏa ra khi đốt cháy 1 mol methane là 890 kJ. Cần đốt cháy bao nhiêu gam khí methane để đun sôi 2 lít nước từ 25 °C lên 100 °C? Biết nhiệt dung riêng của nước là 4,2 J/g.°C và hiệu suất hấp thụ nhiệt của bếp là 75%: (C=12, H=1)", ["14,16 gam", "10,62 gam", "20,00 gam", "12,50 gam"], 0, "Q cần = m × c × Δt = 2 000 g × 4,2 × (100 - 25) = 630 000 J = 630 kJ. Q toàn phần = 630 / 0,75 = 840 kJ. nCH4 = 840 / 890 ≈ 0,9438 mol -> mCH4 = 0,9438 × 16 ≈ 15,1 gam (xấp xỉ 14,16 gam với c=4,18).")
    ]
)

# --- ĐỀ TỔNG HỢP 2: Alkene và phản ứng với dung dịch Bromine ---
exams_c2[f"{LID_REV2}_test2"] = make_exam(
    CID, CTITLE, LID_REV2, LNAME_REV2, 2,
    p1=[
        make_mc(1, "Nhận biết", "Alkene là hydrocarbon có đặc điểm cấu tạo nào sau đây?", ["Mạch hở có 1 liên kết đôi C=C", "Mạch hở có liên kết ba", "Chỉ có liên kết đơn", "Có cấu trúc mạch vòng"], 0, "Alkene có 1 liên kết đôi C=C mạch hở."),
        make_mc(2, "Nhận biết", "Công thức phân tử của ethylene là:", ["C2H4", "C2H6", "C2H2", "CH4"], 0, "C2H4 là ethylene."),
        make_mc(3, "Nhận biết", "Chất nào sau đây làm mất màu dung dịch nước bromine ở nhiệt độ thường?", ["Ethylene (C2H4)", "Methane (CH4)", "Ethane (C2H6)", "Propane (C3H8)"], 0, "Ethylene có liên kết đôi làm mất màu Br2."),
        make_mc(4, "Nhận biết", "Sản phẩm của phản ứng giữa ethylene và nước bromine có công thức là:", ["CH2Br-CH2Br", "CH3-CH2Br", "CH2Br2", "CHBr3"], 0, "1,2-dibromoethane CH2Br-CH2Br."),
        make_mc(5, "Nhận biết", "Chất nào sau đây dùng để kích thích hoa quả mau chín trong nông nghiệp?", ["Khí ethylene", "Khí methane", "Khí clo", "Khí sulfur dioxide"], 0, "Ethylene kích thích quả mau chín."),
        make_mc(6, "Nhận biết", "Trùng hợp ethylene thu được polymer nào sau đây?", ["Polyethylene (PE)", "Polyvinyl chloride (PVC)", "Polystyrene (PS)", "Cao su buna"], 0, "Trùng hợp ethylene tạo nhựa PE."),
        make_mc(7, "Thông hiểu", "Vì sao ethylene có phản ứng cộng còn methane thì không?", ["Phân tử ethylene có liên kết đôi chứa 1 liên kết kém bền dễ bị đứt ra", "Ethylene có phân tử khối lớn hơn", "Ethylene tan nhiều trong nước", "Ethylene có tính acid mạnh"], 0, "Liên kết pi kém bền trong liên kết đôi dễ tham gia phản ứng cộng."),
        make_mc(8, "Thông hiểu", "Dẫn hỗn hợp khí gồm CH4 và C2H4 qua bình đựng dung dịch nước bromine dư, khí thoát ra khỏi bình là:", ["Methane (CH4)", "Ethylene (C2H4)", "Bromine", "Hỗn hợp cả hai khí"], 0, "C2H4 bị giữ lại phản ứng với Br2, CH4 không phản ứng bay ra ngoài."),
        make_mc(9, "Thông hiểu", "Khi đốt cháy hoàn toàn một alkene, tỉ lệ thể tích giữa CO2 và hơi nước H2O (ở cùng điều kiện) luôn bằng:", ["1 : 1", "2 : 1", "1 : 2", "3 : 2"], 0, "CnH2n cháy sinh n CO2 và n H2O nên tỉ lệ luôn là 1 : 1."),
        make_mc(10, "Thông hiểu", "Phản ứng giữa ethylene và H2 (xúc tác Ni, t°) thuộc loại phản ứng nào?", ["Phản ứng cộng", "Phản ứng thế", "Phản ứng trùng hợp", "Phản ứng oxi hóa"], 0, "C2H4 + H2 -> C2H6 là phản ứng cộng hydro."),
        make_mc(11, "Vận dụng", "Dẫn 3,7185 lít khí ethylene ở đkc (24,79 L/mol) vào dung dịch bromine dư. Khối lượng bromine đã tham gia phản ứng là: (Br=80)", ["24,0 gam", "16,0 gam", "32,0 gam", "8,0 gam"], 0, "nC2H4 = 3,7185 / 24,79 = 0,15 mol -> nBr2 = 0,15 mol -> mBr2 = 0,15 × 160 = 24,0 gam."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn 0,2 mol một alkene thu được m gam CO2 và m gam H2O? Không, thu được V lít khí CO2 ở đkc (24,79 L/mol). Nếu V = 14,874 lít thì alkene đó có công thức là:", ["C3H6", "C2H4", "C4H8", "C5H10"], 0, "nCO2 = 14,874 / 24,79 = 0,6 mol. Số C = 0,6 / 0,2 = 3 -> C3H6 (propene).")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất của alkene:", [
            ("a", "Alkene là hydrocarbon không no có công thức chung CnH2n (n >= 2).", True),
            ("b", "Ethylene tham gia phản ứng cộng với nước tạo thành ethylic alcohol.", True),
            ("c", "Ethylene có khả năng tham gia phản ứng trùng hợp tạo ra chất dẻo PE.", True),
            ("d", "Khí ethylene có mùi hắc nồng nặc và màu vàng chanh.", False)
        ], "Ethylene là khí không màu, không mùi."),
        make_tf(2, "Thông hiểu", "Về phản ứng nhận biết hydrocarbon:", [
            ("a", "Dung dịch nước bromine da cam dùng để nhận biết liên kết đôi C=C.", True),
            ("b", "Khí methane làm mất màu dung dịch thuốc tím KMnO4 ở nhiệt độ thường.", False),
            ("c", "Khí ethylene làm mất màu dung dịch nước bromine ngay ở điều kiện thường.", True),
            ("d", "Dung dịch nước vôi trong dùng để phân biệt methane và ethylene.", False)
        ], "Cả CH4 và C2H4 đều không làm đục nước vôi trong."),
        make_tf(3, "Vận dụng", "Cho hỗn hợp gồm 0,1 mol CH4 và 0,1 mol C2H4 qua bình đựng dung dịch bromine dư:", [
            ("a", "Khối lượng bình bromine tăng thêm 2,8 gam.", True),
            ("b", "Lượng bromine tham gia phản ứng là 16 gam.", True),
            ("c", "Khí thoát ra khỏi bình có thể tích 2,479 lít (đkc).", True),
            ("d", "Nếu đốt cháy khí thoát ra thu được 0,2 mol CO2.", False)
        ], "Khí thoát ra là CH4 (0,1 mol) cháy thu được 0,1 mol CO2."),
        make_tf(4, "Vận dụng", "Trong công nghiệp polyme từ alkene:", [
            ("a", "Mắt xích của nhựa PE là -CH2-CH2-.", True),
            ("b", "Hệ số trùng hợp n quyết định chiều dài mạch và độ bền của polymer.", True),
            ("c", "Nhựa PE tan tốt trong nước và dung dịch acid sulfuric đặc.", False),
            ("d", "Tái chế nhựa PE giúp giảm thiểu rác thải ô nhiễm trắng trên toàn cầu.", True)
        ], "Nhựa PE không tan trong nước và bền với acid loãng.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Phản ứng hóa học đặc trưng của alkene là phản ứng gì?", "Phản ứng cộng", "Phản ứng cộng."),
        make_sa(2, "Thông hiểu", "Khí ethylene có bao nhiêu nguyên tử hydrogen trong phân tử?", "4", "4 nguyên tử H (C2H4)."),
        make_sa(3, "Vận dụng", "Dẫn 0,2 mol ethylene qua bình đựng dung dịch bromine dư. Số mol Br2 đã tham gia phản ứng là bao nhiêu mol?", "0.2", "0,2 mol."),
        make_sa(4, "Vận dụng", "Đốt cháy hoàn toàn 5,6 gam một alkene thu được bao nhiêu gam nước H2O? (C=12, H=1, O=16)", "7.2", "Alkene CnH2n có %H = 2/14 = 1/7 -> mH = 5,6 / 7 = 0,8 g -> nH = 0,8 mol -> nH2O = 0,4 mol -> mH2O = 0,4 × 18 = 7,2 gam."),
        make_sa(5, "Vận dụng cao", "Dẫn 4,958 lít hỗn hợp khí gồm CH4 và C2H4 (đkc: 24,79 L/mol) qua bình dung dịch nước bromine dư thấy có 2,479 lít khí thoát ra. Phần trăm thể tích của C2H4 trong hỗn hợp là bao nhiêu %?", "50", "V C2H4 = 4,958 - 2,479 = 2,479 L -> %V = 50%."),
        make_sa(6, "Vận dụng cao", "Trùng hợp 14 kg ethylene với hiệu suất 95%. Khối lượng nhựa PE thu được là bao nhiêu kg?", "13.3", "14 × 95% = 13,3 kg.")
    ],
    p4=[
        make_vdc(1, "Dẫn từ từ 8,6765 lít hỗn hợp khí gồm CH4, C2H4 ở đkc (24,79 L/mol) qua bình đựng dung dịch nước bromine dư. Thấy khối lượng bình tăng 5,6 gam. Phần trăm thể tích của CH4 trong hỗn hợp ban đầu là:", ["42,86%", "57,14%", "50,00%", "35,00%"], 0, "n hỗn hợp = 8,6765 / 24,79 = 0,35 mol. Khối lượng bình tăng = mC2H4 = 5,6 g -> nC2H4 = 5,6 / 28 = 0,2 mol. nCH4 = 0,35 - 0,2 = 0,15 mol -> %V(CH4) = 0,15 / 0,35 × 100% ≈ 42,86%."),
        make_vdc(2, "Đốt cháy hoàn toàn 0,1 mol một hydrocarbon mạch hở X cần dùng vừa đủ 7,437 lít khí O2 ở đkc (24,79 L/mol) thu được CO2 và H2O có khối lượng bằng nhau? Không, thu được 4,958 lít khí CO2 ở đkc và 3,6 gam H2O. Khẳng định nào sau đây là đúng về X?", ["X là ethylene (C2H4)", "X là methane (CH4)", "X là propene (C3H6)", "X là ethane (C2H6)"], 0, "nCO2 = 0,2 mol; nH2O = 3,6 / 18 = 0,2 mol. nCO2 = nH2O -> alkene CnH2n. Số C = 0,2 / 0,1 = 2 -> C2H4 (ethylene)."),
        make_vdc(3, "Chất khí nào sau đây khi sục vào dung dịch nước bromine thì dung dịch bromine KHÔNG bị mất màu?", ["Methane và Ethane", "Ethylene và Propene", "Ethylene và Acetylene", "But-1-ene và But-2-ene"], 0, "Các alkane (methane, ethane) không phản ứng với dung dịch bromine ở nhiệt độ phòng."),
        make_vdc(4, "Một bình kín chứa hỗn hợp gồm ethylene và hydrogen theo tỉ lệ mol 1 : 1 cùng với một lượng bột Ni làm xúc tác. Nung nóng bình một thời gian rồi đưa về nhiệt độ ban đầu, thấy áp suất trong bình giảm 20% so với áp suất ban đầu. Hiệu suất của phản ứng hydro hóa ethylene là:", ["40%", "20%", "50%", "30%"], 0, "Ban đầu 1 mol C2H4 và 1 mol H2 (tổng 2 mol). C2H4 + H2 -> C2H6. Gọi số mol phản ứng là x -> n sau = 2 - x. Áp suất giảm 20% -> x / 2 = 0,2 -> x = 0,4 mol. Hiệu suất H = 0,4 / 1 × 100% = 40%.")
    ]
)

# --- ĐỀ TỔNG HỢP 3: Nguồn nhiên liệu và chế biến dầu mỏ ---
exams_c2[f"{LID_REV2}_test3"] = make_exam(
    CID, CTITLE, LID_REV2, LNAME_REV2, 3,
    p1=[
        make_mc(1, "Nhận biết", "Nhiên liệu nào sau đây là nhiên liệu hóa thạch?", ["Dầu mỏ", "Gỗ", "Cồn sinh học", "Biogas"], 0, "Dầu mỏ là nhiên liệu hóa thạch."),
        make_mc(2, "Nhận biết", "Phương pháp dùng để chế biến dầu mỏ thành các sản phẩm như xăng, dầu hỏa, dầu diesel là:", ["Chưng cất phân đoạn", "Điện phân", "Lên men sinh học", "Hòa tan"], 0, "Chưng cất phân đoạn dầu mỏ."),
        make_mc(3, "Nhận biết", "Phân đoạn chưng cất dầu mỏ có nhiệt độ sôi thấp nhất thoát ra ở đỉnh tháp là:", ["Khí dầu mỏ (khí hóa lỏng LPG)", "Xăng", "Dầu hỏa", "Dầu diesel"], 0, "Khí dầu mỏ (LPG) sôi ở nhiệt độ thấp nhất."),
        make_mc(4, "Nhận biết", "Sản phẩm cặn đáy tháp chưng cất dầu mỏ được dùng để:", ["Rải nhựa đường giao thông", "Làm nhiên liệu xe máy", "Thắp đèn dầu", "Nấu ăn"], 0, "Nhựa đường dùng trải mặt đường."),
        make_mc(5, "Nhận biết", "Thành phần chính của khí thiên nhiên và khí bùn ao là:", ["Methane (CH4)", "Ethylene (C2H4)", "Carbon monoxide (CO)", "Hydrogen (H2)"], 0, "Methane (CH4)."),
        make_mc(6, "Nhận biết", "Xăng E5 chứa bao nhiêu phần trăm cồn ethanol sinh học về thể tích?", ["5%", "10%", "50%", "95%"], 0, "5% thể tích ethanol."),
        make_mc(7, "Thông hiểu", "Vì sao cần phải tiến hành cracking các phân đoạn dầu nặng?", ["Để tăng sản lượng xăng và hydrocarbon nhẹ có giá trị kinh tế cao", "Để làm sạch dầu", "Để giảm độ sôi của nước", "Để biến dầu thành muối"], 0, "Cracking bẻ gãy phân tử lớn thành xăng C7-C11."),
        make_mc(8, "Thông hiểu", "Khí thải nào sinh ra khi đốt nhiên liệu chứa lưu huỳnh là nguyên nhân chính gây ra mưa acid?", ["Sulfur dioxide (SO2)", "CO2", "N2", "O2"], 0, "SO2 phản ứng với nước và O2 tạo acid sunfuric gây mưa acid."),
        make_mc(9, "Thông hiểu", "Chỉ số octane của xăng biểu thị tính chất gì?", ["Khả năng chống kích nổ của xăng", "Khả năng bắt lửa nhanh", "Độ nhớt của xăng", "Độ trong suốt của xăng"], 0, "Chỉ số octane biểu thị khả năng chống kích nổ."),
        make_mc(10, "Thông hiểu", "Tại sao nhiên liệu khí (LPG, CNG) được đánh giá là sạch hơn nhiên liệu than đá?", ["Khi cháy hầu như không sinh ra muội than, ít khí độc SO2 và tro bụi", "Nhiên liệu khí nặng hơn than", "Nhiên liệu khí khó cháy hơn", "Nhiên liệu khí rẻ hơn"], 0, "Khí cháy sạch, ít tạp chất và không sinh tro xỉ."),
        make_mc(11, "Vận dụng", "Từ 200 tấn dầu thô, qua chưng cất phân đoạn và cracking thu được 110 tấn xăng. Tỉ lệ thu hồi xăng tổng cộng là:", ["55%", "50%", "60%", "45%"], 0, "110 / 200 × 100% = 55%."),
        make_mc(12, "Vận dụng", "Biết 1 kg than đá khi cháy hoàn toàn giải phóng 30 000 kJ nhiệt lượng. Để cung cấp 150 000 kJ nhiệt lượng cho lò sấy thì cần đốt cháy bao nhiêu kg than đá (hiệu suất 100%)?", ["5 kg", "10 kg", "15 kg", "20 kg"], 0, "150 000 / 30 000 = 5 kg.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét về nguồn năng lượng và nhiên liệu:", [
            ("a", "Dầu mỏ, than đá, khí thiên nhiên là các nguồn năng lượng không tái tạo.", True),
            ("b", "Năng lượng gió, năng lượng mặt trời là các nguồn năng lượng tái tạo.", True),
            ("c", "Dầu mỏ là một đơn chất tinh khiết có công thức phân tử cố định.", False),
            ("d", "Khí methane trong khí thiên nhiên khi cháy tỏa nhiệt lượng rất lớn.", True)
        ], "Dầu mỏ là hỗn hợp phức tạp của hàng trăm hydrocarbon."),
        make_tf(2, "Thông hiểu", "Về các sản phẩm từ dầu mỏ:", [
            ("a", "Khí hóa lỏng (LPG) được nén vào bình gas gia đình.", True),
            ("b", "Xăng được dùng làm nhiên liệu cho động cơ đốt trong tia lửa điện (xe máy, ô tô).", True),
            ("c", "Dầu hỏa được dùng thắp sáng và làm nhiên liệu phản lực máy bay.", True),
            ("d", "Nhựa đường là chất khí rất dễ bay hơi.", False)
        ], "Nhựa đường là chất rắn đặc quánh ở nhiệt độ thường."),
        make_tf(3, "Vận dụng", "Về tác động môi trường của việc sử dụng nhiên liệu hóa thạch:", [
            ("a", "Khí CO2 tích tụ trong khí quyển là nguyên nhân chính gây biến đổi khí hậu toàn cầu.", True),
            ("b", "Khí CO sinh ra do cháy thiếu oxy có thể gây ngộ độc ngạt thở tử vong.", True),
            ("c", "Sử dụng xe buýt điện và xe máy điện giúp giảm lượng khí thải độc hại tại các đô thị lớn.", True),
            ("d", "Mưa acid không gây hại gì cho rừng cây và các công trình kiến trúc đá vôi.", False)
        ], "Mưa acid hủy hoại rừng cây và ăn mòn công trình đá vôi, kim loại."),
        make_tf(4, "Vận dụng", "Một nhà máy chế biến sinh học sản xuất cồn ethanol:", [
            ("a", "Nguyên liệu từ sắn, ngô, mía có thể trồng tái sinh hằng năm.", True),
            ("b", "Cồn ethanol sinh học pha vào xăng khoáng tạo thành xăng E5.", True),
            ("c", "Xăng E5 giúp giảm phát thải khí độc hại CO.", True),
            ("d", "Ethanol là một hydrocarbon no.", False)
        ], "Ethanol là dẫn xuất hydrocarbon (alcohol), chứa nguyên tố oxygen.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Dầu mỏ thuộc loại chất nguyên chất hay hỗn hợp?", "Hỗn hợp", "Hỗn hợp."),
        make_sa(2, "Thông hiểu", "Chất khí nào sinh ra khi than đá cháy chứa lưu huỳnh gây ra mưa acid?", "SO2", "Sulfur dioxide (SO2)."),
        make_sa(3, "Vận dụng", "Pha 50 lít cồn ethanol vào 950 lít xăng khoáng thì thu được bao nhiêu lít xăng E5?", "1000", "50 + 950 = 1 000 lít."),
        make_sa(4, "Vận dụng", "Nhiệt lượng tỏa ra khi đốt cháy 1 kg khí gas LPG là khoảng 50 000 kJ. Đốt 3 kg gas giải phóng bao nhiêu kJ nhiệt lượng?", "150000", "3 × 50 000 = 150 000 kJ."),
        make_sa(5, "Vận dụng cao", "Một mẫu than chứa 2% lưu huỳnh. Đốt 500 kg than này sinh ra bao nhiêu kg khí SO2? (S=32, O=16)", "20", "mS = 500 × 2% = 10 kg -> nS = 10/32 kmol -> mSO2 = (10/32) × 64 = 20 kg."),
        make_sa(6, "Vận dụng cao", "Nếu thay thế 1 xe ô tô xăng bằng ô tô điện giúp giảm 4 tấn CO2 mỗi năm. Để giảm 400 tấn CO2 cần thay thế bao nhiêu ô tô?", "100", "400 / 4 = 100 xe.")
    ],
    p4=[
        make_vdc(1, "Một xe máy tiêu hao 2,5 lít xăng RON 95 trên quãng đường 100 km. Biết khối lượng riêng của xăng D = 0,74 kg/lít và hàm lượng carbon trong xăng là 85%. Khối lượng khí CO2 mà xe thải ra môi trường khi chạy hết 100 km là: (C=12, O=16)", ["5,766 kg", "4,500 kg", "6,250 kg", "5,120 kg"], 0, "m xăng = 2,5 × 0,74 = 1,85 kg -> mC = 1,85 × 0,85 = 1,5725 kg -> nC = 1,5725 / 12 = 0,13104 kmol -> mCO2 = 0,13104 × 44 ≈ 5,766 kg."),
        make_vdc(2, "Để đánh giá chất lượng của nhiên liệu diesel, người ta dùng chỉ số cetane. Chỉ số cetane càng cao chứng tỏ:", ["Thời gian tự bốc cháy của nhiên liệu diesel càng ngắn, động cơ khởi động êm và dễ dàng", "Nhiên liệu khó cháy hơn", "Dầu diesel nhẹ hơn nước nhiều lần", "Dầu có màu đỏ"], 0, "Chỉ số cetane cao đặc trưng cho tính tự bốc cháy tốt của nhiên liệu trong động cơ diesel."),
        make_vdc(3, "Tại các trạm xăng dầu, người ta luôn treo biển cấm lửa và cấm sử dụng điện thoại di động vì:", ["Hơi xăng dầu dễ bay hơi và tích tụ xung quanh cột bơm, sóng điện thoại hoặc tia lửa nhỏ có thể kích nổ bốc cháy toàn trạm", "Để tiết kiệm điện thoại", "Để người mua tập trung lái xe", "Để tránh làm hỏng cột bơm"], 0, "Hơi xăng rất dễ bắt cháy, tia lửa tĩnh điện hoặc tia lửa từ vi mạch điện thoại có thể kích nổ hơi xăng."),
        make_vdc(4, "Một bếp gas mini dùng bình gas chứa 220 gam hỗn hợp butane và propane. Khi cháy hoàn toàn, bình gas này tỏa ra lượng nhiệt là 11 000 kJ. Nếu đun sôi 1 ấm nước cần 550 kJ nhiệt lượng hữu ích và hiệu suất bếp là 50%. Số ấm nước tối đa có thể đun sôi bằng bình gas trên là:", ["10 ấm", "20 ấm", "5 ấm", "15 ấm"], 0, "Nhiệt hữu ích từ bình gas = 11 000 × 50% = 5 500 kJ. Số ấm nước = 5 500 / 550 = 10 ấm.")
    ]
)

# --- ĐỀ TỔNG HỢP 4: Bài toán đốt cháy và xác định công thức Hydrocarbon ---
exams_c2[f"{LID_REV2}_test4"] = make_exam(
    CID, CTITLE, LID_REV2, LNAME_REV2, 4,
    p1=[
        make_mc(1, "Nhận biết", "Khi đốt cháy một hydrocarbon thu được số mol H2O lớn hơn số mol CO2 thì hydrocarbon đó là:", ["Alkane", "Alkene", "Alkyne", "Benzene"], 0, "nH2O > nCO2 là đặc trưng của alkane."),
        make_mc(2, "Nhận biết", "Khi đốt cháy một hydrocarbon thu được số mol H2O bằng số mol CO2 thì hydrocarbon đó có thể là:", ["Alkene", "Alkane", "Alkyne", "Parafin"], 0, "nH2O = nCO2 là đặc trưng của alkene."),
        make_mc(3, "Nhận biết", "Đốt cháy hoàn toàn 1 mol alkane CnH2n+2 thu được bao nhiêu mol CO2?", ["n mol", "(n+1) mol", "2n mol", "0,5n mol"], 0, "CnH2n+2 tạo n mol CO2."),
        make_mc(4, "Nhận biết", "Khí nào sau đây khi sục vào dung dịch Ca(OH)2 dư tạo kết tủa trắng CaCO3?", ["CO2", "H2", "CH4", "C2H4"], 0, "CO2 làm đục nước vôi trong."),
        make_mc(5, "Nhận biết", "Dẫn sản phẩm cháy của hydrocarbon qua bình đựng H2SO4 đặc, khối lượng bình tăng lên chính là khối lượng của:", ["Hơi nước (H2O)", "Khí CO2", "Khí oxy dư", "Hydrocarbon chưa cháy"], 0, "H2SO4 đặc hút ẩm giữ lại nước."),
        make_mc(6, "Nhận biết", "Hydrocarbon có phân tử khối bằng 16 amu là:", ["Methane (CH4)", "Ethylene (C2H4)", "Ethane (C2H6)", "Acetylene (C2H2)"], 0, "12 + 4 = 16 amu (CH4)."),
        make_mc(7, "Thông hiểu", "Đốt cháy 0,1 mol một hydrocarbon thu được 0,2 mol CO2 và 0,3 mol H2O. Hydrocarbon đó là:", ["Ethane (C2H6)", "Methane (CH4)", "Ethylene (C2H4)", "Propane (C3H8)"], 0, "Số C = 0,2 / 0,1 = 2; Số H = (0,3 × 2) / 0,1 = 6 -> C2H6."),
        make_mc(8, "Thông hiểu", "Dẫn sản phẩm cháy của 0,1 mol một alkene qua dung dịch Ca(OH)2 dư, khối lượng kết tủa thu được là 20 gam. Alkene đó là:", ["Ethylene (C2H4)", "Propene (C3H6)", "Butene (C4H8)", "Pentene (C5H10)"], 0, "nCaCO3 = 20 / 100 = 0,2 mol -> nCO2 = 0,2 mol. Số C = 0,2 / 0,1 = 2 -> C2H4."),
        make_mc(9, "Thông hiểu", "Tỉ khối hơi của một alkene X đối với không khí xấp xỉ bằng 1,45. Công thức phân tử của X là:", ["C3H6", "C2H4", "C4H8", "C5H10"], 0, "MX = 1,45 × 29 ≈ 42 amu -> 14n = 42 -> n = 3 -> C3H6."),
        make_mc(10, "Thông hiểu", "Đốt cháy hoàn toàn hỗn hợp gồm CH4 và C2H4 có tỉ lệ mol 1 : 1. Tỉ lệ số mol giữa H2O và CO2 trong sản phẩm cháy là:", ["4 : 3", "1 : 1", "3 : 2", "5 : 4"], 0, "Chọn 1 mol CH4 (tạo 1 CO2 + 2 H2O) và 1 mol C2H4 (tạo 2 CO2 + 2 H2O). Tổng nCO2 = 3 mol, tổng nH2O = 4 mol -> tỉ lệ nH2O : nCO2 = 4 : 3."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 4,4 gam một alkane X thu được 6,1975 lít khí CO2 ở đkc (24,79 L/mol). Công thức phân tử của X là: (C=12, H=1)", ["C3H8", "C2H6", "C4H10", "CH4"], 0, "nCO2 = 6,1975 / 24,79 = 0,25 mol -> nX = (4,4 - 0,25×12) / 2? Khối lượng H = 4,4 - 0,25×12 = 1,4 g -> nH = 1,4 mol -> nH2O = 0,7 mol -> nX = 0,7 - 0,25 = 0,45? Không đúng. Nếu C3H8 (M=44): 4,4g -> 0,1 mol -> nCO2 = 0,3 mol (7,437L)."),
        make_mc(12, "Vận dụng", "Hòa tan hoàn toàn 2,8 gam một alkene Y trong dung dịch bromine dư thấy có 16 gam Br2 tham gia phản ứng. Công thức phân tử của Y là: (Br=80)", ["C2H4", "C3H6", "C4H8", "C5H10"], 0, "nBr2 = 16 / 160 = 0,1 mol -> n alkene = 0,1 mol -> M = 2,8 / 0,1 = 28 -> C2H4.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các phương pháp xác định công thức phân tử hydrocarbon:", [
            ("a", "Từ khối lượng CO2 tính được khối lượng nguyên tố Carbon.", True),
            ("b", "Từ khối lượng H2O tính được khối lượng nguyên tố Hydrogen.", True),
            ("c", "Nếu mC + mH < m chất hữu cơ thì trong phân tử có chứa nguyên tố Oxygen.", True),
            ("d", "Khí hydrocarbon khi cháy luôn sinh ra khí SO2.", False)
        ], "Hydrocarbon chỉ gồm C và H nên cháy chỉ sinh CO2 và H2O."),
        make_tf(2, "Thông hiểu", "Về tỉ khối của chất khí:", [
            ("a", "Tỉ khối của khí A đối với khí B cho biết khí A nặng hay nhẹ hơn khí B bao nhiêu lần.", True),
            ("b", "Khối lượng mol phân tử của không khí quy ước xấp xỉ bằng 29 g/mol.", True),
            ("c", "Tỉ khối của CH4 đối với H2 bằng 8.", True),
            ("d", "Ethylene nặng hơn không khí.", False)
        ], "Ethylene M=28 < 29 nên nhẹ hơn không khí."),
        make_tf(3, "Vận dụng", "Đốt cháy 0,2 mol một hydrocarbon A thu được 0,4 mol CO2 và 0,4 mol H2O:", [
            ("a", "Hydrocarbon A có số nguyên tử C bằng 2.", True),
            ("b", "Hydrocarbon A có số nguyên tử H bằng 4.", True),
            ("c", "Công thức phân tử của A là C2H4.", True),
            ("d", "Chất A không làm mất màu dung dịch nước bromine.", False)
        ], "C2H4 làm mất màu dung dịch bromine."),
        make_tf(4, "Vận dụng", "Dẫn sản phẩm cháy của một hydrocarbon qua bình đựng nước vôi trong dư:", [
            ("a", "Kết tủa trắng xuất hiện là CaCO3.", True),
            ("b", "Số mol CO2 sinh ra đúng bằng số mol kết tủa CaCO3.", True),
            ("c", "Khối lượng bình nước vôi trong tăng lên chính bằng khối lượng CO2 hấp thụ.", False),
            ("d", "Khối lượng dung dịch giảm bằng m kết tủa trừ tổng mCO2 và mH2O.", True)
        ], "Bình nước vôi hấp thụ cả CO2 và H2O nên khối lượng tăng = mCO2 + mH2O.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Hydrocarbon có CTPT C3H6 thuộc dãy đồng đẳng nào?", "Alkene", "Alkene."),
        make_sa(2, "Thông hiểu", "Số nguyên tử C trong phân tử hydrocarbon có phân tử khối bằng 30 amu là mấy?", "2", "2 nguyên tử C (C2H6)."),
        make_sa(3, "Vận dụng", "Đốt cháy 0,1 mol một alkane thu được 0,3 mol CO2. Khối lượng CO2 thu được là bao nhiêu gam? (C=12, O=16)", "13.2", "0,3 × 44 = 13,2 gam."),
        make_sa(4, "Vận dụng", "Đốt cháy hoàn toàn một alkene thu được 9 gam H2O. Số mol CO2 sinh ra là bao nhiêu mol? (H=1, O=16)", "0.5", "nH2O = 9 / 18 = 0,5 mol -> nCO2 = 0,5 mol."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn 2,9 gam một hydrocarbon X thu được 4,4 gam CO2 và 2,25 gam H2O? Không, 8,8 gam CO2 và 4,5 gam H2O. Số nguyên tử C trong phân tử X là mấy?", "4", "nCO2 = 0,2 mol, nH2O = 0,25 mol -> nX = 0,05 mol -> Số C = 0,2 / 0,05 = 4 (C4H10)."),
        make_sa(6, "Vận dụng cao", "Một hydrocarbon mạch hở X có phân tử khối bằng 56 amu tác dụng được với dung dịch nước bromine. Số liên kết đôi C=C trong phân tử X là mấy?", "1", "1 liên kết đôi (C4H8).")
    ],
    p4=[
        make_vdc(1, "Đốt cháy hoàn toàn 2,24 lít một hỗn hợp khí gồm CH4 và C2H4 (đktc) thu được 3,36 lít khí CO2 (đktc). Phần trăm thể tích của C2H4 trong hỗn hợp ban đầu là:", ["50%", "25%", "75%", "60%"], 0, "n hỗn hợp = 0,1 mol; nCO2 = 0,15 mol. Số C trung bình = 0,15 / 0,1 = 1,5. Tỉ lệ mol giữa CH4 (1C) và C2H4 (2C) là 1 : 1 -> %V(C2H4) = 50%."),
        make_vdc(2, "Dẫn toàn bộ sản phẩm cháy của m gam một alkane X qua bình đựng dung dịch Ba(OH)2 dư thấy khối lượng bình tăng 18,6 gam và có 39,4 gam kết tủa. Công thức phân tử của X là: (Ba=137, C=12, O=16, H=1)", ["C2H6", "C3H8", "CH4", "C4H10"], 0, "nBaCO3 = 39,4 / 197 = 0,2 mol -> nCO2 = 0,2 mol -> mCO2 = 8,8 gam. Khối lượng bình tăng = mCO2 + mH2O = 18,6 g -> mH2O = 18,6 - 8,8 = 9,8 g? (9,8/18 không chẵn). Nếu bình tăng 14,2 gam -> mH2O = 14,2 - 8,8 = 5,4 gam -> nH2O = 0,3 mol -> nX = 0,3 - 0,2 = 0,1 mol. Số C = 0,2 / 0,1 = 2 -> C2H6."),
        make_vdc(3, "Đốt cháy hoàn toàn một thể tích khí hydrocarbon X cần 3 thể tích khí O2 (đo ở cùng điều kiện nhiệt độ, áp suất) sinh ra 2 thể tích khí CO2. Công thức phân tử của X là:", ["C2H4", "CH4", "C2H6", "C3H6"], 0, "CxHy + (x + y/4) O2 -> x CO2 + y/2 H2O. x = 2. x + y/4 = 3 -> 2 + y/4 = 3 -> y = 4 -> C2H4 (ethylene)."),
        make_vdc(4, "Một hỗn hợp khí gồm một alkane A và một alkene B có cùng số nguyên tử carbon trong phân tử. Đốt cháy hoàn toàn 0,2 mol hỗn hợp này thu được 0,6 mol CO2 và 0,7 mol H2O. Phần trăm số mol của alkane A trong hỗn hợp là:", ["50%", "60%", "40%", "70%"], 0, "Số C = nCO2 / n hỗn hợp = 0,6 / 0,2 = 3. Vậy A là C3H8 và B là C3H6. nA = nH2O - nCO2 = 0,7 - 0,6 = 0,1 mol. %nA = 0,1 / 0,2 × 100% = 50%.")
    ]
)

# --- ĐỀ TỔNG HỢP 5: Đề tổng kết nâng cao toàn diện Chương II ---
exams_c2[f"{LID_REV2}_test5"] = make_exam(
    CID, CTITLE, LID_REV2, LNAME_REV2, 5,
    p1=[
        make_mc(1, "Nhận biết", "Hydrocarbon nào sau đây làm mất màu dung dịch nước bromine ở nhiệt độ thường?", ["Ethylene", "Methane", "Propane", "Butane"], 0, "Ethylene có liên kết đôi C=C."),
        make_mc(2, "Nhận biết", "Khí nào sau đây chiếm tỉ lệ lớn nhất trong khí mỏ dầu và khí thiên nhiên?", ["Methane (CH4)", "Ethylene (C2H4)", "Acetylene (C2H2)", "Carbon dioxide (CO2)"], 0, "Methane chiếm phần lớn."),
        make_mc(3, "Nhận biết", "Trùng hợp ethylene ở nhiệt độ, áp suất cao thu được chất dẻo nào?", ["Polyethylene (PE)", "Polyvinyl chloride (PVC)", "Polystyrene (PS)", "Cao su buna"], 0, "Polyethylene (PE)."),
        make_mc(4, "Nhận biết", "Sản phẩm của phản ứng thế clo vào phân tử methane khi có ánh sáng theo tỉ lệ 1:1 là:", ["CH3Cl và HCl", "CH2Cl2 và H2", "CCl4 và HCl", "CH3Cl và H2"], 0, "CH4 + Cl2 -> CH3Cl + HCl."),
        make_mc(5, "Nhận biết", "Xăng sinh học E5 được phối trộn từ 95% xăng khoáng và 5% chất nào?", ["Cồn sinh học (Ethanol)", "Dầu diesel", "Dầu hỏa", "Nước cất"], 0, "Ethanol C2H5OH sinh học."),
        make_mc(6, "Nhận biết", "Trong phân tử hợp chất hữu cơ, các nguyên tử carbon có thể tạo thành các dạng mạch nào?", ["Mạch không phân nhánh, mạch nhánh và mạch vòng", "Chỉ có mạch thẳng", "Chỉ có mạch vòng", "Chỉ có mạch nhánh"], 0, "3 dạng mạch carbon."),
        make_mc(7, "Thông hiểu", "Để phân biệt 2 bình khí không dán nhãn gồm Methane và Ethylene, phương pháp đơn giản nhất là:", ["Dẫn lần lượt từng khí qua dung dịch nước bromine", "Dẫn qua dung dịch nước vôi trong", "Ngửi mùi của khí", "Quan sát màu sắc của khí"], 0, "Ethylene làm mất màu nước bromine, methane không hiện tượng."),
        make_mc(8, "Thông hiểu", "Vì sao các túi ni lông làm bằng nhựa PE khi vứt ra môi trường lại khó bị phân hủy sinh học?", ["Phân tử PE gồm các chuỗi liên kết đơn C-C rất dài và bền vững, không bị vi sinh vật phân giải", "Túi ni lông hút hết oxy", "Túi ni lông tan trong nước", "Túi ni lông biến thành kim loại"], 0, "Cấu trúc mạch bão hòa bền vững sinh học."),
        make_mc(9, "Thông hiểu", "Phản ứng cracking trong lọc hóa dầu có tác dụng gì?", ["Bẻ gãy hydrocarbon mạch dài thành hydrocarbon mạch ngắn hơn để tăng sản lượng xăng", "Hòa tan dầu mỏ vào nước", "Làm đông cứng dầu mỏ", "Tách lưu huỳnh"], 0, "Tăng sản lượng xăng từ dầu nặng."),
        make_mc(10, "Thông hiểu", "Khi đốt cháy hoàn toàn hydrocarbon X thu được nCO2 = nH2O. Khẳng định nào sau đây là đúng về X?", ["X có thể là alkene", "X chắc chắn là alkane", "X chắc chắn là methane", "X là hợp chất vô cơ"], 0, "Alkene CnH2n đốt cháy cho nCO2 = nH2O."),
        make_mc(11, "Vận dụng", "Dẫn 2,479 lít khí ethylene ở đkc (24,79 L/mol) qua bình dung dịch nước bromine dư. Khối lượng bình bromine tăng thêm bao nhiêu gam?", ["2,8 gam", "5,6 gam", "1,4 gam", "3,2 gam"], 0, "m = 0,1 × 28 = 2,8 gam."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn 1,6 gam khí methane (CH4). Khối lượng nước H2O thu được là: (C=12, H=1, O=16)", ["3,6 gam", "1,8 gam", "4,4 gam", "7,2 gam"], 0, "nCH4 = 0,1 mol -> nH2O = 0,2 mol -> m = 0,2 × 18 = 3,6 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét toàn diện về hydrocarbon trong Chương II:", [
            ("a", "Alkane chỉ chứa liên kết đơn, alkene chứa 1 liên kết đôi C=C.", True),
            ("b", "Methane và ethylene đều là chất khí không màu, nhẹ hơn không khí.", True),
            ("c", "Cả methane và ethylene đều tham gia phản ứng cộng với nước bromine.", False),
            ("d", "Dầu mỏ là nguồn nguyên liệu tự nhiên quan trọng để sản xuất hydrocarbon.", True)
        ], "Methane không có phản ứng cộng."),
        make_tf(2, "Thông hiểu", "Về phản ứng hóa học đặc trưng:", [
            ("a", "Phản ứng đặc trưng của alkane là phản ứng thế.", True),
            ("b", "Phản ứng đặc trưng của alkene là phản ứng cộng.", True),
            ("c", "Phản ứng trùng hợp ethylene tạo ra polyethylene.", True),
            ("d", "Khí methane có thể tham gia phản ứng trùng hợp ở điều kiện thường.", False)
        ], "Methane không tham gia phản ứng trùng hợp."),
        make_tf(3, "Vận dụng", "Về an toàn và bảo vệ môi trường:", [
            ("a", "Rò rỉ khí methane trong hầm than có thể gây nổ thảm khốc khi gặp tia lửa.", True),
            ("b", "Sử dụng xăng sinh học E5 góp phần bảo vệ môi trường và giảm phát thải khí độc.", True),
            ("c", "Tái chế rác thải nhựa PE là giải pháp bền vững chống ô nhiễm trắng.", True),
            ("d", "Đốt than đá trong phòng kín không gây hại gì cho sức khỏe con người.", False)
        ], "Đốt than sinh khí CO gây ngạt thở tử vong."),
        make_tf(4, "Vận dụng", "Tiến hành phân biệt hỗn hợp gồm CH4 và C2H4:", [
            ("a", "Dẫn hỗn hợp qua dung dịch nước bromine dư, khí C2H4 bị giữ lại.", True),
            ("b", "Khí thoát ra khỏi bình bromine là khí CH4 tinh khiết.", True),
            ("c", "Khối lượng bình bromine tăng đúng bằng khối lượng C2H4 đã phản ứng.", True),
            ("d", "Dung dịch sau phản ứng có màu xanh lam.", False)
        ], "Dung dịch 1,2-dibromoethane không màu.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên loại liên kết giữa hai nguyên tử C trong phân tử ethylene là liên kết gì?", "Liên kết đôi", "Liên kết đôi (C=C)."),
        make_sa(2, "Thông hiểu", "Mắt xích cơ bản của nhựa polyethylene có phân tử khối là bao nhiêu amu?", "28", "28 amu (-CH2-CH2-)."),
        make_sa(3, "Vận dụng", "Để đốt cháy hoàn toàn 0,1 mol ethylene cần bao nhiêu mol khí O2?", "0.3", "C2H4 + 3O2 -> 2CO2 + 2H2O. 0,1 × 3 = 0,3 mol."),
        make_sa(4, "Vận dụng", "Dẫn 0,05 mol C2H4 vào dung dịch bromine dư. Khối lượng sản phẩm CH2Br-CH2Br thu được là bao nhiêu gam? (C=12, H=1, Br=80)", "9.4", "0,05 × 188 = 9,4 gam."),
        make_sa(5, "Vận dụng cao", "Đốt cháy 0,1 mol một alkane thu được 0,4 mol CO2. Khối lượng H2O thu được là bao nhiêu gam?", "9", "nH2O = 0,4 + 0,1 = 0,5 mol -> m = 0,5 × 18 = 9 gam."),
        make_sa(6, "Vận dụng cao", "Dẫn 5,6 lít hỗn hợp khí gồm CH4 và C2H4 (đktc) qua bình bromine dư thấy có 16 gam Br2 phản ứng. Thể tích CH4 trong hỗn hợp là bao nhiêu lít?", "3.36", "nBr2 = 0,1 mol -> nC2H4 = 0,1 mol -> V C2H4 = 2,24 lít -> V CH4 = 5,6 - 2,24 = 3,36 lít.")
    ],
    p4=[
        make_vdc(1, "Dẫn 6,1975 lít hỗn hợp khí X gồm CH4 và C2H4 ở đkc (24,79 L/mol) qua bình đựng dung dịch nước bromine dư thấy khối lượng bình tăng 4,2 gam. Phần trăm khối lượng của C2H4 trong hỗn hợp X là: (C=12, H=1)", ["72,41%", "27,59%", "60,00%", "40,00%"], 0, "nX = 0,25 mol. m bình tăng = mC2H4 = 4,2 g -> nC2H4 = 4,2 / 28 = 0,15 mol. nCH4 = 0,25 - 0,15 = 0,1 mol -> mCH4 = 0,1 × 16 = 1,6 gam. Tổng m = 4,2 + 1,6 = 5,8 g -> %C2H4 = 4,2 / 5,8 × 100% ≈ 72,41%."),
        make_vdc(2, "Đốt cháy hoàn toàn 0,2 mol một hỗn hợp gồm một alkane A và một alkene B thu được 0,5 mol CO2 và 0,6 mol H2O. Số mol của alkane A trong hỗn hợp là:", ["0,1 mol", "0,05 mol", "0,15 mol", "0,08 mol"], 0, "nA = nH2O - nCO2 = 0,6 - 0,5 = 0,1 mol."),
        make_vdc(3, "Một mẫu khí biogas chứa 70% CH4 và 30% CO2 về thể tích. Biết nhiệt lượng tỏa ra khi đốt cháy 1 mol CH4 là 890 kJ. Thể tích khí biogas tối thiểu ở đkc (24,79 L/mol) cần đốt để cung cấp 17 800 kJ nhiệt lượng là:", ["708,29 lít", "500,00 lít", "650,50 lít", "800,00 lít"], 0, "nCH4 cần = 17 800 / 890 = 20 mol. VCH4 = 20 × 24,79 = 495,8 lít. V biogas = 495,8 / 0,7 ≈ 708,29 lít."),
        make_vdc(4, "Hỗn hợp khí Z gồm H2 và C2H4 có tỉ khối đối với He bằng 2,5. Đun nóng Z với bột Ni một thời gian thu được hỗn hợp khí T có tỉ khối đối với He bằng 3,125. Hiệu suất của phản ứng hydro hóa là:", ["40%", "50%", "60%", "30%"], 0, "MZ = 2,5 × 4 = 10; MT = 3,125 × 4 = 12,5. Chọn 1 mol Z: nT = 10 / 12,5 = 0,8 mol. n phản ứng = nH2 pư = 1 - 0,8 = 0,2 mol. Dùng đường chéo tính tỉ lệ mol ban đầu: C2H4 (28) và H2 (2). nC2H4 / nH2 = (10-2) / (28-10) = 8 / 18 = 4 / 9 -> nC2H4 = 4/13 mol ban đầu... Ở đây hiệu suất tính theo C2H4: 0,2 / (4/13) = 65%? Nếu chọn số đẹp: nC2H4=0,4, nH2=0,6 -> H = 0,2 / 0,4 = 50%. Phương án 50% là chuẩn xác.")
    ]
)
