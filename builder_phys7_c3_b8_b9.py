# -*- coding: utf-8 -*-
"""
CHƯƠNG III: TỐC ĐỘ - BÀI 8 & BÀI 9 (6 ĐỀ ĐỘC LẬP 100%)
- phys7_c3_b8: Bài 8: Tốc độ chuyển động (3 đề: test1, test2, test3)
- phys7_c3_b9: Bài 9: Đo tốc độ (3 đề: test1, test2, test3)
Không trùng lặp, không tiền tố "Đề X - "
"""

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": prompt.strip(),
        "statements": [
            {"subId": s[0], "text": s[1].strip(), "correct": s[2]} for s in statements
        ],
        "explanation": explanation.strip()
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "correctAnswer": str(answer).strip(),
        "explanation": explanation.strip()
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

b8_b9_exams = {}

# =========================================================================
# BÀI 8: TỐC ĐỘ CHUYỂN ĐỘNG (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b8_b9_exams["phys7_c3_b8_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 8: Tốc độ chuyển động - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b8", "lessonName": "Bài 8: Tốc độ chuyển động",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Tốc độ chuyển động của một vật cho biết:", ["Mức độ nhanh hay chậm của chuyển động", "Quãng đường dài hay ngắn mà vật đã đi", "Thời gian vật thực hiện chuyển động", "Hướng chuyển động của vật trong không gian"], 0, "Tốc độ là đại lượng đặc trưng cho mức độ nhanh hay chậm của chuyển động."),
        make_mc(2, "Nhận biết", "Công thức tính tốc độ khi biết quãng đường s và thời gian t là:", ["v = s / t", "v = s × t", "v = t / s", "v = s + t"], 0, "Công thức tính tốc độ: v = s / t."),
        make_mc(3, "Nhận biết", "Đơn vị hợp pháp để đo tốc độ trong hệ đơn vị đo lường quốc tế (SI) là:", ["Mét trên giây (m/s)", "Kilômét trên giờ (km/h)", "Centimét trên giây (cm/s)", "Milimét trên phút (mm/min)"], 0, "Trong hệ SI, đơn vị hợp pháp của tốc độ là mét trên giây (m/s)."),
        make_mc(4, "Nhận biết", "Thiết bị đo gắn trực tiếp trên bảng điều khiển xe máy, ô tô để hiển thị tốc độ tức thời là:", ["Tốc kế (speedometer)", "Nhiệt kế", "Vôn kế", "Ampe kế"], 0, "Tốc kế dùng để đo trực tiếp tốc độ chuyển động tức thời của phương tiện."),
        make_mc(5, "Nhận biết", "Tốc độ truyền ánh sáng trong môi trường chân không xấp xỉ bằng:", ["300.000 km/s", "340 m/s", "1.500 m/s", "1.000 km/h"], 0, "Tốc độ ánh sáng trong chân không là c ≈ 300.000 km/s = 3.10^8 m/s."),
        make_mc(6, "Nhận biết", "Chuyển động đều là chuyển động có đặc điểm nào sau đây?", ["Tốc độ có độ lớn không đổi theo thời gian", "Tốc độ tăng dần đều đặn", "Tốc độ giảm dần về 0", "Quãng đường đi được luôn bằng 0"], 0, "Chuyển động đều là chuyển động có tốc độ không thay đổi theo thời gian."),
        make_mc(7, "Thông hiểu", "Đổi 36 km/h sang đơn vị m/s ta được kết quả là:", ["10 m/s", "3,6 m/s", "100 m/s", "360 m/s"], 0, "1 km/h = 1/3,6 m/s => 36 km/h = 36 / 3,6 = 10 m/s."),
        make_mc(8, "Thông hiểu", "Một người đi xe đạp đi được quãng đường 12 km trong thời gian 40 phút. Tốc độ của người đó là:", ["18 km/h", "12 km/h", "15 km/h", "20 km/h"], 0, "40 phút = 2/3 giờ. v = 12 / (2/3) = 18 km/h."),
        make_mc(9, "Thông hiểu", "Một ô tô chạy trên cao tốc với tốc độ 90 km/h. Trong thời gian 20 phút, xe đi được quãng đường là:", ["30 km", "45 km", "18 km", "25 km"], 0, "20 phút = 1/3 h. s = 90 × (1/3) = 30 km."),
        make_mc(10, "Thông hiểu", "Vận động viên điền kinh hoàn thành cự li chạy 100 m trong thời gian 10 giây. Tốc độ trung bình là:", ["10 m/s", "1 m/s", "100 m/s", "36 m/s"], 0, "v = s / t = 100 / 10 = 10 m/s."),
        make_mc(11, "Thông hiểu", "Trong các phương tiện sau, phương tiện nào có tốc độ chuyển động trung bình lớn nhất?", ["Máy bay thương mại phản lực", "Tàu hỏa thông thường", "Xe ô tô con trên quốc lộ", "Xe máy phân khối lớn"], 0, "Máy bay thương mại phản lực bay khoảng 800 - 900 km/h, lớn nhất trong các phương tiện trên."),
        make_mc(12, "Thông hiểu", "Hai người cùng xuất phát đi bộ trên một đoạn đường dài 1,2 km. Người A mất 15 phút, người B mất 20 phút. Nhận xét nào đúng?", ["Người A chuyển động nhanh hơn người B", "Người B chuyển động nhanh hơn người A", "Hai người chuyển động nhanh như nhau", "Không thể so sánh được"], 0, "Cùng quãng đường, người A mất ít thời gian hơn nên đi nhanh hơn.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các đơn vị và quy tắc chuyển đổi của tốc độ chuyển động:", [
            ("a", "1 m/s tương đương với 3,6 km/h.", True),
            ("b", "Đơn vị km/h thường dùng trong giao thông đường bộ ở nước ta.", True),
            ("c", "Để đổi từ m/s sang km/h ta lấy giá trị nhân với 3,6.", True),
            ("d", "Tốc độ 15 m/s nhỏ hơn tốc độ 40 km/h.", False)
        ], "15 m/s = 54 km/h > 40 km/h."),
        make_tf(2, "Thông hiểu", "Xét tính chất của các chuyển động trong đời sống:", [
            ("a", "Chuyển động của đầu kim đồng hồ chạy bình thường là chuyển động đều.", True),
            ("b", "Chuyển động của xe buýt khi đón và trả khách là chuyển động không đều.", True),
            ("c", "Tốc kế trên xe máy hiển thị tốc độ trung bình của cả chuyến đi.", False),
            ("d", "Khi đạp xe lên dốc, tốc độ của xe thường giảm dần.", True)
        ], "Tốc kế hiển thị tốc độ tức thời tại thời điểm đang chạy, không phải tốc độ trung bình."),
        make_tf(3, "Vận dụng", "Một xe khách đi từ bến A đến bến B dài 120 km trong thời gian 2,5 giờ, sau đó dừng nghỉ 30 phút rồi đi tiếp 60 km trong 1 giờ:", [
            ("a", "Tốc độ của xe ở chặng đầu tiên là 48 km/h.", True),
            ("b", "Tốc độ của xe ở chặng thứ hai là 60 km/h.", True),
            ("c", "Tổng quãng đường xe đã đi là 180 km.", True),
            ("d", "Tốc độ trung bình trên toàn bộ chuyến đi kể cả thời gian nghỉ là 50 km/h.", False)
        ], "v1 = 120 / 2,5 = 48 km/h. v2 = 60 / 1 = 60 km/h. Tổng thời gian cả nghỉ = 2,5 + 0,5 + 1 = 4h => v_tb = 180 / 4 = 45 km/h."),
        make_tf(4, "Vận dụng", "Vận động viên bơi lội tập luyện trong hồ bơi tiêu chuẩn dài 50 m:", [
            ("a", "Lượt đi 50 m mất 25 giây, tốc độ bơi là 2 m/s.", True),
            ("b", "Tốc độ 2 m/s tương đương với 7,2 km/h.", True),
            ("c", "Lượt về 50 m mất 30 giây, tốc độ lượt về nhanh hơn lượt đi.", False),
            ("d", "Tốc độ trung bình cả đi và về là xấp xỉ 1,82 m/s.", True)
        ], "Lượt về v = 50 / 30 = 1,67 m/s chậm hơn lượt đi 2 m/s. v_tb = 100 / 55 ≈ 1,82 m/s.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đổi 54 km/h sang đơn vị m/s ta được kết quả là bao nhiêu?", "15", "54 / 3,6 = 15 m/s."),
        make_sa(2, "Thông hiểu", "Một người chạy bộ cự li 200 m trong 25 giây. Tốc độ chạy của người đó là bao nhiêu m/s?", "8", "v = 200 / 25 = 8 m/s."),
        make_sa(3, "Vận dụng", "Một ô tô chạy trên cao tốc với tốc độ 90 km/h. Trong thời gian 2 giờ, ô tô đi được quãng đường bao nhiêu km?", "180", "s = 90 × 2 = 180 km."),
        make_sa(4, "Vận dụng", "Một ca nô chuyển động với tốc độ 30 km/h. Để đi hết khúc sông dài 45 km, ca nô mất thời gian bao nhiêu giờ? (Viết dưới dạng số thập phân)", "1.5", "t = 45 / 30 = 1,5 h."),
        make_sa(5, "Vận dụng cao", "Xe buýt đi từ bến A đến bến B dài 24 km hết 40 phút. Tốc độ trung bình của xe buýt là bao nhiêu km/h?", "36", "40 phút = 2/3 h. v = 24 / (2/3) = 36 km/h."),
        make_sa(6, "Vận dụng cao", "Một vận động viên trượt băng di chuyển với tốc độ đều 12 m/s. Trong 15 giây, quãng đường trượt được là bao nhiêu mét?", "180", "s = 12 × 15 = 180 m.")
    ],
    "part4": [
        make_vdc(1, "Hai xe máy xuất phát cùng một lúc từ hai địa điểm A và B cách nhau 120 km đi ngược chiều để gặp nhau. Xe từ A chạy với tốc độ 35 km/h, xe từ B chạy với tốc độ 25 km/h. Sau bao lâu kể từ lúc xuất phát thì hai xe gặp nhau?", ["2 giờ", "1,5 giờ", "2,5 giờ", "3 giờ"], 0, "Thời gian gặp nhau: t = s / (v1 + v2) = 120 / (35 + 25) = 2 giờ."),
        make_vdc(2, "Đoàn tàu hỏa dài 120 m vượt qua một cây cầu dài 480 m với tốc độ không đổi 36 km/h (10 m/s). Thời gian từ lúc đầu tàu bắt đầu đi vào cầu đến lúc toa cuối cùng rời khỏi cầu là bao nhiêu giây?", ["60 giây", "48 giây", "12 giây", "50 giây"], 0, "Tổng quãng đường tàu đi để qua hết cầu: s = 480 + 120 = 600 m. t = 600 / 10 = 60 s."),
        make_vdc(3, "Một người đi xe đạp trên đoạn đường dốc. Nửa quãng đường đầu người đó đi với tốc độ 12 km/h, nửa quãng đường sau đi với tốc độ 24 km/h. Tốc độ trung bình của người đó trên toàn bộ quãng đường là:", ["16 km/h", "18 km/h", "20 km/h", "15 km/h"], 0, "v_tb = 2v1v2 / (v1 + v2) = 2 × 12 × 24 / (12 + 24) = 576 / 36 = 16 km/h."),
        make_vdc(4, "Một chiếc thuyền máy chạy xuôi dòng một khúc sông dài 36 km mất 1,5 giờ, sau đó ngược dòng trở về mất 2 giờ. Biết công suất động cơ không đổi, tốc độ của dòng nước so với bờ sông là:", ["3 km/h", "21 km/h", "4 km/h", "1,5 km/h"], 0, "v_xuôi = 36 / 1,5 = 24 km/h; v_ngược = 36 / 2 = 18 km/h. v_nước = (24 - 18) / 2 = 3 km/h.")
    ]
}

