# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - ÔN TẬP CUỐI CHƯƠNG II: MỘT SỐ HỢP CHẤT THÔNG DỤNG (5 ĐỀ ĐỘC LẬP 100%)
Gồm 5 đề thi độc lập 100%, không trùng câu hỏi, bám sát KNTT.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

exams_c2_rev = {}

# ==============================================================================
# ÔN TẬP CUỐI CHƯƠNG II (5 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Phân loại và tính chất của 4 loại hợp chất vô cơ ---
exams_c2_rev["chem8_c2_rev_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Chất nào sau đây làm quỳ tím chuyển sang màu đỏ?", ["Dung dịch axit clohiđric HCl", "Dung dịch natri hiđroxit NaOH", "Dung dịch muối ăn NaCl", "Nước cất tinh khiết"], 0, "Dung dịch axit làm quỳ tím hóa đỏ."),
        make_mc(2, "Nhận biết", "Dung dịch có pH = 12 có môi trường gì?", ["Môi trường bazơ (kiềm)", "Môi trường axit", "Môi trường trung tính", "Môi trường không xác định"], 0, "pH > 7 là môi trường bazơ."),
        make_mc(3, "Nhận biết", "Oxit nào sau đây là oxit axit?", ["CO2 (cacbon đioxit)", "CaO (canxi oxit)", "Na2O (natri oxit)", "CuO (đồng(II) oxit)"], 0, "CO2 là oxit axit tương ứng với H2CO3."),
        make_mc(4, "Nhận biết", "Muối nào sau đây KHÔNG TAN trong nước tạo kết tủa màu trắng?", ["BaSO4 (bari sunfat)", "NaCl (natri clorua)", "KNO3 (kali nitrat)", "CaCl2 (canxi clorua)"], 0, "BaSO4 là kết tủa trắng không tan."),
        make_mc(5, "Thông hiểu", "Cho dãy các chất: H2SO4, NaOH, CuSO4, CaO, Ba(OH)2, CO2. Có bao nhiêu bazơ trong dãy?", ["2", "3", "1", "4"], 0, "Có 2 bazơ: NaOH và Ba(OH)2."),
        make_mc(6, "Thông hiểu", "Khi cho kim loại kẽm Zn vào dung dịch axit sunfuric loãng, khí sinh ra là:", ["H2 (hiđro)", "O2 (oxi)", "SO2 (sunfurơ)", "H2S (hiđro sunfua)"], 0, "Zn + H2SO4 loãng -> ZnSO4 + H2."),
        make_mc(7, "Thông hiểu", "Phản ứng trung hòa là phản ứng giữa:", ["Axit và bazơ tạo muối và nước", "Kim loại và axit tạo muối và hiđro", "Oxit bazơ và oxit axit", "Hai dung dịch muối"], 0, "Định nghĩa phản ứng trung hòa: Axit + Bazơ -> Muối + Nước."),
        make_mc(8, "Thông hiểu", "Phân đạm cung cấp cho cây trồng nguyên tố dinh dưỡng nào sau đây?", ["Nitơ (N)", "Photpho (P)", "Kali (K)", "Canxi (Ca)"], 0, "Phân đạm cung cấp nitơ (N)."),
        make_mc(9, "Vận dụng", "Để nhận biết 3 dung dịch không màu: HCl, NaOH, NaCl, người ta chỉ cần dùng một thuốc thử duy nhất là:", ["Giấy quỳ tím", "Dung dịch phenolphtalein", "Kim loại đồng Cu", "Nước vôi trong"], 0, "Quỳ tím hóa đỏ với HCl, hóa xanh với NaOH, không đổi màu với NaCl."),
        make_mc(10, "Vận dụng", "Hòa tan hoàn toàn 4,0 g oxit đồng CuO vào dung dịch HCl dư. Khối lượng muối CuCl2 thu được là:", ["6,75 g", "13,5 g", "3,375 g", "8,0 g"], 0, "n_CuO = 4 / 80 = 0,05 mol -> m_CuCl2 = 0,05 * 135 = 6,75 g."),
        make_mc(11, "Vận dụng", "Một bao phân NPK có ghi 15-15-15. Số 15 thứ ba biểu thị phần trăm của chất nào?", ["%K2O (hàm lượng kali)", "%N", "%P2O5", "%Tro"], 0, "Theo quy ước: %N - %P2O5 - %K2O."),
        make_mc(12, "Vận dụng cao", "Hòa tan hết 10 g hỗn hợp gồm Fe và Cu vào lượng dư dung dịch axit HCl, sau phản ứng thu được 2,479 lít khí H2 ở đkc. Khối lượng Cu trong hỗn hợp là:", ["4,4 g", "5,6 g", "3,2 g", "6,4 g"], 0, "n_H2 = 0,1 mol -> n_Fe = 0,1 mol -> m_Fe = 5,6 g -> m_Cu = 10 - 5,6 = 4,4 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về 4 loại hợp chất vô cơ trong hóa học 8:", [
            ("a", "Axit gồm nguyên tử H liên kết với gốc axit.", True),
            ("b", "Bazơ gồm kim loại liên kết với một hay nhiều nhóm -OH.", True),
            ("c", "Oxit là hợp chất của 2 nguyên tố trong đó có 1 nguyên tố là oxi.", True),
            ("d", "Muối chỉ gồm duy nhất hai nguyên tố kim loại và phi kim.", False)
        ], "Muối có thể chứa nhiều nguyên tố (ví dụ muối có oxi như Na2SO4, CaCO3)."),
        make_tf(2, "Thông hiểu", "Về môi trường và thang đo pH:", [
            ("a", "Nước vắt từ quả chanh có pH < 7.", True),
            ("b", "Nước xà phòng tắm có pH > 7.", True),
            ("c", "Nước cất tinh khiết có pH = 7.", True),
            ("d", "Đất chua có pH > 7 cần bón thêm axit sunfuric loãng.", False)
        ], "Đất chua có pH < 7 cần bón vôi để khử chua."),
        make_tf(3, "Vận dụng", "Về phản ứng trao đổi trong dung dịch:", [
            ("a", "BaCl2 + Na2SO4 -> BaSO4 (kết tủa trắng) + 2NaCl.", True),
            ("b", "AgNO3 + NaCl -> AgCl (kết tủa trắng) + NaNO3.", True),
            ("c", "CuSO4 + 2NaOH -> Cu(OH)2 (kết tủa xanh lam) + Na2SO4.", True),
            ("d", "NaCl + KNO3 -> NaNO3 + KCl.", False)
        ], "Phản ứng không xảy ra do không có kết tủa hay khí."),
        make_tf(4, "Vận dụng cao", "Về vai trò và bảo quản phân bón hóa học:", [
            ("a", "Bón nhiều phân đạm làm cây tốt lá cành nhưng dễ bị sâu bệnh và gãy đổ.", True),
            ("b", "Phân đạm urê không nên bón cùng vôi bột vì giải phóng khí NH3 bay mất đạm.", True),
            ("c", "Phân lân kích thích phát triển rễ và ra hoa đậu quả.", True),
            ("d", "Phân kali giúp cây chịu rét, hạn và làm củ to hạt chắc.", True)
        ], "Cả 4 nhận định a, b, c, d đều chuẩn xác.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Gốc axit sunfat trong phân tử H2SO4 có hóa trị mấy?", "II", "Gốc =SO4 có hóa trị II."),
        make_sa(2, "Thông hiểu", "Chất chỉ thị phenolphtalein không màu chuyển sang màu gì trong dung dịch kiềm?", "hồng", "Chuyển sang màu hồng."),
        make_sa(3, "Thông hiểu", "Độ pH của dung dịch nước vôi trong lớn hơn hay nhỏ hơn 7? (Điền: lớn hơn)", "lớn hơn", "Dung dịch kiềm có pH > 7."),
        make_sa(4, "Vận dụng", "Hòa tan 0,2 mol NaOH cần bao nhiêu mol axit HCl để trung hòa hoàn toàn? (Ghi số thập phân)", "0,2", "NaOH + HCl -> tỉ lệ 1 : 1 nên cần 0,2 mol."),
        make_sa(5, "Vận dụng", "Khối lượng mol của muối bari sunfat BaSO4 là bao nhiêu g/mol?", "233", "M = 137 + 32 + 16*4 = 233 g/mol."),
        make_sa(6, "Vận dụng cao", "Nhiệt phân hoàn toàn 10 g đá vôi CaCO3 thu được bao nhiêu lít khí CO2 ở đkc? (Ghi số thập phân)", "2,479", "n = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hoàn toàn 6,5 g kim loại kẽm vào 100 mL dung dịch axit HCl 1 M. Sau phản ứng, chất nào còn dư và thể tích khí H2 thu được ở đkc là:", ["Zn dư; thu được 1,2395 lít H2", "HCl dư; thu được 2,479 lít H2", "Cả hai chất phản ứng vừa hết", "Zn dư; thu được 2,479 lít H2"], 0, "n_Zn = 0,1 mol; n_HCl = 0,1 mol -> HCl hết, Zn dư 0,05 mol -> n_H2 = 0,05 mol -> V = 1,2395 L."),
        make_vdc(2, "Trộn 100 mL dung dịch Ba(OH)2 0,5 M với 100 mL dung dịch H2SO4 0,5 M thu được m gam kết tủa. Giá trị của m là:", ["11,65 g", "23,3 g", "5,825 g", "10,4 g"], 0, "n = 0,05 mol -> m_BaSO4 = 0,05 * 233 = 11,65 g."),
        make_vdc(3, "Một loại phân đạm chứa 92% muối amoni nitrat NH4NO3 (M = 80 g/mol). Hàm lượng phần trăm nitơ (%N) trong loại phân này xấp xỉ bằng:", ["32,2%", "35,0%", "46,0%", "28,5%"], 0, "%N = 92% * (28 / 80) = 32,2%."),
        make_vdc(4, "Cho luồng khí CO2 dư đi qua 200 mL dung dịch Ca(OH)2 0,5 M. Sau phản ứng hoàn toàn thu được kết tủa rồi kết tủa tan hết tạo dung dịch muối axit. Khối lượng muối Ca(HCO3)2 tạo thành là:", ["16,2 g", "10,0 g", "8,1 g", "20,0 g"], 0, "n_Ca(OH)2 = 0,1 mol -> n_Ca(HCO3)2 = 0,1 mol -> m = 0,1 * 162 = 16,2 g.")
    ]
}

