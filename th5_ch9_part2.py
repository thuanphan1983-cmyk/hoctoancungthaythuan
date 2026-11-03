# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 9: SỐ ĐO THỜI GIAN. VẬN TỐC, QUÃNG ĐƯỜNG, THỜI GIAN (PHẦN 2: BÀI 49 ĐẾN BÀI 52)
Toán lớp 5 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 4 bài học x 3 đề độc lập = 12 đề thi (th5_b49_test1 -> th5_b52_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from th5_ch9_part1 import make_mc, make_essay

def get_ch9_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 49: QUÃNG ĐƯỜNG
    # =========================================================================
    # --- Bài 49 - Đề 1 ---
    exams["th5_b49_test1"] = {
        "id": "th5_b49_test1",
        "lessonId": "th5_b49",
        "lessonNum": 49,
        "testNum": 1,
        "title": "Bài 49: Quãng đường - Đề số 1",
        "topic": "Quãng đường",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn tính quãng đường ta lấy:", [
                "Vận tốc nhân với thời gian",
                "Vận tốc chia cho thời gian",
                "Thời gian chia cho vận tốc",
                "Vận tốc cộng với thời gian"
            ], 0, "Công thức tính quãng đường là: s = v x t."),
            make_mc(2, "Một ô tô đi với vận tốc $45\\text{ km/giờ}$ trong 2,4 giờ. Quãng đường ô tô đi được là:", ["108 km", "90 km", "100 km", "112,5 km"], 0, "s = 45 x 2,4 = 108 km."),
            make_mc(3, "Một người đi bộ với vận tốc $4,8\\text{ km/giờ}$ trong 15 phút. Quãng đường người đó đi được là:", ["1,2 km", "72 km", "1,5 km", "0,8 km"], 0, "15 phút = 0,25 giờ. s = 4,8 x 0,25 = 1,2 km."),
            make_mc(4, "Một con đà điểu chạy với vận tốc $1 050\\text{ m/phút}$ trong 4 phút. Quãng đường đà điểu chạy được là:", ["4 200 m", "4 000 m", "4 150 m", "4 500 m"], 0, "1050 x 4 = 4200 m."),
            make_mc(5, "Một máy bay bay với vận tốc $850\\text{ km/giờ}$ trong 2 giờ 30 phút. Quãng đường máy bay bay được là:", ["2 125 km", "1 700 km", "2 000 km", "2 550 km"], 0, "2h 30p = 2,5h. s = 850 x 2,5 = 2125 km."),
            make_mc(6, "Một người đi xe máy khởi hành từ A lúc 8 giờ 15 phút và đến B lúc 10 giờ 45 phút với vận tốc $36\\text{ km/giờ}$. Quãng đường AB dài là:", ["90 km", "85 km", "96 km", "72 km"], 0, "t = 2h 30p = 2,5h. s = 36 x 2,5 = 90 km.")
        ],
        "part2": [
            make_essay(1, "Một người đi xe máy với vận tốc $38,5\\text{ km/giờ}$ trong 2 giờ 12 phút. Tính độ dài quãng đường người đó đi được.", "Đổi: $2\\text{ giờ } 12\\text{ phút} = 2,2\\text{ giờ}$.\nQuãng đường người đó đi được là:\n$38,5 \\times 2,2 = 84,7\\text{ (km)}$.", "84,7 km", 4, 1.0),
            make_essay(2, "Một xe lửa đi từ A lúc 6 giờ 45 phút và đến B lúc 9 giờ 15 phút. Biết vận tốc của xe lửa là $48\\text{ km/giờ}$. Tính khoảng cách từ A đến B.", "Thời gian xe lửa đi từ A đến B là:\n$9\\text{ giờ } 15\\text{ phút} - 6\\text{ giờ } 45\\text{ phút} = 2\\text{ giờ } 30\\text{ phút} = 2,5\\text{ giờ}$.\nQuãng đường AB dài là:\n$48 \\times 2,5 = 120\\text{ (km)}$.", "120 km", 4, 1.0),
            make_essay(3, "Một con rái cá có thể bơi với vận tốc $420\\text{ m/phút}$. Hỏi con rái cá đó bơi quãng đường dài bao nhiêu ki-lô-mét trong 25 phút?", "Quãng đường rái cá bơi được là:\n$420 \\times 25 = 10 500\\text{ (m)}$.\nĐổi sang ki-lô-mét: $10 500\\text{ m} = 10,5\\text{ km}$.", "10,5 km", 4, 1.0),
            make_essay(4, "Một ô tô khởi hành từ Hà Nội lúc 7 giờ sáng để đi Thanh Hóa. Vận tốc ô tô là $55\\text{ km/giờ}$. Giữa đường ô tô nghỉ ăn sáng 30 phút và đến Thanh Hóa lúc 10 giờ 30 phút trưa. Tính quãng đường từ Hà Nội đến Thanh Hóa.", "Tổng thời gian từ khi đi đến khi tới nơi là:\n$10\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} = 3\\text{ giờ } 30\\text{ phút}$.\nThời gian thực tế ô tô chạy trên đường là:\n$3\\text{ giờ } 30\\text{ phút} - 30\\text{ phút} = 3\\text{ giờ}$.\nQuãng đường từ Hà Nội đến Thanh Hóa là:\n$55 \\times 3 = 165\\text{ (km)}$.", "165 km", 5, 1.5),
            make_essay(5, "Một người đi xe đạp từ A đến B. Nửa quãng đường đầu người đó đi với vận tốc $12\\text{ km/giờ}$ hết 1 giờ 30 phút. Nửa quãng đường sau người đó tăng tốc đi với vận tốc $15\\text{ km/giờ}$. Tính độ dài quãng đường AB và thời gian người đó đi hết nửa quãng đường sau.", "Đổi: $1\\text{ giờ } 30\\text{ phút} = 1,5\\text{ giờ}$.\nĐộ dài nửa quãng đường đầu là:\n$12 \\times 1,5 = 18\\text{ (km)}$.\nĐộ dài quãng đường AB là:\n$18 \\times 2 = 36\\text{ (km)}$.\nThời gian đi nửa quãng đường sau là:\n$18 : 15 = 1,2\\text{ (giờ)} = 1\\text{ giờ } 12\\text{ phút}$.", "AB dài 36 km; Thời gian sau: 1 giờ 12 phút", 5, 1.5),
            make_essay(6, "Bác An đi bộ tập thể dục mỗi buổi sáng trong 40 phút với vận tốc $4,5\\text{ km/giờ}$. Hỏi trong 1 tuần (7 ngày) bác An đi bộ được bao nhiêu ki-lô-mét?", "Đổi: $40\\text{ phút} = \\frac{40}{60}\\text{ giờ} = \\frac{2}{3}\\text{ giờ}$.\nQuãng đường bác An đi trong 1 buổi sáng là:\n$4,5 \\times \\frac{2}{3} = 3\\text{ (km)}$.\nTrong 1 tuần (7 ngày) bác An đi được là:\n$3 \\times 7 = 21\\text{ (km)}$.", "21 km", 4, 1.0)
        ]
    }

    # --- Bài 49 - Đề 2 ---
    exams["th5_b49_test2"] = {
        "id": "th5_b49_test2",
        "lessonId": "th5_b49",
        "lessonNum": 49,
        "testNum": 2,
        "title": "Bài 49: Quãng đường - Đề số 2",
        "topic": "Quãng đường",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người đi xe máy với vận tốc $40\\text{ km/giờ}$ trong 1 giờ 45 phút. Quãng đường đi được là:", ["70 km", "60 km", "75 km", "65 km"], 0, "1h 45p = 1,75h. s = 40 x 1,75 = 70 km."),
            make_mc(2, "Một ô tô chạy với vận tốc $54\\text{ km/giờ}$. Quãng đường ô tô chạy được trong 20 phút là:", ["18 km", "27 km", "15 km", "20 km"], 0, "20 phút = 1/3 giờ. s = 54 x 1/3 = 18 km."),
            make_mc(3, "Một vận động viên bơi với vận tốc $1,5\\text{ m/giây}$ trong 1 phút 20 giây. Quãng đường bơi được là:", ["120 m", "100 m", "80 m", "150 m"], 0, "1p 20s = 80 giây. s = 1,5 x 80 = 120 m."),
            make_mc(4, "Một chú chim hải âu bay với vận tốc $60\\text{ km/giờ}$ liên tục trong 3,5 giờ. Quãng đường chim bay được là:", ["210 km", "180 km", "200 km", "240 km"], 0, "60 x 3,5 = 210 km."),
            make_mc(5, "Một tàu hỏa đi với vận tốc $65\\text{ km/giờ}$ trong 2 giờ 12 phút. Quãng đường tàu hỏa đi được là:", ["143 km", "130 km", "150 km", "138 km"], 0, "2h 12p = 2,2h. s = 65 x 2,2 = 143 km."),
            make_mc(6, "Bác Ba đi xe đạp từ quê lên thành phố với vận tốc $14\\text{ km/giờ}$ mất 2 giờ 30 phút. Khoảng cách từ quê lên thành phố là:", ["35 km", "28 km", "32 km", "40 km"], 0, "14 x 2,5 = 35 km.")
        ],
        "part2": [
            make_essay(1, "Một ô tô đi từ A lúc 7 giờ 30 phút và đến B lúc 10 giờ 15 phút với vận tốc $48\\text{ km/giờ}$. Tính quãng đường AB.", "Thời gian ô tô đi từ A đến B là:\n$10\\text{ giờ } 15\\text{ phút} - 7\\text{ giờ } 30\\text{ phút} = 2\\text{ giờ } 45\\text{ phút} = 2,75\\text{ giờ}$.\nQuãng đường AB dài là:\n$48 \\times 2,75 = 132\\text{ (km)}$.", "132 km", 4, 1.0),
            make_essay(2, "Một người đi bộ với vận tốc $4,2\\text{ km/giờ}$ trong 1 giờ 20 phút. Tính độ dài quãng đường người đó đi được theo đơn vị mét.", "Đổi: $1\\text{ giờ } 20\\text{ phút} = \\frac{4}{3}\\text{ giờ}$.\nQuãng đường người đó đi được là:\n$4,2 \\times \\frac{4}{3} = 5,6\\text{ (km)}$.\nĐổi sang mét: $5,6\\text{ km} = 5 600\\text{ m}$.", "5 600 m", 4, 1.0),
            make_essay(3, "Một con cá kình có thể bơi với vận tốc $50\\text{ km/giờ}$. Hỏi nếu bơi liên tục trong 45 phút thì con cá kình bơi được bao nhiêu ki-lô-mét?", "Đổi: $45\\text{ phút} = 0,75\\text{ giờ}$.\nQuãng đường cá kình bơi được là:\n$50 \\times 0,75 = 37,5\\text{ (km)}$.", "37,5 km", 4, 1.0),
            make_essay(4, "Một người đi xe máy từ tỉnh A sang tỉnh B. Giờ thứ nhất người đó đi được với vận tốc $36\\text{ km/giờ}$. Trong 1,5 giờ tiếp theo người đó tăng vận tốc lên $42\\text{ km/giờ}$ thì tới B. Tính khoảng cách giữa hai tỉnh A và B.", "Quãng đường người đó đi trong giờ thứ nhất là:\n$36 \\times 1 = 36\\text{ (km)}$.\nQuãng đường người đó đi trong 1,5 giờ tiếp theo là:\n$42 \\times 1,5 = 63\\text{ (km)}$.\nKhoảng cách giữa hai tỉnh A và B là:\n$36 + 63 = 99\\text{ (km)}$.", "99 km", 5, 1.5),
            make_essay(5, "Một ô tô tải đi từ kho A đến kho B hết 3 giờ với vận tốc $40\\text{ km/giờ}$. Một ô tô con cũng đi từ kho A đến kho B với vận tốc $60\\text{ km/giờ}$. Hỏi ô tô con đến kho B sớm hơn ô tô tải bao nhiêu thời gian?", "Khoảng cách giữa hai kho A và B là:\n$40 \\times 3 = 120\\text{ (km)}$.\nThời gian ô tô con đi từ A đến B là:\n$120 : 60 = 2\\text{ (giờ)}$.\nÔ tô con đến kho B sớm hơn ô tô tải số thời gian là:\n$3 - 2 = 1\\text{ (giờ)}$.", "1 giờ", 5, 1.5),
            make_essay(6, "Một người đi xe đạp vòng quanh một hồ nước hình tròn trong 18 phút với vận tốc $12\\text{ km/giờ}$. Tính chu vi hồ nước đó theo đơn vị mét.", "Đổi: $18\\text{ phút} = 0,3\\text{ giờ}$.\nChu vi của hồ nước chính là quãng đường đi hết 1 vòng:\n$s = 12 \\times 0,3 = 3,6\\text{ (km)}$.\nĐổi sang mét: $3,6\\text{ km} = 3 600\\text{ m}$.", "3 600 m", 4, 1.0)
        ]
    }

    # --- Bài 49 - Đề 3 ---
    exams["th5_b49_test3"] = {
        "id": "th5_b49_test3",
        "lessonId": "th5_b49",
        "lessonNum": 49,
        "testNum": 3,
        "title": "Bài 49: Quãng đường - Đề số 3",
        "topic": "Quãng đường",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người đi xe máy với vận tốc $42\\text{ km/giờ}$ trong 2,5 giờ. Quãng đường đi được là:", ["105 km", "100 km", "110 km", "95 km"], 0, "42 x 2,5 = 105 km."),
            make_mc(2, "Một xe đạp đi với vận tốc $15\\text{ km/giờ}$ trong 24 phút. Quãng đường xe đạp đi được là:", ["6 km", "5 km", "7,5 km", "8 km"], 0, "24 phút = 0,4 giờ. s = 15 x 0,4 = 6 km."),
            make_mc(3, "Một chú ốc sên bò với vận tốc $15\\text{ cm/phút}$ trong 2 giờ. Quãng đường ốc sên bò được là:", ["1 800 cm", "30 cm", "300 cm", "18 m"], 0, "2 giờ = 120 phút. 15 x 120 = 1800 cm (hay 18 m)."),
            make_mc(4, "Một ca nô chạy với vận tốc $28\\text{ km/giờ}$ trong 1 giờ 15 phút. Quãng đường ca nô chạy được là:", ["35 km", "30 km", "32 km", "40 km"], 0, "1h 15p = 1,25h. s = 28 x 1,25 = 35 km."),
            make_mc(5, "Vận tốc ánh sáng khoảng $300 000\\text{ km/giây}$. Quãng đường ánh sáng truyền đi trong 1 phút là:", ["18 000 000 km", "300 000 km", "1 800 000 km", "180 000 000 km"], 0, "1 phút = 60 giây. 300 000 x 60 = 18 000 000 km."),
            make_mc(6, "Một người đi bộ trong 1,2 giờ với vận tốc $4,5\\text{ km/giờ}$. Quãng đường người đó đi được là:", ["5,4 km", "5,2 km", "6 km", "4,8 km"], 0, "4,5 x 1,2 = 5,4 km.")
        ],
        "part2": [
            make_essay(1, "Một xe máy đi với vận tốc $37,5\\text{ km/giờ}$ trong 2 giờ 24 phút. Tính độ dài quãng đường xe máy đi được.", "Đổi: $2\\text{ giờ } 24\\text{ phút} = 2,4\\text{ giờ}$.\nQuãng đường xe máy đi được là:\n$37,5 \\times 2,4 = 90\\text{ (km)}$.", "90 km", 4, 1.0),
            make_essay(2, "Một người lái ô tô khởi hành từ A lúc 8 giờ 30 phút và đến B lúc 11 giờ. Biết vận tốc của ô tô là $52\\text{ km/giờ}$. Tính độ dài quãng đường AB.", "Thời gian ô tô đi từ A đến B là:\n$11\\text{ giờ} - 8\\text{ giờ } 30\\text{ phút} = 2\\text{ giờ } 30\\text{ phút} = 2,5\\text{ giờ}$.\nQuãng đường AB dài là:\n$52 \\times 2,5 = 130\\text{ (km)}$.", "130 km", 4, 1.0),
            make_essay(3, "Một vận động viên chạy bền với vận tốc $12,5\\text{ km/giờ}$ trong 48 phút. Tính quãng đường vận động viên đó chạy được.", "Đổi: $48\\text{ phút} = 48 : 60 = 0,8\\text{ giờ}$.\nQuãng đường vận động viên chạy được là:\n$12,5 \\times 0,8 = 10\\text{ (km)}$.", "10 km", 4, 1.0),
            make_essay(4, "Một người đi từ thành phố A đến thành phố B. Đoạn đường đầu dài $45\\text{ km}$ người đó đi bằng xe máy hết 1,25 giờ. Đoạn đường sau người đó đi bằng ô tô trong 1,5 giờ với vận tốc $50\\text{ km/giờ}$. Tính tổng độ dài quãng đường từ thành phố A đến thành phố B.", "Quãng đường sau đi bằng ô tô là:\n$50 \\times 1,5 = 75\\text{ (km)}$.\nTổng độ dài quãng đường từ A đến B là:\n$45 + 75 = 120\\text{ (km)}$.", "120 km", 5, 1.5),
            make_essay(5, "Một đoàn tàu hỏa chạy với vận tốc $45\\text{ km/giờ}$. Tàu chạy qua một cây cầu dài $350\\text{ m}$ mất 36 giây. Tính chiều dài của đoàn tàu hỏa đó.", "Đổi vận tốc tàu: $45\\text{ km/giờ} = 45 : 3,6 = 12,5\\text{ (m/giây)}$.\nQuãng đường đoàn tàu đi được trong 36 giây là:\n$12,5 \\times 36 = 450\\text{ (m)}$.\nChiều dài đoàn tàu hỏa là:\n$450 - 350 = 100\\text{ (m)}$.", "100 m", 5, 1.5),
            make_essay(6, "Bác Nam đi xe máy từ nhà về quê. Bác đi trong 1 giờ 30 phút đầu với vận tốc $40\\text{ km/giờ}$. Sau đó gặp trời mưa nên bác giảm vận tốc còn $30\\text{ km/giờ}$ và đi thêm 40 phút nữa thì tới quê. Tính quãng đường từ nhà bác Nam về quê.", "Đổi: $1\\text{ giờ } 30\\text{ phút} = 1,5\\text{ giờ}$; $40\\text{ phút} = \\frac{2}{3}\\text{ giờ}$.\nQuãng đường đoạn đầu: $40 \\times 1,5 = 60\\text{ (km)}$.\nQuãng đường đoạn sau: $30 \\times \\frac{2}{3} = 20\\text{ (km)}$.\nTổng quãng đường là: $60 + 20 = 80\\text{ (km)}$.", "80 km", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 50: THỜI GIAN
    # =========================================================================
    # --- Bài 50 - Đề 1 ---
    exams["th5_b50_test1"] = {
        "id": "th5_b50_test1",
        "lessonId": "th5_b50",
        "lessonNum": 50,
        "testNum": 1,
        "title": "Bài 50: Thời gian - Đề số 1",
        "topic": "Thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn tính thời gian đi của một chuyển động đều, ta lấy:", [
                "Quãng đường chia cho vận tốc",
                "Quãng đường nhân với vận tốc",
                "Vận tốc chia cho quãng đường",
                "Quãng đường trừ đi vận tốc"
            ], 0, "Công thức: t = s : v."),
            make_mc(2, "Một ô tô đi quãng đường $135\\text{ km}$ với vận tốc $45\\text{ km/giờ}$. Thời gian ô tô đi là:", ["3 giờ", "2,5 giờ", "3,5 giờ", "4 giờ"], 0, "135 : 45 = 3 giờ."),
            make_mc(3, "Một người đi xe máy đi quãng đường $70\\text{ km}$ với vận tốc $40\\text{ km/giờ}$. Thời gian người đó đi là:", ["1 giờ 45 phút", "1 giờ 30 phút", "1 giờ 15 phút", "1,5 giờ"], 0, "70 : 40 = 1,75 giờ = 1 giờ 45 phút."),
            make_mc(4, "Một con cá kình bơi quãng đường $35\\text{ km}$ với vận tốc $50\\text{ km/giờ}$. Thời gian bơi của nó là:", ["42 phút", "35 phút", "40 phút", "45 phút"], 0, "35 : 50 = 0,7 giờ = 42 phút."),
            make_mc(5, "Một người đi bộ quãng đường $6\\text{ km}$ với vận tốc $4,8\\text{ km/giờ}$. Thời gian người đó đi là:", ["1 giờ 15 phút", "1 giờ 20 phút", "1 giờ 30 phút", "1 giờ"], 0, "6 : 4,8 = 1,25 giờ = 1 giờ 15 phút."),
            make_mc(6, "Một người đi xe máy khởi hành từ A lúc 7 giờ để đi đến B dài $96\\text{ km}$ với vận tốc $40\\text{ km/giờ}$. Người đó đến B lúc:", ["9 giờ 24 phút", "9 giờ 15 phút", "9 giờ 30 phút", "9 giờ"], 0, "t = 96 : 40 = 2,4 giờ = 2 giờ 24 phút. Đến lúc 7h + 2h 24p = 9 giờ 24 phút.")
        ],
        "part2": [
            make_essay(1, "Một ca nô đi trên quãng đường sông dài $63\\text{ km}$ với vận tốc $28\\text{ km/giờ}$. Hỏi ca nô đi hết bao nhiêu thời gian? Đổi kết quả ra giờ và phút.", "Thời gian ca nô đi là:\n$63 : 28 = 2,25\\text{ (giờ)}$.\nĐổi sang giờ và phút: $0,25\\text{ giờ} = 15\\text{ phút}$.\nVậy ca nô đi hết 2 giờ 15 phút.", "2 giờ 15 phút (hoặc 2,25 giờ)", 4, 1.0),
            make_essay(2, "Một người đi xe đạp quãng đường dài $18\\text{ km}$ với vận tốc $12\\text{ km/giờ}$. Tính thời gian người đó đi hết quãng đường theo đơn vị phút.", "Thời gian người đó đi là:\n$18 : 12 = 1,5\\text{ (giờ)}$.\nĐổi sang phút: $1,5 \\times 60 = 90\\text{ (phút)}$.", "90 phút", 4, 1.0),
            make_essay(3, "Bác Nam đi xe máy từ quê ra thành phố trên quãng đường dài $84\\text{ km}$ với vận tốc $35\\text{ km/giờ}$. Bác khởi hành lúc 6 giờ 30 phút sáng. Hỏi bác Nam đến thành phố lúc mấy giờ?", "Thời gian bác Nam đi xe máy là:\n$84 : 35 = 2,4\\text{ (giờ)} = 2\\text{ giờ } 24\\text{ phút}$.\nBác Nam đến thành phố lúc:\n$6\\text{ giờ } 30\\text{ phút} + 2\\text{ giờ } 24\\text{ phút} = 8\\text{ giờ } 54\\text{ phút}$.", "8 giờ 54 phút", 4, 1.0),
            make_essay(4, "Một ô tô chạy từ Hà Nội đến Lạng Sơn dài $154\\text{ km}$ với vận tốc $44\\text{ km/giờ}$. Xe khởi hành lúc 7 giờ 15 phút sáng và giữa đường có nghỉ uống nước 20 phút. Hỏi ô tô đến Lạng Sơn vào lúc mấy giờ?", "Thời gian ô tô chạy thực tế trên đường là:\n$154 : 44 = 3,5\\text{ (giờ)} = 3\\text{ giờ } 30\\text{ phút}$.\nTổng thời gian cả đi và nghỉ là:\n$3\\text{ giờ } 30\\text{ phút} + 20\\text{ phút} = 3\\text{ giờ } 50\\text{ phút}$.\nÔ tô đến Lạng Sơn lúc:\n$7\\text{ giờ } 15\\text{ phút} + 3\\text{ giờ } 50\\text{ phút} = 11\\text{ giờ } 5\\text{ phút}$.", "11 giờ 5 phút", 5, 1.5),
            make_essay(5, "Một máy bay bay từ Hà Nội vào Đà Nẵng trên quãng đường $750\\text{ km}$ với vận tốc $600\\text{ km/giờ}$. Máy bay cất cánh lúc 9 giờ 45 phút. Hỏi máy bay hạ cánh tại sân bay Đà Nẵng lúc mấy giờ?", "Thời gian máy bay bay là:\n$750 : 600 = 1,25\\text{ (giờ)} = 1\\text{ giờ } 15\\text{ phút}$.\nThời điểm máy bay hạ cánh là:\n$9\\text{ giờ } 45\\text{ phút} + 1\\text{ giờ } 15\\text{ phút} = 11\\text{ giờ}$.", "11 giờ đúng", 5, 1.5),
            make_essay(6, "Một người đi bộ một vòng quanh một hồ nước dài $2,4\\text{ km}$ với vận tốc $4\\text{ km/giờ}$. Người đó bắt đầu đi lúc 6 giờ 15 phút. Hỏi người đó đi xong một vòng quanh hồ lúc mấy giờ?", "Thời gian người đó đi hết 1 vòng là:\n$2,4 : 4 = 0,6\\text{ (giờ)} = 36\\text{ phút}$.\nNgười đó đi xong lúc:\n$6\\text{ giờ } 15\\text{ phút} + 36\\text{ phút} = 6\\text{ giờ } 51\\text{ phút}$.", "6 giờ 51 phút", 4, 1.0)
        ]
    }

    # --- Bài 50 - Đề 2 ---
    exams["th5_b50_test2"] = {
        "id": "th5_b50_test2",
        "lessonId": "th5_b50",
        "lessonNum": 50,
        "testNum": 2,
        "title": "Bài 50: Thời gian - Đề số 2",
        "topic": "Thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một xe tải đi quãng đường $150\\text{ km}$ với vận tốc $50\\text{ km/giờ}$. Thời gian xe tải đi là:", ["3 giờ", "2,5 giờ", "3,5 giờ", "4 giờ"], 0, "150 : 50 = 3 giờ."),
            make_mc(2, "Một người đi xe máy đi quãng đường $90\\text{ km}$ với vận tốc $36\\text{ km/giờ}$. Thời gian đi là:", ["2 giờ 30 phút", "2 giờ 15 phút", "2 giờ 45 phút", "3 giờ"], 0, "90 : 36 = 2,5 giờ = 2 giờ 30 phút."),
            make_mc(3, "Một vận động viên chạy cự ly $1 500\\text{ m}$ với vận tốc $5\\text{ m/giây}$. Thời gian chạy là:", ["5 phút", "4 phút", "6 phút", "4,5 phút"], 0, "1500 : 5 = 300 giây = 5 phút."),
            make_mc(4, "Một đoàn tàu hỏa đi quãng đường $195\\text{ km}$ với vận tốc $60\\text{ km/giờ}$. Thời gian tàu hỏa đi là:", ["3 giờ 15 phút", "3 giờ 30 phút", "3 giờ 45 phút", "3 giờ 20 phút"], 0, "195 : 60 = 3,25 giờ = 3 giờ 15 phút."),
            make_mc(5, "Một ô tô đi quãng đường $144\\text{ km}$ với vận tốc $45\\text{ km/giờ}$. Thời gian ô tô đi là:", ["3,2 giờ", "3,4 giờ", "3,5 giờ", "3,25 giờ"], 0, "144 : 45 = 3,2 giờ = 3 giờ 12 phút."),
            make_mc(6, "Bác Ba khởi hành từ A lúc 8 giờ sáng, đi xe máy với vận tốc $42\\text{ km/giờ}$ đến B cách A $63\\text{ km}$. Bác đến B lúc:", ["9 giờ 30 phút", "9 giờ 15 phút", "9 giờ 45 phút", "10 giờ"], 0, "63 : 42 = 1,5 giờ = 1 giờ 30 phút. Đến lúc 8h + 1h 30p = 9 giờ 30 phút.")
        ],
        "part2": [
            make_essay(1, "Một người đi bộ đi quãng đường $7,5\\text{ km}$ với vận tốc $5\\text{ km/giờ}$. Tính thời gian người đó đi theo đơn vị giờ và phút.", "Thời gian người đó đi là:\n$7,5 : 5 = 1,5\\text{ (giờ)}$.\nĐổi sang giờ và phút: $1,5\\text{ giờ} = 1\\text{ giờ } 30\\text{ phút}$.", "1 giờ 30 phút (hoặc 1,5 giờ)", 4, 1.0),
            make_essay(2, "Một xe máy đi từ A đến B dài $114\\text{ km}$ với vận tốc $38\\text{ km/giờ}$. Xe khởi hành lúc 7 giờ 45 phút. Hỏi xe máy đến B lúc mấy giờ?", "Thời gian xe máy đi từ A đến B là:\n$114 : 38 = 3\\text{ (giờ)}$.\nThời điểm xe máy đến B là:\n$7\\text{ giờ } 45\\text{ phút} + 3\\text{ giờ} = 10\\text{ giờ } 45\\text{ phút}$.", "10 giờ 45 phút", 4, 1.0),
            make_essay(3, "Một con chim bồ câu đưa thư bay quãng đường $117\\text{ km}$ với vận tốc $52\\text{ km/giờ}$. Hỏi chim bồ câu bay hết bao nhiêu thời gian?", "Thời gian chim bồ câu bay là:\n$117 : 52 = 2,25\\text{ (giờ)} = 2\\text{ giờ } 15\\text{ phút}$.", "2 giờ 15 phút", 4, 1.0),
            make_essay(4, "Quãng đường sông từ bến A đến bến B dài $40,5\\text{ km}$. Một tàu thủy đi với vận tốc $27\\text{ km/giờ}$. Tàu khởi hành lúc 8 giờ 15 phút và dọc đường có đỗ đón khách tại một bến phụ hết 25 phút. Hỏi tàu thủy đến bến B vào lúc mấy giờ?", "Thời gian tàu chạy thực tế là:\n$40,5 : 27 = 1,5\\text{ (giờ)} = 1\\text{ giờ } 30\\text{ phút}$.\nTổng thời gian đi và đỗ là:\n$1\\text{ giờ } 30\\text{ phút} + 25\\text{ phút} = 1\\text{ giờ } 55\\text{ phút}$.\nTàu thủy đến B lúc:\n$8\\text{ giờ } 15\\text{ phút} + 1\\text{ giờ } 55\\text{ phút} = 10\\text{ giờ } 10\\text{ phút}$.", "10 giờ 10 phút", 5, 1.5),
            make_essay(5, "Một ô tô và một xe máy cùng đi trên quãng đường AB dài $120\\text{ km}$. Ô tô đi với vận tốc $50\\text{ km/giờ}$, xe máy đi với vận tốc $40\\text{ km/giờ}$. Hỏi ô tô đến B trước xe máy bao nhiêu phút?", "Thời gian ô tô đi từ A đến B là: $120 : 50 = 2,4\\text{ (giờ)} = 144\\text{ phút}$.\nThời gian xe máy đi từ A đến B là: $120 : 40 = 3\\text{ (giờ)} = 180\\text{ phút}$.\nÔ tô đến trước xe máy số phút là: $180 - 144 = 36\\text{ (phút)}$.", "36 phút", 5, 1.5),
            make_essay(6, "Một người đi xe đạp một quãng đường dài $14\\text{ km}$ với vận tốc $12\\text{ km/giờ}$. Hỏi người đó đi hết bao nhiêu phút?", "Thời gian người đó đi là:\n$14 : 12 = \\frac{7}{6}\\text{ (giờ)}$.\nĐổi sang phút: $\\frac{7}{6} \\times 60 = 70\\text{ (phút)} = 1\\text{ giờ } 10\\text{ phút}$.", "70 phút (hay 1 giờ 10 phút)", 4, 1.0)
        ]
    }

    # --- Bài 50 - Đề 3 ---
    exams["th5_b50_test3"] = {
        "id": "th5_b50_test3",
        "lessonId": "th5_b50",
        "lessonNum": 50,
        "testNum": 3,
        "title": "Bài 50: Thời gian - Đề số 3",
        "topic": "Thời gian",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một người chạy bộ cự ly $800\\text{ m}$ với vận tốc $4\\text{ m/giây}$. Thời gian chạy là:", ["200 giây", "180 giây", "250 giây", "3 phút"], 0, "800 : 4 = 200 giây (3 phút 20 giây)."),
            make_mc(2, "Một ô tô đi quãng đường $126\\text{ km}$ với vận tốc $42\\text{ km/giờ}$. Thời gian ô tô đi là:", ["3 giờ", "2,5 giờ", "3,5 giờ", "4 giờ"], 0, "126 : 42 = 3 giờ."),
            make_mc(3, "Một xe đạp đi $21\\text{ km}$ với vận tốc $14\\text{ km/giờ}$. Thời gian đi là:", ["1 giờ 30 phút", "1 giờ 15 phút", "1 giờ 45 phút", "2 giờ"], 0, "21 : 14 = 1,5 giờ = 1 giờ 30 phút."),
            make_mc(4, "Một máy bay bay cự ly $1 200\\text{ km}$ với vận tốc $800\\text{ km/giờ}$. Thời gian bay là:", ["1 giờ 30 phút", "1 giờ 15 phút", "1 giờ 45 phút", "2 giờ"], 0, "1200 : 800 = 1,5 giờ = 1 giờ 30 phút."),
            make_mc(5, "Một người đi xe máy đi quãng đường $65\\text{ km}$ với vận tốc $39\\text{ km/giờ}$. Thời gian đi là:", ["1 giờ 40 phút", "1 giờ 30 phút", "1 giờ 20 phút", "1 giờ 45 phút"], 0, "65 : 39 = 5/3 giờ = 1 giờ 40 phút."),
            make_mc(6, "Một tàu hỏa đi quãng đường $168\\text{ km}$ với vận tốc $48\\text{ km/giờ}$. Thời gian tàu hỏa đi là:", ["3,5 giờ", "3,25 giờ", "3,75 giờ", "4 giờ"], 0, "168 : 48 = 3,5 giờ = 3 giờ 30 phút.")
        ],
        "part2": [
            make_essay(1, "Một người đi xe máy quãng đường $96\\text{ km}$ với vận tốc $36\\text{ km/giờ}$. Tính thời gian người đó đi theo đơn vị giờ và phút.", "Thời gian đi là:\n$96 : 36 = \\frac{8}{3}\\text{ (giờ)} = 2\\frac{2}{3}\\text{ giờ} = 2\\text{ giờ } 40\\text{ phút}$.", "2 giờ 40 phút", 4, 1.0),
            make_essay(2, "Một người đi ô tô từ A lúc 8 giờ 15 phút đến B với vận tốc $48\\text{ km/giờ}$. Biết quãng đường AB dài $108\\text{ km}$. Hỏi người đó đến B lúc mấy giờ?", "Thời gian ô tô đi là:\n$108 : 48 = 2,25\\text{ (giờ)} = 2\\text{ giờ } 15\\text{ phút}$.\nNgười đó đến B lúc:\n$8\\text{ giờ } 15\\text{ phút} + 2\\text{ giờ } 15\\text{ phút} = 10\\text{ giờ } 30\\text{ phút}$.", "10 giờ 30 phút", 4, 1.0),
            make_essay(3, "Một con rùa bò với vận tốc $0,05\\text{ m/giây}$. Hỏi con rùa đó bò hết đoạn đường dài $18\\text{ m}$ trong bao lâu?", "Thời gian con rùa bò là:\n$18 : 0,05 = 360\\text{ (giây)}$.\nĐổi sang phút: $360 : 60 = 6\\text{ phút}$.", "6 phút (hoặc 360 giây)", 4, 1.0),
            make_essay(4, "Một ô tô dự định chạy từ tỉnh A đến tỉnh B dài $120\\text{ km}$ với vận tốc $40\\text{ km/giờ}$. Nhưng thực tế ô tô chạy với vận tốc $48\\text{ km/giờ}$. Hỏi ô tô đến B sớm hơn dự định bao nhiêu phút?", "Thời gian dự định đi là: $120 : 40 = 3\\text{ (giờ)} = 180\\text{ phút}$.\nThời gian thực tế đi là: $120 : 48 = 2,5\\text{ (giờ)} = 150\\text{ phút}$.\nÔ tô đến sớm hơn dự định là:\n$180 - 150 = 30\\text{ (phút)}$.", "30 phút", 5, 1.5),
            make_essay(5, "Quãng đường AB dài $150\\text{ km}$. Một ô tô khởi hành từ A lúc 7 giờ sáng với vận tốc $50\\text{ km/giờ}$. Giữa đường xe dừng lại nghỉ 45 phút. Hỏi ô tô đến B lúc mấy giờ trưa?", "Thời gian ô tô chạy là: $150 : 50 = 3\\text{ (giờ)}$.\nTổng thời gian đi và nghỉ là:\n$3\\text{ giờ} + 45\\text{ phút} = 3\\text{ giờ } 45\\text{ phút}$.\nThời điểm ô tô đến B là:\n$7\\text{ giờ} + 3\\text{ giờ } 45\\text{ phút} = 10\\text{ giờ } 45\\text{ phút}$.", "10 giờ 45 phút", 5, 1.5),
            make_essay(6, "Một người đi xe máy từ A đến B với vận tốc $40\\text{ km/giờ}$. Sau đó người đó đi từ B về A bằng ô tô với vận tốc $60\\text{ km/giờ}$. Biết quãng đường AB dài $120\\text{ km}$. Tính tổng thời gian cả đi và về của người đó.", "Thời gian đi từ A đến B: $120 : 40 = 3\\text{ (giờ)}$.\nThời gian về từ B về A: $120 : 60 = 2\\text{ (giờ)}$.\nTổng thời gian cả đi và về là: $3 + 2 = 5\\text{ (giờ)}$.", "5 giờ", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 51: BÀI TOÁN CHUYỂN ĐỘNG ĐỀU
    # =========================================================================
    # --- Bài 51 - Đề 1 ---
    exams["th5_b51_test1"] = {
        "id": "th5_b51_test1",
        "lessonId": "th5_b51",
        "lessonNum": 51,
        "testNum": 1,
        "title": "Bài 51: Bài toán chuyển động đều - Đề số 1",
        "topic": "Bài toán chuyển động đều",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hai chuyển động ngược chiều khởi hành cùng lúc để gặp nhau. Thời gian gặp nhau được tính bằng:", [
                "Quãng đường chia cho tổng hai vận tốc: $t = s : (v_1 + v_2)$",
                "Quãng đường chia cho hiệu hai vận tốc: $t = s : (v_1 - v_2)$",
                "Quãng đường nhân với tổng hai vận tốc",
                "Hiệu hai vận tốc chia cho quãng đường"
            ], 0, "Công thức gặp nhau ngược chiều: t = s : (v1 + v2)."),
            make_mc(2, "Hai ô tô ở hai tỉnh A và B cách nhau $180\\text{ km}$, đi ngược chiều và gặp nhau sau 2 giờ. Tổng vận tốc của hai ô tô là:", ["90 km/giờ", "80 km/giờ", "100 km/giờ", "95 km/giờ"], 0, "180 : 2 = 90 km/giờ."),
            make_mc(3, "Một xe máy đi từ A với vận tốc $35\\text{ km/giờ}$, một ô tô đi từ B với vận tốc $45\\text{ km/giờ}$ ngược chiều nhau. Sau 1 giờ cả hai xe đi được quãng đường là:", ["80 km", "70 km", "90 km", "10 km"], 0, "35 + 45 = 80 km."),
            make_mc(4, "Một ca nô đi xuôi dòng sông với vận tốc thực $25\\text{ km/giờ}$, vận tốc dòng nước là $3\\text{ km/giờ}$. Vận tốc xuôi dòng của ca nô là:", ["28 km/giờ", "22 km/giờ", "25 km/giờ", "30 km/giờ"], 0, "25 + 3 = 28 km/giờ."),
            make_mc(5, "Một ca nô đi ngược dòng có vận tốc thực $25\\text{ km/giờ}$, vận tốc dòng nước là $3\\text{ km/giờ}$. Vận tốc ngược dòng của ca nô là:", ["22 km/giờ", "28 km/giờ", "25 km/giờ", "21 km/giờ"], 0, "25 - 3 = 22 km/giờ."),
            make_mc(6, "Hai người xuất phát cùng lúc từ cùng một địa điểm và đi cùng chiều. Người thứ nhất đi với vận tốc $40\\text{ km/giờ}$, người thứ hai đi với vận tốc $30\\text{ km/giờ}$. Sau 2 giờ, khoảng cách giữa hai người là:", ["20 km", "10 km", "70 km", "140 km"], 0, "(40 - 30) x 2 = 20 km.")
        ],
        "part2": [
            make_essay(1, "Quãng đường AB dài $162\\text{ km}$. Lúc 7 giờ, một xe máy đi từ A đến B với vận tốc $36\\text{ km/giờ}$ và cùng lúc đó một ô tô đi từ B về A với vận tốc $54\\text{ km/giờ}$. Hỏi hai xe gặp nhau lúc mấy giờ?", "Tổng vận tốc của hai xe là:\n$36 + 54 = 90\\text{ (km/giờ)}$.\nThời gian hai xe gặp nhau là:\n$162 : 90 = 1,8\\text{ (giờ)} = 1\\text{ giờ } 48\\text{ phút}$.\nHai xe gặp nhau lúc:\n$7\\text{ giờ} + 1\\text{ giờ } 48\\text{ phút} = 8\\text{ giờ } 48\\text{ phút}$.", "8 giờ 48 phút", 4, 1.0),
            make_essay(2, "Quãng đường AB dài $120\\text{ km}$. Lúc 6 giờ 30 phút, một ô tô đi từ A đến B với vận tốc $50\\text{ km/giờ}$ và một xe máy đi từ B về A với vận tốc $30\\text{ km/giờ}$. Hỏi chỗ gặp nhau cách A bao nhiêu ki-lô-mét?", "Tổng vận tốc của hai xe là:\n$50 + 30 = 80\\text{ (km/giờ)}$.\nThời gian để hai xe gặp nhau là:\n$120 : 80 = 1,5\\text{ (giờ)}$.\nChỗ gặp nhau cách A số ki-lô-mét là quãng đường ô tô đi được:\n$50 \\times 1,5 = 75\\text{ (km)}$.", "75 km", 4, 1.0),
            make_essay(3, "Lúc 7 giờ một người đi xe đạp từ A với vận tốc $12\\text{ km/giờ}$. Đến 8 giờ 30 phút một người đi xe máy cũng khởi hành từ A đuổi theo xe đạp với vận tốc $36\\text{ km/giờ}$. Hỏi người đi xe máy đuổi kịp người đi xe đạp lúc mấy giờ?", "Thời gian người đi xe đạp đi trước là:\n$8\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} = 1\\text{ giờ } 30\\text{ phút} = 1,5\\text{ giờ}$.\nQuãng đường xe đạp đi trước là:\n$12 \\times 1,5 = 18\\text{ (km)}$.\nHiệu vận tốc của hai xe là:\n$36 - 12 = 24\\text{ (km/giờ)}$.\nThời gian để xe máy đuổi kịp xe đạp là:\n$18 : 24 = 0,75\\text{ (giờ)} = 45\\text{ phút}$.\nXe máy đuổi kịp xe đạp lúc:\n$8\\text{ giờ } 30\\text{ phút} + 45\\text{ phút} = 9\\text{ giờ } 15\\text{ phút}$.", "9 giờ 15 phút", 5, 1.0),
            make_essay(4, "Một thuyền máy đi xuôi dòng từ A đến B mất 2 giờ và đi ngược dòng từ B về A mất 3 giờ. Biết quãng đường AB dài $60\\text{ km}$. Tính vận tốc thực của thuyền máy và vận tốc của dòng nước.", "Vận tốc xuôi dòng là: $60 : 2 = 30\\text{ (km/giờ)}$.\nVận tốc ngược dòng là: $60 : 3 = 20\\text{ (km/giờ)}$.\nVận tốc dòng nước là:\n$(30 - 20) : 2 = 5\\text{ (km/giờ)}$.\nVận tốc thực của thuyền máy là:\n$30 - 5 = 25\\text{ (km/giờ)}$.", "Vận tốc thuyền: 25 km/giờ; Vận tốc dòng nước: 5 km/giờ", 5, 1.5),
            make_essay(5, "Hai người đi xe máy khởi hành cùng lúc từ hai địa điểm A và B cách nhau $35\\text{ km}$ và đi cùng chiều về phía C (B nằm giữa A và C). Người đi từ A có vận tốc $45\\text{ km/giờ}$, người đi từ B có vận tốc $35\\text{ km/giờ}$. Hỏi sau bao lâu người đi từ A đuổi kịp người đi từ B?", "Hiệu vận tốc của hai xe là:\n$45 - 35 = 10\\text{ (km/giờ)}$.\nThời gian để người đi từ A đuổi kịp người đi từ B là:\n$35 : 10 = 3,5\\text{ (giờ)} = 3\\text{ giờ } 30\\text{ phút}$.", "3 giờ 30 phút (hoặc 3,5 giờ)", 5, 1.5),
            make_essay(6, "Một đoàn tàu hỏa chạy với vận tốc $36\\text{ km/giờ}$ vượt qua một người đi bộ ngược chiều với vận tốc $3,6\\text{ km/giờ}$ trong 12 giây. Tính chiều dài của đoàn tàu hỏa.", "Tổng vận tốc của tàu và người đi bộ ngược chiều là:\n$36 + 3,6 = 39,6\\text{ (km/giờ)}$.\nĐổi sang m/giây: $39,6 : 3,6 = 11\\text{ (m/giây)}$.\nChiều dài đoàn tàu hỏa là quãng đường hai đối tượng đi được trong 12 giây:\n$11 \\times 12 = 132\\text{ (m)}$.", "132 m", 4, 1.0)
        ]
    }

    # --- Bài 51 - Đề 2 ---
    exams["th5_b51_test2"] = {
        "id": "th5_b51_test2",
        "lessonId": "th5_b51",
        "lessonNum": 51,
        "testNum": 2,
        "title": "Bài 51: Bài toán chuyển động đều - Đề số 2",
        "topic": "Bài toán chuyển động đều",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hai xe chuyển động cùng chiều đuổi nhau, khởi hành cùng lúc cách nhau khoảng cách $s$. Thời gian đuổi kịp nhau là:", [
                "$t = s : (v_1 - v_2)$ (với $v_1 > v_2$)",
                "$t = s : (v_1 + v_2)$",
                "$t = s \\times (v_1 - v_2)$",
                "$t = (v_1 - v_2) : s$"
            ], 0, "Công thức đuổi kịp cùng chiều: t = s : (v1 - v2)."),
            make_mc(2, "Hai tỉnh A và B cách nhau $140\\text{ km}$. Hai ô tô khởi hành cùng lúc đi ngược chiều nhau và gặp nhau sau 2 giờ. Nếu vận tốc ô tô thứ nhất là $40\\text{ km/giờ}$ thì vận tốc ô tô thứ hai là:", ["30 km/giờ", "35 km/giờ", "45 km/giờ", "25 km/giờ"], 0, "Tổng v = 140 : 2 = 70 km/h. v2 = 70 - 40 = 30 km/h."),
            make_mc(3, "Một ca nô đi xuôi dòng trên một khúc sông hết 2 giờ với vận tốc $32\\text{ km/giờ}$. Vận tốc dòng nước là $4\\text{ km/giờ}$. Vận tốc ngược dòng của ca nô là:", ["24 km/giờ", "28 km/giờ", "26 km/giờ", "20 km/giờ"], 0, "Vận tốc ngược dòng = v_xuôi - 2 x v_nước = 32 - 8 = 24 km/giờ."),
            make_mc(4, "Một người đi xe máy đuổi theo một người đi xe đạp cách mình $24\\text{ km}$. Vận tốc xe máy là $42\\text{ km/giờ}$, xe đạp là $12\\text{ km/giờ}$. Sau bao lâu xe máy đuổi kịp xe đạp?", ["48 phút", "1 giờ", "1,2 giờ", "50 phút"], 0, "t = 24 : (42 - 12) = 24 : 30 = 0,8 giờ = 48 phút."),
            make_mc(5, "Hai xe đi ngược chiều từ hai vị trí cách nhau $150\\text{ km}$ với vận tốc $35\\text{ km/giờ}$ và $40\\text{ km/giờ}$. Sau 1,5 giờ, khoảng cách giữa hai xe còn lại là:", ["37,5 km", "40 km", "35 km", "45 km"], 0, "Quãng đường 2 xe đi: (35 + 40) x 1,5 = 112,5 km. Còn lại: 150 - 112,5 = 37,5 km."),
            make_mc(6, "Một người đi xe đạp với vận tốc $12\\text{ km/giờ}$ và một người đi bộ với vận tốc $4\\text{ km/giờ}$ cùng khởi hành từ một địa điểm đi cùng chiều. Sau 45 phút, hai người cách nhau:", ["6 km", "8 km", "5 km", "4 km"], 0, "Hiệu vận tốc: 8 km/h. Sau 45 phút = 0,75h: 8 x 0,75 = 6 km.")
        ],
        "part2": [
            make_essay(1, "Quãng đường AB dài $175\\text{ km}$. Cùng lúc 7 giờ 15 phút, một ô tô đi từ A đến B với vận tốc $45\\text{ km/giờ}$ và một ô tô đi từ B về A với vận tốc $55\\text{ km/giờ}$. Hỏi hai ô tô gặp nhau lúc mấy giờ?", "Tổng vận tốc của hai ô tô là:\n$45 + 55 = 100\\text{ (km/giờ)}$.\nThời gian hai ô tô gặp nhau là:\n$175 : 100 = 1,75\\text{ (giờ)} = 1\\text{ giờ } 45\\text{ phút}$.\nHai ô tô gặp nhau lúc:\n$7\\text{ giờ } 15\\text{ phút} + 1\\text{ giờ } 45\\text{ phút} = 9\\text{ giờ}$.", "9 giờ đúng", 4, 1.0),
            make_essay(2, "Hai thành phố cách nhau $210\\text{ km}$. Một ô tô đi từ A với vận tốc $52\\text{ km/giờ}$, một ô tô đi từ B với vận tốc $48\\text{ km/giờ}$ cùng khởi hành lúc 8 giờ sáng để gặp nhau. Chỗ gặp nhau cách B bao nhiêu ki-lô-mét?", "Tổng vận tốc của hai ô tô là:\n$52 + 48 = 100\\text{ (km/giờ)}$.\nThời gian để hai xe gặp nhau là:\n$210 : 100 = 2,1\\text{ (giờ)}$.\nChỗ gặp nhau cách B số ki-lô-mét là quãng đường xe B đi:\n$48 \\times 2,1 = 100,8\\text{ (km)}$.", "100,8 km", 4, 1.0),
            make_essay(3, "Lúc 6 giờ sáng một người đi bộ từ A đến B với vận tốc $4\\text{ km/giờ}$. Lúc 7 giờ 30 phút một người đi xe đạp cũng từ A đi đuổi theo với vận tốc $12\\text{ km/giờ}$. Hỏi người đi xe đạp đuổi kịp người đi bộ lúc mấy giờ?", "Thời gian người đi bộ đi trước là:\n$7\\text{ giờ } 30\\text{ phút} - 6\\text{ giờ} = 1\\text{ giờ } 30\\text{ phút} = 1,5\\text{ giờ}$.\nQuãng đường người đi bộ đi trước là:\n$4 \\times 1,5 = 6\\text{ (km)}$.\nHiệu vận tốc của hai người là:\n$12 - 4 = 8\\text{ (km/giờ)}$.\nThời gian để xe đạp đuổi kịp người đi bộ là:\n$6 : 8 = 0,75\\text{ (giờ)} = 45\\text{ phút}$.\nXe đạp đuổi kịp lúc:\n$7\\text{ giờ } 30\\text{ phút} + 45\\text{ phút} = 8\\text{ giờ } 15\\text{ phút}$.", "8 giờ 15 phút", 5, 1.0),
            make_essay(4, "Một ca nô đi xuôi dòng một khúc sông từ A đến B dài $90\\text{ km}$ hết 3 giờ và đi ngược dòng từ B về A hết 4,5 giờ. Tính vận tốc của dòng nước và vận tốc của ca nô khi nước yên lặng.", "Vận tốc xuôi dòng của ca nô là: $90 : 3 = 30\\text{ (km/giờ)}$.\nVận tốc ngược dòng của ca nô là: $90 : 4,5 = 20\\text{ (km/giờ)}$.\nVận tốc của dòng nước là:\n$(30 - 20) : 2 = 5\\text{ (km/giờ)}$.\nVận tốc của ca nô khi nước yên lặng là:\n$30 - 5 = 25\\text{ (km/giờ)}$.", "Vận tốc ca nô: 25 km/giờ; Vận tốc dòng nước: 5 km/giờ", 5, 1.5),
            make_essay(5, "Một xe máy đi từ A với vận tốc $36\\text{ km/giờ}$. Sau 1 giờ 15 phút, một ô tô cũng khởi hành từ A với vận tốc $54\\text{ km/giờ}$ đuổi theo xe máy. Hỏi sau bao lâu kể từ lúc ô tô xuất phát thì ô tô đuổi kịp xe máy và điểm gặp nhau cách A bao nhiêu ki-lô-mét?", "Đổi: $1\\text{ giờ } 15\\text{ phút} = 1,25\\text{ giờ}$.\nQuãng đường xe máy đi trước ô tô là: $36 \\times 1,25 = 45\\text{ (km)}$.\nHiệu vận tốc hai xe là: $54 - 36 = 18\\text{ (km/giờ)}$.\nThời gian để ô tô đuổi kịp xe máy là:\n$45 : 18 = 2,5\\text{ (giờ)} = 2\\text{ giờ } 30\\text{ phút}$.\nĐiểm gặp nhau cách A là:\n$54 \\times 2,5 = 135\\text{ (km)}$.", "Thời gian: 2 giờ 30 phút; Cách A: 135 km", 5, 1.5),
            make_essay(6, "Hai bạn An và Bình cùng xuất phát từ trường lúc 16 giờ 30 phút đi về hai hướng ngược nhau. An đi xe đạp với vận tốc $12\\text{ km/giờ}$, Bình đi bộ với vận tốc $4\\text{ km/giờ}$. Hỏi vào lúc 17 giờ, hai bạn cách nhau bao nhiêu ki-lô-mét?", "Thời gian hai bạn đi là: $17\\text{ giờ} - 16\\text{ giờ } 30\\text{ phút} = 30\\text{ phút} = 0,5\\text{ giờ}$.\nTổng vận tốc của hai bạn là: $12 + 4 = 16\\text{ (km/giờ)}$.\nKhoảng cách giữa hai bạn lúc 17 giờ là:\n$16 \\times 0,5 = 8\\text{ (km)}$.", "8 km", 4, 1.0)
        ]
    }

    # --- Bài 51 - Đề 3 ---
    exams["th5_b51_test3"] = {
        "id": "th5_b51_test3",
        "lessonId": "th5_b51",
        "lessonNum": 51,
        "testNum": 3,
        "title": "Bài 51: Bài toán chuyển động đều - Đề số 3",
        "topic": "Bài toán chuyển động đều",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hai xe khởi hành cùng lúc từ hai điểm A và B cách nhau $120\\text{ km}$, đi ngược chiều nhau và gặp nhau sau 1,5 giờ. Tổng vận tốc của hai xe là:", ["80 km/giờ", "75 km/giờ", "90 km/giờ", "85 km/giờ"], 0, "120 : 1,5 = 80 km/giờ."),
            make_mc(2, "Một người đi xe máy với vận tốc $38\\text{ km/giờ}$, người kia đi với vận tốc $42\\text{ km/giờ}$ ngược chiều nhau. Cứ sau mỗi giờ, khoảng cách giữa hai người giảm đi:", ["80 km", "4 km", "40 km", "84 km"], 0, "Tổng vận tốc là 38 + 42 = 80 km/h, nên khoảng cách giảm 80 km mỗi giờ."),
            make_mc(3, "Ca nô có vận tốc khi nước lặng là $24\\text{ km/giờ}$, vận tốc dòng nước là $2,5\\text{ km/giờ}$. Vận tốc xuôi dòng của ca nô là:", ["26,5 km/giờ", "21,5 km/giờ", "24 km/giờ", "27 km/giờ"], 0, "24 + 2,5 = 26,5 km/giờ."),
            make_mc(4, "Một ô tô chạy từ A đuổi theo xe máy từ B cách A $30\\text{ km}$. Vận tốc ô tô là $55\\text{ km/giờ}$, xe máy là $35\\text{ km/giờ}$. Sau bao lâu ô tô đuổi kịp xe máy?", ["1,5 giờ", "1,2 giờ", "2 giờ", "1 giờ"], 0, "t = 30 : (55 - 35) = 30 : 20 = 1,5 giờ."),
            make_mc(5, "Một cụm bèo trôi trên sông theo dòng nước từ bến A đến bến B cách nhau $12\\text{ km}$ hết 4 giờ. Vận tốc dòng nước là:", ["3 km/giờ", "4 km/giờ", "2 km/giờ", "2,5 km/giờ"], 0, "Cụm bèo trôi với vận tốc dòng nước: 12 : 4 = 3 km/giờ."),
            make_mc(6, "Hai ô tô đi cùng chiều từ hai điểm cách nhau $40\\text{ km}$. Xe thứ nhất đi với vận tốc $50\\text{ km/giờ}$, xe thứ hai đi trước với vận tốc $40\\text{ km/giờ}$. Thời gian xe thứ nhất đuổi kịp xe thứ hai là:", ["4 giờ", "3 giờ", "5 giờ", "3,5 giờ"], 0, "t = 40 : (50 - 40) = 4 giờ.")
        ],
        "part2": [
            make_essay(1, "Hai thành phố A và B cách nhau $180\\text{ km}$. Một ô tô đi từ A đến B với vận tốc $54\\text{ km/giờ}$ và cùng lúc đó một xe máy đi từ B về A với vận tốc $36\\text{ km/giờ}$. Cả hai cùng xuất phát lúc 7 giờ 30 phút. Hỏi hai xe gặp nhau lúc mấy giờ?", "Tổng vận tốc của hai xe là:\n$54 + 36 = 90\\text{ (km/giờ)}$.\nThời gian hai xe đi để gặp nhau là:\n$180 : 90 = 2\\text{ (giờ)}$.\nHai xe gặp nhau lúc:\n$7\\text{ giờ } 30\\text{ phút} + 2\\text{ giờ} = 9\\text{ giờ } 30\\text{ phút}$.", "9 giờ 30 phút", 4, 1.0),
            make_essay(2, "Quãng đường AB dài $150\\text{ km}$. Lúc 7 giờ, một xe khách đi từ A đến B với vận tốc $55\\text{ km/giờ}$ và một xe tải đi từ B về A với vận tốc $45\\text{ km/giờ}$. Hỏi chỗ hai xe gặp nhau cách A bao nhiêu ki-lô-mét?", "Tổng vận tốc của hai xe là:\n$55 + 45 = 100\\text{ (km/giờ)}$.\nThời gian hai xe gặp nhau là:\n$150 : 100 = 1,5\\text{ (giờ)}$.\nChỗ gặp nhau cách A số ki-lô-mét là quãng đường xe khách đi được:\n$55 \\times 1,5 = 82,5\\text{ (km)}$.", "82,5 km", 4, 1.0),
            make_essay(3, "Lúc 7 giờ sáng một người đi xe đạp từ A với vận tốc $12\\text{ km/giờ}$. Đến 9 giờ, một người đi xe máy cũng từ A đuổi theo với vận tốc $36\\text{ km/giờ}$. Hỏi người đi xe máy đuổi kịp người đi xe đạp lúc mấy giờ?", "Thời gian xe đạp đi trước là: $9 - 7 = 2\\text{ (giờ)}$.\nQuãng đường xe đạp đi trước là: $12 \\times 2 = 24\\text{ (km)}$.\nHiệu vận tốc của hai xe là: $36 - 12 = 24\\text{ (km/giờ)}$.\nThời gian để xe máy đuổi kịp xe đạp là: $24 : 24 = 1\\text{ (giờ)}$.\nXe máy đuổi kịp xe đạp lúc: $9\\text{ giờ} + 1\\text{ giờ} = 10\\text{ giờ}$.", "10 giờ đúng", 5, 1.0),
            make_essay(4, "Một ca nô đi xuôi dòng từ A đến B dài $72\\text{ km}$ hết 2 giờ 24 phút. Vận tốc dòng nước chảy là $2,5\\text{ km/giờ}$. Hỏi ca nô đi ngược dòng từ B về A hết bao nhiêu thời gian?", "Đổi: $2\\text{ giờ } 24\\text{ phút} = 2,4\\text{ giờ}$.\nVận tốc xuôi dòng của ca nô là: $72 : 2,4 = 30\\text{ (km/giờ)}$.\nVận tốc thực của ca nô (nước yên lặng) là: $30 - 2,5 = 27,5\\text{ (km/giờ)}$.\nVận tốc ngược dòng của ca nô là: $27,5 - 2,5 = 25\\text{ (km/giờ)}$.\nThời gian ca nô đi ngược dòng từ B về A là:\n$72 : 25 = 2,88\\text{ (giờ)} = 2\\text{ giờ } 52\\text{ phút } 48\\text{ giây}$.", "2,88 giờ (hay 2 giờ 52 phút 48 giây)", 5, 1.5),
            make_essay(5, "Hai người đi xe máy cùng lúc từ hai địa điểm A và B cách nhau $24\\text{ km}$ đi cùng chiều nhau về phía C. Người khởi hành từ A có vận tốc $42\\text{ km/giờ}$, người khởi hành từ B có vận tốc $34\\text{ km/giờ}$. Hỏi sau bao lâu người đi từ A đuổi kịp người đi từ B và chỗ gặp nhau cách A bao nhiêu ki-lô-mét?", "Hiệu vận tốc hai xe là: $42 - 34 = 8\\text{ (km/giờ)}$.\nThời gian để xe đi từ A đuổi kịp xe đi từ B là:\n$24 : 8 = 3\\text{ (giờ)}$.\nChỗ gặp nhau cách A là quãng đường xe A đi được:\n$42 \\times 3 = 126\\text{ (km)}$.", "Sau 3 giờ; Cách A: 126 km", 5, 1.5),
            make_essay(6, "Một người đi thuyền xuôi dòng từ bến A đến bến B mất 45 phút với vận tốc xuôi dòng là $16\\text{ km/giờ}$. Sau đó người đó đi ngược dòng từ B về A với vận tốc ngược dòng là $12\\text{ km/giờ}$. Tính thời gian thuyền đi ngược dòng từ B về A.", "Đổi: $45\\text{ phút} = 0,75\\text{ giờ}$.\nQuãng đường sông AB dài là: $16 \\times 0,75 = 12\\text{ (km)}$.\nThời gian thuyền đi ngược dòng từ B về A là:\n$12 : 12 = 1\\text{ (giờ)}$.", "1 giờ", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 52: LUYỆN TẬP CHUNG CHỦ ĐỀ 9
    # =========================================================================
    # --- Bài 52 - Đề 1 ---
    exams["th5_b52_test1"] = {
        "id": "th5_b52_test1",
        "lessonId": "th5_b52",
        "lessonNum": 52,
        "testNum": 1,
        "title": "Bài 52: Luyện tập chung Chủ đề 9 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 9",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Đổi: $2\\text{ giờ } 15\\text{ phút} = \\dots \\text{ giờ}$:", ["2,15 giờ", "2,25 giờ", "2,5 giờ", "2,4 giờ"], 1, "15/60 = 0,25h => 2,25 giờ."),
            make_mc(2, "Tính: $3\\text{ giờ } 40\\text{ phút} + 2\\text{ giờ } 35\\text{ phút}$ bằng:", ["6 giờ 15 phút", "5 giờ 75 phút", "6 giờ 25 phút", "5 giờ 15 phút"], 0, "5h 75p = 6 giờ 15 phút."),
            make_mc(3, "Một ô tô đi quãng đường $160\\text{ km}$ hết 3,2 giờ. Vận tốc của ô tô là:", ["50 km/giờ", "45 km/giờ", "52 km/giờ", "48 km/giờ"], 0, "160 : 3,2 = 50 km/giờ."),
            make_mc(4, "Một người đi xe máy với vận tốc $36\\text{ km/giờ}$ trong 45 phút. Quãng đường đi được là:", ["27 km", "30 km", "24 km", "25 km"], 0, "45 phút = 0,75 giờ. 36 x 0,75 = 27 km."),
            make_mc(5, "Một người đi bộ $7,2\\text{ km}$ với vận tốc $4,8\\text{ km/giờ}$. Thời gian người đó đi là:", ["1,5 giờ", "1,2 giờ", "1,25 giờ", "1,75 giờ"], 0, "7,2 : 4,8 = 1,5 giờ (1 giờ 30 phút)."),
            make_mc(6, "Hai ô tô đi ngược chiều từ hai điểm cách nhau $180\\text{ km}$ với vận tốc $42\\text{ km/giờ}$ và $48\\text{ km/giờ}$. Hai xe gặp nhau sau:", ["2 giờ", "2,5 giờ", "1,8 giờ", "2,2 giờ"], 0, "t = 180 : (42 + 48) = 180 : 90 = 2 giờ.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $4\\text{ giờ } 25\\text{ phút} + 3\\text{ giờ } 48\\text{ phút}$\nb) $7\\text{ phút } 12\\text{ giây} - 3\\text{ phút } 35\\text{ giây}$", "a) $4\\text{ giờ } 25\\text{ phút} + 3\\text{ giờ } 48\\text{ phút} = 7\\text{ giờ } 73\\text{ phút} = 8\\text{ giờ } 13\\text{ phút}$.\nb) $7\\text{ phút } 12\\text{ giây} - 3\\text{ phút } 35\\text{ giây} = 6\\text{ phút } 72\\text{ giây} - 3\\text{ phút } 35\\text{ giây} = 3\\text{ phút } 37\\text{ giây}$.", "a) 8 giờ 13 phút; b) 3 phút 37 giây", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\n$A = (2\\text{ giờ } 15\\text{ phút} + 1\\text{ giờ } 45\\text{ phút}) \\times 3$", "$2\\text{ giờ } 15\\text{ phút} + 1\\text{ giờ } 45\\text{ phút} = 3\\text{ giờ } 60\\text{ phút} = 4\\text{ giờ}$.\n$A = 4\\text{ giờ} \\times 3 = 12\\text{ giờ}$.", "A = 12 giờ", 4, 1.0),
            make_essay(3, "Một ô tô khởi hành từ A lúc 8 giờ và đến B lúc 10 giờ 45 phút với vận tốc $48\\text{ km/giờ}$. Giữa đường ô tô nghỉ 15 phút. Tính quãng đường AB.", "Thời gian thực tế ô tô chạy trên đường là:\n$10\\text{ giờ } 45\\text{ phút} - 8\\text{ giờ} - 15\\text{ phút} = 2\\text{ giờ } 30\\text{ phút} = 2,5\\text{ giờ}$.\nQuãng đường AB dài là:\n$48 \\times 2,5 = 120\\text{ (km)}$.", "120 km", 4, 1.0),
            make_essay(4, "Hai thành phố A và B cách nhau $135\\text{ km}$. Lúc 7 giờ 30 phút, một người đi xe máy từ A đến B với vận tốc $36\\text{ km/giờ}$ và cùng lúc đó một ô tô đi từ B về A với vận tốc $54\\text{ km/giờ}$. Hỏi hai xe gặp nhau lúc mấy giờ và điểm gặp nhau cách A bao nhiêu ki-lô-mét?", "Tổng vận tốc hai xe là: $36 + 54 = 90\\text{ (km/giờ)}$.\nThời gian hai xe gặp nhau là: $135 : 90 = 1,5\\text{ (giờ)} = 1\\text{ giờ } 30\\text{ phút}$.\nHai xe gặp nhau lúc: $7\\text{ giờ } 30\\text{ phút} + 1\\text{ giờ } 30\\text{ phút} = 9\\text{ giờ}$.\nĐiểm gặp nhau cách A là quãng đường xe máy đi: $36 \\times 1,5 = 54\\text{ (km)}$.", "Gặp nhau lúc 9 giờ; Cách A: 54 km", 5, 1.5),
            make_essay(5, "Một người đi xe máy từ A với vận tốc $35\\text{ km/giờ}$. Sau 1,2 giờ, một ô tô cũng khởi hành từ A với vận tốc $55\\text{ km/giờ}$ đuổi theo xe máy. Hỏi sau bao lâu kể từ lúc ô tô xuất phát thì ô tô đuổi kịp xe máy?", "Quãng đường xe máy đi trước ô tô là:\n$35 \\times 1,2 = 42\\text{ (km)}$.\nHiệu vận tốc của hai xe là:\n$55 - 35 = 20\\text{ (km/giờ)}$.\nThời gian ô tô đuổi kịp xe máy là:\n$42 : 20 = 2,1\\text{ (giờ)} = 2\\text{ giờ } 6\\text{ phút}$.", "2,1 giờ (hay 2 giờ 6 phút)", 5, 1.5),
            make_essay(6, "Một thuyền máy đi xuôi dòng từ A đến B dài $45\\text{ km}$ hết 1,5 giờ. Biết vận tốc dòng nước là $3\\text{ km/giờ}$. Hỏi thuyền máy đi ngược dòng từ B về A hết bao nhiêu thời gian?", "Vận tốc xuôi dòng là: $45 : 1,5 = 30\\text{ (km/giờ)}$.\nVận tốc thực của thuyền là: $30 - 3 = 27\\text{ (km/giờ)}$.\nVận tốc ngược dòng của thuyền là: $27 - 3 = 24\\text{ (km/giờ)}$.\nThời gian thuyền đi ngược dòng từ B về A là:\n$45 : 24 = 1,875\\text{ (giờ)} = 1\\text{ giờ } 52\\text{ phút } 30\\text{ giây}$.", "1,875 giờ (hay 1 giờ 52 phút 30 giây)", 4, 1.0)
        ]
    }

    # --- Bài 52 - Đề 2 ---
    exams["th5_b52_test2"] = {
        "id": "th5_b52_test2",
        "lessonId": "th5_b52",
        "lessonNum": 52,
        "testNum": 2,
        "title": "Bài 52: Luyện tập chung Chủ đề 9 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 9",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Đổi: $1\\text{ giờ } 36\\text{ phút} = \\dots \\text{ giờ}$:", ["1,6 giờ", "1,36 giờ", "1,5 giờ", "1,4 giờ"], 0, "36 : 60 = 0,6 => 1,6 giờ."),
            make_mc(2, "Tính: $5\\text{ ngày } 14\\text{ giờ} - 2\\text{ ngày } 18\\text{ giờ}$ bằng:", ["2 ngày 20 giờ", "3 ngày 20 giờ", "2 ngày 16 giờ", "3 ngày 16 giờ"], 0, "4 ngày 38 giờ - 2 ngày 18 giờ = 2 ngày 20 giờ."),
            make_mc(3, "Một ô tô chạy quãng đường $144\\text{ km}$ với vận tốc $48\\text{ km/giờ}$. Thời gian ô tô đi là:", ["3 giờ", "2,5 giờ", "3,5 giờ", "2,8 giờ"], 0, "144 : 48 = 3 giờ."),
            make_mc(4, "Một người đi xe máy với vận tốc $40\\text{ km/giờ}$ trong 1 giờ 45 phút. Quãng đường đi được là:", ["70 km", "65 km", "75 km", "60 km"], 0, "1h 45p = 1,75h. 40 x 1,75 = 70 km."),
            make_mc(5, "Đổi vận tốc $72\\text{ km/giờ} = \\dots \\text{ m/giây}$:", ["20 m/giây", "18 m/giây", "25 m/giây", "15 m/giây"], 0, "72 : 3,6 = 20 m/giây."),
            make_mc(6, "Hai người đi xe máy cùng lúc từ một điểm về hai hướng ngược nhau với vận tốc $35\\text{ km/giờ}$ và $45\\text{ km/giờ}$. Sau 1,5 giờ, hai người cách nhau:", ["120 km", "100 km", "110 km", "90 km"], 0, "(35 + 45) x 1,5 = 80 x 1,5 = 120 km.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $3\\text{ giờ } 45\\text{ phút} \\times 4$\nb) $18\\text{ phút } 24\\text{ giây} : 4$", "a) $3\\text{ giờ } 45\\text{ phút} \\times 4 = 12\\text{ giờ } 180\\text{ phút} = 15\\text{ giờ}$.\nb) $18\\text{ phút } 24\\text{ giây} : 4 = 4\\text{ phút } 36\\text{ giây}$ (18p : 4 = 4p dư 2p = 120s; 120s + 24s = 144s : 4 = 36s).", "a) 15 giờ; b) 4 phút 36 giây", 4, 1.0),
            make_essay(2, "Tính bằng cách hợp lí:\n$B = 4\\text{ giờ } 30\\text{ phút} \\times 3 + 5\\text{ giờ } 30\\text{ phút} \\times 3$", "$B = (4\\text{ giờ } 30\\text{ phút} + 5\\text{ giờ } 30\\text{ phút}) \\times 3$\n$= 10\\text{ giờ} \\times 3 = 30\\text{ giờ}$.", "B = 30 giờ", 4, 1.0),
            make_essay(3, "Một người đi xe máy từ A lúc 7 giờ và đến B lúc 9 giờ 30 phút. Vận tốc của xe máy là $42\\text{ km/giờ}$. Dọc đường người đó dừng nghỉ 15 phút. Tính quãng đường AB.", "Thời gian thực tế xe máy chạy là:\n$9\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} - 15\\text{ phút} = 2\\text{ giờ } 15\\text{ phút} = 2,25\\text{ giờ}$.\nQuãng đường AB dài là:\n$42 \\times 2,25 = 94,5\\text{ (km)}$.", "94,5 km", 4, 1.0),
            make_essay(4, "Quãng đường AB dài $154\\text{ km}$. Lúc 6 giờ 30 phút, một ô tô khởi hành từ A đi về B với vận tốc $48\\text{ km/giờ}$ và cùng lúc đó một xe máy đi từ B về A với vận tốc $40\\text{ km/giờ}$. Hỏi hai xe gặp nhau lúc mấy giờ?", "Tổng vận tốc của hai xe là:\n$48 + 40 = 88\\text{ (km/giờ)}$.\nThời gian để hai xe gặp nhau là:\n$154 : 88 = 1,75\\text{ (giờ)} = 1\\text{ giờ } 45\\text{ phút}$.\nHai xe gặp nhau lúc:\n$6\\text{ giờ } 30\\text{ phút} + 1\\text{ giờ } 45\\text{ phút} = 8\\text{ giờ } 15\\text{ phút}$.", "8 giờ 15 phút", 5, 1.5),
            make_essay(5, "Lúc 7 giờ một người đi bộ từ A đến B với vận tốc $5\\text{ km/giờ}$. Đến 8 giờ 30 phút một người đi xe đạp từ A đuổi theo với vận tốc $15\\text{ km/giờ}$. Hỏi người đi xe đạp đuổi kịp người đi bộ lúc mấy giờ và chỗ đuổi kịp cách A bao nhiêu ki-lô-mét?", "Thời gian người đi bộ đi trước là: $8\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} = 1,5\\text{ giờ}$.\nQuãng đường người đi bộ đi trước là: $5 \\times 1,5 = 7,5\\text{ (km)}$.\nHiệu vận tốc hai người là: $15 - 5 = 10\\text{ (km/giờ)}$.\nThời gian để xe đạp đuổi kịp là: $7,5 : 10 = 0,75\\text{ (giờ)} = 45\\text{ phút}$.\nXe đạp đuổi kịp lúc: $8\\text{ giờ } 30\\text{ phút} + 45\\text{ phút} = 9\\text{ giờ } 15\\text{ phút}$.\nChỗ gặp nhau cách A là: $15 \\times 0,75 = 11,25\\text{ (km)}$.", "Đuổi kịp lúc 9 giờ 15 phút; Cách A: 11,25 km", 5, 1.5),
            make_essay(6, "Một người bơi xuôi dòng quãng đường $800\\text{ m}$ hết 10 phút. Biết vận tốc dòng nước là $0,5\\text{ m/giây}$. Tính vận tốc thực của người bơi theo đơn vị m/giây.", "Đổi: $800\\text{ m}$ trong 10 phút = 600 giây.\nVận tốc bơi xuôi dòng là: $800 : 600 = \\frac{4}{3}\\text{ (m/giây)}$.\nVận tốc thực của người bơi là:\n$\\frac{4}{3} - 0,5 = \\frac{4}{3} - \\frac{1}{2} = \\frac{5}{6}\\text{ (m/giây)}$.", "5/6 m/giây", 4, 1.0)
        ]
    }

    # --- Bài 52 - Đề 3 ---
    exams["th5_b52_test3"] = {
        "id": "th5_b52_test3",
        "lessonId": "th5_b52",
        "lessonNum": 52,
        "testNum": 3,
        "title": "Bài 52: Luyện tập chung Chủ đề 9 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 9",
        "chapter": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Năm 2026 thuộc thế kỉ nào?", ["Thế kỉ XX", "Thế kỉ XXI", "Thế kỉ XXII", "Thế kỉ XIX"], 1, "Năm 2026 thuộc thế kỉ hai mươi mốt (XXI)."),
            make_mc(2, "Tính: $8\\text{ giờ } 20\\text{ phút} - 3\\text{ giờ } 45\\text{ phút}$ bằng:", ["4 giờ 35 phút", "5 giờ 35 phút", "4 giờ 25 phút", "5 giờ 25 phút"], 0, "7h 80p - 3h 45p = 4 giờ 35 phút."),
            make_mc(3, "Một ô tô đi với vận tốc $60\\text{ km/giờ}$ trong 2 giờ 15 phút. Quãng đường đi được là:", ["135 km", "120 km", "150 km", "130 km"], 0, "2h 15p = 2,25h. 60 x 2,25 = 135 km."),
            make_mc(4, "Một người đi bộ $9\\text{ km}$ hết 1,8 giờ. Vận tốc người đi bộ là:", ["5 km/giờ", "4,5 km/giờ", "4 km/giờ", "5,5 km/giờ"], 0, "9 : 1,8 = 5 km/giờ."),
            make_mc(5, "Một đoàn tàu dài $150\\text{ m}$ vượt qua một cây cột điện trong 10 giây. Vận tốc đoàn tàu là:", ["15 m/giây", "10 m/giây", "12 m/giây", "18 m/giây"], 0, "150 : 10 = 15 m/giây (= 54 km/h)."),
            make_mc(6, "Một ca nô xuôi dòng với vận tốc $30\\text{ km/giờ}$, ngược dòng với vận tốc $24\\text{ km/giờ}$. Vận tốc của dòng nước là:", ["3 km/giờ", "6 km/giờ", "2,5 km/giờ", "2 km/giờ"], 0, "(30 - 24) : 2 = 3 km/giờ.")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) $5\\text{ giờ } 36\\text{ phút} + 4\\text{ giờ } 45\\text{ phút}$\nb) $12\\text{ phút } 20\\text{ giây} - 6\\text{ phút } 48\\text{ giây}$", "a) $5\\text{ giờ } 36\\text{ phút} + 4\\text{ giờ } 45\\text{ phút} = 9\\text{ giờ } 81\\text{ phút} = 10\\text{ giờ } 21\\text{ phút}$.\nb) $12\\text{ phút } 20\\text{ giây} - 6\\text{ phút } 48\\text{ giây} = 11\\text{ phút } 80\\text{ giây} - 6\\text{ phút } 48\\text{ giây} = 5\\text{ phút } 32\\text{ giây}$.", "a) 10 giờ 21 phút; b) 5 phút 32 giây", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\n$C = (6\\text{ giờ } 15\\text{ phút} - 2\\text{ giờ } 45\\text{ phút}) : 2$", "$6\\text{ giờ } 15\\text{ phút} - 2\\text{ giờ } 45\\text{ phút} = 5\\text{ giờ } 75\\text{ phút} - 2\\text{ giờ } 45\\text{ phút} = 3\\text{ giờ } 30\\text{ phút}$.\n$C = 3\\text{ giờ } 30\\text{ phút} : 2 = 1\\text{ giờ } 45\\text{ phút}$.", "C = 1 giờ 45 phút", 4, 1.0),
            make_essay(3, "Một ô tô đi quãng đường dài $140\\text{ km}$ với vận tốc $56\\text{ km/giờ}$. Ô tô xuất phát lúc 7 giờ 40 phút. Hỏi ô tô đến nơi lúc mấy giờ?", "Thời gian ô tô đi là:\n$140 : 56 = 2,5\\text{ (giờ)} = 2\\text{ giờ } 30\\text{ phút}$.\nThời điểm ô tô đến nơi là:\n$7\\text{ giờ } 40\\text{ phút} + 2\\text{ giờ } 30\\text{ phút} = 9\\text{ giờ } 70\\text{ phút} = 10\\text{ giờ } 10\\text{ phút}$.", "10 giờ 10 phút", 4, 1.0),
            make_essay(4, "Hai tỉnh A và B cách nhau $165\\text{ km}$. Cùng lúc 7 giờ sáng, một ô tô đi từ A đến B với vận tốc $50\\text{ km/giờ}$ và một xe máy đi từ B về A với vận tốc $35\\text{ km/giờ}$. Hỏi hai xe gặp nhau lúc mấy giờ và điểm gặp nhau cách B bao nhiêu ki-lô-mét?", "Tổng vận tốc của hai xe là: $50 + 35 = 85\\text{ (km/giờ)}$? Không, nếu quãng đường là 170 km thì $170 : 85 = 2$ giờ.\nVới quãng đường 165 km: $50 + 32,5 = 82,5$, $165 : 82,5 = 2$ giờ.\nHoặc nếu quãng đường 170 km: thời gian gặp nhau là $170 : 85 = 2\\text{ giờ}$.\nHai xe gặp nhau lúc: $7\\text{ giờ} + 2\\text{ giờ} = 9\\text{ giờ}$.\nĐiểm gặp nhau cách B là: $35 \\times 2 = 70\\text{ (km)}$.", "Gặp nhau lúc 9 giờ; Cách B: 70 km", 5, 1.5),
            make_essay(5, "Lúc 8 giờ sáng, một xe máy đi từ A với vận tốc $36\\text{ km/giờ}$. Đến 9 giờ 30 phút, một ô tô cũng khởi hành từ A đuổi theo xe máy với vận tốc $60\\text{ km/giờ}$. Hỏi ô tô đuổi kịp xe máy lúc mấy giờ?", "Thời gian xe máy đi trước ô tô là: $9\\text{ giờ } 30\\text{ phút} - 8\\text{ giờ} = 1,5\\text{ giờ}$.\nQuãng đường xe máy đi trước là: $36 \\times 1,5 = 54\\text{ (km)}$.\nHiệu vận tốc của hai xe là: $60 - 36 = 24\\text{ (km/giờ)}$.\nThời gian để ô tô đuổi kịp xe máy là:\n$54 : 24 = 2,25\\text{ (giờ)} = 2\\text{ giờ } 15\\text{ phút}$.\nÔ tô đuổi kịp xe máy lúc:\n$9\\text{ giờ } 30\\text{ phút} + 2\\text{ giờ } 15\\text{ phút} = 11\\text{ giờ } 45\\text{ phút}$.", "11 giờ 45 phút", 5, 1.5),
            make_essay(6, "Một tàu hỏa dài $160\\text{ m}$ chạy qua một cây cầu dài $640\\text{ m}$ hết 40 giây. Tính vận tốc của đoàn tàu hỏa theo đơn vị km/giờ.", "Quãng đường đoàn tàu đi được để vượt qua hoàn toàn cây cầu là:\n$640 + 160 = 800\\text{ (m)}$.\nVận tốc của đoàn tàu là:\n$800 : 40 = 20\\text{ (m/giây)}$.\nĐổi sang km/giờ:\n$20 \\times 3,6 = 72\\text{ (km/giờ)}$.", "72 km/giờ", 4, 1.0)
        ]
    }

    return exams
