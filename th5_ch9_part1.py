# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 9: SỐ ĐO THỜI GIAN. VẬN TỐC, QUÃNG ĐƯỜNG, THỜI GIAN (PHẦN 1: BÀI 45 ĐẾN BÀI 48)
Toán lớp 5 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 4 bài học x 3 đề độc lập = 12 đề thi (th5_b45_test1 -> th5_b48_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, question_text, options, correct, explanation):
    q_title = f"**Câu {qid}:** {question_text}" if not question_text.startswith("**Câu") else question_text
    return {
        "id": qid,
        "question": q_title,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question_text, solution, answer, lineCount=5, points=1.0):
    q_title = f"**Bài {qid}:** {question_text}" if not question_text.startswith("**Bài") else question_text
    return {
        "id": qid,
        "question": q_title,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_ch9_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 45: BẢNG ĐƠN VỊ ĐO THỜI GIAN
    # =========================================================================
    # --- Bài 45 - Đề 1 ---
    exams["th5_b45_test1"] = {
        "id": "th5_b45_test1",
        "lessonId": "th5_b45",
        "lessonNum": 45,
        "testNum": 1,
        "title": "Bài 45: Bảng đơn vị đo thời gian - Đề số 1",
        "topic": "Bảng đơn vị đo thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một thế kỉ bằng bao nhiêu năm?", ["10 năm", "50 năm", "100 năm", "1000 năm"], 2, "1 thế kỉ = 100 năm."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $2,5\\text{ giờ} = \\dots \\text{ phút}$ là:", ["120 phút", "150 phút", "250 phút", "130 phút"], 1, "2,5 x 60 = 150 phút."),
            make_mc(3, "Năm 1945 thuộc thế kỉ nào?", ["Thế kỉ XIX", "Thế kỉ XX", "Thế kỉ XXI", "Thế kỉ XVIII"], 1, "Năm 1945 thuộc thế kỉ hai mươi (XX)."),
            make_mc(4, "Một năm nhuận có bao nhiêu ngày?", ["365 ngày", "366 ngày", "364 ngày", "365,25 ngày"], 1, "Năm nhuận có 366 ngày (tháng 2 có 29 ngày)."),
            make_mc(5, "Đổi: $1\\text{ giờ } 15\\text{ phút} = \\dots \\text{ giờ}$:", ["1,15 giờ", "1,25 giờ", "1,5 giờ", "1,75 giờ"], 1, "15 phút = 15/60 giờ = 0,25 giờ, vậy bằng 1,25 giờ."),
            make_mc(6, "Số phút trong $\\frac{3}{4}\\text{ giờ}$ là:", ["30 phút", "40 phút", "45 phút", "50 phút"], 2, "60 x 3/4 = 45 phút.")
        ],
        "part2": [
            make_essay(1, "Viết số hoặc phân số thích hợp vào chỗ chấm:\na) $3\\text{ ngày } = \\dots \\text{ giờ}$\nb) $180\\text{ phút } = \\dots \\text{ giờ}$\nc) $2\\text{ phút } 30\\text{ giây } = \\dots \\text{ giây}$\nd) $36\\text{ tháng } = \\dots \\text{ năm}$", "a) $3 \\times 24 = 72\\text{ giờ}$\nb) $180 : 60 = 3\\text{ giờ}$\nc) $2 \\times 60 + 30 = 150\\text{ giây}$\nd) $36 : 12 = 3\\text{ năm}$", "a) 72; b) 3; c) 150; d) 3", 4, 1.0),
            make_essay(2, "Viết số đo thời gian sau dưới dạng số thập phân:\na) $2\\text{ giờ } 36\\text{ phút}$ (đơn vị giờ)\nb) $1\\text{ phút } 12\\text{ giây}$ (đơn vị phút)", "a) $36\\text{ phút} = 36 : 60 = 0,6\\text{ giờ} \\Rightarrow 2\\text{ giờ } 36\\text{ phút} = 2,6\\text{ giờ}$.\nb) $12\\text{ giây} = 12 : 60 = 0,2\\text{ phút} \\Rightarrow 1\\text{ phút } 12\\text{ giây} = 1,2\\text{ phút}$.", "a) 2,6 giờ; b) 1,2 phút", 4, 1.0),
            make_essay(3, "Chiến thắng Điện Biên Phủ diễn ra vào năm 1954. Hỏi năm đó thuộc thế kỉ nào? Tính từ năm đó đến nay (năm 2026) đã được bao nhiêu năm?", "Năm 1954 thuộc thế kỉ hai mươi (thế kỉ XX).\nSố năm từ năm 1954 đến năm 2026 là:\n$2026 - 1954 = 72\\text{ (năm)}$.", "Thế kỉ XX; 72 năm", 4, 1.0),
            make_essay(4, "Một người làm một sản phẩm hết $1\\text{ giờ } 15\\text{ phút}$. Hỏi người đó làm 4 sản phẩm như thế hết bao nhiêu thời gian?", "Đổi: $1\\text{ giờ } 15\\text{ phút} = 75\\text{ phút}$.\nThời gian làm 4 sản phẩm là:\n$75 \\times 4 = 300\\text{ (phút)}$.\nĐổi sang giờ: $300 : 60 = 5\\text{ giờ}$.", "5 giờ", 5, 1.5),
            make_essay(5, "Một máy bay bay từ Hà Nội lúc 8 giờ 30 phút và đến Thành phố Hồ Chí Minh lúc 10 giờ 45 phút. Giữa đường máy bay bay liên tục không nghỉ. Hỏi chuyến bay kéo dài bao nhiêu giờ, bao nhiêu phút? Hãy đổi kết quả đó ra số thập phân với đơn vị giờ.", "Thời gian chuyến bay kéo dài là:\n$10\\text{ giờ } 45\\text{ phút} - 8\\text{ giờ } 30\\text{ phút} = 2\\text{ giờ } 15\\text{ phút}$.\nĐổi $15\\text{ phút} = 15 : 60 = 0,25\\text{ giờ}$.\nVậy $2\\text{ giờ } 15\\text{ phút} = 2,25\\text{ giờ}$.", "2 giờ 15 phút (hoặc 2,25 giờ)", 5, 1.5),
            make_essay(6, "Bác An làm việc ở cơ quan từ 8 giờ sáng đến 11 giờ 30 phút trưa, buổi chiều từ 13 giờ 30 phút đến 17 giờ. Hỏi trong một ngày bác An làm việc ở cơ quan tất cả bao nhiêu giờ?", "Thời gian làm việc buổi sáng là: $11\\text{ giờ } 30\\text{ phút} - 8\\text{ giờ} = 3\\text{ giờ } 30\\text{ phút} = 3,5\\text{ giờ}$.\nThời gian làm việc buổi chiều là: $17\\text{ giờ} - 13\\text{ giờ } 30\\text{ phút} = 3\\text{ giờ } 30\\text{ phút} = 3,5\\text{ giờ}$.\nTổng thời gian làm việc trong ngày là: $3,5 + 3,5 = 7\\text{ giờ}$.", "7 giờ", 4, 1.0)
        ]
    }

    # --- Bài 45 - Đề 2 ---
    exams["th5_b45_test2"] = {
        "id": "th5_b45_test2",
        "lessonId": "th5_b45",
        "lessonNum": 45,
        "testNum": 2,
        "title": "Bài 45: Bảng đơn vị đo thời gian - Đề số 2",
        "topic": "Bảng đơn vị đo thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Năm 1010 Lý Thái Tổ dời đô về Thăng Long. Năm đó thuộc thế kỉ nào?", ["Thế kỉ X", "Thế kỉ XI", "Thế kỉ XII", "Thế kỉ IX"], 1, "Năm 1010 thuộc thế kỉ mười một (XI)."),
            make_mc(2, "Đổi $3,25\\text{ giờ} = \\dots \\text{ giờ } \\dots \\text{ phút}$:", ["3 giờ 25 phút", "3 giờ 15 phút", "3 giờ 20 phút", "3 giờ 30 phút"], 1, "0,25 x 60 = 15 phút => 3 giờ 15 phút."),
            make_mc(3, "Một tuần lễ có bao nhiêu giờ?", ["168 giờ", "144 giờ", "120 giờ", "180 giờ"], 0, "7 x 24 = 168 giờ."),
            make_mc(4, "Các tháng nào dưới đây đều có 31 ngày?", [
                "Tháng 1, tháng 3, tháng 5, tháng 7",
                "Tháng 4, tháng 6, tháng 9, tháng 11",
                "Tháng 2, tháng 4, tháng 6, tháng 8",
                "Tháng 7, tháng 8, tháng 9, tháng 10"
            ], 0, "Các tháng có 31 ngày là: 1, 3, 5, 7, 8, 10, 12."),
            make_mc(5, "Đổi: $2\\text{ giờ } 45\\text{ phút} = \\dots \\text{ giờ}$:", ["2,45 giờ", "2,75 giờ", "2,5 giờ", "2,8 giờ"], 1, "45/60 = 0,75 giờ => 2,75 giờ."),
            make_mc(6, "Số giây trong $\\frac{2}{5}\\text{ phút}$ là:", ["24 giây", "20 giây", "12 giây", "30 giây"], 0, "60 x 2/5 = 24 giây.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $5\\text{ năm} = \\dots \\text{ tháng}$\nb) $4\\text{ ngày } 12\\text{ giờ} = \\dots \\text{ giờ}$\nc) $300\\text{ giây} = \\dots \\text{ phút}$\nd) $\\frac{1}{2}\\text{ thế kỉ} = \\dots \\text{ năm}$", "a) $5 \\times 12 = 60\\text{ tháng}$\nb) $4 \\times 24 + 12 = 108\\text{ giờ}$\nc) $300 : 60 = 5\\text{ phút}$\nd) $100 : 2 = 50\\text{ năm}$", "a) 60; b) 108; c) 5; d) 50", 4, 1.0),
            make_essay(2, "Viết các số đo sau dưới dạng số thập phân có đơn vị là giờ:\na) $3\\text{ giờ } 18\\text{ phút}$\nb) $1\\text{ giờ } 48\\text{ phút}$", "a) $18\\text{ phút} = 18 : 60 = 0,3\\text{ giờ} \\Rightarrow 3,3\\text{ giờ}$.\nb) $48\\text{ phút} = 48 : 60 = 0,8\\text{ giờ} \\Rightarrow 1,8\\text{ giờ}$.", "a) 3,3 giờ; b) 1,8 giờ", 4, 1.0),
            make_essay(3, "Bác Hồ đọc Tuyên ngôn Độc lập khai sinh ra nước Việt Nam Dân chủ Cộng hòa vào ngày 2 tháng 9 năm 1945. Hỏi ngày đó thuộc thế kỉ nào? Tính đến ngày 2 tháng 9 năm 2025 thì tròn bao nhiêu năm?", "Năm 1945 thuộc thế kỉ hai mươi (thế kỉ XX).\nTính đến năm 2025 tròn số năm là: $2025 - 1945 = 80\\text{ (năm)}$.", "Thế kỉ XX; 80 năm", 4, 1.0),
            make_essay(4, "Một người thợ may một cái áo hết $1\\text{ giờ } 30\\text{ phút}$, may một cái quần hết $1\\text{ giờ } 15\\text{ phút}$. Hỏi người đó may 3 bộ quần áo như thế hết tất cả bao nhiêu thời gian?", "Thời gian may một bộ quần áo (gồm 1 áo và 1 quần) là:\n$1\\text{ giờ } 30\\text{ phút} + 1\\text{ giờ } 15\\text{ phút} = 2\\text{ giờ } 45\\text{ phút} = 2,75\\text{ giờ}$.\nThời gian may 3 bộ quần áo là:\n$2,75 \\times 3 = 8,25\\text{ giờ} = 8\\text{ giờ } 15\\text{ phút}$.", "8 giờ 15 phút (hoặc 8,25 giờ)", 5, 1.5),
            make_essay(5, "Một tàu hỏa khởi hành từ ga A lúc 19 giờ 45 phút tối hôm trước và đến ga B lúc 6 giờ 15 phút sáng hôm sau. Hỏi tàu hỏa đó đã chạy từ A đến B hết bao nhiêu thời gian?", "Từ 19 giờ 45 phút đến 24 giờ cùng ngày hết:\n$24\\text{ giờ} - 19\\text{ giờ } 45\\text{ phút} = 4\\text{ giờ } 15\\text{ phút}$.\nTừ 0 giờ đến 6 giờ 15 phút sáng hôm sau hết: $6\\text{ giờ } 15\\text{ phút}$.\nTổng thời gian tàu chạy là:\n$4\\text{ giờ } 15\\text{ phút} + 6\\text{ giờ } 15\\text{ phút} = 10\\text{ giờ } 30\\text{ phút} = 10,5\\text{ giờ}$.", "10 giờ 30 phút (hay 10,5 giờ)", 5, 1.5),
            make_essay(6, "Bình đi học từ nhà lúc 6 giờ 45 phút và đến trường lúc 7 giờ 10 phút. Trên đường đi Bình dừng lại mua xôi hết 5 phút. Hỏi thời gian thực tế Bình đi trên đường từ nhà đến trường là bao nhiêu phút?", "Thời gian từ lúc xuất phát đến lúc tới trường là:\n$7\\text{ giờ } 10\\text{ phút} - 6\\text{ giờ } 45\\text{ phút} = 25\\text{ phút}$.\nThời gian thực tế đi trên đường là:\n$25 - 5 = 20\\text{ (phút)}$.", "20 phút", 4, 1.0)
        ]
    }

    # --- Bài 45 - Đề 3 ---
    exams["th5_b45_test3"] = {
        "id": "th5_b45_test3",
        "lessonId": "th5_b45",
        "lessonNum": 45,
        "testNum": 3,
        "title": "Bài 45: Bảng đơn vị đo thời gian - Đề số 3",
        "topic": "Bảng đơn vị đo thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Năm 2024 là năm nhuận. Năm nhuận tiếp theo sau năm 2024 là năm nào?", ["Năm 2026", "Năm 2028", "Năm 2030", "Năm 2025"], 1, "Cứ 4 năm lại có một năm nhuận: 2024 + 4 = 2028."),
            make_mc(2, "Đổi: $1,75\\text{ giờ} = \\dots \\text{ phút}$:", ["105 phút", "175 phút", "75 phút", "115 phút"], 0, "1,75 x 60 = 105 phút."),
            make_mc(3, "Thế kỉ XXI bắt đầu từ năm nào đến hết năm nào?", [
                "Từ năm 2000 đến hết năm 2099",
                "Từ năm 2001 đến hết năm 2100",
                "Từ năm 1901 đến hết năm 2000",
                "Từ năm 2001 đến hết năm 2099"
            ], 1, "Thế kỉ 21 bắt đầu từ năm 2001 đến hết năm 2100."),
            make_mc(4, "Đổi: $150\\text{ giây} = \\dots \\text{ phút}$:", ["2,5 phút", "2 phút 50 giây", "1,5 phút", "2,3 phút"], 0, "150 : 60 = 2,5 phút."),
            make_mc(5, "Số ngày trong quý I của một năm không nhuận là:", ["90 ngày", "91 ngày", "89 ngày", "92 ngày"], 0, "Quý I gồm tháng 1 (31 ngày), tháng 2 (28 ngày), tháng 3 (31 ngày): 31 + 28 + 31 = 90 ngày."),
            make_mc(6, "Đổi $2\\text{ ngày } 6\\text{ giờ} = \\dots \\text{ ngày}$:", ["2,25 ngày", "2,6 ngày", "2,4 ngày", "2,5 ngày"], 0, "6 : 24 = 0,25 ngày => 2,25 ngày.")
        ],
        "part2": [
            make_essay(1, "Viết số hoặc phân số thích hợp vào chỗ chấm:\na) $2,5\\text{ ngày} = \\dots \\text{ giờ}$\nb) $48\\text{ tháng} = \\dots \\text{ năm}$\nc) $72\\text{ giây} = \\dots \\text{ phút}$\nd) $\\frac{1}{4}\\text{ giờ} = \\dots \\text{ phút}$", "a) $2,5 \\times 24 = 60\\text{ giờ}$\nb) $48 : 12 = 4\\text{ năm}$\nc) $72 : 60 = 1,2\\text{ phút}$\nd) $60 : 4 = 15\\text{ phút}$", "a) 60; b) 4; c) 1,2; d) 15", 4, 1.0),
            make_essay(2, "Viết các số đo sau dưới dạng số thập phân với đơn vị là giờ:\na) $4\\text{ giờ } 24\\text{ phút}$\nb) $3\\text{ giờ } 15\\text{ phút}$", "a) $24\\text{ phút} = 24 : 60 = 0,4\\text{ giờ} \\Rightarrow 4,4\\text{ giờ}$.\nb) $15\\text{ phút} = 15 : 60 = 0,25\\text{ giờ} \\Rightarrow 3,25\\text{ giờ}$.", "a) 4,4 giờ; b) 3,25 giờ", 4, 1.0),
            make_essay(3, "Bà Triệu lãnh đạo cuộc khởi nghĩa chống quân Đông Ngô vào năm 248. Hỏi năm đó thuộc thế kỉ nào? Tính đến nay (năm 2026) đã được bao nhiêu năm?", "Năm 248 thuộc thế kỉ thứ ba (thế kỉ III).\nTính đến năm 2026 đã được: $2026 - 248 = 1778\\text{ (năm)}$.", "Thế kỉ III; 1778 năm", 4, 1.0),
            make_essay(4, "Một công nhân may mỗi chiếc khẩu trang hết 1 phút 15 giây. Hỏi trong một buổi làm việc 3 giờ (không nghỉ giải lao), người đó may được bao nhiêu chiếc khẩu trang?", "Đổi: 1 phút 15 giây = 75 giây.\n$3\\text{ giờ} = 3 \\times 3600 = 10 800\\text{ giây}$.\nSố chiếc khẩu trang may được là:\n$10 800 : 75 = 144$ (chiếc khẩu trang).", "144 chiếc khẩu trang", 5, 1.5),
            make_essay(5, "Một trận bóng đá bắt đầu lúc 15 giờ 15 phút. Trận đấu gồm 2 hiệp, mỗi hiệp 45 phút và nghỉ giữa hai hiệp 15 phút. Ngoài ra có thêm 5 phút bù giờ cho cả trận đấu. Hỏi trận bóng đá đó kết thúc vào lúc mấy giờ?", "Tổng thời gian của cả trận đấu (kể cả nghỉ và bù giờ) là:\n$45 \\times 2 + 15 + 5 = 110\\text{ (phút)} = 1\\text{ giờ } 50\\text{ phút}$.\nThời điểm trận đấu kết thúc là:\n$15\\text{ giờ } 15\\text{ phút} + 1\\text{ giờ } 50\\text{ phút} = 16\\text{ giờ } 65\\text{ phút} = 17\\text{ giờ } 5\\text{ phút}$.", "17 giờ 5 phút", 5, 1.5),
            make_essay(6, "Bạn Lan dành thời gian trong một ngày như sau: học ở trường 4 giờ 30 phút, tự học ở nhà 2 giờ, ngủ 8 giờ 30 phút, còn lại là các hoạt động khác. Hỏi các hoạt động khác chiếm bao nhiêu giờ?", "Một ngày có 24 giờ.\nTổng thời gian học ở trường, tự học và ngủ là:\n$4\\text{ giờ } 30\\text{ phút} + 2\\text{ giờ} + 8\\text{ giờ } 30\\text{ phút} = 15\\text{ giờ}$.\nThời gian cho các hoạt động khác là:\n$24 - 15 = 9\\text{ (giờ)}$.", "9 giờ", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 46: CỘNG, TRỪ SỐ ĐO THỜI GIAN
    # =========================================================================
    # --- Bài 46 - Đề 1 ---
    exams["th5_b46_test1"] = {
        "id": "th5_b46_test1",
        "lessonId": "th5_b46",
        "lessonNum": 46,
        "testNum": 1,
        "title": "Bài 46: Cộng, trừ số đo thời gian - Đề số 1",
        "topic": "Cộng, trừ số đo thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $3\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 35\\text{ phút}$ là:", ["5 giờ 50 phút", "5 giờ 40 phút", "6 giờ 10 phút", "5 giờ 45 phút"], 0, "3h + 2h = 5h; 15p + 35p = 50p => 5 giờ 50 phút."),
            make_mc(2, "Kết quả của phép tính $5\\text{ giờ } 20\\text{ phút} - 2\\text{ giờ } 45\\text{ phút}$ là:", ["2 giờ 35 phút", "3 giờ 35 phút", "2 giờ 45 phút", "3 giờ 25 phút"], 0, "5h 20p = 4h 80p - 2h 45p = 2 giờ 35 phút."),
            make_mc(3, "Tính: $4\\text{ phút } 18\\text{ giây} + 5\\text{ phút } 45\\text{ giây}$ bằng:", ["9 phút 63 giây", "10 phút 3 giây", "10 phút 13 giây", "9 phút 3 giây"], 1, "9 phút 63 giây = 10 phút 3 giây."),
            make_mc(4, "Một người đi từ A lúc 7 giờ 15 phút và đến B lúc 9 giờ. Thời gian người đó đi từ A đến B là:", ["1 giờ 45 phút", "2 giờ 15 phút", "1 giờ 15 phút", "2 giờ"], 0, "9 giờ - 7 giờ 15 phút = 8 giờ 60 phút - 7 giờ 15 phút = 1 giờ 45 phút."),
            make_mc(5, "Tính: $12\\text{ ngày } 8\\text{ giờ} - 7\\text{ ngày } 15\\text{ giờ}$ bằng:", ["4 ngày 17 giờ", "5 ngày 17 giờ", "4 ngày 7 giờ", "5 ngày 7 giờ"], 0, "11 ngày 32 giờ - 7 ngày 15 giờ = 4 ngày 17 giờ."),
            make_mc(6, "Giá trị của biểu thức $6\\text{ giờ} - 2\\text{ giờ } 18\\text{ phút}$ là:", ["3 giờ 42 phút", "4 giờ 42 phút", "3 giờ 32 phút", "4 giờ 18 phút"], 0, "5 giờ 60 phút - 2 giờ 18 phút = 3 giờ 42 phút.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $4\\text{ giờ } 35\\text{ phút} + 3\\text{ giờ } 42\\text{ phút}$\nb) $8\\text{ phút } 15\\text{ giây} - 3\\text{ phút } 48\\text{ giây}$", "a) $4\\text{ giờ } 35\\text{ phút} + 3\\text{ giờ } 42\\text{ phút} = 7\\text{ giờ } 77\\text{ phút} = 8\\text{ giờ } 17\\text{ phút}$.\nb) $8\\text{ phút } 15\\text{ giây} - 3\\text{ phút } 48\\text{ giây} = 7\\text{ phút } 75\\text{ giây} - 3\\text{ phút } 48\\text{ giây} = 4\\text{ phút } 27\\text{ giây}$.", "a) 8 giờ 17 phút; b) 4 phút 27 giây", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\n$A = (5\\text{ giờ } 20\\text{ phút} + 3\\text{ giờ } 45\\text{ phút}) - 4\\text{ giờ } 30\\text{ phút}$", "Tính trong ngoặc:\n$5\\text{ giờ } 20\\text{ phút} + 3\\text{ giờ } 45\\text{ phút} = 8\\text{ giờ } 65\\text{ phút} = 9\\text{ giờ } 5\\text{ phút}$.\nThực hiện phép trừ:\n$9\\text{ giờ } 5\\text{ phút} - 4\\text{ giờ } 30\\text{ phút} = 8\\text{ giờ } 65\\text{ phút} - 4\\text{ giờ } 30\\text{ phút} = 4\\text{ giờ } 35\\text{ phút}$.", "A = 4 giờ 35 phút", 4, 1.0),
            make_essay(3, "Tìm $x$, biết: $x + 2\\text{ giờ } 45\\text{ phút} = 6\\text{ giờ } 15\\text{ phút}$.", "$x = 6\\text{ giờ } 15\\text{ phút} - 2\\text{ giờ } 45\\text{ phút}$\n$x = 5\\text{ giờ } 75\\text{ phút} - 2\\text{ giờ } 45\\text{ phút} = 3\\text{ giờ } 30\\text{ phút}$.", "x = 3 giờ 30 phút", 4, 1.0),
            make_essay(4, "Một người đi xe đạp từ A đến B. Người đó khởi hành lúc 6 giờ 30 phút, đi được 1 giờ 45 phút thì nghỉ giải lao 20 phút rồi đi tiếp 1 giờ 15 phút nữa thì tới B. Hỏi người đó đến B lúc mấy giờ?", "Tổng thời gian đi và nghỉ là:\n$1\\text{ giờ } 45\\text{ phút} + 20\\text{ phút} + 1\\text{ giờ } 15\\text{ phút} = 3\\text{ giờ } 20\\text{ phút}$.\nThời điểm người đó đến B là:\n$6\\text{ giờ } 30\\text{ phút} + 3\\text{ giờ } 20\\text{ phút} = 9\\text{ giờ } 50\\text{ phút}$.", "9 giờ 50 phút", 5, 1.5),
            make_essay(5, "Trong một cuộc thi chạy tiếp sức, đội thứ nhất hoàn thành phần thi trong 8 phút 45 giây. Đội thứ hai hoàn thành nhanh hơn đội thứ nhất 38 giây. Đội thứ ba hoàn thành chậm hơn đội thứ hai 52 giây. Hỏi đội thứ ba hoàn thành phần thi trong bao lâu?", "Thời gian đội thứ hai chạy là:\n$8\\text{ phút } 45\\text{ giây} - 38\\text{ giây} = 8\\text{ phút } 7\\text{ giây}$.\nThời gian đội thứ ba chạy là:\n$8\\text{ phút } 7\\text{ giây} + 52\\text{ giây} = 8\\text{ phút } 59\\text{ giây}$.", "8 phút 59 giây", 5, 1.5),
            make_essay(6, "Một người thợ làm 2 ca làm việc. Ca thứ nhất làm từ 7 giờ 30 phút đến 11 giờ 45 phút. Ca thứ hai làm từ 13 giờ 15 phút đến 17 giờ. Hỏi cả hai ca người đó làm việc tất cả bao nhiêu thời gian?", "Thời gian ca 1 là: $11\\text{ giờ } 45\\text{ phút} - 7\\text{ giờ } 30\\text{ phút} = 4\\text{ giờ } 15\\text{ phút}$.\nThời gian ca 2 là: $17\\text{ giờ} - 13\\text{ giờ } 30\\text{ phút} = 3\\text{ giờ } 30\\text{ phút}$.\nTổng thời gian là: $4\\text{ giờ } 15\\text{ phút} + 3\\text{ giờ } 30\\text{ phút} = 7\\text{ giờ } 45\\text{ phút}$.", "7 giờ 45 phút", 4, 1.0)
        ]
    }

    # --- Bài 46 - Đề 2 ---
    exams["th5_b46_test2"] = {
        "id": "th5_b46_test2",
        "lessonId": "th5_b46",
        "lessonNum": 46,
        "testNum": 2,
        "title": "Bài 46: Cộng, trừ số đo thời gian - Đề số 2",
        "topic": "Cộng, trừ số đo thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $4\\text{ năm } 7\\text{ tháng} + 3\\text{ năm } 8\\text{ tháng}$ bằng:", ["8 năm 3 tháng", "7 năm 15 tháng", "8 năm 5 tháng", "7 năm 3 tháng"], 0, "7 năm 15 tháng = 8 năm 3 tháng."),
            make_mc(2, "Tính: $7\\text{ ngày } 6\\text{ giờ} - 4\\text{ ngày } 14\\text{ giờ}$ bằng:", ["2 ngày 16 giờ", "3 ngày 16 giờ", "2 ngày 8 giờ", "3 ngày 8 giờ"], 0, "6 ngày 30 giờ - 4 ngày 14 giờ = 2 ngày 16 giờ."),
            make_mc(3, "Kết quả của $9\\text{ phút } 25\\text{ giây} - 4\\text{ phút } 40\\text{ giây}$ là:", ["4 phút 45 giây", "5 phút 45 giây", "4 phút 15 giây", "5 phút 15 giây"], 0, "8 phút 85 giây - 4 phút 40 giây = 4 phút 45 giây."),
            make_mc(4, "Một ô tô đi từ tỉnh M lúc 8 giờ 10 phút và đến tỉnh N lúc 11 giờ 25 phút. Thời gian ô tô đi là:", ["3 giờ 15 phút", "3 giờ 35 phút", "2 giờ 15 phút", "3 giờ"], 0, "11 giờ 25 phút - 8 giờ 10 phút = 3 giờ 15 phút."),
            make_mc(5, "Biết $x - 3\\text{ giờ } 20\\text{ phút} = 4\\text{ giờ } 50\\text{ phút}$. Giá trị của $x$ là:", ["8 giờ 10 phút", "7 giờ 10 phút", "8 giờ 20 phút", "7 giờ 50 phút"], 0, "x = 4h 50p + 3h 20p = 7h 70p = 8 giờ 10 phút."),
            make_mc(6, "Giá trị của $15\\text{ phút} - 8\\text{ phút } 35\\text{ giây}$ là:", ["6 phút 25 giây", "7 phút 25 giây", "6 phút 35 giây", "7 phút 35 giây"], 0, "14 phút 60 giây - 8 phút 35 giây = 6 phút 25 giây.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $6\\text{ ngày } 15\\text{ giờ} + 5\\text{ ngày } 18\\text{ giờ}$\nb) $14\\text{ giờ } 20\\text{ phút} - 8\\text{ giờ } 45\\text{ phút}$", "a) $6\\text{ ngày } 15\\text{ giờ} + 5\\text{ ngày } 18\\text{ giờ} = 11\\text{ ngày } 33\\text{ giờ} = 12\\text{ ngày } 9\\text{ giờ}$.\nb) $14\\text{ giờ } 20\\text{ phút} - 8\\text{ giờ } 45\\text{ phút} = 13\\text{ giờ } 80\\text{ phút} - 8\\text{ giờ } 45\\text{ phút} = 5\\text{ giờ } 35\\text{ phút}$.", "a) 12 ngày 9 giờ; b) 5 giờ 35 phút", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$B = 3\\text{ giờ } 45\\text{ phút} + 2\\text{ giờ } 30\\text{ phút} + 4\\text{ giờ } 15\\text{ phút}$", "$B = (3\\text{ giờ } 45\\text{ phút} + 4\\text{ giờ } 15\\text{ phút}) + 2\\text{ giờ } 30\\text{ phút}$\n$B = 8\\text{ giờ} + 2\\text{ giờ } 30\\text{ phút} = 10\\text{ giờ } 30\\text{ phút}$.", "B = 10 giờ 30 phút", 4, 1.0),
            make_essay(3, "Tìm $y$, biết: $8\\text{ giờ } 10\\text{ phút} - y = 3\\text{ giờ } 45\\text{ phút}$.", "$y = 8\\text{ giờ } 10\\text{ phút} - 3\\text{ giờ } 45\\text{ phút}$\n$y = 7\\text{ giờ } 70\\text{ phút} - 3\\text{ giờ } 45\\text{ phút} = 4\\text{ giờ } 25\\text{ phút}$.", "y = 4 giờ 25 phút", 4, 1.0),
            make_essay(4, "Một đoàn tàu xuất phát từ ga Hà Nội lúc 22 giờ 15 phút đêm hôm trước và đến ga Vinh lúc 4 giờ 30 phút sáng hôm sau. Hỏi thời gian đoàn tàu chạy từ Hà Nội đến Vinh là bao nhiêu giờ, bao nhiêu phút?", "Thời gian tàu chạy trong đêm hôm trước (từ 22h15 đến 24h) là:\n$24\\text{ giờ} - 22\\text{ giờ } 15\\text{ phút} = 1\\text{ giờ } 45\\text{ phút}$.\nThời gian chạy sáng hôm sau là: $4\\text{ giờ } 30\\text{ phút}$.\nTổng thời gian tàu chạy là:\n$1\\text{ giờ } 45\\text{ phút} + 4\\text{ giờ } 30\\text{ phút} = 5\\text{ giờ } 75\\text{ phút} = 6\\text{ giờ } 15\\text{ phút}$.", "6 giờ 15 phút", 5, 1.5),
            make_essay(5, "Bạn An làm xong bài tập Toán hết 45 phút 20 giây. Bạn Bình làm xong bài tập đó nhanh hơn bạn An 8 phút 35 giây. Hỏi cả hai bạn làm xong bài tập hết tất cả bao nhiêu thời gian?", "Thời gian bạn Bình làm bài tập là:\n$45\\text{ phút } 20\\text{ giây} - 8\\text{ phút } 35\\text{ giây} = 44\\text{ phút } 80\\text{ giây} - 8\\text{ phút } 35\\text{ giây} = 36\\text{ phút } 45\\text{ giây}$.\nTổng thời gian cả hai bạn làm là:\n$45\\text{ phút } 20\\text{ giây} + 36\\text{ phút } 45\\text{ giây} = 81\\text{ phút } 65\\text{ giây} = 82\\text{ phút } 5\\text{ giây} = 1\\text{ giờ } 22\\text{ phút } 5\\text{ giây}$.", "1 giờ 22 phút 5 giây (hoặc 82 phút 5 giây)", 5, 1.5),
            make_essay(6, "Một người đi xe máy khởi hành lúc 8 giờ, đến nơi lúc 11 giờ. Giữa đường người đó nghỉ uống nước 25 phút. Tính thời gian thực tế người đó đi trên đường.", "Tổng thời gian từ lúc đi đến lúc đến nơi là:\n$11\\text{ giờ} - 8\\text{ giờ} = 3\\text{ giờ}$.\nThời gian thực tế đi trên đường là:\n$3\\text{ giờ} - 25\\text{ phút} = 2\\text{ giờ } 60\\text{ phút} - 25\\text{ phút} = 2\\text{ giờ } 35\\text{ phút}$.", "2 giờ 35 phút", 4, 1.0)
        ]
    }

    # --- Bài 46 - Đề 3 ---
    exams["th5_b46_test3"] = {
        "id": "th5_b46_test3",
        "lessonId": "th5_b46",
        "lessonNum": 46,
        "testNum": 3,
        "title": "Bài 46: Cộng, trừ số đo thời gian - Đề số 3",
        "topic": "Cộng, trừ số đo thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $5\\text{ giờ } 45\\text{ phút} + 3\\text{ giờ } 30\\text{ phút}$ bằng:", ["9 giờ 15 phút", "8 giờ 75 phút", "9 giờ 25 phút", "8 giờ 15 phút"], 0, "8h 75p = 9 giờ 15 phút."),
            make_mc(2, "Tính: $10\\text{ phút } 12\\text{ giây} - 6\\text{ phút } 35\\text{ giây}$ bằng:", ["3 phút 37 giây", "4 phút 37 giây", "3 phút 47 giây", "4 phút 23 giây"], 0, "9p 72s - 6p 35s = 3 phút 37 giây."),
            make_mc(3, "Một ô tô rời bến lúc 13 giờ 45 phút và đến nơi lúc 16 giờ 10 phút. Thời gian chạy của ô tô là:", ["2 giờ 25 phút", "3 giờ 25 phút", "2 giờ 35 phút", "3 giờ 35 phút"], 0, "16h 10p - 13h 45p = 15h 70p - 13h 45p = 2 giờ 25 phút."),
            make_mc(4, "Tính: $8\\text{ năm } 4\\text{ tháng} - 3\\text{ năm } 9\\text{ tháng}$ bằng:", ["4 năm 7 tháng", "5 năm 7 tháng", "4 năm 5 tháng", "5 năm 5 tháng"], 0, "7 năm 16 tháng - 3 năm 9 tháng = 4 năm 7 tháng."),
            make_mc(5, "Biết $x + 1\\text{ giờ } 40\\text{ phút} = 4\\text{ giờ}$. Giá trị của $x$ là:", ["2 giờ 20 phút", "3 giờ 20 phút", "2 giờ 40 phút", "3 giờ"], 0, "3h 60p - 1h 40p = 2 giờ 20 phút."),
            make_mc(6, "Giá trị của biểu thức $5\\text{ giờ } 10\\text{ phút} - 2\\text{ giờ } 35\\text{ phút} + 1\\text{ giờ } 25\\text{ phút}$ là:", ["4 giờ", "3 giờ 50 phút", "4 giờ 10 phút", "3 giờ"], 0, "2h 35p + 1h 25p = 4 giờ.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $7\\text{ giờ } 28\\text{ phút} + 4\\text{ giờ } 45\\text{ phút}$\nb) $15\\text{ phút } 10\\text{ giây} - 8\\text{ phút } 36\\text{ giây}$", "a) $7\\text{ giờ } 28\\text{ phút} + 4\\text{ giờ } 45\\text{ phút} = 11\\text{ giờ } 73\\text{ phút} = 12\\text{ giờ } 13\\text{ phút}$.\nb) $15\\text{ phút } 10\\text{ giây} - 8\\text{ phút } 36\\text{ giây} = 14\\text{ phút } 70\\text{ giây} - 8\\text{ phút } 36\\text{ giây} = 6\\text{ phút } 34\\text{ giây}$.", "a) 12 giờ 13 phút; b) 6 phút 34 giây", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$C = 7\\text{ giờ } 15\\text{ phút} - 2\\text{ giờ } 40\\text{ phút} - 1\\text{ giờ } 20\\text{ phút}$", "$C = 7\\text{ giờ } 15\\text{ phút} - (2\\text{ giờ } 40\\text{ phút} + 1\\text{ giờ } 20\\text{ phút})$\n$C = 7\\text{ giờ } 15\\text{ phút} - 4\\text{ giờ} = 3\\text{ giờ } 15\\text{ phút}$.", "C = 3 giờ 15 phút", 4, 1.0),
            make_essay(3, "Tìm $x$, biết: $x - 3\\text{ ngày } 14\\text{ giờ} = 2\\text{ ngày } 18\\text{ giờ}$.", "$x = 2\\text{ ngày } 18\\text{ giờ} + 3\\text{ ngày } 14\\text{ giờ}$\n$x = 5\\text{ ngày } 32\\text{ giờ} = 6\\text{ ngày } 8\\text{ giờ}$.", "x = 6 ngày 8 giờ", 4, 1.0),
            make_essay(4, "Một người thợ làm việc từ 7 giờ 45 phút đến 11 giờ 30 phút, nghỉ trưa 1 giờ 15 phút rồi làm tiếp đến 16 giờ 45 phút. Hỏi trong ngày hôm đó người đó làm việc tất cả bao nhiêu thời gian?", "Thời gian làm việc buổi sáng là:\n$11\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ } 45\\text{ phút} = 3\\text{ giờ } 45\\text{ phút}$.\nThời gian bắt đầu làm việc buổi chiều là:\n$11\\text{ giờ } 30\\text{ phút} + 1\\text{ giờ } 15\\text{ phút} = 12\\text{ giờ } 45\\text{ phút}$.\nThời gian làm việc buổi chiều là:\n$16\\text{ giờ } 45\\text{ phút} - 12\\text{ giờ } 45\\text{ phút} = 4\\text{ giờ}$.\nTổng thời gian làm việc trong ngày là:\n$3\\text{ giờ } 45\\text{ phút} + 4\\text{ giờ} = 7\\text{ giờ } 45\\text{ phút}$.", "7 giờ 45 phút", 5, 1.5),
            make_essay(5, "Ba bạn Hùng, Dũng, Tuấn tham gia chạy cự ly $800\\text{ m}$. Hùng chạy hết 2 phút 45 giây. Dũng chạy chậm hơn Hùng 15 giây nhưng nhanh hơn Tuấn 12 giây. Hỏi Tuấn chạy hết bao nhiêu thời gian?", "Thời gian Dũng chạy là:\n$2\\text{ phút } 45\\text{ giây} + 15\\text{ giây} = 3\\text{ phút}$.\nVì Dũng nhanh hơn Tuấn 12 giây nên Tuấn chạy chậm hơn Dũng 12 giây.\nThời gian Tuấn chạy là:\n$3\\text{ phút} + 12\\text{ giây} = 3\\text{ phút } 12\\text{ giây}$.", "3 phút 12 giây", 5, 1.5),
            make_essay(6, "Một người đi từ A lúc 8 giờ 15 phút, đến B người đó nghỉ lại 30 phút rồi đi tiếp đến C lúc 11 giờ 45 phút. Biết thời gian đi từ B đến C là 1 giờ 20 phút. Hỏi thời gian người đó đi từ A đến B là bao nhiêu?", "Tổng thời gian từ khi khởi hành ở A đến khi tới C là:\n$11\\text{ giờ } 45\\text{ phút} - 8\\text{ giờ } 15\\text{ phút} = 3\\text{ giờ } 30\\text{ phút}$.\nThời gian thực tế đi cả hai chặng AB và BC là:\n$3\\text{ giờ } 30\\text{ phút} - 30\\text{ phút} = 3\\text{ giờ}$.\nThời gian đi đoạn đường AB là:\n$3\\text{ giờ} - 1\\text{ giờ } 20\\text{ phút} = 1\\text{ giờ } 40\\text{ phút}$.", "1 giờ 40 phút", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 47: NHÂN, CHIA SỐ ĐO THỜI GIAN VỚI MỘT SỐ
    # =========================================================================
    # --- Bài 47 - Đề 1 ---
    exams["th5_b47_test1"] = {
        "id": "th5_b47_test1",
        "lessonId": "th5_b47",
        "lessonNum": 47,
        "testNum": 1,
        "title": "Bài 47: Nhân, chia số đo thời gian với một số - Đề số 1",
        "topic": "Nhân, chia số đo thời gian với một số",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân $1\\text{ giờ } 25\\text{ phút} \\times 3$ là:", ["3 giờ 75 phút", "4 giờ 15 phút", "4 giờ 25 phút", "3 giờ 15 phút"], 1, "3h 75p = 4 giờ 15 phút."),
            make_mc(2, "Kết quả của phép chia $7\\text{ giờ } 30\\text{ phút} : 3$ là:", ["2 giờ 30 phút", "2 giờ 10 phút", "2 giờ 50 phút", "2 giờ 15 phút"], 0, "7h 30p = 6h 90p : 3 = 2 giờ 30 phút."),
            make_mc(3, "Một người làm 1 chi tiết máy hết 45 phút. Làm 4 chi tiết như thế hết:", ["3 giờ", "2 giờ 40 phút", "3 giờ 15 phút", "2 giờ 45 phút"], 0, "45 x 4 = 180 phút = 3 giờ."),
            make_mc(4, "Tính: $2\\text{ phút } 15\\text{ giây} \\times 4$ bằng:", ["8 phút 60 giây", "9 phút", "8 phút 45 giây", "9 phút 15 giây"], 1, "8 phút 60 giây = 9 phút."),
            make_mc(5, "Tính: $15\\text{ phút } 20\\text{ giây} : 4$ bằng:", ["3 phút 50 giây", "3 phút 45 giây", "3 phút 20 giây", "4 phút 10 giây"], 0, "15p 20s = 12p + 3p 20s = 12p 200s : 4 = 3 phút 50 giây."),
            make_mc(6, "Giá trị của biểu thức $(1\\text{ giờ } 10\\text{ phút} + 2\\text{ giờ } 20\\text{ phút}) \\times 2$ là:", ["7 giờ", "6 giờ 50 phút", "7 giờ 10 phút", "6 giờ"], 0, "3h 30p x 2 = 6h 60p = 7 giờ.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $3\\text{ giờ } 18\\text{ phút} \\times 4$\nb) $14\\text{ phút } 36\\text{ giây} : 3$", "a) $3\\text{ giờ } 18\\text{ phút} \\times 4 = 12\\text{ giờ } 72\\text{ phút} = 13\\text{ giờ } 12\\text{ phút}$.\nb) $14\\text{ phút } 36\\text{ giây} : 3 = 4\\text{ phút } 52\\text{ giây}$ (14p : 3 = 4p dư 2p = 120s; 120s + 36s = 156s : 3 = 52s).", "a) 13 giờ 12 phút; b) 4 phút 52 giây", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\n$A = (4\\text{ giờ } 45\\text{ phút} - 1\\text{ giờ } 30\\text{ phút}) \\times 3$", "$4\\text{ giờ } 45\\text{ phút} - 1\\text{ giờ } 30\\text{ phút} = 3\\text{ giờ } 15\\text{ phút}$.\n$A = 3\\text{ giờ } 15\\text{ phút} \\times 3 = 9\\text{ giờ } 45\\text{ phút}$.", "A = 9 giờ 45 phút", 4, 1.0),
            make_essay(3, "Một vận động viên đua xe đạp đi hết một vòng sân vận động mất 1 phút 25 giây. Hỏi nếu vận động viên đó giữ nguyên tốc độ thì đi hết 6 vòng sân vận động mất bao nhiêu thời gian?", "Thời gian đi hết 6 vòng sân là:\n$1\\text{ phút } 25\\text{ giây} \\times 6 = 6\\text{ phút } 150\\text{ giây} = 8\\text{ phút } 30\\text{ giây}$.", "8 phút 30 giây", 4, 1.0),
            make_essay(4, "Một người thợ làm việc từ 8 giờ đến 11 giờ 30 phút và hoàn thành được 5 sản phẩm cùng loại. Hỏi trung bình người đó làm một sản phẩm hết bao nhiêu phút?", "Thời gian người đó làm 5 sản phẩm là:\n$11\\text{ giờ } 30\\text{ phút} - 8\\text{ giờ} = 3\\text{ giờ } 30\\text{ phút} = 210\\text{ phút}$.\nTrung bình thời gian làm 1 sản phẩm là:\n$210 : 5 = 42\\text{ (phút)}$.", "42 phút", 5, 1.5),
            make_essay(5, "Một máy đóng gói tự động, cứ 1 phút 12 giây thì đóng gói được 1 thùng hàng. Hỏi trong 1 giờ máy đó đóng gói được bao nhiêu thùng hàng?", "Đổi: $1\\text{ phút } 12\\text{ giây} = 72\\text{ giây}$.\n$1\\text{ giờ} = 3600\\text{ giây}$.\nSố thùng hàng máy đóng gói được trong 1 giờ là:\n$3600 : 72 = 50$ (thùng hàng).", "50 thùng hàng", 5, 1.5),
            make_essay(6, "Bác Hải may 4 chiếc áo cùng loại hết 5 giờ 20 phút. Bác may 3 chiếc quần cùng loại hết 3 giờ 15 phút. Hỏi thời gian bác Hải may 1 chiếc áo nhiều hơn may 1 chiếc quần là bao nhiêu phút?", "Thời gian may 1 chiếc áo là: $5\\text{ giờ } 20\\text{ phút} : 4 = 1\\text{ giờ } 20\\text{ phút} = 80\\text{ phút}$.\nThời gian may 1 chiếc quần là: $3\\text{ giờ } 15\\text{ phút} : 3 = 1\\text{ giờ } 5\\text{ phút} = 65\\text{ phút}$.\nMay 1 áo nhiều hơn may 1 quần là: $80 - 65 = 15\\text{ (phút)}$.", "15 phút", 4, 1.0)
        ]
    }

    # --- Bài 47 - Đề 2 ---
    exams["th5_b47_test2"] = {
        "id": "th5_b47_test2",
        "lessonId": "th5_b47",
        "lessonNum": 47,
        "testNum": 2,
        "title": "Bài 47: Nhân, chia số đo thời gian với một số - Đề số 2",
        "topic": "Nhân, chia số đo thời gian với một số",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $2\\text{ ngày } 8\\text{ giờ} \\times 3$ bằng:", ["6 ngày 24 giờ", "7 ngày", "6 ngày 18 giờ", "7 ngày 8 giờ"], 1, "6 ngày 24 giờ = 7 ngày."),
            make_mc(2, "Tính: $9\\text{ giờ } 40\\text{ phút} : 4$ bằng:", ["2 giờ 25 phút", "2 giờ 15 phút", "2 giờ 35 phút", "2 giờ 45 phút"], 0, "9h 40p = 8h 100p : 4 = 2 giờ 25 phút."),
            make_mc(3, "Một ô tô đi 1 vòng quanh bờ hồ mất 18 phút 30 giây. Đi 4 vòng như thế hết:", ["1 giờ 14 phút", "1 giờ 12 phút", "1 giờ 20 phút", "1 giờ 15 phút"], 0, "18p 30s x 4 = 72p 120s = 74 phút = 1 giờ 14 phút."),
            make_mc(4, "Tính: $16\\text{ phút } 32\\text{ giây} : 4$ bằng:", ["4 phút 8 giây", "4 phút 12 giây", "4 phút 6 giây", "4 phút 18 giây"], 0, "16p : 4 = 4p; 32s : 4 = 8s => 4 phút 8 giây."),
            make_mc(5, "Biết $x : 3 = 1\\text{ giờ } 15\\text{ phút}$. Giá trị của $x$ là:", ["3 giờ 45 phút", "3 giờ 30 phút", "4 giờ 15 phút", "3 giờ 15 phút"], 0, "x = 1h 15p x 3 = 3 giờ 45 phút."),
            make_mc(6, "Giá trị của biểu thức $4\\text{ giờ } 15\\text{ phút} \\times 2 + 1\\text{ giờ } 30\\text{ phút}$ là:", ["10 giờ", "9 giờ 30 phút", "10 giờ 15 phút", "9 giờ 45 phút"], 0, "8h 30p + 1h 30p = 9h 60p = 10 giờ.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $2\\text{ giờ } 45\\text{ phút} \\times 5$\nb) $19\\text{ giờ } 12\\text{ phút} : 6$", "a) $2\\text{ giờ } 45\\text{ phút} \\times 5 = 10\\text{ giờ } 225\\text{ phút} = 13\\text{ giờ } 45\\text{ phút}$.\nb) $19\\text{ giờ } 12\\text{ phút} : 6 = 3\\text{ giờ } 12\\text{ phút}$ (19h : 6 = 3h dư 1h = 60p; 60p + 12p = 72p : 6 = 12p).", "a) 13 giờ 45 phút; b) 3 giờ 12 phút", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\n$B = (8\\text{ phút } 20\\text{ giây} + 3\\text{ phút } 40\\text{ giây}) : 4$", "$8\\text{ phút } 20\\text{ giây} + 3\\text{ phút } 40\\text{ giây} = 11\\text{ phút } 60\\text{ giây} = 12\\text{ phút}$.\n$B = 12\\text{ phút} : 4 = 3\\text{ phút}$.", "B = 3 phút", 4, 1.0),
            make_essay(3, "Một công nhân lắp ráp 3 chiếc quạt máy hết 4 giờ 30 phút. Hỏi với tốc độ đó, người công nhân lắp ráp 8 chiếc quạt máy như thế hết bao nhiêu thời gian?", "Thời gian lắp ráp 1 chiếc quạt máy là:\n$4\\text{ giờ } 30\\text{ phút} : 3 = 1\\text{ giờ } 30\\text{ phút} = 1,5\\text{ giờ}$.\nThời gian lắp ráp 8 chiếc quạt máy là:\n$1,5 \\times 8 = 12\\text{ (giờ)}$.", "12 giờ", 4, 1.0),
            make_essay(4, "Một người đi bộ một vòng quanh công viên hết 14 phút 15 giây. Hỏi người đó đi 4 vòng quanh công viên hết bao nhiêu thời gian? Đổi kết quả ra đơn vị giờ.", "Thời gian người đó đi 4 vòng là:\n$14\\text{ phút } 15\\text{ giây} \\times 4 = 56\\text{ phút } 60\\text{ giây} = 57\\text{ phút}$.\nĐổi sang giờ: $57 : 60 = 0,95\\text{ giờ}$.", "57 phút (hoặc 0,95 giờ)", 5, 1.5),
            make_essay(5, "Một xưởng may nhận may 120 bộ đồng phục học sinh. Trung bình mỗi bộ may hết 1 giờ 15 phút. Mỗi ngày xưởng làm việc 8 giờ. Hỏi xưởng đó cần bao nhiêu ngày để hoàn thành đơn hàng?", "Thời gian may 1 bộ là: $1\\text{ giờ } 15\\text{ phút} = 1,25\\text{ giờ}$.\nTổng thời gian may 120 bộ là: $1,25 \\times 120 = 150\\text{ (giờ)}$.\nSố ngày cần thiết là: $150 : 8 = 18,75\\text{ (ngày)}$.\nNhư vậy xưởng cần làm trong 19 ngày để hoàn thành.", "18,75 ngày (hay 19 ngày làm việc)", 5, 1.5),
            make_essay(6, "Tính nhanh: $2\\text{ giờ } 15\\text{ phút} \\times 4 + 3\\text{ giờ } 45\\text{ phút} \\times 4$.", "Áp dụng tính chất phân phối:\n$(2\\text{ giờ } 15\\text{ phút} + 3\\text{ giờ } 45\\text{ phút}) \\times 4$\n$= 5\\text{ giờ } 60\\text{ phút} \\times 4 = 6\\text{ giờ} \\times 4 = 24\\text{ giờ} = 1\\text{ ngày}$.", "24 giờ (hoặc 1 ngày)", 4, 1.0)
        ]
    }

    # --- Bài 47 - Đề 3 ---
    exams["th5_b47_test3"] = {
        "id": "th5_b47_test3",
        "lessonId": "th5_b47",
        "lessonNum": 47,
        "testNum": 3,
        "title": "Bài 47: Nhân, chia số đo thời gian với một số - Đề số 3",
        "topic": "Nhân, chia số đo thời gian với một số",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $1\\text{ giờ } 40\\text{ phút} \\times 5$ bằng:", ["8 giờ 20 phút", "7 giờ 20 phút", "8 giờ 40 phút", "7 giờ 40 phút"], 0, "5h 200p = 5h + 3h 20p = 8 giờ 20 phút."),
            make_mc(2, "Tính: $21\\text{ phút } 15\\text{ giây} : 5$ bằng:", ["4 phút 15 giây", "4 phút 25 giây", "4 phút 3 giây", "4 phút 12 giây"], 0, "21p 15s = 20p + 1p 15s = 20p 75s : 5 = 4 phút 15 giây."),
            make_mc(3, "Một vận động viên bơi một vòng bể hết 54 giây. Bơi 5 vòng như thế hết:", ["4 phút 30 giây", "4 phút 10 giây", "5 phút", "4 phút 50 giây"], 0, "54 x 5 = 270 giây = 4 phút 30 giây."),
            make_mc(4, "Biết $y \\times 4 = 6\\text{ giờ}$. Giá trị của $y$ là:", ["1 giờ 30 phút", "1 giờ 20 phút", "1 giờ 45 phút", "1 giờ 15 phút"], 0, "y = 6h : 4 = 1,5h = 1 giờ 30 phút."),
            make_mc(5, "Tính: $13\\text{ giờ } 20\\text{ phút} : 4$ bằng:", ["3 giờ 20 phút", "3 giờ 15 phút", "3 giờ 25 phút", "3 giờ 30 phút"], 0, "13h 20p = 12h 80p : 4 = 3 giờ 20 phút."),
            make_mc(6, "Giá trị biểu thức $(5\\text{ phút } 12\\text{ giây} - 2\\text{ phút } 42\\text{ giây}) \\times 2$ là:", ["5 phút", "4 phút 40 giây", "5 phút 20 giây", "4 phút 50 giây"], 0, "(4p 72s - 2p 42s) = 2p 30s x 2 = 5 phút.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $4\\text{ phút } 35\\text{ giây} \\times 6$\nb) $25\\text{ giờ } 40\\text{ phút} : 5$", "a) $4\\text{ phút } 35\\text{ giây} \\times 6 = 24\\text{ phút } 210\\text{ giây} = 27\\text{ phút } 30\\text{ giây}$.\nb) $25\\text{ giờ } 40\\text{ phút} : 5 = 5\\text{ giờ } 8\\text{ phút}$.", "a) 27 phút 30 giây; b) 5 giờ 8 phút", 4, 1.0),
            make_essay(2, "Tính bằng cách hợp lí:\n$D = 4\\text{ giờ } 20\\text{ phút} \\times 5 - 1\\text{ giờ } 50\\text{ phút} \\times 5$", "$D = (4\\text{ giờ } 20\\text{ phút} - 1\\text{ giờ } 50\\text{ phút}) \\times 5$\n$= (3\\text{ giờ } 80\\text{ phút} - 1\\text{ giờ } 50\\text{ phút}) \\times 5 = 2\\text{ giờ } 30\\text{ phút} \\times 5 = 12\\text{ giờ } 30\\text{ phút}$.", "D = 12 giờ 30 phút", 4, 1.0),
            make_essay(3, "Bác Nam tiện 6 chi tiết máy hết 2 giờ 24 phút. Hỏi bác Nam tiện 9 chi tiết máy như thế hết bao nhiêu thời gian?", "Thời gian tiện 1 chi tiết máy là:\n$2\\text{ giờ } 24\\text{ phút} : 6 = 144\\text{ phút} : 6 = 24\\text{ (phút)}$.\nThời gian tiện 9 chi tiết máy là:\n$24 \\times 9 = 216\\text{ (phút)} = 3\\text{ giờ } 36\\text{ phút}$.", "3 giờ 36 phút (hoặc 216 phút)", 4, 1.0),
            make_essay(4, "Một máy bay bay từ Thành phố Hồ Chí Minh ra Hà Nội mất 2 giờ 10 phút. Một ngày máy bay đó thực hiện 4 chuyến bay như thế. Hỏi tổng thời gian bay trong ngày của máy bay đó là bao nhiêu giờ, bao nhiêu phút?", "Tổng thời gian bay trong ngày là:\n$2\\text{ giờ } 10\\text{ phút} \\times 4 = 8\\text{ giờ } 40\\text{ phút}$.", "8 giờ 40 phút", 5, 1.5),
            make_essay(5, "Một người thợ đóng 1 chiếc ghế hết 1 giờ 15 phút, đóng 1 chiếc bàn hết 2 giờ 45 phút. Hỏi người đó đóng 4 bộ bàn ghế (mỗi bộ gồm 1 bàn và 4 ghế) hết tất cả bao nhiêu thời gian?", "Thời gian đóng 4 chiếc ghế là: $1\\text{ giờ } 15\\text{ phút} \\times 4 = 5\\text{ giờ}$.\nThời gian đóng 1 bộ bàn ghế (1 bàn và 4 ghế) là:\n$2\\text{ giờ } 45\\text{ phút} + 5\\text{ giờ} = 7\\text{ giờ } 45\\text{ phút} = 7,75\\text{ giờ}$.\nThời gian đóng 4 bộ bàn ghế là:\n$7,75 \\times 4 = 31\\text{ (giờ)}$.", "31 giờ", 5, 1.5),
            make_essay(6, "Trung bình một người thợ gặt lúa một sào hết 1 giờ 45 phút. Hỏi để gặt xong 1 mẫu lúa (gồm 10 sào), người thợ đó cần bao nhiêu giờ công?", "Thời gian gặt 10 sào lúa là:\n$1\\text{ giờ } 45\\text{ phút} \\times 10 = 1,75\\text{ giờ} \\times 10 = 17,5\\text{ giờ} = 17\\text{ giờ } 30\\text{ phút}$.", "17,5 giờ (hay 17 giờ 30 phút)", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 48: VẬN TỐC
    # =========================================================================
    # --- Bài 48 - Đề 1 ---
    exams["th5_b48_test1"] = {
        "id": "th5_b48_test1",
        "lessonId": "th5_b48",
        "lessonNum": 48,
        "testNum": 1,
        "title": "Bài 48: Vận tốc - Đề số 1",
        "topic": "Vận tốc",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn tính vận tốc ta lấy:", [
                "Quãng đường chia cho thời gian",
                "Quãng đường nhân với thời gian",
                "Thời gian chia cho quãng đường",
                "Quãng đường cộng với thời gian"
            ], 0, "Công thức: v = s : t."),
            make_mc(2, "Một ô tô đi được quãng đường $120\\text{ km}$ trong 2,5 giờ. Vận tốc của ô tô là:", ["48 km/giờ", "50 km/giờ", "45 km/giờ", "60 km/giờ"], 0, "120 : 2,5 = 48 km/giờ."),
            make_mc(3, "Đơn vị đo vận tốc thường dùng là:", ["km", "giờ", "km/giờ hoặc m/giây", "m/phút hoặc kg"], 2, "Đơn vị vận tốc là km/giờ, m/giây, m/phút..."),
            make_mc(4, "Một người chạy được $150\\text{ m}$ trong 30 giây. Vận tốc chạy của người đó là:", ["5 m/giây", "10 m/giây", "15 m/giây", "4,5 m/giây"], 0, "150 : 30 = 5 m/giây."),
            make_mc(5, "Một con đà điểu chạy được quãng đường $3 150\\text{ m}$ trong 5 phút. Vận tốc của đà điểu theo m/phút là:", ["630 m/phút", "600 m/phút", "650 m/phút", "530 m/phút"], 0, "3150 : 5 = 630 m/phút."),
            make_mc(6, "Vận tốc $36\\text{ km/giờ}$ đổi ra m/giây bằng:", ["10 m/giây", "12 m/giây", "15 m/giây", "360 m/giây"], 0, "36 000 m : 3600 giây = 10 m/giây.")
        ],
        "part2": [
            make_essay(1, "Một người đi xe máy đi được quãng đường $105\\text{ km}$ trong 2 giờ 30 phút. Tính vận tốc của người đi xe máy đó theo đơn vị km/giờ.", "Đổi: $2\\text{ giờ } 30\\text{ phút} = 2,5\\text{ giờ}$.\nVận tốc của người đi xe máy là:\n$105 : 2,5 = 42\\text{ (km/giờ)}$.", "42 km/giờ", 4, 1.0),
            make_essay(2, "Một máy bay bay được quãng đường $1 800\\text{ km}$ trong 2 giờ 15 phút. Tính vận tốc của máy bay.", "Đổi: $2\\text{ giờ } 15\\text{ phút} = 2,25\\text{ giờ}$.\nVận tốc của máy bay là:\n$1 800 : 2,25 = 800\\text{ (km/giờ)}$.", "800 km/giờ", 4, 1.0),
            make_essay(3, "Một vận động viên bơi bơi cự ly $100\\text{ m}$ hết 1 phút 15 giây. Tính vận tốc bơi của vận động viên đó theo đơn vị m/giây.", "Đổi: 1 phút 15 giây = 75 giây.\nVận tốc bơi của vận động viên là:\n$100 : 75 = \\frac{4}{3}\\text{ (m/giây)} \\approx 1,33\\text{ (m/giây)}$.", "4/3 m/giây (khoảng 1,33 m/giây)", 4, 1.0),
            make_essay(4, "Quãng đường AB dài $135\\text{ km}$. Một ô tô khởi hành từ A lúc 7 giờ 30 phút và đến B lúc 10 giờ 15 phút. Giữa đường ô tô nghỉ 15 phút. Tính vận tốc của ô tô.", "Thời gian ô tô đi cả chặng và nghỉ là:\n$10\\text{ giờ } 15\\text{ phút} - 7\\text{ giờ } 30\\text{ phút} = 2\\text{ giờ } 45\\text{ phút}$.\nThời gian thực tế ô tô chạy trên đường là:\n$2\\text{ giờ } 45\\text{ phút} - 15\\text{ phút} = 2\\text{ giờ } 30\\text{ phút} = 2,5\\text{ giờ}$.\nVận tốc của ô tô là:\n$135 : 2,5 = 54\\text{ (km/giờ)}$.", "54 km/giờ", 5, 1.5),
            make_essay(5, "Một đoàn tàu hỏa chạy qua một cây cầu dài $450\\text{ m}$ hết 45 giây. Biết chiều dài của đoàn tàu là $150\\text{ m}$. Tính vận tốc của đoàn tàu theo đơn vị m/giây và km/giờ.", "Quãng đường đoàn tàu đi được từ khi đầu tàu bước vào cầu đến khi toa cuối cùng ra khỏi cầu là:\n$450 + 150 = 600\\text{ (m)}$.\nVận tốc của đoàn tàu là:\n$600 : 45 = \\frac{40}{3}\\text{ (m/giây)}$.\nĐổi sang km/giờ:\n$\\frac{40}{3} \\times 3,6 = 48\\text{ (km/giờ)}$.", "40/3 m/giây (hay 48 km/giờ)", 5, 1.5),
            make_essay(6, "Bác An đi bộ $1,2\\text{ km}$ hết 15 phút. Bác Ba đi xe đạp $4,5\\text{ km}$ hết 18 phút. Hỏi vận tốc của ai lớn hơn và lớn hơn bao nhiêu km/giờ?", "Đổi thời gian:\n$15\\text{ phút} = 0,25\\text{ giờ} \\Rightarrow$ vận tốc bác An: $1,2 : 0,25 = 4,8\\text{ (km/giờ)}$.\n$18\\text{ phút} = 0,3\\text{ giờ} \\Rightarrow$ vận tốc bác Ba: $4,5 : 0,3 = 15\\text{ (km/giờ)}$.\nVận tốc bác Ba lớn hơn bác An: $15 - 4,8 = 10,2\\text{ (km/giờ)}$.", "Bác Ba nhanh hơn 10,2 km/giờ", 4, 1.0)
        ]
    }

    # --- Bài 48 - Đề 2 ---
    exams["th5_b48_test2"] = {
        "id": "th5_b48_test2",
        "lessonId": "th5_b48",
        "lessonNum": 48,
        "testNum": 2,
        "title": "Bài 48: Vận tốc - Đề số 2",
        "topic": "Vận tốc",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một ô tô đi được quãng đường $140\\text{ km}$ trong 3,5 giờ. Vận tốc của ô tô là:", ["40 km/giờ", "45 km/giờ", "50 km/giờ", "35 km/giờ"], 0, "140 : 3,5 = 40 km/giờ."),
            make_mc(2, "Một người chạy bộ $400\\text{ m}$ trong 1 phút 20 giây. Vận tốc của người đó là:", ["5 m/giây", "4 m/giây", "6 m/giây", "3,5 m/giây"], 0, "1p 20s = 80s. 400 : 80 = 5 m/giây."),
            make_mc(3, "Một con cá heo bơi quãng đường $72\\text{ km}$ trong 2 giờ. Vận tốc của cá heo là:", ["36 km/giờ", "35 km/giờ", "40 km/giờ", "30 km/giờ"], 0, "72 : 2 = 36 km/giờ."),
            make_mc(4, "Một người đi xe máy khởi hành từ A lúc 8 giờ và đến B lúc 9 giờ 45 phút, đi được $70\\text{ km}$. Vận tốc xe máy là:", ["40 km/giờ", "45 km/giờ", "35 km/giờ", "50 km/giờ"], 0, "Thời gian = 1h 45p = 1,75h. 70 : 1,75 = 40 km/giờ."),
            make_mc(5, "Đổi vận tốc $54\\text{ km/giờ}$ ra m/giây được kết quả là:", ["15 m/giây", "18 m/giây", "20 m/giây", "12 m/giây"], 0, "54 : 3,6 = 15 m/giây."),
            make_mc(6, "Vận tốc của một chú ốc sên là $12\\text{ cm/phút}$. Trong 1 giờ chú ốc sên bò được:", ["720 cm", "600 cm", "72 m", "1,2 m"], 0, "12 x 60 = 720 cm = 7,2 m.")
        ],
        "part2": [
            make_essay(1, "Một người đi xe đạp đi được quãng đường $36\\text{ km}$ trong 2 giờ 24 phút. Tính vận tốc của người đi xe đạp theo đơn vị km/giờ.", "Đổi: $2\\text{ giờ } 24\\text{ phút} = 2,4\\text{ giờ}$.\nVận tốc của người đi xe đạp là:\n$36 : 2,4 = 15\\text{ (km/giờ)}$.", "15 km/giờ", 4, 1.0),
            make_essay(2, "Một tàu hỏa đi được quãng đường $196\\text{ km}$ trong 3 giờ 30 phút. Tính vận tốc của tàu hỏa theo đơn vị km/giờ.", "Đổi: $3\\text{ giờ } 30\\text{ phút} = 3,5\\text{ giờ}$.\nVận tốc của tàu hỏa là:\n$196 : 3,5 = 56\\text{ (km/giờ)}$.", "56 km/giờ", 4, 1.0),
            make_essay(3, "Một vận động viên trượt băng lướt được quãng đường $1\\text{ km } 200\\text{ m}$ trong 2 phút 30 giây. Tính vận tốc của vận động viên đó theo đơn vị m/giây.", "Đổi: $1\\text{ km } 200\\text{ m} = 1 200\\text{ m}$.\n$2\\text{ phút } 30\\text{ giây} = 150\\text{ giây}$.\nVận tốc của vận động viên là:\n$1 200 : 150 = 8\\text{ (m/giây)}$.", "8 m/giây", 4, 1.0),
            make_essay(4, "Một người đi xe máy từ A lúc 7 giờ và đến B lúc 10 giờ 30 phút. Giữa đường người đó dừng lại nghỉ 30 phút. Quãng đường AB dài $120\\text{ km}$. Tính vận tốc của xe máy.", "Thời gian thực tế người đó đi xe máy trên đường là:\n$10\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} - 30\\text{ phút} = 3\\text{ giờ}$.\nVận tốc của xe máy là:\n$120 : 3 = 40\\text{ (km/giờ)}$.", "40 km/giờ", 5, 1.5),
            make_essay(5, "Một đoàn tàu dài $200\\text{ m}$ vượt qua một người đi xe đạp cùng chiều với vận tốc $18\\text{ km/giờ}$ trong 20 giây. Tính vận tốc của đoàn tàu theo đơn vị km/giờ.", "Đổi vận tốc xe đạp: $18\\text{ km/giờ} = 5\\text{ m/giây}$.\nVận tốc của tàu so với người đi xe đạp là:\n$200 : 20 = 10\\text{ (m/giây)}$.\nVận tốc thực tế của đoàn tàu là:\n$10 + 5 = 15\\text{ (m/giây)}$.\nĐổi sang km/giờ: $15 \\times 3,6 = 54\\text{ (km/giờ)}$.", "54 km/giờ", 5, 1.5),
            make_essay(6, "Bác Ba đi từ nhà ra thị trấn. Đoạn đường đầu dài $3\\text{ km}$ bác đi bộ hết 36 phút, đoạn đường sau dài $15\\text{ km}$ bác đi xe buýt hết 24 phút. Tính vận tốc của bác Ba trên từng đoạn đường.", "Đổi: $36\\text{ phút} = 0,6\\text{ giờ}$; $24\\text{ phút} = 0,4\\text{ giờ}$.\nVận tốc đi bộ: $3 : 0,6 = 5\\text{ (km/giờ)}$.\nVận tốc xe buýt: $15 : 0,4 = 37,5\\text{ (km/giờ)}$.", "Đi bộ: 5 km/giờ; Xe buýt: 37,5 km/giờ", 4, 1.0)
        ]
    }

    # --- Bài 48 - Đề 3 ---
    exams["th5_b48_test3"] = {
        "id": "th5_b48_test3",
        "lessonId": "th5_b48",
        "lessonNum": 48,
        "testNum": 3,
        "title": "Bài 48: Vận tốc - Đề số 3",
        "topic": "Vận tốc",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người đi xe đạp đi quãng đường $27\\text{ km}$ hết 1,8 giờ. Vận tốc người đi xe đạp là:", ["15 km/giờ", "12 km/giờ", "18 km/giờ", "16 km/giờ"], 0, "27 : 1,8 = 15 km/giờ."),
            make_mc(2, "Một con ong mật bay quãng đường $4\\text{ km}$ trong 15 phút. Vận tốc của ong mật là:", ["16 km/giờ", "15 km/giờ", "18 km/giờ", "12 km/giờ"], 0, "15 phút = 0,25 giờ. 4 : 0,25 = 16 km/giờ."),
            make_mc(3, "Vận tốc của âm thanh trong không khí khoảng $340\\text{ m/giây}$. Một tiếng sét nổ sau 3 giây thì một người nghe thấy. Khoảng cách từ người đó đến nơi sét đánh là:", ["1 020 m", "680 m", "340 m", "1 200 m"], 0, "340 x 3 = 1 020 m."),
            make_mc(4, "Một ca nô đi xuôi dòng quãng đường $45\\text{ km}$ trong 1,5 giờ. Vận tốc xuôi dòng của ca nô là:", ["30 km/giờ", "25 km/giờ", "35 km/giờ", "40 km/giờ"], 0, "45 : 1,5 = 30 km/giờ."),
            make_mc(5, "Đổi $20\\text{ m/giây} = \\dots \\text{ km/giờ}$:", ["72 km/giờ", "60 km/giờ", "54 km/giờ", "80 km/giờ"], 0, "20 x 3,6 = 72 km/giờ."),
            make_mc(6, "Một ô tô đi được $105\\text{ km}$ trong 2 giờ 6 phút. Vận tốc ô tô là:", ["50 km/giờ", "45 km/giờ", "52 km/giờ", "48 km/giờ"], 0, "2h 6p = 2,1h. 105 : 2,1 = 50 km/giờ.")
        ],
        "part2": [
            make_essay(1, "Một ô tô chạy quãng đường $162\\text{ km}$ trong 3 giờ 36 phút. Tính vận tốc của ô tô.", "Đổi: $3\\text{ giờ } 36\\text{ phút} = 3,6\\text{ giờ}$.\nVận tốc của ô tô là:\n$162 : 3,6 = 45\\text{ (km/giờ)}$.", "45 km/giờ", 4, 1.0),
            make_essay(2, "Một người đi xe máy trong 45 phút đi được $27\\text{ km}$. Tính vận tốc của người đi xe máy theo đơn vị km/giờ.", "Đổi: $45\\text{ phút} = 0,75\\text{ giờ}$.\nVận tốc của người đi xe máy là:\n$27 : 0,75 = 36\\text{ (km/giờ)}$.", "36 km/giờ", 4, 1.0),
            make_essay(3, "Một vận động viên bơi $200\\text{ m}$ hết 2 phút 5 giây. Tính vận tốc của vận động viên theo đơn vị m/giây.", "Đổi: $2\\text{ phút } 5\\text{ giây} = 125\\text{ giây}$.\nVận tốc bơi là:\n$200 : 125 = 1,6\\text{ (m/giây)}$.", "1,6 m/giây", 4, 1.0),
            make_essay(4, "Một ô tô khởi hành từ Hải Phòng lúc 6 giờ 45 phút và đến Hà Nội lúc 8 giờ 45 phút. Quãng đường từ Hải Phòng đến Hà Nội dài $102\\text{ km}$. Tính vận tốc của ô tô.", "Thời gian ô tô chạy là:\n$8\\text{ giờ } 45\\text{ phút} - 6\\text{ giờ } 45\\text{ phút} = 2\\text{ giờ}$.\nVận tốc của ô tô là:\n$102 : 2 = 51\\text{ (km/giờ)}$.", "51 km/giờ", 5, 1.5),
            make_essay(5, "Một đoàn tàu hỏa dài $180\\text{ m}$ chạy qua một cột điện ven đường mất 12 giây. Tính vận tốc của đoàn tàu theo đơn vị m/giây và km/giờ.", "Khi tàu chạy qua cột điện, quãng đường đi được chính bằng chiều dài của đoàn tàu.\nVận tốc của đoàn tàu là:\n$180 : 12 = 15\\text{ (m/giây)}$.\nĐổi sang km/giờ: $15 \\times 3,6 = 54\\text{ (km/giờ)}$.", "15 m/giây = 54 km/giờ", 5, 1.5),
            make_essay(6, "Bình đi xe đạp từ nhà ra bến xe buýt với vận tốc $12\\text{ km/giờ}$ hết 20 phút. Từ bến xe buýt, Bình lên xe đi tiếp đến thư viện thành phố với vận tốc $36\\text{ km/giờ}$ hết 40 phút. Tính độ dài quãng đường từ nhà Bình đến thư viện thành phố.", "Đổi: $20\\text{ phút} = \\frac{1}{3}\\text{ giờ}$; $40\\text{ phút} = \\frac{2}{3}\\text{ giờ}$.\nQuãng đường đi xe đạp là: $12 \\times \\frac{1}{3} = 4\\text{ (km)}$.\nQuãng đường đi xe buýt là: $36 \\times \\frac{2}{3} = 24\\text{ (km)}$.\nTổng quãng đường từ nhà đến thư viện là: $4 + 24 = 28\\text{ (km)}$.", "28 km", 4, 1.0)
        ]
    }

    return exams
