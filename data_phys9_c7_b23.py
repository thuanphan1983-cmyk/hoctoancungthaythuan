# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 23: TÁC DỤNG CỦA TỪ TRƯỜNG LÊN ĐOẠN DÂY DẪN MANG DÒNG ĐIỆN
Bao gồm 3 đề thi độc lập 100%: phys9_c7_b23_test1, phys9_c7_b23_test2, phys9_c7_b23_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c7"
CH_TITLE = "Chương VII: Điện từ"

# =============================================================================
# BÀI 23: TÁC DỤNG CỦA TỪ TRƯỜNG LÊN ĐOẠN DÂY DẪN MANG DÒNG ĐIỆN (3 ĐỀ)
# =============================================================================

# --- phys9_c7_b23_test1 ---
p1_b23_t1 = [
    make_mc(1, "Nhận biết", "Lực mà từ trường tác dụng lên một đoạn dây dẫn mang dòng điện đặt trong từ trường được gọi là:", [
        "Lực điện từ (hay lực từ)",
        "Lực ma sát cơ học",
        "Lực đẩy Ác-si-mét",
        "Trọng lực hấp dẫn"
    ], 0, "Lực của từ trường tác dụng lên dây dẫn có dòng điện gọi là lực điện từ."),
    make_mc(2, "Nhận biết", "Quy tắc dùng để xác định chiều của lực điện từ tác dụng lên đoạn dây dẫn mang dòng điện đặt trong từ trường là:", [
        "Quy tắc bàn tay trái",
        "Quy tắc nắm tay phải",
        "Quy tắc bàn tay phải",
        "Quy tắc vặn đinh ốc"
    ], 0, "Quy tắc bàn tay trái dùng để xác định chiều của lực điện từ."),
    make_mc(3, "Nhận biết", "Trong quy tắc bàn tay trái, chiều của các đường sức từ được hứng như thế nào?", [
        "Hướng thẳng vào lòng bàn tay (xuyên vào lòng bàn tay)",
        "Đi ra từ mu bàn tay",
        "Song song với ngón tay giữa",
        "Hướng vào cổ tay"
    ], 0, "Đường sức từ xuyên thẳng vào lòng bàn tay trái."),
    make_mc(4, "Nhận biết", "Trong quy tắc bàn tay trái, chiều từ cổ tay đến ngón tay giữa chỉ:", [
        "Chiều của dòng điện chạy trong đoạn dây dẫn",
        "Chiều của lực điện từ",
        "Chiều của đường sức từ",
        "Chiều quay của động cơ"
    ], 0, "Chiều từ cổ tay đến ngón tay giữa là chiều của dòng điện."),
    make_mc(5, "Nhận biết", "Trong quy tắc bàn tay trái, ngón tay cái choãi ra 90 độ chỉ chiều của:", [
        "Lực điện từ tác dụng lên đoạn dây dẫn",
        "Dòng điện trong dây dẫn",
        "Đường sức từ ngoài không gian",
        "Lực ma sát giữa dây và không khí"
    ], 0, "Ngón tay cái choãi ra 90° chỉ chiều của lực điện từ."),
    make_mc(6, "Nhận biết", "Đoạn dây dẫn mang dòng điện đặt trong từ trường sẽ KHÔNG chịu tác dụng của lực điện từ khi đoạn dây dẫn đó:", [
        "Đặt song song với các đường sức từ",
        "Đặt vuông góc với các đường sức từ",
        "Đặt nghiêng góc 45 độ so với đường sức từ",
        "Đặt nghiêng góc 60 độ so với đường sức từ"
    ], 0, "Khi đoạn dây song song với đường sức từ thì lực từ tác dụng bằng 0."),
    make_mc(7, "Thông hiểu", "Nếu đồng thời đổi chiều dòng điện chạy qua đoạn dây dẫn và đổi chiều của các đường sức từ thì chiều của lực điện từ tác dụng lên đoạn dây sẽ:", [
        "Không thay đổi",
        "Bị đổi chiều ngược lại",
        "Biến mất hoàn toàn",
        "Tăng lên gấp đôi"
    ], 0, "Đổi chiều cả hai yếu tố thì chiều lực từ không đổi."),
    make_mc(8, "Thông hiểu", "Nếu chỉ đổi chiều dòng điện chạy qua đoạn dây dẫn (giữ nguyên chiều đường sức từ) thì lực điện từ sẽ:", [
        "Đổi chiều ngược lại",
        "Giữ nguyên không đổi",
        "Tăng độ lớn lên gấp đôi",
        "Giảm độ lớn về 0"
    ], 0, "Đổi chiều dòng điện làm lực từ đảo chiều ngược lại."),
    make_mc(9, "Thông hiểu", "Hai bộ phận chính của một động cơ điện một chiều (DC Motor) là:", [
        "Nam châm tạo từ trường (stato) và khung dây dẫn có dòng điện quay quanh trục (roto)",
        "Ắc quy và công tắc đóng ngắt",
        "Vôn kế và ampe kế",
        "Bóng đèn sợi đốt và tụ điện"
    ], 0, "Hai bộ phận chính là nam châm (stato) và khung dây dẫn (roto)."),
    make_mc(10, "Thông hiểu", "Tác dụng của bộ phận cổ góp (gồm hai vành bán khuyên và hai chổi quét) trong động cơ điện một chiều là:", [
        "Tự động đổi chiều dòng điện trong khung dây sau mỗi nửa vòng quay để khung quay liên tục theo một chiều",
        "Làm tăng nhiệt độ của khung dây",
        "Đo tốc độ quay của động cơ",
        "Cố định khung dây đứng yên"
    ], 0, "Cổ góp đổi chiều dòng điện sau mỗi nửa vòng để mômen lực từ luôn giữ khung quay theo một chiều."),
    make_mc(11, "Thông hiểu", "Khi một động cơ điện hoạt động bình thường, dạng năng lượng nào chủ yếu được chuyển hóa thành cơ năng?", [
        "Điện năng",
        "Quang năng",
        "Hóa năng",
        "Năng lượng hạt nhân"
    ], 0, "Động cơ điện chuyển hóa điện năng thành cơ năng."),
    make_mc(12, "Thông hiểu", "Loa điện động (loa phóng thanh) biến đổi tín hiệu điện dao động thành âm thanh phát ra không khí dựa trên tác dụng của:", [
        "Lực điện từ làm cuộn dây gắn với màng loa dao động tới lui trong từ trường nam châm",
        "Tác dụng phát sáng của dòng điện",
        "Lực đẩy tĩnh điện giữa hai bản tụ",
        "Tác dụng hóa học làm nóng chảy chất lỏng"
    ], 0, "Lực từ biến thiên tác dụng lên cuộn dây làm màng loa dao động sinh sóng âm thanh.")
]

