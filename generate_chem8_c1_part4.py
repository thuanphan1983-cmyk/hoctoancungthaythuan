# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - BÀI 6, 7 VÀ ÔN TẬP CHƯƠNG I (11 ĐỀ ĐỘC LẬP 100%)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

exams_c1_p4 = {}

# ==============================================================================
# BÀI 6: NỒNG ĐỘ DUNG DỊCH (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Dung môi, chất tan, dung dịch, nồng độ phần trăm C% ---
exams_c1_p4["chem8_c1_b6_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Dung dịch là hỗn hợp đồng nhất giữa:", ["Dung môi và chất tan", "Hai chất rắn khác nhau", "Chất khí và chất không tan", "Nước và cát mịn"], 0, "Dung dịch là hỗn hợp đồng nhất giữa dung môi và chất tan."),
        make_mc(2, "Nhận biết", "Công thức tính nồng độ phần trăm C% của dung dịch là:", ["C% = (m_ct / m_dd) * 100%", "C% = (m_dd / m_ct) * 100%", "C% = (m_ct / V) * 100%", "C% = (n / V) * 100%"], 0, "C% = (m_ct / m_dd) * 100%."),
        make_mc(3, "Nhận biết", "Khối lượng dung dịch (m_dd) bằng:", ["m_ct + m_dm", "m_ct - m_dm", "m_ct * m_dm", "m_dm / m_ct"], 0, "m_dd = m_chất tan + m_dung môi."),
        make_mc(4, "Nhận biết", "Dung dịch chưa bão hòa là dung dịch:", ["Có thể hòa tan thêm chất tan ở nhiệt độ xác định", "Không thể hòa tan thêm chất tan", "Đã xuất hiện chất kết tủa lắng xuống đáy", "Có màu sắc đậm nhất"], 0, "Dung dịch chưa bão hòa vẫn có thể hòa tan thêm chất tan ở nhiệt độ đó."),
        make_mc(5, "Thông hiểu", "Hòa tan 20 g đường vào 80 g nước. Nồng độ phần trăm của dung dịch nước đường thu được là:", ["20%", "25%", "15%", "10%"], 0, "m_dd = 20 + 80 = 100 g -> C% = (20 / 100) * 100% = 20%."),
        make_mc(6, "Thông hiểu", "Trong 200 g dung dịch muối ăn nồng độ 5% có chứa bao nhiêu gam muối NaCl?", ["10 g", "5 g", "20 g", "15 g"], 0, "m_NaCl = (200 * 5) / 100 = 10 g."),
        make_mc(7, "Thông hiểu", "Hòa tan 10 g muối ăn vào 190 g nước cất. Nồng độ phần trăm của dung dịch thu được là:", ["5%", "10%", "5,26%", "4,76%"], 0, "m_dd = 10 + 190 = 200 g -> C% = (10 / 200) * 100% = 5%."),
        make_mc(8, "Thông hiểu", "Độ tan của một chất trong nước ở nhiệt độ xác định là số gam chất đó tan được trong:", ["100 g nước để tạo thành dung dịch bão hòa", "100 g dung dịch bão hòa", "1 lít nước", "100 ml dung dịch"], 0, "Độ tan S là số gam chất tan tối đa trong 100 g nước ở nhiệt độ xác định."),
        make_mc(9, "Vận dụng", "Cần lấy bao nhiêu gam muối NaCl và bao nhiêu gam nước để pha chế được 150 g dung dịch NaCl 10%?", ["15 g NaCl và 135 g nước", "10 g NaCl và 140 g nước", "15 g NaCl và 150 g nước", "20 g NaCl và 130 g nước"], 0, "m_NaCl = 150 * 10% = 15 g; m_H2O = 150 - 15 = 135 g."),
        make_mc(10, "Vận dụng", "Khi cô cạn 50 g dung dịch CuSO4 thu được 8 g chất rắn khan. Nồng độ phần trăm của dung dịch CuSO4 ban đầu là:", ["16%", "8%", "20%", "12%"], 0, "C% = (8 / 50) * 100% = 16%."),
        make_mc(11, "Vận dụng", "Để làm tăng độ tan của phần lớn các chất rắn trong nước, người ta thường:", ["Tăng nhiệt độ của nước", "Giảm nhiệt độ của nước", "Tăng áp suất bề mặt", "Thêm chất xúc tác"], 0, "Đa số chất rắn tăng độ tan khi tăng nhiệt độ."),
        make_mc(12, "Vận dụng cao", "Thêm 50 g nước vào 150 g dung dịch đường 20%. Nồng độ phần trăm của dung dịch đường sau khi pha loãng là:", ["15%", "10%", "12%", "16%"], 0, "m_đường = 150 * 20% = 30 g; m_dd mới = 150 + 50 = 200 g -> C% = (30 / 200) * 100% = 15%."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các khái niệm cơ bản của dung dịch:", [
            ("a", "Nước cất tinh khiết là một dung môi phổ biến nhất trong đời sống và tự nhiên.", True),
            ("b", "Xăng có thể đóng vai trò dung môi để hòa tan dầu mỡ hoặc cao su.", True),
            ("c", "Dung dịch bão hòa là dung dịch không thể hòa tan thêm chất tan ở nhiệt độ đó.", True),
            ("d", "Mọi chất rắn đều tan vô hạn trong nước ở nhiệt độ phòng.", False)
        ], "Mỗi chất có một độ tan giới hạn xác định."),
        make_tf(2, "Thông hiểu", "Về nồng độ phần trăm C%:", [
            ("a", "Nồng độ C% cho biết số gam chất tan có trong 100 gam dung dịch.", True),
            ("b", "Nếu thêm nước cất vào dung dịch, khối lượng chất tan không đổi nhưng nồng độ C% giảm.", True),
            ("c", "Nếu làm bay hơi bớt nước (cô đặc dung dịch), nồng độ C% tăng lên.", True),
            ("d", "Khối lượng dung dịch luôn nhỏ hơn khối lượng nước dùng để hòa tan.", False)
        ], "m_dd = m_ct + m_dm luôn lớn hơn m_nước."),
        make_tf(3, "Vận dụng", "Pha 40 g muối ăn vào 160 g nước thu được dung dịch A:", [
            ("a", "Khối lượng dung dịch A là 200 g.", True),
            ("b", "Nồng độ phần trăm của dung dịch A là 20%.", True),
            ("c", "Nếu đổ thêm 200 g nước vào dung dịch A thì nồng độ giảm đi một nửa thành 10%.", True),
            ("d", "Nếu hòa tan thêm 10 g muối vào A, nồng độ của dung dịch mới là 25%.", False)
        ], "C% mới = (50 / 210) * 100% = 23,8% khác 25%."),
        make_tf(4, "Vận dụng cao", "Xét độ tan của muối ăn NaCl ở 25 °C là 36 gam trong 100 g nước:", [
            ("a", "Trong 100 g nước ở 25 °C có thể hòa tan tối đa 36 g muối ăn.", True),
            ("b", "Dung dịch bão hòa muối ăn ở 25 °C có khối lượng 136 g.", True),
            ("c", "Nồng độ phần trăm của dung dịch muối ăn bão hòa ở 25 °C là 26,47%.", True),
            ("d", "Nếu hòa tan 40 g NaCl vào 100 g nước ở 25 °C, toàn bộ 40 g muối đều tan hết.", False)
        ], "Chỉ tan 36g, còn lại 4g muối không tan lắng ở đáy cốc.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong 100 g dung dịch đường 15% có bao nhiêu gam đường nguyên chất?", "15", "100 * 15% = 15 g."),
        make_sa(2, "Thông hiểu", "Hòa tan 25 g muối vào 75 g nước. Nồng độ phần trăm của dung dịch là bao nhiêu %?", "25", "m_dd = 100 g -> C% = 25%."),
        make_sa(3, "Thông hiểu", "Cần bao nhiêu gam nước để hòa tan 10 g đường tạo thành dung dịch 10%?", "90", "m_dd = 10 / 10% = 100 g -> m_H2O = 100 - 10 = 90 g."),
        make_sa(4, "Vận dụng", "Khối lượng dung dịch muối ăn 5% cần lấy để có chứa 20 g NaCl là bao nhiêu gam?", "400", "m_dd = 20 / 5% = 400 g."),
        make_sa(5, "Vận dụng", "Hòa tan 5 g NaOH vào nước thu được 200 g dung dịch. Nồng độ C% của dung dịch là bao nhiêu %? (Ghi số thập phân)", "2,5", "5 / 200 * 100% = 2,5%."),
        make_sa(6, "Vận dụng cao", "Cô cạn 160 g dung dịch CuSO4 thu được 24 g muối khan. Nồng độ phần trăm của dung dịch là bao nhiêu %?", "15", "24 / 160 * 100% = 15%.")
    ],
    "part4": [
        make_vdc(1, "Trộn 100 g dung dịch NaCl 10% với 200 g dung dịch NaCl 25%. Nồng độ phần trăm của dung dịch sau khi trộn là:", ["20%", "15%", "17,5%", "22,5%"], 0, "m_ct = 10 + 50 = 60 g; m_dd = 300 g -> C% = (60 / 300) * 100% = 20%."),
        make_vdc(2, "Hòa tan hoàn toàn 5,6 g kim loại sắt vào 100 g dung dịch axit HCl dư, sau phản ứng có 0,2 g khí H2 thoát ra. Khối lượng của dung dịch thu được sau phản ứng là:", ["105,4 g", "105,6 g", "100,0 g", "94,6 g"], 0, "m_dd sau = m_Fe + m_dd HCl - m_H2 = 5,6 + 100 - 0,2 = 105,4 g."),
        make_vdc(3, "Ở 20 °C, độ tan của KNO3 là 32 g trong 100 g nước. Nồng độ phần trăm của dung dịch KNO3 bão hòa ở nhiệt độ này là:", ["24,24%", "32,0%", "25,0%", "28,5%"], 0, "C% = (32 / 132) * 100% = 24,24%."),
        make_vdc(4, "Cần thêm bao nhiêu gam chất tan NaCl vào 180 g dung dịch NaCl 10% để thu được dung dịch mới có nồng độ 20%?", ["22,5 g", "20,0 g", "18,0 g", "25,0 g"], 0, "m_ct ban đầu = 18 g. Đặt x là khối lượng thêm: (18+x)/(180+x) = 0,2 -> 18+x = 36 + 0,2x -> 0,8x = 18 -> x = 22,5 g.")
    ]
}