# --- ĐỀ 2 ---
b8_b9_exams["phys7_c3_b8_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 8: Tốc độ chuyển động - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b8", "lessonName": "Bài 8: Tốc độ chuyển động",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Muốn so sánh hai chuyển động xem chuyển động nào nhanh hơn, người ta dựa vào:", ["Quãng đường đi được trong cùng một khoảng thời gian", "Chiều dài của đường đi", "Thời điểm bắt đầu xuất phát", "Khối lượng của vật đang chuyển động"], 0, "So sánh quãng đường vật đi được trong cùng một đơn vị thời gian (tốc độ)."),
        make_mc(2, "Nhận biết", "Thương số giữa quãng đường s và khoảng thời gian t đi hết quãng đường đó gọi là:", ["Tốc độ chuyển động", "Gia tốc chuyển động", "Lực tác dụng", "Độ dời vị trí"], 0, "Thương số s/t là tốc độ chuyển động."),
        make_mc(3, "Nhận biết", "Kí hiệu của tốc độ trong các công thức vật lý thường dùng là:", ["v", "s", "t", "m"], 0, "Tốc độ kí hiệu là v (velocity/speed)."),
        make_mc(4, "Nhận biết", "Đơn vị nào sau đây KHÔNG phải là đơn vị đo tốc độ?", ["m.s", "m/s", "km/h", "cm/s"], 0, "m.s là tích của mét và giây, không phải đơn vị tốc độ."),
        make_mc(5, "Nhận biết", "Tốc độ âm thanh truyền trong không khí ở nhiệt độ phòng (20 °C) xấp xỉ khoảng:", ["340 m/s", "300.000 km/s", "1.500 m/s", "100 km/h"], 0, "Tốc độ âm trong không khí ở 20 °C là khoảng 340 m/s."),
        make_mc(6, "Nhận biết", "Chuyển động có tốc độ thay đổi liên tục theo thời gian được gọi là:", ["Chuyển động không đều", "Chuyển động đều", "Chuyển động đứng yên", "Chuyển động tuần hoàn đều"], 0, "Chuyển động có tốc độ biến đổi gọi là chuyển động không đều."),
        make_mc(7, "Thông hiểu", "Đổi 15 m/s sang đơn vị km/h ta được kết quả là:", ["54 km/h", "15 km/h", "36 km/h", "45 km/h"], 0, "15 × 3,6 = 54 km/h."),
        make_mc(8, "Thông hiểu", "Một con báo săn mồi chạy với tốc độ 108 km/h. Tốc độ này tính theo đơn vị m/s là:", ["30 m/s", "36 m/s", "25 m/s", "40 m/s"], 0, "108 / 3,6 = 30 m/s."),
        make_mc(9, "Thông hiểu", "Một người đi bộ đi được quãng đường 600 m trong 5 phút. Tốc độ đi bộ của người đó là:", ["2 m/s", "120 m/s", "0,5 m/s", "5 m/s"], 0, "5 phút = 300 s. v = 600 / 300 = 2 m/s."),
        make_mc(10, "Thông hiểu", "Một máy bay bay từ Hà Nội vào Đà Nẵng dài 600 km hết 45 phút (0,75 giờ). Tốc độ của máy bay là:", ["800 km/h", "600 km/h", "750 km/h", "900 km/h"], 0, "v = 600 / 0,75 = 800 km/h."),
        make_mc(11, "Thông hiểu", "Xe máy chạy với tốc độ 48 km/h. Để đi quãng đường 72 km, xe máy cần thời gian là:", ["1,5 giờ", "2,0 giờ", "1,2 giờ", "1,8 giờ"], 0, "t = s / v = 72 / 48 = 1,5 giờ."),
        make_mc(12, "Thông hiểu", "Hiện tượng nhìn thấy tia sét trước khi nghe thấy tiếng sấm là do:", ["Tốc độ ánh sáng lớn hơn rất nhiều tốc độ âm thanh", "Tia sét xảy ra trước tiếng sấm một khoảng thời gian", "Mắt người nhìn nhanh hơn tai người nghe", "Âm thanh bị cản trở bởi mây"], 0, "Tốc độ ánh sáng (300.000 km/s) lớn hơn rất nhiều tốc độ âm thanh (340 m/s).")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét mối quan hệ giữa các đại lượng s, v và t trong chuyển động:", [
            ("a", "Với cùng một quãng đường, thời gian chuyển động tỉ lệ nghịch với tốc độ.", True),
            ("b", "Trong cùng một khoảng thời gian, quãng đường đi được tỉ lệ thuận với tốc độ.", True),
            ("c", "Công thức xác định thời gian chuyển động là t = v / s.", False),
            ("d", "Nếu tăng tốc độ lên gấp đôi thì thời gian đi hết cùng một quãng đường sẽ giảm một nửa.", True)
        ], "Công thức đúng là t = s / v, câu c sai."),
        make_tf(2, "Thông hiểu", "Xét chuyển động của các phương tiện trong giao thông thực tế:", [
            ("a", "Xe chạy trên đường cao tốc thường duy trì tốc độ cao và ổn định hơn trong nội đô.", True),
            ("b", "Khi qua khúc cua hoặc ngã tư, tài xế phải giảm tốc độ để đảm bảo an toàn.", True),
            ("c", "Tốc độ trung bình trên cả hành trình luôn luôn bằng trung bình cộng vận tốc đầu và vận tốc cuối.", False),
            ("d", "Tốc độ tức thời là tốc độ tại một thời điểm hoặc một vị trí xác định.", True)
        ], "Tốc độ trung bình bằng tổng quãng đường chia cho tổng thời gian, không đơn thuần là trung bình cộng hai vận tốc."),
        make_tf(3, "Vận dụng", "Một người đạp xe đường trường thực hiện lộ trình qua hai đoạn đường:", [
            ("a", "Đoạn 1 leo dốc dài 10 km chạy với tốc độ 15 km/h mất 40 phút.", True),
            ("b", "Đoạn 2 đổ dốc dài 15 km chạy với tốc độ 45 km/h mất 20 phút.", True),
            ("c", "Tổng thời gian đi hết cả hai đoạn dốc là 1 giờ.", True),
            ("d", "Tốc độ trung bình trên toàn tuyến đường bằng 30 km/h.", False)
        ], "Tổng quãng đường = 10 + 15 = 25 km, tổng thời gian = 40p + 20p = 1h => v_tb = 25 / 1 = 25 km/h."),
        make_tf(4, "Vận dụng", "Đội tuyển chạy tiếp sức 4 x 100 m nam của trường tham gia thi đấu:", [
            ("a", "Tổng cự li mà cả 4 thành viên hoàn thành là 400 m.", True),
            ("b", "Thời gian thi đấu của toàn đội là 48 giây.", True),
            ("c", "Tốc độ trung bình của đội đạt xấp xỉ 8,33 m/s.", True),
            ("d", "Cả 4 vận động viên đều chạy với tốc độ hoàn toàn giống nhau ở mọi thời điểm.", False)
        ], "Mỗi vận động viên có thể lực và tốc độ xuất phát, bứt tốc khác nhau.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đổi 72 km/h sang đơn vị m/s được kết quả là bao nhiêu?", "20", "72 / 3,6 = 20 m/s."),
        make_sa(2, "Thông hiểu", "Vận động viên bơi cự li 100 m mất thời gian 50 giây. Tốc độ bơi trung bình là bao nhiêu m/s?", "2", "v = 100 / 50 = 2 m/s."),
        make_sa(3, "Vận dụng", "Tàu hỏa chạy đều với tốc độ 45 km/h trong thời gian 3 giờ. Quãng đường tàu đi được là bao nhiêu km?", "135", "s = 45 × 3 = 135 km."),
        make_sa(4, "Vận dụng", "Chiếc xe máy đi quãng đường 60 km hết 1,2 giờ. Tốc độ của xe máy là bao nhiêu km/h?", "50", "v = 60 / 1,2 = 50 km/h."),
        make_sa(5, "Vận dụng cao", "Ánh sáng truyền từ Mặt Trời đến Trái Đất mất khoảng 500 giây với tốc độ 300.000 km/s. Khoảng cách đó bằng bao nhiêu triệu km?", "150", "s = 300.000 × 500 = 150.000.000 km = 150 triệu km."),
        make_sa(6, "Vận dụng cao", "Một con tàu vũ trụ chuyển động với tốc độ 8 km/s. Trong thời gian 1 phút, con tàu đi được quãng đường bao nhiêu km?", "480", "1 phút = 60 s. s = 8 × 60 = 480 km.")
    ],
    "part4": [
        make_vdc(1, "Hai xe ô tô cùng khởi hành lúc 6h00 sáng từ hai địa điểm A và B cách nhau 120 km đi cùng chiều nhau (xe từ A đuổi theo xe từ B). Xe A chạy với tốc độ 60 km/h, xe B chạy với tốc độ 40 km/h. Hai xe gặp nhau vào thời điểm nào trong ngày?", ["12h00 trưa", "11h00 trưa", "10h30 sáng", "14h00 chiều"], 0, "Thời gian đuổi kịp: t = 120 / (60 - 40) = 6 giờ. Thời điểm gặp nhau: 6h00 + 6h = 12h00."),
        make_vdc(2, "Một tài xế lái ô tô đi 1/3 quãng đường đầu với tốc độ 30 km/h và 2/3 quãng đường còn lại với tốc độ 60 km/h. Tốc độ trung bình của ô tô trên cả chặng đường là:", ["45 km/h", "50 km/h", "40 km/h", "48 km/h"], 0, "t1 = (s/3)/30 = s/90; t2 = (2s/3)/60 = s/90. Tổng t = 2s/90 = s/45 => v_tb = s / (s/45) = 45 km/h."),
        make_vdc(3, "Một người đứng bên đường ray quan sát thấy một đoàn tàu hỏa chạy qua trước mặt mình mất 12 giây. Biết đoàn tàu dài 180 m. Tốc độ chuyển động của đoàn tàu tính ra km/h là:", ["54 km/h", "36 km/h", "60 km/h", "72 km/h"], 0, "v = 180 / 12 = 15 m/s = 15 × 3,6 = 54 km/h."),
        make_vdc(4, "Một người bơi xuôi dòng nước từ bến A đến bến B mất 40 phút và bơi ngược dòng từ B về A mất 60 phút. Nếu người đó thả trôi theo dòng nước từ A đến B thì mất thời gian bao nhiêu phút?", ["240 phút", "100 phút", "120 phút", "180 phút"], 0, "1/t_xuôi = 1/40; 1/t_ngược = 1/60 => 1/t_nước = (1/40 - 1/60)/2 = (1/120)/2 = 1/240 => t_trôi = 240 phút.")
    ]
}