p2_b23_t1 = [
    make_tf(1, "Thông hiểu", "Về lực điện từ tác dụng lên đoạn dây dẫn thẳng mang dòng điện:", [
        ("a", "Lực điện từ luôn vuông góc với cả đoạn dây dẫn và đường sức từ.", True),
        ("b", "Khi đoạn dây dẫn đặt vuông góc với đường sức từ thì lực điện từ đạt giá trị lớn nhất.", True),
        ("c", "Khi đoạn dây dẫn đặt song song với đường sức từ thì lực điện từ đạt giá trị cực đại.", False),
        ("d", "Quy tắc bàn tay trái dùng để xác định chiều của lực điện từ.", True)
    ], "Khi đặt song song với đường sức từ thì lực điện từ bằng 0."),
    make_tf(2, "Thông hiểu", "Về động cơ điện một chiều:", [
        ("a", "Động cơ điện một chiều hoạt động dựa trên tác dụng của từ trường lên khung dây dẫn có dòng điện.", True),
        ("b", "Hai cạnh đối diện của khung dây chịu tác dụng của cặp lực điện từ ngược chiều nhau tạo thành ngẫu lực làm khung quay.", True),
        ("c", "Nếu không có bộ góp điện đổi chiều dòng điện, khung dây sẽ quay đều liên tục mãi mãi.", False),
        ("d", "Hiệu suất của động cơ điện trong thực tế không đạt được 100% do có hao phí tỏa nhiệt trên dây quấn và ma sát trục quay.", True)
    ], "Không có cổ góp, khung dây chỉ dao động quanh vị trí cân bằng rồi dừng lại."),
    make_tf(3, "Vận dụng", "Một đoạn dây dẫn thẳng nằm ngang có dòng điện I chạy từ Tây sang Đông, đặt trong từ trường đều có đường sức từ hướng thẳng đứng từ dưới lên trên:", [
        ("a", "Để hứng đường sức từ, lòng bàn tay trái phải hướng xuống phía dưới đất.", True),
        ("b", "Chiều từ cổ tay đến ngón tay giữa hướng từ Tây sang Đông.", True),
        ("c", "Ngón tay cái choãi ra 90 độ chỉ về hướng Nam.", True),
        ("d", "Lực điện từ tác dụng lên đoạn dây dẫn có phương thẳng đứng hướng lên trời.", False)
    ], "Bàn tay trái úp xuống hứng đường sức từ đi lên, ngón tay chỉ Tây sang Đông thì ngón cái chỉ về hướng Nam."),
    make_tf(4, "Vận dụng", "Khảo sát lực điện từ F tác dụng lên đoạn dây dẫn dài L = 10 cm vuông góc với từ trường B = 0,2 T khi có dòng điện I chạy qua:", [
        ("a", "Nếu cường độ dòng điện là I = 2 A thì lực từ có độ lớn là F = 0,04 N.", True),
        ("b", "Nếu tăng cường độ dòng điện lên gấp 3 lần (I = 6 A) thì lực từ tăng lên thành F = 0,12 N.", True),
        ("c", "Nếu xoay đoạn dây sao cho nó song song với đường sức từ thì lực từ tăng lên gấp đôi.", False),
        ("d", "Lực điện từ tỉ lệ thuận với cường độ dòng điện I chạy qua đoạn dây.", True)
    ], "F = B.I.L = 0,2 × 2 × 0,1 = 0,04 N. Khi I = 6 A thì F = 0,12 N. Khi song song thì F = 0.")
]

p3_b23_t1 = [
    make_sa(1, "Thông hiểu", "Quy tắc nào được dùng để xác định chiều của lực điện từ tác dụng lên đoạn dây dẫn có dòng điện?", "Bàn tay trái", "Quy tắc bàn tay trái."),
    make_sa(2, "Thông hiểu", "Khi đoạn dây dẫn có dòng điện đặt song song với các đường sức từ thì lực điện từ bằng bao nhiêu N?", "0", "F = 0 khi dây song song với đường sức từ."),
    make_sa(3, "Vận dụng", "Một đoạn dây dẫn vuông góc với từ trường chịu tác dụng của lực từ F = 0,5 N. Nếu tăng cường độ dòng điện qua dây lên gấp 2 lần thì lực từ bằng bao nhiêu Newton?", "1", "F tỉ lệ thuận với I: F' = 0,5 × 2 = 1,0 N."),
    make_sa(4, "Vận dụng", "Trong động cơ điện một chiều, bộ góp điện đổi chiều dòng điện trong khung dây sau mỗi bao nhiêu độ góc quay?", "180", "Đổi chiều sau mỗi nửa vòng quay = 180°."),
    make_sa(5, "Vận dụng cao", "Đoạn dây dẫn dài L = 0,2 m mang dòng điện I = 5 A đặt vuông góc với từ trường đều B = 0,4 T. Lực điện từ tác dụng lên đoạn dây là bao nhiêu Newton?", "0.4", "F = B × I × L = 0,4 × 5 × 0,2 = 0,4 N."),
    make_sa(6, "Vận dụng cao", "Một đoạn dây dẫn dài 0,5 m đặt vuông góc với từ trường đều B = 0,2 T chịu lực từ F = 0,3 N. Cường độ dòng điện chạy qua đoạn dây là bao nhiêu Ampe?", "3", "I = F / (B × L) = 0,3 / (0,2 × 0,5) = 0,3 / 0,1 = 3 A.")
]

