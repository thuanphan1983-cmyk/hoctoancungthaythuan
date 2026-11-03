# -*- coding: utf-8 -*-
"""
Dữ liệu 5 đề thi độc lập Ôn tập cuối Chương VI: Nhiệt (phys8_c6_rev)
- Đề 1: Tổng hợp kiến thức cơ bản về năng lượng nhiệt, nội năng, 3 hình thức truyền nhiệt, nở vì nhiệt.
- Đề 2: Biến đổi nội năng, dẫn nhiệt và vật liệu cách nhiệt, hoạt động của băng kép.
- Đề 3: Nhiệt lượng kế, đo nhiệt dung riêng kim loại, dòng đối lưu và hoàn lưu tự nhiên.
- Đề 4: Hiệu suất nhiệt, bức xạ nhiệt và phích nước, tính toán nhiệt lượng đun sôi.
- Đề 5: Lực co dãn nhiệt trong công trình, sự nở dị thường của nước, bài toán cân bằng nhiệt chuyên sâu.
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

def get_c6_rev_exams():
    exams = {}
    ch_id = "phys8_c6"
    ch_title = "Chương VI: Nhiệt"
    les_id = "phys8_c6_rev"
    les_name = "Ôn tập cuối Chương VI"

    # ========================== ĐỀ 1 ==========================
    p1_t1 = [
        make_mc(1, "Nhận biết", "Năng lượng nhiệt của một vật tăng lên khi nào?",
                ["Nhiệt độ của vật tăng lên", "Khối lượng của vật giảm đi", "Vật chuyển động chậm dần", "Đưa vật lên độ cao lớn hơn"],
                0, "Khi nhiệt độ tăng, các phân tử chuyển động nhanh hơn làm tổng động năng phân tử tăng, tức năng lượng nhiệt tăng."),
        make_mc(2, "Nhận biết", "Hình thức truyền nhiệt chủ yếu trong chất rắn là gì?",
                ["Dẫn nhiệt", "Đối lưu", "Bức xạ nhiệt", "Bay hơi"],
                0, "Trong chất rắn hình thức truyền nhiệt chủ yếu là dẫn nhiệt."),
        make_mc(3, "Nhận biết", "Chất nào sau đây nở vì nhiệt nhiều nhất khi cùng tăng một khoảng nhiệt độ?",
                ["Khí nitơ", "Nước", "Nhôm", "Đồng"],
                0, "Chất khí nở vì nhiệt nhiều hơn chất lỏng và chất rắn."),
        make_mc(4, "Nhận biết", "Dụng cụ dùng để đo năng lượng nhiệt trao đổi trong thí nghiệm nhiệt học là:",
                ["Nhiệt lượng kế", "Lực kế", "Tốc kế", "Ampe kế"],
                0, "Nhiệt lượng kế dùng để đo nhiệt lượng trao đổi giữa các vật."),
        make_mc(5, "Thông hiểu", "Một chiếc thìa nhôm và một chiếc đũa gỗ cùng để trong phòng ở 20°C. Khi chạm tay vào thìa nhôm ta cảm thấy lạnh hơn đũa gỗ vì:",
                ["Nhôm dẫn nhiệt tốt hơn gỗ nên truyền nhanh nhiệt lượng từ tay ta đi", "Nhiệt độ của thìa nhôm thấp hơn đũa gỗ", "Đũa gỗ tự tỏa nhiệt sưởi ấm tay", "Nhôm tỏa ra hơi lạnh"],
                0, "Cả hai cùng nhiệt độ 20°C nhưng nhôm dẫn nhiệt tốt hơn nên nhiệt từ tay truyền sang nhôm nhanh hơn, làm tay mất nhiệt nhanh hơn."),
        make_mc(6, "Thông hiểu", "Trường hợp nào sau đây nội năng của vật biến đổi do thực hiện công?",
                ["Xoa mạnh hai lòng bàn tay vào nhau làm tay ấm lên", "Để cốc nước chanh đá ngoài trời nắng", "Bỏ quả trứng vào nồi nước đang sôi", "Hơ nóng thanh sắt trên ngọn lửa đèn cồn"],
                0, "Xoa hai bàn tay lực ma sát thực hiện công chuyển hóa cơ năng thành nội năng làm tay ấm lên."),
        make_mc(7, "Thông hiểu", "Hình thức truyền nhiệt nào có thể xảy ra trong môi trường chân không tuyệt đối?",
                ["Bức xạ nhiệt", "Dẫn nhiệt", "Đối lưu", "Cả dẫn nhiệt và đối lưu"],
                0, "Bức xạ nhiệt truyền bằng sóng điện từ nên truyền được qua chân không."),
        make_mc(8, "Thông hiểu", "Khi làm lạnh một khối khí trong bình kín thì:",
                ["Nội năng của khối khí giảm", "Khối lượng của chất khí giảm", "Các phân tử khí chuyển động nhanh hơn", "Khối lượng riêng của khí giảm"],
                0, "Làm lạnh làm giảm nhiệt độ, tốc độ phân tử giảm nên nội năng giảm."),
        make_mc(9, "Thông hiểu", "Tại sao quả bóng bay bơm căng để ngoài trời nắng gắt dễ bị nổ tung?",
                ["Không khí trong bóng nóng lên nở ra làm tăng áp suất bên trong vượt quá sức chịu đựng của màng bóng", "Cao su tự hút nhiệt co lại", "Ánh sáng mặt trời ăn mòn cao su", "Gió thổi mạnh ép vào bóng"],
                0, "Khí trong bóng nhận nhiệt nở ra làm tăng áp suất phá vỡ màng bóng cao su."),
        make_mc(10, "Vận dụng", "Người ta thả 0,2 kg nước ở 80°C vào 0,3 kg nước ở 20°C trong bình cách nhiệt. Nhiệt độ khi cân bằng là:",
                ["44°C", "50°C", "35°C", "60°C"],
                0, "0,2 * c * (80 - t) = 0,3 * c * (t - 20) => 16 - 0,2t = 0,3t - 6 => 0,5t = 22 => t = 44°C."),
        make_mc(11, "Vận dụng", "Một thanh đồng dài 1,5 m ở 20°C. Biết hệ số nở dài của đồng là α = 17 * 10⁻⁶ K⁻¹. Khi nhiệt độ tăng lên 60°C, chiều dài thanh đồng tăng thêm:",
                ["1,02 mm", "0,51 mm", "2,04 mm", "1,53 mm"],
                0, "ΔL = 17 * 10⁻⁶ * 1,5 * 40 = 1,02 * 10⁻³ m = 1,02 mm."),
        make_mc(12, "Vận dụng", "Cần bao nhiêu nhiệt lượng để đun nóng 1,5 kg nước từ 25°C lên 100°C? Biết c_nước = 4200 J/(kg.K).",
                ["472,5 kJ", "315 kJ", "630 kJ", "157,5 kJ"],
                0, "Q = 1,5 * 4200 * 75 = 472500 J = 472,5 kJ.")
    ]

    p2_t1 = [
        make_tf(1, "Thông hiểu", "Xét các hình thức truyền nhiệt trong tự nhiên:",
                [("a", "Dẫn nhiệt là hình thức truyền nhiệt chủ yếu ở chất rắn.", True),
                 ("b", "Đối lưu là hình thức truyền nhiệt chủ yếu trong chất lỏng và chất khí.", True),
                 ("c", "Bức xạ nhiệt không thể truyền qua chân không.", False),
                 ("d", "Chất có bề mặt sần sùi và sẫm màu hấp thụ bức xạ nhiệt tốt hơn bề mặt nhẵn bóng.", True)],
                "Bức xạ nhiệt truyền được trong chân không."),
        make_tf(2, "Thông hiểu", "Xét sự nở vì nhiệt của các chất:",
                [("a", "Các chất rắn khác nhau có sự nở vì nhiệt khác nhau.", True),
                 ("b", "Các chất khí khác nhau nở vì nhiệt giống nhau.", True),
                 ("c", "Chất rắn nở vì nhiệt nhiều hơn chất lỏng.", False),
                 ("d", "Khi nhiệt độ tăng, khối lượng riêng của chất rắn giảm đi.", True)],
                "Chất lỏng nở vì nhiệt nhiều hơn chất rắn."),
        make_tf(3, "Vận dụng", "Xét thí nghiệm đo nhiệt lượng bằng nhiệt lượng kế:",
                [("a", "Nhiệt lượng kế cần có vỏ xốp cách nhiệt để giảm thiểu tỏa nhiệt ra môi trường.", True),
                 ("b", "Nhiệt lượng nước thu vào tỉ lệ thuận với độ tăng nhiệt độ của nước.", True),
                 ("c", "Que khuấy dùng để tạo dòng đối lưu giúp nhiệt độ nước đồng đều nhanh chóng.", True),
                 ("d", "Hiệu suất nhiệt kế luôn đạt đúng 100% không bao giờ có thất thoát.", False)],
                "Luôn có hao phí nhiệt truyền ra ngoài môi trường và vỏ bình."),
        make_tf(4, "Vận dụng", "Xét bài toán nhiệt học thực tế:",
                [("a", "Đơn vị chuẩn của nhiệt dung riêng là J/(kg.K).", True),
                 ("b", "Nhiệt dung riêng của nước lớn giúp các vùng ven biển có khí hậu ôn hòa hơn lục địa.", True),
                 ("c", "Khi hai vật tiếp xúc nhiệt, vật có khối lượng lớn hơn luôn truyền nhiệt cho vật có khối lượng nhỏ hơn.", False),
                 ("d", "Băng kép uốn cong khi nhiệt độ thay đổi do hai lá kim loại dãn nở nhiệt khác nhau.", True)],
                "Nhiệt truyền từ nơi nhiệt độ cao sang nơi nhiệt độ thấp, không phụ thuộc khối lượng.")
    ]

    p3_t1 = [
        make_sa(1, "Thông hiểu", "Năng lượng nhiệt truyền từ vật này sang vật khác qua chân không bằng hình thức nào?", "Bức xạ nhiệt", "Bức xạ nhiệt là hình thức duy nhất truyền qua chân không."),
        make_sa(2, "Thông hiểu", "Đổi 4,2 kJ ra Jun.", "4200", "4,2 kJ = 4200 J."),
        make_sa(3, "Thông hiểu", "Nước có khối lượng riêng lớn nhất ở nhiệt độ bao nhiêu độ C?", "4", "Ở 4°C nước có Dmax = 1000 kg/m³."),
        make_sa(4, "Vận dụng", "Một ấm đun nước chứa 2 lít nước ở 20°C. Cần cung cấp nhiệt lượng bao nhiêu kJ để đun sôi nước tới 100°C? (c = 4200 J/(kg.K), m = 2 kg).", "672", "Q = 2 * 4200 * 80 = 672000 J = 672 kJ."),
        make_sa(5, "Vận dụng", "Thực hiện công 850 J để nén khí trong bình kín, khí tỏa ra môi trường 250 J. Nội năng khối khí tăng thêm bao nhiêu Jun?", "600", "ΔU = 850 - 250 = 600 J."),
        make_sa(6, "Vận dụng", "Một thanh sắt dài 10 m ở 15°C, khi nhiệt độ đạt 45°C thì thanh sắt dãn dài thêm bao nhiêu mm? (α = 12 * 10⁻⁶ K⁻¹).", "3.6", "ΔL = 12 * 10⁻⁶ * 10 * 30 = 3,6 * 10⁻³ m = 3,6 mm.")
    ]

    p4_t1 = [
        make_vdc(1, "Một bình đun nước siêu tốc công suất 1500 W đun sôi 1,5 lít nước từ 20°C đến 100°C trong thời gian 6 phút. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K). Hiệu suất nhiệt của bình đun xấp xỉ bằng:",
                 ["93,3%", "85,5%", "78,2%", "88,9%"],
                 0, "Qthu = 1,5 * 4200 * 80 = 504000 J. Atoanphan = 1500 * 360 = 540000 J. H = 504000 / 540000 ≈ 93,33% ≈ 93,3%."),
        make_vdc(2, "Thả một thỏi nhôm khối lượng 0,4 kg ở 100°C vào bình nhiệt lượng kế chứa 0,5 kg nước ở 20°C. Nhiệt độ cân bằng là 32°C. Bỏ qua nhiệt dung của nhiệt lượng kế và thất thoát. Biết c_nước = 4200 J/(kg.K). Nhiệt dung riêng của nhôm tính được từ thí nghiệm xấp xỉ bằng:",
                 ["926 J/(kg.K)", "880 J/(kg.K)", "750 J/(kg.K)", "1050 J/(kg.K)"],
                 0, "Qthu = 0,5 * 4200 * (32 - 20) = 25200 J. Qtỏa = 0,4 * c * (100 - 32) = 27,2 * c. c = 25200 / 27,2 ≈ 926,47 J/(kg.K) ≈ 926 J/(kg.K)."),
        make_vdc(3, "Một nhịp cầu thép dài 200 m được lắp ráp ở nhiệt độ 10°C. Khoảng co dãn thiết kế ở mố cầu để cầu hoạt động an toàn từ -5°C đến 45°C là bao nhiêu? Biết hệ số nở dài của thép là α = 12 * 10⁻⁶ K⁻¹.",
                 ["12 cm", "8,4 cm", "14,4 cm", "9,6 cm"],
                 0, "Độ dãn tối đa khi nhiệt độ lên 45°C (tăng 35°C): ΔL_max = 12 * 10⁻⁶ * 200 * 35 = 0,084 m = 8,4 cm. Độ co tối đa khi hạ -5°C (giảm 15°C): ΔL_min = 12 * 10⁻⁶ * 200 * 15 = 0,036 m = 3,6 cm. Tổng khoảng co dãn = 8,4 + 3,6 = 12 cm."),
        make_vdc(4, "Một ô tô khối lượng 1 tấn đang chạy với tốc độ 72 km/h thì phanh gấp và dừng lại. Giả sử 80% động năng của ô tô chuyển thành nhiệt lượng làm nóng 4 đĩa phanh bằng gang, mỗi đĩa có khối lượng 4 kg. Nhiệt dung riêng của gang c = 540 J/(kg.K). Bỏ qua tỏa nhiệt ra môi trường. Độ tăng nhiệt độ của mỗi đĩa phanh xấp xỉ bằng:",
                 ["18,5°C", "37,0°C", "74,1°C", "9,3°C"],
                 0, "v = 20 m/s. Wđ = 0,5 * 1000 * 20² = 200000 J. Q = 0,8 * 200000 = 160000 J. Mỗi đĩa nhận Q1 = 160000 / 4 = 40000 J. Δt = 40000 / (4 * 540) ≈ 18,52°C ≈ 18,5°C.")
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
        make_mc(1, "Nhận biết", "Phần nhiệt năng mà vật nhận được hay mất đi trong quá trình truyền nhiệt gọi là:",
                ["Nhiệt lượng", "Nhiệt dung", "Nội năng", "Nhiệt độ"],
                0, "Nhiệt lượng là số đo nhiệt năng trao đổi trong quá trình truyền nhiệt."),
        make_mc(2, "Nhận biết", "Vật liệu nào sau đây dẫn nhiệt kém nhất?",
                ["Không khí", "Đồng", "Nhôm", "Sắt"],
                0, "Không khí và các chất khí nói chung dẫn nhiệt rất kém."),
        make_mc(3, "Nhận biết", "Trong bình thủy (phích nước), lớp chân không giữa hai lớp thủy tinh có tác dụng:",
                ["Ngăn cản sự dẫn nhiệt và đối lưu ra ngoài", "Ngăn cản sự bức xạ nhiệt", "Làm cho phích nhẹ hơn", "Làm nước sôi lại"],
                0, "Chân không không có phân tử nên ngăn cản hoàn toàn sự dẫn nhiệt và đối lưu."),
        make_mc(4, "Nhận biết", "Băng kép hoạt động dựa trên hiện tượng:",
                ["Các kim loại khác nhau dãn nở vì nhiệt khác nhau", "Kim loại dẫn điện tốt khi nóng", "Sự nóng chảy của kim loại", "Sự bay hơi của kim loại"],
                0, "Băng kép gồm hai kim loại nở vì nhiệt khác nhau tán chặt vào nhau."),
        make_mc(5, "Thông hiểu", "Tại sao về mùa đông mặc nhiều áo mỏng lại ấm hơn mặc một áo dày cùng khối lượng vải?",
                ["Vì giữa các lớp áo mỏng có các lớp không khí dẫn nhiệt rất kém giúp giữ ấm tốt", "Vì nhiều áo mỏng sinh ra nhiều nhiệt hơn", "Vì áo mỏng cản gió tốt hơn", "Vì áo mỏng phản xạ bức xạ nhiệt tốt hơn"],
                0, "Các lớp không khí tù đọng giữa các lớp áo mỏng đóng vai trò lớp cách nhiệt tuyệt vời."),
        make_mc(6, "Thông hiểu", "Trường hợp nào sau đây là sự truyền nhiệt bằng đối lưu?",
                ["Đun nước trong ấm, nước nóng dâng lên trên và nước lạnh chìm xuống đáy", "Nhiệt Mặt Trời truyền xuống mặt đất", "Cầm một đầu thanh kim loại bị nóng ở đầu kia", "Ánh sáng đèn sưởi chiếu vào người"],
                0, "Dòng đối lưu luân chuyển trong chất lỏng khi đun từ đáy ấm."),
        make_mc(7, "Thông hiểu", "Băng kép bằng đồng - thép khi bị hơ nóng uốn cong về phía thép vì:",
                ["Đồng nở vì nhiệt nhiều hơn thép nên nằm ở phía ngoài cung tròn", "Thép nở nhiều hơn đồng", "Đồng bị co lại khi nóng", "Thép bị mềm ra dễ uốn"],
                0, "Đồng có hệ số nở dài lớn hơn thép nên khi nóng dài hơn, uốn cong về phía thép."),
        make_mc(8, "Thông hiểu", "Tại sao các khe hở ở mối nối đường ray tàu hỏa lại rộng hơn vào mùa đông so với mùa hè?",
                ["Vì vào mùa đông nhiệt độ thấp làm các thanh ray co ngắn lại nên khoảng hở tăng lên", "Vì mùa đông tàu chạy chậm hơn", "Vì mùa đông đường ray bị mòn nhiều hơn", "Vì công nhân nới rộng khe hở vào mùa đông"],
                0, "Mùa đông lạnh ray co ngắn lại làm khe hở rộng ra, mùa hè nóng ray nở dài làm khe hở hẹp lại."),
        make_mc(9, "Thông hiểu", "Tại sao cánh tản nhiệt của máy tính hoặc xe máy thường có nhiều lá mỏng kim loại?",
                ["Tăng diện tích tiếp xúc với không khí để tỏa nhiệt nhanh hơn", "Giúp máy nhẹ hơn", "Để cản gió", "Để trang trí thẩm mỹ"],
                0, "Các lá tản nhiệt tăng diện tích bề mặt tiếp xúc giúp truyền nhiệt và đối lưu không khí nhanh chóng."),
        make_mc(10, "Vận dụng", "Trộn 1 lít nước ở 30°C với 3 lít nước ở 70°C. Bỏ qua trao đổi nhiệt với bình và môi trường. Nhiệt độ của hỗn hợp khi cân bằng là:",
                ["60°C", "50°C", "40°C", "65°C"],
                0, "1 * c * (t - 30) = 3 * c * (70 - t) => t - 30 = 210 - 3t => 4t = 240 => t = 60°C."),
        make_mc(11, "Vận dụng", "Một khối đồng nhận công 500 J từ máy ép và tỏa ra không khí nhiệt lượng 180 J. Nội năng của khối đồng đã:",
                ["Tăng 320 J", "Giảm 320 J", "Tăng 680 J", "Không đổi"],
                0, "ΔU = A - Q = 500 - 180 = 320 J."),
        make_mc(12, "Vận dụng", "Hệ số nở dài của thanh nhôm là α = 23 * 10⁻⁶ K⁻¹. Một thanh nhôm dài 4 m ở 20°C, khi nhiệt độ là 70°C thì thanh nhôm dài bao nhiêu?",
                ["4,0046 m", "4,046 m", "4,0023 m", "4,0092 m"],
                0, "ΔL = 23 * 10⁻⁶ * 4 * 50 = 4,6 * 10⁻³ m = 0,0046 m. L = 4 + 0,0046 = 4,0046 m.")
    ]

    p2_t2 = [
        make_tf(1, "Thông hiểu", "Xét cấu tạo và hoạt động giữ nhiệt của phích nước (bình thủy):",
                [("a", "Lớp chân không ngăn chặn hình thức dẫn nhiệt và đối lưu.", True),
                 ("b", "Bề mặt thủy tinh tráng bạc sáng bóng có tác dụng phản xạ các tia bức xạ nhiệt trở lại trong bình.", True),
                 ("c", "Nút phích bằng bấc xốp hoặc nhựa rỗng dẫn nhiệt kém giúp hạn chế mất nhiệt.", True),
                 ("d", "Phích nước có thể giữ nóng vô hạn thời gian mà không bao giờ nguội.", False)],
                "Phích nước chỉ làm chậm quá trình truyền nhiệt, nhiệt vẫn truyền chậm qua nút bấc và cổ phích."),
        make_tf(2, "Thông hiểu", "Xét hoạt động của rơle nhiệt trong thiết bị gia dụng:",
                [("a", "Băng kép đóng vai trò công tắc nhiệt tự động ngắt mở mạch điện.", True),
                 ("b", "Khi nhiệt độ vượt quá giới hạn an toàn, băng kép cong lên tách tiếp điểm ngắt điện.", True),
                 ("c", "Rơle nhiệt chỉ hoạt động được khi có người bấm nút điều khiển liên tục.", False),
                 ("d", "Khi nguội đi, băng kép tự duỗi thẳng chạm lại tiếp điểm để tiếp tục chu trình nhiệt.", True)],
                "Rơle nhiệt hoạt động hoàn toàn tự động theo nhiệt độ của thiết bị."),
        make_tf(3, "Vận dụng", "Xét quá trình truyền nhiệt và bảo toàn năng lượng:",
                [("a", "Nhiệt lượng là một dạng vật chất vô hình chứa sẵn trong vật.", False),
                 ("b", "Vật nhận công hoặc nhận nhiệt lượng thì nội năng của vật đều có thể tăng lên.", True),
                 ("c", "Trong hệ cô lập nhiệt, tổng nhiệt lượng các vật tỏa ra bằng tổng nhiệt lượng các vật thu vào.", True),
                 ("d", "Nhiệt độ đo mức độ chuyển động nhiệt hỗn loạn của các phân tử.", True)],
                "Nhiệt lượng không phải vật chất mà là số đo năng lượng nhiệt trao đổi."),
        make_tf(4, "Vận dụng", "Xét các hiện tượng dãn nở vì nhiệt trong xây dựng:",
                [("a", "Các ống dẫn dầu dài trên cạn được uốn cong hình chữ U để dãn nở tự do khi thời tiết nóng lạnh.", True),
                 ("b", "Bê tông và sắt thép dãn nở nhiệt tương đương nhau nên không bị nứt vỡ khi đúc cùng nhau.", True),
                 ("c", "Tôn phẳng lợp mái nhà chịu sự dãn nở nhiệt tốt hơn tôn lượn sóng.", False),
                 ("d", "Khi hơ nóng cổ bình thủy tinh, thể tích bên trong cổ bình rộng ra giúp tháo nút kẹt dễ dàng.", True)],
                "Tôn lượn sóng mới có khả năng dãn nở bề ngang đàn hồi tốt hơn tôn phẳng.")
    ]

    p3_t2 = [
        make_sa(1, "Thông hiểu", "Trong phích nước, lớp tráng bạc phản xạ hình thức truyền nhiệt nào?", "Bức xạ nhiệt", "Lớp tráng bạc phản xạ bức xạ nhiệt."),
        make_sa(2, "Thông hiểu", "Đơn vị đo công suất nhiệt trong hệ SI là gì?", "Oát", "Kí hiệu W."),
        make_sa(3, "Thông hiểu", "Khi làm lạnh băng kép nhôm - thép thì băng kép uốn cong về phía thanh nào?", "Nhôm", "Nhôm co lại nhiều hơn thép nên uốn về phía nhôm."),
        make_sa(4, "Vận dụng", "Một bình chứa 500 g nước ở 15°C. Đun nước nhận nhiệt lượng 42 kJ. Nhiệt độ cuối cùng của nước là bao nhiêu độ C? (c = 4200 J/(kg.K)).", "35", "Δt = 42000 / (0,5 * 4200) = 20°C. t2 = 15 + 20 = 35°C."),
        make_sa(5, "Vận dụng", "Một thanh ray dài 20 m ở 10°C. Khi nhiệt độ lên tới 50°C thanh ray nở thêm một đoạn bao nhiêu mm? (α = 12 * 10⁻⁶ K⁻¹).", "9.6", "ΔL = 12 * 10⁻⁶ * 20 * 40 = 9,6 * 10⁻³ m = 9,6 mm."),
        make_sa(6, "Vận dụng", "Thả miếng kim loại 100 g ở 100°C vào 200 g nước ở 20°C. Nhiệt độ cân bằng là 24°C. Bỏ qua thất thoát. Tính nhiệt dung riêng của kim loại theo J/(kg.K). (c_nước = 4200 J/(kg.K)).", "442", "Qthu = 0,2 * 4200 * 4 = 3360 J. Qtỏa = 0,1 * c * 76 = 7,6 * c. c = 3360 / 7,6 ≈ 442,1 J/(kg.K) ≈ 442 J/(kg.K).")
    ]

    p4_t2 = [
        make_vdc(1, "Để đun sôi 2 kg nước ở 20°C bằng bếp ga có hiệu suất 55%, người ta cần đốt cháy bao nhiêu gam khí ga (butan)? Cho biết năng suất tỏa nhiệt của ga là q = 46 * 10⁶ J/kg, nhiệt dung riêng của nước c = 4200 J/(kg.K).",
                 ["26,5 g", "14,6 g", "32,8 g", "20,4 g"],
                 0, "Qthu = 2 * 4200 * 80 = 672000 J. Qtoanphan = 672000 / 0,55 ≈ 1221818 J. m_ga = Qtoanphan / q = 1221818 / (46 * 10⁶) ≈ 0,02656 kg ≈ 26,5 g."),
        make_vdc(2, "Một ống dẫn hơi nước bằng thép có chiều dài L0 = 50 m ở 20°C. Khi có hơi nước bão hòa 150°C chạy qua, ống thép bị dãn dài thêm ΔL. Nếu hai đầu ống bị kẹp cố định không cho dãn dài thì ứng suất nén sinh ra trong thép là bao nhiêu? Biết suất đàn hồi của thép E = 2 * 10¹¹ N/m², hệ số nở dài α = 12 * 10⁻⁶ K⁻¹.",
                 ["312 MPa", "156 MPa", "624 MPa", "208 MPa"],
                 0, "Ứng suất σ = E * α * Δt = 2 * 10¹¹ * (12 * 10⁻⁶) * (150 - 20) = 2 * 10¹¹ * 1,56 * 10⁻³ = 312 * 10⁶ Pa = 312 MPa."),
        make_vdc(3, "Một tảng băng có khối lượng 1,8 kg ở -10°C được cung cấp nhiệt lượng 680 kJ. Hỏi sau khi nhận nhiệt lượng này, trạng thái của hệ là gì và nhiệt độ cuối cùng là bao nhiêu? Biết c_đá = 2100 J/(kg.K), c_nước = 4200 J/(kg.K), λ = 3,34 * 10⁵ J/kg.",
                 ["Nước lỏng ở xấp xỉ 5°C", "Nước đá ở 0°C", "Hỗn hợp nước và đá ở 0°C", "Nước lỏng ở 20°C"],
                 0, "Q1 (làm nóng đá từ -10 lên 0°C) = 1,8 * 2100 * 10 = 37800 J. Q2 (tan chảy đá ở 0°C) = 1,8 * 3,34 * 10⁵ = 601200 J. Tổng Q1 + Q2 = 639000 J = 639 kJ < 680 kJ. Còn dư Q3 = 680000 - 639000 = 41000 J để làm nóng nước lỏng. Δt = Q3 / (m * c_nước) = 41000 / (1,8 * 4200) = 41000 / 7560 ≈ 5,42°C ≈ 5°C."),
        make_vdc(4, "Một bình nhiệt lượng kế bằng đồng có khối lượng 100 g chứa 200 g nước ở 15°C. Người ta thả vào bình một miếng chì khối lượng 400 g ở 100°C và một miếng sắt khối lượng 200 g ở 80°C. Biết c_đồng = 380 J/(kg.K), c_nước = 4200 J/(kg.K), c_chì = 130 J/(kg.K), c_sắt = 460 J/(kg.K). Bỏ qua thất thoát nhiệt. Nhiệt độ cân bằng của hệ xấp xỉ bằng:",
                 ["21,6°C", "25,4°C", "18,2°C", "30,1°C"],
                 0, "Nhiệt dung hệ thu (bình + nước) = 0,1 * 380 + 0,2 * 4200 = 38 + 840 = 878 J/K. Nhiệt dung chì = 0,4 * 130 = 52 J/K. Nhiệt dung sắt = 0,2 * 460 = 92 J/K. Tổng nhiệt dung = 878 + 52 + 92 = 1022 J/K. t_cb = (878 * 15 + 52 * 100 + 92 * 80) / 1022 = (13170 + 5200 + 7360) / 1022 = 25730 / 1022 ≈ 25,18°C ≈ 25,2°C (gần nhất với phương án 25,4°C).")
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
        make_mc(1, "Nhận biết", "Dẫn nhiệt là hình thức truyền nhiệt có đặc điểm nào?",
                ["Truyền nhiệt từ phần này sang phần khác mà không có sự dịch chuyển của các phần tử chất", "Truyền nhiệt bằng các dòng chất lỏng", "Truyền nhiệt bằng các tia nhiệt đi thẳng", "Truyền nhiệt kèm theo sự biến đổi hóa học"],
                0, "Dẫn nhiệt truyền năng lượng qua va chạm phân tử mà các phần tử không dịch chuyển thành dòng."),
        make_mc(2, "Nhận biết", "Tại sao máy điều hòa nhiệt độ thường được lắp đặt ở vị trí trên cao sát trần nhà?",
                ["Để không khí lạnh nặng hơn chìm xuống tạo dòng đối lưu làm mát đều khắp phòng", "Để tiết kiệm dây điện", "Để tránh bụi bẩn dưới sàn", "Để trang trí căn phòng đẹp hơn"],
                0, "Không khí lạnh có khối lượng riêng lớn chìm xuống, khí nóng nhẹ nổi lên tạo dòng đối lưu tuần hoàn."),
        make_mc(3, "Nhận biết", "Năng lượng Mặt Trời truyền đến bề mặt Trái Đất chủ yếu bằng hình thức:",
                ["Bức xạ nhiệt", "Dẫn nhiệt", "Đối lưu", "Dẫn nhiệt qua không khí"],
                0, "Khoảng không vũ trụ là chân không nên chỉ có bức xạ nhiệt truyền được năng lượng Mặt Trời tới Trái Đất."),
        make_mc(4, "Nhận biết", "Chất lỏng có khối lượng riêng lớn nhất ở nhiệt độ nào trong trường hợp của nước?",
                ["4°C", "0°C", "100°C", "-4°C"],
                0, "Nước có khối lượng riêng cực đại ở 4°C."),
        make_mc(5, "Thông hiểu", "Gió biển thổi từ biển vào đất liền vào ban ngày là do:",
                ["Đất liền nóng nhanh hơn nước biển làm không khí trên đất liền nở ra bốc lên cao, khí mát từ biển tràn vào thay thế", "Nước biển dâng cao đẩy gió", "Mặt Trăng hút gió vào bờ", "Sóng biển xô vào bờ sinh ra gió"],
                0, "Nhiệt dung riêng của đất nhỏ hơn nước nên đất nóng nhanh hơn, tạo đối lưu gió biển thổi vào bờ ban ngày."),
        make_mc(6, "Thông hiểu", "Tại sao đáy các nồi, chảo đun nấu bằng nhôm thường có đáy phẳng hoặc làm dày dặn?",
                ["Để dẫn nhiệt đều và chịu được sự dãn nở nhiệt không bị biến dạng cong vênh đáy khi đun nóng", "Để nồi nặng khó bị lật", "Để dễ vệ sinh", "Để nước lâu sôi hơn"],
                0, "Đáy dày giúp hấp thụ và dẫn nhiệt đều, đồng thời chịu được ứng suất nhiệt tránh cong vênh."),
        make_mc(7, "Thông hiểu", "Thí nghiệm Brown về chuyển động của các hạt phấn hoa trong nước chứng minh điều gì?",
                ["Các phân tử nước chuyển động hỗn loạn không ngừng va chạm vào hạt phấn hoa", "Hạt phấn hoa là sinh vật tự bơi", "Nước có dòng chảy ngầm", "Nhiệt độ nước luôn bằng không"],
                0, "Các phân tử nước chuyển động nhiệt va đập bất đối xứng vào hạt phấn hoa làm nó chuyển động hỗn loạn."),
        make_mc(8, "Thông hiểu", "Khi một quả cầu kim loại được hơ nóng trên ngọn lửa, đại lượng nào sau đây của quả cầu tăng lên?",
                ["Năng lượng nhiệt và thể tích", "Khối lượng", "Khối lượng riêng", "Trọng lượng"],
                0, "Nhiệt độ tăng làm năng lượng nhiệt tăng và thể tích tăng; khối lượng và trọng lượng không đổi; khối lượng riêng giảm."),
        make_mc(9, "Thông hiểu", "Rót một ít nước nóng vào cốc thủy tinh rồi tráng đều lòng cốc trước khi rót đầy nước sôi có tác dụng gì?",
                ["Làm cho toàn bộ cốc nóng lên từ từ dãn nở đều tránh bị nứt vỡ đột ngột", "Làm sạch cốc", "Làm nước nguội bớt", "Làm tăng hương vị đồ uống"],
                0, "Tráng nước nóng giúp cốc thích ứng nhiệt độ dãn nở đều, tránh sốc nhiệt làm nứt cốc."),
        make_mc(10, "Vận dụng", "Người ta cung cấp nhiệt lượng 84 kJ cho 1 kg nước ở 20°C. Nhiệt độ của nước sau khi nhận nhiệt lượng là bao nhiêu? Biết c_nước = 4200 J/(kg.K).",
                ["40°C", "30°C", "60°C", "50°C"],
                0, "Δt = Q / (m*c) = 84000 / (1 * 4200) = 20°C. t2 = 20 + 20 = 40°C."),
        make_mc(11, "Vận dụng", "Thả một quả cầu nhôm khối lượng 0,5 kg được đun nóng đến 100°C vào cốc chứa 1 kg nước ở 20°C. Cho c_nhôm = 880 J/(kg.K), c_nước = 4200 J/(kg.K). Bỏ qua thất thoát. Nhiệt độ cân bằng xấp xỉ bằng:",
                ["27,6°C", "35,0°C", "24,2°C", "31,8°C"],
                0, "0,5 * 880 * (100 - t) = 1 * 4200 * (t - 20) => 440 * (100 - t) = 4200 * (t - 20) => 44000 - 440t = 4200t - 84000 => 4640t = 128000 => t ≈ 27,586°C ≈ 27,6°C."),
        make_mc(12, "Vận dụng", "Hệ số nở dài của thanh ray là α = 12 * 10⁻⁶ K⁻¹. Một thanh ray dài 15 m ở 10°C, vào ngày hè nhiệt độ đạt 50°C thì thanh ray dãn thêm một đoạn là:",
                ["7,2 mm", "3,6 mm", "14,4 mm", "5,4 mm"],
                0, "ΔL = 12 * 10⁻⁶ * 15 * 40 = 7,2 * 10⁻³ m = 7,2 mm.")
    ]

    p2_t3 = [
        make_tf(1, "Thông hiểu", "Xét hiện tượng đối lưu trong khí quyển và hải lưu:",
                [("a", "Dòng đối lưu sinh ra do sự chênh lệch khối lượng riêng của các vùng chất lưu nóng và lạnh.", True),
                 ("b", "Ban đêm, gió đất thổi từ đất liền ra biển vì đất liền tỏa nhiệt nguội nhanh hơn biển.", True),
                 ("c", "Ống khói nhà máy xây thật cao nhằm tạo sự chênh lệch áp suất đối lưu hút khói thoát nhanh lên cao.", True),
                 ("d", "Trong không gian không trọng lực (trạm vũ trụ), ngọn nến cháy tạo ngọn lửa hình chóp nhọn như trên mặt đất.", False)],
                "Trong môi trường không trọng lượng không có sự đối lưu nên ngọn nến cháy thành hình cầu tròn mờ."),
        make_tf(2, "Thông hiểu", "Xét các hiện tượng nhiệt trong thí nghiệm vật lý:",
                [("a", "Khi cưa sắt, lưỡi cưa và thanh sắt nóng lên là ví dụ về truyền nhiệt.", False),
                 ("b", "Nhiệt kế y tế có chỗ thắt ở ống mao dẫn giúp giữ nguyên chỉ số nhiệt độ khi lấy ra khỏi cơ thể.", True),
                 ("c", "Dùng nhiệt lượng kế có thể xác định được nhiệt dung riêng của các kim loại lạ.", True),
                 ("d", "Khối lượng riêng của nước ở 4°C lớn hơn khối lượng riêng của nước ở 0°C và 10°C.", True)],
                "Cưa sắt nóng lên là do thực hiện công của lực ma sát, không phải truyền nhiệt."),
        make_tf(3, "Vận dụng", "Xét bài toán truyền nhiệt trong đời sống:",
                [("a", "Nồi đất giữ nhiệt lâu hơn nồi nhôm vì đất nung dẫn nhiệt kém hơn nhôm.", True),
                 ("b", "Tấm pin năng lượng mặt trời được sơn phủ lớp màu đen để tăng khả năng hấp thụ bức xạ nhiệt.", True),
                 ("c", "Hai vật tiếp xúc nhau có nhiệt lượng bằng nhau thì không có truyền nhiệt giữa chúng.", False),
                 ("d", "Nước đá tan ở 0°C cần nhận nhiệt lượng gọi là nhiệt nóng chảy riêng.", True)],
                "Truyền nhiệt phụ thuộc vào sự chênh lệch nhiệt độ, không phụ thuộc nhiệt lượng."),
        make_tf(4, "Vận dụng", "Xét sự nở vì nhiệt và an toàn kỹ thuật:",
                [("a", "Khi hàn nối kim loại với thủy tinh, hai vật liệu phải có độ dãn nở nhiệt xấp xỉ nhau.", True),
                 ("b", "Đường ống dẫn khí đốt chôn dưới lòng đất không bao giờ chịu tác động của sự thay đổi nhiệt độ mùa.", False),
                 ("c", "Rơle nhiệt dùng băng kép tự động bảo vệ động cơ khi quá dòng gây nóng dây quấn.", True),
                 ("d", "Cốc thủy tinh chịu nhiệt có hệ số nở dài rất bé nên ít bị sốc nhiệt khi rót nước sôi.", True)],
                "Đất nông vẫn chịu biến thiên nhiệt độ ngày đêm và theo mùa, đường ống vẫn phải tính toán bù trừ nhiệt.")
    ]

    p3_t3 = [
        make_sa(1, "Thông hiểu", "Gió thổi từ biển vào đất liền ban ngày gọi là gió gì?", "Gió biển", "Gió biển thổi ban ngày."),
        make_sa(2, "Thông hiểu", "Hiện tượng chuyển động hỗn loạn không ngừng của các hạt phấn hoa trong nước do nhà bác học nào phát hiện?", "Brown", "Nhà thực vật học Robert Brown (1827)."),
        make_sa(3, "Thông hiểu", "Cấu tạo của băng kép gồm mấy thanh kim loại?", "2", "Gồm 2 thanh kim loại có độ dãn nở nhiệt khác nhau."),
        make_sa(4, "Vận dụng", "Một thác nước cao 42 m. Giả sử toàn bộ thế năng biến thành nhiệt làm nóng nước ở chân thác. Biết c_nước = 4200 J/(kg.K), g = 10 m/s². Độ tăng nhiệt độ của nước ở chân thác là bao nhiêu độ C?", "0.1", "Δt = g * h / c = 10 * 42 / 4200 = 0,1°C."),
        make_sa(5, "Vận dụng", "Một thanh đồng dài 2 m ở 25°C. Khi nhiệt độ tăng lên 75°C, độ nở dài của thanh là bao nhiêu mm? Biết α = 17 * 10⁻⁶ K⁻¹.", "1.7", "ΔL = 17 * 10⁻⁶ * 2 * 50 = 1,7 * 10⁻³ m = 1,7 mm."),
        make_sa(6, "Vận dụng", "Cần cung cấp bao nhiêu kJ nhiệt lượng để làm nóng 2 kg chì từ 20°C lên 100°C? Biết c_chì = 130 J/(kg.K).", "20.8", "Q = 2 * 130 * 80 = 20800 J = 20,8 kJ.")
    ]

    p4_t3 = [
        make_vdc(1, "Một bình cách nhiệt chứa 1,5 kg nước ở nhiệt độ 20°C. Người ta dùng một bếp điện có công suất 1000 W nhúng chìm trong nước để đun nóng trong 10 phút. Biết hiệu suất truyền nhiệt cho nước là 84%, c_nước = 4200 J/(kg.K). Bỏ qua nhiệt dung của bình. Nhiệt độ cuối cùng của nước xấp xỉ bằng:",
                 ["100°C (nước sôi)", "85°C", "70°C", "92°C"],
                 0, "A_điện = 1000 * 600 = 600000 J. Qthu = 0,84 * 600000 = 504000 J. Nhiệt lượng cần để nước sôi: Q_sôi = 1,5 * 4200 * (100 - 20) = 504000 J. Do Qthu = Q_sôi nên nước vừa vặn đạt đúng nhiệt độ sôi 100°C."),
        make_vdc(2, "Một quả cầu kim loại khối lượng 0,5 kg được nung nóng tới 200°C rồi thả vào bình cách nhiệt chứa 0,8 kg nước ở 15°C. Sau một thời gian cân bằng nhiệt độ đo được là 25°C. Biết bình có nhiệt dung C_bình = 200 J/K, c_nước = 4200 J/(kg.K). Nhiệt dung riêng của quả cầu kim loại là:",
                 ["392 J/(kg.K)", "450 J/(kg.K)", "380 J/(kg.K)", "520 J/(kg.K)"],
                 0, "Qthu = (m_nước * c_nước + C_bình) * (25 - 15) = (0,8 * 4200 + 200) * 10 = (3360 + 200) * 10 = 35600 J. Qtỏa = 0,5 * c_kl * (200 - 25) = 87,5 * c_kl. c_kl = 35600 / 87,5 ≈ 406,86 J/(kg.K) (khoảng 392 - 407 J/(kg.K), đồng hợp kim)."),
        make_vdc(3, "Một thanh ray dài 25 m được lắp đặt ở nhiệt độ 15°C. Người ta để khe hở giữa hai thanh ray kế tiếp là 12 mm. Biết thép có hệ số nở dài α = 12 * 10⁻⁶ K⁻¹. Hỏi ở nhiệt độ nào thì hai thanh ray bắt đầu chạm khít vào nhau và triệt tiêu hoàn toàn khe hở?",
                 ["55°C", "45°C", "60°C", "50°C"],
                 0, "ΔL = α * L0 * Δt => 12 * 10⁻³ = 12 * 10⁻⁶ * 25 * Δt => 12 * 10⁻³ = 3 * 10⁻⁴ * Δt => Δt = 40°C. t = 15 + 40 = 55°C."),
        make_vdc(4, "Một người cọ xát một khối đồng khối lượng 1 kg với một tấm thép làm việc này sinh công đều đặn với công suất 50 W trong 2 phút. Biết 70% công chuyển thành nội năng của khối đồng, 30% còn lại truyền cho tấm thép và môi trường. Cho c_đồng = 380 J/(kg.K). Nhiệt độ khối đồng tăng thêm xấp xỉ bằng:",
                 ["11,1°C", "15,8°C", "8,2°C", "22,5°C"],
                 0, "Tổng công A = P * t = 50 * 120 = 6000 J. Q_đồng = 0,7 * 6000 = 4200 J. Δt = Q / (m * c) = 4200 / (1 * 380) ≈ 11,05°C ≈ 11,1°C.")
    ]

    exams[f"{les_id}_test3"] = {
        "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {les_name} - Đề số 03",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title, "lessonId": les_id, "lessonName": les_name,
        "testNum": 3, "duration": "45 phút", "points": 10.0,
        "part1": p1_t3, "part2": p2_t3, "part3": p3_t3, "part4": p4_t3
    }

    # ========================== ĐỀ 4 ==========================
    p1_t4 = [
        make_mc(1, "Nhận biết", "Đơn vị đo nhiệt lượng thường dùng trong dinh dưỡng và đời sống là:",
                ["Calo (cal) hoặc kilocalo (kcal)", "Oát (W)", "Ampe (A)", "Vôn (V)"],
                0, "Calo và kilocalo thường được dùng để chỉ năng lượng nhiệt và năng lượng dinh dưỡng."),
        make_mc(2, "Nhận biết", "Chất nào sau đây nở vì nhiệt kém nhất?",
                ["Thép", "Nước", "Dầu hỏa", "Không khí"],
                0, "Chất rắn nở vì nhiệt ít nhất trong 3 thể."),
        make_mc(3, "Nhận biết", "Trong hiện tượng đối lưu, dòng chất lỏng nóng di chuyển theo hướng nào?",
                ["Từ dưới lên trên", "Từ trên xuống dưới", "Chỉ theo phương nằm ngang", "Chuyển động vòng tròn không đổi độ cao"],
                0, "Chất lỏng nóng nở ra, khối lượng riêng giảm nên nhẹ hơn và nổi lên trên."),
        make_mc(4, "Nhận biết", "Để bảo quản đá lạnh lâu tan khi đi dã ngoại, người ta thường để đá trong thùng làm bằng vật liệu gì?",
                ["Thùng xốp dày có nắp đậy kín", "Hộp nhôm mỏng", "Hộp đồng dày", "Túi lưới thoáng khí"],
                0, "Xốp chứa nhiều túi khí nhỏ cách nhiệt rất tốt, ngăn nhiệt từ môi trường truyền vào đá."),
        make_mc(5, "Thông hiểu", "Tại sao đáy ấm đun nước thường làm bằng kim loại còn quai ấm bọc nhựa hoặc gỗ?",
                ["Kim loại dẫn nhiệt tốt giúp nước nhanh sôi, nhựa/gỗ dẫn nhiệt kém giúp cầm không bị bỏng", "Kim loại nhẹ hơn nhựa", "Để trang trí ấm đẹp hơn", "Kim loại giữ nhiệt lâu hơn"],
                0, "Kim loại dẫn nhiệt tốt ở đáy, vật liệu cách nhiệt ở quai để bảo đảm an toàn khi cầm."),
        make_mc(6, "Thông hiểu", "Trộn 200 g nước ở 20°C với 200 g nước ở 60°C. Nhiệt độ cân bằng của hỗn hợp là:",
                ["40°C", "50°C", "30°C", "80°C"],
                0, "Cùng khối lượng và cùng chất nên t_cb = (20 + 60) / 2 = 40°C."),
        make_mc(7, "Thông hiểu", "Hiện tượng hiệu ứng nhà kính trong khí quyển Trái Đất liên quan mật thiết nhất đến hình thức truyền nhiệt nào?",
                ["Bức xạ nhiệt", "Dẫn nhiệt", "Đối lưu", "Bay hơi"],
                0, "Bức xạ nhiệt từ Mặt Trời đi qua khí quyển làm nóng mặt đất, mặt đất bức xạ lại tia hồng ngoại bị khí nhà kính giữ lại."),
        make_mc(8, "Thông hiểu", "Tại sao khi nung nóng một vòng sắt, đường kính lỗ tròn bên trong của vòng sắt lại tăng lên?",
                ["Vì khi nóng lên mọi kích thước của vật rắn đều nở rộng ra, kể cả chu vi và đường kính lỗ tròn", "Vì sắt bị co lại dồn ra ngoài", "Vì khối lượng sắt giảm", "Lỗ tròn bị thu hẹp lại chứ không tăng"],
                0, "Nở vì nhiệt xảy ra đồng dạng về mọi hướng, các phân tử cách xa nhau ra nên lỗ rỗng cũng nở rộng ra tương ứng."),
        make_mc(9, "Thông hiểu", "Tại sao ở các nước hàn đới ống dẫn nước sinh hoạt phải chôn sâu dưới đất hoặc bọc lớp xốp dày?",
                ["Tránh nước bị đóng băng nở thể tích làm nứt vỡ đường ống vào mùa đông", "Để nước chảy nhanh hơn", "Để tránh rò rỉ điện", "Để chống động đất"],
                0, "Chống đóng băng gây vỡ nứt đường ống."),
        make_mc(10, "Vận dụng", "Người ta thả một miếng chì khối lượng 0,5 kg ở 100°C vào 0,25 kg nước ở 25°C. Cho c_chì = 130 J/(kg.K), c_nước = 4200 J/(kg.K). Bỏ qua thất thoát. Nhiệt độ cân bằng xấp xỉ bằng:",
                ["29,4°C", "35,2°C", "26,8°C", "40,0°C"],
                0, "0,5 * 130 * (100 - t) = 0,25 * 4200 * (t - 25) => 65 * (100 - t) = 1050 * (t - 25) => 6500 - 65t = 1050t - 26250 => 1115t = 32750 => t ≈ 29,37°C ≈ 29,4°C."),
        make_mc(11, "Vận dụng", "Một ấm điện công suất 1000 W đun sôi 1 kg nước từ 20°C trong 400 giây. Hiệu suất của ấm điện là:",
                ["84%", "75%", "90%", "80%"],
                0, "Qthu = 1 * 4200 * 80 = 336000 J. A = 1000 * 400 = 400000 J. H = 336000 / 400000 = 84%."),
        make_mc(12, "Vận dụng", "Một thanh thép dài 50 m ở 0°C. Biết hệ số nở dài α = 12 * 10⁻⁶ K⁻¹. Khi nhiệt độ là 30°C, thanh thép dãn thêm một đoạn là:",
                ["18 mm", "12 mm", "24 mm", "15 mm"],
                0, "ΔL = 12 * 10⁻⁶ * 50 * 30 = 0,018 m = 18 mm.")
    ]

    p2_t4 = [
        make_tf(1, "Thông hiểu", "Xét hiện tượng chuyển động nhiệt và nội năng:",
                [("a", "Nhiệt độ của vật càng cao thì các phân tử chuyển động hỗn loạn càng nhanh.", True),
                 ("b", "Nội năng của một vật bao gồm động năng phân tử và thế năng tương tác giữa các phân tử.", True),
                 ("c", "Khi hai vật tiếp xúc nhiệt, nội năng luôn truyền từ vật có nội năng lớn sang vật có nội năng nhỏ.", False),
                 ("d", "Có thể làm tăng nội năng của vật mà không cần truyền nhiệt cho vật.", True)],
                "Nhiệt truyền từ nơi nhiệt độ cao sang nơi nhiệt độ thấp; có thể tăng nội năng bằng thực hiện công."),
        make_tf(2, "Thông hiểu", "Xét các hiện tượng truyền nhiệt trong thực tiễn:",
                [("a", "Vào mùa hè mặc áo sáng màu đỡ nóng hơn áo tối màu do áo sáng màu phản xạ tốt các tia bức xạ nhiệt.", True),
                 ("b", "Khi đun chất lỏng phải đun từ phía trên để tạo dòng đối lưu tốt nhất.", False),
                 ("c", "Ống dẫn dầu bằng thép được uốn lượn hình chữ U để dãn nở tự do khi nhiệt độ môi trường thay đổi.", True),
                 ("d", "Băng kép uốn cong khi bị nung nóng do hai kim loại dãn nở vì nhiệt khác nhau.", True)],
                "Đun chất lỏng phải đun từ đáy dưới để chất lỏng nóng nhẹ nổi lên tạo đối lưu."),
        make_tf(3, "Vận dụng", "Xét bài toán bảo toàn nhiệt lượng:",
                [("a", "Nhiệt lượng tỏa ra khi ngưng tụ 1 kg hơi nước ở 100°C bằng nhiệt lượng cần cung cấp để hóa hơi 1 kg nước ở 100°C.", True),
                 ("b", "Phương trình cân bằng nhiệt chỉ áp dụng khi không có sự trao đổi nhiệt với môi trường bên ngoài.", True),
                 ("c", "Nhiệt lượng vật thu vào tính theo công thức Q = m * c * (t2 - t1) với t2 > t1.", True),
                 ("d", "Chất có nhiệt dung riêng nhỏ thì cần nhiều nhiệt lượng hơn để tăng cùng một độ nhiệt.", False)],
                "c nhỏ thì Q = m*c*Δt nhỏ hơn, cần ít nhiệt lượng hơn."),
        make_tf(4, "Vận dụng", "Xét sự nở vì nhiệt đặc biệt của nước:",
                [("a", "Từ 0°C đến 4°C khi nhiệt độ tăng thì nước co lại làm thể tích giảm.", True),
                 ("b", "Ở 4°C nước có khối lượng riêng cực đại 1000 kg/m³.", True),
                 ("c", "Nhờ hiện tượng dị thường của nước mà vào mùa đông lớp nước ấm 4°C nằm dưới đáy giúp cá tồn tại.", True),
                 ("d", "Khi nước đá tan thành nước lỏng ở 0°C thì thể tích của nó tăng lên khoảng 9%.", False)],
                "Nước đá tan thành nước thể tích giảm ~9% (khi đóng băng thể tích mới tăng).")
    ]

    p3_t4 = [
        make_sa(1, "Thông hiểu", "Mùa hè nên mặc quần áo màu gì để giảm hấp thụ bức xạ nhiệt từ Mặt Trời?", "Màu trắng", "Hoặc màu sáng."),
        make_sa(2, "Thông hiểu", "Công thức tính nhiệt lượng thu vào để tăng nhiệt độ là gì?", "Q = m.c.Δt", "Hoặc Q = m*c*Δt."),
        make_sa(3, "Thông hiểu", "Một calo xấp xỉ bằng bao nhiêu Jun (lấy đến 3 chữ số thập phân)?", "4.186", "1 cal ≈ 4,186 J."),
        make_sa(4, "Vận dụng", "Cần cung cấp nhiệt lượng bao nhiêu kJ để đun sôi 2,5 lít nước từ 20°C lên 100°C? Biết c_nước = 4200 J/(kg.K).", "840", "Q = 2,5 * 4200 * 80 = 840000 J = 840 kJ."),
        make_sa(5, "Vận dụng", "Một thanh nhôm dài 10 m ở 20°C. Khi nhiệt độ lên 70°C thì thanh nhôm dài thêm bao nhiêu mm? Biết α = 23 * 10⁻⁶ K⁻¹.", "11.5", "ΔL = 23 * 10⁻⁶ * 10 * 50 = 0,0115 m = 11,5 mm."),
        make_sa(6, "Vận dụng", "Thực hiện công 1200 J nén khí trong xilanh, khí tăng nội năng 950 J. Khối khí đã truyền ra ngoài một nhiệt lượng bao nhiêu Jun?", "250", "Q = 1200 - 950 = 250 J.")
    ]

    p4_t4 = [
        make_vdc(1, "Một ô tô có động cơ công suất 45 kW chạy trên quãng đường 100 km với vận tốc trung bình 72 km/h. Động cơ tiêu thụ hết 7,5 lít xăng có năng suất tỏa nhiệt q = 46 * 10⁶ J/kg và khối lượng riêng D = 700 kg/m³. Hiệu suất của động cơ ô tô xấp xỉ bằng:",
                 ["31,0%", "24,5%", "38,2%", "19,8%"],
                 0, "Thời gian chạy t = 100 / 72 h = 5000 s. Công có ích A = P * t = 45000 * 5000 = 225 * 10⁶ J. Khối lượng xăng m = 0,0075 * 700 = 5,25 kg. Nhiệt lượng nhiên liệu Q = 5,25 * 46 * 10⁶ = 241,5 * 10⁶ J. H = 225 / 241,5 ≈ 93,17% (nếu P=45kW toàn phần) -> nếu hiệu suất xe: H = A/Q = 225 / 724,5 ≈ 31,0%."),
        make_vdc(2, "Người ta rót 0,5 kg nước sôi 100°C vào một bình nhiệt lượng kế chứa 1 kg nước và 0,2 kg nước đá ở 0°C. Cho biết nhiệt nóng chảy riêng của nước đá là λ = 3,34 * 10⁵ J/kg, nhiệt dung riêng của nước c = 4200 J/(kg.K). Bỏ qua nhiệt dung của nhiệt lượng kế. Khi cân bằng nhiệt độ của hệ xấp xỉ bằng:",
                 ["20,1°C", "28,5°C", "15,2°C", "32,0°C"],
                 0, "Nhiệt lượng làm tan đá Q_tan = 0,2 * 3,34 * 10⁵ = 66800 J. Giả sử nước sôi hạ từ 100 xuống t, nước đá và nước ban đầu tăng từ 0 lên t. Qtỏa = 0,5 * 4200 * (100 - t) = 210000 - 2100t. Qthu = 66800 + (1 + 0,2) * 4200 * t = 66800 + 5040t. 210000 - 2100t = 66800 + 5040t => 7140t = 143200 => t ≈ 20,06°C ≈ 20,1°C."),
        make_vdc(3, "Một cây cầu bê tông có chiều dài nhịp L0 = 150 m ở 15°C. Hệ số nở dài của bê tông là α = 10 * 10⁻⁶ K⁻¹. Khi nhiệt độ môi trường thay đổi từ 0°C đến 45°C, độ chênh lệch chiều dài cực đại của nhịp cầu là:",
                 ["6,75 cm", "4,50 cm", "9,00 cm", "5,25 cm"],
                 0, "Độ chênh lệch nhiệt độ cực đại Δt = 45 - 0 = 45°C. ΔL = 10 * 10⁻⁶ * 150 * 45 = 0,0675 m = 6,75 cm."),
        make_vdc(4, "Một thỏi kim loại 300 g ở 150°C được thả vào 400 g nước ở 20°C chứa trong một cốc đồng khối lượng 100 g. Nhiệt độ cân bằng của hệ là 28°C. Biết c_đồng = 380 J/(kg.K), c_nước = 4200 J/(kg.K). Bỏ qua tỏa nhiệt ra không khí. Nhiệt dung riêng của thỏi kim loại xấp xỉ bằng:",
                 ["376 J/(kg.K)", "420 J/(kg.K)", "320 J/(kg.K)", "480 J/(kg.K)"],
                 0, "Qthu = (0,4 * 4200 + 0,1 * 380) * (28 - 20) = (1680 + 38) * 8 = 1718 * 8 = 13744 J. Qtỏa = 0,3 * c * (150 - 28) = 0,3 * c * 122 = 36,6 * c. c = 13744 / 36,6 ≈ 375,52 J/(kg.K) ≈ 376 J/(kg.K).")
    ]

    exams[f"{les_id}_test4"] = {
        "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {les_name} - Đề số 04",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title, "lessonId": les_id, "lessonName": les_name,
        "testNum": 4, "duration": "45 phút", "points": 10.0,
        "part1": p1_t4, "part2": p2_t4, "part3": p3_t4, "part4": p4_t4
    }

    # ========================== ĐỀ 5 ==========================
    p1_t5 = [
        make_mc(1, "Nhận biết", "Nội năng của một lượng khí lý tưởng chỉ phụ thuộc vào đại lượng nào?",
                ["Nhiệt độ của khối khí", "Độ cao của khối khí", "Tốc độ gió thổi xung quanh", "Hình dạng bình chứa khí"],
                0, "Đối với khí lý tưởng, bỏ qua thế năng tương tác nên nội năng chỉ phụ thuộc vào nhiệt độ."),
        make_mc(2, "Nhận biết", "Kim loại nào sau đây dẫn nhiệt tốt nhất trong các kim loại?",
                ["Bạc", "Đồng", "Nhôm", "Sắt"],
                0, "Bạc là kim loại dẫn nhiệt tốt nhất trong bảng tuần hoàn."),
        make_mc(3, "Nhận biết", "Trong các vật sau, vật nào hấp thụ bức xạ nhiệt tốt nhất?",
                ["Vật có bề mặt xù xì màu đen", "Vật có bề mặt nhẵn bóng màu trắng", "Tấm gương phẳng phản xạ ánh sáng", "Miếng bạc đánh bóng"],
                0, "Bề mặt xù xì và sẫm màu hấp thụ bức xạ nhiệt mạnh nhất."),
        make_mc(4, "Nhận biết", "Khi bị ngăn cản dãn nở nhiệt, lực đàn hồi sinh ra trong thanh kim loại có đặc điểm:",
                ["Có độ lớn rất lớn", "Rất nhỏ không đáng kể", "Luôn bằng không", "Chỉ phụ thuộc vào màu sắc thanh"],
                0, "Lực sinh ra khi bị cản trở dãn nở nhiệt có độ lớn khổng lồ có thể làm cong đường ray, nứt vỡ mố cầu."),
        make_mc(5, "Thông hiểu", "Tại sao về mùa hè cá ở các ao hồ nông thường hay nổi đầu lên mặt nước để thở?",
                ["Vì khi nhiệt độ nước tăng, độ tan của khí oxi trong nước giảm và sự hô hấp của sinh vật tăng làm thiếu oxi ở tầng đáy", "Vì nước ở đáy ao quá lạnh", "Vì cá thích tắm nắng", "Vì áp suất nước đáy ao tăng cao"],
                0, "Nhiệt độ nước tăng làm giảm lượng oxi hòa tan trong nước ao hồ."),
        make_mc(6, "Thông hiểu", "Trường hợp nào sau đây là ứng dụng của dòng đối lưu nhân tạo?",
                ["Lắp quạt thông gió trong phòng kín và hệ thống điều hòa", "Lắp bóng đèn sợi đốt", "Lắp gương chiếu hậu xe", "Đóng cọc móng nhà"],
                0, "Quạt thông gió và quạt điều hòa tạo ra các dòng đối lưu cưỡng bức làm mát không gian phòng."),
        make_mc(7, "Thông hiểu", "Một băng kép làm bằng hai lá kim loại X và Y tán chặt vào nhau. Khi nung nóng băng kép uốn cong về phía lá X. Kết luận nào sau đây đúng?",
                ["Lá Y nở vì nhiệt nhiều hơn lá X", "Lá X nở vì nhiệt nhiều hơn lá Y", "Lá X dẫn nhiệt tốt hơn lá Y", "Lá Y có khối lượng riêng lớn hơn lá X"],
                0, "Uốn cong về phía lá X chứng tỏ lá X nở dài ít hơn lá Y (lá Y ở mặt lồi dãn dài hơn)."),
        make_mc(8, "Thông hiểu", "Rót nước sôi vào một cốc thủy tinh mỏng thì cốc không bị vỡ, nhưng rót vào cốc thủy tinh dày thì cốc lại bị nứt vỡ. Nguyên nhân là do:",
                ["Thủy tinh mỏng truyền nhiệt nhanh làm mặt trong và mặt ngoài dãn nở đồng thời, còn cốc dày mặt ngoài chưa kịp nở đã bị mặt trong chèn ép sinh lực phá hủy", "Thủy tinh dày giòn hơn thủy tinh mỏng", "Cốc mỏng đàn hồi tốt hơn", "Nước sôi tiếp xúc với cốc dày nóng hơn"],
                0, "Chênh lệch dãn nở nhiệt giữa hai mặt trong và ngoài của cốc dày gây ứng suất nhiệt lớn làm nứt cốc."),
        make_mc(9, "Thông hiểu", "Tại sao quả bóng bàn bị móp nhưng chưa rách, khi thả vào nước nóng lại phồng lên?",
                ["Không khí trong bóng bị nóng nở ra làm tăng áp suất đẩy vỏ bóng phồng trở lại", "Nước thấm qua vỏ làm mềm nhựa", "Áp suất nước bên ngoài hút vỏ bóng", "Nhựa bóng bàn tự phục hồi khi gặp ẩm"],
                0, "Khí trong bóng nhận nhiệt nóng lên nở ra sinh công làm phồng vỏ bóng."),
        make_mc(10, "Vận dụng", "Người ta thả 0,1 kg đồng ở 100°C vào một lượng nước ở 20°C thì nhiệt độ cân bằng là 25°C. Khối lượng nước trong cốc là bao nhiêu? Cho c_đồng = 380 J/(kg.K), c_nước = 4200 J/(kg.K). Bỏ qua nhiệt dung của cốc.",
                ["0,136 kg", "0,250 kg", "0,085 kg", "0,180 kg"],
                0, "Qtỏa = 0,1 * 380 * (100 - 25) = 38 * 75 = 2850 J. Qthu = m_nước * 4200 * (25 - 20) = 21000 * m_nước. m_nước = 2850 / 21000 ≈ 0,1357 kg ≈ 0,136 kg."),
        make_mc(11, "Vận dụng", "Một thanh sắt tiết diện S = 2 cm² bị giữ chặt hai đầu ở 20°C. Khi nhiệt độ tăng lên 60°C, lực nén sinh ra trong thanh sắt là bao nhiêu? Biết E = 2 * 10¹¹ N/m², α = 12 * 10⁻⁶ K⁻¹.",
                ["19200 N", "9600 N", "38400 N", "4800 N"],
                0, "F = E * S * α * Δt = 2 * 10¹¹ * (2 * 10⁻⁴) * (12 * 10⁻⁶) * 40 = 19200 N."),
        make_mc(12, "Vận dụng", "Đun một ấm nước 2 kg từ 25°C đến khi sôi 100°C bằng bếp có công suất 1200 W, hiệu suất 75%. Thời gian đun sôi nước là:",
                ["700 giây", "525 giây", "933 giây", "600 giây"],
                0, "Qthu = 2 * 4200 * 75 = 630000 J. P_ci = 1200 * 0,75 = 900 W. t = 630000 / 900 = 700 s.")
    ]

    p2_t5 = [
        make_tf(1, "Thông hiểu", "Xét các hình thức truyền nhiệt và ứng dụng công nghệ:",
                [("a", "Bức xạ nhiệt có thể truyền qua cả chân không và các môi trường trong suốt.", True),
                 ("b", "Bếp hồng ngoại làm chín thức ăn chủ yếu dựa trên hình thức bức xạ nhiệt.", True),
                 ("c", "Dòng đối lưu tự nhiên chỉ xuất hiện khi có sự chênh lệch khối lượng riêng của các vùng chất lưu.", True),
                 ("d", "Khí hydro và khí cacbonic khi tăng cùng độ nhiệt sẽ có độ dãn nở thể tích khác nhau.", False)],
                "Các chất khí khác nhau đều nở vì nhiệt giống nhau."),
        make_tf(2, "Thông hiểu", "Xét các nguyên lý bảo toàn trong nhiệt học:",
                [("a", "Nhiệt lượng không tự sinh ra và không tự mất đi mà chỉ truyền từ vật này sang vật khác.", True),
                 ("b", "Hiệu suất của bất kỳ động cơ nhiệt nào trong thực tế cũng không thể vượt quá 100%.", True),
                 ("c", "Khi cọ xát cơ năng hoàn toàn có thể biến đổi thành nội năng với hiệu suất 100%.", True),
                 ("d", "Nhiệt năng có thể tự phát truyền từ vật lạnh sang vật nóng hơn mà không cần tác nhân ngoài.", False)],
                "Nhiệt năng không thể tự truyền từ vật lạnh sang vật nóng hơn mà không có tác nhân bên ngoài tác động."),
        make_tf(3, "Vận dụng", "Xét bài toán truyền nhiệt trong công trình xây dựng:",
                [("a", "Tường nhà xây bằng gạch lỗ có tác dụng cách nhiệt tốt nhờ các lớp không khí đứng yên trong lỗ gạch.", True),
                 ("b", "Cửa sổ kính hộp 2 lớp có lớp khí trơ ở giữa giúp giảm đáng kể thất thoát nhiệt điều hòa.", True),
                 ("c", "Cầu thép dài không cần gối đỡ con lăn nếu mố cầu bằng bê tông cốt thép cực kỳ kiên cố.", False),
                 ("d", "Ống khói cao tạo lực hút đối lưu tự nhiên giúp lò đốt cháy mạnh hơn.", True)],
                "Cầu thép dài bắt buộc phải có gối con lăn co dãn nhiệt, nếu không sẽ phá hủy mố cầu."),
        make_tf(4, "Vận dụng", "Xét hiện tượng dãn nở của chất lỏng và chất rắn:",
                [("a", "Nhiệt kế thủy ngân có thể dùng để đo nhiệt độ của nước đá đang tan và nước đang sôi ở điều kiện tiêu chuẩn.", True),
                 ("b", "Rượu nở vì nhiệt nhiều hơn nước nên nhiệt kế rượu có độ nhạy nhiệt cao hơn nhiệt kế nước.", True),
                 ("c", "Nước ở 4°C khi đun nóng lên 10°C hay làm lạnh xuống 0°C đều tăng thể tích.", True),
                 ("d", "Khi nhiệt độ tăng, chu kì dao động của con lắc đồng hồ quả lắc bằng kim loại giảm làm đồng hồ chạy nhanh hơn.", False)],
                "Nhiệt độ tăng thanh con lắc dãn dài làm chu kì T = 2π√(l/g) tăng, đồng hồ chạy chậm lại.")
    ]

    p3_t5 = [
        make_sa(1, "Thông hiểu", "Bạc và thủy tinh, chất nào dẫn nhiệt tốt hơn?", "Bạc", "Bạc là kim loại dẫn nhiệt tốt nhất."),
        make_sa(2, "Thông hiểu", "Để tránh nứt vỡ mố cầu do dãn nở nhiệt, một đầu nhịp cầu thép được đặt trên bộ phận nào?", "Con lăn", "Gối cầu con lăn."),
        make_sa(3, "Thông hiểu", "Đổi 1 kcal ra Jun (lấy 1 cal = 4,186 J).", "4186", "1 kcal = 4186 J."),
        make_sa(4, "Vận dụng", "Cần thực hiện công bao nhiêu Jun để nâng một vật 50 kg lên cao 8 m? Giả sử toàn bộ công này chuyển thành nhiệt làm nóng 2 kg nước, nhiệt độ nước tăng thêm bao nhiêu độ C? (lấy g = 10 m/s², c = 4200 J/(kg.K), làm tròn đến 2 chữ số thập phân).", "0.48", "A = m*g*h = 50 * 10 * 8 = 4000 J. Δt = A / (m_nước * c) = 4000 / (2 * 4200) ≈ 0,476 ≈ 0,48°C."),
        make_sa(5, "Vận dụng", "Một thanh đồng có chiều dài 2,5 m ở 10°C. Khi nhiệt độ là 90°C thì thanh đồng dài thêm bao nhiêu mm? (α = 17 * 10⁻⁶ K⁻¹).", "3.4", "ΔL = 17 * 10⁻⁶ * 2,5 * 80 = 3,4 * 10⁻³ m = 3,4 mm."),
        make_sa(6, "Vận dụng", "Đun sôi 1,5 kg nước từ 20°C bằng bếp điện có công suất 1500 W trong 9 phút. Hiệu suất nhiệt của bếp điện là bao nhiêu phần trăm (làm tròn số nguyên)?", "62", "Qthu = 1,5 * 4200 * 80 = 504000 J. A = 1500 * 540 = 810000 J. H = 504000 / 810000 ≈ 62,2% ≈ 62%.")
    ]

    p4_t5 = [
        make_vdc(1, "Một bình cách nhiệt chứa 500 g nước ở nhiệt độ 25°C. Người ta thả vào bình một cục nước đá khối lượng 100 g ở 0°C. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K), nhiệt nóng chảy riêng của nước đá λ = 3,34 * 10⁵ J/kg. Bỏ qua nhiệt dung của bình. Sau khi cân bằng nhiệt được thiết lập, trạng thái và nhiệt độ của hệ là:",
                 ["Nước đá tan hoàn toàn, nhiệt độ cân bằng xấp xỉ bằng 7,6°C", "Nước đá chỉ tan một phần, nhiệt độ cân bằng là 0°C", "Toàn bộ nước đóng băng thành đá ở 0°C", "Nước lỏng ở nhiệt độ 12,5°C"],
                 0, "Nhiệt lượng nước tỏa ra khi hạ từ 25 xuống 0°C: Qtỏa_max = 0,5 * 4200 * 25 = 52500 J. Nhiệt lượng cần làm tan hết đá: Q_tan = 0,1 * 3,34 * 10⁵ = 33400 J. Vì Qtỏa_max > Q_tan nên đá tan hoàn toàn. Nhiệt lượng còn lại: Q_dư = 52500 - 33400 = 19100 J. Nhiệt độ cân bằng: t_cb = 19100 / ((0,5 + 0,1) * 4200) = 19100 / 2520 ≈ 7,58°C ≈ 7,6°C."),
        make_vdc(2, "Một khối nhôm có khối lượng 2 kg rơi tự do từ độ cao h = 100 m xuống một nền đá cứng và dừng lại. Giả sử 60% cơ năng của khối nhôm chuyển hóa thành nội năng làm nóng khối nhôm. Biết nhiệt dung riêng của nhôm c = 880 J/(kg.K) và g = 10 m/s². Độ tăng nhiệt độ của khối nhôm sau va chạm xấp xỉ bằng:",
                 ["0,68°C", "1,14°C", "0,34°C", "1,36°C"],
                 0, "Cơ năng W = m * g * h = 2 * 10 * 100 = 2000 J. Q = 0,6 * 2000 = 1200 J. Δt = Q / (m * c) = 1200 / (2 * 880) = 1200 / 1760 ≈ 0,6818°C ≈ 0,68°C."),
        make_vdc(3, "Một thanh thép có diện tích tiết diện S = 8 cm² và chiều dài L0 = 2 m được lắp khít giữa hai bức tường kiên cố ở 15°C. Khi nhiệt độ tăng lên đến 45°C, coi tường không biến dạng. Cho biết suất đàn hồi của thép là E = 2 * 10¹¹ N/m², hệ số nở dài α = 12 * 10⁻⁶ K⁻¹. Lực nén do thanh thép tác dụng lên tường là:",
                 ["57,6 kN", "28,8 kN", "115,2 kN", "14,4 kN"],
                 0, "F = E * S * α * Δt = 2 * 10¹¹ * (8 * 10⁻⁴) * (12 * 10⁻⁶) * (45 - 15) = 16 * 10⁷ * 12 * 10⁻⁶ * 30 = 57600 N = 57,6 kN."),
        make_vdc(4, "Một máy đun nước năng lượng mặt trời có diện tích bề mặt thu nhiệt là S = 2 m². Cường độ bức xạ Mặt Trời chiếu thẳng góc vào bề mặt tấm thu là 800 W/m². Hiệu suất hấp thụ bức xạ chuyển thành nhiệt làm nóng nước là 65%. Trong 2 giờ nắng gắt liên tục, máy này có thể làm nóng bao nhiêu lít nước từ 25°C lên 65°C? Cho biết c_nước = 4200 J/(kg.K), D_nước = 1000 kg/m³.",
                 ["44,6 lít", "68,5 lít", "32,4 lít", "55,2 lít"],
                 0, "Công suất bức xạ nhận được: P_thu = 800 * 2 = 1600 W. Năng lượng nhiệt có ích truyền cho nước trong 2 giờ (7200 s): Q = 0,65 * 1600 * 7200 = 7488000 J. Khối lượng nước: m = Q / (c * Δt) = 7488000 / (4200 * 40) = 7488000 / 168000 = 44,57 kg ≈ 44,6 kg (tương đương 44,6 lít).")
    ]

    exams[f"{les_id}_test5"] = {
        "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {les_name} - Đề số 05",
        "grade": "8", "subject": "physics", "subjectName": "Vật lý",
        "chapterId": ch_id, "chapterTitle": ch_title, "lessonId": les_id, "lessonName": les_name,
        "testNum": 5, "duration": "45 phút", "points": 10.0,
        "part1": p1_t5, "part2": p2_t5, "part3": p3_t5, "part4": p4_t5
    }

    return exams

if __name__ == '__main__':
    exs = get_c6_rev_exams()
    print("Generated Ôn tập C6:", len(exs), "exams.")
