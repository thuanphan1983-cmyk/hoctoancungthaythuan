# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG VI: ÁNH SÁNG
Bao gồm 5 đề thi độc lập 100%: phys9_c6_rev_test1 đến phys9_c6_rev_test5
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c6"
CH_TITLE = "Chương VI: Ánh sáng"
L_ID = "phys9_c6_rev"
L_NAME = "[Đề tổng hợp] Ôn tập cuối Chương VI"

# =============================================================================
# phys9_c6_rev_test1
# =============================================================================
p1_rev_t1 = [
    make_mc(1, "Nhận biết", "Hiện tượng khúc xạ ánh sáng là hiện tượng tia sáng truyền xiên góc qua mặt phân cách giữa hai môi trường trong suốt bị:", [
        "Gãy khúc tại mặt phân cách",
        "Hắt ngược trở lại môi trường cũ",
        "Truyền thẳng tuyệt đối",
        "Biến thành sóng âm thanh"
    ], 0, "Khúc xạ ánh sáng là hiện tượng tia sáng bị gãy khúc tại mặt phân cách."),
    make_mc(2, "Nhận biết", "Điều kiện cần và đủ để xảy ra hiện tượng phản xạ toàn phần là:", [
        "Ánh sáng truyền từ môi trường chiết quang hơn sang kém hơn và góc tới i >= igh",
        "Ánh sáng truyền từ không khí vào nước và góc tới i = 0 độ",
        "Ánh sáng truyền qua thấu kính phân kì",
        "Ánh sáng chiếu vuông góc với mặt gương phẳng"
    ], 0, "Điều kiện: n1 > n2 và i ≥ igh."),
    make_mc(3, "Nhận biết", "Thấu kính hội tụ có đặc điểm hình học nhận biết bên ngoài là:", [
        "Phần rìa mỏng hơn phần giữa",
        "Phần rìa dày hơn phần giữa",
        "Bề mặt phẳng cả hai bên",
        "Luôn có màu đen đục"
    ], 0, "Thấu kính hội tụ có phần rìa mỏng hơn phần giữa."),
    make_mc(4, "Nhận biết", "Chùm tia sáng song song với trục chính sau khi đi qua thấu kính hội tụ sẽ:", [
        "Hội tụ tại tiêu điểm chính của thấu kính",
        "Bị loe rộng ra xa",
        "Song song tiếp tục mãi mãi",
        "Bật ngược lại nguồn phát"
    ], 0, "Chùm song song qua TKHT hội tụ tại tiêu điểm F'."),
    make_mc(5, "Nhận biết", "Kính lúp là một thấu kính hội tụ có tiêu cự ngắn dùng để:", [
        "Quan sát các vật có kích thước nhỏ",
        "Nhìn các ngôi sao ở rất xa",
        "Đo nhiệt độ cơ thể",
        "Hút các vật bằng sắt thép"
    ], 0, "Kính lúp là thấu kính hội tụ f ngắn dùng quan sát vật nhỏ."),
    make_mc(6, "Nhận biết", "Công thức liên hệ giữa số bội giác G và tiêu cự f (tính bằng cm) của kính lúp là:", [
        "G = 25 / f",
        "G = f / 25",
        "G = 25 × f",
        "G = f + 25"
    ], 0, "G = 25 / f (với f tính bằng cm)."),
    make_mc(7, "Thông hiểu", "Một tia sáng chiếu từ nước ra không khí với góc tới i = 30 độ. Nhận xét nào sau đây về góc khúc xạ r là đúng?", [
        "r > 30 độ",
        "r < 30 độ",
        "r = 30 độ",
        "r = 0 độ"
    ], 0, "Từ nước ra không khí kém chiết quang hơn nên tia sáng lệch xa pháp tuyến: r > i = 30°."),
    make_mc(8, "Thông hiểu", "Ứng dụng quan trọng nhất của hiện tượng phản xạ toàn phần trong công nghệ thông tin liên lạc hiện nay là:", [
        "Cáp quang viễn thông truyền internet tốc độ cao xuyên đại dương",
        "Gương soi trong phòng tắm",
        "Kính lúp đọc sách",
        "Mắt kính chống bụi"
    ], 0, "Cáp quang ứng dụng phản xạ toàn phần để truyền xung ánh sáng tốc độ cao."),
    make_mc(9, "Thông hiểu", "Đặt vật thật vuông góc với trục chính của thấu kính hội tụ ở khoảng cách d > 2f. Ảnh thu được trên màn chắn có đặc điểm:", [
        "Ảnh thật, ngược chiều và nhỏ hơn vật",
        "Ảnh ảo, cùng chiều và lớn hơn vật",
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Ảnh ảo, cùng chiều và nhỏ hơn vật"
    ], 0, "d > 2f qua TKHT cho ảnh thật, ngược chiều, nhỏ hơn vật."),
    make_mc(10, "Thông hiểu", "Vật sáng thật đặt trước thấu kính phân kì luôn cho:", [
        "Ảnh ảo, cùng chiều, nhỏ hơn vật và nằm trong khoảng tiêu cự",
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Ảnh ảo, ngược chiều và bằng vật",
        "Ảnh thật, cùng chiều và nằm ngoài khoảng tiêu cự"
    ], 0, "TKPK luôn cho ảnh ảo cùng chiều nhỏ hơn vật nằm trong khoảng tiêu cự."),
    make_mc(11, "Thông hiểu", "Một kính lúp có ghi kí hiệu 5x trên vành kính thì có tiêu cự là:", [
        "5 cm",
        "10 cm",
        "2,5 cm",
        "25 cm"
    ], 0, "f = 25 / G = 25 / 5 = 5 cm."),
    make_mc(12, "Thông hiểu", "Trong bài thực hành đo tiêu cự theo phương pháp Silbermann, khi ảnh thật trên màn chắn có kích thước bằng vật thì khoảng cách giữa vật và màn là:", [
        "L = 4f",
        "L = 2f",
        "L = f",
        "L = 0,5f"
    ], 0, "L = d + d' = 2f + 2f = 4f.")
]

p2_rev_t1 = [
    make_tf(1, "Thông hiểu", "Xét các hiện tượng quang học cơ bản trong Chương VI:", [
        ("a", "Hiện tượng khúc xạ ánh sáng chỉ xảy ra khi ánh sáng truyền qua mặt phân cách giữa hai môi trường trong suốt với góc tới i > 0.", True),
        ("b", "Hiện tượng phản xạ toàn phần có thể xảy ra khi ánh sáng truyền từ không khí vào nước.", False),
        ("c", "Thấu kính hội tụ biến chùm tia tới song song trục chính thành chùm tia ló hội tụ tại tiêu điểm.", True),
        ("d", "Thấu kính phân kì luôn cho ảnh ảo đối với vật thật.", True)
    ], "Không khí sang nước là từ kém sang chiết quang hơn nên không thể phản xạ toàn phần."),
    make_tf(2, "Thông hiểu", "Về kính lúp và sự quan sát qua kính lúp:", [
        ("a", "Kính lúp là thấu kính hội tụ có tiêu cự ngắn.", True),
        ("b", "Khi quan sát qua kính lúp, phải đặt vật trong khoảng tiêu cự của kính.", True),
        ("c", "Ảnh quan sát được qua kính lúp là ảnh thật ngược chiều.", False),
        ("d", "Kính lúp có tiêu cự càng ngắn thì số bội giác càng lớn.", True)
    ], "Ảnh qua kính lúp là ảnh ảo, cùng chiều, lớn hơn vật."),
    make_tf(3, "Vận dụng", "Chiếu tia sáng từ thủy tinh có chiết suất n = 1,5 ra không khí. Góc giới hạn phản xạ toàn phần là igh ≈ 42 độ:", [
        ("a", "Nếu góc tới i = 35 độ thì có tia khúc xạ đi ra ngoài không khí.", True),
        ("b", "Nếu góc tới i = 42 độ thì tia khúc xạ đi là là sát mặt phân cách.", True),
        ("c", "Nếu góc tới i = 50 độ thì toàn bộ tia sáng bị phản xạ trở lại thủy tinh.", True),
        ("d", "Khi góc tới i = 50 độ thì góc phản xạ bằng 40 độ.", False)
    ], "Định luật phản xạ: i' = i = 50°."),
    make_tf(4, "Vận dụng", "Đặt vật sáng AB cao 2 cm vuông góc trục chính thấu kính hội tụ có f = 12 cm, cách thấu kính d = 24 cm:", [
        ("a", "Vật AB đặt tại vị trí d = 2f.", True),
        ("b", "Ảnh A'B' là ảnh thật ngược chiều hứng được trên màn.", True),
        ("c", "Khoảng cách từ thấu kính đến ảnh là d' = 24 cm.", True),
        ("d", "Chiều cao của ảnh A'B' bằng 4 cm.", False)
    ], "Tại d = 2f, ảnh bằng vật: A'B' = AB = 2 cm.")
]