# --- ĐỀ 2, 3, 4, 5: Độc lập 100% ---
# Đề 2: Tính toán phản ứng của oxit và axit
exams_c2_rev["chem8_c2_rev_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Dung dịch chất nào sau đây làm quỳ tím hóa xanh?", ["KOH (kali hiđroxit)", "HCl", "NaCl", "H2SO4"], 0, "Dung dịch kiềm KOH làm quỳ tím hóa xanh."),
        make_mc(2, "Nhận biết", "Oxit nào sau đây tác dụng với nước tạo thành dung dịch axit?", ["SO3", "CaO", "CuO", "Na2O"], 0, "SO3 + H2O -> H2SO4."),
        make_mc(3, "Nhận biết", "Muối ăn hàng ngày dùng trong nấu ăn có công thức hóa học là:", ["NaCl", "KCl", "CaCl2", "BaCl2"], 0, "Natri clorua NaCl."),
        make_mc(4, "Nhận biết", "Kim loại nào sau đây KHÔNG tác dụng với dung dịch axit sunfuric loãng?", ["Đồng (Cu)", "Sắt (Fe)", "Kẽm (Zn)", "Nhôm (Al)"], 0, "Cu đứng sau H nên không tác dụng với H2SO4 loãng."),
        make_mc(5, "Thông hiểu", "Sản phẩm của phản ứng giữa axit clohiđric HCl và natri hiđroxit NaOH là:", ["NaCl và H2O", "Na2O và H2", "NaClO và H2", "Na và Cl2"], 0, "HCl + NaOH -> NaCl + H2O."),
        make_mc(6, "Thông hiểu", "Độ pH của máu người khỏe mạnh ổn định ở khoảng:", ["7,35 - 7,45", "1,5 - 2,5", "8,5 - 9,5", "5,0 - 6,0"], 0, "pH máu hơi kiềm nhẹ ổn định ở 7,35 - 7,45."),
        make_mc(7, "Thông hiểu", "Oxit nào sau đây là oxit lưỡng tính vừa tác dụng axit vừa tác dụng bazơ?", ["Al2O3", "CaO", "CO2", "Na2O"], 0, "Al2O3 là oxit lưỡng tính."),
        make_mc(8, "Thông hiểu", "Cho mẩu đá vôi vào dung dịch axit HCl, hiện tượng quan sát được là:", ["Đá vôi tan dần và sủi bọt khí CO2", "Xuất hiện kết tủa màu vàng", "Có kết tủa màu xanh lam", "Dung dịch bốc cháy sáng"], 0, "CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (sủi bọt khí)."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 2,4 g bột Mg vào dung dịch HCl dư. Thể tích khí H2 sinh ra ở đkc (25 °C, 1 bar) là:", ["2,479 lít", "4,958 lít", "2,24 lít", "1,12 lít"], 0, "n_Mg = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."),
        make_mc(10, "Vận dụng", "Để phân biệt 2 lọ dung dịch mất nhãn chứa NaOH và Ca(OH)2, thuốc thử thích hợp nhất là:", ["Thổi khí CO2 vào", "Dùng quỳ tím", "Dùng dung dịch HCl", "Dùng phenolphtalein"], 0, "Khí CO2 làm Ca(OH)2 vẩn đục trắng CaCO3, còn NaOH không vẩn đục."),
        make_mc(11, "Vận dụng", "Hòa tan 8 g CuO trong dung dịch H2SO4 loãng vừa đủ. Khối lượng muối CuSO4 thu được là:", ["16 g", "8 g", "32 g", "24 g"], 0, "n = 0,1 mol -> m = 0,1 * 160 = 16 g."),
        make_mc(12, "Vận dụng cao", "Trộn 200 mL dung dịch HCl 1 M với 200 mL dung dịch NaOH 1,5 M. Dung dịch sau phản ứng có môi trường gì và pH như thế nào?", ["Môi trường kiềm, pH > 7", "Môi trường axit, pH < 7", "Môi trường trung tính, pH = 7", "Không đổi"], 0, "n_NaOH = 0,3 mol > n_HCl = 0,2 mol -> NaOH dư, dung dịch có tính kiềm, pH > 7."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về tính chất hóa học của bazơ:", [
            ("a", "Dung dịch bazơ làm quỳ tím chuyển sang màu xanh.", True),
            ("b", "Tất cả các bazơ đều bị nhiệt phân hủy khi đun nóng.", False),
            ("c", "Bazơ tác dụng với oxit axit tạo thành muối và nước.", True),
            ("d", "Bazơ tác dụng với axit tạo thành muối và nước.", True)
        ], "Các bazơ kiềm như NaOH, KOH không bị nhiệt phân bởi đèn cồn."),
        make_tf(2, "Thông hiểu", "Về oxit bazơ và oxit axit:", [
            ("a", "CaO, Na2O là các oxit bazơ tan trong nước tạo dung dịch kiềm.", True),
            ("b", "CuO, Fe2O3 là các oxit bazơ không tan trong nước nhưng tan trong axit.", True),
            ("c", "CO2, SO2 là các oxit axit tác dụng với dung dịch kiềm tạo muối cacbonat, sunfit.", True),
            ("d", "CO là oxit axit tác dụng mạnh với nước tạo axit cacbonic.", False)
        ], "CO là oxit trung tính không tác dụng với nước."),
        make_tf(3, "Vận dụng", "Cho các phản ứng tạo kết tủa trong dung dịch:", [
            ("a", "CuSO4 + 2NaOH -> Cu(OH)2 (kết tủa xanh lam) + Na2SO4.", True),
            ("b", "FeCl3 + 3KOH -> Fe(OH)3 (kết tủa nâu đỏ) + 3KCl.", True),
            ("c", "BaCl2 + H2SO4 -> BaSO4 (kết tủa trắng) + 2HCl.", True),
            ("d", "NaCl + H2SO4 loãng -> Na2SO4 + 2HCl.", False)
        ], "Không có kết tủa hay khí nên phản ứng không xảy ra trong dung dịch loãng."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm cho dây sắt nhúng vào dung dịch đồng(II) sunfat CuSO4:", [
            ("a", "Kim loại đồng màu đỏ bám trên bề mặt dây sắt.", True),
            ("b", "Màu xanh lam của dung dịch nhạt dần.", True),
            ("c", "Khối lượng dây sắt tăng lên sau phản ứng.", True),
            ("d", "Dung dịch sau phản ứng chứa muối sắt(III) sunfat Fe2(SO4)3.", False)
        ], "Tạo muối sắt(II) sunfat FeSO4.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong hợp chất oxit, hóa trị của nguyên tố oxi luôn là mấy?", "II", "Oxi luôn có hóa trị II."),
        make_sa(2, "Thông hiểu", "Dung dịch có pH = 7 là môi trường gì? (Điền: trung tính)", "trung tính", "Môi trường trung tính."),
        make_sa(3, "Thông hiểu", "Cho các chất: HCl, NaOH, Na2SO4, CaO. Có bao nhiêu hợp chất muối?", "1", "Chỉ có Na2SO4 là muối (1 chất)."),
        make_sa(4, "Vận dụng", "Cần bao nhiêu mL dung dịch NaOH 1 M để trung hòa hoàn toàn 100 mL dung dịch HCl 1 M?", "100", "Tỉ lệ 1 : 1 -> cần 100 mL."),
        make_sa(5, "Vận dụng", "Khối lượng mol của muối đồng(II) sunfat CuSO4 là bao nhiêu g/mol?", "160", "M = 64 + 32 + 16*4 = 160 g/mol."),
        make_sa(6, "Vận dụng cao", "Cho 0,1 mol kim loại Zn phản ứng vừa hết với bao nhiêu gam axit HCl? (Ghi số thập phân)", "7,3", "n_HCl = 0,2 mol -> m = 0,2 * 36,5 = 7,3 g.")
    ],
    "part4": [
        make_vdc(1, "Cho 13 g kim loại Zn tác dụng vừa đủ với dung dịch axit HCl thu được dung dịch chứa m gam muối ZnCl2. Giá trị của m là:", ["27,2 g", "13,6 g", "54,4 g", "20,4 g"], 0, "n_Zn = 0,2 mol -> m_ZnCl2 = 0,2 * 136 = 27,2 g."),
        make_vdc(2, "Sục 2,479 lít khí CO2 ở đkc vào 150 mL dung dịch Ba(OH)2 1 M thu được kết tủa trắng BaCO3. Khối lượng kết tủa BaCO3 thu được là:", ["19,7 g", "29,55 g", "9,85 g", "39,4 g"], 0, "n_CO2 = 0,1 mol; n_Ba(OH)2 = 0,15 mol -> Ba(OH)2 dư, tính theo CO2 -> m_BaCO3 = 0,1 * 197 = 19,7 g."),
        make_vdc(3, "Để trung hòa 200 mL dung dịch hỗn hợp gồm HCl 0,5 M và H2SO4 0,25 M cần bao nhiêu mL dung dịch NaOH 1 M?", ["200 mL", "150 mL", "300 mL", "100 mL"], 0, "Tổng mol H+ = 0,2 * 0,5 + 0,2 * 0,25 * 2 = 0,1 + 0,1 = 0,2 mol -> n_NaOH = 0,2 mol -> V = 0,2 L = 200 mL."),
        make_vdc(4, "Một loại phân đạm urê có độ tinh khiết 95% (chứa 95% (NH2)2CO). Hàm lượng phần trăm nitơ (%N) trong bao phân này là:", ["44,3%", "46,7%", "35,0%", "40,0%"], 0, "%N = 95% * (28 / 60) = 44,33% xấp xỉ 44,3%.")
    ]
}

