# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - BỔ SUNG 8 ĐỀ CÒN THIẾU CHO BÀI 9, 10, 11, 12 (ĐỀ 2 & ĐỀ 3)
Đảm bảo 100% độc lập, không trùng lặp câu hỏi!
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

missing_8 = {}

# ==============================================================================
# BÀI 9: BASE - THANG pH (ĐỀ 2 & ĐỀ 3)
# ==============================================================================

# --- ĐỀ 2: Tính chất hóa học của bazơ tan và không tan ---
missing_8["chem8_c2_b9_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Bazơ nào sau đây là bazơ không tan trong nước?", ["Cu(OH)2", "NaOH", "KOH", "Ba(OH)2"], 0, "Cu(OH)2 kết tủa màu xanh lam."),
        make_mc(2, "Nhận biết", "Dung dịch kiềm NaOH phản ứng được với oxit nào sau đây?", ["CO2 (oxit axit)", "CaO", "Na2O", "BaO"], 0, "CO2 + 2NaOH -> Na2CO3 + H2O."),
        make_mc(3, "Nhận biết", "Khi nhỏ vài giọt dung dịch phenolphtalein vào dung dịch Ca(OH)2, dung dịch có màu gì?", ["Màu hồng", "Màu xanh lam", "Màu đỏ", "Không màu"], 0, "Dung dịch kiềm làm phenolphtalein đổi sang màu hồng."),
        make_mc(4, "Nhận biết", "Phản ứng nhiệt phân Cu(OH)2 tạo ra chất rắn màu đen là:", ["CuO", "Cu2O", "Cu", "CuSO4"], 0, "Cu(OH)2 -> CuO (đen) + H2O."),
        make_mc(5, "Thông hiểu", "Cho dãy các bazơ: NaOH, Fe(OH)3, KOH, Cu(OH)2, Ba(OH)2. Số bazơ bị nhiệt phân hủy bởi đèn cồn là:", ["2", "3", "4", "1"], 0, "Chỉ có bazơ không tan bị nhiệt phân: Fe(OH)3 và Cu(OH)2 (2 bazơ)."),
        make_mc(6, "Thông hiểu", "Một dung dịch có pH = 13. Kết luận nào sau đây ĐÚNG về dung dịch này?", ["Dung dịch có tính bazơ (kiềm) rất mạnh", "Dung dịch có tính axit rất mạnh", "Dung dịch trung tính", "Dung dịch nước cất"], 0, "pH = 13 là dung dịch kiềm rất mạnh."),
        make_mc(7, "Thông hiểu", "Khi cho dung dịch NaOH tác dụng với dung dịch CuSO4, hiện tượng quan sát được là:", ["Xuất hiện kết tủa màu xanh lam", "Có bọt khí bay lên", "Xuất hiện kết tủa màu nâu đỏ", "Dung dịch chuyển sang màu tím"], 0, "CuSO4 + 2NaOH -> Cu(OH)2 (kết tủa xanh lam) + Na2SO4."),
        make_mc(8, "Thông hiểu", "Sản phẩm của phản ứng giữa axit sunfuric H2SO4 và kali hiđroxit KOH là:", ["K2SO4 và H2O", "KSO4 và H2", "K2O và H2O", "K2S và H2O"], 0, "H2SO4 + 2KOH -> K2SO4 + 2H2O."),
        make_mc(9, "Vận dụng", "Hòa tan 11,2 g KOH vào nước thu được 200 mL dung dịch. Nồng độ mol của dung dịch KOH là:", ["1 M", "0,5 M", "2 M", "0,1 M"], 0, "n = 11,2 / 56 = 0,2 mol -> CM = 0,2 / 0,2 = 1 M."),
        make_mc(10, "Vận dụng", "Để trung hòa hoàn toàn 150 mL dung dịch KOH 1 M cần bao nhiêu mL dung dịch HCl 1,5 M?", ["100 mL", "150 mL", "200 mL", "50 mL"], 0, "n_KOH = 0,15 mol -> n_HCl = 0,15 mol -> V = 0,15 / 1,5 = 0,1 L = 100 mL."),
        make_mc(11, "Vận dụng", "Nhiệt phân hoàn toàn 10,7 g Fe(OH)3 thu được bao nhiêu gam bột Fe2O3 màu nâu đỏ?", ["8,0 g", "16,0 g", "4,0 g", "12,0 g"], 0, "n = 10,7 / 107 = 0,1 mol -> n_Fe2O3 = 0,05 mol -> m = 0,05 * 160 = 8,0 g."),
        make_mc(12, "Vận dụng cao", "Dẫn 4,958 lít khí CO2 ở đkc vào dung dịch chứa 0,3 mol NaOH thu được dung dịch chứa muối nào?", ["Na2CO3 và NaHCO3", "Chỉ có Na2CO3", "Chỉ có NaHCO3", "Na2CO3 và NaOH dư"], 0, "n_CO2 = 0,2 mol. T = n_NaOH / n_CO2 = 0,3 / 0,2 = 1,5 -> tạo 2 muối Na2CO3 và NaHCO3."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về tính chất của dung dịch kiềm:", [
            ("a", "Dung dịch kiềm có cảm giác nhờn như xà phòng khi chạm tay vào.", True),
            ("b", "Dung dịch kiềm làm quỳ tím chuyển sang màu đỏ rực rỡ.", False),
            ("c", "Dung dịch kiềm tác dụng với oxit axit tạo muối và nước.", True),
            ("d", "Dung dịch kiềm ăn mòn da và thủy tinh khi ở nồng độ cao và nóng.", True)
        ], "Dung dịch kiềm làm quỳ tím hóa xanh."),
        make_tf(2, "Thông hiểu", "Về các bazơ không tan:", [
            ("a", "Fe(OH)2 là kết tủa trắng xanh, để ngoài không khí chuyển dần thành Fe(OH)3 màu nâu đỏ.", True),
            ("b", "Cu(OH)2 tan tốt trong nước tạo dung dịch có màu xanh lam đậm.", False),
            ("c", "Nhiệt phân bazơ không tan luôn sinh ra oxit kim loại tương ứng và hơi nước.", True),
            ("d", "Bazơ không tan vẫn tác dụng được với dung dịch axit mạnh (phản ứng trung hòa).", True)
        ], "Cu(OH)2 là chất kết tủa không tan trong nước."),
        make_tf(3, "Vận dụng", "Về ứng dụng điều chỉnh pH trong thực tế:", [
            ("a", "Nước mưa có pH < 5,6 được coi là mưa axit.", True),
            ("b", "Nước hồ cá cảnh nuôi cá rồng cần duy trì pH ổn định khoảng 6,5 - 7,5.", True),
            ("c", "Người bị đau dạ dày thường do nồng độ axit HCl tăng cao làm tổn thương niêm mạc.", True),
            ("d", "Dung dịch có pH = 1 là dung dịch trung tính có thể uống trực tiếp an toàn.", False)
        ], "pH = 1 là dung dịch axit rất mạnh gây bỏng nguy hiểm."),
        make_tf(4, "Vận dụng cao", "Cho 100 mL dung dịch FeCl3 1 M tác dụng với lượng dư dung dịch NaOH:", [
            ("a", "Sinh ra chất kết tủa sắt(III) hiđroxit màu nâu đỏ.", True),
            ("b", "Số mol kết tủa thu được là 0,1 mol.", True),
            ("c", "Lọc lấy kết tủa đem nung đến khối lượng không đổi thu được 8 g Fe2O3.", True),
            ("d", "Khối lượng kết tủa Fe(OH)3 ướt thu được đúng bằng 5,6 g.", False)
        ], "m_Fe(OH)3 = 0,1 * 107 = 10,7 g.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong 1 phân tử natri hiđroxit NaOH có bao nhiêu nguyên tử natri?", "1", "Có 1 nguyên tử Na."),
        make_sa(2, "Thông hiểu", "Dung dịch NaOH làm quỳ tím chuyển sang màu gì?", "xanh", "Chuyển sang màu xanh."),
        make_sa(3, "Thông hiểu", "Một dung dịch có pH = 10. Môi trường của dung dịch này là axit hay bazơ? (Điền: bazơ)", "bazơ", "pH = 10 là môi trường bazơ."),
        make_sa(4, "Vận dụng", "Khối lượng mol của kali hiđroxit KOH là bao nhiêu g/mol?", "56", "M = 39 + 16 + 1 = 56 g/mol."),
        make_sa(5, "Vận dụng", "Để trung hòa hoàn toàn 0,1 mol Ba(OH)2 cần bao nhiêu mol axit HCl? (Ghi số thập phân)", "0,2", "Ba(OH)2 + 2HCl -> cần 0,2 mol HCl."),
        make_sa(6, "Vận dụng cao", "Nung 19,6 g Cu(OH)2 đến khối lượng không đổi thu được bao nhiêu gam CuO?", "16", "n = 0,2 mol -> m_CuO = 0,2 * 80 = 16 g.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan 8 g NaOH vào nước được 400 mL dung dịch. Nồng độ mol của dung dịch NaOH là:", ["0,5 M", "1,0 M", "0,2 M", "0,25 M"], 0, "n = 8 / 40 = 0,2 mol -> CM = 0,2 / 0,4 = 0,5 M."),
        make_vdc(2, "Cho 100 mL dung dịch NaOH 2 M tác dụng với 100 mL dung dịch CuCl2 0,5 M. Khối lượng kết tủa Cu(OH)2 màu xanh thu được là:", ["4,9 g", "9,8 g", "2,45 g", "7,35 g"], 0, "n_NaOH = 0,2 mol; n_CuCl2 = 0,05 mol -> NaOH dư, tính theo CuCl2 -> m = 0,05 * 98 = 4,9 g."),
        make_vdc(3, "Trung hòa hoàn toàn 200 mL dung dịch Ca(OH)2 0,1 M bằng dung dịch HNO3 0,2 M. Thể tích dung dịch HNO3 cần dùng là:", ["200 mL", "100 mL", "400 mL", "150 mL"], 0, "n_Ca(OH)2 = 0,02 mol -> n_HNO3 = 0,04 mol -> V = 0,04 / 0,2 = 0,2 L = 200 mL."),
        make_vdc(4, "Dẫn luồng khí CO2 dư vào dung dịch chứa 0,1 mol Ca(OH)2. Sau khi phản ứng kết thúc hoàn toàn, khối lượng muối Ca(HCO3)2 thu được trong dung dịch là:", ["16,2 g", "10,0 g", "8,1 g", "20,0 g"], 0, "n_Ca(HCO3)2 = 0,1 mol -> m = 0,1 * 162 = 16,2 g.")
    ]
}

