# -*- coding: utf-8 -*-
# generate_c5_part2.py
import os
import sys

code = '''# -*- coding: utf-8 -*-
"""
CHƯƠNG V - PHẦN 2 (14 ĐỀ THI ĐỘC LẬP 100%):
- phys8_c5_b23: Bài 23: Tác dụng của dòng điện (3 đề)
- phys8_c5_b24: Bài 24: Cường độ dòng điện và hiệu điện thế (3 đề)
- phys8_c5_b25: Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế (3 đề)
- phys8_c5_rev: [Đề tổng hợp] Ôn tập cuối Chương V (5 đề)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid, "level": level, "question": q_text,
        "options": options, "correct": correct_idx, "explanation": explanation
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid, "level": level, "question": prompt,
        "statements": [{"subId": s[0], "text": s[1], "correct": s[2]} for s in statements],
        "explanation": explanation
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid, "level": level, "question": q_text,
        "correctAnswer": str(answer).strip(), "explanation": explanation
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid, "level": "Vận dụng cao", "question": q_text,
        "options": options, "correct": correct_idx, "explanation": explanation
    }

def get_c5_part2_exams():
    exams = {}
    ch_id = "phys8_c5"
    ch_title = "Chương V: Điện"

    def meta(l_id, l_name, t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # =========================================================================
    # BÀI 23: TÁC DỤNG CỦA DÒNG ĐIỆN (3 ĐỀ)
    # =========================================================================
    l23_id = "phys8_c5_b23"
    l23_name = "Bài 23: Tác dụng của dòng điện"

    for t in range(1, 4):
        p_dev = ["ấm đun siêu tốc", "bàn là điện", "nồi cơm điện"][t-1]
        p_metal = ["đồng (Cu)", "bạc (Ag)", "vàng (Au)"][t-1]
        p_sol = ["dung dịch copper sulfate (CuSO4)", "dung dịch silver nitrate (AgNO3)", "dung dịch muối vàng dicyanoaurate"][t-1]
        p_core = ["lõi sắt non", "lõi thép mềm", "thanh tôn silic mềm"][t-1]
        p_n = [150 + t*50, 200 + t*50, 300 + t*50][t-1]
        p_u = [6 + t*2, 12 + t*2, 24 + t*2][t-1]
        p_i = [1.2 + t*0.3, 1.8 + t*0.2, 2.5 + t*0.5][t-1]

        p1 = [
            make_mc(1, "Nhận biết", f"Thiết bị nào sau đây hoạt động chủ yếu dựa trên tác dụng nhiệt của dòng điện trong nhóm {t}?", [p_dev.capitalize(), "Quạt máy", "Chuông điện", "Đèn pin LED"], 0, f"{p_dev.capitalize()} biến đổi điện năng thành nhiệt năng nhờ tác dụng nhiệt."),
            make_mc(2, "Nhận biết", f"Dòng điện chạy qua cuộn dây dẫn quấn quanh {p_core} làm cuộn dây có khả năng hút đinh sắt. Hiện tượng này thể hiện tác dụng gì?", ["Tác dụng từ", "Tác dụng nhiệt", "Tác dụng quang", "Tác dụng hóa học"], 0, "Dòng điện qua cuộn dây sinh ra từ trường hút sắt thép."),
            make_mc(3, "Nhận biết", f"Trong kĩ thuật mạ điện kim loại {p_metal}, vật cần mạ phải được gắn vào cực nào của nguồn điện một chiều?", ["Cực âm (catot)", "Cực dương (anot)", "Cực nào cũng được", "Không cần nối điện"], 0, f"Ion {p_metal} mang điện tích dương chuyển dịch về cực âm bám vào vật mạ."),
            make_mc(4, "Nhận biết", f"Đèn điốt phát quang (đèn LED) phát sáng khi nối với nguồn điện {p_u} V là nhờ tác dụng nào?", ["Tác dụng phát sáng (tác dụng quang)", "Tác dụng nhiệt dây tóc nóng đỏ", "Tác dụng từ của bán dẫn", "Tác dụng hóa học"], 0, "Đèn LED phát quang bán dẫn trực tiếp khi có dòng điện thích hợp."),
            make_mc(5, "Nhận biết", f"Hiện tượng dòng điện chạy qua cơ thể người gây co giật cơ bắp và ngừng thở thể hiện tác dụng nào của dòng điện?", ["Tác dụng sinh lí", "Tác dụng nhiệt", "Tác dụng cơ học", "Tác dụng hóa học"], 0, "Dòng điện tác động lên hệ thần kinh và cơ, đó là tác dụng sinh lí."),
            make_mc(6, "Nhận biết", f"Bút thử điện chứa khí neon phát sáng ở điện áp trên {40 + t*5} V dựa trên tác dụng gì?", ["Tác dụng phát sáng", "Tác dụng nhiệt đốt nóng", "Tác dụng từ", "Tác dụng hóa học"], 0, "Chất khí neon bị ion hóa phát quang trong điện trường."),
            make_mc(7, "Thông hiểu", f"Một nam châm điện có cuộn dây {p_n} vòng. Để làm tăng lực từ hút đinh sắt của nam châm này, cách nào sau đây là hiệu quả nhất?", ["Tăng cường độ dòng điện chạy qua cuộn dây", "Giảm số vòng dây của cuộn", "Thay lõi sắt bằng lõi đồng", "Đổi chiều nguồn điện"], 0, "Tăng cường độ dòng điện hoặc số vòng dây làm tăng từ tính."),
            make_mc(8, "Thông hiểu", f"Khi dòng điện chạy qua {p_sol} nối hai điện cực than, lớp {p_metal} bám vào cực âm chứng tỏ dòng điện có:", ["Tác dụng hóa học", "Tác dụng nhiệt", "Tác dụng từ", "Tác dụng sinh lí"], 0, "Hiện tượng điện phân giải phóng kim loại là tác dụng hóa học."),
            make_mc(9, "Thông hiểu", f"Dây chì trong cầu chì ngắt mạch điện tự động khi đoản mạch ở mạch {t} là ứng dụng của:", ["Tác dụng nhiệt khi dòng điện tăng vọt", "Tác dụng từ hút đứt dây", "Tác dụng phát sáng nổ dây", "Tác dụng hóa học ăn mòn"], 0, "Dòng điện tăng vọt sinh nhiệt làm chảy đứt dây chì."),
            make_mc(10, "Thông hiểu", f"Trong y học, máy khử rung tim (sốc tim) truyền xung điện qua lồng ngực là ứng dụng có ích của:", ["Tác dụng sinh lí của dòng điện", "Tác dụng từ trường", "Tác dụng hóa học tế bào", "Tác dụng nhiệt sưởi ấm tim"], 0, "Kích thích tái lập nhịp tim bằng dòng điện là ứng dụng tác dụng sinh lí."),
            make_mc(11, "Thông hiểu", f"Cần cẩu điện hút các tấm sắt vụn phế liệu hoạt động dựa vào tác dụng nào?", ["Tác dụng từ của nam châm điện", "Tác dụng tĩnh điện hút giấy", "Tác dụng hóa học kết tủa", "Tác dụng phát quang"], 0, "Nam châm điện cực lớn tạo lực từ nâng sắt vụn."),
            make_mc(12, "Thông hiểu", f"Khi đổi chiều dòng điện chạy qua một nam châm điện, điều gì sẽ xảy ra?", ["Các cực từ (Bắc - Nam) của nam châm điện đổi chiều cho nhau", "Nam châm điện mất hết từ tính", "Lực hút tăng gấp đôi", "Nam châm biến thành thanh đồng"], 0, "Đổi chiều dòng điện làm đảo chiều các cực từ.")
        ]

        p2 = [
            make_tf(1, "Thông hiểu", f"Về các tác dụng nhiệt và tác dụng phát sáng của dòng điện đợt {t}:", [
                ("a", f"Trong {p_dev}, tác dụng nhiệt là tác dụng chính có ích được khai thác.", True),
                ("b", "Bóng đèn sợi đốt phát sáng do dây tóc vonfram bị nung nóng đến nhiệt độ rất cao.", True),
                ("c", "Đèn LED phát sáng tiêu thụ điện năng nhiều hơn và tỏa nhiệt nhiều hơn đèn sợi đốt.", False),
                ("d", "Khi có dòng điện chạy qua mọi dây dẫn bằng kim loại thì dây luôn luôn tỏa một lượng nhiệt.", True)
            ], "Dòng điện qua điện trở luôn tỏa nhiệt; đèn LED tỏa nhiệt ít và tiết kiệm điện hơn đèn sợi đốt."),
            make_tf(2, "Thông hiểu", f"Về tác dụng từ và cấu tạo của nam châm điện nhóm thí nghiệm {t}:", [
                ("a", f"Nam châm điện gồm một cuộn dây quấn quanh {p_core}.", True),
                ("b", "Nếu thay lõi sắt non bằng lõi gỗ khô thì từ tính của nam châm điện sẽ tăng lên gấp bội.", False),
                ("c", f"Khi tăng số vòng dây từ {p_n} vòng lên {p_n + 150} vòng, lực từ của nam châm điện sẽ mạnh hơn.", True),
                ("d", "Khi ngắt dòng điện chạy qua cuộn dây, lõi sắt non giữ nguyên từ tính vĩnh viễn.", False)
            ], "Sắt non tăng từ trường khi có dòng điện và mất gần hết từ tính ngay khi ngắt điện."),
            make_tf(3, "Thông hiểu", f"Về tác dụng hóa học và công nghệ mạ điện kim loại {p_metal}:", [
                ("a", f"Bình điện phân đựng {p_sol} là môi trường dẫn điện nhờ các ion chuyển động có hướng.", True),
                ("b", f"Vật cần mạ kim loại {p_metal} phải được nối vào cực âm của nguồn điện một chiều.", True),
                ("c", f"Thanh kim loại {p_metal} nguyên chất được nối vào cực dương để hòa tan bù ion vào dung dịch.", True),
                ("d", "Có thể dùng dòng điện xoay chiều 220 V trong lưới điện gia đình để mạ điện trực tiếp mà không cần chỉnh lưu.", False)
            ], "Mạ điện bắt buộc phải dùng dòng điện một chiều DC."),
            make_tf(4, "Thông hiểu", f"Về tác dụng sinh lí và các biện pháp bảo đảm an toàn điện phòng thí nghiệm {t}:", [
                ("a", "Dòng điện có cường độ trên 10 mA chạy qua cơ thể người đã có thể gây nguy hiểm co cơ không tự chủ.", True),
                ("b", "Dòng điện chỉ gây bỏng da ngoài, hoàn toàn không ảnh hưởng tới nhịp tim và hệ hô hấp.", False),
                ("c", "Khi có người bị điện giật, việc đầu tiên cần làm là ngắt ngay nguồn điện trước khi tiếp cận nạn nhân.", True),
                ("d", "Dùng thanh tre tươi hoặc dây sắt để gạt dây điện dính vào người nạn nhân.", False)
            ], "Thanh tre tươi và dây sắt đều dẫn điện, phải dùng vật cách điện khô.")
        ]

        p3 = [
            make_sa(1, "Thông hiểu", f"Một ấm đun nước hoạt động ở hiệu điện thế 220 V với cường độ dòng điện {p_i:.1f} A. Công suất tỏa nhiệt của ấm là bao nhiêu Oát (W)?", f"{round(220 * p_i)}", f"P = U * I = 220 * {p_i:.1f} = {round(220 * p_i)} W."),
            make_sa(2, "Thông hiểu", f"Một nam châm điện có {p_n} vòng dây hút được {12 + t*4} chiếc đinh ghim nhỏ. Khi quấn thêm {50*t} vòng dây thì số đinh hút được tăng thêm {6 + t*2} chiếc. Tổng số đinh ghim hút được lúc sau là bao nhiêu chiếc?", f"{(12 + t*4) + (6 + t*2)}", f"Tổng số đinh = {(12 + t*4)} + {(6 + t*2)} = {(12 + t*4) + (6 + t*2)} chiếc."),
            make_sa(3, "Vận dụng", f"Khi điện phân {p_sol} trong {10*t} phút, khối lượng {p_metal} bám vào cực âm là {0.15*t:.2f} g. Nếu kéo dài thời gian điện phân lên gấp 4 lần với cùng cường độ dòng điện thì khối lượng kim loại bám vào là bao nhiêu gam?", f"{round(0.15*t * 4, 2)}", f"m = {0.15*t:.2f} * 4 = {round(0.15*t * 4, 2)} g."),
            make_sa(4, "Thông hiểu", f"Một đèn LED hoạt động bình thường với hiệu điện thế 2,2 V. Để mắc đèn vào nguồn pin {p_u} V, người ta mắc nối tiếp đèn với một điện trở phụ. Hiệu điện thế đặt lên điện trở phụ bằng bao nhiêu Vôn (V)?", f"{round(p_u - 2.2, 1)}", f"U_R = {p_u} - 2.2 = {round(p_u - 2.2, 1)} V."),
            make_sa(5, "Thông hiểu", f"Một cần cẩu dùng nam châm điện nâng được khối sắt có trọng lượng {2000 + t*1000} N. Lực từ nâng tối thiểu mà nam châm điện tạo ra để giữ yên khối sắt này là bao nhiêu Niutơn (N)?", f"{2000 + t*1000}", f"Lực nâng tối thiểu bằng trọng lượng vật: F = P = {2000 + t*1000} N."),
            make_sa(6, "Vận dụng", f"Bút thử điện chứa khí neon có điện trở rất lớn R = {1.5 + t*0.5:.1f} MΩ ({int((1.5 + t*0.5)*1000000)} Ω). Khi chạm vào điện áp 220 V, cường độ dòng điện chạy qua cơ thể xuống đất bằng bao nhiêu miliampe (mA)? (Làm tròn đến 3 chữ số thập phân).", f"{round(220 / ((1.5 + t*0.5)*1000000) * 1000, 3)}", f"I = 220 / {(1.5 + t*0.5)*1000000:.0f} * 1000 = {round(220 / ((1.5 + t*0.5)*1000000) * 1000, 3)} mA.")
        ]

        vdc_thick = 20 + t*5
        vdc_s = 0.05 + t*0.02
        vdc_dens = 8900 if 'đồng' in p_metal else 10500 if 'bạc' in p_metal else 19300
        vdc_m = round(vdc_s * (vdc_thick * 1e-6) * vdc_dens * 1000, 2)
        p4 = [
            make_vdc(1, f"Một phân xưởng mạ điện cần mạ một lớp {p_metal} dày {vdc_thick} μm (1 μm = 10^-6 m) lên bề mặt một tấm kim loại có diện tích S = {vdc_s:.2f} m2. Biết khối lượng riêng của {p_metal} là D = {vdc_dens} kg/m3. Khối lượng kim loại {p_metal} cần bám lên bề mặt tấm kim loại xấp xỉ bằng:", [
                f"{vdc_m} g", f"{round(vdc_m * 2, 2)} g", f"{round(vdc_m * 0.5, 2)} g", f"{round(vdc_m * 10, 2)} g"
            ], 0, f"V = S * h = {vdc_s:.2f} * {vdc_thick}e-6 m3. m = D * V = {vdc_m} g."),
            make_vdc(2, f"Một chuông điện sử dụng nam châm điện có điện trở R = {10 + t*2} Ω nối với nguồn điện U = {p_u} V. Khi đóng mạch điện, lá thép bị hút gõ vào chuông {15 + t*5} lần/giây. Cường độ dòng điện chạy qua cuộn dây nam châm điện và năng lượng tiêu thụ trong 1 phút là:", [
                f"I = {round(p_u / (10 + t*2), 2)} A; Q = {round((p_u**2 / (10 + t*2)) * 60)} J",
                f"I = {round(p_u / (10 + t*2) * 2, 2)} A; Q = 500 J",
                f"I = 0,5 A; Q = 1000 J",
                f"I = 1,0 A; Q = 2500 J"
            ], 0, f"I = U / R = {round(p_u / (10 + t*2), 2)} A. Q = U * I * t = {round((p_u**2 / (10 + t*2)) * 60)} J."),
            make_vdc(3, f"Một ấm điện có công suất {800 + t*200} W đun sôi {0.8 + t*0.2:.1f} lít nước từ 25°C đến 100°C. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K) và hiệu suất ấm đạt {80 + t*2}%. Thời gian đun sôi nước xấp xỉ bằng:", [
                f"{round((0.8 + t*0.2) * 4200 * 75 / ((800 + t*200) * (80 + t*2)/100) / 60, 1)} phút",
                f"{round((0.8 + t*0.2) * 4200 * 75 / ((800 + t*200) * (80 + t*2)/100) / 60 * 1.5, 1)} phút",
                f"12,5 phút",
                f"2,0 phút"
            ], 0, f"Q_thu = m.c.Δt = {(0.8+t*0.2)*4200*75} J. A = Q / H. t = A / P."),
            make_vdc(4, f"Trong một cần cẩu điện, lực từ F hút khối sắt tỉ lệ thuận với bình phương cường độ dòng điện (F = k.I^2). Khi dòng điện I1 = {1.0 + t*0.2:.1f} A thì cần cẩu nâng được khối lượng m1 = {200 + t*50} kg. Để cần cẩu nâng được khối lượng m2 = {450 + t*50} kg thì dòng điện I2 cần điều chỉnh bằng:", [
                f"{round((1.0 + t*0.2) * ((450 + t*50) / (200 + t*50))**0.5, 2)} A",
                f"{round((1.0 + t*0.2) * 2, 2)} A",
                f"3,5 A",
                f"1,5 A"
            ], 0, f"I2 / I1 = sqrt(m2 / m1) => I2 = {round((1.0 + t*0.2) * ((450 + t*50) / (200 + t*50))**0.5, 2)} A.")
        ]

        exams[f"{l23_id}_test{t}"] = meta(l23_id, l23_name, t, p1, p2, p3, p4)

    # =========================================================================
    # BÀI 24: CƯỜNG ĐỘ DÒNG ĐIỆN VÀ HIỆU ĐIỆN THẾ (3 ĐỀ)
    # =========================================================================
    l24_id = "phys8_c5_b24"
    l24_name = "Bài 24: Cường độ dòng điện và hiệu điện thế"

    for t in range(1, 4):
        p_ma = [120 + t*40, 250 + t*50, 400 + t*50][t-1]
        p_kv = [0.22 + t*0.06, 0.5 + t*0.1, 1.2 + t*0.3][t-1]
        p_bat = [1.5, 3.7, 9.0][t-1]
        p_sec = [15 * t, 20 * t, 30 * t][t-1]
        p_q = [18 * t, 24 * t, 36 * t][t-1]

        p1 = [
            make_mc(1, "Nhận biết", "Đơn vị đo cường độ dòng điện trong hệ thống đo lường quốc tế (SI) là:", ["Ampe (A)", "Vôn (V)", "Oát (W)", "Jun (J)"], 0, "Cường độ dòng điện đo bằng Ampe (A)."),
            make_mc(2, "Nhận biết", f"Dụng cụ nào sau đây dùng để đo hiệu điện thế giữa hai đầu thiết bị điện trong nhóm thực nghiệm {t}?", ["Vôn kế", "Ampe kế", "Lực kế", "Oát kế"], 0, "Vôn kế dùng để đo hiệu điện thế (V)."),
            make_mc(3, "Nhận biết", f"Để đo cường độ dòng điện qua một bóng đèn pin, ampe kế phải được mắc như thế nào?", ["Mắc nối tiếp với bóng đèn", "Mắc song song với bóng đèn", "Mắc vào hai cực nguồn điện mà không qua đèn", "Mắc tùy ý"], 0, "Ampe kế luôn mắc nối tiếp với thiết bị cần đo dòng điện."),
            make_mc(4, "Nhận biết", f"Một dòng điện có cường độ {p_ma} mA đổi sang đơn vị Ampe (A) có giá trị là:", [f"{p_ma / 1000} A", f"{p_ma / 100} A", f"{p_ma * 10} A", f"{p_ma * 1000} A"], 0, f"1 A = 1000 mA nên {p_ma} mA = {p_ma / 1000} A."),
            make_mc(5, "Nhận biết", f"Hiệu điện thế {p_kv} kV đổi sang đơn vị Vôn (V) có giá trị bằng:", [f"{round(p_kv * 1000)} V", f"{round(p_kv * 100)} V", f"{round(p_kv * 10)} V", f"{round(p_kv * 10000)} V"], 0, f"1 kV = 1000 V nên {p_kv} kV = {round(p_kv * 1000)} V."),
            make_mc(6, "Nhận biết", f"Số vôn {p_bat} V ghi trên vỏ một viên pin tiểu cho biết điều gì?", ["Hiệu điện thế giữa hai cực của pin khi mạch hở", "Cường độ dòng điện lớn nhất của pin", "Công suất tiêu thụ của pin", "Thời gian sử dụng của pin"], 0, "Số vôn ghi trên nguồn điện là hiệu điện thế giữa hai cực khi chưa mắc tải."),
            make_mc(7, "Thông hiểu", f"Khi sử dụng vôn kế để đo hiệu điện thế hai đầu bóng đèn, ta phải mắc vôn kế:", ["Song song với bóng đèn, chốt (+) về phía cực dương của nguồn", "Nối tiếp với bóng đèn, chốt (+) về phía cực âm nguồn", "Mắc trực tiếp vào hai đầu khóa K đóng", "Mắc tùy ý không phân biệt cực"], 0, "Vôn kế mắc song song với đoạn mạch cần đo, đúng cực tính."),
            make_mc(8, "Thông hiểu", f"Cường độ dòng điện chạy qua một bóng đèn càng lớn thì bóng đèn đó:", ["Sáng càng mạnh", "Sáng càng yếu", "Tỏa nhiệt càng ít", "Không thay đổi độ sáng"], 0, "Dòng điện càng lớn thì đèn sáng càng mạnh và tỏa nhiều nhiệt hơn."),
            make_mc(9, "Thông hiểu", f"Một ampe kế có thang đo từ 0 đến {2 + t} A được chia thành {20 + t*10} vạch đều nhau. Độ chia nhỏ nhất (ĐCNN) của ampe kế này là:", [f"{round((2 + t) / (20 + t*10), 3)} A", f"{2 + t} A", "0,1 A", "0,5 A"], 0, f"ĐCNN = GHĐ / số khoảng = {(2+t)} / {(20+t*10)} = {round((2+t)/(20+t*10), 3)} A."),
            make_mc(10, "Thông hiểu", f"Nếu vô tình mắc trực tiếp ampe kế vào hai cực của một acquy {12*t} V mà không có điện trở bảo vệ thì:", ["Ampe kế có thể bị cháy hỏng do đoản mạch", "Kim ampe kế chỉ số 0", "Acquy bị sạc đầy ngay lập tức", "Không có hiện tượng gì"], 0, "Ampe kế có điện trở rất bé, mắc thẳng vào nguồn gây ngắn mạch làm cháy ampe kế."),
            make_mc(11, "Thông hiểu", f"Hiệu điện thế giữa hai đầu một đoạn mạch bằng 0 V thì cường độ dòng điện qua đoạn mạch đó:", ["Chắc chắn bằng 0 A", "Đạt giá trị cực đại", "Bằng 1 A", "Không xác định được"], 0, "Không có hiệu điện thế thì không có dòng điện chạy qua tải tiêu thụ."),
            make_mc(12, "Thông hiểu", f"Để đo hiệu điện thế định mức của acquy xe máy khoảng 12 V, nên chọn vôn kế có giới hạn đo nào sau đây là phù hợp nhất?", ["GHĐ 15 V hoặc 20 V", "GHĐ 5 V", "GHĐ 1000 V", "GHĐ 1,5 V"], 0, "Chọn GHĐ lớn hơn giá trị cần đo một lượng vừa phải để đọc chính xác.")
        ]

        p2 = [
            make_tf(1, "Thông hiểu", f"Về quy tắc an toàn và kĩ năng sử dụng ampe kế, vôn kế bài {t}:", [
                ("a", "Trước khi đo cần hiệu chỉnh kim chỉ thị về đúng vạch số 0 (chỉnh zero).", True),
                ("b", "Nên chọn thang đo có GHĐ nhỏ hơn giá trị dự đoán để kim lệch tối đa.", False),
                ("c", "Ampe kế tuyệt đối không được mắc trực tiếp vào hai cực của nguồn điện mà không có tải.", True),
                ("d", "Vôn kế có thể mắc trực tiếp vào hai cực của pin mạch hở để đo suất điện động của pin.", True)
            ], "Ampe kế có điện trở rất nhỏ (gây đoản mạch nếu mắc vào nguồn), vôn kế có điện trở rất lớn nên đo được hiệu điện thế nguồn."),
            make_tf(2, "Thông hiểu", f"Về bản chất cường độ dòng điện và hiệu điện thế trong mạch đợt {t}:", [
                ("a", "Hiệu điện thế sinh ra và duy trì dòng điện chạy trong mạch kín.", True),
                ("b", "Dòng điện 1 A tương ứng với lượng điện tích 1 Culông chuyển qua tiết diện dây trong 1 giây.", True),
                ("c", "Trong kim loại, các electron tự do dịch chuyển cùng chiều với chiều quy ước của dòng điện.", False),
                ("d", "Khi mạch điện bị hở tại công tắc thì dòng điện trong toàn mạch bằng 0 A.", True)
            ], "Chiều dòng điện quy ước từ cực dương sang cực âm, ngược chiều chuyển động của electron tự do."),
            make_tf(3, "Thông hiểu", f"Về sự phụ thuộc của cường độ dòng điện vào hiệu điện thế:", [
                ("a", "Với một bóng đèn nhất định, khi tăng hiệu điện thế đặt vào hai đầu đèn thì cường độ dòng điện qua đèn tăng.", True),
                ("b", "Cường độ dòng điện qua một vật dẫn kim loại tỉ lệ nghịch với hiệu điện thế hai đầu vật dẫn.", False),
                ("c", "Đồ thị biểu diễn sự phụ thuộc của I vào U đối với dây dẫn kim loại là một đường thẳng đi qua gốc tọa độ O.", True),
                ("d", "Hiệu điện thế giữa hai điểm A và B đặc trưng cho khả năng sinh công của điện trường khi dịch chuyển điện tích giữa hai điểm đó.", True)
            ], "I tỉ lệ thuận với U theo định luật Ohm."),
            make_tf(4, "Thông hiểu", f"Về sai số đo lường và đọc chỉ số trên dụng cụ đo điện nhóm {t}:", [
                ("a", "Khi đọc số chỉ, mắt người quan sát phải đặt nhìn vuông góc với mặt thang đo để tránh thị sai.", True),
                ("b", "Nếu kim chỉ nằm ở giữa hai vạch chia nhỏ nhất, người đo chỉ được phép làm tròn xuống vạch dưới.", False),
                ("c", "Sai số dụng cụ thường được lấy bằng một nửa hoặc một độ chia nhỏ nhất của thang đo đang dùng.", True),
                ("d", "Đo lặp lại 3 đến 5 lần và lấy trung bình cộng giúp giảm thiểu sai số ngẫu nhiên của phép đo.", True)
            ], "Quy tắc đọc số đo và xử lý sai số thực nghiệm.")
        ]

        p3 = [
            make_sa(1, "Thông hiểu", f"Dòng điện không đổi có cường độ I = {p_ma / 1000:.2f} A chạy qua dây dẫn trong thời gian {p_sec} giây. Lượng điện tích chuyển qua tiết diện thẳng của dây là bao nhiêu Culông (C)?", f"{round((p_ma / 1000) * p_sec, 2)}", f"q = I * t = {p_ma/1000:.2f} * {p_sec} = {round((p_ma/1000)*p_sec, 2)} C."),
            make_sa(2, "Thông hiểu", f"Trong thời gian {p_sec} giây, có lượng điện tích q = {p_q} C dịch chuyển qua một dây dẫn. Cường độ dòng điện chạy qua dây dẫn đó là bao nhiêu Ampe (A)?", f"{round(p_q / p_sec, 2)}", f"I = q / t = {p_q} / {p_sec} = {round(p_q / p_sec, 2)} A."),
            make_sa(3, "Thông hiểu", f"Một vôn kế có giới hạn đo {10 + t*5} V và mặt thang đo chia thành 50 vạch đều nhau. Kim vôn kế chỉ đúng vạch thứ {20 + t*5}. Hiệu điện thế đo được là bao nhiêu Vôn (V)?", f"{round((10 + t*5) / 50 * (20 + t*5), 2)}", f"U = (GHĐ / 50) * vạch = {(10+t*5)}/50 * {(20+t*5)} = {round((10+t*5)/50*(20+t*5), 2)} V."),
            make_sa(4, "Thông hiểu", f"Một ampe kế có thang đo cực đại 3 A gồm 30 vạch nhỏ. Khi đo dòng điện qua quạt mini, kim lệch 18 vạch. Cường độ dòng điện đo được là bao nhiêu miliampe (mA)?", f"{round(3 / 30 * 18 * 1000)}", f"I = (3/30) * 18 = 1,8 A = 1800 mA."),
            make_sa(5, "Vận dụng", f"Một bóng đèn sợi đốt có điện trở R = {15 + t*5} Ω được mắc vào nguồn pin có hiệu điện thế U = {p_u} V. Cường độ dòng điện chạy qua bóng đèn là bao nhiêu Ampe (A)? (Làm tròn đến 2 chữ số thập phân).", f"{round(p_u / (15 + t*5), 2)}", f"I = U / R = {p_u} / {15+t*5} = {round(p_u / (15+t*5), 2)} A."),
            make_sa(6, "Vận dụng", f"Cường độ dòng điện qua một dây tóc bóng đèn là I = {0.32 + t*0.16:.2f} A. Biết điện tích của một electron là e = 1,6 . 10^-19 C. Số electron tự do đi qua tiết diện dây tóc trong 1 giây là bao nhiêu hạt? (Viết dưới dạng hệ số của 10^18 hạt, ví dụ: 2.0).", f"{round((0.32 + t*0.16) / 1.6 * 10, 2)}", f"N = (I * 1) / e = ({0.32+t*0.16:.2f}) / (1,6e-19) = {round((0.32+t*0.16)/1.6*10, 2)} . 10^18 hạt.")
        ]

        vdc_l = 40 + t*20
        vdc_s_mm = 1.0 + t*0.2
        vdc_v = round((2.0 + t*0.5) / (8.5e28 * 1.6e-19 * (3.14159 * ((vdc_s_mm*1e-3)/2)**2)) * 1000, 3)
        p4 = [
            make_vdc(1, f"Một dây dẫn bằng đồng có chiều dài L = {vdc_l} m, đường kính tiết diện d = {vdc_s_mm:.1f} mm dẫn dòng điện không đổi I = {2.0 + t*0.5:.1f} A. Biết mật độ electron tự do trong đồng n = 8,5 . 10^28 hạt/m3 và điện tích e = 1,6 . 10^-19 C. Tốc độ chuyển dịch có hướng trung bình của các electron trong dây dẫn xấp xỉ bằng:", [
                f"{vdc_v} mm/s", f"{round(vdc_v * 10, 2)} mm/s", f"{round(vdc_v * 0.1, 2)} mm/s", f"1,5 mm/s"
            ], 0, f"v = I / (n * e * S) = {vdc_v} mm/s."),
            make_vdc(2, f"Để mở rộng thang đo của một miliampe kế có giới hạn đo I0 = {50 + t*10} mA và điện trở nội r0 = {18 + t*2} Ω thành ampe kế có thang đo I_max = {2 + t} A, người ta mắc song song một điện trở sun Rs. Giá trị của điện trở sun Rs cần dùng là:", [
                f"{round(((50 + t*10)/1000 * (18 + t*2)) / ((2 + t) - (50 + t*10)/1000), 4)} Ω",
                f"{round(((50 + t*10)/1000 * (18 + t*2)), 3)} Ω",
                f"1,5 Ω",
                f"0,5 Ω"
            ], 0, f"Rs = (I0 * r0) / (I_max - I0) = {round(((50 + t*10)/1000 * (18 + t*2)) / ((2 + t) - (50 + t*10)/1000), 4)} Ω."),
            make_vdc(3, f"Để chế tạo một vôn kế đo được hiệu điện thế tối đa U_max = {20 + t*10} V từ một khung đo miliampe kế có thang đo cực đại I0 = {50 + t*10} mA và điện trở r0 = {18 + t*2} Ω, người ta mắc nối tiếp một điện trở phụ Rp. Giá trị của Rp là:", [
                f"{round(((20 + t*10) - (50 + t*10)/1000 * (18 + t*2)) / ((50 + t*10)/1000), 1)} Ω",
                f"{round((20 + t*10) / ((50 + t*10)/1000), 1)} Ω",
                f"500 Ω",
                f"100 Ω"
            ], 0, f"Rp = (U_max - I0*r0) / I0 = {round(((20 + t*10) - (50 + t*10)/1000 * (18 + t*2)) / ((50 + t*10)/1000), 1)} Ω."),
            make_vdc(4, f"Một cảm biến quang trở có điện trở thay đổi từ {100 + t*20} Ω (khi có ánh sáng) đến {1000 + t*200} Ω (khi tối). Cảm biến được mắc nối tiếp với một điện trở chuẩn R0 = {200 + t*50} Ω vào nguồn U = 12 V. Độ biến thiên hiệu điện thế trên R0 giữa hai trạng thái sáng và tối xấp xỉ bằng:", [
                f"{round(abs(12 * (200 + t*50) / (100 + t*20 + 200 + t*50) - 12 * (200 + t*50) / (1000 + t*200 + 200 + t*50)), 2)} V",
                f"8,5 V",
                f"4,2 V",
                f"1,5 V"
            ], 0, f"ΔU = |U_sang - U_toi| = {round(abs(12 * (200 + t*50) / (100 + t*20 + 200 + t*50) - 12 * (200 + t*50) / (1000 + t*200 + 200 + t*50)), 2)} V.")
        ]

        exams[f"{l24_id}_test{t}"] = meta(l24_id, l24_name, t, p1, p2, p3, p4)

    # =========================================================================
    # BÀI 25: THỰC HÀNH ĐO CƯỜNG ĐỘ DÒNG ĐIỆN VÀ HIỆU ĐIỆN THẾ (3 ĐỀ)
    # =========================================================================
    l25_id = "phys8_c5_b25"
    l25_name = "Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế"

    for t in range(1, 4):
        p_u = [6.0, 9.0, 12.0][t-1]
        p_r1 = [12 + t*2, 15 + t*3, 20 + t*4][t-1]
        p_r2 = [18 + t*2, 25 + t*3, 30 + t*4][t-1]
        p_i_main = [0.4 + t*0.1, 0.6 + t*0.1, 0.8 + t*0.2][t-1]

        p1 = [
            make_mc(1, "Nhận biết", "Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc nối tiếp, hệ thức nào sau đây về cường độ dòng điện là ĐÚNG?", ["I = I1 = I2", "I = I1 + I2", "I = I1 - I2", "I = I1 * I2"], 0, "Trong mạch nối tiếp, cường độ dòng điện như nhau tại mọi vị trí: I = I1 = I2."),
            make_mc(2, "Nhận biết", f"Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc nối tiếp vào nguồn U = {p_u} V, hiệu điện thế toàn mạch U thỏa mãn:", ["U = U1 + U2", "U = U1 = U2", "U = U1 - U2", "U1 + U2 = 2 * U"], 0, "Hiệu điện thế mạch nối tiếp bằng tổng hiệu điện thế thành phần: U = U1 + U2."),
            make_mc(3, "Nhận biết", f"Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc song song vào nguồn {p_u} V, hiệu điện thế hai đầu mỗi bóng đèn thỏa mãn:", ["U = U1 = U2", "U = U1 + U2", "U = U1 - U2", "U = 2 * (U1 + U2)"], 0, "Trong mạch song song, hiệu điện thế hai đầu mỗi nhánh bằng hiệu điện thế nguồn: U = U1 = U2."),
            make_mc(4, "Nhận biết", f"Trong đoạn mạch song song gồm hai nhánh Đ1 và Đ2, cường độ dòng điện mạch chính I và dòng nhánh I1, I2 thỏa mãn:", ["I = I1 + I2", "I = I1 = I2", "I = I1 - I2", "I = (I1 + I2) / 2"], 0, "Dòng điện mạch chính bằng tổng cường độ dòng điện qua các nhánh song song."),
            make_mc(5, "Nhận biết", "Khi một bóng đèn trong mạch hai bóng đèn mắc nối tiếp bị đứt dây tóc thì đèn còn lại sẽ:", ["Tắt hẳn vì mạch bị hở", "Sáng rực rỡ hơn", "Vẫn sáng bình thường không đổi", "Nhấp nháy liên tục"], 0, "Mạch nối tiếp bị đứt một phần tử thì ngắt toàn bộ dòng điện."),
            make_mc(6, "Nhận biết", "Trong mạng điện sinh hoạt gia đình, các thiết bị điện (quạt, đèn, tivi) được mắc với nhau theo kiểu:", ["Mắc song song", "Mắc nối tiếp", "Mắc hỗn hợp ngẫu nhiên", "Mắc qua cầu dao đơn"], 0, "Mắc song song để nhận cùng điện áp định mức 220 V và vận hành độc lập."),
            make_mc(7, "Thông hiểu", f"Hai bóng đèn giống hệt nhau mắc nối tiếp vào nguồn U = {p_u} V. Hiệu điện thế giữa hai đầu mỗi bóng đèn là:", [f"{p_u / 2:.1f} V", f"{p_u:.1f} V", f"{p_u * 2:.1f} V", "0 V"], 0, f"Hai đèn giống nhau chia đôi điện áp: U1 = U2 = U / 2 = {p_u / 2:.1f} V."),
            make_mc(8, "Thông hiểu", f"Trong mạch song song gồm hai đèn, ampe kế mạch chính chỉ {p_i_main} A, nhánh 1 chỉ {round(p_i_main * 0.4, 2)} A. Dòng điện qua nhánh 2 là:", [f"{round(p_i_main * 0.6, 2)} A", f"{p_i_main} A", f"{round(p_i_main * 0.4, 2)} A", f"{round(p_i_main * 1.4, 2)} A"], 0, f"I2 = I - I1 = {p_i_main} - {round(p_i_main * 0.4, 2)} = {round(p_i_main * 0.6, 2)} A."),
            make_mc(9, "Thông hiểu", "Trong mạch gồm hai đèn mắc song song, nếu một bóng đèn bị hỏng đứt tóc thì bóng đèn kia sẽ:", ["Vẫn sáng bình thường vì hiệu điện thế hai đầu nhánh không đổi", "Tắt ngay lập tức", "Cháy theo", "Sáng gấp đôi"], 0, "Các nhánh song song hoạt động độc lập."),
            make_mc(10, "Thông hiểu", f"Khi mắc nối tiếp thêm một điện trở vào đoạn mạch đang có bóng đèn sáng, độ sáng của đèn sẽ:", ["Giảm đi do tổng điện trở mạch tăng làm dòng điện giảm", "Tăng lên rực rỡ", "Không thay đổi", "Lúc sáng lúc tắt"], 0, "Mắc nối tiếp thêm điện trở làm tăng R_td => giảm I => đèn sáng yếu đi."),
            make_mc(11, "Thông hiểu", "Hiện tượng đoản mạch (chập mạch) xảy ra khi:", ["Hai cực nguồn điện bị nối trực tiếp bằng dây dẫn có điện trở rất nhỏ", "Công tắc mạch điện đang mở", "Dây tóc bóng đèn bị đứt", "Vôn kế mắc song song với tải"], 0, "Đoản mạch xảy ra khi dòng điện chạy tắt qua dây dẫn điện trở nhỏ."),
            make_mc(12, "Thông hiểu", "Khi vôn kế mắc vào mạch mà kim quay ngược về phía dưới vạch số 0, nguyên nhân do:", ["Mắc ngược cực (+) và (-) của vôn kế", "Hiệu điện thế quá lớn", "Vôn kế bị đứt cầu chì", "Mạch điện bị hở"], 0, "Ngược cực làm lực từ đẩy kim theo hướng ngược lại.")
        ]

        p2 = [
            make_tf(1, "Thông hiểu", f"Về quy trình lắp ráp và đo đạc trong bài thực hành số {t}:", [
                ("a", "Trong quá trình lắp mạch, công tắc điện luôn phải được để ở vị trí mở (ngắt).", True),
                ("b", "Sau khi lắp xong mạch, phải kiểm tra kĩ sơ đồ trước khi đóng công tắc.", True),
                ("c", "Ampe kế được mắc song song với bóng đèn để kiểm tra dòng điện.", False),
                ("d", "Vôn kế mắc song song với hai đầu đoạn mạch cần xác định hiệu điện thế.", True)
            ], "Ampe kế tuyệt đối không mắc song song vì gây đoản mạch."),
            make_tf(2, "Thông hiểu", f"Về tính chất của đoạn mạch mắc nối tiếp gồm hai điện trở R1 và R2:", [
                ("a", "Điện trở tương đương của đoạn mạch nối tiếp thỏa mãn Rtd = R1 + R2.", True),
                ("b", "Cường độ dòng điện qua điện trở lớn hơn sẽ nhỏ hơn cường độ qua điện trở nhỏ hơn.", False),
                ("c", "Hiệu điện thế giữa hai đầu mỗi điện trở tỉ lệ thuận với giá trị của điện trở đó.", True),
                ("d", "Nếu tháo một điện trở ra khỏi mạch nối tiếp thì dòng điện qua điện trở còn lại vẫn chạy bình thường.", False)
            ], "Mạch nối tiếp có I bằng nhau tại mọi điểm; tháo một phần tử làm hở toàn mạch."),
            make_tf(3, "Thông hiểu", f"Về tính chất của đoạn mạch mắc song song gồm hai điện trở R1 và R2:", [
                ("a", "Hiệu điện thế hai đầu mỗi điện trở bằng nhau và bằng hiệu điện thế toàn mạch.", True),
                ("b", "Cường độ dòng điện mạch chính bằng tổng cường độ dòng điện qua các nhánh rẽ.", True),
                ("c", "Điện trở tương đương của đoạn mạch song song luôn lớn hơn điện trở của mỗi nhánh thành phần.", False),
                ("d", "Công thức tính điện trở tương đương hai nhánh song song là Rtd = (R1 * R2) / (R1 + R2).", True)
            ], "Mạch song song có Rtd luôn nhỏ hơn từng điện trở thành phần."),
            make_tf(4, "Thông hiểu", f"Về hiện tượng sự cố mạch điện thực hành nhóm {t}:", [
                ("a", "Khi xảy ra hiện tượng chập điện (đoản mạch), dòng điện trong mạch chính tăng vọt.", True),
                ("b", "Cầu chì tự ngắt mạch khi có dòng điện tăng cao là nhờ tác dụng từ của dòng điện.", False),
                ("c", "Aptomat (cầu dao tự động) bảo vệ an toàn cho hệ thống điện chống quá tải và chập mạch.", True),
                ("d", "Khi một đèn trong chuỗi đèn nháy trang trí nối tiếp bị đứt, toàn bộ dây đèn nháy sẽ tắt hết.", True)
            ], "Cầu chì đứt do tác dụng nhiệt (dây chì nóng chảy).")
        ]

        r_td_nt = p_r1 + p_r2
        r_td_ss = round((p_r1 * p_r2) / (p_r1 + p_r2), 2)
        p3 = [
            make_sa(1, "Thông hiểu", f"Hai điện trở R1 = {p_r1} Ω và R2 = {p_r2} Ω mắc nối tiếp với nhau. Điện trở tương đương của đoạn mạch nối tiếp này là bao nhiêu Ôm (Ω)?", f"{r_td_nt}", f"Rtd = R1 + R2 = {p_r1} + {p_r2} = {r_td_nt} Ω."),
            make_sa(2, "Thông hiểu", f"Hai điện trở R1 = {p_r1} Ω và R2 = {p_r2} Ω mắc song song với nhau. Điện trở tương đương của đoạn mạch song song này là bao nhiêu Ôm (Ω)? (Làm tròn đến 2 chữ số thập phân).", f"{r_td_ss}", f"Rtd = (R1 * R2) / (R1 + R2) = ({p_r1} * {p_r2}) / ({p_r1} + {p_r2}) = {r_td_ss} Ω."),
            make_sa(3, "Thông hiểu", f"Đoạn mạch nối tiếp hai điện trở trên được mắc vào nguồn U = {p_u} V. Cường độ dòng điện trong mạch bằng bao nhiêu Ampe (A)? (Làm tròn đến 3 chữ số thập phân).", f"{round(p_u / r_td_nt, 3)}", f"I = U / Rtd = {p_u} / {r_td_nt} = {round(p_u / r_td_nt, 3)} A."),
            make_sa(4, "Thông hiểu", f"Khi hai điện trở R1 = {p_r1} Ω và R2 = {p_r2} Ω mắc song song vào nguồn U = {p_u} V, cường độ dòng điện qua nhánh R1 là bao nhiêu Ampe (A)? (Làm tròn đến 3 chữ số thập phân).", f"{round(p_u / p_r1, 3)}", f"I1 = U / R1 = {p_u} / {p_r1} = {round(p_u / p_r1, 3)} A."),
            make_sa(5, "Thông hiểu", f"Trong mạch song song ở câu trên, cường độ dòng điện ở mạch chính bằng bao nhiêu Ampe (A)? (Làm tròn đến 3 chữ số thập phân).", f"{round(p_u / r_td_ss, 3)}", f"I = U / Rtd = {p_u} / {r_td_ss} = {round(p_u / r_td_ss, 3)} A."),
            make_sa(6, "Vận dụng", f"Ba bóng đèn giống nhau mỗi chiếc có điện trở {30 * t} Ω mắc song song vào nguồn 12 V. Điện trở tương đương của bộ ba bóng đèn này là bao nhiêu Ôm (Ω)?", f"{round(30 * t / 3, 1)}", f"Rtd = R / 3 = {30*t} / 3 = {round(30*t/3, 1)} Ω.")
        ]

        vdc_lamp_u = round(p_u * 0.6, 1)
        vdc_lamp_i = round(0.3 + t*0.1, 1)
        vdc_r_lamp = round(vdc_lamp_u / vdc_lamp_i, 2)
        vdc_rb = round((p_u - vdc_lamp_u) / vdc_lamp_i, 2)
        p4 = [
            make_vdc(1, f"Một bóng đèn ghi ({vdc_lamp_u} V - {vdc_lamp_i} A) được mắc nối tiếp với một biến trở con chạy vào nguồn điện U = {p_u} V không đổi. Để bóng đèn sáng đúng công suất định mức bình thường, giá trị điện trở của biến trở cần điều chỉnh tham gia vào mạch là:", [
                f"{vdc_rb} Ω", f"{round(vdc_rb * 1.5, 2)} Ω", f"{round(vdc_rb * 0.5, 2)} Ω", f"10,0 Ω"
            ], 0, f"R_b = (U - U_đ) / I_đ = ({p_u} - {vdc_lamp_u}) / {vdc_lamp_i} = {vdc_rb} Ω."),
            make_vdc(2, f"Một mạch điện trang trí gồm {12 + t*4} bóng đèn LED nhỏ giống nhau. Mỗi bóng có hiệu điện thế định mức 2,5 V và dòng điện 0,02 A. Để các bóng đèn đều sáng bình thường khi mắc thành các nhánh song song giống nhau vào nguồn 10 V, cần mắc thành bao nhiêu nhánh song song và mỗi nhánh gồm mấy đèn nối tiếp?", [
                f"Mắc {round((12 + t*4)/4)} nhánh song song, mỗi nhánh gồm 4 bóng đèn nối tiếp",
                f"Mắc {12 + t*4} nhánh song song",
                f"Mắc nối tiếp toàn bộ {12 + t*4} đèn",
                f"Mắc 2 nhánh song song, mỗi nhánh 10 đèn"
            ], 0, f"Số đèn mỗi nhánh n = U / U0 = 10 / 2.5 = 4 bóng. Số nhánh = ({12 + t*4}) / 4 = {round((12 + t*4)/4)} nhánh."),
            make_vdc(3, f"Một mạch cầu Wheatstone cân bằng gồm 4 điện trở: R1 = {10 + t*5} Ω, R2 = {20 + t*10} Ω, R3 = {15 + t*5} Ω và Rx. Khi cầu cân bằng, kim điện kế giữa hai nút chéo chỉ số 0. Giá trị của điện trở Rx là:", [
                f"{round((20 + t*10) * (15 + t*5) / (10 + t*5), 1)} Ω",
                f"10 Ω",
                f"50 Ω",
                f"25 Ω"
            ], 0, f"R1 / R2 = R3 / Rx => Rx = (R2 * R3) / R1 = {round((20 + t*10) * (15 + t*5) / (10 + t*5), 1)} Ω."),
            make_vdc(4, f"Một đường dây dẫn điện đôi dài {3 + t} km bằng đồng có điện trở suất ρ = 1,7 . 10^-8 Ω.m, tiết diện mỗi sợi dây là S = {17 + t*3} mm2. Dòng điện truyền tải trên dây có cường độ I = {10 + t*2} A. Công suất hao phí tỏa nhiệt trên toàn bộ đường dây đôi là:", [
                f"{round((10 + t*2)**2 * (1.7e-8 * 2 * (3 + t) * 1000 / ((17 + t*3)*1e-6)), 1)} W",
                f"1200 W",
                f"500 W",
                f"3500 W"
            ], 0, f"R = ρ * (2L / S). P_hp = I^2 * R = {round((10 + t*2)**2 * (1.7e-8 * 2 * (3 + t) * 1000 / ((17 + t*3)*1e-6)), 1)} W.")
        ]

        exams[f"{l25_id}_test{t}"] = meta(l25_id, l25_name, t, p1, p2, p3, p4)

    # =========================================================================
    # ĐỀ TỔNG HỢP: ÔN TẬP CUỐI CHƯƠNG V (5 ĐỀ)
    # =========================================================================
    lrev_id = "phys8_c5_rev"
    lrev_name = "[Đề tổng hợp] Ôn tập cuối Chương V"

    for t in range(1, 6):
        p_rub = ["thước nhựa cọ xát với vải dạ", "thanh thủy tinh cọ xát với lụa", "thanh cao su cọ xát với lông thú", "mảnh nilông cọ xát với len", "ống hút nhựa cọ xát giấy lụa"][t-1]
        p_u = [12, 24, 36, 48, 110][t-1]
        p_fuse = [5 + t, 10 + t, 15 + t, 16 + t, 20 + t][t-1]
        p_p = [500 + t*100, 800 + t*150, 1000 + t*200, 1200 + t*200, 1500 + t*200][t-1]

        p1 = [
            make_mc(1, "Nhận biết", f"Khi cọ xát {p_rub}, vật này có khả năng hút các mẩu giấy vụn nhỏ. Hiện tượng này chứng minh:", ["Vật bị nhiễm điện do cọ xát", "Vật trở thành nam châm vĩnh cửu", "Khối lượng vật tăng lên", "Trọng lực bị mất đi"], 0, "Cọ xát làm vật nhiễm điện, có khả năng hút các vật nhẹ."),
            make_mc(2, "Nhận biết", f"Hai quả cầu nhỏ mang điện tích cùng dấu khi đặt gần nhau sẽ có tương tác gì trong đề {t}?", ["Đẩy nhau", "Hút nhau", "Không tương tác", "Vừa hút vừa đẩy"], 0, "Các điện tích cùng dấu thì đẩy nhau, khác dấu thì hút nhau."),
            make_mc(3, "Nhận biết", "Dòng điện trong kim loại là dòng dịch chuyển có hướng của:", ["Các electron tự do", "Các ion dương", "Các nguyên tử kim loại", "Các neutron"], 0, "Dòng điện trong kim loại là dòng electron tự do dịch chuyển có hướng."),
            make_mc(4, "Nhận biết", f"Vật liệu nào sau đây dẫn điện tốt nhất trong các vật liệu nhóm ôn tập {t}?", ["Dây đồng", "Thanh nhựa PVC", "Miếng sứ", "Tấm cao su"], 0, "Đồng là kim loại dẫn điện rất tốt nhờ mật độ electron tự do cao."),
            make_mc(5, "Nhận biết", "Tác dụng từ của dòng điện được thể hiện rõ ràng nhất khi dòng điện:", ["Làm quay kim nam châm đặt gần nó", "Làm nóng dây mayso", "Làm phát sáng khí neon", "Gây co giật cơ"], 0, "Tác dụng từ sinh ra từ trường tác dụng lực lên kim nam châm."),
            make_mc(6, "Nhận biết", "Để đo cường độ dòng điện và hiệu điện thế của bóng đèn, ta mắc:", ["Ampe kế nối tiếp, vôn kế song song với đèn", "Ampe kế song song, vôn kế nối tiếp", "Cả hai cùng mắc song song", "Cả hai cùng mắc nối tiếp"], 0, "Ampe kế mắc nối tiếp để đo I, vôn kế mắc song song để đo U."),
            make_mc(7, "Thông hiểu", f"Trong đoạn mạch gồm hai điện trở R1 và R2 mắc nối tiếp vào hiệu điện thế U = {p_u} V, hệ thức nào sau đây là ĐÚNG?", ["U = U1 + U2 và I = I1 = I2", "U = U1 = U2 và I = I1 + I2", "U = U1 - U2", "I1 / I2 = R2 / R1"], 0, "Mạch nối tiếp có I bằng nhau và U bằng tổng các điện áp."),
            make_mc(8, "Thông hiểu", f"Trong đoạn mạch gồm hai điện trở R1 và R2 mắc song song vào nguồn {p_u} V, hệ thức nào sau đây là ĐÚNG?", ["U = U1 = U2 và I = I1 + I2", "U = U1 + U2 và I = I1 = I2", "U = U1 * U2", "I1 / I2 = R1 / R2"], 0, "Mạch song song có U bằng nhau và I bằng tổng các dòng nhánh."),
            make_mc(9, "Thông hiểu", f"Cầu chì hoặc aptomat loại {p_fuse} A được lắp trên dây pha nhằm mục đích:", ["Tự động ngắt mạch bảo vệ an toàn khi quá tải hoặc đoản mạch", "Tăng điện áp cấp cho thiết bị", "Giảm điện năng tiêu thụ", "Thay thế cho công tắc bật tắt"], 0, "Thiết bị bảo vệ tự động ngắt dòng quá tải tránh hỏa hoạn."),
            make_mc(10, "Thông hiểu", "Vỏ kim loại của các thiết bị điện công suất lớn như bình nóng lạnh, máy giặt cần được:", ["Nối đất an toàn để chống rò điện", "Sơn màu đỏ để cảnh báo", "Nối vào dây pha", "Cách li hoàn toàn trong hộp xốp"], 0, "Nối đất (tiếp địa) dẫn dòng điện rò an toàn xuống đất triệt tiêu nguy cơ điện giật."),
            make_mc(11, "Thông hiểu", f"Một bóng đèn ghi 220V - {60 + t*15}W hoạt động bình thường khi mắc vào mạng điện nào sau đây?", ["Mạng điện có hiệu điện thế 220 V", "Mạng điện 110 V", "Nguồn pin 12 V", "Mạng điện 380 V"], 0, "Đèn hoạt động bình thường khi điện áp cấp bằng đúng điện áp định mức 220 V."),
            make_mc(12, "Thông hiểu", f"Hành động nào sau đây là KHÔNG bảo đảm an toàn điện sinh hoạt gia đình đợt {t}?", ["Dùng tay ướt cắm phích điện vào ổ cắm", "Ngắt cầu dao trước khi sửa chữa điện", "Sử dụng bút thử điện có vỏ cách điện", "Không thả diều gần đường dây cao thế"], 0, "Tay ướt làm giảm điện trở tiếp xúc của da, nguy cơ giật điện rất cao.")
        ]

        p2 = [
            make_tf(1, "Thông hiểu", f"Về bản chất nhiễm điện và cấu tạo nguyên tử ôn tập {t}:", [
                ("a", "Nguyên tử gồm hạt nhân mang điện tích dương và các electron mang điện tích âm.", True),
                ("b", "Một vật nhiễm điện âm khi vật đó nhận thêm các electron từ vật khác.", True),
                ("c", "Hai vật cùng nhiễm điện dương khi đặt gần nhau sẽ hút nhau một lực rất lớn.", False),
                ("d", "Hiện tượng sấm sét trong tự nhiên là sự phóng điện giữa các đám mây tích điện trái dấu hoặc mây và mặt đất.", True)
            ], "Điện tích cùng dấu đẩy nhau; sét là sự phóng điện khí quyển."),
            make_tf(2, "Thông hiểu", f"Về các tác dụng đa dạng của dòng điện và ứng dụng trong đời sống:", [
                ("a", "Tác dụng hóa học của dòng điện được ứng dụng rộng rãi trong kĩ thuật mạ điện kim loại.", True),
                ("b", "Động cơ điện và chuông điện hoạt động dựa trên tác dụng từ của dòng điện.", True),
                ("c", "Dòng điện chỉ có tác dụng nhiệt đối với các thiết bị đun nấu, không có tác dụng nhiệt trên dây dẫn truyền tải.", False),
                ("d", "Tác dụng sinh lí của dòng điện được ứng dụng có ích trong y học để phục hồi nhịp tim bằng máy sốc điện.", True)
            ], "Mọi vật dẫn có điện trở đều tỏa nhiệt khi có dòng điện."),
            make_tf(3, "Thông hiểu", f"Về quy tắc mắc mạch và phân bố thông số dòng điện, hiệu điện thế:", [
                ("a", "Điện trở tương đương của đoạn mạch gồm hai điện trở giống nhau R mắc song song là R/2.", True),
                ("b", "Trong đoạn mạch nối tiếp, cường độ dòng điện chạy qua điện trở lớn hơn sẽ lớn hơn.", False),
                ("c", "Mắc song song giúp các thiết bị điện trong nhà hoạt động độc lập với nhau.", True),
                ("d", "Tổng điện trở tương đương của đoạn mạch nối tiếp luôn lớn hơn từng điện trở thành phần.", True)
            ], "Mạch nối tiếp có dòng điện như nhau tại mọi điểm: I1 = I2 = I."),
            make_tf(4, "Thông hiểu", f"Về các biện pháp sử dụng điện an toàn và tiết kiệm trong gia đình đề {t}:", [
                ("a", "Cầu chì hoặc aptomat điều khiển bắt buộc phải được lắp trên dây pha (dây nóng).", True),
                ("b", "Khi cầu chì bị đứt, có thể dùng dây đồng dày thay thế để không bao giờ bị đứt lại.", False),
                ("c", "Aptomat chống giật (RCCB/ELCB) tự động ngắt điện khi có dòng rò xuống đất vượt ngưỡng an toàn.", True),
                ("d", "Khoảng cách an toàn phóng điện với lưới điện cao áp 220 kV tối thiểu là 4 mét.", True)
            ], "Thay dây đồng vào cầu chì làm mất chức năng bảo vệ ngắt nhiệt, dễ gây cháy nổ.")
        ]

        r_base = 10 + t*5
        p3 = [
            make_sa(1, "Thông hiểu", f"Hai điện trở R1 = {r_base} Ω và R2 = {r_base * 2} Ω mắc nối tiếp vào nguồn U = {p_u} V. Cường độ dòng điện chạy trong mạch là bao nhiêu Ampe (A)? (Làm tròn đến 2 chữ số thập phân).", f"{round(p_u / (r_base * 3), 2)}", f"I = {p_u} / ({r_base} + {r_base*2}) = {round(p_u / (r_base * 3), 2)} A."),
            make_sa(2, "Thông hiểu", f"Hai điện trở R1 = {r_base} Ω và R2 = {r_base * 2} Ω mắc song song vào nguồn 12 V. Cường độ dòng điện ở mạch chính là bao nhiêu Ampe (A)? (Làm tròn đến 2 chữ số thập phân).", f"{round(12 / r_base + 12 / (r_base * 2), 2)}", f"I = 12/{r_base} + 12/{r_base*2} = {round(12 / r_base + 12 / (r_base * 2), 2)} A."),
            make_sa(3, "Thông hiểu", f"Một bếp điện có công suất P = {p_p} W hoạt động ở mạng điện 220 V. Cường độ dòng điện định mức qua bếp điện là bao nhiêu Ampe (A)? (Làm tròn đến 2 chữ số thập phân).", f"{round(p_p / 220, 2)}", f"I = P / U = {p_p} / 220 = {round(p_p / 220, 2)} A."),
            make_sa(4, "Thông hiểu", f"Một bóng đèn {60 + t*10} W được thắp sáng {5 + t} giờ mỗi ngày trong suốt 30 ngày. Điện năng tiêu thụ của bóng đèn trong tháng là bao nhiêu kWh? (Làm tròn đến 2 chữ số thập phân).", f"{round((60 + t*10) * (5 + t) * 30 / 1000, 2)}", f"A = P * t = {(60+t*10)*(5+t)*30} Wh = {round((60 + t*10) * (5 + t) * 30 / 1000, 2)} kWh."),
            make_sa(5, "Thông hiểu", f"Một dòng điện I = {0.5 + t*0.1:.1f} A chạy qua dây dẫn trong thời gian {10 * t} phút ({10*t*60} s). Điện lượng chuyển qua dây dẫn là bao nhiêu Culông (C)?", f"{round((0.5 + t*0.1) * (10 * t * 60))}", f"q = I * t = {0.5+t*0.1:.1f} * {10*t*60} = {round((0.5 + t*0.1) * (10 * t * 60))} C."),
            make_sa(6, "Thông hiểu", f"Một vôn kế có thang đo cực đại {12 + t*6} V chia đều thành 60 vạch. Khi kim chỉ ở vạch thứ {30 + t*4}, giá trị hiệu điện thế đo được là bao nhiêu Vôn (V)?", f"{round((12 + t*6) / 60 * (30 + t*4), 2)}", f"U = {(12+t*6)}/60 * {(30+t*4)} = {round((12 + t*6) / 60 * (30 + t*4), 2)} V.")
        ]

        vdc_e_day = round(((p_p * 1.5) + (2000 * 1.0) + (4 * 15 * 5)) / 1000, 2)
        vdc_e_month = round(vdc_e_day * 30, 1)
        p4 = [
            make_vdc(1, f"Một gia đình sử dụng mạng điện 220 V gồm: 1 bếp điện {p_p} W dùng 1,5 h/ngày, 1 bình nóng lạnh 2000 W dùng 1,0 h/ngày, 4 bóng đèn LED 15 W dùng 5 h/ngày. Tổng điện năng tiêu thụ trong một tháng (30 ngày) của các thiết bị trên xấp xỉ bằng:", [
                f"{vdc_e_month} kWh", f"{round(vdc_e_month * 1.5, 1)} kWh", f"{round(vdc_e_month * 0.7, 1)} kWh", f"250,0 kWh"
            ], 0, f"A_ngay = {vdc_e_day} kWh => A_thang = {vdc_e_month} kWh."),
            make_vdc(2, f"Đường dây tải điện đôi dài {5 + t} km bằng nhôm có điện trở tổng cộng R = {3.5 + t*0.5:.1f} Ω truyền tải công suất điện P = {100 + t*20} kW dưới hiệu điện thế U = 10 kV (10 000 V). Công suất tỏa nhiệt hao phí trên đường dây là:", [
                f"{round(((100 + t*20)*1000 / 10000)**2 * (3.5 + t*0.5) / 1000, 2)} kW",
                f"12,5 kW",
                f"0,5 kW",
                f"25,0 kW"
            ], 0, f"I = P / U = {round((100+t*20)*1000 / 10000, 1)} A. P_hp = I^2 * R = {round(((100 + t*20)*1000 / 10000)**2 * (3.5 + t*0.5) / 1000, 2)} kW."),
            make_vdc(3, f"Một bình nước nóng công suất {2500 + t*250} W đun {50 + t*10} lít nước từ 20°C lên 60°C. Biết c = 4200 J/(kg.K), D = 1000 kg/m3 và hiệu suất bình đạt {90 + t}%. Thời gian đun nước xấp xỉ bằng:", [
                f"{round((50 + t*10) * 4200 * 40 / ((2500 + t*250) * (90 + t)/100) / 60, 1)} phút",
                f"15,0 phút",
                f"90,0 phút",
                f"35,5 phút"
            ], 0, f"t = (m * c * Δt) / (P * H) / 60 = {round((50 + t*10) * 4200 * 40 / ((2500 + t*250) * (90 + t)/100) / 60, 1)} phút."),
            make_vdc(4, f"Một hệ thống pin mặt trời công suất {1.2 + t*0.2:.1f} kW nạp điện cho dàn acquy 24 V qua bộ điều khiển sạc có hiệu suất 92%. Dàn acquy có dung lượng {150 + t*25} Ah đang cạn 60%. Thời gian chiếu nắng liên tục tối thiểu để sạc đầy lượng điện đã cạn là:", [
                f"{round((24 * (150 + t*25) * 0.6) / ((1.2 + t*0.2) * 1000 * 0.92), 2)} giờ",
                f"5,5 giờ",
                f"1,2 giờ",
                f"8,0 giờ"
            ], 0, f"t = E_nap / P_nap = (24 * {(150+t*25)*0.6:.1f}) / ({(1.2+t*0.2)*1000*0.92:.1f}) = {round((24 * (150 + t*25) * 0.6) / ((1.2 + t*0.2) * 1000 * 0.92), 2)} giờ.")
        ]

        exams[f"{lrev_id}_test{t}"] = meta(lrev_id, lrev_name, t, p1, p2, p3, p4)

    return exams

if __name__ == "__main__":
    exams = get_c5_part2_exams()
    print(f"Total Chapter V Part 2 exams: {len(exams)}")
'''

target_path = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt\build_phys8_c5_part2.py"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(code)

print("build_phys8_c5_part2.py generated successfully.")
