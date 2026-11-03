# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 10: PHÂN SỐ - PHẦN 1 (BÀI 44 ĐẾN BÀI 47) - TOÁN 4 KNTT
Gồm 4 bài học, mỗi bài có 3 đề kiểm tra độc lập:
- Bài 44: Khái niệm phân số (th4_b44_test1, th4_b44_test2, th4_b44_test3)
- Bài 45: Phân số và phép chia số tự nhiên (th4_b45_test1, th4_b45_test2, th4_b45_test3)
- Bài 46: Phân số bằng nhau (th4_b46_test1, th4_b46_test2, th4_b46_test3)
- Bài 47: Rút gọn phân số (th4_b47_test1, th4_b47_test2, th4_b47_test3)
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

def get_ch10_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 44: KHÁI NIỆM PHÂN SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b44_test1"] = {
        "id": "th4_b44_test1",
        "lessonId": "th4_b44",
        "lessonNum": 44,
        "testNum": 1,
        "title": "Bài 44: Khái niệm phân số - Đề số 1",
        "topic": "Khái niệm phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số năm phần chín được viết là:", ["5/9", "9/5", "5,9", "9,5"], 0, "Năm phần chín có tử số là 5, mẫu số là 9, viết là 5/9.", "Nhận biết"),
            make_mc(2, "Trong phân số 7/15, mẫu số là:", ["15", "7", "22", "8"], 0, "Mẫu số là số tự nhiên viết dưới gạch ngang, ở đây là 15.", "Nhận biết"),
            make_mc(3, "Một hình vuông chia thành 4 phần bằng nhau, tô màu 3 phần. Phân số chỉ phần đã tô màu là:", ["3/4", "4/3", "1/4", "3/1"], 0, "Tô màu 3 phần trong 4 phần bằng nhau nên phân số là 3/4.", "Thông hiểu"),
            make_mc(4, "Trong phân số 8/13, tử số cho biết:", ["Số phần bằng nhau được lấy ra", "Tổng số phần bằng nhau", "Số phần còn lại", "Tên của phân số"], 0, "Tử số cho biết số phần bằng nhau được lấy ra.", "Nhận biết"),
            make_mc(5, "Mẫu số của một phân số phải là:", ["Số tự nhiên khác 0", "Số tự nhiên bất kì", "Số lớn hơn 10", "Số chẵn"], 0, "Mẫu số của một phân số phải là số tự nhiên khác 0.", "Nhận biết"),
            make_mc(6, "Một tấm bánh pizza được chia đều thành 8 miếng. Bạn Nam đã ăn 3 miếng. Phân số chỉ số phần bánh pizza Nam đã ăn là:", ["3/8", "5/8", "8/3", "3/5"], 0, "Nam ăn 3 trong tổng số 8 miếng, phân số là 3/8.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Viết và đọc các phân số sau:\na) Tử số là 3, mẫu số là 7.\nb) Tử số là 11, mẫu số là 25.", "a) Viết là 3/7; đọc là: ba phần bảy.\nb) Viết là 11/25; đọc là: mười một phần hai mươi lăm.\nĐáp số: a) 3/7; b) 11/25.", "a) 3/7; b) 11/25", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết phân số thích hợp vào chỗ chấm:\na) Có 5 quả cam chia đều cho 8 bạn. Mỗi bạn nhận được ... quả cam.\nb) Một sợi dây dài 3 m được cắt thành 5 đoạn bằng nhau. Mỗi đoạn dài ... m.", "a) Mỗi bạn nhận được: 5/8 quả cam.\nb) Mỗi đoạn dài: 3/5 m.\nĐáp số: a) 5/8; b) 3/5.", "a) 5/8; b) 3/5", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Một hình chữ nhật được chia thành 10 ô vuông bằng nhau, người ta tô màu 7 ô vuông.\na) Viết phân số chỉ phần đã tô màu của hình chữ nhật.\nb) Viết phân số chỉ phần chưa tô màu của hình chữ nhật.", "a) Phân số chỉ phần đã tô màu là: 7/10.\nb) Số ô chưa tô màu là: 10 - 7 = 3 (ô).\nPhân số chỉ phần chưa tô màu là: 3/10.\nĐáp số: a) 7/10; b) 3/10.", "a) 7/10; b) 3/10", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một giá sách có 45 quyển sách, trong đó có 20 quyển sách truyện và 25 quyển sách giáo khoa.\na) Viết phân số chỉ số sách truyện so với tổng số sách trên giá.\nb) Viết phân số chỉ số sách giáo khoa so với tổng số sách trên giá.", "a) Phân số chỉ số sách truyện là: 20/45.\nb) Phân số chỉ số sách giáo khoa là: 25/45.\nĐáp số: a) 20/45; b) 25/45.", "a) 20/45; b) 25/45", 5, 1.5, "Vận dụng"),
            make_essay(5, "Lớp 4A có 35 học sinh, trong đó có 18 học sinh nữ.\na) Viết phân số chỉ số học sinh nữ so với tổng số học sinh của lớp 4A.\nb) Viết phân số chỉ số học sinh nam so với tổng số học sinh của lớp 4A.", "a) Phân số chỉ số học sinh nữ là: 18/35.\nb) Số học sinh nam là:\n35 - 18 = 17 (học sinh)\nPhân số chỉ số học sinh nam là: 17/35.\nĐáp số: a) 18/35; b) 17/35.", "a) 18/35; b) 17/35", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm các phân số có mẫu số là 9 và tử số là các số lẻ bé hơn 8.", "Các số lẻ bé hơn 8 là: 1, 3, 5, 7.\nCác phân số cần tìm có mẫu số là 9 là:\n1/9 ; 3/9 ; 5/9 ; 7/9.\nĐáp số: 1/9 ; 3/9 ; 5/9 ; 7/9.", "1/9 ; 3/9 ; 5/9 ; 7/9", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b44_test2"] = {
        "id": "th4_b44_test2",
        "lessonId": "th4_b44",
        "lessonNum": 44,
        "testNum": 2,
        "title": "Bài 44: Khái niệm phân số - Đề số 2",
        "topic": "Khái niệm phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số bảy phần mười hai được viết là:", ["7/12", "12/7", "7,12", "12,7"], 0, "Viết là 7/12.", "Nhận biết"),
            make_mc(2, "Tử số của phân số 9/16 là:", ["9", "16", "25", "7"], 0, "Tử số là số viết trên dấu gạch ngang: 9.", "Nhận biết"),
            make_mc(3, "Một hình lục giác đều được chia làm 6 tam giác bằng nhau, tô màu 4 tam giác. Phân số chỉ phần đã tô màu là:", ["4/6", "6/4", "2/6", "4/2"], 0, "Tô màu 4 phần trong 6 phần: 4/6.", "Thông hiểu"),
            make_mc(4, "Trong phân số a/b, điều kiện của b là:", ["b là số tự nhiên khác 0", "b có thể bằng 0", "b lớn hơn a", "b là số chẵn"], 0, "Mẫu số luôn phải khác 0.", "Nhận biết"),
            make_mc(5, "Một tuần lễ có 7 ngày, trong đó bạn Lan đi học 5 ngày. Phân số chỉ số ngày Lan đi học trong tuần là:", ["5/7", "7/5", "2/7", "5/2"], 0, "Lan đi học 5 ngày trong 7 ngày: 5/7.", "Thông hiểu"),
            make_mc(6, "Phân số chỉ phần chưa tô màu của một hình tròn chia 8 phần tô 3 phần là:", ["5/8", "3/8", "8/5", "8/3"], 0, "Số phần chưa tô màu là 8 - 3 = 5 phần: 5/8.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Viết và đọc các phân số sau:\na) Tử số là 4, mẫu số là 9.\nb) Tử số là 17, mẫu số là 30.", "a) Viết là 4/9; đọc là: bốn phần chín.\nb) Viết là 17/30; đọc là: mười bảy phần ba mươi.\nĐáp số: a) 4/9; b) 17/30.", "a) 4/9; b) 17/30", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết phân số thích hợp vào chỗ chấm:\na) Chia đều 4 lít nước vào 7 chai. Mỗi chai có ... lít nước.\nb) Rót đều 2 cái bánh cho 3 bạn. Mỗi bạn được ... cái bánh.", "a) Mỗi chai có: 4/7 lít nước.\nb) Mỗi bạn được: 2/3 cái bánh.\nĐáp số: a) 4/7; b) 2/3.", "a) 4/7; b) 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Một mảnh đất được chia làm 12 luống hoa bằng nhau, trong đó có 5 luống trồng hoa hồng, 4 luống trồng hoa cúc, còn lại trồng hoa ly.\na) Viết phân số chỉ phần đất trồng hoa hồng.\nb) Viết phân số chỉ phần đất trồng hoa ly.", "a) Phân số chỉ phần đất trồng hoa hồng là: 5/12.\nb) Số luống trồng hoa ly là:\n12 - (5 + 4) = 3 (luống)\nPhân số chỉ phần đất trồng hoa ly là: 3/12.\nĐáp số: a) 5/12; b) 3/12.", "a) 5/12; b) 3/12", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một hộp bút có 24 chiếc bút gồm 10 bút bi xanh, 8 bút bi đỏ và 6 bút bi đen.\na) Viết phân số chỉ số bút bi xanh so với tổng số bút trong hộp.\nb) Viết phân số chỉ số bút bi đỏ so với tổng số bút trong hộp.", "a) Phân số chỉ số bút bi xanh là: 10/24.\nb) Phân số chỉ số bút bi đỏ là: 8/24.\nĐáp số: a) 10/24; b) 8/24.", "a) 10/24; b) 8/24", 5, 1.5, "Vận dụng"),
            make_essay(5, "Đội văn nghệ của trường có 30 học sinh, trong đó có 12 học sinh nam.\na) Viết phân số chỉ số học sinh nam trong đội văn nghệ.\nb) Viết phân số chỉ số học sinh nữ trong đội văn nghệ.", "a) Phân số chỉ số học sinh nam là: 12/30.\nb) Số học sinh nữ là:\n30 - 12 = 18 (học sinh)\nPhân số chỉ số học sinh nữ là: 18/30.\nĐáp số: a) 12/30; b) 18/30.", "a) 12/30; b) 18/30", 5, 1.5, "Vận dụng"),
            make_essay(6, "Viết tất cả các phân số có tổng của tử số và mẫu số bằng 6 (với tử số và mẫu số là các số tự nhiên khác 0).", "Các cặp số tự nhiên khác 0 có tổng bằng 6 là: (1, 5); (2, 4); (3, 3); (4, 2); (5, 1).\nCác phân số tương ứng là:\n1/5 ; 2/4 ; 3/3 ; 4/2 ; 5/1.\nĐáp số: 1/5 ; 2/4 ; 3/3 ; 4/2 ; 5/1.", "1/5 ; 2/4 ; 3/3 ; 4/2 ; 5/1", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b44_test3"] = {
        "id": "th4_b44_test3",
        "lessonId": "th4_b44",
        "lessonNum": 44,
        "testNum": 3,
        "title": "Bài 44: Khái niệm phân số - Đề số 3",
        "topic": "Khái niệm phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số tám phần mười lăm được viết là:", ["8/15", "15/8", "8,15", "15,8"], 0, "Viết là 8/15.", "Nhận biết"),
            make_mc(2, "Trong phân số 13/20, mẫu số cho biết:", ["Số phần bằng nhau mà đơn vị được chia ra", "Số phần được lấy đi", "Hiệu giữa tử và mẫu", "Tích giữa tử và mẫu"], 0, "Mẫu số cho biết đơn vị được chia thành bao nhiêu phần bằng nhau.", "Nhận biết"),
            make_mc(3, "Một thanh sô-cô-la có 10 ô vuông nhỏ, An ăn mất 4 ô. Phân số chỉ phần sô-cô-la An đã ăn là:", ["4/10", "6/10", "10/4", "4/6"], 0, "An ăn 4 trong 10 ô vuông: 4/10.", "Thông hiểu"),
            make_mc(4, "Một ngày có 24 giờ. Thời gian làm việc của bố là 8 giờ. Phân số chỉ thời gian làm việc của bố trong ngày là:", ["8/24", "16/24", "24/8", "8/16"], 0, "8/24 (hay 1/3 ngày).", "Thông hiểu"),
            make_mc(5, "Tử số của phân số 23/35 là:", ["23", "35", "58", "12"], 0, "Tử số là 23.", "Nhận biết"),
            make_mc(6, "Một rổ bóng có 15 quả, trong đó có 7 quả bóng vàng. Phân số chỉ số bóng vàng trong rổ là:", ["7/15", "8/15", "15/7", "7/8"], 0, "7 quả bóng vàng trên 15 quả: 7/15.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Viết và đọc các phân số sau:\na) Tử số là 5, mẫu số là 11.\nb) Tử số là 19, mẫu số là 35.", "a) Viết là 5/11; đọc là: năm phần mười một.\nb) Viết là 19/35; đọc là: mười chín phần ba mươi lăm.\nĐáp số: a) 5/11; b) 19/35.", "a) 5/11; b) 19/35", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết phân số thích hợp vào chỗ chấm:\na) Có 7 kg đường chia đều vào 10 túi. Mỗi túi có ... kg đường.\nb) Đoạn dây dài 5 m cắt thành 8 phần bằng nhau. Mỗi phần dài ... m.", "a) Mỗi túi có: 7/10 kg đường.\nb) Mỗi phần dài: 5/8 m.\nĐáp số: a) 7/10; b) 5/8.", "a) 7/10; b) 5/8", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Một tấm bìa hình vuông được chia thành 16 ô vuông nhỏ bằng nhau, trong đó tô màu đỏ 6 ô, tô màu xanh 5 ô, phần còn lại tô màu vàng.\na) Viết phân số chỉ phần tô màu đỏ.\nb) Viết phân số chỉ phần tô màu vàng.", "a) Phân số chỉ phần tô màu đỏ là: 6/16.\nb) Số ô tô màu vàng là:\n16 - (6 + 5) = 5 (ô)\nPhân số chỉ phần tô màu vàng là: 5/16.\nĐáp số: a) 6/16; b) 5/16.", "a) 6/16; b) 5/16", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại có 40 con vật nuôi gồm 15 con bò sữa, 18 con lợn và 7 con cừu.\na) Viết phân số chỉ số con bò sữa so với tổng số con vật nuôi.\nb) Viết phân số chỉ số con lợn so với tổng số con vật nuôi.", "a) Phân số chỉ số con bò sữa là: 15/40.\nb) Phân số chỉ số con lợn là: 18/40.\nĐáp số: a) 15/40; b) 18/40.", "a) 15/40; b) 18/40", 5, 1.5, "Vận dụng"),
            make_essay(5, "Khối lớp 4 có 120 học sinh, trong đó có 65 bạn tham gia câu lạc bộ bơi lội.\na) Viết phân số chỉ số học sinh tham gia câu lạc bộ bơi lội.\nb) Viết phân số chỉ số học sinh không tham gia câu lạc bộ bơi lội.", "a) Phân số chỉ học sinh tham gia là: 65/120.\nb) Số học sinh không tham gia bơi lội là:\n120 - 65 = 55 (học sinh)\nPhân số chỉ học sinh không tham gia là: 55/120.\nĐáp số: a) 65/120; b) 55/120.", "a) 65/120; b) 55/120", 5, 1.5, "Vận dụng"),
            make_essay(6, "Viết tất cả các phân số có mẫu số là 8 và tử số là các số tự nhiên lớn hơn 0 và nhỏ hơn mẫu số.", "Tử số là các số tự nhiên: 1, 2, 3, 4, 5, 6, 7.\nCác phân số tương ứng có mẫu số là 8 là:\n1/8 ; 2/8 ; 3/8 ; 4/8 ; 5/8 ; 6/8 ; 7/8.\nĐáp số: 1/8 ; 2/8 ; 3/8 ; 4/8 ; 5/8 ; 6/8 ; 7/8.", "1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 45: PHÂN SỐ VÀ PHÉP CHIA SỐ TỰ NHIÊN (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b45_test1"] = {
        "id": "th4_b45_test1",
        "lessonId": "th4_b45",
        "lessonNum": 45,
        "testNum": 1,
        "title": "Bài 45: Phân số và phép chia số tự nhiên - Đề số 1",
        "topic": "Phân số và phép chia số tự nhiên",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Thương của phép chia 3 : 5 được viết dưới dạng phân số là:", ["3/5", "5/3", "3,5", "5,3"], 0, "Thương của a : b viết là a/b, nên 3 : 5 = 3/5.", "Nhận biết"),
            make_mc(2, "Số tự nhiên 8 được viết dưới dạng phân số có mẫu số là 1 là:", ["8/1", "1/8", "8/8", "18/1"], 0, "Mọi số tự nhiên đều viết được dưới dạng phân số có mẫu số bằng 1: 8 = 8/1.", "Nhận biết"),
            make_mc(3, "Trong các phân số sau, phân số nào có giá trị lớn hơn 1?", ["7/4", "4/7", "4/4", "3/5"], 0, "Tử số lớn hơn mẫu số (7 > 4) nên 7/4 > 1.", "Thông hiểu"),
            make_mc(4, "Cho các phân số sau, phân số có giá trị nhỏ hơn 1 là:", ["5/6", "6/5", "6/6", "9/8"], 0, "Tử số bé hơn mẫu số (5 < 6) nên 5/6 < 1.", "Thông hiểu"),
            make_mc(5, "Phân số nào dưới đây bằng 1?", ["9/9", "9/8", "8/9", "1/9"], 0, "Tử số bằng mẫu số thì phân số bằng 1: 9/9 = 1.", "Nhận biết"),
            make_mc(6, "Kết quả của phép chia 12 : 4 viết dưới dạng phân số là:", ["12/4", "4/12", "1/4", "3/12"], 0, "12 : 4 = 12/4 (và 12/4 = 3).", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Viết thương của mỗi phép chia sau dưới dạng phân số:\na) 4 : 7\nb) 9 : 8\nc) 5 : 5\nd) 15 : 1", "a) 4 : 7 = 4/7\nb) 9 : 8 = 9/8\nc) 5 : 5 = 5/5\nd) 15 : 1 = 15/1\nĐáp số: a) 4/7; b) 9/8; c) 5/5; d) 15/1.", "a) 4/7; b) 9/8; c) 5/5; d) 15/1", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết các số tự nhiên sau dưới dạng phân số có mẫu số là 1:\na) 6\nb) 12\nc) 25\nd) 100", "a) 6 = 6/1\nb) 12 = 12/1\nc) 25 = 25/1\nd) 100 = 100/1\nĐáp số: a) 6/1; b) 12/1; c) 25/1; d) 100/1.", "a) 6/1; b) 12/1; c) 25/1; d) 100/1", 4, 1.0, "Thông hiểu"),
            make_essay(3, "So sánh các phân số sau với 1:\na) 4/5 và 1\nb) 7/6 và 1\nc) 8/8 và 1\nd) 12/15 và 1", "a) 4/5 < 1 (vì 4 < 5)\nb) 7/6 > 1 (vì 7 > 6)\nc) 8/8 = 1 (vì 8 = 8)\nd) 12/15 < 1 (vì 12 < 15)\nĐáp số: a) 4/5 < 1; b) 7/6 > 1; c) 8/8 = 1; d) 12/15 < 1.", "a) < 1; b) > 1; c) = 1; d) < 1", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Có 3 cái bánh nướng như nhau chia đều cho 4 bạn. Hỏi mỗi bạn nhận được bao nhiêu phần của cái bánh?", "Mỗi bạn nhận được số phần cái bánh là:\n3 : 4 = 3/4 (cái bánh)\nĐáp số: 3/4 cái bánh.", "3/4 cái bánh", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một bình nước chứa 5 lít nước được rót đều vào 6 cốc. Hỏi mỗi cốc chứa bao nhiêu phần của lít nước?", "Mỗi cốc chứa số phần lít nước là:\n5 : 6 = 5/6 (lít nước)\nĐáp số: 5/6 lít nước.", "5/6 lít nước", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên a biết: a/7 < 1 và a/7 > 5/7.", "Ta có:\na/7 < 1 suy ra a < 7.\na/7 > 5/7 suy ra a > 5.\nSố tự nhiên a thỏa mãn 5 < a < 7 là a = 6.\nĐáp số: a = 6.", "a = 6", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b45_test2"] = {
        "id": "th4_b45_test2",
        "lessonId": "th4_b45",
        "lessonNum": 45,
        "testNum": 2,
        "title": "Bài 45: Phân số và phép chia số tự nhiên - Đề số 2",
        "topic": "Phân số và phép chia số tự nhiên",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Thương của phép chia 7 : 9 viết dưới dạng phân số là:", ["7/9", "9/7", "7,9", "9,7"], 0, "7 : 9 = 7/9.", "Nhận biết"),
            make_mc(2, "Số 15 viết dưới dạng phân số có mẫu số bằng 1 là:", ["15/1", "1/15", "15/15", "30/2"], 0, "15 = 15/1.", "Nhận biết"),
            make_mc(3, "Trong các phân số 3/4, 5/6, 7/7, 8/5, phân số lớn hơn 1 là:", ["8/5", "3/4", "5/6", "7/7"], 0, "8/5 có tử số lớn hơn mẫu số (8 > 5) nên 8/5 > 1.", "Thông hiểu"),
            make_mc(4, "Trong các phân số 11/10, 9/8, 4/5, 7/6, phân số bé hơn 1 là:", ["4/5", "11/10", "9/8", "7/6"], 0, "4/5 có tử số bé hơn mẫu số nên bé hơn 1.", "Thông hiểu"),
            make_mc(5, "Có 4 quả dưa hấu chia đều cho 5 người. Mỗi người nhận được số quả dưa hấu là:", ["4/5 quả", "5/4 quả", "1 quả", "4 quả"], 0, "4 : 5 = 4/5 (quả dưa).", "Thông hiểu"),
            make_mc(6, "Phân số 16/4 có giá trị là số tự nhiên nào?", ["4", "16", "2", "8"], 0, "16 : 4 = 4.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Viết các thương sau dưới dạng phân số:\na) 6 : 11\nb) 13 : 10\nc) 7 : 7\nd) 20 : 1", "a) 6 : 11 = 6/11\nb) 13 : 10 = 13/10\nc) 7 : 7 = 7/7\nd) 20 : 1 = 20/1\nĐáp số: a) 6/11; b) 13/10; c) 7/7; d) 20/1.", "a) 6/11; b) 13/10; c) 7/7; d) 20/1", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Điền dấu thích hợp (<, >, =) vào ô trống:\na) 9/11 ... 1\nb) 14/13 ... 1\nc) 25/25 ... 1\nd) 6/7 ... 7/6", "a) 9/11 < 1 (vì 9 < 11)\nb) 14/13 > 1 (vì 14 > 13)\nc) 25/25 = 1 (vì 25 = 25)\nd) 6/7 < 1 và 7/6 > 1 nên 6/7 < 7/6\nĐáp số: a) <; b) >; c) =; d) <.", "a) <; b) >; c) =; d) <", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Viết mỗi số tự nhiên sau thành phân số có mẫu số là 3:\na) 2\nb) 5\nc) 8\nd) 10", "a) 2 = (2 x 3)/3 = 6/3\nb) 5 = (5 x 3)/3 = 15/3\nc) 8 = (8 x 3)/3 = 24/3\nd) 10 = (10 x 3)/3 = 30/3\nĐáp số: a) 6/3; b) 15/3; c) 24/3; d) 30/3.", "a) 6/3; b) 15/3; c) 24/3; d) 30/3", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Có 7 mét vải may được 8 cái áo như nhau. Hỏi may mỗi cái áo hết bao nhiêu mét vải?", "May mỗi cái áo hết số mét vải là:\n7 : 8 = 7/8 (m)\nĐáp số: 7/8 m vải.", "7/8 m", 4, 1.5, "Vận dụng"),
            make_essay(5, "Rót đều 9 lít sữa vào 10 chai như nhau. Hỏi mỗi chai chứa bao nhiêu phần của lít sữa?", "Mỗi chai chứa số phần lít sữa là:\n9 : 10 = 9/10 (lít sữa)\nĐáp số: 9/10 lít sữa.", "9/10 lít sữa", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tìm các số tự nhiên x sao cho: 3 < x/4 < 5.", "Ta có 3 = 12/4 và 5 = 20/4.\nBất đẳng thức trở thành: 12/4 < x/4 < 20/4.\nSuy ra 12 < x < 20.\nVậy x nhận các giá trị: 13, 14, 15, 16, 17, 18, 19.\nĐáp số: x thuộc {13, 14, 15, 16, 17, 18, 19}.", "x = 13, 14, 15, 16, 17, 18, 19", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b45_test3"] = {
        "id": "th4_b45_test3",
        "lessonId": "th4_b45",
        "lessonNum": 45,
        "testNum": 3,
        "title": "Bài 45: Phân số và phép chia số tự nhiên - Đề số 3",
        "topic": "Phân số và phép chia số tự nhiên",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Thương của phép chia 5 : 8 là:", ["5/8", "8/5", "5,8", "8,5"], 0, "5 : 8 = 5/8.", "Nhận biết"),
            make_mc(2, "Phân số nào sau đây có giá trị bằng 1?", ["18/18", "18/17", "17/18", "1/18"], 0, "18/18 = 1.", "Nhận biết"),
            make_mc(3, "Trong các phân số 2/3, 5/4, 6/7, 9/10, phân số lớn hơn 1 là:", ["5/4", "2/3", "6/7", "9/10"], 0, "5/4 có tử số lớn hơn mẫu số nên 5/4 > 1.", "Thông hiểu"),
            make_mc(4, "Có 2 lít mật ong chia đều vào 5 lọ. Mỗi lọ chứa số lít mật ong là:", ["2/5 lít", "5/2 lít", "2 lít", "5 lít"], 0, "2 : 5 = 2/5 (lít).", "Thông hiểu"),
            make_mc(5, "Số tự nhiên 7 viết thành phân số có mẫu số là 4 là:", ["28/4", "7/4", "4/7", "21/4"], 0, "7 = (7 x 4)/4 = 28/4.", "Thông hiểu"),
            make_mc(6, "Phân số nào sau đây bé hơn 1?", ["14/15", "15/14", "15/15", "16/15"], 0, "14 < 15 nên 14/15 < 1.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Viết các thương sau dưới dạng phân số:\na) 5 : 9\nb) 11 : 7\nc) 8 : 8\nd) 16 : 1", "a) 5 : 9 = 5/9\nb) 11 : 7 = 11/7\nc) 8 : 8 = 8/8\nd) 16 : 1 = 16/1\nĐáp số: a) 5/9; b) 11/7; c) 8/8; d) 16/1.", "a) 5/9; b) 11/7; c) 8/8; d) 16/1", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Xếp các phân số sau thành ba nhóm: phân số bé hơn 1, phân số bằng 1, phân số lớn hơn 1:\n3/5 ; 7/4 ; 6/6 ; 8/9 ; 11/10 ; 12/12", "Nhóm 1 (bé hơn 1): 3/5 ; 8/9 (vì tử số bé hơn mẫu số).\nNhóm 2 (bằng 1): 6/6 ; 12/12 (vì tử số bằng mẫu số).\nNhóm 3 (lớn hơn 1): 7/4 ; 11/10 (vì tử số lớn hơn mẫu số).\nĐáp số: Bé hơn 1: 3/5, 8/9; Bằng 1: 6/6, 12/12; Lớn hơn 1: 7/4, 11/10.", "Bé hơn 1: 3/5, 8/9; Bằng 1: 6/6, 12/12; Lớn hơn 1: 7/4, 11/10", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Viết mỗi số tự nhiên sau dưới dạng phân số có mẫu số là 5:\na) 1\nb) 3\nc) 6\nd) 8", "a) 1 = 5/5\nb) 3 = 15/5\nc) 6 = 30/5\nd) 8 = 40/5\nĐáp số: a) 5/5; b) 15/5; c) 30/5; d) 40/5.", "a) 5/5; b) 15/5; c) 30/5; d) 40/5", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Có 4 quả dưa hấu chia đều cho 7 bạn. Hỏi mỗi bạn nhận được bao nhiêu phần của quả dưa hấu?", "Mỗi bạn nhận được số phần quả dưa hấu là:\n4 : 7 = 4/7 (quả dưa hấu)\nĐáp số: 4/7 quả dưa hấu.", "4/7 quả dưa hấu", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một sợi dây dài 9 m được chia đều thành 11 đoạn ngắn. Hỏi mỗi đoạn ngắn dài bao nhiêu mét?", "Mỗi đoạn ngắn dài số mét là:\n9 : 11 = 9/11 (m)\nĐáp số: 9/11 m.", "9/11 m", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên a lớn nhất sao cho: a/8 < 1.", "Để a/8 < 1 thì a < 8.\nSố tự nhiên a lớn nhất nhỏ hơn 8 là a = 7.\nĐáp số: a = 7.", "a = 7", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 46: PHÂN SỐ BẰNG NHAU (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b46_test1"] = {
        "id": "th4_b46_test1",
        "lessonId": "th4_b46",
        "lessonNum": 46,
        "testNum": 1,
        "title": "Bài 46: Phân số bằng nhau - Đề số 1",
        "topic": "Phân số bằng nhau",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khi nhân cả tử số và mẫu số của một phân số với cùng một số tự nhiên khác 0 thì:", ["Được một phân số bằng phân số đã cho", "Phân số tăng lên", "Phân số giảm đi", "Phân số bằng 1"], 0, "Tính chất cơ bản: Nhân cả tử và mẫu với cùng số khác 0 thì được phân số bằng phân số đã cho.", "Nhận biết"),
            make_mc(2, "Phân số nào dưới đây bằng phân số 2/3?", ["4/6", "4/9", "3/2", "6/8"], 0, "2/3 = (2 x 2)/(3 x 2) = 4/6.", "Thông hiểu"),
            make_mc(3, "Số thích hợp điền vào dấu ? để 3/5 = ?/15 là:", ["9", "6", "12", "15"], 0, "15 : 5 = 3 nên ? = 3 x 3 = 9.", "Thông hiểu"),
            make_mc(4, "Số thích hợp điền vào dấu ? để 18/24 = 3/? là:", ["4", "6", "8", "3"], 0, "18 : 6 = 3 nên ? = 24 : 6 = 4.", "Thông hiểu"),
            make_mc(5, "Phân số bằng phân số 5/7 là:", ["15/21", "10/15", "20/25", "15/28"], 0, "5/7 = (5 x 3)/(7 x 3) = 15/21.", "Thông hiểu"),
            make_mc(6, "Cặp phân số nào sau đây bằng nhau?", ["2/5 và 6/15", "3/4 và 6/9", "1/2 và 3/5", "4/7 và 8/12"], 0, "2/5 = (2 x 3)/(5 x 3) = 6/15.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) 2/5 = .../10\nb) 3/4 = 12/...\nc) 15/20 = 3/...\nd) 24/36 = .../6", "a) 2/5 = (2 x 2)/(5 x 2) = 4/10\nb) 3/4 = (3 x 4)/(4 x 4) = 12/16\nc) 15/20 = (15 : 5)/(20 : 5) = 3/4\nd) 24/36 = (24 : 6)/(36 : 6) = 4/6\nĐáp số: a) 4; b) 16; c) 4; d) 4.", "a) 4; b) 16; c) 4; d) 4", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết 3 phân số bằng mỗi phân số sau:\na) 2/3\nb) 5/8", "a) 2/3 = 4/6 = 6/9 = 8/12\nb) 5/8 = 10/16 = 15/24 = 20/32\nĐáp số: a) 4/6, 6/9, 8/12; b) 10/16, 15/24, 20/32.", "a) 4/6, 6/9, 8/12; b) 10/16, 15/24, 20/32", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x biết:\na) x/6 = 15/18\nb) 4/x = 20/35", "a) 15/18 = (15 : 3)/(18 : 3) = 5/6 => x = 5\nb) 20/35 = (20 : 5)/(35 : 5) = 4/7 => x = 7\nĐáp số: a) x = 5; b) x = 7.", "a) x = 5; b) x = 7", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một mảnh vườn được chia làm 15 phần bằng nhau, người ta đã trồng rau trên 9 phần. Hỏi có thể nói người ta đã trồng rau trên bao nhiêu phần mảnh vườn nếu coi mảnh vườn được chia thành 5 phần bằng nhau?", "Phân số chỉ số phần mảnh vườn trồng rau là 9/15.\nTa có: 9/15 = (9 : 3)/(15 : 3) = 3/5.\nVậy nếu coi mảnh vườn chia làm 5 phần bằng nhau thì người ta đã trồng rau trên 3 phần.\nĐáp số: 3 phần.", "3 phần", 4, 1.5, "Vận dụng"),
            make_essay(5, "Cho phân số 16/24. Hãy tìm một phân số bằng phân số đã cho sao cho:\na) Tử số là 2\nb) Mẫu số là 18", "a) Rút gọn: 16/24 = 2/3 (chia cả tử và mẫu cho 8). Phân số cần tìm là 2/3.\nb) 16/24 = 2/3 = (2 x 6)/(3 x 6) = 12/18. Phân số cần tìm là 12/18.\nĐáp số: a) 2/3; b) 12/18.", "a) 2/3; b) 12/18", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên a biết: (a + 2)/15 = 2/5.", "Ta có:\n2/5 = (2 x 3)/(5 x 3) = 6/15\nDo đó: (a + 2)/15 = 6/15\nSuy ra: a + 2 = 6\na = 6 - 2 = 4\nĐáp số: a = 4.", "a = 4", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b46_test2"] = {
        "id": "th4_b46_test2",
        "lessonId": "th4_b46",
        "lessonNum": 46,
        "testNum": 2,
        "title": "Bài 46: Phân số bằng nhau - Đề số 2",
        "topic": "Phân số bằng nhau",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số nào bằng phân số 3/4?", ["9/12", "6/9", "9/15", "12/20"], 0, "3/4 = (3 x 3)/(4 x 3) = 9/12.", "Thông hiểu"),
            make_mc(2, "Số thích hợp điền vào ô trống để 4/7 = .../28 là:", ["16", "12", "20", "14"], 0, "28 : 7 = 4, 4 x 4 = 16.", "Thông hiểu"),
            make_mc(3, "Số thích hợp để 20/30 = 2/... là:", ["3", "4", "5", "6"], 0, "20 : 10 = 2, 30 : 10 = 3.", "Thông hiểu"),
            make_mc(4, "Khi chia cả tử số và mẫu số của một phân số cho cùng một số tự nhiên lớn hơn 1 thì:", ["Được phân số bằng phân số đã cho", "Phân số nhỏ đi", "Phân số lớn hơn", "Không chia được"], 0, "Được phân số bằng phân số đã cho.", "Nhận biết"),
            make_mc(5, "Cặp phân số nào dưới đây KHÔNG bằng nhau?", ["3/5 và 9/15", "2/7 và 6/21", "4/9 và 8/18", "1/3 và 3/6"], 3, "1/3 = 2/6 khác 3/6.", "Thông hiểu"),
            make_mc(6, "Tìm y biết y/18 = 2/3:", ["12", "6", "9", "8"], 0, "18 : 3 = 6, y = 2 x 6 = 12.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Điền số thích hợp vào chỗ chấm:\na) 1/3 = .../9\nb) 5/6 = 25/...\nc) 14/21 = 2/...\nd) 30/45 = .../3", "a) 1/3 = 3/9\nb) 5/6 = 25/30\nc) 14/21 = 2/3\nd) 30/45 = 2/3\nĐáp số: a) 3; b) 30; c) 3; d) 2.", "a) 3; b) 30; c) 3; d) 2", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết 3 phân số bằng mỗi phân số sau:\na) 3/5\nb) 4/7", "a) 3/5 = 6/10 = 9/15 = 12/20\nb) 4/7 = 8/14 = 12/21 = 16/28\nĐáp số: a) 6/10, 9/15, 12/20; b) 8/14, 12/21, 16/28.", "a) 6/10, 9/15, 12/20; b) 8/14, 12/21, 16/28", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x biết:\na) x/8 = 15/24\nb) 6/x = 18/30", "a) 15/24 = (15 : 3)/(24 : 3) = 5/8 => x = 5\nb) 18/30 = (18 : 3)/(30 : 3) = 6/10 => x = 10\nĐáp số: a) x = 5; b) x = 10.", "a) x = 5; b) x = 10", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một hộp bánh có 20 chiếc bánh. Bạn Hoa ăn 8 chiếc bánh. Bạn Mai ăn 2/5 số bánh của hộp đó. Hỏi hai bạn có ăn số lượng bánh bằng nhau không? Vì sao?", "Phân số chỉ số bánh Hoa ăn là: 8/20.\nRút gọn phân số 8/20:\n8/20 = (8 : 4)/(20 : 4) = 2/5.\nVì 8/20 = 2/5 nên số bánh Hoa ăn bằng số bánh Mai ăn.\nĐáp số: Hai bạn ăn số bánh bằng nhau.", "Bằng nhau", 5, 1.5, "Vận dụng"),
            make_essay(5, "Cho phân số 18/27. Hãy tìm một phân số bằng phân số đã cho sao cho:\na) Tử số là 2\nb) Mẫu số là 15", "a) 18/27 = (18 : 9)/(27 : 9) = 2/3. Phân số cần tìm là 2/3.\nb) 2/3 = (2 x 5)/(3 x 5) = 10/15. Phân số cần tìm là 10/15.\nĐáp số: a) 2/3; b) 10/15.", "a) 2/3; b) 10/15", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên m biết: 5/(m - 1) = 15/24.", "Rút gọn phân số 15/24:\n15/24 = (15 : 3)/(24 : 3) = 5/8\nTa có: 5/(m - 1) = 5/8\nSuy ra: m - 1 = 8\nm = 8 + 1 = 9\nĐáp số: m = 9.", "m = 9", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b46_test3"] = {
        "id": "th4_b46_test3",
        "lessonId": "th4_b46",
        "lessonNum": 46,
        "testNum": 3,
        "title": "Bài 46: Phân số bằng nhau - Đề số 3",
        "topic": "Phân số bằng nhau",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số bằng phân số 4/5 là:", ["12/15", "8/15", "16/25", "12/20"], 0, "4/5 = (4 x 3)/(5 x 3) = 12/15.", "Thông hiểu"),
            make_mc(2, "Số thích hợp điền vào dấu ? để 5/8 = 20/? là:", ["32", "24", "40", "16"], 0, "20 : 5 = 4, 8 x 4 = 32.", "Thông hiểu"),
            make_mc(3, "Số thích hợp để 36/48 = ?/4 là:", ["3", "4", "2", "6"], 0, "48 : 4 = 12, 36 : 12 = 3.", "Thông hiểu"),
            make_mc(4, "Phân số 15/25 bằng phân số nào sau đây?", ["3/5", "5/3", "3/4", "1/5"], 0, "15/25 = 3/5.", "Thông hiểu"),
            make_mc(5, "Tìm x biết 7/9 = x/27:", ["21", "14", "28", "18"], 0, "27 : 9 = 3, x = 7 x 3 = 21.", "Thông hiểu"),
            make_mc(6, "Cặp phân số bằng nhau là:", ["5/6 và 25/30", "2/3 và 4/9", "3/7 và 6/21", "4/5 và 8/15"], 0, "5/6 = 25/30.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Điền số thích hợp vào chỗ chấm:\na) 2/7 = .../21\nb) 4/9 = 24/...\nc) 18/30 = 3/...\nd) 28/49 = .../7", "a) 2/7 = 6/21\nb) 4/9 = 24/54\nc) 18/30 = 3/5\nd) 28/49 = 4/7\nĐáp số: a) 6; b) 54; c) 5; d) 4.", "a) 6; b) 54; c) 5; d) 4", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết 3 phân số bằng mỗi phân số sau:\na) 5/9\nb) 3/8", "a) 5/9 = 10/18 = 15/27 = 20/36\nb) 3/8 = 6/16 = 9/24 = 12/32\nĐáp số: a) 10/18, 15/27, 20/36; b) 6/16, 9/24, 12/32.", "a) 10/18, 15/27, 20/36; b) 6/16, 9/24, 12/32", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Tìm x biết:\na) x/9 = 20/36\nb) 5/x = 15/42", "a) 20/36 = (20 : 4)/(36 : 4) = 5/9 => x = 5\nb) 15/42 = (15 : 3)/(42 : 3) = 5/14 => x = 14\nĐáp số: a) x = 5; b) x = 14.", "a) x = 5; b) x = 14", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một giá sách có 36 quyển sách. Bạn Bình đã đọc 12 quyển sách. Hỏi bạn Bình đã đọc mấy phần số sách trên giá? (viết kết quả dưới dạng phân số có tử số là 1).", "Phân số chỉ số sách Bình đã đọc là: 12/36.\nRút gọn để có tử số là 1:\n12/36 = (12 : 12)/(36 : 12) = 1/3.\nVậy Bình đã đọc 1/3 số sách trên giá.\nĐáp số: 1/3 số sách.", "1/3 số sách", 4, 1.5, "Vận dụng"),
            make_essay(5, "Cho phân số 20/35. Hãy tìm một phân số bằng phân số đã cho sao cho:\na) Tử số là 4\nb) Mẫu số là 21", "a) 20/35 = (20 : 5)/(35 : 5) = 4/7. Phân số cần tìm là 4/7.\nb) 4/7 = (4 x 3)/(7 x 3) = 12/21. Phân số cần tìm là 12/21.\nĐáp số: a) 4/7; b) 12/21.", "a) 4/7; b) 12/21", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên y biết: 9/(y + 3) = 3/7.", "Ta có:\n3/7 = (3 x 3)/(7 x 3) = 9/21\nDo đó: 9/(y + 3) = 9/21\nSuy ra: y + 3 = 21\ny = 21 - 3 = 18\nĐáp số: y = 18.", "y = 18", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # BÀI 47: RÚT GỌN PHÂN SỐ (TEST 1, 2, 3)
    # =========================================================================

    exams["th4_b47_test1"] = {
        "id": "th4_b47_test1",
        "lessonId": "th4_b47",
        "lessonNum": 47,
        "testNum": 1,
        "title": "Bài 47: Rút gọn phân số - Đề số 1",
        "topic": "Rút gọn phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Thế nào là rút gọn phân số?", ["Làm cho phân số có tử số và mẫu số bé đi mà phân số mới vẫn bằng phân số đã cho", "Lấy tử số chia cho mẫu số", "Làm cho mẫu số bằng 1", "Nhân cả tử số và mẫu số với 2"], 0, "Rút gọn phân số là làm cho tử số và mẫu số bé đi mà giá trị không đổi.", "Nhận biết"),
            make_mc(2, "Rút gọn phân số 12/18 về phân số tối giản ta được:", ["2/3", "6/9", "4/6", "3/4"], 0, "12 : 6 = 2, 18 : 6 = 3. Tối giản là 2/3.", "Thông hiểu"),
            make_mc(3, "Trong các phân số sau, phân số nào là phân số tối giản?", ["5/7", "6/9", "10/15", "8/12"], 0, "5/7 không thể rút gọn được nữa nên là phân số tối giản.", "Nhận biết"),
            make_mc(4, "Rút gọn phân số 25/35 ta được:", ["5/7", "5/6", "5/8", "7/5"], 0, "25 : 5 = 5, 35 : 5 = 7. Kết quả 5/7.", "Thông hiểu"),
            make_mc(5, "Phân số 18/45 rút gọn thành phân số tối giản là:", ["2/5", "6/15", "9/20", "3/5"], 0, "18 : 9 = 2, 45 : 9 = 5. Kết quả 2/5.", "Thông hiểu"),
            make_mc(6, "Phân số nào sau đây CHƯA tối giản?", ["14/21", "3/7", "8/9", "11/13"], 0, "14/21 có thể rút gọn chia cho 7 được 2/3.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) 14/28\nb) 20/35\nc) 24/36\nd) 45/60", "a) 14/28 = (14 : 14)/(28 : 14) = 1/2\nb) 20/35 = (20 : 5)/(35 : 5) = 4/7\nc) 24/36 = (24 : 12)/(36 : 12) = 2/3\nd) 45/60 = (45 : 15)/(60 : 15) = 3/4\nĐáp số: a) 1/2; b) 4/7; c) 2/3; d) 3/4.", "a) 1/2; b) 4/7; c) 2/3; d) 3/4", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Trong các phân số sau: 4/9 ; 15/25 ; 7/12 ; 18/27 ; 13/15.\na) Những phân số nào là phân số tối giản?\nb) Hãy rút gọn các phân số chưa tối giản.", "a) Các phân số tối giản là: 4/9 ; 7/12 ; 13/15.\nb) Rút gọn các phân số chưa tối giản:\n15/25 = 3/5\n18/27 = 2/3\nĐáp số: a) 4/9, 7/12, 13/15; b) 3/5 và 2/3.", "a) 4/9, 7/12, 13/15; b) 3/5 và 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Quy đồng tử số các phân số bằng cách rút gọn về cùng tử số:\na) Rút gọn 12/16 và 15/20\nb) So sánh hai phân số trên.", "a) 12/16 = (12 : 4)/(16 : 4) = 3/4\n15/20 = (15 : 5)/(20 : 5) = 3/4\nb) Vì cùng rút gọn bằng 3/4 nên 12/16 = 15/20.\nĐáp số: a) Cùng bằng 3/4; b) 12/16 = 15/20.", "a) 3/4; b) 12/16 = 15/20", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một cửa hàng có 60 m vải, trong ngày đã bán được 45 m vải.\na) Viết phân số chỉ số phần mét vải cửa hàng đã bán.\nb) Rút gọn phân số đó thành phân số tối giản.", "a) Phân số chỉ số vải đã bán là: 45/60.\nb) Rút gọn: 45/60 = (45 : 15)/(60 : 15) = 3/4.\nĐáp số: a) 45/60; b) 3/4.", "a) 45/60; b) 3/4", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một lớp học có 36 học sinh, trong đó có 24 học sinh đạt danh hiệu học sinh xuất sắc.\na) Viết phân số chỉ số học sinh xuất sắc của lớp học đó.\nb) Rút gọn phân số đó về dạng tối giản.", "a) Phân số chỉ học sinh xuất sắc là: 24/36.\nb) Rút gọn: 24/36 = (24 : 12)/(36 : 12) = 2/3.\nĐáp số: a) 24/36; b) 2/3.", "a) 24/36; b) 2/3", 4, 1.5, "Vận dụng"),
            make_essay(6, "Rút gọn biểu thức sau thành phân số tối giản:\nA = (2 x 3 x 5 x 7) / (3 x 5 x 7 x 11)", "Chia cả tử số và mẫu số cho các thừa số chung là 3, 5, 7:\nA = 2/11\nĐáp số: 2/11.", "2/11", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b47_test2"] = {
        "id": "th4_b47_test2",
        "lessonId": "th4_b47",
        "lessonNum": 47,
        "testNum": 2,
        "title": "Bài 47: Rút gọn phân số - Đề số 2",
        "topic": "Rút gọn phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Rút gọn phân số 15/20 về tối giản ta được:", ["3/4", "3/5", "5/4", "1/2"], 0, "15 : 5 = 3, 20 : 5 = 4. Kết quả 3/4.", "Thông hiểu"),
            make_mc(2, "Phân số tối giản là phân số:", ["Có tử số và mẫu số không cùng chia hết cho số tự nhiên nào lớn hơn 1", "Có tử số bằng 1", "Có mẫu số bằng 1", "Có tử số bé hơn mẫu số"], 0, "Định nghĩa phân số tối giản.", "Nhận biết"),
            make_mc(3, "Rút gọn phân số 28/42 ta được phân số tối giản là:", ["2/3", "4/6", "14/21", "7/10"], 0, "28 : 14 = 2, 42 : 14 = 3. Kết quả 2/3.", "Thông hiểu"),
            make_mc(4, "Trong các phân số 6/8, 9/12, 12/16, phân số tối giản của chúng là:", ["3/4", "1/2", "2/3", "4/5"], 0, "Cả 3 phân số đều rút gọn về 3/4.", "Thông hiểu"),
            make_mc(5, "Rút gọn phân số 32/48 về tối giản được:", ["2/3", "4/6", "16/24", "8/12"], 0, "32 : 16 = 2, 48 : 16 = 3. Kết quả 2/3.", "Thông hiểu"),
            make_mc(6, "Phân số nào dưới đây là phân số tối giản?", ["8/15", "9/15", "10/15", "12/15"], 0, "8 và 15 không cùng chia hết cho số nào lớn hơn 1 nên 8/15 tối giản.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) 16/24\nb) 25/40\nc) 36/54\nd) 42/70", "a) 16/24 = (16 : 8)/(24 : 8) = 2/3\nb) 25/40 = (25 : 5)/(40 : 5) = 5/8\nc) 36/54 = (36 : 18)/(54 : 18) = 2/3\nd) 42/70 = (42 : 14)/(70 : 14) = 3/5\nĐáp số: a) 2/3; b) 5/8; c) 2/3; d) 3/5.", "a) 2/3; b) 5/8; c) 2/3; d) 3/5", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Cho các phân số: 5/11 ; 12/18 ; 7/9 ; 21/28 ; 15/16.\na) Chỉ ra các phân số tối giản.\nb) Rút gọn các phân số chưa tối giản.", "a) Các phân số tối giản là: 5/11 ; 7/9 ; 15/16.\nb) Rút gọn:\n12/18 = 2/3\n21/28 = 3/4\nĐáp số: a) 5/11, 7/9, 15/16; b) 2/3 và 3/4.", "a) 5/11, 7/9, 15/16; b) 2/3 và 3/4", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Rút gọn rồi so sánh hai phân số:\na) 18/24 và 25/30\nb) 14/21 và 10/15", "a) 18/24 = 3/4; 25/30 = 5/6. Quy đồng: 3/4 = 9/12; 5/6 = 10/12. Vì 9/12 < 10/12 nên 18/24 < 25/30.\nb) 14/21 = 2/3; 10/15 = 2/3. Vậy 14/21 = 10/15.\nĐáp số: a) 18/24 < 25/30; b) 14/21 = 10/15.", "a) 18/24 < 25/30; b) 14/21 = 10/15", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một giá sách có 50 quyển sách, trong đó có 35 quyển truyện tranh.\na) Viết phân số chỉ số truyện tranh trên giá sách.\nb) Rút gọn phân số đó về dạng tối giản.", "a) Phân số chỉ số truyện tranh là: 35/50.\nb) Rút gọn: 35/50 = (35 : 5)/(50 : 5) = 7/10.\nĐáp số: a) 35/50; b) 7/10.", "a) 35/50; b) 7/10", 4, 1.5, "Vận dụng"),
            make_essay(5, "Đoàn vận động viên có 48 người, trong đó có 32 nam.\na) Viết phân số chỉ số vận động viên nam so với cả đoàn.\nb) Rút gọn phân số đó thành phân số tối giản.", "a) Phân số chỉ số vận động viên nam là: 32/48.\nb) Rút gọn: 32/48 = (32 : 16)/(48 : 16) = 2/3.\nĐáp số: a) 32/48; b) 2/3.", "a) 32/48; b) 2/3", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh giá trị biểu thức:\nB = (4 x 7 x 9) / (8 x 7 x 18)", "Rút gọn các thừa số giống nhau:\n4/8 = 1/2; 7/7 = 1; 9/18 = 1/2.\nB = (1 x 1 x 1) / (2 x 1 x 2) = 1/4\nĐáp số: 1/4.", "1/4", 4, 1.0, "Vận dụng cao")
        ]
    }

    exams["th4_b47_test3"] = {
        "id": "th4_b47_test3",
        "lessonId": "th4_b47",
        "lessonNum": 47,
        "testNum": 3,
        "title": "Bài 47: Rút gọn phân số - Đề số 3",
        "topic": "Rút gọn phân số",
        "chapter": "Chủ đề 10: Phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Rút gọn phân số 24/32 về tối giản ta được:", ["3/4", "6/8", "12/16", "4/5"], 0, "24 : 8 = 3, 32 : 8 = 4. Kết quả 3/4.", "Thông hiểu"),
            make_mc(2, "Tìm phân số tối giản trong các phân số sau:", ["11/17", "12/18", "15/20", "14/21"], 0, "11/17 là phân số tối giản.", "Nhận biết"),
            make_mc(3, "Rút gọn phân số 35/49 về tối giản ta được:", ["5/7", "7/5", "5/8", "6/7"], 0, "35 : 7 = 5, 49 : 7 = 7. Kết quả 5/7.", "Thông hiểu"),
            make_mc(4, "Phân số 40/100 rút gọn về phân số tối giản là:", ["2/5", "4/10", "20/50", "1/2"], 0, "40 : 20 = 2, 100 : 20 = 5. Kết quả 2/5.", "Thông hiểu"),
            make_mc(5, "Rút gọn phân số 18/54 ta được:", ["1/3", "2/6", "3/9", "1/4"], 0, "18 : 18 = 1, 54 : 18 = 3. Kết quả 1/3.", "Thông hiểu"),
            make_mc(6, "Phân số nào bằng phân số 3/5 sau khi rút gọn?", ["18/30", "12/25", "15/20", "9/20"], 0, "18/30 chia cả tử và mẫu cho 6 được 3/5.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) 18/27\nb) 30/45\nc) 40/64\nd) 55/77", "a) 18/27 = (18 : 9)/(27 : 9) = 2/3\nb) 30/45 = (30 : 15)/(45 : 15) = 2/3\nc) 40/64 = (40 : 8)/(64 : 8) = 5/8\nd) 55/77 = (55 : 11)/(77 : 11) = 5/7\nĐáp số: a) 2/3; b) 2/3; c) 5/8; d) 5/7.", "a) 2/3; b) 2/3; c) 5/8; d) 5/7", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Trong các phân số sau: 7/13 ; 24/36 ; 9/14 ; 35/42 ; 17/19.\na) Tìm các phân số tối giản.\nb) Rút gọn các phân số chưa tối giản về tối giản.", "a) Các phân số tối giản là: 7/13 ; 9/14 ; 17/19.\nb) Rút gọn:\n24/36 = 2/3\n35/42 = 5/6\nĐáp số: a) 7/13, 9/14, 17/19; b) 2/3 và 5/6.", "a) 7/13, 9/14, 17/19; b) 2/3 và 5/6", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Rút gọn rồi so sánh hai phân số:\na) 20/25 và 24/30\nb) 12/18 và 16/24", "a) 20/25 = 4/5; 24/30 = 4/5. Vậy 20/25 = 24/30.\nb) 12/18 = 2/3; 16/24 = 2/3. Vậy 12/18 = 16/24.\nĐáp số: a) 20/25 = 24/30; b) 12/18 = 16/24.", "a) = ; b) =", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại có 80 con gia cầm, trong đó có 48 con vịt.\na) Viết phân số chỉ số con vịt so với tổng số gia cầm.\nb) Rút gọn phân số đó thành phân số tối giản.", "a) Phân số chỉ số con vịt là: 48/80.\nb) Rút gọn: 48/80 = (48 : 16)/(80 : 16) = 3/5.\nĐáp số: a) 48/80; b) 3/5.", "a) 48/80; b) 3/5", 4, 1.5, "Vận dụng"),
            make_essay(5, "Một giờ có 60 phút. Bạn An dành 40 phút để tự học Toán.\na) Viết phân số chỉ thời gian học Toán của An trong một giờ.\nb) Rút gọn phân số đó thành phân số tối giản.", "a) Phân số chỉ thời gian học Toán là: 40/60.\nb) Rút gọn: 40/60 = (40 : 20)/(60 : 20) = 2/3.\nĐáp số: a) 40/60; b) 2/3 giờ.", "a) 40/60; b) 2/3 giờ", 4, 1.5, "Vận dụng"),
            make_essay(6, "Tính nhanh giá trị biểu thức:\nC = (5 x 6 x 8 x 9) / (10 x 12 x 16 x 3)", "Tách và rút gọn:\n5/10 = 1/2; 6/12 = 1/2; 8/16 = 1/2; 9/3 = 3/1.\nC = (1 x 1 x 1 x 3) / (2 x 2 x 2 x 1) = 3/8\nĐáp số: 3/8.", "3/8", 4, 1.0, "Vận dụng cao")
        ]
    }

    return exams