p4_b23_t1 = [
    make_vdc(1, "Trong xe ô tô điện hiện đại (EV), động cơ điện kéo bánh xe có thể chuyển sang chế độ phanh tái sinh năng lượng (Regenerative Braking) khi người lái nhả bàn đạp ga hoặc đạp phanh. Bản chất vật lý của phanh tái sinh là:", [
        "Động cơ điện lập tức hoạt động như một máy phát điện, chuyển đổi động năng của xe thành điện năng nạp ngược trở lại vào pin xe và sinh ra lực từ cản trở chuyển động quay giúp hãm tốc độ xe",
        "Động cơ điện khóa cứng trục quay cơ học làm mòn má phanh",
        "Xe xả hết điện trong pin ra ngoài không khí để dừng lại",
        "Động cơ quay ngược chiều với tốc độ tối đa tức thì"
    ], 0, "Động cơ đảo chức năng thành máy phát nạp điện cho pin, lực cản từ trường hãm xe giảm tốc êm ái và thu hồi năng lượng."),
    make_vdc(2, "Súng điện từ Gauss (Railgun) trong công nghệ quân sự hiện đại có thể bắn viên đạn kim loại với vận tốc siêu vượt âm (Mach 6 - 7). Súng gồm hai thanh ray kim loại song song nối với nguồn điện cực mạnh và viên đạn là vật dẫn trượt trên hai ray đặt trong từ trường vuông góc. Viên đạn bị đẩy bay đi với tốc độ cực lớn là nhờ:", [
        "Lực điện từ cực mạnh của từ trường tác dụng lên dòng điện hàng triệu Ampe chạy qua thân viên đạn",
        "Sự nổ của thuốc súng truyền thống",
        "Lực đẩy của luồng khí gas nén",
        "Phản lực của động cơ tên lửa gắn trong đạn"
    ], 0, "Lực Lorentz (lực từ) cực đại tác dụng lên đoạn đạn dẫn điện trượt giữa 2 thanh ray đẩy đạn bay ra khỏi nòng."),
    make_vdc(3, "Đồng hồ đo điện đa năng kim chỉ cơ (Galvanometer khung quay) đo cường độ dòng điện rất nhỏ dựa trên nguyên lý:", [
        "Từ trường của nam châm vĩnh cửu tác dụng ngẫu lực từ làm quay khung dây mang dòng điện ngược với lực cản của lò xo xoắn, góc quay của kim tỉ lệ với cường độ dòng điện",
        "Dòng điện nung nóng làm cong thanh kim loại",
        "Tác dụng hóa học làm đổi màu dung dịch đo",
        "Lực hút tĩnh điện giữa hai quả cầu"
    ], 0, "Cơ cấu khung quay PMMC: Lực từ cân bằng với mômen đàn hồi của lò xo xoắn, góc quay tỉ lệ tuyến tính với I."),
    make_vdc(4, "Một kỹ sư thiết kế máy bơm điện từ dẫn kim loại lỏng nóng chảy (như natri lỏng trong lò phản ứng hạt nhân) qua đường ống cách nhiệt mà không cần bất kì cánh quạt hay trục quay cơ học tiếp xúc nào. Máy bơm hoạt động bằng cách đặt từ trường vuông góc với đường ống và cho dòng điện chạy vuông góc qua kim loại lỏng. Kim loại lỏng bị đẩy chảy dọc đường ống là nhờ:", [
        "Lực điện từ tác dụng trực tiếp lên dòng điện chạy qua chất lỏng dẫn điện trong từ trường đẩy chất lỏng chuyển động dọc ống",
        "Áp suất bay hơi của kim loại",
        "Trọng lực Trái Đất",
        "Lực ma sát của thành ống dẫn"
    ], 0, "Máy bơm từ trường thủy động (MHD Pump): Lực từ tác dụng trực tiếp lên kim loại lỏng mang dòng điện đẩy dòng chảy đi mà không cần cánh quạt cơ học.")
]

exams["phys9_c7_b23_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b23", "Bài 23: Tác dụng của từ trường lên đoạn dây dẫn mang dòng điện", 1, p1_b23_t1, p2_b23_t1, p3_b23_t1, p4_b23_t1)

