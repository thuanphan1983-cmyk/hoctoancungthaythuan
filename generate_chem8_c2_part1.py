# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - CHƯƠNG II: BÀI 8 (ACID) VÀ BÀI 9 (BASE - THANG pH) (6 ĐỀ ĐỘC LẬP 100%)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

exams_c2 = {}

# ==============================================================================
# BÀI 8: ACID (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Định nghĩa axit, công thức hóa học, làm đổi màu chỉ thị ---
exams_c2["chem8_c2_b8_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Axit là hợp chất mà phân tử gồm có:", ["Một hay nhiều nguyên tử hiđro liên kết với gốc axit", "Một nguyên tử kim loại liên kết với một hay nhiều nhóm hiđroxit (-OH)", "Một nguyên tố kim loại liên kết với một nguyên tố phi kim", "Nguyên tử kim loại liên kết với gốc axit"], 0, "Axit gồm một hay nhiều nguyên tử H liên kết với gốc axit."),
        make_mc(2, "Nhận biết", "Chất nào sau đây là axit?", ["HCl (axit clohiđric)", "NaOH (natri hiđroxit)", "NaCl (natri clorua)", "CaO (canxi oxit)"], 0, "HCl là một axit mạnh phổ biến."),
        make_mc(3, "Nhận biết", "Dung dịch axit làm giấy quỳ tím chuyển sang màu gì?", ["Màu đỏ", "Màu xanh", "Màu hồng", "Màu vàng"], 0, "Dung dịch axit làm quỳ tím chuyển sang màu đỏ."),
        make_mc(4, "Nhận biết", "Gốc axit trong phân tử axit sunfuric H2SO4 là:", ["=SO4 (sunfat)", "-Cl (clorua)", "=CO3 (cacbonat)", "-NO3 (nitrat)"], 0, "Gốc sunfat là =SO4 có hóa trị II."),
        make_mc(5, "Thông hiểu", "Cho dãy các chất: HCl, NaOH, H2SO4, Cu(OH)2, HNO3, K2SO4. Có bao nhiêu axit trong dãy?", ["3", "2", "4", "5"], 0, "Có 3 axit: HCl, H2SO4, HNO3."),
        make_mc(6, "Thông hiểu", "Kim loại nào sau đây KHÔNG tác dụng với dung dịch axit HCl loãng giải phóng khí hiđro?", ["Cu (đồng)", "Fe (sắt)", "Zn (kẽm)", "Mg (magie)"], 0, "Đồng (Cu) đứng sau hiđro trong dãy hoạt động hóa học nên không tác dụng với HCl loãng."),
        make_mc(7, "Thông hiểu", "Khi cho kim loại kẽm vào dung dịch axit clohiđric HCl, khí sinh ra là:", ["H2 (hiđro)", "O2 (oxi)", "Cl2 (clo)", "CO2 (cacbonic)"], 0, "Zn + 2HCl -> ZnCl2 + H2."),
        make_mc(8, "Thông hiểu", "Phương trình phản ứng nào sau đây viết ĐÚNG giữa sắt và axit clohiđric?", ["Fe + 2HCl -> FeCl2 + H2", "2Fe + 6HCl -> 2FeCl3 + 3H2", "Fe + HCl -> FeCl + H", "Fe + 2HCl -> FeCl2 + H2O"], 0, "Sắt tác dụng với HCl chỉ tạo muối sắt(II) FeCl2 và H2."),
        make_mc(9, "Vận dụng", "Trong dạ dày người có một lượng nhỏ axit nào giúp tiêu hóa thức ăn và tiêu diệt vi khuẩn?", ["Axit clohiđric (HCl)", "Axit sunfuric (H2SO4)", "Axit axetic (CH3COOH)", "Axit nitric (HNO3)"], 0, "Dịch vị dạ dày chứa axit HCl nồng độ khoảng 0,0001 - 0,001 M (pH khoảng 1,5 - 3,5)."),
        make_mc(10, "Vận dụng", "Để pha loãng axit sunfuric đặc (H2SO4 đặc) an toàn trong phòng thí nghiệm, thao tác ĐÚNG là:", ["Rót từ từ axit dọc theo đũa thủy tinh vào nước và khuấy đều", "Rót nhanh nước vào axit đặc", "Đổ đồng thời cả axit và nước vào cốc", "Đun nóng axit rồi mới đổ nước vào"], 0, "Quy tắc an toàn: Rót từ từ axit vào nước, tuyệt đối không làm ngược lại vì sẽ gây bắn axit nguy hiểm."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 6,5 g kim loại Zn vào dung dịch HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:", ["2,479 lít", "4,958 lít", "2,24 lít", "1,2395 lít"], 0, "n_Zn = 0,1 mol -> n_H2 = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."),
        make_mc(12, "Vận dụng cao", "Cho m gam hỗn hợp gồm bột sắt và đồng tác dụng với lượng dư dung dịch HCl thu được 4,958 lít khí H2 ở đkc và 3,2 g chất rắn không tan. Giá trị của m là:", ["14,4 g", "11,2 g", "8,8 g", "12,6 g"], 0, "n_H2 = 0,2 mol -> n_Fe = 0,2 mol -> m_Fe = 0,2 * 56 = 11,2 g. m_Cu = 3,2 g -> m = 11,2 + 3,2 = 14,4 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về tính chất chung của dung dịch axit:", [
            ("a", "Dung dịch axit làm quỳ tím hóa đỏ.", True),
            ("b", "Axit tác dụng với kim loại đứng trước H trong dãy hoạt động giải phóng khí H2.", True),
            ("c", "Tất cả các kim loại đều tan trong axit HCl loãng.", False),
            ("d", "Axit tác dụng với bazơ tạo thành muối và nước (phản ứng trung hòa).", True)
        ], "Các kim loại như Cu, Ag, Au đứng sau H không tan trong HCl loãng."),
        make_tf(2, "Thông hiểu", "Về các axit phổ biến trong đời sống và sản xuất:", [
            ("a", "Axit sunfuric H2SO4 là hóa chất hàng đầu được mệnh danh là 'máu của ngành công nghiệp hóa chất'.", True),
            ("b", "Giấm ăn dùng trong gia đình là dung dịch axit axetic (CH3COOH) nồng độ khoảng 2% - 5%.", True),
            ("c", "Axit H2SO4 đặc có tính háo nước mạnh và có thể gây bỏng sâu rất nguy hiểm.", True),
            ("d", "Khi bị axit dính vào da, cần trung hòa ngay bằng dung dịch kiềm đặc NaOH.", False)
        ], "Phải rửa ngay dưới vòi nước chảy liên tục trong nhiều phút, không dùng kiềm đặc."),
        make_tf(3, "Vận dụng", "Cho các phản ứng sau ở nhiệt độ thường:", [
            ("a", "Mg + 2HCl -> MgCl2 + H2.", True),
            ("b", "Fe + H2SO4 loãng -> FeSO4 + H2.", True),
            ("c", "Cu + 2HCl -> CuCl2 + H2.", False),
            ("d", "2Al + 6HCl -> 2AlCl3 + 3H2.", True)
        ], "Đồng không tác dụng với dung dịch HCl loãng."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm cho một lá nhôm (Al) vào dung dịch axit clohiđric loãng:", [
            ("a", "Ban đầu chưa thấy sủi bọt khí ngay do bề mặt nhôm có lớp màng Al2O3 bảo vệ.", True),
            ("b", "Sau khi lớp oxit tan hết, bọt khí H2 thoát ra nhanh và mạnh làm dung dịch nóng lên.", True),
            ("c", "Dung dịch sau phản ứng chứa muối nhôm clorua AlCl3.", True),
            ("d", "Khối lượng dung dịch sau phản ứng tăng đúng bằng khối lượng lá nhôm đã phản ứng.", False)
        ], "Khối lượng tăng bằng m_Al trừ đi m_H2 bay ra.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phân tử axit nitric HNO3, gốc axit có hóa trị mấy?", "I", "Gốc -NO3 có hóa trị I."),
        make_sa(2, "Thông hiểu", "Dung dịch axit clohiđric làm quỳ tím chuyển sang màu gì?", "đỏ", "Chuyển sang màu đỏ."),
        make_sa(3, "Thông hiểu", "Cho các kim loại: Mg, Fe, Cu, Ag, Al. Có bao nhiêu kim loại tác dụng được với dung dịch axit HCl loãng giải phóng H2?", "3", "Mg, Fe, Al (3 kim loại đứng trước H)."),
        make_sa(4, "Vận dụng", "Hòa tan hết 2,4 g kim loại magie vào dung dịch HCl dư. Thể tích khí H2 thoát ra ở đkc là bao nhiêu lít? (Ghi số thập phân)", "2,479", "n_Mg = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."),
        make_sa(5, "Vận dụng", "Khối lượng mol của axit sunfuric H2SO4 là bao nhiêu g/mol?", "98", "M = 98 g/mol."),
        make_sa(6, "Vận dụng cao", "Cho 0,2 mol bột sắt Fe phản ứng hoàn toàn với dung dịch HCl dư. Khối lượng muối FeCl2 thu được là bao nhiêu gam? (Ghi số thập phân)", "25,4", "m = 0,2 * 127 = 25,4 g.")
    ],
    "part4": [
        make_vdc(1, "Cho 10 g hỗn hợp gồm Mg và Cu vào dung dịch HCl dư. Sau phản ứng thu được 4,958 lít khí H2 ở đkc. Phần trăm khối lượng của kim loại đồng trong hỗn hợp là:", ["52%", "48%", "24%", "36%"], 0, "n_H2 = 0,2 mol -> n_Mg = 0,2 mol -> m_Mg = 4,8 g -> m_Cu = 10 - 4,8 = 5,2 g -> %Cu = 52%."),
        make_vdc(2, "Để hòa tan hoàn toàn 4,0 g oxit sắt Fe2O3 cần vừa đủ bao nhiêu mL dung dịch axit HCl 1 M?", ["150 mL", "200 mL", "100 mL", "300 mL"], 0, "Fe2O3 + 6HCl -> 2FeCl3 + 3H2O. n_Fe2O3 = 4 / 160 = 0,025 mol -> n_HCl = 0,15 mol -> V = 0,15 L = 150 mL."),
        make_vdc(3, "Một mẫu axit H2SO4 loãng có nồng độ 10%. Cần lấy bao nhiêu gam dung dịch này để hòa tan hoàn toàn 2,4 g bột magie Mg?", ["98 g", "49 g", "196 g", "120 g"], 0, "n_Mg = 0,1 mol -> n_H2SO4 = 0,1 mol -> m_H2SO4 = 9,8 g -> m_dd = 9,8 / 10% = 98 g."),
        make_vdc(4, "Kim loại nào sau đây khi tác dụng với axit sunfuric loãng giải phóng khí H2 tạo ra dung dịch muối có màu xanh lam nhạt?", ["Sắt (Fe) tạo FeSO4 xanh nhạt", "Đồng (Cu)", "Kẽm (Zn)", "Nhôm (Al)"], 0, "Fe + H2SO4 loãng -> FeSO4 (dung dịch màu xanh lục/lam nhạt) + H2.")
    ]
}

