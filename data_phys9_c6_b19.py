# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 19: THẤU KÍNH
Bao gồm 3 đề thi độc lập 100%: phys9_c6_b19_test1, phys9_c6_b19_test2, phys9_c6_b19_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c6"
CH_TITLE = "Chương VI: Ánh sáng"

# =============================================================================
# BÀI 19: THẤU KÍNH (3 ĐỀ)
# =============================================================================

# --- phys9_c6_b19_test1 ---
p1_b19_t1 = [
    make_mc(1, "Nhận biết", "Thấu kính hội tụ là thấu kính có đặc điểm hình học:", [
        "Phần rìa mỏng hơn phần giữa",
        "Phần rìa dày hơn phần giữa",
        "Phần rìa và phần giữa có độ dày hoàn toàn bằng nhau",
        "Bề mặt luôn luôn phẳng cả hai bên"
    ], 0, "Thấu kính hội tụ có phần rìa mỏng hơn phần giữa."),
    make_mc(2, "Nhận biết", "Thấu kính phân kì là thấu kính có đặc điểm hình học:", [
        "Phần rìa mỏng hơn phần giữa",
        "Phần rìa dày hơn phần giữa",
        "Có dạng hình cầu đặc",
        "Có một mặt lồi và một mặt phẳng"
    ], 1, "Thấu kính phân kì có phần rìa dày hơn phần giữa."),
    make_mc(3, "Nhận biết", "Chiếu một chùm tia sáng song song với trục chính đến thấu kính hội tụ thì chùm tia ló có tính chất:", [
        "Bị loe rộng ra xa trục chính",
        "Phản xạ ngược trở lại nguồn phát",
        "Hội tụ tại tiêu điểm chính của thấu kính",
        "Tiếp tục song song với nhau mãi mãi"
    ], 2, "Chùm tia tới song song với trục chính qua thấu kính hội tụ cho chùm tia ló hội tụ tại tiêu điểm chính."),
    make_mc(4, "Nhận biết", "Điểm chính giữa của thấu kính mà mọi tia sáng truyền qua điểm đó đều tiếp tục truyền thẳng không đổi hướng được gọi là:", [
        "Tiêu điểm chính",
        "Trục phụ",
        "Tâm đối xứng ngoài",
        "Quang tâm của thấu kính"
    ], 3, "Quang tâm O là điểm mà mọi tia sáng đi qua đều truyền thẳng."),
    make_mc(5, "Nhận biết", "Khoảng cách từ quang tâm O đến tiêu điểm chính F của thấu kính được gọi là:", [
        "Tiêu cự của thấu kính",
        "Bán kính cong",
        "Khoảng nhìn rõ",
        "Độ tụ hình học"
    ], 0, "OF = OF' = f gọi là tiêu cự của thấu kính."),
    make_mc(6, "Nhận biết", "Tia tới đi qua quang tâm O của thấu kính phân kì cho tia ló có đặc điểm:", [
        "Bị gãy khúc vuông góc với trục chính",
        "Tiếp tục truyền thẳng theo phương của tia tới",
        "Đi qua tiêu điểm chính F",
        "Hắt ngược trở lại môi trường tới"
    ], 1, "Mọi tia sáng đi qua quang tâm O (cả TKHT và TKPK) đều truyền thẳng."),
    make_mc(7, "Thông hiểu", "Đặt một vật sáng vuông góc với trục chính của thấu kính hội tụ ở khoảng cách d lớn hơn 2 lần tiêu cự (d > 2f). Ảnh thu được trên màn hứng ảnh có đặc điểm:", [
        "Ảnh ảo, cùng chiều và lớn hơn vật",
        "Ảnh ảo, ngược chiều và nhỏ hơn vật",
        "Ảnh thật, ngược chiều và nhỏ hơn vật",
        "Ảnh thật, cùng chiều và bằng vật"
    ], 2, "Khi d > 2f, qua TKHT cho ảnh thật, ngược chiều và nhỏ hơn vật."),
    make_mc(8, "Thông hiểu", "Đặt vật sáng trong khoảng tiêu cự của thấu kính hội tụ (d < f). Ảnh của vật quan sát được có đặc điểm là:", [
        "Ảnh thật, ngược chiều và nhỏ hơn vật",
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Không thể tạo được ảnh nào",
        "Ảnh ảo, cùng chiều và lớn hơn vật"
    ], 3, "Khi d < f (như kính lúp), ảnh thu được là ảnh ảo, cùng chiều và lớn hơn vật."),
    make_mc(9, "Thông hiểu", "Một vật sáng đặt trước thấu kính phân kì luôn cho:", [
        "Ảnh ảo, cùng chiều, nhỏ hơn vật và luôn nằm trong khoảng tiêu cự của thấu kính",
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Ảnh ảo, ngược chiều và bằng vật",
        "Ảnh thật, cùng chiều và nằm ngoài khoảng tiêu cự"
    ], 0, "Thấu kính phân kì luôn cho ảnh ảo, cùng chiều, nhỏ hơn vật và nằm trong khoảng OF."),
    make_mc(10, "Thông hiểu", "Để thu được ảnh thật bằng đúng kích thước của vật (ảnh thật cao bằng vật) qua thấu kính hội tụ có tiêu cự f, ta phải đặt vật cách thấu kính một khoảng bằng:", [
        "d = f",
        "d = 2f",
        "d = 0,5f",
        "d = 3f"
    ], 1, "Khi d = 2f thì d' = 2f và chiều cao ảnh A'B' = AB."),
    make_mc(11, "Thông hiểu", "Chiếu tia tới đi qua tiêu điểm chính F của thấu kính hội tụ thì tia ló tương ứng có đường truyền:", [
        "Đi thẳng qua quang tâm O",
        "Cắt trục chính tại tiêu điểm F'",
        "Song song với trục chính của thấu kính",
        "Vuông góc với trục chính của thấu kính"
    ], 2, "Tia tới qua F thì tia ló song song với trục chính."),
    make_mc(12, "Thông hiểu", "Một người dùng thấu kính hội tụ có tiêu cự f = 10 cm để hứng ảnh của Mặt Trời lên một tờ giấy. Khoảng cách từ thấu kính đến tờ giấy khi vệt sáng thu được gom lại nhỏ nhất (cháy giấy) bằng:", [
        "5 cm",
        "20 cm",
        "15 cm",
        "10 cm"
    ], 3, "Mặt Trời ở rất xa (vô cực) nên chùm sáng coi như song song trục chính, hội tụ đúng tại tiêu điểm F', cách thấu kính d' = f = 10 cm.")
]