p3_rev_t1 = [
    make_sa(1, "Thông hiểu", "Chiếu tia sáng vuông góc với mặt phân cách giữa hai môi trường trong suốt. Góc khúc xạ r bằng bao nhiêu độ?", "0", "i = 0° => r = 0°."),
    make_sa(2, "Thông hiểu", "Kính lúp có ghi 10x trên vành kính có tiêu cự f bằng bao nhiêu cm?", "2.5", "f = 25 / 10 = 2,5 cm."),
    make_sa(3, "Vận dụng", "Chiếu tia sáng từ chất lỏng ra không khí với góc tới 50 độ. Biết góc giới hạn phản xạ toàn phần là 45 độ. Góc phản xạ của tia sáng là bao nhiêu độ?", "50", "i = 50° > igh = 45° nên phản xạ toàn phần, góc phản xạ = 50°."),
    make_sa(4, "Vận dụng", "Một thấu kính hội tụ có tiêu cự f = 15 cm. Khoảng cách ngắn nhất giữa một vật thật và ảnh thật của nó qua thấu kính này là bao nhiêu cm?", "60", "L_min = 4f = 4 × 15 = 60 cm."),
    make_sa(5, "Vận dụng cao", "Đặt vật sáng AB cách thấu kính hội tụ d = 30 cm, thấu kính có f = 20 cm. Tính khoảng cách từ ảnh thật A'B' đến thấu kính theo cm?", "60", "1/d' = 1/20 - 1/30 = 1/60 => d' = 60 cm."),
    make_sa(6, "Vận dụng cao", "Một vật sáng nhỏ cao 3 mm đặt cách kính lúp có f = 5 cm một đoạn d = 4 cm. Chiều cao ảnh ảo quan sát được qua kính lúp bằng bao nhiêu mm?", "15", "1/d' = 1/5 - 1/4 = -1/20 => |d'| = 20 cm. k = 20/4 = 5 => Chiều cao ảnh = 3 mm × 5 = 15 mm.")
]

p4_rev_t1 = [
    make_vdc(1, "Một người thợ lặn ở dưới đáy hồ nước trong veo nhìn lên mặt nước thấy hình ảnh của một chú chim đang bay. Do hiện tượng khúc xạ ánh sáng từ không khí vào nước, vị trí con chim mà người thợ lặn nhìn thấy:", [
        "Cao hơn vị trí thực tế của con chim trên bầu trời",
        "Thấp hơn vị trí thực tế của con chim",
        "Đúng vị trí thực tế của con chim",
        "Bị chìm dưới mặt nước"
    ], 0, "Khúc xạ từ không khí vào nước: r < i làm tia sáng bẻ gãy lại gần pháp tuyến, mắt người lặn kéo dài tia khúc xạ sẽ thấy ảnh chim ở vị trí cao hơn thực tế."),
    make_vdc(2, "Để chế tạo một chiếc kính tiềm vọng quang học đơn giản cho người quan sát dưới chiến hào nhìn lên mặt đất, thiết kế tối ưu nhất về độ sắc nét của hình ảnh là:", [
        "Sử dụng hai lăng kính phản xạ toàn phần bằng thủy tinh vuông cân đặt ở hai đầu ống ngắm",
        "Sử dụng hai gương phẳng tráng nhôm thông thường",
        "Sử dụng hai thấu kính phân kì",
        "Sử dụng hai ống sắt rỗng không gắn gương"
    ], 0, "Lăng kính phản xạ toàn phần phản xạ gần 100% ánh sáng, không bị nhòe ảnh đôi do lớp kính mặt trước như gương tráng kim loại."),
    make_vdc(3, "Một mắt cận thị có điểm cực viễn cách mắt 50 cm. Để mắt có thể nhìn rõ các vật ở xa vô cực mà không phải điều tiết, người này phải đeo sát mắt một thấu kính phân kì có tiêu cự bằng:", [
        "f = -50 cm",
        "f = -25 cm",
        "f = +50 cm",
        "f = -100 cm"
    ], 0, "Vật ở vô cực qua kính cận cho ảnh ảo tại điểm cực viễn: d' = -50 cm => f = d' = -50 cm (thấu kính phân kì tiêu cự 50 cm)."),
    make_vdc(4, "Một máy ảnh kỹ thuật số có vật kính là thấu kính hội tụ tiêu cự f = 5 cm. Người chụp ảnh muốn chụp toàn thân một người cao 1,6 m sao cho ảnh trên cảm biến cao 2 cm. Khoảng cách từ người đó đến máy ảnh là:", [
        "4,05 m",
        "2,05 m",
        "8,05 m",
        "1,65 m"
    ], 0, "k = A'B'/AB = 2/160 = 1/80 => d' = d/80. 1/f = 1/d + 1/d' = 1/d + 80/d = 81/d => d = 81 × f = 81 × 5 cm = 405 cm = 4,05 m.")
]

exams["phys9_c6_rev_test1"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 1, p1_rev_t1, p2_rev_t1, p3_rev_t1, p4_rev_t1)

# =============================================================================
# phys9_c6_rev_test2
# =============================================================================
p1_rev_t2 = [
    make_mc(1, "Nhận biết", "Pháp tuyến tại điểm tới là đường thẳng có tính chất:", [
        "Vuông góc với mặt phân cách tại điểm tới",
        "Song song với mặt phân cách",
        "Nằm nghiêng một góc 45 độ so với mặt phân cách",
        "Trùng khít với tia tới"
    ], 0, "Pháp tuyến vuông góc với mặt phân cách tại điểm tới."),
    make_mc(2, "Nhận biết", "Góc giới hạn phản xạ toàn phần igh được tính theo công thức nào khi ánh sáng truyền từ môi trường n sang không khí?", [
        "sin igh = 1 / n",
        "cos igh = 1 / n",
        "tan igh = n",
        "sin igh = n"
    ], 0, "sin igh = 1/n."),
    make_mc(3, "Nhận biết", "Thấu kính phân kì có đặc điểm hình học nhận biết là:", [
        "Phần rìa dày hơn phần giữa",
        "Phần rìa mỏng hơn phần giữa",
        "Có một mặt cầu lồi cả hai bên",
        "Hoàn toàn bằng phẳng như tấm kính cửa sổ"
    ], 0, "Thấu kính phân kì có phần rìa dày hơn phần giữa."),
    make_mc(4, "Nhận biết", "Tia tới đi qua quang tâm O của thấu kính hội tụ sẽ:", [
        "Tiếp tục truyền thẳng không đổi hướng",
        "Đi qua tiêu điểm F'",
        "Bị gãy khúc vuông góc",
        "Song song với trục chính"
    ], 0, "Tia qua quang tâm O luôn truyền thẳng."),
    make_mc(5, "Nhận biết", "Khi quan sát vật qua kính lúp, ảnh ảo thu được luôn có đặc điểm:", [
        "Cùng chiều và lớn hơn vật",
        "Ngược chiều và nhỏ hơn vật",
        "Ngược chiều và lớn hơn vật",
        "Cùng chiều và nhỏ hơn vật"
    ], 0, "Kính lúp cho ảnh ảo, cùng chiều, lớn hơn vật."),
    make_mc(6, "Nhận biết", "Đơn vị đo tiêu cự của thấu kính trong hệ đo lường quốc tế SI là:", [
        "Mét (m)",
        "Giây (s)",
        "Ampe (A)",
        "Jun (J)"
    ], 0, "Đơn vị đo độ dài chuẩn SI là mét (m)."),
    make_mc(7, "Thông hiểu", "Chiếu tia sáng từ không khí vào khối thủy tinh với góc tới i = 45 độ. Góc khúc xạ r có thể nhận giá trị nào sau đây?", [
        "28 độ",
        "45 độ",
        "60 độ",
        "90 độ"
    ], 0, "Không khí vào thủy tinh chiết quang hơn nên r < i = 45°, chỉ có 28° thỏa mãn."),
    make_mc(8, "Thông hiểu", "Sợi quang học dẫn ánh sáng theo các đường uốn lượn mà không bị thất thoát là nhờ:", [
        "Ánh sáng liên tục phản xạ toàn phần ở mặt phân cách giữa lõi và vỏ",
        "Vỏ sợi quang hút ánh sáng",
        "Tia laser tự uốn cong",
        "Sợi quang làm bằng kim loại dẻo"
    ], 0, "Phản xạ toàn phần giữ chùm sáng bên trong lõi."),
    make_mc(9, "Thông hiểu", "Đặt vật thật vuông góc với trục chính của thấu kính hội tụ ở vị trí f < d < 2f. Ảnh thu được trên màn có đặc điểm:", [
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Ảnh thật, ngược chiều và nhỏ hơn vật",
        "Ảnh ảo, cùng chiều và lớn hơn vật",
        "Ảnh ảo, ngược chiều và bằng vật"
    ], 0, "f < d < 2f cho ảnh thật, ngược chiều, lớn hơn vật."),
    make_mc(10, "Thông hiểu", "Một vật sáng đặt cách thấu kính phân kì d = 15 cm (tiêu cự f = 15 cm). Ảnh của vật nằm cách thấu kính bao nhiêu cm?", [
        "7,5 cm",
        "15 cm",
        "30 cm",
        "Vô cực"
    ], 0, "1/-f = 1/d + 1/d' => 1/-15 = 1/15 + 1/d' => 1/d' = -2/15 => |d'| = 7,5 cm."),
    make_mc(11, "Thông hiểu", "Kính lúp có tiêu cự f = 2,5 cm thì có số bội giác bằng:", [
        "10x",
        "5x",
        "2,5x",
        "25x"
    ], 0, "G = 25 / 2,5 = 10x."),
    make_mc(12, "Thông hiểu", "Trong bài thực hành đo tiêu cự, khi đo được d = 30 cm và d' = 30 cm thì tiêu cự f của thấu kính bằng:", [
        "15 cm",
        "30 cm",
        "60 cm",
        "7,5 cm"
    ], 0, "d = 2f = 30 cm => f = 15 cm.")
]

