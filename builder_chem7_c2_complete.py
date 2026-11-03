# -*- coding: utf-8 -*-
"""
HÓA HỌC 7 - CHƯƠNG II: PHÂN TỬ - LIÊN KẾT HÓA HỌC (14 ĐỀ THI ĐỘC LẬP 100%)
- chem7_c2_b5: Bài 5: Phân tử - Đơn chất - Hợp chất (3 đề)
- chem7_c2_b6: Bài 6: Giới thiệu về liên kết hóa học (3 đề)
- chem7_c2_b7: Bài 7: Hóa trị và công thức hóa học (3 đề)
- chem7_c2_rev: Ôn tập Chương II (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from builder_chem7_c1_complete import exams, make_mc, make_tf, make_sa, make_vdc

# ==============================================================================
# BÀI 5: PHÂN TỬ - ĐƠN CHẤT - HỢP CHẤT (3 ĐỀ ĐỘC LẬP)
# ==============================================================================

# --- ĐỀ 1: Khái niệm phân tử, hạt hợp thành, phân tử khối của đơn chất & hợp chất đơn giản ---
exams["chem7_c2_b5_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và:", ["Thể hiện đầy đủ tính chất hóa học của chất", "Có khối lượng bằng 1 amu", "Luôn gồm các nguyên tử cùng loại", "Không thể bị phân chia trong phản ứng hóa học"], 0, "Phân tử thể hiện đầy đủ tính chất hóa học của chất."),
        make_mc(2, "Nhận biết", "Đơn chất là những chất được tạo nên từ:", ["Một nguyên tố hóa học", "Hai nguyên tố hóa học", "Ba nguyên tố hóa học", "Nhiều nguyên tố hóa học"], 0, "Đơn chất do 1 nguyên tố hóa học tạo nên."),
        make_mc(3, "Nhận biết", "Hợp chất là những chất được tạo nên từ:", ["Từ hai nguyên tố hóa học trở lên", "Chỉ một nguyên tố hóa học", "Hai chất khác nhau trộn lẫn", "Các hạt neutron"], 0, "Hợp chất tạo nên từ 2 nguyên tố hóa học trở lên."),
        make_mc(4, "Nhận biết", "Chất nào sau đây là đơn chất kim loại?", ["Iron (Sắt)", "Nước", "Khí oxygen", "Muối ăn"], 0, "Iron (Fe) là đơn chất kim loại."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là đơn chất phi kim ở thể khí?", ["Khí nitrogen (N2)", "Đồng (Cu)", "Than chì (C)", "Thủy ngân (Hg)"], 0, "Nitrogen là đơn chất phi kim thể khí."),
        make_mc(6, "Nhận biết", "Khối lượng phân tử của một chất bằng:", ["Tổng khối lượng của các nguyên tử trong phân tử", "Khối lượng của nguyên tử nặng nhất", "Số nguyên tử nhân với 1 amu", "Khối lượng hạt nhân của một nguyên tử"], 0, "Khối lượng phân tử = tổng khối lượng các nguyên tử tạo nên phân tử tính theo amu."),
        make_mc(7, "Thông hiểu", "Khối lượng phân tử của nước (H2O) là:", ["18 amu", "16 amu", "17 amu", "20 amu"], 0, "2 × 1 + 16 = 18 amu."),
        make_mc(8, "Thông hiểu", "Trong các chất sau: N2, O2, CO2, Fe, H2O, NaCl. Có bao nhiêu hợp chất?", ["3 hợp chất (CO2, H2O, NaCl)", "2 hợp chất", "4 hợp chất", "5 hợp chất"], 0, "CO2, H2O, NaCl là hợp chất tạo bởi từ 2 nguyên tố."),
        make_mc(9, "Thông hiểu", "Khối lượng phân tử của khí oxygen (O2) là:", ["32 amu", "16 amu", "8 amu", "64 amu"], 0, "2 × 16 = 32 amu."),
        make_mc(10, "Thông hiểu", "Mô hình phân tử khí methane gồm 1 nguyên tử Carbon liên kết với 4 nguyên tử Hydrogen. Khối lượng phân tử methane là:", ["16 amu", "12 amu", "14 amu", "18 amu"], 0, "12 + 4 × 1 = 16 amu."),
        make_mc(11, "Thông hiểu", "Chất nào sau đây là hợp chất vô cơ phổ biến có trong muối ăn hàng ngày?", ["Sodium chloride (NaCl)", "Sucrose (đường mía)", "Ethanol (cồn)", "Glucose"], 0, "Muối ăn là hợp chất NaCl."),
        make_mc(12, "Thông hiểu", "Khí hydrogen là đơn chất nhẹ nhất vì phân tử khối của nó chỉ bằng:", ["2 amu", "1 amu", "4 amu", "14 amu"], 0, "Phân tử H2 có khối lượng = 2 × 1 = 2 amu.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các chất: Khí chlorine (Cl2), Kim loại nhôm (Al), Nước vôi trong (Ca(OH)2), Đường mía (C12H22O11):", [
            ("a", "Cl2 và Al là các đơn chất.", True),
            ("b", "Ca(OH)2 và C12H22O11 là các hợp chất.", True),
            ("c", "Al là đơn chất dẫn điện và dẫn nhiệt tốt.", True),
            ("d", "Cl2 là hợp chất khí màu vàng lục.", False)
        ], "Cl2 chỉ tạo từ 1 nguyên tố Cl nên là đơn chất."),
        make_tf(2, "Thông hiểu", "Về khối lượng phân tử của các chất:", [
            ("a", "Khối lượng phân tử CO2 là 44 amu (12 + 2 × 16).", True),
            ("b", "Khối lượng phân tử NaCl là 58,5 amu (23 + 35,5).", True),
            ("c", "Khối lượng phân tử NH3 là 17 amu (14 + 3 × 1).", True),
            ("d", "Khối lượng phân tử O3 (ozone) nhẹ hơn khí O2.", False)
        ], "O3 có khối lượng 48 amu, nặng hơn O2 (32 amu)."),
        make_tf(3, "Vận dụng", "Cho các mẫu chất: thanh đồng (Cu), bình khí heli (He), cốc nước tinh khiết (H2O), viên than củi (C):", [
            ("a", "Chỉ có nước tinh khiết là hợp chất.", True),
            ("b", "Khí heli tồn tại ở dạng đơn nguyên tử đóng vai trò như phân tử.", True),
            ("c", "Thanh đồng được tạo nên từ vô số nguyên tử đồng xếp khít nhau.", True),
            ("d", "Viên than củi cấu tạo từ hợp chất của cacbon và hidro.", False)
        ], "Than chì cấu tạo từ đơn chất Carbon."),
        make_tf(4, "Vận dụng", "Phân tử axit sunfuric có cấu tạo gồm 2 nguyên tử H, 1 nguyên tử S và 4 nguyên tử O:", [
            ("a", "Công thức phân tử của axit là H2SO4.", True),
            ("b", "Axit sunfuric là một hợp chất.", True),
            ("c", "Khối lượng phân tử của axit sunfuric là 98 amu.", True),
            ("d", "Trong phân tử, nguyên tố có khối lượng lớn nhất là Sulfur.", False)
        ], "Oxygen chiếm 4 × 16 = 64 amu, lớn hơn Sulfur (32 amu).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khối lượng phân tử của khí carbon monoxide (CO) gồm 1 nguyên tử C và 1 nguyên tử O là bao nhiêu amu?", "28", "12 + 16 = 28 amu."),
        make_sa(2, "Thông hiểu", "Khí ozone gồm mấy nguyên tử oxygen liên kết trong một phân tử?", "3", "Ozone là O3 gồm 3 nguyên tử O."),
        make_sa(3, "Vận dụng", "Khối lượng phân tử của calcium carbonate (CaCO3, thành phần chính của đá vôi) là bao nhiêu amu?", "100", "40 + 12 + 3 × 16 = 100 amu."),
        make_sa(4, "Vận dụng", "Trong các chất sau: O2, H2, CO2, Fe, H2SO4, Cu. Có bao nhiêu đơn chất?", "4", "4 đơn chất: O2, H2, Fe, Cu."),
        make_sa(5, "Vận dụng cao", "Một phân tử hợp chất gồm 2 nguyên tử nguyên tố X liên kết với 1 nguyên tử O và nặng bằng 62 amu. Khối lượng nguyên tử của X là bao nhiêu amu?", "23", "2X + 16 = 62 => 2X = 46 => X = 23 (Na)."),
        make_sa(6, "Vận dụng cao", "Phân tử cồn ethanol gồm 2 nguyên tử C, 6 nguyên tử H và 1 nguyên tử O. Khối lượng phân tử của ethanol là bao nhiêu amu?", "46", "2 × 12 + 6 × 1 + 16 = 46 amu.")
    ],
    "part4": [
        make_vdc(1, "Phân tử chất X nặng gấp 1,0625 lần phân tử khí oxygen. Biết X là hợp chất của nguyên tố R với Hydrogen có công thức RH3. Tên của nguyên tố R là:", ["Phosphorus (P)", "Nitrogen (N)", "Boron (B)", "Carbon (C)"], 0, "Khối lượng X = 1,0625 × 32 = 34 amu. R + 3 = 34 => R = 31 (Phosphorus)."),
        make_vdc(2, "Một hợp chất có phân tử gồm nguyên tố X liên kết với nhóm SO4 (khối lượng nhóm là 96 amu) theo tỉ lệ 1 : 1. Biết khối lượng phân tử hợp chất là 160 amu. Nguyên tố X là:", ["Copper (Cu, 64 amu)", "Iron (Fe, 56 amu)", "Zinc (Zn, 65 amu)", "Magnesium (Mg, 24 amu)"], 0, "X + 96 = 160 => X = 64 (Copper, CuSO4)."),
        make_vdc(3, "Cho biết 1 phân tử chất A gồm 2 nguyên tử nguyên tố Y liên kết với 3 nguyên tử Oxygen và nặng gấp 5 lần phân tử khí O2. Khối lượng nguyên tử của Y là:", ["56 amu (Iron)", "27 amu (Aluminium)", "52 amu (Chromium)", "31 amu (Phosphorus)"], 0, "Khối lượng A = 5 × 32 = 160 amu. 2Y + 48 = 160 => 2Y = 112 => Y = 56 (Iron)."),
        make_vdc(4, "Tỉ số về khối lượng giữa nguyên tố Carbon và Oxygen trong phân tử khí CO2 là:", ["3 : 8", "1 : 2", "3 : 4", "12 : 16"], 0, "mC : mO = 12 : (2 × 16) = 12 : 32 = 3 : 8.")
    ]
}

# --- ĐỀ 2: Phân loại đơn chất kim loại, phi kim, hợp chất vô cơ/hữu cơ, tỉ lệ khối lượng ---
exams["chem7_c2_b5_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Đơn chất phi kim nào sau đây ở thể rắn có tính dẫn điện đặc biệt được dùng làm điện cực pin?", ["Than chì (Carbon)", "Lưu huỳnh (Sulfur)", "Photpho (Phosphorus)", "Iot (Iodine)"], 0, "Than chì là phi kim dẫn điện tốt."),
        make_mc(2, "Nhận biết", "Trong các chất sau, chất nào KHÔNG phải là hợp chất?", ["Khí hydrogen (H2)", "Nước (H2O)", "Khí carbon dioxide (CO2)", "Đường ăn (C12H22O11)"], 0, "H2 là đơn chất tạo từ 1 nguyên tố H."),
        make_mc(3, "Nhận biết", "Phân tử của đơn chất khí hiếm Neon gồm bao nhiêu nguyên tử?", ["1 nguyên tử", "2 nguyên tử", "3 nguyên tử", "4 nguyên tử"], 0, "Khí hiếm tồn tại ở dạng đơn nguyên tử."),
        make_mc(4, "Nhận biết", "Kim loại dẫn điện tốt nhất trong số các đơn chất kim loại là:", ["Bạc (Silver)", "Đồng (Copper)", "Vàng (Gold)", "Nhôm (Aluminium)"], 0, "Bạc dẫn điện tốt nhất."),
        make_mc(5, "Nhận biết", "Hợp chất có trong thành phần chính của gas đun nấu gia đình là:", ["Butane và propane (chứa C và H)", "Khí oxygen", "Khí nitrogen", "Nước cất"], 0, "Khí gas là hợp chất hữu cơ hydrocarbon."),
        make_mc(6, "Nhận biết", "Hạt đại diện cho chất và thể hiện đầy đủ tính chất hóa học của chất là:", ["Phân tử", "Nguyên tử đơn lẻ", "Proton", "Electron"], 0, "Phân tử là hạt đại diện cho chất."),
        make_mc(7, "Thông hiểu", "Khối lượng phân tử của sulfuric acid (H2SO4) là:", ["98 amu", "96 amu", "100 amu", "80 amu"], 0, "2 × 1 + 32 + 4 × 16 = 98 amu."),
        make_mc(8, "Thông hiểu", "Chất nào sau đây có khối lượng phân tử bằng 34 amu?", ["Hydrogen sulfide (H2S)", "Nước (H2O)", "Ammonia (NH3)", "Khí methane (CH4)"], 0, "2 × 1 + 32 = 34 amu (H2S)."),
        make_mc(9, "Thông hiểu", "Kim loại nào sau đây dùng làm dây tóc bóng đèn sợi đốt nhờ nhiệt độ nóng chảy rất cao?", ["Tungsten (Vonfram)", "Đồng", "Sắt", "Chì"], 0, "Tungsten có nhiệt độ nóng chảy cao nhất (~3422°C)."),
        make_mc(10, "Thông hiểu", "Một chất lỏng trong suốt không màu, không mùi, sôi ở 100°C và đóng băng ở 0°C. Chất lỏng đó là:", ["Nước tinh khiết", "Cồn ethanol", "Nước muối", "Giấm ăn"], 0, "Tính chất vật lí đặc trưng của nước tinh khiết."),
        make_mc(11, "Thông hiểu", "Khối lượng phân tử của hợp chất NaOH (sodium hydroxide) là:", ["40 amu", "39 amu", "41 amu", "58,5 amu"], 0, "23 + 16 + 1 = 40 amu."),
        make_mc(12, "Thông hiểu", "Số nguyên tố hóa học cấu tạo nên phân tử baking soda (NaHCO3) là:", ["4 nguyên tố (Na, H, C, O)", "3 nguyên tố", "5 nguyên tố", "6 nguyên tố"], 0, "Gồm 4 nguyên tố: Na, H, C, O.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các chất: Kim cương, Khí oxygen, Nước cất, Muối ăn:", [
            ("a", "Kim cương và khí oxygen là các đơn chất phi kim.", True),
            ("b", "Nước cất và muối ăn là các hợp chất.", True),
            ("c", "Khí oxygen nặng hơn nước cất.", False),
            ("d", "Khối lượng phân tử của nước cất là 18 amu.", True)
        ], "Khí oxygen có PTK = 32 amu nhưng ở thể khí khối lượng riêng nhỏ hơn nhiều so với nước lỏng."),
        make_tf(2, "Thông hiểu", "Cho các hợp chất: H2O, NH3, CH4, SO2:", [
            ("a", "Tất cả các chất này đều là hợp chất.", True),
            ("b", "CH4 có khối lượng phân tử nhỏ nhất trong số các chất này (16 amu).", True),
            ("c", "SO2 có khối lượng phân tử lớn nhất (64 amu).", True),
            ("d", "Phân tử NH3 gồm 3 nguyên tử cấu tạo nên.", False)
        ], "NH3 gồm 1 nguyên tử N và 3 nguyên tử H => tổng cộng 4 nguyên tử."),
        make_tf(3, "Vận dụng", "Xét hợp chất nhôm oxide có công thức Al2O3:", [
            ("a", "Hợp chất này được tạo nên từ 2 nguyên tố hóa học là Aluminium và Oxygen.", True),
            ("b", "Trong 1 phân tử có 2 nguyên tử Al và 3 nguyên tử O.", True),
            ("c", "Khối lượng phân tử của Al2O3 là 102 amu.", True),
            ("d", "Aluminium chiếm hơn 60% khối lượng phân tử.", False)
        ], "%Al = (2 × 27) / 102 × 100% ≈ 52,94% (< 60%)."),
        make_tf(4, "Vận dụng", "Hợp chất X có công thức phân tử là Fe2(SO4)3:", [
            ("a", "X được cấu tạo từ 3 nguyên tố: Fe, S, O.", True),
            ("b", "Tổng số nguyên tử có trong 1 phân tử X là 17 nguyên tử.", True),
            ("c", "Khối lượng phân tử của X là 400 amu.", True),
            ("d", "X là một đơn chất kim loại.", False)
        ], "X là hợp chất muối của sắt.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Phân tử khí ammonia (NH3) gồm tổng cộng bao nhiêu nguyên tử?", "4", "1 N + 3 H = 4 nguyên tử."),
        make_sa(2, "Thông hiểu", "Khối lượng phân tử của phân đạm urea (CH4N2O) là bao nhiêu amu?", "60", "12 + 4 + 28 + 16 = 60 amu."),
        make_sa(3, "Vận dụng", "Phân tử copper(II) sulfate gồm 1 nguyên tử Cu, 1 nguyên tử S và 4 nguyên tử O. Khối lượng phân tử của nó là bao nhiêu amu?", "160", "64 + 32 + 64 = 160 amu."),
        make_sa(4, "Vận dụng", "Trong các chất: Al, CuO, N2, HCl, O3, CaCO3. Có bao nhiêu hợp chất?", "3", "3 hợp chất: CuO, HCl, CaCO3."),
        make_sa(5, "Vận dụng cao", "Một oxide của sắt có dạng Fe2Ox nặng 160 amu. Giá trị của x là bao nhiêu?", "3", "2 × 56 + 16x = 160 => 16x = 48 => x = 3 (Fe2O3)."),
        make_sa(6, "Vận dụng cao", "Khối lượng phân tử đường glucose (C6H12O6) là bao nhiêu amu?", "180", "6 × 12 + 12 × 1 + 6 × 16 = 180 amu.")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất có phân tử gồm 1 nguyên tử nguyên tố X liên kết với 2 nguyên tử O và nặng gấp 2 lần phân tử khí O2. Khối lượng nguyên tử của X là:", ["32 amu (Sulfur)", "12 amu (Carbon)", "28 amu (Silicon)", "14 amu (Nitrogen)"], 0, "Khối lượng = 2 × 32 = 64 amu. X + 32 = 64 => X = 32 (Sulfur, SO2)."),
        make_vdc(2, "Tỉ lệ khối lượng của H và O trong phân tử nước (H2O) là:", ["1 : 8", "1 : 16", "2 : 1", "1 : 2"], 0, "mH : mO = 2 : 16 = 1 : 8."),
        make_vdc(3, "Một phân tử khí hydrocarbon X gồm 2 nguyên tử Carbon và một số nguyên tử Hydrogen. Biết khối lượng phân tử X là 28 amu. Số nguyên tử Hydrogen trong phân tử X là:", ["4", "2", "6", "8"], 0, "2 × 12 + y = 28 => y = 4 (C2H4, ethylene)."),
        make_vdc(4, "Hợp chất A chứa 75% Carbon và 25% Hydrogen về khối lượng. Biết khối lượng phân tử của A là 16 amu. Công thức phân tử của A là:", ["CH4", "C2H6", "C2H2", "C3H8"], 0, "mC = 16 × 0,75 = 12 (1C), mH = 4 (4H) => CH4 (methane).")
    ]
}

# --- ĐỀ 3: Mô hình phân tử, cấu tạo hạt của chất, liên hệ tính chất vật lí và hóa học ---
exams["chem7_c2_b5_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Đơn chất kim loại ở thể lỏng ở nhiệt độ phòng là:", ["Thủy ngân (Mercury)", "Chì (Lead)", "Đồng (Copper)", "Sắt (Iron)"], 0, "Mercury (Hg) là kim loại lỏng duy nhất ở điều kiện thường."),
        make_mc(2, "Nhận biết", "Trong các chất sau, chất nào là đơn chất phi kim ở thể rắn?", ["Lưu huỳnh (Sulfur)", "Khí nitrogen", "Nước", "Thủy ngân"], 0, "Lưu huỳnh là phi kim rắn màu vàng."),
        make_mc(3, "Nhận biết", "Khối lượng phân tử của khí chlorine (Cl2) theo amu xấp xỉ là:", ["71 amu", "35,5 amu", "17 amu", "142 amu"], 0, "2 × 35,5 = 71 amu."),
        make_mc(4, "Nhận biết", "Hợp chất nước vôi trong có thành phần chính là:", ["Calcium hydroxide (Ca(OH)2)", "Calcium carbonate (CaCO3)", "Sodium hydroxide (NaOH)", "Calcium oxide (CaO)"], 0, "Nước vôi trong là dung dịch Ca(OH)2."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là hỗn hợp chứ KHÔNG phải chất tinh khiết?", ["Không khí", "Nước cất", "Muối ăn tinh khiết", "Khí oxygen tinh khiết"], 0, "Không khí là hỗn hợp của N2, O2, CO2, hơi nước..."),
        make_mc(6, "Nhận biết", "Chất được cấu tạo từ 2 nguyên tố C và O thường gặp trong khí thở ra của người là:", ["Carbon dioxide (CO2)", "Methane (CH4)", "Ammonia (NH3)", "Sulfur dioxide (SO2)"], 0, "CO2 được sinh ra trong quá trình hô hấp."),
        make_mc(7, "Thông hiểu", "Khối lượng phân tử của acetic acid (CH3COOH, có trong giấm ăn) là:", ["60 amu", "46 amu", "58 amu", "74 amu"], 0, "2 × 12 + 4 × 1 + 2 × 16 = 60 amu."),
        make_mc(8, "Thông hiểu", "Cho các chất: N2, O2, H2O, Cu, CO2, NaCl, Fe. Tỉ lệ giữa số đơn chất và số hợp chất là:", ["4 : 3", "3 : 4", "1 : 1", "5 : 2"], 0, "4 đơn chất (N2, O2, Cu, Fe) và 3 hợp chất (H2O, CO2, NaCl) => 4 : 3."),
        make_mc(9, "Thông hiểu", "Khối lượng phân tử của potassium hydroxide (KOH) là:", ["56 amu", "39 amu", "57 amu", "40 amu"], 0, "39 + 16 + 1 = 56 amu."),
        make_mc(10, "Thông hiểu", "Phân tử khí nào sau đây nặng hơn không khí (khối lượng trung bình của không khí là 29 amu)?", ["Carbon dioxide (CO2, 44 amu)", "Methane (CH4, 16 amu)", "Ammonia (NH3, 17 amu)", "Nitrogen (N2, 28 amu)"], 0, "CO2 có 44 amu > 29 amu nên nặng hơn không khí."),
        make_mc(11, "Thông hiểu", "Trong một phân tử khí sulfur dioxide (SO2), tỉ lệ số nguyên tử S và O là:", ["1 : 2", "2 : 1", "1 : 1", "1 : 3"], 0, "Gồm 1 nguyên tử S và 2 nguyên tử O."),
        make_mc(12, "Thông hiểu", "Chất nào sau đây là đơn chất phi kim được dùng để làm đầu que diêm và thuốc pháo?", ["Photpho (Phosphorus)", "Than chì", "Lưu huỳnh", "Magnesium"], 0, "Photpho đỏ dùng ở đầu que diêm và bao diêm.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét phân tử axit clohiđric (HCl):", [
            ("a", "HCl là một hợp chất.", True),
            ("b", "Được tạo nên từ 2 nguyên tố là Hydrogen và Chlorine.", True),
            ("c", "Khối lượng phân tử của HCl là 36,5 amu.", True),
            ("d", "Khí HCl nhẹ hơn không khí.", False)
        ], "PTK của HCl là 36,5 amu > 29 amu nên nặng hơn không khí."),
        make_tf(2, "Thông hiểu", "Về các đơn chất kim loại trong tự nhiên:", [
            ("a", "Hầu hết các kim loại ở thể rắn (trừ thủy ngân).", True),
            ("b", "Kim loại có ánh kim, dẫn nhiệt và dẫn điện tốt.", True),
            ("c", "Vàng và bạch kim là những kim loại rất khó bị oxi hóa.", True),
            ("d", "Kim loại nhôm nặng hơn sắt.", False)
        ], "Nhôm (D = 2,7 g/cm3) nhẹ hơn sắt (D = 7,86 g/cm3)."),
        make_tf(3, "Vận dụng", "Cho các hợp chất: CO, CO2, SO2, SO3:", [
            ("a", "Đều là hợp chất của phi kim với oxygen (oxide).", True),
            ("b", "SO3 có khối lượng phân tử lớn nhất là 80 amu.", True),
            ("c", "CO có khối lượng phân tử nhẹ nhất là 28 amu.", True),
            ("d", "CO2 nhẹ hơn CO.", False)
        ], "CO2 (44 amu) nặng hơn CO (28 amu)."),
        make_tf(4, "Vận dụng", "Hợp chất X có công thức Al(OH)3:", [
            ("a", "X tạo bởi 3 nguyên tố: Al, O, H.", True),
            ("b", "Khối lượng phân tử của X là 78 amu.", True),
            ("c", "X là kết tủa trắng keo không tan trong nước.", True),
            ("d", "Trong X, phần trăm khối lượng của H là lớn nhất.", False)
        ], "Oxygen chiếm 3 × 16 = 48 amu (lớn nhất).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khối lượng phân tử của hydrogen chloride (HCl) là bao nhiêu amu? (Làm tròn 1 chữ số thập phân)", "36.5", "1 + 35,5 = 36,5 amu."),
        make_sa(2, "Thông hiểu", "Phân tử sulfur trioxide (SO3) gồm bao nhiêu nguyên tử oxygen?", "3", "SO3 có 3 nguyên tử O."),
        make_sa(3, "Vận dụng", "Khối lượng phân tử của magnesium chloride (MgCl2) là bao nhiêu amu?", "95", "24 + 2 × 35,5 = 95 amu."),
        make_sa(4, "Vận dụng", "Trong phân tử hợp chất Fe(OH)3 có bao nhiêu nguyên tố hóa học cấu tạo nên?", "3", "3 nguyên tố: Fe, O, H."),
        make_sa(5, "Vận dụng cao", "Phân tử hợp chất Na2X có khối lượng phân tử bằng 78 amu. Khối lượng nguyên tử của nguyên tố X là bao nhiêu amu?", "32", "2 × 23 + X = 78 => X = 32 amu (Sulfur)."),
        make_sa(6, "Vận dụng cao", "Phân tử tinh thể đồng sunfat ngậm nước có công thức CuSO4.5H2O. Khối lượng phân tử của nó là bao nhiêu amu?", "250", "160 + 5 × 18 = 250 amu.")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất có phân tử gồm 2 nguyên tử nguyên tố X liên kết với 5 nguyên tử Oxygen và có khối lượng phân tử là 142 amu. Tên của nguyên tố X là:", ["Phosphorus (P)", "Nitrogen (N)", "Arsenic (As)", "Vanadium (V)"], 0, "2X + 5 × 16 = 142 => 2X = 62 => X = 31 (Phosphorus, P2O5)."),
        make_vdc(2, "Phần trăm khối lượng của nguyên tố Nitrogen trong phân tử phân đạm NH4NO3 là:", ["35%", "28%", "17,5%", "42%"], 0, "M = 14 + 4 + 14 + 48 = 80 amu. %N = 28 / 80 × 100% = 35%."),
        make_vdc(3, "Một phân tử khí X gồm nguyên tố Carbon liên kết với Hydrogen, trong đó Carbon chiếm 85,71% về khối lượng. Khối lượng phân tử của X là 28 amu. Công thức phân tử của X là:", ["C2H4", "CH4", "C2H6", "C3H6"], 0, "mC = 28 × 0,8571 ≈ 24 (2C), mH = 4 (4H) => C2H4."),
        make_vdc(4, "Khối lượng của 1 phân tử nước tính bằng gam xấp xỉ bằng:", ["2,99 × 10^-23 g", "1,66 × 10^-24 g", "18 g", "1,8 × 10^-22 g"], 0, "18 × 1,6605 × 10^-24 g ≈ 2,989 × 10^-23 g.")
    ]
}

print(f"Hoàn thành Bài 5. Tổng số đề hiện tại: {len(exams)} đề.")
