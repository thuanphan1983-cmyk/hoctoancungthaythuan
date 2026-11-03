# -*- coding: utf-8 -*-
"""
HÓA HỌC 7 - TIẾP TỤC HOÀN THIỆN BÀI 6, BÀI 7 & ÔN TẬP CHƯƠNG II (11 ĐỀ ĐỘC LẬP)
- chem7_c2_b6: Bài 6: Giới thiệu về liên kết hóa học (3 đề)
- chem7_c2_b7: Bài 7: Hóa trị và công thức hóa học (3 đề)
- chem7_c2_rev: Ôn tập Chương II (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from builder_chem7_c2_complete import exams, make_mc, make_tf, make_sa, make_vdc

# ==============================================================================
# BÀI 6: GIỚI THIỆU VỀ LIÊN KẾT HÓA HỌC (3 ĐỀ ĐỘC LẬP)
# ==============================================================================

# --- ĐỀ 1: Quy tắc octet, liên kết ion, sự tạo thành phân tử NaCl, MgO ---
exams["chem7_c2_b6_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Theo quy tắc octet, nguyên tử của các nguyên tố có xu hướng đạt cấu hình electron bền vững ở lớp ngoài cùng gồm:", ["8 electron (hoặc 2 electron đối với helium)", "2 electron cho mọi nguyên tử", "18 electron", "32 electron"], 0, "Quy tắc octet: 8 electron lớp ngoài cùng (riêng He là 2e)."),
        make_mc(2, "Nhận biết", "Liên kết ion là liên kết được hình thành bởi:", ["Lực hút tĩnh điện giữa các ion mang điện tích trái dấu", "Các cặp electron dùng chung", "Lực hút giữa các hạt proton", "Lực tương tác từ"], 0, "Liên kết ion hình thành do lực hút tĩnh điện giữa cation (ion dương) và anion (ion âm)."),
        make_mc(3, "Nhận biết", "Khi nguyên tử kim loại nhường electron, nó biến thành hạt mang điện tích gì?", ["Ion dương (cation)", "Ion âm (anion)", "Phân tử trung hòa", "Hạt neutron"], 0, "Nhường electron mang điện âm sẽ trở thành ion dương."),
        make_mc(4, "Nhận biết", "Khi nguyên tử Sodium (Na) nhường đi 1 electron ở lớp ngoài cùng, nó tạo thành ion nào?", ["Na+", "Na2+", "Na-", "Na2-"], 0, "Na nhường 1e thành Na+."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là hợp chất ion?", ["Sodium chloride (NaCl)", "Khí hydrogen (H2)", "Nước (H2O)", "Khí carbon dioxide (CO2)"], 0, "NaCl là hợp chất ion điển hình giữa kim loại Na và phi kim Cl."),
        make_mc(6, "Nhận biết", "Liên kết cộng hóa trị là liên kết được hình thành giữa hai nguyên tử bằng:", ["Một hay nhiều cặp electron dùng chung", "Lực hút tĩnh điện giữa các ion", "Sự nhường và nhận electron hoàn toàn", "Lực tương tác hấp dẫn"], 0, "Liên kết cộng hóa trị hình thành bằng các cặp electron dùng chung."),
        make_mc(7, "Thông hiểu", "Nguyên tử Chlorine (7e ngoài cùng) đạt cấu hình bền vững của khí hiếm bằng cách:", ["Nhận thêm 1 electron", "Nhường đi 7 electron", "Nhường đi 1 electron", "Nhận thêm 2 electron"], 0, "Cl có 7e ngoài cùng, nhận thêm 1e để đạt 8e bền vững giống Ar."),
        make_mc(8, "Thông hiểu", "Khi tạo thành phân tử Magnesium oxide (MgO), nguyên tử Mg đã:", ["Nhường 2 electron cho nguyên tử O", "Nhận 2 electron từ nguyên tử O", "Góp chung 2 electron với nguyên tử O", "Nhường 1 electron cho nguyên tử O"], 0, "Mg nhường 2e thành Mg2+, O nhận 2e thành O2-."),
        make_mc(9, "Thông hiểu", "Hợp chất ion thường có đặc điểm vật lí nào sau đây?", ["Nhiệt độ nóng chảy và nhiệt độ sôi cao", "Ở thể khí ở nhiệt độ phòng", "Nhiệt độ nóng chảy rất thấp", "Không tan trong nước"], 0, "Liên kết ion bền vững nên hợp chất ion có nhiệt độ nóng chảy và sôi rất cao."),
        make_mc(10, "Thông hiểu", "Dung dịch chất nào sau đây có khả năng dẫn điện tốt?", ["Dung dịch nước muối (NaCl)", "Dung dịch nước đường (sucrose)", "Cồn tinh khiết", "Nước cất"], 0, "NaCl tan trong nước phân li thành các ion Na+ và Cl- tự do dẫn điện."),
        make_mc(11, "Thông hiểu", "Trong phân tử khí hydrogen (H2), hai nguyên tử H liên kết với nhau bằng:", ["1 cặp electron dùng chung", "2 cặp electron dùng chung", "Lực hút ion", "Lực đẩy tĩnh điện"], 0, "Mỗi nguyên tử H góp 1e tạo thành 1 cặp e dùng chung."),
        make_mc(12, "Thông hiểu", "Chất nào sau đây có nhiệt độ nóng chảy cao nhất?", ["Muối ăn (NaCl, khoảng 801°C)", "Đường ăn (nóng chảy khoảng 186°C)", "Nước đá (0°C)", "Cồn (nóng chảy ở -114°C)"], 0, "Hợp chất ion NaCl có nhiệt độ nóng chảy cao vượt trội.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét sự hình thành liên kết trong phân tử Sodium chloride (NaCl):", [
            ("a", "Nguyên tử Sodium nhường 1 electron tạo thành ion dương Na+.", True),
            ("b", "Nguyên tử Chlorine nhận 1 electron tạo thành ion âm Cl-.", True),
            ("c", "Ion Na+ và Cl- hút nhau bằng lực hút tĩnh điện tạo nên tinh thể NaCl.", True),
            ("d", "Trong phân tử NaCl có 1 cặp electron dùng chung giữa Na và Cl.", False)
        ], "NaCl là liên kết ion do lực hút tĩnh điện, không phải góp chung electron."),
        make_tf(2, "Thông hiểu", "Xét tính chất chung của các hợp chất ion:", [
            ("a", "Hầu hết là chất rắn ở nhiệt độ phòng.", True),
            ("b", "Có nhiệt độ nóng chảy và nhiệt độ sôi cao.", True),
            ("c", "Khi tan trong nước hoặc nóng chảy thì dẫn điện được.", True),
            ("d", "Dễ bay hơi và có mùi thơm nồng.", False)
        ], "Hợp chất ion rất khó bay hơi do lực liên kết ion mạnh."),
        make_tf(3, "Vận dụng", "Cho các chất: KCl, CaO, H2O, CH4:", [
            ("a", "KCl và CaO là các hợp chất ion.", True),
            ("b", "H2O và CH4 là các hợp chất cộng hóa trị.", True),
            ("c", "KCl được tạo nên từ kim loại điển hình (K) và phi kim điển hình (Cl).", True),
            ("d", "Tất cả các chất này đều dẫn điện tốt ở thể rắn.", False)
        ], "Ở thể rắn các ion bị giữ chặt trong mạng tinh thể nên không dẫn điện."),
        make_tf(4, "Vận dụng", "Xét quá trình nguyên tử Magnesium (Z = 12) liên kết với Oxygen (Z = 8):", [
            ("a", "Mg có 2e ngoài cùng, có xu hướng nhường 2e tạo Mg2+.", True),
            ("b", "O có 6e ngoài cùng, có xu hướng nhận 2e tạo O2-.", True),
            ("c", "Sau khi tạo ion, cả Mg2+ và O2- đều có 8 electron ở lớp ngoài cùng giống khí hiếm Neon.", True),
            ("d", "Hợp chất tạo thành là Mg2O.", False)
        ], "Hợp chất tạo thành là MgO tỉ lệ 1 : 1.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Số electron tối đa ở lớp ngoài cùng của nguyên tử khí hiếm Neon là bao nhiêu?", "8", "Neon có 8 electron ngoài cùng."),
        make_sa(2, "Thông hiểu", "Điện tích của ion tạo thành khi nguyên tử Calcium nhường 2 electron là bao nhiêu? (Ghi dấu và số)", "+2", "Ca nhường 2e tạo ion Ca2+ mang điện tích +2."),
        make_sa(3, "Vận dụng", "Trong phân tử khí nitrogen (N2), hai nguyên tử N liên kết với nhau bằng bao nhiêu cặp electron dùng chung?", "3", "N2 có liên kết ba (3 cặp electron dùng chung)."),
        make_sa(4, "Vận dụng", "Một ion X- có 10 electron. Số proton trong hạt nhân của nguyên tử X là bao nhiêu?", "9", "X nhận 1e thành X- có 10e => ban đầu X có 9 proton (Fluorine)."),
        make_sa(5, "Vận dụng cao", "Trong phân tử nước (H2O), nguyên tử Oxygen đã góp chung bao nhiêu electron với 2 nguyên tử Hydrogen?", "2", "O góp 2 electron (mỗi liên kết O-H dùng 1 electron của O)."),
        make_sa(6, "Vận dụng cao", "Phân tử carbon dioxide (CO2) có tổng cộng bao nhiêu cặp electron dùng chung giữa C và 2 nguyên tử O?", "4", "CO2 có 2 liên kết đôi O=C=O => tổng cộng 4 cặp e dùng chung.")
    ],
    "part4": [
        make_vdc(1, "Nguyên tử nguyên tố X có 1 electron lớp ngoài cùng, nguyên tử nguyên tố Y có 7 electron lớp ngoài cùng. Liên kết giữa X và Y thuộc loại:", ["Liên kết ion", "Liên kết cộng hóa trị phân cực", "Liên kết cộng hóa trị không phân cực", "Liên kết kim loại"], 0, "Kim loại điển hình (1e ngoài cùng) nhường e cho phi kim điển hình (7e ngoài cùng) tạo liên kết ion."),
        make_vdc(2, "Chất nào sau đây ở điều kiện thường tồn tại ở thể khí và có liên kết cộng hóa trị?", ["Methane (CH4)", "Sodium chloride (NaCl)", "Magnesium oxide (MgO)", "Calcium chloride (CaCl2)"], 0, "CH4 là hợp chất cộng hóa trị ở thể khí."),
        make_vdc(3, "Nguyên tố A (Z = 19) kết hợp với nguyên tố B (Z = 16) tạo thành hợp chất có công thức hóa học là:", ["A2B", "AB", "AB2", "A2B3"], 0, "A là K (hóa trị I, tạo K+), B là S (hóa trị II, tạo S2-) => công thức K2S (A2B)."),
        make_vdc(4, "Giải thích vì sao dung dịch đường mía không dẫn điện trong khi dung dịch muối ăn lại dẫn điện tốt?", ["Đường là chất cộng hóa trị không phân li thành ion, muối ăn là chất ion phân li thành các ion tự do", "Đường không tan trong nước", "Muối ăn chứa kim loại tự do", "Đường có khối lượng phân tử lớn hơn"], 0, "Hợp chất ion phân li thành ion mang điện tự do chuyển động trong dung dịch.")
    ]
}

# --- ĐỀ 2: Liên kết cộng hóa trị, cặp electron dùng chung trong H2, Cl2, O2, N2, H2O, NH3, CO2 ---
exams["chem7_c2_b6_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Liên kết cộng hóa trị thường được hình thành giữa:", ["Các nguyên tử phi kim với nhau", "Kim loại điển hình với phi kim điển hình", "Hai nguyên tử kim loại", "Khí hiếm với phi kim"], 0, "Liên kết cộng hóa trị thường tạo nên giữa các nguyên tử phi kim."),
        make_mc(2, "Nhận biết", "Trong phân tử khí oxygen (O2), hai nguyên tử O liên kết với nhau bằng:", ["Hai cặp electron dùng chung (liên kết đôi)", "Một cặp electron dùng chung", "Ba cặp electron dùng chung", "Lực hút ion"], 0, "O2 có liên kết đôi (2 cặp electron dùng chung O=O)."),
        make_mc(3, "Nhận biết", "Phân tử nào sau đây có liên kết ba giữa hai nguyên tử?", ["Nitrogen (N2)", "Oxygen (O2)", "Hydrogen (H2)", "Chlorine (Cl2)"], 0, "N2 có liên kết ba N≡N rất bền vững."),
        make_mc(4, "Nhận biết", "Hợp chất cộng hóa trị có đặc điểm nào sau đây?", ["Nhiệt độ nóng chảy và nhiệt độ sôi thường thấp hơn hợp chất ion", "Đều dẫn điện tốt ở trạng thái rắn", "Chỉ tồn tại ở thể rắn", "Không bao giờ tan trong nước"], 0, "Hợp chất cộng hóa trị có nhiệt độ nóng chảy và sôi tương đối thấp."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là chất lỏng ở điều kiện thường có liên kết cộng hóa trị?", ["Nước (H2O)", "Sodium chloride (NaCl)", "Magnesium oxide (MgO)", "Đồng (Cu)"], 0, "Nước là chất lỏng cấu tạo bởi các phân tử H2O liên kết cộng hóa trị."),
        make_mc(6, "Nhận biết", "Số electron dùng chung trong một liên kết đơn là:", ["2 electron (1 cặp electron)", "1 electron", "4 electron", "6 electron"], 0, "Liên kết đơn gồm 1 cặp electron dùng chung (2e)."),
        make_mc(7, "Thông hiểu", "Phân tử ammonia (NH3) có bao nhiêu liên kết đơn cộng hóa trị?", ["3 liên kết đơn N - H", "1 liên kết ba", "2 liên kết đôi", "4 liên kết đơn"], 0, "Nguyên tử N liên kết với 3 nguyên tử H bằng 3 liên kết đơn."),
        make_mc(8, "Thông hiểu", "Vì sao khí nitrogen (N2) trơ về mặt hóa học ở nhiệt độ phòng?", ["Do có liên kết ba N≡N rất bền vững giữa 2 nguyên tử N", "Do nitrogen là một khí hiếm", "Do phân tử N2 không có electron", "Do nitrogen ở thể khí"], 0, "Liên kết ba N≡N có năng lượng liên kết rất lớn nên rất bền vững."),
        make_mc(9, "Thông hiểu", "Hợp chất nào sau đây có liên kết ion?", ["Potassium chloride (KCl)", "Khí methane (CH4)", "Khí carbon dioxide (CO2)", "Nước (H2O)"], 0, "KCl tạo bởi kim loại K và phi kim Cl là hợp chất ion."),
        make_mc(10, "Thông hiểu", "Chất nào sau đây dễ bay hơi và có nhiệt độ sôi thấp?", ["Cồn ethanol", "Muối ăn", "Vôi sống (CaO)", "Đá vôi (CaCO3)"], 0, "Cồn ethanol là hợp chất cộng hóa trị dễ bay hơi, sôi ở 78,3°C."),
        make_mc(11, "Thông hiểu", "Khi hòa tan đường ăn vào nước, dung dịch thu được:", ["Không dẫn điện vì phân tử đường không phân li thành ion", "Dẫn điện tốt như nước muối", "Làm quỳ tím hóa đỏ", "Tạo kết tủa trắng"], 0, "Đường là chất cộng hóa trị, dung dịch đường không dẫn điện."),
        make_mc(12, "Thông hiểu", "Trong phân tử hydrogen chloride (HCl), cặp electron dùng chung bị lệch về phía:", ["Nguyên tử Chlorine vì Cl có khả năng hút electron mạnh hơn", "Nguyên tử Hydrogen", "Chính giữa hai nguyên tử", "Không bị lệch"], 0, "Cl có độ âm điện lớn hơn nên hút cặp electron lệch về phía mình.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét phân tử nước (H2O):", [
            ("a", "Được tạo thành bởi liên kết cộng hóa trị giữa 1 nguyên tử O và 2 nguyên tử H.", True),
            ("b", "Mỗi nguyên tử H góp chung 1 electron với nguyên tử O.", True),
            ("c", "Nguyên tử O đạt cấu hình bền vững 8 electron ở lớp ngoài cùng.", True),
            ("d", "Phân tử nước có liên kết ion do lực hút tĩnh điện.", False)
        ], "Nước là hợp chất cộng hóa trị."),
        make_tf(2, "Thông hiểu", "So sánh liên kết ion và liên kết cộng hóa trị:", [
            ("a", "Liên kết ion hình thành do lực hút tĩnh điện giữa các ion trái dấu.", True),
            ("b", "Liên kết cộng hóa trị hình thành do các cặp electron dùng chung.", True),
            ("c", "Hợp chất ion thường có nhiệt độ nóng chảy cao hơn hợp chất cộng hóa trị.", True),
            ("d", "Tất cả các hợp chất cộng hóa trị đều dẫn điện tốt khi tan trong nước.", False)
        ], "Hầu hết hợp chất cộng hóa trị (như đường, cồn...) không dẫn điện khi tan trong nước."),
        make_tf(3, "Vận dụng", "Cho các phân tử: Cl2, O2, N2, CO2:", [
            ("a", "Cl2 có 1 cặp electron dùng chung (liên kết đơn).", True),
            ("b", "O2 có 2 cặp electron dùng chung (liên kết đôi).", True),
            ("c", "N2 có 3 cặp electron dùng chung (liên kết ba).", True),
            ("d", "CO2 chỉ có các liên kết ion.", False)
        ], "CO2 có 2 liên kết đôi cộng hóa trị O=C=O."),
        make_tf(4, "Vận dụng", "Một hợp chất Z được tạo bởi nguyên tố kim loại X (Z = 20) và nguyên tố phi kim Y (Z = 17):", [
            ("a", "X là Calcium, Y là Chlorine.", True),
            ("b", "X nhường 2e tạo Ca2+, mỗi nguyên tử Y nhận 1e tạo Cl-.", True),
            ("c", "Hợp chất Z là CaCl2 có liên kết ion.", True),
            ("d", "Ở điều kiện thường, Z là chất khí dễ cháy.", False)
        ], "CaCl2 là chất rắn màu trắng, khó nóng chảy.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Trong phân tử khí chlorine (Cl2), có bao nhiêu cặp electron dùng chung giữa hai nguyên tử Cl?", "1", "Cl2 có 1 cặp electron dùng chung."),
        make_sa(2, "Thông hiểu", "Nguyên tử Carbon cần góp chung bao nhiêu electron để đạt cấu hình octet bền vững?", "4", "C có 4e ngoài cùng, cần góp chung 4 electron."),
        make_sa(3, "Vận dụng", "Trong phân tử methane (CH4), có tổng cộng bao nhiêu liên kết đơn C - H?", "4", "Có 4 liên kết đơn C - H."),
        make_sa(4, "Vận dụng", "Một ion nhôm Al3+ có bao nhiêu electron ở lớp vỏ?", "10", "Al có 13e, nhường 3e còn 10e."),
        make_sa(5, "Vận dụng cao", "Trong phân tử ammonia (NH3), có bao nhiêu electron ở lớp ngoài cùng của nguyên tử Nitrogen KHÔNG tham gia liên kết (electron tự do)?", "2", "N có 5e ngoài cùng, dùng 3e liên kết với 3H, còn lại 2 electron tự do (1 cặp e)."),
        make_sa(6, "Vận dụng cao", "Một hợp chất có phân tử gồm nguyên tố X liên kết ion với ion Cl- tạo hợp chất XCl2. Biết khối lượng phân tử hợp chất là 111 amu. Tên nguyên tố X là gì?", "Calcium", "X + 2 × 35,5 = 111 => X = 40 (Calcium).")
    ],
    "part4": [
        make_vdc(1, "Nguyên tử X có 6 electron ở lớp ngoài cùng, nguyên tử Hydrogen có 1 electron. Công thức hợp chất cộng hóa trị tạo bởi X và H là:", ["H2X", "HX", "HX2", "H3X"], 0, "X có 6e ngoài cùng cần thêm 2e => liên kết với 2 nguyên tử H tạo H2X (như H2O, H2S)."),
        make_vdc(2, "Cho biết sơ đồ tạo thành liên kết trong phân tử CO2: nguyên tử C góp chung 4 electron với 2 nguyên tử O. Loại liên kết giữa C và O trong phân tử CO2 là:", ["Liên kết cộng hóa trị gồm 2 liên kết đôi", "Liên kết ion", "Liên kết ba", "Liên kết kim loại"], 0, "CO2 có cấu trúc O=C=O gồm hai liên kết đôi cộng hóa trị."),
        make_vdc(3, "Chất nào sau đây khi hòa tan vào nước tạo thành dung dịch KHÔNG dẫn điện?", ["Đường glucose (C6H12O6)", "Muối ăn (NaCl)", "Calcium chloride (CaCl2)", "Sodium hydroxide (NaOH)"], 0, "Glucose là hợp chất cộng hóa trị không phân li thành ion trong nước."),
        make_vdc(4, "Phân tử chất nào sau đây có tổng số electron tham gia liên kết là 6 hạt (3 cặp electron)?", ["Nitrogen (N2)", "Oxygen (O2)", "Chlorine (Cl2)", "Carbon dioxide (CO2)"], 0, "N2 có liên kết ba gồm 3 cặp e (6 hạt electron).")
    ]
}

# --- ĐỀ 3: So sánh tính chất các loại hợp chất, ứng dụng thực tế của liên kết hóa học ---
exams["chem7_c2_b6_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Hạt mang điện tích dương tạo thành khi nguyên tử kim loại nhường electron được gọi là:", ["Cation (ion dương)", "Anion (ion âm)", "Proton tự do", "Phân tử"], 0, "Ion dương được gọi là Cation."),
        make_mc(2, "Nhận biết", "Hạt mang điện tích âm tạo thành khi nguyên tử phi kim nhận electron được gọi là:", ["Anion (ion âm)", "Cation (ion dương)", "Electron tự do", "Hạt nhân"], 0, "Ion âm được gọi là Anion."),
        make_mc(3, "Nhận biết", "Trong tinh thể muối ăn (NaCl), các ion Na+ và Cl- được sắp xếp:", ["Trật tự và luân phiên nhau trong không gian 3 chiều tạo mạng tinh thể", "Lộn xộn không theo quy luật", "Thành từng cặp phân tử riêng biệt tách rời", "Tập trung Na+ ở giữa và Cl- ở ngoài"], 0, "Mạng tinh thể ion lập phương sắp xếp luân phiên trật tự."),
        make_mc(4, "Nhận biết", "Chất nào sau đây tồn tại ở dạng mạng tinh thể ion ở điều kiện thường?", ["Calcium oxide (vôi sống CaO)", "Nước", "Khí nitrogen", "Cồn ethanol"], 0, "CaO là hợp chất ion thể rắn tinh thể."),
        make_mc(5, "Nhận biết", "Liên kết trong phân tử nước (H2O) là:", ["Liên kết cộng hóa trị", "Liên kết ion", "Liên kết kim loại", "Liên kết hidro"], 0, "H2O là hợp chất cộng hóa trị giữa 2 phi kim H và O."),
        make_mc(6, "Nhận biết", "Số electron mà nguyên tử phi kim Oxygen cần nhận thêm để đạt cấu hình octet là:", ["2 electron", "1 electron", "3 electron", "4 electron"], 0, "O có 6e ngoài cùng, nhận thêm 2e để thành 8e (O2-)."),
        make_mc(7, "Thông hiểu", "Chất nào sau đây vừa có nhiệt độ nóng chảy cao vừa dễ tan trong nước tạo dung dịch dẫn điện?", ["Sodium chloride (NaCl)", "Sáp nến (parafin)", "Đường saccarozơ", "Dầu ăn"], 0, "Đặc tính điển hình của hợp chất ion NaCl."),
        make_mc(8, "Thông hiểu", "Vì sao các hợp chất cộng hóa trị như cồn, xăng, dầu lại dễ bay hơi và dễ cháy?", ["Vì lực liên kết giữa các phân tử tương đối yếu", "Vì khối lượng nguyên tử rất lớn", "Vì chúng chứa kim loại", "Vì chúng có liên kết ion"], 0, "Lực hút giữa các phân tử cộng hóa trị yếu nên dễ bay hơi."),
        make_mc(9, "Thông hiểu", "Ion nào sau đây có cấu hình electron bền vững giống khí hiếm Neon (2, 8)?", ["Na+ và F-", "K+ và Cl-", "Ca2+ và S2-", "Mg2+ và Cl-"], 0, "Na (11) nhường 1e thành Na+ (10e), F (9) nhận 1e thành F- (10e) đều giống Ne."),
        make_mc(10, "Thông hiểu", "Trong phân tử hợp chất ion K2O, tỉ lệ số ion K+ và O2- là:", ["2 : 1", "1 : 2", "1 : 1", "2 : 3"], 0, "Công thức K2O gồm 2 ion K+ và 1 ion O2-."),
        make_mc(11, "Thông hiểu", "Mô hình phân tử khí methane (CH4) có dạng hình học nào?", ["Hình tứ diện đều", "Đường thẳng", "Tam giác phẳng", "Hình vuông"], 0, "4 liên kết C-H phân bố đối xứng theo hình tứ diện đều."),
        make_mc(12, "Thông hiểu", "Hiện tượng dẫn điện của dung dịch muối ăn chứng minh:", ["Trong dung dịch có các ion chuyển động tự do", "Muối ăn có chứa dòng điện", "Nước cất tự dẫn điện", "Electron tự do chuyển động trong nước"], 0, "Các ion Na+ và Cl- chuyển động tự do đóng vai trò hạt tải điện.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét phân tử khí hydrogen chloride (HCl):", [
            ("a", "Được tạo thành từ liên kết cộng hóa trị giữa nguyên tử H và Cl.", True),
            ("b", "Cặp electron dùng chung bị hút lệch về phía nguyên tử Chlorine.", True),
            ("c", "Khi tan trong nước, khí HCl tạo thành dung dịch axit dẫn điện được.", True),
            ("d", "Ở nhiệt độ phòng, HCl là chất rắn kết tinh màu trắng.", False)
        ], "Ở nhiệt độ phòng, HCl là chất khí không màu."),
        make_tf(2, "Thông hiểu", "Về khả năng dẫn điện của các chất:", [
            ("a", "Nước cất tinh khiết hầu như không dẫn điện.", True),
            ("b", "Nước muối dẫn điện tốt do có ion tự do.", True),
            ("c", "Muối ăn ở dạng tinh thể rắn dẫn điện rất tốt.", False),
            ("d", "Dung dịch đường ăn trong nước không dẫn điện.", True)
        ], "Muối ăn thể rắn các ion bị giam giữ không chuyển động được nên không dẫn điện."),
        make_tf(3, "Vận dụng", "Cho các hợp chất: Na2O, H2S, NH3, BaCl2:", [
            ("a", "Na2O và BaCl2 là các hợp chất ion.", True),
            ("b", "H2S và NH3 là các hợp chất cộng hóa trị.", True),
            ("c", "H2S có mùi trứng thối đặc trưng.", True),
            ("d", "BaCl2 có nhiệt độ nóng chảy thấp hơn H2S.", False)
        ], "BaCl2 là hợp chất ion có nhiệt độ nóng chảy cao hơn H2S thể khí rất nhiều."),
        make_tf(4, "Vận dụng", "Nguyên tử X (Z = 12) kết hợp với nguyên tử Y (Z = 8) tạo thành chất Z:", [
            ("a", "X là Magnesium, Y là Oxygen.", True),
            ("b", "Z là Magnesium oxide (MgO).", True),
            ("c", "Liên kết trong Z là liên kết ion.", True),
            ("d", "Z có nhiệt độ nóng chảy dưới 100°C.", False)
        ], "MgO có nhiệt độ nóng chảy cực cao (~2852°C), được dùng làm gạch chịu lửa.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Số hạt electron mang điện tích âm trong một ion Na+ là bao nhiêu hạt?", "10", "Na có 11e, nhường 1e còn 10e."),
        make_sa(2, "Thông hiểu", "Số electron mà nguyên tử kim loại Aluminium nhường đi khi tạo liên kết ion là bao nhiêu?", "3", "Al nhường 3e tạo ion Al3+."),
        make_sa(3, "Vận dụng", "Số cặp electron dùng chung trong phân tử khí oxygen (O2) là bao nhiêu?", "2", "O2 có liên kết đôi (2 cặp e dùng chung)."),
        make_sa(4, "Vận dụng", "Một ion oxide O2- có bao nhiêu electron ở lớp vỏ ngoài cùng?", "8", "O nhận 2e đạt octet 8e bền vững."),
        make_sa(5, "Vận dụng cao", "Trong phân tử hợp chất ion CaCl2, tỉ số giữa số cation Ca2+ và anion Cl- là bao nhiêu? (Ghi tỉ số dạng 1:2)", "1:2", "Tỉ lệ 1 ion Ca2+ và 2 ion Cl-."),
        make_sa(6, "Vận dụng cao", "Phân tử khí nào có khối lượng phân tử là 28 amu và có liên kết ba rất bền vững? (Viết KHHH)", "N2", "Nitrogen (N2) có PTK = 28 amu và liên kết ba N≡N.")
    ],
    "part4": [
        make_vdc(1, "Vật liệu chịu lửa trong lò luyện kim thường được chế tạo từ magnesium oxide (MgO). Nguyên nhân chính là do:", ["MgO có liên kết ion rất bền vững nên có nhiệt độ nóng chảy cực kì cao (~2850°C)", "MgO nhẹ hơn các chất khác", "MgO có màu trắng đẹp", "MgO dẫn điện tốt"], 0, "Đặc tính liên kết ion siêu bền của MgO."),
        make_vdc(2, "Cho biết độ âm điện của H là 2,2 và Cl là 3,16. Liên kết trong phân tử HCl là:", ["Liên kết cộng hóa trị có cực (phân cực)", "Liên kết ion", "Liên kết cộng hóa trị không cực", "Liên kết kim loại"], 0, "Hiệu độ âm điện 3,16 - 2,2 = 0,96 thuộc khoảng liên kết cộng hóa trị phân cực."),
        make_vdc(3, "Hai nguyên tử X và Y có cấu hình electron lớp ngoài cùng lần lượt là 3s1 và 2s2 2p4. Công thức phân tử của hợp chất tạo bởi X và Y là:", ["X2Y", "XY", "XY2", "X2Y3"], 0, "X là Na (hóa trị I), Y là O (hóa trị II) => X2Y (Na2O)."),
        make_vdc(4, "Một chất X có các tính chất: ở thể rắn màu trắng, tan nhiều trong nước tạo dung dịch dẫn điện, khi nung nóng ở 800°C mới bắt đầu nóng chảy. X có thể là chất nào?", ["NaCl", "Đường mía", "Parafin", "Nước đá"], 0, "NaCl đáp ứng đầy đủ tính chất của chất ion điển hình.")
    ]
}

print(f"Hoàn thành Bài 6. Tổng số đề hiện tại: {len(exams)} đề.")