p2_rev_t2 = [
    make_tf(1, "Thông hiểu", "Về hiện tượng khúc xạ và phản xạ ánh sáng:", [
        ("a", "Tia khúc xạ và tia tới luôn nằm cùng một phía so với đường pháp tuyến.", False),
        ("b", "Khi tia sáng truyền vuông góc với mặt nước thì góc tới bằng 0 độ và góc khúc xạ bằng 0 độ.", True),
        ("c", "Góc phản xạ luôn luôn bằng góc tới.", True),
        ("d", "Hiện tượng phản xạ toàn phần xảy ra khi góc tới nhỏ hơn góc giới hạn.", False)
    ], "Tia khúc xạ và tia tới nằm ở hai phía đối diện so với pháp tuyến; phản xạ toàn phần cần i ≥ igh."),
    make_tf(2, "Thông hiểu", "Về thấu kính và đặc điểm tạo ảnh:", [
        ("a", "Thấu kính hội tụ có thể tạo ra cả ảnh thật và ảnh ảo tùy thuộc vào vị trí đặt vật.", True),
        ("b", "Thấu kính phân kì chỉ có thể tạo ra ảnh ảo đối với vật sáng thật.", True),
        ("c", "Ảnh thật tạo bởi thấu kính hội tụ luôn luôn cùng chiều với vật.", False),
        ("d", "Ảnh ảo tạo bởi thấu kính phân kì luôn có kích thước nhỏ hơn vật.", True)
    ], "Ảnh thật luôn ngược chiều với vật thật."),
    make_tf(3, "Vận dụng", "Một khối thủy tinh có chiết suất n = √2 (xấp xỉ 1,414). Ánh sáng truyền từ thủy tinh này ra không khí:", [
        ("a", "Góc giới hạn phản xạ toàn phần là igh = 45 độ.", True),
        ("b", "Nếu góc tới i = 30 độ thì góc khúc xạ r = 45 độ.", True),
        ("c", "Nếu góc tới i = 60 độ thì toàn bộ tia sáng bị phản xạ trở lại với góc 60 độ.", True),
        ("d", "Nếu góc tới i = 45 độ thì không còn tia sáng nào đi sát mặt phân cách.", False)
    ], "Tại i = 45° = igh thì tia khúc xạ đi là là sát mặt phân cách (r = 90°)."),
    make_tf(4, "Vận dụng", "Đặt vật sáng AB cao 3 cm vuông góc trục chính thấu kính hội tụ có f = 20 cm, cách thấu kính d = 60 cm:", [
        ("a", "Khoảng cách từ thấu kính đến ảnh thật là d' = 30 cm.", True),
        ("b", "Ảnh thu được trên màn là ảnh thật ngược chiều với vật.", True),
        ("c", "Độ phóng đại của ảnh là k = 0,5.", True),
        ("d", "Chiều cao của ảnh A'B' là 6 cm.", False)
    ], "A'B' = k × AB = 0,5 × 3 = 1,5 cm (không phải 6 cm).")
]

p3_rev_t2 = [
    make_sa(1, "Thông hiểu", "Góc tới là góc hợp bởi tia tới và đường nào?", "Pháp tuyến", "Góc tới hợp bởi tia tới và đường pháp tuyến tại điểm tới."),
    make_sa(2, "Thông hiểu", "Một kính lúp có ghi 2,5x trên vành kính có tiêu cự f bằng bao nhiêu cm?", "10", "f = 25 / 2,5 = 10 cm."),
    make_sa(3, "Vận dụng", "Chiếu tia sáng từ nước (igh = 48,5 độ) ra không khí với góc tới 60 độ. Tia sáng có bị phản xạ toàn phần không? (Trả lời: Có hoặc Không)", "Có", "i = 60° > igh = 48,5° nên có phản xạ toàn phần."),
    make_sa(4, "Vận dụng", "Một thấu kính hội tụ có f = 18 cm. Để thu được ảnh thật bằng vật thì vật phải đặt cách thấu kính bao nhiêu cm?", "36", "d = 2f = 2 × 18 = 36 cm."),
    make_sa(5, "Vận dụng cao", "Đặt vật sáng AB cách thấu kính hội tụ d = 15 cm. Tiêu cự thấu kính là f = 10 cm. Tính khoảng cách từ thấu kính đến ảnh thật theo cm?", "30", "1/d' = 1/10 - 1/15 = 1/30 => d' = 30 cm."),
    make_sa(6, "Vận dụng cao", "Một vật sáng nhỏ cao 2 mm đặt cách kính lúp có f = 8 cm một khoảng d = 6 cm. Chiều cao của ảnh ảo quan sát được là bao nhiêu mm?", "8", "1/d' = 1/8 - 1/6 = -1/24 => |d'| = 24 cm. k = 24/6 = 4 => Chiều cao ảnh = 2 mm × 4 = 8 mm.")
]

p4_rev_t2 = [
    make_vdc(1, "Một người làm thí nghiệm đặt một đồng xu dưới đáy chậu nước sâu 40 cm. Người đó nhìn thẳng góc từ trên mặt nước xuống thấy ảnh của đồng xu dường như cách mặt nước bao nhiêu cm? (Biết chiết suất của nước là 4/3)", [
        "30 cm",
        "40 cm",
        "53,3 cm",
        "20 cm"
    ], 0, "h' = h / n = 40 / (4/3) = 30 cm."),
    make_vdc(2, "Nguyên nhân hiện tượng ảo ảnh trên mặt đường nhựa trưa hè nắng nóng là do:", [
        "Lớp không khí sát mặt đường bị hun nóng rất mạnh nên có khối lượng riêng và chiết suất nhỏ hơn lớp không khí bên trên, gây phản xạ toàn phần ánh sáng bầu trời vào mắt người",
        "Mặt đường nhựa tự tiết ra chất lỏng phản chiếu",
        "Mặt trời phát ra tia laser vào buổi trưa",
        "Mắt người bị mờ do ánh nắng gắt"
    ], 0, "Không khí sát mặt đường nóng loãng hơn có n nhỏ, ánh sáng từ trên truyền xuống bị phản xạ toàn phần ngược lên mắt."),
    make_vdc(3, "Một mắt cận có khoảng nhìn rõ từ 15 cm đến 50 cm. Để người này có thể đọc sách ở khoảng cách bình thường 25 cm mà không cần điều tiết kính, kính cận cần đeo có tiêu cự là:", [
        "-50 cm",
        "-25 cm",
        "-15 cm",
        "+25 cm"
    ], 0, "Kính cận chữa tật cận thị có f = -OCv = -50 cm."),
    make_vdc(4, "Một máy chiếu phim phóng đại một bức ảnh trên tấm phim kích thước 2 cm × 3 cm thành một bức tranh trên màn chiếu có kích thước 1,2 m × 1,8 m. Độ phóng đại của hình ảnh trên màn là:", [
        "60 lần",
        "30 lần",
        "120 lần",
        "10 lần"
    ], 0, "k = 1,2 m / 2 cm = 120 cm / 2 cm = 60 lần.")
]

