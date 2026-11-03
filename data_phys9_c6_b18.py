# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 18: HIỆN TƯỢNG PHẢN XẠ TOÀN PHẦN
Bao gồm 3 đề thi độc lập 100%: phys9_c6_b18_test1, phys9_c6_b18_test2, phys9_c6_b18_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c6"
CH_TITLE = "Chương VI: Ánh sáng"

# =============================================================================
# BÀI 18: HIỆN TƯỢNG PHẢN XẠ TOÀN PHẦN (3 ĐỀ)
# =============================================================================

# --- phys9_c6_b18_test1 ---
p1_b18_t1 = [
    make_mc(1, "Nhận biết", "Hiện tượng phản xạ toàn phần là hiện tượng toàn bộ tia sáng tới bị:", [
        "Phản xạ trở lại môi trường trong suốt ban đầu tại mặt phân cách",
        "Khúc xạ truyền thẳng sang môi trường thứ hai",
        "Hấp thụ hoàn toàn bởi môi trường khúc xạ",
        "Tán sắc thành dải bảy màu cầu vồng"
    ], 0, "Hiện tượng toàn bộ tia sáng tới bị phản xạ trở lại môi trường ban đầu gọi là phản xạ toàn phần."),
    make_mc(2, "Nhận biết", "Điều kiện về môi trường truyền ánh sáng để có thể xảy ra hiện tượng phản xạ toàn phần là:", [
        "Ánh sáng truyền từ môi trường kém chiết quang sang môi trường chiết quang hơn",
        "Ánh sáng truyền từ môi trường chiết quang hơn sang môi trường kém chiết quang hơn",
        "Ánh sáng truyền giữa hai môi trường có cùng chiết suất tuyệt đối",
        "Ánh sáng truyền trong môi trường chân không tuyệt đối"
    ], 1, "Điều kiện cần là ánh sáng phải truyền từ môi trường có chiết suất lớn hơn sang môi trường có chiết suất nhỏ hơn (n1 > n2)."),
    make_mc(3, "Nhận biết", "Điều kiện về góc tới i để xảy ra hiện tượng phản xạ toàn phần là:", [
        "Góc tới i phải nhỏ hơn góc giới hạn phản xạ toàn phần",
        "Góc tới i phải bằng đúng 0 độ",
        "Góc tới i phải lớn hơn hoặc bằng góc giới hạn phản xạ toàn phần (i >= igh)",
        "Góc tới i phải bằng 90 độ"
    ], 2, "Điều kiện đủ là góc tới i ≥ igh."),
    make_mc(4, "Nhận biết", "Công thức xác định góc giới hạn phản xạ toàn phần igh khi ánh sáng truyền từ môi trường chiết suất n sang không khí là:", [
        "cos igh = n",
        "tan igh = 1 / n",
        "sin igh = n",
        "sin igh = 1 / n"
    ], 3, "sin igh = n2 / n1 = 1 / n (vì không khí có n2 ≈ 1)."),
    make_mc(5, "Nhận biết", "Khi góc tới i đúng bằng góc giới hạn phản xạ toàn phần igh thì tia khúc xạ có đặc điểm là:", [
        "Đi là là sát mặt phân cách giữa hai môi trường (góc khúc xạ r = 90 độ)",
        "Truyền vuông góc với mặt phân cách giữa hai môi trường",
        "Bị quay ngược trở lại phương truyền ban đầu",
        "Lập tức biến mất hoàn toàn không để lại vết tích"
    ], 0, "Khi i = igh thì tia khúc xạ đi là là sát mặt phân cách (r = 90°)."),
    make_mc(6, "Nhận biết", "Khi xảy ra hiện tượng phản xạ toàn phần, cường độ sáng của chùm tia phản xạ so với chùm tia tới là:", [
        "Nhỏ hơn rất nhiều do năng lượng bị thất thoát",
        "Gần như bằng 100% cường độ chùm tia tới",
        "Chỉ bằng khoảng 50% cường độ chùm tia tới",
        "Luôn luôn bằng 0"
    ], 1, "Toàn bộ năng lượng ánh sáng được phản xạ lại nên cường độ phản xạ đạt xấp xỉ 100%."),
    make_mc(7, "Thông hiểu", "Sợi quang dùng trong đường truyền internet tốc độ cao hoạt động dựa trên ứng dụng của hiện tượng nào?", [
        "Hiện tượng khúc xạ ánh sáng đơn thuần",
        "Hiện tượng tán sắc ánh sáng trắng",
        "Hiện tượng phản xạ toàn phần của ánh sáng trong lõi sợi quang",
        "Hiện tượng giao thoa ánh sáng laser"
    ], 2, "Cáp quang hoạt động dựa trên hiện tượng phản xạ toàn phần liên tiếp bên trong lõi sợi quang."),
    make_mc(8, "Thông hiểu", "Biết góc giới hạn phản xạ toàn phần từ nước ra không khí là khoảng 48,5 độ. Chiếu một tia sáng từ đáy bể nước lên mặt nước với góc tới 55 độ thì:", [
        "Tia sáng khúc xạ ra ngoài không khí với góc 90 độ",
        "Tia sáng bị gãy khúc và đi vào không khí bình thường",
        "Tia sáng bị hấp thụ hoàn toàn tại mặt nước",
        "Tia sáng bị phản xạ toàn phần trở lại trong nước"
    ], 3, "Vì i = 55° > igh = 48,5° và truyền từ nước ra không khí (n1 > n2) nên xảy ra phản xạ toàn phần."),
    make_mc(9, "Thông hiểu", "Trong kỹ thuật nội soi y học, thiết bị nội soi có thể luồn sâu vào dạ dày bệnh nhân để truyền hình ảnh ra màn hình ngoài là nhờ:", [
        "Chùm sợi quang mềm dẻo truyền dẫn ánh sáng bằng phản xạ toàn phần",
        "Hệ thống gương phẳng truyền thống cồng kềnh",
        "Tia X phát ra từ đầu dò",
        "Sóng siêu âm tần số cực cao"
    ], 0, "Bó sợi quang học mềm mại giúp truyền ánh sáng soi sáng và dẫn hình ảnh ra ngoài nhờ phản xạ toàn phần."),
    make_mc(10, "Thông hiểu", "Kim cương tự nhiên sau khi được thợ kim hoàn mài cắt khéo léo sẽ trở nên lấp lánh rực rỡ dưới ánh sáng. Nguyên nhân vật lý cốt lõi là do:", [
        "Kim cương có chiết suất rất lớn dẫn đến góc giới hạn rất nhỏ, ánh sáng vào trong dễ phản xạ toàn phần nhiều lần",
        "Kim cương tự phát ra ánh sáng huỳnh quang trong bóng tối",
        "Kim cương dẫn nhiệt và dẫn điện rất tốt",
        "Kim cương hấp thụ toàn bộ tia hồng ngoại"
    ], 0, "n kim cương ≈ 2,42 nên igh ≈ 24,5° rất nhỏ, ánh sáng vào trong bị phản xạ toàn phần liên tiếp trước khi ló ra ở các mặt đỉnh."),
    make_mc(11, "Thông hiểu", "Lăng kính phản xạ toàn phần là một khối thủy tinh trong suốt có tiết diện thẳng là:", [
        "Tam giác đều có ba góc bằng 60 độ",
        "Tam giác vuông cân có một góc vuông và hai góc bằng 45 độ",
        "Hình thang cân",
        "Hình chữ nhật phẳng"
    ], 1, "Lăng kính phản xạ toàn phần thường có tiết diện là tam giác vuông cân."),
    make_mc(12, "Thông hiểu", "Vào những ngày hè nắng gắt, người lái xe trên đường nhựa nhìn thấy phía xa dường như có vũng nước loang loáng phản chiếu bầu trời. Hiện tượng ảo ảnh này sinh ra do:", [
        "Mặt đường nhựa bị rò rỉ nước từ lòng đất",
        "Tầng không khí sát mặt đường bị hun nóng rất mạnh làm chiết suất giảm, gây phản xạ toàn phần ánh sáng bầu trời",
        "Mắt người lái xe bị lóa bởi ánh sáng đèn pha",
        "Bụi bẩn trên kính chắn gió tạo ảo giác"
    ], 1, "Lớp không khí sát mặt đường nóng hơn nên loãng hơn (chiết suất nhỏ hơn), ánh sáng truyền từ trên xuống gặp lớp không khí này bị phản xạ toàn phần.")
]