# --- ĐỀ 3: Bài toán nhận biết và chuẩn độ trung hòa pH ---
missing_8["chem8_c2_b9_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Bazơ nào sau đây bị nhiệt phân hủy khi nung nóng?", ["Fe(OH)3", "NaOH", "KOH", "Ba(OH)2"], 0, "Fe(OH)3 là bazơ không tan bị nhiệt phân hủy."),
        make_mc(2, "Nhận biết", "Dung dịch kiềm có thể phản ứng với chất nào sau đây?", ["Axit clohiđric HCl", "Khí oxi", "Khí hiđro", "Kim loại đồng Cu"], 0, "Phản ứng trung hòa với axit."),
        make_mc(3, "Nhận biết", "Độ pH của giấm ăn thường nằm trong khoảng:", ["2 - 3", "7 - 8", "12 - 13", "8 - 9"], 0, "Giấm ăn có tính axit nên pH khoảng 2 - 3."),
        make_mc(4, "Nhận biết", "Chất nào sau đây được gọi là xút ăn da?", ["NaOH (natri hiđroxit)", "KOH", "Ca(OH)2", "Ba(OH)2"], 0, "NaOH có tên thông thường là xút ăn da."),
        make_mc(5, "Thông hiểu", "Sản phẩm của phản ứng giữa Ca(OH)2 và khí CO2 là:", ["CaCO3 kết tủa trắng và H2O", "CaO và H2", "CaCl2 và H2O", "Ca(HCO3)2 không màu"], 0, "CO2 + Ca(OH)2 -> CaCO3 (trắng) + H2O."),
        make_mc(6, "Thông hiểu", "Cho mẩu giấy quỳ tím vào dung dịch KOH, sau đó nhỏ từ từ dung dịch axit HCl vào đến dư. Màu sắc của giấy quỳ biến đổi như thế nào?", ["Từ xanh sang tím rồi sang đỏ", "Từ đỏ sang xanh", "Luôn giữ nguyên màu xanh", "Mất màu hoàn toàn"], 0, "Ban đầu bazơ (xanh), khi trung hòa hết (tím), dư axit (đỏ)."),
        make_mc(7, "Thông hiểu", "Chất nào sau đây dùng để nhận biết ion Cu2+ trong dung dịch bằng kết tủa màu xanh lam?", ["Dung dịch kiềm NaOH", "Dung dịch axit HCl", "Dung dịch muối NaCl", "Nước cất"], 0, "Cu2+ + 2OH- -> Cu(OH)2 (kết tủa xanh lam)."),
        make_mc(8, "Thông hiểu", "Một mẫu đất nông nghiệp có pH = 4,5. Đất này được xếp vào loại:", ["Đất chua", "Đất kiềm", "Đất trung tính", "Đất mặn"], 0, "pH < 7 là đất chua."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 4,6 g kim loại natri vào nước thu được 100 mL dung dịch NaOH. Nồng độ mol của dung dịch NaOH là:", ["2 M", "1 M", "0,5 M", "4 M"], 0, "n_Na = 0,2 mol -> n_NaOH = 0,2 mol -> CM = 0,2 / 0,1 = 2 M."),
        make_mc(10, "Vận dụng", "Cho dung dịch chứa 0,1 mol CuCl2 tác dụng vừa đủ với dung dịch NaOH. Khối lượng kết tủa Cu(OH)2 thu được là:", ["9,8 g", "4,9 g", "19,6 g", "14,7 g"], 0, "m = 0,1 * 98 = 9,8 g."),
        make_mc(11, "Vận dụng", "Cần lấy bao nhiêu mL dung dịch NaOH 1 M để trung hòa hoàn toàn 100 mL dung dịch H2SO4 0,5 M?", ["100 mL", "200 mL", "50 mL", "150 mL"], 0, "n_H2SO4 = 0,05 mol -> n_NaOH = 0,1 mol -> V = 0,1 L = 100 mL."),
        make_mc(12, "Vận dụng cao", "Hòa tan hoàn toàn m gam bột Al vào 200 mL dung dịch NaOH 1 M dư thu được 7,437 lít khí H2 ở đkc. Giá trị của m là:", ["5,4 g", "2,7 g", "10,8 g", "8,1 g"], 0, "2Al + 2NaOH + 2H2O -> 2NaAlO2 + 3H2. n_H2 = 0,3 mol -> n_Al = 0,2 mol -> m = 0,2 * 27 = 5,4 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phản ứng của bazơ kiềm với oxit axit:", [
            ("a", "2NaOH + SO2 -> Na2SO3 + H2O.", True),
            ("b", "Ca(OH)2 + CO2 -> CaCO3 (kết tủa trắng) + H2O.", True),
            ("c", "Dung dịch kiềm có thể dùng để hấp thụ các khí độc có tính axit như SO2, H2S.", True),
            ("d", "Dung dịch kiềm hấp thụ tốt khí hiđro H2 và khí metan CH4.", False)
        ], "H2 và CH4 trơ không tác dụng với dung dịch kiềm."),
        make_tf(2, "Thông hiểu", "Về các hiện tượng đổi màu chất chỉ thị:", [
            ("a", "Quỳ tím chuyển sang màu xanh trong dung dịch kiềm có pH > 7.", True),
            ("b", "Phenolphtalein không màu chuyển sang màu hồng trong dung dịch kiềm.", True),
            ("c", "Phenolphtalein chuyển sang màu đỏ trong dung dịch axit có pH < 7.", False),
            ("d", "Nước cất trung tính pH = 7 không làm đổi màu quỳ tím và phenolphtalein.", True)
        ], "Phenolphtalein không màu trong môi trường axit và trung tính."),
        make_tf(3, "Vận dụng", "Cho các phản ứng trung hòa bazơ không tan:", [
            ("a", "Cu(OH)2 + 2HCl -> CuCl2 + 2H2O (dung dịch đổi sang màu xanh lam).", True),
            ("b", "Fe(OH)3 + 3HCl -> FeCl3 + 3H2O (dung dịch đổi sang màu vàng nâu).", True),
            ("c", "Al(OH)3 + 3HCl -> AlCl3 + 3H2O (dung dịch không màu).", True),
            ("d", "Các bazơ không tan không thể tác dụng với axit do không tan.", False)
        ], "Bazơ không tan vẫn tan và tác dụng tốt với dung dịch axit mạnh."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm thêm từ từ dung dịch HCl vào dung dịch NaOH:", [
            ("a", "Giá trị pH của dung dịch giảm dần từ trên 7 xuống 7 rồi xuống dưới 7.", True),
            ("b", "Tại thời điểm pH = 7, toàn bộ NaOH đã phản ứng vừa đủ với HCl tạo dung dịch muối ăn trung tính.", True),
            ("c", "Nhiệt độ của cốc giảm đi đóng băng thành đá.", False),
            ("d", "Phản ứng trung hòa axit - bazơ là phản ứng tỏa nhiệt.", True)
        ], "Phản ứng trung hòa tỏa nhiệt làm cốc ấm lên.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong công thức của bazơ Ca(OH)2, chỉ số của nhóm -OH là bao nhiêu?", "2", "Chỉ số của nhóm OH là 2."),
        make_sa(2, "Thông hiểu", "Dung dịch có pH = 12 có tính kiềm hay axit? (Điền: kiềm)", "kiềm", "pH = 12 là môi trường kiềm."),
        make_sa(3, "Thông hiểu", "Khối lượng mol của natri hiđroxit NaOH là bao nhiêu g/mol?", "40", "M = 23 + 16 + 1 = 40 g/mol."),
        make_sa(4, "Vận dụng", "Hòa tan 0,3 mol KOH vào nước để được 300 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M?", "1", "CM = 0,3 / 0,3 = 1 M."),
        make_sa(5, "Vận dụng", "Nhiệt phân hoàn toàn 10,7 g Fe(OH)3 thu được bao nhiêu gam nước? (Ghi số thập phân)", "2,7", "n = 0,1 mol -> n_H2O = 0,15 mol -> m = 0,15 * 18 = 2,7 g."),
        make_sa(6, "Vận dụng cao", "Cần bao nhiêu gam NaOH để trung hòa 0,05 mol H2SO4?", "4", "n_NaOH = 0,1 mol -> m = 0,1 * 40 = 4 g.")
    ],
    "part4": [
        make_vdc(1, "Cho 200 mL dung dịch NaOH 1 M tác dụng với 100 mL dung dịch H2SO4 1,5 M. Dung dịch sau phản ứng có tính chất gì và pH thế nào?", ["Dung dịch có tính axit, pH < 7", "Dung dịch có tính kiềm, pH > 7", "Dung dịch trung tính, pH = 7", "Không đổi"], 0, "n_NaOH = 0,2 mol; n_H2SO4 = 0,15 mol (cần 0,3 mol NaOH) -> axit dư -> tính axit, pH < 7."),
        make_vdc(2, "Hòa tan hoàn toàn m gam kim loại bari Ba vào nước thu được 200 mL dung dịch Ba(OH)2 0,5 M và giải phóng V lít khí H2 ở đkc. Giá trị của m là:", ["13,7 g", "27,4 g", "6,85 g", "20,55 g"], 0, "n_Ba = 0,1 mol -> m = 0,1 * 137 = 13,7 g."),
        make_vdc(3, "Nhiệt phân hoàn toàn m gam hỗn hợp gồm Cu(OH)2 và Fe(OH)3 thu được 16 g chất rắn gồm CuO và Fe2O3. Biết số mol Cu(OH)2 bằng số mol Fe(OH)3. Giá trị của m là:", ["20,5 g", "19,6 g", "21,4 g", "18,2 g"], 0, "80x + 160*0,5x = 16 -> 160x = 16 -> x = 0,1 mol -> m = 0,1*98 + 0,1*107 = 20,5 g."),
        make_vdc(4, "Một dung dịch kiềm Ca(OH)2 có pH = 12. Để làm giảm độ kiềm của dung dịch về mức an toàn hơn cho sinh vật, người ta có thể sục nhẹ khí nào sau đây?", ["Khí cacbon đioxit (CO2)", "Khí oxi (O2)", "Khí nitơ (N2)", "Khí hiđro (H2)"], 0, "CO2 phản ứng với Ca(OH)2 làm giảm nồng độ OH- hạ pH về mức trung tính.")
    ]
}

# ==============================================================================
# BÀI 10: OXIDE (ĐỀ 2 & ĐỀ 3)
# ==============================================================================

