# -*- coding: utf-8 -*-
"""
CHƯƠNG VI: TỪ - [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG VI (5 ĐỀ ĐỘC LẬP 100%)
- phys7_c6_rev: [Đề tổng hợp] Ôn tập cuối Chương VI (5 đề: test1..test5)
Không trùng lặp câu hỏi, không tiền tố "Đề X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

c6_rev_exams = {}

# =========================================================================
# [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG VI: TỪ (5 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
c6_rev_exams["phys7_c6_rev_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật nào sau đây có khả năng hút được các mẩu đinh sắt nhỏ?", ["Thanh nam châm thẳng", "Chiếc đũa thủy tinh", "Thanh thước nhựa mica", "Miếng xốp bọt biển"], 0, "Nam châm có từ tính hút các vật liệu bằng sắt thép."),
        make_mc(2, "Nhận biết", "Kí hiệu chuẩn quốc tế của cực Bắc trên thanh nam châm là chữ cái nào?", ["N (North)", "S (South)", "W (West)", "E (East)"], 0, "Cực Bắc kí hiệu là N (North), cực Nam kí hiệu là S (South)."),
        make_mc(3, "Nhận biết", "Xung quanh một thanh nam châm luôn tồn tại dạng vật chất đặc biệt nào có thể tác dụng lực từ lên nam châm khác?", ["Từ trường", "Điện trường tĩnh", "Sóng siêu âm", "Chân không hoàn toàn"], 0, "Xung quanh nam châm luôn tồn tại từ trường."),
        make_mc(4, "Nhận biết", "Hình ảnh các đường mạt sắt sắp xếp trật tự xung quanh thanh nam châm trên tấm bìa được gọi là gì?", ["Từ phổ", "Quang phổ", "Sóng âm", "Lưới tọa độ"], 0, "Hình ảnh mạt sắt sắp xếp quanh nam châm gọi là từ phổ."),
        make_mc(5, "Nhận biết", "Theo quy ước quốc tế, chiều của đường sức từ ở bên ngoài thanh nam châm là chiều nào?", ["Đi ra từ cực Bắc và đi vào cực Nam", "Đi ra từ cực Nam và đi vào cực Bắc", "Đi từ chính giữa ra hai đầu", "Đi ngẫu nhiên không có quy luật"], 0, "Quy ước chiều đường sức từ bên ngoài nam châm: Ra Bắc vào Nam."),
        make_mc(6, "Nhận biết", "Tại sao kim la bàn tự do khi thăng bằng luôn chỉ theo hướng Bắc - Nam địa lý?", ["Vì Trái Đất là một nam châm khổng lồ có từ trường", "Vì có gió thổi theo hướng Bắc Nam", "Vì ánh sáng Mặt Trời chiếu vuông góc", "Vì sức hút của Mặt Trăng"], 0, "Từ trường của Trái Đất định hướng cho kim nam châm của la bàn."),
        make_mc(7, "Nhận biết", "Cực Bắc địa từ của Trái Đất nằm ở vùng lân cận vị trí nào trên Trái Đất?", ["Gần cực Nam địa lí của Trái Đất", "Gần cực Bắc địa lí của Trái Đất", "Ngay tại đường xích đạo", "Ở tâm của Trái Đất"], 0, "Cực Bắc địa từ nằm ở gần cực Nam địa lí, cực Nam địa từ nằm ở gần cực Bắc địa lí."),
        make_mc(8, "Nhận biết", "Để chế tạo một nam châm điện đơn giản, ta cần quấn một cuộn dây dẫn bọc cách điện xung quanh vật nào?", ["Một chiếc đinh sắt non", "Một thanh đồng đỏ", "Một ống hút nhựa", "Một thỏi than chì"], 0, "Lõi sắt non bị nhiễm từ mạnh, tăng cường độ từ trường của nam châm điện."),
        make_mc(9, "Nhận biết", "Yếu tố nào sau đây KHÔNG LÀM THAY ĐỔI độ mạnh của lực từ nam châm điện?", ["Màu sắc lớp vỏ bọc cách điện của dây dẫn", "Cường độ dòng điện qua cuộn dây", "Số vòng quấn của ống dây", "Vật liệu làm lõi của ống dây"], 0, "Màu sắc vỏ cách điện không ảnh hưởng gì đến từ tính của nam châm."),
        make_mc(10, "Thông hiểu", "Khi đưa hai cực cùng tên của hai thanh nam châm lại gần nhau thì hiện tượng gì sẽ xảy ra?", ["Hai thanh nam châm đẩy nhau ra xa", "Hai thanh nam châm hút chặt lấy nhau", "Hai thanh nam châm hoàn toàn không tương tác", "Hai thanh nam châm phát sáng"], 0, "Các cực cùng tên thì đẩy nhau, các cực khác tên thì hút nhau."),
        make_mc(11, "Thông hiểu", "Phương tiện giao thông hiện đại nào sau đây ứng dụng lực từ cực mạnh của nam châm điện để di chuyển không ma sát đường ray?", ["Tàu đệm từ Maglev", "Tàu hỏa chạy bằng hơi nước", "Xe buýt chạy bằng khí gas", "Xe đạp điện"], 0, "Tàu Maglev dùng nam châm điện để nâng và đẩy toa tàu bay lơ lửng trên ray."),
        make_mc(12, "Thông hiểu", "Vật liệu nào sau đây KHÔNG PHẢI là vật liệu từ và hoàn toàn không bị nam châm hút?", ["Thanh đồng đỏ nguyên chất", "Một chiếc đinh thép", "Một mẩu kim loại niken", "Một chiếc kẹp ghim bằng sắt"], 0, "Đồng đỏ không phải vật liệu từ nên không bị nam châm hút.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về tính chất của nam châm vĩnh cửu và sự tương tác từ:", [
            ("a", "Mỗi thanh nam châm luôn luôn có hai cực từ: cực Bắc (N) và cực Nam (S).", True),
            ("b", "Khi bẻ gãy một thanh nam châm làm đôi, mỗi nửa sẽ biến thành một nam châm mới có đủ hai cực.", True),
            ("c", "Hai cực khác tên của hai nam châm khi đặt gần nhau sẽ hút nhau.", True),
            ("d", "Nam châm vĩnh cửu có thể hút được tất cả các kim loại như vàng, bạc, đồng, nhôm.", False)
        ], "Nam châm chỉ hút các kim loại có tính sắt từ như sắt, thép, coban, niken."),
        make_tf(2, "Thông hiểu", "Về từ phổ và các đường sức từ của một thanh nam châm thẳng:", [
            ("a", "Từ phổ cho ta hình ảnh trực quan sinh động về sự phân bố của từ trường trong không gian.", True),
            ("b", "Nơi nào mạt sắt sắp xếp càng dày khít thì từ trường tại đó càng mạnh.", True),
            ("c", "Ở khoảng giữa của thanh nam châm thẳng, từ trường mạnh hơn rất nhiều so với ở hai đầu cực.", False),
            ("d", "Bên ngoài nam châm, đường sức từ là những đường cong khép kín đi ra từ cực Bắc và đi vào cực Nam.", True)
        ], "Lực từ của thanh nam châm tập trung mạnh nhất ở hai đầu cực, ở phần giữa hầu như bằng 0."),
        make_tf(3, "Vận dụng", "Về từ trường của Trái Đất và ứng dụng la bàn trong hàng hải:", [
            ("a", "Trái Đất có từ trường bao bọc xung quanh, đóng vai trò như một lá chắn bảo vệ sinh quyển.", True),
            ("b", "Cực Nam của kim la bàn luôn bị hút về phía cực Bắc địa từ của Trái Đất.", True),
            ("c", "Trục từ của Trái Đất trùng khít hoàn toàn 100% với trục quay địa lý Bắc - Nam của Trái Đất.", False),
            ("d", "Góc lệch giữa hướng Bắc địa từ và hướng Bắc địa lý được gọi là góc từ thiên.", True)
        ], "Trục từ của Trái Đất nghiêng một góc khoảng 11 độ so với trục quay địa lý."),
        make_tf(4, "Vận dụng", "Về nam châm điện và các ứng dụng kỹ thuật trong thực tế:", [
            ("a", "Nam châm điện chỉ sinh ra từ trường khi có dòng điện chạy qua cuộn dây dẫn.", True),
            ("b", "Có thể tăng lực từ của nam châm điện bằng cách tăng số vòng dây hoặc tăng cường độ dòng điện.", True),
            ("c", "Lõi của nam châm điện nên dùng thép tôi cứng để tăng tốc độ khử từ khi ngắt công tắc.", False),
            ("d", "Cần cẩu dọn sắt phế liệu ở các cảng biển sử dụng nam châm điện có công suất lớn.", True)
        ], "Thép giữ từ tính lâu nên khó khử từ; lõi nam châm điện bắt buộc phải dùng sắt non.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một thanh nam châm thẳng ban đầu có 2 cực từ. Người ta cưa thanh nam châm này thành 3 đoạn ngắn bằng nhau. Hỏi tổng số cực từ của cả 3 đoạn nam châm mới là bao nhiêu cực?", "6", "Mỗi đoạn nam châm sau khi cắt đều trở thành một nam châm mới có 2 cực (1 Bắc, 1 Nam). Tổng cộng có 3 x 2 = 6 cực."),
        make_sa(2, "Thông hiểu", "Một cuộn dây nam châm điện quấn 50 vòng hút được 10 chiếc kẹp ghim nhỏ. Nếu giữ nguyên dòng điện và muốn nam châm hút được 30 chiếc kẹp ghim thì cuộn dây cần có tổng cộng bao nhiêu vòng quấn?", "150", "Số ghim tăng gấp 3 lần (30 / 10 = 3) nên số vòng quấn cũng phải tăng gấp 3 lần: 50 x 3 = 150 vòng."),
        make_sa(3, "Thông hiểu", "Tại một trạm khí tượng thủy văn, người ta đo được góc từ thiên giữa kinh tuyến từ và kinh tuyến địa lý là 1,5 độ. Đổi số đo 1,5 độ này ra đơn vị phút góc (kí hiệu là ')?", "90", "1 độ = 60 phút. Do đó 1,5 độ = 1,5 x 60 = 90'."),
        make_sa(4, "Thông hiểu", "Một cần cẩu nam châm điện bốc dỡ phế liệu tại nhà máy luyện kim có khả năng nâng tối đa một khối sắt nặng 3,2 tấn. Khối lượng này quy đổi ra đơn vị kilôgam (kg) là bao nhiêu?", "3200", "3,2 tấn = 3,2 x 1000 = 3200 kg."),
        make_sa(5, "Thông hiểu", "Một học sinh đưa một thanh nam châm lại gần 5 vật nhỏ trên bàn: (1) Chiếc kim bấm thép; (2) Đồng xu bằng nhôm; (3) Chiếc chìa khóa bằng đồng thau; (4) Ghim kẹp bằng niken; (5) Chiếc thước nhựa. Hỏi có bao nhiêu vật thể sẽ bị nam châm hút chặt?", "2", "Có 2 vật bị nam châm hút là (1) kim bấm thép và (4) ghim niken."),
        make_sa(6, "Thông hiểu", "Khi nối cuộn dây nam châm điện với nguồn, ban đầu cường độ dòng điện là 0,4 A. Người ta điều chỉnh biến trở làm dòng điện tăng lên thành 1,6 A. Hỏi cường độ dòng điện đã tăng lên gấp bao nhiêu lần?", "4", "Số lần tăng = 1,6 / 0,4 = 4 lần.")
    ],
    "part4": [
        make_vdc(1, "Từ trường Trái Đất (từ quyển) đóng vai trò là một tấm lá chắn tự nhiên vô cùng quan trọng đối với sự sống trên hành tinh chúng ta. Tấm lá chắn này bảo vệ sinh quyển chủ yếu bằng cách nào?", ["Làm lệch hướng chuyển động của các hạt mang điện tích năng lượng cao từ gió Mặt Trời, ngăn chúng bắn phá mặt đất", "Ngăn chặn 100% ánh sáng nhìn thấy của Mặt Trời chiếu xuống mặt đất", "Hấp thụ toàn bộ nhiệt lượng từ vũ trụ để Trái Đất không bị nóng lên", "Ngăn chặn lực hút của Mặt Trăng gây ra hiện tượng thủy triều"], 0, "Từ quyển tạo lực từ làm lệch quỹ đạo các hạt tích điện từ gió Mặt Trời cuốn về hai cực tạo cực quang, bảo vệ sinh quyển."),
        make_vdc(2, "Trong một hệ thống rơ le bảo vệ quá tải: Lò xo kéo giữ tiếp điểm đóng mạch tải với một lực căng 15 N. Khi dòng điện qua cuộn dây nam châm điện vượt quá 6 A thì lực hút từ của nam châm đạt trên 15 N, thắng lực kéo lò xo và hút cần ngắt mạch điện. Nếu thay lò xo mới có lực căng 25 N thì cường độ dòng điện tối thiểu qua nam châm điện để ngắt mạch là bao nhiêu ampe (coi lực từ tỉ lệ thuận với dòng điện)?", ["10 A", "8 A", "12 A", "9 A"], 0, "Lực từ tỉ lệ thuận với I: I2 = I1 x (F2 / F1) = 6 x (25 / 15) = 10 A."),
        make_vdc(3, "Để so sánh lực hút giữa các vị trí trên một thanh nam châm dài 24 cm, một học sinh dùng lực kế đo lực kéo nhả một viên bi thép nhỏ dính ở các vị trí: Đầu cực Bắc (N) đo được F1 = 1,8 N; vị trí cách đầu cực Bắc 6 cm đo được F2 = 0,9 N; vị trí chính giữa thanh (cách cực 12 cm) đo được F3. Giá trị của F3 xấp xỉ bằng bao nhiêu?", ["Gần bằng 0 N", "1,8 N", "3,6 N", "0,9 N"], 0, "Tại vị trí chính giữa thanh nam châm thẳng, từ trường bị triệt tiêu gần như hoàn toàn nên lực hút F3 xấp xỉ 0 N."),
        make_vdc(4, "Một cần cẩu điện dọn sắt phế liệu ở bến cảng có công suất nâng 5 tấn hàng trong mỗi chuyến. Nếu sử dụng lõi nam châm bằng thép thường thay vì sắt non mềm thì sau khi ngắt công tắc điện, hiện tượng bất lợi nào nghiêm trọng nhất sẽ xảy ra?", ["Lõi thép vẫn giữ từ tính lâu dài làm phế liệu sắt dính chặt không chịu rơi xuống vị trí bốc dỡ", "Thanh thép sẽ bị nổ tung do nhiệt độ tăng cao", "Dòng điện chạy ngược lại phá hỏng nguồn điện máy phát", "Cần cẩu bị mất trọng tâm lật đổ"], 0, "Thép có tính lưu từ cao, biến thành nam châm vĩnh cửu nên khi ngắt điện vẫn giữ sắt phế liệu không nhả ra được.")
    ]
}

# --- ĐỀ 2 ---
c6_rev_exams["phys7_c6_rev_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Vật nào sau đây được gọi là một nam châm nhân tạo?", ["Một thanh thép được từ hóa bằng dòng điện trong ống dây", "Một hòn đá nam châm thiên nhiên (quặng magnetit)", "Một mẩu gỗ hóa thạch", "Một mẩu đá vôi phong hóa"], 0, "Nam châm nhân tạo do con người chế tạo bằng cách từ hóa vật liệu từ."),
        make_mc(2, "Nhận biết", "Trên một thanh nam châm thẳng, nơi nào có các đường sức từ phân bố dày đặc nhất?", ["Ở sát gần hai đầu cực từ của nam châm", "Ở chính giữa thân thanh nam châm", "Ở cách xa nam châm 1 mét", "Ở mọi vị trí đều như nhau"], 0, "Hai đầu cực là nơi từ trường mạnh nhất, đường sức từ tập trung dày đặc nhất."),
        make_mc(3, "Nhận biết", "Chiều của đường sức từ tại một điểm trong từ trường được xác định theo chiều nào?", ["Chiều từ cực Nam đến cực Bắc của kim nam châm nhỏ nằm cân bằng tại điểm đó", "Chiều từ cực Bắc đến cực Nam của kim nam châm nhỏ", "Chiều của trọng lực hướng thẳng đứng xuống dưới", "Chiều gió thổi qua điểm đó"], 0, "Chiều đường sức từ trùng với chiều Nam - Bắc của kim nam châm thử thăng bằng tại điểm đó."),
        make_mc(4, "Nhận biết", "Hiện tượng lịch sử nào khẳng định dòng điện có tác dụng từ?", ["Dòng điện trong dây dẫn làm kim nam châm đặt gần đó quay lệch hướng", "Dòng điện làm dây tóc bóng đèn nóng sáng", "Dòng điện làm nước muối bị điện phân", "Dòng điện gây giật khi chạm tay"], 0, "Thí nghiệm Oersted phát hiện dòng điện làm quay kim nam châm."),
        make_mc(5, "Nhận biết", "Cực Nam địa từ của Trái Đất nằm ở vùng lân cận vị trí địa lý nào?", ["Vùng cực Bắc địa lí của Trái Đất", "Vùng cực Nam địa lí của Trái Đất", "Vùng rừng rậm xích đạo châu Phi", "Tâm địa cầu"], 0, "Cực Nam địa từ nằm ở phía Bắc địa cầu, hút cực Bắc kim la bàn."),
        make_mc(6, "Nhận biết", "Khi đưa một thanh sắt non chưa nhiễm từ lại gần cực Bắc của một thanh nam châm thì thanh sắt non sẽ:", ["Bị hút về phía cực Bắc của nam châm", "Bị cực Bắc của nam châm đẩy ra xa", "Không có hiện tượng gì xảy ra", "Tự động phát ra tia lửa điện"], 0, "Thanh sắt non bị nhiễm từ tạm thời và luôn bị hút vào cực của nam châm."),
        make_mc(7, "Nhận biết", "Thiết bị đóng ngắt mạch điện tự động bảo vệ hệ thống điện từ xa nhờ tác dụng từ của dòng điện là:", ["Rơ le điện từ", "Chiếc cầu chì nhiệt", "Phích cắm điện xoay", "Bóng đèn sợi đốt"], 0, "Rơ le điện từ dùng nam châm điện để đóng ngắt mạch điện."),
        make_mc(8, "Thông hiểu", "Để kim la bàn quay thật nhạy và định hướng chính xác nhất, trục đỡ kim la bàn thường được thiết kế như thế nào?", ["Đặt trên một đầu mũi nhọn bằng kim loại cứng có ma sát cực nhỏ", "Gắn chặt bằng ốc vít cố định không quay được", "Dán chặt bằng keo dính", "Thả nổi tự do trong dầu nhớt đặc"], 0, "Trục nhọn giúp kim la bàn quay nhạy bén mà không bị lực ma sát cản trở."),
        make_mc(9, "Thông hiểu", "Trong mạch điện của nam châm điện, khi ta ngắt công tắc điện thì hiện tượng gì xảy ra ngay lập tức?", ["Từ trường của ống dây biến mất hoàn toàn", "Ống dây phát sáng màu đỏ", "Lực hút của ống dây tăng vọt", "Đinh sắt bị biến dạng cong gãy"], 0, "Không có dòng điện thì từ trường biến mất ngay lập tức."),
        make_mc(10, "Thông hiểu", "Hiện tượng cực quang rực rỡ nhiều màu sắc ở bầu trời vùng cực Trái Đất được sinh ra do nguyên nhân nào?", ["Các hạt mang điện từ gió Mặt Trời va chạm với phân tử khí quyển dưới tác dụng định hướng của từ trường Trái Đất", "Ánh sáng phản chiếu từ các tảng băng trôi khổng lồ", "Ánh đèn của các thành phố phản chiếu lên mây", "Mặt Trời chiếu sáng ban đêm ở vùng cực"], 0, "Gió Mặt Trời chứa electron, proton bị từ trường Trái Đất hướng về vùng cực tương tác với khí quyển sinh ra cực quang."),
        make_mc(11, "Thông hiểu", "Khi đưa hai cực Nam của hai thanh nam châm thẳng lại gần nhau thì chúng sẽ:", ["Đẩy nhau ra xa", "Hút chặt lấy nhau", "Đứng yên không tác dụng lực", "Biến thành hai cực Bắc"], 0, "Hai cực cùng tên (cùng cực Nam) thì đẩy nhau."),
        make_mc(12, "Thông hiểu", "Nếu ta đảo ngược hai đầu dây nối của nam châm điện vào nguồn pin thì:", ["Chiều từ trường bị đảo ngược, cực Bắc và cực Nam đổi chỗ cho nhau", "Nam châm điện mất hết từ tính", "Lực hút tăng lên gấp đôi", "Pin bị nổ tung ngay"], 0, "Đảo chiều dòng điện làm đảo chiều đường sức từ và hoán đổi vị trí hai cực từ.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về tương tác của thanh nam châm với các kim loại khác nhau trong đời sống:", [
            ("a", "Nam châm hút được thanh sắt, chiếc đinh thép và miếng hợp kim niken.", True),
            ("b", "Nam châm không hút được chiếc thìa nhôm, dây đồng và chiếc nhẫn vàng.", True),
            ("c", "Nam châm có thể dùng để phân loại lon sắt thép và lon nhôm trong nhà máy tái chế.", True),
            ("d", "Nếu đưa cực Bắc của nam châm lại gần thanh đồng thì chúng sẽ đẩy nhau rất mạnh.", False)
        ], "Đồng không tương tác từ với nam châm nên không bị đẩy cũng không bị hút."),
        make_tf(2, "Thông hiểu", "Về từ trường của dòng điện và thí nghiệm phát hiện của Oersted:", [
            ("a", "Dây dẫn thẳng có dòng điện chạy qua sinh ra từ trường ở không gian xung quanh nó.", True),
            ("b", "Khi ngắt dòng điện trong dây dẫn, tác dụng từ xung quanh dây dẫn cũng biến mất.", True),
            ("c", "Đường sức từ xung quanh một dây dẫn thẳng dài mang dòng điện là những đường tròn đồng tâm.", True),
            ("d", "Dòng điện chỉ có tác dụng nhiệt và phát sáng, hoàn toàn không có tác dụng từ.", False)
        ], "Dòng điện luôn có tác dụng từ khi chạy qua dây dẫn."),
        make_tf(3, "Vận dụng", "Về từ quyển Trái Đất và hiện tượng bão từ trong vũ trụ:", [
            ("a", "Từ quyển bao bọc Trái Đất kéo dài hàng chục nghìn kilômét ra ngoài không gian vũ trụ.", True),
            ("b", "Bão từ xảy ra khi các đợt phun trào hạt tích điện mạnh từ Mặt Trời đập vào từ trường Trái Đất.", True),
            ("c", "Khi xảy ra bão từ mạnh, các hệ thống định vị vệ tinh, sóng vô tuyến và mạng lưới truyền tải điện có thể bị gián đoạn.", True),
            ("d", "Bão từ làm cho kim la bàn trên mặt đất luôn chỉ tuyệt đối chính xác không hề dao động.", False)
        ], "Bão từ làm kim la bàn dao động mạnh hỗn loạn, không định vị chính xác được hướng."),
        make_tf(4, "Vận dụng", "Về các đặc tính kỹ thuật của nam châm điện công nghiệp:", [
            ("a", "Để tăng lực từ lên mức tối đa, người ta quấn hàng nghìn vòng dây đồng và dùng lõi sắt non cỡ lớn.", True),
            ("b", "Có thể tắt mở lực từ nhanh chóng chỉ bằng thao tác bấm công tắc điều khiển điện.", True),
            ("c", "Nam châm điện tiêu thụ điện năng liên tục trong suốt thời gian giữ chặt vật phế liệu sắt.", True),
            ("d", "Nam châm điện không thể hút được vật nặng trên 100 kg.", False)
        ], "Các nam châm điện công nghiệp có thể nâng các khối thép nặng hàng chục tấn.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một thanh nam châm thẳng ban đầu dài 20 cm bị bẻ gãy làm 4 đoạn bằng nhau. Hỏi sau khi bẻ, tổng số cực Bắc của tất cả các đoạn nam châm mới là bao nhiêu cực?", "4", "Mỗi đoạn nam châm mới đều có đủ 1 cực Bắc và 1 cực Nam. Do đó 4 đoạn có 4 cực Bắc."),
        make_sa(2, "Thông hiểu", "Một cuộn dây nam châm điện có 120 vòng quấn nối nguồn điện hút được 24 kẹp sắt. Khi tháo bớt một nửa số vòng dây chỉ còn 60 vòng (giữ nguyên cường độ dòng điện qua mạch), hỏi số kẹp sắt hút được ước tính là bao nhiêu chiếc?", "12", "Số vòng giảm đi một nửa (60 / 120 = 1/2) nên số kẹp sắt hút được cũng giảm một nửa: 24 / 2 = 12 chiếc."),
        make_sa(3, "Thông hiểu", "Tại vùng xích đạo Trái Đất, góc từ thiên giữa trục từ và trục địa lý xấp xỉ 0 độ. Tại một hải cảng ở phương Bắc, máy đo ghi nhận góc từ thiên là 4,5 độ. Chênh lệch độ từ thiên giữa hai địa điểm này là bao nhiêu độ?", "4,5", "Chênh lệch = 4,5 - 0 = 4,5 độ."),
        make_sa(4, "Thông hiểu", "Một cần cẩu nam châm điện tại bãi bốc xếp có khả năng nâng một lần 15 tấm tôn thép công nghiệp, biết mỗi tấm tôn nặng 80 kg. Tổng khối lượng tôn thép mà cần cẩu nâng được trong một lần là bao nhiêu kilôgam (kg)?", "1200", "Tổng khối lượng = 15 x 80 = 1200 kg."),
        make_sa(5, "Thông hiểu", "Một học sinh thử đưa nam châm lại gần 5 vật dụng trong phòng học: (1) Kim la bàn; (2) Đinh sắt; (3) Chiếc thìa bằng bạc; (4) Đoạn dây may-so niken-crom; (5) Cuộn dây cước câu cá. Hỏi có bao nhiêu vật dụng chịu lực hút của nam châm?", "3", "Có 3 vật chịu lực hút là (1) kim la bàn, (2) đinh sắt, (4) dây may-so niken-crom."),
        make_sa(6, "Thông hiểu", "Trong một thí nghiệm vật lý, khi dịch chuyển con chạy của biến trở làm điện trở mạch giảm xuống, cường độ dòng điện qua nam châm điện tăng từ 0,25 A lên 0,75 A. Hỏi cường độ dòng điện đã tăng thêm bao nhiêu ampe (A)?", "0,5", "Cường độ tăng thêm = 0,75 - 0,25 = 0,5 A.")
    ],
    "part4": [
        make_vdc(1, "Một đợt bùng phát bức xạ Mặt Trời mạnh (Solar Flare) phóng hàng tỉ tấn plasma hạt mang điện về phía Trái Đất gây bão từ cấp độ mạnh. Hiện tượng nào sau đây là hậu quả trực tiếp nguy hiểm nhất của cơn bão từ đối với mạng lưới công nghệ hiện đại trên Trái Đất?", ["Gây ra dòng điện cảm ứng mạnh làm quá tải và cháy nổ các trạm biến áp cao thế, làm tê liệt hệ thống định vị vệ tinh GPS", "Làm cho nước biển dâng cao nhấn chìm các thành phố ven biển", "Làm cho nhiệt độ không khí giảm đột ngột xuống âm 50 độ C", "Làm cho Mặt Trăng ngừng quay quanh Trái Đất"], 0, "Bão từ cảm ứng dòng điện quá tải trong lưới điện cao thế gây mất điện diện rộng và làm nhiễu sóng định vị GPS vệ tinh."),
        make_vdc(2, "Trên tuyến đường tàu cao tốc đệm từ Maglev: Dưới đáy toa tàu gắn các nam châm điện có cực từ hướng xuống dưới là cực Bắc (N). Để toa tàu được nâng lơ lửng ổn định trên đường ray nhờ lực đẩy từ trường, các nam châm điện gắn dọc mặt trên của đường ray tiếp xúc đối diện với đáy toa tàu phải được cấp điện sao cho mặt trên của chúng là cực gì?", ["Cực Bắc (N) để hai cực cùng tên đẩy nhau nâng toa tàu bay lên", "Cực Nam (S) để hai cực hút chặt toa tàu xuống ray", "Luân phiên đổi chiều 1000 lần mỗi giây", "Không cần cực từ nào cả"], 0, "Hai cực cùng tên (cùng cực Bắc N) đẩy nhau tạo lực nâng toa tàu lơ lửng trên đường ray."),
        make_vdc(3, "Hệ thống chuông điện báo cháy tự động hoạt động: Khi nhiệt độ môi trường vượt quá 70 độ C, thanh lưỡng kim nhiệt bị uốn cong chạm vào tiếp điểm đóng mạch điện cấp dòng 0,5 A cho cuộn dây nam châm điện. Nam châm điện ngay lập tức hút miếng sắt non kéo búa gõ vào chuông liên tục. Chức năng chính của thanh lưỡng kim nhiệt trong hệ thống này là:", ["Đóng vai trò như một công tắc cảm biến nhiệt độ tự động đóng mạch điện khi quá nhiệt", "Tạo ra âm thanh chuông báo động trực tiếp", "Hấp thụ nhiệt để làm mát căn phòng", "Cung cấp nguồn điện 220V cho chuông"], 0, "Thanh lưỡng kim hoạt động như một công tắc nhiệt tự động đóng mạch khi gặp nhiệt độ cao."),
        make_vdc(4, "So sánh từ phổ của một thanh nam châm thẳng và một thanh nam châm hình chữ U: Tại sao ở khoảng không gian giữa hai nhánh cực của nam châm hình chữ U, các đường sức từ lại song song và cách đều nhau tạo thành từ trường đều?", ["Vì hai cực Bắc và Nam đặt gần nhau đối diện nhau, đường sức từ đi thẳng từ cực Bắc sang cực Nam với mật độ đồng đều", "Vì nam châm chữ U có từ tính mạnh gấp 10 lần nam châm thẳng", "Vì sắt làm nam châm chữ U dẫn từ tốt hơn thanh thẳng", "Vì không có không khí lọt vào giữa hai cực"], 0, "Hai cực đối diện ở khoảng cách ngắn làm các đường sức từ phân bố thẳng song song và đều đặn (từ trường đều).")
    ]
}

# --- ĐỀ 3 ---
c6_rev_exams["phys7_c6_rev_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Ở thanh nam châm hình chữ U, các đường sức từ ở khoảng giữa hai nhánh cực có hình dạng như thế nào?", ["Gần như song song và cách đều nhau", "Là những vòng tròn đồng tâm", "Là những đường xoắn ốc tỏa rộng", "Không có đường sức từ nào"], 0, "Giữa hai cực nam châm chữ U là từ trường đều, các đường sức từ gần như song song và cách đều nhau."),
        make_mc(2, "Nhận biết", "Vật liệu nào sau đây giữ được từ tính lâu dài nhất sau khi bị nhiễm từ trong từ trường mạnh?", ["Thép carbon cứng", "Sắt non mềm", "Đồng thau", "Nhôm đúc"], 0, "Thép có tính khử từ chậm, giữ từ tính lâu dài tạo thành nam châm vĩnh cửu."),
        make_mc(3, "Nhận biết", "Khi rắc mạt sắt lên tấm bìa đặt trên thanh nam châm rồi gõ nhẹ, các hạt mạt sắt sắp xếp như thế nào?", ["Theo các đường cong nối từ cực này sang cực kia của nam châm", "Tụ tập thành một khối tròn duy nhất ở giữa", "Phân bố tản mạn ngẫu nhiên không quy luật", "Tất cả bị đẩy bay ra khỏi tấm bìa"], 0, "Mạt sắt sắp xếp thành các đường cong nối từ cực này sang cực kia tạo thành từ phổ."),
        make_mc(4, "Nhận biết", "Kim nam châm của một chiếc la bàn thông thường luôn quay tự do quanh trục thẳng đứng và nằm thăng bằng theo phương nào?", ["Phương Bắc - Nam địa lí", "Phương Đông - Tây", "Phương thẳng đứng cắm xuống đất", "Phương song song với tia sáng"], 0, "Kim nam châm tự do luôn thăng bằng theo phương Bắc - Nam địa lí."),
        make_mc(5, "Nhận biết", "Từ trường của Trái Đất có hình dạng tương tự như từ trường của vật nào sau đây?", ["Một thanh nam châm thẳng khổng lồ nằm nghiêng trong lòng Trái Đất", "Một chiếc đĩa nam châm tròn mỏng", "Một cuộn dây xoắn hình lò xo", "Một khối cầu không có cực từ"], 0, "Từ trường Trái Đất tương tự một nam châm thẳng khổng lồ với trục từ nghiêng khoảng 11 độ so với trục địa lý."),
        make_mc(6, "Nhận biết", "Lõi sắt non đặt trong cuộn dây có dòng điện có tác dụng gì quan trọng nhất?", ["Làm tăng cường độ từ trường của cuộn dây lên rất nhiều lần", "Làm giảm nhiệt độ của cuộn dây", "Làm tăng khối lượng để cuộn dây đứng vững", "Làm đổi màu tia lửa điện"], 0, "Lõi sắt non bị nhiễm từ mạnh, làm tăng đáng kể từ trường của ống dây."),
        make_mc(7, "Nhận biết", "Để thay đổi cực từ Bắc và Nam của một nam châm điện, thao tác đơn giản và chuẩn xác nhất là:", ["Đổi chiều dòng điện chạy qua cuộn dây", "Rút lõi sắt non ra quay ngược đầu lại", "Sơn lại màu sắc hai đầu đinh sắt", "Tăng thêm hiệu điện thế nguồn điện"], 0, "Đổi chiều dòng điện làm đảo chiều các đường sức từ và các cực từ."),
        make_mc(8, "Thông hiểu", "Thiết bị nào sau đây biến đổi dao động điện thành dao động âm thanh nhờ lực từ tương tác giữa nam châm và cuộn âm?", ["Loa điện động", "Bếp từ gia đình", "Chiếc ấm siêu tốc", "Bàn là hơi nước"], 0, "Loa điện động hoạt động dựa trên tương tác lực từ giữa cuộn dây có dòng âm tần và nam châm vĩnh cửu."),
        make_mc(9, "Thông hiểu", "Một thanh nam châm vĩnh cửu KHÔNG tác dụng lực hút từ lên vật thể nào sau đây?", ["Một chiếc que bằng thủy tinh trong suốt", "Một chiếc đinh bằng thép cacbon", "Một mẩu dây niken", "Một thanh sắt non"], 0, "Thủy tinh là chất vô cơ không có từ tính nên không bị nam châm hút."),
        make_mc(10, "Thông hiểu", "Khi đưa cực Bắc của thanh nam châm 1 lại gần cực Nam của thanh nam châm 2 thì hai thanh nam châm sẽ:", ["Hút chặt lấy nhau", "Đẩy nhau ra xa", "Không có bất kì tương tác nào", "Làm mất hết từ tính của nhau"], 0, "Hai cực khác tên (Bắc và Nam) thì hút nhau."),
        make_mc(11, "Thông hiểu", "Quy ước sơn màu hoặc kí hiệu đầu cực Nam của kim la bàn thông thường là gì?", ["Sơn màu xanh hoặc trắng, kí hiệu chữ S", "Sơn màu đỏ tươi, kí hiệu chữ N", "Sơn màu vàng đậm, kí hiệu chữ E", "Sơn màu tím, kí hiệu chữ W"], 0, "Cực Nam kí hiệu là S (South), thường được sơn màu xanh hoặc màu trắng."),
        make_mc(12, "Thông hiểu", "Một học sinh quấn một nam châm điện và thấy nó hút được 5 chiếc kẹp giấy. Học sinh muốn nam châm hút được 15 chiếc kẹp giấy thì cần thực hiện cách nào?", ["Mắc thêm pin nối tiếp để tăng dòng điện và quấn thêm nhiều vòng dây", "Tháo bớt 2/3 số vòng dây ra", "Thay lõi sắt non bằng lõi nhựa dẻo", "Mắc thêm điện trở lớn vào mạch"], 0, "Tăng số vòng dây và tăng cường độ dòng điện giúp nam châm hút mạnh hơn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về cấu tạo và hình dạng đường sức từ của nam châm hình chữ U:", [
            ("a", "Nam châm chữ U có hai cực từ Bắc và Nam nằm ở hai đầu nhánh cong.", True),
            ("b", "Đường sức từ ở khoảng giữa hai nhánh đi thẳng từ cực Bắc sang cực Nam.", True),
            ("c", "Đường sức từ ở vùng bên ngoài hai nhánh uốn cong khép kín tương tự nam châm thẳng.", True),
            ("d", "Từ trường ở khoảng cách rất xa nam châm chữ U mạnh hơn nhiều so với ở khoảng giữa hai cực.", False)
        ], "Từ trường mạnh nhất tập trung dày đặc ở khoảng giữa hai cực, càng ra xa càng yếu."),
        make_tf(2, "Thông hiểu", "Về sự nhiễm từ của sắt non và thép trong kỹ thuật chế tạo:", [
            ("a", "Sắt non dễ bị nhiễm từ nhưng cũng rất dễ mất từ tính khi đưa ra khỏi từ trường.", True),
            ("b", "Thép khó nhiễm từ hơn nhưng một khi đã nhiễm từ thì giữ từ tính rất bền vững.", True),
            ("c", "Người ta dùng thép để chế tạo nam châm vĩnh cửu dùng trong loa, la bàn, nắp tủ lạnh.", True),
            ("d", "Trong cần cẩu dọn phế liệu, bắt buộc phải dùng lõi thép tôi cứng để tăng lực giữ hàng.", False)
        ], "Nếu dùng lõi thép thì khi ngắt điện nam châm không chịu nhả phế liệu ra."),
        make_tf(3, "Vận dụng", "Về hiện tượng sinh học định hướng theo từ trường Trái Đất của các loài động vật di cư:", [
            ("a", "Các loài chim bồ câu, én biển có thể bay hàng nghìn kilômét mà không bị lạc đường nhờ cảm nhận từ trường Trái Đất.", True),
            ("b", "Trong cơ thể một số loài sinh vật di cư có chứa các tinh thể khoáng vật từ tính (magnetit) siêu nhỏ.", True),
            ("c", "Nếu gắn một thanh nam châm nhỏ làm nhiễu từ trường lên đầu chim bồ câu, khả năng định hướng của chúng sẽ bị rối loạn.", True),
            ("d", "Rùa biển bơi qua đại dương hoàn toàn dựa vào ngọn hải đăng của con người, không có khả năng cảm nhận từ trường.", False)
        ], "Rùa biển sơ sinh định hướng bơi vượt đại dương nhờ cảm nhận độ nghiêng và cường độ từ trường Trái Đất."),
        make_tf(4, "Vận dụng", "Về cấu tạo và nguyên lý hoạt động của màng loa điện động:", [
            ("a", "Gồm một nam châm vĩnh cửu hình trụ và một cuộn dây âm tần gắn dính liền với màng loa.", True),
            ("b", "Khi có dòng điện âm tần biến thiên chạy qua cuộn dây, cuộn dây chịu lực từ hút đẩy biến thiên liên tục.", True),
            ("c", "Màng loa dao động rung động không khí xung quanh, tái tạo ra sóng âm thanh truyền đến tai người nghe.", True),
            ("d", "Màng loa chỉ có thể rung được nếu cuộn dây được làm hoàn toàn bằng dây nhựa cách điện.", False)
        ], "Cuộn dây âm tần bắt buộc phải làm bằng dây đồng dẫn điện tráng men cách điện.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một thanh nam châm hình chữ U có 2 cực từ. Nếu dùng 3 thanh nam châm hình chữ U giống hệt nhau thì tổng số cực từ của cả 3 thanh nam châm này là bao nhiêu cực?", "6", "Mỗi thanh nam châm có 2 cực từ. 3 thanh có tổng cộng: 3 x 2 = 6 cực."),
        make_sa(2, "Thông hiểu", "Một cuộn dây nam châm điện có 90 vòng dây hút được 18 viên bi sắt nhỏ. Nếu quấn thêm 60 vòng dây nữa thành 150 vòng (với cùng cường độ dòng điện), hỏi số viên bi sắt hút được ước tính là bao nhiêu viên?", "30", "Tỉ lệ số vòng = 150 / 90 = 5/3. Số bi sắt hút được = 18 x (5/3) = 30 viên bi."),
        make_sa(3, "Thông hiểu", "Độ nghiêng từ (góc giữa kim nam châm tự do và mặt phẳng nằm ngang) tại một vị trí vĩ độ cao được đo là 65 độ. Góc phụ của góc nghiêng từ này (bằng 90 độ trừ đi góc nghiêng từ) có giá trị là bao nhiêu độ?", "25", "Góc phụ = 90 - 65 = 25 độ."),
        make_sa(4, "Thông hiểu", "Một cần trục nam châm điện bốc xếp tại xưởng luyện cán thép có thể nâng một khối máy nặng 4,5 tấn trong một lần cẩu. Khối lượng này tương đương bao nhiêu kilôgam (kg)?", "4500", "4,5 tấn = 4,5 x 1000 = 4500 kg."),
        make_sa(5, "Thông hiểu", "Người ta thử đưa nam châm lại gần 6 mẫu vật: (1) Đinh sắt; (2) Kẹp bướm bằng thép; (3) Khối gỗ lim; (4) Đoạn dây đồng; (5) Tấm nhựa PVC; (6) Đồng xu bằng niken. Hỏi có bao nhiêu mẫu vật KHÔNG BỊ nam châm hút?", "3", "Có 3 mẫu không bị hút là (3) khối gỗ lim, (4) dây đồng, (5) tấm nhựa PVC."),
        make_sa(6, "Thông hiểu", "Khi điều chỉnh biến trở trong mạch nam châm điện, cường độ dòng điện tăng từ 0,6 A lên 1,8 A. Hỏi cường độ dòng điện đã tăng lên gấp bao nhiêu lần?", "3", "Số lần tăng = 1,8 / 0,6 = 3 lần.")
    ],
    "part4": [
        make_vdc(1, "Trong cấu tạo của loa điện động: Cuộn dây âm tần có đường kính 25 mm được đặt trong khe hở hẹp có từ trường rất mạnh của nam châm vĩnh cửu. Khi tín hiệu âm thanh có tần số f = 440 Hz (nốt La chuẩn) chạy qua cuộn dây, màng loa sẽ thực hiện bao nhiêu chu kì dao động cơ học trong đúng 1 giây?", ["440 chu kì", "220 chu kì", "880 chu kì", "100 chu kì"], 0, "Tần số f = 440 Hz nghĩa là màng loa thực hiện đúng 440 chu kì dao động trong mỗi giây."),
        make_vdc(2, "Một nhà sinh vật học nghiên cứu chim bồ câu đưa thư: Người ta phát hiện trong mỏ của chim có các cụm tế bào thần kinh chứa hạt nano magnetit nhạy cảm với từ trường Trái Đất có độ lớn B = 50 microtesla (50 uT). Khi chim bay qua vùng có dây điện cao thế phát ra từ trường nhân tạo lên tới 200 microtesla, chim có hiện tượng bay vòng tròn mất phương hướng. Cường độ từ trường nhân tạo này gấp bao nhiêu lần từ trường Trái Đất tại nơi đó?", ["4 lần", "2 lần", "5 lần", "8 lần"], 0, "Tỉ số cường độ từ trường = 200 / 50 = 4 lần."),
        make_vdc(3, "Để phân loại quặng sắt trong công nghiệp khai khoáng: Băng chuyền chở quặng hỗn hợp chạy qua quả lô từ tính (nam châm điện hình trụ quay). Quặng chứa hàm lượng sắt cao bị quả lô từ hút bám dính vào băng chuyền đưa sang máng A, đất đá trơ rơi thẳng xuống máng B. Biện pháp nào sau đây giúp tăng tỉ lệ thu hồi quặng sắt vụn nhỏ mịn trên băng chuyền?", ["Tăng cường độ dòng điện qua các cuộn dây của quả lô từ để tăng lực hút từ", "Tăng tốc độ chạy của băng chuyền lên gấp đôi", "Tưới thêm thật nhiều nước lạnh lên băng chuyền", "Đổi quả lô từ bằng quả lô cao su"], 0, "Tăng cường độ dòng điện làm từ trường quả lô mạnh hơn, hút giữ được các hạt quặng sắt nhỏ mịn tốt hơn."),
        make_vdc(4, "Một thanh nam châm thẳng bị gỉ sét làm mất hết các kí hiệu màu sơn đánh dấu cực Bắc và cực Nam. Một học sinh dùng một sợi chỉ mảnh buộc vào chính giữa thanh nam châm rồi treo lơ lửng trên giá gỗ cách xa các vật kim loại. Khi thanh nam châm dừng dao động và đứng yên thăng bằng, đầu thanh chỉ về hướng Bắc địa lý của Trái Đất chính là cực gì của nam châm?", ["Cực Bắc (N) của nam châm", "Cực Nam (S) của nam châm", "Cực trung hòa của nam châm", "Không xác định được"], 0, "Theo định nghĩa, đầu của nam châm tự do chỉ về phương Bắc địa lý được gọi là cực Bắc (N) của nam châm.")
    ]
}

# --- ĐỀ 4 ---
c6_rev_exams["phys7_c6_rev_test4"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 04",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 4, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Nam châm thể hiện tính chất từ bằng khả năng hút mạnh các vật làm bằng chất nào sau đây?", ["Chất sắt từ như sắt, niken, coban, thép", "Chất cách điện như nhựa, cao su", "Kim loại quý như vàng, bạc", "Kim loại nhẹ như nhôm, titan"], 0, "Nam châm hút các vật liệu sắt từ như sắt, thép, coban, niken."),
        make_mc(2, "Nhận biết", "Các đường sức từ trong không gian cho phép chúng ta hình dung trực quan về đặc điểm nào của từ trường?", ["Hình dạng, hướng và độ mạnh yếu của từ trường", "Nhiệt độ của vùng không gian có từ trường", "Vận tốc di chuyển của từ trường", "Màu sắc của từ trường"], 0, "Đường sức từ mô tả trực quan hình dạng, hướng và độ dày/thưa (mạnh/yếu) của từ trường."),
        make_mc(3, "Nhận biết", "Bên ngoài thanh nam châm thẳng, đường sức từ có chiều đi ra từ cực nào và đi vào cực nào?", ["Đi ra từ cực Bắc và đi vào cực Nam", "Đi ra từ cực Nam và đi vào cực Bắc", "Đi ra từ hai đầu và đi vào giữa", "Đi ra từ giữa và đi vào hai đầu"], 0, "Quy ước: Ra Bắc (N) vào Nam (S)."),
        make_mc(4, "Nhận biết", "Tại bất kì vị trí nào trên Trái Đất, kim nam châm của la bàn luôn có xu hướng định hướng theo phương nào?", ["Phương Bắc - Nam từ trường", "Phương Đông - Tây", "Phương gió thổi", "Phương đường xích đạo"], 0, "Kim la bàn luôn định hướng theo đường sức từ của Trái Đất (phương Bắc - Nam từ trường)."),
        make_mc(5, "Nhận biết", "Tác dụng từ của dòng điện lần đầu tiên trong lịch sử khoa học được phát hiện bởi nhà bác học nào?", ["Hans Christian Oersted", "Isaac Newton", "Michael Faraday", "Albert Einstein"], 0, "Năm 1820, Oersted phát hiện dòng điện làm lệch kim nam châm."),
        make_mc(6, "Nhận biết", "Khi quấn dây dẫn quanh đinh sắt rồi nối pin, nếu ngắt nguồn pin thì đinh sắt sẽ như thế nào?", ["Mất hầu hết từ tính ngay lập tức", "Biến thành nam châm vĩnh cửu hút cực mạnh", "Phát sáng màu vàng", "Nóng chảy ngay"], 0, "Đinh sắt non mất từ tính gần như ngay lập tức khi ngắt dòng điện."),
        make_mc(7, "Nhận biết", "Đặc điểm nào sau đây là ưu thế vượt trội của nam châm điện mà nam châm vĩnh cửu KHÔNG CÓ?", ["Có thể dễ dàng bật tắt từ tính và điều chỉnh lực hút bằng dòng điện", "Không cần dây dẫn điện", "Không bao giờ bị nóng lên", "Lực hút luôn giữ nguyên một mức duy nhất"], 0, "Nam châm điện điều khiển được từ tính thông qua công tắc và cường độ dòng điện."),
        make_mc(8, "Thông hiểu", "Để bảo vệ các thiết bị đo điện tử cực kì nhạy cảm khỏi bị ảnh hưởng bởi từ trường mạnh bên ngoài, người ta thường dùng biện pháp nào?", ["Đặt thiết bị bên trong một hộp kín làm bằng sắt non mềm (màn chắn từ)", "Bọc thiết bị bằng vải bông dày", "Sơn màu đỏ lên vỏ thiết bị", "Đặt thiết bị dưới nước"], 0, "Vỏ sắt non có độ dẫn từ rất cao, hút các đường sức từ chạy bên trong vỏ hộp, che chắn không gian bên trong."),
        make_mc(9, "Thông hiểu", "Trong một chiếc rơ le điện từ, bộ phận nào đóng vai trò tạo ra lực hút để đóng ngắt mạch điện tự động?", ["Nam châm điện", "Lò xo lá thép", "Bóng đèn sợi đốt", "Cầu chì thủy tinh"], 0, "Nam châm điện tạo ra lực từ hút lẫy sắt đóng ngắt mạch điện."),
        make_mc(10, "Thông hiểu", "Khi hai cực Bắc của hai thanh nam châm được đưa lại gần nhau thì lực tương tác giữa chúng là lực gì?", ["Lực đẩy", "Lực hút", "Lực ma sát", "Lực đàn hồi"], 0, "Các cực cùng tên thì đẩy nhau."),
        make_mc(11, "Thông hiểu", "Các cơn bão từ phát sinh từ hoạt động của Mặt Trời gây ra tác hại chủ yếu nào đối với đời sống công nghệ con người?", ["Gây nhiễu loạn liên lạc vô tuyến, mất sóng GPS và có thể phá hỏng lưới truyền tải điện", "Gây động đất và núi lửa phun trào", "Làm nước biển đóng băng", "Làm các tòa nhà cao ốc bị đổ sập"], 0, "Bão từ gây cảm ứng từ trường biến thiên mạnh làm hư hỏng lưới điện và viễn thông vệ tinh."),
        make_mc(12, "Thông hiểu", "Đồ vật nào sau đây KHÔNG CHỨA nam châm trong cấu tạo của nó?", ["Chiếc cốc bằng thủy tinh chịu nhiệt", "Chiếc loa nghe nhạc mini", "Cánh cửa tủ lạnh gia đình", "Chiếc la bàn bỏ túi"], 0, "Cốc thủy tinh hoàn toàn không chứa nam châm.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các quy tắc xác định cực từ và chiều của đường sức từ:", [
            ("a", "Bên ngoài nam châm, đường sức từ đi ra từ cực Bắc và đi vào cực Nam.", True),
            ("b", "Bên trong lòng thanh nam châm, đường sức từ đi từ cực Nam sang cực Bắc tạo thành đường cong khép kín.", True),
            ("c", "Hai đường sức từ bất kì trong cùng một từ trường không bao giờ cắt nhau.", True),
            ("d", "Nơi nào đường sức từ thưa thớt thì từ trường tại nơi đó là cực mạnh.", False)
        ], "Nơi đường sức từ thưa thớt là nơi từ trường yếu; nơi dày đặc là từ trường mạnh."),
        make_tf(2, "Thông hiểu", "Về hiện tượng nhiễm từ và phân loại chất từ trong kỹ thuật:", [
            ("a", "Sắt non, thép, niken và coban là các chất sắt từ bị nam châm hút mạnh.", True),
            ("b", "Đồng, nhôm, gỗ, thủy tinh không bị nhiễm từ trong điều kiện thông thường.", True),
            ("c", "Khi cọ xát một thanh thép nhiều lần theo một chiều vào cực nam châm, thanh thép sẽ bị nhiễm từ trở thành nam châm.", True),
            ("d", "Có thể biến một chiếc thước kẻ nhựa thành nam châm vĩnh cửu bằng cách đặt vào lòng ống dây có dòng điện.", False)
        ], "Nhựa là chất cách điện phi từ tính, không thể bị từ hóa thành nam châm."),
        make_tf(3, "Vận dụng", "Về cấu trúc từ quyển của Trái Đất và vai trò che chở sự sống:", [
            ("a", "Từ quyển Trái Đất kéo dài và bị gió Mặt Trời ép dẹp ở phía ban ngày, kéo dài thành đuôi từ ở phía ban đêm.", True),
            ("b", "Từ trường Trái Đất ngăn cản các hạt bức xạ vũ trụ nguy hiểm bắn phá trực tiếp lên bề mặt Trái Đất.", True),
            ("c", "Nếu Trái Đất mất đi từ trường, bầu khí quyển và sự sống sẽ đứng trước nguy cơ bị bức xạ vũ trụ hủy diệt.", True),
            ("d", "Cực Bắc từ trường Trái Đất trùng khít tuyệt đối 100% với điểm cực Bắc địa lý của quả địa cầu.", False)
        ], "Cực Bắc từ trường Trái Đất lệch xa cực Bắc địa lý hàng trăm kilômét."),
        make_tf(4, "Vận dụng", "Về ứng dụng của nam châm điện trong hệ thống phanh hãm của đoàn tàu cao tốc:", [
            ("a", "Hệ thống phanh điện từ sử dụng các nam châm điện cực mạnh hạ sát mặt ray thép.", True),
            ("b", "Tương tác từ tạo ra lực cản hãm đoàn tàu dừng lại mà không gây mài mòn cơ học má phanh.", True),
            ("c", "Khi cần nhả phanh để tàu chạy tiếp, người lái tàu chỉ cần ngắt dòng điện cung cấp cho nam châm điện.", True),
            ("d", "Phanh điện từ chỉ hoạt động được khi đường ray tàu hỏa được đúc bằng gỗ nguyên khối.", False)
        ], "Đường ray bắt buộc phải bằng thép để tạo tương tác từ và dòng điện xoáy hãm phanh.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một thanh nam châm thẳng có 2 cực. Nếu ta đem 4 thanh nam châm giống hệt nhau ghép nối tiếp đuôi nhau (cực Bắc thanh này nối vào cực Nam thanh kia) thành một thanh dài duy nhất. Hỏi thanh dài mới này có tổng cộng bao nhiêu cực từ ở hai đầu ngoài cùng?", "2", "Khi ghép nối tiếp, các cực ở chỗ nối triệt tiêu lẫn nhau, thanh dài mới trở thành một nam châm duy nhất có đúng 2 cực (1 Bắc và 1 Nam) ở hai đầu tự do."),
        make_sa(2, "Thông hiểu", "Một cuộn dây nam châm điện quấn 75 vòng dây hút được 15 chiếc kẹp giấy. Nếu muốn nam châm hút được 30 chiếc kẹp giấy với cùng nguồn điện đó thì cần quấn cuộn dây có tổng cộng bao nhiêu vòng quấn?", "150", "Số kẹp giấy tăng gấp 2 lần (30 / 15 = 2) nên số vòng quấn cần tăng gấp 2 lần: 75 x 2 = 150 vòng."),
        make_sa(3, "Thông hiểu", "Một nhà thám hiểm sử dụng la bàn tại một hòn đảo có góc lệch từ thiên giữa kinh tuyến từ và kinh tuyến thực là 2,5 độ. Đổi góc lệch này ra đơn vị phút góc (kí hiệu là ')?", "150", "1 độ = 60 phút. Do đó 2,5 độ = 2,5 x 60 = 150'."),
        make_sa(4, "Thông hiểu", "Một cần cẩu nam châm điện dọn phế liệu nâng được 6 khối thép, mỗi khối có khối lượng 350 kg. Tổng khối lượng phế liệu thép mà cần cẩu đã nâng trong chuyến này là bao nhiêu kilôgam (kg)?", "2100", "Tổng khối lượng = 6 x 350 = 2100 kg."),
        make_sa(5, "Thông hiểu", "Trong một hộp dụng cụ có 5 que kim loại cùng kích thước: que 1 bằng thép, que 2 bằng nhôm, que 3 bằng niken, que 4 bằng chì, que 5 bằng bạc. Hỏi có bao nhiêu que kim loại KHÔNG BỊ nam châm hút?", "3", "Có 3 que không bị hút là: que 2 (nhôm), que 4 (chì), que 5 (bạc)."),
        make_sa(6, "Thông hiểu", "Trong mạch điện thí nghiệm, khi điều chỉnh biến trở làm cường độ dòng điện chạy qua nam châm điện tăng từ 0,5 A lên 2,0 A. Hỏi cường độ dòng điện đã tăng lên gấp bao nhiêu lần?", "4", "Số lần tăng = 2,0 / 0,5 = 4 lần.")
    ],
    "part4": [
        make_vdc(1, "Hiện tượng màn chắn từ: Một đồng hồ cơ khí đắt tiền có các bánh răng thép siêu nhỏ được bọc trong một lớp vỏ bằng sắt non mềm dày 1,2 mm. Khi người đeo đồng hồ đi vào khu vực chụp cộng hưởng từ MRI có từ trường rất mạnh 1,5 Tesla, đồng hồ vẫn chạy hoàn toàn chính xác. Nguyên nhân khoa học của hiện tượng này là gì?", ["Lớp vỏ sắt non có độ thẩm từ rất lớn, hút hầu như toàn bộ các đường sức từ chạy khép kín bên trong lớp vỏ kim loại, bảo vệ bộ máy bên trong", "Lớp vỏ sắt non đẩy lùi hoàn toàn các đường sức từ ra xa như gương phản xạ", "Sắt non làm đóng băng từ trường không cho chuyển động", "Từ trường MRI không tương tác với kim loại thép"], 0, "Sắt non hút các đường sức từ tập trung chạy trong thân vỏ sắt, làm không gian rỗng bên trong hầu như không còn từ trường (màn chắn từ)."),
        make_vdc(2, "Trên đường ray tàu đệm từ Maglev: Một khối toa tàu nặng 40 tấn cần được nâng lên khỏi mặt ray một khe hở 10 mm. Khi dòng điện qua hệ thống nam châm nâng là 200 A thì lực nâng cân bằng vừa đúng trọng lực toa tàu. Nếu khối lượng hành khách và hàng hóa chở thêm là 10 tấn (tổng 50 tấn) thì dòng điện qua nam châm nâng cần điều chỉnh lên mức bao nhiêu ampe để duy trì khe hở nâng (coi lực từ tỉ lệ thuận với dòng điện)?", ["250 A", "220 A", "300 A", "240 A"], 0, "Tỉ số trọng lượng = 50 / 40 = 1,25 lần. Cường độ dòng điện cần điều chỉnh = 200 x 1,25 = 250 A."),
        make_vdc(3, "Thiết kế mạch cảnh báo rò rỉ khí gas tự động trong chung cư: Cảm biến phát hiện nồng độ gas tăng sẽ đóng công tắc cấp điện 12 V cho cuộn dây nam châm điện. Nam châm điện hút chốt thép an toàn trong 0,05 giây làm sập lò xo ngắt van gas tổng, đồng thời đóng mạch phụ kích hoạt còi hú 110 dB. Yêu cầu vật liệu làm lõi nam châm điện trong hệ thống này bắt buộc phải là:", ["Sắt non mềm để hút dứt khoát và nhả chốt khi cần thiết lập lại hệ thống", "Thép tôi cứng vĩnh cửu", "Thanh đồng thau nguyên khối", "Thanh nhôm đúc"], 0, "Lõi sắt non có độ cảm từ cao, đáp ứng nhanh và dễ dàng hồi phục vị trí khi reset hệ thống."),
        make_vdc(4, "Xét từ trường tạo bởi hai cực khác tên (cực Bắc N của thanh 1 và cực Nam S của thanh 2) đặt đối diện nhau và cách nhau một khoảng hở hẹp 3 cm. Hình ảnh đường sức từ trong khoảng không gian 3 cm giữa hai cực này có đặc điểm gì?", ["Là những đường thẳng gần như song song, cách đều nhau và hướng thẳng từ cực Bắc của thanh 1 sang cực Nam của thanh 2", "Là những đường tròn xoắn ốc ngược chiều kim đồng hồ", "Đường sức từ uốn cong ra xa tránh né hai cực", "Đường sức từ biến mất hoàn toàn do triệt tiêu nhau"], 0, "Giữa hai cực khác tên đặt gần nhau, các đường sức từ đi thẳng song song từ cực Bắc sang cực Nam tạo thành từ trường đều.")
    ]
}

# --- ĐỀ 5 ---
c6_rev_exams["phys7_c6_rev_test5"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 05",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 5, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Khi cọ xát một đầu thanh nam châm vào chiếc kim may bằng thép nhiều lần theo một chiều nhất định, chiếc kim sẽ:", ["Bị nhiễm từ và trở thành một nam châm nhỏ giữ được từ tính", "Nóng chảy thành chất lỏng", "Bị biến mất", "Mất hết khả năng dẫn điện"], 0, "Thép khi bị cọ xát với nam châm sẽ bị nhiễm từ trở thành nam châm vĩnh cửu."),
        make_mc(2, "Nhận biết", "Đặc điểm cơ bản quan trọng của các đường sức từ trong từ trường là:", ["Là những đường cong khép kín hoặc đi từ vô cực đến vô cực, không bao giờ cắt nhau", "Luôn cắt nhau tại một điểm duy nhất", "Là các đường gấp khúc sắc nhọn", "Là các đoạn thẳng hở hai đầu"], 0, "Đường sức từ là những đường cong khép kín không cắt nhau."),
        make_mc(3, "Nhận biết", "Ở ngay tại vùng cực từ của Trái Đất, kim nam châm của một la bàn đa năng có xu hướng định hướng theo phương nào?", ["Phương gần như thẳng đứng cắm xuống mặt đất", "Phương nằm ngang song song mặt đất", "Phương tạo góc 45 độ với mặt đất", "Quay tít liên tục không dừng"], 0, "Tại các cực từ, đường sức từ đâm thẳng đứng vào hoặc đi thẳng ra khỏi mặt đất nên kim la bàn chúc thẳng đứng."),
        make_mc(4, "Nhận biết", "Yếu tố nào sau đây quyết định chiều của đường sức từ xung quanh một cuộn dây có dòng điện chạy qua?", ["Chiều của dòng điện chạy qua các vòng dây", "Chiều dài của sợi dây dẫn quấn ống dây", "Màu sắc lớp sơn phủ cách điện", "Độ dày của đế đỡ"], 0, "Chiều đường sức từ của ống dây phụ thuộc trực tiếp vào chiều dòng điện qua các vòng dây."),
        make_mc(5, "Nhận biết", "Một nam châm điện đang được cấp điện có thể hút được vật liệu nào sau đây?", ["Mảnh sắt phế liệu và bu-lông thép", "Mẩu gỗ vụn khô", "Cốc nhựa dùng một lần", "Mẩu gạch ngói vỡ"], 0, "Nam châm hút các vật liệu từ như sắt, thép."),
        make_mc(6, "Nhận biết", "Tại sao người ta không dùng bạc nguyên chất để chế tạo lõi nam châm điện?", ["Vì bạc là chất không có tính sắt từ, không bị nhiễm từ để làm tăng từ trường", "Vì bạc quá nhẹ", "Vì bạc không dẫn điện", "Vì bạc có màu trắng"], 0, "Bạc không phải chất sắt từ nên không khuếch đại được từ trường."),
        make_mc(7, "Nhận biết", "Dụng cụ hoặc thiết bị nào dưới đây biến năng lượng điện thành chuyển động quay cơ học nhờ lực từ?", ["Động cơ điện mini", "Bếp nướng điện", "Nồi cơm điện gia đình", "Bàn là khô"], 0, "Động cơ điện biến điện năng thành cơ năng nhờ lực từ tác dụng lên cuộn dây mang dòng điện."),
        make_mc(8, "Thông hiểu", "Trong thí nghiệm tạo từ phổ bằng mạt sắt, hành động dùng ngón tay gõ nhẹ vào tấm bìa nhằm mục đích gì?", ["Làm giảm ma sát nghỉ giúp các mạt sắt dễ dàng xoay và sắp xếp theo các đường sức từ", "Làm nóng các hạt mạt sắt", "Làm nam châm nhiễm điện tĩnh", "Để các hạt mạt sắt dính chặt vào bìa"], 0, "Gõ nhẹ giúp giảm ma sát để mạt sắt sắp xếp trật tự theo đường sức từ."),
        make_mc(9, "Thông hiểu", "Để phân biệt cực Bắc và cực Nam của một thanh nam châm lạ không được sơn màu hay đánh dấu, phương pháp chuẩn xác nhất là:", ["Treo thanh nam châm bằng sợi chỉ mảnh ở giữa để thanh tự do định hướng Bắc - Nam địa lí", "Cân khối lượng hai đầu xem đầu nào nặng hơn", "Nhúng thanh vào chậu nước xem đầu nào nổi", "Đo nhiệt độ hai đầu"], 0, "Đầu thanh nam châm tự do quay về hướng Bắc địa lí chính là cực Bắc của nam châm."),
        make_mc(10, "Thông hiểu", "Nam châm điện dạng hình chữ U có ưu điểm vượt trội hơn nam châm thẳng ở điểm nào?", ["Cả hai cực Bắc và Nam cùng hướng về một phía tiếp xúc hút vật, tăng gấp đôi lực giữ cơ học", "Tiêu tốn ít điện năng hơn 100 lần", "Không cần dùng dây dẫn điện", "Nhẹ hơn nam châm thẳng"], 0, "Hai cực cùng tiếp xúc giúp tăng lực giữ tiếp xúc lên vật gấp nhiều lần."),
        make_mc(11, "Thông hiểu", "Khi chùm hạt điện tích từ gió Mặt Trời bay đến Trái Đất, lực từ của từ trường Trái Đất tác dụng làm chúng:", ["Bị lệch quỹ đạo và bị cuốn xoắn ốc về hai vùng cực tạo nên cực quang", "Bị phản xạ ngược lại Mặt Trời", "Rơi thẳng xuống đường xích đạo", "Tăng tốc độ bay xuyên thủng lòng đất"], 0, "Lực Lorentz của từ trường Trái Đất bẻ cong quỹ đạo hạt tích điện cuốn về hai cực sinh ra hiện tượng cực quang."),
        make_mc(12, "Thông hiểu", "Vật thể nào sau đây hoàn toàn KHÔNG BỊ ảnh hưởng bởi từ trường của một nam châm đặt ngay sát bên cạnh nó?", ["Một viên bi ve bằng thủy tinh trong suốt", "Một chiếc đinh sắt nhỏ", "Một chiếc kim khâu bằng thép", "Một chiếc kẹp tài liệu bằng niken"], 0, "Thủy tinh không có tính sắt từ nên hoàn toàn không bị ảnh hưởng bởi từ trường.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về phương pháp xác định cực từ và sự phân bố từ trường của nam châm:", [
            ("a", "Có thể dùng một kim la bàn đã biết rõ cực Bắc để xác định cực của một thanh nam châm lạ.", True),
            ("b", "Cực Bắc của kim la bàn bị đẩy bởi cực Bắc của thanh nam châm lạ.", True),
            ("c", "Từ trường xung quanh nam châm có thể nhìn thấy trực tiếp bằng mắt thường mà không cần mạt sắt hay la bàn.", False),
            ("d", "Đường sức từ càng dày đặc thì từ trường tại đó càng mạnh.", True)
        ], "Từ trường là môi trường vô hình, không thể nhìn thấy trực tiếp bằng mắt thường nếu không dùng dụng cụ thử."),
        make_tf(2, "Thông hiểu", "Về ảnh hưởng của nhiệt độ cao đến tính chất từ của nam châm vĩnh cửu:", [
            ("a", "Khi bị nung nóng đến nhiệt độ rất cao (nhiệt độ Curie), nam châm vĩnh cửu sẽ bị mất hết từ tính.", True),
            ("b", "Đối với sắt và thép, nhiệt độ mất từ tính hoàn toàn (nhiệt độ Curie) vào khoảng trên 700 độ C.", True),
            ("c", "Khi gõ đập mạnh nhiều lần bằng búa kim loại, nam châm cũng có thể bị suy giảm từ tính.", True),
            ("d", "Nung nóng nam châm trong lò lửa đỏ rực sẽ làm nam châm hút sắt mạnh gấp mười lần.", False)
        ], "Nung nóng làm các nguyên tử dao động nhiệt hỗn loạn, phá vỡ trật tự từ tính làm nam châm mất từ tính."),
        make_tf(3, "Vận dụng", "Về ứng dụng của từ trường Trái Đất trong định vị và dẫn đường hàng hải:", [
            ("a", "La bàn từ là dụng cụ dẫn đường không thể thiếu của thủy thủ từ hàng nghìn năm nay.", True),
            ("b", "Khi đi tàu ngầm sâu dưới đại dương, sóng GPS vệ tinh không truyền tới được nên định vị bằng la bàn từ và con quay quán tính đóng vai trò sống còn.", True),
            ("c", "Trên các bản đồ hàng hải quân sự luôn có ghi chú độ lệch từ thiên để thuyền trưởng hiệu chỉnh phương vị chuẩn xác.", True),
            ("d", "La bàn từ chỉ hoạt động được khi tàu thuyền được làm hoàn toàn bằng sắt nguyên khối.", False)
        ], "Thân tàu bằng sắt quá nhiều thậm chí còn làm lệch kim la bàn, phải đặt các khối cầu bù từ chuyên dụng."),
        make_tf(4, "Vận dụng", "Về sự biến đổi và chuyển hóa năng lượng trong thiết bị dùng nam châm điện:", [
            ("a", "Trong chuông điện, điện năng được chuyển hóa một phần thành cơ năng gõ búa và thành năng lượng âm thanh.", True),
            ("b", "Trong rơ le điện từ, năng lượng điện của cuộn dây chuyển hóa thành cơ năng hút lẫy tiếp điểm.", True),
            ("c", "Trong động cơ điện, điện năng được chuyển hóa thành cơ năng chuyển động quay.", True),
            ("d", "Hiệu suất chuyển hóa năng lượng của nam châm điện luôn đạt 100%, hoàn toàn không có tỏa nhiệt hao phí.", False)
        ], "Dây quấn có điện trở nên luôn có tỏa nhiệt hao phí theo định luật Joule - Lenz.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một thanh thép sau khi từ hóa trở thành một thanh nam châm có 2 cực. Nếu người ta cưa thanh thép này thành 5 đoạn ngắn bằng nhau thì tổng số cực từ của 5 đoạn nam châm mới là bao nhiêu cực?", "10", "Mỗi đoạn nam châm mới có 2 cực từ (1 Bắc, 1 Nam). Do đó 5 đoạn có tổng cộng: 5 x 2 = 10 cực."),
        make_sa(2, "Thông hiểu", "Một cuộn dây nam châm điện quấn 60 vòng hút được 9 viên bi thép nhỏ. Nếu muốn cuộn dây hút được 27 viên bi thép với cùng nguồn điện và điều kiện thí nghiệm thì cuộn dây cần có bao nhiêu vòng quấn?", "180", "Số bi thép tăng gấp 3 lần (27 / 9 = 3) nên số vòng quấn cần tăng gấp 3 lần: 60 x 3 = 180 vòng."),
        make_sa(3, "Thông hiểu", "Một chiếc la bàn hàng hải có vòng chia độ 360 độ quanh mặt số. Khi một con tàu chuyển hướng di chuyển từ hướng chính Bắc (0 độ) sang hướng chính Đông, kim la bàn đã quay một góc bao nhiêu độ?", "90", "Góc quay từ hướng Bắc sang hướng Đông là góc vuông: 90 độ."),
        make_sa(4, "Thông hiểu", "Một chiếc cần cẩu nam châm điện tại bến cảng nhấc bổng một chiếc bồn chứa phế liệu thép có khối lượng 3,6 tấn. Khối lượng bồn phế liệu này quy đổi ra đơn vị kilôgam (kg) là bao nhiêu?", "3600", "3,6 tấn = 3,6 x 1000 = 3600 kg."),
        make_sa(5, "Thông hiểu", "Trong 6 chất sau đây: (1) Sắt; (2) Nhôm; (3) Coban; (4) Thủy tinh; (5) Niken; (6) Cao su tự nhiên. Hỏi có bao nhiêu chất là chất sắt từ bị nam châm hút mạnh?", "3", "Có 3 chất sắt từ là: (1) sắt, (3) coban, (5) niken."),
        make_sa(6, "Thông hiểu", "Trong mạch điện điều khiển nam châm điện, ampe kế đo được dòng điện tăng từ 0,2 A lên 0,8 A khi người thực hành gạt con chạy của biến trở. Hỏi cường độ dòng điện qua nam châm điện đã tăng thêm bao nhiêu ampe (A)?", "0,6", "Cường độ tăng thêm = 0,8 - 0,2 = 0,6 A.")
    ],
    "part4": [
        make_vdc(1, "Thí nghiệm nhiệt độ Curie: Một thanh nam châm thép vĩnh cửu hút chặt một chiếc đinh sắt treo bằng sợi chỉ mảnh. Dùng ngọn lửa đèn khò đốt thanh nam châm đến khi thanh phát sáng đỏ rực (khoảng 780 độ C), chiếc đinh sắt bỗng nhiên rơi tuột xuống đất. Giải thích nguyên nhân vật lý cốt lõi của hiện tượng này:", ["Nhiệt độ cao kích thích dao động nhiệt hỗn loạn của các phân tử, phá vỡ trật tự từ tính định hướng nội tại làm thanh thép mất hoàn toàn từ tính", "Nhiệt độ cao làm bay hơi toàn bộ chiếc đinh sắt", "Ngọn lửa đèn khò sinh ra gió đẩy chiếc đinh rơi xuống", "Sợi chỉ treo bị đứt do nhiệt"], 0, "Ở nhiệt độ trên điểm Curie (770 độ C với sắt thép), dao động nhiệt phá hủy trật tự định hướng của các mômen từ làm vật liệu mất từ tính hoàn toàn."),
        make_vdc(2, "Một cần cẩu nam châm điện nâng thẳng đứng một khối phế liệu thép nặng 2 tấn lên cao 5 mét với vận tốc đều trong thời gian 10 giây. Lấy gia tốc trọng trường g = 10 m/s2. Công cơ học tối thiểu mà lực hút của nam châm điện đã thực hiện để nâng khối thép này lên là bao nhiêu kilôjun (kJ)?", ["100 kJ", "50 kJ", "200 kJ", "20 kJ"], 0, "Trọng lượng P = 2000 kg x 10 = 20 000 N. Công nâng A = P x h = 20 000 N x 5 m = 100 000 J = 100 kJ."),
        make_vdc(3, "Nguyên lí lưu trữ dữ liệu bằng từ tính: Bề mặt đĩa cứng máy tính (HDD) được phủ một lớp màng từ tính siêu mỏng gồm hàng tỉ ô từ cực nhỏ. Đầu đọc/ghi là một nam châm điện vi mô. Khi ghi dữ liệu nhị phân '0' và '1', đầu ghi thực hiện thao tác nào sau đây?", ["Đổi chiều dòng điện qua cuộn vi mô để định hướng chiều từ hóa ngược nhau cho từng ô từ tương ứng với bit 0 hoặc bit 1", "Dùng tia laser đốt cháy các ô từ", "Dùng mực in nano đánh dấu màu sắc", "Dùng điện cao áp đục lỗ trên bề mặt đĩa"], 0, "Đổi chiều dòng điện trong nam châm điện đầu ghi làm đổi chiều từ hóa của ô từ biểu diễn bit 0 và bit 1."),
        make_vdc(4, "Ảnh hưởng của bão từ lên các đường ống dẫn dầu bằng kim loại xuyên lục địa: Khi xảy ra bão từ cực mạnh, từ trường biến thiên xuyên qua mặt đất cảm ứng sinh ra dòng điện chạy dọc thân đường ống thép dài hàng nghìn kilômét. Dòng điện cảm ứng này gây ra nguy cơ nghiêm trọng nào cho đường ống?", ["Tăng tốc độ ăn mòn điện hóa kim loại làm thủng đường ống gây rò rỉ dầu thô ra môi trường", "Làm đông cứng dầu thô bên trong đường ống", "Làm đường ống biến thành vàng nguyên chất", "Làm đường ống bay lơ lửng lên không trung"], 0, "Dòng điện cảm ứng biến thiên chạy trong ống kim loại chôn dưới đất thúc đẩy mạnh phản ứng ăn mòn điện hóa gây rò rỉ thủng ống.")
    ]
}