exams["phys9_c6_rev_test2"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 2, p1_rev_t2, p2_rev_t2, p3_rev_t2, p4_rev_t2)

# =============================================================================
# phys9_c6_rev_test3
# =============================================================================
p1_rev_t3 = [
    make_mc(1, "Nhận biết", "Mặt phẳng tới là mặt phẳng được tạo bởi:", [
        "Tia tới và đường pháp tuyến tại điểm tới",
        "Tia tới và mặt phân cách",
        "Tia khúc xạ và mặt phân cách",
        "Tia phản xạ và trục chính"
    ], 0, "Mặt phẳng tới chứa tia tới và pháp tuyến tại điểm tới."),
    make_mc(2, "Nhận biết", "Hiện tượng phản xạ toàn phần xảy ra khi toàn bộ ánh sáng chiếu tới bị:", [
        "Phản xạ hoàn toàn trở lại môi trường trong suốt ban đầu",
        "Khúc xạ sang môi trường thứ hai",
        "Hấp thụ thành nhiệt năng",
        "Biến đổi thành ánh sáng màu tím"
    ], 0, "Toàn bộ tia sáng bị phản xạ trở lại môi trường ban đầu."),
    make_mc(3, "Nhận biết", "Kí hiệu quy ước của thấu kính hội tụ trên sơ đồ quang học là:", [
        "Đoạn thẳng có hai đầu mũi tên hướng ra ngoài",
        "Đoạn thẳng có hai đầu mũi tên hướng vào trong",
        "Đường cong hình parabol",
        "Hình chữ nhật kẻ sọc"
    ], 0, "TKHT có mũi tên hướng ra ngoài ở hai đầu."),
    make_mc(4, "Nhận biết", "Tia tới song song với trục chính của thấu kính phân kì cho tia ló có đặc điểm:", [
        "Bị loe rộng ra xa với đường kéo dài đi qua tiêu điểm chính F",
        "Hội tụ tại tiêu điểm chính F'",
        "Truyền thẳng không đổi phương",
        "Vuông góc với trục chính"
    ], 0, "Đường kéo dài của tia ló đi qua tiêu điểm F nằm cùng phía với tia tới."),
    make_mc(5, "Nhận biết", "Tiêu cự f của kính lúp có mối liên hệ như thế nào với số bội giác G?", [
        "Tỉ lệ nghịch với số bội giác (f = 25 / G)",
        "Tỉ lệ thuận với số bội giác (f = 25 × G)",
        "Không có mối liên hệ nào",
        "Luôn luôn bằng số bội giác"
    ], 0, "f = 25 / G."),
    make_mc(6, "Nhận biết", "Để xác định nhanh tiêu cự của thấu kính hội tụ dưới ánh nắng mặt trời, ta đo:", [
        "Khoảng cách từ thấu kính đến điểm sáng hội tụ nhỏ nhất trên tờ giấy hứng",
        "Đường kính của thấu kính",
        "Bề dày mép ngoài của thấu kính",
        "Chiều dài cán cầm thấu kính"
    ], 0, "Ánh sáng mặt trời là chùm song song nên hội tụ tại tiêu điểm F', đo khoảng cách từ thấu kính đến điểm sáng nhỏ nhất."),
    make_mc(7, "Thông hiểu", "Chiếu tia sáng từ một khối nhựa trong suốt ra không khí với góc tới i = 25 độ, đo được góc khúc xạ r = 40 độ. Góc lệch giữa phương truyền ban đầu và tia khúc xạ là:", [
        "15 độ",
        "65 độ",
        "25 độ",
        "40 độ"
    ], 0, "D = r - i = 40° - 25° = 15°."),
    make_mc(8, "Thông hiểu", "Kim cương có độ lấp lánh rực rỡ vượt trội so với các loại thủy tinh thông thường vì:", [
        "Kim cương có chiết suất rất lớn dẫn tới góc giới hạn phản xạ toàn phần rất nhỏ",
        "Kim cương tự phát quang hạt nhân",
        "Kim cương là kim loại dẫn điện",
        "Kim cương có bề mặt mềm dễ uốn"
    ], 0, "n kim cương ≈ 2,42 nên igh ≈ 24,5° rất nhỏ, ánh sáng vào trong phản xạ toàn phần nhiều lần trước khi ló ra."),
    make_mc(9, "Thông hiểu", "Đặt vật thật trước thấu kính hội tụ ở khoảng cách d = 2f thì thu được ảnh có đặc điểm:", [
        "Ảnh thật, ngược chiều và có kích thước bằng đúng vật",
        "Ảnh ảo, cùng chiều và lớn hơn vật",
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Ảnh ảo, ngược chiều và nhỏ hơn vật"
    ], 0, "d = 2f cho ảnh thật, ngược chiều và bằng vật."),
    make_mc(10, "Thông hiểu", "Khi quan sát một dòng chữ nhỏ qua thấu kính phân kì, ta thấy hình ảnh chữ viết luôn:", [
        "Cùng chiều và nhỏ hơn chữ viết thật",
        "Ngược chiều và lớn hơn chữ viết thật",
        "Cùng chiều và lớn hơn chữ viết thật",
        "Bị lộn ngược đầu xuống dưới"
    ], 0, "TKPK luôn cho ảnh ảo cùng chiều nhỏ hơn vật."),
    make_mc(11, "Thông hiểu", "Một kính lúp có ghi kí hiệu 4x trên vành kính có tiêu cự bằng:", [
        "6,25 cm",
        "4 cm",
        "100 cm",
        "10 cm"
    ], 0, "f = 25 / 4 = 6,25 cm."),
    make_mc(12, "Thông hiểu", "Một vật sáng đặt cách thấu kính hội tụ d = 40 cm cho ảnh thật rõ nét trên màn cách thấu kính d' = 40 cm. Tiêu cự của thấu kính là:", [
        "20 cm",
        "40 cm",
        "80 cm",
        "10 cm"
    ], 0, "d = d' = 2f = 40 cm => f = 20 cm.")
]

p2_rev_t3 = [
    make_tf(1, "Thông hiểu", "Xét các tính chất của thấu kính mỏng:", [
        ("a", "Mỗi thấu kính mỏng có hai tiêu điểm chính nằm đối xứng nhau qua quang tâm O.", True),
        ("b", "Quang tâm O là điểm mà mọi tia sáng đi qua đều bị bẻ cong 90 độ.", False),
        ("c", "Tiêu cự f là khoảng cách từ quang tâm O đến tiêu điểm chính.", True),
        ("d", "Trục chính của thấu kính vuông góc với mặt thấu kính tại quang tâm.", True)
    ], "Mọi tia sáng đi qua quang tâm O đều tiếp tục truyền thẳng."),
    make_tf(2, "Thông hiểu", "Về hiện tượng phản xạ toàn phần và ứng dụng:", [
        ("a", "Phản xạ toàn phần chỉ xảy ra khi truyền từ môi trường chiết quang hơn sang kém hơn.", True),
        ("b", "Lăng kính phản xạ toàn phần có thể làm đổi hướng tia sáng 90 độ hoặc 180 độ.", True),
        ("c", "Cáp quang viễn thông truyền tín hiệu bằng sóng siêu âm.", False),
        ("d", "Ống nội soi y học sử dụng bó sợi quang mềm dẫn sáng bằng phản xạ toàn phần.", True)
    ], "Cáp quang truyền tín hiệu dưới dạng các xung ánh sáng (photon)."),
    make_tf(3, "Vận dụng", "Đặt vật sáng AB cao 4 cm vuông góc trục chính thấu kính hội tụ có f = 15 cm, vật cách thấu kính d = 10 cm:", [
        ("a", "Vật nằm trong khoảng tiêu cự của thấu kính (d < f).", True),
        ("b", "Ảnh A'B' là ảnh ảo, cùng chiều và lớn hơn vật.", True),
        ("c", "Khoảng cách từ ảnh ảo đến thấu kính là d' = 30 cm.", True),
        ("d", "Chiều cao của ảnh ảo A'B' là 8 cm.", False)
    ], "1/d' = 1/15 - 1/10 = -1/30 => |d'| = 30 cm. k = 30/10 = 3 => A'B' = 3 × 4 = 12 cm (không phải 8 cm)."),
    make_tf(4, "Vận dụng", "Một thấu kính phân kì có tiêu cự f = 20 cm. Đặt ngọn nến sáng cách thấu kính d = 30 cm:", [
        ("a", "Ảnh của ngọn nến là ảnh ảo cùng chiều với ngọn nến.", True),
        ("b", "Khoảng cách từ ảnh ảo đến thấu kính là d' = 12 cm.", True),
        ("c", "Ảnh thu được có thể hứng rõ nét trên một tấm bìa trắng đặt phía sau thấu kính.", False),
        ("d", "Độ phóng đại của ảnh ảo là k = 0,4.", True)
    ], "1/d' = -1/20 - 1/30 = -5/60 = -1/12 => |d'| = 12 cm. k = 12/30 = 0,4. Ảnh ảo không hứng được trên bìa trắng.")
]