p2_b18_t1 = [
    make_tf(1, "Thông hiểu", "Xét các khẳng định về điều kiện xảy ra hiện tượng phản xạ toàn phần:", [
        ("a", "Hiện tượng phản xạ toàn phần chỉ xảy ra khi ánh sáng truyền từ môi trường chiết quang hơn sang môi trường kém chiết quang hơn.", True),
        ("b", "Khi tia sáng truyền từ không khí vào thủy tinh, có thể xảy ra phản xạ toàn phần nếu góc tới đủ lớn.", False),
        ("c", "Góc giới hạn phản xạ toàn phần phụ thuộc vào chiết suất của hai môi trường tiếp xúc.", True),
        ("d", "Khi xảy ra hiện tượng phản xạ toàn phần thì không còn tia khúc xạ đi vào môi trường thứ hai.", True)
    ], "Không khí sang thủy tinh là từ kém sang hơn nên không thể xảy ra phản xạ toàn phần."),
    make_tf(2, "Thông hiểu", "Cấu tạo và hoạt động của sợi quang học trong viễn thông:", [
        ("a", "Sợi quang gồm phần lõi ở giữa và phần vỏ bọc bên ngoài.", True),
        ("b", "Chiết suất của phần lõi phải nhỏ hơn chiết suất của lớp vỏ bọc.", False),
        ("c", "Tín hiệu ánh sáng truyền trong lõi sợi quang nhờ hiện tượng phản xạ toàn phần liên tục tại mặt phân cách lõi - vỏ.", True),
        ("d", "Cáp quang truyền tín hiệu ít bị suy hao và không bị ảnh hưởng bởi nhiễu sóng điện từ.", True)
    ], "Chiết suất của phần lõi bắt buộc phải lớn hơn chiết suất của phần vỏ bọc để xảy ra phản xạ toàn phần."),
    make_tf(3, "Vận dụng", "Chiếu một tia sáng từ khối thủy tinh có chiết suất n = 1,5 ra không khí. Biết góc giới hạn phản xạ toàn phần của thủy tinh là igh ≈ 42 độ:", [
        ("a", "Nếu góc tới i = 30 độ thì vừa có tia phản xạ vừa có tia khúc xạ ra không khí.", True),
        ("b", "Nếu góc tới i = 42 độ thì tia khúc xạ đi là là sát mặt phân cách.", True),
        ("c", "Nếu góc tới i = 50 độ thì toàn bộ tia sáng bị phản xạ trở lại khối thủy tinh.", True),
        ("d", "Khi góc tới i = 50 độ thì góc phản xạ bằng 40 độ.", False)
    ], "Theo định luật phản xạ ánh sáng, góc phản xạ luôn bằng góc tới: i' = i = 50°."),
    make_tf(4, "Vận dụng", "Ứng dụng của phản xạ toàn phần trong các dụng cụ quang học:", [
        ("a", "Kính tiềm vọng trong tàu ngầm có thể dùng hai lăng kính phản xạ toàn phần để đổi hướng tia sáng.", True),
        ("b", "Lăng kính phản xạ toàn phần có độ phản xạ tốt hơn gương phẳng tráng bạc vì không bị bong tróc lớp tráng bạc.", True),
        ("c", "Ống nhòm Porro dùng hệ lăng kính phản xạ toàn phần để đảo chiều hình ảnh thuận chiều mắt nhìn.", True),
        ("d", "Kính lúp cầm tay hoạt động hoàn toàn dựa trên hiện tượng phản xạ toàn phần.", False)
    ], "Kính lúp là thấu kính hội tụ, tạo ảnh dựa trên hiện tượng khúc xạ ánh sáng chứ không phải phản xạ toàn phần.")
]

p3_b18_t1 = [
    make_sa(1, "Thông hiểu", "Chiếu ánh sáng từ nước ra không khí có góc giới hạn phản xạ toàn phần igh = 48,5 độ. Nếu góc tới là 55 độ thì có xảy ra hiện tượng phản xạ toàn phần không? (Trả lời: Có hoặc Không)", "Có", "Vì i = 55° > igh = 48,5° nên có xảy ra phản xạ toàn phần."),
    make_sa(2, "Thông hiểu", "Chiếu một tia sáng từ chất lỏng ra không khí với góc tới i đúng bằng góc giới hạn phản xạ toàn phần. Khi đó góc khúc xạ r bằng bao nhiêu độ?", "90", "Tại góc giới hạn thì r = 90°."),
    make_sa(3, "Vận dụng", "Một tia sáng truyền từ một khối nhựa trong suốt ra không khí với góc tới 52 độ và bị phản xạ toàn phần. Góc phản xạ của tia sáng đó bằng bao nhiêu độ?", "52", "Góc phản xạ bằng góc tới: i' = i = 52°."),
    make_sa(4, "Vận dụng", "Chiết suất của một chất lỏng trong suốt là n = 2. Góc giới hạn phản xạ toàn phần khi chiếu ánh sáng từ chất lỏng này ra không khí bằng bao nhiêu độ? (Biết sin 30° = 0,5)", "30", "sin igh = 1/n = 1/2 = 0,5 => igh = 30°."),
    make_sa(5, "Vận dụng cao", "Một lăng kính phản xạ toàn phần bằng thủy tinh có tiết diện là tam giác vuông cân ABC vuông tại A. Chiếu một tia sáng vuông góc với mặt bên AB vào trong lăng kính. Khi gặp mặt huyền BC, góc tới của tia sáng tại mặt huyền bằng bao nhiêu độ?", "45", "Tia sáng truyền thẳng qua AB đến BC, pháp tuyến tại BC tạo với AB góc 45° nên góc tới là 45°."),
    make_sa(6, "Vận dụng cao", "Một sợi quang có chiết suất lõi n1 = 1,50 và chiết suất vỏ n2 = 1,41. Giá trị sin của góc giới hạn phản xạ toàn phần tại mặt phân cách giữa lõi và vỏ bằng bao nhiêu? (Làm tròn đến 2 chữ số thập phân)", "0.94", "sin igh = n2 / n1 = 1,41 / 1,50 = 0,94.")
]