# --- ĐỀ 2, 3: Phản ứng hóa học của axit, an toàn phòng thí nghiệm ---
exams_c2["chem8_c2_b8_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Axit nào sau đây là axit có oxi trong phân tử?", ["H2SO4 (axit sunfuric)", "HCl (axit clohiđric)", "H2S (axit sunfuhidric)", "HBr (axit bromhiđric)"], 0, "H2SO4 chứa nguyên tố oxi."),
        make_mc(2, "Nhận biết", "Tên gọi của axit HCl là:", ["Axit clohiđric", "Axit sunfuric", "Axit nitric", "Axit cacbonic"], 0, "HCl là axit clohiđric."),
        make_mc(3, "Nhận biết", "Khi nhỏ dung dịch axit vào mẩu giấy quỳ tím, hiện tượng xảy ra là:", ["Giấy quỳ đổi sang màu đỏ", "Giấy quỳ đổi sang màu xanh", "Giấy quỳ mất màu", "Giấy quỳ không đổi màu"], 0, "Quỳ tím chuyển sang màu đỏ."),
        make_mc(4, "Nhận biết", "Kim loại nào sau đây tác dụng được với axit clohiđric HCl sinh ra khí hiđro?", ["Kẽm (Zn)", "Bạc (Ag)", "Vàng (Au)", "Bạch kim (Pt)"], 0, "Zn đứng trước H nên tác dụng sinh H2."),
        make_mc(5, "Thông hiểu", "Sản phẩm của phản ứng giữa axit và bazơ luôn gồm có:", ["Muối và nước", "Kim loại và khí hiđro", "Oxit axit và muối", "Oxit bazơ và nước"], 0, "Phản ứng trung hòa: Axit + Bazơ -> Muối + Nước."),
        make_mc(6, "Thông hiểu", "Cho mẩu đá vôi (CaCO3) vào dung dịch axit HCl, hiện tượng quan sát được là:", ["Đá vôi tan dần và có bọt khí thoát ra", "Xuất hiện kết tủa màu đen", "Có khí mùi khai bay lên", "Dung dịch đông cứng lại"], 0, "CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (sủi bọt khí)."),
        make_mc(7, "Thông hiểu", "Phương trình phản ứng giữa bột nhôm và axit sunfuric loãng là:", ["2Al + 3H2SO4 -> Al2(SO4)3 + 3H2", "Al + H2SO4 -> AlSO4 + H2", "2Al + H2SO4 -> Al2SO4 + H2", "Al + 3H2SO4 -> Al(SO4)3 + 3H2"], 0, "Nhôm có hóa trị III, gốc sunfat hóa trị II -> Al2(SO4)3."),
        make_mc(8, "Thông hiểu", "Khi bị ong hoặc kiến đốt (nọc có chứa axit fomic HCOOH), người ta thường bôi vôi tôi hoặc kem đánh răng (chứa chất kiềm nhẹ) vào vết đốt để:", ["Trung hòa axit làm giảm ngứa và sưng đau", "Làm vết thương nóng lên", "Tiêu diệt vi rút", "Làm đông cứng nọc độc"], 0, "Chất kiềm trung hòa axit của nọc ong, kiến."),
        make_mc(9, "Vận dụng", "Hòa tan 5,6 g kim loại sắt trong dung dịch axit HCl dư. Khối lượng muối FeCl2 thu được là:", ["12,7 g", "16,25 g", "25,4 g", "6,35 g"], 0, "n_Fe = 0,1 mol -> m_FeCl2 = 0,1 * 127 = 12,7 g."),
        make_mc(10, "Vận dụng", "Axit clohiđric phản ứng được với tất cả các chất trong dãy nào sau đây?", ["Fe, NaOH, CuO, CaCO3", "Cu, KOH, BaCl2, Ag", "Au, Al, Na2SO4, CO2", "Ag, Fe2O3, H2SO4, NaCl"], 0, "HCl tác dụng với kim loại đứng trước H (Fe), bazơ (NaOH), oxit bazơ (CuO), muối cacbonat (CaCO3)."),
        make_mc(11, "Vận dụng", "Thể tích khí H2 sinh ra ở đkc (25 °C, 1 bar) khi cho 0,2 mol Al tác dụng hết với dung dịch HCl dư là:", ["7,437 lít", "4,958 lít", "2,479 lít", "6,72 lít"], 0, "n_H2 = 0,2 * 1,5 = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."),
        make_mc(12, "Vận dụng cao", "Để hòa tan hoàn toàn 8 g oxit kim loại RO (hóa trị II) cần vừa đủ 100 mL dung dịch HCl 2 M. Kim loại R là:", ["Đồng (Cu = 64)", "Kẽm (Zn = 65)", "Magiê (Mg = 24)", "Canxi (Ca = 40)"], 0, "RO + 2HCl -> RCl2 + H2O. n_HCl = 0,2 mol -> n_RO = 0,1 mol -> M_RO = 8 / 0,1 = 80 -> M_R = 80 - 16 = 64 (Cu)."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phân loại axit theo thành phần nguyên tố:", [
            ("a", "Axit không có oxi: HCl, H2S, HBr, HF.", True),
            ("b", "Axit có oxi: H2SO4, HNO3, H3PO4, H2CO3.", True),
            ("c", "Tất cả các axit đều là chất lỏng ở điều kiện thường.", False),
            ("d", "Axit photphoric H3PO4 là chất rắn tinh thể ở nhiệt độ phòng.", True)
        ], "H3PO4 ở dạng tinh thể rắn không màu ở nhiệt độ phòng."),
        make_tf(2, "Thông hiểu", "Về tính chất hóa học của axit với oxit kim loại:", [
            ("a", "Axit tác dụng với oxit bazơ tạo thành muối và nước.", True),
            ("b", "Cho bột CuO màu đen vào dung dịch HCl nóng, bột đen tan dần tạo dung dịch có màu xanh lam.", True),
            ("c", "Cho bột Fe2O3 màu nâu đỏ vào dung dịch HCl tạo dung dịch có màu vàng nâu của FeCl3.", True),
            ("d", "Phản ứng giữa oxit kim loại và axit giải phóng khí hiđro thoát ra.", False)
        ], "Oxit bazơ + axit -> muối + nước (không sinh H2)."),
        make_tf(3, "Vận dụng", "Cho các mẩu kim loại: Fe, Cu, Al, Zn vào 4 ống nghiệm đựng axit H2SO4 loãng:", [
            ("a", "Ống nghiệm chứa Fe sủi bọt khí và dung dịch có màu xanh nhạt.", True),
            ("b", "Ống nghiệm chứa Cu không có hiện tượng gì xảy ra.", True),
            ("c", "Ống nghiệm chứa Al và Zn đều sủi bọt khí nhanh và dung dịch không màu.", True),
            ("d", "Khí thoát ra ở các ống nghiệm là khí oxi duy trì sự cháy.", False)
        ], "Khí thoát ra là khí hiđro H2."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm hòa tan mẩu đá vôi CaCO3 vào dung dịch axit clohiđric:", [
            ("a", "Phương trình: CaCO3 + 2HCl -> CaCl2 + H2O + CO2.", True),
            ("b", "Khí CO2 thoát ra làm đục dung dịch nước vôi trong.", True),
            ("c", "Khối lượng của cốc đựng dung dịch sau phản ứng giảm đi đúng bằng khối lượng CO2 bay ra.", True),
            ("d", "Phản ứng trên thuộc loại phản ứng oxi hóa - khử.", False)
        ], "Đây là phản ứng trao đổi, không có sự thay đổi số oxi hóa.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Công thức hóa học của axit sunfuric là gì? (Điền: H2SO4)", "H2SO4", "Axit sunfuric là H2SO4."),
        make_sa(2, "Thông hiểu", "Cho các chất: HCl, KOH, H2SO4, Na2SO4, HNO3. Có bao nhiêu axit trong dãy?", "3", "Gồm HCl, H2SO4, HNO3 (3 axit)."),
        make_sa(3, "Thông hiểu", "Kim loại đồng Cu có tác dụng với axit clohiđric loãng không? (Điền: có hoặc không)", "không", "Đồng đứng sau H nên không tác dụng."),
        make_sa(4, "Vận dụng", "Hòa tan 0,1 mol kim loại kẽm vào dung dịch HCl dư. Thể tích khí H2 thu được ở đkc là bao nhiêu lít? (Ghi số thập phân)", "2,479", "V = 0,1 * 24,79 = 2,479 L."),
        make_sa(5, "Vận dụng", "Khối lượng mol của axit nitric HNO3 là bao nhiêu g/mol?", "63", "M = 1 + 14 + 16*3 = 63 g/mol."),
        make_sa(6, "Vận dụng cao", "Cho 10 g CaCO3 tác dụng hết với axit HCl. Thể tích khí CO2 thoát ra ở đkc là bao nhiêu lít? (Ghi số thập phân)", "2,479", "n = 0,1 mol -> V = 2,479 L.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn 10,8 g kim loại Al vào dung dịch axit HCl dư. Sau phản ứng, khối lượng muối nhôm clorua AlCl3 thu được là:", ["53,4 g", "26,7 g", "80,1 g", "40,05 g"], 0, "n_Al = 0,4 mol -> n_AlCl3 = 0,4 mol -> m = 0,4 * 133,5 = 53,4 g."),
        make_vdc(2, "Cho 16 g bột đồng(II) oxit CuO tác dụng vừa đủ với m gam dung dịch H2SO4 20%. Giá trị của m là:", ["98 g", "49 g", "196 g", "120 g"], 0, "n_CuO = 0,2 mol -> n_H2SO4 = 0,2 mol -> m_H2SO4 = 19,6 g -> m_dd = 19,6 / 20% = 98 g."),
        make_vdc(3, "Kim loại nào sau đây khi hòa tan vào dung dịch axit clohiđric loãng cho cùng một lượng mol khí H2 với khối lượng kim loại tiêu tốn là ít nhất?", ["Magiê (Mg = 24)", "Sắt (Fe = 56)", "Kẽm (Zn = 65)", "Canxi (Ca = 40)"], 0, "1 mol H2 cần 1 mol kim loại hóa trị II: m_Mg = 24g là nhỏ nhất."),
        make_vdc(4, "Một dung dịch chứa 0,1 mol HCl và 0,1 mol H2SO4. Để trung hòa hoàn toàn dung dịch này cần bao nhiêu mol NaOH?", ["0,3 mol", "0,2 mol", "0,1 mol", "0,4 mol"], 0, "Tổng mol H+ = 0,1 + 0,1 * 2 = 0,3 mol -> n_NaOH = 0,3 mol.")
    ]
}

