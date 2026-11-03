# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - CHƯƠNG VI (PHẦN 1: BÀI 17, 18, 19)
Bao gồm 9 đề thi độc lập 100%, không trùng lặp câu hỏi:
- phys9_c6_b17 (test1, test2, test3)
- phys9_c6_b18 (test1, test2, test3)
- phys9_c6_b19 (test1, test2, test3)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c6"
CH_TITLE = "Chương VI: Ánh sáng"

# =============================================================================
# BÀI 17: HIỆN TƯỢNG KHÚC XẠ ÁNH SÁNG (3 ĐỀ)
# =============================================================================

# --- phys9_c6_b17_test1 ---
p1_b17_t1 = [
    make_mc(1, "Nhận biết", "Hiện tượng khúc xạ ánh sáng là hiện tượng tia sáng truyền từ môi trường trong suốt này sang môi trường trong suốt khác bị:", [
        "Gãy khúc tại mặt phân cách giữa hai môi trường",
        "Hắt ngược hoàn toàn trở lại môi trường trong suốt ban đầu",
        "Giữ nguyên hướng truyền thẳng tuyệt đối trong mọi trường hợp",
        "Hấp thụ hoàn toàn và biến đổi thành nhiệt năng"
    ], 0, "Khúc xạ ánh sáng là hiện tượng tia sáng bị gãy khúc tại mặt phân cách giữa hai môi trường trong suốt."),
    make_mc(2, "Nhận biết", "Mặt phẳng tới trong hiện tượng khúc xạ ánh sáng được xác định bởi:", [
        "Mặt phẳng chứa tia khúc xạ và pháp tuyến tại điểm tới",
        "Tia tới và pháp tuyến tại điểm tới",
        "Mặt phân cách giữa hai môi trường trong suốt",
        "Tia tới và mặt phân cách giữa hai môi trường"
    ], 1, "Mặt phẳng tới là mặt phẳng tạo bởi tia tới và đường pháp tuyến tại điểm tới."),
    make_mc(3, "Nhận biết", "Khi truyền tia sáng từ không khí vào nước với góc tới i > 0, mối quan hệ giữa góc khúc xạ r và góc tới i là:", [
        "Góc khúc xạ r lớn hơn góc tới i",
        "Góc khúc xạ r bằng hai lần góc tới i",
        "Góc khúc xạ r nhỏ hơn góc tới i",
        "Góc khúc xạ r luôn bằng 90 độ"
    ], 2, "Vì nước chiết quang hơn không khí nên tia sáng bị bẻ gãy lại gần pháp tuyến, dẫn đến r < i."),
    make_mc(4, "Nhận biết", "Đường thẳng vuông góc với mặt phân cách giữa hai môi trường tại điểm tới được gọi là:", [
        "Tia khúc xạ",
        "Trục chính",
        "Đường phân giác",
        "Pháp tuyến"
    ], 3, "Pháp tuyến tại điểm tới là đường thẳng vuông góc với mặt phân cách tại điểm tới."),
    make_mc(5, "Nhận biết", "Khi chiếu tia sáng vuông góc với mặt phân cách giữa hai môi trường trong suốt (góc tới i = 0 độ) thì:", [
        "Tia sáng truyền thẳng không bị khúc xạ",
        "Tia sáng bị khúc xạ với góc khúc xạ bằng 45 độ",
        "Tia sáng bị phản xạ toàn phần trở lại",
        "Tia sáng bị gãy khúc một góc 90 độ"
    ], 0, "Khi i = 0° (chiếu vuông góc), tia sáng truyền thẳng mà không bị đổi hướng (r = 0°)."),
    make_mc(6, "Nhận biết", "Trong hiện tượng khúc xạ ánh sáng, khi góc tới i tăng dần (nhưng nhỏ hơn 90 độ) thì góc khúc xạ r sẽ:", [
        "Giảm dần về 0 độ",
        "Tăng dần theo",
        "Không đổi và giữ nguyên giá trị",
        "Lập tức bằng 90 độ"
    ], 1, "Khi góc tới tăng, góc khúc xạ cũng tăng dần theo tỉ lệ xác định."),
    make_mc(7, "Thông hiểu", "Đặt một chiếc đũa nghiêng trong một bát nước trong suốt, ta nhìn thấy chiếc đũa dường như bị gãy tại mặt nước. Nguyên nhân của hiện tượng này là do:", [
        "Ánh sáng bị phản xạ toàn phần tại đáy bát",
        "Hiện tượng tán sắc ánh sáng mặt trời",
        "Hiện tượng khúc xạ ánh sáng từ nước ra không khí",
        "Hiện tượng giao thoa ánh sáng trên mặt nước"
    ], 2, "Tia sáng xuất phát từ phần chiếc đũa chìm trong nước khi ra không khí bị khúc xạ lệch xa pháp tuyến, tạo cảm giác đũa bị gập khúc."),
    make_mc(8, "Thông hiểu", "Một người đứng trên bờ nhìn xuống một hồ bơi nước trong suốt sẽ cảm thấy đáy hồ bơi:", [
        "Sâu hơn độ sâu thực tế của hồ",
        "Rộng hơn diện tích thực tế rất nhiều",
        "Có độ sâu không thay đổi so với thực tế",
        "Cạn hơn (nông hơn) so với độ sâu thực tế"
    ], 3, "Hiện tượng khúc xạ làm ảnh ảo của đáy hồ bị nâng lên gần mặt nước hơn so với vị trí thực tế."),
    make_mc(9, "Thông hiểu", "Chiếu một tia sáng từ thủy tinh ra không khí với góc tới i = 30 độ. Giá trị nào sau đây có thể là góc khúc xạ r?", [
        "48 độ",
        "20 độ",
        "15 độ",
        "30 độ"
    ], 0, "Khi truyền từ môi trường chiết quang hơn (thủy tinh) sang môi trường kém chiết quang hơn (không khí), góc khúc xạ r > i nên r > 30°, chỉ có 48° là phù hợp."),
    make_mc(10, "Thông hiểu", "Một con cá vàng đang bơi trong bể kính đựng nước trong veo. Một người nhìn từ ngoài bể vào thấy con cá vàng:", [
        "Ở đúng vị trí thực tế mà con cá đang bơi",
        "Ở vị trí ảnh ảo cao hơn vị trí thật của cá",
        "Ở vị trí ảnh ảo sâu hơn vị trí thật của cá",
        "Bị thu nhỏ kích thước đi rất nhiều lần"
    ], 1, "Khúc xạ từ nước ra không khí làm nâng ảnh của con cá lên cao hơn vị trí thực."),
    make_mc(11, "Thông hiểu", "Khi tia sáng truyền từ không khí vào một khối thủy tinh trong suốt, góc lệch giữa tia tới và tia khúc xạ được tính bằng:", [
        "Tổng của góc tới và góc khúc xạ: i + r",
        "Tích của góc tới và góc khúc xạ: i × r",
        "Hiệu của góc tới và góc khúc xạ: i - r",
        "Thương số giữa góc tới và góc khúc xạ: i / r"
    ], 2, "Vì tia khúc xạ bị lệch lại gần pháp tuyến nên góc lệch so với phương truyền thẳng ban đầu là D = i - r."),
    make_mc(12, "Thông hiểu", "Hiện tượng hoàng hôn hoặc bình minh: Chúng ta nhìn thấy Mặt Trời mọc sớm hơn một chút và lặn muộn hơn một chút so với vị trí hình học thực tế là do:", [
        "Bụi bẩn trong không khí phản xạ ánh sáng Mặt Trời",
        "Trái Đất quay chậm lại vào buổi sớm và chiều tối",
        "Mặt Trời phát ra ánh sáng mạnh hơn vào thời điểm đó",
        "Khí quyển Trái Đất có mật độ giảm dần theo độ cao gây khúc xạ ánh sáng"
    ], 3, "Ánh sáng Mặt Trời bị khúc xạ liên tục khi đi qua tầng khí quyển có mật độ không đều, làm bẻ cong tia sáng về phía bề mặt Trái Đất.")
]

