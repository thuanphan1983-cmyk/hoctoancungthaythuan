# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - ÔN TẬP CUỐI CHƯƠNG I: PHẢN ỨNG HÓA HỌC (5 ĐỀ ĐỘC LẬP 100%)
Đảm bảo 5 đề hoàn toàn khác nhau về câu hỏi, số liệu, chất và đáp án.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

exams_c1_rev = {}

# ==============================================================================
# ÔN TẬP CUỐI CHƯƠNG I (5 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Tổng hợp cơ bản và phân tích định tính Chương I ---
exams_c1_rev["chem8_c1_rev_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Dấu hiệu rõ ràng nhất để phân biệt biến đổi hóa học với biến đổi vật lí là:", ["Có sự tạo thành chất mới", "Có sự thay đổi hình dạng", "Chất chuyển từ thể rắn sang thể lỏng", "Chất tan vào trong nước"], 0, "Bản chất của biến đổi hóa học là sinh ra chất mới."),
        make_mc(2, "Nhận biết", "Trong một phản ứng hóa học, liên kết giữa các nguyên tử:", ["Bị thay đổi làm phân tử này biến đổi thành phân tử khác", "Luôn được giữ nguyên không đổi", "Bị biến mất hoàn toàn không hình thành liên kết mới", "Làm thay đổi số proton của nguyên tử"], 0, "Chỉ có liên kết giữa các nguyên tử thay đổi."),
        make_mc(3, "Nhận biết", "Phản ứng tỏa nhiệt là phản ứng:", ["Giải phóng năng lượng dưới dạng nhiệt ra môi trường", "Hấp thụ nhiệt lượng từ môi trường", "Làm nhiệt độ môi trường hạ thấp", "Không làm thay đổi nhiệt độ"], 0, "Phản ứng tỏa nhiệt giải phóng nhiệt ra môi trường."),
        make_mc(4, "Nhận biết", "Theo định luật bảo toàn khối lượng, trong một phản ứng hóa học:", ["Tổng khối lượng chất sản phẩm bằng tổng khối lượng chất tham gia", "Khối lượng của từng chất không đổi", "Tổng thể tích các chất bảo toàn", "Số phân tử luôn bằng nhau"], 0, "Tổng khối lượng sản phẩm bằng tổng khối lượng chất phản ứng."),
        make_mc(5, "Thông hiểu", "Khối lượng mol của khí carbon dioxide (CO2) là:", ["44 g/mol", "28 g/mol", "32 g/mol", "16 g/mol"], 0, "M_CO2 = 12 + 16*2 = 44 g/mol."),
        make_mc(6, "Thông hiểu", "Thể tích của 0,1 mol khí oxi ở điều kiện chuẩn (25 °C, 1 bar) là:", ["2,479 lít", "22,4 lít", "2,24 lít", "24,79 lít"], 0, "V = 0,1 * 24,79 = 2,479 L."),
        make_mc(7, "Thông hiểu", "Khí nào sau đây nặng hơn không khí?", ["CO2 (M = 44)", "CH4 (M = 16)", "H2 (M = 2)", "NH3 (M = 17)"], 0, "M_CO2 = 44 > 29 nên nặng hơn không khí."),
        make_mc(8, "Thông hiểu", "Hòa tan 15 g muối vào 85 g nước thu được dung dịch có nồng độ phần trăm là:", ["15%", "17,6%", "10%", "20%"], 0, "m_dd = 15 + 85 = 100 g -> C% = 15%."),
        make_mc(9, "Vận dụng", "Nồng độ mol của 200 mL dung dịch chứa 0,4 mol NaOH là:", ["2 M", "1 M", "0,8 M", "0,2 M"], 0, "CM = 0,4 / 0,2 = 2 M."),
        make_mc(10, "Vận dụng", "Khi cho bột kẽm vào dung dịch HCl, thao tác nào sau đây KHÔNG LÀM TĂNG tốc độ phản ứng?", ["Thêm nước cất vào ống nghiệm", "Đun nóng dung dịch axit", "Dùng bột kẽm thay cho kẽm viên", "Dùng axit HCl nồng độ cao hơn"], 0, "Thêm nước làm loãng axit, giảm nồng độ, làm giảm tốc độ phản ứng."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 3,6 g kim loại magie trong bình chứa khí oxi dư thu được 6,0 g magie oxit (MgO). Khối lượng khí oxi đã phản ứng là:", ["2,4 g", "1,2 g", "3,2 g", "1,6 g"], 0, "m_O2 = 6,0 - 3,6 = 2,4 g."),
        make_mc(12, "Vận dụng cao", "Hòa tan hết 5,4 g kim loại nhôm vào dung dịch axit sunfuric loãng vừa đủ. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:", ["7,437 lít", "6,72 lít", "4,958 lít", "2,479 lít"], 0, "2Al + 3H2SO4 -> Al2(SO4)3 + 3H2. n_Al = 0,2 mol -> n_H2 = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các biến đổi chất trong đời sống:", [
            ("a", "Nước sôi bốc hơi là biến đổi vật lí.", True),
            ("b", "Đốt cháy cồn trong đĩa sứ là biến đổi hóa học.", True),
            ("c", "Gỉ sắt hình thành trên bề mặt kim loại là biến đổi vật lí.", False),
            ("d", "Lên men rượu từ cơm nếp là biến đổi hóa học.", True)
        ], "Gỉ sắt là quá trình sắt bị oxi hóa tạo chất mới (hóa học)."),
        make_tf(2, "Thông hiểu", "Về định luật bảo toàn khối lượng và phương trình hóa học:", [
            ("a", "Trong phản ứng hóa học, số nguyên tử của mỗi nguyên tố luôn được bảo toàn.", True),
            ("b", "Khi nung đá vôi, khối lượng chất rắn thu được giảm đi do khí CO2 đã bay đi.", True),
            ("c", "Hệ số cân bằng trong phương trình hóa học có thể là phân số nguyên tố.", False),
            ("d", "Cân bằng phương trình: 4Al + 3O2 -> 2Al2O3 đã chính xác.", True)
        ], "Hệ số phương trình phải là các số nguyên tối giản."),
        make_tf(3, "Vận dụng", "Về chất khí và dung dịch ở điều kiện chuẩn:", [
            ("a", "Ở đkc (25 °C, 1 bar), 1 mol chất khí bất kì đều chiếm thể tích 24,79 lít.", True),
            ("b", "Khí hiđro nhẹ hơn không khí nên được thu bằng cách úp ngược ống nghiệm.", True),
            ("c", "Pha 20 g đường vào 180 g nước thu được dung dịch đường 10%.", True),
            ("d", "Dung dịch bão hòa là dung dịch có thể hòa tan thêm chất tan ở nhiệt độ đó.", False)
        ], "Dung dịch bão hòa không thể hòa tan thêm chất tan ở nhiệt độ đó."),
        make_tf(4, "Vận dụng cao", "Về tốc độ phản ứng và chất xúc tác:", [
            ("a", "Tăng nồng độ chất phản ứng làm tăng số va chạm hiệu quả giữa các phân tử, làm tăng tốc độ phản ứng.", True),
            ("b", "Chất xúc tác làm tăng tốc độ phản ứng và bị tiêu hao hoàn toàn sau phản ứng.", False),
            ("c", "Nhiệt độ càng cao thì tốc độ của phần lớn các phản ứng hóa học càng tăng.", True),
            ("d", "Bảo quản thực phẩm trong tủ lạnh giúp làm chậm tốc độ hư hỏng thức ăn.", True)
        ], "Chất xúc tác không bị tiêu hao sau phản ứng.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong một phản ứng hóa học, đại lượng nào được bảo toàn giữa chất tham gia và sản phẩm? (Điền: khối lượng)", "khối lượng", "Khối lượng được bảo toàn."),
        make_sa(2, "Thông hiểu", "Số mol của 4,958 lít khí N2 ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu mol? (Ghi số thập phân)", "0,2", "4,958 / 24,79 = 0,2 mol."),
        make_sa(3, "Thông hiểu", "Khối lượng mol của muối ăn NaCl là bao nhiêu g/mol? (Ghi số thập phân)", "58,5", "M = 23 + 35,5 = 58,5 g/mol."),
        make_sa(4, "Vận dụng", "Cần lấy bao nhiêu gam muối ăn NaCl để hòa tan vào nước thu được 500 g dung dịch NaCl 2%?", "10", "m = 500 * 2% = 10 g."),
        make_sa(5, "Vận dụng", "Nung 10 g CaCO3 thu được 5,6 g CaO và bao nhiêu gam khí CO2? (Ghi số thập phân)", "4,4", "10 - 5,6 = 4,4 g."),
        make_sa(6, "Vận dụng cao", "Đốt cháy 0,1 mol khí CH4 cần bao nhiêu lít khí oxi ở đkc? (Ghi số thập phân)", "4,958", "CH4 + 2O2 -> cần 0,2 mol O2 = 0,2 * 24,79 = 4,958 L.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn 11,2 g bột sắt vào dung dịch HCl 1 M vừa đủ. Thể tích dung dịch HCl cần dùng là:", ["400 mL", "200 mL", "300 mL", "500 mL"], 0, "n_Fe = 0,2 mol -> n_HCl = 0,4 mol -> V = 0,4 / 1 = 0,4 L = 400 mL."),
        make_vdc(2, "Hỗn hợp khí X gồm 0,1 mol CO2 và 0,4 mol N2. Khối lượng mol trung bình của hỗn hợp X là:", ["31,2 g/mol", "28,8 g/mol", "32,0 g/mol", "30,0 g/mol"], 0, "M_tb = (0,1*44 + 0,4*28) / 0,5 = (4,4 + 11,2) / 0,5 = 31,2 g/mol."),
        make_vdc(3, "Đốt cháy hoàn toàn 6,2 g photpho trong khí oxi dư thu được m gam chất rắn P2O5. Giá trị của m là:", ["14,2 g", "7,1 g", "28,4 g", "10,5 g"], 0, "4P + 5O2 -> 2P2O5. n_P = 0,2 mol -> n_P2O5 = 0,1 mol -> m = 0,1 * 142 = 14,2 g."),
        make_vdc(4, "Trộn 100 mL dung dịch NaOH 1 M với 100 mL dung dịch H2SO4 0,5 M. Nồng độ mol của muối Na2SO4 thu được trong dung dịch sau phản ứng là:", ["0,25 M", "0,5 M", "0,1 M", "0,2 M"], 0, "2NaOH + H2SO4 -> Na2SO4 + 2H2O. n_Na2SO4 = 0,05 mol; V = 0,2 L -> CM = 0,05 / 0,2 = 0,25 M.")
    ]
}