p4_b18_t1 = [
    make_vdc(1, "Tại sao trong các thiết bị ngắm quang học chuyên dụng của quân sự (như kính tiềm vọng tàu ngầm, ống nhòm cao cấp), người ta ưu tiên dùng lăng kính phản xạ toàn phần thay thế cho gương phẳng tráng bạc kim loại thông thường?", [
        "Lăng kính phản xạ toàn phần có hệ số phản xạ gần 100%, không bị ố mờ hay trầy xước theo thời gian và không tạo ảnh kép",
        "Lăng kính nhẹ hơn và giá thành rẻ hơn gương phẳng rất nhiều",
        "Lăng kính có thể tự phóng to hình ảnh gấp hàng trăm lần",
        "Gương tráng bạc kim loại làm lệch màu ánh sáng hoàn toàn"
    ], 0, "Lăng kính phản xạ toàn phần đạt hiệu suất phản xạ gần 100%, bền bỉ tuyệt đối trong môi trường khắc nghiệt và triệt tiêu ảnh phụ."),
    make_vdc(2, "Ảo ảnh trên mặt sa mạc khô nóng (Fata Morgana hay Mirage): Người đi trên sa mạc thường nhìn thấy phía trước có ảo ảnh hồ nước trong xanh in bóng cảnh vật. Giải thích cơ chế quang học của hiện tượng này:", [
        "Ánh sáng từ bầu trời và ngọn cây đi xuống gặp lớp không khí sát mặt cát có nhiệt độ rất cao và chiết suất nhỏ dần, bị bẻ cong liên tục rồi phản xạ toàn phần đi lên mắt người quan sát",
        "Mặt cát sa mạc chứa nhiều tinh thể thạch anh phản chiếu ánh sáng như gương soi",
        "Hơi nước bốc lên từ lòng đất sa mạc ngưng tụ thành gương phẳng tự nhiên",
        "Hiện tượng giao thoa ánh sáng mặt trời qua lớp cát bay"
    ], 0, "Lớp không khí sát mặt đất bị nóng làm giảm khối lượng riêng và chiết suất, tia sáng đi xuống bị khúc xạ liên tiếp xa dần pháp tuyến cho đến khi i ≥ igh thì phản xạ toàn phần ngược lên mắt."),
    make_vdc(3, "Cáp quang viễn thông xuyên đại dương được thiết kế với nhiều lớp bảo vệ, nhưng phần truyền tải tín hiệu chính là sợi thủy tinh có đường kính chỉ bằng sợi tóc. Tại sao tín hiệu ánh sáng có thể truyền đi hàng nghìn kilômét mà năng lượng thất thoát cực kỳ thấp?", [
        "Nhờ hiện tượng phản xạ toàn phần liên tục tại mặt phân cách giữa lõi có chiết suất cao và vỏ có chiết suất thấp, giữ toàn bộ chùm sáng bên trong lõi",
        "Do ánh sáng laser không mang năng lượng nên không thể bị tiêu hao",
        "Do đáy biển rất lạnh làm tăng năng lượng của ánh sáng",
        "Do sợi quang được bọc bằng vàng nguyên chất ngăn ánh sáng thoát ra"
    ], 0, "Phản xạ toàn phần giúp giam giữ các xung photon ánh sáng bên trong lõi sợi quang siêu tinh khiết trên suốt hành trình truyền dẫn."),
    make_vdc(4, "Một viên kim cương thô chưa mài giũa trông mờ đục và kém lấp lánh như viên đá cuội thông thường. Sau khi được các nghệ nhân mài giũa thành hình đa diện tiêu chuẩn 57 - 58 mặt giác (kiểu cắt Brilliant), viên kim cương phát ra ánh sáng lung linh rực rỡ dưới mọi góc nhìn. Yếu tố vật lý mang tính quyết định là:", [
        "Các góc cắt mặt đáy và mặt bên được tính toán chuẩn xác sao cho phần lớn ánh sáng đi vào đều bị phản xạ toàn phần nhiều lần và ló ra ở mặt trên",
        "Mặt cắt kim cương phản xạ ánh sáng như các thấu kính phân kì",
        "Thợ kim hoàn phủ một lớp huỳnh quang nhân tạo lên bề mặt giác cắt",
        "Kim cương bị nén ở áp suất cực cao tạo ra nhiệt năng phát sáng"
    ], 0, "Thiết kế góc cắt chuẩn xác tận dụng triệt để góc giới hạn cực nhỏ của kim cương (igh ≈ 24,5°) để phản xạ toàn phần ánh sáng về phía mắt người xem.")
]

exams["phys9_c6_b18_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b18", "Bài 18: Hiện tượng phản xạ toàn phần", 1, p1_b18_t1, p2_b18_t1, p3_b18_t1, p4_b18_t1)

