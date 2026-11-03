# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 11: ÔN TẬP CUỐI NĂM (PHẦN 2: BÀI 59 VÀ BÀI 60)
Toán lớp 5 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 2 bài học x 3 đề độc lập = 6 đề thi (th5_b59_test1 -> th5_b60_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from th5_ch9_part1 import make_mc, make_essay

def get_ch11_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 59: ÔN TẬP TOÁN CHUYỂN ĐỘNG ĐỀU
    # =========================================================================
    # --- Bài 59 - Đề 1 ---
    exams["th5_b59_test1"] = {
        "id": "th5_b59_test1",
        "lessonId": "th5_b59",
        "lessonNum": 59,
        "testNum": 1,
        "title": "Bài 59: Ôn tập toán chuyển động đều - Đề số 1",
        "topic": "Ôn tập toán chuyển động đều",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một ô tô đi được quãng đường $150\\text{ km}$ trong 3 giờ. Vận tốc của ô tô là:", ["50 km/giờ", "45 km/giờ", "60 km/giờ", "40 km/giờ"], 0, "150 : 3 = 50 km/giờ."),
            make_mc(2, "Một người đi xe máy với vận tốc $38\\text{ km/giờ}$ trong 2,5 giờ. Quãng đường đi được là:", ["95 km", "90 km", "100 km", "85 km"], 0, "38 x 2,5 = 95 km."),
            make_mc(3, "Một người chạy cự ly $600\\text{ m}$ với vận tốc $5\\text{ m/giây}$. Thời gian chạy là:", ["120 giây", "100 giây", "150 giây", "2 phút 30 giây"], 0, "600 : 5 = 120 giây = 2 phút."),
            make_mc(4, "Hai ô tô khởi hành cùng lúc đi ngược chiều nhau từ hai điểm cách nhau $160\\text{ km}$ với vận tốc $45\\text{ km/giờ}$ và $35\\text{ km/giờ}$. Hai xe gặp nhau sau:", ["2 giờ", "2,5 giờ", "1,8 giờ", "3 giờ"], 0, "t = 160 : (45 + 35) = 160 : 80 = 2 giờ."),
            make_mc(5, "Một ca nô đi xuôi dòng quãng đường $36\\text{ km}$ hết 1,2 giờ. Vận tốc xuôi dòng của ca nô là:", ["30 km/giờ", "25 km/giờ", "32 km/giờ", "28 km/giờ"], 0, "36 : 1,2 = 30 km/giờ."),
            make_mc(6, "Đổi vận tốc $18\\text{ km/giờ} = \\dots \\text{ m/giây}$:", ["5 m/giây", "6 m/giây", "4 m/giây", "10 m/giây"], 0, "18 : 3,6 = 5 m/giây.")
        ],
        "part2": [
            make_essay(1, "Một người đi xe máy từ A lúc 7 giờ 30 phút và đến B lúc 10 giờ với vận tốc $42\\text{ km/giờ}$. Dọc đường người đó dừng nghỉ 15 phút. Tính quãng đường AB.", "Thời gian thực tế người đó đi trên đường là:\n$10\\text{ giờ} - 7\\text{ giờ } 30\\text{ phút} - 15\\text{ phút} = 2\\text{ giờ } 15\\text{ phút} = 2,25\\text{ giờ}$.\nQuãng đường AB dài là:\n$42 \\times 2,25 = 94,5\\text{ (km)}$.", "94,5 km", 4, 1.0),
            make_essay(2, "Quãng đường AB dài $120\\text{ km}$. Một ô tô đi từ A đến B với vận tốc $50\\text{ km/giờ}$. Cùng lúc đó một xe máy đi từ B về A với vận tốc $30\\text{ km/giờ}$. Hỏi sau bao lâu hai xe gặp nhau?", "Tổng vận tốc của hai xe là:\n$50 + 30 = 80\\text{ (km/giờ)}$.\nThời gian để hai xe gặp nhau là:\n$120 : 80 = 1,5\\text{ (giờ)} = 1\\text{ giờ } 30\\text{ phút}$.", "1,5 giờ (hay 1 giờ 30 phút)", 4, 1.0),
            make_essay(3, "Lúc 7 giờ một người đi xe đạp từ A với vận tốc $12\\text{ km/giờ}$. Đến 8 giờ 30 phút một người đi xe máy cũng từ A đuổi theo với vận tốc $36\\text{ km/giờ}$. Hỏi người đi xe máy đuổi kịp người đi xe đạp lúc mấy giờ?", "Thời gian xe đạp đi trước là: $8\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} = 1,5\\text{ giờ}$.\nQuãng đường xe đạp đi trước là: $12 \\times 1,5 = 18\\text{ (km)}$.\nHiệu vận tốc hai xe là: $36 - 12 = 24\\text{ (km/giờ)}$.\nThời gian xe máy đuổi kịp xe đạp là: $18 : 24 = 0,75\\text{ (giờ)} = 45\\text{ phút}$.\nXe máy đuổi kịp xe đạp lúc: $8\\text{ giờ } 30\\text{ phút} + 45\\text{ phút} = 9\\text{ giờ } 15\\text{ phút}$.", "9 giờ 15 phút", 4, 1.0),
            make_essay(4, "Một ca nô đi xuôi dòng từ A đến B dài $54\\text{ km}$ hết 1,8 giờ và đi ngược dòng từ B về A hết 2,7 giờ. Tính vận tốc của dòng nước và vận tốc của ca nô khi nước yên lặng.", "Vận tốc xuôi dòng là: $54 : 1,8 = 30\\text{ (km/giờ)}$.\nVận tốc ngược dòng là: $54 : 2,7 = 20\\text{ (km/giờ)}$.\nVận tốc dòng nước là: $(30 - 20) : 2 = 5\\text{ (km/giờ)}$.\nVận tốc thực của ca nô là: $30 - 5 = 25\\text{ (km/giờ)}$.", "Vận tốc ca nô: 25 km/giờ; Vận tốc dòng nước: 5 km/giờ", 5, 1.5),
            make_essay(5, "Một đoàn tàu hỏa chạy với vận tốc $45\\text{ km/giờ}$ đi qua một cây cầu dài $350\\text{ m}$ mất 36 giây. Tính chiều dài của đoàn tàu hỏa.", "Đổi vận tốc tàu: $45\\text{ km/giờ} = 45 : 3,6 = 12,5\\text{ (m/giây)}$.\nQuãng đường tàu đi trong 36 giây là: $12,5 \\times 36 = 450\\text{ (m)}$.\nChiều dài đoàn tàu hỏa là: $450 - 350 = 100\\text{ (m)}$.", "100 m", 5, 1.5),
            make_essay(6, "Bác Nam đi xe máy từ A đến B với vận tốc $40\\text{ km/giờ}$ hết 2,5 giờ. Lúc về bác đi với vận tốc $50\\text{ km/giờ}$. Hỏi thời gian bác Nam đi từ B về A ít hơn thời gian đi từ A đến B bao nhiêu phút?", "Quãng đường AB dài là: $40 \\times 2,5 = 100\\text{ (km)}$.\nThời gian đi từ B về A là: $100 : 50 = 2\\text{ (giờ)}$.\nThời gian về ít hơn thời gian đi là:\n$2,5\\text{ giờ} - 2\\text{ giờ} = 0,5\\text{ giờ} = 30\\text{ phút}$.", "30 phút", 4, 1.0)
        ]
    }

    # --- Bài 59 - Đề 2 ---
    exams["th5_b59_test2"] = {
        "id": "th5_b59_test2",
        "lessonId": "th5_b59",
        "lessonNum": 59,
        "testNum": 2,
        "title": "Bài 59: Ôn tập toán chuyển động đều - Đề số 2",
        "topic": "Ôn tập toán chuyển động đều",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người đi xe máy đi quãng đường $105\\text{ km}$ với vận tốc $42\\text{ km/giờ}$. Thời gian đi là:", ["2,5 giờ", "2 giờ", "3 giờ", "2,25 giờ"], 0, "105 : 42 = 2,5 giờ (2 giờ 30 phút)."),
            make_mc(2, "Một ô tô đi với vận tốc $54\\text{ km/giờ}$ trong 40 phút. Quãng đường đi được là:", ["36 km", "40 km", "30 km", "32 km"], 0, "40 phút = 2/3 giờ. 54 x 2/3 = 36 km."),
            make_mc(3, "Một vận động viên bơi $100\\text{ m}$ hết 1 phút 15 giây. Vận tốc bơi là:", ["$\\frac{4}{3}\\text{ m/giây}$", "$1,5\\text{ m/giây}$", "$1,2\\text{ m/giây}$", "$1,4\\text{ m/giây}$"], 0, "1p 15s = 75 giây. 100 : 75 = 4/3 m/giây."),
            make_mc(4, "Hai ô tô đi cùng chiều từ hai điểm A và B cách nhau $36\\text{ km}$. Vận tốc xe thứ nhất là $54\\text{ km/giờ}$, xe thứ hai là $36\\text{ km/giờ}$. Xe 1 đuổi kịp xe 2 sau:", ["2 giờ", "1,5 giờ", "2,5 giờ", "3 giờ"], 0, "t = 36 : (54 - 36) = 36 : 18 = 2 giờ."),
            make_mc(5, "Vận tốc của một con đại bàng là $90\\text{ km/giờ}$. Trong 20 phút nó bay được:", ["30 km", "45 km", "25 km", "35 km"], 0, "20 phút = 1/3 giờ. 90 x 1/3 = 30 km."),
            make_mc(6, "Một tàu hỏa đi quãng đường $180\\text{ km}$ với vận tốc $60\\text{ km/giờ}$. Tàu khởi hành lúc 8 giờ 15 phút thì đến nơi lúc:", ["11 giờ 15 phút", "11 giờ", "11 giờ 30 phút", "10 giờ 45 phút"], 0, "180 : 60 = 3 giờ. Đến lúc 8h 15p + 3h = 11 giờ 15 phút.")
        ],
        "part2": [
            make_essay(1, "Một người đi xe máy khởi hành từ tỉnh A lúc 7 giờ và đến tỉnh B lúc 9 giờ 45 phút. Biết quãng đường AB dài $110\\text{ km}$. Tính vận tốc của xe máy theo km/giờ.", "Thời gian người đó đi từ A đến B là:\n$9\\text{ giờ } 45\\text{ phút} - 7\\text{ giờ} = 2\\text{ giờ } 45\\text{ phút} = 2,75\\text{ giờ}$.\nVận tốc của xe máy là:\n$110 : 2,75 = 40\\text{ (km/giờ)}$.", "40 km/giờ", 4, 1.0),
            make_essay(2, "Quãng đường AB dài $180\\text{ km}$. Lúc 7 giờ 15 phút, một ô tô đi từ A đến B với vận tốc $52\\text{ km/giờ}$ và cùng lúc đó một ô tô đi từ B về A với vận tốc $48\\text{ km/giờ}$. Hỏi hai xe gặp nhau lúc mấy giờ?", "Tổng vận tốc của hai xe là: $52 + 48 = 100\\text{ (km/giờ)}$.\nThời gian hai xe gặp nhau là: $180 : 100 = 1,8\\text{ (giờ)} = 1\\text{ giờ } 48\\text{ phút}$.\nHai xe gặp nhau lúc:\n$7\\text{ giờ } 15\\text{ phút} + 1\\text{ giờ } 48\\text{ phút} = 8\\text{ giờ } 63\\text{ phút} = 9\\text{ giờ } 3\\text{ phút}$.", "9 giờ 3 phút", 4, 1.0),
            make_essay(3, "Lúc 6 giờ sáng một xe đạp đi từ A với vận tốc $15\\text{ km/giờ}$. Lúc 7 giờ 20 phút một xe máy cũng từ A đuổi theo với vận tốc $35\\text{ km/giờ}$. Hỏi xe máy đuổi kịp xe đạp lúc mấy giờ?", "Thời gian xe đạp đi trước là: $7\\text{ giờ } 20\\text{ phút} - 6\\text{ giờ} = 1\\text{ giờ } 20\\text{ phút} = \\frac{4}{3}\\text{ giờ}$.\nQuãng đường xe đạp đi trước là: $15 \\times \\frac{4}{3} = 20\\text{ (km)}$.\nHiệu vận tốc của hai xe là: $35 - 15 = 20\\text{ (km/giờ)}$.\nThời gian xe máy đuổi kịp xe đạp là: $20 : 20 = 1\\text{ (giờ)}$.\nXe máy đuổi kịp xe đạp lúc: $7\\text{ giờ } 20\\text{ phút} + 1\\text{ giờ} = 8\\text{ giờ } 20\\text{ phút}$.", "8 giờ 20 phút", 4, 1.0),
            make_essay(4, "Một ca nô đi xuôi dòng một khúc sông từ A đến B hết 2 giờ và đi ngược dòng từ B về A hết 2 giờ 30 phút. Biết vận tốc dòng nước là $3\\text{ km/giờ}$. Tính độ dài khúc sông AB.", "Đổi: $2\\text{ giờ } 30\\text{ phút} = 2,5\\text{ giờ}$.\nVận tốc xuôi dòng hơn vận tốc ngược dòng là 2 lần vận tốc dòng nước:\n$v_{\\text{xuôi}} - v_{\\text{ngược}} = 2 \\times 3 = 6\\text{ (km/giờ)}$.\nTỉ số thời gian xuôi và ngược là: $2 : 2,5 = \\frac{4}{5}$.\nDo cùng quãng đường AB nên tỉ số vận tốc xuôi và ngược là $\\frac{5}{4}$.\nVận tốc xuôi dòng là: $6 : (5 - 4) \\times 5 = 30\\text{ (km/giờ)}$.\nĐộ dài khúc sông AB là: $30 \\times 2 = 60\\text{ (km)}$.", "60 km", 5, 1.5),
            make_essay(5, "Hai người cùng xuất phát từ A lúc 7 giờ sáng đi về B. Người thứ nhất đi xe máy với vận tốc $36\\text{ km/giờ}$. Người thứ hai đi ô tô với vận tốc $54\\text{ km/giờ}$. Quãng đường AB dài $108\\text{ km}$. Hỏi người thứ hai đến B trước người thứ nhất bao nhiêu thời gian?", "Thời gian người thứ nhất đi từ A đến B là: $108 : 36 = 3\\text{ (giờ)}$.\nThời gian người thứ hai đi từ A đến B là: $108 : 54 = 2\\text{ (giờ)}$.\nNgười thứ hai đến B trước người thứ nhất số thời gian là:\n$3 - 2 = 1\\text{ (giờ)}$.", "1 giờ", 5, 1.5),
            make_essay(6, "Một người đi xe máy nửa quãng đường đầu với vận tốc $30\\text{ km/giờ}$, nửa quãng đường sau tăng tốc lên $45\\text{ km/giờ}$. Biết cả quãng đường dài $90\\text{ km}$. Tính tổng thời gian người đó đi hết cả quãng đường.", "Độ dài mỗi nửa quãng đường là: $90 : 2 = 45\\text{ (km)}$.\nThời gian đi nửa đầu là: $45 : 30 = 1,5\\text{ (giờ)} = 1\\text{ giờ } 30\\text{ phút}$.\nThời gian đi nửa sau là: $45 : 45 = 1\\text{ (giờ)}$.\nTổng thời gian đi hết quãng đường là: $1,5 + 1 = 2,5\\text{ (giờ)} = 2\\text{ giờ } 30\\text{ phút}$.", "2,5 giờ (hay 2 giờ 30 phút)", 4, 1.0)
        ]
    }

    # --- Bài 59 - Đề 3 ---
    exams["th5_b59_test3"] = {
        "id": "th5_b59_test3",
        "lessonId": "th5_b59",
        "lessonNum": 59,
        "testNum": 3,
        "title": "Bài 59: Ôn tập toán chuyển động đều - Đề số 3",
        "topic": "Ôn tập toán chuyển động đều",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người đi xe đạp đi được $24\\text{ km}$ trong 1 giờ 36 phút. Vận tốc người đi xe đạp là:", ["15 km/giờ", "16 km/giờ", "14 km/giờ", "18 km/giờ"], 0, "1h 36p = 1,6h. 24 : 1,6 = 15 km/giờ."),
            make_mc(2, "Một xe máy đi với vận tốc $37,5\\text{ km/giờ}$ trong 2 giờ 24 phút. Quãng đường đi được là:", ["90 km", "85 km", "95 km", "80 km"], 0, "2h 24p = 2,4h. 37,5 x 2,4 = 90 km."),
            make_mc(3, "Một ô tô chạy quãng đường $168\\text{ km}$ với vận tốc $48\\text{ km/giờ}$. Thời gian ô tô đi là:", ["3,5 giờ", "3,25 giờ", "3,75 giờ", "4 giờ"], 0, "168 : 48 = 3,5 giờ."),
            make_mc(4, "Hai ô tô đi ngược chiều từ hai điểm cách nhau $200\\text{ km}$ với vận tốc $55\\text{ km/giờ}$ và $45\\text{ km/giờ}$. Hai xe gặp nhau sau:", ["2 giờ", "2,5 giờ", "1,8 giờ", "2,2 giờ"], 0, "t = 200 : (55 + 45) = 200 : 100 = 2 giờ."),
            make_mc(5, "Một người đi xe máy đuổi theo xe đạp cách mình $18\\text{ km}$. Vận tốc xe máy là $38\\text{ km/giờ}$, xe đạp là $14\\text{ km/giờ}$. Xe máy đuổi kịp sau:", ["45 phút", "50 phút", "1 giờ", "40 phút"], 0, "t = 18 : (38 - 14) = 18 : 24 = 0,75 giờ = 45 phút."),
            make_mc(6, "Một ca nô có vận tốc khi nước yên lặng là $26\\text{ km/giờ}$, vận tốc dòng nước là $2,5\\text{ km/giờ}$. Vận tốc ngược dòng là:", ["23,5 km/giờ", "28,5 km/giờ", "24 km/giờ", "22,5 km/giờ"], 0, "26 - 2,5 = 23,5 km/giờ.")
        ],
        "part2": [
            make_essay(1, "Một người đi xe đạp quãng đường $30\\text{ km}$ với vận tốc $12\\text{ km/giờ}$. Người đó xuất phát lúc 7 giờ 15 phút. Hỏi người đó đến nơi lúc mấy giờ?", "Thời gian người đó đi là: $30 : 12 = 2,5\\text{ (giờ)} = 2\\text{ giờ } 30\\text{ phút}$.\nNgười đó đến nơi lúc:\n$7\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 30\\text{ phút} = 9\\text{ giờ } 45\\text{ phút}$.", "9 giờ 45 phút", 4, 1.0),
            make_essay(2, "Quãng đường AB dài $165\\text{ km}$. Lúc 7 giờ 30 phút, một ô tô đi từ A đến B với vận tốc $50\\text{ km/giờ}$ và một xe máy đi từ B về A với vận tốc $32,5\\text{ km/giờ}$? (hoặc tổng vận tốc = 55 km/h)", "Tổng vận tốc của hai xe là: $50 + 32,5 = 82,5\\text{ (km/giờ)}$.\nThời gian hai xe gặp nhau là: $165 : 82,5 = 2\\text{ (giờ)}$.\nHai xe gặp nhau lúc: $7\\text{ giờ } 30\\text{ phút} + 2\\text{ giờ} = 9\\text{ giờ } 30\\text{ phút}$.", "9 giờ 30 phút", 4, 1.0),
            make_essay(3, "Lúc 8 giờ một người đi xe máy từ A với vận tốc $36\\text{ km/giờ}$. Đến 9 giờ một ô tô cũng từ A đuổi theo với vận tốc $54\\text{ km/giờ}$. Hỏi ô tô đuổi kịp xe máy lúc mấy giờ?", "Thời gian xe máy đi trước là: $9 - 8 = 1\\text{ (giờ)}$.\nQuãng đường xe máy đi trước là: $36 \\times 1 = 36\\text{ (km)}$.\nHiệu vận tốc hai xe là: $54 - 36 = 18\\text{ (km/giờ)}$.\nThời gian ô tô đuổi kịp xe máy là: $36 : 18 = 2\\text{ (giờ)}$.\nÔ tô đuổi kịp lúc: $9\\text{ giờ} + 2\\text{ giờ} = 11\\text{ giờ}$.", "11 giờ đúng", 4, 1.0),
            make_essay(4, "Một ca nô đi xuôi dòng một khúc sông từ A đến B dài $48\\text{ km}$ hết 1,6 giờ. Biết vận tốc dòng nước là $2,5\\text{ km/giờ}$. Hỏi ca nô đi ngược dòng từ B về A hết bao nhiêu thời gian?", "Vận tốc xuôi dòng là: $48 : 1,6 = 30\\text{ (km/giờ)}$.\nVận tốc thực của ca nô là: $30 - 2,5 = 27,5\\text{ (km/giờ)}$.\nVận tốc ngược dòng của ca nô là: $27,5 - 2,5 = 25\\text{ (km/giờ)}$.\nThời gian ca nô đi ngược dòng từ B về A là:\n$48 : 25 = 1,92\\text{ (giờ)} = 1\\text{ giờ } 55\\text{ phút } 12\\text{ giây}$.", "1,92 giờ (hay 1 giờ 55 phút 12 giây)", 5, 1.5),
            make_essay(5, "Một đoàn tàu hỏa dài $150\\text{ m}$ vượt qua một người đi bộ ngược chiều với vận tốc $3,6\\text{ km/giờ}$ trong 10 giây. Tính vận tốc của đoàn tàu hỏa theo đơn vị km/giờ.", "Đổi: $3,6\\text{ km/giờ} = 1\\text{ m/giây}$.\nTổng vận tốc của tàu hỏa và người đi bộ ngược chiều là:\n$150 : 10 = 15\\text{ (m/giây)}$.\nVận tốc thực của đoàn tàu hỏa là:\n$15 - 1 = 14\\text{ (m/giây)}$.\nĐổi sang km/giờ: $14 \\times 3,6 = 50,4\\text{ (km/giờ)}$.", "50,4 km/giờ", 5, 1.5),
            make_essay(6, "Bác An đi bộ một vòng quanh hồ hết 30 phút với vận tốc $4,8\\text{ km/giờ}$. Bác Ba đi xe đạp một vòng quanh hồ đó với vận tốc $12\\text{ km/giờ}$. Hỏi bác Ba đi một vòng quanh hồ hết bao nhiêu phút?", "Đổi: $30\\text{ phút} = 0,5\\text{ giờ}$.\nChu vi hồ nước (độ dài 1 vòng) là: $4,8 \\times 0,5 = 2,4\\text{ (km)}$.\nThời gian bác Ba đi một vòng là:\n$2,4 : 12 = 0,2\\text{ (giờ)} = 12\\text{ phút}$.", "12 phút", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 60: ÔN TẬP CHUNG TOÀN DIỆN
    # =========================================================================
    # --- Bài 60 - Đề 1 ---
    exams["th5_b60_test1"] = {
        "id": "th5_b60_test1",
        "lessonId": "th5_b60",
        "lessonNum": 60,
        "testNum": 1,
        "title": "Bài 60: Ôn tập chung toàn diện - Đề số 1",
        "topic": "Ôn tập chung toàn diện",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của biểu thức $4,5 \\times 2,4 + 5,5 \\times 2,4$ là:", ["24", "2,4", "240", "12"], 0, "(4,5 + 5,5) x 2,4 = 10 x 2,4 = 24."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $3,5\\text{ giờ} = \\dots \\text{ giờ } \\dots \\text{ phút}$ là:", ["3 giờ 30 phút", "3 giờ 50 phút", "3 giờ 5 phút", "3 giờ 15 phút"], 0, "0,5 x 60 = 30 phút => 3 giờ 30 phút."),
            make_mc(3, "Một mảnh đất hình thang có đáy lớn $18\\text{ m}$, đáy bé $12\\text{ m}$ và chiều cao $8\\text{ m}$. Diện tích mảnh đất là:", ["$120\\text{ m}^2$", "$240\\text{ m}^2$", "$144\\text{ m}^2$", "$150\\text{ m}^2$"], 0, "(18 + 12) x 8 : 2 = 120 m$^2$."),
            make_mc(4, "Một ô tô đi với vận tốc $50\\text{ km/giờ}$ trong 2 giờ 15 phút. Quãng đường đi được là:", ["112,5 km", "100 km", "110 km", "120 km"], 0, "2h 15p = 2,25h. 50 x 2,25 = 112,5 km."),
            make_mc(5, "Tỉ số phần trăm của 15 và 60 là:", ["25%", "20%", "30%", "15%"], 0, "15 : 60 = 0,25 = 25%."),
            make_mc(6, "Diện tích toàn phần của hình lập phương có cạnh $5\\text{ dm}$ là:", ["$150\\text{ dm}^2$", "$100\\text{ dm}^2$", "$125\\text{ dm}^2$", "$25\\text{ dm}^2$"], 0, "5 x 5 x 6 = 150 dm$^2$.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của biểu thức:\n$A = 12,5 \\times 3,8 + 12,5 \\times 6,2 - 25$", "$A = 12,5 \\times (3,8 + 6,2) - 25$\n$A = 12,5 \\times 10 - 25 = 125 - 25 = 100$.", "A = 100", 4, 1.0),
            make_essay(2, "Tìm $x$, biết: $x : 2,4 = 15,6 - 6,8$.", "$x : 2,4 = 8,8$\n$x = 8,8 \\times 2,4 = 21,12$.", "x = 21,12", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chu vi $120\\text{ m}$, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Người ta dùng $25\\%$ diện tích mảnh vườn để làm nhà. Tính diện tích phần đất làm nhà.", "Nửa chu vi mảnh vườn là: $120 : 2 = 60\\text{ (m)}$.\nTổng số phần bằng nhau: $2 + 3 = 5$ (phần).\nChiều dài mảnh vườn: $60 : 5 \\times 3 = 36\\text{ (m)}$.\nChiều rộng mảnh vườn: $60 - 36 = 24\\text{ (m)}$.\nDiện tích mảnh vườn: $36 \\times 24 = 864\\text{ (m$^2$)}$.\nDiện tích làm nhà là: $864 \\times 25 : 100 = 216\\text{ (m$^2$)}$.", "216 m$^2$", 4, 1.0),
            make_essay(4, "Một ô tô khởi hành từ A lúc 7 giờ sáng và đến B lúc 10 giờ 30 phút cùng ngày. Giữa đường ô tô nghỉ giải lao 30 phút. Biết vận tốc của ô tô là $48\\text{ km/giờ}$.\na) Tính độ dài quãng đường AB.\nb) Nếu lúc về ô tô đi với vận tốc $60\\text{ km/giờ}$ và không nghỉ dọc đường thì ô tô đi hết bao nhiêu thời gian?", "a) Thời gian thực tế đi từ A đến B là:\n$10\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} - 30\\text{ phút} = 3\\text{ giờ}$.\nQuãng đường AB dài là: $48 \\times 3 = 144\\text{ (km)}$.\nb) Thời gian đi từ B về A là:\n$144 : 60 = 2,4\\text{ (giờ)} = 2\\text{ giờ } 24\\text{ phút}$.", "a) 144 km; b) 2 giờ 24 phút", 5, 1.5),
            make_essay(5, "Một bể nước dạng hình hộp chữ nhật có kích thước dài $2\\text{ m}$, rộng $1,5\\text{ m}$ và cao $1,2\\text{ m}$. Hiện tại bể đang chứa $1 800\\text{ lít}$ nước. Người ta mở một vòi nước chảy vào bể mỗi phút được 25 lít nước. Hỏi sau bao lâu thì bể đầy nước?", "Thể tích toàn phần của bể là: $2 \\times 1,5 \\times 1,2 = 3,6\\text{ (m$^3$)} = 3 600\\text{ dm$^3$} = 3 600\\text{ lít}$.\nLượng nước cần chảy thêm để đầy bể là: $3 600 - 1 800 = 1 800\\text{ (lít)}$.\nThời gian để vòi chảy đầy bể là: $1 800 : 25 = 72\\text{ (phút)} = 1\\text{ giờ } 12\\text{ phút}$.", "72 phút (hay 1 giờ 12 phút)", 5, 1.5),
            make_essay(6, "Biểu đồ quạt tròn cho biết tỉ lệ tham gia phong trào thể dục thể thao của 400 học sinh: Bóng đá chiếm 40%, Cầu lông chiếm 30%, Bơi lội chiếm 20%, còn lại là Cờ vua. Hỏi có bao nhiêu học sinh tham gia môn Cờ vua?", "Tỉ lệ phần trăm học sinh tham gia Cờ vua là: $100\\% - (40\\% + 30\\% + 20\\%) = 10\\%$.\nSố học sinh tham gia Cờ vua là:\n$400 \\times 10 : 100 = 40$ (học sinh).", "40 học sinh", 4, 1.0)
        ]
    }

    # --- Bài 60 - Đề 2 ---
    exams["th5_b60_test2"] = {
        "id": "th5_b60_test2",
        "lessonId": "th5_b60",
        "lessonNum": 60,
        "testNum": 2,
        "title": "Bài 60: Ôn tập chung toàn diện - Đề số 2",
        "topic": "Ôn tập chung toàn diện",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $38,5 \\times 0,01$ là:", ["0,385", "3,85", "385", "0,0385"], 0, "Dịch sang trái 2 chữ số: 0,385."),
            make_mc(2, "Một hình tròn có bán kính $r = 4\\text{ cm}$. Diện tích hình tròn đó là:", ["$50,24\\text{ cm}^2$", "$25,12\\text{ cm}^2$", "$12,56\\text{ cm}^2$", "$16\\text{ cm}^2$"], 0, "4 x 4 x 3,14 = 50,24 cm$^2$."),
            make_mc(3, "Một ô tô đi được quãng đường $168\\text{ km}$ trong 3,5 giờ. Vận tốc ô tô là:", ["48 km/giờ", "45 km/giờ", "50 km/giờ", "52 km/giờ"], 0, "168 : 3,5 = 48 km/giờ."),
            make_mc(4, "Tính: $3\\text{ giờ } 45\\text{ phút} + 2\\text{ giờ } 30\\text{ phút}$ bằng:", ["6 giờ 15 phút", "5 giờ 75 phút", "6 giờ 25 phút", "5 giờ 15 phút"], 0, "5h 75p = 6 giờ 15 phút."),
            make_mc(5, "Thể tích của một hình lập phương có diện tích một mặt là $16\\text{ cm}^2$ là:", ["$64\\text{ cm}^3$", "$32\\text{ cm}^3$", "$48\\text{ cm}^3$", "$96\\text{ cm}^3$"], 0, "Cạnh = 4 cm. V = 4 x 4 x 4 = 64 cm$^3$."),
            make_mc(6, "Biết 25% của một số là 40. Số đó là:", ["160", "100", "80", "120"], 0, "40 : 25 x 100 = 160.")
        ],
        "part2": [
            make_essay(1, "Tính bằng cách thuận tiện nhất:\n$B = 3,45 \\times 8,7 + 3,45 \\times 1,3$", "$B = 3,45 \\times (8,7 + 1,3) = 3,45 \\times 10 = 34,5$.", "B = 34,5", 4, 1.0),
            make_essay(2, "Tìm $y$, biết: $y - 3,75 = 12,8 : 4$.", "$y - 3,75 = 3,2$\n$y = 3,2 + 3,75 = 6,95$.", "y = 6,95", 4, 1.0),
            make_essay(3, "Một thửa ruộng hình thang có đáy lớn $40\\text{ m}$, đáy bé $30\\text{ m}$ và chiều cao $25\\text{ m}$. Cứ $100\\text{ m}^2$ thu hoạch được $60\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Diện tích thửa ruộng hình thang là: $(40 + 30) \\times 25 : 2 = 875\\text{ (m$^2$)}$.\nKhối lượng thóc thu hoạch được là: $875 : 100 \\times 60 = 525\\text{ (kg)}$.\nĐổi sang tạ: $525\\text{ kg} = 5,25\\text{ tạ thóc}$.", "5,25 tạ thóc", 4, 1.0),
            make_essay(4, "Hai thành phố A và B cách nhau $175\\text{ km}$. Cùng lúc 7 giờ sáng, một ô tô đi từ A đến B với vận tốc $55\\text{ km/giờ}$ và một xe máy đi từ B về A với vận tốc $45\\text{ km/giờ}$. Hỏi hai xe gặp nhau lúc mấy giờ và điểm gặp nhau cách A bao nhiêu ki-lô-mét?", "Tổng vận tốc hai xe: $55 + 45 = 100\\text{ (km/giờ)}$.\nThời gian hai xe gặp nhau: $175 : 100 = 1,75\\text{ (giờ)} = 1\\text{ giờ } 45\\text{ phút}$.\nHai xe gặp nhau lúc: $7\\text{ giờ} + 1\\text{ giờ } 45\\text{ phút} = 8\\text{ giờ } 45\\text{ phút}$.\nĐiểm gặp nhau cách A: $55 \\times 1,75 = 96,25\\text{ (km)}$.", "Gặp nhau lúc 8 giờ 45 phút; Cách A: 96,25 km", 5, 1.5),
            make_essay(5, "Một người thợ quét sơn một cái thùng sắt không có nắp dạng hình hộp chữ nhật dài $1,5\\text{ m}$, rộng $0,8\\text{ m}$ và cao $0,6\\text{ m}$.\na) Tính diện tích cần quét sơn (cả bên trong và bên ngoài thùng, không kể mép hàn).\nb) Biết tiền sơn mỗi mét vuông là 35 000 đồng. Hỏi người đó tốn bao nhiêu tiền sơn?", "a) Diện tích quét sơn 1 mặt (không nắp):\nDiện tích đáy: $1,5 \\times 0,8 = 1,2\\text{ (m$^2$)}$.\nDiện tích xung quanh: $(1,5 + 0,8) \\times 2 \\times 0,6 = 2,76\\text{ (m$^2$)}$.\nDiện tích 1 mặt: $1,2 + 2,76 = 3,96\\text{ (m$^2$)}$.\nDiện tích sơn cả trong và ngoài là: $3,96 \\times 2 = 7,92\\text{ (m$^2$)}$.\nb) Số tiền sơn là: $7,92 \\times 35 000 = 277 200$ (đồng).", "a) 7,92 m$^2$; b) 277 200 đồng", 5, 1.5),
            make_essay(6, "Gieo một con xúc xắc 50 lần, ghi nhận được mặt 6 chấm xuất hiện 8 lần. Hãy viết tỉ số mô tả số lần xuất hiện mặt 6 chấm dưới dạng phân số tối giản và tỉ số phần trăm.", "Tỉ số xuất hiện mặt 6 chấm là: $\\frac{8}{50}$.\n- Phân số tối giản: $\\frac{8 : 2}{50 : 2} = \\frac{4}{25}$.\n- Tỉ số phần trăm: $\\frac{4 \\times 4}{25 \\times 4} = 16\\%$.", "4/25 (hay 16%)", 4, 1.0)
        ]
    }

    # --- Bài 60 - Đề 3 ---
    exams["th5_b60_test3"] = {
        "id": "th5_b60_test3",
        "lessonId": "th5_b60",
        "lessonNum": 60,
        "testNum": 3,
        "title": "Bài 60: Ôn tập chung toàn diện - Đề số 3",
        "topic": "Ôn tập chung toàn diện",
        "chapter": "Chủ đề 11: Ôn tập cuối năm",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân $0,25 \\times 36 \\times 40$ là:", ["360", "36", "3 600", "180"], 0, "(0,25 x 40) x 36 = 10 x 36 = 360."),
            make_mc(2, "Chu vi hình tròn có đường kính $d = 8\\text{ cm}$ là:", ["$25,12\\text{ cm}$", "$50,24\\text{ cm}$", "$12,56\\text{ cm}$", "$16\\text{ cm}$"], 0, "8 x 3,14 = 25,12 cm."),
            make_mc(3, "Một ô tô đi quãng đường $135\\text{ km}$ với vận tốc $45\\text{ km/giờ}$. Thời gian ô tô đi là:", ["3 giờ", "2,5 giờ", "3,5 giờ", "2,75 giờ"], 0, "135 : 45 = 3 giờ."),
            make_mc(4, "Đổi $4,5\\text{ m}^3 = \\dots \\text{ dm}^3$:", ["4 500 dm$^3$", "450 dm$^3$", "45 000 dm$^3$", "45 dm$^3$"], 0, "4,5 x 1000 = 4 500 dm$^3$."),
            make_mc(5, "Một người làm 3 sản phẩm hết 45 phút. Làm 8 sản phẩm như thế hết:", ["2 giờ", "1 giờ 45 phút", "2 giờ 15 phút", "1,5 giờ"], 0, "1 sản phẩm = 15 phút. 8 x 15 = 120 phút = 2 giờ."),
            make_mc(6, "Biết tổng hai số là 72 và số lớn gấp 3 lần số bé. Số bé là:", ["18", "24", "16", "20"], 0, "72 : (1 + 3) = 18.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\n$C = 4\\frac{1}{2} + 2\\frac{1}{4} \\times \\frac{4}{3}$", "$2\\frac{1}{4} \\times \\frac{4}{3} = \\frac{9}{4} \\times \\frac{4}{3} = 3$.\n$C = 4\\frac{1}{2} + 3 = 7\\frac{1}{2} = 7,5$.", "C = 7 1/2 (hoặc 7,5)", 4, 1.0),
            make_essay(2, "Tìm $x$, biết: $x \\times 3,5 = 15,4 - 4,9$.", "$x \\times 3,5 = 10,5$\n$x = 10,5 : 3,5 = 3$.", "x = 3", 4, 1.0),
            make_essay(3, "Một khu đất hình chữ nhật có chu vi $180\\text{ m}$, chiều rộng bằng $\\frac{4}{5}$ chiều dài. Tính diện tích khu đất đó theo đơn vị mét vuông và theo héc-ta.", "Nửa chu vi là: $180 : 2 = 90\\text{ (m)}$.\nTổng số phần bằng nhau: $4 + 5 = 9$ (phần).\nChiều dài khu đất: $90 : 9 \\times 5 = 50\\text{ (m)}$.\nChiều rộng khu đất: $90 - 50 = 40\\text{ (m)}$.\nDiện tích khu đất: $50 \\times 40 = 2 000\\text{ (m$^2$)}$.\nĐổi sang héc-ta: $2 000 : 10 000 = 0,2\\text{ (ha)}$.", "2 000 m$^2$ = 0,2 ha", 4, 1.0),
            make_essay(4, "Một người đi xe máy từ A lúc 7 giờ với vận tốc $36\\text{ km/giờ}$. Đến 8 giờ 30 phút một ô tô từ A đuổi theo với vận tốc $54\\text{ km/giờ}$. Hỏi ô tô đuổi kịp xe máy lúc mấy giờ và điểm gặp nhau cách A bao nhiêu ki-lô-mét?", "Thời gian xe máy đi trước: $8\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} = 1,5\\text{ giờ}$.\nQuãng đường xe máy đi trước: $36 \\times 1,5 = 54\\text{ (km)}$.\nHiệu vận tốc: $54 - 36 = 18\\text{ (km/giờ)}$.\nThời gian để ô tô đuổi kịp: $54 : 18 = 3\\text{ (giờ)}$.\nÔ tô đuổi kịp lúc: $8\\text{ giờ } 30\\text{ phút} + 3\\text{ giờ} = 11\\text{ giờ } 30\\text{ phút}$.\nChỗ gặp nhau cách A là: $54 \\times 3 = 162\\text{ (km)}$.", "Gặp nhau lúc 11 giờ 30 phút; Cách A: 162 km", 5, 1.5),
            make_essay(5, "Một cái bể nước hình hộp chữ nhật có kích thước lòng bể là: chiều dài $1,8\\text{ m}$, chiều rộng $1,2\\text{ m}$ và chiều cao $1\\text{ m}$. Hiện tại bể đang cạn. Người ta mở một vòi nước chảy vào bể mỗi phút được 30 lít. Hỏi sau bao lâu vòi nước chảy được $\\frac{4}{5}$ thể tích của bể?", "Thể tích toàn phần của bể là: $1,8 \\times 1,2 \\times 1 = 2,16\\text{ (m$^3$)} = 2 160\\text{ lít}$.\nThể tích nước bằng $\\frac{4}{5}$ bể là: $2 160 \\times \\frac{4}{5} = 1 728\\text{ (lít)}$.\nThời gian để vòi chảy được $\\frac{4}{5}$ bể là: $1 728 : 30 = 57,6\\text{ (phút)} = 57\\text{ phút } 36\\text{ giây}$.", "57,6 phút (hay 57 phút 36 giây)", 5, 1.5),
            make_essay(6, "Biểu đồ quạt tròn cho biết cơ cấu số học sinh xuất sắc của 4 lớp khối 5: Lớp 5A chiếm 30%, lớp 5B chiếm 28%, lớp 5C chiếm 22%, còn lại là lớp 5D có 8 học sinh xuất sắc. Hỏi cả khối 5 có tất cả bao nhiêu học sinh xuất sắc?", "Tỉ lệ phần trăm học sinh xuất sắc của lớp 5D là:\n$100\\% - (30\\% + 28\\% + 22\\%) = 20\\%$.\nTổng số học sinh xuất sắc của cả khối 5 là:\n$8 : 20 \\times 100 = 40$ (học sinh).", "40 học sinh xuất sắc", 4, 1.0)
        ]
    }

    return exams
