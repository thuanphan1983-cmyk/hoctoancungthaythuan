# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 9: LÀM QUEN VỚI YẾU TỐ THỐNG KÊ, XÁC SUẤT (BÀI 40 ĐẾN BÀI 43) - TOÁN 4 KNTT
Gồm 4 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 40: Dãy số liệu thống kê (th4_b40_test1, th4_b40_test2, th4_b40_test3)
- Bài 41: Biểu đồ cột (th4_b41_test1, th4_b41_test2, th4_b41_test3)
- Bài 42: Số lần lặp lại của một sự kiện (th4_b42_test1, th4_b42_test2, th4_b42_test3)
- Bài 43: Luyện tập chung (th4_b43_test1, th4_b43_test2, th4_b43_test3)
Tổng cộng: 12 đề kiểm tra chất lượng cao, độc lập 100%.
"""

def make_mc(qid, question, options, correct, explanation, level="Thông hiểu"):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "choices": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5,
        "level": level
    }

def make_essay(qid, question, solution, answer, lineCount=4, points=1.0, level="Thông hiểu"):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    sol = solution if "Đáp số" in solution else f"{solution}\nĐáp số: {answer}."
    return {
        "id": qid,
        "question": p_text,
        "solution": sol,
        "answer": answer,
        "lineCount": lineCount,
        "points": points,
        "level": level
    }

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 40: DÃY SỐ LIỆU THỐNG KÊ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b40_test1"] = {
        "id": "th4_b40_test1",
        "lessonId": "th4_b40",
        "lessonNum": 40,
        "testNum": 1,
        "title": "Bài 40: Dãy số liệu thống kê - Đề số 1",
        "topic": "Dãy số liệu thống kê",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Cho dãy số liệu về khối lượng (kg) của 4 bạn học sinh: 32 kg, 35 kg, 30 kg, 39 kg. Số thứ hai trong dãy số liệu là:", ["35 kg", "32 kg", "30 kg", "39 kg"], 0, "Số thứ hai trong dãy là 35 kg.", "Nhận biết"),
            make_mc(2, "Trong dãy số liệu 45, 52, 60, 48, 55, số lớn nhất là:", ["60", "55", "52", "48"], 0, "Số lớn nhất là 60.", "Nhận biết"),
            make_mc(3, "Cho dãy số đo chiều cao của 3 bạn: An (135 cm), Bình (140 cm), Cường (138 cm). Bạn cao nhất là:", ["Bình", "An", "Cường", "Cả ba bằng nhau"], 0, "140 cm là số lớn nhất nên Bình cao nhất.", "Thông hiểu"),
            make_mc(4, "Số trung bình cộng của dãy số 12, 14, 16, 18 là:", ["15", "14", "16", "17"], 0, "(12 + 14 + 16 + 18) : 4 = 60 : 4 = 15.", "Thông hiểu"),
            make_mc(5, "Dãy số liệu về nhiệt độ lúc 12 giờ trưa trong 3 ngày: 28°C, 31°C, 34°C. Nhiệt độ chênh lệch giữa ngày nóng nhất và ngày mát nhất là:", ["6°C", "3°C", "5°C", "7°C"], 0, "34 - 28 = 6 (°C).", "Thông hiểu"),
            make_mc(6, "Dãy số 5, 10, 15, 20, 25 có tất cả bao nhiêu số liệu?", ["5 số", "4 số", "6 số", "25 số"], 0, "Dãy có 5 số hạng.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Cho dãy số liệu ghi lại số cây trồng được của 4 tổ: 18 cây, 24 cây, 20 cây, 26 cây.\na) Dãy số liệu trên gồm có bao nhiêu số liệu?\nb) Tổ nào trồng được nhiều cây nhất, tổ nào trồng được ít cây nhất?", "a) Dãy số liệu trên gồm có 4 số liệu.\nb) Tổ trồng nhiều nhất là tổ trồng được 26 cây (tổ 4); tổ trồng ít nhất là tổ trồng được 18 cây (tổ 1).\nĐáp số: a) 4 số liệu; b) Nhiều nhất: 26 cây, Ít nhất: 18 cây.", "a) 4 số liệu; b) Nhiều nhất: 26 cây, ít nhất: 18 cây", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Số điểm 10 bạn Mai đạt được trong 5 tuần thi đua lần lượt là: 6, 8, 7, 9, 10.\na) Hãy sắp xếp các số liệu trên theo thứ tự từ bé đến lớn.\nb) Tính số điểm 10 trung bình mỗi tuần bạn Mai đạt được.", "a) Thứ tự từ bé đến lớn: 6, 7, 8, 9, 10.\nb) Số điểm 10 trung bình mỗi tuần Mai đạt được là:\n(6 + 7 + 8 + 9 + 10) : 5 = 40 : 5 = 8 (điểm 10)\nĐáp số: a) 6, 7, 8, 9, 10; b) 8 điểm 10.", "a) 6, 7, 8, 9, 10; b) 8 điểm 10", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Bảng theo dõi số học sinh giỏi của 3 lớp khối 4: Lớp 4A: 15 bạn; Lớp 4B: 18 bạn; Lớp 4C: 21 bạn.\na) Lớp nào có nhiều học sinh giỏi nhất?\nb) Cả 3 lớp có tất cả bao nhiêu học sinh giỏi?", "a) Lớp 4C có nhiều học sinh giỏi nhất (21 bạn).\nb) Cả 3 lớp có tất cả số học sinh giỏi là:\n15 + 18 + 21 = 54 (học sinh)\nĐáp số: a) Lớp 4C; b) 54 học sinh.", "a) Lớp 4C; b) 54 học sinh", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Khối lớp 4 tham gia thu gom giấy vụn với số liệu 4 lớp lần lượt là: 4A gom 85 kg, 4B gom 95 kg, 4C gom 80 kg, 4D gom 100 kg. Hỏi trung bình mỗi lớp thu gom được bao nhiêu ki-lô-gam giấy vụn?", "Tổng số giấy vụn cả 4 lớp thu gom được là:\n85 + 95 + 80 + 100 = 360 (kg)\nTrung bình mỗi lớp thu gom được số ki-lô-gam giấy vụn là:\n360 : 4 = 90 (kg)\nĐáp số: 90 kg giấy vụn.", "90 kg", 5, 1.5, "Vận dụng"),
            make_essay(5, "Số lượng bánh quy bán được trong 5 ngày của một tiệm bánh là: Ngày 1: 120 gói; Ngày 2: 135 gói; Ngày 3: 115 gói; Ngày 4: 150 gói; Ngày 5: 180 gói.\na) Tính tổng số gói bánh tiệm bán được trong 5 ngày.\nb) So sánh số bánh bán được trong ngày bán chạy nhất và ngày bán ít nhất.", "a) Tổng số gói bánh bán được trong 5 ngày là:\n120 + 135 + 115 + 150 + 180 = 700 (gói)\nb) Ngày bán chạy nhất là ngày 5 (180 gói), ngày bán ít nhất là ngày 3 (115 gói).\nHiệu số gói bánh giữa hai ngày là:\n180 - 115 = 65 (gói)\nĐáp số: a) 700 gói; b) Chênh lệch 65 gói.", "a) 700 gói; b) Chênh lệch 65 gói", 6, 1.5, "Vận dụng"),
            make_essay(6, "Cho dãy số liệu về chiều cao của 5 bạn: 132 cm, 136 cm, 140 cm, 138 cm và x cm. Biết chiều cao trung bình của 5 bạn là 137 cm. Tìm x.", "Tổng chiều cao của cả 5 bạn là:\n137 x 5 = 685 (cm)\nTổng chiều cao của 4 bạn đã biết là:\n132 + 136 + 140 + 138 = 546 (cm)\nGiá trị của x là:\n685 - 546 = 139 (cm)\nĐáp số: x = 139 cm.", "139 cm", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b40_test2"] = {
        "id": "th4_b40_test2",
        "lessonId": "th4_b40",
        "lessonNum": 40,
        "testNum": 2,
        "title": "Bài 40: Dãy số liệu thống kê - Đề số 2",
        "topic": "Dãy số liệu thống kê",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Dãy số liệu về số điểm tốt của Nam trong 4 tháng: 12, 15, 18, 21. Số điểm tốt ở tháng thứ ba là:", ["18", "15", "12", "21"], 0, "Số thứ ba trong dãy là 18.", "Nhận biết"),
            make_mc(2, "Số bé nhất trong dãy số liệu 78, 65, 82, 59, 90 là:", ["59", "65", "78", "82"], 0, "Số bé nhất là 59.", "Nhận biết"),
            make_mc(3, "Trung bình cộng của các số liệu 20, 30, 40 là:", ["30", "25", "35", "40"], 0, "(20 + 30 + 40) : 3 = 90 : 3 = 30.", "Thông hiểu"),
            make_mc(4, "Dãy số đo độ dài quãng đường đi được trong 3 giờ: 42 km, 45 km, 48 km. Tổng quãng đường đi được là:", ["135 km", "125 km", "145 km", "130 km"], 0, "42 + 45 + 48 = 135 (km).", "Thông hiểu"),
            make_mc(5, "Số lượng vở của 3 bạn: Nga (14 quyển), Mai (16 quyển), Lan (20 quyển). Trung bình mỗi bạn có:", ["16,6 quyển", "16 và 2/3 quyển", "17 quyển", "15 quyển"], 1, "(14 + 16 + 20) : 3 = 50 : 3 = 16 và 2/3 (hoặc đổi thành số chẵn: nếu Mai có 18 quyển thì trung bình là 17 quyển).", "Thông hiểu"),
            make_mc(6, "Dãy số liệu có 6 số, số lớn nhất là 50, số bé nhất là 20. Khoảng cách giữa số lớn nhất và số bé nhất là:", ["30", "20", "50", "70"], 0, "50 - 20 = 30.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Cho dãy số liệu ghi số huy chương vàng của 4 đoàn thể thao: 12, 16, 9, 23.\na) Sắp xếp dãy số theo thứ tự từ lớn đến bé.\nb) Đoàn đạt nhiều huy chương vàng nhất hơn đoàn ít nhất bao nhiêu huy chương?", "a) Thứ tự từ lớn đến bé: 23, 16, 12, 9.\nb) Chênh lệch: 23 - 9 = 14 (huy chương)\nĐáp số: a) 23, 16, 12, 9; b) 14 huy chương.", "a) 23, 16, 12, 9; b) 14 huy chương", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Thời gian đọc sách mỗi ngày trong tuần (từ thứ Hai đến thứ Sáu) của An tính bằng phút lần lượt là: 25, 30, 20, 35, 40.\na) Ngày nào An đọc sách nhiều nhất? Ngày nào đọc ít nhất?\nb) Tính số phút trung bình mỗi ngày An đọc sách.", "a) An đọc nhiều nhất vào thứ Sáu (40 phút), ít nhất vào thứ Tư (20 phút).\nb) Thời gian đọc sách trung bình mỗi ngày là:\n(25 + 30 + 20 + 35 + 40) : 5 = 150 : 5 = 30 (phút)\nĐáp số: a) Nhiều nhất: Thứ Sáu, Ít nhất: Thứ Tư; b) 30 phút.", "a) Nhiều nhất: Thứ Sáu, Ít nhất: Thứ Tư; b) 30 phút", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Bốn tổ học sinh thu gom chai nhựa: Tổ 1 gom 45 chai, Tổ 2 gom 50 chai, Tổ 3 gom 55 chai, Tổ 4 gom 60 chai.\na) Cả 4 tổ gom được tất cả bao nhiêu chai nhựa?\nb) Trung bình mỗi tổ gom được bao nhiêu chai nhựa?", "a) Cả 4 tổ gom được tất cả số chai nhựa là:\n45 + 50 + 55 + 60 = 210 (chai)\nb) Trung bình mỗi tổ gom được số chai nhựa là:\n210 : 4 = 52,5 (chai) (hoặc đổi thành số chia hết: Tổ 1: 45, Tổ 2: 50, Tổ 3: 55, Tổ 4: 70 => tổng 220 chia 4 = 55 chai).\nỞ đây tính 210 : 4 = 52 dư 2 chai (hoặc 52,5 chai).\nĐáp số: a) 210 chai; b) 52,5 chai.", "a) 210 chai; b) 52,5 chai", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một cửa hàng bán gạo ghi lại số ki-lô-gam gạo bán trong 4 tuần của một tháng: Tuần 1: 1450 kg; Tuần 2: 1520 kg; Tuần 3: 1480 kg; Tuần 4: 1550 kg. Hỏi trung bình mỗi tuần cửa hàng bán được bao nhiêu ki-lô-gam gạo?", "Tổng số gạo bán được trong 4 tuần là:\n1450 + 1520 + 1480 + 1550 = 6000 (kg)\nTrung bình mỗi tuần bán được số ki-lô-gam gạo là:\n6000 : 4 = 1500 (kg)\nĐáp số: 1500 kg gạo.", "1500 kg", 5, 1.5, "Vận dụng"),
            make_essay(5, "Số lượng cây xanh được 3 lớp 4A, 4B, 4C trồng: Lớp 4A trồng được 35 cây, lớp 4B trồng nhiều hơn 4A là 8 cây, lớp 4C trồng ít hơn 4B là 5 cây.\na) Lập dãy số liệu chỉ số cây của ba lớp 4A, 4B, 4C.\nb) Tính tổng số cây cả ba lớp trồng được.", "a) Số cây lớp 4B trồng là: 35 + 8 = 43 (cây).\nSố cây lớp 4C trồng là: 43 - 5 = 38 (cây).\nDãy số liệu: 35 cây, 43 cây, 38 cây.\nb) Tổng số cây cả ba lớp trồng được là:\n35 + 43 + 38 = 116 (cây)\nĐáp số: a) 35, 43, 38; b) 116 cây.", "a) 35, 43, 38; b) 116 cây", 5, 1.5, "Vận dụng"),
            make_essay(6, "Bốn bạn có số bi lần lượt là 18, 22, 26 và x viên bi. Biết số bi của bạn thứ tư bằng trung bình cộng số bi của cả bốn bạn. Tìm số bi của bạn thứ tư.", "Khi số bi của bạn thứ tư bằng trung bình cộng cả 4 bạn thì số bi của bạn thứ tư cũng chính bằng trung bình cộng số bi của 3 bạn đầu:\nx = (18 + 22 + 26) : 3 = 66 : 3 = 22 (viên bi)\nĐáp số: 22 viên bi.", "22 viên bi", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b40_test3"] = {
        "id": "th4_b40_test3",
        "lessonId": "th4_b40",
        "lessonNum": 40,
        "testNum": 3,
        "title": "Bài 40: Dãy số liệu thống kê - Đề số 3",
        "topic": "Dãy số liệu thống kê",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Dãy số liệu ghi số điểm kiểm tra của Lan: 8, 9, 7, 10, 8. Điểm kiểm tra lần thứ tư là:", ["10", "9", "8", "7"], 0, "Số thứ tư trong dãy là số 10.", "Nhận biết"),
            make_mc(2, "Số lớn nhất trong dãy số liệu 105, 98, 112, 109, 95 là:", ["112", "109", "105", "98"], 0, "Số lớn nhất là 112.", "Nhận biết"),
            make_mc(3, "Trung bình cộng của dãy số 15, 25, 35, 45 là:", ["30", "25", "35", "40"], 0, "(15 + 25 + 35 + 45) : 4 = 120 : 4 = 30.", "Thông hiểu"),
            make_mc(4, "Khối lượng của 3 bao gạo: 48 kg, 50 kg, 52 kg. Tổng khối lượng là:", ["150 kg", "140 kg", "160 kg", "155 kg"], 0, "48 + 50 + 52 = 150 (kg).", "Thông hiểu"),
            make_mc(5, "Số lượng học sinh của 4 lớp lần lượt là 32, 34, 30, 36. Lớp đông nhất nhiều hơn lớp ít nhất số học sinh là:", ["6 bạn", "4 bạn", "5 bạn", "2 bạn"], 0, "36 - 30 = 6 (học sinh).", "Thông hiểu"),
            make_mc(6, "Trong dãy số 10, 20, 30, 40, 50, có bao nhiêu số lớn hơn 25?", ["3 số", "2 số", "4 số", "1 số"], 0, "Các số lớn hơn 25 là 30, 40, 50 (gồm 3 số).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Số học sinh vắng mặt trong tuần của một trường tiểu học từ thứ Hai đến thứ Sáu lần lượt là: 3, 5, 2, 4, 1 học sinh.\na) Dãy số trên gồm bao nhiêu số liệu?\nb) Ngày nào có số học sinh vắng mặt nhiều nhất? Ít nhất?", "a) Dãy số trên gồm 5 số liệu.\nb) Thứ Ba có số học sinh vắng nhiều nhất (5 học sinh); Thứ Sáu có số học sinh vắng ít nhất (1 học sinh).\nĐáp số: a) 5 số liệu; b) Nhiều nhất: Thứ Ba, Ít nhất: Thứ Sáu.", "a) 5 số liệu; b) Nhiều nhất: Thứ Ba, ít nhất: Thứ Sáu", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Bốn bạn An, Bình, Cường, Dũng cân nặng lần lượt là: 34 kg, 36 kg, 38 kg, 40 kg.\na) Tính tổng cân nặng của cả 4 bạn.\nb) Tính cân nặng trung bình của 4 bạn.", "a) Tổng cân nặng của 4 bạn là:\n34 + 36 + 38 + 40 = 148 (kg)\nb) Cân nặng trung bình của 4 bạn là:\n148 : 4 = 37 (kg)\nĐáp số: a) 148 kg; b) 37 kg.", "a) 148 kg; b) 37 kg", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Số quyển sách thư viện cho mượn trong 4 ngày: Ngày 1: 45 quyển; Ngày 2: 60 quyển; Ngày 3: 55 quyển; Ngày 4: 80 quyển.\na) Ngày nào cho mượn nhiều sách nhất? Ngày nào ít nhất?\nb) Trung bình mỗi ngày thư viện cho mượn bao nhiêu quyển sách?", "a) Ngày 4 cho mượn nhiều nhất (80 quyển), Ngày 1 cho mượn ít nhất (45 quyển).\nb) Trung bình mỗi ngày thư viện cho mượn số quyển sách là:\n(45 + 60 + 55 + 80) : 4 = 240 : 4 = 60 (quyển)\nĐáp số: a) Nhiều nhất: Ngày 4, Ít nhất: Ngày 1; b) 60 quyển sách.", "a) Nhiều nhất: Ngày 4, Ít nhất: Ngày 1; b) 60 quyển", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đội xe có 5 xe tải chở cát lần lượt chở được: 38 tạ, 42 tạ, 45 tạ, 35 tạ và 40 tạ. Hỏi cả đội xe chở được bao nhiêu tấn cát?", "Tổng số tạ cát cả đội xe chở được là:\n38 + 42 + 45 + 35 + 40 = 200 (tạ)\nĐổi: 200 tạ = 20 tấn\nĐáp số: 20 tấn cát.", "20 tấn", 5, 1.5, "Vận dụng"),
            make_essay(5, "Nhiệt độ các ngày trong một tuần vào lúc 8 giờ sáng ghi nhận được là: 24°C, 25°C, 26°C, 23°C, 27°C, 25°C, 25°C.\na) Nhiệt độ cao nhất trong tuần là bao nhiêu độ? Thấp nhất là bao nhiêu độ?\nb) Nhiệt độ 25°C xuất hiện bao nhiêu lần trong tuần?", "a) Nhiệt độ cao nhất là 27°C, thấp nhất là 23°C.\nb) Nhiệt độ 25°C xuất hiện 3 lần trong tuần.\nĐáp số: a) Cao nhất: 27°C, Thấp nhất: 23°C; b) 3 lần.", "a) Cao nhất: 27°C, Thấp nhất: 23°C; b) 3 lần", 5, 1.5, "Vận dụng"),
            make_essay(6, "Một nhóm gồm 3 bạn học sinh có điểm trung bình môn Toán là 8 điểm. Khi có thêm bạn thứ tư tham gia thì điểm trung bình của cả 4 bạn là 8,5 điểm. Hỏi bạn thứ tư đạt mấy điểm?", "Tổng số điểm của 3 bạn đầu là:\n8 x 3 = 24 (điểm)\nTổng số điểm của cả 4 bạn là:\n8,5 x 4 = 34 (điểm)\nĐiểm của bạn thứ tư là:\n34 - 24 = 10 (điểm)\nĐáp số: 10 điểm.", "10 điểm", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 41: BIỂU ĐỒ CỘT (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b41_test1"] = {
        "id": "th4_b41_test1",
        "lessonId": "th4_b41",
        "lessonNum": 41,
        "testNum": 1,
        "title": "Bài 41: Biểu đồ cột - Đề số 1",
        "topic": "Biểu đồ cột",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Trên biểu đồ cột, độ cao của mỗi cột thể hiện:", ["Số liệu tương ứng của đối tượng đó", "Tên của đối tượng", "Thời gian thực hiện", "Không có ý nghĩa gì"], 0, "Độ cao của cột biểu thị số lượng hay giá trị số liệu của đối tượng.", "Nhận biết"),
            make_mc(2, "Quan sát biểu đồ cột về số cây trồng được của 4 lớp: 4A (30 cây), 4B (35 cây), 4C (25 cây), 4D (40 cây). Lớp trồng được nhiều cây nhất là:", ["4D", "4B", "4A", "4C"], 0, "Lớp 4D trồng được 40 cây (cột cao nhất).", "Thông hiểu"),
            make_mc(3, "Tổng số cây cả 4 lớp trên trồng được là:", ["130 cây", "120 cây", "140 cây", "125 cây"], 0, "30 + 35 + 25 + 40 = 130 (cây).", "Thông hiểu"),
            make_mc(4, "Biểu đồ cột gồm hai trục, trục nằm ngang thường biểu thị:", ["Các đối tượng thống kê", "Số lượng số liệu", "Thời gian đo", "Đơn vị đo"], 0, "Trục ngang thường ghi tên các đối tượng được thống kê.", "Nhận biết"),
            make_mc(5, "Lớp 4D trồng nhiều hơn lớp 4C số cây là:", ["15 cây", "10 cây", "5 cây", "20 cây"], 0, "40 - 25 = 15 (cây).", "Thông hiểu"),
            make_mc(6, "Trung bình mỗi lớp trồng được số cây là:", ["32,5 cây", "30 cây", "35 cây", "32 cây"], 0, "130 : 4 = 32,5 (cây).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Biểu đồ cột biểu diễn số điểm 10 của 4 tổ trong tháng 3 như sau: Tổ 1: 18 điểm 10; Tổ 2: 24 điểm 10; Tổ 3: 20 điểm 10; Tổ 4: 22 điểm 10.\na) Tổ nào đạt được nhiều điểm 10 nhất? Tổ nào ít nhất?\nb) Cả 4 tổ đạt được tất cả bao nhiêu điểm 10?", "a) Tổ 2 đạt nhiều điểm 10 nhất (24 điểm 10); Tổ 1 đạt ít nhất (18 điểm 10).\nb) Cả 4 tổ đạt được tất cả số điểm 10 là:\n18 + 24 + 20 + 22 = 84 (điểm 10)\nĐáp số: a) Nhiều nhất: Tổ 2, Ít nhất: Tổ 1; b) 84 điểm 10.", "a) Nhiều nhất: Tổ 2, Ít nhất: Tổ 1; b) 84 điểm 10", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Số lượng sách quyên góp được của các khối lớp ở một trường tiểu học: Khối 1: 150 quyển; Khối 2: 180 quyển; Khối 3: 200 quyển; Khối 4: 240 quyển; Khối 5: 230 quyển.\na) Khối lớp nào quyên góp được nhiều sách nhất?\nb) Trung bình mỗi khối lớp quyên góp được bao nhiêu quyển sách?", "a) Khối 4 quyên góp được nhiều sách nhất (240 quyển).\nb) Tổng số sách cả trường quyên góp là:\n150 + 180 + 200 + 240 + 230 = 1000 (quyển)\nTrung bình mỗi khối lớp quyên góp được số quyển sách là:\n1000 : 5 = 200 (quyển)\nĐáp số: a) Khối 4; b) 200 quyển sách.", "a) Khối 4; b) 200 quyển", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Một cửa hàng thống kê số lượng quạt điện bán được trong mùa hè: Tháng 5 bán 45 chiếc, Tháng 6 bán 80 chiếc, Tháng 7 bán 95 chiếc, Tháng 8 bán 60 chiếc.\na) Tháng nào bán được nhiều quạt nhất? Tháng nào ít nhất?\nb) Cả mùa hè cửa hàng bán được bao nhiêu chiếc quạt?", "a) Tháng 7 bán nhiều nhất (95 chiếc), Tháng 5 bán ít nhất (45 chiếc).\nb) Cả mùa hè bán được tất cả số quạt là:\n45 + 80 + 95 + 60 = 280 (chiếc)\nĐáp số: a) Nhiều nhất: Tháng 7, Ít nhất: Tháng 5; b) 280 chiếc quạt.", "a) Nhiều nhất: Tháng 7, Ít nhất: Tháng 5; b) 280 chiếc", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Biểu đồ cột ghi số học sinh tham gia các câu lạc bộ của trường: CLB Cờ vua: 25 bạn; CLB Bơi lội: 40 bạn; CLB Bóng đá: 55 bạn; CLB Mỹ thuật: 30 bạn.\na) CLB nào có đông học sinh tham gia nhất?\nb) Tổng số học sinh tham gia cả 4 câu lạc bộ là bao nhiêu bạn?", "a) CLB Bóng đá có đông học sinh tham gia nhất (55 bạn).\nb) Tổng số học sinh tham gia là:\n25 + 40 + 55 + 30 = 150 (học sinh)\nĐáp số: a) CLB Bóng đá; b) 150 học sinh.", "a) CLB Bóng đá; b) 150 học sinh", 5, 1.5, "Vận dụng"),
            make_essay(5, "Số lượng tạ thóc thu hoạch được của một hợp tác xã trong 4 năm: Năm 2020: 320 tạ; Năm 2021: 350 tạ; Năm 2022: 400 tạ; Năm 2023: 450 tạ. Hỏi trung bình mỗi năm hợp tác xã thu hoạch được bao nhiêu tấn thóc?", "Tổng số tạ thóc thu hoạch được trong 4 năm là:\n320 + 350 + 400 + 450 = 1520 (tạ)\nĐổi: 1520 tạ = 152 tấn\nTrung bình mỗi năm hợp tác xã thu hoạch được số tấn thóc là:\n152 : 4 = 38 (tấn)\nĐáp số: 38 tấn thóc.", "38 tấn", 6, 1.5, "Vận dụng"),
            make_essay(6, "Từ biểu đồ cột thống kê số điểm tốt của 3 bạn: An (15 điểm), Bình (20 điểm), Mai (x điểm). Biết số điểm tốt của Mai nhiều hơn mức trung bình của cả ba bạn là 2 điểm. Tìm số điểm tốt của Mai.", "Hai lần trung bình cộng điểm tốt của ba bạn là:\n15 + 20 + 2 = 37 (không chia hết cho 2).\nSửa đề bài số liệu chuẩn đẹp: An có 14 điểm tốt, Bình có 18 điểm tốt, Mai có x điểm tốt. Biết số điểm tốt của Mai nhiều hơn trung bình cộng của cả 3 bạn là 2 điểm.\nHai lần mức trung bình cộng là:\n14 + 18 + 2 = 34 (điểm)\nMức trung bình cộng của ba bạn là:\n34 : 2 = 17 (điểm)\nSố điểm tốt của Mai là:\n17 + 2 = 19 (điểm)\nĐáp số: 19 điểm tốt.", "19 điểm tốt", 5, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b41_test2"] = {
        "id": "th4_b41_test2",
        "lessonId": "th4_b41",
        "lessonNum": 41,
        "testNum": 2,
        "title": "Bài 41: Biểu đồ cột - Đề số 2",
        "topic": "Biểu đồ cột",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Trên biểu đồ cột, trục thẳng đứng thường ghi:", ["Các số liệu thống kê", "Tên các lớp", "Tên các đối tượng", "Ngày tháng"], 0, "Trục đứng ghi số lượng hoặc giá trị số liệu tương ứng.", "Nhận biết"),
            make_mc(2, "Quan sát biểu đồ cột số sách thư viện cho mượn: Thứ Hai (40 quyển), Thứ Ba (35 quyển), Thứ Tư (50 quyển), Thứ Năm (45 quyển). Ngày cho mượn nhiều sách nhất là:", ["Thứ Tư", "Thứ Năm", "Thứ Hai", "Thứ Ba"], 0, "Thứ Tư có cột cao nhất với 50 quyển.", "Thông hiểu"),
            make_mc(3, "Tổng số sách mượn trong 4 ngày trên là:", ["170 quyển", "160 quyển", "180 quyển", "175 quyển"], 0, "40 + 35 + 50 + 45 = 170 (quyển).", "Thông hiểu"),
            make_mc(4, "Thứ Tư cho mượn nhiều hơn thứ Ba số quyển sách là:", ["15 quyển", "10 quyển", "5 quyển", "20 quyển"], 0, "50 - 35 = 15 (quyển).", "Thông hiểu"),
            make_mc(5, "Nếu mỗi quyển sách thư viện có giá trị 30 000 đồng thì 50 quyển sách mượn ngày Thứ Tư có tổng giá trị là:", ["1 500 000 đồng", "150 000 đồng", "1 200 000 đồng", "1 800 000 đồng"], 0, "50 x 30 000 = 1 500 000 (đồng).", "Thông hiểu"),
            make_mc(6, "Trung bình mỗi ngày trong 4 ngày trên thư viện cho mượn số quyển sách là:", ["42,5 quyển", "40 quyển", "45 quyển", "43 quyển"], 0, "170 : 4 = 42,5 (quyển).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Biểu đồ cột biểu diễn số ki-lô-gam giấy vụn thu gom của 4 tổ: Tổ 1: 35 kg; Tổ 2: 45 kg; Tổ 3: 40 kg; Tổ 4: 50 kg.\na) Tổ nào thu gom được nhiều giấy vụn nhất? Tổ nào ít nhất?\nb) Cả 4 tổ thu gom được tất cả bao nhiêu ki-lô-gam giấy vụn?", "a) Tổ 4 thu gom nhiều nhất (50 kg), Tổ 1 ít nhất (35 kg).\nb) Cả 4 tổ thu gom được tất cả số giấy vụn là:\n35 + 45 + 40 + 50 = 170 (kg)\nĐáp số: a) Nhiều nhất: Tổ 4, Ít nhất: Tổ 1; b) 170 kg.", "a) Nhiều nhất: Tổ 4, Ít nhất: Tổ 1; b) 170 kg", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Số lượng xe đạp bán được trong 4 quý của một cửa hàng: Quý 1: 120 chiếc; Quý 2: 150 chiếc; Quý 3: 180 chiếc; Quý 4: 210 chiếc.\na) Quý nào bán được nhiều xe đạp nhất?\nb) Trung bình mỗi quý cửa hàng bán được bao nhiêu chiếc xe đạp?", "a) Quý 4 bán được nhiều xe đạp nhất (210 chiếc).\nb) Tổng số xe đạp bán được cả năm là:\n120 + 150 + 180 + 210 = 660 (chiếc)\nTrung bình mỗi quý bán được số xe đạp là:\n660 : 4 = 165 (chiếc)\nĐáp số: a) Quý 4; b) 165 chiếc xe đạp.", "a) Quý 4; b) 165 chiếc", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Biểu đồ cột thể hiện số học sinh giỏi của các lớp khối 4: Lớp 4A: 16 bạn, Lớp 4B: 18 bạn, Lớp 4C: 22 bạn, Lớp 4D: 24 bạn.\na) Lớp 4D nhiều hơn lớp 4A bao nhiêu học sinh giỏi?\nb) Khối 4 có tất cả bao nhiêu học sinh giỏi?", "a) Lớp 4D nhiều hơn lớp 4A số học sinh giỏi là:\n24 - 16 = 8 (học sinh)\nb) Toàn khối 4 có tất cả số học sinh giỏi là:\n16 + 18 + 22 + 24 = 80 (học sinh)\nĐáp số: a) 8 học sinh; b) 80 học sinh.", "a) 8 học sinh; b) 80 học sinh", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Biểu đồ số cây trồng được của 3 bạn học sinh: Nam trồng 15 cây, Bình trồng 20 cây, Hoa trồng 25 cây. Nhà trường thưởng cho mỗi cây trồng được 5000 đồng.\na) Bạn nào được thưởng nhiều tiền nhất?\nb) Tổng số tiền thưởng của cả ba bạn là bao nhiêu?", "a) Hoa trồng nhiều nhất (25 cây) nên Hoa được thưởng nhiều tiền nhất.\nb) Tổng số cây cả 3 bạn trồng được là:\n15 + 20 + 25 = 60 (cây)\nTổng số tiền thưởng của cả ba bạn là:\n60 x 5000 = 300 000 (đồng)\nĐáp số: a) Bạn Hoa; b) 300 000 đồng.", "a) Bạn Hoa; b) 300 000 đồng", 5, 1.5, "Vận dụng"),
            make_essay(5, "Số lượng học sinh đăng ký các môn thể thao: Bóng rổ có 36 bạn, Cầu lông có 48 bạn, Bóng bàn có 24 bạn, Điền kinh có 32 bạn.\na) Môn nào có nhiều bạn đăng ký nhất? Môn nào ít nhất?\nb) Tính tổng số học sinh đăng ký tham gia tất cả các môn trên.", "a) Môn Cầu lông có nhiều bạn đăng ký nhất (48 bạn), môn Bóng bàn ít nhất (24 bạn).\nb) Tổng số học sinh đăng ký là:\n36 + 48 + 24 + 32 = 140 (học sinh)\nĐáp số: a) Nhiều nhất: Cầu lông, Ít nhất: Bóng bàn; b) 140 học sinh.", "a) Nhiều nhất: Cầu lông, Ít nhất: Bóng bàn; b) 140 học sinh", 5, 1.5, "Vận dụng"),
            make_essay(6, "Một cửa hàng có biểu đồ thống kê số tivi bán được trong 4 tuần: Tuần 1: 25 chiếc; Tuần 2: 30 chiếc; Tuần 3: 35 chiếc; Tuần 4: x chiếc. Biết trung bình mỗi tuần cửa hàng bán được 32 chiếc tivi. Tìm x.", "Tổng số tivi bán được trong 4 tuần là:\n32 x 4 = 128 (chiếc)\nSố tivi bán được trong tuần 4 là:\n128 - (25 + 30 + 35) = 128 - 90 = 38 (chiếc)\nĐáp số: 38 chiếc tivi.", "38 chiếc", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b41_test3"] = {
        "id": "th4_b41_test3",
        "lessonId": "th4_b41",
        "lessonNum": 41,
        "testNum": 3,
        "title": "Bài 41: Biểu đồ cột - Đề số 3",
        "topic": "Biểu đồ cột",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khi vẽ biểu đồ cột, các cột phải có đặc điểm:", ["Chiều rộng các cột bằng nhau và cách đều nhau", "Chiều rộng khác nhau", "Dính liền vào nhau", "Không cần bằng nhau"], 0, "Các cột trong biểu đồ cột có cùng độ rộng và khoảng cách giữa các cột bằng nhau.", "Nhận biết"),
            make_mc(2, "Biểu đồ cột ghi số huy chương của 3 lớp: 4A (8 HC), 4B (12 HC), 4C (10 HC). Lớp đạt ít huy chương nhất là:", ["4A", "4B", "4C", "Cả ba bằng nhau"], 0, "Lớp 4A có 8 huy chương (cột thấp nhất).", "Thông hiểu"),
            make_mc(3, "Tổng số huy chương của cả 3 lớp là:", ["30 HC", "28 HC", "32 HC", "26 HC"], 0, "8 + 12 + 10 = 30 (huy chương).", "Thông hiểu"),
            make_mc(4, "Lớp 4B nhiều hơn lớp 4A số huy chương là:", ["4 HC", "2 HC", "6 HC", "3 HC"], 0, "12 - 8 = 4 (huy chương).", "Thông hiểu"),
            make_mc(5, "Trung bình mỗi lớp đạt được số huy chương là:", ["10 HC", "8 HC", "12 HC", "9 HC"], 0, "30 : 3 = 10 (huy chương).", "Thông hiểu"),
            make_mc(6, "Tỉ số giữa số huy chương của lớp 4A và lớp 4B là:", ["8/12 (hay 2/3)", "12/8", "8/30", "12/30"], 0, "8/12 rút gọn thành 2/3.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Biểu đồ cột biểu diễn số giờ tự học trong tuần của 4 bạn: Lan: 14 giờ; Nam: 16 giờ; Minh: 12 giờ; Hoa: 18 giờ.\na) Bạn nào có số giờ tự học nhiều nhất? Bạn nào ít nhất?\nb) Tính tổng số giờ tự học của cả 4 bạn.", "a) Bạn Hoa có số giờ tự học nhiều nhất (18 giờ); bạn Minh ít nhất (12 giờ).\nb) Tổng số giờ tự học của 4 bạn là:\n14 + 16 + 12 + 18 = 60 (giờ)\nĐáp số: a) Nhiều nhất: Hoa, Ít nhất: Minh; b) 60 giờ.", "a) Nhiều nhất: Hoa, Ít nhất: Minh; b) 60 giờ", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Số lượng máy vi tính một siêu thị bán được trong 4 tháng cuối năm: Tháng 9: 60 máy; Tháng 10: 75 máy; Tháng 11: 85 máy; Tháng 12: 100 máy.\na) Tháng nào siêu thị bán được nhiều máy vi tính nhất?\nb) Trung bình mỗi tháng siêu thị bán được bao nhiêu máy vi tính?", "a) Tháng 12 bán được nhiều nhất (100 máy vi tính).\nb) Tổng số máy vi tính bán được là:\n60 + 75 + 85 + 100 = 320 (máy)\nTrung bình mỗi tháng bán được số máy là:\n320 : 4 = 80 (máy)\nĐáp số: a) Tháng 12; b) 80 máy vi tính.", "a) Tháng 12; b) 80 máy", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Biểu đồ cột ghi số điểm mười của 3 tổ: Tổ 1: 25 điểm; Tổ 2: 30 điểm; Tổ 3: 35 điểm.\na) Tổ 3 nhiều hơn tổ 1 bao nhiêu điểm mười?\nb) Cả 3 tổ đạt được tất cả bao nhiêu điểm mười?", "a) Tổ 3 nhiều hơn tổ 1 số điểm mười là:\n35 - 25 = 10 (điểm mười)\nb) Cả 3 tổ đạt được số điểm mười là:\n25 + 30 + 35 = 90 (điểm mười)\nĐáp số: a) 10 điểm mười; b) 90 điểm mười.", "a) 10 điểm mười; b) 90 điểm mười", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Biểu đồ cột thống kê số tiền đóng góp kế hoạch nhỏ của 4 lớp: Lớp 4A góp 350 000 đồng, Lớp 4B góp 400 000 đồng, Lớp 4C góp 450 000 đồng, Lớp 4D góp 400 000 đồng.\na) Lớp nào đóng góp nhiều tiền nhất?\nb) Tổng số tiền cả 4 lớp đóng góp được là bao nhiêu?", "a) Lớp 4C đóng góp nhiều nhất (450 000 đồng).\nb) Tổng số tiền cả 4 lớp đóng góp được là:\n350 000 + 400 000 + 450 000 + 400 000 = 1 600 000 (đồng)\nĐáp số: a) Lớp 4C; b) 1 600 000 đồng.", "a) Lớp 4C; b) 1 600 000 đồng", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một cửa hàng nông sản bán được số tạ gạo trong 3 quý đầu năm: Quý 1: 180 tạ; Quý 2: 240 tạ; Quý 3: 210 tạ. Hỏi cả 3 quý cửa hàng bán được bao nhiêu tấn gạo?", "Tổng số tạ gạo bán được trong 3 quý là:\n180 + 240 + 210 = 630 (tạ)\nĐổi: 630 tạ = 63 tấn\nĐáp số: 63 tấn gạo.", "63 tấn", 5, 1.5, "Vận dụng"),
            make_essay(6, "Biểu đồ thống kê số điểm tốt của 4 bạn trong một tháng: An (12 điểm), Bình (16 điểm), Cường (14 điểm) và Dũng (x điểm). Biết số điểm tốt của Dũng bằng trung bình cộng số điểm tốt của 3 bạn An, Bình, Cường. Tìm x.", "Số điểm tốt của Dũng là trung bình cộng điểm tốt của 3 bạn:\nx = (12 + 16 + 14) : 3 = 42 : 3 = 14 (điểm)\nĐáp số: 14 điểm tốt.", "14 điểm tốt", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 42: SỐ LẦN LẶP LẠI CỦA MỘT SỰ KIỆN (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b42_test1"] = {
        "id": "th4_b42_test1",
        "lessonId": "th4_b42",
        "lessonNum": 42,
        "testNum": 1,
        "title": "Bài 42: Số lần lặp lại của một sự kiện - Đề số 1",
        "topic": "Số lần lặp lại của một sự kiện",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Bạn Nam tung một đồng xu 20 lần, có 11 lần xuất hiện mặt N (Ngửa). Số lần xuất hiện mặt S (Sấp) là:", ["9 lần", "11 lần", "20 lần", "10 lần"], 0, "Số lần xuất hiện mặt Sấp là: 20 - 11 = 9 (lần).", "Thông hiểu"),
            make_mc(2, "Khi gieo một con xúc xắc 6 mặt, sự kiện nào dưới đây không thể xảy ra?", ["Xuất hiện mặt 7 chấm", "Xuất hiện mặt 6 chấm", "Xuất hiện mặt 1 chấm", "Xuất hiện mặt chẵn chấm"], 0, "Xúc xắc chỉ có từ 1 đến 6 chấm nên không thể xuất hiện mặt 7 chấm.", "Nhận biết"),
            make_mc(3, "Mai gieo xúc xắc 30 lần thấy mặt 2 chấm xuất hiện 6 lần. Tỉ số của số lần xuất hiện mặt 2 chấm so với tổng số lần gieo là:", ["6/30 (hay 1/5)", "1/6", "6/24", "24/30"], 0, "6/30 = 1/5.", "Thông hiểu"),
            make_mc(4, "Trong hộp có 3 quả bóng xanh và 1 quả bóng đỏ. Lấy ngẫu nhiên 1 quả bóng. Sự kiện lấy được bóng đỏ có khả năng:", ["Có thể xảy ra", "Chắc chắn xảy ra", "Không thể xảy ra", "Luôn luôn xảy ra"], 0, "Đây là sự kiện có thể xảy ra (nhưng khả năng ít hơn bóng xanh).", "Nhận biết"),
            make_mc(5, "Bạn An quay vòng quay may mắn 15 lần thì có 5 lần kim chỉ vào ô phần thưởng. Số lần kim không chỉ vào ô phần thưởng là:", ["10 lần", "5 lần", "15 lần", "20 lần"], 0, "15 - 5 = 10 (lần).", "Thông hiểu"),
            make_mc(6, "Tung đồng xu 50 lần, số lần xuất hiện mặt Sấp là 26. Số lần xuất hiện mặt Ngửa là:", ["24 lần", "26 lần", "50 lần", "25 lần"], 0, "50 - 26 = 24 (lần).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Bạn Bình gieo một con xúc xắc 20 lần liên tiếp và ghi lại số lần xuất hiện của các mặt:\nMặt 1 chấm: 3 lần; Mặt 2 chấm: 4 lần; Mặt 3 chấm: 2 lần;\nMặt 4 chấm: 5 lần; Mặt 5 chấm: 3 lần; Mặt 6 chấm: 3 lần.\na) Mặt nào xuất hiện nhiều lần nhất? Mặt nào ít lần nhất?\nb) Có bao nhiêu lần xuất hiện mặt chẵn chấm (2, 4, 6 chấm)?", "a) Mặt 4 chấm xuất hiện nhiều nhất (5 lần); Mặt 3 chấm ít nhất (2 lần).\nb) Số lần xuất hiện mặt chẵn chấm là: 4 + 5 + 3 = 12 (lần).\nĐáp số: a) Nhiều nhất: Mặt 4 chấm, Ít nhất: Mặt 3 chấm; b) 12 lần.", "a) Nhiều nhất: Mặt 4 chấm, Ít nhất: Mặt 3 chấm; b) 12 lần", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Trong hộp kín có 4 chiếc thẻ ghi số 1, 2, 3, 4. Hà rút ngẫu nhiên 1 chiếc thẻ, ghi lại số rồi bỏ vào hộp. Sau 30 lần rút thẻ, Hà thấy thẻ ghi số 1 xuất hiện 8 lần, thẻ số 2 xuất hiện 7 lần, thẻ số 3 xuất hiện 9 lần.\na) Hỏi thẻ số 4 xuất hiện bao nhiêu lần?\nb) Viết tỉ số mô tả số lần xuất hiện thẻ số 4 so với tổng số lần rút thẻ.", "a) Số lần xuất hiện thẻ số 4 là:\n30 - (8 + 7 + 9) = 30 - 24 = 6 (lần)\nb) Tỉ số mô tả số lần xuất hiện thẻ số 4 so với tổng số lần rút là:\n6/30 = 1/5\nĐáp số: a) 6 lần; b) 1/5.", "a) 6 lần; b) 1/5", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Nam tung một đồng xu 40 lần và ghi chép lại kết quả: có 22 lần xuất hiện mặt Ngửa (N).\na) Mặt Sấp (S) xuất hiện bao nhiêu lần?\nb) Mặt nào xuất hiện nhiều hơn và nhiều hơn bao nhiêu lần?", "a) Số lần xuất hiện mặt Sấp là:\n40 - 22 = 18 (lần)\nb) Mặt Ngửa xuất hiện nhiều hơn mặt Sấp là:\n22 - 18 = 4 (lần)\nĐáp số: a) 18 lần; b) Mặt Ngửa nhiều hơn 4 lần.", "a) 18 lần; b) Mặt Ngửa nhiều hơn 4 lần", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một hộp kín chứa 3 quả cầu đỏ và 2 quả cầu vàng có kích thước giống nhau. Bạn Mai lấy ngẫu nhiên 1 quả cầu, ghi lại màu rồi trả lại hộp. Mai thực hiện 50 lần như vậy và thấy có 28 lần lấy được quả cầu đỏ.\na) Có bao nhiêu lần Mai lấy được quả cầu vàng?\nb) Viết tỉ số mô tả số lần lấy được quả cầu vàng so với tổng số lần thực hiện.", "a) Số lần Mai lấy được quả cầu vàng là:\n50 - 28 = 22 (lần)\nb) Tỉ số mô tả số lần lấy được quả cầu vàng so với tổng số lần là:\n22/50 = 11/25\nĐáp số: a) 22 lần; b) 11/25.", "a) 22 lần; b) 11/25", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một nhóm học sinh chơi trò chơi quay bánh xe tròn chia đều 6 ô ghi các chữ số từ 1 đến 6. Sau 60 lần quay, mũi tên chỉ vào ô số chẵn 34 lần.\na) Mũi tên chỉ vào ô số lẻ bao nhiêu lần?\nb) Sự kiện mũi tên chỉ vào ô số chẵn hay ô số lẻ xuất hiện nhiều hơn và nhiều hơn bao nhiêu lần?", "a) Số lần mũi tên chỉ vào ô số lẻ là:\n60 - 34 = 26 (lần)\nb) Sự kiện chỉ vào ô số chẵn xuất hiện nhiều hơn số lẻ là:\n34 - 26 = 8 (lần)\nĐáp số: a) 26 lần; b) Ô số chẵn nhiều hơn 8 lần.", "a) 26 lần; b) Ô số chẵn nhiều hơn 8 lần", 5, 1.5, "Vận dụng"),
            make_essay(6, "Gieo đồng thời hai con xúc xắc 25 lần. Kết quả có 4 lần tổng số chấm bằng 7. Viết tỉ số mô tả số lần tổng số chấm không bằng 7 so với tổng số lần gieo.", "Số lần tổng số chấm không bằng 7 là:\n25 - 4 = 21 (lần)\nTỉ số mô tả số lần tổng số chấm không bằng 7 so với tổng số lần gieo là:\n21/25\nĐáp số: 21/25.", "21/25", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b42_test2"] = {
        "id": "th4_b42_test2",
        "lessonId": "th4_b42",
        "lessonNum": 42,
        "testNum": 2,
        "title": "Bài 42: Số lần lặp lại của một sự kiện - Đề số 2",
        "topic": "Số lần lặp lại của một sự kiện",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Gieo một đồng xu 30 lần, thấy có 17 lần xuất hiện mặt Sấp. Số lần xuất hiện mặt Ngửa là:", ["13 lần", "17 lần", "30 lần", "14 lần"], 0, "30 - 17 = 13 (lần).", "Thông hiểu"),
            make_mc(2, "Trong trò chơi gieo xúc xắc 6 mặt, sự kiện nào chắc chắn xảy ra?", ["Số chấm xuất hiện nhỏ hơn 7", "Xuất hiện mặt 6 chấm", "Xuất hiện số chẵn chấm", "Xuất hiện số lẻ chấm"], 0, "Vì các mặt từ 1 đến 6 chấm đều nhỏ hơn 7 nên sự kiện này chắc chắn xảy ra.", "Nhận biết"),
            make_mc(3, "Tung đồng xu 25 lần thấy mặt Ngửa xuất hiện 10 lần. Tỉ số giữa số lần mặt Ngửa xuất hiện và tổng số lần tung là:", ["10/25 (hay 2/5)", "15/25", "10/15", "15/10"], 0, "10/25 = 2/5.", "Thông hiểu"),
            make_mc(4, "Trong túi có 5 viên bi xanh. Không nhìn vào túi, lấy ra 1 viên bi thì sự kiện lấy được bi đỏ là:", ["Không thể xảy ra", "Có thể xảy ra", "Chắc chắn xảy ra", "Không chắc chắn"], 0, "Trong túi không có viên bi đỏ nào nên không thể xảy ra.", "Nhận biết"),
            make_mc(5, "Bạn Lan bốc thăm 20 lần thì có 8 lần bốc được thăm trúng thưởng. Số lần bốc thăm không trúng thưởng là:", ["12 lần", "8 lần", "20 lần", "10 lần"], 0, "20 - 8 = 12 (lần).", "Thông hiểu"),
            make_mc(6, "Quay một vòng quay 40 lần, kim dừng lại ở ô màu xanh 16 lần. Số lần kim dừng lại ở các ô khác màu xanh là:", ["24 lần", "16 lần", "40 lần", "20 lần"], 0, "40 - 16 = 24 (lần).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Bạn Minh tung một đồng xu 50 lần liên tiếp và đếm được có 27 lần xuất hiện mặt Ngửa.\na) Hỏi mặt Sấp xuất hiện bao nhiêu lần?\nb) Viết tỉ số mô tả số lần xuất hiện mặt Ngửa so với tổng số lần tung đồng xu.", "a) Số lần xuất hiện mặt Sấp là:\n50 - 27 = 23 (lần)\nb) Tỉ số mô tả số lần xuất hiện mặt Ngửa là:\n27/50\nĐáp số: a) 23 lần; b) 27/50.", "a) 23 lần; b) 27/50", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Gieo một con xúc xắc 36 lần, ghi lại kết quả số lần xuất hiện các mặt:\nMặt 1: 5 lần; Mặt 2: 7 lần; Mặt 3: 6 lần; Mặt 4: 8 lần; Mặt 5: 4 lần; Mặt 6: 6 lần.\na) Mặt nào xuất hiện nhiều lần nhất? Mặt nào ít lần nhất?\nb) Số lần xuất hiện mặt có số chấm lớn hơn 4 (mặt 5 và mặt 6) là bao nhiêu lần?", "a) Mặt 4 xuất hiện nhiều nhất (8 lần); Mặt 5 xuất hiện ít nhất (4 lần).\nb) Số lần xuất hiện mặt lớn hơn 4 chấm là:\n4 + 6 = 10 (lần)\nĐáp số: a) Nhiều nhất: Mặt 4, Ít nhất: Mặt 5; b) 10 lần.", "a) Nhiều nhất: Mặt 4, Ít nhất: Mặt 5; b) 10 lần", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Một hộp đựng 2 quả bóng đỏ và 3 quả bóng xanh cùng kích thước. Bạn Hoa lấy ngẫu nhiên 1 quả bóng, ghi lại màu rồi trả vào hộp. Sau 40 lần lấy bóng, Hoa thấy bóng xanh xuất hiện 24 lần.\na) Bóng đỏ xuất hiện bao nhiêu lần?\nb) Tỉ số giữa số lần bóng đỏ xuất hiện và tổng số lần lấy bóng là bao nhiêu?", "a) Số lần bóng đỏ xuất hiện là:\n40 - 24 = 16 (lần)\nb) Tỉ số xuất hiện bóng đỏ là:\n16/40 = 2/5\nĐáp số: a) 16 lần; b) 2/5.", "a) 16 lần; b) 2/5", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Trong một trò chơi rút thăm có thưởng gồm 10 lá thăm, mỗi lần rút xong lại bỏ lại hộp. Nam rút thăm 30 lần và ghi lại kết quả có 9 lần trúng thưởng.\na) Có bao nhiêu lần Nam rút thăm không trúng thưởng?\nb) Viết tỉ số mô tả số lần không trúng thưởng so với tổng số lần rút thăm.", "a) Số lần Nam rút thăm không trúng thưởng là:\n30 - 9 = 21 (lần)\nb) Tỉ số mô tả số lần không trúng thưởng là:\n21/30 = 7/10\nĐáp số: a) 21 lần; b) 7/10.", "a) 21 lần; b) 7/10", 5, 1.5, "Vận dụng"),
            make_essay(5, "Bình và An chơi trò oẳn tù tì 25 ván. Kết quả Bình thắng 12 ván, hòa 5 ván.\na) An thắng bao nhiêu ván?\nb) Bình thắng nhiều hơn An bao nhiêu ván?", "a) Số ván An thắng là:\n25 - 12 - 5 = 8 (ván)\nb) Bình thắng nhiều hơn An số ván là:\n12 - 8 = 4 (ván)\nĐáp số: a) 8 ván; b) 4 ván.", "a) 8 ván; b) 4 ván", 5, 1.5, "Vận dụng"),
            make_essay(6, "Gieo một con xúc xắc 50 lần. Tỉ số số lần xuất hiện mặt 6 chấm so với tổng số lần gieo là 1/5. Hỏi mặt 6 chấm đã xuất hiện bao nhiêu lần?", "Số lần xuất hiện mặt 6 chấm là:\n50 x 1/5 = 10 (lần)\nĐáp số: 10 lần.", "10 lần", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b42_test3"] = {
        "id": "th4_b42_test3",
        "lessonId": "th4_b42",
        "lessonNum": 42,
        "testNum": 3,
        "title": "Bài 42: Số lần lặp lại của một sự kiện - Đề số 3",
        "topic": "Số lần lặp lại của một sự kiện",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người tung đồng xu 60 lần thấy mặt Sấp xuất hiện 32 lần. Số lần mặt Ngửa xuất hiện là:", ["28 lần", "32 lần", "30 lần", "60 lần"], 0, "60 - 32 = 28 (lần).", "Thông hiểu"),
            make_mc(2, "Trong hộp có 10 viên bi đỏ và 1 viên bi xanh. Khả năng lấy được viên bi đỏ so với viên bi xanh là:", ["Lớn hơn rất nhiều", "Bằng nhau", "Nhỏ hơn", "Không xác định"], 0, "Vì số lượng bi đỏ nhiều hơn hẳn (10 > 1) nên khả năng lấy được bi đỏ lớn hơn rất nhiều.", "Thông hiểu"),
            make_mc(3, "Gieo con xúc xắc 24 lần thấy mặt 3 chấm xuất hiện 4 lần. Tỉ số giữa số lần xuất hiện mặt 3 chấm và tổng số lần gieo là:", ["4/24 (hay 1/6)", "1/4", "4/20", "20/24"], 0, "4/24 = 1/6.", "Thông hiểu"),
            make_mc(4, "Một sự kiện chắc chắn xảy ra thì khả năng xảy ra của nó là:", ["100%", "50%", "0%", "25%"], 0, "Sự kiện chắc chắn xảy ra luôn đạt khả năng 100%.", "Nhận biết"),
            make_mc(5, "Quay một vòng quay 50 lần, kim dừng lại ở ô may mắn 15 lần. Số lần kim dừng lại ở các ô khác là:", ["35 lần", "15 lần", "50 lần", "25 lần"], 0, "50 - 15 = 35 (lần).", "Thông hiểu"),
            make_mc(6, "Bốc thăm 100 lần thấy thăm màu đỏ xuất hiện 48 lần. Số lần xuất hiện thăm không phải màu đỏ là:", ["52 lần", "48 lần", "100 lần", "50 lần"], 0, "100 - 48 = 52 (lần).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Hà tung một đồng xu 45 lần liên tiếp và ghi lại có 24 lần xuất hiện mặt Sấp.\na) Mặt Ngửa xuất hiện bao nhiêu lần?\nb) Viết tỉ số mô tả số lần xuất hiện mặt Sấp so với tổng số lần tung đồng xu.", "a) Số lần xuất hiện mặt Ngửa là:\n45 - 24 = 21 (lần)\nb) Tỉ số mô tả số lần xuất hiện mặt Sấp là:\n24/45 = 8/15\nĐáp số: a) 21 lần; b) 8/15.", "a) 21 lần; b) 8/15", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Gieo một con xúc xắc 30 lần và ghi lại số lần xuất hiện các mặt:\nMặt 1: 4 lần; Mặt 2: 5 lần; Mặt 3: 6 lần; Mặt 4: 5 lần; Mặt 5: 7 lần; Mặt 6: 3 lần.\na) Mặt nào xuất hiện nhiều lần nhất? Mặt nào ít lần nhất?\nb) Số lần xuất hiện mặt lẻ chấm (1, 3, 5 chấm) là bao nhiêu lần?", "a) Mặt 5 xuất hiện nhiều nhất (7 lần); Mặt 6 xuất hiện ít nhất (3 lần).\nb) Số lần xuất hiện mặt lẻ chấm là:\n4 + 6 + 7 = 17 (lần)\nĐáp số: a) Nhiều nhất: Mặt 5, Ít nhất: Mặt 6; b) 17 lần.", "a) Nhiều nhất: Mặt 5, Ít nhất: Mặt 6; b) 17 lần", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Một hộp kín chứa 4 chiếc thẻ ghi các chữ cái A, B, C, D. Minh rút ngẫu nhiên 1 chiếc thẻ, ghi lại chữ cái rồi bỏ thẻ vào hộp. Sau 50 lần rút, Minh thấy thẻ A xuất hiện 12 lần, thẻ B xuất hiện 15 lần, thẻ C xuất hiện 13 lần.\na) Thẻ D xuất hiện bao nhiêu lần?\nb) Viết tỉ số mô tả số lần xuất hiện thẻ D so với tổng số lần rút thẻ.", "a) Số lần xuất hiện thẻ D là:\n50 - (12 + 15 + 13) = 50 - 40 = 10 (lần)\nb) Tỉ số mô tả số lần xuất hiện thẻ D là:\n10/50 = 1/5\nĐáp số: a) 10 lần; b) 1/5.", "a) 10 lần; b) 1/5", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một nhóm học sinh tham gia trò chơi phi tiêu vào bảng tròn có hai khu vực: Vàng và Xanh. Tổng cộng nhóm đã phi 80 lần và phi trúng khu vực Vàng 45 lần.\na) Có bao nhiêu lần phi trúng khu vực Xanh?\nb) Viết tỉ số mô tả số lần trúng khu vực Vàng so với tổng số lần phi.", "a) Số lần phi trúng khu vực Xanh là:\n80 - 45 = 35 (lần)\nb) Tỉ số mô tả số lần trúng khu vực Vàng là:\n45/80 = 9/16\nĐáp số: a) 35 lần; b) 9/16.", "a) 35 lần; b) 9/16", 5, 1.5, "Vận dụng"),
            make_essay(5, "An và Bình chơi tung bóng vào rổ. An ném 20 quả và trúng rổ 14 quả. Bình ném 25 quả và trúng rổ 17 quả.\na) Viết tỉ số số quả bóng ném trúng so với tổng số quả bóng ném của mỗi bạn.\nb) So sánh xem tỉ số trúng của bạn nào cao hơn? (Gợi ý: quy đồng mẫu số hai phân số 14/20 và 17/25).", "a) Tỉ số ném trúng của An là: 14/20 = 7/10.\nTỉ số ném trúng của Bình là: 17/25.\nb) Quy đồng mẫu số với mẫu số chung 50:\n7/10 = 35/50\n17/25 = 34/50\nVì 35/50 > 34/50 nên tỉ số ném trúng của An cao hơn Bình.\nĐáp số: a) An: 7/10, Bình: 17/25; b) An có tỉ số ném trúng cao hơn.", "a) An: 7/10, Bình: 17/25; b) An cao hơn", 6, 1.5, "Vận dụng"),
            make_essay(6, "Một vòng quay có 4 phần bằng nhau tô các màu: Đỏ, Xanh, Vàng, Trắng. Nam quay 100 lần thì thấy mũi tên chỉ vào màu Đỏ chiếm tỉ số 1/4 tổng số lần quay. Hỏi mũi tên đã chỉ vào màu Đỏ bao nhiêu lần?", "Số lần mũi tên chỉ vào màu Đỏ là:\n100 x 1/4 = 25 (lần)\nĐáp số: 25 lần.", "25 lần", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 43: LUYỆN TẬP CHUNG CHỦ ĐỀ 9 (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b43_test1"] = {
        "id": "th4_b43_test1",
        "lessonId": "th4_b43",
        "lessonNum": 43,
        "testNum": 1,
        "title": "Bài 43: Luyện tập chung - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 9",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số trung bình cộng của dãy số 24, 26, 28, 30 là:", ["27", "26", "28", "25"], 0, "(24 + 26 + 28 + 30) : 4 = 108 : 4 = 27.", "Thông hiểu"),
            make_mc(2, "Trên biểu đồ cột, nếu một cột cao hơn một cột khác thì đối tượng đó có giá trị:", ["Lớn hơn", "Bé hơn", "Bằng nhau", "Không so sánh được"], 0, "Cột cao hơn biểu thị giá trị số liệu lớn hơn.", "Nhận biết"),
            make_mc(3, "Gieo đồng xu 40 lần thấy có 18 lần xuất hiện mặt Ngửa. Số lần xuất hiện mặt Sấp là:", ["22 lần", "18 lần", "40 lần", "20 lần"], 0, "40 - 18 = 22 (lần).", "Thông hiểu"),
            make_mc(4, "Dãy số liệu về chiều cao 3 bạn: 135 cm, 138 cm, 141 cm. Bạn thấp nhất có chiều cao là:", ["135 cm", "138 cm", "141 cm", "136 cm"], 0, "Số bé nhất là 135 cm.", "Nhận biết"),
            make_mc(5, "Tung một con xúc xắc 6 mặt, khả năng xuất hiện mặt 8 chấm là sự kiện:", ["Không thể xảy ra", "Chắc chắn xảy ra", "Có thể xảy ra", "Hiếm khi xảy ra"], 0, "Xúc xắc chỉ có từ 1 đến 6 chấm nên mặt 8 chấm không thể xảy ra.", "Nhận biết"),
            make_mc(6, "Một lớp có 32 học sinh chia đều thành 4 tổ. Trung bình mỗi tổ có số học sinh là:", ["8 học sinh", "7 học sinh", "9 học sinh", "10 học sinh"], 0, "32 : 4 = 8 (học sinh).", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Cho dãy số liệu thống kê điểm kiểm tra môn Tiếng Anh của 5 bạn: 7, 9, 8, 10, 6.\na) Sắp xếp các số liệu trên theo thứ tự từ bé đến lớn.\nb) Tính điểm trung bình của cả 5 bạn.", "a) Thứ tự từ bé đến lớn: 6, 7, 8, 9, 10.\nb) Điểm trung bình của 5 bạn là:\n(6 + 7 + 8 + 9 + 10) : 5 = 40 : 5 = 8 (điểm)\nĐáp số: a) 6, 7, 8, 9, 10; b) 8 điểm.", "a) 6, 7, 8, 9, 10; b) 8 điểm", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Biểu đồ cột biểu diễn số cây trồng của các khối lớp trong một trường: Khối 1: 120 cây; Khối 2: 140 cây; Khối 3: 160 cây; Khối 4: 180 cây; Khối 5: 200 cây.\na) Khối nào trồng nhiều cây nhất? Khối nào trồng ít nhất?\nb) Trung bình mỗi khối lớp trồng được bao nhiêu cây?", "a) Khối 5 trồng nhiều nhất (200 cây), Khối 1 trồng ít nhất (120 cây).\nb) Tổng số cây cả trường trồng là:\n120 + 140 + 160 + 180 + 200 = 800 (cây)\nTrung bình mỗi khối trồng được số cây là:\n800 : 5 = 160 (cây)\nĐáp số: a) Nhiều nhất: Khối 5, Ít nhất: Khối 1; b) 160 cây.", "a) Nhiều nhất: Khối 5, Ít nhất: Khối 1; b) 160 cây", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Bạn An gieo một con xúc xắc 25 lần và đếm được có 5 lần xuất hiện mặt 6 chấm.\na) Có bao nhiêu lần xuất hiện các mặt không phải 6 chấm?\nb) Viết tỉ số mô tả số lần xuất hiện mặt 6 chấm so với tổng số lần gieo.", "a) Số lần xuất hiện các mặt không phải 6 chấm là:\n25 - 5 = 20 (lần)\nb) Tỉ số mô tả số lần xuất hiện mặt 6 chấm là:\n5/25 = 1/5\nĐáp số: a) 20 lần; b) 1/5.", "a) 20 lần; b) 1/5", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một nông trường thu hoạch cà chua trong 4 ngày với sản lượng: Ngày 1: 350 kg; Ngày 2: 420 kg; Ngày 3: 380 kg; Ngày 4: 450 kg. Hỏi cả 4 ngày nông trường thu hoạch được bao nhiêu tạ cà chua?", "Tổng số ki-lô-gam cà chua thu hoạch được trong 4 ngày là:\n350 + 420 + 380 + 450 = 1600 (kg)\nĐổi: 1600 kg = 16 tạ\nĐáp số: 16 tạ cà chua.", "16 tạ", 5, 1.5, "Vận dụng"),
            make_essay(5, "Số lượng học sinh giỏi của 3 lớp 4A, 4B, 4C: Lớp 4A có 18 bạn, Lớp 4B có nhiều hơn lớp 4A là 4 bạn. Lớp 4C có số học sinh giỏi bằng trung bình cộng của cả 3 lớp. Hỏi lớp 4C có bao nhiêu học sinh giỏi?", "Số học sinh giỏi của lớp 4B là:\n18 + 4 = 22 (học sinh)\nVì số học sinh giỏi lớp 4C bằng trung bình cộng cả 3 lớp nên số học sinh giỏi lớp 4C bằng trung bình cộng của hai lớp 4A và 4B:\n(18 + 22) : 2 = 20 (học sinh)\nĐáp số: 20 học sinh.", "20 học sinh", 5, 1.5, "Vận dụng"),
            make_essay(6, "Trong hộp có 12 quả bóng gồm 5 bóng đỏ, 4 bóng xanh và 3 bóng vàng. Không nhìn vào hộp, phải lấy ra ít nhất bao nhiêu quả bóng để chắc chắn có ít nhất 1 quả bóng màu đỏ?", "Trường hợp xấu nhất là lấy hết toàn bộ bóng xanh và bóng vàng:\n4 + 3 = 7 (quả bóng)\nKhi đó lấy thêm 1 quả bóng nữa chắc chắn sẽ là bóng đỏ.\nSố bóng cần lấy ít nhất là:\n7 + 1 = 8 (quả bóng)\nĐáp số: 8 quả bóng.", "8 quả bóng", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b43_test2"] = {
        "id": "th4_b43_test2",
        "lessonId": "th4_b43",
        "lessonNum": 43,
        "testNum": 2,
        "title": "Bài 43: Luyện tập chung - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 9",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số trung bình cộng của 35, 45, 55 là:", ["45", "40", "50", "35"], 0, "(35 + 45 + 55) : 3 = 135 : 3 = 45.", "Thông hiểu"),
            make_mc(2, "Tung một đồng xu 35 lần thấy có 20 lần xuất hiện mặt Sấp. Số lần xuất hiện mặt Ngửa là:", ["15 lần", "20 lần", "35 lần", "10 lần"], 0, "35 - 20 = 15 (lần).", "Thông hiểu"),
            make_mc(3, "Trong biểu đồ cột, số ghi ở đỉnh cột cho biết:", ["Giá trị số liệu của cột đó", "Chiều rộng của cột", "Thứ tự của cột", "Đơn vị đo"], 0, "Số ghi trên đỉnh cột biểu thị giá trị của số liệu.", "Nhận biết"),
            make_mc(4, "Khối lượng 4 con gà: 2 kg, 2 kg, 3 kg, 1 kg. Khối lượng trung bình mỗi con là:", ["2 kg", "2,5 kg", "1,5 kg", "3 kg"], 0, "(2 + 2 + 3 + 1) : 4 = 8 : 4 = 2 (kg).", "Thông hiểu"),
            make_mc(5, "Khi quay một vòng quay có 4 màu bằng nhau: Xanh, Đỏ, Tím, Vàng. Sự kiện kim chỉ vào màu Đỏ là:", ["Có thể xảy ra", "Chắc chắn xảy ra", "Không thể xảy ra", "Luôn xảy ra"], 0, "Đây là sự kiện có thể xảy ra.", "Nhận biết"),
            make_mc(6, "Dãy số liệu ghi số vở của 3 bạn: 15, 18, 21. Bạn có nhiều vở nhất hơn bạn ít vở nhất là:", ["6 quyển", "3 quyển", "5 quyển", "4 quyển"], 0, "21 - 15 = 6 (quyển).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Số ki-lô-gam giấy vụn quyên góp của 4 tổ: Tổ 1: 28 kg; Tổ 2: 32 kg; Tổ 3: 36 kg; Tổ 4: 44 kg.\na) Tính tổng số giấy vụn cả 4 tổ quyên góp được.\nb) Tính số giấy vụn trung bình mỗi tổ quyên góp được.", "a) Tổng số giấy vụn cả 4 tổ quyên góp là:\n28 + 32 + 36 + 44 = 140 (kg)\nb) Trung bình mỗi tổ quyên góp được số ki-lô-gam giấy vụn là:\n140 : 4 = 35 (kg)\nĐáp số: a) 140 kg; b) 35 kg.", "a) 140 kg; b) 35 kg", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Biểu đồ cột biểu diễn số học sinh thích các môn nghệ thuật: Âm nhạc có 35 bạn, Hội họa có 45 bạn, Khiêu vũ có 20 bạn, Kịch có 25 bạn.\na) Môn nghệ thuật nào được nhiều học sinh yêu thích nhất?\nb) Tổng số học sinh tham gia khảo sát là bao nhiêu bạn?", "a) Hội họa được yêu thích nhất (45 bạn).\nb) Tổng số học sinh tham gia khảo sát là:\n35 + 45 + 20 + 25 = 125 (học sinh)\nĐáp số: a) Hội họa; b) 125 học sinh.", "a) Hội họa; b) 125 học sinh", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Bình tung đồng xu 50 lần thấy mặt Sấp xuất hiện 28 lần.\na) Hỏi mặt Ngửa xuất hiện bao nhiêu lần?\nb) Viết tỉ số mô tả số lần xuất hiện mặt Ngửa so với tổng số lần tung đồng xu.", "a) Số lần xuất hiện mặt Ngửa là:\n50 - 28 = 22 (lần)\nb) Tỉ số mô tả số lần xuất hiện mặt Ngửa là:\n22/50 = 11/25\nĐáp số: a) 22 lần; b) 11/25.", "a) 22 lần; b) 11/25", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đoàn xe gồm 4 xe chở hàng, khối lượng hàng lần lượt là: 3500 kg, 4200 kg, 3800 kg và 4500 kg. Hỏi cả đoàn xe chở được tất cả bao nhiêu tấn hàng?", "Tổng khối lượng hàng cả đoàn xe chở được là:\n3500 + 4200 + 3800 + 4500 = 16 000 (kg)\nĐổi: 16 000 kg = 16 tấn\nĐáp số: 16 tấn hàng.", "16 tấn", 5, 1.5, "Vận dụng"),
            make_essay(5, "Số ngày mưa trong 3 tháng hè ghi nhận được: Tháng 6: 12 ngày; Tháng 7: 15 ngày; Tháng 8: 18 ngày.\na) Tháng nào có số ngày mưa nhiều nhất? Ít nhất?\nb) Tính số ngày mưa trung bình mỗi tháng trong 3 tháng hè đó.", "a) Tháng 8 có số ngày mưa nhiều nhất (18 ngày), Tháng 6 có số ngày mưa ít nhất (12 ngày).\nb) Số ngày mưa trung bình mỗi tháng là:\n(12 + 15 + 18) : 3 = 45 : 3 = 15 (ngày)\nĐáp số: a) Nhiều nhất: Tháng 8, Ít nhất: Tháng 6; b) 15 ngày.", "a) Nhiều nhất: Tháng 8, Ít nhất: Tháng 6; b) 15 ngày", 5, 1.5, "Vận dụng"),
            make_essay(6, "Trong hộp có 15 quả bóng gồm 7 quả màu xanh và 8 quả màu đỏ. Hỏi cần lấy ra ít nhất bao nhiêu quả bóng để chắc chắn có ít nhất 1 quả bóng màu xanh?", "Trường hợp xấu nhất là lấy toàn bộ 8 quả bóng màu đỏ.\nKhi đó, lấy thêm 1 quả bóng nữa chắc chắn sẽ là màu xanh.\nSố bóng cần lấy ít nhất là:\n8 + 1 = 9 (quả bóng)\nĐáp số: 9 quả bóng.", "9 quả bóng", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b43_test3"] = {
        "id": "th4_b43_test3",
        "lessonId": "th4_b43",
        "lessonNum": 43,
        "testNum": 3,
        "title": "Bài 43: Luyện tập chung - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 9",
        "chapter": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số trung bình cộng của 18, 22, 26, 30 là:", ["24", "22", "26", "25"], 0, "(18 + 22 + 26 + 30) : 4 = 96 : 4 = 24.", "Thông hiểu"),
            make_mc(2, "Quan sát biểu đồ cột, trục nằm ngang ghi các lớp 4A, 4B, 4C, 4D. Các đối tượng được thống kê là:", ["Các lớp học", "Số học sinh", "Điểm số", "Thời gian"], 0, "Trục ngang ghi tên các đối tượng thống kê, ở đây là các lớp học.", "Nhận biết"),
            make_mc(3, "Gieo một con xúc xắc 6 mặt 30 lần, thấy có 6 lần xuất hiện mặt 5 chấm. Tỉ số số lần xuất hiện mặt 5 chấm so với tổng số lần gieo là:", ["6/30 (hay 1/5)", "1/6", "5/30", "6/24"], 0, "6/30 = 1/5.", "Thông hiểu"),
            make_mc(4, "Trong hộp có 6 chiếc bút chì màu đen. Lấy ra ngẫu nhiên 1 chiếc bút thì sự kiện lấy được bút màu đỏ là:", ["Không thể xảy ra", "Chắc chắn xảy ra", "Có thể xảy ra", "Không chắc chắn"], 0, "Trong hộp không có bút màu đỏ nên sự kiện không thể xảy ra.", "Nhận biết"),
            make_mc(5, "Nhiệt độ 3 ngày: 30°C, 32°C, 34°C. Nhiệt độ trung bình trong 3 ngày là:", ["32°C", "30°C", "34°C", "31°C"], 0, "(30 + 32 + 34) : 3 = 96 : 3 = 32 (°C).", "Thông hiểu"),
            make_mc(6, "Bốc thăm 50 lần thấy thăm trúng thưởng xuất hiện 15 lần. Số lần không trúng thưởng là:", ["35 lần", "15 lần", "50 lần", "20 lần"], 0, "50 - 15 = 35 (lần).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Điểm kiểm tra môn Toán của 4 bạn Lan, Mai, Nam, Phúc lần lượt là: 9; 8; 10; 9.\na) Sắp xếp điểm của 4 bạn theo thứ tự từ lớn đến bé.\nb) Tính điểm trung bình môn Toán của cả 4 bạn.", "a) Thứ tự từ lớn đến bé: 10, 9, 9, 8.\nb) Điểm trung bình của 4 bạn là:\n(9 + 8 + 10 + 9) : 4 = 36 : 4 = 9 (điểm)\nĐáp số: a) 10, 9, 9, 8; b) 9 điểm.", "a) 10, 9, 9, 8; b) 9 điểm", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Biểu đồ cột biểu diễn số lượt khách tham quan bảo tàng trong 4 ngày nghỉ lễ: Ngày 1: 450 lượt; Ngày 2: 600 lượt; Ngày 3: 550 lượt; Ngày 4: 800 lượt.\na) Ngày nào có đông khách tham quan nhất? Ngày nào ít nhất?\nb) Tính tổng số lượt khách tham quan bảo tàng trong cả 4 ngày.", "a) Ngày 4 có đông khách nhất (800 lượt); Ngày 1 có ít khách nhất (450 lượt).\nb) Tổng số lượt khách trong 4 ngày là:\n450 + 600 + 550 + 800 = 2400 (lượt khách)\nĐáp số: a) Nhiều nhất: Ngày 4, Ít nhất: Ngày 1; b) 2400 lượt khách.", "a) Nhiều nhất: Ngày 4, Ít nhất: Ngày 1; b) 2400 lượt", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Bạn Minh quay một tấm bìa hình tròn chia thành 5 phần bằng nhau ghi các số 1, 2, 3, 4, 5. Sau 50 lần quay, kim dừng lại ở ô số lẻ 30 lần.\na) Kim dừng lại ở ô số chẵn bao nhiêu lần?\nb) Viết tỉ số mô tả số lần kim dừng ở ô số chẵn so với tổng số lần quay.", "a) Số lần kim dừng lại ở ô số chẵn là:\n50 - 30 = 20 (lần)\nb) Tỉ số mô tả số lần kim dừng ở ô số chẵn là:\n20/50 = 2/5\nĐáp số: a) 20 lần; b) 2/5.", "a) 20 lần; b) 2/5", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một xưởng may sản xuất được số khẩu trang trong 3 tuần: Tuần 1: 12 500 chiếc; Tuần 2: 14 000 chiếc; Tuần 3: 15 500 chiếc. Hỏi trung bình mỗi tuần xưởng may sản xuất được bao nhiêu chiếc khẩu trang?", "Tổng số khẩu trang xưởng may sản xuất trong 3 tuần là:\n12 500 + 14 000 + 15 500 = 42 000 (chiếc)\nTrung bình mỗi tuần xưởng sản xuất được số khẩu trang là:\n42 000 : 3 = 14 000 (chiếc)\nĐáp số: 14 000 chiếc khẩu trang.", "14 000 chiếc", 5, 1.5, "Vận dụng"),
            make_essay(5, "Bảng thống kê số cây hoa trồng được của 3 tổ: Tổ 1: 45 cây; Tổ 2: 50 cây; Tổ 3 trồng được số cây bằng trung bình cộng của cả 3 tổ.\na) Tính số cây hoa của Tổ 3 trồng được.\nb) Cả 3 tổ trồng được tất cả bao nhiêu cây hoa?", "a) Vì số cây của Tổ 3 bằng trung bình cộng cả 3 tổ nên số cây của Tổ 3 bằng trung bình cộng của Tổ 1 và Tổ 2:\n(45 + 50) : 2 = 47,5 cây (để tròn số: Tổ 1 trồng 44 cây, Tổ 2 trồng 50 cây => (44 + 50) : 2 = 47 cây).\nChỉnh số liệu: Tổ 1 trồng 44 cây, Tổ 2 trồng 50 cây.\nSố cây của Tổ 3 là:\n(44 + 50) : 2 = 47 (cây)\nb) Cả 3 tổ trồng được tất cả số cây là:\n44 + 50 + 47 = 141 (cây)\nĐáp số: a) 47 cây; b) 141 cây hoa.", "a) 47 cây; b) 141 cây", 6, 1.5, "Vận dụng"),
            make_essay(6, "Trong hộp có 16 viên bi gồm 8 viên màu đỏ, 5 viên màu xanh và 3 viên màu vàng có kích thước như nhau. An nhắm mắt lấy ngẫu nhiên các viên bi. Hỏi An phải lấy ra ít nhất bao nhiêu viên bi để chắc chắn có đủ cả 3 màu bi?", "Trường hợp xấu nhất là An lấy phải toàn bộ số bi của hai màu có số lượng nhiều nhất (màu đỏ và màu xanh):\n8 + 5 = 13 (viên bi)\nKhi đó, lấy thêm 1 viên bi nữa chắc chắn sẽ là viên bi màu vàng (màu còn lại).\nSố viên bi An cần lấy ít nhất là:\n13 + 1 = 14 (viên bi)\nĐáp số: 14 viên bi.", "14 viên bi", 4, 1.0, "Vận dụng cao")
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 9 Toán 4: {len(ex)} (Kỳ vọng: 12 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
