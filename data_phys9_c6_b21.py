# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 21: KÍNH LÚP
Bao gồm 3 đề thi độc lập 100%: phys9_c6_b21_test1, phys9_c6_b21_test2, phys9_c6_b21_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c6"
CH_TITLE = "Chương VI: Ánh sáng"

# =============================================================================
# BÀI 21: KÍNH LÚP (3 ĐỀ)
# =============================================================================

# --- phys9_c6_b21_test1 ---
p1_b21_t1 = [
    make_mc(1, "Nhận biết", "Kính lúp là một dụng cụ quang học bổ trợ cho mắt, bản chất của kính lúp là:", [
        "Một thấu kính hội tụ có tiêu cự ngắn",
        "Một thấu kính phân kì có tiêu cự rất dài",
        "Một gương cầu lồi phản chiếu",
        "Một khối lăng kính tam giác đều"
    ], 0, "Kính lúp là một thấu kính hội tụ có tiêu cự ngắn dùng để quan sát các vật nhỏ."),
    make_mc(2, "Nhận biết", "Khi quan sát một vật nhỏ qua kính lúp, ta phải đặt vật ở vị trí nào so với kính lúp?", [
        "Trong khoảng tiêu cự của kính lúp (d < f)",
        "Đúng tại hai lần tiêu cự (d = 2f)",
        "Ngoài khoảng hai lần tiêu cự (d > 2f)",
        "Ở rất xa kính lúp (d = vô cực)"
    ], 0, "Phải đặt vật trong khoảng tiêu cự (d < f) để cho ảnh ảo cùng chiều lớn hơn vật."),
    make_mc(3, "Nhận biết", "Ảnh của một vật nhỏ quan sát được qua kính lúp có tính chất là:", [
        "Ảnh ảo, cùng chiều và lớn hơn vật",
        "Ảnh thật, ngược chiều và nhỏ hơn vật",
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Ảnh ảo, ngược chiều và bằng vật"
    ], 0, "Kính lúp cho ảnh ảo, cùng chiều và lớn hơn vật."),
    make_mc(4, "Nhận biết", "Kí hiệu số bội giác của kính lúp thường được viết trên vành kính là:", [
        "Chữ G (ví dụ: 2x, 3x, 5x, 10x)",
        "Chữ V (ví dụ: 12V, 220V)",
        "Chữ W (ví dụ: 100W)",
        "Chữ A (ví dụ: 5A)"
    ], 0, "Số bội giác ký hiệu là G, ghi kèm chữ x (ví dụ 5x, 10x)."),
    make_mc(5, "Nhận biết", "Công thức liên hệ giữa số bội giác G và tiêu cự f (đo bằng đơn vị cm) của kính lúp là:", [
        "G = 25 / f",
        "G = f / 25",
        "G = 25 × f",
        "G = 25 + f"
    ], 0, "G = 25 / f (với f tính bằng cm)."),
    make_mc(6, "Nhận biết", "Kính lúp có số bội giác càng lớn thì tiêu cự của kính lúp đó:", [
        "Càng ngắn",
        "Càng dài",
        "Không thay đổi",
        "Luôn bằng 25 cm"
    ], 0, "Vì G = 25 / f nên G càng lớn thì f càng ngắn."),
    make_mc(7, "Thông hiểu", "Một kính lúp có ghi kí hiệu 5x trên vành kính. Tiêu cự f của kính lúp này bằng:", [
        "5 cm",
        "10 cm",
        "125 cm",
        "20 cm"
    ], 0, "G = 25 / f = 5 => f = 25 / 5 = 5 cm."),
    make_mc(8, "Thông hiểu", "Một thấu kính hội tụ có tiêu cự f = 10 cm được dùng làm kính lúp. Số bội giác của kính lúp này là:", [
        "2,5x",
        "5x",
        "10x",
        "0,4x"
    ], 0, "G = 25 / 10 = 2,5x."),
    make_mc(9, "Thông hiểu", "Đối tượng nào sau đây thường xuyên sử dụng kính lúp cầm tay trong công việc chuyên môn?", [
        "Thợ sửa chữa đồng hồ và thợ kim hoàn kiểm tra đá quý",
        "Thợ lặn dưới đáy biển sâu",
        "Phi công lái máy bay dân dụng",
        "Thợ xây nhà cao tầng"
    ], 0, "Thợ sửa đồng hồ và thợ kim hoàn soi chi tiết máy và đá quý siêu nhỏ."),
    make_mc(10, "Thông hiểu", "Khi quan sát một dòng chữ in nhỏ qua kính lúp, nếu từ từ đưa kính lúp ra xa trang sách (nhưng khoảng cách d vẫn nhỏ hơn tiêu cự f) thì ảnh ảo nhìn thấy sẽ:", [
        "Ngày càng to dần lên",
        "Nhỏ dần đi bằng mắt thường",
        "Lập tức biến thành ảnh thật ngược chiều",
        "Đổi màu từ đen sang đỏ"
    ], 0, "Khi d tăng từ 0 đến gần f, ảnh ảo dời xa thấu kính và độ phóng đại k tăng lên, ảnh to dần."),
    make_mc(11, "Thông hiểu", "Một người quan sát muốn nhìn thấy ảnh của con bọ qua kính lúp một cách rõ ràng và lâu mà mắt không bị mỏi thì nên đặt ảnh ảo của con bọ ở vị trí nào của mắt?", [
        "Tại điểm cực viễn của mắt (ngắm chừng ở vô cực)",
        "Tại điểm cực cận của mắt",
        "Sát vào giác mạc của mắt",
        "Cách mắt 5 mét"
    ], 0, "Ngắm chừng ở điểm cực viễn (vô cực đối với mắt tốt) thì cơ mi mắt không phải điều tiết, mắt không mỏi."),
    make_mc(12, "Thông hiểu", "Trong các kính lúp có số bội giác sau đây: 2x, 3x, 5x, 10x; kính lúp nào cho phép quan sát các chi tiết nhỏ nhất với kích thước ảnh phóng đại lớn nhất?", [
        "Kính lúp 10x",
        "Kính lúp 2x",
        "Kính lúp 3x",
        "Kính lúp 5x"
    ], 0, "Số bội giác lớn nhất (10x) cho ảnh phóng đại to nhất.")
]

