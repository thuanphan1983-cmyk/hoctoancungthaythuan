# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI - BÀI 19: BIỂU DIỄN DỮ LIỆU BẰNG BẢNG, BIỂU ĐỒ (TOÁN 8 - KNTT)
Gồm 3 đề phân hóa:
- Đề 1 (Cơ bản): Lựa chọn biểu đồ thích hợp (cột, cột kép, đoạn thẳng, quạt tròn), đọc số liệu bảng/biểu đồ, tính góc ở tâm cơ bản.
- Đề 2 (Khá): Chuyển đổi bảng số liệu sang biểu đồ, tính góc ở tâm phức hợp, phân tích số liệu biểu đồ cột kép và đoạn thẳng.
- Đề 3 (Nâng cao): Nhận diện biểu đồ gây hiểu lầm (trục tung bị cắt, tỉ lệ sai, 3D biến dạng), thiết kế bảng biểu chuẩn tắc.
"""

BAI2_EXAMS = {}

# ==============================================================================
# BÀI 19 - ĐỀ 1: CƠ BẢN (🌱)
# ==============================================================================
BAI2_EXAMS["c5_8_bai2_test1"] = {
    "title": "Toán 8 (KNTT) - Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Loại biểu đồ nào sau đây thích hợp nhất để biểu diễn tỉ lệ phần trăm các thành phần trong một tổng thể?",
            "options": ["Biểu đồ hình quạt tròn", "Biểu đồ đoạn thẳng", "Biểu đồ cột", "Biểu đồ tranh"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Loại biểu đồ nào sau đây thích hợp nhất để biểu diễn sự thay đổi của một đại lượng theo thời gian?",
            "options": ["Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn", "Biểu đồ tranh", "Biểu đồ cột kép"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Nhận biết",
            "question": "Để so sánh số học sinh Giỏi và Khá của các lớp khối 8, loại biểu đồ nào sau đây là phù hợp nhất?",
            "options": ["Biểu đồ cột kép", "Biểu đồ hình quạt tròn", "Biểu đồ đoạn thẳng", "Biểu đồ tranh"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Nhận biết",
            "question": "Trong biểu đồ hình quạt tròn, toàn bộ hình tròn biểu diễn bao nhiêu phần trăm?",
            "options": ["$100\\%$", "$50\\%$", "$360\\%$", "$180\\%$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Nhận biết",
            "question": "Trong biểu đồ hình quạt tròn, một hình quạt có số đo góc ở tâm là $90^\\circ$ biểu diễn tỉ lệ bao nhiêu phần trăm?",
            "options": ["$25\\%$", "$50\\%$", "$20\\%$", "$30\\%$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Nhận biết",
            "question": "Trong biểu đồ hình quạt tròn, nửa hình tròn ứng với số đo góc ở tâm là bao nhiêu độ?",
            "options": ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$270^\\circ$"],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Nhận biết",
            "question": "Trục nằm ngang của biểu đồ đoạn thẳng thường dùng để ghi đại lượng nào?",
            "options": [
                "Mốc thời gian (ngày, tháng, năm,...)",
                "Giá trị số lượng (tấn, triệu đồng,...)",
                "Tên các biểu tượng tranh",
                "Tỉ lệ phần trăm"
            ],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Thông hiểu",
            "question": "Tỉ lệ phần trăm $10\\%$ tương ứng với hình quạt tròn có số đo góc ở tâm là:",
            "options": ["$36^\\circ$", "$10^\\circ$", "$18^\\circ$", "$45^\\circ$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Một hình quạt tròn có số đo góc ở tâm là $72^\\circ$. Hình quạt này biểu diễn bao nhiêu phần trăm dữ liệu?",
            "options": ["$20\\%$", "$15\\%$", "$25\\%$", "$30\\%$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Một cửa hàng bán được 120 chiếc áo gồm 3 kích cỡ: S (30 chiếc), M (60 chiếc), L (30 chiếc). Trên biểu đồ quạt tròn, phần biểu diễn áo cỡ M có góc ở tâm bằng:",
            "options": ["$180^\\circ$", "$90^\\circ$", "$120^\\circ$", "$150^\\circ$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Khi muốn biểu diễn số lượng xe máy bán ra của 5 hãng Honda, Yamaha, Piaggio, Suzuki, SYM trong một tháng, nên chọn loại biểu đồ nào?",
            "options": ["Biểu đồ cột", "Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn kép", "Biểu đồ tranh không chú giải"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Cho bảng số liệu ghi lại số học sinh giỏi qua các năm học từ 2020 đến 2024. Để thấy rõ xu hướng tăng giảm số học sinh giỏi qua từng năm, nên vẽ biểu đồ nào?",
            "options": ["Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn", "Biểu đồ tranh", "Biểu đồ cột nằm ngang"],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một gia đình lập bảng chi tiêu hàng tháng gồm 4 khoản chính: Ăn uống ($40\\%$), Giáo dục ($25\\%$), Tiết kiệm ($20\\%$), Chi khác ($15\\%$). Toàn bộ dữ liệu được biểu diễn trên một biểu đồ hình quạt tròn.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Tổng tỉ lệ phần trăm của các hình quạt trên biểu đồ bằng đúng $100\\%$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Hình quạt biểu diễn khoản chi cho Giáo dục có số đo góc ở tâm là $90^\\circ$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Hình quạt biểu diễn khoản Tiết kiệm có số đo góc ở tâm là $60^\\circ$.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Nếu tổng thu nhập hàng tháng của gia đình là 24 triệu đồng thì khoản chi cho Ăn uống là 9.6 triệu đồng.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Biểu đồ đoạn thẳng biểu diễn nhiệt độ đo được tại một trạm quan trắc vào các mốc thời gian trong ngày: 6 giờ ($20^\\circ\\text{C}$); 9 giờ ($25^\\circ\\text{C}$); 12 giờ ($30^\\circ\\text{C}$); 15 giờ ($28^\\circ\\text{C}$); 18 giờ ($24^\\circ\\text{C}$).",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Biểu đồ đoạn thẳng là công cụ trực quan phù hợp để theo dõi sự thay đổi nhiệt độ theo thời gian.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Thời điểm có nhiệt độ cao nhất trong ngày đo được là lúc 12 giờ.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Từ 12 giờ đến 18 giờ, nhiệt độ tại trạm đo có xu hướng tăng.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Chênh lệch giữa nhiệt độ cao nhất và nhiệt độ thấp nhất trong các mốc đo trên là $10^\\circ\\text{C}$.", "correct": True }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Trong biểu đồ hình quạt tròn, góc ở tâm của hình quạt biểu diễn tỉ lệ $30\\%$ có số đo bằng bao nhiêu độ?",
            "answer": "108"
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho biểu đồ cột biểu diễn số cây trồng được của 4 lớp 8A, 8B, 8C, 8D lần lượt là: 25, 30, 20, 35 cây. Tổng số cây trồng được của cả 4 lớp là bao nhiêu cây?",
            "answer": "110"
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Một hình quạt tròn biểu diễn số học sinh thích môn Toán có góc ở tâm là $54^\\circ$. Hình quạt này biểu diễn bao nhiêu phần trăm học sinh?",
            "answer": "15"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Biểu đồ đoạn thẳng ghi lại doanh thu 4 quý của một cửa hàng: Quý 1: 50 triệu; Quý 2: 70 triệu; Quý 3: 65 triệu; Quý 4: 95 triệu. Tính mức chênh lệch doanh thu giữa Quý 4 và Quý 1 (đơn vị: triệu đồng).",
            "answer": "45"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Một khảo sát về phương tiện đến trường của 40 học sinh lớp 8C cho kết quả:\n- Xe đạp: 20 học sinh;\n- Xe buýt: 10 học sinh;\n- Đi bộ: 6 học sinh;\n- Xe máy điện: 4 học sinh.\na) Hãy tính tỉ lệ phần trăm học sinh sử dụng mỗi loại phương tiện.\nb) Tính số đo góc ở tâm tương ứng với từng loại phương tiện để biểu diễn trên biểu đồ hình quạt tròn.",
            "rubric": "a) Tính tỉ lệ phần trăm:\n- Xe đạp: (20 / 40) * 100% = 50% (0.15đ).\n- Xe buýt: (10 / 40) * 100% = 25% (0.15đ).\n- Đi bộ: (6 / 40) * 100% = 15% (0.1đ).\n- Xe máy điện: (4 / 40) * 100% = 10% (0.1đ).\nb) Tính số đo góc ở tâm:\n- Xe đạp: 50% * 360° = 180° (0.15đ).\n- Xe buýt: 25% * 360° = 90° (0.15đ).\n- Đi bộ: 15% * 360° = 54° (0.1đ).\n- Xe máy điện: 10% * 360° = 36° (0.1đ)."
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho bảng số liệu về sản lượng thu hoạch lúa (tấn) của một trang trại qua 4 năm:\n- Năm 2021: 120 tấn;\n- Năm 2022: 150 tấn;\n- Năm 2023: 140 tấn;\n- Năm 2024: 180 tấn.\na) Em hãy cho biết nên lựa chọn loại biểu đồ nào để biểu diễn trực quan xu thế biến đổi sản lượng lúa của trang trại qua các năm? Giải thích vì sao.\nb) Nêu các bước cơ bản để vẽ biểu đồ đó.",
            "rubric": "a) Lựa chọn biểu đồ:\n- Nên chọn biểu đồ đoạn thẳng (hoặc biểu đồ cột) (0.25đ).\n- Giải thích: Vì dữ liệu là một chuỗi thời gian liên tục qua các năm, biểu đồ đoạn thẳng giúp quan sát rõ nét nhất xu hướng tăng, giảm của sản lượng lúa (0.25đ).\nb) Các bước vẽ biểu đồ đoạn thẳng:\n- Bước 1: Vẽ hai trục vuông góc: trục ngang biểu diễn các mốc năm (2021, 2022, 2023, 2024), trục đứng biểu diễn sản lượng (tấn) có chia vạch tỉ lệ phù hợp (0.2đ).\n- Bước 2: Xác định các điểm biểu diễn số liệu tương ứng của từng năm trên mặt phẳng tọa độ (0.15đ).\n- Bước 3: Nối các điểm liên tiếp bằng các đoạn thẳng, ghi giá trị số liệu tại các điểm và đặt tên biểu đồ (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho bảng thống kê hai chiều về số lượng học sinh Giỏi các môn Toán và Tiếng Anh của hai lớp 8A và 8B:\n- Lớp 8A: Môn Toán có 15 học sinh, Môn Tiếng Anh có 18 học sinh;\n- Lớp 8B: Môn Toán có 20 học sinh, Môn Tiếng Anh có 12 học sinh.\na) Nên sử dụng loại biểu đồ nào để so sánh trực quan thành tích học sinh Giỏi hai môn giữa hai lớp?\nb) Mô tả cách bố trí các cột trên biểu đồ đó và chỉ rõ chú giải cần thiết.",
            "rubric": "a) Lựa chọn biểu đồ:\n- Nên sử dụng biểu đồ cột kép (0.4đ).\nb) Mô tả cách bố trí:\n- Trục ngang: Ghi tên hai môn học (Toán, Tiếng Anh) hoặc tên hai lớp (8A, 8B) (0.2đ).\n- Trục đứng: Biểu diễn số học sinh giỏi (chia thang đo từ 0 đến 25) (0.2đ).\n- Chú giải: Cần phân biệt hai cột cạnh nhau bằng màu sắc hoặc họa tiết khác nhau (ví dụ: cột màu xanh biểu diễn lớp 8A, cột màu cam biểu diễn lớp 8B) (0.2đ)."
        }
    ]
}

# ==============================================================================
# BÀI 19 - ĐỀ 2: KHÁ (🌿)
# ==============================================================================
BAI2_EXAMS["c5_8_bai2_test2"] = {
    "title": "Toán 8 (KNTT) - Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây là ĐÚNG khi nói về biểu đồ cột kép?",
            "options": [
                "Biểu diễn từng cặp giá trị của hai đối tượng trên cùng một tiêu chí để so sánh trực diện",
                "Chỉ biểu diễn được các số liệu tỉ lệ phần trăm có tổng bằng $100\\%$",
                "Luôn luôn có hình quạt tròn ở giữa tâm biểu đồ",
                "Không bao giờ cần đến bảng chú giải phân biệt các cột"
            ],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Một hình quạt tròn biểu diễn tỉ lệ $35\\%$ của tập dữ liệu. Số đo góc ở tâm của hình quạt đó là:",
            "options": ["$126^\\circ$", "$135^\\circ$", "$120^\\circ$", "$140^\\circ$"],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Hình quạt tròn có góc ở tâm là $63^\\circ$ thì tương ứng với tỉ lệ bao nhiêu phần trăm?",
            "options": ["$17.5\\%$", "$15\\%$", "$20\\%$", "$18.5\\%$"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Thông hiểu",
            "question": "Lớp 8A có 48 học sinh. Khi biểu diễn xếp loại học tập trên biểu đồ quạt tròn, phần biểu diễn học sinh Tốt có góc ở tâm bằng $120^\\circ$. Số học sinh Tốt của lớp là:",
            "options": ["$16$ học sinh", "$12$ học sinh", "$18$ học sinh", "$20$ học sinh"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Thông hiểu",
            "question": "Khi muốn biểu diễn cơ cấu các nguồn vốn đầu tư trong nền kinh tế qua 2 năm khác nhau, cách biểu diễn nào trực quan và khoa học nhất?",
            "options": [
                "Vẽ 2 biểu đồ hình quạt tròn đặt cạnh nhau",
                "Vẽ 1 biểu đồ tranh không có thang đo",
                "Vẽ 1 biểu đồ đoạn thẳng đơn",
                "Vẽ 1 biểu đồ cột đơn"
            ],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Thông hiểu",
            "question": "Biểu đồ đoạn thẳng kép thường được sử dụng hiệu quả nhất để làm gì?",
            "options": [
                "So sánh xu thế diễn biến theo thời gian của hai đối tượng khác nhau",
                "Chia nhỏ một hình tròn thành 100 phần bằng nhau",
                "Biểu diễn cơ cấu ngân sách của một cá nhân",
                "Xếp thứ tự các loại hoa quả yêu thích"
            ],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Thông hiểu",
            "question": "Một biểu đồ hình quạt tròn có 4 phần, trong đó ba phần có số đo góc lần lượt là $90^\\circ, 108^\\circ, 72^\\circ$. Góc ở tâm của phần thứ tư là:",
            "options": ["$90^\\circ$", "$80^\\circ$", "$100^\\circ$", "$75^\\circ$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng thấp",
            "question": "Bảng số liệu doanh thu (tỷ đồng) của hai chi nhánh công ty trong 3 năm:\nChi nhánh A: 2021 (10), 2022 (15), 2023 (18).\nChi nhánh B: 2021 (12), 2022 (14), 2023 (20).\nNhận định nào đúng khi vẽ biểu đồ cột kép?",
            "options": [
                "Cả hai chi nhánh đều có doanh thu tăng liên tục qua các năm",
                "Chi nhánh A luôn có doanh thu cao hơn Chi nhánh B qua tất cả các năm",
                "Doanh thu Chi nhánh B năm 2022 thấp hơn năm 2021",
                "Nên dùng biểu đồ quạt tròn để so sánh từng năm thay vì cột kép"
            ],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng thấp",
            "question": "Biểu đồ hình quạt tròn biểu diễn tỉ lệ học sinh tham gia 3 môn thi đấu: Cầu lông ($45\\%$), Điền kinh ($35\\%$), Bơi lội ($20\\%$). Tỉ số giữa góc ở tâm của môn Cầu lông và môn Bơi lội bằng:",
            "options": ["$\\frac{9}{4}$", "$\\frac{7}{4}$", "$\\frac{5}{2}$", "$\\frac{4}{9}$"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng thấp",
            "question": "Biểu đồ cột biểu diễn số xe bán ra có trục đứng bắt đầu từ $50$ thay vì $0$. Cột đại diện cho tháng 1 có giá trị $60$ (độ cao cột là 10 đơn vị), cột tháng 2 có giá trị $70$ (độ cao cột là 20 đơn vị). Cảm quan thị giác thấy cột tháng 2 cao gấp đôi cột tháng 1, nhưng thực tế giá trị bán ra tháng 2 gấp tháng 1 khoảng:",
            "options": ["$1.17$ lần", "$2.0$ lần", "$3.0$ lần", "$1.5$ lần"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng thấp",
            "question": "Một trường học có 600 học sinh. Trên biểu đồ quạt tròn, góc biểu diễn số học sinh đi xe buýt là $54^\\circ$, số học sinh đi xe đạp là $144^\\circ$. Số học sinh đi xe đạp nhiều hơn số học sinh đi xe buýt là:",
            "options": ["$150$ học sinh", "$120$ học sinh", "$180$ học sinh", "$90$ học sinh"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng thấp",
            "question": "Cho bảng thống kê 2 chiều về kết quả học lực khối 8. Khi chuyển dữ liệu này sang dạng biểu đồ cột chồng (stacked bar chart), mỗi cột chồng biểu diễn:",
            "options": [
                "Tổng số học sinh của một lớp, được chia thành các đoạn biểu diễn từng mức học lực",
                "Tỉ lệ tăng trưởng theo thời gian của một cá nhân",
                "Góc ở tâm của hình tròn tương ứng với học sinh Tốt",
                "Hiệu số giữa số học sinh nam và học sinh nữ"
            ],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một câu lạc bộ thể thao trường có 120 học sinh tham gia 4 bộ môn: Bóng đá ($45$ em), Cầu lông ($30$ em), Bóng bàn ($15$ em), Bơi lội ($30$ em). Người ta biểu diễn số liệu này trên biểu đồ hình quạt tròn.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Môn Bóng đá chiếm tỉ lệ lớn nhất với $37.5\\%$ tổng số học sinh.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Hình quạt biểu diễn môn Bóng bàn có góc ở tâm là $45^\\circ$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Hình quạt biểu diễn môn Bơi lội có góc ở tâm là $100^\\circ$.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tổng số đo góc ở tâm của hai môn Cầu lông và Bơi lội là $180^\\circ$.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Biểu đồ cột kép biểu diễn số học sinh Nam và Nữ tham gia kì thi học sinh giỏi cấp huyện của trường A qua 3 năm học:\n- Năm học 1: Nam 12, Nữ 18;\n- Năm học 2: Nam 15, Nữ 15;\n- Năm học 3: Nam 20, Nữ 16.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Năm học 1 có tổng số học sinh tham gia là 30 em.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Số lượng học sinh Nam tham gia có xu hướng tăng liên tục qua 3 năm học.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Tỉ số phần trăm học sinh Nữ ở năm học 1 là $50\\%$.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Tổng số học sinh Nam tham gia trong cả 3 năm nhiều hơn tổng số học sinh Nữ tham gia trong cả 3 năm.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính số đo góc ở tâm (độ) của hình quạt tròn biểu diễn tỉ lệ $22.5\\%$.",
            "answer": "81"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một khối lớp 8 có 200 học sinh. Trên biểu đồ quạt tròn, phần biểu diễn số học sinh giỏi có góc ở tâm bằng $72^\\circ$. Hỏi khối 8 có bao nhiêu học sinh giỏi?",
            "answer": "40"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Biểu đồ cột biểu diễn doanh số bán máy tính qua 3 tháng: Tháng 1 là 80 máy, Tháng 2 là 100 máy, Tháng 3 là 120 máy. Tốc độ tăng trưởng doanh số từ Tháng 1 đến Tháng 3 là bao nhiêu phần trăm?",
            "answer": "50"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Biểu đồ quạt tròn chia làm 3 phần. Phần thứ nhất có góc $150^\\circ$, phần thứ hai có góc gấp đôi phần thứ ba. Tính số đo góc (độ) của phần thứ ba.",
            "answer": "70"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho bảng thống kê cơ cấu nguồn thu của một quỹ thiện nguyện học đường năm 2024:\n- Ủng hộ từ phụ huynh: 60 triệu đồng;\n- Ủng hộ từ cựu học sinh: 45 triệu đồng;\n- Doanh thu từ hội chợ kế hoạch nhỏ: 30 triệu đồng;\n- Tài trợ từ doanh nghiệp: 15 triệu đồng.\na) Lập bảng tính tỉ lệ phần trăm và tính số đo góc ở tâm tương ứng của từng nguồn thu.\nb) Trình bày các bước vẽ biểu đồ hình quạt tròn hoàn chỉnh từ các số liệu trên.",
            "rubric": "a) Tính tổng và tỉ lệ, số đo góc:\n- Tổng quỹ: 60 + 45 + 30 + 15 = 150 (triệu đồng) (0.1đ).\n- Phụ huynh: 60/150 = 40%; Góc: 40% * 360° = 144° (0.15đ).\n- Cựu học sinh: 45/150 = 30%; Góc: 30% * 360° = 108° (0.15đ).\n- Hội chợ: 30/150 = 20%; Góc: 20% * 360° = 72° (0.1đ).\n- Doanh nghiệp: 15/150 = 10%; Góc: 10% * 360° = 36° (0.1đ).\nb) Các bước vẽ biểu đồ:\n- Vẽ đường tròn tâm O bán kính bất kì (0.1đ).\n- Vẽ bán kính đầu tiên nằm ngang làm gốc (0.1đ).\n- Dùng thước đo góc vẽ lần lượt các góc ở tâm 144°, 108°, 72°, 36° liền kề nhau (0.1đ).\n- Tô màu/kí hiệu các hình quạt, ghi tỉ lệ phần trăm, lập bảng chú giải và tên biểu đồ (0.1đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một người bán hàng theo dõi doanh thu của cửa hàng trong 6 tháng đầu năm và băn khoăn giữa hai cách vẽ biểu đồ: Biểu đồ cột và Biểu đồ đoạn thẳng.\na) Em hãy so sánh ưu điểm và nhược điểm của hai loại biểu đồ này trong bài toán trên.\nb) Theo em, người bán hàng nên ưu tiên dùng loại biểu đồ nào nếu mục đích chính là phát hiện các tháng có bước ngoặt doanh thu tăng/giảm mạnh?",
            "rubric": "a) So sánh hai loại biểu đồ:\n- Biểu đồ cột: Ưu điểm là so sánh quy mô độ lớn doanh thu giữa các tháng rất trực quan, dễ đọc chính xác độ cao cột; Nhược điểm là đường nối biến thiên không liền mạch bằng đường thẳng (0.35đ).\n- Biểu đồ đoạn thẳng: Ưu điểm là làm nổi bật xu thế tăng/giảm, độ dốc của đoạn thẳng phản ánh trực tiếp tốc độ tăng trưởng; Nhược điểm là khó cảm nhận ngay tỉ lệ quy mô tuyệt đối nếu không nhìn kĩ trục tung (0.35đ).\nb) Lựa chọn tối ưu:\n- Nếu mục đích là phát hiện bước ngoặt và tốc độ biến thiên theo thời gian thì nên ưu tiên BIỂU ĐỒ ĐOẠN THẲNG, vì độ dốc đi lên hoặc đi xuống thể hiện rất rõ thời điểm tăng tốc hay suy thoái (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho bảng thống kê 2 chiều về kết quả học tập môn Toán của 2 lớp 8A và 8B:\n- Lớp 8A (sĩ số 40): Tốt: 16 em; Khá: 16 em; Đạt: 8 em;\n- Lớp 8B (sĩ số 40): Tốt: 10 em; Khá: 22 em; Đạt: 8 em.\na) Tính tỉ lệ phần trăm học sinh đạt loại Tốt và loại Khá của từng lớp.\nb) Nếu vẽ biểu đồ cột kép để so sánh hai lớp, hãy nêu nhận xét về chất lượng học tập môn Toán giữa lớp 8A và lớp 8B.",
            "rubric": "a) Tính tỉ lệ phần trăm:\n- Lớp 8A: Tốt: (16/40)*100% = 40%; Khá: (16/40)*100% = 40%; Đạt: (8/40)*100% = 20% (0.25đ).\n- Lớp 8B: Tốt: (10/40)*100% = 25%; Khá: (22/40)*100% = 55%; Đạt: (8/40)*100% = 20% (0.25đ).\nb) Nhận xét từ biểu đồ cột kép:\n- Cả hai lớp có tỉ lệ học sinh mức Đạt bằng nhau (20%) (0.15đ).\n- Lớp 8A có tỉ lệ học sinh đạt loại Tốt cao hơn vượt trội so với lớp 8B (40% so với 25%, cột Tốt của 8A cao hơn) (0.2đ).\n- Lớp 8B có học sinh tập trung đông nhất ở mức Khá (55%), trong khi lớp 8A có chất lượng mũi nhọn tốt hơn (0.15đ)."
        }
    ]
}

# ==============================================================================
# BÀI 19 - ĐỀ 3: NÂNG CAO (🚀)
# ==============================================================================
BAI2_EXAMS["c5_8_bai2_test3"] = {
    "title": "Toán 8 (KNTT) - Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Hiện tượng 'Cắt cụt trục tung' (Truncated graph) trong biểu đồ cột nhằm mục đích gì?",
            "options": [
                "Làm phóng đại thị giác sự khác biệt nhỏ giữa các cột số liệu",
                "Tiết kiệm diện tích trang giấy khi in ấn tài liệu",
                "Chuyển đổi biểu đồ cột thành biểu đồ hình quạt tròn",
                "Đảm bảo các cột luôn có cùng diện tích"
            ],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Khi biểu diễn dữ liệu bằng biểu đồ hình quạt tròn dạng 3D (không gian ba chiều) bị nghiêng, sai lầm thị giác nào thường xuất hiện?",
            "options": [
                "Hình quạt nằm ở góc nhìn phía trước trông lớn hơn hình quạt có cùng diện tích ở phía sau",
                "Tất cả các hình quạt đều tự động biến thành hình tam giác đều",
                "Tổng các góc ở tâm luôn bị giảm xuống còn $180^\\circ$",
                "Trục hoành và trục tung bị đảo ngược vị trí"
            ],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một biểu đồ cột có trục tung bắt đầu từ giá trị $100$. Cột A có giá trị $105$ (hiển thị cao 5 đơn vị), cột B có giá trị $125$ (hiển thị cao 25 đơn vị). Người xem cảm nhận cột B cao gấp 5 lần cột A, nhưng thực tế giá trị B chỉ gấp A khoảng:",
            "options": ["$1.19$ lần", "$5.00$ lần", "$2.50$ lần", "$1.50$ lần"],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Một biểu đồ hình quạt tròn biểu diễn cơ cấu thị phần của 4 doanh nghiệp. Biết doanh nghiệp A chiếm $40\\%$, doanh nghiệp B chiếm $25\\%$, doanh nghiệp C có góc ở tâm là $72^\\circ$. Hỏi doanh nghiệp D có góc ở tâm là bao nhiêu độ?",
            "options": ["$54^\\circ$", "$36^\\circ$", "$45^\\circ$", "$60^\\circ$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Vận dụng thấp",
            "question": "Khi muốn biểu diễn mối quan hệ giữa hai biến định lượng liên tục (ví dụ: Chiều cao và Cân nặng của học sinh), loại biểu đồ nào thích hợp nhất?",
            "options": ["Biểu đồ phân tán (Scatter plot)", "Biểu đồ tranh", "Biểu đồ hình quạt tròn", "Biểu đồ cột chồng"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng thấp",
            "question": "Biểu đồ đoạn thẳng ghi nhận chỉ số giá tiêu dùng có các mốc thời gian trên trục hoành: 2010, 2015, 2016, 2017, 2024. Điểm sai sót về mặt quy chuẩn hiển thị là:",
            "options": [
                "Khoảng cách vật lí giữa các năm không tỉ lệ thuận với khoảng cách thời gian thực tế",
                "Không được vẽ đoạn thẳng nối các năm có số chẵn",
                "Thiếu hình tròn bao quanh các điểm dữ liệu",
                "Trục tung bắt buộc phải đi qua năm 2000"
            ],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng cao",
            "question": "Một biểu đồ hình quạt tròn biểu diễn 3 thành phần X, Y, Z. Biết góc ở tâm của X bằng $\\frac{3}{5}$ góc của Y, và góc của Z bằng trung bình cộng góc của X và Y. Số đo góc ở tâm của thành phần X là:",
            "options": ["$77.14^\\circ$", "$90.00^\\circ$", "$80.00^\\circ$", "$72.00^\\circ$"],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng cao",
            "question": "Trong một biểu đồ cột so sánh sản lượng 2 nhà máy, chiều cao cột nhà máy A là $h$, nhà máy B là $2h$. Người thiết kế vẽ cột nhà máy B có cả chiều rộng gấp đôi cột nhà máy A. Diện tích cột B gấp mấy lần diện tích cột A, gây ảo giác tăng trưởng bao nhiêu lần?",
            "options": ["$4$ lần", "$2$ lần", "$8$ lần", "$3$ lần"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng cao",
            "question": "Cho bảng dữ liệu về dân số đô thị và nông thôn qua 30 năm (1990 - 2020, mỗi 10 năm một mốc). Để vừa thể hiện được sự biến thiên của tổng dân số, vừa thể hiện được cơ cấu tỉ lệ giữa đô thị và nông thôn, loại biểu đồ tối ưu nhất là:",
            "options": [
                "Biểu đồ miền hoặc biểu đồ cột chồng kết hợp",
                "Ba biểu đồ quạt tròn kích thước bằng nhau",
                "Biểu đồ tranh có ký hiệu người",
                "Biểu đồ đoạn thẳng chỉ vẽ đường nông thôn"
            ],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng cao",
            "question": "Một khảo sát có 5 lựa chọn A, B, C, D, E. Biểu đồ quạt tròn có tỉ lệ phần trăm của A, B, C, D lần lượt là $20\\%, 30\\%, 15\\%, 25\\%$. Khi chuyển dữ liệu này sang biểu đồ cột, tỉ số chiều cao cột B so với cột E bằng:",
            "options": ["$3$", "$2$", "$2.5$", "$4$"],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng cao",
            "question": "Quy tắc vàng trong hiển thị biểu đồ trung thực (Ethical data visualization) yêu cầu trục tung biểu diễn số lượng phải thỏa mãn điều kiện nào?",
            "options": [
                "Gốc tọa độ phải bắt đầu từ giá trị 0 (trừ trường hợp biểu diễn chỉ số biến động nhỏ có ghi chú rõ)",
                "Luôn bắt đầu từ giá trị nhỏ nhất của tập dữ liệu trừ đi 1",
                "Không bao giờ được chia độ dài các khoảng bằng nhau",
                "Phải vẽ theo thang đo logarit trong mọi bài toán"
            ],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng cao",
            "question": "Một báo cáo kinh doanh công bố biểu đồ quạt tròn có 5 thành phần với tỉ lệ lần lượt là: $35\\%, 28\\%, 22\\%, 12\\%, 8\\%$. Báo cáo này bị chuyên gia tài chính bác bỏ ngay lập tức vì lý do:",
            "options": [
                "Tổng các tỉ lệ phần trăm bằng $105\\%$, vi phạm định lí toàn thể",
                "Tỉ lệ thành phần nhỏ nhất nhỏ hơn $10\\%$",
                "Không sử dụng biểu đồ đoạn thẳng thay thế",
                "Có quá nhiều thành phần trên một hình tròn"
            ],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một hãng xe điện công bố biểu đồ cột so sánh quãng đường đi được sau 1 lần sạc của xe Hãng X ($120\\text{ km}$) và xe đối thủ Y ($100\\text{ km}$). Trục tung của biểu đồ bắt đầu từ vạch $95\\text{ km}$, khoảng cách mỗi vạch là $5\\text{ km}$. Trên biểu đồ, cột xe X cao gấp 5 lần cột xe Y.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Trên thực tế, quãng đường xe X đi được chỉ dài hơn xe đối thủ Y đúng $20\\%$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Cảm quan thị giác độ cao cột xe X gấp 5 lần cột xe Y là do gốc trục tung bị cắt xén bắt đầu từ $95$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Cách vẽ biểu đồ như trên hoàn toàn khách quan và tuân thủ chuẩn mực đạo đức trình bày dữ liệu.", "correct": False },
                { "key": "d", "level": "Vận dụng cao", "text": "Nếu vẽ lại biểu đồ với trục tung bắt đầu từ 0 thì cột xe X chỉ cao gấp $1.2$ lần cột xe Y.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Một công ty công nghệ biểu diễn thị phần các hệ điều hành điện thoại trên biểu đồ hình quạt tròn. Hệ điều hành A chiếm $55\\%$, hệ điều hành B chiếm $30\\%$, còn lại là các hệ điều hành khác.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Các hệ điều hành khác chiếm $15\\%$ thị phần.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Góc ở tâm của hình quạt biểu diễn hệ điều hành B là $108^\\circ$.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Góc ở tâm biểu diễn hệ điều hành A lớn hơn góc biểu diễn hệ điều hành B là $90^\\circ$.", "correct": False },
                { "key": "d", "level": "Vận dụng cao", "text": "Nếu vẽ biểu đồ dạng 3D nghiêng và đặt lát cắt hệ điều hành B ở tiền cảnh phía trước, người xem có thể lầm tưởng hệ điều hành B có thị phần tương đương hệ điều hành A.", "correct": True }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Một biểu đồ hình quạt tròn biểu diễn 4 thành phần A, B, C, D. Biết góc của A là $120^\\circ$, góc của B là $90^\\circ$, góc của C là $80^\\circ$. Tính số đo góc ở tâm (độ) của thành phần D.",
            "answer": "70"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một biểu đồ cột có trục tung bắt đầu từ $80$. Giá trị cột 1 là $90$ (hiển thị 10 đơn vị), giá trị cột 2 là $110$ (hiển thị 30 đơn vị). Hỏi trên biểu đồ cột 2 cao gấp mấy lần cột 1?",
            "answer": "3"
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho biểu đồ quạt tròn biểu diễn tỉ lệ học sinh tham gia 3 câu lạc bộ: Thể thao, Nghệ thuật và Học thuật. Biết góc của Thể thao chiếm $40\\%$ góc toàn phần ($144^\\circ$). Tỉ số góc giữa Nghệ thuật và Học thuật là $3:2$. Tính số đo góc (độ) của câu lạc bộ Nghệ thuật.",
            "answer": "129.6"
        },
        {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Một biểu đồ đoạn thẳng ghi nhận tốc độ tăng trưởng doanh số của sản phẩm. Năm 1: 100 sản phẩm, Năm 2: 150 sản phẩm, Năm 3: 225 sản phẩm. Tỉ số phần trăm tăng trưởng của Năm 3 so với Năm 2 là bao nhiêu phần trăm?",
            "answer": "50"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Một mẩu tin quảng cáo sữa tăng chiều cao đăng biểu đồ cột so sánh chiều cao trung bình của trẻ sau 6 tháng sử dụng:\n- Nhóm dùng sữa thường: $118\\text{ cm}$;\n- Nhóm dùng sữa X: $120\\text{ cm}$.\nNgười thiết kế vẽ trục tung bắt đầu từ $117\\text{ cm}$ đến $121\\text{ cm}$. Nhìn vào biểu đồ, cột sữa X cao gấp 3 lần cột sữa thường.\na) Em hãy chỉ ra thủ thuật trực quan gây hiểu lầm trong biểu đồ trên.\nb) Tính toán xem thực tế trẻ dùng sữa X cao hơn trẻ dùng sữa thường bao nhiêu phần trăm, và nêu phương án vẽ lại biểu đồ trung thực.",
            "rubric": "a) Thủ thuật trực quan gây hiểu lầm:\n- Biểu đồ đã cắt cụt trục tung (bắt đầu từ 117 cm thay vì 0 cm) (0.25đ).\n- Chiều cao hiển thị của cột sữa thường là 118 - 117 = 1 đơn vị, cột sữa X là 120 - 117 = 3 đơn vị, tạo cảm giác sữa X giúp cao gấp 3 lần (0.25đ).\nb) Tính toán thực tế và phương án sửa:\n- Mức chênh lệch thực tế: (120 - 118) / 118 ≈ 1.69% (0.25đ).\n- Phương án vẽ lại trung thực: Trục tung phải bắt đầu từ vạch 0 cm với thang chia đều đặn (ví dụ từ 0 đến 130 cm). Khi đó hai cột có độ cao gần như ngang nhau (chênh nhau khoảng 1.7%), phản ánh đúng bản chất dữ liệu (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho bảng dữ liệu về tỉ lệ học sinh tốt nghiệp THCS đỗ vào THPT công lập của một huyện qua 4 năm: 2021 ($70\\%$), 2022 ($72\\%$), 2023 ($68\\%$), 2024 ($75\\%$).\na) Nếu biểu diễn bằng biểu đồ đoạn thẳng với trục tung từ $0\\%$ đến $100\\%$, đường biểu diễn sẽ trông khá bằng phẳng. Có nên bắt đầu trục tung từ $60\\%$ không? Vì sao?\nb) Trong trường hợp trục tung không bắt đầu từ 0, người thiết kế đồ họa cần tuân thủ nguyên tắc gì để không bị coi là ngụy tạo số liệu?",
            "rubric": "a) Nhận định về việc cắt trục tung:\n- CÓ THỂ bắt đầu từ 60% để làm rõ sự dao động tinh tế trong khoảng 68% - 75% vốn rất có ý nghĩa trong công tác quản lí giáo dục (0.35đ).\nb) Nguyên tắc tuân thủ để tránh ngụy tạo:\n- Phải có kí hiệu ngắt trục (dấu ziczac hoặc nét đứt sóng trên trục tung) để cảnh báo người đọc rằng trục tung không bắt đầu từ 0 (0.35đ).\n- Ghi rõ ràng các số liệu phần trăm cụ thể tại từng mốc trên đường biểu diễn (0.15đ).\n- Chú thích rõ thang đo ở phần đầu biểu đồ (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một công ty khảo sát thị phần của 3 đối thủ A, B, C trong 2 năm liên tiếp và thu được bảng số liệu cơ cấu phần trăm:\n- Năm 2023: A ($50\\%$), B ($30\\%$), C ($20\\%$); Tổng dung lượng thị trường: 100 tỷ đồng;\n- Năm 2024: A ($40\\%$), B ($35\\%$), C ($25\\%$); Tổng dung lượng thị trường: 150 tỷ đồng.\na) Thị phần (%) của đối thủ A giảm từ $50\\%$ xuống $40\\%$. Doanh thu tuyệt đối của đối thủ A tăng hay giảm? Tính số tiền cụ thể.\nb) Để thể hiện đồng thời cả thị phần (%) và dung lượng quy mô thị trường (tỷ đồng) qua 2 năm, em hãy đề xuất phương án trực quan hóa tối ưu nhất.",
            "rubric": "a) Tính toán doanh thu đối thủ A:\n- Năm 2023: 50% * 100 = 50 tỷ đồng (0.25đ).\n- Năm 2024: 40% * 150 = 60 tỷ đồng (0.25đ).\n=> Mặc dù thị phần phần trăm giảm nhưng doanh thu tuyệt đối của A vẫn TĂNG 10 tỷ đồng (từ 50 lên 60 tỷ đồng) do quy mô toàn thị trường tăng trưởng mạnh (0.2đ).\nb) Phương án trực quan hóa tối ưu:\n- Vẽ 2 biểu đồ hình quạt tròn cạnh nhau, nhưng diện tích (bán kính) của hình tròn năm 2024 lớn hơn hình tròn năm 2023 theo tỉ lệ căn bậc hai của 150/100 ≈ 1.22 lần bán kính (hoặc biểu đồ cột chồng có chiều cao cột biểu diễn tổng quy mô thị trường) (0.3đ)."
        }
    ]
}