p2_b17_t1 = [
    make_tf(1, "Thông hiểu", "Xét các khẳng định về định luật khúc xạ ánh sáng:", [
        ("a", "Tia khúc xạ và tia tới luôn cùng nằm trong mặt phẳng tới.", True),
        ("b", "Góc khúc xạ r luôn luôn bằng góc tới i trong mọi trường hợp.", False),
        ("c", "Khi tia sáng truyền từ không khí vào nước, góc khúc xạ r luôn nhỏ hơn góc tới i.", True),
        ("d", "Nếu chiếu tia sáng vuông góc với mặt nước thì tia sáng bị lệch một góc 45 độ.", False)
    ], "Góc khúc xạ phụ thuộc vào môi trường truyền; khi chiếu vuông góc (i = 0°) thì tia sáng truyền thẳng."),
    make_tf(2, "Thông hiểu", "Thí nghiệm chiếu tia sáng hẹp từ không khí vào bán trụ thủy tinh trong suốt:", [
        ("a", "Khi tia sáng đi tới tâm của mặt cong bán trụ thì nó truyền thẳng vào trong mà không đổi hướng.", True),
        ("b", "Khi tăng góc tới i từ 10 độ lên 50 độ thì góc khúc xạ r cũng tăng dần theo.", True),
        ("c", "Góc khúc xạ r trong thủy tinh luôn lớn hơn góc tới i trong không khí.", False),
        ("d", "Tia khúc xạ và tia tới nằm ở hai phía khác nhau so với đường pháp tuyến.", True)
    ], "Thủy tinh chiết quang hơn không khí nên r < i."),
    make_tf(3, "Vận dụng", "Một người nông dân dùng xiên nhọn để bắt cá dưới mương nước trong vắt:", [
        ("a", "Hình ảnh con cá mà người nông dân nhìn thấy bằng mắt thường là ảnh ảo của con cá.", True),
        ("b", "Ảnh ảo của con cá nằm nông hơn vị trí thật mà con cá đang bơi.", True),
        ("c", "Để xiên trúng con cá, người nông dân phải ngắm mũi xiên cao hơn vị trí nhìn thấy con cá.", False),
        ("d", "Nếu đứng nhìn thẳng góc từ trên xuống mặt nước thì ảnh của cá vẫn bị nâng lên gần mặt nước.", True)
    ], "Muốn đâm trúng cá, người đi săn phải ngắm thấp hơn vị trí nhìn thấy con cá vì vị trí thật nằm sâu hơn ảnh ảo."),
    make_tf(4, "Vận dụng", "Chiếu một tia sáng từ không khí vào một chất lỏng trong suốt với góc tới i = 45 độ, đo được góc khúc xạ r = 30 độ:", [
        ("a", "Góc hợp bởi tia khúc xạ và phương truyền thẳng ban đầu của tia sáng là 15 độ.", True),
        ("b", "Chất lỏng này có tính chiết quang mạnh hơn không khí.", True),
        ("c", "Nếu giảm góc tới xuống i = 30 độ thì góc khúc xạ r sẽ tăng lên thành 35 độ.", False),
        ("d", "Góc tạo bởi tia khúc xạ và mặt phân cách giữa hai môi trường là 60 độ.", True)
    ], "Góc lệch D = 45° - 30° = 15°. Góc giữa tia khúc xạ và mặt phân cách là 90° - 30° = 60°.")
]

