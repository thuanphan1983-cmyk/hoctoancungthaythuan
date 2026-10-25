# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 6 - CHƯƠNG IV: MỘT SỐ HÌNH PHẲNG TRONG THỰC TIỄN
PHẦN 2:
- BÀI 20: HÌNH BÌNH HÀNH. HÌNH THANG CÂN (c4_6_bai3)
- BÀI KIỂM TRA CUỐI CHƯƠNG IV: MỘT SỐ HÌNH PHẲNG TRONG THỰC TIỄN (c4_6_bai4)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 20: HÌNH BÌNH HÀNH. HÌNH THANG CÂN (c4_6_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c4_6_bai3_test1"] = {
    "title": "Toán 6 (KNTT) - Bài 20: Hình bình hành. Hình thang cân - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hình bình hành là tứ giác có:", "options": ["Các cạnh đối song song và bằng nhau", "Bốn cạnh bằng nhau", "Bốn góc vuông", "Hai đường chéo vuông góc"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hình thang cân là hình thang có:", "options": ["Hai góc kề một đáy bằng nhau", "Hai cạnh đáy bằng nhau", "Bốn cạnh bằng nhau", "Hai đường chéo vuông góc"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Hai đường chéo của hình thang cân có tính chất:", "options": ["Bằng nhau", "Vuông góc với nhau", "Song song với nhau", "Cắt nhau tại trung điểm mỗi đường"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Công thức tính diện tích hình bình hành có đáy $a$ và chiều cao tương ứng $h$ là:", "options": ["$S = a \\cdot h$", "$S = \\frac{1}{2} a \\cdot h$", "$S = (a + h) \\cdot 2$", "$S = 2a \\cdot h$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Công thức tính diện tích hình thang có hai đáy $a, b$ và chiều cao $h$ là:", "options": ["$S = \\frac{(a + b) \\cdot h}{2}$", "$S = (a + b) \\cdot h$", "$S = a \\cdot b \\cdot h$", "$S = \\frac{a \\cdot b}{2}$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Chu vi hình bình hành có độ dài hai cạnh kề $a$ và $b$ là:", "options": ["$C = 2(a + b)$", "$C = 4(a + b)$", "$C = a \\cdot b$", "$C = a + b$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Một hình bình hành có độ dài đáy $10\\text{ cm}$ và chiều cao $6\\text{ cm}$. Diện tích của nó là:", "options": ["$60\\text{ cm}^2$", "$30\\text{ cm}^2$", "$32\\text{ cm}^2$", "$16\\text{ cm}^2$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Một hình thang có đáy lớn $12\\text{ cm}$, đáy bé $8\\text{ cm}$ và chiều cao $5\\text{ cm}$. Diện tích hình thang đó là:", "options": ["$50\\text{ cm}^2$", "$100\\text{ cm}^2$", "$25\\text{ cm}^2$", "$40\\text{ cm}^2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Một hình bình hành có hai cạnh kề dài $7\\text{ cm}$ và $9\\text{ cm}$. Chu vi hình bình hành đó bằng:", "options": ["$32\\text{ cm}$", "$16\\text{ cm}$", "$63\\text{ cm}$", "$28\\text{ cm}$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Hình thang cân $ABCD$ ($AB \\parallel CD$) có $AB = 4\\text{ cm}, CD = 10\\text{ cm}$, hai cạnh bên $AD = BC = 5\\text{ cm}$. Chu vi hình thang cân là:", "options": ["$24\\text{ cm}$", "$19\\text{ cm}$", "$28\\text{ cm}$", "$20\\text{ cm}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Trong hình bình hành $ABCD$, khẳng định nào sau đây là SAI?", "options": ["Hai đường chéo bằng nhau", "Các góc đối bằng nhau", "Hai đường chéo cắt nhau tại trung điểm của mỗi đường", "Các cạnh đối bằng nhau"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Một thửa ruộng hình bình hành có diện tích $120\\text{ m}^2$, chiều cao $8\\text{ m}$. Độ dài đáy của thửa ruộng là:", "options": ["$15\\text{ m}$", "$30\\text{ m}$", "$12\\text{ m}$", "$20\\text{ m}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hình bình hành ABCD có cạnh AB = 12 cm, BC = 8 cm và chiều cao ứng với cạnh AB là AH = 6 cm.",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Cạnh CD = 12 cm và AD = 8 cm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Chu vi hình bình hành ABCD là 40 cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Diện tích hình bình hành ABCD là 72 cm².", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Diện tích hình bình hành ABCD tính bằng 12 x 8 = 96 cm².", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình thang cân MNPQ có đáy MN // PQ, biết MN = 6 cm, PQ = 14 cm, cạnh bên MQ = 5 cm và chiều cao h = 4 cm.",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Cạnh bên NP = 5 cm và hai đường chéo MP = NQ.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Chu vi hình thang cân MNPQ là 30 cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Diện tích hình thang cân MNPQ là 40 cm².", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Hai góc kề đáy MN là góc nhọn (< 90°).", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một mảnh đất hình bình hành có độ dài đáy 18 m, chiều cao tương ứng 10 m. Tính diện tích mảnh đất đó (m²).", "answer": "180"},
        {"id": 2, "level": "Thông hiểu", "question": "Một hình thang có đáy lớn 16 cm, đáy bé 10 cm và diện tích 78 cm². Chiều cao của hình thang là bao nhiêu cm?", "answer": "6"},
        {"id": 3, "level": "Thông hiểu", "question": "Hình thang cân có độ dài hai đáy là 7 cm và 13 cm, chu vi bằng 36 cm. Độ dài mỗi cạnh bên của nó là bao nhiêu cm?", "answer": "8"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Một hình bình hành có chu vi 48 cm, một cạnh dài 15 cm. Độ dài cạnh kề với nó là bao nhiêu cm?", "answer": "9"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "a) Nêu các tính chất về cạnh, góc và đường chéo của hình thang cân.\nb) Tính diện tích hình thang cân có độ dài hai đáy là 8 cm và 14 cm, chiều cao là 7 cm.",
            "rubric": "a) Hai cạnh đáy song song, hai cạnh bên bằng nhau, hai góc kề một đáy bằng nhau, hai đường chéo bằng nhau (0.5đ).\nb) S = (8 + 14) x 7 : 2 = 77 cm² (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một khu đất hình bình hành có đáy dài 45 m, chiều cao kém đáy 15 m.\na) Tính diện tích khu đất đó.\nb) Người ta dùng 1/5 diện tích khu đất để làm nhà, phần còn lại trồng cây ăn quả. Tính diện tích phần trồng cây ăn quả.",
            "rubric": "a) Chiều cao: 45 - 15 = 30 m. Diện tích: 45 x 30 = 1350 m² (0.5đ).\nb) Diện tích làm nhà: 1350 x 1/5 = 270 m². Diện tích trồng cây: 1350 - 270 = 1080 m² (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Mặt cắt của một con đê có dạng hình thang cân với đáy lớn 12 m, đáy nhỏ 6 m và chiều cao 4 m.\na) Tính diện tích mặt cắt ngang của con đê.\nb) Người ta muốn rải sỏi mặt đê (đáy nhỏ) dài 100 m, biết mặt đê rộng 6 m. Tính diện tích mặt đê cần rải sỏi.",
            "rubric": "a) Diện tích mặt cắt: (12 + 6) x 4 : 2 = 36 m² (0.5đ).\nb) Diện tích mặt đê hình chữ nhật: 100 x 6 = 600 m² (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c4_6_bai3_test2"] = {
    "title": "Toán 6 (KNTT) - Bài 20: Hình bình hành. Hình thang cân - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Một mảnh đất hình bình hành có đáy dài gấp 3 lần chiều cao và diện tích là $75\\text{ m}^2$. Độ dài đáy của mảnh đất là:", "options": ["$15\\text{ m}$", "$5\\text{ m}$", "$25\\text{ m}$", "$10\\text{ m}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Một hình thang cân có đáy lớn $20\\text{ cm}$, đáy bé bằng một nửa đáy lớn, cạnh bên $8\\text{ cm}$. Chu vi của hình thang cân đó là:", "options": ["$46\\text{ cm}$", "$38\\text{ cm}$", "$52\\text{ cm}$", "$40\\text{ cm}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Một hình thang có diện tích $150\\text{ cm}^2$, chiều cao $10\\text{ cm}$. Trung bình cộng hai đáy của hình thang là:", "options": ["$15\\text{ cm}$", "$30\\text{ cm}$", "$20\\text{ cm}$", "$25\\text{ cm}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Một mảnh vườn hình bình hành có cạnh $24\\text{ m}$ và $16\\text{ m}$. Người ta rào xung quanh vườn bằng 4 hàng dây thép gai. Tổng chiều dài dây thép gai cần dùng là:", "options": ["$320\\text{ m}$", "$80\\text{ m}$", "$160\\text{ m}$", "$240\\text{ m}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Một hình thang có đáy bé $9\\text{ cm}$, đáy lớn gấp đôi đáy bé. Nếu kéo dài đáy lớn thêm $3\\text{ cm}$ thì diện tích tăng thêm $18\\text{ cm}^2$. Diện tích hình thang ban đầu là:", "options": ["$162\\text{ cm}^2$", "$144\\text{ cm}^2$", "$180\\text{ cm}^2$", "$120\\text{ cm}^2$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Một hình thang cân có chu vi $60\\text{ cm}$, hai cạnh bên mỗi cạnh dài $13\\text{ cm}$. Chiều cao hình thang bằng $12\\text{ cm}$. Diện tích của hình thang cân đó là:", "options": ["$204\\text{ cm}^2$", "$408\\text{ cm}^2$", "$180\\text{ cm}^2$", "$240\\text{ cm}^2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Ghép hai hình thang cân bằng nhau có đáy lớn $10\\text{ cm}$, đáy nhỏ $6\\text{ cm}$ và cạnh bên $5\\text{ cm}$ dọc theo đáy lớn thì ta được một hình:", "options": ["Lục giác", "Hình bình hành", "Hình chữ nhật", "Hình thoi"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho hình bình hành $ABCD$ có diện tích $60\\text{ cm}^2$. Lấy $M$ là trung điểm của cạnh $CD$. Diện tích tam giác $ABM$ là:", "options": ["$30\\text{ cm}^2$", "$20\\text{ cm}^2$", "$15\\text{ cm}^2$", "$40\\text{ cm}^2$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Một thửa ruộng hình thang có đáy lớn $50\\text{ m}$, đáy bé $30\\text{ m}$. Khi mở rộng đáy lớn thêm $10\\text{ m}$ thì diện tích tăng $120\\text{ m}^2$. Diện tích thửa ruộng ban đầu là:", "options": ["$960\\text{ m}^2$", "$1080\\text{ m}^2$", "$840\\text{ m}^2$", "$1200\\text{ m}^2$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Một hình bình hành có chu vi $70\\text{ cm}$, độ dài hai cạnh tỉ lệ $2 : 3$. Độ dài hai cạnh kề của hình bình hành là:", "options": ["$14\\text{ cm}$ và $21\\text{ cm}$", "$10\\text{ cm}$ và $25\\text{ cm}$", "$12\\text{ cm}$ và $18\\text{ cm}$", "$15\\text{ cm}$ và $20\\text{ cm}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một tấm bìa hình thang cân có đáy lớn $18\\text{ cm}$, đáy nhỏ $10\\text{ cm}$, góc ở đáy lớn bằng $45^\\circ$. Chiều cao của hình thang cân đó là:", "options": ["$4\\text{ cm}$", "$8\\text{ cm}$", "$5\\text{ cm}$", "$6\\text{ cm}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hình bình hành $ABCD$ có chiều cao ứng với cạnh $AB$ là $h_1 = 8\\text{ cm}$, chiều cao ứng với cạnh $BC$ là $h_2 = 10\\text{ cm}$. Biết $AB = 15\\text{ cm}$, độ dài cạnh $BC$ là:", "options": ["$12\\text{ cm}$", "$10\\text{ cm}$", "$14\\text{ cm}$", "$16\\text{ cm}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một thửa ruộng hình thang có đáy lớn 120 m, đáy bé bằng 2/3 đáy lớn và chiều cao bằng 40 m:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Đáy bé của thửa ruộng dài 80 m.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích của thửa ruộng hình thang là 4000 m².", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Biết cứ 100 m² thu hoạch được 65 kg thóc, cả thửa ruộng thu hoạch được 2,6 tấn thóc.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Nếu giá bán thóc là 9 000 đồng/kg thì số tiền bán thóc thu được là 26 triệu đồng.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình bình hành MNPQ có góc M = 110°:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Góc P đối diện với góc M có số đo bằng 110°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hai góc kề một cạnh có tổng số đo bằng 180°, nên góc N = 70°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số đo góc Q bằng 70°.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Hình bình hành MNPQ có đúng 2 trục đối xứng.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình thang có tổng độ dài hai đáy là 48 cm, chiều cao bằng 1/3 tổng hai đáy. Diện tích của hình thang đó là bao nhiêu cm²?", "answer": "384"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một hình bình hành có diện tích 216 cm² và cạnh đáy 18 cm. Chiều cao tương ứng bằng bao nhiêu cm?", "answer": "12"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một hình thang cân có đáy lớn 26 cm, đáy nhỏ 14 cm và diện tích 240 cm². Chiều cao của hình thang cân là bao nhiêu cm?", "answer": "12"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một mảnh đất hình bình hành có đáy 35 m. Nếu giảm đáy đi 5 m thì diện tích giảm 60 m². Diện tích mảnh đất ban đầu là bao nhiêu m²?", "answer": "420"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hình thang ABCD (AB // CD) có đáy nhỏ AB = 15 cm, đáy lớn CD = 25 cm, chiều cao AH = 12 cm.\na) Tính diện tích hình thang ABCD.\nb) Tính diện tích tam giác ADC.",
            "rubric": "a) S(ABCD) = (15 + 25) x 12 : 2 = 240 cm² (0.5đ).\nb) Tam giác ADC có đáy CD = 25 cm và chiều cao AH = 12 cm nên S(ADC) = 1/2 x 25 x 12 = 150 cm² (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một công viên có bồn hoa hình bình hành cạnh đáy 28 m và chiều cao tương ứng 15 m. Người ta muốn trồng hoa hồng trên toàn bộ bồn hoa với mật độ 9 cây/m².\na) Tính diện tích bồn hoa.\nb) Tính tổng số cây hoa hồng cần mua để trồng phủ kín bồn hoa đó.",
            "rubric": "a) Diện tích: 28 x 15 = 420 m² (0.5đ).\nb) Số cây hoa hồng: 420 x 9 = 3780 cây (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một thửa ruộng hình thang có đáy lớn 65 m, đáy bé 45 m. Người ta đào một con mương thoát nước chạy ngang qua thửa ruộng có dạng hình bình hành với đáy 3 m và chiều cao bằng chiều cao thửa ruộng. Biết chiều cao thửa ruộng là 24 m.\na) Tính diện tích con mương thoát nước.\nb) Tính diện tích phần đất còn lại dùng để canh tác lúa.",
            "rubric": "a) Diện tích con mương hình bình hành: 3 x 24 = 72 m² (0.4đ).\nb) Diện tích toàn bộ thửa ruộng: (65 + 45) x 24 : 2 = 1320 m² (0.3đ). Diện tích canh tác còn lại: 1320 - 72 = 1248 m² (0.3đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c4_6_bai3_test3"] = {
    "title": "Toán 6 (KNTT) - Bài 20: Hình bình hành. Hình thang cân - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hình bình hành $ABCD$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Một đường thẳng đi qua $O$ cắt $AB$ tại $M$ và cắt $CD$ tại $N$. Khi đó đoạn thẳng $OM$ so với $ON$:", "options": ["$OM = ON$", "$OM > ON$", "$OM < ON$", "Không so sánh được"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một hình thang có đáy lớn gấp $3$ lần đáy nhỏ. Nếu tăng đáy nhỏ thêm $4\\text{ m}$ thì hình thang trở thành hình bình hành có diện tích gấp đôi diện tích ban đầu. Đáy nhỏ ban đầu là:", "options": ["$2\\text{ m}$", "$4\\text{ m}$", "$3\\text{ m}$", "$6\\text{ m}$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một hình thang cân có hai đường chéo vuông góc với nhau và chiều cao bằng $10\\text{ cm}$. Diện tích của hình thang cân đó là:", "options": ["$100\\text{ cm}^2$", "$50\\text{ cm}^2$", "$200\\text{ cm}^2$", "$150\\text{ cm}^2$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hình bình hành $ABCD$ có diện tích $S$. Điểm $E$ nằm trên cạnh $AB$. Diện tích tam giác $EDC$ luôn bằng:", "options": ["$S/2$", "$S/3$", "$2S/3$", "$S/4$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Một thửa ruộng hình thang có diện tích $540\\text{ m}^2$, chiều cao $18\\text{ m}$. Đáy lớn hơn đáy bé $12\\text{ m}$. Độ dài đáy bé và đáy lớn lần lượt là:", "options": ["$24\\text{ m}$ và $36\\text{ m}$", "$20\\text{ m}$ và $32\\text{ m}$", "$22\\text{ m}$ và $34\\text{ m}$", "$18\\text{ m}$ và $30\\text{ m}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cắt một hình thang cân theo một đường thẳng song song với hai đáy để chia thành hai hình thang có chiều cao bằng nhau. Tỉ số diện tích hai phần phụ thuộc vào:", "options": ["Độ dài hai đáy ban đầu", "Chỉ phụ thuộc chiều cao", "Luôn bằng 1", "Không xác định"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $AB = 6\\text{ cm}, CD = 14\\text{ cm}$, góc ở đáy lớn bằng $60^\\circ$. Độ dài cạnh bên $AD$ là:", "options": ["$8\\text{ cm}$", "$4\\text{ cm}$", "$6\\text{ cm}$", "$10\\text{ cm}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho hình bình hành $ABCD$. Trên cạnh $AB$ lấy điểm $M$, trên $CD$ lấy $N$ sao cho $AM = CN$. Tứ giác $MBND$ là hình gì?", "options": ["Hình bình hành", "Hình chữ nhật", "Hình thoi", "Hình thang cân"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Một hình thang có diện tích $210\\text{ cm}^2$, tỉ số hai đáy là $2/5$. Khi kéo dài đáy bé thêm $6\\text{ cm}$ thì được hình bình hành có diện tích $300\\text{ cm}^2$. Chiều cao của hình thang là:", "options": ["$15\\text{ cm}$", "$12\\text{ cm}$", "$18\\text{ cm}$", "$20\\text{ cm}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$ có diện tích $60\\text{ cm}^2$. Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = 2 DB$. Kẻ $DE \\parallel BC$ ($E \\in AC$). Diện tích hình thang $BDEC$ là:", "options": ["$33,3\\text{ cm}^2$", "$40\\text{ cm}^2$", "$26,7\\text{ cm}^2$", "$45\\text{ cm}^2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một hình thang cân có đáy nhỏ $10\\text{ cm}$, cạnh bên $13\\text{ cm}$, chiều cao $12\\text{ cm}$. Đáy lớn của hình thang cân là:", "options": ["$20\\text{ cm}$", "$15\\text{ cm}$", "$25\\text{ cm}$", "$18\\text{ cm}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tổng số đo bốn góc của một hình thang cân luôn bằng:", "options": ["$360^\\circ$", "$180^\\circ$", "$540^\\circ$", "$720^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hình bình hành ABCD có diện tích 120 cm². Lấy điểm M trên cạnh AB sao cho AM = 2 MB, điểm N trên cạnh CD sao cho CN = 2 ND:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tứ giác AMND là hình thang.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Độ dài đoạn AM bằng độ dài đoạn CN.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Diện tích tứ giác AMCN bằng 80 cm².", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Diện tích tam giác BCD bằng 40 cm².", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Một hình thang cân ABCD (AB // CD) có đường chéo BD vuông góc với cạnh bên BC, đáy nhỏ AB = 7 cm, CD = 25 cm:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Đoạn hình chiếu của cạnh bên trên đáy lớn bằng (25 - 7) : 2 = 9 cm.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Hai góc kề đáy CD là góc nhọn.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Chiều cao của hình thang cân bằng 12 cm.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Diện tích hình thang cân ABCD là 180 cm².", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình bình hành có hai đường cao là 6 cm và 8 cm. Biết cạnh đáy ứng với chiều cao 6 cm dài 16 cm. Chu vi của hình bình hành đó là bao nhiêu cm?", "answer": "56"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một hình thang cân có hai đáy là 12 cm và 28 cm, cạnh bên 10 cm. Diện tích của hình thang cân đó là bao nhiêu cm²?", "answer": "120"},
        {"id": 3, "level": "Vận dụng cao", "question": "Một hình thang có diện tích 360 cm², chiều cao 15 cm. Biết đáy lớn gấp đôi đáy bé. Độ dài đáy lớn là bao nhiêu cm?", "answer": "32"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hình bình hành ABCD có diện tích 96 cm². Gọi M, N lần lượt là trung điểm của BC và CD. Diện tích tam giác AMN bằng bao nhiêu cm²?", "answer": "36"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho hình thang vuông ABCD (vuông tại A và D) có đáy bé AB = 16 cm, đáy lớn CD = 24 cm và cạnh bên AD = 12 cm.\na) Tính diện tích hình thang vuông ABCD.\nb) Từ B kẻ BH vuông góc với CD tại H. Tính diện tích tam giác BHC.",
            "rubric": "a) S(ABCD) = (16 + 24) x 12 : 2 = 240 cm² (0.5đ).\nb) Tứ giác ABHD là hình chữ nhật nên DH = AB = 16 cm, BH = AD = 12 cm. HC = CD - DH = 24 - 16 = 8 cm. Diện tích tam giác BHC: 1/2 x 8 x 12 = 48 cm² (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Một thửa ruộng hình thang có đáy lớn 48 m, đáy bé bằng 2/3 đáy lớn. Người ta mở rộng thửa ruộng bằng cách kéo dài đáy lớn thêm 6 m và đáy bé thêm 4 m về cùng một phía để được hình thang mới có diện tích lớn hơn diện tích ban đầu là 75 m².\na) Tính chiều cao của thửa ruộng hình thang.\nb) Tính diện tích thửa ruộng ban đầu.",
            "rubric": "a) Đáy bé ban đầu: 48 x 2/3 = 32 m. Phần đất tăng thêm là hình thang có đáy lớn 6 m, đáy bé 4 m và cùng chiều cao h với thửa ruộng ban đầu. Diện tích tăng thêm: (6 + 4) x h : 2 = 75 => 5h = 75 => h = 15 m (0.5đ).\nb) Diện tích thửa ruộng ban đầu: (48 + 32) x 15 : 2 = 600 m² (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một công ty muốn thiết kế logo là một hình bình hành lồng trong một hình chữ nhật kích thước 20 cm x 12 cm sao cho 4 đỉnh của hình bình hành nằm trên 4 cạnh của hình chữ nhật và cách các đỉnh hình chữ nhật một khoảng bằng x (cm).\na) Viết biểu thức tính diện tích hình bình hành theo x.\nb) Tìm giá trị của x để diện tích hình bình hành đạt giá trị lớn nhất.",
            "rubric": "a) 4 tam giác vuông ở 4 góc gồm 2 tam giác kích thước x và 12 - x, 2 tam giác kích thước x và 20 - x. Tổng diện tích 4 tam giác: 2 x [1/2 x(12 - x)] + 2 x [1/2 x(20 - x)] = x(12 - x) + x(20 - x) = 32x - 2x². Diện tích hình bình hành: S = 20 x 12 - (32x - 2x²) = 240 - 32x + 2x² (cm²) (0.5đ).\nb) S = 2(x² - 16x + 64) + 240 - 128 = 2(x - 8)² + 112. Vì 0 ≤ x ≤ 12, nên (x - 8)² lớn nhất khi x = 0 (S = 240) hoặc x = 12 (S = 2 x 16 + 112 = 144). Để diện tích hình bình hành lớn nhất (thực tế x > 0), xét đỉnh parabol hoặc biên: khi x tiến tới 0 thì hình bình hành tiệm cận hình chữ nhật ban đầu với S = 240 cm² (0.5đ)."
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG IV: MỘT SỐ HÌNH PHẲNG TRONG THỰC TIỄN (c4_6_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c4_6_bai4_test1"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương IV: Hình phẳng - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hình nào sau đây có 4 cạnh bằng nhau và 4 góc vuông?", "options": ["Hình vuông", "Hình thoi", "Hình chữ nhật", "Hình bình hành"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hình nào sau đây có 3 cạnh bằng nhau và 3 góc bằng nhau?", "options": ["Tam giác đều", "Tam giác vuông", "Tam giác cân", "Tam giác tù"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Hình lục giác đều có số đường chéo chính là:", "options": ["$3$", "$6$", "$9$", "$4$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Diện tích hình chữ nhật có kích thước $a = 6\\text{ cm}, b = 4\\text{ cm}$ là:", "options": ["$24\\text{ cm}^2$", "$20\\text{ cm}^2$", "$10\\text{ cm}^2$", "$12\\text{ cm}^2$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Chu vi của một hình vuông có cạnh bằng $8\\text{ cm}$ là:", "options": ["$32\\text{ cm}$", "$64\\text{ cm}$", "$16\\text{ cm}$", "$24\\text{ cm}$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Diện tích hình thoi có hai đường chéo $m = 6\\text{ cm}, n = 8\\text{ cm}$ là:", "options": ["$24\\text{ cm}^2$", "$48\\text{ cm}^2$", "$14\\text{ cm}^2$", "$28\\text{ cm}^2$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Hình thang cân có tính chất nào sau đây?", "options": ["Hai đường chéo bằng nhau", "Bốn cạnh bằng nhau", "Hai đường chéo vuông góc", "Bốn góc bằng nhau"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Một hình bình hành có đáy $12\\text{ cm}$ và chiều cao tương ứng $5\\text{ cm}$. Diện tích của nó là:", "options": ["$60\\text{ cm}^2$", "$30\\text{ cm}^2$", "$34\\text{ cm}^2$", "$17\\text{ cm}^2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Một tam giác đều có chu vi bằng $27\\text{ cm}$. Độ dài mỗi cạnh của nó là:", "options": ["$9\\text{ cm}$", "$6\\text{ cm}$", "$8\\text{ cm}$", "$12\\text{ cm}$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Một hình chữ nhật có diện tích $45\\text{ cm}^2$, chiều rộng $5\\text{ cm}$. Chu vi hình chữ nhật đó là:", "options": ["$28\\text{ cm}$", "$14\\text{ cm}$", "$18\\text{ cm}$", "$24\\text{ cm}$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Chu vi của một hình lục giác đều cạnh $7\\text{ cm}$ là:", "options": ["$42\\text{ cm}$", "$35\\text{ cm}$", "$49\\text{ cm}$", "$28\\text{ cm}$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Một hình thoi có cạnh $6\\text{ cm}$. Chu vi hình thoi đó là:", "options": ["$24\\text{ cm}$", "$36\\text{ cm}$", "$12\\text{ cm}$", "$18\\text{ cm}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Xét các hình phẳng đã học trong Chương IV:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Hình vuông vừa là hình chữ nhật vừa là hình thoi.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Hình chữ nhật có 4 góc bằng nhau và bằng 90°.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hình bình hành luôn có hai đường chéo bằng nhau.", "correct": False},
                {"key": "d", "level": "Thông hiểu", "text": "Hình thang cân có hai cạnh bên bằng nhau.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Một mảnh sân hình chữ nhật có chiều dài 15 m, chiều rộng 8 m:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Chu vi của mảnh sân là 46 m.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích của mảnh sân là 120 m².", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Người ta dùng gạch vuông cạnh 40 cm để lát sân thì cần 750 viên gạch.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Chi phí mua gạch lát sân với giá 120 000 đồng/m² là 15 triệu đồng.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình vuông có diện tích 100 cm². Chu vi hình vuông đó là bao nhiêu cm?", "answer": "40"},
        {"id": 2, "level": "Thông hiểu", "question": "Một hình thang có đáy lớn 14 cm, đáy bé 8 cm và chiều cao 6 cm. Diện tích của hình thang đó bằng bao nhiêu cm²?", "answer": "66"},
        {"id": 3, "level": "Thông hiểu", "question": "Một hình bình hành có đáy 15 m, chiều cao 8 m. Diện tích hình bình hành bằng bao nhiêu m²?", "answer": "120"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Chu vi một hình lục giác đều bằng 54 cm. Cạnh của hình lục giác đó dài bao nhiêu cm?", "answer": "9"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính diện tích của các hình sau:\na) Hình chữ nhật có chiều dài 18 cm, chiều rộng 11 cm.\nb) Hình thoi có hai đường chéo dài 16 cm và 25 cm.",
            "rubric": "a) S = 18 x 11 = 198 cm² (0.5đ).\nb) S = (1/2) x 16 x 25 = 200 cm² (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Một thửa ruộng hình bình hành có đáy 36 m, chiều cao tương ứng 20 m.\na) Tính diện tích thửa ruộng.\nb) Cứ mỗi 100 m² đất ruộng thu hoạch được 70 kg thóc. Hỏi cả thửa ruộng thu được bao nhiêu tạ thóc?",
            "rubric": "a) Diện tích: 36 x 20 = 720 m² (0.5đ).\nb) Sản lượng thóc: (720 : 100) x 70 = 504 kg = 5,04 tạ thóc (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một nền nhà hình chữ nhật có chiều dài 12 m và chiều rộng 5 m. Người ta dùng gạch men hình vuông cạnh 50 cm để lát toàn bộ nền nhà.\na) Tính diện tích nền nhà.\nb) Hỏi cần bao nhiêu viên gạch men để lát kín nền nhà (bỏ qua mép vữa)?",
            "rubric": "a) S nền: 12 x 5 = 60 m² = 600 000 cm² (0.5đ).\nb) S 1 viên gạch: 50 x 50 = 2500 cm². Số viên gạch: 600 000 : 2500 = 240 viên (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c4_6_bai4_test2"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương IV: Hình phẳng - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Hình thoi có chu vi $40\\text{ cm}$, một đường chéo dài $12\\text{ cm}$. Diện tích của hình thoi đó là:", "options": ["$96\\text{ cm}^2$", "$120\\text{ cm}^2$", "$48\\text{ cm}^2$", "$192\\text{ cm}^2$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Ghép 6 tam giác đều cạnh $5\\text{ cm}$ thành một lục giác đều. Chu vi của hình lục giác đều tạo thành là:", "options": ["$30\\text{ cm}$", "$25\\text{ cm}$", "$36\\text{ cm}$", "$15\\text{ cm}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Một hình chữ nhật có chu vi $64\\text{ m}$. Nếu tăng chiều rộng $3\\text{ m}$ và giảm chiều dài $3\\text{ m}$ thì diện tích đạt giá trị lớn nhất. Diện tích lớn nhất đó là:", "options": ["$256\\text{ m}^2$", "$240\\text{ m}^2$", "$250\\text{ m}^2$", "$289\\text{ m}^2$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Một hình thang cân có đáy lớn $22\\text{ cm}$, đáy bé $10\\text{ cm}$, cạnh bên $10\\text{ cm}$. Chiều cao hình thang cân là:", "options": ["$8\\text{ cm}$", "$6\\text{ cm}$", "$10\\text{ cm}$", "$12\\text{ cm}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Cắt một tấm bìa hình vuông cạnh $24\\text{ cm}$ thành các hình vuông nhỏ cạnh $3\\text{ cm}$. Số hình vuông nhỏ thu được là:", "options": ["$64$", "$36$", "$8$", "$48$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Một bồn hoa hình thoi có cạnh $15\\text{ m}$, hai đường chéo dài $18\\text{ m}$ và $24\\text{ m}$. Chiều cao của bồn hoa đó là:", "options": ["$14,4\\text{ m}$", "$12\\text{ m}$", "$15\\text{ m}$", "$16\\text{ m}$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Một mảnh đất hình bình hành có chu vi $100\\text{ m}$, cạnh dài hơn cạnh ngắn $10\\text{ m}$. Cạnh dài của mảnh đất là:", "options": ["$30\\text{ m}$", "$25\\text{ m}$", "$35\\text{ m}$", "$20\\text{ m}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Một hình thang có diện tích $180\\text{ cm}^2$, chiều cao $12\\text{ cm}$. Nếu đáy lớn dài gấp rưỡi đáy bé thì độ dài đáy lớn là:", "options": ["$18\\text{ cm}$", "$12\\text{ cm}$", "$24\\text{ cm}$", "$15\\text{ cm}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Chi phí mua cỏ phủ kín một sân vận động hình chữ nhật kích thước $105\\text{ m} \\times 68\\text{ m}$ với giá $160\\,000$ đồng/m² là:", "options": ["$1\\,142\\,400\\,000$ đồng", "$1\\,140\\,000\\,000$ đồng", "$571\\,200\\,000$ đồng", "$2\\,284\\,800\\,000$ đồng"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Một biển quảng cáo hình lục giác đều cạnh $1\\text{ m}$. Người ta lắp đèn viền xung quanh với giá $150\\,000$ đồng/m. Số tiền làm viền đèn là:", "options": ["$900\\,000$ đồng", "$600\\,000$ đồng", "$1\\,200\\,000$ đồng", "$750\\,000$ đồng"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Nối các trung điểm 4 cạnh của hình chữ nhật có kích thước $16\\text{ cm} \\times 12\\text{ cm}$ ta được hình thoi có diện tích:", "options": ["$96\\text{ cm}^2$", "$192\\text{ cm}^2$", "$48\\text{ cm}^2$", "$144\\text{ cm}^2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một hình vuông và một tam giác đều có cùng chu vi là $36\\text{ cm}$. Tỉ số cạnh của hình vuông so với cạnh của tam giác đều là:", "options": ["$3/4$", "$4/3$", "$1/2$", "$2/3$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Một khu vườn hình thang cân có đáy lớn 50 m, đáy bé 30 m, chiều cao 20 m:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Diện tích của khu vườn là 800 m².", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Người ta làm một lối đi hình bình hành có đáy 2 m chạy cắt ngang vườn theo chiều cao, diện tích lối đi là 40 m².", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Diện tích phần đất trồng cây còn lại là 760 m².", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Lối đi chiếm hơn 10% diện tích của cả khu vườn.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình chữ nhật ABCD có AB = 20 cm, BC = 15 cm. Điểm E là trung điểm của AB:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Diện tích hình chữ nhật ABCD bằng 300 cm².", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tứ giác EBCD là hình thang vuông.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Diện tích tứ giác EBCD là 225 cm².", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Diện tích tam giác ADE bằng một nửa diện tích hình chữ nhật ABCD.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình thoi có hiệu độ dài hai đường chéo là 4 cm, tổng độ dài hai đường chéo là 28 cm. Diện tích của hình thoi đó bằng bao nhiêu cm²?", "answer": "96"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một mảnh vườn hình chữ nhật có chu vi 84 m. Chiều dài gấp rưỡi chiều rộng. Diện tích của mảnh vườn đó là bao nhiêu m²?", "answer": "432"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một hình thang có diện tích 150 cm², chiều cao 10 cm. Biết đáy lớn hơn đáy bé 6 cm. Độ dài đáy lớn là bao nhiêu cm?", "answer": "18"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một sân trường hình chữ nhật có chu vi 180 m. Người ta mở rộng mỗi chiều thêm 5 m thì diện tích tăng thêm bao nhiêu m²?", "answer": "925"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Một mảnh sân hình chữ nhật dài 16 m, rộng 10 m. Người ta xây một bồn hoa hình thoi ở giữa có hai đường chéo dài 6 m và 4 m, phần còn lại lát gạch.\na) Tính diện tích mảnh sân.\nb) Tính diện tích phần lát gạch.",
            "rubric": "a) Diện tích sân: 16 x 10 = 160 m² (0.5đ).\nb) Diện tích bồn hoa hình thoi: (1/2) x 6 x 4 = 12 m². Diện tích phần lát gạch: 160 - 12 = 148 m² (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Bác Tư có một mảnh đất hình bình hành có đáy 30 m, chiều cao tương ứng 18 m.\na) Tính diện tích mảnh đất của bác Tư.\nb) Bác Tư muốn bán mảnh đất với giá 15 triệu đồng/m². Tính tổng số tiền bác Tư thu được khi bán hết mảnh đất đó.",
            "rubric": "a) Diện tích: 30 x 18 = 540 m² (0.5đ).\nb) Tổng số tiền bán đất: 540 x 15 000 000 = 8 100 000 000 đồng (8,1 tỉ đồng) (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Một bờ kè bằng bê tông có mặt cắt ngang là hình thang cân với đáy trên rộng 3 m, đáy dưới rộng 7 m và chiều cao kè là 4 m.\na) Tính diện tích mặt cắt ngang của bờ kè.\nb) Chiều dài toàn bộ bờ kè là 250 m. Tính thể tích khối bê tông cần đúc bờ kè (biết thể tích = diện tích mặt cắt ngang x chiều dài).",
            "rubric": "a) Diện tích mặt cắt: (3 + 7) x 4 : 2 = 20 m² (0.5đ).\nb) Thể tích bê tông cần dùng: 20 x 250 = 5000 m³ (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c4_6_bai4_test3"] = {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương IV: Hình phẳng - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hình chữ nhật có chu vi không đổi $P = 40\\text{ cm}$. Khi diện tích đạt giá trị lớn nhất thì diện tích đó bằng:", "options": ["$100\\text{ cm}^2$", "$96\\text{ cm}^2$", "$84\\text{ cm}^2$", "$64\\text{ cm}^2$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một hình lục giác đều có diện tích $96\\text{ cm}^2$. Nối 3 đỉnh không liền kề nhau ta được một tam giác đều có diện tích là:", "options": ["$48\\text{ cm}^2$", "$32\\text{ cm}^2$", "$64\\text{ cm}^2$", "$24\\text{ cm}^2$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Một hình thoi có độ dài hai đường chéo hơn kém nhau $4\\text{ cm}$ và diện tích bằng $96\\text{ cm}^2$. Cạnh của hình thoi đó là:", "options": ["$10\\text{ cm}$", "$12\\text{ cm}$", "$8\\text{ cm}$", "$15\\text{ cm}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Một thửa ruộng hình thang có diện tích $450\\text{ m}^2$, đáy lớn gấp đôi đáy bé. Khi mở rộng cả hai đáy thêm $5\\text{ m}$ thì diện tích tăng thêm $75\\text{ m}^2$. Độ dài hai đáy ban đầu lần lượt là:", "options": ["$10\\text{ m}$ và $20\\text{ m}$", "$15\\text{ m}$ và $30\\text{ m}$", "$12\\text{ m}$ và $24\\text{ m}$", "$20\\text{ m}$ và $40\\text{ m}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Cho hình bình hành $ABCD$. Lấy $M, N$ lần lượt là trung điểm của $AB$ và $CD$. Tỉ số diện tích tứ giác $AMCN$ so với diện tích hình bình hành $ABCD$ là:", "options": ["$1/2$", "$1/3$", "$2/3$", "$1/4$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Một mảnh đất hình vuông được chia thành 5 hình chữ nhật có diện tích bằng nhau nhờ các đường thẳng song song. Nếu chu vi mỗi hình chữ nhật nhỏ là $48\\text{ m}$ thì diện tích mảnh đất ban đầu là:", "options": ["$400\\text{ m}^2$", "$225\\text{ m}^2$", "$625\\text{ m}^2$", "$900\\text{ m}^2$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho hình thang cân $ABCD$ có đường chéo $AC \\perp BD$, chiều cao $h = 8\\text{ cm}$. Diện tích của hình thang cân đó là:", "options": ["$64\\text{ cm}^2$", "$32\\text{ cm}^2$", "$128\\text{ cm}^2$", "$96\\text{ cm}^2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cắt 4 góc của một hình vuông cạnh $a$ để được một hình bát giác đều. Độ dài cạnh của bát giác đều được tính theo $a$ xấp xỉ bằng:", "options": ["$0,414 a$", "$0,5 a$", "$0,333 a$", "$0,25 a$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Người ta muốn uốn một sợi dây thép dài $60\\text{ cm}$ thành một hình có diện tích lớn nhất. Hình nên uốn là:", "options": ["Hình lục giác đều", "Hình vuông", "Hình tam giác đều", "Hình chữ nhật có tỉ lệ 2:1"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Một hình chữ nhật có kích thước $a \\times b$. Tăng $a$ thêm $20\\%$ và giảm $b$ đi $20\\%$ thì diện tích thay đổi thế nào?", "options": ["Giảm $4\\%$", "Tăng $4\\%$", "Không thay đổi", "Giảm $2\\%$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một mảnh vườn hình chữ nhật có chu vi $120\\text{ m}$. Xung quanh vườn làm đường đi rộng $1\\text{ m}$. Diện tích con đường đó là:", "options": ["$116\\text{ m}^2$", "$124\\text{ m}^2$", "$120\\text{ m}^2$", "$108\\text{ m}^2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho lục giác đều $ABCDEF$. Tỉ số diện tích của tam giác $ABC$ so với lục giác đều $ABCDEF$ bằng:", "options": ["$1/6$", "$1/3$", "$1/4$", "$1/12$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hình vuông ABCD cạnh 20 cm. Lấy các điểm M, N, P, Q lần lượt trên các cạnh AB, BC, CD, DA sao cho AM = BN = CP = DQ = 5 cm:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Bốn tam giác vuông AMQ, BNM, CPN, DQP bằng nhau.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Tứ giác MNPQ là hình vuông.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Diện tích mỗi tam giác vuông ở góc là 37,5 cm².", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Diện tích hình vuông MNPQ là 250 cm².", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Một khu đất hình bình hành ABCD có AB = 60 m, BC = 40 m. Chiều cao hạ từ A xuống CD là 30 m:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Diện tích khu đất hình bình hành ABCD là 1800 m².", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Chiều cao hạ từ A xuống cạnh BC bằng 45 m.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Chu vi của khu đất là 200 m.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Độ dài đường chéo BD luôn bằng đường chéo AC.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một hình chữ nhật có diện tích 300 cm², chiều dài hơn chiều rộng 5 cm. Chu vi của hình chữ nhật đó bằng bao nhiêu cm?", "answer": "70"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một hình thang cân có đáy nhỏ 12 cm, đáy lớn 20 cm và diện tích 128 cm². Chiều cao của hình thang cân bằng bao nhiêu cm?", "answer": "8"},
        {"id": 3, "level": "Vận dụng cao", "question": "Một mảnh đất hình chữ nhật có chu vi 160 m. Người ta đào một cái ao hình vuông có cạnh bằng chiều rộng mảnh đất, phần còn lại là mảnh vườn hình chữ nhật có diện tích 700 m². Chiều dài mảnh đất ban đầu là bao nhiêu mét?", "answer": "70"},
        {"id": 4, "level": "Vận dụng cao", "question": "Một tấm bìa hình lục giác đều có diện tích 120 cm². Người ta cắt bỏ 6 tam giác đều nhỏ ở 6 góc để được một hình lục giác đều mới có cạnh bằng 1/2 cạnh ban đầu. Diện tích hình lục giác đều mới là bao nhiêu cm²?", "answer": "30"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho hình chữ nhật ABCD có diện tích 180 cm². Trên cạnh AB lấy điểm M sao cho AM = 1/3 AB. Trên cạnh CD lấy điểm N sao cho CN = 1/3 CD.\na) Chứng minh tứ giác AMCN là hình bình hành.\nb) Tính diện tích hình bình hành AMCN.",
            "rubric": "a) AM // CN (thuộc AB // CD) và AM = CN = 1/3 AB => AMCN là hình bình hành (0.5đ).\nb) AMCN có đáy AM = 1/3 AB và chiều cao bằng BC (chiều rộng hình chữ nhật). Do đó S(AMCN) = 1/3 S(ABCD) = 1/3 x 180 = 60 cm² (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Một khu liên hợp thể thao gồm một sân bóng đá hình chữ nhật kích thước 100 m x 60 m và hai khu vực phụ hình thang cân gắn vào hai đầu chiều rộng sân bóng, mỗi hình thang cân có đáy lớn 60 m (chung với sân), đáy bé 40 m và chiều cao 15 m.\na) Tính diện tích sân bóng đá.\nb) Tính tổng diện tích của toàn bộ khu liên hợp thể thao đó.\nc) Chi phí trải thảm cỏ nhân tạo cho cả khu liên hợp là 140 000 đồng/m². Tính tổng chi phí trải thảm cỏ.",
            "rubric": "a) Diện tích sân bóng đá: 100 x 60 = 6000 m² (0.3đ).\nb) Diện tích 1 khu phụ hình thang cân: (60 + 40) x 15 : 2 = 750 m². Cả 2 khu phụ: 750 x 2 = 1500 m². Tổng diện tích cả khu: 6000 + 1500 = 7500 m² (0.4đ).\nc) Chi phí trải thảm cỏ: 7500 x 140 000 = 1 050 000 000 đồng (1,05 tỉ đồng) (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Bác An muốn rào một khu đất hình chữ nhật có diện tích 600 m² giáp với một bờ sông thẳng (bên bờ sông không cần rào). Bác có sẵn 70 m lưới thép B40 để làm 3 mặt còn lại của hàng rào.\na) Gọi chiều rộng của mảnh đất vuông góc với bờ sông là x (m). Lập biểu thức biểu thị chiều dài song song với bờ sông theo x.\nb) Tìm các giá trị của x để bác An sử dụng hết đúng 70 m lưới thép đó.\nc) Với kích thước nào thì diện tích khu đất đạt giá trị lớn nhất?",
            "rubric": "a) Chiều dài song song bờ sông: y = 70 - 2x (m) (0.3đ).\nb) Diện tích: x(70 - 2x) = 600 => 70x - 2x² = 600 => x² - 35x + 300 = 0 => (x - 15)(x - 20) = 0 => x = 15 hoặc x = 20 (0.4đ). Nếu x = 15 m thì chiều dài là 40 m (15 x 40 = 600 m²). Nếu x = 20 m thì chiều dài là 30 m (20 x 30 = 600 m²).\nc) Diện tích S(x) = -2(x² - 35x) = -2(x - 17,5)² + 612,5. Diện tích đạt lớn nhất bằng 612,5 m² khi x = 17,5 m và chiều dài y = 35 m (0.3đ)."
        }
    ]
}
