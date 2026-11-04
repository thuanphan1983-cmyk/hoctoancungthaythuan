# -*- coding: utf-8 -*-
"""
HỆ THỐNG SINH ĐỀ KIỂM TRA THEO BÀI CHO TOÁN 3 (KNTT)
Gồm 27 bài học, mỗi bài có 3 đề kiểm tra độc lập (Đề 1, Đề 2, Đề 3).
Tổng cộng: 81 đề kiểm tra.
Cấu trúc mỗi đề:
- Phần I: 6 câu trắc nghiệm (1.5 điểm: 6 x 0.25đ)
- Phần II: 6 bài tự luận (8.5 điểm, có trừ dòng kẻ lineCount cho học sinh làm bài)
- Tổng điểm: 10.0 điểm
"""

import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def mc(qid, question, options, correct, explanation):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.25
    }

def essay(qid, question, solution, answer, lineCount=4, points=1.0):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    return {
        "id": qid,
        "question": p_text,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def build_toan3_lesson(l_num, t_num):
    """Sinh bộ 6 trắc nghiệm + 6 tự luận chuyên biệt theo từng bài Toán 3"""
    # 1, 2, 3. Bảng nhân, chia 2, 3, 4, 5
    if l_num in [1, 2, 3]:
        factor = 2 if l_num == 1 else (3 if l_num == 2 else 4)
        n_step = 4 + t_num * 2
        return [
            mc(1, f"Kết quả của phép nhân ${factor} \\times {n_step}$ là:", [str(factor * n_step), str(factor * n_step + 1), str(factor * n_step - 2), "20"], 0, f"${factor} \\times {n_step} = {factor * n_step}$."),
            mc(2, f"Kết quả của phép chia ${factor * n_step} : {factor}$ là:", [str(n_step), str(n_step + 1), str(n_step - 1), str(factor)], 0, f"${factor * n_step} : {factor} = {n_step}$."),
            mc(3, f"Số thích hợp điền vào ô trống: ${factor} \\times ... = {factor * 7}$", ["7", "6", "8", "9"], 0, f"${factor * 7} : {factor} = 7$."),
            mc(4, f"Một số chia cho {factor} được thương là 8. Số bị chia là:", [str(factor * 8), str(factor * 8 - 1), str(factor * 8 + 2), "30"], 0, f"Số bị chia là: $8 \\times {factor} = {factor * 8}$."),
            mc(5, f"Tính: ${factor} \\times 5 + 10 = $", [str(factor * 5 + 10), str(factor * 5), "30", "25"], 0, f"${factor * 5} + 10 = {factor * 5 + 10}$."),
            mc(6, f"Có {factor * 6} quyển vở chia đều cho {factor} bạn. Mỗi bạn nhận được:", ["6 quyển vở", "5 quyển", "7 quyển", "4 quyển"], 0, f"${factor * 6} : {factor} = 6$ quyển vở.")
        ], [
            essay(1, f"Tính nhẩm:\na) ${factor} \\times 6 = .....$\nb) ${factor} \\times 9 = .....$\nc) ${factor * 4} : {factor} = .....$\nd) ${factor * 8} : {factor} = .....$", f"Bài giải:\na) {factor * 6}\nb) {factor * 9}\nc) 4\nd) 8\nĐáp số: {factor * 6}, {factor * 9}, 4, 8", f"{factor * 6}, {factor * 9}, 4, 8", 4, 1.0),
            essay(2, f"Tính giá trị biểu thức:\na) ${factor} \\times 8 + 36 = .....$\nb) ${factor * 10} : {factor} - 4 = .....$", f"Bài giải:\na) {factor * 8} + 36 = {factor * 8 + 36}\nb) 10 - 4 = 6\nĐáp số: a) {factor * 8 + 36}; b) 6", f"a) {factor * 8 + 36}; b) 6", 4, 1.0),
            essay(3, f"Tìm x biết:\na) $x : {factor} = 9$\nb) ${factor} \\times x = {factor * 7}$", f"Bài giải:\na) x = 9 x {factor} = {9 * factor}\nb) x = {factor * 7} : {factor} = 7\nĐáp số: a) x = {9 * factor}; b) x = 7", f"a) {9 * factor}; b) 7", 4, 1.0),
            essay(4, f"Mỗi bàn học có {factor} học sinh ngồi. Hỏi 8 bàn học như thế có tất cả bao nhiêu học sinh ngồi?", f"Bài giải:\n8 bàn học có tất cả số học sinh là:\n{factor} x 8 = {factor * 8} (học sinh)\nĐáp số: {factor * 8} học sinh", f"{factor * 8} học sinh", 5, 1.5),
            essay(5, f"Có {factor * 9} bông hoa đem cắm đều vào {factor} lọ hoa. Hỏi mỗi lọ có bao nhiêu bông hoa?", f"Bài giải:\nMỗi lọ có số bông hoa là:\n{factor * 9} : {factor} = 9 (bông hoa)\nĐáp số: 9 bông hoa", "9 bông hoa", 5, 2.0),
            essay(6, f"Tìm một số biết rằng lấy số đó nhân với {factor} rồi trừ đi 12 thì được kết quả bằng 24.", f"Bài giải:\nSố đó nhân với {factor} là: 24 + 12 = 36.\nSố cần tìm là: 36 : {factor} = {36 // factor}.\nĐáp số: {36 // factor}", f"{36 // factor}", 4, 2.0)
        ]

    # 4, 5, 6. Bảng nhân, chia 6, 7, 8, 9; Gấp / giảm một số lần
    elif l_num in [4, 5, 6]:
        b_fact = 6 if l_num == 4 else (8 if l_num == 5 else 7)
        k_step = 5 + t_num
        return [
            mc(1, f"Kết quả phép tính ${b_fact} \\times {k_step}$ là:", [str(b_fact * k_step), str(b_fact * k_step + 2), str(b_fact * k_step - 4), "50"], 0, f"${b_fact} \\times {k_step} = {b_fact * k_step}$."),
            mc(2, f"Gấp số 6 lên 4 lần ta được:", ["24", "10", "18", "30"], 0, "$6 \\times 4 = 24$."),
            mc(3, f"Giảm số 35 đi 5 lần ta được:", ["7", "30", "8", "6"], 0, "$35 : 5 = 7$."),
            mc(4, f"Kết quả phép chia ${b_fact * 7} : {b_fact}$ là:", ["7", "6", "8", "9"], 0, f"${b_fact * 7} : {b_fact} = 7$."),
            mc(5, "Số nào giảm đi 6 lần thì được 8?", ["48", "14", "42", "54"], 0, "$8 \\times 6 = 48$."),
            mc(6, "Mai có 8 cái kẹo, số kẹo của Lan gấp 3 lần số kẹo của Mai. Lan có:", ["24 cái kẹo", "11 cái", "16 cái", "20 cái"], 0, "$8 \\times 3 = 24$ cái kẹo.")
        ], [
            essay(1, "Tính nhẩm:\na) $7 \\times 8 = .....$\nb) $9 \\times 6 = .....$\nc) $56 : 7 = .....$\nd) $72 : 8 = .....$", "Bài giải:\na) 56\nb) 54\nc) 8\nd) 9\nĐáp số: 56, 54, 8, 9", "56, 54, 8, 9", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $8 \\times 7 + 45 = .....$\nb) $63 : 9 \\times 5 = .....$\nc) $80 - 48 : 6 = .....$", "Bài giải:\na) 56 + 45 = 101\nb) 7 x 5 = 35\nc) 80 - 8 = 72\nĐáp số: a) 101; b) 35; c) 72", "a) 101; b) 35; c) 72", 4, 1.0),
            essay(3, "a) Gấp số 9 lên 5 lần rồi bớt đi 15.\nb) Giảm số 48 đi 6 lần rồi thêm vào 20.", "Bài giải:\na) 9 x 5 = 45; 45 - 15 = 30\nb) 48 : 6 = 8; 8 + 20 = 28\nĐáp số: a) 30; b) 28", "a) 30; b) 28", 4, 1.0),
            essay(4, "Năm nay con 7 tuổi, tuổi của mẹ gấp 5 lần tuổi của con. Hỏi năm nay mẹ bao nhiêu tuổi?", "Bài giải:\nNăm nay mẹ có số tuổi là:\n7 x 5 = 35 (tuổi)\nĐáp số: 35 tuổi", "35 tuổi", 5, 1.5),
            essay(5, "Một cuộn dây dài 54 mét, người ta đã cắt đi một đoạn dây bằng 1/6 chiều dài cuộn dây. Hỏi cuộn dây còn lại bao nhiêu mét?", "Bài giải:\nĐoạn dây đã cắt đi dài là:\n54 : 6 = 9 (m)\nCuộn dây còn lại số mét là:\n54 - 9 = 45 (m)\nĐáp số: 45 mét", "45 mét", 5, 2.0),
            essay(6, "Tìm một số biết rằng nếu gấp số đó lên 7 lần rồi giảm đi 3 đơn vị thì được 39.", "Bài giải:\nSố đó nhân với 7 là: 39 + 3 = 42.\nSố cần tìm là: 42 : 7 = 6.\nĐáp số: 6", "6", 4, 2.0)
        ]

    # 7 & 8. Hình học: Góc vuông, không vuông; Hình tròn, bán kính, đường kính
    elif l_num in [7, 8]:
        return [
            mc(1, "Dụng cụ dùng để kiểm tra góc vuông là:", ["Thước ê ke", "Com-pa", "Cân đồng hồ", "Nhiệt kế"], 0, "Dùng thước ê ke."),
            mc(2, "Hình tròn có bán kính $r = 5\\text{ cm}$. Đường kính của hình tròn đó là:", ["10 cm", "25 cm", "15 cm", "5 cm"], 0, "Đường kính gấp đôi bán kính: $5 \\times 2 = 10$ cm."),
            mc(3, "Hình tròn có đường kính $d = 16\\text{ cm}$. Bán kính của hình tròn đó là:", ["8 cm", "32 cm", "4 cm", "12 cm"], 0, "Bán kính bằng một nửa đường kính: $16 : 2 = 8$ cm."),
            mc(4, "Trong một hình tròn, độ dài các bán kính thì:", ["Bằng nhau", "Khác nhau", "Gấp đôi nhau", "Tùy ý"], 0, "Mọi bán kính đều bằng nhau."),
            mc(5, "Hình vuông có mấy góc vuông?", ["4 góc vuông", "3 góc vuông", "2 góc vuông", "Không có"], 0, "Hình vuông có 4 góc vuông."),
            mc(6, "Góc đỉnh O, cạnh OA, OB tạo bởi hai cạnh vuông góc gọi là:", ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0, "Góc vuông.")
        ], [
            essay(1, "Cho hình tròn tâm O có bán kính $r = 6\\text{ cm}$.\na) Tính đường kính của hình tròn đó.\nb) Điểm M nằm trên đường tròn, hỏi đoạn OM dài bao nhiêu xăng-ti-mét?", "Bài giải:\na) Đường kính của hình tròn là:\n6 x 2 = 12 (cm)\nb) Vì M nằm trên đường tròn nên OM là bán kính, do đó OM = 6 cm.\nĐáp số: a) 12 cm; b) 6 cm", "a) 12 cm; b) 6 cm", 4, 1.0),
            essay(2, "Dùng ê ke hãy nêu cách kiểm tra góc vuông tại đỉnh A của tứ giác ABCD.", "Bài giải:\n1. Đặt đỉnh góc vuông của ê ke trùng với đỉnh A của tứ giác.\n2. Đặt một cạnh góc vuông của ê ke trùng với cạnh AB.\n3. Nếu cạnh AC trùng khít với cạnh góc vuông còn lại của ê ke thì góc đỉnh A là góc vuông.\nĐáp số: Nêu đúng 3 thao tác kiểm tra", "Đúng các bước dùng ê ke", 4, 1.0),
            essay(3, "Vẽ hình tròn tâm I có bán kính $r = 3\\text{ cm}$ bằng compa và vẽ một đường kính AB của hình tròn đó.", "Bài giải:\n- Dùng compa mở rộng khẩu độ 3 cm trên thước thẳng.\n- Cắm đầu nhọn compa vào điểm I và quay một vòng tròn khép kín.\n- Kẻ đoạn thẳng đi qua tâm I cắt đường tròn tại hai điểm A và B.\nĐáp số: Hình vẽ chuẩn xác 100%", "Vẽ đúng hình tròn r=3cm", 4, 1.0),
            essay(4, "Một bánh xe đạp có bán kính 30 cm. Hỏi đường kính của bánh xe đạp đó dài bao nhiêu xăng-ti-mét?", "Bài giải:\nĐường kính của bánh xe đạp là:\n30 x 2 = 60 (cm)\nĐáp số: 60 cm", "60 cm", 5, 1.5),
            essay(5, "Một hình chữ nhật có mấy góc vuông? Tổng số góc vuông của 3 hình chữ nhật là bao nhiêu?", "Bài giải:\n- Mỗi hình chữ nhật có 4 góc vuông.\n- Tổng số góc vuông của 3 hình chữ nhật là: 4 x 3 = 12 (góc vuông).\nĐáp số: 12 góc vuông", "12 góc vuông", 5, 2.0),
            essay(6, "Cho đoạn thẳng AB dài 10 cm, O là trung điểm của AB. Vẽ đường tròn tâm O bán kính OA. Hỏi đường kính của hình tròn này dài bao nhiêu xăng-ti-mét?", "Bài giải:\nVì O là trung điểm của AB nên OA = OB = 10 : 2 = 5 (cm).\nĐoạn thẳng AB đi qua tâm O và nối hai điểm trên đường tròn nên chính là đường kính.\nVậy đường kính dài 10 cm.\nĐáp số: 10 cm", "10 cm", 4, 2.0)
        ]

    # 9 & 10. Nhân, chia số có hai, ba chữ số với số có 1 chữ số
    elif l_num in [9, 10]:
        m1 = 124 + t_num * 15
        return [
            mc(1, f"Đặt tính rồi tính: ${m1} \\times 3 = $", [str(m1 * 3), str(m1 * 3 + 2), str(m1 * 3 - 5), "300"], 0, f"${m1} \\times 3 = {m1 * 3}$."),
            mc(2, f"Đặt tính rồi tính: ${m1 * 2} : 2 = $", [str(m1), str(m1 + 2), str(m1 - 2), "100"], 0, f"${m1 * 2} : 2 = {m1}$."),
            mc(3, "Tìm số dư trong phép chia $47 : 5$:", ["2", "3", "1", "4"], 0, "$47 = 5 \\times 9 + 2$ nên dư 2."),
            mc(4, "Trong phép chia có dư với số chia là 6, số dư lớn nhất có thể là:", ["5", "6", "4", "7"], 0, "Số dư luôn bé hơn số chia, lớn nhất là $6 - 1 = 5$."),
            mc(5, f"Tính: $215 \\times 4 = $", ["860", "850", "840", "880"], 0, "$215 \\times 4 = 860$."),
            mc(6, f"Tính: $848 : 4 = $", ["212", "214", "202", "222"], 0, "$848 : 4 = 212$.")
        ], [
            essay(1, "Đặt tính rồi tính:\na) $234 \\times 3$\nb) $142 \\times 5$\nc) $648 : 2$\nd) $845 : 4$", "Bài giải:\na) 702\nb) 710\nc) 324\nd) 211 (dư 1)\nĐáp số: a) 702; b) 710; c) 324; d) 211 dư 1", "702, 710, 324, 211 dư 1", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $125 \\times 4 + 180 = .....$\nb) $936 : 3 - 112 = .....$", "Bài giải:\na) 500 + 180 = 680\nb) 312 - 112 = 200\nĐáp số: a) 680; b) 200", "a) 680; b) 200", 4, 1.0),
            essay(3, "Tìm x biết:\na) $x : 4 = 132$\nb) $x \\times 3 = 693$", "Bài giải:\na) x = 132 x 4 = 528\nb) x = 693 : 3 = 231\nĐáp số: a) x = 528; b) x = 231", "a) 528; b) 231", 4, 1.0),
            essay(4, "Một đội công nhân làm đường, mỗi ngày trải nhựa được 135 mét đường. Hỏi trong 4 ngày đội công nhân đó trải nhựa được bao nhiêu mét đường?", "Bài giải:\nTrong 4 ngày đội trải nhựa được số mét đường là:\n135 x 4 = 540 (m)\nĐáp số: 540 mét", "540 mét", 5, 1.5),
            essay(5, "Có 248 lít dầu chia đều vào 4 thùng. Hỏi mỗi thùng chứa bao nhiêu lít dầu?", "Bài giải:\nMỗi thùng chứa số lít dầu là:\n248 : 4 = 62 (lít)\nĐáp số: 62 lít", "62 lít", 5, 2.0),
            essay(6, "Cần xếp 95 chiếc cốc vào các hộp, mỗi hộp đựng được 6 chiếc cốc. Hỏi cần ít nhất bao nhiêu hộp để đựng hết số cốc đó?", "Bài giải:\nTa có phép chia: 95 : 6 = 15 (dư 5).\nNhư vậy đựng đầy 15 hộp và còn thừa 5 chiếc cốc. Cần thêm 1 hộp nữa để đựng 5 chiếc cốc này.\nSố hộp ít nhất cần là: 15 + 1 = 16 (hộp).\nĐáp số: 16 hộp", "16 hộp", 4, 2.0)
        ]

    # 11, 12, 13. Đại lượng: Gam (g), Mi-li-lít (ml), Nhiệt độ (°C)
    elif l_num in [11, 12, 13]:
        return [
            mc(1, "Đổi: $1\\text{ kg} = ...\\text{ g}$", ["1 000 g", "100 g", "10 g", "10 000 g"], 0, "1 kg = 1000 g."),
            mc(2, "Đổi: $1\\text{ l} = ...\\text{ ml}$", ["1 000 ml", "100 ml", "10 ml", "10 000 ml"], 0, "1 l = 1000 ml."),
            mc(3, "Nhiệt kế đo nhiệt độ cơ thể người bình thường khỏe mạnh là khoảng:", ["37 °C", "42 °C", "25 °C", "100 °C"], 0, "Khoảng 37 °C."),
            mc(4, "Nước sôi ở nhiệt độ bao nhiêu độ C?", ["100 °C", "50 °C", "0 °C", "200 °C"], 0, "Nước sôi ở 100 °C."),
            mc(5, f"Tính: $450\\text{{ g}} + 250\\text{{ g}} = $", ["700 g", "600 g", "800 g", "650 g"], 0, "450 + 250 = 700 g."),
            mc(6, f"Tính: $1 000\\text{{ ml}} - 350\\text{{ ml}} = $", ["650 ml", "750 ml", "550 ml", "700 ml"], 0, "1000 - 350 = 650 ml.")
        ], [
            essay(1, "Điền số thích hợp vào chỗ chấm:\na) $1\\text{ kg} = .....\\text{ g}$\nb) $1\\text{ l} = .....\\text{ ml}$\nc) $500\\text{ g} + .....\\text{ g} = 1\\text{ kg}$\nd) $1\\text{ l} - 400\\text{ ml} = .....\\text{ ml}$", "Bài giải:\na) 1000 g\nb) 1000 ml\nc) 500 g\nd) 600 ml\nĐáp số: 1000, 1000, 500, 600", "1000, 1000, 500, 600", 4, 1.0),
            essay(2, "Tính:\na) $350\\text{ g} + 280\\text{ g} = .....$\nb) $850\\text{ ml} - 320\\text{ ml} = .....$\nc) $250\\text{ g} \\times 3 = .....$", "Bài giải:\na) 630 g\nb) 530 ml\nc) 750 g\nĐáp số: 630 g, 530 ml, 750 g", "630 g, 530 ml, 750 g", 4, 1.0),
            essay(3, "Nhiệt độ buổi sáng là 24 °C, buổi trưa nhiệt độ tăng thêm 8 °C. Hỏi nhiệt độ buổi trưa là bao nhiêu độ C?", "Bài giải:\nNhiệt độ buổi trưa là:\n24 + 8 = 32 (°C)\nĐáp số: 32 °C", "32 °C", 4, 1.0),
            essay(4, "Một gói bánh quy nặng 250 g, một hộp kẹo nặng 500 g. Hỏi 2 gói bánh quy và 1 hộp kẹo nặng tất cả bao nhiêu ki-lô-gam?", "Bài giải:\n2 gói bánh quy nặng số gam là: 250 x 2 = 500 (g).\nTổng khối lượng là: 500 + 500 = 1 000 (g).\nĐổi: 1 000 g = 1 kg.\nĐáp số: 1 kg", "1 kg", 5, 1.5),
            essay(5, "Một chai nước khoáng chứa 500 ml nước. Bạn Nam uống hết 200 ml. Hỏi trong chai còn lại bao nhiêu mi-li-lít nước?", "Bài giải:\nTrong chai còn lại số mi-li-lít nước là:\n500 - 200 = 300 (ml)\nĐáp số: 300 ml", "300 ml", 5, 2.0),
            essay(6, "Bác sĩ đo nhiệt độ của em bé bị sốt thấy nhiệt kế chỉ 39 °C. Sau khi uống thuốc hạ sốt, nhiệt độ giảm đi 2 °C. Hỏi lúc này nhiệt độ của em bé là bao nhiêu độ C?", "Bài giải:\nNhiệt độ lúc này của em bé là:\n39 - 2 = 37 (°C)\nĐáp số: 37 °C", "37 °C", 4, 2.0)
        ]

    # 14. Ôn tập học kì 1
    elif l_num == 14:
        return [
            mc(1, "Tính: $7 \\times 8 + 24 = $", ["80", "70", "90", "74"], 0, "$56 + 24 = 80$."),
            mc(2, "Tính: $72 : 9 \\times 4 = $", ["32", "28", "36", "24"], 0, "$8 \\times 4 = 32$."),
            mc(3, "Hình tròn có đường kính 14 cm thì bán kính là:", ["7 cm", "28 cm", "14 cm", "8 cm"], 0, "$14 : 2 = 7$ cm."),
            mc(4, "Số dư lớn nhất trong phép chia cho 7 là:", ["6", "7", "5", "8"], 0, "$7 - 1 = 6$."),
            mc(5, "Đổi: $1\\text{ kg} = ...\\text{ g}$", ["1 000 g", "100 g", "10 g", "500 g"], 0, "1 kg = 1000 g."),
            mc(6, "Gấp 15 lên 3 lần ta được:", ["45", "18", "30", "50"], 0, "$15 \\times 3 = 45$.")
        ], [
            essay(1, "Đặt tính rồi tính:\na) $218 \\times 4$\nb) $848 : 4$\nc) $105 \\times 6$\nd) $735 : 5$", "Bài giải:\na) 872\nb) 212\nc) 630\nd) 147\nĐáp số: 872, 212, 630, 147", "872, 212, 630, 147", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $135 + 240 : 6 = .....$\nb) $(150 - 45) \\times 4 = .....$", "Bài giải:\na) 135 + 40 = 175\nb) 105 x 4 = 420\nĐáp số: a) 175; b) 420", "a) 175; b) 420", 4, 1.0),
            essay(3, "Một mảnh vườn hình chữ nhật có chiều dài 24 m, chiều rộng bằng 1/3 chiều dài. Tính chu vi mảnh vườn đó.", "Bài giải:\nChiều rộng mảnh vườn là:\n24 : 3 = 8 (m)\nChu vi mảnh vườn là:\n(24 + 8) x 2 = 64 (m)\nĐáp số: 64 mét", "64 mét", 4, 1.0),
            essay(4, "Một cửa hàng có 360 kg đường. Ngày thứ nhất bán được 1/3 số đường đó. Hỏi cửa hàng còn lại bao nhiêu ki-lô-gam đường?", "Bài giải:\nNgày thứ nhất bán được số đường là:\n360 : 3 = 120 (kg)\nCửa hàng còn lại số ki-lô-gam đường là:\n360 - 120 = 240 (kg)\nĐáp số: 240 kg", "240 kg", 5, 1.5),
            essay(5, "Cho hình tròn tâm O bán kính OA = 8 cm. Tính độ dài đường kính của hình tròn đó.", "Bài giải:\nĐộ dài đường kính hình tròn là:\n8 x 2 = 16 (cm)\nĐáp số: 16 cm", "16 cm", 5, 2.0),
            essay(6, "Tìm một số biết rằng nếu lấy số đó chia cho 5 rồi cộng với 38 thì được kết quả bằng 60.", "Bài giải:\nSố đó chia cho 5 là: 60 - 38 = 22.\nSố cần tìm là: 22 x 5 = 110.\nĐáp số: 110", "110", 4, 2.0)
        ]

    # 15 & 16. Các số trong phạm vi 10 000
    elif l_num in [15, 16]:
        v4 = 3450 + t_num * 520
        return [
            mc(1, f"Số {v4} đọc là:", [f"Số {v4}", "Không đọc được", "Ba nghìn", "Bốn nghìn"], 0, f"Đọc đúng số {v4}."),
            mc(2, f"Số liền trước của số {v4} là:", [str(v4 - 1), str(v4 + 1), str(v4 - 10), str(v4)], 0, f"{v4} - 1 = {v4 - 1}."),
            mc(3, f"Số liền sau của số {v4} là:", [str(v4 + 1), str(v4 - 1), str(v4 + 10), str(v4)], 0, f"{v4} + 1 = {v4 + 1}."),
            mc(4, "Số lớn nhất có bốn chữ số là:", ["9 999", "10 000", "9 000", "9 990"], 0, "Số 9 999."),
            mc(5, "Số bé nhất có bốn chữ số là:", ["1 000", "1 001", "1 111", "0001"], 0, "Số 1 000."),
            mc(6, f"So sánh: {v4} ... {v4 + 100}", ["<", ">", "=", "Không có"], 0, f"{v4} < {v4 + 100}.")
        ], [
            essay(1, f"Viết số {v4} thành tổng nghìn, trăm, chục, đơn vị:", f"Bài giải:\n{v4} = {v4 // 1000 * 1000} + {((v4 % 1000) // 100) * 100} + {((v4 % 100) // 10) * 10} + {v4 % 10}\nĐáp số: Phân tích đúng cấu tạo số", "Đúng cấu tạo số", 4, 1.0),
            essay(2, "Sắp xếp các số 4 520, 8 105, 3 999, 4 502, 7 840 theo thứ tự:\na) Từ bé đến lớn\nb) Từ lớn đến bé", "Bài giải:\na) 3 999, 4 502, 4 520, 7 840, 8 105\nb) 8 105, 7 840, 4 520, 4 502, 3 999\nĐáp số: Đúng thứ tự hai chiều", "3999, 4502, 4520, 7840, 8105", 4, 1.0),
            essay(3, "Tìm số tròn nghìn liền trước và liền sau của số 6 500.", "Bài giải:\n- Số tròn nghìn liền trước 6 500 là: 6 000.\n- Số tròn nghìn liền sau 6 500 là: 7 000.\nĐáp số: 6 000 và 7 000", "6 000 và 7 000", 4, 1.0),
            essay(4, "Từ 4 chữ số 5, 0, 3, 8 hãy viết số lớn nhất có bốn chữ số khác nhau và số bé nhất có bốn chữ số khác nhau.", "Bài giải:\n- Số lớn nhất có 4 chữ số khác nhau là: 8 530.\n- Số bé nhất có 4 chữ số khác nhau là: 3 058.\nĐáp số: 8 530 và 3 058", "8 530 và 3 058", 5, 1.5),
            essay(5, "Tính: $3 500 + 2 400 - 1 200 = $", "Bài giải:\n3 500 + 2 400 = 5 900.\n5 900 - 1 200 = 4 700.\nĐáp số: 4 700", "4 700", 5, 2.0),
            essay(6, "Tìm số có bốn chữ số, biết chữ số hàng nghìn là 4, các chữ số còn lại đều bằng một nửa chữ số hàng nghìn.", "Bài giải:\nChữ số hàng nghìn là 4.\nCác chữ số hàng trăm, chục, đơn vị là: 4 : 2 = 2.\nSố cần tìm là: 4 222.\nĐáp số: 4 222", "4 222", 4, 2.0)
        ]

    # 17, 18, 19. Chu vi & Diện tích (tam giác, tứ giác, chữ nhật, vuông)
    elif l_num in [17, 18, 19]:
        w = 6 + t_num
        h = 10 + t_num * 2
        return [
            mc(1, f"Chu vi hình chữ nhật có chiều dài {h} cm, chiều rộng {w} cm là:", [f"{(h + w) * 2} cm", f"{h * w} cm", f"{h + w} cm", "50 cm"], 0, f"({h} + {w}) x 2 = {(h + w) * 2} cm."),
            mc(2, f"Diện tích hình chữ nhật có chiều dài {h} cm, chiều rộng {w} cm là:", [f"{h * w} cm²", f"{(h + w) * 2} cm²", f"{h * w} cm", "100 cm²"], 0, f"{h} x {w} = {h * w} cm²."),
            mc(3, f"Chu vi hình vuông có cạnh 7 cm là:", ["28 cm", "49 cm", "14 cm", "21 cm"], 0, "$7 \\times 4 = 28$ cm."),
            mc(4, f"Diện tích hình vuông có cạnh 8 cm là:", ["64 cm²", "32 cm²", "16 cm²", "64 cm"], 0, "$8 \\times 8 = 64$ cm²."),
            mc(5, "Chu vi hình tam giác có 3 cạnh dài 5 cm, 7 cm, 9 cm là:", ["21 cm", "20 cm", "22 cm", "18 cm"], 0, "$5 + 7 + 9 = 21$ cm."),
            mc(6, "Một hình vuông có chu vi 36 cm. Cạnh của hình vuông đó là:", ["9 cm", "6 cm", "18 cm", "8 cm"], 0, "$36 : 4 = 9$ cm.")
        ], [
            essay(1, f"Tính chu vi và diện tích hình chữ nhật có chiều dài {h} cm và chiều rộng {w} cm.", f"Bài giải:\n- Chu vi hình chữ nhật là:\n({h} + {w}) x 2 = {(h + w) * 2} (cm)\n- Diện tích hình chữ nhật là:\n{h} x {w} = {h * w} (cm²)\nĐáp số: Chu vi: {(h + w) * 2} cm; Diện tích: {h * w} cm²", f"P = {(h + w) * 2} cm; S = {h * w} cm²", 4, 1.0),
            essay(2, "Tính chu vi và diện tích một mảnh đất hình vuông có cạnh dài 15 mét.", "Bài giải:\n- Chu vi mảnh đất là:\n15 x 4 = 60 (m)\n- Diện tích mảnh đất là:\n15 x 15 = 225 (m²)\nĐáp số: Chu vi: 60 m; Diện tích: 225 m²", "P = 60 m; S = 225 m²", 4, 1.0),
            essay(3, "Một hình tứ giác có độ dài các cạnh lần lượt là 12 cm, 15 cm, 18 cm và 20 cm. Tính chu vi hình tứ giác đó.", "Bài giải:\nChu vi hình tứ giác là:\n12 + 15 + 18 + 20 = 65 (cm)\nĐáp số: 65 cm", "65 cm", 4, 1.0),
            essay(4, "Một mảnh vườn hình chữ nhật có chu vi là 48 m, chiều dài là 16 m. Tính chiều rộng và diện tích mảnh vườn đó.", "Bài giải:\nNửa chu vi mảnh vườn là:\n48 : 2 = 24 (m)\nChiều rộng mảnh vườn là:\n24 - 16 = 8 (m)\nDiện tích mảnh vườn là:\n16 x 8 = 128 (m²)\nĐáp số: Chiều rộng: 8 m; Diện tích: 128 m²", "Rộng 8 m; S = 128 m²", 5, 1.5),
            essay(5, "Một hình vuông có chu vi bằng chu vi hình chữ nhật có chiều dài 12 cm và chiều rộng 8 cm. Tính diện tích hình vuông đó.", "Bài giải:\nChu vi hình chữ nhật là:\n(12 + 8) x 2 = 40 (cm)\nCạnh hình vuông là:\n40 : 4 = 10 (cm)\nDiện tích hình vuông là:\n10 x 10 = 100 (cm²)\nĐáp số: 100 cm²", "100 cm²", 5, 2.0),
            essay(6, "Bác thợ mộc dùng lưới thép rào quanh một khu đất hình chữ nhật có chiều dài 18 m, chiều rộng 12 m. Biết bác để trống 2 m làm cổng ra vào. Hỏi bác cần bao nhiêu mét lưới thép?", "Bài giải:\nChu vi khu đất là:\n(18 + 12) x 2 = 60 (m)\nSố mét lưới thép cần là:\n60 - 2 = 58 (m)\nĐáp số: 58 mét", "58 mét", 4, 2.0)
        ]

    # 20 & 21. Các số trong phạm vi 100 000
    elif l_num in [20, 21]:
        v5 = 45000 + t_num * 12500
        return [
            mc(1, f"Số {v5} viết thành chữ là:", [f"Số {v5}", "Không đọc được", "Bốn mươi nghìn", "Năm mươi nghìn"], 0, f"Đúng cách đọc số {v5}."),
            mc(2, f"Số liền sau của số {v5} là:", [str(v5 + 1), str(v5 - 1), str(v5 + 10), str(v5)], 0, f"{v5} + 1 = {v5 + 1}."),
            mc(3, "Số lớn nhất có năm chữ số là:", ["99 999", "100 000", "90 000", "99 990"], 0, "Số 99 999."),
            mc(4, "Số bé nhất có năm chữ số là:", ["10 000", "10 001", "11 111", "00001"], 0, "Số 10 000."),
            mc(5, "Một trăm nghìn viết bằng chữ số là:", ["100 000", "10 000", "1 000 000", "1000"], 0, "100 000 có 5 chữ số 0."),
            mc(6, f"So sánh: {v5} ... {v5 + 500}", ["<", ">", "=", "Không có"], 0, f"{v5} < {v5 + 500}.")
        ], [
            essay(1, f"Viết các số sau:\na) Bốn mươi lăm nghìn hai trăm: .....\nb) Bảy mươi nghìn không trăm linh năm: .....\nc) Tám mươi sáu nghìn chín trăm mười lăm: .....\nd) Một trăm nghìn: .....", "Bài giải:\na) 45 200\nb) 70 005\nc) 86 915\nd) 100 000\nĐáp số: 45 200; 70 005; 86 915; 100 000", "45200, 70005, 86915, 100000", 4, 1.0),
            essay(2, "Sắp xếp các số 54 820, 72 105, 39 999, 54 802, 90 000 theo thứ tự:\na) Từ bé đến lớn\nb) Từ lớn đến bé", "Bài giải:\na) 39 999, 54 802, 54 820, 72 105, 90 000\nb) 90 000, 72 105, 54 820, 54 802, 39 999\nĐáp số: Đúng hai chiều", "39999, 54802, 54820, 72105, 90000", 4, 1.0),
            essay(3, "Viết số thích hợp vào chỗ chấm:\na) Số liền trước của 100 000 là .....\nb) Số liền sau của 89 999 là .....\nc) Số tròn chục nghìn bé nhất là .....", "Bài giải:\na) 99 999\nb) 90 000\nc) 10 000\nĐáp số: 99 999, 90 000, 10 000", "99999, 90000, 10000", 4, 1.0),
            essay(4, "Từ các chữ số 7, 0, 4, 9, 2 hãy viết số lớn nhất có 5 chữ số khác nhau và số bé nhất có 5 chữ số khác nhau.", "Bài giải:\n- Số lớn nhất có 5 chữ số khác nhau: 97 420.\n- Số bé nhất có 5 chữ số khác nhau: 20 479.\nĐáp số: 97 420 và 20 479", "97 420 và 20 479", 5, 1.5),
            essay(5, "Làm tròn các số sau đến hàng nghìn:\na) 45 820\nb) 72 350", "Bài giải:\na) 45 820 làm tròn thành 46 000.\nb) 72 350 làm tròn thành 72 000.\nĐáp số: 46 000 và 72 000", "46 000 và 72 000", 5, 2.0),
            essay(6, "Tìm số có 5 chữ số, biết chữ số hàng chục nghìn là 6, các chữ số còn lại đều bằng nhau và bằng một nửa chữ số hàng chục nghìn.", "Bài giải:\nChữ số hàng chục nghìn là 6.\nCác chữ số nghìn, trăm, chục, đơn vị là: 6 : 2 = 3.\nSố cần tìm là 63 333.\nĐáp số: 63 333", "63 333", 4, 2.0)
        ]

    # 22 & 23. Phép tính trong phạm vi 100 000 (cộng, trừ, nhân, chia)
    elif l_num in [22, 23]:
        return [
            mc(1, "Tính: $35 000 + 24 000 = $", ["59 000", "69 000", "58 000", "60 000"], 0, "$35 000 + 24 000 = 59 000$."),
            mc(2, "Tính: $80 000 - 35 000 = $", ["45 000", "55 000", "40 000", "50 000"], 0, "$80 000 - 35 000 = 45 000$."),
            mc(3, "Đặt tính rồi tính: $12 340 \\times 2 = $", ["24 680", "24 640", "24 860", "26 480"], 0, "$12 340 \\times 2 = 24 680$."),
            mc(4, "Đặt tính rồi tính: $48 640 : 2 = $", ["24 320", "24 220", "23 420", "24 340"], 0, "$48 640 : 2 = 24 320$."),
            mc(5, "Số thích hợp điền vào ô trống: $45 000 + ... = 70 000$", ["25 000", "20 000", "30 000", "35 000"], 0, "$70 000 - 45 000 = 25 000$."),
            mc(6, "Tính: $15 000 \\times 4 = $", ["60 000", "50 000", "70 000", "45 000"], 0, "$15 000 \\times 4 = 60 000$.")
        ], [
            essay(1, "Đặt tính rồi tính:\na) $34 520 + 28 350$\nb) $76 840 - 35 290$\nc) $15 204 \\times 4$\nd) $68 450 : 2$", "Bài giải:\na) 62 870\nb) 41 550\nc) 60 816\nd) 34 225\nĐáp số: 62 870, 41 550, 60 816, 34 225", "62 870, 41 550, 60 816, 34 225", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $45 000 + 12 000 \\times 3 = .....$\nb) $(80 000 - 35 000) : 5 = .....$", "Bài giải:\na) 45 000 + 36 000 = 81 000\nb) 45 000 : 5 = 9 000\nĐáp số: a) 81 000; b) 9 000", "a) 81 000; b) 9 000", 4, 1.0),
            essay(3, "Tìm x biết:\na) $x - 24 500 = 35 200$\nb) $x \\times 3 = 45 960$", "Bài giải:\na) x = 35 200 + 24 500 = 59 700\nb) x = 45 960 : 3 = 15 320\nĐáp số: a) x = 59 700; b) x = 15 320", "a) 59 700; b) 15 320", 4, 1.0),
            essay(4, "Một nông trường có 45 200 cây cam và 28 350 cây bưởi. Hỏi nông trường có tất cả bao nhiêu cây ăn quả?", "Bài giải:\nTổng số cây ăn quả là:\n45 200 + 28 350 = 73 550 (cây)\nĐáp số: 73 550 cây", "73 550 cây", 5, 1.5),
            essay(5, "Một kho gạo có 84 000 kg gạo. Người ta xuất cho các trường bán trú 3 lần, mỗi lần 15 000 kg gạo. Hỏi trong kho còn lại bao nhiêu ki-lô-gam gạo?", "Bài giải:\nTổng số gạo đã xuất là:\n15 000 x 3 = 45 000 (kg)\nTrong kho còn lại số gạo là:\n84 000 - 45 000 = 39 000 (kg)\nĐáp số: 39 000 kg", "39 000 kg", 5, 2.0),
            essay(6, "Một phân xưởng may trong 5 ngày may được 12 500 bộ quần áo. Hỏi trong 8 ngày như thế phân xưởng may được bao nhiêu bộ quần áo?", "Bài giải:\nMỗi ngày phân xưởng may được là:\n12 500 : 5 = 2 500 (bộ)\nTrong 8 ngày may được là:\n2 500 x 8 = 20 000 (bộ)\nĐáp số: 20 000 bộ quần áo", "20 000 bộ", 4, 2.0)
        ]

    # 24. Tiền Việt Nam
    elif l_num == 24:
        return [
            mc(1, "Để đổi tờ 50 000 đồng lấy các tờ 10 000 đồng thì cần:", ["5 tờ", "4 tờ", "6 tờ", "10 tờ"], 0, "$50 000 : 10 000 = 5$ tờ."),
            mc(2, "Mẹ đưa cho em 1 tờ 50 000 đồng và 2 tờ 20 000 đồng. Em có tất cả:", ["90 000 đồng", "70 000 đồng", "80 000 đồng", "100 000 đồng"], 0, "$50 000 + 40 000 = 90 000$ đồng."),
            mc(3, "Một hộp bút giá 35 000 đồng, mua 2 hộp bút hết:", ["70 000 đồng", "60 000 đồng", "80 000 đồng", "65 000 đồng"], 0, "$35 000 \\times 2 = 70 000$ đồng."),
            mc(4, "Bạn Nam mua cuốn sách giá 65 000 đồng, Nam đưa tờ 100 000 đồng. Cô bán hàng trả lại:", ["35 000 đồng", "45 000 đồng", "25 000 đồng", "30 000 đồng"], 0, "$100 000 - 65 000 = 35 000$ đồng."),
            mc(5, "Tờ tiền polymer nào có mệnh giá lớn nhất hiện nay?", ["500 000 đồng", "200 000 đồng", "100 000 đồng", "50 000 đồng"], 0, "500 000 đồng."),
            mc(6, "Đổi 1 tờ 100 000 đồng lấy tờ 20 000 đồng thì được:", ["5 tờ", "10 tờ", "4 tờ", "2 tờ"], 0, "$100 000 : 20 000 = 5$ tờ.")
        ], [
            essay(1, "Tính tổng số tiền:\na) 2 tờ 20 000 đồng + 1 tờ 50 000 đồng = ..... đồng\nb) 3 tờ 10 000 đồng + 2 tờ 5 000 đồng = ..... đồng", "Bài giải:\na) 40 000 + 50 000 = 90 000 đồng\nb) 30 000 + 10 000 = 40 000 đồng\nĐáp số: a) 90 000 đồng; b) 40 000 đồng", "a) 90 000 đồng; b) 40 000 đồng", 4, 1.0),
            essay(2, "Bình mua một chiếc ba lô đi học giá 85 000 đồng. Bình đưa cô bán hàng 1 tờ 100 000 đồng. Hỏi cô bán hàng trả lại Bình bao nhiêu tiền?", "Bài giải:\nCô bán hàng trả lại số tiền là:\n100 000 - 85 000 = 15 000 (đồng)\nĐáp số: 15 000 đồng", "15 000 đồng", 4, 1.0),
            essay(3, "Mẹ mua 3 kg táo, mỗi ki-lô-gam giá 25 000 đồng. Mẹ đưa cô bán hàng tờ 100 000 đồng. Hỏi cô bán hàng phải trả lại mẹ bao nhiêu tiền?", "Bài giải:\n3 kg táo có giá là:\n25 000 x 3 = 75 000 (đồng)\nSố tiền cô bán hàng trả lại là:\n100 000 - 75 000 = 25 000 (đồng)\nĐáp số: 25 000 đồng", "25 000 đồng", 4, 1.0),
            essay(4, "Một chiếc cặp sách giá 65 000 đồng, một hộp sáp màu giá 20 000 đồng. Hỏi mua 1 chiếc cặp sách và 2 hộp sáp màu hết bao nhiêu tiền?", "Bài giải:\n2 hộp sáp màu giá là: 20 000 x 2 = 40 000 (đồng).\nTổng số tiền mua là: 65 000 + 40 000 = 105 000 (đồng).\nĐáp số: 105 000 đồng", "105 000 đồng", 5, 1.5),
            essay(5, "Hà có 4 tờ tiền gồm hai loại mệnh giá 20 000 đồng và 50 000 đồng với tổng số tiền là 110 000 đồng. Hỏi Hà có mấy tờ mỗi loại?", "Bài giải:\nNếu có 3 tờ 20 000đ và 1 tờ 50 000đ: 20 000 x 3 + 50 000 = 110 000 đồng (đúng).\nVậy Hà có 3 tờ 20 000 đồng và 1 tờ 50 000 đồng.\nĐáp số: 3 tờ 20 000đ và 1 tờ 50 000đ", "3 tờ 20k, 1 tờ 50k", 5, 2.0),
            essay(6, "Bác nông dân bán 4 con vịt, mỗi con giá 80 000 đồng. Sau đó bác mua một bao cám giá 150 000 đồng. Hỏi bác còn lại bao nhiêu tiền?", "Bài giải:\nSố tiền bán vịt thu được là:\n80 000 x 4 = 320 000 (đồng)\nBác nông dân còn lại số tiền là:\n320 000 - 150 000 = 170 000 (đồng)\nĐáp số: 170 000 đồng", "170 000 đồng", 4, 2.0)
        ]

    # 25. Thống kê & Xác suất
    elif l_num == 25:
        return [
            mc(1, "Khi tung một đồng xu, khả năng xảy ra là:", ["Có thể xuất hiện mặt sấp hoặc mặt ngửa", "Chắc chắn xuất hiện mặt sấp", "Không bao giờ rơi xuống", "Có 3 mặt"], 0, "Có thể xuất hiện mặt sấp hoặc ngửa."),
            mc(2, "Trong một hộp kín có 5 viên bi đỏ và 5 viên bi xanh. Không nhìn vào hộp, lấy ra 1 viên bi thì:", ["Có thể lấy được bi đỏ hoặc bi xanh", "Chắc chắn là bi đỏ", "Chắc chắn là bi vàng", "Không lấy được bi nào"], 0, "Có thể là bi đỏ hoặc bi xanh."),
            mc(3, "Gieo một con xúc xắc 6 mặt. Sự kiện 'Xuất hiện mặt 7 chấm' là sự kiện:", ["Không thể xảy ra", "Chắc chắn xảy ra", "Có thể xảy ra", "Xảy ra một nửa"], 0, "Con xúc xắc chỉ có từ 1 đến 6 chấm."),
            mc(4, "Gieo một con xúc xắc 6 mặt. Sự kiện 'Xuất hiện mặt có số chấm bé hơn 7' là sự kiện:", ["Chắc chắn xảy ra", "Không thể xảy ra", "Có thể xảy ra", "Chưa biết"], 0, "Mọi mặt đều từ 1 đến 6 nên bé hơn 7."),
            mc(5, "Bảng thống kê điểm kiểm tra Toán của tổ có: 5 điểm 10, 4 điểm 9, 1 điểm 8. Tổng số học sinh của tổ là:", ["10 học sinh", "9 học sinh", "8 học sinh", "11 học sinh"], 0, "$5 + 4 + 1 = 10$ học sinh."),
            mc(6, "Điểm kiểm tra phổ biến nhất của tổ trên là:", ["Điểm 10", "Điểm 9", "Điểm 8", "Điểm 7"], 0, "Điểm 10 có 5 bạn (nhiều nhất).")
        ], [
            essay(1, "Bảng theo dõi số giờ đọc sách trong tuần của bạn An:\n- Thứ Hai: 1 giờ\n- Thứ Ba: 2 giờ\n- Thứ Tư: 1 giờ\n- Thứ Năm: 2 giờ\n- Thứ Sáu: 1 giờ\n- Thứ Bảy: 3 giờ\n- Chủ Nhật: 3 giờ\na) Ngày nào bạn An đọc sách nhiều nhất?\nb) Cả tuần bạn An đọc sách tất cả bao nhiêu giờ?", "Bài giải:\na) Thứ Bảy và Chủ Nhật đọc nhiều nhất (3 giờ mỗi ngày).\nb) Cả tuần đọc số giờ là:\n1 + 2 + 1 + 2 + 1 + 3 + 3 = 13 (giờ)\nĐáp số: a) Thứ Bảy và Chủ Nhật; b) 13 giờ", "a) Thứ 7, CN; b) 13 giờ", 4, 1.0),
            essay(2, "Điền từ thích hợp (Chắc chắn, Có thể, Không thể):\na) Mặt trời mọc ở hướng Đông là sự kiện ...............\nb) Một con gà đẻ ra quả trứng vàng là sự kiện ...............\nc) Ngày mai trời mưa là sự kiện ...............", "Bài giải:\na) Chắc chắn\nb) Không thể\nc) Có thể\nĐáp số: a) Chắc chắn; b) Không thể; c) Có thể", "Chắc chắn, Không thể, Có thể", 4, 1.0),
            essay(3, "Trong túi có 6 chiếc bút chì màu xanh và không có chiếc bút màu đỏ nào. Không nhìn vào túi, thò tay lấy ra 1 chiếc bút. Hỏi sự kiện 'Lấy được chiếc bút chì màu đỏ' có thể xảy ra không? Vì sao?", "Bài giải:\nSự kiện này không thể xảy ra vì trong túi hoàn toàn không có chiếc bút chì màu đỏ nào.\nĐáp số: Không thể xảy ra", "Không thể xảy ra", 4, 1.0),
            essay(4, "Thống kê số cây trồng được của 4 tổ trong đợt Tết trồng cây:\n- Tổ 1: 35 cây\n- Tổ 2: 40 cây\n- Tổ 3: 38 cây\n- Tổ 4: 42 cây\na) Tổ nào trồng được nhiều cây nhất?\nb) Cả 4 tổ trồng được tất cả bao nhiêu cây?", "Bài giải:\na) Tổ 4 trồng được nhiều cây nhất (42 cây).\nb) Cả 4 tổ trồng được số cây là:\n35 + 40 + 38 + 42 = 155 (cây)\nĐáp số: a) Tổ 4; b) 155 cây", "a) Tổ 4; b) 155 cây", 5, 1.5),
            essay(5, "Bạn Minh gieo một đồng xu 20 lần và ghi lại kết quả: có 12 lần xuất hiện mặt sấp. Hỏi có bao nhiêu lần xuất hiện mặt ngửa?", "Bài giải:\nSố lần xuất hiện mặt ngửa là:\n20 - 12 = 8 (lần)\nĐáp số: 8 lần", "8 lần", 5, 2.0),
            essay(6, "Trong một hộp kín có 3 viên bi đỏ, 2 viên bi xanh và 1 viên bi vàng. Lấy ngẫu nhiên ra 1 viên bi. Nêu tất cả các khả năng về màu sắc của viên bi lấy ra.", "Bài giải:\nCác khả năng có thể xảy ra là:\n- Lấy được viên bi màu đỏ\n- Lấy được viên bi màu xanh\n- Lấy được viên bi màu vàng\nĐáp số: 3 khả năng: đỏ, xanh hoặc vàng", "Đỏ, xanh hoặc vàng", 4, 2.0)
        ]

    # 26 & 27. Ôn tập cuối năm
    else:
        return [
            mc(1, "Tính: $25 000 + 35 000 = $", ["60 000", "50 000", "70 000", "55 000"], 0, "$25 000 + 35 000 = 60 000$."),
            mc(2, "Tính: $14 000 \\times 3 = $", ["42 000", "32 000", "52 000", "45 000"], 0, "$14 000 \\times 3 = 42 000$."),
            mc(3, "Một hình vuông có chu vi 48 cm thì diện tích là:", ["144 cm²", "96 cm²", "64 cm²", "100 cm²"], 0, "Cạnh = $48 : 4 = 12$ cm. Diện tích = $12 \\times 12 = 144$ cm²."),
            mc(4, "Đổi: $3\\text{ m } 5\\text{ cm} = ...\\text{ cm}$", ["305 cm", "350 cm", "35 cm", "3005 cm"], 0, "$300 + 5 = 305$ cm."),
            mc(5, "Số liền sau của 99 999 là:", ["100 000", "99 998", "100 001", "90 000"], 0, "$99 999 + 1 = 100 000$."),
            mc(6, "Tính: $84 000 : 4 = $", ["21 000", "22 000", "20 000", "24 000"], 0, "$84 000 : 4 = 21 000$.")
        ], [
            essay(1, "Đặt tính rồi tính:\na) $45 280 + 38 450$\nb) $92 340 - 45 680$\nc) $14 250 \\times 4$\nd) $84 640 : 2$", "Bài giải:\na) 83 730\nb) 46 660\nc) 57 000\nd) 42 320\nĐáp số: 83 730, 46 660, 57 000, 42 320", "83730, 46660, 57000, 42320", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $35 000 + 15 000 \\times 3 = .....$\nb) $(75 000 - 25 000) : 5 = .....$", "Bài giải:\na) 35 000 + 45 000 = 80 000\nb) 50 000 : 5 = 10 000\nĐáp số: a) 80 000; b) 10 000", "a) 80 000; b) 10 000", 4, 1.0),
            essay(3, "Một mảnh vườn hình chữ nhật có chiều dài 32 m, chiều rộng bằng 1/4 chiều dài. Tính chu vi và diện tích mảnh vườn đó.", "Bài giải:\nChiều rộng mảnh vườn là:\n32 : 4 = 8 (m)\nChu vi mảnh vườn là:\n(32 + 8) x 2 = 80 (m)\nDiện tích mảnh vườn là:\n32 x 8 = 256 (m²)\nĐáp số: Chu vi: 80 m; Diện tích: 256 m²", "P = 80 m; S = 256 m²", 4, 1.0),
            essay(4, "Một cửa hàng có 45 000 kg xi măng. Ngày thứ nhất bán được 18 000 kg, ngày thứ hai bán được 12 500 kg. Hỏi sau hai ngày cửa hàng còn lại bao nhiêu ki-lô-gam xi măng?", "Bài giải:\nTổng số xi măng đã bán sau hai ngày là:\n18 000 + 12 500 = 30 500 (kg)\nCửa hàng còn lại số xi măng là:\n45 000 - 30 500 = 14 500 (kg)\nĐáp số: 14 500 kg", "14 500 kg", 5, 1.5),
            essay(5, "Một hình vuông có chu vi 36 cm. Một hình chữ nhật có cùng chu vi với hình vuông và có chiều dài 11 cm. Tính diện tích hình chữ nhật đó.", "Bài giải:\nNửa chu vi hình chữ nhật là: 36 : 2 = 18 (cm).\nChiều rộng hình chữ nhật là: 18 - 11 = 7 (cm).\nDiện tích hình chữ nhật là: 11 x 7 = 77 (cm²).\nĐáp số: 77 cm²", "77 cm²", 5, 2.0),
            essay(6, "Tìm số lớn nhất có 5 chữ số khác nhau có chữ số hàng nghìn là 8 và chữ số hàng chục là 5.", "Bài giải:\nĐể số lớn nhất có 5 chữ số khác nhau thì:\n- Chữ số hàng chục nghìn lớn nhất là 9.\n- Chữ số hàng nghìn là 8 (theo đề bài).\n- Chữ số hàng trăm lớn nhất còn lại là 7.\n- Chữ số hàng chục là 5 (theo đề bài).\n- Chữ số hàng đơn vị lớn nhất còn lại là 6.\nVậy số cần tìm là: 98 756.\nĐáp số: 98 756", "98 756", 4, 2.0)
        ]