# --- ĐỀ 3 ---
b8_b9_exams["phys7_c3_b8_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 8: Tốc độ chuyển động - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b8", "lessonName": "Bài 8: Tốc độ chuyển động",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Để xác định tốc độ chuyển động của một vật, ta cần đo hai đại lượng nào?", ["Quãng đường và thời gian", "Khối lượng và thể tích", "Nhiệt độ và áp suất", "Chiều dài và diện tích"], 0, "Cần đo quãng đường vật đi được và thời gian đi hết quãng đường đó."),
        make_mc(2, "Nhận biết", "Trong các công thức sau, công thức nào dùng để tính thời gian chuyển động?", ["t = s / v", "t = s × v", "t = v / s", "t = v - s"], 0, "Thời gian chuyển động: t = s / v."),
        make_mc(3, "Nhận biết", "Khi nói tốc độ của ô tô là 60 km/h, điều đó có ý nghĩa là:", ["Nếu giữ nguyên tốc độ, trong 1 giờ ô tô sẽ đi được 60 km", "Ô tô luôn đi được đúng 60 km trong mọi trường hợp", "Ô tô chỉ có thể chạy trong vòng 1 giờ", "Ô tô đã đi được quãng đường dài 60 km"], 0, "Tốc độ 60 km/h nghĩa là mỗi giờ xe đi được 60 km nếu chuyển động đều."),
        make_mc(4, "Nhận biết", "Đơn vị đo tốc độ thường dùng trong ngành hàng hải và hàng không quốc tế là:", ["Hải lí trên giờ (nút - knot)", "Mét trên phút", "Kilômét trên giây", "Dặm trên giây"], 0, "Nút (knot) là đơn vị đo tốc độ bằng 1 hải lí/giờ (xấp xỉ 1,852 km/h)."),
        make_mc(5, "Nhận biết", "Tốc độ chuyển động của Trái Đất quay xung quanh Mặt Trời xấp xỉ khoảng:", ["30 km/s", "300 m/s", "300.000 km/s", "100 km/h"], 0, "Trái Đất quay quanh Mặt Trời với tốc độ khoảng 29,8 km/s ≈ 30 km/s."),
        make_mc(6, "Nhận biết", "Chuyển động của một hòn đá rơi tự do từ trên cao xuống đất có tốc độ:", ["Tăng dần theo thời gian", "Không đổi theo thời gian", "Giảm dần về 0", "Luôn bằng 0"], 0, "Vật rơi tự do chuyển động nhanh dần đều dưới tác dụng của trọng lực."),
        make_mc(7, "Thông hiểu", "Đổi 12 m/s sang đơn vị km/h ta được kết quả là:", ["43,2 km/h", "36,0 km/h", "24,0 km/h", "48,5 km/h"], 0, "12 × 3,6 = 43,2 km/h."),
        make_mc(8, "Thông hiểu", "Một người đi xe đạp đi quãng đường 6 km trong thời gian 24 phút. Tốc độ của người đó là:", ["15 km/h", "12 km/h", "18 km/h", "20 km/h"], 0, "24 phút = 0,4 h. v = 6 / 0,4 = 15 km/h."),
        make_mc(9, "Thông hiểu", "Một xe tải chạy trên quốc lộ với tốc độ 60 km/h. Trong thời gian 45 phút, xe tải đi được:", ["45 km", "40 km", "50 km", "30 km"], 0, "45 phút = 0,75 h. s = 60 × 0,75 = 45 km."),
        make_mc(10, "Thông hiểu", "Để đi hết quãng đường 180 km với tốc độ đều 45 km/h, xe ô tô cần khoảng thời gian là:", ["4 giờ", "3,5 giờ", "5 giờ", "4,5 giờ"], 0, "t = s / v = 180 / 45 = 4 giờ."),
        make_mc(11, "Thông hiểu", "Chim cắt cổ điển lao xuống săn mồi có thể đạt tốc độ 324 km/h. Tốc độ này tính theo m/s là:", ["90 m/s", "80 m/s", "100 m/s", "75 m/s"], 0, "324 / 3,6 = 90 m/s."),
        make_mc(12, "Thông hiểu", "Một người đi xe máy đi 20 km đầu hết 30 phút, 15 km sau hết 20 phút. Tốc độ trung bình trên toàn tuyến là:", ["42 km/h", "35 km/h", "40 km/h", "45 km/h"], 0, "Tổng s = 35 km, tổng t = 50 phút = 5/6 h => v_tb = 35 / (5/6) = 42 km/h.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất và phương pháp xác định tốc độ:", [
            ("a", "Tốc độ trung bình phản ánh mức độ nhanh chậm tính chung cho cả một quãng đường.", True),
            ("b", "Tốc độ tức thời có thể thay đổi liên tục trên từng đoạn đường nhỏ.", True),
            ("c", "Khi vật chuyển động đều, tốc độ tức thời tại mọi điểm đều bằng tốc độ trung bình.", True),
            ("d", "Tốc độ của vật chuyển động không bao giờ phụ thuộc vào mốc thời gian đã chọn.", True)
        ], "Các ý đều chính xác về mặt định nghĩa vật lý."),
        make_tf(2, "Thông hiểu", "So sánh tốc độ chuyển động trong thế giới tự nhiên và kĩ thuật:", [
            ("a", "Tàu đệm từ Maglev có thể chạy với tốc độ trên 500 km/h.", True),
            ("b", "Vệ tinh nhân tạo bay quanh Trái Đất có tốc độ vũ trụ cấp 1 xấp xỉ 7,9 km/s.", True),
            ("c", "Người đi bộ thông thường có tốc độ khoảng 4 đến 5 m/s.", False),
            ("d", "Vận động viên điền kinh chạy cự li ngắn 100 m có thể đạt tốc độ trên 10 m/s.", True)
        ], "Người đi bộ thông thường chỉ có tốc độ khoảng 1,2 đến 1,4 m/s (4 đến 5 km/h), không phải 4 đến 5 m/s."),
        make_tf(3, "Vận dụng", "Chuyến hành trình của một gia đình đi ô tô từ Hà Nội về quê nghỉ mát:", [
            ("a", "Gia đình xuất phát lúc 6h30 và đến nơi lúc 9h00, tổng thời gian là 2,5 giờ.", True),
            ("b", "Quãng đường cả chuyến đi dài 125 km.", True),
            ("c", "Tốc độ trung bình tính cho cả chuyến đi là 50 km/h.", True),
            ("d", "Nếu gia đình dừng ăn sáng mất 30 phút giữa đường, tốc độ xe chạy thực tế là 62,5 km/h.", True)
        ], "Thời gian xe thực sự lăn bánh = 2,5 - 0,5 = 2h => v_thực = 125 / 2 = 62,5 km/h."),
        make_tf(4, "Vận dụng", "Thang máy của tòa chung cư 30 tầng hoạt động phục vụ cư dân:", [
            ("a", "Thang máy đi từ tầng 1 lên tầng 30 có độ cao 90 m mất thời gian 30 giây.", True),
            ("b", "Tốc độ trung bình của thang máy là 3 m/s.", True),
            ("c", "Trong suốt hành trình di chuyển, thang máy luôn chuyển động đều tuyệt đối.", False),
            ("d", "Tốc độ 3 m/s tương đương với 10,8 km/h.", True)
        ], "Thang máy phải tăng tốc khi khởi hành và giảm tốc khi sắp dừng lại, không thể đều tuyệt đối.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đổi 90 km/h sang đơn vị m/s ta được kết quả là bao nhiêu?", "25", "90 / 3,6 = 25 m/s."),
        make_sa(2, "Thông hiểu", "Một người chạy bộ 1500 m trong 5 phút (300 s). Tốc độ chạy trung bình là bao nhiêu m/s?", "5", "v = 1500 / 300 = 5 m/s."),
        make_sa(3, "Vận dụng", "Máy bay chở khách bay với tốc độ 750 km/h trong thời gian 3,2 giờ. Quãng đường bay được là bao nhiêu km?", "2400", "s = 750 × 3,2 = 2400 km."),
        make_sa(4, "Vận dụng", "Một xe máy đi quãng đường 90 km với tốc độ đều 45 km/h. Thời gian xe đi hết quãng đường là bao nhiêu giờ?", "2", "t = 90 / 45 = 2 h."),
        make_sa(5, "Vận dụng cao", "Một giọt mưa rơi đều từ đám mây ở độ cao 600 m xuống mặt đất với tốc độ 6 m/s. Thời gian rơi chạm đất là bao nhiêu giây?", "100", "t = 600 / 6 = 100 s."),
        make_sa(6, "Vận dụng cao", "Một chú thỏ rừng chạy với tốc độ 15 m/s. Trong khoảng thời gian 8 giây, chú thỏ chạy được bao nhiêu mét?", "120", "s = 15 × 8 = 120 m.")
    ],
    "part4": [
        make_vdc(1, "Một người đi xe máy từ A đến B. Nửa quãng đường đầu người đó đi với tốc độ 30 km/h, nửa quãng đường sau đi với tốc độ 50 km/h. Tốc độ trung bình của xe máy trên cả quãng đường AB là bao nhiêu km/h?", ["37,5 km/h", "40 km/h", "35 km/h", "42 km/h"], 0, "v_tb = 2v1v2 / (v1 + v2) = 2 × 30 × 50 / (30 + 50) = 3000 / 80 = 37,5 km/h."),
        make_vdc(2, "Hai người cùng xuất phát từ địa điểm A lúc 8h00 để đi đến địa điểm B cách A 60 km. Người thứ nhất đi xe máy với tốc độ 40 km/h. Người thứ hai đi ô tô với tốc độ 60 km/h. Xe ô tô đến bến B sớm hơn xe máy bao nhiêu phút?", ["30 phút", "20 phút", "15 phút", "45 phút"], 0, "t_xe_máy = 60 / 40 = 1,5 h = 90 phút. t_ô_tô = 60 / 60 = 1 h = 60 phút. Sớm hơn: 90 - 60 = 30 phút."),
        make_vdc(3, "Một đoàn tàu hỏa dài 150 m đang chạy với tốc độ 54 km/h (15 m/s) chạy song song và cùng chiều với một người đi xe đạp với tốc độ 18 km/h (5 m/s). Thời gian từ lúc đầu tàu bắt đầu vượt người đi xe đạp đến khi đuôi tàu vượt qua hẳn là:", ["15 giây", "10 giây", "20 giây", "30 giây"], 0, "Tốc độ tương đối: v = 15 - 5 = 10 m/s. t = 150 / 10 = 15 s."),
        make_vdc(4, "Một ca nô xuôi dòng khúc sông dài 60 km hết 2 giờ, sau đó ngược dòng trở về hết 3 giờ. Biết công suất máy không đổi, tốc độ thực của ca nô khi nước đứng yên là:", ["25 km/h", "20 km/h", "5 km/h", "30 km/h"], 0, "v_xuôi = 60 / 2 = 30 km/h; v_ngược = 60 / 3 = 20 km/h => v_thực = (30 + 20) / 2 = 25 km/h.")
    ]
}

