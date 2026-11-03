# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 11: ÔN TẬP CUỐI NĂM (PHẦN 1: BÀI 56 ĐẾN BÀI 58)
Toán lớp 5 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 3 bài học x 3 đề độc lập = 9 đề thi (th5_b56_test1 -> th5_b58_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from th5_ch9_part1 import make_mc, make_essay

def get_ch11_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 56: ÔN TẬP VỀ SỐ TỰ NHIÊN, PHÂN SỐ, SỐ THẬP PHÂN
    # =========================================================================
    # --- Bài 56 - Đề 1 ---
    exams["th5_b56_test1"] = {
        "id": "th5_b56_test1",
        "lessonId": "th5_b56",
        "lessonNum": 56,
        "testNum": 1,
        "title": "Bài 56: Ôn tập về số tự nhiên, phân số, số thập phân - Đề số 1",
        "topic": "Ôn tập về số tự nhiên, phân số, số thập phân",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Chữ số 7 trong số thập phân 45,782 có giá trị là:", ["$\\frac{7}{10}$", "$\\frac{7}{100}$", "$\\frac{7}{1000}$", "7"], 0, "Chữ số 7 ở hàng phần mười nên có giá trị là 7/10."),
            make_mc(2, "Phân số $\\frac{3}{4}$ viết dưới dạng số thập phân là:", ["0,75", "0,34", "0,5", "0,25"], 0, "3/4 = 75/100 = 0,75."),
            make_mc(3, "Hỗn số $3\\frac{2}{5}$ viết dưới dạng số thập phân là:", ["3,4", "3,2", "3,25", "3,5"], 0, "2/5 = 0,4 => 3,4."),
            make_mc(4, "Số tự nhiên lớn nhất có 5 chữ số khác nhau là:", ["98 765", "99 999", "98 760", "98 675"], 0, "Chọn các chữ số giảm dần từ 9: 98 765."),
            make_mc(5, "Làm tròn số 84,567 đến hàng phần mười ta được:", ["84,6", "84,5", "85", "84,57"], 0, "Hàng phần trăm là 6 >= 5 nên làm tròn lên 84,6."),
            make_mc(6, "Số nào dưới đây chia hết cho cả 2; 3; 5 và 9?", ["1 350", "1 245", "1 430", "1 260"], 0, "1 350 tận cùng bằng 0 (chia hết cho 2 và 5), tổng các chữ số là 1+3+5+0=9 (chia hết cho 3 và 9).")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) $\\frac{36}{48}$\nb) $\\frac{45}{105}$", "a) $\\frac{36}{48} = \\frac{36 : 12}{48 : 12} = \\frac{3}{4}$.\nb) $\\frac{45}{105} = \\frac{45 : 15}{105 : 15} = \\frac{3}{7}$.", "a) 3/4; b) 3/7", 4, 1.0),
            make_essay(2, "Sắp xếp các số sau theo thứ tự từ bé đến lớn:\n$5,78; 5,87; 5,708; 5,8; 5,087$.", "So sánh các số:\n$5,087 < 5,708 < 5,78 < 5,8 < 5,87$.\nThứ tự tăng dần: $5,087; 5,708; 5,78; 5,8; 5,87$.", "5,087; 5,708; 5,78; 5,8; 5,87", 4, 1.0),
            make_essay(3, "Viết các số sau dưới dạng phân số thập phân có mẫu số là 100:\na) 0,65\nb) $\\frac{7}{25}$", "a) $0,65 = \\frac{65}{100}$.\nb) $\\frac{7}{25} = \\frac{7 \\times 4}{25 \\times 4} = \\frac{28}{100}$.", "a) 65/100; b) 28/100", 4, 1.0),
            make_essay(4, "Tìm $x$, biết: $x + 2,45 = 8,9 - 1,25$.", "$x + 2,45 = 7,65$\n$x = 7,65 - 2,45 = 5,2$.", "x = 5,2", 5, 1.5),
            make_essay(5, "Tìm hai số có tổng bằng 126 và tỉ số giữa chúng là $\\frac{3}{4}$.", "Tổng số phần bằng nhau là: $3 + 4 = 7$ (phần).\nSố bé là: $126 : 7 \\times 3 = 54$.\nSố lớn là: $126 - 54 = 72$.", "Số bé: 54; Số lớn: 72", 5, 1.5),
            make_essay(6, "Tìm số tự nhiên $a$ lớn nhất có hai chữ số sao cho $a$ chia hết cho cả 3 và 5.", "Để chia hết cho cả 3 và 5 thì số đó phải chia hết cho 15.\nSố tự nhiên có hai chữ số lớn nhất chia hết cho 15 là: $15 \\times 6 = 90$.", "a = 90", 4, 1.0)
        ]
    }

    # --- Bài 56 - Đề 2 ---
    exams["th5_b56_test2"] = {
        "id": "th5_b56_test2",
        "lessonId": "th5_b56",
        "lessonNum": 56,
        "testNum": 2,
        "title": "Bài 56: Ôn tập về số tự nhiên, phân số, số thập phân - Đề số 2",
        "topic": "Ôn tập về số tự nhiên, phân số, số thập phân",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Chữ số 5 trong số 128,456 thuộc hàng nào?", ["Hàng phần mười", "Hàng phần trăm", "Hàng phần nghìn", "Hàng đơn vị"], 1, "Chữ số 5 đứng ở vị trí thứ hai sau dấu phẩy là hàng phần trăm."),
            make_mc(2, "Phân số $\\frac{1}{8}$ viết dưới dạng số thập phân là:", ["0,125", "0,8", "0,18", "0,25"], 0, "1/8 = 125/1000 = 0,125."),
            make_mc(3, "Hỗn số $4\\frac{3}{4}$ chuyển thành phân số là:", ["$\\frac{19}{4}$", "$\\frac{16}{4}$", "$\\frac{15}{4}$", "$\\frac{12}{4}$"], 0, "(4x4+3)/4 = 19/4."),
            make_mc(4, "Trong các số sau, số nào là số chia hết cho 9?", ["34 521", "24 579", "51 282", "43 125"], 2, "51 282 có tổng các chữ số là 5+1+2+8+2=18 chia hết cho 9."),
            make_mc(5, "Làm tròn số 12,945 đến hàng đơn vị ta được:", ["13", "12", "12,9", "12,95"], 0, "Hàng phần mười là 9 >= 5 nên làm tròn lên 13."),
            make_mc(6, "Phân số tối giản trong các phân số sau là:", ["$\\frac{14}{21}$", "$\\frac{15}{25}$", "$\\frac{19}{27}$", "$\\frac{18}{30}$"], 2, "19 và 27 nguyên tố cùng nhau.")
        ],
        "part2": [
            make_essay(1, "Quy đồng mẫu số hai phân số:\na) $\\frac{5}{12}$ và $\\frac{7}{18}$\nb) $\\frac{3}{8}$ và $\\frac{5}{6}$", "a) MSC = 36. $\\frac{5}{12} = \\frac{15}{36}$; $\\frac{7}{18} = \\frac{14}{36}$.\nb) MSC = 24. $\\frac{3}{8} = \\frac{9}{24}$; $\\frac{5}{6} = \\frac{20}{24}$.", "a) 15/36 và 14/36; b) 9/24 và 20/24", 4, 1.0),
            make_essay(2, "Xếp các số sau theo thứ tự từ lớn đến bé:\n$8,65; 8,56; 8,605; 8,065; 8,655$.", "So sánh các số:\n$8,655 > 8,65 > 8,605 > 8,56 > 8,065$.\nThứ tự từ lớn đến bé: $8,655; 8,65; 8,605; 8,56; 8,065$.", "8,655; 8,65; 8,605; 8,56; 8,065", 4, 1.0),
            make_essay(3, "Tìm các số tự nhiên $y$ thỏa mãn: $4,85 < y < 8,12$.", "Các số tự nhiên lớn hơn 4,85 và nhỏ hơn 8,12 là: 5; 6; 7; 8.", "y = 5; 6; 7; 8", 4, 1.0),
            make_essay(4, "Tìm $x$, biết: $x \\times \\frac{2}{3} = \\frac{5}{6} - \\frac{1}{4}$.", "$\\frac{5}{6} - \\frac{1}{4} = \\frac{10}{12} - \\frac{3}{12} = \\frac{7}{12}$.\n$x = \\frac{7}{12} : \\frac{2}{3} = \\frac{7}{12} \\times \\frac{3}{2} = \\frac{7}{8}$.", "x = 7/8", 5, 1.5),
            make_essay(5, "Hai số có hiệu bằng 48 và số thứ nhất bằng $\\frac{5}{3}$ số thứ hai. Tìm hai số đó.", "Hiệu số phần bằng nhau: $5 - 3 = 2$ (phần).\nSố thứ hai (số bé) là: $48 : 2 \\times 3 = 72$.\nSố thứ nhất (số lớn) là: $72 + 48 = 120$.", "Số lớn: 120; Số bé: 72", 5, 1.5),
            make_essay(6, "Tìm số thập phân có hai chữ số ở phần thập phân lớn hơn 1,2 và nhỏ hơn 1,3 mà chữ số hàng phần trăm là số chẵn lớn nhất có một chữ số.", "Số thập phân có dạng $1,2a$ hoặc $1,28$.\nChữ số chẵn lớn nhất có một chữ số là 8, nên chữ số hàng phần trăm là 8.\nSố đó là 1,28 (thỏa mãn $1,20 < 1,28 < 1,30$).", "1,28", 4, 1.0)
        ]
    }

    # --- Bài 56 - Đề 3 ---
    exams["th5_b56_test3"] = {
        "id": "th5_b56_test3",
        "lessonId": "th5_b56",
        "lessonNum": 56,
        "testNum": 3,
        "title": "Bài 56: Ôn tập về số tự nhiên, phân số, số thập phân - Đề số 3",
        "topic": "Ôn tập về số tự nhiên, phân số, số thập phân",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của chữ số 9 trong số 25,394 là:", ["0,9", "0,09", "0,009", "9"], 1, "Chữ số 9 ở hàng phần trăm nên có giá trị là 0,09."),
            make_mc(2, "Phân số $\\frac{7}{20}$ viết dưới dạng số thập phân là:", ["0,35", "0,7", "0,035", "0,28"], 0, "7/20 = 35/100 = 0,35."),
            make_mc(3, "Hỗn số $2\\frac{3}{10}$ viết dưới dạng phân số là:", ["$\\frac{23}{10}$", "$\\frac{16}{10}$", "$\\frac{20}{10}$", "$\\frac{6}{10}$"], 0, "(2x10+3)/10 = 23/10."),
            make_mc(4, "Số tự nhiên bé nhất có 6 chữ số khác nhau là:", ["102 345", "100 000", "123 456", "102 354"], 0, "Các chữ số nhỏ nhất khác nhau bắt đầu từ 1: 102 345."),
            make_mc(5, "Làm tròn số 5,678 đến hàng phần trăm ta được:", ["5,68", "5,67", "5,7", "5,60"], 0, "Hàng phần nghìn là 8 >= 5 nên làm tròn lên 5,68."),
            make_mc(6, "Phân số nào dưới đây bằng phân số $\\frac{4}{5}$?", ["$\\frac{16}{20}$", "$\\frac{12}{16}$", "$\\frac{8}{15}$", "$\\frac{20}{30}$"], 0, "(4x4)/(5x4) = 16/20.")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau:\na) $\\frac{42}{56}$\nb) $\\frac{60}{140}$", "a) $\\frac{42}{56} = \\frac{42 : 14}{56 : 14} = \\frac{3}{4}$.\nb) $\\frac{60}{140} = \\frac{60 : 20}{140 : 20} = \\frac{3}{7}$.", "a) 3/4; b) 3/7", 4, 1.0),
            make_essay(2, "So sánh các phân số sau bằng cách hợp lí:\na) $\\frac{13}{17}$ và $\\frac{14}{17}$\nb) $\\frac{2025}{2026}$ và $\\frac{2026}{2027}$", "a) Cùng mẫu số: 13 < 14 nên $\\frac{13}{17} < \\frac{14}{17}$.\nb) So sánh phần bù với 1: $1 - \\frac{2025}{2026} = \\frac{1}{2026}$; $1 - \\frac{2026}{2027} = \\frac{1}{2027}$. Vì $\\frac{1}{2026} > \\frac{1}{2027}$ nên $\\frac{2025}{2026} < \\frac{2026}{2027}$.", "a) 13/17 < 14/17; b) 2025/2026 < 2026/2027", 4, 1.0),
            make_essay(3, "Viết các số đo sau dưới dạng số thập phân:\na) $4\\text{ m } 85\\text{ cm}$ (đơn vị mét)\nb) $2\\text{ tấn } 45\\text{ kg}$ (đơn vị tấn)", "a) $4\\text{ m } 85\\text{ cm} = 4,85\\text{ m}$.\nb) $2\\text{ tấn } 45\\text{ kg} = 2,045\\text{ tấn}$.", "a) 4,85 m; b) 2,045 tấn", 4, 1.0),
            make_essay(4, "Tìm $x$, biết: $x : 1,5 = 3,4 + 2,6$.", "$x : 1,5 = 6$\n$x = 6 \\times 1,5 = 9$.", "x = 9", 5, 1.5),
            make_essay(5, "Một lớp học có 40 học sinh, trong đó số học sinh nam bằng $\\frac{2}{3}$ số học sinh nữ. Tính số học sinh nam và số học sinh nữ của lớp đó.", "Tổng số phần bằng nhau: $2 + 3 = 5$ (phần).\nSố học sinh nam là: $40 : 5 \\times 2 = 16$ (học sinh).\nSố học sinh nữ là: $40 - 16 = 24$ (học sinh).", "Nam: 16 học sinh; Nữ: 24 học sinh", 5, 1.5),
            make_essay(6, "Tìm số thập phân $\\overline{a,b}$ biết khi xóa dấu phẩy của số đó ta được số tự nhiên gấp 10 lần số ban đầu và tổng của số tự nhiên đó với số ban đầu bằng 26,4.", "Khi xóa dấu phẩy thì số đó tăng gấp 10 lần.\nTổng của số tự nhiên mới và số ban đầu là $10 + 1 = 11$ lần số ban đầu.\nSố thập phân ban đầu là: $26,4 : 11 = 2,4$.", "2,4", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 57: ÔN TẬP CÁC PHÉP TÍNH VỚI SỐ ĐO ĐẠI LƯỢNG
    # =========================================================================
    # --- Bài 57 - Đề 1 ---
    exams["th5_b57_test1"] = {
        "id": "th5_b57_test1",
        "lessonId": "th5_b57",
        "lessonNum": 57,
        "testNum": 1,
        "title": "Bài 57: Ôn tập các phép tính với số đo đại lượng - Đề số 1",
        "topic": "Ôn tập các phép tính với số đo đại lượng",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $3\\text{ giờ } 25\\text{ phút} + 2\\text{ giờ } 40\\text{ phút}$ bằng:", ["6 giờ 5 phút", "5 giờ 65 phút", "6 giờ 15 phút", "5 giờ 5 phút"], 0, "5h 65p = 6 giờ 5 phút."),
            make_mc(2, "Tính: $4,5\\text{ tấn} + 350\\text{ kg} = \\dots \\text{ tấn}$:", ["4,85 tấn", "8 tấn", "4,535 tấn", "4,35 tấn"], 0, "350 kg = 0,35 tấn. 4,5 + 0,35 = 4,85 tấn."),
            make_mc(3, "Đổi $5\\text{ m}^2\\ 45\\text{ dm}^2 = \\dots \\text{ dm}^2$:", ["545 dm$^2$", "5045 dm$^2$", "5450 dm$^2$", "54,5 dm$^2$"], 0, "500 + 45 = 545 dm$^2$."),
            make_mc(4, "Tính: $5\\text{ phút } 30\\text{ giây} \\times 3$ bằng:", ["16 phút 30 giây", "15 phút 90 giây", "16 phút", "15 phút 30 giây"], 0, "15 phút 90 giây = 16 phút 30 giây."),
            make_mc(5, "Tính: $14\\text{ giờ } 20\\text{ phút} : 4$ bằng:", ["3 giờ 35 phút", "3 giờ 20 phút", "3 giờ 30 phút", "3 giờ 45 phút"], 0, "14h 20p = 12h 140p : 4 = 3 giờ 35 phút."),
            make_mc(6, "Một tấm vải dài $18\\text{ m}$. May 6 cái áo hết $10,8\\text{ m}$. Hỏi may mỗi cái áo hết bao nhiêu mét vải?", ["1,8 m", "1,6 m", "2 m", "1,5 m"], 0, "10,8 : 6 = 1,8 m.")
        ],
        "part2": [
            make_essay(1, "Thực hiện phép tính:\na) $5\\text{ giờ } 18\\text{ phút} + 3\\text{ giờ } 46\\text{ phút}$\nb) $8\\text{ phút } 15\\text{ giây} - 4\\text{ phút } 38\\text{ giây}$", "a) $5\\text{ giờ } 18\\text{ phút} + 3\\text{ giờ } 46\\text{ phút} = 8\\text{ giờ } 64\\text{ phút} = 9\\text{ giờ } 4\\text{ phút}$.\nb) $8\\text{ phút } 15\\text{ giây} - 4\\text{ phút } 38\\text{ giây} = 7\\text{ phút } 75\\text{ giây} - 4\\text{ phút } 38\\text{ giây} = 3\\text{ phút } 37\\text{ giây}$.", "a) 9 giờ 4 phút; b) 3 phút 37 giây", 4, 1.0),
            make_essay(2, "Thực hiện phép tính:\na) $2\\text{ giờ } 35\\text{ phút} \\times 4$\nb) $15\\text{ phút } 45\\text{ giây} : 5$", "a) $2\\text{ giờ } 35\\text{ phút} \\times 4 = 8\\text{ giờ } 140\\text{ phút} = 10\\text{ giờ } 20\\text{ phút}$.\nb) $15\\text{ phút } 45\\text{ giây} : 5 = 3\\text{ phút } 9\\text{ giây}$.", "a) 10 giờ 20 phút; b) 3 phút 9 giây", 4, 1.0),
            make_essay(3, "Viết số thích hợp vào chỗ chấm:\na) $4,5\\text{ ha} = \\dots \\text{ m}^2$\nb) $2,8\\text{ dm}^3 = \\dots \\text{ cm}^3$", "a) $4,5 \\times 10 000 = 45 000\\text{ m}^2$.\nb) $2,8 \\times 1000 = 2 800\\text{ cm}^3$.", "a) 45 000; b) 2 800", 4, 1.0),
            make_essay(4, "Một người làm việc buổi sáng từ 7 giờ 30 phút đến 11 giờ 30 phút, buổi chiều từ 13 giờ 15 phút đến 17 giờ. Hỏi cả ngày người đó làm việc bao nhiêu thời gian?", "Thời gian làm buổi sáng: $11\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ } 30\\text{ phút} = 4\\text{ giờ}$.\nThời gian làm buổi chiều: $17\\text{ giờ} - 13\\text{ giờ } 15\\text{ phút} = 3\\text{ giờ } 45\\text{ phút}$.\nTổng thời gian làm trong ngày: $4\\text{ giờ} + 3\\text{ giờ } 45\\text{ phút} = 7\\text{ giờ } 45\\text{ phút}$.", "7 giờ 45 phút", 5, 1.5),
            make_essay(5, "Một ô tô chở $3,5\\text{ tấn}$ hàng ở chuyến thứ nhất và $4\\text{ tấn } 200\\text{ kg}$ hàng ở chuyến thứ hai. Hỏi trung bình mỗi chuyến ô tô chở được bao nhiêu tấn hàng?", "Đổi: $4\\text{ tấn } 200\\text{ kg} = 4,2\\text{ tấn}$.\nTổng khối lượng hàng chở được trong hai chuyến là: $3,5 + 4,2 = 7,7\\text{ (tấn)}$.\nTrung bình mỗi chuyến ô tô chở được là: $7,7 : 2 = 3,85\\text{ (tấn)}$.", "3,85 tấn hàng", 5, 1.5),
            make_essay(6, "Một mảnh đất hình chữ nhật có chu vi $84\\text{ m}$, chiều rộng là $18,5\\text{ m}$. Tính diện tích mảnh đất đó.", "Nửa chu vi mảnh đất là: $84 : 2 = 42\\text{ (m)}$.\nChiều dài mảnh đất là: $42 - 18,5 = 23,5\\text{ (m)}$.\nDiện tích mảnh đất là: $23,5 \\times 18,5 = 434,75\\text{ (m$^2$)}$.", "434,75 m$^2$", 4, 1.0)
        ]
    }

    # --- Bài 57 - Đề 2 ---
    exams["th5_b57_test2"] = {
        "id": "th5_b57_test2",
        "lessonId": "th5_b57",
        "lessonNum": 57,
        "testNum": 2,
        "title": "Bài 57: Ôn tập các phép tính với số đo đại lượng - Đề số 2",
        "topic": "Ôn tập các phép tính với số đo đại lượng",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $4\\text{ ngày } 16\\text{ giờ} + 3\\text{ ngày } 12\\text{ giờ}$ bằng:", ["8 ngày 4 giờ", "7 ngày 28 giờ", "8 ngày 8 giờ", "7 ngày 4 giờ"], 0, "7 ngày 28 giờ = 8 ngày 4 giờ."),
            make_mc(2, "Tính: $8,4\\text{ km} - 3\\text{ km } 250\\text{ m} = \\dots \\text{ km}$:", ["5,15 km", "5,25 km", "5,150 km", "5,4 km"], 0, "3 km 250 m = 3,25 km. 8,4 - 3,25 = 5,15 km."),
            make_mc(3, "Đổi: $3\\text{ ha } 50\\text{ m}^2 = \\dots \\text{ m}^2$:", ["30 050 m$^2$", "3 050 m$^2$", "30 500 m$^2$", "350 m$^2$"], 0, "30 000 + 50 = 30 050 m$^2$."),
            make_mc(4, "Tính: $3\\text{ giờ } 12\\text{ phút} \\times 5$ bằng:", ["16 giờ", "15 giờ 60 phút", "16 giờ 12 phút", "15 giờ 12 phút"], 0, "15h 60p = 16 giờ."),
            make_mc(5, "Tính: $21\\text{ phút } 36\\text{ giây} : 3$ bằng:", ["7 phút 12 giây", "7 phút 18 giây", "6 phút 12 giây", "7 phút 6 giây"], 0, "21p : 3 = 7p; 36s : 3 = 12s => 7 phút 12 giây."),
            make_mc(6, "Một người thợ làm 1 chiếc bàn hết 3 giờ 15 phút. Làm 4 chiếc bàn như thế hết:", ["13 giờ", "12 giờ 60 phút", "13 giờ 15 phút", "12 giờ 15 phút"], 0, "3h 15p x 4 = 12h 60p = 13 giờ.")
        ],
        "part2": [
            make_essay(1, "Thực hiện phép tính:\na) $7\\text{ giờ } 45\\text{ phút} + 4\\text{ giờ } 35\\text{ phút}$\nb) $10\\text{ phút } 24\\text{ giây} - 5\\text{ phút } 45\\text{ giây}$", "a) $7\\text{ giờ } 45\\text{ phút} + 4\\text{ giờ } 35\\text{ phút} = 11\\text{ giờ } 80\\text{ phút} = 12\\text{ giờ } 20\\text{ phút}$.\nb) $10\\text{ phút } 24\\text{ giây} - 5\\text{ phút } 45\\text{ giây} = 9\\text{ phút } 84\\text{ giây} - 5\\text{ phút } 45\\text{ giây} = 4\\text{ phút } 39\\text{ giây}$.", "a) 12 giờ 20 phút; b) 4 phút 39 giây", 4, 1.0),
            make_essay(2, "Thực hiện phép tính:\na) $1\\text{ giờ } 45\\text{ phút} \\times 6$\nb) $17\\text{ giờ } 30\\text{ phút} : 5$", "a) $1\\text{ giờ } 45\\text{ phút} \\times 6 = 6\\text{ giờ } 270\\text{ phút} = 10\\text{ giờ } 30\\text{ phút}$.\nb) $17\\text{ giờ } 30\\text{ phút} : 5 = 3\\text{ giờ } 30\\text{ phút}$ (17h : 5 = 3h dư 2h = 120p; 150p : 5 = 30p).", "a) 10 giờ 30 phút; b) 3 giờ 30 phút", 4, 1.0),
            make_essay(3, "Viết số thích hợp vào chỗ chấm:\na) $0,75\\text{ m}^3 = \\dots \\text{ dm}^3$\nb) $450\\text{ kg} = \\dots \\text{ tạ}$", "a) $0,75 \\times 1000 = 750\\text{ dm}^3$.\nb) $450 : 100 = 4,5\\text{ tạ}$.", "a) 750; b) 4,5", 4, 1.0),
            make_essay(4, "Một người thợ đóng được 3 chiếc ghế hết 4 giờ 30 phút. Hỏi với năng suất đó, người thợ đóng 7 chiếc ghế cùng loại hết bao nhiêu thời gian?", "Thời gian đóng 1 chiếc ghế là:\n$4\\text{ giờ } 30\\text{ phút} : 3 = 1\\text{ giờ } 30\\text{ phút} = 1,5\\text{ giờ}$.\nThời gian đóng 7 chiếc ghế là:\n$1,5 \\times 7 = 10,5\\text{ (giờ)} = 10\\text{ giờ } 30\\text{ phút}$.", "10 giờ 30 phút (hoặc 10,5 giờ)", 5, 1.5),
            make_essay(5, "Một thửa ruộng thu hoạch được $2,4\\text{ tấn}$ thóc ở vụ xuân và $3\\text{ tấn } 150\\text{ kg}$ thóc ở vụ mùa. Hỏi cả hai vụ thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Đổi: $2,4\\text{ tấn} = 24\\text{ tạ}$; $3\\text{ tấn } 150\\text{ kg} = 31,5\\text{ tạ}$.\nTổng sản lượng thóc thu hoạch được cả hai vụ là:\n$24 + 31,5 = 55,5\\text{ (tạ thóc)}$.", "55,5 tạ thóc", 5, 1.5),
            make_essay(6, "Một hình vuông có chu vi $34\\text{ dm}$. Tính diện tích hình vuông đó theo mét vuông.", "Độ dài cạnh hình vuông là: $34 : 4 = 8,5\\text{ (dm)} = 0,85\\text{ (m)}$.\nDiện tích hình vuông là:\n$0,85 \\times 0,85 = 0,7225\\text{ (m$^2$)}$.", "0,7225 m$^2$", 4, 1.0)
        ]
    }

    # --- Bài 57 - Đề 3 ---
    exams["th5_b57_test3"] = {
        "id": "th5_b57_test3",
        "lessonId": "th5_b57",
        "lessonNum": 57,
        "testNum": 3,
        "title": "Bài 57: Ôn tập các phép tính với số đo đại lượng - Đề số 3",
        "topic": "Ôn tập các phép tính với số đo đại lượng",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $6\\text{ giờ } 35\\text{ phút} + 4\\text{ giờ } 45\\text{ phút}$ bằng:", ["11 giờ 20 phút", "10 giờ 80 phút", "11 giờ 15 phút", "10 giờ 20 phút"], 0, "10h 80p = 11 giờ 20 phút."),
            make_mc(2, "Tính: $15\\text{ kg } - 6\\text{ kg } 750\\text{ g} = \\dots \\text{ kg}$:", ["8,25 kg", "8,75 kg", "9,25 kg", "8,5 kg"], 0, "15 - 6,75 = 8,25 kg."),
            make_mc(3, "Đổi $2,5\\text{ m}^3 = \\dots \\text{ dm}^3$:", ["2 500 dm$^3$", "250 dm$^3$", "25 000 dm$^3$", "25 dm$^3$"], 0, "2,5 x 1000 = 2 500 dm$^3$."),
            make_mc(4, "Tính: $4\\text{ phút } 20\\text{ giây} \\times 4$ bằng:", ["17 phút 20 giây", "16 phút 80 giây", "17 phút", "16 phút 20 giây"], 0, "16p 80s = 17 phút 20 giây."),
            make_mc(5, "Tính: $25\\text{ giờ } 15\\text{ phút} : 3$ bằng:", ["8 giờ 25 phút", "8 giờ 15 phút", "8 giờ 45 phút", "8 giờ 5 phút"], 0, "25h 15p = 24h 75p : 3 = 8 giờ 25 phút."),
            make_mc(6, "Một bể nước chứa $1,8\\text{ m}^3$ nước. Viết số đo này theo lít là:", ["1 800 lít", "180 lít", "18 000 lít", "18 lít"], 0, "1 m$^3$ = 1 000 lít nên 1,8 m$^3$ = 1 800 lít.")
        ],
        "part2": [
            make_essay(1, "Thực hiện phép tính:\na) $6\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 55\\text{ phút}$\nb) $12\\text{ phút } 10\\text{ giây} - 7\\text{ phút } 45\\text{ giây}$", "a) $6\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 55\\text{ phút} = 8\\text{ giờ } 70\\text{ phút} = 9\\text{ giờ } 10\\text{ phút}$.\nb) $12\\text{ phút } 10\\text{ giây} - 7\\text{ phút } 45\\text{ giây} = 11\\text{ phút } 70\\text{ giây} - 7\\text{ phút } 45\\text{ giây} = 4\\text{ phút } 25\\text{ giây}$.", "a) 9 giờ 10 phút; b) 4 phút 25 giây", 4, 1.0),
            make_essay(2, "Thực hiện phép tính:\na) $3\\text{ giờ } 25\\text{ phút} \\times 4$\nb) $13\\text{ phút } 20\\text{ giây} : 4$", "a) $3\\text{ giờ } 25\\text{ phút} \\times 4 = 12\\text{ giờ } 100\\text{ phút} = 13\\text{ giờ } 40\\text{ phút}$.\nb) $13\\text{ phút } 20\\text{ giây} : 4 = 3\\text{ phút } 20\\text{ giây}$ (13p : 4 = 3p dư 1p = 60s; 80s : 4 = 20s).", "a) 13 giờ 40 phút; b) 3 phút 20 giây", 4, 1.0),
            make_essay(3, "Viết số thích hợp vào chỗ chấm:\na) $5,6\\text{ ha} = \\dots \\text{ m}^2$\nb) $4,25\\text{ tấn} = \\dots \\text{ kg}$", "a) $5,6 \\times 10 000 = 56 000\\text{ m}^2$.\nb) $4,25 \\times 1 000 = 4 250\\text{ kg}$.", "a) 56 000; b) 4 250", 4, 1.0),
            make_essay(4, "Một người thợ may may 5 cái áo hết 8 giờ 45 phút. Hỏi trung bình người đó may 1 chiếc áo hết bao nhiêu thời gian?", "Thời gian may 1 chiếc áo là:\n$8\\text{ giờ } 45\\text{ phút} : 5 = 1\\text{ giờ } 45\\text{ phút}$ (8h : 5 = 1h dư 3h = 180p; 225p : 5 = 45p).", "1 giờ 45 phút", 5, 1.5),
            make_essay(5, "Một bể kính nuôi cá dạng hình hộp chữ nhật có chiều dài $1,2\\text{ m}$, chiều rộng $0,8\\text{ m}$ và chiều cao $0,6\\text{ m}$. Hỏi bể đó có thể chứa tối đa bao nhiêu lít nước? (Biết $1\\text{ dm}^3 = 1\\text{ lít}$, thành bể mỏng không đáng kể).", "Thể tích của bể cá là:\n$1,2 \\times 0,8 \\times 0,6 = 0,576\\text{ (m$^3$)}$.\nĐổi sang đề-xi-mét khối (lít):\n$0,576\\text{ m}^3 = 576\\text{ dm}^3 = 576\\text{ lít}$.", "576 lít nước", 5, 1.5),
            make_essay(6, "Bác Hải đi xe máy từ nhà về quê hết 1 giờ 45 phút, sau đó đi tiếp từ quê sang nhà bạn hết 50 phút. Tổng thời gian bác Hải đi là bao nhiêu giờ, bao nhiêu phút?", "Tổng thời gian bác Hải đi là:\n$1\\text{ giờ } 45\\text{ phút} + 50\\text{ phút} = 1\\text{ giờ } 95\\text{ phút} = 2\\text{ giờ } 35\\text{ phút}$.", "2 giờ 35 phút", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 58: ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG
    # =========================================================================
    # --- Bài 58 - Đề 1 ---
    exams["th5_b58_test1"] = {
        "id": "th5_b58_test1",
        "lessonId": "th5_b58",
        "lessonNum": 58,
        "testNum": 1,
        "title": "Bài 58: Ôn tập hình học và đo lường - Đề số 1",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Diện tích hình tam giác có độ dài đáy $12\\text{ cm}$ và chiều cao $8\\text{ cm}$ là:", ["$48\\text{ cm}^2$", "$96\\text{ cm}^2$", "$20\\text{ cm}^2$", "$40\\text{ cm}^2$"], 0, "(12 x 8) : 2 = 48 cm$^2$."),
            make_mc(2, "Diện tích hình thang có đáy lớn $15\\text{ cm}$, đáy bé $9\\text{ cm}$ và chiều cao $6\\text{ cm}$ là:", ["$72\\text{ cm}^2$", "$144\\text{ cm}^2$", "$45\\text{ cm}^2$", "$36\\text{ cm}^2$"], 0, "(15 + 9) x 6 : 2 = 72 cm$^2$."),
            make_mc(3, "Chu vi hình tròn có bán kính $r = 5\\text{ cm}$ là:", ["$31,4\\text{ cm}$", "$15,7\\text{ cm}$", "$78,5\\text{ cm}$", "$62,8\\text{ cm}$"], 0, "C = 2 x 5 x 3,14 = 31,4 cm."),
            make_mc(4, "Diện tích hình tròn có đường kính $d = 10\\text{ cm}$ là:", ["$78,5\\text{ cm}^2$", "$314\\text{ cm}^2$", "$31,4\\text{ cm}^2$", "$157\\text{ cm}^2$"], 0, "r = 5 cm. S = 5 x 5 x 3,14 = 78,5 cm$^2$."),
            make_mc(5, "Thể tích hình lập phương có cạnh $4\\text{ dm}$ là:", ["$64\\text{ dm}^3$", "$16\\text{ dm}^3$", "$96\\text{ dm}^3$", "$48\\text{ dm}^3$"], 0, "4 x 4 x 4 = 64 dm$^3$."),
            make_mc(6, "Diện tích toàn phần của hình lập phương có cạnh $3\\text{ cm}$ là:", ["$54\\text{ cm}^2$", "$36\\text{ cm}^2$", "$27\\text{ cm}^2$", "$9\\text{ cm}^2$"], 0, "3 x 3 x 6 = 54 cm$^2$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích hình tam giác vuông có độ dài hai cạnh góc vuông là $18\\text{ cm}$ và $24\\text{ cm}$.", "Diện tích hình tam giác vuông là:\n$S = (18 \\times 24) : 2 = 216\\text{ (cm$^2$)}$.", "216 cm$^2$", 4, 1.0),
            make_essay(2, "Một mảnh đất hình thang có đáy lớn $35\\text{ m}$, đáy bé $25\\text{ m}$ và chiều cao $18\\text{ m}$. Tính diện tích mảnh đất đó.", "Diện tích mảnh đất hình thang là:\n$S = (35 + 25) \\times 18 : 2 = 60 \\times 18 : 2 = 540\\text{ (m$^2$)}$.", "540 m$^2$", 4, 1.0),
            make_essay(3, "Một bồn hoa hình tròn có đường kính $6\\text{ m}$. Tính chu vi và diện tích bồn hoa đó.", "Bán kính bồn hoa là: $6 : 2 = 3\\text{ (m)}$.\nChu vi bồn hoa là: $6 \\times 3,14 = 18,84\\text{ (m)}$.\nDiện tích bồn hoa là: $3 \\times 3 \\times 3,14 = 28,26\\text{ (m$^2$)}$.", "Chu vi: 18,84 m; Diện tích: 28,26 m$^2$", 4, 1.0),
            make_essay(4, "Một căn phòng dạng hình hộp chữ nhật có chiều dài $8\\text{ m}$, chiều rộng $5,5\\text{ m}$ và chiều cao $3,5\\text{ m}$. Người ta quét vôi bên trong căn phòng (gồm 4 bức tường xung quanh và trần nhà). Biết tổng diện tích các cửa là $9\\text{ m}^2$. Tính diện tích cần quét vôi.", "Diện tích trần nhà là: $8 \\times 5,5 = 44\\text{ (m$^2$)}$.\nChu vi đáy là: $(8 + 5,5) \\times 2 = 27\\text{ (m)}$.\nDiện tích xung quanh là: $27 \\times 3,5 = 94,5\\text{ (m$^2$)}$.\nDiện tích cần quét vôi là:\n$94,5 + 44 - 9 = 129,5\\text{ (m$^2$)}$.", "129,5 m$^2$", 5, 1.5),
            make_essay(5, "Một cái thùng tôn không có nắp dạng hình lập phương có cạnh dài $0,8\\text{ m}$.\na) Tính diện tích tôn dùng để làm chiếc thùng đó (không kể mép hàn).\nb) Tính thể tích chiếc thùng tôn đó theo lít.", "a) Thùng không nắp gồm 5 mặt:\nDiện tích tôn cần dùng là: $0,8 \\times 0,8 \\times 5 = 3,2\\text{ (m$^2$)}$.\nb) Thể tích chiếc thùng là:\n$0,8 \\times 0,8 \\times 0,8 = 0,512\\text{ (m$^3$)}$.\nĐổi sang lít: $0,512\\text{ m}^3 = 512\\text{ dm}^3 = 512\\text{ lít}$.", "a) 3,2 m$^2$; b) 512 lít", 5, 1.5),
            make_essay(6, "Bánh xe của một xe đạp có đường kính là $0,65\\text{ m}$. Hỏi người đi xe đạp đi được quãng đường dài bao nhiêu mét khi bánh xe lăn được 500 vòng trên mặt đất?", "Chu vi bánh xe đạp là: $0,65 \\times 3,14 = 2,041\\text{ (m)}$.\nQuãng đường đi được sau 500 vòng lăn là:\n$2,041 \\times 500 = 1 020,5\\text{ (m)}$.", "1 020,5 m", 4, 1.0)
        ]
    }

    # --- Bài 58 - Đề 2 ---
    exams["th5_b58_test2"] = {
        "id": "th5_b58_test2",
        "lessonId": "th5_b58",
        "lessonNum": 58,
        "testNum": 2,
        "title": "Bài 58: Ôn tập hình học và đo lường - Đề số 2",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình tam giác có diện tích $36\\text{ cm}^2$, chiều cao $6\\text{ cm}$. Độ dài cạnh đáy tương ứng là:", ["$12\\text{ cm}$", "$6\\text{ cm}$", "$18\\text{ cm}$", "$8\\text{ cm}$"], 0, "Đáy = (36 x 2) : 6 = 12 cm."),
            make_mc(2, "Diện tích hình thang có hai đáy lần lượt là $12\\text{ dm}$ và $8\\text{ dm}$, chiều cao $5\\text{ dm}$ là:", ["$50\\text{ dm}^2$", "$100\\text{ dm}^2$", "$48\\text{ dm}^2$", "$25\\text{ dm}^2$"], 0, "(12 + 8) x 5 : 2 = 50 dm$^2$."),
            make_mc(3, "Một hình tròn có chu vi $18,84\\text{ dm}$. Bán kính của hình tròn đó là:", ["$3\\text{ dm}$", "$6\\text{ dm}$", "$2\\text{ dm}$", "$4\\text{ dm}$"], 0, "r = 18,84 : 2 : 3,14 = 3 dm."),
            make_mc(4, "Một hình hộp chữ nhật có các kích thước dài $6\\text{ cm}$, rộng $4\\text{ cm}$, cao $5\\text{ cm}$. Thể tích là:", ["$120\\text{ cm}^3$", "$60\\text{ cm}^3$", "$148\\text{ cm}^3$", "$74\\text{ cm}^3$"], 0, "6 x 4 x 5 = 120 cm$^3$."),
            make_mc(5, "Diện tích xung quanh của hình lập phương có cạnh $5\\text{ cm}$ là:", ["$100\\text{ cm}^2$", "$150\\text{ cm}^2$", "$125\\text{ cm}^2$", "$25\\text{ cm}^2$"], 0, "5 x 5 x 4 = 100 cm$^2$."),
            make_mc(6, "Bán kính hình tròn tăng lên 2 lần thì diện tích hình tròn tăng lên:", ["4 lần", "2 lần", "8 lần", "Không đổi"], 0, "Diện tích tỉ lệ với bình phương bán kính nên tăng 2 x 2 = 4 lần.")
        ],
        "part2": [
            make_essay(1, "Một thửa ruộng hình tam giác có độ dài cạnh đáy $40\\text{ m}$, chiều cao bằng $\\frac{3}{4}$ độ dài đáy. Tính diện tích thửa ruộng đó.", "Chiều cao thửa ruộng là: $40 \\times \\frac{3}{4} = 30\\text{ (m)}$.\nDiện tích thửa ruộng là: $(40 \\times 30) : 2 = 600\\text{ (m$^2$)}$.", "600 m$^2$", 4, 1.0),
            make_essay(2, "Một mảnh vườn hình thang có đáy lớn $45\\text{ m}$, đáy bé bằng $\\frac{2}{3}$ đáy lớn, chiều cao $20\\text{ m}$. Tính diện tích mảnh vườn hình thang.", "Đáy bé mảnh vườn là: $45 \\times \\frac{2}{3} = 30\\text{ (m)}$.\nDiện tích mảnh vườn là: $(45 + 30) \\times 20 : 2 = 750\\text{ (m$^2$)}$.", "750 m$^2$", 4, 1.0),
            make_essay(3, "Một mặt bàn hình tròn có bán kính $0,6\\text{ m}$. Tính diện tích mặt bàn đó.", "Diện tích mặt bàn hình tròn là:\n$S = 0,6 \\times 0,6 \\times 3,14 = 1,1304\\text{ (m$^2$)}$.", "1,1304 m$^2$", 4, 1.0),
            make_essay(4, "Một bể nước dạng hình hộp chữ nhật có kích thước bên trong là: chiều dài $2,5\\text{ m}$, chiều rộng $1,6\\text{ m}$ và chiều sâu $1,2\\text{ m}$.\na) Tính thể tích của bể nước.\nb) Hiện nay mực nước trong bể cao bằng $\\frac{3}{4}$ chiều sâu của bể. Hỏi trong bể đang có bao nhiêu lít nước?", "a) Thể tích của bể là: $2,5 \\times 1,6 \\times 1,2 = 4,8\\text{ (m$^3$)}$.\nb) Thể tích nước hiện có trong bể là:\n$4,8 \\times \\frac{3}{4} = 3,6\\text{ (m$^3$)}$.\nĐổi sang lít: $3,6\\text{ m}^3 = 3 600\\text{ dm}^3 = 3 600\\text{ lít}$.", "a) 4,8 m$^3$; b) 3 600 lít nước", 5, 1.5),
            make_essay(5, "Một thửa ruộng hình thang có diện tích $960\\text{ m}^2$, chiều cao $24\\text{ m}$. Biết đáy lớn hơn đáy bé $10\\text{ m}$. Tính độ dài đáy lớn và đáy bé của thửa ruộng.", "Tổng độ dài hai đáy là:\n$(960 \\times 2) : 24 = 80\\text{ (m)}$.\nĐáy lớn thửa ruộng là: $(80 + 10) : 2 = 45\\text{ (m)}$.\nĐáy bé thửa ruộng là: $80 - 45 = 35\\text{ (m)}$.", "Đáy lớn: 45 m; Đáy bé: 35 m", 5, 1.5),
            make_essay(6, "Bác Hải có một cái sân hình chữ nhật dài $15\\text{ m}$, rộng $6\\text{ m}$. Bác làm một bồn hoa hình tròn ở giữa sân có bán kính $1,5\\text{ m}$. Phần diện tích còn lại lát gạch chống trượt. Tính diện tích phần sân lát gạch chống trượt.", "Diện tích cả cái sân là: $15 \\times 6 = 90\\text{ (m$^2$)}$.\nDiện tích bồn hoa hình tròn là: $1,5 \\times 1,5 \\times 3,14 = 7,065\\text{ (m$^2$)}$.\nDiện tích phần sân lát gạch chống trượt là:\n$90 - 7,065 = 82,935\\text{ (m$^2$)}$.", "82,935 m$^2$", 4, 1.0)
        ]
    }

    # --- Bài 58 - Đề 3 ---
    exams["th5_b58_test3"] = {
        "id": "th5_b58_test3",
        "lessonId": "th5_b58",
        "lessonNum": 58,
        "testNum": 3,
        "title": "Bài 58: Ôn tập hình học và đo lường - Đề số 3",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình tam giác có đáy $15\\text{ cm}$ và chiều cao $8\\text{ cm}$. Diện tích là:", ["$60\\text{ cm}^2$", "$120\\text{ cm}^2$", "$30\\text{ cm}^2$", "$50\\text{ cm}^2$"], 0, "(15 x 8) : 2 = 60 cm$^2$."),
            make_mc(2, "Diện tích hình thang có đáy lớn $20\\text{ m}$, đáy bé $14\\text{ m}$ và chiều cao $10\\text{ m}$ là:", ["$170\\text{ m}^2$", "$340\\text{ m}^2$", "$140\\text{ m}^2$", "$150\\text{ m}^2$"], 0, "(20 + 14) x 10 : 2 = 170 m$^2$."),
            make_mc(3, "Bán kính hình tròn có chu vi $12,56\\text{ cm}$ là:", ["$2\\text{ cm}$", "$4\\text{ cm}$", "$1\\text{ cm}$", "$3\\text{ cm}$"], 0, "r = 12,56 : 2 : 3,14 = 2 cm."),
            make_mc(4, "Một khối gỗ hình lập phương có diện tích toàn phần là $96\\text{ cm}^2$. Thể tích khối gỗ đó là:", ["$64\\text{ cm}^3$", "$16\\text{ cm}^3$", "$32\\text{ cm}^3$", "$128\\text{ cm}^3$"], 0, "Diện tích 1 mặt = 96 : 6 = 16 cm$^2$ => cạnh = 4 cm. V = 4 x 4 x 4 = 64 cm$^3$."),
            make_mc(5, "Thể tích hình hộp chữ nhật có chiều dài $8\\text{ dm}$, chiều rộng $5\\text{ dm}$, chiều cao $6\\text{ dm}$ là:", ["$240\\text{ dm}^3$", "$120\\text{ dm}^3$", "$190\\text{ dm}^3$", "$200\\text{ dm}^3$"], 0, "8 x 5 x 6 = 240 dm$^3$."),
            make_mc(6, "Diện tích xung quanh của hình hộp chữ nhật có chu vi đáy $24\\text{ m}$ và chiều cao $3,5\\text{ m}$ là:", ["$84\\text{ m}^2$", "$42\\text{ m}^2$", "$168\\text{ m}^2$", "$96\\text{ m}^2$"], 0, "24 x 3,5 = 84 m$^2$.")
        ],
        "part2": [
            make_essay(1, "Một tấm biển quảng cáo hình tam giác có độ dài đáy $3,6\\text{ m}$ và chiều cao $2,5\\text{ m}$. Tính diện tích tấm biển quảng cáo đó.", "Diện tích tấm biển hình tam giác là:\n$S = (3,6 \\times 2,5) : 2 = 4,5\\text{ (m$^2$)}$.", "4,5 m$^2$", 4, 1.0),
            make_essay(2, "Một mảnh vườn hình thang có tổng độ dài hai đáy là $64\\text{ m}$, chiều cao bằng $\\frac{3}{8}$ tổng độ dài hai đáy. Tính diện tích mảnh vườn đó.", "Chiều cao mảnh vườn là: $64 \\times \\frac{3}{8} = 24\\text{ (m)}$.\nDiện tích mảnh vườn hình thang là: $(64 \\times 24) : 2 = 768\\text{ (m$^2$)}$.", "768 m$^2$", 4, 1.0),
            make_essay(3, "Một biển báo giao thông hình tròn có đường kính $50\\text{ cm}$. Tính chu vi và diện tích của biển báo đó.", "Bán kính biển báo là: $50 : 2 = 25\\text{ (cm)}$.\nChu vi biển báo là: $50 \\times 3,14 = 157\\text{ (cm)}$.\nDiện tích biển báo là: $25 \\times 25 \\times 3,14 = 1 962,5\\text{ (cm$^2$)}$.", "Chu vi: 157 cm; Diện tích: 1 962,5 cm$^2$", 4, 1.0),
            make_essay(4, "Một căn phòng học hình hộp chữ nhật có chiều dài $9\\text{ m}$, chiều rộng $6\\text{ m}$ và chiều cao $3,8\\text{ m}$. Người ta sơn tường bên trong phòng học (gồm 4 bức tường và trần nhà). Biết tổng diện tích các cửa là $12\\text{ m}^2$. Tính diện tích cần sơn.", "Diện tích trần nhà là: $9 \\times 6 = 54\\text{ (m$^2$)}$.\nChu vi đáy căn phòng là: $(9 + 6) \\times 2 = 30\\text{ (m)}$.\nDiện tích 4 bức tường xung quanh là: $30 \\times 3,8 = 114\\text{ (m$^2$)}$.\nDiện tích cần sơn là: $114 + 54 - 12 = 156\\text{ (m$^2$)}$.", "156 m$^2$", 5, 1.5),
            make_essay(5, "Một bể bơi hình hộp chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $12\\text{ m}$ và chiều sâu trung bình là $1,5\\text{ m}$. Người ta dùng gạch men hình vuông cạnh $20\\text{ cm}$ để lát kín đáy và 4 mặt xung quanh thành bể.\na) Tính diện tích cần lát gạch men.\nb) Cần bao nhiêu viên gạch men để lát đủ bể bơi đó?", "a) Diện tích đáy bể bơi: $25 \\times 12 = 300\\text{ (m$^2$)}$.\nDiện tích xung quanh bể: $(25 + 12) \\times 2 \\times 1,5 = 111\\text{ (m$^2$)}$.\nDiện tích cần lát gạch men: $300 + 111 = 411\\text{ (m$^2$)}$.\nb) Đổi: $411\\text{ m}^2 = 411 0000\\text{ cm}^2$.\nDiện tích một viên gạch men là: $20 \\times 20 = 400\\text{ (cm$^2$)}$.\nSố viên gạch men cần dùng là: $4 110 000 : 400 = 10 275$ (viên).", "a) 411 m$^2$; b) 10 275 viên gạch", 5, 1.5),
            make_essay(6, "Bánh xe của một ô tô có bán kính $0,35\\text{ m}$. Hỏi khi ô tô đi được quãng đường dài $2,198\\text{ km}$ thì bánh xe đã lăn được bao nhiêu vòng trên mặt đất?", "Chu vi của bánh xe ô tô là: $0,35 \\times 2 \\times 3,14 = 2,198\\text{ (m)}$.\nĐổi quãng đường sang mét: $2,198\\text{ km} = 2 198\\text{ m}$.\nSố vòng bánh xe lăn được là:\n$2 198 : 2,198 = 1 000$ (vòng).", "1 000 vòng", 4, 1.0)
        ]
    }

    return exams
