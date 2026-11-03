# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 8: PHÉP NHÂN VÀ PHÉP CHIA - PHẦN 2 (BÀI 36 ĐẾN BÀI 39) - TOÁN 4 KNTT
Gồm 4 bài học, mỗi bài có 3 đề kiểm tra độc lập:
- Bài 36: Luyện tập chung (th4_b36_test1, th4_b36_test2, th4_b36_test3)
- Bài 37: Chia cho số có một chữ số (th4_b37_test1, th4_b37_test2, th4_b37_test3)
- Bài 38: Chia cho số có hai chữ số (th4_b38_test1, th4_b38_test2, th4_b38_test3)
- Bài 39: Luyện tập chung Chủ đề 8 (th4_b39_test1, th4_b39_test2, th4_b39_test3)
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

def get_ch8_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 36: LUYỆN TẬP CHUNG (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b36_test1"] = {
        "id": "th4_b36_test1",
        "lessonId": "th4_b36",
        "lessonNum": 36,
        "testNum": 1,
        "title": "Bài 36: Luyện tập chung - Đề số 1",
        "topic": "Luyện tập chung về phép nhân",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 12 400 x 6 là:", ["74 400", "72 400", "64 400", "74 000"], 0, "12 400 x 6 = 74 400.", "Thông hiểu"),
            make_mc(2, "Tính nhanh 25 x 36 x 4 có kết quả là:", ["3600", "360", "36 000", "900"], 0, "(25 x 4) x 36 = 100 x 36 = 3600.", "Thông hiểu"),
            make_mc(3, "Tích của số lớn nhất có ba chữ số và số bé nhất có hai chữ số là:", ["9990", "9900", "9000", "9999"], 0, "Số lớn nhất có 3 chữ số là 999, số bé nhất có 2 chữ số là 10. Tích = 999 x 10 = 9990.", "Thông hiểu"),
            make_mc(4, "Một ô tô trong 1 giờ đi được 55 km. Trong 12 giờ ô tô đi được số ki-lô-mét là:", ["660 km", "550 km", "600 km", "650 km"], 0, "55 x 12 = 660 (km).", "Thông hiểu"),
            make_mc(5, "Kết quả của phép tính 180 x 20 là:", ["3600", "360", "36 000", "1800"], 0, "180 x 20 = 3600.", "Thông hiểu"),
            make_mc(6, "Một mảnh đất hình vuông có chu vi 48 m. Diện tích mảnh đất đó là:", ["144 m²", "96 m²", "196 m²", "576 m²"], 0, "Cạnh = 48 : 4 = 12 m. Diện tích = 12 x 12 = 144 (m²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 25 314 x 4\nb) 248 x 35", "a) 25 314 x 4 = 101 256\nb) 248 x 35 = 8680", "a) 101 256; b) 8680", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 50 x 27 x 2\nb) 125 x 49 x 8", "a) 50 x 27 x 2 = (50 x 2) x 27 = 100 x 27 = 2700\nb) 125 x 49 x 8 = (125 x 8) x 49 = 1000 x 49 = 49 000", "a) 2700; b) 49 000", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính giá trị của biểu thức:\na) 35 x 24 + 1800\nb) 12 000 - 450 x 20", "a) 35 x 24 + 1800 = 840 + 1800 = 2640\nb) 12 000 - 450 x 20 = 12 000 - 9000 = 3000", "a) 2640; b) 3000", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một cửa hàng nhập về 25 bao gạo tẻ và 15 bao gạo nếp. Mỗi bao gạo đều cân nặng 50 kg. Hỏi cửa hàng đã nhập về tất cả bao nhiêu tấn gạo?", "Tổng số bao gạo cửa hàng nhập về là:\n25 + 15 = 40 (bao)\nTổng khối lượng gạo cửa hàng đã nhập là:\n50 x 40 = 2000 (kg)\nĐổi: 2000 kg = 2 tấn\nĐáp số: 2 tấn gạo.", "2 tấn", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chu vi 140 m, chiều rộng kém chiều dài 10 m. Tính diện tích mảnh vườn đó.", "Nửa chu vi mảnh vườn là:\n140 : 2 = 70 (m)\nChiều dài mảnh vườn là:\n(70 + 10) : 2 = 40 (m)\nChiều rộng mảnh vườn là:\n40 - 10 = 30 (m)\nDiện tích mảnh vườn là:\n40 x 30 = 1200 (m²)\nĐáp số: 1200 m².", "1200 m²", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 78 x 34 + 78 x 66", "78 x 34 + 78 x 66 = 78 x (34 + 66) = 78 x 100 = 7800\nĐáp số: 7800.", "7800", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b36_test2"] = {
        "id": "th4_b36_test2",
        "lessonId": "th4_b36",
        "lessonNum": 36,
        "testNum": 2,
        "title": "Bài 36: Luyện tập chung - Đề số 2",
        "topic": "Luyện tập chung về phép nhân",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 305 x 42 là:", ["12 810", "12 710", "12 910", "11 810"], 0, "305 x 42 = 12 810.", "Thông hiểu"),
            make_mc(2, "Tính nhanh 4 x 79 x 25 =", ["7900", "790", "79 000", "3950"], 0, "(4 x 25) x 79 = 100 x 79 = 7900.", "Thông hiểu"),
            make_mc(3, "Một xí nghiệp có 15 tổ sản xuất, mỗi tổ có 12 công nhân. Xí nghiệp có tất cả số công nhân là:", ["180 người", "170 người", "190 người", "160 người"], 0, "15 x 12 = 180 (công nhân).", "Thông hiểu"),
            make_mc(4, "Kết quả của biểu thức (15 + 25) x 18 là:", ["720", "620", "820", "520"], 0, "40 x 18 = 720.", "Thông hiểu"),
            make_mc(5, "Số thích hợp điền vào chỗ chấm để 65 x 1000 = ... là:", ["65 000", "6500", "650 000", "650"], 0, "65 x 1000 = 65 000.", "Nhận biết"),
            make_mc(6, "Một tấm thảm hình chữ nhật dài 24 dm, rộng 15 dm có diện tích là:", ["360 dm²", "180 dm²", "78 dm²", "39 dm²"], 0, "24 x 15 = 360 (dm²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 18 205 x 5\nb) 316 x 24", "a) 18 205 x 5 = 91 025\nb) 316 x 24 = 7584", "a) 91 025; b) 7584", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 4 x 58 x 25\nb) 8 x 37 x 125", "a) 4 x 58 x 25 = (4 x 25) x 58 = 100 x 58 = 5800\nb) 8 x 37 x 125 = (8 x 125) x 37 = 1000 x 37 = 37 000", "a) 5800; b) 37 000", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x : 16 = 45\nb) x : 25 = 104", "a) x = 45 x 16 = 720\nb) x = 104 x 25 = 2600", "a) x = 720; b) x = 2600", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đoàn xe chở hàng gồm 12 xe, mỗi xe chở được 45 bao hàng, mỗi bao hàng cân nặng 40 kg. Hỏi cả đoàn xe chở được bao nhiêu tấn hàng?", "Số bao hàng cả đoàn xe chở là:\n45 x 12 = 540 (bao)\nTổng khối lượng hàng cả đoàn xe chở là:\n40 x 540 = 21 600 (kg)\nĐổi: 21 600 kg = 21,6 tấn (hoặc 21 tấn 6 tạ)\nĐáp số: 21 600 kg (21 tấn 6 tạ).", "21 600 kg (21 tấn 6 tạ)", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chu vi là 180 m. Chiều dài hơn chiều rộng 18 m. Tính diện tích mảnh vườn đó.", "Nửa chu vi mảnh vườn là:\n180 : 2 = 90 (m)\nChiều dài mảnh vườn là:\n(90 + 18) : 2 = 54 (m)\nChiều rộng mảnh vườn là:\n54 - 18 = 36 (m)\nDiện tích mảnh vườn là:\n54 x 36 = 1944 (m²)\nĐáp số: 1944 m².", "1944 m²", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 125 x 16 x 5", "125 x 16 x 5 = 125 x (8 x 2) x 5 = (125 x 8) x (2 x 5) = 1000 x 10 = 10 000\nĐáp số: 10 000.", "10 000", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b36_test3"] = {
        "id": "th4_b36_test3",
        "lessonId": "th4_b36",
        "lessonNum": 36,
        "testNum": 3,
        "title": "Bài 36: Luyện tập chung - Đề số 3",
        "topic": "Luyện tập chung về phép nhân",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 415 x 28 là:", ["11 620", "11 520", "11 720", "10 620"], 0, "415 x 28 = 11 620.", "Thông hiểu"),
            make_mc(2, "Tính nhanh: 125 x 80 =", ["10 000", "1000", "100 000", "8000"], 0, "125 x 8 x 10 = 1000 x 10 = 10 000.", "Thông hiểu"),
            make_mc(3, "Một ngày có 24 giờ. Hỏi 15 ngày có tất cả bao nhiêu giờ?", ["360 giờ", "340 giờ", "350 giờ", "380 giờ"], 0, "24 x 15 = 360 (giờ).", "Thông hiểu"),
            make_mc(4, "Tích của 45 và 11 là:", ["495", "455", "505", "485"], 0, "45 x 11 = 495.", "Thông hiểu"),
            make_mc(5, "Đổi 8 tạ = ... kg:", ["800", "80", "8000", "80 000"], 0, "8 tạ = 800 kg.", "Nhận biết"),
            make_mc(6, "Diện tích một hình bình hành có đáy 35 cm, chiều cao 20 cm là:", ["700 cm²", "350 cm²", "110 cm²", "55 cm²"], 0, "35 x 20 = 700 (cm²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 14 360 x 6\nb) 275 x 36", "a) 14 360 x 6 = 86 160\nb) 275 x 36 = 9900", "a) 86 160; b) 9900", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 25 x 68 x 4\nb) 125 x 85 x 8", "a) 25 x 68 x 4 = (25 x 4) x 68 = 100 x 68 = 6800\nb) 125 x 85 x 8 = (125 x 8) x 85 = 1000 x 85 = 85 000", "a) 6800; b) 85 000", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x : 35 = 72\nb) x : 18 = 150", "a) x = 72 x 35 = 2520\nb) x = 150 x 18 = 2700", "a) x = 2520; b) x = 2700", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một cửa hàng sách nhập về 45 thùng sách, mỗi thùng có 60 quyển sách. Cửa hàng đã bán được 1800 quyển sách. Hỏi cửa hàng còn lại bao nhiêu quyển sách?", "Tổng số quyển sách cửa hàng đã nhập là:\n60 x 45 = 2700 (quyển)\nSố quyển sách cửa hàng còn lại là:\n2700 - 1800 = 900 (quyển)\nĐáp số: 900 quyển sách.", "900 quyển", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một khu đất hình chữ nhật có chiều rộng 25 m, chiều dài gấp 3 lần chiều rộng. Người ta xây tường rào quanh khu đất đó, để lại một cổng ra vào rộng 4 m. Hỏi hàng rào dài bao nhiêu mét?", "Chiều dài khu đất là:\n25 x 3 = 75 (m)\nChu vi khu đất là:\n(75 + 25) x 2 = 200 (m)\nChiều dài hàng rào là:\n200 - 4 = 196 (m)\nĐáp số: 196 m.", "196 m", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 85 x 47 + 85 x 53", "85 x 47 + 85 x 53 = 85 x (47 + 53) = 85 x 100 = 8500\nĐáp số: 8500.", "8500", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 37: CHIA CHO SỐ CÓ MỘT CHỮ SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b37_test1"] = {
        "id": "th4_b37_test1",
        "lessonId": "th4_b37",
        "lessonNum": 37,
        "testNum": 1,
        "title": "Bài 37: Chia cho số có một chữ số - Đề số 1",
        "topic": "Chia cho số có một chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép chia 48 642 : 6 là:", ["8107", "8170", "8017", "817"], 0, "48 : 6 = 8, 6 : 6 = 1, 4 : 6 = 0 dư 4, 42 : 6 = 7. Kết quả là 8107.", "Thông hiểu"),
            make_mc(2, "Số dư trong phép chia 35 249 : 5 là:", ["4", "1", "2", "3"], 0, "Chữ số tận cùng là 9, 9 chia 5 được 1 dư 4.", "Thông hiểu"),
            make_mc(3, "Một phân xưởng may cần đóng gói 3648 chiếc áo vào các hộp, mỗi hộp đựng 8 chiếc áo. Số hộp cần dùng là:", ["456 hộp", "455 hộp", "465 hộp", "466 hộp"], 0, "3648 : 8 = 456 (hộp).", "Thông hiểu"),
            make_mc(4, "Biết x x 7 = 35 700. Giá trị của x là:", ["5100", "5010", "510", "5001"], 0, "x = 35 700 : 7 = 5100.", "Thông hiểu"),
            make_mc(5, "Một tuần lễ có 7 ngày. Hỏi 365 ngày gồm bao nhiêu tuần lễ và dư mấy ngày?", ["52 tuần dư 1 ngày", "51 tuần dư 2 ngày", "52 tuần dư 2 ngày", "50 tuần dư 5 ngày"], 0, "365 : 7 = 52 (dư 1).", "Thông hiểu"),
            make_mc(6, "Thương của phép chia 72 000 : 9 là:", ["8000", "800", "9000", "7000"], 0, "72 000 : 9 = 8000.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 45 832 : 4\nb) 63 720 : 9", "a) 45 832 : 4 = 11 458\nb) 63 720 : 9 = 7080", "a) 11 458; b) 7080", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 48 360 : 6 + 12 500\nb) 90 000 - 56 400 : 8", "a) 48 360 : 6 + 12 500 = 8060 + 12 500 = 20 560\nb) 90 000 - 56 400 : 8 = 90 000 - 7050 = 82 950", "a) 20 560; b) 82 950", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 5 = 28 450\nb) x x 8 = 57 632", "a) x = 28 450 : 5 = 5690\nb) x = 57 632 : 8 = 7204", "a) x = 5690; b) x = 7204", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Có 4 xe chở tổng cộng 18 480 kg hàng cứu trợ đến vùng lũ lụt. Hỏi 7 xe như thế chở được tất cả bao nhiêu ki-lô-gam hàng (biết mỗi xe chở lượng hàng như nhau)?", "Mỗi xe chở được số ki-lô-gam hàng là:\n18 480 : 4 = 4620 (kg)\n7 xe như thế chở được số ki-lô-gam hàng là:\n4620 x 7 = 32 340 (kg)\nĐáp số: 32 340 kg hàng.", "32 340 kg", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một cửa hàng có 3 thùng chứa tất cả 1560 lít dầu. Người ta đã bán đi một lượng dầu bằng số dầu của 1 thùng. Hỏi cửa hàng còn lại bao nhiêu lít dầu?", "Mỗi thùng chứa số lít dầu là:\n1560 : 3 = 520 (lít)\nSố lít dầu cửa hàng còn lại là:\n1560 - 520 = 1040 (lít)\n(Hoặc: 520 x 2 = 1040 lít)\nĐáp số: 1040 lít dầu.", "1040 lít", 5, 1.5, "Vận dụng"),
            make_essay(6, "Trong một phép chia có số chia là 7, thương là 1245 và số dư là số dư lớn nhất có thể. Tìm số bị chia của phép chia đó.", "Vì số chia là 7 nên số dư lớn nhất có thể là: 7 - 1 = 6.\nSố bị chia là:\n1245 x 7 + 6 = 8715 + 6 = 8721\nĐáp số: 8721.", "8721", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b37_test2"] = {
        "id": "th4_b37_test2",
        "lessonId": "th4_b37",
        "lessonNum": 37,
        "testNum": 2,
        "title": "Bài 37: Chia cho số có một chữ số - Đề số 2",
        "topic": "Chia cho số có một chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép chia 35 140 : 7 là:", ["5020", "520", "5002", "5200"], 0, "35 : 7 = 5, 1 : 7 = 0 dư 1, 14 : 7 = 2, 0 : 7 = 0. Vậy thương là 5020.", "Thông hiểu"),
            make_mc(2, "Số dư trong một phép chia luôn luôn:", ["Bé hơn số chia", "Lớn hơn số chia", "Bằng số chia", "Bằng 0"], 0, "Quy tắc: Số dư luôn bé hơn số chia.", "Nhận biết"),
            make_mc(3, "Một sợi dây dài 4200 cm được cắt thành 6 đoạn bằng nhau. Mỗi đoạn dài là:", ["700 cm", "600 cm", "70 cm", "800 cm"], 0, "4200 : 6 = 700 (cm).", "Thông hiểu"),
            make_mc(4, "Thương của 56 048 và 8 là:", ["7006", "706", "76", "7060"], 0, "56 048 : 8 = 7006.", "Thông hiểu"),
            make_mc(5, "Tìm x biết x x 6 = 48 360:", ["8060", "860", "8006", "8600"], 0, "x = 48 360 : 6 = 8060.", "Thông hiểu"),
            make_mc(6, "Một hình vuông có chu vi 3240 m thì cạnh của nó dài:", ["810 m", "801 m", "81 m", "800 m"], 0, "3240 : 4 = 810 (m).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 56 385 : 5\nb) 42 168 : 7", "a) 56 385 : 5 = 11 277\nb) 42 168 : 7 = 6024", "a) 11 277; b) 6024", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) (35 240 + 12 760) : 5\nb) 84 000 - 36 120 : 6", "a) (35 240 + 12 760) : 5 = 48 000 : 5 = 9600\nb) 84 000 - 36 120 : 6 = 84 000 - 6020 = 77 980", "a) 9600; b) 77 980", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 4 = 18 360\nb) x x 9 = 74 250", "a) x = 18 360 : 4 = 4590\nb) x = 74 250 : 9 = 8250", "a) x = 4590; b) x = 8250", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một nông trường thu hoạch được 24 640 kg cam đựng đều vào 8 xe tải. Người ta đã chuyển 5 xe về nhà máy chế biến. Hỏi đã có bao nhiêu ki-lô-gam cam được chuyển về nhà máy?", "Mỗi xe tải chở số ki-lô-gam cam là:\n24 640 : 8 = 3080 (kg)\nSố ki-lô-gam cam chuyển về nhà máy là:\n3080 x 5 = 15 400 (kg)\nĐáp số: 15 400 kg cam.", "15 400 kg", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh đất hình chữ nhật có chu vi là 360 m, chiều dài gấp đôi chiều rộng. Tính chiều dài và chiều rộng của mảnh đất đó.", "Nửa chu vi mảnh đất là:\n360 : 2 = 180 (m)\nTổng số phần bằng nhau là:\n1 + 2 = 3 (phần)\nChiều rộng mảnh đất là:\n180 : 3 = 60 (m)\nChiều dài mảnh đất là:\n60 x 2 = 120 (m)\nĐáp số: Chiều dài: 120 m; Chiều rộng: 60 m.", "Dài: 120 m; Rộng: 60 m", 6, 1.5, "Vận dụng"),
            make_essay(6, "Trong một phép chia cho 8, thương là 2045 và số dư là số dư lớn nhất có thể. Tìm số bị chia.", "Số dư lớn nhất khi chia cho 8 là 7.\nSố bị chia là:\n2045 x 8 + 7 = 16 360 + 7 = 16 367\nĐáp số: 16 367.", "16 367", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b37_test3"] = {
        "id": "th4_b37_test3",
        "lessonId": "th4_b37",
        "lessonNum": 37,
        "testNum": 3,
        "title": "Bài 37: Chia cho số có một chữ số - Đề số 3",
        "topic": "Chia cho số có một chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép chia 64 032 : 8 là:", ["8004", "804", "84", "8040"], 0, "64 032 : 8 = 8004.", "Thông hiểu"),
            make_mc(2, "Nếu chia 25 348 cho 5 thì số dư là:", ["3", "1", "2", "4"], 0, "Tận cùng là 8, 8 chia 5 được 1 dư 3.", "Thông hiểu"),
            make_mc(3, "Một trường học có 1248 học sinh xếp đều thành 6 hàng. Mỗi hàng có số học sinh là:", ["208 bạn", "280 bạn", "28 bạn", "218 bạn"], 0, "1248 : 6 = 208 (học sinh).", "Thông hiểu"),
            make_mc(4, "Biết y x 3 = 19 500. Giá trị của y là:", ["6500", "6050", "650", "5500"], 0, "y = 19 500 : 3 = 6500.", "Thông hiểu"),
            make_mc(5, "Thương của 81 072 và 9 là:", ["9008", "908", "98", "9080"], 0, "81 072 : 9 = 9008.", "Thông hiểu"),
            make_mc(6, "Một cuộn dây thép dài 1800 m, người ta cắt lấy 1/4 cuộn dây. Số mét dây thép đã cắt là:", ["450 m", "400 m", "500 m", "350 m"], 0, "1800 : 4 = 450 (m).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 68 472 : 8\nb) 54 270 : 9", "a) 68 472 : 8 = 8559\nb) 54 270 : 9 = 6030", "a) 8559; b) 6030", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 64 800 : 8 - 4500\nb) 24 500 + 42 060 : 6", "a) 64 800 : 8 - 4500 = 8100 - 4500 = 3600\nb) 24 500 + 42 060 : 6 = 24 500 + 7010 = 31 510", "a) 3600; b) 31 510", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 7 = 43 750\nb) x x 6 = 55 236", "a) x = 43 750 : 7 = 6250\nb) x = 55 236 : 6 = 9206", "a) x = 6250; b) x = 9206", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đoàn xe gồm 6 xe chở được 15 360 kg lúa mì. Người ta dùng 9 xe cùng loại như vậy để vận chuyển. Hỏi 9 xe đó chở được tất cả bao nhiêu ki-lô-gam lúa mì?", "Mỗi xe chở được số ki-lô-gam lúa mì là:\n15 360 : 6 = 2560 (kg)\n9 xe như thế chở được số ki-lô-gam lúa mì là:\n2560 x 9 = 23 040 (kg)\nĐáp số: 23 040 kg lúa mì.", "23 040 kg", 5, 1.5, "Vận dụng"),
            make_essay(5, "Có hai kho gạo chứa tất cả 14 500 kg gạo. Nếu chuyển 1500 kg gạo từ kho thứ nhất sang kho thứ hai thì hai kho có số gạo bằng nhau. Tính số gạo ở mỗi kho lúc đầu.", "Khi hai kho có số gạo bằng nhau, mỗi kho có số gạo là:\n14 500 : 2 = 7250 (kg)\nLúc đầu kho thứ nhất có số gạo là:\n7250 + 1500 = 8750 (kg)\nLúc đầu kho thứ hai có số gạo là:\n14 500 - 8750 = 5750 (kg)\nĐáp số: Kho 1: 8750 kg gạo; Kho 2: 5750 kg gạo.", "Kho 1: 8750 kg; Kho 2: 5750 kg", 6, 1.5, "Vận dụng"),
            make_essay(6, "Trong một phép chia có số chia là 6, thương là 3420 và số dư là số dư lớn nhất có thể. Tìm số bị chia.", "Số dư lớn nhất khi chia cho 6 là 5.\nSố bị chia là:\n3420 x 6 + 5 = 20 520 + 5 = 20 525\nĐáp số: 20 525.", "20 525", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 38: CHIA CHO SỐ CÓ HAI CHỮ SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b38_test1"] = {
        "id": "th4_b38_test1",
        "lessonId": "th4_b38",
        "lessonNum": 38,
        "testNum": 1,
        "title": "Bài 38: Chia cho số có hai chữ số - Đề số 1",
        "topic": "Chia cho số có hai chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép chia 840 : 24 là:", ["35", "34", "36", "45"], 0, "84 : 24 = 3 dư 12; hạ 0 được 120 : 24 = 5. Kết quả là 35.", "Thông hiểu"),
            make_mc(2, "Thương của 4620 và 15 là:", ["308", "38", "380", "318"], 0, "4620 : 15 = 308.", "Thông hiểu"),
            make_mc(3, "Một cửa hàng có 1440 kg gạo đóng đều vào các bao, mỗi bao 36 kg. Cửa hàng đóng được số bao là:", ["40 bao", "45 bao", "50 bao", "35 bao"], 0, "1440 : 36 = 40 (bao).", "Thông hiểu"),
            make_mc(4, "Kết quả phép chia 7560 : 36 là:", ["210", "21", "201", "215"], 0, "7560 : 36 = 210.", "Thông hiểu"),
            make_mc(5, "Tìm x biết x x 25 = 8500:", ["340", "34", "350", "360"], 0, "x = 8500 : 25 = 340.", "Thông hiểu"),
            make_mc(6, "Diện tích một hình chữ nhật là 600 m², chiều dài là 25 m. Chiều rộng của hình chữ nhật đó là:", ["24 m", "20 m", "30 m", "25 m"], 0, "600 : 25 = 24 (m).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 5520 : 24\nb) 9180 : 36", "a) 5520 : 24 = 230\nb) 9180 : 36 = 255", "a) 230; b) 255", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 4800 : 25 + 340\nb) 1500 - 9660 : 28", "a) 4800 : 25 + 340 = 192 + 340 = 532\nb) 1500 - 9660 : 28 = 1500 - 345 = 1155", "a) 532; b) 1155", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 35 = 7350\nb) x x 42 = 8820", "a) x = 7350 : 35 = 210\nb) x = 8820 : 42 = 210", "a) x = 210; b) x = 210", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một tổ sản xuất nhận may 1560 bộ quần áo. Mỗi ngày tổ may được 65 bộ quần áo. Hỏi tổ đó hoàn thành kế hoạch may trong bao nhiêu ngày?", "Thời gian để tổ sản xuất hoàn thành kế hoạch là:\n1560 : 65 = 24 (ngày)\nĐáp số: 24 ngày.", "24 ngày", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh vườn hình chữ nhật có diện tích là 840 m², chiều dài là 35 m. Người ta rào xung quanh mảnh vườn đó, để lại một cửa ra vào rộng 3 m. Tính chiều dài hàng rào.", "Chiều rộng mảnh vườn là:\n840 : 35 = 24 (m)\nChu vi mảnh vườn là:\n(35 + 24) x 2 = 118 (m)\nChiều dài hàng rào là:\n118 - 3 = 115 (m)\nĐáp số: 115 m.", "115 m", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số dư trong phép chia 4568 : 34 (không cần tính cả thương, hãy đặt tính và tìm số dư).", "Thực hiện phép chia: 4568 : 34 = 134 (dư 12).\nKiểm tra lại: 134 x 34 + 12 = 4556 + 12 = 4568.\nVậy số dư là 12.\nĐáp số: 12.", "12", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b38_test2"] = {
        "id": "th4_b38_test2",
        "lessonId": "th4_b38",
        "lessonNum": 38,
        "testNum": 2,
        "title": "Bài 38: Chia cho số có hai chữ số - Đề số 2",
        "topic": "Chia cho số có hai chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép chia 960 : 32 là:", ["30", "32", "28", "25"], 0, "960 : 32 = 30.", "Thông hiểu"),
            make_mc(2, "Thương của 8740 và 38 là:", ["230", "23", "203", "235"], 0, "8740 : 38 = 230.", "Thông hiểu"),
            make_mc(3, "Một ô tô đi được quãng đường 720 km trong 16 giờ. Vận tốc trung bình mỗi giờ ô tô đi được là:", ["45 km", "40 km", "50 km", "48 km"], 0, "720 : 16 = 45 (km).", "Thông hiểu"),
            make_mc(4, "Kết quả của phép tính 11 250 : 25 là:", ["450", "45", "405", "550"], 0, "11 250 : 25 = 450.", "Thông hiểu"),
            make_mc(5, "Tìm x biết x x 48 = 9600:", ["200", "20", "250", "220"], 0, "x = 9600 : 48 = 200.", "Thông hiểu"),
            make_mc(6, "Số dư của phép chia 375 : 18 là:", ["15", "12", "18", "0"], 0, "375 : 18 = 20 (dư 15).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 6930 : 33\nb) 11 040 : 48", "a) 6930 : 33 = 210\nb) 11 040 : 48 = 230", "a) 210; b) 230", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị biểu thức:\na) 7500 : 25 - 180\nb) 320 x 15 : 24", "a) 7500 : 25 - 180 = 300 - 180 = 120\nb) 320 x 15 : 24 = 4800 : 24 = 200", "a) 120; b) 200", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 28 = 7140\nb) x x 54 = 9720", "a) x = 7140 : 28 = 255\nb) x = 9720 : 54 = 180", "a) x = 255; b) x = 180", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại có 1920 con gà được chia đều vào 32 dãy chuồng. Hỏi mỗi dãy chuồng có bao nhiêu con gà?", "Mỗi dãy chuồng có số con gà là:\n1920 : 32 = 60 (con)\nĐáp số: 60 con gà.", "60 con", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một thửa ruộng hình chữ nhật có diện tích là 960 m², chiều rộng là 24 m. Tính chu vi thửa ruộng hình chữ nhật đó.", "Chiều dài thửa ruộng là:\n960 : 24 = 40 (m)\nChu vi thửa ruộng là:\n(40 + 24) x 2 = 128 (m)\nĐáp số: 128 m.", "128 m", 5, 1.5, "Vận dụng"),
            make_essay(6, "Trong một phép chia có số chia là 24, thương là 115 và số dư là số dư lớn nhất có thể. Tìm số bị chia.", "Số dư lớn nhất khi chia cho 24 là 23.\nSố bị chia là:\n115 x 24 + 23 = 2760 + 23 = 2783\nĐáp số: 2783.", "2783", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b38_test3"] = {
        "id": "th4_b38_test3",
        "lessonId": "th4_b38",
        "lessonNum": 38,
        "testNum": 3,
        "title": "Bài 38: Chia cho số có hai chữ số - Đề số 3",
        "topic": "Chia cho số có hai chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép chia 9450 : 35 là:", ["270", "27", "207", "275"], 0, "9450 : 35 = 270.", "Thông hiểu"),
            make_mc(2, "Thương của 8640 và 27 là:", ["320", "32", "302", "312"], 0, "8640 : 27 = 320.", "Thông hiểu"),
            make_mc(3, "Một xưởng đóng gói 2400 gói kẹo vào các hộp, mỗi hộp 24 gói. Số hộp đóng được là:", ["100 hộp", "10 hộp", "1000 hộp", "200 hộp"], 0, "2400 : 24 = 100 (hộp).", "Nhận biết"),
            make_mc(4, "Kết quả của 12 600 : 42 là:", ["300", "30", "3000", "350"], 0, "12 600 : 42 = 300.", "Thông hiểu"),
            make_mc(5, "Tìm y biết y x 18 = 4500:", ["250", "25", "205", "260"], 0, "y = 4500 : 18 = 250.", "Thông hiểu"),
            make_mc(6, "Diện tích một mảnh đất hình bình hành là 840 m², độ dài đáy 28 m thì chiều cao tương ứng là:", ["30 m", "25 m", "35 m", "20 m"], 0, "840 : 28 = 30 (m).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 8640 : 24\nb) 13 440 : 56", "a) 8640 : 24 = 360\nb) 13 440 : 56 = 240", "a) 360; b) 240", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 9600 : 32 + 250\nb) 2400 - 10 500 : 42", "a) 9600 : 32 + 250 = 300 + 250 = 550\nb) 2400 - 10 500 : 42 = 2400 - 250 = 2150", "a) 550; b) 2150", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 36 = 9000\nb) x x 45 = 12 150", "a) x = 9000 : 36 = 250\nb) x = 12 150 : 45 = 270", "a) x = 250; b) x = 270", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đoàn tàu chở 1350 hành khách được chia đều vào 15 toa xe. Hỏi mỗi toa xe chở bao nhiêu hành khách?", "Mỗi toa xe chở số hành khách là:\n1350 : 15 = 90 (hành khách)\nĐáp số: 90 hành khách.", "90 hành khách", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một khu vườn hình chữ nhật có diện tích 1080 m², chiều dài là 36 m. Tính chu vi khu vườn hình chữ nhật đó.", "Chiều rộng khu vườn là:\n1080 : 36 = 30 (m)\nChu vi khu vườn là:\n(36 + 30) x 2 = 132 (m)\nĐáp số: 132 m.", "132 m", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số bị chia trong một phép chia cho 35 biết thương là 204 và số dư là số dư lớn nhất có thể.", "Số dư lớn nhất khi chia cho 35 là 34.\nSố bị chia là:\n204 x 35 + 34 = 7140 + 34 = 7174\nĐáp số: 7174.", "7174", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 39: LUYỆN TẬP CHUNG CHỦ ĐỀ 8 (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b39_test1"] = {
        "id": "th4_b39_test1",
        "lessonId": "th4_b39",
        "lessonNum": 39,
        "testNum": 1,
        "title": "Bài 39: Luyện tập chung Chủ đề 8 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 8",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 250 x 30 là:", ["7500", "750", "75 000", "7000"], 0, "250 x 30 = 7500.", "Nhận biết"),
            make_mc(2, "Kết quả của phép chia 9600 : 30 là:", ["320", "32", "3200", "300"], 0, "9600 : 30 = 320.", "Thông hiểu"),
            make_mc(3, "Một hình bình hành có đáy 24 cm và chiều cao 15 cm. Diện tích của nó là:", ["360 cm²", "180 cm²", "78 cm²", "39 cm²"], 0, "24 x 15 = 360 (cm²).", "Thông hiểu"),
            make_mc(4, "Biểu thức 25 x 4 x 38 có giá trị là:", ["3800", "380", "38 000", "7600"], 0, "(25 x 4) x 38 = 100 x 38 = 3800.", "Thông hiểu"),
            make_mc(5, "Đổi 4 tấn 5 tạ = ... kg:", ["4500", "4050", "450", "4005"], 0, "4 tấn = 4000 kg, 5 tạ = 500 kg => 4500 kg.", "Thông hiểu"),
            make_mc(6, "Tìm x biết x : 24 = 15:", ["360", "340", "380", "320"], 0, "x = 15 x 24 = 360.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 235 x 34\nb) 9840 : 24", "a) 235 x 34 = 7990\nb) 9840 : 24 = 410", "a) 7990; b) 410", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 125 x 47 x 8\nb) 25 x 18 x 4", "a) 125 x 47 x 8 = (125 x 8) x 47 = 1000 x 47 = 47 000\nb) 25 x 18 x 4 = (25 x 4) x 18 = 100 x 18 = 1800", "a) 47 000; b) 1800", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 25 = 6250\nb) x : 35 = 120", "a) x = 6250 : 25 = 250\nb) x = 120 x 35 = 4200", "a) x = 250; b) x = 4200", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đoàn xe gồm 8 xe tải chở được 25 600 kg gạo. Người ta chuyển 5 xe về kho lương thực. Hỏi số gạo chuyển về kho lương thực là bao nhiêu tấn?", "Mỗi xe tải chở được số ki-lô-gam gạo là:\n25 600 : 8 = 3200 (kg)\nSố ki-lô-gam gạo chuyển về kho là:\n3200 x 5 = 16 000 (kg)\nĐổi: 16 000 kg = 16 tấn\nĐáp số: 16 tấn gạo.", "16 tấn", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chu vi là 160 m. Chiều dài gấp 3 lần chiều rộng. Tính diện tích của mảnh vườn đó.", "Nửa chu vi mảnh vườn là:\n160 : 2 = 80 (m)\nTổng số phần bằng nhau là:\n1 + 3 = 4 (phần)\nChiều rộng mảnh vườn là:\n80 : 4 = 20 (m)\nChiều dài mảnh vườn là:\n20 x 3 = 60 (m)\nDiện tích mảnh vườn là:\n60 x 20 = 1200 (m²)\nĐáp số: 1200 m².", "1200 m²", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 45 x 68 + 45 x 32", "45 x 68 + 45 x 32 = 45 x (68 + 32) = 45 x 100 = 4500\nĐáp số: 4500.", "4500", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b39_test2"] = {
        "id": "th4_b39_test2",
        "lessonId": "th4_b39",
        "lessonNum": 39,
        "testNum": 2,
        "title": "Bài 39: Luyện tập chung Chủ đề 8 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 8",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 340 x 50 là:", ["17 000", "1700", "170 000", "15 000"], 0, "340 x 50 = 17 000.", "Nhận biết"),
            make_mc(2, "Kết quả của 7500 : 50 là:", ["150", "15", "1500", "250"], 0, "7500 : 50 = 150.", "Thông hiểu"),
            make_mc(3, "Hình bình hành có diện tích 480 dm², chiều cao 16 dm thì cạnh đáy là:", ["30 dm", "20 dm", "25 dm", "15 dm"], 0, "480 : 16 = 30 (dm).", "Thông hiểu"),
            make_mc(4, "Tính nhanh: 5 x 72 x 20 =", ["7200", "720", "72 000", "3600"], 0, "(5 x 20) x 72 = 100 x 72 = 7200.", "Thông hiểu"),
            make_mc(5, "Đổi 6 tạ 8 yến = ... yến:", ["68", "608", "680", "86"], 0, "6 tạ = 60 yến, 60 + 8 = 68 yến.", "Thông hiểu"),
            make_mc(6, "Thương và số dư của phép chia 584 : 25 là:", ["23 dư 9", "23 dư 4", "24 dư 9", "22 dư 9"], 0, "584 : 25 = 23 (dư 9).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 318 x 26\nb) 8960 : 28", "a) 318 x 26 = 8268\nb) 8960 : 28 = 320", "a) 8268; b) 320", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 25 x 43 x 4\nb) 125 x 64 x 8", "a) 25 x 43 x 4 = (25 x 4) x 43 = 100 x 43 = 4300\nb) 125 x 64 x 8 = (125 x 8) x 64 = 1000 x 64 = 64 000", "a) 4300; b) 64 000", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 32 = 7680\nb) x : 15 = 240", "a) x = 7680 : 32 = 240\nb) x = 240 x 15 = 3600", "a) x = 240; b) x = 3600", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một nông trường có 15 thùng đựng mật ong, mỗi thùng chứa 40 chai, mỗi chai chứa 2 lít mật ong. Hỏi nông trường đó có tất cả bao nhiêu lít mật ong?", "Tổng số chai mật ong là:\n40 x 15 = 600 (chai)\nTổng số lít mật ong nông trường có là:\n2 x 600 = 1200 (lít)\nĐáp số: 1200 lít mật ong.", "1200 lít", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một khu đất hình chữ nhật có nửa chu vi là 120 m, chiều dài hơn chiều rộng 20 m. Tính diện tích khu đất đó.", "Chiều dài khu đất là:\n(120 + 20) : 2 = 70 (m)\nChiều rộng khu đất là:\n70 - 20 = 50 (m)\nDiện tích khu đất là:\n70 x 50 = 3500 (m²)\nĐáp số: 3500 m².", "3500 m²", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 64 x 25", "64 x 25 = 16 x (4 x 25) = 16 x 100 = 1600\nĐáp số: 1600.", "1600", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b39_test3"] = {
        "id": "th4_b39_test3",
        "lessonId": "th4_b39",
        "lessonNum": 39,
        "testNum": 3,
        "title": "Bài 39: Luyện tập chung Chủ đề 8 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 8",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 450 x 20 là:", ["9000", "900", "90 000", "8000"], 0, "450 x 20 = 9000.", "Nhận biết"),
            make_mc(2, "Kết quả của 10 800 : 36 là:", ["300", "30", "3000", "350"], 0, "10 800 : 36 = 300.", "Thông hiểu"),
            make_mc(3, "Hình bình hành có cạnh đáy 40 cm, chiều cao 25 cm có diện tích là:", ["1000 cm²", "500 cm²", "130 cm²", "65 cm²"], 0, "40 x 25 = 1000 (cm²).", "Thông hiểu"),
            make_mc(4, "Biểu thức 125 x 8 x 53 có giá trị là:", ["53 000", "5300", "530", "106 000"], 0, "(125 x 8) x 53 = 1000 x 53 = 53 000.", "Thông hiểu"),
            make_mc(5, "Đổi 8 tấn = ... tạ:", ["80", "800", "8000", "8"], 0, "8 tấn = 80 tạ.", "Nhận biết"),
            make_mc(6, "Tìm y biết y x 16 = 6400:", ["400", "40", "4000", "450"], 0, "y = 6400 : 16 = 400.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 425 x 32\nb) 11 760 : 42", "a) 425 x 32 = 13 600\nb) 11 760 : 42 = 280", "a) 13 600; b) 280", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 50 x 84 x 2\nb) 125 x 57 x 8", "a) 50 x 84 x 2 = (50 x 2) x 84 = 100 x 84 = 8400\nb) 125 x 57 x 8 = (125 x 8) x 57 = 1000 x 57 = 57 000", "a) 8400; b) 57 000", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 45 = 11 250\nb) x : 28 = 160", "a) x = 11 250 : 45 = 250\nb) x = 160 x 28 = 4480", "a) x = 250; b) x = 4480", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một nhà máy có 24 phân xưởng, mỗi phân xưởng đóng gói được 150 thùng bánh mỗi ngày. Hỏi trong 5 ngày, nhà máy đó đóng gói được bao nhiêu thùng bánh?", "Số thùng bánh nhà máy đóng gói được trong 1 ngày là:\n150 x 24 = 3600 (thùng)\nSố thùng bánh nhà máy đóng gói được trong 5 ngày là:\n3600 x 5 = 18 000 (thùng)\nĐáp số: 18 000 thùng bánh.", "18 000 thùng", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một khu vườn hình chữ nhật có chu vi là 240 m, chiều rộng bằng 1/3 chiều dài. Tính diện tích khu vườn đó.", "Nửa chu vi khu vườn là:\n240 : 2 = 120 (m)\nTổng số phần bằng nhau là:\n1 + 3 = 4 (phần)\nChiều rộng khu vườn là:\n120 : 4 = 30 (m)\nChiều dài khu vườn là:\n30 x 3 = 90 (m)\nDiện tích khu vườn là:\n90 x 30 = 2700 (m²)\nĐáp số: 2700 m².", "2700 m²", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 125 x 32 x 25", "125 x 32 x 25 = 125 x (8 x 4) x 25 = (125 x 8) x (4 x 25) = 1000 x 100 = 100 000\nĐáp số: 100 000.", "100 000", 4, 1.0, "Vận dụng cao")
        ]
    }

    return exams