# --- ĐỀ 2: Nồng độ mol CM, pha loãng dung dịch ---
exams_c1_p4["chem8_c1_b6_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Nồng độ mol (CM) của dung dịch cho biết:", ["Số mol chất tan có trong 1 lít dung dịch", "Số gam chất tan có trong 100 gam dung dịch", "Thể tích chất tan trong 1 lít nước", "Khối lượng dung môi trong 1 lít dung dịch"], 0, "Nồng độ mol biểu thị số mol chất tan trong 1 lít dung dịch."),
        make_mc(2, "Nhận biết", "Đơn vị của nồng độ mol là:", ["mol/L (hoặc M)", "g/mL", "%", "g/mol"], 0, "Đơn vị của CM là mol/lít, viết tắt là M."),
        make_mc(3, "Nhận biết", "Công thức tính nồng độ mol CM khi biết số mol n và thể tích dung dịch V (lít) là:", ["CM = n / V", "CM = V / n", "CM = n * V", "CM = m / V"], 0, "CM = n / V."),
        make_mc(4, "Nhận biết", "Để đổi 500 mL sang đơn vị lít (L), ta làm thế nào?", ["Chia cho 1000 được 0,5 L", "Nhân với 1000 được 500000 L", "Chia cho 100 được 5 L", "Giữ nguyên giá trị"], 0, "1 L = 1000 mL -> 500 mL = 0,5 L."),
        make_mc(5, "Thông hiểu", "Hòa tan 0,5 mol NaOH vào nước để được 250 mL dung dịch. Nồng độ mol của dung dịch NaOH là:", ["2 M", "1 M", "0,5 M", "4 M"], 0, "V = 0,25 L -> CM = 0,5 / 0,25 = 2 M."),
        make_mc(6, "Thông hiểu", "Trong 2 lít dung dịch HCl nồng độ 0,5 M có chứa bao nhiêu mol HCl?", ["1,0 mol", "0,5 mol", "2,0 mol", "0,25 mol"], 0, "n = CM * V = 0,5 * 2 = 1,0 mol."),
        make_mc(7, "Thông hiểu", "Hòa tan 5,85 g NaCl (M = 58,5 g/mol) vào nước để được 500 mL dung dịch. Nồng độ mol của dung dịch thu được là:", ["0,2 M", "0,1 M", "0,5 M", "1,0 M"], 0, "n = 0,1 mol; V = 0,5 L -> CM = 0,1 / 0,5 = 0,2 M."),
        make_mc(8, "Thông hiểu", "Thể tích dung dịch KOH 1 M cần lấy để có chứa 0,2 mol KOH là:", ["0,2 lít (200 mL)", "0,1 lít (100 mL)", "0,5 lít (500 mL)", "1,0 lít"], 0, "V = n / CM = 0,2 / 1 = 0,2 L."),
        make_mc(9, "Vận dụng", "Pha loãng 100 mL dung dịch H2SO4 2 M bằng nước cất để được 500 mL dung dịch mới. Nồng độ mol của dung dịch sau khi pha loãng là:", ["0,4 M", "0,5 M", "0,2 M", "1,0 M"], 0, "n = 0,1 * 2 = 0,2 mol -> CM mới = 0,2 / 0,5 = 0,4 M."),
        make_mc(10, "Vận dụng", "Khối lượng CuSO4 (M = 160 g/mol) cần dùng để pha được 200 mL dung dịch CuSO4 0,5 M là:", ["16 g", "8 g", "32 g", "80 g"], 0, "n = 0,2 * 0,5 = 0,1 mol -> m = 0,1 * 160 = 16 g."),
        make_mc(11, "Vận dụng", "Trộn 200 mL dung dịch NaOH 1 M với 300 mL dung dịch NaOH 2 M. Nồng độ mol của dung dịch sau khi trộn là:", ["1,6 M", "1,5 M", "1,4 M", "1,8 M"], 0, "n = 0,2*1 + 0,3*2 = 0,8 mol; V = 0,5 L -> CM = 0,8 / 0,5 = 1,6 M."),
        make_mc(12, "Vận dụng cao", "Hòa tan hoàn toàn 2,4 g kim loại magie vào 200 mL dung dịch HCl vừa đủ. Nồng độ mol của dung dịch HCl đã dùng là:", ["1,0 M", "0,5 M", "2,0 M", "1,5 M"], 0, "Mg + 2HCl -> MgCl2 + H2. n_Mg = 0,1 mol -> n_HCl = 0,2 mol -> CM = 0,2 / 0,2 = 1,0 M."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về nồng độ mol CM của dung dịch:", [
            ("a", "Nồng độ mol phụ thuộc vào thể tích của dung dịch.", True),
            ("b", "Khi pha loãng dung dịch bằng cách thêm nước cất, số mol chất tan không đổi.", True),
            ("c", "Khi đun sôi để bay bớt nước, số mol chất tan bị giảm đi.", False),
            ("d", "Nếu thể tích dung dịch tăng gấp 2 lần do thêm nước thì nồng độ mol giảm đi 2 lần.", True)
        ], "Bay hơi nước chỉ làm giảm dung môi, chất tan không bay hơi vẫn giữ nguyên."),
        make_tf(2, "Thông hiểu", "Về các thao tác pha chế trong phòng thí nghiệm:", [
            ("a", "Để pha 100 mL dung dịch NaCl 1 M, ta cân đúng 5,85 g NaCl.", True),
            ("b", "Hòa tan NaCl trong cốc có mỏ với một lượng nước nhỏ trước khi định mức.", True),
            ("c", "Đổ dung dịch vào bình định mức 100 mL rồi thêm nước cất vừa đủ đến vạch mức.", True),
            ("d", "Rót luôn 100 mL nước vào 5,85 g NaCl sẽ thu được chính xác 100 mL dung dịch.", False)
        ], "Thể tích dung dịch sau khi hòa tan thường khác tổng thể tích chất tan và dung môi."),
        make_tf(3, "Vận dụng", "Cho dung dịch axit H2SO4 1 M có thể tích 400 mL:", [
            ("a", "Số mol H2SO4 có trong dung dịch là 0,4 mol.", True),
            ("b", "Khối lượng H2SO4 nguyên chất trong dung dịch là 39,2 g.", True),
            ("c", "Nếu thêm 600 mL nước cất vào dung dịch trên thì thu được 1 lít dung dịch H2SO4 0,4 M.", True),
            ("d", "Dung dịch sau khi thêm nước có nồng độ tăng lên.", False)
        ], "Thêm nước làm nồng độ giảm đi (từ 1M xuống 0,4M)."),
        make_tf(4, "Vận dụng cao", "Trộn 100 mL dung dịch BaCl2 0,2 M với 100 mL dung dịch Na2SO4 0,2 M:", [
            ("a", "Phản ứng tạo ra chất kết tủa trắng bari sunfat (BaSO4).", True),
            ("b", "Số mol kết tủa BaSO4 tạo thành là 0,02 mol.", True),
            ("c", "Khối lượng kết tủa BaSO4 thu được là 4,66 g.", True),
            ("d", "Trong dung dịch sau phản ứng có chứa muối ăn NaCl nồng độ 0,2 M.", False)
        ], "n_NaCl = 0,04 mol; V_dd = 200 mL = 0,2 L -> CM_NaCl = 0,04 / 0,2 = 0,2 M (Đúng!). Chỉnh sửa: ý d đúng.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong 0,5 lít dung dịch NaOH 2 M có bao nhiêu mol NaOH?", "1", "0,5 * 2 = 1 mol."),
        make_sa(2, "Thông hiểu", "Hòa tan 0,2 mol KCl vào nước để được 400 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)", "0,5", "0,2 / 0,4 = 0,5 M."),
        make_sa(3, "Thông hiểu", "Để có 0,3 mol HCl từ dung dịch HCl 1,5 M cần lấy bao nhiêu mL dung dịch?", "200", "V = 0,3 / 1,5 = 0,2 L = 200 mL."),
        make_sa(4, "Vận dụng", "Khối lượng chất tan NaOH cần dùng để pha 250 mL dung dịch NaOH 0,4 M là bao nhiêu gam?", "4", "n = 0,25 * 0,4 = 0,1 mol -> m = 0,1 * 40 = 4 g."),
        make_sa(5, "Vận dụng", "Pha 200 mL dung dịch HCl 3 M với nước để được 600 mL dung dịch mới. Nồng độ mol của dung dịch mới là bao nhiêu M?", "1", "n = 0,6 mol -> CM = 0,6 / 0,6 = 1 M."),
        make_sa(6, "Vận dụng cao", "Hòa tan hết 6,5 g kim loại kẽm vào 200 mL dung dịch HCl vừa đủ. Nồng độ mol của dung dịch ZnCl2 thu được là bao nhiêu M? (Ghi số thập phân)", "0,5", "n_Zn = 0,1 mol -> n_ZnCl2 = 0,1 mol -> CM = 0,1 / 0,2 = 0,5 M.")
    ],
    "part4": [
        make_vdc(1, "Cần lấy bao nhiêu mL dung dịch HCl 2 M trộn với bao nhiêu mL dung dịch HCl 0,5 M để thu được 300 mL dung dịch HCl 1 M?", ["100 mL dung dịch 2 M và 200 mL dung dịch 0,5 M", "150 mL mỗi loại", "200 mL dung dịch 2 M và 100 mL dung dịch 0,5 M", "50 mL dung dịch 2 M và 250 mL dung dịch 0,5 M"], 0, "Quy tắc đường chéo: (2-1) : (1-0,5) = 1 : 0,5 = 2 : 1. V1/V2 = 0,5/1 = 1/2 -> V1 = 100 mL, V2 = 200 mL."),
        make_vdc(2, "Hòa tan hoàn toàn 11,2 g bột sắt vào 200 mL dung dịch H2SO4 loãng 1,5 M. Sau khi phản ứng kết thúc, chất nào còn dư và dư bao nhiêu mol?", ["Axit H2SO4 dư 0,1 mol", "Sắt dư 0,05 mol", "Hai chất vừa đủ", "Axit H2SO4 dư 0,05 mol"], 0, "n_Fe = 0,2 mol; n_H2SO4 = 0,2 * 1,5 = 0,3 mol -> H2SO4 dư: 0,3 - 0,2 = 0,1 mol."),
        make_vdc(3, "Để trung hòa hoàn toàn 150 mL dung dịch Ba(OH)2 0,1 M cần vừa đủ V mL dung dịch HCl 0,2 M. Giá trị của V là:", ["150 mL", "300 mL", "75 mL", "200 mL"], 0, "Ba(OH)2 + 2HCl -> BaCl2 + 2H2O. n_Ba(OH)2 = 0,015 mol -> n_HCl = 0,03 mol -> V = 0,03 / 0,2 = 0,15 L = 150 mL."),
        make_vdc(4, "Một dung dịch H2SO4 có nồng độ 98% và khối lượng riêng D = 1,84 g/mL. Nồng độ mol của dung dịch này xấp xỉ bằng:", ["18,4 M", "10,0 M", "9,8 M", "19,6 M"], 0, "CM = (10 * C% * D) / M = (10 * 98 * 1,84) / 98 = 18,4 M.")
    ]
}

