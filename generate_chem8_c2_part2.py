# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - CHƯƠNG II: BÀI 9 (BASE - THANG pH) VÀ BÀI 10 (OXIDE) (6 ĐỀ ĐỘC LẬP 100%)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

exams_c2_p2 = {}

# ==============================================================================
# BÀI 9: BASE - THANG pH (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Định nghĩa bazơ, phân loại tan/không tan, thang pH ---
exams_c2_p2["chem8_c2_b9_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Bazơ (base) là hợp chất mà phân tử gồm có:", ["Một nguyên tử kim loại liên kết với một hay nhiều nhóm hiđroxit (-OH)", "Một hay nhiều nguyên tử H liên kết với gốc axit", "Hai nguyên tố trong đó có oxi", "Kim loại liên kết với gốc axit"], 0, "Bazơ gồm nguyên tử kim loại liên kết với một hay nhiều nhóm -OH."),
        make_mc(2, "Nhận biết", "Chất nào sau đây là một bazơ tan trong nước (kiềm)?", ["NaOH (natri hiđroxit)", "Cu(OH)2 (đồng(II) hiđroxit)", "Fe(OH)3 (sắt(III) hiđroxit)", "Al(OH)3 (nhôm hiđroxit)"], 0, "NaOH là bazơ kiềm tan tốt trong nước."),
        make_mc(3, "Nhận biết", "Dung dịch kiềm (bazơ tan) làm quỳ tím chuyển sang màu gì?", ["Màu xanh", "Màu đỏ", "Màu tím", "Màu vàng"], 0, "Dung dịch kiềm làm quỳ tím hóa xanh."),
        make_mc(4, "Nhận biết", "Dung dịch phenolphtalein không màu khi gặp dung dịch kiềm sẽ chuyển sang màu:", ["Màu hồng (hoặc đỏ cánh sen)", "Màu xanh lam", "Màu vàng", "Màu trắng đục"], 0, "Phenolphtalein chuyển sang màu hồng trong môi trường kiềm."),
        make_mc(5, "Thông hiểu", "Dãy gồm tất cả các bazơ tan trong nước (kiềm) là:", ["NaOH, KOH, Ca(OH)2, Ba(OH)2", "Cu(OH)2, Fe(OH)2, NaOH, KOH", "Al(OH)3, Ba(OH)2, Mg(OH)2, KOH", "Fe(OH)3, Ca(OH)2, Zn(OH)2, NaOH"], 0, "Các bazơ kiềm tan: Na, K, Ca, Ba."),
        make_mc(6, "Thông hiểu", "Một dung dịch có pH = 3. Môi trường của dung dịch này là:", ["Môi trường axit", "Môi trường bazơ (kiềm)", "Môi trường trung tính", "Môi trường đệm"], 0, "pH < 7 là môi trường axit."),
        make_mc(7, "Thông hiểu", "Nước cất tinh khiết ở 25 °C có giá trị pH bằng:", ["7", "0", "14", "1"], 0, "Nước tinh khiết trung tính có pH = 7."),
        make_mc(8, "Thông hiểu", "Dung dịch có pH = 11 làm quỳ tím đổi màu như thế nào?", ["Chuyển sang màu xanh", "Chuyển sang màu đỏ", "Không đổi màu", "Chuyển sang màu trắng"], 0, "pH > 7 là môi trường kiềm làm quỳ tím hóa xanh."),
        make_mc(9, "Vận dụng", "Để khử chua cho đất trồng nông nghiệp có pH < 5, người nông dân thường bón chất nào sau đây vào ruộng?", ["Vôi tôi Ca(OH)2 hoặc vôi sống CaO", "Phân đạm amoni nitrat", "Axit sunfuric loãng", "Muối ăn NaCl"], 0, "Vôi có tính kiềm giúp trung hòa axit dư thừa trong đất chua."),
        make_mc(10, "Vận dụng", "Khi cho dung dịch axit HCl vào dung dịch NaOH có sẵn vài giọt phenolphtalein (màu hồng), hiện tượng quan sát được tại điểm tương đương là:", ["Màu hồng biến mất thành không màu", "Màu hồng chuyển sang màu xanh", "Xuất hiện kết tủa màu nâu đỏ", "Dung dịch sôi sùng sục bốc khói đen"], 0, "Khi axit trung hòa hết kiềm, phenolphtalein mất màu hồng trở lại không màu."),
        make_mc(11, "Vận dụng", "Khối lượng NaOH có trong 200 mL dung dịch NaOH 1,5 M là:", ["12 g", "6 g", "8 g", "16 g"], 0, "n = 0,2 * 1,5 = 0,3 mol -> m = 0,3 * 40 = 12 g."),
        make_mc(12, "Vận dụng cao", "Trung hòa hoàn toàn 100 mL dung dịch Ba(OH)2 0,1 M cần dùng V mL dung dịch HCl 0,2 M. Giá trị của V là:", ["100 mL", "50 mL", "200 mL", "150 mL"], 0, "Ba(OH)2 + 2HCl -> BaCl2 + 2H2O. n_Ba(OH)2 = 0,01 mol -> n_HCl = 0,02 mol -> V = 0,02 / 0,2 = 0,1 L = 100 mL."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phân loại bazơ theo tính tan:", [
            ("a", "Bazơ tan trong nước được gọi là kiềm: NaOH, KOH, Ba(OH)2, Ca(OH)2.", True),
            ("b", "Bazơ không tan trong nước: Cu(OH)2, Fe(OH)2, Fe(OH)3, Al(OH)3, Mg(OH)2.", True),
            ("c", "Tất cả các bazơ đều làm đổi màu quỳ tím sang màu xanh.", False),
            ("d", "Chỉ có các dung dịch bazơ tan (kiềm) mới làm đổi màu quỳ tím và phenolphtalein.", True)
        ], "Bazơ không tan không phân li ion OH- nên không làm đổi màu chất chỉ thị."),
        make_tf(2, "Thông hiểu", "Về thang đo pH trong đời sống:", [
            ("a", "Thang pH thường có giá trị từ 1 đến 14 biểu thị độ axit hay độ kiềm của dung dịch.", True),
            ("b", "Dung dịch có pH < 7 có môi trường axit; pH càng nhỏ tính axit càng mạnh.", True),
            ("c", "Dung dịch có pH = 7 là môi trường trung tính.", True),
            ("d", "Dung dịch có pH > 7 có môi trường bazơ; pH càng gần 7 tính bazơ càng mạnh.", False)
        ], "pH càng lớn (tiến về 14) tính bazơ càng mạnh."),
        make_tf(3, "Vận dụng", "Về pH của các chất thường gặp:", [
            ("a", "Nước chanh, giấm ăn có pH < 7.", True),
            ("b", "Nước xà phòng, nước vôi có pH > 7.", True),
            ("c", "Dịch máu người khỏe mạnh có pH hơi kiềm ổn định khoảng 7,35 - 7,45.", True),
            ("d", "Dịch vị dạ dày người có tính kiềm mạnh với pH khoảng 10 - 12.", False)
        ], "Dịch vị dạ dày có tính axit mạnh với pH khoảng 1,5 - 3,5."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng nhiệt phân các bazơ không tan:", [
            ("a", "Các bazơ không tan bị nhiệt phân hủy tạo thành oxit kim loại tương ứng và nước.", True),
            ("b", "Nung Cu(OH)2 màu xanh lam thu được chất rắn CuO màu đen và hơi nước.", True),
            ("c", "Các bazơ kiềm như NaOH, KOH bị nung ở ngọn lửa đèn cồn cũng bị phân hủy tạo Na2O và H2O.", False),
            ("d", "Phương trình: 2Fe(OH)3 -> Fe2O3 + 3H2O.", True)
        ], "Bazơ kiềm bền với nhiệt, không bị phân hủy bởi đèn cồn thông thường.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong công thức của bazơ, nhóm nguyên tử nào liên kết với nguyên tử kim loại? (Điền: OH)", "OH", "Nhóm hiđroxit (-OH)."),
        make_sa(2, "Thông hiểu", "Dung dịch nước xà phòng làm giấy quỳ tím chuyển sang màu gì?", "xanh", "Xà phòng có tính kiềm làm quỳ tím hóa xanh."),
        make_sa(3, "Thông hiểu", "Một dung dịch có pH = 9. Môi trường của dung dịch này là axit hay bazơ? (Điền: bazơ)", "bazơ", "pH > 7 là môi trường bazơ."),
        make_sa(4, "Vận dụng", "Khối lượng mol của canxi hiđroxit Ca(OH)2 là bao nhiêu g/mol?", "74", "M = 40 + (16+1)*2 = 74 g/mol."),
        make_sa(5, "Vận dụng", "Hòa tan 0,2 mol KOH vào nước được 500 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)", "0,4", "CM = 0,2 / 0,5 = 0,4 M."),
        make_sa(6, "Vận dụng cao", "Nung hoàn toàn 9,8 g Cu(OH)2 thu được bao nhiêu gam bột CuO màu đen?", "8", "n = 9,8 / 98 = 0,1 mol -> m_CuO = 0,1 * 80 = 8 g.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn m gam kim loại natri vào nước dư thu được 100 mL dung dịch NaOH 1 M và giải phóng V lít khí H2 ở đkc. Giá trị của m là:", ["2,3 g", "4,6 g", "1,15 g", "3,45 g"], 0, "n_NaOH = 0,1 mol -> n_Na = 0,1 mol -> m_Na = 0,1 * 23 = 2,3 g."),
        make_vdc(2, "Cho 200 mL dung dịch NaOH 1 M tác dụng hoàn toàn với 100 mL dung dịch FeCl3 0,5 M. Khối lượng kết tủa Fe(OH)3 màu nâu đỏ thu được là:", ["5,35 g", "10,7 g", "2,675 g", "8,0 g"], 0, "FeCl3 + 3NaOH -> Fe(OH)3 + 3NaCl. n_NaOH = 0,2 mol; n_FeCl3 = 0,05 mol -> NaOH dư, tính theo FeCl3 -> m_Fe(OH)3 = 0,05 * 107 = 5,35 g."),
        make_vdc(3, "Một cốc chứa dung dịch H2SO4 có pH = 2. Để đưa pH của dung dịch về mức trung tính (pH = 7), người ta cần nhỏ vào cốc lượng vừa đủ dung dịch:", ["Dung dịch kiềm như NaOH hoặc Ca(OH)2", "Nước cất tinh khiết vô hạn", "Axit HCl đậm đặc", "Dung dịch giấm ăn"], 0, "Dùng dung dịch kiềm để trung hòa axit."),
        make_vdc(4, "Nhiệt phân hoàn toàn m gam Fe(OH)3 thu được 16 g bột Fe2O3 màu nâu đỏ. Giá trị của m là:", ["21,4 g", "10,7 g", "32,1 g", "16,0 g"], 0, "2Fe(OH)3 -> Fe2O3 + 3H2O. n_Fe2O3 = 0,1 mol -> n_Fe(OH)3 = 0,2 mol -> m = 0,2 * 107 = 21,4 g.")
    ]
}