p2_b19_t1 = [
    make_tf(1, "Thông hiểu", "Xét các tính chất quang học của thấu kính hội tụ:", [
        ("a", "Thấu kính hội tụ có phần giữa dày hơn phần rìa.", True),
        ("b", "Chùm tia sáng tới song song với trục chính qua thấu kính hội tụ cho chùm tia ló loe rộng ra xa.", False),
        ("c", "Tia tới đi qua quang tâm O của thấu kính hội tụ thì truyền thẳng.", True),
        ("d", "Tiêu cự f là khoảng cách từ quang tâm O đến tiêu điểm F.", True)
    ], "Chùm song song qua TKHT cho chùm tia ló hội tụ tại tiêu điểm F'."),
    make_tf(2, "Thông hiểu", "Xét tính chất tạo ảnh của thấu kính phân kì:", [
        ("a", "Thấu kính phân kì có phần rìa dày hơn phần giữa.", True),
        ("b", "Vật thật đặt trước thấu kính phân kì luôn luôn cho ảnh ảo.", True),
        ("c", "Ảnh tạo bởi thấu kính phân kì có thể hứng được rõ nét trên màn chắn.", False),
        ("d", "Ảnh ảo của thấu kính phân kì luôn cùng chiều và nhỏ hơn vật.", True)
    ], "Ảnh ảo không hứng được trên màn chắn, chỉ quan sát được bằng mắt."),
    make_tf(3, "Vận dụng", "Đặt một vật sáng AB hình mũi tên cao 2 cm vuông góc với trục chính của thấu kính hội tụ có tiêu cự f = 12 cm. Vật cách thấu kính d = 24 cm:", [
        ("a", "Vật AB đang đặt tại vị trí cách thấu kính đúng bằng 2 lần tiêu cự (d = 2f).", True),
        ("b", "Ảnh A'B' thu được là ảnh thật, ngược chiều với vật.", True),
        ("c", "Khoảng cách từ thấu kính đến ảnh là d' = 24 cm.", True),
        ("d", "Chiều cao của ảnh A'B' bằng 4 cm.", False)
    ], "Khi d = 2f thì d' = 2f = 24 cm và ảnh bằng vật nên A'B' = AB = 2 cm."),
    make_tf(4, "Vận dụng", "Đặt vật sáng AB cao 4 cm trước một thấu kính hội tụ có tiêu cự f = 20 cm, cách thấu kính một đoạn d = 10 cm:", [
        ("a", "Vật nằm trong khoảng tiêu cự của thấu kính (d < f).", True),
        ("b", "Ảnh thu được là ảnh thật và có thể hứng được trên màn hứng phía sau thấu kính.", False),
        ("c", "Ảnh A'B' là ảnh ảo, cùng chiều và lớn hơn vật AB.", True),
        ("d", "Đây chính là nguyên lý tạo ảnh khi sử dụng thấu kính hội tụ làm kính lúp.", True)
    ], "d < f cho ảnh ảo, cùng chiều, lớn hơn vật, không hứng được trên màn.")
]

p3_b19_t1 = [
    make_sa(1, "Thông hiểu", "Một thấu kính hội tụ có tiêu cự f = 15 cm. Khoảng cách từ quang tâm O đến tiêu điểm F của thấu kính bằng bao nhiêu cm?", "15", "OF = f = 15 cm."),
    make_sa(2, "Thông hiểu", "Đặt vật sáng AB trước thấu kính phân kì. Ảnh thu được là ảnh thật hay ảnh ảo?", "Ảnh ảo", "Thấu kính phân kì luôn cho ảnh ảo đối với vật thật."),
    make_sa(3, "Vận dụng", "Một thấu kính hội tụ có tiêu cự f = 10 cm. Đặt một ngọn nến cách thấu kính d = 20 cm. Khoảng cách từ thấu kính đến màn hứng được ảnh rõ nét là bao nhiêu cm?", "20", "Vì d = 2f = 20 cm nên d' = 2f = 20 cm."),
    make_sa(4, "Vận dụng", "Vật sáng AB cao 2 cm đặt vuông góc với trục chính của thấu kính hội tụ có f = 10 cm, cách thấu kính d = 20 cm. Chiều cao của ảnh A'B' là bao nhiêu cm?", "2", "Tại d = 2f, ảnh thật bằng vật: A'B' = AB = 2 cm."),
    make_sa(5, "Vận dụng cao", "Đặt một vật sáng AB cách thấu kính hội tụ một đoạn d = 30 cm. Thấu kính có tiêu cự f = 20 cm. Tính khoảng cách từ ảnh đến thấu kính theo cm?", "60", "1/f = 1/d + 1/d' => 1/20 = 1/30 + 1/d' => 1/d' = 1/20 - 1/30 = 1/60 => d' = 60 cm."),
    make_sa(6, "Vận dụng cao", "Một vật sáng AB cao 3 cm đặt vuông góc với trục chính của thấu kính hội tụ có tiêu cự 20 cm, cách thấu kính d = 30 cm. Chiều cao của ảnh A'B' thu được trên màn bằng bao nhiêu cm?", "6", "d' = 60 cm. Độ phóng đại k = d'/d = 60/30 = 2 => A'B' = 2 × 3 = 6 cm.")
]

