# -*- coding: utf-8 -*-
"""
CHƯƠNG V: ÁNH SÁNG - BÀI 17: ẢNH CỦA MỘT VẬT TẠO BỞI GƯƠNG PHẲNG (3 ĐỀ ĐỘC LẬP 100%)
- phys7_c5_b17: Bài 17 (3 đề: test1, test2, test3)
Không trùng lặp, không tiền tố "Đề X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

b17_exams = {}

# =========================================================================
# BÀI 17: ẢNH CỦA MỘT VẬT TẠO BỞI GƯƠNG PHẲNG (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b17_exams["phys7_c5_b17_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 17: Ảnh của một vật tạo bởi gương phẳng - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b17", "lessonName": "Bài 17: Ảnh của một vật tạo bởi gương phẳng",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Ảnh của một vật tạo bởi gương phẳng có tính chất nào sau đây?", ["Là ảnh ảo, không hứng được trên màn chắn", "Là ảnh thật, hứng được trên màn chắn", "Là ảnh ảo lớn hơn vật", "Là ảnh thật nhỏ hơn vật"], 0, "Ảnh qua gương phẳng là ảnh ảo không hứng được trên màn chắn."),
        make_mc(2, "Nhận biết", "Độ lớn của ảnh của một vật tạo bởi gương phẳng:", ["Bằng độ lớn của vật", "Lớn hơn độ lớn của vật", "Nhỏ hơn độ lớn của vật", "Gấp đôi độ lớn của vật"], 0, "Độ lớn ảnh luôn bằng độ lớn của vật."),
        make_mc(3, "Nhận biết", "Khoảng cách từ một điểm trên vật đến gương phẳng và khoảng cách từ ảnh của điểm đó đến gương phẳng có mối quan hệ:", ["Bằng nhau", "Khoảng cách từ ảnh lớn hơn", "Khoảng cách từ ảnh nhỏ hơn", "Không bằng nhau"], 0, "Vật và ảnh cách đều mặt phẳng gương."),
        make_mc(4, "Nhận biết", "Ảnh của một vật qua gương phẳng và vật có tính chất đối xứng với nhau qua:", ["Mặt phẳng gương", "Trục thẳng đứng", "Đường pháp tuyến", "Điểm tới"], 0, "Vật và ảnh ảo đối xứng nhau qua mặt phẳng gương."),
        make_mc(5, "Nhận biết", "Vùng không gian mà mắt người quan sát có thể nhìn thấy ảnh của các vật qua gương phẳng được gọi là:", ["Vùng quan sát của gương phẳng (thị trường của gương)", "Vùng bóng tối", "Vùng mù", "Tiêu cự"], 0, "Vùng quan sát (thị trường) của gương phẳng."),
        make_mc(6, "Nhận biết", "Bác sĩ nha khoa thường dùng một chiếc gương tròn nhỏ đưa vào miệng bệnh nhân nhằm:", ["Quan sát ảnh của các góc khuất và mặt sau của răng", "Để đo nhiệt độ", "Để mài răng", "Để làm sáng mắt"], 0, "Gương nha sĩ quan sát ảnh của các góc khuất trong hàm răng."),
        make_mc(7, "Thông hiểu", "Một ngọn nến đặt thẳng đứng cách gương phẳng 20 cm. Ảnh của ngọn nến cách gương phẳng một khoảng là:", ["20 cm", "40 cm", "10 cm", "30 cm"], 0, "d' = d = 20 cm."),
        make_mc(8, "Thông hiểu", "Một vật đặt cách gương phẳng 50 cm. Khoảng cách giữa vật và ảnh của nó tạo bởi gương phẳng là:", ["100 cm (1 mét)", "50 cm", "25 cm", "0 cm"], 0, "Khoảng cách giữa vật và ảnh = 2d = 2 × 50 = 100 cm = 1 m."),
        make_mc(9, "Thông hiểu", "Một bạn học sinh cao 1,6 mét đứng trước một chiếc gương phẳng treo thẳng đứng. Chiều cao ảnh của bạn học sinh trong gương là:", ["1,6 mét", "0,8 mét", "3,2 mét", "1,2 mét"], 0, "Độ lớn ảnh bằng độ lớn vật nên chiều cao ảnh là 1,6 m."),
        make_mc(10, "Thông hiểu", "Một người đứng cách gương phẳng 2 m, nếu người đó tiến lại gần gương thêm 0,5 m thì khoảng cách giữa người đó và ảnh của mình trong gương là:", ["3,0 m", "1,5 m", "4,0 m", "2,5 m"], 0, "Khoảng cách mới đến gương: 2 - 0,5 = 1,5 m => Khoảng cách giữa người và ảnh: 2 × 1,5 = 3,0 m."),
        make_mc(11, "Thông hiểu", "Vì sao trên đầu xe cứu thương (Ambulance), dòng chữ thường được in ngược (ꓱƆИA⅃UᙠMA)?", ["Để khi tài xế xe phía trước nhìn qua gương chiếu hậu sẽ thấy dòng chữ xuôi chiều 'AMBULANCE' rõ ràng và kịp thời nhường đường", "Do máy in bị lỗi", "Là phong cách thẩm mỹ", "Để người đi bộ đọc dễ hơn"], 0, "Gương phẳng đảo trái phải, in ngược chữ giúp người nhìn qua gương thấy chữ xuôi."),
        make_mc(12, "Thông hiểu", "Khi đưa một bàn tay phải đặt song song trước gương phẳng, ảnh của bàn tay trong gương giống như bàn tay nào của một người đối diện?", ["Bàn tay trái", "Bàn tay phải", "Cả hai bàn tay", "Bàn chân"], 0, "Gương phẳng có tính chất đối xứng trục đảo ngược trái - phải.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất cơ bản của ảnh tạo bởi gương phẳng:", [
            ("a", "Ảnh tạo bởi gương phẳng là ảnh ảo, không hứng được trên màn chắn đặt phía sau gương.", True),
            ("b", "Kích thước của ảnh luôn luôn bằng kích thước thật của vật.", True),
            ("c", "Nếu người lùi ra xa gương phẳng thì kích thước thật của ảnh trong gương sẽ nhỏ đi.", False),
            ("d", "Khoảng cách từ vật đến gương bằng khoảng cách từ ảnh đến gương.", True)
        ], "Kích thước thật của ảnh luôn bằng vật, nhìn thấy nhỏ đi là do góc trông của mắt giảm khi ra xa."),
        make_tf(2, "Thông hiểu", "Về cách dựng ảnh của một điểm sáng S qua gương phẳng:", [
            ("a", "Từ S hạ đường vuông góc SH xuống mặt gương, kéo dài lấy đoạn HS' = SH thì S' là ảnh của S.", True),
            ("b", "Từ S vẽ hai tia tới bất kì đến gương, vẽ hai tia phản xạ tương ứng.", True),
            ("c", "Đường kéo dài của hai tia phản xạ cắt nhau tại điểm ảnh ảo S' phía sau gương.", True),
            ("d", "Ảnh ảo S' được tạo bởi sự giao nhau trực tiếp của các tia phản xạ thực tế.", False)
        ], "Ảnh ảo S' là giao điểm của đường kéo dài các tia phản xạ, không phải tia phản xạ thực tế giao nhau."),
        make_tf(3, "Vận dụng", "Một người đứng trước gương phẳng treo thẳng đứng trên tường:", [
            ("a", "Khoảng cách ban đầu từ người đến gương là 1,2 m thì ảnh cách người 2,4 m.", True),
            ("b", "Người đó bước lùi xa gương thêm 0,4 m thì khoảng cách mới từ người đến gương là 1,6 m.", True),
            ("c", "Khoảng cách giữa người và ảnh lúc này là 3,2 m.", True),
            ("d", "Khoảng cách giữa người và ảnh đã tăng thêm 0,4 m so với ban đầu.", False)
        ], "Khoảng cách ban đầu là 2,4 m, sau đó là 3,2 m => tăng thêm 0,8 m (câu d ghi 0,4 m là sai)."),
        make_tf(4, "Vận dụng", "Ứng dụng gương phẳng trong thiết bị kính tiềm vọng (Periscope):", [
            ("a", "Gồm hai gương phẳng đặt song song và nghiêng góc 45 độ so với trục ống.", True),
            ("b", "Giúp người ngồi trong tàu ngầm quan sát các tàu bè trên mặt nước.", True),
            ("c", "Ảnh quan sát được qua kính tiềm vọng là ảnh cùng chiều với vật.", True),
            ("d", "Kính tiềm vọng phóng to kích thước của vật lên gấp 100 lần.", False)
        ], "Gương phẳng không có tác dụng phóng to kích thước vật như kính hiển vi.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Vật cách gương phẳng 40 cm. Ảnh của vật cách gương phẳng bao nhiêu cm?", "40", "40 cm."),
        make_sa(2, "Thông hiểu", "Ảnh tạo bởi gương phẳng là ảnh thật hay ảnh ảo?", "Ảnh ảo", "Ảnh ảo."),
        make_sa(3, "Vận dụng", "Một cây nến cao 15 cm đặt trước gương phẳng. Chiều cao của ảnh cây nến là bao nhiêu cm?", "15", "15 cm."),
        make_sa(4, "Vận dụng", "Một người đứng cách gương phẳng 1,8 m. Khoảng cách giữa người đó và ảnh của mình là bao nhiêu mét?", "3.6", "1,8 × 2 = 3,6 m."),
        make_sa(5, "Vận dụng cao", "Một vật cách gương phẳng 30 cm. Nếu dịch chuyển vật ra xa gương thêm 10 cm thì khoảng cách giữa vật và ảnh lúc này là bao nhiêu cm?", "80", "Khoảng cách mới d = 40 cm => 2d = 80 cm."),
        make_sa(6, "Vận dụng cao", "Để nhìn thấy toàn bộ cơ thể trong một chiếc gương phẳng treo thẳng đứng, chiều cao tối thiểu của tấm gương phải bằng bao nhiêu phần chiều cao cơ thể? (Viết dạng phân số tối giản)", "1/2", "Chiều cao tối thiểu bằng 1/2 chiều cao người.")
    ],
    "part4": [
        make_vdc(1, "Một người cao 1,7 mét đứng thẳng trước một chiếc gương phẳng treo thẳng đứng trên tường. Mắt người cách đỉnh đầu 10 cm (0,1 m). Để người đó có thể nhìn thấy trọn vẹn toàn bộ cơ thể mình từ đỉnh đầu đến gót chân trong gương thì chiều cao tối thiểu của tấm gương và mép dưới của gương cách mặt sàn tối đa bao nhiêu mét?", ["Gương cao tối thiểu 0,85 m và mép dưới cách sàn tối đa 0,80 m", "Gương cao 1,7 m và mép dưới chạm sàn", "Gương cao 0,9 m và mép dưới cách sàn 0,5 m", "Gương cao 1,0 m và mép dưới cách sàn 0,7 m"], 0, "Chiều cao gương tối thiểu = H / 2 = 1,7 / 2 = 0,85 m. Mép dưới cách sàn tối đa = (1,7 - 0,1) / 2 = 0,80 m."),
        make_vdc(2, "Một điểm sáng S đặt trước một chiếc gương phẳng nằm ngang. Nếu giữ nguyên điểm sáng S và dịch chuyển gương phẳng sang phải theo phương song song với mặt gương thì vị trí của ảnh ảo S' sẽ:", ["Không hề thay đổi vị trí trong không gian", "Dịch chuyển sang phải theo gương", "Dịch chuyển lên trên", "Biến mất"], 0, "Vì mặt phẳng gương không đổi vị trí (chỉ tịnh tiến song song trong mặt phẳng của nó) nên trục đối xứng không đổi, ảnh S' đứng yên."),
        make_vdc(3, "Một người đứng cách gương phẳng 1 mét, nhìn thấy ảnh của một chiếc đồng hồ treo tường ở bức tường phía sau lưng mình. Biết bức tường cách gương 4 mét. Khoảng cách từ mắt người đó đến ảnh của chiếc đồng hồ trong gương là:", ["5 mét", "4 mét", "3 mét", "6 mét"], 0, "Đồng hồ cách gương 4 m nên ảnh đồng hồ cách gương 4 m. Người cách gương 1 m (ở cùng phía với đồng hồ) => Khoảng cách từ mắt người đến ảnh = 1 + 4 = 5 m."),
        make_vdc(4, "Một chú mèo con đứng trước một chiếc gương phẳng. Khi chú mèo bước lại gần gương với tốc độ 0,2 m/s theo phương vuông góc với gương thì ảnh của chú mèo tiến lại gần chú mèo với tốc độ tương đối là bao nhiêu?", ["0,4 m/s", "0,2 m/s", "0,1 m/s", "0,8 m/s"], 0, "Mèo tiến lại gần gương 0,2 m/s thì ảnh cũng tiến lại gương 0,2 m/s => Tốc độ tương đối giữa mèo và ảnh = 0,2 + 0,2 = 0,4 m/s.")
    ]
}

# --- ĐỀ 2 ---
b17_exams["phys7_c5_b17_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 17: Ảnh của một vật tạo bởi gương phẳng - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b17", "lessonName": "Bài 17: Ảnh của một vật tạo bởi gương phẳng",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Ảnh của một vật tạo bởi gương phẳng không hứng được trên màn chắn vì:", ["Đó là ảnh ảo được tạo bởi đường kéo dài của các tia sáng phản xạ", "Ảnh quá nhỏ", "Ảnh quá mờ", "Gương hút hết ánh sáng"], 0, "Ảnh ảo là giao điểm của các đường kéo dài tia phản xạ, không có ánh sáng thực hội tụ nên không hứng được trên màn."),
        make_mc(2, "Nhận biết", "Nếu đặt một cây bút chì dài 12 cm trước gương phẳng thì chiều dài ảnh của cây bút chì là:", ["12 cm", "6 cm", "24 cm", "18 cm"], 0, "Độ lớn của ảnh luôn bằng độ lớn của vật (12 cm)."),
        make_mc(3, "Nhận biết", "Đoạn thẳng nối một điểm của vật với ảnh tương ứng của nó qua gương phẳng luôn:", ["Vuông góc với mặt gương và bị mặt gương chia đôi", "Song song với mặt gương", "Hợp với mặt gương góc 45 độ", "Nằm trên mặt gương"], 0, "Tính chất đối xứng qua mặt phẳng gương: đoạn nối vuông góc với gương tại trung điểm."),
        make_mc(4, "Nhận biết", "Khi soi gương phẳng, ảnh của mắt phải của một người sẽ là:", ["Mắt trái của ảnh người đó đối diện trong gương", "Mắt phải của ảnh", "Cả hai mắt", "Mũi"], 0, "Tính chất đối xứng đảo trục trái phải."),
        make_mc(5, "Nhận biết", "Khi tiến lại gần gương phẳng thì góc trông ảnh của mắt người quan sát sẽ:", ["Tăng lên nên cảm thấy ảnh to hơn dù kích thước thật của ảnh không đổi", "Giảm đi", "Không đổi", "Biến mất"], 0, "Lại gần gương góc trông tăng lên làm ta có cảm giác ảnh to hơn."),
        make_mc(6, "Nhận biết", "Ứng dụng nào sau đây KHÔNG sử dụng gương phẳng?", ["Kính lúp phóng to con kiến", "Gương soi trang điểm", "Kính tiềm vọng tàu ngầm", "Kính vạn hoa"], 0, "Kính lúp là thấu kính hội tụ, không dùng gương phẳng."),
        make_mc(7, "Thông hiểu", "Một điểm sáng S cách mặt phẳng gương 35 cm. Ảnh S' của nó cách điểm sáng S một khoảng là:", ["70 cm", "35 cm", "17,5 cm", "0 cm"], 0, "Khoảng cách SS' = 2d = 2 × 35 = 70 cm."),
        make_mc(8, "Thông hiểu", "Một vật đặt cách gương phẳng một đoạn d. Nếu dịch chuyển vật lại gần gương thêm 15 cm thì khoảng cách giữa vật và ảnh sẽ giảm đi:", ["30 cm", "15 cm", "7,5 cm", "45 cm"], 0, "Vật lại gần 15 cm, ảnh lại gần 15 cm => khoảng cách vật và ảnh giảm 30 cm."),
        make_mc(9, "Thông hiểu", "Một người đứng trước gương phẳng nhìn thấy ảnh của mình cách mình 3 mét. Khoảng cách từ người đó đến gương phẳng là:", ["1,5 mét", "3,0 mét", "0,75 mét", "6,0 mét"], 0, "d = 3 / 2 = 1,5 mét."),
        make_mc(10, "Thông hiểu", "Đặt một tấm bìa hình chữ cái 'L' trước một chiếc gương phẳng. Hình ảnh của tấm bìa trong gương có dạng giống chữ cái nào?", ["Hình chữ L bị lật ngược trái phải (⅃)", "Chữ L xuôi", "Chữ T", "Chữ I"], 0, "Ảnh qua gương phẳng bị đảo trục trái - phải đối xứng."),
        make_mc(11, "Thông hiểu", "Thị trường (vùng quan sát) của một chiếc gương phẳng sẽ mở rộng hơn khi:", ["Người quan sát tiến lại gần gương hơn hoặc kích thước gương lớn hơn", "Người lùi xa gương", "Gương nhỏ đi", "Tắt bớt đèn"], 0, "Lại gần gương hoặc dùng gương lớn hơn làm mở rộng vùng quan sát."),
        make_mc(12, "Thông hiểu", "Khi đứng bên bờ hồ nước phẳng lặng trong công viên vào ngày nắng, ta nhìn thấy hình ảnh ngọn tháp lộn ngược dưới mặt nước. Mặt nước đóng vai trò như:", ["Một chiếc gương phẳng nằm ngang", "Một thấu kính phân kì", "Một tấm màn chắn", "Một nguồn sáng"], 0, "Mặt nước phẳng lặng hoạt động như một gương phẳng nằm ngang tạo ảnh đối xứng qua mặt nước.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất ảnh của vật tạo bởi gương phẳng:", [
            ("a", "Tia sáng từ vật chiếu đến gương phản xạ vào mắt người quan sát.", True),
            ("b", "Mắt nhìn thấy ảnh ảo vì các tia phản xạ đi vào mắt có đường kéo dài đi qua ảnh ảo.", True),
            ("c", "Nếu đặt một tấm bìa chắn phía sau gương tại vị trí của ảnh thì ảnh sẽ bị che khuất mất.", False),
            ("d", "Ảnh ảo không thể chụp được bằng máy ảnh thông thường.", False)
        ], "Máy ảnh đóng vai trò như mắt người, thu nhận chùm tia phản xạ nên hoàn toàn chụp được ảnh ảo trong gương."),
        make_tf(2, "Thông hiểu", "Về tính chất khoảng cách và kích thước qua gương phẳng:", [
            ("a", "Vật cao 1 m thì ảnh trong gương phẳng cũng cao đúng 1 m.", True),
            ("b", "Nếu vật chuyển động với tốc độ 1 m/s vuông góc với gương thì ảnh cũng chuyển động với tốc độ 1 m/s đối với gương.", True),
            ("c", "Khoảng cách giữa vật và ảnh luôn gấp đôi khoảng cách từ vật đến gương.", True),
            ("d", "Nếu nghiêng gương một góc thì kích thước của ảnh sẽ bị co ngắn lại.", False)
        ], "Gương phẳng luôn cho ảnh có kích thước bằng kích thước thật của vật, không bị co giãn."),
        make_tf(3, "Vận dụng", "Một ngọn hải đăng cao 25 m xây dựng sát mép biển phẳng lặng:", [
            ("a", "Mặt nước biển phẳng lặng phản chiếu ngọn hải đăng như một gương phẳng nằm ngang.", True),
            ("b", "Ảnh của đỉnh ngọn hải đăng nằm ở vị trí đối xứng qua mặt nước.", True),
            ("c", "Khoảng cách từ đỉnh ngọn hải đăng đến ảnh của nó dưới mặt nước là 50 m.", True),
            ("d", "Ảnh của ngọn hải đăng dưới mặt nước là ảnh thật hứng được trên đáy biển.", False)
        ], "Ảnh dưới mặt nước là ảnh ảo tạo bởi phản xạ của mặt nước."),
        make_tf(4, "Vận dụng", "Khảo sát chuyển động của vật và ảnh qua gương phẳng:", [
            ("a", "Khi người đứng yên, gương dịch chuyển ra xa người 1 m thì ảnh dịch chuyển ra xa người 2 m.", True),
            ("b", "Khi gương đứng yên, người dịch lại gần gương 0,5 m thì khoảng cách giữa người và ảnh giảm đi 1,0 m.", True),
            ("c", "Người giơ tay trái lên thì ảnh trong gương giơ tay phải đối diện.", True),
            ("d", "Nếu nhắm mắt lại thì ảnh trong gương vẫn tiếp tục mở mắt nhìn.", False)
        ], "Ảnh đối xứng chính xác mọi trạng thái biểu cảm cử động của vật tại cùng thời điểm.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Vật cách gương phẳng 25 cm. Khoảng cách từ ảnh đến gương phẳng là bao nhiêu cm?", "25", "25 cm."),
        make_sa(2, "Thông hiểu", "Một chiếc hộp cao 10 cm. Độ cao của ảnh chiếc hộp trong gương phẳng là bao nhiêu cm?", "10", "10 cm."),
        make_sa(3, "Vận dụng", "Khoảng cách giữa người và ảnh của mình trong gương phẳng là 2,4 m. Người cách gương phẳng bao nhiêu mét?", "1.2", "d = 2,4 / 2 = 1,2 m."),
        make_sa(4, "Vận dụng", "Một vật cách gương phẳng 60 cm. Nếu dịch gương lại gần vật 10 cm thì khoảng cách mới giữa vật và ảnh là bao nhiêu cm?", "100", "d mới = 50 cm => 2d = 100 cm."),
        make_sa(5, "Vận dụng cao", "Một người lùi xa gương phẳng với tốc độ 0,5 m/s. Ảnh của người đó dịch chuyển ra xa người đó với tốc độ tương đối là bao nhiêu m/s?", "1", "0,5 × 2 = 1,0 m/s."),
        make_sa(6, "Vận dụng cao", "Hai gương phẳng vuông góc với nhau tạo thành bao nhiêu ảnh ảo của một điểm sáng S đặt giữa hai gương?", "3", "n = 360 / 90 - 1 = 4 - 1 = 3 ảnh.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng trước một chiếc gương phẳng treo thẳng đứng trên tường. Người đó nhận thấy có thể nhìn thấy ảnh của đầu và chân mình trong gương. Nếu người này bước lùi xa gương thêm 2 mét thì chiều cao phần gương tối thiểu để người đó nhìn thấy toàn bộ cơ thể mình sẽ:", ["Không đổi (vẫn bằng một nửa chiều cao người đó)", "Tăng lên gấp đôi", "Giảm đi một nửa", "Tăng lên 2 mét"], 0, "Chiều cao tối thiểu của gương để nhìn thấy toàn thân luôn bằng H/2, hoàn toàn không phụ thuộc vào khoảng cách từ người đến gương."),
        make_vdc(2, "Một căn phòng có trần nhà cao 3,2 mét. Người ta gắn một chiếc gương phẳng tròn trên trần nhà. Trên sàn nhà ngay dưới gương đặt một ngọn nến cao 20 cm. Khoảng cách từ ngọn lửa của cây nến đến ảnh của ngọn lửa trong chiếc gương trên trần nhà là:", ["6,0 mét", "6,4 mét", "3,0 mét", "3,2 mét"], 0, "Khoảng cách từ ngọn lửa đến gương trần: 3,2 - 0,2 = 3,0 m => Khoảng cách giữa ngọn lửa và ảnh: 2 × 3,0 = 6,0 m."),
        make_vdc(3, "Một diễn viên xiếc đứng thăng bằng trên một tấm ván gỗ trước một chiếc gương phẳng lớn. Diễn viên giơ một chiếc gậy dài 1,5 mét theo phương song song với mặt gương. Chiều dài ảnh của chiếc gậy trong gương và phương của ảnh chiếc gậy là:", ["Dài 1,5 mét và song song với chiếc gậy", "Dài 3,0 mét và vuông góc", "Dài 0,75 mét và nghiêng", "Dài 1,5 mét và vuông góc"], 0, "Ảnh bằng vật (1,5 m) và song song với vật do vật đặt song song với mặt phẳng gương."),
        make_vdc(4, "Một người lái xe ô tô quan sát qua gương phẳng chiếu hậu nhìn thấy một chiếc xe tải bám theo sau. Nếu xe tải đang chạy với tốc độ 60 km/h đuổi theo xe ô tô đang chạy với tốc độ 50 km/h thì qua gương chiếu hậu, tài xế ô tô sẽ thấy ảnh của chiếc xe tải đang tiến lại gần mình với tốc độ tương đối là:", ["10 km/h", "20 km/h", "110 km/h", "5 km/h"], 0, "Tốc độ tương đối của xe tải so với ô tô là 60 - 50 = 10 km/h, nên ảnh xe tải qua gương tiến lại gần xe ô tô với tốc độ đúng bằng 10 km/h.")
    ]
}

# --- ĐỀ 3 ---
b17_exams["phys7_c5_b17_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 17: Ảnh của một vật tạo bởi gương phẳng - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b17", "lessonName": "Bài 17: Ảnh của một vật tạo bởi gương phẳng",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Ảnh của một vật tạo bởi gương phẳng là:", ["Ảnh ảo có kích thước bằng vật", "Ảnh thật có kích thước lớn hơn vật", "Ảnh thật có kích thước nhỏ hơn vật", "Ảnh ảo có kích thước gấp đôi vật"], 0, "Ảnh ảo, độ lớn bằng vật."),
        make_mc(2, "Nhận biết", "Nếu vật đặt cách gương phẳng 1 m thì ảnh của vật nằm ở vị trí nào sau gương?", ["Ở phía sau gương cách gương 1 m", "Ở ngay trên mặt gương", "Ở trước gương 1 m", "Ở sau gương 2 m"], 0, "Ảnh ảo nằm sau gương, cách gương đúng 1 m."),
        make_mc(3, "Nhận biết", "Mặt gương phẳng chia đôi đoạn thẳng nối:", ["Mỗi điểm của vật với ảnh tương ứng của nó", "Tia tới và tia phản xạ", "Đỉnh đầu và ngón chân", "Mặt trời và mặt trăng"], 0, "Mặt phẳng gương là mặt phẳng trung trực của đoạn thẳng nối vật và ảnh."),
        make_mc(4, "Nhận biết", "Dụng cụ quang học nào sau đây ứng dụng tính chất của gương phẳng để tạo ra các hoa văn đối xứng tuyệt đẹp khi xoay tròn?", ["Kính vạn hoa", "Kính thiên văn", "Kính hiển vi", "Kính râm"], 0, "Kính vạn hoa ghép các gương phẳng tạo ảnh đối xứng."),
        make_mc(5, "Nhận biết", "Khi nhìn vào gương phẳng, ta thấy ảnh của mình chuyển động:", ["Cùng tốc độ nhưng ngược chiều chuyển động của ta đối với gương", "Nhanh gấp đôi ta", "Chậm hơn ta", "Không chuyển động"], 0, "Ta tiến lại gần gương thì ảnh cũng tiến lại gần gương với cùng tốc độ đối với gương."),
        make_mc(6, "Nhận biết", "Kính tiềm vọng trang bị trên tàu ngầm dùng để:", ["Quan sát quang cảnh và chướng ngại vật trên mặt nước khi tàu ngầm đang lặn", "Đo độ sâu biển", "Bắn ngư lôi", "Chiếu sáng đáy biển"], 0, "Quan sát trên mặt nước khi tàu đang lặn ngầm."),
        make_mc(7, "Thông hiểu", "Một bạn học sinh đứng cách gương phẳng 1,5 mét. Khoảng cách từ bạn học sinh đến ảnh của bạn là:", ["3,0 mét", "1,5 mét", "0,75 mét", "4,5 mét"], 0, "2d = 2 × 1,5 = 3,0 m."),
        make_mc(8, "Thông hiểu", "Một ngọn nến đặt cách gương phẳng 10 cm. Nếu kéo ngọn nến lùi xa gương thêm 5 cm thì khoảng cách giữa ngọn nến và ảnh lúc này là:", ["30 cm", "20 cm", "25 cm", "15 cm"], 0, "d mới = 10 + 5 = 15 cm => 2d = 30 cm."),
        make_mc(9, "Thông hiểu", "Một chiếc đồng hồ kim treo tường đối diện một gương phẳng đang chỉ 9 giờ đúng. Khi nhìn vào ảnh của chiếc đồng hồ trong gương, ta có cảm giác đồng hồ đang chỉ mấy giờ?", ["3 giờ đúng", "9 giờ đúng", "6 giờ đúng", "12 giờ đúng"], 0, "Tính chất đảo trái phải của gương phẳng: kim giờ chỉ số 9 đối xứng thành số 3."),
        make_mc(10, "Thông hiểu", "Một vật AB đặt song song với gương phẳng cách gương 20 cm. Ảnh A'B' của vật sẽ:", ["Song song với AB và cách AB một khoảng 40 cm", "Vuông góc với AB", "Cắt AB", "Trùng với AB"], 0, "Vật song song với gương thì ảnh song song với vật và cách vật 2d = 40 cm."),
        make_mc(11, "Thông hiểu", "Nếu ta bước lại gần gương phẳng một đoạn 30 cm thì khoảng cách giữa ta và ảnh của mình trong gương sẽ:", ["Giảm đi 60 cm", "Giảm đi 30 cm", "Tăng lên 30 cm", "Không đổi"], 0, "Khoảng cách giảm: 2 × 30 = 60 cm."),
        make_mc(12, "Thông hiểu", "Một người nhìn thấy ảnh của ngọn đèn đường dưới một vũng nước mưa phẳng lặng trên sân. Điểm ảnh ảo của ngọn đèn nằm ở đâu?", ["Ở dưới mặt đất (phía dưới đáy vũng nước một khoảng bằng độ cao ngọn đèn)", "Ở ngay trên mặt vũng nước", "Ở trên ngọn đèn", "Ở trong mắt người"], 0, "Ảnh ảo đối xứng qua mặt phẳng nước, nằm sâu phía dưới mặt nước một khoảng bằng độ cao ngọn đèn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc điểm cơ bản của ảnh ảo qua gương phẳng:", [
            ("a", "Ảnh ảo không thể in hình lên một tấm bìa hay màn chắn đặt sau gương.", True),
            ("b", "Ảnh ảo cùng chiều với vật nhưng bị đảo ngược hướng trái - phải.", True),
            ("c", "Độ lớn của ảnh luôn phụ thuộc vào chất lượng tráng bạc của gương phẳng.", False),
            ("d", "Vật và ảnh có cùng kích thước hình học 100%.", True)
        ], "Chất lượng tráng bạc chỉ quyết định độ sáng rõ của ảnh, không quyết định kích thước ảnh."),
        make_tf(2, "Thông hiểu", "Về thị trường (vùng quan sát) của gương phẳng:", [
            ("a", "Thị trường của gương là vùng không gian phía trước gương mà mắt nhìn thấy ảnh của các vật trong đó.", True),
            ("b", "Kích thước gương càng lớn thì thị trường quan sát càng rộng.", True),
            ("c", "Mắt càng đặt gần gương thì vùng quan sát được qua gương càng rộng.", True),
            ("d", "Dịch chuyển mắt ra xa gương thì vùng quan sát qua gương mở rộng hơn.", False)
        ], "Mắt ra xa gương thì góc trông gương thu hẹp lại, vùng quan sát bị thu nhỏ."),
        make_tf(3, "Vận dụng", "Khảo sát một biển báo chữ 'STOP' đặt đối diện một chiếc gương phẳng lớn:", [
            ("a", "Chữ cái đầu tiên gần mép gương nhất cho ảnh gần gương nhất.", True),
            ("b", "Thứ tự các chữ cái trong ảnh nhìn từ trái sang phải bị đảo ngược lại.", True),
            ("c", "Chữ 'O' và chữ 'T' có tính chất đối xứng trục nên ảnh của chúng không bị biến dạng hình dạng.", True),
            ("d", "Chữ 'S' và chữ 'P' trong ảnh sẽ hoàn toàn giống hệt chữ xuôi ban đầu.", False)
        ], "Chữ 'S' và chữ 'P' không có trục đối xứng dọc nên ảnh bị đảo ngược trái phải rõ rệt."),
        make_tf(4, "Vận dụng", "Một chú chim bói cá bay là là trên mặt hồ nước phẳng lặng ở độ cao 1,5 m:", [
            ("a", "Ảnh của chú chim bói cá nằm dưới mặt nước cách mặt nước 1,5 m.", True),
            ("b", "Khoảng cách giữa chú chim và ảnh của nó là 3,0 m.", True),
            ("c", "Nếu chú chim sà xuống độ cao 0,5 m thì khoảng cách giữa chú chim và ảnh là 1,0 m.", True),
            ("d", "Khi chú chim chạm sát mặt nước thì ảnh của chú chim biến mất.", False)
        ], "Khi chạm mặt nước d = 0 thì ảnh trùng khít với vật ngay tại mặt nước.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Vật cách gương phẳng 15 cm. Ảnh của vật cách gương phẳng bao nhiêu cm?", "15", "15 cm."),
        make_sa(2, "Thông hiểu", "Một thanh sắt dài 50 cm. Ảnh của thanh sắt trong gương phẳng dài bao nhiêu cm?", "50", "50 cm."),
        make_sa(3, "Vận dụng", "Khoảng cách giữa vật và ảnh qua gương phẳng là 80 cm. Vật cách gương bao nhiêu cm?", "40", "d = 80 / 2 = 40 cm."),
        make_sa(4, "Vận dụng", "Vật cách gương phẳng 20 cm. Dịch chuyển vật ra xa thêm 15 cm thì khoảng cách vật - ảnh mới là bao nhiêu cm?", "70", "d mới = 35 cm => 2d = 70 cm."),
        make_sa(5, "Vận dụng cao", "Một người tiến lại gần gương phẳng với tốc độ 1,2 m/s. Ảnh của người đó tiến lại gần người đó với tốc độ bao nhiêu m/s?", "2.4", "1,2 × 2 = 2,4 m/s."),
        make_sa(6, "Vận dụng cao", "Một chiếc gương phẳng treo thẳng đứng. Người cao 1,6 m cần một chiếc gương cao tối thiểu bao nhiêu mét để nhìn thấy toàn thân?", "0.8", "H / 2 = 1,6 / 2 = 0,8 m.")
    ],
    "part4": [
        make_vdc(1, "Một người đứng cách một bức tường có gắn một chiếc gương phẳng một khoảng 2 mét. Phía sau lưng người đó cách người đó 3 mét có một bức tranh phong cảnh treo trên tường đối diện. Người đó nhìn vào gương thì thấy ảnh của bức tranh. Khoảng cách từ mắt người đó đến ảnh của bức tranh trong gương là:", ["7 mét", "5 mét", "8 mét", "4 mét"], 0, "Bức tranh cách gương: 2 + 3 = 5 mét => Ảnh bức tranh cách gương 5 mét. Mắt người cách gương 2 mét (ở giữa tranh và gương) => Khoảng cách từ mắt đến ảnh = 2 + 5 = 7 mét."),
        make_vdc(2, "Một điểm sáng S đặt trước gương phẳng cách gương 20 cm. Nếu cho gương phẳng quay một góc 30 độ quanh trục đi qua điểm tới thì quỹ đạo chuyển động của ảnh ảo S' sẽ là:", ["Một cung tròn tâm tại trục quay bán kính 20 cm", "Một đường thẳng", "Một đường parabol", "Một hình elip"], 0, "Khoảng cách từ ảnh S' đến trục quay trên mặt phẳng gương luôn không đổi nên quỹ đạo là một cung tròn."),
        make_vdc(3, "Để đo chiều cao của một cột đèn chiếu sáng công cộng mà không cần trèo lên cột, một học sinh đặt một chiếc gương phẳng nhỏ nằm ngửa trên mặt đất tại điểm C cách chân cột đèn 6 mét. Học sinh lùi lại vị trí cách gương 1,5 mét và đứng thẳng thì nhìn thấy ảnh của đỉnh ngọn đèn trong gương. Biết mắt học sinh cách mặt đất 1,4 mét. Chiều cao của cột đèn là:", ["5,6 mét", "4,2 mét", "6,0 mét", "7,0 mét"], 0, "Theo định luật phản xạ ánh sáng (tam giác đồng dạng): H / 6 = 1,4 / 1,5 => H = 1,4 × 6 / 1,5 = 5,6 mét."),
        make_vdc(4, "Một người đứng trước gương phẳng treo trên tường và nhìn thấy toàn thân. Nếu người đó đội thêm một chiếc mũ rộng vành cao 10 cm trên đầu thì để nhìn thấy toàn bộ từ chóp mũ đến gót chân, chiều cao tối thiểu của tấm gương cần phải tăng thêm ít nhất bao nhiêu cm?", ["5 cm", "10 cm", "20 cm", "Không cần tăng"], 0, "Chiều cao tối thiểu của gương tăng thêm ΔH / 2 = 10 / 2 = 5 cm.")
    ]
}
