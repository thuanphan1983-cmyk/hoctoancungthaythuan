# -*- coding: utf-8 -*-
"""
CHƯƠNG VI: TỪ - BÀI 20: CHẾ TẠO NAM CHÂM ĐIỆN ĐƠN GIẢN (3 ĐỀ ĐỘC LẬP 100%)
- phys7_c6_b20: Bài 20: Chế tạo nam châm điện đơn giản (3 đề: test1, test2, test3)
Không trùng lặp, không tiền tố "Đề X - "
"""

from builder_phys7_c3_b8_b9 import make_mc, make_tf, make_sa, make_vdc

b20_exams = {}

# =========================================================================
# BÀI 20: CHẾ TẠO NAM CHÂM ĐIỆN ĐƠN GIẢN (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b20_exams["phys7_c6_b20_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 20: Chế tạo nam châm điện đơn giản - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b20", "lessonName": "Bài 20: Chế tạo nam châm điện đơn giản",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Cấu tạo cơ bản của một nam châm điện đơn giản bao gồm những bộ phận nào?", ["Một cuộn dây dẫn bọc cách điện quấn quanh một lõi sắt non và nguồn điện", "Hai thanh nam châm vĩnh cửu gắn đối diện nhau", "Một thanh đồng nối với hai cực của bóng đèn", "Một sợi dây cao su dẫn điện quấn quanh đinh nhôm"], 0, "Nam châm điện gồm cuộn dây dẫn bọc cách điện quấn quanh lõi sắt non, khi có dòng điện chạy qua thì sinh ra từ trường."),
        make_mc(2, "Nhận biết", "Tác dụng nào của dòng điện được ứng dụng trực tiếp để chế tạo nam châm điện?", ["Tác dụng từ", "Tác dụng nhiệt", "Tác dụng phát sáng", "Tác dụng hóa học"], 0, "Dòng điện chạy qua dây dẫn sinh ra từ trường xung quanh (tác dụng từ)."),
        make_mc(3, "Nhận biết", "Bộ phận nào trong nam châm điện có vai trò làm tăng cường độ mạnh của từ trường lên rất nhiều lần?", ["Lõi sắt non", "Lớp vỏ nhựa bọc ngoài", "Công tắc ngắt điện", "Dây chỉ buộc cố định"], 0, "Lõi sắt non bị nhiễm từ mạnh, tăng cường tác dụng từ của cuộn dây."),
        make_mc(4, "Nhận biết", "Hiện tượng gì xảy ra với từ tính của nam châm điện có lõi sắt non khi ngắt dòng điện chạy qua cuộn dây?", ["Từ tính biến mất gần như ngay lập tức", "Từ tính tăng gấp đôi", "Đảo ngược hai cực từ", "Vẫn giữ nguyên vĩnh viễn"], 0, "Khi ngắt dòng điện, lõi sắt non mất hầu hết từ tính ngay lập tức."),
        make_mc(5, "Nhận biết", "Để nhận biết cuộn dây dẫn quấn quanh đinh sắt đã trở thành nam châm điện hay chưa, ta có thể đưa đầu đinh lại gần:", ["Các kẹp ghim bằng thép hoặc kim la bàn", "Một mẩu gỗ khô", "Một mẩu nhựa xốp", "Một cốc nước tinh khiết"], 0, "Nam châm hút các vật liệu từ như kẹp ghim thép hoặc làm lệch kim la bàn."),
        make_mc(6, "Nhận biết", "Dây dẫn dùng để quấn nam châm điện bắt buộc phải có đặc điểm gì quan trọng?", ["Có lớp vỏ bọc cách điện bên ngoài", "Là dây đồng trần không bọc men", "Làm hoàn toàn bằng chất dẻo", "Phải là dây xích sắt"], 0, "Dây dẫn phải bọc men cách điện để dòng điện chạy xoắn ốc qua các vòng dây mà không bị chập ngắn mạch."),
        make_mc(7, "Thông hiểu", "Vì sao người ta thường dùng sắt non mà không dùng thép để làm lõi của nam châm điện?", ["Vì sắt non mất từ tính rất nhanh khi ngắt điện, còn thép giữ từ tính lâu biến thành nam châm vĩnh cửu", "Vì sắt non rẻ hơn thép", "Vì sắt non có màu sáng hơn thép", "Vì thép không dẫn điện"], 0, "Sắt non có tính khử từ nhanh, giúp việc đóng ngắt lực từ của nam châm điện diễn ra tức thì."),
        make_mc(8, "Thông hiểu", "Biện pháp nào sau đây giúp làm tăng lực từ của một nam châm điện?", ["Tăng số vòng dây quấn và tăng cường độ dòng điện", "Giảm số vòng dây quấn", "Rút bỏ lõi sắt non ra khỏi cuộn dây", "Giảm hiệu điện thế của nguồn điện"], 0, "Lực từ của nam châm điện tỉ lệ thuận với số vòng dây và cường độ dòng điện qua cuộn dây."),
        make_mc(9, "Thông hiểu", "Khi đổi chiều dòng điện chạy qua các vòng dây của nam châm điện thì điều gì sẽ xảy ra?", ["Vị trí các cực từ của nam châm điện bị đảo ngược", "Nam châm điện mất hết từ tính", "Lực từ tăng gấp đôi", "Cuộn dây bốc cháy ngay lập tức"], 0, "Đổi chiều dòng điện làm đảo chiều đường sức từ, dẫn đến các cực từ bị đảo ngược."),
        make_mc(10, "Thông hiểu", "Ưu điểm nổi bật nhất của cần cẩu dùng nam châm điện so với cần cẩu dùng móc sắt cơ học là gì?", ["Dễ dàng hút và thả phế liệu sắt thép bằng thao tác đóng/ngắt công tắc điện nhanh chóng", "Không tiêu thụ điện năng", "Hút được cả đất đá và bê tông", "Cần cẩu không bao giờ bị hỏng"], 0, "Cần cẩu nam châm điện chỉ cần đóng điện để hút và ngắt điện để thả hàng vạn mẩu sắt vụn cùng lúc."),
        make_mc(11, "Thông hiểu", "Nếu thay lõi sắt non của nam châm điện bằng một thanh gỗ hoặc thanh nhôm có cùng kích thước thì:", ["Từ trường của cuộn dây sẽ rất yếu, chỉ bằng từ trường của cuộn dây không lõi", "Từ trường tăng mạnh hơn lõi sắt", "Cuộn dây bị nổ", "Nam châm điện biến thành nam châm vĩnh cửu"], 0, "Gỗ và nhôm không phải là vật liệu từ nên không có tác dụng tăng cường từ trường."),
        make_mc(12, "Thông hiểu", "Một học sinh quấn 40 vòng dây quanh đinh sắt, nối với pin 1,5V hút được 4 đinh ghim nhỏ. Để hút được nhiều đinh ghim hơn với cùng đinh sắt đó, học sinh nên:", ["Quấn thêm nhiều vòng dây hơn và mắc nối tiếp thêm pin để tăng dòng điện", "Tháo bớt 20 vòng dây ra", "Thay pin 1,5V bằng pin 0,5V yếu hơn", "Rút đinh sắt ra ngoài"], 0, "Tăng số vòng dây và tăng cường độ dòng điện làm tăng lực hút của nam châm điện.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về cấu tạo và nguyên lý hoạt động của nam châm điện:", [
            ("a", "Nam châm điện chỉ thể hiện tính chất từ khi có dòng điện chạy qua cuộn dây.", True),
            ("b", "Lõi sắt non có tác dụng tập trung và khuếch đại đường sức từ của cuộn dây lên hàng trăm lần.", True),
            ("c", "Dây dẫn quấn trên nam châm điện có thể dùng dây đồng trần không bọc cách điện mà vẫn hoạt động bình thường.", False),
            ("d", "Khi ngắt dòng điện chạy qua ống dây có lõi sắt non, tác dụng từ bị mất đi gần như hoàn toàn.", True)
        ], "Nếu dùng dây trần không cách điện thì các vòng dây chạm nhau làm chập mạch đoản mạch."),
        make_tf(2, "Thông hiểu", "Về các yếu tố làm thay đổi độ mạnh của lực từ nam châm điện:", [
            ("a", "Tăng cường độ dòng điện chạy qua cuộn dây làm tăng lực hút của nam châm điện.", True),
            ("b", "Tăng số vòng dây quấn trên cùng một chiều dài lõi làm tăng lực từ của nam châm điện.", True),
            ("c", "Rút lõi sắt non ra khỏi cuộn dây làm lực từ của ống dây tăng vọt lên.", False),
            ("d", "Sử dụng lõi sắt non có tiết diện phù hợp giúp tăng hiệu quả hút giữ vật từ.", True)
        ], "Rút lõi sắt non ra làm từ trường giảm đi rất nhiều lần."),
        make_tf(3, "Vận dụng", "Thực hành chế tạo nam châm điện đơn giản trong phòng học KHTN:", [
            ("a", "Quấn dây đồng tráng men men đều tay theo một chiều quanh thân một chiếc bu-lông sắt.", True),
            ("b", "Cần cạo sạch lớp men cách điện ở hai đầu dây nối trước khi kẹp vào hai cực của pin.", True),
            ("c", "Nếu nối trực tiếp hai đầu dây vào nguồn điện sinh hoạt 220V xoay chiều sẽ rất an toàn và hút cực mạnh.", False),
            ("d", "Dùng la bàn kiểm tra thấy cực của nam châm điện đẩy cực Bắc của kim la bàn chứng tỏ đầu đó là cực Bắc.", True)
        ], "Tuyệt đối không cắm vào nguồn điện 220V vì gây đoản mạch chập cháy nguy hiểm chết người!"),
        make_tf(4, "Vận dụng", "Ứng dụng của nam châm điện trong các thiết bị công nghệ hiện đại:", [
            ("a", "Rơ le điện từ dùng nam châm điện để đóng ngắt mạch điện tự động từ xa hoặc bảo vệ an toàn.", True),
            ("b", "Chuông điện gia đình hoạt động nhờ cơ chế đóng ngắt mạch liên tục bằng nam châm điện và lá thép đàn hồi.", True),
            ("c", "Tàu đệm từ Maglev tận dụng lực từ cực mạnh của hệ thống nam châm điện để nâng đoàn tàu bay lơ lửng trên đường ray.", True),
            ("d", "Kim chỉ nam của chiếc la bàn bỏ túi truyền thống bắt buộc phải là một nam châm điện nối với pin siêu nhỏ.", False)
        ], "La bàn truyền thống dùng kim nam châm vĩnh cửu, không cần dùng pin hay nam châm điện.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một cuộn dây nam châm điện quấn 60 vòng hút được 12 chiếc kẹp ghim bằng thép. Nếu giữ nguyên dòng điện và tăng số vòng dây lên thành 120 vòng thì nam châm điện này hút được bao nhiêu chiếc kẹp ghim?", "24", "Số vòng tăng gấp đôi (120/60 = 2) nên lực từ xấp xỉ tăng gấp 2 lần, hút được 12 x 2 = 24 chiếc kẹp ghim."),
        make_sa(2, "Thông hiểu", "Khi nối nam châm điện với một nguồn pin có cường độ dòng điện 0,5 A thì nó hút được vật nặng tối đa 80 g. Khi tăng cường độ dòng điện lên 1,0 A thì khối lượng vật tối đa nam châm điện hút được xấp xỉ là bao nhiêu gam?", "160", "Dòng điện tăng gấp đôi (1,0 / 0,5 = 2) nên khối lượng hút tăng tương ứng: 80 x 2 = 160 g."),
        make_sa(3, "Thông hiểu", "Có bao nhiêu yếu tố trong các yếu tố sau đây ảnh hưởng đến độ mạnh của từ trường nam châm điện: (1) Cường độ dòng điện; (2) Số vòng quấn của ống dây; (3) Có lõi sắt non hay không; (4) Màu sắc lớp sơn cách điện của dây dẫn?", "3", "Có 3 yếu tố ảnh hưởng là (1), (2), (3). Yếu tố (4) màu sắc lớp sơn không ảnh hưởng."),
        make_sa(4, "Thông hiểu", "Một thợ điện cần quấn một cuộn nam châm điện có tổng cộng 200 vòng dây. Hiện người thợ đã quấn được 145 vòng. Hỏi người đó còn phải quấn thêm bao nhiêu vòng dây nữa để hoàn thành?", "55", "Số vòng cần quấn thêm = 200 - 145 = 55 vòng."),
        make_sa(5, "Thông hiểu", "Cần cẩu nam châm điện tại cảng dỡ hàng nâng được một khối thép công nghiệp nặng 2,5 tấn. Khối lượng thép này tương đương với bao nhiêu kilôgam (kg)?", "2500", "2,5 tấn = 2,5 x 1000 = 2500 kg."),
        make_sa(6, "Thông hiểu", "Trong một thí nghiệm, khi bật công tắc điện, nam châm điện hút dính 15 chiếc kẹp giấy. Sau khi ngắt công tắc điện, do đinh sắt có một chút từ dư nên vẫn còn dính lại 1 chiếc kẹp giấy. Hỏi có bao nhiêu chiếc kẹp giấy đã bị rơi ra ngay khi ngắt điện?", "14", "Số kẹp giấy rơi ra = 15 - 1 = 14 kẹp.")
    ],
    "part4": [
        make_vdc(1, "Một nhóm học sinh làm thí nghiệm khảo sát số đinh ghim hút được bởi nam châm điện với các thông số khác nhau: Thí nghiệm 1 (50 vòng, I = 0,4 A) hút 8 ghim; Thí nghiệm 2 (50 vòng, I = 0,8 A) hút 16 ghim; Thí nghiệm 3 (100 vòng, I = 0,4 A) hút 16 ghim; Thí nghiệm 4 (100 vòng, I = 0,8 A). Dựa vào quy luật trên, dự đoán số đinh ghim hút được ở Thí nghiệm 4 là bao nhiêu?", ["32 đinh ghim", "20 đinh ghim", "24 đinh ghim", "48 đinh ghim"], 0, "So với Thí nghiệm 1, Thí nghiệm 4 có số vòng tăng gấp 2 và cường độ tăng gấp 2 nên lực từ tăng xấp xỉ 4 lần: 8 x 4 = 32 đinh ghim."),
        make_vdc(2, "Trong rơ le điện từ dùng để đóng ngắt mạch điện bảo vệ máy bơm công suất lớn: Khi dòng điện chạy qua nam châm điện đạt giá trị định mức 5 A, lực hút của nam châm thắng lực kéo của lò xo đàn hồi (đang giữ lực kéo 12 N), hút thanh sắt đóng tiếp điểm phụ. Nếu muốn rơ le chỉ ngắt khi dòng điện chạm ngưỡng 7,5 A thì người kỹ thuật viên cần điều chỉnh lực kéo của lò xo lên mức nào (giả sử lực từ tỉ lệ thuận với dòng điện)?", ["18 N", "15 N", "24 N", "9 N"], 0, "Dòng điện tăng 7,5 / 5 = 1,5 lần nên lực từ đạt 12 x 1,5 = 18 N, lò xo phải tăng lực căng lên 18 N."),
        make_vdc(3, "Tại một bãi phế liệu, một cần cẩu điện sử dụng nam châm điện hình chữ U để dọn sắt vụn. Khi dùng nguồn điện 24 V, nam châm hút được mảng thép 360 kg. Do yêu cầu vận chuyển mảng thép lớn 540 kg, người ta phải tăng hiệu điện thế nguồn điện lên bao nhiêu vôn (V) để lực từ tăng tương ứng (coi điện trở cuộn dây không đổi, lực từ tỉ lệ thuận với hiệu điện thế)?", ["36 V", "30 V", "48 V", "28 V"], 0, "Tỉ lệ khối lượng = 540 / 360 = 1,5 lần. Hiệu điện thế cần tăng lên = 24 x 1,5 = 36 V."),
        make_vdc(4, "Một chuông điện tự ngắt hoạt động với tần số búa gõ là 25 lần trong mỗi giây (25 Hz). Hỏi trong thời gian 4 giây bấm giữ công tắc liên tục, búa của chuông điện đã thực hiện bao nhiêu lần gõ vào bát chuông kim loại?", ["100 lần", "50 lần", "75 lần", "25 lần"], 0, "Số lần gõ chuông = 25 lần/giây x 4 giây = 100 lần.")
    ]
}