p4_b19_t1 = [
    make_vdc(1, "Một người dùng máy ảnh kỹ thuật số để chụp một bức tranh trên tường. Vật kính của máy ảnh là một thấu kính hội tụ có tiêu cự f = 50 mm. Để chụp được bức ảnh rõ nét của bức tranh trên cảm biến ảnh (màn hứng), vị trí của bức tranh so với vật kính phải thỏa mãn điều kiện:", [
        "Khoảng cách từ bức tranh đến vật kính lớn hơn hai lần tiêu cự (d > 2f)",
        "Khoảng cách từ bức tranh đến vật kính nhỏ hơn tiêu cự (d < f)",
        "Bức tranh phải đặt đúng tại tiêu điểm của vật kính (d = f)",
        "Bức tranh đặt sát vào bề mặt thấu kính"
    ], 0, "Máy ảnh tạo ảnh thật, ngược chiều và nhỏ hơn vật trên cảm biến, nên vật phải ở khoảng d > 2f."),
    make_vdc(2, "Trong thí nghiệm quang hình học, người ta dời một ngọn nến dọc theo trục chính của một thấu kính hội tụ từ rất xa (d >> 2f) lại gần quang tâm O. Khi ngọn nến đi qua vị trí cách thấu kính đúng 2f và tiến về phía tiêu điểm F, tính chất và kích thước của ảnh thật thay đổi như thế nào?", [
        "Ảnh thật di chuyển ra xa thấu kính hơn và kích thước ảnh ngày càng lớn hơn vật",
        "Ảnh thật di chuyển lại gần thấu kính hơn và kích thước nhỏ dần",
        "Ảnh biến thành ảnh ảo ngay khi dời qua 2f",
        "Ảnh biến mất hoàn toàn không thể quan sát được"
    ], 0, "Khi f < d < 2f, ảnh thật d' > 2f (dời xa thấu kính) và phóng đại ngày càng lớn."),
    make_vdc(3, "Mắt của một người bị tật cận thị không nhìn rõ các vật ở xa vì thủy tinh thể quá phồng, làm ảnh của vật ở vô cực hội tụ trước màng lưới. Để khắc phục tật cận thị này, người đó cần đeo kính cận là loại thấu kính nào?", [
        "Thấu kính phân kì có tiêu điểm trùng với điểm cực viễn của mắt",
        "Thấu kính hội tụ có tiêu cự rất ngắn",
        "Gương phẳng phân kì",
        "Kính màu lọc ánh sáng xanh"
    ], 0, "Kính cận là thấu kính phân kì giúp phân kì chùm sáng để ảnh lùi về hội tụ đúng trên màng lưới của mắt."),
    make_vdc(4, "Một hệ quang học gồm một thấu kính hội tụ L1 (f1 = 20 cm) và một thấu kính phân kì L2 (f2 = -10 cm) đặt đồng trục cách nhau một khoảng a = 10 cm. Chiếu một chùm tia sáng song song với trục chính tới L1. Chùm tia ló ra khỏi L2 có đặc điểm gì?", [
        "Là chùm tia sáng song song với trục chính",
        "Hội tụ tại một điểm cách L2 là 5 cm",
        "Bị tán sắc thành chùm tia bảy màu",
        "Phản xạ ngược trở lại nguồn sáng ban đầu"
    ], 0, "Chùm song song qua L1 hội tụ tại F1' cách L1 là 20 cm, tức cách L2 là 20 - 10 = 10 cm. Điểm này trùng đúng tiêu điểm F2 của L2 nên chùm ló ra khỏi L2 là chùm song song.")
]

exams["phys9_c6_b19_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b19", "Bài 19: Thấu kính", 1, p1_b19_t1, p2_b19_t1, p3_b19_t1, p4_b19_t1)

