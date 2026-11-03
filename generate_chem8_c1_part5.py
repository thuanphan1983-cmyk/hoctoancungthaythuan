# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - BÀI 7 VÀ ÔN TẬP CUỐI CHƯƠNG I (8 ĐỀ ĐỘC LẬP 100%)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from generate_chem8_c1 import make_mc, make_tf, make_sa, make_vdc

exams_c1_p5 = {}

# ==============================================================================
# BÀI 7: TỐC ĐỘ PHẢN ỨNG VÀ CHẤT XÚC TÁC (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Khái niệm tốc độ, ảnh hưởng của nồng độ và nhiệt độ ---
exams_c1_p5["chem8_c1_b7_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Tốc độ phản ứng là đại lượng đặc trưng cho:", ["Mức độ nhanh hay chậm của một phản ứng hóa học", "Khối lượng chất tham gia phản ứng", "Thể tích chất khí sinh ra", "Nhiệt độ sôi của chất phản ứng"], 0, "Tốc độ phản ứng đo lường độ nhanh hay chậm của phản ứng."),
        make_mc(2, "Nhận biết", "Khi tăng nồng độ chất phản ứng, tốc độ phản ứng nói chung sẽ:", ["Tăng lên", "Giảm đi", "Không đổi", "Ban đầu tăng sau giảm"], 0, "Tăng nồng độ làm tăng số va chạm hiệu quả giữa các phân tử, làm tăng tốc độ phản ứng."),
        make_mc(3, "Nhận biết", "Khi tăng nhiệt độ, tốc độ của hầu hết các phản ứng hóa học sẽ:", ["Tăng lên", "Giảm đi", "Không thay đổi", "Biến mất hoàn toàn"], 0, "Nhiệt độ tăng làm các phân tử chuyển động nhanh hơn, tăng va chạm hiệu quả."),
        make_mc(4, "Nhận biết", "Thao tác nào sau đây làm tăng tốc độ phản ứng giữa kẽm và dung dịch axit clohiđric?", ["Đun nóng nhẹ dung dịch axit", "Làm lạnh dung dịch axit", "Pha loãng dung dịch axit bằng nhiều nước", "Dùng miếng kẽm kích thước thật to"], 0, "Đun nóng làm tăng nhiệt độ, đẩy nhanh tốc độ phản ứng."),
        make_mc(5, "Thông hiểu", "Tại sao than củi cháy trong khí oxi nguyên chất sáng và mãnh liệt hơn cháy ngoài không khí?", ["Nồng độ khí oxi trong bình oxi nguyên chất cao hơn nhiều so với trong không khí (khoảng 21%)", "Khí oxi nguyên chất nóng hơn", "Khí oxi nguyên chất chứa chất xúc tác", "Than củi tan biến thành lỏng"], 0, "Nồng độ O2 cao hơn làm phản ứng cháy diễn ra nhanh và mãnh liệt hơn."),
        make_mc(6, "Thông hiểu", "Thực phẩm được bảo quản trong tủ lạnh để lâu bị ôi thiu hơn so với để ở nhiệt độ phòng là ứng dụng của yếu tố nào?", ["Giảm nhiệt độ làm giảm tốc độ của các phản ứng hóa sinh phân hủy", "Tăng nồng độ chất bảo quản", "Giảm diện tích tiếp xúc", "Tăng áp suất trong tủ lạnh"], 0, "Hạ nhiệt độ làm chậm tốc độ phản ứng phân hủy thức ăn."),
        make_mc(7, "Thông hiểu", "Khi hòa tan cùng một khối lượng kẽm vào 2 cốc đựng axit HCl có nồng độ lần lượt là 1 M và 2 M ở cùng nhiệt độ, hiện tượng quan sát được là:", ["Cốc chứa axit 2 M sủi bọt khí nhanh và mạnh hơn", "Cốc chứa axit 1 M sủi bọt khí nhanh hơn", "Cả 2 cốc sủi bọt khí với tốc độ như nhau", "Cốc chứa axit 2 M không sủi bọt"], 0, "Nồng độ axit cao hơn thì tốc độ thoát khí H2 nhanh hơn."),
        make_mc(8, "Thông hiểu", "Dùng nồi áp suất để ninh xương giúp xương nhanh mềm hơn là do:", ["Áp suất cao làm tăng nhiệt độ sôi của nước lên trên 100 °C, làm phản ứng hóa sinh diễn ra nhanh hơn", "Nồi áp suất kín ngăn oxi thoát ra", "Nồi áp suất chứa chất xúc tác", "Nồi áp suất làm giảm thể tích nước"], 0, "Nhiệt độ sôi tăng lên khoảng 115 - 120 °C làm tăng tốc độ phản ứng ninh chín."),
        make_mc(9, "Vận dụng", "Tiến hành phản ứng giữa dung dịch Na2S2O3 với dung dịch H2SO4 loãng ở các nhiệt độ khác nhau (20 °C, 30 °C, 40 °C). Thời gian xuất hiện kết tủa lưu huỳnh vẩn đục ngắn nhất ở nhiệt độ nào?", ["40 °C", "20 °C", "30 °C", "Thời gian như nhau ở cả 3 nhiệt độ"], 0, "Ở 40 °C nhiệt độ cao nhất nên tốc độ phản ứng nhanh nhất, thời gian ngắn nhất."),
        make_mc(10, "Vận dụng", "Trong công nghiệp tổng hợp amoniac (N2 + 3H2 -> 2NH3), người ta thực hiện phản ứng ở áp suất cao (khoảng 200 atm). Yếu tố áp suất ảnh hưởng đến tốc độ phản ứng là do:", ["Nén các phân tử khí lại gần nhau, làm tăng nồng độ chất phản ứng thể khí", "Làm giảm nhiệt độ phản ứng", "Biến đổi chất xúc tác", "Làm khí N2 hóa lỏng"], 0, "Tăng áp suất chất khí tương đương với tăng nồng độ."),
        make_mc(11, "Vận dụng", "Để làm sạch các vết bẩn dầu mỡ trên bát đĩa, người ta thường dùng nước rửa chén pha với nước ấm nóng. Yếu tố ảnh hưởng chính ở đây là:", ["Nhiệt độ ấm làm tăng tốc độ phản ứng và hòa tan dầu mỡ", "Nhiệt độ ấm làm giảm bọt xà phòng", "Nước ấm làm biến đổi cấu tạo sứ", "Nước ấm làm giảm lượng nước rửa bát"], 0, "Nhiệt độ cao thúc đẩy quá trình hòa tan và tẩy rửa."),
        make_mc(12, "Vận dụng cao", "Một phản ứng hóa học khi nhiệt độ tăng thêm 10 °C thì tốc độ phản ứng tăng lên 2 lần (hệ số nhiệt độ gamma = 2). Nếu tăng nhiệt độ từ 20 °C lên 50 °C thì tốc độ phản ứng tăng lên bao nhiêu lần?", ["8 lần", "6 lần", "16 lần", "4 lần"], 0, "Delta t = 30 °C -> tăng 2^(30/10) = 2^3 = 8 lần."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các yếu tố ảnh hưởng đến tốc độ phản ứng:", [
            ("a", "Tốc độ phản ứng tỉ lệ thuận với nồng độ của các chất tham gia.", True),
            ("b", "Khi nhiệt độ tăng, tốc độ của hầu hết các phản ứng hóa học đều tăng.", True),
            ("c", "Tăng áp suất có tác dụng làm tăng tốc độ đối với các phản ứng có chất khí tham gia.", True),
            ("d", "Mọi phản ứng hóa học đều diễn ra với tốc độ như nhau ở cùng một nhiệt độ.", False)
        ], "Mỗi phản ứng có bản chất hóa học khác nhau nên tốc độ rất khác nhau."),
        make_tf(2, "Thông hiểu", "Về các ứng dụng thực tế điều khiển tốc độ phản ứng:", [
            ("a", "Thổi không khí vào lò than đang cháy làm tăng nồng độ O2, giúp than cháy mạnh hơn.", True),
            ("b", "Cho thức ăn vào tủ đông để làm đông đá nước, làm dừng hầu hết phản ứng ôi thiu.", True),
            ("c", "Đậy nắp ấm đun nước để giữ nhiệt độ sôi 100 °C giúp đun nhanh sôi hơn.", True),
            ("d", "Bảo quản hạt giống trong kho lạnh ẩm ướt để hạt nhanh nảy mầm trong kho.", False)
        ], "Cần bảo quản hạt giống ở nơi khô mát để ngăn nảy mầm sớm."),
        make_tf(3, "Vận dụng", "Cho thí nghiệm giữa 2 g kẽm hạt với 50 mL dung dịch HCl 1 M ở các điều kiện khác nhau:", [
            ("a", "Thí nghiệm ở 40 °C thoát khí nhanh hơn ở 20 °C.", True),
            ("b", "Thí nghiệm dùng axit HCl 2 M thoát khí nhanh hơn dùng axit HCl 1 M.", True),
            ("c", "Thay 2 g kẽm hạt bằng 2 g kẽm bột thì phản ứng xảy ra chậm hơn.", False),
            ("d", "Lượng khí H2 tối đa thu được ở hai nhiệt độ 20 °C và 40 °C là bằng nhau nếu Zn phản ứng hết.", True)
        ], "Kẽm bột có diện tích tiếp xúc lớn hơn nên phản ứng nhanh hơn."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng phân hủy canxi cacbonat trong lò vôi công nghiệp: CaCO3 -> CaO + CO2:", [
            ("a", "Để phản ứng phân hủy diễn ra nhanh, người ta phải duy trì nhiệt độ lò khoảng 900 - 1000 °C.", True),
            ("b", "Nếu đập nhỏ đá vôi trước khi nung thì tốc độ phân hủy sẽ tăng lên.", True),
            ("c", "Nếu đóng kín miệng lò để khí CO2 không thoát ra thì phản ứng tạo vôi sống sẽ diễn ra nhanh hơn.", False),
            ("d", "Hút bớt khí CO2 ra khỏi lò giúp cân bằng chuyển dịch theo chiều tạo thêm CaO.", True)
        ], "CO2 tích tụ làm cản trở phản ứng thuận chiều phân hủy.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Khi nồng độ chất phản ứng tăng lên thì tốc độ phản ứng tăng hay giảm?", "tăng", "Nồng độ tăng làm tốc độ tăng."),
        make_sa(2, "Thông hiểu", "Cho các yếu tố: nồng độ, nhiệt độ, áp suất, diện tích bề mặt, chất xúc tác. Có bao nhiêu yếu tố ảnh hưởng đến tốc độ phản ứng?", "5", "Có đủ 5 yếu tố ảnh hưởng."),
        make_sa(3, "Thông hiểu", "Khi nhiệt độ tăng thêm 10 °C, tốc độ phản ứng tăng 3 lần. Nếu nhiệt độ tăng thêm 20 °C thì tốc độ phản ứng tăng bao nhiêu lần?", "9", "3^2 = 9 lần."),
        make_sa(4, "Vận dụng", "Học sinh làm thí nghiệm cho thanh kẽm vào 3 cốc axit HCl có nồng độ: 0,5 M; 1 M; 2 M. Cốc nào có tốc độ thoát khí nhanh nhất? (Điền nồng độ: 0,5 hoặc 1 hoặc 2)", "2", "Cốc có nồng độ 2 M thoát khí nhanh nhất."),
        make_sa(5, "Vận dụng", "Trong công nghệ thực phẩm, sấy khô hoa quả làm giảm hàm lượng nước tự do, qua đó làm giảm tốc độ phản ứng hư hỏng của vi sinh vật. Đây là yếu tố thay đổi nồng độ chất tan hay diện tích bề mặt? (Điền: nồng độ)", "nồng độ", "Giảm hàm lượng nước là thay đổi nồng độ dung môi/chất phản ứng."),
        make_sa(6, "Vận dụng cao", "Một phản ứng kết thúc sau 60 giây ở 30 °C. Biết cứ tăng 10 °C tốc độ phản ứng tăng 2 lần. Ở 50 °C phản ứng sẽ kết thúc sau bao nhiêu giây? (Ghi số thập phân)", "15", "Tăng 20 °C -> tốc độ tăng 4 lần -> thời gian = 60 / 4 = 15 giây.")
    ],
    "part4": [
        make_vdc(1, "Biện pháp nào sau đây KHÔNG LÀM TĂNG tốc độ của phản ứng giữa đá vôi và dung dịch axit clohiđric?", ["Thêm nước cất vào dung dịch axit", "Nghiền nhỏ đá vôi thành bột mịn", "Đun nóng dung dịch axit lên 50 °C", "Dùng dung dịch axit có nồng độ cao hơn"], 0, "Thêm nước cất làm loãng axit (giảm nồng độ), làm giảm tốc độ phản ứng."),
        make_vdc(2, "Khi bảo quản thịt tươi sống, phương pháp nào sau đây dựa trên nguyên tắc làm giảm tốc độ phản ứng phân hủy vi sinh vật bằng cách hạ nhiệt độ?", ["Bảo quản trong ngăn đá tủ lạnh ở -18 °C", "Ướp muối thật mặn", "Hun khói thịt", "Ngâm thịt vào giấm ăn"], 0, "Ngăn đá tủ lạnh hạ nhiệt độ cực thấp làm giảm tốc độ phản ứng."),
        make_vdc(3, "Trong phản ứng tổng hợp amoniac N2 + 3H2 -> 2NH3, người ta dùng bột sắt (Fe) làm chất xúc tác. Vai trò của sắt là:", ["Làm tăng tốc độ phản ứng đạt đến trạng thái cân bằng nhanh hơn mà không bị tiêu hao", "Làm tăng khối lượng amoniac sinh ra vượt mức lí thuyết", "Làm phản ứng không tỏa nhiệt nữa", "Thay thế cho khí nitơ"], 0, "Chất xúc tác chỉ làm tăng tốc độ phản ứng mà không bị tiêu hao."),
        make_vdc(4, "Ở 25 °C, một phản ứng hóa học xảy ra với tốc độ v0. Khi tăng nhiệt độ lên 65 °C, tốc độ phản ứng tăng lên 81 lần. Hệ số nhiệt độ gamma của phản ứng này là:", ["3", "2", "4", "5"], 0, "Delta t = 40 °C -> gamma^(40/10) = gamma^4 = 81 -> gamma = 3.")
    ]
}