p3_b17_t1 = [
    make_sa(1, "Thông hiểu", "Chiếu một tia sáng từ không khí vào nước vuông góc với mặt nước. Góc khúc xạ của tia sáng bằng bao nhiêu độ?", "0", "Chiếu vuông góc nghĩa là góc tới i = 0°, góc khúc xạ r = 0°."),
    make_sa(2, "Thông hiểu", "Chiếu tia sáng từ không khí vào khối thủy tinh với góc tới 50 độ, đo được góc khúc xạ là 30 độ. Góc lệch giữa phương truyền ban đầu và tia khúc xạ là bao nhiêu độ?", "20", "D = i - r = 50° - 30° = 20°."),
    make_sa(3, "Vận dụng", "Chiếu một tia sáng từ một khối nhựa trong suốt ra không khí với góc tới 28 độ. Biết góc khúc xạ lớn hơn góc tới 14 độ. Hỏi góc khúc xạ bằng bao nhiêu độ?", "42", "r = i + 14° = 28° + 14° = 42°."),
    make_sa(4, "Vận dụng", "Một tia sáng chiếu từ không khí vào nước. Biết tia tới hợp với mặt nước một góc 35 độ. Hỏi góc tới i bằng bao nhiêu độ?", "55", "Góc tới là góc hợp với pháp tuyến: i = 90° - 35° = 55°."),
    make_sa(5, "Vận dụng cao", "Một bể bơi chứa nước sâu 1,8 m. Một người nhìn theo phương gần như thẳng đứng từ không khí xuống đáy bể. Biết nước có chiết suất bằng 4/3. Đáy bể dường như cách mặt nước bao nhiêu mét?", "1.35", "h' = h / n = 1,8 / (4/3) = 1,35 m."),
    make_sa(6, "Vận dụng cao", "Một chiếc cọc cắm thẳng đứng dưới đáy hồ, phần nhô lên khỏi mặt nước dài 0,6 m, hồ sâu 1,2 m. Ánh sáng Mặt Trời chiếu nghiêng góc 45 độ so với phương thẳng đứng, tia khúc xạ trong nước tạo góc 30 độ với pháp tuyến. Chiều dài bóng của cọc in dưới đáy hồ là bao nhiêu mét? (Biết tan 45° = 1; tan 30° ≈ 0,577; làm tròn 2 chữ số thập phân)", "1.29", "L = 0,6 × tan(45°) + 1,2 × tan(30°) = 0,6 + 1,2 × 0,577 ≈ 1,29 m.")
]

p4_b17_t1 = [
    make_vdc(1, "Trong kỹ thuật đánh bắt cá ngầm hoặc săn cá bằng cung tên của thổ dân, khi đứng trên bờ ngắm vào một con cá ở dưới nước, người bắn bắt buộc phải ngắm vào đâu để bắn trúng con cá?", [
        "Ngắm thấp hơn vị trí con cá nhìn thấy",
        "Ngắm chính xác ngay vào tâm con cá nhìn thấy",
        "Ngắm chếch lên cao hơn vị trí con cá nhìn thấy",
        "Ngắm sang bên phải con cá nhìn thấy 1 mét"
    ], 0, "Do khúc xạ, ảnh mắt nhìn thấy cao hơn con cá thực tế. Do đó phải ngắm thấp hơn ảnh để trúng cá."),
    make_vdc(2, "Khi quan sát vị trí của một ngôi sao ở gần đường chân trời qua kính viễn vọng, các nhà thiên văn học luôn phải hiệu chỉnh vị trí góc vì:", [
        "Vị trí biểu kiến của ngôi sao nhìn thấy luôn cao hơn vị trí hình học thực tế do khí quyển Trái Đất bẻ cong ánh sáng",
        "Ngôi sao liên tục di chuyển với vận tốc nhanh hơn ánh sáng",
        "Ánh sáng ngôi sao bị Mặt Trăng che khuất một phần",
        "Kính viễn vọng làm đảo ngược hoàn toàn chiều ánh sáng"
    ], 0, "Khí quyển Trái Đất hoạt động như một môi trường chiết quang biến thiên làm bẻ cong ánh sáng hướng xuống, nâng cao vị trí biểu kiến của thiên thể."),
    make_vdc(3, "Thực hiện thí nghiệm: Đặt một đồng xu bằng kim loại dưới đáy một chiếc bát sứ màu đục. Đặt mắt sao cho thành bát vừa vặn che khuất đồng xu. Giữ nguyên vị trí mắt, từ từ rót nước trong vào bát thì hiện tượng gì xảy ra?", [
        "Đồng xu dường như nổi lên và mắt lại nhìn thấy đồng xu rõ ràng",
        "Đồng xu chìm sâu hơn và biến mất hoàn toàn",
        "Đồng xu bị vỡ đôi do áp suất của nước",
        "Đồng xu phát sáng màu xanh dạ quang"
    ], 0, "Khi đổ nước vào, ánh sáng từ đồng xu đi qua mặt phân cách nước - không khí bị khúc xạ bẻ gãy truyền tới mắt, làm đồng xu như nổi lên."),
    make_vdc(4, "Một tia sáng truyền qua một bản thủy tinh hai mặt song song đặt trong không khí. Sau khi khúc xạ hai lần qua hai bề mặt, tia ló ra môi trường không khí có đặc điểm gì?", [
        "Song song với tia tới ban đầu nhưng bị dịch chuyển ngang một khoảng cách",
        "Vuông góc hoàn toàn với tia tới ban đầu",
        "Bị đổi màu sắc thành dải cầu vồng 7 màu",
        "Hội tụ lại tại một tiêu điểm cố định"
    ], 0, "Qua bản mặt song song, góc khúc xạ ở mặt thứ nhất bằng góc tới ở mặt thứ hai nên tia ló song song với tia tới nhưng bị dời ngang.")
]

exams["phys9_c6_b17_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b17", "Bài 17: Hiện tượng khúc xạ ánh sáng", 1, p1_b17_t1, p2_b17_t1, p3_b17_t1, p4_b17_t1)