# --- ĐỀ 2: Tính toán hóa học định lượng, nồng độ và tỉ khối ---
exams_c1_rev["chem8_c1_rev_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Quá trình nào sau đây là phản ứng thu nhiệt?", ["Nung đá vôi trong lò vôi", "Đốt cháy than hoa trong bếp", "Thả vôi sống vào nước", "Đốt cháy que diêm"], 0, "Nung đá vôi cần cấp nhiệt liên tục (phản ứng thu nhiệt)."),
        make_mc(2, "Nhận biết", "Khối lượng của 1 mol nguyên tử đồng (Cu) là:", ["64 g", "32 g", "56 g", "27 g"], 0, "M_Cu = 64 g/mol."),
        make_mc(3, "Nhận biết", "Tỉ khối của khí oxi đối với khí metan (CH4) là:", ["2", "0,5", "1,5", "4"], 0, "d = 32 / 16 = 2."),
        make_mc(4, "Nhận biết", "Nồng độ mol của một dung dịch được xác định bằng biểu thức:", ["CM = n / V", "CM = m / V", "CM = V / n", "CM = n * V"], 0, "CM = n / V (mol/L)."),
        make_mc(5, "Thông hiểu", "Cho phương trình phản ứng: Zn + 2HCl -> ZnCl2 + H2. Tỉ lệ số mol giữa Zn và H2 là:", ["1 : 1", "1 : 2", "2 : 1", "1 : 3"], 0, "Hệ số của Zn và H2 đều là 1."),
        make_mc(6, "Thông hiểu", "Số mol của 12,395 lít khí hiđro ở điều kiện chuẩn (25 °C, 1 bar) là:", ["0,5 mol", "0,25 mol", "1,0 mol", "0,1 mol"], 0, "n = 12,395 / 24,79 = 0,5 mol."),
        make_mc(7, "Thông hiểu", "Hòa tan 8 g NaOH vào nước thu được 200 mL dung dịch. Nồng độ mol của dung dịch NaOH là:", ["1 M", "2 M", "0,5 M", "0,1 M"], 0, "n = 8 / 40 = 0,2 mol -> CM = 0,2 / 0,2 = 1 M."),
        make_mc(8, "Thông hiểu", "Dẫn khí H2 dư qua 16 g bột CuO nung nóng thu được m gam kim loại Cu. Giá trị của m là:", ["12,8 g", "6,4 g", "16,0 g", "8,0 g"], 0, "H2 + CuO -> Cu + H2O. n_CuO = 0,2 mol -> m_Cu = 0,2 * 64 = 12,8 g."),
        make_mc(9, "Vận dụng", "Hòa tan 20 g muối ăn vào nước thu được dung dịch có nồng độ 10%. Khối lượng dung dịch thu được là:", ["200 g", "180 g", "220 g", "100 g"], 0, "m_dd = 20 / 10% = 200 g."),
        make_mc(10, "Vận dụng", "Để làm tăng tốc độ phân hủy của dung dịch H2O2 giải phóng khí oxi, người ta thường cho thêm vào một lượng nhỏ bột:", ["MnO2", "NaCl", "Đường", "Vôi sống"], 0, "MnO2 là chất xúc tác cho phản ứng phân hủy H2O2."),
        make_mc(11, "Vận dụng", "Khí A có tỉ khối đối với không khí là 1,586. Khối lượng mol của khí A là:", ["46 g/mol (NO2)", "34 g/mol (H2S)", "28 g/mol (N2)", "64 g/mol (SO2)"], 0, "M = 1,586 * 29 = 46 g/mol (NO2)."),
        make_mc(12, "Vận dụng cao", "Hòa tan hết 4,8 g kim loại magie vào 150 g dung dịch HCl dư. Khối lượng dung dịch sau phản ứng tăng thêm so với dung dịch axit ban đầu là:", ["4,4 g", "4,8 g", "4,6 g", "4,2 g"], 0, "Mg + 2HCl -> MgCl2 + H2. n_Mg = 0,2 mol -> n_H2 = 0,2 mol -> m_H2 = 0,4 g. m tăng = m_Mg - m_H2 = 4,8 - 0,4 = 4,4 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về năng lượng nhiệt và phản ứng hóa học:", [
            ("a", "Phản ứng tôi vôi sống CaO với nước là phản ứng tỏa nhiệt dữ dội.", True),
            ("b", "Quá trình quang hợp của cây xanh hấp thụ năng lượng mặt trời là quá trình thu nhiệt.", True),
            ("c", "Khi đốt cháy than đá, năng lượng nhiệt giải phóng ra môi trường là phản ứng tỏa nhiệt.", True),
            ("d", "Phản ứng thu nhiệt làm nhiệt độ của môi trường xung quanh tăng vọt lên.", False)
        ], "Phản ứng thu nhiệt hấp thụ năng lượng làm môi trường xung quanh lạnh đi."),
        make_tf(2, "Thông hiểu", "Về khối lượng mol và thể tích mol chất khí:", [
            ("a", "1 mol khí CO2 và 1 mol khí O2 có cùng số lượng phân tử bằng 6,022 * 10^23.", True),
            ("b", "Ở đkc, 1 mol khí CO2 có thể tích lớn hơn 1 mol khí H2 vì phân tử CO2 to hơn.", False),
            ("c", "Tất cả các chất khí ở cùng điều kiện nhiệt độ và áp suất đều có cùng thể tích mol.", True),
            ("d", "Tỉ khối của chất khí giúp so sánh khí nào nặng hơn hay nhẹ hơn.", True)
        ], "Ở cùng nhiệt độ và áp suất, thể tích 1 mol mọi chất khí đều bằng nhau."),
        make_tf(3, "Vận dụng", "Cho phản ứng nhiệt phân muối KClO3 có xúc tác MnO2:", [
            ("a", "Phương trình: 2KClO3 -> 2KCl + 3O2.", True),
            ("b", "Khối lượng chất rắn sau phản ứng giảm đi đúng bằng khối lượng khí oxi bay ra.", True),
            ("c", "MnO2 bị tiêu hao hoàn toàn sau phản ứng.", False),
            ("d", "Khí oxi sinh ra có thể thu bằng phương pháp đẩy nước do ít tan trong nước.", True)
        ], "MnO2 là chất xúc tác nên giữ nguyên khối lượng."),
        make_tf(4, "Vận dụng cao", "Xét dung dịch muối ăn NaCl bão hòa ở 20 °C (độ tan S = 36 g):", [
            ("a", "Trong 100 g nước chỉ hòa tan tối đa 36 g muối ăn ở 20 °C.", True),
            ("b", "Khối lượng dung dịch bão hòa thu được là 136 g.", True),
            ("c", "Nồng độ phần trăm của dung dịch bão hòa là 26,47%.", True),
            ("d", "Nếu đun nóng dung dịch thì lượng muối ăn tan thêm được tăng lên rất lớn.", False)
        ], "Độ tan của NaCl trong nước hầu như thay đổi rất ít theo nhiệt độ.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Công thức hóa học của khí metan là gì? (Điền: CH4)", "CH4", "Khí metan là CH4."),
        make_sa(2, "Thông hiểu", "Thể tích của 0,4 mol khí CO2 ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Ghi số thập phân)", "9,916", "V = 0,4 * 24,79 = 9,916 L."),
        make_sa(3, "Thông hiểu", "Khối lượng của 0,5 mol canxi oxit CaO (M = 56 g/mol) là bao nhiêu gam?", "28", "m = 0,5 * 56 = 28 g."),
        make_sa(4, "Vận dụng", "Để pha 300 mL dung dịch NaOH 0,5 M cần bao nhiêu gam NaOH rắn?", "6", "n = 0,3 * 0,5 = 0,15 mol -> m = 0,15 * 40 = 6 g."),
        make_sa(5, "Vận dụng", "Đốt cháy 4,8 g kim loại Mg trong oxi thu được bao nhiêu gam MgO?", "8", "2Mg + O2 -> 2MgO. n_Mg = 0,2 mol -> n_MgO = 0,2 mol -> m = 0,2 * 40 = 8 g."),
        make_sa(6, "Vận dụng cao", "Tỉ khối của khí SO3 đối với khí O2 bằng bao nhiêu? (Ghi số thập phân)", "2,5", "80 / 32 = 2,5.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn 6,5 g kim loại Zn vào 100 mL dung dịch H2SO4 1,5 M. Sau khi phản ứng kết thúc, thể tích khí H2 thu được ở đkc (25 °C, 1 bar) là:", ["2,479 lít", "3,7185 lít", "4,958 lít", "1,2395 lít"], 0, "n_Zn = 0,1 mol; n_H2SO4 = 0,15 mol -> H2SO4 dư, tính theo Zn -> n_H2 = 0,1 mol -> V = 2,479 L."),
        make_vdc(2, "Khối lượng dung dịch HCl 14,6% cần dùng để hòa tan hoàn toàn 8,0 g đồng(II) oxit CuO là:", ["50 g", "100 g", "25 g", "75 g"], 0, "CuO + 2HCl -> CuCl2 + H2O. n_CuO = 0,1 mol -> n_HCl = 0,2 mol -> m_HCl = 7,3 g -> m_dd = 7,3 / 14,6% = 50 g."),
        make_vdc(3, "Một hỗn hợp gồm 0,2 mol CO và 0,3 mol CO2 có tỉ khối đối với không khí xấp xỉ bằng:", ["1,30", "1,15", "1,45", "1,05"], 0, "M_tb = (0,2*28 + 0,3*44) / 0,5 = (5,6 + 13,2) / 0,5 = 37,6 g/mol -> d = 37,6 / 29 xấp xỉ 1,30."),
        make_vdc(4, "Nhiệt phân hoàn toàn 15,8 g thuốc tím KMnO4 thu được V lít khí O2 ở đkc. Toàn bộ lượng khí O2 này đem đốt cháy m gam kim loại sắt thu được oxit sắt từ Fe3O4. Giá trị của m là:", ["4,2 g", "5,6 g", "8,4 g", "2,8 g"], 0, "2KMnO4 -> O2 (0,05 mol). 3Fe + 2O2 -> Fe3O4: n_Fe = 0,05 * 1,5 = 0,075 mol -> m_Fe = 0,075 * 56 = 4,2 g.")
    ]
}

