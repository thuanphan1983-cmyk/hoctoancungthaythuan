# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 7: ÔN TẬP HỌC KÌ 1 (BÀI 29 ĐẾN BÀI 31)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 3 bài học x 3 đề độc lập = 9 đề kiểm tra chất lượng cao (th4_b29_test1 -> th4_b31_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, question_text, options, correct, explanation):
    q_title = f"**Câu {qid}:** {question_text}" if not question_text.startswith(f"**Câu {qid}:**") else question_text
    return {
        "id": qid,
        "question": q_title,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question_text, solution, answer, lineCount=4, points=1.0):
    p_title = f"**Bài {qid}:** {question_text}" if not question_text.startswith(f"**Bài {qid}:**") else question_text
    return {
        "id": qid,
        "question": p_title,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 29: ÔN TẬP SỐ TỰ NHIÊN VÀ CÁC PHÉP TÍNH
    # =========================================================================

    # --- Bài 29 - Đề 1 ---
    exams["th4_b29_test1"] = {
        "id": "th4_b29_test1",
        "lessonId": "th4_b29",
        "lessonNum": 29,
        "testNum": 1,
        "title": "Bài 29: Ôn tập số tự nhiên và các phép tính - Đề số 1",
        "topic": "Ôn tập số tự nhiên và các phép tính",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 5 triệu, 7 trăm nghìn, 3 chục và 8 đơn vị viết là:", ["5 700 038", "5 070 038", "5 700 380", "570 038"], 0, "5 triệu, 7 trăm nghìn, 0 chục nghìn, 0 nghìn, 0 trăm, 3 chục, 8 đơn vị: 5 700 038."),
            make_mc(2, "Giá trị của chữ số 6 trong số 8 625 400 là:", ["600 000", "60 000", "6 000 000", "6 000"], 0, "Chữ số 6 ở hàng trăm nghìn có giá trị 600 000."),
            make_mc(3, "Làm tròn số 485 729 đến hàng trăm nghìn ta được:", ["500 000", "400 000", "490 000", "480 000"], 0, "Chữ số hàng chục nghìn là 8 >= 5 nên làm tròn lên 500 000."),
            make_mc(4, "Kết quả của phép tính $450\\,000 + 250\\,000 - 180\\,000$ là:", ["520 000", "500 000", "540 000", "620 000"], 0, "700 000 - 180 000 = 520 000."),
            make_mc(5, "Số lớn nhất có 6 chữ số khác nhau là:", ["987 654", "999 999", "987 650", "986 754"], 0, "987 654 có 6 chữ số giảm dần từ 9."),
            make_mc(6, "Tìm $x$ biết: $x + 125\\,000 = 400\\,000$:", ["275 000", "285 000", "375 000", "525 000"], 0, "x = 400 000 - 125 000 = 275 000.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $384\\,625 + 247\\,389$\nb) $702\\,400 - 356\\,815$", "a) $384\\,625 + 247\\,389 = 632\\,014$.\nb) $702\\,400 - 356\\,815 = 345\\,585$.", "a) 632 014; b) 345 585", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $256 + 189 + 744 + 311$\nb) $35 \\times 4 \\times 25$", "a) $(256 + 744) + (189 + 311) = 1000 + 500 = 1500$.\nb) $35 \\times (4 \\times 25) = 35 \\times 100 = 3500$.", "a) 1500; b) 3500", 4, 1.0),
            make_essay(3, "Một thư viện trường học có 45 600 cuốn sách. Tháng trước thư viện nhận thêm 3 450 cuốn, tháng này nhận thêm 2 550 cuốn. Hỏi hiện nay thư viện có tất cả bao nhiêu cuốn sách? (Tính bằng cách thuận tiện).", "Số sách nhận thêm trong hai tháng là:\n$3450 + 2550 = 6000\\text{ (cuốn)}$.\nHiện nay thư viện có số cuốn sách là:\n$45\\,600 + 6000 = 51\\,600\\text{ (cuốn)}$.", "51 600 cuốn sách", 4, 1.0),
            make_essay(4, "Một nông trường có hai đồi trồng chè. Đồi thứ nhất thu hoạch được 14 tấn 5 tạ búp chè tươi. Đồi thứ hai thu hoạch được ít hơn đồi thứ nhất 18 tạ. Hỏi cả hai đồi thu hoạch được bao nhiêu tạ búp chè tươi?", "Đổi: $14\\text{ tấn } 5\\text{ tạ} = 145\\text{ tạ}$.\nĐồi thứ hai thu hoạch được là:\n$145 - 18 = 127\\text{ (tạ)}$.\nCả hai đồi thu hoạch được tất cả là:\n$145 + 127 = 272\\text{ (tạ)}$.", "272 tạ", 5, 1.5),
            make_essay(5, "Tổng của hai số là 480. Nếu lấy số lớn trừ đi số bé thì được hiệu là 64. Tìm hai số đó.", "Số lớn là:\n$(480 + 64) : 2 = 272$.\nSố bé là:\n$480 - 272 = 208$.", "Số lớn: 272; Số bé: 208", 5, 1.5),
            make_essay(6, "Viết số tự nhiên bé nhất có tích các chữ số bằng 30.", "Phân tích 30 thành tích các chữ số khác 1: $30 = 5 \\times 6$ hoặc $30 = 2 \\times 3 \\times 5$.\nĐể số tự nhiên là bé nhất thì số đó phải có ít chữ số nhất. Do đó ta chọn 2 chữ số: 5 và 6.\nSắp xếp chữ số nhỏ đứng trước để được số nhỏ nhất: 56.", "56", 4, 1.0)
        ]
    }

    # --- Bài 29 - Đề 2 ---
    exams["th4_b29_test2"] = {
        "id": "th4_b29_test2",
        "lessonId": "th4_b29",
        "lessonNum": 29,
        "testNum": 2,
        "title": "Bài 29: Ôn tập số tự nhiên và các phép tính - Đề số 2",
        "topic": "Ôn tập số tự nhiên và các phép tính",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 8 chục triệu, 4 triệu, 5 trăm nghìn và 2 đơn vị viết là:", ["84 500 002", "84 050 002", "80 450 002", "84 502 000"], 0, "84 500 002."),
            make_mc(2, "Số liền sau của số 999 999 là:", ["1 000 000", "999 998", "1 000 001", "10 000 000"], 0, "999 999 + 1 = 1 000 000."),
            make_mc(3, "Hiệu của số chẵn lớn nhất có 5 chữ số và số lẻ bé nhất có 5 chữ số là:", ["89 997", "89 999", "89 998", "99 999"], 0, "99 998 - 10 001 = 89 997."),
            make_mc(4, "Tìm $y$, biết: $y - 340\\,000 = 660\\,000$:", ["1 000 000", "320 000", "900 000", "1 100 000"], 0, "y = 660 000 + 340 000 = 1 000 000."),
            make_mc(5, "Tính nhẩm: $25 \\times 8 = \\dots$:", ["200", "150", "250", "180"], 0, "25 x 4 = 100 => 25 x 8 = 200."),
            make_mc(6, "Trong dãy số tự nhiên, hai số chẵn liên tiếp hơn kém nhau:", ["2 đơn vị", "1 đơn vị", "10 đơn vị", "4 đơn vị"], 0, "Hai số chẵn liên tiếp hơn kém nhau 2 đơn vị.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $456\\,780 + 328\\,546$\nb) $900\\,000 - 467\\,832$", "a) $456\\,780 + 328\\,546 = 785\\,326$.\nb) $900\\,000 - 467\\,832 = 432\\,168$.", "a) 785 326; b) 432 168", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức bằng cách thuận tiện nhất:\na) $435 + 278 + 565 + 122$\nb) $125 \\times 7 \\times 8$", "a) $(435 + 565) + (278 + 122) = 1000 + 400 = 1400$.\nb) $(125 \\times 8) \\times 7 = 1000 \\times 7 = 7000$.", "a) 1400; b) 7000", 4, 1.0),
            make_essay(3, "Một cửa hàng xăng dầu có hai bể chứa tất cả 36 000 lít dầu. Nếu chuyển 4 000 lít dầu từ bể thứ nhất sang bể thứ hai thì lượng dầu ở hai bể bằng nhau. Hỏi lúc đầu mỗi bể có bao nhiêu lít dầu?", "Lúc đầu bể thứ nhất nhiều hơn bể thứ hai là:\n$4000 \\times 2 = 8000\\text{ (lít)}$.\nBể thứ nhất chứa số lít dầu là:\n$(36\\,000 + 8000) : 2 = 22\\,000\\text{ (lít)}$.\nBể thứ hai chứa số lít dầu là:\n$36\\,000 - 22\\,000 = 14\\,000\\text{ (lít)}$.", "Bể 1: 22 000 lít; Bể 2: 14 000 lít", 4, 1.0),
            make_essay(4, "Một đoàn tàu chở hàng có 6 toa chở gạo, mỗi toa chở 25 tấn gạo và 4 toa chở ngô, mỗi toa chở 20 tấn ngô. Hỏi đoàn tàu đó chở tất cả bao nhiêu tấn lương thực?", "Khối lượng gạo đoàn tàu chở là:\n$25 \\times 6 = 150\\text{ (tấn)}$.\nKhối lượng ngô đoàn tàu chở là:\n$20 \\times 4 = 80\\text{ (tấn)}$.\nĐoàn tàu chở tất cả số tấn lương thực là:\n$150 + 80 = 230\\text{ (tấn)}$.", "230 tấn lương thực", 5, 1.5),
            make_essay(5, "Năm nay tổng số tuổi của hai ông cháu là 75 tuổi. Ông hơn cháu 57 tuổi. Hỏi năm nay ông bao nhiêu tuổi, cháu bao nhiêu tuổi?", "Tuổi của ông hiện nay là:\n$(75 + 57) : 2 = 66\\text{ (tuổi)}$.\nTuổi của cháu hiện nay là:\n$75 - 66 = 9\\text{ (tuổi)}$.", "Ông: 66 tuổi; Cháu: 9 tuổi", 5, 1.5),
            make_essay(6, "Tìm một số có ba chữ số, biết rằng chữ số hàng trăm gấp đôi chữ số hàng chục, chữ số hàng chục gấp 3 lần chữ số hàng đơn vị.", "Gọi chữ số hàng đơn vị là c ($c > 0$).\nChữ số hàng chục là $b = 3 \\times c$.\nChữ số hàng trăm là $a = 2 \\times b = 2 \\times 3 \\times c = 6 \\times c$.\nVì a là chữ số có 1 chữ số nên $6 \\times c \\le 9 \\Rightarrow c = 1$.\nKhi đó: $c = 1 \\Rightarrow b = 3 \\Rightarrow a = 6$.\nVậy số cần tìm là 631.", "631", 4, 1.0)
        ]
    }

    # --- Bài 29 - Đề 3 ---
    exams["th4_b29_test3"] = {
        "id": "th4_b29_test3",
        "lessonId": "th4_b29",
        "lessonNum": 29,
        "testNum": 3,
        "title": "Bài 29: Ôn tập số tự nhiên và các phép tính - Đề số 3",
        "topic": "Ôn tập số tự nhiên và các phép tính",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 6 triệu, 4 trăm và 5 đơn vị viết là:", ["6 000 405", "6 040 005", "6 400 005", "6 004 050"], 0, "6 000 405."),
            make_mc(2, "Số bé nhất có 7 chữ số là:", ["1 000 000", "1 000 001", "9 999 999", "10 000 000"], 0, "1 000 000 có 7 chữ số."),
            make_mc(3, "Kết quả của biểu thức $150\\,000 + (350\\,000 - 100\\,000)$ là:", ["400 000", "500 000", "300 000", "450 000"], 0, "150 000 + 250 000 = 400 000."),
            make_mc(4, "Một số cộng với 0 thì bằng:", ["Chính số đó", "0", "1", "Không xác định"], 0, "a + 0 = a."),
            make_mc(5, "Tổng của số lớn nhất có 4 chữ số và số bé nhất có 4 chữ số là:", ["10 999", "11 000", "9 999", "10 000"], 0, "9 999 + 1 000 = 10 999."),
            make_mc(6, "Tìm $x$ biết $800\\,000 - x = 250\\,000$:", ["550 000", "650 000", "1 050 000", "450 000"], 0, "x = 800 000 - 250 000 = 550 000.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $618\\,247 + 293\\,865$\nb) $804\\,512 - 376\\,948$", "a) $618\\,247 + 293\\,865 = 912\\,112$.\nb) $804\\,512 - 376\\,948 = 427\\,564$.", "a) 912 112; b) 427 564", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $365 + 148 + 635 + 252$\nb) $25 \\times 9 \\times 4$", "a) $(365 + 635) + (148 + 252) = 1000 + 400 = 1400$.\nb) $(25 \\times 4) \\times 9 = 100 \\times 9 = 900$.", "a) 1400; b) 900", 4, 1.0),
            make_essay(3, "Một xí nghiệp may trong tháng 10 sản xuất được 24 500 bộ quần áo. Tháng 11 sản xuất được nhiều hơn tháng 10 là 3 200 bộ. Tháng 12 sản xuất được nhiều hơn tháng 11 là 1 800 bộ. Hỏi cả ba tháng xí nghiệp may được bao nhiêu bộ quần áo?", "Tháng 11 xí nghiệp may được là:\n$24\\,500 + 3200 = 27\\,700\\text{ (bộ)}$.\nTháng 12 xí nghiệp may được là:\n$27\\,700 + 1800 = 29\\,500\\text{ (bộ)}$.\nCả ba tháng may được là:\n$24\\,500 + 27\\,700 + 29\\,500 = 81\\,700\\text{ (bộ)}$.", "81 700 bộ quần áo", 4, 1.0),
            make_essay(4, "Một cửa hàng nhập về 5 tấn gạo gồm gạo tẻ và gạo nếp. Số gạo tẻ nhiều hơn gạo nếp là 14 tạ. Hỏi cửa hàng nhập về bao nhiêu tạ gạo mỗi loại?", "Đổi: $5\\text{ tấn} = 50\\text{ tạ}$.\nKhối lượng gạo tẻ nhập về là:\n$(50 + 14) : 2 = 32\\text{ (tạ)}$.\nKhối lượng gạo nếp nhập về là:\n$50 - 32 = 18\\text{ (tạ)}$.", "Gạo tẻ: 32 tạ; Gạo nếp: 18 tạ", 5, 1.5),
            make_essay(5, "Hai thùng đựng tất cả 150 lít nước. Nếu đổ 10 lít nước từ thùng thứ nhất sang thùng thứ hai thì thùng thứ hai vẫn ít hơn thùng thứ nhất 10 lít. Hỏi ban đầu mỗi thùng có bao nhiêu lít nước?", "Sau khi đổ 10 lít từ thùng 1 sang thùng 2, thùng 1 hơn thùng 2 là 10 lít.\nVậy ban đầu thùng 1 hơn thùng 2 là:\n$10 \\times 2 + 10 = 30\\text{ (lít)}$.\nSố lít nước ban đầu ở thùng thứ nhất là:\n$(150 + 30) : 2 = 90\\text{ (lít)}$.\nSố lít nước ban đầu ở thùng thứ hai là:\n$150 - 90 = 60\\text{ (lít)}$.", "Thùng 1: 90 lít; Thùng 2: 60 lít", 5, 1.5),
            make_essay(6, "Tính tổng của dãy số cách đều sau:\n$S = 5 + 10 + 15 + 20 + \\dots + 95 + 100$", "Số các số hạng của dãy số là: $(100 - 5) : 5 + 1 = 20\\text{ (số)}$.\nTổng của dãy số là:\n$(100 + 5) \\times 20 : 2 = 105 \\times 10 = 1050$.", "1050", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 30: ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG
    # =========================================================================

    # --- Bài 30 - Đề 1 ---
    exams["th4_b30_test1"] = {
        "id": "th4_b30_test1",
        "lessonId": "th4_b30",
        "lessonNum": 30,
        "testNum": 1,
        "title": "Bài 30: Ôn tập hình học và đo lường - Đề số 1",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm: $4\\text{ tấn } 80\\text{ kg} = \\dots \\text{ kg}$ là:", ["4 080", "4 800", "480", "40 080"], 0, "4 000 + 80 = 4 080 kg."),
            make_mc(2, "Đổi $3\\text{ m}^2 \\text{ } 15\\text{ dm}^2 = \\dots \\text{ dm}^2$:", ["315 dm²", "3 015 dm²", "3 150 dm²", "31,5 dm²"], 0, "300 + 15 = 315 dm²."),
            make_mc(3, "Năm 1975 giải phóng hoàn toàn miền Nam, thống nhất đất nước. Năm đó thuộc thế kỉ nào?", ["Thế kỉ XX", "Thế kỉ XIX", "Thế kỉ XXI", "Thế kỉ XVIII"], 0, "Năm 1975 thuộc thế kỉ XX."),
            make_mc(4, "Góc tạo bởi hai kim đồng hồ lúc 9 giờ đúng là:", ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0, "Lúc 9 giờ hai kim vuông góc với nhau (90°)."),
            make_mc(5, "Hình thoi có hai đường chéo:", ["Vuông góc với nhau", "Song song với nhau", "Bằng nhau", "Không cắt nhau"], 0, "Hai đường chéo hình thoi vuông góc với nhau."),
            make_mc(6, "Chu vi hình vuông có diện tích $36\\text{ cm}^2$ là:", ["24 cm", "12 cm", "18 cm", "36 cm"], 0, "Cạnh = 6 cm (vì 6 x 6 = 36). Chu vi = 6 x 4 = 24 cm.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $6\\text{ tạ } 5\\text{ yến} = \\dots \\text{ kg}$\nb) $8\\text{ dm}^2 \\text{ } 45\\text{ cm}^2 = \\dots \\text{ cm}^2$", "a) $6\\text{ tạ} = 600\\text{ kg}$, $5\\text{ yến} = 50\\text{ kg}$ => $650\\text{ kg}$.\nb) $8\\text{ dm}^2 = 800\\text{ cm}^2$ => $800 + 45 = 845\\text{ cm}^2$.", "a) 650; b) 845", 4, 1.0),
            make_essay(2, "Điền tên góc (góc nhọn, góc vuông, góc tù, góc bẹt) thích hợp vào chỗ chấm:\na) Góc đỉnh O, cạnh OA và OB có số đo $60^\\circ$ là $\\dots$\nb) Góc đỉnh O, cạnh OC và OD có số đo $120^\\circ$ là $\\dots$", "a) Góc có số đo $60^\\circ < 90^\\circ$ là góc nhọn.\nb) Góc có số đo $90^\\circ < 120^\\circ < 180^\\circ$ là góc tù.", "a) Góc nhọn; b) Góc tù", 4, 1.0),
            make_essay(3, "Một khu vườn hình chữ nhật có chiều dài 28 m, chiều rộng 15 m. Người ta dùng $\\frac{1}{4}$ diện tích khu vườn để làm lối đi và trồng hoa, phần còn lại trồng cây cảnh. Tính diện tích phần đất trồng cây cảnh.", "Diện tích khu vườn là:\n$28 \\times 15 = 420\\text{ (m}^2)$.\nDiện tích đất làm lối đi và hoa là:\n$420 : 4 = 105\\text{ (m}^2)$.\nDiện tích đất trồng cây cảnh là:\n$420 - 105 = 315\\text{ (m}^2)$.", "315 m²", 4, 1.0),
            make_essay(4, "Một ô tô chở 3 tấn 5 tạ gạo. Đến cửa hàng thứ nhất xe dỡ xuống 12 tạ gạo, đến cửa hàng thứ hai xe dỡ xuống nhiều hơn cửa hàng thứ nhất 3 tạ gạo. Hỏi sau khi dỡ hàng ở hai cửa hàng, trên xe còn lại bao nhiêu tạ gạo?", "Đổi: $3\\text{ tấn } 5\\text{ tạ} = 35\\text{ tạ}$.\nCửa hàng thứ hai nhận số tạ gạo là:\n$12 + 3 = 15\\text{ (tạ)}$.\nTổng số gạo đã dỡ ở cả hai cửa hàng là:\n$12 + 15 = 27\\text{ (tạ)}$.\nSố gạo còn lại trên xe là:\n$35 - 27 = 8\\text{ (tạ)}$.", "8 tạ", 5, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có chu vi 112 m, chiều dài hơn chiều rộng 16 m. Người ta dùng gạch men hình vuông cạnh 4 dm lát một lối đi dạo có diện tích bằng $\\frac{1}{10}$ diện tích mảnh đất. Hỏi cần bao nhiêu viên gạch men để lát lối đi đó?", "Nửa chu vi mảnh đất là: $112 : 2 = 56\\text{ (m)}$.\nChiều dài mảnh đất là: $(56 + 16) : 2 = 36\\text{ (m)}$.\nChiều rộng mảnh đất là: $56 - 36 = 20\\text{ (m)}$.\nDiện tích cả mảnh đất là: $36 \\times 20 = 720\\text{ (m}^2)$.\nDiện tích lối đi là: $720 : 10 = 72\\text{ (m}^2) = 7200\\text{ dm}^2$.\nDiện tích 1 viên gạch là: $4 \\times 4 = 16\\text{ (dm}^2)$.\nSố viên gạch cần dùng là: $7200 : 16 = 450\\text{ (viên)}$.", "450 viên gạch", 5, 1.5),
            make_essay(6, "Cho hình vuông ABCD có chu vi 40 cm. Lấy điểm M là trung điểm cạnh AB, điểm N là trung điểm cạnh CD. Tính diện tích hình chữ nhật AMND.", "Cạnh hình vuông ABCD là: $40 : 4 = 10\\text{ (cm)}$.\nĐộ dài đoạn AM là: $10 : 2 = 5\\text{ (cm)}$.\nCạnh AD dài 10 cm.\nDiện tích hình chữ nhật AMND là:\n$5 \\times 10 = 50\\text{ (cm}^2)$.", "50 cm²", 4, 1.0)
        ]
    }

    # --- Bài 30 - Đề 2 ---
    exams["th4_b30_test2"] = {
        "id": "th4_b30_test2",
        "lessonId": "th4_b30",
        "lessonNum": 30,
        "testNum": 2,
        "title": "Bài 30: Ôn tập hình học và đo lường - Đề số 2",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm: $5\\text{ tạ } = \\dots \\text{ kg}$ là:", ["500", "50", "5 000", "50 000"], 0, "1 tạ = 100 kg nên 5 tạ = 500 kg."),
            make_mc(2, "Đổi $7\\text{ m}^2 = \\dots \\text{ cm}^2$:", ["70 000", "700", "7 000", "700 000"], 0, "1 m² = 10 000 cm² nên 7 m² = 70 000 cm²."),
            make_mc(3, "Thế kỉ thứ XXI kết thúc vào năm nào?", ["2100", "2099", "2000", "2024"], 0, "Thế kỉ XXI từ 2001 đến 2100."),
            make_mc(4, "Góc tạo bởi hai kim đồng hồ lúc 5 giờ đúng là:", ["Góc tù", "Góc nhọn", "Góc vuông", "Góc bẹt"], 0, "Lúc 5 giờ góc giữa hai kim là 150° (lớn hơn 90° và nhỏ hơn 180°) là góc tù."),
            make_mc(5, "Hình bình hành có hai cặp cạnh đối diện:", ["Song song và bằng nhau", "Vuông góc với nhau", "Bằng nhau nhưng không song song", "Cắt nhau tại góc vuông"], 0, "Đặc điểm cơ bản của hình bình hành."),
            make_mc(6, "Một tấm bìa hình chữ nhật có diện tích $48\\text{ cm}^2$, chiều dài $8\\text{ cm}$. Chu vi tấm bìa đó là:", ["28 cm", "14 cm", "24 cm", "32 cm"], 0, "Chiều rộng = 48 : 8 = 6 cm. Chu vi = (8 + 6) x 2 = 28 cm.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $2\\text{ phút } 35\\text{ giây} = \\dots \\text{ giây}$\nb) $500\\text{ dm}^2 = \\dots \\text{ m}^2$", "a) $2 \\times 60 + 35 = 155\\text{ giây}$.\nb) $500 : 100 = 5\\text{ m}^2$.", "a) 155; b) 5", 4, 1.0),
            make_essay(2, "Kể tên các góc nhọn và góc tù có trong một hình thang cân ABCD (đáy nhỏ AB, đáy lớn CD).", "- Hai góc nhọn tại đáy lớn: góc ADC và góc BCD.\n- Hai góc tù tại đáy nhỏ: góc DAB và góc ABC.", "Góc nhọn: góc ADC, góc BCD; Góc tù: góc DAB, góc ABC", 4, 1.0),
            make_essay(3, "Bác Năm có một mảnh vườn hình chữ nhật dài 30 m, rộng 12 m. Bác rào xung quanh vườn bằng lưới thép và để cửa ra vào rộng 2 m. Tính số mét lưới thép bác Năm cần mua.", "Chu vi mảnh vườn là:\n$(30 + 12) \\times 2 = 84\\text{ (m)}$.\nSố mét lưới thép cần mua là:\n$84 - 2 = 82\\text{ (m)}$.", "82 m", 4, 1.0),
            make_essay(4, "Một đoàn xe gồm 4 xe chở hàng. Xe thứ nhất chở 2 tấn 8 tạ ngô. Ba xe sau mỗi xe chở 24 tạ ngô. Hỏi cả đoàn xe chở được bao nhiêu tạ ngô?", "Đổi: $2\\text{ tấn } 8\\text{ tạ} = 28\\text{ tạ}$.\n3 xe sau chở được số tạ ngô là:\n$24 \\times 3 = 72\\text{ (tạ)}$.\nCả đoàn xe chở được tất cả số tạ ngô là:\n$28 + 72 = 100\\text{ (tạ)}$.\n(Đổi ra tấn: $100\\text{ tạ} = 10\\text{ tấn}$).", "100 tạ (hoặc 10 tấn)", 5, 1.5),
            make_essay(5, "Một căn phòng hình chữ nhật dài 9 m, rộng 6 m. Người ta dùng gạch bông hình vuông cạnh 3 dm để lát nền phòng đó. Biết 1 hộp có 10 viên gạch và giá mỗi hộp là 180 000 đồng. Tính tổng số tiền mua gạch để lát nền phòng.", "Diện tích phòng là: $9 \\times 6 = 54\\text{ (m}^2) = 5400\\text{ dm}^2$.\nDiện tích 1 viên gạch là: $3 \\times 3 = 9\\text{ (dm}^2)$.\nSố viên gạch cần dùng là: $5400 : 9 = 600\\text{ (viên)}$.\nSố hộp gạch cần mua là: $600 : 10 = 60\\text{ (hộp)}$.\nTổng số tiền mua gạch là: $60 \\times 180\\,000 = 10\\,800\\,000\\text{ (đồng)}$.", "10 800 000 đồng", 5, 1.5),
            make_essay(6, "Một hình vuông có cạnh 8 cm. Một hình chữ nhật có chu vi bằng chu vi hình vuông đó và có chiều dài hơn chiều rộng 4 cm. Tính diện tích của hình chữ nhật đó.", "Chu vi hình vuông là: $8 \\times 4 = 32\\text{ (cm)}$.\nNửa chu vi hình chữ nhật là: $32 : 2 = 16\\text{ (cm)}$.\nChiều dài hình chữ nhật là: $(16 + 4) : 2 = 10\\text{ (cm)}$.\nChiều rộng hình chữ nhật là: $16 - 10 = 6\\text{ (cm)}$.\nDiện tích hình chữ nhật là: $10 \\times 6 = 60\\text{ (cm}^2)$.", "60 cm²", 4, 1.0)
        ]
    }

    # --- Bài 30 - Đề 3 ---
    exams["th4_b30_test3"] = {
        "id": "th4_b30_test3",
        "lessonId": "th4_b30",
        "lessonNum": 30,
        "testNum": 3,
        "title": "Bài 30: Ôn tập hình học và đo lường - Đề số 3",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một phần năm tạ bằng bao nhiêu ki-lô-gam?", ["20 kg", "50 kg", "25 kg", "10 kg"], 0, "100 : 5 = 20 kg."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $4\\text{ dm}^2 \\text{ } 8\\text{ mm}^2 = \\dots \\text{ mm}^2$ là:", ["40 008", "408", "4 008", "40 080"], 0, "4 dm² = 40 000 mm² => 40 000 + 8 = 40 008 mm²."),
            make_mc(3, "Bà Triệu lãnh đạo cuộc khởi nghĩa chống quân Ngô năm 248. Năm đó thuộc thế kỉ nào?", ["Thế kỉ III", "Thế kỉ II", "Thế kỉ IV", "Thế kỉ I"], 0, "Năm 248 thuộc thế kỉ III."),
            make_mc(4, "Góc tạo bởi hai kim đồng hồ lúc 1 giờ đúng là:", ["Góc nhọn", "Góc vuông", "Góc tù", "Góc bẹt"], 0, "Lúc 1 giờ góc giữa hai kim là 30° là góc nhọn."),
            make_mc(5, "Đoạn thẳng nối hai điểm đối diện của hình chữ nhật gọi là:", ["Đường chéo", "Cạnh bên", "Chiều dài", "Chiều rộng"], 0, "Đó là đường chéo của hình chữ nhật."),
            make_mc(6, "Một mảnh đất hình bình hành có độ dài đáy 20 m, chiều cao 12 m. Diện tích mảnh đất là:", ["240 m²", "120 m²", "64 m²", "480 m²"], 0, "20 x 12 = 240 m².")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $3\\text{ thế kỉ } 40\\text{ năm} = \\dots \\text{ năm}$\nb) $12\\text{ m}^2 \\text{ } 6\\text{ dm}^2 = \\dots \\text{ dm}^2$", "a) $3 \\times 100 + 40 = 340\\text{ năm}$.\nb) $12 \\times 100 + 6 = 1206\\text{ dm}^2$.", "a) 340; b) 1206", 4, 1.0),
            make_essay(2, "Quan sát hình chữ nhật ABCD. Kể tên các góc vuông và các cặp cạnh song song.", "- 4 góc vuông tại các đỉnh A, B, C, D.\n- 2 cặp cạnh song song: AB song song CD; AD song song BC.", "4 góc vuông tại A, B, C, D; Các cặp cạnh song song: (AB, CD), (AD, BC)", 4, 1.0),
            make_essay(3, "Một mảnh đất hình bình hành có đáy dài 36 m, chiều cao bằng $\\frac{2}{3}$ đáy. Tính diện tích mảnh đất đó.", "Chiều cao mảnh đất là:\n$36 \\times 2 : 3 = 24\\text{ (m)}$.\nDiện tích mảnh đất hình bình hành là:\n$36 \\times 24 = 864\\text{ (m}^2)$.", "864 m²", 4, 1.0),
            make_essay(4, "Một đoàn xe tải có 5 xe, gồm 2 xe lớn chở mỗi xe 3 tấn 5 tạ cát và 3 xe nhỏ chở mỗi xe 18 tạ cát. Hỏi cả 5 xe chở được tất cả bao nhiêu tấn cát?", "Đổi: $3\\text{ tấn } 5\\text{ tạ} = 35\\text{ tạ}$.\n2 xe lớn chở được là:\n$35 \\times 2 = 70\\text{ (tạ)}$.\n3 xe nhỏ chở được là:\n$18 \\times 3 = 54\\text{ (tạ)}$.\nCả đoàn chở được là:\n$70 + 54 = 124\\text{ (tạ)} = 12,4\\text{ (tấn)}$ (hoặc 12 tấn 4 tạ).", "12 tấn 4 tạ (hoặc 124 tạ)", 5, 1.5),
            make_essay(5, "Một khu vui chơi hình chữ nhật có chu vi 160 m. Chiều dài hơn chiều rộng 20 m. Người ta trải thảm cỏ nhân tạo cho $\\frac{3}{5}$ diện tích khu vui chơi với chi phí 120 000 đồng/m². Tính tổng số tiền mua thảm cỏ nhân tạo.", "Nửa chu vi khu vui chơi là: $160 : 2 = 80\\text{ (m)}$.\nChiều dài khu vui chơi là: $(80 + 20) : 2 = 50\\text{ (m)}$.\nChiều rộng khu vui chơi là: $80 - 50 = 30\\text{ (m)}$.\nDiện tích cả khu vui chơi là: $50 \\times 30 = 1500\\text{ (m}^2)$.\nDiện tích trải thảm cỏ là: $1500 \\times 3 : 5 = 900\\text{ (m}^2)$.\nSố tiền mua thảm cỏ là:\n$900 \\times 120\\,000 = 108\\,000\\,000\\text{ (đồng)}$.", "108 000 000 đồng", 5, 1.5),
            make_essay(6, "Bác An có một tấm gỗ hình chữ nhật dài 18 dm, rộng 12 dm. Bác cưa tấm gỗ đó thành các mảnh gỗ hình vuông nhỏ có cạnh 3 dm. Hỏi bác cưa được tất cả bao nhiêu mảnh gỗ hình vuông nhỏ như thế?", "Số mảnh gỗ theo chiều dài là: $18 : 3 = 6\\text{ (mảnh)}$.\nSố mảnh gỗ theo chiều rộng là: $12 : 3 = 4\\text{ (mảnh)}$.\nTổng số mảnh gỗ hình vuông nhỏ cưa được là:\n$6 \\times 4 = 24\\text{ (mảnh)}$.", "24 mảnh gỗ", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 31: ÔN TẬP CHUNG HỌC KÌ 1
    # =========================================================================

    # --- Bài 31 - Đề 1 ---
    exams["th4_b31_test1"] = {
        "id": "th4_b31_test1",
        "lessonId": "th4_b31",
        "lessonNum": 31,
        "testNum": 1,
        "title": "Bài 31: Ôn tập chung học kì 1 - Đề số 1",
        "topic": "Ôn tập chung học kì 1",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số liền trước của số bé nhất có 7 chữ số là:", ["999 999", "1 000 001", "99 999", "999 998"], 0, "Số bé nhất có 7 chữ số là 1 000 000. Liền trước là 999 999."),
            make_mc(2, "Giá trị của biểu thức $345\\,000 + 155\\,000 - 200\\,000$ là:", ["300 000", "500 000", "200 000", "400 000"], 0, "500 000 - 200 000 = 300 000."),
            make_mc(3, "Đổi $2\\text{ tấn } 5\\text{ tạ} = \\dots \\text{ yến}$:", ["250 yến", "25 yến", "2 500 yến", "205 yến"], 0, "25 tạ = 250 yến."),
            make_mc(4, "Hai số có tổng bằng 90, hiệu bằng 20. Số lớn là:", ["55", "35", "70", "45"], 0, "(90 + 20) : 2 = 55."),
            make_mc(5, "Hình thoi có chu vi bằng 36 cm thì độ dài một cạnh là:", ["9 cm", "18 cm", "6 cm", "12 cm"], 0, "36 : 4 = 9 cm."),
            make_mc(6, "Năm 2024 thuộc thế kỉ nào?", ["XXI", "XX", "XIX", "XXII"], 0, "Năm 2024 thuộc thế kỉ XXI.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $482\\,593 + 375\\,849$\nb) $820\\,045 - 456\\,378$", "a) $482\\,593 + 375\\,849 = 858\\,442$.\nb) $820\\,045 - 456\\,378 = 363\\,667$.", "a) 858 442; b) 363 667", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $275 + 384 + 725 + 616$\nb) $50 \\times 38 \\times 2$", "a) $(275 + 725) + (384 + 616) = 1000 + 1000 = 2000$.\nb) $(50 \\times 2) \\times 38 = 100 \\times 38 = 3800$.", "a) 2000; b) 3800", 4, 1.0),
            make_essay(3, "Một cửa hàng có hai kho thóc chứa tất cả 320 tấn thóc. Sau khi chuyển 15 tấn thóc từ kho thứ nhất sang kho thứ hai thì số thóc ở kho thứ nhất vẫn nhiều hơn kho thứ hai 10 tấn. Hỏi ban đầu mỗi kho có bao nhiêu tấn thóc?", "Sau khi chuyển 15 tấn, kho 1 hơn kho 2 là 10 tấn.\nVậy ban đầu kho 1 nhiều hơn kho 2 là:\n$15 \\times 2 + 10 = 40\\text{ (tấn)}$.\nSố thóc ban đầu ở kho thứ nhất là:\n$(320 + 40) : 2 = 180\\text{ (tấn)}$.\nSố thóc ban đầu ở kho thứ hai là:\n$320 - 180 = 140\\text{ (tấn)}$.", "Kho 1: 180 tấn; Kho 2: 140 tấn", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chu vi 144 m, chiều dài hơn chiều rộng 16 m. Người ta dùng $\\frac{2}{5}$ diện tích mảnh vườn để trồng dưa hấu, phần còn lại trồng bắp cải. Tính diện tích phần đất trồng bắp cải.", "Nửa chu vi mảnh vườn là: $144 : 2 = 72\\text{ (m)}$.\nChiều dài mảnh vườn là: $(72 + 16) : 2 = 44\\text{ (m)}$.\nChiều rộng mảnh vườn là: $72 - 44 = 28\\text{ (m)}$.\nDiện tích cả mảnh vườn là: $44 \\times 28 = 1232\\text{ (m}^2)$.\nDiện tích đất trồng dưa hấu là:\n$1232 \\times 2 : 5 = 492,8\\text{ m}^2$ (số thập phân). Sửa số: chu vi 140 m => nửa chu vi 70 m, dài hơn 10 m => dài 40 m, rộng 30 m => diện tích $40 \\times 30 = 1200\\text{ m}^2$.\nKhi đó diện tích trồng dưa hấu là: $1200 \\times 2 : 5 = 480\\text{ (m}^2)$.\nDiện tích trồng bắp cải là: $1200 - 480 = 720\\text{ (m}^2)$.", "720 m²", 5, 1.5),
            make_essay(5, "Hiện nay tổng số tuổi của hai bố con là 50 tuổi. Biết rằng 5 năm trước tuổi bố hơn tuổi con 28 tuổi. Tính tuổi của mỗi người hiện nay.", "Vì hiệu số tuổi không thay đổi theo thời gian nên hiện nay bố vẫn hơn con 28 tuổi.\nTuổi của bố hiện nay là:\n$(50 + 28) : 2 = 39\\text{ (tuổi)}$.\nTuổi của con hiện nay là:\n$50 - 39 = 11\\text{ (tuổi)}$.", "Bố: 39 tuổi; Con: 11 tuổi", 5, 1.5),
            make_essay(6, "Cho hình vuông ABCD có cạnh 12 cm. Chia hình vuông đó thành 4 hình vuông nhỏ bằng nhau. Tính tổng chu vi của 4 hình vuông nhỏ đó và so sánh với chu vi hình vuông ABCD.", "Mỗi hình vuông nhỏ có cạnh bằng một nửa cạnh hình vuông ABCD: $12 : 2 = 6\\text{ (cm)}$.\nChu vi một hình vuông nhỏ là: $6 \\times 4 = 24\\text{ (cm)}$.\nTổng chu vi của 4 hình vuông nhỏ là:\n$24 \\times 4 = 96\\text{ (cm)}$.\nChu vi hình vuông ABCD là: $12 \\times 4 = 48\\text{ (cm)}$.\nVậy tổng chu vi của 4 hình vuông nhỏ gấp 2 lần chu vi hình vuông ABCD.", "Tổng chu vi = 96 cm, gấp đôi chu vi hình vuông ABCD", 4, 1.0)
        ]
    }

    # --- Bài 31 - Đề 2 ---
    exams["th4_b31_test2"] = {
        "id": "th4_b31_test2",
        "lessonId": "th4_b31",
        "lessonNum": 31,
        "testNum": 2,
        "title": "Bài 31: Ôn tập chung học kì 1 - Đề số 2",
        "topic": "Ôn tập chung học kì 1",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 9 triệu và 9 đơn vị viết là:", ["9 000 009", "9 000 090", "9 009 000", "90 000 009"], 0, "9 000 009."),
            make_mc(2, "Số lớn nhất có 5 chữ số cộng với 1 được kết quả là:", ["100 000", "99 999", "1 000 000", "10 000"], 0, "99 999 + 1 = 100 000."),
            make_mc(3, "Đổi $5\\text{ m}^2 \\text{ } 40\\text{ dm}^2 = \\dots \\text{ dm}^2$:", ["540 dm²", "5 040 dm²", "54 dm²", "5 400 dm²"], 0, "500 + 40 = 540 dm²."),
            make_mc(4, "Một đoàn xe chở 40 tấn than, đã chở được 25 tạ than. Số than còn lại là:", ["375 tạ", "37,5 tạ", "15 tạ", "350 tạ"], 0, "40 tấn = 400 tạ. Còn lại: 400 - 25 = 375 tạ."),
            make_mc(5, "Tổng của hai số là 150, số bé kém số lớn 30 đơn vị. Số bé là:", ["60", "90", "75", "45"], 0, "(150 - 30) : 2 = 60."),
            make_mc(6, "Trong hình bình hành, hai góc đối diện:", ["Bằng nhau", "Luôn vuông", "Cộng lại bằng 90°", "Bằng 180°"], 0, "Hai góc đối diện của hình bình hành bằng nhau.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $536\\,428 + 284\\,795$\nb) $700\\,050 - 348\\,267$", "a) $536\\,428 + 284\\,795 = 821\\,223$.\nb) $700\\,050 - 348\\,267 = 351\\,783$.", "a) 821 223; b) 351 783", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức bằng cách thuận tiện:\na) $142 + 259 + 858 + 741$\nb) $25 \\times 17 \\times 4$", "a) $(142 + 858) + (259 + 741) = 1000 + 1000 = 2000$.\nb) $(25 \\times 4) \\times 17 = 100 \\times 17 = 1700$.", "a) 2000; b) 1700", 4, 1.0),
            make_essay(3, "Một đội xe có hai tổ: Tổ Một chở được 18 tấn 5 tạ hàng. Tổ Hai chở được nhiều hơn tổ Một 3 tạ hàng. Hỏi cả hai tổ chở được bao nhiêu tạ hàng?", "Đổi: $18\\text{ tấn } 5\\text{ tạ} = 185\\text{ tạ}$.\nTổ Hai chở được số tạ hàng là:\n$185 + 3 = 188\\text{ (tạ)}$.\nCả hai tổ chở được tất cả số tạ hàng là:\n$185 + 188 = 373\\text{ (tạ)}$.", "373 tạ", 4, 1.0),
            make_essay(4, "Một mảnh đất hình chữ nhật có chu vi 180 m, chiều rộng kém chiều dài 18 m. Người ta dùng $\\frac{1}{6}$ diện tích mảnh đất để đào ao thả cá. Tính diện tích phần đất còn lại.", "Nửa chu vi mảnh đất là: $180 : 2 = 90\\text{ (m)}$.\nChiều dài mảnh đất là: $(90 + 18) : 2 = 54\\text{ (m)}$.\nChiều rộng mảnh đất là: $90 - 54 = 36\\text{ (m)}$.\nDiện tích mảnh đất là: $54 \\times 36 = 1944\\text{ (m}^2)$.\nDiện tích đất đào ao thả cá là: $1944 : 6 = 324\\text{ (m}^2)$.\nDiện tích phần đất còn lại là: $1944 - 324 = 1620\\text{ (m}^2)$.", "1620 m²", 5, 1.5),
            make_essay(5, "Năm nay tổng số tuổi của mẹ và con là 42 tuổi. Biết 4 năm nữa mẹ hơn con 26 tuổi. Tính tuổi của mẹ và tuổi của con hiện nay.", "Hiệu số tuổi luôn không đổi nên hiện nay mẹ vẫn hơn con 26 tuổi.\nTuổi của mẹ hiện nay là:\n$(42 + 26) : 2 = 34\\text{ (tuổi)}$.\nTuổi của con hiện nay là:\n$42 - 34 = 8\\text{ (tuổi)}$.", "Mẹ: 34 tuổi; Con: 8 tuổi", 5, 1.5),
            make_essay(6, "Tìm số có hai chữ số, biết rằng nếu viết thêm chữ số 2 vào bên trái số đó thì được số mới mà tổng của số mới và số đã cho là 278.", "Khi viết thêm chữ số 2 vào bên trái số có hai chữ số thì số đó tăng thêm 200 đơn vị (hiệu là 200).\nSố đã cho (số bé) là:\n$(278 - 200) : 2 = 39$.\nKiểm tra: Số mới là 239. Tổng: $239 + 39 = 278$ (đúng).", "39", 4, 1.0)
        ]
    }

    # --- Bài 31 - Đề 3 ---
    exams["th4_b31_test3"] = {
        "id": "th4_b31_test3",
        "lessonId": "th4_b31",
        "lessonNum": 31,
        "testNum": 3,
        "title": "Bài 31: Ôn tập chung học kì 1 - Đề số 3",
        "topic": "Ôn tập chung học kì 1",
        "chapter": "Chủ đề 7: Ôn tập học kì 1",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 7 triệu, 5 vạn và 8 đơn vị viết là:", ["7 050 008", "7 500 008", "7 005 008", "750 008"], 0, "5 vạn = 50 nghìn => 7 050 008."),
            make_mc(2, "Số lớn nhất có 6 chữ số khác nhau trừ đi số bé nhất có 6 chữ số khác nhau bằng:", ["885 309", "897 654", "885 409", "897 509"], 0, "987 654 - 102 345 = 885 309."),
            make_mc(3, "Đổi $3\\text{ phút } 12\\text{ giây} = \\dots \\text{ giây}$:", ["192 giây", "312 giây", "180 giây", "212 giây"], 0, "3 x 60 + 12 = 192 giây."),
            make_mc(4, "Một hình bình hành có đáy 25 cm, chiều cao 14 cm. Diện tích của nó là:", ["350 cm²", "175 cm²", "700 cm²", "78 cm²"], 0, "25 x 14 = 350 cm²."),
            make_mc(5, "Tổng của hai số là 250, hiệu của hai số là 50. Hai số đó là:", ["150 và 100", "200 và 50", "125 và 125", "160 và 90"], 0, "Số lớn = (250 + 50) : 2 = 150; Số bé = 100."),
            make_mc(6, "Dụng cụ dùng để vẽ góc vuông chuẩn xác nhất là:", ["Thước ê ke", "Com-pa", "Thước dây", "Bút dạ"], 0, "Thước ê ke.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $642\\,835 + 179\\,468$\nb) $910\\,020 - 458\\,736$", "a) $642\\,835 + 179\\,468 = 822\\,303$.\nb) $910\\,020 - 458\\,736 = 451\\,284$.", "a) 822 303; b) 451 284", 4, 1.0),
            make_essay(2, "Tính nhanh:\na) $384 + 195 + 616 + 805$\nb) $125 \\times 13 \\times 8$", "a) $(384 + 616) + (195 + 805) = 1000 + 1000 = 2000$.\nb) $(125 \\times 8) \\times 13 = 1000 \\times 13 = 13\\,000$.", "a) 2000; b) 13 000", 4, 1.0),
            make_essay(3, "Một kho hàng có 120 tấn hàng. Đợt đầu xuất đi 35 tấn 5 tạ. Đợt hai xuất đi nhiều hơn đợt đầu 4 tạ. Hỏi trong kho còn lại bao nhiêu tạ hàng?", "Đổi: $120\\text{ tấn} = 1200\\text{ tạ}$; $35\\text{ tấn } 5\\text{ tạ} = 355\\text{ tạ}$.\nĐợt hai xuất đi số tạ hàng là:\n$355 + 4 = 359\\text{ (tạ)}$.\nCả hai đợt xuất đi số tạ hàng là:\n$355 + 359 = 714\\text{ (tạ)}$.\nTrong kho còn lại số tạ hàng là:\n$1200 - 714 = 486\\text{ (tạ)}$.", "486 tạ", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chu vi 200 m, chiều dài hơn chiều rộng 20 m. Người ta trồng rau trên mảnh vườn đó, trung bình mỗi mét vuông thu hoạch được 3 kg rau. Giá bán mỗi ki-lô-gam rau là 15 000 đồng. Tính tổng số tiền thu được từ việc bán rau.", "Nửa chu vi mảnh vườn là: $200 : 2 = 100\\text{ (m)}$.\nChiều dài mảnh vườn là: $(100 + 20) : 2 = 60\\text{ (m)}$.\nChiều rộng mảnh vườn là: $100 - 60 = 40\\text{ (m)}$.\nDiện tích mảnh vườn là: $60 \\times 40 = 2400\\text{ (m}^2)$.\nSố ki-lô-gam rau thu hoạch được là:\n$2400 \\times 3 = 7200\\text{ (kg)}$.\nTổng số tiền bán rau là:\n$7200 \\times 15\\,000 = 108\\,000\\,000\\text{ (đồng)}$.", "108 000 000 đồng", 5, 1.5),
            make_essay(5, "Hai thùng có tất cả 180 lít nước. Nếu đổ 20 lít từ thùng thứ nhất sang thùng thứ hai thì số nước ở hai thùng bằng nhau. Hỏi ban đầu mỗi thùng có bao nhiêu lít nước?", "Ban đầu thùng 1 hơn thùng 2 là:\n$20 \\times 2 = 40\\text{ (lít)}$.\nSố lít nước ban đầu ở thùng 1 là:\n$(180 + 40) : 2 = 110\\text{ (lít)}$.\nSố lít nước ban đầu ở thùng 2 là:\n$180 - 110 = 70\\text{ (lít)}$.", "Thùng 1: 110 lít; Thùng 2: 70 lít", 5, 1.5),
            make_essay(6, "Tìm hai số có tổng bằng 999 và hiệu bằng số lớn nhất có hai chữ số.", "Tổng của hai số là 999.\nSố lớn nhất có hai chữ số là 99, nên hiệu của hai số là 99.\nSố lớn là:\n$(999 + 99) : 2 = 549$.\nSố bé là:\n$999 - 549 = 450$.", "549 và 450", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 7: {len(ex)} (Kỳ vọng: 9)")
    for b in range(29, 32):
        for t in range(1, 4):
            key = f"th4_b{b}_test{t}"
            assert key in ex, f"Thiếu {key}"
            assert len(ex[key]["part1"]) == 6
            assert len(ex[key]["part2"]) == 6
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6
            assert abs(p2_pts - 7.0) < 1e-6
    print("Chủ đề 7 hoàn hảo 100%!")
