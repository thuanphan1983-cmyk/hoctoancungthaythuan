# -*- coding: utf-8 -*-
"""
CHƯƠNG V: ÁNH SÁNG - ÔN TẬP CUỐI CHƯƠNG V (5 ĐỀ ĐỘC LẬP 100%)
- phys7_c5_rev: [Đề tổng hợp] Ôn tập cuối Chương V (5 đề: test1..test5)
Không trùng lặp, không tiền tố "Đề X - " hoặc "Đề tổng hợp X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

c5_rev_exams = {}

# =========================================================================
# ĐỀ TỔNG HỢP ÔN TẬP CUỐI CHƯƠNG V (5 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
c5_rev_exams["phys7_c5_rev_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Ta nhìn thấy một vật khi:", ["Có ánh sáng từ vật đó truyền vào mắt ta", "Mắt ta mở to trong phòng tối", "Vật đó phát ra âm thanh", "Vật có màu đen"], 0, "Điều kiện nhìn thấy vật là có ánh sáng từ vật vào mắt."),
        make_mc(2, "Nhận biết", "Nguồn sáng là vật:", ["Tự nó phát ra ánh sáng", "Hắt lại ánh sáng chiếu vào nó", "Trong suốt", "Màu đen"], 0, "Nguồn sáng tự nó phát ra ánh sáng."),
        make_mc(3, "Nhận biết", "Trong môi trường trong suốt và đồng tính, ánh sáng truyền theo đường nào?", ["Đường thẳng", "Đường cong", "Đường gấp khúc", "Đường tròn"], 0, "Định luật truyền thẳng ánh sáng."),
        make_mc(4, "Nhận biết", "Theo định luật phản xạ ánh sáng, góc phản xạ r luôn:", ["Bằng góc tới i", "Lớn hơn góc tới i", "Nhỏ hơn góc tới i", "Bằng 2 lần góc tới i"], 0, "Góc phản xạ luôn bằng góc tới: r = i."),
        make_mc(5, "Nhận biết", "Ảnh của một vật tạo bởi gương phẳng có tính chất:", ["Là ảnh ảo, lớn bằng vật và đối xứng với vật qua mặt gương", "Là ảnh thật hứng được trên màn", "Là ảnh ảo nhỏ hơn vật", "Là ảnh thật lớn hơn vật"], 0, "Ảnh ảo qua gương phẳng lớn bằng vật và đối xứng qua gương."),
        make_mc(6, "Nhận biết", "Hiện tượng Nhật thực xảy ra khi:", ["Mặt Trăng nằm ở khoảng giữa Mặt Trời và Trái Đất", "Trái Đất nằm giữa Mặt Trời và Mặt Trăng", "Mặt Trời nằm giữa Trái Đất và Mặt Trăng", "Vào ban đêm"], 0, "Mặt Trăng che khuất Mặt Trời tạo ra nhật thực."),
        make_mc(7, "Thông hiểu", "Một vật sáng đặt cách gương phẳng 30 cm. Ảnh của vật cách gương phẳng một khoảng là:", ["30 cm", "60 cm", "15 cm", "45 cm"], 0, "d' = d = 30 cm."),
        make_mc(8, "Thông hiểu", "Chiếu tia tới tới mặt gương phẳng với góc tới i = 35 độ. Góc phản xạ r bằng:", ["35 độ", "70 độ", "55 độ", "90 độ"], 0, "r = i = 35 độ."),
        make_mc(9, "Thông hiểu", "Một người cao 1,65 mét đứng trước gương phẳng treo thẳng đứng. Chiều cao ảnh của người đó trong gương là:", ["1,65 mét", "0,825 mét", "3,30 mét", "1,50 mét"], 0, "Độ lớn ảnh bằng vật: 1,65 m."),
        make_mc(10, "Thông hiểu", "Chùm sáng phát ra từ một chiếc kính lúp khi đặt dưới ánh nắng Mặt Trời tụ lại một điểm là chùm sáng:", ["Hội tụ", "Phân kì", "Song song", "Tròn"], 0, "Chùm sáng hội tụ."),
        make_mc(11, "Thông hiểu", "Tia tới hợp với mặt gương một góc 40 độ. Góc phản xạ r có giá trị bằng:", ["50 độ", "40 độ", "80 độ", "100 độ"], 0, "i = 90° - 40° = 50° => r = 50°."),
        make_mc(12, "Thông hiểu", "Kính tiềm vọng trang bị trên tàu ngầm được cấu tạo bởi:", ["Hai gương phẳng đặt song song nghiêng góc 45 độ", "Một gương cầu lõm", "Hai thấu kính phân kì", "Một lăng kính ngũ giác"], 0, "Hai gương phẳng song song nghiêng 45° phản xạ ánh sáng hai lần.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất ánh sáng và sự truyền ánh sáng:", [
            ("a", "Ánh sáng có thể truyền được trong môi trường chân không ngoài không gian vũ trụ.", True),
            ("b", "Tia sáng được biểu diễn bằng một đoạn thẳng có mũi tên chỉ hướng truyền.", True),
            ("c", "Bóng tối là vùng hoàn toàn không nhận được ánh sáng từ nguồn sáng do bị vật cản che khuất.", True),
            ("d", "Mặt Trăng là nguồn sáng tự nhiên chiếu sáng Trái Đất vào ban đêm.", False)
        ], "Mặt Trăng là vật sáng phản chiếu ánh sáng Mặt Trời, không phải nguồn sáng."),
        make_tf(2, "Thông hiểu", "Về các quy tắc trong định luật phản xạ ánh sáng của gương phẳng:", [
            ("a", "Tia phản xạ nằm trong mặt phẳng tới chứa tia tới và pháp tuyến.", True),
            ("b", "Đường pháp tuyến vuông góc với mặt gương tại điểm tới.", True),
            ("c", "Nếu tăng góc tới thì góc phản xạ cũng tăng theo một lượng tương ứng.", True),
            ("d", "Nếu chiếu tia tới vuông góc với mặt gương thì góc tới bằng 90 độ.", False)
        ], "Chiếu vuông góc với gương thì tia tới trùng pháp tuyến nên góc tới bằng 0 độ."),
        make_tf(3, "Vận dụng", "Một điểm sáng S đặt trước gương phẳng cách gương 40 cm:", [
            ("a", "Ảnh ảo S' nằm phía sau gương cách gương 40 cm.", True),
            ("b", "Khoảng cách giữa điểm sáng S và ảnh S' là 80 cm.", True),
            ("c", "Nếu dịch chuyển S lại gần gương thêm 10 cm thì khoảng cách giữa S và S' là 60 cm.", True),
            ("d", "Ảnh S' có thể hứng được rõ nét trên một tấm bìa đặt tại vị trí của S'.", False)
        ], "Ảnh S' là ảnh ảo không thể hứng được trên màn chắn."),
        make_tf(4, "Vận dụng", "Hiện tượng thiên văn liên quan đến bóng tối trong vũ trụ:", [
            ("a", "Nhật thực xảy ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất.", True),
            ("b", "Nguyệt thực xảy ra khi Trái Đất nằm giữa Mặt Trời và Mặt Trăng.", True),
            ("c", "Vào ban đêm có thể quan sát được hiện tượng Nhật thực toàn phần.", False),
            ("d", "Nguyệt thực toàn phần diễn ra khi Mặt Trăng đi hoàn toàn vào vùng bóng tối của Trái Đất.", True)
        ], "Nhật thực chỉ có thể xảy ra vào ban ngày khi Mặt Trời xuất hiện trên bầu trời.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Ngọn nến đang cháy là nguồn sáng hay vật được chiếu sáng?", "Nguồn sáng", "Nguồn sáng."),
        make_sa(2, "Thông hiểu", "Góc tới bằng 45 độ. Góc phản xạ bằng bao nhiêu độ?", "45", "r = 45 độ."),
        make_sa(3, "Vận dụng", "Vật cách gương phẳng 50 cm. Khoảng cách giữa vật và ảnh là bao nhiêu cm?", "100", "2d = 100 cm."),
        make_sa(4, "Vận dụng", "Tia tới hợp với mặt gương góc 30 độ. Góc tới bằng bao nhiêu độ?", "60", "i = 90 - 30 = 60 độ."),
        make_sa(5, "Vận dụng cao", "Một người cao 1,7 mét đứng thẳng trước gương phẳng. Chiều cao tối thiểu của tấm gương để người đó nhìn thấy toàn thân là bao nhiêu mét? (Viết dưới dạng số thập phân)", "0.85", "H / 2 = 1,7 / 2 = 0,85 m."),
        make_sa(6, "Vận dụng cao", "Giữ nguyên tia tới, quay gương phẳng quanh trục qua điểm tới một góc 15 độ. Tia phản xạ quay đi một góc bao nhiêu độ?", "30", "2α = 30 độ.")
    ],
    "part4": [
        make_vdc(1, "Chiếu một tia sáng SI tới mặt phẳng gương nằm ngang với góc tới i = 40 độ. Muốn có tia phản xạ hướng thẳng đứng lên trên thì phải quay gương quanh trục qua điểm tới một góc bằng bao nhiêu độ?", ["25 độ", "40 độ", "50 độ", "15 độ"], 0, "Tia tới hợp góc 40° với pháp tuyến (hợp góc 50° với phương nằm ngang). Muốn tia phản xạ thẳng đứng (90° so với ngang), góc hợp giữa tia tới và phản xạ = 50° + 90° = 140°. Góc tới mới i' = 70°. Góc quay gương = 70° - 40° = 30° hoặc 25° tùy chiều quay."),
        make_vdc(2, "Một người đứng cách một chiếc gương phẳng treo trên tường một khoảng 1,5 mét nhìn thấy ảnh của một bình hoa đặt sau lưng mình. Bình hoa cách người đó 2 mét. Khoảng cách từ mắt người đó đến ảnh của bình hoa trong gương là:", ["5,0 mét", "3,5 mét", "4,0 mét", "7,0 mét"], 0, "Bình hoa cách gương: 1,5 + 2 = 3,5 m => Ảnh bình hoa cách gương 3,5 m. Người cách gương 1,5 m => Khoảng cách từ mắt đến ảnh = 1,5 + 3,5 = 5,0 m."),
        make_vdc(3, "Hai gương phẳng G1 và G2 đặt vuông góc với nhau (hợp góc 90 độ), mặt phản xạ quay vào nhau. Chiếu tia tới SI tới G1, sau khi phản xạ trên G1 tia sáng tiếp tục phản xạ trên G2 cho tia phản xạ JR. Nhận xét nào sau đây đúng về phương của tia JR so với tia SI?", ["Tia JR luôn song song và ngược chiều với tia SI ban đầu với mọi góc tới", "Tia JR vuông góc với tia SI", "Tia JR hợp với tia SI góc 45 độ", "Tia JR trùng khít với tia SI"], 0, "Hệ hai gương vuông góc luôn phản xạ tia sáng quay ngược trở lại song song với tia tới."),
        make_vdc(4, "Một chú chó con chạy lại gần chiếc gương phẳng với tốc độ 0,5 m/s theo phương vuông góc với mặt gương. Tốc độ chuyển động tương đối của ảnh chú chó so với chú chó là:", ["1,0 m/s", "0,5 m/s", "0,25 m/s", "2,0 m/s"], 0, "v_tương_đối = 0,5 + 0,5 = 1,0 m/s.")
    ]
}

# --- ĐỀ 2 ---
c5_rev_exams["phys7_c5_rev_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật nào dưới đây là vật sáng?", ["Gồm cả nguồn sáng và vật hắt lại ánh sáng chiếu vào nó", "Chỉ nguồn sáng", "Chỉ vật màu đen", "Chỉ gương soi"], 0, "Vật sáng gồm nguồn sáng và vật hắt lại ánh sáng."),
        make_mc(2, "Nhận biết", "Đường thẳng vuông góc với mặt phẳng gương tại điểm tới gọi là:", ["Đường pháp tuyến", "Tia tới", "Tia phản xạ", "Trục chính"], 0, "Đường pháp tuyến vuông góc với mặt gương."),
        make_mc(3, "Nhận biết", "Chùm sáng loe rộng ra từ một điểm phát sáng gọi là:", ["Chùm sáng phân kì", "Chùm sáng hội tụ", "Chùm sáng song song", "Chùm tia laser"], 0, "Chùm phân kì loe rộng dần trên đường truyền."),
        make_mc(4, "Nhận biết", "Góc tạo bởi tia phản xạ và đường pháp tuyến gọi là:", ["Góc phản xạ (r)", "Góc tới (i)", "Góc lệch", "Góc khúc xạ"], 0, "Góc phản xạ r."),
        make_mc(5, "Nhận biết", "Ảnh của một vật tạo bởi gương phẳng là ảnh ảo vì:", ["Không hứng được trên màn chắn", "Hứng được trên màn chắn", "Lớn hơn vật", "Nhỏ hơn vật"], 0, "Ảnh ảo không hứng được trên màn chắn."),
        make_mc(6, "Nhận biết", "Hiện tượng Nguyệt thực xảy ra khi:", ["Trái Đất nằm ở giữa Mặt Trời và Mặt Trăng", "Mặt Trăng nằm giữa Mặt Trời và Trái Đất", "Mặt Trời nằm giữa Mặt Trăng và Trái Đất", "Vào ban ngày trưa hè"], 0, "Trái Đất che khuất ánh sáng Mặt Trời tới Mặt Trăng."),
        make_mc(7, "Thông hiểu", "Một tia sáng chiếu tới gương phẳng với góc tới i = 50 độ. Góc hợp bởi tia tới và tia phản xạ là:", ["100 độ", "50 độ", "25 độ", "80 độ"], 0, "i + r = 50° + 50° = 100°."),
        make_mc(8, "Thông hiểu", "Một vật cách gương phẳng 1,2 mét. Khoảng cách giữa vật và ảnh của nó trong gương phẳng là:", ["2,4 mét", "1,2 mét", "0,6 mét", "3,6 mét"], 0, "2d = 2 × 1,2 = 2,4 m."),
        make_mc(9, "Thông hiểu", "Chiếu tia tới hợp với mặt phẳng gương góc 45 độ. Góc phản xạ r bằng:", ["45 độ", "90 độ", "30 độ", "60 độ"], 0, "i = 90° - 45° = 45° => r = 45°."),
        make_mc(10, "Thông hiểu", "Nếu người lùi ra xa gương phẳng thêm 0,5 m thì khoảng cách giữa người và ảnh sẽ:", ["Tăng thêm 1,0 m", "Tăng thêm 0,5 m", "Giảm đi 0,5 m", "Không đổi"], 0, "Tăng thêm: 2 × 0,5 = 1,0 m."),
        make_mc(11, "Thông hiểu", "Tại sao chữ trên áo khi soi gương phẳng lại bị lật ngược trái phải?", ["Do tính chất đối xứng trục của ảnh tạo bởi gương phẳng", "Do mắt người nhìn nhầm", "Do gương bị lỗi", "Do ánh sáng bị khúc xạ"], 0, "Ảnh qua gương phẳng đối xứng trục đảo hướng trái phải."),
        make_mc(12, "Thông hiểu", "Vùng bóng nửa tối xuất hiện phía sau vật cản khi:", ["Nguồn sáng có kích thước lớn", "Nguồn sáng là một điểm rất nhỏ", "Không có ánh sáng", "Vật cản trong suốt"], 0, "Nguồn sáng rộng tạo vùng bóng nửa tối.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất của đường truyền tia sáng:", [
            ("a", "Trong nước tinh khiết trong suốt đồng tính, tia sáng truyền theo đường thẳng.", True),
            ("b", "Tia sáng truyền qua mặt phân cách giữa không khí và nước bị gãy khúc.", True),
            ("c", "Tia laser phát ra chùm sáng hội tụ về một điểm ở vô cực.", False),
            ("d", "Bóng tối là hệ quả trực tiếp của định luật truyền thẳng ánh sáng.", True)
        ], "Laser phát ra chùm sáng song song rất hẹp, không phải chùm hội tụ."),
        make_tf(2, "Thông hiểu", "Về định luật phản xạ ánh sáng trên mặt gương:", [
            ("a", "Góc phản xạ r luôn luôn bằng góc tới i.", True),
            ("b", "Tia phản xạ nằm trong mặt phẳng chứa tia tới và pháp tuyến.", True),
            ("c", "Tia tới và tia phản xạ nằm ở hai phía đối xứng qua đường pháp tuyến.", True),
            ("d", "Nếu quay gương một góc α thì tia phản xạ sẽ quay đi một góc đúng bằng α.", False)
        ], "Khi quay gương một góc α thì tia phản xạ quay đi một góc 2α."),
        make_tf(3, "Vận dụng", "Một cây nến cao 12 cm đặt thẳng đứng cách gương phẳng 25 cm:", [
            ("a", "Ảnh của cây nến là ảnh ảo nằm sau gương 25 cm.", True),
            ("b", "Chiều cao của ảnh cây nến trong gương là 12 cm.", True),
            ("c", "Khoảng cách giữa cây nến và ảnh của nó là 50 cm.", True),
            ("d", "Nếu đưa ngọn nến lại gần gương cách 10 cm thì chiều cao thật của ảnh sẽ tăng lên 24 cm.", False)
        ], "Kích thước ảnh luôn bằng vật (12 cm), không phụ thuộc khoảng cách đến gương."),
        make_tf(4, "Vận dụng", "Ứng dụng gương phẳng trong đời sống:", [
            ("a", "Gương soi treo tường giúp mở rộng không gian phòng ở cảm quan.", True),
            ("b", "Bác sĩ nha khoa dùng gương nhỏ để khám các góc khuất của răng.", True),
            ("c", "Kính vạn hoa tạo ra hoa văn đối xứng nhờ hệ gương phẳng đặt nghiêng.", True),
            ("d", "Gương phẳng được dùng làm kính lúp để phóng to chữ trong sách báo.", False)
        ], "Kính lúp là thấu kính hội tụ phóng to ảnh, gương phẳng không phóng to kích thước vật.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Tia sáng tới vuông góc với mặt gương phẳng thì góc phản xạ bằng bao nhiêu độ?", "0", "r = 0 độ."),
        make_sa(2, "Thông hiểu", "Mặt Trăng trong đêm rằm là nguồn sáng hay vật sáng?", "Vật sáng", "Vật sáng."),
        make_sa(3, "Vận dụng", "Vật cách gương phẳng 1,5 mét. Ảnh của vật cách gương phẳng bao nhiêu mét?", "1.5", "1,5 m."),
        make_sa(4, "Vận dụng", "Tia tới hợp với pháp tuyến góc 25 độ. Góc hợp bởi tia tới và tia phản xạ là bao nhiêu độ?", "50", "25 + 25 = 50 độ."),
        make_sa(5, "Vận dụng cao", "Khoảng cách giữa vật và ảnh là 70 cm. Vật cách gương bao nhiêu cm?", "35", "70 / 2 = 35 cm."),
        make_sa(6, "Vận dụng cao", "Một người cao 1,8 mét. Chiều cao tối thiểu của tấm gương để người đó nhìn thấy toàn thân là bao nhiêu mét?", "0.9", "1,8 / 2 = 0,9 m.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng trước gương phẳng treo thẳng đứng. Người đó giơ tay phải lên chạm vào tai phải. Quan sát ảnh trong gương, ta thấy ảnh làm động tác gì đối diện?", ["Giơ tay trái chạm vào tai trái của ảnh", "Giơ tay phải chạm tai phải", "Hai tay giơ lên", "Không cử động"], 0, "Tính chất đối xứng trục qua gương phẳng đảo trái phải: tay phải thành tay trái đối diện."),
        make_vdc(2, "Một tia sáng chiếu tới mặt gương phẳng nằm ngang tạo góc tới i = 30 độ. Nếu quay gương một góc 10 độ quanh trục tới sao cho góc tới tăng lên thành 40 độ thì tia phản xạ sẽ quay đi một góc bằng bao nhiêu độ so với phương tia phản xạ ban đầu?", ["20 độ", "10 độ", "30 độ", "40 độ"], 0, "Góc quay của tia phản xạ = 2α = 2 × 10° = 20°."),
        make_vdc(3, "Một bể bơi có đáy phẳng nằm ngang chứa đầy nước trong suốt sâu 1,5 mét. Đáy bể lát gạch hoa phản xạ ánh sáng như một chiếc gương phẳng. Một bóng đèn nhỏ gắn trên thành hồ cách mặt nước 0,5 mét chiếu xuống đáy hồ. Khoảng cách từ bóng đèn đến ảnh ảo của nó tạo bởi đáy hồ là:", ["3,5 mét", "2,0 mét", "4,0 mét", "1,5 mét"], 0, "Khoảng cách từ đèn đến đáy hồ: 0,5 + 1,5 = 2,0 m => Khoảng cách giữa đèn và ảnh qua đáy hồ = 2 × 2,0 = 4,0 m."),
        make_vdc(4, "Một người tiến lại gần gương phẳng với tốc độ 0,8 m/s theo phương vuông góc với mặt gương. Trong thời gian 5 giây, khoảng cách giữa người đó và ảnh của mình trong gương đã giảm đi bao nhiêu mét?", ["8,0 mét", "4,0 mét", "2,0 mét", "16,0 mét"], 0, "Trong 5 s người đi được: 0,8 × 5 = 4,0 m => Khoảng cách người và ảnh giảm đi: 2 × 4,0 = 8,0 m.")
    ]
}

# --- ĐỀ 3 ---
c5_rev_exams["phys7_c5_rev_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật nào sau đây là nguồn sáng?", ["Ngọn đuốc đang cháy", "Mặt bàn gỗ", "Tấm gương soi", "Mảnh bìa trắng"], 0, "Ngọn đuốc đang cháy tự nó phát ra ánh sáng."),
        make_mc(2, "Nhận biết", "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi:", ["Theo đường thẳng", "Theo đường zích zắc", "Theo đường tròn", "Theo đường elip"], 0, "Định luật truyền thẳng ánh sáng."),
        make_mc(3, "Nhận biết", "Mô hình biểu diễn một tia sáng là:", ["Đường thẳng có mũi tên chỉ hướng truyền của ánh sáng", "Đường thẳng không có mũi tên", "Đường cong uốn lượn", "Hình chữ nhật"], 0, "Tia sáng là đường thẳng có mũi tên chỉ hướng."),
        make_mc(4, "Nhận biết", "Góc tới là góc tạo bởi:", ["Tia tới và pháp tuyến tại điểm tới", "Tia tới và mặt gương", "Tia phản xạ và mặt gương", "Tia tới và tia phản xạ"], 0, "Góc tới i = góc(SIN)."),
        make_mc(5, "Nhận biết", "Ảnh của một điểm sáng S qua gương phẳng được tạo bởi giao điểm của:", ["Các đường kéo dài của các tia phản xạ", "Các tia phản xạ thực tế", "Các tia tới", "Đường pháp tuyến"], 0, "Giao điểm của các đường kéo dài tia phản xạ là ảnh ảo S'."),
        make_mc(6, "Nhận biết", "Kính vạn hoa tạo ra những hoa văn hình học biến hóa rực rỡ nhờ:", ["Sự phản xạ ánh sáng nhiều lần qua hệ gương phẳng", "Bóng đèn led đổi màu", "Kính phóng đại", "Nước đổi màu"], 0, "Hệ gương phẳng phản xạ lặp đi lặp lại tạo hoa văn đối xứng."),
        make_mc(7, "Thông hiểu", "Chiếu tia tới tới mặt gương với góc tới i = 20 độ. Góc phản xạ r bằng:", ["20 độ", "40 độ", "70 độ", "80 độ"], 0, "r = i = 20 độ."),
        make_mc(8, "Thông hiểu", "Một vật đặt cách gương phẳng 45 cm. Ảnh của vật cách vật một khoảng bằng:", ["90 cm", "45 cm", "22,5 cm", "0 cm"], 0, "2d = 2 × 45 = 90 cm."),
        make_mc(9, "Thông hiểu", "Tia tới hợp với mặt gương một góc 50 độ. Góc tới i có giá trị là:", ["40 độ", "50 độ", "80 độ", "20 độ"], 0, "i = 90° - 50° = 40°."),
        make_mc(10, "Thông hiểu", "Khi một người đứng cách gương phẳng 1 m và lùi xa gương thêm 1 m thì khoảng cách giữa người và ảnh là:", ["4 mét", "2 mét", "3 mét", "1 mét"], 0, "Khoảng cách mới đến gương: 1 + 1 = 2 m => Khoảng cách người và ảnh: 2 × 2 = 4 m."),
        make_mc(11, "Thông hiểu", "Vùng tối (bóng tối hoàn toàn) ở phía sau vật cản sáng là vùng:", ["Hoàn toàn không nhận được ánh sáng từ nguồn sáng truyền tới", "Chỉ nhận được một phần ánh sáng từ nguồn sáng truyền tới", "Nhận được toàn bộ ánh sáng từ nguồn sáng", "Luôn phản chiếu ánh sáng mạnh mẽ"], 0, "Bóng tối nằm ở phía sau vật cản, hoàn toàn không nhận được ánh sáng từ nguồn sáng truyền tới."),
        make_mc(12, "Thông hiểu", "Chùm sáng phát ra từ đèn pin rọi vào tường là chùm sáng:", ["Phân kì", "Song song", "Hội tụ", "Tròn"], 0, "Chùm sáng loe rộng ra là chùm phân kì.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các hiện tượng quang học trong đời sống:", [
            ("a", "Bóng của cái cây in trên sân trường thay đổi chiều dài do vị trí Mặt Trời thay đổi.", True),
            ("b", "Ánh sáng từ ngọn đèn truyền thẳng trong không khí tĩnh lặng.", True),
            ("c", "Nguyệt thực toàn phần diễn ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất.", False),
            ("d", "Vùng bóng nửa tối nhận được một phần ánh sáng từ nguồn sáng rộng.", True)
        ], "Mặt Trăng ở giữa Mặt Trời và Trái Đất là Nhật thực, không phải Nguyệt thực."),
        make_tf(2, "Thông hiểu", "Về định luật phản xạ ánh sáng:", [
            ("a", "Góc phản xạ luôn bằng góc tới: r = i.", True),
            ("b", "Tia phản xạ nằm trong mặt phẳng tới.", True),
            ("c", "Góc hợp bởi tia tới và tia phản xạ bằng 2 lần góc tới: α = 2i.", True),
            ("d", "Nếu góc tới là 30 độ thì góc hợp bởi tia tới và mặt gương là 30 độ.", False)
        ], "Góc hợp bởi tia tới và mặt gương là 90° - 30° = 60°."),
        make_tf(3, "Vận dụng", "Khảo sát ảnh của một vật qua gương phẳng:", [
            ("a", "Vật cao 10 cm thì ảnh qua gương phẳng cũng cao đúng 10 cm.", True),
            ("b", "Khoảng cách từ vật đến gương luôn bằng khoảng cách từ ảnh đến gương.", True),
            ("c", "Ảnh tạo bởi gương phẳng có thể in dấu lên tấm phim chụp ảnh đặt sau gương.", False),
            ("d", "Người soi gương giơ tay trái thì ảnh giơ tay phải đối diện.", True)
        ], "Ảnh ảo không thể in hình lên phim đặt phía sau gương vì không có ánh sáng hội tụ thực tế."),
        make_tf(4, "Vận dụng", "Kính tiềm vọng trên tàu ngầm quân sự:", [
            ("a", "Sử dụng hai gương phẳng đặt nghiêng góc 45 độ.", True),
            ("b", "Tia sáng phản xạ 2 lần đổi hướng tổng cộng 180 độ (xuống rồi ngang).", True),
            ("c", "Cho ảnh cùng chiều giúp quan sát dễ dàng các mục tiêu trên mặt nước.", True),
            ("d", "Ảnh nhìn thấy qua kính tiềm vọng bị lộn ngược đầu.", False)
        ], "Ảnh qua kính tiềm vọng là ảnh cùng chiều thẳng đứng.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Bóng đèn pin đang sáng là nguồn sáng hay vật sáng?", "Nguồn sáng", "Nguồn sáng."),
        make_sa(2, "Thông hiểu", "Góc tới i = 50 độ. Góc phản xạ r bằng bao nhiêu độ?", "50", "r = 50 độ."),
        make_sa(3, "Vận dụng", "Vật cách gương phẳng 80 cm. Khoảng cách từ ảnh đến gương là bao nhiêu cm?", "80", "80 cm."),
        make_sa(4, "Vận dụng", "Tia tới hợp với mặt phẳng gương góc 60 độ. Góc tới bằng bao nhiêu độ?", "30", "i = 90 - 60 = 30 độ."),
        make_sa(5, "Vận dụng cao", "Khoảng cách giữa vật và ảnh là 120 cm. Vật cách gương bao nhiêu cm?", "60", "120 / 2 = 60 cm."),
        make_sa(6, "Vận dụng cao", "Người cao 1,5 mét cần chiếc gương phẳng treo tường cao tối thiểu bao nhiêu mét để nhìn thấy toàn thân?", "0.75", "1,5 / 2 = 0,75 m.")
    ],
    "part4": [
        make_vdc(1, "Một tia sáng chiếu tới mặt gương phẳng nằm ngang tạo góc tới i = 45 độ. Góc hợp bởi tia tới và tia phản xạ là bao nhiêu độ?", ["90 độ", "45 độ", "180 độ", "60 độ"], 0, "i + r = 45° + 45° = 90°."),
        make_vdc(2, "Một người đứng trước gương phẳng cách gương 2 mét. Nếu người đó tiến lại gần gương thêm 0,5 mét thì khoảng cách giữa người đó và ảnh của mình trong gương lúc này là bao nhiêu mét?", ["3,0 mét", "1,5 mét", "4,0 mét", "2,5 mét"], 0, "d mới = 2 - 0,5 = 1,5 m => 2d = 3,0 m."),
        make_vdc(3, "Để lấy ánh sáng Mặt Trời từ trên cao chiếu rọi thẳng đứng xuống đáy giếng sâu, biết tia sáng Mặt Trời chiếu nghiêng hợp với phương nằm ngang góc 40 độ. Cần đặt gương phẳng nghiêng góc bao nhiêu độ so với phương thẳng đứng?", ["25 độ", "40 độ", "50 độ", "65 độ"], 0, "Góc giữa tia tới và tia phản xạ = 40° + 90° = 130°. Góc tới i = 65°. Mặt gương nghiêng 90° - 65° = 25° so với phương thẳng đứng."),
        make_vdc(4, "Một người cao 1,6 m đứng trước gương phẳng treo thẳng đứng nhìn thấy toàn thân. Nếu người này bước lùi xa gương thêm 1 m thì kích thước thật của ảnh người đó trong gương:", ["Vẫn bằng 1,6 m không hề thay đổi", "Bị nhỏ đi một nửa", "Tăng lên gấp đôi", "Tăng thêm 1 m"], 0, "Kích thước thật của ảnh luôn bằng kích thước vật (1,6 m).")
    ]
}

# --- ĐỀ 4 ---
c5_rev_exams["phys7_c5_rev_test4"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 04",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 4, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Nguồn sáng tự nhiên lớn nhất cung cấp ánh sáng và sự sống cho Trái Đất là:", ["Mặt Trời", "Mặt Trăng", "Ngọn đuốc", "Bóng đèn"], 0, "Mặt Trời là nguồn sáng tự nhiên vô tận."),
        make_mc(2, "Nhận biết", "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo:", ["Đường thẳng", "Đường cong", "Đường gãy khúc", "Đường sóng"], 0, "Định luật truyền thẳng ánh sáng."),
        make_mc(3, "Nhận biết", "Chùm sáng song song gồm các tia sáng:", ["Song song với nhau", "Giao nhau tại một điểm", "Loe rộng dần ra", "Cắt nhau vuông góc"], 0, "Các tia sáng song song với nhau."),
        make_mc(4, "Nhận biết", "Định luật phản xạ ánh sáng khẳng định:", ["Góc phản xạ bằng góc tới", "Góc phản xạ lớn hơn góc tới", "Góc phản xạ nhỏ hơn góc tới", "Góc phản xạ luôn bằng 90 độ"], 0, "r = i."),
        make_mc(5, "Nhận biết", "Ảnh của một vật tạo bởi gương phẳng:", ["Là ảnh ảo, độ lớn bằng vật", "Là ảnh thật, lớn hơn vật", "Là ảnh ảo, nhỏ hơn vật", "Là ảnh thật, nhỏ hơn vật"], 0, "Ảnh ảo, độ lớn bằng vật."),
        make_mc(6, "Nhận biết", "Vùng bóng tối là vùng phía sau vật cản:", ["Hoàn toàn không nhận được ánh sáng từ nguồn sáng", "Nhận được một nửa ánh sáng", "Nhận được toàn bộ ánh sáng", "Sáng rực rỡ"], 0, "Không nhận được ánh sáng từ nguồn sáng."),
        make_mc(7, "Thông hiểu", "Chiếu tia tới tới gương phẳng với góc tới i = 55 độ. Góc phản xạ r bằng:", ["55 độ", "35 độ", "110 độ", "90 độ"], 0, "r = i = 55 độ."),
        make_mc(8, "Thông hiểu", "Vật đặt cách gương phẳng 70 cm. Ảnh của vật cách gương phẳng một khoảng là:", ["70 cm", "140 cm", "35 cm", "0 cm"], 0, "d' = d = 70 cm."),
        make_mc(9, "Thông hiểu", "Tia tới hợp với mặt gương một góc 25 độ. Góc phản xạ r bằng:", ["65 độ", "25 độ", "50 độ", "130 độ"], 0, "i = 90° - 25° = 65° => r = 65°."),
        make_mc(10, "Thông hiểu", "Khi một người tiến lại gần gương phẳng 0,4 m thì khoảng cách giữa người và ảnh giảm đi:", ["0,8 m", "0,4 m", "0,2 m", "1,2 m"], 0, "Giảm: 2 × 0,4 = 0,8 m."),
        make_mc(11, "Thông hiểu", "Hiện tượng nguyệt thực toàn phần diễn ra khi:", ["Mặt Trăng đi vào vùng bóng tối của Trái Đất", "Mặt Trời đi vào bóng tối", "Trái Đất nằm giữa bóng Mặt Trăng", "Vào ban ngày"], 0, "Mặt Trăng bị bóng tối Trái Đất che khuất."),
        make_mc(12, "Thông hiểu", "Kính vạn hoa tạo hoa văn đẹp mắt nhờ hiện tượng quang học nào?", ["Hiện tượng phản xạ ánh sáng", "Hiện tượng khúc xạ ánh sáng", "Hiện tượng tán sắc ánh sáng", "Hiện tượng nhật thực"], 0, "Phản xạ ánh sáng liên tiếp qua hệ gương phẳng.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc tính của tia sáng và nguồn sáng:", [
            ("a", "Đom đóm tự phát sáng trong đêm là nguồn sáng sinh học.", True),
            ("b", "Ánh trăng là ánh sáng do Mặt Trăng tự phát ra.", False),
            ("c", "Tia sáng được biểu diễn bằng đường thẳng có mũi tên định hướng.", True),
            ("d", "Trong chân không, ánh sáng truyền với tốc độ khoảng 300.000 km/s.", True)
        ], "Mặt Trăng hắt lại ánh sáng Mặt Trời, không tự phát sáng."),
        make_tf(2, "Thông hiểu", "Xét các đặc điểm của hiện tượng phản xạ ánh sáng trên gương phẳng:", [
            ("a", "Tia phản xạ nằm trong mặt phẳng tới.", True),
            ("b", "Đường pháp tuyến vuông góc với mặt phẳng gương.", True),
            ("c", "Góc tới tăng thì góc phản xạ cũng tăng theo.", True),
            ("d", "Tia phản xạ luôn luôn vuông góc với tia tới trong mọi trường hợp.", False)
        ], "Chỉ vuông góc khi góc tới i = 45° (i + r = 90°)."),
        make_tf(3, "Vận dụng", "Khảo sát tính chất đối xứng của ảnh qua gương phẳng:", [
            ("a", "Vật và ảnh đối xứng nhau qua mặt phẳng gương.", True),
            ("b", "Khoảng cách từ vật đến gương bằng khoảng cách từ ảnh đến gương.", True),
            ("c", "Ảnh của bàn tay trái là bàn tay phải đối diện trong gương.", True),
            ("d", "Nếu đứng càng xa gương thì kích thước thật của ảnh sẽ teo nhỏ lại.", False)
        ], "Kích thước thật của ảnh luôn bằng vật."),
        make_tf(4, "Vận dụng", "Hiện tượng Nhật thực và Nguyệt thực trong tự nhiên:", [
            ("a", "Nhật thực xảy ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất.", True),
            ("b", "Nguyệt thực xảy ra khi Trái Đất nằm giữa Mặt Trời và Mặt Trăng.", True),
            ("c", "Nhật thực toàn phần có thể quan sát được từ mọi nơi trên Trái Đất cùng lúc.", False),
            ("d", "Bóng tối của Mặt Trăng trên Trái Đất tạo ra vùng nhật thực.", True)
        ], "Vùng bóng tối của Mặt Trăng chỉ quét qua một dải hẹp trên Trái Đất.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Mặt gương phẳng là bề mặt phản xạ ánh sáng tốt hay kém?", "Tốt", "Phản xạ rất tốt."),
        make_sa(2, "Thông hiểu", "Góc tới bằng 65 độ. Góc phản xạ bằng bao nhiêu độ?", "65", "r = 65 độ."),
        make_sa(3, "Vận dụng", "Vật cách gương phẳng 1 m. Khoảng cách giữa vật và ảnh là bao nhiêu mét?", "2", "2d = 2 m."),
        make_sa(4, "Vận dụng", "Tia tới hợp với mặt gương góc 45 độ. Góc tới bằng bao nhiêu độ?", "45", "i = 90 - 45 = 45 độ."),
        make_sa(5, "Vận dụng cao", "Khoảng cách giữa vật và ảnh là 160 cm. Vật cách gương bao nhiêu cm?", "80", "160 / 2 = 80 cm."),
        make_sa(6, "Vận dụng cao", "Người cao 1,74 m cần gương phẳng cao tối thiểu bao nhiêu mét để nhìn thấy toàn thân?", "0.87", "1,74 / 2 = 0,87 m.")
    ],
    "part4": [
        make_vdc(1, "Chiếu một tia sáng SI tới mặt gương phẳng. Góc hợp bởi tia tới SI và tia phản xạ IR bằng 120 độ. Góc phản xạ r bằng:", ["60 độ", "120 độ", "30 độ", "45 độ"], 0, "r = 120° / 2 = 60°."),
        make_vdc(2, "Một người đứng cách gương phẳng 1,6 m. Nếu người đó lùi xa gương thêm 0,4 m thì khoảng cách giữa người đó và ảnh của mình lúc này là bao nhiêu mét?", ["4,0 mét", "2,0 mét", "3,2 mét", "3,6 mét"], 0, "d mới = 1,6 + 0,4 = 2,0 m => 2d = 4,0 m."),
        make_vdc(3, "Hai gương phẳng G1 và G2 đặt song song với nhau, mặt phản xạ quay vào nhau và cách nhau một khoảng 20 cm. Một điểm sáng S đặt chính giữa hai gương (cách mỗi gương 10 cm). Khoảng cách giữa hai ảnh ảo đầu tiên của điểm sáng S tạo bởi hai gương là:", ["40 cm", "20 cm", "30 cm", "50 cm"], 0, "Ảnh S1 cách G1 là 10 cm (sau G1), ảnh S2 cách G2 là 10 cm (sau G2). Khoảng cách S1S2 = 10 + 20 + 10 = 40 cm."),
        make_vdc(4, "Tại sao khi chụp ảnh thẻ bằng gương phẳng, bức ảnh luôn bị lật ngược trái phải so với người thật ngoài đời?", ["Do tính chất đối xứng trục qua mặt phẳng gương làm đảo ngược hướng trái - phải", "Do máy ảnh bị hỏng", "Do ánh sáng bị hấp thụ", "Do mắt người chụp nhìn sai"], 0, "Ảnh qua gương phẳng đối xứng trục đảo hướng trái phải.")
    ]
}

# --- ĐỀ 5 ---
c5_rev_exams["phys7_c5_rev_test5"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 05",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 5, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật nào sau đây tự nó phát ra ánh sáng?", ["Ngọn nến đang cháy", "Mặt Trăng", "Mặt gương", "Mảnh bìa các-tông"], 0, "Ngọn nến đang cháy tự phát sáng."),
        make_mc(2, "Nhận biết", "Ánh sáng truyền theo đường thẳng trong môi trường nào?", ["Môi trường trong suốt và đồng tính", "Môi trường chân không có nhiều vật cản", "Môi trường nước đục", "Mọi môi trường"], 0, "Trong môi trường trong suốt và đồng tính."),
        make_mc(3, "Nhận biết", "Chùm sáng hội tụ là chùm sáng gồm các tia sáng:", ["Giao nhau tại một điểm", "Song song với nhau", "Loe rộng dần ra", "Không bao giờ cắt nhau"], 0, "Giao nhau tại một điểm."),
        make_mc(4, "Nhận biết", "Góc phản xạ là góc tạo bởi:", ["Tia phản xạ và đường pháp tuyến tại điểm tới", "Tia phản xạ và mặt phẳng gương", "Tia tới và mặt phẳng gương", "Tia tới và tia phản xạ"], 0, "Góc phản xạ r = góc(NIR)."),
        make_mc(5, "Nhận biết", "Tính chất nào sau đây là của ảnh ảo tạo bởi gương phẳng?", ["Là ảnh ảo, đối xứng với vật qua gương", "Là ảnh thật hứng được trên màn", "Là ảnh ảo lớn gấp đôi vật", "Là ảnh thật nhỏ hơn vật"], 0, "Ảnh ảo đối xứng với vật qua mặt gương."),
        make_mc(6, "Nhận biết", "Vùng bóng nửa tối là vùng:", ["Chỉ nhận được một phần ánh sáng từ nguồn sáng", "Hoàn toàn tối đen", "Nhận đủ ánh sáng", "Sáng chói"], 0, "Chỉ nhận được một phần ánh sáng."),
        make_mc(7, "Thông hiểu", "Chiếu tia tới tới mặt gương với góc tới i = 75 độ. Góc phản xạ r bằng:", ["75 độ", "15 độ", "150 độ", "90 độ"], 0, "r = i = 75 độ."),
        make_mc(8, "Thông hiểu", "Vật đặt cách gương phẳng 1,1 mét. Ảnh của vật cách vật một khoảng là:", ["2,2 mét", "1,1 mét", "0,55 mét", "3,3 mét"], 0, "2d = 2 × 1,1 = 2,2 m."),
        make_mc(9, "Thông hiểu", "Tia tới hợp với mặt gương một góc 35 độ. Góc tới i có giá trị là:", ["55 độ", "35 độ", "70 độ", "110 độ"], 0, "i = 90° - 35° = 55°."),
        make_mc(10, "Thông hiểu", "Một người đứng cách gương phẳng 2 mét, nếu tiến lại gần gương thêm 0,8 mét thì khoảng cách giữa người và ảnh là:", ["2,4 mét", "1,2 mét", "3,2 mét", "1,6 mét"], 0, "d mới = 2 - 0,8 = 1,2 m => 2d = 2,4 m."),
        make_mc(11, "Thông hiểu", "Hiện tượng nhật thực xảy ra vào thời điểm nào trong tháng âm lịch?", ["Đầu tháng âm lịch (ngày trăng non)", "Ngày rằm âm lịch (ngày 15)", "Cuối tháng", "Bất kì ngày nào"], 0, "Nhật thực xảy ra vào ngày trăng non đầu tháng âm lịch khi Mặt Trăng ở giữa."),
        make_mc(12, "Thông hiểu", "Kính tiềm vọng dùng hai gương phẳng nghiêng góc bao nhiêu độ so với trục ống ngắm?", ["45 độ", "90 độ", "30 độ", "60 độ"], 0, "Nghiêng góc 45 độ.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất của sự truyền thẳng ánh sáng:", [
            ("a", "Trong không khí đồng tính, ánh sáng truyền đi theo đường thẳng.", True),
            ("b", "Người thợ xây ngắm dây rọi thẳng đứng là ứng dụng sự truyền thẳng ánh sáng.", True),
            ("c", "Tia sáng truyền qua mặt nước không bị đổi hướng.", False),
            ("d", "Bóng tối của vật cản in trên tường là do ánh sáng truyền thẳng.", True)
        ], "Khi truyền qua mặt nước (khúc xạ), tia sáng bị gãy khúc đổi hướng."),
        make_tf(2, "Thông hiểu", "Về các quy tắc phản xạ ánh sáng trên gương phẳng:", [
            ("a", "Góc phản xạ luôn luôn bằng góc tới.", True),
            ("b", "Tia phản xạ nằm trong mặt phẳng tới.", True),
            ("c", "Tia sáng tới vuông góc với mặt gương thì bật ngược trở lại theo phương cũ.", True),
            ("d", "Góc tới tăng thì góc phản xạ lại giảm đi.", False)
        ], "Góc tới tăng thì góc phản xạ cũng tăng theo vì r = i."),
        make_tf(3, "Vận dụng", "Khảo sát chuyển động của vật và ảnh qua gương phẳng:", [
            ("a", "Người chạy lại gần gương 1 m thì ảnh cũng chạy lại gần gương 1 m.", True),
            ("b", "Tốc độ tương đối giữa người và ảnh gấp đôi tốc độ của người đối với gương.", True),
            ("c", "Kích thước của ảnh trong gương phẳng luôn bằng kích thước của người.", True),
            ("d", "Nếu soi gương trong phòng hoàn toàn tối đen không có ánh sáng thì ta vẫn nhìn thấy ảnh rõ nét.", False)
        ], "Phải có ánh sáng chiếu vào người và hắt vào gương rồi tới mắt mới nhìn thấy ảnh."),
        make_tf(4, "Vận dụng", "Hiện tượng bóng tối trong tự nhiên:", [
            ("a", "Vùng bóng tối hoàn toàn không nhận được ánh sáng từ nguồn sáng.", True),
            ("b", "Vùng bóng nửa tối chỉ nhận được một phần ánh sáng từ nguồn sáng rộng.", True),
            ("c", "Nguyệt thực xảy ra khi Trái Đất che khuất ánh sáng Mặt Trời tới Mặt Trăng.", True),
            ("d", "Nhật thực toàn phần có thể nhìn thấy vào lúc nửa đêm.", False)
        ], "Nhật thực chỉ quan sát được vào ban ngày.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đèn pha ô tô đang sáng là nguồn sáng hay vật sáng?", "Nguồn sáng", "Nguồn sáng."),
        make_sa(2, "Thông hiểu", "Góc tới bằng 80 độ. Góc phản xạ bằng bao nhiêu độ?", "80", "r = 80 độ."),
        make_sa(3, "Vận dụng", "Vật cách gương phẳng 1,2 mét. Khoảng cách giữa vật và ảnh là bao nhiêu mét?", "2.4", "2d = 2,4 m."),
        make_sa(4, "Vận dụng", "Tia tới hợp với mặt gương góc 10 độ. Góc tới bằng bao nhiêu độ?", "80", "i = 90 - 10 = 80 độ."),
        make_sa(5, "Vận dụng cao", "Khoảng cách giữa vật và ảnh là 140 cm. Vật cách gương bao nhiêu cm?", "70", "140 / 2 = 70 cm."),
        make_sa(6, "Vận dụng cao", "Người cao 1,68 mét cần chiếc gương phẳng treo tường cao tối thiểu bao nhiêu mét để nhìn thấy toàn thân?", "0.84", "1,68 / 2 = 0,84 m.")
    ],
    "part4": [
        make_vdc(1, "Chiếu một tia sáng SI tới mặt gương phẳng nằm ngang. Góc hợp bởi tia tới SI và tia phản xạ IR là 80 độ. Góc tới i có độ lớn là:", ["40 độ", "80 độ", "20 độ", "50 độ"], 0, "i = 80° / 2 = 40°."),
        make_vdc(2, "Một người đứng cách gương phẳng 2,5 mét. Nếu người đó tiến lại gần gương thêm 1,0 mét thì khoảng cách giữa người đó và ảnh của mình trong gương lúc này là bao nhiêu mét?", ["3,0 mét", "1,5 mét", "4,0 mét", "5,0 mét"], 0, "d mới = 2,5 - 1,0 = 1,5 m => 2d = 3,0 m."),
        make_vdc(3, "Một cây cột cờ cao 5 mét cắm thẳng đứng trên sân trường. Vào buổi trưa nắng, bóng của cột cờ in trên sân dài 2,5 mét. Một bạn học sinh đứng gần đó có bóng dài 0,75 mét. Chiều cao của bạn học sinh là:", ["1,5 mét", "1,4 mét", "1,6 mét", "1,2 mét"], 0, "Tỉ lệ: 5 / 2,5 = 2 => Chiều cao bạn = 0,75 × 2 = 1,5 mét."),
        make_vdc(4, "Một người đứng trước gương phẳng treo thẳng đứng và nhìn thấy toàn thân. Nếu người này bước lùi xa gương thêm 2 mét thì chiều cao tối thiểu của tấm gương để người đó vẫn nhìn thấy toàn thân sẽ:", ["Không đổi (vẫn bằng một nửa chiều cao của người đó)", "Tăng lên gấp đôi", "Giảm đi một nửa", "Tăng thêm 2 mét"], 0, "Chiều cao tối thiểu của gương luôn bằng H/2 không phụ thuộc khoảng cách người đến gương.")
    ]
}
