# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 7: THỂ TÍCH. ĐƠN VỊ ĐO THỂ TÍCH (BÀI 35 ĐẾN BÀI 37) - TOÁN 5 KNTT
Gồm 3 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 35: Khái niệm về thể tích. Xăng-ti-mét khối (th5_b35_test1, th5_b35_test2, th5_b35_test3)
- Bài 36: Đề-xi-mét khối. Mét khối (th5_b36_test1, th5_b36_test2, th5_b36_test3)
- Bài 37: Luyện tập chung Chủ đề 7 (th5_b37_test1, th5_b37_test2, th5_b37_test3)
Tổng cộng: 9 đề kiểm tra chất lượng cao, độc lập 100%.
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
    # BÀI 35: KHÁI NIỆM VỀ THỂ TÍCH. XĂNG-TI-MÉT KHỐI
    # =========================================================================

    # --- Bài 35 - Đề 1 ---
    exams["th5_b35_test1"] = {
        "id": "th5_b35_test1",
        "lessonId": "th5_b35",
        "lessonNum": 35,
        "testNum": 1,
        "title": "Bài 35: Khái niệm về thể tích. Xăng-ti-mét khối - Đề số 1",
        "topic": "Khái niệm về thể tích. Xăng-ti-mét khối",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Xăng-ti-mét khối là thể tích của hình lập phương có cạnh dài:", ["1 mm", "1 cm", "1 dm", "1 m"], 1, "Định nghĩa: Xăng-ti-mét khối là thể tích hình lập phương có cạnh 1 cm."),
            make_mc(2, "Xăng-ti-mét khối được viết tắt là:", ["$\\text{cm}$", "$\\text{cm}^2$", "$\\text{cm}^3$", "$\\text{m}^3$"], 2, "Kí hiệu xăng-ti-mét khối là $\\text{cm}^3$."),
            make_mc(3, "Số 'Một trăm hai mươi lăm xăng-ti-mét khối' được viết là:", ["$125\\text{ cm}$", "$125\\text{ cm}^2$", "$125\\text{ cm}^3$", "$1025\\text{ cm}^3$"], 2, "Viết là $125\\text{ cm}^3$."),
            make_mc(4, "Một hình hộp chữ nhật được ghép bởi 24 khối lập phương nhỏ cạnh $1\\text{ cm}$. Thể tích hình hộp đó là:", ["$24\\text{ cm}$", "$24\\text{ cm}^2$", "$24\\text{ cm}^3$", "$12\\text{ cm}^3$"], 2, "Mỗi khối nhỏ có thể tích $1\\text{ cm}^3$, nên 24 khối có thể tích là $24\\text{ cm}^3$."),
            make_mc(5, "Tính: $35\\text{ cm}^3 + 48\\text{ cm}^3 = \\dots$", ["$73\\text{ cm}^3$", "$83\\text{ cm}^3$", "$83\\text{ cm}^2$", "$85\\text{ cm}^3$"], 1, "$35 + 48 = 83\\text{ cm}^3$."),
            make_mc(6, "Hình A gồm 18 hình lập phương $1\\text{ cm}^3$, hình B gồm 21 hình lập phương $1\\text{ cm}^3$. Khẳng định nào sau đây đúng?", ["Thể tích hình A lớn hơn hình B", "Thể tích hình A bé hơn hình B", "Thể tích hai hình bằng nhau", "Không so sánh được"], 1, "Vì $18\\text{ cm}^3 < 21\\text{ cm}^3$ nên thể tích hình A bé hơn hình B.")
        ],
        "part2": [
            make_essay(1, "Viết và đọc các số đo thể tích sau:\na) $450\\text{ cm}^3$\nb) Tám mươi sáu phẩy năm xăng-ti-mét khối", "a) $450\\text{ cm}^3$: Bốn trăm năm mươi xăng-ti-mét khối.\nb) $86,5\\text{ cm}^3$.", "a) Bốn trăm năm mươi xăng-ti-mét khối; b) 86,5 cm³", 4, 1.0),
            make_essay(2, "Tính giá trị các phép tính sau:\na) $124\\text{ cm}^3 + 89\\text{ cm}^3$\nb) $250\\text{ cm}^3 - 75\\text{ cm}^3$", "a) $124\\text{ cm}^3 + 89\\text{ cm}^3 = 213\\text{ cm}^3$\nb) $250\\text{ cm}^3 - 75\\text{ cm}^3 = 175\\text{ cm}^3$", "a) 213 cm³; b) 175 cm³", 4, 1.0),
            make_essay(3, "Thực hiện phép tính:\na) $36\\text{ cm}^3 \\times 4$\nb) $144\\text{ cm}^3 : 6$", "a) $36\\text{ cm}^3 \\times 4 = 144\\text{ cm}^3$\nb) $144\\text{ cm}^3 : 6 = 24\\text{ cm}^3$", "a) 144 cm³; b) 24 cm³", 4, 1.0),
            make_essay(4, "Một khối gỗ hình lập phương được tạo thành từ 64 khối lập phương nhỏ cạnh $1\\text{ cm}$. Hỏi thể tích của khối gỗ đó là bao nhiêu xăng-ti-mét khối?", "Bài giải:\nThể tích của một khối lập phương nhỏ cạnh $1\\text{ cm}$ là:\n$1 \\times 1 \\times 1 = 1\\text{ (cm}^3)$\nThể tích của khối gỗ hình lập phương đó là:\n$1 \\times 64 = 64\\text{ (cm}^3)$\nĐáp số: $64\\text{ cm}^3$.", "64 cm³", 5, 1.5),
            make_essay(5, "Người ta xếp các khối lập phương nhỏ cạnh $1\\text{ cm}$ thành một hình hộp chữ nhật có lớp đáy gồm 4 hàng, mỗi hàng có 5 khối nhỏ và xếp được 3 lớp như vậy.\na) Tính tổng số khối lập phương nhỏ dùng để xếp thành hình hộp chữ nhật đó.\nb) Tính thể tích của hình hộp chữ nhật được tạo thành.", "Bài giải:\na) Số khối lập phương nhỏ ở mỗi lớp là:\n$5 \\times 4 = 20\\text{ (khối)}$\nTổng số khối lập phương nhỏ dùng để xếp là:\n$20 \\times 3 = 60\\text{ (khối)}$\nb) Thể tích của hình hộp chữ nhật đó là:\n$1 \\times 60 = 60\\text{ (cm}^3)$\nĐáp số:\na) 60 khối;\nb) $60\\text{ cm}^3$.", "a) 60 khối; b) 60 cm³", 5, 1.5),
            make_essay(6, "Một bình đo thể tích đang chứa $150\\text{ cm}^3$ nước. Người ta thả vào bình một viên sỏi chìm hoàn toàn trong nước thì thấy mực nước dâng lên đến vạch $185\\text{ cm}^3$. Tính thể tích của viên sỏi đó.", "Bài giải:\nThể tích của viên sỏi bằng thể tích nước dâng lên:\n$185 - 150 = 35\\text{ (cm}^3)$\nĐáp số: $35\\text{ cm}^3$.", "35 cm³", 5, 1.0)
        ]
    }

    # --- Bài 35 - Đề 2 ---
    exams["th5_b35_test2"] = {
        "id": "th5_b35_test2",
        "lessonId": "th5_b35",
        "lessonNum": 35,
        "testNum": 2,
        "title": "Bài 35: Khái niệm về thể tích. Xăng-ti-mét khối - Đề số 2",
        "topic": "Khái niệm về thể tích. Xăng-ti-mét khối",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số đo $308\\text{ cm}^3$ đọc là:", ["Ba trăm linh tám xăng-ti-mét", "Ba trăm linh tám xăng-ti-mét vuông", "Ba trăm linh tám xăng-ti-mét khối", "Ba không tám xăng-ti-mét khối"], 2, "Đọc là: Ba trăm linh tám xăng-ti-mét khối."),
            make_mc(2, "Xếp 12 khối lập phương $1\\text{ cm}^3$ thành một hàng ngang. Thể tích của hàng ngang đó là:", ["$12\\text{ cm}$", "$12\\text{ cm}^2$", "$12\\text{ cm}^3$", "$144\\text{ cm}^3$"], 2, "Thể tích bằng $12\\text{ cm}^3$."),
            make_mc(3, "Tính: $150\\text{ cm}^3 - 65\\text{ cm}^3 = \\dots$", ["$85\\text{ cm}^3$", "$75\\text{ cm}^3$", "$95\\text{ cm}^3$", "$80\\text{ cm}^3$"], 0, "$150 - 65 = 85\\text{ cm}^3$."),
            make_mc(4, "Một hình có thể tích $40\\text{ cm}^3$, hình kia có thể tích $0,4\\text{ dm}^3$ ($400\\text{ cm}^3$). Khẳng định nào đúng?", ["Hai hình bằng nhau", "Hình thứ hai lớn hơn hình thứ nhất", "Hình thứ nhất lớn hơn", "Không so sánh được"], 1, "Vì $400\\text{ cm}^3 > 40\\text{ cm}^3$."),
            make_mc(5, "Tính: $24\\text{ cm}^3 \\times 5 = \\dots$", ["$100\\text{ cm}^3$", "$120\\text{ cm}^3$", "$110\\text{ cm}^3$", "$125\\text{ cm}^3$"], 1, "$24 \\times 5 = 120\\text{ cm}^3$."),
            make_mc(6, "Người ta chia một khối gỗ thể tích $96\\text{ cm}^3$ thành 4 phần bằng nhau. Thể tích mỗi phần là:", ["$24\\text{ cm}^3$", "$26\\text{ cm}^3$", "$22\\text{ cm}^3$", "$28\\text{ cm}^3$"], 0, "$96 : 4 = 24\\text{ cm}^3$.")
        ],
        "part2": [
            make_essay(1, "Điền dấu ($<, >, =$) thích hợp vào chỗ chấm:\na) $250\\text{ cm}^3 + 150\\text{ cm}^3 \\dots 410\\text{ cm}^3$\nb) $35\\text{ cm}^3 \\times 4 \\dots 140\\text{ cm}^3$", "a) $250 + 150 = 400 < 410$, điền $<$\nb) $35 \\times 4 = 140 = 140$, điền $=$", "a) <; b) =", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $85\\text{ cm}^3 + 45\\text{ cm}^3 \\times 2$\nb) $(210\\text{ cm}^3 - 60\\text{ cm}^3) : 3$", "a) $85 + 90 = 175\\text{ cm}^3$\nb) $150 : 3 = 50\\text{ cm}^3$", "a) 175 cm³; b) 50 cm³", 4, 1.0),
            make_essay(3, "Tìm $x$, biết:\n$x - 45\\text{ cm}^3 = 80\\text{ cm}^3$", "Ta có:\n$x = 80\\text{ cm}^3 + 45\\text{ cm}^3$\n$x = 125\\text{ cm}^3$.\nĐáp số: $x = 125\\text{ cm}^3$.", "x = 125 cm³", 4, 1.0),
            make_essay(4, "Một hộp quà dạng hình chữ nhật được xếp kín bởi 48 khối lập phương nhỏ cạnh $1\\text{ cm}$. Người ta lấy bớt ra $25\\%$ số khối lập phương nhỏ đó. Hỏi trong hộp quà còn lại bao nhiêu xăng-ti-mét khối?", "Bài giải:\nThể tích ban đầu của hộp quà là:\n$1 \\times 48 = 48\\text{ (cm}^3)$\nSố khối lập phương nhỏ lấy ra là:\n$48 \\times 25 : 100 = 12\\text{ (khối)}$\nSố khối lập phương còn lại trong hộp là:\n$48 - 12 = 36\\text{ (khối)}$\nThể tích phần còn lại trong hộp là:\n$1 \\times 36 = 36\\text{ (cm}^3)$\nĐáp số: $36\\text{ cm}^3$.", "36 cm³", 5, 1.5),
            make_essay(5, "Một bình thủy tinh có dung tích $500\\text{ cm}^3$, đang chứa $320\\text{ cm}^3$ nước. Người ta thả vào bình 3 hòn bi sắt giống nhau chìm ngập hoàn toàn thì thấy nước dâng lên đầy bình (chưa tràn ra ngoài).\na) Tính tổng thể tích của 3 hòn bi sắt đó.\nb) Tính thể tích của mỗi hòn bi sắt.", "Bài giải:\na) Tổng thể tích của 3 hòn bi sắt là:\n$500 - 320 = 180\\text{ (cm}^3)$\nb) Thể tích của mỗi hòn bi sắt là:\n$180 : 3 = 60\\text{ (cm}^3)$\nĐáp số:\na) $180\\text{ cm}^3$;\nb) $60\\text{ cm}^3$.", "a) 180 cm³; b) 60 cm³", 5, 1.5),
            make_essay(6, "Người ta dùng các khối lập phương nhỏ cạnh $1\\text{ cm}$ để ghép thành một khối lập phương lớn có cạnh dài $3\\text{ cm}$. Hỏi cần tất cả bao nhiêu khối lập phương nhỏ?", "Bài giải:\nThể tích của khối lập phương lớn cạnh $3\\text{ cm}$ là:\n$3 \\times 3 \\times 3 = 27\\text{ (cm}^3)$\nThể tích của mỗi khối lập phương nhỏ là:\n$1 \\times 1 \\times 1 = 1\\text{ (cm}^3)$\nSố khối lập phương nhỏ cần dùng là:\n$27 : 1 = 27\\text{ (khối)}$\nĐáp số: 27 khối.", "27 khối", 5, 1.0)
        ]
    }

    # --- Bài 35 - Đề 3 ---
    exams["th5_b35_test3"] = {
        "id": "th5_b35_test3",
        "lessonId": "th5_b35",
        "lessonNum": 35,
        "testNum": 3,
        "title": "Bài 35: Khái niệm về thể tích. Xăng-ti-mét khối - Đề số 3",
        "topic": "Khái niệm về thể tích. Xăng-ti-mét khối",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số 'Bảy mươi hai phẩy bốn xăng-ti-mét khối' viết là:", ["$72,4\\text{ cm}$", "$72,4\\text{ cm}^2$", "$72,4\\text{ cm}^3$", "$7,24\\text{ cm}^3$"], 2, "Viết là $72,4\\text{ cm}^3$."),
            make_mc(2, "Tính: $18\\text{ cm}^3 \\times 3 + 26\\text{ cm}^3 = \\dots$", ["$70\\text{ cm}^3$", "$80\\text{ cm}^3$", "$75\\text{ cm}^3$", "$85\\text{ cm}^3$"], 1, "$54 + 26 = 80\\text{ cm}^3$."),
            make_mc(3, "Một khối rubik được ghép từ 27 khối lập phương nhỏ cạnh $1\\text{ cm}$. Thể tích khối rubik đó là:", ["$9\\text{ cm}^3$", "$18\\text{ cm}^3$", "$27\\text{ cm}^3$", "$54\\text{ cm}^3$"], 2, "Thể tích bằng $27\\text{ cm}^3$."),
            make_mc(4, "Một bình đong chứa $200\\text{ cm}^3$ nước, đổ thêm vào bình $75\\text{ cm}^3$ nước nữa. Lượng nước có trong bình lúc này là:", ["$270\\text{ cm}^3$", "$275\\text{ cm}^3$", "$285\\text{ cm}^3$", "$250\\text{ cm}^3$"], 1, "$200 + 75 = 275\\text{ cm}^3$."),
            make_mc(5, "Tính: $140\\text{ cm}^3 : 5 = \\dots$", ["$26\\text{ cm}^3$", "$28\\text{ cm}^3$", "$30\\text{ cm}^3$", "$25\\text{ cm}^3$"], 1, "$140 : 5 = 28\\text{ cm}^3$."),
            make_mc(6, "Khối kim loại A có thể tích $45\\text{ cm}^3$, khối kim loại B có thể tích gấp đôi khối A. Thể tích khối B là:", ["$90\\text{ cm}^3$", "$80\\text{ cm}^3$", "$100\\text{ cm}^3$", "$70\\text{ cm}^3$"], 0, "$45 \\times 2 = 90\\text{ cm}^3$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\na) $25,5\\text{ cm}^3 + 14,8\\text{ cm}^3$\nb) $90\\text{ cm}^3 - 34,6\\text{ cm}^3$", "a) $25,5 + 14,8 = 40,3\\text{ cm}^3$\nb) $90 - 34,6 = 55,4\\text{ cm}^3$", "a) 40,3 cm³; b) 55,4 cm³", 4, 1.0),
            make_essay(2, "Thực hiện phép tính:\na) $15,4\\text{ cm}^3 \\times 4$\nb) $168\\text{ cm}^3 : 8$", "a) $15,4 \\times 4 = 61,6\\text{ cm}^3$\nb) $168 : 8 = 21\\text{ cm}^3$", "a) 61,6 cm³; b) 21 cm³", 4, 1.0),
            make_essay(3, "Một cốc đo hình trụ có chứa $120\\text{ cm}^3$ nước. Người ta thả 2 viên bi giống nhau vào cốc thì mực nước dâng lên $170\\text{ cm}^3$. Tính thể tích của mỗi viên bi.", "Bài giải:\nThể tích của 2 viên bi là:\n$170 - 120 = 50\\text{ (cm}^3)$\nThể tích của mỗi viên bi là:\n$50 : 2 = 25\\text{ (cm}^3)$\nĐáp số: $25\\text{ cm}^3$.", "25 cm³", 4, 1.0),
            make_essay(4, "Một khối gỗ hình hộp chữ nhật được tạo bởi 36 khối lập phương nhỏ cạnh $1\\text{ cm}$. Người ta sơn các mặt ngoài của khối gỗ. Biết có 8 khối nhỏ ở bên trong không được sơn mặt nào.\na) Tính thể tích khối gỗ hình hộp chữ nhật đó.\nb) Tính tổng thể tích các khối nhỏ được quét sơn ít nhất một mặt.", "Bài giải:\na) Thể tích khối gỗ hình hộp chữ nhật là:\n$1 \\times 36 = 36\\text{ (cm}^3)$\nb) Số khối lập phương nhỏ được sơn ít nhất một mặt là:\n$36 - 8 = 28\\text{ (khối)}$\nTổng thể tích các khối nhỏ được sơn là:\n$1 \\times 28 = 28\\text{ (cm}^3)$\nĐáp số:\na) $36\\text{ cm}^3$;\nb) $28\\text{ cm}^3$.", "a) 36 cm³; b) 28 cm³", 5, 1.5),
            make_essay(5, "Người ta xếp các khối lập phương nhỏ cạnh $1\\text{ cm}$ thành một hình hộp chữ nhật có chiều dài $5\\text{ cm}$, chiều rộng $4\\text{ cm}$ và chiều cao $3\\text{ cm}$.\na) Cần bao nhiêu khối lập phương nhỏ để xếp được hình hộp chữ nhật đó?\nb) Nếu lấy bớt đi một nửa số khối nhỏ thì thể tích còn lại là bao nhiêu xăng-ti-mét khối?", "Bài giải:\na) Thể tích hình hộp chữ nhật là:\n$5 \\times 4 \\times 3 = 60\\text{ (cm}^3)$\nSố khối lập phương nhỏ cần dùng là:\n$60 : 1 = 60\\text{ (khối)}$\nb) Thể tích còn lại sau khi bớt một nửa là:\n$60 : 2 = 30\\text{ (cm}^3)$\nĐáp số:\na) 60 khối;\nb) $30\\text{ cm}^3$.", "a) 60 khối; b) 30 cm³", 5, 1.5),
            make_essay(6, "Cho hai khối kim loại: Khối thứ nhất có thể tích $75\\text{ cm}^3$. Khối thứ hai có thể tích bằng $60\\%$ thể tích khối thứ nhất. Tính tổng thể tích của cả hai khối kim loại đó.", "Bài giải:\nThể tích của khối kim loại thứ hai là:\n$75 \\times 60 : 100 = 45\\text{ (cm}^3)$\nTổng thể tích của cả hai khối kim loại là:\n$75 + 45 = 120\\text{ (cm}^3)$\nĐáp số: $120\\text{ cm}^3$.", "120 cm³", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 36: ĐỀ-XI-MÉT KHỐI. MÉT KHỐI
    # =========================================================================

    # --- Bài 36 - Đề 1 ---
    exams["th5_b36_test1"] = {
        "id": "th5_b36_test1",
        "lessonId": "th5_b36",
        "lessonNum": 36,
        "testNum": 1,
        "title": "Bài 36: Đề-xi-mét khối. Mét khối - Đề số 1",
        "topic": "Đề-xi-mét khối. Mét khối",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một đề-xi-mét khối bằng bao nhiêu xăng-ti-mét khối?", ["10", "100", "1000", "10 000"], 2, "$1\\text{ dm}^3 = 1000\\text{ cm}^3$."),
            make_mc(2, "Một mét khối bằng bao nhiêu đề-xi-mét khối?", ["100", "1000", "10 000", "1 000 000"], 1, "$1\\text{ m}^3 = 1000\\text{ dm}^3$."),
            make_mc(3, "Điền số thích hợp: $2,5\\text{ m}^3 = \\dots\\text{ dm}^3$:", ["25", "250", "2500", "25 000"], 2, "$2,5 \\times 1000 = 2500\\text{ dm}^3$."),
            make_mc(4, "Một đề-xi-mét khối tương đương với:", ["1 lít", "10 lít", "100 lít", "0,1 lít"], 0, "$1\\text{ dm}^3 = 1\\text{ lít}$."),
            make_mc(5, "Đổi: $4500\\text{ cm}^3 = \\dots\\text{ dm}^3$:", ["45", "4,5", "0,45", "450"], 1, "$4500 : 1000 = 4,5\\text{ dm}^3$."),
            make_mc(6, "So sánh: $0,8\\text{ m}^3 \\dots 800\\text{ dm}^3$. Dấu thích hợp là:", ["$<$", "$>$", "$=$", "Không so sánh được"], 2, "$0,8\\text{ m}^3 = 800\\text{ dm}^3$ nên điền dấu $=$ .")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $3\\text{ m}^3 = \\dots\\text{ dm}^3$\nb) $5000\\text{ dm}^3 = \\dots\\text{ m}^3$", "a) $3\\text{ m}^3 = 3000\\text{ dm}^3$\nb) $5000\\text{ dm}^3 = 5\\text{ m}^3$", "a) 3000; b) 5", 4, 1.0),
            make_essay(2, "Viết các số đo sau dưới dạng số thập phân có đơn vị đo là đề-xi-mét khối:\na) $4\\text{ dm}^3\\ 350\\text{ cm}^3$\nb) $1800\\text{ cm}^3$", "a) $4\\text{ dm}^3\\ 350\\text{ cm}^3 = 4,35\\text{ dm}^3$\nb) $1800\\text{ cm}^3 = 1,8\\text{ dm}^3$", "a) 4,35 dm³; b) 1,8 dm³", 4, 1.0),
            make_essay(3, "Tính:\na) $2,4\\text{ m}^3 + 1,8\\text{ m}^3$\nb) $450\\text{ dm}^3 \\times 4$", "a) $2,4 + 1,8 = 4,2\\text{ m}^3$\nb) $450 \\times 4 = 1800\\text{ dm}^3 = 1,8\\text{ m}^3$", "a) 4,2 m³; b) 1800 dm³ (hay 1,8 m³)", 4, 1.0),
            make_essay(4, "Một bể nước chứa được $3,2\\text{ m}^3$ nước. Hiện tại trong bể đang có $1800\\text{ dm}^3$ nước. Hỏi cần đổ thêm bao nhiêu lít nước nữa thì đầy bể? (Biết $1\\text{ dm}^3 = 1\\text{ lít}$).", "Bài giải:\nĐổi: $3,2\\text{ m}^3 = 3200\\text{ dm}^3 = 3200\\text{ lít}$.\n$1800\\text{ dm}^3 = 1800\\text{ lít}$.\nSố lít nước cần đổ thêm để đầy bể là:\n$3200 - 1800 = 1400\\text{ (lít)}$\nĐáp số: 1400 lít.", "1400 lít", 5, 1.5),
            make_essay(5, "Một cái thùng tôn hình hộp chữ nhật có thể tích $1,2\\text{ m}^3$. Người ta đổ vào thùng 800 lít nước.\na) Lượng nước đổ vào chiếm bao nhiêu phần trăm thể tích của thùng?\nb) Thể tích phần còn trống của thùng là bao nhiêu đề-xi-mét khối?", "Bài giải:\nĐổi: $1,2\\text{ m}^3 = 1200\\text{ dm}^3 = 1200\\text{ lít}$.\na) Lượng nước đổ vào chiếm tỉ số phần trăm thể tích thùng là:\n$800 : 1200 = \\frac{800}{1200} = \\frac{2}{3} \\approx 66,67\\%$\n(hoặc $\\frac{2}{3}$ thể tích thùng).\nb) Thể tích phần còn trống của thùng là:\n$1200 - 800 = 400\\text{ (dm}^3)$\nĐáp số:\na) $66,67\\%$ (hay $\\frac{2}{3}$);\nb) $400\\text{ dm}^3$.", "a) 66,67%; b) 400 dm³", 5, 1.5),
            make_essay(6, "Một khối gỗ hình lập phương có cạnh $1\\text{ m}$. Người ta xẻ khối gỗ đó thành các khối lập phương nhỏ cạnh $1\\text{ dm}$. Sau đó xếp các khối nhỏ đó nối đuôi nhau thành một hàng thẳng dài. Hỏi hàng thẳng đó dài bao nhiêu mét?", "Bài giải:\nThể tích khối gỗ hình lập phương cạnh $1\\text{ m}$ là:\n$1\\text{ m}^3 = 1000\\text{ dm}^3$\nMỗi khối gỗ nhỏ cạnh $1\\text{ dm}$ có thể tích $1\\text{ dm}^3$, do đó có tất cả 1000 khối nhỏ.\nKhi xếp 1000 khối nhỏ cạnh $1\\text{ dm}$ nối tiếp nhau thành một hàng thẳng thì độ dài của hàng là:\n$1 \\times 1000 = 1000\\text{ (dm)}$\nĐổi: $1000\\text{ dm} = 100\\text{ m}$.\nĐáp số: 100 m.", "100 m", 5, 1.0)
        ]
    }

    # --- Bài 36 - Đề 2 ---
    exams["th5_b36_test2"] = {
        "id": "th5_b36_test2",
        "lessonId": "th5_b36",
        "lessonNum": 36,
        "testNum": 2,
        "title": "Bài 36: Đề-xi-mét khối. Mét khối - Đề số 2",
        "topic": "Đề-xi-mét khối. Mét khối",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một mét khối bằng bao nhiêu xăng-ti-mét khối?", ["1000", "10 000", "100 000", "1 000 000"], 3, "$1\\text{ m}^3 = 1000\\text{ dm}^3 = 1\\,000\\,000\\text{ cm}^3$."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm $0,05\\text{ m}^3 = \\dots\\text{ dm}^3$ là:", ["5", "50", "500", "0,5"], 1, "$0,05 \\times 1000 = 50\\text{ dm}^3$."),
            make_mc(3, "75 lít nước tương ứng với thể tích nào sau đây?", ["$75\\text{ cm}^3$", "$75\\text{ dm}^3$", "$0,75\\text{ dm}^3$", "$75\\text{ m}^3$"], 1, "Vì $1\\text{ lít} = 1\\text{ dm}^3$ nên 75 lít = $75\\text{ dm}^3$."),
            make_mc(4, "Đổi: $32\\,000\\text{ dm}^3 = \\dots\\text{ m}^3$:", ["320", "32", "3,2", "0,32"], 1, "$32\\,000 : 1000 = 32\\text{ m}^3$."),
            make_mc(5, "Tính: $1,5\\text{ m}^3 - 850\\text{ dm}^3 = \\dots$", ["$650\\text{ dm}^3$", "$750\\text{ dm}^3$", "$550\\text{ dm}^3$", "$65\\text{ dm}^3$"], 0, "$1500\\text{ dm}^3 - 850\\text{ dm}^3 = 650\\text{ dm}^3$."),
            make_mc(6, "So sánh: $2\\text{ m}^3\\ 5\\text{ dm}^3 \\dots 2,05\\text{ m}^3$. Dấu thích hợp là:", ["$>$", "$<$", "$=$", "Không so sánh được"], 1, "$2\\text{ m}^3\\ 5\\text{ dm}^3 = 2,005\\text{ m}^3 < 2,05\\text{ m}^3$, dấu $<$ .")
        ],
        "part2": [
            make_essay(1, "Điền số thích hợp vào chỗ chấm:\na) $4,8\\text{ dm}^3 = \\dots\\text{ cm}^3$\nb) $0,75\\text{ m}^3 = \\dots\\text{ dm}^3$", "a) $4,8 \\times 1000 = 4800\\text{ cm}^3$\nb) $0,75 \\times 1000 = 750\\text{ dm}^3$", "a) 4800; b) 750", 4, 1.0),
            make_essay(2, "Viết các số đo sau dưới dạng số đo có đơn vị là mét khối:\na) $3500\\text{ dm}^3$\nb) $6\\text{ m}^3\\ 45\\text{ dm}^3$", "a) $3500 : 1000 = 3,5\\text{ m}^3$\nb) $6 + 45/1000 = 6,045\\text{ m}^3$", "a) 3,5 m³; b) 6,045 m³", 4, 1.0),
            make_essay(3, "Thực hiện các phép tính:\na) $3,5\\text{ m}^3 \\times 3$\nb) $1800\\text{ dm}^3 : 5$", "a) $3,5 \\times 3 = 10,5\\text{ m}^3$\nb) $1800 : 5 = 360\\text{ dm}^3$", "a) 10,5 m³; b) 360 dm³", 4, 1.0),
            make_essay(4, "Một bể bơi mini có thể tích $4,5\\text{ m}^3$. Người ta bơm nước vào bể bằng một máy bơm có công suất 500 lít mỗi phút. Hỏi sau bao lâu thì máy bơm bơm đầy bể nước đó?", "Bài giải:\nĐổi: $4,5\\text{ m}^3 = 4500\\text{ dm}^3 = 4500\\text{ lít}$.\nThời gian để máy bơm bơm đầy bể là:\n$4500 : 500 = 9\\text{ (phút)}$\nĐáp số: 9 phút.", "9 phút", 5, 1.5),
            make_essay(5, "Một téc nước hình trụ chứa được tối đa $2\\text{ m}^3$ nước. Hiện tại trong téc đang có lượng nước bằng $70\\%$ dung tích của téc.\na) Tính số lít nước đang có trong téc.\nb) Người ta đã sử dụng hết 600 lít nước từ téc đó. Hỏi lượng nước còn lại trong téc là bao nhiêu mét khối?", "Bài giải:\nĐổi: $2\\text{ m}^3 = 2000\\text{ dm}^3 = 2000\\text{ lít}$.\na) Số lít nước đang có trong téc là:\n$2000 \\times 70 : 100 = 1400\\text{ (lít)}$\nb) Số lít nước còn lại sau khi dùng là:\n$1400 - 600 = 800\\text{ (lít)}$\nĐổi: $800\\text{ lít} = 800\\text{ dm}^3 = 0,8\\text{ m}^3$.\nĐáp số:\na) $1400\\text{ lít}$;\nb) $0,8\\text{ m}^3$.", "a) 1400 lít; b) 0,8 m³", 5, 1.5),
            make_essay(6, "Một khối bê tông dạng hình hộp chữ nhật có thể tích $3,6\\text{ m}^3$. Biết rằng cứ mỗi đề-xi-mét khối bê tông nặng $2,4\\text{ kg}$. Hỏi toàn bộ khối bê tông đó nặng bao nhiêu tấn?", "Bài giải:\nĐổi: $3,6\\text{ m}^3 = 3600\\text{ dm}^3$.\nKhối bê tông đó nặng số ki-lô-gam là:\n$3600 \\times 2,4 = 8640\\text{ (kg)}$\nĐổi: $8640\\text{ kg} = 8,64\\text{ tấn}$.\nĐáp số: 8,64 tấn.", "8,64 tấn", 5, 1.0)
        ]
    }

    # --- Bài 36 - Đề 3 ---
    exams["th5_b36_test3"] = {
        "id": "th5_b36_test3",
        "lessonId": "th5_b36",
        "lessonNum": 36,
        "testNum": 3,
        "title": "Bài 36: Đề-xi-mét khối. Mét khối - Đề số 3",
        "topic": "Đề-xi-mét khối. Mét khối",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm $1,25\\text{ m}^3 = \\dots\\text{ dm}^3$ là:", ["125", "1250", "12 500", "12,5"], 1, "$1,25 \\times 1000 = 1250\\text{ dm}^3$."),
            make_mc(2, "Số đo $6\\text{ m}^3\\ 8\\text{ dm}^3$ viết dưới dạng số thập phân có đơn vị mét khối là:", ["6,8", "6,08", "6,008", "6,800"], 2, "$6\\text{ m}^3\\ 8\\text{ dm}^3 = 6 + 8/1000 = 6,008\\text{ m}^3$."),
            make_mc(3, "Một can dầu chứa 20 lít dầu. Thể tích dầu trong can là:", ["$20\\text{ cm}^3$", "$20\\text{ dm}^3$", "$0,2\\text{ dm}^3$", "$20\\text{ m}^3$"], 1, "20 lít = $20\\text{ dm}^3$."),
            make_mc(4, "Tính: $350\\text{ dm}^3 + 650\\text{ dm}^3 = \\dots\\text{ m}^3$:", ["1", "10", "100", "0,1"], 0, "$350 + 650 = 1000\\text{ dm}^3 = 1\\text{ m}^3$."),
            make_mc(5, "Đổi: $750\\text{ cm}^3 = \\dots\\text{ dm}^3$:", ["7,5", "0,75", "0,075", "75"], 1, "$750 : 1000 = 0,75\\text{ dm}^3$."),
            make_mc(6, "Bể nước có dung tích $1,6\\text{ m}^3$, đang chứa 1200 lít nước. Thể tích phần còn trống là:", ["$400\\text{ dm}^3$", "$40\\text{ dm}^3$", "$4\\text{ m}^3$", "$0,04\\text{ m}^3$"], 0, "$1600 - 1200 = 400$ lít $= 400\\text{ dm}^3$.")
        ],
        "part2": [
            make_essay(1, "Điền dấu ($<, >, =$) thích hợp:\na) $3,05\\text{ m}^3 \\dots 3050\\text{ dm}^3$\nb) $4500\\text{ cm}^3 \\dots 4,5\\text{ dm}^3$", "a) $3,05\\text{ m}^3 = 3050\\text{ dm}^3$, điền $=$\nb) $4500\\text{ cm}^3 = 4,5\\text{ dm}^3$, điền $=$", "a) =; b) =", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $4,8\\text{ m}^3 - 1,9\\text{ m}^3$\nb) $250\\text{ dm}^3 \\times 6$", "a) $4,8 - 1,9 = 2,9\\text{ m}^3$\nb) $250 \\times 6 = 1500\\text{ dm}^3 = 1,5\\text{ m}^3$", "a) 2,9 m³; b) 1500 dm³ (1,5 m³)", 4, 1.0),
            make_essay(3, "Tìm $y$, biết:\n$y + 450\\text{ dm}^3 = 1,2\\text{ m}^3$", "Đổi: $1,2\\text{ m}^3 = 1200\\text{ dm}^3$.\nTa có: $y + 450\\text{ dm}^3 = 1200\\text{ dm}^3$\n$y = 1200 - 450 = 750\\text{ dm}^3$.\nĐáp số: $y = 750\\text{ dm}^3$ (hay $0,75\\text{ m}^3$).", "y = 750 dm³ (0,75 m³)", 4, 1.0),
            make_essay(4, "Một xe bồn chở nước sạch có dung tích $8\\text{ m}^3$. Xe chở nước đến phân phối cho 3 khu dân cư: Khu A nhận $2500\\text{ lít}$, Khu B nhận $3200\\text{ lít}$, số nước còn lại giao cho Khu C. Hỏi Khu C nhận được bao nhiêu mét khối nước?", "Bài giải:\nĐổi: $8\\text{ m}^3 = 8000\\text{ dm}^3 = 8000\\text{ lít}$.\nTổng lượng nước giao cho Khu A và Khu B là:\n$2500 + 3200 = 5700\\text{ (lít)}$\nLượng nước Khu C nhận được là:\n$8000 - 5700 = 2300\\text{ (lít)}$\nĐổi: $2300\\text{ lít} = 2300\\text{ dm}^3 = 2,3\\text{ m}^3$.\nĐáp số: $2,3\\text{ m}^3$.", "2,3 m³", 5, 1.5),
            make_essay(5, "Một cái hố dạng hình hộp chữ nhật có thể tích $6\\text{ m}^3$. Người ta đổ vào hố $4,5\\text{ m}^3$ cát.\na) Thể tích cát đã đổ chiếm bao nhiêu phần trăm thể tích của hố?\nb) Cần đổ thêm bao nhiêu đề-xi-mét khối cát nữa để đầy hố?", "Bài giải:\na) Tỉ số phần trăm thể tích cát đã đổ là:\n$4,5 : 6 = 0,75 = 75\\%$\nb) Thể tích cát cần đổ thêm để đầy hố là:\n$6 - 4,5 = 1,5\\text{ (m}^3)$\nĐổi: $1,5\\text{ m}^3 = 1500\\text{ dm}^3$.\nĐáp số:\na) $75\\%$;\nb) $1500\\text{ dm}^3$.", "a) 75%; b) 1500 dm³", 5, 1.5),
            make_essay(6, "Biết $1\\text{ dm}^3$ sắt nguyên chất nặng $7,8\\text{ kg}$. Một thanh sắt hình hộp chữ nhật có thể tích $0,05\\text{ m}^3$. Hỏi thanh sắt đó nặng bao nhiêu ki-lô-gam?", "Bài giải:\nĐổi: $0,05\\text{ m}^3 = 0,05 \\times 1000 = 50\\text{ dm}^3$.\nThanh sắt đó nặng số ki-lô-gam là:\n$50 \\times 7,8 = 390\\text{ (kg)}$\nĐáp số: 390 kg.", "390 kg", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 37: LUYỆN TẬP CHUNG CHỦ ĐỀ 7
    # =========================================================================

    # --- Bài 37 - Đề 1 ---
    exams["th5_b37_test1"] = {
        "id": "th5_b37_test1",
        "lessonId": "th5_b37",
        "lessonNum": 37,
        "testNum": 1,
        "title": "Bài 37: Luyện tập chung Chủ đề 7 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 7",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm $3,6\\text{ m}^3 = \\dots\\text{ dm}^3$ là:", ["36", "360", "3600", "36 000"], 2, "$3,6 \\times 1000 = 3600\\text{ dm}^3$."),
            make_mc(2, "Điền số: $450\\text{ dm}^3 = \\dots\\text{ m}^3$:", ["45", "4,5", "0,45", "0,045"], 2, "$450 : 1000 = 0,45\\text{ m}^3$."),
            make_mc(3, "Một bể nước có thể tích $2,4\\text{ m}^3$. Số lít nước bể đó chứa đầy là:", ["240 lít", "2400 lít", "24 000 lít", "24 lít"], 1, "$2,4\\text{ m}^3 = 2400\\text{ dm}^3 = 2400\\text{ lít}$."),
            make_mc(4, "So sánh: $5\\text{ dm}^3\\ 60\\text{ cm}^3 \\dots 5,06\\text{ dm}^3$. Dấu thích hợp là:", ["$>$", "$<$", "$=$", "Không so sánh được"], 2, "$5\\text{ dm}^3\\ 60\\text{ cm}^3 = 5,06\\text{ dm}^3$, dấu $=$ ."),
            make_mc(5, "Tính: $1,2\\text{ m}^3 + 800\\text{ dm}^3 = \\dots\\text{ m}^3$:", ["2", "1,8", "9,2", "20"], 0, "$1,2\\text{ m}^3 + 0,8\\text{ m}^3 = 2\\text{ m}^3$."),
            make_mc(6, "Một khối gỗ thể tích $40\\text{ dm}^3$, người ta cắt đi $30\\%$. Thể tích phần cắt đi là:", ["12 dm³", "10 dm³", "15 dm³", "8 dm³"], 0, "$40 \\times 30 : 100 = 12\\text{ dm}^3$.")
        ],
        "part2": [
            make_essay(1, "Viết các số đo sau dưới dạng số đo có đơn vị đề-xi-mét khối:\na) $2,75\\text{ m}^3$\nb) $4500\\text{ cm}^3$", "a) $2,75 \\times 1000 = 2750\\text{ dm}^3$\nb) $4500 : 1000 = 4,5\\text{ dm}^3$", "a) 2750 dm³; b) 4,5 dm³", 4, 1.0),
            make_essay(2, "Tính giá trị các biểu thức:\na) $3,4\\text{ m}^3 - 1800\\text{ dm}^3$\nb) $450\\text{ cm}^3 \\times 6$", "a) $3400\\text{ dm}^3 - 1800\\text{ dm}^3 = 1600\\text{ dm}^3 = 1,6\\text{ m}^3$\nb) $450 \\times 6 = 2700\\text{ cm}^3 = 2,7\\text{ dm}^3$", "a) 1,6 m³ (1600 dm³); b) 2700 cm³", 4, 1.0),
            make_essay(3, "Tìm $x$ biết:\n$x \\times 4 = 1,8\\text{ m}^3$", "Ta có:\n$x = 1,8 : 4 = 0,45\\text{ m}^3$ (hay $450\\text{ dm}^3$).\nĐáp số: $x = 0,45\\text{ m}^3$.", "x = 0,45 m³", 4, 1.0),
            make_essay(4, "Một bể nước có dung tích $5\\text{ m}^3$. Người ta mở một vòi nước chảy vào bể (bể ban đầu không có nước), mỗi phút chảy được 40 lít.\na) Hỏi sau 1 giờ 30 phút, lượng nước trong bể là bao nhiêu lít?\nb) Lượng nước đó chiếm bao nhiêu phần trăm thể tích của bể?", "Bài giải:\na) Đổi: $1\\text{ giờ } 30\\text{ phút} = 90\\text{ phút}$.\nLượng nước chảy vào bể sau 90 phút là:\n$40 \\times 90 = 3600\\text{ (lít)}$\nb) Đổi: $5\\text{ m}^3 = 5000\\text{ dm}^3 = 5000\\text{ lít}$.\nTỉ số phần trăm lượng nước chảy vào so với bể là:\n$3600 : 5000 = 0,72 = 72\\%$\nĐáp số:\na) $3600\\text{ lít}$;\nb) $72\\%$.", "a) 3600 lít; b) 72%", 5, 1.5),
            make_essay(5, "Một thùng chứa dạng hình hộp chữ nhật có thể tích $1,5\\text{ m}^3$. Người ta đổ dầu vào thùng sao cho lượng dầu chiếm $80\\%$ thể tích thùng.\na) Tính số lít dầu đã đổ vào thùng.\nb) Biết mỗi lít dầu cân nặng $0,8\\text{ kg}$. Tính khối lượng dầu có trong thùng.", "Bài giải:\nĐổi: $1,5\\text{ m}^3 = 1500\\text{ dm}^3 = 1500\\text{ lít}$.\na) Số lít dầu đổ vào thùng là:\n$1500 \\times 80 : 100 = 1200\\text{ (lít)}$\nb) Khối lượng dầu trong thùng là:\n$1200 \\times 0,8 = 960\\text{ (kg)}$\nĐáp số:\na) $1200\\text{ lít}$;\nb) $960\\text{ kg}$.", "a) 1200 lít; b) 960 kg", 5, 1.5),
            make_essay(6, "Thả một khối đá chìm vào một bể chứa nước đang có mực nước cao $40\\text{ cm}$. Đáy bể có diện tích $1,2\\text{ m}^2$. Sau khi thả hòn đá vào thì mực nước dâng lên thành $45\\text{ cm}$. Tính thể tích của hòn đá đó theo đơn vị đề-xi-mét khối.", "Bài giải:\nĐổi: $1,2\\text{ m}^2 = 120\\text{ dm}^2$.\nChiều cao nước dâng thêm là:\n$45 - 40 = 5\\text{ (cm)} = 0,5\\text{ (dm)}$\nThể tích hòn đá bằng thể tích nước dâng lên:\n$120 \\times 0,5 = 60\\text{ (dm}^3)$\nĐáp số: $60\\text{ dm}^3$.", "60 dm³", 5, 1.0)
        ]
    }

    # --- Bài 37 - Đề 2 ---
    exams["th5_b37_test2"] = {
        "id": "th5_b37_test2",
        "lessonId": "th5_b37",
        "lessonNum": 37,
        "testNum": 2,
        "title": "Bài 37: Luyện tập chung Chủ đề 7 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 7",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Điền số: $0,085\\text{ m}^3 = \\dots\\text{ dm}^3$:", ["8,5", "85", "850", "0,85"], 1, "$0,085 \\times 1000 = 85\\text{ dm}^3$."),
            make_mc(2, "Thể tích $2500\\text{ cm}^3$ bằng bao nhiêu đề-xi-mét khối?", ["2,5 dm³", "25 dm³", "250 dm³", "0,25 dm³"], 0, "$2500 : 1000 = 2,5\\text{ dm}^3$."),
            make_mc(3, "Một can dầu chứa 15 lít dầu, tức là can dầu chứa:", ["$15\\text{ cm}^3$", "$15\\text{ dm}^3$", "$0,15\\text{ m}^3$", "$15\\text{ m}^3$"], 1, "15 lít = $15\\text{ dm}^3$."),
            make_mc(4, "Tính: $3\\text{ m}^3 - 1450\\text{ dm}^3 = \\dots$", ["$1550\\text{ dm}^3$", "$1650\\text{ dm}^3$", "$1450\\text{ dm}^3$", "$2550\\text{ dm}^3$"], 0, "$3000 - 1450 = 1550\\text{ dm}^3$."),
            make_mc(5, "So sánh: $4\\text{ m}^3\\ 25\\text{ dm}^3 \\dots 4,25\\text{ m}^3$. Dấu thích hợp là:", ["$>$", "$<$", "$=$", "Không so sánh được"], 1, "$4\\text{ m}^3\\ 25\\text{ dm}^3 = 4,025\\text{ m}^3 < 4,25\\text{ m}^3$."),
            make_mc(6, "Một khối kim loại có thể tích $0,02\\text{ m}^3$. Đổi ra xăng-ti-mét khối ta được:", ["$20\\text{ cm}^3$", "$200\\text{ cm}^3$", "$2000\\text{ cm}^3$", "$20\\,000\\text{ cm}^3$"], 3, "$0,02 \\times 1\\,000\\,000 = 20\\,000\\text{ cm}^3$.")
        ],
        "part2": [
            make_essay(1, "Viết các số đo sau dưới dạng số thập phân có đơn vị đo là mét khối:\na) $1850\\text{ dm}^3$\nb) $7\\text{ m}^3\\ 80\\text{ dm}^3$", "a) $1850 : 1000 = 1,85\\text{ m}^3$\nb) $7 + 80/1000 = 7,08\\text{ m}^3$", "a) 1,85 m³; b) 7,08 m³", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $2,8\\text{ m}^3 \\times 2 + 1500\\text{ dm}^3$\nb) $(4,5\\text{ m}^3 - 1,5\\text{ m}^3) : 6$", "a) $5,6\\text{ m}^3 + 1,5\\text{ m}^3 = 7,1\\text{ m}^3$\nb) $3\\text{ m}^3 : 6 = 0,5\\text{ m}^3 = 500\\text{ dm}^3$", "a) 7,1 m³; b) 0,5 m³ (500 dm³)", 4, 1.0),
            make_essay(3, "Tìm $y$ biết:\n$y : 5 = 180\\text{ dm}^3$", "Ta có:\n$y = 180\\text{ dm}^3 \\times 5 = 900\\text{ dm}^3 = 0,9\\text{ m}^3$.\nĐáp số: $y = 900\\text{ dm}^3$.", "y = 900 dm³ (0,9 m³)", 4, 1.0),
            make_essay(4, "Một bể nước dạng hình hộp chữ nhật có thể tích $3,6\\text{ m}^3$. Người ta dùng máy bơm có lưu lượng 45 lít mỗi phút để bơm nước vào bể (ban đầu bể cạn).\na) Sau 40 phút bơm thì lượng nước trong bể là bao nhiêu lít?\nb) Khi đó lượng nước trong bể chiếm bao nhiêu phần trăm dung tích của bể?", "Bài giải:\na) Sau 40 phút lượng nước bơm vào là:\n$45 \\times 40 = 1800\\text{ (lít)}$\nb) Đổi: $3,6\\text{ m}^3 = 3600\\text{ dm}^3 = 3600\\text{ lít}$.\nTỉ số phần trăm lượng nước trong bể là:\n$1800 : 3600 = 0,5 = 50\\%$\nĐáp số:\na) $1800\\text{ lít}$;\nb) $50\\%$.", "a) 1800 lít; b) 50%", 5, 1.5),
            make_essay(5, "Một chiếc xe tải chở một khối đá hoa cương có thể tích $2,5\\text{ m}^3$. Biết rằng cứ $1\\text{ dm}^3$ đá hoa cương cân nặng $2,7\\text{ kg}$.\na) Tính khối lượng khối đá theo đơn vị ki-lô-gam.\nb) Khối đá đó có vượt quá trọng tải 6 tấn của xe tải không?", "Bài giải:\nĐổi: $2,5\\text{ m}^3 = 2500\\text{ dm}^3$.\na) Khối lượng của khối đá hoa cương là:\n$2500 \\times 2,7 = 6750\\text{ (kg)}$\nb) Đổi: 6 tấn $= 6000\\text{ kg}$.\nVì $6750\\text{ kg} > 6000\\text{ kg}$ nên khối đá đó đã vượt quá trọng tải của xe tải.\nĐáp số:\na) $6750\\text{ kg}$;\nb) Có vượt quá trọng tải.", "a) 6750 kg; b) Có vượt quá", 5, 1.5),
            make_essay(6, "Một bình đong chứa đầy 2 lít nước. Người ta rót vào 4 cốc, mỗi cốc chứa $350\\text{ cm}^3$ nước. Hỏi lượng nước còn lại trong bình là bao nhiêu xăng-ti-mét khối?", "Bài giải:\nĐổi: $2\\text{ lít} = 2\\text{ dm}^3 = 2000\\text{ cm}^3$.\nLượng nước đã rót vào 4 cốc là:\n$350 \\times 4 = 1400\\text{ (cm}^3)$\nLượng nước còn lại trong bình là:\n$2000 - 1400 = 600\\text{ (cm}^3)$\nĐáp số: $600\\text{ cm}^3$.", "600 cm³", 5, 1.0)
        ]
    }

    # --- Bài 37 - Đề 3 ---
    exams["th5_b37_test3"] = {
        "id": "th5_b37_test3",
        "lessonId": "th5_b37",
        "lessonNum": 37,
        "testNum": 3,
        "title": "Bài 37: Luyện tập chung Chủ đề 7 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 7",
        "chapter": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm $4,05\\text{ m}^3 = \\dots\\text{ dm}^3$ là:", ["405", "4050", "450", "40 500"], 1, "$4,05 \\times 1000 = 4050\\text{ dm}^3$."),
            make_mc(2, "Đổi: $68\\,000\\text{ cm}^3 = \\dots\\text{ dm}^3$:", ["680", "68", "6,8", "0,68"], 1, "$68\\,000 : 1000 = 68\\text{ dm}^3$."),
            make_mc(3, "Thể tích của một hình lập phương có cạnh $10\\text{ cm}$ là:", ["$100\\text{ cm}^3$", "$1000\\text{ cm}^3$", "$1\\text{ dm}^3$", "Cả B và C đều đúng"], 3, "$10 \\times 10 \\times 10 = 1000\\text{ cm}^3 = 1\\text{ dm}^3$."),
            make_mc(4, "Một bể nước chứa $1800\\text{ dm}^3$ nước, tức là chứa:", ["18 lít", "180 lít", "1800 lít", "1,8 lít"], 2, "1800 lít nước."),
            make_mc(5, "Tính: $0,6\\text{ m}^3 \\times 5 = \\dots\\text{ m}^3$:", ["3", "30", "0,3", "300"], 0, "$0,6 \\times 5 = 3\\text{ m}^3$."),
            make_mc(6, "Một thùng dầu chứa 120 lít dầu, người ta lấy ra $25\\%$. Thể tích dầu còn lại trong thùng là:", ["30 lít", "80 lít", "90 lít", "100 lít"], 2, "$120 \\times (100\\% - 25\\%) : 100 = 90$ lít.")
        ],
        "part2": [
            make_essay(1, "Điền dấu ($<, >, =$) thích hợp vào chỗ chấm:\na) $5,2\\text{ m}^3 \\dots 5200\\text{ dm}^3$\nb) $3\\text{ m}^3\\ 40\\text{ dm}^3 \\dots 3400\\text{ dm}^3$", "a) $5,2\\text{ m}^3 = 5200\\text{ dm}^3$, điền $=$\nb) $3\\text{ m}^3\\ 40\\text{ dm}^3 = 3040\\text{ dm}^3 < 3400\\text{ dm}^3$, điền $<$", "a) =; b) <", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $2,75\\text{ m}^3 + 1,25\\text{ m}^3 - 800\\text{ dm}^3$\nb) $350\\text{ dm}^3 \\times 4 : 2$", "a) $4\\text{ m}^3 - 0,8\\text{ m}^3 = 3,2\\text{ m}^3 = 3200\\text{ dm}^3$\nb) $1400\\text{ dm}^3 : 2 = 700\\text{ dm}^3$", "a) 3,2 m³ (3200 dm³); b) 700 dm³", 4, 1.0),
            make_essay(3, "Tìm $x$ biết:\n$x - 0,75\\text{ m}^3 = 450\\text{ dm}^3$", "Đổi $0,75\\text{ m}^3 = 750\\text{ dm}^3$.\nTa có: $x = 450 + 750 = 1200\\text{ dm}^3 = 1,2\\text{ m}^3$.\nĐáp số: $x = 1,2\\text{ m}^3$.", "x = 1,2 m³", 4, 1.0),
            make_essay(4, "Một bể chứa nước có thể tích $4\\text{ m}^3$. Hiện tại bể đang chứa $2400\\text{ dm}^3$ nước.\na) Lượng nước hiện có chiếm bao nhiêu phần trăm thể tích của bể?\nb) Người ta xả bớt nước ra để vệ sinh bể, lưu lượng xả là 50 lít mỗi phút. Hỏi sau bao lâu thì xả hết số nước đang có trong bể?", "Bài giải:\nĐổi: $4\\text{ m}^3 = 4000\\text{ dm}^3 = 4000\\text{ lít}$.\n$2400\\text{ dm}^3 = 2400\\text{ lít}$.\na) Tỉ số phần trăm lượng nước hiện có so với bể là:\n$2400 : 4000 = 0,6 = 60\\%$\nb) Thời gian để xả hết nước trong bể là:\n$2400 : 50 = 48\\text{ (phút)}$\nĐáp số:\na) $60\\%$;\nb) 48 phút.", "a) 60%; b) 48 phút", 5, 1.5),
            make_essay(5, "Một khối gỗ hình lập phương có cạnh $0,8\\text{ m}$.\na) Tính thể tích của khối gỗ đó.\nb) Biết mỗi mét khối gỗ đó nặng $700\\text{ kg}$. Tính khối lượng của khối gỗ đó.", "Bài giải:\na) Thể tích của khối gỗ hình lập phương là:\n$0,8 \\times 0,8 \\times 0,8 = 0,512\\text{ (m}^3)$\nb) Khối lượng của khối gỗ đó là:\n$0,512 \\times 700 = 358,4\\text{ (kg)}$\nĐáp số:\na) $0,512\\text{ m}^3$;\nb) $358,4\\text{ kg}$.", "a) 0,512 m³; b) 358,4 kg", 5, 1.5),
            make_essay(6, "Một bình thủy tinh hình hộp chữ nhật có diện tích đáy là $250\\text{ cm}^2$ đang chứa nước. Khi thả một khối kim loại chìm hoàn toàn vào bình thì mực nước dâng cao thêm $2\\text{ cm}$. Tính thể tích của khối kim loại đó theo đơn vị đề-xi-mét khối.", "Bài giải:\nThể tích nước dâng lên bằng thể tích khối kim loại:\n$250 \\times 2 = 500\\text{ (cm}^3)$\nĐổi: $500\\text{ cm}^3 = 0,5\\text{ dm}^3$.\nĐáp số: $0,5\\text{ dm}^3$.", "0,5 dm³", 5, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 7: {len(ex)} (Kỳ vọng: 9 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