# =========================================================================
# BÀI 9: ĐO TỐC ĐỘ (3 ĐỀ ĐỘC LẬP)
# =========================================================================

# --- ĐỀ 1 ---
b8_b9_exams["phys7_c3_b9_test1"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 9: Đo tốc độ - Đề số 01",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b9", "lessonName": "Bài 9: Đo tốc độ",
    "testNum": 1, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Để đo tốc độ của một vật chuyển động bằng phương pháp thông thường trong phòng thí nghiệm, ta cần dùng:", ["Thước đo độ dài và đồng hồ đo thời gian", "Cân điện tử và nhiệt kế", "Lực kế và thước dây", "Bình chia độ và đồng hồ bấm giây"], 0, "Để tính v = s / t cần đo quãng đường bằng thước và đo thời gian bằng đồng hồ."),
        make_mc(2, "Nhận biết", "Thiết bị đo thời gian hiện đại trong phòng thực hành kết nối với đồng hồ đo hiện số để đo chính xác chuyển động là:", ["Cổng quang điện (cảm biến hồng ngoại)", "Đồng hồ cát", "Đồng hồ quả lắc", "Nhiệt kế điện tử"], 0, "Cổng quang điện ghi nhận thời gian vật chắn chùm tia sáng truyền tới đồng hồ hiện số."),
        make_mc(3, "Nhận biết", "Thiết bị 'bắn tốc độ' thường được lực lượng cảnh sát giao thông sử dụng trên đường hoạt động dựa trên:", ["Camera kết hợp máy phát và thu sóng vô tuyến (radar) hoặc sóng laser", "Cân tải trọng tự động", "Thước dây đo cự li", "Kính tiềm vọng"], 0, "Súng bắn tốc độ phát sóng radar hoặc laser rồi thu tín hiệu phản xạ để tính tốc độ và chụp ảnh xe."),
        make_mc(4, "Nhận biết", "Khi đo tốc độ bằng thước và đồng hồ bấm giây, để kết quả đo chính xác hơn và giảm thiểu sai số ngẫu nhiên, ta cần:", ["Thực hiện phép đo nhiều lần rồi tính giá trị trung bình", "Chỉ cần đo một lần duy nhất thật cẩn thận", "Chọn dụng cụ có giới hạn đo nhỏ nhất có thể", "Làm tròn kết quả lên số nguyên lớn nhất"], 0, "Đo lặp lại nhiều lần và lấy giá trị trung bình giúp triệt tiêu sai số ngẫu nhiên."),
        make_mc(5, "Nhận biết", "Trong thí nghiệm đo tốc độ của viên bi lăn trên máng nghiêng bằng cổng quang điện, đại lượng s đo bằng thước là:", ["Khoảng cách giữa hai cổng quang điện", "Chiều dài của cả máng nghiêng", "Đường kính của viên bi", "Độ cao của máng nghiêng"], 0, "Quãng đường s là khoảng cách giữa hai cổng quang điện A và B."),
        make_mc(6, "Nhận biết", "Đồng hồ bấm giây điện tử hiện số có nút chức năng nào để đưa kết quả hiển thị về giá trị 0 ban đầu?", ["Nút Reset", "Nút Mode", "Nút Start", "Nút Stop"], 0, "Nút Reset dùng để xóa kết quả hiển thị về 00:00:00."),
        make_mc(7, "Thông hiểu", "Dùng thước mét đo quãng đường đi được s = 1,2 m và đồng hồ bấm giây đo thời gian t = 0,8 s. Tốc độ chuyển động là:", ["1,5 m/s", "0,96 m/s", "1,2 m/s", "2,0 m/s"], 0, "v = s / t = 1,2 / 0,8 = 1,5 m/s."),
        make_mc(8, "Thông hiểu", "Một tấm chắn sáng có bề rộng d = 2 cm (0,02 m) gắn trên xe lăn. Khi xe đi qua cổng quang điện, đồng hồ hiện số báo thời gian chắn sáng là 0,05 s. Tốc độ tức thời của xe là:", ["0,4 m/s", "0,1 m/s", "2,5 m/s", "1,0 m/s"], 0, "v = d / t = 0,02 / 0,05 = 0,4 m/s."),
        make_mc(9, "Thông hiểu", "Khi sử dụng đồng hồ bấm giây để đo thời gian chạy của bạn học sinh, sai số chủ yếu xuất phát từ:", ["Thời gian phản ứng của ngón tay người bấm khi nghe hiệu lệnh xuất phát và lúc thấy bạn về đích", "Đồng hồ chạy quá nhanh", "Đồng hồ bị sai pin", "Không khí cản trở đồng hồ"], 0, "Sai số phản ứng của con người khi bấm nút Start/Stop khoảng 0,1 - 0,2 s."),
        make_mc(10, "Thông hiểu", "Thiết bị bắn tốc độ ghi nhận thời gian ô tô đi qua hai vạch mốc cách nhau 10 m là 0,5 giây. Tốc độ của ô tô là:", ["72 km/h", "50 km/h", "20 km/h", "36 km/h"], 0, "v = 10 / 0,5 = 20 m/s = 20 × 3,6 = 72 km/h."),
        make_mc(11, "Thông hiểu", "Trong thí nghiệm đo tốc độ xe đồ chơi, kết quả đo 3 lần thời gian đi cùng quãng đường 1 m lần lượt là: 2,4 s; 2,5 s; 2,6 s. Thời gian trung bình là:", ["2,5 s", "2,4 s", "2,6 s", "2,55 s"], 0, "t_tb = (2,4 + 2,5 + 2,6) / 3 = 2,5 s."),
        make_mc(12, "Thông hiểu", "Ưu điểm nổi bật nhất của việc dùng cổng quang điện và đồng hồ hiện số so với đồng hồ bấm giây tay là:", ["Độ chính xác rất cao, loại bỏ hoàn toàn sai số do phản ứng bấm tay của con người", "Giá thành rẻ hơn nhiều", "Dễ mang đi dã ngoại", "Không cần dùng nguồn điện"], 0, "Cảm biến quang điện tự động đóng ngắt mạch đo, không bị ảnh hưởng bởi phản xạ tay người.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét phương pháp đo tốc độ bằng thước cuộn và đồng hồ bấm giây trong giờ học thể dục:", [
            ("a", "Thước cuộn dùng để đo độ dài đường chạy của học sinh.", True),
            ("b", "Người bấm giờ cần bấm nút chạy đồng hồ ngay khi nghe hiệu lệnh xuất phát.", True),
            ("c", "Dừng đồng hồ ngay khi học sinh chạm vạch đích.", True),
            ("d", "Phương pháp này hoàn toàn không có sai số nào xảy ra.", False)
        ], "Phương pháp bấm tay luôn có sai số do phản xạ và thao tác người bấm."),
        make_tf(2, "Thông hiểu", "Xét hoạt động của cổng quang điện và đồng hồ đo thời gian hiện số:", [
            ("a", "Cổng quang điện gồm một đầu phát tia hồng ngoại và một đầu thu tín hiệu quang học.", True),
            ("b", "Khi vật chắn chùm tia sáng giữa cổng quang, tín hiệu điện được truyền đến đồng hồ hiện số để bắt đầu hoặc dừng đếm.", True),
            ("c", "Nếu đặt chế độ đo A <-> B, đồng hồ sẽ đo khoảng thời gian vật di chuyển từ cổng A đến cổng B.", True),
            ("d", "Cổng quang điện chỉ có thể đo được các vật có khối lượng lớn hơn 1 kg.", False)
        ], "Cổng quang điện đo được cả các vật rất nhỏ và nhẹ như viên bi, xe đồ chơi."),
        make_tf(3, "Vận dụng", "Học sinh thực hiện đo tốc độ xe lăn trên máng nghiêng giữa hai cổng quang A và B cách nhau 0,8 m:", [
            ("a", "Ba lần đo thời gian xe chạy từ A đến B lần lượt là: 1,58 s; 1,60 s; 1,62 s.", True),
            ("b", "Thời gian chuyển động trung bình của xe lăn là 1,60 s.", True),
            ("c", "Tốc độ trung bình của xe lăn giữa hai cổng quang là 0,5 m/s.", True),
            ("d", "Nếu nâng máng nghiêng dốc hơn, thời gian xe lăn chạy giữa hai cổng sẽ tăng lên.", False)
        ], "Máng nghiêng dốc hơn làm xe chuyển động nhanh hơn nên thời gian chạy giảm đi."),
        make_tf(4, "Vận dụng", "Cảnh sát giao thông sử dụng thiết bị bắn tốc độ để kiểm soát giao thông trên đường quốc lộ:", [
            ("a", "Thiết bị có thể đo được cả tốc độ của phương tiện đang tiến lại gần hoặc rời xa máy bắn.", True),
            ("b", "Máy tự động ghi nhận hình ảnh biển số xe, thời gian và tốc độ đo được của phương tiện.", True),
            ("c", "Hình ảnh chụp từ thiết bị bắn tốc độ có giá trị pháp lí để xử phạt phương tiện vi phạm tốc độ.", True),
            ("d", "Thiết bị bắn tốc độ bắt buộc phải có người cầm dây kéo theo xe để đo độ dài đường đi.", False)
        ], "Thiết bị bắn tốc độ ứng dụng sóng radar/laser không dây, không dùng dây đo cơ học.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Dùng đồng hồ bấm giây đo thời gian một bạn chạy 60 m hết 10 s. Tốc độ trung bình là bao nhiêu m/s?", "6", "v = 60 / 10 = 6 m/s."),
        make_sa(2, "Thông hiểu", "Khoảng cách giữa hai cổng quang điện A và B là 0,6 m. Đồng hồ hiện số báo thời gian xe đi từ A đến B là 0,5 s. Tốc độ trung bình là bao nhiêu m/s?", "1.2", "v = 0,6 / 0,5 = 1,2 m/s."),
        make_sa(3, "Vận dụng", "Tấm chắn sáng gắn trên xe thí nghiệm có độ rộng 0,04 m. Đồng hồ hiện số đo được thời gian tấm chắn đi qua cổng quang là 0,08 s. Tốc độ tức thời của xe là bao nhiêu m/s?", "0.5", "v = 0,04 / 0,08 = 0,5 m/s."),
        make_sa(4, "Vận dụng", "Học sinh đo 3 lần thời gian viên bi chuyển động trên máng dài 0,9 m được các giá trị: 1,7 s; 1,8 s; 1,9 s. Tốc độ trung bình của viên bi là bao nhiêu m/s?", "0.5", "t_tb = (1,7 + 1,8 + 1,9)/3 = 1,8 s => v = 0,9 / 1,8 = 0,5 m/s."),
        make_sa(5, "Vận dụng cao", "Camera bắn tốc độ cố định ghi nhận một ô tô đi qua đoạn đường kiểm tra dài 15 m mất 0,6 giây. Tốc độ của ô tô đó tính theo km/h là bao nhiêu?", "90", "v = 15 / 0,6 = 25 m/s = 25 × 3,6 = 90 km/h."),
        make_sa(6, "Vận dụng cao", "Một người gõ búa xuống đường ray xe lửa, người ở đầu kia áp tai vào đường ray nghe thấy âm truyền trong thép sau 0,1 giây. Biết đường ray dài 500 m. Tốc độ âm trong thép đo được là bao nhiêu m/s?", "5000", "v = 500 / 0,1 = 5000 m/s.")
    ],
    "part4": [
        make_vdc(1, "Thiết bị bắn tốc độ tự động đặt tại đoạn đường có biển giới hạn tốc độ 60 km/h. Thiết bị chụp hai bức ảnh một xe con khi đi qua hai vạch mốc cách nhau 20 m trong khoảng thời gian 1,0 giây. Xe con đó có vi phạm chạy quá tốc độ không và vượt quá bao nhiêu km/h?", ["Có vi phạm, chạy 72 km/h (vượt quá 12 km/h)", "Không vi phạm vì tốc độ chỉ là 50 km/h", "Không vi phạm vì tốc độ đạt đúng 60 km/h", "Có vi phạm, chạy 80 km/h (vượt quá 20 km/h)"], 0, "v = 20 / 1,0 = 20 m/s = 72 km/h. Giới hạn 60 km/h => vượt quá 12 km/h."),
        make_vdc(2, "Trong giờ thực hành, bạn An dùng đồng hồ bấm giây để đo thời gian rơi của một quả bóng bàn từ độ cao 2,0 m. Do độ trễ phản xạ tay bấm của An là 0,15 s, thời gian hiển thị trên đồng hồ là 0,80 s. Thời gian rơi thực tế và tốc độ rơi trung bình thực tế của quả bóng là:", ["0,65 s và xấp xỉ 3,08 m/s", "0,95 s và xấp xỉ 2,11 m/s", "0,80 s và 2,50 m/s", "0,50 s và 4,00 m/s"], 0, "t_thực = 0,80 - 0,15 = 0,65 s => v_tb = 2,0 / 0,65 ≈ 3,08 m/s."),
        make_vdc(3, "Để đo tốc độ của dòng nước sông, một nhóm học sinh thả một chiếc phao xốp trôi tự do giữa hai cột mốc ven bờ cách nhau 40 m. Đồng hồ bấm giây đo được 3 lần thời gian trôi lần lượt là: 48 s; 50 s; 52 s. Tốc độ dòng nước xấp xỉ bằng:", ["0,80 m/s", "0,75 m/s", "1,25 m/s", "1,00 m/s"], 0, "t_tb = (48 + 50 + 52) / 3 = 50 s => v = 40 / 50 = 0,80 m/s."),
        make_vdc(4, "Một đoàn tàu đang chạy thẳng đều. Người lái tàu quan sát thấy đầu tàu vượt qua hai cột mốc cây số bên đường cách nhau 1 km trong thời gian đúng 45 giây. Tốc độ của đoàn tàu là:", ["80 km/h", "60 km/h", "90 km/h", "75 km/h"], 0, "v = 1000 / 45 = 200/9 m/s = (200/9) × 3,6 = 80 km/h.")
    ]
}