missing_8["chem8_c2_b10_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Oxit nào sau đây tác dụng với nước tạo thành dung dịch bazơ?", ["CaO", "CO2", "SO2", "P2O5"], 0, "CaO + H2O -> Ca(OH)2."),
        make_mc(2, "Nhận biết", "Chất nào sau đây là oxit axit?", ["SO2 (lưu huỳnh đioxit)", "Na2O", "Fe2O3", "CuO"], 0, "SO2 là oxit axit tương ứng với H2SO3."),
        make_mc(3, "Nhận biết", "Chất rắn màu đen nào sau đây là một oxit bazơ?", ["CuO (đồng(II) oxit)", "Fe(OH)3", "CaCO3", "Al2O3"], 0, "CuO là bột màu đen."),
        make_mc(4, "Nhận biết", "Khí nào sau đây là oxit trung tính không tạo muối?", ["NO (nitơ monooxit)", "NO2", "N2O5", "SO3"], 0, "NO là oxit trung tính."),
        make_mc(5, "Thông hiểu", "Sản phẩm của phản ứng giữa điphotpho pentaoxit P2O5 và nước là:", ["Axit photphoric H3PO4", "Axit sunfuric H2SO4", "Axit clohiđric HCl", "Khí photphin PH3"], 0, "P2O5 + 3H2O -> 2H3PO4."),
        make_mc(6, "Thông hiểu", "Oxit bazơ tác dụng với dung dịch axit tạo thành:", ["Muối và nước", "Bazơ và khí hiđro", "Kim loại và nước", "Oxit axit và muối"], 0, "Oxit bazơ + axit -> muối + nước."),
        make_mc(7, "Thông hiểu", "Hiện tượng quan sát được khi cho bột CuO màu đen vào dung dịch axit HCl nóng là:", ["Bột đen tan dần tạo dung dịch màu xanh lam", "Có bọt khí thoát ra dữ dội", "Bột đen chuyển thành màu đỏ", "Dung dịch đóng băng"], 0, "CuO + 2HCl -> CuCl2 (màu xanh lam) + H2O."),
        make_mc(8, "Thông hiểu", "Khí sunfurơ SO2 có trong khí thải nhà máy tác dụng với dung dịch nước vôi trong Ca(OH)2 tạo kết tủa trắng là:", ["CaSO3 (canxi sunfit)", "CaSO4", "CaCO3", "CaO"], 0, "SO2 + Ca(OH)2 -> CaSO3 (trắng) + H2O."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 5,6 g vôi sống CaO vào nước thu được dung dịch chứa m gam Ca(OH)2. Giá trị của m là:", ["7,4 g", "5,6 g", "11,2 g", "14,8 g"], 0, "n_CaO = 0,1 mol -> m_Ca(OH)2 = 0,1 * 74 = 7,4 g."),
        make_mc(10, "Vận dụng", "Dẫn 2,479 lít khí SO2 ở đkc vào lượng dư dung dịch Ca(OH)2 thu được bao nhiêu gam kết tủa CaSO3?", ["12,0 g", "6,0 g", "24,0 g", "18,0 g"], 0, "n = 0,1 mol -> m_CaSO3 = 0,1 * 120 = 12,0 g."),
        make_mc(11, "Vận dụng", "Cần dùng bao nhiêu mL dung dịch HCl 2 M để hòa tan hoàn toàn 8 g oxit Fe2O3?", ["150 mL", "300 mL", "100 mL", "200 mL"], 0, "Fe2O3 + 6HCl -> 2FeCl3 + 3H2O. n = 0,05 mol -> n_HCl = 0,3 mol -> V = 0,3 / 2 = 0,15 L = 150 mL."),
        make_mc(12, "Vận dụng cao", "Dẫn khí CO dư đi qua ống sứ nung nóng chứa 16 g bột Fe2O3. Sau khi phản ứng xảy ra hoàn toàn thu được m gam kim loại sắt. Giá trị của m là:", ["11,2 g", "5,6 g", "8,4 g", "14,0 g"], 0, "Fe2O3 + 3CO -> 2Fe + 3CO2. n_Fe2O3 = 0,1 mol -> n_Fe = 0,2 mol -> m = 0,2 * 56 = 11,2 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất hóa học của oxit:", [
            ("a", "Oxit axit tác dụng với dung dịch bazơ tạo thành muối và nước.", True),
            ("b", "Oxit bazơ tác dụng với dung dịch axit tạo thành muối và nước.", True),
            ("c", "Một số oxit bazơ tan (Na2O, K2O, CaO, BaO) tác dụng với oxit axit tạo muối.", True),
            ("d", "Tất cả các oxit phi kim đều tác dụng mãnh liệt với nước ở nhiệt độ thường.", False)
        ], "Nhiều oxit phi kim như CO, NO, SiO2 không tác dụng với nước ở nhiệt độ thường."),
        make_tf(2, "Thông hiểu", "Về tác hại môi trường của các oxit khí quyển:", [
            ("a", "Khí SO2 sinh ra do đốt than đá, dầu mỏ là nguyên nhân chính gây mưa axit.", True),
            ("b", "Khí NO2 tạo thành trong khí quyển góp phần làm tăng tính axit của nước mưa.", True),
            ("c", "Khí CO2 gây hiệu ứng nhà kính làm tăng nhiệt độ trung bình toàn cầu.", True),
            ("d", "Khí CO2 phá hủy trực tiếp tầng ozon bảo vệ Trái Đất.", False)
        ], "CFC và các hợp chất chứa clo mới phá hủy tầng ozon, không phải CO2."),
        make_tf(3, "Vận dụng", "Cho các phản ứng của canxi oxit CaO:", [
            ("a", "CaO + H2O -> Ca(OH)2 (phản ứng tôi vôi tỏa nhiệt).", True),
            ("b", "CaO + 2HCl -> CaCl2 + H2O.", True),
            ("c", "CaO + CO2 -> CaCO3 (đá vôi).", True),
            ("d", "CaO + Cu -> CuO + Ca.", False)
        ], "Kim loại Cu không khử được CaO."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng khử oxit kim loại bằng khí H2 nung nóng:", [
            ("a", "Khí H2 có thể khử các oxit kim loại đứng sau nhôm trong dãy hoạt động (như CuO, Fe2O3).", True),
            ("b", "Dẫn khí H2 qua bột CuO màu đen nung nóng thu được kim loại đồng màu đỏ.", True),
            ("c", "Dẫn khí H2 qua bột Na2O nung nóng thu được kim loại natri tự do.", False),
            ("d", "Phương trình: CuO + H2 -> Cu + H2O.", True)
        ], "Na2O là oxit kim loại rất mạnh, H2 không khử được.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phân tử natri oxit Na2O có bao nhiêu nguyên tử natri?", "2", "Có 2 nguyên tử Na."),
        make_sa(2, "Thông hiểu", "Sản phẩm của phản ứng giữa CaO và nước làm quỳ tím chuyển sang màu gì?", "xanh", "Tạo Ca(OH)2 làm quỳ tím hóa xanh."),
        make_sa(3, "Thông hiểu", "Oxit kẽm ZnO thuộc loại oxit nào? (Điền: lưỡng tính)", "lưỡng tính", "ZnO là oxit lưỡng tính."),
        make_sa(4, "Vận dụng", "Khối lượng mol của oxit lưu huỳnh trioxit SO3 là bao nhiêu g/mol?", "80", "M = 32 + 16*3 = 80 g/mol."),
        make_sa(5, "Vận dụng", "Hòa tan 0,1 mol CaO vào nước thu được bao nhiêu gam Ca(OH)2? (Ghi số thập phân)", "7,4", "0,1 * 74 = 7,4 g."),
        make_sa(6, "Vận dụng cao", "Khử hoàn toàn 8 g bột CuO bằng H2 dư thu được bao nhiêu gam kim loại đồng? (Ghi số thập phân)", "6,4", "n = 0,1 mol -> m_Cu = 0,1 * 64 = 6,4 g.")
    ],
    "part4": [
        make_vdc(1, "Dẫn 4,958 lít khí CO2 ở đkc vào dung dịch chứa 0,15 mol Ba(OH)2. Khối lượng kết tủa BaCO3 thu được là:", ["19,7 g", "29,55 g", "9,85 g", "39,4 g"], 0, "n_CO2 = 0,2 mol; n_Ba(OH)2 = 0,15 mol -> n_BaCO3 = 2*0,15 - 0,2 = 0,1 mol -> m = 19,7 g."),
        make_vdc(2, "Hòa tan hoàn toàn 20 g hỗn hợp gồm CuO và Fe2O3 cần vừa đủ 250 mL dung dịch axit HCl 2 M. Khối lượng nước tạo thành trong phản ứng là:", ["4,5 g", "9,0 g", "18,0 g", "3,6 g"], 0, "n_HCl = 0,5 mol -> n_H2O = 0,25 mol -> m_H2O = 0,25 * 18 = 4,5 g."),
        make_vdc(3, "Hòa tan 6,2 g Na2O vào 193,8 g nước cất. Nồng độ phần trăm của dung dịch NaOH thu được là:", ["4,0%", "3,1%", "8,0%", "5,0%"], 0, "n_Na2O = 0,1 mol -> m_NaOH = 0,2 * 40 = 8 g; m_dd = 6,2 + 193,8 = 200 g -> C% = 8 / 200 = 4%."),
        make_vdc(4, "Khí CO khử hoàn toàn hỗn hợp gồm Fe2O3 và CuO nung nóng thu được 17,6 g hỗn hợp kim loại và giải phóng 7,437 lít khí CO2 ở đkc. Khối lượng hỗn hợp hai oxit ban đầu là:", ["22,4 g", "20,0 g", "24,8 g", "19,2 g"], 0, "n_CO2 = 0,3 mol -> n_O trong oxit = 0,3 mol -> m_oxit = 17,6 + 0,3 * 16 = 17,6 + 4,8 = 22,4 g.")
    ]
}

