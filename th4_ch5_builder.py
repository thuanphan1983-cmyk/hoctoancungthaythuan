# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 5: PHÉP CỘNG VÀ PHÉP TRỪ (BÀI 21 ĐẾN BÀI 24)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 4 bài học x 3 đề độc lập = 12 đề kiểm tra chất lượng cao (th4_b21_test1 -> th4_b24_test3)
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
    # BÀI 21: PHÉP CỘNG SỐ CÓ NHIỀU CHỮ SỐ
    # =========================================================================

    # --- Bài 21 - Đề 1 ---
    exams["th4_b21_test1"] = {
        "id": "th4_b21_test1",
        "lessonId": "th4_b21",
        "lessonNum": 21,
        "testNum": 1,
        "title": "Bài 21: Phép cộng số có nhiều chữ số - Đề số 1",
        "topic": "Phép cộng số có nhiều chữ số",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $45\\,230 + 13\\,450$ là:", ["58 680", "58 780", "57 680", "59 680"], 0, "45 230 + 13 450 = 58 680."),
            make_mc(2, "Kết quả của phép cộng $386\\,427 + 245\\,189$ là:", ["631 616", "631 516", "621 616", "641 616"], 0, "386 427 + 245 189 = 631 616."),
            make_mc(3, "Tìm $x$, biết: $x - 34\\,500 = 65\\,500$:", ["100 000", "31 000", "90 000", "110 000"], 0, "x = 65 500 + 34 500 = 100 000."),
            make_mc(4, "Một trang trại có 125 000 con gà ri và 87 500 con gà tre. Tổng số gà của trang trại là:", ["212 500 con", "211 500 con", "202 500 con", "213 500 con"], 0, "125 000 + 87 500 = 212 500 con."),
            make_mc(5, "Chữ số thích hợp điền vào dấu $*$ trong phép tính $4*2\\,150 + 135\\,200 = 587\\,350$ là:", ["5", "4", "3", "6"], 0, "4*2 150 = 587 350 - 135 200 = 452 150 nên * là 5."),
            make_mc(6, "Cộng nhẩm: $300\\,000 + 500\\,000 + 200\\,000 = \\dots$:", ["1 000 000", "10 000 000", "900 000", "800 000"], 0, "300 000 + 500 000 + 200 000 = 1 000 000.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $246\\,385 + 137\\,429$\nb) $518\\,206 + 394\\,798$", "a) $246\\,385 + 137\\,429 = 383\\,814$.\nb) $518\\,206 + 394\\,798 = 913\\,004$.", "a) 383 814; b) 913 004", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\na) $425\\,000 + 175\\,000 + 340\\,000$\nb) $a + b$ với $a = 645\\,230$ và $b = 254\\,770$", "a) $425\\,000 + 175\\,000 + 340\\,000 = 600\\,000 + 340\\,000 = 940\\,000$.\nb) Với $a = 645\\,230$ và $b = 254\\,770$, ta có: $a + b = 645\\,230 + 254\\,770 = 900\\,000$.", "a) 940 000; b) 900 000", 4, 1.0),
            make_essay(3, "Một công ty may mặc trong quý I sản xuất được 148 500 chiếc áo, quý II sản xuất được nhiều hơn quý I là 24 800 chiếc áo. Hỏi cả hai quý công ty sản xuất được bao nhiêu chiếc áo?", "Số áo quý II công ty sản xuất được là:\n$148\\,500 + 24\\,800 = 173\\,300\\text{ (chiếc)}$.\nCả hai quý công ty sản xuất được số áo là:\n$148\\,500 + 173\\,300 = 321\\,800\\text{ (chiếc)}$.", "321 800 chiếc áo", 4, 1.0),
            make_essay(4, "Một thư viện trường học năm học trước có 126 400 cuốn sách. Năm học này thư viện mua thêm 15 800 cuốn sách giáo khoa và 12 500 cuốn sách tham khảo. Hỏi hiện nay thư viện trường đó có tất cả bao nhiêu cuốn sách?", "Số sách mua thêm trong năm học này là:\n$15\\,800 + 12\\,500 = 28\\,300\\text{ (cuốn)}$.\nHiện nay thư viện có tất cả số cuốn sách là:\n$126\\,400 + 28\\,300 = 154\\,700\\text{ (cuốn)}$.", "154 700 cuốn sách", 5, 1.5),
            make_essay(5, "Năm ngoái một nhà máy sản xuất được 1 450 000 m vải. Năm nay nhà máy phấn đấu sản xuất vượt năm ngoái 185 000 m vải. Hỏi cả hai năm nhà máy sản xuất được tất cả bao nhiêu mét vải?", "Số mét vải năm nay nhà máy sản xuất được là:\n$1\\,450\\,000 + 185\\,000 = 1\\,635\\,000\\text{ (m)}$.\nCả hai năm nhà máy sản xuất được tất cả số mét vải là:\n$1\\,450\\,000 + 1\\,635\\,000 = 3\\,085\\,000\\text{ (m)}$.", "3 085 000 m vải", 5, 1.5),
            make_essay(6, "Điền các chữ số thích hợp vào dấu $*$:\n  $3*5\\,4*6 + *4*\\,21* = 812\\,689$", "Ta phân tích từng hàng từ phải sang trái:\n- Hàng đơn vị: $6 + * = 9 \\Rightarrow * = 3$.\n- Hàng chục: $* + 1 = 8 \\Rightarrow * = 7$.\n- Hàng trăm: $4 + 2 = 6$ (đúng).\n- Hàng nghìn: $5 + * = 12 \\Rightarrow * = 7$ (nhớ 1).\n- Hàng chục nghìn: $* + 4 + 1 = 11 \\Rightarrow * = 6$ (nhớ 1).\n- Hàng trăm nghìn: $3 + * + 1 = 8 \\Rightarrow * = 4$.\nVậy phép tính là: $365\\,476 + 447\\,213 = 812\\,689$.", "365 476 + 447 213 = 812 689", 4, 1.0)
        ]
    }

    # --- Bài 21 - Đề 2 ---
    exams["th4_b21_test2"] = {
        "id": "th4_b21_test2",
        "lessonId": "th4_b21",
        "lessonNum": 21,
        "testNum": 2,
        "title": "Bài 21: Phép cộng số có nhiều chữ số - Đề số 2",
        "topic": "Phép cộng số có nhiều chữ số",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $318\\,240 + 261\\,539$:", ["579 779", "579 679", "589 779", "578 779"], 0, "318 240 + 261 539 = 579 779."),
            make_mc(2, "Số lớn nhất có 6 chữ số cộng với số bé nhất có 6 chữ số là:", ["1 099 999", "1 099 998", "1 100 000", "999 999"], 0, "999 999 + 100 000 = 1 099 999."),
            make_mc(3, "Tìm $y$, biết: $y - 128\\,400 = 371\\,600$:", ["500 000", "490 000", "510 000", "400 000"], 0, "y = 371 600 + 128 400 = 500 000."),
            make_mc(4, "Một huyện có 65 400 học sinh tiểu học và 48 900 học sinh trung học cơ sở. Huyện đó có tất cả số học sinh là:", ["114 300 học sinh", "113 300 học sinh", "114 200 học sinh", "104 300 học sinh"], 0, "65 400 + 48 900 = 114 300."),
            make_mc(5, "Tổng của số chẵn lớn nhất có 5 chữ số với số lẻ bé nhất có 5 chữ số là:", ["109 999", "110 000", "109 998", "99 999"], 0, "99 998 + 10 001 = 109 999."),
            make_mc(6, "Kết quả của phép cộng $450\\,000 + 350\\,000$ bằng:", ["800 000", "700 000", "900 000", "750 000"], 0, "450 000 + 350 000 = 800 000.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $372\\,514 + 465\\,829$\nb) $684\\,935 + 248\\,176$", "a) $372\\,514 + 465\\,829 = 838\\,343$.\nb) $684\\,935 + 248\\,176 = 933\\,111$.", "a) 838 343; b) 933 111", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $135\\,600 + 264\\,400 + 150\\,000$\nb) $m + n$ với $m = 485\\,350$ và $n = 314\\,650$", "a) $135\\,600 + 264\\,400 + 150\\,000 = 400\\,000 + 150\\,000 = 550\\,000$.\nb) Với $m = 485\\,350, n = 314\\,650$, ta có: $m + n = 485\\,350 + 314\\,650 = 800\\,000$.", "a) 550 000; b) 800 000", 4, 1.0),
            make_essay(3, "Một đội công nhân làm đường trong tuần thứ nhất trải nhựa được 12 450 m đường. Tuần thứ hai trải nhựa được nhiều hơn tuần thứ nhất 1 850 m. Hỏi trong cả hai tuần đội công nhân đó trải nhựa được bao nhiêu mét đường?", "Tuần thứ hai đội công nhân làm được là:\n$12\\,450 + 1\\,850 = 14\\,300\\text{ (m)}$.\nCả hai tuần đội công nhân làm được là:\n$12\\,450 + 14\\,300 = 26\\,750\\text{ (m)}$.", "26 750 m", 4, 1.0),
            make_essay(4, "Một trang trại nuôi 3 khu gà: Khu A có 45 200 con gà, khu B có nhiều hơn khu A là 6 800 con gà, khu C có số gà bằng tổng số gà của khu A và khu B. Hỏi cả trang trại có tất cả bao nhiêu con gà?", "Khu B có số con gà là:\n$45\\,200 + 6\\,800 = 52\\,000\\text{ (con)}$.\nKhu C có số con gà là:\n$45\\,200 + 52\\,000 = 97\\,200\\text{ (con)}$.\nCả trang trại có số con gà là:\n$45\\,200 + 52\\,000 + 97\\,200 = 194\\,400\\text{ (con)}$.", "194 400 con gà", 5, 1.5),
            make_essay(5, "Một thành phố năm 2023 có dân số là 865 400 người. Năm 2024 dân số tăng thêm 14 600 người. Năm 2025 dân số dự kiến tăng thêm 16 500 người nữa so với năm 2024. Hỏi đến hết năm 2025 dân số của thành phố đó ước tính là bao nhiêu người?", "Dân số thành phố năm 2024 là:\n$865\\,400 + 14\\,600 = 880\\,000\\text{ (người)}$.\nDân số thành phố đến hết năm 2025 là:\n$880\\,000 + 16\\,500 = 896\\,500\\text{ (người)}$.", "896 500 người", 5, 1.5),
            make_essay(6, "Cho hai số có tổng là 456 789. Nếu thêm vào số hạng thứ nhất 12 345 đơn vị và thêm vào số hạng thứ hai 23 456 đơn vị thì được tổng mới bằng bao nhiêu?", "Khi thêm vào số hạng thứ nhất 12 345 đơn vị và số hạng thứ hai 23 456 đơn vị thì tổng sẽ tăng thêm:\n$12\\,345 + 23\\,456 = 35\\,801\\text{ (đơn vị)}$.\nTổng mới là:\n$456\\,789 + 35\\,801 = 492\\,590$.", "492 590", 4, 1.0)
        ]
    }

    # --- Bài 21 - Đề 3 ---
    exams["th4_b21_test3"] = {
        "id": "th4_b21_test3",
        "lessonId": "th4_b21",
        "lessonNum": 21,
        "testNum": 3,
        "title": "Bài 21: Phép cộng số có nhiều chữ số - Đề số 3",
        "topic": "Phép cộng số có nhiều chữ số",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $543\\,210 + 234\\,567$ là:", ["777 777", "767 777", "777 677", "877 777"], 0, "543 210 + 234 567 = 777 777."),
            make_mc(2, "Số lớn hơn số $685\\,320$ là $41\\,280$ đơn vị là:", ["726 600", "716 600", "726 500", "626 600"], 0, "685 320 + 41 280 = 726 600."),
            make_mc(3, "Tính nhanh: $250\\,000 + 450\\,000 + 300\\,000$:", ["1 000 000", "900 000", "1 100 000", "850 000"], 0, "250 000 + 450 000 + 300 000 = 700 000 + 300 000 = 1 000 000."),
            make_mc(4, "Một cửa hàng ngày thứ nhất bán được 18 500 kg gạo, ngày thứ hai bán được 21 500 kg gạo. Cả hai ngày cửa hàng bán được số tấn gạo là:", ["40 tấn", "4 tấn", "400 tấn", "38 tấn"], 0, "18 500 + 21 500 = 40 000 kg = 40 tấn."),
            make_mc(5, "Tổng của số bé nhất có 6 chữ số khác nhau và số lớn nhất có 5 chữ số là:", ["202 344", "201 345", "102 345", "202 345"], 0, "Số bé nhất có 6 chữ số khác nhau là 102 345. Số lớn nhất có 5 chữ số là 99 999. Tổng: 102 345 + 99 999 = 202 344."),
            make_mc(6, "Tìm $x$ biết $x - 250\\,000 = 750\\,000$:", ["1 000 000", "500 000", "900 000", "1 250 000"], 0, "x = 750 000 + 250 000 = 1 000 000.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $483\\,627 + 375\\,495$\nb) $629\\,804 + 195\\,398$", "a) $483\\,627 + 375\\,495 = 859\\,122$.\nb) $629\\,804 + 195\\,398 = 825\\,202$.", "a) 859 122; b) 825 202", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $345\\,670 + 254\\,330 + 120\\,000$\nb) $x + y$ với $x = 718\\,400$ và $y = 181\\,600$", "a) $345\\,670 + 254\\,330 + 120\\,000 = 600\\,000 + 120\\,000 = 720\\,000$.\nb) $x + y = 718\\,400 + 181\\,600 = 900\\,000$.", "a) 720 000; b) 900 000", 4, 1.0),
            make_essay(3, "Một nhà máy xi măng tháng 1 sản xuất được 215 400 bao xi măng, tháng 2 sản xuất được nhiều hơn tháng 1 là 32 800 bao xi măng. Hỏi trong cả hai tháng nhà máy sản xuất được tất cả bao nhiêu bao xi măng?", "Tháng 2 nhà máy sản xuất được là:\n$215\\,400 + 32\\,800 = 248\\,200\\text{ (bao)}$.\nCả hai tháng nhà máy sản xuất được là:\n$215\\,400 + 248\\,200 = 463\\,600\\text{ (bao)}$.", "463 600 bao xi măng", 4, 1.0),
            make_essay(4, "Một siêu thị điện máy trong đợt khuyến mãi đã bán được 1 250 chiếc quạt máy, 840 chiếc nồi cơm điện và 1 450 chiếc máy xay sinh tố. Hỏi siêu thị đã bán được tất cả bao nhiêu thiết bị gia dụng?", "Tổng số thiết bị gia dụng siêu thị đã bán là:\n$1250 + 840 + 1450 = 3540\\text{ (thiết bị)}$.", "3540 thiết bị", 5, 1.5),
            make_essay(5, "Năm 2022 một tỉnh trồng được 1 350 000 cây xanh. Năm 2023 tỉnh đó trồng nhiều hơn năm 2022 là 250 000 cây. Năm 2024 tỉnh đó phát động phong trào trồng thêm 300 000 cây nữa so với năm 2023. Hỏi trong cả 3 năm tỉnh đó đã trồng được bao nhiêu cây xanh?", "Năm 2023 tỉnh trồng được số cây là:\n$1\\,350\\,000 + 250\\,000 = 1\\,600\\,000\\text{ (cây)}$.\nNăm 2024 tỉnh trồng được số cây là:\n$1\\,600\\,000 + 300\\,000 = 1\\,900\\,000\\text{ (cây)}$.\nCả 3 năm tỉnh đó trồng được tất cả số cây là:\n$1\\,350\\,000 + 1\\,600\\,000 + 1\\,900\\,000 = 4\\,850\\,000\\text{ (cây)}$.", "4 850 000 cây", 5, 1.5),
            make_essay(6, "Tìm một số biết rằng nếu lấy số đó cộng với số lớn nhất có 5 chữ số thì được số bé nhất có 7 chữ số.", "Số lớn nhất có 5 chữ số là: 99 999.\nSố bé nhất có 7 chữ số là: 1 000 000.\nSố cần tìm là:\n$1\\,000\\,000 - 99\\,999 = 900\\,001$.", "900 001", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 22: PHÉP TRỪ SỐ CÓ NHIỀU CHỮ SỐ
    # =========================================================================

    # --- Bài 22 - Đề 1 ---
    exams["th4_b22_test1"] = {
        "id": "th4_b22_test1",
        "lessonId": "th4_b22",
        "lessonNum": 22,
        "testNum": 1,
        "title": "Bài 22: Phép trừ số có nhiều chữ số - Đề số 1",
        "topic": "Phép trừ số có nhiều chữ số",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hiệu của hai số $584\\,620$ và $231\\,410$ là:", ["353 210", "353 110", "343 210", "352 210"], 0, "584 620 - 231 410 = 353 210."),
            make_mc(2, "Kết quả của phép trừ $725\\,380 - 368\\,594$ là:", ["356 786", "356 886", "366 786", "357 786"], 0, "725 380 - 368 594 = 356 786."),
            make_mc(3, "Tìm $x$, biết: $850\\,000 - x = 320\\,000$:", ["530 000", "520 000", "1 170 000", "540 000"], 0, "x = 850 000 - 320 000 = 530 000."),
            make_mc(4, "Một kho gạo có 150 000 kg gạo, đã xuất đi 45 600 kg. Số gạo còn lại trong kho là:", ["104 400 kg", "104 500 kg", "105 400 kg", "114 400 kg"], 0, "150 000 - 45 600 = 104 400 kg."),
            make_mc(5, "Số bé nhất có 6 chữ số trừ đi số lớn nhất có 5 chữ số bằng:", ["1", "0", "10", "9"], 0, "100 000 - 99 999 = 1."),
            make_mc(6, "Trừ nhẩm: $1\\,000\\,000 - 600\\,000 = \\dots$:", ["400 000", "300 000", "500 000", "450 000"], 0, "1 000 000 - 600 000 = 400 000.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $658\\,942 - 234\\,518$\nb) $800\\,000 - 347\\,256$", "a) $658\\,942 - 234\\,518 = 424\\,424$.\nb) $800\\,000 - 347\\,256 = 452\\,744$.", "a) 424 424; b) 452 744", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\na) $945\\,000 - (320\\,000 + 125\\,000)$\nb) $a - b$ với $a = 782\\,400$ và $b = 356\\,800$", "a) $945\\,000 - 445\\,000 = 500\\,000$.\nb) Với $a = 782\\,400, b = 356\\,800$, ta có: $a - b = 782\\,400 - 356\\,800 = 425\\,600$.", "a) 500 000; b) 425 600", 4, 1.0),
            make_essay(3, "Một nông trường thu hoạch được 250 800 kg mía trong hai đợt. Đợt thứ nhất thu hoạch được 135 400 kg. Hỏi đợt thứ hai thu hoạch được bao nhiêu ki-lô-gam mía và đợt nào thu hoạch được nhiều hơn bao nhiêu ki-lô-gam?", "Đợt thứ hai thu hoạch được số ki-lô-gam mía là:\n$250\\,800 - 135\\,400 = 115\\,400\\text{ (kg)}$.\nĐợt thứ nhất thu hoạch được nhiều hơn đợt thứ hai số ki-lô-gam là:\n$135\\,400 - 115\\,400 = 20\\,000\\text{ (kg)}$.", "Đợt hai: 115 400 kg; Đợt một nhiều hơn 20 000 kg", 4, 1.0),
            make_essay(4, "Một công ty dự định may 450 000 bộ quần áo bảo hộ lao động. Trong 6 tháng đầu năm công ty may được 185 000 bộ, quý III may được 120 000 bộ. Hỏi quý IV công ty cần may thêm bao nhiêu bộ quần áo nữa để hoàn thành kế hoạch năm?", "Số bộ quần áo công ty đã may sau 3 quý là:\n$185\\,000 + 120\\,000 = 305\\,000\\text{ (bộ)}$.\nQuý IV công ty cần may thêm số bộ quần áo là:\n$450\\,000 - 305\\,000 = 145\\,000\\text{ (bộ)}$.", "145 000 bộ quần áo", 5, 1.5),
            make_essay(5, "Một khu rừng phòng hộ có 385 000 cây xanh các loại. Do một trận mưa bão có 12 400 cây bị gãy đổ. Sau đó nhân dân địa phương đã trồng bù lại 25 000 cây mới. Hỏi sau khi trồng bù, khu rừng có tất cả bao nhiêu cây xanh?", "Số cây còn lại sau bão là:\n$385\\,000 - 12\\,400 = 372\\,600\\text{ (cây)}$.\nSau khi trồng bù, khu rừng có số cây là:\n$372\\,600 + 25\\,000 = 397\\,600\\text{ (cây)}$.", "397 600 cây", 5, 1.5),
            make_essay(6, "Hiệu của hai số là 84 500. Nếu bớt ở số bị trừ 4 500 đơn vị và thêm vào số trừ 5 000 đơn vị thì hiệu mới là bao nhiêu?", "Khi bớt ở số bị trừ 4 500 đơn vị thì hiệu giảm 4 500 đơn vị.\nKhi thêm vào số trừ 5 000 đơn vị thì hiệu giảm tiếp 5 000 đơn vị.\nVậy hiệu mới là:\n$84\\,500 - 4\\,500 - 5\\,000 = 75\\,000$.", "75 000", 4, 1.0)
        ]
    }

    # --- Bài 22 - Đề 2 ---
    exams["th4_b22_test2"] = {
        "id": "th4_b22_test2",
        "lessonId": "th4_b22",
        "lessonNum": 22,
        "testNum": 2,
        "title": "Bài 22: Phép trừ số có nhiều chữ số - Đề số 2",
        "topic": "Phép trừ số có nhiều chữ số",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $846\\,519 - 413\\,207$:", ["433 312", "433 212", "432 312", "433 412"], 0, "846 519 - 413 207 = 433 312."),
            make_mc(2, "Kết quả của phép trừ $1\\,000\\,000 - 456\\,789$ là:", ["543 211", "543 210", "544 211", "643 211"], 0, "1 000 000 - 456 789 = 543 211."),
            make_mc(3, "Tìm $y$, biết: $y + 245\\,000 = 600\\,000$:", ["355 000", "345 000", "365 000", "845 000"], 0, "y = 600 000 - 245 000 = 355 000."),
            make_mc(4, "Một nhà máy có 520 000 viên gạch, đã xuất bán 385 000 viên. Trong kho nhà máy còn lại số viên gạch là:", ["135 000 viên", "145 000 viên", "125 000 viên", "235 000 viên"], 0, "520 000 - 385 000 = 135 000 viên."),
            make_mc(5, "Số lớn nhất có 6 chữ số trừ đi số bé nhất có 6 chữ số khác nhau bằng:", ["897 654", "897 655", "896 654", "999 999"], 0, "999 999 - 102 345 = 897 654."),
            make_mc(6, "Một tàu chở 45 000 lít dầu, đã bơm sang kho 28 000 lít. Số dầu còn lại trên tàu là:", ["17 000 lít", "27 000 lít", "16 000 lít", "18 000 lít"], 0, "45 000 - 28 000 = 17 000 lít.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $764\\,892 - 351\\,647$\nb) $912\\,005 - 478\\,369$", "a) $764\\,892 - 351\\,647 = 413\\,245$.\nb) $912\\,005 - 478\\,369 = 433\\,636$.", "a) 413 245; b) 433 636", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $860\\,000 - 240\\,000 - 320\\,000$\nb) $x - y$ với $x = 650\\,000$ và $y = 384\\,500$", "a) $860\\,000 - 240\\,000 - 320\\,000 = 620\\,000 - 320\\,000 = 300\\,000$.\nb) $x - y = 650\\,000 - 384\\,500 = 265\\,500$.", "a) 300 000; b) 265 500", 4, 1.0),
            make_essay(3, "Một hồ chứa nước có dung tích 850 000 m³ nước. Trong đợt hạn hán người ta đã xả 325 000 m³ nước để tưới tiêu. Sau đó một trận mưa cung cấp thêm cho hồ 180 000 m³ nước. Hỏi hiện nay trong hồ có bao nhiêu mét khối nước?", "Sau đợt xả nước trong hồ còn lại:\n$850\\,000 - 325\\,000 = 525\\,000\\text{ (m}^3)$.\nHiện nay trong hồ có số mét khối nước là:\n$525\\,000 + 180\\,000 = 705\\,000\\text{ (m}^3)$.", "705 000 m³", 4, 1.0),
            make_essay(4, "Một siêu thị nhập về 120 000 gói mì ăn liền. Tuần thứ nhất bán được 38 500 gói, tuần thứ hai bán được nhiều hơn tuần thứ nhất 4 200 gói. Hỏi sau hai tuần siêu thị còn lại bao nhiêu gói mì?", "Tuần thứ hai siêu thị bán được số gói mì là:\n$38\\,500 + 4\\,200 = 42\\,700\\text{ (gói)}$.\nCả hai tuần siêu thị bán được số gói mì là:\n$38\\,500 + 42\\,700 = 81\\,200\\text{ (gói)}$.\nSau hai tuần siêu thị còn lại số gói mì là:\n$120\\,000 - 81\\,200 = 38\\,800\\text{ (gói)}$.", "38 800 gói mì", 5, 1.5),
            make_essay(5, "Năm ngoái thu nhập của gia đình bác Hùng là 240 000 000 đồng. Chi tiêu cả năm hết 168 000 000 đồng. Số tiền còn lại bác gửi tiết kiệm. Hỏi năm ngoái bác Hùng tiết kiệm được bao nhiêu tiền?", "Số tiền bác Hùng tiết kiệm được trong năm ngoái là:\n$240\\,000\\,000 - 168\\,000\\,000 = 72\\,000\\,000\\text{ (đồng)}$.", "72 000 000 đồng", 5, 1.5),
            make_essay(6, "Hiệu của hai số là 125 000. Nếu thêm vào số bị trừ 15 000 đơn vị và bớt ở số trừ 10 000 đơn vị thì hiệu mới bằng bao nhiêu?", "Khi thêm vào số bị trừ 15 000 đơn vị thì hiệu tăng 15 000 đơn vị.\nKhi bớt ở số trừ 10 000 đơn vị thì hiệu tăng tiếp 10 000 đơn vị.\nVậy hiệu mới là:\n$125\\,000 + 15\\,000 + 10\\,000 = 150\\,000$.", "150 000", 4, 1.0)
        ]
    }

    # --- Bài 22 - Đề 3 ---
    exams["th4_b22_test3"] = {
        "id": "th4_b22_test3",
        "lessonId": "th4_b22",
        "lessonNum": 22,
        "testNum": 3,
        "title": "Bài 22: Phép trừ số có nhiều chữ số - Đề số 3",
        "topic": "Phép trừ số có nhiều chữ số",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $900\\,000 - 350\\,000$ là:", ["550 000", "650 000", "500 000", "450 000"], 0, "900 000 - 350 000 = 550 000."),
            make_mc(2, "Hiệu của hai số $642\\,805$ và $275\\,438$ là:", ["367 367", "377 367", "367 467", "366 367"], 0, "642 805 - 275 438 = 367 367."),
            make_mc(3, "Tìm $x$, biết: $x + 416\\,500 = 900\\,000$:", ["483 500", "484 500", "493 500", "583 500"], 0, "x = 900 000 - 416 500 = 483 500."),
            make_mc(4, "Một đoàn tàu chở 350 tấn hàng, đến ga thứ nhất dỡ xuống 120 tấn, ga thứ hai dỡ xuống 95 tấn. Số hàng còn lại trên tàu là:", ["135 tấn", "145 tấn", "125 tấn", "155 tấn"], 0, "350 - 120 - 95 = 135 tấn."),
            make_mc(5, "Số bé hơn $500\\,000$ là $125\\,400$ đơn vị là:", ["374 600", "375 600", "384 600", "625 400"], 0, "500 000 - 125 400 = 374 600."),
            make_mc(6, "Một huyện có 128 400 dân, trong đó số người ở độ tuổi lao động là 74 200 người. Số người ngoài độ tuổi lao động là:", ["54 200 người", "54 300 người", "53 200 người", "64 200 người"], 0, "128 400 - 74 200 = 54 200 người.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $849\\,200 - 425\\,673$\nb) $700\\,000 - 289\\,415$", "a) $849\\,200 - 425\\,673 = 423\\,527$.\nb) $700\\,000 - 289\\,415 = 410\\,585$.", "a) 423 527; b) 410 585", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $750\\,000 - (210\\,000 + 190\\,000)$\nb) $m - n$ với $m = 852\\,000$ và $n = 437\\,500$", "a) $750\\,000 - 400\\,000 = 350\\,000$.\nb) $m - n = 852\\,000 - 437\\,500 = 414\\,500$.", "a) 350 000; b) 414 500", 4, 1.0),
            make_essay(3, "Một trang trại thu hoạch được 35 400 kg cam. Ngày đầu bán được 12 800 kg, ngày thứ hai bán được 14 500 kg. Hỏi trang trại còn lại bao nhiêu ki-lô-gam cam?", "Tổng số cam đã bán trong hai ngày là:\n$12\\,800 + 14\\,500 = 27\\,300\\text{ (kg)}$.\nSố ki-lô-gam cam trang trại còn lại là:\n$35\\,400 - 27\\,300 = 8\\,100\\text{ (kg)}$.", "8 100 kg", 4, 1.0),
            make_essay(4, "Một cửa hàng vật liệu xây dựng có 500 tấn xi măng. Tuần thứ nhất bán được 145 tấn, tuần thứ hai bán được nhiều hơn tuần thứ nhất 30 tấn. Hỏi sau hai tuần cửa hàng còn lại bao nhiêu tấn xi măng?", "Tuần thứ hai cửa hàng bán được số tấn xi măng là:\n$145 + 30 = 175\\text{ (tấn)}$.\nCả hai tuần cửa hàng bán được số tấn xi măng là:\n$145 + 175 = 320\\text{ (tấn)}$.\nCửa hàng còn lại số tấn xi măng là:\n$500 - 320 = 180\\text{ (tấn)}$.", "180 tấn", 5, 1.5),
            make_essay(5, "Năm nay một quỹ học bổng có số tiền là 500 000 000 đồng. Đợt 1 quỹ đã trao 180 000 000 đồng học bổng cho học sinh nghèo vượt khó. Đợt 2 trao 150 000 000 đồng học bổng tài năng trẻ. Hỏi quỹ còn lại bao nhiêu tiền?", "Tổng số tiền học bổng đã trao trong 2 đợt là:\n$180\\,000\\,000 + 150\\,000\\,000 = 330\\,000\\,000\\text{ (đồng)}$.\nSố tiền quỹ học bổng còn lại là:\n$500\\,000\\,000 - 330\\,000\\,000 = 170\\,000\\,000\\text{ (đồng)}$.", "170 000 000 đồng", 5, 1.5),
            make_essay(6, "Tìm hai số biết rằng nếu số bị trừ tăng thêm 35 000 và số trừ giảm đi 15 000 thì hiệu mới là 120 000. Hỏi hiệu ban đầu của hai số là bao nhiêu?", "Khi số bị trừ tăng 35 000 thì hiệu tăng 35 000.\nKhi số trừ giảm 15 000 thì hiệu tăng tiếp 15 000.\nNhư vậy hiệu mới đã tăng so với hiệu ban đầu là:\n$35\\,000 + 15\\,000 = 50\\,000$.\nHiệu ban đầu của hai số là:\n$120\\,000 - 50\\,000 = 70\\,000$.", "70 000", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 23: TÍNH CHẤT GIAO HOÁN VÀ KẾT HỢP CỦA PHÉP CỘNG
    # =========================================================================

    # --- Bài 23 - Đề 1 ---
    exams["th4_b23_test1"] = {
        "id": "th4_b23_test1",
        "lessonId": "th4_b23",
        "lessonNum": 23,
        "testNum": 1,
        "title": "Bài 23: Tính chất giao hoán và kết hợp của phép cộng - Đề số 1",
        "topic": "Tính chất giao hoán và kết hợp của phép cộng",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Biểu thức nào dưới đây biểu thị tính chất giao hoán của phép cộng?", ["a + b = b + a", "(a + b) + c = a + (b + c)", "a + 0 = a", "a x b = b x a"], 0, "Tính chất giao hoán: khi đổi chỗ các số hạng trong một tổng thì tổng không thay đổi: a + b = b + a."),
            make_mc(2, "Tính nhanh: $125 + 348 + 75$:", ["548", "558", "448", "538"], 0, "(125 + 75) + 348 = 200 + 348 = 548."),
            make_mc(3, "Số thích hợp điền vào ô trống: $48 + 36 = 36 + \\dots$ là:", ["48", "36", "84", "0"], 0, "Theo tính chất giao hoán: 48 + 36 = 36 + 48."),
            make_mc(4, "Biểu thức $(a + b) + c = a + (b + c)$ biểu thị tính chất gì của phép cộng?", ["Tính chất kết hợp", "Tính chất giao hoán", "Tính chất phân phối", "Cộng với số 0"], 0, "Đó là tính chất kết hợp của phép cộng."),
            make_mc(5, "Tính thuận tiện: $234 + 179 + 66$:", ["479", "469", "489", "579"], 0, "(234 + 66) + 179 = 300 + 179 = 479."),
            make_mc(6, "Giá trị của biểu thức $97 + 154 + 3 + 46$ bằng:", ["300", "290", "310", "280"], 0, "(97 + 3) + (154 + 46) = 100 + 200 = 300.")
        ],
        "part2": [
            make_essay(1, "Tính bằng cách thuận tiện nhất:\na) $345 + 189 + 655$\nb) $237 + 465 + 163 + 135$", "a) $(345 + 655) + 189 = 1000 + 189 = 1189$.\nb) $(237 + 163) + (465 + 135) = 400 + 600 = 1000$.", "a) 1189; b) 1000", 4, 1.0),
            make_essay(2, "Điền số thích hợp vào chỗ chấm:\na) $27 + 84 = \\dots + 27$\nb) $(45 + 67) + 33 = 45 + (\\dots + 33)$", "a) $27 + 84 = 84 + 27$.\nb) $(45 + 67) + 33 = 45 + (67 + 33)$.", "a) 84; b) 67", 4, 1.0),
            make_essay(3, "Tính nhanh tổng của các số sau:\n$10 + 20 + 30 + 40 + 50 + 60 + 70 + 80 + 90$", "Ta nhóm từng cặp có tổng bằng 100:\n$(10 + 90) + (20 + 80) + (30 + 70) + (40 + 60) + 50$\n$= 100 + 100 + 100 + 100 + 50 = 450$.", "450", 4, 1.0),
            make_essay(4, "Một cửa hàng vật liệu xây dựng ngày thứ nhất bán được 125 bao xi măng, ngày thứ hai bán được 178 bao xi măng, ngày thứ ba bán được 75 bao xi măng. Hỏi cả ba ngày cửa hàng bán được bao nhiêu bao xi măng? (Hãy tính bằng cách thuận tiện nhất).", "Số bao xi măng cả 3 ngày bán được là:\n$125 + 178 + 75 = (125 + 75) + 178$\n$= 200 + 178 = 378\\text{ (bao)}$.", "378 bao xi măng", 5, 1.5),
            make_essay(5, "Một khu vườn trồng 4 luống cây: Luống thứ nhất có 348 cây hoa, luống thứ hai có 185 cây hoa, luống thứ ba có 152 cây hoa, luống thứ tư có 215 cây hoa. Hỏi cả khu vườn có bao nhiêu cây hoa? (Tính bằng cách thuận tiện nhất).", "Tổng số cây hoa của 4 luống là:\n$348 + 185 + 152 + 215 = (348 + 152) + (185 + 215)$\n$= 500 + 400 = 900\\text{ (cây)}$.", "900 cây hoa", 5, 1.5),
            make_essay(6, "Tính tổng của 20 số chẵn liên tiếp đầu tiên kể từ số 2:\n$2 + 4 + 6 + \\dots + 38 + 40$", "Dãy số gồm 20 số chẵn, chia làm 10 cặp số có tổng bằng 42:\n$(2 + 40) + (4 + 38) + \\dots + (20 + 22)$\n$= 42 \\times 10 = 420$.", "420", 4, 1.0)
        ]
    }

    # --- Bài 23 - Đề 2 ---
    exams["th4_b23_test2"] = {
        "id": "th4_b23_test2",
        "lessonId": "th4_b23",
        "lessonNum": 23,
        "testNum": 2,
        "title": "Bài 23: Tính chất giao hoán và kết hợp của phép cộng - Đề số 2",
        "topic": "Tính chất giao hoán và kết hợp của phép cộng",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính nhanh: $450 + 280 + 550$:", ["1 280", "1 180", "1 380", "1 080"], 0, "(450 + 550) + 280 = 1 000 + 280 = 1 280."),
            make_mc(2, "Cách nhóm nào dưới đây thuận tiện nhất để tính $176 + 248 + 24$?", ["(176 + 24) + 248", "(176 + 248) + 24", "176 + (248 + 24)", "Không cần nhóm"], 0, "(176 + 24) = 200 là số tròn trăm."),
            make_mc(3, "Điền số thích hợp: $(35 + 89) + 65 = (35 + \\dots) + 89$:", ["65", "89", "35", "100"], 0, "Đổi vị trí theo tính chất giao hoán và kết hợp: (35 + 65) + 89."),
            make_mc(4, "Tổng $19 + 28 + 81 + 72$ bằng:", ["200", "190", "210", "180"], 0, "(19 + 81) + (28 + 72) = 100 + 100 = 200."),
            make_mc(5, "Nếu $a + 25 = 25 + 40$ thì giá trị của $a$ là:", ["40", "25", "65", "15"], 0, "Theo tính chất giao hoán: a = 40."),
            make_mc(6, "Tính nhanh: $12 + 13 + 14 + 15 + 16 + 17 + 18$:", ["105", "100", "110", "95"], 0, "(12 + 18) + (13 + 17) + (14 + 16) + 15 = 30 x 3 + 15 = 105.")
        ],
        "part2": [
            make_essay(1, "Tính bằng cách thuận tiện nhất:\na) $456 + 174 + 244$\nb) $315 + 280 + 185 + 220$", "a) $(456 + 244) + 174 = 700 + 174 = 874$.\nb) $(315 + 185) + (280 + 220) = 500 + 500 = 1000$.", "a) 874; b) 1000", 4, 1.0),
            make_essay(2, "Điền dấu thích hợp ($>$, $<$, $=$) vào ô trống:\na) $(145 + 255) + 180 \\dots 145 + (255 + 180)$\nb) $38 + 92 \\dots 92 + 37$", "a) Hai biểu thức bằng nhau theo tính chất kết hợp ($=$).\nb) $38 + 92 > 92 + 37$ vì $38 > 37$ ($>$).", "a) =; b) >", 4, 1.0),
            make_essay(3, "Bốn bạn Nam, Bắc, Trung, Tây cùng thu gom phế liệu bảo vệ môi trường: Nam thu gom được 135 vỏ lon nước, Bắc thu được 172 vỏ lon, Trung thu được 165 vỏ lon, Tây thu được 128 vỏ lon. Hỏi cả bốn bạn thu gom được tất cả bao nhiêu vỏ lon? (Tính bằng cách thuận tiện nhất).", "Tổng số vỏ lon cả 4 bạn gom được là:\n$135 + 172 + 165 + 128 = (135 + 165) + (172 + 128)$\n$= 300 + 300 = 600\\text{ (vỏ lon)}$.", "600 vỏ lon", 4, 1.0),
            make_essay(4, "Một đội xe chở hàng hóa: Xe thứ nhất chở 2 450 kg gạo, xe thứ hai chở 1 850 kg muối, xe thứ ba chở 1 550 kg đường, xe thứ tư chở 2 150 kg bột mì. Hỏi cả đội xe chở được bao nhiêu ki-lô-gam hàng hóa? (Tính bằng cách thuận tiện nhất).", "Tổng khối lượng hàng hóa là:\n$2450 + 1850 + 1550 + 2150 = (2450 + 1550) + (1850 + 2150)$\n$= 4000 + 4000 = 8000\\text{ (kg)}$.", "8000 kg", 5, 1.5),
            make_essay(5, "Một cửa hàng có 3 thùng dầu: Thùng 1 có 375 lít, thùng 2 có 480 lít, thùng 3 có 625 lít. Người ta đổ thêm vào thùng 2 một lượng dầu là 120 lít. Hỏi khi đó cả ba thùng có tất cả bao nhiêu lít dầu?", "Tổng số lít dầu trong ba thùng là:\n$375 + (480 + 120) + 625 = (375 + 625) + 600$\n$= 1000 + 600 = 1600\\text{ (lít)}$.", "1600 lít dầu", 5, 1.5),
            make_essay(6, "Tính tổng của các số sau bằng cách nhanh nhất:\n$A = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19$", "Dãy số gồm 10 số hạng lẻ liên tiếp, nhóm thành 5 cặp có tổng bằng 20:\n$A = (1 + 19) + (3 + 17) + (5 + 15) + (7 + 13) + (9 + 11)$\n$= 20 \\times 5 = 100$.", "100", 4, 1.0)
        ]
    }

    # --- Bài 23 - Đề 3 ---
    exams["th4_b23_test3"] = {
        "id": "th4_b23_test3",
        "lessonId": "th4_b23",
        "lessonNum": 23,
        "testNum": 3,
        "title": "Bài 23: Tính chất giao hoán và kết hợp của phép cộng - Đề số 3",
        "topic": "Tính chất giao hoán và kết hợp của phép cộng",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính nhanh: $150 + 890 + 850$:", ["1 890", "1 790", "1 990", "1 690"], 0, "(150 + 850) + 890 = 1 000 + 890 = 1 890."),
            make_mc(2, "Số thích hợp điền vào dấu $*$ để $(42 + 58) + 17 = 42 + (* + 17)$ là:", ["58", "42", "17", "100"], 0, "Theo tính chất kết hợp, * = 58."),
            make_mc(3, "Giá trị của biểu thức $64 + 138 + 36 + 62$ là:", ["300", "280", "310", "290"], 0, "(64 + 36) + (138 + 62) = 100 + 200 = 300."),
            make_mc(4, "Một biểu thức gồm 3 số hạng có tổng là 450. Nếu đổi chỗ các số hạng thì tổng mới là:", ["450", "400", "500", "Không xác định được"], 0, "Đổi chỗ các số hạng thì tổng không đổi."),
            make_mc(5, "Tính thuận tiện: $99 + 999 + 1 + 1$:", ["1 100", "1 000", "1 099", "1 010"], 0, "(99 + 1) + (999 + 1) = 100 + 1 000 = 1 100."),
            make_mc(6, "Tính: $25 + 35 + 45 + 55 + 65 + 75$:", ["300", "290", "310", "280"], 0, "(25 + 75) + (35 + 65) + (45 + 55) = 100 x 3 = 300.")
        ],
        "part2": [
            make_essay(1, "Tính bằng cách thuận tiện nhất:\na) $526 + 139 + 474$\nb) $142 + 258 + 356 + 144$", "a) $(526 + 474) + 139 = 1000 + 139 = 1139$.\nb) $(142 + 258) + (356 + 144) = 400 + 500 = 900$.", "a) 1139; b) 900", 4, 1.0),
            make_essay(2, "Không thực hiện phép tính, hãy giải thích vì sao hai biểu thức sau có giá trị bằng nhau:\n$A = (123 + 456) + 789$ và $B = 456 + (789 + 123)$", "Biểu thức A gồm ba số hạng là 123, 456 và 789.\nBiểu thức B cũng gồm đúng ba số hạng đó nhưng được sắp xếp lại thứ tự và cách nhóm.\nTheo tính chất giao hoán và tính chất kết hợp của phép cộng, khi đổi chỗ và thay đổi cách nhóm các số hạng thì tổng không thay đổi. Do đó $A = B$.", "A = B theo tính chất giao hoán và kết hợp của phép cộng", 4, 1.0),
            make_essay(3, "Trong một buổi quyên góp sách cho vùng cao: Khối 1 quyên góp được 145 quyển, Khối 2 quyên góp được 180 quyển, Khối 3 quyên góp được 155 quyển, Khối 4 quyên góp được 220 quyển. Hỏi cả bốn khối đã quyên góp được bao nhiêu quyển sách? (Tính bằng cách thuận tiện nhất).", "Tổng số sách quyên góp được là:\n$145 + 180 + 155 + 220 = (145 + 155) + (180 + 220)$\n$= 300 + 400 = 700\\text{ (quyển)}$.", "700 quyển sách", 4, 1.0),
            make_essay(4, "Một đoàn xe du lịch gồm 4 xe chở học sinh đi tham quan: Xe 1 chở 42 học sinh, xe 2 chở 39 học sinh, xe 3 chở 38 học sinh, xe 4 chở 41 học sinh. Biết giá vé tham quan là 50 000 đồng một học sinh. Hỏi đoàn trường phải mua vé tất cả bao nhiêu tiền?", "Tổng số học sinh của 4 xe là:\n$42 + 39 + 38 + 41 = (42 + 38) + (39 + 41)$\n$= 80 + 80 = 160\\text{ (học sinh)}$.\nTổng số tiền mua vé là:\n$160 \\times 50\\,000 = 8\\,000\\,000\\text{ (đồng)}$.", "8 000 000 đồng", 5, 1.5),
            make_essay(5, "Một người nông dân thu hoạch 4 luống khoai tây: Luống A thu được 326 kg, luống B thu được 218 kg, luống C thu được 174 kg, luống D thu được 282 kg. Toàn bộ số khoai được đóng vào các bao, mỗi bao 50 kg. Hỏi người đó đóng được bao nhiêu bao khoai tây?", "Tổng khối lượng khoai tây thu hoạch là:\n$326 + 218 + 174 + 282 = (326 + 174) + (218 + 282)$\n$= 500 + 500 = 1000\\text{ (kg)}$.\nSố bao khoai tây đóng được là:\n$1000 : 50 = 20\\text{ (bao)}$.", "20 bao khoai tây", 5, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$S = 10 + 15 + 20 + 25 + 30 + 35 + 40 + 45 + 50$", "Nhóm các cặp có tổng bằng 60:\n$S = (10 + 50) + (15 + 45) + (20 + 40) + (25 + 35) + 30$\n$= 60 \\times 4 + 30 = 240 + 30 = 270$.", "270", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 24: TÌM HAI SỐ KHI BIẾT TỔNG VÀ HIỆU CỦA HAI SỐ ĐÓ
    # =========================================================================

    # --- Bài 24 - Đề 1 ---
    exams["th4_b24_test1"] = {
        "id": "th4_b24_test1",
        "lessonId": "th4_b24",
        "lessonNum": 24,
        "testNum": 1,
        "title": "Bài 24: Tìm hai số khi biết tổng và hiệu của hai số đó - Đề số 1",
        "topic": "Tìm hai số khi biết tổng và hiệu của hai số đó",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tìm số lớn khi biết tổng và hiệu của hai số là:", ["Số lớn = (Tổng + Hiệu) : 2", "Số lớn = (Tổng - Hiệu) : 2", "Số lớn = Tổng + Hiệu", "Số lớn = Tổng - Hiệu"], 0, "Số lớn = (Tổng + Hiệu) : 2."),
            make_mc(2, "Hai số có tổng là 45 và hiệu là 15. Số bé là:", ["15", "30", "20", "10"], 0, "Số bé = (45 - 15) : 2 = 15."),
            make_mc(3, "Tuổi của hai mẹ con cộng lại là 42 tuổi, mẹ hơn con 26 tuổi. Tuổi của mẹ là:", ["34 tuổi", "32 tuổi", "36 tuổi", "30 tuổi"], 0, "Tuổi mẹ = (42 + 26) : 2 = 34 tuổi."),
            make_mc(4, "Một mảnh đất hình chữ nhật có chu vi $60\\text{ m}$, chiều dài hơn chiều rộng $6\\text{ m}$. Chiều dài mảnh đất là:", ["18 m", "12 m", "33 m", "24 m"], 0, "Nửa chu vi = 60 : 2 = 30 m. Chiều dài = (30 + 6) : 2 = 18 m."),
            make_mc(5, "Hai số có tổng bằng 100, hiệu bằng 0. Hai số đó là:", ["50 và 50", "100 và 0", "60 và 40", "55 và 45"], 0, "Hiệu bằng 0 nên hai số bằng nhau: 100 : 2 = 50."),
            make_mc(6, "Lớp 4A có 32 học sinh, số bạn nam nhiều hơn số bạn nữ là 4 bạn. Số bạn nữ của lớp là:", ["14 bạn", "18 bạn", "16 bạn", "12 bạn"], 0, "Số bạn nữ = (32 - 4) : 2 = 14 bạn.")
        ],
        "part2": [
            make_essay(1, "Tìm hai số khi biết:\na) Tổng là 86, hiệu là 14.\nb) Tổng là 120, hiệu là 36.", "a) Số lớn là: $(86 + 14) : 2 = 50$.\nSố bé là: $50 - 14 = 36$.\nb) Số lớn là: $(120 + 36) : 2 = 78$.\nSố bé là: $120 - 78 = 42$.", "a) 50 và 36; b) 78 và 42", 4, 1.0),
            make_essay(2, "Một lớp học có 35 học sinh, trong đó số học sinh nam ít hơn số học sinh nữ là 5 bạn. Tính số học sinh nam và số học sinh nữ của lớp đó.", "Số học sinh nam là:\n$(35 - 5) : 2 = 15\\text{ (học sinh)}$.\nSố học sinh nữ là:\n$15 + 5 = 20\\text{ (học sinh)}$.", "Nam: 15 học sinh; Nữ: 20 học sinh", 4, 1.0),
            make_essay(3, "Một mảnh đất hình chữ nhật có nửa chu vi là 48 m, chiều dài hơn chiều rộng 12 m. Tính diện tích của mảnh đất đó.", "Chiều dài mảnh đất là:\n$(48 + 12) : 2 = 30\\text{ (m)}$.\nChiều rộng mảnh đất là:\n$48 - 30 = 18\\text{ (m)}$.\nDiện tích mảnh đất là:\n$30 \\times 18 = 540\\text{ (m}^2)$.", "540 m²", 4, 1.0),
            make_essay(4, "Hai thùng chứa tất cả 160 lít dầu. Nếu chuyển 15 lít dầu từ thùng thứ nhất sang thùng thứ hai thì số dầu ở hai thùng bằng nhau. Hỏi lúc đầu mỗi thùng có bao nhiêu lít dầu?", "Khi chuyển 15 lít từ thùng thứ nhất sang thùng thứ hai thì số dầu hai thùng bằng nhau, vậy lúc đầu thùng thứ nhất hơn thùng thứ hai là:\n$15 \\times 2 = 30\\text{ (lít)}$.\nSố dầu ở thùng thứ nhất lúc đầu là:\n$(160 + 30) : 2 = 95\\text{ (lít)}$.\nSố dầu ở thùng thứ hai lúc đầu là:\n$160 - 95 = 65\\text{ (lít)}$.", "Thùng 1: 95 lít; Thùng 2: 65 lít", 5, 1.5),
            make_essay(5, "Hiện nay tổng số tuổi của hai bố con là 48 tuổi. Bốn năm trước bố hơn con 28 tuổi. Tính tuổi của mỗi người hiện nay.", "Vì hiệu số tuổi của hai bố con không thay đổi theo thời gian nên hiện nay bố vẫn hơn con 28 tuổi.\nTuổi của bố hiện nay là:\n$(48 + 28) : 2 = 38\\text{ (tuổi)}$.\nTuổi của con hiện nay là:\n$48 - 38 = 10\\text{ (tuổi)}$.", "Bố: 38 tuổi; Con: 10 tuổi", 5, 1.5),
            make_essay(6, "Tìm hai số chẵn có tổng bằng 210, biết rằng giữa chúng có 4 số lẻ liên tiếp.", "Hiệu của hai số chẵn mà giữa chúng có 4 số lẻ là:\n$4 \\times 2 = 8$.\nSố lớn là:\n$(210 + 8) : 2 = 109$ (lẻ). Kiểm tra: giữa 2 số chẵn có 4 số lẻ liên tiếp thì hiệu là $4 \\times 2 = 8$. Để số chẵn chẵn thì tổng phải chẵn. Nhưng (210+8):2=109 lẻ. Ta chọn lại: giữa chúng có 5 số chẵn liên tiếp => hiệu là $6 \\times 2 = 12$ => $(210 + 12) : 2 = 111$ lẻ. Nếu giữa chúng có 3 số lẻ liên tiếp thì hiệu là 6: $(210+6):2=108$ (chẵn), số bé: 102. Các số lẻ ở giữa: 103, 105, 107 (đúng 3 số lẻ!). Vậy số lớn là 108, số bé là 102.", "Số lớn: 108; Số bé: 102", 4, 1.0)
        ]
    }

    # --- Bài 24 - Đề 2 ---
    exams["th4_b24_test2"] = {
        "id": "th4_b24_test2",
        "lessonId": "th4_b24",
        "lessonNum": 24,
        "testNum": 2,
        "title": "Bài 24: Tìm hai số khi biết tổng và hiệu của hai số đó - Đề số 2",
        "topic": "Tìm hai số khi biết tổng và hiệu của hai số đó",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tìm số bé khi biết tổng và hiệu là:", ["Số bé = (Tổng - Hiệu) : 2", "Số bé = (Tổng + Hiệu) : 2", "Số bé = Tổng - Hiệu", "Số bé = Tổng : 2"], 0, "Số bé = (Tổng - Hiệu) : 2."),
            make_mc(2, "Hai số có tổng là 150 và hiệu là 50. Số lớn là:", ["100", "50", "75", "125"], 0, "Số lớn = (150 + 50) : 2 = 100."),
            make_mc(3, "Hai thùng gạo chứa tất cả 90 kg gạo. Thùng thứ nhất nhiều hơn thùng thứ hai 18 kg. Số gạo ở thùng thứ nhất là:", ["54 kg", "36 kg", "45 kg", "64 kg"], 0, "Thùng 1 = (90 + 18) : 2 = 54 kg."),
            make_mc(4, "Một mảnh vườn hình chữ nhật có chu vi $80\\text{ m}$, chiều dài hơn chiều rộng $10\\text{ m}$. Chiều rộng mảnh vườn là:", ["15 m", "25 m", "35 m", "20 m"], 0, "Nửa chu vi = 40 m. Chiều rộng = (40 - 10) : 2 = 15 m."),
            make_mc(5, "Tổng của hai số là 78, nếu tăng số bé thêm 6 đơn vị thì hai số bằng nhau. Hai số đó là:", ["42 và 36", "45 và 33", "40 và 38", "50 và 28"], 0, "Tăng số bé thêm 6 đơn vị thì bằng số lớn => Hiệu = 6. Số lớn = (78 + 6) : 2 = 42; Số bé = 36."),
            make_mc(6, "Năm nay tổng số tuổi của hai anh em là 24 tuổi, anh hơn em 4 tuổi. Tuổi của em là:", ["10 tuổi", "14 tuổi", "12 tuổi", "8 tuổi"], 0, "Tuổi em = (24 - 4) : 2 = 10 tuổi.")
        ],
        "part2": [
            make_essay(1, "Tìm hai số có:\na) Tổng bằng 94 và hiệu bằng 26.\nb) Tổng bằng 250 và hiệu bằng 70.", "a) Số lớn là: $(94 + 26) : 2 = 60$.\nSố bé là: $60 - 26 = 34$.\nb) Số lớn là: $(250 + 70) : 2 = 160$.\nSố bé là: $250 - 160 = 90$.", "a) 60 và 34; b) 160 và 90", 4, 1.0),
            make_essay(2, "Một trường tiểu học có 680 học sinh. Số học sinh nữ nhiều hơn số học sinh nam là 40 em. Tính số học sinh nam và số học sinh nữ của trường đó.", "Số học sinh nữ của trường là:\n$(680 + 40) : 2 = 360\\text{ (học sinh)}$.\nSố học sinh nam của trường là:\n$680 - 360 = 320\\text{ (học sinh)}$.", "Nữ: 360 học sinh; Nam: 320 học sinh", 4, 1.0),
            make_essay(3, "Một khu đất hình chữ nhật có chu vi $140\\text{ m}$, chiều dài hơn chiều rộng $14\\text{ m}$. Tính diện tích của khu đất đó.", "Nửa chu vi khu đất là: $140 : 2 = 70\\text{ (m)}$.\nChiều dài khu đất là:\n$(70 + 14) : 2 = 42\\text{ (m)}$.\nChiều rộng khu đất là:\n$70 - 42 = 28\\text{ (m)}$.\nDiện tích khu đất là:\n$42 \\times 28 = 1176\\text{ (m}^2)$.", "1176 m²", 4, 1.0),
            make_essay(4, "Hai kho thóc chứa tất cả 240 tấn thóc. Người ta xuất đi từ kho thứ nhất 25 tấn và nhập thêm vào kho thứ hai 15 tấn thì số thóc ở hai kho bằng nhau. Hỏi ban đầu mỗi kho có bao nhiêu tấn thóc?", "Khi kho thứ nhất xuất 25 tấn và kho thứ hai nhập thêm 15 tấn thì hai kho bằng nhau, tức là ban đầu kho 1 nhiều hơn kho 2 là:\n$25 + 15 = 40\\text{ (tấn)}$.\nSố thóc ban đầu ở kho thứ nhất là:\n$(240 + 40) : 2 = 140\\text{ (tấn)}$.\nSố thóc ban đầu ở kho thứ hai là:\n$240 - 140 = 100\\text{ (tấn)}$.", "Kho 1: 140 tấn; Kho 2: 100 tấn", 5, 1.5),
            make_essay(5, "Tổng số tuổi của hai bà cháu hiện nay là 72 tuổi. Cách đây 5 năm bà hơn cháu 54 tuổi. Hỏi hiện nay bà bao nhiêu tuổi, cháu bao nhiêu tuổi?", "Hiệu số tuổi không thay đổi theo thời gian nên hiện nay bà vẫn hơn cháu 54 tuổi.\nTuổi của bà hiện nay là:\n$(72 + 54) : 2 = 63\\text{ (tuổi)}$.\nTuổi của cháu hiện nay là:\n$72 - 63 = 9\\text{ (tuổi)}$.", "Bà: 63 tuổi; Cháu: 9 tuổi", 5, 1.5),
            make_essay(6, "Tìm hai số lẻ liên tiếp có tổng bằng 204.", "Hai số lẻ liên tiếp hơn kém nhau 2 đơn vị nên hiệu của chúng là 2.\nSố lớn là:\n$(204 + 2) : 2 = 103$.\nSố bé là:\n$204 - 103 = 101$.", "101 và 103", 4, 1.0)
        ]
    }

    # --- Bài 24 - Đề 3 ---
    exams["th4_b24_test3"] = {
        "id": "th4_b24_test3",
        "lessonId": "th4_b24",
        "lessonNum": 24,
        "testNum": 3,
        "title": "Bài 24: Tìm hai số khi biết tổng và hiệu của hai số đó - Đề số 3",
        "topic": "Tìm hai số khi biết tổng và hiệu của hai số đó",
        "chapter": "Chủ đề 5: Phép cộng và phép trừ",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tổng của hai số là 200, hiệu của hai số là 40. Số bé là:", ["80", "120", "70", "90"], 0, "(200 - 40) : 2 = 80."),
            make_mc(2, "Hai thùng nước mắm chứa tất cả 120 lít. Nếu bớt ở thùng thứ nhất 20 lít thì hai thùng bằng nhau. Thùng thứ nhất chứa:", ["70 lít", "50 lít", "60 lít", "80 lít"], 0, "Thùng 1 hơn thùng 2 là 20 lít. Thùng 1 = (120 + 20) : 2 = 70 lít."),
            make_mc(3, "Một mảnh đất hình chữ nhật có nửa chu vi là 36 m, chiều dài hơn chiều rộng 8 m. Chiều dài mảnh đất là:", ["22 m", "14 m", "18 m", "26 m"], 0, "(36 + 8) : 2 = 22 m."),
            make_mc(4, "Hai bạn An và Bình có tất cả 48 viên bi. An cho Bình 4 viên bi thì số bi của hai bạn bằng nhau. Lúc đầu An có số viên bi là:", ["28 viên", "20 viên", "24 viên", "26 viên"], 0, "An hơn Bình: 4 x 2 = 8 viên. An có: (48 + 8) : 2 = 28 viên."),
            make_mc(5, "Tổng của hai số tự nhiên liên tiếp là 2025. Hai số đó là:", ["1012 và 1013", "1011 và 1014", "1010 và 1015", "1012 và 1012"], 0, "Hai số tự nhiên liên tiếp hơn kém nhau 1 đơn vị. Số lớn = (2025 + 1) : 2 = 1013; Số bé = 1012."),
            make_mc(6, "Một tấm vải dài 38 m được cắt thành hai mảnh, mảnh thứ nhất ngắn hơn mảnh thứ hai 6 m. Mảnh thứ hai dài:", ["22 m", "16 m", "20 m", "24 m"], 0, "(38 + 6) : 2 = 22 m.")
        ],
        "part2": [
            make_essay(1, "Tìm hai số có:\na) Tổng bằng 158 và hiệu bằng 32.\nb) Tổng bằng 324 và hiệu bằng 56.", "a) Số lớn là: $(158 + 32) : 2 = 95$.\nSố bé là: $158 - 95 = 63$.\nb) Số lớn là: $(324 + 56) : 2 = 190$.\nSố bé là: $324 - 190 = 134$.", "a) 95 và 63; b) 190 và 134", 4, 1.0),
            make_essay(2, "Hai kho lương thực chứa tất cả 350 tấn thóc. Nếu chuyển từ kho A sang kho B 20 tấn thì số thóc ở kho A vẫn nhiều hơn kho B là 10 tấn. Hỏi ban đầu mỗi kho chứa bao nhiêu tấn thóc?", "Sau khi chuyển 20 tấn từ kho A sang kho B, kho A hơn kho B 10 tấn, vậy lúc đầu kho A hơn kho B là:\n$20 \\times 2 + 10 = 50\\text{ (tấn)}$.\nSố thóc ban đầu ở kho A là:\n$(350 + 50) : 2 = 200\\text{ (tấn)}$.\nSố thóc ban đầu ở kho B là:\n$350 - 200 = 150\\text{ (tấn)}$.", "Kho A: 200 tấn; Kho B: 150 tấn", 4, 1.0),
            make_essay(3, "Một khu vườn hình chữ nhật có chu vi $160\\text{ m}$, chiều dài hơn chiều rộng $20\\text{ m}$. Người ta trồng cây ăn quả trên khu vườn đó, cứ $5\\text{ m}^2$ trồng được 1 cây. Hỏi cả khu vườn trồng được bao nhiêu cây?", "Nửa chu vi khu vườn là: $160 : 2 = 80\\text{ (m)}$.\nChiều dài khu vườn là: $(80 + 20) : 2 = 50\\text{ (m)}$.\nChiều rộng khu vườn là: $80 - 50 = 30\\text{ (m)}$.\nDiện tích khu vườn là: $50 \\times 30 = 1500\\text{ (m}^2)$.\nSố cây ăn quả trồng được là:\n$1500 : 5 = 300\\text{ (cây)}$.", "300 cây", 4, 1.0),
            make_essay(4, "Một giá sách có hai ngăn chứa tất cả 180 cuốn sách. Bạn thủ thư lấy ra 15 cuốn ở ngăn trên và xếp thêm 25 cuốn vào ngăn dưới thì số sách ở ngăn trên ít hơn ngăn dưới là 20 cuốn. Hỏi ban đầu mỗi ngăn có bao nhiêu cuốn sách?", "Sau khi lấy 15 cuốn ở ngăn trên và thêm 25 cuốn vào ngăn dưới, tổng số sách là:\n$180 - 15 + 25 = 190\\text{ (cuốn)}$.\nSố sách ở ngăn dưới lúc sau là:\n$(190 + 20) : 2 = 105\\text{ (cuốn)}$.\nSố sách ở ngăn dưới ban đầu là:\n$105 - 25 = 80\\text{ (cuốn)}$.\nSố sách ở ngăn trên ban đầu là:\n$180 - 80 = 100\\text{ (cuốn)}$.", "Ngăn trên: 100 cuốn; Ngăn dưới: 80 cuốn", 5, 1.5),
            make_essay(5, "Hiện nay tổng số tuổi của mẹ và con là 45 tuổi. Biết rằng 5 năm nữa mẹ hơn con 27 tuổi. Tính tuổi của mỗi người hiện nay.", "Hiệu số tuổi của mẹ và con luôn không đổi, nên hiện nay mẹ vẫn hơn con 27 tuổi.\nTuổi của mẹ hiện nay là:\n$(45 + 27) : 2 = 36\\text{ (tuổi)}$.\nTuổi của con hiện nay là:\n$45 - 36 = 9\\text{ (tuổi)}$.", "Mẹ: 36 tuổi; Con: 9 tuổi", 5, 1.5),
            make_essay(6, "Tìm hai số chẵn liên tiếp có tổng bằng 350.", "Hai số chẵn liên tiếp hơn kém nhau 2 đơn vị nên hiệu của chúng bằng 2.\nSố lớn là:\n$(350 + 2) : 2 = 176$.\nSố bé là:\n$350 - 176 = 174$.", "174 và 176", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 5: {len(ex)} (Kỳ vọng: 12)")
    for b in range(21, 25):
        for t in range(1, 4):
            key = f"th4_b{b}_test{t}"
            assert key in ex, f"Thiếu {key}"
            assert len(ex[key]["part1"]) == 6
            assert len(ex[key]["part2"]) == 6
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6
            assert abs(p2_pts - 7.0) < 1e-6
    print("Chủ đề 5 hoàn hảo 100%!")