p3_rev_t3 = [
    make_sa(1, "Thông hiểu", "Chiếu tia sáng từ không khí vào nước với góc tới 50 độ, góc khúc xạ là 35 độ. Góc lệch giữa tia tới và tia khúc xạ bằng bao nhiêu độ?", "15", "D = 50° - 35° = 15°."),
    make_sa(2, "Thông hiểu", "Kính lúp có ghi 8x trên vành kính có tiêu cự f bằng bao nhiêu cm? (Lấy số thập phân)", "3.125", "f = 25 / 8 = 3,125 cm."),
    make_sa(3, "Vận dụng", "Chiếu tia sáng từ khối nhựa trong suốt ra không khí với góc tới 45 độ và bị phản xạ toàn phần. Góc phản xạ bằng bao nhiêu độ?", "45", "i' = i = 45°."),
    make_sa(4, "Vận dụng", "Khoảng cách giữa vật thật và màn hứng ảnh đo được là L = 48 cm khi ảnh thật ngược chiều bằng vật. Tiêu cự thấu kính bằng bao nhiêu cm?", "12", "f = L / 4 = 48 / 4 = 12 cm."),
    make_sa(5, "Vận dụng cao", "Đặt vật sáng AB cách thấu kính hội tụ d = 40 cm. Tiêu cự thấu kính là f = 24 cm. Tính khoảng cách từ ảnh thật đến thấu kính theo cm?", "60", "1/d' = 1/24 - 1/40 = 2/120 = 1/60 => d' = 60 cm."),
    make_sa(6, "Vận dụng cao", "Dùng kính lúp có f = 10 cm quan sát mẫu vật nhỏ đặt cách kính d = 8 cm. Độ phóng đại ảnh ảo k bằng bao nhiêu lần?", "5", "1/d' = 1/10 - 1/8 = -1/40 => |d'| = 40 cm. k = 40/8 = 5 lần.")
]

p4_rev_t3 = [
    make_vdc(1, "Một người thợ săn cá đứng trên bờ sông trong vắt nhìn thấy một con cá to đang bơi dưới nước. Người đó cầm một ngọn lao nhọn và muốn phóng trúng con cá. Người thợ săn phải phóng ngọn lao:", [
        "Vào vị trí sâu hơn (thấp hơn) hình ảnh con cá nhìn thấy",
        "Vào vị trí nông hơn (cao hơn) hình ảnh con cá nhìn thấy",
        "Chính xác ngay tại tâm hình ảnh con cá nhìn thấy",
        "Về phía bên trái con cá 2 mét"
    ], 0, "Do khúc xạ ánh sáng từ nước ra không khí, ảnh con cá bị nâng lên gần mặt nước hơn vị trí thật. Phải phóng sâu hơn ảnh để trúng cá."),
    make_vdc(2, "Một lăng kính phản xạ toàn phần bằng thủy tinh vuông cân được dùng trong ống nhòm để quay ngược hình ảnh. Khi tia sáng chiếu vuông góc vào mặt bên thứ nhất thì góc tới tại mặt huyền của lăng kính bằng:", [
        "45 độ",
        "30 độ",
        "60 độ",
        "90 độ"
    ], 0, "Mặt huyền nghiêng 45° so với mặt bên, pháp tuyến hợp góc 45° nên góc tới tại mặt huyền là 45°."),
    make_vdc(3, "Mắt của một người già nhìn rõ các vật ở xa nhưng không nhìn rõ các vật ở gần hơn 50 cm (mắt lão). Để người này có thể đọc sách ở cự ly chuẩn 25 cm, người đó phải đeo kính lão là loại thấu kính nào?", [
        "Thấu kính hội tụ có tiêu cự f = 50 cm",
        "Thấu kính phân kì có tiêu cự f = 50 cm",
        "Thấu kính hội tụ có tiêu cự f = 25 cm",
        "Thấu kính phân kì có tiêu cự f = 25 cm"
    ], 0, "Vật tại d = 25 cm cho ảnh ảo tại điểm cực cận d' = -50 cm: 1/f = 1/25 - 1/50 = 1/50 => f = 50 cm (thấu kính hội tụ)."),
    make_vdc(4, "Một kính hiển vi quang học có vật kính là thấu kính hội tụ tiêu cự f1 = 1 cm và thị kính là thấu kính hội tụ tiêu cự f2 = 5 cm. Vật kính tạo ra ảnh thật A1B1 của tế bào phóng đại gấp 20 lần vật thật. Thị kính sau đó phóng đại ảnh A1B1 thêm 5 lần nữa. Độ phóng đại tổng cộng của kính hiển vi đối với tế bào này là:", [
        "100 lần",
        "25 lần",
        "15 lần",
        "200 lần"
    ], 0, "Độ phóng đại tổng cộng K = k1 × k2 = 20 × 5 = 100 lần.")
]

exams["phys9_c6_rev_test3"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 3, p1_rev_t3, p2_rev_t3, p3_rev_t3, p4_rev_t3)