# --- ĐỀ 3, 4, 5: Xây dựng bổ sung độc lập 100% ---
# Đề 3: Cân bằng phản ứng phức tạp, bài toán hỗn hợp khí
exams_c1_rev["chem8_c1_rev_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Chất xúc tác có đặc điểm là:", ["Làm tăng tốc độ phản ứng và không bị biến đổi sau phản ứng", "Bị tiêu hao trong quá trình phản ứng", "Làm thay đổi sản phẩm của phản ứng", "Làm ngừng phản ứng"], 0, "Chất xúc tác giữ nguyên về lượng và chất sau phản ứng."),
        make_mc(2, "Nhận biết", "Trong 1 phân tử khí sunfurơ (SO2) có bao nhiêu nguyên tử oxi?", ["2", "1", "3", "4"], 0, "SO2 có 2 nguyên tử oxi."),
        make_mc(3, "Nhận biết", "Ở điều kiện chuẩn (25 °C, 1 bar), 2 mol khí chiếm thể tích là:", ["49,58 lít", "24,79 lít", "44,8 lít", "22,4 lít"], 0, "2 * 24,79 = 49,58 L."),
        make_mc(4, "Nhận biết", "Đơn vị của nồng độ phần trăm là:", ["%", "mol/L", "g/mol", "gam"], 0, "Kí hiệu là %."),
        make_mc(5, "Thông hiểu", "Số phân tử khí có trong 0,5 mol khí N2 là:", ["3,011 * 10^23", "6,022 * 10^23", "1,204 * 10^24", "1,505 * 10^23"], 0, "0,5 * 6,022 * 10^23 = 3,011 * 10^23."),
        make_mc(6, "Thông hiểu", "Cho phương trình: 2Al + 6HCl -> 2AlCl3 + 3H2. Tỉ lệ giữa số phân tử HCl phản ứng và số phân tử H2 sinh ra là:", ["2 : 1", "6 : 3 = 2 : 1", "3 : 2", "1 : 1"], 0, "Tỉ lệ 6 : 3 = 2 : 1."),
        make_mc(7, "Thông hiểu", "Khí nào sau đây nhẹ nhất trong tất cả các chất khí?", ["H2 (hiđro)", "He (heli)", "CH4 (metan)", "N2 (nitơ)"], 0, "Khí hiđro H2 có phân tử khối bằng 2 nhẹ nhất."),
        make_mc(8, "Thông hiểu", "Khối lượng của 0,2 mol canxi cacbonat CaCO3 là:", ["20 g", "10 g", "40 g", "50 g"], 0, "m = 0,2 * 100 = 20 g."),
        make_mc(9, "Vận dụng", "Hòa tan 10 g đường vào 190 g nước. Nồng độ C% của dung dịch đường là:", ["5%", "10%", "5,26%", "4,5%"], 0, "m_dd = 200 g -> C% = 5%."),
        make_mc(10, "Vận dụng", "Cho các phản ứng: cháy cồn, gỉ sắt, nung vôi, thắp nến. Số phản ứng tỏa nhiệt là:", ["3", "2", "4", "1"], 0, "Cháy cồn, gỉ sắt, thắp nến tỏa nhiệt (3 phản ứng). Nung vôi thu nhiệt."),
        make_mc(11, "Vận dụng", "Thể tích dung dịch NaOH 2 M cần lấy để có 0,1 mol NaOH là:", ["50 mL", "100 mL", "200 mL", "25 mL"], 0, "V = 0,1 / 2 = 0,05 L = 50 mL."),
        make_mc(12, "Vận dụng cao", "Đốt cháy hoàn toàn 2,7 g kim loại nhôm trong khí clo dư thu được 13,35 g muối nhôm clorua (AlCl3). Khối lượng khí clo đã tham gia phản ứng là:", ["10,65 g", "16,05 g", "5,325 g", "7,1 g"], 0, "m_Cl2 = 13,35 - 2,7 = 10,65 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các hiện tượng hóa học xảy ra trong môi trường:", [
            ("a", "Hiện tượng mưa axit gây hại công trình kiến trúc là biến đổi hóa học.", True),
            ("b", "Băng phiến bốc hơi trong tủ quần áo là biến đổi hóa học.", False),
            ("c", "Sự thối rữa xác động thực vật là biến đổi hóa học sinh học phức tạp.", True),
            ("d", "Khí thải CO2 gây hiệu ứng nhà kính làm ấm Trái Đất.", True)
        ], "Băng phiến bốc hơi là hiện tượng thăng hoa vật lí."),
        make_tf(2, "Thông hiểu", "Về nồng độ dung dịch:", [
            ("a", "Pha thêm nước cất làm giảm nồng độ mol của dung dịch.", True),
            ("b", "Đun nóng để nước bay hơi làm tăng nồng độ phần trăm của dung dịch chưa bão hòa.", True),
            ("c", "Dung dịch bão hòa có thể tan thêm chất tan khi hạ nhiệt độ xuống cực thấp.", False),
            ("d", "Nước là dung môi phân cực hòa tan tốt nhiều hợp chất ion như muối ăn.", True)
        ], "Hạ nhiệt độ thường làm giảm độ tan, kết tinh thêm chất rắn."),
        make_tf(3, "Vận dụng", "Về phương trình phản ứng hóa học:", [
            ("a", "Hệ số cân bằng biểu diễn tỉ lệ số hạt giữa các chất.", True),
            ("b", "Cân bằng phương trình: 2Fe + 3Cl2 -> 2FeCl3.", True),
            ("c", "Tổng các hệ số của phản ứng: CH4 + 2O2 -> CO2 + 2H2O là 6.", True),
            ("d", "Phản ứng nhiệt phân đá vôi CaCO3 là phản ứng tỏa nhiệt.", False)
        ], "Nhiệt phân đá vôi là phản ứng thu nhiệt."),
        make_tf(4, "Vận dụng cao", "Cho hỗn hợp khí X gồm 0,2 mol N2 và 0,3 mol O2 ở đkc:", [
            ("a", "Tổng thể tích hỗn hợp khí X ở đkc là 12,395 lít.", True),
            ("b", "Khối lượng của hỗn hợp khí X là 15,2 g.", True),
            ("c", "Khối lượng mol trung bình của X là 30,4 g/mol.", True),
            ("d", "Hỗn hợp X nhẹ hơn không khí.", False)
        ], "M_tb = 30,4 > 29 nên nặng hơn không khí.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phản ứng: A + B -> C, chất C gọi là chất gì? (Điền: sản phẩm)", "sản phẩm", "Chất C là sản phẩm."),
        make_sa(2, "Thông hiểu", "Khối lượng mol của khí oxi O2 là bao nhiêu g/mol?", "32", "M = 32 g/mol."),
        make_sa(3, "Thông hiểu", "Số mol của 2,479 lít khí CO2 ở đkc là bao nhiêu mol? (Ghi số thập phân)", "0,1", "n = 0,1 mol."),
        make_sa(4, "Vận dụng", "Cần bao nhiêu gam đường để pha 100 g dung dịch nước đường 20%?", "20", "100 * 20% = 20 g."),
        make_sa(5, "Vận dụng", "Nung m gam CaCO3 thu được 11,2 g CaO và 8,8 g CO2. Khối lượng m ban đầu là bao nhiêu gam?", "20", "m = 11,2 + 8,8 = 20 g."),
        make_sa(6, "Vận dụng cao", "Tỉ khối của khí A đối với H2 là 16. Khí A là chất nào? (Điền: O2)", "O2", "M = 16 * 2 = 32 (O2).")
    ],
    "part4": [
        make_vdc(1, "Cho 5,6 g kim loại sắt tác dụng vừa đủ với V mL dung dịch HCl 2 M. Giá trị của V là:", ["100 mL", "200 mL", "50 mL", "150 mL"], 0, "n_Fe = 0,1 mol -> n_HCl = 0,2 mol -> V = 0,2 / 2 = 0,1 L = 100 mL."),
        make_vdc(2, "Đốt cháy hoàn toàn 4,8 g kim loại Mg trong khí clo dư thu được bao nhiêu gam muối MgCl2?", ["19,0 g", "9,5 g", "14,25 g", "28,5 g"], 0, "Mg + Cl2 -> MgCl2. n_Mg = 0,2 mol -> m_MgCl2 = 0,2 * 95 = 19,0 g."),
        make_vdc(3, "Khí X có tỉ khối đối với oxi bằng 1,375. Khí X là:", ["CO2", "SO2", "N2", "CH4"], 0, "M = 1,375 * 32 = 44 (CO2)."),
        make_vdc(4, "Một bình kín dung tích 7,437 lít chứa đầy khí N2 ở đkc. Khối lượng khí N2 có trong bình là:", ["8,4 g", "4,2 g", "14,0 g", "2,8 g"], 0, "n = 7,437 / 24,79 = 0,3 mol -> m = 0,3 * 28 = 8,4 g.")
    ]
}

