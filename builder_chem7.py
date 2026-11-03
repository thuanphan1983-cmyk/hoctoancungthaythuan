# -*- coding: utf-8 -*-
"""
BUILDER HÓA 7 - 28 ĐỀ THI ĐỘC LẬP 100%
Gồm 8 bài học:
- Bài 2: Nguyên tử (3 đề)
- Bài 3: Nguyên tố hóa học (3 đề)
- Bài 4: Bảng tuần hoàn (3 đề)
- Ôn tập Chương I (5 đề)
- Bài 5: Phân tử - Đơn chất - Hợp chất (3 đề)
- Bài 6: Liên kết hóa học (3 đề)
- Bài 7: Hóa trị và CTHH (3 đề)
- Ôn tập Chương II (5 đề)
"""

import sys
import json
sys.stdout.reconfigure(encoding='utf-8')

# Import Bài 2 đã có sẵn trong generate_chem7_distinct.py
from generate_chem7_distinct import build_chem7_exams as get_b2_exams

chem7_exams = get_b2_exams()

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": prompt.strip(),
        "statements": [
            {"subId": s[0], "text": s[1].strip(), "correct": s[2]} for s in statements
        ],
        "explanation": explanation.strip()
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "correctAnswer": str(answer).strip(),
        "explanation": explanation.strip()
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation.strip()
    }

# ==============================================================================
# BÀI 3: NGUYÊN TỐ HÓA HỌC (3 ĐỀ ĐỘC LẬP)
# ==============================================================================