p2_b21_t1 = [
    make_tf(1, "Thông hiểu", "Xét các tính chất cơ bản của kính lúp:", [
        ("a", "Kính lúp là thấu kính hội tụ có tiêu cự ngắn.", True),
        ("b", "Kính lúp dùng để quan sát các vật có kích thước rất lớn ở xa.", False),
        ("c", "Ảnh quan sát được qua kính lúp là ảnh ảo, cùng chiều và lớn hơn vật.", True),
        ("d", "Số bội giác của kính lúp càng lớn thì tiêu cự của nó càng dài.", False)
    ], "Kính lúp dùng quan sát vật nhỏ; G càng lớn thì f càng ngắn (G = 25/f)."),
    make_tf(2, "Thông hiểu", "Cách sử dụng kính lúp để quan sát một con tem cổ:", [
        ("a", "Đặt kính lúp ở khoảng cách nhỏ hơn tiêu cự của kính so với con tem.", True),
        ("b", "Mắt người quan sát đặt ở phía sau kính lúp.", True),
        ("c", "Nếu đặt con tem ở khoảng cách lớn hơn hai lần tiêu cự thì mắt vẫn nhìn thấy con tem phóng đại thuận chiều.", False),
        ("d", "Dịch chuyển nhẹ kính lúp để ảnh con tem hiện lên to rõ nét nhất.", True)
    ], "Nếu d > 2f thì thấu kính cho ảnh thật ngược chiều nhỏ hơn vật, không dùng làm kính lúp được."),
    make_tf(3, "Vận dụng", "Một kính lúp có tiêu cự f = 5 cm được dùng để soi một con kiến dài 4 mm. Con kiến đặt cách kính lúp d = 4 cm:", [
        ("a", "Số bội giác của kính lúp này là G = 5x.", True),
        ("b", "Con kiến nằm trong khoảng tiêu cự của kính lúp.", True),
        ("c", "Khoảng cách từ ảnh ảo của con kiến đến kính lúp là d' = 20 cm.", True),
        ("d", "Chiều dài của ảnh con kiến nhìn thấy qua kính lúp là 8 mm.", False)
    ], "1/d' = 1/5 - 1/4 = -1/20 => |d'| = 20 cm. k = 20/4 = 5 => Chiều dài ảnh = 4 mm × 5 = 20 mm = 2 cm."),
    make_tf(4, "Vận dụng", "So sánh hai kính lúp K1 (tiêu cự f1 = 10 cm) và K2 (tiêu cự f2 = 2,5 cm):", [
        ("a", "Kính lúp K1 có số bội giác G1 = 2,5x.", True),
        ("b", "Kính lúp K2 có số bội giác G2 = 10x.", True),
        ("c", "Kính lúp K1 phóng đại hình ảnh tốt hơn kính lúp K2.", False),
        ("d", "Kính lúp K2 có bề mặt cong sâu hơn (rìa mỏng hơn rất nhiều so với giữa) so với kính K1.", True)
    ], "K2 có G2 = 10x phóng đại tốt hơn K1 (G1 = 2,5x); thấu kính có f ngắn hơn thì mặt cong sâu hơn.")
]

p3_b21_t1 = [
    make_sa(1, "Thông hiểu", "Kính lúp là thấu kính hội tụ hay thấu kính phân kì?", "Hội tụ", "Kính lúp là thấu kính hội tụ có tiêu cự ngắn."),
    make_sa(2, "Thông hiểu", "Một kính lúp có tiêu cự f = 12,5 cm. Số bội giác G của kính lúp này bằng bao nhiêu?", "2", "G = 25 / 12,5 = 2x."),
    make_sa(3, "Vận dụng", "Trên vành một kính lúp có ghi 10x. Tiêu cự f của kính lúp này bằng bao nhiêu cm?", "2.5", "f = 25 / 10 = 2,5 cm."),
    make_sa(4, "Vận dụng", "Dùng kính lúp có f = 5 cm để quan sát một mẫu khoáng sản nhỏ đặt cách kính 3 cm. Khoảng cách từ ảnh ảo đến kính lúp bằng bao nhiêu cm?", "7.5", "1/d' = 1/5 - 1/3 = -2/15 => |d'| = 15/2 = 7,5 cm."),
    make_sa(5, "Vận dụng cao", "Dùng kính lúp có f = 10 cm quan sát một chi tiết máy nhỏ đặt cách kính 8 cm. Ảnh ảo của chi tiết máy lớn gấp mấy lần chi tiết máy thật?", "5", "1/d' = 1/10 - 1/8 = -1/40 => |d'| = 40 cm. k = d'/d = 40/8 = 5 lần."),
    make_sa(6, "Vận dụng cao", "Một vật sáng cao 2 mm đặt cách kính lúp có f = 6 cm một đoạn d = 4 cm. Chiều cao ảnh ảo quan sát được qua kính lúp bằng bao nhiêu mm?", "6", "1/d' = 1/6 - 1/4 = -1/12 => |d'| = 12 cm. k = 12/4 = 3 => A'B' = 2 mm × 3 = 6 mm.")
]