# --- phys9_c6_b18_test2 ---
p1_b18_t2 = [
    make_mc(1, "Nhận biết", "Trong hiện tượng phản xạ toàn phần, góc phản xạ r' và góc tới i có mối quan hệ như thế nào?", [
        "Góc phản xạ r' bằng góc tới i",
        "Góc phản xạ r' lớn hơn góc tới i",
        "Góc phản xạ r' luôn bằng 90 độ",
        "Góc phản xạ r' nhỏ hơn góc tới i"
    ], 0, "Theo định luật phản xạ ánh sáng, góc phản xạ luôn bằng góc tới: r' = i."),
    make_mc(2, "Nhận biết", "Trường hợp nào sau đây KHÔNG THỂ xảy ra hiện tượng phản xạ toàn phần?", [
        "Tia sáng truyền từ không khí vào khối thủy tinh trong suốt",
        "Tia sáng truyền từ nước ra ngoài không khí",
        "Tia sáng truyền từ kim cương ra ngoài không khí",
        "Tia sáng truyền từ thủy tinh vào trong nước"
    ], 0, "Không khí có chiết suất nhỏ hơn thủy tinh (n1 < n2) nên không thỏa mãn điều kiện n1 > n2, do đó không thể có phản xạ toàn phần."),
    make_mc(3, "Nhận biết", "Góc giới hạn phản xạ toàn phần giữa môi trường 1 (chiết suất n1) và môi trường 2 (chiết suất n2 với n1 > n2) được xác định bằng công thức:", [
        "cos igh = n2 / n1",
        "sin igh = n2 / n1",
        "tan igh = n1 / n2",
        "sin igh = n1 / n2"
    ], 1, "sin igh = n2 / n1 (với n1 > n2)."),
    make_mc(4, "Nhận biết", "Khi tia sáng truyền từ nước ra không khí, nếu góc tới i < igh thì tại mặt phân cách:", [
        "Chỉ có hiện tượng phản xạ ánh sáng",
        "Chỉ có hiện tượng khúc xạ ánh sáng",
        "Xảy ra đồng thời cả hiện tượng phản xạ và hiện tượng khúc xạ",
        "Tia sáng bị triệt tiêu hoàn toàn"
    ], 2, "Khi i < igh thì có cả tia phản xạ (một phần) và tia khúc xạ đi ra ngoài không khí."),
    make_mc(5, "Nhận biết", "Góc giới hạn phản xạ toàn phần của một chất trong suốt đối với không khí càng nhỏ khi chất đó có:", [
        "Khối lượng riêng càng nhỏ",
        "Độ trong suốt càng thấp",
        "Chiết suất tuyệt đối càng nhỏ",
        "Chiết suất tuyệt đối càng lớn"
    ], 3, "sin igh = 1/n nên khi n càng lớn thì sin igh càng nhỏ, tức là góc giới hạn igh càng nhỏ."),
    make_mc(6, "Nhận biết", "Lớp vỏ bọc của sợi cáp quang có tác dụng chính là:", [
        "Dẫn điện cho sợi quang",
        "Tạo môi trường kém chiết quang hơn phần lõi để giữ ánh sáng phản xạ toàn phần trong lõi",
        "Tản nhiệt cho sợi quang",
        "Hấp thụ sóng radio ngoài môi trường"
    ], 1, "Lớp vỏ bọc có n2 < n1 giúp giữ ánh sáng truyền trong lõi bằng phản xạ toàn phần."),
    make_mc(7, "Thông hiểu", "Một bọt khí nằm trong một khối thủy tinh trong suốt, khi được chiếu sáng từ phía ngoài, bọt khí trông lấp lánh như một giọt thủy ngân bạc. Hiện tượng này là do:", [
        "Ánh sáng truyền trong thủy tinh gặp bề mặt tiếp xúc với bọt khí bị phản xạ toàn phần",
        "Bọt khí chứa kim loại thủy ngân lỏng",
        "Khí bên trong bọt khí bị bốc cháy phát sáng",
        "Thủy tinh tự phát quang tại các lỗ rỗng"
    ], 0, "Ánh sáng từ thủy tinh sang không khí trong bọt khí gặp mặt phân cách với góc i ≥ igh bị phản xạ toàn phần trở lại mắt."),
    make_mc(8, "Thông hiểu", "Chiếu tia sáng từ một chất lỏng trong suốt ra không khí. Khi góc tới tăng từ 30 độ lên 60 độ thì thấy tia khúc xạ ló ra không khí bị lệch dần về sát mặt nước rồi biến mất ở góc tới 45 độ. Góc giới hạn phản xạ toàn phần của chất lỏng này là:", [
        "30 độ",
        "45 độ",
        "60 độ",
        "90 độ"
    ], 1, "Góc tới mà tại đó tia khúc xạ vừa vặn biến mất chính là góc giới hạn: igh = 45°."),
    make_mc(9, "Thông hiểu", "Đèn trang trí sợi quang nhiều màu thường thấy ở các đài phun nước hoặc cây thông Noel phát ra các đốm sáng lung linh chủ yếu ở:", [
        "Đoạn giữa của các sợi quang",
        "Đầu mút của các sợi quang",
        "Toàn bộ bề mặt thân sợi quang",
        "Chân đế cắm nguồn điện"
    ], 1, "Ánh sáng được dẫn trong sợi quang nhờ phản xạ toàn phần nên không lọt qua thành sợi mà chỉ phát ra ở hai đầu mút."),
    make_mc(10, "Thông hiểu", "Chiếu một tia sáng đơn sắc từ môi trường có chiết suất n = căn bậc hai của 2 (xấp xỉ 1,414) ra không khí. Góc giới hạn phản xạ toàn phần của môi trường này là:", [
        "30 độ",
        "60 độ",
        "45 độ",
        "90 độ"
    ], 2, "sin igh = 1 / √2 => igh = 45°."),
    make_mc(11, "Thông hiểu", "So với dây cáp đồng truyền thống truyền tín hiệu điện, cáp quang truyền tín hiệu internet có ưu điểm vượt trội nào sau đây?", [
        "Dễ bị nhiễu do từ trường của dây điện cao thế",
        "Dung lượng đường truyền cực lớn, tốc độ truyền cao và không bị suy hao bức xạ điện từ",
        "Cáp quang rất nặng và cồng kềnh",
        "Cáp quang dễ bị rỉ sét trong môi trường ẩm ướt"
    ], 1, "Cáp quang truyền tín hiệu photon có băng thông rộng, tốc độ cao và miễn nhiễm với can nhiễu điện từ."),
    make_mc(12, "Thông hiểu", "Hiện tượng váng dầu hoặc giọt nước đọng trên lá cây sen lấp lánh như viên ngọc dưới ánh mặt trời buổi sớm là do:", [
        "Sự phản xạ toàn phần của ánh sáng tại mặt tiếp xúc giữa giọt nước và lớp không khí mỏng phía dưới",
        "Lá sen tự phát quang vào ban ngày",
        "Giọt nước bị ion hóa thành plasma",
        "Hiện tượng phóng điện tĩnh trên bề mặt lá"
    ], 0, "Lớp lông nhung vi mô trên lá sen giữ một lớp đệm không khí dưới giọt nước, ánh sáng đi vào giọt nước bị phản xạ toàn phần tại mặt tiếp xúc này tạo ánh lấp lánh.")
]