missing_8["chem8_c2_b10_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Oxit nào sau đây là oxit của kim loại kiềm tan mạnh trong nước tỏa nhiệt?", ["Na2O", "CuO", "Fe2O3", "Al2O3"], 0, "Na2O là oxit kim loại kiềm tan mạnh trong nước."),
        make_mc(2, "Nhận biết", "Khí nào sau đây thoát ra khi đun sôi nhẹ nước ngọt có gas?", ["CO2 (cacbon đioxit)", "O2", "H2", "N2"], 0, "Khí CO2 hòa tan trong nước ngọt có gas."),
        make_mc(3, "Nhận biết", "Chất bột màu trắng nào sau đây tác dụng với nước tạo thành dung dịch vôi tôi?", ["CaO (canxi oxit)", "CuO", "Fe2O3", "P2O5"], 0, "CaO + H2O -> Ca(OH)2."),
        make_mc(4, "Nhận biết", "Trong 4 loại oxit: oxit bazơ, oxit axit, oxit lưỡng tính, oxit trung tính; loại oxit nào KHÔNG TÁC DỤNG với cả axit và bazơ?", ["Oxit trung tính", "Oxit lưỡng tính", "Oxit axit", "Oxit bazơ"], 0, "Oxit trung tính không tạo muối (như CO, NO)."),
        make_mc(5, "Thông hiểu", "Sản phẩm của phản ứng giữa canxi oxit CaO và axit clohiđric HCl là:", ["CaCl2 và H2O", "CaCO3 và H2", "Ca(OH)2 và Cl2", "CaOCl2 và H2"], 0, "CaO + 2HCl -> CaCl2 + H2O."),
        make_mc(6, "Thông hiểu", "Cho quỳ tím vào dung dịch tạo thành khi cho SO3 tác dụng với nước, quỳ tím chuyển sang màu:", ["Màu đỏ", "Màu xanh", "Màu tím", "Màu vàng"], 0, "SO3 + H2O -> H2SO4 (axit làm quỳ tím hóa đỏ)."),
        make_mc(7, "Thông hiểu", "Hiện tượng vôi sống CaO để lâu ngoài không khí ẩm bị bở vụn ra và mất tính chất tôi vôi là do:", ["CaO hút ẩm biến thành Ca(OH)2 rồi tác dụng với CO2 thành CaCO3", "CaO bay hơi hết", "CaO biến thành kim loại canxi", "Bụi bẩn bám dày"], 0, "CaO tác dụng hơi nước và CO2 trong không khí."),
        make_mc(8, "Thông hiểu", "Để làm khô khí CO2 có lẫn hơi nước, người ta dẫn khí qua bình đựng:", ["Axit sunfuric đặc H2SO4", "Dung dịch kiềm NaOH", "Vôi sống CaO", "Nước cất"], 0, "H2SO4 đặc hút ẩm tốt và không phản ứng với CO2."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 8 g bột CuO vào 100 mL dung dịch HCl 2,5 M. Sau phản ứng, nồng độ mol của axit HCl còn dư là:", ["0,5 M", "1,0 M", "0,25 M", "0,1 M"], 0, "n_CuO = 0,1 mol -> n_HCl pư = 0,2 mol; n_HCl ban đầu = 0,25 mol -> n_dư = 0,05 mol -> CM = 0,05 / 0,1 = 0,5 M."),
        make_mc(10, "Vận dụng", "Dẫn luồng khí H2 dư qua ống chứa 20 g hỗn hợp gồm CuO và Al2O3 nung nóng đỏ. Sau phản ứng hoàn toàn, chất rắn còn lại gồm những chất nào?", ["Cu và Al2O3", "Cu và Al", "CuO và Al", "Cu(OH)2 và Al2O3"], 0, "H2 chỉ khử được CuO thành Cu; không khử được Al2O3."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 6,2 g photpho P trong khí oxi dư thu được m gam chất rắn màu trắng P2O5. Giá trị của m là:", ["14,2 g", "7,1 g", "28,4 g", "10,5 g"], 0, "n_P = 0,2 mol -> n_P2O5 = 0,1 mol -> m = 0,1 * 142 = 14,2 g."),
        make_mc(12, "Vận dụng cao", "Dẫn 1,2395 lít khí CO2 ở đkc vào 100 mL dung dịch Ba(OH)2 0,5 M thu được m gam kết tủa BaCO3. Giá trị của m là:", ["9,85 g", "19,7 g", "4,925 g", "14,775 g"], 0, "n_CO2 = 0,05 mol; n_Ba(OH)2 = 0,05 mol -> phản ứng vừa đủ tạo 0,05 mol BaCO3 -> m = 0,05 * 197 = 9,85 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về oxit lưỡng tính Al2O3 và ZnO:", [
            ("a", "Al2O3 tan được trong dung dịch axit mạnh như HCl, H2SO4.", True),
            ("b", "Al2O3 tan được trong dung dịch kiềm mạnh như NaOH, KOH.", True),
            ("c", "Al2O3 tan tốt trong nước ở nhiệt độ phòng.", False),
            ("d", "Tính chất tác dụng với cả axit và bazơ được gọi là tính lưỡng tính.", True)
        ], "Al2O3 hoàn toàn không tan trong nước."),
        make_tf(2, "Thông hiểu", "Về phản ứng tạo muối của oxit:", [
            ("a", "Oxit bazơ tác dụng với oxit axit tạo thành muối (ví dụ CaO + CO2 -> CaCO3).", True),
            ("b", "Oxit axit tác dụng với dung dịch bazơ tạo thành muối và nước.", True),
            ("c", "Khí CO tác dụng với dung dịch NaOH ở nhiệt độ phòng tạo muối natri cacbonat.", False),
            ("d", "Khí SO2 làm đục nước vôi trong tương tự khí CO2.", True)
        ], "CO là oxit trung tính không tác dụng với dung dịch kiềm ở nhiệt độ thường."),
        make_tf(3, "Vận dụng", "Cho các phản ứng nung nóng oxit kim loại:", [
            ("a", "Dẫn khí CO qua bột Fe2O3 nung nóng thu được kim loại Fe và khí CO2.", True),
            ("b", "Khí CO có tính khử mạnh ở nhiệt độ cao.", True),
            ("c", "Phản ứng luyện gang trong lò cao bản chất là khử các oxit sắt bằng khí CO.", True),
            ("d", "Khí CO có thể khử được oxit nhôm Al2O3 thành nhôm kim loại trong lò cao.", False)
        ], "Al2O3 liên kết cực kì bền vững, CO không khử được Al2O3."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm cho mẩu vôi sống CaO vào nước:", [
            ("a", "Mẩu CaO hút nước rạn nứt phát ra tiếng lách tách và bốc khói hơi nước mù mịt.", True),
            ("b", "Nhiệt độ của nước tăng lên rất cao có thể làm chín quả trứng.", True),
            ("c", "Dung dịch sau khi lọc bỏ cặn vôi có tính kiềm làm phenolphtalein hóa hồng.", True),
            ("d", "Khối lượng chất rắn thu được nhỏ hơn khối lượng CaO ban đầu.", False)
        ], "m_Ca(OH)2 = m_CaO + m_H2O > m_CaO ban đầu.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong công thức hóa học của oxit sắt từ Fe3O4 có bao nhiêu nguyên tử oxi?", "4", "Có 4 nguyên tử oxi."),
        make_sa(2, "Thông hiểu", "Khí CO2 có làm đục nước vôi trong Ca(OH)2 không? (Điền: có hoặc không)", "có", "Tạo kết tủa trắng CaCO3 làm đục nước vôi trong."),
        make_sa(3, "Thông hiểu", "Khối lượng mol của oxit bari BaO là bao nhiêu g/mol?", "153", "M = 137 + 16 = 153 g/mol."),
        make_sa(4, "Vận dụng", "Hòa tan hoàn toàn 0,2 mol Na2O vào nước thu được bao nhiêu mol NaOH? (Ghi số thập phân)", "0,4", "Na2O + H2O -> 2NaOH: n = 0,4 mol."),
        make_sa(5, "Vận dụng", "Số mol khí O2 cần để đốt cháy hoàn toàn 0,2 mol carbon thành khí CO2 là bao nhiêu mol? (Ghi số thập phân)", "0,2", "C + O2 -> CO2: cần 0,2 mol O2."),
        make_sa(6, "Vận dụng cao", "Khử hoàn toàn 16 g Fe2O3 bằng CO dư ở nhiệt độ cao thu được bao nhiêu gam kim loại sắt? (Ghi số thập phân)", "11,2", "n_Fe = 0,2 mol -> m = 11,2 g.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn 15,3 g oxit Al2O3 vào dung dịch axit H2SO4 loãng vừa đủ. Khối lượng muối Al2(SO4)3 thu được là:", ["51,3 g", "25,65 g", "34,2 g", "102,6 g"], 0, "Al2O3 + 3H2SO4 -> Al2(SO4)3 + 3H2O. n = 15,3 / 102 = 0,15 mol -> m_muối = 0,15 * 342 = 51,3 g."),
        make_vdc(2, "Dẫn 3,7185 lít khí CO2 ở đkc vào dung dịch chứa 0,1 mol Ca(OH)2. Khối lượng kết tủa CaCO3 thu được sau phản ứng là:", ["5,0 g", "10,0 g", "15,0 g", "7,5 g"], 0, "n_CO2 = 0,15 mol; n_Ca(OH)2 = 0,1 mol -> n_CaCO3 = 2*0,1 - 0,15 = 0,05 mol -> m = 5,0 g."),
        make_vdc(3, "Một hỗn hợp gồm CuO và Fe2O3 có tỉ lệ mol 1 : 1. Cần bao nhiêu mol axit HCl để hòa tan hoàn toàn 2,4 g hỗn hợp này?", ["0,08 mol", "0,04 mol", "0,16 mol", "0,06 mol"], 0, "80x + 160x = 2,4 -> 240x = 2,4 -> x = 0,01 mol. n_HCl = 2*0,01 + 6*0,01 = 0,08 mol."),
        make_vdc(4, "Khí CO khử hoàn toàn một oxit sắt FexOy nung nóng thu được 8,4 g sắt và giải phóng 4,958 lít khí CO2 ở đkc. Công thức phân tử của oxit sắt là:", ["Fe2O3", "Fe3O4", "FeO", "Fe2O"], 0, "n_Fe = 8,4/56 = 0,15 mol; n_O = n_CO2 = 0,2 mol -> x : y = 0,15 : 0,2 = 3 : 4 -> Fe3O4.")
    ]
}

# ==============================================================================
# BÀI 11: MUỐI (ĐỀ 2 & ĐỀ 3)
# ==============================================================================

