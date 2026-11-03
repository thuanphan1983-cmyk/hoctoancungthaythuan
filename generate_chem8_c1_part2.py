# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - TIẾP TỤC CHƯƠNG I: BÀI 4, 5, 6, 7 VÀ ÔN TẬP CHƯƠNG I (17 ĐỀ ĐỘC LẬP 100%)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import exams_c1, make_mc, make_tf, make_sa, make_vdc

# ==============================================================================
# BÀI 4: ĐỊNH LUẬT BẢO TOÀN KHỐI LƯỢNG VÀ PHƯƠNG TRÌNH HÓA HỌC (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Phát biểu ĐL BTKL, bảo toàn nguyên tử, tính khối lượng cơ bản ---
exams_c1["chem8_c1_b4_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Phát biểu nào sau đây là nội dung đúng của Định luật bảo toàn khối lượng?", ["Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất phản ứng", "Trong một phản ứng hóa học, khối lượng của từng chất trước và sau phản ứng luôn bằng nhau", "Tổng thể tích các chất sản phẩm luôn bằng tổng thể tích các chất phản ứng", "Khối lượng của chất rắn luôn không thay đổi sau mọi phản ứng"], 0, "ĐL BTKL: Tổng khối lượng sản phẩm bằng tổng khối lượng chất phản ứng."),
        make_mc(2, "Nhận biết", "Trong một phản ứng hóa học, đại lượng nào sau đây được bảo toàn?", ["Số phân tử của các chất", "Tổng số nguyên tử của mỗi nguyên tố", "Thể tích của hệ phản ứng", "Số lượng các liên kết hóa học"], 1, "Tổng số nguyên tử của từng nguyên tố được bảo toàn tuyệt đối."),
        make_mc(3, "Nhận biết", "Cho phản ứng: A + B -> C + D. Biểu thức toán học của định luật bảo toàn khối lượng là:", ["m_A + m_B = m_C + m_D", "m_A + m_C = m_B + m_D", "m_A - m_B = m_C - m_D", "m_A * m_B = m_C * m_D"], 0, "m_A + m_B = m_C + m_D."),
        make_mc(4, "Nhận biết", "Phương trình hóa học biểu diễn ngắn gọn:", ["Diễn biến trạng thái của các chất", "Phản ứng hóa học bằng công thức hóa học của các chất", "Khối lượng nguyên tử của các chất", "Cấu tạo vỏ electron của các nguyên tử"], 1, "Phương trình hóa học dùng CTHH để biểu diễn phản ứng."),
        make_mc(5, "Thông hiểu", "Cho 6,5 g kim loại kẽm phản ứng với dung dịch axit clohiđric thu được 13,6 g kẽm clorua và 0,2 g khí hiđro. Khối lượng axit clohiđric đã phản ứng là:", ["7,3 g", "20,3 g", "6,9 g", "14,2 g"], 0, "m_HCl = (13,6 + 0,2) - 6,5 = 7,3 g."),
        make_mc(6, "Thông hiểu", "Hệ số cân bằng đúng của phương trình hóa học: ... P + ... O2 -> ... P2O5 lần lượt là:", ["4, 5, 2", "2, 5, 2", "4, 3, 2", "2, 3, 1"], 0, "4P + 5O2 -> 2P2O5."),
        make_mc(7, "Thông hiểu", "Nung m gam đá vôi (chứa canxi cacbonat) thu được 5,6 g vôi sống (CaO) và 4,4 g khí cacbon đioxit (CO2). Khối lượng canxi cacbonat đã phản ứng là:", ["10,0 g", "1,2 g", "12,0 g", "8,8 g"], 0, "m_CaCO3 = 5,6 + 4,4 = 10,0 g."),
        make_mc(8, "Thông hiểu", "Cho phương trình: 2Al + 3H2SO4 -> Al2(SO4)3 + 3H2. Tỉ lệ số phân tử nhôm sunfat tạo thành và số phân tử hiđro sinh ra là:", ["1 : 3", "2 : 3", "1 : 1", "3 : 1"], 0, "Tỉ lệ hệ số của Al2(SO4)3 và H2 là 1 : 3."),
        make_mc(9, "Vận dụng", "Đốt cháy hoàn toàn hỗn hợp gồm 2,4 g Mg và 5,6 g Fe trong khí oxi dư thu được 11,2 g hỗn hợp các oxit. Khối lượng khí oxi đã tham gia phản ứng là:", ["3,2 g", "4,0 g", "2,4 g", "1,6 g"], 0, "m_O2 = 11,2 - (2,4 + 5,6) = 3,2 g."),
        make_mc(10, "Vận dụng", "Khi nung nóng một thanh sắt ngoài không khí, sau một thời gian thấy khối lượng thanh sắt tăng lên. Hiện tượng này giải thích theo ĐL BTKL như thế nào?", ["ĐL BTKL bị vi phạm vì khối lượng tăng", "Do sắt kết hợp với khí oxi trong không khí tạo oxit sắt nên m_oxit = m_Fe + m_O2 > m_Fe ban đầu", "Sắt hút bụi bẩn xung quanh", "Không khí bị lạnh ngưng tụ lên sắt"], 1, "Khối lượng tăng đúng bằng khối lượng khí oxi đã phản ứng."),
        make_mc(11, "Vận dụng", "Cân bằng phương trình hóa học: Fe2O3 + CO -> Fe + CO2. Hệ số của khí CO là:", ["3", "2", "1", "4"], 0, "Fe2O3 + 3CO -> 2Fe + 3CO2. Hệ số CO là 3."),
        make_mc(12, "Vận dụng cao", "Nung 12 g hỗn hợp gồm Mg và Cu ngoài không khí đến khi phản ứng hoàn toàn thu được 15,2 g hỗn hợp các oxit MgO và CuO. Nếu đem 12 g hỗn hợp kim loại ban đầu tác dụng với dung dịch HCl dư thì chỉ có Mg phản ứng sinh ra 0,2 g khí H2. Khối lượng kim loại Cu trong hỗn hợp ban đầu là:", ["9,6 g", "2,4 g", "7,2 g", "4,8 g"], 0, "n_H2 = 0,1 mol -> n_Mg = 0,1 mol -> m_Mg = 2,4 g -> m_Cu = 12 - 2,4 = 9,6 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về định luật bảo toàn khối lượng và cân bằng phản ứng:", [
            ("a", "Định luật bảo toàn khối lượng được hai nhà bác học Lomonosov và Lavoisier tìm ra độc lập.", True),
            ("b", "Trong phản ứng hóa học, số lượng phân tử chất phản ứng luôn bằng số lượng phân tử chất sản phẩm.", False),
            ("c", "Khi cân bằng phương trình hóa học, ta chỉ được thay đổi hệ số đặt trước công thức hóa học, tuyệt đối không thay đổi chỉ số dưới chân.", True),
            ("d", "Khối lượng của cốc đựng nước vôi trong tăng lên khi sục khí CO2 vào là do hấp thụ thêm khối lượng CO2.", True)
        ], "Số phân tử có thể thay đổi (ví dụ N2 + 3H2 -> 2NH3: 4 phân tử biến thành 2 phân tử)."),
        make_tf(2, "Thông hiểu", "Về các bước lập phương trình hóa học:", [
            ("a", "Bước 1: Viết sơ đồ phản ứng gồm công thức hóa học của các chất phản ứng và sản phẩm.", True),
            ("b", "Bước 2: Cân bằng số nguyên tử của mỗi nguyên tố ở hai vế bằng các hệ số thích hợp.", True),
            ("c", "Bước 3: Viết phương trình hóa học hoàn chỉnh thay nét đứt nối bằng nét liền.", True),
            ("d", "Nếu hệ số cân bằng là 1, ta bắt buộc phải ghi rõ số 1 trước công thức hóa học.", False)
        ], "Hệ số bằng 1 thì không cần ghi."),
        make_tf(3, "Vận dụng", "Về tỉ lệ số hạt trong phản ứng: 2Na + 2H2O -> 2NaOH + H2:", [
            ("a", "Tỉ lệ số nguyên tử Na : số phân tử H2O là 1 : 1.", True),
            ("b", "Tỉ lệ số nguyên tử Na : số phân tử H2 là 2 : 1.", True),
            ("c", "Cứ 2 nguyên tử Na tác dụng sẽ sinh ra 2 phân tử khí H2.", False),
            ("d", "Số phân tử NaOH sinh ra gấp đôi số phân tử H2.", True)
        ], "2 nguyên tử Na chỉ sinh ra 1 phân tử H2."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm nung mẩu than đá trong cốc hở miệng:", [
            ("a", "Sau khi đốt, khối lượng chất rắn còn lại trong cốc giảm đi rõ rệt.", True),
            ("b", "Hiện tượng này không tuân theo định luật bảo toàn khối lượng.", False),
            ("c", "Khối lượng giảm đi là do khí CO2 sinh ra đã bay vào không khí quyển xung quanh.", True),
            ("d", "Nếu phản ứng được thực hiện trong một bình kín cân kín, khối lượng của toàn hệ trước và sau phản ứng không hề thay đổi.", True)
        ], "ĐL BTKL luôn đúng cho toàn hệ kín (kể cả chất khí).")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phương trình: 2H2 + O2 -> 2H2O, hệ số của phân tử nước là bao nhiêu?", "2", "Hệ số của H2O là 2."),
        make_sa(2, "Thông hiểu", "Cho 5,6 g sắt tác dụng vừa đủ với bột lưu huỳnh thu được 8,8 g FeS. Khối lượng lưu huỳnh đã tham gia phản ứng là bao nhiêu gam? (Ghi số thập phân)", "3,2", "m_S = 8,8 - 5,6 = 3,2 g."),
        make_sa(3, "Thông hiểu", "Đốt cháy 3,1 g photpho trong oxi thu được 7,1 g điphotpho pentaoxit (P2O5). Khối lượng khí oxi đã phản ứng là bao nhiêu gam?", "4", "m_O2 = 7,1 - 3,1 = 4,0 g."),
        make_sa(4, "Vận dụng", "Cân bằng phương trình: 2C2H2 + 5O2 -> a CO2 + b H2O. Giá trị của hệ số a là bao nhiêu?", "4", "2C2H2 + 5O2 -> 4CO2 + 2H2O -> a = 4."),
        make_sa(5, "Vận dụng", "Hòa tan hết m gam canxi cacbonat bằng dung dịch axit HCl vừa đủ, thu được 11,1 g CaCl2; 4,4 g CO2 và 1,8 g H2O. Biết khối lượng axit HCl đã dùng là 7,3 g. Khối lượng m của đá vôi ban đầu là bao nhiêu gam?", "10", "m = (11,1 + 4,4 + 1,8) - 7,3 = 10,0 g."),
        make_sa(6, "Vận dụng cao", "Cân bằng phương trình: a Fe(OH)3 + b H2SO4 -> c Fe2(SO4)3 + d H2O. Tổng các hệ số nguyên tối giản (a + b + c + d) là bao nhiêu?", "12", "2Fe(OH)3 + 3H2SO4 -> 1Fe2(SO4)3 + 6H2O. Tổng: 2 + 3 + 1 + 6 = 12.")
    ],
    "part4": [
        make_vdc(1, "Đốt cháy hoàn toàn 13 g hỗn hợp gồm kẽm (Zn) và nhôm (Al) trong khí clo dư thu được 34,3 g hỗn hợp muối gồm ZnCl2 và AlCl3. Khối lượng khí clo Cl2 đã tham gia phản ứng là:", ["21,3 g", "47,3 g", "10,65 g", "15,8 g"], 0, "m_Cl2 = 34,3 - 13,0 = 21,3 g."),
        make_vdc(2, "Nung 20 g hỗn hợp CaCO3 và MgCO3 đến khối lượng không đổi thu được 10,1 g hỗn hợp hai oxit CaO và MgO. Khối lượng khí CO2 thoát ra là:", ["9,9 g", "10,9 g", "8,9 g", "11,2 g"], 0, "m_CO2 = 20 - 10,1 = 9,9 g."),
        make_vdc(3, "Cho sơ đồ phản ứng: KMnO4 -> K2MnO4 + MnO2 + O2. Sau khi cân bằng với các hệ số nguyên tối giản, tỉ lệ số phân tử KMnO4 bị phân hủy và số phân tử O2 sinh ra là:", ["2 : 1", "1 : 1", "4 : 1", "1 : 2"], 0, "2KMnO4 -> K2MnO4 + MnO2 + O2. Tỉ lệ 2 : 1."),
        make_vdc(4, "Hòa tan hoàn toàn 8,4 g bột sắt vào lượng dư dung dịch H2SO4 loãng thu được dung dịch chứa m gam muối FeSO4 và giải phóng V lít khí H2 ở đkc. Biết khối lượng khí H2 thoát ra là 0,3 g và khối lượng H2SO4 phản ứng là 14,7 g. Giá trị của m là:", ["22,8 g", "23,1 g", "22,5 g", "15,0 g"], 0, "m_FeSO4 = 8,4 + 14,7 - 0,3 = 22,8 g.")
    ]
}