# --- phys9_c6_b17_test2 ---
p1_b17_t2 = [
    make_mc(1, "Nhận biết", "Góc hợp bởi tia khúc xạ và đường pháp tuyến tại điểm tới được gọi là:", [
        "Góc khúc xạ",
        "Góc tới",
        "Góc phản xạ",
        "Góc lệch phương"
    ], 0, "Góc khúc xạ là góc hợp bởi tia khúc xạ và pháp tuyến."),
    make_mc(2, "Nhận biết", "Khi truyền tia sáng từ nước sang không khí với góc tới i nhỏ hơn góc giới hạn phản xạ toàn phần, so sánh giữa góc tới i và góc khúc xạ r:", [
        "Góc khúc xạ r luôn bằng góc tới i",
        "Góc khúc xạ r lớn hơn góc tới i",
        "Góc khúc xạ r nhỏ hơn góc tới i",
        "Góc khúc xạ r luôn luôn bằng 0 độ"
    ], 1, "Khi truyền từ nước sang không khí kém chiết quang hơn, tia khúc xạ lệch xa pháp tuyến nên r > i."),
    make_mc(3, "Nhận biết", "Giao điểm giữa tia tới và mặt phân cách giữa hai môi trường trong suốt được gọi là:", [
        "Tiêu điểm chính",
        "Quang tâm",
        "Điểm tới",
        "Tâm đối xứng"
    ], 2, "Giao điểm của tia tới với mặt phân cách gọi là điểm tới."),
    make_mc(4, "Nhận biết", "Trong hiện tượng khúc xạ ánh sáng, tia tới và tia khúc xạ:", [
        "Luôn trùng khít lên nhau",
        "Nằm ở cùng một phía so với pháp tuyến",
        "Nằm ở hai mặt phẳng hoàn toàn tách biệt",
        "Nằm ở hai phía khác nhau so với đường pháp tuyến tại điểm tới"
    ], 3, "Tia tới và tia khúc xạ nằm ở hai phía đối diện so với pháp tuyến."),
    make_mc(5, "Nhận biết", "Nếu góc tới i = 0 độ khi truyền ánh sáng giữa hai môi trường trong suốt thì góc khúc xạ r có giá trị là:", [
        "r = 0 độ",
        "r = 45 độ",
        "r = 90 độ",
        "r = 180 độ"
    ], 0, "Góc tới bằng 0° thì tia sáng truyền thẳng, góc khúc xạ r = 0°."),
    make_mc(6, "Nhận biết", "Tia sáng truyền trong một môi trường trong suốt và đồng tính thì có đặc điểm là:", [
        "Truyền theo đường gấp khúc tuần hoàn",
        "Truyền theo đường thẳng",
        "Luôn bị uốn cong hình parabol",
        "Truyền xoắn ốc theo thời gian"
    ], 1, "Định luật truyền thẳng của ánh sáng: Trong môi trường trong suốt và đồng tính, ánh sáng truyền theo đường thẳng."),
    make_mc(7, "Thông hiểu", "Một tia sáng chiếu từ không khí vào khối thủy tinh dưới góc tới 60 độ. Nhận xét nào sau đây về góc khúc xạ r là đúng?", [
        "Góc khúc xạ r lớn hơn 60 độ",
        "Góc khúc xạ r bằng đúng 60 độ",
        "Góc khúc xạ r nhỏ hơn 60 độ",
        "Góc khúc xạ r bằng đúng 90 độ"
    ], 2, "Không khí sang thủy tinh: thủy tinh chiết quang hơn nên tia sáng bị bẻ gãy lại gần pháp tuyến, do đó r < 60°."),
    make_mc(8, "Thông hiểu", "Một người lặn dưới đáy hồ bơi nhìn ngược lên mặt nước thấy hình ảnh của các cây xanh trên bờ bị co cụm lại thành một hình nón sáng. Nguyên nhân là do:", [
        "Ánh sáng từ trên bờ truyền vào nước bị phản xạ hoàn toàn",
        "Hiện tượng hấp thụ ánh sáng của các phân tử nước",
        "Nước làm đảo ngược chiều ánh sáng truyền tới mắt",
        "Hiện tượng khúc xạ ánh sáng từ không khí vào nước có góc khúc xạ nhỏ hơn góc tới"
    ], 3, "Tất cả ánh sáng từ góc 180° trên bờ khi vào nước bị thu hẹp lại trong nón góc mở giới hạn do r < i."),
    make_mc(9, "Thông hiểu", "Chiếu tia sáng từ không khí vào nước với góc tới i = 45 độ, đo được góc khúc xạ r = 32 độ. Góc tạo bởi tia khúc xạ và mặt phân cách là:", [
        "58 độ",
        "32 độ",
        "45 độ",
        "13 độ"
    ], 0, "Góc tạo bởi tia khúc xạ và mặt phân cách là 90° - r = 90° - 32° = 58°."),
    make_mc(10, "Thông hiểu", "Để xác định chiết suất của một chất lỏng, người ta đo góc tới i và góc khúc xạ r. Nếu góc tới tăng từ 30 độ lên 60 độ thì tỉ số sin i / sin r sẽ:", [
        "Tăng lên gấp đôi",
        "Không thay đổi",
        "Giảm đi một nửa",
        "Biến thiên ngẫu nhiên"
    ], 1, "Theo định luật khúc xạ ánh sáng, tỉ số sin i / sin r là một hằng số không đổi đặc trưng cho hai môi trường."),
    make_mc(11, "Thông hiểu", "Khi quan sát một viên bi ve đặt dưới đáy một chậu nước sâu 20 cm, người quan sát nhìn thấy viên bi ve dường như nổi lên cách mặt nước khoảng 15 cm. Hiện tượng này chứng minh rằng:", [
        "Nước có khối lượng riêng lớn hơn không khí",
        "Ánh sáng truyền trong nước nhanh hơn trong không khí",
        "Hiện tượng khúc xạ làm vị trí ảnh ảo của viên bi dời lại gần mặt thoáng",
        "Viên bi thực sự bị đẩy nổi bởi lực đẩy Ác-si-mét"
    ], 2, "Khúc xạ ánh sáng từ nước ra không khí làm nâng ảnh ảo lên gần mặt nước."),
    make_mc(12, "Thông hiểu", "Một tia sáng truyền qua mặt phân cách giữa hai chất lỏng trong suốt khác nhau mà không hề bị gãy khúc (vẫn truyền thẳng dù chiếu xiên góc). Điều này chứng tỏ:", [
        "Hai chất lỏng có cùng chiết suất đối với ánh sáng đó",
        "Hai chất lỏng có cùng khối lượng riêng",
        "Hai chất lỏng có cùng nhiệt độ sôi",
        "Mặt phân cách giữa hai chất lỏng là một mặt gương phẳng"
    ], 0, "Nếu hai môi trường có cùng chiết suất (tỉ số n1/n2 = 1) thì góc r = i, tia sáng truyền thẳng mà không bị khúc xạ.")
]

