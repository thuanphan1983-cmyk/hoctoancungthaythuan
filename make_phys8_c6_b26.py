# -*- coding: utf-8 -*-
"""
Dữ liệu 3 đề thi độc lập Bài 26: Năng lượng nhiệt và nội năng (phys8_c6_b26)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid, "level": level, "question": q_text,
        "options": options, "correct": correct_idx, "explanation": explanation
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid, "level": level, "question": prompt,
        "statements": [{"subId": s[0], "text": s[1], "correct": s[2]} for s in statements],
        "explanation": explanation
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid, "level": level, "question": q_text,
        "correctAnswer": str(answer).strip(), "explanation": explanation
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid, "level": "Vận dụng cao", "question": q_text,
        "options": options, "correct": correct_idx, "explanation": explanation
    }

def get_b26_exams():
    exams = {}
    ch_id = "phys8_c6"
    ch_title = "Chương VI: Nhiệt"
    les_id = "phys8_c6_b26"
    les_name = "Bài 26: Năng lượng nhiệt và nội năng"

    # ========================== ĐỀ 1 ==========================
    p1_t1 = [
        make_mc(1, "Nhận biết", "Năng lượng nhiệt của một vật là gì?",
                ["Tổng động năng của các phân tử cấu tạo nên vật", "Tổng thế năng của các phân tử cấu tạo nên vật", "Hiệu số động năng và thế năng của các phân tử", "Tổng cơ năng của toàn bộ vật khi chuyển động"],
                0, "Năng lượng nhiệt của vật là tổng động năng của các phân tử cấu tạo nên vật."),
        make_mc(2, "Nhận biết", "Khi nhiệt độ của một vật tăng lên thì:",
                ["Các phân tử cấu tạo nên vật chuyển động nhanh hơn", "Các phân tử cấu tạo nên vật chuyển động chậm lại", "Khối lượng của mỗi phân tử tăng lên", "Khoảng cách giữa các phân tử giảm về không"],
                0, "Nhiệt độ càng cao thì các phân tử chuyển động nhiệt càng nhanh."),
        make_mc(3, "Nhận biết", "Nội năng của một vật phụ thuộc vào yếu tố nào?",
                ["Nhiệt độ và thể tích của vật", "Chỉ phụ thuộc vào khối lượng vật", "Chỉ phụ thuộc vào độ cao của vật", "Tốc độ chuyển động của toàn bộ vật"],
                0, "Nội năng phụ thuộc vào nhiệt độ (ảnh hưởng động năng phân tử) và thể tích (ảnh hưởng thế năng tương tác phân tử)."),
        make_mc(4, "Nhận biết", "Đơn vị đo của năng lượng nhiệt trong hệ SI là:",
                ["Jun (J)", "Oát (W)", "Niu-tơn (N)", "Paxcan (Pa)"],
                0, "Đơn vị chuẩn của nhiệt năng/công/năng lượng trong hệ SI là Jun (J)."),
        make_mc(5, "Thông hiểu", "Khi cọ xát một đồng xu kim loại trên mặt bàn gỗ, đồng xu nóng lên là do:",
                ["Cơ năng đã chuyển hóa thành nội năng của đồng xu", "Đồng xu tự sinh ra nhiệt lượng mà không tốn công", "Nhiệt từ mặt bàn gỗ truyền sang đồng xu", "Thế năng của đồng xu chuyển hóa thành động năng"],
                0, "Hiện tượng cọ xát là quá trình thực hiện công chuyển hóa cơ năng thành nội năng."),
        make_mc(6, "Thông hiểu", "Thả một miếng nhôm nóng vào một cốc nước lạnh, nội năng của miếng nhôm và của nước thay đổi thế nào?",
                ["Nội năng miếng nhôm giảm, nội năng của nước tăng", "Nội năng miếng nhôm tăng, nội năng của nước giảm", "Nội năng của cả hai đều cùng tăng", "Nội năng của cả hai đều không thay đổi"],
                0, "Miếng nhôm tỏa nhiệt làm giảm nhiệt độ nên nội năng giảm; nước thu nhiệt làm tăng nhiệt độ nên nội năng tăng."),
        make_mc(7, "Thông hiểu", "Trường hợp nào sau đây làm biến đổi nội năng của vật bằng cách truyền nhiệt?",
                ["Phơi chiếc thìa nhôm ngoài trời nắng gắt", "Dùng búa đập nhiều lần vào thanh sắt", "Dùng cưa cưa đứt một khúc gỗ", "Mài dao trên bàn mài đá"],
                0, "Phơi thìa ngoài nắng là quá trình truyền nhiệt từ ánh nắng Mặt Trời sang thìa mà không có sự thực hiện công cơ học."),
        make_mc(8, "Thông hiểu", "Khi một khối khí trong xi lanh bị nén lại nhanh chóng, nhiệt độ khối khí tăng lên do:",
                ["Lực nén đã thực hiện công làm tăng nội năng của khối khí", "Nhiệt độ bên ngoài truyền vào trong xi lanh", "Khối lượng của chất khí tăng lên", "Áp suất giảm làm khí tự nóng lên"],
                0, "Pít-tông thực hiện công nén khí làm tăng động năng phân tử khí, tức làm tăng nội năng và nhiệt độ."),
        make_mc(9, "Thông hiểu", "Nhiệt lượng là gì?",
                ["Phần năng lượng nhiệt mà vật nhận thêm hay mất bớt đi trong quá trình truyền nhiệt", "Tổng năng lượng nhiệt sẵn có bên trong vật", "Nhiệt độ cao nhất mà vật có thể đạt tới", "Lượng nhiệt cần thiết để làm nóng chảy hoàn toàn vật"],
                0, "Nhiệt lượng là phần nhiệt năng nhận thêm hoặc mất đi trong quá trình truyền nhiệt."),
        make_mc(10, "Vận dụng", "Một viên đạn chì đang bay với vận tốc v đập vào bức tường cát và dừng lại. Khi đó cơ năng của viên đạn đã biến đổi thành:",
                ["Nội năng của viên đạn và của bức tường cát", "Thế năng trọng trường của viên đạn", "Quang năng của bức tường", "Nhiệt năng biến mất hoàn toàn không dấu vết"],
                0, "Động năng của viên đạn đã chuyển hóa thành nội năng làm nóng viên đạn và cát xung quanh."),
        make_mc(11, "Vận dụng", "Đun một ấm nước từ 25°C đến khi sôi 100°C. Trong quá trình này, năng lượng nhiệt của nước:",
                ["Tăng liên tục do nhận được nhiệt lượng từ bếp truyền sang", "Giảm dần vì các phân tử nước bay hơi mang nhiệt đi", "Không đổi vì khối lượng nước giảm dần", "Ban đầu tăng sau đó giảm mạnh"],
                0, "Nước nhận nhiệt lượng từ ngọn lửa nên nhiệt độ tăng, động năng phân tử tăng dẫn đến nội năng tăng."),
        make_mc(12, "Vận dụng", "Biết 1 cal ≈ 4,186 J. Nhiệt lượng 500 cal tương đương với bao nhiêu Jun?",
                ["2093 J", "119,4 J", "500 J", "4186 J"],
                0, "Q = 500 * 4,186 = 2093 J.")
    ]

    p2_t1 = [
        make_tf(1, "Thông hiểu", "Xét các phát biểu về năng lượng nhiệt và nhiệt độ:",
                [("a", "Năng lượng nhiệt của một vật bằng không khi vật ở nhiệt độ 0°C.", False),
                 ("b", "Nhiệt độ của vật càng cao thì các phân tử cấu tạo nên vật chuyển động nhiệt càng nhanh.", True),
                 ("c", "Hai vật có cùng nhiệt độ thì chắc chắn có cùng năng lượng nhiệt.", False),
                 ("d", "Năng lượng nhiệt là tổng động năng của các phân tử cấu tạo nên vật.", True)],
                "0°C các phân tử vẫn chuyển động nhiệt nên năng lượng nhiệt khác 0; vật có khối lượng khác nhau thì năng lượng nhiệt khác nhau dù cùng nhiệt độ."),
        make_tf(2, "Thông hiểu", "Xét các cách làm biến đổi nội năng của vật:",
                [("a", "Thực hiện công là quá trình có sự chuyển hóa từ cơ năng thành nội năng.", True),
                 ("b", "Truyền nhiệt là quá trình có sự chuyển hóa nội năng thành một dạng năng lượng khác.", False),
                 ("c", "Khi cọ xát miếng kim loại vào thanh gỗ, cả hai vật đều có nội năng tăng lên.", True),
                 ("d", "Thả cục nước đá vào ly nước ấm, nhiệt lượng truyền từ nước đá sang ly nước.", False)],
                "Truyền nhiệt không có sự chuyển hóa năng lượng mà chỉ có sự truyền nội năng từ vật nóng sang vật lạnh."),
        make_tf(3, "Vận dụng", "Xét quá trình nén khí và giãn khí trong ống tiêm kín:",
                [("a", "Dùng tay ấn nhanh pít-tông để nén khí, ta đã thực hiện công lên khối khí.", True),
                 ("b", "Khi nén nhanh khối khí, nội năng của khí giảm đi vì thể tích bị thu hẹp.", False),
                 ("c", "Nếu để khối khí nguội dần về nhiệt độ phòng, khí đã truyền nhiệt ra môi trường ngoài.", True),
                 ("d", "Nhiệt lượng khối khí truyền ra môi trường có đơn vị là Oát (W).", False)],
                "Nén khí làm nội năng tăng; đơn vị của nhiệt lượng là Jun (J) chứ không phải Oát (W)."),
        make_tf(4, "Vận dụng", "Xét hiện tượng nhiệt trong đời sống và kỹ thuật:",
                [("a", "Mũi khoan thép khi khoan vào bê tông bị nóng rực lên do thực hiện công.", True),
                 ("b", "Để làm nguội thanh sắt vừa rèn, thợ rèn nhúng thanh sắt vào chậu nước lạnh là phương pháp truyền nhiệt.", True),
                 ("c", "Khi hai vật tiếp xúc truyền nhiệt cho nhau, quá trình truyền nhiệt dừng lại khi hai vật có cùng nhiệt lượng.", False),
                 ("d", "Nhiệt lượng mà vật nóng tỏa ra bằng nhiệt lượng mà vật lạnh thu vào nếu không có thất thoát.", True)],
                "Truyền nhiệt dừng lại khi hai vật có cùng nhiệt độ, không phải cùng nhiệt lượng.")
    ]

    p3_t1 = [
        make_sa(1, "Thông hiểu", "Quy đổi nhiệt lượng 2,5 kJ ra đơn vị Jun (J).", "2500", "2,5 kJ = 2500 J."),
        make_sa(2, "Thông hiểu", "Một quả cầu kim loại nhận nhiệt lượng 600 J thì nội năng của nó tăng thêm bao nhiêu Jun (bỏ qua sự thay đổi thể tích)?", "600", "Theo định luật bảo toàn, ΔU = Q = 600 J."),
        make_sa(3, "Thông hiểu", "Đổi 1200 cal ra đơn vị Jun (lấy 1 cal = 4,186 J, làm tròn đến số nguyên gần nhất).", "5023", "1200 * 4,186 = 5023,2 ≈ 5023 J."),
        make_sa(4, "Vận dụng", "Thực hiện công 450 J để nén khí trong xi lanh, đồng thời khối khí tỏa ra môi trường nhiệt lượng 120 J. Nội năng khối khí tăng thêm bao nhiêu Jun?", "330", "ΔU = A - Q = 450 - 120 = 330 J."),
        make_sa(5, "Vận dụng", "Một vật có khối lượng 2 kg rơi tự do từ độ cao 15 m xuống đất mềm và nằm yên. Coi toàn bộ cơ năng chuyển thành nhiệt làm nóng vật và đất. Tính nhiệt lượng sinh ra (lấy g = 10 m/s²).", "300", "Q = m*g*h = 2 * 10 * 15 = 300 J."),
        make_sa(6, "Vận dụng", "Người ta cọ xát thanh nhôm có khối lượng 0,5 kg làm việc này sinh công 1050 J. Biết nhiệt dung riêng của nhôm c = 880 J/(kg.K). Bỏ qua tỏa nhiệt ra môi trường, nhiệt độ thanh nhôm tăng thêm xấp xỉ bao nhiêu độ C (làm tròn đến chữ số thập phân thứ hai)?", "2.39", "Δt = A / (m*c) = 1050 / (0,5 * 880) ≈ 2,39°C.")
    ]

    p4_t1 = [
        make_vdc(1, "Một búa máy khối lượng 500 kg rơi từ độ cao 4 m xuống đập vào cọc sắt khối lượng 100 kg trên mặt đất. Sau va chạm cọc lún sâu vào đất và búa dừng lại. Biết 40% cơ năng của búa chuyển thành nội năng làm nóng búa và cọc. Lấy g = 10 m/s². Nhiệt lượng làm tăng nội năng của hệ búa và cọc là:",
                 ["8000 J", "12000 J", "20000 J", "4000 J"],
                 0, "Cơ năng búa W = m*g*h = 500 * 10 * 4 = 20000 J. Nhiệt lượng Q = 0,4 * 20000 = 8000 J."),
        make_vdc(2, "Một xe tải có khối lượng 4 tấn đang chạy với tốc độ 54 km/h thì hãm phanh gấp và dừng lại sau quãng đường 25 m. Coi toàn bộ động năng của xe chuyển thành nhiệt lượng phân bố đều cho 4 má phanh bằng thép. Biết mỗi má phanh có khối lượng 5 kg, nhiệt dung riêng của thép c = 460 J/(kg.K). Bỏ qua tỏa nhiệt ra không khí. Độ tăng nhiệt độ của mỗi má phanh xấp xỉ bằng:",
                 ["48,9°C", "24,5°C", "97,8°C", "12,2°C"],
                 0, "v = 15 m/s. Động năng Wđ = 0,5 * 4000 * 15² = 450000 J. Mỗi má phanh nhận Q1 = 450000 / 4 = 112500 J. Δt = Q1 / (m1*c) = 112500 / (5 * 460) ≈ 48,9°C."),
        make_vdc(3, "Để tăng nội năng của 1 kg nước thêm 10500 J, người ta khuấy nước bằng một cánh quạt cơ học nối với động cơ có công suất 50 W. Giả sử hiệu suất truyền cơ năng thành nội năng là 70%. Thời gian cần thiết để khuấy nước là:",
                 ["300 giây", "150 giây", "210 giây", "420 giây"],
                 0, "Công suất có ích Pci = 50 * 0,7 = 35 W. Thời gian t = Q / Pci = 10500 / 35 = 300 s."),
        make_vdc(4, "Một khối khí lý tưởng nhận công 800 J từ pít-tông nén khí, đồng thời truyền ra môi trường nhiệt lượng 350 J. Sau đó khối khí được đun nóng nhận thêm nhiệt lượng 600 J và sinh công đẩy pít-tông ra một đoạn ứng với công 200 J. Độ biến thiên nội năng tổng cộng của khối khí sau cả hai quá trình là:",
                 ["850 J", "1250 J", "450 J", "650 J"],
                 0, "Giai đoạn 1: ΔU1 = A1 - Q1 = 800 - 350 = 450 J. Giai đoạn 2: ΔU2 = Q2 - A2 = 600 - 200 = 400 J. Tổng ΔU = 450 + 400 = 850 J.")
    ]

    exams[f"{les_id}_test1"] = {
        "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {les_name} - Đề số 01",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title, "lessonId": les_id, "lessonName": les_name,
        "testNum": 1, "duration": "45 phút", "points": 10.0,
        "part1": p1_t1, "part2": p2_t1, "part3": p3_t1, "part4": p4_t1
    }

    # ========================== ĐỀ 2 ==========================
    p1_t2 = [
        make_mc(1, "Nhận biết", "Trong quá trình truyền nhiệt, phần năng lượng nhiệt trao đổi giữa hai vật được gọi là:",
                ["Nhiệt lượng", "Nhiệt dung", "Nhiệt năng riêng", "Nội năng toàn phần"],
                0, "Nhiệt lượng là số đo lượng năng lượng nhiệt được truyền đi trong quá trình truyền nhiệt."),
        make_mc(2, "Nhận biết", "Kí hiệu chuẩn của nhiệt lượng trong vật lý là:",
                ["Q", "U", "A", "P"],
                0, "Nhiệt lượng được kí hiệu bằng chữ Q."),
        make_mc(3, "Nhận biết", "Khi hai vật truyền nhiệt cho nhau thì nhiệt lượng luôn tự truyền từ:",
                ["Vật có nhiệt độ cao sang vật có nhiệt độ thấp", "Vật có khối lượng lớn sang vật có khối lượng nhỏ", "Vật có thể tích lớn sang vật có thể tích nhỏ", "Vật có nhiệt dung riêng lớn sang vật có nhiệt dung riêng nhỏ"],
                0, "Nhiệt lượng tự truyền từ nơi có nhiệt độ cao hơn sang nơi có nhiệt độ thấp hơn."),
        make_mc(4, "Nhận biết", "Điều kiện để có quá trình truyền nhiệt giữa hai vật là:",
                ["Có sự chênh lệch nhiệt độ giữa hai vật", "Hai vật phải có cùng nhiệt độ ban đầu", "Hai vật phải có cùng khối lượng", "Hai vật phải ở trạng thái rắn"],
                0, "Điều kiện cần để truyền nhiệt là giữa hai vật có độ chênh lệch nhiệt độ Δt > 0."),
        make_mc(5, "Thông hiểu", "Trường hợp nào sau đây nội năng của vật tăng lên nhờ thực hiện công?",
                ["Bơm hơi vào lốp xe làm ống bơm nóng lên", "Cho một cục nước đá vào cốc nước nóng", "Bỏ quả trứng sống vào nồi nước đang sôi", "Đặt chảo sắt lên bếp ga đang cháy"],
                0, "Bơm lốp xe pít-tông cọ xát với thành bơm và nén khí, thực hiện công làm nóng ống bơm."),
        make_mc(6, "Thông hiểu", "Khi hai vật tiếp xúc truyền nhiệt với nhau đạt đến trạng thái cân bằng nhiệt thì:",
                ["Nhiệt độ của hai vật bằng nhau", "Nội năng của hai vật bằng nhau", "Khối lượng của hai vật bằng nhau", "Nhiệt lượng của hai vật bằng nhau"],
                0, "Trạng thái cân bằng nhiệt đạt được khi hai vật có nhiệt độ bằng nhau."),
        make_mc(7, "Thông hiểu", "Một thìa bạc nhúng vào cốc nước sôi, nhiệt độ thìa bạc tăng lên là do:",
                ["Nước sôi truyền nhiệt lượng cho thìa bạc", "Thìa bạc thực hiện công lên nước sôi", "Nước sôi nhận công từ thìa bạc", "Bạc tự sinh nhiệt năng khi ngập trong nước"],
                0, "Nước sôi có nhiệt độ cao hơn (100°C) truyền nhiệt lượng cho thìa bạc."),
        make_mc(8, "Thông hiểu", "Tại sao khi cưa gỗ, lưỡi cưa và khúc gỗ đều bị nóng lên?",
                ["Lực ma sát giữa lưỡi cưa và gỗ đã thực hiện công làm tăng nội năng của cả hai", "Lưỡi cưa đã hấp thụ nhiệt lượng từ khúc gỗ", "Không khí nén lại ở khe cưa sinh ra nhiệt", "Khúc gỗ truyền nhiệt lượng trực tiếp cho lưỡi cưa"],
                0, "Công của lực ma sát khi cưa chuyển hóa thành nội năng làm nóng cả lưỡi cưa và mặt cắt gỗ."),
        make_mc(9, "Thông hiểu", "Một giọt nước sôi ở 100°C và một ấm nước đầy ở 80°C. So sánh năng lượng nhiệt của chúng:",
                ["Ấm nước đầy có năng lượng nhiệt lớn hơn nhiều vì có tổng số phân tử lớn hơn rất nhiều", "Giọt nước có năng lượng nhiệt lớn hơn vì nhiệt độ cao hơn", "Cả hai có năng lượng nhiệt bằng nhau", "Không thể so sánh năng lượng nhiệt khi khác nhiệt độ"],
                0, "Năng lượng nhiệt là tổng động năng của tất cả phân tử. Ấm nước có khối lượng rất lớn nên tổng động năng lớn hơn nhiều giọt nước."),
        make_mc(10, "Vận dụng", "Người ta thả 100 g chì ở nhiệt độ 120°C vào một bình chứa 200 g nước ở 20°C. Bỏ qua trao đổi nhiệt với môi trường. Khi cân bằng nhiệt, nhiệt độ của nước:",
                ["Lớn hơn 20°C và nhỏ hơn 120°C", "Bằng đúng 120°C", "Nhỏ hơn 20°C", "Bằng trung bình cộng (120+20)/2 = 70°C"],
                0, "Nhiệt độ cân bằng nằm giữa nhiệt độ ban đầu của hai vật: 20°C < t < 120°C."),
        make_mc(11, "Vận dụng", "Một khối đồng nhận công 600 J từ máy dập và tỏa nhiệt 150 J ra không khí xung quanh. Nội năng của khối đồng đã:",
                ["Tăng thêm 450 J", "Giảm đi 450 J", "Tăng thêm 750 J", "Không đổi"],
                0, "ΔU = A - Q = 600 - 150 = 450 J (tăng thêm)."),
        make_mc(12, "Vận dụng", "Nhiệt lượng 1 kcal tương đương với bao nhiêu Jun (lấy 1 cal = 4,186 J)?",
                ["4186 J", "418,6 J", "1000 J", "239 J"],
                0, "1 kcal = 1000 cal = 1000 * 4,186 = 4186 J.")
    ]

    p2_t2 = [
        make_tf(1, "Thông hiểu", "Xét các kết luận về nhiệt lượng và truyền nhiệt:",
                [("a", "Nhiệt lượng không phải là một dạng năng lượng độc lập mà là số đo năng lượng nhiệt truyền đi.", True),
                 ("b", "Một vật có nhiệt độ cao thì luôn có nhiệt lượng lớn.", False),
                 ("c", "Khi truyền nhiệt, nhiệt lượng truyền đi có thể tính theo đơn vị Calo hoặc Jun.", True),
                 ("d", "Nếu hai vật không chênh lệch nhiệt độ thì không thể có sự truyền nhiệt tự phát giữa chúng.", True)],
                "Vật chứa nội năng chứ không chứa 'nhiệt lượng'; nhiệt lượng chỉ xuất hiện trong quá trình truyền nhiệt."),
        make_tf(2, "Thông hiểu", "Xét các hiện tượng thực tế về biến đổi nội năng:",
                [("a", "Quẹt diêm vào vỏ bao diêm làm diêm bốc cháy là ví dụ về biến đổi nội năng bằng thực hiện công.", True),
                 ("b", "Nung đỏ thanh sắt trong lò than là quá trình biến đổi nội năng bằng thực hiện công.", False),
                 ("c", "Đóng đinh vào khúc gỗ, đầu đinh nóng lên là do lực đập của búa thực hiện công.", True),
                 ("d", "Để cốc nước chanh đá ngoài trời một lúc thấy đá tan chảy là quá trình truyền nhiệt.", True)],
                "Nung thanh sắt trong lò than là quá trình truyền nhiệt từ than nóng đỏ sang thanh sắt."),
        make_tf(3, "Vận dụng", "Xét sự thay đổi nội năng của khối khí trong xilanh pít-tông:",
                [("a", "Nếu pít-tông nhận công 200 J và khí nhận nhiệt lượng 100 J thì nội năng tăng 300 J.", True),
                 ("b", "Nếu khí giãn nở đẩy pít-tông sinh công 150 J mà không nhận nhiệt thì nội năng khí tăng 150 J.", False),
                 ("c", "Khi khối khí tỏa nhiệt ra bên ngoài thì nhiệt độ của nó có xu hướng giảm.", True),
                 ("d", "Khí nhận nhiệt lượng và không sinh công thì toàn bộ nhiệt lượng làm tăng nội năng của khí.", True)],
                "Khí sinh công mà không nhận nhiệt thì nội năng khí giảm ΔU = -A = -150 J."),
        make_tf(4, "Vận dụng", "Xét bài toán nhiệt học thực tế:",
                [("a", "Khi phanh xe đạp gấp, vành xe và má phanh nóng lên do động năng chuyển hóa thành nội năng.", True),
                 ("b", "Nhiệt lượng tỏa ra ở má phanh xe đạp bằng tích của lực ma sát và quãng đường phanh.", True),
                 ("c", "Nhiệt năng có thể tự truyền từ vật có nội năng nhỏ sang vật có nội năng lớn hơn mà không cần tác nhân ngoài.", False),
                 ("d", "Trong hệ kín cô lập, độ tăng nội năng của vật này bằng độ giảm nội năng của vật khác.", True)],
                "Nhiệt năng chỉ tự truyền từ nơi nhiệt độ cao sang nhiệt độ thấp, không phụ thuộc giá trị nội năng.")
    ]

    p3_t2 = [
        make_sa(1, "Thông hiểu", "Đổi 3,6 kJ ra đơn vị Jun (J).", "3600", "3,6 kJ = 3600 J."),
        make_sa(2, "Thông hiểu", "Một khối sắt có nội năng ban đầu là 1200 J. Sau khi nhận nhiệt lượng 450 J, nội năng của nó là bao nhiêu Jun?", "1650", "U = 1200 + 450 = 1650 J."),
        make_sa(3, "Thông hiểu", "Biết 1 cal = 4,186 J. Nhiệt lượng 250 cal bằng bao nhiêu Jun (làm tròn đến 1 chữ số thập phân)?", "1046.5", "250 * 4,186 = 1046,5 J."),
        make_sa(4, "Vận dụng", "Dùng búa đập nhiều lần vào một miếng chì, búa sinh công 720 J. Biết 80% công này chuyển thành nội năng của miếng chì. Nhiệt lượng miếng chì nhận được là bao nhiêu Jun?", "576", "Q = 0,8 * 720 = 576 J."),
        make_sa(5, "Vận dụng", "Thực hiện công 500 J để nén khí trong xilanh. Khối khí tăng nội năng thêm 380 J. Hỏi khối khí đã truyền ra ngoài một nhiệt lượng bằng bao nhiêu Jun?", "120", "Q = A - ΔU = 500 - 380 = 120 J."),
        make_sa(6, "Vận dụng", "Một giọt nước mưa khối lượng 0,05 g rơi từ đám mây cao 1200 m xuống mặt đất với vận tốc chạm đất 10 m/s. Lấy g = 10 m/s². Tính nhiệt lượng sinh ra do ma sát với không khí trong suốt quá trình rơi (tính bằng Jun, làm tròn đến 3 chữ số thập phân).", "0.598", "Cơ năng ban đầu W1 = m*g*h = 5e-5 * 10 * 1200 = 0,6 J. Động năng chạm đất W2 = 0,5 * 5e-5 * 10² = 0,0025 J. Q = W1 - W2 = 0,5975 ≈ 0,598 J.")
    ]

    p4_t2 = [
        make_vdc(1, "Một viên đạn bạc có khối lượng 20 g đang bay với vận tốc 300 m/s thì xuyên vào một tấm gỗ dày và dừng lại. Biết 60% động năng của viên đạn chuyển thành nội năng làm nóng viên đạn. Nhiệt dung riêng của bạc c = 234 J/(kg.K). Bỏ qua sự truyền nhiệt ra môi trường. Độ tăng nhiệt độ của viên đạn xấp xỉ bằng:",
                 ["115,4°C", "192,3°C", "76,9°C", "230,8°C"],
                 0, "Wđ = 0,5 * 0,02 * 300² = 900 J. Q = 0,6 * 900 = 540 J. Δt = Q / (m*c) = 540 / (0,02 * 234) ≈ 115,38°C ≈ 115,4°C."),
        make_vdc(2, "Để đun nóng 2 lít nước từ 20°C đến 100°C, người ta dùng bếp điện có hiệu suất 80%. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K) và khối lượng riêng của nước D = 1000 kg/m³. Điện năng toàn phần mà bếp điện đã tiêu thụ là:",
                 ["840 kJ", "672 kJ", "1050 kJ", "537,6 kJ"],
                 0, "m = 2 kg. Qthu = 2 * 4200 * 80 = 672000 J = 672 kJ. A = Qthu / 0,8 = 672 / 0,8 = 840 kJ."),
        make_vdc(3, "Một xilanh chứa 0,2 kg khí ở áp suất không đổi. Khí nhận nhiệt lượng 1200 J từ nguồn nhiệt ngoài, đồng thời giãn nở sinh công 450 J đẩy pít-tông di chuyển. Sau đó, người ta làm mát khí bằng cách cho tỏa nhiệt 300 J trong khi giữ cố định pít-tông. Biến thiên nội năng tổng cộng của khối khí là:",
                 ["450 J", "750 J", "1050 J", "150 J"],
                 0, "Quá trình 1: ΔU1 = Q1 - A1 = 1200 - 450 = 750 J. Quá trình 2: ΔU2 = -300 J (giữ cố định pít-tông nên A2 = 0). Tổng ΔU = 750 - 300 = 450 J."),
        make_vdc(4, "Một ô tô có khối lượng 1,5 tấn hãm phanh đều trên đoạn dốc dài 100 m, nghiêng góc so với phương ngang có độ chênh cao 8 m. Tốc độ của ô tô ở đỉnh dốc là 54 km/h và ở chân dốc là 36 km/h. Lấy g = 10 m/s². Toàn bộ phần cơ năng giảm đi đã biến đổi thành nhiệt làm nóng phanh và lốp xe. Nhiệt lượng sinh ra trong quá trình xuống dốc là:",
                 ["213,75 kJ", "120 kJ", "93,75 kJ", "307,5 kJ"],
                 0, "v1 = 15 m/s, v2 = 10 m/s. W1 = 0,5 * 1500 * 15² + 1500 * 10 * 8 = 168750 + 120000 = 288750 J. W2 = 0,5 * 1500 * 10² = 75000 J. Q = W1 - W2 = 213750 J = 213,75 kJ.")
    ]

    exams[f"{les_id}_test2"] = {
        "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {les_name} - Đề số 02",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title, "lessonId": les_id, "lessonName": les_name,
        "testNum": 2, "duration": "45 phút", "points": 10.0,
        "part1": p1_t2, "part2": p2_t2, "part3": p3_t2, "part4": p4_t2
    }

    # ========================== ĐỀ 3 ==========================
    p1_t3 = [
        make_mc(1, "Nhận biết", "Trong mô hình động học phân tử chất khí, các phân tử khí chuyển động:",
                ["Hỗn loạn không ngừng về mọi phía", "Theo các quỹ đạo tròn đồng tâm", "Chỉ theo phương thẳng đứng từ dưới lên", "Chỉ chuyển động khi có tác dụng của gió"],
                0, "Các phân tử khí chuyển động hỗn loạn không ngừng về mọi phía gọi là chuyển động nhiệt."),
        make_mc(2, "Nhận biết", "Độ không tuyệt đối (0 K) trên thang Kelvin tương ứng với nhiệt độ nào trên thang Celsius?",
                ["-273,15°C", "0°C", "100°C", "-100°C"],
                0, "T (K) = t (°C) + 273,15 => 0 K tương ứng -273,15°C."),
        make_mc(3, "Nhận biết", "Thiết bị nào sau đây hoạt động dựa trên nguyên tắc chuyển đổi nội năng thành cơ năng?",
                ["Động cơ nhiệt (như động cơ xe máy)", "Máy phát điện gió", "Tua-bin thủy điện", "Pin mặt trời"],
                0, "Động cơ nhiệt đốt nhiên liệu giải phóng nội năng rồi chuyển một phần thành cơ năng sinh công."),
        make_mc(4, "Nhận biết", "Nhiệt lượng do một vật tỏa ra khi hạ nhiệt độ phụ thuộc vào:",
                ["Khối lượng, nhiệt dung riêng và độ giảm nhiệt độ của vật", "Chỉ phụ thuộc vào hình dạng của vật", "Chỉ phụ thuộc vào vận tốc chuyển động của vật", "Độ cao của vật so với mặt đất"],
                0, "Công thức tính nhiệt lượng: Q = m * c * Δt."),
        make_mc(5, "Thông hiểu", "Hiện tượng khuếch tán giữa hai chất lỏng xảy ra nhanh hơn khi nhiệt độ tăng là do:",
                ["Các phân tử chất lỏng chuyển động nhiệt nhanh hơn làm chúng xen vào nhau nhanh hơn", "Khối lượng của các phân tử lỏng giảm đi", "Lực hút phân tử biến mất hoàn toàn", "Chất lỏng bay hơi hết"],
                0, "Nhiệt độ tăng làm tốc độ chuyển động nhiệt của các phân tử tăng, hiện tượng khuếch tán diễn ra nhanh hơn."),
        make_mc(6, "Thông hiểu", "Một quả bóng bàn bị móp nhưng chưa thủng, khi nhúng vào bát nước nóng nó lại phồng lên như cũ. Hiện tượng này giải thích là do:",
                ["Không khí bên trong quả bóng nhận nhiệt, nóng lên nở ra làm tăng áp suất đẩy vỏ phồng lên", "Vỏ quả bóng bàn hút nước nóng vào trong", "Nước nóng tác dụng lực đẩy Ác-si-mét làm phồng vỏ", "Chất nhựa làm vỏ bóng tự co lại"],
                0, "Không khí trong quả bóng nhận nhiệt năng từ nước nóng, nhiệt độ tăng nên khí nở ra sinh công làm phồng vỏ bóng."),
        make_mc(7, "Thông hiểu", "Trộn 100 ml rượu với 100 ml nước thu được hỗn hợp có thể tích khoảng 195 ml. Nguyên nhân là do:",
                ["Giữa các phân tử nước và phân tử rượu có khoảng cách nên chúng xen kẽ vào nhau", "Một lượng rượu đã tự bốc cháy sinh nhiệt", "Nước tác dụng hóa học làm mất đi một phần chất lỏng", "Dụng cụ đo thể tích bị sai số 5 ml"],
                0, "Cấu tạo phân tử có khoảng cách nên các phân tử của chất này xen vào khoảng cách giữa các phân tử của chất kia."),
        make_mc(8, "Thông hiểu", "Khi một khối kim loại nguội đi trong không khí:",
                ["Năng lượng nhiệt của khối kim loại giảm dần vì nó truyền nhiệt cho không khí xung quanh", "Năng lượng nhiệt của khối kim loại tăng lên", "Khối lượng kim loại bị hao hụt", "Số lượng nguyên tử kim loại giảm đi"],
                0, "Khối kim loại tỏa nhiệt ra không khí nên nhiệt độ giảm, động năng phân tử giảm, nội năng giảm."),
        make_mc(9, "Thông hiểu", "Một máy hơi nước tiêu thụ nhiệt lượng 10000 J từ nhiên liệu và sinh ra công cơ học có ích là 2500 J. Hiệu suất của máy hơi nước là:",
                ["25%", "40%", "75%", "10%"],
                0, "Hiệu suất H = A_ich / Q_toanphan = 2500 / 10000 = 25%."),
        make_mc(10, "Vận dụng", "Thả một miếng đồng có khối lượng 0,5 kg được nung nóng tới 100°C vào chậu chứa 1 kg nước ở 25°C. Nhiệt dung riêng của đồng c1 = 380 J/(kg.K), của nước c2 = 4200 J/(kg.K). Bỏ qua nhiệt lượng truyền cho chậu và môi trường. Nhiệt độ cân bằng xấp xỉ bằng:",
                ["28,2°C", "62,5°C", "35,0°C", "26,1°C"],
                0, "Qtỏa = Qthu => 0,5*380*(100 - t) = 1*4200*(t - 25) => 190*(100 - t) = 4200*(t - 25) => 4390*t = 124000 => t ≈ 28,25°C ≈ 28,2°C."),
        make_mc(11, "Vận dụng", "Người ta dùng máy khoan để khoan một lỗ trên tấm nhôm. Công suất của máy khoan là 400 W và khoan trong thời gian 30 giây. Biết 75% công của máy khoan biến thành nhiệt làm nóng mũi khoan và tấm nhôm. Nhiệt lượng sinh ra là:",
                ["9000 J", "12000 J", "3000 J", "6000 J"],
                0, "Công toàn phần A = P * t = 400 * 30 = 12000 J. Q = 0,75 * 12000 = 9000 J."),
        make_mc(12, "Vận dụng", "Biết nhiệt nóng chảy riêng của nước đá là λ = 3,34 * 10⁵ J/kg. Cần cung cấp nhiệt lượng bao nhiêu để làm nóng chảy hoàn toàn 2 kg nước đá ở 0°C?",
                ["6,68 * 10⁵ J", "3,34 * 10⁵ J", "1,67 * 10⁵ J", "6,68 * 10⁴ J"],
                0, "Q = m * λ = 2 * 3,34 * 10⁵ = 6,68 * 10⁵ J.")
    ]

    p2_t3 = [
        make_tf(1, "Thông hiểu", "Xét các đặc điểm của cấu tạo chất và nội năng:",
                [("a", "Các chất được cấu tạo từ các hạt riêng biệt gọi là nguyên tử, phân tử.", True),
                 ("b", "Khi nhiệt độ tuyệt đối T = 0 K, các phân tử chuyển động với vận tốc cực đại.", False),
                 ("c", "Thể tích của một chất rắn tăng lên khi nóng lên là do khoảng cách trung bình giữa các phân tử tăng.", True),
                 ("d", "Hiện tượng chuyển động của các hạt phấn hoa trong thí nghiệm của Brown chứng tỏ các phân tử nước chuyển động không ngừng.", True)],
                "Ở 0 K lý thuyết các phân tử ngừng chuyển động nhiệt, không phải vận tốc cực đại."),
        make_tf(2, "Thông hiểu", "Xét hoạt động của động cơ nhiệt:",
                [("a", "Động cơ nhiệt là thiết bị chuyển hóa toàn bộ 100% nhiệt lượng nhận được thành công cơ học.", False),
                 ("b", "Nguồn nóng cung cấp nhiệt lượng cho tác nhân, tác nhân giãn nở sinh công và truyền nhiệt lượng còn lại cho nguồn lạnh.", True),
                 ("c", "Hiệu suất của động cơ nhiệt luôn nhỏ hơn 100% do có nhiệt lượng truyền cho nguồn lạnh và hao phí ma sát.", True),
                 ("d", "Khí thải từ động cơ đốt trong ra môi trường mang theo một phần nội năng chưa được sử dụng.", True)],
                "Theo nguyên lý nhiệt động học, không thể có động cơ nhiệt đạt hiệu suất 100% biến đổi hoàn toàn nhiệt thành công."),
        make_tf(3, "Vận dụng", "Xét quá trình biến đổi nội năng trong xilanh động cơ xăng 4 kỳ:",
                [("a", "Kỳ nén pít-tông đi lên nén hỗn hợp nhiên liệu làm tăng nhiệt độ và nội năng của khí bằng cách thực hiện công.", True),
                 ("b", "Kỳ nổ (sinh công) bu-gi đánh lửa đốt cháy nhiên liệu, khí giãn nở thực hiện công đẩy pít-tông đi xuống.", True),
                 ("c", "Trong kỳ nổ, nội năng của khí đốt cháy biến đổi thành cơ năng của pít-tông.", True),
                 ("d", "Nếu bỏ qua ma sát thì toàn bộ năng lượng của nhiên liệu được chuyển thành cơ năng chuyển động của xe.", False)],
                "Luôn có nhiệt lượng thất thoát qua thành xilanh, hệ thống làm mát và khí thải."),
        make_tf(4, "Vận dụng", "Xét bài toán bảo toàn và chuyển hóa năng lượng nhiệt:",
                [("a", "Đơn vị của nhiệt dung riêng là J/(kg.K).", True),
                 ("b", "Hai vật có cùng khối lượng nhận cùng một nhiệt lượng thì vật nào có nhiệt dung riêng lớn hơn sẽ tăng nhiệt độ nhiều hơn.", False),
                 ("c", "Trong phương trình cân bằng nhiệt, tổng nhiệt lượng tỏa ra bằng tổng nhiệt lượng thu vào nếu bỏ qua thất thoát.", True),
                 ("d", "Nhiệt lượng tỏa ra khi ngưng tụ hơi nước ở 100°C có thể dùng để làm nóng các vật khác.", True)],
                "Δt = Q / (m*c). Với cùng Q và m, c lớn hơn thì Δt sẽ nhỏ hơn.")
    ]

    p3_t3 = [
        make_sa(1, "Thông hiểu", "Một động cơ xe máy nhận nhiệt lượng 40 kJ từ xăng đốt cháy và sinh công cơ học 12 kJ. Hiệu suất của động cơ là bao nhiêu phần trăm (%)?", "30", "H = 12 / 40 * 100% = 30%."),
        make_sa(2, "Thông hiểu", "Cần cung cấp bao nhiêu Jun nhiệt lượng để làm nóng 0,5 kg nhôm từ 20°C lên 80°C? Biết nhiệt dung riêng của nhôm c = 880 J/(kg.K).", "26400", "Q = m*c*Δt = 0,5 * 880 * 60 = 26400 J."),
        make_sa(3, "Thông hiểu", "Đổi 5000 J sang đơn vị Calo (lấy 1 cal = 4,186 J, làm tròn đến số nguyên gần nhất).", "1194", "5000 / 4,186 ≈ 1194,46 ≈ 1194 cal."),
        make_sa(4, "Vận dụng", "Một thác nước cao 30 m đổ xuống. Coi 60% thế năng của nước chuyển thành nội năng làm nóng nước ở chân thác. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K), lấy g = 10 m/s². Độ tăng nhiệt độ của nước xấp xỉ bằng bao nhiêu độ C (làm tròn đến 3 chữ số thập phân)?", "0.043", "Δt = 0,6 * g * h / c = 0,6 * 10 * 30 / 4200 = 180 / 4200 ≈ 0,04286 ≈ 0,043°C."),
        make_sa(5, "Vận dụng", "Một khối khí thực hiện công 750 J khi giãn nở, đồng thời nội năng của khí giảm 250 J. Tính nhiệt lượng mà khối khí đã nhận vào từ môi trường (tính bằng Jun).", "500", "ΔU = Q - A => -250 = Q - 750 => Q = 500 J."),
        make_sa(6, "Vận dụng", "Thả một quả cầu kim loại khối lượng 300 g ở nhiệt độ 150°C vào bình chứa 500 g nước ở 20°C. Khi cân bằng, nhiệt độ là 25°C. Bỏ qua nhiệt dung của bình và thất thoát ra ngoài. Biết c_nước = 4200 J/(kg.K). Tính nhiệt dung riêng của kim loại quả cầu (J/(kg.K), làm tròn đến số nguyên).", "280", "Qthu = 0,5 * 4200 * (25 - 20) = 10500 J. Qtỏa = 0,3 * c * (150 - 25) = 37,5 * c. c = 10500 / 37,5 = 280 J/(kg.K).")
    ]

    p4_t3 = [
        make_vdc(1, "Một ô tô có khối lượng 1,2 tấn chạy với vận tốc không đổi 72 km/h trên đường nằm ngang. Lực cản của mặt đường và không khí tác dụng lên xe là 600 N. Động cơ xe tiêu thụ 8 lít xăng trên quãng đường 100 km. Biết năng suất tỏa nhiệt của xăng q = 46 * 10⁶ J/kg và khối lượng riêng của xăng D = 700 kg/m³. Hiệu suất của động cơ ô tô xấp xỉ bằng:",
                 ["23,3%", "32,5%", "18,4%", "28,7%"],
                 0, "Công có ích trên 100 km: A = F * s = 600 * 100000 = 60 * 10⁶ J. Khối lượng xăng m = 0,008 * 700 = 5,6 kg. Nhiệt lượng tỏa ra: Q = m * q = 5,6 * 46 * 10⁶ = 257,6 * 10⁶ J. H = A / Q = 60 / 257,6 ≈ 23,29% ≈ 23,3%."),
        make_vdc(2, "Người ta thả một cục sắt khối lượng m1 được nung nóng đến 500°C vào một bình cách nhiệt chứa 1 kg nước và 0,5 kg nước đá ở 0°C. Khi cân bằng nhiệt, toàn bộ nước đá tan hết và nhiệt độ của hệ là 30°C. Biết nhiệt dung riêng của sắt c1 = 460 J/(kg.K), của nước c2 = 4200 J/(kg.K), nhiệt nóng chảy của nước đá λ = 3,34 * 10⁵ J/kg. Bỏ qua nhiệt dung của bình. Khối lượng m1 của cục sắt xấp xỉ bằng:",
                 ["1,65 kg", "2,15 kg", "1,20 kg", "2,80 kg"],
                 0, "Nhiệt lượng thu vào: Qthu = m_đá * λ + (m_nước + m_đá) * c2 * (30 - 0) = 0,5 * 3,34 * 10⁵ + 1,5 * 4200 * 30 = 167000 + 189000 = 356000 J. Nhiệt lượng sắt tỏa ra: Qtỏa = m1 * 460 * (500 - 30) = m1 * 460 * 470 = 216200 * m1. m1 = 356000 / 216200 ≈ 1,6466 kg ≈ 1,65 kg."),
        make_vdc(3, "Một xilanh đặt thẳng đứng có pít-tông nặng 2 kg, diện tích tiết diện S = 50 cm² chứa 0,02 m³ khí ở nhiệt độ 27°C. Áp suất khí quyển bên ngoài là p0 = 10⁵ Pa. Người ta đun nóng chậm khối khí để pít-tông đi lên một đoạn 10 cm. Lấy g = 10 m/s². Bỏ qua ma sát. Công do khối khí thực hiện để đẩy pít-tông lên là:",
                 ["52 J", "50 J", "2 J", "104 J"],
                 0, "Áp suất khí trong xilanh: p = p0 + (m_p * g) / S = 10⁵ + (2 * 10) / (50 * 10⁻⁴) = 10⁵ + 4000 = 104000 Pa. Độ tăng thể tích: ΔV = S * h = 50 * 10⁻⁴ * 0,1 = 5 * 10⁻⁴ m³. Công thực hiện: A = p * ΔV = 104000 * 5 * 10⁻⁴ = 52 J."),
        make_vdc(4, "Một máy làm lạnh công nghiệp có công suất điện tiêu thụ là 2 kW hoạt động để đóng băng nước thành đá. Máy lấy đi nhiệt lượng từ nước trong buồng lạnh với tốc độ gấp 3 lần công suất điện tiêu thụ (hệ số hiệu quả làm lạnh COP = 3). Hỏi máy cần hoạt động trong thời gian bao lâu để biến 50 lít nước từ nhiệt độ ban đầu 20°C thành nước đá ở -5°C? Cho biết c_nước = 4200 J/(kg.K), c_đá = 2100 J/(kg.K), λ = 3,34 * 10⁵ J/kg, D_nước = 1000 kg/m³. Bỏ qua thất thoát nhiệt.",
                 ["3575 giây", "2850 giây", "4200 giây", "1980 giây"],
                 0, "m = 50 kg. Nhiệt lượng cần rút ra: Q1 (hạ 20°C về 0°C) = 50 * 4200 * 20 = 4,2 * 10⁶ J. Q2 (đông đặc ở 0°C) = 50 * 3,34 * 10⁵ = 16,7 * 10⁶ J. Q3 (hạ 0°C về -5°C) = 50 * 2100 * 5 = 0,525 * 10⁶ J. Tổng Q = 21,425 * 10⁶ J. Tốc độ làm lạnh P_lạnh = 3 * 2000 = 6000 W = 6 kW. Thời gian t = 21,425 * 10⁶ / 6000 ≈ 3570,8 s ≈ 3575 s (làm tròn).")
    ]

    exams[f"{les_id}_test3"] = {
        "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {les_name} - Đề số 03",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title, "lessonId": les_id, "lessonName": les_name,
        "testNum": 3, "duration": "45 phút", "points": 10.0,
        "part1": p1_t3, "part2": p2_t3, "part3": p3_t3, "part4": p4_t3
    }

    return exams

if __name__ == '__main__':
    exs = get_b26_exams()
    print("Generated Bài 26:", len(exs), "exams.")
