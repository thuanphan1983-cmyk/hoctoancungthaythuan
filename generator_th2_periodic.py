# -*- coding: utf-8 -*-
"""
HỆ THỐNG ĐỀ KIỂM TRA ĐỊNH KỲ TOÁN LỚP 2 (BỘ KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
Bao gồm 32 đề kiểm tra chuẩn hóa độc lập:
- 8 đề Giữa học kì 1 (th2_gk1_de01 -> th2_gk1_de08)
- 8 đề Cuối học kì 1 (th2_ck1_de01 -> th2_ck1_de08)
- 8 đề Giữa học kì 2 (th2_gk2_de01 -> th2_gk2_de08)
- 8 đề Cuối học kì 2 (th2_ck2_de01 -> th2_ck2_de08)
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

def get_th2_exams():
    exams = {}

    terms = [
        ("gk1", "Giữa Học kì 1", "35 phút"),
        ("ck1", "Cuối Học kì 1", "35 phút"),
        ("gk2", "Giữa Học kì 2", "35 phút"),
        ("ck2", "Cuối Học kì 2", "35 phút")
    ]

    for term_code, term_name, duration in terms:
        for t in range(1, 9):
            eid = f"th2_{term_code}_de{t:02d}"

            if term_code == "gk1":
                # GK1 Lớp 2: Số đến 100, cộng trừ qua 10 phạm vi 20, dm
                x, y = 7 + (t % 3), 5 + (t % 4)
                p1 = [
                    make_mc(1, f"Số liền trước của số {40+t} là số:", [str(39+t), str(41+t), str(40+t), str(38+t)], 0, f"Số liền trước của {40+t} là {39+t}."),
                    make_mc(2, f"Tính nhẩm: {x} + {y} = ?", [str(x+y), str(x+y+1), str(x+y-1), str(x+y+2)], 0, f"{x} + {y} = {x+y}."),
                    make_mc(3, f"Kết quả của phép trừ 15 - {y} là:", [str(15-y), str(15-y+1), str(15-y-1), str(y)], 0, f"15 - {y} = {15-y}."),
                    make_mc(4, "Đổi: 1 dm bằng bao nhiêu xăng-ti-mét?", ["10 cm", "100 cm", "1 cm", "20 cm"], 0, "1 dm = 10 cm."),
                    make_mc(5, f"Số hạng thứ nhất là {20+t}, số hạng thứ hai là 15. Tổng là:", [str(35+t), str(34+t), str(36+t), str(25+t)], 0, f"Tổng = {20+t} + 15 = {35+t}."),
                    make_mc(6, "Ba điểm thẳng hàng là ba điểm:", ["Cùng nằm trên một đường thẳng", "Nằm ở ba vị trí bất kì", "Tạo thành một tam giác", "Nằm trên một đường cong"], 0, "Ba điểm cùng nằm trên một đường thẳng gọi là ba điểm thẳng hàng.")
                ]
                p2 = [
                    make_essay(1, f"Tính nhẩm:\na) 9 + {t % 4 + 4}\nb) 14 - {t % 3 + 5}", f"a) 9 + {t % 4 + 4} = {9 + (t % 4 + 4)}\nb) 14 - {t % 3 + 5} = {14 - (t % 3 + 5)}", f"a) {9 + (t % 4 + 4)}; b) {14 - (t % 3 + 5)}", 4, 1.0),
                    make_essay(2, f"Đổi đơn vị đo:\na) {t+2} dm = ... cm\nb) {t*10+20} cm = ... dm", f"a) {t+2} dm = {(t+2)*10} cm\nb) {t*10+20} cm = {t+2} dm", f"a) {(t+2)*10} cm; b) {t+2} dm", 4, 1.0),
                    make_essay(3, f"Tìm x:\na) x - {x} = 9\nb) 16 - x = {y}", f"a) x = 9 + {x} = {9+x}\nb) x = 16 - {y} = {16-y}", f"a) x = {9+x}; b) x = {16-y}", 4, 1.0),
                    make_essay(4, f"Bác nông dân thu hoạch được {30+t*5} bắp ngô nếp và 25 bắp ngô tẻ. Hỏi bác thu hoạch được tất cả bao nhiêu bắp ngô?", f"Bác thu hoạch được tất cả số bắp ngô là:\n{30+t*5} + 25 = {55+t*5} (bắp ngô)\nĐáp số: {55+t*5} bắp ngô", f"{55+t*5} bắp ngô", 5, 1.5),
                    make_essay(5, f"Một cửa hàng có {50+t*4} quyển vở, đã bán được 28 quyển. Hỏi cửa hàng còn lại bao nhiêu quyển vở?", f"Cửa hàng còn lại số quyển vở là:\n{50+t*4} - 28 = {22+t*4} (quyển vở)\nĐáp số: {22+t*4} quyển vở", f"{22+t*4} quyển vở", 5, 1.5),
                    make_essay(6, f"Điền số thích hợp vào ô trống: 8 + ... = 15 - 2", "Ta có: 15 - 2 = 13. Vậy 8 + 5 = 13. Số cần điền là 5.", "5", 4, 1.0)
                ]

            elif term_code == "ck1":
                # CK1 Lớp 2: Cộng trừ có nhớ phạm vi 100, kg, lít, đường gấp khúc, ngày giờ
                nA, nB = 38 + t * 2, 27 + t
                p1 = [
                    make_mc(1, f"Đặt tính rồi tính: {nA} + {nB} = ?", [str(nA+nB), str(nA+nB-1), str(nA+nB+1), str(nA+nB+10)], 0, f"{nA} + {nB} = {nA+nB}."),
                    make_mc(2, f"Kết quả của phép trừ {nA+nB} - {nB} là:", [str(nA), str(nA+1), str(nA-1), str(nB)], 0, f"{nA+nB} - {nB} = {nA}."),
                    make_mc(3, "Bao gạo cân nặng 25 kg, bao ngô nặng hơn bao gạo 8 kg. Bao ngô cân nặng là:", ["33 kg", "17 kg", "30 kg", "35 kg"], 0, "Bao ngô nặng: 25 + 8 = 33 kg."),
                    make_mc(4, "Một can chứa được 10 lít nước. Sau khi rót ra 4 lít thì trong can còn lại:", ["6 lít", "14 lít", "5 lít", "7 lít"], 0, "10 - 4 = 6 lít."),
                    make_mc(5, "Đường gấp khúc gồm 3 đoạn thẳng có độ dài lần lượt là 4 cm, 6 cm và 5 cm. Độ dài đường gấp khúc là:", ["15 cm", "14 cm", "16 cm", "10 cm"], 0, "4 + 6 + 5 = 15 cm."),
                    make_mc(6, "Buổi chiều lúc 4 giờ còn được gọi là mấy giờ trong ngày?", ["16 giờ", "14 giờ", "15 giờ", "17 giờ"], 0, "4 giờ chiều = 12 + 4 = 16 giờ.")
                ]
                p2 = [
                    make_essay(1, f"Đặt tính rồi tính:\na) {nA} + {nB}\nb) {nA+nB} - {nA}", f"a) {nA} + {nB} = {nA+nB}\nb) {nA+nB} - {nA} = {nB}", f"a) {nA+nB}; b) {nB}", 4, 1.0),
                    make_essay(2, f"Tính:\na) 45 kg + {15+t} kg\nb) 60 l - {20+t*2} l", f"a) 45 kg + {15+t} kg = {60+t} kg\nb) 60 l - {20+t*2} l = {40-t*2} l", f"a) {60+t} kg; b) {40-t*2} l", 4, 1.0),
                    make_essay(3, "Tính độ dài đường gấp khúc MNPQ có độ dài các đoạn thẳng: MN = 12 cm, NP = 15 cm, PQ = 18 cm.", "Độ dài đường gấp khúc MNPQ là:\n12 + 15 + 18 = 45 (cm)\nĐáp số: 45 cm", "45 cm", 4, 1.0),
                    make_essay(4, f"Đội Một trồng được {45+t*3} cây xanh, đội Hai trồng được nhiều hơn đội Một 18 cây. Hỏi đội Hai trồng được bao nhiêu cây xanh?", f"Đội Hai trồng được số cây xanh là:\n{45+t*3} + 18 = {63+t*3} (cây)\nĐáp số: {63+t*3} cây xanh", f"{63+t*3} cây", 5, 1.5),
                    make_essay(5, f"Một cuộn dây điện dài 95 m, người thợ đã dùng hết {35+t*5} m. Hỏi cuộn dây điện còn lại bao nhiêu mét?", f"Cuộn dây điện còn lại số mét là:\n95 - {35+t*5} = {60-t*5} (m)\nĐáp số: {60-t*5} m", f"{60-t*5} m", 5, 1.5),
                    make_essay(6, f"Tìm một số biết rằng lấy số đó cộng với 26 thì được 80.", "Số cần tìm là: 80 - 26 = 54.", "54", 4, 1.0)
                ]

            elif term_code == "gk2":
                # GK2 Lớp 2: Bảng nhân chia 2, 5; số đến 1000
                p1 = [
                    make_mc(1, f"Kết quả của phép nhân 2 x {t+1} là:", [str(2*(t+1)), str(2*(t+1)+1), str(2*(t+1)-1), str(t+1)], 0, f"2 x {t+1} = {2*(t+1)}."),
                    make_mc(2, f"Tính: 5 x {t % 5 + 3} = ?", [str(5*(t % 5 + 3)), str(5*(t % 5 + 3)+5), str(5*(t % 5 + 3)-5), "15"], 0, f"5 x {t % 5 + 3} = {5*(t % 5 + 3)}."),
                    make_mc(3, f"Số thích hợp điền vào chỗ chấm: {2*(t+2)} : 2 = ...", [str(t+2), str(t+1), str(t+3), "2"], 0, f"{2*(t+2)} : 2 = {t+2}."),
                    make_mc(4, "Khối nào dưới đây có thể lăn được về mọi phía?", ["Khối cầu", "Khối trụ", "Khối lập phương", "Khối hộp chữ nhật"], 0, "Khối cầu tròn đều có thể lăn về mọi hướng."),
                    make_mc(5, f"Số gồm 5 trăm, 3 chục và 8 đơn vị viết là:", ["538", "583", "358", "853"], 0, "Số gồm 5 trăm, 3 chục, 8 đơn vị là 538."),
                    make_mc(6, f"Số lớn nhất có 3 chữ số khác nhau là:", ["987", "999", "989", "897"], 0, "Số lớn nhất có 3 chữ số khác nhau là 987.")
                ]
                p2 = [
                    make_essay(1, f"Tính nhẩm:\na) 2 x 8 = ...\nb) 5 x 7 = ...\nc) 18 : 2 = ...\nd) 35 : 5 = ...", "a) 2 x 8 = 16\nb) 5 x 7 = 35\nc) 18 : 2 = 9\nd) 35 : 5 = 7", "16, 35, 9, 7", 4, 1.0),
                    make_essay(2, f"Viết các số sau thành tổng các trăm, chục, đơn vị:\na) 645\nb) {t*100+38}", f"a) 645 = 600 + 40 + 5\nb) {t*100+38} = {t*100} + 30 + 8", f"a) 600+40+5; b) {t*100}+30+8", 4, 1.0),
                    make_essay(3, f"So sánh các số sau (> , < , =):\na) 450 ... 405\nb) {t*100+50} ... {t*100+55}", f"a) 450 > 405\nb) {t*100+50} < {t*100+55}", "a) >; b) <", 4, 1.0),
                    make_essay(4, f"Mỗi bàn học có 2 bạn học sinh ngồi. Hỏi {t+4} bàn học như thế có tất cả bao nhiêu bạn học sinh?", f"{t+4} bàn học có tất cả số bạn học sinh là:\n2 x {t+4} = {2*(t+4)} (học sinh)\nĐáp số: {2*(t+4)} học sinh", f"{2*(t+4)} học sinh", 5, 1.5),
                    make_essay(5, f"Có {5*(t+2)} quyển vở chia đều cho 5 bạn học sinh giỏi. Hỏi mỗi bạn nhận được bao nhiêu quyển vở?", f"Mỗi bạn nhận được số quyển vở là:\n{5*(t+2)} : 5 = {t+2} (quyển vở)\nĐáp số: {t+2} quyển vở", f"{t+2} quyển vở", 5, 1.5),
                    make_essay(6, f"Tìm y, biết: y x 2 = {16+t*2 - (t%2)*2}", f"y = {16+t*2 - (t%2)*2} : 2 = {(16+t*2 - (t%2)*2)//2}", str((16+t*2 - (t%2)*2)//2), 4, 1.0)
                ]

            else: # ck2
                # CK2 Lớp 2: Cộng trừ phạm vi 1000, m, km, tiền VN
                vA, vB = 320 + t * 20, 145 + t * 5
                p1 = [
                    make_mc(1, f"Tính: {vA} + {vB} = ?", [str(vA+vB), str(vA+vB+10), str(vA+vB-10), str(vA+vB+100)], 0, f"{vA} + {vB} = {vA+vB}."),
                    make_mc(2, f"Tính: {vA+vB} - {vB} = ?", [str(vA), str(vA+10), str(vA-10), str(vB)], 0, f"{vA+vB} - {vB} = {vA}."),
                    make_mc(3, "Đổi: 1 mét bằng bao nhiêu xăng-ti-mét?", ["100 cm", "10 cm", "1000 cm", "1 cm"], 0, "1 m = 100 cm."),
                    make_mc(4, "Khoảng cách từ Hà Nội đến Thành phố Hồ Chí Minh thường đo bằng đơn vị nào?", ["Ki-lô-mét (km)", "Mét (m)", "Xăng-ti-mét (cm)", "Đề-xi-mét (dm)"], 0, "Khoảng cách đường dài đo bằng ki-lô-mét (km)."),
                    make_mc(5, "Mẹ mua một chiếc bút chì giá 3 000 đồng và một cục tẩy giá 2 000 đồng. Mẹ phải trả tất cả:", ["5 000 đồng", "6 000 đồng", "4 000 đồng", "1 000 đồng"], 0, "3000 + 2000 = 5000 đồng."),
                    make_mc(6, "Số tròn trăm lớn nhất có 3 chữ số là:", ["900", "999", "1000", "800"], 0, "Số tròn trăm lớn nhất có 3 chữ số là 900.")
                ]
                p2 = [
                    make_essay(1, f"Đặt tính rồi tính:\na) {vA} + {vB}\nb) {vA+vB} - {vA}", f"a) {vA} + {vB} = {vA+vB}\nb) {vA+vB} - {vA} = {vB}", f"a) {vA+vB}; b) {vB}", 4, 1.0),
                    make_essay(2, f"Tính giá trị biểu thức:\na) 200 + 300 + 150 = ...\nb) 800 - 300 - 200 = ...", "a) 200 + 300 + 150 = 650\nb) 800 - 300 - 200 = 300", "a) 650; b) 300", 4, 1.0),
                    make_essay(3, "Bác Ba có 1 tờ 5 000 đồng và 2 tờ 2 000 đồng. Hỏi bác Ba có tất cả bao nhiêu tiền?", "Bác Ba có tất cả số tiền là:\n5 000 + 2 000 + 2 000 = 9 000 (đồng)\nĐáp số: 9 000 đồng", "9 000 đồng", 4, 1.0),
                    make_essay(4, f"Quãng đường từ nhà An đến trường dài 450 m, quãng đường từ trường đến nhà sách dài {200+t*10} m. Hỏi quãng đường từ nhà An qua trường rồi đến nhà sách dài tất cả bao nhiêu mét?", f"Quãng đường dài tất cả là:\n450 + {200+t*10} = {650+t*10} (m)\nĐáp số: {650+t*10} m", f"{650+t*10} m", 5, 1.5),
                    make_essay(5, f"Một nông trường nuôi {500+t*20} con bò sữa, đã bán đi 180 con. Hỏi nông trường còn lại bao nhiêu con bò sữa?", f"Nông trường còn lại số con bò sữa là:\n{500+t*20} - 180 = {320+t*20} (con bò)\nĐáp số: {320+t*20} con bò sữa", f"{320+t*20} con", 5, 1.5),
                    make_essay(6, f"Tìm một số có 3 chữ số biết chữ số hàng trăm là 4, chữ số hàng chục gấp đôi chữ số hàng trăm, và chữ số hàng đơn vị là 1.", "Chữ số hàng chục là: 4 x 2 = 8. Vậy số cần tìm là 481.", "481", 4, 1.0)
                ]

            exams[eid] = {
                "id": eid,
                "testNum": t,
                "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ {term_name.upper()} - TOÁN 2 (ĐỀ SỐ {t})",
                "grade": "2",
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
    ex = get_th2_exams()
    print(f"Tổng số đề thi định kỳ Toán 2: {len(ex)}")
