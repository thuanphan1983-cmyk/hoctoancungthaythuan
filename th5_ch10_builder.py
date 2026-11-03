# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 10: MỘT SỐ YẾU TỐ THỐNG KÊ VÀ XÁC SUẤT (BÀI 53 ĐẾN BÀI 55)
Toán lớp 5 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 3 bài học x 3 đề độc lập = 9 đề thi (th5_b53_test1 -> th5_b55_test3)
Xuất hàm get_exams() trả về dictionary của 9 đề thi.
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

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 53: BIỂU ĐỒ HÌNH QUẠT TRÒN
    # =========================================================================
    # --- Bài 53 - Đề 1 ---
    exams["th5_b53_test1"] = {
        "id": "th5_b53_test1",
        "lessonId": "th5_b53",
        "lessonNum": 53,
        "testNum": 1,
        "title": "Bài 53: Biểu đồ hình quạt tròn - Đề số 1",
        "topic": "Biểu đồ hình quạt tròn",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tổng số phần trăm của tất cả các hình quạt trong một biểu đồ hình quạt tròn luôn bằng:", ["50%", "100%", "200%", "360%"], 1, "Toàn bộ hình tròn biểu thị 100% dữ liệu thống kê."),
            make_mc(2, "Một biểu đồ hình quạt tròn biểu thị tỉ lệ học sinh tham gia các môn thể thao: Bóng đá 40%, Cầu lông 25%, Bơi lội 20%, còn lại là Bóng rổ. Tỉ lệ học sinh tham gia môn Bóng rổ là:", ["15%", "10%", "20%", "25%"], 0, "100% - (40% + 25% + 20%) = 15%."),
            make_mc(3, "Một trường học có 400 học sinh. Biểu đồ hình quạt cho biết số học sinh giỏi chiếm 30%. Số học sinh giỏi của trường đó là:", ["120 học sinh", "100 học sinh", "150 học sinh", "80 học sinh"], 0, "400 x 30 : 100 = 120 học sinh."),
            make_mc(4, "Biểu đồ hình quạt tròn chia làm 4 phần bằng nhau. Mỗi phần biểu thị bao nhiêu phần trăm?", ["25%", "20%", "50%", "10%"], 0, "100% : 4 = 25%."),
            make_mc(5, "Một khu vườn trồng cây ăn quả gồm: 50% cây xoài, 30% cây cam và 20% cây bưởi. Loại cây nào được trồng nhiều nhất?", ["Cây xoài", "Cây cam", "Cây bưởi", "Ba loại bằng nhau"], 0, "Cây xoài chiếm tỉ lệ lớn nhất là 50%."),
            make_mc(6, "Một cửa hàng bán được 200 chiếc áo trong một tuần. Trong đó biểu đồ cho biết số áo sơ mi chiếm 45%. Số áo sơ mi bán được là:", ["90 chiếc", "80 chiếc", "100 chiếc", "45 chiếc"], 0, "200 x 45 : 100 = 90 chiếc.")
        ],
        "part2": [
            make_essay(1, "Biểu đồ hình quạt tròn biểu thị sự yêu thích các môn học của 120 học sinh khối 5: môn Toán 35%, môn Tiếng Việt 30%, môn Tiếng Anh 25%, môn Khoa học 10%. Tính số học sinh yêu thích môn Toán và môn Khoa học.", "Số học sinh thích môn Toán là: $120 \\times 35 : 100 = 42$ (học sinh).\nSố học sinh thích môn Khoa học là: $120 \\times 10 : 100 = 12$ (học sinh).", "Toán: 42 học sinh; Khoa học: 12 học sinh", 4, 1.0),
            make_essay(2, "Một trang trại nuôi 500 con gia súc gia cầm, trong đó gà chiếm 50%, vịt chiếm 30%, còn lại là ngan. Tính số con ngan trang trại đó nuôi.", "Tỉ lệ phần trăm số con ngan là: $100\\% - (50\\% + 30\\%) = 20\\%$.\nSố con ngan trang trại nuôi là: $500 \\times 20 : 100 = 100$ (con).", "100 con ngan", 4, 1.0),
            make_essay(3, "Một thư viện trường học có 2 000 cuốn sách gồm: sách giáo khoa 45%, truyện tranh 30%, sách tham khảo 20%, còn lại là báo và tạp chí. Hỏi thư viện có bao nhiêu cuốn truyện tranh và bao nhiêu cuốn báo, tạp chí?", "Số cuốn truyện tranh là: $2 000 \\times 30 : 100 = 600$ (cuốn).\nTỉ lệ phần trăm báo và tạp chí là: $100\\% - (45\\% + 30\\% + 20\\%) = 5\\%$.\nSố cuốn báo và tạp chí là: $2 000 \\times 5 : 100 = 100$ (cuốn).", "Truyện tranh: 600 cuốn; Báo, tạp chí: 100 cuốn", 4, 1.0),
            make_essay(4, "Biểu đồ hình quạt tròn về cơ cấu chi tiêu trong tháng của một gia đình: Tiền ăn uống chiếm 40%, tiền học tập của con chiếm 25%, tiền sinh hoạt phí chiếm 15%, còn lại là tiền tiết kiệm. Biết tổng thu nhập cả gia đình trong tháng là 24 000 000 đồng. Tính số tiền gia đình đó tiết kiệm được trong tháng.", "Tỉ lệ phần trăm số tiền tiết kiệm là:\n$100\\% - (40\\% + 25\\% + 15\\%) = 20\\%$.\nSố tiền gia đình tiết kiệm được là:\n$24 000 000 \\times 20 : 100 = 4 800 000$ (đồng).", "4 800 000 đồng", 5, 1.5),
            make_essay(5, "Một cửa hàng hoa quả nhập về 240 kg hoa quả các loại. Biểu đồ hình quạt tròn cho biết: Xoài chiếm 35%, Cam chiếm 30%, Táo chiếm 25%, Dưa hấu chiếm 10%. Hỏi khối lượng Xoài nhiều hơn khối lượng Dưa hấu là bao nhiêu ki-lô-gam?", "Khối lượng Xoài nhập về là: $240 \\times 35 : 100 = 84\\text{ (kg)}$.\nKhối lượng Dưa hấu nhập về là: $240 \\times 10 : 100 = 24\\text{ (kg)}$.\nKhối lượng Xoài nhiều hơn Dưa hấu là:\n$84 - 24 = 60\\text{ (kg)}$.\n(Cách khác: Xoài hơn Dưa hấu $35\\% - 10\\% = 25\\%$. $240 \\times 25 : 100 = 60\\text{ kg}$).", "60 kg", 5, 1.5),
            make_essay(6, "Biểu đồ hình quạt tròn biểu thị kết quả học tập cuối năm của khối 5 có 4 mức: Xuất sắc, Tốt, Đạt, Cần cố gắng. Biết số học sinh Xuất sắc chiếm 32%, Tốt chiếm 48%, Đạt chiếm 15% và có 10 học sinh Cần cố gắng. Hỏi cả khối 5 có tất cả bao nhiêu học sinh?", "Tỉ lệ phần trăm học sinh Cần cố gắng là:\n$100\\% - (32\\% + 48\\% + 15\\%) = 5\\%$.\nVì 5% tương ứng với 10 học sinh nên tổng số học sinh của cả khối 5 là:\n$10 : 5 \\times 100 = 200$ (học sinh).", "200 học sinh", 4, 1.0)
        ]
    }

    # --- Bài 53 - Đề 2 ---
    exams["th5_b53_test2"] = {
        "id": "th5_b53_test2",
        "lessonId": "th5_b53",
        "lessonNum": 53,
        "testNum": 2,
        "title": "Bài 53: Biểu đồ hình quạt tròn - Đề số 2",
        "topic": "Biểu đồ hình quạt tròn",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một nửa hình tròn trong biểu đồ quạt tròn biểu thị tỉ lệ phần trăm là:", ["25%", "50%", "75%", "100%"], 1, "Một nửa hình tròn tương ứng với 50%."),
            make_mc(2, "Kết quả điều tra về phương tiện đến trường của 300 học sinh: Đi bộ chiếm 20%, Xe đạp chiếm 50%, Bố mẹ đưa đón chiếm 30%. Số học sinh đi xe đạp là:", ["150 học sinh", "60 học sinh", "90 học sinh", "100 học sinh"], 0, "300 x 50 : 100 = 150 học sinh."),
            make_mc(3, "Một mảnh đất có diện tích 500 m$^2$. Biểu đồ cho biết diện tích xây nhà chiếm 35%, diện tích sân vườn chiếm 65%. Diện tích xây nhà là:", ["175 m$^2$", "150 m$^2$", "200 m$^2$", "225 m$^2$"], 0, "500 x 35 : 100 = 175 m$^2$."),
            make_mc(4, "Biểu đồ quạt tròn biểu thị cơ cấu xuất khẩu: Nông sản 45%, Thủy sản 35%, Khoáng sản 20%. Tỉ lệ thủy sản ít hơn nông sản là:", ["10%", "5%", "15%", "20%"], 0, "45% - 35% = 10%."),
            make_mc(5, "Số học sinh của một lớp là 40 em. Biểu đồ quạt cho biết tỉ lệ học sinh thích màu xanh là 25%. Số học sinh thích màu xanh là:", ["10 em", "8 em", "12 em", "15 em"], 0, "40 x 25 : 100 = 10 em."),
            make_mc(6, "Trên biểu đồ quạt tròn có 3 quạt: quạt A là 45%, quạt B là 30%. Quạt C chiếm bao nhiêu phần trăm?", ["25%", "15%", "35%", "20%"], 0, "100% - (45% + 30%) = 25%.")
        ],
        "part2": [
            make_essay(1, "Một trang trại có diện tích $12\\text{ ha}$. Biểu đồ quạt tròn cho biết: diện tích trồng lúa chiếm 50%, diện tích trồng rau chiếm 25%, diện tích ao cá chiếm 15%, còn lại là đường đi. Tính diện tích ao cá theo đơn vị héc-ta.", "Diện tích ao cá của trang trại là:\n$12 \\times 15 : 100 = 1,8\\text{ (ha)}$.", "1,8 ha", 4, 1.0),
            make_essay(2, "Một lớp học có 36 học sinh. Biểu đồ quạt cho biết: học sinh Giỏi chiếm 25%, học sinh Khá chiếm 50%, còn lại là học sinh Trung bình. Tính số học sinh Khá và số học sinh Trung bình của lớp đó.", "Số học sinh Khá là: $36 \\times 50 : 100 = 18$ (học sinh).\nTỉ lệ học sinh Trung bình là: $100\\% - (25\\% + 50\\%) = 25\\%$.\nSố học sinh Trung bình là: $36 \\times 25 : 100 = 9$ (học sinh).", "Khá: 18 học sinh; Trung bình: 9 học sinh", 4, 1.0),
            make_essay(3, "Một cửa hàng điện máy bán được 80 chiếc ti vi trong một tháng gồm: Samsung 40%, Sony 35%, LG 25%. Hỏi cửa hàng đã bán được bao nhiêu chiếc ti vi mỗi loại?", "Số ti vi Samsung bán được: $80 \\times 40 : 100 = 32$ (chiếc).\nSố ti vi Sony bán được: $80 \\times 35 : 100 = 28$ (chiếc).\nSố ti vi LG bán được: $80 \\times 25 : 100 = 20$ (chiếc).", "Samsung: 32 chiếc; Sony: 28 chiếc; LG: 20 chiếc", 4, 1.0),
            make_essay(4, "Biểu đồ hình quạt tròn cho biết tỉ lệ phần trăm các loại cây ăn quả trong một trang trại: Cây bưởi 35%, cây xoài 30%, cây nhãn 20%, cây mít 15%. Biết trang trại có tất cả 600 cây ăn quả. Hỏi số cây bưởi nhiều hơn số cây mít bao nhiêu cây?", "Số cây bưởi trong trang trại là: $600 \\times 35 : 100 = 210$ (cây).\nSố cây mít trong trang trại là: $600 \\times 15 : 100 = 90$ (cây).\nSố cây bưởi nhiều hơn số cây mít là:\n$210 - 90 = 120$ (cây).", "120 cây", 5, 1.5),
            make_essay(5, "Một trường tiểu học quyên góp được 1 500 quyển vở ủng hộ học sinh vùng lũ lụt. Khối 5 quyên góp 30%, Khối 4 quyên góp 26%, Khối 3 quyên góp 20%, Khối 2 quyên góp 14%, còn lại là Khối 1. Tính số quyển vở Khối 1 quyên góp được.", "Tỉ lệ phần trăm số vở Khối 1 quyên góp là:\n$100\\% - (30\\% + 26\\% + 20\\% + 14\\%) = 10\\%$.\nSố vở Khối 1 quyên góp được là:\n$1 500 \\times 10 : 100 = 150$ (quyển vở).", "150 quyển vở", 5, 1.5),
            make_essay(6, "Biểu đồ hình quạt tròn biểu thị thể loại phim yêu thích của 150 bạn học sinh: Hoạt hình 46%, Phiêu lưu 24%, Hài kịch 20%, Khoa học 10%. Tính tổng số bạn thích phim Hoạt hình và Phiêu lưu.", "Tỉ lệ số bạn thích phim Hoạt hình và Phiêu lưu là:\n$46\\% + 24\\% = 70\\%$.\nTổng số bạn thích hai thể loại phim này là:\n$150 \\times 70 : 100 = 105$ (bạn học sinh).", "105 bạn học sinh", 4, 1.0)
        ]
    }

    # --- Bài 53 - Đề 3 ---
    exams["th5_b53_test3"] = {
        "id": "th5_b53_test3",
        "lessonId": "th5_b53",
        "lessonNum": 53,
        "testNum": 3,
        "title": "Bài 53: Biểu đồ hình quạt tròn - Đề số 3",
        "topic": "Biểu đồ hình quạt tròn",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình quạt tròn có góc ở tâm là $90^\\circ$ (góc vuông) biểu thị tỉ lệ là:", ["25%", "50%", "75%", "20%"], 0, "90/360 = 1/4 = 25%."),
            make_mc(2, "Một đội tình nguyện có 80 người. Biểu đồ quạt cho biết số nữ chiếm 60%. Số nam trong đội tình nguyện là:", ["32 người", "48 người", "40 người", "30 người"], 0, "Tỉ lệ nam: 100% - 60% = 40%. Số nam: 80 x 40 : 100 = 32 người."),
            make_mc(3, "Một khu rừng có 1 200 cây gỗ, trong đó cây thông chiếm 45%, cây keo chiếm 35%, còn lại là cây bạch đàn. Tỉ lệ cây bạch đàn là:", ["20%", "25%", "15%", "30%"], 0, "100% - (45% + 35%) = 20%."),
            make_mc(4, "Biểu đồ quạt tròn biểu thị tỉ lệ tiết kiệm tiền của Nam: Mua sách 30%, Tiết kiệm 40%, Tiêu vặt 30%. Nếu Nam có 200 000 đồng thì số tiền mua sách là:", ["60 000 đồng", "80 000 đồng", "70 000 đồng", "50 000 đồng"], 0, "200 000 x 30 : 100 = 60 000 đồng."),
            make_mc(5, "Biểu đồ hình quạt tròn thường được dùng để:", [
                "Biểu thị cơ cấu tỉ lệ phần trăm của các thành phần trong toàn bộ dữ liệu",
                "Biểu thị sự biến động của một đại lượng theo thời gian",
                "Đo lường độ dài quãng đường",
                "Vẽ hình học không gian"
            ], 0, "Biểu đồ hình quạt tròn dùng để so sánh các phần với toàn thể dưới dạng tỉ lệ phần trăm."),
            make_mc(6, "Một vườn thú có 150 con thú. Trong đó biểu đồ cho biết số thú ăn cỏ chiếm 70%. Số thú ăn cỏ là:", ["105 con", "100 con", "110 con", "95 con"], 0, "150 x 70 : 100 = 105 con.")
        ],
        "part2": [
            make_essay(1, "Một xí nghiệp có 400 công nhân. Biểu đồ hình quạt cho biết: Phân xưởng 1 chiếm 35%, Phân xưởng 2 chiếm 40%, còn lại là Phân xưởng 3. Tính số công nhân của Phân xưởng 3.", "Tỉ lệ phần trăm công nhân Phân xưởng 3 là:\n$100\\% - (35\\% + 40\\%) = 25\\%$.\nSố công nhân Phân xưởng 3 là:\n$400 \\times 25 : 100 = 100$ (công nhân).", "100 công nhân", 4, 1.0),
            make_essay(2, "Một trang trại thu hoạch được 5 tấn nông sản gồm: Ngô 40%, Khoai tây 35%, Sắn 25%. Tính khối lượng mỗi loại nông sản thu hoạch được theo đơn vị tấn.", "Khối lượng Ngô: $5 \\times 40 : 100 = 2\\text{ (tấn)}$.\nKhối lượng Khoai tây: $5 \\times 35 : 100 = 1,75\\text{ (tấn)}$.\nKhối lượng Sắn: $5 \\times 25 : 100 = 1,25\\text{ (tấn)}$.", "Ngô: 2 tấn; Khoai tây: 1,75 tấn; Sắn: 1,25 tấn", 4, 1.0),
            make_essay(3, "Một cuộc khảo sát 250 người về đồ uống yêu thích: Nước khoáng 40%, Nước ép trái cây 32%, Trà sữa 20%, Cà phê 8%. Hỏi có bao nhiêu người thích Nước ép trái cây?", "Số người thích nước ép trái cây là:\n$250 \\times 32 : 100 = 80$ (người).", "80 người", 4, 1.0),
            make_essay(4, "Biểu đồ hình quạt tròn thể hiện việc phân bổ thời gian trong ngày (24 giờ) của bạn Minh: Ngủ chiếm 37,5%, Học tập chiếm 33,3% (khoảng 8 giờ), Vui chơi chiếm 12,5%, Ăn uống và vệ sinh chiếm 16,7% (khoảng 4 giờ). Hãy tính chính xác số giờ bạn Minh dành cho việc Ngủ và việc Vui chơi.", "Số giờ dành cho việc Ngủ là: $24 \\times 37,5 : 100 = 9\\text{ (giờ)}$.\nSố giờ dành cho việc Vui chơi là: $24 \\times 12,5 : 100 = 3\\text{ (giờ)}$.", "Ngủ: 9 giờ; Vui chơi: 3 giờ", 5, 1.5),
            make_essay(5, "Biểu đồ hình quạt tròn biểu thị tỉ lệ huy chương của một đoàn thể thao tại SEA Games: Huy chương Vàng chiếm 45%, Huy chương Bạc chiếm 30%, còn lại là Huy chương Đồng. Biết đoàn thể thao đạt được 36 Huy chương Bạc. Hỏi đoàn thể thao đó đạt được tất cả bao nhiêu huy chương các loại?", "Vì 30% tổng số huy chương là 36 chiếc, nên tổng số huy chương đoàn đạt được là:\n$36 : 30 \\times 100 = 120$ (huy chương).", "120 huy chương", 5, 1.5),
            make_essay(6, "Một mảnh vườn hình chữ nhật có diện tích $800\\text{ m}^2$. Người ta dùng $45\\%$ diện tích để trồng hoa hồng, $30\\%$ để trồng hoa cúc, phần còn lại trồng cây cảnh. Tính diện tích đất trồng cây cảnh.", "Tỉ lệ phần trăm đất trồng cây cảnh là: $100\\% - (45\\% + 30\\%) = 25\\%$.\nDiện tích đất trồng cây cảnh là: $800 \\times 25 : 100 = 200\\text{ (m$^2$)}$.", "200 m$^2$", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 54: TỈ SỐ MÔ TẢ SỐ LẦN LẶP LẠI CỦA MỘT KHẢ NĂNG XẢY RA
    # =========================================================================
    # --- Bài 54 - Đề 1 ---
    exams["th5_b54_test1"] = {
        "id": "th5_b54_test1",
        "lessonId": "th5_b54",
        "lessonNum": 54,
        "testNum": 1,
        "title": "Bài 54: Tỉ số mô tả số lần lặp lại của một khả năng xảy ra - Đề số 1",
        "topic": "Tỉ số mô tả số lần lặp lại của một khả năng xảy ra",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Gieo một con xúc xắc 20 lần, thấy có 4 lần xuất hiện mặt 6 chấm. Tỉ số mô tả số lần lặp lại của khả năng xuất hiện mặt 6 chấm là:", ["$\\frac{4}{20}$", "$\\frac{1}{6}$", "$\\frac{16}{20}$", "$\\frac{6}{20}$"], 0, "Tỉ số = số lần xuất hiện / tổng số lần gieo = 4/20 = 1/5."),
            make_mc(2, "Tung một đồng xu 50 lần, có 27 lần xuất hiện mặt ngửa (N). Số lần xuất hiện mặt sấp (S) là:", ["23 lần", "25 lần", "27 lần", "50 lần"], 0, "50 - 27 = 23 lần."),
            make_mc(3, "Quay một vòng quay may mắn 30 lần, kim dừng lại ở ô may mắn 9 lần. Tỉ số giữa số lần xuất hiện ô may mắn và tổng số lần quay rút gọn là:", ["$\\frac{3}{10}$", "$\\frac{9}{30}$", "$\\frac{1}{3}$", "$\\frac{3}{5}$"], 0, "9/30 = 3/10."),
            make_mc(4, "Một hộp có 10 viên bi đỏ và 10 viên bi xanh. Không nhìn vào hộp, lấy ngẫu nhiên 1 viên bi. Khả năng lấy được viên bi màu đỏ là:", ["Chắc chắn", "Có thể", "Không thể", "Không xác định"], 1, "Vì trong hộp có cả bi đỏ và bi xanh nên việc lấy được bi đỏ là sự kiện có thể xảy ra."),
            make_mc(5, "Bạn An ném bóng vào rổ 25 lần, ném trúng đích 15 lần. Tỉ số ném trúng đích viết dưới dạng số thập phân là:", ["0,6", "0,15", "0,25", "0,4"], 0, "15/25 = 3/5 = 0,6."),
            make_mc(6, "Gieo đồng xu 100 lần, thấy mặt S xuất hiện 48 lần. Tỉ số phần trăm số lần xuất hiện mặt S là:", ["48%", "52%", "50%", "24%"], 0, "48/100 = 48%.")
        ],
        "part2": [
            make_essay(1, "Bạn Bình gieo một con xúc xắc 40 lần và ghi lại số lần xuất hiện mặt 5 chấm là 8 lần. Hãy viết tỉ số mô tả số lần xuất hiện mặt 5 chấm so với tổng số lần gieo dưới dạng phân số tối giản và số thập phân.", "Tỉ số mô tả số lần xuất hiện mặt 5 chấm là: $\\frac{8}{40}$.\nRút gọn về phân số tối giản: $\\frac{8 : 8}{40 : 8} = \\frac{1}{5}$.\nViết dưới dạng số thập phân: $\\frac{1}{5} = 0,2$.", "Phân số tối giản: 1/5; Số thập phân: 0,2", 4, 1.0),
            make_essay(2, "Trong một hộp có 5 viên bi xanh, 5 viên bi đỏ và 5 viên bi vàng có kích thước giống nhau. Bạn Nam lấy ngẫu nhiên một viên bi, ghi lại màu rồi trả lại hộp. Sau 50 lần thực hiện, bạn Nam lấy được 18 lần bi xanh, 17 lần bi đỏ, còn lại là bi vàng.\na) Tính số lần bạn Nam lấy được bi vàng.\nb) Viết tỉ số mô tả số lần lấy được bi vàng so với tổng số lần thực nghiệm.", "a) Số lần lấy được viên bi vàng là: $50 - (18 + 17) = 15$ (lần).\nb) Tỉ số mô tả số lần lấy được bi vàng là: $\\frac{15}{50} = \\frac{3}{10}$ (hoặc 0,3).", "a) 15 lần; b) 3/10 (hay 0,3)", 4, 1.0),
            make_essay(3, "Một thủ môn bắt phạt đền 20 lần và cản phá thành công 6 quả phạt đền. Tính tỉ số phần trăm số lần cản phá thành công của thủ môn đó.", "Tỉ số mô tả số lần cản phá thành công là: $\\frac{6}{20}$.\nĐổi sang tỉ số phần trăm: $\\frac{6}{20} = \\frac{30}{100} = 30\\%$.", "30%", 4, 1.0),
            make_essay(4, "Một người thực hiện bắn bia 50 phát, kết quả ghi nhận như sau:\n- Bắn trúng hồng tâm (10 điểm): 15 lần\n- Bắn trúng vòng 9 điểm: 20 lần\n- Bắn trúng vòng 8 điểm: 10 lần\n- Bắn trượt (dưới 8 điểm): 5 lần\nTính tỉ số mô tả số lần bắn đạt từ 9 điểm trở lên so với tổng số phát bắn.", "Số lần bắn đạt từ 9 điểm trở lên là:\n$15 + 20 = 35$ (lần).\nTỉ số so với tổng số phát bắn là:\n$\\frac{35}{50} = \\frac{7}{10} = 0,7$ (hay $70\\%$).", "7/10 (hoặc 70%)", 5, 1.5),
            make_essay(5, "Tung một đồng xu 60 lần, ghi nhận được mặt S xuất hiện 33 lần.\na) Tính số lần xuất hiện mặt N (mặt ngửa).\nb) Viết tỉ số mô tả khả năng xuất hiện mặt N so với tổng số lần tung dưới dạng phân số tối giản.", "a) Số lần xuất hiện mặt N là: $60 - 33 = 27$ (lần).\nb) Tỉ số mô tả khả năng xuất hiện mặt N là:\n$\\frac{27}{60} = \\frac{27 : 3}{60 : 3} = \\frac{9}{20}$.", "a) 27 lần; b) 9/20", 5, 1.5),
            make_essay(6, "Trong một cuộc thi trắc nghiệm gồm 40 câu hỏi, bạn Linh trả lời đúng 34 câu. Viết tỉ số mô tả số câu trả lời đúng so với tổng số câu hỏi dưới dạng phân số tối giản, số thập phân và tỉ số phần trăm.", "Tỉ số câu trả lời đúng là: $\\frac{34}{40}$.\n- Phân số tối giản: $\\frac{17}{20}$.\n- Số thập phân: $\\frac{17}{20} = 0,85$.\n- Tỉ số phần trăm: $85\\%$.", "17/20; 0,85; 85%", 4, 1.0)
        ]
    }

    # --- Bài 54 - Đề 2 ---
    exams["th5_b54_test2"] = {
        "id": "th5_b54_test2",
        "lessonId": "th5_b54",
        "lessonNum": 54,
        "testNum": 2,
        "title": "Bài 54: Tỉ số mô tả số lần lặp lại của một khả năng xảy ra - Đề số 2",
        "topic": "Tỉ số mô tả số lần lặp lại của một khả năng xảy ra",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hộp chỉ đựng toàn bóng bàn màu trắng. Lấy ngẫu nhiên 1 quả bóng ra. Khẳng định nào sau đây là ĐÚNG?", [
                "Chắc chắn lấy được bóng màu trắng",
                "Có thể lấy được bóng màu vàng",
                "Không thể lấy được bóng màu trắng",
                "Chắc chắn lấy được bóng màu đỏ"
            ], 0, "Vì trong hộp chỉ có bóng trắng nên chắc chắn lấy được bóng trắng."),
            make_mc(2, "Gieo con xúc xắc 30 lần, thấy có 5 lần xuất hiện mặt 1 chấm. Tỉ số mô tả số lần xuất hiện mặt 1 chấm là:", ["$\\frac{1}{6}$", "$\\frac{5}{30}$", "$\\frac{1}{5}$", "$\\frac{1}{30}$"], 0, "5/30 = 1/6."),
            make_mc(3, "Tung đồng xu 40 lần, có 22 lần xuất hiện mặt ngửa. Tỉ số xuất hiện mặt ngửa là:", ["$\\frac{11}{20}$", "$\\frac{9}{20}$", "$\\frac{1}{2}$", "$\\frac{22}{100}$"], 0, "22/40 = 11/20."),
            make_mc(4, "Một cung thủ bắn 20 mũi tên, trúng bia 16 mũi tên. Tỉ số phần trăm số mũi tên bắn trúng bia là:", ["80%", "75%", "85%", "70%"], 0, "16/20 = 80/100 = 80%."),
            make_mc(5, "Khi quay bánh xe số may mắn gồm các số từ 1 đến 8, khả năng kim dừng lại ở số 10 là:", ["Không thể", "Có thể", "Chắc chắn", "Tùy ý"], 0, "Trên bánh xe chỉ có số từ 1 đến 8 nên việc dừng ở số 10 là không thể."),
            make_mc(6, "Một học sinh trả lời đúng 18 câu trong bài kiểm tra 20 câu. Tỉ số câu đúng viết dưới dạng số thập phân là:", ["0,9", "0,8", "0,85", "0,95"], 0, "18/20 = 9/10 = 0,9.")
        ],
        "part2": [
            make_essay(1, "Gieo một con xúc xắc 50 lần, người ta ghi lại số lần xuất hiện mặt chẵn (2, 4, 6 chấm) là 28 lần. Hãy tính tỉ số xuất hiện mặt chẵn và viết kết quả dưới dạng số thập phân.", "Tỉ số xuất hiện mặt chẵn là: $\\frac{28}{50}$.\nViết dưới dạng số thập phân: $\\frac{28}{50} = \\frac{56}{100} = 0,56$.", "0,56 (hoặc 14/25)", 4, 1.0),
            make_essay(2, "Một lớp có 30 học sinh làm bài khảo sát môn Tiếng Anh. Có 12 bạn đạt điểm giỏi, 15 bạn đạt điểm khá, còn lại đạt điểm trung bình.\na) Tính số bạn đạt điểm trung bình.\nb) Viết tỉ số phần trăm số học sinh đạt điểm giỏi so với tổng số học sinh cả lớp.", "a) Số bạn đạt điểm trung bình là: $30 - (12 + 15) = 3$ (bạn).\nb) Tỉ số phần trăm học sinh đạt điểm giỏi là:\n$\\frac{12}{30} = \\frac{4}{10} = 40\\%$.", "a) 3 bạn; b) 40%", 4, 1.0),
            make_essay(3, "Tung một đồng xu 80 lần, thấy có 44 lần xuất hiện mặt ngửa.\na) Tính số lần xuất hiện mặt sấp.\nb) Viết tỉ số mô tả số lần xuất hiện mặt sấp so với tổng số lần tung dưới dạng phân số tối giản.", "a) Số lần xuất hiện mặt sấp là: $80 - 44 = 36$ (lần).\nb) Tỉ số mô tả số lần xuất hiện mặt sấp là:\n$\\frac{36}{80} = \\frac{36 : 4}{80 : 4} = \\frac{9}{20}$.", "a) 36 lần; b) 9/20", 4, 1.0),
            make_essay(4, "Một hộp bánh có 4 loại vị: dâu, sô-cô-la, vani và matcha. Một bạn lấy ngẫu nhiên 1 chiếc bánh, ghi lại vị rồi bỏ lại vào hộp. Sau 60 lần lấy bánh, ghi nhận được: 18 lần vị dâu, 21 lần vị sô-cô-la, 12 lần vị vani, còn lại là vị matcha. Tính tỉ số phần trăm số lần lấy được vị matcha.", "Số lần lấy được vị matcha là:\n$60 - (18 + 21 + 12) = 60 - 51 = 9$ (lần).\nTỉ số phần trăm số lần lấy được vị matcha là:\n$\\frac{9}{60} = \\frac{3}{20} = 15\\%$.", "15%", 5, 1.5),
            make_essay(5, "Một cầu thủ bóng rổ thực hiện ném bóng vào rổ 50 lần và ghi được 35 lần ném trúng.\na) Tính tỉ số phần trăm số lần ném trúng của cầu thủ đó.\nb) Nếu cầu thủ đó ném thêm 10 lần và ném trúng cả 10 lần thì tỉ số phần trăm ném trúng lúc này là bao nhiêu?", "a) Tỉ số phần trăm ban đầu là: $\\frac{35}{50} = 70\\%$.\nb) Sau khi ném thêm: tổng số lần ném là $50 + 10 = 60$ lần, số lần trúng là $35 + 10 = 45$ lần.\nTỉ số phần trăm lúc này là: $\\frac{45}{60} = \\frac{3}{4} = 75\\%$.", "a) 70%; b) 75%", 5, 1.5),
            make_essay(6, "Trong một bài kiểm tra có 25 câu hỏi. Bạn Nam làm đúng 21 câu. Hãy viết tỉ số mô tả khả năng làm đúng của bạn Nam dưới dạng phân số tối giản và tỉ số phần trăm.", "Tỉ số câu làm đúng là: $\\frac{21}{25}$.\n- Phân số tối giản: $\\frac{21}{25}$.\n- Tỉ số phần trăm: $\\frac{21 \\times 4}{25 \\times 4} = 84\\%$.", "21/25 (hay 84%)", 4, 1.0)
        ]
    }

    # --- Bài 54 - Đề 3 ---
    exams["th5_b54_test3"] = {
        "id": "th5_b54_test3",
        "lessonId": "th5_b54",
        "lessonNum": 54,
        "testNum": 3,
        "title": "Bài 54: Tỉ số mô tả số lần lặp lại của một khả năng xảy ra - Đề số 3",
        "topic": "Tỉ số mô tả số lần lặp lại của một khả năng xảy ra",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người rút ngẫu nhiên 1 lá bài từ bộ bài gồm 52 lá bài. Khả năng rút được lá bài màu đen là:", ["Có thể", "Chắc chắn", "Không thể", "Không xác định"], 0, "Bộ bài có cả lá bài đen và đỏ nên việc rút được lá đen là có thể."),
            make_mc(2, "Gieo con xúc xắc 60 lần, thấy có 12 lần xuất hiện mặt số chấm chia hết cho 3 (3 hoặc 6 chấm). Tỉ số số lần xuất hiện này là:", ["$\\frac{1}{5}$", "$\\frac{1}{3}$", "$\\frac{1}{6}$", "$\\frac{12}{100}$"], 0, "12/60 = 1/5."),
            make_mc(3, "Tung đồng xu 100 lần, có 53 lần xuất hiện mặt ngửa. Số lần xuất hiện mặt sấp là:", ["47 lần", "53 lần", "50 lần", "45 lần"], 0, "100 - 53 = 47 lần."),
            make_mc(4, "Một xạ thủ bắn 40 phát đạn, có 32 phát trúng mục tiêu. Tỉ số phần trăm bắn trúng mục tiêu là:", ["80%", "75%", "85%", "70%"], 0, "32/40 = 4/5 = 80%."),
            make_mc(5, "Lấy ngẫu nhiên một ngày trong tuần. Khả năng ngày đó là Chủ nhật là:", ["Có thể", "Chắc chắn", "Không thể", "Hiển nhiên"], 0, "Trong tuần có 7 ngày nên có thể ngày đó là Chủ nhật."),
            make_mc(6, "Gieo một con xúc xắc 50 lần, mặt 6 chấm xuất hiện 10 lần. Tỉ số số lần xuất hiện mặt 6 chấm viết dưới dạng số thập phân là:", ["0,2", "0,1", "0,25", "0,5"], 0, "10/50 = 1/5 = 0,2.")
        ],
        "part2": [
            make_essay(1, "Bạn An gieo một đồng xu 50 lần và ghi lại kết quả: có 26 lần xuất hiện mặt S. Viết tỉ số mô tả số lần xuất hiện mặt S dưới dạng phân số tối giản và số thập phân.", "Tỉ số xuất hiện mặt S là: $\\frac{26}{50}$.\n- Phân số tối giản: $\\frac{26 : 2}{50 : 2} = \\frac{13}{25}$.\n- Số thập phân: $\\frac{26}{50} = 0,52$.", "13/25; 0,52", 4, 1.0),
            make_essay(2, "Trong một cuộc thi sút bóng vào khung thành, mỗi bạn được sút 10 lần. Kết quả của bạn Huy: 7 lần bóng vào lưới, 2 lần bóng chạm xà ngang/cột dọc, 1 lần bóng ra ngoài. Tính tỉ số phần trăm số lần bóng vào lưới của bạn Huy.", "Tỉ số phần trăm số lần sút vào lưới là:\n$\\frac{7}{10} = \\frac{70}{100} = 70\\%$.", "70%", 4, 1.0),
            make_essay(3, "Một hộp kín chứa 3 chiếc bút mực xanh, 2 chiếc bút mực đỏ và 5 chiếc bút mực đen. Nam rút ngẫu nhiên 1 chiếc bút, ghi lại màu mực rồi trả lại hộp. Sau 40 lần rút, có 14 lần rút được bút mực đen. Tính tỉ số mô tả khả năng rút được bút mực đen so với tổng số lần rút.", "Tỉ số mô tả khả năng rút được bút mực đen là:\n$\\frac{14}{40} = \\frac{7}{20} = 0,35$ (hay $35\\%$).", "7/20 (hay 0,35)", 4, 1.0),
            make_essay(4, "Một cửa hàng kiểm tra chất lượng của 200 chiếc bóng đèn, phát hiện ra có 6 chiếc bị lỗi (hỏng).\na) Tính tỉ số phần trăm số bóng đèn bị lỗi.\nb) Tính số bóng đèn đạt chuẩn chất lượng và tỉ số phần trăm của số bóng đạt chuẩn.", "a) Tỉ số phần trăm bóng đèn lỗi là: $\\frac{6}{200} = \\frac{3}{100} = 3\\%$.\nb) Số bóng đèn đạt chuẩn là: $200 - 6 = 194$ (chiếc).\nTỉ số phần trăm bóng đèn đạt chuẩn là: $100\\% - 3\\% = 97\\%$.", "a) 3%; b) 194 chiếc (97%)", 5, 1.5),
            make_essay(5, "Bạn Mai quay một vòng quay may mắn có 5 ô bằng nhau đánh số từ 1 đến 5. Mai quay 50 lần và ghi lại số lần kim dừng ở ô số lẻ (1, 3, 5) là 32 lần.\na) Tính số lần kim dừng ở ô số chẵn (2, 4).\nb) Viết tỉ số mô tả khả năng kim dừng ở ô số chẵn so với tổng số lần quay dưới dạng số thập phân.", "a) Số lần kim dừng ở ô số chẵn là: $50 - 32 = 18$ (lần).\nb) Tỉ số mô tả khả năng dừng ở ô số chẵn là:\n$\\frac{18}{50} = \\frac{36}{100} = 0,36$.", "a) 18 lần; b) 0,36", 5, 1.5),
            make_essay(6, "Trong một bài kiểm tra trắc nghiệm 30 câu hỏi, bạn Hoa làm đúng 24 câu. Viết tỉ số mô tả khả năng làm đúng của bạn Hoa dưới dạng phân số tối giản và tỉ số phần trăm.", "Tỉ số câu làm đúng của Hoa là: $\\frac{24}{30}$.\n- Phân số tối giản: $\\frac{24 : 6}{30 : 6} = \\frac{4}{5}$.\n- Tỉ số phần trăm: $\\frac{4}{5} = 80\\%$.", "4/5 (hay 80%)", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 55: LUYỆN TẬP CHUNG CHỦ ĐỀ 10
    # =========================================================================
    # --- Bài 55 - Đề 1 ---
    exams["th5_b55_test1"] = {
        "id": "th5_b55_test1",
        "lessonId": "th5_b55",
        "lessonNum": 55,
        "testNum": 1,
        "title": "Bài 55: Luyện tập chung Chủ đề 10 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 10",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một biểu đồ quạt tròn biểu thị tỉ lệ 400 học sinh: Giỏi 35%, Khá 45%, Trung bình 20%. Số học sinh giỏi là:", ["140 em", "120 em", "150 em", "160 em"], 0, "400 x 35 : 100 = 140 em."),
            make_mc(2, "Tung đồng xu 40 lần, xuất hiện mặt S 18 lần. Tỉ số phần trăm xuất hiện mặt S là:", ["45%", "40%", "50%", "55%"], 0, "18/40 = 9/20 = 45%."),
            make_mc(3, "Gieo con xúc xắc 25 lần, mặt 4 chấm xuất hiện 5 lần. Tỉ số mô tả khả năng xuất hiện mặt 4 chấm là:", ["$\\frac{1}{5}$", "$\\frac{1}{4}$", "$\\frac{5}{20}$", "$\\frac{1}{6}$"], 0, "5/25 = 1/5."),
            make_mc(4, "Biểu đồ quạt tròn có 3 hình quạt: quạt A chiếm 50%, quạt B chiếm 35%. Quạt C chiếm:", ["15%", "20%", "10%", "25%"], 0, "100% - (50% + 35%) = 15%."),
            make_mc(5, "Một xạ thủ bắn 50 phát đạn, trúng 42 phát. Tỉ số bắn trúng là:", ["0,84", "0,42", "0,82", "0,85"], 0, "42/50 = 84/100 = 0,84."),
            make_mc(6, "Trong một hộp kín chỉ có kẹo dâu và kẹo bạc hà. Không nhìn vào hộp, lấy ngẫu nhiên 1 chiếc kẹo. Khả năng lấy được kẹo sô-cô-la là:", ["Không thể", "Có thể", "Chắc chắn", "Tùy ý"], 0, "Hộp không có kẹo sô-cô-la nên sự kiện này không thể xảy ra.")
        ],
        "part2": [
            make_essay(1, "Biểu đồ hình quạt tròn cho biết cơ cấu số học sinh tham gia câu lạc bộ của trường có 500 học sinh: CLB Toán 30%, CLB Tiếng Anh 35%, CLB Âm nhạc 20%, CLB Thể thao 15%. Tính số học sinh tham gia CLB Tiếng Anh và CLB Thể thao.", "Số học sinh tham gia CLB Tiếng Anh: $500 \\times 35 : 100 = 175$ (học sinh).\nSố học sinh tham gia CLB Thể thao: $500 \\times 15 : 100 = 75$ (học sinh).", "Tiếng Anh: 175 học sinh; Thể thao: 75 học sinh", 4, 1.0),
            make_essay(2, "Bạn Minh gieo một con xúc xắc 60 lần và ghi lại số lần xuất hiện mặt số chẵn (2, 4, 6 chấm) là 33 lần.\na) Tính số lần xuất hiện mặt số lẻ (1, 3, 5 chấm).\nb) Viết tỉ số mô tả số lần xuất hiện mặt số lẻ so với tổng số lần gieo dưới dạng phân số tối giản và tỉ số phần trăm.", "a) Số lần xuất hiện mặt số lẻ là: $60 - 33 = 27$ (lần).\nb) Tỉ số mô tả số lần xuất hiện mặt số lẻ là: $\\frac{27}{60} = \\frac{9}{20}$.\nTỉ số phần trăm: $\\frac{9}{20} = 45\\%$.", "a) 27 lần; b) 9/20 (hay 45%)", 4, 1.0),
            make_essay(3, "Một khu vườn rộng $2 400\\text{ m}^2$. Biểu đồ hình quạt tròn cho biết: diện tích trồng hoa chiếm 40%, diện tích trồng rau chiếm 35%, diện tích ao cá chiếm 15%, còn lại là lối đi. Tính diện tích phần đất làm lối đi theo mét vuông.", "Tỉ lệ phần trăm diện tích lối đi là: $100\\% - (40\\% + 35\\% + 15\\%) = 10\\%$.\nDiện tích lối đi là: $2 400 \\times 10 : 100 = 240\\text{ (m$^2$)}$.", "240 m$^2$", 4, 1.0),
            make_essay(4, "Một đợt khảo sát 80 học sinh về việc yêu thích đọc sách truyện: có 60 bạn thích đọc truyện cổ tích, 16 bạn thích truyện trinh thám, 4 bạn không thích đọc truyện.\na) Tính tỉ số phần trăm số bạn thích đọc truyện cổ tích.\nb) Tính tỉ số mô tả số bạn thích truyện trinh thám so với tổng số học sinh dưới dạng phân số tối giản.", "a) Tỉ số phần trăm bạn thích truyện cổ tích là: $\\frac{60}{80} = \\frac{3}{4} = 75\\%$.\nb) Tỉ số bạn thích truyện trinh thám là: $\\frac{16}{80} = \\frac{1}{5}$.", "a) 75%; b) 1/5", 5, 1.5),
            make_essay(5, "Một thư viện trường có 3 000 cuốn sách. Biểu đồ quạt tròn cho biết sách giáo khoa chiếm 45%, truyện thiếu nhi chiếm 35%, còn lại là sách tham khảo. Hỏi số cuốn sách giáo khoa nhiều hơn số cuốn sách tham khảo bao nhiêu cuốn?", "Tỉ lệ phần trăm sách tham khảo là: $100\\% - (45\\% + 35\\%) = 20\\%$.\nSố sách giáo khoa là: $3 000 \\times 45 : 100 = 1 350$ (cuốn).\nSố sách tham khảo là: $3 000 \\times 20 : 100 = 600$ (cuốn).\nSố sách giáo khoa nhiều hơn sách tham khảo là:\n$1 350 - 600 = 750$ (cuốn).", "750 cuốn", 5, 1.5),
            make_essay(6, "Bác Năm nuôi đàn gà gồm 250 con. Bác ghi chép thấy có 140 con gà mái, 60 con gà trống, còn lại là gà con. Tính tỉ số phần trăm của số gà con so với tổng số đàn gà.", "Số con gà con là: $250 - (140 + 60) = 50$ (con).\nTỉ số phần trăm số gà con là:\n$\\frac{50}{250} = \\frac{1}{5} = 20\\%$.", "20%", 4, 1.0)
        ]
    }

    # --- Bài 55 - Đề 2 ---
    exams["th5_b55_test2"] = {
        "id": "th5_b55_test2",
        "lessonId": "th5_b55",
        "lessonNum": 55,
        "testNum": 2,
        "title": "Bài 55: Luyện tập chung Chủ đề 10 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 10",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một khu đất có 25% diện tích để làm nhà. Tỉ số phần trăm phần đất còn lại là:", ["75%", "50%", "25%", "65%"], 0, "100% - 25% = 75%."),
            make_mc(2, "Gieo con xúc xắc 40 lần, thấy mặt 2 chấm xuất hiện 8 lần. Tỉ số số lần xuất hiện mặt 2 chấm là:", ["0,2", "0,25", "0,15", "0,1"], 0, "8/40 = 1/5 = 0,2."),
            make_mc(3, "Một trường học có 600 học sinh. Biểu đồ quạt tròn cho biết học sinh đi xe đạp chiếm 45%. Số học sinh đi xe đạp là:", ["270 em", "250 em", "300 em", "240 em"], 0, "600 x 45 : 100 = 270 em."),
            make_mc(4, "Tung một đồng xu 50 lần, có 28 lần mặt ngửa. Tỉ số phần trăm mặt sấp xuất hiện là:", ["44%", "56%", "48%", "52%"], 0, "Mặt sấp = 50 - 28 = 22 lần. 22/50 = 44%."),
            make_mc(5, "Trong một hộp kín có 10 viên bi đỏ và 1 viên bi vàng. Lấy ngẫu nhiên 1 viên bi. Khả năng lấy được viên bi vàng là:", ["Có thể", "Chắc chắn", "Không thể", "Tất nhiên"], 0, "Bi vàng có trong hộp nên việc lấy được bi vàng là có thể xảy ra."),
            make_mc(6, "Biểu đồ quạt tròn biểu thị 3 thành phần A, B, C. Biết A = 30%, B = 45%. Thành phần C chiếm:", ["25%", "20%", "35%", "15%"], 0, "100% - (30% + 45%) = 25%.")
        ],
        "part2": [
            make_essay(1, "Một cửa hàng bán được 180 bộ quần áo trẻ em gồm: 45% váy bé gái, 35% áo sơ mi bé trai, còn lại là quần soóc. Tính số lượng quần soóc cửa hàng bán được.", "Tỉ lệ phần trăm số quần soóc là: $100\\% - (45\\% + 35\\%) = 20\\%$.\nSố quần soóc bán được là: $180 \\times 20 : 100 = 36$ (chiếc).", "36 chiếc quần soóc", 4, 1.0),
            make_essay(2, "Bạn Lan gieo một đồng xu 60 lần, ghi lại mặt N xuất hiện 36 lần.\na) Tính số lần xuất hiện mặt S.\nb) Viết tỉ số mô tả số lần xuất hiện mặt N dưới dạng phân số tối giản và số thập phân.", "a) Số lần xuất hiện mặt S là: $60 - 36 = 24$ (lần).\nb) Tỉ số xuất hiện mặt N là: $\\frac{36}{60} = \\frac{3}{5} = 0,6$.", "a) 24 lần; b) 3/5 (hay 0,6)", 4, 1.0),
            make_essay(3, "Một khu dân cư có 800 người. Biểu đồ quạt tròn cho biết: trẻ em chiếm 25%, người trong độ tuổi lao động chiếm 60%, người cao tuổi chiếm 15%. Tính số người trong độ tuổi lao động và số trẻ em.", "Số người trong độ tuổi lao động là: $800 \\times 60 : 100 = 480$ (người).\nSố trẻ em là: $800 \\times 25 : 100 = 200$ (người).", "Lao động: 480 người; Trẻ em: 200 người", 4, 1.0),
            make_essay(4, "Một cung thủ bắn 40 mũi tên, kết quả: 18 mũi trúng tâm 10 điểm, 14 mũi trúng vòng 9 điểm, 8 mũi trúng vòng 8 điểm.\na) Tính tỉ số phần trăm số mũi tên trúng tâm 10 điểm.\nb) Tính tỉ số phần trăm số mũi tên đạt từ 9 điểm trở lên.", "a) Tỉ số phần trăm mũi tên trúng tâm 10 điểm: $\\frac{18}{40} = 45\\%$.\nb) Số mũi tên từ 9 điểm trở lên là: $18 + 14 = 32$ (mũi).\nTỉ số phần trăm là: $\\frac{32}{40} = 80\\%$.", "a) 45%; b) 80%", 5, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có diện tích $600\\text{ m}^2$. Biểu đồ quạt tròn cho biết: diện tích làm nhà chiếm 35%, diện tích sân vườn chiếm 45%, phần còn lại làm bể bơi. Tính diện tích bể bơi.", "Tỉ lệ phần trăm diện tích bể bơi là: $100\\% - (35\\% + 45\\%) = 20\\%$.\nDiện tích bể bơi là: $600 \\times 20 : 100 = 120\\text{ (m$^2$)}$.", "120 m$^2$", 5, 1.5),
            make_essay(6, "Một lớp 5 có 32 học sinh. Trong đợt kiểm tra bơi lội, có 28 bạn đạt tiêu chuẩn bơi tốt. Viết tỉ số mô tả số bạn đạt tiêu chuẩn bơi tốt dưới dạng phân số tối giản và tỉ số phần trăm.", "Tỉ số bạn đạt tiêu chuẩn là: $\\frac{28}{32}$.\n- Phân số tối giản: $\\frac{28 : 4}{32 : 4} = \\frac{7}{8}$.\n- Tỉ số phần trăm: $\\frac{7}{8} = 0,875 = 87,5\\%$.", "7/8 (hay 87,5%)", 4, 1.0)
        ]
    }

    # --- Bài 55 - Đề 3 ---
    exams["th5_b55_test3"] = {
        "id": "th5_b55_test3",
        "lessonId": "th5_b55",
        "lessonNum": 55,
        "testNum": 3,
        "title": "Bài 55: Luyện tập chung Chủ đề 10 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 10",
        "chapter": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một trang trại có 1 000 con gà. Biểu đồ quạt tròn cho biết tỉ lệ gà con là 35%. Số gà con là:", ["350 con", "300 con", "400 con", "250 con"], 0, "1000 x 35 : 100 = 350 con."),
            make_mc(2, "Gieo con xúc xắc 50 lần, mặt 5 chấm xuất hiện 12 lần. Tỉ số phần trăm xuất hiện mặt 5 chấm là:", ["24%", "20%", "25%", "12%"], 0, "12/50 = 24/100 = 24%."),
            make_mc(3, "Tung đồng xu 60 lần, mặt ngửa xuất hiện 27 lần. Số lần mặt sấp xuất hiện là:", ["33 lần", "30 lần", "27 lần", "35 lần"], 0, "60 - 27 = 33 lần."),
            make_mc(4, "Biểu đồ quạt tròn biểu thị 4 phần: A = 40%, B = 25%, C = 20%. Phần D chiếm:", ["15%", "10%", "25%", "20%"], 0, "100% - (40% + 25% + 20%) = 15%."),
            make_mc(5, "Một người ném bóng vào rổ 20 lần, trúng đích 14 lần. Tỉ số ném trúng đích là:", ["0,7", "0,14", "0,6", "0,8"], 0, "14/20 = 7/10 = 0,7."),
            make_mc(6, "Khả năng ngày mai Mặt Trời mọc ở phía Tây là:", ["Không thể", "Có thể", "Chắc chắn", "Tùy ý"], 0, "Mặt Trời luôn mọc ở phía Đông nên việc mọc ở phía Tây là không thể.")
        ],
        "part2": [
            make_essay(1, "Một trường học có 500 học sinh. Biểu đồ quạt cho biết tỉ lệ tham gia giao thông: Đi bộ 30%, Bố mẹ chở bằng xe máy 50%, Đi xe đạp 20%. Tính số học sinh đi xe đạp và số học sinh đi bộ.", "Số học sinh đi xe đạp: $500 \\times 20 : 100 = 100$ (học sinh).\nSố học sinh đi bộ: $500 \\times 30 : 100 = 150$ (học sinh).", "Đi xe đạp: 100 học sinh; Đi bộ: 150 học sinh", 4, 1.0),
            make_essay(2, "Một người chơi trò ném phi tiêu 50 lần, ghi nhận được: 15 lần vào vòng 10 điểm, 20 lần vào vòng 9 điểm, 10 lần vào vòng 8 điểm, 5 lần trượt.\na) Tính tỉ số phần trăm số lần ném đạt 10 điểm.\nb) Tính tỉ số mô tả số lần ném trượt dưới dạng phân số tối giản.", "a) Tỉ số phần trăm đạt 10 điểm là: $\\frac{15}{50} = 30\\%$.\nb) Tỉ số ném trượt là: $\\frac{5}{50} = \\frac{1}{10}$.", "a) 30%; b) 1/10", 4, 1.0),
            make_essay(3, "Một xưởng mộc sản xuất 400 sản phẩm gồm: Bàn 35%, Ghế 45%, Tủ 20%. Tính số lượng ghế xưởng sản xuất được.", "Số lượng ghế xưởng sản xuất được là:\n$400 \\times 45 : 100 = 180$ (chiếc ghế).", "180 chiếc ghế", 4, 1.0),
            make_essay(4, "Một hộp chứa 4 viên bi xanh, 3 viên bi đỏ và 3 viên bi vàng. An rút ngẫu nhiên 1 viên bi, ghi màu rồi thả lại. Sau 50 lần thực nghiệm, An rút được 22 lần bi xanh, 14 lần bi đỏ, còn lại là bi vàng.\na) Tính số lần rút được bi vàng.\nb) Tính tỉ số phần trăm số lần rút được bi vàng.", "a) Số lần rút được bi vàng là: $50 - (22 + 14) = 14$ (lần).\nb) Tỉ số phần trăm rút được bi vàng là:\n$\\frac{14}{50} = \\frac{28}{100} = 28\\%$.", "a) 14 lần; b) 28%", 5, 1.5),
            make_essay(5, "Biểu đồ quạt tròn biểu thị tỉ lệ tiêu thụ các loại hoa quả tại một siêu thị trong ngày: Dưa hấu 40%, Xoài 25%, Cam 20%, Chuối 15%. Biết tổng số hoa quả bán được là 300 kg. Hỏi khối lượng Dưa hấu bán được nhiều hơn khối lượng Cam bao nhiêu ki-lô-gam?", "Khối lượng Dưa hấu bán được: $300 \\times 40 : 100 = 120\\text{ (kg)}$.\nKhối lượng Cam bán được: $300 \\times 20 : 100 = 60\\text{ (kg)}$.\nKhối lượng Dưa hấu nhiều hơn Cam là: $120 - 60 = 60\\text{ (kg)}$.", "60 kg", 5, 1.5),
            make_essay(6, "Trong đợt thi học sinh giỏi cấp trường, có 40 bạn tham gia và 34 bạn đạt giải. Viết tỉ số mô tả số bạn đạt giải dưới dạng phân số tối giản và tỉ số phần trăm.", "Tỉ số bạn đạt giải là: $\\frac{34}{40}$.\n- Phân số tối giản: $\\frac{34 : 2}{40 : 2} = \\frac{17}{20}$.\n- Tỉ số phần trăm: $\\frac{17}{20} = 85\\%$.", "17/20 (hay 85%)", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 10: {len(ex)} (Kỳ vọng: 9 đề)")
    for b in range(53, 56):
        for t in range(1, 4):
            key = f"th5_b{b}_test{t}"
            assert key in ex, f"Thiếu mã đề {key}"
            assert len(ex[key]["part1"]) == 6, f"part1 của {key} không đủ 6 câu"
            assert len(ex[key]["part2"]) == 6, f"part2 của {key} không đủ 6 bài"
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6, f"Điểm part1 của {key} là {p1_pts} khác 3.0"
            assert abs(p2_pts - 7.0) < 1e-6, f"Điểm part2 của {key} là {p2_pts} khác 7.0"
            assert abs(p1_pts + p2_pts - 10.0) < 1e-6, f"Tổng điểm của {key} khác 10.0"
    print("Tất cả 9 đề của Chủ đề 10 hoàn hảo 100%!")