# Đề 3: Ứng dụng công nghiệp, nhận biết và tính toán chuyên sâu
exams_c2["chem8_c2_b8_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Gốc axit của axit clohiđric HCl là:", ["-Cl (clorua)", "=SO4 (sunfat)", "-NO3 (nitrat)", "=CO3 (cacbonat)"], 0, "Gốc clorua -Cl có hóa trị I."),
        make_mc(2, "Nhận biết", "Chất nào sau đây KHÔNG PHẢI là axit?", ["NaCl", "H2SO4", "HCl", "HNO3"], 0, "NaCl là muối ăn, không phải axit."),
        make_mc(3, "Nhận biết", "Dung dịch axit nào sau đây có trong ắc quy xe máy, ô tô?", ["Axit sunfuric (H2SO4)", "Axit clohiđric (HCl)", "Axit axetic (CH3COOH)", "Axit nitric (HNO3)"], 0, "Ắc quy chì sử dụng dung dịch axit sunfuric loãng làm chất điện li."),
        make_mc(4, "Nhận biết", "Kim loại nào sau đây đứng trước hiđro trong dãy hoạt động hóa học?", ["Mg (magie)", "Cu (đồng)", "Ag (bạc)", "Au (vàng)"], 0, "Mg đứng trước H."),
        make_mc(5, "Thông hiểu", "Cho các dung dịch: HCl, NaCl, NaOH, nước cất. Dung dịch làm quỳ tím chuyển sang màu đỏ là:", ["HCl", "NaOH", "NaCl", "Nước cất"], 0, "Dung dịch axit HCl làm quỳ tím hóa đỏ."),
        make_mc(6, "Thông hiểu", "Phản ứng giữa dung dịch axit clohiđric và đồng(II) hiđroxit Cu(OH)2 tạo ra dung dịch có màu:", ["Màu xanh lam", "Màu đỏ nâu", "Không màu", "Màu vàng đậm"], 0, "Cu(OH)2 + 2HCl -> CuCl2 (màu xanh lam) + 2H2O."),
        make_mc(7, "Thông hiểu", "Khí nào sau đây thoát ra khi cho mẩu đá vôi vào dung dịch axit sunfuric loãng?", ["Khí cacbon đioxit (CO2)", "Khí hiđro (H2)", "Khí oxi (O2)", "Khí sunfurơ (SO2)"], 0, "CaCO3 + H2SO4 -> CaSO4 + H2O + CO2."),
        make_mc(8, "Thông hiểu", "Để nhận biết lọ đựng dung dịch axit clohiđric HCl và lọ đựng dung dịch muối ăn NaCl, ta có thể dùng:", ["Mẩu giấy quỳ tím", "Nước cất", "Dung dịch đường", "Cân khối lượng"], 0, "Quỳ tím hóa đỏ với HCl, không đổi màu với NaCl."),
        make_mc(9, "Vận dụng", "Một thanh sắt nặng 11,2 g cho vào dung dịch axit sunfuric loãng dư. Sau khi phản ứng hoàn toàn, thể tích khí H2 thu được ở đkc (25 °C, 1 bar) là:", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "n_Fe = 0,2 mol -> n_H2 = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."),
        make_mc(10, "Vận dụng", "Hòa tan hoàn toàn 2,4 g bột magie trong dung dịch H2SO4 loãng vừa đủ. Khối lượng muối magie sunfat MgSO4 thu được sau phản ứng là:", ["12,0 g", "6,0 g", "24,0 g", "8,0 g"], 0, "n_Mg = 0,1 mol -> m_MgSO4 = 0,1 * 120 = 12,0 g."),
        make_mc(11, "Vận dụng", "Cần lấy bao nhiêu mL dung dịch HCl 1 M để trung hòa hoàn toàn 200 mL dung dịch Ba(OH)2 0,5 M?", ["200 mL", "100 mL", "400 mL", "300 mL"], 0, "Ba(OH)2 + 2HCl -> BaCl2 + 2H2O. n_Ba(OH)2 = 0,1 mol -> n_HCl = 0,2 mol -> V = 0,2 / 1 = 0,2 L = 200 mL."),
        make_mc(12, "Vận dụng cao", "Hòa tan hoàn toàn 13 g kim loại kẽm vào dung dịch chứa 0,3 mol axit HCl. Sau phản ứng chất nào còn dư và dư bao nhiêu?", ["Zn dư 0,05 mol", "HCl dư 0,1 mol", "Hai chất vừa đủ", "Zn dư 0,1 mol"], 0, "Zn + 2HCl -> ZnCl2 + H2. n_Zn = 0,2 mol; n_HCl = 0,3 mol -> n_Zn phản ứng = 0,15 mol -> Zn dư = 0,2 - 0,15 = 0,05 mol."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất hóa học đặc trưng của axit:", [
            ("a", "Tác dụng với kim loại đứng trước H tạo muối và giải phóng khí H2.", True),
            ("b", "Tác dụng với bazơ tạo thành muối và nước (phản ứng trung hòa).", True),
            ("c", "Tác dụng với oxit bazơ tạo thành muối và nước.", True),
            ("d", "Tác dụng với mọi loại muối luôn giải phóng khí clo.", False)
        ], "Chỉ phản ứng với một số muối thỏa mãn điều kiện tạo kết tủa hoặc khí."),
        make_tf(2, "Thông hiểu", "Về ứng dụng của axit trong công nghiệp và đời sống:", [
            ("a", "Axit clohiđric dùng để tẩy rỉ sét kim loại trước khi hàn hoặc mạ.", True),
            ("b", "Axit sunfuric dùng để sản xuất phân bón hóa học (supephotphat, amoni sunfat).", True),
            ("c", "Axit nitric HNO3 dùng để sản xuất thuốc nổ và phân đạm.", True),
            ("d", "Axit sunfuric đặc có thể dùng để làm khô mọi chất khí kể cả khí kiềm amoniac NH3.", False)
        ], "H2SO4 đặc phản ứng với NH3 nên không dùng để làm khô NH3."),
        make_tf(3, "Vận dụng", "Cho các phản ứng trung hòa sau:", [
            ("a", "HCl + NaOH -> NaCl + H2O.", True),
            ("b", "H2SO4 + 2KOH -> K2SO4 + 2H2O.", True),
            ("c", "2HCl + Cu(OH)2 -> CuCl2 + 2H2O.", True),
            ("d", "HCl + NaCl -> NaOH + Cl2.", False)
        ], "Axit không phản ứng với muối của chính nó."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm ngâm vỏ trứng (chứa canxi cacbonat CaCO3) vào cốc đựng giấm ăn (axit axetic):", [
            ("a", "Trên bề mặt vỏ trứng xuất hiện nhiều bọt khí nhỏ bám quanh.", True),
            ("b", "Sau vài ngày ngâm, lớp vỏ cứng bị tan hết chỉ còn lại màng dai bên trong quả trứng.", True),
            ("c", "Bọt khí thoát ra trong thí nghiệm này là khí oxi.", False),
            ("d", "Thí nghiệm này chứng minh giấm ăn có tính axit phản ứng hòa tan muối cacbonat.", True)
        ], "Khí sinh ra là khí cacbon đioxit CO2.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong công thức hóa học của axit, nguyên tố nào luôn luôn có mặt ở đầu công thức? (Điền kí hiệu: H)", "H", "Nguyên tố hiđro (H)."),
        make_sa(2, "Thông hiểu", "Cho các kim loại: Al, Cu, Zn, Fe, Ag. Có bao nhiêu kim loại KHÔNG tan trong axit HCl loãng?", "2", "Gồm Cu và Ag (2 kim loại)."),
        make_sa(3, "Thông hiểu", "Dung dịch giấm ăn làm quỳ tím đổi thành màu gì?", "đỏ", "Giấm ăn có tính axit làm quỳ tím hóa đỏ."),
        make_sa(4, "Vận dụng", "Hòa tan hết 4 g bột MgO vào dung dịch HCl dư. Khối lượng muối MgCl2 thu được là bao nhiêu gam? (Ghi số thập phân)", "9,5", "n_MgO = 0,1 mol -> m_MgCl2 = 0,1 * 95 = 9,5 g."),
        make_sa(5, "Vận dụng", "Số mol khí H2 sinh ra khi cho 0,3 mol kẽm Zn tác dụng hoàn toàn với axit sunfuric loãng dư là bao nhiêu mol? (Ghi số thập phân)", "0,3", "n_H2 = n_Zn = 0,3 mol."),
        make_sa(6, "Vận dụng cao", "Để hòa tan hết 5,6 g kim loại sắt cần bao nhiêu gam axit HCl nguyên chất? (Ghi số thập phân)", "7,3", "n_Fe = 0,1 mol -> n_HCl = 0,2 mol -> m = 0,2 * 36,5 = 7,3 g.")
    ],
    "part4": [
        make_vdc(1, "Cho 12 g hỗn hợp gồm Fe và Cu tác dụng với lượng dư dung dịch HCl, sau phản ứng thu được 2,479 lít khí H2 ở đkc. Khối lượng kim loại Cu trong hỗn hợp là:", ["6,4 g", "5,6 g", "3,2 g", "4,8 g"], 0, "n_H2 = 0,1 mol -> n_Fe = 0,1 mol -> m_Fe = 5,6 g -> m_Cu = 12 - 5,6 = 6,4 g."),
        make_vdc(2, "Trung hòa hoàn toàn 100 mL dung dịch H2SO4 1 M bằng dung dịch NaOH 1 M. Thể tích dung dịch NaOH cần dùng là:", ["200 mL", "100 mL", "50 mL", "150 mL"], 0, "H2SO4 + 2NaOH -> Na2SO4 + 2H2O. n_H2SO4 = 0,1 mol -> n_NaOH = 0,2 mol -> V = 0,2 L = 200 mL."),
        make_vdc(3, "Hòa tan hoàn toàn 1,6 g bột oxit đồng CuO vào 100 mL dung dịch axit sunfuric loãng 0,5 M. Nồng độ mol của muối CuSO4 trong dung dịch sau phản ứng là (coi thể tích không đổi):", ["0,2 M", "0,1 M", "0,5 M", "0,05 M"], 0, "n_CuO = 0,02 mol -> n_CuSO4 = 0,02 mol -> CM = 0,02 / 0,1 = 0,2 M."),
        make_vdc(4, "Một mẫu quặng sắt chứa 80% Fe2O3. Để hòa tan hết 20 g mẫu quặng này cần bao nhiêu gam dung dịch axit clohiđric 14,6%?", ["150 g", "100 g", "200 g", "120 g"], 0, "m_Fe2O3 = 16 g -> n = 0,1 mol -> n_HCl = 0,6 mol -> m_HCl = 21,9 g -> m_dd = 21,9 / 14,6% = 150 g.")
    ]
}

print("Đã nạp xong Bài 8 (3 đề độc lập 100%)")