# --- phys9_c6_b19_test2 ---
p1_b19_t2 = [
    make_mc(1, "Nhận biết", "Trục chính của một thấu kính là đường thẳng:", [
        "Vuông góc với mặt thấu kính và đi qua quang tâm O",
        "Song song với bề mặt thấu kính",
        "Nối liền hai mép rìa của thấu kính",
        "Bất kì đi qua thấu kính"
    ], 0, "Trục chính Δ là đường thẳng vuông góc với mặt thấu kính tại quang tâm O."),
    make_mc(2, "Nhận biết", "Mỗi thấu kính mỏng có bao nhiêu tiêu điểm chính nằm trên trục chính đối xứng nhau qua quang tâm O?", [
        "Một tiêu điểm chính duy nhất",
        "Hai tiêu điểm chính F và F'",
        "Ba tiêu điểm chính",
        "Vô số tiêu điểm chính"
    ], 1, "Mỗi thấu kính có 2 tiêu điểm chính F và F' đối xứng nhau qua quang tâm O."),
    make_mc(3, "Nhận biết", "Chiếu chùm tia sáng tới song song với trục chính đến thấu kính phân kì thì chùm tia ló tương ứng:", [
        "Hội tụ tại tiêu điểm chính sau thấu kính",
        "Tiếp tục song song và giữ nguyên phương",
        "Bị loe rộng ra xa với đường kéo dài đi qua tiêu điểm chính của thấu kính",
        "Bị phản xạ ngược trở lại"
    ], 2, "Chùm tia ló của thấu kính phân kì loe rộng, có đường kéo dài đi qua tiêu điểm F."),
    make_mc(4, "Nhận biết", "Kí hiệu quy ước của thấu kính hội tụ trên hình vẽ quang học là:", [
        "Đoạn thẳng có hai đầu mũi tên hướng ra phía ngoài",
        "Đoạn thẳng có hai đầu mũi tên hướng vào phía trong",
        "Đoạn thẳng nét đứt không có mũi tên",
        "Hình tròn có dấu cộng ở giữa"
    ], 0, "Thấu kính hội tụ có rìa mỏng nên ký hiệu là đoạn thẳng có mũi tên hướng ra ngoài ở hai đầu."),
    make_mc(5, "Nhận biết", "Kí hiệu quy ước của thấu kính phân kì trên hình vẽ quang học là:", [
        "Đoạn thẳng có hai đầu mũi tên hướng vào trong (hoặc đuôi mũi tên)",
        "Đoạn thẳng có hai đầu mũi tên hướng ra ngoài",
        "Đường cong hình chữ S",
        "Hình tam giác cân"
    ], 0, "Thấu kính phân kì có rìa dày nên ký hiệu mũi tên hướng vào trong ở hai đầu."),
    make_mc(6, "Nhận biết", "Khi chiếu tia tới đi qua quang tâm O của thấu kính hội tụ, tia ló:", [
        "Tiếp tục truyền thẳng theo phương của tia tới",
        "Bị bẻ cong một góc 45 độ",
        "Đi qua tiêu điểm F'",
        "Song song với trục chính"
    ], 0, "Tia tới qua quang tâm O luôn truyền thẳng."),
    make_mc(7, "Thông hiểu", "Một vật sáng đặt trước thấu kính hội tụ ở khoảng cách f < d < 2f. Ảnh của vật thu được trên màn là:", [
        "Ảnh thật, ngược chiều và lớn hơn vật",
        "Ảnh thật, ngược chiều và nhỏ hơn vật",
        "Ảnh ảo, cùng chiều và lớn hơn vật",
        "Ảnh ảo, cùng chiều và nhỏ hơn vật"
    ], 0, "Trong khoảng f < d < 2f, TKHT cho ảnh thật, ngược chiều và lớn hơn vật."),
    make_mc(8, "Thông hiểu", "Khi đặt vật sáng đúng tại tiêu điểm F của thấu kính hội tụ (d = f) thì chùm tia ló ra khỏi thấu kính có đặc điểm:", [
        "Là chùm tia sáng song song với nhau (ảnh ở vô cực)",
        "Hội tụ tại một điểm cách thấu kính một đoạn f",
        "Phân kì loe rộng cắt nhau tại quang tâm O",
        "Phản xạ toàn phần trở lại vật"
    ], 0, "Vật tại F thì chùm tia ló là chùm song song, ảnh ở vô cực."),
    make_mc(9, "Thông hiểu", "Ảnh của một vật thật tạo bởi thấu kính phân kì có tính chất nào sau đây?", [
        "Luôn là ảnh ảo, cùng chiều và nhỏ hơn vật",
        "Luôn là ảnh thật, ngược chiều và lớn hơn vật",
        "Có thể là ảnh thật hoặc ảnh ảo tùy khoảng cách đặt vật",
        "Luôn lớn hơn vật và ở ngoài khoảng tiêu cự"
    ], 0, "TKPK luôn cho ảnh ảo, cùng chiều, nhỏ hơn vật."),
    make_mc(10, "Thông hiểu", "Tia tới song song với trục chính của thấu kính phân kì cho tia ló có đặc điểm:", [
        "Đường kéo dài của tia ló đi qua tiêu điểm chính F nằm ở cùng phía với tia tới",
        "Tia ló đi qua tiêu điểm F' nằm ở phía sau thấu kính",
        "Tia ló vuông góc với trục chính",
        "Tia ló truyền thẳng không đổi hướng"
    ], 0, "Tia tới song song trục chính qua TKPK cho tia ló phân kì có đường kéo dài đi qua tiêu điểm F ở phía trước."),
    make_mc(11, "Thông hiểu", "Để phân biệt nhanh một thấu kính là hội tụ hay phân kì bằng mắt và tay, ta có thể:", [
        "Dùng tay sờ xem phần rìa mỏng hơn phần giữa (hội tụ) hay phần rìa dày hơn phần giữa (phân kì)",
        "Cân khối lượng của thấu kính",
        "Ngửi mùi của chất liệu làm thấu kính",
        "Đo nhiệt độ sôi của thấu kính"
    ], 0, "Sờ phần rìa so với phần giữa: rìa mỏng là thấu kính hội tụ, rìa dày là thấu kính phân kì."),
    make_mc(12, "Thông hiểu", "Một vật sáng đặt cách thấu kính phân kì một khoảng d = 20 cm. Biết tiêu cự thấu kính là f = 20 cm. Ảnh của vật nằm cách thấu kính một khoảng bằng:", [
        "10 cm (về cùng phía với vật)",
        "20 cm (ở phía sau thấu kính)",
        "40 cm",
        "Vô cực"
    ], 0, "Công thức TKPK: 1/-f = 1/d + 1/d' => 1/-20 = 1/20 + 1/d' => 1/d' = -1/10 => d' = -10 cm (ảnh ảo cách TK 10 cm).")
]

