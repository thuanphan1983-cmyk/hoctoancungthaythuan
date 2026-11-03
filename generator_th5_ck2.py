# -*- coding: utf-8 -*-
"""
HỆ THỐNG 8 ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 (CUỐI NĂM) - TOÁN LỚP 5
Bộ sách: Kết nối tri thức với cuộc sống
Mã kỳ thi: th5_ck2 (Đề 01 đến Đề 08)
Chuẩn ma trận GD&ĐT và chuẩn mực sư phạm Tiểu học:
- Thời gian làm bài: 40 phút
- Thang điểm: 10.0 điểm
- Phần 1 (3.0 điểm): 6 câu trắc nghiệm khách quan 4 lựa chọn (0.5 điểm/câu)
- Phần 2 (7.0 điểm): 6 bài tự luận (1.0, 1.0, 1.0, 1.5, 1.5, 1.0 điểm) có số dòng kẻ (lineCount: 3-8)
- Phạm vi kiến thức toàn diện: Bảng đơn vị đo thời gian; toán chuyển động đều; biểu đồ hình quạt tròn; ôn tập số học và hình học tổng hợp chuẩn bị chuyển cấp lên lớp 6.
- Tính độc lập 100% giữa các mã đề, số liệu chuẩn xác tuyệt đối.
"""