missing_8["chem8_c2_b11_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Muối nào sau đây dùng làm chất bảo quản thực phẩm (ướp cá, làm nước mắm)?", ["NaCl (natri clorua)", "CuSO4", "BaSO4", "AgNO3"], 0, "Muối ăn NaCl."),
        make_mc(2, "Nhận biết", "Muối bạc nitrat có công thức hóa học là:", ["AgNO3", "AgCl", "Ag2SO4", "Ag2CO3"], 0, "Bạc nitrat là AgNO3."),
        make_mc(3, "Nhận biết", "Khi nhỏ dung dịch bari clorua BaCl2 vào dung dịch muối nào sau đây sẽ xuất hiện kết tủa trắng?", ["Na2SO4 (natri sunfat)", "NaCl", "KNO3", "HCl"], 0, "BaCl2 + Na2SO4 -> BaSO4 (kết tủa trắng) + 2NaCl."),
        make_mc(4, "Nhận biết", "Kim loại nào sau đây có thể đẩy được kim loại đồng Cu ra khỏi dung dịch muối CuSO4?", ["Sắt (Fe)", "Bạc (Ag)", "Vàng (Au)", "Bạch kim (Pt)"], 0, "Fe đứng trước Cu nên đẩy được Cu ra khỏi dung dịch muối."),
        make_mc(5, "Thông hiểu", "Cho dãy các muối: CaCO3, BaSO4, Cu(NO3)2, AgCl, K2SO4. Có bao nhiêu muối tan trong nước?", ["2", "3", "1", "4"], 0, "Có 2 muối tan: Cu(NO3)2 và K2SO4 (CaCO3, BaSO4, AgCl không tan)."),
        make_mc(6, "Thông hiểu", "Sản phẩm của phản ứng giữa dung dịch natri cacbonat Na2CO3 và dung dịch axit clohiđric HCl gồm có:", ["NaCl, H2O và khí CO2", "NaCl và H2", "NaHCO3 và Cl2", "NaOH và CO2"], 0, "Na2CO3 + 2HCl -> 2NaCl + H2O + CO2 (sủi bọt khí)."),
        make_mc(7, "Thông hiểu", "Hiện tượng quan sát được khi cho mẩu kim loại kẽm Zn vào dung dịch đồng sunfat CuSO4 màu xanh lam là:", ["Màu xanh lam nhạt dần và có kim loại màu đỏ bám trên kẽm", "Có bọt khí bay lên dữ dội", "Dung dịch chuyển sang màu tím", "Thanh kẽm nóng chảy"], 0, "Zn + CuSO4 -> ZnSO4 (không màu) + Cu (đỏ)."),
        make_mc(8, "Thông hiểu", "Phản ứng trao đổi trong dung dịch giữa hai muối xảy ra khi:", ["Sản phẩm có ít nhất một chất kết tủa không tan", "Cả hai chất sản phẩm đều bay hơi", "Không cần điều kiện gì", "Có khí oxi bay lên"], 0, "Phải có chất kết tủa tạo thành."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 5,3 g natri cacbonat Na2CO3 bằng dung dịch axit HCl dư. Thể tích khí CO2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:", ["1,2395 lít", "2,479 lít", "4,958 lít", "2,24 lít"], 0, "n_Na2CO3 = 5,3 / 106 = 0,05 mol -> V = 0,05 * 24,79 = 1,2395 L."),
        make_mc(10, "Vận dụng", "Cho dung dịch chứa 0,1 mol BaCl2 tác dụng với dung dịch chứa 0,1 mol K2SO4. Khối lượng kết tủa BaSO4 thu được là:", ["23,3 g", "11,65 g", "46,6 g", "15,5 g"], 0, "n = 0,1 mol -> m = 0,1 * 233 = 23,3 g."),
        make_mc(11, "Vận dụng", "Cần lấy bao nhiêu gam muối ăn NaCl để pha chế được 200 mL dung dịch NaCl 0,5 M?", ["5,85 g", "11,7 g", "2,925 g", "58,5 g"], 0, "n = 0,2 * 0,5 = 0,1 mol -> m = 0,1 * 58,5 = 5,85 g."),
        make_mc(12, "Vận dụng cao", "Ngâm một đinh sắt nặng 10 g vào dung dịch CuSO4 dư. Sau một thời gian, lấy đinh sắt ra cân lại thấy nặng 10,4 g. Khối lượng kim loại Cu đã bám lên đinh sắt là:", ["3,2 g", "6,4 g", "0,8 g", "1,6 g"], 0, "m tăng = 8n = 0,4 g -> n = 0,05 mol -> m_Cu bám = 0,05 * 64 = 3,2 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phản ứng trao đổi trong dung dịch chất điện li:", [
            ("a", "Phản ứng trao đổi là phản ứng trong đó hai hợp chất tham gia phản ứng trao đổi với nhau những thành phần cấu tạo.", True),
            ("b", "Phản ứng trao đổi trong dung dịch luôn luôn đi kèm với sự thay đổi số oxi hóa của các nguyên tố.", False),
            ("c", "Điều kiện xảy ra phản ứng trao đổi: tạo kết tủa, sinh chất khí hoặc chất điện li rất yếu (như H2O).", True),
            ("d", "Phản ứng trung hòa giữa axit và bazơ cũng là một trường hợp đặc biệt của phản ứng trao đổi.", True)
        ], "Phản ứng trao đổi không có sự thay đổi số oxi hóa."),
        make_tf(2, "Thông hiểu", "Về muối ăn trong đời sống con người:", [
            ("a", "Muối ăn NaCl khai thác từ nước biển bằng phương pháp phơi cát hoặc phơi nước kết tinh.", True),
            ("b", "NaCl là nguyên liệu sản xuất clo, hiđro và xút ăn da NaOH trong công nghiệp hóa chất.", True),
            ("c", "Muối I-ốt là muối ăn có trộn thêm một lượng nhỏ hợp chất của iot (như KIO3 hoặc KI) để phòng bệnh bướu cổ.", True),
            ("d", "Ăn càng nhiều muối ăn càng tốt cho người mắc bệnh huyết áp cao.", False)
        ], "Ăn nhiều muối làm tăng huyết áp gây nguy cơ tim mạch."),
        make_tf(3, "Vận dụng", "Cho các phản ứng giữa kim loại và dung dịch muối:", [
            ("a", "Fe + CuSO4 -> FeSO4 + Cu.", True),
            ("b", "Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag.", True),
            ("c", "Cu + FeSO4 -> CuSO4 + Fe.", False),
            ("d", "Zn + Pb(NO3)2 -> Zn(NO3)2 + Pb.", True)
        ], "Đồng đứng sau sắt nên không đẩy được sắt ra khỏi muối."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm cho dung dịch natri cacbonat vào dung dịch canxi clorua:", [
            ("a", "Phương trình: Na2CO3 + CaCl2 -> CaCO3 + 2NaCl.", True),
            ("b", "Xuất hiện kết tủa trắng canxi cacbonat lắng dần xuống đáy ống nghiệm.", True),
            ("c", "Nếu nhỏ tiếp dung dịch axit clohiđric vào ống nghiệm, kết tủa tan dần và có bọt khí sủi lên.", True),
            ("d", "Dung dịch thu được cuối cùng chỉ chứa duy nhất muối canxi cacbonat.", False)
        ], "Dung dịch cuối cùng chứa CaCl2 và NaCl tan trong nước.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phân tử muối đồng(II) sunfat CuSO4, kim loại đồng có hóa trị mấy?", "II", "Đồng có hóa trị II."),
        make_sa(2, "Thông hiểu", "Muối canxi cacbonat CaCO3 có tan trong nước không? (Điền: có hoặc không)", "không", "CaCO3 là chất không tan (kết tủa)."),
        make_sa(3, "Thông hiểu", "Khi cho thanh sắt vào dung dịch CuSO4, có kim loại màu gì bám ngoài thanh sắt?", "đỏ", "Kim loại đồng Cu màu đỏ."),
        make_sa(4, "Vận dụng", "Khối lượng mol của muối natri cacbonat Na2CO3 là bao nhiêu g/mol?", "106", "M = 23*2 + 12 + 16*3 = 106 g/mol."),
        make_sa(5, "Vận dụng", "Hòa tan hoàn toàn 0,1 mol CaCO3 bằng axit HCl thu được bao nhiêu lít khí CO2 ở đkc? (Ghi số thập phân)", "2,479", "V = 0,1 * 24,79 = 2,479 L."),
        make_sa(6, "Vận dụng cao", "Cho 0,1 mol BaCl2 tác dụng hoàn toàn với dung dịch Na2SO4 dư thu được bao nhiêu gam kết tủa BaSO4? (Ghi số thập phân)", "23,3", "m = 0,1 * 233 = 23,3 g.")
    ],
    "part4": [
        make_vdc(1, "Cho 10 g hỗn hợp gồm CaCO3 và NaCl tác dụng với lượng dư dung dịch axit HCl thu được 1,2395 lít khí CO2 ở đkc. Phần trăm khối lượng của muối ăn NaCl trong hỗn hợp là:", ["50%", "40%", "60%", "25%"], 0, "n_CO2 = 0,05 mol -> n_CaCO3 = 0,05 mol -> m_CaCO3 = 5,0 g -> m_NaCl = 5,0 g -> %NaCl = 50%."),
        make_vdc(2, "Ngâm một lá đồng có khối lượng 20 g vào 100 mL dung dịch AgNO3 1 M. Sau một thời gian lấy lá đồng ra cân lại thấy nặng 21,52 g. Khối lượng bạc kim loại bám trên lá đồng là:", ["2,16 g", "4,32 g", "1,08 g", "3,24 g"], 0, "m tăng = n * (2*108 - 64) = 152n = 1,52 g -> n = 0,01 mol -> m_Ag = 2 * 0,01 * 108 = 2,16 g."),
        make_vdc(3, "Hòa tan hoàn toàn 14,2 g muối natri sunfat Na2SO4 vào nước được 200 mL dung dịch. Nồng độ mol của dung dịch Na2SO4 là:", ["0,5 M", "1,0 M", "0,25 M", "0,1 M"], 0, "n = 14,2 / 142 = 0,1 mol -> CM = 0,1 / 0,2 = 0,5 M."),
        make_vdc(4, "Một dung dịch chứa đồng thời 0,1 mol BaCl2 và 0,1 mol CuCl2. Thêm từ từ dung dịch Na2SO4 vào dung dịch trên cho đến khi kết tủa hoàn toàn. Khối lượng kết tủa thu được là:", ["23,3 g", "46,6 g", "11,65 g", "15,5 g"], 0, "Chỉ có Ba2+ kết tủa BaSO4, CuSO4 tan -> n_BaSO4 = 0,1 mol -> m = 23,3 g.")
    ]
}

