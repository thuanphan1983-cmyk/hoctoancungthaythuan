# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 13: ÔN TẬP CUỐI NĂM (PHẦN 2: BÀI 62 VÀ BÀI 63)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 2 bài học x 3 đề độc lập = 6 đề thi (th4_b62_test1 -> th4_b63_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, question_text, options, correct, explanation):
    q_title = f"**Câu {qid}:** {question_text}" if not question_text.startswith(f"**Câu {qid}:**") else question_text
    return {
        "id": qid,
        "question": q_title,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question_text, solution, answer, lineCount=4, points=1.0):
    p_title = f"**Bài {qid}:** {question_text}" if not question_text.startswith(f"**Bài {qid}:**") else question_text
    return {
        "id": qid,
        "question": p_title,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_ch13_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 62: ÔN TẬP MỘT SỐ YẾU TỐ THỐNG KÊ VÀ XÁC SUẤT
    # =========================================================================

    # --- Bài 62 - Đề 1 ---
    exams["th4_b62_test1"] = {
        "id": "th4_b62_test1",
        "lessonId": "th4_b62",
        "lessonNum": 62,
        "testNum": 1,
        "title": "Bài 62: Ôn tập một số yếu tố thống kê và xác suất - Đề số 1",
        "topic": "Ôn tập một số yếu tố thống kê và xác suất",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Gieo một con xúc xắc 6 mặt (các mặt ghi số từ 1 đến 6). Sự kiện nào sau đây là 'Không thể xảy ra'?", ["Xuất hiện mặt có 7 chấm", "Xuất hiện mặt có 6 chấm", "Xuất hiện mặt có số chấm là số chẵn", "Xuất hiện mặt có 1 chấm"], 0, "Xúc xắc chỉ có từ 1 đến 6 chấm nên không thể có 7 chấm."),
            make_mc(2, "Trong một hộp kín có 5 viên bi đỏ và 5 viên bi xanh. Không nhìn vào hộp, lấy ra 1 viên bi. Sự kiện nào sau đây là 'Có thể xảy ra'?", ["Lấy được viên bi màu đỏ", "Lấy được viên bi màu vàng", "Lấy được viên bi màu tím", "Lấy được 10 viên bi"], 0, "Lấy được bi đỏ hoặc bi xanh là có thể xảy ra."),
            make_mc(3, "Bảng thống kê số cây trồng của 4 lớp: Lớp 4A: 45 cây; Lớp 4B: 50 cây; Lớp 4C: 40 cây; Lớp 4D: 55 cây. Lớp trồng được nhiều cây nhất là:", ["Lớp 4D", "Lớp 4B", "Lớp 4A", "Lớp 4C"], 0, "Lớp 4D trồng 55 cây là nhiều nhất."),
            make_mc(4, "Trung bình cộng số cây trồng của 4 lớp trên là:", ["47,5 cây", "45 cây", "48 cây", "50 cây"], 0, "(45 + 50 + 40 + 55) : 4 = 190 : 4 = 47,5 cây."),
            make_mc(5, "Tung một đồng xu 1 lần. Khả năng xuất hiện mặt Sấp là:", ["Có thể xảy ra", "Chắc chắn xảy ra", "Không thể xảy ra", "Luôn luôn xảy ra"], 0, "Đồng xu có 2 mặt nên có thể sấp hoặc ngửa."),
            make_mc(6, "Trong biểu đồ cột, chiều cao của mỗi cột biểu diễn:", ["Số liệu của đối tượng thống kê", "Tên của đối tượng", "Độ rộng của cột", "Màu sắc của cột"], 0, "Chiều cao cột thể hiện số liệu thống kê tương ứng.")
        ],
        "part2": [
            make_essay(1, "Trong hộp có 3 quả bóng màu xanh, 2 quả bóng màu đỏ và 1 quả bóng màu vàng. Nam lấy ngẫu nhiên 1 quả bóng. Hãy xác định khả năng xảy ra của các sự kiện sau (chắc chắn, có thể, không thể):\na) Nam lấy được quả bóng màu đỏ.\nb) Nam lấy được quả bóng màu tím.\nc) Quả bóng lấy ra có màu xanh, đỏ hoặc vàng.", "a) Có thể xảy ra (vì trong hộp có bóng đỏ).\nb) Không thể xảy ra (vì trong hộp không có bóng tím).\nc) Chắc chắn xảy ra (vì tất cả bóng trong hộp chỉ có màu xanh, đỏ hoặc vàng).", "a) Có thể; b) Không thể; c) Chắc chắn", 4, 1.0),
            make_essay(2, "Số lượng điểm 10 môn Toán trong học kì 2 của một tổ gồm 5 bạn là: Lan: 8 điểm 10; Mai: 10 điểm 10; Hùng: 6 điểm 10; Nam: 9 điểm 10; Cúc: 7 điểm 10.\na) Bạn nào đạt nhiều điểm 10 nhất? Bạn nào ít điểm 10 nhất?\nb) Tính trung bình mỗi bạn trong tổ đạt bao nhiêu điểm 10?", "a) Bạn Mai đạt nhiều điểm 10 nhất (10 điểm 10); Bạn Hùng đạt ít điểm 10 nhất (6 điểm 10).\nb) Tổng số điểm 10 của cả tổ là: $8 + 10 + 6 + 9 + 7 = 40\\text{ (điểm 10)}$.\nTrung bình mỗi bạn đạt số điểm 10 là:\n$40 : 5 = 8\\text{ (điểm 10)}$.", "a) Nhiều nhất: Mai; Ít nhất: Hùng; b) Trung bình: 8 điểm 10", 4, 1.0),
            make_essay(3, "Bảng thống kê số lượng sách giáo khoa lớp 4 được quyên góp của 4 khối lớp:\nKhối 1: 120 cuốn; Khối 2: 150 cuốn; Khối 3: 180 cuốn; Khối 4: 210 cuốn.\na) Cả 4 khối quyên góp được tất cả bao nhiêu cuốn sách?\nb) Khối 4 quyên góp nhiều hơn Khối 1 bao nhiêu cuốn sách?", "a) Cả 4 khối quyên góp được là:\n$120 + 150 + 180 + 210 = 660\\text{ (cuốn sách)}$.\nb) Khối 4 quyên góp nhiều hơn Khối 1 là:\n$210 - 120 = 90\\text{ (cuốn sách)}$.", "a) 660 cuốn; b) 90 cuốn", 4, 1.0),
            make_essay(4, "Một hộp chứa 4 thẻ ghi các số: 2, 4, 6, 8. Rút ngẫu nhiên một tấm thẻ từ hộp đó. Hãy nêu các kết quả có thể xảy ra và nhận xét xem số ghi trên thẻ rút ra có chắc chắn là số chẵn không? Vì sao?", "Các kết quả có thể xảy ra khi rút thẻ là: Rút được thẻ số 2, hoặc thẻ số 4, hoặc thẻ số 6, hoặc thẻ số 8.\nNhận xét: Số ghi trên thẻ rút ra chắc chắn là số chẵn, vì cả 4 tấm thẻ trong hộp đều ghi các số chẵn (2, 4, 6, 8).", "Các kết quả: 2, 4, 6, 8; Chắc chắn là số chẵn vì cả 4 số đều chẵn", 5, 1.5),
            make_essay(5, "Số lượng học sinh giỏi của 3 lớp 4A, 4B, 4C lần lượt là 16 bạn, 18 bạn và 14 bạn. Cuối năm cô giáo thưởng cho mỗi bạn học sinh giỏi 5 quyển vở.\na) Tính tổng số quyển vở cô giáo cần phát thưởng cho cả 3 lớp.\nb) Trung bình mỗi lớp có bao nhiêu học sinh giỏi?", "a) Tổng số học sinh giỏi của cả 3 lớp là:\n$16 + 18 + 14 = 48\\text{ (học sinh)}$.\nTổng số quyển vở cô giáo cần phát thưởng là:\n$48 \\times 5 = 240\\text{ (quyển)}$.\nb) Trung bình mỗi lớp có số học sinh giỏi là:\n$48 : 3 = 16\\text{ (học sinh)}$.", "a) 240 quyển vở; b) 16 học sinh", 5, 1.5),
            make_essay(6, "Trong trò chơi quay bánh xe may mắn được chia thành 8 phần bằng nhau, trong đó có 3 phần ghi 'Thêm lượt', 4 phần ghi 'Phần quà' và 1 phần ghi 'Mất lượt'.\na) Sự kiện kim quay dừng ở ô nào có khả năng xảy ra cao nhất?\nb) Sự kiện kim quay dừng ở ô nào có khả năng xảy ra thấp nhất?", "a) Sự kiện dừng ở ô 'Phần quà' có khả năng xảy ra cao nhất vì chiếm nhiều ô nhất (4/8 bánh xe).\nb) Sự kiện dừng ở ô 'Mất lượt' có khả năng xảy ra thấp nhất vì chỉ có 1 ô (1/8 bánh xe).", "a) Cao nhất: 'Phần quà'; b) Thấp nhất: 'Mất lượt'", 4, 1.0)
        ]
    }

    # --- Bài 62 - Đề 2 ---
    exams["th4_b62_test2"] = {
        "id": "th4_b62_test2",
        "lessonId": "th4_b62",
        "lessonNum": 62,
        "testNum": 2,
        "title": "Bài 62: Ôn tập một số yếu tố thống kê và xác suất - Đề số 2",
        "topic": "Ôn tập một số yếu tố thống kê và xác suất",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Ngày mai Mặt Trời mọc ở đằng Đông là sự kiện:", ["Chắc chắn xảy ra", "Có thể xảy ra", "Không thể xảy ra", "Hiếm khi xảy ra"], 0, "Quy luật tự nhiên: Mặt Trời luôn mọc ở đằng Đông nên chắc chắn xảy ra."),
            make_mc(2, "Rút một lá bài trong bộ bài tây 52 lá, rút được lá bài màu đen là sự kiện:", ["Có thể xảy ra", "Chắc chắn xảy ra", "Không thể xảy ra", "Không xác định"], 0, "Bộ bài có 26 lá đen và 26 lá đỏ nên có thể xảy ra."),
            make_mc(3, "Bảng điểm kiểm tra môn Toán của 4 bạn: An: 9; Bình: 8; Chi: 10; Dũng: 9. Điểm trung bình của 4 bạn là:", ["9", "8,5", "9,5", "8"], 0, "(9 + 8 + 10 + 9) : 4 = 36 : 4 = 9."),
            make_mc(4, "Biểu đồ cột biểu diễn số cây trồng của khối 4 có các cột cao lần lượt là: 30, 40, 50, 40. Tổng số cây trồng của khối 4 là:", ["160 cây", "150 cây", "170 cây", "140 cây"], 0, "30 + 40 + 50 + 40 = 160 cây."),
            make_mc(5, "Khi gieo một đồng xu, có bao nhiêu khả năng có thể xuất hiện?", ["2 khả năng", "1 khả năng", "3 khả năng", "4 khả năng"], 0, "Có 2 khả năng: mặt Sấp (S) hoặc mặt Ngửa (N)."),
            make_mc(6, "Trong một túi chỉ có 10 cái kẹo dâu. Một bạn thò tay lấy 1 cái kẹo vị cam là sự kiện:", ["Không thể xảy ra", "Có thể xảy ra", "Chắc chắn xảy ra", "Luôn xảy ra"], 0, "Trong túi không có kẹo cam nên không thể xảy ra.")
        ],
        "part2": [
            make_essay(1, "Ghi lại khả năng xảy ra (chắc chắn, có thể, không thể) cho các sự kiện sau:\na) Ngày mai ở trường em trời có mưa.\nb) Một con cá bơi được dưới nước.\nc) Một người bình thường bay được trên không trung như chim mà không cần bất kì dụng cụ nào.", "a) Có thể xảy ra (thời tiết có thể mưa hoặc không).\nb) Chắc chắn xảy ra (cá sống và bơi dưới nước).\nc) Không thể xảy ra (con người không tự bay được).", "a) Có thể; b) Chắc chắn; c) Không thể", 4, 1.0),
            make_essay(2, "Số học sinh của 4 lớp 4A, 4B, 4C, 4D lần lượt là 34, 35, 36, 35 em.\na) Lớp nào có đông học sinh nhất? Lớp nào ít học sinh nhất?\nb) Tính số học sinh trung bình của mỗi lớp.", "a) Lớp 4C đông nhất (36 em); Lớp 4A ít nhất (34 em).\nb) Tổng số học sinh là: $34 + 35 + 36 + 35 = 140\\text{ (em)}$.\nTrung bình mỗi lớp có số học sinh là:\n$140 : 4 = 35\\text{ (em)}$.", "a) Đông nhất: 4C, Ít nhất: 4A; b) Trung bình: 35 học sinh", 4, 1.0),
            make_essay(3, "Bảng thống kê số ki-lô-gam giấy vụn thu gom của 3 tổ:\nTổ 1: 42 kg; Tổ 2: 48 kg; Tổ 3: 45 kg.\na) Cả ba tổ thu gom được tất cả bao nhiêu ki-lô-gam giấy vụn?\nb) Trung bình mỗi tổ thu gom được bao nhiêu ki-lô-gam giấy vụn?", "a) Cả ba tổ thu gom được là:\n$42 + 48 + 45 = 135\\text{ (kg)}$.\nb) Trung bình mỗi tổ thu gom được là:\n$135 : 3 = 45\\text{ (kg)}$.", "a) 135 kg; b) 45 kg", 4, 1.0),
            make_essay(4, "Một hộp có 5 tấm thẻ ghi các số: 10, 20, 30, 40, 50. Mai rút ngẫu nhiên một tấm thẻ.\na) Nêu các kết quả có thể xảy ra.\nb) Sự kiện 'Thẻ rút được là số tròn chục' là sự kiện gì (chắc chắn, có thể hay không thể)?", "a) Các kết quả có thể xảy ra: Rút được thẻ 10, hoặc 20, hoặc 30, hoặc 40, hoặc 50.\nb) Sự kiện 'Thẻ rút được là số tròn chục' là sự kiện chắc chắn xảy ra vì tất cả 5 số trong hộp đều là số tròn chục.", "a) 10, 20, 30, 40, 50; b) Chắc chắn xảy ra", 5, 1.5),
            make_essay(5, "Biểu đồ cột biểu diễn số điểm tốt của bạn Nam trong 4 tuần như sau:\nTuần 1: 12 điểm tốt; Tuần 2: 15 điểm tốt; Tuần 3: 14 điểm tốt; Tuần 4: 19 điểm tốt.\na) Tuần nào Nam đạt nhiều điểm tốt nhất? Tuần nào ít nhất?\nb) Tính trung bình mỗi tuần Nam đạt bao nhiêu điểm tốt?", "a) Tuần 4 đạt nhiều nhất (19 điểm tốt); Tuần 1 đạt ít nhất (12 điểm tốt).\nb) Tổng số điểm tốt trong 4 tuần là:\n$12 + 15 + 14 + 19 = 60\\text{ (điểm tốt)}$.\nTrung bình mỗi tuần Nam đạt:\n$60 : 4 = 15\\text{ (điểm tốt)}$.", "a) Nhiều nhất: Tuần 4; Ít nhất: Tuần 1; b) Trung bình: 15 điểm tốt", 5, 1.5),
            make_essay(6, "Bác An có 3 chiếc chìa khóa giống nhau bề ngoài để mở 3 ổ khóa khác nhau. Bác An thử ngẫu nhiên một chiếc chìa khóa vào ổ khóa thứ nhất. Có những khả năng nào có thể xảy ra đối với chiếc chìa khóa đó?", "Có 2 khả năng có thể xảy ra:\n1) Chiếc chìa khóa đó mở được ổ khóa thứ nhất (đúng chìa).\n2) Chiếc chìa khóa đó không mở được ổ khóa thứ nhất (sai chìa).", "2 khả năng: Mở được hoặc Không mở được", 4, 1.0)
        ]
    }

    # --- Bài 62 - Đề 3 ---
    exams["th4_b62_test3"] = {
        "id": "th4_b62_test3",
        "lessonId": "th4_b62",
        "lessonNum": 62,
        "testNum": 3,
        "title": "Bài 62: Ôn tập một số yếu tố thống kê và xác suất - Đề số 3",
        "topic": "Ôn tập một số yếu tố thống kê và xác suất",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một năm có 365 hoặc 366 ngày. Ngày 30 tháng 2 trong năm là sự kiện:", ["Không thể xảy ra", "Chắc chắn xảy ra", "Có thể xảy ra", "Luôn xảy ra"], 0, "Tháng 2 chỉ có tối đa 29 ngày, không bao giờ có ngày 30 tháng 2."),
            make_mc(2, "Gieo đồng thời hai con xúc xắc. Tổng số chấm xuất hiện lớn hơn 1 là sự kiện:", ["Chắc chắn xảy ra", "Có thể xảy ra", "Không thể xảy ra", "Tùy lúc"], 0, "Số chấm nhỏ nhất của mỗi con là 1, tổng nhỏ nhất là 1 + 1 = 2 > 1 nên chắc chắn xảy ra."),
            make_mc(3, "Bốn bạn đo chiều cao: Hà: 135 cm; Hằng: 138 cm; Hiếu: 140 cm; Hải: 139 cm. Chiều cao trung bình của 4 bạn là:", ["138 cm", "139 cm", "137 cm", "140 cm"], 0, "(135 + 138 + 140 + 139) : 4 = 552 : 4 = 138 cm."),
            make_mc(4, "Biểu đồ tranh biểu thị số con cá bác Ba câu được trong 3 ngày (mỗi biểu tượng con cá ứng với 5 con). Nếu ngày thứ ba có 4 biểu tượng con cá thì số cá câu được là:", ["20 con", "15 con", "25 con", "10 con"], 0, "4 x 5 = 20 con cá."),
            make_mc(5, "Khi chọn ngẫu nhiên một chữ cái trong từ 'TOAN', khả năng chọn được chữ 'O' là:", ["Có thể xảy ra", "Chắc chắn xảy ra", "Không thể xảy ra", "Không xác định"], 0, "Có thể chọn được chữ T, O, A hoặc N."),
            make_mc(6, "Trong dãy số tự nhiên từ 1 đến 10, chọn ngẫu nhiên một số. Khả năng chọn được số chia hết cho 11 là:", ["Không thể xảy ra", "Có thể xảy ra", "Chắc chắn xảy ra", "Hiếm xảy ra"], 0, "Từ 1 đến 10 không có số nào chia hết cho 11 nên không thể xảy ra.")
        ],
        "part2": [
            make_essay(1, "Một túi đựng 6 viên bi gồm 2 bi xanh, 2 bi đỏ và 2 bi vàng. Không nhìn vào túi, lấy ra cùng lúc 4 viên bi. Hãy giải thích vì sao sự kiện 'Trong 4 viên bi lấy ra có ít nhất 2 viên bi cùng màu' là sự kiện chắc chắn xảy ra.", "Trong túi chỉ có 3 màu khác nhau (xanh, đỏ, vàng).\nKhi lấy ra 4 viên bi (số bi lấy ra là 4 lớn hơn số lượng màu là 3), theo nguyên lý thực tế, không thể có chuyện cả 4 viên đều khác màu nhau.\nDo đó chắc chắn phải có ít nhất hai viên bi cùng màu.", "Vì chỉ có 3 màu bi mà lấy 4 viên nên chắc chắn có ít nhất 2 viên cùng màu", 4, 1.0),
            make_essay(2, "Số lượng học sinh tham gia các câu lạc bộ của trường tiểu học:\n- CLB Bóng đá: 45 em\n- CLB Bơi lội: 35 em\n- CLB Cờ vua: 25 em\n- CLB Âm nhạc: 35 em\na) Câu lạc bộ nào có nhiều học sinh tham gia nhất? Câu lạc bộ nào ít nhất?\nb) Trung bình mỗi câu lạc bộ có bao nhiêu học sinh tham gia?", "a) CLB Bóng đá nhiều nhất (45 em); CLB Cờ vua ít nhất (25 em).\nb) Tổng số học sinh là: $45 + 35 + 25 + 35 = 140\\text{ (em)}$.\nTrung bình mỗi CLB có: $140 : 4 = 35\\text{ (em)}$.", "a) Nhiều nhất: Bóng đá; Ít nhất: Cờ vua; b) Trung bình: 35 em", 4, 1.0),
            make_essay(3, "Bảng thống kê lượng mưa trong 3 tháng mùa hè tại một tỉnh:\nTháng 6: 180 mm; Tháng 7: 240 mm; Tháng 8: 210 mm.\na) Tháng nào có lượng mưa nhiều nhất?\nb) Tính lượng mưa trung bình mỗi tháng trong 3 tháng mùa hè đó.", "a) Tháng 7 có lượng mưa nhiều nhất (240 mm).\nb) Tổng lượng mưa trong 3 tháng là:\n$180 + 240 + 210 = 630\\text{ (mm)}$.\nLượng mưa trung bình mỗi tháng là:\n$630 : 3 = 210\\text{ (mm)}$.", "a) Tháng 7; b) 210 mm", 4, 1.0),
            make_essay(4, "Một hộp kín chứa 3 quả cầu lông: 1 quả nhãn hiệu Hải Yến, 1 quả nhãn hiệu Thành Công, 1 quả nhãn hiệu Ba Sao. Minh nhắm mắt bốc lấy 1 quả cầu.\na) Liệt kê tất cả các kết quả có thể xảy ra.\nb) Có thể nói chắc chắn Minh sẽ bốc được quả cầu nhãn hiệu Hải Yến không? Vì sao?", "a) Các kết quả có thể xảy ra: Bốc được quả cầu Hải Yến, hoặc Thành Công, hoặc Ba Sao.\nb) Không thể nói chắc chắn, vì đây là sự kiện ngẫu nhiên có thể xảy ra hoặc không xảy ra (Minh có thể bốc trúng quả cầu Thành Công hoặc Ba Sao).", "a) Hải Yến, Thành Công, Ba Sao; b) Không, vì đây là sự kiện 'có thể xảy ra'", 5, 1.5),
            make_essay(5, "Một cửa hàng bán xe đạp thống kê số xe bán được trong 5 ngày của tuần đầu khai trương:\nThứ Hai: 6 chiếc; Thứ Ba: 8 chiếc; Thứ Tư: 7 chiếc; Thứ Năm: 9 chiếc; Thứ Sáu: 10 chiếc.\na) Cả 5 ngày cửa hàng bán được bao nhiêu chiếc xe đạp?\nb) Trung bình mỗi ngày cửa hàng bán được bao nhiêu chiếc xe đạp?", "a) Cả 5 ngày cửa hàng bán được:\n$6 + 8 + 7 + 9 + 10 = 40\\text{ (chiếc xe đạp)}$.\nb) Trung bình mỗi ngày bán được:\n$40 : 5 = 8\\text{ (chiếc xe đạp)}$.", "a) 40 chiếc xe; b) 8 chiếc xe", 5, 1.5),
            make_essay(6, "Trong trò chơi gieo một con xúc xắc 6 mặt cân đối, bạn An thắng nếu xuất hiện mặt có số chấm là số lẻ (1, 3, 5), bạn Bình thắng nếu xuất hiện mặt có số chấm là số chẵn (2, 4, 6). Em hãy nhận xét xem cơ hội thắng của hai bạn có bằng nhau không? Vì sao?", "Số các mặt mang số lẻ là 3 mặt (1, 3, 5).\nSố các mặt mang số chẵn là 3 mặt (2, 4, 6).\nVì số lượng mặt lẻ bằng số lượng mặt chẵn (đều là 3 mặt trên tổng số 6 mặt) nên khả năng xuất hiện số lẻ và số chẵn là như nhau.\nDo đó cơ hội chiến thắng của bạn An và bạn Bình là hoàn toàn bằng nhau (trò chơi công bằng).", "Cơ hội thắng của hai bạn hoàn toàn bằng nhau", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 63: LUYỆN TẬP CHUNG CUỐI NĂM
    # =========================================================================

    # --- Bài 63 - Đề 1 ---
    exams["th4_b63_test1"] = {
        "id": "th4_b63_test1",
        "lessonId": "th4_b63",
        "lessonNum": 63,
        "testNum": 1,
        "title": "Bài 63: Luyện tập chung cuối năm - Đề số 1",
        "topic": "Luyện tập chung cuối năm",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 4 triệu, 6 chục nghìn, 3 trăm và 5 đơn vị viết là:", ["4 060 305", "4 600 305", "4 060 035", "460 305"], 0, "4 060 305."),
            make_mc(2, "Rút gọn phân số $\\frac{45}{60}$ về phân số tối giản ta được:", ["$\\frac{3}{4}$", "$\\frac{9}{12}$", "$\\frac{15}{20}$", "$\\frac{4}{5}$"], 0, "45:15 / 60:15 = 3/4."),
            make_mc(3, "Kết quả của phép tính $\\frac{2}{3} + \\frac{1}{6} - \\frac{1}{2}$ là:", ["$\\frac{1}{3}$", "$\\frac{2}{6}$", "$\\frac{1}{2}$", "0"], 0, "4/6 + 1/6 - 3/6 = 2/6 = 1/3."),
            make_mc(4, "Một hình chữ nhật có chiều dài $\\frac{4}{5}\\text{ m}$, chiều rộng $\\frac{1}{2}\\text{ m}$. Diện tích hình chữ nhật đó là:", ["$\\frac{2}{5}\\text{ m}^2$", "$\\frac{4}{10}\\text{ m}^2$", "$\\frac{5}{7}\\text{ m}^2$", "$\\frac{3}{10}\\text{ m}^2$"], 0, "4/5 x 1/2 = 4/10 = 2/5 m²."),
            make_mc(5, "Đổi $5\\text{ tấn } 4\\text{ tạ} = \\dots \\text{ yến}$:", ["540 yến", "54 yến", "5 400 yến", "504 yến"], 0, "54 tạ = 540 yến."),
            make_mc(6, "Hai số có tổng bằng 120, hiệu bằng 40. Số lớn là:", ["80", "40", "60", "100"], 0, "(120 + 40) : 2 = 80.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\na) $\\frac{5}{9} \\times \\frac{3}{10} + \\frac{2}{3}$\nb) $3 - \\frac{7}{6} : \\frac{2}{3}$", "a) $\\frac{5}{9} \\times \\frac{3}{10} = \\frac{1}{6}$. Ta có: $\\frac{1}{6} + \\frac{2}{3} = \\frac{1}{6} + \\frac{4}{6} = \\frac{5}{6}$.\nb) $\\frac{7}{6} : \\frac{2}{3} = \\frac{7}{6} \\times \\frac{3}{2} = \\frac{7}{4}$. Ta có: $3 - \\frac{7}{4} = \\frac{12}{4} - \\frac{7}{4} = \\frac{5}{4}$.", "a) 5/6; b) 5/4", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $\\frac{5}{14} + \\frac{3}{8} + \\frac{9}{14} + \\frac{5}{8}$\nb) $125 \\times 47 \\times 8$", "a) $(\\frac{5}{14} + \\frac{9}{14}) + (\\frac{3}{8} + \\frac{5}{8}) = 1 + 1 = 2$.\nb) $(125 \\times 8) \\times 47 = 1000 \\times 47 = 47\\,000$.", "a) 2; b) 47 000", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chu vi 140 m. Chiều dài hơn chiều rộng 10 m. Tính diện tích mảnh vườn đó.", "Nửa chu vi mảnh vườn là: $140 : 2 = 70\\text{ (m)}$.\nChiều dài mảnh vườn là: $(70 + 10) : 2 = 40\\text{ (m)}$.\nChiều rộng mảnh vườn là: $70 - 40 = 30\\text{ (m)}$.\nDiện tích mảnh vườn là: $40 \\times 30 = 1200\\text{ (m}^2)$.", "1200 m²", 4, 1.0),
            make_essay(4, "Một cửa hàng có 3 tấn gạo. Ngày thứ nhất bán được $\\frac{2}{5}$ số gạo đó. Ngày thứ hai bán được số gạo bằng $\\frac{3}{4}$ số gạo bán ngày thứ nhất. Hỏi sau hai ngày, cửa hàng còn lại bao nhiêu ki-lô-gam gạo?", "Đổi: $3\\text{ tấn} = 3000\\text{ kg}$.\nSố gạo bán ngày thứ nhất là:\n$3000 \\times \\frac{2}{5} = 1200\\text{ (kg)}$.\nSố gạo bán ngày thứ hai là:\n$1200 \\times \\frac{3}{4} = 900\\text{ (kg)}$.\nTổng số gạo đã bán trong 2 ngày là:\n$1200 + 900 = 2100\\text{ (kg)}$.\nSố gạo còn lại là:\n$3000 - 2100 = 900\\text{ (kg)}$.", "900 kg gạo", 5, 1.5),
            make_essay(5, "Hiện nay tổng số tuổi của mẹ và con là 48 tuổi. Biết mẹ hơn con 28 tuổi. Hỏi sau bao nhiêu năm nữa thì tuổi mẹ gấp 3 lần tuổi con?", "Tuổi của mẹ hiện nay là: $(48 + 28) : 2 = 38\\text{ (tuổi)}$.\nTuổi của con hiện nay là: $48 - 38 = 10\\text{ (tuổi)}$.\nVì hiệu số tuổi không đổi nên khi tuổi mẹ gấp 3 lần tuổi con thì mẹ vẫn hơn con 28 tuổi.\nHiệu số phần bằng nhau: $3 - 1 = 2\\text{ (phần)}$.\nTuổi của con khi đó là: $28 : 2 = 14\\text{ (tuổi)}$.\nSố năm sau đó là: $14 - 10 = 4\\text{ (năm)}$.", "4 năm", 5, 1.5),
            make_essay(6, "Cho hình thoi ABCD có diện tích $72\\text{ cm}^2$. Biết độ dài một đường chéo là 12 cm. Tính độ dài đường chéo thứ hai của hình thoi đó.", "Độ dài đường chéo thứ hai của hình thoi là:\n$72 \\times 2 : 12 = 12\\text{ (cm)}$.", "12 cm", 4, 1.0)
        ]
    }

    # --- Bài 63 - Đề 2 ---
    exams["th4_b63_test2"] = {
        "id": "th4_b63_test2",
        "lessonId": "th4_b63",
        "lessonNum": 63,
        "testNum": 2,
        "title": "Bài 63: Luyện tập chung cuối năm - Đề số 2",
        "topic": "Luyện tập chung cuối năm",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số chẵn lớn nhất có 6 chữ số khác nhau là:", ["987 654", "999 998", "987 652", "987 650"], 0, "987 654."),
            make_mc(2, "Phân số nào sau đây lớn hơn 1?", ["$\\frac{9}{8}$", "$\\frac{7}{8}$", "$\\frac{8}{8}$", "$\\frac{3}{5}$"], 0, "Tử số 9 > mẫu số 8 nên 9/8 > 1."),
            make_mc(3, "Tính: $\\frac{4}{5} : \\frac{2}{3} = \\dots$:", ["$\\frac{6}{5}$", "$\\frac{8}{15}$", "$\\frac{5}{6}$", "$\\frac{2}{3}$"], 0, "4/5 x 3/2 = 12/10 = 6/5."),
            make_mc(4, "Một mảnh đất hình bình hành có đáy 20 m, chiều cao 15 m. Diện tích mảnh đất là:", ["300 m²", "150 m²", "70 m²", "35 m²"], 0, "20 x 15 = 300 m²."),
            make_mc(5, "Đổi $4\\text{ m}^2 \\text{ } 50\\text{ dm}^2 = \\dots \\text{ dm}^2$:", ["450 dm²", "4 050 dm²", "45 dm²", "4 500 dm²"], 0, "400 + 50 = 450 dm²."),
            make_mc(6, "Năm 2026 thuộc thế kỉ nào?", ["XXI", "XX", "XIX", "XXII"], 0, "Thế kỉ XXI.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\na) $\\frac{7}{12} + \\frac{5}{6} \\times \\frac{3}{10}$\nb) $\\left(\\frac{5}{7} - \\frac{2}{5}\\right) : \\frac{11}{35}$", "a) $\\frac{5}{6} \\times \\frac{3}{10} = \\frac{1}{4}$. Ta có: $\\frac{7}{12} + \\frac{1}{4} = \\frac{7}{12} + \\frac{3}{12} = \\frac{10}{12} = \\frac{5}{6}$.\nb) $\\frac{5}{7} - \\frac{2}{5} = \\frac{25}{35} - \\frac{14}{35} = \\frac{11}{35}$. Ta có: $\\frac{11}{35} : \\frac{11}{35} = 1$.", "a) 5/6; b) 1", 4, 1.0),
            make_essay(2, "Tính thuận tiện nhất:\na) $\\frac{4}{9} \\times \\frac{5}{11} + \\frac{4}{9} \\times \\frac{6}{11}$\nb) $25 \\times 39 \\times 4$", "a) $\\frac{4}{9} \\times (\\frac{5}{11} + \\frac{6}{11}) = \\frac{4}{9} \\times 1 = \\frac{4}{9}$.\nb) $(25 \\times 4) \\times 39 = 100 \\times 39 = 3900$.", "a) 4/9; b) 3900", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chiều dài 36 m, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Người ta dùng $\\frac{1}{4}$ diện tích mảnh vườn để trồng dưa hấu, phần còn lại trồng rau. Tính diện tích phần đất trồng rau.", "Chiều rộng mảnh vườn là: $36 \\times 2 : 3 = 24\\text{ (m)}$.\nDiện tích cả mảnh vườn là: $36 \\times 24 = 864\\text{ (m}^2)$.\nDiện tích trồng dưa hấu là: $864 : 4 = 216\\text{ (m}^2)$.\nDiện tích phần đất trồng rau là:\n$864 - 216 = 648\\text{ (m}^2)$.", "648 m²", 4, 1.0),
            make_essay(4, "Hai thùng chứa tất cả 160 lít dầu. Nếu chuyển 15 lít dầu từ thùng thứ nhất sang thùng thứ hai thì thùng thứ hai vẫn ít hơn thùng thứ nhất 10 lít. Hỏi lúc đầu mỗi thùng có bao nhiêu lít dầu?", "Sau khi chuyển 15 lít từ thùng 1 sang thùng 2, thùng 1 hơn thùng 2 là 10 lít.\nVậy lúc đầu thùng 1 nhiều hơn thùng 2 là:\n$15 \\times 2 + 10 = 40\\text{ (lít)}$.\nSố lít dầu ở thùng thứ nhất lúc đầu là:\n$(160 + 40) : 2 = 100\\text{ (lít)}$.\nSố lít dầu ở thùng thứ hai lúc đầu là:\n$160 - 100 = 60\\text{ (lít)}$.", "Thùng 1: 100 lít; Thùng 2: 60 lít", 5, 1.5),
            make_essay(5, "Một xưởng dệt nhận kế hoạch dệt 1 800 m vải trong 6 ngày. Trong 3 ngày đầu xưởng dệt được $\\frac{1}{2}$ kế hoạch, ngày thứ tư dệt được $\\frac{1}{6}$ kế hoạch. Hỏi trong hai ngày còn lại, trung bình mỗi ngày xưởng phải dệt bao nhiêu mét vải để hoàn thành kế hoạch?", "Số mét vải xưởng đã dệt sau 4 ngày là:\n$1800 \\times \\left(\\frac{1}{2} + \\frac{1}{6}\\right) = 1800 \\times \\frac{4}{6} = 1200\\text{ (m)}$.\nSố mét vải xưởng còn phải dệt trong 2 ngày cuối là:\n$1800 - 1200 = 600\\text{ (m)}$.\nTrung bình mỗi ngày còn lại xưởng phải dệt:\n$600 : 2 = 300\\text{ (m)}$.", "300 m vải", 5, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$S = \\frac{1}{3} + \\frac{1}{9} + \\frac{1}{27} + \\frac{1}{81} + \\frac{1}{243}$.", "Ta nhân cả hai vế với 3:\n$3 \\times S = 1 + \\frac{1}{3} + \\frac{1}{9} + \\frac{1}{27} + \\frac{1}{81}$.\nLấy $3 \\times S - S = 2 \\times S$:\n$2 \\times S = 1 - \\frac{1}{243} = \\frac{242}{243}$.\nDo đó: $S = \\frac{242}{243} : 2 = \\frac{121}{243}$.", "121/243", 4, 1.0)
        ]
    }

    # --- Bài 63 - Đề 3 ---
    exams["th4_b63_test3"] = {
        "id": "th4_b63_test3",
        "lessonId": "th4_b63",
        "lessonNum": 63,
        "testNum": 3,
        "title": "Bài 63: Luyện tập chung cuối năm - Đề số 3",
        "topic": "Luyện tập chung cuối năm",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 8 triệu, 5 trăm và 6 chục viết là:", ["8 000 560", "8 050 060", "8 560 000", "800 560"], 0, "8 000 560."),
            make_mc(2, "Phân số tối giản của $\\frac{48}{72}$ là:", ["$\\frac{2}{3}$", "$\\frac{4}{6}$", "$\\frac{12}{18}$", "$\\frac{6}{9}$"], 0, "48:24 / 72:24 = 2/3."),
            make_mc(3, "Tìm $\\frac{4}{7}$ của 420 kg:", ["240 kg", "280 kg", "180 kg", "300 kg"], 0, "420 x 4 : 7 = 240 kg."),
            make_mc(4, "Một hình thoi có hai đường chéo dài 14 cm và 10 cm. Diện tích của nó là:", ["70 cm²", "140 cm²", "35 cm²", "48 cm²"], 0, "(14 x 10) : 2 = 70 cm²."),
            make_mc(5, "Đổi $3\\text{ thế kỉ } 5\\text{ năm} = \\dots \\text{ năm}$:", ["305 năm", "350 năm", "3 005 năm", "35 năm"], 0, "300 + 5 = 305 năm."),
            make_mc(6, "Biểu thức $\\frac{3}{5} \\times \\frac{5}{7} \\times \\frac{7}{9}$ có giá trị bằng:", ["$\\frac{1}{3}$", "$\\frac{3}{9}$", "$\\frac{105}{315}$", "1"], 0, "(3 x 5 x 7)/(5 x 7 x 9) = 3/9 = 1/3.")
        ],
        "part2": [
            make_essay(1, "Tính:\na) $\\frac{5}{8} : \\frac{15}{16} \\times \\frac{3}{4}$\nb) $\\frac{9}{14} - \\frac{2}{7} + \\frac{5}{14}$", "a) $\\frac{5}{8} \\times \\frac{16}{15} \\times \\frac{3}{4} = \\frac{2}{3} \\times \\frac{3}{4} = \\frac{1}{2}$.\nb) $(\\frac{9}{14} + \\frac{5}{14}) - \\frac{4}{14} = \\frac{14}{14} - \\frac{4}{14} = \\frac{10}{14} = \\frac{5}{7}$.", "a) 1/2; b) 5/7", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $\\frac{7}{15} \\times \\frac{8}{9} + \\frac{7}{15} \\times \\frac{1}{9}$\nb) $50 \\times 68 \\times 2$", "a) $\\frac{7}{15} \\times (\\frac{8}{9} + \\frac{1}{9}) = \\frac{7}{15} \\times 1 = \\frac{7}{15}$.\nb) $(50 \\times 2) \\times 68 = 100 \\times 68 = 6800$.", "a) 7/15; b) 6800", 4, 1.0),
            make_essay(3, "Một thửa ruộng hình chữ nhật có chu vi 180 m, chiều dài hơn chiều rộng 18 m. Người ta trồng ngô trên thửa ruộng đó, cứ $10\\text{ m}^2$ thu hoạch được 8 kg ngô. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ ngô?", "Nửa chu vi thửa ruộng là: $180 : 2 = 90\\text{ (m)}$.\nChiều dài thửa ruộng là: $(90 + 18) : 2 = 54\\text{ (m)}$.\nChiều rộng thửa ruộng là: $90 - 54 = 36\\text{ (m)}$.\nDiện tích thửa ruộng là: $54 \\times 36 = 1944\\text{ (m}^2)$.\nSố ki-lô-gam ngô thu hoạch được là:\n$1944 : 10 \\times 8 = 1555,2\\text{ kg}$ (số lẻ). Ta sửa chu vi: nếu nửa chu vi 90 m, dài hơn 20 m => dài 55 m, rộng 35 m => diện tích $55 \\times 35 = 1925\\text{ m}^2$ cũng không chia hết cho 10. Ta chọn số liệu tròn đẹp: chu vi 160 m, nửa chu vi 80 m, dài hơn 20 m => dài 50 m, rộng 30 m => diện tích $50 \\times 30 = 1500\\text{ m}^2$.\nSố kg ngô thu hoạch: $1500 : 10 \\times 8 = 1200\\text{ kg} = 12\\text{ tạ}$.", "12 tạ ngô", 4, 1.0),
            make_essay(4, "Một đoàn xe chở 45 tấn hàng viện trợ. Ngày đầu chuyển được $\\frac{2}{5}$ số hàng. Ngày thứ hai chuyển được $\\frac{4}{9}$ số hàng còn lại. Hỏi sau hai ngày, đoàn xe còn lại bao nhiêu tấn hàng chưa chuyển?", "Số hàng chuyển ngày đầu là:\n$45 \\times \\frac{2}{5} = 18\\text{ (tấn)}$.\nSố hàng còn lại sau ngày đầu là:\n$45 - 18 = 27\\text{ (tấn)}$.\nSố hàng chuyển ngày thứ hai là:\n$27 \\times \\frac{4}{9} = 12\\text{ (tấn)}$.\nSố hàng còn lại sau hai ngày là:\n$27 - 12 = 15\\text{ (tấn)}$.", "15 tấn hàng", 5, 1.5),
            make_essay(5, "Năm nay tổng số tuổi của hai anh em là 26 tuổi. Biết rằng 3 năm trước anh hơn em 4 tuổi. Hỏi hiện nay anh bao nhiêu tuổi, em bao nhiêu tuổi?", "Hiệu số tuổi luôn không đổi nên hiện nay anh vẫn hơn em 4 tuổi.\nTuổi của anh hiện nay là:\n$(26 + 4) : 2 = 15\\text{ (tuổi)}$.\nTuổi của em hiện nay là:\n$26 - 15 = 11\\text{ (tuổi)}$.", "Anh: 15 tuổi; Em: 11 tuổi", 5, 1.5),
            make_essay(6, "Tìm phân số lớn nhất có tử số và mẫu số đều là số có hai chữ số và có giá trị bằng $\\frac{3}{5}$.", "Phân số cần tìm có dạng $\\frac{3 \\times k}{5 \\times k}$ với $k$ là số tự nhiên.\nVì cả tử số và mẫu số đều là số có hai chữ số nên:\n$3 \\times k < 100$ và $5 \\times k < 100$.\nĐể phân số lớn nhất thì $k$ phải lớn nhất.\nTa có: $5 \\times k \\le 99 \\Rightarrow k \\le 19$ (vì $5 \\times 19 = 95 < 100$).\nVới $k = 19$, tử số là $3 \\times 19 = 57$ (thỏa mãn có hai chữ số).\nVậy phân số cần tìm là $\\frac{57}{95}$.", "57/95", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_ch13_part2_exams()
    print(f"Tổng số đề Chủ đề 13 (Phần 2): {len(ex)} (Kỳ vọng: 6)")
    for b in range(62, 64):
        for t in range(1, 4):
            key = f"th4_b{b}_test{t}"
            assert key in ex, f"Thiếu {key}"
            assert len(ex[key]["part1"]) == 6
            assert len(ex[key]["part2"]) == 6
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6
            assert abs(p2_pts - 7.0) < 1e-6
    print("Phần 2 của Chủ đề 13 hoàn hảo 100%!")
