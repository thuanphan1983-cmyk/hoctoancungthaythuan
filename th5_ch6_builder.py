# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 6: TỈ SỐ PHẦN TRĂM (BÀI 30 ĐẾN BÀI 34) - TOÁN 5 KNTT
Gồm 5 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 30: Tỉ số và tỉ số phần trăm (th5_b30_test1, th5_b30_test2, th5_b30_test3)
- Bài 31: Tìm tỉ số phần trăm của hai số (th5_b31_test1, th5_b31_test2, th5_b31_test3)
- Bài 32: Tìm giá trị phần trăm của một số (th5_b32_test1, th5_b32_test2, th5_b32_test3)
- Bài 33: Sử dụng máy tính cầm tay (th5_b33_test1, th5_b33_test2, th5_b33_test3)
- Bài 34: Luyện tập chung Chủ đề 6 (th5_b34_test1, th5_b34_test2, th5_b34_test3)
Tổng cộng: 15 đề kiểm tra chất lượng cao, độc lập 100%.
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

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 30: TỈ SỐ VÀ TỈ SỐ PHẦN TRĂM
    # =========================================================================

    # --- Bài 30 - Đề 1 ---
    exams["th5_b30_test1"] = {
        "id": "th5_b30_test1",
        "lessonId": "th5_b30",
        "lessonNum": 30,
        "testNum": 1,
        "title": "Bài 30: Tỉ số và tỉ số phần trăm - Đề số 1",
        "topic": "Tỉ số và tỉ số phần trăm",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Viết phân số $\\frac{1}{4}$ dưới dạng tỉ số phần trăm là:", ["14%", "25%", "40%", "20%"], 1, "Ta có: $\\frac{1}{4} = \\frac{25}{100} = 25\\%$."),
            make_mc(2, "Số thập phân $0,65$ viết dưới dạng tỉ số phần trăm là:", ["6,5%", "65%", "650%", "0,65%"], 1, "$0,65 \\times 100 = 65\\%$."),
            make_mc(3, "Tỉ số phần trăm $48\\%$ được đọc là:", ["Bốn mươi tám", "Bốn mươi tám phần trăm", "Bốn phần tám", "Bốn tám phần trăm"], 1, "Kí hiệu $\\%$ đọc là 'phần trăm'."),
            make_mc(4, "Viết tỉ số phần trăm $7,5\\%$ dưới dạng số thập phân là:", ["0,75", "0,075", "7,5", "0,0075"], 1, "$7,5\\% = 7,5 : 100 = 0,075$."),
            make_mc(5, "Một hình vuông được chia thành 100 ô vuông bằng nhau, người ta tô màu 37 ô. Tỉ số phần trăm của phần tô màu là:", ["37%", "73%", "3,7%", "63%"], 0, "Có 37 ô tô màu trên 100 ô nên chiếm $37\\%$."),
            make_mc(6, "Trong các số sau, số nào bằng $150\\%$?", ["1,05", "1,5", "15", "0,15"], 1, "$150\\% = 150 : 100 = 1,5$.")
        ],
        "part2": [
            make_essay(1, "Viết các phân số sau dưới dạng tỉ số phần trăm:\na) $\\frac{3}{5}$\nb) $\\frac{7}{20}$", "a) $\\frac{3}{5} = \\frac{3 \\times 20}{5 \\times 20} = \\frac{60}{100} = 60\\%$\nb) $\\frac{7}{20} = \\frac{7 \\times 5}{20 \\times 5} = \\frac{35}{100} = 35\\%$", "a) 60%; b) 35%", 4, 1.0),
            make_essay(2, "Viết các số thập phân sau dưới dạng tỉ số phần trăm:\na) $0,82$\nb) $1,35$", "a) $0,82 = 0,82 \\times 100\\% = 82\\%$\nb) $1,35 = 1,35 \\times 100\\% = 135\\%$", "a) 82%; b) 135%", 4, 1.0),
            make_essay(3, "Chuyển các tỉ số phần trăm sau thành phân số tối giản:\na) $45\\%$\nb) $80\\%$", "a) $45\\% = \\frac{45}{100} = \\frac{9}{20}$\nb) $80\\% = \\frac{80}{100} = \\frac{4}{5}$", "a) 9/20; b) 4/5", 4, 1.0),
            make_essay(4, "Một giá sách có 200 cuốn, trong đó có 70 cuốn truyện thiếu nhi. Hỏi số cuốn truyện thiếu nhi chiếm bao nhiêu phần trăm tổng số sách trên giá?", "Bài giải:\nTỉ số phần trăm số truyện thiếu nhi so với tổng số sách là:\n$70 : 200 = 0,35 = 35\\%$\nĐáp số: $35\\%$.", "35%", 5, 1.5),
            make_essay(5, "Một đàn gà có 120 con, trong đó số gà mái chiếm $65\\%$, còn lại là gà trống.\na) Hỏi số gà mái chiếm tỉ số phần trăm là bao nhiêu?\nb) Số gà trống chiếm bao nhiêu phần trăm đàn gà?", "Bài giải:\na) Theo đề bài, số gà mái chiếm $65\\%$ đàn gà.\nb) Tỉ số phần trăm số gà trống so với đàn gà là:\n$100\\% - 65\\% = 35\\%$\nĐáp số: a) $65\\%$; b) $35\\%$.", "a) 65%; b) 35%", 5, 1.5),
            make_essay(6, "Cho hình chữ nhật có chu vi $80\\text{ cm}$. Chiều rộng bằng $\\frac{3}{5}$ chiều dài. Hỏi chiều rộng bằng bao nhiêu phần trăm chiều dài?", "Bài giải:\nTheo đề bài, chiều rộng bằng $\\frac{3}{5}$ chiều dài.\nTa đổi: $\\frac{3}{5} = \\frac{60}{100} = 60\\%$.\nVậy chiều rộng bằng $60\\%$ chiều dài.\nĐáp số: $60\\%$.", "60%", 5, 1.0)
        ]
    }

    # --- Bài 30 - Đề 2 ---
    exams["th5_b30_test2"] = {
        "id": "th5_b30_test2",
        "lessonId": "th5_b30",
        "lessonNum": 30,
        "testNum": 2,
        "title": "Bài 30: Tỉ số và tỉ số phần trăm - Đề số 2",
        "topic": "Tỉ số và tỉ số phần trăm",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Viết phân số $\\frac{9}{25}$ dưới dạng tỉ số phần trăm:", ["36%", "45%", "25%", "90%"], 0, "$\\frac{9}{25} = \\frac{9 \\times 4}{25 \\times 4} = \\frac{36}{100} = 36\\%$."),
            make_mc(2, "Số thập phân $0,08$ viết dưới dạng tỉ số phần trăm là:", ["80%", "8%", "0,8%", "0,08%"], 1, "$0,08 = 8\\%$."),
            make_mc(3, "Tỉ số phần trăm của 15 và 100 là:", ["15%", "1,5%", "150%", "0,15%"], 0, "Tỉ số là $15/100 = 15\\%$."),
            make_mc(4, "Một rổ hoa quả có 50 quả, trong đó có 13 quả cam. Tỉ số phần trăm quả cam so với cả rổ là:", ["13%", "26%", "30%", "20%"], 1, "$13 : 50 = \\frac{26}{100} = 26\\%$."),
            make_mc(5, "Số nào dưới đây có giá trị bằng $200\\%$?", ["20", "2", "0,2", "0,02"], 1, "$200\\% = 200 : 100 = 2$."),
            make_mc(6, "Tính: $25\\% + 43\\% - 18\\% = \\dots$", ["50%", "40%", "60%", "45%"], 0, "$25\\% + 43\\% - 18\\% = 68\\% - 18\\% = 50\\%$.")
        ],
        "part2": [
            make_essay(1, "Viết các số đo sau dưới dạng tỉ số phần trăm của một mét:\na) $45\\text{ cm}$\nb) $7\\text{ dm}$", "a) $45\\text{ cm} = \\frac{45}{100}\\text{ m} = 45\\%\\text{ m}$\nb) $7\\text{ dm} = \\frac{70}{100}\\text{ m} = 70\\%\\text{ m}$", "a) 45%; b) 70%", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $34,5\\% + 18,2\\%$\nb) $76\\% - 29,5\\%$", "a) $34,5\\% + 18,2\\% = 52,7\\%$\nb) $76\\% - 29,5\\% = 46,5\\%$", "a) 52,7%; b) 46,5%", 4, 1.0),
            make_essay(3, "Chuyển các hỗn số sau thành tỉ số phần trăm:\na) $1\\frac{1}{2}$\nb) $2\\frac{3}{4}$", "a) $1\\frac{1}{2} = 1,5 = 150\\%$\nb) $2\\frac{3}{4} = 2,75 = 275\\%$", "a) 150%; b) 275%", 4, 1.0),
            make_essay(4, "Lớp 5B có 35 bạn học sinh, trong đó có 21 bạn nữ. Tìm tỉ số phần trăm của số bạn nữ so với tổng số học sinh của cả lớp.", "Bài giải:\nTỉ số phần trăm số bạn nữ so với số học sinh cả lớp là:\n$21 : 35 = 0,6 = 60\\%$\nĐáp số: $60\\%$.", "60%", 5, 1.5),
            make_essay(5, "Một cửa hàng nhập về 160 bao xi măng, buổi sáng bán được 48 bao.\na) Số bao xi măng đã bán chiếm bao nhiêu phần trăm tổng số bao xi măng?\nb) Số bao xi măng còn lại chiếm bao nhiêu phần trăm?", "Bài giải:\na) Tỉ số phần trăm xi măng đã bán là:\n$48 : 160 = 0,3 = 30\\%$\nb) Tỉ số phần trăm xi măng còn lại là:\n$100\\% - 30\\% = 70\\%$\nĐáp số: a) $30\\%$; b) $70\\%$.", "a) 30%; b) 70%", 5, 1.5),
            make_essay(6, "Một mảnh đất có diện tích $250\\text{ m}^2$, người ta sử dụng $75\\text{ m}^2$ để xây nhà, còn lại làm sân và vườn. Hỏi diện tích đất xây nhà chiếm bao nhiêu phần trăm diện tích đất làm sân và vườn?", "Bài giải:\nDiện tích đất làm sân và vườn là:\n$250 - 75 = 175\\text{ (m}^2)$\nTỉ số phần trăm đất xây nhà so với đất sân vườn là:\n$75 : 175 = \\frac{75}{175} = \\frac{3}{7} \\approx 0,4285 = 42,85\\%$\n(hoặc tỉ số là $\\frac{3}{7} = 42,85\\%$).\nĐáp số: $42,85\\%$ (hay $\\frac{300}{7}\\%$).", "42,85% (hoặc 3/7)", 5, 1.0)
        ]
    }

    # --- Bài 30 - Đề 3 ---
    exams["th5_b30_test3"] = {
        "id": "th5_b30_test3",
        "lessonId": "th5_b30",
        "lessonNum": 30,
        "testNum": 3,
        "title": "Bài 30: Tỉ số và tỉ số phần trăm - Đề số 3",
        "topic": "Tỉ số và tỉ số phần trăm",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Viết phân số $\\frac{7}{10}$ dưới dạng tỉ số phần trăm:", ["7%", "70%", "0,7%", "700%"], 1, "$\\frac{7}{10} = \\frac{70}{100} = 70\\%$."),
            make_mc(2, "Số thập phân $0,004$ bằng bao nhiêu phần trăm?", ["0,04%", "0,4%", "4%", "40%"], 1, "$0,004 = 0,4\\%$."),
            make_mc(3, "Tỉ số phần trăm biểu thị phần còn lại của một sản phẩm khi đã bớt đi $32\\%$ là:", ["68%", "78%", "58%", "62%"], 0, "$100\\% - 32\\% = 68\\%$."),
            make_mc(4, "Một người làm được 8 sản phẩm trong số 10 sản phẩm được giao. Người đó đã hoàn thành được:", ["8%", "80%", "18%", "85%"], 1, "$8 : 10 = 0,8 = 80\\%$."),
            make_mc(5, "So sánh: $25\\% \\times 4 \\dots 100\\%$. Dấu thích hợp là:", ["$<$", "$>$", "$=$", "Không so sánh được"], 2, "$25\\% \\times 4 = 100\\%$ nên hai vế bằng nhau."),
            make_mc(6, "Trong 40 học sinh có 10 học sinh giỏi. Tỉ số phần trăm học sinh giỏi là:", ["10%", "20%", "25%", "40%"], 2, "$10 : 40 = 0,25 = 25\\%$.")
        ],
        "part2": [
            make_essay(1, "Thực hiện các phép tính sau:\na) $18,5\\% \\times 4$\nb) $84\\% : 6$", "a) $18,5\\% \\times 4 = 74\\%$\nb) $84\\% : 6 = 14\\%$", "a) 74%; b) 14%", 4, 1.0),
            make_essay(2, "Điền dấu ($<, >, =$) thích hợp vào chỗ chấm:\na) $0,45 \\dots 40\\%$\nb) $1,2 \\dots 120\\%$", "a) $0,45 = 45\\% > 40\\%$\nb) $1,2 = 120\\% = 120\\%$", "a) >; b) =", 4, 1.0),
            make_essay(3, "Tìm $x$ biết:\n$x + 25\\% = 80\\%$", "Ta có:\n$x = 80\\% - 25\\%$\n$x = 55\\%$ (hay $x = 0,55$).\nĐáp số: $x = 55\\%$.", "x = 55%", 4, 1.0),
            make_essay(4, "Một hộp bút có 25 chiếc bút gồm bút bi xanh và bút bi đỏ, trong đó có 16 chiếc bút bi xanh. Hỏi số bút bi xanh chiếm bao nhiêu phần trăm tổng số bút trong hộp?", "Bài giải:\nTỉ số phần trăm số bút bi xanh là:\n$16 : 25 = 0,64 = 64\\%$\nĐáp số: $64\\%$.", "64%", 5, 1.5),
            make_essay(5, "Đội văn nghệ trường có 40 bạn, trong đó có 26 bạn nữ.\na) Tìm tỉ số phần trăm của số bạn nữ so với số thành viên toàn đội.\nb) Tìm tỉ số phần trăm của số bạn nam so với số thành viên toàn đội.", "Bài giải:\na) Tỉ số phần trăm số bạn nữ là:\n$26 : 40 = 0,65 = 65\\%$\nb) Tỉ số phần trăm số bạn nam là:\n$100\\% - 65\\% = 35\\%$\nĐáp số: a) $65\\%$; b) $35\\%$.", "a) 65%; b) 35%", 5, 1.5),
            make_essay(6, "Một người gửi tiết kiệm $50\\,000\\,000$ đồng, sau 1 năm nhận được số tiền lãi là $3\\,000\\,000$ đồng. Hỏi tỉ số phần trăm giữa tiền lãi và tiền gửi ban đầu là bao nhiêu?", "Bài giải:\nTỉ số phần trăm giữa tiền lãi và tiền gửi là:\n$3\\,000\\,000 : 50\\,000\\,000 = 0,06 = 6\\%$\nĐáp số: $6\\%$.", "6%", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 31: TÌM TỈ SỐ PHẦN TRĂM CỦA HAI SỐ
    # =========================================================================

    # --- Bài 31 - Đề 1 ---
    exams["th5_b31_test1"] = {
        "id": "th5_b31_test1",
        "lessonId": "th5_b31",
        "lessonNum": 31,
        "testNum": 1,
        "title": "Bài 31: Tìm tỉ số phần trăm của hai số - Đề số 1",
        "topic": "Tìm tỉ số phần trăm của hai số",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tìm tỉ số phần trăm của hai số 12 và 40:", ["30%", "25%", "35%", "40%"], 0, "$12 : 40 = 0,3 = 30\\%$."),
            make_mc(2, "Một lớp có 32 học sinh, trong đó có 24 bạn đạt điểm 10. Tỉ số phần trăm của số bạn đạt điểm 10 là:", ["70%", "75%", "80%", "85%"], 1, "$24 : 32 = 0,75 = 75\\%$."),
            make_mc(3, "Tỉ số phần trăm của 1,6 và 80 là:", ["20%", "2%", "0,2%", "200%"], 1, "$1,6 : 80 = 0,02 = 2\\%$."),
            make_mc(4, "Một người gieo 100 hạt mầm có 92 hạt nảy mầm. Tỉ số phần trăm hạt nảy mầm là:", ["9,2%", "92%", "8%", "90%"], 1, "$92 : 100 = 92\\%$."),
            make_mc(5, "Tìm tỉ số phần trăm của 0,3 và 0,5:", ["60%", "15%", "6%", "65%"], 0, "$0,3 : 0,5 = 0,6 = 60\\%$."),
            make_mc(6, "Bác Nam nuôi 50 con vịt, trong đó có 15 con vịt trắng. Tỉ số phần trăm vịt trắng so với cả đàn là:", ["15%", "25%", "30%", "35%"], 2, "$15 : 50 = 0,3 = 30\\%$.")
        ],
        "part2": [
            make_essay(1, "Tính tỉ số phần trăm của hai số (phần thập phân lấy đến hai chữ số nếu có):\na) 16 và 64\nb) 27 và 45", "a) $16 : 64 = 0,25 = 25\\%$\nb) $27 : 45 = 0,6 = 60\\%$", "a) 25%; b) 60%", 4, 1.0),
            make_essay(2, "Tính tỉ số phần trăm của:\na) $2,8\\text{ kg}$ và $7\\text{ kg}$\nb) $15\\text{ m}$ và $40\\text{ m}$", "a) $2,8 : 7 = 0,4 = 40\\%$\nb) $15 : 40 = 0,375 = 37,5\\%$", "a) 40%; b) 37,5%", 4, 1.0),
            make_essay(3, "Một xưởng cơ khí theo kế hoạch phải làm 500 chi tiết máy, đến nay đã làm được 420 chi tiết máy. Hỏi xưởng đó đã làm được bao nhiêu phần trăm kế hoạch?", "Bài giải:\nTỉ số phần trăm kế hoạch đã hoàn thành là:\n$420 : 500 = 0,84 = 84\\%$\nĐáp số: $84\\%$.", "84%", 4, 1.0),
            make_essay(4, "Một cửa hàng gạo nhập về 800 kg gạo, ngày thứ nhất bán được 280 kg gạo. Hỏi số gạo ngày thứ nhất bán chiếm bao nhiêu phần trăm tổng số gạo cửa hàng nhập về?", "Bài giải:\nTỉ số phần trăm số gạo bán ngày thứ nhất so với tổng số gạo nhập về là:\n$280 : 800 = 0,35 = 35\\%$\nĐáp số: $35\\%$.", "35%", 5, 1.5),
            make_essay(5, "Khảo sát 120 học sinh khối lớp 5 về môn thể thao yêu thích thì thấy có 54 bạn thích bóng rổ, 42 bạn thích bơi lội, còn lại thích cờ vua.\na) Tỉ số phần trăm số học sinh thích bóng rổ so với khối 5 là bao nhiêu?\nb) Tỉ số phần trăm số học sinh thích cờ vua so với khối 5 là bao nhiêu?", "Bài giải:\na) Tỉ số phần trăm bạn thích bóng rổ là:\n$54 : 120 = 0,45 = 45\\%$\nb) Số bạn thích cờ vua là:\n$120 - (54 + 42) = 24\\text{ (học sinh)}$\nTỉ số phần trăm bạn thích cờ vua là:\n$24 : 120 = 0,2 = 20\\%$\nĐáp số: a) $45\\%$; b) $20\\%$.", "a) 45%; b) 20%", 5, 1.5),
            make_essay(6, "Một mảnh vườn hình chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $16\\text{ m}$. Người ta dành $80\\text{ m}^2$ đất để đào ao. Hỏi diện tích ao chiếm bao nhiêu phần trăm diện tích mảnh vườn?", "Bài giải:\nDiện tích mảnh vườn là:\n$25 \\times 16 = 400\\text{ (m}^2)$\nTỉ số phần trăm diện tích ao so với diện tích vườn là:\n$80 : 400 = 0,2 = 20\\%$\nĐáp số: $20\\%$.", "20%", 5, 1.0)
        ]
    }

    # --- Bài 31 - Đề 2 ---
    exams["th5_b31_test2"] = {
        "id": "th5_b31_test2",
        "lessonId": "th5_b31",
        "lessonNum": 31,
        "testNum": 2,
        "title": "Bài 31: Tìm tỉ số phần trăm của hai số - Đề số 2",
        "topic": "Tìm tỉ số phần trăm của hai số",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tìm tỉ số phần trăm của hai số 21 và 28:", ["70%", "75%", "80%", "65%"], 1, "$21 : 28 = 0,75 = 75\\%$."),
            make_mc(2, "Tìm tỉ số phần trăm của 3,2 và 4:", ["75%", "80%", "85%", "70%"], 1, "$3,2 : 4 = 0,8 = 80\\%$."),
            make_mc(3, "Một đội sản xuất có 25 người, trong đó có 15 nữ. Tỉ số phần trăm của nữ so với cả đội là:", ["50%", "60%", "40%", "55%"], 1, "$15 : 25 = 0,6 = 60\\%$."),
            make_mc(4, "Một vườn có 200 cây cam, có 170 cây đã cho quả. Tỉ số phần trăm cây đã cho quả là:", ["85%", "80%", "75%", "90%"], 0, "$170 : 200 = 0,85 = 85\\%$."),
            make_mc(5, "Tỉ số phần trăm của 45 và 60 là:", ["75%", "80%", "70%", "65%"], 0, "$45 : 60 = 0,75 = 75\\%$."),
            make_mc(6, "Nước biển chứa $3,5\\%$ muối. Có bao nhiêu gam muối trong 200 gam nước biển?", ["7 gam", "3,5 gam", "14 gam", "70 gam"], 0, "$200 \\times 3,5 : 100 = 7\\text{ gam}$.")
        ],
        "part2": [
            make_essay(1, "Tìm tỉ số phần trăm của hai số:\na) 19 và 50\nb) 45 và 150", "a) $19 : 50 = 0,38 = 38\\%$\nb) $45 : 150 = 0,3 = 30\\%$", "a) 38%; b) 30%", 4, 1.0),
            make_essay(2, "Tính tỉ số phần trăm của hai đại lượng:\na) $1,5\\text{ m}$ và $6\\text{ m}$\nb) $360\\text{ m}^2$ và $1200\\text{ m}^2$", "a) $1,5 : 6 = 0,25 = 25\\%$\nb) $360 : 1200 = 0,3 = 30\\%$", "a) 25%; b) 30%", 4, 1.0),
            make_essay(3, "Một trang trại ươm 500 cây giống, sau một tháng có 475 cây phát triển tốt. Hỏi tỉ số phần trăm số cây giống phát triển tốt là bao nhiêu?", "Bài giải:\nTỉ số phần trăm số cây phát triển tốt là:\n$475 : 500 = 0,95 = 95\\%$\nĐáp số: $95\\%$.", "95%", 4, 1.0),
            make_essay(4, "Một người bán một chiếc xe đạp cũ được $1\\,200\\,000$ đồng, số tiền vốn mua xe là $1\\,000\\,000$ đồng. Hỏi người đó đã bán chiếc xe với giá bằng bao nhiêu phần trăm giá vốn?", "Bài giải:\nTỉ số phần trăm giá bán so với giá vốn là:\n$1\\,200\\,000 : 1\\,000\\,000 = 1,2 = 120\\%$\nĐáp số: $120\\%$.", "120%", 5, 1.5),
            make_essay(5, "Một cửa hàng có 600 hộp bánh. Tuần thứ nhất bán được 150 hộp, tuần thứ hai bán được 210 hộp.\na) Số hộp bánh bán trong hai tuần chiếm bao nhiêu phần trăm tổng số bánh cửa hàng có?\nb) Số bánh còn lại chiếm bao nhiêu phần trăm?", "Bài giải:\na) Tổng số hộp bánh đã bán trong hai tuần là:\n$150 + 210 = 360\\text{ (hộp)}$\nTỉ số phần trăm bánh đã bán là:\n$360 : 600 = 0,6 = 60\\%$\nb) Tỉ số phần trăm số bánh còn lại là:\n$100\\% - 60\\% = 40\\%$\nĐáp số: a) $60\\%$; b) $40\\%$.", "a) 60%; b) 40%", 5, 1.5),
            make_essay(6, "Năm ngoái gia đình bác Hà thu hoạch được 5 tấn thóc. Năm nay nhờ áp dụng kĩ thuật mới nên thu hoạch được 5,75 tấn thóc. Hỏi năm nay lượng thóc thu hoạch của gia đình bác Hà tăng thêm bao nhiêu phần trăm so với năm ngoái?", "Bài giải:\nLượng thóc tăng thêm trong năm nay là:\n$5,75 - 5 = 0,75\\text{ (tấn)}$\nTỉ số phần trăm lượng thóc tăng thêm so với năm ngoái là:\n$0,75 : 5 = 0,15 = 15\\%$\nĐáp số: $15\\%$.", "15%", 5, 1.0)
        ]
    }

    # --- Bài 31 - Đề 3 ---
    exams["th5_b31_test3"] = {
        "id": "th5_b31_test3",
        "lessonId": "th5_b31",
        "lessonNum": 31,
        "testNum": 3,
        "title": "Bài 31: Tìm tỉ số phần trăm của hai số - Đề số 3",
        "topic": "Tìm tỉ số phần trăm của hai số",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tìm tỉ số phần trăm của 14 và 35:", ["35%", "40%", "45%", "50%"], 1, "$14 : 35 = 0,4 = 40\\%$."),
            make_mc(2, "Tỉ số phần trăm của 0,72 và 1,2 là:", ["6%", "60%", "65%", "70%"], 1, "$0,72 : 1,2 = 0,6 = 60\\%$."),
            make_mc(3, "Một khu rừng có 800 ha, người ta đã trồng mới 240 ha rừng. Tỉ lệ rừng trồng mới chiếm:", ["24%", "30%", "35%", "40%"], 1, "$240 : 800 = 0,3 = 30\\%$."),
            make_mc(4, "Một người bắn bia 20 phát thì có 17 phát trúng đích. Tỉ số phần trăm phát bắn trúng đích là:", ["85%", "75%", "80%", "90%"], 0, "$17 : 20 = 0,85 = 85\\%$."),
            make_mc(5, "Tỉ số phần trăm của hai số 4 và 5 là:", ["80%", "75%", "125%", "20%"], 0, "$4 : 5 = 0,8 = 80\\%$."),
            make_mc(6, "Tỉ số phần trăm của 5 so với 4 là:", ["80%", "120%", "125%", "100%"], 2, "$5 : 4 = 1,25 = 125\\%$.")
        ],
        "part2": [
            make_essay(1, "Tính tỉ số phần trăm của hai số sau:\na) 33 và 75\nb) 1,4 và 2,8", "a) $33 : 75 = 0,44 = 44\\%$\nb) $1,4 : 2,8 = 0,5 = 50\\%$", "a) 44%; b) 50%", 4, 1.0),
            make_essay(2, "Tính tỉ số phần trăm của:\na) $45\\text{ phút}$ và $1\\text{ giờ}$\nb) $350\\text{ kg}$ và $1\\text{ tấn}$", "a) Đổi $1\\text{ giờ} = 60\\text{ phút}$. Tỉ số: $45 : 60 = 0,75 = 75\\%$.\nb) Đổi $1\\text{ tấn} = 1000\\text{ kg}$. Tỉ số: $350 : 1000 = 0,35 = 35\\%$.", "a) 75%; b) 35%", 4, 1.0),
            make_essay(3, "Một trường học có 600 học sinh, trong đó có 480 học sinh đạt danh hiệu Cháu ngoan Bác Hồ. Tìm tỉ số phần trăm số học sinh đạt danh hiệu Cháu ngoan Bác Hồ của trường.", "Bài giải:\nTỉ số phần trăm số học sinh đạt danh hiệu là:\n$480 : 600 = 0,8 = 80\\%$\nĐáp số: $80\\%$.", "80%", 4, 1.0),
            make_essay(4, "Một người thợ đóng giày được giao làm 250 đôi giày. Tuần đầu làm được 90 đôi, tuần thứ hai làm được 110 đôi. Hỏi người thợ đó đã hoàn thành bao nhiêu phần trăm công việc được giao?", "Bài giải:\nTổng số đôi giày người thợ đã làm được là:\n$90 + 110 = 200\\text{ (đôi)}$\nTỉ số phần trăm công việc đã hoàn thành là:\n$200 : 250 = 0,8 = 80\\%$\nĐáp số: $80\\%$.", "80%", 5, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có chiều dài $20\\text{ m}$, chiều rộng $15\\text{ m}$. Người ta dùng $60\\text{ m}^2$ diện tích đất để làm lối đi và sân phơi.\na) Tính diện tích mảnh đất hình chữ nhật đó.\nb) Diện tích phần đất làm lối đi và sân phơi chiếm bao nhiêu phần trăm diện tích mảnh đất?", "Bài giải:\na) Diện tích mảnh đất là:\n$20 \\times 15 = 300\\text{ (m}^2)$\nb) Tỉ số phần trăm đất làm lối đi và sân phơi là:\n$60 : 300 = 0,2 = 20\\%$\nĐáp số: a) $300\\text{ m}^2$; b) $20\\%$.", "a) 300 m²; b) 20%", 5, 1.5),
            make_essay(6, "Bác Ba gửi ngân hàng $80\\,000\\,000$ đồng. Sau một năm số tiền nhận về cả gốc và lãi là $84\\,800\\,000$ đồng. Hỏi lãi suất tiền gửi của ngân hàng đó là bao nhiêu phần trăm một năm?", "Bài giải:\nSố tiền lãi bác Ba nhận được sau một năm là:\n$84\\,800\\,000 - 80\\,000\\,000 = 4\\,800\\,000\\text{ (đồng)}$\nLãi suất gửi tiết kiệm một năm là:\n$4\\,800\\,000 : 80\\,000\\,000 = 0,06 = 6\\%$\nĐáp số: $6\\%$/năm.", "6%/năm", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 32: TÌM GIÁ TRỊ PHẦN TRĂM CỦA MỘT SỐ
    # =========================================================================

    # --- Bài 32 - Đề 1 ---
    exams["th5_b32_test1"] = {
        "id": "th5_b32_test1",
        "lessonId": "th5_b32",
        "lessonNum": 32,
        "testNum": 1,
        "title": "Bài 32: Tìm giá trị phần trăm của một số - Đề số 1",
        "topic": "Tìm giá trị phần trăm của một số",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tìm $20\\%$ của 150:", ["20", "30", "40", "25"], 1, "$150 \\times 20 : 100 = 30$."),
            make_mc(2, "Tìm $15\\%$ của $240\\text{ kg}$:", ["36 kg", "30 kg", "24 kg", "48 kg"], 0, "$240 \\times 15 : 100 = 36\\text{ kg}$."),
            make_mc(3, "Một mảnh vườn có diện tích $500\\text{ m}^2$, người ta dành $35\\%$ diện tích để trồng hoa. Diện tích trồng hoa là:", ["150 m²", "165 m²", "175 m²", "200 m²"], 2, "$500 \\times 35 : 100 = 175\\text{ m}^2$."),
            make_mc(4, "Một trường tiểu học có 800 học sinh, trong đó có $52\\%$ học sinh nữ. Số học sinh nữ là:", ["416 bạn", "384 bạn", "400 bạn", "420 bạn"], 0, "$800 \\times 52 : 100 = 416$ (bạn)."),
            make_mc(5, "Tìm $0,5\\%$ của 600:", ["30", "3", "0,3", "300"], 1, "$600 \\times 0,5 : 100 = 3$."),
            make_mc(6, "Chiếc áo giá $200\\,000$ đồng, nhân dịp lễ được giảm $10\\%$. Số tiền được giảm là:", ["10 000 đồng", "20 000 đồng", "30 000 đồng", "15 000 đồng"], 1, "$200\\,000 \\times 10 : 100 = 20\\,000$ đồng.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị phần trăm sau:\na) $25\\%$ của 180\nb) $40\\%$ của 250 m", "a) $180 \\times 25 : 100 = 45$\nb) $250 \\times 40 : 100 = 100\\text{ (m)}$", "a) 45; b) 100 m", 4, 1.0),
            make_essay(2, "Tính:\na) $12\\%$ của 500 kg\nb) $35\\%$ của 120 lít", "a) $500 \\times 12 : 100 = 60\\text{ (kg)}$\nb) $120 \\times 35 : 100 = 42\\text{ (lít)}$", "a) 60 kg; b) 42 lít", 4, 1.0),
            make_essay(3, "Một cửa hàng có $1200\\text{ kg}$ gạo tẻ. Cửa hàng đã bán được $30\\%$ số gạo đó. Hỏi cửa hàng đã bán được bao nhiêu ki-lô-gam gạo tẻ?", "Bài giải:\nSố gạo tẻ cửa hàng đã bán là:\n$1200 \\times 30 : 100 = 360\\text{ (kg)}$\nĐáp số: 360 kg.", "360 kg", 4, 1.0),
            make_essay(4, "Một mảnh đất hình chữ nhật có chiều dài $30\\text{ m}$, chiều rộng $20\\text{ m}$. Người ta dùng $45\\%$ diện tích để xây nhà. Tính diện tích phần đất dùng để xây nhà.", "Bài giải:\nDiện tích mảnh đất hình chữ nhật là:\n$30 \\times 20 = 600\\text{ (m}^2)$\nDiện tích phần đất xây nhà là:\n$600 \\times 45 : 100 = 270\\text{ (m}^2)$\nĐáp số: $270\\text{ m}^2$.", "270 m²", 5, 1.5),
            make_essay(5, "Một người gửi tiết kiệm $60\\,000\\,000$ đồng với lãi suất $0,5\\%$ một tháng.\na) Sau một tháng, người đó nhận được bao nhiêu tiền lãi?\nb) Sau một tháng, cả tiền gốc và tiền lãi người đó nhận được là bao nhiêu?", "Bài giải:\na) Số tiền lãi sau một tháng là:\n$60\\,000\\,000 \\times 0,5 : 100 = 300\\,000\\text{ (đồng)}$\nb) Sau một tháng, tổng số tiền nhận được là:\n$60\\,000\\,000 + 300\\,000 = 60\\,300\\,000\\text{ (đồng)}$\nĐáp số:\na) $300\\,000\\text{ đồng}$;\nb) $60\\,300\\,000\\text{ đồng}$.", "a) 300 000 đồng; b) 60 300 000 đồng", 5, 1.5),
            make_essay(6, "Một cửa hàng bán ti vi niêm yết giá $8\\,000\\,000$ đồng. Nhân dịp cuối năm, cửa hàng giảm giá $15\\%$. Hỏi người mua chiếc ti vi đó phải trả bao nhiêu tiền?", "Bài giải:\nSố tiền được giảm giá khi mua ti vi là:\n$8\\,000\\,000 \\times 15 : 100 = 1\\,200\\,000\\text{ (đồng)}$\nSố tiền khách hàng phải trả là:\n$8\\,000\\,000 - 1\\,200\\,000 = 6\\,800\\,000\\text{ (đồng)}$\nĐáp số: $6\\,800\\,000\\text{ đồng}$.", "6 800 000 đồng", 5, 1.0)
        ]
    }

    # --- Bài 32 - Đề 2 ---
    exams["th5_b32_test2"] = {
        "id": "th5_b32_test2",
        "lessonId": "th5_b32",
        "lessonNum": 32,
        "testNum": 2,
        "title": "Bài 32: Tìm giá trị phần trăm của một số - Đề số 2",
        "topic": "Tìm giá trị phần trăm của một số",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tìm $30\\%$ của 90:", ["27", "30", "18", "36"], 0, "$90 \\times 30 : 100 = 27$."),
            make_mc(2, "Tìm $75\\%$ của $200\\text{ m}$:", ["120 m", "150 m", "160 m", "175 m"], 1, "$200 \\times 75 : 100 = 150\\text{ m}$."),
            make_mc(3, "Một bao ngô nặng $60\\text{ kg}$. Lượng nước trong hạt ngô chiếm $15\\%$. Khối lượng nước trong bao ngô đó là:", ["6 kg", "8 kg", "9 kg", "12 kg"], 2, "$60 \\times 15 : 100 = 9\\text{ kg}$."),
            make_mc(4, "Một cuốn sách giá $80\\,000$ đồng, được giảm $20\\%$. Số tiền người mua phải trả là:", ["16 000 đồng", "60 000 đồng", "64 000 đồng", "70 000 đồng"], 2, "$80\\,000 \\times (100\\% - 20\\%) : 100 = 64\\,000$ đồng."),
            make_mc(5, "Tìm $12,5\\%$ của 400 lít:", ["40 lít", "50 lít", "60 lít", "45 lít"], 1, "$400 \\times 12,5 : 100 = 50$ lít."),
            make_mc(6, "Trong bình có 500 ml nước đường, đường chiếm $8\\%$. Khối lượng đường có trong bình là:", ["40 ml", "4 ml", "50 ml", "8 ml"], 0, "$500 \\times 8 : 100 = 40$ ml.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị phần trăm sau:\na) $18\\%$ của 250\nb) $65\\%$ của 160 kg", "a) $250 \\times 18 : 100 = 45$\nb) $160 \\times 65 : 100 = 104\\text{ (kg)}$", "a) 45; b) 104 kg", 4, 1.0),
            make_essay(2, "Tính:\na) $2,5\\%$ của 400 m\nb) $80\\%$ của 350 lít", "a) $400 \\times 2,5 : 100 = 10\\text{ (m)}$\nb) $350 \\times 80 : 100 = 280\\text{ (lít)}$", "a) 10 m; b) 280 lít", 4, 1.0),
            make_essay(3, "Một trang trại nuôi 1500 con vịt. Đợt vừa rồi trang trại đã xuất chuồng $40\\%$ số vịt. Hỏi trang trại đó đã xuất chuồng bao nhiêu con vịt?", "Bài giải:\nSố con vịt trang trại đã xuất chuồng là:\n$1500 \\times 40 : 100 = 600\\text{ (con)}$\nĐáp số: 600 con vịt.", "600 con", 4, 1.0),
            make_essay(4, "Một mảnh đất có diện tích $800\\text{ m}^2$. Người ta dùng $30\\%$ diện tích để trồng rau cải, $45\\%$ diện tích để trồng cà chua, diện tích còn lại làm lối đi. Tính diện tích đất dùng làm lối đi.", "Bài giải:\nTỉ số phần trăm đất làm lối đi là:\n$100\\% - (30\\% + 45\\%) = 25\\%$\nDiện tích đất làm lối đi là:\n$800 \\times 25 : 100 = 200\\text{ (m}^2)$\nĐáp số: $200\\text{ m}^2$.", "200 m²", 5, 1.5),
            make_essay(5, "Bác Minh gửi tiết kiệm ngân hàng $100\\,000\\,000$ đồng kỳ hạn 1 năm với lãi suất $6,5\\%$ một năm.\na) Sau 1 năm bác Minh nhận được bao nhiêu tiền lãi?\nb) Hết 1 năm, cả gốc lẫn lãi bác Minh rút về là bao nhiêu tiền?", "Bài giải:\na) Sau 1 năm, tiền lãi bác Minh nhận được là:\n$100\\,000\\,000 \\times 6,5 : 100 = 6\\,500\\,000\\text{ (đồng)}$\nb) Cả gốc lẫn lãi bác Minh rút về là:\n$100\\,000\\,000 + 6\\,500\\,000 = 106\\,500\\,000\\text{ (đồng)}$\nĐáp số:\na) $6\\,500\\,000\\text{ đồng}$;\nb) $106\\,500\\,000\\text{ đồng}$.", "a) 6 500 000 đồng; b) 106 500 000 đồng", 5, 1.5),
            make_essay(6, "Một cái quạt điện có giá niêm yết $500\\,000$ đồng. Trong chương trình tri ân, cửa hàng giảm giá $12\\%$. Bạn An mua chiếc quạt đó và đưa cho thu ngân tờ tiền $500\\,000$ đồng. Hỏi bạn An được trả lại bao nhiêu tiền?", "Bài giải:\nSố tiền được giảm giá là:\n$500\\,000 \\times 12 : 100 = 60\\,000\\text{ (đồng)}$\nSố tiền An phải trả cho chiếc quạt là:\n$500\\,000 - 60\\,000 = 440\\,000\\text{ (đồng)}$\nSố tiền thu ngân trả lại cho An là:\n$500\\,000 - 440\\,000 = 60\\,000\\text{ (đồng)}$\nĐáp số: $60\\,000\\text{ đồng}$.", "60 000 đồng", 5, 1.0)
        ]
    }

    # --- Bài 32 - Đề 3 ---
    exams["th5_b32_test3"] = {
        "id": "th5_b32_test3",
        "lessonId": "th5_b32",
        "lessonNum": 32,
        "testNum": 3,
        "title": "Bài 32: Tìm giá trị phần trăm của một số - Đề số 3",
        "topic": "Tìm giá trị phần trăm của một số",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tìm $50\\%$ của 320:", ["150", "160", "170", "180"], 1, "$320 \\times 50 : 100 = 160$."),
            make_mc(2, "Tìm $24\\%$ của 250:", ["50", "55", "60", "65"], 2, "$250 \\times 24 : 100 = 60$."),
            make_mc(3, "Một đàn bò có 120 con, trong đó số bê con chiếm $25\\%$. Số bê con là:", ["25 con", "30 con", "35 con", "40 con"], 1, "$120 \\times 25 : 100 = 30$ con."),
            make_mc(4, "Một thùng chứa 200 lít dầu, người ta lấy ra $35\\%$ số dầu đó. Lượng dầu lấy ra là:", ["60 lít", "70 lít", "80 lít", "65 lít"], 1, "$200 \\times 35 : 100 = 70$ lít."),
            make_mc(5, "Tìm $105\\%$ của 40:", ["42", "40", "44", "45"], 0, "$40 \\times 105 : 100 = 42$."),
            make_mc(6, "Một đôi giày có giá $400\\,000$ đồng, giảm giá $15\\%$. Giá bán mới của đôi giày là:", ["360 000 đồng", "340 000 đồng", "350 000 đồng", "380 000 đồng"], 1, "$400\\,000 \\times (100\\% - 15\\%) : 100 = 340\\,000$ đồng.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị phần trăm sau:\na) $32\\%$ của 150\nb) $70\\%$ của 120 m", "a) $150 \\times 32 : 100 = 48$\nb) $120 \\times 70 : 100 = 84\\text{ (m)}$", "a) 48; b) 84 m", 4, 1.0),
            make_essay(2, "Tính:\na) $15\\%$ của 160 kg\nb) $4,5\\%$ của 200 lít", "a) $160 \\times 15 : 100 = 24\\text{ (kg)}$\nb) $200 \\times 4,5 : 100 = 9\\text{ (lít)}$", "a) 24 kg; b) 9 lít", 4, 1.0),
            make_essay(3, "Một xưởng dệt được 2400 mét vải. Người ta đã xuất bán $60\\%$ số vải đó. Hỏi trong xưởng còn lại bao nhiêu mét vải?", "Bài giải:\nTỉ số phần trăm số vải còn lại trong xưởng là:\n$100\\% - 60\\% = 40\\%$\nSố mét vải còn lại trong xưởng là:\n$2400 \\times 40 : 100 = 960\\text{ (m)}$\nĐáp số: 960 m.", "960 m", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chu vi $140\\text{ m}$, chiều dài hơn chiều rộng $10\\text{ m}$. Người ta dành $30\\%$ diện tích mảnh vườn để trồng dưa hấu. Tính diện tích phần đất trồng dưa hấu.", "Bài giải:\nNửa chu vi mảnh vườn là:\n$140 : 2 = 70\\text{ (m)}$\nChiều dài mảnh vườn là:\n$(70 + 10) : 2 = 40\\text{ (m)}$\nChiều rộng mảnh vườn là:\n$70 - 40 = 30\\text{ (m)}$\nDiện tích mảnh vườn là:\n$40 \\times 30 = 1200\\text{ (m}^2)$\nDiện tích phần đất trồng dưa hấu là:\n$1200 \\times 30 : 100 = 360\\text{ (m}^2)$\nĐáp số: $360\\text{ m}^2$.", "360 m²", 5, 1.5),
            make_essay(5, "Năm ngoái một cơ sở sản xuất được 800 chiếc xe nôi trẻ em. Năm nay do nhu cầu thị trường tăng, cơ sở sản xuất vượt mức $15\\%$ so với năm ngoái.\na) Năm nay cơ sở đã sản xuất vượt mức bao nhiêu chiếc xe nôi?\nb) Tổng số xe nôi cơ sở sản xuất được trong năm nay là bao nhiêu?", "Bài giải:\na) Số xe nôi sản xuất vượt mức trong năm nay là:\n$800 \\times 15 : 100 = 120\\text{ (chiếc)}$\nb) Tổng số xe nôi cơ sở sản xuất được năm nay là:\n$800 + 120 = 920\\text{ (chiếc)}$\nĐáp số:\na) 120 chiếc;\nb) 920 chiếc.", "a) 120 chiếc; b) 920 chiếc", 5, 1.5),
            make_essay(6, "Một người bán hàng mua một tấm vải giá $300\\,000$ đồng. Sau khi bán hết tấm vải, người đó tính ra được lãi $20\\%$ theo giá mua. Hỏi người đó đã bán tấm vải với giá bao nhiêu tiền?", "Bài giải:\nSố tiền lãi người đó nhận được là:\n$300\\,000 \\times 20 : 100 = 60\\,000\\text{ (đồng)}$\nNgười đó đã bán tấm vải với giá là:\n$300\\,000 + 60\\,000 = 360\\,000\\text{ (đồng)}$\nĐáp số: $360\\,000\\text{ đồng}$.", "360 000 đồng", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 33: SỬ DỤNG MÁY TÍNH CẦM TAY
    # =========================================================================

    # --- Bài 33 - Đề 1 ---
    exams["th5_b33_test1"] = {
        "id": "th5_b33_test1",
        "lessonId": "th5_b33",
        "lessonNum": 33,
        "testNum": 1,
        "title": "Bài 33: Sử dụng máy tính cầm tay - Đề số 1",
        "topic": "Sử dụng máy tính cầm tay",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phím nào trên máy tính cầm tay dùng để bật máy?", ["OFF", "ON", "AC", "C"], 1, "Phím ON dùng để bật máy tính cầm tay."),
            make_mc(2, "Để xóa toàn bộ màn hình tính toán về số 0, ta bấm phím nào?", ["OFF", "AC (hoặc C)", "ON", "="], 1, "Phím AC (All Clear) hoặc C dùng để xóa sạch phép tính trên màn hình."),
            make_mc(3, "Dùng máy tính cầm tay tính: $34,8 + 19,75 = \\dots$", ["54,55", "54,45", "53,55", "55,55"], 0, "$34,8 + 19,75 = 54,55$."),
            make_mc(4, "Dùng máy tính cầm tay tính $25\\%$ của 480 bằng cách bấm $480 \\times 25\\%$ hoặc $480 \\times 25 : 100$, kết quả là:", ["120", "140", "100", "125"], 0, "$480 \\times 25 : 100 = 120$."),
            make_mc(5, "Dùng máy tính cầm tay tính: $128,8 : 5,6 = \\dots$", ["23", "22", "24", "25"], 0, "$128,8 : 5,6 = 23$."),
            make_mc(6, "Để tính tỉ số phần trăm của 13 và 25 bằng máy tính, ta bấm $13 : 25 =$, sau đó nhân 100. Kết quả là:", ["50%", "52%", "54%", "48%"], 1, "$13 : 25 = 0,52 = 52\\%$.")
        ],
        "part2": [
            make_essay(1, "Sử dụng máy tính cầm tay để tính giá trị các biểu thức sau:\na) $24,56 + 18,745$\nb) $89,1 - 42,68$", "a) $24,56 + 18,745 = 43,305$\nb) $89,1 - 42,68 = 46,42$", "a) 43,305; b) 46,42", 4, 1.0),
            make_essay(2, "Sử dụng máy tính cầm tay để tính:\na) $14,6 \\times 3,85$\nb) $76,32 : 3,6$", "a) $14,6 \\times 3,85 = 56,21$\nb) $76,32 : 3,6 = 21,2$", "a) 56,21; b) 21,2", 4, 1.0),
            make_essay(3, "Dùng máy tính cầm tay tìm tỉ số phần trăm của hai số sau (lấy đến 2 chữ số ở phần thập phân):\na) 37 và 80\nb) 45 và 72", "a) $37 : 80 = 0,4625 = 46,25\\%$\nb) $45 : 72 = 0,625 = 62,5\\%$", "a) 46,25%; b) 62,5%", 4, 1.0),
            make_essay(4, "Sử dụng máy tính cầm tay tính giá trị phần trăm của các số sau:\na) $18\\%$ của 650\nb) $34,5\\%$ của 840 kg", "a) $650 \\times 18 : 100 = 117$\nb) $840 \\times 34,5 : 100 = 289,8\\text{ (kg)}$", "a) 117; b) 289,8 kg", 5, 1.5),
            make_essay(5, "Một cửa hàng sách bán được các mặt hàng với doanh thu như sau: Sách giáo khoa $4\\,500\\,000$ đồng; Truyện thiếu nhi $2\\,800\\,000$ đồng; Vở học sinh $1\\,700\\,000$ đồng.\na) Sử dụng máy tính cầm tay tính tổng doanh thu của cửa hàng.\nb) Tính tỉ số phần trăm doanh thu của sách giáo khoa so với tổng doanh thu (lấy phần thập phân 1 chữ số).", "Bài giải:\na) Tổng doanh thu của cửa hàng là:\n$4\\,500\\,000 + 2\\,800\\,000 + 1\\,700\\,000 = 9\\,000\\,000\\text{ (đồng)}$\nb) Tỉ số phần trăm doanh thu sách giáo khoa là:\n$4\\,500\\,000 : 9\\,000\\,000 = 0,5 = 50\\%$\nĐáp số: a) $9\\,000\\,000\\text{ đồng}$; b) $50\\%$.", "a) 9 000 000 đồng; b) 50%", 5, 1.5),
            make_essay(6, "Dùng máy tính cầm tay giải bài toán: Một mảnh vườn hình thang có đáy lớn $48,5\\text{ m}$, đáy bé $32,5\\text{ m}$, chiều cao $24\\text{ m}$. Người ta dùng $40\\%$ diện tích mảnh vườn để trồng xoài. Tính diện tích đất trồng xoài.", "Bài giải:\nDiện tích mảnh vườn hình thang là:\n$(48,5 + 32,5) \\times 24 : 2 = 81 \\times 12 = 972\\text{ (m}^2)$\nDiện tích phần đất trồng xoài là:\n$972 \\times 40 : 100 = 388,8\\text{ (m}^2)$\nĐáp số: $388,8\\text{ m}^2$.", "388,8 m²", 5, 1.0)
        ]
    }

    # --- Bài 33 - Đề 2 ---
    exams["th5_b33_test2"] = {
        "id": "th5_b33_test2",
        "lessonId": "th5_b33",
        "lessonNum": 33,
        "testNum": 2,
        "title": "Bài 33: Sử dụng máy tính cầm tay - Đề số 2",
        "topic": "Sử dụng máy tính cầm tay",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phím nào dùng để tắt máy tính cầm tay?", ["ON", "OFF", "C", "="], 1, "Phím OFF dùng để tắt máy."),
            make_mc(2, "Dùng máy tính cầm tay tính: $125 \\times 0,8 = \\dots$", ["10", "100", "1000", "80"], 1, "$125 \\times 0,8 = 100$."),
            make_mc(3, "Dùng máy tính cầm tay tính: $450 : 12,5 = \\dots$", ["35", "36", "38", "40"], 1, "$450 : 12,5 = 36$."),
            make_mc(4, "Dùng máy tính cầm tay tính tỉ số phần trăm của 18 so với 75:", ["20%", "24%", "25%", "28%"], 1, "$18 : 75 = 0,24 = 24\\%$."),
            make_mc(5, "Tính $16\\%$ của 250 bằng máy tính cầm tay:", ["40", "45", "50", "35"], 0, "$250 \\times 16 : 100 = 40$."),
            make_mc(6, "Thực hiện phép tính $(34,5 + 15,5) \\times 4,2$ bằng máy tính cầm tay, kết quả là:", ["200", "210", "215", "220"], 1, "$50 \\times 4,2 = 210$.")
        ],
        "part2": [
            make_essay(1, "Dùng máy tính cầm tay tính giá trị các biểu thức:\na) $156,4 - 87,65$\nb) $3,45 \\times 12,8$", "a) $156,4 - 87,65 = 68,75$\nb) $3,45 \\times 12,8 = 44,16$", "a) 68,75; b) 44,16", 4, 1.0),
            make_essay(2, "Dùng máy tính tính kết quả của phép chia:\na) $273,6 : 7,6$\nb) $15,81 : 3,1$", "a) $273,6 : 7,6 = 36$\nb) $15,81 : 3,1 = 5,1$", "a) 36; b) 5,1", 4, 1.0),
            make_essay(3, "Dùng máy tính cầm tay tìm tỉ số phần trăm của:\na) 21 và 84\nb) 51 và 68", "a) $21 : 84 = 0,25 = 25\\%$\nb) $51 : 68 = 0,75 = 75\\%$", "a) 25%; b) 75%", 4, 1.0),
            make_essay(4, "Dùng máy tính tính giá trị phần trăm của các đại lượng:\na) $32\\%$ của $450\\text{ kg}$\nb) $15,5\\%$ của $600\\text{ lít}$", "a) $450 \\times 32 : 100 = 144\\text{ (kg)}$\nb) $600 \\times 15,5 : 100 = 93\\text{ (lít)}$", "a) 144 kg; b) 93 lít", 5, 1.5),
            make_essay(5, "Một siêu thị bán hàng có bảng số liệu bán hàng trong ngày: Táo bán được $120\\text{ kg}$, Nho bán được $80\\text{ kg}$, Dưa hấu bán được $300\\text{ kg}$.\na) Dùng máy tính tính tổng số ki-lô-gam hoa quả đã bán trong ngày.\nb) Tính tỉ số phần trăm số ki-lô-gam táo bán được so với tổng số hoa quả.", "Bài giải:\na) Tổng số ki-lô-gam hoa quả bán được là:\n$120 + 80 + 300 = 500\\text{ (kg)}$\nb) Tỉ số phần trăm số ki-lô-gam táo bán được là:\n$120 : 500 = 0,24 = 24\\%$\nĐáp số: a) $500\\text{ kg}$; b) $24\\%$.", "a) 500 kg; b) 24%", 5, 1.5),
            make_essay(6, "Bác Năm mua 4 chiếc lốp ô tô, mỗi chiếc giá $1\\,250\\,000$ đồng. Nhân dịp khuyến mại, cửa hàng giảm $10\\%$ trên tổng hóa đơn. Dùng máy tính tính số tiền bác Năm phải trả.", "Bài giải:\nTổng giá tiền 4 chiếc lốp khi chưa giảm giá là:\n$1\\,250\\,000 \\times 4 = 5\\,000\\,000\\text{ (đồng)}$\nSố tiền được giảm giá $10\\%$ là:\n$5\\,000\\,000 \\times 10 : 100 = 500\\,000\\text{ (đồng)}$\nSố tiền thực tế bác Năm phải trả là:\n$5\\,000\\,000 - 500\\,000 = 4\\,500\\,000\\text{ (đồng)}$\nĐáp số: $4\\,500\\,000\\text{ đồng}$.", "4 500 000 đồng", 5, 1.0)
        ]
    }

    # --- Bài 33 - Đề 3 ---
    exams["th5_b33_test3"] = {
        "id": "th5_b33_test3",
        "lessonId": "th5_b33",
        "lessonNum": 33,
        "testNum": 3,
        "title": "Bài 33: Sử dụng máy tính cầm tay - Đề số 3",
        "topic": "Sử dụng máy tính cầm tay",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Để tính $350 + 280$ trên máy tính cầm tay, ta bấm lần lượt:", ["350, +, 280, =", "350, -, 280, =", "350, *, 280, =", "350, /, 280, ="], 0, "Bấm 3, 5, 0 rồi bấm phím +, sau đó bấm 2, 8, 0 và phím =."),
            make_mc(2, "Dùng máy tính cầm tay tính: $18,4 \\times 5,5 = \\dots$", ["101,2", "102,2", "100,2", "101,5"], 0, "$18,4 \\times 5,5 = 101,2$."),
            make_mc(3, "Dùng máy tính tính tỉ số phần trăm của 27 so với 60:", ["40%", "45%", "50%", "35%"], 1, "$27 : 60 = 0,45 = 45\\%$."),
            make_mc(4, "Dùng máy tính tìm $35\\%$ của $640\\text{ m}$:", ["214 m", "224 m", "234 m", "220 m"], 1, "$640 \\times 35 : 100 = 224\\text{ m}$."),
            make_mc(5, "Dùng máy tính tính: $157,5 : 4,5 = \\dots$", ["35", "36", "34", "38"], 0, "$157,5 : 4,5 = 35$."),
            make_mc(6, "Kết quả của $45,6 + 28,4 : 4$ trên máy tính khoa học (có ưu tiên nhân chia trước) là:", ["52,7", "18,5", "45,7", "50,7"], 0, "Tính chia trước: $28,4 : 4 = 7,1$, sau đó cộng: $45,6 + 7,1 = 52,7$.")
        ],
        "part2": [
            make_essay(1, "Dùng máy tính cầm tay tính giá trị các biểu thức:\na) $235,78 + 94,6$\nb) $300 - 146,85$", "a) $235,78 + 94,6 = 330,38$\nb) $300 - 146,85 = 153,15$", "a) 330,38; b) 153,15", 4, 1.0),
            make_essay(2, "Dùng máy tính cầm tay tính:\na) $45,8 \\times 6,2$\nb) $364,8 : 9,6$", "a) $45,8 \\times 6,2 = 283,96$\nb) $364,8 : 9,6 = 38$", "a) 283,96; b) 38", 4, 1.0),
            make_essay(3, "Dùng máy tính tìm tỉ số phần trăm của hai số (viết kết quả chính xác):\na) 36 và 48\nb) 28 và 70", "a) $36 : 48 = 0,75 = 75\\%$\nb) $28 : 70 = 0,4 = 40\\%$", "a) 75%; b) 40%", 4, 1.0),
            make_essay(4, "Dùng máy tính tính giá trị phần trăm của các số sau:\na) $28\\%$ của 750\nb) $12,5\\%$ của $800\\text{ kg}$", "a) $750 \\times 28 : 100 = 210$\nb) $800 \\times 12,5 : 100 = 100\\text{ (kg)}$", "a) 210; b) 100 kg", 5, 1.5),
            make_essay(5, "Một cửa hàng xăng dầu có bể chứa $5000\\text{ lít}$ xăng. Buổi sáng bán được $1250\\text{ lít}$, buổi chiều bán được $1750\\text{ lít}$.\na) Dùng máy tính tính số lít xăng cửa hàng đã bán trong cả ngày.\nb) Số lít xăng đã bán chiếm bao nhiêu phần trăm dung tích của bể?", "Bài giải:\na) Số lít xăng đã bán trong cả ngày là:\n$1250 + 1750 = 3000\\text{ (lít)}$\nb) Tỉ số phần trăm xăng đã bán so với bể là:\n$3000 : 5000 = 0,6 = 60\\%$\nĐáp số: a) $3000\\text{ lít}$; b) $60\\%$.", "a) 3000 lít; b) 60%", 5, 1.5),
            make_essay(6, "Một mảnh vườn hình chữ nhật có chiều dài $35\\text{ m}$, chiều rộng $22\\text{ m}$. Người ta dành $15\\%$ diện tích mảnh vườn để đào giếng và xây bể nước, diện tích còn lại trồng hoa hồng. Dùng máy tính tính diện tích phần đất trồng hoa hồng.", "Bài giải:\nDiện tích mảnh vườn là:\n$35 \\times 22 = 770\\text{ (m}^2)$\nTỉ số phần trăm đất trồng hoa hồng là:\n$100\\% - 15\\% = 85\\%$\nDiện tích phần đất trồng hoa hồng là:\n$770 \\times 85 : 100 = 654,5\\text{ (m}^2)$\nĐáp số: $654,5\\text{ m}^2$.", "654,5 m²", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 34: LUYỆN TẬP CHUNG CHỦ ĐỀ 6
    # =========================================================================

    # --- Bài 34 - Đề 1 ---
    exams["th5_b34_test1"] = {
        "id": "th5_b34_test1",
        "lessonId": "th5_b34",
        "lessonNum": 34,
        "testNum": 1,
        "title": "Bài 34: Luyện tập chung Chủ đề 6 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 6",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Viết số thập phân $0,725$ dưới dạng tỉ số phần trăm:", ["7,25%", "72,5%", "725%", "0,725%"], 1, "$0,725 = 72,5\\%$."),
            make_mc(2, "Tìm $35\\%$ của $160\\text{ kg}$:", ["56 kg", "50 kg", "60 kg", "52 kg"], 0, "$160 \\times 35 : 100 = 56\\text{ kg}$."),
            make_mc(3, "Một lớp học có 40 học sinh, trong đó có 26 học sinh nữ. Tỉ số phần trăm số học sinh nữ là:", ["60%", "65%", "70%", "55%"], 1, "$26 : 40 = 0,65 = 65\\%$."),
            make_mc(4, "Biết $25\\%$ của số $x$ là 40. Số $x$ là:", ["10", "160", "100", "200"], 1, "$x = 40 : 25 \\times 100 = 160$."),
            make_mc(5, "Một chiếc xe đạp giá $1\\,800\\,000$ đồng, được giảm giá $10\\%$. Số tiền được giảm là:", ["180 000 đồng", "100 000 đồng", "150 000 đồng", "200 000 đồng"], 0, "$1\\,800\\,000 \\times 10 : 100 = 180\\,000$ đồng."),
            make_mc(6, "Tính: $45\\% + 28\\% - 13\\% = \\dots$", ["50%", "60%", "65%", "55%"], 1, "$45\\% + 28\\% - 13\\% = 73\\% - 13\\% = 60\\%$.")
        ],
        "part2": [
            make_essay(1, "Thực hiện phép tính:\na) $45,8\\% + 27,6\\%$\nb) $80\\% - 34,5\\%", "a) $45,8\\% + 27,6\\% = 73,4\\%$\nb) $80\\% - 34,5\\% = 45,5\\%$", "a) 73,4%; b) 45,5%", 4, 1.0),
            make_essay(2, "Tính:\na) $25\\%$ của $360\\text{ m}$\nb) Tỉ số phần trăm của 18 và 72", "a) $360 \\times 25 : 100 = 90\\text{ (m)}$\nb) $18 : 72 = 0,25 = 25\\%$", "a) 90 m; b) 25%", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x \\times 20\\% = 35$", "Ta có:\n$x = 35 : 20\\% = 35 : 0,2 = 175$.\nĐáp số: $x = 175$.", "x = 175", 4, 1.0),
            make_essay(4, "Một trang trại nuôi 1200 con gà và vịt, trong đó số gà chiếm $45\\%$.\na) Tính số con gà của trang trại.\nb) Tính số con vịt của trang trại.", "Bài giải:\na) Số con gà của trang trại là:\n$1200 \\times 45 : 100 = 540\\text{ (con)}$\nb) Số con vịt của trang trại là:\n$1200 - 540 = 660\\text{ (con)}$\nĐáp số:\na) 540 con gà;\nb) 660 con vịt.", "a) 540 con; b) 660 con", 5, 1.5),
            make_essay(5, "Một khu vườn hình chữ nhật có chiều dài $50\\text{ m}$, chiều rộng $30\\text{ m}$. Người ta dành $20\\%$ diện tích để đào ao nuôi cá, $50\\%$ diện tích để trồng cây ăn quả, diện tích còn lại làm lối đi.\na) Tính diện tích khu vườn.\nb) Tính diện tích phần đất làm lối đi.", "Bài giải:\na) Diện tích khu vườn hình chữ nhật là:\n$50 \\times 30 = 1500\\text{ (m}^2)$\nb) Tỉ số phần trăm đất làm lối đi là:\n$100\\% - (20\\% + 50\\%) = 30\\%$\nDiện tích phần đất làm lối đi là:\n$1500 \\times 30 : 100 = 450\\text{ (m}^2)$\nĐáp số:\na) $1500\\text{ m}^2$;\nb) $450\\text{ m}^2$.", "a) 1500 m²; b) 450 m²", 5, 1.5),
            make_essay(6, "Bác Năm mua một chiếc máy giặt với giá $6\\,000\\,000$ đồng. Cửa hàng giảm giá $10\\%$. Sau đó bác được giảm thêm $2\\%$ trên số tiền đã giảm vì thanh toán qua thẻ ngân hàng. Hỏi bác Năm đã mua chiếc máy giặt đó với giá bao nhiêu tiền?", "Bài giải:\nGiá chiếc máy giặt sau lần giảm thứ nhất là:\n$6\\,000\\,000 \\times (100\\% - 10\\%) : 100 = 5\\,400\\,000\\text{ (đồng)}$\nSố tiền bác được giảm thêm khi thanh toán thẻ là:\n$5\\,400\\,000 \\times 2 : 100 = 108\\,000\\text{ (đồng)}$\nSố tiền bác Năm phải trả là:\n$5\\,400\\,000 - 108\\,000 = 5\\,292\\,000\\text{ (đồng)}$\nĐáp số: $5\\,292\\,000\\text{ đồng}$.", "5 292 000 đồng", 5, 1.0)
        ]
    }

    # --- Bài 34 - Đề 2 ---
    exams["th5_b34_test2"] = {
        "id": "th5_b34_test2",
        "lessonId": "th5_b34",
        "lessonNum": 34,
        "testNum": 2,
        "title": "Bài 34: Luyện tập chung Chủ đề 6 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 6",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Viết phân số $\\frac{4}{5}$ dưới dạng tỉ số phần trăm:", ["40%", "80%", "75%", "85%"], 1, "$\\frac{4}{5} = \\frac{80}{100} = 80\\%$."),
            make_mc(2, "Tìm tỉ số phần trăm của 15 và 60:", ["20%", "25%", "30%", "35%"], 1, "$15 : 60 = 0,25 = 25\\%$."),
            make_mc(3, "Tìm $12\\%$ của 450 lít:", ["45 lít", "50 lít", "54 lít", "60 lít"], 2, "$450 \\times 12 : 100 = 54$ lít."),
            make_mc(4, "Một trường có 500 học sinh, có 375 học sinh xếp loại xuất sắc. Tỉ số phần trăm học sinh xuất sắc là:", ["70%", "75%", "80%", "85%"], 1, "$375 : 500 = 0,75 = 75\\%$."),
            make_mc(5, "Biết $40\\%$ của $A$ là 160. Giá trị của $A$ là:", ["400", "300", "200", "500"], 0, "$A = 160 : 40 \\times 100 = 400$."),
            make_mc(6, "Một món hàng giá $250\\,000$ đồng, giảm giá $20\\%$. Giá bán sau khi giảm là:", ["200 000 đồng", "220 000 đồng", "180 000 đồng", "230 000 đồng"], 0, "$250\\,000 \\times (100\\% - 20\\%) : 100 = 200\\,000$ đồng.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\na) $15\\% \\times 4 + 20\\%$\nb) $85\\% - 12\\% \\times 3$", "a) $15\\% \\times 4 + 20\\% = 60\\% + 20\\% = 80\\%$\nb) $85\\% - 36\\% = 49\\%$", "a) 80%; b) 49%", 4, 1.0),
            make_essay(2, "Tính:\na) $35\\%$ của $400\\text{ kg}$\nb) Tỉ số phần trăm của 3,5 và 14", "a) $400 \\times 35 : 100 = 140\\text{ (kg)}$\nb) $3,5 : 14 = 0,25 = 25\\%$", "a) 140 kg; b) 25%", 4, 1.0),
            make_essay(3, "Tìm $y$, biết:\n$y : 15\\% = 240$", "Ta có:\n$y = 240 \\times 15\\% = 240 \\times 0,15 = 36$.\nĐáp số: $y = 36$.", "y = 36", 4, 1.0),
            make_essay(4, "Một cửa hàng nhập về 500 bao xi măng. Tuần thứ nhất bán được $35\\%$ số bao, tuần thứ hai bán được $40\\%$ số bao.\na) Cả hai tuần cửa hàng bán được bao nhiêu bao xi măng?\nb) Cửa hàng còn lại bao nhiêu bao xi măng?", "Bài giải:\na) Tỉ số phần trăm xi măng bán trong hai tuần là:\n$35\\% + 40\\% = 75\\%$\nSố bao xi măng bán được trong hai tuần là:\n$500 \\times 75 : 100 = 375\\text{ (bao)}$\nb) Số bao xi măng cửa hàng còn lại là:\n$500 - 375 = 125\\text{ (bao)}$\nĐáp số:\na) 375 bao;\nb) 125 bao.", "a) 375 bao; b) 125 bao", 5, 1.5),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chiều dài $40\\text{ m}$, chiều rộng bằng $75\\%$ chiều dài.\na) Tính diện tích mảnh vườn hình chữ nhật đó.\nb) Người ta dùng $30\\%$ diện tích vườn để trồng hoa. Tính diện tích phần đất trồng hoa.", "Bài giải:\na) Chiều rộng của mảnh vườn là:\n$40 \\times 75 : 100 = 30\\text{ (m)}$\nDiện tích mảnh vườn là:\n$40 \\times 30 = 1200\\text{ (m}^2)$\nb) Diện tích phần đất trồng hoa là:\n$1200 \\times 30 : 100 = 360\\text{ (m}^2)$\nĐáp số:\na) $1200\\text{ m}^2$;\nb) $360\\text{ m}^2$.", "a) 1200 m²; b) 360 m²", 5, 1.5),
            make_essay(6, "Bác Ba gửi ngân hàng $120\\,000\\,000$ đồng với lãi suất $6\\%$ một năm. Sau 1 năm bác rút hết tiền và dùng $20\\%$ tổng số tiền đó để mua sắm đồ gia dụng. Hỏi bác Ba còn lại bao nhiêu tiền?", "Bài giải:\nSố tiền lãi bác Ba nhận được sau 1 năm là:\n$120\\,000\\,000 \\times 6 : 100 = 7\\,200\\,000\\text{ (đồng)}$\nTổng số tiền cả gốc và lãi sau 1 năm là:\n$120\\,000\\,000 + 7\\,200\\,000 = 127\\,200\\,000\\text{ (đồng)}$\nSố tiền bác Ba dùng để mua đồ gia dụng là:\n$127\\,200\\,000 \\times 20 : 100 = 25\\,440\\,000\\text{ (đồng)}$\nSố tiền bác Ba còn lại là:\n$127\\,200\\,000 - 25\\,440\\,000 = 101\\,760\\,000\\text{ (đồng)}$\nĐáp số: $101\\,760\\,000\\text{ đồng}$.", "101 760 000 đồng", 5, 1.0)
        ]
    }

    # --- Bài 34 - Đề 3 ---
    exams["th5_b34_test3"] = {
        "id": "th5_b34_test3",
        "lessonId": "th5_b34",
        "lessonNum": 34,
        "testNum": 3,
        "title": "Bài 34: Luyện tập chung Chủ đề 6 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 6",
        "chapter": "Chủ đề 6: Tỉ số phần trăm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Viết phân số $\\frac{13}{20}$ dưới dạng tỉ số phần trăm:", ["65%", "60%", "70%", "55%"], 0, "$\\frac{13}{20} = \\frac{65}{100} = 65\\%$."),
            make_mc(2, "Số học sinh nữ của một lớp là 22 bạn trên tổng số 40 bạn. Tỉ số phần trăm số học sinh nữ là:", ["50%", "55%", "60%", "45%"], 1, "$22 : 40 = 0,55 = 55\\%$."),
            make_mc(3, "Tìm $18\\%$ của $500\\text{ m}$:", ["80 m", "90 m", "100 m", "85 m"], 1, "$500 \\times 18 : 100 = 90\\text{ m}$."),
            make_mc(4, "Biết $15\\%$ của số $x$ là 45. Số $x$ là:", ["300", "250", "200", "350"], 0, "$x = 45 : 15 \\times 100 = 300$."),
            make_mc(5, "Một cái nồi áp suất giá $800\\,000$ đồng, nhân dịp sinh nhật được giảm giá $25\\%$. Giá bán mới là:", ["600 000 đồng", "650 000 đồng", "700 000 đồng", "550 000 đồng"], 0, "$800\\,000 \\times (100\\% - 25\\%) : 100 = 600\\,000$ đồng."),
            make_mc(6, "Một tấm gỗ dài $2,5\\text{ m}$, người ta cắt bớt đi $20\\%$. Chiều dài phần cắt bớt là:", ["0,5 m", "0,25 m", "0,4 m", "0,6 m"], 0, "$2,5 \\times 20 : 100 = 0,5\\text{ m}$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị các phép tính sau:\na) $36\\% + 18,5\\% - 14,2\\%$\nb) $24\\% : 4 \\times 5$", "a) $36\\% + 18,5\\% - 14,2\\% = 54,5\\% - 14,2\\% = 40,3\\%$\nb) $24\\% : 4 \\times 5 = 6\\% \\times 5 = 30\\%$", "a) 40,3%; b) 30%", 4, 1.0),
            make_essay(2, "Tìm:\na) $45\\%$ của $600\\text{ kg}$\nb) Tỉ số phần trăm của 24 và 80", "a) $600 \\times 45 : 100 = 270\\text{ (kg)}$\nb) $24 : 80 = 0,3 = 30\\%$", "a) 270 kg; b) 30%", 4, 1.0),
            make_essay(3, "Tìm $x$ biết:\n$x - 30\\% = 45\\%$", "Ta có:\n$x = 45\\% + 30\\% = 75\\%$ (hay $x = 0,75$).\nĐáp số: $x = 75\\%$.", "x = 75%", 4, 1.0),
            make_essay(4, "Một nông trường có 1500 cây ăn quả, trong đó có 525 cây nhãn, 450 cây xoài, còn lại là cây vải.\na) Tìm tỉ số phần trăm của số cây nhãn so với tổng số cây.\nb) Tính số cây vải của nông trường.", "Bài giải:\na) Tỉ số phần trăm số cây nhãn là:\n$525 : 1500 = 0,35 = 35\\%$\nb) Số cây vải của nông trường là:\n$1500 - (525 + 450) = 525\\text{ (cây)}$\nĐáp số: a) $35\\%$; b) 525 cây.", "a) 35%; b) 525 cây", 5, 1.5),
            make_essay(5, "Một thửa ruộng hình thang có đáy lớn $40\\text{ m}$, đáy bé $25\\text{ m}$, chiều cao $20\\text{ m}$.\na) Tính diện tích thửa ruộng đó.\nb) Người ta dành $40\\%$ diện tích để trồng dưa chuột, diện tích còn lại trồng cà chua. Tính diện tích trồng cà chua.", "Bài giải:\na) Diện tích thửa ruộng hình thang là:\n$(40 + 25) \\times 20 : 2 = 650\\text{ (m}^2)$\nb) Tỉ số phần trăm diện tích trồng cà chua là:\n$100\\% - 40\\% = 60\\%$\nDiện tích trồng cà chua là:\n$650 \\times 60 : 100 = 390\\text{ (m}^2)$\nĐáp số:\na) $650\\text{ m}^2$;\nb) $390\\text{ m}^2$.", "a) 650 m²; b) 390 m²", 5, 1.5),
            make_essay(6, "Một người bán một món hàng với giá $480\\,000$ đồng, tính ra người đó được lãi $20\\%$ theo giá bán. Hỏi người đó được lãi bao nhiêu phần trăm theo giá vốn?", "Bài giải:\nSố tiền lãi người đó nhận được là:\n$480\\,000 \\times 20 : 100 = 96\\,000\\text{ (đồng)}$\nGiá vốn của món hàng là:\n$480\\,000 - 96\\,000 = 384\\,000\\text{ (đồng)}$\nTỉ số phần trăm tiền lãi so với giá vốn là:\n$96\\,000 : 384\\,000 = 0,25 = 25\\%$\nĐáp số: $25\\%$.", "25%", 5, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 6: {len(ex)} (Kỳ vọng: 15 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