p4_b21_t1 = [
    make_vdc(1, "Trong kỹ thuật điều tra dấu vết tội phạm tại hiện trường vụ án, cán bộ kỹ thuật hình sự sử dụng kính lúp cầm tay có độ phóng đại cao kết hợp đèn chiếu tia cực tím để soi dấu vân tay trên tay nắm cửa. Ưu điểm của việc dùng kính lúp hội tụ tiêu cự ngắn trong trường hợp này là:", [
        "Phóng to các đường vân da và lỗ tiết mồ hôi li ti dưới dạng ảnh ảo sắc nét thuận chiều giúp nhận diện chính xác đặc điểm riêng",
        "Làm cháy các vết máu khô để phân tích hóa học",
        "Chiếu chụp hình ảnh xuyên qua bức tường dày",
        "Tạo ra ảnh thật lộn ngược chiếu lên màn hình máy tính"
    ], 0, "Kính lúp hội tụ f ngắn cho ảnh ảo thuận chiều phóng đại cực đại các nếp vân tay li ti."),
    make_vdc(2, "Một người già có khoảng nhìn rõ ngắn nhất là Đ = 40 cm (mắt lão). Khi người này dùng một kính lúp có tiêu cự f = 5 cm để đọc báo thì số bội giác thực tế của kính lúp đối với mắt người này khi ngắm chừng ở cực cận là:", [
        "G = 40 / 5 = 8x",
        "G = 25 / 5 = 5x",
        "G = 40 × 5 = 200x",
        "G = 5 / 40 = 0,125x"
    ], 0, "Số bội giác với mắt người lão thị có điểm cực cận Đ = 40 cm là G = Đ / f = 40 / 5 = 8x."),
    make_vdc(3, "Tại sao các thợ sửa chữa đồng hồ cơ tinh xảo thường sử dụng một chiếc kính lúp nhỏ kẹp trực tiếp vào hốc mắt (kính lúp đeo mắt thợ đồng hồ) thay vì cầm kính lúp bằng tay?", [
        "Giúp giải phóng cả hai bàn tay để cầm nhíp gắp và tua-vít thao tác chính xác với các bánh răng li ti, đồng thời giữ cố định khoảng cách quan sát tối ưu",
        "Để kính không bị rơi xuống đất khi thợ ngủ gật",
        "Để làm mắt thợ đồng hồ không bao giờ bị chớp",
        "Để biến kính lúp thành đèn pin tự phát sáng"
    ], 0, "Kẹp kính vào hốc mắt giúp rảnh cả 2 tay thao tác cơ khí vi mô và định vị khoảng cách ngắm chừng ổn định."),
    make_vdc(4, "Một kính lúp đơn giản làm bằng thấu kính hội tụ thường bị hiện tượng cầu sai và sắc sai (ảnh ở rìa bị mờ nhòe và có viền bảy màu). Để khắc phục triệt để nhược điểm này trong các kính lúp cao cấp (kính lúp tiêu sắc Achromatic), nhà sản xuất đã:", [
        "Ghép hai hoặc ba thấu kính làm từ các loại thủy tinh có độ tán sắc khác nhau dán sát lại với nhau",
        "Sơn đen toàn bộ viền thấu kính",
        "Tăng độ dày thấu kính lên gấp mười lần",
        "Chỉ cho ánh sáng đỏ truyền qua kính lúp"
    ], 0, "Ghép hệ thấu kính tiêu sắc (thấu kính hội tụ thủy tinh crown ghép với thấu kính phân kì thủy tinh flint) giúp triệt tiêu sắc sai và cầu sai.")
]

exams["phys9_c6_b21_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b21", "Bài 21: Kính lúp", 1, p1_b21_t1, p2_b21_t1, p3_b21_t1, p4_b21_t1)

