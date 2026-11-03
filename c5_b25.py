# -*- coding: utf-8 -*-
# c5_b25.py - Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế (3 đề độc lập 100%)
import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {"id": qid, "level": level, "question": q_text, "options": options, "correct": correct_idx, "explanation": explanation}

def make_tf(qid, level, prompt, statements, explanation=""):
    return {"id": qid, "level": level, "question": prompt, "statements": [{"subId": s[0], "text": s[1], "correct": s[2]} for s in statements], "explanation": explanation}

def make_sa(qid, level, q_text, answer, explanation=""):
    return {"id": qid, "level": level, "question": q_text, "correctAnswer": str(answer).strip(), "explanation": explanation}

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {"id": qid, "level": "Vận dụng cao", "question": q_text, "options": options, "correct": correct_idx, "explanation": explanation}

def get_b25_exams():
    exams = {}
    ch_id = "phys8_c5"
    ch_title = "Chương V: Điện"
    l_id = "phys8_c5_b25"
    l_name = "Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế"

    def meta(t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # ĐỀ 1: Khảo sát thực hành đoạn mạch mắc NỐI TIẾP
    exams[f"{l_id}_test1"] = meta(1,
        [
            make_mc(1, "Nhận biết", "Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc nối tiếp, mối liên hệ giữa cường độ dòng điện mạch chính I và qua mỗi đèn I1, I2 là:", ["I = I1 = I2", "I = I1 + I2", "I = I1 - I2", "I = I1 * I2"], 0, "Trong mạch nối tiếp, cường độ dòng điện tại mọi điểm là như nhau."),
            make_mc(2, "Nhận biết", "Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc nối tiếp vào nguồn U, hiệu điện thế toàn mạch thỏa mãn công thức:", ["U = U1 + U2", "U = U1 = U2", "U = U1 - U2", "U1 + U2 = 2 * U"], 0, "Hiệu điện thế toàn mạch bằng tổng các hiệu điện thế thành phần."),
            make_mc(3, "Nhận biết", "Điện trở tương đương của đoạn mạch gồm hai điện trở R1 và R2 mắc nối tiếp được tính bởi:", ["Rtd = R1 + R2", "Rtd = R1 * R2", "Rtd = (R1 + R2) / 2", "1/Rtd = 1/R1 + 1/R2"], 0, "Rtd = R1 + R2 đối với mạch nối tiếp."),
            make_mc(4, "Nhận biết", "Khi tháo bóng đèn Đ1 ra khỏi đui đèn trong đoạn mạch gồm Đ1 nối tiếp Đ2 thì đèn Đ2 sẽ:", ["Tắt hẳn vì toàn mạch bị hở", "Sáng rực rỡ hơn gấp đôi", "Vẫn sáng bình thường", "Nhấp nháy liên tục"], 0, "Mạch nối tiếp hở một điểm thì mất dòng toàn mạch."),
            make_mc(5, "Nhận biết", "Hai bóng đèn giống nhau cùng mắc nối tiếp vào nguồn 9 V. Hiệu điện thế giữa hai đầu mỗi bóng đèn bằng:", ["4,5 V", "9 V", "18 V", "0 V"], 0, "U1 = U2 = 9 / 2 = 4,5 V."),
            make_mc(6, "Nhận biết", "Trong mạch nối tiếp gồm hai điện trở R1 và R2, hiệu điện thế hai đầu mỗi điện trở tỉ lệ với điện trở theo hệ thức:", ["U1 / U2 = R1 / R2", "U1 / U2 = R2 / R1", "U1 * U2 = R1 * R2", "U1 - U2 = R1 - R2"], 0, "Vì I như nhau nên U1 / U2 = R1 / R2."),
            make_mc(7, "Thông hiểu", "Một mạch điện nối tiếp gồm 2 điện trở R1 = 10 Ω và R2 = 20 Ω. Điện trở tương đương của đoạn mạch bằng:", ["30 Ω", "200 Ω", "6,67 Ω", "15 Ω"], 0, "Rtd = 10 + 20 = 30 Ω."),
            make_mc(8, "Thông hiểu", "Mắc nối tiếp thêm một điện trở R3 vào đoạn mạch đang có bóng đèn sáng, hiện tượng quan sát được là:", ["Độ sáng của bóng đèn giảm đi vì tổng điện trở mạch tăng làm dòng điện giảm", "Đèn sáng rực hơn", "Đèn nổ ngay lập tức", "Độ sáng không đổi"], 0, "Tăng Rtd làm dòng điện I giảm, đèn sáng yếu đi."),
            make_mc(9, "Thông hiểu", "Trong mạch gồm hai đèn Đ1 và Đ2 nối tiếp, nếu đèn Đ1 sáng mạnh hơn đèn Đ2 thì kết luận nào sau đây là ĐÚNG?", ["Điện trở và công suất tiêu thụ của đèn Đ1 lớn hơn đèn Đ2", "Dòng điện qua Đ1 lớn hơn qua Đ2", "Hiệu điện thế hai đầu Đ1 nhỏ hơn Đ2", "Đèn Đ2 bị chập"], 0, "Dòng I như nhau, Đ1 sáng hơn vì R1 lớn hơn kéo theo P1 lớn hơn."),
            make_mc(10, "Thông hiểu", "Khi đo cường độ dòng điện trong mạch nối tiếp, vị trí mắc ampe kế ở đâu là chính xác?", ["Mắc ở bất kì vị trí nào trong mạch nối tiếp đều đo được cùng một giá trị dòng điện", "Chỉ được mắc sát cực dương", "Chỉ được mắc sát cực âm", "Phải mắc song song với nguồn"], 0, "Dòng điện bằng nhau tại mọi điểm trong mạch nối tiếp."),
            make_mc(11, "Thông hiểu", "Một chuỗi đèn led nháy trang trí gồm 20 bóng đèn mắc nối tiếp. Nếu vô tình một bóng đèn bị đứt dây tóc thì:", ["Cả chuỗi 20 bóng đèn đều tắt hết", "19 bóng đèn còn lại vẫn sáng", "Các bóng còn lại sáng rực hơn", "Chuỗi đèn đổi màu"], 0, "Đứt một bóng làm hở toàn mạch."),
            make_mc(12, "Thông hiểu", "Khi nối tắt hai đầu bóng đèn Đ1 trong mạch Đ1 nối tiếp Đ2 bằng một sợi dây đồng ngắn (nối tắt Đ1), điều gì xảy ra?", ["Đèn Đ1 tắt hẳn, đèn Đ2 sáng mạnh hơn bình thường", "Cả hai đèn cùng tắt", "Cả hai đèn cùng sáng bình thường", "Đèn Đ1 phát nổ"], 0, "Nối tắt Đ1 làm U1 = 0, toàn bộ điện áp dồn vào Đ2 làm Đ2 sáng hơn.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về các đặc tính cơ bản của đoạn mạch mắc nối tiếp đề 1:", [
                ("a", "Cường độ dòng điện có giá trị như nhau tại mọi điểm trong mạch nối tiếp.", True),
                ("b", "Hiệu điện thế giữa hai đầu toàn mạch bằng tổng hiệu điện thế trên từng điện trở.", True),
                ("c", "Điện trở tương đương của đoạn mạch nối tiếp luôn nhỏ hơn từng điện trở thành phần.", False),
                ("d", "Mắc càng nhiều bóng đèn nối tiếp vào nguồn không đổi thì mỗi đèn càng sáng yếu đi.", True)
            ], "Rtd nối tiếp luôn lớn hơn từng điện trở thành phần."),
            make_tf(2, "Thông hiểu", "Về quy trình lắp ráp thí nghiệm khảo sát mạch nối tiếp đề 1:", [
                ("a", "Khóa K phải ở trạng thái mở trong suốt thời gian cắm dây nối các linh kiện.", True),
                ("b", "Ampe kế được mắc nối tiếp với các bóng đèn để đo cường độ dòng điện toàn mạch.", True),
                ("c", "Vôn kế được mắc nối tiếp vào giữa hai bóng đèn để đo hiệu điện thế nguồn.", False),
                ("d", "Sau khi đóng khóa K, nếu đèn không sáng cần kiểm tra lại các mối cắm dây dẫn.", True)
            ], "Vôn kế phải mắc song song."),
            make_tf(3, "Thông hiểu", "Về phân bố điện áp và công suất trong đoạn mạch nối tiếp đề 1:", [
                ("a", "Phần tử nào có điện trở lớn hơn thì sẽ nhận được hiệu điện thế lớn hơn giữa hai đầu.", True),
                ("b", "Nếu hai bóng đèn giống hệt nhau nối tiếp thì hiệu điện thế chia đều cho mỗi đèn.", True),
                ("c", "Dòng điện qua phần tử có điện trở lớn hơn sẽ bị suy giảm nhỏ hơn dòng qua phần tử nhỏ.", False),
                ("d", "Tổng công suất tiêu thụ toàn mạch bằng tổng công suất tiêu thụ của các phần tử.", True)
            ], "Mạch nối tiếp có dòng điện bằng nhau tại mọi phần tử."),
            make_tf(4, "Thông hiểu", "Về hiện tượng sự cố mạch điện nối tiếp đề 1:", [
                ("a", "Khi một điện trở bị đứt mạch thì dòng điện trong toàn bộ mạch nối tiếp triệt tiêu về 0.", True),
                ("b", "Đoản mạch một phần tử làm giảm tổng điện trở mạch và làm tăng dòng điện qua các phần tử còn lại.", True),
                ("c", "Cầu chì bảo vệ trong gia đình luôn luôn được mắc song song với thiết bị cần bảo vệ.", False),
                ("d", "Dây cáp điện nối tiếp dài làm sụt giảm điện áp ở cuối đường dây tải điện.", True)
            ], "Cầu chì bắt buộc phải mắc nối tiếp trên dây dẫn.")
        ],
        [
            make_sa(1, "Thông hiểu", "Hai bóng đèn có điện trở R1 = 15 Ω và R2 = 25 Ω mắc nối tiếp. Điện trở tương đương của đoạn mạch là bao nhiêu Ôm (Ω)?", "40", "Rtd = 15 + 25 = 40 Ω."),
            make_sa(2, "Thông hiểu", "Mắc đoạn mạch nối tiếp trên vào nguồn U = 12 V. Cường độ dòng điện chạy qua đèn Đ1 là bao nhiêu Ampe (A)?", "0.3", "I = 12 / 40 = 0,3 A."),
            make_sa(3, "Thông hiểu", "Trong đoạn mạch trên (I = 0,3 A), hiệu điện thế giữa hai đầu đèn Đ1 là bao nhiêu Vôn (V)?", "4.5", "U1 = I * R1 = 0,3 * 15 = 4,5 V."),
            make_sa(4, "Thông hiểu", "Hiệu điện thế giữa hai đầu đèn Đ2 trong đoạn mạch trên là bao nhiêu Vôn (V)?", "7.5", "U2 = I * R2 = 0,3 * 25 = 7,5 V."),
            make_sa(5, "Vận dụng", "Ba điện trở R1 = 10 Ω, R2 = 20 Ω, R3 = 30 Ω mắc nối tiếp vào nguồn 24 V. Cường độ dòng điện qua mạch là bao nhiêu Ampe (A)?", "0.4", "Rtd = 10 + 20 + 30 = 60 Ω. I = 24 / 60 = 0,4 A."),
            make_sa(6, "Vận dụng", "Để bóng đèn 6 V - 0,5 A sáng bình thường khi cắm vào nguồn 9 V, cần mắc nối tiếp với đèn một điện trở phụ có giá trị bao nhiêu Ôm (Ω)?", "6", "U_R = 9 - 6 = 3 V. R = 3 / 0,5 = 6 Ω.")
        ],
        [
            make_vdc(1, "Một đoạn mạch gồm điện trở R1 = 8 Ω mắc nối tiếp với một biến trở con chạy Rb vào nguồn điện U = 12 V không đổi. Khi con chạy ở vị trí Rb = 16 Ω, công suất tỏa nhiệt trên biến trở Rb là:", [
                "4,0 W", "2,0 W", "6,0 W", "8,0 W"
            ], 0, "Rtd = 8 + 16 = 24 Ω. I = 12 / 24 = 0,5 A. P_b = I^2 * Rb = 0,25 * 16 = 4,0 W."),
            make_vdc(2, "Trong mạch điện trên (R1 = 8 Ω, nguồn U = 12 V), để công suất tỏa nhiệt trên biến trở Rb đạt giá trị cực đại thì biến trở Rb phải được điều chỉnh bằng:", [
                "8 Ω", "16 Ω", "4 Ω", "0 Ω"
            ], 0, "Theo bất đẳng thức Cauchy, công suất trên Rb đạt cực đại khi Rb = R1 = 8 Ω."),
            make_vdc(3, "Một vôn kế có thang đo cực đại 10 V và điện trở nội Rv = 2000 Ω. Muốn dùng vôn kế này để đo hiệu điện thế tới 50 V thì cần mắc nối tiếp với vôn kế một điện trở phụ có giá trị bằng:", [
                "8000 Ω", "10 000 Ω", "2000 Ω", "4000 Ω"
            ], 0, "Hệ số mở rộng n = 50 / 10 = 5. R_p = (n - 1) * Rv = 4 * 2000 = 8000 Ω."),
            make_vdc(4, "Một đường dây tải điện đôi dài 2 km có điện trở tổng cộng là 4 Ω cấp điện cho một xưởng cơ khí tiêu thụ dòng điện 25 A. Độ sụt áp trên đường dây truyền tải và công suất hao phí tỏa nhiệt trên dây là:", [
                "ΔU = 100 V; P_hp = 2500 W", "ΔU = 50 V; P_hp = 1250 W", "ΔU = 200 V; P_hp = 5000 W", "ΔU = 25 V; P_hp = 625 W"
            ], 0, "ΔU = I * R = 25 * 4 = 100 V. P_hp = I^2 * R = 625 * 4 = 2500 W.")
        ]
    )

    # ĐỀ 2: Khảo sát thực hành đoạn mạch mắc SONG SONG
    exams[f"{l_id}_test2"] = meta(2,
        [
            make_mc(1, "Nhận biết", "Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc song song vào nguồn hiệu điện thế U, hiệu điện thế hai đầu mỗi nhánh thỏa mãn:", ["U = U1 = U2", "U = U1 + U2", "U = U1 - U2", "U = 2 * (U1 + U2)"], 0, "Trong mạch song song, hiệu điện thế hai đầu mỗi nhánh bằng nhau và bằng nguồn."),
            make_mc(2, "Nhận biết", "Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc song song, cường độ dòng điện mạch chính I và dòng nhánh I1, I2 thỏa mãn:", ["I = I1 + I2", "I = I1 = I2", "I = I1 - I2", "I = (I1 + I2) / 2"], 0, "Dòng điện mạch chính bằng tổng dòng qua các nhánh song song."),
            make_mc(3, "Nhận biết", "Điện trở tương đương của đoạn mạch gồm hai điện trở R1 và R2 mắc song song được tính theo công thức:", ["1/Rtd = 1/R1 + 1/R2 (hay Rtd = R1.R2 / (R1+R2))", "Rtd = R1 + R2", "Rtd = R1 * R2", "Rtd = (R1 + R2) / 2"], 0, "Công thức tính điện trở mạch song song."),
            make_mc(4, "Nhận biết", "Khi tháo bóng đèn Đ1 ra khỏi đui đèn trong đoạn mạch gồm Đ1 song song Đ2 thì đèn Đ2 sẽ:", ["Vẫn sáng bình thường vì hiệu điện thế hai đầu nhánh Đ2 không đổi", "Tắt ngay lập tức", "Cháy nổ theo", "Sáng gấp 10 lần"], 0, "Các nhánh song song hoạt động độc lập."),
            make_mc(5, "Nhận biết", "Hai điện trở giống hệt nhau mỗi chiếc có giá trị R được mắc song song. Điện trở tương đương của bộ này là:", ["R / 2", "2 * R", "R", "R^2"], 0, "Rtd = R / 2 đối với 2 điện trở giống nhau song song."),
            make_mc(6, "Nhận biết", "Trong các thiết bị gia đình (quạt, đèn, tivi, tủ lạnh), các thiết bị được mắc với nhau theo cách nào vào mạng 220 V?", ["Mắc song song", "Mắc nối tiếp", "Mắc hỗn hợp ngẫu nhiên", "Mắc qua rơle nhiệt đơn"], 0, "Mắc song song để nhận đúng điện áp 220 V và bật tắt độc lập."),
            make_mc(7, "Thông hiểu", "Một mạch song song gồm R1 = 20 Ω và R2 = 30 Ω. Điện trở tương đương của đoạn mạch song song này bằng:", ["12 Ω", "50 Ω", "600 Ω", "25 Ω"], 0, "Rtd = (20 * 30) / (20 + 30) = 600 / 50 = 12 Ω."),
            make_mc(8, "Thông hiểu", "Mắc song song thêm một bóng đèn vào mạch điện gia đình đang dùng thì cường độ dòng điện ở mạch chính sẽ:", ["Tăng lên do tổng công suất tiêu thụ của mạch tăng", "Giảm đi", "Không đổi", "Bằng 0"], 0, "Thêm tải song song làm giảm tổng điện trở, dòng mạch chính tăng."),
            make_mc(9, "Thông hiểu", "Trong mạch song song gồm R1 và R2, mối quan hệ giữa cường độ dòng điện và điện trở mỗi nhánh là:", ["I1 / I2 = R2 / R1 (tỉ lệ nghịch với điện trở)", "I1 / I2 = R1 / R2", "I1 * I2 = R1 * R2", "I1 - I2 = R1 - R2"], 0, "Cùng hiệu điện thế U nên I tỉ lệ nghịch với R."),
            make_mc(10, "Thông hiểu", "Nếu một nhánh trong mạch song song bị đoản mạch (chập hai đầu dây nối thẳng vào nhau) thì:", ["Cực kì nguy hiểm, dòng điện mạch chính tăng vọt làm nổ cầu chì ngắt mạch", "Chỉ nhánh đó tắt, các nhánh khác vẫn sáng", "Không có ảnh hưởng gì", "Nguồn điện nạp thêm pin"], 0, "Đoản mạch 1 nhánh song song làm đoản mạch toàn bộ nguồn điện."),
            make_mc(11, "Thông hiểu", "Cường độ dòng điện ở mạch chính I so với các dòng điện qua từng nhánh rẽ I1, I2 luôn thỏa mãn:", ["I luôn lớn hơn cả I1 và I2", "I luôn nhỏ hơn I1", "I bằng I1", "I không xác định"], 0, "Vì I = I1 + I2 với I1, I2 > 0 nên I luôn lớn hơn từng dòng nhánh."),
            make_mc(12, "Thông hiểu", "Điện trở tương đương của đoạn mạch song song luôn có đặc điểm nào sau đây?", ["Luôn nhỏ hơn điện trở của mỗi nhánh thành phần", "Luôn lớn hơn các điện trở thành phần", "Bằng trung bình cộng các điện trở", "Bằng tích các điện trở"], 0, "Rtd song song luôn nhỏ hơn điện trở nhỏ nhất trong các nhánh.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về các đặc tính cơ bản của đoạn mạch mắc song song đề 2:", [
                ("a", "Hiệu điện thế giữa hai đầu mỗi nhánh song song luôn bằng hiệu điện thế toàn mạch.", True),
                ("b", "Cường độ dòng điện ở mạch chính bằng tổng cường độ dòng điện qua các nhánh rẽ.", True),
                ("c", "Điện trở tương đương của đoạn mạch song song luôn lớn hơn từng điện trở thành phần.", False),
                ("d", "Mỗi thiết bị trong mạch song song có thể bật hoặc tắt độc lập mà không ảnh hưởng tải khác.", True)
            ], "Rtd song song luôn nhỏ hơn từng điện trở thành phần."),
            make_tf(2, "Thông hiểu", "Về ứng dụng của mạch song song trong mạng điện sinh hoạt gia đình đề 2:", [
                ("a", "Tất cả các ổ cắm điện trong nhà đều được đấu nối song song với nhau vào lưới 220 V.", True),
                ("b", "Khi tắt bóng đèn phòng ngủ thì tivi ở phòng khách vẫn hoạt động hoàn toàn bình thường.", True),
                ("c", "Nếu các thiết bị trong nhà mắc nối tiếp thì khi tắt đèn bàn, tủ lạnh cũng sẽ tắt theo.", True),
                ("d", "Càng cắm nhiều thiết bị công suất lớn vào một ổ cắm thì tổng điện trở mạch càng tăng cao.", False)
            ], "Cắm thêm thiết bị song song làm giảm tổng điện trở mạch, tăng dòng điện."),
            make_tf(3, "Thông hiểu", "Về phân bố dòng điện qua các nhánh song song đề 2:", [
                ("a", "Nhánh nào có điện trở nhỏ hơn thì cường độ dòng điện chạy qua nhánh đó sẽ lớn hơn.", True),
                ("b", "Nếu hai bóng đèn giống hệt nhau mắc song song thì dòng điện qua hai đèn bằng nhau.", True),
                ("c", "Tổng công suất tiêu thụ của đoạn mạch song song bằng tổng công suất của các nhánh.", True),
                ("d", "Cường độ dòng điện qua nhánh rẽ phụ thuộc trực tiếp vào điện trở của nhánh bên cạnh.", False)
            ], "Hiệu điện thế U không đổi nên dòng mỗi nhánh chỉ phụ thuộc R nhánh đó: I_i = U / R_i."),
            make_tf(4, "Thông hiểu", "Về nhận diện nguy cơ chập cháy trong mạch điện song song đề 2:", [
                ("a", "Cắm quá nhiều thiết bị vào ổ cắm có thể làm dòng điện vượt quá giới hạn chịu nhiệt của dây.", True),
                ("b", "Aptomat tổng tự động ngắt khi phát hiện dòng điện mạch chính vượt quá giá trị định mức.", True),
                ("c", "Khi một bóng đèn trong mạch song song bị cháy đứt tóc thì cầu chì tổng sẽ lập tức nổ đứt.", False),
                ("d", "Sự cố ngắn mạch tại bất kì nhánh song song nào cũng sẽ làm tê liệt toàn bộ mạng điện.", True)
            ], "Đèn đứt tóc chỉ làm hở nhánh đó, không gây nổ cầu chì tổng.")
        ],
        [
            make_sa(1, "Thông hiểu", "Hai điện trở R1 = 20 Ω và R2 = 30 Ω mắc song song vào nguồn U = 12 V. Tính điện trở tương đương của đoạn mạch (Ω).", "12", "Rtd = (20 * 30) / (20 + 30) = 12 Ω."),
            make_sa(2, "Thông hiểu", "Trong mạch song song trên (R1 = 20 Ω, U = 12 V), cường độ dòng điện qua điện trở R1 là bao nhiêu Ampe (A)?", "0.6", "I1 = 12 / 20 = 0,6 A."),
            make_sa(3, "Thông hiểu", "Cường độ dòng điện qua điện trở R2 (R2 = 30 Ω, U = 12 V) là bao nhiêu Ampe (A)?", "0.4", "I2 = 12 / 30 = 0,4 A."),
            make_sa(4, "Thông hiểu", "Cường độ dòng điện trong mạch chính của đoạn mạch song song trên là bao nhiêu Ampe (A)?", "1.0", "I = I1 + I2 = 0,6 + 0,4 = 1,0 A."),
            make_sa(5, "Vận dụng", "Ba điện trở giống nhau mỗi chiếc có giá trị 60 Ω mắc song song với nhau. Điện trở tương đương của cả bộ ba điện trở này là bao nhiêu Ôm (Ω)?", "20", "Rtd = 60 / 3 = 20 Ω."),
            make_sa(6, "Vận dụng", "Hai bóng đèn Đ1 (12 V - 0,4 A) và Đ2 (12 V - 0,6 A) mắc song song vào nguồn 12 V. Cường độ dòng điện trong mạch chính khi cả hai đèn cùng sáng bình thường là bao nhiêu Ampe (A)?", "1.0", "I = 0,4 + 0,6 = 1,0 A.")
        ],
        [
            make_vdc(1, "Một đoạn mạch gồm hai điện trở R1 = 15 Ω và R2 = 10 Ω mắc song song với nhau rồi nối tiếp với điện trở R3 = 4 Ω vào nguồn điện không đổi U = 20 V. Cường độ dòng điện chạy qua điện trở R3 và hiệu điện thế hai đầu đoạn mạch song song (R1 // R2) là:", [
                "I3 = 2,0 A; U12 = 12 V", "I3 = 1,0 A; U12 = 10 V", "I3 = 2,5 A; U12 = 15 V", "I3 = 4,0 A; U12 = 8 V"
            ], 0, "R12 = (15*10)/(15+10) = 6 Ω. Rtd = 6 + 4 = 10 Ω. I3 = I = 20 / 10 = 2,0 A. U12 = I * R12 = 2 * 6 = 12 V."),
            make_vdc(2, "Trong mạch điện trên, cường độ dòng điện chạy qua điện trở R1 và qua điện trở R2 lần lượt bằng:", [
                "I1 = 0,8 A; I2 = 1,2 A", "I1 = 1,0 A; I2 = 1,0 A", "I1 = 1,2 A; I2 = 0,8 A", "I1 = 0,5 A; I2 = 1,5 A"
            ], 0, "I1 = U12 / R1 = 12 / 15 = 0,8 A. I2 = U12 / R2 = 12 / 10 = 1,2 A."),
            make_vdc(3, "Một hộ gia đình sử dụng mạng điện 220 V gồm 1 bàn là 1100 W, 1 ấm siêu tốc 1540 W và 5 bóng đèn 44 W mắc song song. Tổng cường độ dòng điện mạch chính khi bật đồng thời tất cả các thiết bị trên là:", [
                "13,0 A", "10,0 A", "15,5 A", "20,0 A"
            ], 0, "P_tong = 1100 + 1540 + (5 * 44) = 2860 W. I = P_tong / U = 2860 / 220 = 13,0 A."),
            make_vdc(4, "Một ampe kế có thang đo cực đại 5 A và điện trở nội Ra = 0,1 Ω. Để ampe kế đo được dòng điện tối đa tới 25 A thì cần mắc song song một điện trở sun Rs có giá trị bằng:", [
                "0,025 Ω", "0,05 Ω", "0,1 Ω", "0,5 Ω"
            ], 0, "Hệ số n = 25 / 5 = 5. Rs = Ra / (n - 1) = 0,1 / 4 = 0,025 Ω.")
        ]
    )

    # ĐỀ 3: Biến trở, Mạch cầu Wheatstone & Xử lý sự cố mạch điện thực hành
    exams[f"{l_id}_test3"] = meta(3,
        [
            make_mc(1, "Nhận biết", "Biến trở là một thiết bị điện có tác dụng gì trong mạch điện?", ["Dùng để điều chỉnh cường độ dòng điện hoặc hiệu điện thế trong mạch", "Dùng để đo hiệu điện thế", "Dùng để tạo ra dòng điện", "Dùng để đóng cắt nguồn tự động"], 0, "Biến trở dùng để điều chỉnh cường độ dòng điện."),
            make_mc(2, "Nhận biết", "Bộ phận chính của một biến trở con chạy thông dụng gồm:", ["Cuộn dây dẫn có điện trở suất lớn quấn trên lõi sứ cách điện và con chạy trượt tiếp xúc", "Hai lá thép mỏng", "Bình đựng dung dịch muối", "Thanh nam châm vĩnh cửu"], 0, "Cuộn dây điện trở suất lớn và con chạy tiếp xúc."),
            make_mc(3, "Nhận biết", "Khi dịch chuyển con chạy của biến trở làm tăng chiều dài phần dây dẫn tham gia vào mạch thì điện trở của biến trở sẽ:", ["Tăng lên", "Giảm đi", "Không đổi", "Bằng 0"], 0, "R tỉ lệ thuận với chiều dài dây dẫn tham gia."),
            make_mc(4, "Nhận biết", "Mạch cầu Wheatstone là một sơ đồ mạch điện đặc biệt dùng để đo chính xác đại lượng nào?", ["Giá trị điện trở của một vật dẫn chưa biết", "Cường độ dòng điện cực đại", "Điện áp của sấm sét", "Nhiệt độ nóng chảy của kim loại"], 0, "Mạch cầu dùng để đo chính xác điện trở Rx."),
            make_mc(5, "Nhận biết", "Điều kiện để mạch cầu Wheatstone (gồm 4 điện trở R1, R2, R3, Rx) cân bằng (dòng qua điện kế G bằng 0) là:", ["R1 * Rx = R2 * R3 (hay R1 / R2 = R3 / Rx)", "R1 + Rx = R2 + R3", "R1 * R2 = R3 * Rx", "R1 - Rx = R2 - R3"], 0, "Tích các điện trở ở nhánh đối diện bằng nhau: R1.Rx = R2.R3."),
            make_mc(6, "Nhận biết", "Trong thí nghiệm thực hành, khi muốn bóng đèn sáng dần lên, ta cần điều chỉnh con chạy của biến trở sao cho:", ["Điện trở biến trở tham gia vào mạch giảm dần", "Điện trở biến trở tăng dần", "Ngắt con chạy ra khỏi mạch", "Đổi cực nguồn điện"], 0, "Giảm Rb làm dòng điện tăng, đèn sáng dần."),
            make_mc(7, "Thông hiểu", "Một biến trở con chạy có ghi (50 Ω - 2 A). Con số 2 A cho biết điều gì?", ["Cường độ dòng điện định mức lớn nhất cho phép chạy qua biến trở mà không làm cháy dây", "Dòng điện nhỏ nhất", "Điện áp định mức", "Khối lượng cuộn dây"], 0, "Dòng điện cực đại cho phép qua biến trở."),
            make_mc(8, "Thông hiểu", "Trước khi đóng công tắc để khảo sát mạch điện có biến trở, người ta thường dịch chuyển con chạy về vị trí có giá trị điện trở:", ["Lớn nhất để dòng điện ban đầu nhỏ nhất bảo vệ các linh kiện trong mạch", "Bằng 0", "Chính giữa cuộn dây", "Vị trí ngẫu nhiên"], 0, "Bắt đầu ở điện trở lớn nhất để bảo vệ thiết bị."),
            make_mc(9, "Thông hiểu", "Trong phương pháp xác định vị trí chập cáp điện ngầm hai sợi, người ta dựa vào nguyên lí:", ["Điện trở của đoạn dây cáp tỉ lệ thuận với khoảng cách từ trạm đo đến điểm chập", "Dây cáp phát sáng", "Nhiệt độ cáp giảm", "Dây co ngắn lại"], 0, "R = ρ.L/S tỉ lệ thuận với chiều dài L."),
            make_mc(10, "Thông hiểu", "Khi nối hai cực của một viên pin bằng dây đồng có điện trở rất nhỏ (đoản mạch nguồn), dòng điện trong dây đạt giá trị rất lớn vì:", ["Tổng điện trở của mạch ngoài xấp xỉ bằng 0", "Hiệu điện thế pin tăng vọt", "Pin tự sinh thêm hạt proton", "Dây dẫn hút thêm electron từ không khí"], 0, "R mạch ngoài gần bằng 0 làm I = U / R tăng vọt."),
            make_mc(11, "Thông hiểu", "Một bóng đèn pin được điều chỉnh độ sáng bằng chiết áp (biến trở than). Núm xoay chiết áp về bản chất là:", ["Con chạy xoay trượt trên một vành điện trở than tròn", "Công tắc bật tắt", "Máy biến thế mini", "Cầu chì tự phục hồi"], 0, "Chiết áp xoay làm thay đổi chiều dài dải than dẫn điện."),
            make_mc(12, "Thông hiểu", "Ưu điểm lớn nhất của mạch cầu Wheatstone so với việc dùng ampe kế và vôn kế thông thường để đo Rx là:", ["Không phụ thuộc vào độ chính xác của nguồn điện và triệt tiêu được sai số do nội trở dụng cụ đo", "Lắp ráp nhanh hơn", "Chỉ cần 1 dây dẫn", "Đo được dòng xoay chiều cao thế"], 0, "Phương pháp cân bằng không (null method) cho độ chính xác rất cao.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về cấu tạo và nguyên tắc hoạt động của biến trở đề 3:", [
                ("a", "Biến trở hoạt động dựa trên sự thay đổi chiều dài của dây dẫn tham gia mạch.", True),
                ("b", "Dây quấn biến trở thường làm bằng hợp kim có điện trở suất lớn như constantan hoặc manganin.", True),
                ("c", "Để biến trở có tác dụng điều chỉnh, ta phải đấu cả hai chốt đầu dây cố định vào mạch mà không dùng chốt con chạy.", False),
                ("d", "Con chạy của biến trở tiếp xúc trượt dọc theo các vòng dây đã cạo sạch lớp sơn cách điện.", True)
            ], "Phải dùng 1 chốt cố định và 1 chốt con chạy mới thay đổi được điện trở."),
            make_tf(2, "Thông hiểu", "Về nguyên tắc cân bằng của mạch cầu đo điện trở đề 3:", [
                ("a", "Cầu cân bằng khi hiệu điện thế giữa hai nút nối điện kế bằng 0 V.", True),
                ("b", "Khi cầu cân bằng, kim của điện kế siêu nhạy chỉ đúng vạch số 0 ở giữa bảng đo.", True),
                ("c", "Nếu đổi cực của nguồn điện thì cầu đang cân bằng sẽ bị mất cân bằng hoàn toàn.", False),
                ("d", "Giá trị Rx đo được tính theo công thức Rx = (R2 * R3) / R1.", True)
            ], "Điều kiện cân bằng R1.Rx = R2.R3 không phụ thuộc cực tính của nguồn điện."),
            make_tf(3, "Thông hiểu", "Về các thao tác an toàn khi sử dụng biến trở trong phòng thí nghiệm đề 3:", [
                ("a", "Không để dòng điện chạy qua biến trở vượt quá giá trị cường độ định mức ghi trên nhãn.", True),
                ("b", "Khi bắt đầu thí nghiệm, luôn kéo con chạy về vị trí có điện trở nhỏ nhất để đèn sáng ngay.", False),
                ("c", "Dịch chuyển con chạy nhẹ nhàng để tránh làm mòn đứt các vòng dây kim loại mảnh.", True),
                ("d", "Sau một thời gian hoạt động với dòng lớn, biến trở có thể bị nóng lên do tác dụng nhiệt của dòng điện.", True)
            ], "Luôn đặt biến trở ở giá trị lớn nhất ban đầu để hạn chế dòng khởi động."),
            make_tf(4, "Thông hiểu", "Về chẩn đoán và khắc phục sự cố hỏng mạch điện thực hành đề 3:", [
                ("a", "Dùng thang đo ôm kế (đo điện trở) của đồng hồ vạn năng để kiểm tra thông mạch dây dẫn.", True),
                ("b", "Nếu dây dẫn bị đứt ngầm bên trong lớp nhựa bọc, ôm kế đo hai đầu dây sẽ chỉ điện trở vô cùng lớn.", True),
                ("c", "Kiểm tra thông mạch bằng ôm kế được tiến hành khi mạch điện vẫn đang cắm vào nguồn điện hoạt động.", False),
                ("d", "Các tiếp điểm bị oxi hóa rỉ sét làm tăng điện trở tiếp xúc khiến đèn sáng chập chờn.", True)
            ], "Tuyệt đối không đo điện trở khi mạch đang có điện vì sẽ làm cháy đồng hồ đo.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một cuộn dây biến trở làm bằng dây nikenlin có chiều dài 20 m và điện trở 40 Ω. Điện trở của mỗi mét dây là bao nhiêu Ôm (Ω)?", "2", "R0 = 40 / 20 = 2 Ω/m."),
            make_sa(2, "Thông hiểu", "Khi dịch con chạy để phần dây tham gia mạch có chiều dài 8 m thì điện trở của biến trở lúc này là bao nhiêu Ôm (Ω)?", "16", "Rb = 8 * 2 = 16 Ω."),
            make_sa(3, "Thông hiểu", "Một mạch cầu Wheatstone cân bằng gồm R1 = 12 Ω, R2 = 24 Ω, R3 = 15 Ω và Rx. Giá trị của điện trở Rx là bao nhiêu Ôm (Ω)?", "30", "Rx = (R2 * R3) / R1 = (24 * 15) / 12 = 30 Ω."),
            make_sa(4, "Thông hiểu", "Một biến trở ghi 50 Ω - 2 A. Hiệu điện thế tối đa cho phép đặt vào hai đầu toàn bộ cuộn dây biến trở là bao nhiêu Vôn (V)?", "100", "U_max = I_max * R_max = 2 * 50 = 100 V."),
            make_sa(5, "Vận dụng", "Một bóng đèn 6 V - 0,6 A mắc nối tiếp với biến trở vào nguồn 12 V. Để đèn sáng bình thường, điện trở biến trở tham gia phải bằng bao nhiêu Ôm (Ω)?", "10", "U_b = 12 - 6 = 6 V. Rb = 6 / 0,6 = 10 Ω."),
            make_sa(6, "Vận dụng", "Một tuyến cáp ngầm đôi có điện trở 5 Ω trên mỗi kilômét (Ω/km). Đo từ trạm thấy điện trở đoạn cáp bị chập hai sợi là 15 Ω. Điểm chập cách trạm bao nhiêu kilômét (km)?", "3", "d = 15 / 5 = 3 km.")
        ],
        [
            make_vdc(1, "Một bóng đèn Đ ghi 6 V - 0,5 A được mắc nối tiếp với một biến trở con chạy Rb vào nguồn điện U = 9 V không đổi. Biến trở có điện trở toàn phần R0 = 30 Ω.\\nKhi dịch chuyển con chạy từ vị trí điện trở cực đại R0 về vị trí đèn sáng bình thường, giá trị điện trở biến trở đã thay đổi một lượng ΔRb bằng:", [
                "Giảm đi 24 Ω (từ 30 Ω xuống 6 Ω)", "Giảm đi 12 Ω", "Tăng thêm 6 Ω", "Giảm đi 18 Ω"
            ], 0, "Để đèn sáng bình thường: U_b = 9 - 6 = 3 V => Rb = 3 / 0,5 = 6 Ω. Độ giảm: ΔRb = 30 - 6 = 24 Ω."),
            make_vdc(2, "Một mạch cầu Wheatstone gồm R1 = 10 Ω, R2 = 20 Ω, R3 là một hộp điện trở có thể điều chỉnh từ 1 Ω đến 100 Ω, và Rx là điện trở cần đo. Khi R3 được điều chỉnh bằng 18,5 Ω thì kim điện kế chỉ số 0. Nếu hộp điện trở R3 có sai số ±0,2 Ω thì giá trị đo được của Rx và khoảng sai số tuyệt đối là:", [
                "Rx = 37,0 Ω; sai số ±0,4 Ω", "Rx = 37,0 Ω; sai số ±0,2 Ω", "Rx = 18,5 Ω; sai số ±0,1 Ω", "Rx = 9,25 Ω; sai số ±0,4 Ω"
            ], 0, "Rx = (R2 / R1) * R3 = (20 / 10) * 18,5 = 37,0 Ω. Sai số ΔRx = 2 * 0,2 = 0,4 Ω."),
            make_vdc(3, "Một cảm biến đo mức nhiên liệu trong bình xe hơi là một biến trở con chạy gắn với một phao nổi. Khi bình đầy nhiên liệu (phao ở đỉnh), biến trở có điện trở 10 Ω. Khi bình cạn (phao ở đáy), biến trở có điện trở 90 Ω. Mạch đo gồm cảm biến nối tiếp với ampe kế nội trở không đáng kể và điện trở bảo vệ R0 = 30 Ω vào nguồn 12 V. Cường độ dòng điện qua ampe kế khi bình đầy và khi bình cạn lần lượt là:", [
                "Khi đầy I = 0,3 A; khi cạn I = 0,1 A", "Khi đầy I = 1,2 A; khi cạn I = 0,13 A", "Khi đầy I = 0,4 A; khi cạn I = 0,15 A", "Khi đầy I = 0,2 A; khi cạn I = 0,05 A"
            ], 0, "Khi đầy: Rtd = 10 + 30 = 40 Ω => I = 12 / 40 = 0,3 A. Khi cạn: Rtd = 90 + 30 = 120 Ω => I = 12 / 120 = 0,1 A."),
            make_vdc(4, "Một dây cáp điện thoại đôi dài 5 km nối từ A đến B bị chập điện giữa hai sợi tại điểm C cách A một khoảng x km. Để xác định x, người ta đo điện trở giữa hai đầu tại A (đầu B để hở) thu được R_A = 24 Ω; đo điện trở giữa hai đầu tại B (đầu A để hở) thu được R_B = 16 Ω. Biết điện trở tiếp xúc tại điểm chập coi như bằng 0 và cáp đồng chất. Khoảng cách x từ đầu A đến điểm chập C là:", [
                "3,0 km", "2,0 km", "2,5 km", "3,5 km"
            ], 0, "R_A / R_B = x / (5 - x) => 24 / 16 = 1,5 => x = 1,5 * (5 - x) => 2,5 x = 7,5 => x = 3,0 km.")
        ]
    )

    return exams
