# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI - BÀI 18: THU THẬP VÀ PHÂN LOẠI DỮ LIỆU (TOÁN 8 - KNTT)
Gồm 3 đề phân hóa:
- Đề 1 (Cơ bản): Nhận biết dữ liệu định tính/định lượng, rời rạc/liên tục, thu thập trực tiếp/gián tiếp, tính hợp lí cơ bản.
- Đề 2 (Khá): Đánh giá tính đại diện của mẫu, thang đo thứ tự, phát hiện sai sót logic, thiết kế phiếu hỏi.
- Đề 3 (Nâng cao): Chọn mẫu phân tầng, xử lí sai số ngẫu nhiên/hệ thống, phát hiện câu hỏi thiên vị (mớm ý), làm sạch dữ liệu.
"""

BAI1_EXAMS = {}

# ==============================================================================
# BÀI 18 - ĐỀ 1: CƠ BẢN (🌱)
# ==============================================================================
BAI1_EXAMS["c5_8_bai1_test1"] = {
    "title": "Toán 8 (KNTT) - Bài 18: Thu thập và phân loại dữ liệu - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Những thông tin thu thập được như số, chữ, hình ảnh,... được gọi chung là:",
            "options": ["Dữ liệu", "Tần số", "Biểu đồ", "Bảng thống kê"],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Phương pháp nào sau đây là phương pháp thu thập dữ liệu trực tiếp?",
            "options": [
                "Lập phiếu hỏi phỏng vấn các bạn trong lớp",
                "Tìm kiếm số liệu dân số trên trang web của Tổng cục Thống kê",
                "Đọc số liệu về nhiệt độ trong sách Địa lí",
                "Lấy số liệu về xuất nhập khẩu từ bản tin thời sự"
            ],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Nhận biết",
            "question": "Dữ liệu nào sau đây là dữ liệu định lượng (dữ liệu là số)?",
            "options": [
                "Chiều cao (tính bằng cm) của các bạn tổ 1",
                "Màu sắc yêu thích của các bạn học sinh",
                "Tên các môn thể thao được yêu thích",
                "Xếp loại học lực của học sinh cuối học kì I"
            ],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Nhận biết",
            "question": "Dữ liệu nào sau đây là dữ liệu định tính KHÔNG THỂ sắp thứ tự?",
            "options": [
                "Quê quán của các học sinh trong lớp",
                "Đánh giá chất lượng dịch vụ (Kém, Trung bình, Tốt, Rất tốt)",
                "Xếp loại rèn luyện (Tốt, Khá, Đạt, Chưa đạt)",
                "Kích cỡ áo đồng phục (S, M, L, XL)"
            ],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Nhận biết",
            "question": "Dữ liệu nào sau đây là dữ liệu định tính CÓ THỂ sắp thứ tự?",
            "options": [
                "Xếp loại học lực (Tốt, Khá, Đạt, Chưa đạt)",
                "Nơi sinh của các thành viên trong gia đình",
                "Tên các câu lạc bộ trong trường",
                "Các loại phương tiện giao thông đến trường"
            ],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Nhận biết",
            "question": "Số liệu nào sau đây là số liệu rời rạc?",
            "options": [
                "Số học sinh tham gia câu lạc bộ bóng rổ",
                "Chiều cao của học sinh lớp 8A",
                "Cân nặng của các bạn trong đội tuyển cầu lông",
                "Thời gian chạy 100m của các vận động viên"
            ],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Nhận biết",
            "question": "Số liệu nào sau đây là số liệu liên tục?",
            "options": [
                "Nhiệt độ không khí tại trạm đo lúc 12 giờ trưa",
                "Số bàn thắng trong một trận đấu bóng đá",
                "Số lượng xe máy bán ra trong một ngày",
                "Số lỗi chính tả trong một bài kiểm tra Ngữ văn"
            ],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Thông hiểu",
            "question": "Bạn An ghi lại điểm kiểm tra môn Toán của 5 bạn: $7; 8.5; 9; 12; 6$. Giá trị nào KHÔNG hợp lí?",
            "options": ["$12$", "$8.5$", "$9$", "$6$"],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Để thu thập dữ liệu về số học sinh bị cận thị của trường THCS gồm 1200 học sinh, cách làm nào sau đây đảm bảo tính đại diện nhất?",
            "options": [
                "Chọn ngẫu nhiên 10 học sinh ở mỗi lớp từ khối 6 đến khối 9",
                "Chỉ khảo sát toàn bộ học sinh lớp 8A",
                "Chỉ khảo sát các bạn học sinh ngồi ở bàn đầu các lớp",
                "Chỉ khảo sát các bạn học sinh trong đội tuyển bơi lội"
            ],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Một nhóm bạn khảo sát tỉ lệ phần trăm yêu thích 4 thể loại nhạc: Nhạc trẻ ($50\\%$), Nhạc cổ điển ($20\\%$), Nhạc rock ($15\\%$), Nhạc trữ tình ($25\\%$). Dữ liệu này không hợp lí vì:",
            "options": [
                "Tổng các tỉ lệ phần trăm vượt quá $100\\%$ ($110\\%$)",
                "Nhạc trẻ có tỉ lệ quá cao",
                "Nhạc rock có tỉ lệ quá thấp",
                "Tất cả các tỉ lệ đều là số chẵn"
            ],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Danh sách tuổi của các thành viên trong câu lạc bộ Cờ vua THCS: $12, 13, 14, 15, 65, 13$. Giá trị nào là giá trị bất thường (outlier)?",
            "options": ["$65$", "$15$", "$12$", "$14$"],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Phương pháp nào sau đây là phương pháp thu thập dữ liệu gián tiếp?",
            "options": [
                "Tra cứu niên giám thống kê trên website chính thức của Tổng cục Thống kê",
                "Đo trực tiếp chiều cao của từng học sinh",
                "Phỏng vấn trực tiếp phụ huynh học sinh",
                "Phát phiếu khảo sát ý kiến tận tay học sinh"
            ],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một giáo viên chủ nhiệm tiến hành khảo sát về môn học yêu thích nhất của 40 học sinh lớp 8A. Kết quả thu được: Toán (14 bạn), Ngữ văn (10 bạn), Tiếng Anh (12 bạn), Khoa học tự nhiên (4 bạn).",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Tổng số học sinh tham gia cuộc khảo sát là 40 học sinh.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Dữ liệu thu được về 'Tên môn học yêu thích nhất' là dữ liệu định tính không thể sắp thứ tự.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Dữ liệu về 'Số học sinh lựa chọn mỗi môn' là số liệu liên tục.", "correct": False },
                { "key": "d", "level": "Vận dụng thấp", "text": "Số học sinh yêu thích môn Toán chiếm đúng $35\\%$ tổng số học sinh cả lớp.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Bạn Bình ghi lại số đo chiều cao (đơn vị: cm) của 8 bạn học sinh nam trong tổ 2: $155; 160; 158; 162; 250; 159; 161; -10$.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Chiều cao của học sinh là dữ liệu định lượng và là số liệu liên tục.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Trong dãy dữ liệu trên có đúng 2 giá trị không hợp lí về chiều cao học sinh lớp 8 là $250$ và $-10$.", "correct": True },
                { "key": "c", "level": "Vận dụng thấp", "text": "Sau khi loại bỏ 2 giá trị không hợp lí, số bạn học sinh có số đo hợp lí là 6 bạn.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Chiều cao trung bình của 6 bạn học sinh có số đo hợp lí lớn hơn $165\\text{ cm}$.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho dãy dữ liệu ghi lại số con trong một số gia đình: $2, 1, 3, 2, 0, 15, 2, 1$. Có bao nhiêu giá trị không hợp lí (bất thường) trong dãy?",
            "answer": "1"
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Bạn Cúc đếm số lỗi chính tả trong 5 bài kiểm tra của mình: $1, 0, 2, 0, 2$. Tổng số lỗi chính tả trong 5 bài là bao nhiêu?",
            "answer": "5"
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Trong 4 dữ liệu sau: (1) Cân nặng (kg), (2) Điểm thi, (3) Chiều cao (m), (4) Số xe đạp trong bãi xe; có bao nhiêu dữ liệu là số liệu liên tục?",
            "answer": "2"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Một lớp có 45 học sinh. Khi khảo sát môn thể thao yêu thích: Bóng đá có 20 bạn, Cầu lông có 15 bạn, Bơi lội có 6 bạn, còn lại thích Bóng bàn. Hỏi có bao nhiêu bạn thích môn Bóng bàn?",
            "answer": "4"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thầy giáo ghi lại kết quả khảo sát thông tin của 30 học sinh một lớp gồm:\n- Họ và tên học sinh;\n- Điểm bài kiểm tra 15 phút (thang điểm 10);\n- Đánh giá mức độ yêu thích học Toán (Rất thích, Thích, Bình thường, Không thích);\n- Thời gian tự học ở nhà mỗi ngày (tính theo giờ).\nEm hãy phân loại các thông tin trên thành dữ liệu định tính và dữ liệu định lượng. Trong các dữ liệu định tính, dữ liệu nào có thể sắp thứ tự?",
            "rubric": "- Dữ liệu định tính: Họ và tên học sinh; Mức độ yêu thích học Toán (0.25đ).\n- Dữ liệu định lượng: Điểm bài kiểm tra 15 phút; Thời gian tự học ở nhà mỗi ngày (0.25đ).\n- Dữ liệu định tính có thể sắp thứ tự là: Mức độ yêu thích học Toán (Rất thích > Thích > Bình thường > Không thích) (0.25đ).\n- Dữ liệu định tính không thể sắp thứ tự là: Họ và tên học sinh (0.25đ)."
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Để tìm hiểu về mức độ sử dụng Internet của học sinh trường THCS Chu Văn An (gồm 1500 học sinh), bạn Lan đã phỏng vấn 50 bạn học sinh trong Câu lạc bộ Tin học của trường.\na) Em hãy cho biết bạn Lan đã thu thập dữ liệu bằng phương pháp nào?\nb) Mẫu dữ liệu thu được của bạn Lan có đảm bảo tính đại diện cho toàn bộ học sinh trường THCS Chu Văn An hay không? Vì sao?",
            "rubric": "a) Bạn Lan đã thu thập dữ liệu bằng phương pháp trực tiếp (phỏng vấn trực tiếp các bạn học sinh) (0.5đ).\nb) Mẫu dữ liệu trên KHÔNG đảm bảo tính đại diện cho toàn bộ học sinh trường (0.25đ), vì:\n+ Các học sinh trong Câu lạc bộ Tin học thường có sở thích và tần suất sử dụng Internet cao hơn mức bình thường của học sinh toàn trường (0.15đ).\n+ Cỡ mẫu chỉ lấy trong một câu lạc bộ, không bao quát được các học sinh thuộc các khối lớp khác nhau và sở thích khác nhau (0.1đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một nhân viên điều tra ghi lại số tiền chi tiêu cho ăn sáng (nghìn đồng) của 6 bạn học sinh trong một tuần như sau: $15; 20; 25; -5; 30; 300$.\na) Chỉ ra các giá trị không hợp lí trong dãy số liệu trên và giải thích vì sao.\nb) Sau khi bỏ đi các giá trị không hợp lí, hãy tính số tiền chi tiêu trung bình cho bữa sáng của các bạn học sinh còn lại.",
            "rubric": "a) Các giá trị không hợp lí là:\n- Giá trị $-5$: Số tiền chi tiêu không thể nhận giá trị âm (0.25đ).\n- Giá trị $300$: $300$ nghìn đồng cho một bữa ăn sáng của học sinh là quá lớn và bất thường so với mức phổ biến (15 - 30 nghìn đồng) (0.25đ).\nb) Các giá trị hợp lí còn lại là: $15; 20; 25; 30$ (0.25đ).\nSố tiền chi tiêu trung bình là: (15 + 20 + 25 + 30) / 4 = 90 / 4 = 22.5 (nghìn đồng) (0.25đ)."
        }
    ]
}

# ==============================================================================
# BÀI 18 - ĐỀ 2: KHÁ (🌿)
# ==============================================================================
BAI1_EXAMS["c5_8_bai1_test2"] = {
    "title": "Toán 8 (KNTT) - Bài 18: Thu thập và phân loại dữ liệu - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {
            "id": 1,
            "level": "Nhận biết",
            "question": "Thang đo nào sau đây thuộc loại dữ liệu định tính có thể sắp thứ tự?",
            "options": [
                "Thang đo mức độ hài lòng: Rất hài lòng, Hài lòng, Không hài lòng",
                "Thang đo màu sắc: Xanh, Đỏ, Vàng, Tím",
                "Thang đo giới tính: Nam, Nữ",
                "Thang đo nơi cư trú: Nông thôn, Thành thị"
            ],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây là ĐÚNG khi nói về dữ liệu liên tục?",
            "options": [
                "Có thể nhận mọi giá trị trong một khoảng số thực nhất định",
                "Chỉ có thể nhận các giá trị nguyên không âm",
                "Không bao giờ đo đạc được bằng dụng cụ đo",
                "Luôn luôn đếm được chính xác từng đơn vị"
            ],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Để đánh giá chất lượng dạy học môn Toán của một trường, cách lấy mẫu nào sau đây khách quan nhất?",
            "options": [
                "Chọn ngẫu nhiên theo danh sách điểm danh 15 học sinh ở mỗi lớp trong toàn trường",
                "Chỉ lấy mẫu các học sinh đạt học lực Tốt môn Toán",
                "Chỉ lấy mẫu học sinh tham gia đội tuyển học sinh giỏi",
                "Lấy mẫu ngẫu nhiên các học sinh có mặt tại căng tin vào giờ ra chơi"
            ],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Thông hiểu",
            "question": "Câu hỏi khảo sát nào sau đây là câu hỏi KHÔNG THIÊN VỊ (không mớm ý người trả lời)?",
            "options": [
                "Bạn đánh giá như thế nào về độ sạch sẽ của nhà vệ sinh trường học?",
                "Có phải bạn rất thích các món ăn ở căng tin trường không?",
                "Bạn có đồng ý rằng bài tập về nhà môn Toán quá nhiều không?",
                "Không phải bạn thấy việc tập thể dục buổi sáng rất mệt mỏi sao?"
            ],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Thông hiểu",
            "question": "Dãy số liệu nào sau đây là số liệu rời rạc hoàn toàn hợp lí về số xe máy một hộ gia đình sở hữu?",
            "options": ["$1, 2, 0, 3, 2, 1$", "$1, 2.5, 0, 3, 2$", "$-1, 2, 0, 4, 1$", "$1, 2, 0, 50, 2$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Thông hiểu",
            "question": "Một bạn học sinh lập bảng hỏi phỏng vấn: 'Bạn dùng bao nhiêu giờ mỗi ngày để chơi game?'. Dữ liệu thu được thuộc loại nào?",
            "options": [
                "Dữ liệu định lượng, số liệu liên tục",
                "Dữ liệu định lượng, số liệu rời rạc",
                "Dữ liệu định tính có thể sắp thứ tự",
                "Dữ liệu định tính không thể sắp thứ tự"
            ],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Thông hiểu",
            "question": "Bạn Minh thực hiện một cuộc khảo sát bằng cách gửi link Google Form lên nhóm bạn thân gồm 20 người. Nhận định nào đúng?",
            "options": [
                "Mẫu điều tra có tính đại diện thấp và dễ bị thiên vị",
                "Mẫu điều tra có tính đại diện rất cao cho toàn bộ học sinh",
                "Đây là phương pháp thu thập gián tiếp từ nguồn thứ cấp",
                "Cỡ mẫu đủ lớn để kết luận cho toàn trường"
            ],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Thông hiểu",
            "question": "Bảng khảo sát ý kiến về đồng phục trường có kết quả: Đồng ý ($65\\%$), Không đồng ý ($30\\%$), Ý kiến khác ($10\\%$). Lỗi sai ở đây là:",
            "options": [
                "Tổng phần trăm bằng $105\\%$, lớn hơn $100\\%$",
                "Tỉ lệ Không đồng ý quá thấp",
                "Số lượng người tham gia khảo sát không chia hết cho 10",
                "Phương pháp thu thập trực tiếp bị sai quy chuẩn"
            ],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng thấp",
            "question": "Một trường có 800 học sinh. Để chọn mẫu 80 học sinh theo phương pháp phân tầng tỉ lệ theo 4 khối lớp: Khối 6 ($30\\%$), Khối 7 ($25\\%$), Khối 8 ($25\\%$), Khối 9 ($20\\%$). Số học sinh khối 8 cần chọn là:",
            "options": ["$20$ học sinh", "$24$ học sinh", "$16$ học sinh", "$25$ học sinh"],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng thấp",
            "question": "Số đo đường kính thân cây (cm) của 6 cây xà cừ cổ thụ đo được là: $80; 85; 82; 84; 86; 83$. Dữ liệu này là:",
            "options": [
                "Số liệu liên tục, có độ phân tán nhỏ và hợp lí",
                "Số liệu rời rạc, có nhiều giá trị ngoại lai",
                "Dữ liệu định tính có thể sắp thứ tự",
                "Dữ liệu không đáng tin cậy vì không có số lẻ thập phân"
            ],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng thấp",
            "question": "Khi kiểm tra tính hợp lí của bảng dữ liệu điều tra dân số một xã, chỉ tiêu nào sau đây chắc chắn BẤT HỢP LÍ?",
            "options": [
                "Số nhân khẩu của một hộ gia đình là $-2$ người",
                "Tỉ lệ tăng dân số tự nhiên là $1.2\\%$",
                "Số người trong độ tuổi lao động chiếm $65\\%$",
                "Số phụ nữ nhiều hơn số nam giới 150 người"
            ],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng thấp",
            "question": "Một nhà nghiên cứu muốn tìm hiểu về thói quen ăn sáng của học sinh Hà Nội. Cách thu thập dữ liệu nào cho kết quả đáng tin cậy nhất?",
            "options": [
                "Chọn ngẫu nhiên 5 trường ở các quận nội thành và 5 trường ở các huyện ngoại thành, mỗi trường chọn ngẫu nhiên 100 học sinh",
                "Phỏng vấn 1000 học sinh tại cổng trường THCS Giảng Võ vào sáng thứ Hai",
                "Gửi phiếu hỏi online lên diễn đàn Facebook dành cho học sinh yêu thích Toán",
                "Khảo sát toàn bộ học sinh của một trường quốc tế tại Hà Nội"
            ],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một nhà trường tổ chức khảo sát về việc tự học ở nhà của 200 học sinh khối 8. Phiếu hỏi thu thập 3 thông tin: (1) Thời gian tự học trung bình mỗi tối (tính bằng phút); (2) Không gian tự học (Phòng riêng, Bàn học chung, Khác); (3) Mức độ tập trung (Rất tập trung, Khá tập trung, Thỉnh thoảng mất tập trung, Hay mất tập trung).",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Thông tin (1) là số liệu liên tục.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Thông tin (2) là dữ liệu định tính có thể sắp thứ tự.", "correct": False },
                { "key": "c", "level": "Vận dụng thấp", "text": "Thông tin (3) là dữ liệu định tính có thể sắp thứ tự.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Nếu có học sinh điền thời gian tự học là 600 phút mỗi tối (10 tiếng) thì đây là giá trị ngoại lai bất thường cần kiểm tra lại.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Để khảo sát sự hài lòng của phụ huynh đối với dịch vụ bán trú, nhà trường phát 500 phiếu khảo sát và thu về 480 phiếu hợp lệ. Thang đo gồm 4 mức: Rất hài lòng, Hài lòng, Chưa hài lòng, Rất không hài lòng.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Tỉ lệ phản hồi của cuộc khảo sát đạt $96\\%$.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Dữ liệu thu được từ phiếu khảo sát là dữ liệu định tính không thể sắp thứ tự.", "correct": False },
                { "key": "c", "level": "Vận dụng thấp", "text": "Nếu có 360 phụ huynh chọn 'Rất hài lòng' hoặc 'Hài lòng' thì tỉ lệ hài lòng chung đạt $75\\%$.", "correct": True },
                { "key": "d", "level": "Vận dụng thấp", "text": "Để tăng độ tin cậy, nhà trường chỉ nên phát phiếu cho các phụ huynh trong Ban đại diện phụ huynh học sinh.", "correct": False }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Một nhóm nghiên cứu khảo sát 120 học sinh. Có 78 bạn trả lời thích đọc sách khoa học. Tính tỉ số phần trăm học sinh thích đọc sách khoa học trong nhóm khảo sát.",
            "answer": "65"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một khối lớp 8 có 240 học sinh (gồm 132 nữ và 108 nam). Người ta muốn chọn mẫu 40 học sinh theo tỉ lệ giới tính. Số học sinh nữ cần chọn vào mẫu là bao nhiêu?",
            "answer": "22"
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho dãy dữ liệu nhiệt độ trung bình ngày ($^\\circ\\text{C}$) trong 7 ngày: $25, 26, 27, 26, 28, 48, 25$. Có bao nhiêu giá trị ngoại lai (bất thường) trong dãy?",
            "answer": "1"
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Bảng khảo sát 50 người về số lần tập thể dục trong tuần: 0 lần: 5 người; 1-2 lần: 15 người; 3-4 lần: 20 người; trên 4 lần: $x$ người. Tìm giá trị của $x$.",
            "answer": "10"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Em hãy thiết kế một phiếu khảo sát ngắn gồm đúng 3 câu hỏi để tìm hiểu về 'Thói quen đọc sách của học sinh lớp 8':\n- Câu 1: Thu thập dữ liệu định lượng rời rạc.\n- Câu 2: Thu thập dữ liệu định lượng liên tục.\n- Câu 3: Thu thập dữ liệu định tính có thể sắp thứ tự.\nGhi rõ câu hỏi và phương án trả lời dự kiến.",
            "rubric": "- Câu 1 (Số liệu rời rạc): Ví dụ: 'Bạn đã đọc bao nhiêu cuốn sách trong tháng vừa qua?' (Các phương án: 0 cuốn; 1 cuốn; 2 cuốn; Từ 3 cuốn trở lên) (0.35đ).\n- Câu 2 (Số liệu liên tục): Ví dụ: 'Trung bình mỗi ngày bạn dành bao nhiêu thời gian để đọc sách?' (Đơn vị: giờ/phút, nhận giá trị liên tục) (0.35đ).\n- Câu 3 (Định tính có thể sắp thứ tự): Ví dụ: 'Bạn đánh giá mức độ yêu thích đọc sách của mình như thế nào?' (Rất thích > Thích > Bình thường > Không thích) (0.3đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Để khảo sát mức độ hài lòng về chất lượng bữa ăn căng tin trường học, ban giám hiệu đưa ra 2 phương án chọn mẫu:\n- Phương án A: Chọn 100 học sinh ngẫu nhiên xếp hàng mua đồ tại căng tin vào giờ ra chơi sáng thứ Ba.\n- Phương án B: Lấy danh sách toàn trường, chọn ngẫu nhiên mỗi lớp 3 học sinh (không phân biệt có ăn căng tin hay không).\nEm hãy so sánh ưu điểm, nhược điểm của hai phương án trên và đề xuất cách lấy mẫu tối ưu nhất.",
            "rubric": "- Phương án A: Ưu điểm là thu thập được ý kiến của những học sinh trực tiếp trải nghiệm; Nhược điểm: Dễ bị thiên vị vì chỉ khảo sát những người đã thích hoặc thường xuyên ăn ở căng tin, bỏ qua nhóm học sinh không ăn ở căng tin vì lý do chất lượng (0.35đ).\n- Phương án B: Ưu điểm là tính bao quát cao; Nhược điểm: Sẽ có những học sinh chưa bao giờ ăn ở căng tin nên không thể đưa ra đánh giá chính xác (0.35đ).\n- Đề xuất tối ưu: Lập danh sách toàn bộ học sinh từng sử dụng căng tin ít nhất 1 lần trong tháng qua, sau đó chọn ngẫu nhiên 100 học sinh từ danh sách đó (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một nhóm học sinh tiến hành đo thời gian hoàn thành cự li chạy 100m (tính bằng giây) của 8 bạn và ghi lại: $14.2; 15.1; 13.8; 14.5; 62.0; 14.8; 15.0; -2.5$.\na) Xác định các dữ liệu không hợp lí và nêu rõ lí do.\nb) Sau khi làm sạch dữ liệu bằng cách loại bỏ các giá trị không hợp lí, tính thời gian chạy trung bình của các bạn còn lại (làm tròn đến chữ số thập phân thứ hai).",
            "rubric": "a) Các giá trị không hợp lí:\n- Giá trị $-2.5$: Thời gian không thể là số âm (0.25đ).\n- Giá trị $62.0$: Thời gian chạy 100m là 62 giây là quá chậm và bất thường đối với học sinh trung học (thường từ 13 - 16 giây), có thể do người bấm giờ ghi nhầm hoặc học sinh đi bộ/gặp sự cố (0.25đ).\nb) Tập dữ liệu hợp lí gồm 6 giá trị: $14.2; 15.1; 13.8; 14.5; 14.8; 15.0$ (0.25đ).\nThời gian chạy trung bình: (14.2 + 15.1 + 13.8 + 14.5 + 14.8 + 15.0) / 6 = 87.4 / 6 ≈ 14.57 (giây) (0.25đ)."
        }
    ]
}

# ==============================================================================
# BÀI 18 - ĐỀ 3: NÂNG CAO (🚀)
# ==============================================================================
BAI1_EXAMS["c5_8_bai1_test3"] = {
    "title": "Toán 8 (KNTT) - Bài 18: Thu thập và phân loại dữ liệu - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Trong thống kê học, phương pháp chọn mẫu phân tầng (Stratified Sampling) được áp dụng hiệu quả nhất khi nào?",
            "options": [
                "Khi tổng thể gồm nhiều nhóm con (tầng) có đặc tính khác biệt rõ rệt",
                "Khi mọi phần tử trong tổng thể hoàn toàn đồng nhất",
                "Khi kích thước của tổng thể là vô hạn và không thể kiểm đếm",
                "Khi chỉ cần thu thập ý kiến của một nhóm người tình nguyện"
            ],
            "correct": 0
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Một bài báo giật tít: '90% người tiêu dùng khẳng định nước ngọt X làm tăng trí nhớ'. Đọc kĩ bài viết thấy khảo sát chỉ thực hiện trên 20 nhân viên của công ty sản xuất nước ngọt X. Sai phạm nghiêm trọng nhất của khảo sát này là:",
            "options": [
                "Cỡ mẫu quá nhỏ và mẫu bị xung đột lợi ích (thiên vị nghiêm trọng)",
                "Phương pháp thu thập dữ liệu gián tiếp không qua công chứng",
                "Dữ liệu thu được là dữ liệu định tính không sắp thứ tự",
                "Không công bố biểu đồ hình quạt tròn đi kèm"
            ],
            "correct": 0
        },
        {
            "id": 3,
            "level": "Thông hiểu",
            "question": "Câu hỏi khảo sát nào sau đây vi phạm nguyên tắc khách quan (câu hỏi mớm ý/định hướng)?",
            "options": [
                "Bạn có nghĩ rằng mức học phí hiện nay là quá đắt đỏ so với chất lượng không?",
                "Bạn đánh giá chất lượng cơ sở vật chất của trường ở mức độ nào?",
                "Trung bình một tuần bạn đến thư viện bao nhiêu lần?",
                "Bạn thường chọn phương tiện nào để đến trường?"
            ],
            "correct": 0
        },
        {
            "id": 4,
            "level": "Vận dụng thấp",
            "question": "Một cuộc điều tra thu thập được 10 số liệu có trung bình cộng là $\\bar{x} = 20$. Sau đó phát hiện có một số liệu ghi nhầm từ $15$ thành $25$. Giá trị trung bình cộng thực sự sau khi sửa lại là:",
            "options": ["$19$", "$19.5$", "$20.5$", "$21$"],
            "correct": 0
        },
        {
            "id": 5,
            "level": "Vận dụng thấp",
            "question": "Trong chọn mẫu phân tầng tỉ lệ, trường THCS có 1000 học sinh gồm: Khối 6 (300 em), Khối 7 (280 em), Khối 8 (220 em), Khối 9 (200 em). Nếu chọn mẫu 150 học sinh thì số học sinh khối 8 và khối 9 được chọn lần lượt là:",
            "options": ["$33$ và $30$", "$35$ và $28$", "$30$ và $33$", "$36$ và $27$"],
            "correct": 0
        },
        {
            "id": 6,
            "level": "Vận dụng thấp",
            "question": "Cho dãy dữ liệu xếp thứ bậc điểm đánh giá từ 1 đến 5 sao: $5, 4, 5, 5, 1, 4, 5, 4$. Giá trị $1$ sao trong tập dữ liệu này có thể được xem là:",
            "options": [
                "Giá trị ngoại lai (outlier) cần xem xét nguyên nhân riêng biệt",
                "Giá trị lỗi không hợp lí buộc phải xóa bỏ ngay lập tức",
                "Giá trị trung bình của toàn bộ tập dữ liệu",
                "Dữ liệu định lượng liên tục bị làm tròn sai"
            ],
            "correct": 0
        },
        {
            "id": 7,
            "level": "Vận dụng thấp",
            "question": "Khi nghiên cứu mối liên hệ giữa 'Thời gian sử dụng mạng xã hội' và 'Kết quả học tập', hai biến số này thuộc loại dữ liệu nào?",
            "options": [
                "Thời gian sử dụng: định lượng liên tục; Kết quả học tập: định lượng hoặc định tính có sắp thứ tự",
                "Cả hai đều là dữ liệu định tính không thể sắp thứ tự",
                "Thời gian sử dụng: định tính; Kết quả học tập: định lượng rời rạc",
                "Cả hai đều là dữ liệu rời rạc chỉ nhận giá trị nguyên"
            ],
            "correct": 0
        },
        {
            "id": 8,
            "level": "Vận dụng cao",
            "question": "Một nhà nghiên cứu muốn khảo sát ý kiến học sinh về việc cấm điện thoại trong trường học. Để tránh sai lệch phản hồi do tâm lí e ngại, giải pháp nào sau đây là tối ưu?",
            "options": [
                "Lập phiếu khảo sát trực tuyến ẩn danh và bảo mật danh tính",
                "Để giáo viên chủ nhiệm phỏng vấn từng học sinh trực tiếp",
                "Yêu cầu học sinh giơ tay biểu quyết công khai trước lớp",
                "Gửi phiếu khảo sát về cho phụ huynh ký xác nhận"
            ],
            "correct": 0
        },
        {
            "id": 9,
            "level": "Vận dụng cao",
            "question": "Bảng khảo sát thời gian sử dụng máy tính của 5 bạn học sinh (giờ/ngày): $1.5; 2.0; 2.5; 3.0; 16.0$. Nếu sử dụng giá trị trung bình cộng để đại diện cho cả nhóm thì hạn chế lớn nhất là:",
            "options": [
                "Bị kéo lệch mạnh bởi giá trị ngoại lai $16.0$, không phản ánh đúng đa số",
                "Trung bình cộng không thể tính được đối với số thập phân",
                "Không biểu diễn được trên biểu đồ cột",
                "Giá trị trung bình luôn nhỏ hơn giá trị nhỏ nhất"
            ],
            "correct": 0
        },
        {
            "id": 10,
            "level": "Vận dụng cao",
            "question": "Khi mã hóa dữ liệu định tính 'Mức độ hiểu bài' (1: Rất hiểu, 2: Hiểu, 3: Mơ hồ, 4: Không hiểu) thành các con số 1, 2, 3, 4, ta KHÔNG ĐƯỢC phép thực hiện phép toán nào sau đây một cách thuần túy số học?",
            "options": [
                "Kết luận mức 4 hiểu bài gấp 4 lần mức 1",
                "Đếm tần số số lượng học sinh ở từng mức",
                "Tính tỉ lệ phần trăm học sinh ở từng mức",
                "Sắp xếp thứ tự các mức từ tốt nhất đến kém nhất"
            ],
            "correct": 0
        },
        {
            "id": 11,
            "level": "Vận dụng cao",
            "question": "Khái niệm 'Sai số hệ thống' (Systematic error) trong thu thập dữ liệu xảy ra khi nào?",
            "options": [
                "Dụng cụ đo bị lệch chuẩn ban đầu hoặc phương pháp chọn mẫu có định kiến cố hữu",
                "Do người điều tra vô tình ghi nhầm một con số ngẫu nhiên",
                "Do thời tiết thay đổi bất chợt trong lúc quan sát",
                "Do học sinh làm tròn kết quả phép tính"
            ],
            "correct": 0
        },
        {
            "id": 12,
            "level": "Vận dụng cao",
            "question": "Một mẫu điều tra đại diện cần thỏa mãn đồng thời hai yếu tố cốt lõi nào sau đây?",
            "options": [
                "Kích thước mẫu đủ lớn và phương pháp chọn mẫu ngẫu nhiên không thiên vị",
                "Chi phí thu thập thấp nhất và thời gian thu thập nhanh nhất",
                "Chỉ khảo sát các cá nhân có trình độ học vấn cao",
                "Số lượng câu hỏi trong phiếu hỏi phải trên 50 câu"
            ],
            "correct": 0
        }
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một đề tài nghiên cứu khoa học học sinh THCS khảo sát về 'Ảnh hưởng của thời gian ngủ đến khả năng tập trung trong giờ học'. Nhóm nghiên cứu tiến hành trên 150 học sinh khối 8.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Biến số 'Thời gian ngủ mỗi đêm' là dữ liệu định lượng liên tục.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Biến số 'Khả năng tập trung' đo bằng trắc nghiệm thang điểm 10 là dữ liệu định lượng.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Nếu nhóm nghiên cứu chỉ chọn 150 học sinh trong các lớp chọn mũi nhọn thì kết quả nghiên cứu vẫn đảm bảo tính khái quát hóa cho toàn bộ học sinh THCS.", "correct": False },
                { "key": "d", "level": "Vận dụng cao", "text": "Khi phát hiện một bạn ghi thời gian ngủ là 25 giờ/ngày, đây là lỗi phi lí học thuật cần loại bỏ trước khi phân tích.", "correct": True }
            ]
        },
        {
            "id": 2,
            "stem": "Một trang tin tức mạng thực hiện bình chọn trực tuyến: 'Bạn có ủng hộ bỏ kì thi tuyển sinh lớp 10 công lập không?'. Sau 1 tuần có 10.000 lượt vote, trong đó $85\\%$ chọn 'Ủng hộ'.",
            "statements": [
                { "key": "a", "level": "Thông hiểu", "text": "Phương pháp thu thập dữ liệu ở đây là thu thập trực tiếp thông qua bình chọn trực tuyến tự nguyện.", "correct": True },
                { "key": "b", "level": "Thông hiểu", "text": "Dữ liệu thu được là dữ liệu định tính.", "correct": True },
                { "key": "c", "level": "Vận dụng cao", "text": "Vì cỡ mẫu lên tới 10.000 lượt tham gia nên kết quả này phản ánh chính xác quan điểm của toàn bộ phụ huynh và học sinh cả nước.", "correct": False },
                { "key": "d", "level": "Vận dụng cao", "text": "Mẫu tự chọn trực tuyến thường bị sai lệch lớn do chỉ thu hút những người có cảm xúc mạnh về vấn đề tham gia bỏ phiếu.", "correct": True }
            ]
        }
    ],
    "part3": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Trường THCS A có 1200 học sinh. Nhà trường muốn chọn một mẫu 120 học sinh phân tầng theo 4 khối lớp: Khối 6 có 360 em; Khối 7 có 320 em; Khối 8 có 280 em; Khối 9 có 240 em. Số học sinh khối 8 cần chọn vào mẫu là bao nhiêu?",
            "answer": "28"
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một dãy 8 số liệu có giá trị trung bình bằng 25. Một bạn nhập máy tính vô tình nhập thiếu một số liệu nên trung bình của 7 số liệu còn lại là 24. Hỏi số liệu bị nhập thiếu có giá trị bằng bao nhiêu?",
            "answer": "32"
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Trong một cuộc điều tra, người ta phát hiện trong 5 câu hỏi có $k$ câu hỏi vi phạm tính khách quan (chứa từ ngữ định hướng cảm xúc người trả lời). Biết rằng tỉ lệ câu hỏi khách quan đạt chuẩn là $60\\%$. Tìm giá trị của $k$.",
            "answer": "2"
        },
        {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Dãy số liệu gồm 5 giá trị: $12, 15, 18, 20, x$. Biết rằng trung bình cộng của dãy là 17 và sau khi thay $x$ bằng giá trị hợp chuẩn thì độ phân tán dữ liệu đạt chuẩn. Tìm giá trị của $x$.",
            "answer": "20"
        }
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Một công ty đồ uống tiến hành khảo sát người tiêu dùng với câu hỏi: 'Nước trái cây tự nhiên của công ty chúng tôi vừa thơm ngon lại vừa giàu vitamin C, bạn có đồng ý rằng sản phẩm này rất tốt cho sức khỏe không?'.\na) Em hãy chỉ ra điểm sai lầm nghiêm trọng trong cách đặt câu hỏi này theo tiêu chuẩn thống kê học.\nb) Hãy viết lại câu hỏi trên để đảm bảo tính khách quan, trung lập và không mớm ý người trả lời.",
            "rubric": "a) Điểm sai lầm nghiêm trọng:\n- Câu hỏi chứa từ ngữ khen ngợi, mớm ý và định hướng trực tiếp cảm xúc người trả lời ('vừa thơm ngon lại vừa giàu vitamin C', 'rất tốt cho sức khỏe') (0.25đ).\n- Cấu trúc câu hỏi dạng 'Bạn có đồng ý rằng...' gây áp lực tâm lí khiến người trả lời có xu hướng chọn đồng ý (hiệu ứng acquiescence bias) (0.25đ).\nb) Viết lại câu hỏi đạt chuẩn khách quan:\n- Câu hỏi: 'Bạn đánh giá như thế nào về tác động của sản phẩm nước trái cây này đối với sức khỏe?' (0.25đ).\n- Các phương án trả lời: (1) Rất tốt; (2) Tốt; (3) Bình thường; (4) Không tốt; (5) Hoàn toàn không tốt (0.25đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Để đánh giá thực trạng thể lực của học sinh trường THCS Lam Sơn gồm 1600 học sinh (Khối 6: 480 học sinh, Khối 7: 400 học sinh, Khối 8: 400 học sinh, Khối 9: 320 học sinh).\na) Em hãy lập kế hoạch chọn một mẫu gồm 80 học sinh bằng phương pháp chọn mẫu phân tầng tỉ lệ theo khối lớp.\nb) Trình bày các bước cụ thể để chọn ngẫu nhiên các học sinh trong từng khối nhằm đảm bảo tính khách quan cao nhất.",
            "rubric": "a) Tính toán số lượng mẫu theo từng khối:\n- Khối 6: (480 / 1600) * 80 = 24 học sinh (0.15đ).\n- Khối 7: (400 / 1600) * 80 = 20 học sinh (0.15đ).\n- Khối 8: (400 / 1600) * 80 = 20 học sinh (0.1đ).\n- Khối 9: (320 / 1600) * 80 = 16 học sinh (0.1đ).\nTổng số: 24 + 20 + 20 + 16 = 80 học sinh.\nb) Các bước chọn ngẫu nhiên trong từng khối:\n- Bước 1: Lập danh sách mã số học sinh toàn khối từ 1 đến N (ví dụ Khối 6 từ 1 đến 480) (0.15đ).\n- Bước 2: Sử dụng hàm sinh số ngẫu nhiên (hoặc bốc thăm ngẫu nhiên) để chọn ra đủ số lượng học sinh quy định cho từng khối (ví dụ 24 số ngẫu nhiên không trùng nhau cho Khối 6) (0.2đ).\n- Bước 3: Liên hệ các học sinh trúng số ngẫu nhiên để tiến hành kiểm tra đo đạc chỉ số thể lực (0.15đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một nhà phân tích dữ liệu nhận được bảng ghi lại điểm số bài thi chuẩn hóa của một lớp học 10 bạn như sau: $8.0; 7.5; 8.5; 9.0; 0.5; 8.0; 7.0; 8.5; 9.5; 18.0$.\na) Chỉ ra giá trị sai lệch logic và giá trị nghi ngờ là ngoại lai trong tập số liệu trên.\nb) Sau khi xác minh, biết rằng điểm thi theo thang 10 nên giá trị $18.0$ là do gõ thừa số 1 (thực tế là $8.0$), còn điểm $0.5$ là của một học sinh bị ốm phải bỏ thi giữa chừng. Hãy tính điểm trung bình chuẩn mực của lớp trong điều kiện bình thường (loại trừ trường hợp bất khả kháng $0.5$).",
            "rubric": "a) Nhận diện dữ liệu bất thường:\n- Giá trị $18.0$ là giá trị sai lệch logic vì thang điểm kiểm tra tối đa là 10 (0.25đ).\n- Giá trị $0.5$ là giá trị ngoại lai cách biệt quá lớn so với phân bố chung của cả lớp (tập trung từ 7.0 đến 9.5) (0.25đ).\nb) Xử lí và tính toán:\n- Hiệu chỉnh $18.0$ thành $8.0$ (0.15đ).\n- Loại bỏ giá trị bất khả kháng $0.5$, tập dữ liệu còn lại gồm 9 bạn: $8.0; 7.5; 8.5; 9.0; 8.0; 7.0; 8.5; 9.5; 8.0$ (0.15đ).\n- Tổng điểm của 9 bạn: 8.0*3 + 7.5 + 8.5*2 + 9.0 + 7.0 + 9.5 = 24.0 + 7.5 + 17.0 + 9.0 + 7.0 + 9.5 = 74.0 (0.1đ).\n- Điểm trung bình: 74.0 / 9 ≈ 8.22 điểm (0.1đ)."
        }
    ]
}