# Đề 3: Chuỗi phản ứng và nhận biết chất
exams_c2_rev["chem8_c2_rev_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Muối nào sau đây có tên gọi là canxi cacbonat?", ["CaCO3", "CaSO4", "CaCl2", "CaO"], 0, "CaCO3 là canxi cacbonat."),
        make_mc(2, "Nhận biết", "Dung dịch kiềm NaOH có thể hòa tan được oxit nào sau đây?", ["CO2 (oxit axit)", "CaO", "Na2O", "CuO"], 0, "CO2 + 2NaOH -> Na2CO3 + H2O."),
        make_mc(3, "Nhận biết", "Axit nào sau đây có trong quả chanh, cam tạo vị chua thanh?", ["Axit xitric", "Axit sunfuric", "Axit clohiđric", "Axit nitric"], 0, "Quả chanh chứa axit xitric tự nhiên."),
        make_mc(4, "Nhận biết", "Dung dịch có pH = 7 là dung dịch có môi trường:", ["Trung tính", "Axit", "Bazơ", "Không xác định"], 0, "pH = 7 là môi trường trung tính."),
        make_mc(5, "Thông hiểu", "Cho sơ đồ chuyển hóa: Ca -> CaO -> Ca(OH)2. Hai phản ứng lần lượt là tác dụng với:", ["O2 rồi tác dụng với H2O", "H2O rồi tác dụng với O2", "CO2 rồi tác dụng với HCl", "Axit rồi tác dụng với bazơ"], 0, "2Ca + O2 -> 2CaO; CaO + H2O -> Ca(OH)2."),
        make_mc(6, "Thông hiểu", "Phản ứng giữa dung dịch bạc nitrat AgNO3 và dung dịch natri clorua NaCl sinh ra kết tủa trắng là:", ["AgCl", "NaNO3", "Ag2O", "Ag2CO3"], 0, "AgNO3 + NaCl -> AgCl (trắng) + NaNO3."),
        make_mc(7, "Thông hiểu", "Để nhận biết khí CO2 thoát ra từ phản ứng nung đá vôi, người ta dẫn khí qua dung dịch nào?", ["Dung dịch nước vôi trong Ca(OH)2 thấy vẩn đục", "Dung dịch axit HCl", "Dung dịch muối ăn NaCl", "Dung dịch cồn"], 0, "Khí CO2 làm vẩn đục nước vôi trong."),
        make_mc(8, "Thông hiểu", "Phân bón NPK thuộc loại phân bón nào?", ["Phân bón hỗn hợp", "Phân đơn", "Phân vi sinh", "Phân hữu cơ"], 0, "NPK là phân hỗn hợp chứa cả 3 nguyên tố N, P, K."),
        make_mc(9, "Vận dụng", "Hòa tan 5,6 g Fe vào 200 mL dung dịch H2SO4 1 M. Sau phản ứng hoàn toàn, thể tích khí H2 thu được ở đkc là:", ["2,479 lít", "4,958 lít", "2,24 lít", "1,2395 lít"], 0, "n_Fe = 0,1 mol; n_H2SO4 = 0,2 mol -> Fe hết -> V = 0,1 * 24,79 = 2,479 L."),
        make_mc(10, "Vận dụng", "Nhiệt phân hoàn toàn 19,6 g Cu(OH)2 thu được m gam bột CuO màu đen. Giá trị của m là:", ["16,0 g", "8,0 g", "12,8 g", "20,0 g"], 0, "n = 19,6 / 98 = 0,2 mol -> m_CuO = 0,2 * 80 = 16,0 g."),
        make_mc(11, "Vận dụng", "Cần dùng bao nhiêu gam muối NaCl để pha thành 500 g dung dịch nước muối sinh lí 0,9%?", ["4,5 g", "9,0 g", "0,9 g", "45 g"], 0, "m = 500 * 0,9% = 4,5 g."),
        make_mc(12, "Vận dụng cao", "Dẫn 4,958 lít khí CO2 ở đkc vào dung dịch chứa 0,15 mol Ba(OH)2 thu được m gam kết tủa BaCO3. Giá trị của m là:", ["19,7 g", "29,55 g", "39,4 g", "9,85 g"], 0, "n_CO2 = 0,2 mol; n_Ba(OH)2 = 0,15 mol -> T = 0,2/0,15 = 1,33 -> n_BaCO3 = 0,15*2 - 0,2 = 0,1 mol -> m = 19,7 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các phản ứng của axit và bazơ:", [
            ("a", "Phản ứng giữa axit và bazơ luôn tạo ra muối và nước.", True),
            ("b", "Nhiệt độ của phản ứng trung hòa thường tăng lên do phản ứng tỏa nhiệt.", True),
            ("c", "Tất cả các bazơ đều tan vô hạn trong nước.", False),
            ("d", "Chỉ thị phenolphtalein đổi màu hồng trong môi trường kiềm.", True)
        ], "Nhiều bazơ như Cu(OH)2, Fe(OH)3 không tan trong nước."),
        make_tf(2, "Thông hiểu", "Về tính tan của muối trong nước:", [
            ("a", "Tất cả các muối nitrat đều tan tốt trong nước.", True),
            ("b", "Muối cacbonat của canxi CaCO3 tan rất tốt trong nước tạo dung dịch kiềm.", False),
            ("c", "Bari sunfat BaSO4 không tan trong nước và cả trong dung dịch axit mạnh.", True),
            ("d", "Muối clorua tan tốt trừ AgCl không tan.", True)
        ], "CaCO3 là chất kết tủa không tan trong nước."),
        make_tf(3, "Vận dụng", "Về phân bón hóa học:", [
            ("a", "Phân kali giúp cây chống chịu rét, hạn và sâu bệnh.", True),
            ("b", "Phân đạm thúc đẩy sinh trưởng cành lá xanh tốt.", True),
            ("c", "Phân lân thúc đẩy quá trình đẻ nhánh, ra hoa và phát triển bộ rễ.", True),
            ("d", "Bón phân đạm urê vào đất có tính kiềm mạnh sẽ làm tăng hiệu quả hấp thụ của cây.", False)
        ], "Môi trường kiềm làm phân urê phân hủy thoát khí amoniac gây thất thoát đạm."),
        make_tf(4, "Vận dụng cao", "Cho m gam kim loại kẽm Zn vào dung dịch muối đồng sunfat CuSO4 dư:", [
            ("a", "Kim loại kẽm tan dần và có kim loại màu đỏ bám trên bề mặt kẽm.", True),
            ("b", "Khối lượng thanh kim loại sau phản ứng tăng lên so với ban đầu.", False),
            ("c", "Khối lượng thanh kim loại giảm đi vì 1 mol Zn (65g) tan ra chỉ có 1 mol Cu (64g) bám vào.", True),
            ("d", "Màu xanh lam của dung dịch nhạt dần theo thời gian.", True)
        ], "Khối lượng thanh kẽm giảm nhẹ: 65 - 64 = 1 g/mol.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Công thức hóa học của khí cacbonic là gì? (Điền: CO2)", "CO2", "Khí cacbonic là CO2."),
        make_sa(2, "Thông hiểu", "Dung dịch kiềm NaOH làm phenolphtalein chuyển sang màu gì?", "hồng", "Chuyển sang màu hồng."),
        make_sa(3, "Thông hiểu", "Khối lượng mol của oxit canxi CaO là bao nhiêu g/mol?", "56", "M = 40 + 16 = 56 g/mol."),
        make_sa(4, "Vận dụng", "Số mol khí H2 sinh ra khi cho 0,2 mol nhôm Al phản ứng hết với HCl dư là bao nhiêu mol? (Ghi số thập phân)", "0,3", "0,2 * 1,5 = 0,3 mol H2."),
        make_sa(5, "Vận dụng", "Hòa tan hết 4 g NaOH vào nước được 250 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)", "0,4", "n = 0,1 mol -> CM = 0,1 / 0,25 = 0,4 M."),
        make_sa(6, "Vận dụng cao", "Để hòa tan hoàn toàn 8 g oxit CuO cần vừa đủ bao nhiêu gam axit HCl nguyên chất? (Ghi số thập phân)", "7,3", "n_CuO = 0,1 mol -> n_HCl = 0,2 mol -> m = 0,2 * 36,5 = 7,3 g.")
    ],
    "part4": [
        make_vdc(1, "Đốt cháy hoàn toàn 11,2 g bột sắt trong khí oxi dư thu được oxit sắt từ Fe3O4. Khối lượng Fe3O4 thu được là:", ["15,47 g", "16,0 g", "11,6 g", "23,2 g"], 0, "3Fe + 2O2 -> Fe3O4. n_Fe = 0,2 mol -> n_Fe3O4 = 0,2 / 3 mol -> m = 0,2/3 * 232 = 15,47 g."),
        make_vdc(2, "Hòa tan 14,8 g Ca(OH)2 vào nước thu được 500 mL dung dịch. Nồng độ mol của dung dịch nước vôi thu được là:", ["0,4 M", "0,2 M", "0,5 M", "0,1 M"], 0, "n = 14,8 / 74 = 0,2 mol -> CM = 0,2 / 0,5 = 0,4 M."),
        make_vdc(3, "Nhiệt phân hoàn toàn 50 g đá vôi CaCO3 thu được bao nhiêu gam vôi sống CaO?", ["28 g", "56 g", "14 g", "22 g"], 0, "n = 0,5 mol -> m_CaO = 0,5 * 56 = 28 g."),
        make_vdc(4, "Một dung dịch chứa 0,2 mol BaCl2. Cần thêm vào dung dịch bao nhiêu mol Na2SO4 để kết tủa hoàn toàn ion Ba2+?", ["0,2 mol", "0,1 mol", "0,4 mol", "0,3 mol"], 0, "Tỉ lệ 1 : 1 -> cần đúng 0,2 mol Na2SO4.")
    ]
}