# =============================================================================
# phys9_c6_rev_test4
# =============================================================================
p1_rev_t4 = [
    make_mc(1, "Nhận biết", "Trong hiện tượng khúc xạ, góc tới i và góc khúc xạ r cùng nằm trong:", [
        "Mặt phẳng tới",
        "Mặt phẳng phân cách",
        "Mặt phẳng nằm ngang",
        "Mặt phẳng vuông góc trục chính"
    ], 0, "Tia tới, pháp tuyến và tia khúc xạ cùng nằm trong mặt phẳng tới."),
    make_mc(2, "Nhận biết", "Hiện tượng phản xạ toàn phần xảy ra khi góc tới i thỏa mãn điều kiện:", [
        "i >= igh (với ánh sáng truyền từ môi trường chiết quang hơn sang kém hơn)",
        "i < igh",
        "i = 0 độ",
        "i luôn bằng 45 độ"
    ], 0, "Điều kiện về góc là i ≥ igh."),
    make_mc(3, "Nhận biết", "Trục chính của thấu kính là đường thẳng:", [
        "Vuông góc với mặt thấu kính tại quang tâm O",
        "Song song với mặt phẳng thấu kính",
        "Nối hai mép ngoài của thấu kính",
        "Bất kì đi qua rìa thấu kính"
    ], 0, "Trục chính vuông góc với mặt thấu kính tại quang tâm O."),
    make_mc(4, "Nhận biết", "Tia tới đi qua tiêu điểm chính F của thấu kính hội tụ cho tia ló có đặc điểm:", [
        "Song song với trục chính của thấu kính",
        "Đi thẳng qua quang tâm O",
        "Vuông góc với trục chính",
        "Cắt trục chính tại F"
    ], 0, "Tia tới qua tiêu điểm F cho tia ló song song với trục chính."),
    make_mc(5, "Nhận biết", "Để nhìn thấy các chi tiết siêu nhỏ trên vi mạch điện tử, kỹ thuật viên dùng dụng cụ nào?", [
        "Kính lúp hoặc kính hiển vi quang học",
        "Gương cầu lồi xe máy",
        "Thước dây cuộn",
        "Kính râm thời trang"
    ], 0, "Kính lúp và kính hiển vi dùng quan sát các chi tiết vi mô."),
    make_mc(6, "Nhận biết", "Phương pháp Silbermann xác định tiêu cự dựa trên vị trí tạo ảnh thật có đặc điểm:", [
        "Ảnh thật ngược chiều và có kích thước bằng đúng vật (d = d' = 2f)",
        "Ảnh thật gấp mười lần vật",
        "Ảnh ảo cùng chiều",
        "Ảnh ở vô cực"
    ], 0, "Phương pháp Silbermann dựa trên d = d' = 2f, ảnh bằng vật."),
    make_mc(7, "Thông hiểu", "Một chiếc thìa cắm nghiêng trong cốc nước trong suốt trông như bị uốn gãy tại mặt nước. Hiện tượng này chứng minh:", [
        "Ánh sáng bị khúc xạ khi truyền từ nước sang không khí",
        "Chiếc thìa thực sự bị gãy do áp suất nước",
        "Nước làm tan chảy chiếc thìa",
        "Ánh sáng bị phản xạ toàn phần ở đáy cốc"
    ], 0, "Khúc xạ ánh sáng từ nước ra không khí làm ảnh của thìa bị gãy tại mặt thoáng."),
    make_mc(8, "Thông hiểu", "Trong một sợi cáp quang, điều kiện về chiết suất của lớp lõi (n1) và lớp vỏ (n2) là:", [
        "n1 > n2 (chiết suất lõi lớn hơn vỏ)",
        "n1 < n2",
        "n1 = n2",
        "n1 = 0"
    ], 0, "n1 > n2 để thỏa mãn điều kiện phản xạ toàn phần trong lõi."),
    make_mc(9, "Thông hiểu", "Đặt vật thật vuông góc với trục chính của thấu kính hội tụ ở vị trí d = f. Chùm tia ló ra khỏi thấu kính có đặc điểm:", [
        "Là chùm tia song song với nhau (ảnh ở vô cực)",
        "Hội tụ tại một điểm cách thấu kính 2f",
        "Phân kì loe rộng cắt nhau tại O",
        "Phản xạ trở lại vật"
    ], 0, "Vật tại F thì chùm tia ló song song, ảnh ở vô cực."),
    make_mc(10, "Thông hiểu", "Một người cận thị nhìn vật ở xa thấy mờ vì ảnh của vật hội tụ ở đâu so với màng lưới của mắt?", [
        "Hội tụ ở phía trước màng lưới",
        "Hội tụ ở phía sau màng lưới",
        "Hội tụ đúng trên màng lưới",
        "Hội tụ tại điểm vàng"
    ], 0, "Mắt cận thị có thủy tinh thể quá phồng làm tiêu cự ngắn, ảnh của vật ở xa hội tụ trước màng lưới."),
    make_mc(11, "Thông hiểu", "Kính lúp có số bội giác G = 2x thì có tiêu cự bằng:", [
        "12,5 cm",
        "25 cm",
        "50 cm",
        "2 cm"
    ], 0, "f = 25 / 2 = 12,5 cm."),
    make_mc(12, "Thông hiểu", "Khoảng cách ngắn nhất giữa một vật thật và ảnh thật của nó qua một thấu kính hội tụ có tiêu cự f = 10 cm là:", [
        "40 cm",
        "20 cm",
        "10 cm",
        "5 cm"
    ], 0, "L_min = 4f = 4 × 10 = 40 cm.")
]

p2_rev_t4 = [
    make_tf(1, "Thông hiểu", "Về định luật khúc xạ ánh sáng:", [
        ("a", "Tia khúc xạ luôn nằm trong mặt phẳng tới.", True),
        ("b", "Khi góc tới tăng dần thì góc khúc xạ cũng tăng dần theo.", True),
        ("c", "Góc khúc xạ r luôn nhỏ hơn góc tới i trong mọi môi trường.", False),
        ("d", "Tia sáng truyền vuông góc với mặt phân cách thì truyền thẳng.", True)
    ], "Khi truyền từ môi trường chiết quang hơn sang kém hơn thì r > i."),
    make_tf(2, "Thông hiểu", "Về cấu tạo và ứng dụng của thấu kính:", [
        ("a", "Thấu kính hội tụ có phần giữa dày hơn phần rìa.", True),
        ("b", "Thấu kính phân kì có phần rìa dày hơn phần giữa.", True),
        ("c", "Kính cận thị là thấu kính hội tụ.", False),
        ("d", "Kính lúp đọc sách là thấu kính hội tụ có tiêu cự ngắn.", True)
    ], "Kính cận thị là thấu kính phân kì."),
    make_tf(3, "Vận dụng", "Chiếu tia sáng từ chất lỏng ra không khí với góc tới i = 30 độ, góc khúc xạ r = 45 độ:", [
        ("a", "Chất lỏng này chiết quang hơn không khí.", True),
        ("b", "Góc lệch giữa tia tới và tia khúc xạ là 15 độ.", True),
        ("c", "Góc giới hạn phản xạ toàn phần của chất lỏng này là igh = 45 độ.", True),
        ("d", "Nếu tăng góc tới lên 50 độ thì tia khúc xạ đi ra ngoài không khí với góc 80 độ.", False)
    ], "Khi i = 50° > igh = 45° thì xảy ra phản xạ toàn phần, không còn tia khúc xạ ra không khí."),
    make_tf(4, "Vận dụng", "Đặt vật sáng AB cao 2 cm vuông góc trục chính thấu kính hội tụ có f = 10 cm, vật cách thấu kính d = 30 cm:", [
        ("a", "Khoảng cách từ thấu kính đến ảnh thật là d' = 15 cm.", True),
        ("b", "Ảnh thu được trên màn nhỏ hơn vật sáng AB.", True),
        ("c", "Chiều cao của ảnh thật A'B' là 1 cm.", True),
        ("d", "Nếu dời vật ra xa thấu kính hơn nữa thì ảnh thật dịch chuyển ra xa thấu kính hơn.", False)
    ], "1/d' = 1/10 - 1/30 = 2/30 = 1/15 => d' = 15 cm. k = 15/30 = 0,5 => A'B' = 1 cm. Khi d tăng thì d' giảm (tiến về f).")
]

p3_rev_t4 = [
    make_sa(1, "Thông hiểu", "Chiếu tia sáng từ không khí vào thủy tinh với góc tới 60 độ, góc khúc xạ là 35 độ. Góc lệch của tia sáng là bao nhiêu độ?", "25", "D = 60° - 35° = 25°."),
    make_sa(2, "Thông hiểu", "Một kính lúp có tiêu cự f = 20 cm. Số bội giác G của kính lúp này bằng bao nhiêu? (Lấy số thập phân)", "1.25", "G = 25 / 20 = 1,25x."),
    make_sa(3, "Vận dụng", "Một tia sáng truyền từ nước ra không khí với góc tới 55 độ. Biết góc giới hạn là 48,5 độ. Góc phản xạ của tia sáng là bao nhiêu độ?", "55", "Xảy ra phản xạ toàn phần nên góc phản xạ = 55°."),
    make_sa(4, "Vận dụng", "Một thấu kính hội tụ có f = 25 cm. Khoảng cách ngắn nhất giữa vật thật và ảnh thật của nó qua thấu kính bằng bao nhiêu cm?", "100", "L_min = 4f = 4 × 25 = 100 cm."),
    make_sa(5, "Vận dụng cao", "Đặt vật sáng AB cách thấu kính hội tụ d = 50 cm. Thấu kính có f = 20 cm. Tính khoảng cách từ ảnh thật đến thấu kính theo cm? (Lấy số thập phân)", "33.3", "1/d' = 1/20 - 1/50 = 3/100 => d' = 100/3 ≈ 33,3 cm."),
    make_sa(6, "Vận dụng cao", "Một vật nhỏ cao 1 mm đặt cách kính lúp có f = 5 cm một khoảng d = 4,5 cm. Chiều cao của ảnh ảo quan sát được qua kính lúp bằng bao nhiêu mm?", "10", "1/d' = 1/5 - 1/4,5 = -0,5/22,5 = -1/45 => |d'| = 45 cm. k = 45 / 4,5 = 10 => Chiều cao ảnh = 1 mm × 10 = 10 mm.")
]