# --- ĐỀ 1: Kí hiệu hóa học, tên IUPAC, định nghĩa nguyên tố (tập trung nhóm kim loại & phi kim phổ biến) ---
chem7_exams["chem7_c1_b3_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Nguyên tố hóa học là tập hợp những nguyên tử cùng loại có cùng:", ["Số neutron trong hạt nhân", "Số proton trong hạt nhân", "Khối lượng nguyên tử", "Số lớp electron"], 1, "Các nguyên tử có cùng số proton thuộc về cùng một nguyên tố hóa học."),
        make_mc(2, "Nhận biết", "Kí hiệu hóa học của nguyên tố Sodium (Natri) là:", ["Na", "So", "S", "Sd"], 0, "Sodium có kí hiệu hóa học là Na."),
        make_mc(3, "Nhận biết", "Tên gọi theo danh pháp quốc tế IUPAC của nguyên tố có kí hiệu hóa học là 'Fe' là:", ["Iron", "Ferum", "Copper", "Zinc"], 0, "Fe là Iron."),
        make_mc(4, "Nhận biết", "Kí hiệu hóa học của nguyên tố Oxygen là:", ["O", "Ox", "Og", "Oh"], 0, "Oxygen có kí hiệu là O."),
        make_mc(5, "Nhận biết", "Quy tắc viết kí hiệu hóa học gồm một chữ cái là:", ["Viết chữ thường", "Viết hoa", "Viết in nghiêng", "Viết kèm số 1"], 1, "Kí hiệu gồm 1 chữ cái luôn viết in hoa (ví dụ: H, C, O, N)."),
        make_mc(6, "Nhận biết", "Nguyên tố hóa học chiếm hàm lượng lớn nhất trong vỏ Trái Đất là:", ["Oxygen", "Silicon", "Aluminium", "Iron"], 0, "Oxygen chiếm khoảng 49,4% khối lượng vỏ Trái Đất."),
        make_mc(7, "Thông hiểu", "Nguyên tố nào sau đây là thành phần chính cấu tạo nên xương và răng của con người?", ["Calcium", "Iron", "Potassium", "Sodium"], 0, "Calcium chiếm tỉ lệ lớn trong mô xương và răng."),
        make_mc(8, "Thông hiểu", "Một nguyên tử có 8 proton và 8 neutron, một nguyên tử khác có 8 proton và 9 neutron. Hai nguyên tử này:", ["Thuộc cùng một nguyên tố hóa học", "Thuộc hai nguyên tố hóa học khác nhau", "Có cùng khối lượng", "Có tính chất hóa học hoàn toàn khác nhau"], 0, "Cùng số proton (8) nên thuộc cùng nguyên tố Oxygen."),
        make_mc(9, "Thông hiểu", "Kí hiệu hóa học nào sau đây viết SAI quy ước?", ["ca", "Al", "Cl", "Mg"], 0, "Calcium phải viết là Ca (chữ cái đầu viết hoa, chữ thứ hai viết thường)."),
        make_mc(10, "Thông hiểu", "Nguyên tố khí hiếm thường được dùng để bơm vào khinh khí cầu và bóng bay trang trí do nhẹ và không cháy là:", ["Helium", "Hydrogen", "Neon", "Argon"], 0, "Helium nhẹ và trơ, an toàn khi sử dụng."),
        make_mc(11, "Thông hiểu", "Tên gọi theo IUPAC của nguyên tố có kí hiệu Cu là:", ["Copper", "Calcium", "Carbon", "Chlorine"], 0, "Cu là Copper (Đồng)."),
        make_mc(12, "Thông hiểu", "Số hiệu nguyên tử của một nguyên tố cho ta biết thông tin nào sau đây?", ["Số proton trong hạt nhân", "Số neutron trong hạt nhân", "Khối lượng nguyên tử", "Số phân tử trong chất"], 0, "Số hiệu nguyên tử Z = số proton = số electron.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các phát biểu về nguyên tố hóa học:", [
            ("a", "Mỗi nguyên tố hóa học được biểu diễn bằng một hoặc hai chữ cái gọi là kí hiệu hóa học.", True),
            ("b", "Chữ cái đầu tiên trong kí hiệu hóa học luôn phải viết hoa.", True),
            ("c", "Nguyên tử của cùng một nguyên tố hóa học có thể có số neutron khác nhau.", True),
            ("d", "Số neutron là đặc trưng cơ bản nhất của một nguyên tố hóa học.", False)
        ], "Số proton mới là đại lượng đặc trưng cơ bản nhất của nguyên tố hóa học."),
        make_tf(2, "Thông hiểu", "Cho các nguyên tố: Hydrogen (H), Carbon (C), Nitrogen (N), Oxygen (O):", [
            ("a", "Đây là 4 nguyên tố chính cấu tạo nên cơ thể sinh vật.", True),
            ("b", "Khối lượng nguyên tử của Carbon là 12 amu.", True),
            ("c", "Kí hiệu của Nitrogen là Ni.", False),
            ("d", "Oxygen là nguyên tố phi kim.", True)
        ], "Nitrogen có kí hiệu là N, Ni là Nickel."),
        make_tf(3, "Vận dụng", "Xét các nguyên tố kim loại thông dụng trong đời sống:", [
            ("a", "Aluminium (Al) có khối lượng nguyên tử là 27 amu, được dùng làm dây dẫn điện trên cao.", True),
            ("b", "Iron (Fe) có khối lượng nguyên tử là 56 amu, là thành phần chính của thép.", True),
            ("c", "Gold (Au) và Silver (Ag) là các kim loại quý dùng làm trang sức.", True),
            ("d", "Copper (Cu) là kim loại có màu trắng bạc và dẫn điện kém.", False)
        ], "Copper có màu đỏ ánh kim và dẫn điện rất tốt."),
        make_tf(4, "Vận dụng", "Cho biết tổng số hạt trong nguyên tử của nguyên tố X là 36, trong đó số hạt mang điện gấp đôi số hạt không mang điện:", [
            ("a", "Nguyên tử X có 12 proton.", True),
            ("b", "Tên gọi theo IUPAC của nguyên tố X là Magnesium.", True),
            ("c", "Kí hiệu hóa học của nguyên tố X là Mn.", False),
            ("d", "Khối lượng nguyên tử của X xấp xỉ bằng 24 amu.", True)
        ], "X là Magnesium, kí hiệu là Mg (Mn là Manganese).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Kí hiệu hóa học của nguyên tố Potassium (Kali) gồm mấy chữ cái?", "1", "Potassium có kí hiệu là K (1 chữ cái)."),
        make_sa(2, "Thông hiểu", "Nguyên tố Carbon có số hiệu nguyên tử bằng bao nhiêu?", "6", "Carbon có Z = 6."),
        make_sa(3, "Vận dụng", "Trong vỏ Trái Đất, nguyên tố kim loại nào chiếm tỉ lệ phần trăm khối lượng lớn nhất? (Viết kí hiệu hóa học)", "Al", "Aluminium (Al) chiếm khoảng 7,5% khối lượng vỏ Trái Đất."),
        make_sa(4, "Vận dụng", "Một nguyên tử có 13 proton và 14 neutron. Khối lượng của nguyên tử đó tính theo đơn vị amu là bao nhiêu?", "27", "13 + 14 = 27 amu (Aluminium)."),
        make_sa(5, "Vận dụng cao", "Một nguyên tố X có nguyên tử khối gấp 2 lần nguyên tử khối của Oxygen. X là nguyên tố nào? (Ghi kí hiệu hóa học)", "S", "Khối lượng = 2 × 16 = 32 amu => Sulfur (S)."),
        make_sa(6, "Vận dụng cao", "Phân tử khí ozone gồm 3 nguyên tử oxygen liên kết với nhau. Khối lượng phân tử ozone theo đơn vị amu là bao nhiêu?", "48", "3 × 16 = 48 amu.")
    ],
    "part4": [
        make_vdc(1, "Nguyên tử của nguyên tố X nặng gấp 14 lần nguyên tử Hydrogen. Tên và kí hiệu hóa học của X là:", ["Nitrogen (N)", "Carbon (C)", "Oxygen (O)", "Silicon (Si)"], 0, "Khối lượng X = 14 × 1 = 14 amu => Nitrogen (N)."),
        make_vdc(2, "Một mẫu quặng chứa 80% khối lượng là Fe2O3. Biết khối lượng nguyên tử Fe = 56 amu, O = 16 amu. Tỉ lệ phần trăm khối lượng của nguyên tố Fe trong Fe2O3 tinh khiết là:", ["70%", "60%", "72,4%", "80%"], 0, "%Fe = (2 × 56) / (2 × 56 + 3 × 16) × 100% = 112 / 160 × 100% = 70%."),
        make_vdc(3, "Nguyên tử của nguyên tố A có tổng số hạt mang điện trong hạt nhân bằng số hạt mang điện ở vỏ của nguyên tử B. Biết A có Z = 15, B có số neutron nhiều hơn A là 1. Tổng số hạt trong B là 32. Khối lượng nguyên tử B theo amu là:", ["32 amu", "31 amu", "30 amu", "33 amu"], 0, "pB = pA = 15 => nB = 17 => tổng hạt 2*15 + 17 = 47. Với S (Z=16), P (Z=15). Nếu pB = 16, nB = 16 => B là Sulfur (32 amu)."),
        make_vdc(4, "Một hợp chất khí gồm nguyên tố X liên kết với Hydrogen có công thức XH3, trong đó Hydrogen chiếm 17,65% về khối lượng. Nguyên tố X là:", ["Nitrogen (N)", "Phosphorus (P)", "Carbon (C)", "Boron (B)"], 0, "3 / (X + 3) = 0,1765 => X + 3 = 17 => X = 14 (Nitrogen).")
    ]
}

