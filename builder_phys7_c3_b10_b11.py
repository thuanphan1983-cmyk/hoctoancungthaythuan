# -*- coding: utf-8 -*-
"""
CHƯƠNG III: TỐC ĐỘ - BÀI 10 & BÀI 11 (6 ĐỀ ĐỘC LẬP 100%)
- phys7_c3_b10: Bài 10: Đồ thị quãng đường - thời gian (3 đề: test1, test2, test3)
- phys7_c3_b11: Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông (3 đề: test1, test2, test3)
Không trùng lặp, không tiền tố "Đề X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

b10_b11_exams = {}

# =========================================================================
# BÀI 10: ĐỒ THỊ QUÃNG ĐƯỜNG - THỜI GIAN (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b10_b11_exams["phys7_c3_b10_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 10: Đồ thị quãng đường - thời gian - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b10", "lessonName": "Bài 10: Đồ thị quãng đường - thời gian",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Trong đồ thị quãng đường - thời gian (s - t), trục thẳng đứng Os và trục nằm ngang Ot lần lượt biểu diễn:", ["Quãng đường chuyển động và thời gian chuyển động", "Thời gian chuyển động và quãng đường chuyển động", "Tốc độ và thời gian", "Lực và quãng đường"], 0, "Trục Os thẳng đứng biểu diễn quãng đường, trục Ot nằm ngang biểu diễn thời gian."),
        make_mc(2, "Nhận biết", "Đồ thị quãng đường - thời gian của một vật chuyển động thẳng đều có dạng là:", ["Đường thẳng nghiêng dốc lên xuất phát từ gốc tọa độ", "Đường parabol uốn cong", "Đường tròn khép kín", "Đường thẳng zích zắc"], 0, "Chuyển động đều có s tỉ lệ thuận với t nên đồ thị s-t là đường thẳng nghiêng."),
        make_mc(3, "Nhận biết", "Khi vật đứng yên không chuyển động, đồ thị quãng đường - thời gian là:", ["Đoạn thẳng song song với trục thời gian Ot", "Đường thẳng dốc đứng lên", "Đường thẳng dốc xuống", "Đường tròn"], 0, "Đứng yên thì quãng đường không đổi theo thời gian, đồ thị nằm ngang song song trục Ot."),
        make_mc(4, "Nhận biết", "Độ dốc (độ nghiêng) của đường đồ thị s - t cho biết đại lượng nào của chuyển động?", ["Tốc độ chuyển động (độ dốc càng lớn thì tốc độ càng nhanh)", "Khối lượng của vật", "Nhiệt độ của vật", "Gia tốc rơi"], 0, "Độ dốc của đồ thị s-t tỉ lệ thuận với tốc độ chuyển động."),
        make_mc(5, "Nhận biết", "Từ đồ thị quãng đường - thời gian, ta KHÔNG THỂ xác định trực tiếp đại lượng nào sau đây?", ["Khối lượng của vật đang chuyển động", "Quãng đường vật đi được sau khoảng thời gian t", "Thời gian cần thiết để vật đi được quãng đường s", "Tốc độ của vật"], 0, "Đồ thị s-t chỉ cho biết thông tin về quãng đường, thời gian và tốc độ, không cho biết khối lượng."),
        make_mc(6, "Nhận biết", "Gốc tọa độ O (0; 0) trên đồ thị s - t thường ứng với:", ["Thời điểm bắt đầu khảo sát chuyển động và vị trí mốc xuất phát", "Thời điểm vật dừng lại", "Thời điểm vật đạt tốc độ tối đa", "Vị trí đích đến"], 0, "Gốc O biểu diễn t = 0 và s = 0."),
        make_mc(7, "Thông hiểu", "Đồ thị s - t biểu diễn một người đi bộ: sau 2 giờ đi được 8 km. Tốc độ của người đó là:", ["4 km/h", "8 km/h", "2 km/h", "16 km/h"], 0, "v = s / t = 8 / 2 = 4 km/h."),
        make_mc(8, "Thông hiểu", "Trên đồ thị s - t, trong khoảng thời gian từ t = 1 h đến t = 2 h, đồ thị là đoạn nằm ngang ở mức s = 40 km. Điều đó có nghĩa là:", ["Trong khoảng thời gian này vật dừng lại không chuyển động", "Vật chạy với tốc độ 40 km/h", "Vật quay đầu trở lại", "Vật tăng tốc rất nhanh"], 0, "Đoạn nằm ngang biểu thị s không đổi, vật đang đứng yên (dừng nghỉ)."),
        make_mc(9, "Thông hiểu", "Hai xe A và B có đồ thị s - t là hai đường thẳng dốc lên. Đường đồ thị của xe A dốc hơn đường của xe B. Kết luận nào đúng?", ["Xe A chuyển động nhanh hơn xe B", "Xe B chuyển động nhanh hơn xe A", "Hai xe chuyển động nhanh như nhau", "Không thể so sánh"], 0, "Đường đồ thị càng dốc chứng tỏ trong cùng một khoảng thời gian vật đi được quãng đường lớn hơn => tốc độ lớn hơn."),
        make_mc(10, "Thông hiểu", "Một ô tô chuyển động đều có đồ thị s - t đi qua điểm M (3 h; 150 km). Quãng đường ô tô đi được sau 5 giờ là:", ["250 km", "200 km", "300 km", "150 km"], 0, "v = 150 / 3 = 50 km/h => s = 50 × 5 = 250 km."),
        make_mc(11, "Thông hiểu", "Một người chạy bộ có đồ thị s - t gồm hai giai đoạn: Giai đoạn 1 đi 300 m trong 50 s; Giai đoạn 2 đi 200 m trong 50 s. So sánh tốc độ v1 và v2:", ["v1 > v2", "v1 < v2", "v1 = v2", "v1 = 0"], 0, "v1 = 300 / 50 = 6 m/s; v2 = 200 / 50 = 4 m/s => v1 > v2."),
        make_mc(12, "Thông hiểu", "Quan sát đồ thị s - t, nếu hai đường đồ thị của hai vật cắt nhau tại điểm K(t0; s0) thì điều đó có ý nghĩa là:", ["Tại thời điểm t0, hai vật gặp nhau ở cùng vị trí cách mốc s0", "Hai vật va chạm nổ tung", "Hai vật dừng lại vĩnh viễn", "Hai vật đổi hướng chuyển động vuông góc"], 0, "Điểm cắt nhau biểu diễn thời điểm và vị trí hai vật gặp nhau.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các tính chất cơ bản của đồ thị quãng đường - thời gian (s - t):", [
            ("a", "Trục Ot thường được chọn làm trục hoành nằm ngang.", True),
            ("b", "Trục Os được chọn làm trục tung thẳng đứng hướng lên.", True),
            ("c", "Đường đồ thị càng dốc đứng thì tốc độ chuyển động của vật càng lớn.", True),
            ("d", "Đoạn đồ thị dốc xuống về trục hoành biểu thị vật bị tiêu biến mất.", False)
        ], "Đoạn dốc xuống biểu thị khoảng cách của vật so với mốc giảm dần (vật chuyển động quay về mốc)."),
        make_tf(2, "Thông hiểu", "Phân tích đồ thị chuyển động của một xe máy trên tuyến đường dài 90 km:", [
            ("a", "Đoạn 1 từ t = 0 đến t = 1 h xe đi từ s = 0 đến s = 40 km với tốc độ 40 km/h.", True),
            ("b", "Đoạn 2 từ t = 1 h đến t = 1,5 h đường đồ thị nằm ngang, xe dừng nghỉ 30 phút.", True),
            ("c", "Đoạn 3 từ t = 1,5 h đến t = 2,5 h xe đi tiếp từ s = 40 km đến s = 90 km với tốc độ 50 km/h.", True),
            ("d", "Tốc độ trung bình trên toàn bộ chuyến đi tính cả thời gian nghỉ là 45 km/h.", False)
        ], "Tổng quãng đường = 90 km, tổng thời gian = 2,5 h => v_tb = 90 / 2,5 = 36 km/h."),
        make_tf(3, "Vận dụng", "Hai bạn học sinh Nam và Hùng cùng đạp xe từ trường về nhà trên một con đường thẳng:", [
            ("a", "Đồ thị s - t của Nam đi qua gốc O(0; 0) và điểm A(20 min; 4 km).", True),
            ("b", "Tốc độ đạp xe của Nam là 12 km/h.", True),
            ("c", "Đồ thị của Hùng đi qua điểm B(30 min; 4,5 km), tốc độ của Hùng là 9 km/h.", True),
            ("d", "Trên đường đi, Hùng chuyển động nhanh hơn Nam.", False)
        ], "Nam chạy 12 km/h nhanh hơn Hùng chạy 9 km/h."),
        make_tf(4, "Vận dụng", "Một xe chở hàng chuyển động được mô tả bởi đồ thị s - t chia làm 2 giai đoạn:", [
            ("a", "Giai đoạn 1: trong 2 giờ đầu đi được 80 km.", True),
            ("b", "Giai đoạn 2: trong 1 giờ tiếp theo đi được thêm 60 km.", True),
            ("c", "Tốc độ ở giai đoạn 2 lớn hơn tốc độ ở giai đoạn 1.", True),
            ("d", "Độ dốc của đồ thị ở giai đoạn 1 lớn hơn độ dốc ở giai đoạn 2.", False)
        ], "v1 = 40 km/h, v2 = 60 km/h => giai đoạn 2 có tốc độ lớn hơn nên đồ thị dốc hơn giai đoạn 1.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Từ đồ thị s - t, vật đi được 120 m trong 15 giây. Tốc độ của vật là bao nhiêu m/s?", "8", "v = 120 / 15 = 8 m/s."),
        make_sa(2, "Thông hiểu", "Một đồ thị s - t chỉ ra xe chạy với tốc độ 60 km/h. Sau 3 giờ xe đi được bao nhiêu km?", "180", "s = 60 × 3 = 180 km."),
        make_sa(3, "Vận dụng", "Đồ thị s - t của một người đi bộ gồm: đoạn dốc lên từ 0 đến 3 km trong 0,5 h, sau đó nằm ngang 0,2 h. Thời gian dừng nghỉ là bao nhiêu phút?", "12", "0,2 h = 0,2 × 60 = 12 phút."),
        make_sa(4, "Vận dụng", "Từ đồ thị s - t, lúc t = 1 h xe ở vị trí 30 km, lúc t = 3 h xe ở vị trí 110 km. Tốc độ của xe trong khoảng thời gian này là bao nhiêu km/h?", "40", "v = (110 - 30) / (3 - 1) = 80 / 2 = 40 km/h."),
        make_sa(5, "Vận dụng cao", "Đồ thị của xe A là s = 50t, đồ thị của xe B xuất phát cùng lúc từ vị trí s = 20 km với s = 30t + 20. Hai xe gặp nhau sau bao nhiêu giờ?", "1", "50t = 30t + 20 => 20t = 20 => t = 1 h."),
        make_sa(6, "Vận dụng cao", "Một người chạy bộ có đồ thị s - t là đường thẳng đi qua điểm (10 s; 40 m). Để đi hết quãng đường 200 m, người đó cần bao nhiêu giây?", "50", "v = 40 / 10 = 4 m/s => t = 200 / 4 = 50 s.")
    ],
    "part4": [
        make_vdc(1, "Một xe ô tô khởi hành từ A lúc 7h00 sáng để đi đến B. Đồ thị s - t của xe gồm: đoạn 1 chạy đều với tốc độ 60 km/h trong 1,5 giờ; đoạn 2 xe dừng nghỉ 30 phút tại trạm dừng chân; đoạn 3 chạy tiếp quãng đường 50 km với tốc độ 50 km/h đến đích. Xe đến B vào thời điểm nào trong ngày?", ["10h00 sáng", "9h30 sáng", "10h30 sáng", "11h00 trưa"], 0, "Thời gian đoạn 1: 1,5 h. Thời gian đoạn 2: 0,5 h. Thời gian đoạn 3: 50 / 50 = 1,0 h. Tổng thời gian: 3,0 h. Đến nơi lúc: 7h00 + 3h = 10h00 sáng."),
        make_vdc(2, "Đồ thị s - t của hai vật 1 và 2 cùng xuất phát từ một điểm chuyển động cùng chiều. Vật 1 có phương trình đồ thị s1 = 40t (km), vật 2 xuất phát sau vật 1 một khoảng thời gian 0,5 giờ và chạy với tốc độ 60 km/h (s2 = 60(t - 0,5)). Thời điểm hai vật gặp nhau cách thời điểm xuất phát của vật 1 là:", ["1,5 giờ", "1,0 giờ", "2,0 giờ", "2,5 giờ"], 0, "40t = 60(t - 0,5) => 40t = 60t - 30 => 20t = 30 => t = 1,5 h."),
        make_vdc(3, "Một vận động viên leo núi có đồ thị s - t như sau: leo lên dốc 3 km với tốc độ 2 km/h; nghỉ trên đỉnh núi 45 phút; leo xuống dốc 3 km theo đường cũ với tốc độ 4 km/h. Tốc độ trung bình của vận động viên trong cả chuyến leo núi kể cả thời gian nghỉ là:", ["2,0 km/h", "2,5 km/h", "3,0 km/h", "1,8 km/h"], 0, "t_lên = 3 / 2 = 1,5 h; t_nghỉ = 45 phút = 0,75 h; t_xuống = 3 / 4 = 0,75 h. Tổng t = 1,5 + 0,75 + 0,75 = 3 h. Tổng s = 6 km => v_tb = 6 / 3 = 2 km/h."),
        make_vdc(4, "Một đoàn tàu chở hàng rời ga với đồ thị s - t biểu diễn: trong 10 phút đầu đi được 5 km; trong 20 phút tiếp theo đi được 20 km; trong 10 phút cuối giảm tốc đi được 5 km thì dừng lại ở ga kế tiếp. Tốc độ trung bình trên toàn tuyến đường nối hai ga là:", ["45 km/h", "60 km/h", "30 km/h", "40 km/h"], 0, "Tổng s = 5 + 20 + 5 = 30 km. Tổng t = 10 + 20 + 10 = 40 phút = 2/3 h => v_tb = 30 / (2/3) = 45 km/h.")
    ]
}

# --- ĐỀ 2 ---
b10_b11_exams["phys7_c3_b10_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 10: Đồ thị quãng đường - thời gian - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b10", "lessonName": "Bài 10: Đồ thị quãng đường - thời gian",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Để vẽ đồ thị quãng đường - thời gian của một chuyển động, bước đầu tiên cần làm là:", ["Lập bảng ghi các giá trị tương ứng của quãng đường s và thời gian t", "Vẽ ngay một đường thẳng bất kì", "Tính gia tốc của chuyển động", "Đo nhiệt độ môi trường"], 0, "Cần lập bảng số liệu thu thập quãng đường s tương ứng với các mốc thời gian t."),
        make_mc(2, "Nhận biết", "Điểm biểu diễn chuyển động trên mặt phẳng tọa độ (s - t) có tọa độ dạng:", ["(t; s)", "(s; t)", "(v; t)", "(s; v)"], 0, "Tọa độ điểm trên đồ thị s-t có hoành độ là t và tung độ là s: (t; s)."),
        make_mc(3, "Nhận biết", "Nếu đồ thị quãng đường - thời gian của một vật là một đường gấp khúc gồm các đoạn thẳng nối tiếp nhau thì chuyển động của vật là:", ["Chuyển động gồm nhiều giai đoạn chuyển động đều với các tốc độ khác nhau", "Chuyển động tròn đều", "Chuyển động biến đổi đều liên tục", "Vật đứng yên hoàn toàn"], 0, "Đường gấp khúc gồm các đoạn thẳng biểu diễn các chặng chuyển động thẳng đều khác nhau."),
        make_mc(4, "Nhận biết", "Trong đồ thị s - t, đoạn đồ thị nào sau đây thể hiện vật chuyển động nhanh nhất?", ["Đoạn có độ nghiêng so với trục Ot lớn nhất", "Đoạn nằm ngang", "Đoạn có độ nghiêng nhỏ nhất", "Đoạn ngắn nhất"], 0, "Độ nghiêng (độ dốc) càng lớn thì tốc độ v = Δs / Δt càng lớn."),
        make_mc(5, "Nhận biết", "Khi vật chuyển động thẳng đều, tỉ số giữa độ biến thiên quãng đường Δs và độ biến thiên thời gian Δt luôn:", ["Không đổi theo thời gian và bằng tốc độ của vật", "Tăng dần theo thời gian", "Giảm dần về 0", "Bằng 0"], 0, "Trong chuyển động đều, v = Δs / Δt là hằng số không đổi."),
        make_mc(6, "Nhận biết", "Trên đồ thị s - t, một đoạn thẳng nằm trùng khít với trục thời gian Ot biểu diễn trạng thái:", ["Vật đứng yên tại gốc mốc tọa độ (s = 0)", "Vật đang chạy với tốc độ cực đại", "Vật đang bay lên trời", "Vật chuyển động lùi"], 0, "Trùng trục Ot nghĩa là s = 0 ở mọi thời điểm t, vật đứng yên tại vị trí mốc."),
        make_mc(7, "Thông hiểu", "Đồ thị s - t của một xe đạp đi qua điểm A(0,5 h; 9 km). Tốc độ của xe đạp là:", ["18 km/h", "9 km/h", "4,5 km/h", "15 km/h"], 0, "v = 9 / 0,5 = 18 km/h."),
        make_mc(8, "Thông hiểu", "Một vật chuyển động có đồ thị s - t: từ t = 0 đến t = 20 s đi được 100 m; từ t = 20 s đến t = 50 s đi thêm 150 m. So sánh tốc độ v1 và v2:", ["v1 = v2 = 5 m/s", "v1 > v2", "v1 < v2", "v2 = 0"], 0, "v1 = 100 / 20 = 5 m/s; v2 = 150 / (50 - 20) = 150 / 30 = 5 m/s => v1 = v2."),
        make_mc(9, "Thông hiểu", "Quan sát đồ thị s - t của hai người đi xe máy khởi hành cùng lúc: sau 1 giờ, người A đi được 45 km, người B đi được 35 km. Nhận xét nào đúng?", ["Đường đồ thị của người A dốc hơn đường đồ thị của người B", "Đường đồ thị của người B dốc hơn", "Hai đường đồ thị song song", "Hai đường đồ thị trùng nhau"], 0, "Người A có tốc độ 45 km/h lớn hơn người B (35 km/h) nên đồ thị của A dốc hơn."),
        make_mc(10, "Thông hiểu", "Một ô tô có đồ thị s - t đi qua điểm (2 h; 80 km). Để đi được quãng đường 200 km, ô tô cần thời gian là:", ["5 giờ", "4 giờ", "6 giờ", "4,5 giờ"], 0, "v = 80 / 2 = 40 km/h => t = 200 / 40 = 5 giờ."),
        make_mc(11, "Thông hiểu", "Đồ thị s - t của một ca nô đi trên hồ: đoạn 1 dốc lên ứng với v1 = 30 km/h trong 1 h; đoạn 2 nằm ngang dài 30 phút. Quãng đường ca nô đi được sau 1,5 h là:", ["30 km", "45 km", "60 km", "15 km"], 0, "30 phút sau ca nô dừng lại nên quãng đường giữ nguyên là 30 km."),
        make_mc(12, "Thông hiểu", "Trên đồ thị s - t của chuyển động thẳng, nếu một đường dốc xuống từ mức s = 60 km về s = 0 trong thời gian 1,5 h thì có nghĩa là:", ["Vật chuyển động đều quay trở về điểm xuất phát với tốc độ 40 km/h", "Vật bị lùi xe với tốc độ âm", "Quãng đường bị giảm đi", "Vật biến mất"], 0, "Đồ thị dốc về gốc s = 0 biểu diễn vật chuyển động đều từ khoảng cách 60 km quay về mốc ban đầu với tốc độ 60 / 1,5 = 40 km/h.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét ý nghĩa các dạng đường trên đồ thị quãng đường - thời gian (s - t):", [
            ("a", "Đường thẳng dốc lên thể hiện chuyển động thẳng đều.", True),
            ("b", "Đường nằm ngang song song trục Ot thể hiện trạng thái đứng yên.", True),
            ("c", "Đường thẳng càng gần phương thẳng đứng thì tốc độ chuyển động càng chậm.", False),
            ("d", "Giao điểm của hai đường đồ thị cho biết thời điểm và vị trí hai vật gặp nhau.", True)
        ], "Càng gần phương thẳng đứng thì độ dốc càng lớn, tốc độ càng nhanh."),
        make_tf(2, "Thông hiểu", "Phân tích đồ thị chuyển động của vận động viên chạy cự li 1500 m:", [
            ("a", "Trong 400 m đầu tiên vận động viên chạy hết 60 giây.", True),
            ("b", "Tốc độ ở chặng 400 m đầu là xấp xỉ 6,67 m/s.", True),
            ("c", "Ở chặng giữa 800 m tiếp theo vận động viên duy trì tốc độ đều 5 m/s trong 160 s.", True),
            ("d", "Vận động viên đứng yên hoàn toàn ở chặng nước rút 300 m cuối.", False)
        ], "Chặng nước rút cuối cùng vận động viên phải tăng tốc về đích, không thể đứng yên."),
        make_tf(3, "Vận dụng", "Hai xe ô tô xuất phát từ cùng một vị trí và đi cùng một hướng:", [
            ("a", "Xe 1 có đồ thị là đường thẳng s1 = 45t.", True),
            ("b", "Xe 2 có đồ thị là đường thẳng s2 = 60t.", True),
            ("c", "Sau 2 giờ, xe 2 đi trước xe 1 một khoảng cách là 30 km.", True),
            ("d", "Đồ thị của xe 1 có độ dốc lớn hơn đồ thị của xe 2.", False)
        ], "v2 = 60 km/h > v1 = 45 km/h nên đồ thị xe 2 dốc hơn xe 1."),
        make_tf(4, "Vận dụng", "Hành trình của một người đi xe đạp từ nhà đến bưu điện rồi quay về nhà:", [
            ("a", "Từ nhà đến bưu điện dài 6 km đi hết 24 phút (0,4 h).", True),
            ("b", "Tốc độ lúc đi là 15 km/h.", True),
            ("c", "Người đó gửi thư tại bưu điện mất 16 phút (khoảng thời gian đồ thị nằm ngang).", True),
            ("d", "Lúc quay về nhà hết 30 phút, tốc độ lúc về nhanh hơn lúc đi.", False)
        ], "Lúc về v = 6 / 0,5 = 12 km/h chậm hơn lúc đi (15 km/h).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Trên đồ thị s - t, vật đi được quãng đường 90 m trong 18 s. Tốc độ chuyển động là bao nhiêu m/s?", "5", "v = 90 / 18 = 5 m/s."),
        make_sa(2, "Thông hiểu", "Đồ thị s - t của ô tô có tốc độ 50 km/h. Sau 2,5 giờ ô tô đi được quãng đường bao nhiêu km?", "125", "s = 50 × 2,5 = 125 km."),
        make_sa(3, "Vận dụng", "Đồ thị s - t biểu diễn một vật: từ 0 đến 1 h đi 40 km, sau đó dừng lại nghỉ 0,5 h. Tổng thời gian của hành trình tính đến khi nghỉ xong là bao nhiêu phút?", "90", "1 h + 0,5 h = 1,5 h = 90 phút."),
        make_sa(4, "Vận dụng", "Từ đồ thị s - t, lúc t = 2 h xe ở vị trí s = 60 km, lúc t = 5 h xe ở vị trí s = 180 km. Tốc độ trung bình trong khoảng thời gian này là bao nhiêu km/h?", "40", "v = (180 - 60) / (5 - 2) = 120 / 3 = 40 km/h."),
        make_sa(5, "Vận dụng cao", "Xe 1 chuyển động với đồ thị s1 = 60t (km), xe 2 xuất phát từ điểm cách mốc 15 km chuyển động cùng chiều với s2 = 45t + 15 (km). Sau bao nhiêu giờ hai xe gặp nhau?", "1", "60t = 45t + 15 => 15t = 15 => t = 1 h."),
        make_sa(6, "Vận dụng cao", "Một vật chuyển động đều có đồ thị s - t đi qua điểm (5 s; 35 m). Để đi hết quãng đường 140 m, vật cần thời gian bao nhiêu giây?", "20", "v = 35 / 5 = 7 m/s => t = 140 / 7 = 20 s.")
    ],
    "part4": [
        make_vdc(1, "Đồ thị quãng đường - thời gian của một người đi bộ được mô tả qua 3 chặng: Chặng 1 đi đều 2 km trong 30 phút; Chặng 2 dừng uống nước 15 phút; Chặng 3 đi tiếp 3 km trong 45 phút. Tốc độ trung bình của người đó trên cả hành trình (kể cả thời gian nghỉ) là bao nhiêu km/h?", ["3,33 km/h", "4,00 km/h", "3,00 km/h", "2,50 km/h"], 0, "Tổng s = 2 + 3 = 5 km. Tổng t = 30 + 15 + 45 = 90 phút = 1,5 h => v_tb = 5 / 1,5 ≈ 3,33 km/h."),
        make_vdc(2, "Đồ thị s - t của hai xe máy A và B xuất phát từ cùng một điểm và đi cùng hướng. Xe A khởi hành lúc 8h00 chạy với tốc độ 30 km/h. Xe B khởi hành lúc 8h30 chạy với tốc độ 45 km/h để đuổi theo xe A. Hai xe gặp nhau lúc mấy giờ?", ["9h30 sáng", "9h00 sáng", "10h00 sáng", "10h30 sáng"], 0, "Thời gian xe B đuổi kịp xe A: t = (30 × 0,5) / (45 - 30) = 15 / 15 = 1,0 h kể từ lúc B xuất phát. Thời điểm gặp nhau: 8h30 + 1h = 9h30 sáng."),
        make_vdc(3, "Một ô tô đồ chơi chạy trên đường thẳng có đồ thị s - t gồm: giai đoạn 1 chạy từ O đến điểm (4 s; 8 m); giai đoạn 2 đứng yên trong 2 s; giai đoạn 3 chạy tiếp đến điểm (10 s; 20 m). Tốc độ của ô tô ở giai đoạn 3 là:", ["3 m/s", "2 m/s", "4 m/s", "2,5 m/s"], 0, "Giai đoạn 3 bắt đầu từ t = 6 s (s = 8 m) đến t = 10 s (s = 20 m) => v3 = (20 - 8) / (10 - 6) = 12 / 4 = 3 m/s."),
        make_vdc(4, "Một đoàn tàu xuất phát từ ga A lúc 6h00 và đến ga B lúc 8h30. Đồ thị s - t cho biết tàu chạy 60 km đầu hết 1 giờ; dừng đỗ tại ga phụ 15 phút; sau đó chạy 75 km còn lại trong 1 giờ 15 phút. Tốc độ trung bình của đoàn tàu trên cả chặng đường nối hai ga A và B là:", ["54 km/h", "60 km/h", "50 km/h", "48 km/h"], 0, "Tổng s = 60 + 75 = 135 km. Tổng t = 2,5 h => v_tb = 135 / 2,5 = 54 km/h.")
    ]
}

# --- ĐỀ 3 ---
b10_b11_exams["phys7_c3_b10_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 10: Đồ thị quãng đường - thời gian - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b10", "lessonName": "Bài 10: Đồ thị quãng đường - thời gian",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Đồ thị quãng đường - thời gian biểu diễn sự phụ thuộc của:", ["Quãng đường đi được vào thời gian chuyển động", "Thời gian chuyển động vào khối lượng", "Tốc độ vào gia tốc", "Lực kéo vào vận tốc"], 0, "Đồ thị biểu diễn hàm số s theo biến số thời gian t: s = s(t)."),
        make_mc(2, "Nhận biết", "Trong đồ thị s - t, đơn vị thường dùng của trục quãng đường và trục thời gian lần lượt là:", ["Mét (m) và Giây (s) hoặc Kilômét (km) và Giờ (h)", "Giây và Mét", "Mét và Kilôgam", "Lít và Giây"], 0, "Hệ đơn vị tương ứng: (m; s) hoặc (km; h)."),
        make_mc(3, "Nhận biết", "Nếu đồ thị s - t của một vật là một đường cong uốn lượn có độ dốc tăng dần thì chuyển động của vật là:", ["Chuyển động có tốc độ tăng dần theo thời gian (chuyển động nhanh dần)", "Chuyển động thẳng đều", "Chuyển động đứng yên", "Chuyển động chậm dần"], 0, "Độ dốc tăng dần đồng nghĩa với tốc độ tức thời tăng dần."),
        make_mc(4, "Nhận biết", "Để xác định thời gian cần thiết để đi được quãng đường s0 từ đồ thị s - t, ta thực hiện:", ["Từ giá trị s0 trên trục tung Os, kẻ đường song song với trục hoành Ot cắt đồ thị tại điểm M, rồi gióng xuống trục Ot để đọc giá trị t0", "Gióng trực tiếp từ gốc O", "Đo chiều dài thước kẻ", "Lấy s0 nhân với 3,6"], 0, "Phương pháp đọc đồ thị: gióng ngang từ s0 sang đồ thị rồi gióng dọc xuống trục Ot."),
        make_mc(5, "Nhận biết", "Đồ thị quãng đường - thời gian của một đoàn tàu đang đỗ tại sân ga là:", ["Một đoạn thẳng nằm ngang song song trục Ot", "Một đường thẳng xiên góc 45 độ", "Một đường thẳng đứng song song trục Os", "Một đường parabol cong"], 0, "Đang đỗ tại ga nghĩa là vật đứng yên, quãng đường không đổi theo thời gian."),
        make_mc(6, "Nhận biết", "Độ dốc của đồ thị s - t bằng 0 khi nào?", ["Khi vật đứng yên (đoạn đồ thị nằm ngang)", "Khi vật chạy cực nhanh", "Khi vật đổi hướng chuyển động", "Khi vật xuất phát"], 0, "Đoạn nằm ngang có độ dốc bằng 0, tương ứng tốc độ v = 0."),
        make_mc(7, "Thông hiểu", "Đồ thị s - t của một ô tô đi qua điểm B(1,5 h; 75 km). Tốc độ của ô tô là:", ["50 km/h", "75 km/h", "112,5 km/h", "60 km/h"], 0, "v = 75 / 1,5 = 50 km/h."),
        make_mc(8, "Thông hiểu", "Một người chạy bộ có đồ thị s - t đi qua điểm (30 s; 180 m). Tốc độ chạy của người đó tính theo km/h là:", ["21,6 km/h", "6,0 km/h", "18,0 km/h", "15,5 km/h"], 0, "v = 180 / 30 = 6 m/s = 6 × 3,6 = 21,6 km/h."),
        make_mc(9, "Thông hiểu", "Trên đồ thị s - t, đường chuyển động của xe 1 hợp với trục Ot một góc 30 độ, đường của xe 2 hợp với trục Ot một góc 60 độ. Kết luận nào đúng?", ["Xe 2 chuyển động nhanh hơn xe 1", "Xe 1 chuyển động nhanh hơn xe 2", "Hai xe chạy cùng tốc độ", "Xe 2 đứng yên"], 0, "Góc hợp với trục Ot càng lớn thì độ dốc càng lớn => tốc độ càng nhanh (tan 60° > tan 30°)."),
        make_mc(10, "Thông hiểu", "Đồ thị s - t của một học sinh đi xe đạp: từ 0 đến 10 phút đi được 2 km; từ 10 đến 25 phút đi thêm 3 km. Tốc độ trung bình trên toàn tuyến 5 km là:", ["12 km/h", "10 km/h", "15 km/h", "8 km/h"], 0, "Tổng s = 5 km, tổng t = 25 phút = 25/60 h = 5/12 h => v_tb = 5 / (5/12) = 12 km/h."),
        make_mc(11, "Thông hiểu", "Một xe khách có đồ thị s - t biểu diễn qua 2 chặng: chặng 1 chạy 60 km/h trong 2 h; chặng 2 chạy 40 km/h trong 1 h. Quãng đường tổng cộng xe đã đi là:", ["160 km", "100 km", "120 km", "150 km"], 0, "s = (60 × 2) + (40 × 1) = 120 + 40 = 160 km."),
        make_mc(12, "Thông hiểu", "Đồ thị s - t của hai vật xuất phát cùng lúc từ vị trí mốc s = 0. Sau thời gian t1, đồ thị của vật A ở mức s = 50 m, đồ thị vật B ở mức s = 30 m. Nhận xét nào đúng?", ["Vật A có tốc độ lớn hơn vật B", "Vật B có tốc độ lớn hơn vật A", "Hai vật có tốc độ bằng nhau", "Không thể kết luận được"], 0, "Cùng thời gian t1, vật A đi được quãng đường lớn hơn nên chuyển động nhanh hơn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phương pháp khai thác thông tin từ đồ thị quãng đường - thời gian:", [
            ("a", "Biết thời gian t có thể tra cứu được quãng đường s tương ứng.", True),
            ("b", "Biết quãng đường s có thể xác định được thời gian t cần thiết.", True),
            ("c", "Tốc độ tại một giai đoạn bằng thương số giữa độ dài đoạn quãng đường và thời gian đi đoạn đó.", True),
            ("d", "Đồ thị s - t không thể cho biết khi nào vật dừng lại nghỉ ngơi.", False)
        ], "Các đoạn nằm ngang trên đồ thị cho biết chính xác thời điểm và khoảng thời gian vật dừng nghỉ."),
        make_tf(2, "Thông hiểu", "Phân tích đồ thị chuyển động của một xe buýt nội thành:", [
            ("a", "Đồ thị gồm nhiều đoạn dốc lên xen kẽ với các đoạn nằm ngang ngắn.", True),
            ("b", "Các đoạn dốc lên thể hiện xe buýt đang di chuyển giữa các trạm dừng.", True),
            ("c", "Các đoạn nằm ngang thể hiện xe buýt đang dừng đón và trả khách tại các trạm.", True),
            ("d", "Chuyển động của xe buýt trên toàn bộ tuyến đường là chuyển động thẳng đều.", False)
        ], "Xe buýt di chuyển có dừng đỗ và thay đổi tốc độ liên tục nên là chuyển động không đều."),
        make_tf(3, "Vận dụng", "Hai bạn An và Bình cùng thi chạy trên quãng đường 100 m:", [
            ("a", "Đồ thị s - t của An đi qua điểm (12,5 s; 100 m), tốc độ của An là 8 m/s.", True),
            ("b", "Đồ thị s - t của Bình đi qua điểm (16,0 s; 100 m), tốc độ của Bình là 6,25 m/s.", True),
            ("c", "An về đích trước Bình một khoảng thời gian là 3,5 giây.", True),
            ("d", "Đường đồ thị của Bình dốc hơn đường đồ thị của An.", False)
        ], "An chạy nhanh hơn (8 m/s > 6,25 m/s) nên đường đồ thị của An dốc hơn Bình."),
        make_tf(4, "Vận dụng", "Một xe tải chở vật liệu có đồ thị chuyển động biểu diễn:", [
            ("a", "Chặng đầu: xe chạy từ mốc 0 đến 45 km trong 1 giờ.", True),
            ("b", "Xe dừng bốc dỡ hàng hóa trong 45 phút (0,75 giờ).", True),
            ("c", "Chặng sau: xe chạy tiếp từ km 45 đến km 90 trong 1 giờ 15 phút (1,25 giờ).", True),
            ("d", "Tốc độ trung bình trên toàn tuyến đường tính cả thời gian bốc dỡ hàng là 40 km/h.", False)
        ], "Tổng s = 90 km, tổng t = 1 + 0,75 + 1,25 = 3 h => v_tb = 90 / 3 = 30 km/h.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Từ đồ thị s - t, một vật đi được 150 m trong thời gian 25 s. Tốc độ của vật là bao nhiêu m/s?", "6", "v = 150 / 25 = 6 m/s."),
        make_sa(2, "Thông hiểu", "Một ô tô có đồ thị s - t biểu thị tốc độ 80 km/h. Sau 1,5 giờ ô tô đi được bao nhiêu km?", "120", "s = 80 × 1,5 = 120 km."),
        make_sa(3, "Vận dụng", "Đồ thị s - t có đoạn nằm ngang từ t = 45 phút đến t = 75 phút. Thời gian vật dừng nghỉ là bao nhiêu phút?", "30", "75 - 45 = 30 phút."),
        make_sa(4, "Vận dụng", "Lúc t = 1 h xe ở vị trí s = 25 km, lúc t = 4 h xe ở vị trí s = 145 km. Tốc độ trung bình trong khoảng thời gian này là bao nhiêu km/h?", "40", "v = (145 - 25) / (4 - 1) = 120 / 3 = 40 km/h."),
        make_sa(5, "Vận dụng cao", "Xe máy có đồ thị s1 = 40t, ô tô xuất phát cùng lúc từ vị trí s = 10 km với s2 = 60t + 10. Khoảng cách giữa hai xe sau 2 giờ là bao nhiêu km?", "50", "s1 = 80 km; s2 = 120 + 10 = 130 km => khoảng cách = 130 - 80 = 50 km."),
        make_sa(6, "Vận dụng cao", "Một vật chuyển động đều có đồ thị s - t đi qua điểm (4 s; 24 m). Thời gian để vật đi hết quãng đường 180 m là bao nhiêu giây?", "30", "v = 24 / 4 = 6 m/s => t = 180 / 6 = 30 s.")
    ],
    "part4": [
        make_vdc(1, "Đồ thị s - t của một người đạp xe biểu diễn: chặng 1 đi quãng đường 8 km với tốc độ 16 km/h; chặng 2 nghỉ giải lao 15 phút; chặng 3 đi tiếp quãng đường 12 km với tốc độ 12 km/h. Tốc độ trung bình của người đạp xe trên toàn bộ quãng đường 20 km kể cả thời gian nghỉ giải lao là:", ["11,43 km/h", "14,00 km/h", "10,50 km/h", "12,50 km/h"], 0, "t1 = 8 / 16 = 0,5 h; t2 = 15/60 = 0,25 h; t3 = 12 / 12 = 1,0 h. Tổng t = 1,75 h. v_tb = 20 / 1,75 ≈ 11,43 km/h."),
        make_vdc(2, "Đồ thị s - t của hai người đi bộ A và B khởi hành cùng lúc từ hai vị trí cách nhau 10 km đi ngược chiều nhau. Người A có đồ thị sA = 4t (km), người B có đồ thị sB = 10 - 6t (km). Hai người gặp nhau sau bao nhiêu giờ và cách vị trí xuất phát của A bao nhiêu km?", ["1,0 giờ và cách A 4 km", "1,5 giờ và cách A 6 km", "0,8 giờ và cách A 3,2 km", "2,0 giờ và cách A 8 km"], 0, "4t = 10 - 6t => 10t = 10 => t = 1,0 h. Vị trí gặp nhau s = 4 × 1 = 4 km."),
        make_vdc(3, "Một ca nô chạy trên hồ nước yên lặng có đồ thị s - t gồm: giai đoạn 1 chạy đều với tốc độ 24 km/h trong 45 phút (0,75 h); giai đoạn 2 dừng lại câu cá trong 30 phút (0,5 h); giai đoạn 3 chạy quay trở về điểm xuất phát ban đầu trong 45 phút. Tốc độ của ca nô ở giai đoạn 3 quay về là:", ["24 km/h", "18 km/h", "30 km/h", "16 km/h"], 0, "Quãng đường lúc đi s = 24 × 0,75 = 18 km. Lúc về đi 18 km trong 0,75 h => v3 = 18 / 0,75 = 24 km/h."),
        make_vdc(4, "Một đoàn tàu hỏa rời ga A đi đến ga B với đồ thị s - t: 15 phút đầu chạy tăng tốc dần đi được 10 km; 45 phút tiếp theo chạy đều với tốc độ 80 km/h đi được 60 km; 15 phút cuối giảm tốc đi được 10 km thì dừng lại tại ga B. Tổng quãng đường giữa hai ga và tốc độ trung bình của đoàn tàu là:", ["80 km và 64 km/h", "75 km và 60 km/h", "80 km và 70 km/h", "90 km và 72 km/h"], 0, "Tổng s = 10 + 60 + 10 = 80 km. Tổng t = 15 + 45 + 15 = 75 phút = 1,25 h => v_tb = 80 / 1,25 = 64 km/h.")
    ]
}

# =========================================================================
# BÀI 11: THẢO LUẬN VỀ ẢNH HƯỞNG CỦA TỐC ĐỘ TRONG AN TOÀN GIAO THÔNG (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b10_b11_exams["phys7_c3_b11_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b11", "lessonName": "Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Biển báo giao thông hình tròn viền đỏ, nền trắng, bên trong có ghi số '60' màu đen là biển báo:", ["Hạn chế tốc độ tối đa không được vượt quá 60 km/h", "Tốc độ tối thiểu phải chạy là 60 km/h", "Khoảng cách giữa hai xe là 60 m", "Cấm xe có trọng tải trên 60 tấn"], 0, "Biển P.127 giới hạn tốc độ tối đa cho phép."),
        make_mc(2, "Nhận biết", "Theo quy định an toàn giao thông đường bộ, khi chạy xe với tốc độ càng cao thì khoảng cách an toàn tối thiểu giữa hai xe phải:", ["Càng lớn hơn", "Càng nhỏ lại", "Giữ nguyên không đổi", "Bằng 0"], 0, "Tốc độ càng cao thì quãng đường phanh dừng càng dài nên khoảng cách an toàn phải càng lớn."),
        make_mc(3, "Nhận biết", "Quy tắc an toàn 'Khoảng cách 3 giây' khi lái xe trên đường cao tốc giúp người lái xe:", ["Đủ thời gian nhận biết chướng ngại vật, phản xạ và phanh dừng xe an toàn", "Chạy xe với tốc độ gấp đôi", "Tiết kiệm nhiên liệu", "Vượt xe phía trước dễ dàng"], 0, "Quy tắc 3 giây đảm bảo cự li phản ứng và hãm phanh khi xe phía trước phanh gấp."),
        make_mc(4, "Nhận biết", "Khi điều kiện thời tiết có mưa to, sương mù làm đường trơn trượt, người lái xe cần:", ["Chủ động giảm tốc độ và tăng khoảng cách an toàn so với xe phía trước", "Tăng tốc chạy thật nhanh về nhà", "Đi sát đuôi xe phía trước để bám đuôi", "Tắt toàn bộ đèn xe"], 0, "Mưa làm giảm độ ma sát lốp xe với mặt đường, tăng quãng đường trượt nên phải giảm tốc và tăng cự li."),
        make_mc(5, "Nhận biết", "Thiết bị an toàn nào trên ô tô được thiết kế để giữ chặt cơ thể hành khách, giảm nguy cơ va đập vào vô lăng hoặc văng ra ngoài khi có va chạm?", ["Dây an toàn (seatbelt)", "Gương chiếu hậu", "Cần gạt nước", "Đèn pha"], 0, "Dây an toàn giữ người ngồi cố định vào ghế theo quán tính khi phanh gấp."),
        make_mc(6, "Nhận biết", "Biển báo giao thông hình tròn nền xanh, bên trong có số '60' màu trắng là biển báo:", ["Tốc độ tối thiểu cho phép (phương tiện không được chạy dưới 60 km/h)", "Tốc độ tối đa cho phép", "Khoảng cách 60 m", "Hết mọi lệnh cấm"], 0, "Biển R.306 quy định tốc độ tối thiểu cho phép trên các làn xe cao tốc."),
        make_mc(7, "Thông hiểu", "Tại sao khi ô tô chạy với tốc độ 100 km/h gặp sự cố thì hậu quả va chạm nghiêm trọng hơn rất nhiều so với khi chạy 50 km/h?", ["Vì động năng của xe tỉ lệ với bình phương tốc độ (tăng 2 lần tốc độ làm động năng tăng gấp 4 lần)", "Vì ô tô bị nặng hơn", "Vì động cơ xe bị hỏng", "Vì lốp xe bị nổ ngay lập tức"], 0, "Động năng Wđ = 1/2 m v^2. Khi tốc độ tăng 2 lần, năng lượng va chạm tăng gấp 4 lần."),
        make_mc(8, "Thông hiểu", "Một người lái xe chạy với tốc độ 72 km/h (20 m/s). Thời gian từ lúc phát hiện chướng ngại vật đến khi đạp phanh (thời gian phản xạ) là 0,8 giây. Trong thời gian phản xạ đó, xe đi được quãng đường là:", ["16 m", "20 m", "10 m", "25 m"], 0, "s_phản_xạ = v × t = 20 × 0,8 = 16 m."),
        make_mc(9, "Thông hiểu", "Hệ thống phanh chống bó cứng ABS (Anti-lock Braking System) trên các dòng xe hiện đại có tác dụng:", ["Ngăn bánh xe bị khóa cứng khi phanh gấp, giúp tài xế vẫn kiểm soát được tay lái và tránh bị trượt lật", "Làm xe dừng lại ngay tức khắc trong 0 giây", "Tăng tốc độ của xe", "Tự động tắt động cơ"], 0, "Hệ thống ABS nhấp nhả phanh liên tục giúp bánh không bị trượt lết và giữ được hướng lái."),
        make_mc(10, "Thông hiểu", "Theo quy định Thông tư Bộ GTVT, khi xe lưu thông với tốc độ từ trên 60 km/h đến 80 km/h trên đường khô ráo, khoảng cách an toàn tối thiểu là:", ["55 m", "35 m", "70 m", "100 m"], 0, "Quy định cự li an toàn: 60 - 80 km/h là 55 m; 80 - 100 km/h là 70 m; 100 - 120 km/h là 100 m."),
        make_mc(11, "Thông hiểu", "Người điều khiển phương tiện xe máy, mô tô bắt buộc phải đội mũ bảo hiểm đạt chuẩn nhằm:", ["Bảo vệ vùng đầu và não bộ, giảm thiểu tối đa chấn thương sọ não khi xảy ra va chạm", "Tránh bụi bẩn cho mắt", "Tránh ánh nắng mặt trời", "Để nghe điện thoại dễ hơn"], 0, "Mũ bảo hiểm hấp thụ xung lực va đập, bảo vệ hộp sọ."),
        make_mc(12, "Thông hiểu", "Hành vi nào sau đây của người tham gia giao thông là vi phạm nghiêm trọng quy định an toàn về tốc độ?", ["Lái xe vượt quá tốc độ tối đa cho phép ghi trên biển báo", "Lái xe thấp hơn tốc độ tối đa", "Dừng xe khi gặp đèn đỏ", "Bật đèn xi nhan khi chuyển làn"], 0, "Chạy quá tốc độ tối đa là hành vi vi phạm nguy hiểm hàng đầu.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về mối quan hệ giữa tốc độ xe và an toàn giao thông đường bộ:", [
            ("a", "Tốc độ càng cao thì người lái xe càng có ít thời gian để xử lí các tình huống bất ngờ.", True),
            ("b", "Quãng đường phanh dừng xe tăng lên khi tốc độ chuyển động của xe tăng lên.", True),
            ("c", "Tốc độ không ảnh hưởng đến mức độ nghiêm trọng của chấn thương khi va chạm.", False),
            ("d", "Tuân thủ giới hạn tốc độ giúp giảm thiểu đáng kể số vụ tai nạn giao thông.", True)
        ], "Tốc độ ảnh hưởng mang tính quyết định đến mức độ tổn thương khi va chạm."),
        make_tf(2, "Thông hiểu", "Về việc giữ khoảng cách an toàn giữa các phương tiện trên cao tốc:", [
            ("a", "Khoảng cách an toàn là cự li tối thiểu cần duy trì với xe chạy liền phía trước.", True),
            ("b", "Khi tốc độ xe từ 80 đến 100 km/h, khoảng cách an toàn tối thiểu quy định là 70 m.", True),
            ("c", "Trời mưa phùn đường trơn có thể rút ngắn khoảng cách an toàn để tránh bị xe khác chen vào.", False),
            ("d", "Trên đường cao tốc thường có các biển báo khoảng cách 0m - 50m - 100m để tài xế căn chỉnh.", True)
        ], "Trời mưa trơn trượt bắt buộc phải tăng thêm khoảng cách an toàn, không được rút ngắn."),
        make_tf(3, "Vận dụng", "Tài xế đang lái ô tô với tốc độ 90 km/h (25 m/s) trên đường thẳng bất ngờ thấy chướng ngại vật:", [
            ("a", "Thời gian phản xạ của tài xế là 1,0 giây thì xe đã đi được quãng đường phản xạ là 25 m.", True),
            ("b", "Sau khi đạp phanh, xe cần quãng đường hãm phanh là 35 m nữa mới dừng hẳn.", True),
            ("c", "Tổng quãng đường dừng xe an toàn tính từ lúc nhìn thấy chướng ngại vật là 60 m.", True),
            ("d", "Nếu chướng ngại vật ở cách xe 50 m thì xe dừng lại an toàn mà không bị va chạm.", False)
        ], "Tổng quãng đường cần thiết là 25 + 35 = 60 m > 50 m nên xe sẽ va chạm vào chướng ngại vật."),
        make_tf(4, "Vận dụng", "Ứng dụng túi khí (Airbag) bảo vệ tính mạng trên xe ô tô:", [
            ("a", "Túi khí được kích hoạt bung ra cực nhanh trong vài phần trăm giây khi có va chạm mạnh phía trước.", True),
            ("b", "Túi khí tạo ra một lớp đệm mềm hấp thụ lực va đập của phần đầu và ngực hành khách.", True),
            ("c", "Khi đã có túi khí thì hành khách không cần phải thắt dây an toàn.", False),
            ("d", "Dây an toàn và túi khí là hệ thống bảo vệ bổ trợ chặt chẽ cho nhau.", True)
        ], "Nếu không thắt dây an toàn, người bị văng mạnh vào túi khí đang nổ với tốc độ cao có thể gây chấn thương nặng hơn.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Theo quy định, khoảng cách an toàn tối thiểu khi chạy xe với tốc độ trên 60 km/h đến 80 km/h trên đường khô ráo là bao nhiêu mét?", "55", "55 mét."),
        make_sa(2, "Thông hiểu", "Một ô tô chạy với tốc độ 20 m/s. Thời gian phản xạ của lái xe là 0,7 giây. Quãng đường xe đi trong thời gian phản xạ là bao nhiêu mét?", "14", "s = 20 × 0,7 = 14 m."),
        make_sa(3, "Vận dụng", "Quy tắc 3 giây trên cao tốc: Nếu xe đang chạy với tốc độ 72 km/h (20 m/s), khoảng cách an toàn 3 giây tương ứng là bao nhiêu mét?", "60", "s = 20 × 3 = 60 m."),
        make_sa(4, "Vận dụng", "Một xe máy chạy 54 km/h (15 m/s). Quãng đường phản xạ là 12 m và quãng đường hãm phanh là 18 m. Tổng quãng đường dừng xe là bao nhiêu mét?", "30", "12 + 18 = 30 m."),
        make_sa(5, "Vận dụng cao", "Khoảng cách an toàn tối thiểu quy định cho xe chạy từ trên 100 km/h đến 120 km/h trên cao tốc là bao nhiêu mét?", "100", "100 m."),
        make_sa(6, "Vận dụng cao", "Một người lái xe đạp phanh khẩn cấp làm xe trượt trên đường một vết dài 20 m với gia tốc hãm trung bình. Nếu tốc độ xe ban đầu tăng gấp đôi thì vết trượt phanh dài bao nhiêu mét?", "80", "Quãng đường phanh tỉ lệ với bình phương tốc độ: tăng 2 lần v => s tăng 2^2 = 4 lần: 20 × 4 = 80 m.")
    ],
    "part4": [
        make_vdc(1, "Một ô tô chạy với tốc độ 90 km/h (25 m/s) trên đường cao tốc. Phía trước có một xe tải phanh gấp. Thời gian phản xạ của tài xế là 0,8 giây và quãng đường hãm phanh xe dừng hẳn là 40 m. Để không đâm vào đuôi xe tải, khoảng cách tối thiểu giữa ô tô và xe tải khi xe tải bắt đầu phanh phải là:", ["60 m", "40 m", "50 m", "45 m"], 0, "Quãng đường phản xạ: 25 × 0,8 = 20 m. Tổng quãng đường dừng: 20 + 40 = 60 m."),
        make_vdc(2, "Theo quy tắc 'Khoảng cách 3 giây', một xe ô tô lưu thông trên đường cao tốc Nội Bài - Lào Cai với tốc độ 108 km/h. Để đảm bảo an toàn theo quy tắc này, khoảng cách với xe liền trước cần duy trì tối thiểu là bao nhiêu mét?", ["90 m", "108 m", "60 m", "75 m"], 0, "108 km/h = 30 m/s. Khoảng cách 3 giây: s = 30 × 3 = 90 m."),
        make_vdc(3, "Khi tham gia giao thông vào ban đêm trên đoạn đường ngoài đô thị không có dải phân cách giữa, người lái xe ô tô khi gặp xe đi ngược chiều phải:", ["Chuyển từ đèn chiếu xa (pha) sang đèn chiếu gần (cốt) để tránh làm lóa mắt tài xế xe đối diện", "Bật đèn chiếu xa thật sáng để nhìn rõ", "Bấm còi liên tục", "Tăng tốc chạy vượt qua"], 0, "Chuyển sang đèn cốt để chống chói mắt gây mù tạm thời cho tài xế xe ngược chiều."),
        make_vdc(4, "Một ô tô chạy trên đường khô ráo ở tốc độ 60 km/h thì quãng đường phanh dừng là 20 m. Khi trời mưa đường ướt, hệ số ma sát giảm một nửa làm quãng đường phanh tăng gấp đôi. Quãng đường phanh của xe trong điều kiện trời mưa ở cùng tốc độ 60 km/h là:", ["40 m", "30 m", "50 m", "60 m"], 0, "Hệ số ma sát giảm 1/2 thì quãng đường hãm phanh tăng gấp đôi: 20 × 2 = 40 m.")
    ]
}

# --- ĐỀ 2 ---
b10_b11_exams["phys7_c3_b11_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b11", "lessonName": "Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Biển báo hiệu lệnh R.420 hình chữ nhật nền xanh bên trong có hình vẽ các tòa nhà biểu thị:", ["Bắt đầu khu đông dân cư (phải giảm tốc độ theo quy định)", "Hết khu đông dân cư", "Đường cao tốc dành riêng cho ô tô", "Khu vực cấm xe ô tô"], 0, "Biển R.420 báo hiệu bắt đầu đoạn đường qua khu đông dân cư."),
        make_mc(2, "Nhận biết", "Quãng đường dừng xe an toàn của một phương tiện bao gồm:", ["Quãng đường xe đi được trong thời gian phản xạ cộng với quãng đường hãm phanh", "Chỉ quãng đường hãm phanh", "Chỉ quãng đường phản xạ", "Quãng đường xe lùi"], 0, "Quãng đường dừng xe = Quãng đường phản xạ + Quãng đường phanh."),
        make_mc(3, "Nhận biết", "Thời gian phản xạ của người lái xe là khoảng thời gian:", ["Từ khi mắt người lái nhìn thấy chướng ngại vật đến khi chân đạp vào bàn đạp phanh", "Từ khi đạp phanh đến khi xe dừng lại", "Thời gian xe đứng yên", "Thời gian động cơ nổ máy"], 0, "Đó là thời gian não bộ nhận biết tín hiệu nguy hiểm và truyền lệnh vận động đến chân đạp phanh."),
        make_mc(4, "Nhận biết", "Việc sử dụng rượu, bia hoặc chất kích thích trước khi lái xe gây nguy hiểm vì:", ["Làm tê liệt hệ thần kinh, kéo dài thời gian phản xạ và làm sai lệch phán đoán tốc độ", "Làm xe chạy nhanh hơn", "Làm lốp xe mòn nhanh hơn", "Làm tốn xăng hơn"], 0, "Cồn trong máu làm giảm khả năng phản xạ và kiểm soát hành vi lái xe."),
        make_mc(5, "Nhận biết", "Gờ giảm tốc được lắp đặt trên mặt đường tại các vị trí gần trường học, ngã tư nhằm:", ["Cảnh báo và buộc các phương tiện phải giảm tốc độ", "Làm đẹp cảnh quan đường phố", "Để thoát nước mưa", "Làm xe tăng tốc"], 0, "Gờ giảm tốc tạo rung chấn nhắc nhở tài xế giảm tốc độ."),
        make_mc(6, "Nhận biết", "Khi chuyển làn đường trên cao tốc, thao tác an toàn bắt buộc phải thực hiện là:", ["Bật đèn xi nhan báo rẽ, quan sát gương chiếu hậu đảm bảo an toàn rồi mới chuyển làn từ từ", "Đánh lái gấp sang làn bên cạnh ngay lập tức", "Bấm còi inh ỏi rồi rẽ", "Phanh dừng xe giữa đường"], 0, "Bật xi nhan cảnh báo và quan sát kĩ các góc gương chiếu hậu trước khi chuyển làn."),
        make_mc(7, "Thông hiểu", "Một xe chạy với tốc độ 54 km/h (15 m/s). Tài xế mất tập trung nhìn điện thoại 2 giây thì trong 2 giây đó xe đã đi được quãng đường là:", ["30 m mà không có sự kiểm soát của tài xế", "15 m", "10 m", "54 m"], 0, "s = 15 × 2 = 30 m xe lao đi trong tình trạng tài xế hoàn toàn mất tập trung."),
        make_mc(8, "Thông hiểu", "Theo quy định an toàn đối với đoạn đường khô ráo khi xe chạy từ trên 80 km/h đến 100 km/h, khoảng cách an toàn tối thiểu là:", ["70 m", "55 m", "35 m", "100 m"], 0, "Cự li an toàn tối thiểu tương ứng là 70 m."),
        make_mc(9, "Thông hiểu", "Lốp xe ô tô bị mòn rãnh gai quá mức cho phép sẽ gây nguy hiểm vì:", ["Làm giảm độ bám đường, tăng nguy cơ trượt nước và kéo dài quãng đường phanh", "Làm xe chạy chậm đi", "Làm xe nặng hơn", "Làm hỏng còi xe"], 0, "Rãnh gai lốp thoát nước, lốp mòn làm mất ma sát gây trượt lết nguy hiểm."),
        make_mc(10, "Thông hiểu", "Hệ thống cân bằng điện tử ESC (Electronic Stability Control) trên ô tô có tác dụng:", ["Tự động can thiệp phanh từng bánh xe để ngăn xe bị văng đuôi hoặc mất lái khi vào cua ở tốc độ cao", "Làm xe bay lên khỏi chướng ngại vật", "Làm sáng đèn pha", "Đóng cửa sổ tự động"], 0, "ESC ổn định thân xe, chống lật và trượt văng khi cua gấp ở tốc độ cao."),
        make_mc(11, "Thông hiểu", "Trẻ em ngồi trên xe ô tô cần được trang bị thiết bị an toàn nào phù hợp với lứa tuổi?", ["Ghế an toàn chuyên dụng cho trẻ em gắn chặt với ghế xe và thắt dây an toàn", "Để trẻ đứng tự do trên ghế sau", "Để trẻ ngồi trong lòng người lái xe", "Cho trẻ thò đầu ra cửa sổ trời"], 0, "Ghế trẻ em chuyên dụng (Child car seat) bảo vệ xương khớp non nớt khi có va chạm."),
        make_mc(12, "Thông hiểu", "Vào ban ngày khi đi qua hầm đường bộ, người điều khiển phương tiện bắt buộc phải:", ["Bật đèn chiếu sáng gần (đèn cốt)", "Tắt hết đèn xe", "Bật đèn pha chiếu xa", "Đi lùi xe"], 0, "Bắt buộc phải bật đèn chiếu gần khi vào hầm đường bộ.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các yếu tố ảnh hưởng trực tiếp đến thời gian phản xạ của người lái xe:", [
            ("a", "Sự mệt mỏi, buồn ngủ làm tăng đáng kể thời gian phản xạ.", True),
            ("b", "Sử dụng điện thoại di động khi lái xe làm người lái mất tập trung quan sát.", True),
            ("c", "Tuổi tác và kinh nghiệm lái xe có ảnh hưởng đến tốc độ phản ứng tình huống.", True),
            ("d", "Uống cà phê đặc giúp người lái xe có thể phản ứng nhanh tức thì trong 0 giây.", False)
        ], "Dù tỉnh táo đến đâu, con người luôn cần thời gian phản xạ tối thiểu khoảng 0,5 - 0,7 s."),
        make_tf(2, "Thông hiểu", "Về tình trạng mặt đường ảnh hưởng đến an toàn khi chuyển động ở tốc độ cao:", [
            ("a", "Mặt đường khô ráo, bê tông nhám có độ ma sát bám đường tốt nhất.", True),
            ("b", "Mặt đường dính bùn đất hoặc dầu mỡ làm giảm nghiêm trọng ma sát trượt.", True),
            ("c", "Khi trời mưa lớn, hiện tượng màng nước nêm lốp (thủy phi cơ) có thể làm xe mất hoàn toàn lái.", True),
            ("d", "Xe chạy ở tốc độ 120 km/h trên đường ướt có quãng đường phanh ngắn hơn đường khô.", False)
        ], "Đường ướt trơn làm quãng đường phanh dài hơn nhiều so với đường khô."),
        make_tf(3, "Vận dụng", "Một xe khách 29 chỗ chạy trên quốc lộ với tốc độ 72 km/h (20 m/s):", [
            ("a", "Tài xế nhìn thấy biển báo công trường cách 70 m.", True),
            ("b", "Thời gian phản xạ của tài xế là 0,8 giây, xe chạy được 16 m trước khi đạp phanh.", True),
            ("c", "Xe đạp phanh và dừng lại sau quãng đường phanh 34 m.", True),
            ("d", "Xe dừng lại cách biển báo công trường một khoảng an toàn là 20 m.", True)
        ], "Tổng quãng đường dừng = 16 + 34 = 50 m. Cách biển báo: 70 - 50 = 20 m."),
        make_tf(4, "Vận dụng", "Hệ thống camera phạt nguội giám sát tốc độ phương tiện:", [
            ("a", "Được lắp đặt cố định tại các điểm đen tai nạn hoặc giá long môn cao tốc.", True),
            ("b", "Ghi lại chính xác hình ảnh phương tiện, tốc độ đo được và thời điểm vi phạm.", True),
            ("c", "Chỉ xử phạt được các phương tiện vào ban ngày, ban đêm không hoạt động.", False),
            ("d", "Giúp lực lượng chức năng xử lí vi phạm công khai, minh bạch và nâng cao ý thức tài xế.", True)
        ], "Camera hiện đại có đèn hồng ngoại hoạt động rõ nét cả ban đêm.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khoảng cách an toàn tối thiểu theo luật giao thông khi xe chạy từ trên 80 km/h đến 100 km/h trên đường khô ráo là bao nhiêu mét?", "70", "70 m."),
        make_sa(2, "Thông hiểu", "Một ô tô chạy tốc độ 25 m/s. Thời gian phản xạ của tài xế là 0,8 s. Quãng đường phản xạ là bao nhiêu mét?", "20", "s = 25 × 0,8 = 20 m."),
        make_sa(3, "Vận dụng", "Quy tắc 3 giây: Xe chạy với tốc độ 90 km/h (25 m/s). Khoảng cách 3 giây tương ứng là bao nhiêu mét?", "75", "25 × 3 = 75 m."),
        make_sa(4, "Vận dụng", "Xe máy chạy 36 km/h (10 m/s). Quãng đường phản xạ là 7 m, quãng đường hãm phanh là 8 m. Tổng quãng đường dừng xe là bao nhiêu mét?", "15", "7 + 8 = 15 m."),
        make_sa(5, "Vận dụng cao", "Khoảng cách an toàn tối thiểu quy định cho xe chạy từ 60 km/h trở xuống trên đường cao tốc là bao nhiêu mét?", "35", "35 m."),
        make_sa(6, "Vận dụng cao", "Một ô tô phanh gấp tạo vết trượt dài 15 m ở tốc độ 40 km/h. Nếu ô tô chạy 80 km/h (tăng gấp đôi) thì vết trượt phanh dài bao nhiêu mét?", "60", "s tỉ lệ với v^2: 15 × 2^2 = 15 × 4 = 60 m.")
    ],
    "part4": [
        make_vdc(1, "Một xe ô tô chạy với tốc độ 80 km/h (xấp xỉ 22,2 m/s). Phía trước có vật cản cách 50 m. Thời gian phản xạ của lái xe là 0,7 giây và quãng đường hãm phanh là 28 m. Ô tô có dừng lại kịp trước vật cản không và còn cách vật cản bao nhiêu mét?", ["Có dừng lại kịp, còn cách vật cản xấp xỉ 6,46 m", "Không kịp, đâm vào vật cản", "Dừng lại chạm đúng vật cản", "Còn cách 15 m"], 0, "s_phản_xạ = 22,2 × 0,7 ≈ 15,54 m. Tổng quãng đường dừng: 15,54 + 28 = 43,54 m < 50 m => Cách vật cản: 50 - 43,54 = 6,46 m."),
        make_vdc(2, "Theo quy định tại Thông tư 31/2019/TT-BGTVT, tốc độ tối đa cho phép của xe cơ giới (trừ xe máy chuyên dùng, xe gắn máy) trên đường bộ trong khu vực đông dân cư có đường đôi hoặc đường một chiều có từ hai làn xe cơ giới trở lên là:", ["60 km/h", "50 km/h", "70 km/h", "80 km/h"], 0, "Đường đôi/đường 1 chiều từ 2 làn trở lên trong khu đông dân cư tối đa là 60 km/h."),
        make_vdc(3, "Tại sao khi chạy xe trên đường đèo dốc quanh co có nhiều khúc cua gấp, lái xe tuyệt đối không được rà phanh liên tục trong thời gian dài mà phải về số thấp (hãm bằng động cơ)?", ["Vì rà phanh liên tục làm má phanh bị ma sát quá nhiệt dẫn đến cháy phanh, sôi dầu phanh và mất hoàn toàn tác dụng phanh", "Để xe chạy nhanh hơn", "Để đỡ tốn xăng", "Để động cơ không bị ồn"], 0, "Rà phanh liên tục khi đổ đèo làm má phanh quá nhiệt, gây trơ lì má phanh và mất phanh nguy hiểm."),
        make_vdc(4, "Một tài xế lái xe với tốc độ 100 km/h trên cao tốc vào một ngày trời mưa tầm tã. Biết khoảng cách an toàn tối thiểu theo luật trên đường khô ráo là 70 m, và quy chuẩn an toàn khuyến cáo phải tăng khoảng cách thêm ít nhất 50% khi đường trơn trượt. Khoảng cách an toàn tài xế cần giữ lúc này là:", ["105 m", "70 m", "85 m", "140 m"], 0, "70 × 1,5 = 105 m.")
    ]
}

# --- ĐỀ 3 ---
b10_b11_exams["phys7_c3_b11_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b11", "lessonName": "Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Biển báo cự li an toàn tối thiểu giữa hai xe (biển P.121) có hình vẽ hai chiếc ô tô nối đuôi nhau và ghi số '50m' ở giữa nghĩa là:", ["Các xe phải giữ khoảng cách an toàn không nhỏ hơn 50 mét", "Các xe phải chạy cách nhau đúng 50 cm", "Đoạn đường dài 50 mét", "Tốc độ tối đa là 50 km/h"], 0, "Biển P.121 quy định cự li tối thiểu giữa hai xe."),
        make_mc(2, "Nhận biết", "Khi điều khiển xe ô tô lưu thông trên đường cao tốc, hành vi nào sau đây bị nghiêm cấm tuyệt đối?", ["Cho xe chạy lùi hoặc quay đầu xe trên đường cao tốc", "Bật đèn pha chiếu sáng", "Giữ khoảng cách an toàn với xe trước", "Chạy xe đúng làn đường quy định"], 0, "Nghiêm cấm lùi xe, quay đầu xe trên cao tốc vì nguy cơ tai nạn đặc biệt thảm khốc."),
        make_mc(3, "Nhận biết", "Lực cản không khí tác dụng lên xe ô tô khi chuyển động tỉ lệ thuận với bình phương tốc độ. Điều này có nghĩa là:", ["Khi xe chạy càng nhanh, lực cản không khí càng tăng mạnh làm tiêu tốn nhiều nhiên liệu hơn", "Xe chạy nhanh thì lực cản giảm", "Không khí không cản trở xe", "Xe chạy càng chậm thì càng tốn xăng"], 0, "Lực cản khí động học tăng theo v^2 nên chạy quá nhanh rất tốn nhiên liệu."),
        make_mc(4, "Nhận biết", "Thiết bị giám sát hành trình (hộp đen) lắp đặt bắt buộc trên các xe ô tô kinh doanh vận tải dùng để:", ["Ghi nhận hành trình, tốc độ di chuyển và thời gian lái xe liên tục của tài xế", "Đo nhiệt độ buồng lái", "Làm mát động cơ", "Bật nhạc giải trí"], 0, "Hộp đen giám sát tốc độ và thời gian làm việc của tài xế để đảm bảo an toàn."),
        make_mc(5, "Nhận biết", "Để cảnh báo nguy hiểm khi xe bị hỏng phải đỗ lại trên làn khẩn cấp của đường cao tốc, người lái xe cần:", ["Bật đèn cảnh báo nguy hiểm (hazard) và đặt tam giác phản quang cách đuôi xe ít nhất 100 - 150 m", "Ngồi trong xe ngủ", "Tắt hết đèn xe", "Đứng giữa làn đường vẫy tay"], 0, "Đặt biển cảnh báo tam giác phản quang từ xa để các xe sau kịp giảm tốc tránh."),
        make_mc(6, "Nhận biết", "Theo luật Giao thông đường bộ, thời gian lái xe liên tục tối đa của một tài xế ô tô kinh doanh vận tải không được vượt quá:", ["4 giờ liên tục", "8 giờ liên tục", "10 giờ liên tục", "12 giờ liên tục"], 0, "Quy định tài xế không được lái xe quá 4 giờ liên tục để tránh mệt mỏi gây tai nạn."),
        make_mc(7, "Thông hiểu", "Một xe con chạy trên cao tốc với tốc độ 120 km/h (xấp xỉ 33,3 m/s). Chỉ trong 1 giây lơ đãng, xe đã di chuyển được quãng đường hơn:", ["33 mét", "12 mét", "20 mét", "10 mét"], 0, "Trong 1 s xe đi được 33,3 m, bằng chiều dài của hơn 7 chiếc ô tô con nối đuôi nhau."),
        make_mc(8, "Thông hiểu", "Theo quy định, khoảng cách an toàn tối thiểu giữa hai xe khi lưu thông trên đường cao tốc với tốc độ trên 100 km/h đến 120 km/h là:", ["100 m", "70 m", "55 m", "35 m"], 0, "Quy định cự li tối thiểu là 100 m đối với dải tốc độ 100 - 120 km/h."),
        make_mc(9, "Thông hiểu", "Tại sao người ngồi ghế trước trên ô tô không cài dây an toàn thì khi xe đâm va trực diện sẽ bị hất văng về phía trước đập đầu vào kính chắn gió?", ["Do quán tính, cơ thể người có xu hướng tiếp tục duy trì trạng thái chuyển động về phía trước", "Do kính chắn gió hút người", "Do động cơ xe đẩy người", "Do trọng lực kéo về phía trước"], 0, "Theo định luật quán tính, khi xe dừng đột ngột, người tiếp tục lao về phía trước."),
        make_mc(10, "Thông hiểu", "Biển báo 'Đoạn đường hay xảy ra tai nạn' kết hợp với biển giới hạn tốc độ 40 km/h đặt ở đoạn đường đèo dốc quanh co nhằm:", ["Nhắc nhở lái xe tập trung cao độ và giảm tốc độ thấp để dễ dàng kiểm soát tay lái khi vào cua", "Cấm xe máy đi qua", "Cho phép xe vượt nhau", "Để xe dừng lại chụp ảnh"], 0, "Hạn chế tốc độ để triệt tiêu lực quán tính ly tâm khi vào cua nguy hiểm."),
        make_mc(11, "Thông hiểu", "Gương chiếu hậu trên xe máy và ô tô giúp người lái xe:", ["Quan sát được tình hình giao thông và phương tiện phía sau cũng như hai bên hông xe", "Soi gương làm đẹp", "Che gió cho tay lái", "Bắt tín hiệu sóng radio"], 0, "Gương chiếu hậu bao quát điểm mù và phương tiện phía sau."),
        make_mc(12, "Thông hiểu", "Hành động nào sau đây thể hiện văn hóa giao thông và đảm bảo an toàn tốc độ?", ["Chủ động giảm tốc độ khi đi qua khu dân cư, trường học và nhường đường cho người đi bộ", "Bóp còi inh ỏi để phóng nhanh qua đám đông", "Lạng lách đánh võng vượt đèn vàng", "Đua xe trái phép trên quốc lộ"], 0, "Giảm tốc độ, chú ý quan sát và nhường đường thể hiện văn hóa giao thông chuẩn mực.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các quy tắc an toàn khi điều khiển xe trên đường cao tốc:", [
            ("a", "Phương tiện chạy chậm hơn phải đi về làn đường bên phải theo chiều đi của mình.", True),
            ("b", "Chỉ được chuyển làn ở những đoạn đường có vạch kẻ đường đứt nét.", True),
            ("c", "Được phép dừng đỗ xe tùy tiện trên bất kì làn đường nào để ngắm cảnh.", False),
            ("d", "Làn dừng xe khẩn cấp chỉ dùng cho các xe gặp sự cố hoặc xe ưu tiên khi làm nhiệm vụ.", True)
        ], "Tuyệt đối không được dừng đỗ tùy tiện trên cao tốc."),
        make_tf(2, "Thông hiểu", "Về tác dụng của hệ thống chiếu sáng xe vào ban đêm đối với an toàn tốc độ:", [
            ("a", "Đèn pha chiếu xa giúp tài xế quan sát đường ở cự li xa khi đường vắng.", True),
            ("b", "Khi đi sau xe khác ở cự li gần, phải chuyển sang đèn cốt để không làm chói mắt tài xế xe trước qua gương chiếu hậu.", True),
            ("c", "Đèn sương mù màu vàng giúp tăng khả năng nhận diện đường khi thời tiết nhiều sương mù.", True),
            ("d", "Bật đèn xi nhan khẩn cấp liên tục khi đang chạy bình thường ở tốc độ cao để xin đường là đúng luật.", False)
        ], "Đèn khẩn cấp (hazard) chỉ dùng khi xe gặp sự cố nguy hiểm dừng đỗ, không dùng để xin vượt tùy tiện."),
        make_tf(3, "Vận dụng", "Một xe container di chuyển với tốc độ 60 km/h (xấp xỉ 16,7 m/s):", [
            ("a", "Khối lượng của xe container rất lớn nên quán tính của xe rất lớn.", True),
            ("b", "Thời gian phản xạ của tài xế là 1,0 s, xe đi được khoảng 16,7 m.", True),
            ("c", "Do tải trọng nặng, quãng đường hãm phanh của xe container dài hơn nhiều so với xe con.", True),
            ("d", "Xe container có thể dừng lại ngay tức khắc trong cự li 1 m khi phanh gấp.", False)
        ], "Xe tải nặng có quán tính cực lớn, quãng đường phanh cần thiết rất dài, không thể dừng ngay trong 1 m."),
        make_tf(4, "Vận dụng", "Quy định về nồng độ cồn đối với người điều khiển phương tiện giao thông ở Việt Nam (Nghị định 100/2019/NĐ-CP):", [
            ("a", "Nghiêm cấm tuyệt đối người điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn.", True),
            ("b", "Người có nồng độ cồn vượt mức quy định sẽ bị xử phạt tiền và tước quyền sử dụng giấy phép lái xe.", True),
            ("c", "Uống một lon bia thì vẫn được phép lái xe máy nếu cảm thấy bản thân còn tỉnh táo.", False),
            ("d", "Đã uống rượu bia thì không lái xe là khẩu hiệu an toàn mang tính sống còn.", True)
        ], "Luật quy định nồng độ cồn bằng 0 khi lái xe, không có mức miễn trừ tự cảm nhận.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Khoảng cách an toàn tối thiểu theo quy định khi xe chạy với tốc độ từ trên 100 km/h đến 120 km/h trên cao tốc là bao nhiêu mét?", "100", "100 m."),
        make_sa(2, "Thông hiểu", "Một ô tô chạy tốc độ 30 m/s. Thời gian phản xạ là 0,6 s. Quãng đường xe chạy trong thời gian phản xạ là bao nhiêu mét?", "18", "s = 30 × 0,6 = 18 m."),
        make_sa(3, "Vận dụng", "Theo quy tắc 3 giây: Xe chạy với tốc độ 108 km/h (30 m/s). Khoảng cách an toàn 3 giây là bao nhiêu mét?", "90", "30 × 3 = 90 m."),
        make_sa(4, "Vận dụng", "Xe chạy với tốc độ 72 km/h (20 m/s). Quãng đường phản xạ là 16 m, quãng đường hãm phanh là 24 m. Tổng quãng đường dừng xe là bao nhiêu mét?", "40", "16 + 24 = 40 m."),
        make_sa(5, "Vận dụng cao", "Một tài xế lái xe liên tục suốt 3,5 giờ. Theo luật giao thông đường bộ, tài xế chỉ được phép lái thêm tối đa bao nhiêu phút nữa trước khi bắt buộc phải dừng nghỉ?", "30", "Luật quy định tối đa 4 giờ liên tục => 4 h - 3,5 h = 0,5 h = 30 phút."),
        make_sa(6, "Vận dụng cao", "Một xe tải chở nặng phanh gấp ở tốc độ 50 km/h tạo vết trượt phanh 25 m. Nếu xe chạy 100 km/h (tăng gấp đôi) thì vết trượt phanh dài bao nhiêu mét?", "100", "25 × 2^2 = 25 × 4 = 100 m.")
    ],
    "part4": [
        make_vdc(1, "Một xe khách đang chạy với tốc độ 72 km/h (20 m/s) trên đường quốc lộ thì gặp chướng ngại vật ở cách xe 45 m. Biết thời gian phản xạ của tài xế là 0,7 giây và quãng đường hãm phanh là 28 m. Xe khách có dừng lại an toàn trước chướng ngại vật không và dừng cách chướng ngại vật bao nhiêu mét?", ["Có dừng lại an toàn, cách chướng ngại vật 3 m", "Không an toàn, va chạm vào chướng ngại vật", "Dừng cách chướng ngại vật 10 m", "Dừng cách chướng ngại vật 15 m"], 0, "Quãng đường phản xạ: 20 × 0,7 = 14 m. Tổng quãng đường dừng: 14 + 28 = 42 m < 45 m => Dừng cách chướng ngại vật: 45 - 42 = 3 m."),
        make_vdc(2, "Theo quy định tại Thông tư số 31/2019/TT-BGTVT, khi tham gia giao thông trên đường bộ ngoài khu vực đông dân cư (trừ đường cao tốc), tốc độ tối đa cho phép đối với xe ô tô con trên đường đôi (có dải phân cách giữa) là:", ["90 km/h", "80 km/h", "70 km/h", "100 km/h"], 0, "Ngoài khu đông dân cư, đường đôi có dải phân cách giữa: xe ô tô con được chạy tối đa 90 km/h."),
        make_vdc(3, "Để vượt xe khác một cách an toàn trên đường hai chiều không có dải phân cách giữa, người lái xe phải tuân thủ điều kiện nào sau đây?", ["Chỉ được vượt khi không có chướng ngại vật phía trước, không có xe chạy ngược chiều trong đoạn đường định vượt và xe chạy trước đã có tín hiệu nhường đường", "Vượt ngay tại khúc cua khuất tầm nhìn", "Vượt khi xe phía trước đang vượt xe khác", "Bấm còi và ép xe ngược chiều xuống lề đường"], 0, "Chỉ được vượt khi đủ tầm nhìn, không có xe đối diện và xe trước nhường đường."),
        make_vdc(4, "Một người điều khiển xe máy đi với tốc độ 40 km/h trên đường trơn ướt. Để đảm bảo an toàn, khoảng cách với xe phía trước cần tối thiểu 30 m. Nếu người này chạy với tốc độ 60 km/h trong cùng điều kiện thì khoảng cách an toàn tối thiểu theo tỉ lệ bình phương tốc độ phải tăng lên xấp xỉ bao nhiêu mét?", ["67,5 m", "45,0 m", "60,0 m", "50,0 m"], 0, "Khoảng cách tỉ lệ với v^2: 30 × (60/40)^2 = 30 × 1,5^2 = 30 × 2,25 = 67,5 m.")
    ]
}
