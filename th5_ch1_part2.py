# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 1: ÔN TẬP VÀ BỔ SUNG (BÀI 4 ĐẾN BÀI 6) - TOÁN 5 KNTT
Mỗi bài có đúng 3 đề kiểm tra độc lập (test1, test2, test3):
- 6 câu trắc nghiệm (part1, mỗi câu 0.5 điểm = 3.0 điểm)
- 6 câu tự luận (part2, 4 câu 1.0 đ + 2 câu 1.5 đ = 7.0 điểm, lineCount: 3 đến 6 dòng)
Tổng điểm: 10.0 điểm, thời gian: 35 phút.
"""
from th5_ch1_part1 import make_mc, make_essay

def get_ch1_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 4: PHÂN SỐ THẬP PHÂN
    # =========================================================================
    # --- Bài 4 - Đề 1 ---
    exams["th5_b4_test1"] = {
        "id": "th5_b4_test1",
        "lessonId": "th5_b4",
        "lessonNum": 4,
        "testNum": 1,
        "title": "Bài 4: Phân số thập phân - Đề số 1",
        "topic": "Phân số thập phân",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Trong các phân số sau, phân số nào là phân số thập phân?", ["$\\frac{3}{20}$", "$\\frac{7}{100}$", "$\\frac{15}{200}$", "$\\frac{9}{50}$"], 1, "Phân số thập phân có mẫu số là 10, 100, 1000... Mẫu số ở đây là 100."),
            make_mc(2, "Phân số $\\frac{3}{5}$ được viết dưới dạng phân số thập phân có mẫu số là 10 là:", ["$\\frac{6}{10}$", "$\\frac{3}{10}$", "$\\frac{15}{10}$", "$\\frac{8}{10}$"], 0, "Nhân cả tử và mẫu với 2: (3x2)/(5x2) = 6/10."),
            make_mc(3, "Viết phân số $\\frac{7}{4}$ thành phân số thập phân có mẫu số là 100:", ["$\\frac{175}{100}$", "$\\frac{70}{100}$", "$\\frac{28}{100}$", "$\\frac{140}{100}$"], 0, "Nhân cả tử và mẫu với 25: (7x25)/(4x25) = 175/100."),
            make_mc(4, "Phân số thập phân 'Tám mươi lăm phần nghìn' được viết là:", ["$\\frac{85}{100}$", "$\\frac{85}{1000}$", "$\\frac{85}{10}$", "$\\frac{85}{10000}$"], 1, "Tử số là 85, mẫu số là 1000."),
            make_mc(5, "Viết số đo $7\\text{ dm}$ dưới dạng phân số thập phân với đơn vị mét là:", ["$\\frac{7}{10}\\text{ m}$", "$\\frac{7}{100}\\text{ m}$", "$\\frac{7}{1000}\\text{ m}$", "$\\frac{70}{10}\\text{ m}$"], 0, "$1\\text{ m} = 10\\text{ dm}$ nên $7\\text{ dm} = \\frac{7}{10}\\text{ m}$."),
            make_mc(6, "Rút gọn phân số thập phân $\\frac{450}{1000}$ thành phân số thập phân có mẫu số là 100:", ["$\\frac{45}{100}$", "$\\frac{4,5}{100}$", "$\\frac{9}{100}$", "$\\frac{90}{100}$"], 0, "Chia cả tử và mẫu cho 10: 450 : 10 / 1000 : 10 = 45/100.")
        ],
        "part2": [
            make_essay(1, "Chuyển các phân số sau thành phân số thập phân:\na) $\\frac{9}{25}$\nb) $\\frac{11}{20}$", "a) $\\frac{9}{25} = \\frac{9 \\times 4}{25 \\times 4} = \\frac{36}{100}$\nb) $\\frac{11}{20} = \\frac{11 \\times 5}{20 \\times 5} = \\frac{55}{100}$", "a) 36/100; b) 55/100", 3, 1.0),
            make_essay(2, "Chuyển các phân số sau thành phân số thập phân:\na) $\\frac{64}{800}$\nb) $\\frac{42}{300}$", "a) $\\frac{64}{800} = \\frac{64 : 8}{800 : 8} = \\frac{8}{100}$\nb) $\\frac{42}{300} = \\frac{42 : 3}{300 : 3} = \\frac{14}{100}$", "a) 8/100; b) 14/100", 3, 1.0),
            make_essay(3, "Viết các số đo sau dưới dạng phân số thập phân:\na) $9\\text{ cm}$ theo đơn vị mét;\nb) $350\\text{ g}$ theo đơn vị ki-lô-gam.", "a) Vì $1\\text{ m} = 100\\text{ cm}$ nên $9\\text{ cm} = \\frac{9}{100}\\text{ m}$.\nb) Vì $1\\text{ kg} = 1000\\text{ g}$ nên $350\\text{ g} = \\frac{350}{1000}\\text{ kg}$ (hoặc $\\frac{35}{100}\\text{ kg}$).", "a) 9/100 m; b) 350/1000 kg", 4, 1.0),
            make_essay(4, "So sánh hai phân số thập phân sau:\na) $\\frac{45}{100}$ và $\\frac{450}{1000}$\nb) $\\frac{8}{10}$ và $\\frac{79}{100}$", "a) $\\frac{450}{1000} = \\frac{450 : 10}{1000 : 10} = \\frac{45}{100}$. Vậy $\\frac{45}{100} = \\frac{450}{1000}$.\nb) $\\frac{8}{10} = \\frac{80}{100}$. Vì $\\frac{80}{100} > \\frac{79}{100}$ nên $\\frac{8}{10} > \\frac{79}{100}$.", "a) =; b) >", 4, 1.0),
            make_essay(5, "Một cửa hàng có $1\\text{ tấn}$ gạo. Buổi sáng bán được $\\frac{35}{100}\\text{ tấn}$, buổi chiều bán được $\\frac{4}{10}\\text{ tấn}$. Hỏi sau hai buổi cửa hàng còn lại bao nhiêu phần của tấn gạo? Hãy viết kết quả dưới dạng phân số thập phân.", "Quy đồng: $\\frac{4}{10} = \\frac{40}{100}\\text{ tấn}$.\nCả hai buổi cửa hàng đã bán được: $\\frac{35}{100} + \\frac{40}{100} = \\frac{75}{100}\\text{ (tấn gạo)}$.\nSố gạo còn lại là: $1 - \\frac{75}{100} = \\frac{100}{100} - \\frac{75}{100} = \\frac{25}{100}\\text{ (tấn gạo)}$.", "25/100 tấn gạo", 4, 1.5),
            make_essay(6, "Một mảnh đất hình chữ nhật có chiều dài $\\frac{4}{5}\\text{ km}$, chiều rộng bằng $\\frac{1}{4}$ chiều dài. Tính chu vi và diện tích mảnh đất đó, kết quả biểu thị dưới dạng phân số thập phân có mẫu số là 10, 100 hoặc 1000.", "Chiều rộng mảnh đất là: $\\frac{4}{5} \\times \\frac{1}{4} = \\frac{1}{5}\\text{ (km)}$.\nChu vi mảnh đất là: $(\\frac{4}{5} + \\frac{1}{5}) \\times 2 = 1 \\times 2 = 2\\text{ (km)} = \\frac{20}{10}\\text{ km}$.\nDiện tích mảnh đất là: $\\frac{4}{5} \\times \\frac{1}{5} = \\frac{4}{25}\\text{ (km$^2$)}$.\nĐổi sang phân số thập phân: $\\frac{4}{25} = \\frac{4 \\times 4}{25 \\times 4} = \\frac{16}{100}\\text{ (km$^2$)}$.", "Chu vi: 20/10 km (hoặc 2 km); Diện tích: 16/100 km$^2$", 5, 1.5)
        ]
    }

    # --- Bài 4 - Đề 2 ---
    exams["th5_b4_test2"] = {
        "id": "th5_b4_test2",
        "lessonId": "th5_b4",
        "lessonNum": 4,
        "testNum": 2,
        "title": "Bài 4: Phân số thập phân - Đề số 2",
        "topic": "Phân số thập phân",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Trong các phân số sau, phân số nào KHÔNG PHẢI là phân số thập phân?", ["$\\frac{7}{10}$", "$\\frac{19}{100}$", "$\\frac{23}{500}$", "$\\frac{41}{1000}$"], 2, "Phân số 23/500 có mẫu số là 500 nên không phải phân số thập phân."),
            make_mc(2, "Chuyển phân số $\\frac{7}{2}$ thành phân số thập phân có mẫu số 10 ta được:", ["$\\frac{35}{10}$", "$\\frac{14}{10}$", "$\\frac{21}{10}$", "$\\frac{70}{10}$"], 0, "(7x5)/(2x5) = 35/10."),
            make_mc(3, "Chuyển phân số $\\frac{3}{8}$ thành phân số thập phân có mẫu số 1000:", ["$\\frac{375}{1000}$", "$\\frac{300}{1000}$", "$\\frac{125}{1000}$", "$\\frac{250}{1000}$"], 0, "(3x125)/(8x125) = 375/1000."),
            make_mc(4, "Viết số đo $45\\text{ m}^2$ dưới dạng phân số thập phân với đơn vị đề-ca-mét vuông ($\\text{dam}^2$) là:", ["$\\frac{45}{10}\\text{ dam}^2$", "$\\frac{45}{100}\\text{ dam}^2$", "$\\frac{45}{1000}\\text{ dam}^2$", "$\\frac{450}{100}\\text{ dam}^2$"], 1, "$1\\text{ dam}^2 = 100\\text{ m}^2$ nên $45\\text{ m}^2 = \\frac{45}{100}\\text{ dam}^2$."),
            make_mc(5, "Điền dấu thích hợp: $\\frac{6}{10} + \\frac{25}{100} \\dots \\frac{85}{100}$:", ["=", ">", "<", "Không so sánh được"], 0, "6/10 = 60/100. 60/100 + 25/100 = 85/100."),
            make_mc(6, "Phân số thập phân $\\frac{125}{100}$ đọc là:", [
                "Một trăm hai mươi lăm phần trăm",
                "Một trăm hai mươi lăm phần mười",
                "Mười hai phần trăm",
                "Một trăm hai mươi lăm phần nghìn"
            ], 0, "Tử số là 125, mẫu số là 100 đọc là 'Một trăm hai mươi lăm phần trăm'.")
        ],
        "part2": [
            make_essay(1, "Chuyển các phân số sau thành phân số thập phân:\na) $\\frac{13}{5}$\nb) $\\frac{7}{4}$", "a) $\\frac{13}{5} = \\frac{13 \\times 2}{5 \\times 2} = \\frac{26}{10}$\nb) $\\frac{7}{4} = \\frac{7 \\times 25}{4 \\times 25} = \\frac{175}{100}$", "a) 26/10; b) 175/100", 3, 1.0),
            make_essay(2, "Chuyển các phân số sau thành phân số thập phân có mẫu số là 100:\na) $\\frac{21}{300}$\nb) $\\frac{72}{600}$", "a) $\\frac{21}{300} = \\frac{21 : 3}{300 : 3} = \\frac{7}{100}$\nb) $\\frac{72}{600} = \\frac{72 : 6}{600 : 6} = \\frac{12}{100}$", "a) 7/100; b) 12/100", 3, 1.0),
            make_essay(3, "Viết các số đo sau dưới dạng phân số thập phân:\na) $8\\text{ dm}$ theo đơn vị mét;\nb) $25\\text{ kg}$ theo đơn vị tạ.", "a) $8\\text{ dm} = \\frac{8}{10}\\text{ m}$.\nb) Vì $1\\text{ tạ} = 100\\text{ kg}$ nên $25\\text{ kg} = \\frac{25}{100}\\text{ tạ}$.", "a) 8/10 m; b) 25/100 tạ", 3, 1.0),
            make_essay(4, "Sắp xếp các phân số thập phân sau theo thứ tự từ bé đến lớn:\n$\\frac{7}{10}; \\frac{65}{100}; \\frac{72}{100}; \\frac{600}{1000}$.", "Quy đồng mẫu số chung là 100:\n$\\frac{7}{10} = \\frac{70}{100}$; $\\frac{600}{1000} = \\frac{60}{100}$.\nVì $\\frac{60}{100} < \\frac{65}{100} < \\frac{70}{100} < \\frac{72}{100}$ nên: $\\frac{600}{1000} < \\frac{65}{100} < \\frac{7}{10} < \\frac{72}{100}$.", "600/1000; 65/100; 7/10; 72/100", 4, 1.0),
            make_essay(5, "Một lớp học có 40 học sinh, trong đó có 24 học sinh nữ. Hỏi số học sinh nữ chiếm bao nhiêu phần tổng số học sinh của lớp? Hãy viết kết quả dưới dạng phân số thập phân có mẫu số là 100.", "Tỉ số giữa số học sinh nữ và số học sinh cả lớp là: $\\frac{24}{40}$.\nRút gọn: $\\frac{24}{40} = \\frac{24 : 8}{40 : 8} = \\frac{3}{5}$.\nChuyển sang phân số thập phân mẫu số 100:\n$\\frac{3}{5} = \\frac{3 \\times 20}{5 \\times 20} = \\frac{60}{100}$.\nVậy số học sinh nữ chiếm $\\frac{60}{100}$ tổng số học sinh của lớp.", "60/100", 4, 1.5),
            make_essay(6, "Bác Nam có một can dầu chứa $5\\text{ lít}$. Lần thứ nhất bác dùng $\\frac{15}{10}\\text{ lít}$ dầu, lần thứ hai bác dùng $\\frac{175}{100}\\text{ lít}$ dầu. Hỏi trong can còn lại bao nhiêu lít dầu? Hãy viết kết quả dưới dạng phân số thập phân có mẫu số là 100.", "Đổi: $5\\text{ lít} = \\frac{500}{100}\\text{ lít}$; $\\frac{15}{10}\\text{ lít} = \\frac{150}{100}\\text{ lít}$.\nTổng lượng dầu bác Nam đã dùng sau 2 lần là:\n$\\frac{150}{100} + \\frac{175}{100} = \\frac{325}{100}\\text{ (lít)}$.\nLượng dầu còn lại trong can là:\n$\\frac{500}{100} - \\frac{325}{100} = \\frac{175}{100}\\text{ (lít)}$.", "175/100 lít", 5, 1.5)
        ]
    }

    # --- Bài 4 - Đề 3 ---
    exams["th5_b4_test3"] = {
        "id": "th5_b4_test3",
        "lessonId": "th5_b4",
        "lessonNum": 4,
        "testNum": 3,
        "title": "Bài 4: Phân số thập phân - Đề số 3",
        "topic": "Phân số thập phân",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số nào dưới đây có thể chuyển thành phân số thập phân có mẫu số là 10?", ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{7}$", "$\\frac{1}{9}$"], 0, "1/2 = 5/10."),
            make_mc(2, "Số thích hợp điền vào ô trống để $\\frac{12}{50} = \\frac{\\square}{100}$ là:", ["24", "12", "6", "48"], 0, "Nhân cả tử và mẫu với 2: 12 x 2 = 24."),
            make_mc(3, "Chuyển phân số $\\frac{19}{200}$ thành phân số thập phân có mẫu số là 1000:", ["$\\frac{95}{1000}$", "$\\frac{38}{1000}$", "$\\frac{190}{1000}$", "$\\frac{76}{1000}$"], 0, "Nhân cả tử và mẫu với 5: 19 x 5 = 95, 200 x 5 = 1000."),
            make_mc(4, "Viết số đo $125\\text{ m}$ dưới dạng phân số thập phân với đơn vị ki-lô-mét là:", ["$\\frac{125}{10}\\text{ km}$", "$\\frac{125}{100}\\text{ km}$", "$\\frac{125}{1000}\\text{ km}$", "$\\frac{125}{10000}\\text{ km}$"], 2, "$1\\text{ km} = 1000\\text{ m}$ nên $125\\text{ m} = \\frac{125}{1000}\\text{ km}$."),
            make_mc(5, "Tổng $\\frac{3}{10} + \\frac{4}{100} + \\frac{5}{1000}$ viết thành phân số thập phân là:", ["$\\frac{345}{1000}$", "$\\frac{12}{1000}$", "$\\frac{345}{100}$", "$\\frac{345}{10}$"], 0, "3/10 = 300/1000; 4/100 = 40/1000; tổng = 345/1000."),
            make_mc(6, "Trong các phân số sau, phân số nào bé hơn $\\frac{5}{10}$?", ["$\\frac{55}{100}$", "$\\frac{48}{100}$", "$\\frac{6}{10}$", "$\\frac{500}{1000}$"], 1, "5/10 = 50/100. 48/100 < 50/100.")
        ],
        "part2": [
            make_essay(1, "Chuyển các phân số sau thành phân số thập phân:\na) $\\frac{9}{8}$\nb) $\\frac{17}{50}$", "a) $\\frac{9}{8} = \\frac{9 \\times 125}{8 \\times 125} = \\frac{1125}{1000}$\nb) $\\frac{17}{50} = \\frac{17 \\times 2}{50 \\times 2} = \\frac{34}{100}$", "a) 1125/1000; b) 34/100", 3, 1.0),
            make_essay(2, "Chuyển các phân số sau thành phân số thập phân có mẫu số là 10:\na) $\\frac{32}{40}$\nb) $\\frac{28}{70}$", "a) $\\frac{32}{40} = \\frac{32 : 4}{40 : 4} = \\frac{8}{10}$\nb) $\\frac{28}{70} = \\frac{28 : 7}{70 : 7} = \\frac{4}{10}$", "a) 8/10; b) 4/10", 3, 1.0),
            make_essay(3, "Viết các số đo sau dưới dạng phân số thập phân:\na) $65\\text{ cm}^2$ theo đơn vị đề-xi-mét vuông ($\\text{dm}^2$);\nb) $18\\text{ phút}$ theo đơn vị giờ.", "a) Vì $1\\text{ dm}^2 = 100\\text{ cm}^2$ nên $65\\text{ cm}^2 = \\frac{65}{100}\\text{ dm}^2$.\nb) $18\\text{ phút} = \\frac{18}{60}\\text{ giờ} = \\frac{18 : 6}{60 : 6}\\text{ giờ} = \\frac{3}{10}\\text{ giờ}$.", "a) 65/100 dm$^2$; b) 3/10 giờ", 4, 1.0),
            make_essay(4, "Tìm phân số thập phân $\\frac{x}{100}$ biết: $\\frac{1}{4} < \\frac{x}{100} < \\frac{3}{10}$.", "Quy đồng mẫu số chung là 100:\n$\\frac{1}{4} = \\frac{25}{100}$; $\\frac{3}{10} = \\frac{30}{100}$.\nTa có: $\\frac{25}{100} < \\frac{x}{100} < \\frac{30}{100}$.\nSuy ra: $25 < x < 30$.\nDo $x$ là số tự nhiên nên $x \\in \\{26; 27; 28; 29\\}$.\nCác phân số thập phân thỏa mãn: $\\frac{26}{100}; \\frac{27}{100}; \\frac{28}{100}; \\frac{29}{100}$.", "26/100; 27/100; 28/100; 29/100", 4, 1.0),
            make_essay(5, "Một đoàn xe vận tải chở $10\\text{ tấn}$ hàng. Xe thứ nhất chở $\\frac{25}{10}\\text{ tấn}$, xe thứ hai chở nhiều hơn xe thứ nhất $\\frac{8}{10}\\text{ tấn}$. Hỏi cả hai xe đã chở được bao nhiêu phần mười của tổng số hàng?", "Xe thứ hai chở số tấn hàng là: $\\frac{25}{10} + \\frac{8}{10} = \\frac{33}{10}\\text{ (tấn)}$.\nCả hai xe chở được: $\\frac{25}{10} + \\frac{33}{10} = \\frac{58}{10}\\text{ (tấn)}$.\nCả hai xe chở được số phần của tổng số hàng ($10\\text{ tấn}$) là:\n$\\frac{58}{10} : 10 = \\frac{58}{100}$ (tổng số hàng).", "58/100 tổng số hàng", 4, 1.5),
            make_essay(6, "Một tấm vải dài $20\\text{ m}$. Lần thứ nhất người ta cắt lấy $\\frac{3}{5}$ tấm vải. Lần thứ hai cắt lấy $\\frac{1}{4}$ số vải còn lại. Hỏi sau hai lần cắt, tấm vải còn lại bao nhiêu mét? Viết phân số chỉ số phần tấm vải còn lại dưới dạng phân số thập phân.", "Lần thứ nhất cắt: $20 \\times \\frac{3}{5} = 12\\text{ (m)}$.\nSố vải còn lại sau lần thứ nhất là: $20 - 12 = 8\\text{ (m)}$.\nLần thứ hai cắt: $8 \\times \\frac{1}{4} = 2\\text{ (m)}$.\nSố mét vải còn lại sau 2 lần là: $8 - 2 = 6\\text{ (m)}$.\nPhân số chỉ số phần vải còn lại so với tấm ban đầu là:\n$\\frac{6}{20} = \\frac{6 \\times 5}{20 \\times 5} = \\frac{30}{100}$.", "6 m vải; 30/100 tấm vải", 5, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 5: ÔN TẬP CÁC PHÉP TÍNH VỚI PHÂN SỐ
    # =========================================================================
    # --- Bài 5 - Đề 1 ---
    exams["th5_b5_test1"] = {
        "id": "th5_b5_test1",
        "lessonId": "th5_b5",
        "lessonNum": 5,
        "testNum": 1,
        "title": "Bài 5: Ôn tập các phép tính với phân số - Đề số 1",
        "topic": "Ôn tập các phép tính với phân số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép cộng $\\frac{2}{5} + \\frac{1}{3}$ là:", ["$\\frac{3}{8}$", "$\\frac{11}{15}$", "$\\frac{3}{15}$", "$\\frac{7}{15}$"], 1, "Quy đồng mẫu số chung là 15: 6/15 + 5/15 = 11/15."),
            make_mc(2, "Kết quả của phép trừ $2 - \\frac{3}{4}$ là:", ["$\\frac{1}{4}$", "$\\frac{5}{4}$", "$\\frac{3}{4}$", "$\\frac{7}{4}$"], 1, "2 = 8/4. 8/4 - 3/4 = 5/4."),
            make_mc(3, "Kết quả của phép nhân $\\frac{4}{7} \\times \\frac{14}{5}$ là:", ["$\\frac{8}{5}$", "$\\frac{56}{35}$", "$\\frac{2}{5}$", "$\\frac{4}{5}$"], 0, "Rút gọn chéo 14 với 7 được 2: (4 x 2)/5 = 8/5."),
            make_mc(4, "Kết quả của phép chia $\\frac{5}{9} : \\frac{2}{3}$ là:", ["$\\frac{10}{27}$", "$\\frac{5}{6}$", "$\\frac{6}{5}$", "$\\frac{15}{18}$"], 1, "5/9 x 3/2 = 15/18 = 5/6."),
            make_mc(5, "Tìm $x$, biết: $x \\times \\frac{3}{5} = \\frac{9}{10}$. Giá trị của $x$ là:", ["$\\frac{3}{2}$", "$\\frac{2}{3}$", "$\\frac{27}{50}$", "$\\frac{1}{2}$"], 0, "x = 9/10 : 3/5 = 9/10 x 5/3 = 3/2."),
            make_mc(6, "Một tấm kính hình chữ nhật có chiều dài $\\frac{4}{5}\\text{ m}$, chiều rộng $\\frac{1}{2}\\text{ m}$. Diện tích tấm kính đó là:", ["$\\frac{5}{7}\\text{ m}^2$", "$\\frac{2}{5}\\text{ m}^2$", "$\\frac{3}{10}\\text{ m}^2$", "$\\frac{4}{7}\\text{ m}^2$"], 1, "Diện tích = 4/5 x 1/2 = 4/10 = 2/5 m$^2$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của các biểu thức sau:\na) $\\frac{5}{6} + \\frac{3}{8}$\nb) $\\frac{7}{4} - \\frac{5}{6}$", "a) MSC = 24. $\\frac{5}{6} + \\frac{3}{8} = \\frac{20}{24} + \\frac{9}{24} = \\frac{29}{24}$.\nb) MSC = 12. $\\frac{7}{4} - \\frac{5}{6} = \\frac{21}{12} - \\frac{10}{12} = \\frac{11}{12}$.", "a) 29/24; b) 11/12", 4, 1.0),
            make_essay(2, "Tính giá trị của các phép tính sau (rút gọn nếu có thể):\na) $\\frac{15}{16} \\times \\frac{8}{25}$\nb) $\\frac{9}{14} : \\frac{6}{7}$", "a) $\\frac{15 \\times 8}{16 \\times 25} = \\frac{(3 \\times 5) \\times 8}{(2 \\times 8) \\times (5 \\times 5)} = \\frac{3}{10}$.\nb) $\\frac{9}{14} \\times \\frac{7}{6} = \\frac{9 \\times 7}{14 \\times 6} = \\frac{3 \\times 1}{2 \\times 2} = \\frac{3}{4}$.", "a) 3/10; b) 3/4", 4, 1.0),
            make_essay(3, "Tính bằng cách thuận tiện nhất:\na) $\\frac{3}{7} \\times \\frac{5}{9} + \\frac{3}{7} \\times \\frac{4}{9}$\nb) $\\frac{8}{15} \\times \\frac{3}{4} \\times \\frac{5}{8}$", "a) $\\frac{3}{7} \\times (\\frac{5}{9} + \\frac{4}{9}) = \\frac{3}{7} \\times 1 = \\frac{3}{7}$.\nb) $(\\frac{8}{15} \\times \\frac{5}{8}) \\times \\frac{3}{4} = \\frac{1}{3} \\times \\frac{3}{4} = \\frac{1}{4}$.", "a) 3/7; b) 1/4", 4, 1.0),
            make_essay(4, "Tìm $x$, biết:\na) $x - \\frac{2}{3} = \\frac{5}{12}$\nb) $\\frac{4}{5} : x = \\frac{8}{15}$", "a) $x = \\frac{5}{12} + \\frac{2}{3} = \\frac{5}{12} + \\frac{8}{12} = \\frac{13}{12}$.\nb) $x = \\frac{4}{5} : \\frac{8}{15} = \\frac{4}{5} \\times \\frac{15}{8} = \\frac{3}{2}$.", "a) x = 13/12; b) x = 3/2", 4, 1.0),
            make_essay(5, "Một cửa hàng có $240\\text{ kg}$ đường. Ngày thứ nhất cửa hàng bán được $\\frac{1}{3}$ số đường, ngày thứ hai bán được $\\frac{3}{8}$ số đường còn lại. Hỏi sau hai ngày cửa hàng còn lại bao nhiêu ki-lô-gam đường?", "Ngày thứ nhất bán được: $240 \\times \\frac{1}{3} = 80\\text{ (kg)}$.\nSố đường còn lại sau ngày thứ nhất là: $240 - 80 = 160\\text{ (kg)}$.\nNgày thứ hai bán được: $160 \\times \\frac{3}{8} = 60\\text{ (kg)}$.\nSau hai ngày, cửa hàng còn lại số ki-lô-gam đường là:\n$160 - 60 = 100\\text{ (kg)}$.", "100 kg đường", 5, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$S = \\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\frac{1}{3 \\times 4} + \\dots + \\frac{1}{9 \\times 10}$", "Ta có: $\\frac{1}{n \\times (n + 1)} = \\frac{1}{n} - \\frac{1}{n + 1}$.\nDo đó:\n$S = (1 - \\frac{1}{2}) + (\\frac{1}{2} - \\frac{1}{3}) + (\\frac{1}{3} - \\frac{1}{4}) + \\dots + (\\frac{1}{9} - \\frac{1}{10})$\n$S = 1 - \\frac{1}{10} = \\frac{9}{10}$.", "9/10", 4, 1.5)
        ]
    }

    # --- Bài 5 - Đề 2 ---
    exams["th5_b5_test2"] = {
        "id": "th5_b5_test2",
        "lessonId": "th5_b5",
        "lessonNum": 5,
        "testNum": 2,
        "title": "Bài 5: Ôn tập các phép tính với phân số - Đề số 2",
        "topic": "Ôn tập các phép tính với phân số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $\\frac{5}{12} + \\frac{7}{18}$ là:", ["$\\frac{12}{30}$", "$\\frac{29}{36}$", "$\\frac{19}{36}$", "$\\frac{35}{36}$"], 1, "MSC = 36. 15/36 + 14/36 = 29/36."),
            make_mc(2, "Kết quả của phép tính $\\frac{9}{14} - \\frac{2}{7}$ là:", ["$\\frac{5}{14}$", "$\\frac{7}{7}$", "$\\frac{1}{2}$", "$\\frac{5}{7}$"], 0, "9/14 - 4/14 = 5/14."),
            make_mc(3, "Giá trị của biểu thức $\\frac{7}{10} \\times 5$ là:", ["$\\frac{7}{50}$", "$\\frac{35}{50}$", "$\\frac{7}{2}$", "$\\frac{12}{10}$"], 2, "7/10 x 5 = 35/10 = 7/2."),
            make_mc(4, "Một hình vuông có cạnh dài $\\frac{3}{4}\\text{ m}$. Chu vi hình vuông đó là:", ["$\\frac{9}{16}\\text{ m}$", "$3\\text{ m}$", "$\\frac{7}{4}\\text{ m}$", "$\\frac{3}{2}\\text{ m}$"], 1, "Chu vi = 3/4 x 4 = 3 m."),
            make_mc(5, "Tìm số nghịch đảo của phân số $\\frac{5}{8}$:", ["$\\frac{8}{5}$", "$-\\frac{5}{8}$", "$\\frac{1}{8}$", "$\\frac{5}{1}$"], 0, "Số nghịch đảo của 5/8 là 8/5."),
            make_mc(6, "Giá trị của biểu thức $\\frac{2}{3} : \\frac{4}{9} \\times \\frac{1}{2}$ là:", ["$\\frac{3}{4}$", "$\\frac{4}{3}$", "$\\frac{1}{3}$", "$3$"], 0, "2/3 x 9/4 x 1/2 = 3/2 x 1/2 = 3/4.")
        ],
        "part2": [
            make_essay(1, "Thực hiện phép tính:\na) $\\frac{4}{9} + \\frac{5}{6}$\nb) $\\frac{8}{5} - \\frac{3}{4}$", "a) MSC = 18. $\\frac{4}{9} + \\frac{5}{6} = \\frac{8}{18} + \\frac{15}{18} = \\frac{23}{18}$.\nb) MSC = 20. $\\frac{8}{5} - \\frac{3}{4} = \\frac{32}{20} - \\frac{15}{20} = \\frac{17}{20}$.", "a) 23/18; b) 17/20", 4, 1.0),
            make_essay(2, "Tính:\na) $\\frac{21}{25} \\times \\frac{10}{14}$\nb) $\\frac{5}{12} : \\frac{15}{16}$", "a) $\\frac{21 \\times 10}{25 \\times 14} = \\frac{3 \\times 7 \\times 2 \\times 5}{5 \\times 5 \\times 2 \\times 7} = \\frac{3}{5}$.\nb) $\\frac{5}{12} \\times \\frac{16}{15} = \\frac{5 \\times 16}{12 \\times 15} = \\frac{1 \\times 4}{3 \\times 3} = \\frac{4}{9}$.", "a) 3/5; b) 4/9", 4, 1.0),
            make_essay(3, "Tính bằng cách thuận tiện nhất:\na) $\\frac{11}{19} \\times \\frac{8}{13} + \\frac{11}{19} \\times \\frac{5}{13}$\nb) $\\frac{5}{7} \\times \\frac{12}{17} + \\frac{5}{7} \\times \\frac{5}{17}$", "a) $\\frac{11}{19} \\times (\\frac{8}{13} + \\frac{5}{13}) = \\frac{11}{19} \\times 1 = \\frac{11}{19}$.\nb) $\\frac{5}{7} \\times (\\frac{12}{17} + \\frac{5}{17}) = \\frac{5}{7} \\times 1 = \\frac{5}{7}$.", "a) 11/19; b) 5/7", 4, 1.0),
            make_essay(4, "Tìm $x$, biết: $x + \\frac{3}{5} \\times \\frac{5}{6} = \\frac{7}{4}$.", "$x + \\frac{1}{2} = \\frac{7}{4}$\n$x = \\frac{7}{4} - \\frac{1}{2} = \\frac{7}{4} - \\frac{2}{4} = \\frac{5}{4}$.", "x = 5/4", 3, 1.0),
            make_essay(5, "Một mảnh đất hình chữ nhật có chu vi là $60\\text{ m}$, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Người ta dùng $\\frac{3}{5}$ diện tích mảnh đất để trồng rau. Tính diện tích phần đất trồng rau.", "Nửa chu vi mảnh đất là: $60 : 2 = 30\\text{ (m)}$.\nTổng số phần bằng nhau: $2 + 3 = 5\\text{ (phần)}$.\nChiều dài mảnh đất: $30 : 5 \\times 3 = 18\\text{ (m)}$.\nChiều rộng mảnh đất: $30 - 18 = 12\\text{ (m)}$.\nDiện tích mảnh đất: $18 \\times 12 = 216\\text{ (m$^2$)}$.\nDiện tích đất trồng rau là: $216 \\times \\frac{3}{5} = \\frac{648}{5} = 129,6\\text{ (m$^2$)}$.", "129,6 m$^2$ (hoặc 648/5 m$^2$)", 5, 1.5),
            make_essay(6, "Bác Ba có một thửa ruộng. Năm nay bác thu hoạch được một số thóc. Đợt 1 bác bán đi $\\frac{1}{4}$ tổng số thóc. Đợt 2 bác bán tiếp $\\frac{2}{3}$ số thóc còn lại sau đợt 1 thì trong kho còn lại $600\\text{ kg}$ thóc. Hỏi cả vụ mùa bác Ba thu hoạch được bao nhiêu tạ thóc?", "Phân số chỉ số thóc còn lại sau đợt 1 là: $1 - \\frac{1}{4} = \\frac{3}{4}$ (tổng số thóc).\nPhân số chỉ số thóc đợt 2 bán được là: $\\frac{3}{4} \\times \\frac{2}{3} = \\frac{1}{2}$ (tổng số thóc).\nPhân số chỉ số thóc còn lại sau 2 đợt là: $\\frac{3}{4} - \\frac{1}{2} = \\frac{1}{4}$ (tổng số thóc).\nTổng số thóc bác Ba thu hoạch được là: $600 : \\frac{1}{4} = 2 400\\text{ (kg)}$.\nĐổi $2 400\\text{ kg} = 24\\text{ tạ thóc}$.", "24 tạ thóc", 5, 1.5)
        ]
    }

    # --- Bài 5 - Đề 3 ---
    exams["th5_b5_test3"] = {
        "id": "th5_b5_test3",
        "lessonId": "th5_b5",
        "lessonNum": 5,
        "testNum": 3,
        "title": "Bài 5: Ôn tập các phép tính với phân số - Đề số 3",
        "topic": "Ôn tập các phép tính với phân số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{7}{15} + \\frac{4}{5}$ bằng:", ["$\\frac{19}{15}$", "$\\frac{11}{20}$", "$\\frac{11}{15}$", "$\\frac{15}{15}$"], 0, "7/15 + 12/15 = 19/15."),
            make_mc(2, "Giá trị của biểu thức $3 : \\frac{3}{4}$ là:", ["$\\frac{9}{4}$", "$\\frac{1}{4}$", "$4$", "$\\frac{4}{9}$"], 2, "3 x 4/3 = 4."),
            make_mc(3, "Biết $\\frac{3}{4}$ quãng đường dài $12\\text{ km}$. Quãng đường đó dài tất cả là:", ["$9\\text{ km}$", "$16\\text{ km}$", "$15\\text{ km}$", "$18\\text{ km}$"], 1, "Quãng đường dài: 12 : 3/4 = 16 km."),
            make_mc(4, "Kết quả của biểu thức $(\\frac{1}{2} + \\frac{1}{3}) : \\frac{5}{6}$ là:", ["$1$", "$\\frac{25}{36}$", "$\\frac{5}{6}$", "$\\frac{6}{5}$"], 0, "(3/6 + 2/6) : 5/6 = 5/6 : 5/6 = 1."),
            make_mc(5, "Tìm $x$, biết: $x - \\frac{1}{4} = \\frac{5}{8}$. Giá trị của $x$ là:", ["$\\frac{7}{8}$", "$\\frac{3}{8}$", "$\\frac{6}{12}$", "$\\frac{9}{8}$"], 0, "x = 5/8 + 2/8 = 7/8."),
            make_mc(6, "Một tấm thảm hình chữ nhật có diện tích $\\frac{9}{10}\\text{ m}^2$, chiều rộng là $\\frac{3}{5}\\text{ m}$. Chiều dài tấm thảm là:", ["$\\frac{3}{2}\\text{ m}$", "$\\frac{27}{50}\\text{ m}$", "$\\frac{2}{3}\\text{ m}$", "$\\frac{6}{5}\\text{ m}$"], 0, "Chiều dài = 9/10 : 3/5 = 9/10 x 5/3 = 3/2 m.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\na) $2 - \\frac{5}{9} - \\frac{4}{9}$\nb) $\\frac{7}{10} + \\frac{3}{4} \\times \\frac{2}{5}$", "a) $2 - (\\frac{5}{9} + \\frac{4}{9}) = 2 - 1 = 1$.\nb) $\\frac{7}{10} + \\frac{3}{10} = \\frac{10}{10} = 1$.", "a) 1; b) 1", 3, 1.0),
            make_essay(2, "Thực hiện phép tính bằng cách hợp lí:\na) $\\frac{17}{23} \\times \\frac{9}{16} + \\frac{17}{23} \\times \\frac{7}{16}$\nb) $\\frac{5}{9} \\times \\frac{7}{13} - \\frac{5}{9} \\times \\frac{3}{13}$", "a) $\\frac{17}{23} \\times (\\frac{9}{16} + \\frac{7}{16}) = \\frac{17}{23} \\times 1 = \\frac{17}{23}$.\nb) $\\frac{5}{9} \\times (\\frac{7}{13} - \\frac{3}{13}) = \\frac{5}{9} \\times \\frac{4}{13} = \\frac{20}{117}$.", "a) 17/23; b) 20/117", 4, 1.0),
            make_essay(3, "Tìm $y$, biết:\na) $y : \\frac{2}{5} = \\frac{15}{16}$\nb) $\\frac{7}{8} - y = \\frac{1}{3} : 2$", "a) $y = \\frac{15}{16} \\times \\frac{2}{5} = \\frac{3}{8}$.\nb) $\\frac{7}{8} - y = \\frac{1}{6} \\Rightarrow y = \\frac{7}{8} - \\frac{1}{6} = \\frac{21}{24} - \\frac{4}{24} = \\frac{17}{24}$.", "a) y = 3/8; b) y = 17/24", 4, 1.0),
            make_essay(4, "Một bể nước có thể tích $3 600\\text{ lít}$. Giờ thứ nhất vòi chảy được $\\frac{2}{9}$ thể tích bể, giờ thứ hai vòi chảy được $\\frac{1}{4}$ thể tích bể. Hỏi sau hai giờ, vòi nước đã chảy vào bể bao nhiêu lít nước?", "Cả hai giờ vòi chảy được số phần thể tích bể là:\n$\\frac{2}{9} + \\frac{1}{4} = \\frac{8}{36} + \\frac{9}{36} = \\frac{17}{36}$ (thể tích bể).\nSố lít nước chảy vào bể sau hai giờ là:\n$3 600 \\times \\frac{17}{36} = 1 700\\text{ (lít)}$.", "1 700 lít nước", 4, 1.0),
            make_essay(5, "Một đoàn xe chở lương thực gồm hai tổ. Tổ một chở được $\\frac{3}{8}$ tổng số lương thực, tổ hai chở được nhiều hơn tổ một $\\frac{1}{6}$ tổng số lương thực. Hỏi cả hai tổ chở được bao nhiêu phần của tổng số lương thực và tổ nào chở nhiều hơn?", "Tổ hai chở được số phần lương thực là:\n$\\frac{3}{8} + \\frac{1}{6} = \\frac{9}{24} + \\frac{4}{24} = \\frac{13}{24}$ (tổng số lương thực).\nCả hai tổ chở được số phần lương thực là:\n$\\frac{9}{24} + \\frac{13}{24} = \\frac{22}{24} = \\frac{11}{12}$ (tổng số lương thực).\nVì tổ hai chở nhiều hơn tổ một $\\frac{1}{6}$ nên tổ hai chở nhiều hơn.", "11/12 tổng số lương thực; Tổ hai chở nhiều hơn", 4, 1.5),
            make_essay(6, "Tính giá trị của biểu thức $A = (1 - \\frac{1}{2}) \\times (1 - \\frac{1}{3}) \\times (1 - \\frac{1}{4}) \\times \\dots \\times (1 - \\frac{1}{50})$.", "Ta có:\n$1 - \\frac{1}{2} = \\frac{1}{2}$; $1 - \\frac{1}{3} = \\frac{2}{3}$; $1 - \\frac{1}{4} = \\frac{3}{4}$; ...; $1 - \\frac{1}{50} = \\frac{49}{50}$.\nThay vào biểu thức:\n$A = \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{3}{4} \\times \\dots \\times \\frac{49}{50}$.\nRút gọn các thừa số giống nhau ở tử và mẫu liên tiếp:\n$A = \\frac{1}{50}$.", "A = 1/50", 4, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 6: BÀI TOÁN LIÊN QUAN ĐẾN TỈ SỐ
    # =========================================================================
    # --- Bài 6 - Đề 1 ---
    exams["th5_b6_test1"] = {
        "id": "th5_b6_test1",
        "lessonId": "th5_b6",
        "lessonNum": 6,
        "testNum": 1,
        "title": "Bài 6: Bài toán liên quan đến tỉ số - Đề số 1",
        "topic": "Bài toán liên quan đến tỉ số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tỉ số của hai số 4 và 9 là:", ["$\\frac{9}{4}$", "$\\frac{4}{9}$", "$4 \\times 9$", "$9 - 4$"], 1, "Tỉ số của a và b là a : b hay a/b, do đó tỉ số là 4/9."),
            make_mc(2, "Hai số có tổng là 45 và tỉ số là $\\frac{2}{3}$. Số bé là:", ["18", "27", "15", "30"], 0, "Tổng số phần: 2 + 3 = 5. Số bé: 45 : 5 x 2 = 18."),
            make_mc(3, "Hai số có hiệu là 24 và tỉ số là $\\frac{5}{2}$. Số lớn là:", ["40", "16", "36", "48"], 0, "Hiệu số phần: 5 - 2 = 3. Số lớn: 24 : 3 x 5 = 40."),
            make_mc(4, "Một lớp học có 35 học sinh, trong đó số học sinh nam bằng $\\frac{3}{4}$ số học sinh nữ. Số học sinh nam là:", ["15", "20", "18", "21"], 0, "Tổng số phần: 3 + 4 = 7. Số học sinh nam: 35 : 7 x 3 = 15 em."),
            make_mc(5, "Hiện nay mẹ 36 tuổi, con 9 tuổi. Tỉ số tuổi của con và mẹ hiện nay là:", ["$\\frac{1}{4}$", "$4$", "$\\frac{1}{3}$", "$\\frac{9}{45}$"], 0, "Tỉ số: 9/36 = 1/4."),
            make_mc(6, "Một tấm vải dài $48\\text{ m}$ được cắt thành hai mảnh, mảnh thứ nhất dài gấp 3 lần mảnh thứ hai. Chiều dài mảnh thứ nhất là:", ["$36\\text{ m}$", "$12\\text{ m}$", "$24\\text{ m}$", "$32\\text{ m}$"], 0, "Tổng số phần: 1 + 3 = 4. Mảnh thứ nhất: 48 : 4 x 3 = 36 m.")
        ],
        "part2": [
            make_essay(1, "Tìm hai số, biết tổng của chúng bằng 108 và số thứ nhất bằng $\\frac{4}{5}$ số thứ hai.", "Tổng số phần bằng nhau là: $4 + 5 = 9$ (phần).\nSố thứ nhất là: $108 : 9 \\times 4 = 48$.\nSố thứ hai là: $108 - 48 = 60$.", "Số thứ nhất: 48; Số thứ hai: 60", 4, 1.0),
            make_essay(2, "Tìm hai số, biết hiệu của chúng bằng 72 và số lớn gấp 4 lần số bé.", "Coi số bé là 1 phần thì số lớn là 4 phần.\nHiệu số phần bằng nhau là: $4 - 1 = 3$ (phần).\nSố bé là: $72 : 3 \\times 1 = 24$.\nSố lớn là: $24 + 72 = 96$.", "Số bé: 24; Số lớn: 96", 4, 1.0),
            make_essay(3, "Một mảnh đất hình chữ nhật có chu vi là $140\\text{ m}$, chiều rộng bằng $\\frac{3}{4}$ chiều dài. Tính diện tích mảnh đất đó.", "Nửa chu vi mảnh đất là: $140 : 2 = 70\\text{ (m)}$.\nTổng số phần bằng nhau: $3 + 4 = 7$ (phần).\nChiều rộng mảnh đất là: $70 : 7 \\times 3 = 30\\text{ (m)}$.\nChiều dài mảnh đất là: $70 - 30 = 40\\text{ (m)}$.\nDiện tích mảnh đất là: $40 \\times 30 = 1 200\\text{ (m$^2$)}$.", "1 200 m$^2$", 5, 1.0),
            make_essay(4, "Khối lớp Năm của một trường có 180 học sinh. Biết số học sinh khá bằng $\\frac{2}{3}$ số học sinh giỏi, còn lại không có học sinh trung bình hay yếu. Hỏi khối lớp Năm có bao nhiêu học sinh giỏi và bao nhiêu học sinh khá?", "Tổng số phần bằng nhau là: $2 + 3 = 5$ (phần).\nSố học sinh khá là: $180 : 5 \\times 2 = 72$ (học sinh).\nSố học sinh giỏi là: $180 - 72 = 108$ (học sinh).", "Giỏi: 108 học sinh; Khá: 72 học sinh", 4, 1.0),
            make_essay(5, "Hiện nay mẹ hơn con 28 tuổi. Sau 3 năm nữa, tuổi mẹ gấp 5 lần tuổi con. Hỏi hiện nay mẹ bao nhiêu tuổi, con bao nhiêu tuổi?", "Hiệu số tuổi của hai mẹ con không thay đổi theo thời gian, luôn là 28 tuổi.\nSau 3 năm nữa, hiệu số phần bằng nhau là: $5 - 1 = 4$ (phần).\nTuổi con sau 3 năm nữa là: $28 : 4 \\times 1 = 7$ (tuổi).\nTuổi con hiện nay là: $7 - 3 = 4$ (tuổi).\nTuổi mẹ hiện nay là: $4 + 28 = 32$ (tuổi).", "Mẹ: 32 tuổi; Con: 4 tuổi", 5, 1.5),
            make_essay(6, "Hai thùng chứa tất cả $120\\text{ lít}$ dầu. Nếu chuyển $15\\text{ lít}$ dầu từ thùng thứ nhất sang thùng thứ hai thì số dầu ở thùng thứ nhất bằng $\\frac{3}{5}$ số dầu ở thùng thứ hai. Hỏi lúc đầu mỗi thùng chứa bao nhiêu lít dầu?", "Khi chuyển 15 lít từ thùng 1 sang thùng 2 thì tổng số dầu hai thùng không đổi vẫn là 120 lít.\nTổng số phần bằng nhau lúc sau là: $3 + 5 = 8$ (phần).\nSố dầu ở thùng thứ nhất lúc sau là: $120 : 8 \\times 3 = 45\\text{ (lít)}$.\nSố dầu ở thùng thứ nhất lúc đầu là: $45 + 15 = 60\\text{ (lít)}$.\nSố dầu ở thùng thứ hai lúc đầu là: $120 - 60 = 60\\text{ (lít)}$.", "Thùng 1: 60 lít; Thùng 2: 60 lít", 5, 1.5)
        ]
    }

    # --- Bài 6 - Đề 2 ---
    exams["th5_b6_test2"] = {
        "id": "th5_b6_test2",
        "lessonId": "th5_b6",
        "lessonNum": 6,
        "testNum": 2,
        "title": "Bài 6: Bài toán liên quan đến tỉ số - Đề số 2",
        "topic": "Bài toán liên quan đến tỉ số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một khu vườn trồng cam và xoài, biết có 30 cây cam và 45 cây xoài. Tỉ số của số cây cam và số cây xoài là:", ["$\\frac{3}{2}$", "$\\frac{2}{3}$", "$\\frac{2}{5}$", "$\\frac{3}{5}$"], 1, "Tỉ số: 30/45 = 2/3."),
            make_mc(2, "Tổng hai số là 96, số thứ nhất gấp 3 lần số thứ hai. Số thứ hai là:", ["24", "72", "32", "64"], 0, "Tổng số phần: 1 + 3 = 4. Số thứ hai: 96 : 4 = 24."),
            make_mc(3, "Hiệu hai số là 35, tỉ số giữa số bé và số lớn là $\\frac{2}{7}$. Số bé là:", ["14", "49", "10", "25"], 0, "Hiệu số phần: 7 - 2 = 5. Số bé: 35 : 5 x 2 = 14."),
            make_mc(4, "Một trang trại có số bò bằng $\\frac{2}{5}$ số trâu. Biết số trâu nhiều hơn số bò là 45 con. Số trâu của trang trại là:", ["75 con", "30 con", "60 con", "90 con"], 0, "Hiệu số phần: 5 - 2 = 3. Số trâu: 45 : 3 x 5 = 75 con."),
            make_mc(5, "Một sợi dây dài $72\\text{ cm}$ được cắt thành hai đoạn, đoạn ngắn bằng $\\frac{1}{3}$ đoạn dài. Đoạn ngắn dài là:", ["$18\\text{ cm}$", "$24\\text{ cm}$", "$54\\text{ cm}$", "$12\\text{ cm}$"], 0, "Tổng số phần: 1 + 3 = 4. Đoạn ngắn: 72 : 4 = 18 cm."),
            make_mc(6, "Biết $\\frac{1}{2}$ số gạo ở kho A bằng $\\frac{1}{3}$ số gạo ở kho B. Tỉ số giữa số gạo kho A và kho B là:", ["$\\frac{3}{2}$", "$\\frac{2}{3}$", "$\\frac{1}{6}$", "$\\frac{5}{6}$"], 1, "Kho A = 2 phần, kho B = 3 phần, nên tỉ số là 2/3.")
        ],
        "part2": [
            make_essay(1, "Tìm hai số có tổng bằng 144 và tỉ số giữa chúng là $\\frac{5}{7}$.", "Tổng số phần bằng nhau: $5 + 7 = 12$ (phần).\nSố bé là: $144 : 12 \\times 5 = 60$.\nSố lớn là: $144 - 60 = 84$.", "Số bé: 60; Số lớn: 84", 4, 1.0),
            make_essay(2, "Tìm hai số có hiệu bằng 56, biết số lớn chia cho số bé được thương là 5.", "Thương bằng 5 nghĩa là số lớn gấp 5 lần số bé.\nHiệu số phần bằng nhau: $5 - 1 = 4$ (phần).\nSố bé là: $56 : 4 \\times 1 = 14$.\nSố lớn là: $14 + 56 = 70$.", "Số bé: 14; Số lớn: 70", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chu vi $160\\text{ m}$. Nếu bớt chiều dài $10\\text{ m}$ và tăng chiều rộng $10\\text{ m}$ thì mảnh vườn trở thành hình vuông. Tính diện tích mảnh vườn hình chữ nhật.", "Nửa chu vi là: $160 : 2 = 80\\text{ (m)}$.\nChiều dài hơn chiều rộng là: $10 + 10 = 20\\text{ (m)}$.\nChiều dài mảnh vườn là: $(80 + 20) : 2 = 50\\text{ (m)}$.\nChiều rộng mảnh vườn là: $80 - 50 = 30\\text{ (m)}$.\nDiện tích mảnh vườn là: $50 \\times 30 = 1 500\\text{ (m$^2$)}$.", "1 500 m$^2$", 5, 1.0),
            make_essay(4, "Một giá sách có hai ngăn chứa tất cả 150 quyển sách. Nếu chuyển 15 quyển từ ngăn trên xuống ngăn dưới thì số sách ở ngăn trên bằng $\\frac{2}{3}$ số sách ở ngăn dưới. Hỏi lúc đầu mỗi ngăn có bao nhiêu quyển sách?", "Tổng số sách không đổi là 150 quyển.\nTổng số phần bằng nhau lúc sau: $2 + 3 = 5$ (phần).\nSố sách ngăn trên lúc sau là: $150 : 5 \\times 2 = 60$ (quyển).\nSố sách ngăn trên lúc đầu là: $60 + 15 = 75$ (quyển).\nSố sách ngăn dưới lúc đầu là: $150 - 75 = 75$ (quyển).", "Ngăn trên: 75 quyển; Ngăn dưới: 75 quyển", 5, 1.0),
            make_essay(5, "Hiện nay tuổi bố gấp 4 lần tuổi con. Biết rằng 5 năm trước, bố hơn con 30 tuổi. Hỏi hiện nay bố bao nhiêu tuổi, con bao nhiêu tuổi?", "Hiệu số tuổi của bố và con luôn không đổi theo thời gian, là 30 tuổi.\nHiện nay tuổi bố gấp 4 lần tuổi con, hiệu số phần là: $4 - 1 = 3$ (phần).\nTuổi con hiện nay là: $30 : 3 \\times 1 = 10$ (tuổi).\nTuổi bố hiện nay là: $10 + 30 = 40$ (tuổi).", "Bố: 40 tuổi; Con: 10 tuổi", 4, 1.5),
            make_essay(6, "Một người bán cam, lần thứ nhất bán được $\\frac{1}{3}$ số cam và thêm 2 quả. Lần thứ hai bán được $\\frac{1}{2}$ số cam còn lại và thêm 3 quả thì trong rổ còn lại 15 quả cam. Hỏi ban đầu người đó có tất cả bao nhiêu quả cam?", "Số cam còn lại trước khi bán thêm 3 quả ở lần thứ hai là: $15 + 3 = 18$ (quả).\n18 quả này chiếm: $1 - \\frac{1}{2} = \\frac{1}{2}$ (số cam còn lại sau lần 1).\nSố cam còn lại sau lần thứ nhất là: $18 : \\frac{1}{2} = 36$ (quả).\nSố cam còn lại trước khi bán thêm 2 quả ở lần thứ nhất là: $36 + 2 = 38$ (quả).\n38 quả này chiếm: $1 - \\frac{1}{3} = \\frac{2}{3}$ (tổng số cam ban đầu).\nSố cam ban đầu là: $38 : \\frac{2}{3} = 57$ (quả).", "57 quả cam", 5, 1.5)
        ]
    }

    # --- Bài 6 - Đề 3 ---
    exams["th5_b6_test3"] = {
        "id": "th5_b6_test3",
        "lessonId": "th5_b6",
        "lessonNum": 6,
        "testNum": 3,
        "title": "Bài 6: Bài toán liên quan đến tỉ số - Đề số 3",
        "topic": "Bài toán liên quan đến tỉ số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một đội tình nguyện gồm 18 nam và 24 nữ. Tỉ số của số nam so với số nữ đã được rút gọn là:", ["$\\frac{4}{3}$", "$\\frac{3}{4}$", "$\\frac{3}{7}$", "$\\frac{4}{7}$"], 1, "18/24 = 3/4."),
            make_mc(2, "Hai số có tổng là 210 và tỉ số là $\\frac{3}{4}$. Số lớn là:", ["90", "120", "150", "140"], 1, "Tổng số phần: 3 + 4 = 7. Số lớn: 210 : 7 x 4 = 120."),
            make_mc(3, "Hai thùng dầu có hiệu số dầu là 48 lít, thùng bé bằng $\\frac{3}{7}$ thùng lớn. Số dầu ở thùng bé là:", ["36 lít", "84 lít", "24 lít", "42 lít"], 0, "Hiệu số phần: 7 - 3 = 4. Thùng bé: 48 : 4 x 3 = 36 lít."),
            make_mc(4, "Một mảnh vườn có chiều dài gấp 3 lần chiều rộng và diện tích là $48\\text{ m}^2$. Chu vi mảnh vườn đó là:", ["$32\\text{ m}$", "$16\\text{ m}$", "$24\\text{ m}$", "$40\\text{ m}$"], 0, "Chia thành 3 hình vuông bằng nhau: 48 : 3 = 16 m$^2$. Cạnh hình vuông = 4 m. Chiều rộng = 4 m, chiều dài = 12 m. Chu vi = (12 + 4) x 2 = 32 m."),
            make_mc(5, "Hiện nay tổng số tuổi của hai anh em là 25 tuổi. Biết anh hơn em 5 tuổi. Tỉ số tuổi của em và anh hiện nay là:", ["$\\frac{2}{3}$", "$\\frac{3}{2}$", "$\\frac{1}{2}$", "$\\frac{3}{5}$"], 0, "Tuổi em: (25 - 5) : 2 = 10 tuổi. Tuổi anh: 15 tuổi. Tỉ số: 10/15 = 2/3."),
            make_mc(6, "Biết $\\frac{2}{3}$ số bi của An bằng $\\frac{4}{5}$ số bi của Bình. Tỉ số bi của An và Bình là:", ["$\\frac{6}{5}$", "$\\frac{5}{6}$", "$\\frac{8}{15}$", "$\\frac{15}{8}$"], 0, "Quy đồng tử số: 4/6 số bi của An = 4/5 số bi của Bình => An 6 phần, Bình 5 phần => tỉ số là 6/5.")
        ],
        "part2": [
            make_essay(1, "Tìm hai số có tổng bằng 175 và biết rằng nếu lấy số lớn chia cho số bé thì được thương là 6.", "Thương bằng 6 tức là số lớn gấp 6 lần số bé.\nTổng số phần bằng nhau: $1 + 6 = 7$ (phần).\nSố bé là: $175 : 7 = 25$.\nSố lớn là: $175 - 25 = 150$.", "Số bé: 25; Số lớn: 150", 4, 1.0),
            make_essay(2, "Một trường tiểu học có số học sinh nữ nhiều hơn số học sinh nam là 64 em. Biết rằng số học sinh nam bằng $\\frac{7}{9}$ số học sinh nữ. Tính số học sinh nam và số học sinh nữ của trường đó.", "Hiệu số phần bằng nhau: $9 - 7 = 2$ (phần).\nSố học sinh nam là: $64 : 2 \\times 7 = 224$ (học sinh).\nSố học sinh nữ là: $224 + 64 = 288$ (học sinh).", "Nam: 224 em; Nữ: 288 em", 4, 1.0),
            make_essay(3, "Một khu đất hình chữ nhật có chu vi là $220\\text{ m}$. Chiều dài bằng $\\frac{6}{5}$ chiều rộng. Tính diện tích khu đất đó theo đơn vị mét vuông.", "Nửa chu vi khu đất là: $220 : 2 = 110\\text{ (m)}$.\nTổng số phần bằng nhau: $6 + 5 = 11$ (phần).\nChiều rộng khu đất là: $110 : 11 \\times 5 = 50\\text{ (m)}$.\nChiều dài khu đất là: $110 - 50 = 60\\text{ (m)}$.\nDiện tích khu đất là: $60 \\times 50 = 3 000\\text{ (m$^2$)}$.", "3 000 m$^2$", 5, 1.0),
            make_essay(4, "Một tổ công nhân có 24 người cần hoàn thành một công việc trong 15 ngày. Nếu muốn hoàn thành công việc đó trong 10 ngày thì cần thêm bao nhiêu công nhân? (Biết năng suất làm việc của mỗi người là như nhau).", "Để hoàn thành công việc trong 1 ngày cần số công nhân là:\n$24 \\times 15 = 360$ (công nhân).\nĐể hoàn thành công việc trong 10 ngày cần số công nhân là:\n$360 : 10 = 36$ (công nhân).\nSố công nhân cần bổ sung thêm là:\n$36 - 24 = 12$ (công nhân).", "12 công nhân", 4, 1.0),
            make_essay(5, "Ba lớp 5A, 5B, 5C thu gom được tất cả $450\\text{ kg}$ giấy vụn. Số giấy vụn của lớp 5A bằng $\\frac{1}{3}$ tổng số giấy vụn của cả ba lớp. Số giấy vụn của lớp 5B bằng $\\frac{2}{3}$ số giấy vụn của lớp 5C. Hỏi mỗi lớp thu gom được bao nhiêu ki-lô-gam giấy vụn?", "Số giấy vụn lớp 5A thu gom được là: $450 \\times \\frac{1}{3} = 150\\text{ (kg)}$.\nTổng số giấy vụn lớp 5B và 5C thu gom được là: $450 - 150 = 300\\text{ (kg)}$.\nTổng số phần bằng nhau của lớp 5B và 5C: $2 + 3 = 5$ (phần).\nSố giấy vụn lớp 5B thu gom được là: $300 : 5 \\times 2 = 120\\text{ (kg)}$.\nSố giấy vụn lớp 5C thu gom được là: $300 - 120 = 180\\text{ (kg)}$.", "5A: 150 kg; 5B: 120 kg; 5C: 180 kg", 5, 1.5),
            make_essay(6, "Một người có 3 chuồng gà. Chuồng 1 có số gà bằng $\\frac{1}{2}$ chuồng 2. Chuồng 2 có số gà bằng $\\frac{2}{3}$ chuồng 3. Biết rằng chuồng 3 nhiều hơn chuồng 1 là 40 con gà. Hỏi cả 3 chuồng có tất cả bao nhiêu con gà?", "Coi số gà chuồng 1 là 1 phần thì số gà chuồng 2 là 2 phần.\nVì chuồng 2 bằng 2/3 chuồng 3, nên số gà chuồng 3 là 3 phần như thế.\nHiệu số phần giữa chuồng 3 và chuồng 1 là: $3 - 1 = 2$ (phần).\nGiá trị 1 phần là: $40 : 2 = 20$ (con gà).\nSố gà chuồng 1: $20 \\times 1 = 20$ (con).\nSố gà chuồng 2: $20 \\times 2 = 40$ (con).\nSố gà chuồng 3: $20 \\times 3 = 60$ (con).\nTổng số gà cả 3 chuồng là: $20 + 40 + 60 = 120$ (con).", "120 con gà", 5, 1.5)
        ]
    }

    return exams