# --- ĐỀ 2 ---
b20_exams["phys7_c6_b20_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 20: Chế tạo nam châm điện đơn giản - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b20", "lessonName": "Bài 20: Chế tạo nam châm điện đơn giản",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Khi có dòng điện chạy qua cuộn dây dẫn quấn quanh một chiếc đinh sắt, đinh sắt đó trở thành:", ["Một nam châm điện", "Một nam châm vĩnh cửu", "Một bóng đèn phát sáng", "Một chất cách điện"], 0, "Dòng điện chạy qua cuộn dây sinh ra từ trường làm đinh sắt trở thành nam châm điện."),
        make_mc(2, "Nhận biết", "Từ trường của nam châm điện chỉ tồn tại trong điều kiện nào?", ["Chỉ tồn tại trong thời gian có dòng điện chạy qua cuộn dây", "Luôn tồn tại vĩnh viễn kể cả khi tháo pin", "Chỉ tồn tại khi thời tiết có sấm sét", "Chỉ tồn tại trong bóng tối"], 0, "Từ trường của nam châm điện sinh ra do dòng điện nên chỉ tồn tại khi có dòng điện."),
        make_mc(3, "Nhận biết", "Muốn làm mất tác dụng từ của nam châm điện một cách tức thì, người ta thực hiện thao tác nào?", ["Ngắt công tắc điện để cắt đứt dòng điện", "Đảo chiều pin", "Tăng thêm số vòng dây", "Nhúng nam châm vào nước lạnh"], 0, "Ngắt dòng điện thì từ tính của nam châm điện mất ngay tức thì."),
        make_mc(4, "Nhận biết", "Vật liệu nào sau đây là lựa chọn thích hợp nhất để chế tạo lõi của nam châm điện?", ["Sắt non", "Đồng thau", "Nhựa cứng", "Gỗ ép"], 0, "Sắt non nhiễm từ rất mạnh và mất từ tính nhanh khi ngắt điện."),
        make_mc(5, "Nhận biết", "Thí nghiệm lịch sử năm 1820 của nhà bác học Oersted đã phát hiện ra mối liên hệ trực tiếp giữa:", ["Dòng điện và từ trường", "Nhiệt độ và ánh sáng", "Âm thanh và lực đẩy", "Trọng lực và áp suất"], 0, "Oersted phát hiện dòng điện trong dây dẫn làm quay kim nam châm (tác dụng từ)."),
        make_mc(6, "Nhận biết", "Một nam châm điện đang hút các đinh ghim ở đầu A. Nếu ta đảo cực của nguồn điện thì đầu A sẽ:", ["Đổi tên cực từ nhưng vẫn tiếp tục hút các đinh ghim", "Đẩy các đinh ghim ra xa", "Mất hoàn toàn lực hút", "Nóng chảy ngay lập tức"], 0, "Nam châm luôn hút sắt thép ở cả hai cực Bắc và Nam, đảo chiều dòng điện chỉ đảo tên cực từ."),
        make_mc(7, "Nhận biết", "Thiết bị nào sau đây KHÔNG sử dụng nam châm điện trong nguyên lý hoạt động?", ["La bàn bỏ túi truyền thống", "Rơ le điện từ", "Cần cẩu dọn phế liệu kim loại", "Chuông điện gia đình"], 0, "La bàn truyền thống dùng kim nam châm vĩnh cửu đặt trên trục quay tự do."),
        make_mc(8, "Thông hiểu", "Khi giữ nguyên cường độ dòng điện nhưng tăng số vòng dây quấn trên cùng một ống dây thì lực từ của nam châm điện sẽ:", ["Tăng lên", "Giảm đi", "Không đổi", "Biến mất"], 0, "Lực từ của nam châm điện tăng khi số vòng dây quấn tăng."),
        make_mc(9, "Thông hiểu", "Nếu quấn dây đồng trần (không có màng sơn men cách điện) sát khít quanh đinh sắt thì hiện tượng gì sẽ xảy ra?", ["Dòng điện bị ngắn mạch chạy tắt qua các vòng dây và đinh sắt, nam châm không hoạt động", "Nam châm hút mạnh gấp đôi", "Đinh sắt biến thành thanh nam châm vĩnh cửu", "Điện trở mạch tăng lên vô cùng lớn"], 0, "Dây trần làm các vòng dây chạm chập nhau, dòng điện không chạy xoắn ốc theo cuộn dây nên không sinh từ trường xoắn."),
        make_mc(10, "Thông hiểu", "Để điều khiển độ mạnh yếu của lực từ một nam châm điện trong phòng thí nghiệm, người ta thường mắc nối tiếp cuộn dây với:", ["Một biến trở", "Một chiếc ampe kế đo dòng", "Một nhiệt kế thủy ngân", "Một vôn kế"], 0, "Biến trở dùng để thay đổi điện trở mạch, từ đó thay đổi cường độ dòng điện qua nam châm điện."),
        make_mc(11, "Thông hiểu", "Tàu đệm từ (Maglev) có thể di chuyển với vận tốc cực lớn mà êm ái, không ma sát đường ray là nhờ ứng dụng:", ["Lực đẩy và lực nâng của hệ thống nam châm điện cực mạnh", "Động cơ phản lực gắn dưới gầm ray", "Đệm không khí nén áp suất cao", "Bánh xe thép lăn siêu trơn"], 0, "Tàu Maglev ứng dụng lực từ của nam châm điện để nâng toa tàu lơ lửng trên đường ray."),
        make_mc(12, "Thông hiểu", "Một học sinh chế tạo hai nam châm điện: Cuộn 1 có 50 vòng dây quấn trên bu-lông sắt non; Cuộn 2 có 50 vòng dây quấn trên đũa tre cùng kích thước. Cho cùng dòng điện 0,5 A chạy qua cả hai cuộn. Kết quả thu được là:", ["Cuộn 1 hút đinh ghim rất mạnh, cuộn 2 hầu như không hút được đinh ghim", "Cuộn 2 hút mạnh hơn cuộn 1", "Hai cuộn hút đinh ghim như nhau", "Cả hai cuộn đều không có từ tính"], 0, "Đũa tre không phải là vật liệu từ nên từ trường rất yếu, bu-lông sắt non tăng cường từ trường lên nhiều lần.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về sự khác biệt giữa lõi sắt non và lõi thép khi đặt trong cuộn dây có dòng điện:", [
            ("a", "Cả sắt non và thép đều bị nhiễm từ mạnh khi đặt trong từ trường của cuộn dây.", True),
            ("b", "Khi ngắt dòng điện, lõi sắt non mất hầu hết từ tính, còn thép giữ được từ tính lâu dài.", True),
            ("c", "Để chế tạo nam châm vĩnh cửu nhân tạo, người ta đặt thanh thép vào lòng ống dây có dòng điện.", True),
            ("d", "Dùng lõi thép làm cần cẩu bốc dỡ phế liệu sẽ giúp việc thả phế liệu diễn ra dễ dàng hơn lõi sắt non.", False)
        ], "Nếu dùng lõi thép thì khi ngắt điện thép vẫn giữ từ tính, sắt vụn dính chặt không chịu rơi xuống."),
        make_tf(2, "Thông hiểu", "Về khả năng điều khiển linh hoạt của nam châm điện so với nam châm vĩnh cửu:", [
            ("a", "Có thể đóng ngắt từ tính của nam châm điện nhanh chóng bằng công tắc.", True),
            ("b", "Có thể tăng giảm lực từ của nam châm điện bằng cách thay đổi cường độ dòng điện.", True),
            ("c", "Có thể đảo cực từ của nam châm điện bằng cách đảo cực của nguồn điện.", True),
            ("d", "Nam châm điện không thể hút được vật liệu coban hay niken.", False)
        ], "Nam châm điện hút được tất cả các vật liệu từ tính như sắt, thép, niken, coban."),
        make_tf(3, "Vận dụng", "Thực hành chế tạo nam châm điện bằng đinh sắt, dây đồng bọc men và pin tròn 1,5V:", [
            ("a", "Dây quấn càng sít nhau và quấn thành nhiều lớp thì từ trường tạo ra càng mạnh.", True),
            ("b", "Đoạn dây dẫn ở hai đầu cuộn dây dùng để nối vào pin phải được cạo sạch lớp men cách điện.", True),
            ("c", "Nếu lắp thêm một viên pin 1,5V nối tiếp thì lực hút của nam châm điện sẽ giảm sút.", False),
            ("d", "Sau khi ngắt pin, nam châm điện với đinh sắt non vẫn hút chặt thanh nhôm không rời.", False)
        ], "Thanh nhôm không có từ tính nên không bao giờ bị nam châm hút."),
        make_tf(4, "Vận dụng", "Ứng dụng công nghiệp và an toàn của nam châm điện:", [
            ("a", "Trong các nhà máy lọc đường hoặc xay xát ngũ cốc, nam châm điện được dùng để hút lọc các mẩu sắt vụn lẫn vào nguyên liệu.", True),
            ("b", "Trong thiết bị ghi âm từ tính hoặc đĩa cứng, đầu đọc/ghi sử dụng các nam châm điện siêu nhỏ.", True),
            ("c", "Cần cẩu nam châm điện có thể dùng để vận chuyển các khối vàng thỏi nguyên chất một cách dễ dàng.", False),
            ("d", "Khóa cửa từ điện tử tại các tòa nhà cao ốc sử dụng nam châm điện để giữ chốt cửa luôn khóa khi có điện.", True)
        ], "Vàng là kim loại không có từ tính nên nam châm không hút được vàng thỏi.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một nam châm điện có cuộn dây 80 vòng nối với pin 3 V hút được 18 chiếc đinh ghim nhỏ. Người ta quấn thêm 40 vòng dây nữa (tổng 120 vòng) và giữ nguyên nguồn điện, hỏi số đinh ghim hút được ước tính là bao nhiêu chiếc?", "27", "Tỉ lệ số vòng = 120 / 80 = 1,5 lần. Số đinh ghim hút được = 18 x 1,5 = 27 chiếc."),
        make_sa(2, "Thông hiểu", "Trong mạch điều khiển nam châm điện, ban đầu cường độ dòng điện là 0,3 A. Sau khi điều chỉnh biến trở thì dòng điện tăng lên thành 0,6 A. Hỏi cường độ dòng điện qua nam châm điện đã tăng thêm bao nhiêu ampe (A)?", "0,3", "Cường độ tăng thêm = 0,6 - 0,3 = 0,3 A."),
        make_sa(3, "Thông hiểu", "Một cần cẩu nam châm điện lần thứ nhất nâng được 450 kg sắt vụn, lần thứ hai nâng được 350 kg sắt vụn. Tổng khối lượng sắt vụn mà cần cẩu đã nâng qua hai lần là bao nhiêu kilôgam (kg)?", "800", "Tổng khối lượng = 450 + 350 = 800 kg."),
        make_sa(4, "Thông hiểu", "Một nhóm học sinh quấn 4 cuộn nam châm điện A, B, C, D có số vòng dây lần lượt là: Mẫu A (30 vòng), Mẫu B (60 vòng), Mẫu C (90 vòng), Mẫu D (120 vòng). Khi cùng cho dòng điện 0,5 A chạy qua, cuộn dây nào có lực từ mạnh nhất?", "D", "Số vòng dây càng nhiều thì lực từ càng mạnh, do đó mẫu D (120 vòng) có lực từ mạnh nhất."),
        make_sa(5, "Thông hiểu", "Một cuộn dây quấn nam châm điện có tổng chiều dài sợi dây đồng bọc men là 4 mét (m). Biết chu vi mỗi vòng quấn quanh lõi đinh sắt là 4 cm. Hỏi cuộn dây này có tổng cộng bao nhiêu vòng quấn?", "100", "Đổi 4 m = 400 cm. Số vòng quấn = 400 / 4 = 100 vòng."),
        make_sa(6, "Thông hiểu", "Khi đóng mạch điện, một nam châm điện công nghiệp hút giữ được 32 thỏi gang. Khi người vận hành ngắt điện hoàn toàn, biết lõi nam châm làm bằng sắt non khử từ tốt, hỏi có bao nhiêu thỏi gang còn bị dính lại trên bề mặt nam châm?", "0", "Lõi sắt non mất từ tính hoàn toàn khi ngắt điện nên toàn bộ 32 thỏi gang rơi xuống, còn dính lại 0 thỏi.")
    ],
    "part4": [
        make_vdc(1, "Một chuông điện tự ngắt sử dụng nguồn điện một chiều 6 V. Khi đóng mạch, cứ mỗi giây miếng sắt của búa gõ đóng mở mạch 20 chu kì, tạo ra 20 tiếng chuông gõ vào bát kim loại. Hỏi nếu học sinh nhấn giữ nút chuông trong đúng 15 giây thì chuông điện đã phát ra tổng cộng bao nhiêu tiếng gõ?", ["300 tiếng gõ", "150 tiếng gõ", "120 tiếng gõ", "200 tiếng gõ"], 0, "Tổng số tiếng gõ = 20 lần/giây x 15 giây = 300 tiếng gõ."),
        make_vdc(2, "Để khảo sát ảnh hưởng của số vòng dây đến lực hút của nam châm điện, một nhóm học sinh đo khối lượng sắt tối đa mà nam châm hút được: Với N1 = 50 vòng hút được 120 g; với N2 = 100 vòng hút được 240 g; với N3 = 150 vòng hút được 360 g. Hỏi nếu quấn tới N4 = 250 vòng dây với cùng cường độ dòng điện đó thì nam châm hút được khối lượng sắt xấp xỉ bao nhiêu gam?", ["600 g", "500 g", "480 g", "720 g"], 0, "Khối lượng hút tỉ lệ thuận với số vòng dây: m = 2,4 x N. Với N = 250 thì m = 2,4 x 250 = 600 g."),
        make_vdc(3, "Một rơ le nhiệt - từ bảo vệ quá tải cho hệ thống điện trong tòa nhà: Dòng điện định mức cho phép là 16 A. Khi xảy ra sự cố chập mạch, dòng điện vọt lên 48 A làm lực từ của nam châm điện tăng vọt, hút chốt ngắt mạch chỉ trong 0,02 giây. Cường độ dòng điện khi xảy ra sự cố đã tăng gấp bao nhiêu lần so với dòng điện định mức ban đầu?", ["3 lần", "2 lần", "4 lần", "6 lần"], 0, "Tỉ số dòng điện = 48 / 16 = 3 lần."),
        make_vdc(4, "Một đoàn tàu đệm từ Maglev có tổng khối lượng 240 tấn được nâng lơ lửng nhờ hệ thống gồm 120 khối nam châm điện siêu dẫn bố trí đều dọc thân tàu. Để nâng được đoàn tàu bay lên, trung bình mỗi khối nam châm điện phải tạo ra một lực từ nâng tối thiểu có độ lớn bao nhiêu niutơn (N), lấy g = 10 m/s2?", ["20 000 N", "10 000 N", "12 000 N", "24 000 N"], 0, "Trọng lượng toàn đoàn tàu P = 240 000 kg x 10 = 2 400 000 N. Mỗi khối nam châm chịu lực nâng = 2 400 000 / 120 = 20 000 N.")
    ]
}