# Đề 4: Chuyên sâu về tốc độ, năng lượng và cân bằng bảo toàn
exams_c1_rev["chem8_c1_rev_test4"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Yếu tố nào sau đây làm giảm tốc độ phản ứng?", ["Hạ nhiệt độ phản ứng", "Tăng nồng độ chất phản ứng", "Nghiền nhỏ chất phản ứng", "Thêm chất xúc tác"], 0, "Hạ nhiệt độ làm giảm tốc độ phản ứng."),
        make_mc(2, "Nhận biết", "Phương trình nào sau đây biểu diễn phản ứng tạo gỉ sắt?", ["Sắt + Oxi + Nước -> Gỉ sắt", "Sắt + Nước -> Khí hiđro", "Sắt + Muối -> Đồng", "Sắt nóng chảy thành lỏng"], 0, "Gỉ sắt hình thành do sắt tác dụng với oxi và nước ẩm."),
        make_mc(3, "Nhận biết", "Đơn vị đo của nồng độ mol là:", ["mol/L", "gam", "%", "g/mL"], 0, "mol/L hoặc M."),
        make_mc(4, "Nhận biết", "Trong phản ứng: CaCO3 -> CaO + CO2, chất phản ứng là:", ["CaCO3 (canxi cacbonat)", "CaO", "CO2", "Hỗn hợp CaO và CO2"], 0, "CaCO3 là chất phản ứng ban đầu."),
        make_mc(5, "Thông hiểu", "Thể tích của 0,3 mol khí hiđro ở điều kiện chuẩn (25 °C, 1 bar) là:", ["7,437 lít", "24,79 lít", "4,958 lít", "2,479 lít"], 0, "V = 0,3 * 24,79 = 7,437 L."),
        make_mc(6, "Thông hiểu", "Khối lượng mol của axit clohiđric HCl là:", ["36,5 g/mol", "35,5 g/mol", "18 g/mol", "98 g/mol"], 0, "M = 1 + 35,5 = 36,5 g/mol."),
        make_mc(7, "Thông hiểu", "Khí metan CH4 có tỉ khối đối với khí hiđro H2 là:", ["8", "16", "4", "2"], 0, "d = 16 / 2 = 8."),
        make_mc(8, "Thông hiểu", "Cân bằng phương trình: ... P + ... O2 -> ... P2O5. Hệ số của O2 là:", ["5", "2", "3", "4"], 0, "4P + 5O2 -> 2P2O5. Hệ số O2 là 5."),
        make_mc(9, "Vận dụng", "Hòa tan 4 g NaOH vào nước thu được 100 mL dung dịch. Nồng độ mol của dung dịch là:", ["1 M", "0,5 M", "2 M", "0,1 M"], 0, "n = 4 / 40 = 0,1 mol -> CM = 0,1 / 0,1 = 1 M."),
        make_mc(10, "Vận dụng", "Cho m gam kim loại kẽm tác dụng vừa đủ với 100 mL dung dịch HCl 1 M. Giá trị của m là:", ["3,25 g", "6,5 g", "1,3 g", "2,6 g"], 0, "n_HCl = 0,1 mol -> n_Zn = 0,05 mol -> m_Zn = 0,05 * 65 = 3,25 g."),
        make_mc(11, "Vận dụng", "Khi pha loãng 50 mL dung dịch H2SO4 2 M thành 200 mL dung dịch mới. Nồng độ mol của dung dịch sau khi pha là:", ["0,5 M", "1,0 M", "0,25 M", "0,2 M"], 0, "n = 0,05 * 2 = 0,1 mol -> CM = 0,1 / 0,2 = 0,5 M."),
        make_mc(12, "Vận dụng cao", "Nhiệt phân hoàn toàn 20 g đá vôi chứa 90% CaCO3, thu được m gam vôi sống CaO. Giá trị của m là:", ["10,08 g", "11,2 g", "9,0 g", "12,6 g"], 0, "m_CaCO3 = 18 g -> n = 0,18 mol -> m_CaO = 0,18 * 56 = 10,08 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các hiện tượng biến đổi vật chất:", [
            ("a", "Nến cháy sinh ra khí CO2 và hơi nước là biến đổi hóa học.", True),
            ("b", "Nến chảy lỏng thấm vào bấc là biến đổi vật lí.", True),
            ("c", "Đập vụn viên than thành bột là biến đổi hóa học.", False),
            ("d", "Bột than cháy trong không khí là biến đổi hóa học.", True)
        ], "Đập than chỉ thay đổi kích thước vật lí."),
        make_tf(2, "Thông hiểu", "Về mol và thể tích khí:", [
            ("a", "1 mol khí CO2 ở đkc nặng 44 g và chiếm thể tích 24,79 lít.", True),
            ("b", "Khí CO2 nặng hơn khí oxi.", True),
            ("c", "Khí CO2 nhẹ hơn không khí.", False),
            ("d", "Để thu khí CO2 ta đặt ngửa bình thu.", True)
        ], "M_CO2 = 44 > 29 nên nặng hơn không khí."),
        make_tf(3, "Vận dụng", "Về phản ứng hóa học trong dung dịch:", [
            ("a", "Cho bột kẽm vào axit clohiđric sủi bọt khí H2.", True),
            ("b", "Dung dịch thu được sau phản ứng chứa kẽm clorua ZnCl2.", True),
            ("c", "Khối lượng dung dịch sau phản ứng giảm đi do khí H2 bay ra.", False),
            ("d", "Khối lượng dung dịch tăng lên do m_Zn thêm vào lớn hơn m_H2 bay ra.", True)
        ], "Khối lượng dung dịch tăng: m_Zn (65g) - m_H2 (2g) > 0."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng nhiệt phân muối natri hidrocacbonat (baking soda):", [
            ("a", "Phương trình: 2NaHCO3 -> Na2CO3 + CO2 + H2O.", True),
            ("b", "Khí CO2 sinh ra làm đục nước vôi trong.", True),
            ("c", "Khối lượng chất rắn giảm đi đúng bằng tổng khối lượng CO2 và H2O.", True),
            ("d", "Đây là phản ứng tỏa nhiệt mạnh.", False)
        ], "Nhiệt phân cần cung cấp nhiệt liên tục (phản ứng thu nhiệt).")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Kí hiệu của hằng số Avogadro là chữ gì?", "N", "Kí hiệu là N."),
        make_sa(2, "Thông hiểu", "Khối lượng mol của khí nitơ N2 là bao nhiêu g/mol?", "28", "M = 28 g/mol."),
        make_sa(3, "Thông hiểu", "Thể tích của 0,5 mol khí oxi ở đkc là bao nhiêu lít? (Ghi số thập phân)", "12,395", "0,5 * 24,79 = 12,395 L."),
        make_sa(4, "Vận dụng", "Để pha 200 g dung dịch NaCl 5% cần bao nhiêu gam muối NaCl?", "10", "200 * 5% = 10 g."),
        make_sa(5, "Vận dụng", "Đốt cháy 0,1 mol bột lưu huỳnh trong oxi dư thu được bao nhiêu gam khí SO2? (Ghi số thập phân)", "6,4", "m = 0,1 * 64 = 6,4 g."),
        make_sa(6, "Vận dụng cao", "Cân bằng phương trình: a Fe + b O2 -> c Fe3O4. Tổng các hệ số (a + b + c) là bao nhiêu?", "6", "3Fe + 2O2 -> 1Fe3O4. Tổng: 3 + 2 + 1 = 6.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn 13 g kim loại Zn vào dung dịch HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "n_Zn = 0,2 mol -> n_H2 = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."),
        make_vdc(2, "Đốt cháy 1,6 g khí metan CH4 trong bình chứa 6,4 g khí O2. Khối lượng khí CO2 tạo thành là:", ["4,4 g", "2,2 g", "8,8 g", "3,6 g"], 0, "CH4 (0,1 mol) + 2O2 (0,2 mol) -> CO2 (0,1 mol). m_CO2 = 4,4 g."),
        make_vdc(3, "Hòa tan hoàn toàn 2,8 g Fe vào 100 mL dung dịch H2SO4 1 M. Sau phản ứng, khối lượng muối FeSO4 thu được là:", ["7,6 g", "15,2 g", "3,8 g", "11,4 g"], 0, "n_Fe = 0,05 mol -> m_FeSO4 = 0,05 * 152 = 7,6 g."),
        make_vdc(4, "Một hỗn hợp gồm 0,1 mol SO2 và 0,1 mol O2 có khối lượng mol trung bình là:", ["48 g/mol", "32 g/mol", "64 g/mol", "96 g/mol"], 0, "M_tb = (64 + 32) / 2 = 48 g/mol.")
    ]
}

