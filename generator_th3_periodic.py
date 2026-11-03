# -*- coding: utf-8 -*-
"""
HỆ THỐNG ĐỀ KIỂM TRA ĐỊNH KỲ TOÁN LỚP 3 (BỘ KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
Bao gồm 32 đề kiểm tra chuẩn hóa độc lập:
- 8 đề Giữa học kì 1 (th3_gk1_de01 -> th3_gk1_de08)
- 8 đề Cuối học kì 1 (th3_ck1_de01 -> th3_ck1_de08)
- 8 đề Giữa học kì 2 (th3_gk2_de01 -> th3_gk2_de08)
- 8 đề Cuối học kì 2 (th3_ck2_de01 -> th3_ck2_de08)
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

def get_th3_exams():
    exams = {}

    terms = [
        ("gk1", "Giữa Học kì 1", "40 phút"),
        ("ck1", "Cuối Học kì 1", "40 phút"),
        ("gk2", "Giữa Học kì 2", "40 phút"),
        ("ck2", "Cuối Học kì 2", "40 phút")
    ]

    for term_code, term_name, duration in terms:
        for t in range(1, 9):
            eid = f"th3_{term_code}_de{t:02d}"

            if term_code == "gk1":
                # GK1 Lớp 3: Bảng cửu chương 3-9, gấp giảm lần, góc vuông
                k = 6 + (t % 4)
                p1 = [
                    make_mc(1, f"Tính nhẩm: 7 x {t % 4 + 4} = ?", [str(7*(t % 4 + 4)), str(7*(t % 4 + 4)+7), str(7*(t % 4 + 4)-7), "35"], 0, f"7 x {t % 4 + 4} = {7*(t % 4 + 4)}."),
                    make_mc(2, f"Kết quả phép chia 54 : 6 là:", ["9", "8", "7", "6"], 0, "54 : 6 = 9 vì 6 x 9 = 54."),
                    make_mc(3, f"Số {k} gấp lên 4 lần thì được:", [str(k*4), str(k+4), str(k*3), str(k*5)], 0, f"{k} x 4 = {k*4}."),
                    make_mc(4, f"Số 36 giảm đi 6 lần thì được:", ["6", "30", "9", "4"], 0, "36 : 6 = 6."),
                    make_mc(5, "Để kiểm tra một góc có phải là góc vuông hay không, ta dùng dụng cụ nào?", ["Thước ê-ke", "Thước dây", "Cân đồng hồ", "Nhiệt kế"], 0, "Dùng thước ê-ke để kiểm tra góc vuông."),
                    make_mc(6, "Một hình tam giác có độ dài các cạnh lần lượt là 6 cm, 8 cm, 10 cm. Chu vi của tam giác đó là:", ["24 cm", "18 cm", "20 cm", "28 cm"], 0, "Chu vi tam giác: 6 + 8 + 10 = 24 cm.")
                ]
                p2 = [
                    make_essay(1, f"Tính giá trị biểu thức:\na) 8 x 6 + 25\nb) 72 : 9 x 4", "a) 8 x 6 + 25 = 48 + 25 = 73\nb) 72 : 9 x 4 = 8 x 4 = 32", "a) 73; b) 32", 4, 1.0),
                    make_essay(2, f"Tìm x:\na) x x 7 = 56\nb) x : 8 = {t % 4 + 3}", f"a) x = 56 : 7 = 8\nb) x = {t % 4 + 3} x 8 = {(t % 4 + 3)*8}", f"a) x = 8; b) x = {(t % 4 + 3)*8}", 4, 1.0),
                    make_essay(3, "Nêu tên đỉnh và các cạnh tạo thành góc vuông trong hình chữ nhật ABCD.", "Trong hình chữ nhật ABCD, có 4 góc vuông tại các đỉnh A, B, C, D.", "4 góc vuông tại A, B, C, D", 4, 1.0),
                    make_essay(4, f"Đoàn có {t*4+16} bạn học sinh xếp đều thành 4 hàng. Hỏi mỗi hàng có bao nhiêu bạn học sinh?", f"Mỗi hàng có số bạn học sinh là:\n{t*4+16} : 4 = {t+4} (học sinh)\nĐáp số: {t+4} học sinh", f"{t+4} học sinh", 5, 1.5),
                    make_essay(5, f"Một cuộn dây thừng dài 48 m, người ta cắt lấy một đoạn bằng 1/6 độ dài cuộn dây. Hỏi đoạn dây đã cắt dài bao nhiêu mét?", f"Đoạn dây đã cắt dài số mét là:\n48 : 6 = 8 (m)\nĐáp số: 8 m", "8 m", 5, 1.5),
                    make_essay(6, f"Tìm một số biết rằng nếu giảm số đó đi 5 lần rồi cộng thêm 12 thì được 18.", "Số đó sau khi giảm 5 lần là: 18 - 12 = 6.\nSố cần tìm là: 6 x 5 = 30.", "30", 4, 1.0)
                ]

            elif term_code == "ck1":
                # CK1 Lớp 3: Nhân chia số 2-3 chữ số, gam, ml, hình tròn
                mA = 124 + t * 2
                p1 = [
                    make_mc(1, f"Tính: {mA} x 3 = ?", [str(mA*3), str(mA*3+2), str(mA*3-2), str(mA*3+10)], 0, f"{mA} x 3 = {mA*3}."),
                    make_mc(2, f"Tính: {mA*4} : 4 = ?", [str(mA), str(mA+1), str(mA-1), str(mA*2)], 0, f"{mA*4} : 4 = {mA}."),
                    make_mc(3, "Đổi: 1 kg bằng bao nhiêu gam?", ["1000 g", "100 g", "10 g", "10 000 g"], 0, "1 kg = 1000 g."),
                    make_mc(4, "Một chai nước khoáng có dung tích 500 ml. Hai chai nước khoáng như thế có dung tích là:", ["1 000 ml hay 1 lít", "100 ml", "750 ml", "2 lít"], 0, "500 x 2 = 1000 ml = 1 l."),
                    make_mc(5, "Trong một hình tròn, độ dài đường kính gấp mấy lần độ dài bán kính?", ["2 lần", "3 lần", "4 lần", "Bằng nhau"], 0, "Đường kính = 2 x bán kính."),
                    make_mc(6, "Nhiệt độ nước đá đang tan là khoảng bao nhiêu độ C?", ["0 độ C", "100 độ C", "37 độ C", "20 độ C"], 0, "Nước đá tan ở 0 độ C.")
                ]
                p2 = [
                    make_essay(1, f"Đặt tính rồi tính:\na) {mA} x 4\nb) 848 : 4", f"a) {mA} x 4 = {mA*4}\nb) 848 : 4 = 212", f"a) {mA*4}; b) 212", 4, 1.0),
                    make_essay(2, f"Tính giá trị biểu thức:\na) (150 + 250) : 5\nb) 240 - 40 x 3", "a) (150 + 250) : 5 = 400 : 5 = 80\nb) 240 - 120 = 120", "a) 80; b) 120", 4, 1.0),
                    make_essay(3, "Cho hình tròn tâm O có bán kính r = 6 cm. Tính độ dài đường kính của hình tròn đó.", "Độ dài đường kính của hình tròn là:\n6 x 2 = 12 (cm)\nĐáp số: 12 cm", "12 cm", 4, 1.0),
                    make_essay(4, f"Một cửa hàng nhập về {3*mA} hộp bánh chia đều vào 3 thùng lớn. Hỏi mỗi thùng lớn có bao nhiêu hộp bánh?", f"Mỗi thùng lớn có số hộp bánh là:\n{3*mA} : 3 = {mA} (hộp bánh)\nĐáp số: {mA} hộp bánh", f"{mA} hộp bánh", 5, 1.5),
                    make_essay(5, f"Mẹ mua 500 g thịt nạc và {t*50+200} g tôm tươi. Hỏi mẹ đã mua tất cả bao nhiêu gam thực phẩm?", f"Mẹ đã mua tất cả số gam thực phẩm là:\n500 + {t*50+200} = {700+t*50} (g)\nĐáp số: {700+t*50} g", f"{700+t*50} g", 5, 1.5),
                    make_essay(6, f"Một người mang 90 quả trứng đi chợ bán. Buổi sáng bán được 1/3 số trứng đó. Hỏi người đó còn lại bao nhiêu quả trứng?", "Số trứng bán buổi sáng là: 90 : 3 = 30 (quả).\nSố trứng còn lại là: 90 - 30 = 60 (quả).\nĐáp số: 60 quả trứng.", "60 quả", 4, 1.0)
                ]

            elif term_code == "gk2":
                # GK2 Lớp 3: Số đến 10 000, cộng trừ 10 000, chu vi hình chữ nhật, hình vuông
                uA, uB = 2450 + t * 100, 1320 + t * 50
                p1 = [
                    make_mc(1, f"Số gồm 6 nghìn, 4 trăm và 5 đơn vị viết là:", ["6 405", "6 450", "6 045", "6 540"], 0, "6 nghìn, 4 trăm, 0 chục, 5 đơn vị = 6 405."),
                    make_mc(2, f"Tính: {uA} + {uB} = ?", [str(uA+uB), str(uA+uB+10), str(uA+uB-10), str(uA+uB+100)], 0, f"{uA} + {uB} = {uA+uB}."),
                    make_mc(3, f"Số lớn nhất trong các số: 5 432, 5 423, 5 439, 5 399 là:", ["5 439", "5 432", "5 423", "5 399"], 0, "5 439 là số lớn nhất."),
                    make_mc(4, "Một hình vuông có cạnh dài 8 cm. Chu vi của hình vuông đó là:", ["32 cm", "16 cm", "64 cm", "24 cm"], 0, "Chu vi hình vuông = 8 x 4 = 32 cm."),
                    make_mc(5, "Một hình chữ nhật có chiều dài 12 cm, chiều rộng 8 cm. Chu vi hình chữ nhật là:", ["40 cm", "20 cm", "96 cm", "24 cm"], 0, "Chu vi = (12 + 8) x 2 = 40 cm."),
                    make_mc(6, "Tháng có 31 ngày trong năm là:", ["Tháng 1", "Tháng 4", "Tháng 6", "Tháng 9"], 0, "Tháng 1 có 31 ngày.")
                ]
                p2 = [
                    make_essay(1, f"Đặt tính rồi tính:\na) {uA} + {uB}\nb) {uA+uB} - {uA}", f"a) {uA} + {uB} = {uA+uB}\nb) {uA+uB} - {uA} = {uB}", f"a) {uA+uB}; b) {uB}", 4, 1.0),
                    make_essay(2, f"Tính giá trị biểu thức:\na) 4 000 + 2 500 - 1 200\nb) 1 500 x 3 - 2 000", "a) 6 500 - 1 200 = 5 300\nb) 4 500 - 2 000 = 2 500", "a) 5 300; b) 2 500", 4, 1.0),
                    make_essay(3, "Một mảnh đất hình chữ nhật có chiều dài 25 m, chiều rộng 15 m. Tính chu vi mảnh đất đó.", "Chu vi mảnh đất hình chữ nhật là:\n(25 + 15) x 2 = 80 (m)\nĐáp số: 80 m", "80 m", 4, 1.0),
                    make_essay(4, f"Một kho thóc có {uA} kg thóc, người ta nhập thêm {uB} kg thóc nữa. Sau đó xuất đi 1 500 kg. Hỏi trong kho còn lại bao nhiêu ki-lô-gam thóc?", f"Tổng số thóc trong kho sau khi nhập là:\n{uA} + {uB} = {uA+uB} (kg)\nTrong kho còn lại số thóc là:\n{uA+uB} - 1 500 = {uA+uB-1500} (kg)\nĐáp số: {uA+uB-1500} kg", f"{uA+uB-1500} kg", 5, 1.5),
                    make_essay(5, f"Một sân chơi hình vuông có cạnh dài {t*5+20} m. Người ta trồng cọc rào xung quanh, biết chu vi của sân chơi là bao nhiêu mét?", f"Chu vi sân chơi hình vuông là:\n{t*5+20} x 4 = {(t*5+20)*4} (m)\nĐáp số: {(t*5+20)*4} m", f"{(t*5+20)*4} m", 5, 1.5),
                    make_essay(6, f"Tìm x, biết: x - 2 400 = 3 600 : 3", "x - 2 400 = 1 200\nx = 1 200 + 2 400 = 3 600", "3 600", 4, 1.0)
                ]

            else: # ck2
                # CK2 Lớp 3: Số đến 100 000, diện tích hình chữ nhật/vuông, tiền VN
                wA = 35000 + t * 2000
                p1 = [
                    make_mc(1, f"Số liền sau của số 49 999 là:", ["50 000", "49 998", "49 900", "59 999"], 0, "Số liền sau của 49 999 là 50 000."),
                    make_mc(2, f"Tính: 20 000 + 30 000 = ?", ["50 000", "60 000", "40 000", "5 000"], 0, "20 000 + 30 000 = 50 000."),
                    make_mc(3, "Một hình vuông có cạnh dài 6 cm. Diện tích của hình vuông đó là:", ["36 cm²", "24 cm²", "12 cm²", "18 cm²"], 0, "Diện tích = 6 x 6 = 36 cm²."),
                    make_mc(4, "Một hình chữ nhật có chiều dài 9 cm, chiều rộng 5 cm. Diện tích của hình chữ nhật là:", ["45 cm²", "28 cm²", "14 cm²", "40 cm²"], 0, "Diện tích = 9 x 5 = 45 cm²."),
                    make_mc(5, "Bạn Minh mua 2 quyển vở, mỗi quyển giá 8 000 đồng. Minh đưa cô bán hàng tờ 20 000 đồng. Cô bán hàng trả lại Minh số tiền là:", ["4 000 đồng", "5 000 đồng", "6 000 đồng", "2 000 đồng"], 0, "2 quyển vở giá: 16 000 đồng. Trả lại: 20 000 - 16 000 = 4 000 đồng."),
                    make_mc(6, "Khả năng xảy ra khi tung một đồng xu là:", ["Có thể xuất hiện mặt sấp hoặc mặt ngửa", "Chắc chắn xuất hiện mặt sấp", "Không bao giờ xuất hiện mặt ngửa", "Không thể xác định"], 0, "Đồng xu có 2 mặt nên có thể ra mặt sấp hoặc mặt ngửa.")
                ]
                p2 = [
                    make_essay(1, f"Đặt tính rồi tính:\na) {wA} + 18 500\nb) 72 600 - 35 200", f"a) {wA} + 18 500 = {wA+18500}\nb) 72 600 - 35 200 = 37 400", f"a) {wA+18500}; b) 37 400", 4, 1.0),
                    make_essay(2, f"Tính giá trị biểu thức:\na) 12 000 x 3 + 14 000\nb) (45 000 - 15 000) : 3", "a) 36 000 + 14 000 = 50 000\nb) 30 000 : 3 = 10 000", "a) 50 000; b) 10 000", 4, 1.0),
                    make_essay(3, "Một tấm bìa hình chữ nhật có chiều dài 18 cm, chiều rộng 10 cm. Tính diện tích tấm bìa đó.", "Diện tích tấm bìa hình chữ nhật là:\n18 x 10 = 180 (cm²)\nĐáp số: 180 cm²", "180 cm²", 4, 1.0),
                    make_essay(4, f"Một cửa hàng ngày thứ nhất bán được {12000+t*1000} lít xăng, ngày thứ hai bán được gấp đôi ngày thứ nhất. Hỏi cả hai ngày cửa hàng bán được bao nhiêu lít xăng?", f"Ngày thứ hai cửa hàng bán được số lít xăng là:\n{12000+t*1000} x 2 = {(12000+t*1000)*2} (lít)\nCả hai ngày cửa hàng bán được số lít xăng là:\n{12000+t*1000} + {(12000+t*1000)*2} = {(12000+t*1000)*3} (lít)\nĐáp số: {(12000+t*1000)*3} lít", f"{(12000+t*1000)*3} lít", 5, 1.5),
                    make_essay(5, f"Một căn phòng hình vuông có cạnh dài {t+4} m. Tính chu vi và diện tích căn phòng đó.", f"Chu vi căn phòng hình vuông là:\n{t+4} x 4 = {(t+4)*4} (m)\nDiện tích căn phòng là:\n{t+4} x {t+4} = {(t+4)*(t+4)} (m²)\nĐáp số: Chu vi: {(t+4)*4} m; Diện tích: {(t+4)*(t+4)} m²", f"Chu vi: {(t+4)*4} m; Diện tích: {(t+4)*(t+4)} m²", 6, 1.5),
                    make_essay(6, f"Tìm y, biết: y x 4 = 48 000 - 8 000", "y x 4 = 40 000\ny = 40 000 : 4 = 10 000", "10 000", 4, 1.0)
                ]

            exams[eid] = {
                "id": eid,
                "testNum": t,
                "title": f"ĐỀ KIỂM TRA ĐỊNH KỲ {term_name.upper()} - TOÁN 3 (ĐỀ SỐ {t})",
                "grade": "3",
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
    ex = get_th3_exams()
    print(f"Tổng số đề thi định kỳ Toán 3: {len(ex)}")