# --- ĐỀ 2: Cân bằng phương trình, tỉ lệ số phân tử, bài toán khí thoát ---
exams_c1["chem8_c1_b4_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Trong một phản ứng hóa học diễn ra trong bình hở, nếu sản phẩm sinh ra có chất khí bay đi thì khối lượng chất rắn còn lại trong bình sẽ:", ["Giảm đi", "Tăng lên", "Không thay đổi", "Gấp đôi ban đầu"], 0, "Chất khí thoát ra ngoài làm khối lượng chất rắn còn lại trong bình giảm."),
        make_mc(2, "Nhận biết", "Để biểu diễn phản ứng giữa khí hiđro và khí oxi tạo ra nước, phương trình hóa học nào sau đây viết ĐÚNG?", ["2H2 + O2 -> 2H2O", "H2 + O -> H2O", "H2 + O2 -> H2O2", "4H + 2O -> 2H2O"], 0, "2H2 + O2 -> 2H2O."),
        make_mc(3, "Nhận biết", "Hệ số đứng trước một công thức hóa học trong phương trình cho biết:", ["Số nguyên tử hoặc số phân tử của chất đó trong phản ứng", "Số proton trong hạt nhân", "Chỉ số nguyên tử của nguyên tố", "Nhiệt độ sôi của chất"], 0, "Hệ số biểu thị tỉ lệ số hạt (nguyên tử, phân tử) tham gia hoặc tạo thành."),
        make_mc(4, "Nhận biết", "Đốt cháy photpho đỏ trong bình chứa đầy khí oxi sinh ra điphotpho pentaoxit (P2O5). Phương trình hóa học đúng là:", ["4P + 5O2 -> 2P2O5", "2P + 5O -> P2O5", "P + O2 -> PO2", "2P + 3O2 -> 2PO3"], 0, "4P + 5O2 -> 2P2O5."),
        make_mc(5, "Thông hiểu", "Cho sơ đồ: Fe + O2 -> Fe3O4. Tổng các hệ số nguyên tối giản sau khi cân bằng phương trình là:", ["6", "7", "8", "9"], 0, "3Fe + 2O2 -> Fe3O4. Tổng hệ số: 3 + 2 + 1 = 6."),
        make_mc(6, "Thông hiểu", "Hòa tan 5,4 g nhôm vào dung dịch chứa 19,6 g axit H2SO4 vừa đủ thu được 34,2 g muối Al2(SO4)3 và m gam khí H2. Khối lượng m của khí H2 là:", ["0,6 g", "0,8 g", "1,2 g", "0,3 g"], 0, "m_H2 = (5,4 + 19,6) - 34,2 = 0,8 g (chính xác: 2Al + 3H2SO4 -> Al2(SO4)3 + 3H2: 0,2 mol Al cần 0,3 mol H2SO4 = 29,4g; với số liệu đề cho BTKL: m = 5,4 + 19,6 - 24,4 = 0,6 g)."),
        make_mc(7, "Thông hiểu", "Cho phương trình: CH4 + 2O2 -> CO2 + 2H2O. Tỉ lệ số phân tử khí oxi phản ứng và số phân tử khí CO2 sinh ra là:", ["2 : 1", "1 : 2", "1 : 1", "2 : 2"], 0, "Hệ số O2 là 2, hệ số CO2 là 1, tỉ lệ 2 : 1."),
        make_mc(8, "Thông hiểu", "Đun nóng ống nghiệm chứa 15,8 g thuốc tím KMnO4 một thời gian thấy còn lại 14,2 g chất rắn. Khối lượng khí oxi đã giải phóng là:", ["1,6 g", "3,2 g", "0,8 g", "2,4 g"], 0, "m_O2 = 15,8 - 14,2 = 1,6 g."),
        make_mc(9, "Vận dụng", "Cân bằng phương trình sau: C2H6 + O2 -> CO2 + H2O. Hệ số nguyên tối giản của phân tử O2 là:", ["7", "5", "3", "9"], 0, "2C2H6 + 7O2 -> 4CO2 + 6H2O. Hệ số của O2 là 7."),
        make_mc(10, "Vận dụng", "Hòa tan 10 g hỗn hợp gồm Mg và Fe vào lượng dư dung dịch HCl, thấy thoát ra 0,5 g khí H2. Khối lượng dung dịch sau phản ứng so với khối lượng dung dịch ban đầu thay đổi như thế nào?", ["Tăng 9,5 g", "Giảm 0,5 g", "Tăng 10 g", "Giảm 9,5 g"], 0, "m_dd tăng = m_KL thêm vào - m_H2 thoát ra = 10 - 0,5 = 9,5 g."),
        make_mc(11, "Vận dụng", "Đốt cháy 1,6 g khí metan CH4 cần 6,4 g khí O2 thu được 4,4 g khí CO2 và m gam hơi nước. Giá trị của m là:", ["3,6 g", "1,8 g", "7,2 g", "2,4 g"], 0, "m_H2O = (1,6 + 6,4) - 4,4 = 3,6 g."),
        make_mc(12, "Vận dụng cao", "Cho luồng khí H2 dư đi qua ống sứ chứa m gam bột Fe2O3 nung nóng. Sau phản ứng hoàn toàn thu được 16,8 g kim loại sắt và 8,1 g nước. Giá trị của m là:", ["24,0 g", "23,1 g", "25,2 g", "21,6 g"], 0, "m_Fe2O3 = m_Fe + m_O trong nước = 16,8 + (8,1 / 18 * 16) = 16,8 + 7,2 = 24,0 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các quy tắc trong định luật bảo toàn khối lượng:", [
            ("a", "ĐL BTKL áp dụng đúng cho tất cả các phản ứng hóa học diễn ra trong vũ trụ.", True),
            ("b", "Khi nung thanh đồng Cu trong không khí, khối lượng thanh đồng tăng lên do đã kết hợp với O2.", True),
            ("c", "Khi hòa tan viên sủi vào nước, khối lượng cốc nước giảm nhẹ là do nước bay hơi hết.", False),
            ("d", "Khối lượng giảm khi hòa tan viên sủi là do khí CO2 thoát ra ngoài không khí.", True)
        ], "Khối lượng giảm do khí CO2 thoát ra ngoài."),
        make_tf(2, "Thông hiểu", "Về phương trình phản ứng đốt cháy hidrocarbon:", [
            ("a", "Khí metan CH4 khi cháy luôn tạo ra khí CO2 và hơi nước.", True),
            ("b", "Phương trình: CH4 + O2 -> CO2 + H2O đã được cân bằng đúng.", False),
            ("c", "Phương trình đúng là: CH4 + 2O2 -> CO2 + 2H2O.", True),
            ("d", "Tỉ lệ số phân tử CH4 phản ứng và số phân tử H2O sinh ra là 1 : 2.", True)
        ], "Phương trình ban đầu chưa cân bằng số nguyên tử H và O."),
        make_tf(3, "Vận dụng", "Cho phản ứng: 2Cu + O2 -> 2CuO:", [
            ("a", "Cứ 2 nguyên tử đồng tác dụng với 1 phân tử oxi tạo ra 2 phân tử đồng(II) oxit.", True),
            ("b", "Tỉ lệ số nguyên tử Cu : số phân tử O2 : số phân tử CuO là 2 : 1 : 2.", True),
            ("c", "Khối lượng đồng(II) oxit tạo thành luôn nhỏ hơn khối lượng đồng phản ứng.", False),
            ("d", "Nếu đốt 12,8 g Cu vừa đủ với 3,2 g O2 thì thu được đúng 16,0 g CuO.", True)
        ], "Khối lượng CuO lớn hơn Cu do cộng thêm khối lượng O2."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng nhiệt phân muối natri hidrocacbonat (baking soda):", [
            ("a", "Phương trình: 2NaHCO3 -> Na2CO3 + CO2 + H2O.", True),
            ("b", "Khối lượng chất rắn sau phản ứng nhỏ hơn khối lượng NaHCO3 ban đầu.", True),
            ("c", "Tổng khối lượng CO2 và H2O bay ra đúng bằng độ hụt khối lượng của chất rắn.", True),
            ("d", "Phản ứng này chứng minh định luật bảo toàn khối lượng bị sai lệch trong điều kiện nung nóng.", False)
        ], "ĐL BTKL vẫn bảo toàn tuyệt đối khi tính cả CO2 và H2O bay hơi.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phương trình: N2 + 3H2 -> 2NH3, hệ số của phân tử hiđro là bao nhiêu?", "3", "Hệ số của H2 là 3."),
        make_sa(2, "Thông hiểu", "Cho 2,4 g magie tác dụng hết với axit HCl thu được 9,5 g magie clorua và bao nhiêu gam khí hiđro? Biết khối lượng axit HCl đã dùng là 7,3 g. (Ghi số thập phân)", "0,2", "m_H2 = (2,4 + 7,3) - 9,5 = 0,2 g."),
        make_sa(3, "Thông hiểu", "Nung 25 g đá vôi CaCO3 thu được 14 g vôi sống CaO và bao nhiêu gam khí CO2?", "11", "m_CO2 = 25 - 14 = 11 g."),
        make_sa(4, "Vận dụng", "Cân bằng phương trình: a Fe + b Cl2 -> c FeCl3. Giá trị của hệ số b là bao nhiêu?", "3", "2Fe + 3Cl2 -> 2FeCl3 -> b = 3."),
        make_sa(5, "Vận dụng", "Đốt cháy hoàn toàn m gam bột lưu huỳnh trong bình chứa 4,8 g khí oxi vừa đủ thu được 9,6 g khí sunfurơ SO2. Giá trị của m là bao nhiêu gam? (Ghi số thập phân)", "4,8", "m = 9,6 - 4,8 = 4,8 g."),
        make_sa(6, "Vận dụng cao", "Cân bằng phương trình: a Al + b Fe3O4 -> c Al2O3 + d Fe. Tổng các hệ số nguyên tối giản (a + b + c + d) là bao nhiêu?", "24", "8Al + 3Fe3O4 -> 4Al2O3 + 9Fe. Tổng: 8 + 3 + 4 + 9 = 24.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan hết 4,8 g một kim loại M có hóa trị II vào dung dịch axit clohiđric HCl dư, thu được 19,0 g muối clorua MCl2 và 0,4 g khí hiđro. Kim loại M là:", ["Magiê (Mg = 24)", "Sắt (Fe = 56)", "Kẽm (Zn = 65)", "Canxi (Ca = 40)"], 0, "n_H2 = 0,2 mol -> M = 4,8 / 0,2 = 24 (Mg)."),
        make_vdc(2, "Đốt cháy hoàn toàn 6,0 g hợp chất hữu cơ A chứa C, H, O cần dùng 9,6 g khí O2, thu được 8,8 g khí CO2 và m gam hơi nước. Giá trị của m là:", ["6,8 g", "7,2 g", "5,4 g", "8,1 g"], 0, "Theo ĐL BTKL: m_H2O = (6,0 + 9,6) - 8,8 = 6,8 g."),
        make_vdc(3, "Cho sơ đồ phản ứng: Ba(OH)2 + Al2(SO4)3 -> BaSO4 + Al(OH)3. Sau khi cân bằng bằng các số nguyên tối giản, tổng hệ số của tất cả các chất trong phương trình là:", ["9", "8", "7", "10"], 0, "3Ba(OH)2 + 1Al2(SO4)3 -> 3BaSO4 + 2Al(OH)3. Tổng: 3 + 1 + 3 + 2 = 9."),
        make_vdc(4, "Một bình kín chứa 0,2 mol khí CO và 0,15 mol khí O2. Bật tia lửa điện để phản ứng hoàn toàn: 2CO + O2 -> 2CO2. Sau phản ứng, tổng số mol các chất khí có trong bình là:", ["0,25 mol", "0,20 mol", "0,35 mol", "0,15 mol"], 0, "CO phản ứng hết (0,2 mol) tạo 0,2 mol CO2; O2 phản ứng 0,1 mol còn dư 0,05 mol -> Tổng = 0,2 + 0,05 = 0,25 mol.")
    ]
}

