# -*- coding: utf-8 -*-
"""
HỆ THỐNG 8 ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN LỚP 5
Bộ sách: Kết nối tri thức với cuộc sống
Mã kỳ thi: th5_gk2 (Đề 01 đến Đề 08)
Chuẩn ma trận GD&ĐT và chuẩn mực sư phạm Tiểu học:
- Thời gian làm bài: 40 phút
- Thang điểm: 10.0 điểm
- Phần 1 (3.0 điểm): 6 câu trắc nghiệm khách quan 4 lựa chọn (0.5 điểm/câu)
- Phần 2 (7.0 điểm): 6 bài tự luận (1.0, 1.0, 1.0, 1.5, 1.5, 1.0 điểm) có số dòng kẻ (lineCount: 3-8)
- Tính độc lập 100% giữa các mã đề, số liệu và tình huống thực tế phong phú, chuẩn xác tuyệt đối.
"""

def get_th5_gk2_exams():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 01 (th5_gk2_de01)
    # =========================================================================
    exams["th5_gk2_de01"] = {
        "id": "th5_gk2_de01",
        "code": "GK2-DE01",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 01)",
        "grade": "5",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Viết phân số $\\frac{3}{4}$ dưới dạng tỉ số phần trăm là:",
                "options": ["34%", "75%", "30%", "70%"],
                "correct": 1,
                "explanation": "Ta có: $\\frac{3}{4} = \\frac{3 \\times 25}{4 \\times 25} = \\frac{75}{100} = 75\\%$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Số thích hợp để điền vào chỗ chấm $4,5\\text{ m}^3 = \\dots\\text{ dm}^3$ là:",
                "options": ["45", "450", "4500", "45000"],
                "correct": 2,
                "explanation": "Vì $1\\text{ m}^3 = 1000\\text{ dm}^3$ nên $4,5\\text{ m}^3 = 4,5 \\times 1000 = 4500\\text{ dm}^3$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 3:** Hình lập phương có bao nhiêu mặt, bao nhiêu cạnh và bao nhiêu đỉnh?",
                "options": [
                    "6 mặt, 12 cạnh, 8 đỉnh",
                    "6 mặt, 8 cạnh, 12 đỉnh",
                    "8 mặt, 12 cạnh, 6 đỉnh",
                    "6 mặt, 10 cạnh, 8 đỉnh"
                ],
                "correct": 0,
                "explanation": "Hình lập phương có 6 mặt là các hình vuông bằng nhau, 12 cạnh bằng nhau và 8 đỉnh."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Một lớp học có 40 học sinh, trong đó số học sinh nữ chiếm $55\\%$. Số học sinh nữ của lớp học đó là:",
                "options": ["18 học sinh", "20 học sinh", "22 học sinh", "24 học sinh"],
                "correct": 2,
                "explanation": "Số học sinh nữ của lớp là: $40 \\times 55 : 100 = 22$ (học sinh)."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Diện tích toàn phần của hình lập phương có cạnh $5\\text{ cm}$ là:",
                "options": ["$100\\text{ cm}^2$", "$125\\text{ cm}^2$", "$150\\text{ cm}^2$", "$25\\text{ cm}^2$"],
                "correct": 2,
                "explanation": "Diện tích toàn phần của hình lập phương là: $5 \\times 5 \\times 6 = 150\\text{ cm}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một khối gỗ hình hộp chữ nhật có chiều dài $8\\text{ dm}$, chiều rộng $5\\text{ dm}$ và chiều cao $4\\text{ dm}$. Thể tích khối gỗ đó là:",
                "options": ["$160\\text{ dm}^3$", "$180\\text{ dm}^3$", "$120\\text{ dm}^3$", "$80\\text{ dm}^3$"],
                "correct": 0,
                "explanation": "Thể tích của khối gỗ là: $8 \\times 5 \\times 4 = 160\\text{ dm}^3$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $34,8 + 27,65$\nb) $128,5 - 46,78$",
                "solution": "a) $34,8 + 27,65 = 62,45$\nb) $128,5 - 46,78 = 81,72$",
                "answer": "a) 62,45; b) 81,72"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$2,5 \\times 16,8 \\times 4$",
                "solution": "Ta có:\n$2,5 \\times 16,8 \\times 4 = (2,5 \\times 4) \\times 16,8$\n$= 10 \\times 16,8 = 168$.\nĐáp số: 168.",
                "answer": "168"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một cửa hàng nhập về $500\\text{ kg}$ gạo tẻ và gạo nếp, trong đó có $175\\text{ kg}$ gạo nếp. Hỏi số gạo nếp chiếm bao nhiêu phần trăm tổng số gạo cửa hàng nhập về?",
                "solution": "Bài giải:\nTỉ số phần trăm của số gạo nếp so với tổng số gạo nhập về là:\n$175 : 500 = 0,35 = 35\\%$\nĐáp số: $35\\%$.",
                "answer": "35%"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một người thợ gò một cái thùng tôn không nắp dạng hình hộp chữ nhật có chiều dài $1,5\\text{ m}$, chiều rộng $0,8\\text{ m}$ và chiều cao $0,6\\text{ m}$. Tính diện tích tôn cần dùng để làm chiếc thùng đó (không tính mép hàn).",
                "solution": "Bài giải:\nChu vi đáy của chiếc thùng tôn là:\n$(1,5 + 0,8) \\times 2 = 4,6\\text{ (m)}$\nDiện tích xung quanh của thùng tôn là:\n$4,6 \\times 0,6 = 2,76\\text{ (m}^2)$\nDiện tích đáy của chiếc thùng tôn là:\n$1,5 \\times 0,8 = 1,2\\text{ (m}^2)$\nVì thùng tôn không có nắp nên diện tích tôn cần dùng là:\n$2,76 + 1,2 = 3,96\\text{ (m}^2)$\nĐáp số: $3,96\\text{ m}^2$.",
                "answer": "3,96 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một bể nước dạng hình hộp chữ nhật có các kích thước trong lòng bể là: chiều dài $2\\text{ m}$, chiều rộng $1,5\\text{ m}$ và chiều cao $1,2\\text{ m}$.\na) Tính thể tích của bể nước đó.\nb) Hiện tại lượng nước trong bể chiếm $60\\%$ thể tích của bể. Hỏi trong bể đang có bao nhiêu lít nước? (Biết $1\\text{ dm}^3 = 1\\text{ lít}$).",
                "solution": "Bài giải:\na) Thể tích của bể nước đó là:\n$2 \\times 1,5 \\times 1,2 = 3,6\\text{ (m}^3)$\nĐổi: $3,6\\text{ m}^3 = 3600\\text{ dm}^3 = 3600\\text{ lít}$.\nb) Lượng nước hiện đang có trong bể là:\n$3600 \\times 60 : 100 = 2160\\text{ (lít)}$\nĐáp số:\na) $3,6\\text{ m}^3$;\nb) $2160\\text{ lít}$.",
                "answer": "a) 3,6 m³; b) 2160 lít"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Một cửa hàng bán một chiếc xe đạp với giá $2\\,400\\,000$ đồng. Tính ra cửa hàng được lãi $20\\%$ so với giá vốn. Hỏi giá vốn của chiếc xe đạp đó là bao nhiêu đồng?",
                "solution": "Bài giải:\nCoi giá vốn của chiếc xe đạp là $100\\%$.\nGiá bán chiếc xe đạp chiếm số phần trăm giá vốn là:\n$100\\% + 20\\% = 120\\%$\nGiá vốn của chiếc xe đạp đó là:\n$2\\,400\\,000 : 120 \\times 100 = 2\\,000\\,000\\text{ (đồng)}$\nĐáp số: $2\\,000\\,000\\text{ đồng}$.",
                "answer": "2 000 000 đồng"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 02 (th5_gk2_de02)
    # =========================================================================
    exams["th5_gk2_de02"] = {
        "id": "th5_gk2_de02",
        "code": "GK2-DE02",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 02)",
        "grade": "5",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Số thập phân $0,325$ viết dưới dạng tỉ số phần trăm là:",
                "options": ["3,25%", "32,5%", "325%", "0,325%"],
                "correct": 1,
                "explanation": "Ta nhân $0,325$ với $100$ rồi viết thêm kí hiệu $\\%$: $0,325 = 32,5\\%$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** $2500\\text{ cm}^3$ bằng bao nhiêu đề-xi-mét khối?",
                "options": ["$2,5\\text{ dm}^3$", "$25\\text{ dm}^3$", "$0,25\\text{ dm}^3$", "$250\\text{ dm}^3$"],
                "correct": 0,
                "explanation": "Vì $1\\text{ dm}^3 = 1000\\text{ cm}^3$ nên $2500\\text{ cm}^3 = 2500 : 1000 = 2,5\\text{ dm}^3$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 3:** Muốn tính diện tích xung quanh của hình hộp chữ nhật, ta lấy chu vi mặt đáy nhân với:",
                "options": ["Chiều dài", "Chiều rộng", "Chiều cao (cùng đơn vị đo)", "Diện tích đáy"],
                "correct": 2,
                "explanation": "Công thức tính diện tích xung quanh hình hộp chữ nhật: $S_{xq} = C_{đáy} \\times h$ (cùng đơn vị đo)."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Một mảnh vườn hình chữ nhật có diện tích $360\\text{ m}^2$. Người ta dành $25\\%$ diện tích để trồng rau. Diện tích đất trồng rau là:",
                "options": ["$60\\text{ m}^2$", "$75\\text{ m}^2$", "$80\\text{ m}^2$", "$90\\text{ m}^2$"],
                "correct": 3,
                "explanation": "Diện tích trồng rau là: $360 \\times 25 : 100 = 90\\text{ m}^2$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Một hình lập phương có cạnh bằng $3\\text{ dm}$. Thể tích của hình lập phương đó là:",
                "options": ["$9\\text{ dm}^3$", "$27\\text{ dm}^3$", "$54\\text{ dm}^3$", "$81\\text{ dm}^3$"],
                "correct": 1,
                "explanation": "Thể tích hình lập phương là: $V = 3 \\times 3 \\times 3 = 27\\text{ dm}^3$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một hình hộp chữ nhật có diện tích đáy là $24\\text{ cm}^2$ và chiều cao là $5\\text{ cm}$. Thể tích của hình hộp chữ nhật đó là:",
                "options": ["$60\\text{ cm}^3$", "$100\\text{ cm}^3$", "$120\\text{ cm}^3$", "$144\\text{ cm}^3$"],
                "correct": 2,
                "explanation": "Thể tích hình hộp chữ nhật là: $V = S_{đáy} \\times h = 24 \\times 5 = 120\\text{ cm}^3$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $15,6 \\times 4,5$\nb) $75,52 : 3,2$",
                "solution": "a) $15,6 \\times 4,5 = 70,2$\nb) $75,52 : 3,2 = 23,6$",
                "answer": "a) 70,2; b) 23,6"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $x$, biết:\n$x \\times 4,8 = 14,4 \\times 2$",
                "solution": "Ta có:\n$x \\times 4,8 = 28,8$\n$x = 28,8 : 4,8$\n$x = 6$.\nĐáp số: $x = 6$.",
                "answer": "x = 6"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Khảo sát 200 học sinh khối lớp 5 của một trường tiểu học, người ta thấy có 156 bạn thích học môn Toán. Hỏi số học sinh thích môn Toán chiếm bao nhiêu phần trăm tổng số học sinh khối lớp 5?",
                "solution": "Bài giải:\nTỉ số phần trăm số học sinh thích môn Toán so với tổng số học sinh khối 5 là:\n$156 : 200 = 0,78 = 78\\%$\nĐáp số: $78\\%$.",
                "answer": "78%"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Người ta sơn toàn bộ mặt ngoài của một chiếc thùng gỗ có nắp dạng hình lập phương cạnh $0,9\\text{ m}$.\na) Tính diện tích cần sơn của chiếc thùng đó.\nb) Biết giá tiền sơn mỗi mét vuông là $40\\,000$ đồng. Hỏi sơn chiếc thùng đó hết bao nhiêu tiền?",
                "solution": "Bài giải:\na) Chiếc thùng gỗ có nắp gồm 6 mặt hình vuông. Diện tích cần sơn của chiếc thùng là:\n$0,9 \\times 0,9 \\times 6 = 4,86\\text{ (m}^2)$\nb) Số tiền dùng để sơn chiếc thùng đó là:\n$4,86 \\times 40\\,000 = 194\\,400\\text{ (đồng)}$\nĐáp số:\na) $4,86\\text{ m}^2$;\nb) $194\\,400\\text{ đồng}$.",
                "answer": "a) 4,86 m²; b) 194 400 đồng"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một bể cá hình hộp chữ nhật có chiều dài $80\\text{ cm}$, chiều rộng $50\\text{ cm}$ và chiều cao $45\\text{ cm}$. Người ta đổ vào bể một lượng nước cao $30\\text{ cm}$.\na) Tính thể tích nước đang có trong bể theo đơn vị lít ($1\\text{ dm}^3 = 1\\text{ lít}$).\nb) Sau đó người ta thả một hòn đá cảnh chìm hoàn toàn vào bể thì thấy mực nước dâng lên cao $34\\text{ cm}$. Tính thể tích của hòn đá cảnh đó.",
                "solution": "Bài giải:\nĐổi: $80\\text{ cm} = 8\\text{ dm}$; $50\\text{ cm} = 5\\text{ dm}$; $30\\text{ cm} = 3\\text{ dm}$; $34\\text{ cm} = 3,4\\text{ dm}$.\na) Thể tích nước đang có trong bể là:\n$8 \\times 5 \\times 3 = 120\\text{ (dm}^3) = 120\\text{ (lít)}$\nb) Mực nước trong bể dâng thêm là:\n$3,4 - 3 = 0,4\\text{ (dm)}$\nThể tích của hòn đá cảnh bằng thể tích nước dâng thêm là:\n$8 \\times 5 \\times 0,4 = 16\\text{ (dm}^3)$\nĐáp số:\na) $120\\text{ lít}$;\nb) $16\\text{ dm}^3$.",
                "answer": "a) 120 lít; b) 16 dm³"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Nếu cạnh của một hình lập phương tăng lên 2 lần thì:\na) Diện tích toàn phần của hình lập phương tăng lên bao nhiêu lần?\nb) Thể tích của hình lập phương đó tăng lên bao nhiêu lần?",
                "solution": "Bài giải:\nGọi cạnh của hình lập phương ban đầu là $a$. Khi tăng cạnh lên 2 lần thì cạnh mới là $a \\times 2$.\na) Diện tích toàn phần ban đầu là: $a \\times a \\times 6$.\nDiện tích toàn phần mới là:\n$(a \\times 2) \\times (a \\times 2) \\times 6 = (a \\times a \\times 6) \\times 4$.\nVậy diện tích toàn phần tăng lên 4 lần.\nb) Thể tích ban đầu là: $a \\times a \\times a$.\nThể tích mới là:\n$(a \\times 2) \\times (a \\times 2) \\times (a \\times 2) = (a \\times a \\times a) \\times 8$.\nVậy thể tích tăng lên 8 lần.\nĐáp số:\na) Tăng 4 lần;\nb) Tăng 8 lần.",
                "answer": "a) Tăng 4 lần; b) Tăng 8 lần"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 03 (th5_gk2_de03)
    # =========================================================================
    exams["th5_gk2_de03"] = {
        "id": "th5_gk2_de03",
        "code": "GK2-DE03",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 03)",
        "grade": "5",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Tỉ số phần trăm của hai số 18 và 72 là:",
                "options": ["25%", "20%", "30%", "24%"],
                "correct": 0,
                "explanation": "Ta có: $18 : 72 = 0,25 = 25\\%$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Điền số thích hợp vào chỗ chấm: $3\\text{ m}^3\\ 45\\text{ dm}^3 = \\dots\\text{ dm}^3$:",
                "options": ["345", "3045", "3450", "30045"],
                "correct": 1,
                "explanation": "Vì $3\\text{ m}^3 = 3000\\text{ dm}^3$ nên $3\\text{ m}^3\\ 45\\text{ dm}^3 = 3000 + 45 = 3045\\text{ dm}^3$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 3:** Diện tích xung quanh của hình lập phương có cạnh $a$ được tính bằng công thức:",
                "options": ["$S_{xq} = a \\times a \\times 6$", "$S_{xq} = a \\times a \\times a$", "$S_{xq} = a \\times a \\times 4$", "$S_{xq} = a \\times 4$"],
                "correct": 2,
                "explanation": "Hình lập phương có 4 mặt xung quanh bằng nhau, do đó: $S_{xq} = a \\times a \\times 4$."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Tìm $15\\%$ của 240 lít nước:",
                "options": ["24 lít", "30 lít", "32 lít", "36 lít"],
                "correct": 3,
                "explanation": "$15\\%$ của 240 lít là: $240 \\times 15 : 100 = 36$ (lít)."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Một cái hộp hình chữ nhật có chiều dài $12\\text{ cm}$, chiều rộng $8\\text{ cm}$ và chiều cao $10\\text{ cm}$. Diện tích xung quanh của chiếc hộp là:",
                "options": ["$400\\text{ cm}^2$", "$200\\text{ cm}^2$", "$960\\text{ cm}^2$", "$592\\text{ cm}^2$"],
                "correct": 0,
                "explanation": "$S_{xq} = (12 + 8) \\times 2 \\times 10 = 40 \\times 10 = 400\\text{ cm}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Người ta xếp 64 khối lập phương nhỏ cạnh $1\\text{ cm}$ thành một khối lập phương lớn. Thể tích của khối lập phương lớn đó là:",
                "options": ["$16\\text{ cm}^3$", "$64\\text{ cm}^3$", "$96\\text{ cm}^3$", "$256\\text{ cm}^3$"],
                "correct": 1,
                "explanation": "Mỗi khối nhỏ có thể tích $1\\text{ cm}^3$. Do đó 64 khối có thể tích là: $64 \\times 1 = 64\\text{ cm}^3$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Tính giá trị của biểu thức:\na) $(38,4 + 19,6) \\times 2,5$\nb) $84,6 - 21,6 : 1,2$",
                "solution": "a) $(38,4 + 19,6) \\times 2,5 = 58 \\times 2,5 = 145$\nb) $84,6 - 21,6 : 1,2 = 84,6 - 18 = 66,6$",
                "answer": "a) 145; b) 66,6"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$36,5 \\times 7,4 + 36,5 \\times 2,6$",
                "solution": "Ta có:\n$36,5 \\times 7,4 + 36,5 \\times 2,6 = 36,5 \\times (7,4 + 2,6)$\n$= 36,5 \\times 10 = 365$.\nĐáp số: 365.",
                "answer": "365"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một vườn cây ăn quả có tất cả 1200 cây, trong đó có $45\\%$ là cây cam, $35\\%$ là cây bưởi, còn lại là cây xoài. Tính số cây xoài có trong vườn cây đó.",
                "solution": "Bài giải:\nTỉ số phần trăm số cây xoài trong vườn là:\n$100\\% - 45\\% - 35\\% = 20\\%$\nSố cây xoài có trong vườn là:\n$1200 \\times 20 : 100 = 240\\text{ (cây)}$\nĐáp số: 240 cây.",
                "answer": "240 cây"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một lớp học có chiều dài $8\\text{ m}$, chiều rộng $6\\text{ m}$ và chiều cao $3,5\\text{ m}$. Người ta quét vôi trần nhà và 4 bức tường phía trong phòng học. Biết diện tích các cửa sổ và cửa ra vào là $12,5\\text{ m}^2$. Tính diện tích cần quét vôi của lớp học đó.",
                "solution": "Bài giải:\nDiện tích xung quanh của phòng học là:\n$(8 + 6) \\times 2 \\times 3,5 = 98\\text{ (m}^2)$\nDiện tích trần nhà của phòng học là:\n$8 \\times 6 = 48\\text{ (m}^2)$\nTổng diện tích tường và trần nhà là:\n$98 + 48 = 146\\text{ (m}^2)$\nDiện tích cần quét vôi của lớp học là:\n$146 - 12,5 = 133,5\\text{ (m}^2)$\nĐáp số: $133,5\\text{ m}^2$.",
                "answer": "133,5 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một bể kính nuôi cá không có nắp dạng hình hộp chữ nhật có chiều dài $1,2\\text{ m}$, chiều rộng $0,5\\text{ m}$ và chiều cao $0,6\\text{ m}$.\na) Tính diện tích kính dùng làm bể cá đó.\nb) Người ta mở một vòi nước chảy vào bể (bể ban đầu không có nước), mỗi phút chảy được 20 lít nước. Hỏi sau bao lâu thì lượng nước trong bể chiếm $80\\%$ thể tích của bể?",
                "solution": "Bài giải:\na) Diện tích xung quanh của bể cá là:\n$(1,2 + 0,5) \\times 2 \\times 0,6 = 2,04\\text{ (m}^2)$\nDiện tích đáy bể kính là:\n$1,2 \\times 0,5 = 0,6\\text{ (m}^2)$\nVì bể không có nắp nên diện tích kính làm bể là:\n$2,04 + 0,6 = 2,64\\text{ (m}^2)$\nb) Thể tích của bể kính nuôi cá là:\n$1,2 \\times 0,5 \\times 0,6 = 0,36\\text{ (m}^3)$\nĐổi: $0,36\\text{ m}^3 = 360\\text{ dm}^3 = 360\\text{ lít}$.\nLượng nước chiếm $80\\%$ thể tích bể là:\n$360 \\times 80 : 100 = 288\\text{ (lít)}$\nThời gian để vòi chảy được lượng nước trên là:\n$288 : 20 = 14,4\\text{ (phút)}$\nĐổi: $14,4\\text{ phút} = 14\\text{ phút } 24\\text{ giây}$.\nĐáp số:\na) $2,64\\text{ m}^2$;\nb) $14,4\\text{ phút (hoặc 14 phút 24 giây)}$.",
                "answer": "a) 2,64 m²; b) 14,4 phút"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Bác Ba gửi tiết kiệm $150\\,000\\,000$ đồng vào ngân hàng với lãi suất $6\\%$ một năm. Hỏi sau một năm, cả số tiền gửi ban đầu và số tiền lãi bác Ba nhận được tất cả là bao nhiêu đồng?",
                "solution": "Bài giải:\nSố tiền lãi bác Ba nhận được sau một năm là:\n$150\\,000\\,000 \\times 6 : 100 = 9\\,000\\,000\\text{ (đồng)}$\nSau một năm, tổng số tiền bác Ba nhận được là:\n$150\\,000\\,000 + 9\\,000\\,000 = 159\\,000\\,000\\text{ (đồng)}$\nĐáp số: $159\\,000\\,000\\text{ đồng}$.",
                "answer": "159 000 000 đồng"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 04 (th5_gk2_de04)
    # =========================================================================
    exams["th5_gk2_de04"] = {
        "id": "th5_gk2_de04",
        "code": "GK2-DE04",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 04)",
        "grade": "5",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Phân số $\\frac{3}{8}$ được viết dưới dạng tỉ số phần trăm là:",
                "options": ["38%", "37%", "37,5%", "38,5%"],
                "correct": 2,
                "explanation": "Ta có: $\\frac{3}{8} = 3 : 8 = 0,375 = 37,5\\%$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Dấu thích hợp để điền vào chỗ chấm $4,05\\text{ m}^3 \\dots 4050\\text{ dm}^3$ là:",
                "options": ["$=$", "$<$", "$>$", "Không so sánh được"],
                "correct": 0,
                "explanation": "Vì $4,05\\text{ m}^3 = 4,05 \\times 1000 = 4050\\text{ dm}^3$ nên hai giá trị bằng nhau."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 3:** Thể tích của hình hộp chữ nhật có ba kích thước $a, b, c$ (cùng đơn vị đo) được tính theo công thức:",
                "options": ["$V = (a + b) \\times c$", "$V = a \\times b \\times c$", "$V = (a + b) \\times 2 \\times c$", "$V = a \\times b + c$"],
                "correct": 1,
                "explanation": "Thể tích hình hộp chữ nhật bằng tích của chiều dài, chiều rộng và chiều cao: $V = a \\times b \\times c$."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Một thư viện trường học có 1500 quyển sách, trong đó sách giáo khoa chiếm $60\\%$. Số sách giáo khoa có trong thư viện là:",
                "options": ["600 quyển", "750 quyển", "900 quyển", "1000 quyển"],
                "correct": 2,
                "explanation": "Số sách giáo khoa là: $1500 \\times 60 : 100 = 900$ (quyển)."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Một hình lập phương có diện tích một mặt là $16\\text{ cm}^2$. Diện tích toàn phần của hình lập phương đó là:",
                "options": ["$64\\text{ cm}^2$", "$80\\text{ cm}^2$", "$96\\text{ cm}^2$", "$256\\text{ cm}^2$"],
                "correct": 2,
                "explanation": "Diện tích toàn phần của hình lập phương là: $16 \\times 6 = 96\\text{ cm}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một khối kim loại hình lập phương có cạnh $0,2\\text{ m}$. Thể tích của khối kim loại đó là:",
                "options": ["$0,08\\text{ m}^3$", "$0,008\\text{ m}^3$", "$0,8\\text{ m}^3$", "$8\\text{ m}^3$"],
                "correct": 1,
                "explanation": "Thể tích khối kim loại là: $0,2 \\times 0,2 \\times 0,2 = 0,008\\text{ m}^3$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $45,67 + 89,5$\nb) $23,4 \\times 3,05$",
                "solution": "a) $45,67 + 89,5 = 135,17$\nb) $23,4 \\times 3,05 = 71,37$",
                "answer": "a) 135,17; b) 71,37"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $y$, biết:\n$y : 3,6 = 15,2 - 8,7$",
                "solution": "Ta có:\n$y : 3,6 = 6,5$\n$y = 6,5 \\times 3,6$\n$y = 23,4$.\nĐáp số: $y = 23,4$.",
                "answer": "y = 23,4"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một trang trại chăn nuôi gia cầm có tất cả 2500 con gồm gà và vịt, trong đó có 875 con vịt.\na) Số con vịt chiếm bao nhiêu phần trăm tổng số gia cầm?\nb) Số con gà chiếm bao nhiêu phần trăm tổng số gia cầm?",
                "solution": "Bài giải:\na) Tỉ số phần trăm của số con vịt so với tổng số gia cầm là:\n$875 : 2500 = 0,35 = 35\\%$\nb) Tỉ số phần trăm của số con gà so với tổng số gia cầm là:\n$100\\% - 35\\% = 65\\%$\nĐáp số:\na) $35\\%$;\nb) $65\\%$.",
                "answer": "a) 35%; b) 65%"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một cái thùng không nắp hình hộp chữ nhật có chiều dài $1,8\\text{ m}$, chiều rộng $1,2\\text{ m}$ và chiều cao $0,8\\text{ m}$. Người ta sơn mặt trong và mặt ngoài của chiếc thùng đó.\na) Tính diện tích toàn bộ bề mặt cần sơn của chiếc thùng đó.\nb) Biết cứ sơn $1\\text{ m}^2$ thì hết $0,2\\text{ kg}$ sơn. Hỏi người ta phải dùng bao nhiêu ki-lô-gam sơn?",
                "solution": "Bài giải:\na) Diện tích xung quanh của chiếc thùng là:\n$(1,8 + 1,2) \\times 2 \\times 0,8 = 4,8\\text{ (m}^2)$\nDiện tích đáy của chiếc thùng là:\n$1,8 \\times 1,2 = 2,16\\text{ (m}^2)$\nVì thùng không có nắp nên diện tích một bề mặt sơn là:\n$4,8 + 2,16 = 6,96\\text{ (m}^2)$\nTổng diện tích toàn bộ bề mặt cần sơn (cả trong lẫn ngoài) là:\n$6,96 \\times 2 = 13,92\\text{ (m}^2)$\nb) Lượng sơn cần dùng là:\n$13,92 \\times 0,2 = 2,784\\text{ (kg)}$\nĐáp số:\na) $13,92\\text{ m}^2$;\nb) $2,784\\text{ kg}$.",
                "answer": "a) 13,92 m²; b) 2,784 kg"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một bể chứa nước dạng hình lập phương có cạnh bằng $1,5\\text{ m}$.\na) Tính thể tích của bể nước đó theo đơn vị mét khối.\nb) Khi bể đang chứa đầy nước, người ta mở một vòi xả nước ra với lưu lượng 25 lít mỗi phút. Hỏi sau 1 giờ 30 phút, lượng nước còn lại trong bể là bao nhiêu lít?",
                "solution": "Bài giải:\na) Thể tích của bể nước dạng hình lập phương là:\n$1,5 \\times 1,5 \\times 1,5 = 3,375\\text{ (m}^3)$\nĐổi: $3,375\\text{ m}^3 = 3375\\text{ dm}^3 = 3375\\text{ lít}$.\nb) Đổi: $1\\text{ giờ } 30\\text{ phút} = 90\\text{ phút}$.\nLượng nước vòi đã xả ra sau 90 phút là:\n$25 \\times 90 = 2250\\text{ (lít)}$\nLượng nước còn lại trong bể là:\n$3375 - 2250 = 1125\\text{ (lít)}$\nĐáp số:\na) $3,375\\text{ m}^3$;\nb) $1125\\text{ lít}$.",
                "answer": "a) 3,375 m³; b) 1125 lít"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Nhân dịp khai trương, một siêu thị điện máy giảm giá $15\\%$ cho tất cả các mặt hàng. Mẹ bạn Lan mua một chiếc nồi cơm điện với giá niêm yết là $1\\,200\\,000$ đồng. Hỏi mẹ Lan phải trả cho chiếc nồi cơm điện đó bao nhiêu tiền?",
                "solution": "Bài giải:\nSố tiền mẹ bạn Lan được giảm giá là:\n$1\\,200\\,000 \\times 15 : 100 = 180\\,000\\text{ (đồng)}$\nSố tiền mẹ Lan phải trả để mua chiếc nồi cơm điện là:\n$1\\,200\\,000 - 180\\,000 = 1\\,020\\,000\\text{ (đồng)}$\nĐáp số: $1\\,020\\,000\\text{ đồng}$.",
                "answer": "1 020 000 đồng"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 05 (th5_gk2_de05)
    # =========================================================================
    exams["th5_gk2_de05"] = {
        "id": "th5_gk2_de05",
        "code": "GK2-DE05",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 05)",
        "grade": "5",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Biết $20\\%$ của một số là 45. Số đó là:",
                "options": ["90", "225", "200", "250"],
                "correct": 1,
                "explanation": "Số đó là: $45 : 20 \\times 100 = 225$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Số đo $56\\,000\\text{ cm}^3$ bằng bao nhiêu đề-xi-mét khối?",
                "options": ["$56\\text{ dm}^3$", "$560\\text{ dm}^3$", "$5,6\\text{ dm}^3$", "$0,56\\text{ dm}^3$"],
                "correct": 0,
                "explanation": "$56\\,000\\text{ cm}^3 = 56\\,000 : 1000 = 56\\text{ dm}^3$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 3:** Một hình lập phương có cạnh $4\\text{ cm}$. Diện tích xung quanh của nó là:",
                "options": ["$16\\text{ cm}^2$", "$32\\text{ cm}^2$", "$64\\text{ cm}^2$", "$96\\text{ cm}^2$"],
                "correct": 2,
                "explanation": "Diện tích xung quanh là: $4 \\times 4 \\times 4 = 64\\text{ cm}^2$."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Một tổ công nhân dự định may 800 chiếc áo, đến nay đã may được 640 chiếc áo. Tổ đó đã hoàn thành được bao nhiêu phần trăm kế hoạch?",
                "options": ["75%", "78%", "82%", "80%"],
                "correct": 3,
                "explanation": "Tỉ số phần trăm đã hoàn thành là: $640 : 800 = 0,8 = 80\\%$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Một hình hộp chữ nhật có thể tích $180\\text{ cm}^3$, chiều dài $9\\text{ cm}$ và chiều rộng $5\\text{ cm}$. Chiều cao của hình hộp chữ nhật đó là:",
                "options": ["$4\\text{ cm}$", "$5\\text{ cm}$", "$6\\text{ cm}$", "$8\\text{ cm}$"],
                "correct": 0,
                "explanation": "Chiều cao của hình hộp chữ nhật là: $180 : (9 \\times 5) = 180 : 45 = 4\\text{ cm}$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một can dầu có thể tích $0,025\\text{ m}^3$. Can dầu đó chứa được tối đa bao nhiêu lít dầu? (Biết $1\\text{ dm}^3 = 1\\text{ lít}$).",
                "options": ["2,5 lít", "250 lít", "25 lít", "0,25 lít"],
                "correct": 2,
                "explanation": "Đổi: $0,025\\text{ m}^3 = 0,025 \\times 1000 = 25\\text{ dm}^3 = 25\\text{ lít}$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $154,32 - 78,56$\nb) $216,72 : 4,2$",
                "solution": "a) $154,32 - 78,56 = 75,76$\nb) $216,72 : 4,2 = 51,6$",
                "answer": "a) 75,76; b) 51,6"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$0,4 \\times 84,7 \\times 25$",
                "solution": "Ta có:\n$0,4 \\times 84,7 \\times 25 = (0,4 \\times 25) \\times 84,7$\n$= 10 \\times 84,7 = 847$.\nĐáp số: 847.",
                "answer": "847"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Năm nay xã Tân Tiến thu hoạch được 420 tấn thóc, đạt $105\\%$ kế hoạch đề ra cho cả năm. Hỏi theo kế hoạch ban đầu, xã Tân Tiến dự định thu hoạch bao nhiêu tấn thóc?",
                "solution": "Bài giải:\nTheo kế hoạch ban đầu, số tấn thóc xã Tân Tiến dự định thu hoạch là:\n$420 : 105 \\times 100 = 400\\text{ (tấn)}$\nĐáp số: 400 tấn thóc.",
                "answer": "400 tấn"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Người ta làm một chiếc khung sắt dạng hình hộp chữ nhật có chiều dài $2,4\\text{ m}$, chiều rộng $1,6\\text{ m}$ và chiều cao $1,5\\text{ m}$.\na) Tính tổng độ dài của tất cả các thanh sắt cần dùng để làm chiếc khung đó.\nb) Người ta bọc kín xung quanh và 2 đáy của chiếc khung bằng bạt nhựa. Tính diện tích bạt nhựa cần dùng (coi mép nối không đáng kể).",
                "solution": "Bài giải:\na) Hình hộp chữ nhật có 4 cạnh chiều dài, 4 cạnh chiều rộng và 4 cạnh chiều cao.\nTổng độ dài các thanh sắt cần dùng là:\n$(2,4 + 1,6 + 1,5) \\times 4 = 5,5 \\times 4 = 22\\text{ (m)}$\nb) Diện tích xung quanh chiếc khung là:\n$(2,4 + 1,6) \\times 2 \\times 1,5 = 12\\text{ (m}^2)$\nDiện tích hai mặt đáy của chiếc khung là:\n$2 \\times (2,4 \\times 1,6) = 7,68\\text{ (m}^2)$\nDiện tích bạt nhựa cần dùng để bọc kín chiếc khung là:\n$12 + 7,68 = 19,68\\text{ (m}^2)$\nĐáp số:\na) $22\\text{ m}$;\nb) $19,68\\text{ m}^2$.",
                "answer": "a) 22 m; b) 19,68 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một cái bể chứa nước hình hộp chữ nhật có chiều dài $2,5\\text{ m}$, chiều rộng $1,8\\text{ m}$ và chiều cao $1,4\\text{ m}$. Bể hiện đang cạn nước.\na) Tính dung tích của bể nước theo đơn vị lít.\nb) Người ta mở hai vòi cùng chảy vào bể. Vòi thứ nhất mỗi phút chảy được 35 lít, vòi thứ hai mỗi phút chảy được 40 lít. Hỏi sau bao lâu kể từ lúc mở vòi thì lượng nước trong bể đạt $75\\%$ thể tích của bể?",
                "solution": "Bài giải:\na) Thể tích của bể nước đó là:\n$2,5 \\times 1,8 \\times 1,4 = 6,3\\text{ (m}^3)$\nĐổi: $6,3\\text{ m}^3 = 6300\\text{ dm}^3 = 6300\\text{ lít}$.\nb) Lượng nước khi bể đạt $75\\%$ thể tích là:\n$6300 \\times 75 : 100 = 4725\\text{ (lít)}$\nMỗi phút cả hai vòi cùng chảy được số lít nước là:\n$35 + 40 = 75\\text{ (lít)}$\nThời gian để hai vòi chảy được lượng nước trên là:\n$4725 : 75 = 63\\text{ (phút)}$\nĐổi: $63\\text{ phút} = 1\\text{ giờ } 3\\text{ phút}$.\nĐáp số:\na) $6300\\text{ lít}$;\nb) $63\\text{ phút (hoặc 1 giờ 3 phút)}$.",
                "answer": "a) 6300 lít; b) 63 phút"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Một hình hộp chữ nhật có chiều dài $a$, chiều rộng $b$ và chiều cao $c$. Nếu người ta tăng chiều dài thêm $20\\%$, giảm chiều rộng đi $20\\%$ và giữ nguyên chiều cao thì thể tích của hình hộp chữ nhật thay đổi như thế nào?",
                "solution": "Bài giải:\nThể tích ban đầu của hình hộp chữ nhật là: $V_1 = a \\times b \\times c$.\nKhi tăng chiều dài $20\\%$, chiều dài mới là: $100\\% + 20\\% = 120\\% = 1,2 \\times a$.\nKhi giảm chiều rộng $20\\%$, chiều rộng mới là: $100\\% - 20\\% = 80\\% = 0,8 \\times b$.\nThể tích mới của hình hộp chữ nhật là:\n$V_2 = (1,2 \\times a) \\times (0,8 \\times b) \\times c = (1,2 \\times 0,8) \\times (a \\times b \\times c) = 0,96 \\times V_1 = 96\\% \\times V_1$.\nSo với thể tích ban đầu, thể tích mới đã giảm đi số phần trăm là:\n$100\\% - 96\\% = 4\\%$.\nĐáp số: Thể tích giảm đi $4\\%$.",
                "answer": "Giảm đi 4%"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 06 (th5_gk2_de06)
    # =========================================================================
    exams["th5_gk2_de06"] = {
        "id": "th5_gk2_de06",
        "code": "GK2-DE06",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 06)",
        "grade": "5",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Tỉ số phần trăm của hai số 45 và 60 là:",
                "options": ["70%", "80%", "75%", "65%"],
                "correct": 2,
                "explanation": "Ta có: $45 : 60 = 0,75 = 75\\%$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Điền số thích hợp vào chỗ chấm: $7,2\\text{ dm}^3 = \\dots\\text{ cm}^3$:",
                "options": ["720", "7200", "72", "72000"],
                "correct": 1,
                "explanation": "$7,2\\text{ dm}^3 = 7,2 \\times 1000 = 7200\\text{ cm}^3$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 3:** Diện tích toàn phần của hình lập phương có cạnh dài $6\\text{ cm}$ là:",
                "options": ["$36\\text{ cm}^2$", "$144\\text{ cm}^2$", "$180\\text{ cm}^2$", "$216\\text{ cm}^2$"],
                "correct": 3,
                "explanation": "$S_{tp} = 6 \\times 6 \\times 6 = 216\\text{ cm}^2$."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Một mảnh đất hình chữ nhật có diện tích $500\\text{ m}^2$. Người ta dùng $40\\%$ diện tích mảnh đất để xây nhà. Diện tích đất xây nhà là:",
                "options": ["$200\\text{ m}^2$", "$250\\text{ m}^2$", "$150\\text{ m}^2$", "$300\\text{ m}^2$"],
                "correct": 0,
                "explanation": "Diện tích đất xây nhà là: $500 \\times 40 : 100 = 200\\text{ m}^2$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Một hình hộp chữ nhật có chiều dài $10\\text{ dm}$, chiều rộng $6\\text{ dm}$ và chiều cao $4\\text{ dm}$. Thể tích của hình hộp chữ nhật đó là:",
                "options": ["$120\\text{ dm}^3$", "$240\\text{ dm}^3$", "$200\\text{ dm}^3$", "$280\\text{ dm}^3$"],
                "correct": 1,
                "explanation": "Thể tích hình hộp chữ nhật là: $10 \\times 6 \\times 4 = 240\\text{ dm}^3$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Biết $25\\%$ của số $A$ là 60. Số $A$ là:",
                "options": ["150", "200", "240", "300"],
                "correct": 2,
                "explanation": "Số $A$ là: $60 : 25 \\times 100 = 240$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Tính giá trị biểu thức:\na) $14,75 \\times 4 + 25,6 : 0,8$\nb) $(125,4 - 45,4) : 2,5$",
                "solution": "a) $14,75 \\times 4 + 25,6 : 0,8 = 59 + 32 = 91$\nb) $(125,4 - 45,4) : 2,5 = 80 : 2,5 = 32$",
                "answer": "a) 91; b) 32"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $x$, biết:\n$x \\times 3,5 + x \\times 6,5 = 245$",
                "solution": "Ta có:\n$x \\times (3,5 + 6,5) = 245$\n$x \\times 10 = 245$\n$x = 245 : 10$\n$x = 24,5$.\nĐáp số: $x = 24,5$.",
                "answer": "x = 24,5"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một trường tiểu học có 800 học sinh. Đợt kiểm tra vừa qua có 440 bạn đạt danh hiệu Xuất sắc, 260 bạn đạt danh hiệu Tiêu biểu, còn lại là các bạn Hoàn thành tốt. Hỏi số học sinh đạt danh hiệu Xuất sắc và Tiêu biểu chiếm bao nhiêu phần trăm tổng số học sinh toàn trường?",
                "solution": "Bài giải:\nTổng số học sinh đạt danh hiệu Xuất sắc và Tiêu biểu là:\n$440 + 260 = 700\\text{ (học sinh)}$\nTỉ số phần trăm của số học sinh đạt Xuất sắc và Tiêu biểu so với toàn trường là:\n$700 : 800 = 0,875 = 87,5\\%$\nĐáp số: $87,5\\%$.",
                "answer": "87,5%"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một căn phòng hình hộp chữ nhật có chiều dài $7,5\\text{ m}$, chiều rộng $5\\text{ m}$ và chiều cao $3,2\\text{ m}$. Người ta muốn sơn trần nhà và 4 bức tường phía trong phòng. Tổng diện tích các cửa sổ và cửa đi là $9,5\\text{ m}^2$.\na) Tính diện tích cần sơn của căn phòng.\nb) Biết tiền công sơn mỗi mét vuông là $25\\,000$ đồng. Tính tổng số tiền công phải trả để sơn căn phòng đó.",
                "solution": "Bài giải:\na) Diện tích xung quanh căn phòng là:\n$(7,5 + 5) \\times 2 \\times 3,2 = 80\\text{ (m}^2)$\nDiện tích trần nhà là:\n$7,5 \\times 5 = 37,5\\text{ (m}^2)$\nDiện tích cần sơn của căn phòng là:\n$80 + 37,5 - 9,5 = 108\\text{ (m}^2)$\nb) Số tiền công phải trả để sơn căn phòng là:\n$108 \\times 25\\,000 = 2\\,700\\,000\\text{ (đồng)}$\nĐáp số:\na) $108\\text{ m}^2$;\nb) $2\\,700\\,000\\text{ đồng}$.",
                "answer": "a) 108 m²; b) 2 700 000 đồng"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một bể cá cảnh hình hộp chữ nhật có các kích thước trong lòng bể: chiều dài $1\\text{ m}$, chiều rộng $0,6\\text{ m}$, chiều cao $0,5\\text{ m}$. Bể đang chứa nước ở mức cao $0,35\\text{ m}$.\na) Tính số lít nước đang có trong bể.\nb) Người ta thả vào bể một hòn đá non bộ thì thấy mực nước trong bể dâng lên chạm đến miệng bể (chưa tràn ra ngoài). Tính thể tích của hòn đá non bộ theo đơn vị đề-xi-mét khối.",
                "solution": "Bài giải:\nĐổi: $1\\text{ m} = 10\\text{ dm}$; $0,6\\text{ m} = 6\\text{ dm}$; $0,5\\text{ m} = 5\\text{ dm}$; $0,35\\text{ m} = 3,5\\text{ dm}$.\na) Lượng nước đang có trong bể là:\n$10 \\times 6 \\times 3,5 = 210\\text{ (dm}^3) = 210\\text{ (lít)}$\nb) Mực nước trong bể dâng thêm là:\n$5 - 3,5 = 1,5\\text{ (dm)}$\nThể tích của hòn đá non bộ bằng thể tích nước dâng thêm:\n$10 \\times 6 \\times 1,5 = 90\\text{ (dm}^3)$\nĐáp số:\na) $210\\text{ lít}$;\nb) $90\\text{ dm}^3$.",
                "answer": "a) 210 lít; b) 90 dm³"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Bác Tư mua một chiếc ti vi với giá niêm yết $8\\,500\\,000$ đồng. Cửa hàng đang có chương trình khuyến mại giảm giá $12\\%$. Ngoài ra, vì bác Tư thanh toán bằng hình thức chuyển khoản nên được giảm tiếp thêm $2\\%$ trên số tiền đã giảm. Hỏi bác Tư phải thanh toán tất cả bao nhiêu tiền?",
                "solution": "Bài giải:\nGiá chiếc ti vi sau khi được giảm $12\\%$ là:\n$8\\,500\\,000 \\times (100\\% - 12\\%) : 100 = 8\\,500\\,000 \\times 0,88 = 7\\,480\\,000\\text{ (đồng)}$\nSố tiền bác Tư được giảm thêm $2\\%$ khi chuyển khoản là:\n$7\\,480\\,000 \\times 2 : 100 = 149\\,600\\text{ (đồng)}$\nSố tiền thực tế bác Tư phải thanh toán là:\n$7\\,480\\,000 - 149\\,600 = 7\\,330\\,400\\text{ (đồng)}$\nĐáp số: $7\\,330\\,400\\text{ đồng}$.",
                "answer": "7 330 400 đồng"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 07 (th5_gk2_de07)
    # =========================================================================
    exams["th5_gk2_de07"] = {
        "id": "th5_gk2_de07",
        "code": "GK2-DE07",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 07)",
        "grade": "5",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Phân số nào dưới đây biểu diễn tỉ số phần trăm $0,8\\%$?",
                "options": ["$\\frac{8}{10}$", "$\\frac{8}{100}$", "$\\frac{8}{1000}$", "$\\frac{8}{10000}$"],
                "correct": 2,
                "explanation": "$0,8\\% = 0,8 : 100 = \\frac{8}{1000}$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Thể tích của một hình lập phương có cạnh dài $10\\text{ cm}$ là:",
                "options": ["$100\\text{ cm}^3$", "$1\\text{ dm}^3$", "$10\\text{ dm}^3$", "$1\\text{ m}^3$"],
                "correct": 1,
                "explanation": "Thể tích là: $10 \\times 10 \\times 10 = 1000\\text{ cm}^3 = 1\\text{ dm}^3$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 3:** Một lớp có 32 học sinh, trong đó có 24 học sinh hoàn thành xuất sắc môn Toán. Tỉ số phần trăm học sinh hoàn thành xuất sắc môn Toán là:",
                "options": ["75%", "70%", "80%", "65%"],
                "correct": 0,
                "explanation": "Ta có: $24 : 32 = 0,75 = 75\\%$."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Diện tích toàn phần của hình hộp chữ nhật bằng:",
                "options": [
                    "Diện tích xung quanh cộng với diện tích một mặt đáy",
                    "Chu vi đáy nhân với chiều cao",
                    "Diện tích xung quanh cộng với diện tích hai mặt đáy",
                    "Chiều dài nhân với chiều rộng nhân chiều cao"
                ],
                "correct": 2,
                "explanation": "Quy tắc: $S_{tp} = S_{xq} + 2 \\times S_{đáy}$."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** $0,75\\text{ m}^3$ bằng bao nhiêu lít nước? (Biết $1\\text{ dm}^3 = 1\\text{ lít}$):",
                "options": ["7,5 lít", "75 lít", "7500 lít", "750 lít"],
                "correct": 3,
                "explanation": "Vì $1\\text{ m}^3 = 1000\\text{ dm}^3 = 1000\\text{ lít}$ nên $0,75\\text{ m}^3 = 750\\text{ lít}$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Một hình hộp chữ nhật có chiều dài $6\\text{ cm}$, chiều rộng $4\\text{ cm}$ và thể tích là $72\\text{ cm}^3$. Chiều cao của hình hộp đó là:",
                "options": ["$2\\text{ cm}$", "$3\\text{ cm}$", "$4\\text{ cm}$", "$5\\text{ cm}$"],
                "correct": 1,
                "explanation": "Chiều cao của hình hộp là: $72 : (6 \\times 4) = 72 : 24 = 3\\text{ cm}$."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $68,4 \\times 2,05$\nb) $175,5 : 4,5$",
                "solution": "a) $68,4 \\times 2,05 = 140,22$\nb) $175,5 : 4,5 = 39$",
                "answer": "a) 140,22; b) 39"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tính bằng cách thuận tiện nhất:\n$4,8 \\times 3,7 + 4,8 \\times 5,3 + 4,8$",
                "solution": "Ta có:\n$4,8 \\times 3,7 + 4,8 \\times 5,3 + 4,8 = 4,8 \\times (3,7 + 5,3 + 1)$\n$= 4,8 \\times 10 = 48$.\nĐáp số: 48.",
                "answer": "48"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một xưởng may theo kế hoạch phải may 1500 bộ quần áo bảo hộ. Đến giữa tháng, xưởng đã may được 1050 bộ quần áo.\na) Xưởng may đã thực hiện được bao nhiêu phần trăm kế hoạch?\nb) Xưởng may còn phải may thêm bao nhiêu phần trăm kế hoạch nữa để hoàn thành mục tiêu?",
                "solution": "Bài giải:\na) Xưởng may đã thực hiện được số phần trăm kế hoạch là:\n$1050 : 1500 = 0,7 = 70\\%$\nb) Xưởng còn phải may thêm số phần trăm kế hoạch là:\n$100\\% - 70\\% = 30\\%$\nĐáp số:\na) $70\\%$;\nb) $30\\%$.",
                "answer": "a) 70%; b) 30%"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một chiếc thùng tôn không nắp dạng hình lập phương có cạnh dài $1,2\\text{ m}$. Người ta sơn cả mặt trong và mặt ngoài của chiếc thùng đó.\na) Tính diện tích tôn dùng để làm thùng (không kể mép hàn).\nb) Tính tổng diện tích bề mặt cần quét sơn (cả mặt trong và mặt ngoài).",
                "solution": "Bài giải:\na) Vì thùng tôn không có nắp nên thùng có 5 mặt hình vuông.\nDiện tích tôn dùng để làm thùng là:\n$1,2 \\times 1,2 \\times 5 = 7,2\\text{ (m}^2)$\nb) Tổng diện tích bề mặt cần quét sơn cả trong lẫn ngoài là:\n$7,2 \\times 2 = 14,4\\text{ (m}^2)$\nĐáp số:\na) $7,2\\text{ m}^2$;\nb) $14,4\\text{ m}^2$.",
                "answer": "a) 7,2 m²; b) 14,4 m²"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một bể bơi dạng hình hộp chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $12\\text{ m}$ và chiều sâu trong lòng bể là $1,8\\text{ m}$.\na) Tính thể tích nước khi bể bơi chứa đầy nước.\nb) Người ta bơm nước vào bể sao cho mực nước cách mép trên của bể $30\\text{ cm}$. Hỏi lượng nước đã bơm vào bể là bao nhiêu mét khối?",
                "solution": "Bài giải:\na) Thể tích của bể bơi là:\n$25 \\times 12 \\times 1,8 = 540\\text{ (m}^3)$\nb) Đổi: $30\\text{ cm} = 0,3\\text{ m}$.\nChiều cao của mực nước trong bể bơi là:\n$1,8 - 0,3 = 1,5\\text{ (m)}$\nLượng nước đã bơm vào bể là:\n$25 \\times 12 \\times 1,5 = 450\\text{ (m}^3)$\nĐáp số:\na) $540\\text{ m}^3$;\nb) $450\\text{ m}^3$.",
                "answer": "a) 540 m³; b) 450 m³"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Giá một lít xăng vào tháng 1 là $24\\,000$ đồng. Đến tháng 2 giá xăng tăng $10\\%$. Đến tháng 3 giá xăng lại giảm $10\\%$ so với tháng 2. Hỏi giá một lít xăng vào tháng 3 là bao nhiêu đồng? Giá xăng tháng 3 so với tháng 1 tăng hay giảm bao nhiêu đồng?",
                "solution": "Bài giải:\nGiá một lít xăng vào tháng 2 là:\n$24\\,000 + 24\\,000 \\times 10 : 100 = 26\\,400\\text{ (đồng)}$\nGiá một lít xăng vào tháng 3 là:\n$26\\,400 - 26\\,400 \\times 10 : 100 = 23\\,760\\text{ (đồng)}$\nSo với tháng 1, giá xăng tháng 3 đã giảm số tiền là:\n$24\\,000 - 23\\,760 = 240\\text{ (đồng)}$\nĐáp số: Giá xăng tháng 3 là $23\\,760\\text{ đồng}$, giảm 240 đồng so với tháng 1.",
                "answer": "23 760 đồng (giảm 240 đồng)"
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08 (th5_gk2_de08)
    # =========================================================================
    exams["th5_gk2_de08"] = {
        "id": "th5_gk2_de08",
        "code": "GK2-DE08",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 5 (ĐỀ SỐ 08)",
        "grade": "5",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            {
                "id": 1,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 1:** Tìm $12\\%$ của 350:",
                "options": ["42", "35", "40", "45"],
                "correct": 0,
                "explanation": "$350 \\times 12 : 100 = 42$."
            },
            {
                "id": 2,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 2:** Số thích hợp để điền vào chỗ chấm $8\\text{ m}^3\\ 6\\text{ dm}^3 = \\dots\\text{ m}^3$ là:",
                "options": ["8,6", "8,06", "8,006", "8,0006"],
                "correct": 2,
                "explanation": "Vì $1\\text{ dm}^3 = \\frac{1}{1000}\\text{ m}^3$ nên $6\\text{ dm}^3 = 0,006\\text{ m}^3$. Do đó $8\\text{ m}^3\\ 6\\text{ dm}^3 = 8,006\\text{ m}^3$."
            },
            {
                "id": 3,
                "points": 0.5,
                "level": "Nhận biết",
                "question": "**Câu 3:** Một hình lập phương có diện tích toàn phần là $54\\text{ dm}^2$. Diện tích xung quanh của nó là:",
                "options": ["$18\\text{ dm}^2$", "$36\\text{ dm}^2$", "$27\\text{ dm}^2$", "$45\\text{ dm}^2$"],
                "correct": 1,
                "explanation": "Diện tích một mặt là: $54 : 6 = 9\\text{ dm}^2$. Diện tích xung quanh là: $9 \\times 4 = 36\\text{ dm}^2$."
            },
            {
                "id": 4,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 4:** Một kho gạo chứa 120 tấn gạo. Người ta đã xuất đi $35\\%$ số gạo đó. Số gạo còn lại trong kho là:",
                "options": ["42 tấn", "65 tấn", "72 tấn", "78 tấn"],
                "correct": 3,
                "explanation": "Số gạo đã xuất là: $120 \\times 35 : 100 = 42$ tấn. Số gạo còn lại là: $120 - 42 = 78$ tấn."
            },
            {
                "id": 5,
                "points": 0.5,
                "level": "Thông hiểu",
                "question": "**Câu 5:** Một hình hộp chữ nhật có chiều dài $15\\text{ cm}$, chiều rộng $8\\text{ cm}$ và chiều cao $6\\text{ cm}$. Diện tích toàn phần của nó là:",
                "options": ["$516\\text{ cm}^2$", "$276\\text{ cm}^2$", "$240\\text{ cm}^2$", "$720\\text{ cm}^2$"],
                "correct": 0,
                "explanation": "$S_{xq} = (15 + 8) \\times 2 \\times 6 = 276\\text{ cm}^2$. $S_{2đáy} = 2 \\times (15 \\times 8) = 240\\text{ cm}^2$. $S_{tp} = 276 + 240 = 516\\text{ cm}^2$."
            },
            {
                "id": 6,
                "points": 0.5,
                "level": "Vận dụng",
                "question": "**Câu 6:** Người ta xếp các khối lập phương nhỏ cạnh $2\\text{ cm}$ vào một chiếc hộp hình chữ nhật có kích thước $10\\text{ cm} \\times 8\\text{ cm} \\times 6\\text{ cm}$. Số khối lập phương nhỏ xếp vừa khít trong hộp là:",
                "options": ["40 khối", "50 khối", "60 khối", "80 khối"],
                "correct": 2,
                "explanation": "Số khối xếp theo chiều dài là: $10 : 2 = 5$. Chiều rộng: $8 : 2 = 4$. Chiều cao: $6 : 2 = 3$. Tổng số khối là: $5 \\times 4 \\times 3 = 60$ khối."
            }
        ],
        "part2": [
            {
                "id": 1,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 1:** Đặt tính rồi tính:\na) $45,8 \\times 3,6$\nb) $285,6 : 6,8$",
                "solution": "a) $45,8 \\times 3,6 = 164,88$\nb) $285,6 : 6,8 = 42$",
                "answer": "a) 164,88; b) 42"
            },
            {
                "id": 2,
                "points": 1.0,
                "lineCount": 4,
                "level": "Thông hiểu",
                "question": "**Bài 2:** Tìm $x$, biết:\n$(x - 1,2) : 2,5 = 3,4$",
                "solution": "Ta có:\n$x - 1,2 = 3,4 \\times 2,5$\n$x - 1,2 = 8,5$\n$x = 8,5 + 1,2$\n$x = 9,7$.\nĐáp số: $x = 9,7$.",
                "answer": "x = 9,7"
            },
            {
                "id": 3,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng",
                "question": "**Bài 3:** Một khu vườn hình chữ nhật có chu vi $160\\text{ m}$, chiều rộng bằng $\\frac{3}{5}$ chiều dài. Người ta dùng $30\\%$ diện tích khu vườn để trồng cây ăn quả, diện tích còn lại trồng rau. Tính diện tích đất trồng rau của khu vườn đó.",
                "solution": "Bài giải:\nNửa chu vi khu vườn hình chữ nhật là:\n$160 : 2 = 80\\text{ (m)}$\nTổng số phần bằng nhau là:\n$3 + 5 = 8\\text{ (phần)}$\nChiều rộng khu vườn là:\n$80 : 8 \\times 3 = 30\\text{ (m)}$\nChiều dài khu vườn là:\n$80 - 30 = 50\\text{ (m)}$\nDiện tích của khu vườn là:\n$50 \\times 30 = 1500\\text{ (m}^2)$\nTỉ số phần trăm diện tích trồng rau là:\n$100\\% - 30\\% = 70\\%$\nDiện tích đất trồng rau là:\n$1500 \\times 70 : 100 = 1050\\text{ (m}^2)$\nĐáp số: $1050\\text{ m}^2$.",
                "answer": "1050 m²"
            },
            {
                "id": 4,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 4:** Một căn phòng dạng hình hộp chữ nhật có chiều dài $9\\text{ m}$, chiều rộng $6\\text{ m}$ và chiều cao $4\\text{ m}$. Người ta sơn tường và trần nhà phía trong phòng. Tổng diện tích các cửa sổ và cửa ra vào là $16\\text{ m}^2$.\na) Tính diện tích cần quét sơn.\nb) Cứ mỗi mét vuông tường sơn hết $0,25\\text{ kg}$ sơn. Hỏi người ta phải mua ít nhất bao nhiêu thùng sơn loại $5\\text{ kg}$ để sơn xong căn phòng đó?",
                "solution": "Bài giải:\na) Diện tích xung quanh căn phòng là:\n$(9 + 6) \\times 2 \\times 4 = 120\\text{ (m}^2)$\nDiện tích trần nhà là:\n$9 \\times 6 = 54\\text{ (m}^2)$\nDiện tích cần quét sơn là:\n$120 + 54 - 16 = 158\\text{ (m}^2)$\nb) Lượng sơn cần dùng để sơn căn phòng là:\n$158 \\times 0,25 = 39,5\\text{ (kg)}$\nSố thùng sơn loại $5\\text{ kg}$ cần mua ít nhất là:\n$39,5 : 5 = 7,9\\text{ (thùng)}$\nVì số thùng sơn phải là số tự nhiên nên người ta phải mua ít nhất 8 thùng sơn.\nĐáp số:\na) $158\\text{ m}^2$;\nb) 8 thùng sơn.",
                "answer": "a) 158 m²; b) 8 thùng sơn"
            },
            {
                "id": 5,
                "points": 1.5,
                "lineCount": 6,
                "level": "Vận dụng",
                "question": "**Bài 5:** Một bể cá hình lập phương có cạnh bằng $8\\text{ dm}$. Hiện tại mực nước trong bể cao $5\\text{ dm}$.\na) Hỏi hiện tại bể đang chứa bao nhiêu lít nước? (Biết $1\\text{ dm}^3 = 1\\text{ lít}$).\nb) Người ta thả một khối đá san hô vào bể thì thấy nước trong bể dâng lên đến chiều cao $6,5\\text{ dm}$. Tính thể tích của khối đá san hô đó.\nc) Sau khi thả khối san hô vào bể, cần đổ thêm bao nhiêu lít nước nữa để đầy bể cá đó?",
                "solution": "Bài giải:\na) Lượng nước hiện tại bể đang chứa là:\n$8 \\times 8 \\times 5 = 320\\text{ (dm}^3) = 320\\text{ (lít)}$\nb) Mực nước trong bể dâng thêm là:\n$6,5 - 5 = 1,5\\text{ (dm)}$\nThể tích của khối đá san hô là:\n$8 \\times 8 \\times 1,5 = 96\\text{ (dm}^3)$\nc) Chiều cao phần còn trống của bể là:\n$8 - 6,5 = 1,5\\text{ (dm)}$\nLượng nước cần đổ thêm để đầy bể là:\n$8 \\times 8 \\times 1,5 = 96\\text{ (dm}^3) = 96\\text{ (lít)}$\nĐáp số:\na) $320\\text{ lít}$;\nb) $96\\text{ dm}^3$;\nc) $96\\text{ lít}$.",
                "answer": "a) 320 lít; b) 96 dm³; c) 96 lít"
            },
            {
                "id": 6,
                "points": 1.0,
                "lineCount": 5,
                "level": "Vận dụng cao",
                "question": "**Bài 6:** Một người bán một chiếc quạt điện được $600\\,000$ đồng, tính ra người đó lãi $20\\%$ so với giá bán. Hỏi người đó lãi bao nhiêu phần trăm so với giá vốn?",
                "solution": "Bài giải:\nSố tiền lãi người đó nhận được khi bán chiếc quạt là:\n$600\\,000 \\times 20 : 100 = 120\\,000\\text{ (đồng)}$\nGiá vốn của chiếc quạt điện là:\n$600\\,000 - 120\\,000 = 480\\,000\\text{ (đồng)}$\nTỉ số phần trăm tiền lãi so với giá vốn là:\n$120\\,000 : 480\\,000 = 0,25 = 25\\%$\nĐáp số: $25\\%$.",
                "answer": "25%"
            }
        ]
    }

    return exams

if __name__ == "__main__":
    exams = get_th5_gk2_exams()
    print(f"Tổng số đề GK2 đã tạo: {len(exams)}")
    for eid, ex in exams.items():
        print(f"[{eid}] {ex['title']} - Part 1: {len(ex['part1'])} câu, Part 2: {len(ex['part2'])} bài")
