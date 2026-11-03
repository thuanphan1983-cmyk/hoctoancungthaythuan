# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - CHƯƠNG II: BÀI 11 (MUỐI), BÀI 12 (PHÂN BÓN HÓA HỌC) VÀ ÔN TẬP CUỐI CHƯƠNG II (11 ĐỀ ĐỘC LẬP 100%)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

exams_c2_p3 = {}

# ==============================================================================
# BÀI 11: MUỐI (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Định nghĩa muối, phân loại, tính tan của muối ---
exams_c2_p3["chem8_c2_b11_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Muối là hợp chất mà phân tử gồm có:", ["Nguyên tử kim loại (hoặc nhóm amoni NH4+) liên kết với một hay nhiều gốc axit", "Một hay nhiều nguyên tử H liên kết với gốc axit", "Kim loại liên kết với nhóm hiđroxit", "Hai nguyên tố trong đó có oxi"], 0, "Muối gồm kim loại (hoặc NH4+) liên kết với gốc axit."),
        make_mc(2, "Nhận biết", "Muối nào sau đây tan tốt trong nước?", ["NaCl (natri clorua)", "BaSO4 (bari sunfat)", "CaCO3 (canxi cacbonat)", "AgCl (bạc clorua)"], 0, "NaCl tan rất tốt trong nước."),
        make_mc(3, "Nhận biết", "Muối nào sau đây KHÔNG TAN (kết tủa trắng) trong nước?", ["BaSO4", "Na2SO4", "K2SO4", "MgSO4"], 0, "BaSO4 là kết tủa trắng không tan trong nước và axit."),
        make_mc(4, "Nhận biết", "Tất cả các muối của gốc axit nào sau đây đều tan tốt trong nước?", ["Gốc nitrat (-NO3)", "Gốc cacbonat (=CO3)", "Gốc sunfit (=SO3)", "Gốc photphat (≡PO4)"], 0, "Tất cả các muối nitrat (-NO3) đều tan trong nước."),
        make_mc(5, "Thông hiểu", "Cho dãy các muối: NaCl, BaSO4, KNO3, CaCO3, CuCl2, AgCl. Số muối tan tốt trong nước là:", ["3", "4", "2", "5"], 0, "Có 3 muối tan: NaCl, KNO3, CuCl2 (BaSO4, CaCO3, AgCl không tan)."),
        make_mc(6, "Thông hiểu", "Phản ứng giữa dung dịch bari clorua BaCl2 và dung dịch natri sunfat Na2SO4 sinh ra kết tủa trắng là:", ["BaSO4 (bari sunfat)", "NaCl", "BaCO3", "Na2SO3"], 0, "BaCl2 + Na2SO4 -> BaSO4 (trắng) + 2NaCl."),
        make_mc(7, "Thông hiểu", "Khi cho một đinh sắt sạch vào dung dịch đồng(II) sunfat CuSO4, sau một thời gian hiện tượng quan sát được là:", ["Có lớp kim loại màu đỏ bám trên đinh sắt và màu xanh của dung dịch nhạt dần", "Có bọt khí thoát ra dữ dội", "Đinh sắt bị tan biến thành chất lỏng", "Dung dịch chuyển sang màu tím đậm"], 0, "Fe + CuSO4 -> FeSO4 (xanh nhạt) + Cu (đỏ bám trên sắt)."),
        make_mc(8, "Thông hiểu", "Điều kiện để phản ứng trao đổi giữa hai dung dịch muối xảy ra là sản phẩm phải có:", ["Ít nhất một chất kết tủa hoặc chất khí", "Chất phản ứng phải là chất rắn", "Phải có nhiệt độ thật cao", "Cả hai sản phẩm đều phải tan"], 0, "Điều kiện phản ứng trao đổi trong dung dịch: tạo kết tủa, khí hoặc chất điện li yếu (nước)."),
        make_mc(9, "Vận dụng", "Hòa tan hoàn toàn 10 g đá vôi CaCO3 bằng dung dịch axit HCl dư. Thể tích khí CO2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:", ["2,479 lít", "4,958 lít", "2,24 lít", "1,2395 lít"], 0, "n_CaCO3 = 0,1 mol -> V_CO2 = 0,1 * 24,79 = 2,479 L."),
        make_mc(10, "Vận dụng", "Trộn 100 mL dung dịch AgNO3 0,1 M với 100 mL dung dịch NaCl 0,1 M. Khối lượng kết tủa AgCl thu được là:", ["1,435 g", "2,87 g", "0,7175 g", "1,08 g"], 0, "AgNO3 + NaCl -> AgCl + NaNO3. n = 0,01 mol -> m_AgCl = 0,01 * 143,5 = 1,435 g."),
        make_mc(11, "Vận dụng", "Cặp chất nào sau đây CÙNG TỒN TẠI trong một dung dịch mà không phản ứng với nhau?", ["NaCl và KNO3", "BaCl2 và Na2SO4", "AgNO3 và NaCl", "NaOH và FeCl3"], 0, "NaCl và KNO3 không tạo kết tủa hay khí nên cùng tồn tại trong dung dịch."),
        make_mc(12, "Vận dụng cao", "Cho 200 g dung dịch BaCl2 5,2% tác dụng vừa đủ với dung dịch H2SO4 loãng. Khối lượng kết tủa BaSO4 thu được là:", ["11,65 g", "23,3 g", "5,825 g", "10,4 g"], 0, "m_BaCl2 = 10,4 g -> n = 0,05 mol -> m_BaSO4 = 0,05 * 233 = 11,65 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về tính tan của các muối trong nước:", [
            ("a", "Hầu hết các muối natri (Na) và kali (K) đều tan tốt trong nước.", True),
            ("b", "Tất cả các muối nitrat (-NO3) đều tan trong nước.", True),
            ("c", "Muối clorua (-Cl) hầu hết tan tốt, trừ AgCl không tan.", True),
            ("d", "Tất cả các muối cacbonat (=CO3) đều tan tốt trong nước.", False)
        ], "Hầu hết muối cacbonat không tan, trừ muối của Na, K, NH4+."),
        make_tf(2, "Thông hiểu", "Về tính chất hóa học của muối:", [
            ("a", "Dung dịch muối tác dụng với kim loại đứng trước trong dãy hoạt động hóa học tạo muối mới và kim loại mới.", True),
            ("b", "Dung dịch muối tác dụng với axit tạo thành muối mới và axit mới.", True),
            ("c", "Dung dịch muối tác dụng với dung dịch kiềm tạo muối mới và bazơ mới.", True),
            ("d", "Hai dung dịch muối bất kì khi trộn lẫn với nhau luôn xảy ra phản ứng hóa học.", False)
        ], "Chỉ phản ứng nếu sản phẩm tạo thành có chất kết tủa."),
        make_tf(3, "Vận dụng", "Cho các phản ứng trao đổi trong dung dịch sau:", [
            ("a", "BaCl2 + Na2SO4 -> BaSO4 + 2NaCl.", True),
            ("b", "AgNO3 + NaCl -> AgCl + NaNO3.", True),
            ("c", "CuSO4 + 2NaOH -> Cu(OH)2 + Na2SO4.", True),
            ("d", "KNO3 + NaCl -> KCl + NaNO3.", False)
        ], "Không có kết tủa hay khí sinh ra nên phản ứng không xảy ra."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm ngâm thanh đồng (Cu) vào dung dịch bạc nitrat (AgNO3):", [
            ("a", "Phương trình: Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag.", True),
            ("b", "Dung dịch từ không màu chuyển dần sang màu xanh lam của muối đồng(II).", True),
            ("c", "Có kim loại bạc màu trắng xám bám ngoài thanh đồng.", True),
            ("d", "Sau phản ứng, khối lượng thanh đồng bị giảm đi.", False)
        ], "1 mol Cu (64g) tan ra tạo 2 mol Ag (216g) bám vào nên khối lượng thanh đồng tăng lên rõ rệt.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Muối ăn hàng ngày có công thức hóa học là gì? (Điền: NaCl)", "NaCl", "Natri clorua NaCl."),
        make_sa(2, "Thông hiểu", "Cho các muối: Na2SO4, BaSO4, AgCl, CaCO3. Có bao nhiêu muối kết tủa không tan trong nước?", "3", "BaSO4, AgCl, CaCO3 (3 muối không tan)."),
        make_sa(3, "Thông hiểu", "Phản ứng giữa dung dịch AgNO3 và dung dịch NaCl sinh ra chất kết tủa màu gì?", "trắng", "Kết tủa AgCl màu trắng."),
        make_sa(4, "Vận dụng", "Khối lượng mol của muối canxi cacbonat CaCO3 là bao nhiêu g/mol?", "100", "M = 40 + 12 + 16*3 = 100 g/mol."),
        make_sa(5, "Vận dụng", "Hòa tan hết 5,85 g NaCl vào nước để được 100 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M?", "1", "n = 0,1 mol -> CM = 0,1 / 0,1 = 1 M."),
        make_sa(6, "Vận dụng cao", "Nhiệt phân hoàn toàn 10 g đá vôi CaCO3 thu được bao nhiêu gam vôi sống CaO? (Ghi số thập phân)", "5,6", "n = 0,1 mol -> m_CaO = 0,1 * 56 = 5,6 g.")
    ],
    "part4": [
        make_vdc(1, "Ngâm một lá sắt có khối lượng 10 g vào 200 mL dung dịch CuSO4 0,5 M. Sau một thời gian lấy lá sắt ra, rửa nhẹ, sấy khô cân lại thấy nặng 10,8 g. Khối lượng kim loại đồng Cu đã bám lên lá sắt là:", ["6,4 g", "0,8 g", "3,2 g", "1,6 g"], 0, "m tăng = n * (64 - 56) = 8n = 0,8 g -> n = 0,1 mol -> m_Cu bám = 0,1 * 64 = 6,4 g."),
        make_vdc(2, "Cho dung dịch chứa 0,2 mol BaCl2 tác dụng với dung dịch chứa 0,15 mol Na2SO4. Khối lượng kết tủa BaSO4 thu được là:", ["34,95 g", "46,6 g", "23,3 g", "11,65 g"], 0, "Tính theo Na2SO4 thiếu: n_BaSO4 = 0,15 mol -> m = 0,15 * 233 = 34,95 g."),
        make_vdc(3, "Trộn lẫn 100 mL dung dịch CaCl2 1 M với 100 mL dung dịch Na2CO3 1 M thu được m gam kết tủa trắng. Giá trị của m là:", ["10,0 g", "5,0 g", "20,0 g", "7,5 g"], 0, "CaCl2 + Na2CO3 -> CaCO3 + 2NaCl. n = 0,1 mol -> m = 0,1 * 100 = 10,0 g."),
        make_vdc(4, "Một dung dịch chứa hỗn hợp hai muối FeSO4 và CuSO4. Để tách hoàn toàn ion Cu2+ ra khỏi dung dịch mà không đưa thêm ion kim loại lạ vào dung dịch, người ta cho vào một lượng dư kim loại nào?", ["Kim loại bột sắt Fe", "Kim loại kẽm Zn", "Kim loại nhôm Al", "Kim loại magie Mg"], 0, "Fe đẩy Cu ra khỏi muối (Fe + CuSO4 -> FeSO4 + Cu), tạo thêm FeSO4 trùng với chất có sẵn.")
    ]
}

