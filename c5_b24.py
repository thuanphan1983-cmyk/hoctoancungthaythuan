# -*- coding: utf-8 -*-
# c5_b24.py - Bài 24: Cường độ dòng điện và hiệu điện thế (3 đề độc lập 100%)
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

def get_b24_exams():
    exams = {}
    ch_id = "phys8_c5"
    ch_title = "Chương V: Điện"
    l_id = "phys8_c5_b24"
    l_name = "Bài 24: Cường độ dòng điện và hiệu điện thế"

    def meta(t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # ĐỀ 1: Khái niệm, Đơn vị đo & Ý nghĩa thông số nguồn điện
    exams[f"{l_id}_test1"] = meta(1,
        [
            make_mc(1, "Nhận biết", "Cường độ dòng điện cho biết điều gì về dòng điện chạy qua vật dẫn?", ["Đặc trưng cho độ mạnh hoặc yếu của dòng điện", "Đặc trưng cho thể tích dây dẫn", "Đặc trưng cho màu sắc dây dẫn", "Đặc trưng cho khối lượng nguồn"], 0, "Cường độ dòng điện đặc trưng cho mức độ mạnh yếu của dòng điện."),
            make_mc(2, "Nhận biết", "Đơn vị đo cường độ dòng điện trong hệ thống đo lường quốc tế (SI) là:", ["Ampe (kí hiệu là A)", "Vôn (kí hiệu là V)", "Oát (kí hiệu là W)", "Jun (kí hiệu là J)"], 0, "Cường độ dòng điện đo bằng Ampe (A)."),
            make_mc(3, "Nhận biết", "Đơn vị đo hiệu điện thế trong hệ thống đo lường quốc tế (SI) là:", ["Vôn (kí hiệu là V)", "Ampe (kí hiệu là A)", "Ôm (kí hiệu là Ω)", "Culông (kí hiệu là C)"], 0, "Hiệu điện thế đo bằng Vôn (V)."),
            make_mc(4, "Nhận biết", "Một cường độ dòng điện 250 mA đổi sang đơn vị Ampe (A) có giá trị là:", ["0,25 A", "2,5 A", "25 A", "0,025 A"], 0, "250 mA = 250 / 1000 = 0,25 A."),
            make_mc(5, "Nhận biết", "Một hiệu điện thế 0,5 kV đổi sang đơn vị Vôn (V) có giá trị là:", ["500 V", "50 V", "5000 V", "0,0005 V"], 0, "0,5 kV = 0,5 * 1000 = 500 V."),
            make_mc(6, "Nhận biết", "Trên thân một viên pin tiểu hình trụ có ghi 1,5 V. Con số 1,5 V này có ý nghĩa gì?", ["Hiệu điện thế định mức giữa hai cực của pin khi mạch hở chưa nối tải", "Dòng điện lớn nhất pin có thể phát ra", "Khối lượng của viên pin", "Chiều dài của viên pin"], 0, "Số vôn là hiệu điện thế giữa 2 cực khi mạch hở."),
            make_mc(7, "Thông hiểu", "Trên một bóng đèn xe máy có ghi (12 V - 35 W). Để đèn sáng bình thường, ta phải mắc bóng đèn vào nguồn có hiệu điện thế:", ["Bằng đúng 12 V", "Lớn hơn 24 V", "Bằng 6 V", "Bằng 220 V"], 0, "Cần cấp đúng hiệu điện thế định mức 12 V."),
            make_mc(8, "Thông hiểu", "Acquy xe đạp điện thường có ghi thông số 48 V. Hiệu điện thế giữa hai cực của bộ acquy này bằng:", ["48 V", "4,8 V", "480 V", "0,48 V"], 0, "Hiệu điện thế định mức của acquy là 48 V."),
            make_mc(9, "Thông hiểu", "Trong một đoạn mạch kim loại, dòng điện có cường độ càng lớn khi:", ["Lượng điện tích tự do chuyển dịch qua tiết diện thẳng trong 1 giây càng nhiều", "Dây dẫn càng dài", "Dây dẫn càng nóng", "Nguồn điện càng cũ"], 0, "I = q / t đặc trưng cho điện lượng dịch chuyển trong 1 giây."),
            make_mc(10, "Thông hiểu", "Một microampe (1 μA) bằng bao nhiêu phần của một Ampe (A)?", ["10^-6 A (một phần triệu Ampe)", "10^-3 A (một phần nghìn Ampe)", "10^-2 A", "10^6 A"], 0, "1 μA = 10^-6 A."),
            make_mc(11, "Thông hiểu", "Hiệu điện thế giữa hai cực của pin con thỏ mới tinh khi chưa mắc vào mạch là 1,5 V. Nếu mắc pin vào bóng đèn đang sáng thì hiệu điện thế hai cực pin đo được sẽ:", ["Hơi nhỏ hơn 1,5 V do có điện trở trong của pin", "Tăng lên 3 V", "Bằng 0 V", "Tăng lên vô cùng"], 0, "Khi có tải dòng I, độ sụt áp làm U hai cực hơi giảm so với suất điện động hở mạch."),
            make_mc(12, "Thông hiểu", "Mạng điện sinh hoạt dân dụng tại Việt Nam cung cấp hiệu điện thế hiệu dụng tiêu chuẩn là:", ["220 V", "110 V", "380 V", "12 V"], 0, "Lưới điện sinh hoạt Việt Nam chuẩn 220 V.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về các đơn vị và đại lượng cường độ dòng điện, hiệu điện thế đề 1:", [
                ("a", "Kí hiệu chữ cái đại diện cho cường độ dòng điện là I, đơn vị là A.", True),
                ("b", "Kí hiệu chữ cái đại diện cho hiệu điện thế là U, đơn vị là V.", True),
                ("c", "1 Ampe tương đương với 100 miliampe.", False),
                ("d", "1 kilôvôn tương đương với 1000 Vôn.", True)
            ], "1 A = 1000 mA."),
            make_tf(2, "Thông hiểu", "Về ý nghĩa số vôn và nguồn điện thường gặp trong cuộc sống:", [
                ("a", "Số vôn ghi trên pin cho biết khả năng sinh công của lực điện trường của viên pin đó.", True),
                ("b", "Pin nút áo dùng cho đồng hồ đeo tay thường có hiệu điện thế khoảng 1,5 V đến 3 V.", True),
                ("c", "Nguồn pin 1,5 V có thể gây điện giật chết người khi vô tình chạm hai tay vào hai cực.", False),
                ("d", "Nối tiếp 2 viên pin 1,5 V cùng chiều sẽ tạo ra bộ nguồn có hiệu điện thế tổng bằng 3 V.", True)
            ], "Điện áp 1,5 V rất an toàn, không thể gây giật chết người."),
            make_tf(3, "Thông hiểu", "Về mối quan hệ giữa hiệu điện thế và cường độ dòng điện trên vật dẫn:", [
                ("a", "Muốn có dòng điện chạy qua vật tiêu thụ, bắt buộc phải tạo ra hiệu điện thế giữa hai đầu vật đó.", True),
                ("b", "Khi hiệu điện thế đặt vào hai đầu bóng đèn tăng lên thì độ sáng của đèn cũng tăng theo.", True),
                ("c", "Khi hiệu điện thế giữa hai đầu một đoạn dây dẫn bằng 0 thì dòng điện qua dây đạt giá trị cực đại.", False),
                ("d", "Hiệu điện thế tạo ra lực điện trường làm các hạt mang điện chuyển dịch có hướng thành dòng điện.", True)
            ], "U = 0 thì không có lực điện trường, I = 0."),
            make_tf(4, "Thông hiểu", "Về định mức sử dụng an toàn của các thiết bị điện sinh hoạt:", [
                ("a", "Mỗi thiết bị điện đều có hiệu điện thế định mức do nhà sản xuất quy định trên nhãn máy.", True),
                ("b", "Cắm thiết bị 110 V trực tiếp vào nguồn điện 220 V có thể làm thiết bị bị cháy hỏng ngay lập tức.", True),
                ("c", "Thiết bị điện 220 V cắm vào nguồn 110 V sẽ hoạt động với công suất gấp đôi bình thường.", False),
                ("d", "Sử dụng đúng hiệu điện thế định mức giúp thiết bị vận hành an toàn và bền bỉ tối đa.", True)
            ], "Cắm thiết bị 220V vào 110V sẽ chạy rất yếu chứ không thể tăng công suất.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một dòng điện có cường độ 0,45 A. Đổi giá trị này sang đơn vị miliampe (mA).", "450", "0,45 A = 0,45 * 1000 = 450 mA."),
            make_sa(2, "Thông hiểu", "Một đường dây điện cao thế có hiệu điện thế 500 kV. Đổi giá trị này sang đơn vị Vôn (V).", "500000", "500 kV = 500 * 1000 = 500 000 V."),
            make_sa(3, "Thông hiểu", "Một người ghép nối tiếp 4 viên pin tiểu loại 1,5 V để lắp vào đèn pin. Hiệu điện thế tổng cộng của bộ pin là bao nhiêu Vôn (V)?", "6", "U = 4 * 1,5 = 6 V."),
            make_sa(4, "Thông hiểu", "Một acquy ô tô có hiệu điện thế 12 V gồm các ngăn pin 2 V mắc nối tiếp. Số ngăn pin có trong chiếc acquy này là bao nhiêu?", "6", "Số ngăn = 12 / 2 = 6 ngăn."),
            make_sa(5, "Vận dụng", "Trong thời gian 25 giây, có điện lượng 15 Culông chuyển qua tiết diện dây dẫn. Cường độ dòng điện qua dây dẫn là bao nhiêu Ampe (A)?", "0.6", "I = q / t = 15 / 25 = 0,6 A."),
            make_sa(6, "Vận dụng", "Một vôn kế có 100 vạch chia đều, giới hạn đo là 20 V. Giá trị mỗi độ chia nhỏ nhất của vôn kế này là bao nhiêu Vôn (V)?", "0.2", "ĐCNN = 20 / 100 = 0,2 V.")
        ],
        [
            make_vdc(1, "Một tia sét đánh xuống đất mang một lượng điện tích khổng lồ q = 30 Culông phóng qua không khí trong thời gian chỉ 0,0002 giây (0,2 mili-giây). Cường độ dòng điện cực đại của tia sét này bằng:", [
                "150 000 A (150 kA)", "60 000 A", "15 000 A", "300 A"
            ], 0, "I = q / t = 30 / 0,0002 = 150 000 A = 150 kA."),
            make_vdc(2, "Một viên pin dự phòng điện thoại có dung lượng danh định ghi trên vỏ là 10 000 mAh ở điện áp 3,7 V. Tổng năng lượng điện tích trữ bên trong viên pin dự phòng này (tính theo Jun) xấp xỉ bằng:", [
                "133 200 J (tương đương 37 Wh)", "37 000 J", "100 000 J", "10 000 J"
            ], 0, "q = 10 A * 3600 s = 36 000 C. W = U * q = 3,7 * 36 000 = 133 200 J = 37 Wh."),
            make_vdc(3, "Một bóng đèn xe máy loại 12 V - 24 W được cấp nguồn từ acquy 12 V có dung lượng 6 Ah. Giả sử acquy phóng điện ổn định và xả hết 100% dung lượng, thời gian bóng đèn có thể sáng liên tục xấp xỉ bằng:", [
                "3,0 giờ", "6,0 giờ", "1,5 giờ", "4,5 giờ"
            ], 0, "I = P / U = 24 / 12 = 2 A. t = Q / I = 6 Ah / 2 A = 3,0 giờ."),
            make_vdc(4, "Một mạch điện có hiệu điện thế U1 = 6 V thì cường độ dòng điện là I1 = 0,3 A. Nếu muốn cường độ dòng điện tăng thêm 0,2 A nữa (I2 = 0,5 A) thì hiệu điện thế U2 cần đặt vào hai đầu mạch phải bằng:", [
                "10 V", "8 V", "12 V", "15 V"
            ], 0, "R = U1 / I1 = 6 / 0,3 = 20 Ω. U2 = I2 * R = 0,5 * 20 = 10 V.")
        ]
    )

    # ĐỀ 2: Kĩ năng sử dụng Ampe kế và Vôn kế thực hành
    p1_t2 = [
            make_mc(1, "Nhận biết", "Dụng cụ dùng để đo cường độ dòng điện chạy qua một đoạn mạch là:", ["Ampe kế", "Vôn kế", "Nhiệt kế", "Lực kế"], 0, "Ampe kế đo cường độ dòng điện."),
            make_mc(2, "Nhận biết", "Dụng cụ dùng để đo hiệu điện thế giữa hai đầu đoạn mạch hoặc hai cực nguồn là:", ["Vôn kế", "Ampe kế", "Oát kế", "Tốc kế"], 0, "Vôn kế đo hiệu điện thế."),
            make_mc(3, "Nhận biết", "Để đo cường độ dòng điện qua bóng đèn, ampe kế phải được mắc như thế nào?", ["Mắc nối tiếp với bóng đèn", "Mắc song song với bóng đèn", "Mắc vào nguồn không qua đèn", "Mắc ngoài vỏ đui đèn"], 0, "Ampe kế luôn mắc nối tiếp."),
            make_mc(4, "Nhận biết", "Để đo hiệu điện thế hai đầu bóng đèn, vôn kế phải được mắc như thế nào?", ["Mắc song song với bóng đèn", "Mắc nối tiếp với bóng đèn", "Mắc thẳng vào dây nối", "Mắc vào công tắc đang ngắt"], 0, "Vôn kế luôn mắc song song."),
            make_mc(5, "Nhận biết", "Quy tắc cắm chốt nối dây của ampe kế và vôn kế vào mạch điện là:", ["Chốt dương (+) nối về phía cực dương của nguồn, chốt âm (-) về cực âm", "Chốt âm nối cực dương", "Cắm tùy ý không cần phân biệt cực", "Hai chốt cắm chung 1 điểm"], 0, "Cực (+) về phía cực dương nguồn."),
            make_mc(6, "Nhận biết", "Thao tác đầu tiên trước khi dùng ampe kế kim để đo dòng điện là:", ["Chỉnh kim chỉ thị về đúng vạch số 0 (chỉnh zero)", "Lắc mạnh đồng hồ", "Đóng khóa K ngay", "Cắm thẳng vào ổ điện 220 V"], 0, "Chỉnh zero trước khi đo."),
            make_mc(7, "Thông hiểu", "Nếu mắc nhầm ampe kế song song trực tiếp với hai cực của nguồn điện thì điều gì sẽ xảy ra?", ["Gây hiện tượng đoản mạch làm cháy ampe kế và hỏng nguồn", "Kim ampe kế đứng yên", "Vôn kế bị nổ", "Nguồn điện sạc đầy"], 0, "Ampe kế có R rất bé, mắc song song gây đoản mạch cháy đồng hồ."),
            make_mc(8, "Thông hiểu", "Vì sao vôn kế có thể mắc trực tiếp vào hai cực của nguồn điện hở mà không bị cháy?", ["Vì vôn kế có điện trở vô cùng lớn nên dòng điện qua nó vô cùng nhỏ", "Vì vôn kế không dẫn điện", "Vì nguồn không có điện", "Vì vôn kế tự làm mát"], 0, "Điện trở vôn kế rất lớn nên dòng rất bé an toàn."),
            make_mc(9, "Thông hiểu", "Một ampe kế có thang đo gồm 2 thang: 0,6 A và 3 A. Để đo dòng điện dự kiến khoảng 0,4 A, nên chọn thang đo nào?", ["Thang 0,6 A để kim lệch nhiều đọc số chính xác nhất", "Thang 3 A", "Thang nào cũng như nhau", "Không đo được"], 0, "Chọn thang 0,6 A gần với 0,4 A giúp đọc số đo rõ và chính xác."),
            make_mc(10, "Thông hiểu", "Khi mắc vôn kế vào mạch điện mà kim chỉ thị bị quay ngược về bên trái vạch số 0, lỗi sai ở đây là:", ["Chốt (+) và chốt (-) của vôn kế bị mắc ngược cực", "Hiệu điện thế quá lớn", "Mạch điện bị chập", "Vôn kế hết pin"], 0, "Ngược cực làm lực điện từ đẩy kim theo chiều ngược lại."),
            make_mc(11, "Thông hiểu", "Khi đọc số chỉ trên bảng chia độ của ampe kế hoặc vôn kế kim, tư thế đặt mắt chuẩn là:", ["Đặt mắt nhìn vuông góc với mặt kính của bảng chia độ", "Nhìn nghiêng từ bên trái", "Nhìn nghiêng từ bên phải", "Nhìn từ dưới lên"], 0, "Nhìn vuông góc để tránh sai số thị sai."),
            make_mc(12, "Thông hiểu", "Nếu dòng điện cần đo vượt quá giới hạn đo (GHĐ) của ampe kế thì có thể dẫn đến hậu quả:", ["Kim va đập mạnh làm cong gãy kim hoặc cháy cuộn dây ampe kế", "Kim quay tròn liên tục", "Pin yếu đi", "Ampe kế tự biến thành vôn kế"], 0, "Quá tải thang đo làm cháy kim đồng hồ.")
    ]

    p2_t2 = [
        make_tf(1, "Thông hiểu", "Về cách mắc và nguyên tắc đo của Ampe kế trong mạch đề 2:", [
            ("a", "Ampe kế đo dòng điện chạy qua chính bản thân nó.", True),
            ("b", "Ampe kế lí tưởng có điện trở bằng 0 để không làm thay đổi dòng trong mạch.", True),
            ("c", "Có thể dùng ampe kế có GHĐ 100 mA để đo dòng điện 2 A của bàn là.", False),
            ("d", "Chốt âm (-) của ampe kế phải hướng về phía cực âm của nguồn điện.", True)
        ], "Dòng 2 A quá lớn làm cháy ampe kế 100 mA."),
        make_tf(2, "Thông hiểu", "Về cách mắc và nguyên tắc đo của Vôn kế trong mạch đề 2:", [
            ("a", "Vôn kế được mắc song song với thiết bị cần xác định độ giảm thế.", True),
            ("b", "Vôn kế lí tưởng có điện trở vô cùng lớn để không làm rẽ dòng mạch chính.", True),
            ("c", "Mắc nối tiếp vôn kế vào mạch thắp sáng bóng đèn thì đèn vẫn sáng bình thường.", False),
            ("d", "Vôn kế đo hiệu điện thế giữa hai điểm mà hai chốt đo của nó tiếp xúc.", True)
        ], "Vôn kế mắc nối tiếp sẽ cản trở gần như toàn bộ dòng điện làm đèn tắt."),
        make_tf(3, "Thông hiểu", "Về thao tác chọn thang đo và giảm sai số thực hành đề 2:", [
            ("a", "Luôn chọn thang đo có GHĐ lớn hơn giá trị ước lượng cần đo.", True),
            ("b", "Độ chia nhỏ nhất của dụng cụ càng nhỏ thì phép đo có độ chính xác tiềm năng càng cao.", True),
            ("c", "Chỉ cần đo 1 lần duy nhất là kết quả đã đạt độ tin cậy tuyệt đối.", False),
            ("d", "Sau khi hoàn thành thí nghiệm phải ngắt công tắc và rút dây khỏi các chốt đo.", True)
        ], "Cần đo lặp lại nhiều lần lấy trung bình cộng để giảm sai số."),
        make_tf(4, "Thông hiểu", "Về nhận diện sự cố và khắc phục khi dùng đồng hồ đo điện đề 2:", [
            ("a", "Nếu kim đồng hồ không chỉ số 0 trước khi đo, dùng tuốc-nơ-vít chỉnh núm xoay zero.", True),
            ("b", "Khi kim vôn kế bị lệch ngược, ta chỉ cần đảo chốt cắm dây của vôn kế lại cho đúng cực.", True),
            ("c", "Nếu kim chỉ thị vượt quá giới hạn đo, ta phải giữ nguyên mạch và ép kim lại bằng tay.", False),
            ("d", "Đồng hồ đa năng số (DMM) hiển thị trực tiếp giá trị bằng các con số trên màn hình LCD.", True)
        ], "Phải ngắt mạch ngay và chuyển sang thang đo lớn hơn.")
    ]

    p3_t2 = [
        make_sa(1, "Thông hiểu", "Một ampe kế có giới hạn đo 3 A và có 30 vạch chia đều. Kim ampe kế đang chỉ ở vạch thứ 15. Giá trị dòng điện đo được là bao nhiêu Ampe (A)?", "1.5", "I = (3 / 30) * 15 = 1,5 A."),
        make_sa(2, "Thông hiểu", "Một vôn kế có thang đo cực đại 15 V gồm 75 vạch chia. Khi đo hiệu điện thế pin, kim chỉ vạch thứ 45. Giá trị hiệu điện thế đo được là bao nhiêu Vôn (V)?", "9", "U = (15 / 75) * 45 = 9 V."),
        make_sa(3, "Thông hiểu", "Một ampe kế có giới hạn đo 500 mA gồm 50 vạch. Độ chia nhỏ nhất của ampe kế này là bao nhiêu miliampe (mA)?", "10", "ĐCNN = 500 / 50 = 10 mA."),
        make_sa(4, "Thông hiểu", "Để đo dòng điện dự đoán 1,8 A, ta có các ampe kế có GHĐ: (A) 0,5 A; (B) 2 A; (C) 10 A. Ampe kế nào phù hợp và đọc chính xác nhất? (Ghi chữ cái A, B hoặc C).", "B", "GHĐ 2 A lớn hơn 1,8 A và gần nhất."),
        make_sa(5, "Vận dụng", "Khi mắc vôn kế vào hai cực một viên pin thì vôn kế chỉ 4,5 V. Nếu mắc nối tiếp thêm một pin 1,5 V cùng chiều thì vôn kế chỉ bao nhiêu Vôn (V)?", "6", "U = 4,5 + 1,5 = 6 V."),
        make_sa(6, "Vận dụng", "Một ampe kế có điện trở nội 0,2 Ω. Khi có dòng điện 1,5 A chạy qua, hiệu điện thế sụt trên ampe kế là bao nhiêu Vôn (V)?", "0.3", "U = I * R = 1,5 * 0,2 = 0,3 V.")
    ]

    p4_t2 = [
        make_vdc(1, "Một khung đo miliampe kế có thang đo cực đại I0 = 10 mA và điện trở cuộn dây r0 = 90 Ω. Để mở rộng dải đo thành ampe kế có giới hạn đo I = 1 A, cần mắc song song một điện trở sun Rs có giá trị bằng:", [
            "0,909 Ω", "0,1 Ω", "9,0 Ω", "1,0 Ω"
        ], 0, "Rs = (I0 * r0) / (I - I0) = (0,01 * 90) / (1 - 0,01) = 0,9 / 0,99 ≈ 0,909 Ω."),
        make_vdc(2, "Cũng với miliampe kế trên (I0 = 10 mA, r0 = 90 Ω), để chế tạo thành vôn kế đo được hiệu điện thế tối đa U = 10 V, cần mắc nối tiếp một điện trở phụ Rp có giá trị là:", [
            "910 Ω", "1000 Ω", "900 Ω", "1090 Ω"
        ], 0, "Rp = (U / I0) - r0 = (10 / 0,01) - 90 = 1000 - 90 = 910 Ω."),
        make_vdc(3, "Một vôn kế có điện trở Rv = 5000 Ω được mắc vào hai đầu một điện trở R = 1000 Ω đang có dòng điện mạch chính 0,012 A chạy qua. Sai số do vôn kế gây ra làm điện trở tương đương của đoạn mạch giảm xuống còn:", [
            "833,3 Ω", "1000 Ω", "950 Ω", "500 Ω"
        ], 0, "Rtd = (1000 * 5000) / (1000 + 5000) = 5000 / 6 ≈ 833,3 Ω."),
        make_vdc(4, "Một mạch điện có sơ đồ gồm nguồn E = 9 V, ampe kế có điện trở Ra = 1 Ω mắc nối tiếp với bóng đèn có điện trở Rđ = 17 Ω. Số chỉ của ampe kế khi mạch đóng là:", [
            "0,5 A", "0,53 A", "1,0 A", "0,25 A"
        ], 0, "I = E / (Ra + Rđ) = 9 / (1 + 17) = 9 / 18 = 0,5 A.")
    ]

    exams[f"{l_id}_test2"] = meta(2, p1_t2, p2_t2, p3_t2, p4_t2)

    # ĐỀ 3: Bản chất hạt electron, Liên hệ q = I.t & Tốc độ dịch chuyển
    exams[f"{l_id}_test3"] = meta(3,
        [
            make_mc(1, "Nhận biết", "Điện tích nguyên tố của một hạt electron có độ lớn tuyệt đối là:", ["e ≈ 1,6 . 10^-19 Culông (C)", "e ≈ 1,6 . 10^-16 C", "e ≈ 9,1 . 10^-31 C", "e = 1 C"], 0, "Độ lớn điện tích nguyên tố là 1,6 . 10^-19 C."),
            make_mc(2, "Nhận biết", "Công thức liên hệ giữa điện lượng q, cường độ dòng điện I và thời gian t là:", ["q = I × t", "q = I / t", "q = t / I", "q = I + t"], 0, "q = I * t."),
            make_mc(3, "Nhận biết", "Số hạt electron N chuyển qua tiết diện dây dẫn khi có điện lượng q dịch chuyển được tính bởi công thức:", ["N = q / e", "N = q × e", "N = e / q", "N = q + e"], 0, "N = q / e."),
            make_mc(4, "Nhận biết", "Trong kim loại, các electron tự do chuyển động nhiệt hỗn loạn theo mọi hướng khi:", ["Chưa có điện trường (chưa nối với nguồn điện)", "Có dòng điện chạy qua", "Dây dẫn bị đứt", "Ở nhiệt độ 0 tuyệt đối"], 0, "Khi không có điện trường, electron chuyển động nhiệt hỗn loạn."),
            make_mc(5, "Nhận biết", "Khi nối hai đầu dây kim loại vào nguồn điện, các electron tự do ngoài chuyển động nhiệt còn có thêm:", ["Chuyển động có hướng ngược chiều điện trường", "Chuyển động quay tròn tại chỗ", "Chuyển động rơi tự do", "Đứng yên hoàn toàn"], 0, "Electron dịch chuyển có hướng ngược chiều điện trường."),
            make_mc(6, "Nhận biết", "Tốc độ dịch chuyển có hướng (tốc độ trôi) của các electron tự do trong dây dẫn kim loại thường có giá trị:", ["Rất nhỏ, chỉ khoảng vài milimét trên một giây (mm/s)", "Bằng tốc độ ánh sáng 300 000 km/s", "Bằng tốc độ âm thanh 340 m/s", "Bằng 0"], 0, "Tốc độ trôi của electron rất chậm (khoảng vài mm/s đến cm/s)."),
            make_mc(7, "Thông hiểu", "Mặc dù tốc độ trôi của electron rất nhỏ, bóng đèn vẫn sáng ngay lập tức khi bật công tắc vì:", ["Tốc độ truyền điện trường trong dây dẫn xấp xỉ bằng tốc độ ánh sáng (300 000 km/s)", "Bóng đèn có pin dự phòng", "Electron tự nhảy vọt qua không gian", "Dây dẫn tự co lại"], 0, "Điện trường lan truyền với vận tốc ánh sáng."),
            make_mc(8, "Thông hiểu", "Dòng điện 1 Ampe chạy qua dây dẫn tương ứng với lượng điện tích chuyển qua tiết diện trong 1 giây là:", ["1 Culông (1 C)", "10 Culông", "1000 Culông", "0,1 Culông"], 0, "1 A = 1 C / 1 s."),
            make_mc(9, "Thông hiểu", "Khi tăng cường độ dòng điện chạy qua một dây dẫn lên gấp 3 lần, lượng điện tích chuyển qua tiết diện dây trong cùng một khoảng thời gian sẽ:", ["Tăng lên gấp 3 lần", "Giảm đi 3 lần", "Không đổi", "Tăng lên gấp 9 lần"], 0, "q = I * t tỉ lệ thuận với I."),
            make_mc(10, "Thông hiểu", "Mật độ electron tự do trong kim loại đồng xấp xỉ khoảng:", ["8,5 . 10^28 electron/m3", "10^10 electron/m3", "1000 electron/m3", "10^50 electron/m3"], 0, "Mật độ electron tự do trong đồng rất lớn, khoảng 10^28 đến 10^29 hạt/m3."),
            make_mc(11, "Thông hiểu", "Đồ thị biểu diễn mối liên hệ giữa điện lượng q chuyển qua dây dẫn và thời gian t (khi I không đổi) là:", ["Một đoạn thẳng đi qua gốc tọa độ O", "Một đường cong parabol", "Một đường tròn", "Một đường nằm ngang song song trục hoành"], 0, "q tỉ lệ thuận với t, đồ thị là đường thẳng qua O."),
            make_mc(12, "Thông hiểu", "Một hạt bụi mang điện tích -3,2 . 10^-18 C. Số hạt electron thừa bám trên hạt bụi này là:", ["20 electron", "2 electron", "200 electron", "10 electron"], 0, "N = 3,2e-18 / 1,6e-19 = 20 hạt.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về bản chất vi mô của dòng điện trong dây dẫn kim loại đề 3:", [
                ("a", "Electron mang điện tích âm có giá trị q = -1,6 . 10^-19 Culông.", True),
                ("b", "Các hạt proton trong hạt nhân kim loại cũng dịch chuyển tự do dọc theo chiều dài của dây dẫn.", False),
                ("c", "Chiều chuyển động có hướng của electron tự do là từ cực âm về cực dương của nguồn điện.", True),
                ("d", "Tốc độ truyền tín hiệu điện trường bằng đúng tốc độ dịch chuyển có hướng của từng hạt electron.", False)
            ], "Proton gắn chặt trong mạng tinh thể; tốc độ điện trường nhanh hơn tốc độ trôi hàng tỉ lần."),
            make_tf(2, "Thông hiểu", "Về tính toán điện lượng và dòng điện không đổi đề 3:", [
                ("a", "Điện lượng q đo bằng Culông (kí hiệu là C).", True),
                ("b", "Dòng điện không đổi là dòng điện có chiều và cường độ không thay đổi theo thời gian.", True),
                ("c", "Nếu trong 10 giây có 5 C điện tích chuyển qua tiết diện thì cường độ dòng điện là 2 A.", False),
                ("d", "Cường độ dòng điện là đại lượng đo bằng thương số giữa điện lượng q và thời gian t dịch chuyển.", True)
            ], "I = q / t = 5 / 10 = 0,5 A."),
            make_tf(3, "Thông hiểu", "Về tốc độ trôi của electron và điện trường trong dây dẫn đề 3:", [
                ("a", "Tốc độ dịch chuyển có hướng của electron tỉ lệ thuận với cường độ dòng điện chạy qua dây.", True),
                ("b", "Với cùng dòng điện, dây dẫn có tiết diện càng nhỏ thì tốc độ trôi của electron càng lớn.", True),
                ("c", "Chuyển động nhiệt của các electron tự do hoàn toàn biến mất khi có điện trường xuất hiện.", False),
                ("d", "Chuyển động có hướng của electron được xếp chồng lên trên chuyển động nhiệt hỗn loạn.", True)
            ], "Chuyển động nhiệt vẫn tiếp tục diễn ra hỗn loạn."),
            make_tf(4, "Thông hiểu", "Về sự tương tác điện tích và cân bằng điện trong nguyên tử đề 3:", [
                ("a", "Một vật trung hòa về điện khi tổng điện tích dương bằng tổng điện tích âm.", True),
                ("b", "Khi một thanh kim loại mất bớt một số electron thì nó trở thành vật nhiễm điện dương.", True),
                ("c", "Điện tích của một vật bất kì luôn là một số nguyên lần điện tích nguyên tố e.", True),
                ("d", "Electron có thể bị phân chia thành các mảnh nhỏ mang điện tích lẻ như 0,1e trong điều kiện thường.", False)
            ], "Điện tích nguyên tố là điện tích nhỏ nhất không thể phân chia trong tự nhiên.")
        ],
        [
            make_sa(1, "Thông hiểu", "Dòng điện I = 0,8 A chạy qua dây tóc bóng đèn trong 40 giây. Điện lượng chuyển qua dây tóc là bao nhiêu Culông (C)?", "32", "q = 0,8 * 40 = 32 C."),
            make_sa(2, "Thông hiểu", "Một điện tích q = 48 C chuyển qua một tiết diện thẳng trong thời gian 1 phút (60 giây). Cường độ dòng điện là bao nhiêu Ampe (A)?", "0.8", "I = 48 / 60 = 0,8 A."),
            make_sa(3, "Thông hiểu", "Có 5 . 10^19 electron dịch chuyển qua tiết diện thẳng của dây dẫn. Biết e = 1,6 . 10^-19 C. Điện lượng tổng cộng là bao nhiêu Culông (C)?", "8", "q = 5e19 * 1,6e-19 = 8 C."),
            make_sa(4, "Thông hiểu", "Dòng điện I = 1,6 A chạy qua một ống phóng điện tử. Số electron phóng qua trong 1 giây là bao nhiêu hạt? (Viết hệ số của 10^19 hạt, ví dụ 1.0).", "1.0", "N = (1,6 * 1) / 1,6e-19 = 1,0 . 10^19 hạt."),
            make_sa(5, "Vận dụng", "Trong 5 phút (300 giây), một ắc quy phóng điện với dòng 2 A. Tổng điện tích đã phóng ra khỏi cực acquy là bao nhiêu Culông (C)?", "600", "q = 2 * 300 = 600 C."),
            make_sa(6, "Vận dụng", "Một tụ điện tích được điện lượng 0,006 C ở hiệu điện thế 12 V. Nếu phóng hết điện tích này trong thời gian 0,002 giây thì dòng điện phóng trung bình là bao nhiêu Ampe (A)?", "3", "I = 0,006 / 0,002 = 3 A.")
        ],
        [
            make_vdc(1, "Một dây dẫn bằng đồng có tiết diện thẳng S = 1 mm2 (10^-6 m2) có dòng điện I = 1,7 A chạy qua. Biết mật độ electron tự do trong đồng n = 8,5 . 10^28 hạt/m3 và điện tích e = 1,6 . 10^-19 C. Tốc độ dịch chuyển có hướng trung bình của electron trong dây đồng là:", [
                "0,125 mm/s", "1,25 mm/s", "12,5 mm/s", "0,0125 mm/s"
            ], 0, "v = I / (n * e * S) = 1,7 / (8,5e28 * 1,6e-19 * 1e-6) = 1,7 / 13,6 = 0,125 mm/s."),
            make_vdc(2, "Một chùm hạt electron trong ống đèn hình vô tuyến chuyển động với vận tốc v = 4 . 10^7 m/s tạo thành một dòng điện có cường độ I = 0,8 mA. Số electron bay đến đập vào màn hình huỳnh quang trong mỗi giây là:", [
                "5 . 10^15 hạt", "5 . 10^18 hạt", "8 . 10^15 hạt", "1,6 . 10^16 hạt"
            ], 0, "N = I / e = (0,8 . 10^-3) / (1,6 . 10^-19) = 5 . 10^15 hạt/giây."),
            make_vdc(3, "Một viên pin điện thoại dung lượng 4000 mAh (tương đương 4 Ah). Khi chơi game liên tục, điện thoại tiêu thụ dòng điện trung bình 800 mA. Thời gian chơi game liên tục cho đến khi cạn pin là:", [
                "5,0 giờ", "4,0 giờ", "3,2 giờ", "2,5 giờ"
            ], 0, "t = 4000 mAh / 800 mA = 5,0 giờ."),
            make_vdc(4, "Một dây dẫn đồng dài L = 100 m dẫn dòng điện 5 A. Tổng số electron tự do tham gia dẫn điện có mặt trong toàn bộ đoạn dây dẫn đồng (tiết diện S = 2 mm2, mật độ n = 8,5 . 10^28 m^-3) xấp xỉ bằng:", [
                "1,7 . 10^25 hạt", "8,5 . 10^24 hạt", "3,4 . 10^26 hạt", "1,7 . 10^23 hạt"
            ], 0, "V = S * L = (2 . 10^-6) * 100 = 2 . 10^-4 m3. N = n * V = 8,5e28 * 2e-4 = 1,7 . 10^25 hạt.")
        ]
    )

    return exams