# --- ĐỀ 2: Nguồn gốc tên gọi, nguyên tố trong cơ thể người & vỏ Trái Đất, nhận diện nguyên tố ---
chem7_exams["chem7_c1_b3_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Hiện nay các nhà khoa học đã tìm ra khoảng bao nhiêu nguyên tố hóa học?", ["Khoảng 90", "Khoảng 118", "Khoảng 200", "Khoảng 500"], 1, "Hiện nay có 118 nguyên tố hóa học đã được xác định."),
        make_mc(2, "Nhận biết", "Kí hiệu hóa học của nguyên tố Phosphorus (Photpho) là:", ["P", "Ph", "Po", "Ps"], 0, "Phosphorus có kí hiệu là P."),
        make_mc(3, "Nhận biết", "Tên gọi theo IUPAC của nguyên tố có kí hiệu 'Ag' là:", ["Silver", "Gold", "Aluminium", "Silicon"], 0, "Ag là Silver (Bạc)."),
        make_mc(4, "Nhận biết", "Nguyên tố nào sau đây là chất khí ở điều kiện thường và duy trì sự sống?", ["Oxygen", "Nitrogen", "Hydrogen", "Carbon"], 0, "Khí oxygen duy trì sự hô hấp của con người và sinh vật."),
        make_mc(5, "Nhận biết", "Kí hiệu hóa học của nguyên tố Chlorine là:", ["Cl", "C", "Ch", "Cr"], 0, "Chlorine có kí hiệu là Cl."),
        make_mc(6, "Nhận biết", "Nguyên tố phổ biến thứ hai trong vỏ Trái Đất (sau Oxygen) là:", ["Silicon", "Aluminium", "Iron", "Calcium"], 0, "Silicon chiếm khoảng 25,8% khối lượng vỏ Trái Đất."),
        make_mc(7, "Thông hiểu", "Nguyên tố nào sau đây là thành phần cấu tạo hồng cầu trong máu giúp vận chuyển oxygen?", ["Iron (Sắt)", "Calcium", "Zinc", "Magnesium"], 0, "Iron (Fe) có trong hemoglobin của hồng cầu."),
        make_mc(8, "Thông hiểu", "Cho các nguyên tử có cấu tạo hạt nhân như sau: X (6p, 6n), Y (7p, 7n), Z (6p, 7n). Các nguyên tử thuộc cùng một nguyên tố hóa học là:", ["X và Z", "X và Y", "Y và Z", "Cả X, Y, Z"], 0, "X và Z đều có 6 proton nên cùng thuộc nguyên tố Carbon."),
        make_mc(9, "Thông hiểu", "Tên gọi theo IUPAC của nguyên tố có kí hiệu Au là:", ["Gold", "Silver", "Aluminium", "Argon"], 0, "Au là Gold (Vàng)."),
        make_mc(10, "Thông hiểu", "Chất nào sau đây được cấu tạo từ DUY NHẤT một nguyên tố hóa học?", ["Khí nitrogen", "Nước tinh khiết", "Muối ăn", "Khí carbon dioxide"], 0, "Khí nitrogen chỉ gồm các nguyên tử nguyên tố N."),
        make_mc(11, "Thông hiểu", "Khối lượng nguyên tử của nguyên tố Magnesium theo amu là:", ["24 amu", "12 amu", "23 amu", "27 amu"], 0, "Magnesium có khối lượng nguyên tử xấp xỉ 24 amu."),
        make_mc(12, "Thông hiểu", "Kí hiệu của nguyên tố chì theo IUPAC (Lead) là:", ["Pb", "Pl", "Pd", "Pt"], 0, "Lead có kí hiệu là Pb.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các nguyên tố có trong cơ thể con người:", [
            ("a", "Oxygen, Carbon, Hydrogen và Nitrogen chiếm khoảng 96% khối lượng cơ thể.", True),
            ("b", "Thiếu nguyên tố Iodine (I) có thể dẫn đến bệnh bướu cổ.", True),
            ("c", "Iron (Fe) là nguyên tố vi lượng cần thiết cho quá trình tạo máu.", True),
            ("d", "Cơ thể con người không chứa bất kì nguyên tố kim loại nào.", False)
        ], "Cơ thể chứa nhiều nguyên tố kim loại như Ca, Na, K, Fe, Mg, Zn..."),
        make_tf(2, "Thông hiểu", "Về quy tắc đặt tên và kí hiệu hóa học của các nguyên tố:", [
            ("a", "Tên nguyên tố hiện nay được thống nhất gọi theo danh pháp quốc tế IUPAC.", True),
            ("b", "Kí hiệu hóa học thường được lấy từ chữ cái đầu tiên trong tên tiếng Latin hoặc tiếng Anh.", True),
            ("c", "Nếu kí hiệu gồm 2 chữ cái thì cả 2 chữ cái đều phải viết hoa.", False),
            ("d", "Mỗi nguyên tố hóa học chỉ có duy nhất một kí hiệu hóa học tương ứng.", True)
        ], "Chữ cái thứ hai bắt buộc phải viết thường (ví dụ: He, Na, Ca)."),
        make_tf(3, "Vận dụng", "Cho các nguyên tố hóa học: H (1 amu), C (12 amu), N (14 amu), O (16 amu), Na (23 amu):", [
            ("a", "Nguyên tử Na nặng hơn nguyên tử C xấp xỉ 1,92 lần.", True),
            ("b", "Hai nguyên tử H có khối lượng bằng 2 amu.", True),
            ("c", "Nguyên tử O nhẹ hơn nguyên tử N.", False),
            ("d", "Tổng khối lượng của 1 nguyên tử C và 2 nguyên tử O là 44 amu.", True)
        ], "Oxygen (16 amu) nặng hơn Nitrogen (14 amu)."),
        make_tf(4, "Vận dụng", "Nguyên tố R có nguyên tử nặng gấp 2,5 lần nguyên tử Oxygen:", [
            ("a", "Khối lượng nguyên tử của R là 40 amu.", True),
            ("b", "Tên gọi theo IUPAC của R là Calcium.", True),
            ("c", "Kí hiệu hóa học của R là Ca.", True),
            ("d", "R là một nguyên tố phi kim ở thể khí.", False)
        ], "Calcium là kim loại kiềm thổ ở thể rắn.")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Kí hiệu hóa học của nguyên tố Kẽm (Zinc) là gì?", "Zn", "Zinc có kí hiệu là Zn."),
        make_sa(2, "Thông hiểu", "Nguyên tố Silicon có bao nhiêu proton trong hạt nhân?", "14", "Silicon có số hiệu Z = 14."),
        make_sa(3, "Vận dụng", "Một nguyên tử nguyên tố X có khối lượng nặng gấp 2 lần khối lượng nguyên tử Carbon. Kí hiệu hóa học của X là gì?", "Mg", "Khối lượng X = 2 × 12 = 24 amu => Magnesium (Mg)."),
        make_sa(4, "Vận dụng", "Nguyên tố nào có khối lượng nguyên tử bằng 39 amu? (Viết kí hiệu hóa học)", "K", "Potassium (K) có khối lượng nguyên tử là 39 amu."),
        make_sa(5, "Vận dụng cao", "Một hợp chất có dạng XO2, biết phân tử khối của hợp chất là 64 amu. Kí hiệu hóa học của nguyên tố X là gì?", "S", "X + 2 × 16 = 64 => X = 32 => Sulfur (S)."),
        make_sa(6, "Vận dụng cao", "Hạt nhân nguyên tử nguyên tố Y có tổng số proton và neutron là 19. Biết số hạt neutron nhiều hơn proton là 1. Tên gọi theo IUPAC của Y là gì?", "Fluorine", "p + n = 19, n - p = 1 => p = 9 (Fluorine).")
    ],
    "part4": [
        make_vdc(1, "Nguyên tử của nguyên tố X có khối lượng gấp 2,25 lần nguyên tử Carbon. Số electron ở lớp ngoài cùng của nguyên tử X là:", ["3", "1", "2", "7"], 0, "Khối lượng X = 2,25 × 12 = 27 amu => Aluminium (Al, Z=13). Cấu hình: 2, 8, 3 => lớp ngoài cùng có 3e."),
        make_vdc(2, "Một hợp chất gồm 2 nguyên tử của nguyên tố X liên kết với 3 nguyên tử Oxygen, nặng gấp 5 lần phân tử khí Oxygen (O2). Nguyên tố X là:", ["Iron (Fe)", "Aluminium (Al)", "Chromium (Cr)", "Phosphorus (P)"], 0, "Khối lượng hợp chất = 5 × 32 = 160 amu. 2X + 3 × 16 = 160 => 2X = 112 => X = 56 (Iron)."),
        make_vdc(3, "Khối lượng của một nguyên tử nguyên tố A tính bằng gam là 4,482 × 10^-23 gam. Biết 1 amu = 1,6605 × 10^-24 gam. Kí hiệu hóa học của nguyên tố A là:", ["Al", "Mg", "Na", "Si"], 0, "Khối lượng amu = 4,482 × 10^-23 / (1,6605 × 10^-24) ≈ 27 amu => Al."),
        make_vdc(4, "Nguyên tố X có tỉ số giữa số hạt mang điện và hạt không mang điện trong nguyên tử là 1,875. Biết tổng số hạt cơ bản là 46. X là nguyên tố nào?", ["Phosphorus (P)", "Sulfur (S)", "Chlorine (Cl)", "Silicon (Si)"], 0, "2p / n = 1,875 => 2p = 1,875n. Thay vào 2p + n = 46 => 2,875n = 46 => n = 16 => 2p = 30 => p = 15 (Phosphorus).")
    ]
}