# --- BÀI 12: PHÂN BÓN HÓA HỌC (3 ĐỀ) ---
# --- ĐỀ 1: Các loại phân bón đơn: đạm, lân, kali, phân hỗn hợp NPK ---
exams_c2_p3["chem8_c2_b12_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Phân bón hóa học là những hóa chất chứa các nguyên tố dinh dưỡng được bón cho cây trồng nhằm:", ["Tăng năng suất và chất lượng cây trồng", "Diệt sâu bọ hại cây", "Làm đông cứng đất trồng", "Tăng nhiệt độ của đất"], 0, "Cung cấp dinh dưỡng cho cây phát triển khỏe mạnh, tăng năng suất."),
        make_mc(2, "Nhận biết", "Nguyên tố dinh dưỡng nào sau đây có trong phân đạm?", ["Nitơ (N)", "Photpho (P)", "Kali (K)", "Canxi (Ca)"], 0, "Phân đạm cung cấp nguyên tố dinh dưỡng nitơ (N)."),
        make_mc(3, "Nhận biết", "Nguyên tố dinh dưỡng nào sau đây có trong phân lân?", ["Photpho (P)", "Nitơ (N)", "Kali (K)", "Lưu huỳnh (S)"], 0, "Phân lân cung cấp photpho (P)."),
        make_mc(4, "Nhận biết", "Nguyên tố dinh dưỡng nào sau đây có trong phân kali?", ["Kali (K)", "Nitơ (N)", "Photpho (P)", "Magie (Mg)"], 0, "Phân kali cung cấp kali (K)."),
        make_mc(5, "Thông hiểu", "Phân đạm urê có công thức hóa học là:", ["(NH2)2CO", "NH4NO3", "(NH4)2SO4", "KNO3"], 0, "Urê là (NH2)2CO chứa hàm lượng nitơ cao nhất (khoảng 46%)."),
        make_mc(6, "Thông hiểu", "Phân đạm có tác dụng chủ yếu kích thích:", ["Sự sinh trưởng của lá, thân và cành cây phát triển xanh tốt", "Sự phát triển của bộ rễ và củ", "Quả ngọt và hạt chắc, tăng chịu rét", "Hoa nở nhiều màu sắc"], 0, "Đạm kích thích lá, cành, sinh khối phát triển."),
        make_mc(7, "Thông hiểu", "Phân lân có tác dụng chủ yếu kích thích:", ["Sự phát triển của bộ rễ, sự tạo củ và ra hoa kết quả", "Sự lớn nhanh của cành lá", "Tăng khả năng chống rét chịu hạn", "Tạo chất diệp lục"], 0, "Lân kích thích cành, rễ, củ và mầm hoa."),
        make_mc(8, "Thông hiểu", "Phân kali có tác dụng chủ yếu giúp cây trồng:", ["Tăng khả năng chống chịu sâu bệnh, rét, hạn và làm quả ngọt, hạt chắc", "Tốt lá tốt cành", "Tăng độ chua của đất", "Kích thích rễ dài ra"], 0, "Kali tăng sức đề kháng, vận chuyển đường bột làm chắc hạt, ngọt quả."),
        make_mc(9, "Vận dụng", "Trên bao bì một loại phân bón NPK có ghi chỉ số 16-16-8. Các con số này cho biết tỉ lệ phần trăm tương ứng của:", ["N, P2O5 và K2O", "N, P và K", "NO3, PO4 và K", "Đạm, lân và vi lượng"], 0, "Quy ước quốc tế: %N, %P2O5, %K2O."),
        make_mc(10, "Vận dụng", "Loại phân đạm nào sau đây có hàm lượng phần trăm nitơ cao nhất?", ["Urê (NH2)2CO (khoảng 46%)", "Amoni nitrat NH4NO3 (khoảng 35%)", "Amoni sunfat (NH4)2SO4 (khoảng 21%)", "Natri nitrat NaNO3 (khoảng 16%)"], 0, "Urê có %N = 28 / 60 = 46,67% cao nhất."),
        make_mc(11, "Vận dụng", "Tại sao không nên bón phân đạm amoni ((NH4)2SO4 hoặc NH4NO3) cùng lúc với vôi tôi Ca(OH)2?", ["Vì vôi tác dụng với muối amoni giải phóng khí amoniac (NH3) bay mất làm thất thoát chất đạm", "Vì làm đất bị lạnh đóng băng", "Vì tạo ra chất nổ", "Vì làm chết cây ngay lập tức do thiếu nước"], 0, "2NH4+ + Ca(OH)2 -> Ca2+ + 2NH3 bay hơi + 2H2O làm mất đạm."),
        make_mc(12, "Vận dụng cao", "Một người nông dân cần bón 28 kg nitơ cho một thửa ruộng. Khối lượng phân đạm urê (chứa 90% (NH2)2CO nguyên chất, còn lại tạp chất) cần dùng là:", ["66,7 kg", "60,0 kg", "75,0 kg", "50,0 kg"], 0, "m_urê nguyên chất = 28 / (28/60) = 60 kg -> m_phân bón = 60 / 90% = 66,7 kg."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về vai trò của ba nguyên tố dinh dưỡng đa lượng N, P, K:", [
            ("a", "Nitơ (N) là thành phần cấu tạo nên protein và diệp lục trong cây.", True),
            ("b", "Photpho (P) thúc đẩy sự phát triển của hệ rễ và quá trình chín của hạt, quả.", True),
            ("c", "Kali (K) giúp cây tăng khả năng chống chịu thời tiết khắc nghiệt và sâu bệnh.", True),
            ("d", "Cây trồng chỉ cần duy nhất phân đạm là có thể phát triển hoàn hảo mà không cần P và K.", False)
        ], "Cây cần cân đối cả 3 yếu tố N, P, K và các nguyên tố vi lượng."),
        make_tf(2, "Thông hiểu", "Về các loại phân bón hóa học thông dụng:", [
            ("a", "Phân đơn là phân chỉ chứa 1 trong 3 nguyên tố dinh dưỡng chính (N, P hoặc K).", True),
            ("b", "Phân đạm urê (NH2)2CO tan rất tốt trong nước và dễ hút ẩm.", True),
            ("c", "Phân lân supephotphat có thành phần chính là Ca(H2PO4)2 tan trong nước.", True),
            ("d", "Phân kali thường dùng là muối kali clorua (KCl) hoặc kali sunfat (K2SO4).", True)
        ], "Các nhận định a, b, c, d đều đúng."),
        make_tf(3, "Vận dụng", "Về phân bón hỗn hợp và phân vi lượng:", [
            ("a", "Phân NPK là phân bón hỗn hợp chứa cả 3 nguyên tố dinh dưỡng N, P, K.", True),
            ("b", "Phân vi lượng chứa các nguyên tố như Bo, Kẽm, Đồng, Sắt, Mangan với lượng rất nhỏ nhưng không thể thiếu.", True),
            ("c", "Bón càng nhiều phân bón hóa học càng tốt cho đất và nguồn nước ngầm.", False),
            ("d", "Bón thừa phân đạm làm cây yếu, dễ lốp đổ và tích lũy nitrat độc hại trong rau củ.", True)
        ], "Bón thừa phân gây ô nhiễm nguồn nước và thoái hóa đất."),
        make_tf(4, "Vận dụng cao", "Về nguyên tắc bón phân khoa học (nguyên tắc 4 đúng):", [
            ("a", "Bón đúng loại phân phù hợp với nhu cầu từng thời kì sinh trưởng của cây.", True),
            ("b", "Bón đúng liều lượng chỉ dẫn, tránh dư thừa gây lãng phí và ô nhiễm.", True),
            ("c", "Bón đúng thời điểm (đúng lúc) và đúng phương pháp (cách bón).", True),
            ("d", "Bón phân vào buổi trưa nắng gắt hoặc ngay trước cơn mưa rào lớn là phương pháp tốt nhất.", False)
        ], "Bón lúc nắng gắt làm phân bay hơi; mưa to làm phân bị rửa trôi gây ô nhiễm.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Kí hiệu hóa học của nguyên tố kali là chữ gì?", "K", "Kí hiệu là K."),
        make_sa(2, "Thông hiểu", "Phân đạm cung cấp cho cây trồng nguyên tố dinh dưỡng nào? (Điền: nitơ)", "nitơ", "Cung cấp nguyên tố nitơ (N)."),
        make_sa(3, "Thông hiểu", "Phân bón NPK chứa bao nhiêu nguyên tố dinh dưỡng đa lượng chính?", "3", "Chứa 3 nguyên tố: N, P, K."),
        make_sa(4, "Vận dụng", "Hàm lượng phần trăm nitơ (%N) trong phân đạm amoni nitrat NH4NO3 (M = 80 g/mol) là bao nhiêu %?", "35", "%N = (28 / 80) * 100% = 35%."),
        make_sa(5, "Vận dụng", "Khối lượng mol của urê (NH2)2CO là bao nhiêu g/mol?", "60", "M = (14+2)*2 + 12 + 16 = 60 g/mol."),
        make_sa(6, "Vận dụng cao", "Một bao phân NPK có ghi 20-20-15. Phần trăm của nguyên tố P2O5 trong phân bón này là bao nhiêu %?", "20", "Con số thứ hai là %P2O5 = 20%.")
    ],
    "part4": [
        make_vdc(1, "Hàm lượng phần trăm dinh dưỡng (%N) của phân đạm urê tinh khiết (NH2)2CO xấp xỉ bằng:", ["46,7%", "35,0%", "21,2%", "40,0%"], 0, "%N = (28 / 60) * 100% = 46,67% xấp xỉ 46,7%."),
        make_vdc(2, "Một loại phân kali chứa 95% KCl nguyên chất, còn lại là tạp chất trơ không chứa kali. Độ dinh dưỡng của loại phân này tính theo %K2O là: (Biết 2KCl tương ứng K2O: 149 g KCl ứng với 94 g K2O)", ["60,0%", "50,0%", "63,1%", "55,0%"], 0, "%K2O = 95% * (94 / 149) = 59,93% xấp xỉ 60,0%."),
        make_vdc(3, "Biện pháp nào sau đây thể hiện việc sử dụng phân bón hóa học an toàn, thân thiện với môi trường?", ["Kết hợp bón phân hữu cơ ủ hoai mục với phân vô cơ hợp lí theo nhu cầu của cây trồng", "Bón thật nhiều phân đạm để rau xanh mướt quanh năm", "Bón phân đạm hòa vào nguồn nước tưới xả tràn ra sông suối", "Bón phân vô cơ liên tục không cần cải tạo đất"], 0, "Kết hợp phân hữu cơ và vô cơ cân đối giúp đất màu mỡ và bền vững."),
        make_vdc(4, "Bón phân nào sau đây cho đất chua lâu ngày sẽ làm tăng độ chua của đất nếu không bón kèm vôi khử chua?", ["Phân đạm amoni sunfat (NH4)2SO4", "Phân lân nung chảy (có tính kiềm nhẹ)", "Vôi tôi Ca(OH)2", "Tro bếp (chứa K2CO3)"], 0, "Muối amoni của axit mạnh làm tăng tính axit (độ chua) của đất.")
    ]
}

print("Đã nạp xong Bài 11 và Bài 12 (độc lập 100%)")