p2_b19_t2 = [
    make_tf(1, "Thông hiểu", "Về đường đi của các tia sáng đặc biệt qua thấu kính hội tụ:", [
        ("a", "Tia tới song song với trục chính cho tia ló đi qua tiêu điểm chính F'.", True),
        ("b", "Tia tới đi qua quang tâm O tiếp tục truyền thẳng.", True),
        ("c", "Tia tới đi qua tiêu điểm F cho tia ló song song với trục chính.", True),
        ("d", "Tia tới bất kì đều bị bẻ gãy một góc vuông 90 độ.", False)
    ], "Đường truyền tuân theo 3 tia đặc biệt, không vuông góc ngẫu nhiên."),
    make_tf(2, "Thông hiểu", "Về ảnh tạo bởi thấu kính đối với vật sáng thật:", [
        ("a", "Ảnh thật luôn luôn ngược chiều với vật.", True),
        ("b", "Ảnh ảo tạo bởi thấu kính hội tụ luôn lớn hơn vật.", True),
        ("c", "Ảnh ảo tạo bởi thấu kính phân kì luôn nhỏ hơn vật.", True),
        ("d", "Thấu kính phân kì có thể tạo ra ảnh thật hứng được trên màn nếu vật ở rất xa.", False)
    ], "Vật thật qua TKPK luôn chỉ cho ảnh ảo nhỏ hơn vật, không bao giờ cho ảnh thật."),
    make_tf(3, "Vận dụng", "Đặt vật sáng AB cao 1 cm vuông góc với trục chính của thấu kính hội tụ có tiêu cự f = 15 cm. Vật đặt cách thấu kính d = 45 cm:", [
        ("a", "Vật đặt ngoài khoảng hai lần tiêu cự (d > 2f).", True),
        ("b", "Ảnh A'B' thu được trên màn chắn là ảnh thật, ngược chiều với vật.", True),
        ("c", "Khoảng cách từ thấu kính đến ảnh là d' = 22,5 cm.", True),
        ("d", "Chiều cao của ảnh A'B' lớn hơn 1 cm.", False)
    ], "1/d' = 1/15 - 1/45 = 2/45 => d' = 22,5 cm. k = 22,5/45 = 0,5 => A'B' = 0,5 cm < 1 cm."),
    make_tf(4, "Vận dụng", "Một thấu kính phân kì có tiêu cự f = 12 cm. Đặt một ngọn nến sáng cao 6 cm cách thấu kính d = 24 cm:", [
        ("a", "Ảnh của ngọn nến là ảnh ảo, cùng chiều với ngọn nến.", True),
        ("b", "Ảnh nằm trong khoảng tiêu cự của thấu kính.", True),
        ("c", "Khoảng cách từ ảnh ảo đến thấu kính là d' = 8 cm.", True),
        ("d", "Chiều cao ảnh ảo bằng 3 cm.", False)
    ], "1/d' = -1/12 - 1/24 = -3/24 = -1/8 => |d'| = 8 cm. k = 8/24 = 1/3 => A'B' = 6 × (1/3) = 2 cm.")
]

p3_b19_t2 = [
    make_sa(1, "Thông hiểu", "Một thấu kính phân kì có khoảng cách từ quang tâm đến tiêu điểm F là 18 cm. Tiêu cự f của thấu kính bằng bao nhiêu cm?", "18", "Tiêu cự f = OF = 18 cm."),
    make_sa(2, "Thông hiểu", "Ảnh ảo tạo bởi thấu kính hội tụ cùng chiều hay ngược chiều với vật?", "Cùng chiều", "Ảnh ảo qua thấu kính luôn cùng chiều với vật."),
    make_sa(3, "Vận dụng", "Đặt vật sáng AB cao 4 cm trước thấu kính hội tụ tại vị trí d = 2f. Chiều cao của ảnh A'B' thu được bằng bao nhiêu cm?", "4", "Tại d = 2f thì ảnh thật có chiều cao bằng vật: A'B' = AB = 4 cm."),
    make_sa(4, "Vận dụng", "Một thấu kính hội tụ có tiêu cự f = 15 cm. Đặt vật cách thấu kính d = 30 cm. Khoảng cách từ thấu kính đến ảnh d' bằng bao nhiêu cm?", "30", "d = 2f = 30 cm => d' = 2f = 30 cm."),
    make_sa(5, "Vận dụng cao", "Đặt vật sáng AB cách thấu kính hội tụ d = 15 cm. Tiêu cự thấu kính là f = 10 cm. Tính khoảng cách từ ảnh thật đến thấu kính theo cm?", "30", "1/d' = 1/10 - 1/15 = 1/30 => d' = 30 cm."),
    make_sa(6, "Vận dụng cao", "Vật sáng AB cao 2 cm đặt trước thấu kính hội tụ có f = 10 cm, cách thấu kính d = 15 cm. Chiều cao của ảnh thật A'B' bằng bao nhiêu cm?", "4", "d' = 30 cm. k = d'/d = 30/15 = 2 => A'B' = 2 × 2 = 4 cm.")
]

p4_b19_t2 = [
    make_vdc(1, "Kính lúp là một thấu kính hội tụ có tiêu cự ngắn (thường từ vài cm đến hơn 10 cm). Khi dùng kính lúp để đọc một dòng chữ in li ti trong từ điển, người quan sát phải đặt thấu kính ở vị trí nào so với trang sách?", [
        "Cách trang sách một khoảng nhỏ hơn tiêu cự của kính lúp (d < f)",
        "Cách trang sách đúng bằng hai lần tiêu cự (d = 2f)",
        "Cách trang sách lớn hơn hai lần tiêu cự (d > 2f)",
        "Đặt kính lúp cách xa trang sách từ 1 mét trở lên"
    ], 0, "Kính lúp cần tạo ảnh ảo, cùng chiều và lớn hơn vật nên phải đặt vật trong khoảng tiêu cự (d < f)."),
    make_vdc(2, "Máy chiếu phim trong rạp chiếu bóng sử dụng nguồn sáng mạnh chiếu qua tấm phim nhỏ, sau đó đi qua hệ thấu kính hội tụ (vật kính máy chiếu) để phóng đại hình ảnh lên màn chiếu khổng lồ ở khoảng cách xa. Khi đó, tấm phim phải được đặt ở vị trí nào so với thấu kính máy chiếu?", [
        "Trong khoảng từ một lần tiêu cự đến hai lần tiêu cự (f < d < 2f) và đặt lộn ngược tấm phim",
        "Đặt ngoài khoảng hai lần tiêu cự (d > 2f) và đặt xuôi chiều",
        "Đặt trong khoảng tiêu cự (d < f)",
        "Đặt tại đúng tiêu điểm F (d = f)"
    ], 0, "Muốn thu ảnh thật phóng đại lớn trên màn xa, vật phải đặt trong khoảng f < d < 2f và lộn ngược để ảnh thật ngược chiều thành thuận chiều."),
    make_vdc(3, "Mắt người già mắc tật lão thị thường gặp khó khăn khi đọc sách báo ở cự ly gần (khoảng 25 cm) do khả năng điều tiết của cơ thể mi suy giảm. Để khắc phục tật lão thị, người già cần đeo loại kính nào?", [
        "Kính hội tụ (kính viễn/lão) để đưa ảnh của vật ở gần lùi ra xa điểm cực cận của mắt",
        "Kính phân kì để làm giảm tiêu cự",
        "Kính râm chống tia cực tím",
        "Kính bảo hộ lao động phân cực"
    ], 0, "Kính lão là thấu kính hội tụ giúp hỗ trợ hội tụ chùm sáng từ vật ở gần lên đúng màng lưới."),
    make_vdc(4, "Một chùm tia sáng hội tụ truyền đến một thấu kính phân kì có tiêu cự f = 15 cm sao cho đỉnh hội tụ của chùm sáng nằm sau thấu kính cách quang tâm 10 cm. Chùm tia ló ra khỏi thấu kính phân kì sẽ:", [
        "Hội tụ tại một điểm nằm sau thấu kính cách quang tâm 30 cm",
        "Biến thành chùm tia phân kì không bao giờ cắt nhau",
        "Trở thành chùm tia song song với trục chính",
        "Phản xạ ngược lại nguồn sáng"
    ], 0, "Vật ảo d = -10 cm: 1/d' = -1/15 - 1/(-10) = -1/15 + 1/10 = 1/30 => d' = 30 cm (ảnh thật hội tụ sau thấu kính 30 cm).")
]

