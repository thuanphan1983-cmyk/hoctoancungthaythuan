# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 2: SỐ THẬP PHÂN (BÀI 10 VÀ BÀI 11) - TOÁN 5 KNTT
Mỗi bài có đúng 3 đề kiểm tra độc lập (test1, test2, test3):
- 6 câu trắc nghiệm (part1, mỗi câu 0.5 điểm = 3.0 điểm)
- 6 câu tự luận (part2, 4 câu 1.0 đ + 2 câu 1.5 đ = 7.0 điểm, lineCount: 3 đến 6 dòng)
Tổng điểm: 10.0 điểm, thời gian: 35 phút.
"""
from th5_ch1_part1 import make_mc, make_essay

def get_ch2_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 10: KHÁI NIỆM SỐ THẬP PHÂN
    # =========================================================================
    # --- Bài 10 - Đề 1 ---
    exams["th5_b10_test1"] = {
        "id": "th5_b10_test1",
        "lessonId": "th5_b10",
        "lessonNum": 10,
        "testNum": 1,
        "title": "Bài 10: Khái niệm số thập phân - Đề số 1",
        "topic": "Khái niệm số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thập phân gồm có mấy phần?", ["1 phần", "2 phần", "3 phần", "4 phần"], 1, "Số thập phân gồm hai phần: phần nguyên và phần thập phân, ngăn cách bởi dấu phẩy."),
            make_mc(2, "Chữ số 5 trong số thập phân 24,58 có giá trị là:", ["5", "$\\frac{5}{10}$", "$\\frac{5}{100}$", "$\\frac{5}{1000}$"], 1, "Chữ số 5 đứng ngay sau dấu phẩy ở hàng phần mười nên có giá trị là 5/10 (hay 0,5)."),
            make_mc(3, "Số thập phân 'Bốn mươi hai đơn vị, bảy phần trăm' viết là:", ["42,7", "42,07", "42,007", "420,7"], 1, "Phần nguyên là 42, phần trăm là 7 nên viết là 42,07."),
            make_mc(4, "Phân số thập phân $\\frac{35}{100}$ được viết dưới dạng số thập phân là:", ["3,5", "0,35", "0,035", "35,0"], 1, "35/100 = 0,35."),
            make_mc(5, "Khi viết thêm chữ số 0 vào bên phải phần thập phân của một số thập phân thì:", [
                "Giá trị của số đó tăng lên 10 lần",
                "Giá trị của số đó giảm đi 10 lần",
                "Giá trị của số đó không thay đổi",
                "Phần nguyên của số đó thay đổi"
            ], 2, "Nếu viết thêm hoặc bỏ bớt chữ số 0 ở tận cùng bên phải phần thập phân thì được một số thập phân bằng nó."),
            make_mc(6, "Số nào dưới đây bằng số 3,4?", ["3,04", "3,40", "3,004", "0,34"], 1, "3,4 = 3,40 (thêm 0 vào tận cùng bên phải).")
        ],
        "part2": [
            make_essay(1, "Viết các phân số thập phân sau thành số thập phân:\na) $\\frac{7}{10}$\nb) $\\frac{85}{100}$\nc) $\\frac{249}{1000}$\nd) $\\frac{125}{100}$", "a) $\\frac{7}{10} = 0,7$\nb) $\\frac{85}{100} = 0,85$\nc) $\\frac{249}{1000} = 0,249$\nd) $\\frac{125}{100} = 1,25$", "a) 0,7; b) 0,85; c) 0,249; d) 1,25", 4, 1.0),
            make_essay(2, "Nêu phần nguyên, phần thập phân và giá trị theo vị trí của mỗi chữ số trong số thập phân 63,582.", "Số 63,582 gồm:\n- Phần nguyên là 63 (gồm 6 chục và 3 đơn vị).\n- Phần thập phân là 582 (gồm 5 phần mười, 8 phần trăm và 2 phần nghìn).", "Phần nguyên: 63; Phần thập phân: 582 (5 phần mười, 8 phần trăm, 2 phần nghìn)", 4, 1.0),
            make_essay(3, "Viết các số thập phân sau thành phân số thập phân:\na) 0,9\nb) 0,45\nc) 1,28\nd) 0,075", "a) $0,9 = \\frac{9}{10}$\nb) $0,45 = \\frac{45}{100}$\nc) $1,28 = \\frac{128}{100}$\nd) $0,075 = \\frac{75}{1000}$", "a) 9/10; b) 45/100; c) 128/100; d) 75/1000", 4, 1.0),
            make_essay(4, "Viết các số sau dưới dạng số thập phân gọn nhất (bỏ các chữ số 0 thừa ở tận cùng):\na) 45,600\nb) 7,050\nc) 120,4000\nd) 0,80", "a) $45,600 = 45,6$\nb) $7,050 = 7,05$\nc) $120,4000 = 120,4$\nd) $0,80 = 0,8$", "a) 45,6; b) 7,05; c) 120,4; d) 0,8", 4, 1.0),
            make_essay(5, "Viết các hỗn số sau thành số thập phân:\na) $3\\frac{4}{10}$\nb) $15\\frac{7}{100}$\nc) $8\\frac{25}{1000}$\nd) $2\\frac{1}{2}$", "a) $3\\frac{4}{10} = 3,4$\nb) $15\\frac{7}{100} = 15,07$\nc) $8\\frac{25}{1000} = 8,025$\nd) $2\\frac{1}{2} = 2\\frac{5}{10} = 2,5$", "a) 3,4; b) 15,07; c) 8,025; d) 2,5", 4, 1.5),
            make_essay(6, "Từ các chữ số 0; 2; 5 và dấu phẩy, hãy viết tất cả các số thập phân có 3 chữ số khác nhau và phần thập phân có 2 chữ số.", "Số thập phân cần lập có dạng: $a,bc$ với $a, b, c \\in \\{0; 2; 5\\}$ khác nhau và $a \\neq 0$.\n- Nếu phần nguyên là 2: ta có các số 2,05 và 2,50.\n- Nếu phần nguyên là 5: ta có các số 5,02 và 5,20.\nVậy có tất cả 4 số thỏa mãn là: 2,05; 2,50; 5,02; 5,20.", "4 số: 2,05; 2,50; 5,02; 5,20", 5, 1.5)
        ]
    }

    # --- Bài 10 - Đề 2 ---
    exams["th5_b10_test2"] = {
        "id": "th5_b10_test2",
        "lessonId": "th5_b10",
        "lessonNum": 10,
        "testNum": 2,
        "title": "Bài 10: Khái niệm số thập phân - Đề số 2",
        "topic": "Khái niệm số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Chữ số 8 trong số 135,486 có giá trị là:", ["8", "0,8", "0,08", "0,008"], 2, "Chữ số 8 thuộc hàng phần trăm nên có giá trị là 0,08."),
            make_mc(2, "Số thập phân 'Bảy trăm linh hai đơn vị, năm phần mười, sáu phần nghìn' viết là:", ["702,56", "702,506", "702,056", "720,506"], 1, "Phần nguyên là 702, phần mười là 5, phần trăm là 0, phần nghìn là 6: 702,506."),
            make_mc(3, "Hỗn số $4\\frac{3}{100}$ viết dưới dạng số thập phân là:", ["4,3", "4,03", "4,003", "43,0"], 1, "4 và 3 phần trăm viết là 4,03."),
            make_mc(4, "Số 0,008 đọc là:", ["Không phẩy tám", "Không phẩy không tám", "Không phẩy không không tám", "Tám phần trăm"], 2, "Đọc là không phẩy không không tám (hoặc tám phần nghìn)."),
            make_mc(5, "Số thập phân nào sau đây bằng số 5,600?", ["5,06", "5,6", "5,006", "0,56"], 1, "Bỏ hai chữ số 0 ở tận cùng phần thập phân được 5,6."),
            make_mc(6, "Phân số $\\frac{3}{4}$ viết dưới dạng số thập phân là:", ["0,34", "0,75", "0,5", "0,25"], 1, "3/4 = 75/100 = 0,75.")
        ],
        "part2": [
            make_essay(1, "Viết các số thập phân sau thành phân số thập phân rồi rút gọn thành phân số tối giản:\na) 0,4\nb) 0,25\nc) 0,65", "a) $0,4 = \\frac{4}{10} = \\frac{2}{5}$\nb) $0,25 = \\frac{25}{100} = \\frac{1}{4}$\nc) $0,65 = \\frac{65}{100} = \\frac{13}{20}$", "a) 2/5; b) 1/4; c) 13/20", 4, 1.0),
            make_essay(2, "Chuyển các phân số sau thành số thập phân:\na) $\\frac{3}{5}$\nb) $\\frac{7}{2}$\nc) $\\frac{11}{20}$\nd) $\\frac{1}{8}$", "a) $\\frac{3}{5} = \\frac{6}{10} = 0,6$\nb) $\\frac{7}{2} = \\frac{35}{10} = 3,5$\nc) $\\frac{11}{20} = \\frac{55}{100} = 0,55$\nd) $\\frac{1}{8} = \\frac{125}{1000} = 0,125$", "a) 0,6; b) 3,5; c) 0,55; d) 0,125", 4, 1.0),
            make_essay(3, "Viết các số sau dưới dạng số thập phân có 3 chữ số ở phần thập phân (mà giá trị không đổi):\na) 7,5\nb) 12,34\nc) 9\nd) 0,8", "a) $7,5 = 7,500$\nb) $12,34 = 12,340$\nc) $9 = 9,000$\nd) $0,8 = 0,800$", "a) 7,500; b) 12,340; c) 9,000; d) 0,800", 4, 1.0),
            make_essay(4, "Tìm chữ số $x$ trong số thập phân $45,6x9$, biết rằng giá trị của chữ số $x$ là $\\frac{7}{100}$.", "Trong số $45,6x9$, chữ số $x$ đứng ở vị trí hàng phần trăm.\nVì giá trị của chữ số $x$ là $\\frac{7}{100}$ nên $x = 7$.\nSố thập phân đó là $45,679$.", "x = 7 (số là 45,679)", 3, 1.0),
            make_essay(5, "Viết số thập phân thích hợp vào chỗ chấm:\na) Số gồm 5 đơn vị, 3 phần mười và 8 phần trăm: ...\nb) Số gồm 4 chục, 2 đơn vị và 6 phần nghìn: ...\nc) Số gồm 0 đơn vị, 9 phần trăm và 4 phần nghìn: ...", "a) 5,38\nb) 42,006\nc) 0,094", "a) 5,38; b) 42,006; c) 0,094", 3, 1.5),
            make_essay(6, "Tìm một số thập phân có hai chữ số ở phần thập phân, biết rằng nếu xóa đi chữ số 0 ở tận cùng bên phải phần thập phân của số đó thì phần thập phân chỉ còn 1 chữ số và số đó giảm đi 0,45 đơn vị (điều này chỉ xảy ra khi xóa đi chữ số khác 0). Nếu chỉ bỏ chữ số 0 ở tận cùng thì giá trị số đó như thế nào? Em hãy giải thích rõ quy tắc thêm hoặc bớt chữ số 0 ở tận cùng bên phải phần thập phân.", "Theo quy tắc: Khi viết thêm hoặc xóa bớt chữ số 0 ở tận cùng bên phải phần thập phân của một số thập phân thì giá trị của số đó KHÔNG ĐỔI.\nVí dụ: $2,50 = 2,5$; $4,800 = 4,8$.\nNếu xóa chữ số 0 ở tận cùng bên phải phần thập phân thì số mới thu được luôn bằng chính số ban đầu.", "Giá trị của số không thay đổi. Ví dụ: 2,50 = 2,5.", 4, 1.5)
        ]
    }

    # --- Bài 10 - Đề 3 ---
    exams["th5_b10_test3"] = {
        "id": "th5_b10_test3",
        "lessonId": "th5_b10",
        "lessonNum": 10,
        "testNum": 3,
        "title": "Bài 10: Khái niệm số thập phân - Đề số 3",
        "topic": "Khái niệm số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Chữ số 4 trong số thập phân 92,345 ở hàng nào?", ["Hàng phần mười", "Hàng phần trăm", "Hàng phần nghìn", "Hàng đơn vị"], 1, "Đứng thứ hai sau dấu phẩy là hàng phần trăm."),
            make_mc(2, "Số thập phân thích hợp điền vào chỗ chấm: $5\\text{ m } 8\\text{ dm} = \\dots \\text{ m}$ là:", ["5,8", "5,08", "5,008", "58"], 0, "8 dm = 8/10 m = 0,8 m nên bằng 5,8 m."),
            make_mc(3, "Phân số $\\frac{9}{1000}$ viết dưới dạng số thập phân là:", ["0,9", "0,09", "0,009", "0,0009"], 2, "9/1000 = 0,009."),
            make_mc(4, "Số thập phân 'Mười lăm phẩy bốn trăm linh sáu' viết là:", ["15,46", "15,406", "15,046", "150,406"], 1, "15,406."),
            make_mc(5, "Số nào dưới đây KHÔNG BẰNG các số còn lại?", ["0,7", "0,70", "0,07", "0,700"], 2, "0,07 là bảy phần trăm, khác 0,7 là bảy phần mười."),
            make_mc(6, "Trong số 78,92, phần nguyên là:", ["78", "92", "7", "8"], 0, "Phần nguyên đứng trước dấu phẩy là 78.")
        ],
        "part2": [
            make_essay(1, "Viết các số thập phân sau thành tổng theo các hàng:\na) 25,38\nb) 104,506", "a) $25,38 = 20 + 5 + 0,3 + 0,08 = 20 + 5 + \\frac{3}{10} + \\frac{8}{100}$\nb) $104,506 = 100 + 4 + 0,5 + 0,006 = 100 + 4 + \\frac{5}{10} + \\frac{6}{1000}$", "a) 20 + 5 + 0,3 + 0,08; b) 100 + 4 + 0,5 + 0,006", 4, 1.0),
            make_essay(2, "Viết các phân số sau thành số thập phân:\na) $\\frac{4}{25}$\nb) $\\frac{13}{4}$\nc) $\\frac{7}{8}$", "a) $\\frac{4}{25} = \\frac{16}{100} = 0,16$\nb) $\\frac{13}{4} = \\frac{325}{100} = 3,25$\nc) $\\frac{7}{8} = \\frac{875}{1000} = 0,875$", "a) 0,16; b) 3,25; c) 0,875", 4, 1.0),
            make_essay(3, "Viết các số đo sau dưới dạng số thập phân:\na) $4\\text{ m } 5\\text{ dm}$ (đơn vị mét);\nb) $2\\text{ m } 35\\text{ cm}$ (đơn vị mét);\nc) $6\\text{ kg } 250\\text{ g}$ (đơn vị ki-lô-gam).", "a) $4\\text{ m } 5\\text{ dm} = 4,5\\text{ m}$\nb) $2\\text{ m } 35\\text{ cm} = 2,35\\text{ m}$\nc) $6\\text{ kg } 250\\text{ g} = 6,25\\text{ kg}$ (hoặc 6,250 kg)", "a) 4,5 m; b) 2,35 m; c) 6,25 kg", 4, 1.0),
            make_essay(4, "Cho số thập phân $A = 38,452$. Nếu chuyển dấu phẩy của số $A$ sang bên phải một chữ số thì ta được số mới là bao nhiêu? Số mới thay đổi như thế nào so với số ban đầu?", "Khi chuyển dấu phẩy sang bên phải một chữ số, ta được số mới là $384,52$.\nSố mới gấp 10 lần số ban đầu ($384,52 = 38,452 \\times 10$).", "Số mới: 384,52; Gấp 10 lần số ban đầu", 3, 1.0),
            make_essay(5, "Tìm số thập phân có dạng $\\overline{a,bc}$, biết rằng tổng ba chữ số $a + b + c = 9$, $a$ gấp đôi $b$ và $c$ là số lẻ nhỏ nhất khác 0.", "Vì $c$ là số lẻ nhỏ nhất khác 0 nên $c = 1$.\nThay vào: $a + b + 1 = 9 \\Rightarrow a + b = 8$.\nTheo đề bài: $a = 2 \\times b$.\nTổng số phần bằng nhau của $a$ và $b$ là: $2 + 1 = 3$ phần.\nVì 8 không chia hết cho 3 nên xét lại: nếu $c$ là số lẻ có thể là 3 hay không?\nNếu $c = 2$ (chẵn). Nếu $c = 5$: $a + b = 4 \\Rightarrow b$ không nguyên.\nNếu $c = 0$ (chẵn). Nếu $a + b + c = 10$: $c = 1 \\Rightarrow a+b = 9 \\Rightarrow b = 3, a = 6 \\Rightarrow$ số là 6,31.\nVới $a+b+c = 10$, $a=6, b=3, c=1$ thỏa mãn: $6+3+1=10, 6=2\\times 3$, $c=1$.", "6,31", 5, 1.5),
            make_essay(6, "Bạn Lan viết một số thập phân có phần nguyên là số lẻ nhỏ nhất có hai chữ số, phần thập phân gồm ba chữ số giống nhau và tổng của ba chữ số đó bằng 15. Em hãy giúp Lan viết số thập phân đó và đọc số đó lên.", "Số lẻ nhỏ nhất có hai chữ số là 11, nên phần nguyên là 11.\nPhần thập phân gồm 3 chữ số giống nhau có tổng bằng 15, nên mỗi chữ số là: $15 : 3 = 5$.\nVậy số thập phân đó là: 11,555.\nĐọc số: 'Mười một phẩy năm trăm năm mươi lăm' (hoặc Mười một đơn vị, năm trăm năm mươi lăm phần nghìn).", "Số: 11,555; Đọc là: Mười một phẩy năm trăm năm mươi lăm", 4, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 11: SO SÁNH CÁC SỐ THẬP PHÂN
    # =========================================================================
    # --- Bài 11 - Đề 1 ---
    exams["th5_b11_test1"] = {
        "id": "th5_b11_test1",
        "lessonId": "th5_b11",
        "lessonNum": 11,
        "testNum": 1,
        "title": "Bài 11: So sánh các số thập phân - Đề số 1",
        "topic": "So sánh các số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Điền dấu thích hợp: $5,72 \\dots 5,8$:", ["<", ">", "=", "Không so sánh được"], 0, "So sánh hàng phần mười: 7 < 8 nên 5,72 < 5,8."),
            make_mc(2, "Trong các số sau, số nào lớn nhất?", ["12,45", "12,54", "12,05", "12,504"], 1, "Phần nguyên bằng 12. So sánh phần mười rồi phần trăm: 12,54 có hàng phần trăm là 4 > 0 trong 12,504."),
            make_mc(3, "Số thập phân nào bé hơn 0,45?", ["0,5", "0,452", "0,405", "0,450"], 2, "0,405 có hàng phần trăm là 0 < 5 trong 0,45."),
            make_mc(4, "Tìm số tự nhiên $x$ thỏa mãn: $6,8 < x < 7,9$. Giá trị của $x$ là:", ["6", "7", "8", "9"], 1, "Số tự nhiên duy nhất nằm giữa 6,8 và 7,9 là 7."),
            make_mc(5, "Dãy số nào dưới đây được xếp theo thứ tự từ bé đến lớn?", [
                "4,5; 4,25; 4,05; 4,12",
                "4,05; 4,12; 4,25; 4,5",
                "4,5; 4,25; 4,12; 4,05",
                "4,05; 4,25; 4,12; 4,5"
            ], 1, "4,05 < 4,12 < 4,25 < 4,50."),
            make_mc(6, "Điền chữ số thích hợp vào dấu * để: $8,5*2 > 8,582$:", ["7", "8", "9", "6"], 2, "Hàng phần trăm * phải lớn hơn 8 nên * = 9.")
        ],
        "part2": [
            make_essay(1, "Điền dấu ($>, <, =$) thích hợp vào chỗ chấm:\na) $84,2 \\dots 84,19$\nb) $6,84 \\dots 6,840$\nc) $0,75 \\dots 0,705$\nd) $15,08 \\dots 15,1$", "a) $84,2 = 84,20 > 84,19$\nb) $6,84 = 6,840$\nc) $0,75 = 0,750 > 0,705$\nd) $15,08 < 15,10$", "a) >; b) =; c) >; d) <", 4, 1.0),
            make_essay(2, "Sắp xếp các số sau theo thứ tự từ bé đến lớn:\n$5,78; 5,87; 5,708; 5,807; 5,087$.", "So sánh các số:\n$5,087 < 5,708 < 5,78 < 5,807 < 5,87$.\nVậy thứ tự từ bé đến lớn là: $5,087; 5,708; 5,78; 5,807; 5,87$.", "5,087; 5,708; 5,78; 5,807; 5,87", 4, 1.0),
            make_essay(3, "Sắp xếp các số sau theo thứ tự từ lớn đến bé:\n$9,6; 9,58; 9,605; 9,06; 9,599$.", "So sánh các số:\n$9,605 > 9,6 > 9,599 > 9,58 > 9,06$.\nThứ tự từ lớn đến bé là: $9,605; 9,6; 9,599; 9,58; 9,06$.", "9,605; 9,6; 9,599; 9,58; 9,06", 4, 1.0),
            make_essay(4, "Tìm các số tự nhiên $y$ thỏa mãn:\na) $3,45 < y < 6,12$\nb) $0,8 < y < 2,05$", "a) Các số tự nhiên lớn hơn 3,45 và nhỏ hơn 6,12 là: $y \\in \\{4; 5; 6\\}$.\nb) Các số tự nhiên lớn hơn 0,8 và nhỏ hơn 2,05 là: $y \\in \\{1; 2\\}$.", "a) y = 4; 5; 6; b) y = 1; 2", 4, 1.0),
            make_essay(5, "Tìm chữ số $x$ thích hợp, biết:\na) $4,x5 < 4,15$\nb) $9,8x5 > 9,875$", "a) Hàng phần mười $x < 1$, mà $x$ là chữ số nên $x = 0$. Kiểm tra: $4,05 < 4,15$ (đúng).\nb) Hàng phần trăm $x > 7$, nên $x \\in \\{8; 9\\}$.", "a) x = 0; b) x = 8 hoặc x = 9", 4, 1.5),
            make_essay(6, "Hãy viết 3 số thập phân thích hợp nằm giữa 0,2 và 0,3.", "Ta có $0,2 = 0,20$ và $0,3 = 0,30$.\nCác số thập phân nằm giữa 0,20 và 0,30 có thể chọn là: 0,21; 0,25; 0,28 (hoặc 0,22; 0,23...).", "Ví dụ: 0,21; 0,25; 0,28", 3, 1.5)
        ]
    }

    # --- Bài 11 - Đề 2 ---
    exams["th5_b11_test2"] = {
        "id": "th5_b11_test2",
        "lessonId": "th5_b11",
        "lessonNum": 11,
        "testNum": 2,
        "title": "Bài 11: So sánh các số thập phân - Đề số 2",
        "topic": "So sánh các số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Điền dấu thích hợp: $14,09 \\dots 14,1$:", ["<", ">", "=", "Không so sánh được"], 0, "14,09 < 14,10 vì hàng phần mười 0 < 1."),
            make_mc(2, "Số bé nhất trong các số: 3,12; 3,09; 3,2; 3,019 là:", ["3,12", "3,09", "3,2", "3,019"], 3, "3,019 có hàng phần trăm là 1 < 9 trong 3,090."),
            make_mc(3, "Có bao nhiêu số tự nhiên $n$ thỏa mãn: $8,9 < n < 12,1$?", ["3", "4", "5", "6"], 1, "Các số tự nhiên đó là 9; 10; 11; 12 (có 4 số)."),
            make_mc(4, "Tìm chữ số $a$ để $7,a6 < 7,16$. Giá trị của $a$ là:", ["0", "1", "2", "3"], 0, "a phải nhỏ hơn 1 nên a = 0."),
            make_mc(5, "Số thập phân nào dưới đây nằm giữa 1,5 và 1,6?", ["1,49", "1,55", "1,61", "1,65"], 1, "1,50 < 1,55 < 1,60."),
            make_mc(6, "Khẳng định nào sau đây là ĐÚNG?", [
                "$0,9 > 1,1$",
                "$4,500 < 4,5$",
                "$7,08 < 7,8$",
                "$12,34 > 12,4$"
            ], 2, "7,08 < 7,80 là đúng vì hàng phần mười 0 < 8.")
        ],
        "part2": [
            make_essay(1, "Điền dấu thích hợp ($>, <, =$):\na) $38,5 \\dots 38,499$\nb) $0,6 \\dots \\frac{3}{5}$\nc) $7,105 \\dots 7,15$", "a) Hàng phần mười 5 > 4 nên $38,5 > 38,499$.\nb) $\\frac{3}{5} = 0,6$ nên $0,6 = \\frac{3}{5}$.\nc) $7,105 < 7,150$ vì hàng phần trăm 0 < 5.", "a) >; b) =; c) <", 4, 1.0),
            make_essay(2, "Xếp các số sau theo thứ tự từ lớn đến bé:\n$8,25; 8,52; 8,052; 8,502; 8,205$.", "So sánh các số: $8,52 > 8,502 > 8,25 > 8,205 > 8,052$.\nThứ tự giảm dần: $8,52; 8,502; 8,25; 8,205; 8,052$.", "8,52; 8,502; 8,25; 8,205; 8,052", 4, 1.0),
            make_essay(3, "Tìm số tự nhiên $x$ lớn nhất thỏa mãn: $x < 9,75$.", "Các số tự nhiên nhỏ hơn 9,75 là: 0; 1; 2; 3; 4; 5; 6; 7; 8; 9.\nSố lớn nhất trong các số đó là 9.\nVậy $x = 9$.", "x = 9", 3, 1.0),
            make_essay(4, "Tìm 4 số thập phân $x$ sao cho: $0,7 < x < 0,8$.", "Ta viết $0,7 = 0,70$ và $0,8 = 0,80$.\n4 số thập phân thỏa mãn là: 0,71; 0,73; 0,75; 0,78.", "Ví dụ: 0,71; 0,73; 0,75; 0,78", 3, 1.0),
            make_essay(5, "Bốn bạn An, Bình, Cường, Dũng đo chiều cao được các kết quả lần lượt là: $1,42\\text{ m}$; $1,38\\text{ m}$; $1,45\\text{ m}$; $1,40\\text{ m}$. Hỏi bạn nào cao nhất? Bạn nào thấp nhất?", "So sánh chiều cao của bốn bạn:\n$1,38\\text{ m} < 1,40\\text{ m} < 1,42\\text{ m} < 1,45\\text{ m}$.\nVậy bạn Cường cao nhất ($1,45\\text{ m}$) và bạn Bình thấp nhất ($1,38\\text{ m}$).", "Cao nhất: Cường (1,45 m); Thấp nhất: Bình (1,38 m)", 4, 1.5),
            make_essay(6, "Cho 4 chữ số 1; 3; 5; 7. Hãy dùng cả 4 chữ số này để viết số thập phân lớn nhất và số thập phân nhỏ nhất có phần nguyên gồm một chữ số.", "Số thập phân có phần nguyên gồm 1 chữ số có dạng: $a,bcd$.\n- Để số lớn nhất: chọn chữ số hàng cao nhất lớn nhất: phần nguyên $a = 7$, các chữ số phần thập phân giảm dần: 5; 3; 1. Số đó là 7,531.\n- Để số nhỏ nhất: chọn phần nguyên nhỏ nhất: $a = 1$, các chữ số phần thập phân tăng dần: 3; 5; 7. Số đó là 1,357.", "Lớn nhất: 7,531; Nhỏ nhất: 1,357", 4, 1.5)
        ]
    }

    # --- Bài 11 - Đề 3 ---
    exams["th5_b11_test3"] = {
        "id": "th5_b11_test3",
        "lessonId": "th5_b11",
        "lessonNum": 11,
        "testNum": 3,
        "title": "Bài 11: So sánh các số thập phân - Đề số 3",
        "topic": "So sánh các số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Điền dấu thích hợp: $0,99 \\dots 1,01$:", ["<", ">", "=", "Không so sánh được"], 0, "So sánh phần nguyên: 0 < 1 nên 0,99 < 1,01."),
            make_mc(2, "Số lớn nhất trong các số: 7,89; 7,9; 7,809; 7,098 là:", ["7,89", "7,9", "7,809", "7,098"], 1, "7,900 có hàng phần mười là 9 lớn nhất."),
            make_mc(3, "Tìm số tự nhiên $m$ bé nhất sao cho: $m > 5,42$. Giá trị của $m$ là:", ["5", "6", "7", "8"], 1, "Số tự nhiên bé nhất lớn hơn 5,42 là 6."),
            make_mc(4, "Có bao nhiêu chữ số $x$ thỏa mãn: $3,56 < 3,x6 < 3,96$?", ["2 chữ số", "3 chữ số", "4 chữ số", "5 chữ số"], 1, "x có thể nhận các giá trị: 6; 7; 8 (có 3 chữ số)."),
            make_mc(5, "Số thập phân nào sau đây lớn hơn 2,4 và nhỏ hơn 2,5?", ["2,39", "2,45", "2,51", "2,55"], 1, "2,40 < 2,45 < 2,50."),
            make_mc(6, "Dãy số nào sau đây được xếp theo thứ tự giảm dần?", [
                "15,6; 15,45; 15,08; 15,01",
                "15,01; 15,08; 15,45; 15,6",
                "15,6; 15,08; 15,45; 15,01",
                "15,45; 15,6; 15,08; 15,01"
            ], 0, "15,60 > 15,45 > 15,08 > 15,01.")
        ],
        "part2": [
            make_essay(1, "Điền dấu ($>, <, =$):\na) $42,7 \\dots 42,69$\nb) $0,875 \\dots \\frac{7}{8}$\nc) $5,040 \\dots 5,04$", "a) $42,7 = 42,70 > 42,69$.\nb) $\\frac{7}{8} = 0,875$ nên $0,875 = \\frac{7}{8}$.\nc) Bỏ chữ số 0 tận cùng: $5,040 = 5,04$.", "a) >; b) =; c) =", 4, 1.0),
            make_essay(2, "Xếp các số sau theo thứ tự từ bé đến lớn:\n$0,45; 0,54; 0,405; 0,504; 0,054$.", "So sánh các số:\n$0,054 < 0,405 < 0,45 < 0,504 < 0,54$.\nThứ tự từ bé đến lớn: $0,054; 0,405; 0,45; 0,504; 0,54$.", "0,054; 0,405; 0,45; 0,504; 0,54", 4, 1.0),
            make_essay(3, "Tìm tất cả các số tự nhiên $n$ thỏa mãn: $12,8 < n \\le 16,3$.", "Các số tự nhiên lớn hơn 12,8 và bé hơn hoặc bằng 16,3 là: 13; 14; 15; 16.", "n = 13; 14; 15; 16", 3, 1.0),
            make_essay(4, "Tìm hai số tự nhiên liên tiếp $a$ và $b$ sao cho: $a < 7,85 < b$.", "Số tự nhiên liền trước 7,85 là 7 và số tự nhiên liền sau là 8.\nVậy $a = 7$ và $b = 8$.", "a = 7; b = 8", 3, 1.0),
            make_essay(5, "Năm học sinh chạy cự ly $60\\text{ m}$ có kết quả thời gian như sau: Nam ($10,2\\text{ giây}$), Hoàng ($9,8\\text{ giây}$), Minh ($10,05\\text{ giây}$), Long ($9,75\\text{ giây}$), Đức ($10,1\\text{ giây}$). Hỏi bạn nào chạy nhanh nhất (về đích đầu tiên)? Bạn nào về đích cuối cùng?", "Trong chạy cự ly, bạn chạy với thời gian ít nhất là nhanh nhất, nhiều thời gian nhất là chậm nhất.\nSo sánh thời gian: $9,75 < 9,8 < 10,05 < 10,1 < 10,2$.\nVậy Long chạy nhanh nhất ($9,75\\text{ giây}$) và Nam về đích cuối cùng ($10,2\\text{ giây}$).", "Nhanh nhất: Long (9,75 giây); Về cuối: Nam (10,2 giây)", 5, 1.5),
            make_essay(6, "Tìm số thập phân $x$ có hai chữ số ở phần thập phân sao cho: $1,2 < x < 1,3$ và chữ số hàng phần trăm gấp đôi chữ số hàng phần mười.", "Số thập phân có dạng: $1,ab$ với $1 \\le a, b \\le 9$ và $b = 2 \\times a$.\nVì $1,2 < 1,ab < 1,3$ nên hàng phần mười phải là 2 ($a = 2$).\nSuy ra chữ số hàng phần trăm là: $b = 2 \\times 2 = 4$.\nVậy số thập phân cần tìm là 1,24. (Thỏa mãn $1,20 < 1,24 < 1,30$).", "x = 1,24", 4, 1.5)
        ]
    }

    return exams