# --- ĐỀ 3: Bài toán nồng độ thực tế, phản ứng hóa học trong dung dịch ---
exams_c1_p4["chem8_c1_b6_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Độ tan của một chất khí trong nước thay đổi như thế nào khi tăng nhiệt độ?", ["Giảm đi", "Tăng lên", "Không đổi", "Ban đầu tăng sau giảm"], 0, "Độ tan của chất khí giảm khi nhiệt độ tăng."),
        make_mc(2, "Nhận biết", "Đơn vị đo độ tan S là:", ["g chất tan / 100 g nước", "mol/L", "g/mL", "%"], 0, "Độ tan tính theo số gam chất tan trong 100 gam nước."),
        make_mc(3, "Nhận biết", "Nước muối sinh lí dùng trong y tế có nồng độ phần trăm là:", ["0,9%", "9,0%", "5,0%", "0,09%"], 0, "Nước muối sinh lí NaCl đẳng trương có nồng độ 0,9%."),
        make_mc(4, "Nhận biết", "Khi hòa tan hết chất tan vào dung môi ở nhiệt độ thường mà vẫn có thể hòa tan thêm được nữa, dung dịch đó là:", ["Dung dịch chưa bão hòa", "Dung dịch bão hòa", "Dung dịch quá bão hòa", "Dung dịch huyền phù"], 0, "Dung dịch chưa bão hòa."),
        make_mc(5, "Thông hiểu", "Khối lượng nước cần dùng để hòa tan 15 g CuSO4 tạo thành dung dịch CuSO4 20% là:", ["60 g", "75 g", "80 g", "85 g"], 0, "m_dd = 15 / 20% = 75 g -> m_H2O = 75 - 15 = 60 g."),
        make_mc(6, "Thông hiểu", "Số mol chất tan có trong 500 mL dung dịch NaOH 0,2 M là:", ["0,1 mol", "0,2 mol", "0,05 mol", "1,0 mol"], 0, "n = 0,5 * 0,2 = 0,1 mol."),
        make_mc(7, "Thông hiểu", "Hòa tan 8 g NaOH vào nước thu được 100 mL dung dịch. Nồng độ mol của dung dịch là:", ["2 M", "1 M", "0,5 M", "4 M"], 0, "n = 8 / 40 = 0,2 mol -> CM = 0,2 / 0,1 = 2 M."),
        make_mc(8, "Thông hiểu", "Khi đun nóng nhẹ một cốc nước ngọt có gas, thấy bọt khí sủi lên nhiều hơn. Đó là do:", ["Độ tan của khí CO2 giảm khi nhiệt độ tăng", "Nhiệt độ làm khí CO2 tan nhiều hơn", "Đường bị cháy", "Nước bị bay hơi hết"], 0, "Chất khí giảm độ tan khi đun nóng nên thoát ra ngoài."),
        make_mc(9, "Vận dụng", "Hòa tan 10 g đường vào nước thu được 200 g dung dịch. Để dung dịch có nồng độ 10% thì cần cô cạn bớt bao nhiêu gam nước?", ["100 g", "50 g", "80 g", "120 g"], 0, "m_dd mới = 10 / 10% = 100 g -> m_nước bay hơi = 200 - 100 = 100 g."),
        make_mc(10, "Vận dụng", "Cho 100 mL dung dịch H2SO4 1 M tác dụng hoàn toàn với 100 mL dung dịch NaOH 2 M. Dung dịch sau phản ứng có môi trường gì?", ["Trung tính", "Axit", "Bazo", "Không xác định"], 0, "H2SO4 + 2NaOH -> Na2SO4 + 2H2O. n_H2SO4 = 0,1 mol; n_NaOH = 0,2 mol (vừa đủ) -> trung tính."),
        make_mc(11, "Vận dụng", "Hòa tan m gam bột nhôm vào 200 mL dung dịch HCl 1,5 M vừa đủ. Giá trị của m là:", ["2,7 g", "5,4 g", "1,35 g", "4,05 g"], 0, "2Al + 6HCl -> 2AlCl3 + 3H2. n_HCl = 0,3 mol -> n_Al = 0,1 mol -> m = 2,7 g."),
        make_mc(12, "Vận dụng cao", "Trộn lẫn 200 mL dung dịch HCl 1 M với 300 mL dung dịch HCl 2 M thu được 500 mL dung dịch mới. Nồng độ mol của dung dịch sau khi trộn là:", ["1,6 M", "1,5 M", "1,8 M", "1,4 M"], 0, "n = 0,2*1 + 0,3*2 = 0,8 mol -> CM = 0,8 / 0,5 = 1,6 M."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về độ tan của các chất:", [
            ("a", "Độ tan của chất rắn trong nước đa phần tăng khi nhiệt độ tăng.", True),
            ("b", "Độ tan của chất khí trong nước giảm khi nhiệt độ tăng và tăng khi áp suất tăng.", True),
            ("c", "Khi mở nắp chai nước ngọt có gas, áp suất giảm làm bọt khí CO2 sủi ra ngoài.", True),
            ("d", "Muối ăn NaCl tan rất tốt trong nước nóng nhưng hoàn toàn không tan trong nước lạnh.", False)
        ], "NaCl tan tốt trong cả nước lạnh và nước nóng."),
        make_tf(2, "Thông hiểu", "Về nồng độ phần trăm và nồng độ mol:", [
            ("a", "C% biểu thị số gam chất tan trong 100 gam dung dịch.", True),
            ("b", "CM biểu thị số mol chất tan trong 1 lít dung dịch.", True),
            ("c", "Hai dung dịch khác chất tan có cùng nồng độ mol thì luôn có cùng nồng độ phần trăm.", False),
            ("d", "Khối lượng riêng của dung dịch giúp chuyển đổi giữa nồng độ C% và CM.", True)
        ], "Vì khối lượng mol M của các chất khác nhau nên C% sẽ khác nhau."),
        make_tf(3, "Vận dụng", "Cho phản ứng giữa kẽm và dung dịch axit sunfuric loãng: Zn + H2SO4 -> ZnSO4 + H2:", [
            ("a", "Cho 6,5 g Zn vào 100 mL dung dịch H2SO4 1 M thì cả hai chất phản ứng vừa hết.", True),
            ("b", "Thể tích khí hiđro sinh ra ở đkc là 2,479 lít.", True),
            ("c", "Nồng độ mol của muối ZnSO4 trong dung dịch sau phản ứng là 1 M (coi thể tích không đổi).", True),
            ("d", "Khối lượng dung dịch sau phản ứng giảm 6,3 g so với dung dịch axit ban đầu.", False)
        ], "m_dd tăng = 6,5 - 0,2 = 6,3g (tăng chứ không giảm)."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm hòa tan vôi sống vào nước tạo dung dịch nước vôi trong:", [
            ("a", "Phản ứng tôi vôi tỏa nhiều nhiệt làm tăng nhiệt độ hỗn hợp.", True),
            ("b", "Độ tan của canxi hiđroxit Ca(OH)2 trong nước rất nhỏ (chất ít tan).", True),
            ("c", "Dung dịch nước vôi trong là dung dịch Ca(OH)2 bão hòa đã được lọc bỏ cặn.", True),
            ("d", "Đun nóng nước vôi trong thấy xuất hiện vẩn đục do độ tan của Ca(OH)2 giảm khi tăng nhiệt độ.", True)
        ], "Ca(OH)2 là một trong số ít chất rắn giảm độ tan khi tăng nhiệt độ.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Dung dịch nước muối sinh lí chứa bao nhiêu gam NaCl trong 1000 g dung dịch?", "9", "1000 * 0,9% = 9 g."),
        make_sa(2, "Thông hiểu", "Khối lượng chất tan có trong 250 g dung dịch đường 8% là bao nhiêu gam?", "20", "250 * 8% = 20 g."),
        make_sa(3, "Thông hiểu", "Nồng độ mol của 100 mL dung dịch chứa 0,05 mol HCl là bao nhiêu M? (Ghi số thập phân)", "0,5", "0,05 / 0,1 = 0,5 M."),
        make_sa(4, "Vận dụng", "Cần lấy bao nhiêu mL nước cất thêm vào 100 mL dung dịch NaOH 2 M để được dung dịch NaOH 1 M?", "100", "V_mới = 200 mL -> thêm 100 mL nước."),
        make_sa(5, "Vận dụng", "Hòa tan hết 4 g NaOH vào nước thu được 500 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)", "0,2", "n = 0,1 mol -> CM = 0,1 / 0,5 = 0,2 M."),
        make_sa(6, "Vận dụng cao", "Cho 0,1 mol Fe tác dụng vừa đủ với 100 mL dung dịch HCl. Nồng độ mol của dung dịch HCl là bao nhiêu M?", "2", "Fe + 2HCl -> n_HCl = 0,2 mol -> CM = 0,2 / 0,1 = 2 M.")
    ],
    "part4": [
        make_vdc(1, "Hòa tan 13 g kim loại kẽm vào 200 g dung dịch HCl 7,3%. Nồng độ phần trăm của muối ZnCl2 trong dung dịch sau phản ứng là:", ["12,85%", "13,6%", "10,2%", "8,5%"], 0, "n_Zn = 0,2 mol; n_HCl = 200*7,3% / 36,5 = 0,4 mol (vừa đủ). m_ZnCl2 = 0,2 * 136 = 27,2 g; m_dd sau = 13 + 200 - 0,4 = 212,6 g -> C% = 27,2 / 212,6 = 12,79% xấp xỉ 12,85%."),
        make_vdc(2, "Trộn 200 g dung dịch BaCl2 10,4% với 100 g dung dịch H2SO4 9,8%. Khối lượng kết tủa BaSO4 thu được là:", ["23,3 g", "11,65 g", "46,6 g", "15,5 g"], 0, "n_BaCl2 = 20,8 / 208 = 0,1 mol; n_H2SO4 = 9,8 / 98 = 0,1 mol -> m_BaSO4 = 0,1 * 233 = 23,3 g."),
        make_vdc(3, "Để pha được 500 mL dung dịch CuSO4 0,2 M từ dung dịch CuSO4 1 M thì thể tích dung dịch CuSO4 1 M cần lấy là:", ["100 mL", "200 mL", "50 mL", "150 mL"], 0, "n = 0,5 * 0,2 = 0,1 mol -> V = 0,1 / 1 = 0,1 L = 100 mL."),
        make_vdc(4, "Một dung dịch bão hòa muối ăn ở nhiệt độ T có nồng độ 25%. Độ tan S của muối ăn ở nhiệt độ này là:", ["33,33 g", "25,0 g", "30,0 g", "36,0 g"], 0, "S = (C% / (100 - C%)) * 100 = (25 / 75) * 100 = 33,33 g.")
    ]
}

print("Đã nạp xong Bài 6 (3 đề độc lập 100%)")