p2_b17_t2 = [
    make_tf(1, "Thông hiểu", "Xét các hiện tượng liên quan đến sự truyền ánh sáng qua mặt phân cách:", [
        ("a", "Tia phản xạ và tia khúc xạ luôn nằm trong cùng một mặt phẳng tới.", True),
        ("b", "Góc phản xạ luôn bằng góc tới.", True),
        ("c", "Góc khúc xạ luôn bằng góc phản xạ.", False),
        ("d", "Hiện tượng khúc xạ chỉ xảy ra khi chiếu tia sáng xiên góc qua mặt phân cách giữa hai môi trường trong suốt khác nhau.", True)
    ], "Góc khúc xạ phụ thuộc chiết suất của môi trường nên thường khác góc phản xạ; khi chiếu vuông góc thì không bị bẻ gãy."),
    make_tf(2, "Thông hiểu", "Một tia sáng truyền từ dầu hỏa sang nước trong suốt (biết dầu hỏa chiết quang hơn nước):", [
        ("a", "Tia sáng truyền từ môi trường chiết quang hơn sang môi trường kém chiết quang hơn.", True),
        ("b", "Góc khúc xạ r trong nước lớn hơn góc tới i trong dầu hỏa.", True),
        ("c", "Tia khúc xạ bị bẻ gãy lệch lại gần đường pháp tuyến.", False),
        ("d", "Nếu chiếu tia sáng vuông góc với mặt phân cách thì tia sáng vẫn truyền thẳng.", True)
    ], "Từ chiết quang hơn sang kém hơn thì r > i, tia khúc xạ lệch xa pháp tuyến."),
    make_tf(3, "Vận dụng", "Một chậu thủy tinh chứa một lớp nước trong suốt, đáy chậu có đặt một đồng xu:", [
        ("a", "Ảnh của đồng xu thu được là ảnh thật và hứng được trên màn chắn.", False),
        ("b", "Độ nâng của ảnh đồng xu phụ thuộc vào độ sâu của lớp nước và chiết suất của nước.", True),
        ("c", "Nếu thay nước bằng dung dịch nước muối đậm đặc có chiết suất lớn hơn thì ảnh của đồng xu càng bị nâng cao hơn.", True),
        ("d", "Khi nhìn nghiêng góc càng lớn so với pháp tuyến thì đồng xu trông càng bị dời xa vị trí thật.", True)
    ], "Ảnh của đồng xu nhìn từ ngoài vào là ảnh ảo, không thể hứng trên màn."),
    make_tf(4, "Vận dụng", "Chiếu tia sáng từ không khí vào một tấm thủy tinh phẳng với góc tới i = 60 độ, biết góc khúc xạ là r = 35 độ:", [
        ("a", "Tia khúc xạ bị lệch so với hướng ban đầu của tia tới một góc bằng 25 độ.", True),
        ("b", "Góc hợp bởi tia khúc xạ và pháp tuyến là 55 độ.", False),
        ("c", "Góc tạo bởi tia khúc xạ và mặt phẳng tấm thủy tinh là 55 độ.", True),
        ("d", "Vận tốc truyền ánh sáng trong tấm thủy tinh này nhỏ hơn vận tốc ánh sáng trong chân không.", True)
    ], "Góc khúc xạ là góc hợp với pháp tuyến nên r = 35°. Góc hợp với bề mặt tấm là 90° - 35° = 55°.")
]

p3_b17_t2 = [
    make_sa(1, "Thông hiểu", "Một tia sáng tới mặt nước tạo với bề mặt nước một góc 60 độ. Góc tới i của tia sáng bằng bao nhiêu độ?", "30", "Góc tới là góc hợp với pháp tuyến: i = 90° - 60° = 30°."),
    make_sa(2, "Thông hiểu", "Chiếu tia sáng từ không khí vào khối chất lỏng với góc tới 45 độ, đo được góc khúc xạ là 30 độ. Góc tới lớn hơn góc khúc xạ bao nhiêu độ?", "15", "45° - 30° = 15°."),
    make_sa(3, "Vận dụng", "Một tia sáng truyền từ thủy tinh ra không khí với góc tới 25 độ. Biết tia khúc xạ bị lệch một góc 15 độ so với phương tia tới. Góc khúc xạ r bằng bao nhiêu độ?", "40", "Từ thủy tinh ra không khí thì r > i, nên r = i + D = 25° + 15° = 40°."),
    make_sa(4, "Vận dụng", "Đáy một hồ bơi sâu 2,0 m. Khi nhìn thẳng góc từ trên bờ xuống hồ, người quan sát thấy đáy hồ cách mặt nước 1,5 m. Chiết suất của nước trong hồ bằng bao nhiêu? (Làm tròn 2 chữ số thập phân)", "1.33", "n = h / h' = 2,0 / 1,5 ≈ 1,33."),
    make_sa(5, "Vận dụng cao", "Chiếu một tia sáng từ không khí vào bản thủy tinh dày d = 4 cm với góc tới 60 độ. Góc khúc xạ trong thủy tinh là 30 độ. Độ dài đường đi của tia sáng bên trong bản thủy tinh bằng bao nhiêu cm? (Lấy kết quả đến 2 chữ số thập phân)", "4.62", "Độ dài đường truyền bên trong bản: s = d / cos(r) = 4 / cos(30°) = 4 / 0,866 ≈ 4,62 cm."),
    make_sa(6, "Vận dụng cao", "Một chiếc que cắm thẳng đứng ngập hoàn toàn trong nước. Phần que chìm trong nước dài 80 cm. Biết chiết suất của nước là 4/3. Khi nhìn gần như thẳng góc từ trên mặt nước xuống, ảnh của que có chiều dài biểu kiến là bao nhiêu cm?", "60", "L' = L / n = 80 / (4/3) = 60 cm.")
]