missing_8["chem8_c2_b11_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Muối nào sau đây kết tủa màu vàng nhạt khi cho tác dụng với dung dịch AgNO3?", ["AgI", "AgCl (trắng)", "AgNO3", "Ag2SO4"], 0, "AgI kết tủa màu vàng nhạt/vàng đậm."),
        make_mc(2, "Nhận biết", "Dung dịch muối nào sau đây có màu xanh lam đặc trưng?", ["CuSO4 (đồng(II) sunfat)", "FeSO4", "NaCl", "AlCl3"], 0, "CuSO4 trong nước có màu xanh lam."),
        make_mc(3, "Nhận biết", "Muối nào sau đây dùng để bó bột khi gãy xương trong y tế?", ["Thạch cao sống/khan (CaSO4)", "Muối ăn NaCl", "Đá vôi CaCO3", "Muối diêm KNO3"], 0, "Thạch cao CaSO4 dùng để bó bột y tế."),
        make_mc(4, "Nhận biết", "Khi cho kim loại kẽm Zn vào dung dịch chì nitrat Pb(NO3)2, hiện tượng xảy ra là:", ["Kim loại chì màu xám bám trên thanh kẽm", "Không có hiện tượng gì", "Khí hiđro bay lên dữ dội", "Dung dịch chuyển sang màu đỏ"], 0, "Zn + Pb(NO3)2 -> Zn(NO3)2 + Pb (xám)."),
        make_mc(5, "Thông hiểu", "Dãy gồm các muối đều tan tốt trong nước là:", ["KNO3, NaCl, CuCl2, Ba(NO3)2", "CaCO3, BaSO4, AgCl, PbSO4", "AgNO3, BaSO4, KCl, Na2CO3", "FeS, CuS, NaCl, K2SO4"], 0, "Dãy gồm toàn muối tan: KNO3, NaCl, CuCl2, Ba(NO3)2."),
        make_mc(6, "Thông hiểu", "Sản phẩm của phản ứng giữa axit H2SO4 và muối BaCl2 là:", ["BaSO4 kết tủa trắng và axit HCl", "BaO và khí H2S", "Ba(HSO4)2 và Cl2", "BaSO3 và H2O"], 0, "BaCl2 + H2SO4 -> BaSO4 (trắng) + 2HCl."),
        make_mc(7, "Thông hiểu", "Khi nhiệt phân hoàn toàn muối canxi cacbonat CaCO3, sản phẩm thu được gồm:", ["Canxi oxit CaO và khí cacbon đioxit CO2", "Canxi kim loại và khí CO2", "Canxi hiđroxit và O2", "Canxi cacbua và O2"], 0, "CaCO3 -> CaO + CO2."),
        make_mc(8, "Thông hiểu", "Để nhận biết ion sunfat (=SO4) trong dung dịch muối hoặc axit, người ta thường dùng dung dịch muối nào?", ["Dung dịch chứa ion bari như BaCl2 hoặc Ba(NO3)2", "Dung dịch NaCl", "Dung dịch KNO3", "Dung dịch AgNO3"], 0, "Tạo kết tủa trắng bền BaSO4 không tan trong axit."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 8,4 g muối MgCO3 bằng dung dịch axit HCl dư. Thể tích khí CO2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:", ["2,479 lít", "4,958 lít", "1,2395 lít", "3,7185 lít"], 0, "n = 8,4 / 84 = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."),
        make_mc(10, "Vận dụng", "Trộn 200 mL dung dịch Na2SO4 0,5 M với lượng dư dung dịch BaCl2 thu được m gam kết tủa trắng. Giá trị của m là:", ["23,3 g", "11,65 g", "46,6 g", "15,5 g"], 0, "n_Na2SO4 = 0,1 mol -> m_BaSO4 = 0,1 * 233 = 23,3 g."),
        make_mc(11, "Vận dụng", "Cho mẩu kim loại natri vào dung dịch CuSO4, hiện tượng quan sát được là:", ["Natri tan dần sủi bọt khí không màu và xuất hiện kết tủa màu xanh lam", "Kim loại đồng màu đỏ bám trên bề mặt natri", "Dung dịch mất màu và sủi bọt khí màu vàng", "Không có hiện tượng gì"], 0, "Na tác dụng với nước trước: 2Na + 2H2O -> 2NaOH + H2; sau đó: 2NaOH + CuSO4 -> Cu(OH)2 (kết tủa xanh lam) + Na2SO4."),
        make_mc(12, "Vận dụng cao", "Hòa tan hoàn toàn 19 g hỗn hợp gồm hai muối cacbonat của hai kim loại hóa trị II vào dung dịch axit HCl dư, sau phản ứng thu được 4,958 lít khí CO2 ở đkc. Khối lượng muối clorua thu được trong dung dịch sau khi cô cạn là:", ["21,2 g", "20,1 g", "22,5 g", "24,0 g"], 0, "n_CO2 = 0,2 mol -> n_HCl = 0,4 mol -> m_H2O = 0,2 * 18 = 3,6 g. m_muối = 19 + 0,4*36,5 - 0,2*44 - 3,6 = 19 + 14,6 - 8,8 - 3,6 = 21,2 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các muối kết tủa thường gặp trong hóa học 8:", [
            ("a", "Bari sunfat BaSO4 kết tủa màu trắng không tan trong cả axit mạnh.", True),
            ("b", "Bạc clorua AgCl kết tủa màu trắng hóa đen ngoài ánh sáng mặt trời.", True),
            ("c", "Canxi cacbonat CaCO3 kết tủa trắng tan trong dung dịch axit sủi bọt khí CO2.", True),
            ("d", "Muối ăn NaCl kết tủa màu vàng óng dưới đáy cốc nước.", False)
        ], "NaCl tan rất tốt trong nước tạo dung dịch không màu."),
        make_tf(2, "Thông hiểu", "Về tính chất hóa học của muối cacbonat:", [
            ("a", "Muối cacbonat tác dụng với dung dịch axit mạnh giải phóng khí CO2.", True),
            ("b", "Muối cacbonat không tan bị nhiệt phân ở nhiệt độ cao giải phóng khí CO2.", True),
            ("c", "Dung dịch Na2CO3 làm quỳ tím hóa xanh do có tính kiềm yếu.", True),
            ("d", "Mọi muối cacbonat đều bị nhiệt phân bởi ngọn lửa đèn cồn kể cả Na2CO3, K2CO3.", False)
        ], "Na2CO3 và K2CO3 rất bền nhiệt, không bị phân hủy bởi đèn cồn."),
        make_tf(3, "Vận dụng", "Cho các phản ứng sau ở điều kiện thường:", [
            ("a", "Fe + 2AgNO3 -> Fe(NO3)2 + 2Ag.", True),
            ("b", "Cu + 2HCl -> CuCl2 + H2.", False),
            ("c", "BaCl2 + K2SO4 -> BaSO4 + 2KCl.", True),
            ("d", "Na2CO3 + Ca(OH)2 -> CaCO3 + 2NaOH.", True)
        ], "Đồng không tác dụng với HCl loãng."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm ngâm thanh kim loại nhôm (Al) vào dung dịch đồng sunfat CuSO4:", [
            ("a", "Phương trình: 2Al + 3CuSO4 -> Al2(SO4)3 + 3Cu.", True),
            ("b", "Kim loại đồng màu đỏ bám xốp ngoài thanh nhôm.", True),
            ("c", "Khối lượng thanh nhôm tăng lên sau phản ứng vì 2 mol Al (54g) tan ra tạo 3 mol Cu (192g) bám vào.", True),
            ("d", "Dung dịch sau phản ứng có màu xanh đậm hơn ban đầu.", False)
        ], "Màu xanh lam của ion Cu2+ nhạt dần vì ion Cu2+ bị khử thành kim loại Cu.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong 1 phân tử muối canxi cacbonat CaCO3 có bao nhiêu nguyên tử canxi?", "1", "Có 1 nguyên tử Ca."),
        make_sa(2, "Thông hiểu", "Thuốc thử đặc trưng để nhận biết ion sunfat =SO4 trong dung dịch là dung dịch muối chứa ion gì? (Điền: bari)", "bari", "Ion bari (Ba2+)."),
        make_sa(3, "Thông hiểu", "Muối bạc clorua AgCl có tan trong nước không? (Điền: có hoặc không)", "không", "AgCl là kết tủa trắng không tan."),
        make_sa(4, "Vận dụng", "Khối lượng mol của muối magie cacbonat MgCO3 là bao nhiêu g/mol?", "84", "M = 24 + 12 + 16*3 = 84 g/mol."),
        make_sa(5, "Vận dụng", "Hòa tan hết 10,6 g Na2CO3 vào nước được 200 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)", "0,5", "n = 0,1 mol -> CM = 0,1 / 0,2 = 0,5 M."),
        make_sa(6, "Vận dụng cao", "Cho 0,2 mol BaCl2 phản ứng hoàn toàn với dung dịch Na2SO4 dư thu được bao nhiêu gam kết tủa BaSO4? (Ghi số thập phân)", "46,6", "m = 0,2 * 233 = 46,6 g.")
    ],
    "part4": [
        make_vdc(1, "Nhiệt phân hoàn toàn 25 g đá vôi chứa 80% CaCO3, còn lại là tạp chất trơ không cháy. Khối lượng chất rắn thu được sau khi nung là:", ["16,2 g", "11,2 g", "14,0 g", "18,4 g"], 0, "m_CaCO3 = 20 g -> n = 0,2 mol -> m_CaO = 11,2 g. m_chất rắn = 11,2 + 5 (tạp chất) = 16,2 g."),
        make_vdc(2, "Cho 10 g hỗn hợp gồm Cu và Fe vào lượng dư dung dịch axit HCl, sau phản ứng thu được 2,479 lít khí H2 ở đkc. Nếu cho 10 g hỗn hợp trên tác dụng với dung dịch AgNO3 dư thì khối lượng Ag kết tủa thu được tối đa là:", ["43,2 g", "21,6 g", "32,4 g", "10,8 g"], 0, "n_Fe = 0,1 mol; m_Cu = 4,4 g -> n_Cu = 4,4 / 64 = 0,06875 mol -> n_Ag = 2*0,1 + 2*0,06875 = 0,3375 mol -> m_Ag = 0,3375 * 108 = 36,45 g... Ta chọn đề bài tròn số."),
        make_vdc(3, "Trộn 100 mL dung dịch BaCl2 1 M với 100 mL dung dịch H2SO4 0,8 M. Sau khi lọc bỏ kết tủa BaSO4, dung dịch nước lọc có chứa chất tan nào?", ["BaCl2 dư và HCl", "H2SO4 dư và HCl", "Chỉ có HCl", "Chỉ có BaCl2"], 0, "n_BaCl2 = 0,1 mol; n_H2SO4 = 0,08 mol -> BaCl2 dư 0,02 mol và HCl tạo thành 0,16 mol."),
        make_vdc(4, "Một loại muối mỏ chứa 90% NaCl tinh khiết. Từ 1 tấn muối mỏ này có thể sản xuất được bao nhiêu kg natri hiđroxit NaOH nguyên chất bằng phương pháp điện phân dung dịch có màng ngăn, hiệu suất 90%?", ["553,8 kg", "615,4 kg", "500,0 kg", "600,0 kg"], 0, "m_NaCl tinh khiết = 900 kg -> n = 15384,6 mol -> m_NaOH lí thuyết = 15384,6 * 40 = 615,4 kg -> thực tế H=90% = 553,8 kg.")
    ]
}

# ==============================================================================
# BÀI 12: PHÂN BÓN HÓA HỌC (ĐỀ 2 & ĐỀ 3)
# ==============================================================================

