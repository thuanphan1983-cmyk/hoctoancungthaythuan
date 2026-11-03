# -*- coding: utf-8 -*-
"""
BUILDER HÓA HỌC 9 - CHƯƠNG III: ETHYLIC ALCOHOL VÀ ACETIC ACID (11 ĐỀ ĐỘC LẬP 100%)
Gồm 2 bài học (3 đề/bài = 6 đề) và 1 bài ôn tập cuối chương (5 đề) = 11 đề.
Không trùng lặp câu hỏi, số liệu và đáp án giữa các đề trong cùng bài học.
"""

from chem9_helpers import make_mc, make_tf, make_sa, make_vdc, make_exam

exams_c3 = {}

CID = "chem9_c3"
CTITLE = "Chương III: Ethylic alcohol và Acetic acid"

# ==============================================================================
# BÀI 9: ETHYLIC ALCOHOL (chem9_c3_b9) - 3 ĐỀ
# ==============================================================================
LID_B9 = "chem9_c3_b9"
LNAME_B9 = "Bài 9: Ethylic alcohol"

# --- BÀI 9 - ĐỀ 1: Cấu tạo phân tử, tính chất vật lí và độ cồn ---
exams_c3[f"{LID_B9}_test1"] = make_exam(
    CID, CTITLE, LID_B9, LNAME_B9, 1,
    p1=[
        make_mc(1, "Nhận biết", "Công thức phân tử của ethylic alcohol (rượu etylic) là:", ["C2H6O", "C2H4O2", "CH4O", "C3H8O"], 0, "Ethylic alcohol có CTPT là C2H6O."),
        make_mc(2, "Nhận biết", "Công thức cấu tạo thu gọn của ethylic alcohol là:", ["CH3-CH2-OH", "CH3-O-CH3", "CH3-COOH", "CH3-CHO"], 0, "CH3-CH2-OH (chứa nhóm chức alcohol -OH)."),
        make_mc(3, "Nhận biết", "Nhóm nguyên tử nào quyết định tính chất hóa học đặc trưng của ethylic alcohol?", ["Nhóm hydroxy (-OH)", "Nhóm methyl (-CH3)", "Nhóm carboxyl (-COOH)", "Nhóm carbonyl (-C=O)"], 0, "Nhóm -OH quyết định tính chất của rượu."),
        make_mc(4, "Nhận biết", "Ở điều kiện thường, ethylic alcohol là chất gì?", ["Chất lỏng không màu, mùi thơm đặc trưng, vị cay, tan vô hạn trong nước", "Chất khí màu vàng nhạt", "Chất rắn màu trắng kết tinh", "Chất lỏng màu xanh không tan trong nước"], 0, "Ethylic alcohol là chất lỏng không màu, nhẹ hơn nước, tan vô hạn trong nước."),
        make_mc(5, "Nhận biết", "Nhiệt độ sôi của ethylic alcohol nguyên chất ở áp suất khí quyển khoảng:", ["78,3 °C", "100 °C", "118 °C", "35 °C"], 0, "Nhiệt độ sôi của ethylic alcohol là 78,3 °C."),
        make_mc(6, "Nhận biết", "Độ cồn (độ rượu) là gì?", ["Số mililít ethylic alcohol nguyên chất có trong 100 mililít dung dịch rượu", "Số gam rượu trong 100 gam dung dịch", "Phần trăm khối lượng của rượu", "Nhiệt độ sôi của rượu"], 0, "Định nghĩa độ cồn: số mL rượu nguyên chất trong 100 mL dung dịch hỗn hợp với nước."),
        make_mc(7, "Thông hiểu", "Trên nhãn chai rượu vang có ghi '12°'. Con số này có ý nghĩa là:", ["Trong 100 mL rượu vang đó có chứa 12 mL ethylic alcohol nguyên chất", "Chai rượu nặng 12 kg", "Rượu sôi ở 12 °C", "Trong 100 gam rượu có 12 gam cồn"], 0, "Rượu 12° chứa 12 mL rượu nguyên chất trong 100 mL dung dịch."),
        make_mc(8, "Thông hiểu", "Vì sao cồn y tế 70° lại có tác dụng sát trùng, diệt khuẩn tối ưu hơn cồn 90°?", ["Cồn 70° thấm sâu vào tế bào vi khuẩn làm đông tụ protein từ từ, trong khi cồn 90° làm protein bề mặt đông tụ quá nhanh tạo màng cản ngăn cồn thấm vào trong", "Cồn 70° độc hơn cồn 90°", "Cồn 90° bay hơi tạo độc tố", "Cồn 70° chứa nhiều vitamin"], 0, "Cồn 70° duy trì độ ẩm vừa đủ để cồn ngấm sâu tiêu diệt triệt để vi khuẩn."),
        make_mc(9, "Thông hiểu", "Khối lượng riêng của ethylic alcohol nguyên chất ở 20 °C xấp xỉ bằng:", ["0,8 g/mL", "1,0 g/mL", "1,2 g/mL", "0,5 g/mL"], 0, "D của cồn nguyên chất ≈ 0,8 g/mL (nhẹ hơn nước)."),
        make_mc(10, "Thông hiểu", "Để pha được 200 mL cồn 45° từ cồn nguyên chất và nước cất, thể tích cồn nguyên chất cần lấy là:", ["90 mL", "45 mL", "100 mL", "135 mL"], 0, "Vrượu = (200 × 45) / 100 = 90 mL."),
        make_mc(11, "Vận dụng", "Khối lượng của 50 mL ethylic alcohol nguyên chất (biết D = 0,8 g/mL) là:", ["40 gam", "50 gam", "62,5 gam", "45 gam"], 0, "m = V × D = 50 × 0,8 = 40 gam."),
        make_mc(12, "Vận dụng", "Trong 500 mL dung dịch rượu 40° có chứa bao nhiêu gam ethylic alcohol nguyên chất? (D = 0,8 g/mL)", ["160 gam", "200 gam", "250 gam", "180 gam"], 0, "Vrượu = (500 × 40) / 100 = 200 mL -> m = 200 × 0,8 = 160 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất vật lí của ethylic alcohol:", [
            ("a", "Ethylic alcohol nhẹ hơn nước và tan vô hạn trong nước ở mọi tỉ lệ.", True),
            ("b", "Nhiệt độ sôi của ethylic alcohol (78,3 °C) thấp hơn nhiệt độ sôi của nước (100 °C).", True),
            ("c", "Ethylic alcohol có thể hòa tan được nhiều chất như iodine, benzene, dầu mỡ, hương liệu...", True),
            ("d", "Khi trộn 50 mL cồn nguyên chất với 50 mL nước cất thu được đúng 100 mL dung dịch.", False)
        ], "Có sự co ngót thể tích do lực hút phân tử nên thể tích hỗn hợp < 100 mL."),
        make_tf(2, "Thông hiểu", "Về khái niệm độ cồn và ứng dụng y tế:", [
            ("a", "Rượu 45° nghĩa là trong 100 gam dung dịch rượu có 45 gam rượu nguyên chất.", False),
            ("b", "Độ cồn biểu thị phần trăm thể tích của ethylic alcohol nguyên chất trong dung dịch.", True),
            ("c", "Cồn y tế sát trùng hiệu quả nhất là cồn có nồng độ khoảng 70°.", True),
            ("d", "Dung dịch cồn trong nước có thể phân tách bằng phương pháp chưng cất đơn giản nhờ nhiệt độ sôi khác nhau.", True)
        ], "Độ cồn tính theo mL thể tích, không tính theo gam khối lượng."),
        make_tf(3, "Vận dụng", "Một cơ sở pha chế cồn sát trùng y tế 70°:", [
            ("a", "Lấy 700 mL cồn 96° thêm nước cất cho vừa đủ 1 000 mL sẽ thu được cồn 70°.", False),
            ("b", "Để có 700 mL cồn nguyên chất cần dùng 700 / 0,96 ≈ 729,2 mL cồn 96° rồi thêm nước tới vạch 1 lít.", True),
            ("c", "Cồn 70° dùng để sát khuẩn tay nhanh và khử trùng bề mặt dụng cụ.", True),
            ("d", "Cồn sát trùng có thể uống thay rượu vang mà không gây hại.", False)
        ], "Cồn y tế chứa phụ gia và nồng độ cồn rất cao gây bỏng thực quản và ngộ độc nghiêm trọng."),
        make_tf(4, "Vận dụng", "Về cấu tạo hóa học của ethylic alcohol:", [
            ("a", "Công thức phân tử C2H6O có 2 đồng phân cấu tạo: ethylic alcohol và dimethyl ether.", True),
            ("b", "Trong phân tử ethylic alcohol có 1 nguyên tử H liên kết trực tiếp với nguyên tử O tạo nhóm -OH.", True),
            ("c", "Nguyên tử H trong nhóm -OH linh động hơn các nguyên tử H liên kết với carbon.", True),
            ("d", "Dimethyl ether cũng có nhóm -OH tương tự như ethylic alcohol.", False)
        ], "Dimethyl ether có công thức CH3-O-CH3 không chứa nhóm -OH.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Số mililít ethylic alcohol nguyên chất có trong 100 mL dung dịch rượu gọi là gì?", "Độ cồn", "Độ cồn (độ rượu)."),
        make_sa(2, "Thông hiểu", "Nồng độ độ cồn tối ưu của cồn y tế dùng để sát trùng diệt khuẩn là bao nhiêu độ?", "70", "70° (hoặc 70 độ)."),
        make_sa(3, "Vận dụng", "Một chai rượu nếp 500 mL có độ cồn 40°. Thể tích rượu nguyên chất trong chai là bao nhiêu mL?", "200", "500 × 40% = 200 mL."),
        make_sa(4, "Vận dụng", "Pha 60 mL ethylic alcohol nguyên chất vào nước cất để thu được 200 mL dung dịch rượu. Độ cồn của dung dịch thu được là bao nhiêu độ?", "30", "60 / 200 × 100 = 30°."),
        make_sa(5, "Vận dụng cao", "Tính khối lượng của 250 mL cồn 96° biết khối lượng riêng của cồn nguyên chất là 0,8 g/mL? (Bỏ qua khối lượng nước, chỉ tính cồn nguyên chất)", "192", "Vrượu = 250 × 96% = 240 mL -> m = 240 × 0,8 = 192 gam."),
        make_sa(6, "Vận dụng cao", "Cần bao nhiêu mL cồn nguyên chất để pha thành 500 mL dung dịch rượu 45°?", "225", "500 × 45% = 225 mL.")
    ],
    p4=[
        make_vdc(1, "Một người uống 2 lon bia (mỗi lon dung tích 330 mL có nồng độ cồn 5%). Biết khối lượng riêng của cồn là 0,8 g/mL và khoảng 10% lượng cồn hấp thụ sẽ được bài tiết qua hơi thở và mồ hôi, 90% còn lại chuyển hóa tại gan. Tổng khối lượng ethylic alcohol nguyên chất người đó đã nạp vào cơ thể là:", ["26,4 gam", "33,0 gam", "16,5 gam", "21,1 gam"], 0, "Tổng V cồn = 2 × 330 × 5% = 33 mL -> m cồn = 33 × 0,8 = 26,4 gam."),
        make_vdc(2, "Để pha được 1 lít cồn y tế 70° từ cồn 90° và nước cất thì thể tích cồn 90° cần dùng là bao nhiêu? (Coi thể tích dung dịch không bị co ngót khi pha trộn)", ["777,8 mL", "700,0 mL", "850,0 mL", "630,0 mL"], 0, "Lượng cồn nguyên chất cần = 1 000 mL × 70% = 700 mL -> V cồn 90° = 700 / 0,9 ≈ 777,78 mL ≈ 777,8 mL."),
        make_vdc(3, "Tại sao khi kiểm tra nồng độ cồn của người lái xe, cảnh sát giao thông chỉ cần cho tài xế thổi hơi vào máy đo nồng độ cồn mà không bắt buộc phải lấy máu ngay lập tức?", ["Nồng độ cồn trong khí phế nang hơi thở luôn tỉ lệ thuận trực tiếp với nồng độ cồn trong máu theo tỉ lệ sinh học xác định", "Máy đo tự tạo ra cồn", "Hơi thở chứa nhiều cồn hơn trong máu", "Do máu không chứa cồn"], 0, "Tỉ lệ phân bố cồn giữa máu và khí phế nang trong phổi là tỉ lệ cố định (khoảng 2100:1) nên đo hơi thở phản ánh chính xác nồng độ cồn trong máu."),
        make_vdc(4, "Một dung dịch rượu X có độ cồn 92°. Biết khối lượng riêng của cồn nguyên chất là D1 = 0,8 g/mL và của nước là D2 = 1,0 g/mL (giả thiết thể tích dung dịch bằng tổng thể tích các chất thành phần). Khối lượng riêng của dung dịch rượu X là:", ["0,816 g/mL", "0,850 g/mL", "0,900 g/mL", "0,920 g/mL"], 0, "Xét 100 mL dung dịch rượu X: chứa 92 mL cồn và 8 mL nước. mdd = 92 × 0,8 + 8 × 1,0 = 73,6 + 8 = 81,6 gam -> Ddd = 81,6 / 100 = 0,816 g/mL.")
    ]
)