p4_b17_t2 = [
    make_vdc(1, "Vào buổi chiều tà khi hoàng hôn buông xuống, đĩa Mặt Trời nhìn thấy ở chân trời thường có dạng hình elip bị dẹt theo phương thẳng đứng thay vì hình tròn hoàn hảo. Nguyên nhân vật lý của hiện tượng này là:", [
        "Các tia sáng từ mép dưới của Mặt Trời đi qua lớp không khí dày và đặc hơn nên bị khúc xạ nâng lên nhiều hơn mép trên",
        "Mặt Trời thực sự bị co lại do nhiệt độ giảm vào buổi tối",
        "Tốc độ quay của Trái Đất kéo giãn hình ảnh Mặt Trời",
        "Mắt người bị mỏi vào buổi chiều gây ảo giác quang học"
    ], 0, "Khí quyển càng sát mặt đất càng đặc, độ chênh lệch khúc xạ giữa mép trên và mép dưới của đĩa Mặt Trời làm mép dưới bị nâng cao hơn, khiến hình ảnh trông bị dẹt."),
    make_vdc(2, "Khúc xạ kế Abbe là thiết bị quang học dùng trong công nghiệp thực phẩm để đo nồng độ đường trong nước mía. Thiết bị này hoạt động dựa trên nguyên lý:", [
        "Sự thay đổi góc khúc xạ của chùm tia sáng khi nồng độ chất tan trong dung dịch thay đổi làm chiết suất thay đổi",
        "Đo nhiệt độ sôi của dung dịch đường",
        "Đo độ dẫn điện của dung dịch nước mía",
        "Đo khối lượng chất tan bị lắng đọng dưới đáy"
    ], 0, "Nồng độ chất tan (đường) làm thay đổi chiết suất dung dịch, dẫn tới sự thay đổi góc khúc xạ đo được trên thang chia."),
    make_vdc(3, "Một bể bơi hình chữ nhật không chứa nước, người đứng ở một đầu thành bể nhìn thấy một điểm đen đánh dấu ở mép đáy đối diện. Khi bơm đầy nước trong suốt vào bể bơi thì:", [
        "Điểm đen trông như bị dời lại gần người quan sát và nâng cao hơn so với đáy bể ban đầu",
        "Điểm đen bị chìm sâu hơn và lùi xa người quan sát",
        "Điểm đen biến mất hoàn toàn không thể quan sát được nữa",
        "Điểm đen đổi màu từ đen sang màu đỏ rực"
    ], 0, "Khúc xạ ánh sáng làm ảnh ảo của đáy bể và các vật thể dưới đáy dời lên cao và hướng lại gần mặt nước theo phương nhìn."),
    make_vdc(4, "Một tia sáng truyền từ không khí vào một giọt sương hình cầu trong suốt. Sau khi khúc xạ tại mặt trước, phản xạ một lần tại mặt sau và khúc xạ thoát ra ngoài, chùm tia sáng tạo nên hiện tượng tự nhiên nào?", [
        "Cầu vồng sau cơn mưa",
        "Nhật thực toàn phần",
        "Ảo ảnh sa mạc Fata Morgana",
        "Sét đánh trong cơn giông"
    ], 0, "Hiện tượng cầu vồng hình thành do ánh sáng mặt trời bị khúc xạ, phản xạ trong giọt nước mưa và tán sắc thoát ra ngoài.")
]

exams["phys9_c6_b17_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b17", "Bài 17: Hiện tượng khúc xạ ánh sáng", 2, p1_b17_t2, p2_b17_t2, p3_b17_t2, p4_b17_t2)

