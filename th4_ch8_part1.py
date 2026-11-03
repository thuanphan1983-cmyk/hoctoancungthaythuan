# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 8: PHÉP NHÂN VÀ PHÉP CHIA - PHẦN 1 (BÀI 32 ĐẾN BÀI 35) - TOÁN 4 KNTT
Gồm 4 bài học, mỗi bài có 3 đề kiểm tra độc lập:
- Bài 32: Nhân với số có một chữ số (th4_b32_test1, th4_b32_test2, th4_b32_test3)
- Bài 33: Tính chất giao hoán và kết hợp của phép nhân (th4_b33_test1, th4_b33_test2, th4_b33_test3)
- Bài 34: Nhân với 10, 100, 1000,... Chia cho 10, 100, 1000,... (th4_b34_test1, th4_b34_test2, th4_b34_test3)
- Bài 35: Nhân với số có hai chữ số (th4_b35_test1, th4_b35_test2, th4_b35_test3)
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

def get_ch8_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 32: NHÂN VỚI SỐ CÓ MỘT CHỮ SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b32_test1"] = {
        "id": "th4_b32_test1",
        "lessonId": "th4_b32",
        "lessonNum": 32,
        "testNum": 1,
        "title": "Bài 32: Nhân với số có một chữ số - Đề số 1",
        "topic": "Nhân với số có một chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 14 235 x 3 là:", ["42 705", "42 605", "32 705", "42 715"], 0, "14 235 x 3 = 42 705.", "Thông hiểu"),
            make_mc(2, "Một số nhân với 1 thì bằng:", ["Chính số đó", "0", "1", "Gấp đôi số đó"], 0, "Bất kì số nào nhân với 1 cũng bằng chính nó.", "Nhận biết"),
            make_mc(3, "Tìm x biết x : 4 = 12 500. Giá trị của x là:", ["50 000", "48 000", "52 000", "3125"], 0, "x = 12 500 x 4 = 50 000.", "Thông hiểu"),
            make_mc(4, "Một bao gạo nặng 25 kg. Hỏi 6 bao gạo như thế nặng bao nhiêu ki-lô-gam?", ["120 kg", "150 kg", "160 kg", "140 kg"], 1, "6 bao nặng: 25 x 6 = 150 (kg).", "Thông hiểu"),
            make_mc(5, "Số thích hợp điền vào ô trống trong phép tính 20 300 x 4 = ... là:", ["81 200", "80 200", "81 000", "80 120"], 0, "20 300 x 4 = 81 200.", "Thông hiểu"),
            make_mc(6, "Một hình vuông có cạnh dài 1250 m. Chu vi hình vuông đó là:", ["5000 m", "2500 m", "3750 m", "10 000 m"], 0, "Chu vi hình vuông = 1250 x 4 = 5000 (m).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 24 163 x 3\nb) 15 208 x 6", "a) 24 163 x 3 = 72 489\nb) 15 208 x 6 = 91 248", "a) 72 489; b) 91 248", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 13 450 x 4 + 12 300\nb) 95 000 - 18 200 x 5", "a) 13 450 x 4 + 12 300 = 53 800 + 12 300 = 66 100\nb) 95 000 - 18 200 x 5 = 95 000 - 91 000 = 4000", "a) 66 100; b) 4000", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x : 5 = 14 260\nb) x : 7 = 8045", "a) x = 14 260 x 5 = 71 300\nb) x = 8045 x 7 = 56 315", "a) x = 71 300; b) x = 56 315", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một cửa hàng nhập về 8 thùng dầu, mỗi thùng chứa 125 lít dầu. Cửa hàng đã bán được 650 lít dầu. Hỏi cửa hàng còn lại bao nhiêu lít dầu?", "Tổng số lít dầu cửa hàng đã nhập là:\n125 x 8 = 1000 (lít)\nSố lít dầu cửa hàng còn lại là:\n1000 - 650 = 350 (lít)\nĐáp số: 350 lít dầu.", "350 lít", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một khu đất hình chữ nhật có chiều rộng là 2450 m, chiều dài gấp 3 lần chiều rộng. Tính chu vi của khu đất đó.", "Chiều dài của khu đất là:\n2450 x 3 = 7350 (m)\nChu vi của khu đất hình chữ nhật là:\n(7350 + 2450) x 2 = 19 600 (m)\nĐáp số: 19 600 m.", "19 600 m", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 125 x 8 x 7", "125 x 8 x 7 = (125 x 8) x 7 = 1000 x 7 = 7000\nĐáp số: 7000.", "7000", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b32_test2"] = {
        "id": "th4_b32_test2",
        "lessonId": "th4_b32",
        "lessonNum": 32,
        "testNum": 2,
        "title": "Bài 32: Nhân với số có một chữ số - Đề số 2",
        "topic": "Nhân với số có một chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 31 824 x 2 là:", ["63 648", "62 648", "63 548", "62 548"], 0, "31 824 x 2 = 63 648.", "Thông hiểu"),
            make_mc(2, "Số nào nhân với 0 cũng có kết quả bằng:", ["0", "1", "Chính số đó", "Không xác định"], 0, "Bất kì số nào nhân với 0 cũng bằng 0.", "Nhận biết"),
            make_mc(3, "Một ô tô chở được 1500 kg hàng. Hỏi 4 ô tô như thế chở được bao nhiêu ki-lô-gam hàng?", ["6000 kg", "5000 kg", "4500 kg", "7500 kg"], 0, "1500 x 4 = 6000 (kg).", "Thông hiểu"),
            make_mc(4, "Biểu thức 12 000 x 5 có giá trị bằng:", ["60 000", "50 000", "70 000", "65 000"], 0, "12 000 x 5 = 60 000.", "Nhận biết"),
            make_mc(5, "Chu vi của một hình tam giác đều có cạnh 215 cm là:", ["645 cm", "430 cm", "860 cm", "615 cm"], 0, "Chu vi tam giác đều = 215 x 3 = 645 (cm).", "Thông hiểu"),
            make_mc(6, "Tìm y biết y : 6 = 3500. Giá trị của y là:", ["21 000", "18 000", "24 000", "20 500"], 0, "y = 3500 x 6 = 21 000.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 18 342 x 4\nb) 27 059 x 3", "a) 18 342 x 4 = 73 368\nb) 27 059 x 3 = 81 177", "a) 73 368; b) 81 177", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 16 000 x 5 - 25 400\nb) (23 400 - 15 200) x 4", "a) 16 000 x 5 - 25 400 = 80 000 - 25 400 = 54 600\nb) (23 400 - 15 200) x 4 = 8200 x 4 = 32 800", "a) 54 600; b) 32 800", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x : 8 = 9125\nb) x : 6 = 12 400", "a) x = 9125 x 8 = 73 000\nb) x = 12 400 x 6 = 74 400", "a) x = 73 000; b) x = 74 400", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại nuôi 5 chuồng gà, mỗi chuồng có 1240 con gà. Người ta đã xuất bán đi 2500 con gà. Hỏi trang trại đó còn lại bao nhiêu con gà?", "Tổng số gà trang trại có là:\n1240 x 5 = 6200 (con)\nSố gà trang trại còn lại là:\n6200 - 2500 = 3700 (con)\nĐáp số: 3700 con gà.", "3700 con", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh đất hình chữ nhật có chiều rộng 180 m, chiều dài gấp 4 lần chiều rộng. Tính diện tích của mảnh đất đó.", "Chiều dài mảnh đất là:\n180 x 4 = 720 (m)\nDiện tích mảnh đất là:\n720 x 180 = 129 600 (m²)\nĐáp số: 129 600 m².", "129 600 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh giá trị biểu thức: 250 x 4 x 9", "250 x 4 x 9 = (250 x 4) x 9 = 1000 x 9 = 9000\nĐáp số: 9000.", "9000", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b32_test3"] = {
        "id": "th4_b32_test3",
        "lessonId": "th4_b32",
        "lessonNum": 32,
        "testNum": 3,
        "title": "Bài 32: Nhân với số có một chữ số - Đề số 3",
        "topic": "Nhân với số có một chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 16 075 x 5 là:", ["80 375", "80 275", "80 475", "75 375"], 0, "16 075 x 5 = 80 375.", "Thông hiểu"),
            make_mc(2, "Gấp số 15 200 lên 4 lần ta được:", ["60 800", "60 000", "61 800", "58 800"], 0, "15 200 x 4 = 60 800.", "Thông hiểu"),
            make_mc(3, "Một xí nghiệp may mỗi ngày may được 450 bộ quần áo. Hỏi trong 6 ngày xí nghiệp may được bao nhiêu bộ quần áo?", ["2700 bộ", "2600 bộ", "2800 bộ", "2500 bộ"], 0, "450 x 6 = 2700 (bộ).", "Thông hiểu"),
            make_mc(4, "Giá trị của chữ số 6 trong tích 12 345 x 5 là:", ["Không có chữ số 6", "60 000", "6000", "600"], 1, "12 345 x 5 = 61 725. Chữ số 6 ở hàng chục nghìn nên có giá trị 60 000.", "Thông hiểu"),
            make_mc(5, "Một hình vuông có chu vi là 36 cm thì diện tích của nó là:", ["81 cm²", "72 cm²", "64 cm²", "100 cm²"], 0, "Cạnh = 36 : 4 = 9 cm. Diện tích = 9 x 9 = 81 (cm²).", "Thông hiểu"),
            make_mc(6, "Nếu a = 12 050 thì giá trị của biểu thức a x 7 là:", ["84 350", "84 050", "85 350", "83 350"], 0, "12 050 x 7 = 84 350.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 32 418 x 3\nb) 14 625 x 5", "a) 32 418 x 3 = 97 254\nb) 14 625 x 5 = 73 125", "a) 97 254; b) 73 125", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 18 500 x 3 + 24 500\nb) 80 000 - 14 200 x 4", "a) 18 500 x 3 + 24 500 = 55 500 + 24 500 = 80 000\nb) 80 000 - 14 200 x 4 = 80 000 - 56 800 = 23 200", "a) 80 000; b) 23 200", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x : 4 = 21 350\nb) x : 9 = 6205", "a) x = 21 350 x 4 = 85 400\nb) x = 6205 x 9 = 55 845", "a) x = 85 400; b) x = 55 845", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đoàn xe vận chuyển gồm 7 xe tải, mỗi xe chở được 2350 kg ngô. Người ta đã chuyển giao 12 500 kg ngô cho nhà máy. Hỏi trên đoàn xe còn lại bao nhiêu ki-lô-gam ngô?", "Tổng khối lượng ngô trên đoàn xe là:\n2350 x 7 = 16 450 (kg)\nKhối lượng ngô còn lại là:\n16 450 - 12 500 = 3950 (kg)\nĐáp số: 3950 kg ngô.", "3950 kg", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một khu vườn hình chữ nhật có chu vi là 480 m, chiều dài gấp 3 lần chiều rộng. Tính diện tích của khu vườn đó.", "Nửa chu vi khu vườn là:\n480 : 2 = 240 (m)\nTổng số phần bằng nhau là:\n1 + 3 = 4 (phần)\nChiều rộng khu vườn là:\n240 : 4 = 60 (m)\nChiều dài khu vườn là:\n60 x 3 = 180 (m)\nDiện tích khu vườn là:\n180 x 60 = 10 800 (m²)\nĐáp số: 10 800 m².", "10 800 m²", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 500 x 8 x 3", "500 x 8 x 3 = (500 x 8) x 3 = 4000 x 3 = 12 000\nĐáp số: 12 000.", "12 000", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 33: TÍNH CHẤT GIAO HOÁN VÀ KẾT HỢP CỦA PHÉP NHÂN (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b33_test1"] = {
        "id": "th4_b33_test1",
        "lessonId": "th4_b33",
        "lessonNum": 33,
        "testNum": 1,
        "title": "Bài 33: Tính chất giao hoán và kết hợp của phép nhân - Đề số 1",
        "topic": "Tính chất giao hoán và kết hợp của phép nhân",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Biểu thức thể hiện tính chất giao hoán của phép nhân là:", ["a x b = b x a", "(a x b) x c = a x (b x c)", "a x 1 = a", "a x 0 = 0"], 0, "Tính chất giao hoán: Khi đổi chỗ các thừa số trong một tích thì tích không thay đổi: a x b = b x a.", "Nhận biết"),
            make_mc(2, "Số thích hợp điền vào chỗ chấm để 25 x 4 = 4 x ... là:", ["25", "100", "4", "1"], 0, "Theo tính chất giao hoán, 25 x 4 = 4 x 25.", "Nhận biết"),
            make_mc(3, "Giá trị của biểu thức 2 x 45 x 5 là:", ["450", "90", "500", "400"], 0, "2 x 45 x 5 = (2 x 5) x 45 = 10 x 45 = 450.", "Thông hiểu"),
            make_mc(4, "Biểu thức nào dưới đây bằng (12 x 5) x 4?", ["12 x (5 x 4)", "12 x 5 + 4", "(12 + 5) x 4", "12 + 5 + 4"], 0, "Theo tính chất kết hợp của phép nhân: (a x b) x c = a x (b x c).", "Nhận biết"),
            make_mc(5, "Tính nhanh 25 x 9 x 4 có kết quả là:", ["900", "100", "90", "9000"], 0, "(25 x 4) x 9 = 100 x 9 = 900.", "Thông hiểu"),
            make_mc(6, "Nếu a x b = 150 thì (a x 2) x b bằng:", ["300", "150", "600", "75"], 0, "(a x 2) x b = (a x b) x 2 = 150 x 2 = 300.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Điền số thích hợp vào ô trống:\na) 345 x 6 = 6 x ...\nb) 25 x 37 x 4 = (... x ...) x 37", "a) 345 x 6 = 6 x 345\nb) 25 x 37 x 4 = (25 x 4) x 37", "a) 345; b) 25 và 4", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 5 x 76 x 2\nb) 25 x 18 x 4", "a) 5 x 76 x 2 = (5 x 2) x 76 = 10 x 76 = 760\nb) 25 x 18 x 4 = (25 x 4) x 18 = 100 x 18 = 1800", "a) 760; b) 1800", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính bằng cách thuận tiện nhất:\na) 125 x 39 x 8\nb) 50 x 67 x 2", "a) 125 x 39 x 8 = (125 x 8) x 39 = 1000 x 39 = 39 000\nb) 50 x 67 x 2 = (50 x 2) x 67 = 100 x 67 = 6700", "a) 39 000; b) 6700", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đội xe có 4 xe chở hàng, mỗi xe chở 25 kiện hàng, mỗi kiện hàng chứa 8 chiếc áo ấm. Hỏi đội xe đó chở được tất cả bao nhiêu chiếc áo ấm?", "Tổng số kiện hàng đội xe chở là:\n4 x 25 = 100 (kiện)\nTổng số chiếc áo ấm đội xe chở là:\n100 x 8 = 800 (chiếc)\nĐáp số: 800 chiếc áo ấm.", "800 chiếc", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một lớp học có 8 nhóm học sinh, mỗi nhóm có 5 bạn, mỗi bạn đóng góp 25 quyển vở cho quỹ từ thiện. Tính tổng số quyển vở cả lớp đã quyên góp được (tính bằng cách thuận tiện nhất).", "Tổng số quyển vở cả lớp quyên góp được là:\n8 x 5 x 25 = 8 x (5 x 25) = (8 x 25) x 5 = 200 x 5 = 1000 (quyển)\n(Hoặc: (8 x 5) x 25 = 40 x 25 = 1000 quyển)\nĐáp số: 1000 quyển vở.", "1000 quyển", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh giá trị biểu thức: 4 x 17 x 25 x 2", "4 x 17 x 25 x 2 = (4 x 25) x (17 x 2) = 100 x 34 = 3400\nĐáp số: 3400.", "3400", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b33_test2"] = {
        "id": "th4_b33_test2",
        "lessonId": "th4_b33",
        "lessonNum": 33,
        "testNum": 2,
        "title": "Bài 33: Tính chất giao hoán và kết hợp của phép nhân - Đề số 2",
        "topic": "Tính chất giao hoán và kết hợp của phép nhân",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính chất (a x b) x c = a x (b x c) được gọi là:", ["Tính chất kết hợp của phép nhân", "Tính chất giao hoán của phép nhân", "Tính chất phân phối", "Tính chất nhân với 1"], 0, "Đây là tính chất kết hợp của phép nhân.", "Nhận biết"),
            make_mc(2, "Kết quả của biểu thức 125 x 7 x 8 là:", ["7000", "700", "5600", "70 000"], 0, "(125 x 8) x 7 = 1000 x 7 = 7000.", "Thông hiểu"),
            make_mc(3, "Số thích hợp điền vào dấu ? để 50 x 9 x 2 = (50 x ?) x 9 là:", ["2", "9", "50", "100"], 0, "Nhóm 50 với 2: (50 x 2) x 9 nên ? = 2.", "Nhận biết"),
            make_mc(4, "Biểu thức 2 x 34 x 5 có giá trị bằng:", ["340", "170", "680", "3400"], 0, "(2 x 5) x 34 = 10 x 34 = 340.", "Thông hiểu"),
            make_mc(5, "Khi nhân một tích hai số với số thứ ba, ta có thể:", ["Nhân số thứ nhất với tích của số thứ hai và số thứ ba", "Cộng các số lại với nhau", "Nhân số thứ nhất với số thứ ba rồi cộng số thứ hai", "Lấy tích chia cho thừa số"], 0, "Đây là định nghĩa tính chất kết hợp của phép nhân.", "Nhận biết"),
            make_mc(6, "Giá trị của biểu thức 20 x 15 x 5 là:", ["1500", "300", "150", "3000"], 0, "(20 x 5) x 15 = 100 x 15 = 1500.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) 48 x 75 = 75 x ...\nb) (15 x 4) x 6 = 15 x (... x 6)", "a) 48 x 75 = 75 x 48\nb) (15 x 4) x 6 = 15 x (4 x 6)", "a) 48; b) 4", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 2 x 89 x 5\nb) 4 x 47 x 25", "a) 2 x 89 x 5 = (2 x 5) x 89 = 10 x 89 = 890\nb) 4 x 47 x 25 = (4 x 25) x 47 = 100 x 47 = 4700", "a) 890; b) 4700", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tính bằng cách thuận tiện nhất:\na) 125 x 63 x 8\nb) 20 x 38 x 5", "a) 125 x 63 x 8 = (125 x 8) x 63 = 1000 x 63 = 63 000\nb) 20 x 38 x 5 = (20 x 5) x 38 = 100 x 38 = 3800", "a) 63 000; b) 3800", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một cửa hàng có 5 thùng kẹo, mỗi thùng chứa 20 hộp kẹo, mỗi hộp kẹo có 15 chiếc kẹo. Hỏi cửa hàng có tất cả bao nhiêu chiếc kẹo?", "Tổng số hộp kẹo cửa hàng có là:\n5 x 20 = 100 (hộp)\nTổng số chiếc kẹo cửa hàng có là:\n100 x 15 = 1500 (chiếc)\nĐáp số: 1500 chiếc kẹo.", "1500 chiếc", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một trường học có 4 khối lớp tham gia cắm trại, mỗi khối có 5 lớp, mỗi lớp có 30 học sinh. Tính tổng số học sinh tham gia cắm trại của trường đó bằng cách thuận tiện nhất.", "Tổng số học sinh tham gia là:\n4 x 5 x 30 = (4 x 5) x 30 = 20 x 30 = 600 (học sinh)\nĐáp số: 600 học sinh.", "600 học sinh", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 8 x 29 x 125", "8 x 29 x 125 = (8 x 125) x 29 = 1000 x 29 = 29 000\nĐáp số: 29 000.", "29 000", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b33_test3"] = {
        "id": "th4_b33_test3",
        "lessonId": "th4_b33",
        "lessonNum": 33,
        "testNum": 3,
        "title": "Bài 33: Tính chất giao hoán và kết hợp của phép nhân - Đề số 3",
        "topic": "Tính chất giao hoán và kết hợp của phép nhân",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 25 x 5 x 4 là:", ["500", "250", "1000", "100"], 0, "(25 x 4) x 5 = 100 x 5 = 500.", "Thông hiểu"),
            make_mc(2, "Số điền vào chỗ chấm để 125 x ... = 1000 là:", ["8", "6", "4", "5"], 0, "125 x 8 = 1000.", "Nhận biết"),
            make_mc(3, "Tính nhanh: 5 x 43 x 20 =", ["4300", "430", "860", "43 000"], 0, "(5 x 20) x 43 = 100 x 43 = 4300.", "Thông hiểu"),
            make_mc(4, "Điền dấu thích hợp vào chỗ chấm: 34 x 5 ... 5 x 34:", ["=", ">", "<", "Không so sánh được"], 0, "Theo tính chất giao hoán của phép nhân: 34 x 5 = 5 x 34.", "Nhận biết"),
            make_mc(5, "Giá trị của biểu thức (2 x 50) x 78 là:", ["7800", "780", "1560", "78 000"], 0, "100 x 78 = 7800.", "Thông hiểu"),
            make_mc(6, "Một mảnh vườn hình chữ nhật có chiều dài 25 m, chiều rộng 8 m. Diện tích mảnh vườn đó là:", ["200 m²", "100 m²", "66 m²", "33 m²"], 0, "25 x 8 = 200 (m²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính bằng cách thuận tiện nhất:\na) 5 x 64 x 2\nb) 25 x 73 x 4", "a) 5 x 64 x 2 = (5 x 2) x 64 = 10 x 64 = 640\nb) 25 x 73 x 4 = (25 x 4) x 73 = 100 x 73 = 7300", "a) 640; b) 7300", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) 125 x 46 x 8\nb) 50 x 82 x 2", "a) 125 x 46 x 8 = (125 x 8) x 46 = 1000 x 46 = 46 000\nb) 50 x 82 x 2 = (50 x 2) x 82 = 100 x 82 = 8200", "a) 46 000; b) 8200", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x biết:\na) x : (25 x 4) = 15\nb) x : (125 x 8) = 7", "a) x : 100 = 15 => x = 15 x 100 = 1500\nb) x : 1000 = 7 => x = 7 x 1000 = 7000", "a) x = 1500; b) x = 7000", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đoàn xe chở hàng gồm 8 xe tải, mỗi xe chở 125 thùng hàng, mỗi thùng có 6 hộp bánh. Tính tổng số hộp bánh mà đoàn xe chở được bằng cách thuận tiện nhất.", "Tổng số thùng hàng cả đoàn xe chở là:\n8 x 125 = 1000 (thùng)\nTổng số hộp bánh đoàn xe chở được là:\n1000 x 6 = 6000 (hộp)\nĐáp số: 6000 hộp bánh.", "6000 hộp bánh", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một nông trại nuôi bò sữa có 4 dãy chuồng, mỗi dãy có 25 con bò, mỗi con bò trung bình cho 18 lít sữa mỗi ngày. Hỏi mỗi ngày nông trại thu được bao nhiêu lít sữa?", "Tổng số bò của nông trại là:\n4 x 25 = 100 (con)\nSố lít sữa nông trại thu được mỗi ngày là:\n100 x 18 = 1800 (lít)\nĐáp số: 1800 lít sữa.", "1800 lít", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 2 x 125 x 4 x 8 x 5", "Nhóm các thừa số hợp lý:\n(2 x 5) x (125 x 8) x 4 = 10 x 1000 x 4 = 40 000\nĐáp số: 40 000.", "40 000", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 34: NHÂN, CHIA CHO 10, 100, 1000,... (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b34_test1"] = {
        "id": "th4_b34_test1",
        "lessonId": "th4_b34",
        "lessonNum": 34,
        "testNum": 1,
        "title": "Bài 34: Nhân với 10, 100, 1000,... Chia cho 10, 100, 1000,... - Đề số 1",
        "topic": "Nhân với 10, 100, 1000,... Chia cho 10, 100, 1000,...",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khi nhân một số tự nhiên với 10, 100, 1000,... ta chỉ việc:", ["Viết thêm một, hai, ba,... chữ số 0 vào bên phải số đó", "Bớt đi các chữ số 0", "Nhân với chữ số 1", "Cộng thêm 10, 100, 1000"], 0, "Quy tắc: Nhân với 10, 100, 1000,... thì viết thêm tương ứng 1, 2, 3,... chữ số 0 vào bên phải số đó.", "Nhận biết"),
            make_mc(2, "Kết quả của phép tính 235 x 100 là:", ["23 500", "2350", "235 000", "235000"], 0, "235 x 100 = 23 500.", "Thông hiểu"),
            make_mc(3, "Kết quả của phép chia 45 000 : 100 là:", ["450", "45", "4500", "45 000"], 0, "Bớt đi hai chữ số 0 ở bên phải: 45 000 : 100 = 450.", "Thông hiểu"),
            make_mc(4, "Số thích hợp điền vào chỗ chấm để ... x 10 = 18 000 là:", ["1800", "180", "18", "180 000"], 0, "18 000 : 10 = 1800.", "Thông hiểu"),
            make_mc(5, "Đổi: 5 tấn = ... kg:", ["5000", "500", "50", "50 000"], 0, "1 tấn = 1000 kg nên 5 tấn = 5000 kg.", "Nhận biết"),
            make_mc(6, "Kết quả của 72 000 : 1000 là:", ["72", "720", "7200", "7"], 0, "72 000 : 1000 = 72.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) 34 x 10\nb) 205 x 100\nc) 18 x 1000\nd) 54 000 : 100", "a) 34 x 10 = 340\nb) 205 x 100 = 20 500\nc) 18 x 1000 = 18 000\nd) 54 000 : 100 = 540", "a) 340; b) 20 500; c) 18 000; d) 540", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) 6 tấn = ... kg\nb) 400 yến = ... tạ\nc) 8000 kg = ... tấn\nd) 12 tạ = ... yến", "a) 6 tấn = 6000 kg\nb) 400 yến = 40 tạ\nc) 8000 kg = 8 tấn\nd) 12 tạ = 120 yến", "a) 6000; b) 40; c) 8; d) 120", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 100 = 42 000\nb) x : 10 = 3560", "a) x = 42 000 : 100 = 420\nb) x = 3560 x 10 = 35 600", "a) x = 420; b) x = 35 600", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một cửa hàng nhập về 100 bao xi măng, mỗi bao nặng 50 kg. Hỏi cửa hàng đã nhập về tất cả bao nhiêu tấn xi măng?", "Tổng khối lượng xi măng đã nhập là:\n50 x 100 = 5000 (kg)\nĐổi: 5000 kg = 5 tấn\nĐáp số: 5 tấn xi măng.", "5 tấn", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một đoàn tàu chở 10 toa hàng, mỗi toa chở 12 tấn hàng. Sau đó người ta dỡ xuống 40 tấn hàng. Hỏi đoàn tàu còn chở lại bao nhiêu tấn hàng?", "Tổng số tấn hàng đoàn tàu chở ban đầu là:\n12 x 10 = 120 (tấn)\nSố tấn hàng còn lại là:\n120 - 40 = 80 (tấn)\nĐáp số: 80 tấn hàng.", "80 tấn", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 3400 : 100 x 50", "3400 : 100 x 50 = 34 x 50 = 1700\nĐáp số: 1700.", "1700", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b34_test2"] = {
        "id": "th4_b34_test2",
        "lessonId": "th4_b34",
        "lessonNum": 34,
        "testNum": 2,
        "title": "Bài 34: Nhân với 10, 100, 1000,... Chia cho 10, 100, 1000,... - Đề số 2",
        "topic": "Nhân với 10, 100, 1000,... Chia cho 10, 100, 1000,...",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khi chia một số tròn chục, tròn trăm, tròn nghìn cho 10, 100, 1000,... ta bớt đi ở bên phải số đó lần lượt là:", ["1, 2, 3,... chữ số 0", "Thêm các chữ số 0", "Nhân với 10", "Không thay đổi"], 0, "Quy tắc chia cho 10, 100, 1000,... là bớt đi 1, 2, 3,... chữ số 0.", "Nhận biết"),
            make_mc(2, "Kết quả của 480 x 100 là:", ["48 000", "4800", "480 000", "480"], 0, "480 x 100 = 48 000.", "Thông hiểu"),
            make_mc(3, "Kết quả của 360 000 : 1000 là:", ["360", "36", "3600", "36 000"], 0, "Bớt đi 3 chữ số 0: 360 000 : 1000 = 360.", "Thông hiểu"),
            make_mc(4, "Đổi: 7000 kg = ... tạ:", ["70", "7", "700", "7000"], 0, "1 tạ = 100 kg nên 7000 kg = 70 tạ.", "Thông hiểu"),
            make_mc(5, "Số nào nhân với 100 thì được 85 000?", ["850", "85", "8500", "850 000"], 0, "85 000 : 100 = 850.", "Thông hiểu"),
            make_mc(6, "Một tấm vải dài 10 m. Người ta cắt ra các mảnh vải dài 1 m. Số mảnh vải cắt được là:", ["10 mảnh", "100 mảnh", "5 mảnh", "20 mảnh"], 0, "10 : 1 = 10 (mảnh).", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) 560 x 10\nb) 78 x 100\nc) 62 000 : 10\nd) 90 000 : 1000", "a) 560 x 10 = 5600\nb) 78 x 100 = 7800\nc) 62 000 : 10 = 6200\nd) 90 000 : 1000 = 90", "a) 5600; b) 7800; c) 6200; d) 90", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Điền số thích hợp vào chỗ chấm:\na) 9 tấn = ... tạ\nb) 500 yến = ... tạ\nc) 30 000 kg = ... tấn\nd) 4 tạ 5 yến = ... yến", "a) 9 tấn = 90 tạ\nb) 500 yến = 50 tạ\nc) 30 000 kg = 30 tấn\nd) 4 tạ 5 yến = 45 yến", "a) 90; b) 50; c) 30; d) 45", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm y:\na) y x 1000 = 75 000\nb) y : 100 = 480", "a) y = 75 000 : 1000 = 75\nb) y = 480 x 100 = 48 000", "a) y = 75; b) y = 48 000", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại thu hoạch được 1000 bao ngô, mỗi bao nặng 45 kg. Hỏi cả trang trại thu hoạch được bao nhiêu tấn ngô?", "Tổng khối lượng ngô trang trại thu hoạch là:\n45 x 1000 = 45 000 (kg)\nĐổi: 45 000 kg = 45 tấn\nĐáp số: 45 tấn ngô.", "45 tấn", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một xí nghiệp đóng gói 50 000 chiếc bút bi vào các hộp, mỗi hộp có 100 chiếc bút. Hỏi xí nghiệp đó đóng được tất cả bao nhiêu hộp bút?", "Số hộp bút đóng được là:\n50 000 : 100 = 500 (hộp)\nĐáp số: 500 hộp bút.", "500 hộp", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 120 x 50 : 10", "120 x 50 : 10 = 120 : 10 x 50 = 12 x 50 = 600\nĐáp số: 600.", "600", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b34_test3"] = {
        "id": "th4_b34_test3",
        "lessonId": "th4_b34",
        "lessonNum": 34,
        "testNum": 3,
        "title": "Bài 34: Nhân với 10, 100, 1000,... Chia cho 10, 100, 1000,... - Đề số 3",
        "topic": "Nhân với 10, 100, 1000,... Chia cho 10, 100, 1000,...",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính 1500 x 10 là:", ["15 000", "150 000", "1500", "150"], 0, "1500 x 10 = 15 000.", "Nhận biết"),
            make_mc(2, "Số thích hợp để 8400 : ... = 84 là:", ["100", "10", "1000", "1"], 0, "8400 : 84 = 100.", "Thông hiểu"),
            make_mc(3, "Một bao đường nặng 50 kg. 100 bao đường như thế nặng bao nhiêu tạ?", ["50 tạ", "500 tạ", "5 tạ", "5000 tạ"], 0, "50 x 100 = 5000 kg = 50 tạ.", "Thông hiểu"),
            make_mc(4, "Kết quả của 95 000 : 100 là:", ["950", "95", "9500", "95 000"], 0, "95 000 : 100 = 950.", "Thông hiểu"),
            make_mc(5, "Đổi: 12 tấn = ... kg:", ["12 000", "1200", "120", "120 000"], 0, "12 tấn = 12 000 kg.", "Nhận biết"),
            make_mc(6, "Tìm x biết x : 100 = 75:", ["7500", "750", "75 000", "75"], 0, "x = 75 x 100 = 7500.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Tính nhẩm:\na) 69 x 100\nb) 400 x 10\nc) 85 000 : 100\nd) 120 000 : 1000", "a) 69 x 100 = 6900\nb) 400 x 10 = 4000\nc) 85 000 : 100 = 850\nd) 120 000 : 1000 = 120", "a) 6900; b) 4000; c) 850; d) 120", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) 15 tấn = ... tạ\nb) 800 tạ = ... tấn\nc) 45 000 kg = ... tấn\nd) 25 tạ = ... kg", "a) 15 tấn = 150 tạ\nb) 800 tạ = 80 tấn\nc) 45 000 kg = 45 tấn\nd) 25 tạ = 2500 kg", "a) 150; b) 80; c) 45; d) 2500", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x x 10 = 24 800\nb) x : 1000 = 36", "a) x = 24 800 : 10 = 2480\nb) x = 36 x 1000 = 36 000", "a) x = 2480; b) x = 36 000", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một kho lương thực có 100 bao gạo tẻ và 100 bao gạo nếp. Mỗi bao gạo tẻ nặng 50 kg, mỗi bao gạo nếp nặng 40 kg. Hỏi kho lương thực đó có tất cả bao nhiêu tấn gạo?", "Tổng khối lượng gạo tẻ là:\n50 x 100 = 5000 (kg)\nTổng khối lượng gạo nếp là:\n40 x 100 = 4000 (kg)\nTổng khối lượng cả hai loại gạo là:\n5000 + 4000 = 9000 (kg)\nĐổi: 9000 kg = 9 tấn\nĐáp số: 9 tấn gạo.", "9 tấn", 6, 1.5, "Vận dụng"),
            make_essay(5, "Một xưởng sản xuất đóng 24 000 gói bánh vào các thùng, mỗi thùng chứa 100 gói bánh. Người ta đã vận chuyển đi 150 thùng bánh. Hỏi xưởng đó còn lại bao nhiêu thùng bánh?", "Tổng số thùng bánh xưởng đóng được là:\n24 000 : 100 = 240 (thùng)\nSố thùng bánh xưởng còn lại là:\n240 - 150 = 90 (thùng)\nĐáp số: 90 thùng bánh.", "90 thùng", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính giá trị biểu thức bằng cách thuận tiện: 45 000 : 10 : 5", "45 000 : (10 x 5) = 45 000 : 50 = 900\nĐáp số: 900.", "900", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 35: NHÂN VỚI SỐ CÓ HAI CHỮ SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b35_test1"] = {
        "id": "th4_b35_test1",
        "lessonId": "th4_b35",
        "lessonNum": 35,
        "testNum": 1,
        "title": "Bài 35: Nhân với số có hai chữ số - Đề số 1",
        "topic": "Nhân với số có hai chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 36 x 24 là:", ["864", "844", "764", "884"], 0, "36 x 24 = 864.", "Thông hiểu"),
            make_mc(2, "Khi đặt tính nhân với số có hai chữ số, tích riêng thứ hai phải viết lùi sang bên trái so với tích riêng thứ nhất mấy cột?", ["1 cột", "2 cột", "3 cột", "Thẳng cột"], 0, "Tích riêng thứ hai chỉ hàng chục nên lùi sang bên trái 1 cột.", "Nhận biết"),
            make_mc(3, "Một mảnh vườn hình chữ nhật có chiều dài 35 m, chiều rộng 18 m. Diện tích mảnh vườn là:", ["630 m²", "620 m²", "530 m²", "106 m²"], 0, "35 x 18 = 630 (m²).", "Thông hiểu"),
            make_mc(4, "Kết quả của 145 x 12 là:", ["1740", "1640", "1840", "1540"], 0, "145 x 12 = 1740.", "Thông hiểu"),
            make_mc(5, "Một quyển vở có 48 trang. Hỏi 25 quyển vở như thế có tất cả bao nhiêu trang?", ["1200 trang", "1000 trang", "1100 trang", "1250 trang"], 0, "48 x 25 = 1200 (trang).", "Thông hiểu"),
            make_mc(6, "Giá trị của biểu thức 26 x 11 là:", ["286", "266", "296", "276"], 0, "26 x 11 = 286.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 48 x 23\nb) 135 x 26", "a) 48 x 23 = 1104\nb) 135 x 26 = 3510", "a) 1104; b) 3510", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 214 x 15 - 1200\nb) 45 x 28 + 350", "a) 214 x 15 - 1200 = 3210 - 1200 = 2010\nb) 45 x 28 + 350 = 1260 + 350 = 1610", "a) 2010; b) 1610", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x : 15 = 48\nb) x : 24 = 125", "a) x = 48 x 15 = 720\nb) x = 125 x 24 = 3000", "a) x = 720; b) x = 3000", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trường tiểu học mua 35 bộ bàn ghế, mỗi bộ bàn ghế có giá 240 000 đồng. Hỏi nhà trường phải trả tất cả bao nhiêu tiền?", "Nhà trường phải trả tất cả số tiền là:\n240 000 x 35 = 8 400 000 (đồng)\nĐáp số: 8 400 000 đồng.", "8 400 000 đồng", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một khu đất hình chữ nhật có chiều rộng là 24 m, chiều dài gấp đôi chiều rộng. Tính diện tích của khu đất hình chữ nhật đó.", "Chiều dài khu đất là:\n24 x 2 = 48 (m)\nDiện tích khu đất là:\n48 x 24 = 1152 (m²)\nĐáp số: 1152 m².", "1152 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 35 x 11 + 65 x 11", "35 x 11 + 65 x 11 = (35 + 65) x 11 = 100 x 11 = 1100\nĐáp số: 1100.", "1100", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b35_test2"] = {
        "id": "th4_b35_test2",
        "lessonId": "th4_b35",
        "lessonNum": 35,
        "testNum": 2,
        "title": "Bài 35: Nhân với số có hai chữ số - Đề số 2",
        "topic": "Nhân với số có hai chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 52 x 31 là:", ["1612", "1512", "1622", "1522"], 0, "52 x 31 = 1612.", "Thông hiểu"),
            make_mc(2, "Tích của 25 và 40 là:", ["1000", "100", "10 000", "500"], 0, "25 x 40 = 1000.", "Nhận biết"),
            make_mc(3, "Một ô tô chạy trong 14 giờ, mỗi giờ đi được 45 km. Quãng đường ô tô đã đi là:", ["630 km", "530 km", "640 km", "620 km"], 0, "45 x 14 = 630 (km).", "Thông hiểu"),
            make_mc(4, "Kết quả của phép tính 208 x 16 là:", ["3328", "3228", "3318", "3128"], 0, "208 x 16 = 3328.", "Thông hiểu"),
            make_mc(5, "Khi nhân một số với 11, ví dụ 45 x 11 ta được kết quả là:", ["495", "455", "505", "485"], 0, "45 x 11 = 495.", "Thông hiểu"),
            make_mc(6, "Một tấm bìa hình chữ nhật có kích thước 25 cm x 16 cm. Diện tích của nó là:", ["400 cm²", "200 cm²", "82 cm²", "500 cm²"], 0, "25 x 16 = 400 (cm²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 56 x 34\nb) 246 x 18", "a) 56 x 34 = 1904\nb) 246 x 18 = 4428", "a) 1904; b) 4428", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị biểu thức:\na) 152 x 24 - 1648\nb) 36 x 45 + 1380", "a) 152 x 24 - 1648 = 3648 - 1648 = 2000\nb) 36 x 45 + 1380 = 1620 + 1380 = 3000", "a) 2000; b) 3000", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x : 26 = 65\nb) x : 32 = 114", "a) x = 65 x 26 = 1690\nb) x = 114 x 32 = 3648", "a) x = 1690; b) x = 3648", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đoàn xe gồm 15 xe tải, mỗi xe chở được 35 tạ hàng. Hỏi cả đoàn xe chở được tất cả bao nhiêu tạ hàng?", "Cả đoàn xe chở được số tạ hàng là:\n35 x 15 = 525 (tạ)\nĐáp số: 525 tạ hàng.", "525 tạ", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chiều rộng 28 m, chiều dài hơn chiều rộng 12 m. Tính diện tích mảnh vườn hình chữ nhật đó.", "Chiều dài mảnh vườn là:\n28 + 12 = 40 (m)\nDiện tích mảnh vườn là:\n40 x 28 = 1120 (m²)\nĐáp số: 1120 m².", "1120 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 48 x 25", "48 x 25 = 12 x (4 x 25) = 12 x 100 = 1200\nĐáp số: 1200.", "1200", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b35_test3"] = {
        "id": "th4_b35_test3",
        "lessonId": "th4_b35",
        "lessonNum": 35,
        "testNum": 3,
        "title": "Bài 35: Nhân với số có hai chữ số - Đề số 3",
        "topic": "Nhân với số có hai chữ số",
        "chapter": "Chủ đề 8: Phép nhân và phép chia",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân 47 x 26 là:", ["1222", "1212", "1232", "1122"], 0, "47 x 26 = 1222.", "Thông hiểu"),
            make_mc(2, "Số thích hợp điền vào dấu ? để 18 x 15 = 9 x ? là:", ["30", "15", "60", "20"], 0, "18 x 15 = (9 x 2) x 15 = 9 x 30. Vậy ? = 30.", "Thông hiểu"),
            make_mc(3, "Một cửa hàng bán được 25 bao gạo, mỗi bao nặng 45 kg. Cửa hàng đã bán được số ki-lô-gam gạo là:", ["1125 kg", "1025 kg", "1150 kg", "1225 kg"], 0, "45 x 25 = 1125 (kg).", "Thông hiểu"),
            make_mc(4, "Kết quả của 315 x 21 là:", ["6615", "6515", "6625", "6315"], 0, "315 x 21 = 6615.", "Thông hiểu"),
            make_mc(5, "Tính nhẩm 72 x 11 ta được:", ["792", "782", "802", "772"], 0, "72 x 11 = 792.", "Thông hiểu"),
            make_mc(6, "Một tấm thảm hình chữ nhật có kích thước 32 dm x 15 dm. Diện tích tấm thảm là:", ["480 dm²", "240 dm²", "460 dm²", "450 dm²"], 0, "32 x 15 = 480 (dm²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 63 x 28\nb) 325 x 14", "a) 63 x 28 = 1764\nb) 325 x 14 = 4550", "a) 1764; b) 4550", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Tính giá trị của biểu thức:\na) 184 x 25 - 2600\nb) 48 x 35 + 1320", "a) 184 x 25 - 2600 = 4600 - 2600 = 2000\nb) 48 x 35 + 1320 = 1680 + 1320 = 3000", "a) 2000; b) 3000", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x:\na) x : 18 = 75\nb) x : 45 = 120", "a) x = 75 x 18 = 1350\nb) x = 120 x 45 = 5400", "a) x = 1350; b) x = 5400", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một phân xưởng may trong 24 ngày may được bao nhiêu bộ quần áo, biết mỗi ngày phân xưởng may được 135 bộ quần áo?", "Trong 24 ngày phân xưởng may được số bộ quần áo là:\n135 x 24 = 3240 (bộ)\nĐáp số: 3240 bộ quần áo.", "3240 bộ", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh đất hình chữ nhật có nửa chu vi là 75 m, chiều dài hơn chiều rộng 15 m. Tính diện tích của mảnh đất hình chữ nhật đó.", "Chiều dài mảnh đất là:\n(75 + 15) : 2 = 45 (m)\nChiều rộng mảnh đất là:\n75 - 45 = 30 (m)\nDiện tích mảnh đất là:\n45 x 30 = 1350 (m²)\nĐáp số: 1350 m².", "1350 m²", 6, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh: 36 x 45 + 36 x 55", "36 x 45 + 36 x 55 = 36 x (45 + 55) = 36 x 100 = 3600\nĐáp số: 3600.", "3600", 4, 1.0, "Vận dụng cao")
        ]
    }

    return exams
