# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG III: GÓC VÀ ĐƯỜNG THẲNG SONG SONG
PHẦN 1:
- BÀI 8: GÓC Ở VỊ TRÍ ĐẶC BIỆT. TIA PHÂN GIÁC CỦA MỘT GÓC (c3_7_bai1)
- BÀI 9: HAI ĐƯỜNG THẲNG SONG SONG VÀ DẤU HIỆU NHẬN BIẾT (c3_7_bai2)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART1 = {}

# ==============================================================================
# BÀI 8: GÓC Ở VỊ TRÍ ĐẶC BIỆT. TIA PHÂN GIÁC CỦA MỘT GÓC (c3_7_bai1)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c3_7_bai1_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 8: Góc đặc biệt. Tia phân giác - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hai góc kề bù là hai góc:", "options": ["Vừa kề nhau vừa bù nhau (có tổng số đo bằng $180^\\circ$)", "Có tổng số đo bằng $90^\\circ$", "Có chung một cạnh và không có điểm trong chung", "Có hai cạnh là hai tia đối nhau"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hai góc đối đỉnh là hai góc mà:", "options": ["Mỗi cạnh của góc này là tia đối của một cạnh của góc kia", "Có tổng số đo bằng $180^\\circ$", "Có chung đỉnh và bằng nhau", "Nằm đối diện nhau"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Khẳng định nào sau đây là đúng về hai góc đối đỉnh?", "options": ["Hai góc đối đỉnh thì bằng nhau", "Hai góc bằng nhau thì đối đỉnh", "Hai góc đối đỉnh có tổng số đo bằng $180^\\circ$", "Hai góc đối đỉnh luôn là góc nhọn"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Tia phân giác của một góc là tia:", "options": ["Nằm trong góc và tạo với hai cạnh của góc đó hai góc bằng nhau", "Nằm ngoài góc đó", "Vuông góc với một cạnh của góc", "Cắt cạnh đối diện của góc"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Nếu tia $Oz$ là tia phân giác của góc $\\widehat{xOy}$ có số đo $80^\\circ$ thì số đo của góc $\\widehat{xOz}$ bằng:", "options": ["$40^\\circ$", "$80^\\circ$", "$160^\\circ$", "$20^\\circ$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Hai góc bù nhau là hai góc có tổng số đo bằng:", "options": ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$60^\\circ$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho hai góc $\\widehat{xOy}$ và $\\widehat{yOz}$ kề bù. Biết $\\widehat{xOy} = 60^\\circ$, số đo của góc $\\widehat{yOz}$ là:", "options": ["$120^\\circ$", "$30^\\circ$", "$60^\\circ$", "$180^\\circ$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho hai đường thẳng $AB$ và $CD$ cắt nhau tại $O$. Biết $\\widehat{AOC} = 50^\\circ$. Số đo của góc đối đỉnh $\\widehat{BOD}$ là:", "options": ["$50^\\circ$", "$130^\\circ$", "$40^\\circ$", "$180^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Hai góc phụ nhau là hai góc có tổng số đo bằng:", "options": ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$", "$360^\\circ$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cho $\\widehat{xOy} = 110^\\circ$. Góc kề bù với $\\widehat{xOy}$ có số đo bằng:", "options": ["$70^\\circ$", "$110^\\circ$", "$90^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Tia $Ot$ là tia phân giác của $\\widehat{mOn}$. Biết $\\widehat{mOt} = 35^\\circ$, số đo của $\\widehat{mOn}$ là:", "options": ["$70^\\circ$", "$35^\\circ$", "$17,5^\\circ$", "$140^\\circ$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Số đo góc tạo bởi hai tia phân giác của hai góc kề bù bằng:", "options": ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$", "$60^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai đường thẳng xx' và yy' cắt nhau tại điểm O, biết góc xOy = 70°:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Góc x'Oy' là góc đối đỉnh với góc xOy, nên x'Oy' = 70°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc xOy' kề bù với góc xOy, nên góc xOy' = 180° - 70° = 110°.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Góc x'Oy đối đỉnh với góc xOy', nên góc x'Oy = 110°.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Tổng số đo của 4 góc đỉnh O tạo thành bằng 180°.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho góc xOy = 100°. Vẽ tia Oz là tia phân giác của góc xOy, vẽ tia Ot là tia đối của tia Oz:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Tia Oz nằm giữa hai tia Ox và Oy.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số đo góc xOz = yOz = 50°.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Góc xOt kề bù với góc xOz, nên góc xOt = 130°.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Góc yOt = 50°.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hai góc kề bù nhau, trong đó một góc có số đo bằng 75°. Góc còn lại có số đo bằng bao nhiêu độ?", "answer": "105"},
        {"id": 2, "level": "Thông hiểu", "question": "Cho góc aOb = 130°, tia Oc là tia phân giác của góc aOb. Số đo góc aOc bằng bao nhiêu độ?", "answer": "65"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Hai đường thẳng cắt nhau tạo thành 4 góc. Biết tổng số đo của 3 trong 4 góc đó bằng 250°. Số đo của góc thứ tư là bao nhiêu độ?", "answer": "110"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho hai góc kề nhau xOy và yOz có tổng số đo bằng 140°. Biết tia phân giác của xOy và yOz tạo với nhau một góc bằng bao nhiêu độ?", "answer": "70"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Hai đường thẳng AB và CD cắt nhau tại O tạo thành góc AOC có số đo bằng 40°.\na) Tính số đo các góc BOD, AOD, BOC.\nb) Vẽ tia phân giác OM của góc AOC và tia phân giác ON của góc BOD. Chứng tỏ hai tia OM và ON là hai tia đối nhau.",
            "rubric": "a) BOD = AOC = 40° (đối đỉnh). AOD = 180° - 40° = 140° (kề bù). BOC = AOD = 140° (đối đỉnh) (0.5đ).\nb) AOM = 20°, BON = 20°. Góc MON = MOA + AOD + DON = 20° + 140° + 20° = 180° => OM và ON là hai tia đối nhau (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho góc bẹt xOy. Vẽ tia Oz sao cho góc xOz = 70°.\na) Tính số đo góc yOz.\nb) Vẽ tia Om là tia phân giác của góc xOz, tia On là tia phân giác của góc yOz. Tính số đo góc mOn.",
            "rubric": "a) yOz = 180° - 70° = 110° (vì kề bù với xOz) (0.4đ).\nb) mOz = 70° : 2 = 35°; zOn = 110° : 2 = 55° (0.3đ). Vì Oz nằm giữa Om và On nên mOn = mOz + zOn = 35° + 55° = 90° (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một chiếc kéo cắt vải khi mở ra tạo thành hai góc đối đỉnh ở hai phía của trục ốc. Biết góc giữa hai mũi kéo là 35°.\na) Tính góc giữa hai tay cầm của kéo.\nb) Nếu người thợ mở rộng thêm góc ở mũi kéo thêm 15° thì góc ở tay cầm thay đổi như thế nào và bằng bao nhiêu độ?",
            "rubric": "a) Vì hai góc ở mũi kéo và tay cầm đối đỉnh nhau qua trục ốc nên góc ở tay cầm bằng góc ở mũi kéo và bằng 35° (0.5đ).\nb) Góc ở tay cầm cũng tăng thêm đúng 15° và bằng 35° + 15° = 50° (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c3_7_bai1_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 8: Góc đặc biệt. Tia phân giác - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$, biết $\\widehat{xOy} = 2\\widehat{yOz}$. Số đo góc $\\widehat{xOy}$ là:", "options": ["$120^\\circ$", "$60^\\circ$", "$90^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho hai góc đối đỉnh $\\widehat{AOB}$ và $\\widehat{COD}$. Biết $\\widehat{AOB} + \\widehat{COD} = 140^\\circ$. Số đo của góc $\\widehat{AOC}$ là:", "options": ["$110^\\circ$", "$70^\\circ$", "$140^\\circ$", "$40^\\circ$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tia $Oz$ nằm giữa hai tia $Ox$ và $Oy$ sao cho $\\widehat{xOz} = 40^\\circ$ và $\\widehat{yOz} = 40^\\circ$. Kết luận nào sau đây đúng?", "options": ["$Oz$ là tia phân giác của $\\widehat{xOy}$", "$Oz$ vuông góc với $Ox$", "$\\widehat{xOy} = 40^\\circ$", "$Oz$ là tia đối của $Ox$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho góc $\\widehat{xOy} = 120^\\circ$, tia phân giác $Oz$. Vẽ tia $Ot$ nằm trong góc $\\widehat{xOy}$ sao cho $\\widehat{xOt} = 30^\\circ$. Số đo góc $\\widehat{zOt}$ là:", "options": ["$30^\\circ$", "$60^\\circ$", "$90^\\circ$", "$45^\\circ$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Hai đường thẳng $xx'$ và $yy'$ cắt nhau tại $O$. Biết $\\widehat{xOy} - \\widehat{xOy'} = 40^\\circ$. Số đo góc $\\widehat{xOy}$ là:", "options": ["$110^\\circ$", "$70^\\circ$", "$140^\\circ$", "$120^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Cho ba tia chung gốc $Ox, Oy, Oz$ sao cho $\\widehat{xOy} = 80^\\circ, \\widehat{yOz} = 60^\\circ, \\widehat{xOz} = 140^\\circ$. Tia nằm giữa hai tia còn lại là:", "options": ["Tia $Oy$", "Tia $Ox$", "Tia $Oz$", "Không có tia nào nằm giữa"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Góc tạo bởi hai tia phân giác của hai góc kề nhau có tổng số đo bằng $150^\\circ$ là:", "options": ["$75^\\circ$", "$150^\\circ$", "$90^\\circ$", "$60^\\circ$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho $\\widehat{xOy} = 70^\\circ$. Vẽ tia $Oz$ là tia đối của $Ox$, tia $Ot$ là tia đối của $Oy$. Góc đối đỉnh với $\\widehat{yOz}$ là:", "options": ["$\\widehat{xOt}$", "$\\widehat{xOy}$", "$\\widehat{zOt}$", "$\\widehat{yOt}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho 4 đường thẳng phân biệt cùng đi qua điểm $O$. Số cặp góc đối đỉnh (khác góc bẹt) tạo thành là:", "options": ["$12$", "$8$", "$16$", "$6$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho góc bẹt $\\widehat{AOB}$. Trên cùng một nửa mặt phẳng bờ $AB$ vẽ hai tia $OC, OD$ sao cho $\\widehat{AOC} = 40^\\circ, \\widehat{BOD} = 50^\\circ$. Số đo góc $\\widehat{COD}$ là:", "options": ["$90^\\circ$", "$80^\\circ$", "$100^\\circ$", "$45^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho $\\widehat{xOy} = 100^\\circ$. Tia $Oz$ nằm giữa $Ox$ và $Oy$ sao cho $\\widehat{xOz} = 2\\widehat{zOy}$. Số đo góc $\\widehat{xOz}$ là:", "options": ["$\\frac{200^\\circ}{3}$", "$50^\\circ$", "$60^\\circ$", "$75^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$. Biết tia phân giác của $\\widehat{AOB}$ hợp với tia $OC$ một góc $130^\\circ$. Số đo $\\widehat{AOB}$ là:", "options": ["$100^\\circ$", "$80^\\circ$", "$120^\\circ$", "$50^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho góc vuông xOy. Vẽ tia Oz nằm giữa Ox và Oy. Vẽ tia Om là phân giác của góc xOz, tia On là phân giác của góc zOy:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "xOz + zOy = 90°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "mOz = (1/2) xOz và zOn = (1/2) zOy.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số đo góc mOn = 45° không phụ thuộc vào vị trí của tia Oz trong góc xOy.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Nếu xOz = 30° thì mOn = 60°.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai đường thẳng AB và CD cắt nhau tại O. Biết góc AOC + góc BOD = 100°:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Hai góc AOC và BOD là hai góc đối đỉnh nên AOC = BOD = 50°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc AOD kề bù với góc AOC nên AOD = 130°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Góc BOC = 130°.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Tia phân giác của AOC và tia phân giác của AOD vuông góc với nhau.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hai góc kề bù xOy và yOz. Biết xOy hơn yOz một góc 40°. Số đo góc xOy bằng bao nhiêu độ?", "answer": "110"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Qua điểm O vẽ 5 đường thẳng phân biệt. Có bao nhiêu cặp góc đối đỉnh (khác góc bẹt) được tạo thành?", "answer": "20"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho góc xOy = 80°. Vẽ tia Oz là tia đối của Ox. Gọi Ot là tia phân giác của yOz. Số đo góc xOt bằng bao nhiêu độ?", "answer": "130"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hai góc kề bù AOB và BOC. Tia phân giác OM của AOB vuông góc với tia phân giác ON của BOC. Số đo góc MON bằng bao nhiêu độ?", "answer": "90"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai góc kề bù xOy và yOz có tỉ số số đo là 4 : 5.\na) Tính số đo mỗi góc xOy và yOz.\nb) Vẽ tia phân giác Ot của góc yOz. Tính số đo góc xOt.",
            "rubric": "a) xOy + yOz = 180°. xOy = 180° x 4/9 = 80°; yOz = 180° x 5/9 = 100° (0.5đ).\nb) yOt = 100° : 2 = 50°. Vì Oy nằm giữa Ox và Ot nên xOt = xOy + yOt = 80° + 50° = 130° (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho góc xOy = 120°. Trong góc xOy vẽ hai tia Om và On sao cho Om vuông góc với Ox và On vuông góc với Oy.\na) Chứng tỏ tia On nằm giữa hai tia Ox và Om.\nb) Tính số đo góc mOn.\nc) Chứng minh tia phân giác của góc xOy cũng là tia phân giác của góc mOn.",
            "rubric": "a) xOm = 90° < 120° nên Om nằm trong góc. xOn = 120° - 90° = 30° < 90° nên On nằm giữa Ox và Om (0.3đ).\nb) mOn = xOm - xOn = 90° - 30° = 60° (0.4đ).\nc) Gọi Ot là phân giác xOy => xOt = 60°. Tia Ot nằm giữa Om và On và tạo với mỗi tia một góc 30° => Ot là phân giác mOn (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho điểm O nằm trên đường thẳng xy. Trên cùng một nửa mặt phẳng bờ xy, vẽ các tia Oz, Ot sao cho góc xOz = 50° và góc yOt = 65°.\na) Tính số đo góc zOt.\nb) Tia Oz có phải là tia phân giác của góc xOt không? Vì sao?",
            "rubric": "a) xOy = 180° (góc bẹt). xOt = 180° - 65° = 115°. Vì xOz = 50° < xOt = 115° nên Oz nằm giữa Ox và Ot => zOt = 115° - 50° = 65° (0.5đ).\nb) xOz = 50° ≠ zOt = 65° nên Oz không phải là tia phân giác của góc xOt (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c3_7_bai1_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 8: Góc đặc biệt. Tia phân giác - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $n$ đường thẳng phân biệt cùng đi qua điểm $O$ ($n \\geq 2$). Số cặp góc đối đỉnh (nhỏ hơn $180^\\circ$) được tạo thành là:", "options": ["$n(n - 1)$", "$2n(n - 1)$", "$\\frac{n(n - 1)}{2}$", "$n^2$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho góc $\\widehat{xOy} = 140^\\circ$. Vẽ phía ngoài góc đó hai tia $Oz \\perp Ox$ và $Ot \\perp Oy$. Số đo góc $\\widehat{zOt}$ là:", "options": ["$40^\\circ$", "$50^\\circ$", "$60^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$. Biết tia phân giác $OD$ của góc $\\widehat{AOB}$ vuông góc với đường thẳng chứa tia $OB$. Khi đó góc $\\widehat{AOB}$ là:", "options": ["Góc bẹt", "Góc vuông", "Góc nhọn", "Không tồn tại"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho góc bẹt $\\widehat{xOy}$. Trên cùng một nửa mặt phẳng bờ $xy$, vẽ 2024 tia phân biệt chung gốc $O$ (không trùng $Ox, Oy$). Số góc tạo thành đỉnh $O$ tất cả là:", "options": ["$\\frac{2026 \\cdot 2025}{2}$", "$\\frac{2024 \\cdot 2023}{2}$", "$2024 \\cdot 2025$", "$2026^2$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Cho $\\widehat{AOB} = 90^\\circ$. Bên trong góc đó vẽ hai tia $OC, OD$ sao cho $\\widehat{AOC} = \\widehat{BOD} = 60^\\circ$. Số đo góc $\\widehat{COD}$ là:", "options": ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$15^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho hai góc kề nhau $\\widehat{xOy}$ và $\\widehat{yOz}$ có tổng số đo bằng $100^\\circ$, hiệu số đo bằng $40^\\circ$. Góc tạo bởi tia phân giác của hai góc đó có số đo là:", "options": ["$50^\\circ$", "$40^\\circ$", "$20^\\circ$", "$70^\\circ$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho góc $\\widehat{xOy} = \\alpha$ ($0^\\circ < \\alpha < 180^\\circ$). Lấy $Om$ là phân giác của $\\widehat{xOy}$. Lấy $On$ là phân giác của $\\widehat{xOm}$. Góc $\\widehat{yOn}$ có số đo bằng:", "options": ["$\\frac{3\\alpha}{4}$", "$\\frac{\\alpha}{4}$", "$\\frac{\\alpha}{2}$", "$\\frac{2\\alpha}{3}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho ba tia $Ox, Oy, Oz$ sao cho $\\widehat{xOy} = \\widehat{yOz} = \\widehat{zOx} = 120^\\circ$. Gọi $Ox', Oy', Oz'$ lần lượt là các tia đối của $Ox, Oy, Oz$. Nhận định nào sau đây đúng?", "options": ["$Ox'$ là tia phân giác của $\\widehat{yOz}$", "$Ox'$ vuông góc với $Oy$", "$\\widehat{x'Oy} = 30^\\circ$", "Các tia $Ox', Oy'$ trùng nhau"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho 6 đường thẳng phân biệt cùng đi qua điểm $O$. Số góc nhọn tạo thành (không kể góc bẹt và góc không) là:", "options": ["$60$ góc (tính cả góc đơn và góc ghép nhọn)", "$30$", "$12$", "$6$"], "correct": 1},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho góc $\\widehat{xOy} = 150^\\circ$. Vẽ tia $Oz$ nằm giữa $Ox$ và $Oy$ sao cho $\\widehat{xOz} = 4\\widehat{yOz}$. Số đo góc $\\widehat{xOz}$ là:", "options": ["$120^\\circ$", "$30^\\circ$", "$100^\\circ$", "$125^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$. Gọi $Om, On$ lần lượt là phân giác của $\\widehat{xOy}$ và $\\widehat{yOz}$. Kẻ tia $Ot$ là tia đối của $Om$. Số đo góc $\\widehat{tOn}$ là:", "options": ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$", "$135^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Hai góc bù nhau có tỉ số là $7 : 11$. Hiệu số đo của hai góc đó là:", "options": ["$40^\\circ$", "$30^\\circ$", "$50^\\circ$", "$20^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai góc kề nhau AOB và BOC có tổng số đo bằng 160° và hiệu số đo bằng 40° (AOB > BOC):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số đo góc AOB = (160° + 40°) : 2 = 100°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số đo góc BOC = 160° - 100° = 60°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tia phân giác của AOB và tia phân giác của BOC tạo với nhau góc 80°.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Vẽ tia đối của tia OB thì tia đó là tia phân giác của góc AOC.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho góc nhọn xOy. Vẽ tia Oz vuông góc với Ox (Oz và Oy cùng thuộc một nửa mặt phẳng bờ Ox). Vẽ tia Ot vuông góc với Oy (Ot và Ox cùng thuộc một nửa mặt phẳng bờ Oy):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "xOz = 90° và yOt = 90°.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Góc xOt = góc yOz (vì cùng phụ với góc zOt).", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Góc xOy + góc zOt = 180°.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Tia phân giác của góc xOy và tia phân giác của góc zOt vuông góc với nhau.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho biết n đường thẳng cùng đi qua điểm O tạo thành 72 cặp góc đối đỉnh (không kể góc bẹt). Số đường thẳng n bằng bao nhiêu?", "answer": "9"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho góc xOy = 135°. Vẽ tia Oz nằm trong góc xOy sao cho xOz = (1/2) zOy. Số đo góc zOy bằng bao nhiêu độ?", "answer": "90"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho hai góc kề bù nhau có tỉ số số đo bằng 1 : 3. Góc lớn hơn có số đo bằng bao nhiêu độ?", "answer": "135"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho góc xOy = 120°. Kẻ các tia Oz và Ot nằm trong góc đó sao cho xOz = 90° và yOt = 90°. Số đo góc zOt bằng bao nhiêu độ?", "answer": "60"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho góc bẹt xOy. Trên cùng một nửa mặt phẳng bờ xy, vẽ các tia Om, On sao cho góc xOm = 30° và góc yOn = 60°.\na) Chứng tỏ tia On vuông góc với tia Om.\nb) Vẽ tia phân giác Oz của góc mOn. Tính số đo góc xOz.",
            "rubric": "a) yOm = 180° - 30° = 150°. mOn = yOm - yOn = 150° - 60° = 90° => Om vuông góc với On (0.5đ).\nb) mOz = 90° : 2 = 45°. xOz = xOm + mOz = 30° + 45° = 75° (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho góc vuông xOy. Vẽ tia Oz nằm giữa hai tia Ox và Oy. Gọi Om là tia phân giác của góc xOz, On là tia phân giác của góc zOy.\na) Chứng minh rằng số đo góc mOn luôn không đổi khi Oz thay đổi trong góc xOy.\nb) Tìm vị trí của tia Oz để góc xOm = góc yOn.",
            "rubric": "a) mOn = mOz + zOn = (1/2) xOz + (1/2) zOy = (1/2)(xOz + zOy) = 1/2 x 90° = 45° (không đổi) (0.5đ).\nb) xOm = yOn <=> (1/2) xOz = (1/2) zOy <=> xOz = zOy. Vậy Oz là tia phân giác của góc vuông xOy (khi đó xOz = 45°) (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho 2025 đường thẳng phân biệt cùng đi qua một điểm O.\na) Có bao nhiêu góc đỉnh O được tạo thành (kể cả góc bẹt)?\nb) Chứng minh rằng trong các góc tạo thành không có góc nào lớn hơn 180°, luôn tồn tại ít nhất một góc có số đo không vượt quá (360 / 4050)°.",
            "rubric": "a) 2025 đường thẳng tạo thành 4050 tia chung gốc O. Số góc tạo thành là: 4050 x 4049 : 2 = 8 199 225 góc (0.4đ).\nb) 4050 tia chung gốc chia mặt phẳng thành 4050 góc kề nhau không có điểm trong chung. Tổng 4050 góc này bằng 360° (0.3đ). Theo nguyên lí Dirichlet, nếu tất cả các góc đều lớn hơn 360° / 4050 thì tổng sẽ lớn hơn 360° (mâu thuẫn). Vậy tồn tại ít nhất một góc có số đo ≤ 360° / 4050 = (4/45)° (0.3đ)."
        }
    ]
}


# ==============================================================================
# BÀI 9: HAI ĐƯỜNG THẲNG SONG SONG VÀ DẤU HIỆU NHẬN BIẾT (c3_7_bai2)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART1["c3_7_bai2_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 9: Hai đường thẳng song song - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hai đường thẳng song song là hai đường thẳng:", "options": ["Không có điểm chung nào", "Có đúng một điểm chung", "Có vô số điểm chung", "Cắt nhau"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hai góc so le trong bằng nhau thì hai đường thẳng đó:", "options": ["Song song với nhau", "Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Nếu đường thẳng $c$ cắt hai đường thẳng $a$ và $b$ tạo thành một cặp góc đồng vị bằng nhau thì:", "options": ["$a \\parallel b$", "$a \\perp b$", "$a$ cắt $b$", "$a$ trùng $b$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Kí hiệu hai đường thẳng $a$ và $b$ song song với nhau là:", "options": ["$a \\parallel b$", "$a \\perp b$", "$a = b$", "$a \\subset b$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Hai góc trong cùng phía tạo bởi một đường thẳng cắt hai đường thẳng song song có tổng số đo bằng:", "options": ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$60^\\circ$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Qua một điểm ở ngoài một đường thẳng, có bao nhiêu đường thẳng song song với đường thẳng đó?", "options": ["Chỉ có 1 đường thẳng duy nhất", "Có 2 đường thẳng", "Có vô số đường thẳng", "Không có đường thẳng nào"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Đường thẳng $c$ cắt $a$ và $b$ tại $A$ và $B$. Biết một cặp góc so le trong $\\widehat{A_1} = 60^\\circ$ và $\\widehat{B_1} = 60^\\circ$. Kết luận nào sau đây đúng?", "options": ["$a \\parallel b$", "$a$ cắt $b$", "$a \\perp b$", "Không xác định"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho $a \\parallel b$, đường thẳng $c$ cắt $a$ tại $A$ và cắt $b$ tại $B$. Biết $\\widehat{A_1} = 45^\\circ$. Số đo góc đồng vị $\\widehat{B_1}$ là:", "options": ["$45^\\circ$", "$135^\\circ$", "$90^\\circ$", "$60^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Cho $a \\parallel b$. Một góc so le trong có số đo $75^\\circ$. Góc so le trong còn lại có số đo là:", "options": ["$75^\\circ$", "$105^\\circ$", "$15^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cho $a \\parallel b$. Biết một góc trong cùng phía bằng $110^\\circ$. Góc trong cùng phía còn lại có số đo là:", "options": ["$70^\\circ$", "$110^\\circ$", "$90^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Hình ảnh nào sau đây trong thực tế cho ta hình ảnh về hai đường thẳng song song?", "options": ["Hai thanh ray của đường tàu hỏa", "Hai cạnh kề nhau của mặt bàn", "Hai kim đồng hồ lúc 3 giờ", "Hai chiếc kéo đang mở"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Dấu hiệu nào sau đây KHÔNG PHẢI là dấu hiệu nhận biết hai đường thẳng song song?", "options": ["Hai góc kề bù bằng nhau", "Một cặp góc so le trong bằng nhau", "Một cặp góc đồng vị bằng nhau", "Một cặp góc trong cùng phía bù nhau"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho đường thẳng c cắt hai đường thẳng a và b lần lượt tại A và B:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Nếu có một cặp góc so le trong bằng nhau thì cặp góc so le trong còn lại cũng bằng nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu có một cặp góc đồng vị bằng nhau thì các cặp góc đồng vị khác cũng bằng nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu hai góc so le trong có tổng số đo bằng 180° thì a song song với b.", "correct": False},
                {"key": "d", "level": "Thông hiểu", "text": "Nếu hai góc trong cùng phía bù nhau thì a song song với b.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình vẽ có đường thẳng c cắt a tại A và cắt b tại B, biết góc A1 = 120° và B2 = 60° (với A1 và B2 là hai góc trong cùng phía):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tổng số đo A1 + B2 = 120° + 60° = 180°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Vì hai góc trong cùng phía bù nhau nên đường thẳng a song song với đường thẳng b.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Góc so le trong với góc A1 cũng có số đo bằng 120°.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Đường thẳng a vuông góc với đường thẳng b.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Đường thẳng c cắt hai đường thẳng a và b. Biết một cặp góc đồng vị có số đo lần lượt là 65° và 65°. Hai đường thẳng a và b có song song với nhau không? (Trả lời: có hoặc không)", "answer": "có"},
        {"id": 2, "level": "Thông hiểu", "question": "Cho a // b, đường thẳng d cắt a và b. Biết một góc so le trong bằng 55°. Góc so le trong kia có số đo bằng bao nhiêu độ?", "answer": "55"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho a // b. Biết hai góc trong cùng phía có số đo là x và 2x. Giá trị của x bằng bao nhiêu độ?", "answer": "60"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Hai đường thẳng song song a và b bị cắt bởi đường thẳng c. Nếu một góc nhọn bằng 40° thì góc tù tạo thành có số đo bằng bao nhiêu độ?", "answer": "140"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hình vẽ: đường thẳng c cắt đường thẳng a tại A và cắt đường thẳng b tại B. Biết góc A1 = 50° và góc B1 = 50° (ở vị trí đồng vị).\na) Đường thẳng a có song song với đường thẳng b không? Vì sao?\nb) Tính số đo góc B2 (góc kề bù với góc B1).",
            "rubric": "a) Vì góc A1 = góc B1 = 50° mà hai góc này ở vị trí đồng vị nên a // b (0.5đ).\nb) Vì B2 kề bù với B1 nên B2 = 180° - B1 = 180° - 50° = 130° (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho góc xOy = 70°. Trên tia Ox lấy điểm A khác O. Qua A vẽ đường thẳng d song song với Oy sao cho tia Oy và d nằm trên cùng một nửa mặt phẳng bờ chứa tia Ox.\na) Vẽ hình theo diễn đạt trên.\nb) Tính số đo góc tạo bởi d và tia Ox.",
            "rubric": "a) Vẽ đúng góc xOy = 70°, lấy điểm A trên Ox, kẻ d // Oy chính xác (0.4đ).\nb) Gọi góc tạo bởi d và tia Ox là xAd. Vì d // Oy nên góc xAd và góc xOy là hai góc đồng vị => xAd = xOy = 70° (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Hai thanh của một chiếc thang gấp chữ A được giằng lại bằng một thanh ngang kim loại MN song song với mặt đất AB. Biết góc đỉnh tạo bởi hai chân thang là góc C = 60° và tam giác ABC cân tại C (góc A = góc B).\na) Tính số đo góc A và góc B.\nb) Tính các góc của tứ giác AMNB.",
            "rubric": "a) Tổng 3 góc trong tam giác ABC = 180° => A + B = 180° - 60° = 120°. Vì A = B nên A = B = 60° (0.5đ).\nb) Vì MN // AB nên góc CMN = góc A = 60° (đồng vị) => góc AMN = 180° - 60° = 120° (kề bù). Tương tự góc BNM = 120°. Vậy tứ giác AMNB có góc A = góc B = 60°, góc M = góc N = 120° (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART1["c3_7_bai2_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 9: Hai đường thẳng song song - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hình vẽ: $\\widehat{A} = 110^\\circ$ và $\\widehat{B} = 70^\\circ$ là hai góc trong cùng phía. Kết luận nào sau đây đúng?", "options": ["Hai đường thẳng chứa hai góc song song với nhau", "Hai đường thẳng cắt nhau", "Hai đường thẳng vuông góc", "Không kết luận được"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho tam giác $ABC$. Qua đỉnh $A$ vẽ đường thẳng $xy \\parallel BC$. Số đo góc $\\widehat{xAB}$ bằng:", "options": ["Số đo góc $\\widehat{B}$ (so le trong)", "Số đo góc $\\widehat{C}$", "Số đo góc $\\widehat{A}$", "$90^\\circ$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $a \\parallel b$. Đường thẳng $c$ cắt $a$ và $b$. Biết tỉ số của hai góc trong cùng phía là $2 : 3$. Số đo của góc lớn là:", "options": ["$108^\\circ$", "$72^\\circ$", "$120^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho hình vẽ: tia $Ax \\parallel By$. Biết $\\widehat{OAx} = 40^\\circ, \\widehat{OBy} = 50^\\circ$ (cùng hướng về phía trong). Góc $\\widehat{AOB}$ có số đo là:", "options": ["$90^\\circ$", "$10^\\circ$", "$80^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Cho hai đường thẳng song song $a$ và $b$. Lấy điểm $M$ nằm ngoài cả hai đường thẳng. Qua $M$ vẽ được tối đa bao nhiêu đường thẳng song song với $a$?", "options": ["Chỉ đúng $1$", "$2$", "Vô số", "$0$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Nếu hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì chúng:", "options": ["Song song với nhau", "Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho $\\widehat{xOy} = 80^\\circ$. Lấy điểm $A$ trên $Ox$, vẽ tia $Az$ sao cho $\\widehat{OAz} = 100^\\circ$ (tia $Az$ và $Oy$ cùng nằm trên một nửa mặt phẳng bờ $Ox$). Khi đó:", "options": ["$Az \\parallel Oy$", "$Az$ cắt $Oy$", "$Az \\perp Oy$", "$Az \\parallel Ox$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho $a \\parallel b$ và $b \\parallel c$. Khẳng định nào sau đây là SAI?", "options": ["$a$ cắt $c$", "$a \\parallel c$", "Nếu $d \\perp a$ thì $d \\perp c$", "Đường thẳng cắt $a$ thì cũng cắt $c$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho góc $\\widehat{xOy} = 60^\\circ$. Trên tia $Ox$ lấy điểm $A$. Kẻ $Az \\parallel Oy$ (hướng vào trong). Kẻ tia phân giác $Ot$ của $\\widehat{xOy}$ và phân giác $Am$ của $\\widehat{xAz}$. Hai tia phân giác này:", "options": ["Song song với nhau", "Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hai đường thẳng $a$ và $b$ song song. Đường thẳng $c$ cắt $a$ tại $A$ và $b$ tại $B$. Hai tia phân giác của hai góc so le trong:", "options": ["Song song với nhau", "Vuông góc với nhau", "Trùng nhau", "Cắt nhau tạo góc $60^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hình vẽ: biết $AB \\parallel CD$. Góc $\\widehat{A} = 130^\\circ, \\widehat{C} = 140^\\circ$. Góc nhọn $\\widehat{AEC}$ ở giữa có số đo là:", "options": ["$90^\\circ$", "$80^\\circ$", "$100^\\circ$", "$70^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hai góc có cạnh tương ứng song song, một góc nhọn và một góc tù. Mối quan hệ giữa hai góc đó là:", "options": ["Bù nhau (tổng bằng $180^\\circ$)", "Bằng nhau", "Phụ nhau", "Không có mối liên hệ"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tam giác ABC có góc B = 70°, góc C = 50°. Vẽ tia Ax là tia đối của tia AB, vẽ tia Ay // BC:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Góc xAy và góc B là hai góc đồng vị, nên xAy = 70°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc yAC và góc C là hai góc so le trong, nên yAC = 50°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số đo góc BAC = 180° - (70° + 50°) = 60°.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Tia Ay là tia phân giác của góc xAC.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai đường thẳng song song a và b bị cắt bởi đường thẳng c tại A và B. Vẽ tia phân giác Ax của một góc so le trong và tia phân giác By của góc so le trong còn lại:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Hai góc so le trong ban đầu bằng nhau.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Một nửa của hai góc so le trong đó cũng bằng nhau.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Hai tia phân giác Ax và By tạo thành một cặp góc so le trong bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Tia Ax vuông góc với tia By.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho a // b. Hai góc trong cùng phía có hiệu số đo bằng 30°. Số đo của góc lớn hơn bằng bao nhiêu độ?", "answer": "105"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho Ax // By. Điểm O nằm giữa hai đường thẳng sao cho góc xAO = 35° và góc AOB = 80°. Số đo góc OBy bằng bao nhiêu độ?", "answer": "45"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho hai góc xOy và x'O'y' có Ox // O'x' và Oy // O'y'. Biết góc xOy = 65° và x'O'y' là góc tù. Số đo góc x'O'y' bằng bao nhiêu độ?", "answer": "115"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hai đường thẳng song song a và b. Hai tia phân giác của hai góc trong cùng phía cắt nhau tạo thành một góc bằng bao nhiêu độ?", "answer": "90"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hình vẽ: biết đường thẳng a song song với đường thẳng b. Đường thẳng c cắt a tại A và b tại B. Cho biết góc A1 = 2 . B1 (trong đó A1 và B1 là hai góc trong cùng phía).\na) Tính số đo góc A1 và góc B1.\nb) Tính số đo các góc còn lại tại đỉnh A và đỉnh B.",
            "rubric": "a) Vì a // b nên A1 + B1 = 180°. Mà A1 = 2 . B1 => 3 . B1 = 180° => B1 = 60° và A1 = 120° (0.5đ).\nb) Tại mỗi đỉnh, các góc đối đỉnh và kề bù được tính nhanh: 4 góc gồm hai góc 60° và hai góc 120° (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho góc xOy = 110°. Lấy điểm A trên tia Ox (A khác O). Kẻ tia Az // Oy (tia Az nằm trong góc xOy). Gọi Ot là tia phân giác của góc xOy, Am là tia phân giác của góc xAz.\na) Tính số đo góc xAz.\nb) Chứng minh tia Ot song song với tia Am.",
            "rubric": "a) Vì Az // Oy nên góc xAz và góc xOy là hai góc đồng vị => xAz = xOy = 110° (0.5đ).\nb) Ot là phân giác xOy => xOt = 110° : 2 = 55°. Am là phân giác xAz => xAm = 110° : 2 = 55°. Vì xOt = xAm = 55° mà hai góc này ở vị trí đồng vị nên Ot // Am (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho hình vẽ: biết Ax // Cy. Cho góc xAB = 30° và góc BCy = 140° (với tia Cy hướng ngược lại so với tia Ax). Điểm B nằm giữa hai đường thẳng.\na) Kẻ đường thẳng qua B song song với Ax.\nb) Tính số đo của góc ABC.",
            "rubric": "a) Kẻ tia Bz // Ax (cùng phía với tia Ax). Vì Ax // Cy nên Bz // Cy (0.4đ).\nb) Vì Bz // Ax nên góc ABz = góc xAB = 30° (so le trong) (0.3đ). Vì Bz // Cy nên góc CBz + góc BCy = 180° (trong cùng phía) => CBz = 180° - 140° = 40°. Suy ra góc ABC = ABz + CBz = 30° + 40° = 70° (0.3đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART1["c3_7_bai2_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 9: Hai đường thẳng song song - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hình vẽ: $Ax \\parallel By$. Biết $\\widehat{A} = 120^\\circ, \\widehat{B} = 130^\\circ$. Điểm $C$ nằm giữa hai đường thẳng sao cho góc $\\widehat{ACB}$ quay về phía ngược lại. Số đo góc $\\widehat{ACB}$ là:", "options": ["$110^\\circ$", "$70^\\circ$", "$90^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Hai góc $\\widehat{xOy}$ và $\\widehat{x'O'y'}$ có $Ox \\parallel O'x'$ và $Oy \\parallel O'y'$. Nếu $\\widehat{xOy} = 50^\\circ$ thì $\\widehat{x'O'y'}$ bằng:", "options": ["$50^\\circ$ hoặc $130^\\circ$", "$50^\\circ$", "$130^\\circ$", "$40^\\circ$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho hai đường thẳng $a \\parallel b$. Lấy 5 điểm phân biệt trên $a$ và 6 điểm phân biệt trên $b$. Nối các cặp điểm để tạo thành các đoạn thẳng. Số đoạn thẳng nối 1 điểm trên $a$ với 1 điểm trên $b$ là:", "options": ["$30$", "$11$", "$55$", "$60$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$. Từ điểm $D$ trên cạnh $BC$ kẻ $DE \\parallel AB$ ($E \\in AC$) và $DF \\parallel AC$ ($F \\in AB$). Tứ giác $AEDF$ có các góc đối:", "options": ["Bằng nhau", "Bù nhau", "Phụ nhau", "Không bằng nhau"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Cho hình zíc-zắc: $AB \\parallel EF$. Góc $\\widehat{B} = 40^\\circ, \\widehat{C} = 70^\\circ, \\widehat{D} = 80^\\circ, \\widehat{E} = 50^\\circ$. Mối liên hệ tổng các góc quay sang trái và sang phải là:", "options": ["Tổng góc quay trái bằng tổng góc quay phải", "Góc trái lớn hơn góc phải", "Góc trái nhỏ hơn góc phải", "Không có quy luật"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho góc $\\widehat{xOy} = 90^\\circ$. Điểm $A$ nằm trong góc. Kẻ $AB \\perp Ox$ và $AC \\perp Oy$. Nhận xét nào sau đây đúng?", "options": ["$AB \\parallel Oy$ và $AC \\parallel Ox$", "$AB \\perp AC$", "Tứ giác $ABOC$ có 4 góc vuông", "Cả ba nhận xét đều đúng"], "correct": 3},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho $a \\parallel b$. Đường thẳng $c$ cắt $a, b$. Hai tia phân giác của hai góc đồng vị tương ứng:", "options": ["Song song với nhau", "Vuông góc với nhau", "Trùng nhau", "Cắt nhau"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho hình vẽ có $Ax \\parallel By$. Số đo góc $\\widehat{AOB}$ thỏa mãn công thức:", "options": ["$\\widehat{AOB} = 360^\\circ - (\\widehat{A} + \\widehat{B})$ khi góc quay ra ngoài", "$\\widehat{AOB} = \\widehat{A} + \\widehat{B}$", "$\\widehat{AOB} = |\\widehat{A} - \\widehat{B}|$", "Tùy thuộc vào hình vẽ cụ thể"], "correct": 3},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho ba đường thẳng phân biệt $a, b, c$. Biết $a \\parallel b$ và $b$ cắt $c$. Khi đó:", "options": ["$a$ cũng cắt $c$", "$a \\parallel c$", "$a \\perp c$", "$a$ trùng $c$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$. Kẻ tia phân giác $AD$ của góc $A$. Từ $D$ kẻ đường thẳng song song với $AB$ cắt $AC$ tại $E$. Tam giác $ADE$ là:", "options": ["Tam giác có hai góc ở đáy bằng nhau (tam giác cân)", "Tam giác đều", "Tam giác vuông", "Tam giác vuông cân"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hình bình hành $ABCD$. Góc $\\widehat{A} = 120^\\circ$. Số đo các góc $\\widehat{B}, \\widehat{C}, \\widehat{D}$ lần lượt là:", "options": ["$60^\\circ, 120^\\circ, 60^\\circ$", "$120^\\circ, 60^\\circ, 60^\\circ$", "$60^\\circ, 60^\\circ, 120^\\circ$", "$90^\\circ, 90^\\circ, 90^\\circ$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Trong mặt phẳng, cho 2024 đường thẳng phân biệt, trong đó có 24 đường thẳng đôi một song song với nhau, các đường thẳng còn lại cắt nhau từng đôi một. Số giao điểm tối đa tạo thành là:", "options": ["$\\frac{2024 \\cdot 2023}{2} - \\frac{24 \\cdot 23}{2}$", "$\\frac{2024 \\cdot 2023}{2}$", "$2024 \\cdot 24$", "$\\frac{2000 \\cdot 1999}{2}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tam giác ABC có góc A = 90°. Lấy điểm M trên cạnh BC. Từ M kẻ MD vuông góc với AB tại D, ME vuông góc với AC tại E:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "MD // AC vì cùng vuông góc với AB.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "ME // AB vì cùng vuông góc với AC.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tứ giác ADME có 3 góc vuông tại A, D, E.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Đoạn thẳng DE luôn bằng đoạn thẳng AM trong mọi trường hợp.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình vẽ có Ax // Cz. Biết góc xAB = 120°, góc BCz = 150° (các tia Ax, Cz cùng hướng sang phải, điểm B nằm ở giữa):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Kẻ tia By // Ax sang phải thì By cũng song song với Cz.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc ABy và góc xAB là hai góc trong cùng phía, nên góc ABy = 180° - 120° = 60°.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Góc CBy và góc BCz là hai góc trong cùng phía, nên góc CBy = 180° - 150° = 30°.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Số đo góc ABC = ABy + CBy = 90° (tức AB vuông góc với BC).", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hình vẽ: Ax // By. Góc xAB = 140°, góc AOB = 90°. Góc OBy có số đo bằng bao nhiêu độ?", "answer": "130"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho tam giác ABC. Qua A kẻ đường thẳng d // BC. Biết góc B = 65° và C = 55°. Góc dAC (kề bù với góc dAB) có số đo bằng bao nhiêu độ?", "answer": "125"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho hai góc xOy = 70° và x'O'y' có các cạnh tương ứng song song: Ox // O'x', Oy // O'y'. Biết góc x'O'y' là góc nhọn. Số đo góc x'O'y' bằng bao nhiêu độ?", "answer": "70"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho ba đường thẳng song song a, b, c cách đều nhau. Một đường thẳng cắt cả ba đường thẳng lần lượt tại A, B, C. Tỉ số độ dài AB / BC bằng bao nhiêu?", "answer": "1"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho hình vẽ: Biết Ax // By. Góc xAB = 130°, góc AOB = 70°.\na) Kẻ tia Oz song song với Ax (tia Oz nằm trong góc AOB).\nb) Chứng minh rằng Oz cũng song song với By và tính số đo góc OBy.",
            "rubric": "a) Vẽ tia Oz // Ax hướng sang phải (0.3đ).\nb) Vì Oz // Ax nên góc AOz + xAB = 180° (trong cùng phía) => AOz = 180° - 130° = 50° (0.3đ). zOB = AOB - AOz = 70° - 50° = 20°. Vì Ax // By và Oz // Ax => Oz // By => zOB + OBy = 180° (trong cùng phía) => OBy = 180° - 20° = 160° (0.4đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác ABC. Trên tia đối của tia AB lấy điểm D. Kẻ tia Dm song song với BC.\na) Chứng minh rằng tia phân giác của góc BAC và tia phân giác của góc BCD không thể song song với nhau.\nb) Giả sử tia phân giác của góc xAC (góc ngoài tại A) song song với BC. Chứng minh rằng góc B = góc C.",
            "rubric": "a) Lập luận dựa trên góc và vị trí cắt nhau của các tia phân giác (0.5đ).\nb) Gọi Ay là phân giác xAC => xAy = yAC = 1/2 xAC. Vì Ay // BC nên xAy = B (đồng vị) và yAC = C (so le trong). Từ đó suy ra B = C (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho hình vẽ: Ax // Cy. Chứng minh rằng:\nGóc ABC = góc xAB + góc yCB (với góc ABC quay về phía trong và hai góc xAB, yCB nhọn).",
            "rubric": "Qua B kẻ đường thẳng Bz song song với Ax (0.3đ). Vì Ax // Cy nên Bz // Cy (0.2đ). Ta có góc ABz = góc xAB (so le trong) và góc CBz = góc yCB (so le trong) (0.3đ). Vì tia Bz nằm giữa hai tia BA và BC nên góc ABC = ABz + CBz = góc xAB + góc yCB (đpcm) (0.2đ)."
        }
    ]
}
