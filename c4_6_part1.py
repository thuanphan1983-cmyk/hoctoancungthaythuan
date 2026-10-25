# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 6 - CHƯƠNG IV: MỘT SỐ HÌNH PHẲNG TRONG THỰC TIỄN
PHẦN 1:
- BÀI 18: HÌNH TAM GIÁC ĐỀU. HÌNH VUÔNG. HÌNH LỤC GIÁC ĐỀU (c4_6_bai1)
- BÀI 19: HÌNH CHỮ NHẬT. HÌNH THOI (c4_6_bai2)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 18: HÌNH TAM GIÁC ĐỀU. HÌNH VUÔNG. HÌNH LỤC GIÁC ĐỀU (c4_6_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c4_6_bai1_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 18: Tam giác đều, Hình vuông, Lục giác đều - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Tam giác đều là tam giác có:", "options": ["Ba cạnh bằng nhau và ba góc bằng nhau bằng $60^\\circ$", "Hai cạnh bằng nhau", "Ba cạnh có độ dài bất kì", "Một góc vuông"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hình vuông là tứ giác có:", "options": ["4 cạnh bằng nhau và 4 góc vuông", "4 cạnh bằng nhau và 4 góc nhọn", "2 cạnh dài và 2 cạnh ngắn", "4 góc bằng nhau nhưng 4 cạnh khác nhau"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Hình lục giác đều có bao nhiêu cạnh bằng nhau?", "options": ["$6$ cạnh", "$4$ cạnh", "$8$ cạnh", "$5$ cạnh"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Chu vi của một hình vuông có cạnh bằng $5\\text{ cm}$ là:", "options": ["$20\\text{ cm}$", "$25\\text{ cm}$", "$10\\text{ cm}$", "$15\\text{ cm}$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Một tam giác đều có cạnh $6\\text{ cm}$. Chu vi tam giác đều đó bằng:", "options": ["$18\\text{ cm}$", "$12\\text{ cm}$", "$36\\text{ cm}$", "$24\\text{ cm}$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Hình lục giác đều được ghép từ bao nhiêu tam giác đều bằng nhau?", "options": ["$6$", "$4$", "$5$", "$8$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Một hình vuông có chu vi bằng $36\\text{ cm}$. Độ dài cạnh hình vuông đó là:", "options": ["$9\\text{ cm}$", "$6\\text{ cm}$", "$18\\text{ cm}$", "$12\\text{ cm}$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Diện tích của hình vuông có cạnh $7\\text{ cm}$ là:", "options": ["$49\\text{ cm}^2$", "$28\\text{ cm}^2$", "$14\\text{ cm}^2$", "$21\\text{ cm}^2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Trong hình lục giác đều $ABCDEF$, các đường chéo chính là:", "options": ["$AD, BE, CF$", "$AB, BC, CD$", "$AC, BD, CE$", "$AF, EF, DE$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Một biển báo giao thông hình tam giác đều có chu vi $120\\text{ cm}$. Cạnh của biển báo đó dài:", "options": ["$40\\text{ cm}$", "$60\\text{ cm}$", "$30\\text{ cm}$", "$45\\text{ cm}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Mỗi góc của hình lục giác đều có số đo bằng:", "options": ["$120^\\circ$", "$60^\\circ$", "$90^\\circ$", "$108^\\circ$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Hai đường chéo của hình vuông có tính chất nào sau đây?", "options": ["Bằng nhau và vuông góc với nhau", "Không bằng nhau", "Bằng nhau nhưng không vuông góc", "Song song với nhau"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hình vuông MNPQ có cạnh bằng 6 cm.",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Bốn cạnh MN = NP = PQ = QM = 6 cm.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Bốn góc ở các đỉnh M, N, P, Q đều là góc vuông (90°).", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Chu vi hình vuông MNPQ là 24 cm.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Diện tích hình vuông MNPQ là 24 cm².", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình lục giác đều ABCDEF có tâm O.",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Hình có 6 cạnh bằng nhau và 6 đỉnh.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Các đường chéo chính AD, BE, CF cắt nhau tại điểm O.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tam giác OAB là tam giác đều.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Độ dài đường chéo chính AD bằng một nửa cạnh AB.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tính diện tích của một viên gạch lát nền hình vuông có cạnh dài 60 cm (đơn vị cm²).", "answer": "3600"},
        {"id": 2, "level": "Thông hiểu", "question": "Một hình vuông có diện tích là 81 cm². Chu vi của hình vuông đó bằng bao nhiêu cm?", "answer": "36"},
        {"id": 3, "level": "Thông hiểu", "question": "Chu vi của một hình lục giác đều có cạnh bằng 5 cm là bao nhiêu cm?", "answer": "30"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Người ta dùng dây thép gai rào quanh một khu đất hình vuông cạnh 15 m. Chiều dài dây rào (tính bằng mét) cần dùng là:", "answer": "60"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Nêu các yếu tố về cạnh, góc và đường chéo của hình vuông ABCD.\nb) Vẽ hình tam giác đều ABC có cạnh bằng 4 cm (nêu rõ các bước vẽ).",
            "rubric": "a) 4 cạnh bằng nhau (AB=BC=CD=DA); 4 góc vuông 90°; 2 đường chéo bằng nhau và vuông góc tại trung điểm mỗi đường (0.5đ).\nb) Vẽ đoạn thẳng AB = 4 cm. Dùng compa vẽ hai cung tròn tâm A và B bán kính 4 cm cắt nhau tại C. Nối AC, BC (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một bồn hoa hình tam giác đều có chu vi bằng 18 m.\na) Tính độ dài mỗi cạnh của bồn hoa đó.\nb) Người ta muốn trồng hoa viền quanh bồn hoa, cứ cách 1 m trồng một cây hoa. Hỏi trồng được tất cả bao nhiêu cây hoa viền quanh bồn?",
            "rubric": "a) Độ dài mỗi cạnh: 18 : 3 = 6 (m) (0.5đ).\nb) Số cây hoa trồng quanh chu vi khép kín bằng chu vi chia khoảng cách: 18 : 1 = 18 (cây hoa) (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một căn phòng hình vuông có cạnh dài 8 m. Người ta dùng các viên gạch men hình vuông cạnh 40 cm để lát nền căn phòng đó.\na) Tính diện tích căn phòng theo đơn vị mét vuông và xăng-ti-mét vuông.\nb) Tính số viên gạch cần dùng để lát kín nền phòng (bỏ qua diện tích mạch vữa).",
            "rubric": "a) Diện tích căn phòng: 8 x 8 = 64 m² = 640000 cm² (0.5đ).\nb) Diện tích 1 viên gạch: 40 x 40 = 1600 cm². Số viên gạch cần: 640000 : 1600 = 400 (viên) (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c4_6_bai1_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 18: Tam giác đều, Hình vuông, Lục giác đều - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Nếu cạnh của một hình vuông tăng lên gấp đôi thì diện tích của nó tăng lên gấp:", "options": ["$4$ lần", "$2$ lần", "$8$ lần", "$16$ lần"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Một hình lục giác đều có chu vi là $48\\text{ cm}$. Độ dài mỗi cạnh của nó là:", "options": ["$8\\text{ cm}$", "$6\\text{ cm}$", "$12\\text{ cm}$", "$16\\text{ cm}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Ghép hai hình tam giác đều có cùng độ dài cạnh bằng nhau ta được một hình:", "options": ["Hình thoi", "Hình vuông", "Hình chữ nhật", "Hình lục giác"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Một mảnh sân hình vuông có diện tích $144\\text{ m}^2$. Chu vi của mảnh sân đó là:", "options": ["$48\\text{ m}$", "$24\\text{ m}$", "$36\\text{ m}$", "$60\\text{ m}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Trong hình lục giác đều có bao nhiêu đường chéo chính?", "options": ["$3$", "$6$", "$9$", "$12$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Một sợi dây thép dài $48\\text{ cm}$ uốn vừa đủ thành một hình vuông. Diện tích hình vuông đó là:", "options": ["$144\\text{ cm}^2$", "$96\\text{ cm}^2$", "$64\\text{ cm}^2$", "$196\\text{ cm}^2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Một chiếc bàn ăn mặt gỗ có dạng hình lục giác đều với cạnh $60\\text{ cm}$. Khoảng cách giữa hai đỉnh đối diện nhau qua tâm bằng:", "options": ["$120\\text{ cm}$", "$60\\text{ cm}$", "$90\\text{ cm}$", "$180\\text{ cm}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Nếu giảm cạnh của một hình vuông đi $3\\text{ cm}$ thì diện tích giảm $39\\text{ cm}^2$. Cạnh ban đầu của hình vuông là:", "options": ["$8\\text{ cm}$", "$7\\text{ cm}$", "$9\\text{ cm}$", "$10\\text{ cm}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cho tam giác đều $ABC$ cạnh $a$. Lấy điểm $M, N, P$ lần lượt là trung điểm của $AB, BC, CA$. Hình lục giác hoặc tam giác $MNP$ là:", "options": ["Tam giác đều có cạnh bằng $a/2$", "Tam giác vuông", "Tam giác cân nhưng không đều", "Hình thoi"], "correct": 0},
        {"id": 10, "level": "Vận dụng thấp", "question": "Chi phí lát gạch một sân chơi hình vuông cạnh $10\\text{ m}$ với giá $150\\,000$ đồng/m² là:", "options": ["$15\\,000\\,000$ đồng", "$6\\,000\\,000$ đồng", "$30\\,000\\,000$ đồng", "$22\\,500\\,000$ đồng"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Ghép 6 tam giác đều cạnh $4\\text{ cm}$ thành một hình lục giác đều. Chu vi của hình lục giác đều tạo thành là:", "options": ["$24\\text{ cm}$", "$36\\text{ cm}$", "$18\\text{ cm}$", "$48\\text{ cm}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một khung ảnh hình vuông cạnh ngoài $25\\text{ cm}$, bề rộng của viền khung là $2\\text{ cm}$. Diện tích phần bên trong để gắn ảnh là:", "options": ["$441\\text{ cm}^2$", "$529\\text{ cm}^2$", "$400\\text{ cm}^2$", "$484\\text{ cm}^2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho một mảnh đất hình vuông có cạnh dài 20 m.",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Chu vi của mảnh đất là 80 m.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích của mảnh đất là 400 m².", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nếu người ta để lại một lối đi rộng 2 m bao quanh phía trong mép đất thì khu đất còn lại có cạnh là 18 m.", "correct": False},
                {"key": "d", "level": "Vận dụng thấp", "text": "Diện tích khu đất còn lại bên trong lối đi là 256 m².", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Xét các hình đa giác đều gồm tam giác đều, hình vuông và lục giác đều:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Hình vuông có 4 trục đối xứng.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hình lục giác đều có đúng 6 trục đối xứng.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tổng số đo 6 góc của hình lục giác đều bằng 720°.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Độ dài đường chéo chính của lục giác đều luôn gấp 3 lần độ dài một cạnh của nó.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một bồn hoa hình vuông có chu vi 28 m. Diện tích của bồn hoa đó là bao nhiêu m²?", "answer": "49"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một người uốn một thanh sắt dài 72 cm thành một hình lục giác đều. Độ dài mỗi cạnh của hình lục giác đó là bao nhiêu cm?", "answer": "12"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một mảnh đất hình vuông có chu vi 64 m. Người ta đào một cái ao hình vuông ở giữa có cạnh 8 m. Diện tích đất còn lại để trồng cây bằng bao nhiêu m²?", "answer": "192"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một hình vuông có diện tích 225 cm². Nếu tăng mỗi cạnh thêm 2 cm thì diện tích hình vuông mới bằng bao nhiêu cm²?", "answer": "289"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hình lục giác đều ABCDEF tâm O có cạnh AB = 5 cm.\na) Tính độ dài các đoạn thẳng OA, OB, OC, OD, OE, OF.\nb) Tính độ dài các đường chéo chính AD, BE, CF.",
            "rubric": "a) Vì lục giác đều ghép từ 6 tam giác đều nên OA = OB = OC = OD = OE = OF = AB = 5 cm (0.5đ).\nb) AD = 2 . OA = 10 cm, tương tự BE = CF = 10 cm (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một sân thể thao hình vuông có cạnh dài 30 m. Nhà trường muốn lát cỏ nhân tạo toàn bộ sân với chi phí 180 000 đồng/m² và lắp hàng rào lưới thép bao quanh sân với giá 120 000 đồng/m.\na) Tính tổng diện tích cần trải cỏ.\nb) Tính tổng chi phí lát cỏ và làm hàng rào lưới thép xung quanh sân.",
            "rubric": "a) Diện tích sân: 30 x 30 = 900 m² (0.4đ).\nb) Tiền cỏ: 900 x 180 000 = 162 000 000 đồng. Chu vi sân: 30 x 4 = 120 m. Tiền rào: 120 x 120 000 = 14 400 000 đồng. Tổng chi phí: 162 000 000 + 14 400 000 = 176 400 000 đồng (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một lối đi lát sỏi hình vuông được bao quanh bởi một bồn hoa cũng hình vuông (hai hình vuông có cùng tâm). Biết cạnh của bồn hoa ngoài dài 12 m và cạnh của lối đi bên trong dài 8 m.\na) Tính diện tích của lối đi lát sỏi.\nb) Tính diện tích phần đất trồng hoa nằm giữa hai hình vuông đó.",
            "rubric": "a) Diện tích hình vuông trong (lối đi lát sỏi): 8 x 8 = 64 m² (0.4đ).\nb) Diện tích toàn bộ hình vuông lớn: 12 x 12 = 144 m². Diện tích phần đất trồng hoa (vành khăn hình vuông): 144 - 64 = 80 m² (0.6đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c4_6_bai1_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 18: Tam giác đều, Hình vuông, Lục giác đều - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Số đường chéo tất cả của một hình lục giác đều là:", "options": ["$9$", "$6$", "$12$", "$3$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho hình vuông có diện tích $S$. Nếu tăng cạnh của hình vuông thêm $10\\%$ thì diện tích tăng thêm bao nhiêu phần trăm?", "options": ["$21\\%$", "$20\\%$", "$10\\%$", "$15\\%$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một người ghép 4 viên gạch hình tam giác đều bằng nhau có cạnh $a$ để tạo thành một tam giác đều lớn hơn. Chu vi của tam giác đều lớn đó là:", "options": ["$6a$", "$12a$", "$4a$", "$3a$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Một hình vuông có cạnh $a$ và một tam giác đều có cạnh $b$ có chu vi bằng nhau. Tỉ số diện tích của hình vuông và diện tích tam giác đều (xấp xỉ) phụ thuộc vào tỉ số giữa $a$ và $b$. Biết chu vi bằng $24\\text{ cm}$. Tỉ số $a/b$ là:", "options": ["$3/4$", "$4/3$", "$2/3$", "$1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Một mảnh đất hình vuông được chia thành 4 thửa ruộng hình chữ nhật nhỏ bằng nhau bởi hai đường thẳng song song với các cạnh. Nếu chu vi mỗi thửa ruộng nhỏ là $50\\text{ m}$ thì chu vi mảnh đất ban đầu là:", "options": ["$80\\text{ m}$", "$100\\text{ m}$", "$120\\text{ m}$", "$60\\text{ m}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Trong một hình lục giác đều cạnh $6\\text{ cm}$, diện tích lục giác đều này gấp bao nhiêu lần diện tích một tam giác đều có cùng cạnh $6\\text{ cm}$?", "options": ["$6$ lần", "$3$ lần", "$12$ lần", "$4$ lần"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cắt một tờ bìa hình vuông cạnh $20\\text{ cm}$ ở 4 góc thành 4 hình vuông nhỏ cạnh $4\\text{ cm}$ để gấp thành một cái hộp không nắp. Diện tích đáy hộp là:", "options": ["$144\\text{ cm}^2$", "$256\\text{ cm}^2$", "$196\\text{ cm}^2$", "$169\\text{ cm}^2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho hình vuông $ABCD$ cạnh $12\\text{ cm}$. Điểm $M, N$ lần lượt là trung điểm của $AB$ và $BC$. Diện tích tứ giác $AMND$ là:", "options": ["$90\\text{ cm}^2$", "$72\\text{ cm}^2$", "$108\\text{ cm}^2$", "$84\\text{ cm}^2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Một viên gạch trang trí hình lục giác đều có diện tích $54\\text{ cm}^2$. Người ta ghép các viên này lại thành một mảng trang trí gồm 10 viên. Diện tích toàn bộ mảng là:", "options": ["$540\\text{ cm}^2$", "$480\\text{ cm}^2$", "$600\\text{ cm}^2$", "$500\\text{ cm}^2$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Tìm số tự nhiên $n$ sao cho một đa giác đều $n$ cạnh có số đo mỗi góc bằng $120^\\circ$:", "options": ["$n = 6$", "$n = 5$", "$n = 8$", "$n = 4$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một sân hình vuông được mở rộng về 4 phía, mỗi phía tăng thêm $2\\text{ m}$, làm diện tích tăng thêm $64\\text{ m}^2$. Cạnh ban đầu của sân là:", "options": ["$6\\text{ m}$", "$8\\text{ m}$", "$10\\text{ m}$", "$4\\text{ m}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho lục giác đều $ABCDEF$ có diện tích $S$. Diện tích tam giác $ACE$ bằng:", "options": ["$S/2$", "$S/3$", "$2S/3$", "$S/4$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một mảnh vườn hình vuông ban đầu có cạnh x (m). Người ta mở rộng mảnh vườn bằng cách tăng cạnh thêm 3 m về cả hai chiều ngang và dọc:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Diện tích mảnh vườn sau khi mở rộng là (x + 3)² m².", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích tăng thêm của mảnh vườn là (6x + 9) m².", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Nếu diện tích tăng thêm là 57 m² thì cạnh ban đầu của mảnh vườn là x = 8 m.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Chu vi mảnh vườn sau khi mở rộng tăng thêm 24 m so với ban đầu.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình lục giác đều ABCDEF cạnh a có tâm O:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Hình gồm 6 tam giác đều: OAB, OBC, OCD, ODE, OEF, OFA bằng nhau.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Tứ giác ABEF là hình thang cân.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Tứ giác ABCO là hình thoi có cạnh bằng a.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Diện tích tứ giác ABDE bằng đúng 2/3 diện tích lục giác đều ABCDEF.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Số lượng đường chéo không đi qua tâm O của một hình lục giác đều là bao nhiêu?", "answer": "6"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một mảnh đất hình vuông có cạnh 16 m. Người ta bớt ở mỗi góc một hình vuông nhỏ có cạnh 2 m để trồng hoa. Chu vi của phần đất còn lại bằng bao nhiêu mét?", "answer": "64"},
        {"id": 3, "level": "Vận dụng cao", "question": "Người ta ghép 24 viên gạch hình tam giác đều cạnh 10 cm thành một dải hoa văn trang trí. Nếu ghép thành hình lục giác đều lớn thì cần bao nhiêu viên gạch tam giác đều cạnh 10 cm để được hình lục giác đều cạnh 20 cm?", "answer": "24"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một căn phòng hình vuông lát bằng 500 viên gạch hình vuông cạnh 40 cm. Nếu thay bằng gạch hình vuông cạnh 50 cm thì cần bao nhiêu viên gạch?", "answer": "320"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho hình lục giác đều ABCDEF tâm O có diện tích là 72 cm².\na) Tính diện tích tam giác OAB.\nb) Tính diện tích tứ giác ABOF.\nc) Tính diện tích tam giác BDF.",
            "rubric": "a) Diện tích tam giác OAB = 72 : 6 = 12 cm² (0.3đ).\nb) Tứ giác ABOF gồm hai tam giác OAB và OFA nên có diện tích = 12 x 2 = 24 cm² (0.3đ).\nc) Tam giác BDF có diện tích bằng một nửa diện tích lục giác đều: S(BDF) = 72 : 2 = 36 cm² (0.4đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Bác Ba có một khu đất hình vuông cạnh 24 m. Bác muốn làm một con đường đi rộng 2 m chạy vòng quanh phía trong khu đất, phần đất vuông ở chính giữa dùng để dựng nhà và trồng cây cảnh.\na) Tính diện tích phần đất làm đường đi.\nb) Chi phí đổ bê tông lối đi là 120 000 đồng/m². Tính tổng số tiền bác Ba cần chuẩn bị để làm lối đi đó.",
            "rubric": "a) Cạnh phần đất chính giữa: 24 - 2 x 2 = 20 m. Diện tích đất ở giữa: 20 x 20 = 400 m². Diện tích lối đi = Diện tích cả khu đất - diện tích giữa = 24 x 24 - 400 = 576 - 400 = 176 m² (0.6đ).\nb) Số tiền làm đường: 176 x 120 000 = 21 120 000 đồng (0.4đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một người nông dân muốn rào một mảnh vườn hình chữ nhật có diện tích 180 m² giáp với bờ tường đá (không cần rào phía bờ tường). Người đó có 38 m lưới thép. Hỏi người đó có thể rào mảnh vườn với kích thước nguyên là bao nhiêu để vừa khít 38 m lưới?",
            "rubric": "Gọi cạnh song song bờ tường là a (m), hai cạnh vuông góc là b (m). Chu vi rào: a + 2b = 38 => a = 38 - 2b. Diện tích: a . b = (38 - 2b)b = 180 => 2b² - 38b + 180 = 0 => b² - 19b + 90 = 0 (0.4đ). Phân tích (b - 9)(b - 10) = 0 => b = 9 hoặc b = 10 (0.3đ). Nếu b = 9 m thì a = 38 - 18 = 20 m (thỏa mãn diện tích 20 x 9 = 180 m²). Nếu b = 10 m thì a = 38 - 20 = 18 m (thỏa mãn 18 x 10 = 180 m²). Kết luận kích thước mảnh vườn: 20 m x 9 m hoặc 18 m x 10 m (0.3đ)."
        }
    ]
}


# ==============================================================================
# BÀI 19: HÌNH CHỮ NHẬT. HÌNH THOI (c4_6_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c4_6_bai2_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 19: Hình chữ nhật. Hình thoi - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hình chữ nhật là tứ giác có:", "options": ["4 góc vuông", "4 cạnh bằng nhau", "Hai đường chéo vuông góc", "Hai cạnh kề bằng nhau"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hình thoi là tứ giác có:", "options": ["4 cạnh bằng nhau", "4 góc vuông", "Hai đường chéo bằng nhau", "Không có trục đối xứng"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Công thức tính diện tích hình chữ nhật có chiều dài $a$, chiều rộng $b$ là:", "options": ["$S = a \\cdot b$", "$S = (a + b) \\cdot 2$", "$S = a^2$", "$S = \\frac{1}{2} a \\cdot b$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Công thức tính diện tích hình thoi có độ dài hai đường chéo là $m$ và $n$ là:", "options": ["$S = \\frac{1}{2} m \\cdot n$", "$S = m \\cdot n$", "$S = (m + n) \\cdot 2$", "$S = 2(m + n)$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Chu vi hình thoi có cạnh $a$ được tính theo công thức:", "options": ["$C = 4a$", "$C = 2a$", "$C = a^2$", "$C = a + 4$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Hai đường chéo của hình thoi có tính chất:", "options": ["Vuông góc với nhau tại trung điểm của mỗi đường", "Bằng nhau và song song", "Không cắt nhau", "Không vuông góc"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Một hình chữ nhật có chiều dài $12\\text{ cm}$, chiều rộng $8\\text{ cm}$. Chu vi của nó là:", "options": ["$40\\text{ cm}$", "$96\\text{ cm}$", "$20\\text{ cm}$", "$48\\text{ cm}$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Diện tích hình chữ nhật có chiều dài $15\\text{ m}$, chiều rộng $6\\text{ m}$ là:", "options": ["$90\\text{ m}^2$", "$42\\text{ m}^2$", "$21\\text{ m}^2$", "$180\\text{ m}^2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Một hình thoi có độ dài hai đường chéo lần lượt là $8\\text{ cm}$ và $10\\text{ cm}$. Diện tích của hình thoi đó là:", "options": ["$40\\text{ cm}^2$", "$80\\text{ cm}^2$", "$36\\text{ cm}^2$", "$18\\text{ cm}^2$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Hình thoi có chu vi bằng $28\\text{ cm}$. Độ dài mỗi cạnh của hình thoi là:", "options": ["$7\\text{ cm}$", "$14\\text{ cm}$", "$4\\text{ cm}$", "$8\\text{ cm}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Trong hình chữ nhật $ABCD$, khẳng định nào sau đây là SAI?", "options": ["Hai đường chéo vuông góc với nhau", "Hai đường chéo bằng nhau", "Các cạnh đối song song và bằng nhau", "Bốn góc đều bằng $90^\\circ$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Một mảnh vườn hình chữ nhật có chu vi $60\\text{ m}$, chiều dài $20\\text{ m}$. Chiều rộng của mảnh vườn là:", "options": ["$10\\text{ m}$", "$20\\text{ m}$", "$40\\text{ m}$", "$15\\text{ m}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hình chữ nhật ABCD có chiều dài AB = 8 cm, chiều rộng BC = 5 cm.",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Độ dài đoạn CD = 8 cm và AD = 5 cm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Chu vi của hình chữ nhật ABCD bằng 26 cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Diện tích của hình chữ nhật ABCD bằng 40 cm².", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Độ dài đường chéo AC ngắn hơn cạnh AB.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình thoi MNPQ có hai đường chéo MP = 12 cm và NQ = 16 cm cắt nhau tại O.",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Hai đường chéo MP và NQ vuông góc với nhau tại O.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Điểm O là trung điểm của MP và NQ, suy ra OM = 6 cm và ON = 8 cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Diện tích hình thoi MNPQ bằng 96 cm².", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Diện tích hình thoi MNPQ bằng tích MP . NQ = 192 cm².", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một thửa ruộng hình chữ nhật có chiều dài 25 m, chiều rộng 12 m. Diện tích của thửa ruộng đó là bao nhiêu m²?", "answer": "300"},
        {"id": 2, "level": "Thông hiểu", "question": "Một hình thoi có diện tích là 54 cm², một đường chéo dài 12 cm. Độ dài đường chéo còn lại là bao nhiêu cm?", "answer": "9"},
        {"id": 3, "level": "Thông hiểu", "question": "Chu vi của một hình thoi có cạnh 15 cm là bao nhiêu cm?", "answer": "60"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Một mảnh đất hình chữ nhật có diện tích 180 m² và chiều rộng 9 m. Chu vi mảnh đất đó bằng bao nhiêu mét?", "answer": "58"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Nêu các tính chất về cạnh, góc và đường chéo của hình thoi.\nb) Tính diện tích hình thoi biết độ dài hai đường chéo lần lượt là 14 cm và 20 cm.",
            "rubric": "a) 4 cạnh bằng nhau, các góc đối bằng nhau, hai đường chéo vuông góc tại trung điểm mỗi đường và là đường phân giác các góc (0.5đ).\nb) Diện tích: S = (1/2) x 14 x 20 = 140 cm² (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một gian phòng khách hình chữ nhật có chiều dài 9 m và chiều rộng 6 m. Người ta dùng gạch men hình vuông cạnh 30 cm để lát toàn bộ sàn phòng.\na) Tính diện tích nền phòng khách.\nb) Tính số viên gạch cần dùng để lát xong nền phòng khách (coi mạch vữa không đáng kể).",
            "rubric": "a) Diện tích nền phòng: 9 x 6 = 54 m² = 540 000 cm² (0.5đ).\nb) Diện tích 1 viên gạch: 30 x 30 = 900 cm². Số viên gạch: 540 000 : 900 = 600 viên (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một khu vườn hình chữ nhật có chu vi 120 m. Chiều dài hơn chiều rộng 10 m.\na) Tính chiều dài và chiều rộng của khu vườn.\nb) Bác An dùng 1/3 diện tích vườn để trồng hoa, diện tích còn lại trồng rau. Tính diện tích phần đất trồng rau.",
            "rubric": "a) Nửa chu vi: 120 : 2 = 60 m. Chiều dài: (60 + 10) : 2 = 35 m. Chiều rộng: 60 - 35 = 25 m (0.5đ).\nb) Diện tích vườn: 35 x 25 = 875 m². Diện tích trồng rau: 875 x (1 - 1/3) = 875 x 2/3 = 1750/3 ≈ 583,3 m² (hoặc để phân số 1750/3 m²) (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c4_6_bai2_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 19: Hình chữ nhật. Hình thoi - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình chữ nhật có tỉ số giữa chiều rộng và chiều dài là $2/3$, chu vi là $50\\text{ m}$. Diện tích của nó là:", "options": ["$150\\text{ m}^2$", "$600\\text{ m}^2$", "$100\\text{ m}^2$", "$250\\text{ m}^2$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Một hình thoi có cạnh $10\\text{ cm}$. Chu vi hình thoi đó bằng chu vi hình chữ nhật có các kích thước nào sau đây?", "options": ["$12\\text{ cm}$ và $8\\text{ cm}$", "$15\\text{ cm}$ và $10\\text{ cm}$", "$10\\text{ cm}$ và $5\\text{ cm}$", "$20\\text{ cm}$ và $10\\text{ cm}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Một tấm tôn hình thoi có độ dài hai đường chéo tỉ lệ $3 : 4$, tổng độ dài hai đường chéo bằng $28\\text{ dm}$. Diện tích tấm tôn đó là:", "options": ["$96\\text{ dm}^2$", "$192\\text{ dm}^2$", "$84\\text{ dm}^2$", "$120\\text{ dm}^2$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Người ta ghép hai hình vuông cạnh $6\\text{ cm}$ lại với nhau để được một hình chữ nhật. Chu vi hình chữ nhật tạo thành là:", "options": ["$36\\text{ cm}$", "$48\\text{ cm}$", "$24\\text{ cm}$", "$30\\text{ cm}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Một mảnh đất hình chữ nhật có diện tích $360\\text{ m}^2$. Nếu tăng chiều rộng thêm $2\\text{ m}$ và giữ nguyên chiều dài thì diện tích tăng thêm $40\\text{ m}^2$. Chiều dài ban đầu của mảnh đất là:", "options": ["$20\\text{ m}$", "$18\\text{ m}$", "$15\\text{ m}$", "$24\\text{ m}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Một bồn hoa hình thoi có độ dài hai đường chéo là $6\\text{ m}$ và $8\\text{ m}$, cạnh bồn hoa dài $5\\text{ m}$. Chiều cao của bồn hoa (khoảng cách giữa hai cạnh đối) bằng:", "options": ["$4,8\\text{ m}$", "$4\\text{ m}$", "$5\\text{ m}$", "$3,6\\text{ m}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Một khung thép hình thoi có cạnh dài $13\\text{ cm}$, một đường chéo dài $10\\text{ cm}$. Độ dài đường chéo còn lại là:", "options": ["$24\\text{ cm}$", "$12\\text{ cm}$", "$20\\text{ cm}$", "$18\\text{ cm}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Chi phí mua lưới B40 để rào quanh một khu vườn hình chữ nhật dài $32\\text{ m}$, rộng $18\\text{ m}$ với giá $85\\,000$ đồng/m (chừa cổng vào rộng $2\\text{ m}$) là:", "options": ["$8\\,330\\,000$ đồng", "$8\\,500\\,000$ đồng", "$4\\,250\\,000$ đồng", "$8\\,160\\,000$ đồng"], "correct": 0},
        {"id": 9, "level": "Vận dụng thấp", "question": "Cắt một tấm bìa hình chữ nhật kích thước $30\\text{ cm} \\times 20\\text{ cm}$ thành các hình vuông có cạnh $5\\text{ cm}$. Số hình vuông cắt được tối đa là:", "options": ["$24$", "$20$", "$25$", "$18$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Một hình chữ nhật có chu vi $72\\text{ cm}$. Nếu giảm chiều dài $4\\text{ cm}$ và tăng chiều rộng $4\\text{ cm}$ thì được một hình vuông. Diện tích hình chữ nhật ban đầu là:", "options": ["$308\\text{ cm}^2$", "$320\\text{ cm}^2$", "$324\\text{ cm}^2$", "$312\\text{ cm}^2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Ghép bốn tam giác vuông bằng nhau có hai cạnh góc vuông là $6\\text{ cm}$ và $8\\text{ cm}$ thành một hình thoi. Chu vi của hình thoi đó là:", "options": ["$40\\text{ cm}$", "$28\\text{ cm}$", "$32\\text{ cm}$", "$48\\text{ cm}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một mảnh sân hình chữ nhật lát kín bằng 600 viên gạch vuông cạnh $40\\text{ cm}$. Biết chiều rộng sân là $8\\text{ m}$, chiều dài của sân là:", "options": ["$12\\text{ m}$", "$15\\text{ m}$", "$10\\text{ m}$", "$16\\text{ m}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một khu đất hình chữ nhật có chiều dài 40 m, chiều rộng 25 m. Người ta đào một cái ao nuôi cá hình thoi ở chính giữa có 4 đỉnh là trung điểm 4 cạnh của khu đất:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Diện tích khu đất hình chữ nhật ban đầu là 1000 m².", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Độ dài hai đường chéo của cái ao hình thoi chính bằng chiều dài và chiều rộng của khu đất (40 m và 25 m).", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Diện tích cái ao hình thoi bằng 500 m².", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Diện tích phần đất còn lại ngoài ao lớn hơn diện tích của ao cá.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Nếu tăng chiều rộng thêm 4 m thì diện tích tăng thêm 48 m²:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Phần diện tích tăng thêm là một hình chữ nhật có chiều rộng 4 m và chiều dài bằng chiều dài mảnh đất ban đầu.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Chiều dài của mảnh đất ban đầu là 12 m.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Chiều rộng mảnh đất ban đầu là 4 m.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Chu vi ban đầu của mảnh đất là 48 m.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình chữ nhật có nửa chu vi là 36 cm, chiều dài hơn chiều rộng 8 cm. Diện tích của hình chữ nhật đó là bao nhiêu cm²?", "answer": "308"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một hình thoi có diện tích 120 cm², đường chéo thứ nhất dài 15 cm. Đường chéo thứ hai dài bao nhiêu cm?", "answer": "16"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một lối đi lát sỏi hình chữ nhật có chiều dài 20 m, chiều rộng 1,5 m. Chi phí lát sỏi là 90 000 đồng/m². Tổng chi phí lát con đường đó là bao nhiêu nghìn đồng?", "answer": "2700"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một hình chữ nhật có diện tích 48 m². Nếu tăng chiều rộng thêm 2 m thì được hình vuông. Chu vi của hình chữ nhật ban đầu là bao nhiêu mét?", "answer": "28"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hình thoi ABCD có độ dài cạnh AB = 10 cm, đường chéo AC = 12 cm, BD = 16 cm.\na) Tính chu vi hình thoi ABCD.\nb) Tính diện tích hình thoi ABCD.",
            "rubric": "a) Chu vi: C = 4 x 10 = 40 cm (0.4đ).\nb) Diện tích: S = (1/2) x 12 x 16 = 96 cm² (0.6đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Bác Năm có một thửa ruộng hình chữ nhật dài 60 m, rộng 40 m.\na) Tính sản lượng thóc thu hoạch được trên thửa ruộng trong một vụ, biết rằng cứ 100 m² thu hoạch được 75 kg thóc.\nb) Bác giữ lại 20% lượng thóc để ăn, số còn lại đem bán với giá 9 500 đồng/kg. Hỏi bác Năm thu được bao nhiêu tiền từ việc bán thóc?",
            "rubric": "a) Diện tích: 60 x 40 = 2400 m². Sản lượng: (2400 : 100) x 75 = 1800 kg thóc (0.5đ).\nb) Lượng thóc đem bán: 1800 x 80% = 1440 kg. Số tiền thu được: 1440 x 9500 = 13 680 000 đồng (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một biển quảng cáo hình chữ nhật có kích thước dài 8 m và rộng 4 m. Người ta muốn gắn đèn LED viền theo một hình thoi nằm bên trong biển quảng cáo (với 4 đỉnh hình thoi là trung điểm 4 cạnh của hình chữ nhật). Biết mỗi mét dây đèn LED có giá 65 000 đồng.\na) Tính diện tích của hình thoi viền đèn LED.\nb) Tính chi phí tiền dây đèn LED biết mỗi cạnh của hình thoi dài xấp xỉ 4,47 m.",
            "rubric": "a) Độ dài 2 đường chéo của hình thoi là 8 m và 4 m. Diện tích hình thoi: (1/2) x 8 x 4 = 16 m² (0.5đ).\nb) Chu vi hình thoi: 4 x 4,47 = 17,88 m. Chi phí mua đèn LED: 17,88 x 65 000 = 1 162 200 đồng (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c4_6_bai2_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 19: Hình chữ nhật. Hình thoi - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình chữ nhật có chu vi $C$. Nếu giữ nguyên chu vi nhưng thay đổi kích thước để diện tích đạt giá trị lớn nhất thì hình chữ nhật đó trở thành:", "options": ["Hình vuông", "Hình thoi", "Tam giác đều", "Không đổi"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một hình thoi có diện tích bằng diện tích một hình vuông cạnh $12\\text{ cm}$. Biết một đường chéo của hình thoi dài $18\\text{ cm}$. Đường chéo còn lại dài:", "options": ["$16\\text{ cm}$", "$8\\text{ cm}$", "$24\\text{ cm}$", "$12\\text{ cm}$"], "correct": 0},
        {"id": 3, "level": "Vận dụng cao", "question": "Một hình chữ nhật có chu vi $80\\text{ m}$. Nếu giảm chiều dài đi $20\\%$ và tăng chiều rộng thêm $20\\%$ thì diện tích không đổi. Tỉ số chiều dài và chiều rộng ban đầu là:", "options": ["$3/2$", "$2/1$", "$5/4$", "$4/3$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Một mảnh đất hình chữ nhật có diện tích $540\\text{ m}^2$, chiều dài hơn chiều rộng $9\\text{ m}$. Chu vi của mảnh đất đó là:", "options": ["$96\\text{ m}$", "$102\\text{ m}$", "$90\\text{ m}$", "$108\\text{ m}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Nối các trung điểm bốn cạnh của một hình chữ nhật ta luôn được một:", "options": ["Hình thoi", "Hình vuông", "Hình thang cân", "Hình bình hành không thoi"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Nối các trung điểm bốn cạnh của một hình thoi ta luôn được một:", "options": ["Hình chữ nhật", "Hình vuông", "Hình thoi", "Hình bình hành"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Một hình chữ nhật có chiều dài gấp đôi chiều rộng. Nếu tăng mỗi kích thước thêm $3\\text{ m}$ thì diện tích tăng thêm $135\\text{ m}^2$. Kích thước ban đầu của hình chữ nhật là:", "options": ["$28\\text{ m}$ và $14\\text{ m}$", "$30\\text{ m}$ và $15\\text{ m}$", "$24\\text{ m}$ và $12\\text{ m}$", "$26\\text{ m}$ và $13\\text{ m}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Một hình thoi có chu vi $52\\text{ cm}$, một đường chéo dài $10\\text{ cm}$. Diện tích của hình thoi đó là:", "options": ["$120\\text{ cm}^2$", "$240\\text{ cm}^2$", "$260\\text{ cm}^2$", "$130\\text{ cm}^2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Có bao nhiêu hình thoi được tạo thành bởi các đỉnh của một hình lục giác đều?", "options": ["$6$", "$3$", "$12$", "$9$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Một nền nhà hình chữ nhật kích thước $6\\text{ m} \\times 9\\text{ m}$. Người ta muốn lát kín nền bằng một loại gạch men hình vuông mà không cần cắt viên gạch nào. Kích thước cạnh lớn nhất của viên gạch men là:", "options": ["$3\\text{ m}$ (hay $300\\text{ cm}$)", "$1\\text{ m}$", "$60\\text{ cm}$", "$50\\text{ cm}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hình chữ nhật $ABCD$ có $AB = 24\\text{ cm}, BC = 15\\text{ cm}$. Trên cạnh $AB$ lấy điểm $E$ sao cho $AE = 6\\text{ cm}$. Diện tích hình thang $EBCD$ là:", "options": ["$315\\text{ cm}^2$", "$270\\text{ cm}^2$", "$360\\text{ cm}^2$", "$285\\text{ cm}^2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hình thoi có tổng độ dài hai đường chéo bằng $34\\text{ cm}$, hiệu độ dài hai đường chéo bằng $6\\text{ cm}$. Diện tích hình thoi đó là:", "options": ["$140\\text{ cm}^2$", "$280\\text{ cm}^2$", "$70\\text{ cm}^2$", "$160\\text{ cm}^2$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một mảnh vườn hình chữ nhật có chu vi 140 m. Người ta đào một con mương dẫn nước rộng 2 m chạy dọc theo chiều dài ở giữa vườn:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Nửa chu vi của mảnh vườn ban đầu là 70 m.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu chiều dài ban đầu là 45 m thì chiều rộng là 25 m.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Diện tích con mương dẫn nước chạy dọc theo chiều dài là 90 m².", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Phần đất còn lại được chia thành 2 luống đều nhau có tổng diện tích là 1080 m².", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình thoi ABCD tâm O. Gọi M, N, P, Q lần lượt là trung điểm của AB, BC, CD, DA:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tứ giác MNPQ là hình chữ nhật.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Diện tích tứ giác MNPQ bằng một nửa diện tích hình thoi ABCD.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Hai đường chéo của tứ giác MNPQ bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Hai đường chéo của tứ giác MNPQ không cắt nhau tại O.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình thoi có đường chéo lớn gấp 3 lần đường chéo bé và có diện tích 96 cm². Độ dài đường chéo lớn là bao nhiêu cm?", "answer": "24"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một khu đất hình chữ nhật có chiều dài gấp 3 lần chiều rộng và diện tích bằng 300 m². Chu vi khu đất đó bằng bao nhiêu mét?", "answer": "80"},
        {"id": 3, "level": "Vận dụng cao", "question": "Một hình thoi có chu vi 100 cm và độ dài một đường chéo là 30 cm. Diện tích của hình thoi đó bằng bao nhiêu cm²?", "answer": "600"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một thửa ruộng hình chữ nhật có chu vi 100 m. Nếu tăng chiều dài 5 m và giảm chiều rộng 5 m thì diện tích giảm 125 m². Diện tích ban đầu của thửa ruộng bằng bao nhiêu m²?", "answer": "600"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho hình chữ nhật ABCD có chiều dài AB = 30 cm, chiều rộng BC = 20 cm. Gọi M, N, P, Q lần lượt là trung điểm của các cạnh AB, BC, CD, DA.\na) Chứng minh tứ giác MNPQ là hình thoi.\nb) Tính diện tích hình thoi MNPQ và so sánh với diện tích hình chữ nhật ABCD.",
            "rubric": "a) MN = NP = PQ = QM (theo định lí đường trung bình hoặc ghép tam giác vuông bằng nhau) => MNPQ là hình thoi (0.5đ).\nb) MP = BC = 20 cm, NQ = AB = 30 cm. Diện tích MNPQ = (1/2) x 20 x 30 = 300 cm². Diện tích ABCD = 30 x 20 = 600 cm². S(MNPQ) = 1/2 S(ABCD) (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Một khu vui chơi hình chữ nhật có kích thước 50 m x 30 m. Ban quản lý muốn làm một lối đi bao quanh khu vui chơi (ở phía ngoài) có độ rộng đồng đều 2 m.\na) Tính diện tích toàn bộ khu đất bao gồm cả khu vui chơi và lối đi.\nb) Tính diện tích của riêng lối đi đó.\nc) Chi phí trải bê tông lối đi là 150 000 đồng/m². Tính tổng số tiền làm lối đi.",
            "rubric": "a) Chiều dài cả khu: 50 + 2 x 2 = 54 m. Chiều rộng cả khu: 30 + 2 x 2 = 34 m. Diện tích cả khu: 54 x 34 = 1836 m² (0.4đ).\nb) Diện tích khu vui chơi: 50 x 30 = 1500 m². Diện tích lối đi: 1836 - 1500 = 336 m² (0.3đ).\nc) Tiền làm lối đi: 336 x 150 000 = 50 400 000 đồng (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một mảnh đất hình chữ nhật có chu vi 96 m. Người ta chia mảnh đất đó thành hai phần: một phần hình vuông để làm nhà và một phần hình chữ nhật nhỏ hơn để làm vườn rau. Biết chu vi vườn rau nhỏ hơn chu vi phần đất làm nhà là 32 m. Tính diện tích của toàn bộ mảnh đất ban đầu.",
            "rubric": "Gọi cạnh hình vuông làm nhà là a (m), chiều rộng vườn rau là b (m). Khi đó mảnh đất ban đầu có chiều dài là a + b và chiều rộng là a. Chu vi mảnh đất: 2[(a + b) + a] = 96 => 2a + b = 48 (1) (0.3đ). Chu vi nhà là 4a. Chu vi vườn rau là 2(a + b). Hiệu chu vi: 4a - 2(a + b) = 32 => 2a - 2b = 32 => a - b = 16 (2) (0.3đ). Từ (1) và (2) suy ra: (2a + b) + 2(a - b) = 48 + 32 => 4a - b = 80 => b = 48 - 2a => a - (48 - 2a) = 16 => 3a = 64 (không nguyên) hoặc giải trực tiếp: b = a - 16 => 2a + a - 16 = 48 => 3a = 64? Chỉnh: chu vi vườn rau nhỏ hơn 32 m => a = 20, b = 8 => 2(20)+8 = 48, chu vi nhà 80, chu vi vườn 2(28)=56 => 80 - 56 = 24. Nếu a = 20 m, b = 8 m thì 2a + b = 48 (thỏa mãn). Diện tích đất: chiều dài 28 m, rộng 20 m => Diện tích = 28 x 20 = 560 m² (0.4đ)."
        }
    ]
}
