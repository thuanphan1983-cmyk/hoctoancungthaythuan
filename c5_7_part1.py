# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG V (PHẦN 1)
Bao gồm:
- Bài 17: Thu thập và phân loại dữ liệu (3 đề: Cơ bản, Khá, Nâng cao)
- Bài 18: Biểu đồ hình quạt tròn (3 đề: Cơ bản, Khá, Nâng cao)
Chuẩn ma trận Bộ GD&ĐT 2025: 12 TN + 2 Đ/S (8 ý) + 4 TLN + 3 TL. Tổng 10.0 điểm.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

EXAMS_PART1 = {}

# =====================================================================
# BÀI 17: THU THẬP VÀ PHÂN LOẠI DỮ LIỆU
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c5_7_bai1_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 17: Thu thập và phân loại dữ liệu - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Phương pháp nào sau đây là phương pháp thu thập dữ liệu trực tiếp?", "options": ["Quan sát hoặc làm thí nghiệm, lập phiếu hỏi", "Tìm kiếm trên mạng Internet", "Đọc trong sách tham khảo", "Tra cứu trên niên giám thống kê"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Dữ liệu nào sau đây là dữ liệu số (số liệu)?", "options": ["Chiều cao của các học sinh trong lớp (cm)", "Tên các loài hoa yêu thích", "Xếp loại học lực (Tốt, Khá, Đạt)", "Nơi sinh của các bạn học sinh"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Dữ liệu nào sau đây không phải là số liệu (dữ liệu định tính)?", "options": ["Màu sắc yêu thích của các bạn trong tổ", "Số học sinh giỏi của từng lớp", "Điểm kiểm tra môn Toán", "Nhiệt độ trung bình các ngày trong tuần"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Dữ liệu định tính nào sau đây có thể so sánh được (thứ bậc)?", "options": ["Mức độ hài lòng của khách hàng: Rất hài lòng, Hài lòng, Không hài lòng", "Màu mắt: Đen, Nâu, Xanh", "Môn thể thao yêu thích: Bóng đá, Bơi, Cầu lông", "Tên các quận, huyện của Hà Nội"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Để thu thập dữ liệu về điểm kiểm tra môn Toán học kì I của các bạn học sinh lớp 7A, bạn lớp trưởng nên thu thập từ nguồn nào?", "options": ["Sổ điểm hoặc bảng điểm của giáo viên dạy Toán", "Hỏi các bạn trong tổ của mình", "Tìm kiếm trên mạng Internet", "Hỏi bác bảo vệ của trường"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Dãy dữ liệu nào sau đây gồm các dữ liệu hợp lí về điểm thi môn Toán thang điểm 10?", "options": ["$8; 9; 7{,}5; 10; 6$", "$8; 12; 7; -2; 9$", "$9; 10; A; B; 8$", "$7; 8; 15; 6; 7$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho dãy dữ liệu về năm sinh của học sinh lớp 7: $2011, 2012, 1995, 2012, 2011$. Giá trị nào là không hợp lí?", "options": ["$1995$", "$2011$", "$2012$", "Không có giá trị nào"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Bảng khảo sát về sở thích đọc sách của học sinh có các mức: Không thích, Bình thường, Thích, Rất thích. Đây là loại dữ liệu:", "options": ["Dữ liệu định tính có thể sắp xếp thứ bậc", "Dữ liệu định tính không thể sắp xếp thứ bậc", "Dữ liệu số liên tục", "Dữ liệu số rời rạc"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Dãy dữ liệu về thân nhiệt của một bệnh nhân (độ C) lúc 8h sáng: $36{,}8; 37{,}0; 37{,}2; 45{,}5$. Giá trị bất thường trong dãy là:", "options": ["$45{,}5$", "$37{,}0$", "$36{,}8$", "$37{,}2$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Để tìm hiểu về số lượng xe máy của mỗi hộ gia đình tại một khu phố, loại dữ liệu thu thập được là:", "options": ["Dữ liệu số", "Dữ liệu định tính", "Dữ liệu hình ảnh", "Dữ liệu âm thanh"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Một tổ có 8 học sinh có số cuốn sách đọc trong học kì I là: $3, 5, 2, 4, 3, 6, 4, 5$. Tổng số sách tổ đó đọc được là:", "options": ["$32$", "$30$", "$34$", "$28$"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Số lượng học sinh vắng mặt trong tuần của một lớp là: Thứ Hai: 1, Thứ Ba: 0, Thứ Tư: 2, Thứ Năm: 0, Thứ Sáu: 1. Số ngày không có học sinh vắng là:", "options": ["$2$ ngày", "$1$ ngày", "$3$ ngày", "$0$ ngày"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Thầy giáo ghi lại điểm kiểm tra giữa kì I môn Toán của 10 bạn trong tổ 1 như sau: $7; 8; 6; 9; 10; 8; 7; 8; 9; 8$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Dữ liệu thu được là dữ liệu định lượng (số liệu).", "isCorrect": True, "explanation": "Điểm số là các giá trị bằng số."},
                {"id": "b", "statement": "Điểm số cao nhất của tổ là $10$ điểm.", "isCorrect": True, "explanation": "Trong dãy điểm, điểm 10 là lớn nhất."},
                {"id": "c", "statement": "Có 4 bạn trong tổ đạt điểm 8.", "isCorrect": True, "explanation": "Có bốn giá trị 8 trong dãy: 8; 8; 8; 8."},
                {"id": "d", "statement": "Điểm trung bình của 10 bạn trong tổ bằng $7{,}5$.", "isCorrect": False, "explanation": "Tổng điểm $= 7+8+6+9+10+8+7+8+9+8 = 80 \\Rightarrow$ điểm trung bình $= 80/10 = 8{,}0 \\neq 7{,}5$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Trong các thông tin thu thập dưới đây, xét tính đúng/sai về việc phân loại dữ liệu:",
            "statements": [
                {"id": "a", "statement": "Họ và tên học sinh là dữ liệu định tính không thể sắp xếp thứ tự ưu tiên logic.", "isCorrect": True, "explanation": "Họ tên chỉ là danh xưng, không có thứ bậc hơn kém."},
                {"id": "b", "statement": "Kích cỡ áo sơ mi (S, M, L, XL, XXL) là dữ liệu định tính có thể sắp xếp thứ bậc.", "isCorrect": True, "explanation": "Các size biểu thị kích thước tăng dần từ nhỏ đến lớn."},
                {"id": "c", "statement": "Khối lượng một quả táo là dữ liệu định tính.", "isCorrect": False, "explanation": "Khối lượng tính bằng gam/kg là dữ liệu số (định lượng)."},
                {"id": "d", "statement": "Số người trong gia đình là dữ liệu số.", "isCorrect": True, "explanation": "Số người là số nguyên dương, là dữ liệu số."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một cửa hàng thống kê số lượng áo bán được theo size trong ngày: S: 15, M: 25, L: 20, XL: 10. Tổng số áo bán được trong ngày là bao nhiêu chiếc?", "answer": 70, "unit": "chiếc"},
        {"id": 2, "level": "Thông hiểu", "question": "Cho dãy dữ liệu nhiệt độ các ngày trong tuần: $28^\\circ C, 29^\\circ C, 31^\\circ C, 30^\\circ C, 32^\\circ C, 33^\\circ C, 27^\\circ C$. Chênh lệch giữa nhiệt độ cao nhất và thấp nhất là bao nhiêu độ C?", "answer": 6, "unit": "độ C"},
        {"id": 3, "level": "Vận dụng", "question": "Số lượng huy chương vàng của 5 lớp trong Hội khỏe Phù Đổng là: $3, 5, 2, 4, 6$. Trung bình mỗi lớp đạt được bao nhiêu huy chương vàng?", "answer": 4, "unit": "huy chương"},
        {"id": 4, "level": "Vận dụng", "question": "Trong danh sách số điện thoại của 6 người: $0912..., 0983..., 0905..., 12345, 0977..., 0936...$, có bao nhiêu số điện thoại không hợp lệ?", "answer": 1, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Để tìm hiểu về loại trái cây yêu thích của 40 học sinh lớp 7B, bạn An lập phiếu hỏi và thu được bảng dữ liệu như sau:\n- Cam: 12 bạn\n- Xoài: 10 bạn\n- Táo: 8 bạn\n- Chuối: 10 bạn\na) Dữ liệu thu thập được thuộc loại dữ liệu nào?\nb) Lập bảng thống kê biểu diễn dữ liệu trên và cho biết loại trái cây nào được yêu thích nhiều nhất.",
            "maxScore": 1.0,
            "solution": "a) Dữ liệu \"loại trái cây yêu thích\" là dữ liệu định tính (không phải số liệu, không thể sắp xếp thứ bậc).\nb) Bảng thống kê:\n| Loại trái cây | Cam | Xoài | Táo | Chuối |\n| Số bạn thích | 12 | 10 | 8 | 10 |\nTổng số học sinh là $12 + 10 + 8 + 10 = 40$ học sinh.\nLoại trái cây được yêu thích nhiều nhất là Cam (với 12 bạn lựa chọn).",
            "rubric": [
                {"step": "Xác định đúng loại dữ liệu định tính", "subScore": 0.4},
                {"step": "Lập đúng bảng thống kê và chỉ ra Cam nhiều nhất", "subScore": 0.6}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Bạn Minh ghi chép số giờ sử dụng máy tính mỗi ngày trong một tuần của mình như sau: $2; 1{,}5; 2; 3; 2{,}5; 14; 2$. Em hãy cho biết giá trị nào trong dãy trên là bất thường? Hãy giải thích vì sao và đề xuất phương án sửa lại cho hợp lí.",
            "maxScore": 1.0,
            "solution": "- Giá trị bất thường trong dãy số liệu là $14$ (giờ).\n- Giải thích: Một học sinh THCS trong ngày nghỉ cuối tuần hoặc ngày học thường chỉ dùng máy tính từ $1$ đến $3$ giờ. Việc sử dụng $14$ giờ một ngày là không hợp lí đối với lứa tuổi học sinh và sinh hoạt bình thường (rất có thể là lỗi ghi chép, bạn ghi nhầm $1{,}4$ hoặc $4$ giờ).\n- Phương án sửa: Bạn Minh cần kiểm tra lại nhật kí sử dụng của ngày hôm đó, nếu là $1{,}4$ giờ hoặc $4$ giờ thì sửa lại theo thực tế.",
            "rubric": [
                {"step": "Chỉ ra đúng giá trị bất thường là 14", "subScore": 0.4},
                {"step": "Giải thích tính bất hợp lí và đề xuất cách xử lí", "subScore": 0.6}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một tổ học sinh gồm 8 bạn có điểm kiểm tra thường xuyên môn Toán như sau: $6; 7; 8; 7; 9; 8; x; 10$. Biết điểm trung bình môn Toán của tổ là $8{,}0$. Hãy tìm điểm $x$ của bạn còn lại.",
            "maxScore": 1.0,
            "solution": "Tổng điểm của cả tổ gồm 8 bạn là:\n$S = 8 \\times 8{,}0 = 64$ (điểm).\nTổng điểm của 7 bạn đã biết là:\n$6 + 7 + 8 + 7 + 9 + 8 + 10 = 55$ (điểm).\nĐiểm số $x$ của bạn còn lại là:\n$x = 64 - 55 = 9$ (điểm).\nGiá trị $x = 9$ là hợp lí trong thang điểm 10.",
            "rubric": [
                {"step": "Tính tổng điểm của tổ: 64 điểm", "subScore": 0.4},
                {"step": "Thiết lập phương trình và giải ra x = 9", "subScore": 0.6}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c5_7_bai1_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 17: Thu thập và phân loại dữ liệu - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tiêu chí nào sau đây cần đảm bảo khi thu thập dữ liệu?", "options": ["Tính đầy đủ, chính xác và có tính đại diện", "Càng nhiều càng tốt không cần chính xác", "Chỉ chọn dữ liệu có lợi cho mình", "Thu thập ngẫu nhiên không cần mục đích"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Để đánh giá mức độ hài lòng của phụ huynh học sinh về các hoạt động ngoại khóa của trường, nhà trường nên thu thập dữ liệu bằng cách nào?", "options": ["Gửi phiếu khảo sát trực tuyến hoặc phiếu giấy đến toàn thể phụ huynh", "Hỏi ý kiến của một lớp bất kì", "Chỉ hỏi ban đại diện cha mẹ học sinh của trường", "Hỏi các thầy cô giáo chủ nhiệm"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Trong các dãy dữ liệu sau, dãy nào là dữ liệu định tính có thể so sánh thứ bậc?", "options": ["Học lực học kì: Tốt, Khá, Đạt, Chưa đạt", "Màu xe máy: Đỏ, Trắng, Đen, Xanh", "Môn thể thao: Cầu lông, Bóng rổ, Bơi lội", "Tên thủ đô các nước Đông Nam Á"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Khảo sát thời gian tự học ở nhà mỗi ngày của 5 bạn học sinh (đơn vị: giờ): $2; 1{,}5; -0{,}5; 3; 2{,}5$. Giá trị không hợp lí trong dãy dữ liệu là:", "options": ["$-0{,}5$", "$1{,}5$", "$2{,}5$", "$3$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Một bảng dữ liệu ghi điểm thi môn Tiếng Anh: $8; 7; 9; 10; 8; \\text{Tốt}; 7$. Thành phần không hợp lí là:", "options": ["$\\text{Tốt}$", "$10$", "$7$", "$8$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Thu thập số lượng học sinh của 4 khối lớp tại một trường THCS được kết quả: Khối 6: 180, Khối 7: 175, Khối 8: 160, Khối 9: 155. Tổng số học sinh toàn trường là:", "options": ["$670$", "$660$", "$680$", "$650$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Kết quả khảo sát món ăn sáng yêu thích của 100 học sinh: Bánh mì 45, Phở 25, Xôi 20, Khác 10. Tỉ lệ học sinh thích Bánh mì là:", "options": ["$45\\%$", "$25\\%$", "$20\\%$", "$55\\%$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Một bạn ghi chép số cuốn vở dùng trong một năm của 5 bạn: $15, 18, 12, 16, 14$. Trung vị của dãy số liệu trên là:", "options": ["$15$", "$16$", "$18$", "$14$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Số lượng cây trồng của 4 tổ trong đợt phát động Tết trồng cây: Tổ 1: 24, Tổ 2: 28, Tổ 3: 22, Tổ 4: 26. Tổ nào trồng được nhiều cây nhất?", "options": ["Tổ 2", "Tổ 1", "Tổ 4", "Tổ 3"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Cho dãy dữ liệu xếp loại thể lực: Rất khỏe (30%), Khỏe (50%), Trung bình (15%), Yếu (x%). Giá trị của $x$ để tổng phần trăm bằng 100% là:", "options": ["$5$", "$10$", "$15$", "$0$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Để chọn mẫu khảo sát đại diện cho ý kiến của 1000 học sinh toàn trường, phương pháp chọn mẫu nào sau đây là hợp lí nhất?", "options": ["Chọn ngẫu nhiên 10 học sinh từ mỗi lớp trong 25 lớp của trường", "Chọn toàn bộ học sinh khối 9", "Chọn 50 bạn hay đến thư viện", "Chọn các bạn tham gia đội tuyển học sinh giỏi"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Dữ liệu liên tục là dữ liệu nhận các giá trị trong một khoảng số thực. Ví dụ nào sau đây là dữ liệu liên tục?", "options": ["Cân nặng của các bạn học sinh (kg)", "Số lượng học sinh trong lớp", "Số bàn thắng trong trận đấu", "Số quyển sách trên giá"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Bảng khảo sát mức độ hài lòng về căn tin trường học của 200 học sinh:\n- Rất hài lòng: 60 bạn\n- Hài lòng: 100 bạn\n- Bình thường: 30 bạn\n- Không hài lòng: 10 bạn.\nXét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Dữ liệu khảo sát là dữ liệu định tính có thứ bậc.", "isCorrect": True, "explanation": "Các mức độ hài lòng sắp xếp được từ cao xuống thấp."},
                {"id": "b", "statement": "Tỉ lệ học sinh \"Hài lòng\" chiếm đúng $50\\%$ số học sinh được khảo sát.", "isCorrect": True, "explanation": "$100 / 200 = 50\\%$."},
                {"id": "c", "statement": "Tổng số học sinh có ý kiến tích cực (Rất hài lòng và Hài lòng) là $160$ bạn ($80\\%$).", "isCorrect": True, "explanation": "$60 + 100 = 160$ bạn, tức $160/200 = 80\\%$."},
                {"id": "d", "statement": "Số học sinh không hài lòng chiếm $10\\%$ tổng số học sinh.", "isCorrect": False, "explanation": "$10 / 200 = 5\\%$ chứ không phải $10\\%$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Bạn Hà ghi lại điểm thi 5 môn của mình: Toán 9, Ngữ văn 8, Tiếng Anh 9, KHTN 9, Lịch sử & Địa lí $x$. Biết điểm trung bình 5 môn là $8{,}8$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Dữ liệu điểm số là dữ liệu số liệu.", "isCorrect": True, "explanation": "Điểm là các con số cụ thể."},
                {"id": "b", "statement": "Tổng điểm 4 môn đã biết bằng $35$ điểm.", "isCorrect": True, "explanation": "$9 + 8 + 9 + 9 = 35$ điểm."},
                {"id": "c", "statement": "Tổng điểm của 5 môn là $44$ điểm.", "isCorrect": True, "explanation": "$8{,}8 \\times 5 = 44$ điểm."},
                {"id": "d", "statement": "Điểm số $x$ của môn Lịch sử & Địa lí là $8{,}5$.", "isCorrect": False, "explanation": "$x = 44 - 35 = 9$ điểm, không phải $8{,}5$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Khảo sát sĩ số 4 lớp khối 7: lớp 7A có 42 bạn, 7B có 40 bạn, 7C có 45 bạn, 7D có 41 bạn. Tìm sĩ số trung bình của mỗi lớp (điền số thập phân).", "answer": 42, "unit": "học sinh"},
        {"id": 2, "level": "Vận dụng", "question": "Một nhóm gồm 10 học sinh làm một bài trắc nghiệm có 10 câu hỏi. Số câu đúng của các bạn là: $8, 9, 7, 10, 8, 9, 6, 8, 9, 6$. Có bao nhiêu bạn đạt từ 8 câu đúng trở lên?", "answer": 8, "unit": "bạn"},
        {"id": 3, "level": "Vận dụng", "question": "Trong một giải bóng đá có 4 đội thi đấu vòng tròn 1 lượt (mỗi đội gặp nhau 1 lần). Tổng số trận đấu trong giải là bao nhiêu?", "answer": 6, "unit": "trận"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho một dãy số liệu gồm 5 số nguyên dương có số trung bình cộng là 12, số nhỏ nhất là 8, số lớn nhất là 20. Tổng của 3 số còn lại là bao nhiêu?", "answer": 32, "unit": ""}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Để khảo sát về phương tiện đến trường của học sinh một trường THCS, bạn Lan đề xuất: \"Chỉ phỏng vấn các bạn đi xe đạp điện ở cổng trường vào lúc 6h45 sáng\".\na) Em có đồng ý với phương pháp thu thập dữ liệu của bạn Lan không? Vì sao?\nb) Hãy đề xuất một phương án thu thập dữ liệu đại diện và khách quan hơn.",
            "maxScore": 1.0,
            "solution": "a) Em không đồng ý với phương pháp của bạn Lan.\nVì mẫu thu thập không mang tính đại diện cho toàn thể học sinh trong trường: chỉ phỏng vấn các bạn đi xe đạp điện sẽ bỏ sót các phương tiện khác (đi bộ, xe buýt, xe đạp thường, phụ huynh chở bằng ô tô/xe máy).\nb) Phương án đề xuất khách quan hơn:\n- Lập phiếu khảo sát (trên giấy hoặc trực tuyến) gửi tới tất cả các lớp trong trường.\n- Hoặc tại mỗi lớp trong toàn trường, chọn ngẫu nhiên 5 đến 10 học sinh để phỏng vấn, đảm bảo đại diện đủ các khối lớp và phương tiện.",
            "rubric": [
                {"step": "Nhận xét đúng và giải thích tính thiếu đại diện của mẫu", "subScore": 0.5},
                {"step": "Đề xuất phương án thu thập đại diện và khoa học", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một trạm khí tượng thủy văn đo lượng mưa (đơn vị: mm) trong 7 ngày liên tiếp của tuần đầu tháng 8 như sau: $12; 25; 0; 45; 18; 150; 30$.\na) Phân tích xem trong dãy số liệu trên có giá trị nào bất thường không?\nb) Nếu giá trị 150 mm xuất hiện trong ngày có bão lớn đổ bộ, thì giá trị đó có hợp lí không?",
            "maxScore": 1.0,
            "solution": "a) Giá trị $150$ mm cao đột biến so với các ngày còn lại (dao động từ $0$ đến $45$ mm). Nếu trong điều kiện thời tiết ngày thường thì giá trị $150$ là một giá trị bất thường.\nb) Nếu ngày đó có bão lớn đổ bộ thì lượng mưa $150$ mm là hoàn toàn hợp lí về mặt thực tế khí tượng, phản ánh đúng hiện tượng thời tiết cực đoan và cần được giữ nguyên trong báo cáo thống kê kèm chú thích về cơn bão.",
            "rubric": [
                {"step": "Chỉ ra giá trị 150 mm cao đột biến và giải thích", "subScore": 0.5},
                {"step": "Lập luận tính hợp lí trong hoàn cảnh có bão lớn", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một tổ có 10 học sinh gồm 6 nam và 4 nữ. Điểm trung bình môn Toán của 6 bạn nam là $7{,}5$ và điểm trung bình môn Toán của 4 bạn nữ là $8{,}5$. Hãy tính điểm trung bình môn Toán của cả tổ 10 bạn.",
            "maxScore": 1.0,
            "solution": "Tổng điểm môn Toán của 6 bạn nam là:\n$S_{\\text{nam}} = 6 \\times 7{,}5 = 45$ (điểm).\nTổng điểm môn Toán của 4 bạn nữ là:\n$S_{\\text{nữ}} = 4 \\times 8{,}5 = 34$ (điểm).\nTổng điểm môn Toán của cả tổ 10 bạn là:\n$S = S_{\\text{nam}} + S_{\\text{nữ}} = 45 + 34 = 79$ (điểm).\nĐiểm trung bình môn Toán của cả tổ là:\n$\\bar{X} = \\frac{79}{10} = 7{,}9$ (điểm).\nVậy điểm trung bình của cả tổ là $7{,}9$.",
            "rubric": [
                {"step": "Tính đúng tổng điểm nam (45) và tổng điểm nữ (34)", "subScore": 0.5},
                {"step": "Tính đúng điểm trung bình cả tổ là 7,9", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c5_7_bai1_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 17: Thu thập và phân loại dữ liệu - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Khi nghiên cứu tỉ lệ ủng hộ của công chúng đối với dự án mở rộng công viên, cơ quan khảo sát phỏng vấn 100 người đi bộ trong công viên đó vào sáng Chủ nhật. Kết luận nào sau đây đúng về mẫu khảo sát?", "options": ["Mẫu bị thiên lệch (chệch) vì người có mặt ở công viên có xu hướng ủng hộ cao hơn mặt bằng chung", "Mẫu có tính đại diện cao cho toàn bộ dân cư thành phố", "Mẫu hoàn toàn ngẫu nhiên và khách quan", "Mẫu không đủ số lượng người để khảo sát"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Dữ liệu nào sau đây là dữ liệu rời rạc (chỉ nhận giá trị nguyên hoặc đếm được)?", "options": ["Số lượng xe ôtô đi qua trạm thu phí mỗi giờ", "Khối lượng bao gạo cân được", "Khoảng cách giữa hai thành phố", "Thời gian chạy 100 m của vận động viên"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Một bảng thống kê thu nhập của 10 hộ gia đình (triệu đồng/tháng): $12, 15, 10, 14, 13, 11, 16, 12, 14, 500$. Để phản ánh đúng mức thu nhập phổ biến của đa số người dân, số đặc trưng nào thích hợp hơn?", "options": ["Số trung vị", "Số trung bình cộng", "Số lớn nhất", "Tổng thu nhập"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho dãy số liệu điểm thi: $5, 7, 8, 9, x, 6, 8, 10$. Biết trung bình cộng của dãy là $7{,}5$. Giá trị của $x$ là:", "options": ["$7$", "$8$", "$6$", "$9$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Một trường học có tỉ lệ học sinh các khối 6, 7, 8, 9 lần lượt là $28\\%, 26\\%, 24\\%, 22\\%$. Nếu cần chọn 200 học sinh theo đúng tỉ lệ trên, số học sinh khối 7 cần chọn là:", "options": ["$52$ bạn", "$56$ bạn", "$48$ bạn", "$44$ bạn"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Khảo sát cân nặng của 5 em bé sơ sinh: $3{,}1; 3{,}3; 3{,}2; 3{,}5; 2{,}9$ (kg). Độ lệch giữa bé nặng nhất và bé nhẹ nhất là:", "options": ["$0{,}6$ kg", "$0{,}4$ kg", "$0{,}5$ kg", "$0{,}3$ kg"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Một cuộc thăm dò ý kiến gồm 500 phiếu có 3 phương án lựa chọn A, B, C. Tỉ lệ chọn A là 42%, chọn B là 38%. Số người chọn phương án C là:", "options": ["$100$ người", "$80$ người", "$120$ người", "$150$ người"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Có 4 số tự nhiên có trung bình cộng là 15. Nếu thêm số thứ năm là 25 thì trung bình cộng của cả 5 số là:", "options": ["$17$", "$18$", "$16$", "$20$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Một lớp có 40 học sinh gồm hai nhóm A và B. Nhóm A có 25 học sinh có điểm trung bình là 8,0. Nhóm B có điểm trung bình là 7,0. Điểm trung bình của cả lớp là:", "options": ["$7{,}625$", "$7{,}5$", "$7{,}6$", "$7{,}7$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Để tìm hiểu thời lượng sử dụng Internet của học sinh khối 7, người ta phân tầng chọn ngẫu nhiên mỗi lớp 10 học sinh. Phương pháp này gọi là:", "options": ["Chọn mẫu ngẫu nhiên phân tầng", "Chọn mẫu thuận tiện", "Chọn mẫu hệ thống", "Chọn mẫu tự nguyện"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một dãy số liệu có 7 giá trị nguyên dương tăng dần: $3, 5, 7, x, 11, 14, 18$. Biết số trung vị bằng 9. Giá trị của $x$ là:", "options": ["$9$", "$8$", "$10$", "$7$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Sai số trong thu thập dữ liệu có thể phát sinh từ:", "options": ["Dụng cụ đo không chuẩn, người trả lời khai báo sai hoặc người nhập dữ liệu nhầm lẫn", "Chỉ do dụng cụ đo", "Chỉ do người khảo sát cố ý làm sai", "Không bao giờ có sai số nếu khảo sát nhiều"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Một giáo viên theo dõi thời gian làm một bài toán (tính theo phút) của 12 học sinh: $5, 6, 7, 6, 8, 5, 9, 7, 6, 8, 7, 6$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Thời gian làm bài nhanh nhất là $5$ phút và chậm nhất là $9$ phút.", "isCorrect": True, "explanation": "Giá trị nhỏ nhất là 5, lớn nhất là 9."},
                {"id": "b", "statement": "Giá trị xuất hiện nhiều nhất (mốt) của dãy số liệu là $6$ phút (xuất hiện 4 lần).", "isCorrect": True, "explanation": "Số 6 xuất hiện 4 lần, nhiều nhất."},
                {"id": "c", "statement": "Tổng thời gian làm bài của 12 học sinh là $80$ phút.", "isCorrect": True, "explanation": "$5+6+7+6+8+5+9+7+6+8+7+6 = 80$ phút."},
                {"id": "d", "statement": "Thời gian trung bình làm bài của một học sinh là đúng $7$ phút.", "isCorrect": False, "explanation": "Trung bình $= 80 / 12 \\approx 6{,}67$ phút, không phải 7 phút."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho bảng phân bố tần số về số lỗi chính tả trong bài kiểm tra Ngữ văn của 30 học sinh:\n- 0 lỗi: 12 học sinh\n- 1 lỗi: 8 học sinh\n- 2 lỗi: 6 học sinh\n- 3 lỗi: 4 học sinh.\nXét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tổng số lỗi chính tả của cả 30 học sinh là $32$ lỗi.", "isCorrect": True, "explanation": "$0 \\times 12 + 1 \\times 8 + 2 \\times 6 + 3 \\times 4 = 0 + 8 + 12 + 12 = 32$ lỗi."},
                {"id": "b", "statement": "Tỉ lệ học sinh không mắc lỗi chính tả chiếm $40\\%$.", "isCorrect": True, "explanation": "$12 / 30 = 40\\%$."},
                {"id": "c", "statement": "Số lỗi chính tả trung bình của mỗi học sinh là hơn $1{,}5$ lỗi.", "isCorrect": False, "explanation": "Trung bình $= 32 / 30 \\approx 1{,}07$ lỗi, nhỏ hơn 1,5."},
                {"id": "d", "statement": "Tỉ lệ học sinh mắc từ 2 lỗi trở lên là $\\frac{1}{3}$.", "isCorrect": True, "explanation": "Có $6 + 4 = 10$ học sinh mắc $\\ge 2$ lỗi $\\Rightarrow 10/30 = 1/3$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Một tổ có 5 bạn có tuổi trung bình là 13 tuổi. Khi thầy giáo chủ nhiệm 31 tuổi tham gia vào nhóm thì tuổi trung bình của cả 6 người là bao nhiêu tuổi?", "answer": 16, "unit": "tuổi"},
        {"id": 2, "level": "Vận dụng", "question": "Cho 6 số có trung bình cộng bằng 20. Nếu bỏ đi một số thì trung bình cộng của 5 số còn lại là 18. Số bị bỏ đi là bao nhiêu?", "answer": 30, "unit": ""},
        {"id": 3, "level": "Vận dụng cao", "question": "Khảo sát điểm kiểm tra của 20 học sinh ta tính được điểm trung bình là 7,5. Khi kiểm tra lại phát hiện ghi nhầm 1 bạn từ điểm 3 thành điểm 8. Điểm trung bình chính xác của 20 bạn là bao nhiêu (điền số thập phân)?", "answer": 7.25, "unit": ""},
        {"id": 4, "level": "Vận dụng cao", "question": "Trong đợt quyên góp sách, lớp 7A có 3 tổ: Tổ 1 quyên góp 30 quyển, Tổ 2 quyên góp 45 quyển, Tổ 3 quyên góp số sách bằng trung bình cộng của cả 3 tổ. Tổ 3 quyên góp được bao nhiêu quyển sách?", "answer": 37.5, "unit": "quyển"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Một công ty dự định ra mắt một hương vị kem mới dành cho lứa tuổi thanh thiếu niên (từ 12 đến 18 tuổi). Giám đốc yêu cầu bộ phận nghiên cứu thị trường thu thập ý kiến khách hàng.\na) Nêu 2 sai lầm có thể xảy ra nếu nhóm nghiên cứu chỉ khảo sát khách hàng tại các quán cà phê cao cấp vào buổi sáng ngày làm việc.\nb) Thiết kế một kế hoạch khảo sát hợp lí (đối tượng, địa điểm, thời gian, phương pháp) để dữ liệu thu được đảm bảo tính đại diện và khách quan.",
            "maxScore": 1.0,
            "solution": "a) Hai sai lầm có thể xảy ra:\n1. Sai lầm về đối tượng khách hàng: Khách hàng tại quán cà phê cao cấp vào sáng ngày làm việc chủ yếu là người đi làm, người lớn tuổi, không thuộc nhóm thanh thiếu niên (12 - 18 tuổi) là đối tượng mục tiêu của sản phẩm.\n2. Sai lầm về thời gian: Buổi sáng ngày làm việc, thanh thiếu niên đang đi học ở trường nên mẫu khảo sát bị lệch hoàn toàn.\nb) Kế hoạch khảo sát đề xuất hợp lí:\n- Đối tượng: Học sinh THCS và THPT từ 12 đến 18 tuổi.\n- Địa điểm: Cổng trường học, khu vui chơi giải trí, nhà sách, trung tâm thương mại hoặc các lớp học thêm.\n- Thời gian: Chiều tan học, ngày thứ Bảy và Chủ nhật.\n- Phương pháp: Cho thử mẫu kem miễn phí giấu nhãn hiệu (mù đôi) và phát phiếu đánh giá trực tiếp về hương vị, độ ngọt, mức giá sẵn sàng chi trả.",
            "rubric": [
                {"step": "Phân tích rõ 2 sai lầm về đối tượng và thời gian khảo sát", "subScore": 0.5},
                {"step": "Thiết kế kế hoạch khảo sát chuẩn chỉnh đầy đủ 4 yếu tố", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho bảng phân bố điểm kiểm tra cuối kì môn Toán của lớp 7A (sĩ số 40 bạn):\n| Điểm | 5 | 6 | 7 | 8 | 9 | 10 |\n| Số bạn | 3 | 7 | 12 | 10 | 6 | 2 |\na) Tính điểm trung bình môn Toán của lớp 7A.\nb) Nhà trường quy định lớp đạt chuẩn tiên tiến nếu có từ $70\\%$ số học sinh đạt điểm từ 7 trở lên. Lớp 7A có đạt tiêu chuẩn này không?",
            "maxScore": 1.0,
            "solution": "a) Tổng điểm của cả lớp là:\n$S = 5 \\times 3 + 6 \\times 7 + 7 \\times 12 + 8 \\times 10 + 9 \\times 6 + 10 \\times 2$\n$= 15 + 42 + 84 + 80 + 54 + 20 = 295$ (điểm).\nĐiểm trung bình của lớp 7A là:\n$\\bar{X} = \\frac{295}{40} = 7{,}375$ (điểm).\nb) Số học sinh đạt điểm từ 7 trở lên là:\n$12 + 10 + 6 + 2 = 30$ (học sinh).\nTỉ lệ học sinh đạt điểm từ 7 trở lên là:\n$P = \\frac{30}{40} \\times 100\\% = 75\\%$.\nVì $75\\% > 70\\%$, nên lớp 7A hoàn toàn đạt tiêu chuẩn lớp tiên tiến theo quy định của nhà trường.",
            "rubric": [
                {"step": "Tính đúng tổng điểm 295 và điểm trung bình 7,375", "subScore": 0.5},
                {"step": "Tính đúng tỉ lệ 75% và đưa ra kết luận đạt chuẩn", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một nhóm gồm $n$ người có độ tuổi trung bình là 24 tuổi. Sau khi có một người 36 tuổi rời nhóm và một người 18 tuổi gia nhập nhóm thì độ tuổi trung bình của nhóm giảm đi 1 tuổi (số lượng người trong nhóm không đổi). Hãy tìm số người $n$ trong nhóm.",
            "maxScore": 1.0,
            "solution": "Tổng số tuổi ban đầu của $n$ người là:\n$T_1 = 24n$ (tuổi).\nSau khi người 36 tuổi rời đi và người 18 tuổi gia nhập, tổng số tuổi mới của nhóm là:\n$T_2 = 24n - 36 + 18 = 24n - 18$ (tuổi).\nĐộ tuổi trung bình mới của nhóm là $24 - 1 = 23$ tuổi.\nVì số người trong nhóm vẫn là $n$, ta có phương trình:\n$\\frac{24n - 18}{n} = 23$\n$\\Leftrightarrow 24n - 18 = 23n$\n$\\Leftrightarrow 24n - 23n = 18$\n$\\Leftrightarrow n = 18$.\nVậy trong nhóm có 18 người.",
            "rubric": [
                {"step": "Biểu diễn tổng số tuổi ban đầu và tổng số tuổi mới", "subScore": 0.5},
                {"step": "Thiết lập phương trình và giải ra n = 18", "subScore": 0.5}
            ]
        }
    ]
}

# =====================================================================
# BÀI 18: BIỂU ĐỒ HÌNH QUẠT TRÒN
# =====================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c5_7_bai2_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 18: Biểu đồ hình quạt tròn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Biểu đồ hình quạt tròn thường được dùng để:", "options": ["So sánh các phần trong toàn bộ dữ liệu (tỉ lệ phần trăm)", "Biểu diễn sự thay đổi của dữ liệu theo thời gian", "So sánh các giá trị tuyệt đối giữa các đối tượng", "Biểu diễn vị trí không gian"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Trong biểu đồ hình quạt tròn, toàn bộ hình tròn biểu diễn:", "options": ["$100\\%$", "$50\\%$", "$360\\%$", "$180\\%$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trong hình tròn có tổng số đo góc ở tâm là:", "options": ["$360^\\circ$", "$180^\\circ$", "$90^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Một hình quạt tròn biểu diễn $25\\%$ của tổng thể thì góc ở tâm tương ứng là:", "options": ["$90^\\circ$", "$45^\\circ$", "$180^\\circ$", "$60^\\circ$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Một hình quạt tròn có góc ở tâm là $180^\\circ$ thì biểu diễn bao nhiêu phần trăm tổng thể?", "options": ["$50\\%$", "$25\\%$", "$75\\%$", "$100\\%$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Biểu đồ hình quạt tròn thể hiện cơ cấu chi tiêu của một gia đình gồm: Ăn uống (40%), Tiết kiệm (20%), Giáo dục (25%), Chi khác (x%). Giá trị của $x$ là:", "options": ["$15$", "$20$", "$10$", "$5$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Lớp 7A có 40 học sinh. Biểu đồ quạt tròn cho biết học sinh Khá chiếm $40\\%$. Số học sinh Khá của lớp 7A là:", "options": ["$16$ học sinh", "$10$ học sinh", "$20$ học sinh", "$24$ học sinh"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Góc ở tâm biểu diễn tỉ lệ $10\\%$ trong biểu đồ quạt tròn là:", "options": ["$36^\\circ$", "$10^\\circ$", "$18^\\circ$", "$72^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Một trường học có 800 học sinh. Biểu đồ quạt tròn cho thấy $50\\%$ học sinh đi bộ đến trường. Số học sinh đi bộ đến trường là:", "options": ["$400$ học sinh", "$300$ học sinh", "$500$ học sinh", "$200$ học sinh"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Trong biểu đồ hình quạt tròn biểu diễn các phương tiện đến trường, hình quạt biểu diễn \"Đi xe buýt\" chiếm góc $72^\\circ$. Tỉ lệ phần trăm học sinh đi xe buýt là:", "options": ["$20\\%$", "$15\\%$", "$25\\%$", "$30\\%$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Khảo sát loại hình giải trí yêu thích của 200 bạn: Đọc sách $25\\%$, Chơi thể thao $45\\%$, Xem phim $20\\%$, Khác $10\\%$. Số bạn thích chơi thể thao là:", "options": ["$90$ bạn", "$50$ bạn", "$40$ bạn", "$70$ bạn"], "correct": 0},
        {"id": 12, "level": "Vận dụng", "question": "Một thư viện trường có 1200 cuốn sách gồm 3 loại: Sách giáo khoa (50%), Sách tham khảo (30%), Truyện tranh (20%). Số sách tham khảo là:", "options": ["$360$ cuốn", "$600$ cuốn", "$240$ cuốn", "$400$ cuốn"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Biểu đồ hình quạt tròn biểu diễn tỉ lệ phần trăm xếp loại học lực của khối 7 (gồm 300 học sinh): Xuất sắc 15%, Tốt 35%, Khá 40%, Đạt 10%. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tổng các tỉ lệ phần trăm trên biểu đồ bằng $100\\%$.", "isCorrect": True, "explanation": "$15\\% + 35\\% + 40\\% + 10\\% = 100\\%$."},
                {"id": "b", "statement": "Số học sinh đạt loại Xuất sắc là $45$ học sinh.", "isCorrect": True, "explanation": "$300 \\times 15\\% = 45$ học sinh."},
                {"id": "c", "statement": "Số học sinh Khá nhiều hơn số học sinh Tốt là $15$ học sinh.", "isCorrect": True, "explanation": "Học sinh Khá $= 300 \\times 40\\% = 120$; Tốt $= 300 \\times 35\\% = 105 \\Rightarrow 120 - 105 = 15$ bạn."},
                {"id": "d", "statement": "Góc ở tâm của hình quạt biểu diễn học sinh loại Đạt là $18^\\circ$.", "isCorrect": False, "explanation": "Góc ở tâm $= 360^\\circ \\times 10\\% = 36^\\circ$, không phải $18^\\circ$."}
            ]
        },
        {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Cho các nhận định về góc ở tâm trong biểu đồ hình quạt tròn, xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tỉ lệ $50\\%$ ứng với góc ở tâm là $180^\\circ$ (nửa hình tròn).", "isCorrect": True, "explanation": "$360^\\circ \\times 50\\% = 180^\\circ$."},
                {"id": "b", "statement": "Tỉ lệ $25\\%$ ứng với góc ở tâm là $90^\\circ$ (góc vuông).", "isCorrect": True, "explanation": "$360^\\circ \\times 25\\% = 90^\\circ$."},
                {"id": "c", "statement": "Tỉ lệ $75\\%$ ứng với góc ở tâm là $270^\\circ$.", "isCorrect": True, "explanation": "$360^\\circ \\times 75\\% = 270^\\circ$."},
                {"id": "d", "statement": "Hình quạt có góc ở tâm $60^\\circ$ biểu diễn tỉ lệ $20\\%$.", "isCorrect": False, "explanation": "$60^\\circ / 360^\\circ = 1/6 \\approx 16{,}67\\% \\neq 20\\%$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính số đo góc ở tâm (độ) tương ứng với hình quạt tròn biểu diễn $30\\%$ tổng thể.", "answer": 108, "unit": "độ"},
        {"id": 2, "level": "Thông hiểu", "question": "Một tổ có 10 bạn quyên góp được 50 quyển sách. Trong đó sách tham khảo chiếm $40\\%$. Hỏi có bao nhiêu quyển sách tham khảo?", "answer": 20, "unit": "quyển"},
        {"id": 3, "level": "Vận dụng", "question": "Một gia đình có thu nhập 20 triệu đồng mỗi tháng. Biểu đồ quạt tròn cho biết tiền ăn uống chiếm $45\\%$. Hỏi mỗi tháng gia đình đó chi bao nhiêu triệu đồng cho tiền ăn uống?", "answer": 9, "unit": "triệu đồng"},
        {"id": 4, "level": "Vận dụng", "question": "Biểu đồ quạt tròn thể hiện diện tích trồng trọt: Lúa 60%, Ngô 25%, Khoai 15%. Biết diện tích trồng khoai là 30 ha. Tổng diện tích trồng trọt là bao nhiêu ha?", "answer": 200, "unit": "ha"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Bảng sau đây cho biết kết quả xếp loại thi đua học kì I của 40 học sinh lớp 7C:\n- Tốt: 16 bạn\n- Khá: 14 bạn\n- Đạt: 8 bạn\n- Chưa đạt: 2 bạn\na) Tính tỉ lệ phần trăm của mỗi loại xếp loại thi đua so với cả lớp.\nb) Tính góc ở tâm tương ứng của từng hình quạt biểu diễn các loại trên trong biểu đồ hình quạt tròn.",
            "maxScore": 1.0,
            "solution": "a) Tỉ lệ phần trăm của từng loại:\n- Tốt: $\\frac{16}{40} \\times 100\\% = 40\\%$.\n- Khá: $\\frac{14}{40} \\times 100\\% = 35\\%$.\n- Đạt: $\\frac{8}{40} \\times 100\\% = 20\\%$.\n- Chưa đạt: $\\frac{2}{40} \\times 100\\% = 5\\%$.\nTổng tỉ lệ $= 40\\% + 35\\% + 20\\% + 5\\% = 100\\%$.\nb) Góc ở tâm tương ứng:\n- Tốt: $360^\\circ \\times 40\\% = 144^\\circ$.\n- Khá: $360^\\circ \\times 35\\% = 126^\\circ$.\n- Đạt: $360^\\circ \\times 20\\% = 72^\\circ$.\n- Chưa đạt: $360^\\circ \\times 5\\% = 18^\\circ$.\nTổng các góc ở tâm $= 144^\\circ + 126^\\circ + 72^\\circ + 18^\\circ = 360^\\circ$.",
            "rubric": [
                {"step": "Tính đúng 4 tỉ lệ phần trăm", "subScore": 0.5},
                {"step": "Tính đúng 4 số đo góc ở tâm tương ứng", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Biểu đồ hình quạt tròn biểu diễn cơ cấu các loại cây ăn quả trong một vườn cây gồm 500 cây:\n- Cây xoài: 30%\n- Cây ổi: 25%\n- Cây cam: 35%\n- Cây bưởi: 10%\na) Tính số lượng cây mỗi loại trong vườn.\nb) Loại cây nào được trồng nhiều nhất và nhiều hơn loại cây ít nhất bao nhiêu cây?",
            "maxScore": 1.0,
            "solution": "a) Số lượng cây mỗi loại trong vườn:\n- Cây xoài: $500 \\times 30\\% = 150$ cây.\n- Cây ổi: $500 \\times 25\\% = 125$ cây.\n- Cây cam: $500 \\times 35\\% = 175$ cây.\n- Cây bưởi: $500 \\times 10\\% = 50$ cây.\nb) Cây cam được trồng nhiều nhất (175 cây), cây bưởi được trồng ít nhất (50 cây).\nChênh lệch số lượng là: $175 - 50 = 125$ cây.",
            "rubric": [
                {"step": "Tính đúng số lượng cả 4 loại cây", "subScore": 0.6},
                {"step": "Xác định cây cam nhiều nhất và độ chênh lệch là 125 cây", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một người bán hàng thống kê doanh thu bán 3 mặt hàng trong một ngày:\n- Mặt hàng A đạt doanh thu 4 triệu đồng (chiếm 50% tổng doanh thu).\n- Mặt hàng B chiếm 30% tổng doanh thu.\n- Mặt hàng C chiếm phần còn lại.\na) Tính tổng doanh thu trong ngày của người đó.\nb) Tính doanh thu của mặt hàng B và mặt hàng C.",
            "maxScore": 1.0,
            "solution": "a) Vì mặt hàng A đạt doanh thu 4 triệu đồng và chiếm 50% tổng doanh thu nên tổng doanh thu trong ngày là:\n$4 : 50\\% = 4 : 0{,}5 = 8$ (triệu đồng).\nb) Doanh thu của mặt hàng B là:\n$8 \\times 30\\% = 2{,}4$ (triệu đồng).\nTỉ lệ doanh thu của mặt hàng C là:\n$100\\% - 50\\% - 30\\% = 20\\%$.\nDoanh thu của mặt hàng C là:\n$8 \\times 20\\% = 1{,}6$ (triệu đồng) (hoặc $8 - 4 - 2{,}4 = 1{,}6$ triệu đồng).",
            "rubric": [
                {"step": "Tính đúng tổng doanh thu 8 triệu đồng", "subScore": 0.5},
                {"step": "Tính đúng doanh thu mặt hàng B (2,4 tr) và C (1,6 tr)", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c5_7_bai2_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 18: Biểu đồ hình quạt tròn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Góc ở tâm $54^\\circ$ trong biểu đồ hình quạt tròn tương ứng với tỉ lệ phần trăm là:", "options": ["$15\\%$", "$12\\%$", "$18\\%$", "$20\\%$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Biểu đồ quạt tròn biểu diễn thành phần các loại rác thải: Rác hữu cơ 55%, Nhựa tái chế 20%, Giấy 15%, Rác khác 10%. Góc ở tâm biểu diễn Rác hữu cơ là:", "options": ["$198^\\circ$", "$180^\\circ$", "$200^\\circ$", "$190^\\circ$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Một người dành 8 giờ để ngủ mỗi ngày. Trên biểu đồ quạt tròn biểu diễn 24 giờ trong ngày, hình quạt biểu diễn thời gian ngủ có góc ở tâm là:", "options": ["$120^\\circ$", "$90^\\circ$", "$100^\\circ$", "$150^\\circ$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Biểu đồ hình quạt biểu diễn thể loại phim yêu thích của 400 học sinh: Hoạt hình 45%, Hành động 30%, Hài 15%, Trinh thám 10%. Số học sinh thích phim Hoạt hình nhiều hơn phim Hài là:", "options": ["$120$ bạn", "$100$ bạn", "$80$ bạn", "$60$ bạn"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Biểu đồ quạt tròn có 3 hình quạt với các góc ở tâm lần lượt là $90^\\circ, 120^\\circ$ và góc thứ ba. Số đo góc thứ ba là:", "options": ["$150^\\circ$", "$160^\\circ$", "$140^\\circ$", "$130^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một giải chạy việt dã có 500 vận động viên tham gia. Tỉ lệ hoàn thành cự ly là 84%, bỏ cuộc là 16%. Số vận động viên hoàn thành cự ly là:", "options": ["$420$ người", "$400$ người", "$430$ người", "$450$ người"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Một hợp kim gồm Đồng, Kẽm và Chì. Biểu đồ quạt tròn cho biết Đồng chiếm $60\\%$, Kẽm chiếm $35\\%$, còn lại là Chì. Khối lượng Chì trong $200$ g hợp kim là:", "options": ["$10$ g", "$20$ g", "$15$ g", "$5$ g"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Biểu đồ hình quạt thể hiện kết quả học tập của học sinh khối 7. Biết góc ở tâm của nhóm học sinh Giỏi là $72^\\circ$. Tỉ số giữa số học sinh Giỏi và tổng số học sinh khối 7 là:", "options": ["$\\frac{1}{5}$", "$\\frac{1}{4}$", "$\\frac{1}{6}$", "$\\frac{2}{5}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Trong biểu đồ quạt tròn biểu diễn doanh thu 4 quý của một công ty, Quý I chiếm 20%, Quý II chiếm 25%, Quý III chiếm 30%. Nếu doanh thu Quý IV là 50 tỷ đồng thì tổng doanh thu cả năm là:", "options": ["$200$ tỷ đồng", "$150$ tỷ đồng", "$250$ tỷ đồng", "$180$ tỷ đồng"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Một lớp có số học sinh giỏi chiếm 30%, khá chiếm 50%, còn lại là 8 học sinh trung bình. Số học sinh của cả lớp là:", "options": ["$40$ học sinh", "$45$ học sinh", "$50$ học sinh", "$35$ học sinh"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Để vẽ biểu đồ hình quạt tròn cho bảng số liệu gồm 5 đối tượng có các tỉ lệ: 30%, 25%, 20%, 15%, 10%, số đo góc lớn nhất gấp mấy lần số đo góc nhỏ nhất?", "options": ["$3$ lần", "$2$ lần", "$2{,}5$ lần", "$4$ lần"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Hai biểu đồ hình quạt tròn A và B cùng biểu diễn tỉ lệ học sinh thích môn Toán là $25\\%$. Biết tổng số học sinh ở biểu đồ A là 400 em, ở biểu đồ B là 600 em. Khẳng định nào sau đây đúng?", "options": ["Số học sinh thích môn Toán ở trường B nhiều hơn trường A", "Số học sinh thích môn Toán ở hai trường bằng nhau", "Góc ở tâm của hình quạt biểu diễn môn Toán ở trường B lớn hơn trường A", "Góc ở tâm của hình quạt biểu diễn môn Toán ở trường A lớn hơn trường B"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Biểu đồ hình quạt tròn biểu diễn các khoản chi tiêu hàng tháng của một gia đình có tổng thu nhập 25 triệu đồng:\n- Tiền ăn: 40%\n- Tiền nhà: 24%\n- Giáo dục: 20%\n- Tiết kiệm: 16%.\nXét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Số tiền chi tiêu cho tiền ăn là $10$ triệu đồng.", "isCorrect": True, "explanation": "$25 \\times 40\\% = 10$ triệu đồng."},
                {"id": "b", "statement": "Số tiền tiết kiệm mỗi tháng là $4$ triệu đồng.", "isCorrect": True, "explanation": "$25 \\times 16\\% = 4$ triệu đồng."},
                {"id": "c", "statement": "Góc ở tâm của hình quạt biểu diễn tiền nhà là $86{,}4^\\circ$.", "isCorrect": True, "explanation": "$360^\\circ \\times 24\\% = 86{,}4^\\circ$."},
                {"id": "d", "statement": "Tổng số tiền chi cho giáo dục và tiền nhà chiếm hơn $50\\%$ thu nhập.", "isCorrect": False, "explanation": "$24\\% + 20\\% = 44\\% < 50\\%$."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một khu rừng có 3 loại cây gỗ: Cây Keo chiếm góc ở tâm $144^\\circ$, Cây Bạch đàn chiếm $108^\\circ$, còn lại là Cây Thông. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Góc ở tâm biểu diễn Cây Thông là $108^\\circ$.", "isCorrect": True, "explanation": "$360^\\circ - 144^\\circ - 108^\\circ = 108^\\circ$."},
                {"id": "b", "statement": "Tỉ lệ phần trăm của Cây Keo trong khu rừng là $40\\%$.", "isCorrect": True, "explanation": "$144^\\circ / 360^\\circ = 40\\%$."},
                {"id": "c", "statement": "Số lượng Cây Bạch đàn và Cây Thông trong rừng là bằng nhau.", "isCorrect": True, "explanation": "Vì cùng có góc ở tâm là $108^\\circ$ (chiếm $30\\%$)."},
                {"id": "d", "statement": "Nếu rừng có tổng cộng 2000 cây thì số Cây Keo là 600 cây.", "isCorrect": False, "explanation": "Số Cây Keo $= 2000 \\times 40\\% = 800$ cây, không phải $600$ cây."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Góc ở tâm của hình quạt biểu diễn tỉ lệ $35\\%$ là bao nhiêu độ (điền số thập phân)?", "answer": 126, "unit": "độ"},
        {"id": 2, "level": "Vận dụng", "question": "Một thư viện có 600 bạn đọc đăng kí: Học sinh THCS chiếm 45%, Học sinh THPT chiếm 35%, còn lại là Giáo viên. Có bao nhiêu giáo viên đăng kí bạn đọc?", "answer": 120, "unit": "người"},
        {"id": 3, "level": "Vận dụng", "question": "Trong biểu đồ quạt tròn, phần thể hiện quả Cam có góc ở tâm là $72^\\circ$. Biết số quả Cam trong rổ là 24 quả. Tổng số quả trong rổ là bao nhiêu quả?", "answer": 120, "unit": "quả"},
        {"id": 4, "level": "Vận dụng cao", "question": "Biểu đồ quạt tròn gồm 3 phần A, B, C. Tỉ lệ của phần A gấp đôi phần B, phần B gấp đôi phần C. Tìm tỉ lệ phần trăm của phần A (làm tròn đến hàng phần mười, ví dụ 57.1).", "answer": 57.1, "unit": "%"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Một trường học phát động phong trào đọc sách. Số sách học sinh quyên góp được phân loại thành 4 nhóm:\n- Sách giáo khoa: 240 cuốn (chiếm 40%)\n- Truyện tranh: 180 cuốn\n- Sách khoa học: 120 cuốn\n- Báo, tạp chí: phần còn lại.\na) Tính tổng số sách quyên góp được của toàn trường.\nb) Tính tỉ lệ phần trăm của từng nhóm sách và tính góc ở tâm của nhóm Báo, tạp chí khi vẽ trên biểu đồ quạt tròn.",
            "maxScore": 1.0,
            "solution": "a) Tổng số sách quyên góp được là:\n$240 : 40\\% = 600$ (cuốn).\nb) Số lượng Báo, tạp chí là:\n$600 - (240 + 180 + 120) = 600 - 540 = 60$ (cuốn).\nTỉ lệ phần trăm của từng nhóm:\n- Sách giáo khoa: $40\\%$.\n- Truyện tranh: $\\frac{180}{600} \\times 100\\% = 30\\%$.\n- Sách khoa học: $\\frac{120}{600} \\times 100\\% = 20\\%$.\n- Báo, tạp chí: $\\frac{60}{600} \\times 100\\% = 10\\%$.\nGóc ở tâm của hình quạt biểu diễn Báo, tạp chí là:\n$360^\\circ \\times 10\\% = 36^\\circ$.",
            "rubric": [
                {"step": "Tính đúng tổng số sách 600 cuốn", "subScore": 0.4},
                {"step": "Tính đúng tỉ lệ các nhóm sách và góc ở tâm 36 độ", "subScore": 0.6}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Biểu đồ quạt tròn biểu diễn tỉ lệ học sinh tham gia 3 câu lạc bộ của trường:\n- CLB Thể thao: góc ở tâm $162^\\circ$\n- CLB Âm nhạc: góc ở tâm $126^\\circ$\n- CLB Mĩ thuật: phần còn lại.\nBiết CLB Mĩ thuật có 80 học sinh tham gia.\na) Tính tỉ lệ phần trăm học sinh tham gia từng câu lạc bộ.\nb) Tính tổng số học sinh tham gia cả 3 câu lạc bộ.",
            "maxScore": 1.0,
            "solution": "a) Góc ở tâm của CLB Mĩ thuật là:\n$360^\\circ - (162^\\circ + 126^\\circ) = 360^\\circ - 288^\\circ = 72^\\circ$.\nTỉ lệ phần trăm của từng CLB:\n- CLB Thể thao: $\\frac{162^\\circ}{360^\\circ} \\times 100\\% = 45\\%$.\n- CLB Âm nhạc: $\\frac{126^\\circ}{360^\\circ} \\times 100\\% = 35\\%$.\n- CLB Mĩ thuật: $\\frac{72^\\circ}{360^\\circ} \\times 100\\% = 20\\%$.\nb) Tổng số học sinh tham gia 3 CLB là:\n$80 : 20\\% = 80 : 0{,}2 = 400$ (học sinh).",
            "rubric": [
                {"step": "Tính đúng góc 72 độ và các tỉ lệ 45%, 35%, 20%", "subScore": 0.6},
                {"step": "Tính đúng tổng số 400 học sinh", "subScore": 0.4}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Năm 2023, doanh thu của một cửa hàng máy tính gồm 3 mảng: Laptop (50%), Điện thoại (30%), Phụ kiện (20%). Năm 2024, doanh thu Laptop tăng 20%, doanh thu Điện thoại tăng 10%, doanh thu Phụ kiện không đổi.\na) Hỏi tổng doanh thu năm 2024 tăng bao nhiêu phần trăm so với năm 2023?\nb) Tính tỉ lệ phần trăm của mảng Laptop trong cơ cấu doanh thu năm 2024.",
            "maxScore": 1.0,
            "solution": "a) Giả sử tổng doanh thu năm 2023 là 100 (đơn vị):\n- Doanh thu Laptop 2023: $50$.\n- Doanh thu Điện thoại 2023: $30$.\n- Doanh thu Phụ kiện 2023: $20$.\nDoanh thu từng mảng năm 2024:\n- Laptop 2024: $50 \\times (1 + 0{,}2) = 60$.\n- Điện thoại 2024: $30 \\times (1 + 0{,}1) = 33$.\n- Phụ kiện 2024: $20$.\nTổng doanh thu năm 2024 là: $60 + 33 + 20 = 113$.\nVậy tổng doanh thu năm 2024 tăng: $\\frac{113 - 100}{100} \\times 100\\% = 13\\%$ so với năm 2023.\nb) Tỉ lệ phần trăm của mảng Laptop trong cơ cấu doanh thu năm 2024 là:\n$P = \\frac{60}{113} \\times 100\\% \\approx 53{,}1\\%$.",
            "rubric": [
                {"step": "Thiết lập mô hình doanh thu và tính đúng mức tăng 13%", "subScore": 0.6},
                {"step": "Tính đúng tỉ lệ mới của Laptop xấp xỉ 53,1%", "subScore": 0.4}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c5_7_bai2_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 18: Biểu đồ hình quạt tròn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Biểu đồ quạt tròn biểu diễn cơ cấu nông nghiệp gồm: Trồng trọt, Chăn nuôi và Thủy sản. Biết góc ở tâm của Trồng trọt là $216^\\circ$, Chăn nuôi là $90^\\circ$. Tỉ lệ phần trăm của ngành Thủy sản là:", "options": ["$15\\%$", "$20\\%$", "$12\\%$", "$25\\%$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Để vẽ biểu đồ hình quạt tròn từ bảng số liệu có tỉ số $\\frac{3}{8}$, góc ở tâm tương ứng là:", "options": ["$135^\\circ$", "$120^\\circ$", "$150^\\circ$", "$145^\\circ$"], "correct": 0},
        {"id": 3, "level": "Vận dụng", "question": "Một người nông dân thu hoạch 12 tấn nông sản gồm 3 loại: Thóc 60%, Bắp 25%, Khoai 15%. Khối lượng thóc thu được nhiều hơn tổng khối lượng bắp và khoai là:", "options": ["$2{,}4$ tấn", "$1{,}2$ tấn", "$3{,}6$ tấn", "$4{,}8$ tấn"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cơ cấu dân số theo độ tuổi của một địa phương: Dưới 15 tuổi (20%), Từ 15 đến 64 tuổi (65%), Từ 65 tuổi trở lên (15%). Góc ở tâm của nhóm tuổi lao động (15 đến 64 tuổi) là:", "options": ["$234^\\circ$", "$240^\\circ$", "$220^\\circ$", "$216^\\circ$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Một hình quạt tròn có diện tích $15\\pi$ cm$^2$ trong một hình tròn có diện tích $60\\pi$ cm$^2$. Hình quạt đó biểu diễn tỉ lệ bao nhiêu phần trăm?", "options": ["$25\\%$", "$20\\%$", "$30\\%$", "$15\\%$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một xí nghiệp có 3 phân xưởng A, B, C. Tỉ lệ sản phẩm của xưởng A gấp 1,5 lần xưởng B; xưởng B gấp 2 lần xưởng C. Góc ở tâm biểu diễn phân xưởng A là:", "options": ["$180^\\circ$", "$150^\\circ$", "$200^\\circ$", "$120^\\circ$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Một trường học có tỉ lệ đỗ tốt nghiệp qua các mức Giỏi (30%), Khá (50%), Trung bình (20%). Nếu số học sinh Khá là 250 em thì số học sinh Giỏi là:", "options": ["$150$ em", "$100$ em", "$200$ em", "$125$ em"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho biểu đồ hình quạt tròn biểu diễn 4 thành phần A, B, C, D với tỉ số diện tích quạt tương ứng là $1 : 2 : 3 : 4$. Góc ở tâm của phần D là:", "options": ["$144^\\circ$", "$108^\\circ$", "$72^\\circ$", "$36^\\circ$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Một bể cá có 3 loại cá: Cá vàng, Cá chép và Cá bảy màu. Số cá vàng bằng $40\\%$ tổng số cá, số cá chép bằng $\\frac{2}{3}$ số cá còn lại. Tỉ lệ phần trăm của cá bảy màu là:", "options": ["$20\\%$", "$25\\%$", "$15\\%$", "$30\\%$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Hai hình quạt kề nhau trên biểu đồ tròn có góc ở tâm lần lượt là $\\alpha$ và $\\beta$ thỏa mãn $\\alpha + \\beta = 180^\\circ$ và $\\alpha - \\beta = 36^\\circ$. Tỉ lệ phần trăm tương ứng của hình quạt lớn là:", "options": ["$30\\%$", "$25\\%$", "$35\\%$", "$20\\%$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Số lượng vé bán ra của một rạp chiếu phim trong tuần gồm 3 mức giá: Vé VIP, Vé Thường, Vé Khuyến mãi. Biết số vé Thường gấp đôi vé VIP, số vé Khuyến mãi bằng $\\frac{1}{2}$ vé VIP. Tỉ lệ doanh số về số lượng vé VIP là:", "options": ["$\\frac{2}{7}$", "$\\frac{1}{3}$", "$\\frac{2}{5}$", "$\\frac{1}{4}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Sai lầm nào sau đây thường gặp nhất khi vẽ hoặc đọc biểu đồ hình quạt tròn?", "options": ["Tổng các tỉ lệ phần trăm ghi trên các quạt không bằng 100% hoặc vẽ sai tỉ lệ góc ở tâm", "Dùng màu sắc khác nhau cho các quạt", "Ghi tên chú giải rõ ràng", "Vẽ hình tròn bằng compa"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Biểu đồ hình quạt tròn biểu diễn thị phần của 4 hãng điện thoại thông minh: Hãng A (40%), Hãng B (25%), Hãng C (20%), Hãng D (15%). Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Góc ở tâm của hình quạt Hãng A là $144^\\circ$.", "isCorrect": True, "explanation": "$360^\\circ \\times 40\\% = 144^\\circ$."},
                {"id": "b", "statement": "Hiệu giữa góc ở tâm của Hãng B và Hãng D là $36^\\circ$.", "isCorrect": True, "explanation": "Chênh lệch tỉ lệ $= 25\\% - 15\\% = 10\\% \\Rightarrow 360^\\circ \\times 10\\% = 36^\\circ$."},
                {"id": "c", "statement": "Thị phần của Hãng A bằng tổng thị phần của Hãng B và Hãng D.", "isCorrect": True, "explanation": "$40\\% = 25\\% + 15\\%$."},
                {"id": "d", "statement": "Nếu Hãng C bán được 10 triệu chiếc thì Hãng A bán được 25 triệu chiếc.", "isCorrect": False, "explanation": "Hãng C chiếm 20% ứng với 10 triệu chiếc $\\Rightarrow$ tổng thị trường $= 50$ triệu. Hãng A chiếm 40% $\\Rightarrow 50 \\times 40\\% = 20$ triệu chiếc, không phải 25 triệu."}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho biểu đồ hình quạt tròn có 3 quạt với tỉ lệ phần trăm lần lượt là $x\\%, y\\%, z\\%$ ($x, y, z > 0$) thỏa mãn $x : y : z = 3 : 5 : 4$. Xét tính đúng/sai:",
            "statements": [
                {"id": "a", "statement": "Tổng số phần bằng nhau là $3 + 5 + 4 = 12$ phần.", "isCorrect": True, "explanation": "Tổng số phần tỉ lệ là 12."},
                {"id": "b", "statement": "Giá trị của $x$ là $25\\%$.", "isCorrect": True, "explanation": "$x = \\frac{3}{12} \\times 100\\% = 25\\%$."},
                {"id": "c", "statement": "Góc ở tâm lớn nhất là của hình quạt biểu diễn $y$, có số đo là $150^\\circ$.", "isCorrect": True, "explanation": "$y$ chiếm $\\frac{5}{12} \\times 360^\\circ = 150^\\circ$."},
                {"id": "d", "statement": "Góc ở tâm của hình quạt biểu diễn $z$ là $100^\\circ$.", "isCorrect": False, "explanation": "$z$ chiếm $\\frac{4}{12} \\times 360^\\circ = 120^\\circ$, không phải $100^\\circ$."}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Vận dụng", "question": "Một người chia số tiền 120 triệu đồng vào 3 quỹ: Đầu tư, Tiết kiệm, Tiêu dùng theo tỉ lệ $5 : 3 : 2$. Số tiền dành cho quỹ Đầu tư là bao nhiêu triệu đồng?", "answer": 60, "unit": "triệu đồng"},
        {"id": 2, "level": "Vận dụng", "question": "Góc ở tâm của hình quạt thứ nhất là $120^\\circ$, của hình quạt thứ hai là $90^\\circ$, phần còn lại là của hình quạt thứ ba. Hỏi hình quạt thứ ba chiếm bao nhiêu phần trăm tổng thể (điền số thập phân, ví dụ 41.7)?", "answer": 41.7, "unit": "%"},
        {"id": 3, "level": "Vận dụng cao", "question": "Một công ty có doanh thu từ nội địa và xuất khẩu. Doanh thu xuất khẩu gấp 3 lần nội địa. Hỏi trên biểu đồ hình quạt tròn, góc ở tâm biểu diễn doanh thu xuất khẩu là bao nhiêu độ?", "answer": 270, "unit": "độ"},
        {"id": 4, "level": "Vận dụng cao", "question": "Biểu đồ quạt tròn biểu diễn 3 thành phần A, B, C. Biết diện tích hình quạt A hơn hình quạt B là $10\\%$, diện tích hình quạt B hơn hình quạt C là $10\\%$. Tính số đo góc ở tâm (độ) của hình quạt A.", "answer": 156, "unit": "độ"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng cao",
            "question": "Một công ty công nghệ có 3 nhóm nghiên cứu: Nhóm Trí tuệ nhân tạo (AI), Nhóm An ninh mạng (Cyber), Nhóm Ứng dụng di động (Mobile).\nBiết số nhân sự nhóm AI gấp đôi nhóm Mobile, nhóm Cyber nhiều hơn nhóm Mobile là 10 người. Tổng số nhân sự của công ty là 130 người.\na) Tính số nhân sự của mỗi nhóm.\nb) Tính góc ở tâm của từng nhóm khi biểu diễn trên biểu đồ hình quạt tròn (làm tròn đến hàng đơn vị độ).",
            "maxScore": 1.0,
            "solution": "a) Gọi số nhân sự nhóm Mobile là $x$ ($x \\in \\mathbb{N}^*$).\nKhi đó số nhân sự nhóm AI là $2x$, nhóm Cyber là $x + 10$.\nTổng số nhân sự là 130 người nên:\n$x + 2x + (x + 10) = 130 \\Leftrightarrow 4x + 10 = 130 \\Leftrightarrow 4x = 120 \\Leftrightarrow x = 30$.\nSố nhân sự của từng nhóm:\n- Nhóm Mobile: 30 người.\n- Nhóm AI: $2 \\times 30 = 60$ người.\n- Nhóm Cyber: $30 + 10 = 40$ người.\nb) Tỉ lệ và góc ở tâm tương ứng:\n- Nhóm AI: chiếm $\\frac{60}{130} \\approx 46{,}15\\% \\Rightarrow$ Góc ở tâm: $360^\\circ \\times \\frac{60}{130} \\approx 166^\\circ$.\n- Nhóm Cyber: chiếm $\\frac{40}{130} \\approx 30{,}77\\% \\Rightarrow$ Góc ở tâm: $360^\\circ \\times \\frac{40}{130} \\approx 111^\\circ$.\n- Nhóm Mobile: chiếm $\\frac{30}{130} \\approx 23{,}08\\% \\Rightarrow$ Góc ở tâm: $360^\\circ \\times \\frac{30}{130} \\approx 83^\\circ$.\nKiểm tra tổng góc: $166^\\circ + 111^\\circ + 83^\\circ = 360^\\circ$.",
            "rubric": [
                {"step": "Thiết lập phương trình tìm đúng số người: Mobile 30, AI 60, Cyber 40", "subScore": 0.5},
                {"step": "Tính đúng các góc ở tâm xấp xỉ 166 độ, 111 độ, 83 độ", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Năm trước, tỉ lệ học sinh Giỏi, Khá, Trung bình của một trường THCS lần lượt là 20%, 50%, 30%. Năm nay, nhà trường đổi mới phương pháp giảng dạy nên số học sinh Giỏi tăng 50%, số học sinh Khá tăng 20%, số học sinh Trung bình giảm 40% (tổng số học sinh toàn trường không đổi).\na) Hỏi nhận định \"tổng số học sinh không đổi\" có phù hợp với số liệu trên không? Hãy chứng minh.\nb) Tính cơ cấu tỉ lệ phần trăm mới của 3 nhóm học sinh năm nay.",
            "maxScore": 1.0,
            "solution": "a) Giả sử tổng số học sinh năm trước là $100$ em:\n- Giỏi: 20 em; Khá: 50 em; Trung bình: 30 em.\nNăm nay:\n- Số học sinh Giỏi mới: $20 \\times (1 + 0{,}5) = 30$ em.\n- Số học sinh Khá mới: $50 \\times (1 + 0{,}2) = 60$ em.\n- Số học sinh Trung bình mới: $30 \\times (1 - 0{,}4) = 18$ em.\nTổng số học sinh năm nay là: $30 + 60 + 18 = 108$ em.\nNhư vậy tổng số học sinh đã tăng từ 100 lên 108 em (tăng 8%), do đó nhận định \"tổng số học sinh toàn trường không đổi\" là mâu thuẫn với tỉ lệ thay đổi của các nhóm trên thực tế.\nb) Để tính cơ cấu phần trăm mới trên tổng số học sinh mới (108 em):\n- Tỉ lệ Giỏi mới: $\\frac{30}{108} \\times 100\\% \\approx 27{,}8\\%$.\n- Tỉ lệ Khá mới: $\\frac{60}{108} \\times 100\\% \\approx 55{,}6\\%$.\n- Tỉ lệ Trung bình mới: $\\frac{18}{108} \\times 100\\% \\approx 16{,}7\\%$.\nTổng tỉ lệ mới $= 27{,}8\\% + 55{,}6\\% + 16{,}7\\% \\approx 100\\%$.",
            "rubric": [
                {"step": "Chứng minh số liệu dẫn tới tổng số học sinh tăng từ 100 lên 108", "subScore": 0.5},
                {"step": "Tính đúng cơ cấu phần trăm mới: Giỏi 27,8%, Khá 55,6%, TB 16,7%", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho biểu đồ hình quạt tròn biểu diễn phân bổ ngân sách 3 dự án A, B, C. Góc ở tâm của dự án A là $\\alpha$, dự án B là $\\beta$, dự án C là $\\gamma$. Biết $\\alpha, \\beta, \\gamma$ lập thành một cấp số cộng thỏa mãn $\\alpha < \\beta < \\gamma$ và góc lớn nhất gấp 3 lần góc nhỏ nhất ($\\gamma = 3\\alpha$).\na) Tìm số đo các góc $\\alpha, \\beta, \\gamma$.\nb) Dự án A được cấp 15 tỷ đồng. Tính tổng ngân sách cấp cho cả 3 dự án.",
            "maxScore": 1.0,
            "solution": "a) Vì $\\alpha, \\beta, \\gamma$ tạo thành cấp số cộng nên $\\alpha + \\gamma = 2\\beta$.\nTổng 3 góc ở tâm của biểu đồ tròn là: $\\alpha + \\beta + \\gamma = 360^\\circ$.\nThay $\\alpha + \\gamma = 2\\beta$ vào: $2\\beta + \\beta = 360^\\circ \\Leftrightarrow 3\\beta = 360^\\circ \\Rightarrow \\beta = 120^\\circ$.\nSuy ra: $\\alpha + \\gamma = 240^\\circ$.\nMặt khác, $\\gamma = 3\\alpha$, do đó: $\\alpha + 3\\alpha = 240^\\circ \\Leftrightarrow 4\\alpha = 240^\\circ \\Rightarrow \\alpha = 60^\\circ$.\nSuy ra: $\\gamma = 3 \\times 60^\\circ = 180^\\circ$.\nVậy ba góc ở tâm là $\\alpha = 60^\\circ, \\beta = 120^\\circ, \\gamma = 180^\\circ$.\nb) Tỉ lệ ngân sách của dự án A là:\n$P_A = \\frac{60^\\circ}{360^\\circ} = \\frac{1}{6}$.\nTổng ngân sách của cả 3 dự án là:\n$15 : \\frac{1}{6} = 15 \\times 6 = 90$ (tỷ đồng).",
            "rubric": [
                {"step": "Tìm đúng beta = 120 độ, alpha = 60 độ, gamma = 180 độ", "subScore": 0.6},
                {"step": "Tính đúng tổng ngân sách là 90 tỷ đồng", "subScore": 0.4}
            ]
        }
    ]
}