# Đề 5: Đề phân hóa đỉnh cao, tổng hợp toàn diện Chương I
exams_c1_rev["chem8_c1_rev_test5"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Trong một phương trình hóa học, chỉ số dưới chân nguyên tử biểu thị:", ["Số nguyên tử của nguyên tố đó trong một phân tử", "Số phân tử của chất", "Khối lượng mol của chất", "Hóa trị của nguyên tố"], 0, "Chỉ số biểu thị số lượng nguyên tử trong một phân tử."),
        make_mc(2, "Nhận biết", "Hiện tượng thanh sắt gỉ ngoài không khí ẩm là phản ứng:", ["Tỏa nhiệt chậm", "Thu nhiệt nhanh", "Biến đổi vật lí", "Quang hợp"], 0, "Sự oxi hóa chậm tỏa nhiệt nhưng lượng nhiệt tản nhanh ra môi trường."),
        make_mc(3, "Nhận biết", "Khối lượng mol của axit sunfuric H2SO4 là:", ["98 g/mol", "49 g/mol", "36,5 g/mol", "64 g/mol"], 0, "M = 1*2 + 32 + 16*4 = 98 g/mol."),
        make_mc(4, "Nhận biết", "Khí nhẹ nhất trong các khí sau là:", ["H2 (M = 2)", "He (M = 4)", "CH4 (M = 16)", "N2 (M = 28)"], 0, "H2 nhẹ nhất."),
        make_mc(5, "Thông hiểu", "Thể tích của 0,25 mol khí CO2 ở điều kiện chuẩn (25 °C, 1 bar) là:", ["6,1975 lít", "24,79 lít", "12,395 lít", "4,958 lít"], 0, "V = 0,25 * 24,79 = 6,1975 L."),
        make_mc(6, "Thông hiểu", "Cho phương trình: 2K + 2H2O -> 2KOH + H2. Tỉ lệ số nguyên tử kali và số phân tử khí hiđro sinh ra là:", ["2 : 1", "1 : 1", "1 : 2", "2 : 2"], 0, "Hệ số K là 2, hệ số H2 là 1 -> 2 : 1."),
        make_mc(7, "Thông hiểu", "Hòa tan 20 g đường vào 180 g nước thu được dung dịch có nồng độ phần trăm là:", ["10%", "11,1%", "20%", "5%"], 0, "m_dd = 200 g -> C% = 20 / 200 = 10%."),
        make_mc(8, "Thông hiểu", "Nồng độ mol của 500 mL dung dịch chứa 0,5 mol HCl là:", ["1 M", "0,5 M", "2 M", "0,25 M"], 0, "CM = 0,5 / 0,5 = 1 M."),
        make_mc(9, "Vận dụng", "Đốt cháy 6,4 g bột đồng Cu trong khí oxi dư thu được m gam CuO màu đen. Giá trị của m là:", ["8,0 g", "7,2 g", "9,6 g", "8,8 g"], 0, "2Cu + O2 -> 2CuO. n_Cu = 0,1 mol -> m_CuO = 0,1 * 80 = 8,0 g."),
        make_mc(10, "Vận dụng", "Để làm sạch gỉ sét bám trên bề mặt đinh sắt, người ta ngâm đinh sắt vào dung dịch axit clohiđric loãng. Thao tác này là ứng dụng của:", ["Biến đổi hóa học hòa tan lớp gỉ oxit sắt", "Biến đổi vật lí mài mòn", "Phản ứng tôi vôi", "Hiện tượng ngưng tụ"], 0, "Axit tác dụng với oxit sắt gỉ tạo muối tan, làm sạch bề mặt."),
        make_mc(11, "Vận dụng", "Hòa tan 11,7 g muối ăn NaCl vào nước để được 200 mL dung dịch. Nồng độ mol của dung dịch NaCl là:", ["1 M", "0,5 M", "2 M", "0,1 M"], 0, "n = 11,7 / 58,5 = 0,2 mol -> CM = 0,2 / 0,2 = 1 M."),
        make_mc(12, "Vận dụng cao", "Dẫn 2,479 lít khí CO (đkc) qua ống sứ nung nóng chứa Fe2O3 dư. Sau phản ứng hoàn toàn, khối lượng sắt Fe thu được là:", ["3,73 g", "5,6 g", "11,2 g", "2,8 g"], 0, "n_CO = 0,1 mol. Fe2O3 + 3CO -> 2Fe + 3CO2. n_Fe = 0,1 * 2/3 mol -> m_Fe = 0,2/3 * 56 = 3,73 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các quá trình hóa học và vật lí:", [
            ("a", "Hòa tan đường vào nước là biến đổi vật lí.", True),
            ("b", "Nung đường thành than đen có mùi khét là biến đổi hóa học.", True),
            ("c", "Cồn etylic cháy tạo khí CO2 và H2O là biến đổi hóa học.", True),
            ("d", "Rượu để lâu bị bay hơi cồn làm giảm độ rượu là biến đổi hóa học.", False)
        ], "Bay hơi cồn là biến đổi vật lí trạng thái."),
        make_tf(2, "Thông hiểu", "Về các quy tắc bảo toàn khối lượng:", [
            ("a", "ĐL BTKL được xây dựng dựa trên sự bảo toàn số nguyên tử của từng nguyên tố.", True),
            ("b", "Khối lượng dung dịch sau phản ứng có kết tủa luôn nhỏ hơn tổng khối lượng các dung dịch ban đầu.", True),
            ("c", "Khối lượng dung dịch sau phản ứng có khí thoát ra luôn nhỏ hơn tổng khối lượng ban đầu.", True),
            ("d", "Trong phản ứng tạo gỉ sắt, khối lượng sắt bị mất đi hoàn toàn biến thành nhiệt.", False)
        ], "Sắt kết hợp với oxi và nước tạo thành gỉ sắt."),
        make_tf(3, "Vận dụng", "Về nồng độ phần trăm và nồng độ mol:", [
            ("a", "Dung dịch muối ăn 0,9% được gọi là nước muối sinh lí.", True),
            ("b", "Nồng độ mol biểu thị số mol chất tan trong một lít dung dịch.", True),
            ("c", "Để pha loãng dung dịch, ta thêm dung môi (nước cất).", True),
            ("d", "Khi pha loãng, cả số mol chất tan và nồng độ mol đều tăng lên.", False)
        ], "Số mol chất tan không đổi, nồng độ mol giảm."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng giữa kim loại magie và dung dịch axit sunfuric loãng:", [
            ("a", "Phương trình: Mg + H2SO4 -> MgSO4 + H2.", True),
            ("b", "Cho 2,4 g Mg vào 100 mL dung dịch H2SO4 1 M thì phản ứng vừa đủ.", True),
            ("c", "Thể tích khí H2 thu được ở đkc là 2,479 lít.", True),
            ("d", "Khối lượng muối MgSO4 thu được sau khi cô cạn dung dịch là 12,0 g.", True)
        ], "n = 0,1 mol -> m_MgSO4 = 0,1 * 120 = 12,0 g.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phản ứng hóa học, liên kết giữa các loại hạt nào bị thay đổi? (Điền: nguyên tử)", "nguyên tử", "Liên kết giữa các nguyên tử."),
        make_sa(2, "Thông hiểu", "Thể tích của 1 mol khí ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Ghi số thập phân)", "24,79", "24,79 lít."),
        make_sa(3, "Thông hiểu", "Khối lượng mol của khí cacbonic CO2 là bao nhiêu g/mol?", "44", "M = 44 g/mol."),
        make_sa(4, "Vận dụng", "Để có 0,2 mol NaCl cần bao nhiêu gam NaCl khan? (Ghi số thập phân)", "11,7", "0,2 * 58,5 = 11,7 g."),
        make_sa(5, "Vận dụng", "Cho 4,6 g kim loại Na tác dụng hết với nước. Số mol khí H2 sinh ra là bao nhiêu mol? (Ghi số thập phân)", "0,1", "n_Na = 0,2 mol -> n_H2 = 0,1 mol."),
        make_sa(6, "Vận dụng cao", "Cân bằng phương trình: a Al + b O2 -> c Al2O3. Tổng hệ số (a + b + c) là bao nhiêu?", "9", "4 + 3 + 2 = 9.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn 2,7 g kim loại nhôm vào dung dịch HCl dư. Thể tích khí H2 sinh ra ở đkc (25 °C, 1 bar) là:", ["3,7185 lít", "2,479 lít", "7,437 lít", "4,958 lít"], 0, "n_Al = 0,1 mol -> n_H2 = 0,15 mol -> V = 0,15 * 24,79 = 3,7185 L."),
        make_vdc(2, "Đốt cháy 3,2 g lưu huỳnh trong bình chứa 4,8 g khí oxi. Khối lượng khí SO2 tạo thành là:", ["6,4 g", "8,0 g", "3,2 g", "4,8 g"], 0, "S (0,1 mol) + O2 (0,15 mol) -> O2 dư, tính theo S -> m_SO2 = 0,1 * 64 = 6,4 g."),
        make_vdc(3, "Trộn 200 mL dung dịch HCl 1 M với 200 mL dung dịch NaOH 1 M. Dung dịch sau phản ứng có môi trường gì và chứa muối gì?", ["Môi trường trung tính, chứa muối NaCl", "Môi trường axit, chứa HCl dư", "Môi trường bazo, chứa NaOH dư", "Môi trường axit, chứa muối Na2SO4"], 0, "Phản ứng vừa đủ tạo NaCl và H2O, môi trường trung tính."),
        make_vdc(4, "Một hợp chất khí X có tỉ khối đối với hiđro là 17. Đốt cháy X sinh ra khí nitơ và hơi nước. Khí X là:", ["H2S (M = 34)", "NH3 (M = 17)", "PH3 (M = 34)", "CH4 (M = 16)"], 0, "M = 17 * 2 = 34 (H2S; phản ứng đốt cháy H2S tạo SO2 + H2O hoặc S + H2O).")
    ]
}

print("Đã nạp xong Ôn tập cuối Chương I (5 đề độc lập 100%)")