# --- phys9_c6_b21_test2 ---
p1_b21_t2 = [
    make_mc(1, "Nhận biết", "Kính lúp là dụng cụ quang học dùng để:", [
        "Quan sát các vật nhỏ mà mắt thường khó nhìn rõ chi tiết",
        "Nhìn các vật ở rất xa như các vì sao",
        "Đo cường độ dòng điện trong mạch",
        "Chắn gió và bụi cho mắt khi đi đường"
    ], 0, "Kính lúp dùng để quan sát các vật nhỏ."),
    make_mc(2, "Nhận biết", "Số ghi trên vành kính lúp như 2,5x; 5x; 8x cho biết:", [
        "Số bội giác của kính lúp",
        "Khối lượng của kính lúp",
        "Đường kính của vành kính lúp",
        "Năm sản xuất của kính lúp"
    ], 0, "Số ghi 2,5x, 5x... cho biết số bội giác G của kính lúp."),
    make_mc(3, "Nhận biết", "Để quan sát được ảnh ảo lớn hơn vật qua kính lúp, khoảng cách từ vật đến kính lúp (d) phải thỏa mãn điều kiện:", [
        "d < f (nhỏ hơn tiêu cự của kính lúp)",
        "d = 2f",
        "d > 2f",
        "d = 4f"
    ], 0, "Vật phải đặt trong khoảng tiêu cự (d < f)."),
    make_mc(4, "Nhận biết", "Trong công thức G = 25 / f của kính lúp, con số 25 cm đại diện cho:", [
        "Khoảng nhìn rõ ngắn nhất (khoảng cực cận) của mắt bình thường",
        "Chiều dài của chiếc kính lúp",
        "Khoảng cách từ Trái Đất đến Mặt Trăng",
        "Tiêu cự cố định của mọi thấu kính"
    ], 0, "Đ = 25 cm là khoảng cực cận trung bình của mắt người bình thường."),
    make_mc(5, "Nhận biết", "Giữa hai kính lúp có tiêu cự f1 = 5 cm và f2 = 10 cm thì:", [
        "Kính lúp có tiêu cự f1 = 5 cm có số bội giác lớn hơn",
        "Kính lúp có tiêu cự f2 = 10 cm có số bội giác lớn hơn",
        "Hai kính lúp có số bội giác bằng nhau",
        "Không thể so sánh số bội giác của hai kính"
    ], 0, "G = 25/f nên f càng nhỏ thì G càng lớn: G1 = 5x > G2 = 2,5x."),
    make_mc(6, "Nhận biết", "Ảnh của một vật tạo bởi kính lúp là:", [
        "Ảnh ảo cùng chiều",
        "Ảnh thật ngược chiều",
        "Ảnh thật cùng chiều",
        "Ảnh ảo ngược chiều"
    ], 0, "Kính lúp luôn cho ảnh ảo cùng chiều lớn hơn vật."),
    make_mc(7, "Thông hiểu", "Một kính lúp có tiêu cự f = 2,5 cm. Số bội giác của kính lúp này là:", [
        "10x",
        "2,5x",
        "5x",
        "20x"
    ], 0, "G = 25 / 2,5 = 10x."),
    make_mc(8, "Thông hiểu", "Trên vành của một kính lúp có ghi chữ 8x. Tiêu cự f của kính lúp này là:", [
        "3,125 cm",
        "8 cm",
        "200 cm",
        "0,32 cm"
    ], 0, "f = 25 / 8 = 3,125 cm."),
    make_mc(9, "Thông hiểu", "Một học sinh dùng kính lúp quan sát gân của một chiếc lá cây. Bạn học sinh thấy hình ảnh gân lá rõ nét và to nhất khi:", [
        "Đặt chiếc lá cách kính lúp một khoảng gần bằng nhưng nhỏ hơn tiêu cự f của kính",
        "Dán chặt chiếc lá vào sát mắt của mình",
        "Để chiếc lá cách kính lúp 2 mét",
        "Nhúng chiếc lá chìm trong nước sôi"
    ], 0, "Đặt vật sát tiêu điểm (d gần bằng f) cho ảnh ảo ở xa và độ phóng đại góc lớn nhất."),
    make_mc(10, "Thông hiểu", "Khi thợ sửa đồng hồ quan sát các bánh răng nhỏ qua kính lúp, mắt của người thợ đặt ở đâu?", [
        "Đặt sát phía sau kính lúp để nhìn chùm tia ló phát ra từ kính",
        "Đặt phía trước vật quan sát",
        "Đặt cách kính lúp 5 mét",
        "Nhắm chặt cả hai mắt"
    ], 0, "Mắt đặt sau kính lúp để thu nhận chùm tia ló tạo ảnh ảo trên võng mạc."),
    make_mc(11, "Thông hiểu", "Thấu kính phân kì có thể dùng làm kính lúp được không? Tại sao?", [
        "Không thể, vì thấu kính phân kì luôn cho ảnh ảo nhỏ hơn vật nên không có tác dụng phóng đại",
        "Được, vì thấu kính phân kì cũng tạo ảnh ảo",
        "Được, nếu thấu kính phân kì có tiêu cự rất lớn",
        "Được, nếu chiếu đèn laser vào kính"
    ], 0, "Thấu kính phân kì luôn cho ảnh ảo nhỏ hơn vật thật nên không thể làm kính lúp."),
    make_mc(12, "Thông hiểu", "Một người dùng kính lúp có tiêu cự f = 10 cm để soi một vết nứt trên mặt đá quý. Nếu người đó đặt viên đá cách kính 15 cm thì hiện tượng quan sát được là:", [
        "Không thể quan sát được ảnh ảo phóng đại thuận chiều vì vật nằm ngoài tiêu cự (d > f)",
        "Ảnh vết nứt phóng to gấp một trăm lần",
        "Kính lúp tự động phát sáng rực rỡ",
        "Vết nứt trên đá quý tự biến mất"
    ], 0, "d = 15 cm > f = 10 cm nên thấu kính tạo ảnh thật ngược chiều phía sau kính, mắt nhìn từ sau không thấy ảnh ảo phóng đại.")
]