# --- phys9_c7_b23_test2 ---
p1_b23_t2 = [
    make_mc(1, "Nhận biết", "Quy tắc bàn tay trái xác định được:", [
        "Chiều của lực điện từ tác dụng lên đoạn dây dẫn mang dòng điện đặt trong từ trường",
        "Chiều của các đường sức từ ngoài thanh nam châm",
        "Chiều của dòng điện cảm ứng",
        "Độ lớn của hiệu điện thế nguồn"
    ], 0, "Quy tắc bàn tay trái xác định chiều của lực điện từ."),
    make_mc(2, "Nhận biết", "Khi áp dụng quy tắc bàn tay trái, các đường sức từ đi vào:", [
        "Lòng bàn tay trái",
        "Mu bàn tay trái",
        "Đầu ngón tay cái",
        "Khe giữa các ngón tay"
    ], 0, "Đường sức từ xuyên vào lòng bàn tay."),
    make_mc(3, "Nhận biết", "Chiều từ cổ tay đến ngón tay giữa trong quy tắc bàn tay trái biểu diễn:", [
        "Chiều dòng điện chạy trong đoạn dây dẫn",
        "Chiều của đường sức từ",
        "Chiều của lực điện từ",
        "Chiều của trọng lực"
    ], 0, "Chiều từ cổ tay đến ngón tay giữa là chiều dòng điện."),
    make_mc(4, "Nhận biết", "Lực điện từ có phương:", [
        "Vuông góc với cả đoạn dây dẫn và đường sức từ",
        "Song song với đoạn dây dẫn",
        "Trùng với phương của đường sức từ",
        "Tạo góc 45 độ với mặt phẳng chứa dây dẫn và đường sức từ"
    ], 0, "Lực điện từ luôn vuông góc với mặt phẳng chứa đoạn dây dẫn và đường sức từ."),
    make_mc(5, "Nhận biết", "Trong động cơ điện một chiều, bộ phận đứng yên tạo ra từ trường được gọi là:", [
        "Stato",
        "Roto",
        "Cổ góp",
        "Chổi than"
    ], 0, "Stato là phần đứng yên tạo từ trường."),
    make_mc(6, "Nhận biết", "Bộ phận quay của động cơ điện một chiều được gọi là:", [
        "Roto",
        "Stato",
        "Khung vỏ",
        "Ổ bi"
    ], 0, "Roto là phần chuyển động quay."),
    make_mc(7, "Thông hiểu", "Một đoạn dây dẫn mang dòng điện đặt vuông góc với đường sức từ. Nếu đổi chiều đường sức từ (giữ nguyên chiều dòng điện) thì lực điện từ sẽ:", [
        "Đổi chiều ngược lại",
        "Không thay đổi chiều",
        "Tăng độ lớn lên gấp 4 lần",
        "Biến mất hoàn toàn"
    ], 0, "Đổi chiều đường sức từ thì lực từ bị đảo ngược chiều."),
    make_mc(8, "Thông hiểu", "Một đoạn dây dẫn mang dòng điện đặt trong từ trường đều. Trong trường hợp nào sau đây lực điện từ tác dụng lên dây có độ lớn bằng 0?", [
        "Đoạn dây dẫn đặt song song với các đường sức từ",
        "Đoạn dây dẫn đặt vuông góc với các đường sức từ",
        "Đoạn dây dẫn đặt nghiêng góc 30 độ so với đường sức từ",
        "Đoạn dây dẫn đặt nghiêng góc 60 độ so với đường sức từ"
    ], 0, "Khi đoạn dây song song với đường sức từ thì lực từ F = 0."),
    make_mc(9, "Thông hiểu", "Khi một khung dây dẫn có dòng điện đặt trong từ trường đều, cặp lực từ tác dụng lên hai cạnh đối diện của khung dây tạo thành:", [
        "Một ngẫu lực làm khung dây quay quanh trục của nó",
        "Một lực kéo làm khung dây chuyển động tịnh tiến sang ngang",
        "Lực nén làm méo khung dây",
        "Không có lực nào tác dụng"
    ], 0, "Cặp lực từ ngược chiều tác dụng vào hai cạnh đối diện tạo thành ngẫu lực quay."),
    make_mc(10, "Thông hiểu", "Nếu không có hai thanh quét và hai bán khuyên (cổ góp điện) thì khung dây của động cơ điện một chiều sẽ:", [
        "Chỉ quay được nửa vòng rồi dừng lại ở vị trí cân bằng bền",
        "Quay nhanh hơn gấp đôi",
        "Tự động sinh ra điện năng",
        "Bị nóng chảy tức thì"
    ], 0, "Không có cổ góp đổi chiều dòng điện thì ngẫu lực đổi chiều kéo ngược khung dừng ở vị trí mặt khung vuông góc đường sức từ."),
    make_mc(11, "Thông hiểu", "Thiết bị nào sau đây hoạt động dựa trên tác dụng của lực từ lên khung dây dẫn có dòng điện?", [
        "Quạt điện chạy bằng pin một chiều",
        "Ấm đun nước siêu tốc",
        "Bình thủy tinh giữ nhiệt",
        "Nồi cơm điện tử"
    ], 0, "Quạt điện dùng động cơ điện hoạt động nhờ lực từ làm quay khung dây."),
    make_mc(12, "Thông hiểu", "Loa điện thoại thông minh phát ra âm thanh khi có tín hiệu điện là nhờ:", [
        "Cuộn dây nhỏ mang dòng điện âm tần dao động trong khe từ trường của nam châm làm màng loa rung động",
        "Pin điện thoại phát ra sóng âm thanh",
        "Mặt kính màn hình tự rung",
        "Sóng vô tuyến đập trực tiếp vào tai"
    ], 0, "Loa điện động mini rung màng nhờ lực từ tác dụng lên cuộn dây âm tần.")
]

p2_b23_t2 = [
    make_tf(1, "Thông hiểu", "Xét các yếu tố tác động đến lực điện từ:", [
        ("a", "Lực điện từ đổi chiều khi đổi chiều dòng điện.", True),
        ("b", "Lực điện từ đổi chiều khi đổi chiều đường sức từ.", True),
        ("c", "Lực điện từ không đổi chiều khi đồng thời đổi chiều cả dòng điện và đường sức từ.", True),
        ("d", "Lực điện từ phụ thuộc vào màu sắc của lớp vỏ cách điện của dây dẫn.", False)
    ], "Màu sơn vỏ cách điện không ảnh hưởng đến lực từ."),
    make_tf(2, "Thông hiểu", "Về cấu tạo và nguyên lý của loa điện động:", [
        ("a", "Gồm một nam châm hình trụ có lõi từ và một cuộn dây gắn với màng loa.", True),
        ("b", "Khi dòng điện âm tần chạy qua cuộn dây, lực từ làm cuộn dây dao động dọc trục.", True),
        ("c", "Màng loa dao động ép vào không khí tạo ra sóng âm truyền tới tai người nghe.", True),
        ("d", "Loa điện động chỉ hoạt động với dòng điện một chiều không đổi phát ra âm thanh liên tục.", False)
    ], "Dòng điện âm tần biến thiên mới tạo dao động âm thanh; dòng DC không đổi chỉ kéo màng loa lệch một vị trí cố định."),
    make_tf(3, "Vận dụng", "Một đoạn dây dẫn thẳng đặt nằm ngang có dòng điện I chạy từ Bắc xuống Nam, đặt trong từ trường đều có đường sức từ hướng từ Đông sang Tây:", [
        ("a", "Bàn tay trái phải hướng lòng bàn tay sang hướng Đông để hứng đường sức từ.", True),
        ("b", "Chiều từ cổ tay đến ngón tay giữa hướng từ Bắc xuống Nam.", True),
        ("c", "Ngón tay cái choãi ra 90 độ hướng thẳng đứng lên trời.", True),
        ("d", "Lực điện từ tác dụng lên đoạn dây dẫn có chiều hướng thẳng đứng xuống đất.", False)
    ], "Hứng từ Đông sang Tây thì ngón cái choãi ra hướng lên trên (thẳng đứng lên trời)."),
    make_tf(4, "Vận dụng", "Một đoạn dây dẫn dài L = 20 cm đặt vuông góc với từ trường đều B = 0,5 T. Cường độ dòng điện qua dây là I = 4 A:", [
        ("a", "Lực điện từ tác dụng lên đoạn dây là F = 0,4 N.", True),
        ("b", "Nếu tăng dòng điện lên I = 8 A thì lực từ tăng lên F = 0,8 N.", True),
        ("c", "Nếu giảm chiều dài đoạn dây chịu tác dụng của từ trường xuống một nửa thì lực từ giảm một nửa.", True),
        ("d", "Nếu xoay đoạn dây một góc 180 độ thì lực từ không đổi chiều.", False)
    ], "F = B.I.L = 0,5 × 4 × 0,2 = 0,4 N. Xoay 180° tức là đảo chiều dòng điện nên lực từ đổi chiều.")
]

