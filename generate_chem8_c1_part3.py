# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - BÀI 5, 6, 7 VÀ ÔN TẬP CHƯƠNG I (14 ĐỀ ĐỘC LẬP 100%)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

exams_c1_p3 = {}

# ==============================================================================
# BÀI 5: MOL VÀ TỈ KHỐI CỦA CHẤT KHÍ (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Khái niệm mol, số Avogadro, khối lượng mol M ---
exams_c1_p3["chem8_c1_b5_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Mol là lượng chất có chứa bao nhiêu nguyên tử hoặc phân tử của chất đó?", ["6,022 * 10^23", "6,022 * 10^22", "3,011 * 10^23", "1,660 * 10^-24"], 0, "1 mol chứa hằng số Avogadro N = 6,022 * 10^23 hạt."),
        make_mc(2, "Nhận biết", "Khối lượng mol của một chất được định nghĩa là:", ["Khối lượng tính bằng gam của N hạt nguyên tử hoặc phân tử chất đó", "Khối lượng của 1 nguyên tử tính theo amu", "Thể tích của 1 mol chất khí ở đkc", "Khối lượng của một lít dung dịch"], 0, "Khối lượng mol là khối lượng tính bằng gam của 1 mol chất."),
        make_mc(3, "Nhận biết", "Khối lượng mol của khí oxi (O2) là:", ["32 g/mol", "16 g/mol", "8 g/mol", "64 g/mol"], 0, "M_O2 = 16 * 2 = 32 g/mol."),
        make_mc(4, "Nhận biết", "Công thức tính số mol n khi biết khối lượng m và khối lượng mol M là:", ["n = m / M", "n = m * M", "n = M / m", "n = m + M"], 0, "n = m / M."),
        make_mc(5, "Thông hiểu", "Khối lượng của 0,5 mol kim loại đồng (Cu = 64) là:", ["32 g", "64 g", "16 g", "128 g"], 0, "m = n * M = 0,5 * 64 = 32 g."),
        make_mc(6, "Thông hiểu", "Số mol của 8,8 g khí carbon dioxide (CO2, M = 44 g/mol) là:", ["0,2 mol", "0,1 mol", "0,4 mol", "0,5 mol"], 0, "n = 8,8 / 44 = 0,2 mol."),
        make_mc(7, "Thông hiểu", "Ở điều kiện chuẩn (25 °C và 1 bar), 1 mol của mọi chất khí đều chiếm thể tích là:", ["24,79 lít", "22,4 lít", "24,0 lít", "25,0 lít"], 0, "Theo chuẩn mới đkc (25 °C, 1 bar), 1 mol khí chiếm 24,79 lít."),
        make_mc(8, "Thông hiểu", "Thể tích của 0,2 mol khí hiđro (H2) ở điều kiện chuẩn là:", ["4,958 lít", "4,48 lít", "2,479 lít", "9,916 lít"], 0, "V = 0,2 * 24,79 = 4,958 L."),
        make_mc(9, "Vận dụng", "Trong 0,1 mol khí cacbonic CO2 có chứa bao nhiêu phân tử CO2?", ["6,022 * 10^22 phân tử", "6,022 * 10^23 phân tử", "1,204 * 10^23 phân tử", "3,011 * 10^22 phân tử"], 0, "N_phân tử = 0,1 * 6,022 * 10^23 = 6,022 * 10^22."),
        make_mc(10, "Vận dụng", "Số mol của 4,958 lít khí oxi O2 ở điều kiện chuẩn (25 °C, 1 bar) là:", ["0,2 mol", "0,1 mol", "0,25 mol", "0,5 mol"], 0, "n = 4,958 / 24,79 = 0,2 mol."),
        make_mc(11, "Vận dụng", "Hợp chất X có công thức hóa học XO2. Biết khối lượng mol của X là 64 g/mol. Nguyên tố X là:", ["Lưu huỳnh (S = 32)", "Cacbon (C = 12)", "Nitơ (N = 14)", "Silic (Si = 28)"], 0, "M_X + 32 = 64 -> M_X = 32 (S)."),
        make_mc(12, "Vận dụng cao", "Một mẫu khí A có thể tích 7,437 lít ở đkc và nặng 8,4 g. Khối lượng mol của khí A là:", ["28 g/mol (N2 hoặc CO)", "32 g/mol (O2)", "44 g/mol (CO2)", "16 g/mol (CH4)"], 0, "n = 7,437 / 24,79 = 0,3 mol -> M = 8,4 / 0,3 = 28 g/mol."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các khái niệm mol và số Avogadro:", [
            ("a", "Số Avogadro được kí hiệu là N và có giá trị xấp xỉ 6,022 * 10^23.", True),
            ("b", "Khối lượng mol của một chất có trị số bằng nguyên tử khối hoặc phân tử khối của chất đó.", True),
            ("c", "1 mol sắt và 1 mol nhôm có cùng khối lượng bằng nhau.", False),
            ("d", "1 mol khí oxi và 1 mol khí nitơ chứa cùng số lượng phân tử bằng nhau.", True)
        ], "1 mol Fe nặng 56g, 1 mol Al nặng 27g nên khối lượng khác nhau."),
        make_tf(2, "Thông hiểu", "Về thể tích mol chất khí ở điều kiện chuẩn (25 °C, 1 bar):", [
            ("a", "Ở cùng điều kiện nhiệt độ và áp suất, các thể tích bằng nhau của mọi chất khí đều chứa cùng số mol phân tử.", True),
            ("b", "Thể tích mol của chất khí ở đkc (25 °C, 1 bar) là 24,79 lít/mol.", True),
            ("c", "Thể tích mol của chất lỏng và chất rắn ở đkc cũng bằng 24,79 lít/mol.", False),
            ("d", "Khí nhẹ hơn hay nặng hơn đều chiếm thể tích 24,79 lít cho mỗi mol khí ở đkc.", True)
        ], "24,79 L/mol chỉ áp dụng cho thể khí, không áp dụng cho lỏng và rắn."),
        make_tf(3, "Vận dụng", "Cho 0,5 mol khí N2 ở điều kiện chuẩn:", [
            ("a", "Khối lượng của lượng khí này là 14 g.", True),
            ("b", "Thể tích của lượng khí này ở đkc là 12,395 lít.", True),
            ("c", "Lượng khí này chứa 3,011 * 10^23 phân tử nitơ N2.", True),
            ("d", "Số nguyên tử nitơ N có trong lượng khí này là 3,011 * 10^23 nguyên tử.", False)
        ], "Số nguyên tử N gấp đôi số phân tử N2, tức là 6,022 * 10^23 nguyên tử."),
        make_tf(4, "Vận dụng cao", "Xét hỗn hợp khí gồm 0,1 mol O2 và 0,4 mol N2 ở đkc:", [
            ("a", "Tổng thể tích của hỗn hợp khí ở đkc là 12,395 lít.", True),
            ("b", "Tổng khối lượng của hỗn hợp khí là 14,4 g.", True),
            ("c", "Khối lượng mol trung bình của hỗn hợp khí là 28,8 g/mol.", True),
            ("d", "Hỗn hợp khí này nặng hơn không khí.", False)
        ], "M_tb = 28,8 < 29 nên hỗn hợp nhẹ hơn không khí một chút.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Khối lượng mol của nguyên tử sắt Fe là bao nhiêu g/mol?", "56", "M_Fe = 56 g/mol."),
        make_sa(2, "Thông hiểu", "Khối lượng của 0,25 mol canxi cacbonat CaCO3 (M = 100 g/mol) là bao nhiêu gam? (Ghi số thập phân)", "25", "m = 0,25 * 100 = 25 g."),
        make_sa(3, "Thông hiểu", "Thể tích của 2 mol khí oxi O2 ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Ghi số thập phân)", "49,58", "V = 2 * 24,79 = 49,58 L."),
        make_sa(4, "Vận dụng", "Trong 0,5 mol phân tử H2O có chứa bao nhiêu mol nguyên tử H?", "1", "1 mol H2O có 2 mol H -> 0,5 mol H2O có 1 mol H."),
        make_sa(5, "Vận dụng", "Đốt cháy hết 0,2 mol carbon cần vừa đủ bao nhiêu lít khí oxi ở đkc? (Ghi số thập phân)", "4,958", "n_O2 = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."),
        make_sa(6, "Vận dụng cao", "Khối lượng của 1,5 mol hợp chất MgSO4 (M = 120 g/mol) là bao nhiêu gam?", "180", "m = 1,5 * 120 = 180 g.")
    ],
    "part4": [
        make_vdc(1, "Một bình kín chứa hỗn hợp gồm 0,2 mol khí CO2 và 0,3 mol khí O2 ở điều kiện chuẩn. Khối lượng và thể tích của hỗn hợp khí lần lượt là:", ["18,4 g và 12,395 lít", "17,6 g và 11,2 lít", "18,4 g và 11,2 lít", "16,0 g và 12,395 lít"], 0, "m = 0,2*44 + 0,3*32 = 8,8 + 9,6 = 18,4 g; V = 0,5 * 24,79 = 12,395 L."),
        make_vdc(2, "Khối lượng của 12,044 * 10^23 phân tử khí metan CH4 (M = 16 g/mol) là bao nhiêu gam?", ["32 g", "16 g", "48 g", "8 g"], 0, "n = 12,044*10^23 / (6,022*10^23) = 2 mol -> m = 2 * 16 = 32 g."),
        make_vdc(3, "Hỗn hợp X gồm khí SO2 và O2 có tỉ lệ mol 1 : 1. Khối lượng mol trung bình của hỗn hợp X là:", ["48 g/mol", "32 g/mol", "64 g/mol", "96 g/mol"], 0, "M_tb = (64 + 32) / 2 = 48 g/mol."),
        make_vdc(4, "Đốt cháy hoàn toàn m gam kim loại sắt cần vừa đủ 3,7185 lít khí O2 ở đkc thu được oxit sắt từ Fe3O4. Biết n_O2 = 3,7185 / 24,79 = 0,15 mol. Giá trị của m là:", ["12,6 g", "8,4 g", "16,8 g", "11,2 g"], 0, "3Fe + 2O2 -> Fe3O4. n_Fe = 0,15 * 1,5 = 0,225 mol -> m_Fe = 0,225 * 56 = 12,6 g.")
    ]
}