# --- BÀI 10: OXIDE (3 ĐỀ) ---
# --- ĐỀ 1: Định nghĩa oxit, phân loại 4 nhóm oxit ---
exams_c2_p2["chem8_c2_b10_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Oxit là hợp chất gồm có:", ["Hai nguyên tố, trong đó có một nguyên tố là oxi", "Kim loại liên kết với nhóm hiđroxit", "Hiđro liên kết với gốc axit", "Các nguyên tố phi kim liên kết với nhau"], 0, "Oxit là hợp chất của 2 nguyên tố trong đó có 1 nguyên tố là oxi."),
        make_mc(2, "Nhận biết", "Chất nào sau đây là một oxit bazơ?", ["CaO (canxi oxit)", "CO2 (cacbon đioxit)", "SO2 (lưu huỳnh đioxit)", "P2O5 (điphotpho pentaoxit)"], 0, "CaO là oxit bazơ tương ứng với bazơ Ca(OH)2."),
        make_mc(3, "Nhận biết", "Chất nào sau đây là một oxit axit?", ["SO3 (lưu huỳnh trioxit)", "Na2O (natri oxit)", "CuO (đồng(II) oxit)", "BaO (bari oxit)"], 0, "SO3 là oxit axit tương ứng với axit H2SO4."),
        make_mc(4, "Nhận biết", "Oxit nào sau đây tác dụng với nước tạo thành dung dịch làm quỳ tím hóa xanh?", ["Na2O", "P2O5", "CO2", "SO2"], 0, "Na2O + H2O -> 2NaOH (dung dịch kiềm làm quỳ tím hóa xanh)."),
        make_mc(5, "Thông hiểu", "Cho các oxit: CO2, SO2, CaO, Na2O, CuO, P2O5. Số oxit axit trong dãy là:", ["3", "2", "4", "1"], 0, "Gồm CO2, SO2, P2O5 (3 oxit axit)."),
        make_mc(6, "Thông hiểu", "Khí CO và NO thuộc loại oxit nào sau đây?", ["Oxit trung tính (không tạo muối)", "Oxit axit", "Oxit bazơ", "Oxit lưỡng tính"], 0, "CO và NO không tác dụng với axit, bazơ ở điều kiện thường nên gọi là oxit trung tính."),
        make_mc(7, "Thông hiểu", "Oxit lưỡng tính là oxit:", ["Vừa tác dụng được với dung dịch axit, vừa tác dụng được với dung dịch bazơ", "Chỉ tác dụng với nước", "Không tác dụng với chất nào", "Làm đổi màu quỳ tím sang vàng"], 0, "Định nghĩa: Oxit lưỡng tính tác dụng với cả axit và bazơ (ví dụ Al2O3, ZnO)."),
        make_mc(8, "Thông hiểu", "Sản phẩm của phản ứng giữa canxi oxit CaO với nước là:", ["Canxi hiđroxit Ca(OH)2 tỏa nhiều nhiệt", "Canxi cacbonat", "Khí hiđro", "Canxi clorua"], 0, "CaO + H2O -> Ca(OH)2 (phản ứng tôi vôi tỏa nhiệt mạnh)."),
        make_mc(9, "Vận dụng", "Dẫn luồng khí CO2 dư vào dung dịch nước vôi trong Ca(OH)2, hiện tượng quan sát được là:", ["Dung dịch bị vẩn đục màu trắng do tạo kết tủa CaCO3", "Dung dịch chuyển sang màu xanh lam", "Có bọt khí cháy bùng lên", "Không có hiện tượng gì"], 0, "CO2 + Ca(OH)2 -> CaCO3 (kết tủa trắng) + H2O."),
        make_mc(10, "Vận dụng", "Hòa tan hoàn toàn 6,2 g Na2O vào nước thu được 200 mL dung dịch NaOH. Nồng độ mol của dung dịch NaOH là:", ["1 M", "0,5 M", "2 M", "0,25 M"], 0, "Na2O + H2O -> 2NaOH. n_Na2O = 0,1 mol -> n_NaOH = 0,2 mol -> CM = 0,2 / 0,2 = 1 M."),
        make_mc(11, "Vận dụng", "Khối lượng CuO cần dùng để phản ứng vừa đủ với 100 mL dung dịch HCl 1 M là:", ["4,0 g", "8,0 g", "2,0 g", "6,4 g"], 0, "CuO + 2HCl -> CuCl2 + H2O. n_HCl = 0,1 mol -> n_CuO = 0,05 mol -> m = 0,05 * 80 = 4,0 g."),
        make_mc(12, "Vận dụng cao", "Dẫn 3,7185 lít khí CO2 ở đkc (tương ứng 0,15 mol) vào dung dịch chứa 0,1 mol Ca(OH)2. Sau phản ứng hoàn toàn thu được m gam kết tủa CaCO3. Giá trị của m là:", ["5,0 g", "10,0 g", "15,0 g", "7,5 g"], 0, "T = n_CO2 / n_Ca(OH)2 = 1,5 -> tạo 0,05 mol CaCO3 và 0,05 mol Ca(HCO3)2 -> m = 0,05 * 100 = 5,0 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phân loại oxit:", [
            ("a", "Oxit bazơ là oxit tác dụng với axit tạo thành muối và nước.", True),
            ("b", "Oxit axit thường là oxit của phi kim tương ứng với một axit.", True),
            ("c", "Al2O3 và ZnO là các oxit lưỡng tính.", True),
            ("d", "Tất cả các oxit kim loại đều là oxit bazơ tan tốt trong nước.", False)
        ], "Rất nhiều oxit kim loại như CuO, Fe2O3 không tan trong nước."),
        make_tf(2, "Thông hiểu", "Về tác dụng của oxit với nước:", [
            ("a", "Các oxit bazơ tan như Na2O, K2O, CaO, BaO tác dụng với nước tạo dung dịch kiềm.", True),
            ("b", "Nhiều oxit axit như SO2, SO3, P2O5 tác dụng với nước tạo dung dịch axit tương ứng.", True),
            ("c", "Oxit sắt Fe2O3 tác dụng mãnh liệt với nước tạo bazơ Fe(OH)3.", False),
            ("d", "Khí cacbon monooxit CO tác dụng với nước tạo axit cacbonic.", False)
        ], "Fe2O3 và CO đều không tác dụng với nước ở điều kiện thường."),
        make_tf(3, "Vận dụng", "Cho các phản ứng sau ở điều kiện thích hợp:", [
            ("a", "CaO + CO2 -> CaCO3.", True),
            ("b", "CuO + 2HCl -> CuCl2 + H2O.", True),
            ("c", "P2O5 + 3H2O -> 2H3PO4.", True),
            ("d", "CO2 + H2O -> H2SO4.", False)
        ], "CO2 + H2O tạo H2CO3."),
        make_tf(4, "Vận dụng cao", "Về oxit trong công nghiệp và môi trường:", [
            ("a", "Khí SO2 và NO2 là thủ phạm chính gây ra hiện tượng mưa axit phá hủy môi trường.", True),
            ("b", "Vôi sống CaO được dùng để khử chua đất trồng và xử lý nước thải công nghiệp.", True),
            ("c", "Khí CO là oxit trung tính không màu, không mùi, độc hại do kết hợp với hemoglobin trong máu.", True),
            ("d", "Khí CO2 là khí độc nguy hiểm bậc một có thể gây nổ ngay ở nhiệt độ phòng.", False)
        ], "CO2 không độc hại trực tiếp như CO và không gây nổ mà chỉ gây ngạt khi nồng độ quá cao.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong một phân tử oxit luôn chứa nguyên tử của nguyên tố nào? (Điền: oxi)", "oxi", "Nguyên tố oxi (O)."),
        make_sa(2, "Thông hiểu", "Cho các oxit: Na2O, SO2, CaO, CO2, CuO. Có bao nhiêu oxit bazơ trong dãy?", "3", "Na2O, CaO, CuO (3 oxit bazơ)."),
        make_sa(3, "Thông hiểu", "Sản phẩm của phản ứng giữa P2O5 và nước làm quỳ tím chuyển sang màu gì?", "đỏ", "P2O5 + 3H2O -> 2H3PO4 (axit làm quỳ tím hóa đỏ)."),
        make_sa(4, "Vận dụng", "Khối lượng mol của oxit sắt Fe2O3 là bao nhiêu g/mol?", "160", "M = 56*2 + 16*3 = 160 g/mol."),
        make_sa(5, "Vận dụng", "Hòa tan 8 g CuO bằng dung dịch H2SO4 loãng vừa đủ. Khối lượng muối CuSO4 thu được là bao nhiêu gam?", "16", "n = 0,1 mol -> m = 0,1 * 160 = 16 g."),
        make_sa(6, "Vận dụng cao", "Dẫn 2,479 lít khí CO2 (đkc) vào dung dịch Ca(OH)2 dư. Khối lượng kết tủa CaCO3 thu được là bao nhiêu gam?", "10", "n = 0,1 mol -> m = 0,1 * 100 = 10 g.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn 20 g hỗn hợp gồm CuO và Fe2O3 cần vừa đủ 500 mL dung dịch axit HCl 1 M. Khối lượng muối clorua thu được trong dung dịch sau phản ứng là:", ["33,75 g", "35,25 g", "28,5 g", "40,0 g"], 0, "n_HCl = 0,5 mol -> n_O trong oxit = 0,25 mol -> m_O = 4 g -> m_KL = 20 - 4 = 16 g. m_muối = 16 + 0,5 * 35,5 = 33,75 g."),
        make_vdc(2, "Khí CO2 có lẫn tạp chất là khí SO2. Để thu được khí CO2 tinh khiết, người ta dẫn hỗn hợp khí qua bình đựng lượng dư dung dịch nào sau đây?", ["Dung dịch nước brom (Br2) vì SO2 phản ứng làm mất màu brom còn CO2 không phản ứng", "Dung dịch nước vôi trong Ca(OH)2", "Dung dịch NaOH", "Dung dịch Ba(OH)2"], 0, "Nước brom giữ lại SO2 (SO2 + Br2 + 2H2O -> H2SO4 + 2HBr), khí CO2 thoát ra ngoài tinh khiết."),
        make_vdc(3, "Cho m gam hỗn hợp gồm Na2O và K2O có tỉ lệ mol 1 : 1 tác dụng hoàn toàn với nước thu được dung dịch chứa 0,2 mol NaOH và 0,2 mol KOH. Giá trị của m là:", ["15,6 g", "31,2 g", "7,8 g", "23,4 g"], 0, "n_Na2O = 0,1 mol; n_K2O = 0,1 mol -> m = 0,1*62 + 0,1*94 = 6,2 + 9,4 = 15,6 g."),
        make_vdc(4, "Một oxit của kim loại M hóa trị III có chứa 70% kim loại M về khối lượng. Kim loại M là:", ["Sắt (Fe = 56)", "Nhôm (Al = 27)", "Crom (Cr = 52)", "Mangan (Mn = 55)"], 0, "M2O3: 2M / (2M + 48) = 0,7 -> 2M = 1,4M + 33,6 -> 0,6M = 33,6 -> M = 56 (Fe).")
    ]
}

print("Đã nạp xong Bài 9 và Bài 10 (mỗi bài có đề độc lập 100%)")
