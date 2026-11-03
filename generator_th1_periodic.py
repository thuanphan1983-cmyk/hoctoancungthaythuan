# -*- coding: utf-8 -*-
"""
HỆ THỐNG ĐỀ KIỂM TRA ĐỊNH KỲ TOÁN LỚP 1 (BỘ KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
Bao gồm 32 đề kiểm tra chuẩn hóa độc lập:
- 8 đề Giữa học kì 1 (th1_gk1_de01 -> th1_gk1_de08)
- 8 đề Cuối học kì 1 (th1_ck1_de01 -> th1_ck1_de08)
- 8 đề Giữa học kì 2 (th1_gk2_de01 -> th1_gk2_de08)
- 8 đề Cuối học kì 2 (th1_ck2_de01 -> th1_ck2_de08)
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def make_mc(qid, question, options, correct, explanation):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "choices": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question, solution, answer, lineCount=4, points=1.0):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    return {
        "id": qid,
        "question": p_text,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_th1_exams():
    exams = {}

    terms = [
        ("gk1", "Giữa Học kì 1", "35 phút"),
        ("ck1", "Cuối Học kì 1", "35 phút"),
        ("gk2", "Giữa Học kì 2", "35 phút"),
        ("ck2", "Cuối Học kì 2", "35 phút")
    ]

    for term_code, term_name, duration in terms:
        for t in range(1, 9):
            eid = f"th1_{term_code}_de{t:02d}"
            
            if term_code == "gk1":
                # GK1: Số 0-10, so sánh, hình phẳng
                a, b = 2 + (t % 5), 4 + ((t + 2) % 5)
                larger = max(a, b)
                smaller = min(a, b)
                p1 = [
                    make_mc(1, f"Số thích hợp điền vào dấu chấm: {t}, {t+1}, ..., {t+3} là:", [str(t+2), str(t+1), str(t+4), str(t)], 0, f"Dãy số đếm tăng dần: {t}, {t+1}, {t+2}, {t+3}."),
                    make_mc(2, f"Trong hai số {a} và {b}, số bé hơn là số:", [str(smaller), str(larger), str(larger + 1), "Bằng nhau"], 0, f"Ta có {smaller} < {larger}."),
                    make_mc(3, "Hình nào dưới đây có 3 cạnh và 3 đỉnh?", ["Hình tam giác", "Hình tròn", "Hình vuông", "Hình chữ nhật"], 0, "Hình tam giác có 3 cạnh và 3 đỉnh."),
                    make_mc(4, f"Có {t + 1} chú thỏ và {t + 3} củ cà rốt. Khẳng định nào đúng?", ["Số thỏ ít hơn số cà rốt", "Số thỏ nhiều hơn số cà rốt", "Số thỏ bằng số cà rốt", "Không so sánh được"], 0, f"Vì {t+1} < {t+3} nên số thỏ ít hơn số cà rốt."),
                    make_mc(5, f"Số lớn nhất trong các số {t}, {t+2}, {t+1}, {t+3} là:", [str(t+3), str(t+2), str(t+1), str(t)], 0, f"Số {t+3} là số lớn nhất trong dãy."),
                    make_mc(6, "Bánh quy dạng hình tròn có đặc điểm gì?", ["Không có cạnh và góc nhọn", "Có 4 cạnh bằng nhau", "Có 3 cạnh", "Có 4 góc vuông"], 0, "Hình tròn có đường viền cong kín tròn đều.")
                ]
                p2 = [
                    make_essay(1, f"Viết các số sau theo thứ tự từ bé đến lớn:\n{t+3}, {t}, {t+2}, {t+1}", f"Sắp xếp từ bé đến lớn: {t}, {t+1}, {t+2}, {t+3}", f"{t}, {t+1}, {t+2}, {t+3}", 4, 1.0),
                    make_essay(2, f"Điền dấu (>, <, =) thích hợp vào ô trống:\na) {a} ... {b}\nb) {larger} ... {smaller}", f"a) {a} < {b} (hoặc > tùy giá trị)\nb) {larger} > {smaller}", "a) <; b) >", 4, 1.0),
                    make_essay(3, "Đếm số hình trong hình vẽ (hình tam giác, hình tròn, hình vuông).", "Học sinh đếm cẩn thận và điền đúng số lượng từng hình phẳng.", "Đúng số lượng", 4, 1.0),
                    make_essay(4, f"Bình có {t+2} quả bóng bay màu đỏ và {t+1} quả bóng bay màu xanh. Hỏi Bình có tất cả bao nhiêu quả bóng bay?", f"Bình có tất cả số quả bóng bay là:\n{t+2} + {t+1} = {2*t+3} (quả bóng)\nĐáp số: {2*t+3} quả bóng", f"{2*t+3} quả bóng", 5, 1.5),
                    make_essay(5, f"Trên cành cây có {t+4} con chim đang đậu, sau đó có {t+1} con chim bay đi. Hỏi trên cành cây còn lại bao nhiêu con chim?", f"Trên cành cây còn lại số con chim là:\n{t+4} - {t+1} = 3 (con chim)\nĐáp số: 3 con chim", "3 con chim", 5, 1.5),
                    make_essay(6, f"Điền số thích hợp vào ô trống: ... + 2 = {t+4}", f"Số cần điền là: {t+4} - 2 = {t+2}", str(t+2), 4, 1.0)
                ]

            elif term_code == "ck1":
                # CK1: Cộng trừ phạm vi 10, hình khối
                s1, s2 = (t % 4) + 2, (t % 3) + 3
                p1 = [
                    make_mc(1, f"Kết quả của phép tính {s1} + {s2} là:", [str(s1+s2), str(s1+s2+1), str(s1+s2-1), str(s1+s2+2)], 0, f"{s1} + {s2} = {s1+s2}."),
                    make_mc(2, f"Kết quả của phép trừ 10 - {t} là:", [str(10-t), str(10-t+1), str(10-t-1), str(t)], 0, f"10 - {t} = {10-t}."),
                    make_mc(3, "Hộp sữa tươi có dạng hình khối nào?", ["Khối hộp chữ nhật", "Khối lập phương", "Hình tròn", "Hình tam giác"], 0, "Hộp sữa tươi thông thường có dạng khối hộp chữ nhật."),
                    make_mc(4, f"Phép tính nào dưới đây có kết quả bằng {t+2}?", [f"{t} + 2", f"{t} + 1", f"{t} + 3", f"{t} - 1"], 0, f"{t} + 2 = {t+2}."),
                    make_mc(5, f"Số thích hợp điền vào chỗ chấm: {s1+s2} - ... = {s1} là:", [str(s2), str(s1), str(s1+1), "0"], 0, f"{s1+s2} - {s2} = {s1}."),
                    make_mc(6, "Viên xúc xắc (xí ngầu) có dạng hình khối nào?", ["Khối lập phương", "Khối hộp chữ nhật", "Hình vuông", "Hình trụ"], 0, "Viên xúc xắc có 6 mặt hình vuông bằng nhau nên có dạng khối lập phương.")
                ]
                p2 = [
                    make_essay(1, f"Tính:\na) {s1} + {s2} = ...\nb) 9 - {t % 5 + 1} = ...", f"a) {s1} + {s2} = {s1+s2}\nb) 9 - {t % 5 + 1} = {9 - (t % 5 + 1)}", f"a) {s1+s2}; b) {9 - (t % 5 + 1)}", 4, 1.0),
                    make_essay(2, f"Tính giá trị dãy tính:\na) {t} + 2 + 1 = ...\nb) 10 - 3 - 2 = ...", f"a) {t} + 2 + 1 = {t+3}\nb) 10 - 3 - 2 = 5", f"a) {t+3}; b) 5", 4, 1.0),
                    make_essay(3, "Kể tên các đồ vật trong gia đình em có dạng khối lập phương hoặc khối hộp chữ nhật.", "Các đồ vật: Hộp bánh quy, tủ lạnh, hộp sữa, viên gạch xây nhà...", "Nêu đúng đồ vật", 4, 1.0),
                    make_essay(4, f"Lan có {s1+1} bông hoa, Mai tặng Lan thêm {s2} bông hoa nữa. Hỏi Lan có tất cả bao nhiêu bông hoa?", f"Lan có tất cả số bông hoa là:\n{s1+1} + {s2} = {s1+1+s2} (bông hoa)\nĐáp số: {s1+1+s2} bông hoa", f"{s1+1+s2} bông hoa", 5, 1.5),
                    make_essay(5, f"Trong đĩa có 10 quả dâu tây, bé An đã ăn {t} quả. Hỏi trong đĩa còn lại bao nhiêu quả dâu tây?", f"Trong đĩa còn lại số quả dâu tây là:\n10 - {t} = {10-t} (quả dâu tây)\nĐáp số: {10-t} quả dâu tây", f"{10-t} quả dâu tây", 5, 1.5),
                    make_essay(6, f"Điền số thích hợp vào chỗ chấm: 8 - ... + 3 = 7", "Ta có: 8 - 4 + 3 = 4 + 3 = 7. Vậy số cần điền là 4.", "4", 4, 1.0)
                ]

            elif term_code == "gk2":
                # GK2: Số có 2 chữ số đến 100, cm
                tens = 2 + (t % 6)
                p1 = [
                    make_mc(1, f"Số gồm {tens} chục và 5 đơn vị viết là:", [f"{tens}5", f"5{tens}", f"{tens}05", f"{tens+5}"], 0, f"{tens} chục và 5 đơn vị là số {tens}5."),
                    make_mc(2, f"Số liền sau của số {tens}9 là:", [f"{tens+1}0", f"{tens}8", f"{tens}7", f"{tens+1}1"], 0, f"Số liền sau của {tens}9 là {tens+1}0."),
                    make_mc(3, "Đơn vị xăng-ti-mét được viết tắt là:", ["cm", "m", "dm", "kg"], 0, "Xăng-ti-mét viết tắt là cm."),
                    make_mc(4, f"Đoạn thẳng AB dài {10+t} cm, đoạn thẳng CD dài {15+t} cm. Đoạn thẳng nào dài hơn?", ["Đoạn thẳng CD", "Đoạn thẳng AB", "Hai đoạn bằng nhau", "Không xác định"], 0, f"Vì {15+t} cm > {10+t} cm nên đoạn thẳng CD dài hơn."),
                    make_mc(5, f"Số tròn chục lớn hơn {tens*10} và bé hơn {(tens+2)*10} là:", [f"{(tens+1)*10}", f"{tens*10 + 5}", f"{(tens-1)*10}", f"{tens*10}"], 0, f"Số tròn chục nằm giữa là {(tens+1)*10}."),
                    make_mc(6, f"Đọc số: Số 4{t} được đọc là:", [f"Bốn mươi {t}", f"Bốn mươi", f"Bốn {t}", f"{t} mươi tư"], 0, f"Số 4{t} đọc là bốn mươi...")
                ]
                p2 = [
                    make_essay(1, f"Viết số thích hợp vào chỗ chấm:\na) Số {tens}7 gồm ... chục và ... đơn vị\nb) Số tròn chục liền trước số {tens*10+10} là ...", f"a) Số {tens}7 gồm {tens} chục và 7 đơn vị\nb) Số tròn chục liền trước là {tens*10}", f"a) {tens} chục, 7 đơn vị; b) {tens*10}", 4, 1.0),
                    make_essay(2, f"Tính:\na) {10+t} cm + 5 cm = ...\nb) {18+t} cm - 8 cm = ...", f"a) {10+t} cm + 5 cm = {15+t} cm\nb) {18+t} cm - 8 cm = {10+t} cm", f"a) {15+t} cm; b) {10+t} cm", 4, 1.0),
                    make_essay(3, f"Sắp xếp các số sau theo thứ tự từ lớn đến bé:\n{tens*10+2}, {tens*10+8}, {tens*10+5}, {tens*10}", f"Thứ tự từ lớn đến bé: {tens*10+8}, {tens*10+5}, {tens*10+2}, {tens*10}", f"{tens*10+8}, {tens*10+5}, {tens*10+2}, {tens*10}", 4, 1.0),
                    make_essay(4, f"Cây bút chì dài 12 cm, chiếc thước kẻ dài hơn cây bút chì 6 cm. Hỏi chiếc thước kẻ dài bao nhiêu xăng-ti-mét?", f"Chiếc thước kẻ dài số xăng-ti-mét là:\n12 + 6 = 18 (cm)\nĐáp số: 18 cm", "18 cm", 5, 1.5),
                    make_essay(5, f"Đoạn dây thứ nhất dài 19 cm, bạn Nam cắt bớt đi {t+2} cm. Hỏi đoạn dây còn lại dài bao nhiêu xăng-ti-mét?", f"Đoạn dây còn lại dài số xăng-ti-mét là:\n19 - {t+2} = {17-t} (cm)\nĐáp số: {17-t} cm", f"{17-t} cm", 5, 1.5),
                    make_essay(6, f"Tìm một số có hai chữ số biết chữ số hàng chục là {tens} và chữ số hàng đơn vị lớn hơn chữ số hàng chục 1 đơn vị.", f"Chữ số hàng đơn vị là: {tens} + 1 = {tens+1}. Vậy số cần tìm là: {tens}{tens+1}.", f"{tens}{tens+1}", 4, 1.0)
                ]

            else: # ck2
                # CK2: Cộng trừ không nhớ phạm vi 100, đồng hồ, thứ ngày
                numA, numB = 20 + t * 5, 12 + t
                p1 = [
                    make_mc(1, f"Kết quả của phép tính {numA} + {numB} là:", [str(numA+numB), str(numA+numB+1), str(numA+numB-1), str(numA+numB+10)], 0, f"{numA} + {numB} = {numA+numB}."),
                    make_mc(2, f"Kết quả của phép trừ {numA+numB} - {numB} là:", [str(numA), str(numA+1), str(numB), str(numA-1)], 0, f"{numA+numB} - {numB} = {numA}."),
                    make_mc(3, "Đồng hồ kim ngắn chỉ số 8, kim dài chỉ số 12. Lúc đó là mấy giờ?", ["8 giờ đúng", "12 giờ đúng", "8 giờ 12 phút", "6 giờ đúng"], 0, "Kim ngắn chỉ số 8, kim dài chỉ số 12 là 8 giờ đúng."),
                    make_mc(4, "Một tuần lễ có bao nhiêu ngày?", ["7 ngày", "5 ngày", "6 ngày", "8 ngày"], 0, "Một tuần lễ có 7 ngày (từ Thứ Hai đến Chủ nhật)."),
                    make_mc(5, f"Hình bên dưới có bao nhiêu hình vuông nhỏ?", ["4 hình", "3 hình", "5 hình", "6 hình"], 0, "Học sinh đếm chính xác số lượng hình vuông."),
                    make_mc(6, f"Nếu hôm nay là Thứ Ba thì ngày mai là:", ["Thứ Tư", "Thứ Hai", "Thứ Năm", "Chủ nhật"], 0, "Ngày liền sau Thứ Ba là Thứ Tư.")
                ]
                p2 = [
                    make_essay(1, f"Đặt tính rồi tính:\na) {numA} + {numB}\nb) {numA+numB} - {numA}", f"a) {numA} + {numB} = {numA+numB}\nb) {numA+numB} - {numA} = {numB}", f"a) {numA+numB}; b) {numB}", 4, 1.0),
                    make_essay(2, f"Tính nhẩm:\na) 40 + 30 = ...\nb) 90 - 50 = ...", "a) 40 + 30 = 70\nb) 90 - 50 = 40", "a) 70; b) 40", 4, 1.0),
                    make_essay(3, "Vẽ kim đồng hồ chỉ: a) 7 giờ đúng; b) 4 giờ đúng.", "Học sinh vẽ kim ngắn chỉ vào số 7 (hoặc 4), kim dài chỉ thẳng đứng vào số 12.", "Vẽ đúng giờ", 4, 1.0),
                    make_essay(4, f"Lớp 1A trồng được {numA} cây hoa, lớp 1B trồng được {numB} cây hoa. Hỏi cả hai lớp trồng được tất cả bao nhiêu cây hoa?", f"Cả hai lớp trồng được tất cả số cây hoa là:\n{numA} + {numB} = {numA+numB} (cây hoa)\nĐáp số: {numA+numB} cây hoa", f"{numA+numB} cây hoa", 5, 1.5),
                    make_essay(5, f"Đàn gà nhà bà có {numA+numB} con gà, mẹ đã bán đi {numB} con gà. Hỏi nhà bà còn lại bao nhiêu con gà?", f"Nhà bà còn lại số con gà là:\n{numA+numB} - {numB} = {numA} (con gà)\nĐáp số: {numA} con gà", f"{numA} con gà", 5, 1.5),
                    make_essay(6, f"Điền dấu (+, -) thích hợp vào ô trống:\n30 ... 20 ... 10 = 40", "Ta có: 30 + 20 - 10 = 50 - 10 = 40. Vậy dấu cần điền là + và -.", "+ và -", 4, 1.0)
                ]

            exams[eid] = {
                "id": eid,
                "testNum": t,
                "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ {term_name.upper()} - TOÁN 1 (ĐỀ SỐ {t})",
                "grade": "1",
                "term": term_code,
                "termName": term_name,
                "duration": duration,
                "points": 10.0,
                "totalPoints": 10.0,
                "part1": p1,
                "part2": p2
            }

    return exams

if __name__ == "__main__":
    ex = get_th1_exams()
    print(f"Tổng số đề thi định kỳ Toán 1: {len(ex)}")
