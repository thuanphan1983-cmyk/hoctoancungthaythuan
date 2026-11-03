# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 2: SỐ THẬP PHÂN (BÀI 12 ĐẾN BÀI 14) - TOÁN 5 KNTT
Mỗi bài có đúng 3 đề kiểm tra độc lập (test1, test2, test3):
- 6 câu trắc nghiệm (part1, mỗi câu 0.5 điểm = 3.0 điểm)
- 6 câu tự luận (part2, 4 câu 1.0 đ + 2 câu 1.5 đ = 7.0 điểm, lineCount: 3 đến 6 dòng)
Tổng điểm: 10.0 điểm, thời gian: 35 phút.
"""
from th5_ch1_part1 import make_mc, make_essay

def get_ch2_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 12: VIẾT SỐ ĐO ĐẠI LƯỢNG DƯỚI DẠNG SỐ THẬP PHÂN
    # =========================================================================
    # --- Bài 12 - Đề 1 ---
    exams["th5_b12_test1"] = {
        "id": "th5_b12_test1",
        "lessonId": "th5_b12",
        "lessonNum": 12,
        "testNum": 1,
        "title": "Bài 12: Viết số đo đại lượng dưới dạng số thập phân - Đề số 1",
        "topic": "Viết số đo đại lượng dưới dạng số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm: $4\\text{ m } 7\\text{ dm} = \\dots \\text{ m}$ là:", ["4,7", "4,07", "47", "0,47"], 0, "7 dm = 0,7 m nên 4 m 7 dm = 4,7 m."),
            make_mc(2, "Viết số đo $3\\text{ kg } 250\\text{ g}$ dưới dạng số thập phân với đơn vị ki-lô-gam là:", ["3,25", "3,025", "3,250", "32,5"], 0, "250 g = 0,25 kg nên 3 kg 250 g = 3,25 kg."),
            make_mc(3, "Số thích hợp điền vào chỗ chấm: $5\\text{ m}^2\\ 8\\text{ dm}^2 = \\dots \\text{ m}^2$ là:", ["5,8", "5,08", "5,008", "58"], 1, "1 m$^2$ = 100 dm$^2$ nên 8 dm$^2$ = 0,08 m$^2$ => 5,08 m$^2$."),
            make_mc(4, "Viết số đo $7\\text{ km } 35\\text{ m}$ dưới dạng số thập phân có đơn vị ki-lô-mét là:", ["7,35", "7,035", "7,350", "73,5"], 1, "35 m = 35/1000 km = 0,035 km => 7,035 km."),
            make_mc(5, "Đổi $2\\text{ tấn } 50\\text{ kg} = \\dots \\text{ tấn}$:", ["2,5", "2,05", "2,005", "25"], 1, "50 kg = 50/1000 tấn = 0,05 tấn => 2,05 tấn."),
            make_mc(6, "Diện tích $4\\text{ ha}$ bằng bao nhiêu ki-lô-mét vuông?", ["0,4 km$^2$", "0,04 km$^2$", "40 km$^2$", "400 km$^2$"], 1, "1 km$^2$ = 100 ha nên 4 ha = 4/100 km$^2$ = 0,04 km$^2$.")
        ],
        "part2": [
            make_essay(1, "Viết số thập phân thích hợp vào chỗ chấm:\na) $8\\text{ m } 5\\text{ cm} = \\dots \\text{ m}$\nb) $3\\text{ km } 450\\text{ m} = \\dots \\text{ km}$\nc) $6\\text{ tấn } 8\\text{ tạ} = \\dots \\text{ tấn}$\nd) $25\\text{ kg } 75\\text{ g} = \\dots \\text{ kg}$", "a) $8\\text{ m } 5\\text{ cm} = 8,05\\text{ m}$\nb) $3\\text{ km } 450\\text{ m} = 3,45\\text{ km}$\nc) $6\\text{ tấn } 8\\text{ tạ} = 6,8\\text{ tấn}$\nd) $25\\text{ kg } 75\\text{ g} = 25,075\\text{ kg}$", "a) 8,05; b) 3,45; c) 6,8; d) 25,075", 4, 1.0),
            make_essay(2, "Viết số thập phân thích hợp vào chỗ chấm:\na) $4\\text{ m}^2\\ 35\\text{ dm}^2 = \\dots \\text{ m}^2$\nb) $7\\text{ dm}^2\\ 6\\text{ cm}^2 = \\dots \\text{ dm}^2$\nc) $15\\text{ ha} = \\dots \\text{ km}^2$\nd) $250\\text{ m}^2 = \\dots \\text{ ha}$", "a) $4\\text{ m}^2\\ 35\\text{ dm}^2 = 4,35\\text{ m}^2$\nb) $7\\text{ dm}^2\\ 6\\text{ cm}^2 = 7,06\\text{ dm}^2$\nc) $15\\text{ ha} = 0,15\\text{ km}^2$\nd) $250\\text{ m}^2 = 0,025\\text{ ha}$", "a) 4,35; b) 7,06; c) 0,15; d) 0,025", 4, 1.0),
            make_essay(3, "Viết các số đo sau dưới dạng số đo có đơn vị là mét vuông:\na) $8\\text{ ha}$\nb) $2,5\\text{ km}^2$", "a) $8\\text{ ha} = 8 \\times 10 000 = 80 000\\text{ m}^2$.\nb) $2,5\\text{ km}^2 = 2,5 \\times 1 000 000 = 2 500 000\\text{ m}^2$.", "a) 80 000 m$^2$; b) 2 500 000 m$^2$", 3, 1.0),
            make_essay(4, "Một cuộn dây điện dài $50\\text{ m}$. Người thợ đã cắt lấy 3 đoạn, mỗi đoạn dài $4\\text{ m } 25\\text{ cm}$. Hỏi cuộn dây điện đó còn lại bao nhiêu mét?", "Đổi: $4\\text{ m } 25\\text{ cm} = 4,25\\text{ m}$.\nTổng chiều dài 3 đoạn dây đã cắt là: $4,25 \\times 3 = 12,75\\text{ (m)}$.\nCuộn dây điện còn lại số mét là:\n$50 - 12,75 = 37,25\\text{ (m)}$.", "37,25 m", 4, 1.0),
            make_essay(5, "Một ô tô chở hàng, xe thứ nhất chở được $3\\text{ tấn } 500\\text{ kg}$, xe thứ hai chở được nhiều hơn xe thứ nhất $4\\text{ tạ}$. Hỏi cả hai xe chở được bao nhiêu tấn hàng?", "Đổi sang đơn vị tấn:\n$3\\text{ tấn } 500\\text{ kg} = 3,5\\text{ tấn}$.\n$4\\text{ tạ} = 0,4\\text{ tấn}$.\nXe thứ hai chở được: $3,5 + 0,4 = 3,9\\text{ (tấn)}$.\nCả hai xe chở được tất cả:\n$3,5 + 3,9 = 7,4\\text{ (tấn)}$.", "7,4 tấn hàng", 5, 1.5),
            make_essay(6, "Một thửa ruộng hình chữ nhật có chiều dài $120\\text{ m}$, chiều rộng $80\\text{ m}$. Hỏi diện tích thửa ruộng đó bằng bao nhiêu mét vuông? Bằng bao nhiêu héc-ta?", "Diện tích thửa ruộng là:\n$120 \\times 80 = 9 600\\text{ (m$^2$)}$.\nĐổi sang héc-ta ($1\\text{ ha} = 10 000\\text{ m}^2$):\n$9 600 : 10 000 = 0,96\\text{ (ha)}$.", "9 600 m$^2$; 0,96 ha", 4, 1.5)
        ]
    }

    # --- Bài 12 - Đề 2 ---
    exams["th5_b12_test2"] = {
        "id": "th5_b12_test2",
        "lessonId": "th5_b12",
        "lessonNum": 12,
        "testNum": 2,
        "title": "Bài 12: Viết số đo đại lượng dưới dạng số thập phân - Đề số 2",
        "topic": "Viết số đo đại lượng dưới dạng số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Viết số đo $9\\text{ dm } 4\\text{ cm}$ dưới dạng số thập phân với đơn vị đề-xi-mét là:", ["9,4 dm", "9,04 dm", "94 dm", "0,94 dm"], 0, "4 cm = 0,4 dm nên 9 dm 4 cm = 9,4 dm."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $6\\text{ kg } 50\\text{ g} = \\dots \\text{ kg}$ là:", ["6,5", "6,05", "6,005", "65"], 1, "50 g = 0,05 kg nên bằng 6,05 kg."),
            make_mc(3, "Đổi $3\\text{ m}^2\\ 450\\text{ cm}^2 = \\dots \\text{ m}^2$:", ["3,45", "3,045", "3,450", "34,5"], 1, "1 m$^2$ = 10 000 cm$^2$ nên 450 cm$^2$ = 0,045 m$^2$ => 3,045 m$^2$."),
            make_mc(4, "Viết số đo $5\\text{ km } 8\\text{ m}$ dưới dạng số thập phân có đơn vị ki-lô-mét là:", ["5,8 km", "5,08 km", "5,008 km", "58 km"], 2, "8 m = 0,008 km nên bằng 5,008 km."),
            make_mc(5, "Đổi $4\\text{ tấn } 8\\text{ tạ} = \\dots \\text{ tấn}$:", ["4,8", "4,08", "48", "0,48"], 0, "8 tạ = 0,8 tấn nên bằng 4,8 tấn."),
            make_mc(6, "Diện tích một sân vận động là $12 500\\text{ m}^2$. Viết số đo này theo đơn vị héc-ta là:", ["1,25 ha", "12,5 ha", "0,125 ha", "125 ha"], 0, "12 500 : 10 000 = 1,25 ha.")
        ],
        "part2": [
            make_essay(1, "Viết số thập phân thích hợp vào chỗ chấm:\na) $15\\text{ m } 8\\text{ dm} = \\dots \\text{ m}$\nb) $4\\text{ km } 75\\text{ m} = \\dots \\text{ km}$\nc) $8\\text{ tạ } 5\\text{ kg} = \\dots \\text{ tạ}$\nd) $9\\text{ kg } 800\\text{ g} = \\dots \\text{ kg}$", "a) $15\\text{ m } 8\\text{ dm} = 15,8\\text{ m}$\nb) $4\\text{ km } 75\\text{ m} = 4,075\\text{ km}$\nc) $8\\text{ tạ } 5\\text{ kg} = 8,05\\text{ tạ}$\nd) $9\\text{ kg } 800\\text{ g} = 9,8\\text{ kg}$", "a) 15,8; b) 4,075; c) 8,05; d) 9,8", 4, 1.0),
            make_essay(2, "Viết số thập phân thích hợp vào chỗ chấm:\na) $9\\text{ m}^2\\ 75\\text{ dm}^2 = \\dots \\text{ m}^2$\nb) $3\\text{ dm}^2\\ 8\\text{ cm}^2 = \\dots \\text{ dm}^2$\nc) $45\\text{ ha} = \\dots \\text{ km}^2$\nd) $3 500\\text{ m}^2 = \\dots \\text{ ha}$", "a) $9\\text{ m}^2\\ 75\\text{ dm}^2 = 9,75\\text{ m}^2$\nb) $3\\text{ dm}^2\\ 8\\text{ cm}^2 = 3,08\\text{ dm}^2$\nc) $45\\text{ ha} = 0,45\\text{ km}^2$\nd) $3 500\\text{ m}^2 = 0,35\\text{ ha}$", "a) 9,75; b) 3,08; c) 0,45; d) 0,35", 4, 1.0),
            make_essay(3, "So sánh hai số đo sau:\na) $4\\text{ m } 5\\text{ dm} \\dots 4,05\\text{ m}$\nb) $2\\text{ tấn } 50\\text{ kg} \\dots 2,5\\text{ tấn}$", "a) $4\\text{ m } 5\\text{ dm} = 4,5\\text{ m}$. Vì $4,5 > 4,05$ nên $4\\text{ m } 5\\text{ dm} > 4,05\\text{ m}$.\nb) $2\\text{ tấn } 50\\text{ kg} = 2,05\\text{ tấn}$. Vì $2,05 < 2,5$ nên $2\\text{ tấn } 50\\text{ kg} < 2,5\\text{ tấn}$.", "a) >; b) <", 4, 1.0),
            make_essay(4, "Một người thợ may dùng một tấm vải dài $15\\text{ m}$ để may quần áo. May một cái áo hết $1\\text{ m } 80\\text{ cm}$, may một cái quần hết $1\\text{ m } 20\\text{ cm}$. Hỏi người đó may được bao nhiêu bộ quần áo như thế?", "Đổi: $1\\text{ m } 80\\text{ cm} = 1,8\\text{ m}$; $1\\text{ m } 20\\text{ cm} = 1,2\\text{ m}$.\nĐể may một bộ quần áo cần số mét vải là:\n$1,8 + 1,2 = 3\\text{ (m)}$.\nSố bộ quần áo người đó may được là:\n$15 : 3 = 5$ (bộ quần áo).", "5 bộ quần áo", 4, 1.0),
            make_essay(5, "Một khu đất hình chữ nhật có chiều dài $250\\text{ m}$, chiều rộng bằng $\\frac{3}{5}$ chiều dài. Tính diện tích khu đất đó theo đơn vị mét vuông và theo đơn vị héc-ta.", "Chiều rộng khu đất là: $250 \\times \\frac{3}{5} = 150\\text{ (m)}$.\nDiện tích khu đất là: $250 \\times 150 = 37 500\\text{ (m$^2$)}$.\nĐổi sang héc-ta: $37 500 : 10 000 = 3,75\\text{ (ha)}$.", "37 500 m$^2$; 3,75 ha", 4, 1.5),
            make_essay(6, "Bác Năm thu hoạch rau trên một thửa ruộng hình bình hành có đáy dài $60\\text{ m}$, chiều cao bằng $45\\text{ m}$. Trung bình mỗi mét vuông bác thu được $2,5\\text{ kg}$ rau. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tấn rau?", "Diện tích thửa ruộng hình bình hành là:\n$60 \\times 45 = 2 700\\text{ (m$^2$)}$.\nKhối lượng rau thu hoạch được là:\n$2 700 \\times 2,5 = 6 750\\text{ (kg)}$.\nĐổi sang đơn vị tấn: $6 750\\text{ kg} = 6,75\\text{ tấn rau}$.", "6,75 tấn rau", 5, 1.5)
        ]
    }

    # --- Bài 12 - Đề 3 ---
    exams["th5_b12_test3"] = {
        "id": "th5_b12_test3",
        "lessonId": "th5_b12",
        "lessonNum": 12,
        "testNum": 3,
        "title": "Bài 12: Viết số đo đại lượng dưới dạng số thập phân - Đề số 3",
        "topic": "Viết số đo đại lượng dưới dạng số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thích hợp điền vào chỗ chấm: $75\\text{ cm} = \\dots \\text{ m}$ là:", ["7,5", "0,75", "0,075", "75"], 1, "75 cm = 75/100 m = 0,75 m."),
            make_mc(2, "Viết số đo $8\\text{ kg } 5\\text{ g}$ dưới dạng số thập phân có đơn vị ki-lô-gam là:", ["8,5 kg", "8,05 kg", "8,005 kg", "85 kg"], 2, "5 g = 0,005 kg nên bằng 8,005 kg."),
            make_mc(3, "Đổi $2\\text{ m}^2\\ 4\\text{ dm}^2 = \\dots \\text{ m}^2$:", ["2,4", "2,04", "2,004", "24"], 1, "4 dm$^2$ = 0,04 m$^2$ nên bằng 2,04 m$^2$."),
            make_mc(4, "Một bao gạo nặng $50\\text{ kg}$, viết khối lượng đó theo đơn vị tạ là:", ["5 tạ", "0,5 tạ", "0,05 tạ", "500 tạ"], 1, "1 tạ = 100 kg nên 50 kg = 0,5 tạ."),
            make_mc(5, "Đổi $12\\text{ km } 60\\text{ m} = \\dots \\text{ km}$:", ["12,6", "12,06", "12,006", "126"], 1, "60 m = 0,06 km nên bằng 12,06 km."),
            make_mc(6, "Diện tích $0,8\\text{ ha}$ bằng bao nhiêu mét vuông?", ["80 m$^2$", "800 m$^2$", "8 000 m$^2$", "80 000 m$^2$"], 2, "0,8 x 10 000 = 8 000 m$^2$.")
        ],
        "part2": [
            make_essay(1, "Viết số thập phân thích hợp vào chỗ chấm:\na) $2\\text{ m } 75\\text{ mm} = \\dots \\text{ m}$\nb) $5\\text{ tấn } 65\\text{ kg} = \\dots \\text{ tấn}$\nc) $12\\text{ m}^2\\ 9\\text{ dm}^2 = \\dots \\text{ m}^2$\nd) $4\\text{ ha } 500\\text{ m}^2 = \\dots \\text{ ha}$", "a) $2\\text{ m } 75\\text{ mm} = 2,075\\text{ m}$\nb) $5\\text{ tấn } 65\\text{ kg} = 5,065\\text{ tấn}$\nc) $12\\text{ m}^2\\ 9\\text{ dm}^2 = 12,09\\text{ m}^2$\nd) $4\\text{ ha } 500\\text{ m}^2 = 4,05\\text{ ha}$", "a) 2,075; b) 5,065; c) 12,09; d) 4,05", 4, 1.0),
            make_essay(2, "Sắp xếp các số đo sau theo thứ tự từ bé đến lớn:\n$3,5\\text{ km}$; $3\\text{ km } 450\\text{ m}$; $3 600\\text{ m}$; $3,08\\text{ km}$.", "Đổi các số đo về cùng đơn vị ki-lô-mét:\n$3\\text{ km } 450\\text{ m} = 3,45\\text{ km}$; $3 600\\text{ m} = 3,6\\text{ km}$.\nSo sánh: $3,08 < 3,45 < 3,5 < 3,6$.\nVậy thứ tự từ bé đến lớn là: $3,08\\text{ km}$; $3\\text{ km } 450\\text{ m}$; $3,5\\text{ km}$; $3 600\\text{ m}$.", "3,08 km; 3 km 450 m; 3,5 km; 3 600 m", 4, 1.0),
            make_essay(3, "Viết số đo thích hợp vào chỗ chấm dưới dạng số tự nhiên:\na) $4,5\\text{ tấn} = \\dots \\text{ kg}$\nb) $0,75\\text{ ha} = \\dots \\text{ m}^2$\nc) $1,25\\text{ m} = \\dots \\text{ cm}$", "a) $4,5 \\times 1 000 = 4 500\\text{ kg}$\nb) $0,75 \\times 10 000 = 7 500\\text{ m}^2$\nc) $1,25 \\times 100 = 125\\text{ cm}$", "a) 4 500; b) 7 500; c) 125", 3, 1.0),
            make_essay(4, "Một đoàn xe chở hàng có 4 xe tải, mỗi xe chở được $2\\text{ tấn } 250\\text{ kg}$ gạo. Hỏi cả đoàn xe chở được tất cả bao nhiêu tấn gạo?", "Đổi: $2\\text{ tấn } 250\\text{ kg} = 2,25\\text{ tấn}$.\nCả đoàn xe chở được số tấn gạo là:\n$2,25 \\times 4 = 9\\text{ (tấn)}$.", "9 tấn gạo", 3, 1.0),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chiều rộng $40\\text{ m}$, chiều dài gấp rưỡi chiều rộng. Tính diện tích mảnh vườn đó theo đơn vị mét vuông và theo đơn vị héc-ta.", "Gấp rưỡi nghĩa là gấp 1,5 lần (hay bằng 3/2).\nChiều dài mảnh vườn là: $40 \\times 1,5 = 60\\text{ (m)}$.\nDiện tích mảnh vườn là: $60 \\times 40 = 2 400\\text{ (m$^2$)}$.\nĐổi sang héc-ta: $2 400 : 10 000 = 0,24\\text{ (ha)}$.", "2 400 m$^2$; 0,24 ha", 4, 1.5),
            make_essay(6, "Bác An có một thửa đất hình thang vuông có đáy lớn $40\\text{ m}$, đáy bé $25\\text{ m}$ và chiều cao $20\\text{ m}$. Bác dành $35\\%$ diện tích để làm nhà, phần còn lại trồng cây ăn quả. Tính diện tích phần đất trồng cây ăn quả theo đơn vị mét vuông và héc-ta.", "Diện tích thửa đất hình thang là:\n$(40 + 25) \\times 20 : 2 = 650\\text{ (m$^2$)}$.\nPhần đất trồng cây ăn quả chiếm: $100\\% - 35\\% = 65\\%$ diện tích thửa đất.\nDiện tích trồng cây ăn quả là:\n$650 \\times 65 : 100 = 422,5\\text{ (m$^2$)}$.\nĐổi sang héc-ta: $422,5 : 10 000 = 0,04225\\text{ (ha)}$.", "422,5 m$^2$ (hoặc 0,04225 ha)", 5, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 13: LÀM TRÒN SỐ THẬP PHÂN
    # =========================================================================
    # --- Bài 13 - Đề 1 ---
    exams["th5_b13_test1"] = {
        "id": "th5_b13_test1",
        "lessonId": "th5_b13",
        "lessonNum": 13,
        "testNum": 1,
        "title": "Bài 13: Làm tròn số thập phân - Đề số 1",
        "topic": "Làm tròn số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Làm tròn số 4,7 đến hàng đơn vị ta được số:", ["4", "5", "4,8", "4,0"], 1, "Chữ số hàng phần mười là 7 >= 5 nên làm tròn lên 5."),
            make_mc(2, "Làm tròn số 12,34 đến hàng phần mười (chữ số thập phân thứ nhất) ta được số:", ["12,3", "12,4", "12", "12,30"], 0, "Chữ số hàng phần trăm là 4 < 5 nên giữ nguyên 12,3."),
            make_mc(3, "Làm tròn số 8,568 đến hàng phần trăm (chữ số thập phân thứ hai) ta được số:", ["8,56", "8,57", "8,6", "8,50"], 1, "Chữ số hàng phần nghìn là 8 >= 5 nên làm tròn lên 8,57."),
            make_mc(4, "Một bao gạo cân nặng 49,6 kg. Làm tròn khối lượng này đến hàng đơn vị là:", ["49 kg", "50 kg", "49,5 kg", "51 kg"], 1, "49,6 làm tròn đến hàng đơn vị thành 50 kg."),
            make_mc(5, "Số thập phân nào dưới đây khi làm tròn đến hàng phần mười thì được số 7,5?", ["7,44", "7,56", "7,48", "7,59"], 2, "7,48 có hàng phần trăm là 8 >= 5 nên làm tròn lên 7,5."),
            make_mc(6, "Làm tròn số 125,094 đến hàng phần mười ta được:", ["125", "125,1", "125,0", "125,09"], 1, "Chữ số hàng phần trăm là 9 >= 5 nên làm tròn lên 125,1.")
        ],
        "part2": [
            make_essay(1, "Làm tròn các số thập phân sau đến hàng đơn vị:\na) 6,38\nb) 19,75\nc) 104,52\nd) 0,89", "a) Chữ số hàng phần mười là 3 < 5 $\\Rightarrow$ làm tròn thành 6.\nb) Chữ số hàng phần mười là 7 >= 5 $\\Rightarrow$ làm tròn thành 20.\nc) Chữ số hàng phần mười là 5 >= 5 $\\Rightarrow$ làm tròn thành 105.\nd) Chữ số hàng phần mười là 8 >= 5 $\\Rightarrow$ làm tròn thành 1.", "a) 6; b) 20; c) 105; d) 1", 4, 1.0),
            make_essay(2, "Làm tròn các số thập phân sau đến hàng phần mười:\na) 4,26\nb) 15,83\nc) 0,97\nd) 7,049", "a) Hàng phần trăm 6 >= 5 $\\Rightarrow 4,3$.\nb) Hàng phần trăm 3 < 5 $\\Rightarrow 15,8$.\nc) Hàng phần trăm 7 >= 5 $\\Rightarrow 1,0$.\nd) Hàng phần trăm 4 < 5 $\\Rightarrow 7,0$.", "a) 4,3; b) 15,8; c) 1,0; d) 7,0", 4, 1.0),
            make_essay(3, "Làm tròn các số sau đến hàng phần trăm:\na) 5,638\nb) 12,404\nc) 9,996", "a) Hàng phần nghìn 8 >= 5 $\\Rightarrow 5,64$.\nb) Hàng phần nghìn 4 < 5 $\\Rightarrow 12,40$.\nc) Hàng phần nghìn 6 >= 5 $\\Rightarrow 10,00$.", "a) 5,64; b) 12,40; c) 10,00", 3, 1.0),
            make_essay(4, "Một vận động viên nhảy xa đạt thành tích $6,74\\text{ m}$. Hãy làm tròn thành tích này:\na) Đến hàng phần mười;\nb) Đến hàng đơn vị.", "a) Làm tròn đến hàng phần mười: chữ số hàng phần trăm là 4 < 5 nên ta được $6,7\\text{ m}$.\nb) Làm tròn đến hàng đơn vị: chữ số hàng phần mười là 7 >= 5 nên ta được $7\\text{ m}$.", "a) 6,7 m; b) 7 m", 3, 1.0),
            make_essay(5, "Biết cân nặng của 3 bạn học sinh lần lượt là: $34,8\\text{ kg}$; $36,25\\text{ kg}$ và $35,4\\text{ kg}$.\na) Hãy tính tổng cân nặng của cả 3 bạn.\nb) Làm tròn tổng cân nặng tìm được đến hàng đơn vị.", "a) Tổng cân nặng của cả 3 bạn là:\n$34,8 + 36,25 + 35,4 = 106,45\\text{ (kg)}$.\nb) Làm tròn số 106,45 đến hàng đơn vị:\nChữ số hàng phần mười là 4 < 5 nên ta được $106\\text{ kg}$.", "a) 106,45 kg; b) 106 kg", 4, 1.5),
            make_essay(6, "Tìm tất cả các chữ số $x$ thích hợp để khi làm tròn số thập phân $8,4x7$ đến hàng phần mười thì ta được số 8,5.", "Để làm tròn số $8,4x7$ đến hàng phần mười được 8,5 thì chữ số hàng phần trăm $x$ phải lớn hơn hoặc bằng 5.\nDo đó $x \\in \\{5; 6; 7; 8; 9\\}$.", "x = 5; 6; 7; 8; 9", 3, 1.5)
        ]
    }

    # --- Bài 13 - Đề 2 ---
    exams["th5_b13_test2"] = {
        "id": "th5_b13_test2",
        "lessonId": "th5_b13",
        "lessonNum": 13,
        "testNum": 2,
        "title": "Bài 13: Làm tròn số thập phân - Đề số 2",
        "topic": "Làm tròn số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Làm tròn số 8,42 đến hàng đơn vị ta được:", ["8", "9", "8,4", "8,0"], 0, "Chữ số hàng phần mười là 4 < 5 nên làm tròn thành 8."),
            make_mc(2, "Làm tròn số 25,67 đến hàng phần mười ta được:", ["25,6", "25,7", "26", "25,60"], 1, "Chữ số hàng phần trăm là 7 >= 5 nên làm tròn lên 25,7."),
            make_mc(3, "Làm tròn số 3,1415 đến hàng phần trăm (chữ số thập phân thứ hai) ta được:", ["3,14", "3,15", "3,1", "3,142"], 0, "Chữ số hàng phần nghìn là 1 < 5 nên làm tròn thành 3,14."),
            make_mc(4, "Một chai nước khoáng có dung tích 1,48 lít. Làm tròn dung tích này đến hàng phần mười là:", ["1,4 lít", "1,5 lít", "1 lít", "2 lít"], 1, "1,48 làm tròn đến hàng phần mười thành 1,5 lít."),
            make_mc(5, "Số thập phân nào sau đây khi làm tròn đến hàng đơn vị thì được số 15?", ["14,35", "14,82", "15,65", "15,8"], 1, "14,82 có chữ số hàng phần mười là 8 >= 5 nên làm tròn thành 15."),
            make_mc(6, "Làm tròn số 9,95 đến hàng phần mười ta được số:", ["9,9", "10,0", "9,0", "10"], 1, "Chữ số hàng phần trăm là 5 >= 5 nên 9,9 + 0,1 = 10,0.")
        ],
        "part2": [
            make_essay(1, "Làm tròn các số sau đến hàng đơn vị:\na) 14,2\nb) 28,64\nc) 99,8\nd) 0,45", "a) 14,2 làm tròn thành 14\nb) 28,64 làm tròn thành 29\nc) 99,8 làm tròn thành 100\nd) 0,45 làm tròn thành 0", "a) 14; b) 29; c) 100; d) 0", 4, 1.0),
            make_essay(2, "Làm tròn các số sau đến hàng phần mười:\na) 6,48\nb) 19,05\nc) 3,72\nd) 10,96", "a) 6,48 làm tròn thành 6,5\nb) 19,05 làm tròn thành 19,1\nc) 3,72 làm tròn thành 3,7\nd) 10,96 làm tròn thành 11,0", "a) 6,5; b) 19,1; c) 3,7; d) 11,0", 4, 1.0),
            make_essay(3, "Làm tròn các số sau đến hàng phần trăm:\na) 4,256\nb) 8,034\nc) 1,795", "a) 4,256 làm tròn thành 4,26\nb) 8,034 làm tròn thành 8,03\nc) 1,795 làm tròn thành 1,80", "a) 4,26; b) 8,03; c) 1,80", 3, 1.0),
            make_essay(4, "Nhiệt độ cơ thể của em bé khi đo bằng nhiệt kế điện tử là $37,64^\\circ\\text{C}$. Hãy làm tròn số đo nhiệt độ này đến hàng phần mười và đến hàng đơn vị.", "Làm tròn đến hàng phần mười: chữ số hàng phần trăm là 4 < 5 nên ta được $37,6^\\circ\\text{C}$.\nLàm tròn đến hàng đơn vị: chữ số hàng phần mười là 6 >= 5 nên ta được $38^\\circ\\text{C}$.", "Hàng phần mười: 37,6 độ C; Hàng đơn vị: 38 độ C", 3, 1.0),
            make_essay(5, "Một cửa hàng bán được $125,75\\text{ kg}$ gạo vào buổi sáng và $98,4\\text{ kg}$ gạo vào buổi chiều.\na) Tính tổng số ki-lô-gam gạo cửa hàng bán được trong cả ngày.\nb) Làm tròn kết quả tìm được đến hàng đơn vị.", "a) Cả ngày cửa hàng bán được:\n$125,75 + 98,4 = 224,15\\text{ (kg)}$.\nb) Làm tròn số 224,15 đến hàng đơn vị:\nChữ số hàng phần mười là 1 < 5 nên ta được $224\\text{ kg}$.", "a) 224,15 kg; b) 224 kg", 4, 1.5),
            make_essay(6, "Có bao nhiêu số thập phân có một chữ số ở phần thập phân lớn hơn 4 và nhỏ hơn 5 mà khi làm tròn đến hàng đơn vị thì được số 4? Hãy viết các số đó ra.", "Các số thập phân có một chữ số ở phần thập phân lớn hơn 4 và nhỏ hơn 5 có dạng $4,a$ ($a \\in \\{1; 2; ...; 9\\}$).\nĐể khi làm tròn đến hàng đơn vị được số 4 thì chữ số $a < 5$, tức là $a \\in \\{1; 2; 3; 4\\}$.\nVậy có 4 số thỏa mãn là: 4,1; 4,2; 4,3; 4,4.", "4 số: 4,1; 4,2; 4,3; 4,4", 4, 1.5)
        ]
    }

    # --- Bài 13 - Đề 3 ---
    exams["th5_b13_test3"] = {
        "id": "th5_b13_test3",
        "lessonId": "th5_b13",
        "lessonNum": 13,
        "testNum": 3,
        "title": "Bài 13: Làm tròn số thập phân - Đề số 3",
        "topic": "Làm tròn số thập phân",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Làm tròn số 32,5 đến hàng đơn vị ta được:", ["32", "33", "32,0", "30"], 1, "Chữ số hàng phần mười là 5 >= 5 nên làm tròn lên 33."),
            make_mc(2, "Làm tròn số 7,456 đến hàng phần trăm ta được:", ["7,45", "7,46", "7,5", "7,40"], 1, "Hàng phần nghìn là 6 >= 5 nên làm tròn lên 7,46."),
            make_mc(3, "Làm tròn số 0,845 đến hàng phần mười ta được:", ["0,8", "0,9", "0,85", "1,0"], 0, "Chữ số hàng phần trăm là 4 < 5 nên giữ nguyên 0,8."),
            make_mc(4, "Quãng đường từ nhà An đến trường dài 2,36 km. Làm tròn độ dài này đến hàng phần mười là:", ["2,3 km", "2,4 km", "2 km", "3 km"], 1, "2,36 làm tròn thành 2,4 km."),
            make_mc(5, "Số nào dưới đây khi làm tròn đến hàng đơn vị thì được số 20?", ["19,45", "19,52", "20,65", "20,8"], 1, "19,52 có hàng phần mười là 5 >= 5 nên làm tròn lên 20."),
            make_mc(6, "Làm tròn số 5,097 đến hàng phần trăm ta được:", ["5,1", "5,10", "5,09", "5,00"], 1, "Hàng phần nghìn là 7 >= 5 nên 5,09 làm tròn lên thành 5,10.")
        ],
        "part2": [
            make_essay(1, "Làm tròn các số sau đến hàng đơn vị:\na) 45,71\nb) 8,39\nc) 0,55\nd) 199,6", "a) 45,71 làm tròn thành 46\nb) 8,39 làm tròn thành 8\nc) 0,55 làm tròn thành 1\nd) 199,6 làm tròn thành 200", "a) 46; b) 8; c) 1; d) 200", 4, 1.0),
            make_essay(2, "Làm tròn các số sau đến hàng phần mười:\na) 13,85\nb) 7,04\nc) 24,96\nd) 0,638", "a) 13,85 làm tròn thành 13,9\nb) 7,04 làm tròn thành 7,0\nc) 24,96 làm tròn thành 25,0\nd) 0,638 làm tròn thành 0,6", "a) 13,9; b) 7,0; c) 25,0; d) 0,6", 4, 1.0),
            make_essay(3, "Làm tròn các số sau đến hàng phần trăm:\na) 2,481\nb) 15,376\nc) 0,085", "a) 2,481 làm tròn thành 2,48\nb) 15,376 làm tròn thành 15,38\nc) 0,085 làm tròn thành 0,09", "a) 2,48; b) 15,38; c) 0,09", 3, 1.0),
            make_essay(4, "Một mảnh đất hình chữ nhật có chiều dài $15,8\\text{ m}$ và chiều rộng $9,4\\text{ m}$.\na) Tính chu vi mảnh đất đó.\nb) Làm tròn kết quả chu vi vừa tìm được đến hàng đơn vị.", "a) Chu vi mảnh đất là: $(15,8 + 9,4) \\times 2 = 25,2 \\times 2 = 50,4\\text{ (m)}$.\nb) Làm tròn số 50,4 đến hàng đơn vị: chữ số hàng phần mười là 4 < 5 nên ta được $50\\text{ m}$.", "a) 50,4 m; b) 50 m", 4, 1.0),
            make_essay(5, "Một xe tải chở 3 kiện hàng có khối lượng lần lượt là $1,45\\text{ tấn}$; $2,38\\text{ tấn}$ và $1,82\\text{ tấn}$.\na) Tính tổng khối lượng của 3 kiện hàng.\nb) Làm tròn tổng khối lượng tìm được đến hàng phần mười và đến hàng đơn vị.", "a) Tổng khối lượng 3 kiện hàng là:\n$1,45 + 2,38 + 1,82 = 5,65\\text{ (tấn)}$.\nb) - Làm tròn đến hàng phần mười: chữ số hàng phần trăm là 5 >= 5 $\\Rightarrow 5,7\\text{ tấn}$.\n- Làm tròn đến hàng đơn vị: chữ số hàng phần mười là 6 >= 5 $\\Rightarrow 6\\text{ tấn}$.", "a) 5,65 tấn; b) Hàng phần mười: 5,7 tấn; Hàng đơn vị: 6 tấn", 5, 1.5),
            make_essay(6, "Tìm số tự nhiên $a$ bé nhất sao cho khi làm tròn số thập phân $a,75$ đến hàng đơn vị thì ta được một số lớn hơn 15.", "Khi làm tròn số $a,75$ đến hàng đơn vị: vì chữ số hàng phần mười là 7 >= 5 nên số làm tròn được là $a + 1$.\nTheo đề bài: $a + 1 > 15 \\Rightarrow a > 14$.\nVì $a$ là số tự nhiên bé nhất nên $a = 15$.\nKiểm tra: số 15,75 làm tròn đến hàng đơn vị được 16 > 15 (thỏa mãn).", "a = 15", 4, 1.5)
        ]
    }

    # =========================================================================
    # BÀI 14: LUYỆN TẬP CHUNG CHỦ ĐỀ 2
    # =========================================================================
    # --- Bài 14 - Đề 1 ---
    exams["th5_b14_test1"] = {
        "id": "th5_b14_test1",
        "lessonId": "th5_b14",
        "lessonNum": 14,
        "testNum": 1,
        "title": "Bài 14: Luyện tập chung Chủ đề 2 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 2",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Chữ số 6 trong số thập phân 45,368 có giá trị là:", ["$\\frac{6}{10}$", "$\\frac{6}{100}$", "$\\frac{6}{1000}$", "6"], 1, "Chữ số 6 ở hàng phần trăm nên có giá trị là 6/100."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $5\\text{ m } 8\\text{ cm} = \\dots \\text{ m}$ là:", ["5,8", "5,08", "5,008", "58"], 1, "8 cm = 0,08 m => 5,08 m."),
            make_mc(3, "Điền dấu thích hợp: $7,45 \\dots 7,409$:", [">", "<", "=", "Không so sánh được"], 0, "7,450 > 7,409 vì hàng phần trăm 5 > 0."),
            make_mc(4, "Làm tròn số 34,76 đến hàng phần mười ta được:", ["34,7", "34,8", "35", "34,70"], 1, "Chữ số hàng phần trăm là 6 >= 5 nên làm tròn lên 34,8."),
            make_mc(5, "Đổi $3\\text{ ha } 400\\text{ m}^2 = \\dots \\text{ ha}$:", ["3,4", "3,04", "3,004", "34"], 1, "400 m$^2$ = 400/10 000 ha = 0,04 ha => 3,04 ha."),
            make_mc(6, "Số tự nhiên $x$ thỏa mãn $4,85 < x < 5,9$ là:", ["4", "5", "6", "Không có số nào"], 1, "Số tự nhiên nằm giữa 4,85 và 5,9 là 5.")
        ],
        "part2": [
            make_essay(1, "Viết các số đo sau dưới dạng số thập phân:\na) $9\\text{ m } 25\\text{ cm}$ (đơn vị mét)\nb) $4\\text{ tấn } 65\\text{ kg}$ (đơn vị tấn)\nc) $7\\text{ m}^2\\ 45\\text{ dm}^2$ (đơn vị mét vuông)\nd) $8\\text{ ha}$ (đơn vị ki-lô-mét vuông)", "a) $9\\text{ m } 25\\text{ cm} = 9,25\\text{ m}$\nb) $4\\text{ tấn } 65\\text{ kg} = 4,065\\text{ tấn}$\nc) $7\\text{ m}^2\\ 45\\text{ dm}^2 = 7,45\\text{ m}^2$\nd) $8\\text{ ha} = 0,08\\text{ km}^2$", "a) 9,25; b) 4,065; c) 7,45; d) 0,08", 4, 1.0),
            make_essay(2, "Sắp xếp các số sau theo thứ tự từ bé đến lớn:\n$6,38; 6,83; 6,083; 6,308; 6,803$.", "So sánh các số:\n$6,083 < 6,308 < 6,38 < 6,803 < 6,83$.\nThứ tự từ bé đến lớn: $6,083; 6,308; 6,38; 6,803; 6,83$.", "6,083; 6,308; 6,38; 6,803; 6,83", 4, 1.0),
            make_essay(3, "Làm tròn số 85,468:\na) Đến hàng phần trăm;\nb) Đến hàng phần mười;\nc) Đến hàng đơn vị.", "a) Hàng phần nghìn 8 >= 5 $\\Rightarrow 85,47$.\nb) Hàng phần trăm 6 >= 5 $\\Rightarrow 85,5$.\nc) Hàng phần mười 4 < 5 $\\Rightarrow 85$.", "a) 85,47; b) 85,5; c) 85", 4, 1.0),
            make_essay(4, "Tìm số tự nhiên $y$, biết $y$ là số lớn nhất thỏa mãn: $y < 12,85$.", "Các số tự nhiên nhỏ hơn 12,85 là: 0; 1; 2; ...; 11; 12.\nSố lớn nhất trong các số đó là 12.\nVậy $y = 12$.", "y = 12", 3, 1.0),
            make_essay(5, "Một mảnh vườn hình chữ nhật có chiều dài $24,5\\text{ m}$, chiều rộng $15,2\\text{ m}$.\na) Tính chu vi mảnh vườn đó.\nb) Làm tròn kết quả chu vi đến hàng đơn vị.", "a) Chu vi mảnh vườn là:\n$(24,5 + 15,2) \\times 2 = 39,7 \\times 2 = 79,4\\text{ (m)}$.\nb) Làm tròn 79,4 đến hàng đơn vị: chữ số hàng phần mười là 4 < 5 nên ta được $79\\text{ m}$.", "a) 79,4 m; b) 79 m", 4, 1.5),
            make_essay(6, "Cho các chữ số 0; 1; 4; 7. Hãy viết tất cả các số thập phân có ba chữ số khác nhau, trong đó phần thập phân có một chữ số và các số đó lớn hơn 40.", "Số thập phân có dạng $\\overline{ab,c}$ với $a, b, c \\in \\{0; 1; 4; 7\\}$ đôi một khác nhau.\nĐể số đó lớn hơn 40 thì chữ số hàng chục $a$ có thể là 4 hoặc 7.\n- Trường hợp $a = 4$:\n  + $b = 0$: 40,1; 40,7.\n  + $b = 1$: 41,0; 41,7.\n  + $b = 7$: 47,0; 47,1.\n  (Có 6 số lớn hơn 40).\n- Trường hợp $a = 7$:\n  + $b = 0$: 70,1; 70,4.\n  + $b = 1$: 71,0; 71,4.\n  + $b = 4$: 74,0; 74,1.\n  (Có 6 số lớn hơn 40).\nTổng cộng có: $6 + 6 = 12$ số thỏa mãn.", "12 số: 40,1; 40,7; 41,0; 41,7; 47,0; 47,1; 70,1; 70,4; 71,0; 71,4; 74,0; 74,1", 5, 1.5)
        ]
    }

    # --- Bài 14 - Đề 2 ---
    exams["th5_b14_test2"] = {
        "id": "th5_b14_test2",
        "lessonId": "th5_b14",
        "lessonNum": 14,
        "testNum": 2,
        "title": "Bài 14: Luyện tập chung Chủ đề 2 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 2",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số thập phân gồm '3 đơn vị, 5 phần trăm và 8 phần nghìn' viết là:", ["3,58", "3,058", "3,508", "35,8"], 1, "Phần nguyên là 3, phần mười là 0, phần trăm là 5, phần nghìn là 8: 3,058."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $6\\text{ tấn } 45\\text{ kg} = \\dots \\text{ tấn}$ là:", ["6,45", "6,045", "6,450", "64,5"], 1, "45 kg = 0,045 tấn => 6,045 tấn."),
            make_mc(3, "Số bé nhất trong các số: 5,42; 5,24; 5,402; 5,204 là:", ["5,42", "5,24", "5,402", "5,204"], 3, "5,204 có hàng phần mười là 2, hàng phần trăm là 0 bé nhất."),
            make_mc(4, "Làm tròn số 19,85 đến hàng đơn vị ta được:", ["19", "20", "19,9", "19,8"], 1, "Chữ số hàng phần mười là 8 >= 5 nên làm tròn lên 20."),
            make_mc(5, "Đổi $4\\text{ m}^2\\ 7\\text{ dm}^2 = \\dots \\text{ m}^2$:", ["4,7", "4,07", "4,007", "47"], 1, "7 dm$^2$ = 0,07 m$^2$ => 4,07 m$^2$."),
            make_mc(6, "Có bao nhiêu số tự nhiên $n$ thỏa mãn: $8,2 < n < 11,5$?", ["2", "3", "4", "5"], 1, "Các số tự nhiên là: 9; 10; 11 (có 3 số).")
        ],
        "part2": [
            make_essay(1, "Viết các số đo sau dưới dạng số thập phân:\na) $12\\text{ m } 6\\text{ dm}$ (đơn vị mét)\nb) $3\\text{ kg } 450\\text{ g}$ (đơn vị ki-lô-gam)\nc) $5\\text{ m}^2\\ 80\\text{ dm}^2$ (đơn vị mét vuông)\nd) $25\\text{ ha}$ (đơn vị ki-lô-mét vuông)", "a) $12\\text{ m } 6\\text{ dm} = 12,6\\text{ m}$\nb) $3\\text{ kg } 450\\text{ g} = 3,45\\text{ kg}$\nc) $5\\text{ m}^2\\ 80\\text{ dm}^2 = 5,8\\text{ m}^2$\nd) $25\\text{ ha} = 0,25\\text{ km}^2$", "a) 12,6; b) 3,45; c) 5,8; d) 0,25", 4, 1.0),
            make_essay(2, "Xếp các số sau theo thứ tự từ lớn đến bé:\n$9,5; 9,48; 9,505; 9,05; 9,499$.", "So sánh các số:\n$9,505 > 9,5 > 9,499 > 9,48 > 9,05$.\nThứ tự giảm dần: $9,505; 9,5; 9,499; 9,48; 9,05$.", "9,505; 9,5; 9,499; 9,48; 9,05", 4, 1.0),
            make_essay(3, "Làm tròn các số sau đến hàng phần mười:\na) 7,24\nb) 15,68\nc) 0,95", "a) 7,24 làm tròn thành 7,2\nb) 15,68 làm tròn thành 15,7\nc) 0,95 làm tròn thành 1,0", "a) 7,2; b) 15,7; c) 1,0", 3, 1.0),
            make_essay(4, "Tìm 3 số thập phân $x$ thỏa mãn: $1,4 < x < 1,5$.", "Viết $1,4 = 1,40$ và $1,5 = 1,50$.\n3 số thập phân thỏa mãn có thể là: 1,42; 1,45; 1,48.", "Ví dụ: 1,42; 1,45; 1,48", 3, 1.0),
            make_essay(5, "Một cửa hàng có 3 bao đường. Bao thứ nhất nặng $45,5\\text{ kg}$, bao thứ hai nặng $48,25\\text{ kg}$, bao thứ ba nặng $51,4\\text{ kg}$.\na) Tính tổng cân nặng của cả 3 bao đường.\nb) Làm tròn tổng cân nặng tìm được đến hàng đơn vị.", "a) Tổng cân nặng cả 3 bao đường là:\n$45,5 + 48,25 + 51,4 = 145,15\\text{ (kg)}$.\nb) Làm tròn số 145,15 đến hàng đơn vị:\nChữ số hàng phần mười là 1 < 5 nên ta được $145\\text{ kg}$.", "a) 145,15 kg; b) 145 kg", 4, 1.5),
            make_essay(6, "Tìm số thập phân $\\overline{a,b}$ biết rằng khi làm tròn số đó đến hàng đơn vị thì được 8 và $a + b = 11$.", "Vì số thập phân có dạng $\\overline{a,b}$ làm tròn đến hàng đơn vị được 8, nên có hai trường hợp:\n- Trường hợp 1: $a = 8$ và $b < 5$ ($b \\in \\{0; 1; 2; 3; 4\\}$).\n  Khi đó $b = 11 - 8 = 3$ (thỏa mãn vì $3 < 5$).\n  Số đó là 8,3.\n- Trường hợp 2: $a = 7$ và $b \\ge 5$ ($b \\in \\{5; 6; 7; 8; 9\\}$).\n  Khi đó $b = 11 - 7 = 4$ (loại vì $4 < 5$, khi làm tròn lên chỉ được 7).\nVậy số thập phân cần tìm là 8,3.", "8,3", 5, 1.5)
        ]
    }

    # --- Bài 14 - Đề 3 ---
    exams["th5_b14_test3"] = {
        "id": "th5_b14_test3",
        "lessonId": "th5_b14",
        "lessonNum": 14,
        "testNum": 3,
        "title": "Bài 14: Luyện tập chung Chủ đề 2 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 2",
        "chapter": "Chủ đề 2: Số thập phân",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Chữ số 4 trong số 12,456 có giá trị là:", ["4", "0,4", "0,04", "0,004"], 1, "Chữ số 4 ở hàng phần mười nên có giá trị là 0,4 (hay 4/10)."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $8\\text{ km } 25\\text{ m} = \\dots \\text{ km}$ là:", ["8,25", "8,025", "8,250", "82,5"], 1, "25 m = 0,025 km => 8,025 km."),
            make_mc(3, "Điền dấu thích hợp: $0,65 \\dots \\frac{13}{20}$:", ["<", ">", "=", "Không so sánh được"], 2, "13/20 = 65/100 = 0,65 nên bằng nhau."),
            make_mc(4, "Làm tròn số 8,975 đến hàng phần mười ta được:", ["8,9", "9,0", "8,98", "9"], 1, "Hàng phần trăm là 7 >= 5 nên làm tròn lên 9,0."),
            make_mc(5, "Đổi $5\\text{ ha } 20\\text{ m}^2 = \\dots \\text{ ha}$:", ["5,2", "5,02", "5,002", "5,0020"], 2, "20 m$^2$ = 20/10 000 ha = 0,002 ha => 5,002 ha."),
            make_mc(6, "Số thập phân nào dưới đây nằm giữa 3,6 và 3,7?", ["3,59", "3,65", "3,71", "3,75"], 1, "3,60 < 3,65 < 3,70.")
        ],
        "part2": [
            make_essay(1, "Viết các số đo sau dưới dạng số thập phân:\na) $7\\text{ m } 8\\text{ cm} = \\dots \\text{ m}$\nb) $9\\text{ tấn } 50\\text{ kg} = \\dots \\text{ tấn}$\nc) $6\\text{ m}^2\\ 35\\text{ dm}^2 = \\dots \\text{ m}^2$\nd) $150\\text{ m}^2 = \\dots \\text{ ha}$", "a) $7\\text{ m } 8\\text{ cm} = 7,08\\text{ m}$\nb) $9\\text{ tấn } 50\\text{ kg} = 9,05\\text{ tấn}$\nc) $6\\text{ m}^2\\ 35\\text{ dm}^2 = 6,35\\text{ m}^2$\nd) $150\\text{ m}^2 = 0,015\\text{ ha}$", "a) 7,08; b) 9,05; c) 6,35; d) 0,015", 4, 1.0),
            make_essay(2, "Xếp các số sau theo thứ tự từ bé đến lớn:\n$4,75; 4,57; 4,705; 4,075; 4,507$.", "So sánh các số:\n$4,075 < 4,507 < 4,57 < 4,705 < 4,75$.\nThứ tự tăng dần: $4,075; 4,507; 4,57; 4,705; 4,75$.", "4,075; 4,507; 4,57; 4,705; 4,75", 4, 1.0),
            make_essay(3, "Làm tròn số 12,485:\na) Đến hàng đơn vị;\nb) Đến hàng phần mười;\nc) Đến hàng phần trăm.", "a) Hàng phần mười là 4 < 5 $\\Rightarrow 12$.\nb) Hàng phần trăm là 8 >= 5 $\\Rightarrow 12,5$.\nc) Hàng phần nghìn là 5 >= 5 $\\Rightarrow 12,49$.", "a) 12; b) 12,5; c) 12,49", 4, 1.0),
            make_essay(4, "Tìm số tự nhiên $x$ bé nhất thỏa mãn: $x > 8,76$.", "Các số tự nhiên lớn hơn 8,76 là: 9; 10; 11; ...\nSố tự nhiên bé nhất là 9.\nVậy $x = 9$.", "x = 9", 3, 1.0),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chiều dài $80\\text{ m}$, chiều rộng bằng $\\frac{3}{4}$ chiều dài.\na) Tính diện tích thửa ruộng đó theo mét vuông và héc-ta.\nb) Biết cứ $100\\text{ m}^2$ thu được $65\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu được bao nhiêu tạ thóc?", "a) Chiều rộng thửa ruộng là: $80 \\times \\frac{3}{4} = 60\\text{ (m)}$.\nDiện tích thửa ruộng là: $80 \\times 60 = 4 800\\text{ (m$^2$)}$.\nĐổi sang héc-ta: $4 800 : 10 000 = 0,48\\text{ (ha)}$.\nb) Số thóc thu hoạch được là: $4 800 : 100 \\times 65 = 3 120\\text{ (kg)}$.\nĐổi sang tạ: $3 120\\text{ kg} = 31,2\\text{ tạ thóc}$.", "a) 4 800 m$^2$ = 0,48 ha; b) 31,2 tạ thóc", 5, 1.5),
            make_essay(6, "Một số thập phân có ba chữ số ở phần thập phân. Khi làm tròn số đó đến hàng phần trăm ta được số 4,85. Hỏi số thập phân ban đầu có thể có giá trị lớn nhất là bao nhiêu và bé nhất là bao nhiêu?", "Gọi số thập phân đó là $4,85x$ hoặc $4,84y$.\n- Để làm tròn được 4,85 thì:\n  + Nếu là $4,84y$: $y \\in \\{5; 6; 7; 8; 9\\}$, số bé nhất là 4,845.\n  + Nếu là $4,85x$: $x \\in \\{0; 1; 2; 3; 4\\}$, số lớn nhất là 4,854.\nVậy số bé nhất là 4,845 và số lớn nhất là 4,854.", "Số bé nhất: 4,845; Số lớn nhất: 4,854", 5, 1.5)
        ]
    }

    return exams