p3_b23_t2 = [
    make_sa(1, "Thông hiểu", "Ngón tay nào trong quy tắc bàn tay trái chỉ chiều của lực điện từ?", "Ngón cái", "Ngón tay cái choãi ra 90° chỉ chiều lực từ."),
    make_sa(2, "Thông hiểu", "Động cơ điện chuyển hóa năng lượng nào thành cơ năng?", "Điện năng", "Điện năng thành cơ năng."),
    make_sa(3, "Vận dụng", "Đoạn dây dẫn chịu lực từ F = 1,2 N. Nếu cường độ dòng điện giảm đi một nửa thì lực từ tác dụng lên đoạn dây bằng bao nhiêu Newton?", "0.6", "F' = 1,2 / 2 = 0,6 N."),
    make_sa(4, "Vận dụng", "Một đoạn dây dẫn dài 0,1 m mang dòng điện 2 A đặt vuông góc trong từ trường đều B = 0,5 T. Lực điện từ tác dụng lên đoạn dây bằng bao nhiêu Newton?", "0.1", "F = 0,5 × 2 × 0,1 = 0,1 N."),
    make_sa(5, "Vận dụng cao", "Một đoạn dây dẫn đặt vuông góc với từ trường đều B = 0,25 T chịu lực từ F = 0,1 N khi dòng điện I = 2 A. Chiều dài L của đoạn dây trong từ trường là bao nhiêu mét?", "0.2", "L = F / (B × I) = 0,1 / (0,25 × 2) = 0,1 / 0,5 = 0,2 m."),
    make_sa(6, "Vận dụng cao", "Đoạn dây dẫn dài 0,4 m đặt vuông góc trong từ trường chịu lực từ F = 0,8 N khi dòng điện I = 5 A. Độ lớn từ trường B là bao nhiêu Tesla (T)?", "0.4", "B = F / (I × L) = 0,8 / (5 × 0,4) = 0,8 / 2 = 0,4 T.")
]

p4_b23_t2 = [
    make_vdc(1, "Trong xe máy và ô tô, củ đề (động cơ khởi động điện - Starter Motor) là một động cơ điện một chiều công suất rất lớn (từ 1 kW đến 3 kW). Khi người lái bấm nút đề, dòng điện từ bình ắc quy phóng qua động cơ khởi động để làm quay trục khuỷu động cơ xăng. Để tạo ra mômen quay cực đại tức thì, thiết kế động cơ khởi động có đặc điểm gì?", [
        "Cuộn dây stato và roto được quấn bằng các thanh đồng to bản có điện trở cực nhỏ để cho dòng điện hàng trăm Ampe đi qua trong vài giây đầu",
        "Dùng dây điện siêu mảnh bằng nhôm",
        "Chỉ dùng nam châm vĩnh cửu siêu nhỏ",
        "Có cánh quạt làm mát bằng nước đá"
    ], 0, "Dây quấn đồng to bản chịu dòng phóng cực lớn (100A - 300A) tạo mômen lực từ khổng lồ khởi động động cơ đốt trong."),
    make_vdc(2, "Nguyên lý con lắc từ trường nhảy (Con lắc Roget): Một lò xo dẫn điện treo thẳng đứng có đầu dưới nhúng vào một chén thủy ngân dẫn điện nối với nguồn điện. Khi đóng mạch điện, các vòng dây của lò xo lập tức:", [
        "Hút nhau làm lò xo co ngắn lại, đầu dưới nhấc khỏi thủy ngân ngắt mạch điện, lò xo giãn ra chạm lại thủy ngân lặp lại dao động liên tục",
        "Đẩy nhau làm lò xo giãn dài ra chạm đáy chén thủy ngân và dính chặt mãi mãi",
        "Xoắn tròn lại quanh trục",
        "Bị nóng chảy tức thì và bốc hơi"
    ], 0, "Các vòng dây song song có dòng điện cùng chiều hút nhau làm lò xo co lại ngắt mạch, chu kỳ đóng ngắt lặp lại tạo dao động nhún nhảy."),
    make_vdc(3, "Cân điện từ vi lượng (Electromagnetic Microbalance) trong phòng thí nghiệm phân tích hóa học chính xác tới 0,0001 mg hoạt động bằng cách bù trừ trọng lượng mẫu vật bằng lực điện từ. Khi đặt mẫu vật lên đĩa cân:", [
        "Hệ thống tự động tăng dòng điện qua cuộn dây đặt trong từ trường để sinh lực từ nâng đĩa cân về vị trí cân bằng, dòng điện đo được phản ánh chính xác khối lượng mẫu vật",
        "Mẫu vật bị từ trường hút dính chặt vào đĩa cân",
        "Mẫu vật bị đốt cháy hoàn toàn để đo tro",
        "Đĩa cân rơi xuống đáy tủ kính"
    ], 0, "Nguyên lý cân bù lực từ: Lực từ F = B.I.L cân bằng chính xác với trọng lượng P = m.g, dòng I đo được tỉ lệ tuyến tính với khối lượng m."),
    make_vdc(4, "Một khung dây dẫn hình chữ nhật mang dòng điện đặt trong từ trường đều của nam châm chữ U. Khi khung dây quay đến vị trí mặt phẳng khung dây vuông góc với các đường sức từ thì:", [
        "Cặp lực từ tác dụng lên hai cạnh đối diện cùng nằm trên một mặt phẳng và kéo dãn khung dây (mômen ngẫu lực bằng 0), khung ở vị trí cân bằng",
        "Lực từ đạt giá trị cực đại làm khung quay nhanh nhất",
        "Lực từ tự động biến mất hoàn toàn",
        "Dòng điện trong khung bị ngắt đột ngột"
    ], 0, "Tại vị trí mặt phẳng khung vuông góc đường sức từ, hai lực từ đối diện cùng phương ngược chiều nằm trong mặt phẳng khung, mômen quay bằng 0 (vị trí cân bằng).")
]