# Đề 4 & Đề 5: Hoàn thiện đủ 5 đề độc lập 100%
exams_c2_rev["chem8_c2_rev_test4"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Chất nào sau đây là oxit trung tính không tạo muối?", ["CO (cacbon monooxit)", "CO2", "CaO", "SO2"], 0, "CO là oxit trung tính."),
        make_mc(2, "Nhận biết", "Dung dịch axit có giá trị pH nằm trong khoảng nào?", ["pH < 7", "pH = 7", "pH > 7", "pH = 14"], 0, "pH < 7 là môi trường axit."),
        make_mc(3, "Nhận biết", "Muối nào sau đây dùng làm bột nở khi làm bánh?", ["NaHCO3 (natri hidrocacbonat)", "NaCl", "BaSO4", "CuSO4"], 0, "Baking soda NaHCO3 dùng làm bột nở."),
        make_mc(4, "Nhận biết", "Trong nông nghiệp, vôi tôi Ca(OH)2 được dùng để:", ["Khử chua cho đất và sát trùng chuồng trại", "Làm đông đất", "Làm tăng độ mặn của đất", "Cung cấp đạm cho cây"], 0, "Vôi tôi khử chua đất và diệt khuẩn chuồng trại."),
        make_mc(5, "Thông hiểu", "Cho dãy các chất: CuO, Ba(OH)2, HCl, Na2CO3, CO2. Chất nào phản ứng được với dung dịch HCl sinh chất khí?", ["Na2CO3 (sinh khí CO2)", "CuO", "Ba(OH)2", "CO2"], 0, "Na2CO3 + 2HCl -> 2NaCl + H2O + CO2 (khí)."),
        make_mc(6, "Thông hiểu", "Sản phẩm của phản ứng giữa kim loại magie và axit sunfuric loãng là:", ["MgSO4 và H2", "MgO và H2", "MgSO3 và H2", "MgS và H2O"], 0, "Mg + H2SO4 -> MgSO4 + H2."),
        make_mc(7, "Thông hiểu", "Hiện tượng nước đá vôi để lâu ngoài không khí xuất hiện một lớp màng mỏng cứng trên bề mặt là do:", ["Ca(OH)2 tác dụng với khí CO2 trong không khí tạo CaCO3", "Nước bay hơi hết", "Vôi bị thối rữa", "Bụi bẩn bám vào"], 0, "Ca(OH)2 + CO2 -> CaCO3 (màng cứng trắng) + H2O."),
        make_mc(8, "Thông hiểu", "Phân kali cung cấp cho cây trồng nguyên tố nào?", ["Kali (K)", "Nitơ (N)", "Photpho (P)", "Oxi (O)"], 0, "Phân kali cung cấp nguyên tố K."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 5,4 g kim loại Al vào dung dịch axit HCl dư. Thể tích khí H2 thoát ra ở đkc (25 °C, 1 bar) là:", ["7,437 lít", "4,958 lít", "2,479 lít", "6,72 lít"], 0, "n_Al = 0,2 mol -> n_H2 = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."),
        make_mc(10, "Vận dụng", "Để trung hòa hoàn toàn 100 mL dung dịch H2SO4 0,5 M cần bao nhiêu mL dung dịch NaOH 1 M?", ["100 mL", "50 mL", "200 mL", "150 mL"], 0, "H2SO4 + 2NaOH -> n_H2SO4 = 0,05 mol -> n_NaOH = 0,1 mol -> V = 0,1 L = 100 mL."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 2,4 g bột magie trong khí oxi dư thu được bao nhiêu gam magie oxit MgO?", ["4,0 g", "3,6 g", "6,0 g", "2,8 g"], 0, "n = 0,1 mol -> m = 0,1 * 40 = 4,0 g."),
        make_mc(12, "Vận dụng cao", "Cho dung dịch chứa 0,1 mol AgNO3 tác dụng với dung dịch chứa 0,1 mol CaCl2. Khối lượng kết tủa AgCl thu được là:", ["14,35 g", "28,7 g", "7,175 g", "21,525 g"], 0, "2AgNO3 + CaCl2 -> 2AgCl + Ca(NO3)2. n_AgCl = 0,1 mol -> m = 0,1 * 143,5 = 14,35 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các phản ứng của hợp chất vô cơ:", [
            ("a", "Oxit axit tác dụng với dung dịch kiềm tạo thành muối và nước.", True),
            ("b", "Axit tác dụng với kim loại đứng sau H trong dãy hoạt động giải phóng khí H2.", False),
            ("c", "Bazơ không tan bị phân hủy ở nhiệt độ cao tạo oxit bazơ và nước.", True),
            ("d", "Phản ứng trao đổi trong dung dịch chỉ xảy ra khi có chất kết tủa hoặc chất khí sinh ra.", True)
        ], "Kim loại sau H không giải phóng H2."),
        make_tf(2, "Thông hiểu", "Về nồng độ và pH:", [
            ("a", "Độ pH là chỉ số đo độ hoạt động của ion H+ trong dung dịch.", True),
            ("b", "Dung dịch kiềm có nồng độ OH- cao hơn nồng độ H+.", True),
            ("c", "Pha loãng dung dịch axit bằng nước làm pH của dung dịch tăng dần về 7.", True),
            ("d", "Pha loãng dung dịch kiềm bằng nước làm pH của dung dịch tăng vọt lên 14.", False)
        ], "Pha loãng kiềm làm giảm nồng độ OH-, pH giảm dần về 7."),
        make_tf(3, "Vận dụng", "Về ứng dụng thực tiễn của các hợp chất:", [
            ("a", "NaCl dùng làm gia vị thức ăn và bảo quản thịt cá.", True),
            ("b", "CaCO3 là thành phần chính của đá vôi dùng làm vật liệu xây dựng và sản xuất xi măng.", True),
            ("c", "CuSO4 dùng làm thuốc trừ nấm mốc trong nông nghiệp (dung dịch Booc-đô).", True),
            ("d", "H2SO4 đặc dùng làm nước giải khát mùa hè.", False)
        ], "H2SO4 là hóa chất độc hại, ăn mòn cực mạnh không uống được."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng cho dung dịch Na2CO3 vào dung dịch CaCl2:", [
            ("a", "Phương trình: Na2CO3 + CaCl2 -> CaCO3 (kết tủa trắng) + 2NaCl.", True),
            ("b", "Lọc lấy kết tủa hòa tan vào dung dịch axit HCl thấy sủi bọt khí CO2.", True),
            ("c", "Dung dịch lọc sau khi bỏ kết tủa chứa muối ăn NaCl.", True),
            ("d", "Đây là phản ứng oxi hóa - khử.", False)
        ], "Đây là phản ứng trao đổi không thay đổi số oxi hóa.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Phân đạm urê có chứa nguyên tố dinh dưỡng nào? (Điền: nitơ)", "nitơ", "Chứa nguyên tố nitơ."),
        make_sa(2, "Thông hiểu", "Muối bari sunfat BaSO4 có tan trong nước không? (Điền: có hoặc không)", "không", "BaSO4 là kết tủa trắng không tan."),
        make_sa(3, "Thông hiểu", "Khối lượng mol của oxit đồng CuO là bao nhiêu g/mol?", "80", "M = 64 + 16 = 80 g/mol."),
        make_sa(4, "Vận dụng", "Cần bao nhiêu gam NaOH để trung hòa 0,1 mol axit HCl?", "4", "n = 0,1 mol -> m = 0,1 * 40 = 4 g."),
        make_sa(5, "Vận dụng", "Số mol khí CO2 sinh ra khi nhiệt phân 20 g CaCO3 là bao nhiêu mol? (Ghi số thập phân)", "0,2", "n = 20 / 100 = 0,2 mol."),
        make_sa(6, "Vận dụng cao", "Cho 0,1 mol Zn phản ứng hoàn toàn với dung dịch CuSO4 dư thu được bao nhiêu gam Cu?", "6,4", "n = 0,1 mol -> m_Cu = 0,1 * 64 = 6,4 g.")
    ],
    "part4": [
        make_vdc(1, "Cho 10 g CaCO3 tác dụng hoàn toàn với lượng dư dung dịch axit HCl. Thể tích khí CO2 thu được ở đkc (25 °C, 1 bar) là:", ["2,479 lít", "4,958 lít", "1,2395 lít", "3,7185 lít"], 0, "n = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."),
        make_vdc(2, "Hòa tan 11,2 g bột sắt Fe vào dung dịch H2SO4 loãng dư. Thể tích khí H2 sinh ra ở đkc là:", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "n_Fe = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."),
        make_vdc(3, "Hòa tan 8 g CuO trong 100 mL dung dịch HCl 2,5 M. Nồng độ mol của CuCl2 thu được trong dung dịch sau phản ứng là (coi thể tích không đổi):", ["1,0 M", "0,5 M", "2,0 M", "0,1 M"], 0, "n_CuO = 0,1 mol -> n_CuCl2 = 0,1 mol -> CM = 0,1 / 0,1 = 1,0 M."),
        make_vdc(4, "Một hỗn hợp gồm 0,1 mol BaCl2 và 0,1 mol Na2SO4 hòa tan vào nước thu được m gam kết tủa. Giá trị của m là:", ["23,3 g", "11,65 g", "46,6 g", "15,5 g"], 0, "n = 0,1 mol -> m = 0,1 * 233 = 23,3 g.")
    ]
}