p2_b18_t2 = [
    make_tf(1, "Thông hiểu", "So sánh giữa phản xạ thông thường và hiện tượng phản xạ toàn phần:", [
        ("a", "Hiện tượng phản xạ thông thường xảy ra tại bề mặt ngăn cách của bất kì môi trường nào.", True),
        ("b", "Hiện tượng phản xạ toàn phần chỉ xảy ra khi thỏa mãn đồng thời hai điều kiện về môi trường và góc tới.", True),
        ("c", "Trong phản xạ thông thường, luôn có một phần năng lượng ánh sáng bị khúc xạ hoặc hấp thụ.", True),
        ("d", "Hệ số phản xạ của gương tráng bạc thông thường lớn hơn hệ số phản xạ toàn phần của lăng kính thủy tinh.", False)
    ], "Lăng kính phản xạ toàn phần phản xạ xấp xỉ 100% ánh sáng tới, cao hơn gương tráng bạc thông thường (~90-95%)."),
    make_tf(2, "Thông hiểu", "Về cáp quang truyền thông tin viễn thông:", [
        ("a", "Lõi sợi quang được làm bằng thủy tinh silica siêu tinh khiết.", True),
        ("b", "Lớp vỏ sợi quang có chiết suất nhỏ hơn phần lõi để thỏa mãn điều kiện n1 > n2.", True),
        ("c", "Khi truyền qua các đoạn uốn cong vừa phải, ánh sáng vẫn tiếp tục phản xạ toàn phần bên trong lõi.", True),
        ("d", "Nếu bẻ gập sợi quang một góc 90 độ thật gấp thì tín hiệu ánh sáng vẫn truyền qua không hề suy giảm.", False)
    ], "Nếu bẻ gập sợi quang quá gấp, góc tới tại thành sợi sẽ nhỏ hơn góc giới hạn igh làm ánh sáng thoát ra ngoài gây đứt tín hiệu."),
    make_tf(3, "Vận dụng", "Chiếu tia sáng từ một khối nhựa trong suốt (n = 1,414 ≈ √2) ra không khí:", [
        ("a", "Góc giới hạn phản xạ toàn phần của khối nhựa này là igh = 45 độ.", True),
        ("b", "Nếu chiếu với góc tới i = 30 độ thì tia khúc xạ đi ra không khí với góc khúc xạ r = 45 độ.", True),
        ("c", "Nếu chiếu với góc tới i = 60 độ thì toàn bộ tia sáng bị phản xạ trở lại với góc phản xạ 60 độ.", True),
        ("d", "Nếu chiếu với góc tới i = 45 độ thì không còn tia sáng nào truyền đi sát mặt phân cách.", False)
    ], "Tại i = 45° = igh, tia khúc xạ đi là là sát mặt phân cách (r = 90°)."),
    make_tf(4, "Vận dụng", "Ứng dụng của phản xạ toàn phần trong đời sống và kỹ thuật:", [
        ("a", "Thiết bị cảm biến gạt nước mưa tự động trên ô tô ứng dụng sự thay đổi phản xạ toàn phần khi có nước mưa bám vào kính.", True),
        ("b", "Kính tiềm vọng trong tàu ngầm dùng lăng kính phản xạ toàn phần giúp quan sát mục tiêu trên mặt biển an toàn.", True),
        ("c", "Đèn pha ô tô dùng hiện tượng phản xạ toàn phần để tạo chùm sáng song song rọi xa.", False),
        ("d", "Ống nội soi quang học mềm dùng trong bệnh viện ứng dụng chùm sợi quang phản xạ toàn phần.", True)
    ], "Đèn pha ô tô dùng gương cầu lõm (hoặc chóa parabol) phản xạ ánh sáng từ bóng đèn đặt tại tiêu điểm, không phải phản xạ toàn phần.")
]

p3_b18_t2 = [
    make_sa(1, "Thông hiểu", "Góc giới hạn phản xạ toàn phần từ thủy tinh ra không khí là 42 độ. Chiếu một tia sáng từ thủy tinh ra không khí với góc tới 40 độ thì có xảy ra hiện tượng phản xạ toàn phần không? (Trả lời: Có hoặc Không)", "Không", "Góc tới i = 40° < igh = 42° nên chưa xảy ra phản xạ toàn phần."),
    make_sa(2, "Thông hiểu", "Chiếu một tia sáng từ chất lỏng ra không khí với góc tới 60 độ. Biết góc giới hạn là 50 độ. Góc phản xạ của tia sáng bằng bao nhiêu độ?", "60", "Xảy ra phản xạ toàn phần nên góc phản xạ i' = i = 60°."),
    make_sa(3, "Vận dụng", "Biết chiết suất của một khối thủy tinh đối với ánh sáng là n = 2. Tính góc giới hạn phản xạ toàn phần khi chiếu tia sáng từ khối thủy tinh này ra không khí theo độ?", "30", "sin igh = 1/2 => igh = 30°."),
    make_sa(4, "Vận dụng", "Một tia sáng truyền từ nước ra không khí. Góc giới hạn phản xạ toàn phần là 48,5 độ. Góc tới lớn nhất để tia sáng vẫn còn khúc xạ thoát ra ngoài không khí là bao nhiêu độ?", "48.5", "Khi i = 48,5° thì tia khúc xạ đi là là sát mặt nước (r = 90°)."),
    make_sa(5, "Vận dụng cao", "Một sợi quang có chiết suất lõi là 1,6 và chiết suất vỏ là 1,44. Tính giá trị sin của góc giới hạn phản xạ toàn phần tại mặt phân cách lõi - vỏ?", "0.9", "sin igh = 1,44 / 1,6 = 0,9."),
    make_sa(6, "Vận dụng cao", "Một lăng kính phản xạ toàn phần làm bằng thủy tinh có tiết diện là tam giác vuông cân ABC vuông tại A. Một tia sáng chiếu vuông góc vào mặt bên AB, phản xạ toàn phần tại mặt huyền BC và ló ra vuông góc ở mặt bên AC. Góc lệch giữa tia ló và tia tới bằng bao nhiêu độ?", "90", "Tia tới truyền thẳng vào AB, tại BC bị quay góc 90° rồi ló vuông góc ra AC. Do đó góc lệch là 90°.")
]