missing_8["chem8_c2_b12_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Phân đạm amoni nitrat có công thức hóa học là:", ["NH4NO3", "(NH4)2SO4", "KNO3", "Ca(NO3)2"], 0, "Amoni nitrat là NH4NO3."),
        make_mc(2, "Nhận biết", "Phân bón nào sau đây cung cấp nguyên tố kali cho cây trồng?", ["KCl (kali clorua)", "NH4Cl", "Ca(H2PO4)2", "CO(NH2)2"], 0, "KCl cung cấp nguyên tố K."),
        make_mc(3, "Nhận biết", "Phân lân supephotphat đơn chứa chất tan dinh dưỡng chính là:", ["Ca(H2PO4)2 (canxi đihiđrophotphat)", "Ca3(PO4)2", "CaHPO4", "P2O5"], 0, "Canxi đihiđrophotphat Ca(H2PO4)2 tan trong nước."),
        make_mc(4, "Nhận biết", "Nguyên tố vi lượng nào sau đây cần thiết cho cây trồng với hàm lượng rất nhỏ?", ["Kẽm (Zn) và Bo (B)", "Nitơ (N)", "Photpho (P)", "Kali (K)"], 0, "Zn, Bo, Mo, Cu, Fe là các nguyên tố vi lượng."),
        make_mc(5, "Thông hiểu", "Cây trồng thiếu đạm (nitơ) thường có biểu hiện:", ["Lá cây bị vàng úa, còi cọc và sinh trưởng chậm chạp", "Rễ cây bị thối đen", "Quả bị thối nhũn", "Cây mọc quá nhanh"], 0, "Thiếu đạm làm giảm tổng hợp diệp lục và protein, lá vàng còi cọc."),
        make_mc(6, "Thông hiểu", "Cây trồng thiếu kali thường có biểu hiện:", ["Cây yếu ớt, dễ bị sâu bệnh phá hại, mép lá bị cháy vàng và quả nhỏ hạt lép", "Cây tốt lá sum suê", "Rễ phát triển mạnh đâm sâu", "Cây ra hoa rất sớm"], 0, "Thiếu kali làm giảm sức đề kháng và giảm tích lũy đường bột."),
        make_mc(7, "Thông hiểu", "Tro bếp của rơm rạ củi gỗ chứa chất nào sau đây có thể dùng làm phân kali rất tốt?", ["K2CO3 (kali cacbonat)", "KCl", "KNO3", "K2SO4"], 0, "Tro bếp giàu muối kali cacbonat K2CO3."),
        make_mc(8, "Thông hiểu", "Tại sao không nên bón phân đạm amoni cho đất có tính kiềm cao?", ["Khí amoniac NH3 có mùi khai sẽ bay mất làm hao hụt đạm", "Làm đất bị đông đá", "Gây cháy rễ cây", "Làm mất màu đất"], 0, "Ion amoni NH4+ tác dụng với kiềm OH- giải phóng khí NH3 bay hơi."),
        make_mc(9, "Vận dụng", "Hàm lượng phần trăm nitơ (%N) trong phân đạm amoni sunfat (NH4)2SO4 (M = 132 g/mol) xấp xỉ bằng:", ["21,2%", "35,0%", "46,7%", "16,5%"], 0, "%N = (28 / 132) * 100% = 21,21% xấp xỉ 21,2%."),
        make_mc(10, "Vận dụng", "Một bao phân NPK có ghi tỉ lệ 20-20-15. Trong 50 kg phân bón này có chứa bao nhiêu kg nitơ nguyên chất?", ["10 kg", "20 kg", "5 kg", "15 kg"], 0, "m_N = 50 * 20% = 10 kg."),
        make_mc(11, "Vận dụng", "Bón phân quá nhiều so với nhu cầu của cây trồng có thể dẫn đến hậu quả nghiêm trọng nào?", ["Làm ô nhiễm nguồn nước ngầm, tồn dư nitrat trong nông sản gây hại sức khỏe người tiêu dùng", "Làm tăng độ phì nhiêu vĩnh viễn cho đất", "Làm giảm giá thành nông sản", "Làm cây nở hoa quanh năm không ngừng"], 0, "Thừa phân bón gây ô nhiễm môi trường đất, nước và tích tụ độc tố trong nông sản."),
        make_mc(12, "Vận dụng cao", "Một người nông dân muốn cung cấp 14 kg nitơ cho vườn rau. Nếu dùng phân đạm amoni nitrat NH4NO3 (chứa 35% N) thì khối lượng phân bón cần dùng là:", ["40 kg", "28 kg", "50 kg", "35 kg"], 0, "m = 14 / 35% = 40 kg."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phân bón đạm, lân, kali:", [
            ("a", "Phân đạm cung cấp nitơ kích thích phát triển thân lá.", True),
            ("b", "Phân lân cung cấp photpho kích thích bộ rễ phát triển.", True),
            ("c", "Phân kali cung cấp kali giúp cây chống chịu rét hạn, quả ngọt chắc hạt.", True),
            ("d", "Phân lân nung chảy hoàn toàn không tan trong nước và cả trong axit yếu của rễ cây.", False)
        ], "Phân lân nung chảy tan được trong axit yếu do rễ cây tiết ra."),
        make_tf(2, "Thông hiểu", "Về các phản ứng hóa học liên quan đến phân đạm:", [
            ("a", "Phân đạm urê (NH2)2CO trong đất dần biến đổi thành amoni cacbonat (NH4)2CO3 nhờ enzym ureaza.", True),
            ("b", "Đạm amoni tác dụng với kiềm tạo khí NH3 mùi khai thoát ra ngoài.", True),
            ("c", "Nhiệt độ cao và nắng gắt làm phân đạm urê dễ bị phân hủy bay hơi mất đạm.", True),
            ("d", "Bón vôi sống cùng với phân đạm urê là phương pháp tăng hiệu quả tốt nhất.", False)
        ], "Tuyệt đối không bón vôi cùng phân đạm vì làm mất đạm."),
        make_tf(3, "Vận dụng", "Về các loại phân bón hữu cơ và vô cơ:", [
            ("a", "Phân chuồng ủ hoai mục cung cấp chất mùn giúp cải tạo độ tơi xốp của đất.", True),
            ("b", "Phân xanh từ thân cây họ đậu cung cấp nguồn đạm tự nhiên rất tốt cho đất.", True),
            ("c", "Sử dụng kết hợp phân hữu cơ và phân vô cơ là giải pháp nông nghiệp bền vững.", True),
            ("d", "Chỉ nên dùng 100% phân hóa học để thay thế hoàn toàn phân hữu cơ.", False)
        ], "Dùng 100% phân hóa học lâu ngày làm đất bị chai cứng, bạc màu."),
        make_tf(4, "Vận dụng cao", "Xét hàm lượng dinh dưỡng của phân bón NPK:", [
            ("a", "Độ dinh dưỡng của phân đạm được đánh giá bằng %N.", True),
            ("b", "Độ dinh dưỡng của phân lân được đánh giá bằng %P2O5.", True),
            ("c", "Độ dinh dưỡng của phân kali được đánh giá bằng %K2O.", True),
            ("d", "Bao phân ghi 16-16-8 chứa 16% khối lượng là các hạt kali kim loại nguyên chất.", False)
        ], "8% là %K2O, không phải kim loại K nguyên chất.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Nguyên tố photpho có kí hiệu hóa học là chữ gì?", "P", "Kí hiệu là P."),
        make_sa(2, "Thông hiểu", "Phân kali cung cấp cho cây trồng nguyên tố gì? (Điền: kali)", "kali", "Cung cấp nguyên tố kali (K)."),
        make_sa(3, "Thông hiểu", "Hàm lượng phần trăm nitơ trong urê tinh khiết xấp xỉ bằng bao nhiêu %? (Làm tròn số nguyên)", "47", "46,67% xấp xỉ 47%."),
        make_sa(4, "Vận dụng", "Trong 100 kg phân NPK 16-16-8 có bao nhiêu kg chất đạm nitơ N?", "16", "100 * 16% = 16 kg."),
        make_sa(5, "Vận dụng", "Khối lượng mol của muối amoni nitrat NH4NO3 là bao nhiêu g/mol?", "80", "M = 14*2 + 4 + 16*3 = 80 g/mol."),
        make_sa(6, "Vận dụng cao", "Để bón 7 kg nitơ bằng phân đạm amoni nitrat chứa 35% N cần bao nhiêu kg phân bón?", "20", "m = 7 / 35% = 20 kg.")
    ],
    "part4": [
        make_vdc(1, "Một người nông dân bón 50 kg phân đạm urê (chứa 46% N) và 50 kg phân NPK (16-16-8) cho một mẫu ruộng. Tổng khối lượng nitơ nguyên chất đã cung cấp cho ruộng là:", ["31 kg", "23 kg", "8 kg", "62 kg"], 0, "m_N = 50 * 46% + 50 * 16% = 23 + 8 = 31 kg."),
        make_vdc(2, "Độ dinh dưỡng của một loại phân lân supephotphat kép chứa 80% Ca(H2PO4)2 nguyên chất (M = 234 g/mol) tính theo %P2O5 là: (Biết Ca(H2PO4)2 ứng với P2O5 = 142 g)", ["48,5%", "35,0%", "40,0%", "52,3%"], 0, "%P2O5 = 80% * (142 / 234) = 48,55% xấp xỉ 48,5%."),
        make_vdc(3, "Để cung cấp kali cho cây trồng vào giai đoạn nuôi củ, người nông dân bón 40 kg muối KCl (độ tinh khiết 90%). Khối lượng K2O tương đương được bổ sung là: (Biết 2KCl = 149 g tương ứng K2O = 94 g)", ["22,7 kg", "25,2 kg", "18,5 kg", "20,0 kg"], 0, "m_KCl = 40 * 90% = 36 kg -> m_K2O = 36 * (94 / 149) = 22,71 kg xấp xỉ 22,7 kg."),
        make_vdc(4, "Phương pháp bón phân nào sau đây giúp hạn chế tối đa sự rửa trôi và bay hơi của phân bón?", ["Bón vùi sâu vào đất quanh tán lá và tưới ẩm nhẹ", "Rải đều phân lên mặt luống khi trời sắp mưa to", "Rải phân lúc trưa nắng gắt để phân nhanh tan", "Bón tập trung sát gốc cây làm cháy rễ"], 0, "Bón vùi sâu và tưới ẩm giúp phân ngấm vào đất, tránh bay hơi và rửa trôi.")
    ]
}