p4_rev_t4 = [
    make_vdc(1, "Một người thợ kim hoàn quan sát một viên kim cương tự nhiên dưới ánh sáng đèn bàn. Nhờ hiện tượng phản xạ toàn phần liên tiếp bên trong các giác cắt góc nghiêng chính xác, viên kim cương phát ra các tia sáng lấp lánh rực rỡ. Nếu viên kim cương bị nhúng chìm hoàn toàn trong một cốc chất lỏng trong suốt có chiết suất rất gần với chiết suất của kim cương thì:", [
        "Độ lấp lánh của viên kim cương bị giảm đi rất nhiều và viên kim cương trông như gần như tàng hình trong chất lỏng",
        "Kim cương phát sáng rực rỡ hơn gấp trăm lần",
        "Kim cương bị hòa tan ngay lập tức",
        "Kim cương biến đổi thành than chì"
    ], 0, "Khi chiết suất môi trường ngoài gần bằng kim cương, góc giới hạn tăng lên rất lớn làm giảm phản xạ toàn phần, ánh sáng đi thẳng qua khiến kim cương mất lấp lánh và mờ nhạt."),
    make_vdc(2, "Trong hệ thống thông tin cáp quang, người ta sử dụng chùm tia laser phát xung ánh sáng đơn sắc thay cho ánh sáng trắng thông thường. Ưu điểm quyết định của việc dùng ánh sáng laser đơn sắc là:", [
        "Tránh được hiện tượng tán sắc ánh sáng (sắc sai) làm các xung ánh sáng bị nhòe và giãn rộng theo thời gian truyền dẫn",
        "Laser không mang năng lượng nên không tốn điện",
        "Laser có thể truyền qua dây đồng",
        "Laser biến thành âm thanh trực tiếp"
    ], 0, "Ánh sáng đơn sắc có một bước sóng duy nhất nên truyền cùng vận tốc trong sợi quang, tránh hiện tượng tán sắc làm biến dạng xung tín hiệu số."),
    make_vdc(3, "Một mắt cận thị chỉ nhìn rõ các vật trong khoảng từ 10 cm đến 40 cm. Khi đeo kính cận phù hợp (f = -40 cm) để nhìn rõ vật ở vô cực thì điểm nhìn rõ gần nhất mới của người này cách mắt bao nhiêu cm?", [
        "13,3 cm",
        "10 cm",
        "25 cm",
        "40 cm"
    ], 0, "Vật tại d_mới cho ảnh ảo tại điểm cực cận cũ d' = -10 cm qua kính có f = -40 cm: 1/f = 1/d + 1/d' => -1/40 = 1/d - 1/10 => 1/d = 1/10 - 1/40 = 3/40 => d = 40/3 ≈ 13,3 cm."),
    make_vdc(4, "Một người làm thí nghiệm đo tiêu cự bằng phương pháp Bessel: Khoảng cách vật - màn cố định L = 80 cm. Có hai vị trí của thấu kính cho ảnh rõ nét cách nhau một đoạn e = 40 cm. Tiêu cự của thấu kính hội tụ này là:", [
        "15 cm",
        "20 cm",
        "10 cm",
        "25 cm"
    ], 0, "f = (L^2 - e^2) / (4L) = (80^2 - 40^2) / (4 × 80) = (6400 - 1600) / 320 = 4800 / 320 = 15 cm.")
]

exams["phys9_c6_rev_test4"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 4, p1_rev_t4, p2_rev_t4, p3_rev_t4, p4_rev_t4)

# =============================================================================
# phys9_c6_rev_test5
# =============================================================================
p1_rev_t5 = [
    make_mc(1, "Nhận biết", "Hiện tượng gãy khúc của tia sáng khi truyền xiên góc qua mặt phân cách giữa hai môi trường trong suốt được gọi là:", [
        "Hiện tượng khúc xạ ánh sáng",
        "Hiện tượng phản xạ ánh sáng",
        "Hiện tượng hấp thụ ánh sáng",
        "Hiện tượng giao thoa ánh sáng"
    ], 0, "Định nghĩa hiện tượng khúc xạ ánh sáng."),
    make_mc(2, "Nhận biết", "Góc giới hạn phản xạ toàn phần từ nước ra không khí có giá trị xấp xỉ khoảng:", [
        "48,5 độ",
        "42 độ",
        "24,5 độ",
        "90 độ"
    ], 0, "Nước ra không khí: sin igh = 1/(4/3) = 0,75 => igh ≈ 48,5°."),
    make_mc(3, "Nhận biết", "Thấu kính hội tụ mỏng biến đổi một chùm tia tới song song thành:", [
        "Chùm tia ló hội tụ",
        "Chùm tia ló phân kì loe rộng",
        "Chùm tia ló song song ngược chiều",
        "Chùm tia vuông góc với nhau"
    ], 0, "Thấu kính hội tụ cho chùm tia ló hội tụ."),
    make_mc(4, "Nhận biết", "Kí hiệu quy ước của thấu kính phân kì trên hình vẽ quang học là:", [
        "Đoạn thẳng có hai đầu mũi tên hướng vào trong (hoặc đuôi mũi tên)",
        "Đoạn thẳng có hai đầu mũi tên hướng ra ngoài",
        "Đường tròn có tâm O",
        "Hình tam giác vuông cân"
    ], 0, "Thấu kính phân kì có đuôi mũi tên hướng vào trong ở hai đầu."),
    make_mc(5, "Nhận biết", "Kính lúp thường có số bội giác nằm trong khoảng thông dụng từ:", [
        "1,5x đến khoảng 40x",
        "1000x đến 10.000x",
        "0,01x đến 0,1x",
        "Vô cùng lớn"
    ], 0, "Kính lúp thông dụng có số bội giác từ khoảng 1,5x đến 40x."),
    make_mc(6, "Nhận biết", "Trong thí nghiệm thực hành đo tiêu cự, khi thu được ảnh thật bằng vật thì khoảng cách từ vật đến thấu kính bằng:", [
        "d = 2f",
        "d = f",
        "d = 4f",
        "d = 0,5f"
    ], 0, "Ảnh thật bằng vật khi d = 2f."),
    make_mc(7, "Thông hiểu", "Chiếu tia sáng từ không khí vào một chất lỏng với góc tới i = 60 độ, góc khúc xạ r = 35 độ. Góc hợp bởi tia khúc xạ và mặt phân cách giữa hai môi trường là:", [
        "55 độ",
        "35 độ",
        "60 độ",
        "25 độ"
    ], 0, "Góc hợp bởi tia khúc xạ và mặt phân cách là 90° - r = 90° - 35° = 55°."),
    make_mc(8, "Thông hiểu", "Sợi cáp quang y tế dùng trong phẫu thuật nội soi ổ bụng giúp bác sĩ quan sát nội tạng dựa trên hiện tượng:", [
        "Phản xạ toàn phần ánh sáng trong các bó sợi quang mềm",
        "Khúc xạ ánh sáng qua gương phẳng",
        "Bức xạ nhiệt của cơ thể bệnh nhân",
        "Sóng siêu âm biến thành ánh sáng"
    ], 0, "Dây nội soi truyền ánh sáng bằng phản xạ toàn phần."),
    make_mc(9, "Thông hiểu", "Đặt vật thật trước thấu kính hội tụ ở khoảng cách d < f. Ảnh quan sát được có đặc điểm:", [
        "Ảnh ảo, cùng chiều và lớn hơn vật",
        "Ảnh thật, ngược chiều và nhỏ hơn vật",
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Ảnh ảo, cùng chiều và nhỏ hơn vật"
    ], 0, "d < f qua TKHT cho ảnh ảo cùng chiều lớn hơn vật."),
    make_mc(10, "Thông hiểu", "Một người già đọc sách báo phải đưa sách ra xa mắt hơn 25 cm mới đọc được. Người này mắc tật gì và cần đeo kính gì?", [
        "Mắc tật lão thị, cần đeo thấu kính hội tụ",
        "Mắc tật cận thị, cần đeo thấu kính phân kì",
        "Mắc tật loạn thị, cần đeo kính râm",
        "Mắt bình thường không cần đeo kính"
    ], 0, "Mắt lão thị cực cận dời ra xa, cần đeo thấu kính hội tụ hỗ trợ."),
    make_mc(11, "Thông hiểu", "Một kính lúp có tiêu cự f = 5 cm. Số bội giác của kính lúp này là:", [
        "5x",
        "10x",
        "2,5x",
        "25x"
    ], 0, "G = 25 / 5 = 5x."),
    make_mc(12, "Thông hiểu", "Khi dịch chuyển một vật sáng từ rất xa lại gần thấu kính phân kì, ảnh ảo của vật sẽ:", [
        "Di chuyển từ tiêu điểm F lại gần quang tâm O và kích thước lớn dần",
        "Di chuyển ra xa vô cực và nhỏ dần",
        "Biến thành ảnh thật ở khoảng cách 2f",
        "Không thay đổi vị trí"
    ], 0, "Khi d giảm (tiến về 0) qua TKPK, ảnh ảo dời từ F về O và kích thước tăng dần (tiến tới bằng vật).")
]