exams["phys9_c7_b23_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b23", "Bài 23: Tác dụng của từ trường lên đoạn dây dẫn mang dòng điện", 2, p1_b23_t2, p2_b23_t2, p3_b23_t2, p4_b23_t2)

# --- phys9_c7_b23_test3 ---
p1_b23_t3 = [
    make_mc(1, "Nhận biết", "Lực điện từ tác dụng lên đoạn dây dẫn mang dòng điện đặt vuông góc với đường sức từ có độ lớn phụ thuộc vào:", [
        "Cường độ dòng điện, chiều dài đoạn dây dẫn và độ mạnh yếu của từ trường",
        "Màu sắc của lớp vỏ nhựa bọc dây dẫn",
        "Vận tốc gió trong phòng",
        "Khối lượng của Trái Đất"
    ], 0, "F phụ thuộc I, L và từ trường B."),
    make_mc(2, "Nhận biết", "Để xác định chiều của lực điện từ, ta dùng bàn tay trái theo quy tắc:", [
        "Đặt bàn tay trái hứng đường sức từ vào lòng bàn tay, chiều từ cổ tay đến ngón tay giữa chỉ chiều dòng điện, ngón cái choãi 90 độ chỉ chiều lực từ",
        "Nắm bàn tay trái sao cho 4 ngón tay theo chiều dòng điện",
        "Đặt úp bàn tay phải lên mặt phẳng",
        "Ngửa hai bàn tay hứng ánh sáng"
    ], 0, "Định nghĩa quy tắc bàn tay trái."),
    make_mc(3, "Nhận biết", "Trong quy tắc bàn tay trái, nếu đường sức từ đi từ cực Bắc sang cực Nam thì lòng bàn tay phải hướng về phía:", [
        "Cực Bắc của nam châm để hứng đường sức từ",
        "Cực Nam của nam châm",
        "Mặt đất",
        "Nguồn điện"
    ], 0, "Đường sức từ ra Bắc vào Nam nên lòng bàn tay phải hướng về phía cực Bắc để hứng đường sức từ đâm vào."),
    make_mc(4, "Nhận biết", "Khi đoạn dây dẫn có dòng điện đổi chiều từ trái sang phải thành từ phải sang trái thì lực điện từ sẽ:", [
        "Đổi chiều ngược lại",
        "Giữ nguyên phương chiều cũ",
        "Biến thành trọng lực",
        "Tăng độ lớn lên gấp mười lần"
    ], 0, "Đổi chiều dòng điện làm lực từ đổi chiều ngược lại."),
    make_mc(5, "Nhận biết", "Cổ góp điện trong động cơ điện một chiều gồm có:", [
        "Hai vành bán khuyên cách điện và hai chổi quét tì sát",
        "Hai vòng bi thép",
        "Một thanh nam châm vĩnh cửu",
        "Hai bóng đèn LED báo nguồn"
    ], 0, "Cổ góp gồm 2 bán khuyên và 2 chổi quét than tì sát."),
    make_mc(6, "Nhận biết", "Động cơ điện được ứng dụng trong thiết bị nào sau đây trong đời sống?", [
        "Quạt trần, máy bơm nước, máy khoan cầm tay",
        "Bếp than tổ ong",
        "Ấm sắc thuốc bắc",
        "Gương soi trang điểm"
    ], 0, "Quạt trần, máy bơm, máy khoan đều chạy bằng động cơ điện."),
    make_mc(7, "Thông hiểu", "Một đoạn dây dẫn mang dòng điện đặt nằm ngang theo phương Đông - Tây, lực từ tác dụng lên dây có phương thẳng đứng. Đường sức từ của từ trường có thể nằm theo phương nào?", [
        "Phương Bắc - Nam",
        "Phương Đông - Tây",
        "Phương thẳng đứng",
        "Bất kì phương nào"
    ], 0, "Đoạn dây (Đông - Tây), lực từ (thẳng đứng) => đường sức từ phải nằm theo phương Bắc - Nam để vuông góc với cả hai."),
    make_mc(8, "Thông hiểu", "Khi một khung dây mang dòng điện đặt trong từ trường đang quay, nếu ngắt nguồn điện cấp cho khung dây thì khung dây sẽ:", [
        "Quay chậm dần rồi dừng lại do lực cản ma sát",
        "Dừng lại ngay lập tức tại chỗ",
        "Tự động tăng tốc quay nhanh hơn",
        "Đảo chiều quay liên tục"
    ], 0, "Ngắt điện thì mất lực từ, khung dây quay theo quán tính chậm dần rồi dừng lại do ma sát."),
    make_mc(9, "Thông hiểu", "Để động cơ điện một chiều quay nhanh hơn (tăng tốc độ quay), người ta có thể:", [
        "Tăng cường độ dòng điện chạy qua cuộn dây của động cơ",
        "Giảm hiệu điện thế cấp nguồn",
        "Rút bớt vòng dây trong cuộn dây",
        "Tháo bớt nam châm ra ngoài"
    ], 0, "Tăng dòng điện I làm tăng lực từ và mômen quay của động cơ."),
    make_mc(10, "Thông hiểu", "Màng loa trong loa điện động thường được làm bằng giấy đặc biệt hoặc màng polymer mỏng nhẹ nhằm mục đích:", [
        "Có khối lượng nhỏ và độ đàn hồi tốt để dao động nhanh theo tín hiệu âm thanh với độ trung thực cao",
        "Dẫn điện thật tốt từ nam châm",
        "Chống nước sôi 100 độ C",
        "Tạo ra từ trường vĩnh cửu"
    ], 0, "Màng loa nhẹ và đàn hồi giúp dao động nhanh nhạy theo tần số âm thanh tạo âm trong trẻo."),
    make_mc(11, "Thông hiểu", "Một khung dây dẫn mang dòng điện được đặt trong từ trường đều. Khung dây sẽ đứng yên không quay khi mặt phẳng của khung dây:", [
        "Vuông góc với các đường sức từ",
        "Song song với các đường sức từ",
        "Nghiêng góc 30 độ so với đường sức từ",
        "Nghiêng góc 45 độ so với đường sức từ"
    ], 0, "Khi mặt khung vuông góc đường sức từ thì mômen quay bằng 0, khung ở vị trí cân bằng."),
    make_mc(12, "Thông hiểu", "Khi nối hai dây dẫn song song có dòng điện chạy cùng chiều với nhau, giữa hai dây dẫn xuất hiện lực tương tác gì?", [
        "Lực hút lẫn nhau",
        "Lực đẩy lẫn nhau",
        "Không có lực tương tác",
        "Lực xoắn quanh nhau"
    ], 0, "Hai dây dẫn thẳng song song có dòng điện cùng chiều thì hút nhau (ngược chiều thì đẩy nhau).")
]