# --- ĐỀ 2: Tỉ khối của chất khí, so sánh nặng nhẹ hơn không khí ---
exams_c1_p3["chem8_c1_b5_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Công thức tính tỉ khối của khí A đối với khí B là:", ["d_A/B = M_A / M_B", "d_A/B = M_B / M_A", "d_A/B = M_A * M_B", "d_A/B = M_A + M_B"], 0, "d_A/B = M_A / M_B."),
        make_mc(2, "Nhận biết", "Khối lượng mol quy ước của không khí là:", ["29 g/mol", "28 g/mol", "32 g/mol", "18 g/mol"], 0, "M_kk xấp xỉ 29 g/mol (0,8 * 28 + 0,2 * 32)."),
        make_mc(3, "Nhận biết", "Khí nào sau đây nhẹ hơn không khí?", ["CH4 (metan)", "CO2 (cacbonic)", "O2 (oxi)", "SO2 (sunfurơ)"], 0, "M_CH4 = 16 < 29 nên nhẹ hơn không khí."),
        make_mc(4, "Nhận biết", "Để thu khí hiđro vào bình bằng phương pháp đẩy không khí, ta phải đặt bình như thế nào?", ["Úp ngược miệng bình xuống dưới", "Để ngửa miệng bình lên trên", "Đặt nằm ngang trên bàn", "Nghiêng góc 45 độ"], 0, "H2 rất nhẹ (M=2) nên bay lên trên, ta phải úp ngược bình."),
        make_mc(5, "Thông hiểu", "Tỉ khối của khí oxi O2 đối với khí hiđro H2 là:", ["16", "32", "8", "2"], 0, "d_O2/H2 = 32 / 2 = 16."),
        make_mc(6, "Thông hiểu", "Khí carbon dioxide CO2 nặng gấp bao nhiêu lần không khí? (lấy xấp xỉ)", ["1,52 lần", "1,2 lần", "0,8 lần", "2,0 lần"], 0, "d_CO2/kk = 44 / 29 xấp xỉ 1,52."),
        make_mc(7, "Thông hiểu", "Để thu khí CO2 bằng cách đẩy không khí, người ta phải đặt ống nghiệm hoặc bình thu thế nào?", ["Ngửa miệng bình lên trên", "Úp ngược miệng bình xuống", "Đậy kín nắp khi thu", "Nhúng chìm bình vào nước"], 0, "CO2 nặng hơn không khí (d = 1,52) nên chìm xuống đáy, ta đặt ngửa bình."),
        make_mc(8, "Thông hiểu", "Khí sunfurơ (SO2) nặng gấp bao nhiêu lần khí oxi (O2)?", ["2 lần", "1,5 lần", "3 lần", "4 lần"], 0, "d_SO2/O2 = 64 / 32 = 2."),
        make_mc(9, "Vận dụng", "Một chất khí X có tỉ khối đối với khí oxi là 1,375. Khối lượng mol của khí X là:", ["44 g/mol (CO2 hoặc N2O)", "34 g/mol (H2S)", "28 g/mol (N2)", "64 g/mol (SO2)"], 0, "M_X = 1,375 * 32 = 44 g/mol."),
        make_mc(10, "Vận dụng", "Khí A có tỉ khối đối với không khí d_A/kk = 0,55. Khí A là chất nào sau đây?", ["CH4 (M = 16)", "NH3 (M = 17)", "CO (M = 28)", "C2H2 (M = 26)"], 0, "M_A = 0,55 * 29 = 15,95 xấp xỉ 16 (CH4)."),
        make_mc(11, "Vận dụng", "Trong các hang sâu hoặc giếng sâu lâu ngày, người ta thường gặp hiện tượng tích tụ khí nào gây ngạt thở do khí đó nặng chìm ở đáy?", ["CO2 (cacbonic)", "H2 (hiđro)", "CH4 (metan)", "N2 (nitơ)"], 0, "CO2 nặng hơn không khí nên tích tụ ở đáy giếng, hang sâu."),
        make_mc(12, "Vận dụng cao", "Một hỗn hợp khí gồm CO và CO2 có tỉ khối đối với hiđro là 18. Phần trăm thể tích của khí CO trong hỗn hợp là:", ["50%", "40%", "60%", "25%"], 0, "M_tb = 18 * 2 = 36. Áp dụng quy tắc đường chéo: (44-36) : (36-28) = 8 : 8 = 1 : 1 -> 50%."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về tỉ khối của chất khí:", [
            ("a", "Tỉ khối của chất khí là đại lượng không có đơn vị đo.", True),
            ("b", "Khí có tỉ khối đối với không khí lớn hơn 1 thì nặng hơn không khí.", True),
            ("c", "Khí hiđro là chất khí nhẹ nhất trong tất cả các chất khí đã biết.", True),
            ("d", "Khí clo (Cl2 = 71) nhẹ hơn không khí nên bay lơ lửng trên cao.", False)
        ], "Cl2 nặng hơn không khí rất nhiều (71/29 = 2,45) nên chìm sát mặt đất."),
        make_tf(2, "Thông hiểu", "Về phương pháp thu khí trong phòng thí nghiệm:", [
            ("a", "Khí ít tan hoặc không tan trong nước có thể thu bằng phương pháp đẩy nước.", True),
            ("b", "Khí tan nhiều trong nước như NH3, HCl không thể thu bằng phương pháp đẩy nước.", True),
            ("c", "Để thu khí nặng hơn không khí (như O2, CO2, Cl2), ta đặt ngửa miệng bình thu.", True),
            ("d", "Để thu khí nhẹ hơn không khí (như H2, CH4), ta cũng đặt ngửa miệng bình thu.", False)
        ], "Khí nhẹ hơn không khí phải úp ngược bình."),
        make_tf(3, "Vận dụng", "Về các khí quen thuộc trong đời sống:", [
            ("a", "Khí heli (He = 4) nhẹ hơn không khí nên được bơm vào bóng bay, khí cầu.", True),
            ("b", "Khí gas đun bếp (propan C3H8, butan C4H10) nặng hơn không khí nên khi rò rỉ sẽ tích tụ dưới sàn nhà.", True),
            ("c", "Khí cacbon oxit (CO = 28) xấp xỉ bằng khối lượng không khí (29) nên khuếch tán đều trong phòng kín.", True),
            ("d", "Khí oxi nặng hơn khí nitơ.", True)
        ], "M_O2 = 32 > M_N2 = 28."),
        make_tf(4, "Vận dụng cao", "Xét hỗn hợp X gồm 2 khí H2 và O2 có tỉ lệ thể tích 2 : 1:", [
            ("a", "Khối lượng mol trung bình của hỗn hợp X là 12 g/mol.", True),
            ("b", "Hỗn hợp X nhẹ hơn không khí.", True),
            ("c", "Tỉ khối của hỗn hợp X đối với heli là 3.", True),
            ("d", "Khi đốt cháy hỗn hợp X, phản ứng xảy ra êm dịu không gây tiếng nổ.", False)
        ], "Tỉ lệ 2 H2 : 1 O2 là hỗn hợp nổ cực mạnh.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Tỉ khối của khí SO2 (M = 64) đối với khí O2 (M = 32) bằng bao nhiêu?", "2", "64 / 32 = 2."),
        make_sa(2, "Thông hiểu", "Khí metan CH4 có khối lượng mol là 16 g/mol. Tỉ khối của CH4 đối với khí H2 là bao nhiêu?", "8", "16 / 2 = 8."),
        make_sa(3, "Thông hiểu", "Một chất khí A có d_A/H2 = 14. Khối lượng mol của khí A là bao nhiêu g/mol?", "28", "M = 14 * 2 = 28 g/mol."),
        make_sa(4, "Vận dụng", "Cho các khí: O2, CO2, H2, CH4, Cl2, NH3. Có bao nhiêu khí nhẹ hơn không khí (M < 29)?", "3", "H2 (2), CH4 (16), NH3 (17) -> 3 khí nhẹ hơn không khí."),
        make_sa(5, "Vận dụng", "Tỉ khối của một oxit của nitơ đối với khí H2 là 23. Phân tử khối của oxit đó là bao nhiêu?", "46", "M = 23 * 2 = 46 (NO2)."),
        make_sa(6, "Vận dụng cao", "Hỗn hợp gồm 0,1 mol khí O2 và 0,1 mol khí N2 có tổng thể tích ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Ghi số thập phân)", "4,958", "V = 0,2 * 24,79 = 4,958 L.")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất khí của lưu huỳnh và oxi có tỉ khối đối với khí oxi bằng 2,5. Công thức hóa học của oxit đó là:", ["SO3 (lưu huỳnh trioxit)", "SO2 (lưu huỳnh đioxit)", "SO (lưu huỳnh monooxit)", "S2O (đilưu huỳnh oxit)"], 0, "M = 2,5 * 32 = 80 -> SO3."),
        make_vdc(2, "Hỗn hợp khí X gồm H2 và CH4 có tỉ khối so với heli (He = 4) bằng 2,25. Khối lượng mol trung bình của hỗn hợp X là 9 g/mol. Phần trăm thể tích của khí H2 trong hỗn hợp là:", ["50%", "40%", "60%", "25%"], 0, "M_tb = 9. Đường chéo: (16-9) : (9-2) = 7 : 7 = 1 : 1 -> 50%."),
        make_vdc(3, "Trong phòng thí nghiệm, khí nào sau đây KHÔNG THỂ thu bằng phương pháp đẩy nước?", ["Khí hiđroclorua (HCl) vì tan cực kì nhiều trong nước", "Khí oxi vì ít tan trong nước", "Khí hiđro vì ít tan trong nước", "Khí nitơ vì ít tan trong nước"], 0, "HCl tan vô hạn trong nước tạo dung dịch axit nên không thể đẩy nước."),
        make_vdc(4, "Nạp đầy một quả bóng bay bằng 2,479 lít khí hiđro ở đkc. Khối lượng khí hiđro trong quả bóng là:", ["0,2 g", "0,1 g", "0,4 g", "2,0 g"], 0, "n_H2 = 2,479 / 24,79 = 0,1 mol -> m = 0,1 * 2 = 0,2 g.")
    ]
}

