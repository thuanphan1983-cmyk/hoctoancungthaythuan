# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG V (PHẦN 2)
Bao gồm:
- Bài 19: Biểu đồ đoạn thẳng (3 đề: Cơ bản, Khá, Nâng cao)
- Bài kiểm tra cuối Chương V: Thu thập và biểu diễn dữ liệu (3 đề: Cơ bản, Khá, Nâng cao)
Chuẩn ma trận Bộ GD&ĐT 2025: 12 TN + 2 Đ/S (8 ý) + 4 TLN + 3 TL. Tổng 10.0 điểm.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

EXAMS_PART2 = {}

# =====================================================================
# BÀI 19: BIỂU ĐỒ ĐOẠN THẲNG
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c5_7_bai3_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 19: Biểu đồ đoạn thẳng - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Biểu đồ đoạn thẳng thường được dùng để biểu diễn:", "options": ["Sự thay đổi của một đại lượng theo thời gian", "Cơ cấu tỉ lệ các phần trong toàn bộ", "Sự phân bố không gian", "Mức độ hài lòng của khách hàng"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Trên biểu đồ đoạn thẳng, trục nằm ngang (trục hoành) thường biểu diễn:", "options": ["Thời gian (ngày, tháng, năm, giờ,...)", "Số lượng hoặc giá trị đo được", "Tên các địa danh", "Tỉ lệ phần trăm"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trên biểu đồ đoạn thẳng, trục thẳng đứng (trục tung) biểu diễn:", "options": ["Đại lượng cần theo dõi (nhiệt độ, doanh thu, sản lượng,...)", "Thời gian theo dõi", "Tên đơn vị đo", "Tiêu đề biểu đồ"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Khi đoạn thẳng đi lên từ trái sang phải, đại lượng có xu hướng:", "options": ["Tăng lên", "Giảm đi", "Không đổi", "Bằng không"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Khi đoạn thẳng nằm ngang song song với trục thời gian, đại lượng có xu hướng:", "options": ["Không thay đổi (giữ nguyên)", "Tăng nhanh", "Giảm mạnh", "Biến động mạnh"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Một biểu đồ đoạn thẳng biểu diễn nhiệt độ trong tuần: Thứ Hai: $25^\\circ$C, Thứ Ba: $27^\\circ$C, Thứ Tư: $26^\\circ$C. Nhiệt độ ngày Thứ Ba tăng bao nhiêu độ C so với ngày Thứ Hai?", "options": ["$2^\\circ$C", "$1^\\circ$C", "$3^\\circ$C", "$0^\\circ$C"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Biểu đồ đoạn thẳng biểu diễn số học sinh giỏi của một trường qua 4 năm: Năm 1: 120 em, Năm 2: 135 em, Năm 3: 150 em, Năm 4: 165 em. Xu thế chung của số học sinh giỏi là:", "options": ["Tăng đều qua các năm", "Giảm dần qua các năm", "Dao động thất thường", "Không đổi"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Quan sát biểu đồ chiều cao của bạn Nam từ 11 đến 14 tuổi: 11 tuổi: 140 cm, 12 tuổi: 146 cm, 13 tuổi: 153 cm, 14 tuổi: 161 cm. Trong độ tuổi nào bạn Nam tăng chiều cao nhiều nhất?", "options": ["Từ 13 đến 14 tuổi (tăng 8 cm)", "Từ 11 đến 12 tuổi", "Từ 12 đến 13 tuổi", "Tăng đều nhau"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Nếu một biểu đồ đoạn thẳng biểu diễn doanh số bán hàng từ tháng 1 đến tháng 6 có đoạn nối giữa tháng 3 và tháng 4 dốc xuống, điều đó chứng tỏ:", "options": ["Doanh số tháng 4 giảm so với tháng 3", "Doanh số tháng 4 tăng so với tháng 3", "Doanh số tháng 4 bằng tháng 3", "Doanh số tháng 4 bằng 0"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Số lượng xe đạp bán ra trong 3 tháng đầu năm: Tháng 1: 50 chiếc, Tháng 2: 40 chiếc, Tháng 3: 60 chiếc. Chênh lệch số xe bán được giữa tháng cao nhất và thấp nhất là:", "options": ["$20$ chiếc", "$10$ chiếc", "$30$ chiếc", "$15$ chiếc"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Biểu đồ đoạn thẳng biểu diễn điểm kiểm tra của An qua 4 lần: $7, 8, 8, 9$. Điểm trung bình của An qua 4 lần kiểm tra là:", "options": ["$8{,}0$", "$8{,}25$", "$7{,}75$", "$8{,}5$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Nhiệt độ đo được lúc 6h, 12h, 18h trong ngày lần lượt là $20^\\circ$C, $32^\\circ$C, $26^\\circ$C. Độ chênh lệch nhiệt độ lớn nhất trong ngày là:", "options": ["$12^\\circ$C", "$6^\\circ$C", "$8^\\circ$C", "$10^\\circ$C"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Biểu đồ đoạn thẳng theo dõi số lượng sách mượn tại thư viện trong 5 ngày của một tuần:\n- Thứ Hai: 45 cuốn\n- Thứ Ba: 60 cuốn\n- Thứ Tư: 50 cuốn\n- Thứ Năm: 70 cuốn\n- Thứ Sáu: 55 cuốn.\nXét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Ngày có số sách mượn nhiều nhất là Thứ Năm (70 cuốn).", "isCorrect": True, "explanation": "Giá trị 70 là cao nhất trong tuần."},
                {"id": "b", "statement": "Ngày có số sách mượn ít nhất là Thứ Hai (45 cuốn).", "isCorrect": True, "explanation": "Giá trị 45 là thấp nhất trong tuần."},
                {"id": "c", "statement": "Từ Thứ Ba đến Thứ Tư, số lượng sách mượn có xu hướng tăng.", "isCorrect": False, "explanation": "Thứ Ba (60) đến Thứ Tư (50) là giảm 10 cuốn, đoạn thẳng dốc xuống."},
                {"id": "d", "statement": "Tổng số sách mượn trong cả tuần là $280$ cuốn.", "isCorrect": True, "explanation": "$45 + 60 + 50 + 70 + 55 = 280$ cuốn."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho các nhận định về cách vẽ biểu đồ đoạn thẳng, xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Khoảng cách giữa các mốc thời gian trên trục ngang cần được chia đều nhau tương ứng với khoảng thời gian bằng nhau.", "isCorrect": True, "explanation": "Đảm bảo tính chính xác và trực quan của tỉ lệ thời gian."},
                {"id": "b", "statement": "Trục thẳng đứng bắt buộc phải bắt đầu từ số 0 hoặc có dấu ngắt trục rõ ràng.", "isCorrect": True, "explanation": "Tránh gây hiểu lầm về độ lớn tương đối."},
                {"id": "c", "statement": "Mỗi điểm trên biểu đồ được xác định bởi một cặp giá trị (thời gian, số liệu tương ứng).", "isCorrect": True, "explanation": "Đúng theo nguyên tắc biểu diễn đồ thị tọa độ."},
                {"id": "d", "statement": "Sau khi xác định các điểm, ta dùng các đường cong tròn để nối chúng lại.", "isCorrect": False, "explanation": "Biểu đồ đoạn thẳng dùng các đoạn thẳng gấp khúc nối liên tiếp các điểm kề nhau."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Số lượng học sinh giỏi của lớp 7A trong 4 kì học liên tiếp là: 12, 15, 14, 19. Số học sinh giỏi tăng bao nhiêu em từ kì 1 đến kì 4?", "answer": 7, "unit": "học sinh"},
        {"id": 2, "level": "Thông hiểu", "question": "Nhiệt độ đo được lúc 6h sáng là $22^\\circ$C, đến 14h chiều tăng thêm $8^\\circ$C. Hỏi nhiệt độ lúc 14h chiều là bao nhiêu độ C?", "answer": 30, "unit": "độ C"},
        {"id": 3, "level": "Vận dụng", "question": "Doanh thu bán hàng của một cửa hàng trong 3 ngày: Ngày 1: 5 triệu, Ngày 2: 7 triệu, Ngày 3: 9 triệu. Doanh thu trung bình mỗi ngày là bao nhiêu triệu đồng?", "answer": 7, "unit": "triệu đồng"},
        {"id": 4, "level": "Vận dụng", "question": "Một người chạy bộ ghi lại quãng đường chạy (km) trong 4 tuần: Tuần 1: 15 km, Tuần 2: 18 km, Tuần 3: 20 km, Tuần 4: 27 km. Tổng quãng đường người đó đã chạy trong 4 tuần là bao nhiêu km?", "answer": 80, "unit": "km"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Bảng sau đây ghi lại số lượng xe đạp điện bán được của một cửa hàng trong 6 tháng đầu năm:\n| Tháng | 1 | 2 | 3 | 4 | 5 | 6 |\n| Số xe | 20 | 25 | 18 | 30 | 35 | 40 |\na) Hãy cho biết tháng nào cửa hàng bán được nhiều xe nhất? Tháng nào bán được ít xe nhất?\nb) Số lượng xe bán ra có xu hướng thay đổi như thế nào trong khoảng từ tháng 3 đến tháng 6?",
            "maxScore": 1.0,
            "solution": "a) - Tháng cửa hàng bán được nhiều xe nhất là Tháng 6 (với 40 chiếc xe).\n- Tháng bán được ít xe nhất là Tháng 3 (với 18 chiếc xe).\nb) Từ tháng 3 đến tháng 6, số lượng xe bán ra tăng liên tục:\n- Tháng 3: 18 xe\n- Tháng 4: 30 xe (tăng 12 xe)\n- Tháng 5: 35 xe (tăng 5 xe)\n- Tháng 6: 40 xe (tăng 5 xe)\nĐoạn thẳng biểu diễn trên biểu đồ liên tục đi lên từ trái sang phải, thể hiện xu hướng tăng trưởng ổn định và mạnh mẽ.",
            "rubric": [
                {"step": "Chỉ ra đúng tháng cao nhất (tháng 6) và thấp nhất (tháng 3)", "subScore": 0.5},
                {"step": "Nhận xét đúng xu hướng tăng trưởng liên tục từ tháng 3 đến tháng 6", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Nhiệt độ không khí trung bình các tháng mùa đông (tháng 11, 12, 1, 2) tại Hà Nội được ghi lại: Tháng 11: $22^\\circ$C, Tháng 12: $18^\\circ$C, Tháng 1: $16^\\circ$C, Tháng 2: $17^\\circ$C.\na) Tính nhiệt độ trung bình của cả mùa đông (4 tháng trên).\nb) Tháng nào có nhiệt độ thấp nhất? Độ chênh lệch nhiệt độ giữa tháng 11 và tháng 1 là bao nhiêu?",
            "maxScore": 1.0,
            "solution": "a) Nhiệt độ trung bình cả mùa đông là:\n$\\bar{T} = \\frac{22 + 18 + 16 + 17}{4} = \\frac{73}{4} = 18{,}25^\\circ$C.\nb) - Tháng có nhiệt độ thấp nhất là Tháng 1 ($16^\\circ$C).\n- Chênh lệch nhiệt độ giữa tháng 11 và tháng 1 là: $22^\\circ\\text{C} - 16^\\circ\\text{C} = 6^\\circ$C.",
            "rubric": [
                {"step": "Tính đúng nhiệt độ trung bình mùa đông là 18,25 độ C", "subScore": 0.5},
                {"step": "Chỉ ra đúng tháng 1 lạnh nhất và độ chênh lệch là 6 độ C", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Số lượng người dùng một ứng dụng học tập trực tuyến trong 4 quý năm 2024 như sau: Quý I: 1000 người, Quý II: 1200 người, Quý III: 1500 người, Quý IV: 1800 người.\na) Tính tốc độ tăng trưởng người dùng (tỉ lệ phần trăm tăng) từ Quý I đến Quý II.\nb) Tính tốc độ tăng trưởng người dùng từ Quý I đến Quý IV của cả năm.",
            "maxScore": 1.0,
            "solution": "a) Số người dùng tăng từ Quý I đến Quý II là:\n$1200 - 1000 = 200$ (người).\nTốc độ tăng trưởng từ Quý I đến Quý II là:\n$\\frac{200}{1000} \\times 100\\% = 20\\%$.\nb) Số người dùng tăng từ Quý I đến Quý IV là:\n$1800 - 1000 = 800$ (người).\nTốc độ tăng trưởng người dùng cả năm là:\n$\\frac{800}{1000} \\times 100\\% = 80\\%$.",
            "rubric": [
                {"step": "Tính đúng mức tăng trưởng Quý I -> Quý II là 20%", "subScore": 0.5},
                {"step": "Tính đúng mức tăng trưởng cả năm Quý I -> Quý IV là 80%", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c5_7_bai3_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 19: Biểu đồ đoạn thẳng - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Biểu đồ đoạn thẳng kép thường được dùng để:", "options": ["So sánh xu hướng phát triển của hai đối tượng theo cùng một mốc thời gian", "Biểu diễn cơ cấu các phần trăm", "Tính diện tích hình tròn", "Thay thế hoàn toàn bảng tần số"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Biểu đồ doanh thu của một cửa hàng 4 quý: Quý I: 80 triệu, Quý II: 100 triệu, Quý III: 90 triệu, Quý IV: 130 triệu. Quý nào có doanh thu tăng mạnh nhất so với quý trước đó?", "options": ["Quý IV (tăng 40 triệu)", "Quý II (tăng 20 triệu)", "Quý III", "Quý I"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Sản lượng lúa của một tỉnh trong 3 năm liên tiếp: Năm 2021: 1,2 triệu tấn; Năm 2022: 1,35 triệu tấn; Năm 2023: 1,5 triệu tấn. Sản lượng năm 2023 tăng bao nhiêu phần trăm so với năm 2021?", "options": ["$25\\%$", "$20\\%$", "$15\\%$", "$30\\%$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Nhiệt độ tại Sa Pa đo được lúc 0h là $6^\\circ$C, lúc 6h là $4^\\circ$C, lúc 12h là $14^\\circ$C, lúc 18h là $10^\\circ$C. Khoảng thời gian nào nhiệt độ tăng nhanh nhất?", "options": ["Từ 6h đến 12h (tăng $10^\\circ$C trong 6 giờ)", "Từ 0h đến 6h", "Từ 12h đến 18h", "Không có khoảng nào"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Một người gửi tiết kiệm với số dư tài khoản qua 3 năm: Năm 1: 50 triệu; Năm 2: 55 triệu; Năm 3: 60,5 triệu. Lãi suất mỗi năm người đó nhận được là:", "options": ["$10\\%$/năm", "$8\\%$/năm", "$5\\%$/năm", "$12\\%$/năm"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Khối lượng một con bê sơ sinh sau 4 tháng: Tháng 1: 25 kg, Tháng 2: 32 kg, Tháng 3: 40 kg, Tháng 4: 50 kg. Khối lượng trung bình mỗi tháng con bê tăng được là:", "options": ["$8{,}33$ kg", "$7{,}5$ kg", "$6{,}25$ kg", "$9$ kg"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tỉ lệ thất nghiệp của một thành phố trong 4 năm: 2020: 3,5%, 2021: 4,2%, 2022: 3,8%, 2023: 3,0%. Năm nào có tỉ lệ thất nghiệp cao nhất?", "options": ["Năm 2021", "Năm 2020", "Năm 2022", "Năm 2023"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Số lượng người truy cập một trang web từ thứ Hai đến thứ Bảy: 200, 250, 300, 280, 350, 420. Trung vị của dãy số liệu trên là:", "options": ["$290$", "$300$", "$280$", "$275$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Một bạn học sinh theo dõi số trang sách đọc mỗi ngày trong 5 ngày: 15, 20, 25, 30, x. Biết trung bình mỗi ngày bạn đọc 24 trang. Giá trị của x là:", "options": ["$30$", "$25$", "$35$", "$20$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Trong biểu đồ đoạn thẳng kép theo dõi xuất khẩu và nhập khẩu của một quốc gia, khi đường xuất khẩu nằm phía trên đường nhập khẩu thì cán cân thương mại:", "options": ["Xuất siêu (thặng dư thương mại)", "Nhập siêu (thâm hụt thương mại)", "Cân bằng thương mại", "Bị lỗ"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một người chạy bộ ghi lại thời gian hoàn thành cự ly 5 km qua 5 tuần: 30 phút, 28 phút, 27 phút, 25 phút, 24 phút. Nhận xét nào sau đây đúng về thành tích chạy của người đó?", "options": ["Thành tích ngày càng tiến bộ vì thời gian chạy ngày càng rút ngắn", "Thành tích ngày càng kém đi vì số phút giảm", "Không thể nhận xét được", "Thành tích không đổi"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Độ dốc của đoạn thẳng nối hai điểm $(t_1, y_1)$ và $(t_2, y_2)$ trên biểu đồ đoạn thẳng thể hiện:", "options": ["Tốc độ thay đổi trung bình của đại lượng trong khoảng thời gian đó", "Giá trị tuyệt đối của đại lượng", "Sai số của phép đo", "Thời gian bắt đầu thí nghiệm"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Biểu đồ đoạn thẳng kép biểu diễn số học sinh nam và nữ đạt điểm Giỏi môn Toán của lớp 7A trong 4 bài kiểm tra định kì:\n- Bài 1: Nam 8, Nữ 10\n- Bài 2: Nam 10, Nữ 12\n- Bài 3: Nam 12, Nữ 11\n- Bài 4: Nam 14, Nữ 15.\nXét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Số học sinh nữ đạt điểm Giỏi ở Bài 1 nhiều hơn số học sinh nam.", "isCorrect": True, "explanation": "Nữ 10 > Nam 8."},
                {"id": "b", "statement": "Ở Bài 3, số học sinh nam đạt điểm Giỏi nhiều hơn số học sinh nữ.", "isCorrect": True, "explanation": "Nam 12 > Nữ 11."},
                {"id": "c", "statement": "Số học sinh nam đạt điểm Giỏi tăng liên tục qua cả 4 bài kiểm tra.", "isCorrect": True, "explanation": "Dãy số nam: 8 -> 10 -> 12 -> 14 tăng đều liên tục."},
                {"id": "d", "statement": "Tổng số lượt học sinh nữ đạt điểm Giỏi qua 4 bài là 45 lượt.", "isCorrect": False, "explanation": "Tổng lượt nữ $= 10 + 12 + 11 + 15 = 48$ lượt, không phải 45."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Bảng số liệu ghi lại dân số của một thị trấn qua 4 cuộc tổng điều tra:\n- Năm 1990: 10 000 người\n- Năm 2000: 12 000 người\n- Năm 2010: 15 000 người\n- Năm 2020: 18 000 người.\nXét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Từ năm 1990 đến năm 2020, dân số thị trấn luôn có xu hướng tăng.", "isCorrect": True, "explanation": "Các giá trị tăng liên tục từ 10 000 lên 18 000."},
                {"id": "b", "statement": "Trong giai đoạn 1990 - 2000, dân số tăng $20\\%$.", "isCorrect": True, "explanation": "$(12 000 - 10 000) / 10 000 = 20\\%$."},
                {"id": "c", "statement": "Trong giai đoạn 2000 - 2010, dân số tăng $25\\%$.", "isCorrect": True, "explanation": "$(15 000 - 12 000) / 12 000 = 3 000 / 12 000 = 25\\%$."},
                {"id": "d", "statement": "Giai đoạn có tốc độ tăng trưởng phần trăm cao nhất là 2010 - 2020.", "isCorrect": False, "explanation": "Giai đoạn 2010 - 2020 tăng $(18000 - 15000) / 15000 = 20\\%$, thấp hơn mức 25% của giai đoạn 2000 - 2010."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Số lượng xe máy bán ra của cửa hàng trong 3 tháng quý I: Tháng 1: 45 xe, Tháng 2: 52 xe, Tháng 3: 65 xe. Tìm số xe bán ra trung bình mỗi tháng trong quý I.", "answer": 54, "unit": "xe"},
        {"id": 2, "level": "Vận dụng", "question": "Nhiệt độ lúc 8h sáng là $24^\\circ$C, lúc 12h trưa là $32^\\circ$C. Tính tốc độ tăng nhiệt độ trung bình mỗi giờ trong khoảng thời gian đó theo độ C/giờ.", "answer": 2, "unit": "độ C/giờ"},
        {"id": 3, "level": "Vận dụng", "question": "Doanh số của một công ty năm 2022 là 50 tỷ đồng, năm 2023 đạt 65 tỷ đồng. Hỏi doanh số năm 2023 tăng bao nhiêu phần trăm so với năm 2022?", "answer": 30, "unit": "%"},
        {"id": 4, "level": "Vận dụng cao", "question": "Chiều cao của một cái cây qua các năm đo được: Năm 1: 1,2 m; Năm 2: 1,8 m; Năm 3: 2,5 m; Năm 4: 3,3 m. Trong năm nào chiều cao của cây tăng nhiều nhất (điền 1, 2, 3 hoặc 4 ứng với năm thứ n)?", "answer": 4, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Biểu đồ đoạn thẳng kép ghi lại nhiệt độ cao nhất ($T_1$) và nhiệt độ thấp nhất ($T_2$) trong 5 ngày của một tuần tại Đà Lạt:\n| Ngày | T2 | T3 | T4 | T5 | T6 |\n| $T_1$ ($^\\circ$C) | 22 | 24 | 21 | 25 | 23 |\n| $T_2$ ($^\\circ$C) | 14 | 15 | 13 | 16 | 15 |\na) Ngày nào có biên độ nhiệt (chênh lệch giữa nhiệt độ cao nhất và thấp nhất) lớn nhất? Biên độ đó là bao nhiêu độ C?\nb) Tính nhiệt độ cao nhất trung bình trong 5 ngày trên.",
            "maxScore": 1.0,
            "solution": "a) Biên độ nhiệt của từng ngày:\n- T2: $22 - 14 = 8^\\circ$C.\n- T3: $24 - 15 = 9^\\circ$C.\n- T4: $21 - 13 = 8^\\circ$C.\n- T5: $25 - 16 = 9^\\circ$C.\n- T6: $23 - 15 = 8^\\circ$C.\nBiên độ nhiệt lớn nhất là $9^\\circ$C (xảy ra vào các ngày Thứ Ba và Thứ Năm).\nb) Nhiệt độ cao nhất trung bình trong 5 ngày là:\n$\\bar{T}_1 = \\frac{22 + 24 + 21 + 25 + 23}{5} = \\frac{115}{5} = 23^\\circ$C.",
            "rubric": [
                {"step": "Tính đúng biên độ các ngày và chỉ ra lớn nhất là 9 độ C (T3, T5)", "subScore": 0.5},
                {"step": "Tính đúng nhiệt độ cao nhất trung bình là 23 độ C", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Bảng sau ghi số lượng học sinh tham gia phong trào \"Kế hoạch nhỏ\" thu gom giấy vụn của 4 lớp khối 7:\n| Lớp | 7A | 7B | 7C | 7D |\n| Số kg gom được | 120 | 150 | 135 | 195 |\na) Lớp nào thu gom được nhiều giấy vụn nhất? Chiếm bao nhiêu phần trăm tổng số giấy gom được của cả khối?\nb) Trung bình mỗi lớp thu gom được bao nhiêu kg giấy vụn?",
            "maxScore": 1.0,
            "solution": "a) Tổng số giấy vụn gom được của cả khối là:\n$120 + 150 + 135 + 195 = 600$ (kg).\nLớp thu gom được nhiều nhất là lớp 7D với $195$ kg.\nTỉ lệ phần trăm lớp 7D đóng góp là:\n$\\frac{195}{600} \\times 100\\% = 32{,}5\\%$.\nb) Trung bình mỗi lớp thu gom được số kg giấy vụn là:\n$\\frac{600}{4} = 150$ (kg).",
            "rubric": [
                {"step": "Tính tổng 600 kg, xác định 7D nhiều nhất và tỉ lệ 32,5%", "subScore": 0.5},
                {"step": "Tính đúng trung bình mỗi lớp 150 kg", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một xí nghiệp có kế hoạch sản xuất trong 4 quý năm 2024. Bảng số liệu so sánh sản lượng kế hoạch và sản lượng thực tế:\n| Quý | I | II | III | IV |\n| Kế hoạch (sản phẩm) | 1000 | 1200 | 1200 | 1500 |\n| Thực tế (sản phẩm) | 1050 | 1140 | 1320 | 1650 |\na) Tính tỉ lệ phần trăm hoàn thành kế hoạch của từng quý (làm tròn đến hàng phần mười).\nb) Cả năm xí nghiệp có hoàn thành vượt mức kế hoạch không? Vượt mức bao nhiêu phần trăm?",
            "maxScore": 1.0,
            "solution": "a) Tỉ lệ hoàn thành kế hoạch từng quý:\n- Quý I: $\\frac{1050}{1000} \\times 100\\% = 105\\%$ (vượt 5%).\n- Quý II: $\\frac{1140}{1200} \\times 100\\% = 95\\%$ (chưa đạt, thiếu 5%).\n- Quý III: $\\frac{1320}{1200} \\times 100\\% = 110\\%$ (vượt 10%).\n- Quý IV: $\\frac{1650}{1500} \\times 100\\% = 110\\%$ (vượt 10%).\nb) Tổng kế hoạch cả năm: $1000 + 1200 + 1200 + 1500 = 4900$ (sản phẩm).\nTổng thực tế cả năm: $1050 + 1140 + 1320 + 1650 = 5160$ (sản phẩm).\nTỉ lệ hoàn thành cả năm là:\n$\\frac{5160}{4900} \\times 100\\% \\approx 105{,}3\\%$.\nVậy cả năm xí nghiệp hoàn thành vượt mức kế hoạch khoảng $5{,}3\\%$.",
            "rubric": [
                {"step": "Tính đúng tỉ lệ hoàn thành từng quý", "subScore": 0.5},
                {"step": "Tính đúng tổng cả năm và kết luận vượt mức xấp xỉ 5,3%", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c5_7_bai3_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 19: Biểu đồ đoạn thẳng - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Khi muốn biểu diễn đồng thời số lượng sản phẩm xuất khẩu và giá trị kim ngạch thu về (hai đơn vị đo khác nhau) theo thời gian trên cùng một biểu đồ, người ta thường dùng:", "options": ["Biểu đồ đoạn thẳng hai trục tung (hai trục tỉ lệ khác nhau)", "Biểu đồ hình quạt tròn đơn", "Biểu đồ cột chồng", "Biểu đồ tranh"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Để làm nổi bật sự chênh lệch nhỏ giữa các giá trị lớn (ví dụ nhiệt độ cơ thể từ $36{,}5$ đến $39^\\circ$C), người ta nên làm gì trên trục tung?", "options": ["Cắt gãy trục tung (bắt đầu từ giá trị gần 36 thay vì từ 0) kèm kí hiệu ngắt trục rõ ràng", "Kéo dài trục hoành gấp đôi", "Đổi đơn vị đo sang độ F", "Bỏ qua các giá trị thập phân"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Một cổ phiếu có giá đóng cửa qua 5 phiên liên tiếp: 50, 52, 48, 54, 60 (nghìn đồng). Mức thay đổi giá lớn nhất giữa hai phiên liền kề là:", "options": ["Tăng $6$ nghìn đồng (từ 54 lên 60)", "Giảm $4$ nghìn đồng", "Tăng $2$ nghìn đồng", "Tăng $10$ nghìn đồng"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Dân số một thành phố qua 3 năm: 2021: 2,0 triệu; 2022: 2,04 triệu; 2023: 2,0808 triệu. Tốc độ gia tăng dân số hằng năm của thành phố là:", "options": ["$2\\%$/năm", "$4\\%$/năm", "$1\\%$/năm", "$2{,}5\\%$/năm"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Quãng đường một vật chuyển động theo thời gian: 1s: 2m, 2s: 8m, 3s: 18m, 4s: 32m. Vận tốc trung bình trong giây thứ 4 (từ giây thứ 3 đến giây thứ 4) là:", "options": ["$14$ m/s", "$8$ m/s", "$10$ m/s", "$16$ m/s"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Nồng độ bụi mịn PM2.5 tại một trạm quan trắc trong 6 giờ: 45, 55, 75, 80, 60, 45 (mcg/m$^3$). Số giờ nồng độ vượt ngưỡng an toàn (50 mcg/m$^3$) là:", "options": ["$4$ giờ", "$3$ giờ", "$5$ giờ", "$2$ giờ"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Biểu đồ đoạn thẳng ghi nhận lượng nước tiêu thụ của gia đình trong 4 tháng: 18, 22, 25, 20 ($m^3$). Giá nước là 10 000 đồng/$m^3$. Tổng số tiền nước 4 tháng là:", "options": ["$850$ nghìn đồng", "$800$ nghìn đồng", "$900$ nghìn đồng", "$750$ nghìn đồng"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Nếu dữ liệu có tính chu kì (ví dụ doanh thu bán kem cao vào mùa hè và thấp vào mùa đông lặp lại hằng năm), biểu đồ đoạn thẳng nhiều năm sẽ có hình dạng:", "options": ["Hình sóng lượn dao động tuần hoàn", "Đường thẳng dốc đứng liên tục", "Đường nằm ngang tuyệt đối", "Đường xoắn ốc"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Chỉ số CPI (chỉ số giá tiêu dùng) của một quốc gia qua 4 quý: 101,2; 101,8; 102,5; 103,1. Xu thế lạm phát qua 4 quý là:", "options": ["Mặt bằng giá tiếp tục tăng đều", "Mặt bằng giá giảm dần", "Giá cả đóng băng không đổi", "Không thể xác định"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Một người đầu tư 100 triệu. Năm đầu lãi 20%, năm thứ hai lỗ 20%. Sau hai năm số tiền còn lại là:", "options": ["$96$ triệu đồng", "$100$ triệu đồng", "$104$ triệu đồng", "$90$ triệu đồng"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Để dự báo xu thế giá vàng trong tương lai gần dựa vào biểu đồ đoạn thẳng lịch sử 30 ngày qua, người ta sử dụng đường nào?", "options": ["Đường xu thế (Trendline) hoặc trung bình động (Moving Average)", "Đường bao ngoài", "Đường tiệm cận ngang", "Đường phân giác"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Hiện tượng \"gây nhiễu thị giác\" trong biểu đồ đoạn thẳng thường xảy ra khi:", "options": ["Trục tung bị bóp méo tỉ lệ khiến độ dốc trông quá lớn hoặc quá phẳng so với thực tế", "Ghi chú quá nhiều chữ", "Dùng màu đen trắng", "Vẽ trên giấy kẻ ô vuông"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Biểu đồ đoạn thẳng kép biểu diễn doanh số bán điện thoại (triệu chiếc) của hai hãng X và Y qua 4 năm:\n- 2020: X = 15, Y = 10\n- 2021: X = 18, Y = 14\n- 2022: X = 20, Y = 18\n- 2023: X = 21, Y = 22.\nXét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Năm 2020, doanh số của hãng X gấp 1,5 lần hãng Y.", "isCorrect": True, "explanation": "$15 / 10 = 1{,}5$ lần."},
                {"id": "b", "statement": "Hãng Y có tốc độ tăng trưởng doanh số nhanh hơn hãng X qua các năm.", "isCorrect": True, "explanation": "Y tăng từ 10 lên 22 (tăng 120%), X tăng từ 15 lên 21 (tăng 40%)."},
                {"id": "c", "statement": "Năm 2023 là năm đầu tiên hãng Y vượt qua doanh số của hãng X.", "isCorrect": True, "explanation": "Năm 2023: Y = 22 > X = 21."},
                {"id": "d", "statement": "Tổng doanh số của hai hãng năm 2022 bằng năm 2023.", "isCorrect": False, "explanation": "Tổng 2022 = $20 + 18 = 38$; Tổng 2023 = $21 + 22 = 43 \\neq 38$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho bảng số liệu ghi nhận độ sâu (m) của mực nước trong hồ thủy điện qua các tháng mùa khô (tháng 1 đến tháng 5):\n- Tháng 1: 85 m\n- Tháng 2: 82 m\n- Tháng 3: 78 m\n- Tháng 4: 73 m\n- Tháng 5: 68 m.\nBiết mực nước chết của hồ là 65 m. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Mực nước hồ giảm liên tục qua các tháng mùa khô.", "isCorrect": True, "explanation": "Các giá trị giảm dần từ 85 xuống 68 m."},
                {"id": "b", "statement": "Độ giảm mực nước trung bình mỗi tháng là $4{,}25$ m.", "isCorrect": True, "explanation": "$(85 - 68) / 4 = 17 / 4 = 4{,}25$ m/tháng."},
                {"id": "c", "statement": "Tháng 4 có tốc độ sụt giảm mực nước mạnh nhất (giảm 5 m so với tháng trước).", "isCorrect": True, "explanation": "T3 -> T4 giảm $78 - 73 = 5$ m; T4 -> T5 cũng giảm 5 m (cùng giảm mạnh nhất)."},
                {"id": "d", "statement": "Đến tháng 5, mực nước hồ đã chạm mực nước chết.", "isCorrect": False, "explanation": "Mực nước tháng 5 là 68 m, vẫn cao hơn mực nước chết 65 m (cách 3 m)."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Doanh thu của một cửa hàng sách trong 4 tháng cuối năm lần lượt là: 40, 50, 60, 70 (triệu đồng). Dự báo theo đà tăng đều này thì doanh thu tháng 1 đầu năm sau là bao nhiêu triệu đồng?", "answer": 80, "unit": "triệu đồng"},
        {"id": 2, "level": "Vận dụng", "question": "Số ca mắc cúm mùa tại một trạm y tế trong 4 tuần: Tuần 1: 12 ca, Tuần 2: 24 ca, Tuần 3: 48 ca, Tuần 4: 36 ca. Tuần nào có số ca mắc tăng gấp đôi tuần trước đó (điền 1, 2, 3 hoặc 4)?", "answer": 2, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Một người tiết kiệm gửi ngân hàng 100 triệu với lãi suất kép 6%/năm. Sau 2 năm số tiền cả gốc và lãi người đó nhận được là bao nhiêu triệu đồng (làm tròn đến hàng phần trăm, ví dụ 112.36)?", "answer": 112.36, "unit": "triệu đồng"},
        {"id": 4, "level": "Vận dụng cao", "question": "Khối lượng một bao ngũ cốc giảm dần do hao hụt: Ngày 0: 50 kg; Ngày 10: 48,5 kg; Ngày 20: 47 kg; Ngày 30: 45,5 kg. Hỏi sau bao nhiêu ngày kể từ ngày 0 thì khối lượng bao ngũ cốc còn đúng 35 kg (nếu tốc độ hao hụt không đổi)?", "answer": 100, "unit": "ngày"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Biểu đồ đoạn thẳng kép ghi lại sản lượng xuất khẩu gạo (triệu tấn) và kim ngạch (tỷ USD) của Việt Nam trong 3 năm:\n- 2021: Sản lượng 6,2 triệu tấn; Kim ngạch 3,28 tỷ USD.\n- 2022: Sản lượng 7,1 triệu tấn; Kim ngạch 3,45 tỷ USD.\n- 2023: Sản lượng 8,1 triệu tấn; Kim ngạch 4,68 tỷ USD.\na) Tính giá xuất khẩu bình quân mỗi tấn gạo (USD/tấn) của từng năm (làm tròn đến hàng đơn vị).\nb) Nhận xét về xu hướng giá trị xuất khẩu gạo năm 2023 so với hai năm trước đó.",
            "maxScore": 1.0,
            "solution": "a) Giá xuất khẩu bình quân mỗi tấn gạo = $\\frac{\\text{Kim ngạch (tỷ USD)} \\times 10^9}{\\text{Sản lượng (triệu tấn)} \\times 10^6} = \\frac{\\text{Kim ngạch}}{\\text{Sản lượng}} \\times 1000$ (USD/tấn).\n- Năm 2021: $\\frac{3{,}28}{6{,}2} \\times 1000 \\approx 529$ USD/tấn.\n- Năm 2022: $\\frac{3{,}45}{7{,}1} \\times 1000 \\approx 486$ USD/tấn.\n- Năm 2023: $\\frac{4{,}68}{8{,}1} \\times 1000 \\approx 578$ USD/tấn.\nb) Nhận xét: Năm 2023, giá xuất khẩu gạo bình quân tăng vọt lên 578 USD/tấn (tăng gần 19% so với năm 2022). Cả sản lượng và giá bán đều tăng mạnh, giúp kim ngạch xuất khẩu gạo năm 2023 đạt mức kỉ lục 4,68 tỷ USD.",
            "rubric": [
                {"step": "Tính đúng giá bình quân cả 3 năm: 529, 486, 578 USD/tấn", "subScore": 0.6},
                {"step": "Phân tích và nhận xét sâu sắc xu hướng tăng trưởng năm 2023", "subScore": 0.4}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Bảng số liệu ghi lại tốc độ tăng trưởng GDP (%) của một quốc gia qua 5 năm:\n- Năm 1: 6,5%\n- Năm 2: 7,0%\n- Năm 3: 2,5% (năm dịch bệnh)\n- Năm 4: 8,0%\n- Năm 5: 6,8%.\na) Vẽ phác biểu đồ đoạn thẳng mô tả sự biến động của tốc độ tăng trưởng GDP.\nb) Hãy chỉ ra điểm gãy (biến động đột ngột) trên biểu đồ và giải thích nguyên nhân tác động thực tế của điểm gãy đó.",
            "maxScore": 1.0,
            "solution": "a) Mô tả biểu đồ đoạn thẳng:\n- Trục hoành: Năm 1, Năm 2, Năm 3, Năm 4, Năm 5.\n- Trục tung: Tốc độ tăng trưởng GDP (%).\n- Nối các điểm: $(1; 6{,}5) \\to (2; 7{,}0) \\to (3; 2{,}5) \\to (4; 8{,}0) \\to (5; 6{,}8)$.\nb) Điểm gãy trên biểu đồ:\n- Điểm gãy xuất hiện tại Năm 3 khi tốc độ tăng trưởng sụt giảm nghiêm trọng từ $7{,}0\\%$ xuống chỉ còn $2{,}5\\%$ (giảm 4,5 điểm phần trăm).\n- Giải thích thực tế: Năm 3 là năm xảy ra dịch bệnh bùng phát, các hoạt động sản xuất kinh doanh bị đình trệ, giãn cách xã hội khiến nền kinh tế bị ảnh hưởng nặng nề.\n- Ngay sau đó vào Năm 4, kinh tế phục hồi mạnh mẽ đạt đỉnh $8{,}0\\%$ (tăng trưởng chữ V) nhờ các chính sách kích cầu và mở cửa trở lại.",
            "rubric": [
                {"step": "Mô tả đầy đủ các mốc tọa độ và xu hướng đồ thị đoạn thẳng", "subScore": 0.5},
                {"step": "Chỉ ra điểm gãy năm 3 và phân tích nguyên nhân dịch bệnh cùng đà phục hồi năm 4", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một người bắt đầu tập thể dục giảm cân. Cân nặng của người đó được ghi lại vào ngày đầu tiên mỗi tháng như sau:\n- Tháng 1: 76 kg\n- Tháng 2: 74 kg\n- Tháng 3: 72,5 kg\n- Tháng 4: 71 kg\n- Tháng 5: 70 kg.\nMục tiêu của người đó là đạt cân nặng 65 kg.\na) Tính tốc độ giảm cân trung bình mỗi tháng của người đó từ tháng 1 đến tháng 5.\nb) Nếu tiếp tục duy trì tốc độ giảm cân trung bình trên, sau bao nhiêu tháng nữa kể từ tháng 5 người đó sẽ đạt được cân nặng mục tiêu?",
            "maxScore": 1.0,
            "solution": "a) Tổng số cân nặng đã giảm từ tháng 1 đến tháng 5 là:\n$76 - 70 = 6$ (kg).\nThời gian giảm là: $5 - 1 = 4$ (tháng).\nTốc độ giảm cân trung bình mỗi tháng là:\n$v = \\frac{6}{4} = 1{,}5$ (kg/tháng).\nb) Số cân nặng người đó cần giảm tiếp từ 70 kg về 65 kg là:\n$70 - 65 = 5$ (kg).\nThời gian cần thêm để đạt mục tiêu là:\n$t = \\frac{5}{1{,}5} = \\frac{10}{3} \\approx 3{,}33$ (tháng) (tức khoảng 3 tháng 10 ngày).\nVậy sau khoảng gần 3,5 tháng nữa (vào khoảng giữa tháng 8), người đó sẽ đạt được cân nặng mục tiêu 65 kg.",
            "rubric": [
                {"step": "Tính đúng tốc độ giảm cân trung bình là 1,5 kg/tháng", "subScore": 0.5},
                {"step": "Tính đúng thời gian cần thêm khoảng 3,33 tháng để đạt 65 kg", "subScore": 0.5}
            ]
        }
    ]
}

# =====================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG V: THU THẬP VÀ BIỂU DIỄN DỮ LIỆU
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c5_7_bai4_test1"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương V: Thu thập và biểu diễn dữ liệu - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Dữ liệu nào sau đây là số liệu (dữ liệu định lượng)?", "options": ["Chiều cao của các học sinh trong lớp", "Tên các môn học yêu thích", "Xếp loại rèn luyện (Tốt, Khá, Đạt)", "Màu sắc áo đồng phục"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Biểu đồ nào thích hợp nhất để biểu diễn tỉ lệ phần trăm các thành phần trong một tổng thể?", "options": ["Biểu đồ hình quạt tròn", "Biểu đồ đoạn thẳng", "Biểu đồ tranh", "Biểu đồ cột đơn"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Biểu đồ nào thích hợp nhất để theo dõi sự biến đổi nhiệt độ trong một ngày theo thời gian?", "options": ["Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn", "Biểu đồ tranh", "Bảng dữ liệu chữ"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Trong biểu đồ hình quạt tròn, góc ở tâm $90^\\circ$ biểu diễn bao nhiêu phần trăm tổng thể?", "options": ["$25\\%$", "$50\\%$", "$75\\%$", "$10\\%$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Phương pháp nào sau đây là phương pháp thu thập dữ liệu gián tiếp?", "options": ["Tra cứu niên giám thống kê trên cổng thông tin điện tử", "Phát phiếu hỏi trực tiếp", "Quan sát và ghi chép thí nghiệm", "Phỏng vấn từng người"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Dãy dữ liệu nào sau đây về điểm thi môn Toán (thang điểm 10) là hợp lí?", "options": ["$6; 7; 8{,}5; 9; 10$", "$5; 11; 8; -1; 7$", "$8; 9; A; 7; 6$", "$10; 8; 15; 9; 7$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Lớp 7A có 40 học sinh. Biểu đồ quạt tròn cho biết tỉ lệ học sinh thích chơi bóng đá là $45\\%$. Số học sinh thích chơi bóng đá của lớp 7A là:", "options": ["$18$ học sinh", "$20$ học sinh", "$16$ học sinh", "$22$ học sinh"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Góc ở tâm biểu diễn tỉ lệ $40\\%$ trong biểu đồ hình quạt tròn là:", "options": ["$144^\\circ$", "$120^\\circ$", "$100^\\circ$", "$160^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Nhiệt độ các ngày trong tuần: Thứ Hai: $28^\\circ$C, Thứ Ba: $30^\\circ$C, Thứ Tư: $29^\\circ$C, Thứ Năm: $32^\\circ$C. Ngày nào có nhiệt độ cao nhất?", "options": ["Thứ Năm", "Thứ Ba", "Thứ Hai", "Thứ Tư"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Khảo sát ý kiến của 50 học sinh về món ăn sáng: Bánh mì 25, Phở 15, Xôi 10. Tỉ lệ học sinh thích Bánh mì là:", "options": ["$50\\%$", "$30\\%$", "$20\\%$", "$40\\%$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Một tổ có 6 bạn có số điểm kiểm tra: $7; 8; 9; 8; 8; 8$. Điểm trung bình của tổ là:", "options": ["$8{,}0$", "$7{,}5$", "$8{,}2$", "$8{,}5$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Một gia đình có tổng thu nhập 15 triệu đồng/tháng. Biểu đồ quạt tròn cho biết tiền tiết kiệm chiếm 20%. Số tiền tiết kiệm mỗi tháng là:", "options": ["$3$ triệu đồng", "$2$ triệu đồng", "$4$ triệu đồng", "$2{,}5$ triệu đồng"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Biểu đồ quạt tròn biểu diễn tỉ lệ phân loại rác thải của một trường học: Giấy 35%, Nhựa 40%, Kim loại 15%, Rác khác 10%. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Rác thải nhựa chiếm tỉ lệ lớn nhất ($40\\%$).", "isCorrect": True, "explanation": "$40\\%$ là tỉ lệ cao nhất."},
                {"id": "b", "statement": "Góc ở tâm của hình quạt biểu diễn rác thải giấy là $126^\\circ$.", "isCorrect": True, "explanation": "$360^\\circ \\times 35\\% = 126^\\circ$."},
                {"id": "c", "statement": "Góc ở tâm biểu diễn rác kim loại là $54^\\circ$.", "isCorrect": True, "explanation": "$360^\\circ \\times 15\\% = 54^\\circ$."},
                {"id": "d", "statement": "Nếu tổng khối lượng rác là 200 kg thì rác hữu cơ/khác là 30 kg.", "isCorrect": False, "explanation": "Khối lượng rác khác $= 200 \\times 10\\% = 20$ kg, không phải 30 kg."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho các khẳng định về lựa chọn biểu đồ thích hợp để biểu diễn dữ liệu, xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Để so sánh dân số giữa 5 thành phố lớn tại một thời điểm, ta nên dùng biểu đồ cột.", "isCorrect": True, "explanation": "Biểu đồ cột trực quan nhất để so sánh các số lượng tuyệt đối."},
                {"id": "b", "statement": "Để biểu diễn sự thay đổi giá vàng trong 30 ngày vừa qua, ta nên dùng biểu đồ đoạn thẳng.", "isCorrect": True, "explanation": "Biểu đồ đoạn thẳng thích hợp nhất cho sự biến thiên theo thời gian."},
                {"id": "c", "statement": "Để biểu diễn tỉ lệ phần trăm các loại chi phí sinh hoạt của gia đình, ta nên dùng biểu đồ hình quạt tròn.", "isCorrect": True, "explanation": "Biểu đồ quạt tròn tối ưu cho tỉ lệ cơ cấu phần trăm của một tổng thể."},
                {"id": "d", "statement": "Biểu đồ hình quạt tròn có thể dùng để biểu diễn đại lượng có giá trị âm.", "isCorrect": False, "explanation": "Các phần trăm và góc ở tâm trong biểu đồ quạt tròn luôn là các giá trị dương."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính góc ở tâm (độ) của hình quạt biểu diễn tỉ lệ $20\\%$ trong biểu đồ hình quạt tròn.", "answer": 72, "unit": "độ"},
        {"id": 2, "level": "Thông hiểu", "question": "Điểm kiểm tra của An qua 3 lần là: 7, 8, 9. Tính điểm trung bình của An qua 3 lần đó.", "answer": 8, "unit": ""},
        {"id": 3, "level": "Vận dụng", "question": "Một trường học có 600 học sinh. Biểu đồ quạt cho biết có 15% học sinh đi xe buýt. Có bao nhiêu học sinh đi xe buýt đến trường?", "answer": 90, "unit": "học sinh"},
        {"id": 4, "level": "Vận dụng", "question": "Nhiệt độ lúc 7h sáng là $21^\\circ$C, lúc 13h trưa là $29^\\circ$C. Độ chênh lệch nhiệt độ giữa hai thời điểm là bao nhiêu độ C?", "answer": 8, "unit": "độ C"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Khảo sát ý thích về 4 môn thể thao của 120 học sinh khối 7 thu được kết quả:\n- Bóng đá: 48 bạn\n- Cầu lông: 36 bạn\n- Bơi lội: 24 bạn\n- Bóng rổ: 12 bạn\na) Lập bảng tỉ lệ phần trăm của từng môn thể thao.\nb) Tính góc ở tâm tương ứng của mỗi môn thể thao khi biểu diễn trên biểu đồ hình quạt tròn.",
            "maxScore": 1.0,
            "solution": "a) Tỉ lệ phần trăm của từng môn:\n- Bóng đá: $\\frac{48}{120} \\times 100\\% = 40\\%$.\n- Cầu lông: $\\frac{36}{120} \\times 100\\% = 30\\%$.\n- Bơi lội: $\\frac{24}{120} \\times 100\\% = 20\\%$.\n- Bóng rổ: $\\frac{12}{120} \\times 100\\% = 10\\%$.\nb) Góc ở tâm tương ứng:\n- Bóng đá: $360^\\circ \\times 40\\% = 144^\\circ$.\n- Cầu lông: $360^\\circ \\times 30\\% = 108^\\circ$.\n- Bơi lội: $360^\\circ \\times 20\\% = 72^\\circ$.\n- Bóng rổ: $360^\\circ \\times 10\\% = 36^\\circ$.",
            "rubric": [
                {"step": "Tính đúng các tỉ lệ: 40%, 30%, 20%, 10%", "subScore": 0.5},
                {"step": "Tính đúng các góc ở tâm: 144 độ, 108 độ, 72 độ, 36 độ", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Biểu đồ đoạn thẳng theo dõi lượng điện tiêu thụ (kWh) của một hộ gia đình trong 6 tháng đầu năm:\n- Tháng 1: 180 kWh\n- Tháng 2: 160 kWh\n- Tháng 3: 170 kWh\n- Tháng 4: 210 kWh\n- Tháng 5: 260 kWh\n- Tháng 6: 300 kWh\na) Tháng nào gia đình tiêu thụ nhiều điện nhất? Tháng nào tiêu thụ ít điện nhất?\nb) Giải thích vì sao lượng điện tiêu thụ lại tăng mạnh trong tháng 5 và tháng 6.",
            "maxScore": 1.0,
            "solution": "a) - Tháng tiêu thụ nhiều điện nhất là Tháng 6 (300 kWh).\n- Tháng tiêu thụ ít điện nhất là Tháng 2 (160 kWh).\nb) Giải thích thực tế: Tháng 5 và tháng 6 là thời điểm bắt đầu vào mùa hè nắng nóng đỉnh điểm ở nước ta. Gia đình sử dụng nhiều thiết bị làm mát công suất lớn như quạt điện, máy điều hòa nhiệt độ hoạt động liên tục cả ngày lẫn đêm, dẫn đến sản lượng điện tiêu thụ tăng vọt.",
            "rubric": [
                {"step": "Chỉ ra đúng tháng nhiều nhất (T6) và ít nhất (T2)", "subScore": 0.5},
                {"step": "Giải thích hợp lí nguyên nhân thời tiết mùa hè nắng nóng dùng máy lạnh", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một tổ có 10 học sinh làm một bài kiểm tra Toán. Điểm của 9 bạn là: $6, 7, 8, 8, 9, 7, 8, 9, 10$. Biết điểm trung bình của cả tổ 10 bạn là $8{,}0$. Hãy tìm điểm của bạn thứ 10.",
            "maxScore": 1.0,
            "solution": "Tổng điểm của cả 10 bạn là:\n$S = 10 \\times 8{,}0 = 80$ (điểm).\nTổng điểm của 9 bạn đã biết là:\n$6 + 7 + 8 + 8 + 9 + 7 + 8 + 9 + 10 = 72$ (điểm).\nĐiểm số của bạn thứ 10 là:\n$x = 80 - 72 = 8$ (điểm).\nVậy bạn thứ 10 đạt 8 điểm.",
            "rubric": [
                {"step": "Tính tổng điểm cả tổ: 80 điểm", "subScore": 0.5},
                {"step": "Tính tổng 9 bạn là 72 và suy ra bạn thứ 10 được 8 điểm", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c5_7_bai4_test2"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương V: Thu thập và biểu diễn dữ liệu - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Để biểu diễn số lượng học sinh giỏi các lớp 7A, 7B, 7C, 7D, loại biểu đồ nào sau đây là phù hợp nhất?", "options": ["Biểu đồ cột", "Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn", "Biểu đồ đám mây"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Biểu đồ quạt tròn biểu diễn xếp loại thi đua có góc ở tâm của khối Tốt là $162^\\circ$. Tỉ lệ học sinh đạt loại Tốt là:", "options": ["$45\\%$", "$40\\%$", "$50\\%$", "$35\\%$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Một giải bóng đá có 8 đội thi đấu vòng tròn 1 lượt. Mỗi trận thắng được 3 điểm, hòa 1 điểm, thua 0 điểm. Dữ liệu \"số điểm của các đội sau giải\" thuộc loại:", "options": ["Dữ liệu số rời rạc", "Dữ liệu định tính", "Dữ liệu liên tục", "Dữ liệu không so sánh được"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Biểu đồ đoạn thẳng ghi lại số ca khỏi bệnh Covid-19 trong một tuần có đoạn dốc đứng nhất vào ngày nào? Điều đó có ý nghĩa gì?", "options": ["Ngày có số ca khỏi bệnh tăng nhanh nhất so với ngày trước", "Ngày có số ca khỏi bệnh thấp nhất", "Ngày không có ca khỏi bệnh nào", "Ngày trạm y tế đóng cửa"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Cơ cấu chi phí sản xuất một sản phẩm gồm: Nguyên liệu 50%, Nhân công 30%, Khấu hao 15%, Chi khác 5%. Góc ở tâm biểu diễn chi phí Nguyên liệu là:", "options": ["$180^\\circ$", "$150^\\circ$", "$120^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một cửa hàng thống kê doanh thu 4 tuần của tháng 12: 50, 65, 80, 105 (triệu đồng). Doanh thu tuần 4 tăng bao nhiêu phần trăm so với tuần 1?", "options": ["$110\\%$", "$100\\%$", "$120\\%$", "$90\\%$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Khảo sát thời gian xem tivi mỗi ngày của 5 học sinh: 1h, 1,5h, 2h, 2,5h, 3h. Thời gian xem trung bình của nhóm là:", "options": ["$2$ giờ", "$1{,}8$ giờ", "$2{,}2$ giờ", "$2{,}5$ giờ"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Trong biểu đồ quạt tròn, phần dành cho thể thao chiếm góc $108^\\circ$. Nếu có tổng cộng 500 bạn được khảo sát thì có bao nhiêu bạn chọn thể thao?", "options": ["$150$ bạn", "$120$ bạn", "$180$ bạn", "$100$ bạn"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Cho dãy dữ liệu nhiệt độ: $25, 27, 26, 31, 28, 29$. Trung vị của dãy số liệu là:", "options": ["$27{,}5$", "$27$", "$28$", "$26{,}5$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Một người bán hàng lãi 15% trong tháng 1, lãi 25% trong tháng 2 so với vốn ban đầu không đổi. Mức tăng trưởng lợi nhuận của tháng 2 so với tháng 1 là:", "options": ["$66{,}7\\%$", "$10\\%$", "$50\\%$", "$40\\%$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Khi đọc biểu đồ đoạn thẳng, việc trục tung không xuất phát từ 0 mà không có kí hiệu ngắt trục có thể gây ra ảo giác gì?", "options": ["Làm người đọc cảm thấy sự khác biệt giữa các số liệu bị phóng đại quá mức", "Làm cho số liệu trông nhỏ hơn thực tế", "Làm mất tính thời gian của số liệu", "Làm đổi chiều tăng giảm"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một trường học có 1200 học sinh. Để chọn mẫu 60 học sinh khảo sát, người ta chọn ngẫu nhiên mỗi lớp 2 học sinh. Cách chọn mẫu này gọi là:", "options": ["Chọn mẫu phân tầng ngẫu nhiên", "Chọn mẫu thuận tiện", "Chọn mẫu tự nguyện", "Chọn mẫu cụm"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Biểu đồ hình quạt tròn biểu diễn tỉ lệ học sinh tham gia 3 môn năng khiếu: Vẽ 30%, Hát 45%, Nhảy hiện đại 25%. Tổng số học sinh là 200 bạn. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Số bạn thích Hát là $90$ bạn.", "isCorrect": True, "explanation": "$200 \\times 45\\% = 90$ bạn."},
                {"id": "b", "statement": "Góc ở tâm biểu diễn môn Nhảy hiện đại là $90^\\circ$.", "isCorrect": True, "explanation": "$360^\\circ \\times 25\\% = 90^\\circ$."},
                {"id": "c", "statement": "Số bạn thích Vẽ nhiều hơn số bạn thích Nhảy là 10 bạn.", "isCorrect": True, "explanation": "Vẽ: 60 bạn; Nhảy: 50 bạn $\\Rightarrow 60 - 50 = 10$ bạn."},
                {"id": "d", "statement": "Góc ở tâm biểu diễn môn Hát là $180^\\circ$.", "isCorrect": False, "explanation": "$360^\\circ \\times 45\\% = 162^\\circ \\neq 180^\\circ$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một biểu đồ đoạn thẳng biểu diễn số sản phẩm lỗi của một nhà máy trong 5 tuần: Tuần 1: 50, Tuần 2: 42, Tuần 3: 35, Tuần 4: 25, Tuần 5: 18. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Số sản phẩm lỗi có xu hướng giảm liên tục qua các tuần.", "isCorrect": True, "explanation": "Các giá trị giảm đều: 50 -> 42 -> 35 -> 25 -> 18."},
                {"id": "b", "statement": "Tổng số sản phẩm lỗi trong 5 tuần là $170$ sản phẩm.", "isCorrect": True, "explanation": "$50 + 42 + 35 + 25 + 18 = 170$ sản phẩm."},
                {"id": "c", "statement": "Tuần 4 có số lỗi giảm nhiều nhất so với tuần liền trước (giảm 10 lỗi).", "isCorrect": True, "explanation": "$35 - 25 = 10$ lỗi (các tuần khác giảm 8, 7, 7)."},
                {"id": "d", "statement": "Số sản phẩm lỗi ở Tuần 5 giảm hơn $70\\%$ so với Tuần 1.", "isCorrect": False, "explanation": "Tỉ lệ giảm $= (50 - 18) / 50 = 32 / 50 = 64\\% < 70\\%$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Góc ở tâm của hình quạt biểu diễn tỉ lệ $45\\%$ là bao nhiêu độ?", "answer": 162, "unit": "độ"},
        {"id": 2, "level": "Vận dụng", "question": "Điểm trung bình của 4 bài kiểm tra môn Toán là 7,5. Sau bài kiểm tra thứ năm, điểm trung bình tăng lên thành 7,8. Hỏi bài kiểm tra thứ năm bạn đó đạt mấy điểm?", "answer": 9, "unit": "điểm"},
        {"id": 3, "level": "Vận dụng", "question": "Một công ty có doanh thu quý I là 40 tỷ đồng, quý II là 52 tỷ đồng. Doanh thu quý II tăng bao nhiêu phần trăm so với quý I?", "answer": 30, "unit": "%"},
        {"id": 4, "level": "Vận dụng cao", "question": "Biểu đồ quạt tròn có 3 hình quạt. Góc ở tâm của hình quạt 1 là $144^\\circ$, hình quạt 2 là $108^\\circ$. Hỏi hình quạt 3 chiếm bao nhiêu phần trăm tổng thể?", "answer": 30, "unit": "%"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Bảng số liệu sau ghi nhận kim ngạch xuất khẩu thủy sản của Việt Nam trong 4 quý năm 2023:\n- Quý I: 1,8 tỷ USD\n- Quý II: 2,3 tỷ USD\n- Quý III: 2,5 tỷ USD\n- Quý IV: 2,4 tỷ USD\na) Vẽ bảng phân bố tỉ lệ phần trăm kim ngạch xuất khẩu từng quý so với cả năm (tổng cả năm là 9,0 tỷ USD).\nb) Tính số đo góc ở tâm tương ứng của từng quý trên biểu đồ hình quạt tròn.",
            "maxScore": 1.0,
            "solution": "a) Tổng kim ngạch cả năm $= 1{,}8 + 2{,}3 + 2{,}5 + 2{,}4 = 9{,}0$ (tỷ USD).\nTỉ lệ phần trăm từng quý:\n- Quý I: $\\frac{1{,}8}{9{,}0} \\times 100\\% = 20\\%$.\n- Quý II: $\\frac{2{,}3}{9{,}0} \\times 100\\% \\approx 25{,}56\\%$.\n- Quý III: $\\frac{2{,}5}{9{,}0} \\times 100\\% \\approx 27{,}78\\%$.\n- Quý IV: $\\frac{2{,}4}{9{,}0} \\times 100\\% \\approx 26{,}66\\%$.\nb) Góc ở tâm tương ứng:\n- Quý I: $360^\\circ \\times 20\\% = 72^\\circ$.\n- Quý II: $360^\\circ \\times \\frac{2{,}3}{9{,}0} = 92^\\circ$.\n- Quý III: $360^\\circ \\times \\frac{2{,}5}{9{,}0} = 100^\\circ$.\n- Quý IV: $360^\\circ \\times \\frac{2{,}4}{9{,}0} = 96^\\circ$.\nKiểm tra: $72^\\circ + 92^\\circ + 100^\\circ + 96^\\circ = 360^\\circ$.",
            "rubric": [
                {"step": "Tính đúng các tỉ lệ phần trăm từng quý", "subScore": 0.5},
                {"step": "Tính đúng các góc ở tâm: 72, 92, 100, 96 độ", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một người ghi chép thời gian chạy bộ mỗi ngày trong 1 tuần (phút): $30; 35; 40; 0; 45; 50; 45$.\na) Xác định giá trị bất thường trong dãy số liệu trên và giải thích lí do.\nb) Tính thời gian chạy bộ trung bình mỗi ngày trong những ngày người đó có tập luyện.",
            "maxScore": 1.0,
            "solution": "a) Giá trị bất thường là $0$ (phút).\nGiải thích: Giá trị này tương ứng với ngày người đó nghỉ tập (hoặc bận việc đột xuất/ốm), khác biệt hoàn toàn với thói quen tập từ 30 đến 50 phút của các ngày còn lại.\nb) Số ngày có tập luyện là 6 ngày. Tổng thời gian tập của 6 ngày là:\n$30 + 35 + 40 + 45 + 50 + 45 = 245$ (phút).\nThời gian chạy bộ trung bình mỗi ngày tập là:\n$\\bar{t} = \\frac{245}{6} \\approx 40{,}83$ phút (khoảng 40 phút 50 giây).",
            "rubric": [
                {"step": "Chỉ ra giá trị bất thường 0 phút và giải thích hợp lí", "subScore": 0.5},
                {"step": "Tính đúng thời gian trung bình của 6 ngày tập là 40,83 phút", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một lớp học có 40 học sinh gồm 3 tổ. Tổ 1 có 12 bạn có điểm trung bình môn Văn là 7,5. Tổ 2 có 14 bạn có điểm trung bình là 8,0. Cả lớp có điểm trung bình là 7,8.\na) Tính điểm trung bình môn Văn của Tổ 3.\nb) Nhận xét về chất lượng học tập môn Văn giữa 3 tổ.",
            "maxScore": 1.0,
            "solution": "a) Số học sinh của Tổ 3 là:\n$40 - (12 + 14) = 40 - 26 = 14$ (học sinh).\nTổng điểm môn Văn của cả lớp là:\n$S = 40 \\times 7{,}8 = 312$ (điểm).\nTổng điểm của Tổ 1 là:\n$S_1 = 12 \\times 7{,}5 = 90$ (điểm).\nTổng điểm của Tổ 2 là:\n$S_2 = 14 \\times 8{,}0 = 112$ (điểm).\nTổng điểm của Tổ 3 là:\n$S_3 = 312 - (90 + 112) = 312 - 202 = 110$ (điểm).\nĐiểm trung bình môn Văn của Tổ 3 là:\n$\\bar{X}_3 = \\frac{110}{14} \\approx 7{,}86$ (điểm).\nb) Nhận xét: Tổ 2 có điểm trung bình cao nhất ($8{,}0$), tiếp theo là Tổ 3 ($7{,}86$) và Tổ 1 thấp nhất ($7{,}5$). Cả 3 tổ đều đạt mức điểm Khá giỏi đồng đều.",
            "rubric": [
                {"step": "Tính đúng số học sinh Tổ 3 là 14 và điểm trung bình xấp xỉ 7,86", "subScore": 0.6},
                {"step": "So sánh và đưa ra nhận xét chính xác giữa 3 tổ", "subScore": 0.4}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c5_7_bai4_test3"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương V: Thu thập và biểu diễn dữ liệu - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Khi muốn khảo sát ý kiến học sinh về việc đổi mới đồng phục, phương pháp chọn mẫu nào sau đây tránh được thiên vị giới tính và khối lớp nhất?", "options": ["Chọn mẫu ngẫu nhiên phân tầng theo khối lớp và theo giới tính nam/nữ", "Phỏng vấn các bạn ở câu lạc bộ thời trang", "Hỏi các bạn nữ trong trường", "Lấy ý kiến đại diện của các bạn trong ban cán sự lớp"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Trong biểu đồ quạt tròn có 4 hình quạt A, B, C, D tỉ lệ thuận với các số $2, 3, 4, 6$. Số đo góc ở tâm của hình quạt lớn nhất là:", "options": ["$144^\\circ$", "$120^\\circ$", "$96^\\circ$", "$160^\\circ$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Một người đầu tư cổ phiếu: ngày 1 tăng 10%, ngày 2 giảm 10% so với ngày 1. So với giá ban đầu, giá cổ phiếu sau 2 ngày:", "options": ["Giảm $1\\%$", "Không thay đổi", "Tăng $1\\%$", "Giảm $2\\%$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Một dãy gồm 9 số nguyên dương xếp theo thứ tự tăng dần có số trung vị là 15. Nếu tăng số lớn nhất lên 10 đơn vị thì số trung vị mới là:", "options": ["$15$", "$25$", "$16$", "Không xác định"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Biểu đồ đoạn thẳng kép ghi nhận doanh thu và chi phí của công ty qua 4 quý. Lợi nhuận đạt mức cao nhất khi:", "options": ["Khoảng cách thẳng đứng từ điểm doanh thu xuống điểm chi phí là lớn nhất (doanh thu > chi phí)", "Doanh thu cao nhất", "Chi phí thấp nhất", "Doanh thu bằng chi phí"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một bể bơi ghi nhận lượng khách trong 4 ngày nghỉ lễ: 500, 650, 800, 950 người. Lượng khách trung bình mỗi ngày là:", "options": ["$725$ người", "$700$ người", "$750$ người", "$800$ người"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Biểu đồ quạt tròn biểu diễn 3 thành phần X, Y, Z. Biết diện tích hình quạt X bằng $\\frac{1}{3}$ hình quạt Y, hình quạt Y bằng $\\frac{1}{2}$ hình quạt Z. Góc ở tâm của hình quạt X là:", "options": ["$36^\\circ$", "$72^\\circ$", "$108^\\circ$", "$144^\\circ$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho bảng phân bố điểm thi môn Toán của 50 học sinh có trung bình là 7,2. Khi phát hiện một bài 4 điểm bị chấm nhầm thành 9 điểm và được sửa lại, điểm trung bình thực tế của lớp là:", "options": ["$7{,}1$", "$7{,}0$", "$7{,}15$", "$7{,}05$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Một tam giác số liệu hình quạt tròn có 3 góc ở tâm tỉ lệ với $1 : 2 : 3$. Tỉ lệ phần trăm của hình quạt lớn nhất là:", "options": ["$50\\%$", "$60\\%$", "$33{,}3\\%$", "$45\\%$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Khi nghiên cứu mối quan hệ giữa chiều cao và cân nặng của học sinh, loại biểu đồ thích hợp nhất để nhận biết tương quan hai đại lượng là:", "options": ["Biểu đồ phân tán (Scatter plot)", "Biểu đồ hình quạt tròn", "Biểu đồ cột đơn", "Biểu đồ tranh"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho dãy số: $2, 4, 6, 8, \\dots, 2n$ có trung bình cộng bằng 21. Giá trị của $n$ là:", "options": ["$20$", "$21$", "$19$", "$22$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một người quan sát thấy biểu đồ doanh thu một công ty có trục tung bắt đầu từ 90 đến 100 với bước nhảy 1 đơn vị. Đoạn thẳng dốc vọt lên trên biểu đồ thực tế thể hiện mức tăng trưởng:", "options": ["Rất nhỏ (chỉ vài phần trăm) nhưng bị phóng đại trực quan do ngắt trục", "Tăng trưởng đột biến hàng trăm phần trăm", "Doanh thu bị giảm", "Không có doanh thu"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Một gia đình phân bổ ngân sách 30 triệu đồng/tháng thành 4 khoản: Sinh hoạt phí 45%, Học phí cho con 25%, Tiết kiệm 20%, Quỹ dự phòng 10%. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Số tiền chi cho sinh hoạt phí là $13{,}5$ triệu đồng.", "isCorrect": True, "explanation": "$30 \\times 45\\% = 13{,}5$ triệu đồng."},
                {"id": "b", "statement": "Góc ở tâm của hình quạt biểu diễn quỹ dự phòng là $36^\\circ$.", "isCorrect": True, "explanation": "$360^\\circ \\times 10\\% = 36^\\circ$."},
                {"id": "c", "statement": "Số tiền dành cho học phí và tiết kiệm tổng cộng là $13{,}5$ triệu đồng.", "isCorrect": True, "explanation": "$25\\% + 20\\% = 45\\% \\Rightarrow 30 \\times 45\\% = 13{,}5$ triệu đồng."},
                {"id": "d", "statement": "Góc ở tâm của hình quạt biểu diễn học phí gấp đôi quỹ dự phòng.", "isCorrect": False, "explanation": "Học phí là 25%, dự phòng là 10% $\\Rightarrow 25/10 = 2{,}5$ lần, không phải gấp đôi."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho bảng số liệu ghi nhận sự tăng trưởng chiều cao (cm) của một cây tre giống mới qua 5 ngày:\n- Ngày 1: 10 cm\n- Ngày 2: 25 cm\n- Ngày 3: 50 cm\n- Ngày 4: 90 cm\n- Ngày 5: 150 cm.\nXét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tốc độ tăng chiều cao của cây tre ngày sau luôn lớn hơn ngày trước.", "isCorrect": True, "explanation": "Mức tăng mỗi ngày: $15, 25, 40, 60$ cm (tăng dần)."},
                {"id": "b", "statement": "Trong ngày thứ 5 (từ ngày 4 đến ngày 5), cây tre cao thêm $60$ cm.", "isCorrect": True, "explanation": "$150 - 90 = 60$ cm."},
                {"id": "c", "statement": "Chiều cao trung bình mỗi ngày cây tre tăng được trong 4 khoảng ngày là $35$ cm/ngày.", "isCorrect": True, "explanation": "$(150 - 10) / 4 = 140 / 4 = 35$ cm/ngày."},
                {"id": "d", "statement": "Biểu đồ đoạn thẳng mô tả chiều cao cây tre có độ dốc giảm dần.", "isCorrect": False, "explanation": "Tốc độ tăng ngày càng nhanh nên biểu đồ có độ dốc ngày càng lớn (cong vồng lên), không phải giảm dần."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Một tổ gồm 5 học sinh có cân nặng trung bình là 42 kg. Sau khi một bạn nặng 50 kg chuyển sang tổ khác, cân nặng trung bình của 4 bạn còn lại là bao nhiêu kg?", "answer": 40, "unit": "kg"},
        {"id": 2, "level": "Vận dụng", "question": "Góc ở tâm của hình quạt thứ nhất là $150^\\circ$, hình quạt thứ hai là $120^\\circ$, hình quạt thứ ba chiếm phần còn lại. Hỏi hình quạt thứ ba chiếm bao nhiêu phần trăm tổng thể?", "answer": 25, "unit": "%"},
        {"id": 3, "level": "Vận dụng cao", "question": "Một người chạy bộ tuần 1 chạy 20 km. Mỗi tuần sau người đó tăng quãng đường chạy thêm 10% so với tuần trước đó. Hỏi trong tuần thứ 3 người đó chạy được bao nhiêu km (điền số thập phân)?", "answer": 24.2, "unit": "km"},
        {"id": 4, "level": "Vận dụng cao", "question": "Biểu đồ quạt tròn biểu diễn 3 thành phần A, B, C. Tỉ số diện tích giữa A và B là 2:3, giữa B và C là 3:5. Tính số đo góc ở tâm (độ) của thành phần C.", "answer": 180, "unit": "độ"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Một công ty dự định đầu tư vào 3 mảng kinh doanh: Nông nghiệp công nghệ cao, Năng lượng tái tạo và Dịch vụ số với tỉ lệ vốn góp ban đầu theo thứ tự là $2 : 3 : 5$. Tổng số vốn là 200 tỷ đồng.\na) Tính số vốn đầu tư vào từng mảng.\nb) Sau 1 năm, vốn ở mảng Nông nghiệp tăng $20\\%$, Năng lượng tăng $10\\%$, Dịch vụ số tăng $30\\%$. Tính cơ cấu tỉ lệ phần trăm mới của 3 mảng sau 1 năm (làm tròn đến hàng phần mười).",
            "maxScore": 1.0,
            "solution": "a) Tổng số phần bằng nhau là: $2 + 3 + 5 = 10$ phần.\nGiá trị 1 phần là: $200 : 10 = 20$ (tỷ đồng).\nSố vốn ban đầu của từng mảng:\n- Nông nghiệp: $20 \\times 2 = 40$ tỷ đồng.\n- Năng lượng: $20 \\times 3 = 60$ tỷ đồng.\n- Dịch vụ số: $20 \\times 5 = 100$ tỷ đồng.\nb) Số vốn của từng mảng sau 1 năm:\n- Nông nghiệp: $40 \\times (1 + 0{,}2) = 48$ tỷ đồng.\n- Năng lượng: $60 \\times (1 + 0{,}1) = 66$ tỷ đồng.\n- Dịch vụ số: $100 \\times (1 + 0{,}3) = 130$ tỷ đồng.\nTổng số vốn sau 1 năm là: $48 + 66 + 130 = 244$ tỷ đồng.\nCơ cấu tỉ lệ phần trăm mới:\n- Nông nghiệp: $\\frac{48}{244} \\times 100\\% \\approx 19{,}7\\%$.\n- Năng lượng: $\\frac{66}{244} \\times 100\\% \\approx 27{,}0\\%$.\n- Dịch vụ số: $\\frac{130}{244} \\times 100\\% \\approx 53{,}3\\%$.\nTổng tỉ lệ mới $= 19{,}7\\% + 27{,}0\\% + 53{,}3\\% = 100\\%$.",
            "rubric": [
                {"step": "Tính đúng vốn ban đầu: Nông nghiệp 40, Năng lượng 60, Dịch vụ số 100 tỷ", "subScore": 0.5},
                {"step": "Tính đúng vốn mới và cơ cấu phần trăm mới: 19,7%, 27,0%, 53,3%", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Biểu đồ đoạn thẳng kép ghi nhận doanh thu (D) và chi phí (C) của một chuỗi nhà hàng qua 4 quý năm 2024 (đơn vị: tỷ đồng):\n| Quý | I | II | III | IV |\n| Doanh thu (D) | 12 | 15 | 18 | 22 |\n| Chi phí (C) | 10 | 11 | 13 | 15 |\na) Tính lợi nhuận (Lợi nhuận = Doanh thu - Chi phí) của chuỗi nhà hàng ở từng quý.\nb) Tính tỉ suất lợi nhuận trên doanh thu (Lợi nhuận / Doanh thu) của cả năm 2024.",
            "maxScore": 1.0,
            "solution": "a) Lợi nhuận của chuỗi nhà hàng từng quý:\n- Quý I: $12 - 10 = 2$ tỷ đồng.\n- Quý II: $15 - 11 = 4$ tỷ đồng.\n- Quý III: $18 - 13 = 5$ tỷ đồng.\n- Quý IV: $22 - 15 = 7$ tỷ đồng.\nb) Tổng doanh thu cả năm 2024:\n$D_{\\text{năm}} = 12 + 15 + 18 + 22 = 67$ tỷ đồng.\nTổng chi phí cả năm 2024:\n$C_{\\text{năm}} = 10 + 11 + 13 + 15 = 49$ tỷ đồng.\nTổng lợi nhuận cả năm 2024:\n$L_{\\text{năm}} = 67 - 49 = 18$ tỷ đồng (hoặc $2 + 4 + 5 + 7 = 18$ tỷ đồng).\nTỉ suất lợi nhuận trên doanh thu cả năm là:\n$P = \\frac{18}{67} \\times 100\\% \\approx 26{,}87\\%$.",
            "rubric": [
                {"step": "Tính đúng lợi nhuận từng quý: 2, 4, 5, 7 tỷ đồng", "subScore": 0.5},
                {"step": "Tính đúng tổng cả năm và tỉ suất lợi nhuận xấp xỉ 26,87%", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho dãy số nguyên dương gồm $n$ số: $x_1, x_2, \\dots, x_n$ có trung bình cộng bằng 10. Nếu thêm số 26 vào dãy thì trung bình cộng của dãy mới là 12.\na) Tìm số phần tử $n$ ban đầu.\nb) Nếu tiếp tục bỏ đi số nhỏ nhất trong dãy ban đầu là số 2 thì trung bình cộng của các số còn lại là bao nhiêu?",
            "maxScore": 1.0,
            "solution": "a) Tổng của $n$ số ban đầu là:\n$S = 10n$.\nKhi thêm số 26 vào dãy, tổng mới là $10n + 26$ và số lượng phần tử mới là $n + 1$.\nTheo đề bài, trung bình cộng mới là 12, nên ta có phương trình:\n$\\frac{10n + 26}{n + 1} = 12$\n$\\Leftrightarrow 10n + 26 = 12(n + 1)$\n$\\Leftrightarrow 10n + 26 = 12n + 12$\n$\\Leftrightarrow 2n = 14 \\Rightarrow n = 7$.\nVậy số phần tử ban đầu là $n = 7$.\nb) Tổng của 7 số ban đầu là $S = 10 \\times 7 = 70$.\nKhi bỏ đi số 2, tổng của 6 số còn lại là:\n$S' = 70 - 2 = 68$.\nTrung bình cộng của 6 số còn lại là:\n$\\bar{X}' = \\frac{68}{6} = \\frac{34}{3} \\approx 11{,}33$.",
            "rubric": [
                {"step": "Thiết lập phương trình và giải ra n = 7", "subScore": 0.6},
                {"step": "Tính đúng trung bình cộng còn lại là 34/3 xấp xỉ 11,33", "subScore": 0.4}
            ]
        }
    ]
}