p4_b18_t2 = [
    make_vdc(1, "Nguyên lý cảm biến gạt mưa tự động trên kính chắn gió ô tô hiện đại: Một cảm biến phát tia hồng ngoại chiếu xiên vào mặt trong kính chắn gió với góc tới 45 độ (lớn hơn góc giới hạn của kính ra không khí là 42 độ). Khi kính chắn gió khô ráo, hiện tượng gì xảy ra với tia hồng ngoại?", [
        "Tia hồng ngoại bị phản xạ toàn phần 100% tại mặt ngoài kính chắn gió và đi thẳng vào đầu thu cảm biến",
        "Tia hồng ngoại truyền thẳng ra ngoài không gian phía trước xe",
        "Tia hồng ngoại bị mặt kính hấp thụ hoàn toàn thành nhiệt",
        "Tia hồng ngoại bị tán xạ thành chùm ánh sáng nhìn thấy nhiều màu"
    ], 0, "Khi khô ráo, i = 45° > igh = 42° nên phản xạ toàn phần hoàn toàn vào đầu thu; khi có nước mưa bám vào ngoài, chiết suất tăng làm ánh sáng khúc xạ thoát ra ngoài, kích hoạt gạt mưa."),
    make_vdc(2, "Cửa sổ Snell của thợ lặn dưới nước: Một thợ lặn đang ở độ sâu 2 m dưới hồ nước phẳng lặng nhìn lên mặt nước vào ban ngày sẽ thấy toàn bộ thế giới trên mặt nước co cụm lại trong một hình nón có góc mở bằng bao nhiêu độ?", [
        "Khoảng 97 độ (hai lần góc giới hạn 48,5 độ)",
        "Khoảng 180 độ phẳng tuyệt đối",
        "Đúng 45 độ",
        "Đúng 360 độ hình cầu"
    ], 0, "Tia sáng từ khắp không gian 180° trên không khi vào nước bị khúc xạ trong nón góc giới hạn igh = 48,5°, góc mở của hình nón là 2 × 48,5° = 97°."),
    make_vdc(3, "Ống nhòm hai mắt quân sự sử dụng hệ lăng kính phản xạ toàn phần Porro (gồm 2 lăng kính vuông cân đặt vuông góc nhau cho mỗi bên mắt). Mục đích chính của hệ lăng kính này là:", [
        "Đảo ngược hình ảnh ngược chiều (từ vật kính) thành hình ảnh thuận chiều mắt nhìn và kéo dài đường đi ánh sáng trong thân ống nhòm ngắn gọn",
        "Tăng độ sáng của hình ảnh lên gấp mười lần",
        "Lọc bỏ hoàn toàn ánh sáng ban đêm để biến thành kính nhìn đêm",
        "Bảo vệ mắt người dùng khỏi tia laser chiếu thẳng"
    ], 0, "Hệ lăng kính Porro đảo ngược ảnh từ trên xuống dưới và từ trái qua phải, cho ảnh thuận chiều và giúp thu ngắn chiều dài thân ống nhòm."),
    make_vdc(4, "Một kỹ sư thiết kế hệ thống chiếu sáng dẫn ánh sáng mặt trời từ trên mái nhà xuống các phòng tầng hầm không có cửa sổ bằng các ống dẫn sáng quang học. Để hạn chế tối đa suy hao ánh sáng qua các góc cua trong tòa nhà, giải pháp tối ưu nhất là:", [
        "Sử dụng ống dẫn phủ màng quang học phản xạ toàn phần bên trong lòng ống",
        "Sử dụng bóng đèn sợi đốt công suất lớn thắp liên tục",
        "Dùng ống nhựa đục màu đen để giữ ánh sáng",
        "Mở quạt thông gió công suất lớn để hút ánh sáng xuống"
    ], 0, "Ống dẫn sáng ứng dụng phản xạ toàn phần dẫn ánh sáng tự nhiên đi qua nhiều khúc cua mà không bị thất thoát quang năng.")
]

exams["phys9_c6_b18_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b18", "Bài 18: Hiện tượng phản xạ toàn phần", 2, p1_b18_t2, p2_b18_t2, p3_b18_t2, p4_b18_t2)

# --- phys9_c6_b18_test3 ---
p1_b18_t3 = [
    make_mc(1, "Nhận biết", "Trong các cặp môi trường sau, hiện tượng phản xạ toàn phần CHỈ có thể xảy ra khi ánh sáng truyền từ:", [
        "Thủy tinh sang không khí",
        "Không khí vào nước",
        "Chân không vào kim cương",
        "Không khí vào khối nhựa trong suốt"
    ], 0, "Phản xạ toàn phần chỉ xảy ra khi truyền từ môi trường chiết quang hơn sang kém hơn: thủy tinh (n ≈ 1,5) sang không khí (n ≈ 1)."),
    make_mc(2, "Nhận biết", "Khi ánh sáng truyền từ một môi trường trong suốt có chiết suất n ra không khí, góc giới hạn phản xạ toàn phần igh phụ thuộc vào:", [
        "Chiết suất n của môi trường trong suốt đó",
        "Cường độ của chùm sáng chiếu tới",
        "Diện tích bề mặt phân cách giữa hai môi trường",
        "Nhiệt độ của không khí xung quanh"
    ], 0, "sin igh = 1/n, do đó góc giới hạn chỉ phụ thuộc vào chiết suất của môi trường."),
    make_mc(3, "Nhận biết", "Khi xảy ra hiện tượng phản xạ toàn phần, góc tới i và góc phản xạ r' thỏa mãn điều kiện:", [
        "i >= igh và r' = i",
        "i < igh và r' = 90 độ",
        "i = 0 độ và r' = 180 độ",
        "i >= igh và r' = 2i"
    ], 0, "Điều kiện phản xạ toàn phần là i ≥ igh và theo định luật phản xạ r' = i."),
    make_mc(4, "Nhận biết", "Khi chiếu tia sáng từ thủy tinh ra không khí, nếu tăng dần góc tới i từ 0 độ đến 90 độ thì cường độ chùm tia khúc xạ ló ra ngoài không khí sẽ:", [
        "Giảm dần và biến mất hoàn toàn khi i >= igh",
        "Tăng dần liên tục đến vô cực",
        "Không đổi và luôn bằng cường độ tia tới",
        "Bị đổi màu từ đỏ sang tím"
    ], 0, "Càng tăng góc tới, tia phản xạ càng sáng dần, còn tia khúc xạ yếu dần và biến mất khi i ≥ igh."),
    make_mc(5, "Nhận biết", "Vật liệu thường dùng làm lõi của sợi cáp quang viễn thông hiện nay là:", [
        "Thủy tinh silica hoặc nhựa quang học có độ tinh khiết cực cao",
        "Kim loại đồng nguyên chất kéo sợi",
        "Hợp kim nhôm siêu nhẹ",
        "Sợi than chì dẫn điện tốt"
    ], 0, "Lõi cáp quang làm bằng silica thủy tinh độ tinh khiết cao để giảm thiểu hấp thụ ánh sáng."),
    make_mc(6, "Nhận biết", "Lăng kính phản xạ toàn phần được ứng dụng rộng rãi trong thiết bị nào sau đây?", [
        "Ống nhòm hai mắt và kính tiềm vọng",
        "Bình nóng lạnh gia đình",
        "Bếp từ nấu ăn",
        "Máy đo huyết áp điện tử"
    ], 0, "Lăng kính phản xạ toàn phần dùng trong ống nhòm, kính tiềm vọng, máy ảnh phản xạ ống kính đơn (DSLR)."),
    make_mc(7, "Thông hiểu", "Một tia sáng truyền từ một khối thủy tinh (n = 1,5) ra không khí với góc tới i = 45 độ. Biết góc giới hạn của thủy tinh là igh = 42 độ. Hiện tượng quan sát được tại mặt phân cách là:", [
        "Tia sáng bị phản xạ toàn phần trở lại thủy tinh với góc phản xạ 45 độ",
        "Tia sáng khúc xạ ra không khí với góc khúc xạ 90 độ",
        "Tia sáng truyền thẳng tiếp tục ra không khí",
        "Tia sáng bị gãy khúc lệch lại gần pháp tuyến"
    ], 0, "Vì i = 45° > igh = 42° nên toàn bộ tia sáng bị phản xạ toàn phần với r' = 45°."),
    make_mc(8, "Thông hiểu", "Một chiếc đĩa nhựa tròn mỏng có gắn một nguồn sáng nhỏ ở tâm đĩa được thả nổi trên mặt nước trong bể bơi. Để không có bất kỳ tia sáng nào lọt từ nguồn qua mặt nước ra không khí thì bán kính tối thiểu của đĩa phụ thuộc vào:", [
        "Độ sâu của nguồn sáng dưới nước và góc giới hạn phản xạ toàn phần của nước",
        "Màu sắc sơn của chiếc đĩa nhựa",
        "Nhiệt độ sôi của nước trong bể bơi",
        "Độ dày của thành bể bơi"
    ], 0, "Bán kính tối thiểu R = h × tan(igh), phụ thuộc độ sâu h và góc giới hạn phản xạ toàn phần."),
    make_mc(9, "Thông hiểu", "Hiện tượng sợi cáp quang dẫn ánh sáng đi qua nhiều chỗ uốn cong mà ánh sáng không bị lọt ra ngoài là nhờ:", [
        "Góc tới của tia sáng tại mặt phân cách giữa lõi và vỏ luôn lớn hơn góc giới hạn phản xạ toàn phần",
        "Vỏ sợi quang phản xạ ánh sáng bằng nam châm điện",
        "Ánh sáng bị đông đặc lại bên trong sợi quang",
        "Ánh sáng tự uốn cong theo từ trường Trái Đất"
    ], 0, "Tia sáng truyền theo đường dích dắc phản xạ toàn phần liên tiếp ở mặt phân cách lõi - vỏ."),
    make_mc(10, "Thông hiểu", "Trong một thí nghiệm, chiếu tia sáng từ nước ra không khí. Khi góc khúc xạ đạt giá trị cực đại r = 90 độ thì góc tới i khi đó được gọi là:", [
        "Góc giới hạn phản xạ toàn phần",
        "Góc lệch phương truyền cực đại",
        "Góc phản xạ tuyệt đối",
        "Góc tới vuông pha"
    ], 0, "Góc tới tương ứng với góc khúc xạ r = 90° chính là góc giới hạn igh."),
    make_mc(11, "Thông hiểu", "Một viên kim cương có chiết suất n = 2,42 đặt trong không khí. Biết sin 24,4° ≈ 0,413 = 1/2,42. Góc giới hạn phản xạ toàn phần của kim cương là:", [
        "Khoảng 24,4 độ",
        "Khoảng 48,5 độ",
        "Khoảng 42,0 độ",
        "Đúng 90 độ"
    ], 0, "sin igh = 1/2,42 ≈ 0,413 => igh ≈ 24,4°."),
    make_mc(12, "Thông hiểu", "Lăng kính phản xạ toàn phần loại đổi hướng tia sáng 180 độ (lăng kính Porro) thường có tia sáng đi vào và đi ra qua:", [
        "Mặt huyền của lăng kính",
        "Hai mặt góc vuông",
        "Đỉnh góc vuông",
        "Mặt đáy tam giác đều"
    ], 0, "Tia sáng đi vào vuông góc với mặt huyền, phản xạ toàn phần tại hai mặt bên và ló ra ngược chiều ở mặt huyền.")
]

