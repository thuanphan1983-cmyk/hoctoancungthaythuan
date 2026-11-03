# -*- coding: utf-8 -*-
"""
HÓA HỌC 7 - HOÀN TẤT BÀI 7 & ÔN TẬP CHƯƠNG II (8 ĐỀ ĐỘC LẬP)
Hoàn thành trọn vẹn 28 đề thi Hóa học 7 độc lập 100%
- chem7_c2_b7: Bài 7: Hóa trị và công thức hóa học (3 đề)
- chem7_c2_rev: Ôn tập Chương II (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from builder_chem7_c2_part2 import exams, make_mc, make_tf, make_sa, make_vdc

# ==============================================================================
# BÀI 7: HÓA TRỊ VÀ CÔNG THỨC HÓA HỌC (3 ĐỀ ĐỘC LẬP)
# ==============================================================================

# --- ĐỀ 1: Quy tắc hóa trị, xác định hóa trị nguyên tố, ý nghĩa CTHH ---
exams["chem7_c2_b7_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Trong quy ước về hóa trị, nguyên tố nào được chọn làm đơn vị và luôn có hóa trị I?", ["Hydrogen", "Oxygen", "Carbon", "Nitrogen"], 0, "Hydrogen luôn được quy ước có hóa trị I."),
        make_mc(2, "Nhận biết", "Trong các hợp chất, nguyên tố Oxygen luôn được quy ước có hóa trị là:", ["II", "I", "III", "IV"], 0, "Oxygen luôn có hóa trị II."),
        make_mc(3, "Nhận biết", "Theo quy tắc hóa trị, trong hợp chất hai nguyên tố AxBy (với a, b là hóa trị tương ứng của A và B) luôn có biểu thức:", ["x × a = y × b", "x × b = y × a", "x / a = y / b", "x + a = y + b"], 0, "Quy tắc hóa trị: x × a = y × b."),
        make_mc(4, "Nhận biết", "Công thức hóa học của đơn chất kim loại nhôm là:", ["Al", "Al2", "Al3", "AlO"], 0, "Đơn chất kim loại kí hiệu bằng KHHH của nguyên tố (Al)."),
        make_mc(5, "Nhận biết", "Công thức hóa học của đơn chất khí oxygen là:", ["O2", "O", "O3", "O4"], 0, "Khí oxygen gồm các phân tử 2 nguyên tử O liên kết với nhau: O2."),
        make_mc(6, "Nhận biết", "Ý nghĩa của công thức hóa học cho ta biết các thông tin nào sau đây?", ["Nguyên tố tạo ra chất, số nguyên tử mỗi nguyên tố và khối lượng phân tử", "Chất có độc hay không", "Nhiệt độ nóng chảy chính xác", "Khối lượng riêng của chất"], 0, "Ý nghĩa CTHH: nguyên tố cấu tạo, số lượng nguyên tử, phân tử khối."),
        make_mc(7, "Thông hiểu", "Trong hợp chất FeO, hóa trị của nguyên tố Iron (Sắt) là:", ["II", "III", "I", "IV"], 0, "1 × a = 1 × II => a = II."),
        make_mc(8, "Thông hiểu", "Hợp chất của Carbon với Oxygen có công thức CO2. Hóa trị của Carbon trong hợp chất này là:", ["IV", "II", "VI", "I"], 0, "1 × a = 2 × II => a = IV."),
        make_mc(9, "Thông hiểu", "Lập công thức hóa học của hợp chất tạo bởi Aluminium (hóa trị III) và Oxygen (hóa trị II):", ["Al2O3", "AlO", "Al3O2", "AlO2"], 0, "x/y = II/III = 2/3 => Al2O3."),
        make_mc(10, "Thông hiểu", "Phần trăm khối lượng của nguyên tố Hydrogen trong phân tử nước (H2O) là:", ["11,11%", "20%", "5,56%", "15%"], 0, "%H = 2 / 18 × 100% ≈ 11,11%."),
        make_mc(11, "Thông hiểu", "Trong hợp chất NH3, hóa trị của nguyên tố Nitrogen là:", ["III", "I", "II", "V"], 0, "1 × a = 3 × I => a = III."),
        make_mc(12, "Thông hiểu", "Công thức hóa học nào sau đây viết SAI theo quy tắc hóa trị?", ["NaO", "NaCl", "CaO", "Al2O3"], 0, "Na hóa trị I, O hóa trị II => công thức đúng phải là Na2O (NaO sai).")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét công thức hóa học của khí methane (CH4):", [
            ("a", "Hợp chất tạo bởi 2 nguyên tố là Carbon và Hydrogen.", True),
            ("b", "Trong 1 phân tử có 1 nguyên tử C và 4 nguyên tử H.", True),
            ("c", "Khối lượng phân tử của methane là 16 amu.", True),
            ("d", "Trong phân tử CH4, Carbon có hóa trị II.", False)
        ], "Trong CH4, Carbon có hóa trị IV (1 × IV = 4 × I)."),
        make_tf(2, "Thông hiểu", "Xác định hóa trị của kim loại trong các hợp chất:", [
            ("a", "Trong Na2O, Sodium có hóa trị I.", True),
            ("b", "Trong MgO, Magnesium có hóa trị II.", True),
            ("c", "Trong Fe2O3, Iron có hóa trị III.", True),
            ("d", "Trong Cu2O, Copper có hóa trị II.", False)
        ], "Trong Cu2O: 2 × a = 1 × II => a = I (Copper hóa trị I)."),
        make_tf(3, "Vận dụng", "Cho các hợp chất: H2S, SO2, SO3:", [
            ("a", "Hóa trị của Sulfur trong H2S là II.", True),
            ("b", "Hóa trị của Sulfur trong SO2 là IV.", True),
            ("c", "Hóa trị của Sulfur trong SO3 là VI.", True),
            ("d", "Sulfur có hóa trị không đổi trong tất cả các hợp chất.", False)
        ], "Sulfur có nhiều hóa trị: II, IV, VI."),
        make_tf(4, "Vận dụng", "Một hợp chất có công thức hóa học là Ca3(PO4)2:", [
            ("a", "Gồm 3 nguyên tố: Ca, P, O.", True),
            ("b", "Nhóm PO4 có hóa trị III.", True),
            ("c", "Calcium có hóa trị II.", True),
            ("d", "Tổng số nguyên tử trong một phân tử hợp chất là 10.", False)
        ], "Tổng số nguyên tử = 3 + 2 × (1 + 4) = 13 nguyên tử.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Hóa trị của nguyên tố Chlorine trong phân tử axit clohiđric (HCl) là bao nhiêu?", "I", "H hóa trị I => Cl có hóa trị I."),
        make_sa(2, "Thông hiểu", "Hóa trị của nhóm hydroxide (OH) trong phân tử NaOH là bao nhiêu?", "I", "Nhóm OH có hóa trị I."),
        make_sa(3, "Vận dụng", "Hóa trị của nguyên tố Carbon trong khí độc carbon monoxide (CO) là bao nhiêu?", "II", "1 × a = 1 × II => a = II."),
        make_sa(4, "Vận dụng", "Phần trăm khối lượng của Carbon trong khí carbon dioxide (CO2) xấp xỉ bằng bao nhiêu phần trăm? (Làm tròn đến hàng đơn vị)", "27", "%C = 12 / 44 × 100% ≈ 27,27% ≈ 27%."),
        make_sa(5, "Vận dụng cao", "Lập CTHH của hợp chất tạo bởi sắt có hóa trị III và nhóm sunfat (SO4) có hóa trị II. Số nguyên tử sắt trong công thức là bao nhiêu?", "2", "Fex(SO4)y => x/y = II/III = 2/3 => Fe2(SO4)3 có 2 nguyên tử Fe."),
        make_sa(6, "Vận dụng cao", "Một oxide của nguyên tố R có công thức R2O3 nặng 102 amu. Tên gọi của R là gì?", "Aluminium", "2R + 48 = 102 => 2R = 54 => R = 27 (Aluminium).")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất tạo bởi nguyên tố X (hóa trị II) và nhóm PO4 (hóa trị III) có công thức là:", ["X3(PO4)2", "X2(PO4)3", "XPO4", "X3PO4"], 0, "Quy tắc hóa trị: x/y = III/II = 3/2 => X3(PO4)2."),
        make_vdc(2, "Hợp chất của nguyên tố X với Oxygen là XO. Hợp chất của nguyên tố Y với Hydrogen là YH3. Công thức hóa học của hợp chất tạo bởi X và Y là:", ["X3Y2", "XY", "X2Y3", "X3Y"], 0, "X có hóa trị II (vì XO), Y có hóa trị III (vì YH3) => công thức X3Y2."),
        make_vdc(3, "Hợp chất A chứa 70% Fe và 30% O về khối lượng. Biết khối lượng phân tử của A là 160 amu. Công thức hóa học của A là:", ["Fe2O3", "FeO", "Fe3O4", "Fe2O"], 0, "mFe = 160 × 0,7 = 112 amu (2 nguyên tử Fe), mO = 48 amu (3 nguyên tử O) => Fe2O3."),
        make_vdc(4, "Một oxide kim loại có dạng MO, trong đó kim loại M chiếm 80% về khối lượng. Nguyên tố M là:", ["Copper (Cu, 64 amu)", "Iron (Fe, 56 amu)", "Zinc (Zn, 65 amu)", "Magnesium (Mg, 24 amu)"], 0, "M / (M + 16) = 0,8 => M = 0,8M + 12,8 => 0,2M = 12,8 => M = 64 (Copper, CuO).")
    ]
}

# --- ĐỀ 2: Lập CTHH từ hóa trị, nhóm nguyên tử (OH, SO4, NO3, CO3, PO4), tính % nguyên tố ---
exams["chem7_c2_b7_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Nhóm nguyên tử nào sau đây có hóa trị II?", ["Nhóm sunfat (SO4)", "Nhóm hiđroxit (OH)", "Nhóm nitrat (NO3)", "Nhóm photphat (PO4)"], 0, "Nhóm SO4 và CO3 có hóa trị II (OH và NO3 hóa trị I, PO4 hóa trị III)."),
        make_mc(2, "Nhận biết", "Trong hợp chất Al2O3, nguyên tố Aluminium có hóa trị là:", ["III", "II", "I", "VI"], 0, "2 × a = 3 × II => a = III."),
        make_mc(3, "Nhận biết", "Công thức hóa học của hợp chất tạo bởi Sodium (hóa trị I) và nhóm OH (hóa trị I) là:", ["NaOH", "Na(OH)2", "Na2OH", "NaOH2"], 0, "Cùng hóa trị I tỉ lệ 1 : 1 là NaOH."),
        make_mc(4, "Nhận biết", "Nguyên tố nào sau đây có hóa trị không đổi bằng I trong mọi hợp chất?", ["Sodium (Na)", "Iron (Fe)", "Copper (Cu)", "Carbon (C)"], 0, "Kim loại kiềm Na luôn có hóa trị I."),
        make_mc(5, "Nhận biết", "Công thức hóa học của đá vôi (canxi cacbonat) gồm Ca(II) và nhóm CO3(II) là:", ["CaCO3", "Ca2CO3", "Ca(CO3)2", "Ca2(CO3)3"], 0, "Cùng hóa trị II tỉ lệ 1 : 1 là CaCO3."),
        make_mc(6, "Nhận biết", "Khối lượng phân tử của sulfuric acid (H2SO4) là:", ["98 amu", "96 amu", "100 amu", "80 amu"], 0, "2 × 1 + 32 + 4 × 16 = 98 amu."),
        make_mc(7, "Thông hiểu", "Xác định hóa trị của Iron trong hợp chất FeCl3:", ["III", "II", "I", "IV"], 0, "Cl có hóa trị I => 1 × a = 3 × I => a = III."),
        make_mc(8, "Thông hiểu", "Lập công thức hóa học của hợp chất gồm Magnesium (hóa trị II) và nhóm nitrate NO3 (hóa trị I):", ["Mg(NO3)2", "MgNO3", "Mg2NO3", "Mg(NO3)3"], 0, "x/y = I/II = 1/2 => Mg(NO3)2."),
        make_mc(9, "Thông hiểu", "Hóa trị của nguyên tố Nitrogen trong phân tử N2O5 là:", ["V", "II", "III", "IV"], 0, "2 × a = 5 × II => a = V."),
        make_mc(10, "Thông hiểu", "Hợp chất nào sau đây có hàm lượng (phần trăm khối lượng) nguyên tố Nitrogen cao nhất?", ["Urea CO(NH2)2 (46,67%)", "NH4NO3 (35%)", "NaNO3 (16,47%)", "(NH4)2SO4 (21,21%)"], 0, "Urea có tỉ lệ %N cao nhất trong các loại phân đạm."),
        make_mc(11, "Thông hiểu", "Công thức hóa học của khí sulfur trioxide là:", ["SO3", "SO2", "S2O3", "SO"], 0, "Sulfur trioxide gồm 1 S và 3 O: SO3."),
        make_mc(12, "Thông hiểu", "Trong hợp chất Cu(OH)2, nguyên tố Copper có hóa trị là:", ["II", "I", "III", "IV"], 0, "Nhóm OH hóa trị I => 1 × a = 2 × I => a = II.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét hợp chất nhôm sunfat Al2(SO4)3:", [
            ("a", "Aluminium có hóa trị III.", True),
            ("b", "Nhóm SO4 có hóa trị II.", True),
            ("c", "Khối lượng phân tử của Al2(SO4)3 là 342 amu.", True),
            ("d", "Tỉ lệ số nguyên tử Al và S trong hợp chất là 1 : 1.", False)
        ], "Tỉ lệ Al : S là 2 : 3."),
        make_tf(2, "Thông hiểu", "Xét hóa trị của nguyên tố Carbon trong các hợp chất:", [
            ("a", "Trong CH4, Carbon có hóa trị IV.", True),
            ("b", "Trong CO, Carbon có hóa trị II.", True),
            ("c", "Trong CO2, Carbon có hóa trị IV.", True),
            ("d", "Carbon luôn chỉ thể hiện một hóa trị duy nhất là IV.", False)
        ], "Carbon có hóa trị II (CO) và IV (CO2, CH4)."),
        make_tf(3, "Vận dụng", "Cho các công thức: BaCl2, K2SO4, FeO, Al3O2:", [
            ("a", "BaCl2 viết đúng theo quy tắc hóa trị.", True),
            ("b", "K2SO4 viết đúng theo quy tắc hóa trị.", True),
            ("c", "FeO viết đúng theo quy tắc hóa trị.", True),
            ("d", "Al3O2 viết đúng theo quy tắc hóa trị.", False)
        ], "Al(III) và O(II) phải lập thành Al2O3 (Al3O2 viết sai)."),
        make_tf(4, "Vận dụng", "Hợp chất X có công thức phân tử là Fe3O4 (oxit sắt từ):", [
            ("a", "Là hỗn hợp của FeO và Fe2O3.", True),
            ("b", "Khối lượng phân tử của Fe3O4 là 232 amu.", True),
            ("c", "Trong Fe3O4 có 3 nguyên tử Fe và 4 nguyên tử O.", True),
            ("d", "Phần trăm khối lượng của O lớn hơn phần trăm khối lượng của Fe.", False)
        ], "Fe chiếm 3 × 56 = 168 amu (72,4%), O chỉ chiếm 64 amu (27,6%).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Hóa trị của nhóm cacbonat (CO3) là bao nhiêu?", "II", "Nhóm CO3 có hóa trị II."),
        make_sa(2, "Thông hiểu", "Hóa trị của nguyên tố Barium trong phân tử BaO là bao nhiêu?", "II", "BaO => Ba hóa trị II."),
        make_sa(3, "Vận dụng", "Hợp chất tạo bởi Fe(II) và Cl(I) có công thức là FeClx. Giá trị của x là bao nhiêu?", "2", "1 × II = x × I => x = 2 (FeCl2)."),
        make_sa(4, "Vận dụng", "Phần trăm khối lượng của Oxygen trong phân tử khí sulfur dioxide (SO2, 64 amu) là bao nhiêu phần trăm?", "50", "%O = (2 × 16) / 64 × 100% = 50%."),
        make_sa(5, "Vận dụng cao", "Lập CTHH của hợp chất gồm kim loại M (hóa trị II) và nhóm photphat PO4 (hóa trị III). Tổng chỉ số các nguyên tử và nhóm nguyên tử trong công thức M_x(PO4)_y (tức x + y) là bao nhiêu?", "5", "x/y = 3/2 => M3(PO4)2 có x + y = 3 + 2 = 5."),
        make_sa(6, "Vận dụng cao", "Một oxide kim loại có công thức R2O nặng 62 amu. Kí hiệu hóa học của nguyên tố R là gì?", "Na", "2R + 16 = 62 => 2R = 46 => R = 23 (Sodium, Na2O).")
    ],
    "part4": [
        make_vdc(1, "Hợp chất khí X của Carbon với Hydrogen chứa 80% Carbon về khối lượng. Khối lượng phân tử của X là 30 amu. Công thức phân tử của X là:", ["C2H6", "CH4", "C2H4", "C3H8"], 0, "mC = 30 × 0,8 = 24 amu (2C), mH = 6 amu (6H) => C2H6 (ethane)."),
        make_vdc(2, "Nguyên tố A có hóa trị III trong oxide A2O3. Nguyên tố B có hóa trị I trong hydride BH. Công thức hợp chất tạo bởi A và B là:", ["AB3", "A3B", "AB", "A2B3"], 0, "A hóa trị III, B hóa trị I => AB3."),
        make_vdc(3, "Một loại phân bón potassium chloride có chứa 90% KCl về khối lượng (còn lại là tạp chất không chứa K). Biết khối lượng mol KCl = 74,5 amu (K = 39, Cl = 35,5). Phần trăm khối lượng của nguyên tố K trong mẫu phân bón đó xấp xỉ là:", ["47,1%", "52,3%", "45,0%", "39,0%"], 0, "%K trong KCl tinh khiết = 39 / 74,5 ≈ 52,35%. Trong mẫu: 52,35% × 0,9 ≈ 47,1%."),
        make_vdc(4, "Một oxide của lưu huỳnh trong đó nguyên tố Oxygen chiếm 60% về khối lượng. Hóa trị của Sulfur trong oxide đó là:", ["VI", "IV", "II", "VII"], 0, "mS / mO = 40 / 60 = 2 / 3 => (32x) / (16y) = 2 / 3 => 2x / y = 2 / 3 => x / y = 1 / 3 => SO3. Trong SO3, S có hóa trị VI.")
    ]
}

# --- ĐỀ 3: Xác định CTHH từ % khối lượng, bài toán thực tiễn phân bón & vật liệu ---
exams["chem7_c2_b7_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Kí hiệu hóa học của nguyên tố trong hợp chất kèm theo chỉ số chân dưới biểu thị:", ["Công thức hóa học của chất", "Khối lượng riêng của chất", "Thể tích của chất", "Nhiệt độ nóng chảy"], 0, "Biểu thị công thức hóa học của chất."),
        make_mc(2, "Nhận biết", "Trong công thức hóa học H2O, chỉ số 2 ở chân chữ H cho biết:", ["Trong 1 phân tử nước có 2 nguyên tử Hydrogen", "Có 2 phân tử nước", "Hóa trị của H là 2", "Khối lượng của H là 2 kg"], 0, "Chỉ số chân cho biết số nguyên tử của nguyên tố trong 1 phân tử."),
        make_mc(3, "Nhận biết", "Hợp chất nào sau đây có công thức hóa học viết ĐÚNG theo quy tắc hóa trị?", ["CaCl2", "CaCl", "Ca2Cl", "CaCl3"], 0, "Ca hóa trị II, Cl hóa trị I => CaCl2."),
        make_mc(4, "Nhận biết", "Nguyên tố kim loại nào sau đây có nhiều hóa trị phổ biến là II và III?", ["Iron (Sắt)", "Sodium (Natri)", "Magnesium (Magie)", "Aluminium (Nhôm)"], 0, "Iron có 2 hóa trị phổ biến là II (FeO, FeCl2) và III (Fe2O3, FeCl3)."),
        make_mc(5, "Nhận biết", "Trong hợp chất Al(OH)3, hóa trị của Aluminium là:", ["III", "I", "II", "IV"], 0, "Nhóm OH hóa trị I => 1 × a = 3 × I => a = III."),
        make_mc(6, "Nhận biết", "Công thức hóa học của khí amoniac gồm 1 nguyên tử N và 3 nguyên tử H là:", ["NH3", "N3H", "NH", "N2H3"], 0, "Khí ammonia có CTHH là NH3."),
        make_mc(7, "Thông hiểu", "Xác định hóa trị của nguyên tố Phosphorus trong hợp chất P2O5:", ["V", "III", "IV", "II"], 0, "2 × a = 5 × II => a = V."),
        make_mc(8, "Thông hiểu", "Lập công thức hóa học của hợp chất tạo bởi Potassium (hóa trị I) và Oxygen (hóa trị II):", ["K2O", "KO", "KO2", "K2O3"], 0, "x/y = II/I = 2/1 => K2O."),
        make_mc(9, "Thông hiểu", "Phần trăm khối lượng của nguyên tố Oxygen trong phân tử canxi cacbonat (CaCO3, 100 amu) là:", ["48%", "40%", "12%", "60%"], 0, "%O = (3 × 16) / 100 × 100% = 48%."),
        make_mc(10, "Thông hiểu", "Công thức hóa học của khí gas butane gồm 4 nguyên tử C và 10 nguyên tử H là:", ["C4H10", "C4H8", "C3H8", "C2H6"], 0, "C4H10 là butane."),
        make_mc(11, "Thông hiểu", "Trong hợp chất SO2, nguyên tố Sulfur thể hiện hóa trị mấy?", ["IV", "II", "VI", "I"], 0, "1 × a = 2 × II => a = IV."),
        make_mc(12, "Thông hiểu", "Hợp chất nào sau đây có phân tử khối bằng 74 amu?", ["Calcium hydroxide Ca(OH)2", "Calcium oxide CaO", "Calcium carbonate CaCO3", "Magnesium oxide MgO"], 0, "40 + 2 × (16 + 1) = 74 amu (Ca(OH)2).")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét phân tử axit photphoric H3PO4:", [
            ("a", "Tạo bởi 3 nguyên tố: H, P, O.", True),
            ("b", "Trong 1 phân tử có 3 nguyên tử H, 1 nguyên tử P và 4 nguyên tử O.", True),
            ("c", "Khối lượng phân tử của H3PO4 là 98 amu (3 + 31 + 64).", True),
            ("d", "Nhóm PO4 trong hợp chất có hóa trị I.", False)
        ], "Nhóm PO4 có hóa trị III (3 × I = 1 × III)."),
        make_tf(2, "Thông hiểu", "Xác định hóa trị của nguyên tố Cu trong các hợp chất:", [
            ("a", "Trong CuO, Cu có hóa trị II.", True),
            ("b", "Trong Cu2O, Cu có hóa trị I.", True),
            ("c", "Trong CuSO4, Cu có hóa trị II.", True),
            ("d", "Trong CuCl, Cu có hóa trị II.", False)
        ], "Trong CuCl, Cl có hóa trị I nên Cu có hóa trị I."),
        make_tf(3, "Vận dụng", "Cho các hợp chất: N2O, NO, NO2, N2O5:", [
            ("a", "Hóa trị của Nitrogen trong N2O là I.", True),
            ("b", "Hóa trị của Nitrogen trong NO là II.", True),
            ("c", "Hóa trị của Nitrogen trong NO2 là IV.", True),
            ("d", "Hóa trị của Nitrogen trong N2O5 là III.", False)
        ], "Trong N2O5, Nitrogen có hóa trị V."),
        make_tf(4, "Vận dụng", "Hợp chất đá vôi CaCO3 bị nung nóng tạo vôi sống CaO và khí CO2:", [
            ("a", "CaCO3, CaO, CO2 đều là các hợp chất.", True),
            ("b", "Trong cả CaCO3 và CaO, Calcium đều có hóa trị II.", True),
            ("c", "Trong cả CaCO3 và CO2, Carbon đều có hóa trị IV.", True),
            ("d", "Phản ứng nung đá vôi là hiện tượng biến đổi vật lí.", False)
        ], "Nung đá vôi sinh ra chất mới là biến đổi hóa học.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Hóa trị của nguyên tố Magnesium trong phân tử MgSO4 là bao nhiêu?", "II", "Mg có hóa trị II."),
        make_sa(2, "Thông hiểu", "Khối lượng phân tử của vôi sống (CaO) là bao nhiêu amu?", "56", "40 + 16 = 56 amu."),
        make_sa(3, "Vận dụng", "Hóa trị của nguyên tố Nitrogen trong phân tử khí NO2 là bao nhiêu?", "IV", "1 × a = 2 × II => a = IV."),
        make_sa(4, "Vận dụng", "Phần trăm khối lượng của Mg trong phân tử MgO (40 amu) là bao nhiêu phần trăm?", "60", "%Mg = 24 / 40 × 100% = 60%."),
        make_sa(5, "Vận dụng cao", "Lập CTHH của hợp chất tạo bởi sắt có hóa trị II và nhóm nitrat (NO3, hóa trị I). Số nguyên tử Oxygen có trong 1 phân tử hợp chất này là bao nhiêu?", "6", "Fe(NO3)2 có 2 × 3 = 6 nguyên tử O."),
        make_sa(6, "Vận dụng cao", "Một hợp chất có dạng X2O3 nặng 160 amu. Kí hiệu hóa học của nguyên tố X là gì?", "Fe", "2X + 48 = 160 => 2X = 112 => X = 56 (Iron, Fe).")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất tạo bởi Carbon và Hydrogen có tỉ lệ khối lượng mC : mH = 3 : 1. Khối lượng phân tử của hợp chất là 16 amu. Công thức phân tử của hợp chất là:", ["CH4", "C2H6", "C2H4", "C3H8"], 0, "mC = 16 × 3/4 = 12 amu (1C), mH = 4 amu (4H) => CH4."),
        make_vdc(2, "Quặng bauxite chứa thành phần chính là Al2O3. Để thu được 54 tấn kim loại nhôm (Al) nguyên chất từ Al2O3 tinh khiết, khối lượng Al2O3 cần dùng theo lý thuyết là:", ["102 tấn", "108 tấn", "150 tấn", "80 tấn"], 0, "Trong 102 tấn Al2O3 có 2 × 27 = 54 tấn Al => cần đúng 102 tấn Al2O3."),
        make_vdc(3, "Một hợp chất có công thức R(OH)3 nặng 78 amu. Tên gọi theo IUPAC của nguyên tố R là:", ["Aluminium", "Iron", "Chromium", "Boron"], 0, "R + 3 × 17 = 78 => R = 78 - 51 = 27 (Aluminium)."),
        make_vdc(4, "Một oxide của kim loại sắt có khối lượng phân tử là 232 amu và tỉ lệ số nguyên tử Fe : O là 3 : 4. Công thức phân tử của oxide này là:", ["Fe3O4", "Fe2O3", "FeO", "Fe4O3"], 0, "3 × 56 + 4 × 16 = 168 + 64 = 232 amu => Fe3O4 (oxit sắt từ).")
    ]
}

# ==============================================================================
# ÔN TẬP CUỐI CHƯƠNG II: PHÂN TỬ - LIÊN KẾT HÓA HỌC (5 ĐỀ ĐỘC LẬP 100%)
# ==============================================================================

# --- ĐỀ 1: Tổng hợp Chương II (Liên kết ion, đơn chất/hợp chất, CTHH AxBy) ---
exams["chem7_c2_rev_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Chất được tạo nên từ hai nguyên tố hóa học trở lên được gọi là:", ["Hợp chất", "Đơn chất", "Hỗn hợp", "Dung dịch"], 0, "Hợp chất tạo từ 2 nguyên tố trở lên."),
        make_mc(2, "Nhận biết", "Liên kết ion được hình thành do lực hút tĩnh điện giữa:", ["Ion dương và ion âm", "Hai ion dương", "Hai ion âm", "Nguyên tử và electron"], 0, "Lực hút tĩnh điện giữa cation (+) và anion (-)."),
        make_mc(3, "Nhận biết", "Trong phân tử hợp chất Al2O3, hóa trị của Aluminium là:", ["III", "II", "I", "IV"], 0, "Al có hóa trị III trong Al2O3."),
        make_mc(4, "Nhận biết", "Khối lượng phân tử của nước (H2O) là:", ["18 amu", "16 amu", "20 amu", "17 amu"], 0, "2 × 1 + 16 = 18 amu."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là đơn chất phi kim?", ["Khí nitrogen (N2)", "Đồng (Cu)", "Nhôm (Al)", "Vàng (Au)"], 0, "N2 là đơn chất phi kim."),
        make_mc(6, "Nhận biết", "Quy tắc octet chỉ ra rằng các nguyên tử có xu hướng đạt lớp ngoài cùng gồm:", ["8 electron", "2 electron", "18 electron", "6 electron"], 0, "Quy tắc 8 electron bền vững."),
        make_mc(7, "Thông hiểu", "Chất nào sau đây là hợp chất ion có nhiệt độ nóng chảy rất cao?", ["Sodium chloride (NaCl)", "Khí carbon dioxide (CO2)", "Nước (H2O)", "Cồn (C2H5OH)"], 0, "NaCl là hợp chất ion nóng chảy ở 801°C."),
        make_mc(8, "Thông hiểu", "Trong phân tử khí methane (CH4), liên kết giữa Carbon và Hydrogen là:", ["Liên kết cộng hóa trị", "Liên kết ion", "Liên kết kim loại", "Liên kết đôi"], 0, "Liên kết cộng hóa trị dùng chung electron."),
        make_mc(9, "Thông hiểu", "Lập CTHH của hợp chất tạo bởi Calcium (hóa trị II) và Oxygen (hóa trị II):", ["CaO", "Ca2O", "CaO2", "Ca2O2"], 0, "Cùng hóa trị II tỉ lệ 1 : 1 là CaO."),
        make_mc(10, "Thông hiểu", "Khối lượng phân tử của calcium carbonate (CaCO3) là:", ["100 amu", "80 amu", "120 amu", "90 amu"], 0, "40 + 12 + 48 = 100 amu."),
        make_mc(11, "Thông hiểu", "Hợp chất nào sau đây tan trong nước tạo thành dung dịch dẫn điện tốt?", ["Muối ăn (NaCl)", "Đường ăn", "Cồn", "Dầu ăn"], 0, "Dung dịch muối ăn phân li thành ion tự do dẫn điện."),
        make_mc(12, "Thông hiểu", "Hóa trị của nguyên tố Carbon trong hợp chất CO2 là:", ["IV", "II", "I", "VI"], 0, "Carbon có hóa trị IV trong CO2.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các chất: Cl2, Fe, H2O, CO2:", [
            ("a", "Cl2 và Fe là các đơn chất.", True),
            ("b", "H2O và CO2 là các hợp chất cộng hóa trị.", True),
            ("c", "Fe là kim loại dẫn điện và dẫn nhiệt tốt.", True),
            ("d", "Khối lượng phân tử của CO2 nhẹ hơn H2O.", False)
        ], "CO2 (44 amu) nặng hơn H2O (18 amu)."),
        make_tf(2, "Thông hiểu", "Về liên kết hóa học trong các chất:", [
            ("a", "NaCl có liên kết ion do Na nhường 1e và Cl nhận 1e.", True),
            ("b", "Phân tử O2 có liên kết đôi gồm 2 cặp electron dùng chung.", True),
            ("c", "Phân tử N2 có liên kết ba gồm 3 cặp electron dùng chung rất bền.", True),
            ("d", "Hợp chất ion có nhiệt độ sôi thấp hơn hợp chất cộng hóa trị.", False)
        ], "Hợp chất ion có nhiệt độ sôi cao hơn rất nhiều."),
        make_tf(3, "Vận dụng", "Cho các hợp chất: Na2O, Al2O3, SO3:", [
            ("a", "Sodium trong Na2O có hóa trị I.", True),
            ("b", "Aluminium trong Al2O3 có hóa trị III.", True),
            ("c", "Sulfur trong SO3 có hóa trị VI.", True),
            ("d", "Al2O3 là hợp chất cộng hóa trị ở thể khí.", False)
        ], "Al2O3 là hợp chất rắn khó nóng chảy."),
        make_tf(4, "Vận dụng", "Hợp chất có công thức phân tử là Ba(OH)2:", [
            ("a", "Gồm 3 nguyên tố: Ba, O, H.", True),
            ("b", "Barium có hóa trị II.", True),
            ("c", "Nhóm OH có hóa trị I.", True),
            ("d", "Khối lượng phân tử của hợp chất là 154 amu.", False)
        ], "Khối lượng phân tử = 137 + 2 × 17 = 171 amu.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khối lượng phân tử của khí ammonia (NH3) là bao nhiêu amu?", "17", "14 + 3 × 1 = 17 amu."),
        make_sa(2, "Thông hiểu", "Số cặp electron dùng chung trong phân tử khí hydrogen (H2) là bao nhiêu?", "1", "H2 có 1 liên kết đơn (1 cặp e)."),
        make_sa(3, "Vận dụng", "Hóa trị của sắt trong hợp chất Fe2O3 là bao nhiêu?", "III", "Iron có hóa trị III."),
        make_sa(4, "Vận dụng", "Khối lượng phân tử của copper(II) oxide (CuO) là bao nhiêu amu?", "80", "64 + 16 = 80 amu."),
        make_sa(5, "Vận dụng cao", "Phần trăm khối lượng của nguyên tố Carbon trong khí methane (CH4, 16 amu) là bao nhiêu phần trăm?", "75", "%C = 12 / 16 × 100% = 75%."),
        make_sa(6, "Vận dụng cao", "Hợp chất của nguyên tố R với Oxygen có dạng RO nặng 56 amu. Kí hiệu hóa học của R là gì?", "Ca", "R + 16 = 56 => R = 40 (Calcium, CaO).")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 3 nguyên tử Oxygen, nặng 160 amu. Nguyên tố X là:", ["Iron (Fe)", "Aluminium (Al)", "Chromium (Cr)", "Phosphorus (P)"], 0, "2X + 48 = 160 => 2X = 112 => X = 56 (Iron, Fe2O3)."),
        make_vdc(2, "Nguyên tử A có 3 electron lớp ngoài cùng, nguyên tử B có 6 electron lớp ngoài cùng. Công thức hợp chất tạo bởi A và B là:", ["A2B3", "AB", "AB2", "A3B2"], 0, "A nhường 3e (hóa trị III), B nhận 2e (hóa trị II) => A2B3."),
        make_vdc(3, "Cho biết tỉ lệ khối lượng của Sulfur và Oxygen trong phân tử khí sulfur dioxide (SO2) là:", ["1 : 1", "1 : 2", "2 : 1", "3 : 2"], 0, "mS : mO = 32 : (2 × 16) = 32 : 32 = 1 : 1."),
        make_vdc(4, "Một oxide kim loại có công thức M2O3, trong đó M chiếm 70% về khối lượng. Tên gọi theo IUPAC của kim loại M là:", ["Iron (Fe)", "Aluminium (Al)", "Chromium (Cr)", "Titanium (Ti)"], 0, "2M / (2M + 48) = 0,7 => 2M = 112 => M = 56 (Iron).")
    ]
}

# Đề 2, 3, 4, 5 của Ôn tập Chương II
exams["chem7_c2_rev_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Chất nào sau đây là đơn chất kim loại ở thể rắn có màu đỏ ánh kim dẫn điện rất tốt?", ["Copper (Đồng)", "Iron (Sắt)", "Aluminium (Nhôm)", "Silver (Bạc)"], 0, "Copper có màu đỏ ánh kim."),
        make_mc(2, "Nhận biết", "Trong phân tử hợp chất, liên kết cộng hóa trị được hình thành do:", ["Các cặp electron dùng chung", "Lực hút ion trái dấu", "Lực hút hạt nhân", "Sự nhường nhận electron"], 0, "Các cặp electron dùng chung."),
        make_mc(3, "Nhận biết", "Quy ước hóa trị của nguyên tố Hydrogen là:", ["I", "II", "III", "IV"], 0, "H luôn có hóa trị I."),
        make_mc(4, "Nhận biết", "Khối lượng phân tử của khí carbon dioxide (CO2) là:", ["44 amu", "28 amu", "32 amu", "16 amu"], 0, "12 + 2 × 16 = 44 amu."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là hợp chất?", ["Nước tinh khiết (H2O)", "Kim loại đồng", "Khí oxygen", "Kim cương"], 0, "H2O là hợp chất tạo bởi 2 nguyên tố H và O."),
        make_mc(6, "Nhận biết", "Số electron tối đa có ở lớp ngoài cùng của các nguyên tử (trừ He) là:", ["8 electron", "2 electron", "18 electron", "6 electron"], 0, "8 electron (quy tắc octet)."),
        make_mc(7, "Thông hiểu", "Trong hợp chất Fe2O3, hóa trị của Iron là:", ["III", "II", "I", "IV"], 0, "Iron có hóa trị III."),
        make_mc(8, "Thông hiểu", "Chất nào sau đây có liên kết ion?", ["Magnesium oxide (MgO)", "Nước (H2O)", "Khí methane (CH4)", "Khí ammonia (NH3)"], 0, "MgO là hợp chất ion giữa kim loại Mg và phi kim O."),
        make_mc(9, "Thông hiểu", "Lập CTHH của hợp chất tạo bởi Na(I) và SO4(II):", ["Na2SO4", "NaSO4", "Na(SO4)2", "Na2(SO4)3"], 0, "x/y = II/I = 2/1 => Na2SO4."),
        make_mc(10, "Thông hiểu", "Phân tử nào sau đây có liên kết đôi?", ["Oxygen (O2)", "Nitrogen (N2)", "Hydrogen (H2)", "Chlorine (Cl2)"], 0, "O2 có liên kết đôi O=O."),
        make_mc(11, "Thông hiểu", "Khối lượng phân tử của calcium oxide (CaO) là:", ["56 amu", "40 amu", "72 amu", "48 amu"], 0, "40 + 16 = 56 amu."),
        make_mc(12, "Thông hiểu", "Hóa trị của nhóm OH trong hợp chất Ba(OH)2 là:", ["I", "II", "III", "IV"], 0, "Nhóm OH có hóa trị I.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét phân tử axit clohiđric (HCl):", [
            ("a", "Là hợp chất cộng hóa trị.", True),
            ("b", "Cặp electron dùng chung lệch về phía Cl.", True),
            ("c", "Khối lượng phân tử là 36,5 amu.", True),
            ("d", "HCl ở nhiệt độ phòng là chất rắn kết tinh.", False)
        ], "HCl ở nhiệt độ phòng là chất khí."),
        make_tf(2, "Thông hiểu", "Về tính chất của hợp chất ion và cộng hóa trị:", [
            ("a", "Hợp chất ion có nhiệt độ nóng chảy cao.", True),
            ("b", "Dung dịch muối ăn dẫn điện được.", True),
            ("c", "Dung dịch đường ăn dẫn điện được.", False),
            ("d", "Khí CO2 là hợp chất cộng hóa trị.", True)
        ], "Dung dịch đường không dẫn điện."),
        make_tf(3, "Vận dụng", "Cho các hợp chất: H2S, SO2, SO3:", [
            ("a", "Sulfur trong H2S có hóa trị II.", True),
            ("b", "Sulfur trong SO2 có hóa trị IV.", True),
            ("c", "Sulfur trong SO3 có hóa trị VI.", True),
            ("d", "SO3 có khối lượng phân tử nhẹ hơn SO2.", False)
        ], "SO3 (80 amu) nặng hơn SO2 (64 amu)."),
        make_tf(4, "Vận dụng", "Hợp chất Al2(SO4)3:", [
            ("a", "Gồm 3 nguyên tố Al, S, O.", True),
            ("b", "Khối lượng phân tử là 342 amu.", True),
            ("c", "Al có hóa trị III, nhóm SO4 có hóa trị II.", True),
            ("d", "Chứa 12 nguyên tử Oxygen trong 1 phân tử.", True)
        ], "Có 3 × 4 = 12 nguyên tử O.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khối lượng phân tử của phân đạm urea CH4N2O là bao nhiêu amu?", "60", "60 amu."),
        make_sa(2, "Thông hiểu", "Hóa trị của nguyên tố Carbon trong khí CO là bao nhiêu?", "II", "Carbon hóa trị II."),
        make_sa(3, "Vận dụng", "Số cặp electron dùng chung trong phân tử N2 là bao nhiêu?", "3", "Liên kết ba có 3 cặp e dùng chung."),
        make_sa(4, "Vận dụng", "Khối lượng phân tử của NaCl là bao nhiêu amu? (Làm tròn 1 chữ số thập phân)", "58.5", "58,5 amu."),
        make_sa(5, "Vận dụng cao", "Phần trăm khối lượng của Oxygen trong phân tử SO2 (64 amu) là bao nhiêu phần trăm?", "50", "32/64 = 50%."),
        make_sa(6, "Vận dụng cao", "Một oxide kim loại R2O3 nặng 102 amu. Tên kim loại R là gì?", "Aluminium", "Al (27 amu).")
    ],
    "part4": [
        make_vdc(1, "Hợp chất A gồm 2 nguyên tử của nguyên tố X liên kết với 1 nguyên tử O và nặng 62 amu. X là nguyên tố nào?", ["Sodium (Na)", "Potassium (K)", "Lithium (Li)", "Copper (Cu)"], 0, "2X + 16 = 62 => X = 23 (Na)."),
        make_vdc(2, "Một hợp chất có phân tử gồm Cu(II) và nhóm SO4(II). Khối lượng phân tử của hợp chất là:", ["160 amu", "128 amu", "144 amu", "150 amu"], 0, "64 + 32 + 64 = 160 amu (CuSO4)."),
        make_vdc(3, "Nguyên tố R có hóa trị IV trong oxide RO2. Hợp chất khí của R với Hydrogen có dạng:", ["RH4", "RH2", "RH3", "RH"], 0, "Hóa trị với H = 8 - 4 = 4 => RH4 (như CH4, SiH4)."),
        make_vdc(4, "Phần trăm khối lượng của nguyên tố Nitrogen trong phân tử NH4NO3 là:", ["35%", "28%", "17,5%", "42%"], 0, "28 / 80 × 100% = 35%.")
    ]
}

# Đề 3, 4, 5 tiếp tục được hoàn thiện độc lập 100%
exams["chem7_c2_rev_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Phân tử là hạt đại diện cho chất và:", ["Thể hiện đầy đủ tính chất hóa học của chất", "Chỉ gồm các nguyên tử cùng loại", "Có kích thước bằng hạt nhân", "Không thể bị chia nhỏ trong mọi điều kiện"], 0, "Phân tử thể hiện đầy đủ tính chất hóa học."),
        make_mc(2, "Nhận biết", "Liên kết trong phân tử khí hydrogen (H2) là:", ["Liên kết cộng hóa trị đơn", "Liên kết ion", "Liên kết đôi", "Liên kết kim loại"], 0, "Liên kết đơn H-H."),
        make_mc(3, "Nhận biết", "Trong hợp chất, hóa trị của Oxygen luôn được lấy bằng:", ["II", "I", "III", "IV"], 0, "Hóa trị II."),
        make_mc(4, "Nhận biết", "Khối lượng phân tử của sulfur trioxide (SO3) là:", ["80 amu", "64 amu", "48 amu", "96 amu"], 0, "32 + 3 × 16 = 80 amu."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là đơn chất phi kim ở thể rắn có màu vàng?", ["Sulfur (Lưu huỳnh)", "Photpho", "Than chì", "Kim cương"], 0, "Sulfur là chất rắn màu vàng."),
        make_mc(6, "Nhận biết", "Khi nguyên tử nhận thêm electron, nó trở thành:", ["Anion (ion âm)", "Cation (ion dương)", "Phân tử", "Khí hiếm"], 0, "Nhận thêm electron mang điện âm trở thành anion."),
        make_mc(7, "Thông hiểu", "Trong hợp chất Al(OH)3, Aluminium có hóa trị là:", ["III", "II", "I", "IV"], 0, "Al có hóa trị III."),
        make_mc(8, "Thông hiểu", "Chất nào sau đây có nhiệt độ nóng chảy cao nhất?", ["Calcium oxide (CaO)", "Nước (H2O)", "Cồn", "Đường mía"], 0, "CaO là hợp chất ion có nhiệt độ nóng chảy rất cao (~2572°C)."),
        make_mc(9, "Thông hiểu", "Lập CTHH của hợp chất tạo bởi Mg(II) và Cl(I):", ["MgCl2", "MgCl", "Mg2Cl", "MgCl3"], 0, "MgCl2."),
        make_mc(10, "Thông hiểu", "Phân tử khí nào sau đây có liên kết ba rất bền vững?", ["Nitrogen (N2)", "Oxygen (O2)", "Hydrogen (H2)", "Chlorine (Cl2)"], 0, "N2 có liên kết ba."),
        make_mc(11, "Thông hiểu", "Khối lượng phân tử của hợp chất NaOH là:", ["40 amu", "39 amu", "58,5 amu", "42 amu"], 0, "23 + 16 + 1 = 40 amu."),
        make_mc(12, "Thông hiểu", "Hóa trị của nhóm CO3 trong CaCO3 là:", ["II", "I", "III", "IV"], 0, "Nhóm CO3 có hóa trị II.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các chất: Fe, Cu, H2SO4, NaCl:", [
            ("a", "Fe và Cu là các đơn chất kim loại.", True),
            ("b", "NaCl là hợp chất ion.", True),
            ("c", "H2SO4 là hợp chất cộng hóa trị có khối lượng phân tử 98 amu.", True),
            ("d", "NaCl ở thể rắn dẫn điện rất tốt.", False)
        ], "NaCl thể rắn không dẫn điện."),
        make_tf(2, "Thông hiểu", "Xét phân tử nước H2O:", [
            ("a", "Gồm 2 nguyên tử H và 1 nguyên tử O.", True),
            ("b", "Liên kết O-H là liên kết cộng hóa trị.", True),
            ("c", "Khối lượng phân tử là 18 amu.", True),
            ("d", "Nước sôi ở 0°C và đóng băng ở 100°C.", False)
        ], "Nước sôi ở 100°C và đóng băng ở 0°C."),
        make_tf(3, "Vận dụng", "Cho các oxide của carbon: CO và CO2:", [
            ("a", "Trong CO, Carbon có hóa trị II.", True),
            ("b", "Trong CO2, Carbon có hóa trị IV.", True),
            ("c", "CO là khí không màu, rất độc.", True),
            ("d", "CO2 nhẹ hơn CO.", False)
        ], "CO2 (44 amu) nặng hơn CO (28 amu)."),
        make_tf(4, "Vận dụng", "Hợp chất K2O:", [
            ("a", "Tạo bởi kim loại K và phi kim O.", True),
            ("b", "Có liên kết ion giữa ion K+ và O2-.", True),
            ("c", "Khối lượng phân tử là 94 amu (2 × 39 + 16).", True),
            ("d", "K trong hợp chất có hóa trị II.", False)
        ], "K có hóa trị I.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khối lượng phân tử của ozone (O3) là bao nhiêu amu?", "48", "3 × 16 = 48 amu."),
        make_sa(2, "Thông hiểu", "Hóa trị của Sulfur trong hợp chất SO2 là bao nhiêu?", "IV", "Hóa trị IV."),
        make_sa(3, "Vận dụng", "Trong phân tử O2 có bao nhiêu cặp electron dùng chung?", "2", "2 cặp e dùng chung."),
        make_sa(4, "Vận dụng", "Khối lượng phân tử của magnesium chloride (MgCl2) là bao nhiêu amu?", "95", "24 + 71 = 95 amu."),
        make_sa(5, "Vận dụng cao", "Phần trăm khối lượng của nguyên tố Hydrogen trong CH4 là bao nhiêu phần trăm?", "25", "4/16 = 25%."),
        make_sa(6, "Vận dụng cao", "Một hợp chất có dạng XO nặng 56 amu. Kí hiệu hóa học của X là gì?", "Ca", "Ca (40 amu).")
    ],
    "part4": [
        make_vdc(1, "Hợp chất tạo bởi nguyên tố R (hóa trị III) và Oxygen có công thức là:", ["R2O3", "RO3", "R3O2", "RO"], 0, "R2O3."),
        make_vdc(2, "Một chất khí X có tỉ khối so với khí hydrogen (H2) là 17. Khối lượng phân tử của X là:", ["34 amu (H2S)", "17 amu", "28 amu", "44 amu"], 0, "17 × 2 = 34 amu (H2S)."),
        make_vdc(3, "Tỉ lệ khối lượng của C và H trong phân tử C2H2 là:", ["12 : 1", "6 : 1", "24 : 2", "3 : 1"], 0, "24 : 2 = 12 : 1."),
        make_vdc(4, "Hợp chất A gồm nguyên tố M và Oxygen trong đó M chiếm 72,41% về khối lượng. Biết khối lượng phân tử là 232 amu. Công thức của A là:", ["Fe3O4", "Fe2O3", "FeO", "Al2O3"], 0, "Fe3O4.")
    ]
}

exams["chem7_c2_rev_test4"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Đơn chất kim loại nào sau đây ở thể lỏng ở nhiệt độ thường?", ["Mercury (Hg)", "Copper (Cu)", "Iron (Fe)", "Gold (Au)"], 0, "Mercury là kim loại lỏng."),
        make_mc(2, "Nhận biết", "Trong phân tử NaCl, liên kết giữa các ion Na+ và Cl- là:", ["Liên kết ion", "Liên kết cộng hóa trị", "Liên kết kim loại", "Liên kết hidro"], 0, "Liên kết ion."),
        make_mc(3, "Nhận biết", "Nguyên tố Hydrogen trong hợp chất luôn có hóa trị là:", ["I", "II", "III", "IV"], 0, "Hóa trị I."),
        make_mc(4, "Nhận biết", "Khối lượng phân tử của khí chlorine (Cl2) là:", ["71 amu", "35,5 amu", "17 amu", "142 amu"], 0, "71 amu."),
        make_mc(5, "Nhận biết", "Hợp chất nào sau đây là thành phần chính của đá vôi?", ["CaCO3", "CaO", "Ca(OH)2", "CaCl2"], 0, "CaCO3."),
        make_mc(6, "Nhận biết", "Quy tắc octet là xu hướng đạt lớp ngoài cùng gồm:", ["8 electron", "2 electron", "18 electron", "10 electron"], 0, "8 electron."),
        make_mc(7, "Thông hiểu", "Trong hợp chất FeO, hóa trị của Iron là:", ["II", "III", "I", "IV"], 0, "Iron hóa trị II."),
        make_mc(8, "Thông hiểu", "Chất nào sau đây là hợp chất cộng hóa trị ở thể khí?", ["Methane (CH4)", "Muối ăn (NaCl)", "Đá vôi (CaCO3)", "Vôi sống (CaO)"], 0, "CH4 thể khí."),
        make_mc(9, "Thông hiểu", "Lập CTHH của hợp chất gồm Al(III) và Cl(I):", ["AlCl3", "AlCl", "Al3Cl", "Al2Cl3"], 0, "AlCl3."),
        make_mc(10, "Thông hiểu", "Phân tử khí nào sau đây có liên kết đôi?", ["O2", "N2", "H2", "Cl2"], 0, "O2."),
        make_mc(11, "Thông hiểu", "Khối lượng phân tử của sulfuric acid (H2SO4) là:", ["98 amu", "96 amu", "100 amu", "80 amu"], 0, "98 amu."),
        make_mc(12, "Thông hiểu", "Hóa trị của nhóm SO4 trong hợp chất Na2SO4 là:", ["II", "I", "III", "IV"], 0, "Nhóm SO4 có hóa trị II.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét phân tử khí carbon dioxide (CO2):", [
            ("a", "Là hợp chất cộng hóa trị.", True),
            ("b", "Có 2 liên kết đôi giữa C và 2 nguyên tử O.", True),
            ("c", "Khối lượng phân tử là 44 amu.", True),
            ("d", "Khí CO2 duy trì sự cháy rất tốt.", False)
        ], "CO2 không duy trì sự cháy, dùng để dập lửa."),
        make_tf(2, "Thông hiểu", "Về các đơn chất và hợp chất trong tự nhiên:", [
            ("a", "Khí oxygen là đơn chất cần cho sự hô hấp.", True),
            ("b", "Nước là hợp chất phổ biến nhất trên bề mặt Trái Đất.", True),
            ("c", "Muối ăn NaCl là hợp chất ion.", True),
            ("d", "Tất cả các kim loại đều nhẹ hơn nước.", False)
        ], "Hầu hết kim loại đều nặng hơn nước (Fe, Cu, Pb...)."),
        make_tf(3, "Vận dụng", "Cho các oxide: Na2O, MgO, Al2O3:", [
            ("a", "Đều là oxide của kim loại.", True),
            ("b", "Hóa trị của kim loại lần lượt là I, II, III.", True),
            ("c", "Đều là hợp chất ion rắn khó nóng chảy.", True),
            ("d", "Al2O3 có khối lượng phân tử nhẹ nhất trong dãy.", False)
        ], "Al2O3 (102 amu) nặng nhất trong dãy."),
        make_tf(4, "Vận dụng", "Hợp chất Cu(OH)2:", [
            ("a", "Cu có hóa trị II.", True),
            ("b", "Nhóm OH có hóa trị I.", True),
            ("c", "Khối lượng phân tử là 98 amu (64 + 2 × 17).", True),
            ("d", "Tan vô hạn trong nước tạo dung dịch màu đỏ.", False)
        ], "Cu(OH)2 là kết tủa màu xanh lam không tan trong nước.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khối lượng phân tử của khí methane (CH4) là bao nhiêu amu?", "16", "16 amu."),
        make_sa(2, "Thông hiểu", "Hóa trị của nguyên tố Carbon trong CO2 là bao nhiêu?", "IV", "Hóa trị IV."),
        make_sa(3, "Vận dụng", "Số liên kết đơn trong phân tử nước (H2O) là bao nhiêu?", "2", "2 liên kết O-H."),
        make_sa(4, "Vận dụng", "Khối lượng phân tử của potassium hydroxide (KOH) là bao nhiêu amu?", "56", "39 + 17 = 56 amu."),
        make_sa(5, "Vận dụng cao", "Phần trăm khối lượng của nguyên tố H trong phân tử H2O là bao nhiêu phần trăm? (Làm tròn 1 chữ số thập phân)", "11.1", "11,1%."),
        make_sa(6, "Vận dụng cao", "Một oxide kim loại MO nặng 80 amu. Kí hiệu của M là gì?", "Cu", "Cu (64 amu, CuO).")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 5 nguyên tử Oxygen, nặng 142 amu. X là nguyên tố nào?", ["Phosphorus (P)", "Nitrogen (N)", "Arsenic (As)", "Vanadium (V)"], 0, "2X + 80 = 142 => X = 31 (P)."),
        make_vdc(2, "Chất nào sau đây khi hòa tan vào nước tạo dung dịch dẫn điện?", ["NaCl", "Đường", "Cồn", "Dầu ăn"], 0, "NaCl."),
        make_vdc(3, "Phần trăm khối lượng của Carbon trong phân tử CaCO3 (100 amu) là:", ["12%", "40%", "48%", "20%"], 0, "12%."),
        make_vdc(4, "Hợp chất khí X của Sulfur với Hydrogen có công thức H2S. Hóa trị của Sulfur trong hợp chất này là:", ["II", "IV", "VI", "I"], 0, "Hóa trị II.")
    ]
}

exams["chem7_c2_rev_test5"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Chất nào sau đây là đơn chất phi kim ở thể khí duy trì sự sống?", ["Oxygen (O2)", "Nitrogen (N2)", "Carbon (C)", "Iron (Fe)"], 0, "O2."),
        make_mc(2, "Nhận biết", "Liên kết trong phân tử nước (H2O) là:", ["Liên kết cộng hóa trị", "Liên kết ion", "Liên kết kim loại", "Liên kết đôi"], 0, "Liên kết cộng hóa trị."),
        make_mc(3, "Nhận biết", "Quy ước hóa trị của Oxygen trong hợp chất luôn là:", ["II", "I", "III", "IV"], 0, "Hóa trị II."),
        make_mc(4, "Nhận biết", "Khối lượng phân tử của khí hydrogen (H2) là:", ["2 amu", "1 amu", "4 amu", "16 amu"], 0, "2 amu."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là hợp chất vô cơ?", ["Muối ăn (NaCl)", "Thanh nhôm", "Khí oxygen", "Than chì"], 0, "NaCl."),
        make_mc(6, "Nhận biết", "Quy tắc octet quy ước lớp ngoài cùng bền vững có:", ["8 electron (riêng He có 2e)", "2 electron cho mọi nguyên tố", "18 electron", "6 electron"], 0, "8 electron."),
        make_mc(7, "Thông hiểu", "Trong hợp chất Fe2(SO4)3, hóa trị của Iron là:", ["III", "II", "I", "IV"], 0, "Iron hóa trị III."),
        make_mc(8, "Thông hiểu", "Chất nào sau đây có nhiệt độ nóng chảy cao trên 800°C?", ["Sodium chloride (NaCl)", "Nước", "Cồn", "Đường"], 0, "NaCl nóng chảy ở 801°C."),
        make_mc(9, "Thông hiểu", "Lập CTHH của hợp chất gồm Ca(II) và OH(I):", ["Ca(OH)2", "CaOH", "Ca2OH", "Ca(OH)3"], 0, "Ca(OH)2."),
        make_mc(10, "Thông hiểu", "Phân tử nào sau đây có liên kết ba N≡N rất bền vững?", ["Nitrogen (N2)", "Oxygen (O2)", "Hydrogen (H2)", "Chlorine (Cl2)"], 0, "N2."),
        make_mc(11, "Thông hiểu", "Khối lượng phân tử của barium sulfate (BaSO4) là:", ["233 amu", "137 amu", "96 amu", "200 amu"], 0, "137 + 32 + 64 = 233 amu."),
        make_mc(12, "Thông hiểu", "Hóa trị của nhóm PO4 trong Ca3(PO4)2 là:", ["III", "II", "I", "IV"], 0, "Nhóm PO4 có hóa trị III.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các hợp chất: H2O, CO2, NH3, CH4:", [
            ("a", "Đều là hợp chất cộng hóa trị.", True),
            ("b", "Đều được tạo bởi các nguyên tố phi kim.", True),
            ("c", "CH4 có khối lượng phân tử nhẹ nhất (16 amu).", True),
            ("d", "Tất cả các chất này đều dẫn điện ở thể lỏng.", False)
        ], "Không dẫn điện."),
        make_tf(2, "Thông hiểu", "Về liên kết ion trong hợp chất:", [
            ("a", "Hình thành giữa kim loại điển hình và phi kim điển hình.", True),
            ("b", "Do lực hút tĩnh điện giữa các ion mang điện trái dấu.", True),
            ("c", "Có nhiệt độ nóng chảy và nhiệt độ sôi cao.", True),
            ("d", "Các ion không thể tách rời khi hòa tan trong nước.", False)
        ], "Khi tan trong nước các ion phân li tự do."),
        make_tf(3, "Vận dụng", "Cho các hợp chất: Al2O3, CuO, Na2O:", [
            ("a", "Al trong Al2O3 có hóa trị III.", True),
            ("b", "Cu trong CuO có hóa trị II.", True),
            ("c", "Na trong Na2O có hóa trị I.", True),
            ("d", "Na2O có khối lượng phân tử lớn hơn Al2O3.", False)
        ], "Na2O (62 amu) nhẹ hơn Al2O3 (102 amu)."),
        make_tf(4, "Vận dụng", "Hợp chất BaCl2:", [
            ("a", "Là hợp chất ion.", True),
            ("b", "Ba có hóa trị II, Cl có hóa trị I.", True),
            ("c", "Khối lượng phân tử là 208 amu (137 + 71).", True),
            ("d", "Không tan trong nước.", False)
        ], "BaCl2 tan rất tốt trong nước.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khối lượng phân tử của glucose (C6H12O6) là bao nhiêu amu?", "180", "180 amu."),
        make_sa(2, "Thông hiểu", "Hóa trị của Carbon trong hợp chất CH4 là bao nhiêu?", "IV", "Hóa trị IV."),
        make_sa(3, "Vận dụng", "Số cặp electron dùng chung trong phân tử Cl2 là bao nhiêu?", "1", "1 cặp e."),
        make_sa(4, "Vận dụng", "Khối lượng phân tử của copper(II) sulfate (CuSO4) là bao nhiêu amu?", "160", "160 amu."),
        make_sa(5, "Vận dụng cao", "Phần trăm khối lượng của nguyên tố Oxygen trong phân tử CO2 (44 amu) xấp xỉ bằng bao nhiêu phần trăm? (Làm tròn đến hàng đơn vị)", "73", "32/44 = 72,7% ≈ 73%."),
        make_sa(6, "Vận dụng cao", "Một oxide kim loại M2O3 nặng 102 amu. Kí hiệu hóa học của M là gì?", "Al", "Al (27 amu).")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất có phân tử gồm 1 nguyên tử nguyên tố X liên kết với 2 nguyên tử O và nặng 64 amu. X là nguyên tố nào?", ["Sulfur (S)", "Carbon (C)", "Silicon (Si)", "Nitrogen (N)"], 0, "SO2 (32 amu)."),
        make_vdc(2, "Phân tử chất nào sau đây có tổng số electron tham gia liên kết là 4 hạt (2 cặp electron)?", ["Oxygen (O2)", "Nitrogen (N2)", "Hydrogen (H2)", "Chlorine (Cl2)"], 0, "O2 có liên kết đôi (4 hạt e)."),
        make_vdc(3, "Phần trăm khối lượng của nguyên tố S trong phân tử FeS2 xấp xỉ bằng:", ["53,33%", "46,67%", "60%", "36,36%"], 0, "64 / (56 + 64) × 100% = 64 / 120 × 100% ≈ 53,33%."),
        make_vdc(4, "Hợp chất ion tạo bởi nguyên tố kim loại X (Z = 11) và nguyên tố phi kim Y (Z = 17) có công thức là:", ["XY (NaCl)", "X2Y", "XY2", "X2Y3"], 0, "NaCl (XY).")
    ]
}

print(f"🎉 Hoàn thành xuất sắc 100% toàn bộ 28 đề thi Hóa học 7 độc lập! Tổng số đề: {len(exams)} đề.")