# --- phys9_c6_b17_test3 ---
p1_b17_t3 = [
    make_mc(1, "Nhận biết", "Trong hiện tượng khúc xạ ánh sáng, đại lượng nào sau đây của chùm sóng ánh sáng không thay đổi khi truyền qua mặt phân cách hai môi trường?", [
        "Tần số của ánh sáng",
        "Vận tốc truyền ánh sáng",
        "Bước sóng của ánh sáng",
        "Phương truyền của tia sáng"
    ], 0, "Tần số của sóng ánh sáng do nguồn phát quyết định và không bao giờ đổi khi truyền qua các môi trường khác nhau."),
    make_mc(2, "Nhận biết", "So với vận tốc truyền ánh sáng trong chân không (c ≈ 300.000 km/s), vận tốc truyền ánh sáng trong nước:", [
        "Lớn hơn rất nhiều",
        "Nhỏ hơn",
        "Bằng nhau tuyệt đối",
        "Luôn bằng 0"
    ], 1, "Vận tốc ánh sáng trong các môi trường vật chất luôn nhỏ hơn trong chân không: v = c / n."),
    make_mc(3, "Nhận biết", "Góc hợp bởi tia tới và đường pháp tuyến tại điểm tới được kí hiệu là:", [
        "Kí hiệu r",
        "Kí hiệu D",
        "Kí hiệu i",
        "Kí hiệu alpha"
    ], 2, "Góc tới được ký hiệu là i (incident angle)."),
    make_mc(4, "Nhận biết", "Khi tia sáng truyền từ không khí vào khối nhựa trong suốt với góc tới i = 50 độ, góc khúc xạ r thoả mãn điều kiện:", [
        "r > 50 độ",
        "r = 90 độ",
        "r = 50 độ",
        "r < 50 độ"
    ], 3, "Nhựa trong suốt chiết quang hơn không khí nên góc khúc xạ nhỏ hơn góc tới: r < 50°."),
    make_mc(5, "Nhận biết", "Nếu tia sáng truyền từ chất lỏng ra không khí với góc tới i = 25 độ thì góc khúc xạ r:", [
        "Chắc chắn lớn hơn 25 độ",
        "Chắc chắn nhỏ hơn 25 độ",
        "Bằng đúng 25 độ",
        "Luôn luôn bằng 0 độ"
    ], 0, "Từ chất lỏng ra không khí kém chiết quang hơn thì r > i, do đó r > 25°."),
    make_mc(6, "Nhận biết", "Hiện tượng khúc xạ ánh sáng chỉ xảy ra tại:", [
        "Bên trong lòng của một môi trường hoàn toàn đồng tính",
        "Mặt phân cách giữa hai môi trường trong suốt khi chiếu xiên góc",
        "Bề mặt của vật đục không cho ánh sáng đi qua",
        "Mọi điểm trong không gian vũ trụ chân không"
    ], 1, "Khúc xạ xảy ra tại mặt phân cách giữa hai môi trường trong suốt."),
    make_mc(7, "Thông hiểu", "Một bình thủy tinh chứa đầy nước. Nhìn từ trên xuống đáy bình, ta có cảm giác nước trong bình nông hơn thực tế. Để đo chính xác chiều cao cột nước, ta phải dùng dụng cụ nào?", [
        "Ước lượng bằng mắt thường từ phía trên",
        "Dùng ống nhòm quang học",
        "Dùng thước đo thẳng nhúng trực tiếp chạm đáy bình",
        "Dùng kính lúp cầm tay"
    ], 2, "Mắt thường nhìn bị ảo giác do khúc xạ, nên phải dùng thước thẳng đo trực tiếp chiều sâu."),
    make_mc(8, "Thông hiểu", "Chiếu tia sáng từ không khí vào nước với góc tới i = 60 độ, biết góc khúc xạ là r = 40 độ. Góc hợp bởi tia phản xạ và tia khúc xạ là:", [
        "100 độ",
        "80 độ",
        "60 độ",
        "120 độ"
    ], 1, "Góc phản xạ i' = i = 60°. Pháp tuyến nằm giữa tia phản xạ và tia khúc xạ nên góc hợp bởi chúng là 180° - (i' + r) = 180° - (60° + 40°) = 80°."),
    make_mc(9, "Thông hiểu", "Một tia sáng đi từ môi trường 1 vào môi trường 2 có góc tới 45 độ và góc khúc xạ 30 độ. Kết luận nào sau đây là chính xác?", [
        "Môi trường 2 chiết quang hơn môi trường 1",
        "Môi trường 1 chiết quang hơn môi trường 2",
        "Vận tốc ánh sáng trong môi trường 2 lớn hơn trong môi trường 1",
        "Ánh sáng không bị gãy khúc tại mặt phân cách"
    ], 0, "Vì r < i nên môi trường 2 chiết quang hơn môi trường 1 (v2 < v1)."),
    make_mc(10, "Thông hiểu", "Khi ánh sáng truyền từ môi trường có chiết suất n1 sang môi trường có chiết suất n2, nếu n1 > n2 thì:", [
        "Tia khúc xạ bị lệch lại gần pháp tuyến",
        "Tia khúc xạ bị lệch ra xa đường pháp tuyến hơn so với tia tới",
        "Không có tia phản xạ tại mặt phân cách",
        "Tia sáng luôn truyền thẳng với mọi góc tới"
    ], 1, "n1 > n2 => sin r > sin i => r > i, tia khúc xạ lệch xa pháp tuyến."),
    make_mc(11, "Thông hiểu", "Thước ngắm của thợ lặn dưới nước khi nhìn lên các mục tiêu trên bờ trời bị lệch góc do:", [
        "Tia sáng từ bờ vào mắt thợ lặn dưới nước bị bẻ gập lại gần pháp tuyến",
        "Nước biển làm biến đổi bước sóng ánh sáng thành tia X",
        "Mắt thợ lặn bị giảm thị lực hoàn toàn",
        "Kính lặn phản xạ 100% ánh sáng chiếu tới"
    ], 0, "Khúc xạ ánh sáng từ không khí vào nước làm thay đổi phương truyền tia sáng tới mắt người lặn."),
    make_mc(12, "Thông hiểu", "Một tia sáng chiếu vuông góc vào mặt bên của một lăng kính tam giác đều bằng thủy tinh. Tại mặt bên này, góc tới và góc khúc xạ lần lượt là:", [
        "i = 0 độ và r = 0 độ",
        "i = 60 độ và r = 30 độ",
        "i = 90 độ và r = 0 độ",
        "i = 30 độ và r = 60 độ"
    ], 0, "Chiếu vuông góc với mặt lăng kính nghĩa là tia tới trùng pháp tuyến: i = 0°, r = 0° (truyền thẳng vào trong lăng kính).")
]

p2_b17_t3 = [
    make_tf(1, "Thông hiểu", "Xét tính chất của hiện tượng khúc xạ ánh sáng:", [
        ("a", "Chiết suất tuyệt đối của mọi môi trường trong suốt đều lớn hơn hoặc bằng 1.", True),
        ("b", "Vận tốc ánh sáng trong nước bằng vận tốc ánh sáng trong chân không.", False),
        ("c", "Khi góc tới i = 0 độ thì góc khúc xạ r = 0 độ đối với mọi cặp môi trường.", True),
        ("d", "Hiện tượng khúc xạ chỉ xảy ra với chùm sáng có cường độ cực lớn.", False)
    ], "Chiết suất n = c / v ≥ 1; vận tốc ánh sáng trong môi trường vật chất luôn nhỏ hơn c."),
    make_tf(2, "Thông hiểu", "Một tia sáng đi từ không khí vào nước với góc tới i = 30 độ, góc khúc xạ r = 22 độ:", [
        ("a", "Tia khúc xạ lệch lại gần pháp tuyến hơn so với tia tới.", True),
        ("b", "Góc lệch D giữa tia tới và tia khúc xạ là 8 độ.", True),
        ("c", "Góc giữa tia khúc xạ và mặt nước là 68 độ.", True),
        ("d", "Góc phản xạ tại mặt nước là 22 độ.", False)
    ], "Góc phản xạ i' = i = 30°. Góc giữa tia khúc xạ và mặt nước là 90° - 22° = 68°."),
    make_tf(3, "Vận dụng", "Quan sát một viên ngọc nằm ở đáy một chiếc cốc thủy tinh đựng đầy nước:", [
        ("a", "Người quan sát nhìn thấy ảnh ảo của viên ngọc ở vị trí cao hơn đáy cốc thực tế.", True),
        ("b", "Khoảng cách từ mặt nước đến ảnh ảo nhỏ hơn độ sâu thực tế của cốc nước.", True),
        ("c", "Nếu rút bớt nước trong cốc thì vị trí ảnh ảo của viên ngọc càng dời lên gần miệng cốc.", False),
        ("d", "Hiện tượng nâng ảnh này là ứng dụng trực tiếp của hiện tượng khúc xạ ánh sáng.", True)
    ], "Rút bớt nước thì độ sâu giảm, ảnh ảo hạ dần về vị trí đáy thật."),
    make_tf(4, "Vận dụng", "Chiếu tia sáng từ chất lỏng chiết suất n ra không khí với góc tới i = 30 độ, đo được góc khúc xạ r = 45 độ:", [
        ("a", "Chất lỏng này chiết quang hơn không khí.", True),
        ("b", "Tia khúc xạ bị lệch một góc 15 độ so với phương truyền thẳng ban đầu của tia tới.", True),
        ("c", "Chiết suất n của chất lỏng xấp xỉ bằng 1,41 (căn bậc hai của 2).", True),
        ("d", "Nếu tăng góc tới lên 60 độ thì chắc chắn góc khúc xạ r sẽ bằng 90 độ.", False)
    ], "n = sin(45°)/sin(30°) = √2 ≈ 1,41. Khi i = 60° > igh = 45° thì xảy ra phản xạ toàn phần, không còn tia khúc xạ.")
]