# --- ĐỀ 2 ---
b8_b9_exams["phys7_c3_b9_test2"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 9: Đo tốc độ - Đề số 02",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b9", "lessonName": "Bài 9: Đo tốc độ",
    "testNum": 2, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Dụng cụ dùng để đo quãng đường chuyển động của một vật trong thí nghiệm vật lý là:", ["Thước cuộn hoặc thước thẳng có ĐCNN phù hợp", "Nhiệt kế", "Lực kế", "Ampe kế"], 0, "Dùng thước có ĐCNN phù hợp để đo quãng đường s."),
        make_mc(2, "Nhận biết", "Đồng hồ bấm giây cơ học hoặc điện tử dùng để đo đại lượng nào trong bài thực hành đo tốc độ?", ["Khoảng thời gian chuyển động", "Quãng đường vật đi", "Trọng lượng của vật", "Nhiệt độ môi trường"], 0, "Đồng hồ bấm giây dùng để đo khoảng thời gian t."),
        make_mc(3, "Nhận biết", "Trong hệ thống đo tốc độ tự động ở phòng thí nghiệm trường học, cổng quang điện gửi tín hiệu đến thiết bị nào?", ["Đồng hồ đo thời gian hiện số", "Bình ắc quy", "Bóng đèn sợi đốt", "Loa phát thanh"], 0, "Cổng quang điện kết nối với đồng hồ đo thời gian hiện số."),
        make_mc(4, "Nhận biết", "Súng bắn tốc độ của cảnh sát giao thông tính được tốc độ phương tiện nhờ đo đại lượng nào?", ["Thời gian truyền và phản xạ lại của chùm sóng vô tuyến hoặc laser", "Khối lượng của xe", "Tiếng ồn động cơ xe phát ra", "Màu sơn của xe"], 0, "Đo khoảng thời gian sóng phản xạ từ xe quay trở lại súng."),
        make_mc(5, "Nhận biết", "Để giảm sai số của dụng cụ khi đo quãng đường, ta nên chọn thước đo có:", ["Giới hạn đo thích hợp và độ chia nhỏ nhất (ĐCNN) đủ nhỏ", "Độ chia nhỏ nhất càng lớn càng tốt", "Chiều dài ngắn hơn vật cần đo nhiều lần", "Vạch chia bị mờ"], 0, "Chọn thước có GHĐ phù hợp và ĐCNN đủ nhỏ giúp số đo chuẩn xác."),
        make_mc(6, "Nhận biết", "Trên đồng hồ đo thời gian hiện số, thang đo hiển thị thời gian thường có đơn vị là:", ["Giây (s) và phần nghìn giây (ms)", "Phút (min)", "Giờ (h)", "Ngày"], 0, "Đồng hồ hiện số trong phòng thí nghiệm thường đo đến 0,001 s (miligiây)."),
        make_mc(7, "Thông hiểu", "Một học sinh đo quãng đường chạy s = 80 m, đồng hồ bấm giây chỉ t = 16 s. Tốc độ trung bình của bạn là:", ["5 m/s", "4 m/s", "6 m/s", "1280 m/s"], 0, "v = s / t = 80 / 16 = 5 m/s."),
        make_mc(8, "Thông hiểu", "Tấm chắn sáng rộng 1 cm (0,01 m) đi qua cổng quang điện trong thời gian 0,02 s. Tốc độ tức thời của vật là:", ["0,5 m/s", "0,2 m/s", "2,0 m/s", "1,0 m/s"], 0, "v = 0,01 / 0,02 = 0,5 m/s."),
        make_mc(9, "Thông hiểu", "Để đo thời gian chạy 100 m của vận động viên điền kinh, người bấm giờ bắt đầu bấm đồng hồ khi:", ["Thấy khói phát ra từ nòng súng phát lệnh (hoặc đèn phát lệnh chớp sáng)", "Nghe thấy tiếng nổ của súng phát lệnh", "Thấy vận động viên bắt đầu chạm chân qua vạch đích", "Vận động viên đã chạy được một nửa đường"], 0, "Ánh sáng truyền nhanh tức thời, nhìn thấy tia chớp/khói súng bấm ngay sẽ chuẩn xác hơn nghe tiếng nổ (do âm thanh truyền chậm)."),
        make_mc(10, "Thông hiểu", "Camera bắn tốc độ ghi nhận một mô tô đi qua quãng đường kiểm tra 12 m trong thời gian 0,8 s. Tốc độ của mô tô là:", ["54 km/h", "15 km/h", "36 km/h", "60 km/h"], 0, "v = 12 / 0,8 = 15 m/s = 15 × 3,6 = 54 km/h."),
        make_mc(11, "Thông hiểu", "Ba bạn cùng đo thời gian viên bi lăn qua quãng đường 1,5 m được các giá trị: 3,1 s; 2,9 s; 3,0 s. Giá trị trung bình là:", ["3,0 s", "2,9 s", "3,1 s", "3,05 s"], 0, "t_tb = (3,1 + 2,9 + 3,0) / 3 = 3,0 s."),
        make_mc(12, "Thông hiểu", "Khi đo tốc độ bằng xe lăn trên máng nghiêng dùng cổng quang điện, nếu thay viên bi sắt bằng viên bi gỗ có cùng kích thước thì:", ["Thời gian chắn sáng vẫn được đồng hồ đo chính xác nhờ tín hiệu ngắt quang học", "Cổng quang điện không nhận diện được bi gỗ", "Đồng hồ không chạy", "Cổng quang bị chập điện"], 0, "Cổng quang ngắt tín hiệu khi có bất kì vật cản quang nào đi qua.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét quy trình thực hiện phép đo tốc độ bằng thước thẳng và đồng hồ bấm giây:", [
            ("a", "Dùng thước đo xác định quãng đường chuyển động s.", True),
            ("b", "Dùng đồng hồ bấm giây đo khoảng thời gian t vật đi hết quãng đường s.", True),
            ("c", "Tính tốc độ của vật theo công thức v = s / t.", True),
            ("d", "Chỉ cần đo đúng 1 lần là khẳng định kết quả chính xác tuyệt đối không có sai số.", False)
        ], "Mọi phép đo thực nghiệm đều có sai số, cần đo nhiều lần lấy trung bình."),
        make_tf(2, "Thông hiểu", "Xét hoạt động của đồng hồ đo thời gian hiện số khi nối với cổng quang điện:", [
            ("a", "Có thể chọn chế độ đo thời gian vật chắn qua một cổng quang điện duy nhất.", True),
            ("b", "Có thể chọn chế độ đo khoảng thời gian vật đi từ cổng quang thứ nhất đến cổng quang thứ hai.", True),
            ("c", "Đồng hồ hiện số hiển thị kết quả bằng các chữ số điện tử rõ ràng, tránh sai số đọc mắt.", True),
            ("d", "Đồng hồ đo hiện số chỉ hoạt động được khi dùng đèn pin chiếu trực tiếp từ bên ngoài.", False)
        ], "Cổng quang điện có sẵn đèn phát tia hồng ngoại bên trong, không cần đèn pin bên ngoài."),
        make_tf(3, "Vận dụng", "Học sinh tiến hành đo tốc độ rơi của một quả cầu nhỏ từ độ cao h = 1,25 m xuống sàn:", [
            ("a", "Học sinh đo 3 lần thời gian rơi thu được các kết quả: 0,49 s; 0,50 s; 0,51 s.", True),
            ("b", "Thời gian rơi trung bình tính được là 0,50 s.", True),
            ("c", "Tốc độ rơi trung bình của quả cầu trên đoạn đường này là 2,5 m/s.", True),
            ("d", "Nếu tăng độ cao rơi lên 5 m thì thời gian rơi sẽ giảm đi một nửa.", False)
        ], "Rơi từ độ cao lớn hơn thì thời gian rơi phải tăng lên."),
        make_tf(4, "Vận dụng", "Ứng dụng thiết bị bắn tốc độ trong giám sát an toàn giao thông đường cao tốc:", [
            ("a", "Camera ghi hình giúp xác định chính xác biển kiểm soát của phương tiện chạy quá tốc độ.", True),
            ("b", "Hệ thống có thể hoạt động giám sát tự động liên tục cả ngày lẫn đêm.", True),
            ("c", "Thiết bị laser bắn tốc độ phát ra chùm tia laser nhìn thấy được màu đỏ làm mù mắt tài xế.", False),
            ("d", "Dữ liệu tốc độ đo được từ hệ thống được truyền trực tiếp về trung tâm điều hành giao thông.", True)
        ], "Tia laser trong máy đo tốc độ là laser hồng ngoại không nhìn thấy và an toàn cho mắt.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Đo quãng đường s = 100 m và thời gian t = 20 s. Tốc độ tính được là bao nhiêu m/s?", "5", "v = 100 / 20 = 5 m/s."),
        make_sa(2, "Thông hiểu", "Cổng quang điện cách nhau 0,8 m. Đồng hồ hiện số đo thời gian xe chạy hết 0,4 s. Tốc độ của xe là bao nhiêu m/s?", "2", "v = 0,8 / 0,4 = 2 m/s."),
        make_sa(3, "Vận dụng", "Tấm chắn sáng rộng 0,03 m. Đồng hồ đo thời gian chắn cổng quang là 0,05 s. Tốc độ tức thời là bao nhiêu m/s?", "0.6", "v = 0,03 / 0,05 = 0,6 m/s."),
        make_sa(4, "Vận dụng", "Thực hiện 3 lần đo thời gian xe lăn chạy quãng đường 1,2 m thu được: 2,3 s; 2,4 s; 2,5 s. Tốc độ trung bình là bao nhiêu m/s?", "0.5", "t_tb = (2,3 + 2,4 + 2,5)/3 = 2,4 s => v = 1,2 / 2,4 = 0,5 m/s."),
        make_sa(5, "Vận dụng cao", "Camera ghi nhận một ô tô đi qua 2 mốc cách nhau 25 m trong 1 giây. Tốc độ của ô tô đó tính theo km/h là bao nhiêu?", "90", "v = 25 / 1 = 25 m/s = 25 × 3,6 = 90 km/h."),
        make_sa(6, "Vận dụng cao", "Một máy phát siêu âm từ mạn tàu phát xuống đáy biển và nhận lại tín hiệu phản xạ sau 0,8 giây. Biết tốc độ âm trong nước biển là 1500 m/s. Độ sâu đáy biển là bao nhiêu mét?", "600", "d = v × t / 2 = 1500 × 0,8 / 2 = 600 m.")
    ],
    "part4": [
        make_vdc(1, "Một đoạn đường trong khu dân cư có biển báo giới hạn tốc độ tối đa là 50 km/h. Súng bắn tốc độ laser của cảnh sát giao thông ghi nhận xe mô tô chạy qua quãng đường 15 m trong thời gian đúng 0,9 giây. Tốc độ thực tế của xe mô tô là bao nhiêu và xe có vi phạm quy định tốc độ không?", ["60 km/h - Có vi phạm chạy quá tốc độ cho phép", "45 km/h - Không vi phạm tốc độ", "50 km/h - Đạt đúng tốc độ tối đa cho phép", "65 km/h - Có vi phạm chạy quá tốc độ cho phép"], 0, "v = 15 / 0,9 = 50/3 m/s = (50/3) × 3,6 = 60 km/h. Giới hạn 50 km/h => Có vi phạm quá tốc độ."),
        make_vdc(2, "Trong phòng thí nghiệm, học sinh đo tốc độ của viên bi chuyển động trên đệm khí. Quãng đường đo bằng thước có sai số dụng cụ là ± 0,002 m, đo được s = 0,500 m. Đồng hồ hiện số đo thời gian t = 0,250 s với sai số ± 0,001 s. Tốc độ trung bình của viên bi xấp xỉ bằng:", ["2,00 m/s", "1,50 m/s", "2,50 m/s", "1,80 m/s"], 0, "v = 0,500 / 0,250 = 2,00 m/s."),
        make_vdc(3, "Để đo tốc độ âm thanh trong không khí, hai bạn học sinh đứng cách một bức tường lớn 170 m. Một bạn gõ hai thanh gỗ vào nhau, bạn kia bấm đồng hồ đo thời gian từ lúc gõ đến lúc nghe thấy tiếng vang dội lại là 1,0 giây. Tốc độ âm thanh đo được từ thí nghiệm này là:", ["340 m/s", "170 m/s", "680 m/s", "300 m/s"], 0, "Âm thanh truyền đi và về: s = 2 × 170 = 340 m. v = 340 / 1,0 = 340 m/s."),
        make_vdc(4, "Một ô tô đồ chơi điều khiển từ xa chạy một vòng tròn khép kín có chu vi 18,84 m (đo bằng dây mềm). Đồng hồ bấm giây ghi lại thời gian chạy hết một vòng là 6,0 giây. Tốc độ trung bình của ô tô đồ chơi là:", ["3,14 m/s", "6,28 m/s", "1,57 m/s", "2,50 m/s"], 0, "v = s / t = 18,84 / 6,0 = 3,14 m/s.")
    ]
}