exams["phys9_c6_b19_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b19", "Bài 19: Thấu kính", 2, p1_b19_t2, p2_b19_t2, p3_b19_t2, p4_b19_t2)

# --- phys9_c6_b19_test3 ---
p1_b19_t3 = [
    make_mc(1, "Nhận biết", "Trong không khí, thấu kính làm bằng thủy tinh có dạng phẳng - lồi (một mặt phẳng, một mặt lồi) là loại thấu kính:", [
        "Thấu kính hội tụ",
        "Thấu kính phân kì",
        "Gương cầu lồi",
        "Bản mặt song song"
    ], 0, "Thấu kính phẳng - lồi có phần rìa mỏng hơn phần giữa nên là thấu kính hội tụ."),
    make_mc(2, "Nhận biết", "Trong không khí, thấu kính làm bằng thủy tinh có dạng phẳng - lõm (một mặt phẳng, một mặt lõm) là loại thấu kính:", [
        "Thấu kính hội tụ",
        "Thấu kính phân kì",
        "Gương cầu lõm",
        "Lăng kính phản xạ"
    ], 1, "Thấu kính phẳng - lõm có phần rìa dày hơn phần giữa nên là thấu kính phân kì."),
    make_mc(3, "Nhận biết", "Đặc điểm chung của quang tâm O ở cả thấu kính hội tụ và thấu kính phân kì là:", [
        "Tia sáng đi qua quang tâm O luôn truyền thẳng không đổi phương",
        "Là điểm hội tụ của mọi chùm tia sáng",
        "Luôn nằm ở mép ngoài của rìa thấu kính",
        "Là tiêu điểm có tiêu cự bằng 0"
    ], 0, "Mọi tia sáng truyền qua quang tâm O đều tiếp tục truyền thẳng."),
    make_mc(4, "Nhận biết", "Đường thẳng đi qua quang tâm O nhưng không vuông góc với bề mặt thấu kính được gọi là:", [
        "Trục phụ của thấu kính",
        "Trục chính của thấu kính",
        "Pháp tuyến tại rìa",
        "Đường phân giác chính"
    ], 0, "Đường thẳng qua O nhưng không vuông góc mặt thấu kính gọi là trục phụ."),
    make_mc(5, "Nhận biết", "Đối với thấu kính hội tụ, tiêu điểm vật chính F và tiêu điểm ảnh chính F' nằm ở:", [
        "Hai phía đối diện so với thấu kính và cách đều quang tâm O",
        "Cùng một phía duy nhất trước thấu kính",
        "Trùng khít lên quang tâm O",
        "Vô cực phía sau thấu kính"
    ], 0, "Hai tiêu điểm F và F' đối xứng nhau qua O: OF = OF' = f."),
    make_mc(6, "Nhận biết", "Thấu kính phân kì thường được dùng làm bộ phận quang học chính trong loại kính đeo nào sau đây?", [
        "Kính cận thị",
        "Kính lão thị",
        "Kính lúp đọc sách",
        "Kính viễn vọng thiên văn loại hội tụ"
    ], 0, "Kính cận thị là thấu kính phân kì giúp đưa ảnh của vật ở xa về trong khoảng nhìn rõ của mắt cận."),
    make_mc(7, "Thông hiểu", "Đặt một ngọn nến sáng trước thấu kính hội tụ ở khoảng cách d = 2f. Trên màn chắn đặt cách thấu kính d' = 2f ta thu được hình ảnh ngọn nến có đặc điểm:", [
        "Ảnh thật, ngược chiều và có kích thước bằng đúng ngọn nến thật",
        "Ảnh ảo, cùng chiều và lớn gấp đôi ngọn nến thật",
        "Ảnh thật, cùng chiều và nhỏ hơn ngọn nến thật",
        "Ảnh ảo, ngược chiều và bằng ngọn nến thật"
    ], 0, "Khi d = 2f thì d' = 2f, ảnh thật, ngược chiều và có kích thước đúng bằng vật thật."),
    make_mc(8, "Thông hiểu", "Một người đưa một thấu kính lại sát một trang sách rồi từ từ nâng thấu kính lên cao vài cm. Người đó quan sát thấy chữ viết trong trang sách to dần lên và luôn cùng chiều với chữ thật. Thấu kính người đó đang cầm là:", [
        "Thấu kính hội tụ (quan sát trong khoảng d < f)",
        "Thấu kính phân kì",
        "Gương phẳng tráng bạc",
        "Kính râm phân cực"
    ], 0, "TKHT khi d < f cho ảnh ảo cùng chiều và phóng đại lớn hơn vật."),
    make_mc(9, "Thông hiểu", "Một chùm tia sáng loe rộng phát ra từ một bóng đèn nhỏ đặt tại đúng tiêu điểm chính F của thấu kính hội tụ. Sau khi đi qua thấu kính, chùm tia ló trở thành:", [
        "Chùm tia sáng song song với trục chính của thấu kính",
        "Chùm tia hội tụ tại điểm 2f",
        "Chùm tia phân kì loe rộng hơn nữa",
        "Bị hấp thụ hoàn toàn thành nhiệt"
    ], 0, "Tia tới xuất phát từ F cho chùm tia ló song song với trục chính."),
    make_mc(10, "Thông hiểu", "Ảnh của một cột điện ở rất xa (coi như ở vô cực d = ∞) tạo bởi một thấu kính hội tụ có tiêu cự f = 50 cm sẽ nằm cách thấu kính một đoạn bằng:", [
        "Đúng 50 cm",
        "100 cm",
        "25 cm",
        "Vô cực"
    ], 0, "Vật ở vô cực qua TKHT cho ảnh thật tại tiêu diện ảnh, cách thấu kính đúng bằng tiêu cự: d' = f = 50 cm."),
    make_mc(11, "Thông hiểu", "Đặt một vật sáng vuông góc với trục chính của thấu kính phân kì có tiêu cự f = 15 cm. Dù dời vật đến bất kỳ vị trí nào trước thấu kính (với d > 0), khoảng cách d' từ ảnh đến thấu kính luôn thoả mãn:", [
        "d' < 15 cm",
        "d' > 15 cm",
        "d' = 30 cm",
        "d' > 30 cm"
    ], 0, "Ảnh ảo của vật thật qua TKPK luôn nằm trong khoảng tiêu cự (d' < f = 15 cm)."),
    make_mc(12, "Thông hiểu", "Một ngọn nến đặt trước thấu kính hội tụ tạo một vệt sáng mờ trên màn hứng. Để thu được ảnh thật sắc nét nhất của ngọn nến trên màn, người làm thí nghiệm cần làm gì?", [
        "Điều chỉnh từ từ khoảng cách giữa ngọn nến, thấu kính và màn hứng ảnh cho đến khi ảnh nét nhất",
        "Thổi tắt ngọn nến",
        "Bật thêm đèn chiếu sáng trong phòng thí nghiệm",
        "Thay màn hứng bằng một tấm gương soi"
    ], 0, "Phải tịnh tiến màn hứng dọc theo trục chính để tìm đúng vị trí tạo ảnh nét rõ nhất.")
]