def get_th5_ck2_exams():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 01 (th5_ck2_de01)
    # =========================================================================
    exams["th5_ck2_de01"] = {
        "id": "th5_ck2_de01",
        "code": "CK2-DE01",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 01)",
        "grade": "5",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Đổi 2 giờ 15 phút sang số phút ta được:",
                "options": ["125 phút", "135 phút", "215 phút", "150 phút"],
                "correct": 1,
                "explanation": "Ta có: $2\\text{ giờ } 15\\text{ phút} = 2 \\times 60 + 15 = 135\\text{ phút}$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Một người đi xe máy trong 2,5 giờ đi được quãng đường $100\\text{ km}$. Vận tốc của người đi xe máy đó là:",
                "options": ["$35\\text{ km/h}$", "$40\\text{ km/h}$", "$45\\text{ km/h}$", "$50\\text{ km/h}$"],
                "correct": 1,
                "explanation": "Vận tốc là: $v = s : t = 100 : 2,5 = 40\\text{ km/h}$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 3:** Biểu đồ hình quạt tròn biểu diễn tỉ lệ học sinh tham gia các câu lạc bộ: Bóng đá $40\\%$, Cờ vua $25\\%$, Bơi lội $20\\%$, còn lại là Cầu lông. Tỉ số phần trăm học sinh tham gia Cầu lông là:",
                "options": ["10%", "15%", "20%", "25%"],
                "correct": 1,
                "explanation": "Tỉ số phần trăm tham gia Cầu lông là: $100\\% - (40\\% + 25\\% + 20\\%) = 15\\%$."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 4:** Phân số $\\frac{3}{5}$ được viết dưới dạng số thập phân là:",
                "options": ["0,35", "0,53", "0,6", "0,75"],
                "correct": 2,
                "explanation": "Ta có: $\\frac{3}{5} = 3 : 5 = 0,6$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Diện tích hình tròn có bán kính $r = 5\\text{ cm}$ là:",
                "options": ["$31,4\\text{ cm}^2$", "$78,5\\text{ cm}^2$", "$15,7\\text{ cm}^2$", "$157\\text{ cm}^2$"],
                "correct": 1,
                "explanation": "Diện tích hình tròn là: $S = r \\times r \\times 3,14 = 5 \\times 5 \\times 3,14 = 78,5\\text{ cm}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Hai ô tô cùng xuất phát từ A và B cách nhau $180\\text{ km}$ đi ngược chiều nhau. Vận tốc xe đi từ A là $48\\text{ km/h}$, vận tốc xe đi từ B là $42\\text{ km/h}$. Hai xe gặp nhau sau:",
                "options": ["1,5 giờ", "2 giờ", "2,5 giờ", "3 giờ"],
                "correct": 1,
                "explanation": "Tổng vận tốc hai xe là: $48 + 42 = 90\\text{ km/h}$. Thời gian gặp nhau: $180 : 90 = 2$ giờ."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) 4 giờ 35 phút + 3 giờ 40 phút\nb) 15 phút 20 giây - 6 phút 45 giây",
                "solution": "a) 4 giờ 35 phút + 3 giờ 40 phút = 7 giờ 75 phút = 8 giờ 15 phút.\nb) 15 phút 20 giây - 6 phút 45 giây = 14 phút 80 giây - 6 phút 45 giây = 8 phút 35 giây.",
                "answer": "a) 8 giờ 15 phút; b) 8 phút 35 giây"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$12,45 \\times 36 + 12,45 \\times 63 + 12,45$",
                "solution": "Ta có:\n$12,45 \\times 36 + 12,45 \\times 63 + 12,45 = 12,45 \\times (36 + 63 + 1)$\n$= 12,45 \\times 100 = 1245$.\nĐáp số: 1245.",
                "answer": "1245"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Biểu đồ hình quạt tròn cho biết cơ cấu các loại sách trong thư viện trường tiểu học gồm 1200 cuốn: Sách giáo khoa chiếm $50\\%$, Sách tham khảo chiếm $30\\%$, Truyện tranh chiếm $20\\%$.\na) Tính số cuốn sách giáo khoa có trong thư viện.\nb) Số cuốn sách tham khảo nhiều hơn số cuốn truyện tranh là bao nhiêu cuốn?",
                "solution": "Bài giải:\na) Số cuốn sách giáo khoa có trong thư viện là:\n$1200 \\times 50 : 100 = 600\\text{ (cuốn)}$\nb) Tỉ số phần trăm sách tham khảo nhiều hơn truyện tranh là:\n$30\\% - 20\\% = 10\\%$\nSố cuốn sách tham khảo nhiều hơn truyện tranh là:\n$1200 \\times 10 : 100 = 120\\text{ (cuốn)}$\nĐáp số:\na) 600 cuốn;\nb) 120 cuốn.",
                "answer": "a) 600 cuốn; b) 120 cuốn"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một thửa ruộng hình thang có đáy lớn $45\\text{ m}$, đáy bé bằng $\\frac{2}{3}$ đáy lớn, chiều cao bằng $18\\text{ m}$.\na) Tính diện tích thửa ruộng hình thang đó.\nb) Người ta cấy lúa trên thửa ruộng đó, cứ $100\\text{ m}^2$ thu hoạch được $65\\text{ kg}$ thóc. Hỏi trên cả thửa ruộng đó thu hoạch được bao nhiêu tạ thóc?",
                "solution": "Bài giải:\na) Độ dài đáy bé của thửa ruộng là:\n$45 \\times 2 : 3 = 30\\text{ (m)}$\nDiện tích thửa ruộng hình thang là:\n$(45 + 30) \\times 18 : 2 = 675\\text{ (m}^2)$\nb) Số ki-lô-gam thóc thu hoạch được trên cả thửa ruộng là:\n$675 : 100 \\times 65 = 438,75\\text{ (kg)}$\nĐổi: $438,75\\text{ kg} = 4,3875\\text{ tạ}$.\nĐáp số:\na) $675\\text{ m}^2$;\nb) $4,3875\\text{ tạ thóc}$.",
                "answer": "a) 675 m²; b) 4,3875 tạ"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 7,
                "level": "Vận dụng",
                "question": "**Bài 5:** Quãng đường từ thành phố A đến thành phố B dài $135\\text{ km}$. Lúc 7 giờ 15 phút, một người đi xe máy từ A đến B với vận tốc $36\\text{ km/h}$. Dọc đường người đó nghỉ giải lao 25 phút. Hỏi người đi xe máy đến B lúc mấy giờ?",
                "solution": "Bài giải:\nThời gian người đó đi xe máy trên đường là:\n$135 : 36 = 3,75\\text{ (giờ)}$\nĐổi: $3,75\\text{ giờ} = 3\\text{ giờ } 45\\text{ phút}$.\nTổng thời gian đi và nghỉ dọc đường là:\n$3\\text{ giờ } 45\\text{ phút} + 25\\text{ phút} = 4\\text{ giờ } 10\\text{ phút}$.\nNgười đi xe máy đến thành phố B lúc:\n$7\\text{ giờ } 15\\text{ phút} + 4\\text{ giờ } 10\\text{ phút} = 11\\text{ giờ } 25\\text{ phút}$.\nĐáp số: 11 giờ 25 phút.",
                "answer": "11 giờ 25 phút"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 6,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Cho phân số $\\frac{19}{27}$. Hỏi phải cùng thêm vào cả tử số và mẫu số của phân số đó bao nhiêu đơn vị để được phân số mới có giá trị bằng $\\frac{5}{7}$?",
                "solution": "Bài giải:\nKhi cùng thêm vào cả tử số và mẫu số một số đơn vị như nhau thì hiệu giữa mẫu số và tử số không thay đổi.\nHiệu giữa mẫu số và tử số là:\n$27 - 19 = 8$\nCoi tử số mới là 5 phần bằng nhau thì mẫu số mới là 7 phần như thế.\nHiệu số phần bằng nhau là:\n$7 - 5 = 2\\text{ (phần)}$\nGiá trị của một phần là:\n$8 : 2 = 4$\nTử số mới là:\n$4 \\times 5 = 20$\nSố đơn vị cần thêm vào cả tử số và mẫu số là:\n$20 - 19 = 1$\nĐáp số: 1.",
                "answer": "1"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 02 (th5_ck2_de02)
    # =========================================================================
    exams["th5_ck2_de02"] = {
        "id": "th5_ck2_de02",
        "code": "CK2-DE02",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 02)",
        "grade": "5",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Số đo thời gian 3,5 giờ viết dưới dạng giờ và phút là:",
                "options": ["3 giờ 5 phút", "3 giờ 50 phút", "3 giờ 30 phút", "3 giờ 15 phút"],
                "correct": 2,
                "explanation": "$3,5\\text{ giờ} = 3\\text{ giờ} + 0,5 \\times 60\\text{ phút} = 3\\text{ giờ } 30\\text{ phút}$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Một con ong mật bay với vận tốc $8,4\\text{ km/h}$. Trong 15 phút, con ong đó bay được quãng đường là:",
                "options": ["$2,1\\text{ km}$", "$1,26\\text{ km}$", "$21\\text{ km}$", "$0,21\\text{ km}$"],
                "correct": 0,
                "explanation": "Đổi: $15\\text{ phút} = 0,25\\text{ giờ}$. Quãng đường bay: $8,4 \\times 0,25 = 2,1\\text{ km}$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 3:** Khảo sát sở thích đọc sách của 400 học sinh: Khoa học $35\\%$, Lịch sử $25\\%$, Văn học $30\\%$, Kỹ năng sống $10\\%$. Số học sinh thích đọc sách Lịch sử là:",
                "options": ["80 học sinh", "100 học sinh", "120 học sinh", "140 học sinh"],
                "correct": 1,
                "explanation": "Số học sinh thích sách Lịch sử là: $400 \\times 25 : 100 = 100$ (học sinh)."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 4:** Chữ số 7 trong số thập phân 182,375 có giá trị là:",
                "options": ["7", "$\\frac{7}{10}$", "$\\frac{7}{100}$", "$\\frac{7}{1000}$"],
                "correct": 2,
                "explanation": "Chữ số 7 nằm ở hàng phần trăm nên có giá trị là $\\frac{7}{100}$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Chu vi của một hình tròn có đường kính $d = 8\\text{ dm}$ là:",
                "options": ["$25,12\\text{ dm}$", "$50,24\\text{ dm}$", "$12,56\\text{ dm}$", "$200,96\\text{ dm}$"],
                "correct": 0,
                "explanation": "Chu vi hình tròn là: $C = d \\times 3,14 = 8 \\times 3,14 = 25,12\\text{ dm}$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Hai người đi bộ cùng xuất phát từ một điểm và đi cùng chiều. Người thứ nhất đi với vận tốc $4\\text{ km/h}$, người thứ hai đi với vận tốc $5,5\\text{ km/h}$. Sau 2 giờ, khoảng cách giữa hai người là:",
                "options": ["$1,5\\text{ km}$", "$3\\text{ km}$", "$4,5\\text{ km}$", "$19\\text{ km}$"],
                "correct": 1,
                "explanation": "Mỗi giờ người thứ hai đi xa hơn người thứ nhất: $5,5 - 4 = 1,5\\text{ km}$. Sau 2 giờ khoảng cách là: $1,5 \\times 2 = 3\\text{ km}$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Tính phép tính số đo thời gian sau:\na) 3 giờ 24 phút $\\times 4$\nb) 14 phút 36 giây $: 3$",
                "solution": "a) 3 giờ 24 phút $\\times 4 = 12$ giờ 96 phút = 13 giờ 36 phút.\nb) 14 phút 36 giây : 3 = 12 phút 156 giây : 3 = 4 phút 52 giây.",
                "answer": "a) 13 giờ 36 phút; b) 4 phút 52 giây"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $x$, biết:\n$(x + 2,4) \\times 3,5 = 21$",
                "solution": "Ta có:\n$x + 2,4 = 21 : 3,5$\n$x + 2,4 = 6$\n$x = 6 - 2,4$\n$x = 3,6$.\nĐáp số: $x = 3,6$.",
                "answer": "x = 3,6"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một trang trại nuôi 1500 con gia cầm gồm gà, vịt và ngan. Qua biểu đồ hình quạt tròn thấy tỉ lệ gà chiếm $48\\%$, vịt chiếm $32\\%$, còn lại là ngan.\na) Tính số con ngan trang trại đó đang nuôi.\nb) Số con gà nhiều hơn số con vịt bao nhiêu con?",
                "solution": "Bài giải:\na) Tỉ lệ phần trăm con ngan trang trại đang nuôi là:\n$100\\% - (48\\% + 32\\%) = 20\\%$\nSố con ngan trang trại đang nuôi là:\n$1500 \\times 20 : 100 = 300\\text{ (con)}$\nb) Số con gà nhiều hơn số con vịt là:\n$1500 \\times (48\\% - 32\\%) : 100 = 240\\text{ (con)}$\nĐáp số:\na) 300 con ngan;\nb) 240 con.",
                "answer": "a) 300 con; b) 240 con"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một mảnh đất hình thang có đáy lớn $36\\text{ m}$, đáy bé $24\\text{ m}$, chiều cao bằng trung bình cộng hai đáy. Ở giữa mảnh đất người ta đào một cái ao hình tròn có bán kính $3\\text{ m}$. Phần đất còn lại dùng để trồng cỏ.\na) Tính diện tích mảnh đất hình thang.\nb) Tính diện tích đất dùng để trồng cỏ.",
                "solution": "Bài giải:\na) Chiều cao mảnh đất hình thang là:\n$(36 + 24) : 2 = 30\\text{ (m)}$\nDiện tích mảnh đất hình thang là:\n$(36 + 24) \\times 30 : 2 = 900\\text{ (m}^2)$\nb) Diện tích cái ao hình tròn là:\n$3 \\times 3 \\times 3,14 = 28,26\\text{ (m}^2)$\nDiện tích phần đất dùng để trồng cỏ là:\n$900 - 28,26 = 871,74\\text{ (m}^2)$\nĐáp số:\na) $900\\text{ m}^2$;\nb) $871,74\\text{ m}^2$.",
                "answer": "a) 900 m²; b) 871,74 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 7,
                "level": "Vận dụng",
                "question": "**Bài 5:** Quãng đường AB dài $120\\text{ km}$. Lúc 6 giờ sáng, một ô tô đi từ A về B với vận tốc $50\\text{ km/h}$. Cùng lúc đó, một xe máy đi từ B về A với vận tốc $30\\text{ km/h}$.\na) Hỏi sau bao lâu kể từ lúc khởi hành thì hai xe gặp nhau?\nb) Hai xe gặp nhau lúc mấy giờ?\nc) Điểm gặp nhau cách A bao nhiêu ki-lô-mét?",
                "solution": "Bài giải:\na) Quãng đường hai xe cùng đi được trong một giờ là:\n$50 + 30 = 80\\text{ (km)}$\nThời gian để hai xe gặp nhau là:\n$120 : 80 = 1,5\\text{ (giờ)}$\nĐổi: $1,5\\text{ giờ} = 1\\text{ giờ } 30\\text{ phút}$.\nb) Hai xe gặp nhau vào thời điểm:\n$6\\text{ giờ} + 1\\text{ giờ } 30\\text{ phút} = 7\\text{ giờ } 30\\text{ phút}$.\nc) Điểm gặp nhau cách điểm xuất phát A là:\n$50 \\times 1,5 = 75\\text{ (km)}$\nĐáp số:\na) 1,5 giờ (1 giờ 30 phút);\nb) 7 giờ 30 phút;\nc) $75\\text{ km}$.",
                "answer": "a) 1,5 giờ; b) 7 giờ 30 phút; c) 75 km"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 6,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Hai người thợ cùng làm chung một công việc thì sau 6 giờ sẽ hoàn thành. Nếu người thứ nhất làm một mình thì sau 10 giờ mới hoàn thành công việc. Hỏi nếu người thứ hai làm một mình thì sau bao nhiêu giờ sẽ hoàn thành công việc đó?",
                "solution": "Bài giải:\nTrong 1 giờ, cả hai người thợ cùng làm được số phần công việc là:\n$1 : 6 = \\frac{1}{6}\\text{ (công việc)}$\nTrong 1 giờ, người thứ nhất làm được số phần công việc là:\n$1 : 10 = \\frac{1}{10}\\text{ (công việc)}$\nTrong 1 giờ, người thứ hai làm một mình được số phần công việc là:\n$\\frac{1}{6} - \\frac{1}{10} = \\frac{5}{30} - \\frac{3}{30} = \\frac{2}{30} = \\frac{1}{15}\\text{ (công việc)}$\nNếu làm một mình, người thứ hai hoàn thành công việc sau thời gian là:\n$1 : \\frac{1}{15} = 15\\text{ (giờ)}$\nĐáp số: 15 giờ.",
                "answer": "15 giờ"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 03 (th5_ck2_de03)
    # =========================================================================
    exams["th5_ck2_de03"] = {
        "id": "th5_ck2_de03",
        "code": "CK2-DE03",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 03)",
        "grade": "5",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Năm 2024 thuộc thế kỉ thứ mấy?",
                "options": ["Thế kỉ XIX", "Thế kỉ XX", "Thế kỉ XXI", "Thế kỉ XXII"],
                "correct": 2,
                "explanation": "Từ năm 2001 đến năm 2100 thuộc thế kỉ XXI."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Một vận động viên chạy cự li $100\\text{ m}$ hết 12,5 giây. Vận tốc chạy của vận động viên đó tính theo mét/giây là:",
                "options": ["$8\\text{ m/s}$", "$8,5\\text{ m/s}$", "$7,5\\text{ m/s}$", "$10\\text{ m/s}$"],
                "correct": 0,
                "explanation": "Vận tốc chạy là: $100 : 12,5 = 8\\text{ m/s}$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 3:** Biểu đồ hình quạt tròn cho biết kết quả xếp loại học lực của 240 học sinh: Xuất sắc $30\\%$, Giỏi $45\\%$, Khá $20\\%$, Hoàn thành $5\\%$. Số học sinh xếp loại Giỏi là:",
                "options": ["72 học sinh", "96 học sinh", "108 học sinh", "120 học sinh"],
                "correct": 2,
                "explanation": "Số học sinh xếp loại Giỏi là: $240 \\times 45 : 100 = 108$ (học sinh)."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Tìm một số biết $30\\%$ của số đó bằng 75:",
                "options": ["25", "225", "250", "300"],
                "correct": 2,
                "explanation": "Số đó là: $75 : 30 \\times 100 = 250$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Một hình tam giác có độ dài đáy $14\\text{ cm}$ và chiều cao $8\\text{ cm}$. Diện tích của hình tam giác đó là:",
                "options": ["$112\\text{ cm}^2$", "$56\\text{ cm}^2$", "$28\\text{ cm}^2$", "$44\\text{ cm}^2$"],
                "correct": 1,
                "explanation": "Diện tích tam giác là: $S = 14 \\times 8 : 2 = 56\\text{ cm}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một người đi xe đạp với vận tốc $12\\text{ km/h}$. Quãng đường người đó đi được trong 45 phút là:",
                "options": ["$9\\text{ km}$", "$8\\text{ km}$", "$10\\text{ km}$", "$6\\text{ km}$"],
                "correct": 0,
                "explanation": "Đổi: $45\\text{ phút} = 0,75\\text{ giờ}$. Quãng đường là: $12 \\times 0,75 = 9\\text{ km}$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Tính giá trị biểu thức sau:\na) $(4,85 + 2,15) \\times 3,6 - 12,5$\nb) 5 ngày 14 giờ + 3 ngày 18 giờ",
                "solution": "a) $(4,85 + 2,15) \\times 3,6 - 12,5 = 7 \\times 3,6 - 12,5 = 25,2 - 12,5 = 12,7$\nb) 5 ngày 14 giờ + 3 ngày 18 giờ = 8 ngày 32 giờ = 9 ngày 8 giờ.",
                "answer": "a) 12,7; b) 9 ngày 8 giờ"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$0,25 \\times 1,25 \\times 4 \\times 8$",
                "solution": "Ta có:\n$0,25 \\times 1,25 \\times 4 \\times 8 = (0,25 \\times 4) \\times (1,25 \\times 8)$\n$= 1 \\times 10 = 10$.\nĐáp số: 10.",
                "answer": "10"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một cửa hàng hoa quả nhập về $800\\text{ kg}$ trái cây các loại. Biểu đồ hình quạt tròn cho biết: Xoài chiếm $35\\%$, Dưa hấu chiếm $25\\%$, Cam chiếm $30\\%$, Nho chiếm $10\\%$.\na) Tính số ki-lô-gam xoài và số ki-lô-gam nho cửa hàng nhập về.\nb) Số ki-lô-gam cam nhiều hơn số ki-lô-gam dưa hấu là bao nhiêu ki-lô-gam?",
                "solution": "Bài giải:\na) Số ki-lô-gam xoài cửa hàng nhập về là:\n$800 \\times 35 : 100 = 280\\text{ (kg)}$\nSố ki-lô-gam nho cửa hàng nhập về là:\n$800 \\times 10 : 100 = 80\\text{ (kg)}$\nb) Số ki-lô-gam cam nhiều hơn dưa hấu là:\n$800 \\times (30\\% - 25\\%) : 100 = 40\\text{ (kg)}$\nĐáp số:\na) Xoài: $280\\text{ kg}$, Nho: $80\\text{ kg}$;\nb) $40\\text{ kg}$.",
                "answer": "a) Xoài 280 kg, Nho 80 kg; b) 40 kg"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một bồn hoa hình tròn có đường kính $6\\text{ m}$. Người ta làm một lối đi xung quanh bồn hoa đó rộng $1\\text{ m}$.\na) Tính diện tích của bồn hoa hình tròn.\nb) Tính diện tích của lối đi xung quanh bồn hoa đó.",
                "solution": "Bài giải:\na) Bán kính của bồn hoa hình tròn là:\n$6 : 2 = 3\\text{ (m)}$\nDiện tích bồn hoa hình tròn là:\n$3 \\times 3 \\times 3,14 = 28,26\\text{ (m}^2)$\nb) Bán kính của hình tròn gồm cả bồn hoa và lối đi là:\n$3 + 1 = 4\\text{ (m)}$\nDiện tích hình tròn gồm cả bồn hoa và lối đi là:\n$4 \\times 4 \\times 3,14 = 50,24\\text{ (m}^2)$\nDiện tích của lối đi xung quanh bồn hoa là:\n$50,24 - 28,26 = 21,98\\text{ (m}^2)$\nĐáp số:\na) $28,26\\text{ m}^2$;\nb) $21,98\\text{ m}^2$.",
                "answer": "a) 28,26 m²; b) 21,98 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 7,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một người đi xe đạp từ A đến B với vận tốc $12\\text{ km/h}$. Sau 2 giờ, một người đi xe máy cũng xuất phát từ A đuổi theo người đi xe đạp với vận tốc $36\\text{ km/h}$.\na) Hỏi sau bao lâu kể từ lúc xe máy bắt đầu khởi hành thì xe máy đuổi kịp xe đạp?\nb) Điểm gặp nhau cách vị trí xuất phát A bao nhiêu ki-lô-mét?",
                "solution": "Bài giải:\na) Trong 2 giờ người đi xe đạp đã đi được quãng đường là:\n$12 \\times 2 = 24\\text{ (km)}$\nMỗi giờ xe máy đi nhanh hơn xe đạp quãng đường là:\n$36 - 12 = 24\\text{ (km)}$\nThời gian xe máy đuổi kịp xe đạp là:\n$24 : 24 = 1\\text{ (giờ)}$\nb) Điểm gặp nhau cách điểm xuất phát A là:\n$36 \\times 1 = 36\\text{ (km)}$\nĐáp số:\na) 1 giờ;\nb) $36\\text{ km}$.",
                "answer": "a) 1 giờ; b) 36 km"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 6,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Tính tổng của dãy số cách đều sau:\n$S = 1,2 + 2,3 + 3,4 + 4,5 + \\dots + 22,1$",
                "solution": "Bài giải:\nDãy số trên là dãy số cách đều với khoảng cách giữa hai số liên tiếp là:\n$2,3 - 1,2 = 1,1$\nSố các số hạng của dãy số trên là:\n$(22,1 - 1,2) : 1,1 + 1 = 20,9 : 1,1 + 1 = 19 + 1 = 20\\text{ (số hạng)}$\nTổng $S$ của dãy số trên là:\n$(1,2 + 22,1) \\times 20 : 2 = 23,3 \\times 10 = 233$\nĐáp số: 233.",
                "answer": "233"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 04 (th5_ck2_de04)
    # =========================================================================
    exams["th5_ck2_de04"] = {
        "id": "th5_ck2_de04",
        "code": "CK2-DE04",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 04)",
        "grade": "5",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** 4 phút 18 giây bằng bao nhiêu giây?",
                "options": ["248 giây", "258 giây", "418 giây", "268 giây"],
                "correct": 1,
                "explanation": "$4\\text{ phút } 18\\text{ giây} = 4 \\times 60 + 18 = 258\\text{ giây}$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Một ca nô xuôi dòng với vận tốc $24\\text{ km/h}$, vận tốc dòng nước là $3\\text{ km/h}$. Vận tốc của ca nô khi đi ngược dòng là:",
                "options": ["$21\\text{ km/h}$", "$18\\text{ km/h}$", "$27\\text{ km/h}$", "$20\\text{ km/h}$"],
                "correct": 1,
                "explanation": "Vận tốc thực ca nô là $24 - 3 = 21\\text{ km/h}$. Vận tốc ngược dòng là $21 - 3 = 18\\text{ km/h}$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 3:** Một hình lập phương có cạnh $0,5\\text{ m}$. Thể tích của hình lập phương đó là:",
                "options": ["$0,25\\text{ m}^3$", "$1,25\\text{ m}^3$", "$0,125\\text{ m}^3$", "$0,0125\\text{ m}^3$"],
                "correct": 2,
                "explanation": "$V = 0,5 \\times 0,5 \\times 0,5 = 0,125\\text{ m}^3$."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Biểu đồ hình quạt tròn thể hiện phương tiện đến trường của 500 học sinh: Đi bộ $20\\%$, Xe đạp $45\\%$, Xe máy bố mẹ chở $30\\%$, Xe buýt $5\\%$. Số học sinh đi xe đạp là:",
                "options": ["150 học sinh", "200 học sinh", "225 học sinh", "250 học sinh"],
                "correct": 2,
                "explanation": "Số học sinh đi xe đạp là: $500 \\times 45 : 100 = 225$ (học sinh)."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 5:** Viết số đo diện tích $4\\text{ m}^2\\ 8\\text{ dm}^2$ dưới dạng số thập phân có đơn vị mét vuông là:",
                "options": ["$4,8\\text{ m}^2$", "$4,08\\text{ m}^2$", "$4,008\\text{ m}^2$", "$48\\text{ m}^2$"],
                "correct": 1,
                "explanation": "Vì $1\\text{ dm}^2 = 0,01\\text{ m}^2$ nên $4\\text{ m}^2\\ 8\\text{ dm}^2 = 4,08\\text{ m}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một ô tô khởi hành từ Hà Nội lúc 8 giờ và đến Hải Phòng lúc 10 giờ 30 phút. Quãng đường Hà Nội - Hải Phòng dài $105\\text{ km}$. Vận tốc của ô tô là:",
                "options": ["$40\\text{ km/h}$", "$42\\text{ km/h}$", "$45\\text{ km/h}$", "$50\\text{ km/h}$"],
                "correct": 1,
                "explanation": "Thời gian đi là: $10\\text{ giờ } 30\\text{ phút} - 8\\text{ giờ} = 2,5\\text{ giờ}$. Vận tốc: $105 : 2,5 = 42\\text{ km/h}$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) 5 giờ 12 phút : 4\nb) 2 giờ 45 phút $\\times 3$",
                "solution": "a) 5 giờ 12 phút : 4 = 4 giờ 72 phút : 4 = 1 giờ 18 phút.\nb) 2 giờ 45 phút $\\times 3 = 6$ giờ 135 phút = 8 giờ 15 phút.",
                "answer": "a) 1 giờ 18 phút; b) 8 giờ 15 phút"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $x$, biết:\n$x : 2,4 = 18,5 - 9,7$",
                "solution": "Ta có:\n$x : 2,4 = 8,8$\n$x = 8,8 \\times 2,4$\n$x = 21,12$.\nĐáp số: $x = 21,12$.",
                "answer": "x = 21,12"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một hợp tác xã thu hoạch được 120 tấn nông sản gồm lúa, ngô, khoai và sắn. Biểu đồ hình quạt tròn cho biết: Lúa chiếm $55\\%$, Ngô chiếm $25\\%$, Khoai chiếm $12\\%$, còn lại là Sắn.\na) Tính số tấn lúa và số tấn ngô thu hoạch được.\nb) Tỉ lệ phần trăm của sắn là bao nhiêu và sắn thu hoạch được bao nhiêu tấn?",
                "solution": "Bài giải:\na) Số tấn lúa thu hoạch được là:\n$120 \\times 55 : 100 = 66\\text{ (tấn)}$\nSố tấn ngô thu hoạch được là:\n$120 \\times 25 : 100 = 30\\text{ (tấn)}$\nb) Tỉ số phần trăm của lượng sắn thu hoạch là:\n$100\\% - (55\\% + 25\\% + 12\\%) = 8\\%$\nSố tấn sắn thu hoạch được là:\n$120 \\times 8 : 100 = 9,6\\text{ (tấn)}$\nĐáp số:\na) Lúa: 66 tấn, Ngô: 30 tấn;\nb) $8\\%$ và 9,6 tấn sắn.",
                "answer": "a) Lúa 66 tấn, Ngô 30 tấn; b) 8% và 9,6 tấn"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một thửa ruộng hình chữ nhật có chiều dài $60\\text{ m}$, chiều rộng bằng $\\frac{2}{3}$ chiều dài.\na) Tính diện tích thửa ruộng đó.\nb) Người ta dùng $15\\%$ diện tích thửa ruộng để đào ao thả cá, phần diện tích còn lại trồng ngô. Tính diện tích phần đất trồng ngô.",
                "solution": "Bài giải:\na) Chiều rộng của thửa ruộng hình chữ nhật là:\n$60 \\times 2 : 3 = 40\\text{ (m)}$\nDiện tích của thửa ruộng là:\n$60 \\times 40 = 2400\\text{ (m}^2)$\nb) Tỉ số phần trăm diện tích đất trồng ngô là:\n$100\\% - 15\\% = 85\\%$\nDiện tích đất trồng ngô là:\n$2400 \\times 85 : 100 = 2040\\text{ (m}^2)$\nĐáp số:\na) $2400\\text{ m}^2$;\nb) $2040\\text{ m}^2$.",
                "answer": "a) 2400 m²; b) 2040 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 7,
                "level": "Vận dụng",
                "question": "**Bài 5:** Hai tỉnh A và B cách nhau $140\\text{ km}$. Lúc 7 giờ sáng, một ô tô đi từ A về B với vận tốc $45\\text{ km/h}$. Cùng lúc đó một người đi xe máy từ B về A với vận tốc $35\\text{ km/h}$.\na) Sau bao lâu kể từ lúc bắt đầu đi thì hai xe gặp nhau?\nb) Hai xe gặp nhau lúc mấy giờ?\nc) Chỗ gặp nhau cách B bao nhiêu ki-lô-mét?",
                "solution": "Bài giải:\na) Tổng vận tốc của hai xe là:\n$45 + 35 = 80\\text{ (km/h)}$\nThời gian để hai xe gặp nhau là:\n$140 : 80 = 1,75\\text{ (giờ)}$\nĐổi: $1,75\\text{ giờ} = 1\\text{ giờ } 45\\text{ phút}$.\nb) Hai xe gặp nhau vào lúc:\n$7\\text{ giờ} + 1\\text{ giờ } 45\\text{ phút} = 8\\text{ giờ } 45\\text{ phút}$.\nc) Chỗ gặp nhau cách tỉnh B quãng đường là:\n$35 \\times 1,75 = 61,25\\text{ (km)}$\nĐáp số:\na) 1,75 giờ (1 giờ 45 phút);\nb) 8 giờ 45 phút;\nc) $61,25\\text{ km}$.",
                "answer": "a) 1,75 giờ; b) 8 giờ 45 phút; c) 61,25 km"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 6,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Vừa gà vừa chó có tất cả 36 con và 100 cái chân. Hỏi có bao nhiêu con gà và bao nhiêu con chó?",
                "solution": "Bài giải:\nGiả sử tất cả 36 con đều là gà, khi đó tổng số chân là:\n$36 \\times 2 = 72\\text{ (chân)}$\nSố chân hụt đi so với thực tế là:\n$100 - 72 = 28\\text{ (chân)}$\nMỗi con chó nhiều hơn mỗi con gà số chân là:\n$4 - 2 = 2\\text{ (chân)}$\nSố con chó có là:\n$28 : 2 = 14\\text{ (con)}$\nSố con gà có là:\n$36 - 14 = 22\\text{ (con)}$\nĐáp số: 22 con gà và 14 con chó.",
                "answer": "22 con gà, 14 con chó"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 05 (th5_ck2_de05)
    # =========================================================================
    exams["th5_ck2_de05"] = {
        "id": "th5_ck2_de05",
        "code": "CK2-DE05",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 05)",
        "grade": "5",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Đổi 1,75 giờ ra giờ và phút ta được:",
                "options": ["1 giờ 45 phút", "1 giờ 75 phút", "1 giờ 15 phút", "1 giờ 30 phút"],
                "correct": 0,
                "explanation": "$1,75\\text{ giờ} = 1\\text{ giờ} + 0,75 \\times 60\\text{ phút} = 1\\text{ giờ } 45\\text{ phút}$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Một người đi bộ đi được quãng đường $10,5\\text{ km}$ trong 2,5 giờ. Vận tốc của người đó là:",
                "options": ["$4\\text{ km/h}$", "$4,2\\text{ km/h}$", "$4,5\\text{ km/h}$", "$5\\text{ km/h}$"],
                "correct": 1,
                "explanation": "Vận tốc là: $10,5 : 2,5 = 4,2\\text{ km/h}$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 3:** Khảo sát các món ăn sáng ưa thích của 300 học sinh: Phở $30\\%$, Bánh mì $40\\%$, Xôi $20\\%$, Bún $10\\%$. Số học sinh thích ăn Xôi là:",
                "options": ["40 học sinh", "50 học sinh", "60 học sinh", "70 học sinh"],
                "correct": 2,
                "explanation": "Số học sinh thích ăn xôi là: $300 \\times 20 : 100 = 60$ (học sinh)."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 4:** Giá trị của biểu thức $\\frac{3}{4} + \\frac{1}{2} : 2$ là:",
                "options": ["$\\frac{5}{8}$", "$\\frac{3}{4}$", "$\\frac{7}{8}$", "$1$"],
                "correct": 3,
                "explanation": "Ta có: $\\frac{3}{4} + \\frac{1}{4} = \\frac{4}{4} = 1$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Diện tích hình thang có hai đáy lần lượt là $12\\text{ cm}$ và $8\\text{ cm}$, chiều cao $6\\text{ cm}$ là:",
                "options": ["$60\\text{ cm}^2$", "$120\\text{ cm}^2$", "$48\\text{ cm}^2$", "$72\\text{ cm}^2$"],
                "correct": 0,
                "explanation": "$S = (12 + 8) \\times 6 : 2 = 60\\text{ cm}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một ô tô đi từ tỉnh A đến tỉnh B hết 3 giờ với quãng đường $150\\text{ km}$. Vận tốc của ô tô là:",
                "options": ["$45\\text{ km/h}$", "$50\\text{ km/h}$", "$55\\text{ km/h}$", "$60\\text{ km/h}$"],
                "correct": 1,
                "explanation": "Vận tốc ô tô là: $150 : 3 = 50\\text{ km/h}$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Tính bằng cách thuận tiện nhất:\n$8,3 \\times 97 + 8,3 \\times 2 + 8,3$",
                "solution": "Ta có:\n$8,3 \\times 97 + 8,3 \\times 2 + 8,3 = 8,3 \\times (97 + 2 + 1)$\n$= 8,3 \\times 100 = 830$.\nĐáp số: 830.",
                "answer": "830"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $x$, biết:\n$x \\times 1,8 - x \\times 0,8 = 15,6$",
                "solution": "Ta có:\n$x \\times (1,8 - 0,8) = 15,6$\n$x \\times 1 = 15,6$\n$x = 15,6$.\nĐáp số: $x = 15,6$.",
                "answer": "x = 15,6"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Biểu đồ quạt tròn biểu diễn 500 cây ăn quả trong trang trại: Xoài $30\\%$, Nhãn $35\\%$, Mít $20\\%$, Bưởi $15\\%$.\na) Tính số cây nhãn và số cây mít trong trang trại.\nb) Số cây bưởi ít hơn số cây xoài là bao nhiêu cây?",
                "solution": "Bài giải:\na) Số cây nhãn có trong trang trại là:\n$500 \\times 35 : 100 = 175\\text{ (cây)}$\nSố cây mít có trong trang trại là:\n$500 \\times 20 : 100 = 100\\text{ (cây)}$\nb) Số cây bưởi ít hơn số cây xoài là:\n$500 \\times (30\\% - 15\\%) : 100 = 75\\text{ (cây)}$\nĐáp số:\na) Nhãn: 175 cây, Mít: 100 cây;\nb) 75 cây.",
                "answer": "a) Nhãn 175 cây, Mít 100 cây; b) 75 cây"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một mảnh đất hình thang có đáy lớn $50\\text{ m}$, đáy bé bằng $\\frac{3}{5}$ đáy lớn, chiều cao kém đáy bé $6\\text{ m}$.\na) Tính diện tích mảnh đất hình thang đó.\nb) Người ta dùng $35\\%$ diện tích để làm nhà và sân chơi, phần đất còn lại trồng hoa. Tính diện tích phần đất trồng hoa.",
                "solution": "Bài giải:\na) Độ dài đáy bé của mảnh đất là:\n$50 \\times 3 : 5 = 30\\text{ (m)}$\nChiều cao của mảnh đất là:\n$30 - 6 = 24\\text{ (m)}$\nDiện tích của mảnh đất hình thang là:\n$(50 + 30) \\times 24 : 2 = 960\\text{ (m}^2)$\nb) Tỉ số phần trăm diện tích trồng hoa là:\n$100\\% - 35\\% = 65\\%$\nDiện tích phần đất trồng hoa là:\n$960 \\times 65 : 100 = 624\\text{ (m}^2)$\nĐáp số:\na) $960\\text{ m}^2$;\nb) $624\\text{ m}^2$.",
                "answer": "a) 960 m²; b) 624 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 7,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một người đi xe đạp từ A với vận tốc $14\\text{ km/h}$. Sau 1 giờ 30 phút, một người đi xe máy cũng xuất phát từ A đuổi theo xe đạp với vận tốc $35\\text{ km/h}$.\na) Xe máy đuổi kịp xe đạp sau bao lâu kể từ lúc xe máy bắt đầu khởi hành?\nb) Chỗ hai xe gặp nhau cách điểm xuất phát A bao nhiêu ki-lô-mét?",
                "solution": "Bài giải:\na) Đổi: $1\\text{ giờ } 30\\text{ phút} = 1,5\\text{ giờ}$.\nTrong 1,5 giờ người đi xe đạp đi được quãng đường là:\n$14 \\times 1,5 = 21\\text{ (km)}$\nMỗi giờ xe máy đi nhanh hơn xe đạp quãng đường là:\n$35 - 14 = 21\\text{ (km)}$\nThời gian xe máy đi để đuổi kịp xe đạp là:\n$21 : 21 = 1\\text{ (giờ)}$\nb) Điểm hai xe gặp nhau cách A quãng đường là:\n$35 \\times 1 = 35\\text{ (km)}$\nĐáp số:\na) 1 giờ;\nb) $35\\text{ km}$.",
                "answer": "a) 1 giờ; b) 35 km"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 6,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Lớp 5A có số học sinh giỏi bằng $\\frac{1}{3}$ số học sinh còn lại của lớp. Sau học kì 1 có thêm 2 bạn học sinh đạt loại giỏi nên số học sinh giỏi lúc này bằng $\\frac{3}{7}$ số học sinh còn lại. Hỏi lớp 5A có tất cả bao nhiêu học sinh?",
                "solution": "Bài giải:\nLúc đầu, số học sinh giỏi bằng $\\frac{1}{3}$ số học sinh còn lại, nghĩa là số học sinh giỏi bằng:\n$1 : (1 + 3) = \\frac{1}{4}\\text{ (số học sinh cả lớp)}$\nSau học kì 1, số học sinh giỏi bằng $\\frac{3}{7}$ số học sinh còn lại, nghĩa là số học sinh giỏi bằng:\n$3 : (3 + 7) = \\frac{3}{10}\\text{ (số học sinh cả lớp)}$\nPhân số chỉ 2 học sinh giỏi tăng thêm là:\n$\\frac{3}{10} - \\frac{1}{4} = \\frac{6}{20} - \\frac{5}{20} = \\frac{1}{20}\\text{ (số học sinh cả lớp)}$\nTổng số học sinh của lớp 5A là:\n$2 : \\frac{1}{20} = 40\\text{ (học sinh)}$\nĐáp số: 40 học sinh.",
                "answer": "40 học sinh"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 06 (th5_ck2_de06)
    # =========================================================================
    exams["th5_ck2_de06"] = {
        "id": "th5_ck2_de06",
        "code": "CK2-DE06",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 06)",
        "grade": "5",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 1:** Một ca nô xuôi dòng quãng đường sông $45\\text{ km}$ hết 1,5 giờ. Vận tốc dòng nước là $3\\text{ km/h}$. Vận tốc thực của ca nô khi nước yên lặng là:",
                "options": ["$30\\text{ km/h}$", "$27\\text{ km/h}$", "$24\\text{ km/h}$", "$33\\text{ km/h}$"],
                "correct": 1,
                "explanation": "Vận tốc xuôi dòng là: $45 : 1,5 = 30\\text{ km/h}$. Vận tốc thực của ca nô là: $30 - 3 = 27\\text{ km/h}$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 2:** 2 ngày 6 giờ bằng bao nhiêu giờ?",
                "options": ["26 giờ", "48 giờ", "54 giờ", "60 giờ"],
                "correct": 2,
                "explanation": "$2\\text{ ngày } 6\\text{ giờ} = 2 \\times 24 + 6 = 54\\text{ giờ}$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 3:** Khảo sát 600 phương tiện trong bãi đỗ xe: Xe con $25\\%$, Xe máy $60\\%$, Xe đạp $10\\%$, Xe tải $5\\%$. Số lượng xe con trong bãi đỗ là:",
                "options": ["150 xe", "120 xe", "180 xe", "200 xe"],
                "correct": 0,
                "explanation": "Số lượng xe con là: $600 \\times 25 : 100 = 150$ (xe)."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 4:** Phân số $\\frac{7}{25}$ viết dưới dạng tỉ số phần trăm là:",
                "options": ["7%", "25%", "14%", "28%"],
                "correct": 3,
                "explanation": "Ta có: $\\frac{7}{25} = \\frac{7 \\times 4}{25 \\times 4} = \\frac{28}{100} = 28\\%$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Một hình tròn có chu vi $18,84\\text{ cm}$. Bán kính của hình tròn đó là:",
                "options": ["$3\\text{ cm}$", "$6\\text{ cm}$", "$4\\text{ cm}$", "$2\\text{ cm}$"],
                "correct": 0,
                "explanation": "Bán kính hình tròn là: $r = 18,84 : 3,14 : 2 = 3\\text{ cm}$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một đoàn tàu dài $150\\text{ m}$ vượt qua một cây cầu dài $450\\text{ m}$ với vận tốc $15\\text{ m/s}$. Thời gian để đoàn tàu vượt qua hoàn toàn cây cầu là:",
                "options": ["30 giây", "35 giây", "40 giây", "45 giây"],
                "correct": 2,
                "explanation": "Quãng đường đoàn tàu đi: $150 + 450 = 600\\text{ m}$. Thời gian: $600 : 15 = 40$ giây."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) 4 giờ 25 phút + 2 giờ 48 phút\nb) 9 giờ 15 phút - 4 giờ 38 phút",
                "solution": "a) 4 giờ 25 phút + 2 giờ 48 phút = 6 giờ 73 phút = 7 giờ 13 phút.\nb) 9 giờ 15 phút - 4 giờ 38 phút = 8 giờ 75 phút - 4 giờ 38 phút = 4 giờ 37 phút.",
                "answer": "a) 7 giờ 13 phút; b) 4 giờ 37 phút"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $x$, biết:\n$(x - 4,5) : 3,2 = 6,5$",
                "solution": "Ta có:\n$x - 4,5 = 6,5 \\times 3,2$\n$x - 4,5 = 20,8$\n$x = 20,8 + 4,5$\n$x = 25,3$.\nĐáp số: $x = 25,3$.",
                "answer": "x = 25,3"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một cửa hàng bán gạo thống kê 400 tấn gạo đã bán trong tháng: Gạo ST25 chiếm $40\\%$, Gạo Đài Thơm chiếm $30\\%$, Gạo Nàng Thơm chiếm $20\\%$, Gạo nếp chiếm $10\\%$.\na) Tính số tấn gạo ST25 và số tấn gạo Nàng Thơm cửa hàng đã bán.\nb) Số tấn gạo Đài Thơm nhiều hơn số tấn gạo nếp là bao nhiêu tấn?",
                "solution": "Bài giải:\na) Số tấn gạo ST25 đã bán là:\n$400 \\times 40 : 100 = 160\\text{ (tấn)}$\nSố tấn gạo Nàng Thơm đã bán là:\n$400 \\times 20 : 100 = 80\\text{ (tấn)}$\nb) Số tấn gạo Đài Thơm nhiều hơn số gạo nếp là:\n$400 \\times (30\\% - 10\\%) : 100 = 80\\text{ (tấn)}$\nĐáp số:\na) Gạo ST25: 160 tấn, Gạo Nàng Thơm: 80 tấn;\nb) 80 tấn.",
                "answer": "a) ST25: 160 tấn, Nàng Thơm: 80 tấn; b) 80 tấn"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một mảnh đất hình chữ nhật có chu vi $120\\text{ m}$, chiều rộng bằng $\\frac{3}{5}$ chiều dài.\na) Tính diện tích mảnh đất hình chữ nhật đó.\nb) Người ta đào một cái hồ nuôi cá hình tròn có đường kính $10\\text{ m}$ trên mảnh đất đó. Tính diện tích phần đất còn lại.",
                "solution": "Bài giải:\na) Nửa chu vi mảnh đất là:\n$120 : 2 = 60\\text{ (m)}$\nTổng số phần bằng nhau là:\n$3 + 5 = 8\\text{ (phần)}$\nChiều rộng của mảnh đất là:\n$60 : 8 \\times 3 = 22,5\\text{ (m)}$\nChiều dài của mảnh đất là:\n$60 - 22,5 = 37,5\\text{ (m)}$\nDiện tích của mảnh đất là:\n$37,5 \\times 22,5 = 843,75\\text{ (m}^2)$\nb) Bán kính của hồ cá hình tròn là:\n$10 : 2 = 5\\text{ (m)}$\nDiện tích hồ nuôi cá là:\n$5 \\times 5 \\times 3,14 = 78,5\\text{ (m}^2)$\nDiện tích phần đất còn lại là:\n$843,75 - 78,5 = 765,25\\text{ (m}^2)$\nĐáp số:\na) $843,75\\text{ m}^2$;\nb) $765,25\\text{ m}^2$.",
                "answer": "a) 843,75 m²; b) 765,25 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 7,
                "level": "Vận dụng",
                "question": "**Bài 5:** Quãng đường AB dài $162\\text{ km}$. Lúc 7 giờ 30 phút, một ô tô đi từ A về B với vận tốc $54\\text{ km/h}$. Cùng lúc đó một người đi xe máy từ B về A với vận tốc $36\\text{ km/h}$.\na) Hai xe gặp nhau sau bao lâu?\nb) Hai xe gặp nhau lúc mấy giờ?\nc) Điểm gặp nhau cách điểm xuất phát A bao nhiêu ki-lô-mét?",
                "solution": "Bài giải:\na) Quãng đường hai xe đi được trong một giờ là:\n$54 + 36 = 90\\text{ (km)}$\nThời gian hai xe gặp nhau là:\n$162 : 90 = 1,8\\text{ (giờ)}$\nĐổi: $1,8\\text{ giờ} = 1\\text{ giờ } 48\\text{ phút}$.\nb) Hai xe gặp nhau vào lúc:\n$7\\text{ giờ } 30\\text{ phút} + 1\\text{ giờ } 48\\text{ phút} = 9\\text{ giờ } 18\\text{ phút}$.\nc) Điểm gặp nhau cách điểm xuất phát A quãng đường là:\n$54 \\times 1,8 = 97,2\\text{ (km)}$\nĐáp số:\na) 1,8 giờ (1 giờ 48 phút);\nb) 9 giờ 18 phút;\nc) $97,2\\text{ km}$.",
                "answer": "a) 1,8 giờ; b) 9 giờ 18 phút; c) 97,2 km"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 6,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Một người đem rổ trứng ra chợ bán. Lần thứ nhất người đó bán được một nửa số trứng và thêm 1 quả. Lần thứ hai người đó bán được một nửa số trứng còn lại và thêm 1 quả. Lần thứ ba người đó bán được một nửa số trứng còn lại sau lần thứ hai và thêm 1 quả thì vừa hết trứng trong rổ. Hỏi ban đầu người đó có bao nhiêu quả trứng trong rổ?",
                "solution": "Bài giải:\nTheo phương pháp tính ngược từ cuối:\nSố trứng còn lại sau lần bán thứ hai là:\n$(0 + 1) \\times 2 = 2\\text{ (quả)}$\nSố trứng còn lại sau lần bán thứ nhất là:\n$(2 + 1) \\times 2 = 6\\text{ (quả)}$\nBan đầu trong rổ có số quả trứng là:\n$(6 + 1) \\times 2 = 14\\text{ (quả)}$\nĐáp số: 14 quả trứng.",
                "answer": "14 quả"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 07 (th5_ck2_de07)
    # =========================================================================
    exams["th5_ck2_de07"] = {
        "id": "th5_ck2_de07",
        "code": "CK2-DE07",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 07)",
        "grade": "5",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** 1 giờ 40 phút bằng bao nhiêu phút?",
                "options": ["80 phút", "100 phút", "140 phút", "120 phút"],
                "correct": 1,
                "explanation": "$1\\text{ giờ } 40\\text{ phút} = 60 + 40 = 100\\text{ phút}$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Một người đi xe đạp với vận tốc $15\\text{ km/h}$. Thời gian để xe đạp đi hết quãng đường $37,5\\text{ km}$ là:",
                "options": ["2 giờ", "2 giờ 15 phút", "2,5 giờ", "3 giờ"],
                "correct": 2,
                "explanation": "Thời gian đi là: $37,5 : 15 = 2,5$ giờ (tức 2 giờ 30 phút)."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 3:** Khảo sát môn thể thao yêu thích của 200 học sinh: Bóng rổ $25\\%$, Bơi lội $35\\%$, Điền kinh $15\\%$, Bóng đá $25\\%$. Số học sinh thích môn Bơi lội là:",
                "options": ["50 bạn", "60 bạn", "65 bạn", "70 bạn"],
                "correct": 3,
                "explanation": "Số học sinh thích bơi lội là: $200 \\times 35 : 100 = 70$ (bạn)."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 4:** Số thập phân 4,05 gấp số thập phân 0,0405 bao nhiêu lần?",
                "options": ["100 lần", "10 lần", "1000 lần", "10000 lần"],
                "correct": 0,
                "explanation": "Ta có: $4,05 : 0,0405 = 100$ lần."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Thể tích của hình hộp chữ nhật có ba kích thước lần lượt là $5\\text{ dm}, 4\\text{ dm}, 3\\text{ dm}$ là:",
                "options": ["$30\\text{ dm}^3$", "$60\\text{ dm}^3$", "$94\\text{ dm}^3$", "$120\\text{ dm}^3$"],
                "correct": 1,
                "explanation": "$V = 5 \\times 4 \\times 3 = 60\\text{ dm}^3$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Hai ô tô ở hai địa điểm cách nhau $60\\text{ km}$ và đi cùng chiều. Xe đi trước chạy với vận tốc $40\\text{ km/h}$, xe đi sau chạy với vận tốc $60\\text{ km/h}$. Thời gian để xe đi sau đuổi kịp xe đi trước là:",
                "options": ["2 giờ", "2,5 giờ", "3 giờ", "3,5 giờ"],
                "correct": 2,
                "explanation": "Hiệu vận tốc: $60 - 40 = 20\\text{ km/h}$. Thời gian đuổi kịp: $60 : 20 = 3$ giờ."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Tính giá trị phép tính sau:\na) 3 ngày 8 giờ $\\times 3$\nb) 16 phút 40 giây : 5",
                "solution": "a) 3 ngày 8 giờ $\\times 3 = 9$ ngày 24 giờ = 10 ngày.\nb) 16 phút 40 giây : 5 = 15 phút 100 giây : 5 = 3 phút 20 giây.",
                "answer": "a) 10 ngày; b) 3 phút 20 giây"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$24,6 \\times 4,5 + 24,6 \\times 5,5$",
                "solution": "Ta có:\n$24,6 \\times 4,5 + 24,6 \\times 5,5 = 24,6 \\times (4,5 + 5,5)$\n$= 24,6 \\times 10 = 246$.\nĐáp số: 246.",
                "answer": "246"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một cửa hàng thời trang bán được 1000 sản phẩm trong tháng khuyến mại. Biểu đồ hình quạt tròn cho biết: Áo thun chiếm $45\\%$, Quần jean chiếm $25\\%$, Váy chiếm $20\\%$, Áo khoác chiếm $10\\%$.\na) Tính số lượng áo thun và số lượng quần jean cửa hàng đã bán.\nb) Số lượng áo thun đã bán nhiều hơn số lượng váy bao nhiêu chiếc?",
                "solution": "Bài giải:\na) Số lượng áo thun cửa hàng đã bán là:\n$1000 \\times 45 : 100 = 450\\text{ (chiếc)}$\nSố lượng quần jean cửa hàng đã bán là:\n$1000 \\times 25 : 100 = 250\\text{ (chiếc)}$\nb) Số lượng áo thun bán nhiều hơn số lượng váy là:\n$1000 \\times (45\\% - 20\\%) : 100 = 250\\text{ (chiếc)}$\nĐáp số:\na) Áo thun: 450 chiếc, Quần jean: 250 chiếc;\nb) 250 chiếc.",
                "answer": "a) Áo thun 450, Quần jean 250; b) 250 chiếc"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một mảnh đất hình thang có tổng độ dài hai đáy là $84\\text{ m}$, chiều cao bằng $\\frac{1}{3}$ tổng độ dài hai đáy.\na) Tính diện tích mảnh đất hình thang đó.\nb) Người ta dùng $60\\%$ diện tích mảnh đất để trồng rau sạch, diện tích còn lại trồng hoa. Tính diện tích đất dùng để trồng hoa.",
                "solution": "Bài giải:\na) Chiều cao của mảnh đất hình thang là:\n$84 \\times 1 : 3 = 28\\text{ (m)}$\nDiện tích của mảnh đất hình thang là:\n$84 \\times 28 : 2 = 1176\\text{ (m}^2)$\nb) Tỉ số phần trăm diện tích đất trồng hoa là:\n$100\\% - 60\\% = 40\\%$\nDiện tích phần đất trồng hoa là:\n$1176 \\times 40 : 100 = 470,4\\text{ (m}^2)$\nĐáp số:\na) $1176\\text{ m}^2$;\nb) $470,4\\text{ m}^2$.",
                "answer": "a) 1176 m²; b) 470,4 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 7,
                "level": "Vận dụng",
                "question": "**Bài 5:** Quãng đường AB dài $175\\text{ km}$. Lúc 7 giờ sáng, một ô tô xuất phát từ A đi về B với vận tốc $50\\text{ km/h}$. Đến 7 giờ 30 phút, một xe máy cũng xuất phát từ B đi về A với vận tốc $40\\text{ km/h}$.\na) Tính quãng đường ô tô đã đi được trước khi xe máy xuất phát.\nb) Hai xe gặp nhau lúc mấy giờ?",
                "solution": "Bài giải:\na) Thời gian ô tô đi trước khi xe máy khởi hành là:\n$7\\text{ giờ } 30\\text{ phút} - 7\\text{ giờ} = 30\\text{ phút} = 0,5\\text{ giờ}$\nQuãng đường ô tô đã đi được trong 30 phút là:\n$50 \\times 0,5 = 25\\text{ (km)}$\nb) Lúc 7 giờ 30 phút khoảng cách giữa hai xe là:\n$175 - 25 = 150\\text{ (km)}$\nTổng vận tốc của hai xe là:\n$50 + 40 = 90\\text{ (km/h)}$\nThời gian kể từ lúc 7 giờ 30 phút để hai xe gặp nhau là:\n$150 : 90 = \\frac{5}{3}\\text{ (giờ)}$\nĐổi: $\\frac{5}{3}\\text{ giờ} = 1\\text{ giờ } 40\\text{ phút}$.\nHai xe gặp nhau vào lúc:\n$7\\text{ giờ } 30\\text{ phút} + 1\\text{ giờ } 40\\text{ phút} = 9\\text{ giờ } 10\\text{ phút}$.\nĐáp số:\na) $25\\text{ km}$;\nb) 9 giờ 10 phút.",
                "answer": "a) 25 km; b) 9 giờ 10 phút"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 6,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Một đàn vịt trời đang bay. Một con vịt đầu đàn nhìn xuống và cất tiếng chào: \"Chào 100 bạn vịt!\". Con vịt đầu đàn bên dưới đáp: \"Không phải chúng tôi có 100 con đâu! Số vịt chúng tôi hiện có, cộng thêm chính số vịt này nữa, thêm một nửa số vịt này, thêm một phần tư số vịt này và cả bạn nữa mới tròn 100 con!\". Hỏi đàn vịt bên dưới có tất cả bao nhiêu con?",
                "solution": "Bài giải:\nSố vịt bên dưới khi chưa tính con vịt đầu đàn nhập vào là:\n$100 - 1 = 99\\text{ (con)}$\nCoi số vịt của đàn bên dưới là 1 đơn vị (hay 4 phần bằng nhau).\nTổng số phần biểu thị số vịt là:\n$1 + 1 + \\frac{1}{2} + \\frac{1}{4} = \\frac{11}{4}\\text{ (số vịt của đàn)}$\nSố con vịt của đàn bên dưới là:\n$99 : \\frac{11}{4} = 99 \\times 4 : 11 = 36\\text{ (con)}$\nĐáp số: 36 con vịt.",
                "answer": "36 con vịt"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08 (th5_ck2_de08)
    # =========================================================================
    exams["th5_ck2_de08"] = {
        "id": "th5_ck2_de08",
        "code": "CK2-DE08",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ CUỐI HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 08)",
        "grade": "5",
        "term": "ck2",
        "termName": "Cuối Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** 0,75 ngày bằng bao nhiêu giờ?",
                "options": ["18 giờ", "15 giờ", "12 giờ", "20 giờ"],
                "correct": 0,
                "explanation": "$0,75\\text{ ngày} = 0,75 \\times 24 = 18\\text{ giờ}$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Một người đi bộ với vận tốc $4,5\\text{ km/h}$ trong 40 phút. Quãng đường người đó đi được là:",
                "options": ["$2,5\\text{ km}$", "$3\\text{ km}$", "$3,5\\text{ km}$", "$4\\text{ km}$"],
                "correct": 1,
                "explanation": "Đổi: $40\\text{ phút} = \\frac{2}{3}\\text{ giờ}$. Quãng đường: $4,5 \\times \\frac{2}{3} = 3\\text{ km}$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 3:** Khảo sát 400 học sinh về loại trái cây yêu thích: Xoài $40\\%$, Táo $30\\%$, Cam $20\\%$, Chuối $10\\%$. Số học sinh thích quả Táo là:",
                "options": ["80 bạn", "100 bạn", "120 bạn", "160 bạn"],
                "correct": 2,
                "explanation": "Số học sinh thích táo là: $400 \\times 30 : 100 = 120$ (bạn)."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 4:** Điền số thích hợp vào chỗ chấm: $3\\text{ dm}^3\\ 25\\text{ cm}^3 = \\dots\\text{ cm}^3$:",
                "options": ["325", "3250", "30025", "3025"],
                "correct": 3,
                "explanation": "$3\\text{ dm}^3\\ 25\\text{ cm}^3 = 3 \\times 1000 + 25 = 3025\\text{ cm}^3$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Diện tích hình tròn có đường kính $d = 10\\text{ cm}$ là:",
                "options": ["$31,4\\text{ cm}^2$", "$78,5\\text{ cm}^2$", "$157\\text{ cm}^2$", "$314\\text{ cm}^2$"],
                "correct": 1,
                "explanation": "Bán kính là $r = 10 : 2 = 5\\text{ cm}$. Diện tích: $5 \\times 5 \\times 3,14 = 78,5\\text{ cm}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Hai ô tô cùng xuất phát từ A đến B lúc 7 giờ. Xe thứ nhất đi với vận tốc $60\\text{ km/h}$, xe thứ hai đi với vận tốc $45\\text{ km/h}$. Đến 9 giờ 30 phút, khoảng cách giữa hai xe là:",
                "options": ["$37,5\\text{ km}$", "$30\\text{ km}$", "$25\\text{ km}$", "$45\\text{ km}$"],
                "correct": 0,
                "explanation": "Thời gian đi là 2,5 giờ. Khoảng cách: $(60 - 45) \\times 2,5 = 15 \\times 2,5 = 37,5\\text{ km}$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Tính giá trị của biểu thức sau:\na) $(15,6 + 24,4) \\times 2,5 - 45 : 1,5$\nb) 4 giờ 15 phút $\\times 3 - 5$ giờ 20 phút",
                "solution": "a) $(15,6 + 24,4) \\times 2,5 - 45 : 1,5 = 40 \\times 2,5 - 30 = 100 - 30 = 70$\nb) 4 giờ 15 phút $\\times 3 - 5$ giờ 20 phút = 12 giờ 45 phút - 5 giờ 20 phút = 7 giờ 25 phút.",
                "answer": "a) 70; b) 7 giờ 25 phút"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $x$, biết:\n$x \\times 4,5 + x \\times 5,5 = 125$",
                "solution": "Ta có:\n$x \\times (4,5 + 5,5) = 125$\n$x \\times 10 = 125$\n$x = 125 : 10$\n$x = 12,5$.\nĐáp số: $x = 12,5$.",
                "answer": "x = 12,5"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Khảo sát 800 học sinh khối lớp 5 về môn nghệ thuật yêu thích: Hội họa $35\\%$, Âm nhạc $40\\%$, Kịch nghệ $15\\%$, Múa $10\\%$.\na) Tính số học sinh yêu thích Hội họa và số học sinh yêu thích Âm nhạc.\nb) Số học sinh thích Âm nhạc nhiều hơn số học sinh thích Kịch nghệ là bao nhiêu em?",
                "solution": "Bài giải:\na) Số học sinh yêu thích Hội họa là:\n$800 \\times 35 : 100 = 280\\text{ (học sinh)}$\nSố học sinh yêu thích Âm nhạc là:\n$800 \\times 40 : 100 = 320\\text{ (học sinh)}$\nb) Số học sinh thích Âm nhạc nhiều hơn Kịch nghệ là:\n$800 \\times (40\\% - 15\\%) : 100 = 200\\text{ (học sinh)}$\nĐáp số:\na) Hội họa: 280 học sinh, Âm nhạc: 320 học sinh;\nb) 200 học sinh.",
                "answer": "a) Hội họa 280 em, Âm nhạc 320 em; b) 200 em"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một khu đất hình thang có diện tích $1200\\text{ m}^2$, chiều cao $30\\text{ m}$. Đáy bé kém đáy lớn $10\\text{ m}$.\na) Tính độ dài đáy lớn và đáy bé của khu đất đó.\nb) Người ta dành $25\\%$ diện tích khu đất để xây nhà, phần còn lại làm sân chơi và vườn cây. Tính diện tích phần đất làm sân chơi và vườn cây.",
                "solution": "Bài giải:\na) Tổng độ dài hai đáy của khu đất là:\n$1200 \\times 2 : 30 = 80\\text{ (m)}$\nĐộ dài đáy lớn là:\n$(80 + 10) : 2 = 45\\text{ (m)}$\nĐộ dài đáy bé là:\n$80 - 45 = 35\\text{ (m)}$\nb) Tỉ số phần trăm diện tích làm sân chơi và vườn cây là:\n$100\\% - 25\\% = 75\\%$\nDiện tích phần đất làm sân chơi và vườn cây là:\n$1200 \\times 75 : 100 = 900\\text{ (m}^2)$\nĐáp số:\na) Đáy lớn: $45\\text{ m}$, đáy bé: $35\\text{ m}$;\nb) $900\\text{ m}^2$.",
                "answer": "a) Đáy lớn 45 m, đáy bé 35 m; b) 900 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 7,
                "level": "Vận dụng",
                "question": "**Bài 5:** Quãng đường sông từ bến A đến bến B dài $48\\text{ km}$. Một ca nô xuôi dòng từ A đến B hết 2 giờ, sau đó ca nô ngược dòng từ B về A hết 3 giờ.\na) Tính vận tốc của ca nô khi xuôi dòng và khi ngược dòng.\nb) Tính vận tốc của dòng nước và vận tốc thực của ca nô khi nước yên lặng.",
                "solution": "Bài giải:\na) Vận tốc của ca nô khi xuôi dòng là:\n$48 : 2 = 24\\text{ (km/h)}$\nVận tốc của ca nô khi ngược dòng là:\n$48 : 3 = 16\\text{ (km/h)}$\nb) Vận tốc của dòng nước là:\n$(24 - 16) : 2 = 4\\text{ (km/h)}$\nVận tốc thực của ca nô khi nước yên lặng là:\n$24 - 4 = 20\\text{ (km/h)}$\nĐáp số:\na) Xuôi dòng: $24\\text{ km/h}$, ngược dòng: $16\\text{ km/h}$;\nb) Dòng nước: $4\\text{ km/h}$, ca nô: $20\\text{ km/h}$.",
                "answer": "a) Xuôi dòng 24 km/h, ngược dòng 16 km/h; b) Dòng nước 4 km/h, ca nô 20 km/h"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 6,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Cho tích sau:\n$A = 1 \\times 2 \\times 3 \\times \\dots \\times 25 \\times 26$.\nHỏi tích $A$ tận cùng bằng bao nhiêu chữ số 0 liên tiếp?",
                "solution": "Bài giải:\nMỗi chữ số 0 tận cùng của tích $A$ được tạo thành từ tích của một thừa số chia hết cho 2 và một thừa số chia hết cho 5 trong tích. Vì số lượng thừa số chia hết cho 2 trong dãy từ 1 đến 26 nhiều hơn số lượng thừa số chia hết cho 5, nên số chữ số 0 tận cùng bằng tổng số lần xuất hiện của thừa số 5 khi phân tích các số trong tích ra thừa số nguyên tố.\nCác số chia hết cho 5 trong dãy từ 1 đến 26 là:\n$5, 10, 15, 20, 25$.\nTrong đó:\n- Các số $5, 10, 15, 20$ mỗi số đóng góp 1 thừa số 5 (có $4 \\times 1 = 4$ thừa số 5).\n- Số $25 = 5 \\times 5$ đóng góp 2 thừa số 5.\nTổng số thừa số 5 có trong tích là:\n$4 + 2 = 6\\text{ (thừa số 5)}$\nVậy tích $A$ có tận cùng bằng 6 chữ số 0 liên tiếp.\nĐáp số: 6 chữ số 0.",
                "answer": "6 chữ số 0"
            }
        ]
    }

    return exams

if __name__ == "__main__":
    exams = get_th5_ck2_exams()
    print(f"Tổng số đề CK2 đã tạo: {len(exams)}")
    for eid, ex in exams.items():
        print(f"[{eid}] {ex['title']} - Part 1: {len(ex['part1'])} câu, Part 2: {len(ex['part2'])} bài")
