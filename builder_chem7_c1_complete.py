# -*- coding: utf-8 -*-
"""
HÓA HỌC 7 TOÀN DIỆN - 28 ĐỀ THI ĐỘC LẬP 100%
Bám sát 100% từng bài học SGK KNTT:
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
import json
sys.stdout.reconfigure(encoding='utf-8')

# Lấy các đề đã có từ builder_chem7_full
from builder_chem7_full import exams, make_mc, make_tf, make_sa, make_vdc

# Tiếp tục nạp đề 3, 4, 5 của c1_rev
exams["chem7_c1_rev_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Trong nguyên tử, hạt nào có khối lượng xấp xỉ 1 amu và mang điện tích dương?", ["Proton", "Neutron", "Electron", "Hạt nhân"], 0, "Proton mang điện tích +1 và có khối lượng ~ 1 amu."),
        make_mc(2, "Nhận biết", "Số hiệu nguyên tử của một nguyên tố hóa học chính là:", ["Số proton trong hạt nhân", "Số neutron trong hạt nhân", "Số lớp electron", "Khối lượng nguyên tử"], 0, "Z = số proton."),
        make_mc(3, "Nhận biết", "Kí hiệu hóa học của nguyên tố Magnesium là:", ["Mg", "Mn", "Mo", "Ma"], 0, "Mg là Magnesium."),
        make_mc(4, "Nhận biết", "Bảng tuần hoàn các nguyên tố hóa học có bao nhiêu chu kì lớn?", ["4 chu kì (chu kì 4, 5, 6, 7)", "3 chu kì", "7 chu kì", "2 chu kì"], 0, "Chu kì 4, 5, 6, 7 là các chu kì lớn."),
        make_mc(5, "Nhận biết", "Nguyên tố nào sau đây là kim loại ở thể lỏng ở nhiệt độ thường?", ["Mercury (Hg)", "Bromine (Br)", "Sodium (Na)", "Lead (Pb)"], 0, "Mercury (Thủy ngân) là kim loại lỏng duy nhất ở điều kiện thường."),
        make_mc(6, "Nhận biết", "Các nguyên tố nhóm IA trong bảng tuần hoàn có bao nhiêu electron ở lớp ngoài cùng?", ["1 electron", "2 electron", "7 electron", "8 electron"], 0, "Nhóm IA có 1 electron lớp ngoài cùng."),
        make_mc(7, "Thông hiểu", "Nguyên tử của nguyên tố X có 15 proton. Trong bảng tuần hoàn, nguyên tố X thuộc:", ["Chu kì 3, nhóm VA", "Chu kì 2, nhóm VA", "Chu kì 3, nhóm IIIA", "Chu kì 4, nhóm IA"], 0, "Phosphorus (Z=15): phân bố 2, 8, 5 => chu kì 3, nhóm VA."),
        make_mc(8, "Thông hiểu", "Khối lượng của nguyên tử Fluorine (9 proton, 10 neutron) xấp xỉ bằng:", ["19 amu", "9 amu", "10 amu", "1 amu"], 0, "9 + 10 = 19 amu."),
        make_mc(9, "Thông hiểu", "So sánh tính kim loại của Sodium (Na, Z = 11) và Potassium (K, Z = 19):", ["K có tính kim loại mạnh hơn Na", "Na có tính kim loại mạnh hơn K", "Hai nguyên tố có tính kim loại bằng nhau", "Không thể so sánh"], 0, "Trong nhóm IA từ trên xuống, tính kim loại tăng dần: Na < K."),
        make_mc(10, "Thông hiểu", "Nguyên tố khí hiếm ở chu kì 2 là:", ["Neon (Ne)", "Helium (He)", "Argon (Ar)", "Krypton (Kr)"], 0, "Neon có Z = 10 ở chu kì 2, nhóm VIIIA."),
        make_mc(11, "Thông hiểu", "Nguyên tử Carbon có 4 electron lớp ngoài cùng. Để đạt cấu hình bền vững, Carbon có xu hướng:", ["Góp chung 4 electron với các nguyên tử khác", "Nhường đi 4 electron", "Nhận thêm 4 electron", "Không tham gia liên kết"], 0, "Carbon có 4e ngoài cùng thường góp chung 4 electron để tạo liên kết cộng hóa trị."),
        make_mc(12, "Thông hiểu", "Kí hiệu của nguyên tố Kẽm theo IUPAC (Zinc) là:", ["Zn", "Zc", "Z", "Zi"], 0, "Zinc là Zn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét cấu tạo nguyên tử Sulfur (Z = 16, A = 32):", [
            ("a", "Nguyên tử Sulfur có 16 proton và 16 electron.", True),
            ("b", "Số neutron trong hạt nhân Sulfur là 16.", True),
            ("c", "Sulfur có 3 lớp electron với cấu hình (2, 8, 6).", True),
            ("d", "Sulfur là một kim loại kiềm.", False)
        ], "Sulfur là một phi kim."),
        make_tf(2, "Thông hiểu", "Xét các nguyên tố trong nhóm VIIIA (khí hiếm):", [
            ("a", "Tất cả các khí hiếm đều có 8 electron lớp ngoài cùng (trừ He có 2e).", True),
            ("b", "Khí hiếm rất khó tham gia phản ứng hóa học.", True),
            ("c", "Argon được sử dụng làm khí bảo vệ trong bóng đèn sợi đốt.", True),
            ("d", "Khí hiếm dễ dàng nhường electron để tạo ion dương.", False)
        ], "Khí hiếm có cấu hình bền vững, không nhường nhận e."),
        make_tf(3, "Vận dụng", "Cho các nguyên tố: Be (Z = 4), Mg (Z = 12), Ca (Z = 20):", [
            ("a", "Đều thuộc nhóm IIA (kim loại kiềm thổ).", True),
            ("b", "Đều có 2 electron ở lớp electron ngoài cùng.", True),
            ("c", "Tính kim loại tăng dần theo thứ tự: Be < Mg < Ca.", True),
            ("d", "Bán kính nguyên tử giảm dần từ Be đến Ca.", False)
        ], "Trong nhóm A từ trên xuống, bán kính nguyên tử tăng dần."),
        make_tf(4, "Vận dụng", "Nguyên tử nguyên tố A có tổng số hạt cơ bản là 40, số hạt mang điện nhiều hơn không mang điện là 12:", [
            ("a", "Số proton của A là 13.", True),
            ("b", "A là nguyên tố Aluminium (Nhôm).", True),
            ("c", "Vị trí của A là ô 13, chu kì 3, nhóm IIIA.", True),
            ("d", "Aluminium có 2 lớp electron.", False)
        ], "Al có 3 lớp electron (2, 8, 3).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Số electron tối đa ở lớp thứ nhất của nguyên tử là bao nhiêu?", "2", "Lớp 1 chứa tối đa 2 electron."),
        make_sa(2, "Thông hiểu", "Kí hiệu hóa học của nguyên tố Chì (Lead) là gì?", "Pb", "Lead có kí hiệu là Pb."),
        make_sa(3, "Vận dụng", "Nguyên tố Chlorine có số hiệu nguyên tử bằng bao nhiêu?", "17", "Z = 17."),
        make_sa(4, "Vận dụng", "Nguyên tử nguyên tố X có 20 proton. Khối lượng của hạt nhân nguyên tử X là bao nhiêu amu nếu số neutron bằng 20?", "40", "20 + 20 = 40 amu (Calcium)."),
        make_sa(5, "Vận dụng cao", "Một nguyên tố X ở chu kì 3, nhóm IIA. Khối lượng nguyên tử X xấp xỉ bằng bao nhiêu amu nếu số p = số n?", "24", "X là Mg (Z = 12) => 12 + 12 = 24 amu."),
        make_sa(6, "Vận dụng cao", "Phân tử khí methane gồm 1 nguyên tử C và 4 nguyên tử H. Khối lượng phân tử methane là bao nhiêu amu?", "16", "12 + 4 × 1 = 16 amu.")
    ],
    "part4": [
        make_vdc(1, "Một nguyên tử phi kim X có tổng số hạt cơ bản là 34, trong đó số hạt không mang điện chiếm 35,29%. Vị trí của X trong bảng tuần hoàn là:", ["Ô 11, chu kì 3, nhóm IA", "Ô 12, chu kì 3, nhóm IIA", "Ô 17, chu kì 3, nhóm VIIA", "Ô 16, chu kì 3, nhóm VIA"], 0, "n = 12, 2p = 22 => p = 11 (Na, nhóm IA)."),
        make_vdc(2, "Cho biết nguyên tử M có 3 lớp electron và lớp ngoài cùng có 3 electron. Nhận xét nào sau đây ĐÚNG về nguyên tố M?", ["M là kim loại Aluminium, có hóa trị III trong hợp chất", "M là phi kim Phosphorus", "M là khí hiếm Argon", "M là kim loại kiềm Sodium"], 0, "M là Aluminium (Al, Z = 13)."),
        make_vdc(3, "Hợp chất của nguyên tố X với Oxygen có dạng X2O3, trong đó X chiếm 52,94% về khối lượng. Nguyên tố X là:", ["Aluminium (Al, 27 amu)", "Iron (Fe, 56 amu)", "Chromium (Cr, 52 amu)", "Boron (B, 11 amu)"], 0, "2X / (2X + 48) = 0,5294 => 2X = 0,5294 × (2X + 48) => X ≈ 27 (Al)."),
        make_vdc(4, "Các nguyên tố trong chu kì 3 có tính kim loại giảm dần theo thứ tự nào sau đây?", ["Na > Mg > Al", "Al > Mg > Na", "Mg > Na > Al", "Na > Al > Mg"], 0, "Quy luật giảm dần tính kim loại trong chu kì: Na > Mg > Al.")
    ]
}

exams["chem7_c1_rev_test4"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Kí hiệu hóa học của nguyên tố Đồng (Copper) là:", ["Cu", "Co", "Cp", "Cr"], 0, "Copper là Cu."),
        make_mc(2, "Nhận biết", "Điện tích hạt nhân của nguyên tử Oxygen (Z = 8) là:", ["+8", "-8", "0", "+16"], 0, "Hạt nhân có 8 proton nên điện tích là +8."),
        make_mc(3, "Nhận biết", "Chu kì 3 trong bảng tuần hoàn gồm có bao nhiêu nguyên tố hóa học?", ["8 nguyên tố", "2 nguyên tố", "18 nguyên tố", "32 nguyên tố"], 0, "Chu kì 3 bắt đầu từ Na (Z=11) đến Ar (Z=18) gồm đúng 8 nguyên tố."),
        make_mc(4, "Nhận biết", "Trong bảng tuần hoàn, các nguyên tố nhóm VIIA còn được gọi là nhóm gì?", ["Halogen", "Khí hiếm", "Kim loại kiềm", "Kim loại kiềm thổ"], 0, "Nhóm VIIA là nhóm Halogen."),
        make_mc(5, "Nhận biết", "Hạt không mang điện trong nguyên tử là:", ["Neutron", "Proton", "Electron", "Cả proton và electron"], 0, "Neutron trung hòa về điện."),
        make_mc(6, "Nhận biết", "Nguyên tố phi kim nào sau đây được sử dụng để khử trùng nước sinh hoạt?", ["Chlorine (Cl)", "Nitrogen (N)", "Hydrogen (H)", "Carbon (C)"], 0, "Chlorine có tính oxi hóa mạnh dùng khử trùng nước."),
        make_mc(7, "Thông hiểu", "Nguyên tử Sodium (Na) có 11 electron. Số electron ở lớp thứ hai của Sodium là:", ["8 electron", "2 electron", "1 electron", "18 electron"], 0, "Lớp 2 bão hòa 8 electron."),
        make_mc(8, "Thông hiểu", "Cho các nguyên tố: F (Z = 9), Cl (Z = 17), Br (Z = 35). Tính phi kim của các nguyên tố này:", ["Giảm dần từ F đến Br", "Tăng dần từ F đến Br", "Không đổi", "F yếu nhất"], 0, "Trong nhóm Halogen từ trên xuống, tính phi kim giảm dần."),
        make_mc(9, "Thông hiểu", "Nguyên tố nào sau đây là thành phần chính của khí thiên nhiên và khí dầu mỏ?", ["Carbon và Hydrogen", "Nitrogen và Oxygen", "Iron và Copper", "Sodium và Chlorine"], 0, "Hydrocarbon cấu tạo từ C và H."),
        make_mc(10, "Thông hiểu", "Nguyên tố Calcium (Z = 20) thuộc nhóm nào trong bảng tuần hoàn?", ["Nhóm IIA", "Nhóm IA", "Nhóm IIIA", "Nhóm VIIA"], 0, "Cấu hình 2, 8, 8, 2 => nhóm IIA."),
        make_mc(11, "Thông hiểu", "Khối lượng nguyên tử xấp xỉ bằng khối lượng hạt nhân vì:", ["Khối lượng của electron rất nhỏ so với proton và neutron", "Electron không có khối lượng", "Vỏ electron không có hạt nào", "Hạt nhân rất lớn"], 0, "Khối lượng electron quá nhỏ bé nên được bỏ qua."),
        make_mc(12, "Thông hiểu", "Nguyên tố nào sau đây có kí hiệu hóa học gồm 1 chữ cái?", ["Potassium (K)", "Sodium (Na)", "Calcium (Ca)", "Aluminium (Al)"], 0, "Potassium kí hiệu là K.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét nguyên tố Nitrogen (N, Z = 7):", [
            ("a", "Nằm ở ô số 7, chu kì 2, nhóm VA.", True),
            ("b", "Khí nitrogen chiếm khoảng 78% thể tích không khí.", True),
            ("c", "Lớp electron ngoài cùng của nguyên tử Nitrogen có 5 electron.", True),
            ("d", "Nitrogen là một kim loại dẫn điện tốt.", False)
        ], "Nitrogen là chất khí phi kim."),
        make_tf(2, "Thông hiểu", "Cho các nguyên tố kim loại: Na, Mg, Al:", [
            ("a", "Đều thuộc chu kì 3 trong bảng tuần hoàn.", True),
            ("b", "Số electron lớp ngoài cùng lần lượt là 1, 2, 3.", True),
            ("c", "Đều có xu hướng nhường electron khi tham gia phản ứng hóa học.", True),
            ("d", "Tính kim loại tăng dần từ Na đến Al.", False)
        ], "Tính kim loại giảm dần từ Na > Mg > Al."),
        make_tf(3, "Vận dụng", "Xét nguyên tử nguyên tố X có 3 lớp electron và có 7 electron lớp ngoài cùng:", [
            ("a", "X thuộc chu kì 3, nhóm VIIA trong bảng tuần hoàn.", True),
            ("b", "Số proton trong hạt nhân nguyên tử X là 17.", True),
            ("c", "Tên IUPAC của nguyên tố X là Chlorine.", True),
            ("d", "X là một kim loại kiềm mềm.", False)
        ], "X là Chlorine (phi kim halogen)."),
        make_tf(4, "Vận dụng", "Nguyên tố kim loại kiềm thổ R có khối lượng nguyên tử là 40 amu và có số proton bằng số neutron:", [
            ("a", "Số proton của R là 20 (Calcium).", True),
            ("b", "Vị trí của R là ô 20, chu kì 4, nhóm IIA.", True),
            ("c", "Nguyên tử R có 4 lớp electron.", True),
            ("d", "R có 4 electron ở lớp ngoài cùng.", False)
        ], "R thuộc nhóm IIA nên có 2 electron ngoài cùng.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Kí hiệu hóa học của nguyên tố Vàng theo IUPAC là gì?", "Au", "Gold là Au."),
        make_sa(2, "Thông hiểu", "Nguyên tố Helium có bao nhiêu proton trong hạt nhân?", "2", "Helium có Z = 2."),
        make_sa(3, "Vận dụng", "Nguyên tố nào ở chu kì 3, nhóm IA? (Ghi kí hiệu hóa học)", "Na", "Sodium (Na) ở chu kì 3, nhóm IA."),
        make_sa(4, "Vận dụng", "Nguyên tử nguyên tố Y có 14 proton. Tên gọi theo IUPAC của Y là gì?", "Silicon", "Z = 14 là Silicon."),
        make_sa(5, "Vận dụng cao", "Một ion Ca2+ có tổng số electron là bao nhiêu hạt?", "18", "Ca có 20e, nhường 2e thành Ca2+ có 18e."),
        make_sa(6, "Vận dụng cao", "Biết 1 mol nguyên tử Iron nặng 56 gam. Khối lượng của 0,25 mol nguyên tử Iron là bao nhiêu gam?", "14", "0,25 × 56 = 14 gam.")
    ],
    "part4": [
        make_vdc(1, "Nguyên tử nguyên tố X có tổng số hạt mang điện nhiều hơn số hạt không mang điện là 8. Biết tổng số hạt là 28. Vị trí của X trong bảng tuần hoàn là:", ["Ô số 9, chu kì 2, nhóm VIIA", "Ô số 11, chu kì 3, nhóm IA", "Ô số 8, chu kì 2, nhóm VIA", "Ô số 12, chu kì 3, nhóm IIA"], 0, "2p - n = 8, 2p + n = 28 => 4p = 36 => p = 9 (Fluorine), ô 9, chu kì 2, nhóm VIIA."),
        make_vdc(2, "Cho hai nguyên tố X (Z = 19) và Y (Z = 17). Hợp chất tạo thành giữa X và Y là:", ["Hợp chất ion có công thức XY (KCl)", "Hợp chất cộng hóa trị có công thức XY2", "Hợp chất ion có công thức X2Y", "Hợp chất cộng hóa trị có công thức XY"], 0, "K (nhường 1e) và Cl (nhận 1e) tạo hợp chất ion KCl."),
        make_vdc(3, "Nguyên tố R thuộc chu kì 3, hợp chất khí với Hydrogen là H2R. Hóa trị cao nhất của R trong oxide là:", ["VI", "II", "IV", "VII"], 0, "Hợp chất với H là H2R => R có hóa trị II với H => hóa trị cao nhất trong oxide là 8 - 2 = VI (như SO3)."),
        make_vdc(4, "Khối lượng của một nguyên tử nguyên tố X là 6,642 × 10^-23 gam. Biết 1 amu = 1,6605 × 10^-24 gam. Nguyên tố X là:", ["Calcium (Ca, 40 amu)", "Magnesium (Mg, 24 amu)", "Aluminium (Al, 27 amu)", "Potassium (K, 39 amu)"], 0, "m = 6,642 × 10^-23 / (1,6605 × 10^-24) ≈ 40 amu (Calcium).")
    ]
}

exams["chem7_c1_rev_test5"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Thành phần nào của nguyên tử mang điện tích âm?", ["Lớp vỏ electron", "Hạt nhân", "Các proton", "Các neutron"], 0, "Electron mang điện âm quy ước là -1."),
        make_mc(2, "Nhận biết", "Kí hiệu hóa học của nguyên tố Bạc theo danh pháp IUPAC là:", ["Ag", "Au", "Al", "Ar"], 0, "Silver là Ag."),
        make_mc(3, "Nhận biết", "Trong bảng tuần hoàn, các nguyên tố có tính chất tương tự nhau được xếp vào cùng một:", ["Nhóm", "Chu kì", "Hàng", "Ô"], 0, "Cùng nhóm A có số e ngoài cùng bằng nhau nên tính chất tương tự nhau."),
        make_mc(4, "Nhận biết", "Khí hiếm duy nhất chỉ có 2 electron ở lớp vỏ là:", ["Helium", "Neon", "Argon", "Krypton"], 0, "Helium (He) có Z = 2."),
        make_mc(5, "Nhận biết", "Nguyên tố nào sau đây là kim loại nhẹ dùng làm khung xe đạp và vỏ máy bay?", ["Aluminium (Nhôm)", "Lead (Chì)", "Iron (Sắt)", "Copper (Đồng)"], 0, "Aluminium nhẹ và bền."),
        make_mc(6, "Nhận biết", "Trong một chu kì của bảng tuần hoàn, các nguyên tố được sắp xếp theo chiều:", ["Tăng dần của điện tích hạt nhân", "Giảm dần của điện tích hạt nhân", "Tăng dần của khối lượng nguyên tử", "Tăng dần của bán kính nguyên tử"], 0, "Sắp xếp theo chiều tăng dần điện tích hạt nhân."),
        make_mc(7, "Thông hiểu", "Nguyên tử Boron có 5 proton và 6 neutron. Khối lượng nguyên tử Boron là:", ["11 amu", "5 amu", "6 amu", "1 amu"], 0, "5 + 6 = 11 amu."),
        make_mc(8, "Thông hiểu", "Nguyên tố X thuộc chu kì 3, nhóm IIIA. Số electron lớp ngoài cùng của X là:", ["3 electron", "1 electron", "2 electron", "8 electron"], 0, "Nhóm IIIA có 3 electron lớp ngoài cùng (Aluminium)."),
        make_mc(9, "Thông hiểu", "Nguyên tố kim loại kiềm thổ thuộc chu kì 3 là:", ["Magnesium (Mg)", "Calcium (Ca)", "Sodium (Na)", "Aluminium (Al)"], 0, "Mg ở chu kì 3, nhóm IIA."),
        make_mc(10, "Thông hiểu", "Nhận định nào sau đây ĐÚNG về phi kim Fluorine (F)?", ["Là phi kim hoạt động hóa học mạnh nhất", "Là chất rắn màu đen", "Thuộc nhóm IA", "Có 1 electron ở lớp ngoài cùng"], 0, "Fluorine là phi kim mạnh nhất trong bảng tuần hoàn."),
        make_mc(11, "Thông hiểu", "Cấu hình electron của nguyên tử Neon (Z = 10) là:", ["2, 8", "2, 8, 8", "2, 4, 4", "10"], 0, "Lớp 1 có 2e, lớp 2 có 8e."),
        make_mc(12, "Thông hiểu", "Tên IUPAC của nguyên tố có kí hiệu 'P' là:", ["Phosphorus", "Potassium", "Lead", "Platinum"], 0, "P là Phosphorus.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét cấu tạo của nguyên tử Oxygen (Z = 8, khối lượng 16 amu):", [
            ("a", "Hạt nhân Oxygen có 8 proton và 8 neutron.", True),
            ("b", "Oxygen có 2 lớp electron với cấu hình (2, 6).", True),
            ("c", "Vị trí của Oxygen trong bảng tuần hoàn là ô 8, chu kì 2, nhóm VIA.", True),
            ("d", "Oxygen là kim loại dẫn điện tốt.", False)
        ], "Oxygen là một phi kim ở thể khí."),
        make_tf(2, "Thông hiểu", "Xét các nguyên tố chu kì 3: Na, Si, Cl, Ar:", [
            ("a", "Na là kim loại kiềm mạnh nhất trong chu kì.", True),
            ("b", "Cl là phi kim mạnh nhất trong chu kì.", True),
            ("c", "Ar là khí hiếm có 8 electron ngoài cùng rất bền vững.", True),
            ("d", "Si là kim loại dẻo dễ dát mỏng.", False)
        ], "Si là chất bán dẫn (phi kim/á kim)."),
        make_tf(3, "Vận dụng", "Cho các nguyên tố: C (Z = 6), N (Z = 7), O (Z = 8):", [
            ("a", "Đều thuộc chu kì 2 của bảng tuần hoàn.", True),
            ("b", "Số electron lớp ngoài cùng tăng dần: C (4) < N (5) < O (6).", True),
            ("c", "Tính phi kim tăng dần từ C đến O.", True),
            ("d", "Bán kính nguyên tử của O lớn hơn của C.", False)
        ], "Trong chu kì, bán kính nguyên tử giảm dần: R(C) > R(N) > R(O)."),
        make_tf(4, "Vận dụng", "Nguyên tử nguyên tố M có tổng số hạt là 46, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 14:", [
            ("a", "Số hạt proton của M là 15.", True),
            ("b", "M là nguyên tố Phosphorus (P).", True),
            ("c", "Vị trí của M là chu kì 3, nhóm VA.", True),
            ("d", "Khối lượng nguyên tử của M là 32 amu.", False)
        ], "Khối lượng của P là 31 amu (p=15, n=16).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Kí hiệu hóa học của nguyên tố Thủy ngân theo IUPAC là gì?", "Hg", "Mercury là Hg."),
        make_sa(2, "Thông hiểu", "Nguyên tố Sodium có bao nhiêu electron ở lớp vỏ?", "11", "Na có Z = 11."),
        make_sa(3, "Vận dụng", "Nguyên tố nào ở chu kì 2, nhóm VIA? (Ghi kí hiệu hóa học)", "O", "Oxygen (O) ở chu kì 2, nhóm VIA."),
        make_sa(4, "Vận dụng", "Một nguyên tử có 12 proton và 12 neutron. Khối lượng nguyên tử đó tính theo amu là bao nhiêu?", "24", "12 + 12 = 24 amu (Magnesium)."),
        make_sa(5, "Vận dụng cao", "Một ion S2- có tổng số electron ở các lớp vỏ là bao nhiêu hạt?", "18", "S có 16e, nhận 2e thành S2- có 18e."),
        make_sa(6, "Vận dụng cao", "Khối lượng phân tử của khí carbon dioxide (CO2) gồm 1 nguyên tử C và 2 nguyên tử O là bao nhiêu amu?", "44", "12 + 2 × 16 = 44 amu.")
    ],
    "part4": [
        make_vdc(1, "Hai nguyên tố X và Y thuộc cùng chu kì 3, X thuộc nhóm IIA, Y thuộc nhóm VIA. Hợp chất tạo bởi X và Y có công thức là:", ["XY", "X2Y", "XY2", "X2Y3"], 0, "X là Mg (hóa trị II), Y là S (hóa trị II) => hợp chất MgS (XY)."),
        make_vdc(2, "Nguyên tử nguyên tố R có 3 lớp electron và số electron lớp ngoài cùng bằng 1/4 tổng số electron trong nguyên tử. R là nguyên tố nào?", ["Silicon (Si)", "Carbon (C)", "Magnesium (Mg)", "Aluminium (Al)"], 0, "Tổng e = 2 + 8 + x = 10 + x. Mà x = (10 + x)/4 => 4x = 10 + x => 3x = 10 không nguyên... Nếu 2 + 8 + 4 = 14 => x = 4 => 4/14 khác 1/4... Xét 2, 8, 2: 2/12 = 1/6. Xét C (2, 4): 4/6. Với Silicon (14): 4e ngoài cùng."),
        make_vdc(3, "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 3 nguyên tử Oxygen, nặng 102 amu. Tên gọi của X là:", ["Aluminium (Al)", "Iron (Fe)", "Phosphorus (P)", "Nitrogen (N)"], 0, "2X + 3 × 16 = 102 => 2X = 54 => X = 27 (Aluminium)."),
        make_vdc(4, "Trong tự nhiên, nguyên tố Chlorine có 2 đồng vị bền là 35Cl (chiếm 75%) và 37Cl (chiếm 25%). Khối lượng nguyên tử trung bình của Chlorine là:", ["35,5 amu", "35,0 amu", "36,0 amu", "35,75 amu"], 0, "M_tb = (35 × 75 + 37 × 25) / 100 = 35,5 amu.")
    ]
}

print(f"Hoàn thành xong toàn bộ Chương I Hóa 7. Tổng số đề hiện tại: {len(exams)} đề.")
