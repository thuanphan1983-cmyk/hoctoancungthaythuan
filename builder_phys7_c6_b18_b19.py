# -*- coding: utf-8 -*-
"""
CHƯƠNG VI: TỪ - BÀI 18 & BÀI 19 (6 ĐỀ ĐỘC LẬP 100%)
- phys7_c6_b18: Bài 18: Nam châm (3 đề: test1, test2, test3)
- phys7_c6_b19: Bài 19: Từ trường (3 đề: test1, test2, test3)
Không trùng lặp, không tiền tố "Đề X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

b18_b19_exams = {}

# =========================================================================
# BÀI 18: NAM CHÂM (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b18_b19_exams["phys7_c6_b18_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 18: Nam châm - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b18", "lessonName": "Bài 18: Nam châm",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Nam châm vĩnh cửu có khả năng hút mạnh các vật liệu làm từ chất nào sau đây?", ["Sắt, thép, niken, coban", "Đồng, nhôm", "Vàng, bạc", "Nhựa, gỗ, cao su"], 0, "Nam châm hút các vật liệu từ như sắt, thép, niken, coban."),
        make_mc(2, "Nhận biết", "Mỗi thanh nam châm luôn luôn có bao nhiêu cực từ chính?", ["2 cực (cực Bắc và cực Nam)", "1 cực duy nhất", "3 cực", "4 cực"], 0, "Nam châm luôn có hai cực từ: cực Bắc và cực Nam."),
        make_mc(3, "Nhận biết", "Cực Bắc và cực Nam của nam châm thường được kí hiệu bằng các chữ cái in hoa lần lượt là:", ["N (North) và S (South)", "S và N", "A và B", "P và Q"], 0, "N là North (Bắc), S là South (Nam)."),
        make_mc(4, "Nhận biết", "Khi đưa hai cực cùng tên của hai thanh nam châm lại gần nhau thì chúng sẽ:", ["Đẩy nhau", "Hút nhau", "Không tương tác", "Phát sáng"], 0, "Các cực cùng tên thì đẩy nhau."),
        make_mc(5, "Nhận biết", "Khi đưa hai cực khác tên của hai thanh nam châm lại gần nhau thì chúng sẽ:", ["Hút nhau", "Đẩy nhau", "Không tương tác", "Làm mất từ tính"], 0, "Các cực khác tên thì hút nhau."),
        make_mc(6, "Nhận biết", "Thiết bị dùng để xác định phương hướng trên mặt đất dựa vào từ tính của kim nam châm là:", ["La bàn", "Nhiệt kế", "Tốc kế", "Lực kế"], 0, "La bàn ứng dụng kim nam châm định hướng Bắc - Nam."),
        make_mc(7, "Thông hiểu", "Vị trí nào trên một thanh nam châm thẳng có lực từ hút sắt mạnh nhất?", ["Ở hai đầu cực của thanh nam châm", "Ở chính giữa thanh nam châm", "Ở mọi điểm đều bằng nhau", "Không có vị trí nào"], 0, "Lực từ mạnh nhất tập trung ở hai đầu cực, ở giữa hầu như bằng 0."),
        make_mc(8, "Thông hiểu", "Nếu bẻ gãy đôi một thanh nam châm thẳng thành hai nửa thì mỗi nửa sẽ:", ["Trở thành một nam châm mới hoàn chỉnh có đủ hai cực Bắc và Nam", "Biến thành thanh sắt mất hết từ tính", "Chỉ còn một cực duy nhất", "Nổ tung"], 0, "Mỗi nửa gãy vẫn tạo thành một nam châm mới đầy đủ hai cực Bắc - Nam."),
        make_mc(9, "Thông hiểu", "Kim nam châm tự do khi đứng cân bằng trên mặt đất luôn định hướng theo phương nào?", ["Phương Bắc - Nam địa lí", "Phương Đông - Tây", "Phương thẳng đứng", "Phương ngẫu nhiên"], 0, "Kim nam châm luôn định hướng theo phương Bắc - Nam địa lí."),
        make_mc(10, "Thông hiểu", "Vật nào sau đây KHÔNG BỊ nam châm hút?", ["Một chiếc thìa bằng nhôm", "Một chiếc đinh sắt", "Một chiếc kẹp ghim bằng thép", "Một miếng niken"], 0, "Nhôm không phải là vật liệu từ nên không bị nam châm hút."),
        make_mc(11, "Thông hiểu", "Để phân biệt một thanh sắt non chưa bị nhiễm từ và một thanh nam châm có hình dạng kích thước giống hệt nhau mà không dùng thêm vật dụng khác, người ta có thể:", ["Đưa đầu thanh 1 chạm vào điểm chính giữa của thanh 2, nếu hút mạnh thì thanh 1 là nam châm", "Cân khối lượng", "Đo chiều dài", "Gõ vào nhau"], 0, "Đầu cực nam châm hút mạnh vào phần giữa của thanh sắt non, còn phần giữa nam châm không hút đầu thanh sắt."),
        make_mc(12, "Thông hiểu", "Tại sao người ta thường sơn màu đỏ cho cực Bắc (N) và màu xanh (hoặc trắng) cho cực Nam (S) của nam châm?", ["Để người sử dụng dễ dàng nhận biết và phân biệt chính xác hai cực từ của nam châm", "Để chống gỉ sét", "Để nam châm hút mạnh hơn", "Là màu bắt buộc của kim loại"], 0, "Quy ước màu sơn giúp nhận biết nhanh hai cực từ.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc điểm cơ bản của nam châm vĩnh cửu:", [
            ("a", "Nam châm hút được các vật bằng sắt vụn, đinh thép, bột niken.", True),
            ("b", "Nam châm không hút được các vật bằng đồng đỏ, nhôm, bạc, vàng.", True),
            ("c", "Tồn tại các thanh nam châm đơn cực chỉ có duy nhất một cực Bắc trong tự nhiên.", False),
            ("d", "Lực hút từ của nam châm tác dụng xuyên qua được tấm bìa giấy mỏng hoặc tấm kính.", True)
        ], "Trong tự nhiên không bao giờ tồn tại nam châm đơn cực (từ tích đơn cực)."),
        make_tf(2, "Thông hiểu", "Về tương tác giữa hai nam châm đặt gần nhau:", [
            ("a", "Cực Bắc của nam châm 1 hút cực Nam của nam châm 2.", True),
            ("b", "Cực Nam của nam châm 1 đẩy cực Nam của nam châm 2.", True),
            ("c", "Cực Bắc của nam châm 1 đẩy cực Bắc của nam châm 2.", True),
            ("d", "Hai nam châm luôn luôn hút nhau trong mọi trường hợp đặt cạnh nhau.", False)
        ], "Nếu đặt các cực cùng tên lại gần nhau thì chúng sẽ đẩy nhau."),
        make_tf(3, "Vận dụng", "Thí nghiệm treo một thanh nam châm bằng sợi chỉ mảnh ở giữa để thanh quay tự do:", [
            ("a", "Sau khi dao động, thanh nam châm luôn dừng lại theo hướng Bắc - Nam.", True),
            ("b", "Đầu thanh nam châm chỉ về hướng Bắc địa lí gọi là cực Bắc của nam châm.", True),
            ("c", "Nếu đưa một thanh đồng lại gần thì thanh nam châm sẽ bị hút xoay tít.", False),
            ("d", "Nếu đưa cực Bắc của một nam châm khác lại gần cực Bắc của thanh đang treo thì thanh bị đẩy xoay đi.", True)
        ], "Đồng không có từ tính nên không làm xoay nam châm."),
        make_tf(4, "Vận dụng", "Ứng dụng của nam châm trong đời sống hàng ngày:", [
            ("a", "Miếng đệm từ ở cánh cửa tủ lạnh giúp cửa hít chặt vào thân tủ bảo toàn nhiệt độ.", True),
            ("b", "Nắp hộp bút học sinh có gắn nam châm nhỏ giúp đóng mở nắp hộp dễ dàng.", True),
            ("c", "Bảng từ văn phòng sử dụng các viên nam châm nút nhỏ để đính giữ giấy tờ.", True),
            ("d", "Nam châm vĩnh cửu có thể hút sạch các mảnh vỡ thủy tinh rơi trên sàn nhà.", False)
        ], "Thủy tinh không có từ tính nên không thể dùng nam châm để hút.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Cực Bắc của nam châm được kí hiệu bằng chữ cái in hoa nào?", "N", "Chữ N (North)."),
        make_sa(2, "Thông hiểu", "Cực Nam của nam châm được kí hiệu bằng chữ cái in hoa nào?", "S", "Chữ S (South)."),
        make_sa(3, "Vận dụng", "Khi đưa hai cực Bắc của hai nam châm lại gần nhau, chúng hút nhau hay đẩy nhau?", "Đẩy nhau", "Cùng tên thì đẩy nhau."),
        make_sa(4, "Vận dụng", "Khi đưa cực Bắc của nam châm A lại gần cực Nam của nam châm B, chúng hút nhau hay đẩy nhau?", "Hút nhau", "Khác tên thì hút nhau."),
        make_sa(5, "Vận dụng cao", "Kim la bàn bị lệch khỏi phương Bắc - Nam khi đưa vật nào lại gần? (Thanh sắt hay Thanh gỗ)", "Thanh sắt", "Thanh sắt (hoặc nam châm) tương tác từ làm kim la bàn bị lệch."),
        make_sa(6, "Vận dụng cao", "Một thanh nam châm bị bẻ gãy làm 3 đoạn ngắn. Tổng số cực từ của 3 đoạn ngắn đó là bao nhiêu cực?", "6", "Mỗi đoạn có 2 cực => 3 × 2 = 6 cực.")
    ],
    "part4": [
        make_vdc(1, "Có một chiếc hộp đen kín bên trong chứa một vật bí ẩn. Khi đưa một cực của thanh nam châm lại gần chiếc hộp thì thấy chiếc hộp bị hút lại gần. Khi đảo đầu thanh nam châm và đưa lại gần thì chiếc hộp vẫn tiếp tục bị hút mãnh liệt. Vật chứa bên trong chiếc hộp đen có thể là vật nào sau đây?", ["Một khối sắt non (chưa bị nhiễm từ)", "Một thanh nam châm vĩnh cửu", "Một miếng nhôm", "Một khối vàng"], 0, "Nếu là nam châm thì khi đổi đầu sẽ có một lần bị đẩy. Cả hai lần đều bị hút chứng tỏ vật trong hộp là chất từ tính (sắt non) chưa thành nam châm."),
        make_vdc(2, "Trong phòng thí nghiệm có một thanh kim loại chưa được đánh dấu cực. Khi đưa đầu A của thanh kim loại lại gần cực Bắc của một kim nam châm đang thăng bằng thì thấy cực Bắc của kim nam châm bị đẩy lùi ra xa. Kết luận nào sau đây chắc chắn đúng?", ["Đầu A của thanh kim loại là cực Bắc của một thanh nam châm", "Đầu A chỉ là một thanh sắt thông thường", "Đầu A là cực Nam", "Thanh kim loại bằng nhôm"], 0, "Hiện tượng đẩy nhau là bằng chứng duy nhất và chắc chắn nhất chứng minh vật đó là nam châm và đầu A cùng tên với cực bị đẩy (cực Bắc)."),
        make_vdc(3, "Tại sao khi sản xuất la bàn đi biển, vỏ hộp của chiếc la bàn luôn được làm bằng chất liệu đồng, nhôm hoặc nhựa cao cấp mà tuyệt đối không được làm bằng sắt hay thép?", ["Vì sắt thép có từ tính sẽ làm lệch kim nam châm dẫn đến chỉ sai hướng định vị", "Vì sắt thép quá nặng", "Vì sắt thép đắt tiền hơn", "Vì nhựa trong suốt đẹp hơn"], 0, "Sắt thép gây nhiễu loạn từ trường bên trong la bàn làm kim nam châm chỉ sai."),
        make_vdc(4, "Một người làm rơi một chiếc kim khâu bằng thép nhỏ xíu vào một thảm cỏ rậm rạp. Biện pháp thông minh và nhanh nhất để tìm lại chiếc kim khâu mà không làm đứt tay là:", ["Dùng một thanh nam châm mạnh rà sát trên mặt thảm cỏ để nam châm hút dính chiếc kim thép lên", "Dùng kính lúp soi từng ngọn cỏ", "Tưới nước lên thảm cỏ", "Chờ ban đêm dùng đèn pin soi"], 0, "Kim khâu làm bằng thép có từ tính nên bị nam châm hút dính dễ dàng.")
    ]
}

# --- ĐỀ 2 ---
b18_b19_exams["phys7_c6_b18_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 18: Nam châm - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b18", "lessonName": "Bài 18: Nam châm",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Nam châm hình móng ngựa (hình chữ U) có:", ["Hai cực từ nằm ở hai đầu nhánh của chữ U", "Chỉ một cực ở đáy chữ U", "Không có cực từ", "Bốn cực từ"], 0, "Hai cực từ N và S nằm ở hai đầu nhánh chữ U."),
        make_mc(2, "Nhận biết", "Vật liệu nào sau đây là vật liệu từ bị nam châm hút mạnh?", ["Coban (Cobalt)", "Gỗ thông", "Nhựa mica", "Thủy tinh hữu cơ"], 0, "Coban là chất từ tính mạnh bị nam châm hút."),
        make_mc(3, "Nhận biết", "Để xác định cực của một thanh nam châm bị mờ sơn kí hiệu, ta có thể dùng:", ["Một chiếc la bàn đã biết rõ các cực", "Một chiếc nhiệt kế", "Một thanh nhôm", "Một cốc nước"], 0, "Dùng la bàn: cực Bắc của nam châm sẽ hút cực Nam của kim la bàn."),
        make_mc(4, "Nhận biết", "Khi treo tự do, đầu kim nam châm chỉ về hướng Nam địa lí được gọi là:", ["Cực Nam của kim nam châm", "Cực Bắc của kim nam châm", "Cực Đông", "Cực Tây"], 0, "Đầu chỉ về hướng Nam là cực Nam (S)."),
        make_mc(5, "Nhận biết", "Khi nung nóng một thanh nam châm vĩnh cửu lên nhiệt độ rất cao (trên điểm Curie) thì:", ["Nam châm sẽ bị mất từ tính", "Nam châm hút mạnh hơn", "Nam châm phát nổ", "Nam châm đổi thành nam châm điện"], 0, "Nhiệt độ cao làm xáo trộn chuyển động nhiệt của các nguyên tử làm mất từ tính."),
        make_mc(6, "Nhận biết", "Chất nào sau đây KHÔNG BỊ nam châm hút trong mọi điều kiện?", ["Đồng thau", "Sắt non", "Thép tôi", "Niken"], 0, "Đồng thau (hợp kim đồng - kẽm) không phải vật liệu từ."),
        make_mc(7, "Thông hiểu", "Đặt hai thanh nam châm thẳng trên mặt bàn nhẵn sao cho cực Nam của thanh A đối diện với cực Nam của thanh B. Hiện tượng xảy ra là:", ["Hai thanh nam châm đẩy nhau ra xa", "Hai thanh nam châm dính chặt vào nhau", "Hai thanh quay tròn", "Không có hiện tượng gì"], 0, "Các cực cùng tên (Nam - Nam) đẩy nhau."),
        make_mc(8, "Thông hiểu", "Một chiếc kim may bằng thép sau khi được cọ xát nhiều lần theo một chiều dọc theo thanh nam châm sẽ:", ["Bị nhiễm từ và trở thành một chiếc kim nam châm nhỏ hút được ghim giấy", "Bị nóng chảy", "Bị mất khối lượng", "Biến thành vàng"], 0, "Phương pháp từ hóa: cọ xát làm thép bị nhiễm từ lâu dài thành nam châm."),
        make_mc(9, "Thông hiểu", "Tương tác từ giữa hai nam châm diễn ra thông qua:", ["Từ trường tồn tại xung quanh mỗi nam châm", "Không khí thổi", "Ánh sáng chiếu vào", "Nhiệt độ phòng"], 0, "Từ trường là môi trường truyền tương tác từ."),
        make_mc(10, "Thông hiểu", "Khi một thanh nam châm hút một chiếc đinh sắt thì chiếc đinh sắt cũng:", ["Tác dụng một lực hút trở lại thanh nam châm với độ lớn bằng lực nam châm hút nó", "Đẩy thanh nam châm", "Không tác dụng lực gì", "Làm thanh nam châm mất từ tính"], 0, "Theo định luật III Newton, hai vật tương tác lẫn nhau bằng hai lực trực đối."),
        make_mc(11, "Thông hiểu", "Tại sao đầu mũi của những chiếc tuốc-nơ-vít (tua vít) thợ sửa chữa hay dùng thường có từ tính nhẹ?", ["Để hút dính giữ chặt các ốc vít bằng thép giúp thao tác vặn ốc ở các khe hẹp dễ dàng", "Để dẫn điện tốt hơn", "Để tránh bị mòn", "Để làm đẹp"], 0, "Đầu tua vít có từ tính giữ chặt đinh ốc bằng thép không bị rơi."),
        make_mc(12, "Thông hiểu", "Nếu bẻ một thanh nam châm thành 4 đoạn ngắn thì ta thu được:", ["4 thanh nam châm mới, mỗi thanh có đủ hai cực Bắc - Nam", "2 thanh có cực Bắc và 2 thanh có cực Nam", "Các thanh sắt vụn mất từ tính", "1 thanh nam châm lớn"], 0, "Mỗi đoạn cắt ra đều là một nam châm độc lập có đủ hai cực.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các tính chất đặc trưng của nam châm:", [
            ("a", "Nam châm có khả năng hút các vật làm từ vật liệu từ tính.", True),
            ("b", "Lực từ của nam châm có thể tác dụng từ xa mà không cần tiếp xúc trực tiếp.", True),
            ("c", "Nam châm có thể hút dính được các đồng tiền xu làm hoàn toàn bằng nhôm nguyên chất.", False),
            ("d", "Hai cực cùng tên của nam châm thì đẩy nhau, khác tên thì hút nhau.", True)
        ], "Nhôm không có từ tính nên nam châm không hút."),
        make_tf(2, "Thông hiểu", "Về cấu tạo và hoạt động của chiếc la bàn:", [
            ("a", "Bộ phận cốt lõi của la bàn là một kim nam châm nhỏ có thể quay tự do trên một trục nhọn.", True),
            ("b", "Mặt số của la bàn được chia thành 360 độ và ghi rõ các hướng chính Đông, Tây, Nam, Bắc.", True),
            ("c", "Khi đặt la bàn gần một thanh nam châm mạnh, kim la bàn sẽ chỉ sai lệch hướng Bắc - Nam địa lí.", True),
            ("d", "La bàn chỉ có thể hoạt động chính xác vào ban ngày, ban đêm kim la bàn không quay.", False)
        ], "Từ trường Trái Đất tồn tại liên tục ngày đêm nên la bàn hoạt động chính xác mọi lúc."),
        make_tf(3, "Vận dụng", "Học sinh thực hiện thí nghiệm xác định cực của một thanh nam châm cũ bị mất sơn màu:", [
            ("a", "Treo thanh nam châm bằng sợi chỉ mảnh cho thăng bằng quay tự do trong phòng không có gió.", True),
            ("b", "Khi thanh dừng lại, đầu thanh quay về hướng Bắc địa lí chính là cực Bắc của thanh nam châm.", True),
            ("c", "Đầu thanh quay về hướng Nam địa lí chính là cực Nam của thanh nam châm.", True),
            ("d", "Dù treo thanh ở bất kì vị trí nào cạnh cục sắt to thì thanh luôn chỉ đúng hướng Bắc địa lí.", False)
        ], "Cạnh cục sắt hoặc nam châm khác có từ trường cục bộ làm thanh nam châm bị hút lệch hướng."),
        make_tf(4, "Vận dụng", "Ứng dụng nam châm vĩnh cửu trong thiết bị âm thanh (loa phóng thanh):", [
            ("a", "Bên trong củ loa luôn có một khối nam châm vĩnh cửu hình xuyến mạnh.", True),
            ("b", "Nam châm tương tác với cuộn dây mang dòng điện âm tần làm màng loa rung phát ra âm thanh.", True),
            ("c", "Nếu tháo bỏ khối nam châm ra thì loa vẫn phát ra âm thanh to như cũ.", False),
            ("d", "Lực từ của nam châm vĩnh cửu trong loa không đổi theo thời gian ở điều kiện bình thường.", True)
        ], "Không có nam châm thì không có lực từ làm rung màng loa, loa không phát được âm thanh.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một thanh nam châm có bao nhiêu cực từ chính?", "2", "2 cực (Bắc và Nam)."),
        make_sa(2, "Thông hiểu", "Kim nam châm tự do luôn định hướng theo phương nào? (Trả lời: Bắc - Nam hay Đông - Tây)", "Bắc - Nam", "Phương Bắc - Nam."),
        make_sa(3, "Vận dụng", "Đưa cực Nam lại gần cực Nam của một nam châm khác thì chúng hút nhau hay đẩy nhau?", "Đẩy nhau", "Đẩy nhau."),
        make_sa(4, "Vận dụng", "Đưa cực Nam của thanh nam châm lại gần cực Bắc của kim la bàn, chúng hút nhau hay đẩy nhau?", "Hút nhau", "Khác tên hút nhau."),
        make_sa(5, "Vận dụng cao", "Dùng búa đập mạnh nhiều lần vào thanh nam châm có làm từ tính của nó giảm đi không? (Có hay Không)", "Có", "Va đập cơ học mạnh làm xáo trộn các miền từ khiến từ tính bị suy giảm."),
        make_sa(6, "Vận dụng cao", "Một thanh nam châm bị gãy làm 2 đoạn. Có tất cả bao nhiêu cực Bắc được tạo thành từ 2 đoạn đó?", "2", "Mỗi đoạn có 1 cực Bắc => tổng có 2 cực Bắc.")
    ],
    "part4": [
        make_vdc(1, "Có hai thanh kim loại A và B bề ngoài giống hệt nhau. Một thanh là nam châm vĩnh cửu và một thanh là thép thường. Không dùng thêm bất kì dụng cụ nào khác, phương án tối ưu để xác định thanh nào là nam châm là:", ["Lấy đầu của thanh A chạm vào điểm chính giữa của thanh B. Nếu đầu A hút mạnh thanh B thì thanh A là nam châm, nếu không hút thì thanh B là nam châm", "Gõ hai thanh vào nhau", "Thả rơi hai thanh", "Cọ xát hai thanh"], 0, "Chính giữa thanh nam châm không có từ tính, còn đầu thanh nam châm có từ tính mạnh nhất. Do đó đầu nam châm hút điểm giữa thanh thép, còn đầu thanh thép không bị điểm giữa nam châm hút."),
        make_vdc(2, "Một người làm rơi chiếc nhẫn vàng 18K lẫn trong một đống cát và vụn sắt rỉ sét trên công trường. Người đó dùng một thanh nam châm mạnh rà trên đống cát. Kết quả thu được là gì?", ["Nam châm sẽ hút sạch các vụn sắt rỉ sét ra khỏi đống cát, để lại chiếc nhẫn vàng trong cát giúp người đó tìm thấy dễ dàng", "Nam châm hút dính chiếc nhẫn vàng", "Nam châm hút cát", "Chiếc nhẫn vàng bị biến mất"], 0, "Vàng không bị nam châm hút, còn sắt bị hút sạch ra giúp tách nhẫn vàng dễ dàng."),
        make_vdc(3, "Đặt ba thanh nam châm thẳng 1, 2, 3 nằm thẳng hàng trên mặt bàn nhẵn. Thanh 1 và thanh 2 hút nhau; thanh 2 và thanh 3 đẩy nhau. Nếu cực ngoài cùng bên trái của thanh 1 là cực Bắc thì cực ngoài cùng bên phải của thanh 3 là cực gì?", ["Cực Bắc", "Cực Nam", "Không có cực", "Cả hai cực"], 0, "Thanh 1: [Bắc - Nam]. Vì hút thanh 2 => Thanh 2: [Bắc - Nam]. Vì thanh 2 và 3 đẩy nhau => Thanh 3: [Nam - Bắc] => Cực ngoài cùng bên phải của thanh 3 là cực Bắc."),
        make_vdc(4, "Tại sao các ổ đĩa cứng máy tính truyền thống (HDD), băng từ cát-xét và thẻ ngân hàng lại bị khuyến cáo tuyệt đối không được để gần các cục nam châm vĩnh cửu mạnh?", ["Vì từ trường mạnh của nam châm sẽ làm xáo trộn và xóa sạch các mẫu dữ liệu từ tính nhị phân đã ghi trên bề mặt đĩa từ và thẻ", "Vì nam châm làm nóng chảy đĩa", "Vì nam châm làm thẻ bị đổi màu", "Vì thẻ bị dính chặt không gỡ ra được"], 0, "Từ trường mạnh phá hủy cấu trúc sắp xếp các hạt oxit từ tính mã hóa thông tin.")
    ]
}

# --- ĐỀ 3 ---
b18_b19_exams["phys7_c6_b18_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 18: Nam châm - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b18", "lessonName": "Bài 18: Nam châm",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật nào sau đây có khả năng tương tác hút hoặc đẩy với một thanh nam châm khác?", ["Một thanh nam châm thứ hai", "Một miếng gỗ khô", "Một cốc thủy tinh", "Một cục gôm tẩy"], 0, "Hai nam châm tương tác từ với nhau (hút hoặc đẩy)."),
        make_mc(2, "Nhận biết", "Tên gọi của hai cực từ của nam châm bắt nguồn từ:", ["Khả năng định hướng theo hướng Bắc và hướng Nam của Trái Đất khi để tự do", "Tên nhà bác học phát minh", "Tên các hành tinh", "Màu sắc của sơn"], 0, "Định hướng theo cực Bắc và Nam của Trái Đất."),
        make_mc(3, "Nhận biết", "Vật liệu nào sau đây là vật liệu không có tính từ?", ["Đồng nguyên chất", "Sắt", "Niken", "Thép"], 0, "Đồng là kim loại không có tính từ."),
        make_mc(4, "Nhận biết", "Khi treo lơ lửng một kim nam châm nhỏ thăng bằng thì trục của kim nam châm sẽ trùng với:", ["Hướng Bắc - Nam địa lí", "Hướng Đông - Tây", "Đường xích đạo", "Phương thẳng đứng"], 0, "Trục kim nam châm định hướng theo phương Bắc - Nam."),
        make_mc(5, "Nhận biết", "Trong các trường hợp sau, trường hợp nào xảy ra lực đẩy giữa hai thanh nam châm?", ["Đưa hai cực Nam lại gần nhau", "Đưa cực Bắc lại gần cực Nam", "Đưa cực Nam lại gần cực Bắc", "Đưa nam châm lại gần thanh sắt"], 0, "Cực cùng tên (Nam - Nam) đẩy nhau."),
        make_mc(6, "Nhận biết", "Bột mạt sắt rải đều trên một tờ bìa đặt trên thanh nam châm sẽ bị hút bám dày đặc nhất ở đâu?", ["Ở hai đầu cực của thanh nam châm", "Ở giữa thanh", "Không bị hút", "Rải đều khắp nơi"], 0, "Mạt sắt bám nhiều nhất ở hai đầu cực nơi lực từ mạnh nhất."),
        make_mc(7, "Thông hiểu", "Để bảo quản nam châm vĩnh cửu không bị suy giảm từ tính theo thời gian, người ta thường:", ["Ghép hai cực khác tên của hai thanh nam châm bằng các miếng sắt non đệm ở đầu", "Nung nóng trong lửa", "Dùng búa đập thường xuyên", "Ngâm trong nước muối"], 0, "Dùng thanh sắt non nối hai cực khác tên khép kín mạch từ giúp bảo toàn từ tính."),
        make_mc(8, "Thông hiểu", "Một thanh sắt non được đặt tiếp xúc với cực Bắc của một thanh nam châm thì đầu kia của thanh sắt non sẽ:", ["Trở thành cực Bắc tạm thời và có thể hút được các vụn sắt khác", "Trở thành cực Nam vĩnh viễn", "Mất hết tính chất", "Bị đẩy ra"], 0, "Sắt non bị nhiễm từ tạm thời do hưởng ứng từ, đầu xa mang từ tính cùng tên."),
        make_mc(9, "Thông hiểu", "Một chiếc kim khâu bằng thép khi bị rơi xuống khe sàn gỗ hẹp, dụng cụ tiện lợi nhất để lấy kim lên là:", ["Một thanh nam châm nhỏ buộc vào đầu sợi dây", "Một chiếc đũa tre", "Một chiếc kẹp nhựa", "Một ống hút"], 0, "Nam châm hút kim thép dính chặt kéo lên."),
        make_mc(10, "Thông hiểu", "Vì sao các cánh cửa tủ quần áo cao cấp thường lắp các miếng hít từ (nam châm nhỏ)?", ["Để giữ cánh cửa luôn đóng khép chặt mà không cần chốt khóa cơ học phức tạp", "Để trang trí", "Để làm cửa nhẹ hơn", "Để mở cửa khó hơn"], 0, "Hút giữ cánh cửa êm ái và khép chặt."),
        make_mc(11, "Thông hiểu", "Đặc điểm nào sau đây chứng minh một thanh kim loại ĐÃ BỊ NHIỄM TỪ thành nam châm?", ["Nó có thể đẩy một cực xác định của kim nam châm tự do", "Nó có thể hút chiếc đinh sắt", "Nó có màu xám đen", "Nó dẫn điện tốt"], 0, "Lực đẩy là dấu hiệu duy nhất khẳng định vật đó là nam châm."),
        make_mc(12, "Thông hiểu", "Các hạt mạt sắt dùng trong thí nghiệm từ học được làm từ chất nào?", ["Sắt hoặc thép", "Nhôm", "Đồng", "Than chì"], 0, "Mạt sắt làm từ sắt/thép để nhiễm từ rõ nét.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất từ tính của vật chất:", [
            ("a", "Sắt, thép, coban, niken là các vật liệu có tính chất từ.", True),
            ("b", "Đồng, nhôm, gỗ, cao su là các vật liệu phi từ tính.", True),
            ("c", "Nam châm vĩnh cửu có thể hút được tất cả các kim loại có trong tự nhiên.", False),
            ("d", "Lực từ có thể tác dụng xuyên qua chất lỏng và không khí.", True)
        ], "Nam châm không hút được vàng, bạc, đồng, nhôm, chì..."),
        make_tf(2, "Thông hiểu", "Về các cực từ của nam châm:", [
            ("a", "Mỗi nam châm có ít nhất hai cực từ khác nhau.", True),
            ("b", "Cực Bắc sơn màu đỏ, kí hiệu chữ N.", True),
            ("c", "Cực Nam sơn màu xanh, kí hiệu chữ S.", True),
            ("d", "Hai cực cùng tên thì hút nhau mãnh liệt.", False)
        ], "Cùng tên thì đẩy nhau."),
        make_tf(3, "Vận dụng", "Thí nghiệm nhiễm từ cho một thanh thép và một thanh sắt non:", [
            ("a", "Sau khi cọ xát với nam châm, cả thanh sắt non và thép đều bị nhiễm từ.", True),
            ("b", "Khi đưa ra xa nam châm, thanh sắt non nhanh chóng mất hết từ tính.", True),
            ("c", "Thanh thép giữ được từ tính lâu dài và trở thành nam châm vĩnh cửu.", True),
            ("d", "Sắt non giữ từ tính tốt hơn thép nhiều lần.", False)
        ], "Thép giữ từ tính lâu dài, sắt non khử từ rất nhanh."),
        make_tf(4, "Vận dụng", "Ứng dụng la bàn trong thám hiểm rừng rậm:", [
            ("a", "La bàn giúp xác định phương hướng chính xác khi không nhìn thấy Mặt Trời.", True),
            ("b", "Cần giữ la bàn thăng bằng nằm ngang khi đọc số đo góc.", True),
            ("c", "Nên đặt la bàn cạnh một chiếc dao găm bằng thép lớn khi đo hướng.", False),
            ("d", "Đầu kim sơn đỏ của la bàn chỉ về hướng Bắc.", True)
        ], "Dao găm bằng thép gây lệch kim la bàn, làm sai hướng.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Cực mang kí hiệu chữ S của nam châm là cực gì? (Bắc hay Nam)", "Nam", "Cực Nam (South)."),
        make_sa(2, "Thông hiểu", "Chất liệu sắt non có bị nam châm hút không? (Có hay Không)", "Có", "Có bị hút mạnh."),
        make_sa(3, "Vận dụng", "Hai cực Bắc của hai thanh nam châm để gần nhau sẽ hút hay đẩy?", "Đẩy", "Đẩy nhau."),
        make_sa(4, "Vận dụng", "Cực Bắc của nam châm hút cực nào của kim nam châm khác?", "Nam", "Cực Nam."),
        make_sa(5, "Vận dụng cao", "Một chiếc ghim giấy bằng thép dính vào nam châm có thể hút thêm một chiếc ghim khác không? (Có hay Không)", "Có", "Ghim thép bị nhiễm từ tạm thời nên hút được ghim khác."),
        make_sa(6, "Vận dụng cao", "Vật liệu nào sau đây làm vỏ la bàn: Đồng hay Sắt?", "Đồng", "Đồng (không nhiễm từ, không làm lệch kim la bàn).")
    ],
    "part4": [
        make_vdc(1, "Một đoàn tàu đệm từ Maglev chạy trên đường ray không ma sát nhờ hệ thống nam châm đặt ở gầm tàu và trên đường ray. Nguyên lí lực từ được ứng dụng ở đây là gì?", ["Lực đẩy giữa các cực cùng tên của hệ thống nam châm điện nâng đoàn tàu lơ lửng trên mặt ray", "Lực hút của nam châm kéo tàu xuống", "Lực ma sát cực lớn", "Lực nâng khí động học"], 0, "Lực đẩy từ trường cùng tên nâng đoàn tàu bay lơ lửng cách mặt ray 1 - 2 cm triệt tiêu ma sát lăn."),
        make_vdc(2, "Một người có 3 thanh kim loại giống hệt nhau được đánh số 1, 2, 3. Khi đưa thanh 1 lại gần thanh 2 thì thấy chúng hút nhau. Khi đưa thanh 2 lại gần thanh 3 thì thấy chúng hút nhau. Khi đưa thanh 1 lại gần thanh 3 thì chúng đẩy nhau. Kết luận nào sau đây đúng nhất?", ["Thanh 1 và thanh 3 là hai thanh nam châm, thanh 2 là thanh sắt", "Cả 3 thanh đều là nam châm", "Thanh 1 là sắt, thanh 2 và 3 là nam châm", "Cả 3 thanh đều là sắt"], 0, "1 và 3 đẩy nhau => 1 và 3 chắc chắn là nam châm. Cả 1 và 3 đều hút 2 ở mọi trường hợp => 2 là thanh sắt non."),
        make_vdc(3, "Trong nhà máy tái chế rác thải công nghiệp, để tách các lon nước ngọt làm bằng sắt tây ra khỏi các lon nước ngọt làm bằng nhôm hỗn hợp, người ta sử dụng thiết bị nào sau đây hiệu quả nhất?", ["Một băng chuyền chạy qua một tang trống từ tính (nam châm cực mạnh)", "Dùng quạt thổi gió", "Dùng sàng rung", "Dùng nước ngâm"], 0, "Tang trống từ tính hút giữ các lon sắt lại, còn lon nhôm không nhiễm từ rơi tự do ra ngoài giúp phân loại tự động."),
        make_vdc(4, "Một thanh nam châm thẳng được đặt trên một chiếc đĩa xốp nhẹ thả nổi trên chậu nước rộng. Khi đĩa xốp đứng yên thăng bằng, thanh nam châm sẽ nằm theo hướng nào?", ["Trục thanh nam châm nằm theo hướng Bắc - Nam địa lí", "Nằm theo hướng Đông - Tây", "Quay tròn liên tục", "Chìm xuống đáy"], 0, "Đĩa xốp nổi giúp nam châm quay tự do như kim la bàn định hướng Bắc - Nam theo từ trường Trái Đất.")
    ]
}

# =========================================================================
# BÀI 19: TỪ TRƯỜNG (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b18_b19_exams["phys7_c6_b19_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 19: Từ trường - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b19", "lessonName": "Bài 19: Từ trường",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Không gian xung quanh nam châm hoặc xung quanh dòng điện có tồn tại một dạng vật chất gọi là:", ["Từ trường", "Điện trường tĩnh", "Ánh sáng", "Nhiệt trường"], 0, "Xung quanh nam châm hoặc dòng điện có từ trường."),
        make_mc(2, "Nhận biết", "Dụng cụ dùng để nhận biết sự tồn tại của từ trường trong một vùng không gian là:", ["Kim nam châm (nam châm thử)", "Nhiệt kế", "Vôn kế", "Thước đo"], 0, "Kim nam châm thử bị lệch hướng khi đặt trong từ trường."),
        make_mc(3, "Nhận biết", "Hình ảnh các đường mạt sắt sắp xếp trật tự xung quanh nam châm được gọi là:", ["Từ phổ", "Quang phổ", "Bản đồ nhiệt", "Sóng âm"], 0, "Từ phổ là hình ảnh các đường mạt sắt xung quanh nam châm."),
        make_mc(4, "Nhận biết", "Quy ước chiều của đường sức từ ở bên ngoài thanh nam châm thẳng đi:", ["Ra từ cực Bắc (N), đi vào ở cực Nam (S)", "Ra từ cực Nam, đi vào ở cực Bắc", "Từ cực Đông sang cực Tây", "Từ dưới lên trên"], 0, "Quy ước chiều đường sức từ: 'Vào Nam Ra Bắc'."),
        make_mc(5, "Nhận biết", "Nơi nào có từ trường mạnh thì các đường sức từ ở đó sẽ:", ["Dày (mau) hơn", "Thưa hơn", "Thẳng tắp", "Biến mất"], 0, "Từ trường mạnh thì đường sức từ mau (dày đặc)."),
        make_mc(6, "Nhận biết", "Trái Đất của chúng ta hoạt động như một nam châm khổng lồ với cực từ nam nằm ở gần:", ["Cực Bắc địa lí của Trái Đất", "Cực Nam địa lí của Trái Đất", "Đường xích đạo", "Tâm Trái Đất"], 0, "Cực từ nam của Trái Đất nằm ở vùng cực Bắc địa lí (do đó cực Bắc la bàn bị hút về cực Bắc địa lí)."),
        make_mc(7, "Thông hiểu", "Thí nghiệm lịch sử của nhà bác học Đan Mạch Oersted (Ơ-xtét) năm 1820 đã chứng minh:", ["Xung quanh dòng điện có từ trường tác dụng lực từ làm lệch kim nam châm", "Dòng điện phát ra ánh sáng", "Nam châm phát ra điện", "Dòng điện có nhiệt độ"], 0, "Thí nghiệm Oersted phát hiện tác dụng từ của dòng điện."),
        make_mc(8, "Thông hiểu", "Các đường sức từ có đặc điểm hình học nào sau đây?", ["Là các đường cong khép kín không bao giờ cắt nhau", "Là các đoạn thẳng hở", "Là các đường tròn đồng tâm cắt nhau", "Là các đường xoắn ốc cắt nhau liên tục"], 0, "Đường sức từ là các đường cong khép kín không cắt nhau."),
        make_mc(9, "Thông hiểu", "Hiện tượng Cực quang (Aurora) rực rỡ xuất hiện trên bầu trời hai vùng cực Trái Đất là kết quả của:", ["Sự tương tác giữa các hạt mang điện từ gió Mặt Trời bị từ trường Trái Đất bẫy tương tác với khí quyển", "Ánh sáng phản chiếu từ băng tuyết", "Pháo hoa vũ trụ", "Đèn chiếu sáng"], 0, "Gió Mặt Trời tương tác với từ trường Trái Đất sinh ra cực quang."),
        make_mc(10, "Thông hiểu", "Tại sao từ trường Trái Đất lại có ý nghĩa sinh tử đối với sự sống của sinh quyển?", ["Che chắn các luồng bức xạ hạt vũ trụ năng lượng cao nguy hiểm từ gió Mặt Trời", "Làm cho Trái Đất ấm lên", "Tạo ra oxy", "Tạo ra mưa rơi"], 0, "Từ quyển Trái Đất là lá chắn bảo vệ sinh quyển khỏi bức xạ hạt nguy hiểm."),
        make_mc(11, "Thông hiểu", "Khi đặt một kim nam châm nhỏ trong từ trường của một thanh nam châm, kim nam châm sẽ:", ["Định hướng theo phương của đường sức từ tại điểm đó", "Quay tròn liên tục không ngừng", "Bị rơi xuống đất", "Mất hết từ tính"], 0, "Kim nam châm định hướng dọc theo đường sức từ tại điểm đặt."),
        make_mc(12, "Thông hiểu", "Nếu hai đường sức từ cắt nhau tại một điểm trong không gian thì tại điểm đó:", ["Kim nam châm thử sẽ chỉ hai hướng khác nhau cùng lúc (điều này vô lí, chứng tỏ các đường sức từ không bao giờ cắt nhau)", "Kim nam châm đứng yên", "Từ trường bằng 0", "Nam châm phát nổ"], 0, "Tại mỗi điểm từ trường chỉ có một hướng duy nhất nên đường sức từ không cắt nhau.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất và tính chất của từ trường:", [
            ("a", "Từ trường tồn tại xung quanh nam châm vĩnh cửu.", True),
            ("b", "Từ trường tồn tại xung quanh dây dẫn có dòng điện chạy qua.", True),
            ("c", "Từ trường tác dụng lực từ lên kim nam châm đặt trong nó.", True),
            ("d", "Mắt người có thể trực tiếp nhìn thấy các đường từ trường trong không khí.", False)
        ], "Từ trường là trường vật chất vô hình, mắt không nhìn thấy được."),
        make_tf(2, "Thông hiểu", "Về hình ảnh đường sức từ và từ phổ:", [
            ("a", "Rắc mạt sắt lên tấm nhựa đặt trên nam châm rồi gõ nhẹ ta thu được từ phổ.", True),
            ("b", "Đường sức từ có hướng đi ra từ cực Bắc và đi vào ở cực Nam bên ngoài nam châm.", True),
            ("c", "Ở gần hai đầu cực của nam châm, các đường sức từ rất dày đặc chứng tỏ từ trường rất mạnh.", True),
            ("d", "Ở càng xa nam châm, các đường sức từ càng mau hơn.", False)
        ], "Càng xa nam châm thì từ trường càng yếu nên đường sức từ càng thưa thớt."),
        make_tf(3, "Vận dụng", "Thí nghiệm Oersted về tác dụng từ của dòng điện:", [
            ("a", "Đặt một dây dẫn thẳng song song với trục của một kim nam châm đang thăng bằng.", True),
            ("b", "Khi chưa đóng công tắc điện, kim nam châm chỉ phương Bắc - Nam.", True),
            ("c", "Khi đóng công tắc cho dòng điện chạy qua dây dẫn, kim nam châm bị lệch khỏi vị trí cân bằng.", True),
            ("d", "Nếu ngắt dòng điện thì kim nam châm vẫn bị lệch mãi không quay về vị trí ban đầu.", False)
        ], "Ngắt dòng điện thì từ trường của dây dẫn mất đi, kim nam châm quay về phương Bắc - Nam của Trái Đất."),
        make_tf(4, "Vận dụng", "Từ trường của Trái Đất (địa từ trường):", [
            ("a", "Bắc cực từ của Trái Đất nằm ở vùng Nam cực địa lí.", True),
            ("b", "Nam cực từ của Trái Đất nằm ở vùng Bắc cực địa lí.", True),
            ("c", "Cực Bắc của kim la bàn bị hút về phía cực từ nam của Trái Đất (ở phương Bắc địa lí).", True),
            ("d", "Bão từ Mặt Trời hoàn toàn không ảnh hưởng gì đến mạng lưới truyền tải điện trên Trái Đất.", False)
        ], "Bão từ mạnh có thể làm sập lưới điện và làm gián đoạn thông tin liên lạc vệ tinh.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Chiều đường sức từ ở bên ngoài thanh nam châm đi ra ở cực nào? (Bắc hay Nam)", "Bắc", "Ra Bắc vào Nam."),
        make_sa(2, "Thông hiểu", "Chiều đường sức từ ở bên ngoài thanh nam châm đi vào ở cực nào? (Bắc hay Nam)", "Nam", "Đi vào ở cực Nam."),
        make_sa(3, "Vận dụng", "Xung quanh một dây dẫn có dòng điện chạy qua có tồn tại từ trường không? (Có hay Không)", "Có", "Có từ trường (thí nghiệm Oersted)."),
        make_sa(4, "Vận dụng", "Hình ảnh các đường mạt sắt xung quanh nam châm được gọi là gì?", "Từ phổ", "Từ phổ."),
        make_sa(5, "Vận dụng cao", "Nơi có từ trường mạnh thì các đường sức từ dày hay thưa?", "Dày", "Dày (mau)."),
        make_sa(6, "Vận dụng cao", "Hiện tượng dải ánh sáng rực rỡ trên bầu trời đêm vùng cực Trái Đất gọi là gì?", "Cực quang", "Hiện tượng Cực quang (Aurora).")
    ],
    "part4": [
        make_vdc(1, "Tại sao khi một cơn bão từ (Geomagnetic storm) do các đợt bùng nổ bức xạ từ Mặt Trời quét qua Trái Đất, các thiết bị định vị GPS, sóng viễn thông vệ tinh và la bàn của tàu thuyền lại bị nhiễu loạn nghiêm trọng?", ["Vì các hạt mang điện năng lượng cao từ gió Mặt Trời làm biến dạng mạnh mẽ từ trường Trái Đất, gây ra sự dao động hỗn loạn của kim la bàn và cản trở sóng điện từ", "Vì không khí bị bốc cháy", "Vì nước biển sôi lên", "Vì Trái Đất ngừng quay"], 0, "Bão từ làm biến dạng địa từ trường và ion hóa mạnh tầng điện li gây gián đoạn sóng vô tuyến."),
        make_vdc(2, "Một đoạn dây dẫn thẳng AB đặt theo phương nằm ngang có dòng điện một chiều không đổi chạy qua từ A sang B. Đặt một kim nam châm thử nhỏ ngay phía dưới dây dẫn. Khi dòng điện chạy qua, kim nam châm bị lệch góc 45 độ so với trục dây. Nếu đảo chiều dòng điện từ B sang A thì kim nam châm sẽ:", ["Lệch theo chiều ngược lại so với ban đầu", "Vẫn lệch theo chiều cũ", "Không bị lệch nữa", "Quay tròn liên tục"], 0, "Đảo chiều dòng điện làm đảo chiều từ trường sinh ra xung quanh dây dẫn, do đó kim nam châm lệch theo chiều ngược lại."),
        make_vdc(3, "Nhiều loài chim di cư (như bồ câu, nhạn biển, ngỗng trời) và loài rùa biển có thể bay và bơi hàng nghìn kilômét xuyên lục địa và đại dương về đúng nơi sinh sản mà không bao giờ bị lạc đường. Khả năng định vị phi thường này chủ yếu dựa vào:", ["Cơ quan cảm ứng từ sinh học nhạy cảm bên trong cơ thể giúp chúng cảm nhận được từ trường Trái Đất như một chiếc la bàn tự nhiên", "Chúng nhớ từng cái cây", "Chúng ngửi mùi gió", "Chúng bay theo đàn đông"], 0, "Các hạt tinh thể magnetit sinh học trong cơ thể chim và rùa biển hoạt động như la bàn sinh học định hướng theo địa từ trường."),
        make_vdc(4, "Người ta rải mạt sắt lên một tấm kính đặt trên hai cực của một nam châm hình chữ U rồi gõ nhẹ. Kết quả quan sát thấy ở khoảng không gian giữa hai nhánh cực của nam châm hình chữ U, các đường mạt sắt là:", ["Các đường thẳng song song và cách đều nhau (từ trường đều)", "Các vòng tròn đồng tâm", "Các đường zích zắc", "Các đám mạt sắt dồn vào một điểm"], 0, "Trong lòng khoảng không giữa hai cực nam châm chữ U là từ trường đều, các đường sức từ song song cách đều nhau.")
    ]
}

# --- ĐỀ 2 ---
b18_b19_exams["phys7_c6_b19_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 19: Từ trường - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b19", "lessonName": "Bài 19: Từ trường",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Tính chất cơ bản của từ trường là:", ["Tác dụng lực từ lên kim nam châm đặt trong nó", "Làm nóng các vật", "Phát ra ánh sáng huỳnh quang", "Hút mọi vật bằng nhựa"], 0, "Tác dụng lực từ lên nam châm là đặc tính cơ bản của từ trường."),
        make_mc(2, "Nhận biết", "Để vẽ đường sức từ của một nam châm, người ta dựa vào:", ["Hình ảnh các đường mạt sắt trong từ phổ", "Các tia sáng", "Hướng của gió", "Đường dây điện"], 0, "Đường sức từ mô phỏng từ phổ mạt sắt."),
        make_mc(3, "Nhận biết", "Quy tắc xác định chiều đường sức từ bên ngoài thanh nam châm là:", ["Vào cực Nam, Ra cực Bắc", "Vào cực Bắc, Ra cực Nam", "Đi từ trong ra ngoài", "Đi từ dưới lên trên"], 0, "Chiều đường sức từ: 'Vào Nam Ra Bắc'."),
        make_mc(4, "Nhận biết", "Nhà bác học nào đã phát hiện ra hiện tượng dòng điện tác dụng lực từ lên kim nam châm vào năm 1820?", ["Oersted (Ơ-xtét)", "Newton", "Galileo", "Faraday"], 0, "Oersted phát hiện tác dụng từ của dòng điện năm 1820."),
        make_mc(5, "Nhận biết", "Tại một điểm trong không gian, hướng của từ trường là hướng:", ["Nam - Bắc của kim nam châm thử nằm cân bằng tại điểm đó", "Đông - Tây của kim nam châm", "Thẳng đứng", "Tùy ý"], 0, "Hướng từ trường là hướng Nam - Bắc của kim nam châm thử cân bằng."),
        make_mc(6, "Nhận biết", "Cực Bắc của kim la bàn định hướng về phía cực Bắc địa lí của Trái Đất là vì:", ["Ở gần cực Bắc địa lí có cực từ Nam của Trái Đất hút cực Bắc của kim la bàn", "Ở cực Bắc có nhiều băng tuyết", "Ở cực Bắc lạnh hơn", "Trái Đất quay quanh trục"], 0, "Khác tên hút nhau: cực từ Nam của Trái Đất hút cực Bắc của kim la bàn."),
        make_mc(7, "Thông hiểu", "Khi đưa kim nam châm thử lại gần một cuộn dây đang có dòng điện chạy qua, hiện tượng gì xảy ra?", ["Kim nam châm bị quay lệch khỏi phương Bắc - Nam ban đầu", "Kim nam châm đứng yên", "Kim nam châm bị nóng chảy", "Không có hiện tượng gì"], 0, "Từ trường của dòng điện tác dụng lực từ làm quay kim nam châm."),
        make_mc(8, "Thông hiểu", "Đặc điểm nào sau đây của đường sức từ là ĐÚNG?", ["Mỗi điểm trong từ trường chỉ có một đường sức từ đi qua", "Các đường sức từ có thể cắt nhau", "Đường sức từ xuất phát từ cực Nam", "Đường sức từ là các đường thẳng hở"], 0, "Mỗi điểm chỉ có 1 đường sức từ đi qua, các đường không cắt nhau."),
        make_mc(9, "Thông hiểu", "Ở hai cực của nam châm chữ U, các đường sức từ:", ["Dày đặc và khép kín nối cực Bắc sang cực Nam", "Thưa thớt nhất", "Không đi qua hai cực", "Song song với thân nam châm"], 0, "Ở hai cực từ trường mạnh nhất nên đường sức từ tập trung dày đặc nhất."),
        make_mc(10, "Thông hiểu", "Trái Đất có từ trường bao quanh tạo thành một vùng không gian bảo vệ gọi là:", ["Từ quyển", "Khí quyển", "Thủy quyển", "Sinh quyển"], 0, "Từ quyển (Magnetosphere) bảo vệ Trái Đất."),
        make_mc(11, "Thông hiểu", "Nếu ngắt dòng điện chạy qua dây dẫn thì từ trường xung quanh dây dẫn sẽ:", ["Biến mất hoàn toàn", "Tồn tại vĩnh viễn", "Mạnh lên gấp đôi", "Đổi màu"], 0, "Ngắt điện thì từ trường của dòng điện lập tức biến mất."),
        make_mc(12, "Thông hiểu", "Tại sao các đường sức từ không bao giờ cắt nhau?", ["Vì tại mỗi điểm trong từ trường, lực từ chỉ có một phương và một chiều xác định duy nhất", "Vì chúng rất thẳng", "Vì chúng bằng kim loại", "Vì chúng quá ngắn"], 0, "Từ trường tại mỗi điểm chỉ có một vectơ cảm ứng từ duy nhất xác định.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về không gian có từ trường:", [
            ("a", "Từ trường tồn tại xung quanh thanh nam châm thẳng.", True),
            ("b", "Từ trường tồn tại xung quanh chiếc còi xe máy khi đang bấm còi có điện.", True),
            ("c", "Xung quanh một cục pin đặt trên bàn chưa nối mạch điện có từ trường rất mạnh.", False),
            ("d", "Xung quanh dây dẫn có dòng điện chạy qua có từ trường.", True)
        ], "Cục pin chưa nối mạch (không có dòng điện chạy) thì không sinh ra từ trường xung quanh."),
        make_tf(2, "Thông hiểu", "Về quy ước chiều và hình dạng của đường sức từ:", [
            ("a", "Đường sức từ là các đường cong có hướng.", True),
            ("b", "Bên ngoài nam châm, chiều đường sức từ đi ra từ cực Bắc và đi vào ở cực Nam.", True),
            ("c", "Bên trong lòng thanh nam châm, chiều đường sức từ đi từ cực Nam sang cực Bắc tạo thành vòng khép kín.", True),
            ("d", "Các đường sức từ là những đường thẳng hở xuất phát từ vô cực.", False)
        ], "Đường sức từ là các đường cong khép kín hoàn chỉnh."),
        make_tf(3, "Vận dụng", "Khảo sát từ phổ của một nam châm thẳng bằng mạt sắt:", [
            ("a", "Mạt sắt sau khi gõ nhẹ sẽ bị nhiễm từ trở thành các kim nam châm nhỏ.", True),
            ("b", "Các mạt sắt tự sắp xếp nối đuôi nhau thành các đường cong cong nối hai cực.", True),
            ("c", "Mật độ các đường mạt sắt dày nhất ở hai đầu cực thanh nam châm.", True),
            ("d", "Nếu thay mạt sắt bằng mạt nhôm mịn thì cũng thu được hình ảnh từ phổ y hệt.", False)
        ], "Nhôm không phải chất từ tính nên không bị nhiễm từ và không sắp xếp thành từ phổ."),
        make_tf(4, "Vận dụng", "Ứng dụng từ trường Trái Đất trong việc sử dụng la bàn quân sự:", [
            ("a", "La bàn giúp chiến sĩ hành quân xác định mục tiêu trong đêm tối.", True),
            ("b", "Khi sử dụng la bàn cần tránh xa các xe bọc thép, súng pháo và đường dây điện cao thế.", True),
            ("c", "Khối thép lớn của xe tăng sẽ làm kim la bàn bị lệch hướng nghiêm trọng.", True),
            ("d", "La bàn quân sự hoạt động tốt nhất khi đặt trực tiếp lên nắp hầm sắt thép.", False)
        ], "Đặt lên nắp hầm bằng sắt sẽ làm kim la bàn bị hút lệch hoàn toàn.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Từ trường tác dụng lực gì lên kim nam châm đặt trong nó?", "Lực từ", "Lực từ."),
        make_sa(2, "Thông hiểu", "Tên nhà bác học người Đan Mạch làm thí nghiệm dòng điện làm lệch kim nam châm năm 1820 là ai?", "Oersted", "Ơ-xtét (Oersted)."),
        make_sa(3, "Vận dụng", "Bên ngoài nam châm, đường sức từ đi ra ở cực nào?", "Bắc", "Cực Bắc."),
        make_sa(4, "Vận dụng", "Bên ngoài nam châm, đường sức từ đi vào ở cực nào?", "Nam", "Cực Nam."),
        make_sa(5, "Vận dụng cao", "Các đường sức từ có cắt nhau tại điểm nào không? (Có hay Không)", "Không", "Không bao giờ cắt nhau."),
        make_sa(6, "Vận dụng cao", "Vùng không gian bảo vệ bao quanh Trái Đất do từ trường tạo nên gọi là gì?", "Từ quyển", "Từ quyển (Magnetosphere).")
    ],
    "part4": [
        make_vdc(1, "Một sợi dây dẫn điện thẳng dài được chôn ngầm dưới lớp vữa của bức tường trong phòng. Để xác định chính xác vị trí sợi dây điện ngầm có dòng điện đang chạy qua mà không cần đục phá tường, người thợ điện có thể làm gì?", ["Cầm một chiếc la bàn nhạy rà sát bề mặt tường, nơi nào kim la bàn bị lệch hướng mạnh nhất thì nơi đó có dây điện ngầm", "Dùng kính lúp soi tường", "Dùng búa gõ vào tường", "Dùng nhiệt kế đo tường"], 0, "Từ trường của dòng điện chạy trong dây dẫn ngầm sẽ tác dụng lực từ làm lệch kim la bàn khi rà sát."),
        make_vdc(2, "Đặt hai thanh nam châm thẳng nằm thẳng hàng trên mặt bàn nhẵn sao cho hai cực Bắc quay vào nhau và cách nhau 5 cm. Rải mạt sắt lên tấm nhựa đặt phía trên hai cực và gõ nhẹ. Từ phổ quan sát được ở khoảng giữa hai cực Bắc có đặc điểm gì?", ["Các đường mạt sắt bị bẻ cong tẽ ra hai bên và ở chính giữa có một điểm hoàn toàn không có mạt sắt bám (điểm trung hòa từ trường)", "Các đường mạt sắt nối thẳng giữa hai cực", "Mạt sắt dồn hết vào giữa", "Không có mạt sắt nào"], 0, "Hai cực cùng tên đẩy nhau tạo điểm trung hòa từ trường ở chính giữa, các đường sức từ tẽ cong ra ngoài không giao nhau."),
        make_vdc(3, "Trạm vũ trụ quốc tế ISS bay quanh Trái Đất ở độ cao khoảng 400 km. Các phi hành gia trên trạm ISS vẫn được bảo vệ tương đối an toàn khỏi các bức xạ hạt nguy hiểm từ bão mặt trời là nhờ:", ["Trạm ISS vẫn nằm trong phạm vi che chắn của từ quyển Trái Đất", "Trạm ISS có vỏ giáp dày 1 mét", "Không gian quanh ISS không có bức xạ", "ISS bay rất nhanh"], 0, "Từ quyển Trái Đất mở rộng ra không gian hàng chục nghìn kilômét, bao trùm và che chở trạm ISS."),
        make_vdc(4, "Một kim nam châm nhỏ thăng bằng trên trục nhọn. Người ta đưa một dây dẫn thẳng có dòng điện chạy qua đặt song song phía trên kim nam châm. Hiện tượng gì sẽ xảy ra nếu ta ngắt công tắc điện rồi lại đóng công tắc điện liên tục theo chu kì 1 giây?", ["Kim nam châm sẽ dao động lắc qua lắc lại liên tục quanh trục thăng bằng", "Kim nam châm đứng yên", "Kim nam châm bị bay lên trần nhà", "Kim nam châm bị mất từ tính"], 0, "Đóng ngắt điện liên tục tạo ra từ trường biến thiên ngắt quãng tác dụng lực từ gián đoạn làm kim nam châm dao động lắc liên tục.")
    ]
}

# --- ĐỀ 3 ---
b18_b19_exams["phys7_c6_b19_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 19: Từ trường - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b19", "lessonName": "Bài 19: Từ trường",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Từ trường là môi trường vật chất đặc biệt tồn tại xung quanh:", ["Nam châm và dòng điện", "Các vật đứng yên bằng gỗ", "Cục than đá", "Bình chứa nước"], 0, "Xung quanh nam châm và dòng điện có từ trường."),
        make_mc(2, "Nhận biết", "Để phát hiện từ trường trong một căn phòng, dụng cụ đơn giản và hiệu quả nhất là:", ["Kim nam châm thử", "Nhiệt kế thủy ngân", "Thước dây", "Cân đồng hồ"], 0, "Kim nam châm thử nhạy cảm với từ trường."),
        make_mc(3, "Nhận biết", "Các đường sức từ có chiều quy ước ở ngoài thanh nam châm là:", ["Đi ra từ cực Bắc và đi vào ở cực Nam", "Đi ra từ cực Nam và đi vào ở cực Bắc", "Đi từ Đông sang Tây", "Không có chiều"], 0, "Quy ước: Ra Bắc Vào Nam."),
        make_mc(4, "Nhận biết", "Tại vị trí nào xung quanh nam châm thì đường sức từ có mật độ dày đặc nhất?", ["Gần hai cực từ của nam châm", "Ở rất xa nam châm", "Ở chính giữa thanh nam châm", "Ở phía trên cao"], 0, "Hai đầu cực có từ trường mạnh nhất nên đường sức từ dày đặc nhất."),
        make_mc(5, "Nhận biết", "Hiện tượng mạt sắt sắp xếp thành các đường cong nối hai cực của nam châm gọi là:", ["Từ phổ", "Quang phổ", "Nhiệt phổ", "Âm phổ"], 0, "Hình ảnh mạt sắt sắp xếp gọi là từ phổ."),
        make_mc(6, "Nhận biết", "Bên ngoài Trái Đất, từ trường mở rộng ra không gian bao quanh địa cầu tạo thành:", ["Từ quyển Trái Đất", "Tầng ozon", "Khí quyển", "Tầng đối lưu"], 0, "Từ quyển (Magnetosphere)."),
        make_mc(7, "Thông hiểu", "Thí nghiệm Oersted phát hiện mối liên hệ chặt chẽ giữa hai hiện tượng nào trong tự nhiên?", ["Hiện tượng điện và hiện tượng từ", "Hiện tượng điện và nhiệt", "Hiện tượng quang và âm", "Hiện tượng cơ và hóa"], 0, "Thí nghiệm Oersted mở đầu cho thuyết điện từ học (mối liên hệ giữa điện và từ)."),
        make_mc(8, "Thông hiểu", "Đường sức từ của nam châm chữ U trong khoảng không gian giữa hai nhánh cực là:", ["Các đường thẳng song song cách đều nhau", "Các vòng tròn đồng tâm", "Các đường cong ngoằn ngoèo", "Các đường xoắn ốc"], 0, "Từ trường đều giữa hai cực gồm các đường thẳng song song cách đều."),
        make_mc(9, "Thông hiểu", "Cực từ bắc của Trái Đất nằm ở:", ["Gần cực Nam địa lí của Trái Đất", "Gần cực Bắc địa lí", "Đường xích đạo", "Tâm địa cầu"], 0, "Cực từ bắc của Trái Đất nằm ở vùng cực Nam địa lí."),
        make_mc(10, "Thông hiểu", "Vì sao các phi hành gia ngoài không gian khi đáp xuống Mặt Trăng lại không thể dùng la ban từ để định hướng?", ["Vì Mặt Trăng không có từ trường toàn cầu mạnh như Trái Đất", "Vì Mặt Trăng quá nóng", "Vì la bàn bị nặng", "Vì không có oxy"], 0, "Mặt Trăng không có từ trường địa cầu mạnh nên kim la bàn không định hướng được."),
        make_mc(11, "Thông hiểu", "Một kim nam châm nhỏ tự do đặt trong từ trường sẽ luôn nằm theo phương:", ["Tiếp tuyến với đường sức từ tại điểm đó", "Vuông góc với đường sức từ", "Hợp góc 45 độ với đường sức từ", "Thẳng đứng lên trời"], 0, "Trục kim nam châm trùng với tiếp tuyến của đường sức từ tại điểm đặt."),
        make_mc(12, "Thông hiểu", "Nếu bẻ cong một thanh nam châm thẳng thành hình chữ U thì từ trường ở khoảng giữa hai đầu cực sẽ:", ["Mạnh hơn nhiều so với khi để thẳng", "Bị biến mất hoàn toàn", "Yếu đi", "Không đổi"], 0, "Uốn cong hai cực lại gần nhau làm từ trường ở khe hở cực kỳ mạnh và tập trung.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các đặc trưng hình học của đường sức từ:", [
            ("a", "Đường sức từ là những đường cong khép kín kín hoàn chỉnh.", True),
            ("b", "Các đường sức từ tuyệt đối không bao giờ cắt nhau.", True),
            ("c", "Nơi từ trường yếu thì các đường sức từ sắp xếp thưa thớt.", True),
            ("d", "Bên ngoài nam châm, đường sức từ đi ra từ cực Nam và đi vào cực Bắc.", False)
        ], "Quy ước bên ngoài: đi ra ở cực Bắc và đi vào ở cực Nam."),
        make_tf(2, "Thông hiểu", "Về thí nghiệm đặt kim nam châm cạnh dây dẫn có dòng điện:", [
            ("a", "Dòng điện sinh ra từ trường tác dụng lực từ làm quay kim nam châm.", True),
            ("b", "Khi đổi chiều dòng điện thì chiều quay của kim nam châm cũng bị đổi ngược lại.", True),
            ("c", "Dòng điện càng lớn thì lực từ tác dụng lên kim nam châm càng mạnh.", True),
            ("d", "Thí nghiệm này chứng minh dòng điện phát ra sóng ánh sáng nhìn thấy.", False)
        ], "Thí nghiệm chứng minh dòng điện sinh ra từ trường, không liên quan ánh sáng phát ra."),
        make_tf(3, "Vận dụng", "Khảo sát từ phổ của hai thanh nam châm đặt khác tên gần nhau (Bắc đối diện Nam):", [
            ("a", "Các đường mạt sắt nối liền giữa cực Bắc của thanh này sang cực Nam của thanh kia.", True),
            ("b", "Mật độ mạt sắt giữa hai cực rất dày đặc chứng tỏ lực hút rất mạnh.", True),
            ("c", "Hai thanh nam châm hút chặt vào nhau nếu để tự do.", True),
            ("d", "Các đường mạt sắt bị bẻ cong tẽ ra xa không nối nhau.", False)
        ], "Khác tên hút nhau nên các đường mạt sắt nối liền liên tục giữa hai cực."),
        make_tf(4, "Vận dụng", "Từ trường Trái Đất và tác dụng bảo vệ sinh quyển:", [
            ("a", "Lõi nóng chảy của Trái Đất quay tạo ra địa từ trường khổng lồ.", True),
            ("b", "Từ trường làm lệch hướng các hạt mang điện năng lượng cao từ gió Mặt Trời.", True),
            ("c", "Cực quang là dấu hiệu thị giác của sự tương tác bão từ tại hai cực Trái Đất.", True),
            ("d", "Nếu Trái Đất mất hoàn toàn từ trường thì bầu khí quyển vẫn không bị ảnh hưởng gì.", False)
        ], "Nếu mất từ trường, gió Mặt Trời sẽ thổi bay khí quyển như đã từng xảy ra với Sao Hỏa.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Vùng không gian xung quanh dòng điện có tồn tại từ trường không? (Có hay Không)", "Có", "Có từ trường."),
        make_sa(2, "Thông hiểu", "Đường sức từ bên ngoài thanh nam châm đi ra ở cực nào?", "Bắc", "Cực Bắc."),
        make_sa(3, "Vận dụng", "Nơi từ trường yếu thì đường sức từ dày hay thưa?", "Thưa", "Thưa."),
        make_sa(4, "Vận dụng", "Hình ảnh mạt sắt sắp xếp quanh nam châm gọi là gì?", "Từ phổ", "Từ phổ."),
        make_sa(5, "Vận dụng cao", "Kim nam châm dùng để thử từ trường gọi là nam châm gì?", "Nam châm thử", "Nam châm thử."),
        make_sa(6, "Vận dụng cao", "Các đường sức từ có cắt nhau không? (Có hay Không)", "Không", "Không bao giờ cắt nhau.")
    ],
    "part4": [
        make_vdc(1, "Một bạn học sinh đặt một chiếc la bàn trên mặt bàn học. Bất ngờ bạn thấy kim la bàn quay lệch góc 30 độ khỏi hướng Bắc - Nam. Khi bạn nhấc chiếc laptop đang cắm sạc ra xa khỏi bàn thì kim la bàn lập tức quay trở về chỉ đúng hướng Bắc - Nam. Hiện tượng kim la bàn bị lệch lúc đầu là do:", ["Bộ sạc và dòng điện chạy trong laptop đã tạo ra từ trường xung quanh tác dụng lực từ làm lệch kim la bàn", "Laptop quá nóng", "Màn hình laptop phát sáng", "Do pin laptop bị hỏng"], 0, "Dòng điện trong thiết bị điện tử sinh ra từ trường cục bộ làm lệch kim la bàn."),
        make_vdc(2, "Một khung dây tròn mang dòng điện không đổi đặt thẳng đứng trong mặt phẳng kinh tuyến từ của Trái Đất. Tại tâm của khung dây đặt một kim nam châm nhỏ thăng bằng. Khi đóng khóa điện, kim nam châm chịu tác dụng đồng thời của hai từ trường: từ trường Trái Đất và từ trường của dòng điện trong khung dây. Trục của kim nam châm sẽ định hướng như thế nào?", ["Định hướng theo phương của từ trường tổng hợp của hai từ trường nói trên", "Chỉ theo hướng cũ", "Chỉ thẳng đứng", "Quay tròn liên tục"], 0, "Kim nam châm định hướng theo vectơ từ trường tổng hợp tại điểm đặt."),
        make_vdc(3, "Các nhà địa chất học khi đi tìm kiếm các mỏ quặng sắt ngầm dưới lòng đất thường sử dụng thiết bị đo từ trường (từ kế) đo độ biến thiên địa từ trường trên mặt đất. Cơ sở khoa học của phương pháp thăm dò này là:", ["Các mỏ quặng sắt có từ tính cao sẽ làm tăng cục bộ cường độ từ trường Trái Đất tại khu vực đó (gây dị thường từ)", "Quặng sắt phát ra nhiệt độ cao", "Quặng sắt làm đất đổi màu", "Quặng sắt phát ra sóng âm"], 0, "Dị thường từ (Magnetic anomaly): quặng sắt từ hóa làm tăng đột biến từ trường mặt đất giúp định vị mỏ quặng."),
        make_vdc(4, "Tại sao khi vẽ đường sức từ của một nam châm, người ta phải vẽ mũi tên định hướng trên mỗi đường cong mà không vẽ đường trơn không có mũi tên?", ["Vì đường sức từ là đường có hướng, mũi tên thể hiện chiều quy ước của từ trường (đi ra từ cực Bắc và đi vào ở cực Nam)", "Để trang trí cho đẹp", "Để phân biệt với tia sáng", "Để đếm số lượng đường"], 0, "Đường sức từ có hướng xác định, mũi tên chỉ hướng của lực từ tác dụng lên cực Bắc của nam châm thử.")
    ]
}
