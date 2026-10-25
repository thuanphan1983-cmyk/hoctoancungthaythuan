# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 7 - CHƯƠNG III: GÓC VÀ ĐƯỜNG THẲNG SONG SONG
PHẦN 2:
- BÀI 10: TIÊN ĐỀ EUCLID. TÍNH CHẤT CỦA HAI ĐƯỜNG THẲNG SONG SONG (c3_7_bai3)
- BÀI 11: ĐỊNH LÍ VÀ CHỨNG MINH ĐỊNH LÍ (c3_7_bai4)
- BÀI KIỂM TRA CUỐI CHƯƠNG III: GÓC VÀ ĐƯỜNG THẲNG SONG SONG (c3_7_bai5)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 10: TIÊN ĐỀ EUCLID. TÍNH CHẤT CỦA HAI ĐƯỜNG THẲNG SONG SONG (c3_7_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c3_7_bai3_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 10: Tiên đề Euclid và tính chất - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Nội dung tiên đề Euclid khẳng định: Qua một điểm ở ngoài một đường thẳng:", "options": ["Chỉ có một đường thẳng song song với đường thẳng đó", "Có ít nhất một đường thẳng song song với đường thẳng đó", "Có vô số đường thẳng song song với đường thẳng đó", "Có đúng hai đường thẳng song song với đường thẳng đó"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Nếu hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì chúng:", "options": ["Song song với nhau", "Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Nếu một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó:", "options": ["Vuông góc với đường thẳng kia", "Song song với đường thẳng kia", "Trùng với đường thẳng kia", "Không cắt đường thẳng kia"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng:", "options": ["Song song với nhau", "Vuông góc với nhau", "Cắt nhau", "Trùng nhau"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Cho $a \\parallel b$ và $c \\perp a$. Kết luận nào sau đây đúng?", "options": ["$c \\perp b$", "$c \\parallel b$", "$a \\perp b$", "$c$ trùng $b$"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Cho ba đường thẳng $a, b, c$. Biết $a \\parallel b$ và $b \\parallel c$. Kết luận nào sau đây đúng?", "options": ["$a \\parallel c$", "$a \\perp c$", "$a$ cắt $c$", "$a$ trùng $c$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $a \\parallel b$. Đường thẳng $c$ cắt $a$ tại $A$ và $b$ tại $B$. Biết $\\widehat{A_1} = 70^\\circ$ (so le trong với $\\widehat{B_1}$). Số đo $\\widehat{B_1}$ là:", "options": ["$70^\\circ$", "$110^\\circ$", "$20^\\circ$", "$180^\\circ$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho $a \\parallel b$. Hai góc trong cùng phía có số đo là $\\widehat{A}$ và $\\widehat{B}$. Biết $\\widehat{A} = 100^\\circ$, số đo $\\widehat{B}$ là:", "options": ["$80^\\circ$", "$100^\\circ$", "$90^\\circ$", "$180^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Qua điểm $M$ nằm ngoài đường thẳng $d$, một học sinh vẽ được hai đường thẳng $a$ và $b$ cùng đi qua $M$ và cùng song song với $d$. Khi đó:", "options": ["Hai đường thẳng $a$ và $b$ phải trùng nhau", "Học sinh vẽ đúng", "Hai đường thẳng $a$ và $b$ vuông góc", "Hai đường thẳng $a$ và $b$ cắt nhau"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cho tam giác $ABC$. Qua $A$ vẽ đường thẳng $d \\parallel BC$. Hỏi có bao nhiêu đường thẳng như vậy?", "options": ["$1$", "$2$", "$0$", "Vô số"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Nếu đường thẳng $c$ cắt hai đường thẳng song song $a$ và $b$ thì:", "options": ["Hai góc so le trong bằng nhau", "Hai góc trong cùng phía bằng nhau", "Hai góc đồng vị bù nhau", "Hai góc so le trong bù nhau"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Biết $x \\perp y$ và $y \\perp z$. Khi đó quan hệ giữa $x$ và $z$ là:", "options": ["$x \\parallel z$ (nếu $x, z$ phân biệt)", "$x \\perp z$", "$x$ cắt $z$", "$x$ trùng $y$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hình vẽ có a // b và đường thẳng c vuông góc với a tại A, cắt b tại B:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Đường thẳng c cũng vuông góc với đường thẳng b tại B.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số đo góc tạo bởi c và b bằng 90°.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tất cả 4 góc tại đỉnh B đều bằng 90°.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Đường thẳng a song song với đường thẳng c.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét tính đúng/sai của các khẳng định sau:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Qua một điểm O ở ngoài đường thẳng d chỉ có duy nhất một đường thẳng vuông góc với d.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Qua một điểm O ở ngoài đường thẳng d chỉ có duy nhất một đường thẳng song song với d.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Nếu hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì chúng trùng nhau.", "correct": False},
                {"key": "d", "level": "Thông hiểu", "text": "Hai đường thẳng song song thì không bao giờ cắt nhau.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho a // b và a ⊥ c. Số đo góc tạo bởi đường thẳng b và đường thẳng c bằng bao nhiêu độ?", "answer": "90"},
        {"id": 2, "level": "Thông hiểu", "question": "Cho a // b // c. Khoảng cách từ a đến b là 3 cm, khoảng cách từ b đến c là 5 cm (b nằm giữa a và c). Khoảng cách từ a đến c bằng bao nhiêu cm?", "answer": "8"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho hai đường thẳng song song a và b. Một góc đồng vị có số đo 115°. Góc trong cùng phía với nó có số đo bằng bao nhiêu độ?", "answer": "65"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Qua điểm A nằm ngoài đường thẳng xy, kẻ đường thẳng m // xy và đường thẳng n // xy. Góc tạo bởi đường thẳng m và n có số đo bằng bao nhiêu độ?", "answer": "0"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hình vẽ: biết a ⊥ d và b ⊥ d.\na) Chứng minh rằng a // b.\nb) Biết đường thẳng c cắt a tại M và b tại N sao cho góc M1 = 65° (so le trong). Tính số đo góc N1.",
            "rubric": "a) Vì a ⊥ d và b ⊥ d (hai đường thẳng cùng vuông góc với đường thẳng thứ ba) nên a // b (0.5đ).\nb) Vì a // b nên hai góc so le trong bằng nhau: N1 = M1 = 65° (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho tam giác ABC. Trên nửa mặt phẳng bờ AC không chứa B, kẻ tia Ax // BC. Trên nửa mặt phẳng bờ AB không chứa C, kẻ tia Ay // BC.\na) Chứng minh ba điểm x, A, y thẳng hàng.\nb) Tính tổng ba góc của tam giác ABC bằng cách sử dụng các góc so le trong và kề bù tại đỉnh A.",
            "rubric": "a) Theo tiên đề Euclid, qua điểm A chỉ có một đường thẳng duy nhất song song với BC. Do đó hai tia Ax và Ay phải là hai tia đối nhau, tức ba điểm x, A, y thẳng hàng (0.5đ).\nb) xAB = B (so le trong), yAC = C (so le trong). Vì x, A, y thẳng hàng nên xAB + BAC + yAC = 180° => A + B + C = 180° (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Một người thợ xây dùng dây dọi để kiểm tra độ thẳng đứng của hai bức tường song song với nhau. Dây dọi vuông góc với mặt sàn phẳng.\na) Nếu bức tường thứ nhất thẳng đứng (vuông góc mặt sàn) và bức tường thứ hai cũng thẳng đứng thì hai bức tường có song song với nhau không? Dựa vào kiến thức nào?\nb) Nếu khoảng cách giữa hai bức tường ở chân tường là 4 m thì khoảng cách giữa chúng ở độ cao 3 m là bao nhiêu mét?",
            "rubric": "a) Có song song với nhau, dựa vào tính chất: hai đường thẳng phân biệt cùng vuông góc với một mặt sàn phẳng (đường thẳng thứ ba) thì song song với nhau (0.5đ).\nb) Vì hai bức tường song song nên khoảng cách giữa chúng không đổi tại mọi vị trí, bằng đúng 4 m (0.5đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c3_7_bai3_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 10: Tiên đề Euclid và tính chất - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho $a \\parallel b$ và $b \\perp c$. Khẳng định nào sau đây chắc chắn đúng?", "options": ["$a \\perp c$", "$a \\parallel c$", "$a$ cắt $b$", "$b$ trùng $c$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho ba đường thẳng phân biệt $a, b, c$. Biết $a \\perp b$ và $a \\perp c$. Khi đó:", "options": ["$b \\parallel c$", "$b \\perp c$", "$b$ cắt $c$", "$b$ trùng $c$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho hình vẽ: biết $a \\parallel b$. Góc $\\widehat{A} = 50^\\circ$ và $\\widehat{B} = 70^\\circ$. Góc $\\widehat{AOB}$ nhọn ở giữa (với $Ox \\parallel a$) có số đo là:", "options": ["$120^\\circ$", "$20^\\circ$", "$60^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho tam giác $ABC$. Qua mỗi đỉnh của tam giác, vẽ đường thẳng song song với cạnh đối diện. Số tam giác nhỏ bằng tam giác $ABC$ được tạo thành bên trong hình lớn là:", "options": ["$4$", "$3$", "$2$", "$1$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Cho $\\widehat{xOy} = 70^\\circ$. Trên tia $Ox$ lấy điểm $A$. Kẻ tia $Az \\parallel Oy$. Kẻ tia phân giác $Om$ của $\\widehat{xOy}$ và $An$ của $\\widehat{xAz}$. Hai tia phân giác này:", "options": ["Song song với nhau", "Vuông góc với nhau", "Trùng nhau", "Cắt nhau tạo góc $35^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Cho bốn đường thẳng phân biệt $a, b, c, d$. Biết $a \\parallel b,\\ b \\parallel c$ và $c \\perp d$. Khẳng định nào sau đây SAI?", "options": ["$a \\parallel d$", "$a \\perp d$", "$b \\perp d$", "$a \\parallel c$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho hai đường thẳng $a \\parallel b$. Đường thẳng $c$ cắt $a$ và $b$. Hai tia phân giác của hai góc trong cùng phía:", "options": ["Vuông góc với nhau", "Song song với nhau", "Trùng nhau", "Tạo với nhau góc $60^\\circ$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho hình vẽ có $AB \\parallel CD$. Góc $\\widehat{BAE} = 130^\\circ, \\widehat{DCE} = 120^\\circ$. Số đo góc $\\widehat{AEC}$ là:", "options": ["$110^\\circ$", "$70^\\circ$", "$90^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho góc $\\widehat{xOy}$ nhọn. Lấy điểm $A$ trên $Ox$, điểm $B$ trên $Oy$. Vẽ $Am \\perp Ox, Bn \\perp Oy$. Nếu $Am$ cắt $Bn$ tại $I$ thì:", "options": ["$\\widehat{AIB} + \\widehat{xOy} = 180^\\circ$", "$\\widehat{AIB} = \\widehat{xOy}$", "$\\widehat{AIB} = 90^\\circ$", "$\\widehat{AIB} + \\widehat{xOy} = 90^\\circ$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hình vẽ: biết $Ax \\parallel By$. Góc $\\widehat{A} = 40^\\circ$, góc $\\widehat{B} = 50^\\circ$. Góc $\\widehat{AOB}$ là:", "options": ["Góc vuông ($90^\\circ$)", "Góc nhọn ($80^\\circ$)", "Góc tù ($100^\\circ$)", "Không xác định"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Nếu hai góc có cạnh tương ứng vuông góc cùng là góc nhọn thì chúng:", "options": ["Bằng nhau", "Bù nhau", "Phụ nhau", "Không bằng nhau"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho đường thẳng $d$ và 10 điểm phân biệt nằm ngoài $d$. Qua mỗi điểm vẽ một đường thẳng song song với $d$. Số đường thẳng song song phân biệt tối đa có thể vẽ được là:", "options": ["$10$", "$1$", "$9$", "Vô số"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tam giác ABC có góc A = 80°, B = 60°. Kẻ tia phân giác AD của góc A (D ∈ BC). Từ D kẻ đường thẳng song song với AB cắt AC tại E:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số đo góc C = 180° - 80° - 60° = 40°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc BAD = CAD = 40°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Góc ADE = góc BAD = 40° (hai góc so le trong).", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Góc DEC = 100°.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hai đường thẳng song song a và b. Một cát tuyến c cắt a tại A và cắt b tại B tạo ra cặp góc trong cùng phía A1 và B1:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "A1 + B1 = 180°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Vẽ tia phân giác Ap của A1 và Bq của B1 thì Ap cắt Bq tại I.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Góc IAB = 1/2 A1 và góc IBA = 1/2 B1.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Góc AIB = 90° (tức hai tia phân giác vuông góc với nhau).", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho a // b và c // b. Biết góc tạo bởi a và d bằng 50°. Góc tạo bởi c và d (ở vị trí đồng vị) bằng bao nhiêu độ?", "answer": "50"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho hình vẽ: Ax // By. Góc xAO = 130°, góc OBy = 120°. Số đo góc nhọn AOB bằng bao nhiêu độ?", "answer": "110"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho góc xOy = 120°. Lấy điểm A trên Ox, kẻ tia Az // Oy hướng vào trong. Tia phân giác của xOy và phân giác của xAz tạo với nhau một góc bằng bao nhiêu độ?", "answer": "0"},
        {"id": 4, "level": "Vận dụng cao", "question": "Hai đường thẳng song song bị cắt bởi một cát tuyến. Tổng số đo của hai góc so le trong bằng 160°. Số đo mỗi góc so le trong đó bằng bao nhiêu độ?", "answer": "80"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hình vẽ có Ax // By. Điểm C nằm giữa hai đường thẳng sao cho góc xAC = 35° và góc yBC = 45°.\na) Kẻ tia Cz // Ax (cùng hướng với Ax).\nb) Tính số đo góc ACB.",
            "rubric": "a) Vẽ tia Cz // Ax hướng sang phải. Vì Ax // By nên Cz // By (0.4đ).\nb) Vì Cz // Ax nên ACz = xAC = 35° (so le trong). Vì Cz // By nên BCz = yBC = 45° (so le trong). Do Cz nằm giữa CA và CB nên ACB = ACz + BCz = 35° + 45° = 80° (0.6đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho tam giác ABC có góc B = góc C. Tia phân giác của góc ngoài tại đỉnh A là tia Ax.\na) Chứng minh rằng góc ngoài tại đỉnh A bằng 2 lần góc B.\nb) Chứng minh rằng Ax // BC.",
            "rubric": "a) Góc ngoài yAC = B + C. Vì B = C nên yAC = 2B (0.5đ).\nb) Vì Ax là phân giác yAC nên yAx = 1/2 yAC = B. Mà hai góc yAx và B ở vị trí đồng vị nên Ax // BC (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho hình vẽ: AB // CD // EF. Biết góc A = 130°, góc E = 120°.\na) Tính số đo các góc ACE và ACD nếu C nằm giữa và tia CD chia góc ACE thành hai góc.\nb) Giả sử góc ACE = 110°, hãy kiểm tra xem tia CD có song song với AB và EF không?",
            "rubric": "a) Kẻ đường thẳng hoặc dùng tính chất trong cùng phía: ACD = 180° - 130° = 50°; ECD = 180° - 120° = 60° => ACE = 50° + 60° = 110° (0.5đ).\nb) Vì ACD = 50° (trong cùng phía bù với A = 130°) nên CD // AB. Tương tự ECD = 60° (bù với E = 120°) nên CD // EF. Theo tính chất bắc cầu, AB // CD // EF (0.5đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c3_7_bai3_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 10: Tiên đề Euclid và tính chất - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho góc $\\widehat{xOy} = \\alpha$. Lấy điểm $A$ trên $Ox$, điểm $B$ trên $Oy$. Vẽ $Az \\parallel Oy$ và $Bt \\parallel Ox$. Tứ giác $OAZB$ là:", "options": ["Hình bình hành", "Hình chữ nhật", "Hình thoi", "Hình thang cân"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho hình zíc-zắc có $n$ đỉnh nằm xen kẽ giữa hai đường thẳng song song $d_1$ và $d_2$. Tổng các góc quay sang trái luôn:", "options": ["Bằng tổng các góc quay sang phải", "Lớn hơn tổng các góc quay sang phải", "Nhỏ hơn tổng các góc quay sang phải", "Bằng $180^\\circ$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho hình vẽ: $Ax \\parallel By$. Biết $\\widehat{A} = 150^\\circ, \\widehat{B} = 140^\\circ$. Góc $\\widehat{AOB}$ ngoài (hướng ra ngoài) có số đo là:", "options": ["$70^\\circ$", "$110^\\circ$", "$90^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$. Kẻ phân giác $AD$ của góc $A$. Qua $D$ kẻ $DE \\parallel AB$ ($E \\in AC$). Qua $E$ kẻ $EF \\parallel BC$ ($F \\in AB$). Khẳng định nào sau đây SAI?", "options": ["$AE = BF$", "$AE = DE$", "$DE \\parallel AB$", "Tam giác $ADE$ có hai góc bằng nhau"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Cho $a \\parallel b$. Lấy điểm $M$ trên $a$, điểm $N$ trên $b$. Điểm $P$ thỏa mãn $\\widehat{PMa} = 30^\\circ$ và $\\widehat{PNb} = 40^\\circ$. Số đo góc $\\widehat{MPN}$ có thể là:", "options": ["$70^\\circ$ hoặc $10^\\circ$", "$70^\\circ$", "$10^\\circ$", "$110^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Trong một mặt phẳng, nếu có 100 đường thẳng đôi một cắt nhau và không có ba đường thẳng nào đồng quy, thì số giao điểm là:", "options": ["$4950$", "$5000$", "$9900$", "$100$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho hai góc nhọn có cạnh tương ứng song song. Hai tia phân giác của hai góc đó:", "options": ["Song song với nhau", "Vuông góc với nhau", "Trùng nhau", "Cắt nhau tạo góc $45^\\circ$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho hình bình hành $ABCD$. Tia phân giác góc $A$ và tia phân giác góc $B$ cắt nhau tại $I$. Số đo góc $\\widehat{AIB}$ là:", "options": ["$90^\\circ$", "$60^\\circ$", "$120^\\circ$", "$45^\\circ$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho hai đường thẳng $a \\parallel b$. Điểm $O$ nằm giữa hai đường thẳng. Kẻ $OM \\perp a$ và $ON \\perp b$. Ba điểm $M, O, N$:", "options": ["Thẳng hàng", "Tạo thành tam giác vuông", "Tạo thành tam giác đều", "Không thẳng hàng"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho 2024 đường thẳng phân biệt sao cho cứ hai đường thẳng bất kì thì song song hoặc vuông góc với nhau. Có tối đa bao nhiêu đường thẳng đôi một vuông góc với nhau?", "options": ["$2$", "$4$", "$2024$", "$1012$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$. Qua $B$ kẻ đường thẳng song song với $AC$, qua $C$ kẻ đường thẳng song song với $AB$, chúng cắt nhau tại $D$. Tứ giác $ABDC$ có:", "options": ["Các cạnh đối bằng nhau", "Bốn cạnh bằng nhau", "Bốn góc vuông", "Hai đường chéo vuông góc"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hình vẽ có $Ax \\parallel By$. Biết $\\widehat{xAO} = \\alpha, \\widehat{OBy} = \\beta$ và góc $\\widehat{AOB}$ tù. Hệ thức đúng là:", "options": ["$\\widehat{AOB} = \\alpha + \\beta$ (nếu vẽ tia Oz // Ax chia AOB)", "$\\widehat{AOB} = 180^\\circ - (\\alpha + \\beta)$", "$\\widehat{AOB} = 360^\\circ - (\\alpha + \\beta)$", "Tùy theo hướng các tia"], "correct": 3}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tam giác ABC. Trên cạnh AC lấy điểm D. Qua D kẻ DE // BC (E ∈ AB) và DF // AB (F ∈ BC):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Tứ giác AEDF là hình bình hành.", "correct": False},
                {"key": "b", "level": "Thông hiểu", "text": "Tứ giác BEDF có các cạnh đối song song từng đôi một: DE // BF và DF // BE.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Góc EDF = góc B.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Góc AED = góc C.", "correct": True}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình vẽ có 3 đường thẳng d1 // d2 // d3 cách đều nhau. Một đường thẳng cắt d1, d2, d3 tại A, B, C và một đường thẳng khác cắt tại D, E, F:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Đoạn thẳng AB = BC.", "correct": True},
                {"key": "b", "level": "Vận dụng thấp", "text": "Đoạn thẳng DE = EF.", "correct": True},
                {"key": "c", "level": "Vận dụng cao", "text": "Tỉ số AB / DE = BC / EF.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Đoạn thẳng AC luôn bằng đoạn thẳng DF.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hình vẽ: Ax // By. Góc xAB = 135°, góc yBO = 145°. Số đo góc nhọn AOB bằng bao nhiêu độ?", "answer": "80"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Trong mặt phẳng có 20 đường thẳng đôi một song song. Chúng chia mặt phẳng thành bao nhiêu phần?", "answer": "21"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho góc xOy = 80°. Lấy điểm A trên Ox, B trên Oy. Kẻ Az // Oy và Bt // Ox cắt nhau tại C. Số đo góc ACB bằng bao nhiêu độ?", "answer": "80"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hai góc có cạnh tương ứng vuông góc. Biết hiệu hai góc đó là 50° và một góc là góc tù. Số đo góc tù đó bằng bao nhiêu độ?", "answer": "115"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho hình vẽ: Ax // By. Điểm O nằm giữa hai đường thẳng. Kẻ Oz // Ax.\na) Chứng minh rằng góc AOB = góc xAO + góc yBO (với các tia Ax, By hướng ngược lại so với tia Oz chia góc).\nb) Áp dụng tính góc AOB biết xAO = 38° và yBO = 52°.",
            "rubric": "a) Oz // Ax => AOz = xAO (so le trong). Oz // By => BOz = yBO (so le trong). Suy ra AOB = AOz + BOz = xAO + yBO (0.5đ).\nb) AOB = 38° + 52° = 90° (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác ABC. Lấy điểm M là trung điểm của cạnh BC. Trên tia đối của tia MA lấy điểm D sao cho MD = MA.\na) Chứng minh rằng AB // CD.\nb) Chứng minh rằng AC // BD.",
            "rubric": "a) Xét tam giác MAB và MDC có: MA = MD (gt), AMB = DMC (đối đỉnh), MB = MC (gt) => tam giác MAB = MDC (c.g.c) => MAB = MDC (so le trong) => AB // CD (0.5đ).\nb) Tương tự chứng minh tam giác MAC = MDB (c.g.c) => MCA = MBD (so le trong) => AC // BD (0.5đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho góc xOy = 120°. Trên Ox lấy điểm A, kẻ tia Az nằm trong góc xOy sao cho góc OAz = 60°.\na) Chứng minh Az // Oy.\nb) Kẻ tia phân giác Ot của góc xOy và tia phân giác An của góc xAz. Chứng minh Ot // An.\nc) Kẻ tia phân giác Am của góc OAz. Chứng minh Am ⊥ Ot.",
            "rubric": "a) OAz + xOy = 60° + 120° = 180° (hai góc trong cùng phía bù nhau) => Az // Oy (0.3đ).\nb) xOt = 60°; xAz = 180° - 60° = 120° (kề bù) => xAn = 60°. Vì xOt = xAn = 60° ở vị trí đồng vị nên Ot // An (0.4đ).\nc) Am là phân giác OAz, An là phân giác xAz kề bù nên Am ⊥ An. Vì Ot // An nên Am ⊥ Ot (0.3đ)."
        }
    ]
}


# ==============================================================================
# BÀI 11: ĐỊNH LÍ VÀ CHỨNG MINH ĐỊNH LÍ (c3_7_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c3_7_bai4_test1"] = {
    "title": "Toán 7 (KNTT) - Bài 11: Định lí và chứng minh định lí - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Một định lí là:", "options": ["Một khẳng định được suy ra từ những khẳng định được coi là đúng", "Một khẳng định được suy đoán bằng trực giác", "Một câu hỏi chưa có lời giải", "Một hình vẽ hình học"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Mỗi định lí thường được phát biểu dưới dạng:", "options": ["Nếu ... thì ...", "Vì ... nên ...", "Tuy ... nhưng ...", "Hoặc ... hoặc ..."], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Phần nằm giữa từ \"Nếu\" và từ \"thì\" là:", "options": ["Giả thiết của định lí", "Kết luận của định lí", "Chứng minh của định lí", "Hình vẽ minh họa"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Phần nằm sau từ \"thì\" là:", "options": ["Kết luận của định lí", "Giả thiết của định lí", "Lời giải định lí", "Định nghĩa"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Chứng minh định lí là:", "options": ["Dùng lập luận để từ giả thiết suy ra kết luận", "Đo đạc bằng thước", "Vẽ hình thật đẹp", "Dùng trực giác để khẳng định"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Giả thiết (GT) và kết luận (KL) của định lí thường được viết tắt là:", "options": ["GT và KL", "G và K", "TH và LUẬN", "ĐL và CM"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Trong định lí: \"Nếu hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì chúng song song với nhau\", giả thiết là:", "options": ["Hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba", "Chúng song song với nhau", "Hai đường thẳng cắt nhau", "Không có giả thiết"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Trong định lí: \"Hai góc đối đỉnh thì bằng nhau\", kết luận là:", "options": ["Hai góc đó bằng nhau", "Hai góc đó đối đỉnh", "Hai góc đó kề bù", "Hai góc đó phụ nhau"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Phát biểu lại định lí \"Hai góc đối đỉnh thì bằng nhau\" dưới dạng \"Nếu ... thì ...\":", "options": ["Nếu hai góc đối đỉnh thì hai góc đó bằng nhau", "Nếu hai góc bằng nhau thì hai góc đó đối đỉnh", "Nếu hai góc kề bù thì hai góc đó bằng nhau", "Nếu hai góc bằng nhau thì chúng đối đỉnh nhau"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Khẳng định nào sau đây KHÔNG PHẢI là một định lí?", "options": ["Hai góc bằng nhau thì đối đỉnh", "Hai góc đối đỉnh thì bằng nhau", "Nếu hai đường thẳng cùng vuông góc với đường thẳng thứ ba thì chúng song song", "Tổng ba góc trong một tam giác bằng $180^\\circ$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Để bác bỏ một khẳng định sai, ta chỉ cần:", "options": ["Chỉ ra một phản ví dụ", "Vẽ thật nhiều hình", "Hỏi nhiều người", "Không thể bác bỏ được"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Cho khẳng định: \"Nếu $a \\perp b$ và $b \\perp c$ thì $a \\parallel c$\". Giả thiết của khẳng định là:", "options": ["$a \\perp b$ và $b \\perp c$", "$a \\parallel c$", "$a$ cắt $c$", "$a, b, c$ phân biệt"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Xét định lí: \"Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc so le trong bằng nhau\":",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Giả thiết là: Một đường thẳng cắt hai đường thẳng song song.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Kết luận là: Hai góc so le trong bằng nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Định lí này đã được chứng minh và luôn đúng.", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Khẳng định đảo lại: \"Nếu hai góc so le trong bằng nhau thì hai đường thẳng song song\" là sai.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho khẳng định: \"Nếu hai góc có tổng bằng 180° thì hai góc đó là hai góc kề bù\":",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Giả thiết của khẳng định là hai góc có tổng số đo bằng 180°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Kết luận của khẳng định là hai góc đó kề bù.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Khẳng định trên là một định lí đúng.", "correct": False},
                {"key": "d", "level": "Vận dụng thấp", "text": "Phản ví dụ: hai góc của hai hình khác nhau mỗi góc bằng 90° có tổng bằng 180° nhưng không kề nhau.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Định lí có mấy phần cấu thành cơ bản? (Trả lời bằng số)", "answer": "2"},
        {"id": 2, "level": "Thông hiểu", "question": "Trong định lí: \"Nếu hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau\", phần kết luận gồm mấy mệnh đề?", "answer": "1"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm từ còn thiếu vào chỗ trống: \"Để chứng minh một khẳng định là đúng, ta phải dùng ... logic từ giả thiết suy ra kết luận.\" (Trả lời: lập luận)", "answer": "lập luận"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho khẳng định: \"Tất cả các số nguyên tố đều là số lẻ\". Số nào sau đây là phản ví dụ bác bỏ khẳng định đó? (Trả lời bằng số)", "answer": "2"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho định lí: \"Hai tia phân giác của hai góc kề bù thì vuông góc với nhau\".\na) Hãy vẽ hình minh họa cho định lí.\nb) Ghi giả thiết và kết luận của định lí bằng kí hiệu hình học.",
            "rubric": "a) Vẽ góc kề bù xOy và yOz, vẽ tia phân giác Om của xOy, On của yOz (0.5đ).\nb) GT: xOy và yOz kề bù; Om là phân giác xOy; On là phân giác yOz. KL: Om ⊥ On (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Chứng minh định lí: \"Hai góc đối đỉnh thì bằng nhau\".\n(Cho hai đường thẳng xx' và yy' cắt nhau tại O. Chứng minh góc xOy = góc x'Oy').",
            "rubric": "Ta có: xOy + xOy' = 180° (vì hai góc kề bù) (0.3đ). x'Oy' + xOy' = 180° (vì hai góc kề bù) (0.3đ). Suy ra xOy = 180° - xOy' và x'Oy' = 180° - xOy'. Do đó xOy = x'Oy' (đpcm) (0.4đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Hãy phát biểu định lí được suy ra từ hình vẽ sau dưới dạng \"Nếu ... thì ...\":\nCho hình vẽ có a ⊥ c và b ⊥ c (a và b phân biệt), suy ra a // b.",
            "rubric": "Phát biểu: \"Nếu hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau\" (0.6đ). Nêu rõ giả thiết (a ⊥ c, b ⊥ c, a ≠ b) và kết luận (a // b) (0.4đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c3_7_bai4_test2"] = {
    "title": "Toán 7 (KNTT) - Bài 11: Định lí và chứng minh định lí - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho định lí: \"Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc đồng vị bằng nhau\". Giả thiết là:", "options": ["Một đường thẳng cắt hai đường thẳng song song", "Hai góc đồng vị bằng nhau", "Hai góc so le trong bằng nhau", "Hai đường thẳng vuông góc"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Khẳng định: \"Nếu hai góc bằng nhau thì hai góc đó đối đỉnh\" là:", "options": ["Khẳng định sai", "Khẳng định đúng", "Định lí hình học", "Tiên đề"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Để chứng minh một định lí hình học, ta thực hiện theo thứ tự:", "options": ["Vẽ hình -> Ghi GT, KL -> Dùng lập luận suy từ GT ra KL", "Ghi KL -> Vẽ hình -> Ghi GT", "Dùng lập luận -> Vẽ hình -> Ghi GT", "Đo góc -> Kết luận"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho định lí: \"Một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó cũng vuông góc với đường thẳng kia\". Viết dưới dạng kí hiệu:", "options": ["GT: $a \\parallel b, c \\perp a$. KL: $c \\perp b$", "GT: $a \\perp b, b \\perp c$. KL: $a \\parallel c$", "GT: $a \\parallel b, c \\parallel a$. KL: $c \\parallel b$", "GT: $c \\perp b$. KL: $a \\parallel b$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Khẳng định nào sau đây là định lí đúng?", "options": ["Hai tia phân giác của hai góc đối đỉnh là hai tia đối nhau", "Hai góc có số đo bằng $90^\\circ$ là hai góc kề bù", "Hai đường thẳng không cắt nhau thì trùng nhau", "Hai góc phụ nhau có tổng số đo bằng $180^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Cho mệnh đề: \"Nếu $x^2 = 25$ thì $x = 5$\". Phản ví dụ để bác bỏ mệnh đề này là:", "options": ["$x = -5$", "$x = 0$", "$x = 25$", "$x = 5$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Chứng minh định lí: \"Nếu hai góc cùng phụ với một góc thứ ba thì hai góc đó bằng nhau\". Lập luận nào đúng?", "options": ["$\\widehat{A} + \\widehat{C} = 90^\\circ, \\widehat{B} + \\widehat{C} = 90^\\circ \\Rightarrow \\widehat{A} = \\widehat{B}$", "$\\widehat{A} + \\widehat{B} = 90^\\circ$", "$\\widehat{A} + \\widehat{C} = 180^\\circ$", "Hai góc đối đỉnh"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho định lí: \"Tia phân giác của hai góc kề bù vuông góc với nhau\". Số đo góc tạo bởi hai tia phân giác đó là:", "options": ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$", "$60^\\circ$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho định lí: \"Nếu hai đường thẳng $a$ và $b$ cùng song song với đường thẳng $c$ thì $a \\parallel b$\". Khi chứng minh định lí này, người ta thường dùng phương pháp:", "options": ["Phương pháp phản chứng dựa vào tiên đề Euclid", "Đo trực tiếp", "Vẽ hình", "Không cần chứng minh"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Phát biểu nào sau đây diễn đạt đúng một định lí?", "options": ["Nếu một tam giác có hai góc bằng nhau thì tam giác đó có hai cạnh bằng nhau", "Nếu tam giác có một góc vuông thì hai góc kia bằng nhau", "Nếu một góc lớn hơn $90^\\circ$ thì nó là góc nhọn", "Nếu hai góc bằng nhau thì có số đo bằng $60^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Trong phép chứng minh phản chứng, ta bắt đầu bằng cách:", "options": ["Giả sử kết luận là sai", "Giả sử giả thiết là sai", "Không quan tâm giả thiết", "Chứng minh kết luận là đúng"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho khẳng định: \"Mọi số tự nhiên chia hết cho 2 và chia hết cho 3 thì chia hết cho 6\". Đây là:", "options": ["Một định lí đúng trong số học", "Khẳng định sai", "Một tiên đề chưa chứng minh", "Một dự đoán"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Xét định lí: \"Hai góc cùng bù với một góc thứ ba thì bằng nhau\":",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Giả thiết: góc A và góc B cùng bù với góc C (tức A + C = 180° và B + C = 180°).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Kết luận: góc A = góc B.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Từ giả thiết suy ra A = 180° - C và B = 180° - C, do đó A = B.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Định lí này chỉ đúng khi góc C là góc nhọn.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho bài toán chứng minh: \"Tia phân giác của hai góc đối đỉnh là hai tia đối nhau\":",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Cho hai đường thẳng xx' và yy' cắt nhau tại O. Tia Oz là phân giác xOy, tia Oz' là phân giác x'Oy'.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "xOz = (1/2) xOy và x'Oz' = (1/2) x'Oy'.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Vì xOy = x'Oy' (đối đỉnh) nên xOz = x'Oz'.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Góc zOz' = 90°.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho định lí: \"Nếu hai góc kề nhau có hai tia ngoài cùng là hai tia đối nhau thì hai góc đó kề bù\". Tổng số đo của hai góc đó bằng bao nhiêu độ?", "answer": "180"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho định lí: \"Tổng các góc của một tứ giác bằng 360°\". Một tứ giác có 3 góc vuông thì góc thứ tư bằng bao nhiêu độ?", "answer": "90"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Tìm số tự nhiên n thỏa mãn khẳng định: \"Số tự nhiên chẵn duy nhất là số nguyên tố là n\". Giá trị của n là:", "answer": "2"},
        {"id": 4, "level": "Vận dụng cao", "question": "Có bao nhiêu định lí trong số các khẳng định sau: (1) Hai góc đối đỉnh thì bằng nhau; (2) Hai góc bằng nhau thì đối đỉnh; (3) Đường thẳng đi qua trung điểm và vuông góc với đoạn thẳng là đường trung trực; (4) Tam giác đều có 3 góc bằng 60°?", "answer": "3"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho định lí: \"Nếu một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó cũng vuông góc với đường thẳng kia\".\na) Vẽ hình minh họa định lí.\nb) Viết giả thiết và kết luận của định lí bằng kí hiệu.",
            "rubric": "a) Vẽ hai đường thẳng song song a // b, đường thẳng c ⊥ a tại A, c cắt b tại B (0.5đ).\nb) GT: a // b, c ⊥ a. KL: c ⊥ b (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Chứng minh định lí ở bài trên: Cho a // b và c ⊥ a tại A. Chứng minh c ⊥ b tại B.",
            "rubric": "Vì c ⊥ a tại A nên góc tạo bởi c và a là góc A1 = 90° (0.3đ). Vì a // b nên góc đồng vị B1 tạo bởi c và b bằng góc A1: B1 = A1 = 90° (0.4đ). Vì B1 = 90° nên c ⊥ b tại B (đpcm) (0.3đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Chứng minh định lí: \"Hai tia phân giác của hai góc kề bù thì vuông góc với nhau\".",
            "rubric": "Gọi hai góc kề bù là xOy và yOz => xOy + yOz = 180° (0.2đ). Gọi Om là phân giác xOy => mOy = 1/2 xOy. Gọi On là phân giác yOz => yOn = 1/2 yOz (0.3đ). Vì Oy nằm giữa Om và On nên mOn = mOy + yOn = 1/2 xOy + 1/2 yOz = 1/2 (xOy + yOz) = 1/2 x 180° = 90° (0.3đ). Vì mOn = 90° nên Om ⊥ On (đpcm) (0.2đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c3_7_bai4_test3"] = {
    "title": "Toán 7 (KNTT) - Bài 11: Định lí và chứng minh định lí - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Để chứng minh định lí: \"Nếu hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì chúng song song với nhau\", ta dùng phương pháp phản chứng. Bước đầu tiên giả sử:", "options": ["Hai đường thẳng đó không song song (tức là chúng cắt nhau)", "Hai đường thẳng đó song song", "Hai đường thẳng đó trùng nhau", "Đường thẳng thứ ba không tồn tại"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Một định lí đảo của một định lí đúng:", "options": ["Có thể đúng hoặc sai, cần phải chứng minh", "Luôn luôn đúng", "Luôn luôn sai", "Chính là tiên đề"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Xét định lí: \"Nếu một tam giác có ba cạnh bằng nhau thì tam giác đó có ba góc bằng nhau\". Định lí đảo của nó là:", "options": ["Nếu một tam giác có ba góc bằng nhau thì tam giác đó có ba cạnh bằng nhau", "Nếu một tam giác không có ba cạnh bằng nhau thì ba góc không bằng nhau", "Nếu một tam giác có ba cạnh bằng nhau thì đó là tam giác đều", "Không có định lí đảo"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Trong các khẳng định sau, khẳng định nào KHÔNG THỂ chứng minh bằng lập luận hình học Euclid?", "options": ["Tiên đề Euclid", "Định lí về hai góc đối đỉnh", "Định lí về tổng ba góc trong tam giác", "Tính chất hai đường thẳng cùng vuông góc với đường thẳng thứ ba"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Cho định lí: \"Nếu hai góc nhọn $\\widehat{xOy}$ và $\\widehat{x'O'y'}$ có các cạnh tương ứng song song thì chúng bằng nhau\". Giả thiết cần thêm là:", "options": ["Các tia $Ox, O'x'$ cùng hướng và $Oy, O'y'$ cùng hướng (hoặc cùng ngược hướng)", "Không cần điều kiện gì thêm", "Hai góc phải kề nhau", "Hai góc phải kề bù"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Mệnh đề: \"Tích của hai số vô tỉ luôn là một số vô tỉ\" là sai vì có phản ví dụ:", "options": ["$\\sqrt{2} \\cdot \\sqrt{2} = 2$ là số hữu tỉ", "$\\sqrt{2} \\cdot \\sqrt{3} = \\sqrt{6}$", "$\\pi \\cdot 2 = 2\\pi$", "$0 \\cdot \\sqrt{5} = 0$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho định lí: \"Trong một tam giác, góc đối diện với cạnh lớn hơn là góc lớn hơn\". Giả thiết của định lí là:", "options": ["Tam giác $ABC$ có $AC > AB$", "Tam giác $ABC$ có $\\widehat{B} > \\widehat{C}$", "Tam giác $ABC$ vuông", "Tam giác $ABC$ đều"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Chứng minh rằng: \"Không tồn tại số tự nhiên $n$ sao cho $n^2 + 1$ tận cùng bằng 3\". Phương pháp chứng minh phù hợp nhất là:", "options": ["Xét chữ số tận cùng của số chính phương", "Đo đạc", "Thử với vài số cụ thể", "Dùng định lí Pythagore"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho định lí: \"Nếu một đường thẳng cắt hai cạnh của một tam giác và song song với cạnh còn lại thì nó tạo thành một tam giác mới có ba góc lần lượt bằng ba góc của tam giác ban đầu\". Kết luận gồm:", "options": ["Ba cặp góc tương ứng bằng nhau", "Ba cặp cạnh tương ứng bằng nhau", "Hai tam giác bằng nhau", "Diện tích hai tam giác bằng nhau"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho khẳng định: \"Nếu $a^2 = b^2$ thì $a = b$\". Khẳng định này sai vì:", "options": ["Có phản ví dụ $a = -2, b = 2$ thỏa mãn $(-2)^2 = 2^2$ nhưng $-2 \\neq 2$", "Đúng với mọi số thực", "Chỉ đúng với số tự nhiên", "Sai do định nghĩa"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Định lí Pythagore phát biểu về tam giác vuông: \"Trong một tam giác vuông, bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông\". Giả thiết là:", "options": ["Tam giác vuông", "Bình phương cạnh huyền", "Tam giác cân", "Tam giác đều"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Số lượng tiên đề trong bộ tiên đề Euclid chuẩn cho hình học phẳng là:", "options": ["$5$", "$3$", "$10$", "$1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Xét mệnh đề toán học P: \"Nếu n là số tự nhiên thì n² + n + 1 là số nguyên tố\":",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Với n = 1: 1² + 1 + 1 = 3 là số nguyên tố.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Với n = 2: 2² + 2 + 1 = 7 là số nguyên tố.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Với n = 4: 4² + 4 + 1 = 21 là hợp số (chia hết cho 3 và 7).", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Mệnh đề P là một định lí đúng.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Xét quá trình chứng minh phản chứng định lí: \"Nếu hai đường thẳng a và b cùng song song với c thì a song song với b\":",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Giả sử phản chứng: a không song song với b, tức a cắt b tại điểm M.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi đó qua điểm M có hai đường thẳng a và b cùng song song với đường thẳng c.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Điều này mâu thuẫn trực tiếp với Tiên đề Euclid.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Vậy điều giả sử là đúng, a cắt b tại M.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một học sinh đưa ra phát biểu: \"Mọi hình chữ nhật đều có hai đường chéo bằng nhau\". Kết luận của định lí này là gì? (Trả lời: hai đường chéo bằng nhau)", "answer": "hai đường chéo bằng nhau"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho khẳng định: \"Mọi số chia hết cho 5 đều có tận cùng bằng 5\". Số tự nhiên nhỏ nhất khác 0 là phản ví dụ cho khẳng định này là:", "answer": "10"},
        {"id": 3, "level": "Vận dụng cao", "question": "Số khẳng định đúng trong các câu sau: (1) Hai góc đối đỉnh thì bằng nhau; (2) Hai góc kề bù có tổng bằng 180°; (3) Hai góc bằng nhau thì so le trong; (4) Đường thẳng vuông góc với một trong hai đường thẳng song song thì vuông góc với đường thẳng kia.", "answer": "3"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho định lí: \"Trong tam giác vuông, hai góc nhọn phụ nhau\". Nếu một góc nhọn bằng 35° thì góc nhọn còn lại bằng bao nhiêu độ?", "answer": "55"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Chứng minh định lí: \"Hai tia phân giác của hai góc đối đỉnh là hai tia đối nhau\".",
            "rubric": "Vẽ hai đường thẳng AB và CD cắt nhau tại O. Kẻ tia phân giác OM của AOC và tia phân giác ON của BOD (0.2đ). Ta có AOC = BOD (đối đỉnh) => AOM = MOC = BON = NOD = 1/2 AOC (0.3đ). Vì C, O, D thẳng hàng nên MOC + MOB = 180° => BON + MOB = 180° hay MON = 180° (0.3đ). Vậy OM và ON là hai tia đối nhau (đpcm) (0.2đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Dùng phương pháp phản chứng để chứng minh định lí sau:\n\"Nếu hai đường thẳng phân biệt a và b cùng song song với đường thẳng c thì a song song với b\".",
            "rubric": "Giả sử a không song song với b. Vì a và b phân biệt nên a phải cắt b tại một điểm M (0.3đ). Khi đó qua điểm M có hai đường thẳng phân biệt a và b cùng song song với đường thẳng c (0.3đ). Điều này mâu thuẫn với tiên đề Euclid (qua một điểm ở ngoài một đường thẳng chỉ có duy nhất một đường thẳng song song với đường thẳng đó) (0.3đ). Vậy điều giả sử là sai => a // b (đpcm) (0.1đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Chứng minh định lí: \"Nếu một đường thẳng cắt hai đường thẳng song song thì hai tia phân giác của hai góc so le trong song song với nhau\".",
            "rubric": "Cho a // b, đường thẳng c cắt a tại A và b tại B tạo ra cặp góc so le trong A1 = B1 (0.2đ). Gọi Ax là phân giác của A1 và By là phân giác của B1 (0.2đ). Ta có xAB = 1/2 A1 và yBA = 1/2 B1. Vì A1 = B1 nên xAB = yBA (0.3đ). Mà hai góc xAB và yBA ở vị trí so le trong của hai tia Ax và By bị cắt bởi cát tuyến AB, suy ra Ax // By (đpcm) (0.3đ)."
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG III: GÓC VÀ ĐƯỜNG THẲNG SONG SONG (c3_7_bai5)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c3_7_bai5_test1"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương III: Góc và song song - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hai góc đối đỉnh thì:", "options": ["Bằng nhau", "Kề bù", "Phụ nhau", "Có tổng bằng $90^\\circ$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hai góc kề bù có tổng số đo bằng:", "options": ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Tia phân giác của một góc chia góc đó thành:", "options": ["Hai góc bằng nhau", "Hai góc kề bù", "Hai góc phụ nhau", "Hai góc nhọn bất kì"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Nếu đường thẳng $c$ cắt hai đường thẳng $a$ và $b$ tạo thành một cặp góc so le trong bằng nhau thì:", "options": ["$a \\parallel b$", "$a \\perp b$", "$a$ cắt $b$", "$a$ trùng $b$"], "correct": 0},
        {"id": 5, "level": "Nhận biết", "question": "Hai đường thẳng phân biệt cùng vuông góc với đường thẳng thứ ba thì:", "options": ["Song song với nhau", "Vuông góc với nhau", "Cắt nhau", "Trùng nhau"], "correct": 0},
        {"id": 6, "level": "Nhận biết", "question": "Tiên đề Euclid khẳng định qua một điểm ở ngoài đường thẳng có bao nhiêu đường thẳng song song với đường thẳng đó?", "options": ["Chỉ có 1 đường thẳng duy nhất", "Có 2 đường thẳng", "Có vô số đường thẳng", "Không có đường thẳng nào"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Cho $\\widehat{xOy} = 70^\\circ$. Góc đối đỉnh với $\\widehat{xOy}$ có số đo là:", "options": ["$70^\\circ$", "$110^\\circ$", "$20^\\circ$", "$180^\\circ$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Cho hai góc kề bù $\\widehat{A}$ và $\\widehat{B}$. Biết $\\widehat{A} = 50^\\circ$, số đo góc $\\widehat{B}$ là:", "options": ["$130^\\circ$", "$50^\\circ$", "$40^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Tia $Oz$ là phân giác của $\\widehat{xOy} = 80^\\circ$. Số đo góc $\\widehat{xOz}$ là:", "options": ["$40^\\circ$", "$80^\\circ$", "$160^\\circ$", "$20^\\circ$"], "correct": 0},
        {"id": 10, "level": "Thông hiểu", "question": "Cho $a \\parallel b$. Một góc đồng vị có số đo bằng $65^\\circ$. Góc đồng vị kia có số đo là:", "options": ["$65^\\circ$", "$115^\\circ$", "$25^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 11, "level": "Thông hiểu", "question": "Hai đường thẳng $a$ và $b$ song song với nhau. Một góc trong cùng phía bằng $120^\\circ$. Góc trong cùng phía còn lại bằng:", "options": ["$60^\\circ$", "$120^\\circ$", "$90^\\circ$", "$180^\\circ$"], "correct": 0},
        {"id": 12, "level": "Thông hiểu", "question": "Cho $a \\perp c$ và $b \\parallel a$. Mối quan hệ giữa $b$ và $c$ là:", "options": ["$b \\perp c$", "$b \\parallel c$", "$b$ trùng $c$", "$b$ cắt $c$ nhưng không vuông góc"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hình vẽ hai đường thẳng a và b song song bị cắt bởi cát tuyến c tại A và B:",
            "statements": [
                {"key": "a", "level": "Nhận biết", "text": "Các cặp góc so le trong bằng nhau.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Các cặp góc đồng vị bằng nhau.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Các cặp góc trong cùng phía bù nhau (có tổng bằng 180°).", "correct": True},
                {"key": "d", "level": "Thông hiểu", "text": "Hai góc so le trong luôn phụ nhau (tổng bằng 90°).", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho góc xOy = 120°. Vẽ tia Oz là tia đối của Ox, tia Ot là phân giác của góc yOz:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Góc yOz kề bù với góc xOy, nên yOz = 60°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Ot là phân giác yOz nên zOt = yOt = 30°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số đo góc xOt = 150°.", "correct": True},
                {"key": "d", "level": "Vận dụng thấp", "text": "Tia Oy vuông góc với tia Ot.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Hai đường thẳng cắt nhau tạo thành 4 góc. Biết một góc có số đo 45°. Góc đối đỉnh với góc đó có số đo bằng bao nhiêu độ?", "answer": "45"},
        {"id": 2, "level": "Thông hiểu", "question": "Cho góc xOy = 150°. Tia Oz là phân giác của góc xOy. Số đo góc xOz bằng bao nhiêu độ?", "answer": "75"},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho a // b. Hai góc trong cùng phía có số đo là 2x và 3x. Giá trị của x bằng bao nhiêu độ?", "answer": "36"},
        {"id": 4, "level": "Vận dụng thấp", "question": "Góc tạo bởi hai tia phân giác của hai góc kề bù bằng bao nhiêu độ?", "answer": "90"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hình vẽ: biết a // b. Đường thẳng c cắt a tại A và cắt b tại B. Cho biết góc A1 = 70° (góc so le trong với B1).\na) Tính số đo góc B1.\nb) Tính số đo góc B2 (góc kề bù với B1).",
            "rubric": "a) Vì a // b nên góc B1 = góc A1 = 70° (hai góc so le trong) (0.5đ).\nb) Vì B2 kề bù với B1 nên B2 = 180° - 70° = 110° (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho góc bẹt xOy. Vẽ tia Oz sao cho góc xOz = 80°.\na) Tính số đo góc yOz.\nb) Vẽ tia Om là phân giác của góc xOz, tia On là phân giác của góc yOz. Chứng minh rằng Om vuông góc với On.",
            "rubric": "a) yOz = 180° - 80° = 100° (vì kề bù với xOz) (0.4đ).\nb) mOz = 80° : 2 = 40°; zOn = 100° : 2 = 50°. mOn = mOz + zOn = 40° + 50° = 90° => Om ⊥ On (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng thấp",
            "question": "Cho hình vẽ: biết Ax // By. Góc xAO = 30° và góc OBy = 50° (điểm O nằm giữa hai đường thẳng).\na) Kẻ tia Oz song song với Ax.\nb) Tính số đo góc AOB.",
            "rubric": "a) Kẻ tia Oz // Ax hướng sang phải. Do Ax // By nên Oz // By (0.4đ).\nb) Oz // Ax => AOz = xAO = 30° (so le trong). Oz // By => BOz = OBy = 50° (so le trong). Suy ra góc AOB = AOz + BOz = 30° + 50° = 80° (0.6đ)."
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c3_7_bai5_test2"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương III: Góc và song song - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hai góc kề bù $\\widehat{xOy}$ và $\\widehat{yOz}$. Biết $\\widehat{xOy} = 3\\widehat{yOz}$. Số đo góc $\\widehat{xOy}$ là:", "options": ["$135^\\circ$", "$45^\\circ$", "$120^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho hình vẽ: biết $a \\perp c$ và $b \\perp c$. Khẳng định nào sau đây đúng?", "options": ["$a \\parallel b$", "$a \\perp b$", "$a$ cắt $b$", "$a$ trùng $b$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Cho $a \\parallel b$. Đường thẳng $c$ cắt $a$ và $b$. Biết hiệu hai góc trong cùng phía là $40^\\circ$. Số đo của góc bé là:", "options": ["$70^\\circ$", "$110^\\circ$", "$60^\\circ$", "$80^\\circ$"], "correct": 0},
        {"id": 4, "level": "Vận dụng thấp", "question": "Cho hình vẽ: $Ax \\parallel By$. Biết $\\widehat{xAC} = 120^\\circ, \\widehat{yBC} = 130^\\circ$. Góc $\\widehat{ACB}$ ở giữa (quay ra ngoài) có số đo là:", "options": ["$110^\\circ$", "$70^\\circ$", "$90^\\circ$", "$100^\\circ$"], "correct": 0},
        {"id": 5, "level": "Vận dụng thấp", "question": "Cho góc $\\widehat{xOy} = 100^\\circ$. Lấy điểm $A$ trên tia $Ox$. Kẻ $Az \\parallel Oy$ (hướng vào trong). Tia phân giác của $\\widehat{xAz}$ cắt $Oy$ tại $B$. Tam giác $OAB$ là:", "options": ["Tam giác có hai góc bằng nhau (tam giác cân)", "Tam giác đều", "Tam giác vuông", "Tam giác vuông cân"], "correct": 0},
        {"id": 6, "level": "Vận dụng thấp", "question": "Cho hai góc đối đỉnh $\\widehat{AOB}$ và $\\widehat{COD}$. Biết $\\widehat{AOB} + \\widehat{COD} = 160^\\circ$. Số đo của góc kề bù với $\\widehat{AOB}$ là:", "options": ["$100^\\circ$", "$80^\\circ$", "$160^\\circ$", "$20^\\circ$"], "correct": 0},
        {"id": 7, "level": "Vận dụng thấp", "question": "Cho tam giác $ABC$. Kẻ tia phân giác $Ax$ của góc ngoài tại đỉnh $A$. Nếu $Ax \\parallel BC$ thì tam giác $ABC$ có:", "options": ["$\\widehat{B} = \\widehat{C}$", "$\\widehat{A} = 90^\\circ$", "$\\widehat{B} = 60^\\circ$", "$AB = BC = CA$"], "correct": 0},
        {"id": 8, "level": "Vận dụng thấp", "question": "Cho ba đường thẳng phân biệt $a, b, c$. Biết $a \\parallel b$ và $c$ cắt $a$. Khi đó $c$ và $b$:", "options": ["Cắt nhau", "Song song", "Trùng nhau", "Vuông góc"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho $\\widehat{xOy} = 60^\\circ$. Vẽ tia $Oz$ là tia đối của $Ox$. Vẽ tia $Ot$ vuông góc với $Oy$ ($Ot$ nằm trong $\\widehat{yOz}$). Số đo góc $\\widehat{zOt}$ là:", "options": ["$30^\\circ$", "$60^\\circ$", "$45^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Hai đường thẳng song song $a$ và $b$ bị cắt bởi cát tuyến $c$. Hai tia phân giác của hai góc so le trong:", "options": ["Song song với nhau", "Vuông góc với nhau", "Trùng nhau", "Cắt nhau tạo góc $45^\\circ$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Qua điểm $O$ vẽ 4 đường thẳng phân biệt. Số cặp góc đối đỉnh nhỏ hơn góc bẹt tạo thành là:", "options": ["$12$", "$8$", "$16$", "$6$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hình vẽ: biết $AB \\parallel CD$. Góc $\\widehat{A} = 40^\\circ$, góc $\\widehat{C} = 60^\\circ$. Góc $\\widehat{AEC}$ nhọn ở giữa bằng:", "options": ["$100^\\circ$", "$20^\\circ$", "$80^\\circ$", "$50^\\circ$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho hai góc kề nhau xOy và yOz có tổng số đo bằng 150°. Biết xOy = 4 . yOz:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Số đo góc yOz = 150° : 5 = 30°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số đo góc xOy = 120°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Tia phân giác của xOy và phân giác của yOz tạo thành góc 75°.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Góc xOz là góc bẹt.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho tam giác ABC có góc A = 90°. Kẻ AH vuông góc với BC tại H:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Góc B + góc C = 90° (hai góc phụ nhau).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc BAH + góc B = 90°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Góc BAH = góc C (vì cùng phụ với góc B).", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Góc CAH = góc C.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hai góc đối đỉnh có tổng số đo bằng 130°. Số đo mỗi góc đó bằng bao nhiêu độ?", "answer": "65"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho a // b. Cát tuyến c cắt a và b. Biết một góc đồng vị bằng 80°. Góc trong cùng phía với nó có số đo bằng bao nhiêu độ?", "answer": "100"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho góc xOy = 140°. Kẻ các tia Oz và Ot nằm trong góc xOy sao cho Oz ⊥ Ox và Ot ⊥ Oy. Số đo góc zOt bằng bao nhiêu độ?", "answer": "40"},
        {"id": 4, "level": "Vận dụng cao", "question": "Số cặp góc đối đỉnh khác góc bẹt tạo bởi 6 đường thẳng đồng quy là bao nhiêu?", "answer": "30"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hai đường thẳng AB và CD cắt nhau tại O. Biết góc AOC - góc AOD = 30°.\na) Tính số đo góc AOC và góc AOD.\nb) Tính số đo các góc BOD và BOC.",
            "rubric": "a) AOC + AOD = 180° (kề bù) và AOC - AOD = 30°. AOC = (180° + 30°) : 2 = 105°; AOD = 180° - 105° = 75° (0.5đ).\nb) BOD = AOC = 105° (đối đỉnh); BOC = AOD = 75° (đối đỉnh) (0.5đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng thấp",
            "question": "Cho tam giác ABC có góc B = 70°, C = 30°. Kẻ tia phân giác AD của góc A (D ∈ BC).\na) Tính số đo góc BAC.\nb) Kẻ tia Dx // AB (x ∈ AC). Tính số đo các góc của tam giác ADE.",
            "rubric": "a) BAC = 180° - (70° + 30°) = 80° (0.4đ).\nb) BAD = CAD = 40°. Vì Dx // AB nên ADE = BAD = 40° (so le trong). AED kề bù với góc trong cùng phía với A => AED = 180° - 80° = 100° (hoặc tính qua góc tam giác). DAE = 40°, ADE = 40°, AED = 100° (0.6đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho hình vẽ: Ax // By. Cho biết góc xAC = 130°, góc CBy = 150° (các tia Ax, By cùng hướng sang phải, điểm C nằm ở giữa).\na) Kẻ tia Cz // Ax hướng sang phải. Chứng minh Cz // By.\nb) Tính số đo góc ACB.",
            "rubric": "a) Kẻ Cz // Ax. Vì Ax // By nên Cz // By (0.4đ).\nb) Vì Cz // Ax nên ACz + xAC = 180° (trong cùng phía) => ACz = 180° - 130° = 50° (0.3đ). Vì Cz // By nên BCz + CBy = 180° (trong cùng phía) => BCz = 180° - 150° = 30°. Vậy góc ACB = ACz + BCz = 50° + 30° = 80° (0.3đ)."
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c3_7_bai5_test3"] = {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương III: Góc và song song - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho góc $\\widehat{xOy} = 120^\\circ$. Vẽ tia $Oz$ sao cho $Ox \\perp Oz$ và tia $Ot$ sao cho $Oy \\perp Ot$ (các tia $Oz, Ot$ nằm trong góc $\\widehat{xOy}$). Góc $\\widehat{zOt}$ có số đo là:", "options": ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$90^\\circ$"], "correct": 0},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho hai đường thẳng song song $a$ và $b$. Lấy 10 điểm trên $a$ và 10 điểm trên $b$. Nối tất cả các điểm trên $a$ với các điểm trên $b$. Giả sử không có ba đoạn thẳng nào đồng quy tại một điểm ở giữa hai đường thẳng. Số giao điểm của các đoạn thẳng nằm giữa $a$ và $b$ là:", "options": ["$2025$", "$45$", "$100$", "$900$"], "correct": 0},
        {"id": 3, "level": "Vận dụng thấp", "question": "Cho hình vẽ có $Ax \\parallel By$. Góc $\\widehat{A} = 30^\\circ, \\widehat{B} = 40^\\circ$. Điểm $C$ nằm giữa hai đường thẳng sao cho góc $\\widehat{ACB}$ quay về phía trong. Số đo góc $\\widehat{ACB}$ là:", "options": ["$70^\\circ$", "$10^\\circ$", "$110^\\circ$", "$150^\\circ$"], "correct": 0},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho tam giác $ABC$. Kẻ tia phân giác $BD$ của góc $B$ và $CE$ của góc $C$. Nếu $BD \\parallel CE$ thì:", "options": ["Điều này không thể xảy ra", "Tam giác $ABC$ đều", "Tam giác $ABC$ vuông", "$\\widehat{B} = \\widehat{C} = 90^\\circ$"], "correct": 0},
        {"id": 5, "level": "Vận dụng cao", "question": "Cho góc $\\widehat{xOy} = 75^\\circ$. Lấy điểm $A$ trên $Ox$, kẻ $Az \\parallel Oy$. Tia phân giác của $\\widehat{OAz}$ cắt $Oy$ tại $B$. Số đo góc $\\widehat{ABO}$ là:", "options": ["$\\frac{105^\\circ}{2} = 52,5^\\circ$", "$75^\\circ$", "$37,5^\\circ$", "$45^\\circ$"], "correct": 0},
        {"id": 6, "level": "Vận dụng cao", "question": "Cho $n$ đường thẳng đồng quy tại $O$. Nếu số cặp góc đối đỉnh (khác góc bẹt) tạo thành là 90 thì $n$ bằng:", "options": ["$10$", "$9$", "$11$", "$12$"], "correct": 0},
        {"id": 7, "level": "Vận dụng cao", "question": "Cho hình bình hành $ABCD$. Góc $\\widehat{A} = 110^\\circ$. Tia phân giác của góc $A$ cắt cạnh $CD$ tại $E$. Tam giác $ADE$ là:", "options": ["Tam giác có hai góc ở đáy bằng $55^\\circ$ (tam giác cân)", "Tam giác đều", "Tam giác vuông", "Tam giác tù"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho hình zíc-zắc 3 đoạn $AB \\parallel CD$. Góc $\\widehat{B} = 35^\\circ, \\widehat{D} = 45^\\circ, \\widehat{BCD} = 80^\\circ$. Nhận định nào sau đây đúng?", "options": ["Điểm $C$ là đỉnh của góc quay", "Hình vẽ thỏa mãn $AB \\parallel CD$", "Tổng góc trái bằng tổng góc phải", "Cả ba nhận định đều đúng"], "correct": 3},
        {"id": 9, "level": "Vận dụng cao", "question": "Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$. Kẻ $OD$ là phân giác của $\\widehat{AOB}$. Biết $\\widehat{COD} = 140^\\circ$. Số đo góc $\\widehat{AOB}$ là:", "options": ["$80^\\circ$", "$100^\\circ$", "$60^\\circ$", "$120^\\circ$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Hai đường thẳng song song $a$ và $b$ bị cắt bởi cát tuyến $c$. Khoảng cách giữa hai đường thẳng phân giác của hai góc đồng vị tương ứng:", "options": ["Không đổi", "Bằng 0", "Thay đổi tùy cát tuyến", "Bằng độ dài cát tuyến"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho 2024 đường thẳng phân biệt cùng đi qua điểm $O$. Số góc tạo thành khác góc bẹt và góc không là:", "options": ["$2024 \\cdot 4047$", "$2024 \\cdot 2023$", "$4048 \\cdot 4047$", "$2024^2$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho góc $\\widehat{xOy} = 90^\\circ$. Trong góc đó vẽ các tia $Oz, Ot$ sao cho $\\widehat{xOz} = \\widehat{yOt} = 30^\\circ$. Tia phân giác của góc $\\widehat{zOt}$ cũng là:", "options": ["Tia phân giác của $\\widehat{xOy}$", "Tia $Ox$", "Tia $Oy$", "Tia đối của $Oz$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "stem": "Cho tam giác ABC có góc A = 80°. Kẻ các đường phân giác BD và CE của tam giác cắt nhau tại I:",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "B + C = 180° - 80° = 100°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "IBC + ICB = (1/2)(B + C) = 50°.", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Số đo góc BIC = 180° - 50° = 130°.", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Góc BIC = 90° + A.", "correct": False}
            ]
        },
        {
            "id": 2,
            "stem": "Cho hình vẽ có Ax // By. Điểm C nằm giữa sao cho góc xAC = α, góc yBC = β (với Ax, By cùng hướng, góc ACB nhọn hướng vào trong):",
            "statements": [
                {"key": "a", "level": "Thông hiểu", "text": "Kẻ Cz // Ax thì Cz cũng song song với By.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc ACz = α (so le trong).", "correct": True},
                {"key": "c", "level": "Vận dụng thấp", "text": "Góc BCz = β (so le trong).", "correct": True},
                {"key": "d", "level": "Vận dụng cao", "text": "Số đo góc ACB = α + β.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho góc xOy = 110°. Vẽ tia Oz là phân giác của góc xOy, sau đó vẽ tia Ot là tia phân giác của góc xOz. Số đo góc yOt bằng bao nhiêu độ?", "answer": "82,5"},
        {"id": 2, "level": "Vận dụng thấp", "question": "Cho hai đường thẳng song song a và b. Một cát tuyến c cắt a và b tạo thành 8 góc. Biết tổng của 4 góc nhọn bằng 280°. Số đo của mỗi góc tù bằng bao nhiêu độ?", "answer": "110"},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho n đường thẳng phân biệt cùng đi qua điểm O tạo thành 110 cặp góc đối đỉnh (không kể góc bẹt). Giá trị của n bằng bao nhiêu?", "answer": "11"},
        {"id": 4, "level": "Vận dụng cao", "question": "Cho hình vẽ: Ax // By. Góc xAB = 140°, góc AOB = 80°. Số đo góc tù OBy bằng bao nhiêu độ?", "answer": "120"}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng thấp",
            "question": "Cho hình vẽ: Ax // Cy. Cho góc xAB = 120°, góc BCy = 130°. Điểm B nằm giữa hai đường thẳng Ax và Cy.\na) Kẻ tia Bz // Ax (hướng sang phải). Chứng minh Bz // Cy.\nb) Tính số đo góc ABC.",
            "rubric": "a) Vì Bz // Ax và Ax // Cy nên Bz // Cy (0.4đ).\nb) Vì Bz // Ax nên ABz + xAB = 180° (trong cùng phía) => ABz = 180° - 120° = 60° (0.3đ). Vì Bz // Cy nên CBz + BCy = 180° (trong cùng phía) => CBz = 180° - 130° = 50°. Suy ra ABC = ABz + CBz = 60° + 50° = 110° (0.3đ)."
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho tam giác ABC có góc B = 60°, C = 40°. Kẻ tia phân giác AD của góc A (D ∈ BC).\na) Tính số đo góc BAC và góc ADC.\nb) Từ D kẻ đường thẳng song song với AB cắt AC tại E. Chứng minh tam giác ADE có hai góc bằng nhau.",
            "rubric": "a) BAC = 180° - (60° + 40°) = 80° (0.2đ) => BAD = CAD = 40°. Trong tam giác ADC: ADC = 180° - (40° + 40°) = 100° (0.3đ).\nb) Vì DE // AB nên ADE = BAD = 40° (so le trong) (0.3đ). Mà EAD = CAD = 40° => EAD = ADE = 40°. Tam giác ADE có hai góc bằng nhau (0.2đ)."
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "question": "Cho góc nhọn xOy. Lấy điểm A trên Ox, điểm B trên Oy sao cho OA = OB. Qua A kẻ đường thẳng d1 vuông góc với Ox. Qua B kẻ đường thẳng d2 vuông góc với Oy. Gọi I là giao điểm của d1 và d2.\na) Chứng minh rằng góc AIB và góc xOy bù nhau.\nb) Chứng minh rằng tia OI là tia phân giác của góc xOy.",
            "rubric": "a) Tứ giác OAIB có OAI = 90° và OBI = 90°. Tổng 4 góc = 360° => AIB + xOy = 360° - 180° = 180° (bù nhau) (0.5đ).\nb) Xét hai tam giác vuông OAI và OBI có: cạnh huyền OI chung, OA = OB (gt) => tam giác OAI = OBI (cạnh huyền - cạnh góc vuông) => AOI = BOI => OI là tia phân giác của xOy (0.5đ)."
        }
    ]
}