p2_b23_t3 = [
    make_tf(1, "Thông hiểu", "Về tương tác từ giữa dòng điện và từ trường:", [
        ("a", "Từ trường tác dụng lực lên điện tích chuyển động.", True),
        ("b", "Đoạn dây dẫn có dòng điện thực chất là dòng các hạt mang điện tích dịch chuyển có hướng.", True),
        ("c", "Lực điện từ có độ lớn lớn nhất khi góc giữa dây dẫn và đường sức từ bằng 90 độ.", True),
        ("d", "Lực điện từ có độ lớn lớn nhất khi đoạn dây song song với đường sức từ.", False)
    ], "Lực từ lớn nhất khi vuông góc (90°), và bằng 0 khi song song (0° hoặc 180°)."),
    make_tf(2, "Thông hiểu", "Về động cơ điện trong thực tiễn đời sống:", [
        ("a", "Động cơ điện chuyển hóa phần lớn điện năng thành cơ năng có ích.", True),
        ("b", "Động cơ điện thân thiện với môi trường hơn động cơ đốt trong vì không phát thải khí CO2 trực tiếp khi hoạt động.", True),
        ("c", "Động cơ điện xe máy điện không cần sử dụng bất kỳ từ trường nào.", False),
        ("d", "Xe điện có khả năng tăng tốc nhanh mượt mà nhờ động cơ điện sinh mômen xoắn lớn ngay từ tốc độ xuất phát.", True)
    ], "Động cơ điện bắt buộc phải có từ trường (nam châm vĩnh cửu hoặc nam châm điện) để hoạt động."),
    make_tf(3, "Vận dụng", "Hai thanh ray kim loại song song đặt nằm ngang trong từ trường đều hướng thẳng đứng xuống đất. Đoạn dây nhôm AB đặt vuông góc trên hai ray mang dòng điện chạy từ A sang B:", [
        ("a", "Lòng bàn tay trái phải hướng lên trời để hứng đường sức từ hướng xuống.", True),
        ("b", "Chiều từ cổ tay đến ngón tay giữa hướng từ A sang B.", True),
        ("c", "Ngón tay cái choãi ra 90 độ chỉ chiều lực từ tác dụng lên đoạn dây AB.", True),
        ("d", "Lực từ làm đoạn dây AB trượt dọc theo hai thanh ray.", True)
    ], "Lực từ nằm ngang vuông góc với AB đẩy đoạn dây lăn trượt dọc theo 2 ray dẫn."),
    make_tf(4, "Vận dụng", "Đoạn dây dẫn thẳng dài L = 15 cm mang dòng điện I = 2 A đặt vuông góc trong từ trường đều B = 0,4 T:", [
        ("a", "Lực điện từ tác dụng lên đoạn dây là F = 0,12 N.", True),
        ("b", "Nếu tăng dòng điện lên I = 4 A thì lực từ tăng lên F = 0,24 N.", True),
        ("c", "Nếu giảm từ trường đi một nửa (B = 0,2 T) thì lực từ giảm đi một nửa.", True),
        ("d", "Nếu giữ nguyên I và B nhưng gập đôi đoạn dây lại thì lực từ tăng gấp đôi.", False)
    ], "F = B.I.L = 0,4 × 2 × 0,15 = 0,12 N. Gập đôi dây thì chiều dài trong từ trường giảm một nửa nên lực từ giảm một nửa.")
]

