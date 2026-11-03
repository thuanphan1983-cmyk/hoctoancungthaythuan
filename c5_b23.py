# -*- coding: utf-8 -*-
# c5_b23.py - Bài 23: Tác dụng của dòng điện (3 đề độc lập 100%)
import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {"id": qid, "level": level, "question": q_text, "options": options, "correct": correct_idx, "explanation": explanation}

def make_tf(qid, level, prompt, statements, explanation=""):
    return {"id": qid, "level": level, "question": prompt, "statements": [{"subId": s[0], "text": s[1], "correct": s[2]} for s in statements], "explanation": explanation}

def make_sa(qid, level, q_text, answer, explanation=""):
    return {"id": qid, "level": level, "question": q_text, "correctAnswer": str(answer).strip(), "explanation": explanation}

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {"id": qid, "level": "Vận dụng cao", "question": q_text, "options": options, "correct": correct_idx, "explanation": explanation}

def get_b23_exams():
    exams = {}
    ch_id = "phys8_c5"
    ch_title = "Chương V: Điện"
    l_id = "phys8_c5_b23"
    l_name = "Bài 23: Tác dụng của dòng điện"

    def meta(t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # ĐỀ 1: Tác dụng nhiệt và Tác dụng phát sáng
    exams[f"{l_id}_test1"] = meta(1,
        [
            make_mc(1, "Nhận biết", "Tác dụng nhiệt của dòng điện là hiện tượng dòng điện chạy qua vật dẫn làm cho vật dẫn:", ["Nóng lên", "Nhiễm điện", "Phát ra âm thanh", "Chuyển động"], 0, "Dòng điện làm vật dẫn nóng lên."),
            make_mc(2, "Nhận biết", "Thiết bị nào sau đây hoạt động chủ yếu dựa vào tác dụng nhiệt có ích của dòng điện?", ["Bàn là điện", "Quạt máy", "Máy bơm nước", "Chuông điện"], 0, "Bàn là chuyển điện năng thành nhiệt năng."),
            make_mc(3, "Nhận biết", "Dây tóc bóng đèn sợi đốt phát sáng được là nhờ hiện tượng nào?", ["Dây tóc bị dòng điện nung nóng đến nhiệt độ rất cao (nóng sáng)", "Hiện tượng phóng điện trong chất khí", "Phản ứng hóa học phát quang", "Từ trường kích thích"], 0, "Nóng sáng ở nhiệt độ cao."),
            make_mc(4, "Nhận biết", "Vật liệu thường được dùng làm dây tóc bóng đèn sợi đốt là:", ["Vonfram", "Đồng", "Nhôm", "Chì"], 0, "Vonfram có nhiệt độ nóng chảy rất cao."),
            make_mc(5, "Nhận biết", "Đèn điốt phát quang (đèn LED) phát ra ánh sáng dựa vào cơ chế nào?", ["Chất bán dẫn phát sáng trực tiếp khi có dòng điện thích hợp chạy qua", "Dây tóc nóng đỏ", "Khí neon bốc cháy", "Dung dịch điện phân"], 0, "Phát quang bán dẫn trực tiếp."),
            make_mc(6, "Nhận biết", "Bóng đèn của bút thử điện phát sáng khi có dòng điện chạy qua chất nào bên trong bóng?", ["Khí neon ở áp suất thấp", "Dây tóc vonfram", "Dung dịch muối", "Thanh than chì"], 0, "Chất khí neon phát sáng do phóng điện."),
            make_mc(7, "Thông hiểu", "Ưu điểm nổi bật nhất của đèn LED so với bóng đèn sợi đốt khi thắp sáng là:", ["Tiêu thụ ít điện năng hơn và tỏa rất ít nhiệt", "Có giá thành đắt hơn nhiều", "Cần hiệu điện thế rất cao 1000 V", "Dễ vỡ hơn"], 0, "Hiệu suất phát sáng cao, tiết kiệm điện, ít tỏa nhiệt."),
            make_mc(8, "Thông hiểu", "Trong các thiết bị sau, thiết bị nào tác dụng nhiệt là tác dụng KHÔNG mong muốn (hao phí)?", ["Quạt điện đang quay", "Nồi cơm điện", "Ấm đun nước siêu tốc", "Máy sưởi dầu"], 0, "Quạt điện chỉ cần cơ năng quay, nhiệt tỏa ra là hao phí."),
            make_mc(9, "Thông hiểu", "Dây mai so trong bếp điện thường được làm bằng hợp kim niken - crom vì hợp kim này có đặc tính:", ["Điện trở suất lớn và chịu được nhiệt độ cao mà không bị oxi hóa đứt", "Nhiệt độ nóng chảy rất thấp", "Dẫn điện tốt như đồng", "Dễ uốn và tan trong nước"], 0, "Chịu nhiệt tốt và có điện trở suất cao."),
            make_mc(10, "Thông hiểu", "Nguyên tắc hoạt động ngắt điện của cầu chì khi xảy ra quá tải dựa trên:", ["Tác dụng nhiệt làm dây chì nóng chảy và đứt mạch", "Tác dụng từ hút đứt dây", "Tác dụng hóa học ăn mòn", "Tác dụng quang làm cháy"], 0, "Nhiệt độ dòng quá tải làm chì chảy đứt mạch."),
            make_mc(11, "Thông hiểu", "Đèn LED chỉ phát sáng khi được mắc vào mạch điện theo cách nào?", ["Cực dương của đèn nối với cực dương nguồn, cực âm nối cực âm", "Mắc ngược cực dương đèn vào cực âm nguồn", "Mắc vào nguồn xoay chiều không phân cực", "Chỉ cần chạm 1 đầu vào dây điện"], 0, "Đèn LED chỉ cho dòng điện đi qua theo một chiều thuận."),
            make_mc(12, "Thông hiểu", "Trường hợp nào sau đây KHÔNG xuất hiện tác dụng nhiệt của dòng điện?", ["Không có trường hợp nào, dòng điện qua vật dẫn có điện trở luôn sinh nhiệt", "Khi dòng điện rất nhỏ", "Khi bật đèn LED", "Khi sạc điện thoại"], 0, "Mọi dòng điện chạy qua vật dẫn có điện trở đều tỏa nhiệt.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về tác dụng nhiệt của dòng điện trong sinh hoạt gia đình đề 1:", [
                ("a", "Ấm đun siêu tốc, bàn là, bình nóng lạnh là các thiết bị khai thác tác dụng nhiệt có ích.", True),
                ("b", "Nhiệt lượng tỏa ra trên dây dẫn truyền tải điện năng từ nhà máy về nhà là nhiệt lượng có ích.", False),
                ("c", "Dây tóc bóng đèn sợi đốt có thể đạt nhiệt độ trên 2000°C khi phát sáng bình thường.", True),
                ("d", "Dây dẫn bằng đồng nguyên chất khi có dòng điện chạy qua hoàn toàn không tỏa nhiệt ra môi trường.", False)
            ], "Dây dẫn luôn có điện trở nên luôn tỏa nhiệt hao phí."),
            make_tf(2, "Thông hiểu", "Về tác dụng phát sáng và hiệu suất các loại bóng đèn chiếu sáng đề 1:", [
                ("a", "Bóng đèn sợi đốt biến đổi phần lớn điện năng tiêu thụ thành nhiệt năng làm nóng môi trường.", True),
                ("b", "Đèn huỳnh quang phát sáng nhờ lớp bột huỳnh quang tráng bên trong thành ống thủy tinh.", True),
                ("c", "Đèn LED chỉ phát sáng khi cực âm của đèn được nối trực tiếp với cực dương của nguồn điện.", False),
                ("d", "Sử dụng đèn LED thay thế đèn sợi đốt giúp tiết kiệm đáng kể chi phí tiền điện chiếu sáng.", True)
            ], "Đèn LED mắc cực thuận: dương vào dương, âm vào âm."),
            make_tf(3, "Thông hiểu", "Về cấu tạo và ứng dụng của bút thử điện học đường đề 1:", [
                ("a", "Bút thử điện chứa bóng đèn khí neon mắc nối tiếp với một điện trở bảo vệ có giá trị rất lớn.", True),
                ("b", "Khi thử dây pha (dây lửa), có dòng điện an toàn chạy qua bút và cơ thể người xuống đất.", True),
                ("c", "Người dùng không cần chạm tay vào chốt kim loại ở chuôi bút thì bóng đèn bút vẫn sáng bình thường.", False),
                ("d", "Bóng đèn bút thử điện phát sáng do dây tóc bên trong nóng đỏ lên đến nhiệt độ cao.", False)
            ], "Cần chạm chuôi bút tạo mạch kín xuống đất; bóng sáng do phóng điện khí neon."),
            make_tf(4, "Thông hiểu", "Về nguyên tắc an toàn nhiệt khi sử dụng thiết bị điện công suất lớn đề 1:", [
                ("a", "Không cắm chung nhiều thiết bị tỏa nhiệt lớn (bàn là, bếp lẩu) vào cùng một ổ cắm nối dài.", True),
                ("b", "Dây dẫn cấp nguồn cho bình nóng lạnh cần chọn loại có tiết diện lớn để giảm bớt nhiệt tỏa trên dây.", True),
                ("c", "Bao bọc kín đệm vải xung quanh ấm điện đang đun để giữ nhiệt cho nước nhanh sôi hơn.", False),
                ("d", "Khi dây dẫn điện bị nóng ran và có mùi khét cách điện thì phải lập tức ngắt cầu dao tổng.", True)
            ], "Che bọc vải lên ấm điện dễ gây hỏa hoạn cháy nổ.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một bàn là điện hoạt động ở hiệu điện thế 220 V với dòng điện 4,5 A. Tính công suất tỏa nhiệt của bàn là (W).", "990", "P = U * I = 220 * 4,5 = 990 W."),
            make_sa(2, "Thông hiểu", "Một ấm siêu tốc 1500 W đun nước trong 4 phút (240 giây). Điện năng tiêu thụ biến thành nhiệt là bao nhiêu Jun (J)?", "360000", "A = P * t = 1500 * 240 = 360 000 J."),
            make_sa(3, "Thông hiểu", "Một bóng đèn sợi đốt 220 V - 60 W chỉ biến đổi 5% điện năng thành quang năng. Công suất tỏa nhiệt hao phí của đèn là bao nhiêu Oát (W)?", "57", "P_nhiet = 60 * 95% = 57 W."),
            make_sa(4, "Thông hiểu", "Một đèn LED 12 W có độ sáng tương đương bóng đèn sợi đốt 60 W. Công suất điện tiết kiệm được khi dùng đèn LED là bao nhiêu Oát (W)?", "48", "P_tietkiem = 60 - 12 = 48 W."),
            make_sa(5, "Vận dụng", "Một điện trở sưởi R = 44 Ω mắc vào hiệu điện thế 220 V. Cường độ dòng điện qua điện trở là bao nhiêu Ampe (A)?", "5", "I = U / R = 220 / 44 = 5 A."),
            make_sa(6, "Vận dụng", "Bút thử điện có điện trở R = 1,1 MΩ (1 100 000 Ω). Khi thử mạng điện 220 V, dòng điện an toàn qua người là bao nhiêu miliampe (mA)?", "0.2", "I = 220 / 1100000 = 0,0002 A = 0,2 mA.")
        ],
        [
            make_vdc(1, "Một ấm đun nước điện công suất 1000 W đun sôi 1,5 lít nước từ 20°C đến 100°C. Biết c = 4200 J/(kg.K) và hiệu suất ấm là 84%. Thời gian đun sôi nước là:", [
                "10 phút", "12,5 phút", "8 phút", "15 phút"
            ], 0, "Q = 1,5 * 4200 * 80 = 504 000 J. A = 504000 / 0,84 = 600 000 J. t = 600000 / 1000 = 600 s = 10 phút."),
            make_vdc(2, "Một đoạn dây niken dài 10 m tiết diện 0,1 mm2 có điện trở suất ρ = 4,0 . 10^-7 Ω.m. Mắc dây này vào nguồn 20 V thì công suất tỏa nhiệt của dây là:", [
                "10 W", "20 W", "40 W", "5 W"
            ], 0, "R = 4e-7 * 10 / (0,1e-6) = 40 Ω. P = U^2 / R = 400 / 40 = 10 W."),
            make_vdc(3, "Một bóng đèn sợi đốt 220 V - 100 W và một đèn LED 220 V - 15 W cùng phát ra độ sáng như nhau. Nếu dùng thắp sáng 6 giờ mỗi ngày trong 30 ngày với giá điện 2000 đ/kWh, số tiền điện tiết kiệm được khi dùng đèn LED là:", [
                "30 600 đồng", "15 300 đồng", "61 200 đồng", "45 000 đồng"
            ], 0, "ΔP = 85 W. ΔA = 0,085 * 6 * 30 = 15,3 kWh. Tiền = 15,3 * 2000 = 30 600 đồng."),
            make_vdc(4, "Một nồi cơm điện 220 V - 660 W hoạt động bình thường liên tục trong 35 phút. Lượng nhiệt mà mâm nhiệt nồi cơm tỏa ra xấp xỉ bằng:", [
                "1,386 MJ", "0,66 MJ", "2,31 MJ", "3,5 MJ"
            ], 0, "Q = 660 * (35 * 60) = 1 386 000 J = 1,386 MJ.")
        ]
    )

    # ĐỀ 2: Tác dụng từ và Nam châm điện
    exams[f"{l_id}_test2"] = meta(2,
        [
            make_mc(1, "Nhận biết", "Tác dụng từ của dòng điện được phát hiện thông qua hiện tượng dòng điện làm quay:", ["Kim nam châm đặt gần dây dẫn", "Lá nhôm mỏng", "Thanh thủy tinh cọ xát", "Mảnh giấy vụn"], 0, "Dòng điện làm quay kim nam châm."),
            make_mc(2, "Nhận biết", "Cấu tạo cơ bản của một nam châm điện đơn giản gồm:", ["Một cuộn dây dẫn quấn quanh một lõi sắt non", "Một thanh nam châm vĩnh cửu", "Hai thanh đồng song song", "Một thanh nhôm bọc cao su"], 0, "Cuộn dây có lõi sắt non."),
            make_mc(3, "Nhận biết", "Vật liệu thích hợp nhất để làm lõi của nam châm điện là:", ["Sắt non", "Thép tôi cứng", "Đồng nguyên chất", "Bạc nguyên chất"], 0, "Sắt non tăng từ trường mạnh và mất từ tính ngay khi ngắt điện."),
            make_mc(4, "Nhận biết", "Thiết bị nào sau đây hoạt động dựa trên tác dụng từ của dòng điện?", ["Chuông điện", "Nồi cơm điện", "Bút thử điện", "Bình thủy điện"], 0, "Chuông điện dùng nam châm điện hút lá thép."),
            make_mc(5, "Nhận biết", "Khi ngắt dòng điện chạy qua cuộn dây của nam châm điện thì từ tính của lõi sắt non sẽ:", ["Mất đi gần như hoàn toàn ngay lập tức", "Vẫn giữ nguyên vĩnh viễn", "Đổi chiều cực từ", "Tăng lên gấp đôi"], 0, "Lõi sắt non mất từ tính khi ngắt dòng điện."),
            make_mc(6, "Nhận biết", "Để đảo chiều các cực từ (Bắc - Nam) của một nam châm điện, ta cần làm gì?", ["Đổi chiều dòng điện chạy qua cuộn dây", "Tăng cường độ dòng điện", "Rút lõi sắt ra ngoài", "Tăng số vòng dây"], 0, "Đổi chiều dòng điện làm đảo cực từ."),
            make_mc(7, "Thông hiểu", "Để tăng lực hút của nam châm điện đối với các vật bằng sắt, ta có thể áp dụng biện pháp nào?", ["Tăng số vòng dây và tăng cường độ dòng điện qua cuộn dây", "Giảm cường độ dòng điện", "Thay lõi sắt non bằng thanh gỗ", "Bỏ bớt vòng dây"], 0, "Tăng số vòng dây và tăng dòng điện làm tăng từ tính."),
            make_mc(8, "Thông hiểu", "Vì sao người ta không dùng thép tôi cứng để làm lõi nam châm điện dùng trong cần cẩu phế liệu?", ["Thép giữ từ tính lâu sau khi ngắt điện làm sắt vụn không nhả ra được", "Thép không dẫn từ", "Thép quá mềm dễ gãy", "Thép đắt hơn vàng"], 0, "Thép biến thành nam châm vĩnh cửu không thả sắt ra được."),
            make_mc(9, "Thông hiểu", "Bộ phận nào trong động cơ điện mini tạo ra từ trường để làm quay rôto?", ["Cuộn dây nam châm điện hoặc nam châm vĩnh cửu", "Cánh quạt gió", "Vỏ nhựa bảo vệ", "Trục quay cơ học"], 0, "Nam châm tạo từ trường làm quay rôto."),
            make_mc(10, "Thông hiểu", "Trong rơle điện từ dùng đóng ngắt tự động, nam châm điện có nhiệm vụ:", ["Hút thanh tiếp điểm bằng sắt để đóng hoặc ngắt mạch điện thứ hai", "Phát sáng báo hiệu", "Nung nóng tiếp điểm", "Tạo ra điện áp cao"], 0, "Lực từ hút tiếp điểm điều khiển mạch."),
            make_mc(11, "Thông hiểu", "Một kim nam châm tự do chỉ hướng Bắc - Nam. Khi đặt gần dây dẫn có dòng điện một chiều, kim nam châm bị lệch đi một góc vì:", ["Dòng điện tạo ra từ trường xung quanh dây tác dụng lực từ lên kim", "Dòng điện hút kim vì tĩnh điện", "Dòng điện làm nóng không khí đẩy kim", "Gió thổi từ dây"], 0, "Dòng điện sinh từ trường tác dụng lực từ lên kim."),
            make_mc(12, "Thông hiểu", "Khi tăng khoảng cách từ nam châm điện đến đinh sắt, lực từ tác dụng lên đinh sắt sẽ:", ["Giảm đi nhanh chóng", "Tăng lên", "Không đổi", "Bằng vô cùng"], 0, "Từ trường giảm nhanh khi ra xa nam châm.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về từ tính và đặc điểm của nam châm điện thí nghiệm đề 2:", [
                ("a", "Nam châm điện chỉ có từ tính khi có dòng điện chạy qua cuộn dây.", True),
                ("b", "Từ tính của nam châm điện có thể điều chỉnh mạnh hay yếu một cách linh hoạt.", True),
                ("c", "Nếu rút lõi sắt non ra khỏi cuộn dây thì lực từ của cuộn dây sẽ tăng lên gấp nhiều lần.", False),
                ("d", "Các cực từ của nam châm điện phụ thuộc vào chiều của dòng điện chạy trong cuộn dây.", True)
            ], "Rút lõi sắt làm giảm từ tính."),
            make_tf(2, "Thông hiểu", "Về hoạt động của chiếc chuông điện báo động gia đình đề 2:", [
                ("a", "Khi nhấn nút chuông, mạch điện kín và nam châm điện hút miếng sắt gắn đầu búa.", True),
                ("b", "Đầu búa đập vào chuông làm chuông phát ra âm thanh báo hiệu.", True),
                ("c", "Khi miếng sắt bị hút, tiếp điểm hở làm ngắt mạch điện của nam châm điện.", True),
                ("d", "Chuông điện reo liên tục nhờ dòng điện được giữ kín cố định không bao giờ bị ngắt quãng.", False)
            ], "Chuông reo nhờ cơ chế tự ngắt mạch đóng ngắt liên tục."),
            make_tf(3, "Thông hiểu", "Về ứng dụng của cần cẩu điện dọn phế liệu sắt thép đề 2:", [
                ("a", "Cần cẩu điện sử dụng nam châm điện có kích thước và công suất cực lớn.", True),
                ("b", "Để thả các khối sắt phế liệu xuống thùng xe tải, người vận hành chỉ cần ngắt dòng điện qua nam châm.", True),
                ("c", "Cần cẩu nam châm điện có thể dùng để hút phân loại các tấm kim loại bằng đồng và nhôm.", False),
                ("d", "Nam châm điện nâng được tải trọng sắt lớn hơn khi tăng cường độ dòng điện cấp cho cuộn dây.", True)
            ], "Đồng và nhôm không bị nam châm hút."),
            make_tf(4, "Thông hiểu", "Về rơle điện từ trong các hệ thống điều khiển tự động đề 2:", [
                ("a", "Rơle điện từ dùng dòng điện nhỏ ở mạch điều khiển để đóng ngắt mạch điện công suất lớn an toàn.", True),
                ("b", "Khi cuộn dây của rơle có điện, lực từ hút thanh tiếp điểm đóng mạch tải.", True),
                ("c", "Rơle điện từ hoạt động dựa hoàn toàn vào tác dụng hóa học của chất điện phân.", False),
                ("d", "Sử dụng rơle giúp bảo vệ người vận hành không phải tiếp xúc trực tiếp với lưới điện cao áp.", True)
            ], "Rơle hoạt động theo tác dụng từ.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một nam châm điện cuộn dây 200 vòng hút được 15 chiếc đinh sắt. Khi quấn thêm 100 vòng dây cùng loại với dòng điện không đổi, nam châm hút được 22 chiếc đinh. Số đinh hút thêm được là bao nhiêu chiếc?", "7", "22 - 15 = 7 chiếc."),
            make_sa(2, "Thông hiểu", "Một cuộn dây nam châm điện có điện trở R = 8 Ω nối với nguồn 12 V. Cường độ dòng điện qua cuộn dây là bao nhiêu Ampe (A)?", "1.5", "I = U / R = 12 / 8 = 1,5 A."),
            make_sa(3, "Thông hiểu", "Một cần cẩu điện có khả năng tạo lực từ nâng 15 000 N. Khối lượng sắt tối đa mà cần cẩu nâng được là bao nhiêu kilôgam (kg)? (Lấy g = 10 m/s2).", "1500", "m = F / g = 15000 / 10 = 1500 kg."),
            make_sa(4, "Thông hiểu", "Một rơle điện từ cần dòng điện tối thiểu 0,2 A để đóng tiếp điểm. Nếu cuộn dây có điện trở 60 Ω thì hiệu điện thế kích hoạt tối thiểu là bao nhiêu Vôn (V)?", "12", "U = I * R = 0,2 * 60 = 12 V."),
            make_sa(5, "Vận dụng", "Khi dòng điện qua nam châm điện là 1 A thì lực từ là 4 N. Biết lực từ tỉ lệ thuận với bình phương cường độ dòng điện (F ~ I^2). Khi dòng điện tăng lên 2 A thì lực từ là bao nhiêu Niutơn (N)?", "16", "F' = 4 * (2/1)^2 = 16 N."),
            make_sa(6, "Vận dụng", "Một chuông điện gõ chuông 12 lần trong 1 giây. Trong 5 giây bấm chuông liên tục, búa đã gõ vào chuông tổng cộng bao nhiêu lần?", "60", "Số lần = 12 * 5 = 60 lần.")
        ],
        [
            make_vdc(1, "Một nam châm điện dùng trong công nghiệp có cuộn dây gồm 1000 vòng dây đồng có điện trở suất ρ = 1,7 . 10^-8 Ω.m, chiều dài trung bình mỗi vòng dây là 20 cm, tiết diện dây là 0,34 mm2. Mắc nam châm vào nguồn U = 24 V. Cường độ dòng điện chạy qua cuộn dây nam châm điện là:", [
                "2,4 A", "1,2 A", "4,8 A", "0,6 A"
            ], 0, "L = 1000 * 0,2 = 200 m. R = 1,7e-8 * 200 / (0,34e-6) = 10 Ω. I = 24 / 10 = 2,4 A."),
            make_vdc(2, "Một cần cẩu nam châm điện nâng một khối thép nặng 2,5 tấn (2500 kg) lên cao 4 m trong thời gian 10 giây. Lấy g = 10 m/s2. Công suất cơ học tối thiểu của hệ thống nâng là:", [
                "10 kW", "2,5 kW", "25 kW", "100 kW"
            ], 0, "A = m*g*h = 2500 * 10 * 4 = 100 000 J. P = A / t = 100 000 / 10 = 10 000 W = 10 kW."),
            make_vdc(3, "Để điều khiển một máy bơm nước 220 V - 2,2 kW từ xa an toàn, người ta dùng một rơle điện từ cuộn hút 12 V - 0,1 A. Tỉ số giữa công suất máy bơm và công suất tiêu thụ của mạch điều khiển rơle là:", [
                "Khoảng 1833 lần", "100 lần", "500 lần", "2200 lần"
            ], 0, "P_relay = 12 * 0,1 = 1,2 W. P_bom = 2200 W. Tỉ số = 2200 / 1,2 ≈ 1833 lần."),
            make_vdc(4, "Một nam châm điện được cấp bởi nguồn điện 12 V qua một biến trở con chạy. Khi biến trở có giá trị R1 = 14 Ω (cuộn dây có điện trở r = 2 Ω), dòng điện trong mạch là I1 = 0,75 A. Khi dịch con chạy để biến trở có giá trị R2 = 6 Ω thì dòng điện I2 và tỉ số lực từ (F2/F1) xấp xỉ bằng:", [
                "I2 = 1,5 A; F2/F1 = 4", "I2 = 2,0 A; F2/F1 = 2", "I2 = 1,0 A; F2/F1 = 1,5", "I2 = 0,5 A; F2/F1 = 0,25"
            ], 0, "I2 = 12 / (6 + 2) = 1,5 A. I2/I1 = 2 => F2/F1 = 2^2 = 4.")
        ]
    )

    # ĐỀ 3: Tác dụng hóa học và Tác dụng sinh lí
    exams[f"{l_id}_test3"] = meta(3,
        [
            make_mc(1, "Nhận biết", "Tác dụng hóa học của dòng điện được thể hiện rõ nét nhất qua hiện tượng nào sau đây?", ["Hiện tượng điện phân dung dịch muối kim loại", "Dây tóc bóng đèn phát sáng", "Nam châm điện hút đinh sắt", "Bàn là nóng lên"], 0, "Điện phân dung dịch là tác dụng hóa học."),
            make_mc(2, "Nhận biết", "Trong thí nghiệm điện phân dung dịch copper sulfate (CuSO4) với hai điện cực than, sau một thời gian ở cực âm bám vào một lớp kim loại màu đỏ là:", ["Đồng (Cu)", "Sắt (Fe)", "Nhôm (Al)", "Kẽm (Zn)"], 0, "Đồng bám vào cực âm."),
            make_mc(3, "Nhận biết", "Trong kĩ thuật mạ điện kim loại (mạ bạc, mạ vàng), vật cần mạ phải được gắn vào cực nào của nguồn điện một chiều?", ["Cực âm (catot)", "Cực dương (anot)", "Gắn vào cực nào cũng được", "Không gắn vào nguồn điện"], 0, "Vật cần mạ gắn vào cực âm."),
            make_mc(4, "Nhận biết", "Tác dụng sinh lí của dòng điện là hiện tượng dòng điện chạy qua cơ thể sinh vật làm cho:", ["Cơ bắp bị co giật, tim và hệ hô hấp bị tác động mạnh", "Cơ thể phát ra ánh sáng huỳnh quang", "Cơ thể bị nhiễm từ hút sắt", "Cơ thể phân giải thành kim loại"], 0, "Dòng điện gây co cơ, tác động thần kinh tim mạch."),
            make_mc(5, "Nhận biết", "Ứng dụng nào sau đây trong y học khai thác tác dụng sinh lí có ích của dòng điện?", ["Máy sốc tim hồi sức bệnh nhân ngừng tim", "Máy chụp X-quang", "Kính hiển vi quang học", "Nhiệt kế thủy ngân"], 0, "Máy sốc tim dùng xung điện kích tim."),
            make_mc(6, "Nhận biết", "Dung dịch nào sau đây KHÔNG dẫn điện và không xảy ra hiện tượng điện phân khi có dòng điện?", ["Nước cất tinh khiết", "Dung dịch muối ăn NaCl", "Dung dịch axit sulfuric H2SO4", "Dung dịch copper sulfate CuSO4"], 0, "Nước cất tinh khiết là chất cách điện."),
            make_mc(7, "Thông hiểu", "Tại sao trong công nghệ mạ điện, người ta bắt buộc phải sử dụng nguồn điện một chiều (DC) mà không dùng xoay chiều (AC)?", ["Để các ion kim loại luôn chuyển dời cố định về cực âm bám vào vật mạ", "Vì dòng xoay chiều không sinh nhiệt", "Vì nguồn một chiều rẻ hơn", "Vì pin nhẹ hơn máy biến áp"], 0, "Dòng 1 chiều giúp ion kim loại di chuyển 1 hướng về cực âm."),
            make_mc(8, "Thông hiểu", "Tác dụng sinh lí của dòng điện có thể gây nguy hiểm chết người khi dòng điện xoay chiều có cường độ khoảng bao nhiêu chạy qua cơ thể?", ["Từ 10 mA đến 25 mA trở lên", "Dưới 0,001 mA", "Chỉ khi trên 1000 A", "Bất kì dòng điện nào"], 0, "Khoảng 10-25 mA đã làm co cơ lồng ngực gây ngạt thở."),
            make_mc(9, "Thông hiểu", "Mục đích chính của việc mạ một lớp niken hoặc crom lên bề mặt các chi tiết kim loại bằng sắt là:", ["Chống rỉ sét, ăn mòn hóa học và làm đẹp bề mặt sản phẩm", "Làm cho vật nặng hơn", "Làm tăng độ dẻo", "Để hút nam châm mạnh hơn"], 0, "Chống ăn mòn và tăng tính thẩm mỹ."),
            make_mc(10, "Thông hiểu", "Phương pháp châm cứu điện (điện châm) trong y học cổ truyền hoạt động dựa trên tác dụng gì của dòng điện?", ["Tác dụng sinh lí kích thích các huyệt đạo thần kinh", "Tác dụng nhiệt đốt cháy huyệt", "Tác dụng mạ kim loại vào da", "Tác dụng từ hút máu"], 0, "Kích thích huyệt đạo qua tác dụng sinh lí an toàn."),
            make_mc(11, "Thông hiểu", "Khi một người bị điện giật dính chặt vào dây điện, hành động cứu nạn ĐẦU TIÊN đúng quy tắc là:", ["Nhanh chóng ngắt ngay cầu dao điện hoặc dùng cây gậy gỗ khô gạt dây điện ra", "Dùng tay không kéo nạn nhân ra ngay", "Dội nước vào người nạn nhân", "Hô hấp nhân tạo ngay khi nạn nhân còn dính điện"], 0, "Ngắt điện hoặc dùng vật cách điện khô."),
            make_mc(12, "Thông hiểu", "Khối lượng kim loại bám vào điện cực âm trong bình mạ điện tỉ lệ thuận với yếu tố nào?", ["Cường độ dòng điện và thời gian dòng điện chạy qua bình", "Thể tích của bình đựng", "Màu sắc của dung dịch", "Khoảng cách từ bình đến nguồn điện"], 0, "Khối lượng m tỉ lệ thuận với điện lượng q = I.t.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về quá trình điện phân và công nghệ mạ điện kim loại đề 3:", [
                ("a", "Dung dịch muối hoặc axit có khả năng dẫn điện nhờ sự dịch chuyển có hướng của các ion tự do.", True),
                ("b", "Trong bình mạ đồng, cực dương thường được làm bằng một thanh đồng nguyên chất để hòa tan bổ sung ion.", True),
                ("c", "Vật cần mạ kim loại có thể được nối vào bất kì cực nào của nguồn điện một chiều mà vẫn bám đều.", False),
                ("d", "Khối lượng lớp kim loại mạ bám trên bề mặt tăng lên khi ta kéo dài thời gian mạ điện.", True)
            ], "Vật cần mạ bắt buộc phải nối cực âm."),
            make_tf(2, "Thông hiểu", "Về các tác động sinh lí của dòng điện lên cơ thể sống đề 3:", [
                ("a", "Dòng điện chạy qua cơ thể làm các cơ bắp co giật mạnh không thể tự duỗi ra được.", True),
                ("b", "Dòng điện cường độ lớn chạy qua lồng ngực có thể làm tê liệt cơ hô hấp và gây ngừng tim đột ngột.", True),
                ("c", "Dòng điện chỉ gây nguy hiểm khi có hiệu điện thế trên 10 000 V, dưới mức đó hoàn toàn an toàn.", False),
                ("d", "Dòng điện nhỏ có kiểm soát được dùng trong y tế để phục hồi chức năng cơ bắp bị teo liệt.", True)
            ], "Dòng điện ở hiệu điện thế sinh hoạt 220V rất nguy hiểm có thể gây chết người."),
            make_tf(3, "Thông hiểu", "Về các biện pháp cứu chữa ban đầu khi gặp tai nạn điện giật đề 3:", [
                ("a", "Phải tách ngay nạn nhân ra khỏi nguồn điện trước khi tiến hành các bước hô hấp nhân tạo.", True),
                ("b", "Nếu không ngắt được cầu dao, người cứu có thể đi ủng cao su hoặc đứng trên ván gỗ khô để kéo nạn nhân.", True),
                ("c", "Có thể dùng xẻng sắt ướt để gạt dây điện dính trên người nạn nhân trong lúc vội vã.", False),
                ("d", "Sau khi tách khỏi nguồn điện, nếu nạn nhân bất tỉnh phải tiến hành ép tim ngoài lồng ngực ngay lập tức.", True)
            ], "Xẻng sắt ướt dẫn điện gây nguy hiểm tính mạng người cứu hộ."),
            make_tf(4, "Thông hiểu", "Về hiện tượng ăn mòn điện hóa và bảo vệ kim loại đề 3:", [
                ("a", "Mạ một lớp kẽm lên vỏ tàu biển bằng thép là giải pháp bảo vệ vỏ tàu khỏi bị nước biển ăn mòn.", True),
                ("b", "Khi mạ điện, độ dày của lớp mạ phụ thuộc vào cường độ dòng điện chạy qua dung dịch mạ.", True),
                ("c", "Trong quá trình mạ vàng cho đồ trang sức, dung dịch mạ có thể thay thế bằng nước đường nguyên chất.", False),
                ("d", "Lớp mạ điện giúp tăng khả năng chống chịu thời tiết và tăng độ bóng sáng thẩm mỹ cho sản phẩm.", True)
            ], "Nước đường không dẫn điện, không mạ được.")
        ],
        [
            make_sa(1, "Thông hiểu", "Trong một thí nghiệm mạ đồng, người ta cho dòng điện chạy qua bình điện phân trong 20 phút thì thu được 0,32 g đồng. Nếu thời gian mạ tăng lên 60 phút với dòng điện không đổi, khối lượng đồng thu được là bao nhiêu gam?", "0.96", "m = 0,32 * (60 / 20) = 0,96 g."),
            make_sa(2, "Thông hiểu", "Một bình mạ bạc tiêu thụ dòng điện không đổi I = 2 A trong thời gian 500 giây. Điện lượng đã chuyển qua bình mạ là bao nhiêu Culông (C)?", "1000", "q = I * t = 2 * 500 = 1000 C."),
            make_sa(3, "Thông hiểu", "Khi mạ niken cho 5 chiếc chìa khóa giống nhau, mỗi chiếc cần 0,15 g niken bám vào. Tổng khối lượng niken cần dùng để mạ cả 5 chiếc chìa khóa là bao nhiêu gam?", "0.75", "m = 5 * 0,15 = 0,75 g."),
            make_sa(4, "Thông hiểu", "Dòng điện xoay chiều có cường độ an toàn tối đa cho cơ thể người tiếp xúc lâu dài là khoảng 10 mA. Giá trị 10 mA đổi sang đơn vị Ampe (A) là bao nhiêu?", "0.01", "10 mA = 0,01 A."),
            make_sa(5, "Vận dụng", "Trong công nghệ luyện nhôm điện phân, dòng điện có cường độ cực lớn I = 50 000 A chạy qua bể điện phân trong 1 giây. Điện lượng dịch chuyển qua bể trong 1 giây là bao nhiêu Culông (C)?", "50000", "q = 50 000 * 1 = 50 000 C."),
            make_sa(6, "Vận dụng", "Một máy sốc tim phát ra một xung điện mang năng lượng 200 Jun (J) trong thời gian 0,004 giây (4 mili-giây). Công suất cực đại của xung điện này là bao nhiêu Oát (W)?", "50000", "P = A / t = 200 / 0,004 = 50 000 W.")
        ],
        [
            make_vdc(1, "Một cơ sở sản xuất cần mạ một lớp đồng dày 20 μm (20 . 10^-6 m) lên bề mặt một tấm kim loại hình chữ nhật có kích thước 20 cm x 30 cm. Biết khối lượng riêng của đồng là D = 8900 kg/m3. Khối lượng đồng cần bám lên một mặt tấm kim loại là:", [
                "10,68 g", "5,34 g", "21,36 g", "1,07 g"
            ], 0, "S = 0,2 * 0,3 = 0,06 m2. V = 0,06 * 20e-6 = 1,2e-6 m3. m = 8900 * 1,2e-6 = 0,01068 kg = 10,68 g."),
            make_vdc(2, "Để mạ vàng cho 100 chiếc vỏ đồng hồ giống nhau, mỗi chiếc có diện tích bề mặt cần mạ là 40 cm2 với lớp vàng dày 2 μm (2 . 10^-6 m). Biết khối lượng riêng của vàng là D = 19 300 kg/m3. Tổng khối lượng vàng nguyên chất cần dùng cho lô hàng là:", [
                "15,44 g", "30,88 g", "7,72 g", "154,4 g"
            ], 0, "S_tong = 100 * 40 * 1e-4 = 0,4 m2. V = 0,4 * 2e-6 = 0,8e-6 m3. m = 19300 * 0,8e-6 = 0,01544 kg = 15,44 g."),
            make_vdc(3, "Một người có điện trở cơ thể đo từ tay sang chân là R = 2200 Ω. Nếu vô tình chạm vào dây pha của mạng điện 220 V có nối đất thì cường độ dòng điện chạy qua cơ thể người và mức độ nguy hiểm là:", [
                "I = 100 mA; cực kì nguy hiểm đến tính mạng (có thể gây tử vong ngay lập tức)",
                "I = 10 mA; chỉ bị giật tê nhẹ không nguy hiểm",
                "I = 1 mA; hoàn toàn không có cảm giác gì",
                "I = 2200 mA; nổ tung tức thì"
            ], 0, "I = U / R = 220 / 2200 = 0,1 A = 100 mA. Dòng 100 mA qua tim cực kì nguy hiểm gây tử vong."),
            make_vdc(4, "Một bể mạ niken sử dụng nguồn điện một chiều 6 V với dòng điện không đổi I = 25 A chạy qua liên tục trong thời gian 2 giờ (7200 giây). Điện năng mà bể mạ tiêu thụ trong suốt thời gian trên là:", [
                "1,08 MJ (tương đương 0,3 kWh)", "0,15 MJ", "2,16 MJ", "0,5 kWh"
            ], 0, "A = U * I * t = 6 * 25 * 7200 = 1 080 000 J = 1,08 MJ = 0,3 kWh.")
        ]
    )

    return exams