p2_rev_t5 = [
    make_tf(1, "Thông hiểu", "Về các hiện tượng quang hình học:", [
        ("a", "Hiện tượng khúc xạ ánh sáng tuân theo định luật khúc xạ ánh sáng.", True),
        ("b", "Hiện tượng phản xạ toàn phần có thể xảy ra khi ánh sáng truyền từ kim cương ra không khí.", True),
        ("c", "Tia sáng truyền qua quang tâm của thấu kính luôn bị lệch góc 45 độ.", False),
        ("d", "Vật thật qua thấu kính phân kì luôn cho ảnh ảo nhỏ hơn vật.", True)
    ], "Tia qua quang tâm O luôn truyền thẳng."),
    make_tf(2, "Thông hiểu", "Về các tật quang học của mắt và kính bổ trợ:", [
        ("a", "Mắt cận thị nhìn rõ các vật ở gần nhưng khó nhìn rõ các vật ở xa.", True),
        ("b", "Kính cận là thấu kính phân kì giúp đưa ảnh của vật ở xa về điểm cực viễn của mắt.", True),
        ("c", "Mắt lão thị của người già nhìn rõ các vật ở gần mà không nhìn rõ ở xa.", False),
        ("d", "Kính lão là thấu kính hội tụ giúp hỗ trợ mắt nhìn rõ các vật ở cự ly gần.", True)
    ], "Mắt lão nhìn xa bình thường nhưng nhìn gần bị mờ do cực cận lùi ra xa."),
    make_tf(3, "Vận dụng", "Một khối thủy tinh có góc giới hạn phản xạ toàn phần igh = 42 độ. Chiếu tia sáng từ khối thủy tinh ra không khí:", [
        ("a", "Nếu góc tới i = 30 độ thì có cả tia khúc xạ và tia phản xạ.", True),
        ("b", "Khi góc tới tăng đến đúng bằng góc giới hạn i = 42 độ thì góc khúc xạ đạt giá trị lớn nhất r = 90 độ.", True),
        ("c", "Nếu góc tới i = 60 độ thì toàn bộ tia sáng bị phản xạ toàn phần với góc phản xạ 60 độ.", True),
        ("d", "Nếu góc tới i = 0 độ thì xảy ra phản xạ toàn phần 100%.", False)
    ], "i = 0° là chiếu vuông góc, tia sáng truyền thẳng ra ngoài không khí (r = 0°)."),
    make_tf(4, "Vận dụng", "Đặt vật sáng AB cao 2 cm vuông góc trục chính thấu kính hội tụ có f = 12 cm, cách thấu kính d = 6 cm:", [
        ("a", "Vật đặt trong khoảng tiêu cự của thấu kính (d < f).", True),
        ("b", "Ảnh thu được là ảnh ảo, cùng chiều với vật.", True),
        ("c", "Vị trí của ảnh ảo cách thấu kính một đoạn bằng d' = 12 cm.", True),
        ("d", "Chiều cao của ảnh ảo A'B' là 4 cm.", True)
    ], "1/d' = 1/12 - 1/6 = -1/12 => |d'| = 12 cm. k = 12/6 = 2 => A'B' = 2 × 2 = 4 cm.")
]

p3_rev_t5 = [
    make_sa(1, "Thông hiểu", "Chiếu tia sáng từ không khí vào khối nhựa với góc tới 45 độ, đo được góc khúc xạ là 30 độ. Góc lệch của tia sáng bằng bao nhiêu độ?", "15", "D = 45° - 30° = 15°."),
    make_sa(2, "Thông hiểu", "Một kính lúp có ghi 5x trên vành kính có tiêu cự f bằng bao nhiêu cm?", "5", "f = 25 / 5 = 5 cm."),
    make_sa(3, "Vận dụng", "Chiếu tia sáng từ thủy tinh (igh = 42 độ) ra không khí với góc tới 50 độ. Góc phản xạ của tia sáng bằng bao nhiêu độ?", "50", "i = 50° > igh = 42° nên phản xạ toàn phần, góc phản xạ = 50°."),
    make_sa(4, "Vận dụng", "Một thấu kính hội tụ có f = 14 cm. Khoảng cách ngắn nhất giữa vật thật và ảnh thật của nó là bao nhiêu cm?", "56", "L_min = 4f = 4 × 14 = 56 cm."),
    make_sa(5, "Vận dụng cao", "Đặt vật sáng AB cách thấu kính hội tụ d = 36 cm. Thấu kính có f = 18 cm. Tính khoảng cách từ ảnh thật đến thấu kính theo cm?", "36", "d = 2f = 36 cm => d' = 2f = 36 cm."),
    make_sa(6, "Vận dụng cao", "Dùng kính lúp có f = 6 cm quan sát một mẫu vật nhỏ đặt cách kính d = 4 cm. Ảnh ảo của mẫu vật phóng đại gấp mấy lần vật thật?", "3", "1/d' = 1/6 - 1/4 = -1/12 => |d'| = 12 cm. k = 12/4 = 3 lần.")
]

p4_rev_t5 = [
    make_vdc(1, "Một người muốn chụp ảnh một chiếc ô tô dài 4 m đậu cách máy ảnh một đoạn 20 m. Vật kính của máy ảnh có tiêu cự f = 5 cm. Chiều dài ảnh của chiếc ô tô in trên cảm biến máy ảnh là bao nhiêu cm?", [
        "1,0 cm",
        "2,0 cm",
        "0,5 cm",
        "4,0 cm"
    ], 0, "k ≈ f / d = 0,05 m / 20 m = 1/400. Chiều dài ảnh = 4 m / 400 = 0,01 m = 1,0 cm."),
    make_vdc(2, "Trong y học nhãn khoa, người ta dùng phương pháp bắn laser mổ mắt điều trị cận thị (phương pháp Lasik). Bản chất của phẫu thuật Lasik là:", [
        "Dùng tia laser gọt bớt độ cong giác mạc để làm giảm độ hội tụ của mắt, giúp ảnh của vật lùi về đúng trên màng lưới",
        "Gắn một thấu kính phân kì vĩnh viễn vào trong nhãn cầu",
        "Kéo dài nhãn cầu ra phía sau",
        "Làm tăng độ nhạy sáng của màng lưới"
    ], 0, "Lasik bào mòn giác mạc làm giảm độ cong và độ tụ của mắt, đưa tiêu điểm lùi về màng lưới."),
    make_vdc(3, "Một bể bơi nước sâu 2,0 m có đáy phẳng nằm ngang. Chiết suất của nước là 4/3. Người đứng trên bờ nhìn gần như thẳng góc xuống đáy bể thấy đáy bể như được nâng lên cao thêm bao nhiêu cm so với vị trí thực tế?", [
        "50 cm",
        "150 cm",
        "20 cm",
        "100 cm"
    ], 0, "h' = 200 / (4/3) = 150 cm. Độ nâng ảnh Δh = h - h' = 200 - 150 = 50 cm."),
    make_vdc(4, "Một kính tiềm vọng đơn giản có chiều cao giữa hai lăng kính phản xạ toàn phần là H = 60 cm. Khi người quan sát ngắm nhìn một con tàu trên mặt biển cách lăng kính phía trên một khoảng d = 500 m thì hình ảnh con tàu quan sát được qua kính tiềm vọng có khoảng cách quang học đến mắt người là:", [
        "500,6 m",
        "500 m",
        "499,4 m",
        "300 m"
    ], 0, "Ánh sáng đi từ tàu đến lăng kính trên (500 m), truyền dọc thân kính (0,6 m) tới lăng kính dưới rồi vào mắt: d_tổng = 500 + 0,6 = 500,6 m.")
]

exams["phys9_c6_rev_test5"] = make_exam(CH_ID, CH_TITLE, L_ID, L_NAME, 5, p1_rev_t5, p2_rev_t5, p3_rev_t5, p4_rev_t5)

print("Added phys9_c6_rev (5 tests).")