p2_b18_t3 = [
    make_tf(1, "Thông hiểu", "Xét các tính chất vật lý của hiện tượng phản xạ toàn phần:", [
        ("a", "Hiện tượng phản xạ toàn phần có thể xảy ra khi ánh sáng truyền từ kim cương sang không khí.", True),
        ("b", "Hiện tượng phản xạ toàn phần có thể xảy ra khi ánh sáng truyền từ không khí vào kim cương.", False),
        ("c", "Góc giới hạn phản xạ toàn phần igh luôn luôn nhỏ hơn 90 độ.", True),
        ("d", "Khi góc tới i = igh thì tia khúc xạ vuông góc với đường pháp tuyến.", True)
    ], "Không khí sang kim cương là từ môi trường kém sang chiết quang hơn nên không thể xảy ra phản xạ toàn phần."),
    make_tf(2, "Thông hiểu", "Ưu điểm của cáp quang so với dây cáp đồng kim loại:", [
        ("a", "Truyền được lượng dữ liệu khổng lồ với tốc độ cực nhanh trong cùng một thời gian.", True),
        ("b", "Không bị can nhiễu bởi sấm sét hay sóng điện từ từ các thiết bị xung quanh.", True),
        ("c", "Nhẹ hơn và khó bị ăn mòn hóa học hơn so với kim loại đồng.", True),
        ("d", "Có thể dẫn được dòng điện cao thế để chạy các động cơ công nghiệp lớn.", False)
    ], "Cáp quang chỉ truyền tín hiệu ánh sáng photon, hoàn toàn không dẫn dòng điện."),
    make_tf(3, "Vận dụng", "Một khối chất lỏng trong suốt có chiết suất n = 1,414 (căn bậc hai của 2). Ánh sáng chiếu từ chất lỏng ra không khí:", [
        ("a", "Góc giới hạn phản xạ toàn phần của chất lỏng là 45 độ.", True),
        ("b", "Nếu góc tới i = 30 độ thì góc khúc xạ r = 45 độ.", True),
        ("c", "Nếu góc tới i = 50 độ thì xảy ra hiện tượng phản xạ toàn phần.", True),
        ("d", "Nếu chiếu tia sáng vuông góc với mặt thoáng chất lỏng thì tia sáng bị phản xạ toàn phần trở lại đáy.", False)
    ], "Chiếu vuông góc (i = 0°) thì tia sáng truyền thẳng ra ngoài không khí (r = 0°)."),
    make_tf(4, "Vận dụng", "Xét ứng dụng của hiện tượng phản xạ toàn phần trong đời sống:", [
        ("a", "Trong máy ảnh cơ truyền thống, lăng kính ngũ giác (pentaprism) sử dụng phản xạ toàn phần để hướng hình ảnh lên kính ngắm.", True),
        ("b", "Các hạt cườm phản quang gắn trên biển báo giao thông hoặc áo bảo hộ ban đêm ứng dụng phản xạ toàn phần.", True),
        ("c", "Đèn pin chiếu sáng thông thường hoạt động hoàn toàn dựa trên phản xạ toàn phần.", False),
        ("d", "Dây cáp quang nội soi y tế truyền ánh sáng lạnh vào cơ thể không gây bỏng rát các mô nội tạng.", True)
    ], "Đèn pin dùng gương phản xạ parabol (chóa đèn) phản xạ ánh sáng đèn sợi đốt hoặc LED, không phải hiện tượng phản xạ toàn phần.")
]