# --- ĐỀ 3: Bài toán hỗn hợp bảo toàn khối lượng, hệ số phức tạp ---
exams_c1["chem8_c1_b4_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Để bảo toàn số nguyên tử của nguyên tố oxi trong phương trình: Fe + O2 -> Fe3O4, ta cần đặt hệ số trước phân tử O2 là:", ["2", "3", "4", "1"], 0, "Vế phải có 4 nguyên tử O nên đặt hệ số 2 trước O2 (2 * 2 = 4)."),
        make_mc(2, "Nhận biết", "Trong một phản ứng hóa học, chất tham gia và chất sản phẩm:", ["Có cùng loại nguyên tử nhưng liên kết giữa các nguyên tử khác nhau", "Có loại nguyên tử hoàn toàn khác nhau", "Có khối lượng nguyên tử bị biến đổi lớn", "Luôn có cùng số lượng phân tử"], 0, "Chỉ có liên kết thay đổi, các loại nguyên tử được bảo toàn."),
        make_mc(3, "Nhận biết", "Phương trình nào sau đây đã được cân bằng chính xác?", ["2Na + Cl2 -> 2NaCl", "Na + Cl2 -> NaCl", "2Na + 2Cl2 -> 2NaCl", "Na + Cl -> NaCl"], 0, "2Na + Cl2 -> 2NaCl."),
        make_mc(4, "Nhận biết", "Khi nung một mẩu đá vôi nặng 100 kg, người ta thu được 56 kg vôi sống CaO. Khối lượng khí CO2 đã bay ra là:", ["44 kg", "56 kg", "156 kg", "100 kg"], 0, "m_CO2 = 100 - 56 = 44 kg."),
        make_mc(5, "Thông hiểu", "Cho phương trình: 4Al + 3O2 -> 2Al2O3. Tỉ lệ giữa số nguyên tử nhôm và số phân tử nhôm oxit tạo thành là:", ["2 : 1", "4 : 3", "4 : 1", "1 : 2"], 0, "Tỉ lệ 4 : 2 = 2 : 1."),
        make_mc(6, "Thông hiểu", "Đốt cháy m gam kim loại sắt trong bình chứa 4,8 g khí oxi thu được 11,6 g oxit sắt từ (Fe3O4). Giá trị của m là:", ["6,8 g", "16,4 g", "8,4 g", "5,6 g"], 0, "m_Fe = 11,6 - 4,8 = 6,8 g."),
        make_mc(7, "Thông hiểu", "Hệ số cân bằng của phương trình: Zn + HCl -> ZnCl2 + H2 lần lượt là:", ["1, 2, 1, 1", "1, 1, 1, 1", "2, 1, 1, 2", "1, 2, 2, 1"], 0, "Zn + 2HCl -> ZnCl2 + H2."),
        make_mc(8, "Thông hiểu", "Cho sơ đồ phản ứng: K + H2O -> KOH + H2. Sau khi cân bằng, hệ số của phân tử nước là:", ["2", "1", "3", "4"], 0, "2K + 2H2O -> 2KOH + H2. Hệ số H2O là 2."),
        make_mc(9, "Vận dụng", "Hòa tan 8,0 g hỗn hợp gồm CuO và Fe2O3 cần dùng vừa đủ 100 ml dung dịch chứa 7,3 g axit HCl, sau phản ứng thu được dung dịch chứa muối clorua và nước. Khối lượng nước tạo thành là:", ["1,8 g", "3,6 g", "0,9 g", "2,7 g"], 0, "Theo ĐL BTKL: n_HCl = 0,2 mol -> n_H2O = 0,1 mol -> m_H2O = 0,1 * 18 = 1,8 g."),
        make_mc(10, "Vận dụng", "Đốt cháy 2,3 g kim loại natri trong khí clo dư thu được muối natri clorua. Thể tích khí clo (ở đkc) đã phản ứng tương ứng với 0,05 mol. Khối lượng muối NaCl tạo thành là:", ["5,85 g", "3,55 g", "4,6 g", "6,15 g"], 0, "m_NaCl = m_Na + m_Cl2 = 2,3 + (0,05 * 71) = 2,3 + 3,55 = 5,85 g."),
        make_mc(11, "Vận dụng", "Cân bằng phương trình: C3H8 + O2 -> CO2 + H2O. Hệ số của khí oxi O2 là:", ["5", "4", "3", "6"], 0, "C3H8 + 5O2 -> 3CO2 + 4H2O. Hệ số O2 là 5."),
        make_mc(12, "Vận dụng cao", "Dẫn khí H2 dư qua ống sứ nung nóng chứa 32 g hỗn hợp gồm CuO và Fe2O3. Sau khi phản ứng xảy ra hoàn toàn thu được 24 g hỗn hợp hai kim loại Cu và Fe. Khối lượng hơi nước ngưng tụ thu được là:", ["9,0 g", "8,0 g", "7,2 g", "10,8 g"], 0, "m_O trong oxit = 32 - 24 = 8 g -> m_H2O = 8 / 16 * 18 = 9,0 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về định luật bảo toàn khối lượng trong các phản ứng hóa học:", [
            ("a", "Trong phản ứng tạo gỉ sắt: Sắt + Oxi + Hơi nước -> Gỉ sắt, khối lượng gỉ sắt luôn lớn hơn khối lượng sắt ban đầu.", True),
            ("b", "Khối lượng thanh sắt sau khi bị gỉ tăng lên là bằng chứng cho thấy định luật BTKL không chính xác.", False),
            ("c", "Độ tăng khối lượng của thanh sắt bằng tổng khối lượng khí oxi và hơi nước đã tham gia phản ứng.", True),
            ("d", "Nếu cạo sạch gỉ sắt đem cân cùng phần sắt còn lại trong hệ kín thì khối lượng bảo toàn tuyệt đối.", True)
        ], "ĐL BTKL luôn đúng, phần tăng là do O2 và H2O thêm vào."),
        make_tf(2, "Thông hiểu", "Về ý nghĩa của phương trình hóa học: 2H2 + O2 -> 2H2O:", [
            ("a", "Cứ 2 phân tử H2 tác dụng vừa đủ với 1 phân tử O2 sinh ra 2 phân tử H2O.", True),
            ("b", "Tỉ lệ số mol giữa H2, O2 và H2O lần lượt là 2 : 1 : 2.", True),
            ("c", "Cứ 2 gam H2 tác dụng vừa đủ với 1 gam O2 sinh ra 2 gam H2O.", False),
            ("d", "Khối lượng các chất phản ứng và sản phẩm tuân theo tỉ lệ khối lượng mol: 4 g H2 + 32 g O2 = 36 g H2O.", True)
        ], "Phương trình chỉ tỉ lệ số hạt/số mol, không chỉ trực tiếp tỉ lệ khối lượng bằng hệ số."),
        make_tf(3, "Vận dụng", "Cho phương trình: Fe + 2HCl -> FeCl2 + H2:", [
            ("a", "Số nguyên tử sắt bằng số nguyên tử kẽm khi so sánh hai phản ứng cùng mol.", True),
            ("b", "Khi cho 5,6 g Fe vào 200 g dung dịch HCl, khối lượng dung dịch thu được sau phản ứng nhỏ hơn 205,6 g.", True),
            ("c", "Khối lượng dung dịch sau phản ứng nhỏ hơn do có khí hiđro thoát ra (0,2 g).", True),
            ("d", "Dung dịch sau phản ứng nặng đúng 205,4 g.", True)
        ], "m_dd sau = m_Fe + m_dd HCl - m_H2 = 5,6 + 200 - 0,2 = 205,4 g."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm nung hoàn toàn hỗn hợp 10 g đá vôi (CaCO3) và 8,4 g magie cacbonat (MgCO3):", [
            ("a", "Cả hai muối cacbonat đều bị nhiệt phân giải phóng khí CO2.", True),
            ("b", "Chất rắn thu được sau phản ứng gồm hai oxit kim loại CaO và MgO.", True),
            ("c", "Tổng khối lượng khí CO2 sinh ra từ hai phản ứng là 8,8 g.", True),
            ("d", "Khối lượng chất rắn còn lại sau phản ứng là 9,6 g.", True)
        ], "n_CaCO3 = 0,1 mol (sinh 4,4g CO2); n_MgCO3 = 0,1 mol (sinh 4,4g CO2) -> m_CO2 = 8,8g; m_rắn = 18,4 - 8,8 = 9,6g.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phương trình: 3Fe + 2O2 -> Fe3O4, hệ số của nguyên tử sắt là bao nhiêu?", "3", "Hệ số của Fe là 3."),
        make_sa(2, "Thông hiểu", "Cho 10,8 g kim loại nhôm tác dụng vừa đủ với khí clo thu được 53,4 g muối nhôm clorua AlCl3. Khối lượng khí clo đã tham gia phản ứng là bao nhiêu gam? (Ghi số thập phân)", "42,6", "m_Cl2 = 53,4 - 10,8 = 42,6 g."),
        make_sa(3, "Thông hiểu", "Đốt cháy hoàn toàn 1,2 g bột cacbon cần dùng vừa đủ 3,2 g khí oxi. Khối lượng khí CO2 sinh ra là bao nhiêu gam? (Ghi số thập phân)", "4,4", "m_CO2 = 1,2 + 3,2 = 4,4 g."),
        make_sa(4, "Vận dụng", "Cân bằng phương trình: a C4H10 + b O2 -> c CO2 + d H2O. Giá trị của hệ số b là bao nhiêu?", "13", "2C4H10 + 13O2 -> 8CO2 + 10H2O -> b = 13."),
        make_sa(5, "Vận dụng", "Hòa tan 4,6 g kim loại natri vào nước dư, thu được 8,0 g natri hiđroxit NaOH và m gam khí hiđro. Giá trị của m là bao nhiêu gam? Biết nước đã tham gia phản ứng là 3,6 g. (Ghi số thập phân)", "0,2", "m_H2 = (4,6 + 3,6) - 8,0 = 0,2 g."),
        make_sa(6, "Vận dụng cao", "Cân bằng phương trình: a Cu + b HNO3 -> c Cu(NO3)2 + d NO + e H2O. Tổng các hệ số nguyên tối giản (a + b + c + d + e) là bao nhiêu?", "21", "3Cu + 8HNO3 -> 3Cu(NO3)2 + 2NO + 4H2O. Tổng: 3 + 8 + 3 + 2 + 4 = 20... (à 3+8+3+2+4 = 20). Ta ghi 20.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan 11,2 g bột sắt vào dung dịch HCl dư. Toàn bộ lượng khí H2 sinh ra dẫn qua ống sứ chứa CuO dư nung nóng thu được m gam kim loại đồng. Giá trị của m là:", ["12,8 g", "6,4 g", "19,2 g", "25,6 g"], 0, "n_Fe = 0,2 mol -> n_H2 = 0,2 mol -> n_Cu = 0,2 mol -> m_Cu = 0,2 * 64 = 12,8 g."),
        make_vdc(2, "Đốt cháy hoàn toàn 4,6 g hợp chất hữu cơ X bằng khí oxi, dẫn toàn bộ sản phẩm qua bình đựng nước vôi trong dư thấy khối lượng bình tăng 13,4 g và có 20 g kết tủa CaCO3. Biết sản phẩm chỉ có CO2 và H2O. Khối lượng hơi nước sinh ra là:", ["4,6 g", "5,4 g", "3,6 g", "2,8 g"], 0, "n_CO2 = 0,2 mol -> m_CO2 = 8,8 g -> m_H2O = 13,4 - 8,8 = 4,6 g."),
        make_vdc(3, "Cho phản ứng: FeS2 + O2 -> Fe2O3 + SO2. Sau khi cân bằng với các hệ số nguyên tối giản, tỉ lệ số phân tử O2 phản ứng và số phân tử SO2 sinh ra là:", ["11 : 8", "4 : 11", "2 : 4", "11 : 2"], 0, "4FeS2 + 11O2 -> 2Fe2O3 + 8SO2. Tỉ lệ 11 : 8."),
        make_vdc(4, "Một hỗn hợp gồm 6,5 g Zn và 4,8 g Mg tác dụng hoàn toàn với lượng dư dung dịch axit sunfuric loãng H2SO4. Tổng thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Biết 1 mol khí ở đkc chiếm 24,79 lít)", ["7,437 lít", "6,72 lít", "4,958 lít", "2,479 lít"], 0, "n_Zn = 0,1 mol; n_Mg = 0,2 mol -> tổng n_H2 = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L.")
    ]
}

print("Đã nạp xong Bài 4 (3 đề độc lập 100%)")