p3_b23_t3 = [
    make_sa(1, "Thông hiểu", "Hai đoạn dây dẫn thẳng song song có dòng điện chạy cùng chiều nhau thì hút nhau hay đẩy nhau?", "Hút nhau", "Dòng điện cùng chiều thì hút nhau."),
    make_sa(2, "Thông hiểu", "Bộ phận nào trong động cơ điện một chiều làm nhiệm vụ đổi chiều dòng điện sau mỗi nửa vòng quay?", "Cổ góp", "Cổ góp (bán khuyên và chổi quét)."),
    make_sa(3, "Vận dụng", "Một đoạn dây dẫn mang dòng điện chịu lực từ F = 0,8 N. Nếu tăng độ lớn từ trường B lên gấp đôi thì lực từ tác dụng lên dây là bao nhiêu Newton?", "1.6", "F' = 0,8 × 2 = 1,6 N."),
    make_sa(4, "Vận dụng", "Đoạn dây dẫn dài 0,25 m mang dòng điện 4 A đặt vuông góc trong từ trường đều B = 0,3 T. Lực điện từ tác dụng lên đoạn dây bằng bao nhiêu Newton?", "0.3", "F = 0,3 × 4 × 0,25 = 0,3 N."),
    make_sa(5, "Vận dụng cao", "Một đoạn dây dẫn dài L = 0,4 m đặt vuông góc trong từ trường B = 0,5 T. Để lực từ tác dụng lên đoạn dây là F = 1 N thì cường độ dòng điện chạy qua dây là bao nhiêu Ampe?", "5", "I = F / (B × L) = 1 / (0,5 × 0,4) = 1 / 0,2 = 5 A."),
    make_sa(6, "Vận dụng cao", "Đoạn dây mang dòng điện I = 3 A dài 0,2 m chịu lực từ F = 0,18 N khi đặt vuông góc với từ trường. Độ lớn cảm ứng từ B bằng bao nhiêu Tesla?", "0.3", "B = F / (I × L) = 0,18 / (3 × 0,2) = 0,18 / 0,6 = 0,3 T.")
]

p4_b23_t3 = [
    make_vdc(1, "Động cơ điện không chổi than (Brushless DC Motor - BLDC) được ứng dụng trong flycam (drone), xe điện Tesla và quạt thông minh cao cấp. Khác với động cơ DC truyền thống có chổi than cơ học dễ mòn và đánh lửa, động cơ BLDC sử dụng:", [
        "Mạch vi điều khiển điện tử thông minh để tự động chuyển mạch dòng điện trong các cuộn dây stato cố định, làm roto nam châm vĩnh cửu quay êm ái với tuổi thọ siêu bền và hiệu suất trên 90%",
        "Bộ ly hợp thủy lực bằng dầu",
        "Bình ắc quy tự phát nổ nhỏ",
        "Bộ truyền động xích xe đạp"
    ], 0, "Động cơ BLDC dùng chuyển mạch điện tử (Electronic Commutation) triệt tiêu ma sát chổi than, tuổi thọ cực cao và hiệu suất tối ưu."),
    make_vdc(2, "Máy gia tốc hạt dạng vòng (Synchrotron hoặc Cyclotron) dùng trong vật lý hạt nhân và xạ trị ung thư sử dụng các nam châm lưỡng cực công suất lớn để uốn cong quỹ đạo chùm hạt mang điện (như proton hoặc electron). Chùm hạt uốn cong thành quỹ đạo tròn khép kín là nhờ:", [
        "Lực từ Lorentz tác dụng liên tục vuông góc với vận tốc chuyển động của hạt đóng vai trò lực hướng tâm",
        "Hạt va chạm với thành ống chân không",
        "Lực hút tĩnh điện của hạt nhân",
        "Áp suất ánh sáng đẩy hạt"
    ], 0, "Lực từ F = q.v.B luôn vuông góc với véc tơ vận tốc v nên đóng vai trò lực hướng tâm bẻ cong quỹ đạo hạt thành đường tròn."),
    make_vdc(3, "Tai nghe màng phẳng từ tính cao cấp (Planar Magnetic Headphones) dành cho người thẩm âm chuyên nghiệp có màng loa siêu mỏng in mạch dẫn điện đặt giữa hai giàn nam châm vĩnh cửu đối xứng. Khi có dòng điện âm tần chạy qua, toàn bộ diện tích màng loa:", [
        "Được lực điện từ phân bố đều đẩy kéo đồng thời trên toàn bộ bề mặt màng, giúp âm thanh phát ra cực kỳ chi tiết, độ méo tiếng xấp xỉ bằng 0",
        "Bị uốn cong tại tâm như loa hình nón",
        "Nóng đỏ lên như dây mayso",
        "Tự động đổi màu theo nhịp điệu bài hát"
    ], 0, "Lực từ phân bố đều trên khắp diện tích màng phẳng, triệt tiêu méo phi tuyến của màng loa nón truyền thống."),
    make_vdc(4, "Một kỹ sư thiết kế bộ truyền động tuyến tính (Linear Motor) cho cửa tự động tàu điện ngầm. Thay vì dùng động cơ quay kéo dây curoa, người ta 'trải phẳng' stato của động cơ dọc theo thanh trượt ray cửa. Cánh cửa gắn roto mở đóng trực tiếp với tốc độ nhanh và êm là nhờ:", [
        "Lực điện từ tuyến tính tác dụng trực tiếp dọc theo thanh ray đẩy cánh cửa chuyển động thẳng mà không cần bất kỳ bộ phận truyền động cơ học trung gian nào",
        "Khí nén đẩy xi lanh thủy lực",
        "Lò xo kéo tay",
        "Sức căng của nam châm vĩnh cửu"
    ], 0, "Động cơ tuyến tính tạo lực từ đẩy thẳng dọc thanh ray, loại bỏ hộp số và dây đai cơ học, chuyển động nhanh và không mòn cơ.")
]

exams["phys9_c7_b23_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b23", "Bài 23: Tác dụng của từ trường lên đoạn dây dẫn mang dòng điện", 3, p1_b23_t3, p2_b23_t3, p3_b23_t3, p4_b23_t3)

print("Added phys9_c7_b23 (3 tests).")