# --- ĐỀ 3 ---
b20_exams["phys7_c6_b20_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 20: Chế tạo nam châm điện đơn giản - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c6", "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b20", "lessonName": "Bài 20: Chế tạo nam châm điện đơn giản",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Bộ phận trực tiếp sinh ra từ trường trong một nam châm điện là:", ["Cuộn dây dẫn khi có dòng điện chạy qua", "Lớp vỏ cách điện bên ngoài", "Công tắc bật mở", "Đế đỡ bằng gỗ"], 0, "Dòng điện chạy qua cuộn dây dẫn trực tiếp sinh ra từ trường."),
        make_mc(2, "Nhận biết", "Đặc tính nào sau đây là ưu điểm vượt trội của nam châm điện so với nam châm vĩnh cửu?", ["Có thể dễ dàng điều khiển độ mạnh yếu và bật tắt từ tính", "Không bao giờ bị nóng lên khi sử dụng", "Luôn giữ nguyên lực hút không đổi", "Không cần cung cấp năng lượng điện"], 0, "Nam châm điện điều khiển được từ trường thông qua việc điều chỉnh dòng điện."),
        make_mc(3, "Nhận biết", "Từ trường của ống dây có lõi sắt non tập trung mạnh nhất tại vị trí nào?", ["Ở hai đầu của lõi sắt non", "Ở chính giữa thân ống dây", "Ở nguồn điện", "Ở dây dẫn nối ngoài"], 0, "Các cực từ nằm ở hai đầu lõi sắt non là nơi từ trường tập trung dày đặc nhất."),
        make_mc(4, "Nhận biết", "Khi tăng đồng thời cả cường độ dòng điện chạy qua cuộn dây và số vòng dây quấn thì lực từ của nam châm điện sẽ:", ["Tăng lên rất mạnh", "Giảm đi rõ rệt", "Không thay đổi", "Biến mất hoàn toàn"], 0, "Cả hai yếu tố đều làm tăng lực từ nên khi tăng đồng thời lực từ tăng mạnh."),
        make_mc(5, "Nhận biết", "Tại sao người ta không dùng lõi bằng nhựa hoặc cao su trong nam châm điện?", ["Vì nhựa và cao su không có từ tính, không thể tăng cường từ trường của cuộn dây", "Vì nhựa quá nặng", "Vì nhựa dẫn điện quá tốt", "Vì nhựa quá đắt tiền"], 0, "Nhựa và cao su không nhiễm từ nên không khuếch đại được từ trường."),
        make_mc(6, "Nhận biết", "Dụng cụ dùng để thay đổi cường độ dòng điện qua cuộn dây nhằm tăng giảm lực hút nam châm điện trong thí nghiệm là:", ["Biến trở", "Thước cuộn", "Nhiệt kế", "Lực kế"], 0, "Biến trở có thể thay đổi điện trở, từ đó điều chỉnh cường độ dòng điện I."),
        make_mc(7, "Nhận biết", "Khi đóng khóa K của mạch điện chứa nam châm điện, kim nam châm nhỏ đặt thăng bằng ở gần đó sẽ:", ["Bị lệch góc quay khỏi vị trí cân bằng ban đầu", "Đứng yên không hề dịch chuyển", "Bốc cháy", "Rơi xuống đất"], 0, "Từ trường của nam châm điện tác dụng lực từ làm kim nam châm xoay lệch."),
        make_mc(8, "Thông hiểu", "Thiết bị hoạt động dựa trên nguyên tắc: nam châm điện hút miếng sắt kéo búa đập vào chuông, đồng thời ngắt mạch điện nhả miếng sắt về vị trí ban đầu là:", ["Chuông điện tự ngắt", "Bếp hồng ngoại", "Bình thủy điện", "Đồng hồ quả lắc cơ học"], 0, "Đó chính là nguyên lý tự ngắt liên tục của chuông điện."),
        make_mc(9, "Thông hiểu", "Nếu dùng lõi thép thay cho lõi sắt non thì sau khi ngắt dòng điện chạy qua ống dây, lõi thép sẽ:", ["Vẫn giữ được từ tính lâu dài và trở thành nam châm vĩnh cửu", "Mất hết từ tính ngay lập tức", "Chảy lỏng ra", "Bị vỡ thành nhiều mảnh"], 0, "Thép có tính khử từ chậm, giữ từ tính lâu dài tạo thành nam châm vĩnh cửu."),
        make_mc(10, "Thông hiểu", "Để đảo chiều các cực từ của nam châm điện, thao tác đúng nhất là:", ["Đổi chiều dòng điện bằng cách hoán đổi hai cực của nguồn điện nối vào cuộn dây", "Xoay ngược chiều đinh sắt trong cuộn dây", "Sơn màu ngược lại cho hai đầu đinh", "Tăng thêm số vòng dây"], 0, "Đảo chiều dòng điện làm đảo chiều các đường sức từ và cực từ."),
        make_mc(11, "Thông hiểu", "Người ta chế tạo nam châm điện dạng hình chữ U quấn hai cuộn dây nhằm mục đích gì?", ["Đưa cả hai cực Bắc và Nam về cùng một phía để tăng lực hút tiếp xúc lên vật bằng sắt", "Để tiết kiệm dây điện", "Để dễ cầm tay hơn", "Để giảm khối lượng nam châm"], 0, "Hai cực từ cùng nằm một phía cho phép cả hai cực cùng hút vật, tăng lực giữ gấp đôi."),
        make_mc(12, "Thông hiểu", "Đồ vật hoặc thiết bị nào sau đây KHÔNG sử dụng nguyên lý hoạt động của nam châm điện?", ["Chiếc bút bi bấm học sinh", "Máy chụp cộng hưởng từ MRI trong bệnh viện", "Loa phóng thanh điện động", "Rơ le bảo vệ máy biến áp"], 0, "Bút bi hoạt động hoàn toàn bằng cơ học lò xo, không dùng nam châm điện.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về quy trình các bước thực hành chế tạo nam châm điện đơn giản:", [
            ("a", "Chọn một chiếc đinh sắt hoặc bu-lông sắt dài khoảng 5 - 10 cm làm lõi.", True),
            ("b", "Quấn dây đồng tráng men cách điện đều đặn nhiều vòng xung quanh đinh sắt.", True),
            ("c", "Để nguyên lớp men sơn ở hai đầu dây khi cắm vào cực pin để dòng điện chạy êm hơn.", False),
            ("d", "Dùng các kẹp giấy kim loại để kiểm tra độ mạnh yếu của lực từ nam châm vừa tạo ra.", True)
        ], "Bắt buộc phải cạo sạch lớp men cách điện ở hai đầu dây thì dòng điện mới truyền qua được."),
        make_tf(2, "Thông hiểu", "Về các đặc tính từ trường của nam châm điện có lõi sắt non:", [
            ("a", "Từ trường xung quanh nam châm điện có dạng tương tự như từ trường của một thanh nam châm thẳng.", True),
            ("b", "Đầu cuộn dây mà các đường sức từ đi ra là cực Bắc, đầu đi vào là cực Nam.", True),
            ("c", "Khi dòng điện qua cuộn dây càng lớn thì từ trường sinh ra càng mạnh.", True),
            ("d", "Nếu ngắt dòng điện thì từ trường của nam châm điện vẫn tồn tại vĩnh viễn không bao giờ mất.", False)
        ], "Nam châm điện mất từ trường gần như hoàn toàn khi ngắt dòng điện."),
        make_tf(3, "Vận dụng", "Thí nghiệm khảo sát lực hút kẹp ghim của nam châm điện khi thay đổi nguồn điện:", [
            ("a", "Dùng 1 viên pin 1,5V hút được 6 kẹp ghim; dùng 2 viên pin 1,5V mắc nối tiếp hút được khoảng 12 kẹp ghim.", True),
            ("b", "Khi lắp 2 viên pin nối tiếp, hiệu điện thế tăng gấp đôi làm cường độ dòng điện tăng.", True),
            ("c", "Nếu lắp 2 viên pin ngược cực nhau (+ đấu với +) thì lực hút của nam châm sẽ tăng mạnh nhất.", False),
            ("d", "Đưa đầu nam châm điện lại gần mẩu dây đồng vụn thì nam châm không hút được mẩu đồng nào.", True)
        ], "Mắc ngược cực hai viên pin giống nhau thì triệt tiêu hiệu điện thế (U = 0V), nam châm không hoạt động."),
        make_tf(4, "Vận dụng", "Cơ chế bảo vệ của rơ-le điện từ và cầu dao tự động (Aptomat):", [
            ("a", "Trong mạng điện gia đình, Aptomat chứa một nam châm điện nhỏ nối tiếp trong mạch chính.", True),
            ("b", "Khi xảy ra hiện tượng đoản mạch ngắn mạch, dòng điện tăng đột biến làm nam châm điện hút mạnh lẫy bật ngắt công tắc.", True),
            ("c", "Sau khi sự cố được khắc phục, người dùng có thể gạt cần gạt đóng lại Aptomat để cấp điện trở lại.", True),
            ("d", "Aptomat chỉ ngắt được điện khi có ai đó dùng tay kéo cần gạt, nam châm điện không có tác dụng tự ngắt.", False)
        ], "Nam châm điện tự động hút lẫy ngắt mạch tức thì khi quá tải mà không cần thao tác thủ công.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Một học sinh quấn 100 vòng dây quanh một chiếc đinh sắt non, khi nối với pin 1,5V thì nam châm hút được 16 chiếc đinh ghim nhỏ. Nếu quấn tăng lên thành 150 vòng dây với cùng viên pin đó, hỏi nam châm điện này hút được ước tính bao nhiêu chiếc đinh ghim?", "24", "Tỉ lệ số vòng = 150 / 100 = 1,5 lần. Số đinh ghim hút được = 16 x 1,5 = 24 chiếc."),
        make_sa(2, "Thông hiểu", "Để tăng lực hút của nam châm điện trong thí nghiệm, người ta điều chỉnh biến trở làm dòng điện tăng từ 0,4 A lên 1,2 A. Hỏi cường độ dòng điện chạy qua cuộn dây đã tăng lên gấp bao nhiêu lần?", "3", "Số lần tăng = 1,2 / 0,4 = 3 lần."),
        make_sa(3, "Thông hiểu", "Một cần trục điện tại xưởng đúc thép có khả năng nâng một khối sắt nặng 1,8 tấn trong một lần hút. Khối lượng khối sắt này bằng bao nhiêu kilôgam (kg)?", "1800", "1,8 tấn = 1,8 x 1000 = 1800 kg."),
        make_sa(4, "Thông hiểu", "Một cuộn dây nam châm điện gồm có 240 vòng dây được quấn đều đặn thành 4 lớp chồng lên nhau quanh một lõi thép non. Hỏi mỗi lớp có bao nhiêu vòng dây?", "60", "Số vòng mỗi lớp = 240 / 4 = 60 vòng."),
        make_sa(5, "Thông hiểu", "Trong một bài thực hành: Khi cường độ dòng điện là 0,2 A thì nam châm hút được 6 kẹp ghim; khi dòng điện là 0,4 A thì hút được 12 kẹp ghim. Hỏi khi dòng điện là 0,6 A thì nam châm hút được bao nhiêu chiếc kẹp ghim (giả sử số kẹp hút tỉ lệ thuận với dòng điện)?", "18", "Dòng điện 0,6 A gấp 3 lần 0,2 A nên số kẹp ghim hút được = 6 x 3 = 18 kẹp."),
        make_sa(6, "Thông hiểu", "Một học sinh chuẩn bị các dụng cụ: (1) Đinh sắt non; (2) Dây đồng bọc men cách điện; (3) Nguồn pin 1,5V; (4) Khóa K; (5) Thước kẻ nhựa; (6) Hộp kẹp ghim bằng thép để thử từ tính. Hỏi có bao nhiêu dụng cụ thực sự cần thiết để chế tạo và kiểm tra hoạt động của nam châm điện?", "5", "Có 5 dụng cụ cần thiết là (1), (2), (3), (4), (6). Thước kẻ nhựa không cần thiết.")
    ],
    "part4": [
        make_vdc(1, "Một nam châm điện hình chữ U có hai cuộn dây giống nhau quấn trên hai nhánh. Mỗi nhánh quấn 80 vòng dây. Dòng điện chạy qua cả hai cuộn là 0,5 A. Để tăng gấp đôi lực hút của nam châm điện này lên thanh sắt bắc ngang hai cực mà vẫn giữ nguyên cường độ dòng điện 0,5 A, người ta cần quấn thêm vào mỗi nhánh bao nhiêu vòng dây nữa?", ["80 vòng", "40 vòng", "160 vòng", "120 vòng"], 0, "Lực từ tăng gấp đôi nên tổng số vòng mỗi nhánh phải tăng gấp đôi từ 80 thành 160 vòng, tức quấn thêm 80 vòng mỗi nhánh."),
        make_vdc(2, "Thiết kế hệ thống báo động chống trộm: Một nam châm điện dùng dòng điện thường trực 0,2 A để hút giữ một tấm kim loại mở tiếp điểm chuông. Khi kẻ trộm giẫm lên dây bẫy làm đứt mạch điện của nam châm, lò xo ngay lập tức kéo tấm kim loại đóng tiếp điểm mạch phụ làm chuông 12 V reo vang với cường độ âm thanh 95 dB. Bộ phận đóng vai trò cảm ứng ngắt tự động trong hệ thống này là:", ["Rơ le điện từ mở tiếp điểm thường đóng", "Biến trở xoay", "Cầu chì nhiệt", "Điện trở quang"], 0, "Đây là nguyên lý hoạt động của rơ-le điện từ với tiếp điểm thường đóng: mất điện cuộn hút thì tiếp điểm đóng lại."),
        make_vdc(3, "Một cuộn dây nam châm điện có điện trở R = 15 ôm (ohm). Khi nối cuộn dây vào nguồn điện không đổi có hiệu điện thế U1 = 6 V thì cường độ dòng điện qua mạch là I1 = 0,4 A và hút được 10 đinh thép. Muốn dòng điện tăng lên thành I2 = 0,8 A để hút được 20 đinh thép thì hiệu điện thế của nguồn điện phải điều chỉnh lên mức U2 bằng bao nhiêu?", ["12 V", "18 V", "24 V", "9 V"], 0, "Dòng điện tăng gấp đôi (0,8 / 0,4 = 2) thì hiệu điện thế cũng phải tăng gấp đôi: U2 = 6 x 2 = 12 V (vì I = U/R)."),
        make_vdc(4, "Trong thiết bị ghi dữ liệu ổ đĩa cứng máy tính (HDD), đầu ghi là một nam châm điện siêu nhỏ có chiều rộng khe từ chỉ 50 nanômét (nm). Đầu ghi tạo ra các vùng từ hóa cực nhỏ trên đĩa từ quay với tốc độ 7200 vòng/phút. Đổi kích thước 50 nanômét ra đơn vị mét (m):", ["5 x 10^-8 m", "5 x 10^-9 m", "5 x 10^-7 m", "5 x 10^-6 m"], 0, "1 nm = 10^-9 m. Do đó 50 nm = 50 x 10^-9 m = 5 x 10^-8 m.")
    ]
}