exams_c2_rev["chem8_c2_rev_test5"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Hợp chất nào sau đây là oxit axit?", ["P2O5", "K2O", "Fe2O3", "BaO"], 0, "P2O5 là oxit axit tương ứng với H3PO4."),
        make_mc(2, "Nhận biết", "Dung dịch kiềm có giá trị pH nằm trong khoảng nào?", ["pH > 7", "pH = 7", "pH < 7", "pH = 0"], 0, "Dung dịch kiềm có pH > 7."),
        make_mc(3, "Nhận biết", "Muối nào sau đây kết tủa màu trắng không tan trong nước?", ["AgCl", "NaCl", "CuSO4", "KNO3"], 0, "AgCl là kết tủa trắng."),
        make_mc(4, "Nhận biết", "Phân lân cung cấp cho cây trồng nguyên tố dinh dưỡng nào?", ["Photpho (P)", "Nitơ (N)", "Kali (K)", "Canxi (Ca)"], 0, "Phân lân cung cấp photpho."),
        make_mc(5, "Thông hiểu", "Cho dãy các chất: HCl, NaOH, CaCO3, SO2, Cu(OH)2, KNO3. Số muối trong dãy là:", ["2", "3", "1", "4"], 0, "Có 2 muối: CaCO3 và KNO3."),
        make_mc(6, "Thông hiểu", "Phản ứng giữa dung dịch axit clohiđric và đồng(II) oxit CuO tạo ra dung dịch có màu:", ["Màu xanh lam", "Màu nâu đỏ", "Không màu", "Màu vàng"], 0, "CuO + 2HCl -> CuCl2 (màu xanh lam) + H2O."),
        make_mc(7, "Thông hiểu", "Khí nào sau đây thoát ra khi cho kẽm vào axit clohiđric?", ["Khí hiđro (H2)", "Khí oxi", "Khí clo", "Khí cacbonic"], 0, "Zn + 2HCl -> ZnCl2 + H2."),
        make_mc(8, "Thông hiểu", "Khử chua cho đất nông nghiệp bằng cách bón vôi là ứng dụng của phản ứng nào?", ["Phản ứng trung hòa giữa bazơ và axit", "Phản ứng oxi hóa - khử", "Phản ứng phân hủy", "Phản ứng trùng hợp"], 0, "Trung hòa axit trong đất bằng kiềm của vôi."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 4,8 g kim loại magie vào dung dịch axit HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "n_Mg = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."),
        make_mc(10, "Vận dụng", "Để phân biệt dung dịch H2SO4 và dung dịch HCl, người ta dùng thuốc thử tốt nhất là:", ["Dung dịch BaCl2", "Quỳ tím", "Dung dịch NaOH", "Kim loại kẽm"], 0, "BaCl2 tạo kết tủa trắng BaSO4 với H2SO4, còn HCl không có hiện tượng."),
        make_mc(11, "Vận dụng", "Hòa tan 11,2 g bột sắt Fe vào dung dịch axit sunfuric loãng vừa đủ. Khối lượng muối FeSO4 thu được là:", ["30,4 g", "15,2 g", "60,8 g", "22,8 g"], 0, "n_Fe = 0,2 mol -> m_FeSO4 = 0,2 * 152 = 30,4 g."),
        make_mc(12, "Vận dụng cao", "Dẫn 2,479 lít khí CO2 ở đkc vào 200 mL dung dịch Ba(OH)2 0,5 M thu được m gam kết tủa trắng BaCO3. Giá trị của m là:", ["19,7 g", "9,85 g", "29,55 g", "39,4 g"], 0, "n_CO2 = 0,1 mol; n_Ba(OH)2 = 0,1 mol -> phản ứng vừa đủ tạo 0,1 mol BaCO3 -> m = 19,7 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất đặc trưng của axit, bazơ, oxit, muối:", [
            ("a", "Dung dịch axit làm quỳ tím hóa đỏ.", True),
            ("b", "Dung dịch kiềm làm quỳ tím hóa xanh.", True),
            ("c", "Oxit kim loại luôn luôn tan tốt trong nước ở nhiệt độ thường.", False),
            ("d", "Phản ứng giữa axit và bazơ luôn tạo thành muối và nước.", True)
        ], "Nhiều oxit kim loại như CuO, Fe2O3, Al2O3 không tan trong nước."),
        make_tf(2, "Thông hiểu", "Về thang đo pH và sức khỏe con người:", [
            ("a", "Dung dịch có pH < 7 là môi trường axit.", True),
            ("b", "Dịch dạ dày có pH axit thấp (khoảng 1,5 - 3,5) giúp tiêu hóa thức ăn.", True),
            ("c", "Khi bị đau dạ dày do dư axit, người ta có thể uống thuốc muối Nabica (NaHCO3).", True),
            ("d", "Uống dung dịch kiềm đặc NaOH là phương pháp tốt nhất để chữa đau dạ dày.", False)
        ], "NaOH kiềm mạnh ăn mòn da và niêm mạc cực kì nguy hiểm."),
        make_tf(3, "Vận dụng", "Về phân bón hóa học trong nông nghiệp:", [
            ("a", "Phân đạm thúc đẩy quá trình sinh trưởng cành lá xanh tốt.", True),
            ("b", "Phân lân kích thích sự phát triển của hệ rễ và củ.", True),
            ("c", "Phân kali giúp cây trồng tăng khả năng chống chịu rét và sâu bệnh.", True),
            ("d", "Bón càng nhiều phân hóa học thì cây càng xanh tốt và đất càng tơi xốp.", False)
        ], "Lạm dụng phân bón hóa học gây chai hóa đất và ô nhiễm nguồn nước."),
        make_tf(4, "Vận dụng cao", "Cho mẩu kim loại natri vào cốc đựng dung dịch đồng(II) sunfat CuSO4:", [
            ("a", "Natri phản ứng mãnh liệt với nước trong dung dịch tạo NaOH và khí H2 bay lên.", True),
            ("b", "Dung dịch NaOH sinh ra phản ứng với CuSO4 tạo kết tủa xanh lam Cu(OH)2.", True),
            ("c", "Kim loại đồng màu đỏ bám ngoài mẩu natri.", False),
            ("d", "Hiện tượng quan sát được: Natri tan dần sủi bọt khí và xuất hiện kết tủa màu xanh lam.", True)
        ], "Na không đẩy Cu trực tiếp mà tác dụng với nước trước.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong 1 phân tử phân đạm urê (NH2)2CO có bao nhiêu nguyên tử nitơ?", "2", "Có 2 nguyên tử nitơ."),
        make_sa(2, "Thông hiểu", "Dung dịch muối ăn NaCl có làm đổi màu giấy quỳ tím không? (Điền: có hoặc không)", "không", "Muối trung tính không đổi màu quỳ tím."),
        make_sa(3, "Thông hiểu", "Khối lượng mol của muối canxi cacbonat CaCO3 là bao nhiêu g/mol?", "100", "M = 100 g/mol."),
        make_sa(4, "Vận dụng", "Hòa tan 0,1 mol kim loại kẽm Zn vào axit HCl dư. Thể tích khí H2 sinh ra ở đkc là bao nhiêu lít? (Ghi số thập phân)", "2,479", "V = 0,1 * 24,79 = 2,479 L."),
        make_sa(5, "Vận dụng", "Để trung hòa hoàn toàn 0,2 mol axit H2SO4 cần bao nhiêu mol NaOH? (Ghi số thập phân)", "0,4", "Tỉ lệ 1 : 2 -> cần 0,4 mol NaOH."),
        make_sa(6, "Vận dụng cao", "Nhiệt phân hoàn toàn 20 g đá vôi CaCO3 thu được bao nhiêu gam vôi sống CaO? (Ghi số thập phân)", "11,2", "n = 0,2 mol -> m_CaO = 0,2 * 56 = 11,2 g.")
    ],
    "part4": [
        make_vdc(1, "Cho 12 g hỗn hợp gồm Fe và Cu vào lượng dư dung dịch axit HCl, sau phản ứng thu được 2,479 lít khí H2 ở đkc. Khối lượng chất rắn không tan còn lại là:", ["6,4 g", "5,6 g", "3,2 g", "4,8 g"], 0, "n_H2 = 0,1 mol -> n_Fe = 0,1 mol -> m_Fe = 5,6 g -> m_Cu (không tan) = 12 - 5,6 = 6,4 g."),
        make_vdc(2, "Hòa tan hoàn toàn 8 g oxit kim loại RO vào 100 mL dung dịch H2SO4 1 M vừa đủ. Kim loại R là:", ["Đồng (Cu = 64)", "Kẽm (Zn = 65)", "Magiê (Mg = 24)", "Canxi (Ca = 40)"], 0, "n_H2SO4 = 0,1 mol -> M_RO = 8 / 0,1 = 80 -> M_R = 80 - 16 = 64 (Cu)."),
        make_vdc(3, "Hòa tan 14,8 g Ca(OH)2 vào nước được dung dịch A. Sục khí CO2 dư vào dung dịch A thu được dung dịch chứa muối Ca(HCO3)2. Khối lượng muối Ca(HCO3)2 tạo thành là:", ["32,4 g", "16,2 g", "20,0 g", "40,0 g"], 0, "n_Ca(OH)2 = 0,2 mol -> n_Ca(HCO3)2 = 0,2 mol -> m = 0,2 * 162 = 32,4 g."),
        make_vdc(4, "Một loại phân lân supephotphat đơn có chứa 71% Ca(H2PO4)2 nguyên chất (M = 234 g/mol). Độ dinh dưỡng của loại phân này tính theo %P2O5 là:", ["43,1%", "35,5%", "50,0%", "40,0%"], 0, "Ca(H2PO4)2 tương ứng P2O5: %P2O5 = 71% * (142 / 234) = 43,08% xấp xỉ 43,1%.")
    ]
}

print("Đã nạp xong Ôn tập cuối Chương II (5 đề độc lập 100%)")