p2_b19_t3 = [
    make_tf(1, "Thông hiểu", "Xét hình dạng và tính chất quang học cơ bản của các loại thấu kính:", [
        ("a", "Thấu kính hội tụ biến chùm tia tới song song trục chính thành chùm tia ló hội tụ.", True),
        ("b", "Thấu kính phân kì biến chùm tia tới song song trục chính thành chùm tia ló phân kì.", True),
        ("c", "Thấu kính hội tụ luôn có hai mặt lồi hình cầu.", False),
        ("d", "Vật liệu làm thấu kính phải là môi trường trong suốt đối với ánh sáng.", True)
    ], "TKHT có thể có dạng một mặt lồi một mặt phẳng, hoặc hai mặt lồi, hoặc một mặt lồi một mặt lõm (rìa mỏng)."),
    make_tf(2, "Thông hiểu", "Đặc điểm tạo ảnh của thấu kính phân kì:", [
        ("a", "Khoảng cách từ ảnh ảo đến thấu kính phân kì luôn nhỏ hơn tiêu cự f của thấu kính.", True),
        ("b", "Khi dời vật ra xa thấu kính phân kì thì ảnh ảo cũng dời dần về phía tiêu điểm F.", True),
        ("c", "Ảnh ảo tạo bởi thấu kính phân kì luôn có kích thước lớn hơn vật thật.", False),
        ("d", "Mắt người nhìn qua thấu kính phân kì có thể quan sát thấy ảnh ảo nhỏ hơn vật.", True)
    ], "Ảnh ảo tạo bởi TKPK luôn nhỏ hơn vật thật."),
    make_tf(3, "Vận dụng", "Đặt vật sáng AB cao 3 cm vuông góc trục chính thấu kính hội tụ có f = 10 cm, vật cách thấu kính d = 5 cm:", [
        ("a", "Vật đặt trong khoảng tiêu cự của thấu kính (d < f).", True),
        ("b", "Ảnh thu được là ảnh ảo, cùng chiều với vật.", True),
        ("c", "Khoảng cách từ ảnh ảo đến thấu kính là d' = 10 cm.", True),
        ("d", "Chiều cao của ảnh ảo A'B' bằng 6 cm.", True)
    ], "1/d' = 1/10 - 1/5 = -1/10 => |d'| = 10 cm. k = 10/5 = 2 => A'B' = 2 × 3 = 6 cm."),
    make_tf(4, "Vận dụng", "Một thấu kính hội tụ có tiêu cự f = 12 cm. Đặt ngọn nến ở vị trí d1 = 8 cm và sau đó dời đến d2 = 18 cm:", [
        ("a", "Ở vị trí d1 = 8 cm, thấu kính cho ảnh ảo lớn hơn ngọn nến.", True),
        ("b", "Ở vị trí d2 = 18 cm, thấu kính cho ảnh thật lớn hơn ngọn nến.", True),
        ("c", "Ở cả hai vị trí, ảnh đều hứng được trên màn chắn phía sau thấu kính.", False),
        ("d", "Nếu đặt ngọn nến tại d = 12 cm thì không thu được ảnh trên màn hứng ở khoảng cách hữu hạn.", True)
    ], "Tại d1 = 8 cm < f tạo ảnh ảo nên không thể hứng trên màn chắn.")
]

