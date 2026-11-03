# -*- coding: utf-8 -*-
"""
CHƯƠNG V: ÁNH SÁNG - BÀI 15 & BÀI 16 (6 ĐỀ ĐỘC LẬP 100%)
- phys7_c5_b15: Bài 15: Ánh sáng, tia sáng (3 đề: test1, test2, test3)
- phys7_c5_b16: Bài 16: Sự phản xạ ánh sáng (3 đề: test1, test2, test3)
Không trùng lặp, không tiền tố "Đề X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

b15_b16_exams = {}

# =========================================================================
# BÀI 15: ÁNH SÁNG, TIA SÁNG (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b15_b15_exams = b15_b16_exams

b15_b16_exams["phys7_c5_b15_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 15: Ánh sáng, tia sáng - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b15", "lessonName": "Bài 15: Ánh sáng, tia sáng",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Ta nhận biết được ánh sáng khi:", ["Có ánh sáng truyền vào mắt ta", "Mắt ta mở to trong bóng tối", "Vật được chiếu sáng", "Xung quanh có nguồn điện"], 0, "Mắt nhận biết ánh sáng khi có ánh sáng lọt vào mắt."),
        make_mc(2, "Nhận biết", "Ta nhìn thấy một vật khi:", ["Có ánh sáng từ vật đó truyền vào mắt ta", "Vật đó có kích thước rất lớn", "Vật đó phát ra ánh sáng", "Mắt ta phát ra tia sáng chiếu đến vật"], 0, "Điều kiện nhìn thấy vật là có ánh sáng từ vật truyền tới mắt."),
        make_mc(3, "Nhận biết", "Nguồn sáng là vật:", ["Tự nó phát ra ánh sáng", "Hắt lại ánh sáng chiếu vào nó", "Có màu sắc rực rỡ", "Trong suốt"], 0, "Nguồn sáng là vật tự phát ra ánh sáng."),
        make_mc(4, "Nhận biết", "Vật nào sau đây là nguồn sáng?", ["Ngọn nến đang cháy sáng", "Mặt Trăng trong đêm rằm", "Tấm gương soi", "Quyển sách trên bàn"], 0, "Ngọn nến đang cháy tự phát sáng; Mặt Trăng hắt lại ánh sáng Mặt Trời."),
        make_mc(5, "Nhận biết", "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường nào?", ["Đường thẳng", "Đường cong parabol", "Đường gấp khúc", "Đường tròn"], 0, "Định luật truyền thẳng ánh sáng."),
        make_mc(6, "Nhận biết", "Quy ước biểu diễn đường truyền của ánh sáng bằng một đường thẳng có mũi tên chỉ hướng truyền được gọi là:", ["Tia sáng", "Chùm sáng", "Pháp tuyến", "Vùng tối"], 0, "Tia sáng được biểu diễn bằng đường thẳng có mũi tên chỉ hướng."),
        make_mc(7, "Thông hiểu", "Vật nào sau đây là vật sáng nhưng KHÔNG PHẢI là nguồn sáng?", ["Mặt Trăng", "Mặt Trời", "Ngọn đuốc đang cháy", "Đèn LED đang sáng"], 0, "Mặt Trăng là vật sáng vì hắt lại ánh sáng Mặt Trời, không tự phát sáng."),
        make_mc(8, "Thông hiểu", "Chùm sáng gồm các tia sáng song song với nhau trên đường truyền được gọi là:", ["Chùm sáng song song", "Chùm sáng hội tụ", "Chùm sáng phân kì", "Chùm sáng cầu"], 0, "Chùm sáng song song."),
        make_mc(9, "Thông hiểu", "Vùng phía sau vật cản hoàn toàn không nhận được ánh sáng từ nguồn sáng truyền tới được gọi là:", ["Vùng bóng tối", "Vùng bóng nửa tối", "Vùng sáng", "Vùng chạng vạng"], 0, "Vùng bóng tối không nhận được bất kì ánh sáng nào từ nguồn sáng."),
        make_mc(10, "Thông hiểu", "Hiện tượng Nhật thực xảy ra khi:", ["Mặt Trăng nằm ở khoảng giữa Mặt Trời và Trái Đất", "Trái Đất nằm ở giữa Mặt Trời và Mặt Trăng", "Mặt Trời nằm giữa Trái Đất và Mặt Trăng", "Vào ban đêm trăng tròn"], 0, "Nhật thực xảy ra khi Mặt Trăng che khuất Mặt Trời chiếu xuống Trái Đất."),
        make_mc(11, "Thông hiểu", "Chùm sáng phát ra từ một chiếc đèn pin chiếu xa có dạng là:", ["Chùm sáng phân kì loe rộng dần ra", "Chùm sáng song song tuyệt đối", "Chùm sáng hội tụ về một điểm", "Chùm sáng zích zắc"], 0, "Chùm sáng đèn pin loe rộng ra là chùm phân kì."),
        make_mc(12, "Thông hiểu", "Hiện tượng Nguyệt thực xảy ra khi:", ["Trái Đất nằm ở khoảng giữa Mặt Trời và Mặt Trăng", "Mặt Trăng nằm giữa Mặt Trời và Trái Đất", "Mặt Trời bị mây che", "Vào ban ngày"], 0, "Trái Đất che khuất ánh sáng Mặt Trời chiếu đến Mặt Trăng tạo ra nguyệt thực.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về điều kiện nhìn thấy vật và bản chất của nguồn sáng:", [
            ("a", "Ban đêm trong phòng kín tối đen, ta không nhìn thấy đồ vật vì không có ánh sáng từ vật truyền vào mắt.", True),
            ("b", "Bật đèn sáng lên, đèn chiếu sáng đồ vật và đồ vật hắt ánh sáng vào mắt giúp ta nhìn thấy vật.", True),
            ("c", "Mắt người có khả năng tự phát ra ánh sáng chiếu sáng các vật xung quanh.", False),
            ("d", "Vật sáng bao gồm cả nguồn sáng và các vật hắt lại ánh sáng.", True)
        ], "Mắt người là thụ cảm quang học, không tự phát ra ánh sáng."),
        make_tf(2, "Thông hiểu", "Về định luật truyền thẳng ánh sáng và các hệ quả:", [
            ("a", "Ánh sáng chỉ truyền theo đường thẳng khi môi trường trong suốt và đồng tính.", True),
            ("b", "Trong môi trường không khí bị khói bụi hoặc nước có váng dầu không đồng nhất, ánh sáng có thể bị bẻ cong.", True),
            ("c", "Người thợ xây ngắm đường thẳng bằng cách dùng mắt ngắm thẳng hàng là ứng dụng định luật truyền thẳng ánh sáng.", True),
            ("d", "Bóng tối của vật cản được hình thành là do ánh sáng có thể tự uốn cong vòng qua vật cản.", False)
        ], "Bóng tối hình thành do ánh sáng truyền thẳng, bị vật cản chặn lại không truyền qua được."),
        make_tf(3, "Vận dụng", "Thí nghiệm dùng đèn pin nhỏ (nguồn sáng hẹp) chiếu vào một quả bóng bàn đặt trước một màn chắn:", [
            ("a", "Phía sau quả bóng bàn trên màn chắn xuất hiện một vùng tròn bóng tối rõ nét.", True),
            ("b", "Xung quanh vùng bóng tối này không có vùng bóng nửa tối khi dùng nguồn sáng điểm nhỏ.", True),
            ("c", "Nếu dịch chuyển quả bóng bàn lại gần màn chắn hơn thì kích thước bóng tối trên màn sẽ thu nhỏ lại.", True),
            ("d", "Nếu thay quả bóng bàn bằng một tấm kính thủy tinh trong suốt thì bóng tối trên màn vẫn đậm đặc như cũ.", False)
        ], "Kính thủy tinh trong suốt cho ánh sáng truyền qua nên không tạo bóng tối đậm đặc."),
        make_tf(4, "Vận dụng", "Hiện tượng Nhật thực và Nguyệt thực trong thiên văn học:", [
            ("a", "Nhật thực chỉ có thể xảy ra vào ban ngày khi có trăng mới (đầu tháng âm lịch).", True),
            ("b", "Nguyệt thực chỉ có thể xảy ra vào ban đêm khi trăng tròn (ngày rằm âm lịch).", True),
            ("c", "Người đứng ở vùng bóng tối của Mặt Trăng trên Trái Đất sẽ quan sát được Nhật thực toàn phần.", True),
            ("d", "Hiện tượng Nhật thực chứng tỏ ánh sáng truyền đi theo đường cong xoắn ốc.", False)
        ], "Nhật thực là minh chứng thực tế rõ nét cho định luật truyền thẳng ánh sáng.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Mặt Trời là nguồn sáng hay vật được chiếu sáng?", "Nguồn sáng", "Mặt Trời tự phát sáng."),
        make_sa(2, "Thông hiểu", "Mặt Trăng là nguồn sáng hay vật sáng?", "Vật sáng", "Mặt Trăng là vật sáng (hắt lại ánh sáng)."),
        make_sa(3, "Vận dụng", "Trong môi trường trong suốt và đồng tính, ánh sáng truyền theo đường gì?", "Đường thẳng", "Đường thẳng."),
        make_sa(4, "Vận dụng", "Chùm sáng có các tia sáng xuất phát từ cùng một điểm và loe rộng ra gọi là chùm sáng gì?", "Phân kì", "Chùm sáng phân kì."),
        make_sa(5, "Vận dụng cao", "Tốc độ truyền ánh sáng trong chân không là bao nhiêu nghìn km/s?", "300", "300.000 km/s = 300 nghìn km/s."),
        make_sa(6, "Vận dụng cao", "Hiện tượng Mặt Trăng nằm giữa Mặt Trời và Trái Đất tạo ra hiện tượng gì? (Nhật thực hay Nguyệt thực)", "Nhật thực", "Nhật thực.")
    ],
    "part4": [
        make_vdc(1, "Để kiểm tra xem một hàng cọc rào có được cắm thẳng hàng trên bãi đất hay không, một người thợ ngắm bằng mắt dọc theo hàng cọc. Nếu người đó nhìn cọc thứ nhất mà cọc này che khuất hoàn toàn cọc thứ hai và cọc thứ ba thì kết luận nào sau đây đúng?", ["Ba cọc rào đã được cắm thẳng hàng vì ánh sáng truyền thẳng từ các cọc sau bị cọc trước chắn lại", "Hàng cọc bị cong", "Cọc thứ nhất ngắn hơn", "Không thể kết luận được"], 0, "Ứng dụng định luật truyền thẳng ánh sáng: các cọc che khuất nhau nghĩa là chúng thẳng hàng."),
        make_vdc(2, "Tại sao khi làm phẫu thuật trong phòng mổ, người ta không sử dụng bóng đèn tròn thông thường mà lại sử dụng hệ thống đèn mổ gồm nhiều bóng đèn nhỏ bố trí xung quanh một vành tròn lớn?", ["Để tạo ra chùm sáng rộng triệt tiêu vùng bóng tối dưới bàn tay và dụng cụ của bác sĩ phẫu thuật (đèn không hắt bóng)", "Để phòng mổ thật nóng", "Để tiết kiệm điện", "Để trang trí thẩm mỹ"], 0, "Đèn mổ không bóng tạo ra nhiều nguồn sáng rộng khiến vùng bóng tối dưới tay bác sĩ bị triệt tiêu hoàn toàn thành bóng nửa tối mờ nhạt."),
        make_vdc(3, "Một cột cờ cao 6 mét dựng thẳng đứng trên mặt sân phẳng. Vào một thời điểm trời nắng, bóng của cột cờ in trên mặt sân có chiều dài 8 mét. Cùng lúc đó, một chiếc cọc sắt dựng thẳng đứng có bóng in trên sân dài 2 mét. Chiều cao của chiếc cọc sắt đó là:", ["1,5 mét", "2,0 mét", "3,0 mét", "1,2 mét"], 0, "Tỉ lệ chiều cao / chiều dài bóng: h_cờ / s_cờ = 6 / 8 = 0,75 => h_cọc = 2 × 0,75 = 1,5 m."),
        make_vdc(4, "Một người đứng dưới ánh sáng của một cột đèn đường cao vào ban đêm. Khi người này bước đi ra xa dần khỏi cột đèn thì chiều dài bóng của người đó trên mặt đất sẽ:", ["Dài dần ra", "Ngắn dần lại", "Không đổi", "Biến mất hoàn toàn"], 0, "Khi ra xa chân đèn, góc tới của tia sáng giới hạn tạo bóng phẳng hơn, làm chiều dài bóng trên mặt đất dài ra.")
    ]
}

# --- ĐỀ 2 ---
b15_b16_exams["phys7_c5_b15_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 15: Ánh sáng, tia sáng - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b15", "lessonName": "Bài 15: Ánh sáng, tia sáng",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật nào dưới đây được coi là nguồn sáng tự nhiên?", ["Mặt Trời", "Đèn pin", "Bóng đèn huỳnh quang", "Màn hình tivi"], 0, "Mặt Trời là nguồn sáng tự nhiên vô tận."),
        make_mc(2, "Nhận biết", "Con người nhận biết được ánh sáng nhờ cơ quan thụ cảm nào?", ["Mắt (thị giác)", "Tai (thính giác)", "Mũi (khứu giác)", "Da (xúc giác)"], 0, "Mắt là cơ quan thụ cảm ánh sáng."),
        make_mc(3, "Nhận biết", "Chùm sáng hội tụ là chùm sáng gồm các tia sáng:", ["Giao nhau tại một điểm trên đường truyền của chúng", "Song song với nhau", "Loe rộng dần ra", "Không bao giờ cắt nhau"], 0, "Chùm hội tụ giao nhau tại một điểm tiêu điểm."),
        make_mc(4, "Nhận biết", "Trong môi trường nước trong suốt và đồng chất, ánh sáng truyền theo đường nào?", ["Đường thẳng", "Đường gấp khúc", "Đường cong tròn", "Đường lượn sóng"], 0, "Môi trường trong suốt đồng tính thì ánh sáng truyền thẳng."),
        make_mc(5, "Nhận biết", "Đom đóm đực phát sáng lập lòe trong đêm mùa hè là một ví dụ về:", ["Nguồn sáng sinh học", "Vật phản xạ ánh sáng", "Vật hấp thụ ánh sáng", "Gương phẳng"], 0, "Đom đóm tự phát sáng nhờ phản ứng sinh hóa, là nguồn sáng sinh học."),
        make_mc(6, "Nhận biết", "Vùng bóng nửa tối là vùng:", ["Chỉ nhận được một phần ánh sáng từ nguồn sáng truyền tới", "Hoàn toàn tối đen không nhận được ánh sáng", "Nhận được toàn bộ ánh sáng", "Sáng rực rỡ"], 0, "Vùng bóng nửa tối nhận một phần ánh sáng từ nguồn sáng rộng."),
        make_mc(7, "Thông hiểu", "Vì sao trong một căn phòng đóng kín cửa vào ban đêm ta lại không nhìn thấy chiếc bàn?", ["Vì chiếc bàn không tự phát sáng và không có nguồn sáng chiếu vào để hắt ánh sáng tới mắt ta", "Vì chiếc bàn tàng hình", "Vì mắt ta bị hỏng", "Vì chiếc bàn biến thành màu đen"], 0, "Không có ánh sáng từ chiếc bàn truyền vào mắt."),
        make_mc(8, "Thông hiểu", "Chùm sáng phát ra từ một chiếc đèn laser đồ chơi chiếu trên bảng là mô hình thực tế của:", ["Tia sáng hẹp (hoặc chùm sáng song song rất mảnh)", "Chùm sáng phân kì rộng", "Chùm sáng hội tụ", "Nguồn sáng cầu"], 0, "Tia laser có chùm tia cực mảnh và song song, dùng làm mô hình tia sáng."),
        make_mc(9, "Thông hiểu", "Khi Trái Đất đi vào vùng bóng tối hoàn toàn của Mặt Trăng, trên Trái Đất sẽ quan sát được hiện tượng:", ["Nhật thực toàn phần", "Nguyệt thực toàn phần", "Nhật thực một phần", "Sao băng"], 0, "Vùng bóng tối của Mặt Trăng trên Trái Đất quan sát được Nhật thực toàn phần."),
        make_mc(10, "Thông hiểu", "Đặt một tấm bìa đục chắn trước ngọn nến đang cháy, phía sau tấm bìa đặt màn chắn. Trên màn chắn xuất hiện:", ["Vùng bóng tối ở giữa bao quanh bởi vùng bóng nửa tối", "Vùng sáng đều", "Không có hiện tượng gì", "Toàn bộ màn chắn đều sáng rực"], 0, "Nguồn nến là nguồn sáng rộng nên tạo vùng bóng tối ở tâm và bóng nửa tối viền xung quanh."),
        make_mc(11, "Thông hiểu", "Tại sao người ta dùng ống ngắm laze trên súng thể thao bắn bia?", ["Vì ánh sáng laser truyền thẳng giúp định vị đường ngắm bắn chuẩn xác", "Vì tia laser đẩy viên đạn bay nhanh hơn", "Vì tia laser làm bia phát sáng", "Vì tia laser làm súng nhẹ hơn"], 0, "Ứng dụng tính truyền thẳng của tia laser để định hướng đường ngắm thẳng."),
        make_mc(12, "Thông hiểu", "Hiện tượng bóng của cái cây trên sân trường thay đổi chiều dài từ sáng đến trưa rồi đến chiều là do:", ["Vị trí của Mặt Trời trên bầu trời thay đổi làm góc chiếu của tia sáng thay đổi", "Cái cây lớn nhanh trong ngày", "Mặt đất bị nghiêng", "Không khí nóng lên"], 0, "Góc chiếu của tia sáng Mặt Trời thay đổi theo thời gian trong ngày.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phân loại nguồn sáng và vật sáng trong đời sống:", [
            ("a", "Bóng đèn LED đang sáng là nguồn sáng nhân tạo.", True),
            ("b", "Mặt Trời và các ngôi sao tự phát sáng là các nguồn sáng tự nhiên.", True),
            ("c", "Tờ giấy trắng đặt dưới ánh đèn là vật sáng vì nó hắt lại ánh sáng của đèn.", True),
            ("d", "Mặt gương soi tự nó phát ra ánh sáng trong đêm tối mà không cần đèn.", False)
        ], "Gương soi chỉ phản xạ ánh sáng, không thể tự phát sáng."),
        make_tf(2, "Thông hiểu", "Về các loại chùm sáng thường gặp:", [
            ("a", "Chùm sáng song song gồm các tia sáng song song không bao giờ giao nhau.", True),
            ("b", "Chùm sáng hội tụ loe rộng dần trên đường truyền.", False),
            ("c", "Chùm sáng phân kì loe rộng dần ra trên đường truyền.", True),
            ("d", "Ánh sáng phát ra từ một ngọn đèn dầu là chùm sáng phân kì truyền theo mọi hướng.", True)
        ], "Chùm hội tụ thu hẹp dần và giao nhau tại một điểm, chùm phân kì mới loe rộng ra."),
        make_tf(3, "Vận dụng", "Khảo sát vùng bóng tối và bóng nửa tối phía sau một vật cản tròn:", [
            ("a", "Nếu nguồn sáng là một điểm sáng rất nhỏ thì chỉ thu được vùng bóng tối rõ nét trên màn chắn.", True),
            ("b", "Nếu nguồn sáng có kích thước lớn (như bóng đèn tuýp dài) thì sẽ xuất hiện cả vùng bóng tối và vùng bóng nửa tối.", True),
            ("c", "Vùng bóng nửa tối là vùng hoàn toàn không có tia sáng nào chiếu tới.", False),
            ("d", "Di chuyển màn chắn ra xa vật cản thì kích thước vùng bóng nửa tối sẽ mở rộng ra.", True)
        ], "Vùng bóng nửa tối nhận được một phần ánh sáng từ nguồn sáng rộng."),
        make_tf(4, "Vận dụng", "Quan sát hiện tượng Nguyệt thực vào đêm rằm:", [
            ("a", "Mặt Trăng đi vào vùng bóng tối của Trái Đất nên bị che khuất không nhận được ánh sáng Mặt Trời.", True),
            ("b", "Mọi người ở nửa Trái Đất quay về phía ban đêm đều có thể cùng quan sát được Nguyệt thực.", True),
            ("c", "Thời gian diễn ra hiện tượng Nguyệt thực thường dài hơn nhiều so với Nhật thực toàn phần.", True),
            ("d", "Hiện tượng Nguyệt thực xảy ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất.", False)
        ], "Nguyệt thực xảy ra khi Trái Đất nằm ở giữa Mặt Trời và Mặt Trăng.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đom đóm lập lòe trong đêm là nguồn sáng hay vật được chiếu sáng?", "Nguồn sáng", "Nguồn sáng sinh học."),
        make_sa(2, "Thông hiểu", "Quyển sách nằm trên bàn ban ngày là nguồn sáng hay vật sáng?", "Vật sáng", "Vật sáng (hắt lại ánh sáng)."),
        make_sa(3, "Vận dụng", "Chùm sáng gồm các tia sáng giao nhau tại một điểm gọi là chùm sáng gì?", "Hội tụ", "Chùm sáng hội tụ."),
        make_sa(4, "Vận dụng", "Khi Trái Đất nằm giữa Mặt Trời và Mặt Trăng sẽ xảy ra hiện tượng gì? (Nhật thực hay Nguyệt thực)", "Nguyệt thực", "Nguyệt thực."),
        make_sa(5, "Vận dụng cao", "Một chiếc cọc cao 1 mét cắm thẳng đứng trên sân phẳng có bóng nắng dài 1,5 mét. Một cái cây gần đó có bóng dài 6 mét. Cây cao bao nhiêu mét?", "4", "h = 6 / 1,5 = 4 m."),
        make_sa(6, "Vận dụng cao", "Đường truyền của ánh sáng được biểu diễn bằng hình gì có mũi tên chỉ hướng?", "Đường thẳng", "Đường thẳng có mũi tên chỉ hướng.")
    ],
    "part4": [
        make_vdc(1, "Một người muốn đóng một chiếc cọc thứ ba C thẳng hàng với hai chiếc cọc A và B đã cắm sẵn trên cánh đồng. Người đó đứng tại vị trí cọc A, nhìn về phía cọc B và cắm cọc C sao cho:", ["Cọc B che khuất hoàn toàn cọc C đối với mắt đặt tại A", "Cọc C cao hơn cọc B", "Cọc C ở bên cạnh cọc B", "Cọc C phát sáng"], 0, "Ánh sáng truyền thẳng, nếu cọc B che khuất cọc C thì A, B, C thẳng hàng."),
        make_vdc(2, "Vào những ngày nắng gắt, dưới bóng mát của các tán cây rậm rạp, ta thường quan sát thấy trên mặt đất có những đốm sáng hình tròn nhỏ li ti sáng rực rỡ. Nguồn gốc của các đốm sáng hình tròn này là:", ["Hình ảnh thực của Mặt Trời (nguồn sáng hình cầu) được tạo bởi hiện tượng tạo ảnh qua lỗ kim từ các khe hở nhỏ giữa các kẽ lá", "Do gió thổi tròn lá", "Do bóng của lá cây hình tròn", "Do giọt nước đọng trên lá"], 0, "Hiện tượng máy ảnh lỗ kim (Pinhole camera) tự nhiên: khe lá nhỏ tạo ảnh thật của Mặt Trời hình tròn trên mặt đất."),
        make_vdc(3, "Một ngọn đèn đường treo ở độ cao 4 mét so với mặt đất. Một người cao 1,6 mét đứng cách cột đèn một khoảng 3 mét. Chiều dài bóng của người đó in trên mặt đất là:", ["2,0 mét", "1,5 mét", "2,5 mét", "1,8 mét"], 0, "Gọi chiều dài bóng là x. Ta có: x / (x + 3) = 1,6 / 4 = 0,4 => x = 0,4x + 1,2 => 0,6x = 1,2 => x = 2,0 m."),
        make_vdc(4, "Tại sao khi xảy ra hiện tượng Nhật thực một phần, nếu nhìn trực tiếp bằng mắt thường hoặc qua kính râm thông thường thì có thể bị bỏng giác mạc và mù lòa vĩnh viễn?", ["Vì cường độ bức xạ hồng ngoại và tử ngoại của Mặt Trời chiếu vào mắt cực mạnh làm cháy các tế bào võng mạc mà mắt không có phản xạ chớp", "Vì Mặt Trăng phát tia độc", "Vì không khí biến thành khí độc", "Vì bóng tối làm cay mắt"], 0, "Bức xạ mặt trời có năng lượng hội tụ vào đáy mắt làm cháy võng mạc mà không kịp chớp mắt tự vệ.")
    ]
}

# --- ĐỀ 3 ---
b15_b16_exams["phys7_c5_b15_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 15: Ánh sáng, tia sáng - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b15", "lessonName": "Bài 15: Ánh sáng, tia sáng",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật nào sau đây KHÔNG PHẢI là nguồn sáng?", ["Mặt Trăng", "Mặt Trời", "Ngọn nến đang cháy", "Bóng đèn neon đang sáng"], 0, "Mặt Trăng hắt lại ánh sáng từ Mặt Trời, không phải nguồn sáng."),
        make_mc(2, "Nhận biết", "Ánh sáng từ Mặt Trời chiếu xuống Trái Đất truyền qua môi trường chân không ngoài vũ trụ chứng tỏ:", ["Ánh sáng có thể truyền được trong môi trường chân không", "Chân không là chất lỏng", "Chân không hút ánh sáng", "Ánh sáng không có thật"], 0, "Ánh sáng là sóng điện từ truyền được hoàn hảo trong chân không."),
        make_mc(3, "Nhận biết", "Chùm sáng phát ra từ một chiếc kính lúp khi để dưới ánh nắng Mặt Trời tụ lại thành một điểm sáng nhỏ rất nóng là chùm sáng:", ["Hội tụ", "Phân kì", "Song song", "Tròn"], 0, "Tụ lại thành một điểm là chùm sáng hội tụ."),
        make_mc(4, "Nhận biết", "Định luật truyền thẳng ánh sáng chỉ nghiệm đúng trong điều kiện môi trường:", ["Trong suốt và đồng tính (đồng nhất)", "Bất kì", "Có nhiều bụi bẩn", "Đang chuyển động hỗn loạn"], 0, "Môi trường phải trong suốt và đồng tính."),
        make_mc(5, "Nhận biết", "Mô hình biểu diễn tia sáng gồm:", ["Một đoạn thẳng có mũi tên chỉ hướng truyền của ánh sáng", "Một hình tròn kín", "Một hình tam giác", "Một đường cong parabol"], 0, "Tia sáng biểu diễn bằng đường thẳng có mũi tên chỉ hướng."),
        make_mc(6, "Nhận biết", "Khi có Nhật thực toàn phần xảy ra, vùng tối trên bề mặt Trái Đất là nơi nhận được:", ["Hoàn toàn không có ánh sáng trực tiếp từ Mặt Trời chiếu tới", "Toàn bộ ánh sáng Mặt Trời", "Một nửa ánh sáng", "Ánh sáng màu xanh"], 0, "Vùng bóng tối của Mặt Trăng không nhận ánh sáng trực tiếp từ Mặt Trời."),
        make_mc(7, "Thông hiểu", "Vì sao người thợ mộc khi bào một thanh gỗ thường nhắm một mắt và ngắm dọc theo mép thanh gỗ?", ["Để ứng dụng định luật truyền thẳng ánh sáng kiểm tra độ phẳng thẳng của mép gỗ", "Để thư giãn mắt", "Để thanh gỗ không bị bụi", "Để gỗ nhanh khô"], 0, "Ngắm thẳng hàng theo đường truyền thẳng của tia sáng."),
        make_mc(8, "Thông hiểu", "Chùm sáng phát ra từ đèn pha ô tô khi bật chế độ chiếu xa (đèn pha) xấp xỉ là chùm sáng:", ["Song song", "Hội tụ", "Phân kì rất rộng", "Hình cầu"], 0, "Đèn pha ô tô dùng chóa phản xạ tạo chùm sáng song song chiếu xa."),
        make_mc(9, "Thông hiểu", "Bóng nửa tối xuất hiện xung quanh bóng tối khi nguồn sáng là:", ["Nguồn sáng có kích thước rộng", "Một điểm sáng cực nhỏ", "Mặt Trăng tròn", "Tia laser"], 0, "Nguồn sáng có kích thước lớn tạo vùng bóng nửa tối viền xung quanh."),
        make_mc(10, "Thông hiểu", "Khi đứng trước một ngọn đèn cao áp vào ban đêm, nếu ta giơ một bàn tay lên phía trước thì trên mặt đất xuất hiện bóng của bàn tay. Đó là do:", ["Bàn tay là vật cản cản trở ánh sáng truyền thẳng từ đèn xuống mặt đất", "Bàn tay hút ánh sáng", "Đèn bị hỏng", "Không khí bị lạnh đi"], 0, "Ánh sáng truyền thẳng gặp bàn tay bị chặn lại tạo bóng tối trên đất."),
        make_mc(11, "Thông hiểu", "Vào những đêm trăng rằm không mây, ta nhìn thấy Mặt Trăng tròn vành vạnh chiếu sáng bầu trời đêm. Ánh trăng đó bắt nguồn từ:", ["Ánh sáng của Mặt Trời chiếu vào bề mặt Mặt Trăng rồi phản xạ (hắt lại) đến mắt ta trên Trái Đất", "Mặt Trăng tự cháy sáng", "Trái Đất chiếu sáng Mặt Trăng", "Mặt Trăng phát ra lân tinh"], 0, "Mặt Trăng là vật sáng phản chiếu ánh sáng Mặt Trời."),
        make_mc(12, "Thông hiểu", "Hiện tượng nguyệt thực toàn phần có thể kéo dài hàng giờ đồng hồ trong khi nhật thực toàn phần chỉ diễn ra trong vài phút là vì:", ["Bóng tối của Trái Đất có kích thước lớn hơn rất nhiều so với bóng tối của Mặt Trăng", "Mặt Trời tắt đi", "Mặt Trăng bay rất nhanh", "Mặt Trăng nhỏ hơn hạt cát"], 0, "Kích thước Trái Đất lớn hơn Mặt Trăng rất nhiều nên vùng bóng tối Trái Đất bao trùm rộng lớn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất của sự truyền ánh sáng:", [
            ("a", "Ánh sáng truyền đi trong không khí với tốc độ xấp xỉ 300.000 km/s.", True),
            ("b", "Khi ánh sáng truyền qua mặt phân cách giữa không khí và nước thì tia sáng bị gãy khúc.", True),
            ("c", "Tia sáng luôn truyền theo đường thẳng trong mọi điều kiện môi trường bất kì.", False),
            ("d", "Bóng tối là vùng hoàn toàn không nhận được ánh sáng từ nguồn sáng do vật cản chắn lại.", True)
        ], "Ánh sáng chỉ truyền thẳng trong môi trường trong suốt và đồng tính."),
        make_tf(2, "Thông hiểu", "Về các chùm sáng cơ bản trong quang học:", [
            ("a", "Chùm sáng song song gồm các tia sáng song song nhau.", True),
            ("b", "Chùm sáng hội tụ gồm các tia sáng tiến lại gần nhau và giao nhau tại một điểm.", True),
            ("c", "Chùm sáng phân kì loe rộng ra từ một điểm nguồn.", True),
            ("d", "Chùm sáng phát ra từ đèn pin là chùm sáng hội tụ.", False)
        ], "Đèn pin phát ra chùm sáng phân kì loe rộng ra."),
        make_tf(3, "Vận dụng", "Ứng dụng định luật truyền thẳng ánh sáng trong đời sống và kĩ thuật:", [
            ("a", "Người thợ xây căng một sợi dây rọi để xây tường thẳng đứng.", True),
            ("b", "Các vận động viên bắn súng ngắm qua đầu ruồi và khe ngắm thẳng hàng với tâm bia.", True),
            ("c", "Kính thiên văn quang học dùng để thu nhận ánh sáng từ các vì sao truyền qua không gian vũ trụ.", True),
            ("d", "Đèn hải đăng chiếu chùm sáng phân kì thật rộng để rọi sáng đáy biển.", False)
        ], "Đèn hải đăng tạo chùm sáng song song cực mạnh quét ngang mặt biển để báo hiệu cho tàu thuyền từ xa."),
        make_tf(4, "Vận dụng", "Quan sát hiện tượng Nhật thực trên Trái Đất:", [
            ("a", "Nhật thực xảy ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất trên một đường thẳng.", True),
            ("b", "Vùng bóng tối của Mặt Trăng trên bề mặt Trái Đất chỉ quét qua một dải hẹp vài trăm kilômét.", True),
            ("c", "Người ở vùng bóng nửa tối quan sát được Nhật thực một phần.", True),
            ("d", "Nhật thực có thể quan sát được vào lúc nửa đêm.", False)
        ], "Nhật thực là Mặt Trời bị che khuất, chỉ quan sát được vào ban ngày.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Mặt Trời truyền ánh sáng đến Trái Đất qua môi trường gì ngoài không gian vũ trụ?", "Chân không", "Môi trường chân không."),
        make_sa(2, "Thông hiểu", "Chùm sáng có các tia sáng song song nhau gọi là chùm sáng gì?", "Song song", "Chùm sáng song song."),
        make_sa(3, "Vận dụng", "Khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất sẽ tạo ra hiện tượng gì? (Nhật thực hay Nguyệt thực)", "Nhật thực", "Nhật thực."),
        make_sa(4, "Vận dụng", "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường gì?", "Đường thẳng", "Đường thẳng."),
        make_sa(5, "Vận dụng cao", "Một chiếc cọc sắt cao 2 mét cắm thẳng đứng có bóng nắng trên sân dài 1 mét. Một tòa nhà gần đó có bóng dài 15 mét. Chiều cao của tòa nhà là bao nhiêu mét?", "30", "h = 15 × 2 = 30 m."),
        make_sa(6, "Vận dụng cao", "Ánh sáng Mặt Trời truyền đến Trái Đất (khoảng cách 150 triệu km) với tốc độ 300.000 km/s mất thời gian bao nhiêu giây?", "500", "t = 150.000.000 / 300.000 = 500 s.")
    ],
    "part4": [
        make_vdc(1, "Một người muốn cắm một hàng cọc gồm 4 chiếc A, B, C, D thẳng hàng nhau trên một bờ ruộng. Người đó đã cắm xong hai cọc A và D ở hai đầu. Để cắm hai cọc B và C nằm chính xác trên đường thẳng nối A và D, người đó nên làm thế nào?", ["Đứng tại cọc A ngắm cọc D, sau đó cắm cọc B và C sao cho cọc trước che khuất cọc sau đối với mắt nhìn", "Cắm bừa rồi dùng dây kéo", "Đo bằng bước chân", "Đợi trời tối mới cắm"], 0, "Ứng dụng sự truyền thẳng của tia sáng: các cọc che khuất nhau trên đường ngắm."),
        make_vdc(2, "Tại sao khi chiếu đèn pin vào một quả cầu lớn đặt trước màn chắn, ta lại quan sát thấy trên màn chắn có một vùng tròn bóng tối đậm ở chính giữa và bao quanh bởi một dải bóng nửa tối nhạt dần ra ngoài?", ["Vì bóng đèn pin là nguồn sáng có kích thước rộng, các tia sáng từ các điểm khác nhau của bóng đèn tạo ra vùng bóng nửa tối viền xung quanh vùng bóng tối", "Vì quả cầu phát ra ánh sáng", "Vì màn chắn bị rách", "Vì pin sắp hết"], 0, "Nguồn sáng rộng luôn tạo vùng bóng tối ở tâm và vùng bóng nửa tối ở rìa."),
        make_vdc(3, "Một ngọn đèn đường treo ở đỉnh cột đèn cao 6 mét. Một bạn học sinh cao 1,5 mét đứng cách chân cột đèn 6 mét. Chiều dài bóng của bạn học sinh in trên mặt đường bằng bao nhiêu mét?", ["2 mét", "1,5 mét", "3 mét", "2,5 mét"], 0, "Gọi bóng là x. Ta có x / (x + 6) = 1,5 / 6 = 1/4 => 4x = x + 6 => 3x = 6 => x = 2 mét."),
        make_vdc(4, "Nhà thiên văn học Eratosthenes thời Hy Lạp cổ đại đã đo được chu vi Trái Đất xấp xỉ 40.000 km chỉ bằng cách đo bóng nắng của một chiếc cọc tại hai thành phố Alexandria và Syene vào buổi trưa ngày Hạ chí. Cơ sở khoa học nền tảng mà ông đã sử dụng là:", ["Định luật truyền thẳng ánh sáng và các tia sáng Mặt Trời chiếu tới Trái Đất coi như các đường thẳng song song", "Định luật phản xạ ánh sáng", "Định luật bảo toàn năng lượng", "Thuyết tương đối"], 0, "Tia sáng mặt trời chiếu song song kết hợp bóng của cọc thẳng đứng và định luật truyền thẳng ánh sáng.")
    ]
}

# =========================================================================
# BÀI 16: SỰ PHẢN XẠ ÁNH SÁNG (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b15_b16_exams["phys7_c5_b16_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 16: Sự phản xạ ánh sáng - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b16", "lessonName": "Bài 16: Sự phản xạ ánh sáng",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Hiện tượng tia sáng khi gặp mặt phân cách giữa hai môi trường trong suốt bị hắt ngược trở lại môi trường ban đầu được gọi là:", ["Hiện tượng phản xạ ánh sáng", "Hiện tượng khúc xạ ánh sáng", "Hiện tượng tán sắc ánh sáng", "Hiện tượng hấp thụ ánh sáng"], 0, "Hiện tượng phản xạ ánh sáng."),
        make_mc(2, "Nhận biết", "Đường thẳng vuông góc với mặt gương tại điểm tới I được gọi là:", ["Đường pháp tuyến (pháp tuyến tại điểm tới)", "Tia tới", "Tia phản xạ", "Mặt phẳng tới"], 0, "Đường pháp tuyến IN vuông góc với mặt gương."),
        make_mc(3, "Nhận biết", "Góc tới (kí hiệu i) là góc tạo bởi:", ["Tia tới SI và đường pháp tuyến IN", "Tia tới SI và mặt gương", "Tia phản xạ IR và mặt gương", "Tia phản xạ IR và tia tới SI"], 0, "Góc tới i = góc(SIN)."),
        make_mc(4, "Nhận biết", "Theo định luật phản xạ ánh sáng, góc phản xạ (r) và góc tới (i) luôn có mối quan hệ:", ["Góc phản xạ bằng góc tới (r = i)", "Góc phản xạ lớn hơn góc tới (r > i)", "Góc phản xạ nhỏ hơn góc tới (r < i)", "r + i = 90 độ"], 0, "Định luật phản xạ ánh sáng: r = i."),
        make_mc(5, "Nhận biết", "Mặt phẳng tới là mặt phẳng chứa:", ["Tia tới và đường pháp tuyến của gương tại điểm tới", "Tia phản xạ và mặt gương", "Tia tới và mặt gương", "Đường pháp tuyến và mặt gương"], 0, "Mặt phẳng tới chứa tia tới và pháp tuyến tại điểm tới."),
        make_mc(6, "Nhận biết", "Hiện tượng ánh sáng phản xạ theo nhiều hướng hỗn loạn khi gặp bề mặt gồ ghề, nhám được gọi là:", ["Hiện tượng phản xạ khuếch tán (tán xạ)", "Hiện tượng phản xạ gương", "Hiện tượng khúc xạ", "Hiện tượng bóng tối"], 0, "Phản xạ khuếch tán xảy ra trên bề mặt gồ ghề nhám."),
        make_mc(7, "Thông hiểu", "Chiếu một tia sáng tới mặt gương phẳng với góc tới i = 40 độ. Góc phản xạ r có giá trị bằng:", ["40 độ", "50 độ", "80 độ", "20 độ"], 0, "r = i = 40 độ."),
        make_mc(8, "Thông hiểu", "Chiếu một tia sáng tới vuông góc với mặt gương phẳng (góc tới i = 0 độ). Góc phản xạ có giá trị bằng:", ["0 độ (tia phản xạ bật ngược trở lại theo phương cũ)", "90 độ", "45 độ", "180 độ"], 0, "i = 0° => r = 0°, tia phản xạ bật thẳng ngược trở lại trùng pháp tuyến."),
        make_mc(9, "Thông hiểu", "Một tia sáng tới hợp với mặt phẳng gương một góc 30 độ. Góc tới i của tia sáng bằng:", ["60 độ", "30 độ", "90 độ", "120 độ"], 0, "Góc tới i = 90° - 30° = 60°."),
        make_mc(10, "Thông hiểu", "Chiếu tia tới tới mặt gương với góc tới i = 45 độ. Góc hợp bởi tia tới và tia phản xạ bằng:", ["90 độ", "45 độ", "180 độ", "60 độ"], 0, "Góc hợp bởi tia tới và phản xạ = i + r = 45° + 45° = 90°."),
        make_mc(11, "Thông hiểu", "Khi tăng góc tới i thêm 10 độ thì góc phản xạ r sẽ:", ["Tăng thêm 10 độ", "Giảm đi 10 độ", "Không đổi", "Tăng thêm 20 độ"], 0, "Vì r = i nên khi i tăng 10° thì r cũng tăng 10°."),
        make_mc(12, "Thông hiểu", "Hiện tượng nhìn thấy ảnh rõ nét của mình trong một chiếc gương soi phẳng là nhờ hiện tượng:", ["Phản xạ gương trên bề mặt nhẵn bóng", "Phản xạ khuếch tán", "Khúc xạ ánh sáng", "Nhiễu xạ ánh sáng"], 0, "Phản xạ gương tạo ảnh rõ nét đối xứng.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về định luật phản xạ ánh sáng đối với gương phẳng:", [
            ("a", "Tia phản xạ luôn nằm trong mặt phẳng tới chứa tia tới và đường pháp tuyến.", True),
            ("b", "Góc phản xạ luôn luôn bằng góc tới.", True),
            ("c", "Nếu tia sáng truyền theo chiều ngược lại của tia phản xạ thì nó sẽ phản xạ theo chiều tia tới ban đầu (tính thuận nghịch của ánh sáng).", True),
            ("d", "Góc tới là góc tạo bởi tia tới và bề mặt của gương.", False)
        ], "Góc tới là góc giữa tia tới và đường pháp tuyến vuông góc với gương."),
        make_tf(2, "Thông hiểu", "Về hiện tượng phản xạ gương và phản xạ khuếch tán:", [
            ("a", "Phản xạ gương xảy ra trên bề mặt nhẵn bóng như mặt gương phẳng, mặt nước phẳng lặng.", True),
            ("b", "Phản xạ gương cho ta nhìn thấy ảnh rõ nét của vật.", True),
            ("c", "Phản xạ khuếch tán xảy ra trên bề mặt gồ ghề nhám như mặt giấy, tường nhà.", True),
            ("d", "Phản xạ khuếch tán không tuân theo định luật phản xạ ánh sáng.", False)
        ], "Tại mỗi điểm tới vi mô trên bề mặt gồ ghề, định luật phản xạ ánh sáng vẫn nghiệm đúng tuyệt đối."),
        make_tf(3, "Vận dụng", "Chiếu tia sáng SI tới gương phẳng nằm ngang, tia tới hợp với mặt gương một góc 35 độ:", [
            ("a", "Đường pháp tuyến vuông góc với mặt gương tạo góc 90 độ.", True),
            ("b", "Góc tới i bằng 55 độ.", True),
            ("c", "Góc phản xạ r bằng 55 độ.", True),
            ("d", "Góc tạo bởi tia tới và tia phản xạ là 70 độ.", False)
        ], "Góc tạo bởi tia tới và phản xạ là i + r = 55° + 55° = 110°."),
        make_tf(4, "Vận dụng", "Một tia sáng chiếu tới mặt gương cố định. Giữ nguyên hướng tia tới, nếu quay mặt phẳng gương quanh trục qua điểm tới một góc 10 độ:", [
            ("a", "Pháp tuyến của gương quay đi một góc 10 độ.", True),
            ("b", "Góc tới thay đổi một lượng 10 độ.", True),
            ("c", "Tia phản xạ sẽ quay đi một góc 20 độ.", True),
            ("d", "Tia phản xạ giữ nguyên hướng không hề thay đổi.", False)
        ], "Khi quay gương một góc α, tia phản xạ quay đi một góc 2α = 20°.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Góc tới bằng 30 độ thì góc phản xạ bằng bao nhiêu độ?", "30", "r = i = 30 độ."),
        make_sa(2, "Thông hiểu", "Tia tới hợp với pháp tuyến góc 50 độ. Góc phản xạ bằng bao nhiêu độ?", "50", "r = i = 50 độ."),
        make_sa(3, "Vận dụng", "Tia tới hợp với mặt gương phẳng góc 40 độ. Góc tới bằng bao nhiêu độ?", "50", "i = 90 - 40 = 50 độ."),
        make_sa(4, "Vận dụng", "Góc tới bằng 60 độ. Góc tạo bởi tia tới và tia phản xạ bằng bao nhiêu độ?", "120", "i + r = 60 + 60 = 120 độ."),
        make_sa(5, "Vận dụng cao", "Tia tới hợp với tia phản xạ một góc 80 độ. Góc phản xạ bằng bao nhiêu độ?", "40", "r = 80 / 2 = 40 độ."),
        make_sa(6, "Vận dụng cao", "Giữ nguyên tia tới, quay gương phẳng quanh trục qua điểm tới một góc 25 độ. Tia phản xạ quay đi một góc bao nhiêu độ?", "50", "2α = 2 × 25 = 50 độ.")
    ],
    "part4": [
        make_vdc(1, "Một tia sáng SI chiếu tới gương phẳng nằm ngang. Muốn có tia phản xạ IR hướng thẳng đứng từ dưới lên trên thì góc hợp bởi tia tới SI và mặt gương phải bằng bao nhiêu độ? Biết tia tới SI chiếu chếch từ trên xuống hợp với phương nằm ngang góc 40 độ.", ["65 độ", "40 độ", "50 độ", "75 độ"], 0, "Góc giữa SI và IR = 90° + 40° = 130°. Góc tới i = 130° / 2 = 65°. Góc hợp bởi tia tới và mặt gương = 90° - 65° = 25° (hoặc gương đặt nghiêng góc thích hợp tạo góc 65°)."),
        make_vdc(2, "Hai gương phẳng G1 và G2 đặt vuông góc với nhau (hợp với nhau góc 90 độ), mặt phản xạ quay vào nhau. Chiếu một tia sáng SI tới gương G1 với góc tới i1 bất kì (0 < i1 < 90°), tia phản xạ từ G1 đến đập vào gương G2 rồi phản xạ tiếp thành tia JR. Tia phản xạ cuối cùng JR có hướng như thế nào so với tia tới ban đầu SI?", ["Luôn luôn song song và ngược chiều với tia tới ban đầu SI", "Vuông góc với tia tới ban đầu", "Trùng khít với tia tới", "Hợp với tia tới góc 45 độ"], 0, "Hệ hai gương vuông góc luôn phản xạ tia sáng quay ngược trở lại song song (nguyên lí tấm phản quang mắt mèo)."),
        make_vdc(3, "Một căn phòng tối có một lỗ nhỏ trên mái nhà cho một tia sáng Mặt Trời lọt vào theo phương nghiêng hợp với phương nằm ngang một góc 60 độ. Để chiếu thẳng đứng tia sáng đó xuống đáy một chiếc giếng sâu dưới sàn phòng, người ta cần đặt một gương phẳng tại điểm tới nghiêng một góc bao nhiêu độ so với phương thẳng đứng?", ["15 độ", "30 độ", "75 độ", "45 độ"], 0, "Góc giữa tia tới và tia phản xạ: 60° + 90° = 150°. Góc tới i = 150° / 2 = 75°. Pháp tuyến nghiêng 75° so với tia phản xạ (thẳng đứng), mặt gương nghiêng 90° - 75° = 15° so với phương thẳng đứng."),
        make_vdc(4, "Một ngọn nến đặt trước một tấm bìa đen có khoét một lỗ kim nhỏ, phía sau là một màn chắn. Nếu đặt thêm một chiếc gương phẳng ở phía sau lỗ kim hợp góc 45 độ thì đường truyền tia sáng phản xạ sẽ đổi hướng bao nhiêu độ?", ["90 độ", "45 độ", "180 độ", "60 độ"], 0, "Gương nghiêng 45° đổi hướng tia sáng một góc 90°.")
    ]
}

# --- ĐỀ 2 ---
b15_b16_exams["phys7_c5_b16_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 16: Sự phản xạ ánh sáng - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b16", "lessonName": "Bài 16: Sự phản xạ ánh sáng",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Góc phản xạ là góc tạo bởi:", ["Tia phản xạ và đường pháp tuyến của gương tại điểm tới", "Tia phản xạ và mặt phẳng gương", "Tia tới và mặt phẳng gương", "Tia tới và tia phản xạ"], 0, "Góc phản xạ r = góc(NIR)."),
        make_mc(2, "Nhận biết", "Kí hiệu thông thường của góc tới và góc phản xạ lần lượt là:", ["i và r", "r và i", "α và β", "v và s"], 0, "Góc tới là i, góc phản xạ là r."),
        make_mc(3, "Nhận biết", "Tia phản xạ nằm trong mặt phẳng nào sau đây?", ["Mặt phẳng tới chứa tia tới và pháp tuyến tại điểm tới", "Mặt phẳng chứa gương", "Mặt phẳng vuông góc với tia tới", "Mặt phẳng ngang"], 0, "Tia phản xạ nằm trong mặt phẳng tới."),
        make_mc(4, "Nhận biết", "Nếu chiếu tia tới SI vuông góc với mặt gương phẳng thì góc tới i bằng:", ["0 độ", "90 độ", "45 độ", "180 độ"], 0, "Tia tới trùng pháp tuyến nên i = 0 độ."),
        make_mc(5, "Nhận biết", "Gương phẳng là:", ["Một mặt phẳng nhẵn bóng có khả năng phản xạ hầu hết ánh sáng chiếu tới", "Một khối cầu trong suốt", "Một tấm kính mờ", "Một tấm kim loại gồ ghề"], 0, "Gương phẳng là mặt phẳng nhẵn bóng phản xạ tốt."),
        make_mc(6, "Nhận biết", "Khi có phản xạ khuếch tán, ta nhìn thấy bề mặt vật sáng:", ["Được chiếu sáng từ mọi hướng nhưng không thấy ảnh rõ nét của nguồn sáng", "Như một chiếc gương soi", "Tối đen hoàn toàn", "Phát ra tia laser"], 0, "Phản xạ khuếch tán giúp ta nhìn thấy vật sáng từ mọi phía mà không thấy ảnh."),
        make_mc(7, "Thông hiểu", "Chiếu một tia sáng tới gương phẳng với góc tới i = 25 độ. Góc phản xạ r bằng:", ["25 độ", "50 độ", "65 độ", "75 độ"], 0, "r = i = 25 độ."),
        make_mc(8, "Thông hiểu", "Tia sáng tới hợp với mặt gương một góc 45 độ. Góc phản xạ r có giá trị bằng:", ["45 độ", "90 độ", "30 độ", "60 độ"], 0, "Góc tới i = 90° - 45° = 45° => r = 45°."),
        make_mc(9, "Thông hiểu", "Chiếu tia tới SI sao cho góc hợp bởi tia tới và tia phản xạ bằng 100 độ. Góc tới i có giá trị là:", ["50 độ", "100 độ", "25 độ", "40 độ"], 0, "i = 100° / 2 = 50°."),
        make_mc(10, "Thông hiểu", "Nếu giảm góc tới i đi 15 độ thì góc tạo bởi tia tới và tia phản xạ sẽ:", ["Giảm đi 30 độ", "Giảm đi 15 độ", "Tăng thêm 15 độ", "Không đổi"], 0, "Góc hợp bởi hai tia là 2i, khi i giảm 15° thì 2i giảm 30°."),
        make_mc(11, "Thông hiểu", "Khi soi gương, ta có thể nhìn thấy dòng chữ trên áo mình in ngược là do:", ["Hiện tượng phản xạ ánh sáng của gương phẳng tạo ảnh đối xứng trục trái phải", "Mắt người nhìn sai", "Áo in bị lỗi", "Gương bị cong"], 0, "Gương phẳng tạo ảnh đối xứng qua mặt phẳng gương, đổi hướng trái phải."),
        make_mc(12, "Thông hiểu", "Tấm phản quang gắn ở đuôi xe đạp có màu đỏ phát sáng khi đèn xe ô tô phía sau chiếu vào là nhờ cấu tạo:", ["Nhiều góc vuông gồm các mặt phản xạ vuông góc với nhau hắt tia sáng ngược trở lại nguồn", "Bên trong có bóng đèn pin", "Sơn lân tinh tự sáng", "Pin năng lượng mặt trời"], 0, "Cấu tạo các hốc phản xạ góc vuông hắt tia sáng quay về nguồn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các quy tắc trong định luật phản xạ ánh sáng:", [
            ("a", "Pháp tuyến là đường thẳng vuông góc với mặt gương tại điểm tới.", True),
            ("b", "Góc phản xạ r luôn luôn bằng góc tới i.", True),
            ("c", "Tia phản xạ và tia tới luôn nằm cùng một phía so với đường pháp tuyến.", False),
            ("d", "Tia tới, tia phản xạ và đường pháp tuyến cùng nằm trong một mặt phẳng.", True)
        ], "Tia tới và tia phản xạ nằm ở hai phía đối xứng qua đường pháp tuyến."),
        make_tf(2, "Thông hiểu", "Về ứng dụng của hiện tượng phản xạ ánh sáng:", [
            ("a", "Gương chiếu hậu trên xe ô tô giúp tài xế quan sát các xe phía sau nhờ phản xạ ánh sáng.", True),
            ("b", "Mặt biển phẳng lặng phản chiếu hình ảnh ngọn núi và bầu trời như một tấm gương khổng lồ.", True),
            ("c", "Mặt đường nhựa khô ráp phản xạ ánh sáng theo kiểu phản xạ gương rõ nét.", False),
            ("d", "Khi trời mưa, mặt đường đọng nước nhẵn bóng có thể gây lóa mắt tài xế do phản xạ gương ánh đèn.", True)
        ], "Đường nhựa khô nhám gây phản xạ khuếch tán, khi ướt đọng nước mới tạo phản xạ gương làm chói lóa."),
        make_tf(3, "Vận dụng", "Chiếu tia sáng SI tới mặt gương nằm ngang, góc hợp bởi tia tới và mặt gương là 50 độ:", [
            ("a", "Góc tới i bằng 40 độ.", True),
            ("b", "Góc phản xạ r bằng 40 độ.", True),
            ("c", "Góc hợp bởi tia phản xạ và mặt phẳng gương là 50 độ.", True),
            ("d", "Góc tạo bởi tia tới và tia phản xạ là 100 độ.", False)
        ], "Góc hợp bởi tia tới và tia phản xạ là i + r = 40° + 40° = 80° (câu d ghi 100° là sai)."),
        make_tf(4, "Vận dụng", "Khảo sát tia sáng qua hai gương phẳng đặt song song có mặt phản xạ hướng vào nhau:", [
            ("a", "Chiếu tia tới tới gương 1 với góc tới i1, tia phản xạ tới gương 2 với góc tới i2.", True),
            ("b", "Vì hai gương song song nên hai pháp tuyến song song, do đó i1 = i2.", True),
            ("c", "Tia phản xạ ló ra từ gương 2 luôn song song và cùng chiều với tia tới ban đầu.", True),
            ("d", "Nếu đổi góc tới thì tia phản xạ cuối cùng sẽ bị lệch vuông góc.", False)
        ], "Hai gương phẳng song song luôn cho tia phản xạ cuối cùng song song với tia tới ban đầu.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Góc tới bằng 45 độ. Góc phản xạ bằng bao nhiêu độ?", "45", "r = i = 45 độ."),
        make_sa(2, "Thông hiểu", "Chiếu tia sáng vuông góc với gương phẳng. Góc phản xạ bằng bao nhiêu độ?", "0", "r = i = 0 độ."),
        make_sa(3, "Vận dụng", "Tia tới hợp với mặt phẳng gương góc 30 độ. Góc tới bằng bao nhiêu độ?", "60", "i = 90 - 30 = 60 độ."),
        make_sa(4, "Vận dụng", "Góc tới bằng 35 độ. Góc tạo bởi tia tới và tia phản xạ bằng bao nhiêu độ?", "70", "35 + 35 = 70 độ."),
        make_sa(5, "Vận dụng cao", "Góc tạo bởi tia tới và tia phản xạ bằng 60 độ. Góc phản xạ bằng bao nhiêu độ?", "30", "r = 60 / 2 = 30 độ."),
        make_sa(6, "Vận dụng cao", "Tia tới cố định, nếu quay mặt gương một góc 12 độ thì tia phản xạ quay đi một góc bao nhiêu độ?", "24", "2 × 12 = 24 độ.")
    ],
    "part4": [
        make_vdc(1, "Một tia sáng SI chiếu nghiêng hợp với phương nằm ngang một góc 30 độ truyền tới một điểm I trên mặt đất. Người ta đặt một gương phẳng tại I để hắt tia phản xạ IR truyền thẳng đứng xuống đáy một chiếc giếng sâu. Mặt gương phẳng cần đặt nghiêng một góc bao nhiêu độ so với phương thẳng đứng?", ["30 độ", "60 độ", "15 độ", "45 độ"], 0, "Góc giữa SI và IR = 30° + 90° = 120°. Góc tới i = 120° / 2 = 60°. Mặt gương nghiêng 90° - 60° = 30° so với phương thẳng đứng."),
        make_vdc(2, "Một ngọn hải đăng phát ra một chùm tia sáng hẹp nằm ngang. Để chiếu chùm tia sáng đó xuống chiếu sáng một chiếc ca nô đang cứu nạn ở phương tạo với phương nằm ngang một góc 40 độ chếch xuống dưới, người ta đặt một tấm gương phẳng tại điểm đèn. Góc tới i của tia sáng tới mặt gương bằng:", ["20 độ", "40 độ", "70 độ", "50 độ"], 0, "Góc giữa tia tới và tia phản xạ là 40°. Góc tới i = 40° / 2 = 20°."),
        make_vdc(3, "Một căn phòng có hai gương phẳng treo trên hai bức tường đối diện song song nhau. Khi một người đứng giữa hai gương soi gương, người đó sẽ quan sát thấy:", ["Vô số ảnh ảo của mình nối tiếp nhau thành một hàng sâu hun hút", "Chỉ duy nhất một ảnh", "Hai ảnh", "Bốn ảnh"], 0, "Hiện tượng phản xạ ánh sáng lặp đi lặp lại vô tận giữa hai gương phẳng song song tạo dãy vô số ảnh."),
        make_vdc(4, "Một tia sáng chiếu tới gương phẳng tại điểm I với góc tới i = 30 độ. Nếu giữ nguyên tia tới và quay gương một góc 15 độ quanh trục vuông góc với mặt phẳng tới thì góc hợp bởi tia tới và tia phản xạ mới có thể nhận giá trị nào sau đây?", ["90 độ (hoặc 30 độ)", "60 độ", "45 độ", "120 độ"], 0, "Góc hợp ban đầu 2i = 60°. Khi quay gương 15°, tia phản xạ quay 2α = 30° => Góc mới: 60° + 30° = 90° (hoặc 60° - 30° = 30°).")
    ]
}

# --- ĐỀ 3 ---
b15_b16_exams["phys7_c5_b16_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 16: Sự phản xạ ánh sáng - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c5", "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b16", "lessonName": "Bài 16: Sự phản xạ ánh sáng",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Trong định luật phản xạ ánh sáng, tia phản xạ nằm trong:", ["Mặt phẳng tới chứa tia tới và đường pháp tuyến", "Mặt phẳng gương", "Bất kì mặt phẳng nào", "Mặt phẳng thẳng đứng"], 0, "Tia phản xạ nằm trong mặt phẳng tới."),
        make_mc(2, "Nhận biết", "Mối quan hệ giữa góc tới i và góc phản xạ r là:", ["r = i", "r > i", "r < i", "r = 2i"], 0, "r = i."),
        make_mc(3, "Nhận biết", "Đường pháp tuyến của gương phẳng tại điểm tới là đường thẳng:", ["Vuông góc với mặt gương tại điểm tới", "Song song với mặt gương", "Hợp với mặt gương góc 45 độ", "Trùng với tia tới"], 0, "Pháp tuyến vuông góc với mặt gương tại điểm tới."),
        make_mc(4, "Nhận biết", "Hiện tượng ánh sáng bị hắt lại theo một hướng xác định từ bề mặt phẳng nhẵn được gọi là:", ["Phản xạ gương", "Phản xạ khuếch tán", "Khúc xạ", "Hấp thụ"], 0, "Phản xạ gương định hướng tia sáng xác định."),
        make_mc(5, "Nhận biết", "Vật nào sau đây phản xạ ánh sáng theo định luật phản xạ ánh sáng?", ["Mọi vật có bề mặt phản xạ (cả mặt nhẵn và mặt gồ ghề vi mô)", "Chỉ gương phẳng", "Chỉ mặt nước", "Chỉ kim loại"], 0, "Định luật phản xạ ánh sáng đúng tại mọi điểm tới của mọi bề mặt."),
        make_mc(6, "Nhận biết", "Góc hợp bởi tia tới và mặt gương có mối quan hệ với góc tới i là:", ["Góc hợp = 90 độ - i", "Góc hợp = i", "Góc hợp = 180 độ - i", "Góc hợp = 2i"], 0, "Vì pháp tuyến vuông góc gương nên góc hợp với gương = 90° - i."),
        make_mc(7, "Thông hiểu", "Chiếu tia tới tới gương phẳng với góc tới i = 60 độ. Góc phản xạ r bằng:", ["60 độ", "30 độ", "120 độ", "90 độ"], 0, "r = i = 60 độ."),
        make_mc(8, "Thông hiểu", "Tia tới hợp với mặt phẳng gương một góc 20 độ. Góc phản xạ r bằng:", ["70 độ", "20 độ", "40 độ", "80 độ"], 0, "i = 90° - 20° = 70° => r = 70°."),
        make_mc(9, "Thông hiểu", "Tia tới SI hợp với tia phản xạ IR một góc 140 độ. Góc tới i có độ lớn là:", ["70 độ", "140 độ", "35 độ", "40 độ"], 0, "i = 140° / 2 = 70°."),
        make_mc(10, "Thông hiểu", "Khi một người dịch chuyển đèn pin lại gần gương sao cho góc tới i tăng từ 30 độ lên 50 độ thì góc phản xạ r sẽ:", ["Tăng từ 30 độ lên 50 độ", "Giảm xuống 20 độ", "Không đổi", "Tăng lên 100 độ"], 0, "Góc phản xạ r luôn bằng góc tới i nên tăng lên 50°."),
        make_mc(11, "Thông hiểu", "Kính tiềm vọng dùng trên tàu ngầm đơn giản nhất được cấu tạo bởi:", ["Hai gương phẳng đặt song song nghiêng góc 45 độ so với trục ống ngắm", "Một thấu kính hội tụ", "Hai gương cầu lõm", "Một lăng kính tam giác"], 0, "Kính tiềm vọng gồm 2 gương phẳng song song nghiêng 45° phản xạ ánh sáng 2 lần góc 90°."),
        make_mc(12, "Thông hiểu", "Tại sao ban đêm đi trên đường nhựa khô ta nhìn rõ mặt đường, nhưng khi đường ướt sũng nước thì bị chói mắt bởi ánh đèn xe?", ["Vì mặt đường ướt nhẵn bóng gây phản xạ gương làm chùm sáng phản xạ tập trung chiếu thẳng vào mắt người lái", "Vì nước phát sáng", "Vì đèn xe sáng hơn", "Vì đường bị mòn"], 0, "Nước đọng tạo bề mặt nhẵn bóng biến phản xạ khuếch tán thành phản xạ gương gây chói mắt.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất hình học của sự phản xạ ánh sáng:", [
            ("a", "Tia phản xạ, tia tới và pháp tuyến cùng nằm trên một mặt phẳng.", True),
            ("b", "Góc phản xạ luôn luôn bằng góc tới.", True),
            ("c", "Nếu tia tới vuông góc với mặt gương (i = 0°) thì tia phản xạ bật ngược trở lại theo phương cũ.", True),
            ("d", "Nếu góc tới là 90° thì tia sáng sẽ đâm xuyên thẳng qua gương.", False)
        ], "Góc tới 90° nghĩa là tia sáng đi là là sát mặt phẳng gương."),
        make_tf(2, "Thông hiểu", "Về hiện tượng phản xạ khuếch tán trong tự nhiên:", [
            ("a", "Nhờ có phản xạ khuếch tán mà ta có thể đọc được các chữ in trên trang sách từ nhiều góc nhìn khác nhau.", True),
            ("b", "Bức tường quét vôi trắng phản xạ khuếch tán ánh sáng giúp căn phòng sáng đều.", True),
            ("c", "Mặt gương kính vỡ vụn gây phản xạ khuếch tán làm ánh sáng tán xạ lung linh.", True),
            ("d", "Phản xạ khuếch tán chỉ xảy ra trong phòng tối.", False)
        ], "Phản xạ khuếch tán xảy ra ở bất kì nơi nào có ánh sáng chiếu vào bề mặt gồ ghề nhám."),
        make_tf(3, "Vận dụng", "Chiếu tia tới SI lên mặt gương phẳng, góc tạo bởi tia tới SI và tia phản xạ IR là 80 độ:", [
            ("a", "Đường pháp tuyến là đường phân giác của góc tạo bởi tia tới và tia phản xạ.", True),
            ("b", "Góc tới i bằng 40 độ.", True),
            ("c", "Góc phản xạ r bằng 40 độ.", True),
            ("d", "Góc tạo bởi tia tới SI và mặt phẳng gương là 40 độ.", False)
        ], "Góc tạo bởi SI và mặt gương là 90° - 40° = 50°."),
        make_tf(4, "Vận dụng", "Kính tiềm vọng (Periscope) quang học đơn giản:", [
            ("a", "Ánh sáng từ mục tiêu truyền vào gương thứ nhất ở trên cao phản xạ một góc 90 độ xuống dưới.", True),
            ("b", "Gương thứ hai ở dưới nhận tia phản xạ và tiếp tục phản xạ góc 90 độ vào mắt người quan sát.", True),
            ("c", "Hai gương phẳng trong kính tiềm vọng phải đặt nghiêng góc 45 độ so với trục ống ngắm.", True),
            ("d", "Ảnh quan sát được qua kính tiềm vọng bị lộn ngược đầu xuống đất.", False)
        ], "Hai lần phản xạ gương phẳng cho ảnh cùng chiều thẳng đứng giúp quan sát rõ ràng mục tiêu.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Góc tới i = 70 độ. Góc phản xạ bằng bao nhiêu độ?", "70", "r = i = 70 độ."),
        make_sa(2, "Thông hiểu", "Tia tới hợp với pháp tuyến góc 15 độ. Góc phản xạ bằng bao nhiêu độ?", "15", "r = i = 15 độ."),
        make_sa(3, "Vận dụng", "Tia tới hợp với mặt phẳng gương góc 55 độ. Góc tới bằng bao nhiêu độ?", "35", "i = 90 - 55 = 35 độ."),
        make_sa(4, "Vận dụng", "Góc tới bằng 20 độ. Góc tạo bởi tia tới và tia phản xạ bằng bao nhiêu độ?", "40", "20 + 20 = 40 độ."),
        make_sa(5, "Vận dụng cao", "Góc hợp bởi tia tới và tia phản xạ là 110 độ. Góc phản xạ bằng bao nhiêu độ?", "55", "r = 110 / 2 = 55 độ."),
        make_sa(6, "Vận dụng cao", "Giữ nguyên hướng tia tới, quay gương một góc 18 độ. Tia phản xạ quay đi một góc bao nhiêu độ?", "36", "2 × 18 = 36 độ.")
    ],
    "part4": [
        make_vdc(1, "Một tia sáng Mặt Trời chiếu nghiêng hợp với mặt đất nằm ngang một góc 50 độ. Để chiếu tia sáng này theo phương nằm ngang vào trong một hang động tối, người ta dùng một chiếc gương phẳng đặt tại điểm tới. Góc nghiêng của mặt phẳng gương so với phương nằm ngang là bao nhiêu độ?", ["25 độ", "50 độ", "65 độ", "40 độ"], 0, "Góc giữa tia tới và tia phản xạ nằm ngang: 180° - 50° = 130°. Góc tới i = 130° / 2 = 65°. Pháp tuyến hợp với mặt đất góc 65° - 50° = 15°. Mặt gương hợp góc 90° - 65° = 25° so với phương nằm ngang."),
        make_vdc(2, "Hai gương phẳng G1 và G2 đặt hợp với nhau một góc nhọn α = 60 độ, mặt phản xạ quay vào nhau. Chiếu một tia sáng SI song song với gương G2 tới gương G1. Sau khi phản xạ lần thứ nhất trên G1, tia sáng đến đập vào gương G2 rồi phản xạ tiếp thành tia JR. Góc tới i2 trên gương G2 bằng:", ["30 độ", "60 độ", "45 độ", "0 độ"], 0, "Tia SI song song G2 nên góc tới i1 = 30°. Tia phản xạ đập vào G2 với góc tới i2 = 0° (vuông góc với G2) rồi bật thẳng ngược trở lại."),
        make_vdc(3, "Kính vạn hoa (Kaleidoscope) tạo ra những hoa văn rực rỡ biến hóa liên tục nhờ cấu tạo cốt lõi gồm:", ["Ba tấm gương phẳng dài ghép lại thành hình lăng trụ tam giác đều phản xạ ánh sáng nhiều lần qua lại", "Một bóng đèn nhấp nháy", "Hai thấu kính phân kì", "Một quả cầu thủy tinh"], 0, "Hệ 3 gương phẳng nghiêng 60° phản xạ liên tiếp tạo các mẫu hoa văn đối xứng hình học tuyệt đẹp."),
        make_vdc(4, "Một tia sáng chiếu tới mặt gương phẳng nằm ngang với góc tới i = 40 độ. Nếu quay gương quanh trục tới một góc 10 độ làm cho góc tới tăng lên thành 50 độ thì góc hợp bởi tia tới và tia phản xạ mới sẽ tăng thêm bao nhiêu độ?", ["20 độ", "10 độ", "30 độ", "40 độ"], 0, "Góc hợp ban đầu 2i = 80°, góc hợp mới 2i' = 100° => Tăng thêm: 100° - 80° = 20°.")
    ]
}
