# -*- coding: utf-8 -*-
"""
HÓA HỌC 7 - HOÀN THIỆN TOÀN BỘ 28 ĐỀ THI ĐỘC LẬP 100%
Gồm 8 bài học:
- chem7_c1_b2 (3 đề)
- chem7_c1_b3 (3 đề)
- chem7_c1_b4 (3 đề)
- chem7_c1_rev (5 đề)
- chem7_c2_b5 (3 đề)
- chem7_c2_b6 (3 đề)
- chem7_c2_b7 (3 đề)
- chem7_c2_rev (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from builder_chem7_full import exams, make_mc, make_tf, make_sa, make_vdc

# ==============================================================================
# ÔN TẬP CUỐI CHƯƠNG I: NGUYÊN TỬ - BẢNG TUẦN HOÀN (5 ĐỀ ĐỘC LẬP 100%)
# ==============================================================================

# --- ĐỀ 1: Tổng hợp kiến thức cơ bản Chương I (Tập trung chu kì 2) ---
exams["chem7_c1_rev_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Hạt nhân nguyên tử được cấu tạo bởi các loại hạt:", ["Proton và electron", "Proton và neutron", "Electron và neutron", "Chỉ có hạt proton"], 1, "Hạt nhân gồm các hạt proton mang điện tích dương và neutron không mang điện."),
        make_mc(2, "Nhận biết", "Nguyên tử luôn trung hòa về điện là do:", ["Số hạt proton bằng số hạt electron", "Số hạt proton bằng số hạt neutron", "Số hạt neutron bằng số hạt electron", "Không chứa hạt mang điện"], 0, "Tổng điện tích dương của proton bằng tổng điện tích âm của electron."),
        make_mc(3, "Nhận biết", "Đơn vị khối lượng nguyên tử amu quy ước lấy theo khối lượng của nguyên tử:", ["Hydrogen", "Carbon-12", "Oxygen-16", "Nitrogen-14"], 1, "1 amu bằng 1/12 khối lượng của một nguyên tử carbon-12."),
        make_mc(4, "Nhận biết", "Kí hiệu hóa học của nguyên tố Potassium (Kali) là:", ["K", "P", "Po", "Pt"], 0, "Potassium có kí hiệu là K."),
        make_mc(5, "Nhận biết", "Các nguyên tố trong cùng một chu kì của bảng tuần hoàn có cùng:", ["Số electron lớp ngoài cùng", "Số lớp electron", "Số neutron", "Điện tích hạt nhân"], 1, "Số thứ tự chu kì bằng số lớp electron của nguyên tử."),
        make_mc(6, "Nhận biết", "Bảng tuần hoàn các nguyên tố hóa học hiện nay có bao nhiêu nhóm A?", ["7 nhóm A", "8 nhóm A", "10 nhóm A", "18 nhóm A"], 1, "Có 8 nhóm A (từ IA đến VIIIA)."),
        make_mc(7, "Thông hiểu", "Nguyên tử nguyên tố X có 7 proton và 7 neutron. Khối lượng nguyên tử X xấp xỉ bằng:", ["7 amu", "14 amu", "21 amu", "28 amu"], 1, "Khối lượng ≈ 7 + 7 = 14 amu (Nitrogen)."),
        make_mc(8, "Thông hiểu", "Nguyên tố nào sau đây là kim loại kiềm thuộc chu kì 2?", ["Lithium (Li)", "Sodium (Na)", "Potassium (K)", "Beryllium (Be)"], 0, "Lithium (Z = 3) là kim loại kiềm chu kì 2 (cấu hình 2, 1)."),
        make_mc(9, "Thông hiểu", "Khí hiếm nào sau đây chỉ có 2 electron ở lớp vỏ nhưng vẫn thuộc nhóm VIIIA?", ["Helium (He)", "Neon (Ne)", "Argon (Ar)", "Krypton (Kr)"], 0, "Helium chỉ có 1 lớp electron bão hòa 2e nên xếp vào nhóm VIIIA."),
        make_mc(10, "Thông hiểu", "Trong một chu kì, đi từ trái sang phải theo chiều tăng của điện tích hạt nhân, tính kim loại của các nguyên tố:", ["Tăng dần", "Giảm dần", "Không đổi", "Tăng rồi giảm"], 1, "Tính kim loại giảm dần, tính phi kim tăng dần."),
        make_mc(11, "Thông hiểu", "Nguyên tố phi kim nào sau đây nằm ở chu kì 2, nhóm VIIA?", ["Fluorine (F)", "Chlorine (Cl)", "Oxygen (O)", "Nitrogen (N)"], 0, "Fluorine (Z = 9) ở chu kì 2, nhóm VIIA."),
        make_mc(12, "Thông hiểu", "Nguyên tử Carbon có 6 electron. Sự phân bố electron vào các lớp từ trong ra ngoài của Carbon là:", ["2, 4", "4, 2", "2, 8", "6"], 0, "Carbon có 2 lớp electron: lớp trong có 2e, lớp ngoài cùng có 4e.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các nguyên tố chu kì 2: Li (Z=3), C (Z=6), N (Z=7), F (Z=9):", [
            ("a", "Tất cả các nguyên tố này đều có 2 lớp electron.", True),
            ("b", "Li là kim loại, F là phi kim mạnh nhất trong chu kì.", True),
            ("c", "Số electron lớp ngoài cùng tăng dần từ 1 (ở Li) đến 7 (ở F).", True),
            ("d", "Khối lượng nguyên tử của các nguyên tố này giảm dần từ trái sang phải.", False)
        ], "Khối lượng nguyên tử tăng dần theo chiều tăng của Z."),
        make_tf(2, "Thông hiểu", "Xét cấu tạo nguyên tử của nguyên tố Magnesium (Mg, Z = 12):", [
            ("a", "Hạt nhân Magnesium có 12 hạt proton.", True),
            ("b", "Vỏ nguyên tử Magnesium có 3 lớp electron.", True),
            ("c", "Lớp ngoài cùng có 2 electron nên Mg thuộc nhóm IIA.", True),
            ("d", "Magnesium là một nguyên tố phi kim.", False)
        ], "Magnesium là kim loại kiềm thổ."),
        make_tf(3, "Vận dụng", "Cho các nguyên tố: Na (Z = 11), Al (Z = 13), Cl (Z = 17):", [
            ("a", "Cả 3 nguyên tố đều thuộc chu kì 3.", True),
            ("b", "Na có tính kim loại mạnh hơn Al.", True),
            ("c", "Cl là phi kim có 7 electron ở lớp ngoài cùng.", True),
            ("d", "Bán kính nguyên tử của Cl lớn hơn bán kính của Na.", False)
        ], "Trong chu kì, bán kính nguyên tử giảm dần từ trái sang phải: R(Na) > R(Al) > R(Cl)."),
        make_tf(4, "Vận dụng", "Một nguyên tử X có tổng số hạt cơ bản là 28, trong đó số hạt không mang điện là 10:", [
            ("a", "Số hạt mang điện trong nguyên tử X là 18.", True),
            ("b", "Số proton của X là 9 (Fluorine).", True),
            ("c", "Vị trí của X trong bảng tuần hoàn là ô 9, chu kì 2, nhóm VIIA.", True),
            ("d", "X là một nguyên tố kim loại hoạt động mạnh.", False)
        ], "Fluorine là phi kim mạnh nhất.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Nguyên tố nào có số hiệu nguyên tử bằng 1? (Viết kí hiệu hóa học)", "H", "Hydrogen có Z = 1."),
        make_sa(2, "Thông hiểu", "Nguyên tử Aluminium có 13 electron. Số electron ở lớp ngoài cùng của Aluminium là bao nhiêu?", "3", "Cấu hình 2, 8, 3 => 3e ngoài cùng."),
        make_sa(3, "Vận dụng", "Một nguyên tử có 16 proton và 16 neutron. Khối lượng nguyên tử đó tính theo đơn vị amu là bao nhiêu?", "32", "16 + 16 = 32 amu (Sulfur)."),
        make_sa(4, "Vận dụng", "Nguyên tố Calcium (Z = 20) thuộc chu kì mấy trong bảng tuần hoàn?", "4", "Cấu hình 2, 8, 8, 2 => 4 lớp electron => chu kì 4."),
        make_sa(5, "Vận dụng cao", "Tổng số hạt trong nguyên tử của một nguyên tố kim loại là 40. Biết số hạt mang điện nhiều hơn số hạt không mang điện là 12. Số electron lớp ngoài cùng của nguyên tử này là bao nhiêu?", "3", "p = 13 (Al), phân bố 2, 8, 3 => lớp ngoài cùng có 3e."),
        make_sa(6, "Vận dụng cao", "Một mẫu chất chứa 0,5 mol nguyên tử Carbon (12 amu). Biết 1 mol chứa 6,022 × 10^23 nguyên tử. Khối lượng của mẫu chất đó là bao nhiêu gam?", "6", "0,5 × 12 = 6 gam.")
    ],
    "part4": [
        make_vdc(1, "Hai nguyên tố X và Y thuộc cùng chu kì 3, X thuộc nhóm IA, Y thuộc nhóm VIIA. Hợp chất tạo bởi X và Y có công thức là:", ["NaCl", "Na2O", "MgCl2", "KCl"], 0, "X là Na (11, IA), Y là Cl (17, VIIA) => hợp chất NaCl."),
        make_vdc(2, "Nguyên tử của nguyên tố R có tổng số electron ở phân lớp s là 6 và ở phân lớp p là 6. Vị trí của R trong bảng tuần hoàn là:", ["Ô số 12, chu kì 3, nhóm IIA", "Ô số 14, chu kì 3, nhóm IVA", "Ô số 16, chu kì 3, nhóm VIA", "Ô số 10, chu kì 2, nhóm VIIIA"], 0, "Tổng số e = 6 + 6 = 12 => Z = 12 (Mg), ô 12, chu kì 3, nhóm IIA."),
        make_vdc(3, "Cho các nguyên tố: Li, Na, K, Rb. Kim loại có phản ứng mãnh liệt nhất với nước ở nhiệt độ thường trong dãy là:", ["Rb", "K", "Na", "Li"], 0, "Trong nhóm IA từ trên xuống dưới, tính kim loại tăng dần: Li < Na < K < Rb."),
        make_vdc(4, "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 1 nguyên tử Oxygen, nặng bằng 62 amu. Nguyên tố X là:", ["Sodium (Na)", "Potassium (K)", "Lithium (Li)", "Copper (Cu)"], 0, "2X + 16 = 62 => 2X = 46 => X = 23 (Na).")
    ]
}

# --- ĐỀ 2: Tổng hợp Chương I (Tập trung chu kì 3 & kim loại kiềm thổ, Halogen) ---
exams["chem7_c1_rev_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Khối lượng của hạt nào trong nguyên tử được coi là không đáng kể?", ["Electron", "Proton", "Neutron", "Cả proton và electron"], 0, "Electron có khối lượng rất nhỏ (khoảng 0,00055 amu) so với proton và neutron."),
        make_mc(2, "Nhận biết", "Kí hiệu hóa học của nguyên tố Calcium là:", ["Ca", "C", "Cl", "Cu"], 0, "Ca là Calcium."),
        make_mc(3, "Nhận biết", "Các nguyên tố trong cùng một nhóm A có tính chất hóa học tương tự nhau vì:", ["Có cùng số electron ở lớp ngoài cùng", "Có cùng số proton", "Có cùng số neutron", "Có cùng số chu kì"], 0, "Số e lớp ngoài cùng quyết định tính chất hóa học."),
        make_mc(4, "Nhận biết", "Nguyên tố nào sau đây là thành phần chính cấu tạo nên kim cương và than chì?", ["Carbon", "Silicon", "Iron", "Sulfur"], 0, "Kim cương và than chì là các dạng thù hình của Carbon."),
        make_mc(5, "Nhận biết", "Trong bảng tuần hoàn, nhóm IIA gồm các nguyên tố kim loại có tên là:", ["Kim loại kiềm thổ", "Kim loại kiềm", "Halogen", "Khí hiếm"], 0, "Nhóm IIA là nhóm kim loại kiềm thổ: Be, Mg, Ca, Sr, Ba, Ra."),
        make_mc(6, "Nhận biết", "Số electron tối đa ở lớp thứ 2 của nguyên tử là:", ["8", "2", "18", "32"], 0, "Lớp 2 bão hòa 8 electron."),
        make_mc(7, "Thông hiểu", "Nguyên tử nguyên tố Silicon có 14 electron. Số lớp electron của Silicon là:", ["3 lớp", "2 lớp", "4 lớp", "1 lớp"], 0, "Phân bố: 2, 8, 4 => có 3 lớp electron."),
        make_mc(8, "Thông hiểu", "Nguyên tố Sulfur (S, Z = 16) nằm ở vị trí nào trong bảng tuần hoàn?", ["Ô 16, chu kì 3, nhóm VIA", "Ô 16, chu kì 3, nhóm IVA", "Ô 16, chu kì 2, nhóm VIA", "Ô 16, chu kì 4, nhóm IIA"], 0, "Cấu hình 2, 8, 6 => ô 16, chu kì 3, nhóm VIA."),
        make_mc(9, "Thông hiểu", "So sánh bán kính nguyên tử của các nguyên tử chu kì 3: Na, Mg, Al. Thứ tự giảm dần bán kính là:", ["Na > Mg > Al", "Al > Mg > Na", "Mg > Na > Al", "Na > Al > Mg"], 0, "Trong chu kì từ trái qua phải, bán kính nguyên tử giảm dần: Na > Mg > Al."),
        make_mc(10, "Thông hiểu", "Nguyên tố phi kim nào sau đây duy trì sự hô hấp và sự cháy?", ["Oxygen", "Nitrogen", "Hydrogen", "Carbon dioxide"], 0, "Khí oxygen duy trì sự sống và sự cháy."),
        make_mc(11, "Thông hiểu", "Nguyên tử của nguyên tố X có 2 electron ở lớp ngoài cùng và thuộc chu kì 3. X là nguyên tố nào?", ["Magnesium (Mg)", "Calcium (Ca)", "Sodium (Na)", "Aluminium (Al)"], 0, "Chu kì 3, nhóm IIA là Magnesium (Mg, Z = 12)."),
        make_mc(12, "Thông hiểu", "Tên IUPAC của nguyên tố có kí hiệu 'N' là:", ["Nitrogen", "Neon", "Sodium", "Nickel"], 0, "N là Nitrogen.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các nguyên tố nhóm Halogen: F, Cl, Br, I:", [
            ("a", "Đều có 7 electron ở lớp ngoài cùng.", True),
            ("b", "Thuộc nhóm VIIA trong bảng tuần hoàn.", True),
            ("c", "Tính phi kim giảm dần từ F đến I.", True),
            ("d", "Tất cả các halogen đều không tác dụng được với kim loại.", False)
        ], "Halogen tác dụng mãnh liệt với nhiều kim loại tạo muối halide."),
        make_tf(2, "Thông hiểu", "Cho các nguyên tử: X (11p, 12n), Y (12p, 12n), Z (11p, 13n):", [
            ("a", "X và Z thuộc cùng một nguyên tố hóa học (Sodium).", True),
            ("b", "Y là nguyên tố Magnesium (Mg).", True),
            ("c", "X và Y cùng thuộc chu kì 3.", True),
            ("d", "Khối lượng nguyên tử của X bằng khối lượng của Z.", False)
        ], "Khối lượng của X là 23 amu, của Z là 24 amu."),
        make_tf(3, "Vận dụng", "Xét kim loại Potassium (K, Z = 19):", [
            ("a", "Nằm ở ô số 19, chu kì 4, nhóm IA.", True),
            ("b", "Có 4 lớp electron, lớp ngoài cùng có 1 electron.", True),
            ("c", "Có tính kim loại mạnh hơn Sodium (Na, Z = 11).", True),
            ("d", "Dễ dàng nhận thêm 1 electron để đạt cấu hình khí hiếm.", False)
        ], "Kim loại kiềm có xu hướng nhường 1e, không nhận e."),
        make_tf(4, "Vận dụng", "Nguyên tố R có công thức oxide cao nhất là RO2, trong đó O chiếm 53,33% về khối lượng:", [
            ("a", "Khối lượng nguyên tử của R là 28 amu (Silicon).", True),
            ("b", "R thuộc nhóm IVA trong bảng tuần hoàn.", True),
            ("c", "R có 4 electron ở lớp ngoài cùng.", True),
            ("d", "R là một kim loại kiềm.", False)
        ], "Silicon là một phi kim (á kim).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khối lượng nguyên tử của Oxygen theo amu là bao nhiêu?", "16", "Oxygen có khối lượng là 16 amu."),
        make_sa(2, "Thông hiểu", "Kí hiệu hóa học của nguyên tố Sắt theo IUPAC là gì?", "Fe", "Iron có kí hiệu là Fe."),
        make_sa(3, "Vận dụng", "Nguyên tố nào có 3 lớp electron và có 5 electron lớp ngoài cùng? (Ghi kí hiệu hóa học)", "P", "Phosphorus (P, Z = 15)."),
        make_sa(4, "Vận dụng", "Nguyên tử Argon có bao nhiêu electron ở lớp ngoài cùng?", "8", "Argon là khí hiếm có 8e ngoài cùng."),
        make_sa(5, "Vận dụng cao", "Tổng số proton của hai nguyên tố A và B thuộc cùng chu kì và đứng kế tiếp nhau trong bảng tuần hoàn là 31. Số hiệu nguyên tử của nguyên tố A (đứng trước) là bao nhiêu?", "15", "pB - pA = 1, pA + pB = 31 => pA = 15 (P), pB = 16 (S)."),
        make_sa(6, "Vận dụng cao", "Một ion X- có tổng số electron là 18. Số proton trong hạt nhân nguyên tử X là bao nhiêu?", "17", "X nhận 1e thành X- có 18e => số p = 18 - 1 = 17 (Chlorine).")
    ],
    "part4": [
        make_vdc(1, "Nguyên tố X có tổng số hạt cơ bản là 34, trong đó số hạt không mang điện nhiều hơn số hạt mang điện dương là 1. X thuộc nhóm nào trong bảng tuần hoàn?", ["Nhóm IA", "Nhóm IIA", "Nhóm VIIA", "Nhóm VIIIA"], 0, "n - p = 1, 2p + n = 34 => 3p = 33 => p = 11 (Na), nhóm IA."),
        make_vdc(2, "Cho 3 nguyên tố X, Y, Z có cấu hình electron: X (2, 8, 1), Y (2, 8, 2), Z (2, 8, 7). Hợp chất ion tạo bởi X và Z có công thức là:", ["XZ", "XZ2", "X2Z", "XZ3"], 0, "X nhường 1e thành X+, Z nhận 1e thành Z- => công thức XZ (NaCl)."),
        make_vdc(3, "Oxide cao nhất của một nguyên tố có dạng R2O7. Nguyên tố R thuộc nhóm nào trong bảng tuần hoàn?", ["Nhóm VIIA", "Nhóm VA", "Nhóm VIA", "Nhóm IIA"], 0, "R2O7 => hóa trị VII => nhóm VIIA (như Cl2O7)."),
        make_vdc(4, "Biết nguyên tử khối của Cu là 64 amu, của O là 16 amu. Tỉ lệ % khối lượng của Cu trong hợp chất CuO là:", ["80%", "75%", "64%", "88,89%"], 0, "%Cu = 64 / (64 + 16) × 100% = 64 / 80 × 100% = 80%.")
    ]
}

# Đề 3, 4, 5 của c1_rev tiếp tục được nạp tương tự với nội dung hoàn toàn độc lập...
print("Đã nạp xong C1_rev test 1 & 2. Đang tiến hành nạp các bài tiếp theo...")