# --- ĐỀ 2: Diện tích bề mặt tiếp xúc và chất xúc tác ---
exams_c1_p5["chem8_c1_b7_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Chất xúc tác là chất:", ["Làm tăng tốc độ phản ứng và được hoàn nguyên khối lượng, tính chất sau phản ứng", "Bị biến đổi hoàn toàn thành sản phẩm mới", "Làm giảm tốc độ của phản ứng hóa học", "Có mặt để hòa tan các chất phản ứng"], 0, "Chất xúc tác đẩy nhanh phản ứng và không bị biến đổi sau phản ứng."),
        make_mc(2, "Nhận biết", "Khi tăng diện tích bề mặt tiếp xúc của chất rắn phản ứng, tốc độ phản ứng sẽ:", ["Tăng lên", "Giảm đi", "Không đổi", "Bằng không"], 0, "Diện tích tiếp xúc càng lớn thì số va chạm giữa các chất phản ứng càng nhiều, tốc độ phản ứng càng tăng."),
        make_mc(3, "Nhận biết", "Chất xúc tác sinh học có trong cơ thể sinh vật sống được gọi là:", ["Enzym (men)", "Vitamin", "Hormon", "Protein dự trữ"], 0, "Enzym là các chất xúc tác sinh học đặc hiệu trong cơ thể."),
        make_mc(4, "Nhận biết", "Hành động nào sau đây làm tăng diện tích bề mặt tiếp xúc của chất rắn?", ["Nghiền nhỏ hoặc tán thành bột mịn", "Đúc thành một khối tròn đặc", "Nhúng vào dầu chống ẩm", "Đựng trong hộp kín"], 0, "Nghiền nhỏ làm tăng diện tích tiếp xúc."),
        make_mc(5, "Thông hiểu", "Tại sao than tổ ong thường được tạo nhiều lỗ rỗng xuyên suốt thân viên than?", ["Để tăng diện tích tiếp xúc giữa than với không khí và hút dưỡng khí giúp than cháy đều và mạnh", "Để làm viên than nhẹ hơn dễ vận chuyển", "Để tiết kiệm lượng than sản xuất", "Để dễ cầm tay khi gắp than"], 0, "Các lỗ rỗng tăng lưu thông không khí và tăng diện tích tiếp xúc với oxi."),
        make_mc(6, "Thông hiểu", "Khi cho một mẩu MnO2 vào dung dịch hiđro peoxit (H2O2 - nước oxy già), thấy bọt khí O2 sủi lên mãnh liệt. Vai trò của MnO2 là:", ["Chất xúc tác thúc đẩy sự phân hủy của H2O2", "Chất phản ứng bị tiêu hao hoàn toàn", "Chất ức chế làm chậm phản ứng", "Dung môi hòa tan khí oxi"], 0, "MnO2 là chất xúc tác cho phản ứng: 2H2O2 -> 2H2O + O2."),
        make_mc(7, "Thông hiểu", "Hòa tan cùng một lượng viên sủi vitamin C vào 2 cốc nước ở cùng nhiệt độ: cốc 1 thả nguyên viên sủi, cốc 2 nghiền nát thành bột rồi đổ vào. Hiện tượng quan sát được là:", ["Cốc 2 tan nhanh và sủi bọt mạnh hơn cốc 1", "Cốc 1 tan nhanh hơn cốc 2", "Hai cốc tan với thời gian hoàn toàn bằng nhau", "Cốc 2 không sủi bọt"], 0, "Bột sủi có diện tích tiếp xúc lớn hơn nên phản ứng với nước nhanh hơn."),
        make_mc(8, "Thông hiểu", "Chẻ nhỏ củi trước khi cho vào bếp đun nấu là ứng dụng của yếu tố nào ảnh hưởng đến tốc độ phản ứng?", ["Tăng diện tích bề mặt tiếp xúc", "Tăng nồng độ chất phản ứng", "Thêm chất xúc tác", "Tăng áp suất"], 0, "Chẻ nhỏ củi làm tăng diện tích tiếp xúc của củi với oxi."),
        make_mc(9, "Vận dụng", "Men nở (nấm men bánh mì) dùng khi làm bánh mì có vai trò:", ["Xúc tác quá trình lên men phân giải đường sinh khí CO2 làm bột bánh xốp nở", "Làm vỏ bánh ngọt hơn", "Tẩy trắng bột mì", "Làm bánh đông đặc thành khối cứng"], 0, "Nấm men tiết enzym xúc tác quá trình lên men sinh CO2 tạo độ xốp."),
        make_mc(10, "Vận dụng", "Thực hiện phản ứng: CaCO3 + 2HCl -> CaCl2 + CO2 + H2O. Trong 4 trường hợp sau, trường hợp nào phản ứng diễn ra với tốc độ nhanh nhất?", ["Bột đá vôi mịn + dung dịch HCl 2 M ở 40 °C", "Mẩu đá vôi to + dung dịch HCl 2 M ở 40 °C", "Bột đá vôi mịn + dung dịch HCl 1 M ở 25 °C", "Mẩu đá vôi to + dung dịch HCl 1 M ở 25 °C"], 0, "Kết hợp cả 3 yếu tố: dạng bột (diện tích lớn), nồng độ 2 M cao và nhiệt độ 40 °C cao."),
        make_mc(11, "Vận dụng", "Để làm giảm tốc độ gỉ sét của vỏ tàu biển bằng thép, người ta gắn các tấm kẽm (Zn) vào vỏ tàu hoặc sơn phủ lớp sơn chống rỉ. Lớp sơn chống rỉ có vai trò:", ["Ngăn cách bề mặt sắt tiếp xúc với oxi và nước ẩm trong không khí/nước biển", "Đóng vai trò chất xúc tác phân hủy gỉ", "Tăng nhiệt độ của kim loại", "Hòa tan các muối biển"], 0, "Lớp sơn cách li kim loại với môi trường ăn mòn."),
        make_mc(12, "Vận dụng cao", "Hai thí nghiệm phân hủy dung dịch H2O2 cùng nồng độ và thể tích: Thí nghiệm 1 không có xúc tác mất 20 phút mới phân hủy hết. Thí nghiệm 2 thêm 0,1 g bột MnO2 chỉ mất 15 giây. Sau thí nghiệm 2, lọc lấy chất rắn MnO2, sấy khô và cân lại thấy khối lượng của MnO2 là:", ["Đúng 0,1 g", "0,05 g", "0,0 g (tan hết)", "0,2 g"], 0, "Chất xúc tác không bị tiêu hao sau phản ứng nên khối lượng vẫn giữ nguyên 0,1 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về diện tích bề mặt tiếp xúc và tốc độ phản ứng:", [
            ("a", "Diện tích bề mặt tiếp xúc chỉ có ý nghĩa đối với các phản ứng có chất rắn tham gia.", True),
            ("b", "Nghiền chất rắn thành bột mịn làm tăng tổng diện tích bề mặt tiếp xúc lên nhiều lần.", True),
            ("c", "Chất rắn ở dạng khối đặc tiếp xúc tốt hơn chất rắn ở dạng bột tơi xốp.", False),
            ("d", "Bụi than và bụi bột mì lơ lửng trong không khí có thể gây ra các vụ nổ bụi nguy hiểm do diện tích tiếp xúc cực lớn.", True)
        ], "Khối đặc có diện tích tiếp xúc nhỏ hơn dạng bột."),
        make_tf(2, "Thông hiểu", "Về chất xúc tác và enzym trong đời sống:", [
            ("a", "Chất xúc tác làm tăng tốc độ phản ứng nhưng không tham gia vào thành phần sản phẩm cuối cùng.", True),
            ("b", "Mỗi loại enzym sinh học thường chỉ xúc tác cho một phản ứng hoặc một nhóm phản ứng nhất định.", True),
            ("c", "Chất xúc tác bị tiêu hao dần theo thời gian và biến thành chất mới sau phản ứng.", False),
            ("d", "Trong cơ thể người, men amilaza trong nước bọt xúc tác cho phản ứng thủy phân tinh bột thành đường.", True)
        ], "Chất xúc tác được hoàn nguyên nguyên vẹn về lượng và chất."),
        make_tf(3, "Vận dụng", "Về các kinh nghiệm dân gian trong ẩm thực và đời sống:", [
            ("a", "Hầm thịt bò với quả đu đủ xanh giúp thịt nhanh mềm vì trong nhựa đu đủ có chứa enzym papain phân giải protein.", True),
            ("b", "Đập dập củ sả, ớt, tỏi trước khi ướp thịt giúp các tinh dầu và chất ngấm nhanh hơn nhờ tăng diện tích tiếp xúc.", True),
            ("c", "Muối dưa cà muốn nhanh chua thì cho thêm một ít nước dưa cũ đóng vai trò cung cấp vi khuẩn lên men (tương tự xúc tác).", True),
            ("d", "Để đống mùn cưa to ướt trong góc nhà sẽ tự bốc cháy ngay tức khắc vì diện tích tiếp xúc rất lớn.", False)
        ], "Mùn cưa ướt không đủ điều kiện bốc cháy tức thì."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng phân hủy khí N2O trên bề mặt chất xúc tác platin (Pt):", [
            ("a", "Chất xúc tác Pt tạo ra con đường phản ứng mới có năng lượng hoạt hóa thấp hơn.", True),
            ("b", "Tốc độ phân hủy N2O tăng lên hàng triệu lần khi có mặt Pt nung nóng.", True),
            ("c", "Lượng platin sau phản ứng bị hao hụt 50% khối lượng.", False),
            ("d", "Bộ lọc khí thải xe máy, ô tô dùng chất xúc tác kim loại quý (Pt, Pd, Rh) để xử lý khí độc hại CO, NOx thành CO2, N2 vô hại.", True)
        ], "Xúc tác Pt không hề bị hao hụt khối lượng.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Chất làm tăng tốc độ phản ứng mà không bị tiêu hao sau phản ứng gọi là chất gì?", "chất xúc tác", "Chất xúc tác."),
        make_sa(2, "Thông hiểu", "Cho hai mẫu kẽm cùng khối lượng 5 g: mẫu 1 dạng lá mỏng, mẫu 2 dạng khối cầu đặc. Mẫu nào phản ứng với axit HCl nhanh hơn? (Điền: mẫu 1 hoặc mẫu 2)", "mẫu 1", "Mẫu 1 dạng lá mỏng có diện tích bề mặt lớn hơn."),
        make_sa(3, "Thông hiểu", "Khối lượng của 0,5 g chất xúc tác MnO2 sau khi phản ứng kết thúc còn lại bao nhiêu gam? (Ghi số thập phân)", "0,5", "Chất xúc tác giữ nguyên khối lượng 0,5 g."),
        make_sa(4, "Vận dụng", "Trong công nghiệp sản xuất axit sunfuric, người ta dùng oxit vanadi (V2O5) làm gì trong phản ứng oxi hóa SO2 thành SO3? (Điền: chất xúc tác)", "chất xúc tác", "V2O5 đóng vai trò chất xúc tác."),
        make_sa(5, "Vận dụng", "Để than nhanh bén lửa và cháy đượm, người ta thường chẻ nhỏ củi mồi rồi xếp so le tạo khe hở. Thao tác này tác động đến bao nhiêu yếu tố chính (diện tích tiếp xúc, nồng độ oxi)?", "2", "Tác động đến 2 yếu tố: diện tích tiếp xúc và nồng độ lưu thông oxi."),
        make_sa(6, "Vận dụng cao", "Trong dạ dày người, axit clohiđric HCl cùng men gì xúc tác phân giải protein thịt cá? (Điền tên men: pepsin)", "pepsin", "Enzym pepsin.")
    ],
    "part4": [
        make_vdc(1, "Một học sinh làm 4 thí nghiệm thoát khí CO2 từ phản ứng giữa canxi cacbonat và axit clohiđric. Cặp thí nghiệm nào sau đây chứng minh rõ ràng nhất ảnh hưởng của DIỆN TÍCH BỀ MẶT TIẾP XÚC đến tốc độ phản ứng?", ["10 g đá vôi hạt to + 100 mL HCl 1 M và 10 g đá vôi bột mịn + 100 mL HCl 1 M ở cùng nhiệt độ", "10 g đá vôi bột mịn + 100 mL HCl 1 M ở 25 °C và 10 g đá vôi bột mịn + 100 mL HCl 1 M ở 50 °C", "10 g đá vôi hạt to + 100 mL HCl 1 M và 10 g đá vôi hạt to + 100 mL HCl 2 M ở 25 °C", "10 g đá vôi bột mịn + 100 mL HCl 1 M và 5 g đá vôi hạt to + 50 mL HCl 0,5 M"], 0, "Cần giữ nguyên nồng độ HCl, thể tích và nhiệt độ, chỉ thay đổi kích thước đá vôi (hạt to vs bột mịn)."),
        make_vdc(2, "Tại các mỏ than, hầm chứa thóc ngô khô hay xưởng cưa, biển cảnh báo cấm lửa tuyệt đối được treo nghiêm ngặt. Nguy cơ nổ bụi tại các nơi này rất cao là do:", ["Các hạt bụi mịn có diện tích bề mặt tiếp xúc với oxi không khí vô cùng lớn, khi gặp mồi lửa phản ứng cháy xảy ra tức thì tỏa nhiệt cực lớn gây nổ", "Bụi than tự bốc cháy ở -20 °C", "Bụi ngô chứa chất phóng xạ", "Hầm chứa không có khí oxi"], 0, "Nổ bụi là hiện tượng cháy cực nhanh do diện tích tiếp xúc khổng lồ của các hạt bụi mịn."),
        make_vdc(3, "Hiện tượng nào sau đây thể hiện tác dụng làm CHẬM tốc độ phản ứng (sử dụng chất ức chế)?", ["Thêm một lượng nhỏ chất chống oxi hóa BHT vào dầu ăn để ngăn dầu bị ôi khét", "Thêm men rượu vào cơm nếp", "Thêm MnO2 vào H2O2", "Thêm bột sắt vào hỗn hợp N2 và H2"], 0, "Chất chống oxi hóa đóng vai trò chất ức chế làm chậm phản ứng hư hỏng."),
        make_vdc(4, "Cho phản ứng phân hủy H2O2 có xúc tác MnO2. Nếu dùng 0,2 g bột MnO2 mịn so với 0,2 g viên MnO2 ép chặt thì:", ["Dùng bột MnO2 mịn phản ứng diễn ra nhanh hơn do diện tích bề mặt chất xúc tác lớn hơn", "Dùng viên MnO2 ép chặt phản ứng nhanh hơn", "Tốc độ như nhau vì cùng khối lượng 0,2 g", "Bột MnO2 làm ngừng phản ứng"], 0, "Chất xúc tác dạng bột mịn có diện tích bề mặt lớn hơn, tiếp xúc tốt hơn nên xúc tác hiệu quả hơn.")
    ]
}

