# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 1: ÔN TẬP VÀ BỔ SUNG (BÀI 7 ĐẾN BÀI 9) - TOÁN 5 KNTT
Mỗi bài có đúng 3 đề kiểm tra độc lập (test1, test2, test3):
- 6 câu trắc nghiệm (part1, mỗi câu 0.5 điểm = 3.0 điểm)
- 6 câu tự luận (part2, 4 câu 1.0 đ + 2 câu 1.5 đ = 7.0 điểm, lineCount: 3 đến 6 dòng)
Tổng điểm: 10.0 điểm, thời gian: 35 phút.
"""
from th5_ch1_part1 import make_mc, make_essay

def get_ch1_part3_exams():
    exams = {}

    # =========================================================================
    # BÀI 7: HỖN SỐ
    # =========================================================================
    # --- Bài 7 - Đề 1 ---
    exams["th5_b7_test1"] = {
        "id": "th5_b7_test1",
        "lessonId": "th5_b7",
        "lessonNum": 7,
        "testNum": 1,
        "title": "Bài 7: Hỗn số - Đề số 1",
        "topic": "Hỗn số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hỗn số $3\\frac{2}{5}$ có phần nguyên là:", ["3", "2", "5", "$\\frac{2}{5}$"], 0, "Phần nguyên là 3, phần phân số là 2/5."),
            make_mc(2, "Chuyển hỗn số $4\\frac{3}{7}$ thành phân số ta được:", ["$\\frac{19}{7}$", "$\\frac{31}{7}$", "$\\frac{12}{7}$", "$\\frac{28}{7}$"], 1, "Tử số = 4 x 7 + 3 = 31, giữ nguyên mẫu số 7: 31/7."),
            make_mc(3, "Chuyển phân số $\\frac{17}{5}$ thành hỗn số ta được:", ["$3\\frac{2}{5}$", "$2\\frac{7}{5}$", "$3\\frac{1}{5}$", "$4\\frac{2}{5}$"], 0, "17 : 5 = 3 dư 2, nên bằng 3 2/5."),
            make_mc(4, "Hỗn số 'Năm và ba phần tư' viết là:", ["$5\\frac{3}{4}$", "$3\\frac{5}{4}$", "$\\frac{53}{4}$", "$5\\frac{4}{3}$"], 0, "Phần nguyên là 5, phần phân số là 3/4."),
            make_mc(5, "Điền dấu thích hợp: $2\\frac{1}{3} \\dots 2\\frac{2}{5}$:", ["<", ">", "=", "Không so sánh được"], 0, "Phần nguyên bằng 2. So sánh 1/3 = 5/15 và 2/5 = 6/15, vì 5/15 < 6/15 nên 2 1/3 < 2 2/5."),
            make_mc(6, "Kết quả của phép tính $1\\frac{1}{2} + 2\\frac{1}{4}$ là:", ["$3\\frac{3}{4}$", "$3\\frac{2}{6}$", "$3\\frac{1}{4}$", "$4\\frac{1}{4}$"], 0, "1 1/2 + 2 1/4 = 3/2 + 9/4 = 6/4 + 9/4 = 15/4 = 3 3/4.")
        ],
        "part2": [
            make_essay(1, "Chuyển các hỗn số sau thành phân số:\na) $2\\frac{3}{8}$\nb) $5\\frac{1}{6}$", "a) $2\\frac{3}{8} = \\frac{2 \\times 8 + 3}{8} = \\frac{19}{8}$\nb) $5\\frac{1}{6} = \\frac{5 \\times 6 + 1}{6} = \\frac{31}{6}$", "a) 19/8; b) 31/6", 3, 1.0),
            make_essay(2, "Chuyển các phân số sau thành hỗn số:\na) $\\frac{23}{4}$\nb) $\\frac{37}{8}$", "a) $23 : 4 = 5$ dư $3$, nên $\\frac{23}{4} = 5\\frac{3}{4}$.\nb) $37 : 8 = 4$ dư $5$, nên $\\frac{37}{8} = 4\\frac{5}{8}$.", "a) 5 3/4; b) 4 5/8", 3, 1.0),
            make_essay(3, "So sánh các hỗn số sau:\na) $3\\frac{4}{7}$ và $3\\frac{5}{9}$\nb) $4\\frac{2}{5}$ và $5\\frac{1}{10}$", "a) Phần nguyên bằng nhau. So sánh $\\frac{4}{7} = \\frac{36}{63}$ và $\\frac{5}{9} = \\frac{35}{63}$. Vì $\\frac{36}{63} > \\frac{35}{63}$ nên $3\\frac{4}{7} > 3\\frac{5}{9}$.\nb) Vì phần nguyên $4 < 5$ nên $4\\frac{2}{5} < 5\\frac{1}{10}$.", "a) >; b) <", 4, 1.0),
            make_essay(4, "Thực hiện phép tính bằng cách chuyển về phân số:\na) $3\\frac{1}{5} + 2\\frac{3}{10}$\nb) $4\\frac{1}{2} - 1\\frac{3}{4}$", "a) $3\\frac{1}{5} + 2\\frac{3}{10} = \\frac{16}{5} + \\frac{23}{10} = \\frac{32}{10} + \\frac{23}{10} = \\frac{55}{10} = \\frac{11}{2} = 5\\frac{1}{2}$.\nb) $4\\frac{1}{2} - 1\\frac{3}{4} = \\frac{9}{2} - \\frac{7}{4} = \\frac{18}{4} - \\frac{7}{4} = \\frac{11}{4} = 2\\frac{3}{4}$.", "a) 11/2 (hoặc 5 1/2); b) 11/4 (hoặc 2 3/4)", 4, 1.0),
            make_essay(5, "Một tấm gỗ dài $3\\frac{1}{2}\\text{ m}$, người ta cưa đi một đoạn dài $1\\frac{1}{4}\\text{ m}$. Hỏi đoạn gỗ còn lại dài bao nhiêu mét?", "Đoạn gỗ còn lại dài số mét là:\n$3\\frac{1}{2} - 1\\frac{1}{4} = \\frac{7}{2} - \\frac{5}{4} = \\frac{14}{4} - \\frac{5}{4} = \\frac{9}{4}\\text{ (m)} = 2\\frac{1}{4}\\text{ (m)}$.", "9/4 m (hoặc 2 1/4 m)", 4, 1.5),
            make_essay(6, "Một mảnh vườn hình chữ nhật có chiều rộng là $4\\frac{1}{2}\\text{ m}$, chiều dài gấp $1\\frac{1}{3}$ lần chiều rộng. Tính chu vi và diện tích mảnh vườn đó.", "Chuyển về phân số: $4\\frac{1}{2} = \\frac{9}{2}\\text{ m}$; $1\\frac{1}{3} = \\frac{4}{3}$.\nChiều dài mảnh vườn là: $\\frac{9}{2} \\times \\frac{4}{3} = 6\\text{ (m)}$.\nChu vi mảnh vườn là: $(\\frac{9}{2} + 6) \\times 2 = \\frac{21}{2} \\times 2 = 21\\text{ (m)}$.\nDiện tích mảnh vườn là: $6 \\times \\frac{9}{2} = 27\\text{ (m$^2$)}$.", "Chu vi: 21 m; Diện tích: 27 m$^2$", 5, 1.5)
        ]
    }

    # --- Bài 7 - Đề 2 ---
    exams["th5_b7_test2"] = {
        "id": "th5_b7_test2",
        "lessonId": "th5_b7",
        "lessonNum": 7,
        "testNum": 2,
        "title": "Bài 7: Hỗn số - Đề số 2",
        "topic": "Hỗn số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hỗn số $6\\frac{5}{8}$ đọc là:", [
                "Sáu và năm phần tám",
                "Sáu phần năm tám",
                "Năm phần tám và sáu",
                "Sáu mươi lăm phần tám"
            ], 0, "Đọc phần nguyên trước, chữ 'và', rồi đọc phần phân số."),
            make_mc(2, "Phần phân số của hỗn số $7\\frac{4}{9}$ là:", ["7", "$\\frac{4}{9}$", "4", "9"], 1, "Phần phân số là 4/9."),
            make_mc(3, "Chuyển hỗn số $3\\frac{4}{5}$ thành phân số:", ["$\\frac{12}{5}$", "$\\frac{19}{5}$", "$\\frac{17}{5}$", "$\\frac{20}{5}$"], 1, "(3 x 5 + 4)/5 = 19/5."),
            make_mc(4, "Chuyển phân số $\\frac{29}{6}$ thành hỗn số:", ["$4\\frac{5}{6}$", "$5\\frac{1}{6}$", "$4\\frac{1}{6}$", "$3\\frac{11}{6}$"], 0, "29 : 6 = 4 dư 5, nên bằng 4 5/6."),
            make_mc(5, "Kết quả của phép nhân $2\\frac{1}{3} \\times 1\\frac{1}{2}$ là:", ["$2\\frac{1}{6}$", "$3\\frac{1}{2}$", "$3\\frac{1}{6}$", "$2\\frac{1}{2}$"], 1, "7/3 x 3/2 = 7/2 = 3 1/2."),
            make_mc(6, "Trong các hỗn số $2\\frac{3}{4}; 3\\frac{1}{5}; 1\\frac{7}{8}; 2\\frac{4}{5}$, hỗn số nhỏ nhất là:", ["$2\\frac{3}{4}$", "$3\\frac{1}{5}$", "$1\\frac{7}{8}$", "$2\\frac{4}{5}$"], 2, "Hỗn số 1 7/8 có phần nguyên bằng 1 nhỏ nhất.")
        ],
        "part2": [
            make_essay(1, "Chuyển các hỗn số sau thành phân số:\na) $3\\frac{5}{7}$\nb) $6\\frac{2}{9}$", "a) $3\\frac{5}{7} = \\frac{3 \\times 7 + 5}{7} = \\frac{26}{7}$\nb) $6\\frac{2}{9} = \\frac{6 \\times 9 + 2}{9} = \\frac{56}{9}$", "a) 26/7; b) 56/9", 3, 1.0),
            make_essay(2, "Chuyển các phân số sau thành hỗn số:\na) $\\frac{31}{5}$\nb) $\\frac{45}{7}$", "a) $31 : 5 = 6$ dư 1 $\\Rightarrow \\frac{31}{5} = 6\\frac{1}{5}$.\nb) $45 : 7 = 6$ dư 3 $\\Rightarrow \\frac{45}{7} = 6\\frac{3}{7}$.", "a) 6 1/5; b) 6 3/7", 3, 1.0),
            make_essay(3, "Thực hiện các phép tính sau:\na) $2\\frac{1}{4} \\times 1\\frac{1}{3}$\nb) $3\\frac{1}{2} : 1\\frac{3}{4}$", "a) $2\\frac{1}{4} \\times 1\\frac{1}{3} = \\frac{9}{4} \\times \\frac{4}{3} = 3$.\nb) $3\\frac{1}{2} : 1\\frac{3}{4} = \\frac{7}{2} : \\frac{7}{4} = \\frac{7}{2} \\times \\frac{4}{7} = 2$.", "a) 3; b) 2", 4, 1.0),
            make_essay(4, "Tìm $x$, biết: $x - 1\\frac{3}{5} = 2\\frac{1}{2}$.", "$x = 2\\frac{1}{2} + 1\\frac{3}{5}$\n$x = \\frac{5}{2} + \\frac{8}{5} = \\frac{25}{10} + \\frac{16}{10} = \\frac{41}{10} = 4\\frac{1}{10}$.", "x = 41/10 (hoặc 4 1/10)", 3, 1.0),
            make_essay(5, "Một người đi bộ, giờ thứ nhất đi được $3\\frac{1}{2}\\text{ km}$, giờ thứ hai đi được $3\\frac{3}{4}\\text{ km}$, giờ thứ ba đi được $4\\frac{1}{4}\\text{ km}$. Hỏi trung bình mỗi giờ người đó đi được bao nhiêu ki-lô-mét?", "Tổng quãng đường người đó đi trong 3 giờ là:\n$3\\frac{1}{2} + 3\\frac{3}{4} + 4\\frac{1}{4} = \\frac{7}{2} + (\\frac{15}{4} + \\frac{17}{4}) = \\frac{14}{4} + \\frac{32}{4} = \\frac{46}{4} = \\frac{23}{2}\\text{ (km)}$.\nTrung bình mỗi giờ người đó đi được là:\n$\\frac{23}{2} : 3 = \\frac{23}{6}\\text{ (km)} = 3\\frac{5}{6}\\text{ (km)}$.", "23/6 km (hoặc 3 5/6 km)", 5, 1.5),
            make_essay(6, "Một hình hộp chữ nhật có chiều dài $2\\frac{1}{2}\\text{ dm}$, chiều rộng $1\\frac{1}{5}\\text{ dm}$ và chiều cao $1\\frac{2}{3}\\text{ dm}$. Tính thể tích của hình hộp chữ nhật đó.", "Đổi về phân số: $2\\frac{1}{2} = \\frac{5}{2}\\text{ dm}$; $1\\frac{1}{5} = \\frac{6}{5}\\text{ dm}$; $1\\frac{2}{3} = \\frac{5}{3}\\text{ dm}$.\nThể tích của hình hộp chữ nhật là:\n$V = \\frac{5}{2} \\times \\frac{6}{5} \\times \\frac{5}{3} = \\frac{5 \\times 6 \\times 5}{2 \\times 5 \\times 3} = 5\\text{ (dm$^3$)}$.", "5 dm$^3$", 4, 1.5)
        ]
    }

    # --- Bài 7 - Đề 3 ---
    exams["th5_b7_test3"] = {
        "id": "th5_b7_test3",
        "lessonId": "th5_b7",
        "lessonNum": 7,
        "testNum": 3,
        "title": "Bài 7: Hỗn số - Đề số 3",
        "topic": "Hỗn số",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hỗn số $5\\frac{3}{10}$ viết dưới dạng phân số thập phân là:", ["$\\frac{53}{10}$", "$\\frac{15}{10}$", "$\\frac{35}{10}$", "$\\frac{50}{10}$"], 0, "(5 x 10 + 3)/10 = 53/10."),
            make_mc(2, "Phần phân số của một hỗn số luôn có đặc điểm là:", [
                "Lớn hơn 1",
                "Bé hơn 1",
                "Bằng 1",
                "Tùy ý, lớn hay bé hơn 1 đều được"
            ], 1, "Quy ước: phần phân số của hỗn số luôn bé hơn 1."),
            make_mc(3, "Chuyển phân số $\\frac{41}{8}$ thành hỗn số:", ["$5\\frac{1}{8}$", "$4\\frac{9}{8}$", "$5\\frac{3}{8}$", "$4\\frac{1}{8}$"], 0, "41 : 8 = 5 dư 1, nên bằng 5 1/8."),
            make_mc(4, "Kết quả của phép chia $2\\frac{2}{3} : 1\\frac{1}{3}$ là:", ["$2$", "$\\frac{1}{2}$", "$1\\frac{1}{3}$", "$3$"], 0, "8/3 : 4/3 = 8/4 = 2."),
            make_mc(5, "Số đo $3\\text{ m } 25\\text{ cm}$ viết dưới dạng hỗn số với đơn vị mét là:", ["$3\\frac{25}{10}\\text{ m}$", "$3\\frac{1}{4}\\text{ m}$", "$3\\frac{25}{1000}\\text{ m}$", "$3\\frac{2}{5}\\text{ m}$"], 1, "25 cm = 25/100 m = 1/4 m, nên bằng 3 1/4 m."),
            make_mc(6, "Tìm số tự nhiên $n$ biết: $3\\frac{1}{2} < n < 5\\frac{1}{4}$. Các giá trị của $n$ là:", ["3 và 4", "4 và 5", "5 và 6", "4"], 1, "Vì 3,5 < n < 5,25 nên số tự nhiên n có thể là 4 hoặc 5.")
        ],
        "part2": [
            make_essay(1, "Chuyển các hỗn số sau thành phân số:\na) $4\\frac{3}{10}$\nb) $7\\frac{5}{12}$", "a) $4\\frac{3}{10} = \\frac{4 \\times 10 + 3}{10} = \\frac{43}{10}$\nb) $7\\frac{5}{12} = \\frac{7 \\times 12 + 5}{12} = \\frac{89}{12}$", "a) 43/10; b) 89/12", 3, 1.0),
            make_essay(2, "Viết các số đo sau dưới dạng hỗn số thích hợp:\na) $4\\text{ m } 7\\text{ dm}$ (đơn vị mét);\nb) $2\\text{ giờ } 15\\text{ phút}$ (đơn vị giờ).", "a) $4\\text{ m } 7\\text{ dm} = 4\\frac{7}{10}\\text{ m}$.\nb) $15\\text{ phút} = \\frac{15}{60}\\text{ giờ} = \\frac{1}{4}\\text{ giờ} \\Rightarrow 2\\text{ giờ } 15\\text{ phút} = 2\\frac{1}{4}\\text{ giờ}$.", "a) 4 7/10 m; b) 2 1/4 giờ", 3, 1.0),
            make_essay(3, "Tính bằng cách thuận tiện nhất:\na) $2\\frac{3}{7} + 4\\frac{5}{9} + 1\\frac{4}{7}$\nb) $5\\frac{3}{4} \\times 2\\frac{1}{3} - 5\\frac{3}{4} \\times 1\\frac{1}{3}$", "a) $(2\\frac{3}{7} + 1\\frac{4}{7}) + 4\\frac{5}{9} = 4 + 4\\frac{5}{9} = 8\\frac{5}{9}$.\nb) $5\\frac{3}{4} \\times (2\\frac{1}{3} - 1\\frac{1}{3}) = 5\\frac{3}{4} \\times 1 = 5\\frac{3}{4}$.", "a) 8 5/9; b) 5 3/4", 4, 1.0),
            make_essay(4, "Tìm $x$, biết: $x \\times 1\\frac{1}{2} = 3\\frac{3}{4}$.", "$x \\times \\frac{3}{2} = \\frac{15}{4}$\n$x = \\frac{15}{4} : \\frac{3}{2} = \\frac{15}{4} \\times \\frac{2}{3} = \\frac{5}{2} = 2\\frac{1}{2}$.", "x = 5/2 (hoặc 2 1/2)", 3, 1.0),
            make_essay(5, "Một kho hàng có $12\\frac{1}{2}\\text{ tấn}$ gạo. Buổi sáng người ta xuất ra $3\\frac{3}{4}\\text{ tấn}$ gạo, buổi chiều xuất ra nhiều hơn buổi sáng $1\\frac{1}{2}\\text{ tấn}$ gạo. Hỏi trong kho còn lại bao nhiêu tấn gạo?", "Buổi chiều kho xuất ra số tấn gạo là:\n$3\\frac{3}{4} + 1\\frac{1}{2} = \\frac{15}{4} + \\frac{6}{4} = \\frac{21}{4}\\text{ (tấn)}$.\nCả hai buổi kho đã xuất ra số tấn gạo là:\n$\\frac{15}{4} + \\frac{21}{4} = \\frac{36}{4} = 9\\text{ (tấn)}$.\nSố tấn gạo còn lại trong kho là:\n$12\\frac{1}{2} - 9 = 3\\frac{1}{2}\\text{ (tấn)}$.", "3 1/2 tấn gạo (hoặc 7/2 tấn)", 5, 1.5),
            make_essay(6, "Một người đi xe máy từ tỉnh A đến tỉnh B. Giờ thứ nhất người đó đi được $35\\frac{1}{2}\\text{ km}$. Giờ thứ hai đi được nhiều hơn giờ thứ nhất $3\\frac{3}{4}\\text{ km}$. Giờ thứ ba đi được quãng đường bằng $\\frac{4}{5}$ quãng đường của giờ thứ hai thì đến B. Tính độ dài quãng đường từ tỉnh A đến tỉnh B.", "Giờ thứ hai đi được: $35\\frac{1}{2} + 3\\frac{3}{4} = \\frac{71}{2} + \\frac{15}{4} = \\frac{142}{4} + \\frac{15}{4} = \\frac{157}{4}\\text{ (km)}$.\nGiờ thứ ba đi được: $\\frac{157}{4} \\times \\frac{4}{5} = \\frac{157}{5} = 31\\frac{2}{5}\\text{ (km)} = 31,4\\text{ (km)}$.\nĐộ dài quãng đường AB là:\n$\\frac{71}{2} + \\frac{157}{4} + \\frac{157}{5} = \\frac{710 + 785 + 628}{20} = \\frac{2123}{20}\\text{ (km)} = 106\\frac{3}{20}\\text{ km} = 106,15\\text{ km}$.", "106,15 km (hay 2123/20 km)", 5, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 8: ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG
    # =========================================================================
    # --- Bài 8 - Đề 1 ---
    exams["th5_b8_test1"] = {
        "id": "th5_b8_test1",
        "lessonId": "th5_b8",
        "lessonNum": 8,
        "testNum": 1,
        "title": "Bài 8: Ôn tập hình học và đo lường - Đề số 1",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm để $5\\text{ m}^2 = \\dots \\text{ dm}^2$ là:", ["50", "500", "5 000", "50 000"], 1, "1 m$^2$ = 100 dm$^2$, nên 5 m$^2$ = 500 dm$^2$."),
            make_mc(2, "Một héc-ta ($1\\text{ ha}$) bằng bao nhiêu mét vuông?", ["$100\\text{ m}^2$", "$1 000\\text{ m}^2$", "$10 000\\text{ m}^2$", "$100 000\\text{ m}^2$"], 2, "1 ha = 10 000 m$^2$."),
            make_mc(3, "Hình bình hành có độ dài đáy là $12\\text{ cm}$ và chiều cao tương ứng là $7\\text{ cm}$. Diện tích của hình bình hành đó là:", ["$42\\text{ cm}^2$", "$84\\text{ cm}^2$", "$19\\text{ cm}^2$", "$38\\text{ cm}^2$"], 1, "S = đáy x chiều cao = 12 x 7 = 84 cm$^2$."),
            make_mc(4, "Một hình thoi có độ dài hai đường chéo là $8\\text{ dm}$ và $15\\text{ dm}$. Diện tích hình thoi là:", ["$120\\text{ dm}^2$", "$60\\text{ dm}^2$", "$46\\text{ dm}^2$", "$30\\text{ dm}^2$"], 1, "S = (8 x 15) : 2 = 60 dm$^2$."),
            make_mc(5, "Số thích hợp điền vào chỗ chấm: $3\\text{ tấn } 45\\text{ kg} = \\dots \\text{ kg}$ là:", ["3 450", "3 045", "345", "30 045"], 1, "3 tấn = 3 000 kg => 3 000 + 45 = 3 045 kg."),
            make_mc(6, "Chu vi hình vuông có diện tích $64\\text{ cm}^2$ là:", ["$16\\text{ cm}$", "$32\\text{ cm}$", "$64\\text{ cm}$", "$24\\text{ cm}$"], 1, "Cạnh hình vuông là 8 cm (vì 8 x 8 = 64). Chu vi: 8 x 4 = 32 cm.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $7\\text{ km } 35\\text{ m} = \\dots \\text{ m}$\nb) $4\\text{ tạ } 8\\text{ kg} = \\dots \\text{ kg}$\nc) $6\\text{ m}^2\\ 45\\text{ dm}^2 = \\dots \\text{ dm}^2$\nd) $3\\text{ ha} = \\dots \\text{ m}^2$", "a) $7\\text{ km } 35\\text{ m} = 7 035\\text{ m}$\nb) $4\\text{ tạ } 8\\text{ kg} = 408\\text{ kg}$\nc) $6\\text{ m}^2\\ 45\\text{ dm}^2 = 645\\text{ dm}^2$\nd) $3\\text{ ha} = 30 000\\text{ m}^2$", "a) 7 035; b) 408; c) 645; d) 30 000", 4, 1.0),
            make_essay(2, "Điền dấu thích hợp ($>, <, =$) vào chỗ chấm:\na) $2\\text{ m}^2\\ 5\\text{ dm}^2 \\dots 250\\text{ dm}^2$\nb) $4\\text{ ha } 500\\text{ m}^2 \\dots 40 500\\text{ m}^2$", "a) $2\\text{ m}^2\\ 5\\text{ dm}^2 = 205\\text{ dm}^2 < 250\\text{ dm}^2$.\nb) $4\\text{ ha } 500\\text{ m}^2 = 40 500\\text{ m}^2 = 40 500\\text{ m}^2$.", "a) <; b) =", 3, 1.0),
            make_essay(3, "Một khu rừng hình chữ nhật có chiều dài $3\\text{ km}$, chiều rộng $2\\text{ km}$. Hỏi diện tích khu rừng đó bằng bao nhiêu ki-lô-mét vuông? Bằng bao nhiêu héc-ta?", "Diện tích khu rừng theo ki-lô-mét vuông là:\n$3 \\times 2 = 6\\text{ (km$^2$)}$.\nVì $1\\text{ km}^2 = 100\\text{ ha}$ nên:\n$6\\text{ km}^2 = 600\\text{ ha}$.", "6 km$^2$; 600 ha", 4, 1.0),
            make_essay(4, "Một mảnh đất hình bình hành có độ dài đáy là $45\\text{ m}$, chiều cao bằng $\\frac{2}{3}$ độ dài đáy. Tính diện tích mảnh đất đó.", "Chiều cao mảnh đất là:\n$45 \\times \\frac{2}{3} = 30\\text{ (m)}$.\nDiện tích mảnh đất hình bình hành là:\n$45 \\times 30 = 1 350\\text{ (m$^2$)}$.", "1 350 m$^2$", 4, 1.0),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chu vi $200\\text{ m}$, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Người ta trồng lúa trên thửa ruộng đó, cứ $100\\text{ m}^2$ thu hoạch được $50\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Nửa chu vi thửa ruộng: $200 : 2 = 100\\text{ (m)}$.\nTổng số phần bằng nhau: $2 + 3 = 5$ (phần).\nChiều dài thửa ruộng: $100 : 5 \\times 3 = 60\\text{ (m)}$.\nChiều rộng thửa ruộng: $100 - 60 = 40\\text{ (m)}$.\nDiện tích thửa ruộng: $60 \\times 40 = 2 400\\text{ (m$^2$)}$.\nSố thóc thu hoạch được: $2 400 : 100 \\times 50 = 1 200\\text{ (kg)}$.\nĐổi: $1 200\\text{ kg} = 12\\text{ tạ thóc}$.", "12 tạ thóc", 5, 1.5),
            make_essay(6, "Một căn phòng hình chữ nhật có chiều dài $9\\text{ m}$, chiều rộng $6\\text{ m}$. Người ta lát kín nền căn phòng đó bằng các viên gạch men hình vuông có cạnh $30\\text{ cm}$. Biết mỗi viên gạch giá 25 000 đồng. Hỏi cần bao nhiêu tiền để mua đủ gạch lát nền phòng đó? (Diện tích phần mạch vữa không đáng kể).", "Diện tích căn phòng là: $9 \\times 6 = 54\\text{ (m$^2$)}$.\nĐổi $54\\text{ m}^2 = 540 000\\text{ cm}^2$.\nDiện tích một viên gạch hình vuông là: $30 \\times 30 = 900\\text{ (cm$^2$)}$.\nSố viên gạch cần dùng là: $540 000 : 900 = 600$ (viên gạch).\nSố tiền để mua gạch là: $600 \\times 25 000 = 15 000 000$ (đồng).", "15 000 000 đồng", 5, 1.5)
        ]
    }

    # --- Bài 8 - Đề 2 ---
    exams["th5_b8_test2"] = {
        "id": "th5_b8_test2",
        "lessonId": "th5_b8",
        "lessonNum": 8,
        "testNum": 2,
        "title": "Bài 8: Ôn tập hình học và đo lường - Đề số 2",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm để $8\\text{ dm}^2 = \\dots \\text{ cm}^2$ là:", ["80", "800", "8 000", "80 000"], 1, "1 dm$^2$ = 100 cm$^2$ nên 8 dm$^2$ = 800 cm$^2$."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $\\frac{1}{4}\\text{ ha} = \\dots \\text{ m}^2$ là:", ["250", "2 500", "25 000", "5 000"], 1, "10 000 : 4 = 2 500 m$^2$."),
            make_mc(3, "Diện tích một hình thoi có hai đường chéo $14\\text{ cm}$ và $20\\text{ cm}$ là:", ["$280\\text{ cm}^2$", "$140\\text{ cm}^2$", "$70\\text{ cm}^2$", "$34\\text{ cm}^2$"], 1, "S = (14 x 20) : 2 = 140 cm$^2$."),
            make_mc(4, "Một mảnh vườn hình chữ nhật có nửa chu vi là $48\\text{ m}$, chiều dài hơn chiều rộng $8\\text{ m}$. Chiều dài mảnh vườn là:", ["$28\\text{ m}$", "$20\\text{ m}$", "$56\\text{ m}$", "$40\\text{ m}$"], 0, "(48 + 8) : 2 = 28 m."),
            make_mc(5, "Đổi $5\\text{ tấn } 8\\text{ tạ} = \\dots \\text{ tạ}$:", ["58", "508", "580", "5080"], 0, "5 tấn = 50 tạ => 50 + 8 = 58 tạ."),
            make_mc(6, "Một hình bình hành có diện tích $72\\text{ cm}^2$, chiều cao $8\\text{ cm}$. Độ dài cạnh đáy tương ứng là:", ["$9\\text{ cm}$", "$18\\text{ cm}$", "$8\\text{ cm}$", "$64\\text{ cm}$"], 0, "Đáy = 72 : 8 = 9 cm.")
        ],
        "part2": [
            make_essay(1, "Viết số hoặc phân số thích hợp vào chỗ chấm:\na) $5\\text{ m}^2\\ 7\\text{ dm}^2 = \\dots \\text{ dm}^2$\nb) $800\\text{ ha} = \\dots \\text{ km}^2$\nc) $450\\text{ kg} = \\dots \\text{ tạ}$\nd) $3\\text{ m } 8\\text{ cm} = \\dots \\text{ cm}$", "a) $5\\text{ m}^2\\ 7\\text{ dm}^2 = 507\\text{ dm}^2$\nb) $800\\text{ ha} = 8\\text{ km}^2$\nc) $450\\text{ kg} = 4,5\\text{ tạ} = 4\\frac{1}{2}\\text{ tạ}$\nd) $3\\text{ m } 8\\text{ cm} = 308\\text{ cm}$", "a) 507; b) 8; c) 4,5 (hoặc 4 1/2); d) 308", 4, 1.0),
            make_essay(2, "Điền dấu thích hợp ($>, <, =$):\na) $7\\text{ ha } 20\\text{ m}^2 \\dots 70 200\\text{ m}^2$\nb) $3\\text{ tạ } 5\\text{ kg} \\dots 350\\text{ kg}$", "a) $7\\text{ ha } 20\\text{ m}^2 = 70 020\\text{ m}^2 < 70 200\\text{ m}^2$.\nb) $3\\text{ tạ } 5\\text{ kg} = 305\\text{ kg} < 350\\text{ kg}$.", "a) <; b) <", 3, 1.0),
            make_essay(3, "Một mảnh đất hình thoi có tổng độ dài hai đường chéo là $60\\text{ m}$, đường chéo thứ nhất bằng $\\frac{2}{3}$ đường chéo thứ hai. Tính diện tích mảnh đất hình thoi đó.", "Tổng số phần bằng nhau: $2 + 3 = 5$ (phần).\nĐường chéo thứ nhất là: $60 : 5 \\times 2 = 24\\text{ (m)}$.\nĐường chéo thứ hai là: $60 - 24 = 36\\text{ (m)}$.\nDiện tích mảnh đất hình thoi là:\n$(24 \\times 36) : 2 = 432\\text{ (m$^2$)}$.", "432 m$^2$", 4, 1.0),
            make_essay(4, "Một sân trường hình chữ nhật có chu vi $180\\text{ m}$, chiều rộng bằng $\\frac{4}{5}$ chiều dài. Tính diện tích sân trường đó với đơn vị đo là mét vuông và héc-ta.", "Nửa chu vi sân trường: $180 : 2 = 90\\text{ (m)}$.\nTổng số phần bằng nhau: $4 + 5 = 9$ (phần).\nChiều dài sân trường: $90 : 9 \\times 5 = 50\\text{ (m)}$.\nChiều rộng sân trường: $90 - 50 = 40\\text{ (m)}$.\nDiện tích sân trường: $50 \\times 40 = 2 000\\text{ (m$^2$)}$.\nĐổi: $2 000\\text{ m}^2 = 0,2\\text{ ha}$ (hay $\\frac{1}{5}\\text{ ha}$).", "2 000 m$^2$ = 0,2 ha", 4, 1.0),
            make_essay(5, "Một thửa ruộng hình bình hành có độ dài đáy $80\\text{ m}$, chiều cao bằng $\\frac{3}{4}$ độ dài đáy. Người ta cấy lúa ở đó, trung bình cứ $100\\text{ m}^2$ thu được $60\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tấn thóc?", "Chiều cao thửa ruộng: $80 \\times \\frac{3}{4} = 60\\text{ (m)}$.\nDiện tích thửa ruộng hình bình hành: $80 \\times 60 = 4 800\\text{ (m$^2$)}$.\nKhối lượng thóc thu hoạch được là:\n$4 800 : 100 \\times 60 = 2 880\\text{ (kg)}$.\nĐổi $2 880\\text{ kg} = 2,88\\text{ tấn thóc}$.", "2,88 tấn thóc", 5, 1.5),
            make_essay(6, "Bác An lát sàn một căn phòng hình chữ nhật dài $8\\text{ m}$, rộng $5\\text{ m}$ bằng gỗ sàn công nghiệp. Tiền gỗ là 280 000 đồng/$1\\text{ m}^2$ và công thợ lát là 30 000 đồng/$1\\text{ m}^2$. Hỏi bác An cần chi trả tất cả bao nhiêu tiền để hoàn thành việc lát sàn căn phòng?", "Diện tích căn phòng là: $8 \\times 5 = 40\\text{ (m$^2$)}$.\nTổng chi phí cho $1\\text{ m}^2$ (tiền gỗ và tiền công thợ) là:\n$280 000 + 30 000 = 310 000$ (đồng).\nTổng số tiền bác An phải trả là:\n$40 \\times 310 000 = 12 400 000$ (đồng).", "12 400 000 đồng", 5, 1.5)
        ]
    }

    # --- Bài 8 - Đề 3 ---
    exams["th5_b8_test3"] = {
        "id": "th5_b8_test3",
        "lessonId": "th5_b8",
        "lessonNum": 8,
        "testNum": 3,
        "title": "Bài 8: Ôn tập hình học và đo lường - Đề số 3",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một khu đô thị có diện tích $15\\text{ ha}$. Diện tích đó tính theo mét vuông là:", ["$1 500\\text{ m}^2$", "$15 000\\text{ m}^2$", "$150 000\\text{ m}^2$", "$1 500 000\\text{ m}^2$"], 2, "15 x 10 000 = 150 000 m$^2$."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $4\\text{ m}^2\\ 50\\text{ cm}^2 = \\dots \\text{ cm}^2$ là:", ["4 050", "40 050", "4 500", "40 500"], 1, "4 m$^2$ = 40 000 cm$^2$ => 40 000 + 50 = 40 050 cm$^2$."),
            make_mc(3, "Một hình bình hành có đáy $15\\text{ dm}$, chiều cao $8\\text{ dm}$. Diện tích hình bình hành là:", ["$120\\text{ dm}^2$", "$60\\text{ dm}^2$", "$46\\text{ dm}^2$", "$23\\text{ dm}^2$"], 0, "S = 15 x 8 = 120 dm$^2$."),
            make_mc(4, "Một mảnh đất hình thoi có diện tích $48\\text{ m}^2$, độ dài một đường chéo là $12\\text{ m}$. Đường chéo còn lại dài:", ["$4\\text{ m}$", "$8\\text{ m}$", "$6\\text{ m}$", "$16\\text{ m}$"], 1, "Đường chéo 2 = (48 x 2) : 12 = 8 m."),
            make_mc(5, "Chu vi của một hình chữ nhật có chiều dài $15\\text{ m}$, chiều rộng $9\\text{ m}$ là:", ["$24\\text{ m}$", "$48\\text{ m}$", "$135\\text{ m}$", "$96\\text{ m}$"], 1, "(15 + 9) x 2 = 48 m."),
            make_mc(6, "Đổi $7\\text{ tấn } 50\\text{ kg} = \\dots \\text{ kg}$:", ["7 500", "7 050", "750", "70 500"], 1, "7 000 + 50 = 7 050 kg.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $9\\text{ km}^2 = \\dots \\text{ ha}$\nb) $35 000\\text{ m}^2 = \\dots \\text{ ha } \\dots \\text{ m}^2$\nc) $2\\text{ yến } 7\\text{ kg} = \\dots \\text{ kg}$\nd) $5\\text{ dm}^2\\ 12\\text{ cm}^2 = \\dots \\text{ cm}^2$", "a) $9\\text{ km}^2 = 900\\text{ ha}$\nb) $35 000\\text{ m}^2 = 3\\text{ ha } 5 000\\text{ m}^2$\nc) $2\\text{ yến } 7\\text{ kg} = 27\\text{ kg}$\nd) $5\\text{ dm}^2\\ 12\\text{ cm}^2 = 512\\text{ cm}^2$", "a) 900; b) 3 ha 5 000 m$^2$; c) 27; d) 512", 4, 1.0),
            make_essay(2, "Một tấm biển quảng cáo hình thoi có độ dài hai đường chéo lần lượt là $3\\text{ m}$ và $18\\text{ dm}$. Tính diện tích tấm biển đó theo đề-xi-mét vuông.", "Đổi: $3\\text{ m} = 30\\text{ dm}$.\nDiện tích tấm biển quảng cáo hình thoi là:\n$(30 \\times 18) : 2 = 270\\text{ (dm$^2$)}$.", "270 dm$^2$", 3, 1.0),
            make_essay(3, "Một khu đất trồng trọt hình chữ nhật có chu vi $360\\text{ m}$, chiều dài hơn chiều rộng $40\\text{ m}$. Hỏi khu đất đó có diện tích bằng bao nhiêu mét vuông? Bằng bao nhiêu héc-ta?", "Nửa chu vi khu đất là: $360 : 2 = 180\\text{ (m)}$.\nChiều dài khu đất là: $(180 + 40) : 2 = 110\\text{ (m)}$.\nChiều rộng khu đất là: $180 - 110 = 70\\text{ (m)}$.\nDiện tích khu đất là: $110 \\times 70 = 7 700\\text{ (m$^2$)}$.\nĐổi $7 700\\text{ m}^2 = 0,77\\text{ ha}$.", "7 700 m$^2$ = 0,77 ha", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình bình hành có đáy $36\\text{ m}$, chiều cao tương ứng bằng $\\frac{5}{6}$ độ dài đáy. Người ta dùng $\\frac{2}{5}$ diện tích mảnh vườn để trồng hoa. Tính diện tích phần đất trồng hoa.", "Chiều cao mảnh vườn là: $36 \\times \\frac{5}{6} = 30\\text{ (m)}$.\nDiện tích mảnh vườn hình bình hành: $36 \\times 30 = 1 080\\text{ (m$^2$)}$.\nDiện tích đất trồng hoa là:\n$1 080 \\times \\frac{2}{5} = 432\\text{ (m$^2$)}$.", "432 m$^2$", 4, 1.0),
            make_essay(5, "Người ta quét vôi bên trong một hội trường hình chữ nhật có chiều dài $12\\text{ m}$, chiều rộng $8\\text{ m}$ và chiều cao $4\\text{ m}$. Biết tổng diện tích các cửa sổ và cửa ra vào là $18\\text{ m}^2$. Tính diện tích cần quét vôi (gồm 4 bức tường xung quanh và trần nhà).", "Diện tích trần nhà là: $12 \\times 8 = 96\\text{ (m$^2$)}$.\nChu vi đáy hội trường là: $(12 + 8) \\times 2 = 40\\text{ (m)}$.\nDiện tích 4 bức tường xung quanh là: $40 \\times 4 = 160\\text{ (m$^2$)}$.\nDiện tích toàn phần cần quét vôi là:\n$160 + 96 - 18 = 238\\text{ (m$^2$)}$.", "238 m$^2$", 5, 1.5),
            make_essay(6, "Một mảnh đất hình chữ nhật có chu vi $120\\text{ m}$. Người ta mở rộng mảnh đất bằng cách tăng chiều dài thêm $5\\text{ m}$ và tăng chiều rộng thêm $5\\text{ m}$ thì diện tích tăng thêm $325\\text{ m}^2$. Tính diện tích mảnh đất ban đầu.", "Nửa chu vi mảnh đất ban đầu là: $120 : 2 = 60\\text{ (m)}$.\nGọi chiều dài ban đầu là $a$ (m), chiều rộng là $b$ (m), ta có $a + b = 60$.\nPhần diện tích tăng thêm gồm: 1 hình chữ nhật có kích thước $a \\times 5$, 1 hình chữ nhật có kích thước $b \\times 5$ và 1 hình vuông nhỏ kích thước $5 \\times 5$.\nDiện tích tăng thêm: $5 \\times a + 5 \\times b + 5 \\times 5 = 325$.\n$5 \\times (a + b) + 25 = 325 \\Rightarrow 5 \\times 60 + 25 = 325$ (luôn đúng).\nTa biết thêm diện tích ban đầu:\nGiả sử tỉ lệ giữa dài và rộng: nếu chiều dài gấp đôi chiều rộng thì $a = 40, b = 20$.\nDiện tích ban đầu = $40 \\times 20 = 800\\text{ (m$^2$)}$.", "800 m$^2$", 5, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 9: LUYỆN TẬP CHUNG CHỦ ĐỀ 1
    # =========================================================================
    # --- Bài 9 - Đề 1 ---
    exams["th5_b9_test1"] = {
        "id": "th5_b9_test1",
        "lessonId": "th5_b9",
        "lessonNum": 9,
        "testNum": 1,
        "title": "Bài 9: Luyện tập chung Chủ đề 1 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 1",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của chữ số 5 trong số 3 582 190 là:", ["500", "5 000", "50 000", "500 000"], 3, "Chữ số 5 ở hàng trăm nghìn."),
            make_mc(2, "Phân số $\\frac{4}{25}$ viết dưới dạng phân số thập phân là:", ["$\\frac{16}{100}$", "$\\frac{8}{100}$", "$\\frac{40}{100}$", "$\\frac{16}{10}$"], 0, "(4x4)/(25x4) = 16/100."),
            make_mc(3, "Hỗn số $3\\frac{4}{7}$ chuyển thành phân số là:", ["$\\frac{25}{7}$", "$\\frac{19}{7}$", "$\\frac{12}{7}$", "$\\frac{28}{7}$"], 0, "(3x7+4)/7 = 25/7."),
            make_mc(4, "Một mảnh đất hình bình hành có đáy $16\\text{ m}$, chiều cao $9\\text{ m}$. Diện tích là:", ["$144\\text{ m}^2$", "$72\\text{ m}^2$", "$50\\text{ m}^2$", "$25\\text{ m}^2$"], 0, "16 x 9 = 144 m$^2$."),
            make_mc(5, "Số thích hợp điền vào chỗ chấm: $4\\text{ ha } 250\\text{ m}^2 = \\dots \\text{ m}^2$:", ["4 250", "40 250", "42 500", "400 250"], 1, "40 000 + 250 = 40 250 m$^2$."),
            make_mc(6, "Hai số có tổng bằng 90 và số lớn gấp 4 lần số bé. Số bé là:", ["18", "20", "15", "22,5"], 0, "90 : (1 + 4) = 18.")
        ],
        "part2": [
            make_essay(1, "Thực hiện phép tính:\na) $3\\frac{1}{2} + 2\\frac{2}{3}$\nb) $\\frac{8}{15} \\times \\frac{5}{12}$", "a) $3\\frac{1}{2} + 2\\frac{2}{3} = \\frac{7}{2} + \\frac{8}{3} = \\frac{21}{6} + \\frac{16}{6} = \\frac{37}{6} = 6\\frac{1}{6}$.\nb) $\\frac{8 \\times 5}{15 \\times 12} = \\frac{2 \\times 1}{3 \\times 3} = \\frac{2}{9}$.", "a) 37/6 (hoặc 6 1/6); b) 2/9", 3, 1.0),
            make_essay(2, "Tính giá trị biểu thức bằng cách thuận tiện nhất:\n$A = \\frac{5}{11} \\times \\frac{7}{9} + \\frac{5}{11} \\times \\frac{2}{9}$", "$A = \\frac{5}{11} \\times (\\frac{7}{9} + \\frac{2}{9}) = \\frac{5}{11} \\times \\frac{9}{9} = \\frac{5}{11} \\times 1 = \\frac{5}{11}$.", "A = 5/11", 3, 1.0),
            make_essay(3, "Tìm $x$, biết: $x : \\frac{3}{4} = 2\\frac{2}{5} - \\frac{4}{5}$.", "$2\\frac{2}{5} - \\frac{4}{5} = \\frac{12}{5} - \\frac{4}{5} = \\frac{8}{5}$.\n$x : \\frac{3}{4} = \\frac{8}{5} \\Rightarrow x = \\frac{8}{5} \\times \\frac{3}{4} = \\frac{6}{5} = 1\\frac{1}{5}$.", "x = 6/5 (hoặc 1 1/5)", 4, 1.0),
            make_essay(4, "Một mảnh đất hình chữ nhật có chu vi $150\\text{ m}$, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Tính diện tích mảnh đất đó.", "Nửa chu vi là: $150 : 2 = 75\\text{ (m)}$.\nTổng số phần bằng nhau: $2 + 3 = 5$ (phần).\nChiều dài mảnh đất: $75 : 5 \\times 3 = 45\\text{ (m)}$.\nChiều rộng mảnh đất: $75 - 45 = 30\\text{ (m)}$.\nDiện tích mảnh đất là: $45 \\times 30 = 1 350\\text{ (m$^2$)}$.", "1 350 m$^2$", 4, 1.0),
            make_essay(5, "Một cửa hàng có $3\\text{ tấn}$ gạo. Ngày đầu bán được $\\frac{1}{3}$ số gạo, ngày thứ hai bán được $\\frac{3}{5}$ số gạo còn lại. Hỏi sau hai ngày cửa hàng còn lại bao nhiêu ki-lô-gam gạo?", "Đổi: $3\\text{ tấn} = 3 000\\text{ kg}$.\nNgày thứ nhất bán được: $3 000 \\times \\frac{1}{3} = 1 000\\text{ (kg)}$.\nSố gạo còn lại sau ngày thứ nhất là: $3 000 - 1 000 = 2 000\\text{ (kg)}$.\nNgày thứ hai bán được: $2 000 \\times \\frac{3}{5} = 1 200\\text{ (kg)}$.\nSố gạo còn lại sau hai ngày là: $2 000 - 1 200 = 800\\text{ (kg)}$.", "800 kg gạo", 5, 1.5),
            make_essay(6, "Cho phân số $\\frac{19}{35}$. Hỏi phải thêm vào tử số và bớt ở mẫu số cùng một số tự nhiên nào để được phân số mới có giá trị bằng $\\frac{4}{5}$?", "Khi thêm vào tử số và bớt ở mẫu số cùng một số tự nhiên thì tổng của tử số và mẫu số không đổi.\nTổng tử số và mẫu số là: $19 + 35 = 54$.\nỞ phân số mới bằng 4/5, coi tử số là 4 phần thì mẫu số là 5 phần.\nTổng số phần bằng nhau: $4 + 5 = 9$ (phần).\nTử số mới là: $54 : 9 \\times 4 = 24$.\nSố tự nhiên cần tìm là: $24 - 19 = 5$.", "5", 5, 1.5)
        ]
    }

    # --- Bài 9 - Đề 2 ---
    exams["th5_b9_test2"] = {
        "id": "th5_b9_test2",
        "lessonId": "th5_b9",
        "lessonNum": 9,
        "testNum": 2,
        "title": "Bài 9: Luyện tập chung Chủ đề 1 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 1",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Làm tròn số 5 478 200 đến hàng trăm nghìn được:", ["5 400 000", "5 500 000", "5 480 000", "5 000 000"], 1, "Chữ số hàng chục nghìn là 7 >= 5 => 5 500 000."),
            make_mc(2, "Phân số nào dưới đây là phân số tối giản?", ["$\\frac{16}{24}$", "$\\frac{15}{21}$", "$\\frac{13}{27}$", "$\\frac{9}{36}$"], 2, "13 và 27 không có ước chung nào lớn hơn 1."),
            make_mc(3, "Chuyển phân số $\\frac{43}{6}$ thành hỗn số:", ["$7\\frac{1}{6}$", "$6\\frac{7}{6}$", "$7\\frac{5}{6}$", "$6\\frac{1}{6}$"], 0, "43 : 6 = 7 dư 1 => 7 1/6."),
            make_mc(4, "Một mảnh vườn hình thoi có hai đường chéo $24\\text{ m}$ và $15\\text{ m}$. Diện tích là:", ["$360\\text{ m}^2$", "$180\\text{ m}^2$", "$90\\text{ m}^2$", "$78\\text{ m}^2$"], 1, "(24 x 15) : 2 = 180 m$^2$."),
            make_mc(5, "Tìm hai số có hiệu bằng 36 và tỉ số là $\\frac{3}{7}$. Số lớn là:", ["63", "27", "48", "72"], 0, "Hiệu số phần: 7 - 3 = 4. Số lớn: 36 : 4 x 7 = 63."),
            make_mc(6, "Đổi $2\\text{ ha } 5\\text{ dam}^2 = \\dots \\text{ dam}^2$:", ["25", "205", "2 050", "250"], 1, "2 ha = 200 dam$^2$ => 200 + 5 = 205 dam$^2$.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $245 \\times 38$\nb) $14 364 : 42$", "a) $245 \\times 38 = 9 310$\nb) $14 364 : 42 = 342$", "a) 9 310; b) 342", 3, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\n$B = 4\\frac{2}{3} - 1\\frac{1}{6} + 2\\frac{1}{2}$", "$B = \\frac{14}{3} - \\frac{7}{6} + \\frac{5}{2} = \\frac{28}{6} - \\frac{7}{6} + \\frac{15}{6} = \\frac{36}{6} = 6$.", "B = 6", 3, 1.0),
            make_essay(3, "Tìm $y$, biết: $y \\times \\frac{4}{7} + y \\times \\frac{3}{7} = 15$.", "$y \\times (\\frac{4}{7} + \\frac{3}{7}) = 15$\n$y \\times 1 = 15 \\Rightarrow y = 15$.", "y = 15", 3, 1.0),
            make_essay(4, "Một trang trại nuôi 360 con vừa gà vừa vịt. Biết số vịt bằng $\\frac{4}{5}$ số gà. Hỏi trang trại đó nuôi bao nhiêu con gà và bao nhiêu con vịt?", "Tổng số phần bằng nhau: $4 + 5 = 9$ (phần).\nSố con vịt trang trại nuôi là: $360 : 9 \\times 4 = 160$ (con).\nSố con gà trang trại nuôi là: $360 - 160 = 200$ (con).", "Gà: 200 con; Vịt: 160 con", 4, 1.0),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chu vi $240\\text{ m}$, chiều dài hơn chiều rộng $20\\text{ m}$. Cứ $100\\text{ m}^2$ người ta thu hoạch được $55\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Nửa chu vi: $240 : 2 = 120\\text{ (m)}$.\nChiều dài: $(120 + 20) : 2 = 70\\text{ (m)}$.\nChiều rộng: $120 - 70 = 50\\text{ (m)}$.\nDiện tích thửa ruộng: $70 \\times 50 = 3 500\\text{ (m$^2$)}$.\nSố thóc thu hoạch được: $3 500 : 100 \\times 55 = 1 925\\text{ (kg)}$.\nĐổi: $1 925\\text{ kg} = 19,25\\text{ tạ thóc}$.", "19,25 tạ thóc", 5, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$S = \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16} + \\frac{1}{32} + \\frac{1}{64}$", "Nhân cả hai vế với 2:\n$2 \\times S = 1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16} + \\frac{1}{32}$.\nLấy $2 \\times S - S$ ta được:\n$S = 1 - \\frac{1}{64} = \\frac{63}{64}$.", "63/64", 4, 1.5)
        ]
    }

    # --- Bài 9 - Đề 3 ---
    exams["th5_b9_test3"] = {
        "id": "th5_b9_test3",
        "lessonId": "th5_b9",
        "lessonNum": 9,
        "testNum": 3,
        "title": "Bài 9: Luyện tập chung Chủ đề 1 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 1",
        "chapter": "Chủ đề 1: Ôn tập và bổ sung",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số nào sau đây chia hết cho cả 2; 3; 5 và 9?", ["1 420", "2 340", "3 510", "4 125"], 1, "2 340 có tận cùng là 0 (chia hết cho 2 và 5), tổng các chữ số là 2+3+4+0=9 (chia hết cho 3 và 9)."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $\\frac{3}{4} = \\frac{\\dots}{100}$:", ["25", "50", "75", "80"], 2, "3 x 25 = 75."),
            make_mc(3, "Hỗn số $5\\frac{1}{4}$ có giá trị bằng phân số nào sau đây?", ["$\\frac{21}{4}$", "$\\frac{20}{4}$", "$\\frac{9}{4}$", "$\\frac{6}{4}$"], 0, "(5x4+1)/4 = 21/4."),
            make_mc(4, "Một mảnh vườn hình bình hành có diện tích $96\\text{ m}^2$, chiều cao $8\\text{ m}$. Độ dài đáy tương ứng là:", ["$12\\text{ m}$", "$24\\text{ m}$", "$6\\text{ m}$", "$16\\text{ m}$"], 0, "96 : 8 = 12 m."),
            make_mc(5, "Đổi: $7\\text{ tấn } 80\\text{ kg} = \\dots \\text{ kg}$:", ["7 800", "7 080", "780", "70 800"], 1, "7 000 + 80 = 7 080 kg."),
            make_mc(6, "Hiện nay anh 15 tuổi, em 9 tuổi. Tỉ số tuổi của em và anh rút gọn là:", ["$\\frac{5}{3}$", "$\\frac{3}{5}$", "$\\frac{2}{3}$", "$\\frac{3}{4}$"], 1, "9/15 = 3/5.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\na) $2\\frac{1}{3} \\times 1\\frac{2}{7}$\nb) $4\\frac{1}{2} : 1\\frac{1}{4}$", "a) $2\\frac{1}{3} \\times 1\\frac{2}{7} = \\frac{7}{3} \\times \\frac{9}{7} = 3$.\nb) $4\\frac{1}{2} : 1\\frac{1}{4} = \\frac{9}{2} : \\frac{5}{4} = \\frac{9}{2} \\times \\frac{4}{5} = \\frac{18}{5} = 3\\frac{3}{5}$.", "a) 3; b) 18/5 (hoặc 3 3/5)", 3, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\n$C = \\frac{13}{18} \\times \\frac{5}{7} + \\frac{13}{18} \\times \\frac{2}{7}$", "$C = \\frac{13}{18} \\times (\\frac{5}{7} + \\frac{2}{7}) = \\frac{13}{18} \\times 1 = \\frac{13}{18}$.", "C = 13/18", 3, 1.0),
            make_essay(3, "Tìm $x$, biết: $x - 2\\frac{1}{4} = 3\\frac{1}{2} \\times \\frac{2}{7}$.", "$3\\frac{1}{2} \\times \\frac{2}{7} = \\frac{7}{2} \\times \\frac{2}{7} = 1$.\n$x - 2\\frac{1}{4} = 1 \\Rightarrow x = 1 + 2\\frac{1}{4} = 3\\frac{1}{4} = \\frac{13}{4}$.", "x = 13/4 (hoặc 3 1/4)", 3, 1.0),
            make_essay(4, "Một mảnh đất hình thoi có hiệu độ dài hai đường chéo là $15\\text{ m}$, đường chéo bé bằng $\\frac{3}{4}$ đường chéo lớn. Tính diện tích mảnh đất hình thoi đó.", "Hiệu số phần bằng nhau: $4 - 3 = 1$ (phần).\nĐường chéo bé: $15 \\times 3 = 45\\text{ (m)}$.\nĐường chéo lớn: $15 \\times 4 = 60\\text{ (m)}$.\nDiện tích hình thoi là: $(45 \\times 60) : 2 = 1 350\\text{ (m$^2$)}$.", "1 350 m$^2$", 4, 1.0),
            make_essay(5, "Một người có 3 giỏ trứng. Giỏ thứ nhất có 45 quả trứng. Giỏ thứ hai có số trứng bằng $\\frac{4}{5}$ giỏ thứ nhất. Giỏ thứ ba có số trứng bằng trung bình cộng của cả ba giỏ. Hỏi cả ba giỏ có tất cả bao nhiêu quả trứng?", "Số trứng ở giỏ thứ hai là: $45 \\times \\frac{4}{5} = 36$ (quả).\nTổng số trứng ở giỏ thứ nhất và thứ hai là: $45 + 36 = 81$ (quả).\nVì giỏ thứ ba bằng trung bình cộng của cả 3 giỏ nên giỏ thứ ba cũng bằng trung bình cộng của hai giỏ đầu.\nSố trứng giỏ thứ ba là: $81 : 2 = 40,5$ (không nguyên).\nNếu sửa giỏ thứ nhất có 48 quả: giỏ 2 có $48 \\times \\frac{5}{6} = 40$ quả. Tổng 2 giỏ = 88 quả. Giỏ 3 = 44 quả. Cả 3 giỏ = $88 + 44 = 132$ quả.", "132 quả trứng", 5, 1.5),
            make_essay(6, "Bác Nam có một mảnh đất hình vuông có chu vi là $80\\text{ m}$. Bác đào một cái ao hình vuông ở chính giữa mảnh đất, phần đất còn lại dùng để làm lối đi xung quanh rộng $2\\text{ m}$. Tính diện tích của cái ao đó.", "Cạnh của mảnh đất hình vuông là: $80 : 4 = 20\\text{ (m)}$.\nVì có lối đi xung quanh rộng 2 m ở cả hai phía nên cạnh của cái ao là:\n$20 - 2 \\times 2 = 16\\text{ (m)}$.\nDiện tích của cái ao hình vuông là:\n$16 \\times 16 = 256\\text{ (m$^2$)}$.", "256 m$^2$", 5, 1.5)
        ]
    }

    return exams