p3_b18_t3 = [
    make_sa(1, "Thông hiểu", "Chiếu ánh sáng từ một khối thạch anh ra không khí với góc giới hạn igh = 40 độ. Nếu chiếu tia sáng với góc tới 45 độ thì góc phản xạ bằng bao nhiêu độ?", "45", "Vì i = 45° > igh = 40° nên xảy ra phản xạ toàn phần, góc phản xạ r' = i = 45°."),
    make_sa(2, "Thông hiểu", "Một tia sáng truyền từ nước ra không khí. Khi góc tới đúng bằng góc giới hạn phản xạ toàn phần thì góc khúc xạ r bằng bao nhiêu độ?", "90", "Tại i = igh, tia khúc xạ đi là là sát mặt nước (r = 90°)."),
    make_sa(3, "Vận dụng", "Chiếu tia sáng từ môi trường trong suốt có chiết suất n = √2 (xấp xỉ 1,414) ra không khí. Góc giới hạn phản xạ toàn phần bằng bao nhiêu độ?", "45", "sin igh = 1/√2 => igh = 45°."),
    make_sa(4, "Vận dụng", "Một người chiếu đèn pin từ đáy bể bơi lên mặt nước với góc tới 60 độ. Biết góc giới hạn phản xạ toàn phần của nước là 48,5 độ. Tia sáng có lọt được ra ngoài không khí không? (Trả lời: Có hoặc Không)", "Không", "i = 60° > igh = 48,5° nên tia sáng bị phản xạ toàn phần trở lại nước."),
    make_sa(5, "Vận dụng cao", "Trong một sợi cáp quang viễn thông, chiết suất của phần lõi là n1 = 1,5 và phần vỏ là n2 = 1,44. Tỉ số n2 / n1 (chính là sin igh) bằng bao nhiêu?", "0.96", "1,44 / 1,5 = 0,96."),
    make_sa(6, "Vận dụng cao", "Một lăng kính phản xạ toàn phần hình tam giác vuông cân được dùng để quay hướng truyền của tia sáng một góc 180 độ. Tia sáng tới đã thực hiện phản xạ toàn phần mấy lần bên trong lăng kính này?", "2", "Tia sáng phản xạ toàn phần lần 1 tại mặt bên thứ nhất và lần 2 tại mặt bên thứ hai, quay ngược 180°.")
]

p4_b18_t3 = [
    make_vdc(1, "Công nghệ bảo mật chống nghe lén trên đường truyền cáp quang: Kẻ gian muốn lấy cắp thông tin truyền qua cáp quang thường phải uốn cong sợi quang để trích xuất tín hiệu. Tại sao khi sợi quang bị uốn cong quá mức thì thông tin có thể bị rò rỉ ra ngoài?", [
        "Khi sợi quang bị uốn cong, góc tới của tia sáng tại mặt phân cách lõi - vỏ bị giảm xuống nhỏ hơn góc giới hạn igh, làm ánh sáng khúc xạ lọt ra ngoài vỏ",
        "Sợi quang bị nóng chảy làm ánh sáng bắn tung tóe",
        "Tín hiệu ánh sáng bị đảo chiều truyền ngược về nguồn phát",
        "Sóng vô tuyến xung quanh hút ánh sáng ra khỏi cáp quang"
    ], 0, "Bán kính uốn cong nhỏ làm góc tới i < igh, ánh sáng khúc xạ thoát ra ngoài lớp vỏ bọc."),
    make_vdc(2, "Bẫy ánh sáng trong tế bào pin quang điện mặt trời hiệu suất cao: Người ta chế tạo bề mặt pin với các vi cấu trúc dạng kim tự tháp đảo ngược để chùm tia sáng mặt trời sau khi đi vào trong lớp silicon:", [
        "Bị phản xạ toàn phần nhiều lần giữa các mặt đáy và không thể thoát ra ngoài, làm tăng tối đa khả năng hấp thụ photon",
        "Làm nguội nhiệt độ bề mặt pin xuống dưới 0 độ C",
        "Tạo ra từ trường mạnh tự hút các hạt electron",
        "Ngăn chặn hoàn toàn sự tích điện tĩnh trên tấm pin"
    ], 0, "Cấu trúc bẫy quang học làm góc tới tại các mặt thoát lớn hơn igh, ánh sáng bị giam giữ phản xạ toàn phần nhiều lần tăng hấp thụ sinh điện."),
    make_vdc(3, "Hiện tượng cầu vồng đôi (cầu vồng chính và cầu vồng phụ): Trong những buổi chiều sau cơn mưa, đôi khi ta nhìn thấy hai dải cầu vồng đồng tâm trên bầu trời. Cầu vồng phụ ở phía ngoài có thứ tự màu ngược lại (đỏ ở trong, tím ở ngoài) và mờ hơn cầu vồng chính là do:", [
        "Ánh sáng mặt trời bị phản xạ toàn phần hai lần bên trong giọt nước mưa trước khi ló ra ngoài",
        "Cầu vồng phụ được chiếu sáng bởi ánh sáng Mặt Trăng",
        "Cầu vồng phụ sinh ra từ các hạt bụi cát sa mạc",
        "Mắt người bị lưu ảnh ảo sau khi nhìn cầu vồng chính"
    ], 0, "Cầu vồng bậc hai (cầu vồng phụ) hình thành do ánh sáng phản xạ hai lần bên trong giọt nước, làm đảo ngược thứ tự các màu quang phổ."),
    make_vdc(4, "Một kỹ sư thiết kế ngọn hải đăng hiện đại sử dụng thấu kính Fresnel kết hợp hệ thống lăng kính phản xạ toàn phần bao quanh nguồn sáng LED công suất lớn. Ưu điểm vượt trội của việc kết hợp lăng kính phản xạ toàn phần ở mép trên và mép dưới đèn hải đăng là:", [
        "Tận dụng toàn bộ các tia sáng phát ra theo hướng lên trời và hướng xuống biển, bẻ gập chúng thành chùm tia sáng song song quét xa hàng chục hải lý",
        "Làm cho ngọn hải đăng phát ra tia laser tiêu diệt chướng ngại vật ngầm",
        "Giúp hải đăng tự quay mà không cần động cơ điện",
        "Làm ngọn đèn không tỏa nhiệt chút nào"
    ], 0, "Lăng kính phản xạ toàn phần thu gom toàn bộ ánh sáng phát tán theo các hướng vô ích và định hướng thành chùm sáng song song rọi xa trên mặt biển.")
]

exams["phys9_c6_b18_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b18", "Bài 18: Hiện tượng phản xạ toàn phần", 3, p1_b18_t3, p2_b18_t3, p3_b18_t3, p4_b18_t3)

print("Added phys9_c6_b18 (3 tests).")
