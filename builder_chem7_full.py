# -*- coding: utf-8 -*-
"""
HÓA HỌC 7 - 28 ĐỀ THI ĐỘC LẬP HOÀN TOÀN (BÁM SÁT SGK KẾT NỐI TRI THỨC)
Tập hợp toàn bộ 8 bài:
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

# Import các đề b2 và b3 từ builder_chem7
from builder_chem7 import chem7_exams as exams, make_mc, make_tf, make_sa, make_vdc

# ==============================================================================
# BÀI 4: SƠ LƯỢC VỀ BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC (3 ĐỀ ĐỘC LẬP)
# ==============================================================================

# --- ĐỀ 1: Nguyên tắc sắp xếp, cấu tạo ô nguyên tố, chu kì & nhóm A cơ bản ---
exams["chem7_c1_b4_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Bảng tuần hoàn các nguyên tố hóa học được sắp xếp theo chiều tăng dần của:", ["Khối lượng nguyên tử", "Điện tích hạt nhân", "Số neutron", "Bán kính nguyên tử"], 1, "Các nguyên tố được xếp theo chiều tăng dần của điện tích hạt nhân."),
        make_mc(2, "Nhận biết", "Số thứ tự của ô nguyên tố trong bảng tuần hoàn bằng:", ["Số neutron", "Số hiệu nguyên tử (số proton)", "Số lớp electron", "Số electron lớp ngoài cùng"], 1, "Số thứ tự ô = số hiệu nguyên tử Z = số proton = số electron."),
        make_mc(3, "Nhận biết", "Trong bảng tuần hoàn, các nguyên tố có cùng số lớp electron trong nguyên tử được xếp vào cùng một:", ["Ô", "Chu kì", "Nhóm", "Phân nhóm"], 1, "Các nguyên tố có cùng số lớp electron xếp vào cùng một hàng gọi là chu kì."),
        make_mc(4, "Nhận biết", "Bảng tuần hoàn các nguyên tố hóa học hiện nay gồm có bao nhiêu chu kì?", ["5 chu kì", "6 chu kì", "7 chu kì", "8 chu kì"], 2, "Bảng tuần hoàn gồm 7 chu kì (từ chu kì 1 đến chu kì 7)."),
        make_mc(5, "Nhận biết", "Các nguyên tố trong cùng một nhóm A có đặc điểm chung là:", ["Có cùng số electron ở lớp ngoài cùng", "Có cùng số lớp electron", "Có cùng khối lượng nguyên tử", "Có cùng số neutron"], 0, "Các nguyên tố nhóm A có cùng số electron lớp ngoài cùng nên tính chất hóa học tương tự nhau."),
        make_mc(6, "Nhận biết", "Chu kì 1 trong bảng tuần hoàn là chu kì nhỏ nhất, chỉ gồm mấy nguyên tố?", ["2 nguyên tố (H và He)", "8 nguyên tố", "18 nguyên tố", "32 nguyên tố"], 0, "Chu kì 1 chỉ gồm 2 nguyên tố là Hydrogen (H) và Helium (He)."),
        make_mc(7, "Thông hiểu", "Nguyên tử nguyên tố X có 11 proton. Trong bảng tuần hoàn, nguyên tố X thuộc chu kì mấy?", ["Chu kì 1", "Chu kì 2", "Chu kì 3", "Chu kì 4"], 2, "X là Na (Z = 11): phân bố 2, 8, 1 có 3 lớp electron => thuộc chu kì 3."),
        make_mc(8, "Thông hiểu", "Nguyên tố Oxygen ở ô số 8, nhóm VIA, chu kì 2. Số electron ở lớp ngoài cùng của Oxygen là:", ["2", "6", "8", "16"], 1, "Nguyên tố nhóm VIA có 6 electron ở lớp ngoài cùng."),
        make_mc(9, "Thông hiểu", "Các nguyên tố thuộc nhóm IA (trừ Hydrogen) được gọi là nhóm:", ["Kim loại kiềm", "Kim loại kiềm thổ", "Halogen", "Khí hiếm"], 0, "Nhóm IA gồm các kim loại kiềm: Li, Na, K, Rb, Cs, Fr."),
        make_mc(10, "Thông hiểu", "Nguyên tố Chlorine (Z = 17) thuộc nhóm nào trong bảng tuần hoàn?", ["Nhóm IA", "Nhóm VA", "Nhóm VIIA", "Nhóm VIIIA"], 2, "Cl có 7e lớp ngoài cùng (2, 8, 7) => thuộc nhóm VIIA (Halogen)."),
        make_mc(11, "Thông hiểu", "Trong một chu kì, đi từ trái sang phải theo chiều tăng dần của điện tích hạt nhân, tính kim loại và tính phi kim biến đổi như thế nào?", ["Tính kim loại tăng, tính phi kim giảm", "Tính kim loại giảm dần, tính phi kim tăng dần", "Cả tính kim loại và phi kim đều tăng", "Không thay đổi"], 1, "Trong một chu kì theo chiều Z tăng: tính kim loại giảm dần, tính phi kim tăng dần."),
        make_mc(12, "Thông hiểu", "Nhóm nguyên tố nào trong bảng tuần hoàn gồm toàn các chất khí trơ ở điều kiện thường?", ["Nhóm IA", "Nhóm IIA", "Nhóm VIIA", "Nhóm VIIIA"], 3, "Nhóm VIIIA là nhóm khí hiếm (He, Ne, Ar, Kr, Xe, Rn).")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét thông tin ghi trong ô nguyên tố Aluminium (ô số 13):", [
            ("a", "Số hiệu nguyên tử của Aluminium là 13.", True),
            ("b", "Kí hiệu hóa học của nguyên tố là Al.", True),
            ("c", "Aluminium thuộc chu kì 3 vì có 3 lớp electron.", True),
            ("d", "Aluminium thuộc nhóm IIA vì có 2 electron ngoài cùng.", False)
        ], "Al có cấu hình 2, 8, 3 => thuộc nhóm IIIA."),
        make_tf(2, "Thông hiểu", "Xét các nguyên tắc sắp xếp các nguyên tố trong bảng tuần hoàn:", [
            ("a", "Sắp xếp theo chiều tăng dần điện tích hạt nhân nguyên tử.", True),
            ("b", "Các nguyên tố có cùng số lớp electron được xếp vào cùng một chu kì.", True),
            ("c", "Các nguyên tố có tính chất hóa học tương tự nhau được xếp vào cùng một nhóm.", True),
            ("d", "Các nguyên tố có cùng khối lượng nguyên tử luôn được xếp vào cùng một ô.", False)
        ], "Mỗi ô chỉ dành cho một nguyên tố có số hiệu nguyên tử xác định."),
        make_tf(3, "Vận dụng", "Cho các nguyên tố: Na (Z = 11), Mg (Z = 12), Al (Z = 13), Si (Z = 14):", [
            ("a", "Tất cả các nguyên tố này đều thuộc chu kì 3.", True),
            ("b", "Na là kim loại hoạt động mạnh nhất trong số các nguyên tố này.", True),
            ("c", "Al có 3 electron ở lớp ngoài cùng.", True),
            ("d", "Tính kim loại tăng dần từ Na đến Si.", False)
        ], "Trong chu kì 3, tính kim loại giảm dần từ Na > Mg > Al > Si."),
        make_tf(4, "Vận dụng", "Nguyên tố R thuộc chu kì 2, nhóm VA trong bảng tuần hoàn:", [
            ("a", "Nguyên tử R có 2 lớp electron.", True),
            ("b", "Lớp ngoài cùng của nguyên tử R có 5 electron.", True),
            ("c", "Số hiệu nguyên tử của R là 7 (Nitrogen).", True),
            ("d", "R là một nguyên tố kim loại.", False)
        ], "Nitrogen là một nguyên tố phi kim.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Bảng tuần hoàn các nguyên tố hóa học có bao nhiêu chu kì nhỏ (gồm chu kì 1, 2, 3)?", "3", "Có 3 chu kì nhỏ là chu kì 1, 2, 3."),
        make_sa(2, "Thông hiểu", "Nguyên tố Carbon ở ô số 6. Số hạt proton trong nguyên tử Carbon là bao nhiêu?", "6", "Số thứ tự ô = số p = 6."),
        make_sa(3, "Vận dụng", "Nguyên tố Potassium (K) có Z = 19. Số thứ tự chu kì của Potassium trong bảng tuần hoàn là bao nhiêu?", "4", "K có cấu hình 2, 8, 8, 1 => 4 lớp e => chu kì 4."),
        make_sa(4, "Vận dụng", "Nguyên tố Sulfur (S) ở chu kì 3, nhóm VIA. Số electron ở lớp vỏ ngoài cùng của nguyên tử Sulfur là bao nhiêu?", "6", "Số thứ tự nhóm A = số e lớp ngoài cùng = 6."),
        make_sa(5, "Vận dụng cao", "Một nguyên tố X ở chu kì 3. Oxide cao nhất của X có dạng XO3. Số thứ tự nhóm của nguyên tố X là nhóm mấy A?", "6", "Oxide cao nhất XO3 => hóa trị VI => nhóm VIA."),
        make_sa(6, "Vận dụng cao", "Hai nguyên tố A và B đứng kế tiếp nhau trong cùng một chu kì có tổng số proton là 25. Số proton của nguyên tố B (có Z lớn hơn) là bao nhiêu?", "13", "pB - pA = 1, pA + pB = 25 => pB = 13 (Al), pA = 12 (Mg).")
    ],
    "part4": [
        make_vdc(1, "Nguyên tố X thuộc chu kì 3, nhóm IIA. Nhận định nào sau đây là ĐÚNG về nguyên tố X?", ["X là phi kim, có 3 lớp electron", "X là kim loại kiềm thổ, có 2 electron ở lớp ngoài cùng", "X là khí hiếm có 8 electron ở lớp ngoài cùng", "X có số hiệu nguyên tử bằng 20"], 1, "X là Magnesium (Mg, Z = 12), kim loại kiềm thổ nhóm IIA, có 2e ngoài cùng."),
        make_vdc(2, "Hai nguyên tố X và Y thuộc cùng một nhóm A và ở hai chu kì liên tiếp có tổng số hiệu nguyên tử là 32. Số hiệu nguyên tử của X và Y lần lượt là:", ["12 và 20", "8 và 24", "11 và 21", "9 và 23"], 0, "pY - pX = 8, pX + pY = 32 => pX = 12 (Mg), pY = 20 (Ca), cùng nhóm IIA."),
        make_vdc(3, "Cho các nguyên tố: F (Z = 9), Cl (Z = 17), Br (Z = 35). Thứ tự tính phi kim giảm dần của các nguyên tố này là:", ["F > Cl > Br", "Br > Cl > F", "Cl > F > Br", "F > Br > Cl"], 0, "Trong nhóm Halogen (VIIA), đi từ trên xuống dưới theo chiều tăng của Z thì tính phi kim giảm dần."),
        make_vdc(4, "Một nguyên tố phi kim R ở chu kì 2. Hợp chất khí của R với Hydrogen có công thức RH4. Vị trí của R trong bảng tuần hoàn là:", ["Ô số 6, chu kì 2, nhóm IVA", "Ô số 7, chu kì 2, nhóm VA", "Ô số 8, chu kì 2, nhóm VIA", "Ô số 14, chu kì 3, nhóm IVA"], 0, "Hóa trị 4 với H => nhóm IVA. Chu kì 2 => cấu hình 2, 4 => Z = 6 (Carbon).")
    ]
}

# --- ĐỀ 2: Tính chất biến đổi trong chu kì & nhóm, vị trí các nguyên tố đặc biệt, kim loại kiềm & halogen ---
exams["chem7_c1_b4_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Các nguyên tố trong bảng tuần hoàn được chia thành 3 loại chính gồm:", ["Kim loại, phi kim và khí hiếm", "Chất rắn, chất lỏng và chất khí", "Kim loại nhẹ, kim loại nặng và phi kim", "Đơn chất, hợp chất và hỗn hợp"], 0, "Phân loại theo tính chất hóa học thành: Kim loại, phi kim và khí hiếm."),
        make_mc(2, "Nhận biết", "Đại đa số các nguyên tố hóa học trong bảng tuần hoàn là:", ["Kim loại (chiếm hơn 80%)", "Phi kim", "Khí hiếm", "Á kim"], 0, "Hơn 80% trong số 118 nguyên tố là các nguyên tố kim loại."),
        make_mc(3, "Nhận biết", "Chu kì 2 và chu kì 3 trong bảng tuần hoàn đều chứa bao nhiêu nguyên tố?", ["2 nguyên tố", "8 nguyên tố", "18 nguyên tố", "32 nguyên tố"], 1, "Chu kì 2 và chu kì 3 đều chứa đúng 8 nguyên tố."),
        make_mc(4, "Nhận biết", "Nhóm VIIA trong bảng tuần hoàn còn có tên gọi thông dụng là nhóm:", ["Halogen", "Kim loại kiềm", "Kim loại kiềm thổ", "Khí hiếm"], 0, "Nhóm VIIA gồm F, Cl, Br, I, At được gọi là nhóm Halogen."),
        make_mc(5, "Nhận biết", "Trong một nhóm A, đi từ trên xuống dưới theo chiều tăng của điện tích hạt nhân, số lớp electron của nguyên tử:", ["Tăng dần", "Giảm dần", "Không đổi", "Tăng rồi giảm"], 0, "Mỗi chu kì mới tương ứng thêm 1 lớp electron nên đi từ trên xuống dưới số lớp e tăng dần."),
        make_mc(6, "Nhận biết", "Số electron lớp ngoài cùng của các nguyên tử nguyên tố nhóm IIA là:", ["1", "2", "3", "8"], 1, "Các nguyên tố nhóm IIA có 2 electron ở lớp ngoài cùng."),
        make_mc(7, "Thông hiểu", "Nguyên tố Calcium (Z = 20) nằm ở chu kì 4, nhóm IIA. Cấu hình phân bố electron của Calcium là:", ["2, 8, 8, 2", "2, 8, 10", "2, 10, 8", "2, 8, 9, 1"], 0, "Ca (Z = 20) phân bố: lớp 1 (2e), lớp 2 (8e), lớp 3 (8e), lớp 4 (2e)."),
        make_mc(8, "Thông hiểu", "Nguyên tố nào sau đây có tính phi kim mạnh nhất trong bảng tuần hoàn?", ["Fluorine (F)", "Chlorine (Cl)", "Oxygen (O)", "Nitrogen (N)"], 0, "Fluorine ở góc trên bên phải bảng tuần hoàn (trừ khí hiếm) là phi kim mạnh nhất."),
        make_mc(9, "Thông hiểu", "Nguyên tố phi kim nào sau đây nằm ở chu kì 3, nhóm VA?", ["Phosphorus (P, Z = 15)", "Nitrogen (N, Z = 7)", "Sulfur (S, Z = 16)", "Silicon (Si, Z = 14)"], 0, "Phosphorus có Z = 15: phân bố 2, 8, 5 => chu kì 3, nhóm VA."),
        make_mc(10, "Thông hiểu", "Trong một nhóm A, theo chiều tăng của điện tích hạt nhân (từ trên xuống dưới), tính kim loại biến đổi như thế nào?", ["Tăng dần", "Giảm dần", "Không đổi", "Không theo quy luật"], 0, "Trong nhóm A đi từ trên xuống: tính kim loại tăng dần, tính phi kim giảm dần."),
        make_mc(11, "Thông hiểu", "Nguyên tố Argon (Ar, Z = 18) thuộc chu kì 3, nhóm VIIIA. Số electron ở lớp ngoài cùng của Argon là:", ["2", "6", "8", "18"], 2, "Argon là khí hiếm có 8 electron bão hòa ở lớp ngoài cùng."),
        make_mc(12, "Thông hiểu", "Dãy gồm các nguyên tố kim loại kiềm (nhóm IA) là:", ["Li, Na, K", "Be, Mg, Ca", "F, Cl, Br", "He, Ne, Ar"], 0, "Li, Na, K thuộc nhóm kim loại kiềm IA.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét vị trí và tính chất của nguyên tố Sodium (Na, Z = 11):", [
            ("a", "Sodium nằm ở ô số 11, chu kì 3, nhóm IA.", True),
            ("b", "Sodium là một kim loại kiềm mềm, nhẹ và hoạt động hóa học mạnh.", True),
            ("c", "Nguyên tử Sodium có 1 electron ở lớp ngoài cùng.", True),
            ("d", "Sodium có tính kim loại yếu hơn Magnesium (Mg, Z = 12).", False)
        ], "Trong chu kì 3, Na đứng trước Mg nên Na có tính kim loại mạnh hơn Mg."),
        make_tf(2, "Thông hiểu", "Xét các nguyên tố trong nhóm Halogen (nhóm VIIA):", [
            ("a", "Đều có 7 electron ở lớp electron ngoài cùng.", True),
            ("b", "Đều là những phi kim hoạt động hóa học mạnh.", True),
            ("c", "Dễ dàng nhận thêm 1 electron để đạt cấu hình bão hòa giống khí hiếm.", True),
            ("d", "Tất cả các halogen đều là chất khí ở nhiệt độ phòng.", False)
        ], "Bromine là chất lỏng, Iodine là chất rắn."),
        make_tf(3, "Vận dụng", "Cho ba nguyên tố X (Z = 11), Y (Z = 12), Z (Z = 19):", [
            ("a", "X và Y cùng thuộc chu kì 3.", True),
            ("b", "X và Z cùng thuộc nhóm IA.", True),
            ("c", "Tính kim loại của Z mạnh hơn tính kim loại của X.", True),
            ("d", "Y có bán kính nguyên tử lớn hơn X.", False)
        ], "Trong chu kì 3, đi từ trái sang phải bán kính nguyên tử giảm dần => R(Na) > R(Mg)."),
        make_tf(4, "Vận dụng", "Nguyên tố T ở chu kì 3, nhóm VIIA trong bảng tuần hoàn:", [
            ("a", "T có số hiệu nguyên tử là 17 (Chlorine).", True),
            ("b", "Nguyên tử T có 3 lớp electron.", True),
            ("c", "T là một phi kim điển hình.", True),
            ("d", "Hạt nhân nguyên tử T có điện tích là +7.", False)
        ], "Hạt nhân có 17 proton nên điện tích hạt nhân là +17.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Các nguyên tố kim loại kiềm thổ nằm ở nhóm mấy A trong bảng tuần hoàn?", "2", "Nhóm IIA là nhóm kim loại kiềm thổ."),
        make_sa(2, "Thông hiểu", "Nguyên tố Neon (Ne) nằm ở chu kì 2, nhóm VIIIA. Số hiệu nguyên tử của Neon là bao nhiêu?", "10", "Neon có Z = 10."),
        make_sa(3, "Vận dụng", "Nguyên tố X có cấu hình electron là 2, 8, 4. Số thứ tự nhóm A của nguyên tố X là nhóm mấy?", "4", "Có 4e ngoài cùng => nhóm IVA (Silicon)."),
        make_sa(4, "Vận dụng", "Nguyên tố Bromine có 35 proton. Số thứ tự ô của Bromine trong bảng tuần hoàn là bao nhiêu?", "35", "Số thứ tự ô = Z = 35."),
        make_sa(5, "Vận dụng cao", "Hai nguyên tố X và Y đứng kế tiếp nhau trong cùng một nhóm A ở hai chu kì liên tiếp, có tổng số proton là 22. Số proton của nguyên tố X (ở chu kì nhỏ hơn) là bao nhiêu?", "7", "pY - pX = 8, pX + pY = 22 => pX = 7 (Nitrogen), pY = 15 (Phosphorus)."),
        make_sa(6, "Vận dụng cao", "Một nguyên tố R có công thức oxide cao nhất là R2O5. Số electron lớp ngoài cùng của nguyên tử R là bao nhiêu?", "5", "R2O5 => hóa trị V => nhóm VA => có 5 electron lớp ngoài cùng.")
    ],
    "part4": [
        make_vdc(1, "Nguyên tố X thuộc chu kì 3, nhóm VIA. Khẳng định nào sau đây là KHÔNG đúng?", ["Nguyên tử X có 3 lớp electron", "Lớp ngoài cùng của X có 6 electron", "X là phi kim (Sulfur, Z = 16)", "Hợp chất khí của X với Hydrogen là XH4"], 3, "Hợp chất với H của nguyên tố nhóm VIA có công thức là H2X (hoặc XH2) như H2S."),
        make_vdc(2, "Cho biết nguyên tố M có 3 lớp electron và có 1 electron lớp ngoài cùng. Nhận xét nào sau đây đúng về vị trí và tính chất của M?", ["M ở ô 11, chu kì 3, nhóm IA; là kim loại mạnh", "M ở ô 13, chu kì 3, nhóm IIIA; là kim loại", "M ở ô 19, chu kì 4, nhóm IA; là kim loại kiềm", "M ở ô 9, chu kì 2, nhóm VIIA; là phi kim"], 0, "Cấu hình 2, 8, 1 => Z = 11 (Na), chu kì 3, nhóm IA, kim loại kiềm mạnh."),
        make_vdc(3, "Ba nguyên tố A, B, C có số hiệu nguyên tử lần lượt là 11, 12, 13. Thứ tự sắp xếp theo chiều tính kim loại giảm dần là:", ["A > B > C", "C > B > A", "B > A > C", "A > C > B"], 0, "Na (11) > Mg (12) > Al (13) theo quy luật giảm dần tính kim loại trong chu kì."),
        make_vdc(4, "Một nguyên tử phi kim X có tổng số hạt là 52, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 16. Vị trí của X trong bảng tuần hoàn là:", ["Ô số 17, chu kì 3, nhóm VIIA", "Ô số 16, chu kì 3, nhóm VIA", "Ô số 15, chu kì 3, nhóm VA", "Ô số 35, chu kì 4, nhóm VIIA"], 0, "p = 17 (Chlorine), phân bố 2, 8, 7 => ô 17, chu kì 3, nhóm VIIA.")
    ]
}

# --- ĐỀ 3: Ứng dụng quy luật BTH, so sánh tính chất kim loại/phi kim, câu hỏi liên môn & thực tiễn ---
exams["chem7_c1_b4_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Trong bảng tuần hoàn, ranh giới phân chia giữa kim loại và phi kim là một đường zíc-zắc kéo dài từ nguyên tố:", ["Boron đến Astatine", "Hydrogen đến Helium", "Lithium đến Fluorine", "Carbon đến Lead"], 0, "Đường zíc-zắc từ B đến At phân cách kim loại (bên trái) và phi kim (bên phải)."),
        make_mc(2, "Nhận biết", "Căn cứ vào cấu tạo nguyên tử, số thứ tự chu kì cho ta biết thông tin trực tiếp về:", ["Số electron lớp ngoài cùng", "Số lớp electron của nguyên tử", "Số neutron trong hạt nhân", "Khối lượng nguyên tử"], 1, "Số thứ tự chu kì = số lớp electron."),
        make_mc(3, "Nhận biết", "Nguyên tố nào sau đây là một phi kim ở thể rắn có màu vàng chanh đặc trưng?", ["Sulfur (Lưu huỳnh)", "Phosphorus", "Carbon", "Silicon"], 0, "Sulfur (S) là chất rắn màu vàng chanh."),
        make_mc(4, "Nhận biết", "Số electron tối đa ở lớp ngoài cùng của mọi nguyên tử nguyên tố (trừ Helium) là:", ["2", "8", "18", "32"], 1, "Lớp ngoài cùng bền vững tối đa 8 electron (quy tắc octet)."),
        make_mc(5, "Nhận biết", "Bảng tuần hoàn các nguyên tố hóa học đầu tiên do nhà hóa học vĩ đại nào phát minh vào năm 1869?", ["Dmitri Mendeleev", "John Dalton", "Ernest Rutherford", "Niels Bohr"], 0, "Mendeleev là người đầu tiên sắp xếp và công bố bảng tuần hoàn."),
        make_mc(6, "Nhận biết", "Nguyên tố Helium (He) có 2 electron ở lớp vỏ nhưng được xếp vào nhóm VIIIA vì:", ["Helium có 8 electron", "Lớp ngoài cùng của Helium đã bão hòa và có tính chất trơ của khí hiếm", "Helium là một kim loại", "Helium có 8 proton"], 1, "Helium chỉ có 1 lớp electron và đã bão hòa tối đa 2e, trơ giống các khí hiếm khác."),
        make_mc(7, "Thông hiểu", "Trong các nguyên tố sau, nguyên tố nào có tính kim loại mạnh nhất?", ["Potassium (K, Z = 19)", "Sodium (Na, Z = 11)", "Lithium (Li, Z = 3)", "Aluminium (Al, Z = 13)"], 0, "Trong nhóm IA, tính kim loại tăng dần: Li < Na < K => K mạnh nhất."),
        make_mc(8, "Thông hiểu", "Nguyên tố X ở chu kì 2, nhóm IVA. Kí hiệu hóa học của nguyên tố X là:", ["C", "Si", "N", "B"], 0, "Chu kì 2, nhóm IVA có 2 lớp e và 4e ngoài cùng => Z = 6 (Carbon, C)."),
        make_mc(9, "Thông hiểu", "Tính chất nào sau đây của các nguyên tố BIẾN ĐỔI tuần hoàn theo chiều tăng điện tích hạt nhân?", ["Điện tích hạt nhân", "Số electron lớp ngoài cùng", "Khối lượng nguyên tử", "Số proton"], 1, "Số electron lớp ngoài cùng biến đổi lặp lại tuần hoàn từ 1 đến 8."),
        make_mc(10, "Thông hiểu", "Nguyên tố nào sau đây là thành phần quan trọng trong pin sạc điện thoại và xe điện hiện nay?", ["Lithium (Li)", "Sodium (Na)", "Calcium (Ca)", "Iron (Fe)"], 0, "Pin Lithium-ion sử dụng nguyên tố Lithium."),
        make_mc(11, "Thông hiểu", "Cho các nguyên tố: Na (Z = 11), P (Z = 15), Cl (Z = 17). Sắp xếp theo chiều tính phi kim tăng dần là:", ["Na < P < Cl", "Cl < P < Na", "P < Na < Cl", "Na < Cl < P"], 0, "Cùng chu kì 3, tính phi kim tăng dần từ trái sang phải: Na (kim loại) < P < Cl."),
        make_mc(12, "Thông hiểu", "Ô nguyên tố cho biết các thông tin gồm:", ["Số hiệu nguyên tử, KHHH, tên nguyên tố, khối lượng nguyên tử", "Số neutron, bán kính nguyên tử, độ âm điện", "Số phân tử, nhiệt độ sôi, khối lượng riêng", "Công thức phân tử và trạng thái tự nhiên"], 0, "4 thông tin chuẩn trong ô nguyên tố SGK KHTN 7.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét nguyên tố Khí hiếm Neon (Ne, ô số 10):", [
            ("a", "Neon thuộc chu kì 2, nhóm VIIIA trong bảng tuần hoàn.", True),
            ("b", "Nguyên tử Neon có 2 lớp electron với cấu hình là (2, 8).", True),
            ("c", "Lớp ngoài cùng của Neon đã bão hòa 8 electron nên rất bền vững.", True),
            ("d", "Neon dễ dàng phản ứng với kim loại Sodium ở nhiệt độ phòng.", False)
        ], "Khí hiếm Neon trơ về mặt hóa học, không phản ứng với Sodium."),
        make_tf(2, "Thông hiểu", "Xét sự biến đổi tính chất trong bảng tuần hoàn:", [
            ("a", "Trong một chu kì từ trái qua phải, tính phi kim có xu hướng tăng dần.", True),
            ("b", "Trong một nhóm A từ trên xuống dưới, tính kim loại có xu hướng tăng dần.", True),
            ("c", "Kim loại mạnh nhất trong bảng tuần hoàn nằm ở góc dưới bên trái (nhóm IA).", True),
            ("d", "Phi kim mạnh nhất nằm ở góc dưới bên phải (nhóm VIIA).", False)
        ], "Phi kim mạnh nhất là Fluorine ở góc TRÊN bên phải nhóm VIIA."),
        make_tf(3, "Vận dụng", "Cho các nguyên tố: O (Z = 8), F (Z = 9), S (Z = 16), Cl (Z = 17):", [
            ("a", "O và F cùng thuộc chu kì 2.", True),
            ("b", "O và S cùng thuộc nhóm VIA.", True),
            ("c", "Tính phi kim của F mạnh hơn O.", True),
            ("d", "Tính phi kim của S mạnh hơn O.", False)
        ], "Trong nhóm VIA từ trên xuống, tính phi kim giảm: O mạnh hơn S."),
        make_tf(4, "Vận dụng", "Nguyên tố kim loại kiềm M thuộc chu kì 3:", [
            ("a", "M là Sodium (Na) có số hiệu nguyên tử bằng 11.", True),
            ("b", "M tác dụng mãnh liệt với nước tạo dung dịch kiềm và giải phóng khí Hydrogen.", True),
            ("c", "Nguyên tử M có xu hướng nhường 1 electron để đạt cấu hình giống Neon.", True),
            ("d", "M thuộc nhóm IIA trong bảng tuần hoàn.", False)
        ], "Sodium thuộc nhóm IA.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Nhóm các nguyên tố kim loại kiềm có bao nhiêu electron ở lớp ngoài cùng?", "1", "Nhóm IA có 1 electron lớp ngoài cùng."),
        make_sa(2, "Thông hiểu", "Nguyên tố Silicon có số hiệu nguyên tử bằng 14. Số thứ tự chu kì của Silicon là bao nhiêu?", "3", "Cấu hình 2, 8, 4 => 3 lớp electron => chu kì 3."),
        make_sa(3, "Vận dụng", "Nguyên tố X có số hiệu nguyên tử bằng 16. Số electron lớp ngoài cùng của X là bao nhiêu?", "6", "Sulfur (Z = 16): 2, 8, 6 => lớp ngoài cùng có 6 electron."),
        make_sa(4, "Vận dụng", "Nguyên tố nào ở chu kì 2, nhóm VIIA? (Ghi kí hiệu hóa học)", "F", "Fluorine (F, Z = 9) ở chu kì 2, nhóm VIIA."),
        make_sa(5, "Vận dụng cao", "Tổng số electron ở các lớp vỏ của hai nguyên tử X và Y thuộc cùng chu kì 3 là 27. Biết X thuộc nhóm IA, Y thuộc nhóm VIA. Số proton của Y là bao nhiêu?", "16", "X là Na (11), Y là S (16): 11 + 16 = 27."),
        make_sa(6, "Vận dụng cao", "Một nguyên tố phi kim R tạo hợp chất với Hydrogen có dạng RH3. Trong oxide cao nhất, R có hóa trị là bao nhiêu?", "5", "Hóa trị với H là 3 => hóa trị cao nhất trong oxide là 8 - 3 = 5 (như P2O5, N2O5).")
    ],
    "part4": [
        make_vdc(1, "Nguyên tố X có 2 lớp electron, lớp ngoài cùng có 7 electron. Hợp chất của X với kim loại Sodium có công thức là:", ["NaF", "NaCl", "Na2O", "Na3N"], 0, "X là Fluorine (Z = 9), hợp chất là Sodium fluoride (NaF)."),
        make_vdc(2, "Cho hai nguyên tố X (Z = 12) và Y (Z = 16). Nhận xét nào sau đây ĐÚNG về hai nguyên tố này?", ["Cả hai đều là kim loại", "X là kim loại, Y là phi kim, cùng thuộc chu kì 3", "X là phi kim, Y là kim loại", "X thuộc chu kì 2, Y thuộc chu kì 3"], 1, "Mg (Z = 12, kim loại) và S (Z = 16, phi kim) đều có 3 lớp e => cùng chu kì 3."),
        make_vdc(3, "Nguyên tố R có cấu hình electron lớp ngoài cùng là 3s2 3p5 (7 electron lớp ngoài cùng ở lớp 3). Tỉ lệ khối lượng của R trong hợp chất với Hydrogen (HR) là bao nhiêu? (Biết R có khối lượng 35,5 amu, H có khối lượng 1 amu):", ["97,26%", "95,5%", "85,2%", "75,5%"], 0, "%R = 35,5 / (1 + 35,5) × 100% ≈ 97,26% (trong HCl)."),
        make_vdc(4, "Cho các nguyên tố: Li (Z = 3), Na (Z = 11), K (Z = 19). Nhận định nào sau đây SAI?", ["Đều thuộc nhóm IA", "Bán kính nguyên tử tăng dần: Li < Na < K", "Tính kim loại tăng dần: Li < Na < K", "Số electron lớp ngoài cùng tăng dần từ Li đến K"], 3, "Số electron lớp ngoài cùng đều bằng 1 không đổi.")
    ]
}

print(f"Tổng số đề sau khi thêm Bài 4: {len(exams)} đề.")