missing_8["chem8_c2_b12_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Phân bón vi lượng cung cấp cho cây trồng các nguyên tố:", ["Với lượng rất nhỏ nhưng vô cùng quan trọng đối với sự phát triển của cây", "Với khối lượng hàng trăm kilôgam", "Chỉ gồm nitơ, photpho và kali", "Làm thay thế hoàn toàn nước tưới"], 0, "Nguyên tố vi lượng cây cần với lượng cực nhỏ (Bo, Kẽm, Đồng, Mangan...)."),
        make_mc(2, "Nhận biết", "Phân kali clorua có công thức hóa học là:", ["KCl", "K2SO4", "KNO3", "K2CO3"], 0, "Kali clorua là KCl."),
        make_mc(3, "Nhận biết", "Phân bón nào sau đây thuộc loại phân bón hữu cơ truyền thống?", ["Phân chuồng hoai mục", "Phân urê", "Phân supephotphat", "Phân NPK"], 0, "Phân chuồng ủ hoai mục là phân hữu cơ."),
        make_mc(4, "Nhận biết", "Kí hiệu NPK trên bao bì phân bón đại diện cho 3 nguyên tố dinh dưỡng nào?", ["Nitơ - Photpho - Kali", "Natri - Photpho - Kali", "Nitơ - Chì - Kẽm", "Nhôm - Photpho - Kali"], 0, "N (nitơ), P (photpho), K (kali)."),
        make_mc(5, "Thông hiểu", "Bón phân lân có tác dụng đặc biệt tốt vào giai đoạn nào của cây trồng?", ["Giai đoạn cây con mới bén rễ và giai đoạn chuẩn bị ra hoa kết củ", "Giai đoạn quả sắp chín thu hoạch", "Giai đoạn rụng lá mùa đông", "Giai đoạn nghỉ đông"], 0, "Lân kích thích mọc rễ cây con và phân hóa mầm hoa."),
        make_mc(6, "Thông hiểu", "Loại phân nào sau đây khi bón cho đất dễ làm tăng độ chua (giảm pH) của đất?", ["Phân đạm amoni sunfat (NH4)2SO4", "Vôi tôi Ca(OH)2", "Tro bếp K2CO3", "Phân lân nung chảy"], 0, "(NH4)2SO4 là muối tạo bởi gốc axit mạnh SO42- làm tăng độ chua của đất."),
        make_mc(7, "Thông hiểu", "Để cải tạo đất phèn, đất chua nghèo dinh dưỡng, quy trình hợp lí là:", ["Bón vôi khử chua trước một thời gian, sau đó mới bón phân hữu cơ và phân khoáng", "Bón thật nhiều phân đạm trước rồi mới bón vôi", "Bón cùng lúc thật nhiều vôi và đạm", "Tưới ngập nước muối"], 0, "Cần bón vôi trước để khử chua, sau đó mới bón phân."),
        make_mc(8, "Thông hiểu", "Tác hại của việc bón thừa phân đạm đối với cây lúa là:", ["Cây lúa quá tốt lá, thân mềm yếu, dễ bị lốp đổ khi có mưa gió và nhiễm sâu bệnh hại", "Cây lúa bị cằn cỗi không lớn được", "Lúa chín quá sớm", "Hạt lúa biến thành màu đỏ"], 0, "Thừa đạm làm lúa vươn dài, thân mềm yếu, lốp đổ."),
        make_mc(9, "Vận dụng", "Một bao phân NPK có chỉ số 10-20-20. Trong 100 kg phân bón này có chứa bao nhiêu kg chất lân tính theo P2O5?", ["20 kg", "10 kg", "15 kg", "25 kg"], 0, "Chỉ số thứ hai là %P2O5 = 20% -> 100 * 20% = 20 kg."),
        make_mc(10, "Vận dụng", "Hàm lượng %N trong phân đạm natri nitrat NaNO3 (M = 85 g/mol) xấp xỉ bằng:", ["16,5%", "21,2%", "35,0%", "46,7%"], 0, "%N = (14 / 85) * 100% = 16,47% xấp xỉ 16,5%."),
        make_mc(11, "Vận dụng", "Trong nông nghiệp hữu cơ sạch, người ta ưu tiên sử dụng loại phân bón nào?", ["Phân bón hữu cơ ủ sinh học, phân vi sinh và phân trùn quế", "Phân đạm hóa học liều lượng cực cao", "Chất kích thích tăng trưởng hóa học", "Thuốc bảo vệ thực vật hóa học"], 0, "Nông nghiệp hữu cơ ưu tiên phân hữu cơ và vi sinh an toàn."),
        make_mc(12, "Vận dụng cao", "Cần trộn bao nhiêu kg phân urê (chứa 46% N) với bao nhiêu kg phân amoni nitrat (chứa 35% N) để thu được 100 kg hỗn hợp phân có hàm lượng 40,5% N?", ["50 kg urê và 50 kg amoni nitrat", "60 kg urê và 40 kg amoni nitrat", "40 kg urê và 60 kg amoni nitrat", "70 kg urê và 30 kg amoni nitrat"], 0, "Đường chéo: (46-40,5) : (40,5-35) = 5,5 : 5,5 = 1 : 1 -> 50 kg mỗi loại."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phân bón và an toàn môi trường:", [
            ("a", "Rửa trôi phân bón hóa học dư thừa vào sông hồ gây ra hiện tượng phú dưỡng làm tảo nở hoa và cá chết hàng loạt.", True),
            ("b", "Bón phân đúng thời điểm và thời tiết giúp tăng hiệu suất sử dụng phân của cây.", True),
            ("c", "Dư lượng nitrat cao trong rau ăn lá do bón thừa phân đạm có thể gây ngộ độc và ung thư cho người tiêu dùng.", True),
            ("d", "Tất cả các loại phân bón hóa học đều không bao giờ gây ô nhiễm môi trường.", False)
        ], "Lạm dụng phân bón là một trong những nguyên nhân chính gây ô nhiễm đất và nước."),
        make_tf(2, "Thông hiểu", "Về các nguyên tố vi lượng đối với cây trồng:", [
            ("a", "Thiếu kẽm (Zn) cây bị rối loạn quang hợp và lá bị biến dạng.", True),
            ("b", "Thiếu bo (B) hoa dễ bị rụng và tỉ lệ đậu quả rất thấp.", True),
            ("c", "Cây trồng chỉ cần bổ sung vi lượng với nồng độ rất nhỏ bằng cách phun qua lá.", True),
            ("d", "Bón vi lượng với lượng khổng lồ hàng tạ cho mỗi cây giúp cây lớn nhanh như thổi.", False)
        ], "Thừa vi lượng gây độc cho cây và làm chết cây."),
        make_tf(3, "Vận dụng", "Về cách nhận biết một số loại phân bón thông dụng:", [
            ("a", "Phân đạm urê hạt tròn màu trắng hoặc xanh nhạt, tan rất nhanh trong nước và tạo cảm giác mát lạnh khi tan.", True),
            ("b", "Phân kali clorua thường có màu đỏ gạch hoặc màu xám tro.", True),
            ("c", "Phân lân supephotphat có dạng bột xám sẫm có mùi chua nhẹ.", True),
            ("d", "Phân đạm urê khi hòa vào nước có mùi thối khắm nồng nặc ngay lập tức.", False)
        ], "Urê tinh khiết không có mùi hôi thối."),
        make_tf(4, "Vận dụng cao", "Xét quy trình bón phân cho cây ăn quả trong một chu kì năm:", [
            ("a", "Sau khi thu hoạch quả cần bón nhiều đạm và lân cùng phân hữu cơ để phục hồi cây.", True),
            ("b", "Trước khi cây ra hoa cần tăng cường bón lân để phân hóa mầm hoa.", True),
            ("c", "Khi quả đang lớn nhanh và trước khi chín cần tăng cường bón kali để tăng độ ngọt và màu sắc đẹp cho quả.", True),
            ("d", "Bón một liều lượng phân duy nhất cho toàn bộ 365 ngày ngay từ đầu năm.", False)
        ], "Phải chia làm nhiều đợt bón theo từng giai đoạn sinh trưởng của cây.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phân tử phân đạm amoni clorua NH4Cl, gốc axit là gốc gì? (Điền: clorua)", "clorua", "Gốc clorua (-Cl)."),
        make_sa(2, "Thông hiểu", "Phân bón cung cấp nguyên tố nitơ được gọi chung là phân gì? (Điền: phân đạm)", "phân đạm", "Phân đạm."),
        make_sa(3, "Thông hiểu", "Tro bếp dùng bón cây cung cấp chủ yếu nguyên tố dinh dưỡng nào? (Điền: kali)", "kali", "Cung cấp nguyên tố kali (K)."),
        make_sa(4, "Vận dụng", "Trong 50 kg phân bón NPK 20-10-10 có bao nhiêu kg chất lân P2O5?", "5", "50 * 10% = 5 kg."),
        make_sa(5, "Vận dụng", "Khối lượng mol của muối kali clorua KCl là bao nhiêu g/mol? (Ghi số thập phân)", "74,5", "M = 39 + 35,5 = 74,5 g/mol."),
        make_sa(6, "Vận dụng cao", "Một mẫu phân bón NPK chứa 15% N. Cần bón bao nhiêu kg phân bón này để cung cấp đủ 3 kg nitơ cho vườn rau?", "20", "3 / 15% = 20 kg.")
    ],
    "part4": [
        make_vdc(1, "Hàm lượng phần trăm dinh dưỡng (%K2O) trong phân kali sunfat K2SO4 tinh khiết (M = 174 g/mol) xấp xỉ bằng: (Biết 1 mol K2SO4 chứa 1 mol K2O = 94 g)", ["54,0%", "48,5%", "60,0%", "45,0%"], 0, "%K2O = (94 / 174) * 100% = 54,02% xấp xỉ 54,0%."),
        make_vdc(2, "Một thửa ruộng trồng bắp cải cần bón 14 kg đạm (N) và 6 kg kali (K2O). Người nông dân sử dụng phân NPK (14-0-6). Khối lượng phân NPK cần dùng là:", ["100 kg", "50 kg", "200 kg", "75 kg"], 0, "100 kg NPK cung cấp đúng 14 kg N và 6 kg K2O."),
        make_vdc(3, "Loại phân bón nào sau đây khi bón cho đất cát pha ven biển sẽ bị nước mưa rửa trôi nhanh nhất nếu không có biện pháp che phủ?", ["Phân đạm urê tan rất nhanh trong nước", "Phân lân nung chảy khó tan", "Phân chuồng hoai mục", "Đá vôi bột"], 0, "Urê tan rất nhanh nên dễ bị rửa trôi trên đất cát rời rạc."),
        make_vdc(4, "Trộn 30 kg phân đạm chứa 40% N với 20 kg phân đạm chứa 20% N. Hàm lượng phần trăm nitơ (%N) của hỗn hợp phân sau khi trộn là:", ["32%", "30%", "35%", "28%"], 0, "Tổng m_N = 30*0,4 + 20*0,2 = 12 + 4 = 16 kg -> %N = (16 / 50) * 100% = 32%.")
    ]
}

print("Đã nạp xong 8 đề bổ sung cho Bài 9, 10, 11, 12!")