p2_b21_t2 = [
    make_tf(1, "Thông hiểu", "Xét các đặc tính kỹ thuật của kính lúp thông dụng:", [
        ("a", "Về mặt quang học, kính lúp thực chất là một thấu kính hội tụ có tiêu cự ngắn (thường nhỏ hơn 25 cm).", True),
        ("b", "Số bội giác của kính lúp thường nằm trong khoảng từ 1,5x đến 40x.", True),
        ("c", "Kính lúp có tiêu cự càng dài thì số bội giác càng lớn.", False),
        ("d", "Vật quan sát qua kính lúp phải đặt trong khoảng tiêu cự của kính.", True)
    ], "G = 25 / f nên f càng ngắn thì G càng lớn."),
    make_tf(2, "Thông hiểu", "Hoạt động tạo ảnh của kính lúp đối với mắt người quan sát:", [
        ("a", "Ảnh ảo tạo bởi kính lúp nằm cùng phía với vật so với thấu kính.", True),
        ("b", "Ảnh ảo của vật qua kính lúp luôn ngược chiều với vật.", False),
        ("c", "Mắt người nhìn thấy ảnh ảo vì chùm tia ló qua kính lúp đi vào con ngươi của mắt.", True),
        ("d", "Góc trông ảnh qua kính lúp lớn hơn nhiều so với góc trông vật trực tiếp bằng mắt thường.", True)
    ], "Ảnh ảo qua kính lúp luôn cùng chiều với vật."),
    make_tf(3, "Vận dụng", "Một kính lúp có ghi kí hiệu 4x trên vành kính:", [
        ("a", "Tiêu cự của kính lúp này là f = 6,25 cm.", True),
        ("b", "Số bội giác của kính lúp là G = 4.", True),
        ("c", "Nếu đặt vật cách kính d = 5 cm thì thu được ảnh ảo cách kính d' = 25 cm.", True),
        ("d", "Độ phóng đại của ảnh trong trường hợp này là k = 10.", False)
    ], "f = 25 / 4 = 6,25 cm. 1/d' = 1/6,25 - 1/5 = -1/25 => |d'| = 25 cm. k = 25 / 5 = 5 (không phải 10)."),
    make_tf(4, "Vận dụng", "Hai bạn học sinh dùng kính lúp để đọc một dòng chữ nhỏ: Bạn Hùng dùng kính có f = 5 cm (G = 5x), bạn Tuấn dùng kính có f = 8,33 cm (G = 3x):", [
        ("a", "Kính của bạn Hùng có độ phóng đại góc lớn hơn kính của bạn Tuấn.", True),
        ("b", "Để nhìn thấy ảnh ảo, cả hai bạn đều phải đặt sách trong khoảng tiêu cự của kính mình cầm.", True),
        ("c", "Kính của bạn Hùng có phần rìa dày hơn phần giữa.", False),
        ("d", "Nếu ngắm chừng ở vô cực, mắt người quan sát không phải điều tiết khi nhìn qua kính lúp.", True)
    ], "Kính lúp là thấu kính hội tụ nên phần rìa phải mỏng hơn phần giữa.")
]

p3_b21_t2 = [
    make_sa(1, "Thông hiểu", "Một kính lúp có tiêu cự f = 5 cm. Số bội giác của kính lúp này bằng bao nhiêu?", "5", "G = 25 / 5 = 5x."),
    make_sa(2, "Thông hiểu", "Ảnh quan sát được qua kính lúp lớn hơn hay nhỏ hơn vật thật?", "Lớn hơn", "Kính lúp luôn cho ảnh ảo phóng đại lớn hơn vật."),
    make_sa(3, "Vận dụng", "Trên vành một kính lúp có ghi 5x. Tiêu cự f của kính lúp này bằng bao nhiêu cm?", "5", "f = 25 / 5 = 5 cm."),
    make_sa(4, "Vận dụng", "Một vật sáng nhỏ đặt cách kính lúp có f = 10 cm một khoảng d = 5 cm. Khoảng cách từ ảnh ảo đến kính lúp bằng bao nhiêu cm?", "10", "1/d' = 1/10 - 1/5 = -1/10 => |d'| = 10 cm."),
    make_sa(5, "Vận dụng cao", "Dùng kính lúp có f = 8 cm quan sát vật nhỏ đặt cách kính d = 6 cm. Độ phóng đại ảnh ảo k bằng bao nhiêu lần?", "4", "1/d' = 1/8 - 1/6 = -1/24 => |d'| = 24 cm. k = d'/d = 24/6 = 4 lần."),
    make_sa(6, "Vận dụng cao", "Một vật nhỏ cao 1,5 mm đặt trước kính lúp có f = 4 cm, cách kính d = 3 cm. Chiều cao của ảnh ảo quan sát được là bao nhiêu mm?", "6", "1/d' = 1/4 - 1/3 = -1/12 => |d'| = 12 cm. k = 12/3 = 4 => Chiều cao ảnh = 1,5 mm × 4 = 6 mm.")
]

p4_b21_t2 = [
    make_vdc(1, "Trong ngành công nghiệp vi điện tử bán dẫn, các kỹ thuật viên kiểm tra lỗi chân hàn của chip IC trên bo mạch chủ bằng kính hiển vi soi nổi hoặc kính lúp để bàn có gắn đèn LED tròn xung quanh. Tác dụng của đèn LED tròn vòng quanh vành kính lúp là:", [
        "Chiếu sáng đều từ mọi phía triệt tiêu bóng tối của các linh kiện nhô cao, giúp quan sát rõ nét mọi góc cạnh của chân hàn",
        "Làm tăng tiêu cự của kính lúp lên gấp đôi",
        "Hàn nóng chảy lại các mối hàn bị hở",
        "Khử từ trường dư trên bo mạch điện tử"
    ], 0, "Đèn LED tròn chiếu sáng không bóng (shadowless) giúp nhìn rõ các góc chân hàn siêu nhỏ."),
    make_vdc(2, "Một người muốn tự chế tạo một chiếc kính lúp đơn giản từ một bóng đèn sợi đốt tròn đã cháy hỏng. Người đó tháo đui đèn, đổ đầy nước trong suốt vào trong bóng thủy tinh rồi bịt kín lại. Chiếc bóng đèn chứa đầy nước này có thể hoạt động như một kính lúp hội tụ vì:", [
        "Khối cầu nước trong suốt có bề mặt cong lồi và chiết suất lớn hơn không khí nên hoạt động như một thấu kính hội tụ có tiêu cự ngắn",
        "Nước bên trong bóng đèn phản xạ ánh sáng như gương soi",
        "Bóng đèn chứa khí trơ phát quang",
        "Thủy tinh làm lạnh môi trường xung quanh"
    ], 0, "Quả cầu nước trong suốt là thấu kính hội tụ cầu có tiêu cự ngắn, phóng to vật nhỏ đặt sát mặt cầu."),
    make_vdc(3, "Để quan sát cấu tạo mắt kép của một con ruồi giấm trong giờ thực hành Sinh học 9, học sinh nên chọn dụng cụ nào sau đây để có độ phóng đại chi tiết tốt nhất?", [
        "Kính hiển vi quang học có độ phóng đại từ 40x đến 400x",
        "Kính lúp cầm tay loại 2x",
        "Gương cầu lồi xe máy",
        "Thước nhựa trong suốt chia vạch"
    ], 0, "Mắt kép côn trùng có cấu tạo hàng nghìn mắt đơn cực nhỏ, cần độ phóng đại hàng trăm lần của kính hiển vi quang học."),
    make_vdc(4, "Một kính lúp có số bội giác G = 5x (f = 5 cm). Một người mắt tốt quan sát một vật nhỏ qua kính lúp trong trạng thái ngắm chừng ở vô cực (vật đặt đúng tại tiêu điểm F của kính lúp). Khi đó chùm tia sáng ló ra khỏi kính lúp đi vào mắt người quan sát có đặc điểm:", [
        "Là chùm tia sáng song song với nhau, mắt nhìn vật ở trạng thái thư giãn hoàn toàn không phải điều tiết",
        "Hội tụ tại một điểm cách mắt 10 cm làm mắt bị căng thẳng",
        "Phân kì loe rộng làm mắt không thể quan sát được",
        "Bị đổi màu thành ánh sáng xanh lam"
    ], 0, "Khi ngắm chừng ở vô cực, vật tại F cho chùm tia ló song song, mắt quan sát thư giãn không phải điều tiết.")
]