def get_toan3_lesson_exams():
    exams = {}
    from toan3_curriculum_def import TOAN3_CURRICULUM
    ch_map = {}
    for ch in TOAN3_CURRICULUM["chapters"]:
        for les in ch["lessons"]:
            ch_map[les["num"]] = (ch["title"], ch["term"], les["name"])

    for l_num in range(1, 28):
        ch_title, term_code, les_name = ch_map.get(l_num, ("Chủ đề bài học", "hk1", f"Bài {l_num}"))
        for t_idx in range(1, 4):
            eid = f"th3_b{l_num}_test{t_idx}"
            p1, p2 = build_toan3_lesson(l_num, t_idx)
            exams[eid] = {
                "id": eid, "lessonId": f"th3_b{l_num}", "lessonNum": l_num, "testNum": t_idx,
                "title": f"{les_name} - Đề số {t_idx}",
                "topic": ch_title, "chapter": ch_title.split(":")[0],
                "grade": "3", "term": term_code, "duration": "40 phút", "points": 10.0,
                "part1": p1,
                "part2": p2
            }

    print(f"-> Đã tạo thành công {len(exams)} đề kiểm tra theo bài cho TOÁN 3 (27 bài x 3 đề = 81 đề)")
    return exams

if __name__ == "__main__":
    exs = get_toan3_lesson_exams()
    print("Mẫu đề th3_b1_test1:", exs["th3_b1_test1"]["title"])
    print("P1 len:", len(exs["th3_b1_test1"]["part1"]), "P2 len:", len(exs["th3_b1_test1"]["part2"]))