p3_b19_t3 = [
    make_sa(1, "Thông hiểu", "Một thấu kính hội tụ có tiêu cự f = 25 cm. Khoảng cách giữa hai tiêu điểm chính F và F' của thấu kính bằng bao nhiêu cm?", "50", "FF' = 2f = 2 × 25 = 50 cm."),
    make_sa(2, "Thông hiểu", "Khi vật sáng thật đặt ở rất xa (vô cực) trước thấu kính hội tụ có f = 12 cm thì ảnh thật của vật cách thấu kính bao nhiêu cm?", "12", "Vật ở vô cực cho ảnh tại tiêu diện d' = f = 12 cm."),
    make_sa(3, "Vận dụng", "Đặt vật sáng AB cao 5 cm cách thấu kính hội tụ một đoạn d = 2f. Chiều cao của ảnh A'B' thu được là bao nhiêu cm?", "5", "Tại d = 2f, ảnh thật bằng vật nên A'B' = 5 cm."),
    make_sa(4, "Vận dụng", "Một thấu kính hội tụ có f = 20 cm. Phải đặt ngọn nến cách thấu kính bao nhiêu cm để thu được ảnh thật bằng đúng ngọn nến?", "40", "d = 2f = 2 × 20 = 40 cm."),
    make_sa(5, "Vận dụng cao", "Đặt vật sáng AB cách thấu kính hội tụ một khoảng d = 60 cm. Thấu kính có tiêu cự f = 20 cm. Khoảng cách từ thấu kính đến ảnh thật d' bằng bao nhiêu cm?", "30", "1/d' = 1/20 - 1/60 = 2/60 = 1/30 => d' = 30 cm."),
    make_sa(6, "Vận dụng cao", "Vật sáng AB cao 4 cm đặt cách thấu kính hội tụ d = 60 cm (f = 20 cm). Chiều cao ảnh thật A'B' bằng bao nhiêu cm?", "2", "d' = 30 cm. k = d'/d = 30/60 = 0,5 => A'B' = 4 × 0,5 = 2 cm.")
]

p4_b19_t3 = [
    make_vdc(1, "Kính thiên văn khúc xạ Kepler gồm hai thấu kính hội tụ: vật kính có tiêu cự f1 rất dài và thị kính có tiêu cự f2 rất ngắn. Để quan sát được hình ảnh của một ngôi sao ở xa vô cực qua kính thiên văn ở trạng thái mắt không phải điều tiết (ngắm chừng ở vô cực), khoảng cách giữa hai thấu kính này phải được điều chỉnh bằng:", [
        "Tổng tiêu cự của hai thấu kính: L = f1 + f2",
        "Hiệu tiêu cự của hai thấu kính: L = f1 - f2",
        "Tích tiêu cự của hai thấu kính: L = f1 × f2",
        "Thương số giữa hai tiêu cự: L = f1 / f2"
    ], 0, "Khi ngắm chừng ở vô cực, tiêu điểm ảnh của vật kính F1' trùng với tiêu điểm vật F2 của thị kính, khoảng cách giữa 2 thấu kính là L = f1 + f2."),
    make_vdc(2, "Một người thợ kim hoàn sử dụng một thấu kính hội tụ mỏng có tiêu cự f = 10 cm để kiểm tra một viên ngọc bích quý. Người đó muốn thu được ảnh ảo phóng đại gấp 5 lần viên ngọc bích để soi rõ các vân đá bên trong. Khoảng cách đặt viên ngọc trước thấu kính là:", [
        "8 cm",
        "5 cm",
        "2 cm",
        "10 cm"
    ], 0, "Ảnh ảo phóng đại k = 5: d' = -5d. 1/f = 1/d + 1/d' => 1/10 = 1/d - 1/(5d) = 4/(5d) => 5d = 40 => d = 8 cm."),
    make_vdc(3, "Mắt của một người nhìn rõ các vật từ 50 cm đến vô cực (mắt viễn thị). Để người này có thể đọc sách ở khoảng cách bình thường 25 cm như mắt tốt, người đó phải đeo một kính có độ tụ thích hợp. Bản chất của thấu kính mà người này cần đeo là:", [
        "Thấu kính hội tụ có tiêu cự f = 50 cm",
        "Thấu kính phân kì có tiêu cự f = 25 cm",
        "Thấu kính hội tụ có tiêu cự f = 25 cm",
        "Thấu kính phân kì có tiêu cự f = 50 cm"
    ], 0, "Vật tại d = 25 cm cho ảnh ảo tại điểm cực cận d' = -50 cm: 1/f = 1/25 - 1/50 = 1/50 => f = 50 cm (thấu kính hội tụ)."),
    make_vdc(4, "Một thấu kính hội tụ bằng thủy tinh đặt trong không khí có tiêu cự f = 20 cm. Nếu nhúng chìm hoàn toàn thấu kính này vào trong một bể nước trong suốt (biết chiết suất của nước lớn hơn không khí nhưng nhỏ hơn thủy tinh) thì tiêu cự của thấu kính trong nước sẽ:", [
        "Tăng lên lớn hơn 20 cm vì độ chênh lệch chiết suất giữa thấu kính và môi trường nước giảm đi",
        "Giảm xuống nhỏ hơn 20 cm vì nước có lực đẩy Ác-si-mét",
        "Không thay đổi chút nào và vẫn bằng 20 cm",
        "Biến thành tiêu cự âm và thấu kính trở thành phân kì"
    ], 0, "Theo công thức chế tạo thấu kính, khi chênh lệch chiết suất (n_kính/n_môi_trường - 1) giảm thì khả năng bẻ gãy tia sáng giảm, dẫn đến tiêu cự f tăng lên.")
]

exams["phys9_c6_b19_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b19", "Bài 19: Thấu kính", 3, p1_b19_t3, p2_b19_t3, p3_b19_t3, p4_b19_t3)

print("Added phys9_c6_b19 (3 tests).")