exams["phys9_c6_b21_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b21", "Bài 21: Kính lúp", 2, p1_b21_t2, p2_b21_t2, p3_b21_t2, p4_b21_t2)

# --- phys9_c6_b21_test3 ---
p1_b21_t3 = [
    make_mc(1, "Nhận biết", "Vật sáng quan sát qua kính lúp phải có kích thước như thế nào so với tầm nhìn thông thường của mắt?", [
        "Kích thước nhỏ mà mắt thường khó nhìn rõ các chi tiết",
        "Kích thước khổng lồ như một tòa nhà",
        "Kích thước của một sân bóng đá",
        "Vật thể ở ngoài không gian vũ trụ"
    ], 0, "Kính lúp dùng để quan sát các vật có kích thước nhỏ."),
    make_mc(2, "Nhận biết", "Số bội giác G của kính lúp cho biết:", [
        "Ảnh của vật qua kính lúp lớn hơn bao nhiêu lần so với khi nhìn trực tiếp vật bằng mắt thường ở khoảng cực cận",
        "Khoảng cách từ kính lúp đến mắt",
        "Thời gian ánh sáng đi qua kính lúp",
        "Độ trong suốt của thủy tinh làm kính"
    ], 0, "Số bội giác đo tỉ lệ góc trông ảnh qua kính so với góc trông vật trực tiếp ở cực cận."),
    make_mc(3, "Nhận biết", "Kính lúp có tiêu cự f = 5 cm thì số bội giác ghi trên vành kính là:", [
        "5x",
        "2x",
        "10x",
        "25x"
    ], 0, "G = 25 / 5 = 5x."),
    make_mc(4, "Nhận biết", "Nếu kính lúp có số bội giác G = 2x thì tiêu cự của kính lúp đó bằng:", [
        "12,5 cm",
        "25 cm",
        "50 cm",
        "2 cm"
    ], 0, "f = 25 / 2 = 12,5 cm."),
    make_mc(5, "Nhận biết", "Đặc điểm của chùm tia ló khi chiếu chùm tia tới xuất phát từ một điểm của vật đặt trong khoảng tiêu cự của kính lúp là:", [
        "Chùm tia phân kì có đường kéo dài gặp nhau tạo ảnh ảo",
        "Chùm tia hội tụ thực sự tại một điểm sau kính",
        "Chùm tia song song với nhau",
        "Chùm tia bị phản xạ toàn phần trở lại nguồn"
    ], 0, "Vật trong khoảng tiêu cự cho chùm ló phân kì có đường kéo dài cắt nhau tạo ảnh ảo."),
    make_mc(6, "Nhận biết", "Một người thợ sửa đồng hồ cơ khí tinh xảo sử dụng kính lúp để làm gì?", [
        "Quan sát rõ các bánh răng, lò xo và trục xoay siêu nhỏ bên trong đồng hồ",
        "Đo nhiệt độ của pin đồng hồ",
        "Lên dây cót cho đồng hồ",
        "Hàn dây điện bằng kính lúp"
    ], 0, "Kính lúp giúp thợ đồng hồ phóng to các chi tiết cơ khí vi mô."),
    make_mc(7, "Thông hiểu", "Một kính lúp có tiêu cự f = 6,25 cm. Số bội giác của kính lúp này là:", [
        "4x",
        "2,5x",
        "6x",
        "8x"
    ], 0, "G = 25 / 6,25 = 4x."),
    make_mc(8, "Thông hiểu", "Một người cận thị dùng kính lúp để đọc một dòng chữ nhỏ. So với người mắt bình thường, người cận thị có điểm cực cận gần mắt hơn (ví dụ Đ = 15 cm). Số bội giác thực tế của kính lúp (f = 5 cm) đối với người cận thị này là:", [
        "G = 15 / 5 = 3x",
        "G = 25 / 5 = 5x",
        "G = 15 × 5 = 75x",
        "G = 5 / 15 = 0,33x"
    ], 0, "G_cận = Đ_cận / f = 15 / 5 = 3x."),
    make_mc(9, "Thông hiểu", "Khi sử dụng kính lúp để soi một con rệp cây trên lá, nếu để con rệp quá xa kính lúp (cách kính một khoảng lớn hơn tiêu cự f) thì mắt người quan sát đặt sau kính sẽ:", [
        "Không thể quan sát được ảnh ảo cùng chiều phóng đại của con rệp",
        "Thấy con rệp to gấp một triệu lần",
        "Thấy con rệp phát ra ánh sáng huỳnh quang",
        "Thấy kính lúp tự bốc cháy"
    ], 0, "d > f cho ảnh thật ngược chiều, không quan sát được ảnh ảo phóng đại như kính lúp."),
    make_mc(10, "Thông hiểu", "Để kính lúp phát huy hiệu quả phóng đại tối đa mà mắt không bị mệt mỏi sau thời gian dài làm việc, người sử dụng nên điều chỉnh kính sao cho:", [
        "Vật nằm ở vị trí sao cho ảnh ảo hiện ra ở điểm cực viễn của mắt (ngắm chừng ở vô cực)",
        "Dán chặt vật vào mắt",
        "Kéo kính lúp ra xa vật hết cỡ",
        "Vừa soi vừa lắc kính lúp liên tục"
    ], 0, "Ngắm chừng ở cực viễn giúp mắt thư giãn hoàn toàn, không phải điều tiết."),
    make_mc(11, "Thông hiểu", "Dụng cụ quang học nào sau đây gồm hai bộ phận chính là vật kính và thị kính đều có tính chất như các kính lúp phóng đại?", [
        "Kính hiển vi quang học",
        "Kính cận thị đơn tròng",
        "Gương soi trang điểm phẳng",
        "Kính mắt râm thời trang"
    ], 0, "Kính hiển vi gồm vật kính có f1 rất ngắn tạo ảnh thật và thị kính hoạt động như kính lúp phóng đại ảnh thật đó."),
    make_mc(12, "Thông hiểu", "Một giọt nước tròn trong suốt đọng trên tờ báo in chữ nhỏ hoạt động như một kính lúp tự nhiên vì:", [
        "Mặt cong lồi của giọt nước khúc xạ ánh sáng như một thấu kính hội tụ có tiêu cự ngắn",
        "Nước tẩy sạch vết mực in",
        "Nước làm giấy báo nở to ra",
        "Nước tự phát ra tia laser"
    ], 0, "Giọt nước lồi hoạt động như thấu kính hội tụ mỏng có tiêu cự ngắn làm kính lúp phóng to chữ.")
]

