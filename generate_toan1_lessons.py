# -*- coding: utf-8 -*-
"""
HỆ THỐNG SINH ĐỀ KIỂM TRA THEO BÀI CHO TOÁN 1 (KNTT)
Gồm 22 bài học, mỗi bài có 3 đề kiểm tra độc lập (Đề 1, Đề 2, Đề 3).
Tổng cộng: 66 đề kiểm tra.
Cấu trúc mỗi đề:
- Phần I: 6 câu trắc nghiệm (1.5 điểm: 6 x 0.25đ)
- Phần II: 6 bài tự luận (8.5 điểm, có trừ dòng kẻ lineCount cho học sinh làm bài)
- Tổng điểm: 10.0 điểm
"""

import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def mc(qid, question, options, correct, explanation):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.25
    }

def essay(qid, question, solution, answer, lineCount=4, points=1.0):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    return {
        "id": qid,
        "question": p_text,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_toan1_lesson_exams():
    exams = {}

    # Danh mục 22 bài học Toán 1
    # =========================================================================
    # BÀI 1: CÁC SỐ 0, 1, 2, 3, 4, 5
    # =========================================================================
    for t_idx, (num_s, rabbit_cnt, flower_cnt, apple_cnt, fish_cnt, car_cnt) in enumerate([
        ("1", 3, 4, 2, 5, 1),
        ("2", 4, 2, 5, 1, 3),
        ("3", 5, 3, 1, 4, 2)
    ], 1):
        eid = f"th1_b1_test{t_idx}"
        exams[eid] = {
            "id": eid, "lessonId": "th1_b1", "lessonNum": 1, "testNum": t_idx,
            "title": f"Bài 1: Các số 0, 1, 2, 3, 4, 5 - Đề số {t_idx}",
            "topic": "Chủ đề 1: Các số từ 0 đến 10", "chapter": "Chủ đề 1",
            "grade": "1", "term": "hk1", "duration": "35 phút", "points": 10.0,
            "part1": [
                mc(1, f"Có {rabbit_cnt} chú thỏ trắng đang ăn cỏ. Số chỉ số chú thỏ là:", [str(rabbit_cnt), str(rabbit_cnt+1), str(rabbit_cnt-1), "0"], 0, f"Có đúng {rabbit_cnt} chú thỏ."),
                mc(2, f"Số liền sau của số {flower_cnt-1} là:", [str(flower_cnt), str(flower_cnt-1), str(flower_cnt+1), "0"], 0, f"Số liền sau của {flower_cnt-1} là {flower_cnt}."),
                mc(3, f"Bình có {apple_cnt} quả táo, Mai không có quả táo nào. Số quả táo của Mai chỉ số:", ["0", "1", "2", "3"], 0, "Không có quả nào tương ứng với số 0."),
                mc(4, f"Dãy số nào sau đây được xếp theo thứ tự tăng dần?", ["0, 1, 2, 3, 4, 5", "5, 4, 3, 2, 1", "0, 2, 1, 3, 5", "1, 0, 2, 3, 4"], 0, "Dãy tăng dần từ bé đến lớn là: 0, 1, 2, 3, 4, 5."),
                mc(5, f"Số thích hợp điền vào dấu chấm: 1, 2, ..., 4, 5 là:", ["3", "2", "5", "0"], 0, "Đếm liên tiếp: 1, 2, 3, 4, 5 nên điền 3."),
                mc(6, f"Bàn tay của em có bao nhiêu ngón tay?", ["5 ngón tay", "4 ngón tay", "6 ngón tay", "3 ngón tay"], 0, "Mỗi bàn tay người bình thường có 5 ngón tay.")
            ],
            "part2": [
                essay(1, "Viết các số từ 0 đến 5 theo thứ tự từ bé đến lớn và ngược lại:", "Bài giải:\na) Từ bé đến lớn: 0, 1, 2, 3, 4, 5\nb) Từ lớn đến bé: 5, 4, 3, 2, 1, 0\nĐáp số: a) 0, 1, 2, 3, 4, 5; b) 5, 4, 3, 2, 1, 0", "a) 0, 1, 2, 3, 4, 5; b) 5, 4, 3, 2, 1, 0", 4, 1.0),
                essay(2, f"Điền số thích hợp vào chỗ chấm:\na) Có {fish_cnt} con cá đang bơi dưới nước, viết số: ........\nb) Một cành cây không có quả cam nào, viết số: ........", f"Bài giải:\na) Viết số {fish_cnt}\nb) Viết số 0\nĐáp số: a) {fish_cnt}; b) 0", f"a) {fish_cnt}; b) 0", 4, 1.0),
                essay(3, "Vẽ số hình tròn tương ứng với mỗi số sau:\na) Số 3: vẽ 3 hình tròn\nb) Số 5: vẽ 5 hình tròn", "Bài giải:\na) Học sinh vẽ 3 hình tròn: ○ ○ ○\nb) Học sinh vẽ 5 hình tròn: ○ ○ ○ ○ ○\nĐáp số: 3 hình tròn và 5 hình tròn", "Vẽ đúng số lượng hình", 4, 1.0),
                essay(4, f"Lan có {apple_cnt} bông hoa đỏ và {car_cnt} bông hoa vàng. Hỏi Lan có tất cả bao nhiêu bông hoa?", f"Bài giải:\nLan có tất cả số bông hoa là:\n{apple_cnt} + {car_cnt} = {apple_cnt + car_cnt} (bông hoa)\nĐáp số: {apple_cnt + car_cnt} bông hoa", f"{apple_cnt + car_cnt} bông hoa", 5, 1.5),
                essay(5, f"Tìm số liền trước và số liền sau của mỗi số sau:\na) Số {rabbit_cnt}\nb) Số {flower_cnt}", f"Bài giải:\na) Số {rabbit_cnt}: Liền trước là {rabbit_cnt-1}, liền sau là {rabbit_cnt+1}\nb) Số {flower_cnt}: Liền trước là {flower_cnt-1}, liền sau là {flower_cnt+1}\nĐáp số: a) {rabbit_cnt-1} và {rabbit_cnt+1}; b) {flower_cnt-1} và {flower_cnt+1}", f"a) {rabbit_cnt-1}, {rabbit_cnt+1}; b) {flower_cnt-1}, {flower_cnt+1}", 5, 2.0),
                essay(6, "Điền số thích hợp vào ô trống:\na) 0, 1, ..., 3, ...\nb) 5, 4, ..., 2, ..., 0", "Bài giải:\na) Điền 2 và 4 (ta có dãy: 0, 1, 2, 3, 4)\nb) Điền 3 và 1 (ta có dãy: 5, 4, 3, 2, 1, 0)\nĐáp số: a) 2, 4; b) 3, 1", "a) 2, 4; b) 3, 1", 4, 2.0)
            ]
        }

    # =========================================================================
    # BÀI 2: CÁC SỐ 6, 7, 8, 9, 10
    # =========================================================================
    for t_idx, (s6, s7, s8, s9, s10) in enumerate([
        (6, 7, 8, 9, 10),
        (7, 8, 6, 10, 9),
        (8, 6, 9, 7, 10)
    ], 1):
        eid = f"th1_b2_test{t_idx}"
        exams[eid] = {
            "id": eid, "lessonId": "th1_b2", "lessonNum": 2, "testNum": t_idx,
            "title": f"Bài 2: Các số 6, 7, 8, 9, 10 - Đề số {t_idx}",
            "topic": "Chủ đề 1: Các số từ 0 đến 10", "chapter": "Chủ đề 1",
            "grade": "1", "term": "hk1", "duration": "35 phút", "points": 10.0,
            "part1": [
                mc(1, f"Số liền sau của số {s7-1} là:", [str(s7), str(s7-1), str(s7+1), "10"], 0, f"Số liền sau của {s7-1} là {s7}."),
                mc(2, f"Số lớn nhất trong các số 6, 8, 7, 10 là:", ["10", "8", "7", "6"], 0, "Số 10 là số lớn nhất trong phạm vi 10."),
                mc(3, f"Số chấm tròn trên 2 bàn tay xòe ra của một người là:", ["10", "8", "9", "7"], 0, "Hai bàn tay xòe đủ có 10 ngón tay."),
                mc(4, f"Dãy số đếm bớt dần nào sau đây đúng?", ["10, 9, 8, 7, 6", "6, 7, 8, 9, 10", "10, 8, 9, 7, 6", "9, 10, 8, 7, 6"], 0, "Bớt dần từng đơn vị: 10, 9, 8, 7, 6."),
                mc(5, f"Số bảy được viết là:", ["7", "6", "8", "9"], 0, "Số bảy viết là chữ số 7."),
                mc(6, f"Con nhện có 8 cái chân. Số chân con nhện là số:", ["8", "6", "7", "9"], 0, "Số 8 biểu thị số chân của con nhện.")
            ],
            "part2": [
                essay(1, "Viết các số 7, 10, 6, 9, 8 theo thứ tự:\na) Từ bé đến lớn\nb) Từ lớn đến bé", "Bài giải:\na) Từ bé đến lớn: 6, 7, 8, 9, 10\nb) Từ lớn đến bé: 10, 9, 8, 7, 6\nĐáp số: a) 6, 7, 8, 9, 10; b) 10, 9, 8, 7, 6", "a) 6, 7, 8, 9, 10; b) 10, 9, 8, 7, 6", 4, 1.0),
                essay(2, f"Tìm số liền trước và liền sau của số {s8}:", f"Bài giải:\nSố liền trước của {s8} là {s8-1}\nSố liền sau của {s8} là {s8+1}\nĐáp số: Liền trước: {s8-1}; Liền sau: {s8+1}", f"{s8-1} và {s8+1}", 4, 1.0),
                essay(3, "Điền số thích hợp vào chỗ chấm:\na) 6, 7, ..., 9, 10\nb) 10, ..., 8, 7, ...", "Bài giải:\na) Số còn thiếu là 8 (dãy 6, 7, 8, 9, 10)\nb) Số còn thiếu là 9 và 6 (dãy 10, 9, 8, 7, 6)\nĐáp số: a) 8; b) 9 và 6", "a) 8; b) 9 và 6", 4, 1.0),
                essay(4, f"Hộp thứ nhất có {s6} chiếc bút chì, hộp thứ hai có {10 - s6} chiếc bút chì. Hỏi cả hai hộp có tất cả bao nhiêu chiếc bút chì?", f"Bài giải:\nCả hai hộp có tất cả số bút chì là:\n{s6} + {10 - s6} = 10 (chiếc bút chì)\nĐáp số: 10 chiếc bút chì", "10 chiếc bút chì", 5, 1.5),
                essay(5, f"Cho các số: 3, 6, 8, 1, 10, 5.\na) Tìm các số bé hơn 7.\nb) Tìm các số lớn hơn 7.", "Bài giải:\na) Các số bé hơn 7 là: 1, 3, 5, 6\nb) Các số lớn hơn 7 là: 8, 10\nĐáp số: a) 1, 3, 5, 6; b) 8, 10", "a) 1, 3, 5, 6; b) 8, 10", 5, 2.0),
                essay(6, "Bạn An có 9 nhãn vở, bạn Bình có 7 nhãn vở. Hỏi bạn nào có nhiều nhãn vở hơn và nhiều hơn mấy chiếc?", "Bài giải:\nVì 9 > 7 nên bạn An có nhiều nhãn vở hơn bạn Bình.\nAn nhiều hơn Bình số nhãn vở là:\n9 - 7 = 2 (nhãn vở)\nĐáp số: Bạn An có nhiều hơn 2 nhãn vở", "An nhiều hơn 2 nhãn vở", 4, 2.0)
            ]
        }

    # =========================================================================
    # BÀI 3: NHIỀU HƠN, ÍT HƠN, BẰNG NHAU
    # =========================================================================
    for t_idx, (b1, b2) in enumerate([(4, 3), (5, 4), (6, 5)], 1):
        eid = f"th1_b3_test{t_idx}"
        exams[eid] = {
            "id": eid, "lessonId": "th1_b3", "lessonNum": 3, "testNum": t_idx,
            "title": f"Bài 3: Nhiều hơn, ít hơn, bằng nhau - Đề số {t_idx}",
            "topic": "Chủ đề 1: Các số từ 0 đến 10", "chapter": "Chủ đề 1",
            "grade": "1", "term": "hk1", "duration": "35 phút", "points": 10.0,
            "part1": [
                mc(1, f"Có {b1} chú sóc và {b2} hạt dẻ. Khẳng định nào đúng?", ["Số chú sóc nhiều hơn số hạt dẻ", "Số chú sóc ít hơn số hạt dẻ", "Số chú sóc bằng số hạt dẻ", "Không so sánh được"], 0, f"Vì {b1} > {b2} nên số chú sóc nhiều hơn."),
                mc(2, f"Có 5 bông hoa và 5 chú ong. Ta nói:", ["Số bông hoa bằng số chú ong", "Số hoa nhiều hơn số ong", "Số hoa ít hơn số ong", "Không bằng nhau"], 0, "Cùng có số lượng 5 nên bằng nhau."),
                mc(3, f"Bình có 6 viên bi, Dũng có 4 viên bi. Ta nói:", ["Số bi của Dũng ít hơn số bi của Bình", "Số bi của Dũng nhiều hơn số bi của Bình", "Số bi hai bạn bằng nhau", "Không biết"], 0, "Dũng có 4, Bình có 6 nên Dũng ít hơn."),
                mc(4, f"Nếu mỗi con mèo ăn 1 con cá, có 3 con mèo và 5 con cá thì:", ["Thừa cá", "Thiếu cá", "Vừa đủ cá", "Không có cá"], 0, "Có 5 con cá mà chỉ 3 con mèo nên còn thừa cá."),
                mc(5, f"Số lượng ngón chân trên bàn chân trái so với bàn chân phải thì:", ["Bằng nhau", "Bên trái nhiều hơn", "Bên phải nhiều hơn", "Không bằng"], 0, "Mỗi bàn chân đều có 5 ngón chân nên bằng nhau."),
                mc(6, f"Muốn số bút chì bằng số cục tẩy khi có 4 bút và 3 tẩy, ta cần:", ["Thêm 1 cục tẩy", "Bớt 1 cục tẩy", "Thêm 1 bút chì", "Không làm gì"], 0, "Thêm 1 cục tẩy để 3 + 1 = 4 bằng số bút chì.")
            ],
            "part2": [
                essay(1, "Quan sát tranh và điền từ thích hợp (nhiều hơn, ít hơn, bằng nhau):\na) 6 cái bát so với 4 cái thìa thì số bát ............... số thìa.\nb) 5 cái đĩa so với 5 cái cốc thì số đĩa ............... số cốc.", "Bài giải:\na) 6 > 4 nên số bát nhiều hơn số thìa.\nb) 5 = 5 nên số đĩa bằng nhau với số cốc.\nĐáp số: a) nhiều hơn; b) bằng nhau", "a) nhiều hơn; b) bằng nhau", 4, 1.0),
                essay(2, f"Tổ Một có {b1} bạn, tổ Hai có {b2} bạn.\na) Tổ nào có nhiều bạn hơn?\nb) Tổ nào có ít bạn hơn?", f"Bài giải:\nVì {b1} > {b2} nên:\na) Tổ Một có nhiều bạn hơn.\nb) Tổ Hai có ít bạn hơn.\nĐáp số: a) Tổ Một; b) Tổ Hai", "a) Tổ Một; b) Tổ Hai", 4, 1.0),
                essay(3, "Em hãy vẽ:\na) 4 quả cam\nb) Số quả táo nhiều hơn số quả cam 1 quả", "Bài giải:\na) Vẽ 4 quả cam: 🍊 🍊 🍊 🍊\nb) Vẽ số táo là 4 + 1 = 5 quả: 🍎 🍎 🍎 🍎 🍎\nĐáp số: 4 quả cam và 5 quả táo", "4 quả cam và 5 quả táo", 4, 1.0),
                essay(4, f"Trong bể có 7 con cá vàng và 5 con cá bảy màu. Hỏi cá vàng nhiều hơn cá bảy màu bao nhiêu con?", "Bài giải:\nSố cá vàng nhiều hơn số cá bảy màu là:\n7 - 5 = 2 (con cá)\nĐáp số: 2 con cá", "2 con cá", 5, 1.5),
                essay(5, "Đội bóng A có 6 cầu thủ, đội bóng B có 8 cầu thủ. Để số cầu thủ hai đội bằng nhau thì đội B cần chuyển sang đội A mấy cầu thủ?", "Bài giải:\nĐội B nhiều hơn đội A số cầu thủ là: 8 - 6 = 2 (cầu thủ).\nĐể hai đội bằng nhau thì đội B cần chuyển sang đội A: 2 : 2 = 1 (cầu thủ).\nKhi đó mỗi đội có: 6 + 1 = 7 (cầu thủ).\nĐáp số: 1 cầu thủ", "1 cầu thủ", 5, 2.0),
                essay(6, "Có 3 con thỏ và 4 củ cà rốt. Nếu mỗi con thỏ ăn 1 củ cà rốt thì thừa hay thiếu bao nhiêu củ cà rốt?", "Bài giải:\nVì 4 củ cà rốt trừ đi 3 củ cho 3 con thỏ:\n4 - 3 = 1 (củ cà rốt)\nNên còn thừa 1 củ cà rốt.\nĐáp số: Thừa 1 củ cà rốt", "Thừa 1 củ cà rốt", 4, 2.0)
            ]
        }

    # =========================================================================
    # BÀI 4: SO SÁNH SỐ (DẤU >, <, =)
    # =========================================================================
    for t_idx, (v1, v2, v3, v4) in enumerate([(4, 7, 5, 5), (6, 3, 8, 8), (2, 9, 7, 7)], 1):
        eid = f"th1_b4_test{t_idx}"
        exams[eid] = {
            "id": eid, "lessonId": "th1_b4", "lessonNum": 4, "testNum": t_idx,
            "title": f"Bài 4: So sánh số - Đề số {t_idx}",
            "topic": "Chủ đề 1: Các số từ 0 đến 10", "chapter": "Chủ đề 1",
            "grade": "1", "term": "hk1", "duration": "35 phút", "points": 10.0,
            "part1": [
                mc(1, f"Điền dấu thích hợp vào chỗ chấm: {v1} ... {v2}", ["<" if v1 < v2 else ">", ">" if v1 < v2 else "<", "=", "Không có"], 0, f"Vì {v1} {'bé hơn' if v1 < v2 else 'lớn hơn'} {v2}."),
                mc(2, f"Điền dấu thích hợp vào chỗ chấm: {v3} ... {v4}", ["=", ">", "<", "Không có"], 0, f"Vì hai vế đều bằng {v3} nên điền dấu =."),
                mc(3, "Phép so sánh nào dưới đây đúng?", ["3 < 5", "7 < 4", "9 < 6", "8 = 5"], 0, "3 < 5 là phép so sánh chính xác."),
                mc(4, "Số lớn nhất trong các số 2, 7, 9, 4 là:", ["9", "7", "4", "2"], 0, "Số 9 là số lớn nhất trong các số đã cho."),
                mc(5, "Số bé nhất trong các số 8, 3, 5, 1 là:", ["1", "3", "5", "8"], 0, "Số 1 là số bé nhất."),
                mc(6, "Các số 4, 1, 8, 6 được sắp xếp từ bé đến lớn là:", ["1, 4, 6, 8", "8, 6, 4, 1", "1, 6, 4, 8", "4, 1, 6, 8"], 0, "Thứ tự từ bé đến lớn: 1, 4, 6, 8.")
            ],
            "part2": [
                essay(1, "Điền dấu thích hợp (>, <, =) vào chỗ chấm:\na) 4 ... 8\nb) 9 ... 6\nc) 7 ... 7\nd) 0 ... 5", "Bài giải:\na) 4 < 8\nb) 9 > 6\nc) 7 = 7\nd) 0 < 5\nĐáp số: a) <; b) >; c) =; d) <", "a) <; b) >; c) =; d) <", 4, 1.0),
                essay(2, "Sắp xếp các số 9, 3, 7, 1, 5 theo thứ tự:\na) Từ bé đến lớn\nb) Từ lớn đến bé", "Bài giải:\na) Từ bé đến lớn: 1, 3, 5, 7, 9\nb) Từ lớn đến bé: 9, 7, 5, 3, 1\nĐáp số: a) 1, 3, 5, 7, 9; b) 9, 7, 5, 3, 1", "a) 1, 3, 5, 7, 9; b) 9, 7, 5, 3, 1", 4, 1.0),
                essay(3, "Viết các số thích hợp vào chỗ chấm:\na) Số lớn hơn 6 và bé hơn 9 là: ........\nb) Số bé hơn 2 là: ........", "Bài giải:\na) Các số lớn hơn 6 và bé hơn 9 là: 7; 8\nb) Các số bé hơn 2 là: 0; 1\nĐáp số: a) 7, 8; b) 0, 1", "a) 7, 8; b) 0, 1", 4, 1.0),
                essay(4, "Có ba hộp bút:\n- Hộp xanh có 5 chiếc bút\n- Hộp đỏ có 8 chiếc bút\n- Hộp vàng có 6 chiếc bút\nHỏi hộp nào có nhiều bút nhất? Hộp nào có ít bút nhất?", "Bài giải:\nSo sánh số bút: 5 < 6 < 8.\nDo đó:\n- Hộp đỏ có nhiều bút nhất (8 chiếc).\n- Hộp xanh có ít bút nhất (5 chiếc).\nĐáp số: Hộp đỏ nhiều nhất; Hộp xanh ít nhất", "Đỏ nhiều nhất, Xanh ít nhất", 5, 1.5),
                essay(5, "Tìm tất cả các số x thỏa mãn:\na) 4 < x < 8\nb) x ≤ 3", "Bài giải:\na) Các số x lớn hơn 4 và bé hơn 8 là: 5, 6, 7.\nb) Các số x bé hơn hoặc bằng 3 là: 0, 1, 2, 3.\nĐáp số: a) x = 5, 6, 7; b) x = 0, 1, 2, 3", "a) 5, 6, 7; b) 0, 1, 2, 3", 5, 2.0),
                essay(6, "Điền dấu thích hợp:\na) 3 + 2 ... 6\nb) 7 - 1 ... 5 + 1", "Bài giải:\na) Ta có 3 + 2 = 5, mà 5 < 6 nên 3 + 2 < 6.\nb) Ta có 7 - 1 = 6 và 5 + 1 = 6, nên 7 - 1 = 5 + 1.\nĐáp số: a) <; b) =", "a) <; b) =", 4, 2.0)
            ]
        }

    # =========================================================================
    # BÀI 5: HÌNH VUÔNG, HÌNH TRÒN, HÌNH TAM GIÁC, HÌNH CHỮ NHẬT
    # =========================================================================
    for t_idx, shape_focus in enumerate(["tam giác", "hình vuông", "hình chữ nhật"], 1):
        eid = f"th1_b5_test{t_idx}"
        exams[eid] = {
            "id": eid, "lessonId": "th1_b5", "lessonNum": 5, "testNum": t_idx,
            "title": f"Bài 5: Hình vuông, hình tròn, hình tam giác, hình chữ nhật - Đề số {t_idx}",
            "topic": "Chủ đề 2: Làm quen với một số hình phẳng", "chapter": "Chủ đề 2",
            "grade": "1", "term": "hk1", "duration": "35 phút", "points": 10.0,
            "part1": [
                mc(1, "Hình có 3 cạnh và 3 góc nhọn là:", ["Hình tam giác", "Hình tròn", "Hình vuông", "Hình chữ nhật"], 0, "Hình tam giác có 3 cạnh."),
                mc(2, "Mặt đồng hồ treo tường hình tròn có dạng hình gì?", ["Hình tròn", "Hình vuông", "Hình tam giác", "Hình chữ nhật"], 0, "Có dạng hình tròn."),
                mc(3, "Khăn quàng đỏ của học sinh tiểu học có dạng hình gì?", ["Hình tam giác", "Hình chữ nhật", "Hình vuông", "Hình tròn"], 0, "Khăn quàng đỏ dạng tam giác."),
                mc(4, "Mặt bảng lớp học thường có dạng hình gì?", ["Hình chữ nhật", "Hình vuông", "Hình tròn", "Hình tam giác"], 0, "Mặt bảng lớp có dạng hình chữ nhật dài."),
                mc(5, "Viên gạch lát sàn nhà hình vuông có bao nhiêu cạnh?", ["4 cạnh bằng nhau", "3 cạnh", "5 cạnh", "Không có cạnh nào"], 0, "Hình vuông có 4 cạnh bằng nhau."),
                mc(6, "Hình nào dưới đây không có góc và không có cạnh?", ["Hình tròn", "Hình vuông", "Hình chữ nhật", "Hình tam giác"], 0, "Hình tròn được tạo bởi đường cong khép kín.")
            ],
            "part2": [
                essay(1, "Em hãy kể tên 4 đồ vật quen thuộc trong gia đình hoặc lớp học có dạng:\na) Hình tròn\nb) Hình chữ nhật", "Bài giải:\na) Đồ vật hình tròn: đồng hồ treo tường, cái đĩa, nắp chai, bánh xe đạp.\nb) Đồ vật hình chữ nhật: quyển sách toán, mặt bàn học, cánh cửa ra vào, màn hình tivi.\nĐáp số: Học sinh nêu đúng mỗi loại 2 đồ vật trở lên", "Nêu đúng đồ vật thực tế", 4, 1.0),
                essay(2, "Hình vuông và hình tam giác khác nhau ở điểm nào?", "Bài giải:\n- Hình vuông có 4 cạnh bằng nhau và 4 góc.\n- Hình tam giác chỉ có 3 cạnh và 3 góc.\nĐáp số: Hình vuông có 4 cạnh, hình tam giác có 3 cạnh", "Hình vuông có 4 cạnh, tam giác có 3 cạnh", 4, 1.0),
                essay(3, "Vẽ các hình sau:\na) Một hình tam giác\nb) Một hình chữ nhật", "Bài giải:\nHọc sinh dùng thước kẻ vẽ chuẩn xác:\na) Vẽ hình tam giác gồm 3 đoạn thẳng khép kín.\nb) Vẽ hình chữ nhật gồm 2 cạnh dài và 2 cạnh ngắn.\nĐáp số: Hình vẽ đẹp, đúng quy cách", "Vẽ đúng hình tam giác và hình chữ nhật", 4, 1.0),
                essay(4, "Một ngôi nhà đồ chơi được ghép bởi 1 hình tam giác (mái nhà), 1 hình vuông (thân nhà) và 1 hình chữ nhật (cửa ra vào). Hỏi ngôi nhà đó được ghép từ tất cả bao nhiêu hình phẳng?", "Bài giải:\nTổng số hình phẳng ghép nên ngôi nhà là:\n1 + 1 + 1 = 3 (hình)\nĐáp số: 3 hình phẳng", "3 hình", 5, 1.5),
                essay(5, "Đếm số hình trong hình vẽ (hình thuyền buồm):\nThuyền gồm 1 thân hình thang/chữ nhật, 2 cánh buồm hình tam giác.\nHỏi có bao nhiêu hình tam giác?", "Bài giải:\nQuan sát hình cánh buồm gồm có 2 hình tam giác.\nĐáp số: 2 hình tam giác", "2 hình tam giác", 5, 2.0),
                essay(6, "Cắt một hình vuông theo đường chéo từ một góc sang góc đối diện, ta sẽ thu được mấy hình mới và đó là hình gì?", "Bài giải:\nKhi cắt đôi hình vuông theo đường chéo, ta thu được 2 hình mới.\nCả hai hình mới đều là hình tam giác.\nĐáp số: 2 hình tam giác", "2 hình tam giác", 4, 2.0)
            ]
        }

    # =========================================================================
    # BÀI 6 ĐẾN 22 CHO TOÁN 1: SINH TIẾP THEO BẢN ĐẶC TẢ
    # =========================================================================
    def build_p1_p2_for_lesson(l_num, t_num):
        """Hàm sinh tự động đề 6 trắc nghiệm + 6 tự luận chuẩn xác cho các bài còn lại"""
        if l_num == 6: # Phép cộng phạm vi 10
            v_a = 3 + t_num
            v_b = 2 + (t_num % 2)
            return [
                mc(1, f"Kết quả của phép tính ${v_a} + {v_b}$ là:", [str(v_a + v_b), str(v_a + v_b - 1), str(v_a + v_b + 1), "10"], 0, f"Ta có ${v_a} + {v_b} = {v_a + v_b}$."),
                mc(2, "Số thích hợp điền vào ô trống: $4 + ... = 7$ là:", ["3", "2", "4", "5"], 0, "$7 - 4 = 3$."),
                mc(3, "Phép tính nào có kết quả bằng 8?", ["$5 + 3$", "$4 + 3$", "$6 + 1$", "$5 + 4$"], 0, "$5 + 3 = 8$."),
                mc(4, f"Lan có {v_a} bông hoa, mẹ cho Lan thêm {v_b} bông hoa nữa. Lan có tất cả số hoa là:", [str(v_a + v_b), str(v_a + v_b + 1), str(v_a), "10"], 0, f"{v_a} + {v_b} = {v_a + v_b}."),
                mc(5, "Trong phép tính $2 + 6 = 8$, số 8 được gọi là:", ["Tổng", "Số hạng", "Hiệu", "Số trừ"], 0, "Kết quả phép cộng gọi là tổng."),
                mc(6, "Điền dấu: $3 + 4 ... 2 + 5$", ["=", ">", "<", "Không so được"], 0, "Cả hai vế đều có kết quả bằng 7.")
            ], [
                essay(1, f"Tính:\na) ${v_a} + {v_b} = .....$\nb) ${v_b} + {v_a} = .....$\nc) $2 + 5 = .....$\nd) $4 + 4 = .....$", f"Bài giải:\na) {v_a + v_b}\nb) {v_a + v_b}\nc) 7\nd) 8\nĐáp số: a) {v_a + v_b}; b) {v_a + v_b}; c) 7; d) 8", f"{v_a + v_b}, {v_a + v_b}, 7, 8", 4, 1.0),
                essay(2, "Điền số thích hợp vào chỗ chấm:\na) $3 + .... = 6$\nb) $.... + 2 = 8$\nc) $5 + .... = 9$\nd) $.... + 1 = 10$", "Bài giải:\na) 3\nb) 6\nc) 4\nd) 9\nĐáp số: 3, 6, 4, 9", "3, 6, 4, 9", 4, 1.0),
                essay(3, "Nối phép tính với kết quả thích hợp:\n- $4 + 3$ nối với 7\n- $2 + 6$ nối với 8\n- $5 + 4$ nối với 9\n- $1 + 5$ nối với 6", "Bài giải:\nHọc sinh tính nhẩm và nối đúng.\nĐáp số: Nối chuẩn xác", "Nối đúng", 4, 1.0),
                essay(4, f"Trên cây có {v_a} con chim đang đậu, có thêm {v_b} con chim bay tới đậu cùng. Hỏi trên cây có tất cả bao nhiêu con chim?", f"Bài giải:\nTrên cây có tất cả số con chim là:\n{v_a} + {v_b} = {v_a + v_b} (con chim)\nĐáp số: {v_a + v_b} con chim", f"{v_a + v_b} con chim", 5, 1.5),
                essay(5, "Viết phép tính thích hợp theo tranh vẽ:\nCó 5 chú vịt ở dưới ao và 3 chú vịt ở trên bờ. Hỏi có tất cả bao nhiêu chú vịt?", "Bài giải:\nPhép tính là: 5 + 3 = 8 (chú vịt)\nĐáp số: 8 chú vịt", "5 + 3 = 8", 5, 2.0),
                essay(6, "Tìm số điền vào ô trống sao cho: $2 + 3 + ... = 9$", "Bài giải:\nTa có 2 + 3 = 5. Để bằng 9 thì số cần điền là: 9 - 5 = 4.\nĐáp số: 4", "4", 4, 2.0)
            ]

        elif l_num == 7: # Phép trừ phạm vi 10
            v_a = 7 + (t_num % 3)
            v_b = 3 + t_num
            return [
                mc(1, f"Kết quả của phép tính ${v_a} - {v_b}$ là:", [str(v_a - v_b), str(v_a - v_b + 1), str(v_a - v_b - 1), "0"], 0, f"{v_a} - {v_b} = {v_a - v_b}."),
                mc(2, "Số thích hợp điền vào ô trống: $9 - ... = 4$ là:", ["5", "4", "3", "6"], 0, "$9 - 4 = 5$."),
                mc(3, "Phép trừ nào có kết quả bằng 3?", ["$8 - 5$", "$9 - 5$", "$7 - 3$", "$6 - 2$"], 0, "$8 - 5 = 3$."),
                mc(4, f"Hà có {v_a} chiếc kẹo, Hà cho bạn {v_b} chiếc. Hà còn lại số kẹo là:", [str(v_a - v_b), str(v_a), str(v_b), "1"], 0, f"{v_a} - {v_b} = {v_a - v_b}."),
                mc(5, "Kết quả của phép tính $6 - 0$ là:", ["6", "0", "5", "1"], 0, "Bất kỳ số nào trừ 0 vẫn bằng chính nó."),
                mc(6, "Điền dấu: $8 - 2 ... 3 + 3$", ["=", ">", "<", "Không có"], 0, "Cả hai vế đều bằng 6.")
            ], [
                essay(1, f"Tính:\na) ${v_a} - {v_b} = .....$\nb) $8 - 3 = .....$\nc) $10 - 4 = .....$\nd) $7 - 0 = .....$", f"Bài giải:\na) {v_a - v_b}\nb) 5\nc) 6\nd) 7\nĐáp số: {v_a - v_b}, 5, 6, 7", f"{v_a - v_b}, 5, 6, 7", 4, 1.0),
                essay(2, "Điền số thích hợp vào chỗ chấm:\na) $8 - .... = 3$\nb) $.... - 4 = 2$\nc) $9 - .... = 5$\nd) $10 - .... = 6$", "Bài giải:\na) 5\nb) 6\nc) 4\nd) 4\nĐáp số: 5, 6, 4, 4", "5, 6, 4, 4", 4, 1.0),
                essay(3, "Điền dấu thích hợp (>, <, =):\na) $7 - 2 ... 4$\nb) $9 - 3 ... 5 + 2$\nc) $8 - 4 ... 2 + 2$", "Bài giải:\na) 5 > 4\nb) 6 < 7\nc) 4 = 4\nĐáp số: a) >; b) <; c) =", "a) >; b) <; c) =", 4, 1.0),
                essay(4, f"Trong rổ có {v_a} quả cam. Mẹ lấy ra {v_b} quả để vắt nước. Hỏi trong rổ còn lại bao nhiêu quả cam?", f"Bài giải:\nTrong rổ còn lại số quả cam là:\n{v_a} - {v_b} = {v_a - v_b} (quả cam)\nĐáp số: {v_a - v_b} quả cam", f"{v_a - v_b} quả cam", 5, 1.5),
                essay(5, "Viết phép tính thích hợp:\nCó 7 con bướm đang đậu trên bông hoa, sau đó 3 con bướm bay đi. Hỏi còn lại mấy con bướm?", "Bài giải:\nPhép tính là: 7 - 3 = 4 (con bướm)\nĐáp số: 4 con bướm", "7 - 3 = 4", 5, 2.0),
                essay(6, "Tìm số điền vào ô vuông: $10 - 2 - ... = 5$", "Bài giải:\nTa có 10 - 2 = 8. Để bằng 5 thì số cần trừ tiếp là: 8 - 5 = 3.\nĐáp số: 3", "3", 4, 2.0)
            ]

        elif l_num == 8: # Luyện tập chung phép cộng, trừ phạm vi 10
            return [
                mc(1, "Tính: $3 + 4 - 2 = $", ["5", "6", "4", "7"], 0, "$3 + 4 = 7; 7 - 2 = 5$."),
                mc(2, "Tính: $8 - 3 + 4 = $", ["9", "8", "7", "10"], 0, "$8 - 3 = 5; 5 + 4 = 9$."),
                mc(3, "Số thích hợp: $5 + ... = 10$", ["5", "4", "6", "3"], 0, "$10 - 5 = 5$."),
                mc(4, "Số thích hợp: $... - 3 = 4$", ["7", "6", "8", "5"], 0, "$4 + 3 = 7$."),
                mc(5, "Dãy tính nào có kết quả lớn nhất?", ["$4 + 5$", "$9 - 1$", "$3 + 4$", "$10 - 3$"], 0, "$4 + 5 = 9$ là lớn nhất."),
                mc(6, "Minh có 5 viên bi, Hùng cho Minh thêm 3 viên, Minh đánh rơi 1 viên. Minh còn:", ["7 viên", "8 viên", "6 viên", "5 viên"], 0, "$5 + 3 - 1 = 7$ viên.")
            ], [
                essay(1, "Tính giá trị biểu thức:\na) $4 + 3 - 2 = .....$\nb) $8 - 5 + 4 = .....$\nc) $9 - 3 - 2 = .....$\nd) $2 + 6 - 5 = .....$", "Bài giải:\na) 5\nb) 7\nc) 4\nd) 3\nĐáp số: 5, 7, 4, 3", "5, 7, 4, 3", 4, 1.0),
                essay(2, "Điền số thích hợp:\na) $3 + ... = 8$\nb) $... + 4 = 9$\nc) $7 - ... = 2$\nd) $... - 5 = 5$", "Bài giải:\na) 5\nb) 5\nc) 5\nd) 10\nĐáp số: 5, 5, 5, 10", "5, 5, 5, 10", 4, 1.0),
                essay(3, "Điền dấu (>, <, =):\na) $4 + 4 ... 9 - 1$\nb) $3 + 5 ... 10 - 3$\nc) $6 - 2 ... 2 + 3$", "Bài giải:\na) 8 = 8\nb) 8 > 7\nc) 4 < 5\nĐáp số: a) =; b) >; c) <", "a) =; b) >; c) <", 4, 1.0),
                essay(4, "Một bến xe có 6 chiếc ô tô, sau đó có 3 chiếc rời bến và 2 chiếc khác vào bến. Hỏi lúc này bến xe có bao nhiêu chiếc ô tô?", "Bài giải:\nSố xe ô tô hiện có ở bến là:\n6 - 3 + 2 = 5 (chiếc ô tô)\nĐáp số: 5 chiếc ô tô", "5 chiếc ô tô", 5, 1.5),
                essay(5, "Từ 3 số 3, 5, 8 hãy viết 2 phép tính cộng và 2 phép tính trừ thích hợp.", "Bài giải:\nCác phép tính là:\n3 + 5 = 8\n5 + 3 = 8\n8 - 3 = 5\n8 - 5 = 3\nĐáp số: 4 phép tính đúng", "3+5=8, 5+3=8, 8-3=5, 8-5=3", 5, 2.0),
                essay(6, "Tìm số thích hợp điền vào dấu ?: $1 + 2 + 3 + ? = 10$", "Bài giải:\nTa có: 1 + 2 + 3 = 6.\nSố cần tìm là: 10 - 6 = 4.\nĐáp số: 4", "4", 4, 2.0)
            ]

        elif l_num == 9: # Khối lập phương, khối hộp chữ nhật
            return [
                mc(1, "Hộp sữa tươi giấy em thường uống có dạng khối gì?", ["Khối hộp chữ nhật", "Khối lập phương", "Khối tròn", "Khối trụ"], 0, "Dạng khối hộp chữ nhật."),
                mc(2, "Con xúc xắc (xí ngầu) đồ chơi có dạng hình khối gì?", ["Khối lập phương", "Khối hộp chữ nhật", "Khối cầu", "Khối nón"], 0, "Con xúc xắc có 6 mặt vuông bằng nhau là khối lập phương."),
                mc(3, "Khối lập phương có bao nhiêu mặt?", ["6 mặt", "4 mặt", "8 mặt", "5 mặt"], 0, "Khối lập phương có đúng 6 mặt phẳng."),
                mc(4, "Tủ lạnh gia đình em có dạng khối gì?", ["Khối hộp chữ nhật", "Khối lập phương", "Khối tam giác", "Khối tròn"], 0, "Tủ lạnh có dạng khối hộp chữ nhật đứng."),
                mc(5, "Đặc điểm các mặt của khối lập phương là:", ["Đều là hình vuông bằng nhau", "Đều là hình tròn", "Đều là hình chữ nhật dài", "Đều là hình tam giác"], 0, "6 mặt của khối lập phương đều là hình vuông bằng nhau."),
                mc(6, "Bể cá cảnh hình chữ nhật có dạng khối gì?", ["Khối hộp chữ nhật", "Khối lập phương", "Hình tròn", "Hình vuông"], 0, "Dạng khối hộp chữ nhật.")
            ], [
                essay(1, "Kể tên 3 đồ vật trong gia đình hoặc trường học có dạng:\na) Khối hộp chữ nhật\nb) Khối lập phương", "Bài giải:\na) Khối hộp chữ nhật: Hộp bánh, viên gạch xây nhà, bao diêm, hộp phấn.\nb) Khối lập phương: Khối rubik, con xúc xắc, hộp quà vuông.\nĐáp số: Nêu đúng tên đồ vật thực tế", "Nêu đúng đồ vật", 4, 1.0),
                essay(2, "Khối lập phương và khối hộp chữ nhật giống nhau và khác nhau ở điểm nào?", "Bài giải:\n- Giống nhau: Đều có 6 mặt phẳng.\n- Khác nhau: Khối lập phương có 6 mặt đều là hình vuông bằng nhau; Khối hộp chữ nhật có các mặt là hình chữ nhật.\nĐáp số: Nêu đúng điểm giống và khác", "Giống có 6 mặt; khác hình vuông / chữ nhật", 4, 1.0),
                essay(3, "Bạn An dùng 4 khối gỗ lập phương nhỏ để xếp thành một khối chữ nhật dài. Hỏi khối chữ nhật đó gồm mấy khối lập phương nhỏ?", "Bài giải:\nKhối chữ nhật dài đó gồm 4 khối lập phương nhỏ ghép lại.\nĐáp số: 4 khối lập phương nhỏ", "4 khối", 4, 1.0),
                essay(4, "Một hộp quà hình lập phương có tất cả bao nhiêu đỉnh và bao nhiêu cạnh?", "Bài giải:\nHộp quà hình lập phương có 8 đỉnh và 12 cạnh.\nĐáp số: 8 đỉnh và 12 cạnh", "8 đỉnh, 12 cạnh", 5, 1.5),
                essay(5, "Người ta dán giấy màu vào tất cả các mặt của một con xúc xắc hình lập phương. Hỏi người ta phải dán bao nhiêu mặt giấy màu?", "Bài giải:\nVì hình lập phương có 6 mặt nên cần dán tất cả 6 mặt giấy màu.\nĐáp số: 6 mặt", "6 mặt", 5, 2.0),
                essay(6, "Đếm số khối lập phương nhỏ trong một chồng gồm 2 tầng, mỗi tầng có 3 khối.", "Bài giải:\nSố khối lập phương nhỏ là:\n3 + 3 = 6 (khối)\nĐáp số: 6 khối lập phương nhỏ", "6 khối", 4, 2.0)
            ]

        elif l_num == 10: # Ôn tập học kì 1
            return [
                mc(1, "Số bé nhất có một chữ số là:", ["0", "1", "9", "10"], 0, "Số 0 là số bé nhất có một chữ số."),
                mc(2, "Số lớn nhất có một chữ số là:", ["9", "10", "8", "7"], 0, "Số 9 là số lớn nhất có 1 chữ số."),
                mc(3, "Kết quả của phép tính $4 + 5 - 3$ là:", ["6", "7", "5", "8"], 0, "$4 + 5 = 9; 9 - 3 = 6$."),
                mc(4, "Hình có 4 cạnh bằng nhau là:", ["Hình vuông", "Hình chữ nhật", "Hình tròn", "Hình tam giác"], 0, "Hình vuông có 4 cạnh bằng nhau."),
                mc(5, "Số thích hợp điền vào chỗ chấm: $10 - ... = 7$", ["3", "2", "4", "5"], 0, "$10 - 7 = 3$."),
                mc(6, "Một tuần lễ có mấy ngày?", ["7 ngày", "5 ngày", "6 ngày", "8 ngày"], 0, "Một tuần lễ có 7 ngày.")
            ], [
                essay(1, "Tính nhẩm:\na) $3 + 4 = .....$\nb) $8 - 5 = .....$\nc) $2 + 7 - 4 = .....$\nd) $10 - 6 + 3 = .....$", "Bài giải:\na) 7\nb) 3\nc) 5\nd) 7\nĐáp số: 7, 3, 5, 7", "7, 3, 5, 7", 4, 1.0),
                essay(2, "Điền dấu thích hợp (>, <, =):\na) $5 + 3 ... 9$\nb) $8 - 2 ... 3 + 3$\nc) $10 - 4 ... 7$\nd) $6 + 0 ... 6 - 0$", "Bài giải:\na) 8 < 9\nb) 6 = 6\nc) 6 < 7\nd) 6 = 6\nĐáp số: a) <; b) =; c) <; d) =", "a) <; b) =; c) <; d) =", 4, 1.0),
                essay(3, "Sắp xếp các số 8, 3, 10, 0, 5 theo thứ tự từ bé đến lớn.", "Bài giải:\nThứ tự từ bé đến lớn là: 0, 3, 5, 8, 10.\nĐáp số: 0, 3, 5, 8, 10", "0, 3, 5, 8, 10", 4, 1.0),
                essay(4, "Đàn gà nhà bác An có 6 con gà mái và 3 con gà trống. Hỏi đàn gà nhà bác An có tất cả bao nhiêu con gà?", "Bài giải:\nĐàn gà có tất cả số con là:\n6 + 3 = 9 (con gà)\nĐáp số: 9 con gà", "9 con gà", 5, 1.5),
                essay(5, "Vườn nhà Mai có 10 cây hoa, trong đó có 4 cây hoa hồng, còn lại là hoa cúc. Hỏi vườn nhà Mai có bao nhiêu cây hoa cúc?", "Bài giải:\nSố cây hoa cúc là:\n10 - 4 = 6 (cây hoa cúc)\nĐáp số: 6 cây hoa cúc", "6 cây", 5, 2.0),
                essay(6, "Tìm số x thích hợp biết: $4 + x < 6$ và $x$ là số tự nhiên.", "Bài giải:\nVì 4 + x < 6 nên 4 + x chỉ có thể bằng 4 hoặc bằng 5.\n- Nếu 4 + x = 4 thì x = 0.\n- Nếu 4 + x = 5 thì x = 1.\nVậy x = 0 hoặc x = 1.\nĐáp số: x = 0; x = 1", "x = 0 hoặc x = 1", 4, 2.0)
            ]

        elif l_num in [11, 12, 13, 14]: # Các số trong phạm vi 100
            step = (l_num - 11) * 20 + t_num * 5
            return [
                mc(1, f"Số gồm {2 + t_num} chục và 5 đơn vị viết là:", [f"{2 + t_num}5", f"5{2 + t_num}", f"{2 + t_num}05", "25"], 0, f"Viết là {2 + t_num}5."),
                mc(2, f"Số liền sau của số {29 + t_num} là:", [str(30 + t_num), str(28 + t_num), str(31 + t_num), "29"], 0, f"Liền sau là {30 + t_num}."),
                mc(3, "Số tròn chục liền trước của số 50 là:", ["40", "30", "60", "49"], 0, "Số tròn chục liền trước 50 là 40."),
                mc(4, "Số lớn nhất có hai chữ số là:", ["99", "100", "90", "98"], 0, "Số lớn nhất có 2 chữ số là 99."),
                mc(5, f"So sánh: {40 + t_num} ... {45 + t_num}", ["<", ">", "=", "Không có"], 0, f"{40 + t_num} < {45 + t_num}."),
                mc(6, "Số mười chín được viết là chữ số:", ["19", "91", "109", "9"], 0, "Mười chín viết là 19.")
            ], [
                essay(1, f"Viết các số sau:\na) Ba mươi lăm: ........\nb) Bốn mươi: ........\nc) Tám mươi bảy: ........\nd) Một trăm: ........", "Bài giải:\na) 35\nb) 40\nc) 87\nd) 100\nĐáp số: 35, 40, 87, 100", "35, 40, 87, 100", 4, 1.0),
                essay(2, "Viết số thích hợp vào chỗ chấm:\na) Số liền trước của 60 là ........\nb) Số liền sau của 89 là ........\nc) Số 75 gồm ........ chục và ........ đơn vị", "Bài giải:\na) 59\nb) 90\nc) 7 chục và 5 đơn vị\nĐáp số: a) 59; b) 90; c) 7 chục và 5 đơn vị", "59, 90, 7 chục 5 đơn vị", 4, 1.0),
                essay(3, "Điền dấu (>, <, =):\na) 45 ... 54\nb) 70 ... 69\nc) 82 ... 82\nd) 99 ... 100", "Bài giải:\na) 45 < 54\nb) 70 > 69\nc) 82 = 82\nd) 99 < 100\nĐáp số: a) <; b) >; c) =; d) <", "a) <; b) >; c) =; d) <", 4, 1.0),
                essay(4, "Sắp xếp các số 42, 18, 75, 50, 93 theo thứ tự:\na) Từ bé đến lớn\nb) Từ lớn đến bé", "Bài giải:\na) Từ bé đến lớn: 18, 42, 50, 75, 93\nb) Từ lớn đến bé: 93, 75, 50, 42, 18\nĐáp số: a) 18, 42, 50, 75, 93; b) 93, 75, 50, 42, 18", "a) 18, 42, 50, 75, 93; b) 93, 75, 50, 42, 18", 5, 1.5),
                essay(5, "Lớp 1A có 32 học sinh, lớp 1B có 35 học sinh. Hỏi lớp nào có nhiều học sinh hơn và nhiều hơn bao nhiêu bạn?", "Bài giải:\nVì 35 > 32 nên lớp 1B có nhiều học sinh hơn lớp 1A.\nLớp 1B nhiều hơn lớp 1A số bạn là:\n35 - 32 = 3 (bạn)\nĐáp số: Lớp 1B nhiều hơn 3 bạn", "Lớp 1B nhiều hơn 3 bạn", 5, 2.0),
                essay(6, "Tìm số có hai chữ số, biết chữ số hàng chục là số lớn nhất có 1 chữ số, chữ số hàng đơn vị kém chữ số hàng chục 5 đơn vị.", "Bài giải:\nChữ số lớn nhất có 1 chữ số là 9 nên chữ số hàng chục là 9.\nChữ số hàng đơn vị là: 9 - 5 = 4.\nVậy số cần tìm là 94.\nĐáp số: 94", "94", 4, 2.0)
            ]

        elif l_num in [15, 16]: # Độ dài và xăng-ti-mét (cm)
            len_val = 10 + t_num * 2
            return [
                mc(1, "Xăng-ti-mét được viết tắt là:", ["cm", "m", "dm", "kg"], 0, "Viết tắt là cm."),
                mc(2, f"Đoạn thẳng AB dài {len_val} cm, đoạn thẳng CD dài {len_val + 3} cm. Đoạn thẳng nào dài hơn?", ["Đoạn thẳng CD", "Đoạn thẳng AB", "Bằng nhau", "Không biết"], 0, f"{len_val + 3} cm > {len_val} cm."),
                mc(3, "Độ dài chiếc bút chì của em khoảng bao nhiêu?", ["15 cm", "15 m", "1 cm", "100 cm"], 0, "Bút chì dài khoảng 15 cm."),
                mc(4, f"Tính: ${len_val}\\text{{ cm}} + 5\\text{{ cm}} = $", [f"{len_val + 5} cm", f"{len_val + 5}", "15 cm", "20 cm"], 0, f"{len_val} + 5 = {len_val + 5} cm."),
                mc(5, f"Tính: $18\\text{{ cm}} - 6\\text{{ cm}} = $", ["12 cm", "11 cm", "14 cm", "10 cm"], 0, "18 - 6 = 12 cm."),
                mc(6, "Thước kẻ học sinh thông thường có vạch chia từ số 0 đến số:", ["20 cm", "2 cm", "100 cm", "5 cm"], 0, "Thước kẻ học sinh thường dài 20 cm.")
            ], [
                essay(1, f"Tính:\na) ${len_val}\\text{{ cm}} + 4\\text{{ cm}} = .....$\nb) $19\\text{{ cm}} - 7\\text{{ cm}} = .....$\nc) $12\\text{{ cm}} + 6\\text{{ cm}} - 5\\text{{ cm}} = .....$\nd) $20\\text{{ cm}} - 10\\text{{ cm}} = .....$", f"Bài giải:\na) {len_val + 4} cm\nb) 12 cm\nc) 13 cm\nd) 10 cm\nĐáp số: {len_val + 4} cm, 12 cm, 13 cm, 10 cm", f"{len_val + 4} cm, 12 cm, 13 cm, 10 cm", 4, 1.0),
                essay(2, "Điền số thích hợp vào chỗ chấm:\na) $8\\text{ cm} + ....\\text{ cm} = 15\\text{ cm}$\nb) $....\\text{ cm} - 6\\text{ cm} = 10\\text{ cm}$", "Bài giải:\na) 15 - 8 = 7 cm\nb) 10 + 6 = 16 cm\nĐáp số: a) 7; b) 16", "a) 7; b) 16", 4, 1.0),
                essay(3, "Em hãy nêu cách dùng thước thẳng có vạch chia xăng-ti-mét để đo độ dài chiếc bút sáp màu.", "Bài giải:\n1. Đặt vạch số 0 của thước trùng với một đầu của bút sáp.\n2. Đặt thước thẳng sát dọc theo thân bút sáp.\n3. Nhìn xem đầu kia của bút sáp trùng với vạch số mấy trên thước thì đó chính là độ dài của bút sáp.\nĐáp số: Nêu đúng 3 bước đo chuẩn", "Đúng các bước đo", 4, 1.0),
                essay(4, "Đoạn băng dính màu đỏ dài 14 cm, đoạn băng dính màu xanh dài hơn đoạn băng dính màu đỏ 5 cm. Hỏi đoạn băng dính màu xanh dài bao nhiêu xăng-ti-mét?", "Bài giải:\nĐoạn băng dính màu xanh dài là:\n14 + 5 = 19 (cm)\nĐáp số: 19 cm", "19 cm", 5, 1.5),
                essay(5, "Một sợi dây đồng dài 18 cm, bố cắt bớt đi 8 cm. Hỏi sợi dây đồng còn lại dài bao nhiêu xăng-ti-mét?", "Bài giải:\nSợi dây đồng còn lại dài là:\n18 - 8 = 10 (cm)\nĐáp số: 10 cm", "10 cm", 5, 2.0),
                essay(6, "Cho 3 điểm A, B, C thẳng hàng. Biết đoạn thẳng AB dài 6 cm, đoạn thẳng BC dài 4 cm. Hỏi đoạn thẳng AC dài bao nhiêu xăng-ti-mét?", "Bài giải:\nĐộ dài đoạn thẳng AC là:\n6 + 4 = 10 (cm)\nĐáp số: 10 cm", "10 cm", 4, 2.0)
            ]

        elif l_num in [17, 18]: # Phép cộng, trừ trong phạm vi 100 (không nhớ)
            p_a = 40 + t_num * 5
            p_b = 21 + t_num * 2
            return [
                mc(1, f"Kết quả phép tính ${p_a} + {p_b}$ là:", [str(p_a + p_b), str(p_a + p_b - 1), str(p_a + p_b + 10), "70"], 0, f"{p_a} + {p_b} = {p_a + p_b}."),
                mc(2, f"Kết quả phép tính ${p_a + 20} - 10$ là:", [str(p_a + 10), str(p_a), str(p_a + 20), "50"], 0, f"{p_a + 20} - 10 = {p_a + 10}."),
                mc(3, "Đặt tính rồi tính: $34 + 25 = $", ["59", "69", "49", "58"], 0, "4 + 5 = 9, 3 + 2 = 5, viết 59."),
                mc(4, "Đặt tính rồi tính: $68 - 24 = $", ["44", "42", "54", "34"], 0, "8 - 4 = 4, 6 - 2 = 4, viết 44."),
                mc(5, f"Số thích hợp điền vào chỗ chấm: $52 + ... = 58$", ["6", "5", "7", "8"], 0, "58 - 52 = 6."),
                mc(6, "Điền dấu: $30 + 40 ... 80 - 10$", ["=", ">", "<", "Không có"], 0, "70 = 70.")
            ], [
                essay(1, f"Đặt tính rồi tính:\na) $32 + 25$\nb) $68 - 14$\nc) $43 + 30$\nd) $79 - 45$", "Bài giải:\na) 32 + 25 = 57\nb) 68 - 14 = 54\nc) 43 + 30 = 73\nd) 79 - 45 = 34\nĐáp số: 57, 54, 73, 34", "57, 54, 73, 34", 4, 1.0),
                essay(2, "Tính giá trị biểu thức:\na) $45 + 20 - 15 = .....$\nb) $78 - 30 + 11 = .....$", "Bài giải:\na) 45 + 20 = 65; 65 - 15 = 50\nb) 78 - 30 = 48; 48 + 11 = 59\nĐáp số: a) 50; b) 59", "a) 50; b) 59", 4, 1.0),
                essay(3, "Điền số thích hợp vào chỗ chấm:\na) $42 + .... = 47$\nb) $65 - .... = 61$\nc) $.... + 23 = 55$", "Bài giải:\na) 5\nb) 4\nc) 32\nĐáp số: a) 5; b) 4; c) 32", "a) 5; b) 4; c) 32", 4, 1.0),
                essay(4, "Một trang trại có 45 con bò sữa và 32 con bò thịt. Hỏi trang trại đó có tất cả bao nhiêu con bò?", "Bài giải:\nTrang trại đó có tất cả số con bò là:\n45 + 32 = 77 (con bò)\nĐáp số: 77 con bò", "77 con bò", 5, 1.5),
                essay(5, "Một cửa hàng có 68 chiếc xe đạp, buổi sáng bán được 25 chiếc xe đạp. Hỏi cửa hàng còn lại bao nhiêu chiếc xe đạp?", "Bài giải:\nCửa hàng còn lại số xe đạp là:\n68 - 25 = 43 (chiếc xe đạp)\nĐáp số: 43 chiếc xe đạp", "43 chiếc xe đạp", 5, 2.0),
                essay(6, "Tìm một số biết rằng lấy số đó cộng với 23 thì được kết quả là 58.", "Bài giải:\nSố cần tìm là:\n58 - 23 = 35\nĐáp số: 35", "35", 4, 2.0)
            ]

        elif l_num in [19, 20]: # Đồng hồ, lịch và ngày trong tuần
            hour_val = 7 + t_num
            return [
                mc(1, f"Đồng hồ chỉ kim ngắn vào số {hour_val}, kim dài chỉ đúng số 12. Khi đó là mấy giờ?", [f"{hour_val} giờ đúng", f"{hour_val - 1} giờ", "12 giờ", "6 giờ"], 0, f"Là {hour_val} giờ đúng."),
                mc(2, "Một tuần lễ có mấy ngày?", ["7 ngày", "5 ngày", "6 ngày", "8 ngày"], 0, "Một tuần lễ có 7 ngày."),
                mc(3, "Nếu hôm nay là Thứ Hai thì ngày mai là:", ["Thứ Ba", "Chủ Nhật", "Thứ Tư", "Thứ Bảy"], 0, "Liền sau Thứ Hai là Thứ Ba."),
                mc(4, "Em thường vào lớp học buổi sáng lúc mấy giờ?", ["7 giờ hoặc 8 giờ", "12 giờ trưa", "10 giờ đêm", "3 giờ sáng"], 0, "Buổi sáng học lúc 7 hoặc 8 giờ."),
                mc(5, "Ngày đầu tiên trong tuần lễ em đi học là:", ["Thứ Hai", "Chủ Nhật", "Thứ Bảy", "Thứ Sáu"], 0, "Bắt đầu tuần học là Thứ Hai."),
                mc(6, "Nếu ngày 5 là Thứ Tư thì ngày 6 cùng tháng là Thứ mấy?", ["Thứ Năm", "Thứ Ba", "Thứ Sáu", "Thứ Bảy"], 0, "Ngày 6 liền sau ngày 5 nên là Thứ Năm.")
            ], [
                essay(1, f"Điền giờ thích hợp vào chỗ chấm:\na) Kim ngắn chỉ số 8, kim dài chỉ số 12: ........ giờ\nb) Kim ngắn chỉ số {hour_val}, kim dài chỉ số 12: ........ giờ", f"Bài giải:\na) 8 giờ\nb) {hour_val} giờ\nĐáp số: a) 8 giờ; b) {hour_val} giờ", f"a) 8 giờ; b) {hour_val} giờ", 4, 1.0),
                essay(2, "Viết tên 7 ngày trong một tuần lễ theo đúng thứ tự:", "Bài giải:\nThứ Hai, Thứ Ba, Thứ Tư, Thứ Năm, Thứ Sáu, Thứ Bảy, Chủ Nhật.\nĐáp số: Đúng thứ tự 7 ngày", "Thứ Hai đến Chủ Nhật", 4, 1.0),
                essay(3, "Hôm nay là Thứ Sáu ngày 10.\na) Ngày mai là Thứ mấy, ngày bao nhiêu?\nb) Hôm qua là Thứ mấy, ngày bao nhiêu?", "Bài giải:\na) Ngày mai là Thứ Bảy, ngày 11.\nb) Hôm qua là Thứ Năm, ngày 9.\nĐáp số: a) Thứ Bảy ngày 11; b) Thứ Năm ngày 9", "a) Thứ Bảy 11; b) Thứ Năm 9", 4, 1.0),
                essay(4, "Bạn Nam bắt đầu ngồi vào bàn học lúc 8 giờ tối và học bài xong lúc 9 giờ tối. Hỏi bạn Nam đã học bài trong bao nhiêu giờ?", "Bài giải:\nThời gian bạn Nam học bài là:\n9 - 8 = 1 (giờ)\nĐáp số: 1 giờ", "1 giờ", 5, 1.5),
                essay(5, "Một tuần bạn Lan đi học 5 ngày từ Thứ Hai đến Thứ Sáu, được nghỉ 2 ngày cuối tuần. Hỏi trong 2 tuần bạn Lan đi học mấy ngày và được nghỉ mấy ngày?", "Bài giải:\nTrong 2 tuần bạn Lan đi học số ngày là: 5 + 5 = 10 (ngày).\nSố ngày được nghỉ là: 2 + 2 = 4 (ngày).\nĐáp số: Đi học 10 ngày, nghỉ 4 ngày", "Đi học 10 ngày, nghỉ 4 ngày", 5, 2.0),
                essay(6, "Vẽ kim ngắn và kim dài trên mặt đồng hồ để chỉ thời gian em đi ngủ vào buổi tối (9 giờ đúng).", "Bài giải:\n- Kim ngắn (kim giờ) vẽ chỉ thẳng vào số 9.\n- Kim dài (kim phút) vẽ chỉ thẳng vào số 12.\nĐáp số: Vẽ đúng mặt đồng hồ 9 giờ", "Vẽ kim ngắn chỉ số 9, kim dài chỉ số 12", 4, 2.0)
            ]

        else: # Bài 21 & 22: Ôn tập cuối năm
            return [
                mc(1, "Số tròn chục lớn nhất có hai chữ số là:", ["90", "99", "100", "80"], 0, "Số tròn chục lớn nhất có 2 chữ số là 90."),
                mc(2, "Tính: $56 + 23 = $", ["79", "69", "89", "78"], 0, "56 + 23 = 79."),
                mc(3, "Tính: $87 - 35 = $", ["52", "62", "42", "53"], 0, "87 - 35 = 52."),
                mc(4, "Hình có 3 đỉnh và 3 cạnh là hình:", ["Hình tam giác", "Hình tròn", "Hình chữ nhật", "Hình vuông"], 0, "Hình tam giác."),
                mc(5, "Đoạn thẳng dài 15 cm bớt đi 5 cm còn lại:", ["10 cm", "20 cm", "5 cm", "15 cm"], 0, "15 - 5 = 10 cm."),
                mc(6, "Số liền trước của 100 là:", ["99", "98", "101", "90"], 0, "100 - 1 = 99.")
            ], [
                essay(1, "Đặt tính rồi tính:\na) $42 + 36$\nb) $89 - 45$\nc) $60 + 28$\nd) $95 - 50$", "Bài giải:\na) 78\nb) 44\nc) 88\nd) 45\nĐáp số: 78, 44, 88, 45", "78, 44, 88, 45", 4, 1.0),
                essay(2, "Tính giá trị biểu thức:\na) $35 + 14 - 20 = .....$\nb) $88 - 32 + 13 = .....$", "Bài giải:\na) 35 + 14 = 49; 49 - 20 = 29\nb) 88 - 32 = 56; 56 + 13 = 69\nĐáp số: a) 29; b) 69", "a) 29; b) 69", 4, 1.0),
                essay(3, "Điền dấu (>, <, =):\na) $54 + 12 ... 68$\nb) $79 - 25 ... 50$\nc) $18\\text{ cm} + 2\\text{ cm} ... 20\\text{ cm}$", "Bài giải:\na) 66 < 68\nb) 54 > 50\nc) 20 cm = 20 cm\nĐáp số: a) <; b) >; c) =", "a) <; b) >; c) =", 4, 1.0),
                essay(4, "Một giá sách có 56 quyển truyện thiếu nhi và 31 quyển sách giáo khoa. Hỏi giá sách đó có tất cả bao nhiêu quyển sách truyện?", "Bài giải:\nTổng số quyển sách truyện là:\n56 + 31 = 87 (quyển)\nĐáp số: 87 quyển", "87 quyển", 5, 1.5),
                essay(5, "Đoạn dây thứ nhất dài 45 cm, đoạn dây thứ hai ngắn hơn đoạn dây thứ nhất 12 cm. Hỏi đoạn dây thứ hai dài bao nhiêu xăng-ti-mét?", "Bài giải:\nĐộ dài đoạn dây thứ hai là:\n45 - 12 = 33 (cm)\nĐáp số: 33 cm", "33 cm", 5, 2.0),
                essay(6, "Tìm một số biết rằng lấy số đó trừ đi 34 thì được kết quả là 42.", "Bài giải:\nSố cần tìm là:\n42 + 34 = 76\nĐáp số: 76", "76", 4, 2.0)
            ]

    # Vòng lặp sinh cho các bài từ 6 đến 22
    from toan1_curriculum_def import TOAN1_CURRICULUM
    ch_map = {}
    for ch in TOAN1_CURRICULUM["chapters"]:
        for les in ch["lessons"]:
            ch_map[les["num"]] = (ch["title"], ch["term"], les["name"])

    for l_num in range(6, 23):
        ch_title, term_code, les_name = ch_map.get(l_num, ("Chủ đề bài học", "hk1", f"Bài {l_num}"))
        for t_idx in range(1, 4):
            eid = f"th1_b{l_num}_test{t_idx}"
            p1, p2 = build_p1_p2_for_lesson(l_num, t_idx)
            exams[eid] = {
                "id": eid, "lessonId": f"th1_b{l_num}", "lessonNum": l_num, "testNum": t_idx,
                "title": f"{les_name} - Đề số {t_idx}",
                "topic": ch_title, "chapter": ch_title.split(":")[0],
                "grade": "1", "term": term_code, "duration": "35 phút", "points": 10.0,
                "part1": p1,
                "part2": p2
            }

    print(f"-> Đã tạo thành công {len(exams)} đề kiểm tra theo bài cho TOÁN 1 (22 bài x 3 đề = 66 đề)")
    return exams

if __name__ == "__main__":
    exs = get_toan1_lesson_exams()
    print("Mẫu 1 đề:")
    k = list(exs.keys())[0]
    print(k, exs[k]["title"])
    print("P1 len:", len(exs[k]["part1"]), "P2 len:", len(exs[k]["part2"]))