# --- ĐỀ 3: Ứng dụng thực tiễn, phân loại nguyên tố, tính toán khối lượng & so sánh ---
chem7_exams["chem7_c1_b3_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Kí hiệu hóa học của nguyên tố Boron là:", ["B", "Bo", "Br", "Ba"], 0, "Boron có kí hiệu là B."),
        make_mc(2, "Nhận biết", "Tên IUPAC của nguyên tố có kí hiệu 'Ba' là:", ["Barium", "Boron", "Beryllium", "Bromine"], 0, "Ba là Barium."),
        make_mc(3, "Nhận biết", "Nguyên tố phi kim ở thể lỏng duy nhất ở điều kiện nhiệt độ phòng là:", ["Bromine", "Mercury", "Chlorine", "Iodine"], 0, "Bromine (Br2) là chất lỏng màu nâu đỏ (Mercury là kim loại lỏng)."),
        make_mc(4, "Nhận biết", "Nguyên tố kim loại ở thể lỏng duy nhất ở nhiệt độ phòng dùng trong nhiệt kế thủy ngân là:", ["Mercury (Thủy ngân)", "Lead (Chì)", "Silver (Bạc)", "Gallium"], 0, "Mercury (Hg) là kim loại dạng lỏng ở nhiệt độ thường."),
        make_mc(5, "Nhận biết", "Kí hiệu hóa học của nguyên tố Lưu huỳnh theo IUPAC (Sulfur) là:", ["S", "Su", "Sf", "Sl"], 0, "Sulfur có kí hiệu là S."),
        make_mc(6, "Nhận biết", "Nguyên tố nào sau đây là khí hiếm được dùng nhiều trong biển quảng cáo phát sáng màu cam đỏ?", ["Neon", "Argon", "Helium", "Krypton"], 0, "Đèn neon phát ánh sáng cam đỏ rực rỡ."),
        make_mc(7, "Thông hiểu", "Nguyên tố kim loại dẫn điện và dẫn nhiệt tốt nhất là:", ["Silver (Bạc)", "Copper (Đồng)", "Gold (Vàng)", "Aluminium (Nhôm)"], 0, "Silver dẫn điện tốt nhất, tiếp theo là Copper."),
        make_mc(8, "Thông hiểu", "Hai nguyên tử khác nhau nhưng có cùng số neutron thì:", ["Chưa chắc thuộc cùng một nguyên tố hóa học", "Chắc chắn thuộc cùng một nguyên tố hóa học", "Luôn có tính chất hóa học giống nhau", "Luôn có cùng số proton"], 0, "Các nguyên tố khác nhau có thể có cùng số neutron (ví dụ 14C và 14N không cùng số n, 13C và 14N có cùng 7n)."),
        make_mc(9, "Thông hiểu", "Kí hiệu của nguyên tố Chromium là:", ["Cr", "Ch", "Cm", "Co"], 0, "Chromium có kí hiệu là Cr."),
        make_mc(10, "Thông hiểu", "Khối lượng nguyên tử của nguyên tố Chlorine theo bảng tuần hoàn thường lấy xấp xỉ là:", ["35,5 amu", "35 amu", "36 amu", "37 amu"], 0, "Chlorine có 2 đồng vị bền phổ biến 35Cl và 37Cl, nguyên tử khối trung bình là 35,5 amu."),
        make_mc(11, "Thông hiểu", "Nguyên tố nào sau đây được dùng nhiều để sản xuất phân bón đạm cho cây trồng?", ["Nitrogen", "Potassium", "Phosphorus", "Calcium"], 0, "Phân đạm cung cấp nguyên tố Nitrogen (N) cho cây trồng."),
        make_mc(12, "Thông hiểu", "Kim loại nhẹ và bền dùng nhiều trong công nghiệp chế tạo máy bay và vỏ điện thoại là:", ["Aluminium", "Iron", "Lead", "Copper"], 0, "Aluminium (Nhôm) nhẹ và có màng oxide bảo vệ.")
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Cho các nguyên tố: He, Ne, Ar, Kr, Xe:", [
            ("a", "Đây là nhóm các nguyên tố khí hiếm (khí trơ).", True),
            ("b", "Các nguyên tố này đều rất bền vững và khó tham gia phản ứng hóa học.", True),
            ("c", "Ở điều kiện thường, chúng tồn tại dưới dạng phân tử hai nguyên tử như He2.", False),
            ("d", "Neon và Argon được ứng dụng rộng rãi trong chiếu sáng nghệ thuật.", True)
        ], "Khí hiếm tồn tại dưới dạng đơn nguyên tử (He, Ne, Ar...)."),
        make_tf(2, "Thông hiểu", "Xét về nguồn gốc và vai trò của các nguyên tố hóa học:", [
            ("a", "Trong vũ trụ, Hydrogen và Helium là hai nguyên tố dồi dào nhất.", True),
            ("b", "Nước được tạo nên từ hai nguyên tố hóa học là Hydrogen và Oxygen.", True),
            ("c", "Muối ăn hàng ngày là hợp chất của hai nguyên tố Sodium và Chlorine.", True),
            ("d", "Kim cương và than chì được cấu tạo từ hai nguyên tố hóa học khác nhau.", False)
        ], "Kim cương và than chì đều là các dạng thù hình cấu tạo từ duy nhất nguyên tố Carbon."),
        make_tf(3, "Vận dụng", "Cho các nguyên tố: H (1 amu), O (16 amu), S (32 amu), Fe (56 amu):", [
            ("a", "Khối lượng của một nguyên tử Fe nặng gấp 3,5 lần nguyên tử O.", True),
            ("b", "Một nguyên tử S nặng gấp 2 lần một nguyên tử O.", True),
            ("c", "Phân tử nước (H2O) có khối lượng là 18 amu.", True),
            ("d", "Khối lượng phân tử H2SO4 nhẹ hơn khối lượng phân tử FeO.", False)
        ], "H2SO4 có khối lượng = 2*1 + 32 + 64 = 98 amu; FeO = 56 + 16 = 72 amu => H2SO4 nặng hơn."),
        make_tf(4, "Vận dụng", "Nguyên tử nguyên tố M có tổng số hạt cơ bản là 40, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 12:", [
            ("a", "Số proton của nguyên tố M là 13.", True),
            ("b", "Tên IUPAC của M là Aluminium.", True),
            ("c", "M là nguyên tố phi kim ở trạng thái khí.", False),
            ("d", "Khối lượng nguyên tử của M là 27 amu.", True)
        ], "M là Aluminium (kim loại).")
    ],
    "part3": [
        make_sa(1, "Thông hiểu", "Kí hiệu hóa học của nguyên tố Bạc (Silver) gồm mấy chữ cái?", "2", "Silver có kí hiệu là Ag (2 chữ cái)."),
        make_sa(2, "Thông hiểu", "Nguyên tố Calcium có khối lượng nguyên tử bằng bao nhiêu amu?", "40", "Calcium có khối lượng nguyên tử là 40 amu."),
        make_sa(3, "Vận dụng", "Một phân tử carbon dioxide (CO2) có khối lượng phân tử là bao nhiêu amu?", "44", "12 + 2 × 16 = 44 amu."),
        make_sa(4, "Vận dụng", "Nguyên tố X có số proton bằng số neutron, tổng số hạt mang điện trong hạt nhân là 8. Kí hiệu của X là gì?", "O", "p = 8 => Oxygen (O)."),
        make_sa(5, "Vận dụng cao", "Phân tử muối ăn gồm 1 nguyên tử Na và 1 nguyên tử Cl. Khối lượng phân tử muối ăn theo amu là bao nhiêu? (Làm tròn 1 chữ số thập phân)", "58.5", "23 + 35,5 = 58,5 amu."),
        make_sa(6, "Vận dụng cao", "Một nguyên tử nguyên tố X có 20 neutron và khối lượng nguyên tử là 39 amu. Tên gọi theo IUPAC của X là gì?", "Potassium", "p = 39 - 20 = 19 (Potassium).")
    ],
    "part4": [
        make_vdc(1, "Một hợp chất có phân tử gồm 1 nguyên tử nguyên tố X liên kết với 2 nguyên tử Oxygen và nặng gấp 2,75 lần phân tử Oxygen. Kí hiệu hóa học của X là:", ["N", "C", "S", "Si"], 0, "Khối lượng phân tử = 2,75 × 32 = 88 amu không có... Nếu nặng gấp 1,375 lần O2 => 44 amu (CO2) hoặc nặng 64 amu (SO2). Sửa: nặng gấp 2 lần phân tử O2 => 64 amu => X + 32 = 64 => X = 32 (S)."),
        make_vdc(2, "Khối lượng tính bằng gam của 6,022 × 10^23 nguyên tử Sodium (Na, 23 amu) là bao nhiêu? (Biết 1 amu = 1,6605 × 10^-24 g):", ["23 gam", "11 gam", "46 gam", "12 gam"], 0, "6,022 × 10^23 × 23 × 1,6605 × 10^-24 g ≈ 23 gam (khái niệm mol nguyên tử)."),
        make_vdc(3, "Nguyên tử nguyên tố Y có tổng số hạt cơ bản là 52. Số hạt mang điện nhiều hơn số hạt không mang điện là 16. Y thuộc loại nguyên tố nào?", ["Phi kim (Chlorine)", "Kim loại (Sodium)", "Khí hiếm (Argon)", "Kim loại (Aluminium)"], 0, "p = 17 (Chlorine), là phi kim nhóm halogen."),
        make_vdc(4, "Một oxide kim loại có công thức M2O3, trong đó O chiếm 30% về khối lượng. Nguyên tố M là:", ["Iron (Fe)", "Aluminium (Al)", "Chromium (Cr)", "Titanium (Ti)"], 0, "(3 × 16) / (2M + 48) = 0,3 => 2M + 48 = 160 => 2M = 112 => M = 56 (Iron).")
    ]
}

print(f"Tổng số đề đã nạp: {len(chem7_exams)} đề.")