p3_b17_t3 = [
    make_sa(1, "Thông hiểu", "Chiếu một tia sáng từ không khí vào nước với góc tới 60 độ. Biết góc khúc xạ là 40 độ. Góc lệch giữa phương truyền ban đầu và tia khúc xạ bằng bao nhiêu độ?", "20", "D = i - r = 60° - 40° = 20°."),
    make_sa(2, "Thông hiểu", "Một tia sáng đi từ thủy tinh ra không khí. Góc tới i = 20 độ, góc khúc xạ r = 31 độ. Góc khúc xạ lớn hơn góc tới bao nhiêu độ?", "11", "31° - 20° = 11°."),
    make_sa(3, "Vận dụng", "Một tia sáng chiếu tới mặt phân cách tạo với mặt phân cách một góc 40 độ. Tính số đo góc tới i theo độ?", "50", "i = 90° - 40° = 50°."),
    make_sa(4, "Vận dụng", "Một bể cá cảnh sâu 60 cm. Khi nhìn gần như vuông góc từ trên xuống, ta thấy đáy bể dường như cách mặt nước bao nhiêu cm? (Biết chiết suất của nước là 4/3)", "45", "h' = 60 / (4/3) = 45 cm."),
    make_sa(5, "Vận dụng cao", "Chiếu một tia sáng từ không khí vào một khối thủy tinh với góc tới 60 độ. Tia phản xạ vuông góc với tia khúc xạ. Góc khúc xạ r bằng bao nhiêu độ?", "30", "Tia phản xạ vuông góc tia khúc xạ: i' + r = 90° => r = 90° - 60° = 30°."),
    make_sa(6, "Vận dụng cao", "Một chiếc cọc cắm thẳng đứng trong nước sâu 1,5 m, phần cọc nhô khỏi mặt nước dài 0,5 m. Ánh nắng chiếu nghiêng góc 45 độ so với phương thẳng đứng. Biết góc khúc xạ trong nước là 32 độ (cho tan 45° = 1, tan 32° ≈ 0,625). Chiều dài vệt bóng cọc in dưới đáy hồ là bao nhiêu mét? (Làm tròn 2 chữ số thập phân)", "1.44", "L = 0,5 × tan(45°) + 1,5 × tan(32°) = 0,5 + 1,5 × 0,625 = 0,5 + 0,9375 = 1,4375 ≈ 1,44 m.")
]

p4_b17_t3 = [
    make_vdc(1, "Khi chiếu chùm tia laser hẹp qua một khối chất lỏng có nồng độ muối tăng dần theo độ sâu (chiết suất tăng dần từ trên xuống dưới), đường đi của tia laser trong chất lỏng có dạng:", [
        "Một đường cong uốn lõm hướng xuống dưới",
        "Một đường thẳng tắp không đổi hướng",
        "Một đường xoắn ốc khép kín",
        "Bị đứt đoạn từng khúc rời rạc"
    ], 0, "Môi trường có chiết suất biến thiên liên tục làm tia sáng bị khúc xạ liên tiếp tạo thành một đường cong."),
    make_vdc(2, "Bản mặt song song dày d = 3 cm chiết suất n = 1,5 được đặt trong không khí. Khi nhìn một dòng chữ in trên trang sách qua bản mặt song song này theo phương vuông góc, dòng chữ dường như bị nâng lên một đoạn bằng:", [
        "1,0 cm",
        "2,0 cm",
        "0,5 cm",
        "1,5 cm"
    ], 0, "Độ nâng ảnh: Δh = d × (1 - 1/n) = 3 × (1 - 1/1,5) = 3 × (1/3) = 1,0 cm."),
    make_vdc(3, "Để đo góc lệch cực tiểu của một tia sáng qua lăng kính tam giác đều bằng thủy tinh, người ta điều chỉnh góc tới sao cho đường đi của tia sáng bên trong lăng kính:", [
        "Song song với đáy của lăng kính",
        "Vuông góc với đáy của lăng kính",
        "Trùng khít với một cạnh bên của lăng kính",
        "Phản xạ toàn phần trở lại mặt tới"
    ], 0, "Ở góc lệch cực tiểu, đường truyền của tia sáng đối xứng qua mặt phẳng phân giác của góc chiết quang, tức song song với mặt đáy."),
    make_vdc(4, "Một người làm thí nghiệm dùng đèn pin chiếu một chùm sáng hẹp xiên góc vào một cốc nước trà trong suốt. Người đó quan sát thấy chùm tia sáng đi qua mặt phân cách bị gãy khúc rõ rệt. Nếu người đó hòa thêm rất nhiều đường vào cốc nước và khuấy đều thì góc khúc xạ sẽ:", [
        "Giảm bớt đi vì dung dịch đường đặc chiết quang hơn nước tinh khiết",
        "Tăng lên bằng đúng góc tới",
        "Không thay đổi chút nào",
        "Lập tức biến thành góc 90 độ"
    ], 0, "Nước đường đặc có chiết suất lớn hơn nước lọc (chiết quang hơn) nên tia sáng bị bẻ gãy lại gần pháp tuyến hơn, khiến góc khúc xạ r giảm.")
]

exams["phys9_c6_b17_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b17", "Bài 17: Hiện tượng khúc xạ ánh sáng", 3, p1_b17_t3, p2_b17_t3, p3_b17_t3, p4_b17_t3)

print("Added phys9_c6_b17 (3 tests).")