# --- BÀI 9 - ĐỀ 2: Tính chất hóa học của Ethylic alcohol ---
exams_c3[f"{LID_B9}_test2"] = make_exam(
    CID, CTITLE, LID_B9, LNAME_B9, 2,
    p1=[
        make_mc(1, "Nhận biết", "Khi cho mẩu kim loại natri (Na) vào ống nghiệm đựng ethylic alcohol nguyên chất, hiện tượng quan sát được là:", ["Có bọt khí không màu thoát ra đều đặn, mẩu natri tan dần", "Natri chìm xuống đáy và bốc cháy nổ dữ dội", "Dung dịch xuất hiện kết tủa màu nâu đỏ", "Không có hiện tượng gì"], 0, "2C2H5OH + 2Na -> 2C2H5ONa + H2. Phản ứng êm dịu hơn nhiều so với phản ứng của Na với nước."),
        make_mc(2, "Nhận biết", "Khí thoát ra trong phản ứng giữa ethylic alcohol và natri là khí nào?", ["Khí hydrogen (H2)", "Khí oxygen (O2)", "Khí carbon dioxide (CO2)", "Khí methane (CH4)"], 0, "Khí H2 thoát ra."),
        make_mc(3, "Nhận biết", "Sản phẩm muối hữu cơ tạo thành khi cho natri phản ứng với ethylic alcohol có tên là:", ["Sodium ethoxide (C2H5ONa)", "Sodium acetate (CH3COONa)", "Sodium formate (HCOONa)", "Sodium carbonate (Na2CO3)"], 0, "C2H5ONa có tên là sodium ethoxide."),
        make_mc(4, "Nhận biết", "Phương trình hóa học nào sau đây biểu diễn phản ứng cháy hoàn toàn của ethylic alcohol?", ["C2H5OH + 3O2 -> 2CO2 + 3H2O", "C2H5OH + O2 -> CH3COOH + H2O", "2C2H5OH + O2 -> 2CH3CHO + 2H2O", "C2H5OH + 2O2 -> 2CO + 3H2O"], 0, "C2H5OH + 3O2 --t°--> 2CO2 + 3H2O (tỏa nhiều nhiệt)."),
        make_mc(5, "Nhận biết", "Khi nhúng mẩu giấy quỳ tím vào dung dịch ethylic alcohol nguyên chất, hiện tượng quan sát được là:", ["Quỳ tím không đổi màu", "Quỳ tím hóa đỏ", "Quỳ tím hóa xanh", "Quỳ tím mất màu hoàn toàn"], 0, "Ethylic alcohol trung tính, không làm đổi màu quỳ tím."),
        make_mc(6, "Nhận biết", "Chất nào sau đây KHÔNG phản ứng với ethylic alcohol?", ["Dung dịch kiềm NaOH", "Kim loại natri (Na)", "Kim loại kali (K)", "Khí oxy khi đốt nóng"], 0, "Alcohol không có tính acid nên không phản ứng với dung dịch kiềm NaOH."),
        make_mc(7, "Thông hiểu", "Vì sao mẩu natri phản ứng với nước mãnh liệt hơn nhiều so với phản ứng với ethylic alcohol?", ["Liên kết O-H trong phân tử nước phân cực mạnh hơn liên kết O-H trong phân tử rượu nên nguyên tử H trong nước linh động hơn", "Vì nước nặng hơn rượu", "Vì rượu có màu", "Vì natri sợ rượu"], 0, "Nguyên tử H trong H-OH linh động hơn nguyên tử H trong C2H5-OH."),
        make_mc(8, "Thông hiểu", "Khi để rượu nhạt (dung dịch ethylic alcohol khoảng 6 - 8°) tiếp xúc lâu ngoài không khí có men giấm, rượu sẽ bị chua và biến đổi thành chất nào?", ["Acetic acid (CH3COOH)", "Carbonic acid (H2CO3)", "Lactic acid", "Glucose"], 0, "Men giấm oxy hóa ethylic alcohol thành acetic acid: C2H5OH + O2 --(men giấm)--> CH3COOH + H2O."),
        make_mc(9, "Thông hiểu", "Đèn cồn trong phòng thí nghiệm cháy tạo ra ngọn lửa màu gì và có khói muội đen hay không?", ["Ngọn lửa màu xanh mờ, hầu như không có khói muội than", "Ngọn lửa màu vàng cam với khói đen mù mịt", "Ngọn lửa màu đỏ tím", "Ngọn lửa phát nổ liên tục"], 0, "Cồn cháy rất sạch tạo ngọn lửa xanh nhạt tỏa nhiệt lớn, không sinh muội than."),
        make_mc(10, "Thông hiểu", "Cho mẩu kim loại Na vào cốc đựng dung dịch rượu 45° (hỗn hợp rượu và nước), natri sẽ phản ứng với chất nào trước?", ["Natri phản ứng đồng thời với cả nước và ethylic alcohol giải phóng H2", "Chỉ phản ứng với cồn, không phản ứng với nước", "Chỉ phản ứng với nước, không phản ứng với cồn", "Không phản ứng với chất nào"], 0, "Na phản ứng với cả H2O và C2H5OH sinh ra NaOH, C2H5ONa và khí H2."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 9,2 gam ethylic alcohol (C2H6O). Thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là: (C=12, H=1, O=16)", ["9,916 lít", "4,958 lít", "7,437 lít", "12,395 lít"], 0, "nC2H5OH = 9,2 / 46 = 0,2 mol -> nCO2 = 0,4 mol -> V = 0,4 × 24,79 = 9,916 lít."),
        make_mc(12, "Vận dụng", "Cho 0,2 mol ethylic alcohol nguyên chất tác dụng hoàn toàn với lượng dư kim loại natri. Thể tích khí H2 sinh ra ở điều kiện chuẩn (24,79 L/mol) là:", ["2,479 lít", "4,958 lít", "1,2395 lít", "3,7185 lít"], 0, "2C2H5OH -> H2. nH2 = 0,2 / 2 = 0,1 mol -> V = 0,1 × 24,79 = 2,479 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét phản ứng của ethylic alcohol với kim loại kiềm:", [
            ("a", "Ethylic alcohol phản ứng được với kim loại Na và K giải phóng khí H2.", True),
            ("b", "Chỉ có nguyên tử H trong nhóm -OH bị thay thế bởi nguyên tử kim loại Na.", True),
            ("c", "Các nguyên tử H trong gốc -C2H5 tham gia phản ứng thế tạo hợp chất C2Na5ONa.", False),
            ("d", "Phản ứng giữa ethylic alcohol nguyên chất và natri xảy ra chậm hơn phản ứng của natri với nước.", True)
        ], "Chỉ có H trong nhóm -OH phản ứng thế với Na."),
        make_tf(2, "Thông hiểu", "Về phản ứng oxy hóa ethylic alcohol:", [
            ("a", "Đốt cháy hoàn toàn ethylic alcohol tạo thành CO2 và H2O.", True),
            ("b", "Khi ethylic alcohol cháy, số mol H2O sinh ra luôn lớn hơn số mol CO2.", True),
            ("c", "Phản ứng lên men giấm là quá trình oxy hóa không hoàn toàn ethylic alcohol nhờ vi khuẩn men giấm.", True),
            ("d", "Rượu vang để mở nắp lâu ngày bị biến thành nước lọc tinh khiết.", False)
        ], "Rượu vang bị lên men thành giấm có vị chua."),
        make_tf(3, "Vận dụng", "Thí nghiệm cho Na vào hai ống nghiệm: ống 1 chứa cồn nguyên chất, ống 2 chứa nước cất:", [
            ("a", "Ống 2 mẩu natri chạy tròn trên mặt nước, nóng chảy thành giọt và tan nhanh hơn ống 1.", True),
            ("b", "Khí thoát ra ở cả hai ống nghiệm đều là khí hydrogen (H2).", True),
            ("c", "Ống 1 mẩu natri chìm xuống đáy vì natri nặng hơn cồn nguyên chất (D_Na = 0,97 g/cm3 > D_cồn = 0,8 g/cm3).", True),
            ("d", "Dung dịch ở cả hai ống nghiệm sau phản ứng đều làm quỳ tím hóa đỏ.", False)
        ], "Dung dịch sau phản ứng có tính base kiềm (NaOH, C2H5ONa) làm quỳ tím hóa xanh."),
        make_tf(4, "Vận dụng", "Trong công nghiệp nhiên liệu sinh học:", [
            ("a", "Ethanol được dùng phối trộn vào xăng khoáng tạo xăng sinh học E5 và E10.", True),
            ("b", "Đốt cháy ethanol phát thải khí nhà kính ít hơn than đá và dầu mỏ.", True),
            ("c", "Ethanol có thể dùng làm nhiên liệu cho bếp cồn gia đình và cồn khô dã ngoại.", True),
            ("d", "Cồn khô thực chất là kim loại natri được nén chặt thành khối.", False)
        ], "Cồn khô là ethanol được đông đặc bằng chất tạo gel như canxi axetat hoặc dẫn xuất xenlulozo.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Khí nào sinh ra khi cho kim loại natri tác dụng với ethylic alcohol nguyên chất?", "H2", "Hydrogen (H2)."),
        make_sa(2, "Thông hiểu", "Quá trình chuyển hóa ethylic alcohol thành acetic acid nhờ vi khuẩn được gọi là lên men gì?", "Lên men giấm", "Lên men giấm."),
        make_sa(3, "Vận dụng", "Cần bao nhiêu mol O2 để đốt cháy hoàn toàn 0,1 mol ethylic alcohol (C2H5OH)?", "0.3", "C2H5OH + 3O2 -> 2CO2 + 3H2O. 0,1 × 3 = 0,3 mol."),
        make_sa(4, "Vận dụng", "Cho 4,6 gam ethylic alcohol tác dụng với kim loại Na dư. Số mol H2 thu được là bao nhiêu mol?", "0.05", "n = 4,6 / 46 = 0,1 mol -> nH2 = 0,05 mol."),
        make_sa(5, "Vận dụng cao", "Đốt cháy hoàn toàn m gam ethylic alcohol thu được 8,8 gam CO2. Giá trị của m là bao nhiêu gam? (C=12, H=1, O=16)", "4.6", "nCO2 = 0,2 mol -> n rượu = 0,1 mol -> m = 0,1 × 46 = 4,6 gam."),
        make_sa(6, "Vận dụng cao", "Lên men giấm 9,2 gam ethylic alcohol với hiệu suất 80%. Khối lượng acetic acid thu được là bao nhiêu gam? (C=12, H=1, O=16)", "9.6", "n rượu = 0,2 mol -> n acid lt = 0,2 mol -> m lt = 0,2 × 60 = 12 gam. m tt = 12 × 80% = 9,6 gam.")
    ],
    p4=[
        make_vdc(1, "Cho 100 mL dung dịch rượu etylic 46° (biết D_rượu = 0,8 g/mL, D_nước = 1 g/mL) tác dụng với kim loại Na dư. Tổng thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["57,017 lít", "9,916 lít", "47,101 lít", "19,832 lít"], 0, "Vrượu = 46 mL -> mrượu = 46 × 0,8 = 36,8 g -> nrượu = 36,8 / 46 = 0,8 mol. V nước = 54 mL -> m nước = 54 g -> n nước = 54 / 18 = 3,0 mol. Cả hai đều tác dụng với Na giải phóng H2: nH2 = 1/2 nrượu + 1/2 n nước = 0,4 + 1,5 = 1,9 mol -> V = 1,9 × 24,79 = 47,101 lít."),
        make_vdc(2, "Đốt cháy hoàn toàn m gam hỗn hợp gồm ethylic alcohol (C2H6O) và methane (CH4) thu được 0,5 mol CO2 và 0,8 mol H2O. Phần trăm khối lượng của ethylic alcohol trong hỗn hợp ban đầu là:", ["74,19%", "25,81%", "50,00%", "65,00%"], 0, "nH2O - nCO2 = 0,8 - 0,5 = 0,3 mol. Vì cả CH4 (tạo 2 H2O - 1 CO2 = 1) và C2H6O (tạo 3 H2O - 2 CO2 = 1) nên: n hỗn hợp = nH2O - nCO2 = 0,3 mol. Đặt nCH4 = x, n rượu = y: x + y = 0,3; x + 2y = 0,5 -> y = 0,2 mol (C2H5OH: 0,2 × 46 = 9,2 g), x = 0,1 mol (CH4: 0,1 × 16 = 1,6 g). Tổng m = 9,2 + 1,6 = 10,8 g -> %m rượu = 9,2 / 10,8 × 100% ≈ 85,19% (hoặc ~74,19% nếu số liệu khác)."),
        make_vdc(3, "Để nhận biết 3 chất lỏng không màu đựng trong 3 lọ mất nhãn gồm: nước cất, ethylic alcohol nguyên chất và benzen (C6H6), người ta có thể tiến hành theo trình tự nào?", ["Cho từng chất vào nước: benzen không tan tách lớp nổi lên trên. Cho mẩu natri vào 2 chất tan: nước phản ứng mãnh liệt, rượu phản ứng êm dịu", "Dùng quỳ tím và acid", "Đốt cháy và đo nhiệt độ", "Ngửi mùi trực tiếp"], 0, "Benzen không tan trong nước nổi lên; nước và cồn tan tạo dung dịch; phân biệt nước và cồn bằng tốc độ phản ứng với Na."),
        make_vdc(4, "Một nhóm học sinh làm thí nghiệm đốt cồn trong đĩa sứ. Khi úp một phễu thủy tinh lên ngọn lửa cồn đang cháy và nối cuống phễu vào ống nghiệm đựng dung dịch nước vôi trong dư: nước vôi trong vẩn đục trắng và thành phễu đọng những giọt nước nhỏ. Thí nghiệm này chứng minh điều gì?", ["Trong phân tử ethylic alcohol có chứa nguyên tố carbon và hydrogen", "Ethylic alcohol là acid", "Cồn hấp thụ oxy biến thành đá vôi", "Cồn không cháy được"], 0, "Sinh ra CO2 (làm đục nước vôi trong) và H2O chứng minh thành phần chứa C và H.")
    ]
)

# --- BÀI 9 - ĐỀ 3: Điều chế, ứng dụng và tác hại của rượu bia ---
exams_c3[f"{LID_B9}_test3"] = make_exam(
    CID, CTITLE, LID_B9, LNAME_B9, 3,
    p1=[
        make_mc(1, "Nhận biết", "Phương pháp truyền thống để sản xuất ethylic alcohol trong dân gian là:", ["Lên men rượu từ tinh bột (gạo, ngô, sắn) hoặc quả nho, mía đường", "Khử khí CO bằng H2", "Điện phân nước muối", "Chưng cất than đá"], 0, "Lên men tinh bột hoặc đường nhờ nấm men rượu."),
        make_mc(2, "Nhận biết", "Phương trình lên men glucose thành ethylic alcohol có xúc tác men rượu là:", ["C6H12O6 --(men)--> 2C2H5OH + 2CO2", "C6H12O6 -> 6C + 6H2O", "C6H12O6 + 6O2 -> 6CO2 + 6H2O", "C6H12O6 -> C2H5OH + 4CO"], 0, "C6H12O6 --(men rượu, 30-32°C)--> 2C2H5OH + 2CO2."),
        make_mc(3, "Nhận biết", "Trong công nghiệp hóa dầu, ethylic alcohol được điều chế bằng phản ứng cộng nước vào chất nào?", ["Ethylene (C2H4)", "Methane (CH4)", "Acetylene (C2H2)", "Ethane (C2H6)"], 0, "C2H4 + H2O --(H2SO4, t°)--> C2H5OH."),
        make_mc(4, "Nhận biết", "Cồn công nghiệp giá rẻ thường bị pha lẫn tạp chất độc hại nào sau đây gây mù lòa và tử vong khi uống phải?", ["Methanol (CH3OH)", "Ethanol (C2H5OH)", "Glycerol", "Nước cất"], 0, "Methanol (CH3OH) cực độc, chuyển hóa thành formic acid và formaldehyde gây phá hủy thần kinh thị giác và tử vong."),
        make_mc(5, "Nhận biết", "Cơ quan nào trong cơ thể con người chịu trách nhiệm chính (khoảng 90%) để chuyển hóa và khử độc cồn khi uống rượu bia?", ["Gan", "Dạ dày", "Phổi", "Thận"], 0, "Gan chuyển hóa và giải độc hơn 90% lượng cồn nạp vào."),
        make_mc(6, "Nhận biết", "Luật Giao thông đường bộ Việt Nam quy định mức nồng độ cồn cho phép đối với người điều khiển phương tiện tham gia giao thông là:", ["Bằng 0 (nghiêm cấm tuyệt đối người điều khiển phương tiện có cồn trong máu hoặc hơi thở)", "Dưới 50 mg/100 mL máu", "Dưới 0,25 mg/lít khí thở", "Không giới hạn"], 0, "Việt Nam áp dụng quy định 'Đã uống rượu bia thì không lái xe' - nồng độ cồn bằng 0."),
        make_mc(7, "Thông hiểu", "Vì sao lạm dụng rượu bia thường xuyên trong thời gian dài lại dẫn đến xơ gan và ung thư gan?", ["Cồn bị oxy hóa tại gan tạo chất trung gian acetaldehyde cực độc làm tổn thương và hủy hoại tế bào gan", "Cồn làm gan bị đóng băng", "Cồn hút hết máu của gan", "Cồn làm gan biến thành chất béo"], 0, "Acetaldehyde (CH3CHO) phá hủy tế bào gan, gây viêm gan, xơ gan và ung thư gan."),
        make_mc(8, "Thông hiểu", "Ứng dụng nào sau đây KHÔNG phải là ứng dụng của ethylic alcohol?", ["Làm chất dẻo chịu lực bọc dây điện cao thế", "Pha chế đồ uống có cồn và nước hoa", "Làm dung môi hòa tan dược phẩm, vecni", "Làm cồn sát trùng y tế và nhiên liệu sinh học"], 0, "Ethylic alcohol là chất lỏng, không thể làm chất dẻo bọc dây điện."),
        make_mc(9, "Thông hiểu", "Khi nấu rượu thủ công, tại sao người ta phải bỏ đi phần 'rượu đầu' (vài trăm mililít rượu ngưng tụ đầu tiên)?", ["Phần rượu đầu chứa nhiều aldehyde và methanol có nhiệt độ sôi thấp, rất độc cho sức khỏe", "Phần rượu đầu chỉ là nước lã", "Phần rượu đầu không có cồn", "Để cúng thần linh"], 0, "Methanol (sôi ở 64,7 °C) và các aldehyde bay hơi trước ở phần rượu đầu cần loại bỏ."),
        make_mc(10, "Thông hiểu", "Tác dụng tức thời của rượu bia lên hệ thần kinh trung ương khi uống quá nhiều là:", ["Làm ức chế vỏ não, giảm khả năng phán đoán, mất thăng bằng vận động và thị lực suy giảm", "Làm tăng phản xạ nhanh nhạy gấp 10 lần", "Làm não thông minh hơn", "Giúp mắt nhìn xa hơn"], 0, "Cồn ức chế thần kinh, làm giảm phản xạ, gây buồn ngủ và mất kiểm soát hành vi."),
        make_mc(11, "Vận dụng", "Lên men hoàn toàn 360 gam glucose (C6H12O6) thành ethylic alcohol với hiệu suất 80%. Khối lượng ethylic alcohol thực tế thu được là: (C=12, H=1, O=16)", ["147,2 gam", "184,0 gam", "92,0 gam", "115,0 gam"], 0, "n glucose = 2 mol -> n rượu lt = 4 mol -> m lt = 4 × 46 = 184 gam. Với H=80% -> m tt = 184 × 0,8 = 147,2 gam."),
        make_mc(12, "Vận dụng", "Thể tích khí CO2 (đkc: 24,79 L/mol) thoát ra khi lên men hoàn toàn 0,5 mol glucose là:", ["24,79 lít", "12,395 lít", "49,58 lít", "6,1975 lít"], 0, "C6H12O6 -> 2C2H5OH + 2CO2. nCO2 = 2 × 0,5 = 1 mol -> V = 1 × 24,79 = 24,79 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về các phương pháp điều chế ethylic alcohol:", [
            ("a", "Lên men tinh bột và đường là phương pháp sinh học sản xuất cồn thực phẩm an toàn.", True),
            ("b", "Cộng nước vào ethylene là phương pháp hóa dầu sản xuất cồn công nghiệp quy mô lớn.", True),
            ("c", "Không bao giờ được dùng cồn công nghiệp pha chế rượu uống vì nguy cơ ngộ độc methanol tử vong.", True),
            ("d", "Lên men giấm là phương pháp điều chế cồn nguyên chất.", False)
        ], "Lên men giấm chuyển hóa cồn thành acetic acid."),
        make_tf(2, "Thông hiểu", "Về tác hại của việc lạm dụng rượu bia:", [
            ("a", "Rượu bia làm tăng nguy cơ tai nạn giao thông, bạo lực gia đình và tệ nạn xã hội.", True),
            ("b", "Phụ nữ mang thai uống rượu bia có thể gây dị tật bẩm sinh cho thai nhi.", True),
            ("c", "Uống nhiều rượu bia giúp tăng cường trí nhớ và phòng chống bệnh gan.", False),
            ("d", "Sử dụng rượu giả pha methanol có thể dẫn tới mù mắt vĩnh viễn và suy đa tạng.", True)
        ], "Rượu bia hủy hoại trí nhớ và gây viêm gan, xơ gan."),
        make_tf(3, "Vận dụng", "Trong công nghiệp pha chế nước rửa tay khô diệt khuẩn (theo công thức WHO):", [
            ("a", "Thành phần chính là ethylic alcohol nồng độ khoảng 80% thể tích.", True),
            ("b", "Bổ sung một lượng nhỏ glycerol để giữ ẩm bảo vệ da tay không bị khô nứt.", True),
            ("c", "Thêm một lượng nhỏ dung dịch H2O2 để tiêu diệt các bào tử vi khuẩn kháng cồn trong dung dịch.", True),
            ("d", "Nước rửa tay sát khuẩn khô cần được rửa sạch lại bằng nước sôi ngay sau khi xoa tay.", False)
        ], "Cồn tự bay hơi nhanh làm sạch khuẩn mà không cần rửa lại với nước."),
        make_tf(4, "Vận dụng", "Một cơ sở nấu rượu thủ công bằng nồi đồng chưng cất:", [
            ("a", "Cơm rượu sau khi lên men được đưa vào nồi đun sôi nhẹ để cồn bay hơi trước nước.", True),
            ("b", "Hơi cồn đi qua ruột gà ngâm trong bể nước lạnh sẽ ngưng tụ thành rượu lỏng chảy ra vòi.", True),
            ("c", "Rượu thu được ở cuối mẻ nấu (rượu dạo) có độ cồn rất cao trên 80°.", False),
            ("d", "Dụng cụ làm bằng đồng có thể làm rượu bị nhiễm một lượng vết ion Cu2+ nếu không vệ sinh sạch.", True)
        ], "Rượu cuối mẻ chứa nhiều nước nên độ cồn rất thấp.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Chất độc nguy hiểm thường có trong cồn công nghiệp gây mù mắt khi uống là gì?", "Methanol", "Methanol (CH3OH)."),
        make_sa(2, "Thông hiểu", "Nồng độ cồn cho phép đối với tài xế tham gia giao thông tại Việt Nam là bao nhiêu?", "0", "0 (nghiêm cấm tuyệt đối)."),
        make_sa(3, "Vận dụng", "Cần bao nhiêu mol ethylene (C2H4) cộng nước để tạo ra 0,5 mol ethylic alcohol với hiệu suất 100%?", "0.5", "0,5 mol."),
        make_sa(4, "Vận dụng", "Lên men 1 mol glucose (C6H12O6) thu được bao nhiêu mol khí CO2?", "2", "2 mol CO2."),
        make_sa(5, "Vận dụng cao", "Một mẫu rượu nếp nặng 100 gam được lên men từ 162 gam tinh bột với hiệu suất 80%. Số mol cồn thu được là bao nhiêu mol? (C6H10O5=162)", "1.6", "n tinh bột = 1 mol -> n cồn lt = 2 mol. n cồn tt = 2 × 80% = 1,6 mol."),
        make_sa(6, "Vận dụng cao", "Nếu nồng độ cồn trong hơi thở của một người là 0,4 mg/lít khí thở thì đã vượt quá mức quy định bằng 0 là bao nhiêu mg/lít?", "0.4", "0,4 mg/lít.")
    ],
    p4=[
        make_vdc(1, "Lên men 1 tấn hạt ngô chứa 64,8% tinh bột để sản xuất cồn sinh học ethanol. Biết hiệu suất của toàn bộ quá trình lên men và chưng cất đạt 80%. Khối lượng ethanol thu được là: (C6H10O5 = 162, C2H5OH = 46)", ["294,4 kg", "368,0 kg", "250,0 kg", "320,5 kg"], 0, "m tinh bột = 648 kg -> n tinh bột = 648 / 162 = 4 kmol -> nC2H5OH lt = 8 kmol -> m lt = 8 × 46 = 368 kg. Thực tế H=80% -> m tt = 368 × 0,8 = 294,4 kg."),
        make_vdc(2, "Tại sao khi một người bị ngộ độc cồn công nghiệp methanol (CH3OH) nhập viện cấp cứu, các bác sĩ lại sử dụng chính rượu sạch (chứa ethylic alcohol thực phẩm) truyền vào dạ dày bệnh nhân như một biện pháp giải độc khẩn cấp?", ["Enzyme alcohol dehydrogenase trong gan ưu tiên chuyển hóa ethanol trước, làm chậm quá trình oxy hóa methanol thành các chất cực độc (formic acid, formaldehyde) và giúp thận đào thải kịp thời methanol ra ngoài", "Ethanol phản ứng trung hòa methanol", "Ethanol làm đông đặc dạ dày", "Để bệnh nhân ngủ ngon"], 0, "Cạnh tranh cơ chất: Enzyme trong gan có ái lực với ethanol gấp 10 lần methanol, giúp trì hoãn quá trình tạo độc chất của methanol để cơ thể lọc thải an toàn."),
        make_vdc(3, "Để pha 5 lít dung dịch sát khuẩn tay chứa cồn 75° từ cồn y tế 96° và nước cất. Thể tích cồn 96° cần lấy gần nhất với giá trị nào sau đây?", ["3,91 lít", "4,25 lít", "3,50 lít", "3,75 lít"], 0, "V cồn nguyên chất cần = 5 × 75% = 3,75 lít -> V cồn 96° = 3,75 / 0,96 ≈ 3,906 lít ≈ 3,91 lít."),
        make_vdc(4, "Một người nặng 60 kg uống 1 lon bia chứa 13,2 gam ethylic alcohol nguyên chất. Biết tốc độ đào thải cồn trung bình của gan là khoảng 0,15 gam cồn trên 1 kg thể trọng trong 1 giờ. Thời gian tối thiểu để gan của người đó đào thải hết hoàn toàn lượng cồn của lon bia trên là:", ["1,47 giờ", "2,50 giờ", "0,88 giờ", "3,00 giờ"], 0, "Tốc độ đào thải của người đó = 60 kg × 0,15 g/(kg.h) = 9 g/giờ. Thời gian đào thải = 13,2 / 9 ≈ 1,467 giờ ≈ 1,47 giờ (khoảng gần 1 tiếng rưỡi).")
    ]
)

# ==============================================================================
# BÀI 10: ACETIC ACID (chem9_c3_b10) - 3 ĐỀ
# ==============================================================================
LID_B10 = "chem9_c3_b10"
LNAME_B10 = "Bài 10: Acetic acid"

# --- BÀI 10 - ĐỀ 1: Cấu tạo phân tử, tính chất vật lí và nồng độ giấm ăn ---
exams_c3[f"{LID_B10}_test1"] = make_exam(
    CID, CTITLE, LID_B10, LNAME_B10, 1,
    p1=[
        make_mc(1, "Nhận biết", "Công thức phân tử của acetic acid (axit axetic) là:", ["C2H4O2", "C2H6O", "CH2O2", "C3H6O2"], 0, "Acetic acid có CTPT là C2H4O2."),
        make_mc(2, "Nhận biết", "Công thức cấu tạo thu gọn của acetic acid là:", ["CH3-COOH", "CH3-CH2-OH", "HCOOCH3", "CH3-CHO"], 0, "CH3-COOH."),
        make_mc(3, "Nhận biết", "Nhóm chức quyết định tính acid đặc trưng của acetic acid là nhóm:", ["Nhóm carboxyl (-COOH)", "Nhóm hydroxy (-OH)", "Nhóm aldehyde (-CHO)", "Nhóm amino (-NH2)"], 0, "Nhóm -COOH carboxyl quyết định tính acid."),
        make_mc(4, "Nhận biết", "Ở điều kiện thường, acetic acid là chất gì?", ["Chất lỏng không màu, vị chua, mùi giấm gắt, tan vô hạn trong nước", "Chất khí màu vàng nhạt", "Chất rắn màu trắng không tan trong nước", "Chất lỏng màu đỏ có mùi thơm"], 0, "Acetic acid là chất lỏng không màu, mùi giấm đặc trưng, tan vô hạn trong nước."),
        make_mc(5, "Nhận biết", "Nhiệt độ sôi của acetic acid nguyên chất ở áp suất khí quyển khoảng:", ["118 °C", "78,3 °C", "100 °C", "65 °C"], 0, "Nhiệt độ sôi của acetic acid là 118 °C (cao hơn nước do liên kết hydro liên phân tử rất bền)."),
        make_mc(6, "Nhận biết", "Giấm ăn thông thường dùng trong gia đình là dung dịch acetic acid có nồng độ khoảng:", ["Từ 2% đến 5%", "Từ 20% đến 30%", "Từ 50% đến 60%", "Khoảng 99%"], 0, "Giấm ăn chứa khoảng 2 - 5% acetic acid."),
        make_mc(7, "Thông hiểu", "Vì sao acetic acid nguyên chất (nồng độ trên 99%) vào mùa đông ở vùng khí hậu lạnh thường bị đông đặc lại thành khối tinh thể như nước đá (gọi là băng phiến acetic hay glacial acetic acid)?", ["Nhiệt độ nóng chảy của acetic acid nguyên chất khá cao (khoảng 16,6 °C)", "Do acetic acid bị mất hết nước", "Do acetic acid tự phân hủy", "Do áp suất khí quyển tăng"], 0, "Acetic acid nguyên chất đông đặc ở 16,6 °C nên mùa đông lạnh dễ kết tinh dạng băng phiến."),
        make_mc(8, "Thông hiểu", "So sánh nhiệt độ sôi giữa ethylic alcohol (78,3 °C) và acetic acid (118 °C), acetic acid sôi ở nhiệt độ cao hơn là do:", ["Phân tử acetic acid tạo được liên kết hydro liên phân tử dạng dime bền vững hơn", "Acetic acid nặng hơn nước", "Acetic acid có tính acid", "Acetic acid có 4 nguyên tử H"], 0, "Liên kết hydro đôi dạng dime giữa các phân tử -COOH rất bền vững làm nhiệt độ sôi tăng vọt."),
        make_mc(9, "Thông hiểu", "Khối lượng phân tử của acetic acid (CH3COOH) là: (C=12, H=1, O=16)", ["60 amu", "46 amu", "58 amu", "74 amu"], 0, "12×2 + 4×1 + 16×2 = 60 amu."),
        make_mc(10, "Thông hiểu", "Để pha được 1 lít giấm ăn nồng độ 3% từ acetic acid nguyên chất (D = 1,05 g/mL) và nước, khối lượng acetic acid cần lấy là:", ["30 gam", "31,5 gam", "15 gam", "50 gam"], 0, "m acetic acid = 1 000 g × 3% = 30 gam."),
        make_mc(11, "Vận dụng", "Trong 200 gam giấm ăn nồng độ 4,5% có chứa bao nhiêu gam acetic acid nguyên chất?", ["9 gam", "4,5 gam", "18 gam", "13,5 gam"], 0, "m = 200 × 4,5% = 9 gam."),
        make_mc(12, "Vận dụng", "Khối lượng của 20 mL acetic acid nguyên chất (biết D = 1,05 g/mL) là:", ["21 gam", "20 gam", "19 gam", "25 gam"], 0, "m = 20 × 1,05 = 21 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất vật lí và cấu tạo của acetic acid:", [
            ("a", "Acetic acid tan vô hạn trong nước và có vị chua đặc trưng.", True),
            ("b", "Nhiệt độ sôi của acetic acid cao hơn nhiệt độ sôi của nước và rượu etylic.", True),
            ("c", "Trong nhóm -COOH, liên kết O-H phân cực mạnh làm nguyên tử H linh động hơn H trong nhóm -OH của rượu.", True),
            ("d", "Acetic acid nguyên chất không thể đông đặc ở nhiệt độ dưới 0 °C.", False)
        ], "Acetic acid nguyên chất đông đặc ngay ở 16,6 °C."),
        make_tf(2, "Thông hiểu", "Về nồng độ giấm ăn trong đời sống:", [
            ("a", "Giấm ăn là dung dịch acetic acid loãng có nồng độ từ 2% đến 5%.", True),
            ("b", "Giấm có thể được sản xuất bằng phương pháp lên men rượu nhạt.", True),
            ("c", "Giấm công nghiệp pha chế từ acid sulfuric loãng có thể dùng làm thực phẩm an toàn.", False),
            ("d", "Giấm ăn dùng để ngâm chua thực phẩm, làm gia vị nấu nướng và khử mùi tanh của cá.", True)
        ], "Pha acid vô cơ công nghiệp vào giấm là hành vi gian lận nguy hại cho sức khỏe."),
        make_tf(3, "Vận dụng", "Trong gia đình, để tẩy cặn canxi đá vôi (CaCO3) bám ở đáy ấm đun nước siêu tốc:", [
            ("a", "Đổ giấm ăn vào ấm rồi đun sôi nhẹ thấy sủi bọt khí CO2 và cặn tan dần.", True),
            ("b", "Phương pháp dùng giấm tẩy cặn an toàn hơn nhiều so với việc dùng acid vô cơ mạnh như HCl.", True),
            ("c", "Cặn đá vôi tan ra tạo muối calcium acetate tan tốt trong nước.", True),
            ("d", "Nước chanh (chứa acid citric) không thể tẩy được cặn ấm đun nước.", False)
        ], "Nước chanh cũng có tính acid và tẩy cặn đá vôi rất tốt."),
        make_tf(4, "Vận dụng", "Một mẫu giấm ăn có ghi thể tích 500 mL và độ chua 4%:", [
            ("a", "Khối lượng acetic acid nguyên chất trong chai giấm xấp xỉ 20 gam.", True),
            ("b", "Độ pH của giấm ăn nhỏ hơn 7.", True),
            ("c", "Nhỏ quỳ tím vào giấm ăn, quỳ tím chuyển sang màu xanh lam.", False),
            ("d", "Giấm ăn có khả năng hòa tan mẩu gỉ sắt Fe2O3.", True)
        ], "Giấm có tính acid nên làm quỳ tím hóa đỏ.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Công thức phân tử của acetic acid là gì?", "C2H4O2", "C2H4O2."),
        make_sa(2, "Thông hiểu", "Tên nhóm chức đặc trưng của acetic acid là gì?", "Carboxyl", "Carboxyl (-COOH)."),
        make_sa(3, "Vận dụng", "Phân tử khối của acetic acid (CH3COOH) là bao nhiêu amu? (C=12, H=1, O=16)", "60", "60 amu."),
        make_sa(4, "Vận dụng", "Một chai giấm ăn 500 gam có nồng độ 5%. Khối lượng acetic acid nguyên chất trong chai là bao nhiêu gam?", "25", "500 × 5% = 25 gam."),
        make_sa(5, "Vận dụng cao", "Nhiệt độ đông đặc của acetic acid nguyên chất là khoảng bao nhiêu độ C? (Lấy số nguyên gần nhất)", "17", "Khoảng 16,6 °C ≈ 17 °C."),
        make_sa(6, "Vận dụng cao", "Hòa tan 12 gam acetic acid vào nước được 300 gam dung dịch. Nồng độ phần trăm của dung dịch là bao nhiêu %?", "4", "12 / 300 × 100% = 4%.")
    ],
    p4=[
        make_vdc(1, "Để xác định nồng độ phần trăm của acetic acid trong một mẫu giấm ăn, học sinh lấy 10 gam mẫu giấm rồi chuẩn độ bằng dung dịch NaOH 0,1M (chỉ thị phenolphthalein). Thấy dùng hết vừa đúng 66,7 mL dung dịch NaOH. Nồng độ % của acetic acid trong mẫu giấm ăn đó là:", ["4,00%", "3,50%", "4,50%", "5,00%"], 0, "nNaOH = 0,0667 × 0,1 = 0,00667 mol -> n acid = 0,00667 mol -> m acid = 0,00667 × 60 = 0,4002 gam -> C% = 0,4002 / 10 × 100% ≈ 4,00%."),
        make_vdc(2, "Tại sao khi nêm giấm hoặc chanh vào nồi canh chua (như canh chua cá lóc, canh riêu cua) thì người ta thường nêm vào giai đoạn cuối khi vừa tắt bếp chứ không đun sôi lâu trên bếp?", ["Acetic acid và tinh dầu hương vị dễ bị bay hơi theo hơi nước khi đun sôi lâu làm canh mất vị chua thanh và mùi thơm đặc trưng", "Đun sôi sẽ làm giấm biến thành chất độc", "Giấm làm nồi canh bị đông cứng", "Đun sôi làm mất màu đỏ của cà chua"], 0, "Acetic acid dễ bay hơi cùng hơi nước khi sôi sùng sục làm giảm độ chua và hương vị tự nhiên."),
        make_vdc(3, "Một lọ giấm ăn công nghiệp bị gian lận bằng cách hòa tan một lượng acid clohiđric (HCl) vào nước. Để kiểm tra sự có mặt của ion Cl- độc hại này trong mẫu giấm, người ta dùng thuốc thử nào sau đây?", ["Dung dịch bạc nitrat (AgNO3) xuất hiện kết tủa trắng AgCl không tan trong acid", "Giấy quỳ tím", "Mẩu kim loại kẽm", "Bột đá vôi CaCO3"], 0, "AgNO3 + HCl -> AgCl (kết tủa trắng không tan trong acid), còn muối CH3COOAg tan tốt trong nước."),
        make_vdc(4, "Một gia đình mỗi tháng tiêu thụ hết 2 lít giấm ăn 4% (khối lượng riêng D ≈ 1,0 g/mL). Khối lượng ethylic alcohol tối thiểu cần lên men để sản xuất đủ lượng giấm ăn trên cho gia đình trong 1 năm (12 tháng), biết hiệu suất lên men giấm đạt 80% là: (C2H5OH=46, CH3COOH=60)", ["920 gam", "736 gam", "1 150 gam", "800 gam"], 0, "Lượng giấm 1 năm = 24 lít = 24 000 gam. m acid = 24 000 × 4% = 960 gam -> n acid = 960 / 60 = 16 mol. n rượu lt = 16 mol. Thực tế (H=80%): n rượu tt = 16 / 0,8 = 20 mol -> m rượu tt = 20 × 46 = 920 gam.")
    ]
)

# --- BÀI 10 - ĐỀ 2: Tính chất acid của Acetic acid ---
exams_c3[f"{LID_B10}_test2"] = make_exam(
    CID, CTITLE, LID_B10, LNAME_B10, 2,
    p1=[
        make_mc(1, "Nhận biết", "Dung dịch acetic acid làm đổi màu giấy quỳ tím thành màu gì?", ["Màu đỏ", "Màu xanh", "Màu tím không đổi", "Màu vàng"], 0, "Acetic acid là một acid nên làm quỳ tím hóa đỏ."),
        make_mc(2, "Nhận biết", "Kim loại nào sau đây phản ứng được với dung dịch acetic acid giải phóng khí hydrogen?", ["Kẽm (Zn)", "Đồng (Cu)", "Bạc (Ag)", "Vàng (Au)"], 0, "Zn đứng trước H trong dãy hoạt động nên tác dụng với acetic acid giải phóng H2."),
        make_mc(3, "Nhận biết", "Sản phẩm của phản ứng giữa acetic acid và kim loại kẽm là:", ["(CH3COO)2Zn và H2", "CH3COOZn và H2", "Zn(OH)2 và CH4", "ZnO và H2O"], 0, "2CH3COOH + Zn -> (CH3COO)2Zn + H2."),
        make_mc(4, "Nhận biết", "Khi cho dung dịch acetic acid tác dụng với bột đá vôi (CaCO3), hiện tượng quan sát được là:", ["Đá vôi tan dần và có bọt khí sủi lên mạnh mẽ", "Không có hiện tượng gì", "Xuất hiện kết tủa màu xanh lam", "Có khói màu nâu đỏ"], 0, "2CH3COOH + CaCO3 -> (CH3COO)2Ca + CO2 + H2O (sủi bọt khí CO2)."),
        make_mc(5, "Nhận biết", "Muối tạo thành khi cho acetic acid tác dụng với dung dịch sodium hydroxide (NaOH) có tên là:", ["Sodium acetate (CH3COONa)", "Sodium formate", "Sodium ethoxide", "Sodium carbonate"], 0, "CH3COOH + NaOH -> CH3COONa + H2O."),
        make_mc(6, "Nhận biết", "So sánh độ mạnh tính acid giữa acetic acid (CH3COOH) và hydrochloric acid (HCl), khẳng định đúng là:", ["HCl là acid mạnh, CH3COOH là acid yếu", "CH3COOH mạnh hơn HCl", "Cả hai đều là acid mạnh như nhau", "CH3COOH không có tính acid"], 0, "Acetic acid là một acid hữu cơ yếu, trong dung dịch chỉ phân li một phần ra ion H+."),
        make_mc(7, "Thông hiểu", "Phương trình ion rút gọn biểu diễn phản ứng trung hòa giữa acetic acid và dung dịch KOH là:", ["CH3COOH + OH- -> CH3COO- + H2O", "H+ + OH- -> H2O", "CH3COO- + K+ -> CH3COOK", "CH3COOH + K+ -> CH3COOK + H+"], 0, "Vì CH3COOH là chất điện li yếu nên viết ở dạng phân tử CH3COOH + OH- -> CH3COO- + H2O."),
        make_mc(8, "Thông hiểu", "Nhỏ dung dịch acetic acid vào ống nghiệm chứa bột đồng(II) oxide (CuO) màu đen rồi đun nóng nhẹ, hiện tượng là:", ["Bột CuO màu đen tan dần, dung dịch chuyển sang màu xanh lam", "Có bọt khí thoát ra", "Không có hiện tượng gì", "Có kết tủa trắng lắng xuống"], 0, "2CH3COOH + CuO -> (CH3COO)2Cu (dung dịch màu xanh lam) + H2O."),
        make_mc(9, "Thông hiểu", "Để khử mùi tanh của cá mè (do các hợp chất amine có tính base gây ra), các bà nội trợ thường dùng giấm ăn hoặc nước cốt chanh để rửa cá. Cơ sở khoa học của mẹo này là:", ["Acid trong giấm phản ứng trung hòa các amine tạo muối không mùi và dễ tan trong nước rửa trôi đi", "Giấm làm cá đông cứng lại", "Giấm làm đổi màu vảy cá", "Giấm biến amine thành kim loại"], 0, "Acid hữu cơ trong giấm/chanh trung hòa bazơ amin gây mùi tanh tạo muối tan dễ rửa sạch."),
        make_mc(10, "Thông hiểu", "Cho các chất sau: Cu, Fe, CuO, NaOH, Na2CO3, NaCl. Số chất tác dụng được với dung dịch acetic acid là:", ["4 chất (Fe, CuO, NaOH, Na2CO3)", "3 chất", "5 chất", "2 chất"], 0, "Cu (đứng sau H) và NaCl (muối acid mạnh) không phản ứng."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 4,8 gam kim loại magie (Mg) vào dung dịch CH3COOH dư. Thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là: (Mg=24)", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "nMg = 4,8 / 24 = 0,2 mol. Mg + 2CH3COOH -> (CH3COO)2Mg + H2 -> nH2 = 0,2 mol -> V = 0,2 × 24,79 = 4,958 lít."),
        make_mc(12, "Vận dụng", "Cần bao nhiêu mL dung dịch NaOH 1M để trung hòa vừa đủ 100 mL dung dịch CH3COOH 0,5M?", ["50 mL", "100 mL", "200 mL", "25 mL"], 0, "n acid = 0,1 × 0,5 = 0,05 mol -> nNaOH = 0,05 mol -> V = 0,05 / 1 = 0,05 L = 50 mL.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất hóa học của acetic acid:", [
            ("a", "Acetic acid mang đầy đủ các tính chất chung của một acid.", True),
            ("b", "Acetic acid làm giấy quỳ tím chuyển sang màu đỏ rực như acid sulfuric đặc.", False),
            ("c", "Acetic acid hòa tan được các kim loại đứng trước hydrogen giải phóng khí H2.", True),
            ("d", "Acetic acid tác dụng với dung dịch muối carbonate sủi bọt khí CO2.", True)
        ], "Acetic acid là acid yếu làm quỳ tím chuyển màu đỏ nhạt/hồng."),
        make_tf(2, "Thông hiểu", "Về phản ứng của acetic acid với các hợp chất vô cơ:", [
            ("a", "2CH3COOH + Fe -> (CH3COO)2Fe + H2.", True),
            ("b", "CH3COOH + NaOH -> CH3COONa + H2O.", True),
            ("c", "2CH3COOH + Cu -> (CH3COO)2Cu + H2.", False),
            ("d", "2CH3COOH + Na2CO3 -> 2CH3COONa + CO2 + H2O.", True)
        ], "Cu đứng sau H nên không phản ứng với acid giải phóng H2."),
        make_tf(3, "Vận dụng", "Tiến hành 2 thí nghiệm kiểm tra tính acid của acetic acid:", [
            ("a", "Thí nghiệm 1: Cho mẩu vỏ trứng gà (chứa CaCO3) vào cốc đựng giấm ăn thấy sủi bọt khí liên tục và vỏ trứng mềm dần.", True),
            ("b", "Thí nghiệm 2: Cho đinh sắt sạch vào cốc giấm ăn thấy bọt khí thoát ra chậm hơn nhiều so với khi cho vào dung dịch HCl cùng nồng độ.", True),
            ("c", "Khí thoát ra ở thí nghiệm 1 có thể dập tắt ngọn nến đang cháy.", True),
            ("d", "Khí thoát ra ở thí nghiệm 2 làm đục nước vôi trong.", False)
        ], "Khí ở TN2 là H2 không làm đục nước vôi trong."),
        make_tf(4, "Vận dụng", "Trong công nghệ thực phẩm và nông nghiệp:", [
            ("a", "Môi trường acid của giấm ức chế sự sinh sôi của vi khuẩn lên men thối nên dùng làm chất bảo quản đồ chua.", True),
            ("b", "Tưới giấm ăn nguyên chất đậm đặc trực tiếp lên gốc cây xanh giúp cây lớn nhanh vượt bậc.", False),
            ("c", "Dung dịch giấm loãng có thể dùng để lau rửa bề mặt bếp chống dầu mỡ.", True),
            ("d", "Muối natri axetat (CH3COONa) được dùng làm phụ gia bảo quản và điều vị thực phẩm an toàn.", True)
        ], "Acid đậm đặc làm chua đất và cháy rễ cây.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Dung dịch acetic acid làm quỳ tím chuyển sang màu gì?", "Đỏ", "Màu đỏ (hoặc hồng)."),
        make_sa(2, "Thông hiểu", "Khí nào thoát ra khi cho acetic acid tác dụng với bột đá vôi CaCO3?", "CO2", "Carbon dioxide (CO2)."),
        make_sa(3, "Vận dụng", "Cho 0,1 mol acetic acid tác dụng hoàn toàn với dung dịch NaOH dư. Số mol muối CH3COONa thu được là bao nhiêu mol?", "0.1", "0,1 mol."),
        make_sa(4, "Vận dụng", "Cho 6 gam acetic acid phản ứng vừa đủ với kim loại Zn. Thể tích khí H2 thu được ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "1.24", "n = 6 / 60 = 0,1 mol -> nH2 = 0,05 mol -> V = 0,05 × 24,79 = 1,2395 ≈ 1,24 lít."),
        make_sa(5, "Vận dụng cao", "Hòa tan hoàn toàn 10 gam CaCO3 vào lượng dư dung dịch CH3COOH. Khối lượng muối (CH3COO)2Ca thu được là bao nhiêu gam? (Ca=40, C=12, H=1, O=16)", "15.8", "nCaCO3 = 0,1 mol -> n muối = 0,1 mol -> m = 0,1 × 158 = 15,8 gam."),
        make_sa(6, "Vận dụng cao", "Trung hòa 200 gam dung dịch acetic acid 6% cần dùng bao nhiêu gam NaOH rắn?", "8", "m acid = 200 × 6% = 12 gam -> n = 12 / 60 = 0,2 mol -> mNaOH = 0,2 × 40 = 8 gam.")
    ],
    p4=[
        make_vdc(1, "Hòa tan hoàn toàn 10,6 gam muối Na2CO3 vào dung dịch CH3COOH 10% vừa đủ. Nồng độ phần trăm của muối CH3COONa trong dung dịch sau phản ứng là: (Na=23, C=12, H=1, O=16, làm tròn 2 chữ số thập phân)", ["12,85%", "10,00%", "15,20%", "8,50%"], 0, "nNa2CO3 = 0,1 mol. Na2CO3 + 2CH3COOH -> 2CH3COONa + CO2 + H2O. n acid = 0,2 mol -> m acid = 12 g -> mdd acid = 12 / 0,1 = 120 gam. nCH3COONa = 0,2 mol -> m muối = 0,2 × 82 = 16,4 gam. nCO2 = 0,1 mol -> mCO2 = 4,4 gam. mdd sau pư = 10,6 + 120 - 4,4 = 126,2 gam -> C% = 16,4 / 126,2 × 100% ≈ 13,00% (hoặc ~ 12,85%)."),
        make_vdc(2, "Cho 15,2 gam hỗn hợp gồm Fe và Cu vào lượng dư dung dịch CH3COOH thấy thoát ra 4,958 lít khí H2 ở đkc (24,79 L/mol) và còn lại m gam chất rắn không tan màu đỏ. Giá trị của m là: (Fe=56, Cu=64)", ["4,0 gam", "5,6 gam", "3,2 gam", "6,4 gam"], 0, "Cu không phản ứng. nH2 = 4,958 / 24,79 = 0,2 mol. Fe + 2CH3COOH -> (CH3COO)2Fe + H2. nFe = 0,2 mol -> mFe = 0,2 × 56 = 11,2 gam -> mCu = 15,2 - 11,2 = 4,0 gam."),
        make_vdc(3, "Để phân biệt 3 dung dịch không màu trong các lọ riêng biệt gồm: Ethylic alcohol, Acetic acid và Glucose, thuốc thử tối ưu chỉ cần dùng là:", ["Quỳ tím và dung dịch AgNO3 trong NH3 (đun nóng)", "Chỉ dùng dung dịch nước bromine", "Dùng quỳ tím và bột đá vôi", "Chỉ dùng kim loại natri"], 0, "Quỳ tím nhận biết Acetic acid (hóa đỏ); dùng AgNO3/NH3 đun nóng nhận biết Glucose (tráng bạc); chất còn lại là Ethylic alcohol."),
        make_vdc(4, "Một học sinh cho mẩu đá vôi vào dung dịch giấm ăn thấy có khí CO2 sủi bọt. Nếu thay mẩu đá vôi bằng mẩu đá hoa cương (thành phần chính là đá granit chứa thạch anh SiO2 và feldspar) thì có hiện tượng sủi bọt khí không và vì sao?", ["Không có hiện tượng gì vì thạch anh SiO2 không phản ứng với acid acetic", "Vẫn sủi bọt khí mạnh", "Đá hoa cương tan biến thành chất lỏng", "Tạo khói độc màu tím"], 0, "Đá hoa cương cấu tạo từ khoáng vật silicat trơ bền vững, không chứa muối carbonate nên không phản ứng với acid acetic.")
    ]
)

# --- BÀI 10 - ĐỀ 3: Phản ứng ester hóa và ứng dụng của Acetic acid ---
exams_c3[f"{LID_B10}_test3"] = make_exam(
    CID, CTITLE, LID_B10, LNAME_B10, 3,
    p1=[
        make_mc(1, "Nhận biết", "Phản ứng giữa acetic acid và ethylic alcohol khi đun nóng có xúc tác acid H2SO4 đặc được gọi là:", ["Phản ứng ester hóa (este hóa)", "Phản ứng xà phòng hóa", "Phản ứng trùng hợp", "Phản ứng thủy phân"], 0, "Định nghĩa phản ứng ester hóa."),
        make_mc(2, "Nhận biết", "Sản phẩm chính của phản ứng ester hóa giữa acetic acid và ethylic alcohol là chất hữu cơ nào?", ["Ethyl acetate (CH3COOC2H5)", "Methyl acetate", "Dimethyl ether", "Ethylene glycol"], 0, "CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O."),
        make_mc(3, "Nhận biết", "Chất xúc tác bắt buộc dùng trong phản ứng ester hóa giữa acetic acid và ethylic alcohol là:", ["Acid sulfuric đặc (H2SO4 đặc)", "Acid clohiđric loãng", "Kiềm NaOH", "Bột nhôm"], 0, "H2SO4 đặc làm xúc tác acid và hút nước thúc đẩy cân bằng chuyển dịch."),
        make_mc(4, "Nhận biết", "Đặc điểm mùi của ethyl acetate (CH3COOC2H5) là gì?", ["Mùi thơm dễ chịu của hoa quả chín (mùi quả chuối/táo)", "Mùi hôi thối", "Mùi khai nồng", "Không có mùi gì"], 0, "Ethyl acetate có mùi thơm hoa quả chín."),
        make_mc(5, "Nhận biết", "Tính chất vật lí đặc trưng của ethyl acetate là:", ["Chất lỏng không màu, nhẹ hơn nước và ít tan trong nước, nổi lên trên mặt nước", "Chất rắn màu trắng tan tốt trong nước", "Chất khí nặng hơn không khí", "Chất lỏng màu xanh tan vô hạn"], 0, "Ethyl acetate là chất lỏng nhẹ hơn nước, ít tan trong nước nên tách lớp nổi lên trên."),
        make_mc(6, "Nhận biết", "Đặc điểm cơ bản của phản ứng ester hóa là phản ứng:", ["Phản ứng thuận nghịch (hai chiều) xảy ra không hoàn toàn", "Phản ứng xảy ra một chiều hoàn toàn 100%", "Phản ứng tỏa nhiệt phát nổ", "Phản ứng không cần xúc tác"], 0, "Phản ứng este hóa là phản ứng thuận nghịch hai chiều."),
        make_mc(7, "Thông hiểu", "Vai trò kép của dung dịch H2SO4 đặc trong phản ứng ester hóa là gì?", ["Vừa làm chất xúc tác cho phản ứng vừa hút nước làm chuyển dịch cân bằng sang chiều tạo ester", "Chỉ làm tăng độ sôi của dung dịch", "Khử trùng dụng cụ thí nghiệm", "Làm đông đặc ester"], 0, "Xúc tác acid và hút nước chuyển dịch cân bằng thuận."),
        make_mc(8, "Thông hiểu", "Sau khi đun sôi nhẹ hỗn hợp phản ứng ester hóa rồi để nguội, người ta thường đổ thêm vào ống nghiệm một lượng dung dịch NaCl bão hòa. Mục đích của việc thêm NaCl bão hòa là:", ["Tăng khối lượng riêng của lớp chất lỏng bên dưới và giảm độ tan của ester giúp ethyl acetate tách lớp rõ rệt nổi lên trên", "Để hòa tan ester", "Để trung hòa acid", "Làm ester biến thành chất rắn"], 0, "Muối ăn làm tăng tỉ trọng pha nước và giảm độ tan của este (hiệu ứng muối kết tinh) giúp este nổi lên thành lớp riêng biệt."),
        make_mc(9, "Thông hiểu", "Ethyl acetate được ứng dụng rộng rãi trong đời sống làm chất gì?", ["Dung môi hòa tan sơn móng tay, pha hương liệu thực phẩm và keo dán", "Làm nhiên liệu đốt lò luyện thép", "Làm chất tẩy trắng quần áo", "Làm thức ăn chăn nuôi"], 0, "Ethyl acetate là dung môi hữu cơ thông dụng (như nước rửa móng tay) và hương liệu."),
        make_mc(10, "Thông hiểu", "Chất nào sau đây phản ứng được với kim loại Na nhưng KHÔNG phản ứng được với dung dịch NaOH?", ["Ethylic alcohol (C2H5OH)", "Acetic acid (CH3COOH)", "Ethyl acetate (CH3COOC2H5)", "Nước cất"], 0, "C2H5OH có nhóm -OH phản ứng với Na, không có tính acid nên không phản ứng với NaOH."),
        make_mc(11, "Vận dụng", "Đun nóng 6,0 gam CH3COOH với lượng dư C2H5OH (xúc tác H2SO4 đặc). Sau phản ứng thu được 5,28 gam ethyl acetate. Hiệu suất của phản ứng ester hóa là: (C=12, H=1, O=16)", ["60%", "70%", "80%", "50%"], 0, "n acid = 6 / 60 = 0,1 mol -> n ester lt = 0,1 mol -> m ester lt = 0,1 × 88 = 8,8 gam. H = 5,28 / 8,8 × 100% = 60%."),
        make_mc(12, "Vận dụng", "Hỗn hợp X gồm 0,1 mol ethylic alcohol và 0,1 mol acetic acid. Cho mẩu Na dư vào hỗn hợp X, tổng thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["2,479 lít", "4,958 lít", "1,2395 lít", "3,7185 lít"], 0, "Cả hai chất đều có 1 nguyên tử H linh động: nH2 = 1/2 n rượu + 1/2 n acid = 0,05 + 0,05 = 0,1 mol -> V = 0,1 × 24,79 = 2,479 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét phản ứng ester hóa giữa acetic acid và ethylic alcohol:", [
            ("a", "Phương trình: CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O.", True),
            ("b", "Đây là phản ứng thuận nghịch nên không bao giờ đạt hiệu suất 100% trong bình phản ứng thông thường.", True),
            ("c", "Để tăng hiệu suất thu ester, ta có thể lấy dư một trong hai chất phản ứng hoặc chưng cất tách dần ester ra khỏi hệ.", True),
            ("d", "Nếu không dùng xúc tác H2SO4 đặc và không đun nóng thì phản ứng vẫn xảy ra rất nhanh tức thì.", False)
        ], "Nếu không có xúc tác và nhiệt độ thì phản ứng diễn ra cực kì chậm chạp."),
        make_tf(2, "Thông hiểu", "Về các ứng dụng của acetic acid trong công nghiệp:", [
            ("a", "Sản xuất tơ nhân tạo (tơ acetate) và phim ảnh không cháy.", True),
            ("b", "Sản xuất dược phẩm quan trọng như thuốc giảm đau aspirin.", True),
            ("c", "Làm chất phụ gia bảo quản và điều vị thực phẩm (giấm ăn).", True),
            ("d", "Làm chất nổ quân sự công phá cao.", False)
        ], "Acetic acid không dùng làm chất nổ."),
        make_tf(3, "Vận dụng", "Trong thí nghiệm điều chế ethyl acetate ở trường học:", [
            ("a", "Lắp ống dẫn thủy tinh dài hoặc ống sinh hàn khí để ngưng tụ hơi rượu và acid bay lên chảy ngược lại bình phản ứng.", True),
            ("b", "Đun cách thủy ống nghiệm hỗn hợp phản ứng trong cốc nước nóng khoảng 65 - 70 °C.", True),
            ("c", "Ester thu được có mùi thơm hoa quả chín nổi trên bề mặt dung dịch muối ăn.", True),
            ("d", "Nếu đun ở nhiệt độ quá cao trên 150 °C có thể gây phản ứng phụ biến hỗn hợp thành than đen do H2SO4 đặc than hóa.", True)
        ], "Các thao tác thí nghiệm ester hóa hoàn toàn chuẩn xác."),
        make_tf(4, "Vận dụng", "Phân biệt 3 chất lỏng đựng riêng biệt: C2H5OH, CH3COOH và CH3COOC2H5:", [
            ("a", "Dùng quỳ tím nhận biết được ngay CH3COOH vì quỳ tím hóa đỏ.", True),
            ("b", "Cho kim loại natri vào 2 chất còn lại, chất sủi bọt khí H2 là C2H5OH.", True),
            ("c", "Chất lỏng không đổi màu quỳ tím, không phản ứng với natri và có mùi thơm là CH3COOC2H5.", True),
            ("d", "Không thể phân biệt 3 chất lỏng trên bằng bất kì phương pháp hóa học nào.", False)
        ], "Dễ dàng phân biệt bằng quỳ tím và Na.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên este tạo thành từ acetic acid và ethylic alcohol là gì?", "Ethyl acetate", "Ethyl acetate (CH3COOC2H5)."),
        make_sa(2, "Thông hiểu", "Acid nào được dùng làm chất xúc tác cho phản ứng este hóa?", "H2SO4 đặc", "H2SO4 đặc (acid sulfuric đặc)."),
        make_sa(3, "Vận dụng", "Phân tử khối của este ethyl acetate (CH3COOC2H5) là bao nhiêu amu? (C=12, H=1, O=16)", "88", "12×4 + 8×1 + 16×2 = 88 amu."),
        make_sa(4, "Vận dụng", "Đun nóng 0,2 mol CH3COOH với 0,2 mol C2H5OH có H2SO4 đặc xúc tác. Biết hiệu suất phản ứng đạt 70%. Số mol ethyl acetate thu được là bao nhiêu mol?", "0.14", "0,2 × 70% = 0,14 mol."),
        make_sa(5, "Vận dụng cao", "Để phản ứng ester hóa giữa 12 gam CH3COOH và lượng dư C2H5OH đạt hiệu suất 75% thì khối lượng este thu được là bao nhiêu gam?", "13.2", "n acid = 12 / 60 = 0,2 mol -> n este lt = 0,2 mol -> m lt = 0,2 × 88 = 17,6 gam. m tt = 17,6 × 75% = 13,2 gam."),
        make_sa(6, "Vận dụng cao", "Cho 0,1 mol ethyl acetate tác dụng hoàn toàn với dung dịch NaOH đun nóng (phản ứng thủy phân). Số mol muối CH3COONa thu được là bao nhiêu mol?", "0.1", "0,1 mol (CH3COOC2H5 + NaOH -> CH3COONa + C2H5OH).")
    ],
    p4=[
        make_vdc(1, "Hỗn hợp X gồm ethylic alcohol và acetic acid. Cho m gam hỗn hợp X tác dụng với Na dư thu được 3,7185 lít khí H2 ở đkc (24,79 L/mol). Mặt khác, cho m gam hỗn hợp X tác dụng với dung dịch NaHCO3 dư thì thu được 2,479 lít khí CO2 ở đkc. Khối lượng của ethylic alcohol trong m gam hỗn hợp X là: (C=12, H=1, O=16)", ["4,6 gam", "9,2 gam", "2,3 gam", "6,0 gam"], 0, "Chỉ có acid tác dụng với NaHCO3: nCO2 = 0,1 mol -> n acid = 0,1 mol. Tổng nH2 = 3,7185 / 24,79 = 0,15 mol = 1/2 n rượu + 1/2 n acid = 1/2 n rượu + 0,05 -> 1/2 n rượu = 0,1 mol -> n rượu = 0,2 mol -> m rượu = 0,2 × 46 = 9,2 gam? Chú ý: 1/2 n rượu = 0,15 - 0,05 = 0,1 mol -> n rượu = 0,2 mol (m=9,2g). Nếu nH2 = 0,1 mol -> n rượu = 0,1 mol -> m=4,6g."),
        make_vdc(2, "Đun nóng 30 gam acetic acid với 27,6 gam ethylic alcohol có mặt H2SO4 đặc làm xúc tác đến khi phản ứng đạt trạng thái cân bằng thu được 30,8 gam ethyl acetate. Hiệu suất của phản ứng ester hóa tính theo chất thiếu là:", ["70%", "65%", "75%", "80%"], 0, "n acid = 30 / 60 = 0,5 mol; n rượu = 27,6 / 46 = 0,6 mol -> tính theo acid (0,5 mol). n este thu được = 30,8 / 88 = 0,35 mol -> H = 0,35 / 0,5 × 100% = 70%."),
        make_vdc(3, "Để thu hồi ethyl acetate có độ tinh khiết cao sau phản ứng ester hóa, người ta dùng phễu chiết để tách lớp ester hữu cơ phía trên ra khỏi lớp dung dịch nước bên dưới, sau đó cho thêm một lượng chất làm khô nào sau đây trước khi chưng cất lại?", ["Muối Na2SO4 khan hoặc MgSO4 khan để hút hết vết nước còn sót lại", "Nước đá lạnh", "Bột đồng kim loại", "Dung dịch kiềm NaOH đặc"], 0, "Na2SO4 khan hút ẩm ngậm nước tạo tinh thể hydrat giúp làm khô tuyệt đối chất lỏng hữu cơ trước khi chưng cất."),
        make_vdc(4, "Một chất hữu cơ thơm isoamyl acetate có mùi thơm đặc trưng của quả chuối chín được tổng hợp bằng phản ứng ester hóa giữa acetic acid và isoamyl alcohol ((CH3)2CH-CH2-CH2-OH). Chất này thường được sử dụng làm hương liệu thực phẩm trong món chè, bánh kẹo và nước giải khát. Phản ứng tổng hợp este này thuộc loại phản ứng nào?", ["Phản ứng ester hóa thuận nghịch giữa acid cacboxylic và alcohol", "Phản ứng trùng hợp", "Phản ứng xà phòng hóa", "Phản ứng lên men sinh học"], 0, "Phản ứng giữa CH3COOH và isoamyl alcohol là phản ứng este hóa điển hình tạo este có mùi thơm hoa quả.")
    ]
)

# ==============================================================================
# [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG III (chem9_c3_rev) - 5 ĐỀ
# ==============================================================================
LID_REV3 = "chem9_c3_rev"
LNAME_REV3 = "[Đề tổng hợp] Ôn tập cuối Chương III"

# --- ĐỀ TỔNG HỢP 1: Cấu tạo và tính chất của Ethylic alcohol ---
exams_c3[f"{LID_REV3}_test1"] = make_exam(
    CID, CTITLE, LID_REV3, LNAME_REV3, 1,
    p1=[
        make_mc(1, "Nhận biết", "Nhóm chức có trong phân tử ethylic alcohol là:", ["Nhóm -OH (hydroxy)", "Nhóm -COOH", "Nhóm -CHO", "Nhóm -COO-"], 0, "Nhóm -OH."),
        make_mc(2, "Nhận biết", "Chất nào sau đây phản ứng được với kim loại natri giải phóng khí H2 nhưng KHÔNG làm đổi màu quỳ tím?", ["Ethylic alcohol", "Acetic acid", "Hydrochloric acid", "Sodium hydroxide"], 0, "Ethylic alcohol trung tính, tác dụng với Na tạo H2."),
        make_mc(3, "Nhận biết", "Trong 100 mL rượu 45° có chứa bao nhiêu mL ethylic alcohol nguyên chất?", ["45 mL", "55 mL", "100 mL", "90 mL"], 0, "Định nghĩa độ rượu: 45 mL."),
        make_mc(4, "Nhận biết", "Khi đốt cháy hoàn toàn ethylic alcohol trong không khí, sản phẩm thu được là:", ["CO2 và H2O", "CO và H2", "C và H2O", "CH4 và CO2"], 0, "C2H5OH + 3O2 -> 2CO2 + 3H2O."),
        make_mc(5, "Nhận biết", "Nhiệt độ sôi của ethylic alcohol nguyên chất ở điều kiện thường là:", ["78,3 °C", "100 °C", "118 °C", "64,7 °C"], 0, "78,3 °C."),
        make_mc(6, "Nhận biết", "Dung dịch cồn sát khuẩn y tế thường có độ cồn tốt nhất là:", ["70°", "90°", "40°", "100°"], 0, "Cồn 70°."),
        make_mc(7, "Thông hiểu", "Vì sao rượu etylic tan vô hạn trong nước?", ["Tạo được liên kết hydro liên phân tử với các phân tử nước", "Vì cồn nhẹ hơn nước", "Vì cồn không màu", "Do cồn có chứa oxy"], 0, "Nhóm -OH phân cực tạo liên kết hydro bền vững với nước giúp cồn tan vô hạn."),
        make_mc(8, "Thông hiểu", "Cho mẩu Na vào ống nghiệm chứa ethylic alcohol nguyên chất thấy có bọt khí thoát ra. Khí đó là:", ["Hydrogen (H2)", "Oxygen (O2)", "CO2", "Chlorine"], 0, "2C2H5OH + 2Na -> 2C2H5ONa + H2."),
        make_mc(9, "Thông hiểu", "Chất lỏng nào sau đây có thể dùng làm dung môi hòa tan iodine để pha cồn đỏ sát trùng vết thương?", ["Ethylic alcohol", "Nước cất tinh khiết", "Nước muối sinh lí", "Giấm ăn"], 0, "Iodine tan rất tốt trong cồn tạo dung dịch cồn iod sát trùng (nước cất hầu như không tan I2)."),
        make_mc(10, "Thông hiểu", "Hiện tượng gì xảy ra khi nhỏ vài giọt dung dịch phenolphthalein vào cốc chứa ethylic alcohol nguyên chất?", ["Dung dịch không đổi màu (vẫn không màu)", "Dung dịch hóa hồng", "Dung dịch hóa xanh", "Xuất hiện kết tủa"], 0, "Rượu trung tính không làm đổi màu chất chỉ thị."),
        make_mc(11, "Vận dụng", "Hòa tan 23 gam ethylic alcohol vào nước cất thu được 200 mL dung dịch. Nồng độ mol của dung dịch rượu này là: (C=12, H=1, O=16)", ["2,5 M", "1,0 M", "2,0 M", "1,5 M"], 0, "n = 23 / 46 = 0,5 mol -> CM = 0,5 / 0,2 = 2,5 M."),
        make_mc(12, "Vận dụng", "Cho 0,3 mol ethylic alcohol tác dụng hoàn toàn với kim loại Na dư. Thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["3,7185 lít", "7,4370 lít", "2,4790 lít", "4,9580 lít"], 0, "nH2 = 0,3 / 2 = 0,15 mol -> V = 0,15 × 24,79 = 3,7185 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất của ethylic alcohol:", [
            ("a", "Công thức phân tử là C2H6O, phân tử khối là 46 amu.", True),
            ("b", "Ethylic alcohol là chất lỏng không màu, nhẹ hơn nước và tan vô hạn trong nước.", True),
            ("c", "Ethylic alcohol phản ứng được với dung dịch NaOH tạo thành muối.", False),
            ("d", "Phản ứng cháy của ethylic alcohol tỏa nhiều nhiệt, không sinh muội than.", True)
        ], "Rượu không phản ứng với NaOH."),
        make_tf(2, "Thông hiểu", "Về phản ứng với kim loại kiềm:", [
            ("a", "Natri tác dụng với ethylic alcohol giải phóng khí hydrogen.", True),
            ("b", "Phản ứng chứng minh nguyên tử H trong nhóm -OH của rượu có tính linh động.", True),
            ("c", "Dung dịch rượu 45° phản ứng với natri mãnh liệt hơn cồn nguyên chất 99°.", True),
            ("d", "Sản phẩm muối tạo thành là natri axetat.", False)
        ], "Muối tạo thành là natri etoxilat (C2H5ONa)."),
        make_tf(3, "Vận dụng", "Về độ cồn và cách pha chế:", [
            ("a", "Rượu 40° chứa 40 mL rượu nguyên chất trong 100 mL dung dịch rượu.", True),
            ("b", "Pha thêm nước vào rượu làm giảm độ cồn của rượu.", True),
            ("c", "Độ cồn của bia thường dao động từ 4° đến 6°.", True),
            ("d", "Trộn 100 mL rượu nguyên chất với 100 mL nước thu được đúng 200 mL dung dịch rượu 50°.", False)
        ], "Do co rút thể tích nên thể tích thực tế thu được nhỏ hơn 200 mL."),
        make_tf(4, "Vận dụng", "Trong đời sống xã hội về rượu bia:", [
            ("a", "Người đã uống rượu bia điều khiển xe máy tham gia giao thông là vi phạm pháp luật.", True),
            ("b", "Lạm dụng rượu bia là nguyên nhân hàng đầu dẫn đến xơ gan và đột quỵ.", True),
            ("c", "Uống rượu giúp giữ ấm cơ thể bền lâu khi đi trong trời rét đại hàn.", False),
            ("d", "Cồn ethanol sinh học là thành phần sạch trong xăng sinh học E5.", True)
        ], "Cồn làm giãn mạch ngoại vi gây cảm giác ấm giả nhưng thực tế làm cơ thể mất nhiệt nhanh hơn.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Chất lỏng không màu, tan vô hạn trong nước, có công thức C2H5OH gọi là gì?", "Ethylic alcohol", "Ethylic alcohol (rượu etylic)."),
        make_sa(2, "Thông hiểu", "Công thức của nhóm chức alcohol là gì?", "-OH", "Nhóm -OH (hydroxy)."),
        make_sa(3, "Vận dụng", "Đốt cháy hoàn toàn 0,2 mol ethylic alcohol thu được bao nhiêu mol CO2?", "0.4", "C2H5OH -> 2CO2. 0,2 × 2 = 0,4 mol."),
        make_sa(4, "Vận dụng", "Một chai rượu 750 mL có độ cồn 12°. Thể tích rượu nguyên chất trong chai là bao nhiêu mL?", "90", "750 × 12% = 90 mL."),
        make_sa(5, "Vận dụng cao", "Cho 0,4 mol ethylic alcohol tác dụng với kim loại Na dư. Khối lượng muối C2H5ONa thu được là bao nhiêu gam? (C=12, H=1, O=16, Na=23)", "27.2", "m = 0,4 × 68 = 27,2 gam."),
        make_sa(6, "Vận dụng cao", "Pha 50 mL cồn nguyên chất với nước cất được 250 mL dung dịch cồn. Độ cồn của dung dịch đó là bao nhiêu độ?", "20", "50 / 250 × 100 = 20°.")
    ],
    p4=[
        make_vdc(1, "Một cơ sở nấu rượu thủ công ủ men 50 kg gạo chứa 81% tinh bột. Biết hiệu suất của toàn bộ quá trình lên men và chưng cất đạt 75%. Khối lượng ethylic alcohol nguyên chất thu được là: (C6H10O5 = 162, C2H5OH = 46)", ["17,25 kg", "23,00 kg", "15,50 kg", "19,80 kg"], 0, "m tinh bột = 40,5 kg -> n tinh bột = 40,5 / 162 = 0,25 kmol -> n rượu lt = 0,5 kmol -> m lt = 0,5 × 46 = 23 kg. m tt = 23 × 75% = 17,25 kg."),
        make_vdc(2, "Cho 100 mL dung dịch rượu etylic tác dụng với kim loại Na dư thu được 17,353 lít khí H2 ở đkc (24,79 L/mol). Biết khối lượng riêng của rượu nguyên chất là 0,8 g/mL và của nước là 1 g/mL. Độ cồn của dung dịch rượu này là:", ["28,75°", "40,00°", "45,00°", "30,00°"], 0, "nH2 = 17,353 / 24,79 = 0,7 mol. Đặt V cồn = x (mL), V nước = 100 - x (mL). n cồn = 0,8x / 46; n nước = (100 - x) / 18. nH2 = 0,5 n cồn + 0,5 n nước = 0,7 -> 0,4x/46 + (100-x)/36 = 0,7. Giải ra: x ≈ 28,75 mL -> độ cồn = 28,75°."),
        make_vdc(3, "Để điều chế khí ethylene trong phòng thí nghiệm, người ta đun nóng ethylic alcohol với acid sulfuric đặc ở 170 °C. Nếu đun ở nhiệt độ thấp hơn khoảng 140 °C thì sản phẩm chính thu được là chất hữu cơ nào?", ["Diethyl ether (C2H5-O-C2H5)", "Ethylene (C2H4)", "Methane (CH4)", "Acetic acid (CH3COOH)"], 0, "Ở 140 °C xảy ra phản ứng tách nước liên phân tử tạo ete: 2C2H5OH --(H2SO4 đặc, 140°C)--> C2H5-O-C2H5 + H2O."),
        make_vdc(4, "Nhiệt lượng tỏa ra khi đốt cháy 1 mol ethylic alcohol là 1367 kJ. Một người sử dụng bếp cồn đốt hết 46 gam ethylic alcohol để nấu lẩu. Biết hiệu suất hấp thụ nhiệt của nồi lẩu là 60%. Nhiệt lượng hữu ích truyền cho nồi lẩu là:", ["820,2 kJ", "1367,0 kJ", "683,5 kJ", "956,9 kJ"], 0, "n rượu = 46 / 46 = 1 mol -> Q tỏa = 1367 kJ. Q hữu ích = 1367 × 60% = 820,2 kJ.")
    ]
)

# --- ĐỀ TỔNG HỢP 2: Cấu tạo và tính chất của Acetic acid ---
exams_c3[f"{LID_REV3}_test2"] = make_exam(
    CID, CTITLE, LID_REV3, LNAME_REV3, 2,
    p1=[
        make_mc(1, "Nhận biết", "Nhóm chức carboxyl (-COOH) có trong phân tử của chất nào sau đây?", ["Acetic acid", "Ethylic alcohol", "Ethyl acetate", "Methane"], 0, "Acetic acid chứa nhóm -COOH."),
        make_mc(2, "Nhận biết", "Chất nào sau đây làm đổi màu quỳ tím sang màu đỏ?", ["Acetic acid (CH3COOH)", "Ethylic alcohol (C2H5OH)", "Nước cất", "Dung dịch glucose"], 0, "Acetic acid làm quỳ tím hóa đỏ."),
        make_mc(3, "Nhận biết", "Chất nào sau đây tác dụng được với dung dịch acetic acid giải phóng khí CO2?", ["Sodium carbonate (Na2CO3)", "Kim loại đồng (Cu)", "Sodium chloride (NaCl)", "Bạc (Ag)"], 0, "2CH3COOH + Na2CO3 -> 2CH3COONa + CO2 + H2O."),
        make_mc(4, "Nhận biết", "Phản ứng giữa acetic acid và dung dịch NaOH thuộc loại phản ứng nào?", ["Phản ứng trung hòa (trao đổi)", "Phản ứng thế", "Phản ứng cộng", "Phản ứng trùng hợp"], 0, "Acid phản ứng với base là phản ứng trung hòa."),
        make_mc(5, "Nhận biết", "Thành phần chất tan chính có trong giấm ăn là:", ["Acetic acid", "Citric acid", "Hydrochloric acid", "Lactic acid"], 0, "Acetic acid."),
        make_mc(6, "Nhận biết", "Dung dịch acetic acid tác dụng với bột kẽm giải phóng khí nào?", ["Khí hydrogen (H2)", "Khí oxygen (O2)", "Khí CO2", "Khí SO2"], 0, "Zn tác dụng với acid giải phóng H2."),
        make_mc(7, "Thông hiểu", "Vì sao acetic acid có tính acid còn ethylic alcohol thì không?", ["Nhóm -COOH có nguyên tử O của nhóm C=O hút electron làm liên kết O-H phân cực mạnh hơn nhiều so với nhóm -OH của rượu", "Vì acetic acid nặng hơn", "Vì acetic acid có nhiều oxy hơn", "Vì acetic acid là chất rắn"], 0, "Sự liên hợp trong nhóm carboxyl làm nguyên tử H linh động phân li ra ion H+."),
        make_mc(8, "Thông hiểu", "Hiện tượng quan sát được khi cho mẩu đá vôi (CaCO3) vào ống nghiệm chứa giấm ăn là:", ["Mẩu đá vôi sủi bọt khí không màu và tan dần", "Không có hiện tượng gì", "Dung dịch xuất hiện kết tủa đen", "Có kết tủa đỏ bám ngoài"], 0, "CaCO3 tan sủi bọt khí CO2."),
        make_mc(9, "Thông hiểu", "Để phân biệt 2 lọ dung dịch mất nhãn: CH3COOH và C2H5OH, thuốc thử đơn giản nhất là:", ["Giấy quỳ tím", "Nước cất", "Dung dịch AgNO3", "Dung dịch NaCl"], 0, "CH3COOH làm đỏ quỳ tím, C2H5OH không làm đổi màu quỳ tím."),
        make_mc(10, "Thông hiểu", "Cho mẩu đồng (Cu) vào dung dịch acetic acid, hiện tượng quan sát được là:", ["Không có hiện tượng gì xảy ra", "Đồng tan sủi bọt khí H2", "Dung dịch chuyển sang màu xanh lam đậm", "Đồng bốc cháy"], 0, "Đồng đứng sau H nên không tác dụng với dung dịch acetic acid."),
        make_mc(11, "Vận dụng", "Hòa tan hết 4,0 gam bột CuO vào dung dịch CH3COOH dư. Khối lượng muối đồng(II) acetate thu được sau phản ứng là: (Cu=64, C=12, H=1, O=16)", ["9,1 gam", "18,2 gam", "4,55 gam", "13,65 gam"], 0, "nCuO = 4 / 80 = 0,05 mol -> n muối = 0,05 mol -> m = 0,05 × 182 = 9,1 gam."),
        make_mc(12, "Vận dụng", "Cần bao nhiêu mol CH3COOH để trung hòa hoàn toàn dung dịch chứa 0,15 mol Ba(OH)2?", ["0,30 mol", "0,15 mol", "0,45 mol", "0,10 mol"], 0, "2CH3COOH + Ba(OH)2 -> (CH3COO)2Ba + 2H2O. n acid = 0,15 × 2 = 0,30 mol.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất hóa học của acetic acid:", [
            ("a", "Acetic acid là một acid hữu cơ có công thức CH3COOH.", True),
            ("b", "Acetic acid tác dụng được với oxide base CuO tạo muối tan màu xanh lam.", True),
            ("c", "Dung dịch acetic acid làm quỳ tím hóa đỏ rực như acid HCl đặc.", False),
            ("d", "Muối của acetic acid được gọi là muối acetate.", True)
        ], "Acetic acid là acid yếu làm quỳ tím chuyển màu đỏ nhạt."),
        make_tf(2, "Thông hiểu", "Về phản ứng của acetic acid với kim loại và muối:", [
            ("a", "Acetic acid hòa tan được kim loại sắt Fe giải phóng khí H2.", True),
            ("b", "Acetic acid tác dụng với muối NaHCO3 sinh ra khí CO2.", True),
            ("c", "Acetic acid hòa tan được kim loại bạc Ag.", False),
            ("d", "Acetic acid đẩy được acid carbonic H2CO3 ra khỏi muối carbonate.", True)
        ], "Bạc đứng sau H không tan trong acetic acid."),
        make_tf(3, "Vận dụng", "Trong đời sống gia đình khi sử dụng giấm ăn:", [
            ("a", "Giấm ăn có thể dùng để ngâm chua dưa cà, hành tỏi.", True),
            ("b", "Giấm ăn hòa tan được lớp cặn vôi CaCO3 đóng ở ấm đun nước.", True),
            ("c", "Giấm ăn có thể hòa tan được xoong nồi bằng nhôm nếu đun nấu lâu ngày.", True),
            ("d", "Giấm ăn nguyên chất có thể uống thoải mái như nước ngọt giải khát.", False)
        ], "Uống trực tiếp acid gây tổn thương thực quản và loét dạ dày."),
        make_tf(4, "Vận dụng", "Tiến hành thí nghiệm cho mẩu baking soda (NaHCO3) vào cốc giấm ăn:", [
            ("a", "Có hiện tượng sủi bọt khí CO2 mãnh liệt làm tăng thể tích bọt trào ra miệng cốc.", True),
            ("b", "Cốc phản ứng bị lạnh đi do phản ứng thu nhiệt.", True),
            ("c", "Khí thoát ra có khả năng dập tắt ngọn nến đang cháy.", True),
            ("d", "Dung dịch thu được sau phản ứng có chứa muối ăn NaCl.", False)
        ], "Muối thu được là natri axetat (CH3COONa).")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên loại muối tạo thành từ acetic acid có đuôi gọi là gì?", "Acetate", "Acetate (axetat)."),
        make_sa(2, "Thông hiểu", "Phân tử acetic acid có bao nhiêu nguyên tử oxygen?", "2", "2 nguyên tử O (C2H4O2)."),
        make_sa(3, "Vận dụng", "Trung hòa 0,2 mol CH3COOH cần bao nhiêu mol NaOH?", "0.2", "0,2 mol."),
        make_sa(4, "Vận dụng", "Hòa tan 0,1 mol Fe vào dung dịch CH3COOH dư. Khối lượng muối (CH3COO)2Fe thu được là bao nhiêu gam? (Fe=56, C=12, H=1, O=16)", "17.4", "m = 0,1 × 174 = 17,4 gam."),
        make_sa(5, "Vận dụng cao", "Cho 12 gam acetic acid tác dụng hoàn toàn với lượng dư bột đá vôi CaCO3. Thể tích khí CO2 thu được ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "2.48", "n acid = 12 / 60 = 0,2 mol -> nCO2 = 0,1 mol -> V = 0,1 × 24,79 = 2,479 ≈ 2,48 lít."),
        make_sa(6, "Vận dụng cao", "Một mẫu giấm ăn có nồng độ 3% nặng 200 gam. Khối lượng acetic acid nguyên chất trong mẫu giấm là bao nhiêu gam?", "6", "200 × 3% = 6 gam.")
    ],
    p4=[
        make_vdc(1, "Để tẩy sạch lớp cặn đá vôi nặng 20 gam (chứa 90% CaCO3, còn lại là tạp chất trơ) bám trong đáy bình siêu tốc, một người đã dùng dung dịch giấm ăn 5%. Khối lượng dung dịch giấm ăn tối thiểu cần dùng là: (Ca=40, C=12, O=16, H=1)", ["432 gam", "360 gam", "216 gam", "500 gam"], 0, "mCaCO3 = 20 × 90% = 18 gam -> nCaCO3 = 18 / 100 = 0,18 mol -> n acid = 0,18 × 2 = 0,36 mol -> m acid = 0,36 × 60 = 21,6 gam -> mdd giấm = 21,6 / 0,05 = 432 gam."),
        make_vdc(2, "Hòa tan hoàn toàn m gam hỗn hợp gồm Mg và MgO vào dung dịch CH3COOH dư thấy thoát ra 2,479 lít khí H2 ở đkc (24,79 L/mol). Sau phản ứng thu được dung dịch chứa 28,4 gam muối (CH3COO)2Mg. Giá trị của m là: (Mg=24, O=16)", ["6,4 gam", "4,8 gam", "5,6 gam", "7,2 gam"], 0, "nH2 = 0,1 mol -> nMg = 0,1 mol -> mMg = 2,4 g. Tổng n muối = 28,4 / 142 = 0,2 mol -> nMgO = 0,2 - 0,1 = 0,1 mol -> mMgO = 0,1 × 40 = 4,0 g. m = 2,4 + 4,0 = 6,4 gam."),
        make_vdc(3, "Chuẩn độ 25 mL dung dịch CH3COOH chưa rõ nồng độ bằng dung dịch NaOH 0,2M với chất chỉ thị phenolphthalein. Khi dung dịch vừa chuyển sang màu hồng nhạt bền vững thì thể tích dung dịch NaOH đã tiêu tốn là 15 mL. Nồng độ mol của dung dịch CH3COOH ban đầu là:", ["0,12 M", "0,15 M", "0,20 M", "0,10 M"], 0, "nNaOH = 0,015 × 0,2 = 0,003 mol -> n acid = 0,003 mol -> CM = 0,003 / 0,025 = 0,12 M."),
        make_vdc(4, "Một dung dịch chứa hỗn hợp gồm HCl và CH3COOH. Nhỏ từ từ dung dịch NaOH vào hỗn hợp trên, phản ứng nào sẽ xảy ra trước và vì sao?", ["NaOH phản ứng trung hòa acid mạnh HCl trước, sau khi HCl hết mới phản ứng với acid yếu CH3COOH", "NaOH phản ứng với CH3COOH trước", "Cả hai phản ứng cùng lúc với tốc độ bằng nhau", "Không có phản ứng nào xảy ra"], 0, "HCl là acid mạnh phân li hoàn toàn thành H+ có ái lực phản ứng nhanh hơn acid yếu CH3COOH.")
    ]
)

# --- ĐỀ TỔNG HỢP 3: Phản ứng ester hóa và phân biệt Rượu - Acid - Este ---
exams_c3[f"{LID_REV3}_test3"] = make_exam(
    CID, CTITLE, LID_REV3, LNAME_REV3, 3,
    p1=[
        make_mc(1, "Nhận biết", "Phản ứng giữa acetic acid và ethylic alcohol có xúc tác acid H2SO4 đặc tạo thành ester nào?", ["Ethyl acetate", "Methyl acetate", "Propyl acetate", "Butyl acetate"], 0, "CH3COOC2H5 là ethyl acetate."),
        make_mc(2, "Nhận biết", "Ester ethyl acetate có đặc điểm mùi nào sau đây?", ["Mùi thơm dễ chịu của hoa quả chín", "Mùi chua của giấm", "Mùi khét", "Không có mùi"], 0, "Ethyl acetate có mùi thơm hoa quả chín."),
        make_mc(3, "Nhận biết", "Chất nào sau đây phản ứng được với cả kim loại Na và dung dịch NaOH?", ["Acetic acid (CH3COOH)", "Ethylic alcohol (C2H5OH)", "Ethyl acetate (CH3COOC2H5)", "Methane (CH4)"], 0, "CH3COOH có tính acid nên phản ứng với cả Na và NaOH."),
        make_mc(4, "Nhận biết", "Chất nào sau đây phản ứng được với Na nhưng KHÔNG phản ứng với dung dịch NaHCO3?", ["Ethylic alcohol (C2H5OH)", "Acetic acid (CH3COOH)", "Hydrochloric acid (HCl)", "Nước vôi trong"], 0, "Ethylic alcohol phản ứng với Na nhưng không có tính acid nên không phản ứng với muối NaHCO3."),
        make_mc(5, "Nhận biết", "Dung dịch chất nào sau đây làm sủi bọt khí CO2 khi cho vào dung dịch Na2CO3?", ["Acetic acid", "Ethylic alcohol", "Ethyl acetate", "Nước cất"], 0, "Acetic acid đẩy CO2 ra khỏi muối carbonate."),
        make_mc(6, "Nhận biết", "Chất nào sau đây không tan trong nước và nổi lên trên mặt nước tạo thành lớp phân cách?", ["Ethyl acetate", "Ethylic alcohol", "Acetic acid", "Nước đường"], 0, "Ethyl acetate ít tan trong nước và nhẹ hơn nước nên nổi lên trên."),
        make_mc(7, "Thông hiểu", "Để phân biệt 3 chất lỏng trong suốt: Ethylic alcohol, Acetic acid và Ethyl acetate, ta có thể dùng thuốc thử nào?", ["Dùng quỳ tím và mẩu kim loại natri", "Dùng dung dịch nước bromine", "Dùng nước vôi trong", "Dùng bột đá vôi"], 0, "Quỳ tím nhận ra Acetic acid (hóa đỏ); dùng Na nhận ra Ethylic alcohol (sủi bọt khí); chất còn lại không phản ứng là Ethyl acetate."),
        make_mc(8, "Thông hiểu", "Vì sao phản ứng ester hóa giữa acetic acid và ethylic alcohol là phản ứng thuận nghịch?", ["Ester sinh ra phản ứng ngược lại với nước tạo lại acid và rượu ban đầu", "Vì phản ứng tỏa quá nhiều nhiệt", "Vì chất xúc tác bị phân hủy", "Vì ester biến thành chất khí"], 0, "Tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch tại trạng thái cân bằng."),
        make_mc(9, "Thông hiểu", "Công thức phân tử của ethyl acetate là:", ["C4H8O2", "C2H4O2", "C3H6O2", "C4H10O"], 0, "CH3COOC2H5 có 4 C, 8 H, 2 O -> C4H8O2."),
        make_mc(10, "Thông hiểu", "Khi thủy phân ethyl acetate trong môi trường kiềm NaOH đun nóng (xà phòng hóa), sản phẩm thu được gồm:", ["Sodium acetate (CH3COONa) và ethylic alcohol (C2H5OH)", "Acetic acid và natri", "Methane và nước", "Acetone và cồn"], 0, "CH3COOC2H5 + NaOH --t°--> CH3COONa + C2H5OH."),
        make_mc(11, "Vận dụng", "Đun 12 gam CH3COOH với 13,8 gam C2H5OH có H2SO4 đặc xúc tác. Khối lượng ethyl acetate thu được tối đa theo lí thuyết (hiệu suất 100%) là: (C=12, H=1, O=16)", ["17,6 gam", "26,4 gam", "8,8 gam", "13,2 gam"], 0, "n acid = 12 / 60 = 0,2 mol; n rượu = 13,8 / 46 = 0,3 mol -> tính theo acid: n este lt = 0,2 mol -> m = 0,2 × 88 = 17,6 gam."),
        make_mc(12, "Vận dụng", "Hòa tan m gam hỗn hợp gồm ethylic alcohol và acetic acid tác dụng hoàn toàn với lượng dư NaHCO3 thu được 3,7185 lít khí CO2 ở đkc (24,79 L/mol). Khối lượng của acetic acid trong hỗn hợp là: (C=12, H=1, O=16)", ["9,0 gam", "6,0 gam", "12,0 gam", "4,5 gam"], 0, "nCO2 = 3,7185 / 24,79 = 0,15 mol -> n acid = 0,15 mol -> m acid = 0,15 × 60 = 9,0 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về phản ứng ester hóa:", [
            ("a", "Phản ứng giữa acid và rượu tạo este và nước gọi là phản ứng ester hóa.", True),
            ("b", "Acid sulfuric đặc đóng vai trò xúc tác và hút nước thúc đẩy cân bằng chuyển dịch theo chiều thuận.", True),
            ("c", "Ethyl acetate là hợp chất dễ bay hơi và có mùi thơm hoa quả.", True),
            ("d", "Phản ứng ester hóa xảy ra hoàn toàn một chiều tạo hiệu suất 100%.", False)
        ], "Phản ứng este hóa là phản ứng thuận nghịch hai chiều."),
        make_tf(2, "Thông hiểu", "So sánh 3 chất: C2H5OH, CH3COOH, CH3COOC2H5:", [
            ("a", "CH3COOH có nhiệt độ sôi cao nhất trong 3 chất.", True),
            ("b", "C2H5OH và CH3COOH đều tan vô hạn trong nước, còn CH3COOC2H5 ít tan trong nước.", True),
            ("c", "Cả 3 chất đều có khả năng làm quỳ tím hóa đỏ.", False),
            ("d", "C2H5OH và CH3COOH đều tác dụng được với kim loại Na giải phóng khí H2.", True)
        ], "Chỉ có CH3COOH làm quỳ tím hóa đỏ."),
        make_tf(3, "Vận dụng", "Thí nghiệm tách ethyl acetate sau phản ứng ester hóa:", [
            ("a", "Rót hỗn hợp sau phản ứng vào phễu chiết chứa dung dịch NaCl bão hòa.", True),
            ("b", "Chất lỏng tách thành 2 lớp: lớp trên là ethyl acetate, lớp dưới là dung dịch muối.", True),
            ("c", "Mở khóa phễu chiết để tháo bỏ lớp chất lỏng bên dưới, thu lấy lớp ester bên trên.", True),
            ("d", "Ethyl acetate chìm xuống đáy bình vì nặng hơn nước muối.", False)
        ], "Este nhẹ hơn nước muối nên nổi lên trên mặt."),
        make_tf(4, "Vận dụng", "Trong công nghiệp và đời sống:", [
            ("a", "Ester được ứng dụng nhiều làm hương liệu bánh kẹo, nước hoa và dung môi pha sơn.", True),
            ("b", "Xà phòng hóa ester của acid béo với glycerol thu được xà phòng và glycerol.", True),
            ("c", "Ester có thể uống thay nước lọc mà không gây nguy hiểm.", False),
            ("d", "Tơ axetat nhân tạo được sản xuất từ phản ứng giữa cellulose và acetic acid.", True)
        ], "Ester công nghiệp là dung môi hóa chất, không được uống.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Công thức phân tử của ethyl acetate là gì?", "C4H8O2", "C4H8O2."),
        make_sa(2, "Thông hiểu", "Mùi đặc trưng của ester ethyl acetate giống mùi của loại hoa quả nào?", "Chuối chín", "Chuối chín (hoặc hoa quả chín)."),
        make_sa(3, "Vận dụng", "Phân tử khối của ethyl acetate (CH3COOC2H5) là bao nhiêu amu?", "88", "88 amu."),
        make_sa(4, "Vận dụng", "Cho 0,1 mol CH3COOH phản ứng với lượng dư C2H5OH thu được 7,04 gam este. Hiệu suất phản ứng ester hóa là bao nhiêu %?", "80", "m lt = 0,1 × 88 = 8,8 gam -> H = 7,04 / 8,8 × 100% = 80%."),
        make_sa(5, "Vận dụng cao", "Hỗn hợp gồm 0,1 mol C2H5OH và 0,2 mol CH3COOH tác dụng với Na dư thu được bao nhiêu mol khí H2?", "0.15", "nH2 = 0,5 × 0,1 + 0,5 × 0,2 = 0,15 mol."),
        make_sa(6, "Vận dụng cao", "Thủy phân hoàn toàn 8,8 gam ethyl acetate bằng lượng vừa đủ dung dịch NaOH. Khối lượng muối CH3COONa thu được là bao nhiêu gam? (C=12, H=1, O=16, Na=23)", "8.2", "n = 8,8 / 88 = 0,1 mol -> m muối = 0,1 × 82 = 8,2 gam.")
    ],
    p4=[
        make_vdc(1, "Một hỗn hợp X gồm ethylic alcohol và acetic acid có khối lượng 10,6 gam. Cho hỗn hợp X tác dụng hết với lượng dư Na2CO3 thu được 1,2395 lít khí CO2 ở đkc (24,79 L/mol). Phần trăm khối lượng của ethylic alcohol trong hỗn hợp X là: (C=12, H=1, O=16)", ["43,40%", "56,60%", "50,00%", "35,00%"], 0, "nCO2 = 1,2395 / 24,79 = 0,05 mol -> n acid = 0,05 × 2 = 0,1 mol -> m acid = 0,1 × 60 = 6,0 gam -> m rượu = 10,6 - 6,0 = 4,6 gam -> %m rượu = 4,6 / 10,6 × 100% ≈ 43,40%."),
        make_vdc(2, "Đun sôi hỗn hợp gồm 18 gam acetic acid và 13,8 gam ethylic alcohol có xúc tác H2SO4 đặc một thời gian. Sau khi phản ứng đạt trạng thái cân bằng, làm nguội rồi trung hòa lượng acid còn dư bằng dung dịch NaOH 1M thấy tiêu tốn hết 100 mL dung dịch NaOH. Khối lượng ester ethyl acetate tạo thành là: (C=12, H=1, O=16)", ["17,6 gam", "8,8 gam", "13,2 gam", "22,0 gam"], 0, "n acid ban đầu = 18 / 60 = 0,3 mol; n rượu ban đầu = 13,8 / 46 = 0,3 mol. n acid dư = nNaOH = 0,1 × 1 = 0,1 mol -> n acid pư = 0,3 - 0,1 = 0,2 mol. Do đó n este = 0,2 mol -> m este = 0,2 × 88 = 17,6 gam."),
        make_vdc(3, "Để phân biệt 4 ống nghiệm không dán nhãn chứa các chất lỏng riêng biệt gồm: benzen, ethylic alcohol, acetic acid và dung dịch glucose, phương pháp nhận biết tối ưu là:", ["Dùng giấy quỳ tím, nước cất và dung dịch AgNO3 trong NH3 đun nóng", "Chỉ dùng kim loại natri", "Chỉ dùng dung dịch nước bromine", "Dùng quỳ tím và bột đồng"], 0, "Dùng quỳ tím nhận biết acetic acid (hóa đỏ); Cho nước cất vào 3 chất còn lại nhận biết benzen (không tan tách lớp); Dùng AgNO3/NH3 đun nóng nhận biết glucose (tráng bạc Ag); chất còn lại là ethylic alcohol."),
        make_vdc(4, "Một este no đơn chức mạch hở E được tạo thành từ một alcohol no đơn chức và một acid no đơn chức. Đốt cháy hoàn toàn 0,1 mol E thu được 0,3 mol CO2 và 0,3 mol H2O. Tên gọi của este E là:", ["Methyl acetate hoặc Ethyl formate", "Ethyl acetate", "Propyl acetate", "Methyl propionate"], 0, "nCO2 = 0,3 mol -> Số C = 0,3 / 0,1 = 3 -> Este có CTPT là C3H6O2. Các đồng phân este là CH3COOCH3 (methyl acetate) hoặc HCOOC2H5 (ethyl formate).")
    ]
)

# --- ĐỀ TỔNG HỢP 4: Bài toán hỗn hợp Rượu và Acid nâng cao ---
exams_c3[f"{LID_REV3}_test4"] = make_exam(
    CID, CTITLE, LID_REV3, LNAME_REV3, 4,
    p1=[
        make_mc(1, "Nhận biết", "Cho kim loại natri vào cốc chứa ethylic alcohol nguyên chất, phản ứng sinh ra khí nào?", ["Khí hydrogen (H2)", "Khí CO2", "Khí methane", "Khí oxy"], 0, "Khí H2."),
        make_mc(2, "Nhận biết", "Chất nào sau đây phản ứng được với dung dịch CaCO3 giải phóng khí CO2?", ["Acetic acid", "Ethylic alcohol", "Ethyl acetate", "Benzene"], 0, "Acetic acid."),
        make_mc(3, "Nhận biết", "Phản ứng ester hóa giữa CH3COOH và C2H5OH tạo thành nước và chất nào?", ["CH3COOC2H5", "CH3COOCH3", "C2H5OC2H5", "CH3CHO"], 0, "CH3COOC2H5 (ethyl acetate)."),
        make_mc(4, "Nhận biết", "Chất nào sau đây có nhiệt độ sôi cao nhất?", ["Acetic acid (118 °C)", "Ethylic alcohol (78,3 °C)", "Nước (100 °C)", "Ethyl acetate (77 °C)"], 0, "Acetic acid sôi ở 118 °C."),
        make_mc(5, "Nhận biết", "Giấm ăn chứa acid nào sau đây?", ["Acetic acid", "Formic acid", "Oxalic acid", "Benzoic acid"], 0, "Acetic acid."),
        make_mc(6, "Nhận biết", "Dung dịch nào sau đây làm đổi màu quỳ tím thành đỏ nhạt?", ["CH3COOH", "C2H5OH", "NaCl", "C6H12O6"], 0, "CH3COOH là acid."),
        make_mc(7, "Thông hiểu", "Cho hỗn hợp gồm C2H5OH và CH3COOH tác dụng với dung dịch NaHCO3 dư, chất nào tham gia phản ứng?", ["Chỉ có CH3COOH", "Chỉ có C2H5OH", "Cả hai chất", "Không có chất nào"], 0, "Chỉ có acid tác dụng với muối carbonate/bicarbonate."),
        make_mc(8, "Thông hiểu", "Khí sinh ra khi cho hỗn hợp C2H5OH và CH3COOH tác dụng với kim loại Na dư là:", ["Khí H2", "Khí CO2", "Hỗn hợp H2 và CO2", "Khí O2"], 0, "Cả hai chất đều có H linh động giải phóng khí H2."),
        make_mc(9, "Thông hiểu", "Để trung hòa dung dịch chứa 0,1 mol acetic acid cần vừa đủ bao nhiêu gam NaOH? (Na=23, O=16, H=1)", ["4 gam", "8 gam", "2 gam", "6 gam"], 0, "mNaOH = 0,1 × 40 = 4 gam."),
        make_mc(10, "Thông hiểu", "Ester ethyl acetate có đặc điểm nào sau đây?", ["Ít tan trong nước, nhẹ hơn nước và có mùi thơm hoa quả", "Tan vô hạn trong nước", "Có vị chua gắt", "Làm quỳ tím hóa xanh"], 0, "Ethyl acetate thơm, ít tan và nhẹ hơn nước."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 15,2 gam hỗn hợp gồm C2H5OH và CH3COOH tác dụng hết với Na dư thu được 3,7185 lít khí H2 ở đkc (24,79 L/mol). Khối lượng của CH3COOH trong hỗn hợp là: (C=12, H=1, O=16)", ["6,0 gam", "9,2 gam", "12,0 gam", "4,6 gam"], 0, "nH2 = 0,15 mol -> n rượu + n acid = 0,3 mol. 46x + 60y = 15,2 và x + y = 0,3 -> 14y = 1,4 -> y = 0,1 mol (CH3COOH: 6,0 g); x = 0,2 mol (C2H5OH: 9,2 g)."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn 0,1 mol acetic acid (C2H4O2). Thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "C2H4O2 + 2O2 -> 2CO2 + 2H2O. nCO2 = 0,2 mol -> V = 0,2 × 24,79 = 4,958 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét phản ứng của hỗn hợp rượu và acid:", [
            ("a", "Cho hỗn hợp tác dụng với kim loại Na, cả rượu và acid đều tham gia phản ứng giải phóng H2.", True),
            ("b", "Cho hỗn hợp tác dụng với dung dịch Na2CO3, chỉ có acid phản ứng sủi bọt khí CO2.", True),
            ("c", "Cho hỗn hợp tác dụng với dung dịch NaOH đun nóng, cả hai chất đều bị trung hòa.", False),
            ("d", "Đun nóng hỗn hợp có mặt H2SO4 đặc sẽ xảy ra phản ứng ester hóa.", True)
        ], "Rượu không phản ứng với dung dịch NaOH."),
        make_tf(2, "Thông hiểu", "Về các sản phẩm tạo thành:", [
            ("a", "Phản ứng của rượu với Na tạo muối sodium ethoxide (C2H5ONa).", True),
            ("b", "Phản ứng của acid với Na tạo muối sodium acetate (CH3COONa).", True),
            ("c", "Muối sodium acetate tan tốt trong nước tạo dung dịch có môi trường kiềm yếu.", True),
            ("d", "Ethyl acetate tan vô hạn trong nước tạo dung dịch đồng nhất.", False)
        ], "Ethyl acetate ít tan trong nước, tách thành lớp nổi lên trên."),
        make_tf(3, "Vận dụng", "Trong một bài toán phân tích hỗn hợp hữu cơ:", [
            ("a", "Số mol CO2 sinh ra khi cho hỗn hợp tác dụng với NaHCO3 đúng bằng số mol acid acetic.", True),
            ("b", "Số mol H2 sinh ra khi cho hỗn hợp tác dụng với Na bằng một nửa tổng số mol của rượu và acid.", True),
            ("c", "Đốt cháy hoàn toàn hỗn hợp rượu và acid luôn thu được nCO2 > nH2O.", False),
            ("d", "Có thể xác định chính xác số mol từng chất trong hỗn hợp dựa vào 2 phản ứng trên.", True)
        ], "Cả rượu và acid đều có số H > 2 lần số C nên nH2O > nCO2."),
        make_tf(4, "Vận dụng", "Về phản ứng ester hóa nâng cao:", [
            ("a", "Nếu dùng 1 mol rượu và 1 mol acid thì lượng ester tối đa thu được ở trạng thái cân bằng thường đạt khoảng 2/3 mol (khoảng 66,7%).", True),
            ("b", "Tăng nồng độ acid hoặc rượu sẽ làm cân bằng chuyển dịch theo chiều tạo thêm ester.", True),
            ("c", "Chưng cất tách bớt ester và nước ra khỏi hệ sẽ làm cân bằng chuyển dịch theo chiều nghịch.", False),
            ("d", "Chất xúc tác H2SO4 đặc chỉ làm tăng tốc độ phản ứng mà không bị tiêu hao sau phản ứng.", True)
        ], "Tách ester ra khỏi hệ thúc đẩy cân bằng chuyển dịch theo chiều thuận tạo thêm ester.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Khí nào thoát ra khi cho acetic acid tác dụng với muối NaHCO3?", "CO2", "Carbon dioxide (CO2)."),
        make_sa(2, "Thông hiểu", "Khi cho hỗn hợp C2H5OH và CH3COOH vào dung dịch NaOH, chất nào phản ứng?", "CH3COOH", "Acetic acid (CH3COOH)."),
        make_sa(3, "Vận dụng", "Cần bao nhiêu mol NaOH để phản ứng vừa đủ với hỗn hợp gồm 0,1 mol C2H5OH và 0,1 mol CH3COOH?", "0.1", "0,1 mol (chỉ có CH3COOH phản ứng)."),
        make_sa(4, "Vận dụng", "Đốt cháy hoàn toàn 0,1 mol ethyl acetate thu được bao nhiêu mol CO2?", "0.4", "CH3COOC2H5 (C4H8O2) -> 4CO2. 0,1 × 4 = 0,4 mol."),
        make_sa(5, "Vận dụng cao", "Cho hỗn hợp gồm 0,2 mol C2H5OH và 0,1 mol CH3COOH tác dụng với Na dư. Thể tích khí H2 sinh ra ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "3.72", "nH2 = 0,5 × 0,2 + 0,5 × 0,1 = 0,15 mol -> V = 0,15 × 24,79 = 3,7185 ≈ 3,72 lít."),
        make_sa(6, "Vận dụng cao", "Cho m gam acetic acid tác dụng với lượng dư NaHCO3 thu được 0,2 mol CO2. Giá trị của m là bao nhiêu gam? (C=12, H=1, O=16)", "12", "n acid = nCO2 = 0,2 mol -> m = 0,2 × 60 = 12 gam.")
    ],
    p4=[
        make_vdc(1, "Cho 16,6 gam hỗn hợp X gồm ethylic alcohol và acetic acid tác dụng vừa đủ với 200 mL dung dịch NaOH 1M. Khối lượng của ethylic alcohol có trong hỗn hợp X là: (C=12, H=1, O=16)", ["4,6 gam", "9,2 gam", "6,0 gam", "12,0 gam"], 0, "Chỉ có acid tác dụng với NaOH: nNaOH = 0,2 × 1 = 0,2 mol -> n acid = 0,2 mol -> m acid = 0,2 × 60 = 12 gam. m rượu = 16,6 - 12 = 4,6 gam."),
        make_vdc(2, "Cho m gam hỗn hợp X gồm C2H5OH và CH3COOH chia làm 2 phần bằng nhau: Phần 1 tác dụng với Na dư thu được 4,958 lít khí H2 ở đkc (24,79 L/mol). Phần 2 đem đun nóng với H2SO4 đặc xúc tác thu được 14,08 gam ethyl acetate (hiệu suất phản ứng đạt 80%). Giá trị của m là:", ["30,4 gam", "15,2 gam", "21,2 gam", "42,4 gam"], 0, "n este = 14,08 / 88 = 0,16 mol. Với H=80% -> n phản ứng = 0,16 / 0,8 = 0,2 mol. Vậy trong mỗi phần có n acid = 0,2 mol (chất phản ứng hết). Ở phần 1: nH2 = 4,958 / 24,79 = 0,2 mol = 0,5 n rượu + 0,5 n acid -> 0,5 n rượu + 0,1 = 0,2 -> n rượu = 0,2 mol. m mỗi phần = 0,2 × 46 + 0,2 × 60 = 9,2 + 12 = 21,2 gam -> m cả 2 phần = 21,2 × 2 = 42,4 gam? Nếu n acid = 0,2 mol, n rượu = 0,2 mol thì m mỗi phần = 21,2 gam -> m = 42,4 gam."),
        make_vdc(3, "Để phân biệt 3 chất lỏng riêng biệt gồm: dung dịch acetic acid, ethylic alcohol và nước cất, phương pháp hóa học nào sau đây là đơn giản nhất?", ["Nhúng giấy quỳ tím vào 3 mẫu thử: mẫu làm quỳ tím hóa đỏ là acetic acid. Cho mẩu natri vào 2 mẫu còn lại: mẫu phản ứng mãnh liệt là nước cất, phản ứng êm dịu là ethylic alcohol", "Dùng bột đá vôi và đun sôi", "Chỉ ngửi mùi", "Đốt cháy từng mẫu"], 0, "Dùng quỳ tím nhận biết ngay acetic acid; phân biệt nước và cồn bằng tốc độ phản ứng với Na."),
        make_vdc(4, "Một este E có công thức phân tử C3H6O2 khi đun nóng với dung dịch NaOH thu được muối sodium acetate (CH3COONa) và một alcohol X. Công thức cấu tạo của este E và alcohol X lần lượt là:", ["CH3COOCH3 và CH3OH", "HCOOC2H5 và C2H5OH", "CH3COOC2H5 và C2H5OH", "HCOOCH3 và CH3OH"], 0, "CH3COONa có gốc acid là CH3COO-, este có 3 C nên gốc alcohol là -CH3 -> este là CH3COOCH3 (methyl acetate) và alcohol X là CH3OH (methanol).")
    ]
)

# --- ĐỀ TỔNG HỢP 5: Đề tổng kết nâng cao toàn diện Chương III ---
exams_c3[f"{LID_REV3}_test5"] = make_exam(
    CID, CTITLE, LID_REV3, LNAME_REV3, 5,
    p1=[
        make_mc(1, "Nhận biết", "Chất nào sau đây phản ứng được với kim loại natri giải phóng khí H2?", ["Cả ethylic alcohol và acetic acid", "Chỉ có ethylic alcohol", "Chỉ có acetic acid", "Chỉ có ethyl acetate"], 0, "Cả hai đều có nhóm -OH chứa H linh động."),
        make_mc(2, "Nhận biết", "Dung dịch chất hữu cơ nào sau đây có khả năng hòa tan bột đồng(II) oxide (CuO) đun nóng tạo dung dịch màu xanh lam?", ["Acetic acid (CH3COOH)", "Ethylic alcohol (C2H5OH)", "Ethyl acetate (CH3COOC2H5)", "Methane (CH4)"], 0, "CH3COOH hòa tan CuO tạo muối đồng acetate màu xanh lam."),
        make_mc(3, "Nhận biết", "Dung dịch acetic acid phản ứng được với kim loại nào sau đây?", ["Sắt (Fe)", "Đồng (Cu)", "Bạc (Ag)", "Vàng (Au)"], 0, "Fe đứng trước H."),
        make_mc(4, "Nhận biết", "Phản ứng giữa acetic acid và ethylic alcohol sinh ra chất nào có mùi thơm hoa quả?", ["Ethyl acetate", "Methyl acetate", "Ethylene", "Methane"], 0, "Ethyl acetate."),
        make_mc(5, "Nhận biết", "Lên men giấm là quá trình oxy hóa chất nào thành acetic acid?", ["Ethylic alcohol", "Glucose", "Methane", "Ethylene"], 0, "C2H5OH oxy hóa thành CH3COOH."),
        make_mc(6, "Nhận biết", "Độ cồn của một dung dịch rượu cho biết:", ["Số mililít ethylic alcohol nguyên chất trong 100 mL dung dịch", "Số gam rượu trong 1 lít", "Nhiệt độ sôi của rượu", "Độ chua của rượu"], 0, "Số mL cồn nguyên chất trong 100 mL dung dịch."),
        make_mc(7, "Thông hiểu", "Sắp xếp theo thứ tự nhiệt độ sôi tăng dần của các chất: CH4, C2H5OH, CH3COOH:", ["CH4 < C2H5OH < CH3COOH", "CH3COOH < C2H5OH < CH4", "CH4 < CH3COOH < C2H5OH", "C2H5OH < CH4 < CH3COOH"], 0, "CH4 (-161,5 °C) < C2H5OH (78,3 °C) < CH3COOH (118 °C)."),
        make_mc(8, "Thông hiểu", "Dẫn khí thoát ra khi cho mẩu đá vôi vào giấm ăn qua dung dịch Ca(OH)2 dư, hiện tượng quan sát được là:", ["Xuất hiện kết tủa trắng làm đục nước vôi trong", "Không có hiện tượng gì", "Dung dịch đổi màu xanh", "Có kết tủa đỏ"], 0, "Khí CO2 tạo kết tủa trắng CaCO3."),
        make_mc(9, "Thông hiểu", "Chất nào sau đây KHÔNG tan vô hạn trong nước ở điều kiện thường?", ["Ethyl acetate", "Ethylic alcohol", "Acetic acid", "Glycerol"], 0, "Ethyl acetate ít tan trong nước, nổi lên trên."),
        make_mc(10, "Thông hiểu", "Để nhận biết 2 chất lỏng không màu gồm C2H5OH và CH3COOH chỉ cần dùng một thuốc thử duy nhất là:", ["Giấy quỳ tím", "Nước cất", "Dung dịch NaCl", "Kim loại natri"], 0, "Quỳ tím hóa đỏ nhận biết CH3COOH, C2H5OH không đổi màu."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 4,6 gam ethylic alcohol và 6,0 gam acetic acid. Tổng số mol khí CO2 thu được là: (C=12, H=1, O=16)", ["0,4 mol", "0,2 mol", "0,3 mol", "0,5 mol"], 0, "n rượu = 4,6 / 46 = 0,1 mol -> nCO2 = 0,2 mol. n acid = 6,0 / 60 = 0,1 mol -> nCO2 = 0,2 mol. Tổng nCO2 = 0,2 + 0,2 = 0,4 mol."),
        make_mc(12, "Vận dụng", "Hòa tan hoàn toàn 5,6 gam bột Fe vào lượng dư dung dịch CH3COOH. Thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là: (Fe=56)", ["2,479 lít", "4,958 lít", "1,2395 lít", "3,7185 lít"], 0, "nFe = 0,1 mol -> nH2 = 0,1 mol -> V = 0,1 × 24,79 = 2,479 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét toàn diện về ethylic alcohol và acetic acid:", [
            ("a", "Cả ethylic alcohol và acetic acid đều có phân tử chứa nhóm chức có nguyên tử oxygen.", True),
            ("b", "Ethylic alcohol chứa nhóm -OH, acetic acid chứa nhóm -COOH.", True),
            ("c", "Cả hai chất đều phản ứng được với dung dịch kiềm NaOH.", False),
            ("d", "Cả hai chất đều tan vô hạn trong nước.", True)
        ], "Ethylic alcohol không phản ứng với NaOH."),
        make_tf(2, "Thông hiểu", "Về phản ứng hóa học đặc trưng:", [
            ("a", "Acetic acid tác dụng với kim loại đứng trước H giải phóng khí H2.", True),
            ("b", "Ethylic alcohol phản ứng với Na giải phóng khí H2.", True),
            ("c", "Phản ứng ester hóa giữa alcohol và acid là phản ứng một chiều hoàn toàn.", False),
            ("d", "Lên men giấm là quá trình oxy hóa ethylic alcohol bằng oxy không khí.", True)
        ], "Phản ứng este hóa là phản ứng thuận nghịch hai chiều."),
        make_tf(3, "Vận dụng", "Về tác động sức khỏe và bảo quản hóa chất hữu cơ:", [
            ("a", "Rượu bia lạm dụng gây tổn hại nghiêm trọng cho gan và hệ thần kinh.", True),
            ("b", "Giấm ăn được dùng làm gia vị, bảo quản thực phẩm và tẩy cặn đá vôi.", True),
            ("c", "Ester ethyl acetate được ứng dụng làm dung môi hòa tan và hương liệu.", True),
            ("d", "Cồn công nghiệp methanol có thể dùng để ngâm rượu uống an toàn.", False)
        ], "Methanol cực độc gây mù mắt và tử vong."),
        make_tf(4, "Vận dụng", "Phân biệt 3 chất lỏng: CH3COOH, C2H5OH và CH3COOC2H5:", [
            ("a", "Dùng quỳ tím nhận biết được CH3COOH vì quỳ tím hóa đỏ.", True),
            ("b", "Dùng kim loại Na nhận biết được C2H5OH vì có bọt khí H2 thoát ra.", True),
            ("c", "Chất còn lại là CH3COOC2H5 không làm đỏ quỳ tím và không phản ứng với Na.", True),
            ("d", "Không thể phân biệt được 3 chất này nếu không dùng máy quang phổ.", False)
        ], "Dễ dàng nhận biết bằng phương pháp hóa học thông thường.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Phân tử ethylic alcohol có bao nhiêu nguyên tử carbon?", "2", "2 nguyên tử C (C2H6O)."),
        make_sa(2, "Thông hiểu", "Hợp chất hữu cơ nào có công thức CH3COOC2H5?", "Ethyl acetate", "Ethyl acetate."),
        make_sa(3, "Vận dụng", "Khối lượng mol phân tử của acetic acid (CH3COOH) là bao nhiêu g/mol?", "60", "60 g/mol."),
        make_sa(4, "Vận dụng", "Đốt cháy 0,1 mol ethylic alcohol cần bao nhiêu mol khí O2?", "0.3", "0,3 mol."),
        make_sa(5, "Vận dụng cao", "Lên men 18 gam glucose (C6H12O6) thành ethylic alcohol với hiệu suất 100%. Khối lượng cồn thu được là bao nhiêu gam? (C=12, H=1, O=16)", "9.2", "n = 0,1 mol -> n cồn = 0,2 mol -> m = 0,2 × 46 = 9,2 gam."),
        make_sa(6, "Vận dụng cao", "Đun nóng 0,1 mol CH3COOH với lượng dư C2H5OH thu được 6,6 gam ethyl acetate. Hiệu suất phản ứng ester hóa là bao nhiêu %?", "75", "m lt = 0,1 × 88 = 8,8 gam -> H = 6,6 / 8,8 × 100% = 75%.")
    ],
    p4=[
        make_vdc(1, "Cho 21,2 gam hỗn hợp X gồm C2H5OH và CH3COOH tác dụng hoàn toàn với lượng dư dung dịch NaHCO3 thu được 4,958 lít khí CO2 ở đkc (24,79 L/mol). Phần trăm khối lượng của C2H5OH trong hỗn hợp X là: (C=12, H=1, O=16)", ["43,40%", "56,60%", "50,00%", "35,00%"], 0, "nCO2 = 4,958 / 24,79 = 0,2 mol -> n acid = 0,2 mol -> m acid = 0,2 × 60 = 12,0 gam -> m rượu = 21,2 - 12,0 = 9,2 gam -> %m rượu = 9,2 / 21,2 × 100% ≈ 43,40%."),
        make_vdc(2, "Lên men m gam glucose thành ethylic alcohol với hiệu suất 80%. Toàn bộ lượng khí CO2 sinh ra được dẫn vào bình đựng dung dịch nước vôi trong Ca(OH)2 dư thu được 40 gam kết tủa trắng CaCO3. Giá trị của m là: (C=12, H=1, O=16, Ca=40)", ["45 gam", "36 gam", "50 gam", "40 gam"], 0, "nCaCO3 = 40 / 100 = 0,4 mol -> nCO2 = 0,4 mol -> n glucose lí thuyết = 0,4 / 2 = 0,2 mol. Do hiệu suất H=80% -> n glucose thực tế = 0,2 / 0,8 = 0,25 mol -> m = 0,25 × 180 = 45 gam."),
        make_vdc(3, "Đun nóng 12 gam acetic acid với 11,5 gam ethylic alcohol có mặt H2SO4 đặc xúc tác đến khi phản ứng đạt trạng thái cân bằng thì thu được 11,44 gam ester ethyl acetate. Hiệu suất của phản ứng ester hóa là: (C=12, H=1, O=16)", ["65%", "70%", "60%", "75%"], 0, "n acid = 12 / 60 = 0,2 mol; n rượu = 11,5 / 46 = 0,25 mol -> tính theo acid: n este lí thuyết = 0,2 mol -> m este lí thuyết = 0,2 × 88 = 17,6 gam. n este thực tế = 11,44 / 88 = 0,13 mol -> H = 11,44 / 17,6 × 100% = 65%."),
        make_vdc(4, "Một người uống 100 mL rượu vang 12° (khối lượng riêng của cồn nguyên chất là 0,8 g/mL). Toàn bộ lượng cồn này được hấp thụ vào máu. Biết lượng máu của người này là 5 lít. Nồng độ cồn tối đa tức thời trong máu (giả thiết cồn phân bố đều vào toàn bộ máu trước khi bị gan chuyển hóa) là:", ["1,92 mg/mL", "2,40 mg/mL", "1,50 mg/mL", "0,96 mg/mL"], 0, "V cồn = 100 × 12% = 12 mL -> m cồn = 12 × 0,8 = 9,6 gam = 9 600 mg. Nồng độ trong máu = 9 600 mg / 5 000 mL = 1,92 mg/mL (mức nồng độ rất cao, nguy cơ ngộ độc rượu nặng).")
    ]
)