p2_b21_t3 = [
    make_tf(1, "Thông hiểu", "Về cấu tạo và công dụng của kính lúp trong khoa học đời sống:", [
        ("a", "Kính lúp cầm tay có phần vành bảo vệ và cán cầm bằng nhựa hoặc kim loại.", True),
        ("b", "Kính lúp giúp tăng góc trông ảnh của vật nhỏ lên mắt người quan sát.", True),
        ("c", "Kính lúp có thể dùng để tập trung ánh sáng mặt trời đốt cháy một mẩu giấy nhỏ.", True),
        ("d", "Kính lúp có thể tạo ra ảnh thật cùng chiều và nhỏ hơn vật.", False)
    ], "Ảnh thật qua TKHT luôn ngược chiều với vật."),
    make_tf(2, "Thông hiểu", "Nguyên lý ngắm chừng qua kính lúp:", [
        ("a", "Ngắm chừng ở cực cận là điều chỉnh để ảnh ảo hiện lên ở điểm cực cận của mắt.", True),
        ("b", "Ngắm chừng ở vô cực là điều chỉnh để ảnh ảo hiện lên ở vô cực (vật đặt đúng tiêu điểm F của kính).", True),
        ("c", "Khi ngắm chừng ở vô cực, mắt người có thị lực bình thường phải điều tiết tối đa.", False),
        ("d", "Người già bị lão thị ngắm chừng ở cực viễn cũng không phải điều tiết mắt.", True)
    ], "Ở vô cực, mắt bình thường nhìn ở trạng thái nghỉ, hoàn toàn không phải điều tiết."),
    make_tf(3, "Vận dụng", "Một kính lúp có ghi kí hiệu 2,5x. Dùng kính này quan sát một hạt vừng dài 2 mm đặt cách kính d = 6 cm:", [
        ("a", "Tiêu cự của kính lúp là f = 10 cm.", True),
        ("b", "Hạt vừng nằm trong khoảng tiêu cự của kính lúp.", True),
        ("c", "Khoảng cách từ ảnh ảo đến kính lúp là d' = 15 cm.", True),
        ("d", "Chiều dài của ảnh hạt vừng nhìn thấy qua kính lúp là 5 mm.", True)
    ], "f = 25 / 2,5 = 10 cm. 1/d' = 1/10 - 1/6 = -1/15 => |d'| = 15 cm. k = 15/6 = 2,5 => Chiều dài ảnh = 2 mm × 2,5 = 5 mm."),
    make_tf(4, "Vận dụng", "Xét ba kính lúp có tiêu cự lần lượt là fA = 2,5 cm; fB = 5 cm; fC = 10 cm:", [
        ("a", "Số bội giác tương ứng là GA = 10x; GB = 5x; GC = 2,5x.", True),
        ("b", "Kính lúp A có khả năng phóng to chi tiết tốt nhất trong ba kính.", True),
        ("c", "Kính lúp C có độ cong bề mặt lớn nhất.", False),
        ("d", "Cả ba kính lúp đều là thấu kính hội tụ rìa mỏng.", True)
    ], "Kính A có tiêu cự ngắn nhất (fA = 2,5 cm) nên mặt cầu phải cong sâu nhất, không phải kính C.")
]

