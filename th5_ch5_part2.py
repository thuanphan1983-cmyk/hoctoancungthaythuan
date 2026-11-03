# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 5: ÔN TẬP HỌC KÌ 1 (BÀI 26 ĐẾN BÀI 29) - PHẦN 2: BÀI 28 VÀ BÀI 29
Toán lớp 5 - Kết nối tri thức với cuộc sống.
Gồm 6 đề kiểm tra:
- Bài 28: Ôn tập một số yếu tố xác suất và thống kê (th5_b28_test1, th5_b28_test2, th5_b28_test3)
- Bài 29: Luyện tập chung Học kì 1 (th5_b29_test1, th5_b29_test2, th5_b29_test3)
"""

def get_ch5_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 28: ÔN TẬP MỘT SỐ YẾU TỐ XÁC SUẤT VÀ THỐNG KÊ (TEST 1, 2, 3)
    # =========================================================================

    exams["th5_b28_test1"] = {
        "title": "ĐỀ KIỂM TRA BÀI 28 (ĐỀ 1): ÔN TẬP MỘT SỐ YẾU TỐ XÁC SUẤT VÀ THỐNG KÊ",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Gieo một con xúc xắc 6 mặt (từ 1 đến 6 chấm). Sự kiện \"Xuất hiện mặt có số chấm lớn hơn 6\" là sự kiện:",
                "choices": ["Chắc chắn xảy ra", "Có thể xảy ra", "Không thể xảy ra", "Luôn xảy ra"],
                "correct": 2,
                "explanation": "Con xúc xắc chỉ có các mặt từ 1 đến 6 chấm, không có mặt nào lớn hơn 6 chấm nên sự kiện này không thể xảy ra.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Trong hộp có 4 viên bi đỏ và 1 viên bi xanh có cùng kích thước. Lấy ngẫu nhiên 1 viên bi từ hộp. Sự kiện \"Lấy được viên bi màu đỏ\" là sự kiện:",
                "choices": ["Không thể xảy ra", "Chắc chắn xảy ra", "Có thể xảy ra", "Không bao giờ xảy ra"],
                "correct": 2,
                "explanation": "Trong hộp có cả bi đỏ và bi xanh nên việc lấy được bi đỏ là sự kiện có thể xảy ra (với khả năng xảy ra cao hơn bi xanh).",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Tung một đồng xu 20 lần liên tiếp, thấy có 12 lần xuất hiện mặt Ngửa. Tỉ số mô tả số lần xuất hiện mặt Ngửa so với tổng số lần tung là:",
                "choices": ["3/5", "2/5", "3/2", "1/2"],
                "correct": 0,
                "explanation": "Tỉ số là 12/20. Rút gọn chia cả tử và mẫu cho 4 ta được 3/5.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Thống kê số cây trồng được của 4 tổ: Tổ 1 trồng 15 cây, Tổ 2 trồng 18 cây, Tổ 3 trồng 20 cây, Tổ 4 trồng 17 cây. Tổng số cây cả 4 tổ trồng được là:",
                "choices": ["60 cây", "70 cây", "68 cây", "72 cây"],
                "correct": 1,
                "explanation": "Tổng số cây = 15 + 18 + 20 + 17 = 70 (cây).",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Nam quay một vòng quay may mắn chia đều 4 phần ghi các số 1, 2, 3, 4. Khả năng mũi tên chỉ vào ô ghi số lẻ có tỉ số là:",
                "choices": ["1/4", "1/2", "3/4", "1"],
                "correct": 1,
                "explanation": "Có 2 số lẻ là 1 và 3 trong tổng số 4 số. Tỉ số mô tả khả năng là 2/4 = 1/2.",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Một lớp học có 32 học sinh, trong đó có 18 học sinh nữ. Tỉ số của số học sinh nam so với tổng số học sinh cả lớp là:",
                "choices": ["9/16", "7/16", "9/7", "7/9"],
                "correct": 1,
                "explanation": "Số học sinh nam là: 32 - 18 = 14 (học sinh). Tỉ số số học sinh nam so với cả lớp là: 14/32 = 7/16.",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Trong hộp kín có 3 quả bóng xanh, 2 quả bóng đỏ và 1 quả bóng vàng có cùng kích thước. Bạn An nhắm mắt lấy ra cùng lúc 2 quả bóng. Hãy dùng các từ \"chắc chắn\", \"có thể\", \"không thể\" để điền vào chỗ chấm:\na) An ... lấy được 2 quả bóng màu vàng.\nb) An ... lấy được ít nhất 1 quả bóng màu xanh.\nc) An ... lấy được 2 quả bóng màu tím.\nd) Hai quả bóng lấy ra ... có màu khác nhau.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Trong hộp chỉ có 1 quả bóng vàng nên An không thể lấy được 2 quả bóng màu vàng.\nb) Có 3 quả bóng xanh nên An có thể lấy được ít nhất 1 quả bóng màu xanh.\nc) Trong hộp không có quả bóng màu tím nào nên An không thể lấy được 2 quả bóng màu tím.\nd) Hai quả bóng lấy ra có thể có màu khác nhau (ví dụ 1 xanh và 1 đỏ).\nĐáp số: a) không thể; b) có thể; c) không thể; d) có thể.",
                "answer": "a) không thể; b) có thể; c) không thể; d) có thể"
            },
            {
                "question": "**Bài 2:** Bảng số liệu sau ghi lại chiều cao (cm) của 5 bạn học sinh: Lan: 138 cm; Minh: 142 cm; Nam: 140 cm; Hoa: 136 cm; Đức: 144 cm.\na) Bạn nào cao nhất? Bạn nào thấp nhất?\nb) Tính chiều cao trung bình của 5 bạn học sinh đó.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) So sánh chiều cao: 136 < 138 < 140 < 142 < 144.\nBạn Đức cao nhất (144 cm), bạn Hoa thấp nhất (136 cm).\nb) Chiều cao trung bình của 5 bạn là:\n(138 + 142 + 140 + 136 + 144) : 5 = 700 : 5 = 140 (cm)\nĐáp số: a) Đức cao nhất (144 cm), Hoa thấp nhất (136 cm); b) 140 cm.",
                "answer": "a) Đức cao nhất, Hoa thấp nhất; b) 140 cm"
            },
            {
                "question": "**Bài 3:** Bạn Bình gieo một con xúc xắc 30 lần liên tiếp và ghi nhận mặt 6 chấm xuất hiện 5 lần.\na) Viết tỉ số mô tả số lần xuất hiện mặt 6 chấm so với tổng số lần gieo.\nb) Mặt không phải 6 chấm xuất hiện bao nhiêu lần? Viết tỉ số mô tả số lần xuất hiện mặt không phải 6 chấm so với tổng số lần gieo.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Tỉ số mô tả số lần xuất hiện mặt 6 chấm so với tổng số lần gieo là:\n5/30 = 1/6\nb) Số lần xuất hiện mặt không phải 6 chấm là:\n30 - 5 = 25 (lần)\nTỉ số mô tả số lần xuất hiện mặt không phải 6 chấm là:\n25/30 = 5/6\nĐáp số: a) 1/6; b) 25 lần, tỉ số là 5/6.",
                "answer": "a) 1/6; b) 25 lần, tỉ số là 5/6"
            },
            {
                "question": "**Bài 4:** Thống kê số quyển vở quyên góp ủng hộ học sinh vùng cao của các khối lớp ở một trường tiểu học: Khối 1: 180 quyển; Khối 2: 210 quyển; Khối 3: 240 quyển; Khối 4: 270 quyển; Khối 5: 300 quyển.\na) Khối lớp nào quyên góp được nhiều nhất? Khối nào ít nhất?\nb) Cả trường đã quyên góp được tất cả bao nhiêu quyển vở?\nc) Trung bình mỗi khối lớp quyên góp được bao nhiêu quyển vở?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Khối 5 quyên góp nhiều nhất (300 quyển); Khối 1 quyên góp ít nhất (180 quyển).\nb) Toàn trường quyên góp được tất cả số quyển vở là:\n180 + 210 + 240 + 270 + 300 = 1200 (quyển)\nc) Trung bình mỗi khối lớp quyên góp được số quyển vở là:\n1200 : 5 = 240 (quyển)\nĐáp số: a) Khối 5 nhiều nhất, Khối 1 ít nhất; b) 1200 quyển; c) 240 quyển.",
                "answer": "a) Khối 5 nhiều nhất, Khối 1 ít nhất; b) 1200 quyển; c) 240 quyển"
            },
            {
                "question": "**Bài 5:** Trong túi có 20 chiếc kẹo gồm 8 kẹo cam, 7 kẹo dâu và 5 kẹo nho cùng kích thước. Mai nhắm mắt lấy ngẫu nhiên các chiếc kẹo trong túi.\na) Nếu chỉ lấy ra 1 chiếc kẹo, sự kiện \"Mai lấy được chiếc kẹo vị sô-cô-la\" có khả năng xảy ra như thế nào?\nb) Mai phải lấy ra ít nhất bao nhiêu chiếc kẹo để chắc chắn có ít nhất 1 chiếc kẹo vị nho?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Vì trong túi không có chiếc kẹo vị sô-cô-la nào nên sự kiện \"Mai lấy được chiếc kẹo vị sô-cô-la\" là sự kiện không thể xảy ra.\nb) Trường hợp xấu nhất là Mai lấy phải toàn bộ số kẹo cam và kẹo dâu:\n8 + 7 = 15 (chiếc kẹo)\nKhi đó, lấy thêm 1 chiếc kẹo nữa thì chắc chắn chiếc kẹo đó là vị nho.\nSố chiếc kẹo Mai cần lấy ra ít nhất là:\n15 + 1 = 16 (chiếc kẹo)\nĐáp số: a) Không thể xảy ra; b) 16 chiếc kẹo.",
                "answer": "a) Không thể xảy ra; b) 16 chiếc kẹo"
            },
            {
                "question": "**Bài 6:** Điểm kiểm tra môn Toán của 4 bạn học sinh là 8; 9; 10 và x điểm. Biết điểm trung bình của cả 4 bạn là 8,5 điểm. Tìm giá trị của x.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Tổng số điểm của cả 4 bạn học sinh là:\n8,5 x 4 = 34 (điểm)\nTổng số điểm của 3 bạn đã biết là:\n8 + 9 + 10 = 27 (điểm)\nGiá trị của x (điểm của bạn thứ tư) là:\n34 - 27 = 7 (điểm)\nĐáp số: x = 7.",
                "answer": "x = 7"
            }
        ]
    }

    exams["th5_b28_test2"] = {
        "title": "ĐỀ KIỂM TRA BÀI 28 (ĐỀ 2): ÔN TẬP MỘT SỐ YẾU TỐ XÁC SUẤT VÀ THỐNG KÊ",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Gieo một đồng xu có hai mặt Sấp (S) và Ngửa (N). Sự kiện \"Mặt xuất hiện là mặt Sấp hoặc mặt Ngửa\" là sự kiện:",
                "choices": ["Không thể xảy ra", "Chắc chắn xảy ra", "Có thể xảy ra", "Hiếm khi xảy ra"],
                "correct": 1,
                "explanation": "Đồng xu chỉ có hai mặt Sấp và Ngửa nên khi gieo chắc chắn sẽ xuất hiện một trong hai mặt đó.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Trong túi có 5 viên bi xanh và 5 viên bi đỏ có cùng kích thước. Lấy ngẫu nhiên 1 viên bi. Khả năng lấy được bi xanh và khả năng lấy được bi đỏ là:",
                "choices": ["Khả năng lấy bi xanh lớn hơn", "Khả năng lấy bi đỏ lớn hơn", "Như nhau (bằng nhau)", "Không xác định được"],
                "correct": 2,
                "explanation": "Vì số lượng bi xanh và bi đỏ trong túi bằng nhau (đều có 5 viên) nên khả năng lấy được mỗi loại bi là như nhau.",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Điểm kiểm tra môn Tiếng Việt của bạn Hà trong 4 lần kiểm tra lần lượt là: 8; 9; 7; 10. Điểm kiểm tra trung bình của Hà là:",
                "choices": ["8,0", "8,5", "9,0", "8,2"],
                "correct": 1,
                "explanation": "Điểm trung bình = (8 + 9 + 7 + 10) : 4 = 34 : 4 = 8,5.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Một hộp có 10 tấm thẻ được đánh số từ 1 đến 10. Rút ngẫu nhiên một tấm thẻ. Tỉ số mô tả khả năng rút được tấm thẻ mang số chẵn là:",
                "choices": ["1/5", "1/2", "3/10", "2/5"],
                "correct": 1,
                "explanation": "Có 5 số chẵn là 2, 4, 6, 8, 10 trong 10 số. Tỉ số là 5/10 = 1/2.",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Điều tra về môn thể thao yêu thích nhất của 40 học sinh: Bóng đá có 18 bạn, Cầu lông có 12 bạn, Bơi lội có 6 bạn, Cờ vua có 4 bạn. Tỉ số của số bạn thích bóng đá so với cả lớp là:",
                "choices": ["9/20", "3/10", "3/20", "1/10"],
                "correct": 0,
                "explanation": "Tỉ số bạn thích bóng đá so với cả lớp là 18/40 = 9/20.",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Bạn Khoa tung con xúc xắc 24 lần thì có 4 lần xuất hiện mặt 1 chấm. Tỉ số giữa số lần xuất hiện mặt 1 chấm và tổng số lần tung là:",
                "choices": ["1/4", "1/6", "1/5", "1/8"],
                "correct": 1,
                "explanation": "Tỉ số là 4/24 = 1/6.",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Điền từ \"chắc chắn\", \"có thể\", \"không thể\" thích hợp vào chỗ chấm:\nMột hộp đựng 4 quả bóng xanh và 3 quả bóng đỏ cùng kích thước.\na) Lấy ra 1 quả bóng thì quả bóng đó ... có màu đỏ.\nb) Lấy ra 1 quả bóng thì quả bóng đó ... có màu vàng.\nc) Lấy ra 5 quả bóng thì ... có ít nhất 1 quả bóng màu xanh.\nd) Lấy ra 2 quả bóng thì 2 quả bóng đó ... cùng màu.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Lấy ra 1 quả bóng thì quả bóng đó có thể có màu đỏ.\nb) Trong hộp không có bóng vàng nên bóng lấy ra không thể có màu vàng.\nc) Vì chỉ có 3 bóng đỏ nên nếu lấy 5 quả thì chắc chắn có ít nhất 2 quả bóng màu xanh (nên chắc chắn có ít nhất 1 quả bóng xanh).\nd) Lấy ra 2 quả bóng thì 2 quả bóng đó có thể cùng màu (cùng đỏ hoặc cùng xanh).\nĐáp số: a) có thể; b) không thể; c) chắc chắn; d) có thể.",
                "answer": "a) có thể; b) không thể; c) chắc chắn; d) có thể"
            },
            {
                "question": "**Bài 2:** Số lượng sách quyên góp được của 4 tổ học sinh: Tổ 1: 24 quyển; Tổ 2: 28 quyển; Tổ 3: 32 quyển; Tổ 4: 36 quyển.\na) Tổ nào quyên góp được nhiều sách nhất? Tổ nào ít sách nhất?\nb) Tính số sách trung bình mỗi tổ quyên góp được.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Tổ 4 quyên góp nhiều nhất (36 quyển), Tổ 1 ít nhất (24 quyển).\nb) Tổng số sách 4 tổ quyên góp được là:\n24 + 28 + 32 + 36 = 120 (quyển)\nTrung bình mỗi tổ quyên góp được số quyển sách là:\n120 : 4 = 30 (quyển)\nĐáp số: a) Tổ 4 nhiều nhất, Tổ 1 ít nhất; b) 30 quyển sách.",
                "answer": "a) Tổ 4 nhiều nhất, Tổ 1 ít nhất; b) 30 quyển"
            },
            {
                "question": "**Bài 3:** Bạn Linh quay một tấm bìa hình tròn chia thành 8 phần bằng nhau, trong đó có 3 phần tô màu đỏ, 2 phần tô màu xanh và 3 phần tô màu vàng.\na) Viết tỉ số mô tả khả năng mũi tên dừng lại ở phần tô màu xanh.\nb) Khả năng mũi tên dừng lại ở phần màu đỏ và phần màu vàng như thế nào với nhau?",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Tỉ số mô tả khả năng mũi tên dừng lại ở phần màu xanh là:\n2/8 = 1/4\nb) Vì số phần tô màu đỏ và số phần tô màu vàng bằng nhau (đều là 3 phần) nên khả năng mũi tên dừng lại ở phần màu đỏ và phần màu vàng là như nhau (bằng nhau).\nĐáp số: a) 1/4; b) Như nhau (bằng nhau).",
                "answer": "a) 1/4; b) Như nhau (bằng nhau)"
            },
            {
                "question": "**Bài 4:** Ba lớp 5A, 5B, 5C tham gia trồng hoa trong vườn trường. Lớp 5A trồng được 65 cây. Lớp 5B trồng được nhiều hơn lớp 5A là 10 cây. Lớp 5C trồng được số cây kém mức trung bình cộng của cả ba lớp là 4 cây.\na) Tính số cây hoa lớp 5B trồng được.\nb) Tính số cây hoa lớp 5C trồng được.",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Số cây hoa lớp 5B trồng được là:\n65 + 10 = 75 (cây)\nb) Hai lần trung bình cộng của ba lớp là:\n65 + 75 - 4 = 136 (cây)\nTrung bình cộng số cây của cả ba lớp là:\n136 : 2 = 68 (cây)\nSố cây hoa lớp 5C trồng được là:\n68 - 4 = 64 (cây)\nĐáp số: a) 75 cây; b) 64 cây.",
                "answer": "a) 75 cây; b) 64 cây"
            },
            {
                "question": "**Bài 5:** Một hộp có 15 viên bi gồm 6 bi đỏ, 5 bi xanh và 4 bi vàng có cùng kích thước.\na) Không nhìn vào hộp, cần lấy ra ít nhất bao nhiêu viên bi để chắc chắn có ít nhất 1 viên bi màu đỏ?\nb) Cần lấy ra ít nhất bao nhiêu viên bi để chắc chắn lấy được đủ cả 3 màu bi?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Trường hợp xấu nhất là lấy phải toàn bộ số bi xanh và bi vàng:\n5 + 4 = 9 (viên)\nLấy thêm 1 viên nữa chắc chắn được bi đỏ. Vậy cần lấy ít nhất:\n9 + 1 = 10 (viên bi)\nb) Trường hợp xấu nhất là lấy hết toàn bộ bi của 2 màu có số lượng nhiều nhất (bi đỏ và bi xanh):\n6 + 5 = 11 (viên)\nLấy thêm 1 viên nữa chắc chắn có viên bi màu vàng. Vậy cần lấy ít nhất:\n11 + 1 = 12 (viên bi)\nĐáp số: a) 10 viên bi; b) 12 viên bi.",
                "answer": "a) 10 viên bi; b) 12 viên bi"
            },
            {
                "question": "**Bài 6:** Một cửa hàng ghi lại số lượng tivi bán được trong 5 tháng đầu năm: Tháng 1 bán 25 chiếc; Tháng 2 bán 30 chiếc; Tháng 3 bán 28 chiếc; Tháng 4 bán 35 chiếc; Tháng 5 bán x chiếc. Biết số tivi bán được trung bình mỗi tháng là 32 chiếc. Tìm số tivi cửa hàng bán được trong tháng 5.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Tổng số tivi cửa hàng bán được trong 5 tháng là:\n32 x 5 = 160 (chiếc)\nTổng số tivi bán được trong 4 tháng đầu là:\n25 + 30 + 28 + 35 = 118 (chiếc)\nSố tivi bán được trong tháng 5 là:\n160 - 118 = 42 (chiếc)\nĐáp số: 42 chiếc tivi.",
                "answer": "42 chiếc"
            }
        ]
    }

    exams["th5_b28_test3"] = {
        "title": "ĐỀ KIỂM TRA BÀI 28 (ĐỀ 3): ÔN TẬP MỘT SỐ YẾU TỐ XÁC SUẤT VÀ THỐNG KÊ",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Trong các sự kiện sau, sự kiện nào là sự kiện \"Chắc chắn xảy ra\"?",
                "choices": [
                    "Ngày mai trời sẽ có mưa to",
                    "Mặt trời mọc ở hướng Đông",
                    "Gieo xúc xắc được mặt 6 chấm",
                    "Tung đồng xu rơi trúng mặt ngửa"
                ],
                "correct": 1,
                "explanation": "Quy luật tự nhiên mặt trời luôn mọc ở hướng Đông nên sự kiện này chắc chắn xảy ra.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Gieo một con xúc xắc 6 mặt một lần. Khả năng xuất hiện mặt có số chấm chia hết cho 3 có tỉ số là:",
                "choices": ["1/6", "1/3", "1/2", "2/3"],
                "correct": 1,
                "explanation": "Có 2 mặt chia hết cho 3 (mặt 3 chấm và mặt 6 chấm) trong 6 mặt. Tỉ số là 2/6 = 1/3.",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Một tổ có 10 bạn học sinh. Trong bài kiểm tra Toán có 4 bạn đạt 10 điểm, 5 bạn đạt 9 điểm và 1 bạn đạt 8 điểm. Điểm trung bình môn Toán của tổ đó là:",
                "choices": ["9,0", "9,1", "9,3", "9,5"],
                "correct": 2,
                "explanation": "Tổng số điểm = 4 x 10 + 5 x 9 + 1 x 8 = 40 + 45 + 8 = 93 (điểm). Điểm trung bình = 93 : 10 = 9,3.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Trong một hộp có 12 chiếc bút chì gồm 7 chiếc màu đỏ và 5 chiếc màu xanh. Tỉ số giữa số bút chì màu xanh và tổng số bút chì trong hộp là:",
                "choices": ["5/7", "7/12", "5/12", "1/2"],
                "correct": 2,
                "explanation": "Tỉ số của số bút chì xanh so với tổng số bút trong hộp là 5/12.",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Bạn Nam tung đồng xu 50 lần liên tiếp và ghi nhận được 28 lần xuất hiện mặt Sấp. Số lần xuất hiện mặt Ngửa là:",
                "choices": ["28 lần", "22 lần", "50 lần", "25 lần"],
                "correct": 1,
                "explanation": "Số lần xuất hiện mặt Ngửa là: 50 - 28 = 22 (lần).",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Nhiệt độ đo được lúc 12 giờ trưa trong 5 ngày từ thứ Hai đến thứ Sáu lần lượt là: 26°C, 28°C, 27°C, 29°C, 30°C. Nhiệt độ trung bình trong 5 ngày đó là:",
                "choices": ["28°C", "27,5°C", "28,5°C", "29°C"],
                "correct": 0,
                "explanation": "Nhiệt độ trung bình = (26 + 28 + 27 + 29 + 30) : 5 = 140 : 5 = 28 (°C).",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Bạn Hùng bốc thăm ngẫu nhiên 1 chiếc thăm từ chiếc hộp có 10 chiếc thăm đánh số từ 1 đến 10. Điền từ \"chắc chắn\", \"có thể\", \"không thể\" vào chỗ chấm:\na) Hùng ... bốc được chiếc thăm ghi số có hai chữ số.\nb) Hùng ... bốc được chiếc thăm ghi số 0.\nc) Hùng ... bốc được chiếc thăm ghi số nhỏ hơn 11.\nd) Hùng ... bốc được chiếc thăm ghi số chia hết cho 5.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Trong hộp có số 10 là số có hai chữ số nên Hùng có thể bốc được chiếc thăm ghi số có hai chữ số.\nb) Hộp chỉ có thăm từ 1 đến 10 nên Hùng không thể bốc được chiếc thăm ghi số 0.\nc) Tất cả các số từ 1 đến 10 đều nhỏ hơn 11 nên Hùng chắc chắn bốc được số nhỏ hơn 11.\nd) Có các số 5 và 10 chia hết cho 5 nên Hùng có thể bốc được số chia hết cho 5.\nĐáp số: a) có thể; b) không thể; c) chắc chắn; d) có thể.",
                "answer": "a) có thể; b) không thể; c) chắc chắn; d) có thể"
            },
            {
                "question": "**Bài 2:** Một cửa hàng bán trái cây trong 4 ngày ghi lại số lượng cam bán được: Ngày 1 bán 45 kg; Ngày 2 bán 52 kg; Ngày 3 bán 48 kg; Ngày 4 bán 55 kg.\na) Ngày nào bán được nhiều cam nhất? Ngày nào bán ít cam nhất?\nb) Trung bình mỗi ngày cửa hàng bán được bao nhiêu ki-lô-gam cam?",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Ngày 4 bán nhiều nhất (55 kg); Ngày 1 bán ít nhất (45 kg).\nb) Tổng số cam bán được trong 4 ngày là:\n45 + 52 + 48 + 55 = 200 (kg)\nTrung bình mỗi ngày bán được số ki-lô-gam cam là:\n200 : 4 = 50 (kg)\nĐáp số: a) Ngày 4 nhiều nhất, Ngày 1 ít nhất; b) 50 kg.",
                "answer": "a) Ngày 4 nhiều nhất, Ngày 1 ít nhất; b) 50 kg"
            },
            {
                "question": "**Bài 3:** Bạn Lan gieo một con xúc xắc 20 lần và ghi lại số lần xuất hiện các mặt: Mặt 1 chấm: 3 lần; Mặt 2 chấm: 4 lần; Mặt 3 chấm: 2 lần; Mặt 4 chấm: 5 lần; Mặt 5 chấm: 3 lần; Mặt 6 chấm: 3 lần.\na) Mặt nào xuất hiện nhiều lần nhất? Mặt nào ít lần nhất?\nb) Viết tỉ số mô tả số lần xuất hiện mặt 4 chấm so với tổng số lần gieo.",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) Mặt 4 chấm xuất hiện nhiều lần nhất (5 lần); Mặt 3 chấm xuất hiện ít lần nhất (2 lần).\nb) Tỉ số mô tả số lần xuất hiện mặt 4 chấm so với tổng số lần gieo là:\n5/20 = 1/4\nĐáp số: a) Mặt 4 chấm nhiều nhất, Mặt 3 chấm ít nhất; b) 1/4.",
                "answer": "a) Mặt 4 chấm nhiều nhất, Mặt 3 chấm ít nhất; b) 1/4"
            },
            {
                "question": "**Bài 4:** Thống kê số cây bóng mát trồng được trong 3 đợt của một trường tiểu học: Đợt 1 trồng được 120 cây. Đợt 2 trồng được nhiều hơn đợt 1 là 30 cây. Đợt 3 trồng được số cây bằng trung bình cộng của cả ba đợt.\na) Đợt 2 trồng được bao nhiêu cây?\nb) Đợt 3 trồng được bao nhiêu cây?\nc) Cả ba đợt trường đó trồng được tất cả bao nhiêu cây?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Số cây đợt 2 trồng được là:\n120 + 30 = 150 (cây)\nb) Vì số cây đợt 3 bằng trung bình cộng của cả 3 đợt nên số cây đợt 3 bằng trung bình cộng số cây của đợt 1 và đợt 2:\n(120 + 150) : 2 = 135 (cây)\nc) Cả ba đợt trường đó trồng được số cây là:\n120 + 150 + 135 = 405 (cây)\nĐáp số: a) 150 cây; b) 135 cây; c) 405 cây.",
                "answer": "a) 150 cây; b) 135 cây; c) 405 cây"
            },
            {
                "question": "**Bài 5:** Trong một chiếc hộp có chứa 8 viên bi xanh, 6 viên bi đỏ và 4 viên bi vàng cùng kích thước. Bạn Long nhắm mắt lấy ra ngẫu nhiên một số viên bi.\na) Long cần lấy ra ít nhất bao nhiêu viên bi để chắc chắn trong số bi lấy ra có đủ cả 3 màu?\nb) Long cần lấy ra ít nhất bao nhiêu viên bi để chắc chắn có ít nhất 2 viên bi màu xanh?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Trường hợp xấu nhất là Long lấy hết toàn bộ số bi của hai màu có số lượng nhiều nhất (xanh và đỏ):\n8 + 6 = 14 (viên)\nLấy thêm 1 viên nữa chắc chắn là bi vàng. Vậy Long cần lấy ít nhất:\n14 + 1 = 15 (viên bi)\nb) Trường hợp xấu nhất là Long lấy hết toàn bộ bi đỏ và bi vàng:\n6 + 4 = 10 (viên)\nKhi đó cần lấy thêm 2 viên bi nữa thì chắc chắn 2 viên đó đều là bi xanh. Vậy cần lấy ít nhất:\n10 + 2 = 12 (viên bi)\nĐáp số: a) 15 viên bi; b) 12 viên bi.",
                "answer": "a) 15 viên bi; b) 12 viên bi"
            },
            {
                "question": "**Bài 6:** Điểm trung bình môn Toán của 5 bạn học sinh là 8,4 điểm. Sau khi có thêm điểm kiểm tra của bạn thứ sáu thì điểm trung bình của cả 6 bạn là 8,5 điểm. Hỏi bạn thứ sáu đạt được bao nhiêu điểm?",
                "points": 1.0,
                "lineCount": 4,
                "solution": "Tổng số điểm kiểm tra của 5 bạn học sinh ban đầu là:\n8,4 x 5 = 42 (điểm)\nTổng số điểm kiểm tra của cả 6 bạn học sinh là:\n8,5 x 6 = 51 (điểm)\nĐiểm kiểm tra của bạn học sinh thứ sáu là:\n51 - 42 = 9 (điểm)\nĐáp số: 9 điểm.",
                "answer": "9 điểm"
            }
        ]
    }

    # =========================================================================
    # BÀI 29: LUYỆN TẬP CHUNG HỌC KÌ 1 (TEST 1, 2, 3)
    # =========================================================================

    exams["th5_b29_test1"] = {
        "title": "ĐỀ KIỂM TRA BÀI 29 (ĐỀ 1): LUYỆN TẬP CHUNG HỌC KÌ 1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Số thập phân gồm 24 đơn vị, 5 phần trăm và 7 phần nghìn được viết là:",
                "choices": ["24,57", "24,057", "24,507", "240,57"],
                "correct": 1,
                "explanation": "Phần nguyên là 24, hàng phần mười là 0, hàng phần trăm là 5, hàng phần nghìn là 7 nên viết là 24,057.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Phân số 3/4 được viết dưới dạng số thập phân là:",
                "choices": ["0,34", "0,75", "0,5", "0,25"],
                "correct": 1,
                "explanation": "3/4 = (3 x 25) / (4 x 25) = 75/100 = 0,75.",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Kết quả của phép tính 3,75 x 4 là:",
                "choices": ["15", "14,8", "15,2", "12,75"],
                "correct": 0,
                "explanation": "3,75 x 4 = 15,00 = 15.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Một mảnh đất hình tam giác có độ dài đáy là 20 m và chiều cao tương ứng là 12 m. Diện tích mảnh đất đó là:",
                "choices": ["240 m²", "120 m²", "60 m²", "160 m²"],
                "correct": 1,
                "explanation": "Diện tích tam giác = (20 x 12) : 2 = 120 (m²).",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Chu vi hình tròn có đường kính d = 6 cm là:",
                "choices": ["18,84 cm", "9,42 cm", "28,26 cm", "37,68 cm"],
                "correct": 0,
                "explanation": "Chu vi hình tròn = d x 3,14 = 6 x 3,14 = 18,84 (cm).",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Bạn Mai tung một đồng xu 25 lần thì có 15 lần xuất hiện mặt Ngửa. Tỉ số giữa số lần xuất hiện mặt Ngửa và tổng số lần tung là:",
                "choices": ["3/5", "2/5", "5/3", "1/2"],
                "correct": 0,
                "explanation": "Tỉ số là 15/25 = 3/5.",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Đặt tính rồi tính:\na) 538,45 + 179,8\nb) 400 - 165,38",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 538,45 + 179,80 = 718,25\nb) 400,00 - 165,38 = 234,62\nĐáp số: a) 718,25; b) 234,62.",
                "answer": "a) 718,25; b) 234,62"
            },
            {
                "question": "**Bài 2:** Đặt tính rồi tính:\na) 36,5 x 2,8\nb) 91,2 : 24",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 36,5 x 2,8 = 102,2\nb) 91,2 : 24 = 3,8 (91 : 24 = 3 dư 19; phẩy; hạ 2 được 192 : 24 = 8)\nĐáp số: a) 102,2; b) 3,8.",
                "answer": "a) 102,2; b) 3,8"
            },
            {
                "question": "**Bài 3:** Tính bằng cách thuận tiện nhất:\n8,3 x 7,5 + 8,3 x 2,5",
                "points": 1.0,
                "lineCount": 4,
                "solution": "8,3 x 7,5 + 8,3 x 2,5 = 8,3 x (7,5 + 2,5)\n= 8,3 x 10\n= 83\nĐáp số: 83.",
                "answer": "83"
            },
            {
                "question": "**Bài 4:** Một thửa ruộng hình thang có đáy lớn 45 m, đáy bé 35 m và chiều cao 20 m.\na) Tính diện tích thửa ruộng đó theo mét vuông và héc-ta.\nb) Người ta cấy lúa trên thửa ruộng, cứ 100 m² thu hoạch được 70 kg thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Diện tích thửa ruộng hình thang là:\n(45 + 35) x 20 : 2 = 800 (m²)\nĐổi: 800 m² = 0,08 ha\nb) Cả thửa ruộng thu hoạch được số ki-lô-gam thóc là:\n800 : 100 x 70 = 560 (kg)\nĐổi: 560 kg = 5,6 tạ\nĐáp số: a) 800 m² (0,08 ha); b) 5,6 tạ thóc.",
                "answer": "a) 800 m² (0,08 ha); b) 5,6 tạ"
            },
            {
                "question": "**Bài 5:** Hai đội công nhân cùng tham gia sửa một đoạn đường dài 480 m. Sau khi hoàn thành, đoạn đường đội thứ nhất sửa được bằng 3/5 đoạn đường đội thứ hai sửa được. Hỏi mỗi đội đã sửa được bao nhiêu mét đường?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "Tổng số phần bằng nhau là:\n3 + 5 = 8 (phần)\nĐội thứ nhất đã sửa được số mét đường là:\n480 : 8 x 3 = 180 (m)\nĐội thứ hai đã sửa được số mét đường là:\n480 - 180 = 300 (m)\nĐáp số: Đội thứ nhất: 180 m đường; Đội thứ hai: 300 m đường.",
                "answer": "Đội 1: 180 m; Đội 2: 300 m"
            },
            {
                "question": "**Bài 6:** Tìm một số thập phân có một chữ số ở phần thập phân, biết rằng nếu xóa dấu phẩy của số đó đi thì số đó tăng thêm 154,8 đơn vị.",
                "points": 1.0,
                "lineCount": 5,
                "solution": "Khi xóa dấu phẩy của số thập phân có một chữ số ở phần thập phân, số đó gấp lên 10 lần.\nHiệu số phần bằng nhau là:\n10 - 1 = 9 (phần)\nSố thập phân ban đầu cần tìm là:\n154,8 : 9 = 17,2\nĐáp số: 17,2.",
                "answer": "17,2"
            }
        ]
    }

    exams["th5_b29_test2"] = {
        "title": "ĐỀ KIỂM TRA BÀI 29 (ĐỀ 2): LUYỆN TẬP CHUNG HỌC KÌ 1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Chữ số 5 trong số thập phân 162,58 có giá trị là:",
                "choices": ["5", "5/10", "5/100", "50"],
                "correct": 1,
                "explanation": "Chữ số 5 đứng ở vị trí hàng phần mười nên có giá trị là 5/10 (hay 0,5).",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Số đo 6 m² 8 dm² được viết dưới dạng số thập phân có đơn vị mét vuông là:",
                "choices": ["6,8 m²", "6,08 m²", "6,008 m²", "68 m²"],
                "correct": 1,
                "explanation": "8 dm² = 0,08 m² nên 6 m² 8 dm² = 6,08 m².",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Kết quả của phép tính 48,6 : 0,1 là:",
                "choices": ["4,86", "486", "48,60", "0,486"],
                "correct": 1,
                "explanation": "Chia một số cho 0,1 bằng nhân số đó với 10: 48,6 : 0,1 = 486.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Một hình tam giác có diện tích 48 cm² và chiều cao 8 cm. Độ dài cạnh đáy tương ứng của hình tam giác đó là:",
                "choices": ["6 cm", "12 cm", "8 cm", "24 cm"],
                "correct": 1,
                "explanation": "Độ dài đáy = Diện tích x 2 : Chiều cao = 48 x 2 : 8 = 12 (cm).",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Diện tích của hình tròn có bán kính r = 3 cm là:",
                "choices": ["18,84 cm²", "9,42 cm²", "28,26 cm²", "14,13 cm²"],
                "correct": 2,
                "explanation": "Diện tích hình tròn = 3 x 3 x 3,14 = 28,26 (cm²).",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Trong hộp có 8 bút chì màu đen và 12 bút chì màu vàng. Tỉ số của số bút màu đen so với tổng số bút trong hộp là:",
                "choices": ["2/3", "2/5", "3/5", "4/5"],
                "correct": 1,
                "explanation": "Tổng số bút là 8 + 12 = 20 chiếc. Tỉ số số bút đen so với tổng số bút là 8/20 = 2/5.",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Viết số thập phân thích hợp vào chỗ chấm:\na) 5 km 68 m = ... km\nb) 9 tấn 35 kg = ... tấn\nc) 7 ha 400 m² = ... ha\nd) 15 m² 8 dm² = ... m²",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 68 m = 0,068 km => 5 km 68 m = 5,068 km\nb) 35 kg = 0,035 tấn => 9 tấn 35 kg = 9,035 tấn\nc) 400 m² = 0,04 ha => 7 ha 400 m² = 7,04 ha\nd) 8 dm² = 0,08 m² => 15 m² 8 dm² = 15,08 m²\nĐáp số: a) 5,068 km; b) 9,035 tấn; c) 7,04 ha; d) 15,08 m².",
                "answer": "a) 5,068 km; b) 9,035 tấn; c) 7,04 ha; d) 15,08 m²"
            },
            {
                "question": "**Bài 2:** Đặt tính rồi tính:\na) 42,7 x 3,6\nb) 124,8 : 32",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 42,7 x 3,6 = 153,72\nb) 124,8 : 32 = 3,9 (124 : 32 = 3 dư 28; phẩy; hạ 8 được 288 : 32 = 9)\nĐáp số: a) 153,72; b) 3,9.",
                "answer": "a) 153,72; b) 3,9"
            },
            {
                "question": "**Bài 3:** Tìm x, biết:\na) x + 25,6 = 72,15\nb) x x 3,5 = 84",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) x + 25,6 = 72,15\nx = 72,15 - 25,6\nx = 46,55\nb) x x 3,5 = 84\nx = 84 : 3,5\nx = 24\nĐáp số: a) x = 46,55; b) x = 24.",
                "answer": "a) x = 46,55; b) x = 24"
            },
            {
                "question": "**Bài 4:** Một mảnh đất hình chữ nhật có chu vi là 140 m, chiều rộng bằng 3/4 chiều dài.\na) Tính diện tích mảnh đất đó.\nb) Người ta dùng 40% diện tích mảnh đất để làm nhà, phần diện tích còn lại làm sân và vườn cây. Tính diện tích phần đất làm sân và vườn cây.",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Nửa chu vi mảnh đất là:\n140 : 2 = 70 (m)\nTổng số phần bằng nhau là:\n3 + 4 = 7 (phần)\nChiều rộng mảnh đất là:\n70 : 7 x 3 = 30 (m)\nChiều dài mảnh đất là:\n70 - 30 = 40 (m)\nDiện tích mảnh đất là:\n40 x 30 = 1200 (m²)\nb) Phần diện tích làm sân và vườn cây chiếm số phần trăm là:\n100% - 40% = 60%\nDiện tích phần đất làm sân và vườn cây là:\n1200 x 60 : 100 = 720 (m²)\nĐáp số: a) 1200 m²; b) 720 m².",
                "answer": "a) 1200 m²; b) 720 m²"
            },
            {
                "question": "**Bài 5:** Bánh xe của một xe đạp có đường kính là 0,65 m.\na) Tính chu vi của bánh xe đạp đó.\nb) Khi người đi xe đạp đi được quãng đường dài 2041 m thì bánh xe đã lăn được bao nhiêu vòng trên mặt đất?",
                "points": 1.5,
                "lineCount": 5,
                "solution": "a) Chu vi bánh xe đạp là:\n0,65 x 3,14 = 2,041 (m)\nb) Số vòng bánh xe đã lăn được là:\n2041 : 2,041 = 1000 (vòng)\nĐáp số: a) 2,041 m; b) 1000 vòng.",
                "answer": "a) 2,041 m; b) 1000 vòng"
            },
            {
                "question": "**Bài 6:** Tính giá trị của biểu thức bằng cách thuận tiện nhất:\nB = 0,25 x 6,8 x 40",
                "points": 1.0,
                "lineCount": 4,
                "solution": "B = 0,25 x 6,8 x 40\n= (0,25 x 40) x 6,8\n= 10 x 6,8\n= 68\nĐáp số: 68.",
                "answer": "68"
            }
        ]
    }

    exams["th5_b29_test3"] = {
        "title": "ĐỀ KIỂM TRA BÀI 29 (ĐỀ 3): LUYỆN TẬP CHUNG HỌC KÌ 1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            {
                "question": "**Câu 1:** Phân số 4/5 được viết dưới dạng số thập phân là:",
                "choices": ["0,45", "0,8", "0,4", "0,08"],
                "correct": 1,
                "explanation": "4/5 = 8/10 = 0,8.",
                "points": 0.5
            },
            {
                "question": "**Câu 2:** Số lớn nhất trong các số thập phân 9,08; 9,8; 9,805; 9,799 là:",
                "choices": ["9,08", "9,8", "9,805", "9,799"],
                "correct": 2,
                "explanation": "So sánh phần thập phân: 805 phần nghìn lớn hơn 800 phần nghìn và 799 phần nghìn nên 9,805 lớn nhất.",
                "points": 0.5
            },
            {
                "question": "**Câu 3:** Kết quả của phép tính 15,6 : 1,2 là:",
                "choices": ["1,3", "13", "130", "12"],
                "correct": 1,
                "explanation": "15,6 : 1,2 = 156 : 12 = 13.",
                "points": 0.5
            },
            {
                "question": "**Câu 4:** Một mảnh vườn hình thang có đáy lớn 18 m, đáy bé 12 m và chiều cao 9 m. Diện tích mảnh vườn đó là:",
                "choices": ["270 m²", "135 m²", "90 m²", "162 m²"],
                "correct": 1,
                "explanation": "Diện tích hình thang = (18 + 12) x 9 : 2 = 30 x 9 : 2 = 135 (m²).",
                "points": 0.5
            },
            {
                "question": "**Câu 5:** Chu vi hình tròn có bán kính r = 2,5 dm là:",
                "choices": ["7,85 dm", "15,7 dm", "31,4 dm", "19,625 dm"],
                "correct": 1,
                "explanation": "Chu vi hình tròn = 2,5 x 2 x 3,14 = 15,7 (dm).",
                "points": 0.5
            },
            {
                "question": "**Câu 6:** Gieo một con xúc xắc 6 mặt một lần. Khả năng xuất hiện mặt có số chấm là số nguyên tố (2; 3; 5) có tỉ số so với tổng số mặt là:",
                "choices": ["1/6", "1/3", "1/2", "2/3"],
                "correct": 2,
                "explanation": "Có 3 số nguyên tố (2, 3, 5) trong 6 mặt. Tỉ số là 3/6 = 1/2.",
                "points": 0.5
            }
        ],
        "part2": [
            {
                "question": "**Bài 1:** Đặt tính rồi tính:\na) 612,48 + 289,75\nb) 805,2 - 347,65",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 612,48 + 289,75 = 902,23\nb) 805,20 - 347,65 = 457,55\nĐáp số: a) 902,23; b) 457,55.",
                "answer": "a) 902,23; b) 457,55"
            },
            {
                "question": "**Bài 2:** Đặt tính rồi tính:\na) 54,6 x 4,5\nb) 165,6 : 36",
                "points": 1.0,
                "lineCount": 4,
                "solution": "a) 54,6 x 4,5 = 245,7\nb) 165,6 : 36 = 4,6 (165 : 36 = 4 dư 21; phẩy; hạ 6 được 216 : 36 = 6)\nĐáp số: a) 245,7; b) 4,6.",
                "answer": "a) 245,7; b) 4,6"
            },
            {
                "question": "**Bài 3:** Tính bằng cách thuận tiện nhất:\n4,56 x 7,8 + 4,56 x 2,2",
                "points": 1.0,
                "lineCount": 4,
                "solution": "4,56 x 7,8 + 4,56 x 2,2 = 4,56 x (7,8 + 2,2)\n= 4,56 x 10\n= 45,6\nĐáp số: 45,6.",
                "answer": "45,6"
            },
            {
                "question": "**Bài 4:** Một mảnh vườn hình thang có đáy bé 25 m, đáy lớn bằng 7/5 đáy bé, chiều cao là 18 m.\na) Tính diện tích mảnh vườn hình thang đó.\nb) Ở giữa vườn người ta đào một ao nuôi cá hình tròn có bán kính 4 m. Tính diện tích phần đất còn lại của vườn.",
                "points": 1.5,
                "lineCount": 6,
                "solution": "a) Độ dài đáy lớn mảnh vườn là:\n25 x 7/5 = 35 (m)\nDiện tích mảnh vườn hình thang là:\n(35 + 25) x 18 : 2 = 540 (m²)\nb) Diện tích ao cá hình tròn là:\n4 x 4 x 3,14 = 50,24 (m²)\nDiện tích phần đất còn lại của vườn là:\n540 - 50,24 = 489,76 (m²)\nĐáp số: a) 540 m²; b) 489,76 m².",
                "answer": "a) 540 m²; b) 489,76 m²"
            },
            {
                "question": "**Bài 5:** Một cửa hàng có 3 bao gạo chứa tất cả 180 kg gạo. Bao thứ nhất chứa 54,5 kg gạo. Bao thứ hai chứa nhiều hơn bao thứ nhất 6,8 kg gạo. Hỏi bao thứ ba chứa bao nhiêu ki-lô-gam gạo?",
                "points": 1.5,
                "lineCount": 6,
                "solution": "Bao gạo thứ hai chứa số ki-lô-gam gạo là:\n54,5 + 6,8 = 61,3 (kg)\nCả hai bao đầu chứa số ki-lô-gam gạo là:\n54,5 + 61,3 = 115,8 (kg)\nBao gạo thứ ba chứa số ki-lô-gam gạo là:\n180 - 115,8 = 64,2 (kg)\nĐáp số: 64,2 kg gạo.",
                "answer": "64,2 kg"
            },
            {
                "question": "**Bài 6:** Tìm một số tự nhiên có hai chữ số, biết rằng nếu viết thêm chữ số 1 vào bên phải số đó thì được số mới lớn hơn số đã cho 460 đơn vị.",
                "points": 1.0,
                "lineCount": 5,
                "solution": "Gọi số tự nhiên có hai chữ số cần tìm là ab (a khác 0; a, b là chữ số).\nKhi viết thêm chữ số 1 vào bên phải ta được số ab1.\nTheo đề bài ta có:\nab1 - ab = 460\nab x 10 + 1 - ab = 460\nab x 9 + 1 = 460\nab x 9 = 459\nab = 459 : 9\nab = 51\nVậy số tự nhiên cần tìm là 51.\nĐáp số: 51.",
                "answer": "51"
            }
        ]
    }

    return exams