# --- ĐỀ 3: Tổng hợp các yếu tố, đồ thị tốc độ, bài toán thực tiễn ---
exams_c1_p5["chem8_c1_b7_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Để xác định tốc độ của phản ứng sinh ra chất khí, người ta thường đo:", ["Thể tích chất khí thoát ra theo thời gian", "Khối lượng của bình sau 1 năm", "Độ dài của ống nghiệm", "Màu sắc của ngọn lửa đèn cồn"], 0, "Đo thể tích khí sinh ra theo từng khoảng thời gian xác định."),
        make_mc(2, "Nhận biết", "Yếu tố nào sau đây KHÔNG ảnh hưởng đến tốc độ phản ứng hóa học?", ["Khối lượng của chất xúc tác tăng gấp 10 lần", "Thể tích bình chứa chất lỏng không tham gia phản ứng", "Nồng độ chất phản ứng", "Nhiệt độ môi trường"], 1, "Thể tích khoảng không của bình không ảnh hưởng trực tiếp đến tốc độ phản ứng trong dung dịch."),
        make_mc(3, "Nhận biết", "Khi quạt gió vào bếp than đang cháy, ta đã tác động đến yếu tố nào?", ["Tăng nồng độ khí oxi tiếp xúc với than", "Giảm nhiệt độ của than", "Thêm chất xúc tác", "Làm than biến thành bột"], 0, "Quạt gió cung cấp liên tục O2 mới làm tăng nồng độ oxi."),
        make_mc(4, "Nhận biết", "Trong cơ thể người, chất xúc tác enzym hoạt động tối ưu ở nhiệt độ khoảng:", ["37 °C (thân nhiệt)", "100 °C", "0 °C", "60 °C"], 0, "Enzym trong cơ thể người hoạt động tốt nhất quanh thân nhiệt 37 °C."),
        make_mc(5, "Thông hiểu", "Khi cho cùng một khối lượng magie vào cốc 1 đựng HCl 1 M và cốc 2 đựng HCl 0,5 M, tốc độ bọt khí thoát ra ở cốc 1 nhanh hơn cốc 2 là do:", ["Ảnh hưởng của nồng độ chất phản ứng", "Ảnh hưởng của nhiệt độ", "Ảnh hưởng của diện tích tiếp xúc", "Ảnh hưởng của chất xúc tác"], 0, "Nồng độ HCl ở cốc 1 (1 M) cao hơn cốc 2 (0,5 M)."),
        make_mc(6, "Thông hiểu", "Cho thanh kim loại sắt nhúng vào axit HCl loãng nguội thì bọt khí thoát ra từ từ; khi đun nóng cốc thì bọt khí thoát ra mãnh liệt. Hiện tượng này chứng minh:", ["Tốc độ phản ứng tăng khi tăng nhiệt độ", "Tốc độ phản ứng giảm khi tăng nhiệt độ", "Sắt tan chảy ở nhiệt độ thấp", "Axit bị phân hủy thành nước"], 0, "Tăng nhiệt độ thúc đẩy tốc độ phản ứng."),
        make_mc(7, "Thông hiểu", "Khi muối dưa cải, người ta thường nén chặt dưa dưới một tấm vỉ và đè đá nặng lên trên. Thao tác này có tác dụng chính là:", ["Làm dưa ngập hoàn toàn trong nước muối, hạn chế tiếp xúc với oxi không khí để vi khuẩn lactic lên men kị khí tốt và tránh mốc váng", "Làm dưa ngọt hơn", "Tăng nhiệt độ của vại dưa", "Làm tan hết muối ăn"], 0, "Nén dưa kị khí giúp vi khuẩn lactic phát triển, ngăn vi khuẩn hiếu khí gây thối hỏng."),
        make_mc(8, "Thông hiểu", "Nghiền nát hạt đậu tương trước khi nấu sữa đậu nành giúp sữa đặc sánh và thơm ngon hơn là do:", ["Tăng diện tích bề mặt tiếp xúc giúp các chất béo và protein tan nhanh vào nước", "Làm giảm nhiệt độ sôi của nước", "Thêm enzym vào sữa", "Làm protein biến tính thành đường"], 0, "Nghiền nhỏ tăng diện tích tiếp xúc giúp chiết xuất kiệt dinh dưỡng."),
        make_mc(9, "Vận dụng", "Trong công nghiệp sản xuất phân đạm urê từ khí amoniac và CO2, người ta thực hiện ở nhiệt độ 180 - 200 °C và áp suất khoảng 200 atm. Việc duy trì áp suất cực cao nhằm mục đích gì?", ["Tăng nồng độ các chất khí phản ứng giúp phản ứng xảy ra nhanh chóng và chuyển dịch cân bằng tạo nhiều urê hơn", "Làm giảm chi phí nhiên liệu", "Làm loãng chất khí", "Hút ẩm cho urê"], 0, "Tăng áp suất làm tăng mật độ hạt khí, tăng tốc độ phản ứng."),
        make_mc(10, "Vận dụng", "Một miếng kim loại nhôm để ngoài không khí tự hình thành lớp màng oxit Al2O3 mỏng, mịn và rất bền vững bao bọc bên ngoài. Lớp màng này có tác dụng gì?", ["Ngăn cản nhôm tiếp xúc với oxi và hơi ẩm, làm dừng hoàn toàn sự ăn mòn phá hủy nhôm bên trong", "Làm nhôm dẫn điện tốt hơn", "Làm tăng khối lượng nhôm lên gấp 10 lần", "Làm nhôm nóng chảy"], 0, "Màng oxit trơ bảo vệ nhôm khỏi sự ăn mòn tiếp diễn."),
        make_mc(11, "Vận dụng", "Đồ thị biểu diễn thể tích khí hiđro thoát ra theo thời gian khi cho kẽm vào axit HCl có dạng đường cong dốc đứng lúc đầu rồi thoai thoải dần và nằm ngang. Nguyên nhân đường cong thoai thoải dần là do:", ["Nồng độ axit HCl giảm dần trong quá trình phản ứng nên tốc độ phản ứng giảm dần", "Nhiệt độ của cốc bị giảm xuống âm độ", "Kẽm bị trơ hóa biến thành vàng", "Khí hiđro ngưng tụ thành chất lỏng"], 0, "Nồng độ chất phản ứng tiêu hao dần làm tốc độ chậm lại."),
        make_mc(12, "Vận dụng cao", "Tiến hành 4 thí nghiệm hòa tan bột đá vôi bằng axit HCl với các điều kiện: (1) 20 °C, HCl 1 M; (2) 20 °C, HCl 2 M; (3) 40 °C, HCl 1 M; (4) 40 °C, HCl 2 M. Thứ tự tốc độ phản ứng tăng dần từ chậm nhất đến nhanh nhất là:", ["(1) < (3) < (2) < (4) hoặc (1) < (2) < (3) < (4)", "(4) < (3) < (2) < (1)", "(1) < (4) < (2) < (3)", "(2) < (1) < (4) < (3)"], 0, "Thí nghiệm (1) thấp nhất (nhiệt độ thấp, nồng độ thấp); thí nghiệm (4) cao nhất (nhiệt độ cao, nồng độ cao)."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các phương pháp thực nghiệm đo tốc độ phản ứng:", [
            ("a", "Có thể đo tốc độ phản ứng bằng cách đo độ giảm khối lượng của bình hở có khí thoát ra theo thời gian.", True),
            ("b", "Có thể đo tốc độ phản ứng bằng cách đo thời gian cần thiết để xuất hiện lượng kết tủa làm mờ một dấu chữ thập dưới đáy cốc.", True),
            ("c", "Tốc độ phản ứng hóa học thường không đổi từ lúc bắt đầu cho đến khi kết thúc.", False),
            ("d", "Tốc độ phản ứng thường nhanh nhất ở giai đoạn đầu khi nồng độ chất phản ứng lớn nhất.", True)
        ], "Tốc độ giảm dần theo thời gian do nồng độ các chất phản ứng giảm dần."),
        make_tf(2, "Thông hiểu", "Về an toàn hóa chất và tốc độ phản ứng:", [
            ("a", "Phản ứng cháy nổ của bình gas xảy ra với tốc độ tức thời giải phóng lượng nhiệt và áp suất khổng lồ.", True),
            ("b", "Sự gỉ sét của đinh sắt ngoài trời là phản ứng oxi hóa chậm diễn ra trong nhiều tháng hoặc nhiều năm.", True),
            ("c", "Để làm chậm sự ôi thiu của dầu thực vật, người ta đóng chai kín và để ở nơi râm mát, tránh ánh nắng mặt trời.", True),
            ("d", "Tất cả các phản ứng có chất xúc tác đều giải phóng nhiệt lượng lớn gây nổ.", False)
        ], "Chất xúc tác chỉ tăng tốc độ, không làm thay đổi nhiệt phản ứng."),
        make_tf(3, "Vận dụng", "Xét phản ứng nhiệt phân muối KClO3: 2KClO3 -> 2KCl + 3O2:", [
            ("a", "Nếu không có xúc tác MnO2, muối KClO3 cần nung ở nhiệt độ rất cao (khoảng 400 - 500 °C) mới phân hủy chậm chạp.", True),
            ("b", "Khi trộn thêm bột MnO2, phản ứng phân hủy xảy ra mãnh liệt ngay ở nhiệt độ khoảng 200 °C.", True),
            ("c", "MnO2 trong phản ứng này đóng vai trò chất phản ứng cung cấp thêm oxi.", False),
            ("d", "Bột MnO2 sau phản ứng có thể tách ra bằng cách hòa tan hỗn hợp vào nước rồi lọc lấy chất rắn không tan.", True)
        ], "Oxi sinh ra hoàn toàn từ KClO3, MnO2 là chất xúc tác không đổi."),
        make_tf(4, "Vận dụng cao", "Về sự biến đổi tốc độ phản ứng sinh học trong đời sống:", [
            ("a", "Khi sốt cao trên 40 °C, các enzym trong cơ thể người có nguy cơ bị biến tính và mất hoạt tính xúc tác.", True),
            ("b", "Nhiệt độ quá thấp (0 °C) làm enzym ngừng hoạt động tạm thời nhưng không phá hủy cấu trúc của đa số enzym.", True),
            ("c", "Muối chua dưa cải thành công là do sự phát triển chiếm ưu thế của vi khuẩn sinh axit lactic ức chế các vi khuẩn gây thối.", True),
            ("d", "Rau quả để lâu trong môi trường chân không sẽ chín nhanh hơn để ngoài không khí.", False)
        ], "Hút chân không loại bỏ O2 làm chậm quá trình chín và hư hỏng của rau quả.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Phản ứng gỉ sắt là phản ứng xảy ra nhanh hay chậm?", "chậm", "Gỉ sắt là phản ứng oxi hóa chậm."),
        make_sa(2, "Thông hiểu", "Phản ứng cháy nổ của thuốc pháo xảy ra nhanh hay chậm?", "nhanh", "Cháy nổ thuốc pháo xảy ra cực nhanh."),
        make_sa(3, "Thông hiểu", "Để thúc đẩy quá trình lên men rượu diễn ra thuận lợi, người ta cần bổ sung chất xúc tác sinh học gì vào tinh bột chín? (Điền: men rượu)", "men rượu", "Men rượu (chứa các enzym nấm men)."),
        make_sa(4, "Vận dụng", "Khi cho 0,1 mol Zn tác dụng với dung dịch HCl dư. Thể tích khí H2 sinh ra tối đa ở đkc là bao nhiêu lít? (Ghi số thập phân)", "2,479", "n_H2 = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."),
        make_sa(5, "Vận dụng", "Trong công nghiệp thực phẩm, để hoa quả tươi lâu khi vận chuyển đi xa, người ta bơm khí trơ nào vào túi bọc để làm giảm tốc độ oxi hóa? (Điền: nitơ)", "nitơ", "Khí nitơ N2 trơ về mặt hóa học."),
        make_sa(6, "Vận dụng cao", "Nếu tăng nhiệt độ của phản ứng lên thêm 30 °C, biết hệ số nhiệt độ gamma = 2. Tốc độ phản ứng sẽ tăng lên bao nhiêu lần?", "8", "2^3 = 8 lần.")
    ],
    "part4": [
        make_vdc(1, "Một nhóm học sinh khảo sát tốc độ phản ứng giữa magie và axit sunfuric loãng bằng cách thu khí hiđro vào ống đong chia độ úp ngược trên chậu nước. Sau các khoảng thời gian 10s, 20s, 30s, 40s, thể tích khí H2 thu được lần lượt là 15 mL, 28 mL, 38 mL, 45 mL. Tốc độ trung bình thoát khí trong khoảng thời gian từ 10s đến 20s là:", ["1,3 mL/s", "1,5 mL/s", "1,0 mL/s", "0,7 mL/s"], 0, "v_tb = (28 - 15) / (20 - 10) = 13 / 10 = 1,3 mL/s."),
        make_vdc(2, "Khi bảo quản sữa tươi thanh trùng, tại sao trên bao bì nhà sản xuất luôn khuyến cáo 'Bảo quản ở nhiệt độ 2 °C - 4 °C và dùng hết trong vòng 24 giờ sau khi mở nắp'?", ["Để nhiệt độ thấp kìm hãm tối đa tốc độ sinh sôi và chuyển hóa của vi khuẩn, và mở nắp làm nồng độ oxi tiếp xúc tăng mạnh thúc đẩy quá trình ôi thiu", "Để làm sữa ngọt hơn", "Để sữa không bị bay hơi", "Để sữa đông đặc thành phô mai"], 0, "Hạ nhiệt độ làm chậm tốc độ phản ứng phân hủy vi sinh vật; mở nắp tăng tiếp xúc với O2 và vi khuẩn."),
        make_vdc(3, "Đốt cháy một que đóm trong không khí thấy cháy sáng bình thường; đưa vào lọ chứa khí oxi nguyên chất thấy bùng cháy chói lòa; đưa vào lọ chứa khí nitơ thấy tắt ngay lập tức. Thí nghiệm chứng minh:", ["Nồng độ khí oxi quyết định tốc độ của phản ứng cháy", "Khí nitơ duy trì sự cháy tốt hơn oxi", "Que đóm cháy không cần nhiệt độ", "Tốc độ cháy trong nitơ là lớn nhất"], 0, "Nồng độ O2 càng cao tốc độ cháy càng nhanh mãnh liệt."),
        make_vdc(4, "Một bình kín chứa hỗn hợp khí gồm 1 mol SO2 và 0,5 mol O2 có mặt chất xúc tác V2O5. Nung nóng bình ở 450 °C một thời gian, hiệu suất phản ứng đạt 80%. Số mol SO3 tạo thành là:", ["0,8 mol", "1,0 mol", "0,4 mol", "0,5 mol"], 0, "2SO2 + O2 -> 2SO3. n_SO2 pư = 1 * 80% = 0,8 mol -> n_SO3 = 0,8 mol.")
    ]
}

print("Đã nạp xong Bài 7 (3 đề độc lập 100%)")