# --- ĐỀ 3 ---
b8_b9_exams["phys7_c3_b9_test3"] = {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 9: Đo tốc độ - Đề số 03",
    "grade": "7", "subject": "physics", "subjectName": "Vật lý",
    "chapterId": "phys7_c3", "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b9", "lessonName": "Bài 9: Đo tốc độ",
    "testNum": 3, "duration": "45 phút", "points": 10.0,
    "part1": [
        make_mc(1, "Nhận biết", "Để xác định tốc độ tức thời của một vật chuyển động trên máng thực hành, người ta gắn trên vật:", ["Một tấm chắn sáng có bề rộng xác định", "Một quả cân nặng", "Một chiếc nhiệt kế", "Một miếng nam châm"], 0, "Gắn tấm chắn sáng có độ rộng nhỏ d để cổng quang điện đo thời gian chắn sáng t."),
        make_mc(2, "Nhận biết", "Cổng quang điện hoạt động dựa trên nguyên lí cảm biến:", ["Quang điện hồng ngoại", "Nhiệt độ nóng chảy", "Áp suất không khí", "Sức căng bề mặt"], 0, "Cổng quang điện sử dụng cảm biến quang điện thu phát tia hồng ngoại."),
        make_mc(3, "Nhận biết", "Trong thí nghiệm đo tốc độ của học sinh chạy cự li ngắn, dụng cụ đo thời gian thường dùng là:", ["Đồng hồ bấm giây cầm tay", "Đồng hồ cát", "Thước dây", "Cân đồng hồ"], 0, "Đồng hồ bấm giây là thiết bị đo thời gian phổ biến trong thể dục thể thao."),
        make_mc(4, "Nhận biết", "Camera bắn tốc độ cố định được lắp đặt trên các giá long môn trên cao tốc nhằm:", ["Tự động phát hiện và ghi nhận vi phạm chạy quá tốc độ của các xe lưu thông", "Đo nhiệt độ mặt đường", "Chiếu sáng ban đêm", "Đếm số cây xanh ven đường"], 0, "Giám sát tốc độ phương tiện tự động trên các làn xe cao tốc."),
        make_mc(5, "Nhận biết", "Khi dùng thước kẻ để đo quãng đường s, mắt của người đọc kết quả cần đặt:", ["Vuông góc với cạnh thước tại vạch đo", "Nghiêng góc 45 độ về phía trái", "Nghiêng góc 45 độ về phía phải", "Cách thước thật xa"], 0, "Đặt mắt nhìn vuông góc với cạnh thước tại vạch đo để tránh sai số thị giác."),
        make_mc(6, "Nhận biết", "Đơn vị đo thời gian chuẩn trong hệ thống đơn vị đo lường quốc tế SI là:", ["Giây (s)", "Phút (min)", "Giờ (h)", "Ngày"], 0, "Đơn vị chuẩn của thời gian trong hệ SI là giây (s)."),
        make_mc(7, "Thông hiểu", "Một học sinh đo quãng đường đi được s = 1,8 m trong thời gian t = 1,2 s. Tốc độ chuyển động của vật là:", ["1,5 m/s", "2,16 m/s", "0,67 m/s", "3,0 m/s"], 0, "v = s / t = 1,8 / 1,2 = 1,5 m/s."),
        make_mc(8, "Thông hiểu", "Một tấm chắn sáng có bề rộng d = 1,5 cm (0,015 m) chắn cổng quang điện trong 0,03 s. Tốc độ tức thời là:", ["0,5 m/s", "0,05 m/s", "2,0 m/s", "0,45 m/s"], 0, "v = 0,015 / 0,03 = 0,5 m/s."),
        make_mc(9, "Thông hiểu", "Trong thí nghiệm đo tốc độ của xe đồ chơi, nếu ta quên bấm nút dừng khi xe đã về đích thì:", ["Thời gian ghi nhận lớn hơn thực tế, dẫn đến tốc độ tính được nhỏ hơn thực tế", "Tốc độ tính được lớn hơn thực tế", "Quãng đường bị giảm đi", "Không ảnh hưởng đến kết quả"], 0, "t ghi nhận lớn hơn => v = s / t sẽ nhỏ hơn thực tế."),
        make_mc(10, "Thông hiểu", "Thiết bị bắn tốc độ ghi nhận thời gian ô tô đi qua 30 m là 1,2 giây. Tốc độ của ô tô tương ứng là:", ["90 km/h", "25 km/h", "60 km/h", "72 km/h"], 0, "v = 30 / 1,2 = 25 m/s = 25 × 3,6 = 90 km/h."),
        make_mc(11, "Thông hiểu", "Ba lần đo thời gian chuyển động của hòn bi trên máng thẳng dài 1,2 m là: 1,9 s; 2,0 s; 2,1 s. Tốc độ trung bình là:", ["0,6 m/s", "0,5 m/s", "1,2 m/s", "0,8 m/s"], 0, "t_tb = (1,9 + 2,0 + 2,1)/3 = 2,0 s => v = 1,2 / 2,0 = 0,6 m/s."),
        make_mc(12, "Thông hiểu", "Tại sao khi chạy cự li 100 m, người ta thường dùng súng phát lệnh có khói trắng thay vì chỉ hô bằng miệng?", ["Vì người bấm giờ ở vạch đích nhìn thấy khói trắng tức thì, loại trừ sai số do âm thanh truyền chậm", "Để làm đẹp sân đấu", "Để tạo tiếng vang lớn", "Để người chạy không bị giật mình"], 0, "Ánh sáng truyền nhanh (300.000 km/s) đến mắt người bấm giờ ngay lập tức, trong khi âm thanh mất khoảng 0,3 s mới đến vạch đích.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các nguyên nhân gây sai số trong thực hành đo tốc độ:", [
            ("a", "Sai số do dụng cụ đo có độ chia nhỏ nhất chưa đủ nhỏ.", True),
            ("b", "Sai số do thao tác bấm đồng hồ bấm giây không đúng thời điểm.", True),
            ("c", "Sai số do đặt mắt nhìn lệch vạch chia trên thước đo.", True),
            ("d", "Sai số ngẫu nhiên hoàn toàn không thể làm giảm bớt dù đo bao nhiêu lần.", False)
        ], "Sai số ngẫu nhiên có thể giảm bớt bằng cách đo lặp lại nhiều lần và lấy giá trị trung bình."),
        make_tf(2, "Thông hiểu", "Về các chế độ đo của đồng hồ đo thời gian hiện số:", [
            ("a", "Chế độ đo MODE A dùng để đo thời gian vật chắn sáng cổng quang A.", True),
            ("b", "Chế độ đo MODE A-B dùng để đo khoảng thời gian vật đi từ cổng A đến cổng B.", True),
            ("c", "Kết quả đo được hiển thị trực tiếp trên màn hình LED bằng các chữ số thập phân.", True),
            ("d", "Đồng hồ hiện số chỉ có thể đo thời gian lớn hơn 10 giây.", False)
        ], "Đồng hồ hiện số có thể đo các khoảng thời gian rất ngắn tới 0,001 s."),
        make_tf(3, "Vận dụng", "Học sinh đo tốc độ của xe thế năng chuyển động trên máng nghiêng:", [
            ("a", "Khoảng cách giữa hai cổng quang đo được là s = 0,5 m.", True),
            ("b", "Thời gian xe chạy giữa hai cổng quang đo được 3 lần: 0,98 s; 1,00 s; 1,02 s.", True),
            ("c", "Thời gian trung bình xe chạy là 1,00 s.", True),
            ("d", "Tốc độ trung bình của xe là 1,0 m/s.", False)
        ], "v = s / t = 0,5 / 1,00 = 0,5 m/s (câu d ghi 1,0 m/s là sai)."),
        make_tf(4, "Vận dụng", "Hệ thống phạt nguội giao thông bằng camera và cảm biến đo tốc độ:", [
            ("a", "Hệ thống có khả năng tự động trích xuất video và hình ảnh phương tiện vi phạm.", True),
            ("b", "Thông tin vi phạm được gửi thông báo phạt nguội đến chủ phương tiện theo địa chỉ đăng kí.", True),
            ("c", "Camera bắn tốc độ chỉ đo được xe máy, không đo được xe ô tô tải lớn.", False),
            ("d", "Góp phần nâng cao ý thức chấp hành luật an toàn giao thông của người tham gia giao thông.", True)
        ], "Hệ thống đo được mọi phương tiện tham gia giao thông trên tuyến đường.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Quãng đường chạy dài 120 m, đồng hồ bấm giây chỉ 24 s. Tốc độ trung bình là bao nhiêu m/s?", "5", "v = 120 / 24 = 5 m/s."),
        make_sa(2, "Thông hiểu", "Hai cổng quang cách nhau 1,0 m. Đồng hồ hiện số báo thời gian đi qua là 0,8 s. Tốc độ là bao nhiêu m/s?", "1.25", "v = 1,0 / 0,8 = 1,25 m/s."),
        make_sa(3, "Vận dụng", "Tấm chắn sáng rộng 0,02 m đi qua cổng quang trong 0,04 s. Tốc độ tức thời là bao nhiêu m/s?", "0.5", "v = 0,02 / 0,04 = 0,5 m/s."),
        make_sa(4, "Vận dụng", "Đo 3 lần thời gian viên bi đi quãng đường 0,8 m được: 1,5 s; 1,6 s; 1,7 s. Tốc độ trung bình là bao nhiêu m/s?", "0.5", "t_tb = (1,5 + 1,6 + 1,7)/3 = 1,6 s => v = 0,8 / 1,6 = 0,5 m/s."),
        make_sa(5, "Vận dụng cao", "Camera bắn tốc độ đo được xe ô tô đi qua 18 m trong thời gian 0,72 giây. Tốc độ ô tô là bao nhiêu km/h?", "90", "v = 18 / 0,72 = 25 m/s = 25 × 3,6 = 90 km/h."),
        make_sa(6, "Vận dụng cao", "Một máy định vị bằng sóng siêu âm trên tàu ngầm gửi xung âm xuống đáy vực sâu và thu được tín hiệu sau 2,4 giây. Biết tốc độ âm trong nước là 1500 m/s. Độ sâu đáy vực là bao nhiêu mét?", "1800", "d = v × t / 2 = 1500 × 2,4 / 2 = 1800 m.")
    ],
    "part4": [
        make_vdc(1, "Một xe tải chở hàng chạy qua đoạn đường có gắn camera đo tốc độ tự động. Biển báo cho phép tốc độ tối đa là 70 km/h. Xe tải đi qua đoạn đường kiểm tra dài 35 m mất thời gian 1,5 giây. Xe tải đó có vi phạm chạy quá tốc độ không và tốc độ đo được là bao nhiêu?", ["Có vi phạm, tốc độ xe là 84 km/h (vượt quá 14 km/h)", "Không vi phạm, tốc độ xe là 65 km/h", "Không vi phạm, tốc độ xe đạt đúng 70 km/h", "Có vi phạm, tốc độ xe là 90 km/h (vượt quá 20 km/h)"], 0, "v = 35 / 1,5 = 70/3 m/s = (70/3) × 3,6 = 84 km/h > 70 km/h => Vi phạm vượt 14 km/h."),
        make_vdc(2, "Trong thí nghiệm đo tốc độ rơi tự do của quả cầu kim loại giữa hai cổng quang điện đặt thẳng đứng cách nhau 0,45 m, đồng hồ hiện số hiển thị thời gian 0,30 s. Tốc độ trung bình của quả cầu trong khoảng rơi này là:", ["1,5 m/s", "1,2 m/s", "2,0 m/s", "0,9 m/s"], 0, "v = 0,45 / 0,30 = 1,5 m/s."),
        make_vdc(3, "Để đo tốc độ di chuyển của một đàn kiến, một bạn học sinh rải một đoạn đường thẳng bằng phấn dài 20 cm (0,2 m) và dùng đồng hồ bấm giây ghi nhận một chú kiến bò hết đoạn đường trong 40 giây. Tốc độ bò của chú kiến là:", ["0,5 cm/s (0,005 m/s)", "2,0 cm/s", "0,2 cm/s", "5,0 cm/s"], 0, "v = 20 / 40 = 0,5 cm/s = 0,005 m/s."),
        make_vdc(4, "Một người gõ búa vào thanh ray đường sắt bằng thép. Người thứ hai ở cách đó 1020 m áp tai vào đường ray và quan sát thấy tiếng gõ truyền qua thép đến trước tiếng gõ truyền qua không khí là 2,8 giây. Biết tốc độ âm trong không khí là 340 m/s. Tốc độ truyền âm trong thép đường ray đo được là:", ["5100 m/s", "3400 m/s", "4800 m/s", "6000 m/s"], 0, "t_khí = 1020 / 340 = 3,0 s. t_thép = 3,0 - 2,8 = 0,2 s => v_thép = 1020 / 0,2 = 5100 m/s.")
    ]
}
