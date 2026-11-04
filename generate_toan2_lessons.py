# -*- coding: utf-8 -*-
"""
HỆ THỐNG SINH ĐỀ KIỂM TRA THEO BÀI CHO TOÁN 2 (KNTT)
Gồm 32 bài học, mỗi bài có 3 đề kiểm tra độc lập (Đề 1, Đề 2, Đề 3).
Tổng cộng: 96 đề kiểm tra.
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

def build_toan2_lesson(l_num, t_num):
    """Sinh bộ 6 trắc nghiệm + 6 tự luận chuyên biệt theo từng bài Toán 2"""
    # 1. Ôn tập các số đến 100
    if l_num == 1:
        s_val = 60 + t_num * 8
        return [
            mc(1, f"Số gồm {s_val // 10} chục và {s_val % 10} đơn vị viết là:", [str(s_val), str(s_val+1), str(s_val-10), str(s_val*10)], 0, f"Viết là {s_val}."),
            mc(2, f"Số liền trước của {s_val} là:", [str(s_val - 1), str(s_val + 1), str(s_val - 10), str(s_val)], 0, f"{s_val} - 1 = {s_val - 1}."),
            mc(3, f"Số liền sau của {s_val} là:", [str(s_val + 1), str(s_val - 1), str(s_val + 10), str(s_val)], 0, f"{s_val} + 1 = {s_val + 1}."),
            mc(4, "Số lớn nhất có hai chữ số là:", ["99", "100", "90", "98"], 0, "Số 99."),
            mc(5, "Số bé nhất có hai chữ số là:", ["10", "01", "11", "00"], 0, "Số 10."),
            mc(6, f"Điền dấu: {s_val} ... {s_val + 5}", ["<", ">", "=", "Không có"], 0, f"{s_val} < {s_val + 5}.")
        ], [
            essay(1, f"Viết số thích hợp vào chỗ chấm:\na) Số {s_val} gồm ..... chục và ..... đơn vị\nb) Số liền trước của 80 là .....\nc) Số liền sau của 99 là .....\nd) Các số tròn chục từ 50 đến 90 là: .....", f"Bài giải:\na) {s_val // 10} chục và {s_val % 10} đơn vị\nb) 79\nc) 100\nd) 50, 60, 70, 80, 90\nĐáp số: Đúng các ý", f"{s_val // 10} chục, {s_val % 10} đơn vị; 79; 100; 50, 60, 70, 80, 90", 4, 1.0),
            essay(2, "Sắp xếp các số 45, 89, 23, 76, 54 theo thứ tự:\na) Từ bé đến lớn\nb) Từ lớn đến bé", "Bài giải:\na) Từ bé đến lớn: 23, 45, 54, 76, 89\nb) Từ lớn đến bé: 89, 76, 54, 45, 23\nĐáp số: a) 23, 45, 54, 76, 89; b) 89, 76, 54, 45, 23", "a) 23, 45, 54, 76, 89; b) 89, 76, 54, 45, 23", 4, 1.0),
            essay(3, "Từ các chữ số 3, 7, 0 hãy viết tất cả các số có hai chữ số khác nhau.", "Bài giải:\nCác số có hai chữ số khác nhau ghép từ 3, 7, 0 là: 30, 37, 70, 73.\nĐáp số: 30, 37, 70, 73", "30, 37, 70, 73", 4, 1.0),
            essay(4, "Một giá sách có hai ngăn. Ngăn trên có 45 quyển sách, ngăn dưới có 52 quyển sách. Hỏi cả hai ngăn có tất cả bao nhiêu quyển sách?", "Bài giải:\nCả hai ngăn có tất cả số quyển sách là:\n45 + 52 = 97 (quyển sách)\nĐáp số: 97 quyển sách", "97 quyển sách", 5, 1.5),
            essay(5, "Đoàn tàu có 88 hành khách, đến ga có 25 hành khách xuống tàu. Hỏi trên đoàn tàu lúc đó còn lại bao nhiêu hành khách?", "Bài giải:\nTrên đoàn tàu còn lại số hành khách là:\n88 - 25 = 63 (hành khách)\nĐáp số: 63 hành khách", "63 hành khách", 5, 2.0),
            essay(6, "Tìm số có hai chữ số, biết tổng hai chữ số bằng 11 và chữ số hàng chục hơn chữ số hàng đơn vị là 3.", "Bài giải:\nTa có: 7 + 4 = 11 và 7 - 4 = 3.\nVậy chữ số hàng chục là 7, chữ số hàng đơn vị là 4.\nSố cần tìm là 74.\nĐáp số: 74", "74", 4, 2.0)
        ]

    # 2. Tia số. Số liền trước, số liền sau
    elif l_num == 2:
        val = 20 + t_num * 10
        return [
            mc(1, f"Trên tia số, điểm đứng ngay trước số {val} là điểm chỉ số:", [str(val - 1), str(val + 1), str(val - 2), str(val)], 0, f"Đó là số liền trước: {val - 1}."),
            mc(2, f"Trên tia số, gốc tia số là điểm chỉ số:", ["0", "1", "10", "Không có"], 0, "Gốc của tia số là điểm 0."),
            mc(3, f"Số liền trước của 1 là:", ["0", "2", "Không có", "10"], 0, "$1 - 1 = 0$."),
            mc(4, f"Số liền sau của 99 là:", ["100", "98", "101", "90"], 0, "$99 + 1 = 100$."),
            mc(5, f"Số nào vừa là số liền sau của 45 vừa là số liền trước của 47?", ["46", "44", "48", "45"], 0, "Đó là số 46."),
            mc(6, "Trên tia số, số càng ở bên phải thì:", ["Càng lớn", "Càng bé", "Không đổi", "Bằng nhau"], 0, "Các số trên tia số tăng dần từ trái sang phải.")
        ], [
            essay(1, f"Viết số thích hợp vào chỗ chấm trên tia số:\na) Số liền trước của {val} là .....; số liền sau của {val} là .....\nb) Số liền trước của 75 là .....; số liền sau của 75 là .....", f"Bài giải:\na) {val - 1} và {val + 1}\nb) 74 và 76\nĐáp số: a) {val - 1}, {val + 1}; b) 74, 76", f"{val - 1}, {val + 1}; 74, 76", 4, 1.0),
            essay(2, "Vẽ một đoạn tia số từ số 15 đến số 22 và đánh dấu vị trí các số chẵn.", "Bài giải:\nHọc sinh kẻ tia số và điền: 15, 16, 17, 18, 19, 20, 21, 22.\nCác số chẵn được khoanh tròn là: 16, 18, 20, 22.\nĐáp số: Đầy đủ tia số và số chẵn", "Tia số 15-22, đánh dấu 16, 18, 20, 22", 4, 1.0),
            essay(3, "Tìm ba số liên tiếp biết số ở giữa là 50.", "Bài giải:\nSố liền trước của 50 là 49.\nSố liền sau của 50 là 51.\nBa số liên tiếp là: 49, 50, 51.\nĐáp số: 49, 50, 51", "49, 50, 51", 4, 1.0),
            essay(4, "Một bạn viết một dãy số cách đều 5 đơn vị trên tia số bắt đầu từ 0: 0, 5, 10, 15, ... Hỏi số thứ 6 trong dãy là số nào?", "Bài giải:\nDãy số: 0 (thứ 1), 5 (thứ 2), 10 (thứ 3), 15 (thứ 4), 20 (thứ 5), 25 (thứ 6).\nSố thứ 6 là số 25.\nĐáp số: 25", "25", 5, 1.5),
            essay(5, "Biết số a là số liền trước của 40, số b là số liền sau của 50. Tính tổng của a và b.", "Bài giải:\nSố liền trước của 40 là a = 39.\nSố liền sau của 50 là b = 51.\nTổng của a và b là: 39 + 51 = 90.\nĐáp số: 90", "90", 5, 2.0),
            essay(6, "Tìm số liền sau của số lớn nhất có hai chữ số khác nhau.", "Bài giải:\nSố lớn nhất có hai chữ số khác nhau là 98.\nSố liền sau của 98 là: 98 + 1 = 99.\nĐáp số: 99", "99", 4, 2.0)
        ]

    # 3. Thành phần phép cộng, phép trừ
    elif l_num == 3:
        a_val = 32 + t_num * 4
        b_val = 15 + t_num * 2
        return [
            mc(1, f"Trong phép tính ${a_val} + {b_val} = {a_val + b_val}$, {a_val + b_val} được gọi là:", ["Tổng", "Số hạng", "Số bị trừ", "Hiệu"], 0, "Kết quả phép cộng là tổng."),
            mc(2, f"Trong phép tính ${a_val + b_val} - {b_val} = {a_val}$, {a_val + b_val} được gọi là:", ["Số bị trừ", "Số trừ", "Hiệu", "Tổng"], 0, "Số đứng trước dấu trừ là số bị trừ."),
            mc(3, f"Trong phép tính ${a_val + b_val} - {b_val} = {a_val}$, {b_val} được gọi là:", ["Số trừ", "Số bị trừ", "Hiệu", "Số hạng"], 0, "Số đứng sau dấu trừ là số trừ."),
            mc(4, "Biết hai số hạng là 24 và 35. Tổng là:", ["59", "69", "49", "58"], 0, "24 + 35 = 59."),
            mc(5, "Biết số bị trừ là 78, số trừ là 30. Hiệu là:", ["48", "38", "58", "40"], 0, "78 - 30 = 48."),
            mc(6, "Muốn tìm số hạng chưa biết khi biết tổng và số hạng kia, ta lấy:", ["Tổng trừ đi số hạng đã biết", "Tổng cộng số hạng đã biết", "Số hạng trừ tổng", "Hai số nhân nhau"], 0, "Quy tắc tìm số hạng chưa biết.")
        ], [
            essay(1, f"Viết tên gọi thành phần của mỗi số trong phép tính:\na) ${a_val} + {b_val} = {a_val + b_val}$\nb) ${a_val + b_val} - {b_val} = {a_val}$", f"Bài giải:\na) {a_val}: số hạng; {b_val}: số hạng; {a_val + b_val}: tổng.\nb) {a_val + b_val}: số bị trừ; {b_val}: số trừ; {a_val}: hiệu.\nĐáp số: Ghi đúng tên các thành phần", "Nêu đúng tên các thành phần", 4, 1.0),
            essay(2, "Tìm x biết:\na) $x + 25 = 68$\nb) $x - 30 = 42$\nc) $79 - x = 45$", "Bài giải:\na) x = 68 - 25 = 43\nb) x = 42 + 30 = 72\nc) x = 79 - 45 = 34\nĐáp số: a) x = 43; b) x = 72; c) x = 34", "a) 43; b) 72; c) 34", 4, 1.0),
            essay(3, "Tính tổng biết hai số hạng là 46 và 33. Tính hiệu biết số bị trừ là 87 và số trừ là 52.", "Bài giải:\n- Tổng là: 46 + 33 = 79.\n- Hiệu là: 87 - 52 = 35.\nĐáp số: Tổng là 79; Hiệu là 35", "Tổng 79; Hiệu 35", 4, 1.0),
            essay(4, "Một người có một bao gạo. Sau khi bán đi 24 kg thì trong bao còn lại 35 kg. Hỏi ban đầu bao gạo có bao nhiêu ki-lô-gam gạo?", "Bài giải:\nBan đầu bao gạo có số ki-lô-gam là:\n35 + 24 = 59 (kg)\nĐáp số: 59 kg", "59 kg", 5, 1.5),
            essay(5, "Tổng của hai số là 86. Nếu giữ nguyên một số hạng và thêm vào số hạng kia 5 đơn vị thì tổng mới là bao nhiêu?", "Bài giải:\nKhi thêm vào một số hạng 5 đơn vị thì tổng cũng tăng thêm 5 đơn vị.\nTổng mới là:\n86 + 5 = 91\nĐáp số: 91", "91", 5, 2.0),
            essay(6, "Hiệu của hai số là 40. Nếu bớt ở số bị trừ 6 đơn vị và giữ nguyên số trừ thì hiệu mới là bao nhiêu?", "Bài giải:\nKhi bớt ở số bị trừ 6 đơn vị thì hiệu giảm đi 6 đơn vị.\nHiệu mới là:\n40 - 6 = 34\nĐáp số: 34", "34", 4, 2.0)
        ]

    # 4 & 5 & 6. Bảng cộng, trừ qua 10 phạm vi 20
    elif l_num in [4, 5, 6]:
        n_a = 9 if l_num == 4 else 14
        n_b = 6 + t_num
        ans = (n_a + n_b) if l_num == 4 else (n_a - n_b)
        return [
            mc(1, f"Kết quả của phép tính ${n_a} {'+' if l_num == 4 else '-'} {n_b}$ là:", [str(ans), str(ans+1), str(ans-1), "20"], 0, f"Tính nhẩm qua 10: kết quả là {ans}."),
            mc(2, "Tính: $9 + 5 = $", ["14", "13", "15", "16"], 0, "$9 + 1 + 4 = 14$."),
            mc(3, "Tính: $8 + 7 = $", ["15", "14", "16", "17"], 0, "$8 + 2 + 5 = 15$."),
            mc(4, "Tính: $13 - 6 = $", ["7", "8", "6", "9"], 0, "$13 - 3 - 3 = 7$."),
            mc(5, "Tính: $16 - 8 = $", ["8", "7", "9", "6"], 0, "$16 - 6 - 2 = 8$."),
            mc(6, "Số thích hợp điền vào dấu chấm: $8 + ... = 15$", ["7", "6", "8", "9"], 0, "$15 - 8 = 7$.")
        ], [
            essay(1, "Tính nhẩm:\na) $9 + 4 = .....$\nb) $8 + 6 = .....$\nc) $12 - 5 = .....$\nd) $15 - 7 = .....$", "Bài giải:\na) 13\nb) 14\nc) 7\nd) 8\nĐáp số: 13, 14, 7, 8", "13, 14, 7, 8", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $9 + 6 - 7 = .....$\nb) $14 - 8 + 5 = .....$\nc) $8 + 8 - 9 = .....$", "Bài giải:\na) 15 - 7 = 8\nb) 6 + 5 = 11\nc) 16 - 9 = 7\nĐáp số: a) 8; b) 11; c) 7", "a) 8; b) 11; c) 7", 4, 1.0),
            essay(3, "Điền dấu (>, <, =):\na) $9 + 5 ... 13$\nb) $8 + 7 ... 7 + 8$\nc) $16 - 9 ... 15 - 7$", "Bài giải:\na) 14 > 13\nb) 15 = 15\nc) 7 < 8\nĐáp số: a) >; b) =; c) <", "a) >; b) =; c) <", 4, 1.0),
            essay(4, "Hà có 8 bông hoa, Lan có nhiều hơn Hà 5 bông hoa. Hỏi Lan có bao nhiêu bông hoa?", "Bài giải:\nLan có số bông hoa là:\n8 + 5 = 13 (bông hoa)\nĐáp số: 13 bông hoa", "13 bông hoa", 5, 1.5),
            essay(5, "Trên cành cây có 14 con chim đang hót, sau đó có 6 con chim bay đi. Hỏi trên cành cây còn lại bao nhiêu con chim?", "Bài giải:\nTrên cành cây còn lại số con chim là:\n14 - 6 = 8 (con chim)\nĐáp số: 8 con chim", "8 con chim", 5, 2.0),
            essay(6, "Tìm một số biết rằng lấy số đó cộng với 7 thì được kết quả là 16.", "Bài giải:\nSố cần tìm là:\n16 - 7 = 9\nĐáp số: 9", "9", 4, 2.0)
        ]

    # 7 & 8. Ki-lô-gam (kg), Lít (l)
    elif l_num in [7, 8]:
        unit = "kg" if l_num == 7 else "l"
        u_name = "ki-lô-gam" if l_num == 7 else "lít"
        k_val = 15 + t_num * 5
        return [
            mc(1, f"Tên viết tắt của đơn vị {u_name} là:", [unit, "m", "cm", "g"], 0, f"Ký hiệu là {unit}."),
            mc(2, f"Tính: ${k_val}\\text{{ {unit}}} + 8\\text{{ {unit}}} = $", [f"{k_val + 8} {unit}", f"{k_val + 8}", "20", "25"], 0, f"{k_val} + 8 = {k_val + 8} {unit}."),
            mc(3, f"Tính: $35\\text{{ {unit}}} - 15\\text{{ {unit}}} = $", [f"20 {unit}", "15", "25", "10"], 0, f"35 - 15 = 20 {unit}."),
            mc(4, f"Cân nặng của một học sinh lớp 2 khoảng bao nhiêu?", ["25 kg", "25 g", "2 kg", "250 kg"], 0, "Khoảng 25 kg."),
            mc(5, f"Can nước to đựng được 10 l, can nhỏ đựng được 3 l. Cả hai can đựng được:", ["13 l", "7 l", "10 l", "15 l"], 0, "10 + 3 = 13 l."),
            mc(6, f"So sánh: $18\\text{{ {unit}}} ... 20\\text{{ {unit}}}$", ["<", ">", "=", "Không có"], 0, f"18 < 20.")
        ], [
            essay(1, f"Tính:\na) $25\\text{{ {unit}}} + 14\\text{{ {unit}}} = .....$\nb) $48\\text{{ {unit}}} - 23\\text{{ {unit}}} = .....$\nc) $12\\text{{ {unit}}} + 8\\text{{ {unit}}} - 5\\text{{ {unit}}} = .....$", f"Bài giải:\na) 39 {unit}\nb) 25 {unit}\nc) 15 {unit}\nĐáp số: 39 {unit}, 25 {unit}, 15 {unit}", f"39 {unit}, 25 {unit}, 15 {unit}", 4, 1.0),
            essay(2, "Điền dấu thích hợp (>, <, =):\na) $15\\text{ kg} + 5\\text{ kg} ... 22\\text{ kg}$\nb) $30\\text{ l} - 10\\text{ l} ... 20\\text{ l}$", "Bài giải:\na) 20 kg < 22 kg\nb) 20 l = 20 l\nĐáp số: a) <; b) =", "a) <; b) =", 4, 1.0),
            essay(3, "Bao gạo to cân nặng 35 kg, bao gạo bé cân nặng 20 kg. Hỏi cả hai bao gạo cân nặng bao nhiêu ki-lô-gam?", "Bài giải:\nCả hai bao gạo cân nặng là:\n35 + 20 = 55 (kg)\nĐáp số: 55 kg", "55 kg", 4, 1.0),
            essay(4, "Một thùng đựng 45 lít dầu, người ta đã rót ra 18 lít dầu. Hỏi trong thùng còn lại bao nhiêu lít dầu?", "Bài giải:\nTrong thùng còn lại số lít dầu là:\n45 - 18 = 27 (lít)\nĐáp số: 27 lít dầu", "27 lít", 5, 1.5),
            essay(5, "Một xô nước đựng 12 lít nước, một can nước đựng 5 lít nước. Hỏi xô nước đựng nhiều hơn can nước bao nhiêu lít?", "Bài giải:\nXô nước đựng nhiều hơn can nước số lít là:\n12 - 5 = 7 (lít)\nĐáp số: 7 lít", "7 lít", 5, 2.0),
            essay(6, "Có 3 quả dưa hấu: quả thứ nhất nặng 3 kg, quả thứ hai nặng 4 kg, quả thứ ba nặng 5 kg. Hỏi cả ba quả dưa hấu nặng tất cả bao nhiêu ki-lô-gam?", "Bài giải:\nCả ba quả nặng số ki-lô-gam là:\n3 + 4 + 5 = 12 (kg)\nĐáp số: 12 kg", "12 kg", 4, 2.0)
        ]

    # 9 & 10. Phép cộng, trừ có nhớ trong phạm vi 100
    elif l_num in [9, 10]:
        c_a = 48 + t_num * 3
        c_b = 25 + t_num * 2
        return [
            mc(1, f"Đặt tính rồi tính: ${c_a} + {c_b} = $", [str(c_a + c_b), str(c_a + c_b - 1), str(c_a + c_b + 10), "80"], 0, f"Cộng có nhớ: {c_a} + {c_b} = {c_a + c_b}."),
            mc(2, f"Đặt tính rồi tính: ${c_a + 20} - {c_b} = $", [str(c_a + 20 - c_b), str(c_a + 20 - c_b + 1), str(c_a - c_b), "30"], 0, f"Trừ có nhớ: kết quả là {c_a + 20 - c_b}."),
            mc(3, "Phép tính nào có kết quả bằng 60?", ["$35 + 25$", "$38 + 24$", "$45 + 16$", "$50 + 12$"], 0, "$35 + 25 = 60$."),
            mc(4, "Số thích hợp điền vào ô trống: $47 + ... = 72$", ["25", "24", "26", "35"], 0, "$72 - 47 = 25$."),
            mc(5, "Số thích hợp điền vào ô trống: $... - 28 = 36$", ["64", "54", "74", "62"], 0, "$36 + 28 = 64$."),
            mc(6, "Tìm hiệu của số lớn nhất có hai chữ số và số 35:", ["64", "54", "65", "63"], 0, "$99 - 35 = 64$.")
        ], [
            essay(1, "Đặt tính rồi tính:\na) $37 + 25$\nb) $58 + 36$\nc) $72 - 38$\nd) $61 - 27$", "Bài giải:\na) 62\nb) 94\nc) 34\nd) 34\nĐáp số: 62, 94, 34, 34", "62, 94, 34, 34", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $46 + 28 - 35 = .....$\nb) $83 - 47 + 19 = .....$", "Bài giải:\na) 46 + 28 = 74; 74 - 35 = 39\nb) 83 - 47 = 36; 36 + 19 = 55\nĐáp số: a) 39; b) 55", "a) 39; b) 55", 4, 1.0),
            essay(3, "Tìm x biết:\na) $x - 36 = 28$\nb) $54 + x = 82$", "Bài giải:\na) x = 28 + 36 = 64\nb) x = 82 - 54 = 28\nĐáp số: a) x = 64; b) x = 28", "a) 64; b) 28", 4, 1.0),
            essay(4, "Một trường tiểu học có 48 học sinh giỏi khối 1 và 45 học sinh giỏi khối 2. Hỏi cả hai khối có tất cả bao nhiêu học sinh giỏi?", "Bài giải:\nCả hai khối có tất cả số học sinh giỏi là:\n48 + 45 = 93 (học sinh)\nĐáp số: 93 học sinh", "93 học sinh", 5, 1.5),
            essay(5, "Bác thợ may có một khúc vải dài 82 mét, bác đã may quần áo hết 47 mét. Hỏi khúc vải còn lại dài bao nhiêu mét?", "Bài giải:\nKhúc vải còn lại dài số mét là:\n82 - 47 = 35 (mét)\nĐáp số: 35 mét", "35 mét", 5, 2.0),
            essay(6, "Tổng của hai số là 75. Nếu số hạng thứ nhất tăng thêm 18 đơn vị và số hạng thứ hai giảm đi 9 đơn vị thì tổng mới là bao nhiêu?", "Bài giải:\nTổng mới là:\n75 + 18 - 9 = 84\nĐáp số: 84", "84", 4, 2.0)
        ]

    # 11, 12, 13. Hình học: Điểm, đoạn thẳng, đường cong, đường gấp khúc, 3 điểm thẳng hàng
    elif l_num in [11, 12, 13]:
        return [
            mc(1, "Hình gồm các đoạn thẳng nối tiếp nhau không thẳng hàng gọi là:", ["Đường gấp khúc", "Đoạn thẳng", "Đường cong", "Tia số"], 0, "Khái niệm đường gấp khúc."),
            mc(2, "Độ dài đường gấp khúc gồm 2 đoạn thẳng dài 8 cm và 12 cm là:", ["20 cm", "22 cm", "18 cm", "16 cm"], 0, "8 + 12 = 20 cm."),
            mc(3, "Ba điểm cùng nằm trên một đường thẳng được gọi là:", ["Ba điểm thẳng hàng", "Ba điểm cắt nhau", "Tam giác", "Đoạn thẳng"], 0, "Khái niệm ba điểm thẳng hàng."),
            mc(4, "Đoạn thẳng AB được giới hạn bởi mấy điểm?", ["2 điểm (điểm A và điểm B)", "1 điểm", "3 điểm", "Vô số điểm"], 0, "Giới hạn bởi 2 đầu mút."),
            mc(5, "Độ dài đường gấp khúc ABCD gồm các đoạn AB = 4 cm, BC = 5 cm, CD = 6 cm là:", ["15 cm", "14 cm", "16 cm", "13 cm"], 0, "4 + 5 + 6 = 15 cm."),
            mc(6, "Cây cầu vồng trên bầu trời có dạng đường gì?", ["Đường cong", "Đoạn thẳng", "Đường thẳng", "Đường gấp khúc"], 0, "Có dạng đường cong.")
        ], [
            essay(1, "Tính độ dài đường gấp khúc MNPQ biết:\nMN = 15 cm, NP = 12 cm, PQ = 18 cm.", "Bài giải:\nĐộ dài đường gấp khúc MNPQ là:\n15 + 12 + 18 = 45 (cm)\nĐáp số: 45 cm", "45 cm", 4, 1.0),
            essay(2, "Cho ba điểm A, B, C thẳng hàng theo thứ tự đó. Biết AB = 8 cm, BC = 6 cm. Tính độ dài đoạn thẳng AC.", "Bài giải:\nĐộ dài đoạn thẳng AC là:\n8 + 6 = 14 (cm)\nĐáp số: 14 cm", "14 cm", 4, 1.0),
            essay(3, "Một đường gấp khúc gồm 4 đoạn thẳng có độ dài đều bằng 5 cm. Tính độ dài đường gấp khúc đó.", "Bài giải:\nĐộ dài đường gấp khúc đó là:\n5 + 5 + 5 + 5 = 20 (cm)\nĐáp số: 20 cm", "20 cm", 4, 1.0),
            essay(4, "Vẽ đoạn thẳng AB dài 7 cm và tìm điểm I trên đoạn AB sao cho AI = 3 cm. Hỏi đoạn IB dài mấy xăng-ti-mét?", "Bài giải:\nĐộ dài đoạn thẳng IB là:\n7 - 3 = 4 (cm)\nĐáp số: 4 cm", "4 cm", 5, 1.5),
            essay(5, "Cho 4 điểm A, B, C, D không có 3 điểm nào thẳng hàng. Nối từng cặp điểm ta vẽ được tất cả bao nhiêu đoạn thẳng?", "Bài giải:\nCác đoạn thẳng vẽ được là: AB, AC, AD, BC, BD, CD.\nCó tất cả 6 đoạn thẳng.\nĐáp số: 6 đoạn thẳng", "6 đoạn thẳng", 5, 2.0),
            essay(6, "Một con kiến bò từ điểm A đến điểm B hết 12 cm, rồi bò tiếp từ B đến C hết 15 cm. Hỏi con kiến đã bò quãng đường dài bao nhiêu xăng-ti-mét?", "Bài giải:\nQuãng đường con kiến đã bò là:\n12 + 15 = 27 (cm)\nĐáp số: 27 cm", "27 cm", 4, 2.0)
        ]

    # 14, 15, 16. Thời gian & Ôn tập học kì 1
    elif l_num in [14, 15, 16]:
        return [
            mc(1, "Một ngày có bao nhiêu giờ?", ["24 giờ", "12 giờ", "60 giờ", "48 giờ"], 0, "1 ngày = 24 giờ."),
            mc(2, "Một giờ có bao nhiêu phút?", ["60 phút", "100 phút", "30 phút", "24 phút"], 0, "1 giờ = 60 phút."),
            mc(3, "Đồng hồ chỉ 8 giờ 30 phút còn gọi là:", ["8 giờ rưỡi", "9 giờ kém 30", "8 giờ", "9 giờ"], 0, "8 giờ 30 phút là 8 giờ rưỡi."),
            mc(4, "Tháng nào sau đây luôn có 31 ngày?", ["Tháng 12", "Tháng 4", "Tháng 6", "Tháng 9"], 0, "Tháng 12 có 31 ngày."),
            mc(5, "Tháng 2 năm nhuận có bao nhiêu ngày?", ["29 ngày", "28 ngày", "30 ngày", "31 ngày"], 0, "Năm nhuận có 29 ngày."),
            mc(6, "Nếu ngày 2 tháng 9 là Thứ Sáu thì ngày 9 tháng 9 là Thứ mấy?", ["Thứ Sáu", "Thứ Bảy", "Chủ Nhật", "Thứ Năm"], 0, "Cách nhau đúng 7 ngày (1 tuần) nên cùng Thứ Sáu.")
        ], [
            essay(1, "Điền số hoặc chữ thích hợp vào chỗ chấm:\na) 1 ngày = ..... giờ\nb) 1 giờ = ..... phút\nc) Tháng 1, tháng 3, tháng 5 có ..... ngày\nd) Tháng 4, tháng 6, tháng 9 có ..... ngày", "Bài giải:\na) 24\nb) 60\nc) 31\nd) 30\nĐáp số: 24, 60, 31, 30", "24, 60, 31, 30", 4, 1.0),
            essay(2, "Xem đồng hồ và đọc giờ:\na) Kim ngắn chỉ số 4, kim dài chỉ số 12: ..... giờ\nb) Kim ngắn chỉ giữa số 7 và 8, kim dài chỉ số 6: ..... giờ ..... phút", "Bài giải:\na) 4 giờ đúng\nb) 7 giờ 30 phút (hay 7 giờ rưỡi)\nĐáp số: a) 4 giờ; b) 7 giờ 30 phút", "a) 4 giờ; b) 7 giờ 30 phút", 4, 1.0),
            essay(3, "Hôm nay là Thứ Tư ngày 15 tháng 10. Hỏi Thứ Tư tuần sau là ngày bao nhiêu?", "Bài giải:\nThứ Tư tuần sau là ngày:\n15 + 7 = 22 (tháng 10)\nĐáp số: Ngày 22 tháng 10", "Ngày 22 tháng 10", 4, 1.0),
            essay(4, "Một bộ phim bắt đầu chiếu lúc 7 giờ tối và kết thúc lúc 9 giờ tối. Hỏi bộ phim đó chiếu trong thời gian bao lâu?", "Bài giải:\nThời gian chiếu bộ phim là:\n9 - 7 = 2 (giờ)\nĐáp số: 2 giờ", "2 giờ", 5, 1.5),
            essay(5, "Đặt tính rồi tính tổng kết kì 1:\na) $56 + 37$\nb) $82 - 45$\nc) $64 + 29$\nd) $90 - 54$", "Bài giải:\na) 93\nb) 37\nc) 93\nd) 36\nĐáp số: 93, 37, 93, 36", "93, 37, 93, 36", 5, 2.0),
            essay(6, "Tìm một số biết rằng nếu lấy số đó cộng với 38 rồi trừ đi 15 thì được kết quả là 60.", "Bài giải:\nTa có: Số cần tìm + 38 = 60 + 15 = 75.\nSố cần tìm là:\n75 - 38 = 37\nĐáp số: 37", "37", 4, 2.0)
        ]

    # 17 đến 20: Phép nhân, phép chia (bảng nhân, chia 2 và 5)
    elif l_num in [17, 18, 19, 20]:
        m_val = 2 if (l_num in [18, 20] and t_num % 2 == 1) else 5
        k_step = 3 + t_num
        return [
            mc(1, f"Kết quả của phép nhân ${m_val} \\times {k_step}$ là:", [str(m_val * k_step), str(m_val * k_step + 1), str(m_val * k_step - 2), "10"], 0, f"${m_val} \\times {k_step} = {m_val * k_step}$."),
            mc(2, f"Kết quả của phép chia ${m_val * k_step} : {m_val}$ là:", [str(k_step), str(k_step + 1), str(k_step - 1), str(m_val)], 0, f"${m_val * k_step} : {m_val} = {k_step}$."),
            mc(3, "Trong phép tính $2 \\times 6 = 12$, số 12 được gọi là:", ["Tích", "Thừa số", "Thương", "Số bị chia"], 0, "Kết quả phép nhân là tích."),
            mc(4, "Trong phép tính $15 : 5 = 3$, số 3 được gọi là:", ["Thương", "Số chia", "Số bị chia", "Tích"], 0, "Kết quả phép chia là thương."),
            mc(5, "Số thích hợp điền vào dấu chấm: $5 \\times ... = 35$", ["7", "6", "8", "9"], 0, "$35 : 5 = 7$."),
            mc(6, "Có 10 cái kẹo chia đều cho 2 bạn. Mỗi bạn được:", ["5 cái kẹo", "4 cái", "6 cái", "2 cái"], 0, "$10 : 2 = 5$ cái kẹo.")
        ], [
            essay(1, "Tính nhẩm:\na) $2 \\times 7 = .....$\nb) $5 \\times 6 = .....$\nc) $16 : 2 = .....$\nd) $40 : 5 = .....$", "Bài giải:\na) 14\nb) 30\nc) 8\nd) 8\nĐáp số: 14, 30, 8, 8", "14, 30, 8, 8", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $2 \\times 8 + 15 = .....$\nb) $5 \\times 7 - 12 = .....$\nc) $20 : 2 + 25 = .....$", "Bài giải:\na) 16 + 15 = 31\nb) 35 - 12 = 23\nc) 10 + 25 = 35\nĐáp số: a) 31; b) 23; c) 35", "a) 31; b) 23; c) 35", 4, 1.0),
            essay(3, "Tìm x biết:\na) $x \\times 2 = 18$\nb) $x : 5 = 6$", "Bài giải:\na) x = 18 : 2 = 9\nb) x = 6 x 5 = 30\nĐáp số: a) x = 9; b) x = 30", "a) 9; b) 30", 4, 1.0),
            essay(4, "Mỗi chuồng có 5 chú thỏ. Hỏi 6 chuồng như thế có tất cả bao nhiêu chú thỏ?", "Bài giải:\n6 chuồng có tất cả số chú thỏ là:\n5 x 6 = 30 (chú thỏ)\nĐáp số: 30 chú thỏ", "30 chú thỏ", 5, 1.5),
            essay(5, "Có 18 quả cam chia đều vào các đĩa, mỗi đĩa 2 quả. Hỏi chia được bao nhiêu đĩa cam như thế?", "Bài giải:\nSố đĩa cam chia được là:\n18 : 2 = 9 (đĩa cam)\nĐáp số: 9 đĩa cam", "9 đĩa", 5, 2.0),
            essay(6, "Một người có 35 bông hoa đem cắm đều vào 5 bình hoa. Hỏi mỗi bình hoa có mấy bông hoa?", "Bài giải:\nMỗi bình hoa có số bông hoa là:\n35 : 5 = 7 (bông hoa)\nĐáp số: 7 bông hoa", "7 bông hoa", 4, 2.0)
        ]

    # 21. Khối trụ, khối cầu
    elif l_num == 21:
        return [
            mc(1, "Quả bóng đá em chơi thường có dạng hình khối gì?", ["Khối cầu", "Khối trụ", "Khối lập phương", "Khối hộp"], 0, "Quả bóng có dạng khối cầu."),
            mc(2, "Lon nước ngọt coca hoặc sữa đặc có dạng hình khối gì?", ["Khối trụ", "Khối cầu", "Khối chóp", "Khối vuông"], 0, "Lon nước ngọt có dạng khối trụ."),
            mc(3, "Khối cầu có đặc điểm nào dưới đây?", ["Lăn được về mọi phía", "Có 6 mặt vuông", "Có các cạnh nhọn", "Không lăn được"], 0, "Khối cầu tròn đều nên lăn được về mọi phía."),
            mc(4, "Khối trụ có mấy mặt đáy hình tròn bằng nhau?", ["2 mặt đáy hình tròn", "1 mặt đáy", "3 mặt", "Không có"], 0, "Khối trụ có 2 đáy tròn."),
            mc(5, "Hộp đựng cầu lông thường có dạng khối gì?", ["Khối trụ", "Khối cầu", "Khối lập phương", "Khối chóp"], 0, "Dạng khối trụ tròn dài."),
            mc(6, "Viên bi ve em hay bắn có dạng khối gì?", ["Khối cầu", "Khối trụ", "Khối tròn dẹt", "Khối vuông"], 0, "Viên bi là khối cầu tròn.")
        ], [
            essay(1, "Kể tên 3 đồ vật quen thuộc trong đời sống có dạng:\na) Khối cầu\nb) Khối trụ", "Bài giải:\na) Khối cầu: Quả địa cầu, quả bóng đá, viên bi ve, quả cam.\nb) Khối trụ: Lon nước ngọt, hộp sữa bột, ống bơ đong gạo, cục pin.\nĐáp số: Đúng tên các đồ vật", "Đúng các đồ vật", 4, 1.0),
            essay(2, "Khối cầu và khối trụ giống nhau và khác nhau ở điểm nào?", "Bài giải:\n- Giống nhau: Đều có bề mặt cong và có thể lăn được.\n- Khác nhau: Khối cầu lăn được về mọi phía; Khối trụ chỉ lăn được khi đặt nằm và có 2 đáy hình tròn phẳng.\nĐáp số: Nêu đúng điểm giống và khác", "Giống lăn được; khác đáy phẳng / mọi phía", 4, 1.0),
            essay(3, "Bạn An xếp chồng 3 lon sữa bò dạng khối trụ lên nhau. Hỏi khối mới tạo thành có dạng hình khối gì?", "Bài giải:\nKhối mới tạo thành vẫn là một khối trụ cao hơn.\nĐáp số: Khối trụ", "Khối trụ", 4, 1.0),
            essay(4, "Trong một rổ đồ chơi gồm có 5 quả bóng tennis và 4 hộp sữa bột rỗng. Hỏi trong rổ có bao nhiêu vật dạng khối cầu và bao nhiêu vật dạng khối trụ?", "Bài giải:\n- Có 5 vật dạng khối cầu (5 quả bóng).\n- Có 4 vật dạng khối trụ (4 hộp sữa bột).\nĐáp số: 5 khối cầu và 4 khối trụ", "5 khối cầu, 4 khối trụ", 5, 1.5),
            essay(5, "Tại sao bánh xe ô tô, xe máy lại được làm tròn (hình trụ dẹt) mà không làm hình vuông?", "Bài giải:\nVì hình tròn và khối trụ lăn được dễ dàng trên mặt đất giúp xe di chuyển êm ái và tốn ít sức lực hơn.\nĐáp số: Vì lăn được êm và dễ di chuyển", "Vì dễ lăn, giảm ma sát", 5, 2.0),
            essay(6, "Cắt đôi một khối cầu bằng một mặt phẳng cắt qua tâm, mặt cắt thu được là hình gì?", "Bài giải:\nMặt cắt thu được là một hình tròn phẳng.\nĐáp số: Hình tròn", "Hình tròn", 4, 2.0)
        ]

    # 22, 23, 24. Các số trong phạm vi 1000
    elif l_num in [22, 23, 24]:
        val3 = 300 + t_num * 125
        return [
            mc(1, f"Số gồm {val3 // 100} trăm, {(val3 % 100) // 10} chục và {val3 % 10} đơn vị viết là:", [str(val3), str(val3+10), str(val3-1), "1000"], 0, f"Viết là {val3}."),
            mc(2, f"Số liền trước của số {val3} là:", [str(val3 - 1), str(val3 + 1), str(val3 - 10), str(val3)], 0, f"{val3} - 1 = {val3 - 1}."),
            mc(3, "Số lớn nhất có ba chữ số là:", ["999", "1000", "900", "990"], 0, "Số 999."),
            mc(4, "Số bé nhất có ba chữ số là:", ["100", "101", "111", "001"], 0, "Số 100."),
            mc(5, "Một nghìn viết bằng chữ số là:", ["1 000", "100", "10 000", "10"], 0, "Số 1 000 có 3 chữ số 0."),
            mc(6, f"So sánh: {val3} ... {val3 + 50}", ["<", ">", "=", "Không có"], 0, f"{val3} < {val3 + 50}.")
        ], [
            essay(1, f"Viết các số sau:\na) Năm trăm hai mươi tư: .....\nb) Bảy trăm linh tám: .....\nc) Tám trăm chín mươi: .....\nd) Một nghìn: .....", "Bài giải:\na) 524\nb) 708\nc) 890\nd) 1000\nĐáp số: 524, 708, 890, 1000", "524, 708, 890, 1000", 4, 1.0),
            essay(2, f"Viết số {val3} thành tổng các trăm, chục và đơn vị:", f"Bài giải:\n{val3} = {val3 // 100 * 100} + {((val3 % 100) // 10) * 10} + {val3 % 10}\nĐáp số: {val3 // 100 * 100} + {((val3 % 100) // 10) * 10} + {val3 % 10}", f"{val3 // 100 * 100} + {((val3 % 100) // 10) * 10} + {val3 % 10}", 4, 1.0),
            essay(3, "Sắp xếp các số 354, 782, 198, 520, 905 theo thứ tự:\na) Từ bé đến lớn\nb) Từ lớn đến bé", "Bài giải:\na) 198, 354, 520, 782, 905\nb) 905, 782, 520, 354, 198\nĐáp số: a) 198, 354, 520, 782, 905; b) 905, 782, 520, 354, 198", "a) 198, 354, 520, 782, 905; b) 905, 782, 520, 354, 198", 4, 1.0),
            essay(4, "Tìm số tròn trăm liền trước và liền sau của số 450.", "Bài giải:\n- Số tròn trăm liền trước 450 là: 400.\n- Số tròn trăm liền sau 450 là: 500.\nĐáp số: 400 và 500", "400 và 500", 5, 1.5),
            essay(5, "Từ ba chữ số 4, 0, 7 hãy viết tất cả các số có ba chữ số khác nhau và sắp xếp chúng theo thứ tự từ lớn đến bé.", "Bài giải:\nCác số có ba chữ số khác nhau ghép được là: 407, 470, 704, 740.\nSắp xếp từ lớn đến bé: 740, 704, 470, 407.\nĐáp số: 740, 704, 470, 407", "740, 704, 470, 407", 5, 2.0),
            essay(6, "Tìm số lớn nhất có 3 chữ số khác nhau có chữ số hàng trăm bằng 6.", "Bài giải:\nĐể số lớn nhất thì chữ số hàng chục phải lớn nhất là 9, chữ số hàng đơn vị tiếp theo là 8.\nSố cần tìm là 698.\nĐáp số: 698", "698", 4, 2.0)
        ]

    # 25 & 26. Mét (m), Ki-lô-mét (km), Mi-li-mét (mm)
    elif l_num in [25, 26]:
        return [
            mc(1, "Đổi: $1\\text{ m} = ...\\text{ dm}$", ["10 dm", "100 dm", "1 dm", "1000 dm"], 0, "1 m = 10 dm."),
            mc(2, "Đổi: $1\\text{ m} = ...\\text{ cm}$", ["100 cm", "10 cm", "1000 cm", "1 cm"], 0, "1 m = 100 cm."),
            mc(3, "Đổi: $1\\text{ km} = ...\\text{ m}$", ["1 000 m", "100 m", "10 m", "10 000 m"], 0, "1 km = 1000 m."),
            mc(4, "Đổi: $1\\text{ cm} = ...\\text{ mm}$", ["10 mm", "100 mm", "1 mm", "1000 mm"], 0, "1 cm = 10 mm."),
            mc(5, "Quãng đường từ Hà Nội đến Thành phố Hồ Chí Minh đo bằng đơn vị:", ["Ki-lô-mét (km)", "Mét (m)", "Xăng-ti-mét (cm)", "Mi-li-mét (mm)"], 0, "Khoảng cách xa đo bằng km."),
            mc(6, "Bề dày của cuốn sách Toán 2 dày khoảng:", ["8 mm", "8 m", "8 km", "80 cm"], 0, "Khoảng 8 mm.")
        ], [
            essay(1, "Viết số thích hợp vào chỗ chấm:\na) $1\\text{ m} = .....\\text{ cm}$\nb) $1\\text{ km} = .....\\text{ m}$\nc) $1\\text{ cm} = .....\\text{ mm}$\nd) $1\\text{ m} = .....\\text{ mm}$", "Bài giải:\na) 100 cm\nb) 1000 m\nc) 10 mm\nd) 1000 mm\nĐáp số: 100, 1000, 10, 1000", "100, 1000, 10, 1000", 4, 1.0),
            essay(2, "Tính:\na) $35\\text{ m} + 28\\text{ m} = .....$\nb) $80\\text{ km} - 35\\text{ km} = .....$\nc) $45\\text{ mm} + 25\\text{ mm} = .....$", "Bài giải:\na) 63 m\nb) 45 km\nc) 70 mm\nĐáp số: 63 m, 45 km, 70 mm", "63 m, 45 km, 70 mm", 4, 1.0),
            essay(3, "Điền dấu thích hợp (>, <, =):\na) $1\\text{ m} ... 95\\text{ cm}$\nb) $1\\text{ km} ... 1 000\\text{ m}$\nc) $3\\text{ cm} ... 35\\text{ mm}$", "Bài giải:\na) 100 cm > 95 cm\nb) 1000 m = 1000 m\nc) 30 mm < 35 mm\nĐáp số: a) >; b) =; c) <", "a) >; b) =; c) <", 4, 1.0),
            essay(4, "Một cây cột cờ cao 8 mét, người ta lắp thêm một cán cờ cao 2 mét ở đỉnh. Hỏi đỉnh cột cờ lúc này cách mặt đất bao nhiêu mét?", "Bài giải:\nĐỉnh cột cờ cách mặt đất số mét là:\n8 + 2 = 10 (m)\nĐáp số: 10 mét", "10 mét", 5, 1.5),
            essay(5, "Quãng đường từ nhà bạn Nam đến trường dài 2 km, quãng đường từ nhà bạn Bình đến trường dài 1 500 m. Hỏi nhà bạn nào xa trường hơn và xa hơn bao nhiêu mét?", "Bài giải:\nĐổi: 2 km = 2 000 m.\nVì 2 000 m > 1 500 m nên nhà bạn Nam xa trường hơn.\nXa hơn số mét là:\n2 000 - 1 500 = 500 (m)\nĐáp số: Nhà Nam xa hơn 500 m", "Nhà Nam xa hơn 500 m", 5, 2.0),
            essay(6, "Một tấm gỗ dài 2 mét, thợ mộc cưa bớt đi 60 cm. Hỏi tấm gỗ còn lại dài bao nhiêu xăng-ti-mét?", "Bài giải:\nĐổi: 2 m = 200 cm.\nTấm gỗ còn lại dài là:\n200 - 60 = 140 (cm)\nĐáp số: 140 cm", "140 cm", 4, 2.0)
        ]

    # 27 & 28. Phép cộng, trừ trong phạm vi 1000
    elif l_num in [27, 28]:
        d_a = 432 + t_num * 50
        d_b = 215 + t_num * 30
        return [
            mc(1, f"Đặt tính rồi tính: ${d_a} + {d_b} = $", [str(d_a + d_b), str(d_a + d_b + 10), str(d_a + d_b - 5), "700"], 0, f"{d_a} + {d_b} = {d_a + d_b}."),
            mc(2, f"Đặt tính rồi tính: ${d_a + 100} - {d_b} = $", [str(d_a + 100 - d_b), str(d_a + 100 - d_b + 10), "300", "400"], 0, f"{d_a + 100} - {d_b} = {d_a + 100 - d_b}."),
            mc(3, "Tính nhẩm: $500 + 400 = $", ["900", "800", "1000", "700"], 0, "500 + 400 = 900."),
            mc(4, "Tính nhẩm: $1 000 - 300 = $", ["700", "600", "800", "900"], 0, "1000 - 300 = 700."),
            mc(5, f"Số thích hợp điền vào chỗ chấm: $320 + ... = 380$", ["60", "50", "70", "80"], 0, "380 - 320 = 60."),
            mc(6, "Điền dấu: $450 + 50 ... 600 - 100$", ["=", ">", "<", "Không có"], 0, "500 = 500.")
        ], [
            essay(1, "Đặt tính rồi tính:\na) $345 + 231$\nb) $678 - 342$\nc) $506 + 263$\nd) $894 - 450$", "Bài giải:\na) 576\nb) 336\nc) 769\nd) 444\nĐáp số: 576, 336, 769, 444", "576, 336, 769, 444", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $320 + 150 - 200 = .....$\nb) $780 - 240 + 110 = .....$", "Bài giải:\na) 470 - 200 = 270\nb) 540 + 110 = 650\nĐáp số: a) 270; b) 650", "a) 270; b) 650", 4, 1.0),
            essay(3, "Tìm x biết:\na) $x - 230 = 450$\nb) $x + 315 = 785$", "Bài giải:\na) x = 450 + 230 = 680\nb) x = 785 - 315 = 470\nĐáp số: a) x = 680; b) x = 470", "a) 680; b) 470", 4, 1.0),
            essay(4, "Một trang trại nuôi 345 con gà mái và 120 con gà trống. Hỏi trang trại đó nuôi tất cả bao nhiêu con gà?", "Bài giải:\nTrang trại đó nuôi tất cả số con gà là:\n345 + 120 = 465 (con gà)\nĐáp số: 465 con gà", "465 con gà", 5, 1.5),
            essay(5, "Một cửa hàng có 850 mét vải hoa. Tuần thứ nhất bán được 320 mét vải, tuần thứ hai bán được 210 mét vải. Hỏi cửa hàng còn lại bao nhiêu mét vải hoa?", "Bài giải:\nCả hai tuần bán được số mét vải là:\n320 + 210 = 530 (m)\nCửa hàng còn lại số mét vải hoa là:\n850 - 530 = 320 (m)\nĐáp số: 320 mét vải", "320 mét", 5, 2.0),
            essay(6, "Tìm tổng của số lớn nhất có ba chữ số và số bé nhất có ba chữ số khác nhau.", "Bài giải:\n- Số lớn nhất có ba chữ số là 999.\n- Số bé nhất có ba chữ số khác nhau là 102.\nTổng là: 999 + 102 = 1 101.\nĐáp số: 1 101", "1 101", 4, 2.0)
        ]

    # 29 & 30. Tiền Việt Nam và Thống kê số liệu
    elif l_num in [29, 30]:
        return [
            mc(1, "Tờ tiền Việt Nam nào có mệnh giá nhỏ nhất trong các tờ sau?", ["100 đồng", "1 000 đồng", "2 000 đồng", "5 000 đồng"], 0, "Tờ 100 đồng nhỏ nhất."),
            mc(2, "Mẹ đưa cho em 2 tờ 2 000 đồng và 1 tờ 1 000 đồng. Em có tất cả:", ["5 000 đồng", "4 000 đồng", "3 000 đồng", "6 000 đồng"], 0, "$2 000 + 2 000 + 1 000 = 5 000$ đồng."),
            mc(3, "Để mua một cây kem giá 5 000 đồng bằng các tờ 1 000 đồng thì cần:", ["5 tờ", "4 tờ", "6 tờ", "2 tờ"], 0, "5 tờ 1 000 đồng."),
            mc(4, "Tung một đồng xu 10 lần thu được 6 lần mặt sấp. Số lần mặt ngửa là:", ["4 lần", "5 lần", "6 lần", "10 lần"], 0, "$10 - 6 = 4$ lần."),
            mc(5, "Bảng kiểm đếm số học sinh thích ăn các loại quả cho biết có 8 bạn thích cam, 12 bạn thích xoài, 5 bạn thích chuối. Loại quả được thích nhiều nhất là:", ["Xoài", "Cam", "Chuối", "Bằng nhau"], 0, "Quả xoài có 12 bạn (nhiều nhất)."),
            mc(6, "Đổi 1 tờ 5 000 đồng lấy các tờ 1 000 đồng và 2 000 đồng thì được:", ["1 tờ 1 000đ và 2 tờ 2 000đ", "3 tờ 2 000đ", "2 tờ 1 000đ", "4 tờ 2 000đ"], 0, "$1 000 + 2 000 + 2 000 = 5 000$ đồng.")
        ], [
            essay(1, "Tính tổng số tiền:\na) 2 tờ 1 000 đồng + 1 tờ 2 000 đồng = ..... đồng\nb) 1 tờ 5 000 đồng + 2 tờ 2 000 đồng = ..... đồng", "Bài giải:\na) 2000 + 2000 = 4 000 đồng\nb) 5000 + 4000 = 9 000 đồng\nĐáp số: a) 4 000 đồng; b) 9 000 đồng", "a) 4 000 đồng; b) 9 000 đồng", 4, 1.0),
            essay(2, "Bạn An mua một chiếc bút chì giá 3 000 đồng và một cục tẩy giá 2 000 đồng. An đưa cô bán hàng tờ 10 000 đồng. Hỏi cô bán hàng trả lại An bao nhiêu tiền?", "Bài giải:\nTổng số tiền mua hàng là:\n3 000 + 2 000 = 5 000 (đồng)\nCô bán hàng trả lại số tiền là:\n10 000 - 5 000 = 5 000 (đồng)\nĐáp số: 5 000 đồng", "5 000 đồng", 4, 1.0),
            essay(3, "Bảng thống kê số hoa điểm 10 trong tuần của tổ 1:\n- Thứ Hai: 8 hoa\n- Thứ Ba: 6 hoa\n- Thứ Tư: 9 hoa\n- Thứ Năm: 7 hoa\n- Thứ Sáu: 10 hoa\na) Ngày nào tổ 1 được nhiều hoa điểm 10 nhất?\nb) Cả tuần tổ 1 được bao nhiêu hoa điểm 10?", "Bài giải:\na) Ngày Thứ Sáu được nhiều hoa điểm 10 nhất (10 hoa).\nb) Cả tuần được số hoa điểm 10 là:\n8 + 6 + 9 + 7 + 10 = 40 (hoa điểm 10)\nĐáp số: a) Thứ Sáu; b) 40 hoa điểm 10", "a) Thứ Sáu; b) 40 hoa", 4, 1.0),
            essay(4, "Một hộp sữa giá 7 000 đồng, một cái bánh mì giá 8 000 đồng. Nam có 20 000 đồng. Hỏi sau khi mua 1 hộp sữa và 1 cái bánh mì thì Nam còn lại bao nhiêu tiền?", "Bài giải:\nTổng số tiền Nam mua là:\n7 000 + 8 000 = 15 000 (đồng)\nNam còn lại số tiền là:\n20 000 - 15 000 = 5 000 (đồng)\nĐáp số: 5 000 đồng", "5 000 đồng", 5, 1.5),
            essay(5, "Kiểm đếm các con vật nuôi trong sân nhà bà ngoại:\n- Gà: 15 con\n- Vịt: 12 con\n- Ngan: 8 con\na) Loại con vật nào có nhiều nhất?\nb) Tổng số các con vật nuôi trong sân là bao nhiêu con?", "Bài giải:\na) Gà có nhiều nhất (15 con).\nb) Tổng số con vật là:\n15 + 12 + 8 = 35 (con vật)\nĐáp số: a) Gà nhiều nhất; b) 35 con vật", "a) Gà; b) 35 con", 5, 2.0),
            essay(6, "Bình có 3 tờ tiền gồm hai loại mệnh giá 2 000 đồng và 5 000 đồng. Hỏi Bình có thể có tất cả bao nhiêu tiền?", "Bài giải:\nTrường hợp 1: Có 2 tờ 2 000đ và 1 tờ 5 000đ:\n2 000 x 2 + 5 000 = 9 000 (đồng).\nTrường hợp 2: Có 1 tờ 2 000đ và 2 tờ 5 000đ:\n2 000 + 5 000 x 2 = 12 000 (đồng).\nĐáp số: Bình có thể có 9 000 đồng hoặc 12 000 đồng", "9 000 đồng hoặc 12 000 đồng", 4, 2.0)
        ]

    # 31 & 32. Ôn tập cuối năm
    else:
        return [
            mc(1, "Số liền sau của 899 là:", ["900", "898", "901", "890"], 0, "$899 + 1 = 900$."),
            mc(2, "Tính: $5 \\times 8 = $", ["40", "35", "45", "30"], 0, "$5 \\times 8 = 40$."),
            mc(3, "Tính: $18 : 2 = $", ["9", "8", "7", "6"], 0, "$18 : 2 = 9$."),
            mc(4, "Độ dài đường gấp khúc gồm 3 đoạn 4 cm, 6 cm, 8 cm là:", ["18 cm", "16 cm", "20 cm", "14 cm"], 0, "$4 + 6 + 8 = 18$ cm."),
            mc(5, "Đổi: $1\\text{ m} = ...\\text{ cm}$", ["100 cm", "10 cm", "1000 cm", "1 cm"], 0, "1 m = 100 cm."),
            mc(6, "Đồng hồ chỉ 3 giờ chiều còn gọi là:", ["15 giờ", "13 giờ", "14 giờ", "16 giờ"], 0, "$3 + 12 = 15$ giờ.")
        ], [
            essay(1, "Đặt tính rồi tính:\na) $456 + 238$\nb) $872 - 345$\nc) $5 \\times 9$\nd) $14 : 2$", "Bài giải:\na) 694\nb) 527\nc) 45\nd) 7\nĐáp số: 694, 527, 45, 7", "694, 527, 45, 7", 4, 1.0),
            essay(2, "Tính giá trị biểu thức:\na) $2 \\times 9 + 45 = .....$\nb) $40 : 5 + 32 = .....$", "Bài giải:\na) 18 + 45 = 63\nb) 8 + 32 = 40\nĐáp số: a) 63; b) 40", "a) 63; b) 40", 4, 1.0),
            essay(3, "Tìm x biết:\na) $x \\times 2 = 16$\nb) $x - 145 = 320$", "Bài giải:\na) x = 16 : 2 = 8\nb) x = 320 + 145 = 465\nĐáp số: a) x = 8; b) x = 465", "a) 8; b) 465", 4, 1.0),
            essay(4, "Một cửa hàng có 350 kg gạo tẻ và 210 kg gạo nếp. Buổi sáng cửa hàng bán được 180 kg gạo các loại. Hỏi cửa hàng còn lại bao nhiêu ki-lô-gam gạo?", "Bài giải:\nTổng số gạo cửa hàng có là:\n350 + 210 = 560 (kg)\nCửa hàng còn lại số ki-lô-gam gạo là:\n560 - 180 = 380 (kg)\nĐáp số: 380 kg gạo", "380 kg", 5, 1.5),
            essay(5, "Một sợi dây dài 20 mét được cắt thành 5 đoạn bằng nhau. Hỏi mỗi đoạn dây dài bao nhiêu mét?", "Bài giải:\nMỗi đoạn dây dài số mét là:\n20 : 5 = 4 (m)\nĐáp số: 4 mét", "4 mét", 5, 2.0),
            essay(6, "Tìm một số biết rằng lấy số đó chia cho 2 rồi cộng với 15 thì được kết quả bằng 24.", "Bài giải:\nSố đó chia cho 2 là: 24 - 15 = 9.\nSố cần tìm là:\n9 x 2 = 18.\nĐáp số: 18", "18", 4, 2.0)
        ]

def get_toan2_lesson_exams():
    exams = {}
    from toan2_curriculum_def import TOAN2_CURRICULUM
    ch_map = {}
    for ch in TOAN2_CURRICULUM["chapters"]:
        for les in ch["lessons"]:
            ch_map[les["num"]] = (ch["title"], ch["term"], les["name"])

    for l_num in range(1, 33):
        ch_title, term_code, les_name = ch_map.get(l_num, ("Chủ đề bài học", "hk1", f"Bài {l_num}"))
        for t_idx in range(1, 4):
            eid = f"th2_b{l_num}_test{t_idx}"
            p1, p2 = build_toan2_lesson(l_num, t_idx)
            exams[eid] = {
                "id": eid, "lessonId": f"th2_b{l_num}", "lessonNum": l_num, "testNum": t_idx,
                "title": f"{les_name} - Đề số {t_idx}",
                "topic": ch_title, "chapter": ch_title.split(":")[0],
                "grade": "2", "term": term_code, "duration": "35 phút", "points": 10.0,
                "part1": p1,
                "part2": p2
            }

    print(f"-> Đã tạo thành công {len(exams)} đề kiểm tra theo bài cho TOÁN 2 (32 bài x 3 đề = 96 đề)")
    return exams

if __name__ == "__main__":
    exs = get_toan2_lesson_exams()
    print("Mẫu đề th2_b1_test1:", exs["th2_b1_test1"]["title"])
    print("P1 len:", len(exs["th2_b1_test1"]["part1"]), "P2 len:", len(exs["th2_b1_test1"]["part2"]))
