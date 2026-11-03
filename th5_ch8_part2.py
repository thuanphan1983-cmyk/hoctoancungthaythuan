# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 8 (PHẦN 2): THỂ TÍCH HÌNH HỘP CHỮ NHẬT, HÌNH LẬP PHƯƠNG, HÌNH TRỤ - LUYỆN TẬP CHUNG
Gồm Bài 41, 42, 43, 44 (12 đề kiểm tra: test1, test2, test3):
- Bài 41: Thể tích hình hộp chữ nhật (th5_b41_test1, th5_b41_test2, th5_b41_test3)
- Bài 42: Thể tích hình lập phương (th5_b42_test1, th5_b42_test2, th5_b42_test3)
- Bài 43: Giới thiệu hình trụ (th5_b43_test1, th5_b43_test2, th5_b43_test3)
- Bài 44: Luyện tập chung Chủ đề 8 (th5_b44_test1, th5_b44_test2, th5_b44_test3)
"""

def make_mc(qid, question, options, correct, explanation):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question, solution, answer, lineCount=4, points=1.0):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    return {
        "id": qid,
        "question": p_text,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_ch8_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 41: THỂ TÍCH HÌNH HỘP CHỮ NHẬT
    # =========================================================================

    # --- Bài 41 - Đề 1 ---
    exams["th5_b41_test1"] = {
        "id": "th5_b41_test1",
        "lessonId": "th5_b41",
        "lessonNum": 41,
        "testNum": 1,
        "title": "Bài 41: Thể tích hình hộp chữ nhật - Đề số 1",
        "topic": "Thể tích hình hộp chữ nhật",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tính thể tích của hình hộp chữ nhật có ba kích thước $a, b, c$ (cùng đơn vị đo) là:", ["$V = a \\times b \\times c$", "$V = (a + b) \\times 2 \\times c$", "$V = a + b + c$", "$V = a \\times b + c$"], 0, "$V = a \\times b \\times c$."),
            make_mc(2, "Một hình hộp chữ nhật có chiều dài $8\\text{ cm}$, chiều rộng $5\\text{ cm}$, chiều cao $6\\text{ cm}$. Thể tích của nó là:", ["$120\\text{ cm}^3$", "$240\\text{ cm}^3$", "$190\\text{ cm}^3$", "$360\\text{ cm}^3$"], 1, "$V = 8 \\times 5 \\times 6 = 240\\text{ cm}^3$."),
            make_mc(3, "Một bể nước có diện tích đáy là $2,5\\text{ m}^2$ và chiều cao là $1,2\\text{ m}$. Thể tích của bể là:", ["$2,8\\text{ m}^3$", "$3\\text{ m}^3$", "$3,5\\text{ m}^3$", "$4\\text{ m}^3$"], 1, "$V = 2,5 \\times 1,2 = 3\\text{ m}^3$."),
            make_mc(4, "Một khối gỗ hình hộp chữ nhật có thể tích $180\\text{ dm}^3$, diện tích đáy là $30\\text{ dm}^2$. Chiều cao của khối gỗ là:", ["5 dm", "6 dm", "7 dm", "8 dm"], 1, "$h = 180 : 30 = 6\\text{ dm}$."),
            make_mc(5, "Đổi: $0,4\\text{ m} = \\dots\\text{ cm}$:", ["4", "40", "400", "0,04"], 1, "$0,4\\text{ m} = 40\\text{ cm}$."),
            make_mc(6, "Một hộp sữa hình chữ nhật có kích thước $6\\text{ cm} \\times 4\\text{ cm} \\times 10\\text{ cm}$. Dung tích của hộp sữa là:", ["240 ml", "240 lít", "24 ml", "2400 ml"], 0, "$6 \\times 4 \\times 10 = 240\\text{ cm}^3 = 240\\text{ ml}$.")
        ],
        "part2": [
            make_essay(1, "Tính thể tích của hình hộp chữ nhật có:\na) Chiều dài $12\\text{ cm}$, chiều rộng $8\\text{ cm}$, chiều cao $5\\text{ cm}$.\nb) Chiều dài $2,5\\text{ m}$, chiều rộng $1,6\\text{ m}$, chiều cao $1,2\\text{ m}$.", "a) $V = 12 \\times 8 \\times 5 = 480\\text{ (cm}^3)$\nb) $V = 2,5 \\times 1,6 \\times 1,2 = 4,8\\text{ (m}^3)$", "a) 480 cm³; b) 4,8 m³", 4, 1.0),
            make_essay(2, "Một hình hộp chữ nhật có thể tích $360\\text{ cm}^3$, chiều dài $10\\text{ cm}$ và chiều rộng $6\\text{ cm}$. Tính chiều cao của hình hộp chữ nhật đó.", "Diện tích đáy là: $10 \\times 6 = 60\\text{ (cm}^2)$.\nChiều cao của hình hộp chữ nhật là:\n$360 : 60 = 6\\text{ (cm)}$\nĐáp số: 6 cm.", "6 cm", 4, 1.0),
            make_essay(3, "Một chiếc bể cá bằng kính có dạng hình hộp chữ nhật có chiều dài $80\\text{ cm}$, chiều rộng $40\\text{ cm}$ và chiều cao $50\\text{ cm}$. Tính thể tích của bể cá theo đơn vị lít.", "Đổi: $80\\text{ cm} = 8\\text{ dm}$; $40\\text{ cm} = 4\\text{ dm}$; $50\\text{ cm} = 5\\text{ dm}$.\nThể tích của bể cá là:\n$8 \\times 4 \\times 5 = 160\\text{ (dm}^3) = 160\\text{ (lít)}$\nĐáp số: 160 lít.", "160 lít", 4, 1.0),
            make_essay(4, "Một bể nước dạng hình hộp chữ nhật có các kích thước trong lòng bể: chiều dài $2\\text{ m}$, chiều rộng $1,5\\text{ m}$ và chiều cao $1,2\\text{ m}$.\na) Tính thể tích nước khi bể chứa đầy.\nb) Hiện tại lượng nước trong bể chiếm $70\\%$ thể tích bể. Hỏi trong bể có bao nhiêu lít nước?", "Bài giải:\na) Thể tích của bể nước là:\n$2 \\times 1,5 \\times 1,2 = 3,6\\text{ (m}^3)$\nĐổi: $3,6\\text{ m}^3 = 3600\\text{ dm}^3 = 3600\\text{ lít}$.\nb) Lượng nước hiện có trong bể là:\n$3600 \\times 70 : 100 = 2520\\text{ (lít)}$\nĐáp số:\na) $3,6\\text{ m}^3$;\nb) 2520 lít.", "a) 3,6 m³; b) 2520 lít", 5, 1.5),
            make_essay(5, "Một cái hố dạng hình hộp chữ nhật sâu $1,5\\text{ m}$, đáy hố có chiều dài $3\\text{ m}$ và chiều rộng $2\\text{ m}$.\na) Tính thể tích đất phải đào lên để tạo thành chiếc hố đó.\nb) Người ta dùng xe rùa mỗi chuyến chở được $0,15\\text{ m}^3$ đất. Hỏi cần chở ít nhất bao nhiêu chuyến để hết số đất đã đào?", "Bài giải:\na) Thể tích đất phải đào lên là:\n$3 \\times 2 \\times 1,5 = 9\\text{ (m}^3)$\nb) Số chuyến xe rùa cần chở là:\n$9 : 0,15 = 60\\text{ (chuyến)}$\nĐáp số:\na) $9\\text{ m}^3$;\nb) 60 chuyến.", "a) 9 m³; b) 60 chuyến", 5, 1.5),
            make_essay(6, "Một hình hộp chữ nhật có thể tích là $V$. Nếu gấp chiều dài lên 2 lần, gấp chiều rộng lên 3 lần và giữ nguyên chiều cao thì thể tích của hình hộp chữ nhật mới gấp mấy lần thể tích ban đầu?", "Bài giải:\nThể tích ban đầu là: $V_1 = a \\times b \\times c$.\nThể tích mới là:\n$V_2 = (a \\times 2) \\times (b \\times 3) \\times c = (a \\times b \\times c) \\times 6 = 6 \\times V_1$.\nVậy thể tích mới gấp 6 lần thể tích ban đầu.\nĐáp số: 6 lần.", "6 lần", 5, 1.0)
        ]
    }

    # --- Bài 41 - Đề 2 ---
    exams["th5_b41_test2"] = {
        "id": "th5_b41_test2",
        "lessonId": "th5_b41",
        "lessonNum": 41,
        "testNum": 2,
        "title": "Bài 41: Thể tích hình hộp chữ nhật - Đề số 2",
        "topic": "Thể tích hình hộp chữ nhật",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình hộp chữ nhật có kích thước $7\\text{ dm}, 4\\text{ dm}, 3\\text{ dm}$. Thể tích của nó là:", ["$84\\text{ dm}^3$", "$68\\text{ dm}^3$", "$56\\text{ dm}^3$", "$98\\text{ dm}^3$"], 0, "$7 \\times 4 \\times 3 = 84\\text{ dm}^3$."),
            make_mc(2, "Muốn tính thể tích hình hộp chữ nhật, ta có thể lấy diện tích đáy nhân với:", ["Chiều dài", "Chiều rộng", "Chiều cao (cùng đơn vị đo)", "Chu vi đáy"], 2, "Quy tắc: $V = S_{đáy} \\times h$."),
            make_mc(3, "Một bể nước có thể tích $4,8\\text{ m}^3$, chiều cao $1,5\\text{ m}$. Diện tích đáy của bể là:", ["$3\\text{ m}^2$", "$3,2\\text{ m}^2$", "$3,5\\text{ m}^2$", "$2,8\\text{ m}^2$"], 1, "$S_{đáy} = 4,8 : 1,5 = 3,2\\text{ m}^2$."),
            make_mc(4, "Một hộp quà hình hộp chữ nhật có kích thước $15\\text{ cm} \\times 10\\text{ cm} \\times 8\\text{ cm}$. Thể tích hộp quà là:", ["$1200\\text{ cm}^3$", "$1500\\text{ cm}^3$", "$800\\text{ cm}^3$", "$600\\text{ cm}^3$"], 0, "$15 \\times 10 \\times 8 = 1200\\text{ cm}^3$."),
            make_mc(5, "Đổi: $1,2\\text{ m} = \\dots\\text{ dm}$:", ["12", "120", "0,12", "1200"], 0, "$1,2\\text{ m} = 12\\text{ dm}$."),
            make_mc(6, "Một khối đá hình hộp chữ nhật có thể tích $0,6\\text{ m}^3$. Khối đá đó bằng bao nhiêu đề-xi-mét khối?", ["$6\\text{ dm}^3$", "$60\\text{ dm}^3$", "$600\\text{ dm}^3$", "$6000\\text{ dm}^3$"], 2, "$0,6 \\times 1000 = 600\\text{ dm}^3$.")
        ],
        "part2": [
            make_essay(1, "Tính thể tích của hình hộp chữ nhật có:\na) Chiều dài $9\\text{ dm}$, chiều rộng $6\\text{ dm}$, chiều cao $4\\text{ dm}$.\nb) Chiều dài $1,5\\text{ m}$, chiều rộng $0,8\\text{ m}$, chiều cao $0,5\\text{ m}$.", "a) $V = 9 \\times 6 \\times 4 = 216\\text{ (dm}^3)$\nb) $V = 1,5 \\times 0,8 \\times 0,5 = 0,6\\text{ (m}^3)$", "a) 216 dm³; b) 0,6 m³", 4, 1.0),
            make_essay(2, "Một hình hộp chữ nhật có thể tích $280\\text{ dm}^3$, diện tích đáy là $35\\text{ dm}^2$. Tính chiều cao của hình hộp chữ nhật đó.", "Chiều cao của hình hộp chữ nhật là:\n$280 : 35 = 8\\text{ (dm)}$\nĐáp số: 8 dm.", "8 dm", 4, 1.0),
            make_essay(3, "Một cái thùng tôn hình hộp chữ nhật có chiều dài $1,8\\text{ m}$, chiều rộng $1,2\\text{ m}$ và chiều cao $0,9\\text{ m}$. Tính thể tích của thùng tôn theo đơn vị lít.", "Đổi: $1,8\\text{ m} = 18\\text{ dm}$; $1,2\\text{ m} = 12\\text{ dm}$; $0,9\\text{ m} = 9\\text{ dm}$.\nThể tích thùng tôn là:\n$18 \\times 12 \\times 9 = 1944\\text{ (dm}^3) = 1944\\text{ (lít)}$\nĐáp số: 1944 lít.", "1944 lít", 4, 1.0),
            make_essay(4, "Một bể kính nuôi cá hình hộp chữ nhật có chiều dài $1\\text{ m}$, chiều rộng $0,5\\text{ m}$ và chiều cao $0,6\\text{ m}$. Người ta đổ nước vào bể sao cho mực nước cao $40\\text{ cm}$.\na) Tính thể tích của cả bể kính.\nb) Tính số lít nước đang có trong bể.", "Bài giải:\na) Thể tích cả bể kính là:\n$1 \\times 0,5 \\times 0,6 = 0,3\\text{ (m}^3)$\nb) Đổi: $1\\text{ m} = 10\\text{ dm}$; $0,5\\text{ m} = 5\\text{ dm}$; $40\\text{ cm} = 4\\text{ dm}$.\nSố lít nước có trong bể là:\n$10 \\times 5 \\times 4 = 200\\text{ (dm}^3) = 200\\text{ (lít)}$\nĐáp số:\na) $0,3\\text{ m}^3$;\nb) 200 lít.", "a) 0,3 m³; b) 200 lít", 5, 1.5),
            make_essay(5, "Một cái kho chứa thóc hình hộp chữ nhật có chiều dài $10\\text{ m}$, chiều rộng $6\\text{ m}$ và chiều cao $4\\text{ m}$. Người ta chứa thóc trong kho đầy tới chiều cao $3,5\\text{ m}$.\na) Tính thể tích lượng thóc có trong kho.\nb) Biết cứ $1\\text{ m}^3$ thóc nặng $0,75\\text{ tấn}$. Hỏi kho thóc đó chứa bao nhiêu tấn thóc?", "Bài giải:\na) Thể tích lượng thóc trong kho là:\n$10 \\times 6 \\times 3,5 = 210\\text{ (m}^3)$\nb) Khối lượng thóc có trong kho là:\n$210 \\times 0,75 = 157,5\\text{ (tấn)}$\nĐáp số:\na) $210\\text{ m}^3$;\nb) 157,5 tấn.", "a) 210 m³; b) 157,5 tấn", 5, 1.5),
            make_essay(6, "Một bể nước hình hộp chữ nhật có diện tích đáy là $4,5\\text{ m}^2$. Người ta mở vòi cho nước chảy vào bể được $2,7\\text{ m}^3$ nước. Hỏi mực nước trong bể dâng lên thêm bao nhiêu đề-xi-mét?", "Bài giải:\nChiều cao mực nước dâng lên trong bể là:\n$2,7 : 4,5 = 0,6\\text{ (m)}$\nĐổi: $0,6\\text{ m} = 6\\text{ dm}$.\nĐáp số: 6 dm.", "6 dm", 5, 1.0)
        ]
    }

    # --- Bài 41 - Đề 3 ---
    exams["th5_b41_test3"] = {
        "id": "th5_b41_test3",
        "lessonId": "th5_b41",
        "lessonNum": 41,
        "testNum": 3,
        "title": "Bài 41: Thể tích hình hộp chữ nhật - Đề số 3",
        "topic": "Thể tích hình hộp chữ nhật",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình hộp chữ nhật có kích thước $10\\text{ cm}, 6\\text{ cm}, 4\\text{ cm}$. Thể tích của nó là:", ["$120\\text{ cm}^3$", "$240\\text{ cm}^3$", "$160\\text{ cm}^3$", "$200\\text{ cm}^3$"], 1, "$10 \\times 6 \\times 4 = 240\\text{ cm}^3$."),
            make_mc(2, "Bể nước có chiều dài $2\\text{ m}$, rộng $1,5\\text{ m}$, cao $1\\text{ m}$. Dung tích tối đa của bể là:", ["3000 lít", "300 lít", "30 000 lít", "30 lít"], 0, "$2 \\times 1,5 \\times 1 = 3\\text{ m}^3 = 3000$ lít."),
            make_mc(3, "Một hình hộp chữ nhật có thể tích $150\\text{ cm}^3$, chiều cao $5\\text{ cm}$. Diện tích đáy của hình hộp là:", ["$25\\text{ cm}^2$", "$30\\text{ cm}^2$", "$35\\text{ cm}^2$", "$20\\text{ cm}^2$"], 1, "$150 : 5 = 30\\text{ cm}^2$."),
            make_mc(4, "Một thùng carton có kích thước đáy $50\\text{ cm} \\times 40\\text{ cm}$, chiều cao $30\\text{ cm}$. Thể tích là:", ["$60\\text{ dm}^3$", "$600\\text{ dm}^3$", "$6\\text{ dm}^3$", "$6000\\text{ dm}^3$"], 0, "$50 \\times 40 \\times 30 = 60\\,000\\text{ cm}^3 = 60\\text{ dm}^3$."),
            make_mc(5, "Nếu tăng cả 3 kích thước của hình hộp chữ nhật lên 2 lần thì thể tích tăng lên:", ["2 lần", "4 lần", "6 lần", "8 lần"], 3, "$2 \\times 2 \\times 2 = 8$ lần."),
            make_mc(6, "Khối kim loại hình hộp chữ nhật có thể tích $0,005\\text{ m}^3$. Đổi ra đề-xi-mét khối là:", ["$0,5\\text{ dm}^3$", "$5\\text{ dm}^3$", "$50\\text{ dm}^3$", "$500\\text{ dm}^3$"], 1, "$0,005 \\times 1000 = 5\\text{ dm}^3$.")
        ],
        "part2": [
            make_essay(1, "Tính thể tích của hình hộp chữ nhật có:\na) $a = 15\\text{ cm}, b = 8\\text{ cm}, c = 6\\text{ cm}$\nb) $a = 3\\text{ m}, b = 2,2\\text{ m}, c = 1,5\\text{ m}$", "a) $V = 15 \\times 8 \\times 6 = 720\\text{ (cm}^3)$\nb) $V = 3 \\times 2,2 \\times 1,5 = 9,9\\text{ (m}^3)$", "a) 720 cm³; b) 9,9 m³", 4, 1.0),
            make_essay(2, "Một hình hộp chữ nhật có thể tích $540\\text{ cm}^3$, chiều rộng $6\\text{ cm}$ và chiều cao $9\\text{ cm}$. Tính chiều dài của hình hộp chữ nhật đó.", "Chiều dài của hình hộp chữ nhật là:\n$540 : (6 \\times 9) = 540 : 54 = 10\\text{ (cm)}$\nĐáp số: 10 cm.", "10 cm", 4, 1.0),
            make_essay(3, "Một bể nước có diện tích đáy là $3,5\\text{ m}^2$ và thể tích là $4,2\\text{ m}^3$. Tính chiều sâu (chiều cao) của bể nước đó.", "Chiều cao của bể nước là:\n$4,2 : 3,5 = 1,2\\text{ (m)}$\nĐáp số: 1,2 m.", "1,2 m", 4, 1.0),
            make_essay(4, "Một cái bể nước hình hộp chữ nhật có chiều dài $2,4\\text{ m}$, chiều rộng $1,5\\text{ m}$ và chiều cao $1,2\\text{ m}$. Bể đang chứa nước ở mức $60\\%$ chiều cao bể.\na) Tính thể tích của bể nước.\nb) Cần đổ thêm bao nhiêu lít nước nữa để đầy bể?", "Bài giải:\na) Thể tích của bể nước là:\n$2,4 \\times 1,5 \\times 1,2 = 4,32\\text{ (m}^3)$\nĐổi: $4,32\\text{ m}^3 = 4320\\text{ dm}^3 = 4320\\text{ lít}$.\nb) Tỉ số phần trăm dung tích cần đổ thêm là:\n$100\\% - 60\\% = 40\\%$\nSố lít nước cần đổ thêm là:\n$4320 \\times 40 : 100 = 1728\\text{ (lít)}$\nĐáp số:\na) $4,32\\text{ m}^3$;\nb) 1728 lít.", "a) 4,32 m³; b) 1728 lít", 5, 1.5),
            make_essay(5, "Một cái thùng hình hộp chữ nhật dài $80\\text{ cm}$, rộng $60\\text{ cm}$, cao $50\\text{ cm}$. Người ta xếp các hộp trà hình lập phương cạnh $10\\text{ cm}$ vào thùng.\na) Xếp được nhiều nhất bao nhiêu hộp trà vào thùng đó?\nb) Thể tích của một hộp trà chiếm bao nhiêu phần trăm thể tích của chiếc thùng?", "Bài giải:\na) Số hộp trà xếp theo chiều dài: $80 : 10 = 8\\text{ (hộp)}$.\nSố hộp trà xếp theo chiều rộng: $60 : 10 = 6\\text{ (hộp)}$.\nSố hộp trà xếp theo chiều cao: $50 : 10 = 5\\text{ (hộp)}$.\nTổng số hộp trà xếp được là:\n$8 \\times 6 \\times 5 = 240\\text{ (hộp)}$\nb) Thể tích của một hộp trà là: $10 \\times 10 \\times 10 = 1000\\text{ (cm}^3)$.\nThể tích của thùng là: $80 \\times 60 \\times 50 = 240\\,000\\text{ (cm}^3)$.\nTỉ số phần trăm thể tích 1 hộp trà so với thùng là:\n$1000 : 240\\,000 = \\frac{1}{240} \\approx 0,42\\%$\nĐáp số:\na) 240 hộp trà;\nb) $0,42\\%$ (hay $\\frac{1}{240}$).", "a) 240 hộp; b) 0,42%", 5, 1.5),
            make_essay(6, "Một bình thủy tinh hình hộp chữ nhật có diện tích đáy là $120\\text{ cm}^2$ đang chứa nước. Khi thả chìm hoàn toàn một khối đá thì mực nước trong bình dâng lên $2,5\\text{ cm}$. Tính thể tích khối đá đó.", "Bài giải:\nThể tích khối đá bằng thể tích nước dâng thêm:\n$120 \\times 2,5 = 300\\text{ (cm}^3)$\nĐáp số: $300\\text{ cm}^3$.", "300 cm³", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 42: THỂ TÍCH HÌNH LẬP PHƯƠNG
    # =========================================================================

    # --- Bài 42 - Đề 1 ---
    exams["th5_b42_test1"] = {
        "id": "th5_b42_test1",
        "lessonId": "th5_b42",
        "lessonNum": 42,
        "testNum": 1,
        "title": "Bài 42: Thể tích hình lập phương - Đề số 1",
        "topic": "Thể tích hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tính thể tích của hình lập phương có cạnh $a$ là:", ["$V = a \\times a \\times a$", "$V = a \\times a \\times 4$", "$V = a \\times a \\times 6$", "$V = a \\times 12$"], 0, "$V = a \\times a \\times a$."),
            make_mc(2, "Một hình lập phương có cạnh $4\\text{ cm}$. Thể tích của nó là:", ["$16\\text{ cm}^3$", "$64\\text{ cm}^3$", "$96\\text{ cm}^3$", "$32\\text{ cm}^3$"], 1, "$V = 4 \\times 4 \\times 4 = 64\\text{ cm}^3$."),
            make_mc(3, "Một hình lập phương có cạnh $0,5\\text{ m}$. Thể tích của nó là:", ["$0,25\\text{ m}^3$", "$1,25\\text{ m}^3$", "$0,125\\text{ m}^3$", "$0,0125\\text{ m}^3$"], 2, "$V = 0,5 \\times 0,5 \\times 0,5 = 0,125\\text{ m}^3$."),
            make_mc(4, "Một khối kim loại hình lập phương có thể tích $27\\text{ dm}^3$. Cạnh của khối kim loại đó là:", ["3 dm", "4 dm", "9 dm", "6 dm"], 0, "Vì $3 \\times 3 \\times 3 = 27$ nên cạnh là 3 dm."),
            make_mc(5, "Một cái bể hình lập phương có cạnh $1\\text{ m}$. Dung tích tối đa của bể là:", ["100 lít", "1000 lít", "10 000 lít", "10 lít"], 1, "$1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000$ lít."),
            make_mc(6, "Nếu cạnh của hình lập phương tăng lên 2 lần thì thể tích tăng lên:", ["2 lần", "4 lần", "6 lần", "8 lần"], 3, "$2 \\times 2 \\times 2 = 8$ lần.")
        ],
        "part2": [
            make_essay(1, "Tính thể tích của hình lập phương có cạnh:\na) $6\\text{ cm}$\nb) $1,2\\text{ m}$", "a) $V = 6 \\times 6 \\times 6 = 216\\text{ (cm}^3)$\nb) $V = 1,2 \\times 1,2 \\times 1,2 = 1,728\\text{ (m}^3)$", "a) 216 cm³; b) 1,728 m³", 4, 1.0),
            make_essay(2, "Một hình lập phương có diện tích một mặt là $25\\text{ cm}^2$. Tính thể tích của hình lập phương đó.", "Vì $5 \\times 5 = 25$ nên độ dài cạnh hình lập phương là $5\\text{ cm}$.\nThể tích của hình lập phương là:\n$5 \\times 5 \\times 5 = 125\\text{ (cm}^3)$\nĐáp số: $125\\text{ cm}^3$.", "125 cm³", 4, 1.0),
            make_essay(3, "Một khối gỗ hình lập phương có chu vi một mặt là $36\\text{ dm}$. Tính thể tích của khối gỗ đó.", "Cạnh của khối gỗ là: $36 : 4 = 9\\text{ (dm)}$.\nThể tích khối gỗ là:\n$9 \\times 9 \\times 9 = 729\\text{ (dm}^3)$\nĐáp số: $729\\text{ dm}^3$.", "729 dm³", 4, 1.0),
            make_essay(4, "Một bể nước dạng hình lập phương có cạnh trong lòng bể là $1,5\\text{ m}$. Hiện tại bể đang chứa $1800\\text{ lít}$ nước.\na) Tính dung tích toàn bộ bể nước theo đơn vị lít.\nb) Cần đổ thêm bao nhiêu lít nước nữa để đầy bể?", "Bài giải:\na) Thể tích của bể nước là:\n$1,5 \\times 1,5 \\times 1,5 = 3,375\\text{ (m}^3)$\nĐổi: $3,375\\text{ m}^3 = 3375\\text{ dm}^3 = 3375\\text{ lít}$.\nb) Số lít nước cần đổ thêm là:\n$3375 - 1800 = 1575\\text{ (lít)}$\nĐáp số:\na) 3375 lít;\nb) 1575 lít.", "a) 3375 lít; b) 1575 lít", 5, 1.5),
            make_essay(5, "Một khối kim loại hình lập phương có cạnh $0,2\\text{ m}$. Biết rằng cứ $1\\text{ dm}^3$ kim loại đó cân nặng $7,5\\text{ kg}$.\na) Tính thể tích của khối kim loại theo đơn vị đề-xi-mét khối.\nb) Tính khối lượng của khối kim loại đó.", "Bài giải:\nĐổi: $0,2\\text{ m} = 2\\text{ dm}$.\na) Thể tích khối kim loại là:\n$2 \\times 2 \\times 2 = 8\\text{ (dm}^3)$\nb) Khối lượng của khối kim loại là:\n$8 \\times 7,5 = 60\\text{ (kg)}$\nĐáp số:\na) $8\\text{ dm}^3$;\nb) 60 kg.", "a) 8 dm³; b) 60 kg", 5, 1.5),
            make_essay(6, "Người ta ghép 27 khối lập phương nhỏ cạnh $2\\text{ cm}$ thành một khối lập phương lớn. Hỏi cạnh của khối lập phương lớn dài bao nhiêu và thể tích của nó là bao nhiêu xăng-ti-mét khối?", "Bài giải:\nKhối lập phương lớn gồm 3 lớp, mỗi lớp có $3 \\times 3 = 9$ khối nhỏ.\nCạnh của khối lập phương lớn là:\n$2 \\times 3 = 6\\text{ (cm)}$\nThể tích của khối lập phương lớn là:\n$6 \\times 6 \\times 6 = 216\\text{ (cm}^3)$\nĐáp số: Cạnh: 6 cm; Thể tích: $216\\text{ cm}^3$.", "Cạnh 6 cm; V = 216 cm³", 5, 1.0)
        ]
    }

    # --- Bài 42 - Đề 2 ---
    exams["th5_b42_test2"] = {
        "id": "th5_b42_test2",
        "lessonId": "th5_b42",
        "lessonNum": 42,
        "testNum": 2,
        "title": "Bài 42: Thể tích hình lập phương - Đề số 2",
        "topic": "Thể tích hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình lập phương có cạnh $3\\text{ dm}$. Thể tích của nó là:", ["$9\\text{ dm}^3$", "$27\\text{ dm}^3$", "$54\\text{ dm}^3$", "$81\\text{ dm}^3$"], 1, "$3 \\times 3 \\times 3 = 27\\text{ dm}^3$."),
            make_mc(2, "Một hình lập phương có diện tích toàn phần là $54\\text{ cm}^2$. Thể tích của nó là:", ["$27\\text{ cm}^3$", "$36\\text{ cm}^3$", "$18\\text{ cm}^3$", "$81\\text{ cm}^3$"], 0, "Diện tích 1 mặt: $54 : 6 = 9\\text{ cm}^2 \\implies a = 3\\text{ cm}$. $V = 3 \\times 3 \\times 3 = 27\\text{ cm}^3$."),
            make_mc(3, "Một khối gỗ hình lập phương có thể tích $125\\text{ cm}^3$. Độ dài cạnh khối gỗ là:", ["4 cm", "5 cm", "6 cm", "25 cm"], 1, "Vì $5 \\times 5 \\times 5 = 125$ nên cạnh là 5 cm."),
            make_mc(4, "Một bể cá hình lập phương có cạnh $0,8\\text{ m}$. Thể tích bể cá là:", ["$0,512\\text{ m}^3$", "$5,12\\text{ m}^3$", "$0,64\\text{ m}^3$", "$0,0512\\text{ m}^3$"], 0, "$0,8 \\times 0,8 \\times 0,8 = 0,512\\text{ m}^3$."),
            make_mc(5, "Xếp 64 khối lập phương nhỏ cạnh $1\\text{ cm}$ thành hình lập phương lớn. Cạnh hình lập phương lớn là:", ["2 cm", "3 cm", "4 cm", "8 cm"], 2, "Vì $4 \\times 4 \\times 4 = 64$ nên cạnh dài 4 cm."),
            make_mc(6, "Nếu cạnh hình lập phương gấp lên 3 lần thì thể tích gấp lên:", ["3 lần", "9 lần", "18 lần", "27 lần"], 3, "$3 \\times 3 \\times 3 = 27$ lần.")
        ],
        "part2": [
            make_essay(1, "Tính thể tích của hình lập phương có cạnh:\na) $7\\text{ cm}$\nb) $0,9\\text{ m}$", "a) $V = 7 \\times 7 \\times 7 = 343\\text{ (cm}^3)$\nb) $V = 0,9 \\times 0,9 \\times 0,9 = 0,729\\text{ (m}^3)$", "a) 343 cm³; b) 0,729 m³", 4, 1.0),
            make_essay(2, "Một hình lập phương có diện tích xung quanh là $64\\text{ dm}^2$. Tính thể tích của hình lập phương đó.", "Diện tích một mặt là: $64 : 4 = 16\\text{ (dm}^2)$.\nVì $4 \\times 4 = 16$ nên cạnh hình lập phương là $4\\text{ dm}$.\nThể tích hình lập phương là:\n$4 \\times 4 \\times 4 = 64\\text{ (dm}^3)$\nĐáp số: $64\\text{ dm}^3$.", "64 dm³", 4, 1.0),
            make_essay(3, "Một hình lập phương có tổng độ dài 12 cạnh là $60\\text{ cm}$. Tính thể tích của hình lập phương đó.", "Độ dài mỗi cạnh là: $60 : 12 = 5\\text{ (cm)}$.\nThể tích hình lập phương là:\n$5 \\times 5 \\times 5 = 125\\text{ (cm}^3)$\nĐáp số: $125\\text{ cm}^3$.", "125 cm³", 4, 1.0),
            make_essay(4, "Một bể nước dạng hình lập phương có cạnh $1,2\\text{ m}$. Bể đang chứa nước chiếm $75\\%$ thể tích bể.\na) Tính thể tích nước đang có trong bể theo đơn vị lít.\nb) Người ta dùng hết một lượng nước bằng $40\\%$ số nước đang có. Hỏi lượng nước còn lại trong bể là bao nhiêu lít?", "Bài giải:\na) Thể tích của bể nước là:\n$1,2 \\times 1,2 \\times 1,2 = 1,728\\text{ (m}^3)$\nĐổi: $1,728\\text{ m}^3 = 1728\\text{ dm}^3 = 1728\\text{ lít}$.\nLượng nước đang có trong bể là:\n$1728 \\times 75 : 100 = 1296\\text{ (lít)}$\nb) Số lít nước còn lại sau khi dùng là:\n$1296 \\times (100\\% - 40\\%) : 100 = 777,6\\text{ (lít)}$\nĐáp số:\na) 1296 lít;\nb) 777,6 lít.", "a) 1296 lít; b) 777,6 lít", 5, 1.5),
            make_essay(5, "Hai khối kim loại hình lập phương: Khối A có cạnh $4\\text{ cm}$, Khối B có cạnh $8\\text{ cm}$.\na) Thể tích khối B gấp mấy lần thể tích khối A?\nb) Nếu khối A nặng $480\\text{ gam}$ thì khối B nặng bao nhiêu gam (cùng chất liệu)?", "Bài giải:\na) Thể tích khối A là: $4 \\times 4 \\times 4 = 64\\text{ (cm}^3)$.\nThể tích khối B là: $8 \\times 8 \\times 8 = 512\\text{ (cm}^3)$.\nThể tích khối B gấp thể tích khối A số lần là:\n$512 : 64 = 8\\text{ (lần)}$\nb) Khối B nặng số gam là:\n$480 \\times 8 = 3840\\text{ (gam)}$\nĐáp số:\na) 8 lần;\nb) 3840 gam.", "a) 8 lần; b) 3840 gam", 5, 1.5),
            make_essay(6, "Một khối gỗ hình hộp chữ nhật có kích thước $12\\text{ dm} \\times 8\\text{ dm} \\times 6\\text{ dm}$. Người ta muốn cắt khối gỗ đó thành các khối lập phương cạnh $2\\text{ dm}$ mà không thừa mẩu gỗ nào. Hỏi cắt được bao nhiêu khối lập phương như vậy?", "Bài giải:\nThể tích khối gỗ hình hộp chữ nhật là:\n$12 \\times 8 \\times 6 = 576\\text{ (dm}^3)$\nThể tích mỗi khối lập phương nhỏ là:\n$2 \\times 2 \\times 2 = 8\\text{ (dm}^3)$\nSố khối lập phương cắt được là:\n$576 : 8 = 72\\text{ (khối)}$\nĐáp số: 72 khối.", "72 khối", 5, 1.0)
        ]
    }

    # --- Bài 42 - Đề 3 ---
    exams["th5_b42_test3"] = {
        "id": "th5_b42_test3",
        "lessonId": "th5_b42",
        "lessonNum": 42,
        "testNum": 3,
        "title": "Bài 42: Thể tích hình lập phương - Đề số 3",
        "topic": "Thể tích hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình lập phương có cạnh $10\\text{ cm}$. Thể tích của nó là:", ["$100\\text{ cm}^3$", "$1000\\text{ cm}^3$", "$1\\text{ dm}^3$", "Cả B và C đều đúng"], 3, "$10 \\times 10 \\times 10 = 1000\\text{ cm}^3 = 1\\text{ dm}^3$."),
            make_mc(2, "Một hình lập phương có thể tích $1\\text{ m}^3$. Cạnh của nó là:", ["1 dm", "10 dm", "100 dm", "0,1 m"], 1, "Vì $10 \\times 10 \\times 10 = 1000\\text{ dm}^3 = 1\\text{ m}^3$ nên cạnh dài $10\\text{ dm}$."),
            make_mc(3, "Một khối rubik có thể tích $216\\text{ cm}^3$. Độ dài cạnh của nó là:", ["5 cm", "6 cm", "7 cm", "8 cm"], 1, "Vì $6 \\times 6 \\times 6 = 216$ nên cạnh là 6 cm."),
            make_mc(4, "Một bể cá hình lập phương cạnh $6\\text{ dm}$ chứa đầy nước. Lượng nước trong bể là:", ["36 lít", "72 lít", "216 lít", "2160 lít"], 2, "$6 \\times 6 \\times 6 = 216\\text{ dm}^3 = 216$ lít."),
            make_mc(5, "Hai hình lập phương có cạnh lần lượt là $2\\text{ cm}$ và $4\\text{ cm}$. Tỉ số thể tích của hình bé so với hình lớn là:", ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{1}{8}$", "$\\frac{1}{16}$"], 2, "$(2/4)^3 = (1/2)^3 = 1/8$."),
            make_mc(6, "Một khối kim loại hình lập phương cạnh $0,1\\text{ m}$ có thể tích là:", ["$0,1\\text{ m}^3$", "$0,01\\text{ m}^3$", "$0,001\\text{ m}^3$", "$1\\text{ dm}^3$"], 2, "$0,1 \\times 0,1 \\times 0,1 = 0,001\\text{ m}^3 = 1\\text{ dm}^3$.")
        ],
        "part2": [
            make_essay(1, "Tính thể tích của hình lập phương có cạnh:\na) $2,5\\text{ dm}$\nb) $8\\text{ cm}$", "a) $V = 2,5 \\times 2,5 \\times 2,5 = 15,625\\text{ (dm}^3)$\nb) $V = 8 \\times 8 \\times 8 = 512\\text{ (cm}^3)$", "a) 15,625 dm³; b) 512 cm³", 4, 1.0),
            make_essay(2, "Một hình lập phương có diện tích toàn phần là $150\\text{ cm}^2$. Tính thể tích của hình lập phương đó.", "Diện tích một mặt là: $150 : 6 = 25\\text{ (cm}^2)$.\nVì $5 \\times 5 = 25$ nên cạnh hình lập phương là $5\\text{ cm}$.\nThể tích hình lập phương là:\n$5 \\times 5 \\times 5 = 125\\text{ (cm}^3)$\nĐáp số: $125\\text{ cm}^3$.", "125 cm³", 4, 1.0),
            make_essay(3, "Một khối bê tông hình lập phương có thể tích $0,729\\text{ m}^3$. Hỏi cạnh của khối bê tông đó dài bao nhiêu mét?", "Ta có: $0,9 \\times 0,9 \\times 0,9 = 0,729$.\nDo đó cạnh của khối bê tông dài $0,9\\text{ m}$.\nĐáp số: 0,9 m.", "0,9 m", 4, 1.0),
            make_essay(4, "Một bể nước hình lập phương có cạnh $1,6\\text{ m}$. Hiện tại bể đang chứa nước cao $1\\text{ m}$.\na) Tính số lít nước đang có trong bể.\nb) Cần đổ thêm bao nhiêu lít nước nữa để đầy bể?", "Bài giải:\nĐổi: $1,6\\text{ m} = 16\\text{ dm}$; $1\\text{ m} = 10\\text{ dm}$.\na) Số lít nước đang có trong bể là:\n$16 \\times 16 \\times 10 = 2560\\text{ (dm}^3) = 2560\\text{ (lít)}$\nb) Chiều cao phần bể chưa có nước là:\n$16 - 10 = 6\\text{ (dm)}$\nSố lít nước cần đổ thêm là:\n$16 \\times 16 \\times 6 = 1536\\text{ (dm}^3) = 1536\\text{ (lít)}$\nĐáp số:\na) 2560 lít;\nb) 1536 lít.", "a) 2560 lít; b) 1536 lít", 5, 1.5),
            make_essay(5, "Một cái thùng tôn hình lập phương không nắp có diện tích tôn làm thùng là $1,8\\text{ m}^2$ (không kể mép hàn).\na) Tính diện tích một mặt của chiếc thùng tôn đó.\nb) Tính thể tích của chiếc thùng tôn đó theo đơn vị lít.", "Bài giải:\na) Thùng không nắp có 5 mặt hình vuông. Diện tích một mặt là:\n$1,8 : 5 = 0,36\\text{ (m}^2)$\nb) Vì $0,6 \\times 0,6 = 0,36$ nên cạnh của thùng tôn là $0,6\\text{ m}$.\nThể tích của chiếc thùng là:\n$0,6 \\times 0,6 \\times 0,6 = 0,216\\text{ (m}^3)$\nĐổi: $0,216\\text{ m}^3 = 216\\text{ dm}^3 = 216\\text{ lít}$.\nĐáp số:\na) $0,36\\text{ m}^2$;\nb) 216 lít.", "a) 0,36 m²; b) 216 lít", 5, 1.5),
            make_essay(6, "Một khối kim loại hình lập phương cạnh $10\\text{ cm}$ đem nung chảy rồi đúc thành các khối lập phương nhỏ cạnh $2\\text{ cm}$. Hỏi đúc được tất cả bao nhiêu khối lập phương nhỏ (coi hao hụt không đáng kể)?", "Bài giải:\nThể tích khối kim loại lớn là:\n$10 \\times 10 \\times 10 = 1000\\text{ (cm}^3)$\nThể tích mỗi khối lập phương nhỏ là:\n$2 \\times 2 \\times 2 = 8\\text{ (cm}^3)$\nSố khối lập phương nhỏ đúc được là:\n$1000 : 8 = 125\\text{ (khối)}$\nĐáp số: 125 khối.", "125 khối", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 43: GIỚI THIỆU HÌNH TRỤ
    # =========================================================================

    # --- Bài 43 - Đề 1 ---
    exams["th5_b43_test1"] = {
        "id": "th5_b43_test1",
        "lessonId": "th5_b43",
        "lessonNum": 43,
        "testNum": 1,
        "title": "Bài 43: Giới thiệu hình trụ - Đề số 1",
        "topic": "Giới thiệu hình trụ",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hình trụ có bao nhiêu mặt đáy?", ["1 mặt", "2 mặt", "3 mặt", "4 mặt"], 1, "Hình trụ có 2 mặt đáy."),
            make_mc(2, "Hai mặt đáy của hình trụ là hai hình gì?", ["Hình vuông", "Hình chữ nhật", "Hình tròn bằng nhau", "Hình elip"], 2, "Hai mặt đáy của hình trụ là hai hình tròn bằng nhau."),
            make_mc(3, "Đồ vật nào dưới đây có dạng hình trụ?", ["Hộp sữa bột dạng lon", "Hộp phấn hình chữ nhật", "Khối rubik", "Quả bóng đá"], 0, "Lon sữa bột có dạng hình trụ."),
            make_mc(4, "Mặt xung quanh của hình trụ khi trải phẳng ra là một:", ["Hình tròn", "Hình tam giác", "Hình chữ nhật", "Hình thang"], 2, "Mặt xung quanh hình trụ khi mở ra là một hình chữ nhật."),
            make_mc(5, "Khoảng cách giữa hai mặt đáy của hình trụ gọi là:", ["Bán kính đáy", "Đường kính đáy", "Chiều cao của hình trụ", "Chu vi đáy"], 2, "Khoảng cách giữa hai đáy là chiều cao hình trụ."),
            make_mc(6, "Một lon nước ngọt hình trụ có đường kính đáy $6\\text{ cm}$. Bán kính đáy của lon nước ngọt là:", ["2 cm", "3 cm", "4 cm", "12 cm"], 1, "$r = 6 : 2 = 3\\text{ cm}$.")
        ],
        "part2": [
            make_essay(1, "Nêu các đặc điểm cơ bản của hình trụ (mặt đáy, mặt xung quanh).", "Đặc điểm của hình trụ:\n- Có 2 mặt đáy là hai hình tròn bằng nhau và song song với nhau.\n- Có một mặt xung quanh cong nối liền hai mặt đáy.\n- Chiều cao là khoảng cách vuông góc giữa hai mặt đáy.", "2 đáy tròn bằng nhau, 1 mặt xung quanh", 4, 1.0),
            make_essay(2, "Hãy kể tên 4 đồ vật trong đời sống hàng ngày có dạng hình trụ.", "Bốn đồ vật có dạng hình trụ là:\n1. Lon nước ngọt (hoặc lon sữa đặc);\n2. Ống nghiệm (hoặc cây nến tròn);\n3. Thùng phuy đựng dầu;\n4. Hộp bút chì dạng ống tròn.", "Lon nước, cây nến, thùng phuy, ống đựng bút", 4, 1.0),
            make_essay(3, "Một hình trụ có bán kính mặt đáy là $4\\text{ cm}$. Tính chu vi và diện tích một mặt đáy của hình trụ đó.", "Chu vi một mặt đáy là:\n$4 \\times 2 \\times 3,14 = 25,12\\text{ (cm)}$\nDiện tích một mặt đáy là:\n$4 \\times 4 \\times 3,14 = 50,24\\text{ (cm}^2)$\nĐáp số: Chu vi: 25,12 cm; Diện tích: $50,24\\text{ cm}^2$.", "C = 25,12 cm; S = 50,24 cm²", 4, 1.0),
            make_essay(4, "Một hộp sữa hình trụ có đường kính đáy là $10\\text{ cm}$ và chiều cao là $14\\text{ cm}$.\na) Tính chu vi mặt đáy của hộp sữa.\nb) Người ta dán một nhãn giấy bao quanh vừa khít mặt xung quanh của hộp sữa. Tính diện tích nhãn giấy đó (không kể mép dán).", "Bài giải:\na) Chu vi mặt đáy của hộp sữa là:\n$10 \\times 3,14 = 31,4\\text{ (cm)}$\nb) Nhãn giấy bao quanh mặt xung quanh có dạng hình chữ nhật với chiều dài bằng chu vi đáy và chiều rộng bằng chiều cao hộp sữa.\nDiện tích nhãn giấy là:\n$31,4 \\times 14 = 439,6\\text{ (cm}^2)$\nĐáp số:\na) 31,4 cm;\nb) $439,6\\text{ cm}^2$.", "a) 31,4 cm; b) 439,6 cm²", 5, 1.5),
            make_essay(5, "Một cái thùng phuy hình trụ có chiều cao $1,2\\text{ m}$, đường kính đáy là $0,6\\text{ m}$.\na) Tính diện tích hai mặt đáy của chiếc thùng phuy đó.\nb) Tính diện tích mặt xung quanh của thùng phuy.", "Bài giải:\nBán kính đáy thùng phuy là: $0,6 : 2 = 0,3\\text{ (m)}$.\na) Diện tích một mặt đáy là:\n$0,3 \\times 0,3 \\times 3,14 = 0,2826\\text{ (m}^2)$\nDiện tích hai mặt đáy là:\n$0,2826 \\times 2 = 0,5652\\text{ (m}^2)$\nb) Chu vi đáy thùng phuy là:\n$0,6 \\times 3,14 = 1,884\\text{ (m)}$\nDiện tích xung quanh là:\n$1,884 \\times 1,2 = 2,2608\\text{ (m}^2)$\nĐáp số:\na) $0,5652\\text{ m}^2$;\nb) $2,2608\\text{ m}^2$.", "a) 0,5652 m²; b) 2,2608 m²", 5, 1.5),
            make_essay(6, "Một khúc gỗ hình trụ tròn có chiều dài $2\\text{ m}$. Bác thợ mộc cưa khúc gỗ thành 3 khúc ngắn hơn bằng 2 nhát cưa ngang. Hỏi sau khi cưa, tổng số mặt đáy của các khúc gỗ nhỏ tạo thành là bao nhiêu mặt?", "Bài giải:\nMỗi khúc gỗ hình trụ có 2 mặt đáy.\nSau khi cưa thành 3 khúc gỗ hình trụ, tổng số khúc gỗ là 3.\nTổng số mặt đáy của 3 khúc gỗ là:\n$3 \\times 2 = 6\\text{ (mặt đáy)}$\n(Ban đầu có 2 mặt đáy, mỗi nhát cưa tạo thêm 2 mặt đáy mới: $2 + 2 \\times 2 = 6$ mặt đáy).\nĐáp số: 6 mặt đáy.", "6 mặt đáy", 5, 1.0)
        ]
    }

    # --- Bài 43 - Đề 2 ---
    exams["th5_b43_test2"] = {
        "id": "th5_b43_test2",
        "lessonId": "th5_b43",
        "lessonNum": 43,
        "testNum": 2,
        "title": "Bài 43: Giới thiệu hình trụ - Đề số 2",
        "topic": "Giới thiệu hình trụ",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hình trụ có mặt xung quanh là:", ["Một mặt phẳng", "Một mặt cong", "Hai mặt phẳng", "Các hình chữ nhật ghép lại"], 1, "Mặt xung quanh của hình trụ là một mặt cong."),
            make_mc(2, "Đặc điểm nào dưới đây KHÔNG phải của hình trụ?", ["Có hai mặt đáy là hình tròn bằng nhau", "Có 8 đỉnh và 12 cạnh", "Mặt xung quanh là mặt cong", "Các mặt đáy nằm trên hai mặt phẳng song song"], 1, "Hình trụ không có các đỉnh và các cạnh thẳng như hình đa diện."),
            make_mc(3, "Một cốc uống nước hình trụ có bán kính đáy $3\\text{ cm}$. Diện tích đáy cốc là:", ["$9,42\\text{ cm}^2$", "$18,84\\text{ cm}^2$", "$28,26\\text{ cm}^2$", "$56,52\\text{ cm}^2$"], 2, "$3 \\times 3 \\times 3,14 = 28,26\\text{ cm}^2$."),
            make_mc(4, "Một ống nước bằng nhựa có dạng hình gì?", ["Hình hộp chữ nhật", "Hình lập phương", "Hình trụ", "Hình cầu"], 2, "Ống nước tròn có dạng hình trụ."),
            make_mc(5, "Khi cuộn một tờ giấy hình chữ nhật kích thước $20\\text{ cm} \\times 10\\text{ cm}$ theo chiều dài thì ta được mặt xung quanh của:", ["Hình hộp chữ nhật", "Hình lập phương", "Hình trụ", "Hình tròn"], 2, "Ta được mặt xung quanh của một hình trụ."),
            make_mc(6, "Một lon sữa đặc có chiều cao $8\\text{ cm}$ và chu vi đáy $24\\text{ cm}$. Diện tích nhãn bọc xung quanh lon sữa là:", ["$192\\text{ cm}^2$", "$96\\text{ cm}^2$", "$120\\text{ cm}^2$", "$160\\text{ cm}^2$"], 0, "$S = 24 \\times 8 = 192\\text{ cm}^2$.")
        ],
        "part2": [
            make_essay(1, "So sánh hình trụ với hình hộp chữ nhật về:\na) Hình dạng mặt đáy\nb) Mặt xung quanh", "a) Mặt đáy của hình hộp chữ nhật là hình chữ nhật, còn mặt đáy hình trụ là hình tròn.\nb) Mặt xung quanh hình hộp chữ nhật gồm 4 mặt phẳng hình chữ nhật, còn mặt xung quanh hình trụ là một mặt cong.", "Đáy tròn vs chữ nhật; cong vs phẳng", 4, 1.0),
            make_essay(2, "Một chiếc cột cờ dạng hình trụ có đường kính đáy là $0,4\\text{ m}$. Tính chu vi đáy của chiếc cột cờ đó.", "Chu vi đáy cột cờ là:\n$0,4 \\times 3,14 = 1,256\\text{ (m)}$\nĐáp số: 1,256 m.", "1,256 m", 4, 1.0),
            make_essay(3, "Một cây nến hình trụ có bán kính đáy là $2\\text{ cm}$. Tính tổng diện tích của hai mặt đáy cây nến đó.", "Diện tích một mặt đáy cây nến là:\n$2 \\times 2 \\times 3,14 = 12,56\\text{ (cm}^2)$\nTổng diện tích hai mặt đáy là:\n$12,56 \\times 2 = 25,12\\text{ (cm}^2)$\nĐáp số: $25,12\\text{ cm}^2$.", "25,12 cm²", 4, 1.0),
            make_essay(4, "Một ống cống bê tông dạng hình trụ rỗng có chiều dài $2\\text{ m}$, đường kính ngoài là $1\\text{ m}$. Người ta lăn sơn chống thấm toàn bộ mặt xung quanh phía ngoài của ống cống.\na) Tính chu vi đáy ngoài của ống cống.\nb) Tính diện tích bề mặt cần quét sơn chống thấm.", "Bài giải:\na) Chu vi đáy ngoài của ống cống là:\n$1 \\times 3,14 = 3,14\\text{ (m)}$\nb) Diện tích mặt ngoài cần quét sơn là:\n$3,14 \\times 2 = 6,28\\text{ (m}^2)$\nĐáp số:\na) 3,14 m;\nb) $6,28\\text{ m}^2$.", "a) 3,14 m; b) 6,28 m²", 5, 1.5),
            make_essay(5, "Một chiếc thùng rác thông minh có dạng hình trụ không có nắp phía trên, đường kính đáy là $30\\text{ cm}$, chiều cao $45\\text{ cm}$.\na) Tính diện tích mặt đáy của chiếc thùng rác.\nb) Tính diện tích mặt xung quanh của chiếc thùng rác.", "Bài giải:\nBán kính đáy là: $30 : 2 = 15\\text{ (cm)}$.\na) Diện tích mặt đáy thùng rác là:\n$15 \\times 15 \\times 3,14 = 706,5\\text{ (cm}^2)$\nb) Chu vi đáy thùng rác là:\n$30 \\times 3,14 = 94,2\\text{ (cm)}$\nDiện tích mặt xung quanh thùng rác là:\n$94,2 \\times 45 = 4239\\text{ (cm}^2)$\nĐáp số:\na) $706,5\\text{ cm}^2$;\nb) $4239\\text{ cm}^2$.", "a) 706,5 cm²; b) 4239 cm²", 5, 1.5),
            make_essay(6, "Người ta dùng một tấm bìa hình chữ nhật có chiều dài $31,4\\text{ cm}$ và chiều rộng $15\\text{ cm}$ uốn cong mép để tạo thành mặt xung quanh của một hình trụ (không tính mép dán). Tính đường kính đáy của hình trụ được tạo thành.", "Bài giải:\nChu vi mặt đáy của hình trụ chính bằng chiều dài của tấm bìa hình chữ nhật:\n$C = 31,4\\text{ cm}$.\nĐường kính đáy của hình trụ đó là:\n$d = 31,4 : 3,14 = 10\\text{ (cm)}$\nĐáp số: 10 cm.", "10 cm", 5, 1.0)
        ]
    }

    # --- Bài 43 - Đề 3 ---
    exams["th5_b43_test3"] = {
        "id": "th5_b43_test3",
        "lessonId": "th5_b43",
        "lessonNum": 43,
        "testNum": 3,
        "title": "Bài 43: Giới thiệu hình trụ - Đề số 3",
        "topic": "Giới thiệu hình trụ",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hai mặt đáy của hình trụ có đặc điểm gì?", ["Song song và bằng nhau", "Cắt nhau", "Có bán kính khác nhau", "Không cùng nằm trên hai mặt phẳng"], 0, "Hai đáy của hình trụ song song và là hai hình tròn bằng nhau."),
            make_mc(2, "Cắt một hình trụ bằng một mặt phẳng song song với đáy, ta được mặt cắt là:", ["Hình chữ nhật", "Hình vuông", "Hình tròn", "Hình tam giác"], 2, "Mặt cắt song song với đáy là hình tròn bằng đáy."),
            make_mc(3, "Một hình trụ có chu vi đáy $18,84\\text{ cm}$. Bán kính đáy của nó là:", ["2 cm", "3 cm", "4 cm", "6 cm"], 1, "$r = 18,84 : 3,14 : 2 = 3\\text{ cm}$."),
            make_mc(4, "Một lon chè hình trụ có chiều cao $12\\text{ cm}$, bán kính đáy $4\\text{ cm}$. Diện tích một đáy là:", ["$50,24\\text{ cm}^2$", "$25,12\\text{ cm}^2$", "$12,56\\text{ cm}^2$", "$100,48\\text{ cm}^2$"], 0, "$4 \\times 4 \\times 3,14 = 50,24\\text{ cm}^2$."),
            make_mc(5, "Đồ vật nào dưới đây KHÔNG có dạng hình trụ?", ["Viên gạch ống", "Hộp phấn hình lập phương", "Cây nến tròn", "Cột nhà tròn"], 1, "Hộp phấn có dạng hình lập phương hoặc hình hộp chữ nhật."),
            make_mc(6, "Một tấm kim loại hình chữ nhật cuộn tròn thành hình trụ có chiều cao $20\\text{ cm}$ và diện tích xung quanh $628\\text{ cm}^2$. Chu vi đáy là:", ["31,4 cm", "62,8 cm", "15,7 cm", "20 cm"], 0, "$628 : 20 = 31,4\\text{ cm}$.")
        ],
        "part2": [
            make_essay(1, "Hình vẽ khai triển của một hình trụ gồm những hình nào?", "Hình khai triển của hình trụ gồm:\n- Một hình chữ nhật (mặt xung quanh);\n- Hai hình tròn bằng nhau (hai mặt đáy).", "1 hình chữ nhật và 2 hình tròn", 4, 1.0),
            make_essay(2, "Một ống tre dạng hình trụ có đường kính ngoài là $8\\text{ cm}$. Tính chu vi mặt ngoài ống tre đó.", "Chu vi mặt ngoài ống tre là:\n$8 \\times 3,14 = 25,12\\text{ (cm)}$\nĐáp số: 25,12 cm.", "25,12 cm", 4, 1.0),
            make_essay(3, "Một cái lọ hoa hình trụ có bán kính đáy $5\\text{ cm}$. Tính diện tích của đáy lọ hoa đó.", "Diện tích đáy lọ hoa là:\n$5 \\times 5 \\times 3,14 = 78,5\\text{ (cm}^2)$\nĐáp số: $78,5\\text{ cm}^2$.", "78,5 cm²", 4, 1.0),
            make_essay(4, "Một chiếc bánh kem sinh nhật hình trụ có đường kính đáy $24\\text{ cm}$ và chiều cao $10\\text{ cm}$.\na) Tính diện tích mặt trên của chiếc bánh kem.\nb) Người ta viền một dải ruy băng xung quanh thân bánh kem vừa khít 1 vòng. Tính chiều dài dải ruy băng (không kể phần thắt nơ).", "Bài giải:\nBán kính đáy bánh kem là: $24 : 2 = 12\\text{ (cm)}$.\na) Diện tích mặt trên của chiếc bánh là:\n$12 \\times 12 \\times 3,14 = 452,16\\text{ (cm}^2)$\nb) Chiều dài dải ruy băng bằng chu vi đáy của chiếc bánh:\n$24 \\times 3,14 = 75,36\\text{ (cm)}$\nĐáp số:\na) $452,16\\text{ cm}^2$;\nb) 75,36 cm.", "a) 452,16 cm²; b) 75,36 cm", 5, 1.5),
            make_essay(5, "Một cái thùng tôn hình trụ có nắp, đường kính đáy là $0,8\\text{ m}$, chiều cao $1,5\\text{ m}$.\na) Tính diện tích tôn làm hai mặt đáy.\nb) Tính diện tích tôn làm mặt xung quanh (coi mép nối không đáng kể).", "Bài giải:\nBán kính đáy là: $0,8 : 2 = 0,4\\text{ (m)}$.\na) Diện tích một đáy là: $0,4 \\times 0,4 \\times 3,14 = 0,5024\\text{ (m}^2)$.\nDiện tích 2 đáy là:\n$0,5024 \\times 2 = 1,0048\\text{ (m}^2)$\nb) Chu vi đáy là: $0,8 \\times 3,14 = 2,512\\text{ (m)}$.\nDiện tích xung quanh là:\n$2,512 \\times 1,5 = 3,768\\text{ (m}^2)$\nĐáp số:\na) $1,0048\\text{ m}^2$;\nb) $3,768\\text{ m}^2$.", "a) 1,0048 m²; b) 3,768 m²", 5, 1.5),
            make_essay(6, "Cắt một hình trụ bằng một mặt phẳng đi qua trục của nó ta được thiết diện là một hình vuông có cạnh bằng $8\\text{ cm}$. Tính bán kính đáy và chiều cao của hình trụ đó.", "Bài giải:\nThiết diện qua trục là hình vuông cạnh $8\\text{ cm}$, do đó:\n- Chiều cao của hình trụ bằng cạnh hình vuông: $h = 8\\text{ cm}$.\n- Đường kính đáy của hình trụ bằng cạnh hình vuông: $d = 8\\text{ cm}$.\nBán kính đáy của hình trụ là:\n$8 : 2 = 4\\text{ (cm)}$\nĐáp số: Bán kính đáy: 4 cm; Chiều cao: 8 cm.", "r = 4 cm; h = 8 cm", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 44: LUYỆN TẬP CHUNG CHỦ ĐỀ 8
    # =========================================================================

    # --- Bài 44 - Đề 1 ---
    exams["th5_b44_test1"] = {
        "id": "th5_b44_test1",
        "lessonId": "th5_b44",
        "lessonNum": 44,
        "testNum": 1,
        "title": "Bài 44: Luyện tập chung Chủ đề 8 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 8",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình lập phương có cạnh $5\\text{ cm}$. Diện tích toàn phần của nó là:", ["$100\\text{ cm}^2$", "$125\\text{ cm}^2$", "$150\\text{ cm}^2$", "$25\\text{ cm}^2$"], 2, "$S_{tp} = 5 \\times 5 \\times 6 = 150\\text{ cm}^2$."),
            make_mc(2, "Thể tích của hình hộp chữ nhật có kích thước $6\\text{ dm}, 5\\text{ dm}, 4\\text{ dm}$ là:", ["$120\\text{ dm}^3$", "$100\\text{ dm}^3$", "$150\\text{ dm}^3$", "$80\\text{ dm}^3$"], 0, "$6 \\times 5 \\times 4 = 120\\text{ dm}^3$."),
            make_mc(3, "Một hình lập phương có thể tích $64\\text{ cm}^3$. Diện tích xung quanh của nó là:", ["$16\\text{ cm}^2$", "$48\\text{ cm}^2$", "$64\\text{ cm}^2$", "$96\\text{ cm}^2$"], 2, "Cạnh là 4 cm. $S_{xq} = 4 \\times 4 \\times 4 = 64\\text{ cm}^2$."),
            make_mc(4, "Một bể nước dạng hình hộp chữ nhật có diện tích đáy $3\\text{ m}^2$, chiều cao $1,4\\text{ m}$. Thể tích bể là:", ["$3,4\\text{ m}^3$", "$4,2\\text{ m}^3$", "$4,5\\text{ m}^3$", "$5,2\\text{ m}^3$"], 1, "$3 \\times 1,4 = 4,2\\text{ m}^3$."),
            make_mc(5, "Đặc điểm nào phân biệt hình trụ với hình hộp chữ nhật?", ["Hình trụ có các mặt đáy là hình tròn", "Hình trụ không có mặt xung quanh", "Hình trụ có 6 mặt", "Hình trụ có 8 đỉnh"], 0, "Hình trụ có 2 mặt đáy là hình tròn."),
            make_mc(6, "Xếp các khối lập phương cạnh $1\\text{ cm}$ vào hộp kích thước $4\\text{ cm} \\times 3\\text{ cm} \\times 2\\text{ cm}$. Xếp được:", ["24 khối", "12 khối", "18 khối", "36 khối"], 0, "$4 \\times 3 \\times 2 = 24$ khối.")
        ],
        "part2": [
            make_essay(1, "Một hình hộp chữ nhật có chiều dài $8\\text{ cm}$, chiều rộng $5\\text{ cm}$, chiều cao $4\\text{ cm}$.\na) Tính diện tích xung quanh của hình hộp chữ nhật.\nb) Tính thể tích của hình hộp chữ nhật đó.", "a) $S_{xq} = (8 + 5) \\times 2 \\times 4 = 104\\text{ (cm}^2)$\nb) $V = 8 \\times 5 \\times 4 = 160\\text{ (cm}^3)$", "a) 104 cm²; b) 160 cm³", 4, 1.0),
            make_essay(2, "Một hình lập phương có cạnh $0,6\\text{ m}$. Tính diện tích toàn phần và thể tích của hình lập phương đó.", "$S_{tp} = 0,6 \\times 0,6 \\times 6 = 2,16\\text{ (m}^2)$\n$V = 0,6 \\times 0,6 \\times 0,6 = 0,216\\text{ (m}^3)$", "Stp = 2,16 m²; V = 0,216 m³", 4, 1.0),
            make_essay(3, "Một hình hộp chữ nhật có thể tích $210\\text{ cm}^3$, chiều dài $7\\text{ cm}$, chiều cao $5\\text{ cm}$. Tính diện tích mặt đáy của hình hộp chữ nhật đó.", "Diện tích mặt đáy của hình hộp chữ nhật là:\n$210 : 5 = 42\\text{ (cm}^2)$\nĐáp số: $42\\text{ cm}^2$.", "42 cm²", 4, 1.0),
            make_essay(4, "Một căn phòng học hình hộp chữ nhật có chiều dài $9\\text{ m}$, chiều rộng $6\\text{ m}$ và chiều cao $3,5\\text{ m}$. Người ta quét vôi trần nhà và 4 bức tường xung quanh phòng. Tổng diện tích các cửa sổ và cửa ra vào là $11,5\\text{ m}^2$.\na) Tính diện tích cần quét vôi của căn phòng.\nb) Biết tiền công quét vôi $1\\text{ m}^2$ là $25\\,000$ đồng. Hỏi quét vôi căn phòng đó hết bao nhiêu tiền?", "Bài giải:\na) Diện tích xung quanh căn phòng là:\n$(9 + 6) \\times 2 \\times 3,5 = 105\\text{ (m}^2)$\nDiện tích trần nhà là:\n$9 \\times 6 = 54\\text{ (m}^2)$\nDiện tích cần quét vôi là:\n$105 + 54 - 11,5 = 147,5\\text{ (m}^2)$\nb) Số tiền công quét vôi là:\n$147,5 \\times 25\\,000 = 3\\,687\\,500\\text{ (đồng)}$\nĐáp số:\na) $147,5\\text{ m}^2$;\nb) $3\\,687\\,500\\text{ đồng}$.", "a) 147,5 m²; b) 3 687 500 đồng", 5, 1.5),
            make_essay(5, "Một cái bể nước hình hộp chữ nhật có kích thước trong lòng bể: chiều dài $2,5\\text{ m}$, chiều rộng $1,6\\text{ m}$ và chiều cao $1,2\\text{ m}$. Hiện tại bể đang chứa nước cao $0,8\\text{ m}$.\na) Tính số lít nước đang có trong bể.\nb) Cần đổ thêm bao nhiêu lít nước nữa để đầy bể?", "Bài giải:\nĐổi: $2,5\\text{ m} = 25\\text{ dm}$; $1,6\\text{ m} = 16\\text{ dm}$; $0,8\\text{ m} = 8\\text{ dm}$; $1,2\\text{ m} = 12\\text{ dm}$.\na) Số lít nước đang có trong bể là:\n$25 \\times 16 \\times 8 = 3200\\text{ (dm}^3) = 3200\\text{ (lít)}$\nb) Chiều cao phần bể còn trống là:\n$12 - 8 = 4\\text{ (dm)}$\nSố lít nước cần đổ thêm là:\n$25 \\times 16 \\times 4 = 1600\\text{ (dm}^3) = 1600\\text{ (lít)}$\nĐáp số:\na) 3200 lít;\nb) 1600 lít.", "a) 3200 lít; b) 1600 lít", 5, 1.5),
            make_essay(6, "Một bể kính hình hộp chữ nhật có diện tích đáy là $200\\text{ cm}^2$ đang chứa nước. Người ta thả chìm vào bể một khối kim loại hình lập phương cạnh $6\\text{ cm}$. Hỏi mực nước trong bể dâng lên thêm bao nhiêu xăng-ti-mét?", "Bài giải:\nThể tích của khối kim loại hình lập phương là:\n$6 \\times 6 \\times 6 = 216\\text{ (cm}^3)$\nMực nước trong bể dâng thêm chiều cao là:\n$216 : 200 = 1,08\\text{ (cm)}$\nĐáp số: $1,08\\text{ cm}$.", "1,08 cm", 5, 1.0)
        ]
    }

    # --- Bài 44 - Đề 2 ---
    exams["th5_b44_test2"] = {
        "id": "th5_b44_test2",
        "lessonId": "th5_b44",
        "lessonNum": 44,
        "testNum": 2,
        "title": "Bài 44: Luyện tập chung Chủ đề 8 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 8",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình hộp chữ nhật có chiều dài $12\\text{ cm}$, rộng $8\\text{ cm}$, cao $5\\text{ cm}$. Diện tích xung quanh là:", ["$100\\text{ cm}^2$", "$200\\text{ cm}^2$", "$96\\text{ cm}^2$", "$392\\text{ cm}^2$"], 1, "$S_{xq} = (12 + 8) \\times 2 \\times 5 = 200\\text{ cm}^2$."),
            make_mc(2, "Tính thể tích của hình hộp chữ nhật có chiều dài $12\\text{ cm}$, rộng $8\\text{ cm}$, cao $5\\text{ cm}$:", ["$480\\text{ cm}^3$", "$240\\text{ cm}^3$", "$960\\text{ cm}^3$", "$500\\text{ cm}^3$"], 0, "$V = 12 \\times 8 \\times 5 = 480\\text{ cm}^3$."),
            make_mc(3, "Một hình lập phương có chu vi một mặt là $28\\text{ cm}$. Diện tích toàn phần của nó là:", ["$196\\text{ cm}^2$", "$294\\text{ cm}^2$", "$343\\text{ cm}^2$", "$245\\text{ cm}^2$"], 1, "Cạnh $28 : 4 = 7\\text{ cm}$. $S_{tp} = 7 \\times 7 \\times 6 = 294\\text{ cm}^2$."),
            make_mc(4, "Một hình lập phương có chu vi một mặt là $28\\text{ cm}$. Thể tích của hình lập phương đó là:", ["$343\\text{ cm}^3$", "$294\\text{ cm}^3$", "$196\\text{ cm}^3$", "$512\\text{ cm}^3$"], 0, "$V = 7 \\times 7 \\times 7 = 343\\text{ cm}^3$."),
            make_mc(5, "Một cái thùng không nắp hình lập phương có cạnh $0,8\\text{ m}$. Diện tích bề mặt ngoài là:", ["$2,56\\text{ m}^2$", "$3,2\\text{ m}^2$", "$3,84\\text{ m}^2$", "$1,92\\text{ m}^2$"], 1, "Thùng không nắp có 5 mặt: $0,8 \\times 0,8 \\times 5 = 3,2\\text{ m}^2$."),
            make_mc(6, "Bể bơi mini hình hộp chữ nhật có kích thước đáy $4\\text{ m} \\times 2,5\\text{ m}$, chứa nước sâu $0,8\\text{ m}$. Thể tích nước là:", ["$8\\text{ m}^3$", "$10\\text{ m}^3$", "$6,4\\text{ m}^3$", "$12\\text{ m}^3$"], 0, "$4 \\times 2,5 \\times 0,8 = 8\\text{ m}^3$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích toàn phần và thể tích của hình hộp chữ nhật có kích thước: dài $15\\text{ cm}$, rộng $10\\text{ cm}$, cao $8\\text{ cm}$.", "$S_{xq} = (15 + 10) \\times 2 \\times 8 = 400\\text{ (cm}^2)$\n$S_{2đáy} = 2 \\times (15 \\times 10) = 300\\text{ (cm}^2)$\n$S_{tp} = 400 + 300 = 700\\text{ (cm}^2)$\n$V = 15 \\times 10 \\times 8 = 1200\\text{ (cm}^3)$", "Stp = 700 cm²; V = 1200 cm³", 4, 1.0),
            make_essay(2, "Một khối gỗ hình lập phương có diện tích xung quanh là $144\\text{ dm}^2$. Tính thể tích của khối gỗ đó.", "Diện tích một mặt: $144 : 4 = 36\\text{ (dm}^2)$.\nVì $6 \\times 6 = 36$ nên cạnh khối gỗ là $6\\text{ dm}$.\nThể tích khối gỗ là:\n$6 \\times 6 \\times 6 = 216\\text{ (dm}^3)$\nĐáp số: $216\\text{ dm}^3$.", "216 dm³", 4, 1.0),
            make_essay(3, "Một cái thùng tôn hình hộp chữ nhật có diện tích xung quanh là $6,4\\text{ m}^2$, chiều cao $0,8\\text{ m}$. Tính chu vi đáy của chiếc thùng đó.", "Chu vi đáy của thùng tôn là:\n$6,4 : 0,8 = 8\\text{ (m)}$\nĐáp số: 8 m.", "8 m", 4, 1.0),
            make_essay(4, "Một người thợ đóng một chiếc hòm gỗ hình hộp chữ nhật có nắp dài $1,5\\text{ m}$, rộng $0,8\\text{ m}$ và cao $0,6\\text{ m}$. Người đó sơn cả mặt trong lẫn mặt ngoài của chiếc hòm đó.\na) Tính diện tích toàn phần bề mặt ngoài chiếc hòm.\nb) Biết tiền công sơn $1\\text{ m}^2$ cả vật liệu là $30\\,000$ đồng. Hỏi sơn toàn bộ hòm gỗ (cả trong lẫn ngoài) hết bao nhiêu tiền?", "Bài giải:\na) Diện tích xung quanh hòm gỗ là:\n$(1,5 + 0,8) \\times 2 \\times 0,6 = 2,76\\text{ (m}^2)$\nDiện tích hai mặt đáy là:\n$2 \\times (1,5 \\times 0,8) = 2,4\\text{ (m}^2)$\nDiện tích toàn phần bề mặt ngoài là:\n$2,76 + 2,4 = 5,16\\text{ (m}^2)$\nb) Diện tích cần sơn cả trong lẫn ngoài là:\n$5,16 \\times 2 = 10,32\\text{ (m}^2)$\nChi phí sơn chiếc hòm gỗ là:\n$10,32 \\times 30\\,000 = 309\\,600\\text{ (đồng)}$\nĐáp số:\na) $5,16\\text{ m}^2$;\nb) $309\\,600\\text{ đồng}$.", "a) 5,16 m²; b) 309 600 đồng", 5, 1.5),
            make_essay(5, "Một bể nước hình hộp chữ nhật có chiều dài $2\\text{ m}$, chiều rộng $1,5\\text{ m}$, chiều cao $1,4\\text{ m}$. Bể đang cạn nước. Người ta mở một vòi nước chảy vào bể mỗi phút được 35 lít.\na) Tính dung tích toàn bộ bể nước theo đơn vị lít.\nb) Sau khi mở vòi 1 giờ, mực nước trong bể cao bao nhiêu mét?", "Bài giải:\na) Thể tích của bể nước là:\n$2 \\times 1,5 \\times 1,4 = 4,2\\text{ (m}^3)$\nĐổi: $4,2\\text{ m}^3 = 4200\\text{ dm}^3 = 4200\\text{ lít}$.\nb) Đổi: $1\\text{ giờ} = 60\\text{ phút}$.\nLượng nước chảy vào bể sau 1 giờ là:\n$35 \\times 60 = 2100\\text{ (lít)} = 2,1\\text{ m}^3$\nDiện tích đáy bể nước là:\n$2 \\times 1,5 = 3\\text{ (m}^2)$\nMực nước trong bể cao là:\n$2,1 : 3 = 0,7\\text{ (m)}$\nĐáp số:\na) 4200 lít;\nb) 0,7 m.", "a) 4200 lít; b) 0,7 m", 5, 1.5),
            make_essay(6, "Một hình hộp chữ nhật có chiều dài gấp đôi chiều rộng và chiều cao bằng chiều rộng. Biết thể tích của hình hộp chữ nhật là $432\\text{ cm}^3$. Tính các kích thước dài, rộng, cao của hình hộp chữ nhật đó.", "Bài giải:\nGọi chiều rộng là $a$, thì chiều cao là $a$ và chiều dài là $a \\times 2$.\nThể tích hình hộp chữ nhật là:\n$(a \\times 2) \\times a \\times a = 2 \\times (a \\times a \\times a) = 432\\text{ (cm}^3)$\nSuy ra: $a \\times a \\times a = 432 : 2 = 216\\text{ (cm}^3)$.\nVì $6 \\times 6 \\times 6 = 216$ nên $a = 6\\text{ cm}$.\nVậy:\n- Chiều rộng: $6\\text{ cm}$;\n- Chiều cao: $6\\text{ cm}$;\n- Chiều dài: $6 \\times 2 = 12\\text{ cm}$.\nĐáp số: Dài 12 cm, Rộng 6 cm, Cao 6 cm.", "Dài 12 cm, Rộng 6 cm, Cao 6 cm", 5, 1.0)
        ]
    }

    # --- Bài 44 - Đề 3 ---
    exams["th5_b44_test3"] = {
        "id": "th5_b44_test3",
        "lessonId": "th5_b44",
        "lessonNum": 44,
        "testNum": 3,
        "title": "Bài 44: Luyện tập chung Chủ đề 8 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 8",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình lập phương có cạnh $0,4\\text{ m}$. Thể tích của nó là:", ["$0,064\\text{ m}^3$", "$0,64\\text{ m}^3$", "$0,16\\text{ m}^3$", "$0,016\\text{ m}^3$"], 0, "$0,4 \\times 0,4 \\times 0,4 = 0,064\\text{ m}^3$."),
            make_mc(2, "Tính diện tích toàn phần của hình lập phương có cạnh $0,4\\text{ m}$:", ["$0,96\\text{ m}^2$", "$0,64\\text{ m}^2$", "$0,16\\text{ m}^2$", "$1,44\\text{ m}^2$"], 0, "$0,4 \\times 0,4 \\times 6 = 0,96\\text{ m}^2$."),
            make_mc(3, "Một hình hộp chữ nhật có kích thước đáy $8\\text{ dm} \\times 6\\text{ dm}$ và thể tích $240\\text{ dm}^3$. Chiều cao của nó là:", ["4 dm", "5 dm", "6 dm", "8 dm"], 1, "$h = 240 : (8 \\times 6) = 5\\text{ dm}$."),
            make_mc(4, "Một lon sữa đặc hình trụ có đường kính đáy $8\\text{ cm}$. Chu vi đáy lon sữa là:", ["12,56 cm", "25,12 cm", "50,24 cm", "16 cm"], 1, "$8 \\times 3,14 = 25,12\\text{ cm}$."),
            make_mc(5, "Một khối gỗ hình hộp chữ nhật có $S_{xq} = 160\\text{ cm}^2$, diện tích 2 đáy là $120\\text{ cm}^2$. Diện tích toàn phần là:", ["$280\\text{ cm}^2$", "$220\\text{ cm}^2$", "$200\\text{ cm}^2$", "$320\\text{ cm}^2$"], 0, "$160 + 120 = 280\\text{ cm}^2$."),
            make_mc(6, "Bể nước chứa $3,5\\text{ m}^3$ nước, lấy ra $40\\%$ lượng nước. Số nước còn lại là:", ["1400 lít", "2100 lít", "1500 lít", "2000 lít"], 1, "$3500 \\times (100\\% - 40\\%) : 100 = 2100$ lít.")
        ],
        "part2": [
            make_essay(1, "Một hình hộp chữ nhật có chiều dài $20\\text{ cm}$, chiều rộng $12\\text{ cm}$, chiều cao $10\\text{ cm}$. Tính:\na) Diện tích xung quanh của hình hộp chữ nhật.\nb) Thể tích của hình hộp chữ nhật.", "a) $S_{xq} = (20 + 12) \\times 2 \\times 10 = 640\\text{ (cm}^2)$\nb) $V = 20 \\times 12 \\times 10 = 2400\\text{ (cm}^3)$", "a) 640 cm²; b) 2400 cm³", 4, 1.0),
            make_essay(2, "Một khối kim loại hình lập phương có thể tích $512\\text{ cm}^3$. Tính diện tích toàn phần của khối kim loại đó.", "Vì $8 \\times 8 \\times 8 = 512$ nên cạnh khối kim loại là $8\\text{ cm}$.\nDiện tích toàn phần là:\n$8 \\times 8 \\times 6 = 384\\text{ (cm}^2)$\nĐáp số: $384\\text{ cm}^2$.", "384 cm²", 4, 1.0),
            make_essay(3, "Một cái thùng tôn hình hộp chữ nhật có chiều dài $1,6\\text{ m}$, chiều rộng $1\\text{ m}$ và thể tích $1,28\\text{ m}^3$. Tính chiều cao của chiếc thùng tôn đó.", "Diện tích đáy thùng tôn là:\n$1,6 \\times 1 = 1,6\\text{ (m}^2)$\nChiều cao của thùng tôn là:\n$1,28 : 1,6 = 0,8\\text{ (m)}$\nĐáp số: 0,8 m.", "0,8 m", 4, 1.0),
            make_essay(4, "Một căn phòng dạng hình hộp chữ nhật có chiều dài $7,5\\text{ m}$, chiều rộng $4,5\\text{ m}$ và chiều cao $3,2\\text{ m}$. Người ta sơn tường và trần nhà phía trong phòng. Tổng diện tích cửa sổ và cửa ra vào là $8,5\\text{ m}^2$.\na) Tính diện tích cần sơn.\nb) Cứ mỗi mét vuông tường sơn hết $0,2\\text{ kg}$ sơn. Hỏi cần bao nhiêu ki-lô-gam sơn để sơn căn phòng đó?", "Bài giải:\na) Diện tích xung quanh phòng là:\n$(7,5 + 4,5) \\times 2 \\times 3,2 = 76,8\\text{ (m}^2)$\nDiện tích trần nhà là:\n$7,5 \\times 4,5 = 33,75\\text{ (m}^2)$\nDiện tích cần quét sơn là:\n$76,8 + 33,75 - 8,5 = 102,05\\text{ (m}^2)$\nb) Lượng sơn cần dùng là:\n$102,05 \\times 0,2 = 20,41\\text{ (kg)}$\nĐáp số:\na) $102,05\\text{ m}^2$;\nb) $20,41\\text{ kg}$.", "a) 102,05 m²; b) 20,41 kg", 5, 1.5),
            make_essay(5, "Một bể nước hình lập phương có cạnh $1,4\\text{ m}$. Khi bể đang cạn, người ta cho hai vòi nước cùng chảy vào bể. Vòi thứ nhất mỗi phút chảy được 30 lít, vòi thứ hai mỗi phút chảy được 34 lít.\na) Tính dung tích toàn bộ bể nước theo đơn vị lít.\nb) Sau bao lâu thì hai vòi chảy được lượng nước bằng $70\\%$ thể tích bể?", "Bài giải:\na) Thể tích của bể nước là:\n$1,4 \\times 1,4 \\times 1,4 = 2,744\\text{ (m}^3)$\nĐổi: $2,744\\text{ m}^3 = 2744\\text{ dm}^3 = 2744\\text{ lít}$.\nb) Lượng nước ứng với $70\\%$ thể tích bể là:\n$2744 \\times 70 : 100 = 1920,8\\text{ (lít)}$\nMỗi phút cả hai vòi cùng chảy được:\n$30 + 34 = 64\\text{ (lít)}$\nThời gian để hai vòi chảy được lượng nước trên là:\n$1920,8 : 64 = 30,0125\\text{ (phút)}$\n(hoặc nếu làm tròn: khoảng 30 phút).\nĐáp số:\na) 2744 lít;\nb) 30,0125 phút.", "a) 2744 lít; b) 30,0125 phút", 5, 1.5),
            make_essay(6, "Một bể cá hình hộp chữ nhật có chiều dài $60\\text{ cm}$, chiều rộng $40\\text{ cm}$ đang chứa nước cao $25\\text{ cm}$. Người ta thả vào bể một hòn đá cảnh thì mực nước trong bể dâng lên thành $28\\text{ cm}$. Tính thể tích của hòn đá cảnh đó theo đơn vị đề-xi-mét khối.", "Bài giải:\nChiều cao mực nước dâng thêm là:\n$28 - 25 = 3\\text{ (cm)}$\nThể tích của hòn đá cảnh là:\n$60 \\times 40 \\times 3 = 7200\\text{ (cm}^3)$\nĐổi: $7200\\text{ cm}^3 = 7,2\\text{ dm}^3$.\nĐáp số: $7,2\\text{ dm}^3$.", "7,2 dm³", 5, 1.0)
        ]
    }

    return exams