# --- ĐỀ 3: Tính toán hỗn hợp khí, số hạt, chuyển đổi đại lượng ---
exams_c1_p3["chem8_c1_b5_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Đơn vị đo khối lượng mol M là:", ["g/mol", "gam", "mol", "lít/mol"], 0, "Khối lượng mol có đơn vị là g/mol."),
        make_mc(2, "Nhận biết", "Trong 1 mol phân tử axit sunfuric H2SO4 có chứa bao nhiêu mol nguyên tử oxi?", ["4 mol", "2 mol", "1 mol", "7 mol"], 0, "Chỉ số oxi là 4 nên có 4 mol nguyên tử O."),
        make_mc(3, "Nhận biết", "Số mol của 9,916 lít khí N2 ở điều kiện chuẩn (25 °C, 1 bar) là:", ["0,4 mol", "0,2 mol", "0,5 mol", "0,1 mol"], 0, "n = 9,916 / 24,79 = 0,4 mol."),
        make_mc(4, "Nhận biết", "Tỉ khối của khí lưu huỳnh đioxit SO2 đối với không khí là:", ["2,21", "1,52", "0,97", "1,10"], 0, "d = 64 / 29 xấp xỉ 2,21."),
        make_mc(5, "Thông hiểu", "Khối lượng của 0,3 mol muối ăn NaCl (M = 58,5 g/mol) là:", ["17,55 g", "11,7 g", "5,85 g", "23,4 g"], 0, "m = 0,3 * 58,5 = 17,55 g."),
        make_mc(6, "Thông hiểu", "Ở điều kiện chuẩn, 1,2395 lít khí oxi O2 có số mol là:", ["0,05 mol", "0,1 mol", "0,02 mol", "0,5 mol"], 0, "n = 1,2395 / 24,79 = 0,05 mol."),
        make_mc(7, "Thông hiểu", "Khí nào sau đây có tỉ khối đối với khí hiđro bằng 14?", ["N2 và CO", "O2", "CO2", "CH4"], 0, "M = 14 * 2 = 28 -> N2 và CO."),
        make_mc(8, "Thông hiểu", "Số phân tử có trong 0,25 mol nước là:", ["1,5055 * 10^23 phân tử", "6,022 * 10^23 phân tử", "3,011 * 10^23 phân tử", "1,2044 * 10^23 phân tử"], 0, "N = 0,25 * 6,022 * 10^23 = 1,5055 * 10^23."),
        make_mc(9, "Vận dụng", "Đốt cháy hoàn toàn 6,0 g carbon trong oxi dư. Thể tích khí CO2 thu được ở điều kiện chuẩn là:", ["12,395 lít", "24,79 lít", "11,2 lít", "6,72 lít"], 0, "n_C = 6 / 12 = 0,5 mol -> V_CO2 = 0,5 * 24,79 = 12,395 L."),
        make_mc(10, "Vận dụng", "Một hợp chất có thành phần gồm 75% C và 25% H về khối lượng, khối lượng mol là 16 g/mol. Công thức phân tử của hợp chất là:", ["CH4", "C2H6", "C2H4", "C3H8"], 0, "m_C = 16*0,75 = 12 (1C); m_H = 4 (4H) -> CH4."),
        make_mc(11, "Vận dụng", "Một bình khí chứa hỗn hợp gồm 0,5 mol O2 và 1,5 mol N2. Khối lượng của hỗn hợp khí trong bình là:", ["58 g", "56 g", "60 g", "64 g"], 0, "m = 0,5*32 + 1,5*28 = 16 + 42 = 58 g."),
        make_mc(12, "Vận dụng cao", "Hỗn hợp X gồm khí O2 và O3 có tỉ khối đối với hiđro bằng 20. Khối lượng mol trung bình của hỗn hợp X là 40 g/mol. Phần trăm thể tích của O3 trong hỗn hợp X là:", ["50%", "25%", "75%", "33,3%"], 0, "Áp dụng đường chéo: (48-40) : (40-32) = 8 : 8 = 1 : 1 -> 50%."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các công thức biến đổi giữa khối lượng, thể tích và số mol:", [
            ("a", "m = n * M (khối lượng bằng số mol nhân khối lượng mol).", True),
            ("b", "V = n * 24,79 (thể tích khí ở đkc 25 °C, 1 bar).", True),
            ("c", "N = n * 6,022 * 10^23 (số hạt bằng số mol nhân số Avogadro).", True),
            ("d", "Khối lượng mol của hỗn hợp khí luôn bằng tổng khối lượng mol của các khí thành phần.", False)
        ], "M_tb là trung bình cộng theo tỉ lệ mol, không phải phép cộng trực tiếp."),
        make_tf(2, "Thông hiểu", "Về ứng dụng tỉ khối trong an toàn đời sống:", [
            ("a", "Khí metan nhẹ hơn không khí nên dễ thoát lên trần nhà khi bị rò rỉ.", True),
            ("b", "Khí gas bếp (propan/butan) nặng hơn không khí nên chìm sát mặt sàn, gây nguy cơ cháy nổ cao.", True),
            ("c", "Khí cacbon monooxit (CO) có thể tích tụ lâu trong phòng kín vì khối lượng xấp xỉ không khí.", True),
            ("d", "Người ta có thể ngửi thấy mùi khí CO vì khí CO có mùi khai nồng nặc.", False)
        ], "Khí CO không màu, không mùi, cực kì độc hại."),
        make_tf(3, "Vận dụng", "Cho 11,2 g bột sắt Fe phản ứng hết với axit HCl dư:", [
            ("a", "Số mol sắt tham gia phản ứng là 0,2 mol.", True),
            ("b", "Phương trình: Fe + 2HCl -> FeCl2 + H2.", True),
            ("c", "Số mol khí hiđro sinh ra là 0,2 mol.", True),
            ("d", "Thể tích khí hiđro thu được ở đkc (25 °C, 1 bar) là 4,48 lít.", False)
        ], "Ở đkc: V = 0,2 * 24,79 = 4,958 L."),
        make_tf(4, "Vận dụng cao", "Xét mẫu khí nitơ N2 có thể tích 12,395 lít ở đkc:", [
            ("a", "Số mol phân tử N2 trong mẫu là 0,5 mol.", True),
            ("b", "Khối lượng của mẫu khí nitơ là 14 g.", True),
            ("c", "Mẫu khí chứa 3,011 * 10^23 phân tử nitơ.", True),
            ("d", "Tổng số nguyên tử nitơ chứa trong mẫu là 6,022 * 10^23 nguyên tử.", True)
        ], "0,5 mol N2 có 1 mol nguyên tử N = 6,022 * 10^23 nguyên tử.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Khối lượng mol của phân tử nước H2O là bao nhiêu g/mol?", "18", "M_H2O = 1*2 + 16 = 18 g/mol."),
        make_sa(2, "Thông hiểu", "Khối lượng của 0,5 mol khí cacbon đioxit CO2 là bao nhiêu gam?", "22", "m = 0,5 * 44 = 22 g."),
        make_sa(3, "Thông hiểu", "Số mol của 7,437 lít khí O2 ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu mol? (Ghi số thập phân)", "0,3", "n = 7,437 / 24,79 = 0,3 mol."),
        make_sa(4, "Vận dụng", "Tỉ khối của khí A đối với không khí là 1,1. Khối lượng mol của khí A (làm tròn số nguyên) là bao nhiêu g/mol?", "32", "M = 1,1 * 29 = 31,9 xấp xỉ 32 g/mol."),
        make_sa(5, "Vận dụng", "Trong 0,2 mol phân tử Fe2O3 có bao nhiêu mol nguyên tử sắt Fe? (Ghi số thập phân)", "0,4", "0,2 * 2 = 0,4 mol Fe."),
        make_sa(6, "Vận dụng cao", "Đốt cháy 0,1 mol khí CH4 thu được bao nhiêu gam nước? (Ghi số thập phân)", "3,6", "CH4 + 2O2 -> CO2 + 2H2O. n_H2O = 0,2 mol -> m = 3,6 g.")
    ],
    "part4": [
        make_vdc(1, "Đốt cháy hoàn toàn 2,4 g kim loại Mg trong bình chứa đầy khí oxi dư. Thể tích khí oxi tối thiểu (đkc, 25 °C, 1 bar) đã tham gia phản ứng là:", ["1,2395 lít", "2,479 lít", "1,12 lít", "2,24 lít"], 0, "2Mg + O2 -> 2MgO. n_Mg = 0,1 mol -> n_O2 = 0,05 mol -> V = 0,05 * 24,79 = 1,2395 L."),
        make_vdc(2, "Cho 10 g hỗn hợp gồm CaCO3 và MgCO3 có tỉ lệ mol 1 : 1. Số mol của mỗi chất trong hỗn hợp là bao nhiêu? (Biết 100x + 84x = 10)", ["0,0543 mol", "0,1 mol", "0,05 mol", "0,02 mol"], 0, "184x = 10 -> x xấp xỉ 0,0543 mol."),
        make_vdc(3, "Một hợp chất khí X có tỉ khối đối với oxi là 0,5. Khí X cháy trong oxi sinh ra khí nitơ và hơi nước. Khí X là:", ["NH3 (amoniac, M = 17)", "CH4 (metan, M = 16)", "H2 (hiđro, M = 2)", "N2 (nitơ, M = 28)"], 1, "M_X = 0,5 * 32 = 16 (CH4; hoặc NH3 = 17, 16/32 = 0,5 chính xác là CH4)."),
        make_vdc(4, "Một bình kín có dung tích 4,958 lít chứa đầy khí oxi ở đkc. Nếu đưa vào bình m gam bột than C rồi đốt cháy hoàn toàn thì thu được tối đa bao nhiêu gam khí CO2?", ["8,8 g", "4,4 g", "17,6 g", "13,2 g"], 0, "n_O2 = 4,958 / 24,79 = 0,2 mol -> n_CO2 = 0,2 mol -> m_CO2 = 0,2 * 44 = 8,8 g.")
    ]
}

print("Đã nạp xong Bài 5 (3 đề độc lập 100%)")