p3_b21_t3 = [
    make_sa(1, "Thông hiểu", "Số bội giác của kính lúp có tiêu cự f = 25 cm bằng bao nhiêu?", "1", "G = 25 / 25 = 1x."),
    make_sa(2, "Thông hiểu", "Kính lúp có tiêu cự ngắn hơn thì số bội giác lớn hơn hay nhỏ hơn?", "Lớn hơn", "G tỉ lệ nghịch với f nên f ngắn hơn thì G lớn hơn."),
    make_sa(3, "Vận dụng", "Trên vành một kính lúp có ghi 20x. Tiêu cự f của kính lúp này bằng bao nhiêu cm?", "1.25", "f = 25 / 20 = 1,25 cm."),
    make_sa(4, "Vận dụng", "Một kính lúp có f = 8 cm. Muốn ngắm chừng ở vô cực (mắt không phải điều tiết), người quan sát phải đặt vật cách kính lúp bao nhiêu cm?", "8", "Vật phải đặt đúng tại tiêu điểm vật chính: d = f = 8 cm."),
    make_sa(5, "Vận dụng cao", "Dùng kính lúp có f = 12 cm quan sát một con kiến đặt cách kính d = 9 cm. Ảnh ảo của con kiến cách kính lúp bao nhiêu cm?", "36", "1/d' = 1/12 - 1/9 = -1/36 => |d'| = 36 cm."),
    make_sa(6, "Vận dụng cao", "Một vật sáng nhỏ cao 1 mm đặt cách kính lúp có f = 12 cm một đoạn d = 9 cm. Chiều cao của ảnh ảo quan sát được qua kính lúp bằng bao nhiêu mm?", "4", "d' = 36 cm. k = 36/9 = 4 => Chiều cao ảnh = 1 mm × 4 = 4 mm.")
]

p4_b21_t3 = [
    make_vdc(1, "Khi nhà bác học Leeuwenhoek tự tay mài các thấu kính hội tụ thủy tinh siêu nhỏ dạng hình cầu có đường kính chỉ khoảng 1 - 2 mm vào thế kỷ 17 để làm chiếc kính hiển vi đơn giản đầu tiên, ông đã chế tạo ra các kính lúp có tiêu cự cực ngắn. Tiêu cự càng ngắn thì:", [
        "Số bội giác của kính lúp càng lớn (lên tới 200x - 300x), cho phép lần đầu tiên nhìn thấy vi khuẩn và tinh trùng",
        "Kính lúp biến thành thấu kính phân kì",
        "Ánh sáng không thể đi qua kính lúp được nữa",
        "Số bội giác giảm về 0"
    ], 0, "G = 25/f nên khi f chỉ khoảng 0,8 - 1 mm thì G đạt tới 250x - 300x, giúp khám phá thế giới vi sinh vật."),
    make_vdc(2, "Một kính lúp cầm tay có tiêu cự f = 10 cm. Người quan sát có khoảng nhìn rõ từ 25 cm đến vô cực. Khi người này di chuyển vật quan sát trong khoảng từ vị trí cách kính lúp d1 = 7,14 cm đến vị trí d2 = 10 cm thì:", [
        "Ảnh ảo của vật sẽ di chuyển từ điểm cực cận (d' = 25 cm) ra đến vô cực, giúp người quan sát luôn nhìn rõ vật mà chỉ cần điều tiết mắt trong giới hạn cho phép",
        "Ảnh ảo biến thành ảnh thật và đảo ngược chiều",
        "Vật bị cháy đen do nhiệt độ tăng cao",
        "Ảnh bị thu nhỏ lại bé hơn kích thước ban đầu"
    ], 0, "Tại d1 = 7,14 cm thì d' = -25 cm (ảnh ở cực cận); tại d2 = 10 cm thì d' = ∞ (ảnh ở cực viễn). Đây là khoảng ngắm chừng của kính lúp."),
    make_vdc(3, "Để đo đường kính của một sợi tóc người bằng phương pháp quang học đơn giản, một nhóm học sinh đặt sợi tóc lên một thước đo milimét rồi quan sát qua kính lúp có số bội giác G = 5x (f = 5 cm). Trên ảnh ảo, sợi tóc có độ dày đo được là 0,4 mm khi độ phóng đại k = 4. Đường kính thực tế của sợi tóc này là:", [
        "0,1 mm (100 micromet)",
        "0,4 mm",
        "1,6 mm",
        "0,02 mm"
    ], 0, "Đường kính thực = Chiều dày ảnh / k = 0,4 mm / 4 = 0,1 mm = 100 µm."),
    make_vdc(4, "Một người thợ kim hoàn mua một kính lúp gấp gọn 3 lớp tròng (Triplet Loupe 10x). Thấu kính này gồm 3 thấu kính nhỏ dán sát nhau bằng keo quang học trong suốt. Thiết kế 3 lớp thấu kính ghép này có công dụng chính là gì so với kính lúp 1 thấu kính đơn giản?", [
        "Khử hiện tượng méo hình ở rìa thấu kính và khử hiện tượng tán sắc viền cầu vồng (sắc sai), cho hình ảnh đá quý phẳng và chuẩn xác màu sắc 100%",
        "Làm kính lúp có thể gập lại như dao xếp",
        "Giúp kính lúp không bị vỡ khi rơi từ trên cao",
        "Làm tăng nhiệt độ viên đá quý lên mức nóng chảy"
    ], 0, "Hệ thấu kính Triplet triệt tiêu sắc sai và cầu sai, giữ cho ảnh phẳng và đúng màu sắc của viên đá quý.")
]

exams["phys9_c6_b21_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b21", "Bài 21: Kính lúp", 3, p1_b21_t3, p2_b21_t3, p3_b21_t3, p4_b21_t3)

print("Added phys9_c6_b21 (3 tests).")
